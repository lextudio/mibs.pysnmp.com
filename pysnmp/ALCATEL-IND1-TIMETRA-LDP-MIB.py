# SNMP MIB module (ALCATEL-IND1-TIMETRA-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-LDP-MIB
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

(TFilterID,
 TFilterLogId) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-FILTER-MIB",
    "TFilterID",
    "TFilterLogId")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(SdpId,
 ServType,
 TdmOptionsCasTrunkFraming,
 TdmOptionsSigPkts) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-SERV-MIB",
    "SdpId",
    "ServType",
    "TdmOptionsCasTrunkFraming",
    "TdmOptionsSigPkts")

(TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxOperState,
 TmnxServId,
 TmnxVRtrMplsLspID,
 TmnxVcId,
 TmnxVcType) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxOperState",
    "TmnxServId",
    "TmnxVRtrMplsLspID",
    "TmnxVcId",
    "TmnxVcType")

(vRtrID,
 vRtrLdpStatus) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrLdpStatus")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(MplsLdpIdentifier,
 MplsLsrIdentifier) = mibBuilder.importSymbols(
    "MPLS-LDP-MIB",
    "MplsLdpIdentifier",
    "MplsLsrIdentifier")

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
 TestAndIncr,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

timetraLdpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 8)
)
timetraLdpMIBModule.setRevisions(
        ("1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-16 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1901-08-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxLdpKeepAliveFactor(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxLdpKeepAliveTimeout(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxLdpHelloFactor(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxLdpHelloTimeout(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxLdpBackoffTime(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2592000),
    )



class TmnxLdpFECPolicy(Integer32, TextualConvention):
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
        *(("all", 3),
          ("interface", 2),
          ("none", 4),
          ("system", 1))
    )



class TmnxLdpLabelDistMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstreamOnDemand", 1),
          ("downstreamUnsolicited", 2))
    )



class TmnxLdpAdjacencyType(Integer32, TextualConvention):
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
          ("link", 1),
          ("targeted", 2))
    )



class TmnxVpnId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )



class TmnxLabelStatus(Bits, TextualConvention):
    status = "current"


class TmnxLabelSigStatus(Unsigned32, TextualConvention):
    status = "current"


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



class TmnxLdpFECFlags(Bits, TextualConvention):
    status = "current"


class TmnxLdpGenOperDownReasonCode(Integer32, TextualConvention):
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
        *(("adminDown", 1),
          ("clearDown", 8),
          ("iomFailure", 6),
          ("noDiscoverySocket", 3),
          ("noListenSocket", 2),
          ("noResources", 9),
          ("noRtm", 4),
          ("noTtm", 5),
          ("operUp", 0),
          ("recvFailure", 7),
          ("systemIpDown", 10))
    )



class TmnxLdpIntTargOperDownReasonCode(Integer32, TextualConvention):
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
        *(("addrFecDeprogram", 5),
          ("adminDown", 1),
          ("clearDown", 7),
          ("instanceDown", 8),
          ("interfaceDown", 9),
          ("interfaceInvalid", 11),
          ("noDiscoverySocket", 3),
          ("noListenSocket", 2),
          ("noResources", 4),
          ("operUp", 0),
          ("svcFecDeprogram", 6),
          ("targetIpInvalid", 10))
    )



class TmnxLdpFec129Tlv(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxLdpConformance_ObjectIdentity = ObjectIdentity
tmnxLdpConformance = _TmnxLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8)
)
_TmnxLdpCompliances_ObjectIdentity = ObjectIdentity
tmnxLdpCompliances = _TmnxLdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1)
)
_TmnxLdpGroups_ObjectIdentity = ObjectIdentity
tmnxLdpGroups = _TmnxLdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2)
)
_TmnxLdpObjs_ObjectIdentity = ObjectIdentity
tmnxLdpObjs = _TmnxLdpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8)
)
_VRtrLdpGeneralTable_Object = MibTable
vRtrLdpGeneralTable = _VRtrLdpGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpGeneralTable.setStatus("current")
_VRtrLdpGeneralEntry_Object = MibTableRow
vRtrLdpGeneralEntry = _VRtrLdpGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1)
)
vRtrLdpGeneralEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrLdpGeneralEntry.setStatus("current")
_VRtrLdpGenLastChange_Type = TimeStamp
_VRtrLdpGenLastChange_Object = MibTableColumn
vRtrLdpGenLastChange = _VRtrLdpGenLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 1),
    _VRtrLdpGenLastChange_Type()
)
vRtrLdpGenLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenLastChange.setStatus("current")


class _VRtrLdpGenAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpGenAdminState based on TmnxAdminState"""


_VRtrLdpGenAdminState_Object = MibTableColumn
vRtrLdpGenAdminState = _VRtrLdpGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 2),
    _VRtrLdpGenAdminState_Type()
)
vRtrLdpGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenAdminState.setStatus("current")
_VRtrLdpGenOperState_Type = TmnxOperState
_VRtrLdpGenOperState_Object = MibTableColumn
vRtrLdpGenOperState = _VRtrLdpGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 3),
    _VRtrLdpGenOperState_Type()
)
vRtrLdpGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenOperState.setStatus("current")
_VRtrLdpGenLdpLsrId_Type = MplsLsrIdentifier
_VRtrLdpGenLdpLsrId_Object = MibTableColumn
vRtrLdpGenLdpLsrId = _VRtrLdpGenLdpLsrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 4),
    _VRtrLdpGenLdpLsrId_Type()
)
vRtrLdpGenLdpLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenLdpLsrId.setStatus("current")
_VRtrLdpGenProtocolVersion_Type = Unsigned32
_VRtrLdpGenProtocolVersion_Object = MibTableColumn
vRtrLdpGenProtocolVersion = _VRtrLdpGenProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 5),
    _VRtrLdpGenProtocolVersion_Type()
)
vRtrLdpGenProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenProtocolVersion.setStatus("current")


class _VRtrLdpGenDeaggregateFec_Type(TruthValue):
    """Custom type vRtrLdpGenDeaggregateFec based on TruthValue"""


_VRtrLdpGenDeaggregateFec_Object = MibTableColumn
vRtrLdpGenDeaggregateFec = _VRtrLdpGenDeaggregateFec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 6),
    _VRtrLdpGenDeaggregateFec_Type()
)
vRtrLdpGenDeaggregateFec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenDeaggregateFec.setStatus("current")


class _VRtrLdpGenKeepAliveFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpGenKeepAliveFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 3


_VRtrLdpGenKeepAliveFactor_Object = MibTableColumn
vRtrLdpGenKeepAliveFactor = _VRtrLdpGenKeepAliveFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 7),
    _VRtrLdpGenKeepAliveFactor_Type()
)
vRtrLdpGenKeepAliveFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenKeepAliveFactor.setStatus("current")


class _VRtrLdpGenKeepAliveTimeout_Type(TmnxLdpKeepAliveTimeout):
    """Custom type vRtrLdpGenKeepAliveTimeout based on TmnxLdpKeepAliveTimeout"""
    defaultValue = 30


_VRtrLdpGenKeepAliveTimeout_Object = MibTableColumn
vRtrLdpGenKeepAliveTimeout = _VRtrLdpGenKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 8),
    _VRtrLdpGenKeepAliveTimeout_Type()
)
vRtrLdpGenKeepAliveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenKeepAliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpGenKeepAliveTimeout.setUnits("seconds")


class _VRtrLdpGenHelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpGenHelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpGenHelloFactor_Object = MibTableColumn
vRtrLdpGenHelloFactor = _VRtrLdpGenHelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 9),
    _VRtrLdpGenHelloFactor_Type()
)
vRtrLdpGenHelloFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenHelloFactor.setStatus("current")


class _VRtrLdpGenHelloTimeout_Type(TmnxLdpHelloTimeout):
    """Custom type vRtrLdpGenHelloTimeout based on TmnxLdpHelloTimeout"""
    defaultValue = 15


_VRtrLdpGenHelloTimeout_Object = MibTableColumn
vRtrLdpGenHelloTimeout = _VRtrLdpGenHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 10),
    _VRtrLdpGenHelloTimeout_Type()
)
vRtrLdpGenHelloTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenHelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpGenHelloTimeout.setUnits("seconds")


class _VRtrLdpGenRoutePreference_Type(Unsigned32):
    """Custom type vRtrLdpGenRoutePreference based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrLdpGenRoutePreference_Type.__name__ = "Unsigned32"
_VRtrLdpGenRoutePreference_Object = MibTableColumn
vRtrLdpGenRoutePreference = _VRtrLdpGenRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 11),
    _VRtrLdpGenRoutePreference_Type()
)
vRtrLdpGenRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenRoutePreference.setStatus("current")


class _VRtrLdpGenControlMode_Type(Integer32):
    """Custom type vRtrLdpGenControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 2),
          ("ordered", 1))
    )


_VRtrLdpGenControlMode_Type.__name__ = "Integer32"
_VRtrLdpGenControlMode_Object = MibTableColumn
vRtrLdpGenControlMode = _VRtrLdpGenControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 12),
    _VRtrLdpGenControlMode_Type()
)
vRtrLdpGenControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenControlMode.setStatus("current")
_VRtrLdpGenDistMethod_Type = TmnxLdpLabelDistMethod
_VRtrLdpGenDistMethod_Object = MibTableColumn
vRtrLdpGenDistMethod = _VRtrLdpGenDistMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 13),
    _VRtrLdpGenDistMethod_Type()
)
vRtrLdpGenDistMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenDistMethod.setStatus("current")


class _VRtrLdpGenRetentionMode_Type(Integer32):
    """Custom type vRtrLdpGenRetentionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conservative", 1),
          ("liberal", 2))
    )


_VRtrLdpGenRetentionMode_Type.__name__ = "Integer32"
_VRtrLdpGenRetentionMode_Object = MibTableColumn
vRtrLdpGenRetentionMode = _VRtrLdpGenRetentionMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 14),
    _VRtrLdpGenRetentionMode_Type()
)
vRtrLdpGenRetentionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenRetentionMode.setStatus("current")


class _VRtrLdpGenTransportAddrType_Type(Integer32):
    """Custom type vRtrLdpGenTransportAddrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("system", 2))
    )


_VRtrLdpGenTransportAddrType_Type.__name__ = "Integer32"
_VRtrLdpGenTransportAddrType_Object = MibTableColumn
vRtrLdpGenTransportAddrType = _VRtrLdpGenTransportAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 15),
    _VRtrLdpGenTransportAddrType_Type()
)
vRtrLdpGenTransportAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTransportAddrType.setStatus("current")


class _VRtrLdpGenPropagatePolicy_Type(TmnxLdpFECPolicy):
    """Custom type vRtrLdpGenPropagatePolicy based on TmnxLdpFECPolicy"""


_VRtrLdpGenPropagatePolicy_Object = MibTableColumn
vRtrLdpGenPropagatePolicy = _VRtrLdpGenPropagatePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 16),
    _VRtrLdpGenPropagatePolicy_Type()
)
vRtrLdpGenPropagatePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenPropagatePolicy.setStatus("current")


class _VRtrLdpGenLoopDetectCapable_Type(Integer32):
    """Custom type vRtrLdpGenLoopDetectCapable based on Integer32"""
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
        *(("hopCount", 3),
          ("hopCountAndPathVector", 5),
          ("none", 1),
          ("other", 2),
          ("pathVector", 4))
    )


_VRtrLdpGenLoopDetectCapable_Type.__name__ = "Integer32"
_VRtrLdpGenLoopDetectCapable_Object = MibTableColumn
vRtrLdpGenLoopDetectCapable = _VRtrLdpGenLoopDetectCapable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 17),
    _VRtrLdpGenLoopDetectCapable_Type()
)
vRtrLdpGenLoopDetectCapable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenLoopDetectCapable.setStatus("current")


class _VRtrLdpGenHopLimit_Type(Unsigned32):
    """Custom type vRtrLdpGenHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpGenHopLimit_Type.__name__ = "Unsigned32"
_VRtrLdpGenHopLimit_Object = MibTableColumn
vRtrLdpGenHopLimit = _VRtrLdpGenHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 18),
    _VRtrLdpGenHopLimit_Type()
)
vRtrLdpGenHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenHopLimit.setStatus("current")


class _VRtrLdpGenPathVectorLimit_Type(Unsigned32):
    """Custom type vRtrLdpGenPathVectorLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpGenPathVectorLimit_Type.__name__ = "Unsigned32"
_VRtrLdpGenPathVectorLimit_Object = MibTableColumn
vRtrLdpGenPathVectorLimit = _VRtrLdpGenPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 19),
    _VRtrLdpGenPathVectorLimit_Type()
)
vRtrLdpGenPathVectorLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenPathVectorLimit.setStatus("current")


class _VRtrLdpGenBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpGenBackoffTime based on TmnxLdpBackoffTime"""
    defaultValue = 15

    subtypeSpec = TmnxLdpBackoffTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2592000),
    )


_VRtrLdpGenBackoffTime_Type.__name__ = "TmnxLdpBackoffTime"
_VRtrLdpGenBackoffTime_Object = MibTableColumn
vRtrLdpGenBackoffTime = _VRtrLdpGenBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 20),
    _VRtrLdpGenBackoffTime_Type()
)
vRtrLdpGenBackoffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpGenBackoffTime.setUnits("seconds")


class _VRtrLdpGenMaxBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpGenMaxBackoffTime based on TmnxLdpBackoffTime"""
    defaultValue = 120


_VRtrLdpGenMaxBackoffTime_Object = MibTableColumn
vRtrLdpGenMaxBackoffTime = _VRtrLdpGenMaxBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 21),
    _VRtrLdpGenMaxBackoffTime_Type()
)
vRtrLdpGenMaxBackoffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenMaxBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpGenMaxBackoffTime.setUnits("seconds")


class _VRtrLdpGenTargKeepAliveFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpGenTargKeepAliveFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 4


_VRtrLdpGenTargKeepAliveFactor_Object = MibTableColumn
vRtrLdpGenTargKeepAliveFactor = _VRtrLdpGenTargKeepAliveFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 22),
    _VRtrLdpGenTargKeepAliveFactor_Type()
)
vRtrLdpGenTargKeepAliveFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargKeepAliveFactor.setStatus("current")


class _VRtrLdpGenTargKeepAliveTimeout_Type(TmnxLdpKeepAliveTimeout):
    """Custom type vRtrLdpGenTargKeepAliveTimeout based on TmnxLdpKeepAliveTimeout"""
    defaultValue = 40


_VRtrLdpGenTargKeepAliveTimeout_Object = MibTableColumn
vRtrLdpGenTargKeepAliveTimeout = _VRtrLdpGenTargKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 23),
    _VRtrLdpGenTargKeepAliveTimeout_Type()
)
vRtrLdpGenTargKeepAliveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargKeepAliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpGenTargKeepAliveTimeout.setUnits("seconds")


class _VRtrLdpGenTargHelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpGenTargHelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpGenTargHelloFactor_Object = MibTableColumn
vRtrLdpGenTargHelloFactor = _VRtrLdpGenTargHelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 24),
    _VRtrLdpGenTargHelloFactor_Type()
)
vRtrLdpGenTargHelloFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargHelloFactor.setStatus("current")


class _VRtrLdpGenTargHelloTimeout_Type(TmnxLdpHelloTimeout):
    """Custom type vRtrLdpGenTargHelloTimeout based on TmnxLdpHelloTimeout"""
    defaultValue = 45


_VRtrLdpGenTargHelloTimeout_Object = MibTableColumn
vRtrLdpGenTargHelloTimeout = _VRtrLdpGenTargHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 25),
    _VRtrLdpGenTargHelloTimeout_Type()
)
vRtrLdpGenTargHelloTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargHelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpGenTargHelloTimeout.setUnits("seconds")


class _VRtrLdpGenTargPassiveMode_Type(TruthValue):
    """Custom type vRtrLdpGenTargPassiveMode based on TruthValue"""


_VRtrLdpGenTargPassiveMode_Object = MibTableColumn
vRtrLdpGenTargPassiveMode = _VRtrLdpGenTargPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 26),
    _VRtrLdpGenTargPassiveMode_Type()
)
vRtrLdpGenTargPassiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargPassiveMode.setStatus("current")


class _VRtrLdpGenTargetedSessions_Type(TruthValue):
    """Custom type vRtrLdpGenTargetedSessions based on TruthValue"""


_VRtrLdpGenTargetedSessions_Object = MibTableColumn
vRtrLdpGenTargetedSessions = _VRtrLdpGenTargetedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 27),
    _VRtrLdpGenTargetedSessions_Type()
)
vRtrLdpGenTargetedSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTargetedSessions.setStatus("current")
_VRtrLdpGenCreateTime_Type = TimeStamp
_VRtrLdpGenCreateTime_Object = MibTableColumn
vRtrLdpGenCreateTime = _VRtrLdpGenCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 28),
    _VRtrLdpGenCreateTime_Type()
)
vRtrLdpGenCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenCreateTime.setStatus("current")
_VRtrLdpGenUpTime_Type = TimeInterval
_VRtrLdpGenUpTime_Object = MibTableColumn
vRtrLdpGenUpTime = _VRtrLdpGenUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 29),
    _VRtrLdpGenUpTime_Type()
)
vRtrLdpGenUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenUpTime.setStatus("current")


class _VRtrLdpGenImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenImportPolicy1_Object = MibTableColumn
vRtrLdpGenImportPolicy1 = _VRtrLdpGenImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 30),
    _VRtrLdpGenImportPolicy1_Type()
)
vRtrLdpGenImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImportPolicy1.setStatus("current")


class _VRtrLdpGenImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenImportPolicy2_Object = MibTableColumn
vRtrLdpGenImportPolicy2 = _VRtrLdpGenImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 31),
    _VRtrLdpGenImportPolicy2_Type()
)
vRtrLdpGenImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImportPolicy2.setStatus("current")


class _VRtrLdpGenImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenImportPolicy3_Object = MibTableColumn
vRtrLdpGenImportPolicy3 = _VRtrLdpGenImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 32),
    _VRtrLdpGenImportPolicy3_Type()
)
vRtrLdpGenImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImportPolicy3.setStatus("current")


class _VRtrLdpGenImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenImportPolicy4_Object = MibTableColumn
vRtrLdpGenImportPolicy4 = _VRtrLdpGenImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 33),
    _VRtrLdpGenImportPolicy4_Type()
)
vRtrLdpGenImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImportPolicy4.setStatus("current")


class _VRtrLdpGenImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenImportPolicy5_Object = MibTableColumn
vRtrLdpGenImportPolicy5 = _VRtrLdpGenImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 34),
    _VRtrLdpGenImportPolicy5_Type()
)
vRtrLdpGenImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenImportPolicy5.setStatus("current")


class _VRtrLdpGenExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenExportPolicy1_Object = MibTableColumn
vRtrLdpGenExportPolicy1 = _VRtrLdpGenExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 35),
    _VRtrLdpGenExportPolicy1_Type()
)
vRtrLdpGenExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenExportPolicy1.setStatus("current")


class _VRtrLdpGenExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenExportPolicy2_Object = MibTableColumn
vRtrLdpGenExportPolicy2 = _VRtrLdpGenExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 36),
    _VRtrLdpGenExportPolicy2_Type()
)
vRtrLdpGenExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenExportPolicy2.setStatus("current")


class _VRtrLdpGenExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenExportPolicy3_Object = MibTableColumn
vRtrLdpGenExportPolicy3 = _VRtrLdpGenExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 37),
    _VRtrLdpGenExportPolicy3_Type()
)
vRtrLdpGenExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenExportPolicy3.setStatus("current")


class _VRtrLdpGenExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenExportPolicy4_Object = MibTableColumn
vRtrLdpGenExportPolicy4 = _VRtrLdpGenExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 38),
    _VRtrLdpGenExportPolicy4_Type()
)
vRtrLdpGenExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenExportPolicy4.setStatus("current")


class _VRtrLdpGenExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpGenExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpGenExportPolicy5_Object = MibTableColumn
vRtrLdpGenExportPolicy5 = _VRtrLdpGenExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 39),
    _VRtrLdpGenExportPolicy5_Type()
)
vRtrLdpGenExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenExportPolicy5.setStatus("current")


class _VRtrLdpGenTunnelDownDampTime_Type(Unsigned32):
    """Custom type vRtrLdpGenTunnelDownDampTime based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_VRtrLdpGenTunnelDownDampTime_Type.__name__ = "Unsigned32"
_VRtrLdpGenTunnelDownDampTime_Object = MibTableColumn
vRtrLdpGenTunnelDownDampTime = _VRtrLdpGenTunnelDownDampTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 40),
    _VRtrLdpGenTunnelDownDampTime_Type()
)
vRtrLdpGenTunnelDownDampTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTunnelDownDampTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpGenTunnelDownDampTime.setUnits("seconds")
_VRtrLdpGenOperDownReason_Type = TmnxLdpGenOperDownReasonCode
_VRtrLdpGenOperDownReason_Object = MibTableColumn
vRtrLdpGenOperDownReason = _VRtrLdpGenOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 41),
    _VRtrLdpGenOperDownReason_Type()
)
vRtrLdpGenOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpGenOperDownReason.setStatus("current")


class _VRtrLdpGenTrustList_Type(TFilterID):
    """Custom type vRtrLdpGenTrustList based on TFilterID"""
    defaultValue = 0


_VRtrLdpGenTrustList_Object = MibTableColumn
vRtrLdpGenTrustList = _VRtrLdpGenTrustList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 42),
    _VRtrLdpGenTrustList_Type()
)
vRtrLdpGenTrustList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenTrustList.setStatus("obsolete")


class _VRtrLdpGenGracefulRestart_Type(TruthValue):
    """Custom type vRtrLdpGenGracefulRestart based on TruthValue"""


_VRtrLdpGenGracefulRestart_Object = MibTableColumn
vRtrLdpGenGracefulRestart = _VRtrLdpGenGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 43),
    _VRtrLdpGenGracefulRestart_Type()
)
vRtrLdpGenGracefulRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenGracefulRestart.setStatus("current")


class _VRtrLdpGenGRNbrLiveTime_Type(Unsigned32):
    """Custom type vRtrLdpGenGRNbrLiveTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_VRtrLdpGenGRNbrLiveTime_Type.__name__ = "Unsigned32"
_VRtrLdpGenGRNbrLiveTime_Object = MibTableColumn
vRtrLdpGenGRNbrLiveTime = _VRtrLdpGenGRNbrLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 44),
    _VRtrLdpGenGRNbrLiveTime_Type()
)
vRtrLdpGenGRNbrLiveTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenGRNbrLiveTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpGenGRNbrLiveTime.setUnits("seconds")


class _VRtrLdpGenGRMaxRecoveryTime_Type(Unsigned32):
    """Custom type vRtrLdpGenGRMaxRecoveryTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1800),
    )


_VRtrLdpGenGRMaxRecoveryTime_Type.__name__ = "Unsigned32"
_VRtrLdpGenGRMaxRecoveryTime_Object = MibTableColumn
vRtrLdpGenGRMaxRecoveryTime = _VRtrLdpGenGRMaxRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 1, 1, 45),
    _VRtrLdpGenGRMaxRecoveryTime_Type()
)
vRtrLdpGenGRMaxRecoveryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpGenGRMaxRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpGenGRMaxRecoveryTime.setUnits("seconds")
_VRtrLdpStatsTable_Object = MibTable
vRtrLdpStatsTable = _VRtrLdpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    vRtrLdpStatsTable.setStatus("current")
_VRtrLdpStatsEntry_Object = MibTableRow
vRtrLdpStatsEntry = _VRtrLdpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpStatsEntry.setStatus("current")
_VRtrLdpStatsOperDownEvents_Type = Counter32
_VRtrLdpStatsOperDownEvents_Object = MibTableColumn
vRtrLdpStatsOperDownEvents = _VRtrLdpStatsOperDownEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 1),
    _VRtrLdpStatsOperDownEvents_Type()
)
vRtrLdpStatsOperDownEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsOperDownEvents.setStatus("current")
_VRtrLdpStatsActiveSessions_Type = Gauge32
_VRtrLdpStatsActiveSessions_Object = MibTableColumn
vRtrLdpStatsActiveSessions = _VRtrLdpStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 2),
    _VRtrLdpStatsActiveSessions_Type()
)
vRtrLdpStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsActiveSessions.setStatus("current")
_VRtrLdpStatsActiveAdjacencies_Type = Gauge32
_VRtrLdpStatsActiveAdjacencies_Object = MibTableColumn
vRtrLdpStatsActiveAdjacencies = _VRtrLdpStatsActiveAdjacencies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 3),
    _VRtrLdpStatsActiveAdjacencies_Type()
)
vRtrLdpStatsActiveAdjacencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsActiveAdjacencies.setStatus("current")
_VRtrLdpStatsActiveInterfaces_Type = Gauge32
_VRtrLdpStatsActiveInterfaces_Object = MibTableColumn
vRtrLdpStatsActiveInterfaces = _VRtrLdpStatsActiveInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 4),
    _VRtrLdpStatsActiveInterfaces_Type()
)
vRtrLdpStatsActiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsActiveInterfaces.setStatus("current")
_VRtrLdpStatsInactiveInterfaces_Type = Gauge32
_VRtrLdpStatsInactiveInterfaces_Object = MibTableColumn
vRtrLdpStatsInactiveInterfaces = _VRtrLdpStatsInactiveInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 5),
    _VRtrLdpStatsInactiveInterfaces_Type()
)
vRtrLdpStatsInactiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsInactiveInterfaces.setStatus("current")
_VRtrLdpStatsActiveTargSessions_Type = Gauge32
_VRtrLdpStatsActiveTargSessions_Object = MibTableColumn
vRtrLdpStatsActiveTargSessions = _VRtrLdpStatsActiveTargSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 6),
    _VRtrLdpStatsActiveTargSessions_Type()
)
vRtrLdpStatsActiveTargSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsActiveTargSessions.setStatus("current")
_VRtrLdpStatsInactiveTargSessions_Type = Gauge32
_VRtrLdpStatsInactiveTargSessions_Object = MibTableColumn
vRtrLdpStatsInactiveTargSessions = _VRtrLdpStatsInactiveTargSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 7),
    _VRtrLdpStatsInactiveTargSessions_Type()
)
vRtrLdpStatsInactiveTargSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsInactiveTargSessions.setStatus("current")
_VRtrLdpStatsAddrFECRecv_Type = Gauge32
_VRtrLdpStatsAddrFECRecv_Object = MibTableColumn
vRtrLdpStatsAddrFECRecv = _VRtrLdpStatsAddrFECRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 8),
    _VRtrLdpStatsAddrFECRecv_Type()
)
vRtrLdpStatsAddrFECRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsAddrFECRecv.setStatus("current")
_VRtrLdpStatsAddrFECSent_Type = Gauge32
_VRtrLdpStatsAddrFECSent_Object = MibTableColumn
vRtrLdpStatsAddrFECSent = _VRtrLdpStatsAddrFECSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 9),
    _VRtrLdpStatsAddrFECSent_Type()
)
vRtrLdpStatsAddrFECSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsAddrFECSent.setStatus("current")
_VRtrLdpStatsSvcFECRecv_Type = Gauge32
_VRtrLdpStatsSvcFECRecv_Object = MibTableColumn
vRtrLdpStatsSvcFECRecv = _VRtrLdpStatsSvcFECRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 10),
    _VRtrLdpStatsSvcFECRecv_Type()
)
vRtrLdpStatsSvcFECRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSvcFECRecv.setStatus("current")
_VRtrLdpStatsSvcFECSent_Type = Gauge32
_VRtrLdpStatsSvcFECSent_Object = MibTableColumn
vRtrLdpStatsSvcFECSent = _VRtrLdpStatsSvcFECSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 11),
    _VRtrLdpStatsSvcFECSent_Type()
)
vRtrLdpStatsSvcFECSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSvcFECSent.setStatus("current")
_VRtrLdpStatsAttemptedSessions_Type = Counter32
_VRtrLdpStatsAttemptedSessions_Object = MibTableColumn
vRtrLdpStatsAttemptedSessions = _VRtrLdpStatsAttemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 12),
    _VRtrLdpStatsAttemptedSessions_Type()
)
vRtrLdpStatsAttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsAttemptedSessions.setStatus("current")
_VRtrLdpStatsSessRejNoHelloErrors_Type = Counter32
_VRtrLdpStatsSessRejNoHelloErrors_Object = MibTableColumn
vRtrLdpStatsSessRejNoHelloErrors = _VRtrLdpStatsSessRejNoHelloErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 13),
    _VRtrLdpStatsSessRejNoHelloErrors_Type()
)
vRtrLdpStatsSessRejNoHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSessRejNoHelloErrors.setStatus("current")
_VRtrLdpStatsSessRejAdvErrors_Type = Counter32
_VRtrLdpStatsSessRejAdvErrors_Object = MibTableColumn
vRtrLdpStatsSessRejAdvErrors = _VRtrLdpStatsSessRejAdvErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 14),
    _VRtrLdpStatsSessRejAdvErrors_Type()
)
vRtrLdpStatsSessRejAdvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSessRejAdvErrors.setStatus("current")
_VRtrLdpStatsSessRejMaxPduErrors_Type = Counter32
_VRtrLdpStatsSessRejMaxPduErrors_Object = MibTableColumn
vRtrLdpStatsSessRejMaxPduErrors = _VRtrLdpStatsSessRejMaxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 15),
    _VRtrLdpStatsSessRejMaxPduErrors_Type()
)
vRtrLdpStatsSessRejMaxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSessRejMaxPduErrors.setStatus("current")
_VRtrLdpStatsSessRejLabelRangeErrors_Type = Counter32
_VRtrLdpStatsSessRejLabelRangeErrors_Object = MibTableColumn
vRtrLdpStatsSessRejLabelRangeErrors = _VRtrLdpStatsSessRejLabelRangeErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 16),
    _VRtrLdpStatsSessRejLabelRangeErrors_Type()
)
vRtrLdpStatsSessRejLabelRangeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsSessRejLabelRangeErrors.setStatus("current")
_VRtrLdpStatsBadLdpIdentifierErrors_Type = Counter32
_VRtrLdpStatsBadLdpIdentifierErrors_Object = MibTableColumn
vRtrLdpStatsBadLdpIdentifierErrors = _VRtrLdpStatsBadLdpIdentifierErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 17),
    _VRtrLdpStatsBadLdpIdentifierErrors_Type()
)
vRtrLdpStatsBadLdpIdentifierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsBadLdpIdentifierErrors.setStatus("current")
_VRtrLdpStatsBadPduLengthErrors_Type = Counter32
_VRtrLdpStatsBadPduLengthErrors_Object = MibTableColumn
vRtrLdpStatsBadPduLengthErrors = _VRtrLdpStatsBadPduLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 18),
    _VRtrLdpStatsBadPduLengthErrors_Type()
)
vRtrLdpStatsBadPduLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsBadPduLengthErrors.setStatus("current")
_VRtrLdpStatsBadMessageLengthErrors_Type = Counter32
_VRtrLdpStatsBadMessageLengthErrors_Object = MibTableColumn
vRtrLdpStatsBadMessageLengthErrors = _VRtrLdpStatsBadMessageLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 19),
    _VRtrLdpStatsBadMessageLengthErrors_Type()
)
vRtrLdpStatsBadMessageLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsBadMessageLengthErrors.setStatus("current")
_VRtrLdpStatsBadTlvLengthErrors_Type = Counter32
_VRtrLdpStatsBadTlvLengthErrors_Object = MibTableColumn
vRtrLdpStatsBadTlvLengthErrors = _VRtrLdpStatsBadTlvLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 20),
    _VRtrLdpStatsBadTlvLengthErrors_Type()
)
vRtrLdpStatsBadTlvLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsBadTlvLengthErrors.setStatus("current")
_VRtrLdpStatsMalformedTlvValueErrors_Type = Counter32
_VRtrLdpStatsMalformedTlvValueErrors_Object = MibTableColumn
vRtrLdpStatsMalformedTlvValueErrors = _VRtrLdpStatsMalformedTlvValueErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 21),
    _VRtrLdpStatsMalformedTlvValueErrors_Type()
)
vRtrLdpStatsMalformedTlvValueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsMalformedTlvValueErrors.setStatus("current")
_VRtrLdpStatsKeepAliveExpiredErrors_Type = Counter32
_VRtrLdpStatsKeepAliveExpiredErrors_Object = MibTableColumn
vRtrLdpStatsKeepAliveExpiredErrors = _VRtrLdpStatsKeepAliveExpiredErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 22),
    _VRtrLdpStatsKeepAliveExpiredErrors_Type()
)
vRtrLdpStatsKeepAliveExpiredErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsKeepAliveExpiredErrors.setStatus("current")
_VRtrLdpStatsShutdownNotifRecv_Type = Counter32
_VRtrLdpStatsShutdownNotifRecv_Object = MibTableColumn
vRtrLdpStatsShutdownNotifRecv = _VRtrLdpStatsShutdownNotifRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 23),
    _VRtrLdpStatsShutdownNotifRecv_Type()
)
vRtrLdpStatsShutdownNotifRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsShutdownNotifRecv.setStatus("current")
_VRtrLdpStatsShutdownNotifSent_Type = Counter32
_VRtrLdpStatsShutdownNotifSent_Object = MibTableColumn
vRtrLdpStatsShutdownNotifSent = _VRtrLdpStatsShutdownNotifSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 2, 1, 24),
    _VRtrLdpStatsShutdownNotifSent_Type()
)
vRtrLdpStatsShutdownNotifSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStatsShutdownNotifSent.setStatus("current")
_VRtrLdpPolicyTable_Object = MibTable
vRtrLdpPolicyTable = _VRtrLdpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    vRtrLdpPolicyTable.setStatus("obsolete")
_VRtrLdpPolicyEntry_Object = MibTableRow
vRtrLdpPolicyEntry = _VRtrLdpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3, 1)
)
vRtrLdpPolicyEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPolicyType"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPolicyIndex"),
)
if mibBuilder.loadTexts:
    vRtrLdpPolicyEntry.setStatus("obsolete")


class _VRtrLdpPolicyType_Type(Integer32):
    """Custom type vRtrLdpPolicyType based on Integer32"""
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
        *(("egress", 4),
          ("export", 2),
          ("import", 1),
          ("ingress", 3))
    )


_VRtrLdpPolicyType_Type.__name__ = "Integer32"
_VRtrLdpPolicyType_Object = MibTableColumn
vRtrLdpPolicyType = _VRtrLdpPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3, 1, 1),
    _VRtrLdpPolicyType_Type()
)
vRtrLdpPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPolicyType.setStatus("obsolete")


class _VRtrLdpPolicyIndex_Type(Unsigned32):
    """Custom type vRtrLdpPolicyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_VRtrLdpPolicyIndex_Type.__name__ = "Unsigned32"
_VRtrLdpPolicyIndex_Object = MibTableColumn
vRtrLdpPolicyIndex = _VRtrLdpPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3, 1, 2),
    _VRtrLdpPolicyIndex_Type()
)
vRtrLdpPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPolicyIndex.setStatus("obsolete")
_VRtrLdpPolicyRowStatus_Type = RowStatus
_VRtrLdpPolicyRowStatus_Object = MibTableColumn
vRtrLdpPolicyRowStatus = _VRtrLdpPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3, 1, 3),
    _VRtrLdpPolicyRowStatus_Type()
)
vRtrLdpPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPolicyRowStatus.setStatus("obsolete")


class _VRtrLdpPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPolicyName_Object = MibTableColumn
vRtrLdpPolicyName = _VRtrLdpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 3, 1, 4),
    _VRtrLdpPolicyName_Type()
)
vRtrLdpPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPolicyName.setStatus("obsolete")


class _VRtrLdpIfTableSpinlock_Type(TestAndIncr):
    """Custom type vRtrLdpIfTableSpinlock based on TestAndIncr"""
    defaultValue = 0


_VRtrLdpIfTableSpinlock_Object = MibScalar
vRtrLdpIfTableSpinlock = _VRtrLdpIfTableSpinlock_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 4),
    _VRtrLdpIfTableSpinlock_Type()
)
vRtrLdpIfTableSpinlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpIfTableSpinlock.setStatus("current")
_VRtrLdpIfTable_Object = MibTable
vRtrLdpIfTable = _VRtrLdpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5)
)
if mibBuilder.loadTexts:
    vRtrLdpIfTable.setStatus("current")
_VRtrLdpIfEntry_Object = MibTableRow
vRtrLdpIfEntry = _VRtrLdpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1)
)
vRtrLdpIfEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfIndex"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpIfEntry.setStatus("current")
_VRtrLdpIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpIfIndex_Object = MibTableColumn
vRtrLdpIfIndex = _VRtrLdpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 1),
    _VRtrLdpIfIndex_Type()
)
vRtrLdpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpIfIndex.setStatus("current")
_VRtrLdpPeerAddress_Type = IpAddress
_VRtrLdpPeerAddress_Object = MibTableColumn
vRtrLdpPeerAddress = _VRtrLdpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 2),
    _VRtrLdpPeerAddress_Type()
)
vRtrLdpPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPeerAddress.setStatus("current")
_VRtrLdpIfRowStatus_Type = RowStatus
_VRtrLdpIfRowStatus_Object = MibTableColumn
vRtrLdpIfRowStatus = _VRtrLdpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 3),
    _VRtrLdpIfRowStatus_Type()
)
vRtrLdpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfRowStatus.setStatus("current")
_VRtrLdpIfLastChange_Type = TimeStamp
_VRtrLdpIfLastChange_Object = MibTableColumn
vRtrLdpIfLastChange = _VRtrLdpIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 4),
    _VRtrLdpIfLastChange_Type()
)
vRtrLdpIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfLastChange.setStatus("current")


class _VRtrLdpIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpIfAdminState based on TmnxAdminState"""


_VRtrLdpIfAdminState_Object = MibTableColumn
vRtrLdpIfAdminState = _VRtrLdpIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 5),
    _VRtrLdpIfAdminState_Type()
)
vRtrLdpIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfAdminState.setStatus("current")
_VRtrLdpIfOperState_Type = TmnxOperState
_VRtrLdpIfOperState_Object = MibTableColumn
vRtrLdpIfOperState = _VRtrLdpIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 6),
    _VRtrLdpIfOperState_Type()
)
vRtrLdpIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfOperState.setStatus("current")


class _VRtrLdpIfInheritance_Type(Unsigned32):
    """Custom type vRtrLdpIfInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrLdpIfInheritance_Object = MibTableColumn
vRtrLdpIfInheritance = _VRtrLdpIfInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 7),
    _VRtrLdpIfInheritance_Type()
)
vRtrLdpIfInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfInheritance.setStatus("current")


class _VRtrLdpIfKeepAliveFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpIfKeepAliveFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 3


_VRtrLdpIfKeepAliveFactor_Object = MibTableColumn
vRtrLdpIfKeepAliveFactor = _VRtrLdpIfKeepAliveFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 8),
    _VRtrLdpIfKeepAliveFactor_Type()
)
vRtrLdpIfKeepAliveFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfKeepAliveFactor.setStatus("current")


class _VRtrLdpIfKeepAliveTimeout_Type(TmnxLdpKeepAliveTimeout):
    """Custom type vRtrLdpIfKeepAliveTimeout based on TmnxLdpKeepAliveTimeout"""
    defaultValue = 30


_VRtrLdpIfKeepAliveTimeout_Object = MibTableColumn
vRtrLdpIfKeepAliveTimeout = _VRtrLdpIfKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 9),
    _VRtrLdpIfKeepAliveTimeout_Type()
)
vRtrLdpIfKeepAliveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfKeepAliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpIfKeepAliveTimeout.setUnits("seconds")


class _VRtrLdpIfHelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpIfHelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpIfHelloFactor_Object = MibTableColumn
vRtrLdpIfHelloFactor = _VRtrLdpIfHelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 10),
    _VRtrLdpIfHelloFactor_Type()
)
vRtrLdpIfHelloFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfHelloFactor.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpIfHelloFactor.setUnits("seconds")


class _VRtrLdpIfHelloTimeout_Type(TmnxLdpHelloTimeout):
    """Custom type vRtrLdpIfHelloTimeout based on TmnxLdpHelloTimeout"""
    defaultValue = 15


_VRtrLdpIfHelloTimeout_Object = MibTableColumn
vRtrLdpIfHelloTimeout = _VRtrLdpIfHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 11),
    _VRtrLdpIfHelloTimeout_Type()
)
vRtrLdpIfHelloTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfHelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpIfHelloTimeout.setUnits("seconds")


class _VRtrLdpIfBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpIfBackoffTime based on TmnxLdpBackoffTime"""
    defaultValue = 15

    subtypeSpec = TmnxLdpBackoffTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2592000),
    )


_VRtrLdpIfBackoffTime_Type.__name__ = "TmnxLdpBackoffTime"
_VRtrLdpIfBackoffTime_Object = MibTableColumn
vRtrLdpIfBackoffTime = _VRtrLdpIfBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 12),
    _VRtrLdpIfBackoffTime_Type()
)
vRtrLdpIfBackoffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpIfBackoffTime.setUnits("seconds")


class _VRtrLdpIfMaxBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpIfMaxBackoffTime based on TmnxLdpBackoffTime"""
    defaultValue = 120


_VRtrLdpIfMaxBackoffTime_Object = MibTableColumn
vRtrLdpIfMaxBackoffTime = _VRtrLdpIfMaxBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 13),
    _VRtrLdpIfMaxBackoffTime_Type()
)
vRtrLdpIfMaxBackoffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfMaxBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpIfMaxBackoffTime.setUnits("seconds")


class _VRtrLdpIfTransportAddrType_Type(Integer32):
    """Custom type vRtrLdpIfTransportAddrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("system", 2))
    )


_VRtrLdpIfTransportAddrType_Type.__name__ = "Integer32"
_VRtrLdpIfTransportAddrType_Object = MibTableColumn
vRtrLdpIfTransportAddrType = _VRtrLdpIfTransportAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 14),
    _VRtrLdpIfTransportAddrType_Type()
)
vRtrLdpIfTransportAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfTransportAddrType.setStatus("current")


class _VRtrLdpIfPassiveMode_Type(TruthValue):
    """Custom type vRtrLdpIfPassiveMode based on TruthValue"""


_VRtrLdpIfPassiveMode_Object = MibTableColumn
vRtrLdpIfPassiveMode = _VRtrLdpIfPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 15),
    _VRtrLdpIfPassiveMode_Type()
)
vRtrLdpIfPassiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfPassiveMode.setStatus("current")
_VRtrLdpIfAutoCreate_Type = TruthValue
_VRtrLdpIfAutoCreate_Object = MibTableColumn
vRtrLdpIfAutoCreate = _VRtrLdpIfAutoCreate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 16),
    _VRtrLdpIfAutoCreate_Type()
)
vRtrLdpIfAutoCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfAutoCreate.setStatus("current")
_VRtrLdpIfOperDownReason_Type = TmnxLdpIntTargOperDownReasonCode
_VRtrLdpIfOperDownReason_Object = MibTableColumn
vRtrLdpIfOperDownReason = _VRtrLdpIfOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 17),
    _VRtrLdpIfOperDownReason_Type()
)
vRtrLdpIfOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfOperDownReason.setStatus("current")


class _VRtrLdpIfTunneling_Type(TruthValue):
    """Custom type vRtrLdpIfTunneling based on TruthValue"""


_VRtrLdpIfTunneling_Object = MibTableColumn
vRtrLdpIfTunneling = _VRtrLdpIfTunneling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 5, 1, 18),
    _VRtrLdpIfTunneling_Type()
)
vRtrLdpIfTunneling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfTunneling.setStatus("current")
_VRtrLdpIfStatsTable_Object = MibTable
vRtrLdpIfStatsTable = _VRtrLdpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 6)
)
if mibBuilder.loadTexts:
    vRtrLdpIfStatsTable.setStatus("current")
_VRtrLdpIfStatsEntry_Object = MibTableRow
vRtrLdpIfStatsEntry = _VRtrLdpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpIfStatsEntry.setStatus("current")
_VRtrLdpIfExistingAdjacencies_Type = Gauge32
_VRtrLdpIfExistingAdjacencies_Object = MibTableColumn
vRtrLdpIfExistingAdjacencies = _VRtrLdpIfExistingAdjacencies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 6, 1, 1),
    _VRtrLdpIfExistingAdjacencies_Type()
)
vRtrLdpIfExistingAdjacencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpIfExistingAdjacencies.setStatus("current")
_VRtrLdpHelloAdjTable_Object = MibTable
vRtrLdpHelloAdjTable = _VRtrLdpHelloAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7)
)
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjTable.setStatus("current")
_VRtrLdpHelloAdjEntry_Object = MibTableRow
vRtrLdpHelloAdjEntry = _VRtrLdpHelloAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1)
)
vRtrLdpHelloAdjEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfIndex"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjEntry.setStatus("current")
_VRtrLdpPeerLdpId_Type = MplsLdpIdentifier
_VRtrLdpPeerLdpId_Object = MibTableColumn
vRtrLdpPeerLdpId = _VRtrLdpPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 1),
    _VRtrLdpPeerLdpId_Type()
)
vRtrLdpPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpPeerLdpId.setStatus("current")
_VRtrLdpHelloAdjLocalLdpId_Type = MplsLdpIdentifier
_VRtrLdpHelloAdjLocalLdpId_Object = MibTableColumn
vRtrLdpHelloAdjLocalLdpId = _VRtrLdpHelloAdjLocalLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 2),
    _VRtrLdpHelloAdjLocalLdpId_Type()
)
vRtrLdpHelloAdjLocalLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjLocalLdpId.setStatus("current")


class _VRtrLdpHelloAdjEntityIndex_Type(Unsigned32):
    """Custom type vRtrLdpHelloAdjEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpHelloAdjEntityIndex_Type.__name__ = "Unsigned32"
_VRtrLdpHelloAdjEntityIndex_Object = MibTableColumn
vRtrLdpHelloAdjEntityIndex = _VRtrLdpHelloAdjEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 3),
    _VRtrLdpHelloAdjEntityIndex_Type()
)
vRtrLdpHelloAdjEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjEntityIndex.setStatus("current")


class _VRtrLdpHelloAdjIndex_Type(Unsigned32):
    """Custom type vRtrLdpHelloAdjIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpHelloAdjIndex_Type.__name__ = "Unsigned32"
_VRtrLdpHelloAdjIndex_Object = MibTableColumn
vRtrLdpHelloAdjIndex = _VRtrLdpHelloAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 4),
    _VRtrLdpHelloAdjIndex_Type()
)
vRtrLdpHelloAdjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjIndex.setStatus("current")
_VRtrLdpHelloAdjHoldTimeRemaining_Type = Unsigned32
_VRtrLdpHelloAdjHoldTimeRemaining_Object = MibTableColumn
vRtrLdpHelloAdjHoldTimeRemaining = _VRtrLdpHelloAdjHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 5),
    _VRtrLdpHelloAdjHoldTimeRemaining_Type()
)
vRtrLdpHelloAdjHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjHoldTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjHoldTimeRemaining.setUnits("seconds")
_VRtrLdpHelloAdjType_Type = TmnxLdpAdjacencyType
_VRtrLdpHelloAdjType_Object = MibTableColumn
vRtrLdpHelloAdjType = _VRtrLdpHelloAdjType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 6),
    _VRtrLdpHelloAdjType_Type()
)
vRtrLdpHelloAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjType.setStatus("current")
_VRtrLdpHelloAdjRemoteConfSeqNum_Type = Unsigned32
_VRtrLdpHelloAdjRemoteConfSeqNum_Object = MibTableColumn
vRtrLdpHelloAdjRemoteConfSeqNum = _VRtrLdpHelloAdjRemoteConfSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 7),
    _VRtrLdpHelloAdjRemoteConfSeqNum_Type()
)
vRtrLdpHelloAdjRemoteConfSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjRemoteConfSeqNum.setStatus("current")
_VRtrLdpHelloAdjRemoteIpAddress_Type = IpAddress
_VRtrLdpHelloAdjRemoteIpAddress_Object = MibTableColumn
vRtrLdpHelloAdjRemoteIpAddress = _VRtrLdpHelloAdjRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 8),
    _VRtrLdpHelloAdjRemoteIpAddress_Type()
)
vRtrLdpHelloAdjRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjRemoteIpAddress.setStatus("current")
_VRtrLdpHelloAdjUpTime_Type = TimeInterval
_VRtrLdpHelloAdjUpTime_Object = MibTableColumn
vRtrLdpHelloAdjUpTime = _VRtrLdpHelloAdjUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 9),
    _VRtrLdpHelloAdjUpTime_Type()
)
vRtrLdpHelloAdjUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjUpTime.setStatus("current")
_VRtrLdpHelloAdjLocalConfSeqNum_Type = Unsigned32
_VRtrLdpHelloAdjLocalConfSeqNum_Object = MibTableColumn
vRtrLdpHelloAdjLocalConfSeqNum = _VRtrLdpHelloAdjLocalConfSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 10),
    _VRtrLdpHelloAdjLocalConfSeqNum_Type()
)
vRtrLdpHelloAdjLocalConfSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjLocalConfSeqNum.setStatus("current")
_VRtrLdpHelloAdjLocalIpAddress_Type = IpAddress
_VRtrLdpHelloAdjLocalIpAddress_Object = MibTableColumn
vRtrLdpHelloAdjLocalIpAddress = _VRtrLdpHelloAdjLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 11),
    _VRtrLdpHelloAdjLocalIpAddress_Type()
)
vRtrLdpHelloAdjLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjLocalIpAddress.setStatus("current")
_VRtrLdpHelloAdjInHelloMsgCount_Type = Counter32
_VRtrLdpHelloAdjInHelloMsgCount_Object = MibTableColumn
vRtrLdpHelloAdjInHelloMsgCount = _VRtrLdpHelloAdjInHelloMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 12),
    _VRtrLdpHelloAdjInHelloMsgCount_Type()
)
vRtrLdpHelloAdjInHelloMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjInHelloMsgCount.setStatus("current")
_VRtrLdpHelloAdjOutHelloMsgCount_Type = Counter32
_VRtrLdpHelloAdjOutHelloMsgCount_Object = MibTableColumn
vRtrLdpHelloAdjOutHelloMsgCount = _VRtrLdpHelloAdjOutHelloMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 13),
    _VRtrLdpHelloAdjOutHelloMsgCount_Type()
)
vRtrLdpHelloAdjOutHelloMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjOutHelloMsgCount.setStatus("current")
_VRtrLdpHelloAdjLocalHelloTimeout_Type = TmnxLdpHelloTimeout
_VRtrLdpHelloAdjLocalHelloTimeout_Object = MibTableColumn
vRtrLdpHelloAdjLocalHelloTimeout = _VRtrLdpHelloAdjLocalHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 14),
    _VRtrLdpHelloAdjLocalHelloTimeout_Type()
)
vRtrLdpHelloAdjLocalHelloTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjLocalHelloTimeout.setStatus("current")
_VRtrLdpHelloAdjRemoteHelloTimeout_Type = TmnxLdpHelloTimeout
_VRtrLdpHelloAdjRemoteHelloTimeout_Object = MibTableColumn
vRtrLdpHelloAdjRemoteHelloTimeout = _VRtrLdpHelloAdjRemoteHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 7, 1, 15),
    _VRtrLdpHelloAdjRemoteHelloTimeout_Type()
)
vRtrLdpHelloAdjRemoteHelloTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjRemoteHelloTimeout.setStatus("current")
_VRtrLdpHelloAdjMapTable_Object = MibTable
vRtrLdpHelloAdjMapTable = _VRtrLdpHelloAdjMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 8)
)
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjMapTable.setStatus("current")
_VRtrLdpHelloAdjMapEntry_Object = MibTableRow
vRtrLdpHelloAdjMapEntry = _VRtrLdpHelloAdjMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 8, 1)
)
vRtrLdpHelloAdjMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfIndex"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerAddress"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjMapLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjMapEntry.setStatus("current")
_VRtrLdpHelloAdjMapLdpId_Type = MplsLdpIdentifier
_VRtrLdpHelloAdjMapLdpId_Object = MibTableColumn
vRtrLdpHelloAdjMapLdpId = _VRtrLdpHelloAdjMapLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 8, 1, 1),
    _VRtrLdpHelloAdjMapLdpId_Type()
)
vRtrLdpHelloAdjMapLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpHelloAdjMapLdpId.setStatus("current")
_VRtrLdpSessionTable_Object = MibTable
vRtrLdpSessionTable = _VRtrLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9)
)
if mibBuilder.loadTexts:
    vRtrLdpSessionTable.setStatus("current")
_VRtrLdpSessionEntry_Object = MibTableRow
vRtrLdpSessionEntry = _VRtrLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1)
)
vRtrLdpSessionEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpSessionEntry.setStatus("current")
_VRtrLdpSessLocalLdpId_Type = MplsLdpIdentifier
_VRtrLdpSessLocalLdpId_Object = MibTableColumn
vRtrLdpSessLocalLdpId = _VRtrLdpSessLocalLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 1),
    _VRtrLdpSessLocalLdpId_Type()
)
vRtrLdpSessLocalLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLocalLdpId.setStatus("current")


class _VRtrLdpSessEntityIndex_Type(Unsigned32):
    """Custom type vRtrLdpSessEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpSessEntityIndex_Type.__name__ = "Unsigned32"
_VRtrLdpSessEntityIndex_Object = MibTableColumn
vRtrLdpSessEntityIndex = _VRtrLdpSessEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 2),
    _VRtrLdpSessEntityIndex_Type()
)
vRtrLdpSessEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessEntityIndex.setStatus("current")
_VRtrLdpSessLabelDistMethod_Type = TmnxLdpLabelDistMethod
_VRtrLdpSessLabelDistMethod_Object = MibTableColumn
vRtrLdpSessLabelDistMethod = _VRtrLdpSessLabelDistMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 3),
    _VRtrLdpSessLabelDistMethod_Type()
)
vRtrLdpSessLabelDistMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLabelDistMethod.setStatus("current")


class _VRtrLdpSessLoopDetectForPV_Type(Integer32):
    """Custom type vRtrLdpSessLoopDetectForPV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VRtrLdpSessLoopDetectForPV_Type.__name__ = "Integer32"
_VRtrLdpSessLoopDetectForPV_Object = MibTableColumn
vRtrLdpSessLoopDetectForPV = _VRtrLdpSessLoopDetectForPV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 4),
    _VRtrLdpSessLoopDetectForPV_Type()
)
vRtrLdpSessLoopDetectForPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLoopDetectForPV.setStatus("current")


class _VRtrLdpSessPathVectorLimit_Type(Unsigned32):
    """Custom type vRtrLdpSessPathVectorLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpSessPathVectorLimit_Type.__name__ = "Unsigned32"
_VRtrLdpSessPathVectorLimit_Object = MibTableColumn
vRtrLdpSessPathVectorLimit = _VRtrLdpSessPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 5),
    _VRtrLdpSessPathVectorLimit_Type()
)
vRtrLdpSessPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPathVectorLimit.setStatus("current")


class _VRtrLdpSessState_Type(Integer32):
    """Custom type vRtrLdpSessState based on Integer32"""
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
        *(("initialized", 2),
          ("nonexistent", 1),
          ("openrec", 3),
          ("opensent", 4),
          ("operational", 5))
    )


_VRtrLdpSessState_Type.__name__ = "Integer32"
_VRtrLdpSessState_Object = MibTableColumn
vRtrLdpSessState = _VRtrLdpSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 6),
    _VRtrLdpSessState_Type()
)
vRtrLdpSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessState.setStatus("current")
_VRtrLdpSessAdjacencyType_Type = TmnxLdpAdjacencyType
_VRtrLdpSessAdjacencyType_Object = MibTableColumn
vRtrLdpSessAdjacencyType = _VRtrLdpSessAdjacencyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 7),
    _VRtrLdpSessAdjacencyType_Type()
)
vRtrLdpSessAdjacencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessAdjacencyType.setStatus("current")
_VRtrLdpSessProtocolVersion_Type = Unsigned32
_VRtrLdpSessProtocolVersion_Object = MibTableColumn
vRtrLdpSessProtocolVersion = _VRtrLdpSessProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 8),
    _VRtrLdpSessProtocolVersion_Type()
)
vRtrLdpSessProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessProtocolVersion.setStatus("current")


class _VRtrLdpSessLocalUdpPort_Type(Unsigned32):
    """Custom type vRtrLdpSessLocalUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpSessLocalUdpPort_Type.__name__ = "Unsigned32"
_VRtrLdpSessLocalUdpPort_Object = MibTableColumn
vRtrLdpSessLocalUdpPort = _VRtrLdpSessLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 9),
    _VRtrLdpSessLocalUdpPort_Type()
)
vRtrLdpSessLocalUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLocalUdpPort.setStatus("current")


class _VRtrLdpSessPeerUdpPort_Type(Unsigned32):
    """Custom type vRtrLdpSessPeerUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpSessPeerUdpPort_Type.__name__ = "Unsigned32"
_VRtrLdpSessPeerUdpPort_Object = MibTableColumn
vRtrLdpSessPeerUdpPort = _VRtrLdpSessPeerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 10),
    _VRtrLdpSessPeerUdpPort_Type()
)
vRtrLdpSessPeerUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPeerUdpPort.setStatus("current")


class _VRtrLdpSessLocalTcpPort_Type(Unsigned32):
    """Custom type vRtrLdpSessLocalTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpSessLocalTcpPort_Type.__name__ = "Unsigned32"
_VRtrLdpSessLocalTcpPort_Object = MibTableColumn
vRtrLdpSessLocalTcpPort = _VRtrLdpSessLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 11),
    _VRtrLdpSessLocalTcpPort_Type()
)
vRtrLdpSessLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLocalTcpPort.setStatus("current")


class _VRtrLdpSessPeerTcpPort_Type(Unsigned32):
    """Custom type vRtrLdpSessPeerTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpSessPeerTcpPort_Type.__name__ = "Unsigned32"
_VRtrLdpSessPeerTcpPort_Object = MibTableColumn
vRtrLdpSessPeerTcpPort = _VRtrLdpSessPeerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 12),
    _VRtrLdpSessPeerTcpPort_Type()
)
vRtrLdpSessPeerTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPeerTcpPort.setStatus("current")
_VRtrLdpSessLocalAddress_Type = IpAddress
_VRtrLdpSessLocalAddress_Object = MibTableColumn
vRtrLdpSessLocalAddress = _VRtrLdpSessLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 13),
    _VRtrLdpSessLocalAddress_Type()
)
vRtrLdpSessLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLocalAddress.setStatus("current")
_VRtrLdpSessPeerAddress_Type = IpAddress
_VRtrLdpSessPeerAddress_Object = MibTableColumn
vRtrLdpSessPeerAddress = _VRtrLdpSessPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 14),
    _VRtrLdpSessPeerAddress_Type()
)
vRtrLdpSessPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPeerAddress.setStatus("current")
_VRtrLdpSessKAHoldTimeRemaining_Type = TimeInterval
_VRtrLdpSessKAHoldTimeRemaining_Object = MibTableColumn
vRtrLdpSessKAHoldTimeRemaining = _VRtrLdpSessKAHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 15),
    _VRtrLdpSessKAHoldTimeRemaining_Type()
)
vRtrLdpSessKAHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessKAHoldTimeRemaining.setStatus("current")


class _VRtrLdpSessMaxPduLength_Type(Unsigned32):
    """Custom type vRtrLdpSessMaxPduLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrLdpSessMaxPduLength_Type.__name__ = "Unsigned32"
_VRtrLdpSessMaxPduLength_Object = MibTableColumn
vRtrLdpSessMaxPduLength = _VRtrLdpSessMaxPduLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 16),
    _VRtrLdpSessMaxPduLength_Type()
)
vRtrLdpSessMaxPduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessMaxPduLength.setStatus("current")
_VRtrLdpSessUpTime_Type = TimeInterval
_VRtrLdpSessUpTime_Object = MibTableColumn
vRtrLdpSessUpTime = _VRtrLdpSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 17),
    _VRtrLdpSessUpTime_Type()
)
vRtrLdpSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessUpTime.setStatus("current")
_VRtrLdpSessLocalKATimeout_Type = TmnxLdpKeepAliveTimeout
_VRtrLdpSessLocalKATimeout_Object = MibTableColumn
vRtrLdpSessLocalKATimeout = _VRtrLdpSessLocalKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 18),
    _VRtrLdpSessLocalKATimeout_Type()
)
vRtrLdpSessLocalKATimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLocalKATimeout.setStatus("current")
_VRtrLdpSessPeerKATimeout_Type = TmnxLdpKeepAliveTimeout
_VRtrLdpSessPeerKATimeout_Object = MibTableColumn
vRtrLdpSessPeerKATimeout = _VRtrLdpSessPeerKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 19),
    _VRtrLdpSessPeerKATimeout_Type()
)
vRtrLdpSessPeerKATimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPeerKATimeout.setStatus("current")


class _VRtrLdpSessAdvertise_Type(Integer32):
    """Custom type vRtrLdpSessAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("address", 1),
          ("addressAndService", 3),
          ("service", 2))
    )


_VRtrLdpSessAdvertise_Type.__name__ = "Integer32"
_VRtrLdpSessAdvertise_Object = MibTableColumn
vRtrLdpSessAdvertise = _VRtrLdpSessAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 20),
    _VRtrLdpSessAdvertise_Type()
)
vRtrLdpSessAdvertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessAdvertise.setStatus("current")
_VRtrLdpSessRestartHelperState_Type = TruthValue
_VRtrLdpSessRestartHelperState_Object = MibTableColumn
vRtrLdpSessRestartHelperState = _VRtrLdpSessRestartHelperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 21),
    _VRtrLdpSessRestartHelperState_Type()
)
vRtrLdpSessRestartHelperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessRestartHelperState.setStatus("current")
_VRtrLdpSessPeerNumRestart_Type = Counter32
_VRtrLdpSessPeerNumRestart_Object = MibTableColumn
vRtrLdpSessPeerNumRestart = _VRtrLdpSessPeerNumRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 22),
    _VRtrLdpSessPeerNumRestart_Type()
)
vRtrLdpSessPeerNumRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessPeerNumRestart.setStatus("current")
_VRtrLdpSessLastRestartTime_Type = TimeStamp
_VRtrLdpSessLastRestartTime_Object = MibTableColumn
vRtrLdpSessLastRestartTime = _VRtrLdpSessLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 23),
    _VRtrLdpSessLastRestartTime_Type()
)
vRtrLdpSessLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessLastRestartTime.setStatus("current")
_VRtrLdpSessFtReconnectTimeNego_Type = Unsigned32
_VRtrLdpSessFtReconnectTimeNego_Object = MibTableColumn
vRtrLdpSessFtReconnectTimeNego = _VRtrLdpSessFtReconnectTimeNego_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 24),
    _VRtrLdpSessFtReconnectTimeNego_Type()
)
vRtrLdpSessFtReconnectTimeNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessFtReconnectTimeNego.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpSessFtReconnectTimeNego.setUnits("seconds")
_VRtrLdpSessFtRecoveryTimeNego_Type = Unsigned32
_VRtrLdpSessFtRecoveryTimeNego_Object = MibTableColumn
vRtrLdpSessFtRecoveryTimeNego = _VRtrLdpSessFtRecoveryTimeNego_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 25),
    _VRtrLdpSessFtRecoveryTimeNego_Type()
)
vRtrLdpSessFtRecoveryTimeNego.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessFtRecoveryTimeNego.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpSessFtRecoveryTimeNego.setUnits("seconds")
_VRtrLdpSessFtReconTimeRemaining_Type = Unsigned32
_VRtrLdpSessFtReconTimeRemaining_Object = MibTableColumn
vRtrLdpSessFtReconTimeRemaining = _VRtrLdpSessFtReconTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 26),
    _VRtrLdpSessFtReconTimeRemaining_Type()
)
vRtrLdpSessFtReconTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessFtReconTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpSessFtReconTimeRemaining.setUnits("seconds")
_VRtrLdpSessFtRecovTimeRemaining_Type = Unsigned32
_VRtrLdpSessFtRecovTimeRemaining_Object = MibTableColumn
vRtrLdpSessFtRecovTimeRemaining = _VRtrLdpSessFtRecovTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 9, 1, 27),
    _VRtrLdpSessFtRecovTimeRemaining_Type()
)
vRtrLdpSessFtRecovTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessFtRecovTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpSessFtRecovTimeRemaining.setUnits("seconds")
_VRtrLdpSessionStatsTable_Object = MibTable
vRtrLdpSessionStatsTable = _VRtrLdpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10)
)
if mibBuilder.loadTexts:
    vRtrLdpSessionStatsTable.setStatus("current")
_VRtrLdpSessionStatsEntry_Object = MibTableRow
vRtrLdpSessionStatsEntry = _VRtrLdpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpSessionStatsEntry.setStatus("current")
_VRtrLdpSessStatsTargAdj_Type = Gauge32
_VRtrLdpSessStatsTargAdj_Object = MibTableColumn
vRtrLdpSessStatsTargAdj = _VRtrLdpSessStatsTargAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 1),
    _VRtrLdpSessStatsTargAdj_Type()
)
vRtrLdpSessStatsTargAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsTargAdj.setStatus("current")
_VRtrLdpSessStatsLinkAdj_Type = Gauge32
_VRtrLdpSessStatsLinkAdj_Object = MibTableColumn
vRtrLdpSessStatsLinkAdj = _VRtrLdpSessStatsLinkAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 2),
    _VRtrLdpSessStatsLinkAdj_Type()
)
vRtrLdpSessStatsLinkAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLinkAdj.setStatus("current")
_VRtrLdpSessStatsFECRecv_Type = Counter32
_VRtrLdpSessStatsFECRecv_Object = MibTableColumn
vRtrLdpSessStatsFECRecv = _VRtrLdpSessStatsFECRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 3),
    _VRtrLdpSessStatsFECRecv_Type()
)
vRtrLdpSessStatsFECRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsFECRecv.setStatus("current")
_VRtrLdpSessStatsFECSent_Type = Counter32
_VRtrLdpSessStatsFECSent_Object = MibTableColumn
vRtrLdpSessStatsFECSent = _VRtrLdpSessStatsFECSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 4),
    _VRtrLdpSessStatsFECSent_Type()
)
vRtrLdpSessStatsFECSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsFECSent.setStatus("current")
_VRtrLdpSessStatsHelloIn_Type = Counter32
_VRtrLdpSessStatsHelloIn_Object = MibTableColumn
vRtrLdpSessStatsHelloIn = _VRtrLdpSessStatsHelloIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 5),
    _VRtrLdpSessStatsHelloIn_Type()
)
vRtrLdpSessStatsHelloIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsHelloIn.setStatus("current")
_VRtrLdpSessStatsHelloOut_Type = Counter32
_VRtrLdpSessStatsHelloOut_Object = MibTableColumn
vRtrLdpSessStatsHelloOut = _VRtrLdpSessStatsHelloOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 6),
    _VRtrLdpSessStatsHelloOut_Type()
)
vRtrLdpSessStatsHelloOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsHelloOut.setStatus("current")
_VRtrLdpSessStatsKeepaliveIn_Type = Counter32
_VRtrLdpSessStatsKeepaliveIn_Object = MibTableColumn
vRtrLdpSessStatsKeepaliveIn = _VRtrLdpSessStatsKeepaliveIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 7),
    _VRtrLdpSessStatsKeepaliveIn_Type()
)
vRtrLdpSessStatsKeepaliveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsKeepaliveIn.setStatus("current")
_VRtrLdpSessStatsKeepaliveOut_Type = Counter32
_VRtrLdpSessStatsKeepaliveOut_Object = MibTableColumn
vRtrLdpSessStatsKeepaliveOut = _VRtrLdpSessStatsKeepaliveOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 8),
    _VRtrLdpSessStatsKeepaliveOut_Type()
)
vRtrLdpSessStatsKeepaliveOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsKeepaliveOut.setStatus("current")
_VRtrLdpSessStatsInitIn_Type = Counter32
_VRtrLdpSessStatsInitIn_Object = MibTableColumn
vRtrLdpSessStatsInitIn = _VRtrLdpSessStatsInitIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 9),
    _VRtrLdpSessStatsInitIn_Type()
)
vRtrLdpSessStatsInitIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsInitIn.setStatus("current")
_VRtrLdpSessStatsInitOut_Type = Counter32
_VRtrLdpSessStatsInitOut_Object = MibTableColumn
vRtrLdpSessStatsInitOut = _VRtrLdpSessStatsInitOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 10),
    _VRtrLdpSessStatsInitOut_Type()
)
vRtrLdpSessStatsInitOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsInitOut.setStatus("current")
_VRtrLdpSessStatsLabelMappingIn_Type = Counter32
_VRtrLdpSessStatsLabelMappingIn_Object = MibTableColumn
vRtrLdpSessStatsLabelMappingIn = _VRtrLdpSessStatsLabelMappingIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 11),
    _VRtrLdpSessStatsLabelMappingIn_Type()
)
vRtrLdpSessStatsLabelMappingIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelMappingIn.setStatus("current")
_VRtrLdpSessStatsLabelMappingOut_Type = Counter32
_VRtrLdpSessStatsLabelMappingOut_Object = MibTableColumn
vRtrLdpSessStatsLabelMappingOut = _VRtrLdpSessStatsLabelMappingOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 12),
    _VRtrLdpSessStatsLabelMappingOut_Type()
)
vRtrLdpSessStatsLabelMappingOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelMappingOut.setStatus("current")
_VRtrLdpSessStatsLabelRequestIn_Type = Counter32
_VRtrLdpSessStatsLabelRequestIn_Object = MibTableColumn
vRtrLdpSessStatsLabelRequestIn = _VRtrLdpSessStatsLabelRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 13),
    _VRtrLdpSessStatsLabelRequestIn_Type()
)
vRtrLdpSessStatsLabelRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelRequestIn.setStatus("current")
_VRtrLdpSessStatsLabelRequestOut_Type = Counter32
_VRtrLdpSessStatsLabelRequestOut_Object = MibTableColumn
vRtrLdpSessStatsLabelRequestOut = _VRtrLdpSessStatsLabelRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 14),
    _VRtrLdpSessStatsLabelRequestOut_Type()
)
vRtrLdpSessStatsLabelRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelRequestOut.setStatus("current")
_VRtrLdpSessStatsLabelReleaseIn_Type = Counter32
_VRtrLdpSessStatsLabelReleaseIn_Object = MibTableColumn
vRtrLdpSessStatsLabelReleaseIn = _VRtrLdpSessStatsLabelReleaseIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 15),
    _VRtrLdpSessStatsLabelReleaseIn_Type()
)
vRtrLdpSessStatsLabelReleaseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelReleaseIn.setStatus("current")
_VRtrLdpSessStatsLabelReleaseOut_Type = Counter32
_VRtrLdpSessStatsLabelReleaseOut_Object = MibTableColumn
vRtrLdpSessStatsLabelReleaseOut = _VRtrLdpSessStatsLabelReleaseOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 16),
    _VRtrLdpSessStatsLabelReleaseOut_Type()
)
vRtrLdpSessStatsLabelReleaseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelReleaseOut.setStatus("current")
_VRtrLdpSessStatsLabelWithdrawIn_Type = Counter32
_VRtrLdpSessStatsLabelWithdrawIn_Object = MibTableColumn
vRtrLdpSessStatsLabelWithdrawIn = _VRtrLdpSessStatsLabelWithdrawIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 17),
    _VRtrLdpSessStatsLabelWithdrawIn_Type()
)
vRtrLdpSessStatsLabelWithdrawIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelWithdrawIn.setStatus("current")
_VRtrLdpSessStatsLabelWithdrawOut_Type = Counter32
_VRtrLdpSessStatsLabelWithdrawOut_Object = MibTableColumn
vRtrLdpSessStatsLabelWithdrawOut = _VRtrLdpSessStatsLabelWithdrawOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 18),
    _VRtrLdpSessStatsLabelWithdrawOut_Type()
)
vRtrLdpSessStatsLabelWithdrawOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelWithdrawOut.setStatus("current")
_VRtrLdpSessStatsLabelAbortIn_Type = Counter32
_VRtrLdpSessStatsLabelAbortIn_Object = MibTableColumn
vRtrLdpSessStatsLabelAbortIn = _VRtrLdpSessStatsLabelAbortIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 19),
    _VRtrLdpSessStatsLabelAbortIn_Type()
)
vRtrLdpSessStatsLabelAbortIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelAbortIn.setStatus("current")
_VRtrLdpSessStatsLabelAbortOut_Type = Counter32
_VRtrLdpSessStatsLabelAbortOut_Object = MibTableColumn
vRtrLdpSessStatsLabelAbortOut = _VRtrLdpSessStatsLabelAbortOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 20),
    _VRtrLdpSessStatsLabelAbortOut_Type()
)
vRtrLdpSessStatsLabelAbortOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsLabelAbortOut.setStatus("current")
_VRtrLdpSessStatsAddrIn_Type = Counter32
_VRtrLdpSessStatsAddrIn_Object = MibTableColumn
vRtrLdpSessStatsAddrIn = _VRtrLdpSessStatsAddrIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 21),
    _VRtrLdpSessStatsAddrIn_Type()
)
vRtrLdpSessStatsAddrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsAddrIn.setStatus("current")
_VRtrLdpSessStatsAddrOut_Type = Counter32
_VRtrLdpSessStatsAddrOut_Object = MibTableColumn
vRtrLdpSessStatsAddrOut = _VRtrLdpSessStatsAddrOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 22),
    _VRtrLdpSessStatsAddrOut_Type()
)
vRtrLdpSessStatsAddrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsAddrOut.setStatus("current")
_VRtrLdpSessStatsAddrWithdrawIn_Type = Counter32
_VRtrLdpSessStatsAddrWithdrawIn_Object = MibTableColumn
vRtrLdpSessStatsAddrWithdrawIn = _VRtrLdpSessStatsAddrWithdrawIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 23),
    _VRtrLdpSessStatsAddrWithdrawIn_Type()
)
vRtrLdpSessStatsAddrWithdrawIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsAddrWithdrawIn.setStatus("current")
_VRtrLdpSessStatsAddrWithdrawOut_Type = Counter32
_VRtrLdpSessStatsAddrWithdrawOut_Object = MibTableColumn
vRtrLdpSessStatsAddrWithdrawOut = _VRtrLdpSessStatsAddrWithdrawOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 24),
    _VRtrLdpSessStatsAddrWithdrawOut_Type()
)
vRtrLdpSessStatsAddrWithdrawOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsAddrWithdrawOut.setStatus("current")
_VRtrLdpSessStatsNotificationIn_Type = Counter32
_VRtrLdpSessStatsNotificationIn_Object = MibTableColumn
vRtrLdpSessStatsNotificationIn = _VRtrLdpSessStatsNotificationIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 25),
    _VRtrLdpSessStatsNotificationIn_Type()
)
vRtrLdpSessStatsNotificationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsNotificationIn.setStatus("current")
_VRtrLdpSessStatsNotificationOut_Type = Counter32
_VRtrLdpSessStatsNotificationOut_Object = MibTableColumn
vRtrLdpSessStatsNotificationOut = _VRtrLdpSessStatsNotificationOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 10, 1, 26),
    _VRtrLdpSessStatsNotificationOut_Type()
)
vRtrLdpSessStatsNotificationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpSessStatsNotificationOut.setStatus("current")
_VRtrLdpServFecTable_Object = MibTable
vRtrLdpServFecTable = _VRtrLdpServFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11)
)
if mibBuilder.loadTexts:
    vRtrLdpServFecTable.setStatus("current")
_VRtrLdpServFecEntry_Object = MibTableRow
vRtrLdpServFecEntry = _VRtrLdpServFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1)
)
vRtrLdpServFecEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecFecType"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecVcType"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecVcId"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpServFecEntry.setStatus("current")
_VRtrLdpServFecFecType_Type = TmnxLdpFECType
_VRtrLdpServFecFecType_Object = MibTableColumn
vRtrLdpServFecFecType = _VRtrLdpServFecFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 1),
    _VRtrLdpServFecFecType_Type()
)
vRtrLdpServFecFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpServFecFecType.setStatus("current")
_VRtrLdpServFecVcType_Type = TmnxVcType
_VRtrLdpServFecVcType_Object = MibTableColumn
vRtrLdpServFecVcType = _VRtrLdpServFecVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 2),
    _VRtrLdpServFecVcType_Type()
)
vRtrLdpServFecVcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpServFecVcType.setStatus("current")
_VRtrLdpServFecVcId_Type = TmnxVcId
_VRtrLdpServFecVcId_Object = MibTableColumn
vRtrLdpServFecVcId = _VRtrLdpServFecVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 3),
    _VRtrLdpServFecVcId_Type()
)
vRtrLdpServFecVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpServFecVcId.setStatus("current")
_VRtrLdpServFecServType_Type = ServType
_VRtrLdpServFecServType_Object = MibTableColumn
vRtrLdpServFecServType = _VRtrLdpServFecServType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 4),
    _VRtrLdpServFecServType_Type()
)
vRtrLdpServFecServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecServType.setStatus("current")


class _VRtrLdpServFecServId_Type(TmnxServId):
    """Custom type vRtrLdpServFecServId based on TmnxServId"""
    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrLdpServFecServId_Type.__name__ = "TmnxServId"
_VRtrLdpServFecServId_Object = MibTableColumn
vRtrLdpServFecServId = _VRtrLdpServFecServId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 5),
    _VRtrLdpServFecServId_Type()
)
vRtrLdpServFecServId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecServId.setStatus("current")
_VRtrLdpServFecVpnId_Type = TmnxVpnId
_VRtrLdpServFecVpnId_Object = MibTableColumn
vRtrLdpServFecVpnId = _VRtrLdpServFecVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 6),
    _VRtrLdpServFecVpnId_Type()
)
vRtrLdpServFecVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecVpnId.setStatus("current")
_VRtrLdpServFecFlags_Type = TmnxLdpFECFlags
_VRtrLdpServFecFlags_Object = MibTableColumn
vRtrLdpServFecFlags = _VRtrLdpServFecFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 7),
    _VRtrLdpServFecFlags_Type()
)
vRtrLdpServFecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecFlags.setStatus("current")
_VRtrLdpServFecNumInLabels_Type = Unsigned32
_VRtrLdpServFecNumInLabels_Object = MibTableColumn
vRtrLdpServFecNumInLabels = _VRtrLdpServFecNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 8),
    _VRtrLdpServFecNumInLabels_Type()
)
vRtrLdpServFecNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecNumInLabels.setStatus("current")
_VRtrLdpServFecNumOutLabels_Type = Unsigned32
_VRtrLdpServFecNumOutLabels_Object = MibTableColumn
vRtrLdpServFecNumOutLabels = _VRtrLdpServFecNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 9),
    _VRtrLdpServFecNumOutLabels_Type()
)
vRtrLdpServFecNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecNumOutLabels.setStatus("current")
_VRtrLdpServFecInLabel1_Type = Unsigned32
_VRtrLdpServFecInLabel1_Object = MibTableColumn
vRtrLdpServFecInLabel1 = _VRtrLdpServFecInLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 10),
    _VRtrLdpServFecInLabel1_Type()
)
vRtrLdpServFecInLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabel1.setStatus("current")
_VRtrLdpServFecInLabelStatus1_Type = TmnxLabelStatus
_VRtrLdpServFecInLabelStatus1_Object = MibTableColumn
vRtrLdpServFecInLabelStatus1 = _VRtrLdpServFecInLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 11),
    _VRtrLdpServFecInLabelStatus1_Type()
)
vRtrLdpServFecInLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelStatus1.setStatus("current")
_VRtrLdpServFecInLabel2_Type = Unsigned32
_VRtrLdpServFecInLabel2_Object = MibTableColumn
vRtrLdpServFecInLabel2 = _VRtrLdpServFecInLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 12),
    _VRtrLdpServFecInLabel2_Type()
)
vRtrLdpServFecInLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabel2.setStatus("current")
_VRtrLdpServFecInLabelStatus2_Type = TmnxLabelStatus
_VRtrLdpServFecInLabelStatus2_Object = MibTableColumn
vRtrLdpServFecInLabelStatus2 = _VRtrLdpServFecInLabelStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 13),
    _VRtrLdpServFecInLabelStatus2_Type()
)
vRtrLdpServFecInLabelStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelStatus2.setStatus("current")
_VRtrLdpServFecInLabel3_Type = Unsigned32
_VRtrLdpServFecInLabel3_Object = MibTableColumn
vRtrLdpServFecInLabel3 = _VRtrLdpServFecInLabel3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 14),
    _VRtrLdpServFecInLabel3_Type()
)
vRtrLdpServFecInLabel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabel3.setStatus("current")
_VRtrLdpServFecInLabelStatus3_Type = TmnxLabelStatus
_VRtrLdpServFecInLabelStatus3_Object = MibTableColumn
vRtrLdpServFecInLabelStatus3 = _VRtrLdpServFecInLabelStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 15),
    _VRtrLdpServFecInLabelStatus3_Type()
)
vRtrLdpServFecInLabelStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelStatus3.setStatus("current")
_VRtrLdpServFecInLabel4_Type = Unsigned32
_VRtrLdpServFecInLabel4_Object = MibTableColumn
vRtrLdpServFecInLabel4 = _VRtrLdpServFecInLabel4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 16),
    _VRtrLdpServFecInLabel4_Type()
)
vRtrLdpServFecInLabel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabel4.setStatus("current")
_VRtrLdpServFecInLabelStatus4_Type = TmnxLabelStatus
_VRtrLdpServFecInLabelStatus4_Object = MibTableColumn
vRtrLdpServFecInLabelStatus4 = _VRtrLdpServFecInLabelStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 17),
    _VRtrLdpServFecInLabelStatus4_Type()
)
vRtrLdpServFecInLabelStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelStatus4.setStatus("current")
_VRtrLdpServFecInLabel5_Type = Unsigned32
_VRtrLdpServFecInLabel5_Object = MibTableColumn
vRtrLdpServFecInLabel5 = _VRtrLdpServFecInLabel5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 18),
    _VRtrLdpServFecInLabel5_Type()
)
vRtrLdpServFecInLabel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabel5.setStatus("current")
_VRtrLdpServFecInLabelStatus5_Type = TmnxLabelStatus
_VRtrLdpServFecInLabelStatus5_Object = MibTableColumn
vRtrLdpServFecInLabelStatus5 = _VRtrLdpServFecInLabelStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 19),
    _VRtrLdpServFecInLabelStatus5_Type()
)
vRtrLdpServFecInLabelStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelStatus5.setStatus("current")
_VRtrLdpServFecOutLabel1_Type = Unsigned32
_VRtrLdpServFecOutLabel1_Object = MibTableColumn
vRtrLdpServFecOutLabel1 = _VRtrLdpServFecOutLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 20),
    _VRtrLdpServFecOutLabel1_Type()
)
vRtrLdpServFecOutLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabel1.setStatus("current")
_VRtrLdpServFecOutLabelStatus1_Type = TmnxLabelStatus
_VRtrLdpServFecOutLabelStatus1_Object = MibTableColumn
vRtrLdpServFecOutLabelStatus1 = _VRtrLdpServFecOutLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 21),
    _VRtrLdpServFecOutLabelStatus1_Type()
)
vRtrLdpServFecOutLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelStatus1.setStatus("current")
_VRtrLdpServFecOutLabel2_Type = Unsigned32
_VRtrLdpServFecOutLabel2_Object = MibTableColumn
vRtrLdpServFecOutLabel2 = _VRtrLdpServFecOutLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 22),
    _VRtrLdpServFecOutLabel2_Type()
)
vRtrLdpServFecOutLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabel2.setStatus("current")
_VRtrLdpServFecOutLabelStatus2_Type = TmnxLabelStatus
_VRtrLdpServFecOutLabelStatus2_Object = MibTableColumn
vRtrLdpServFecOutLabelStatus2 = _VRtrLdpServFecOutLabelStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 23),
    _VRtrLdpServFecOutLabelStatus2_Type()
)
vRtrLdpServFecOutLabelStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelStatus2.setStatus("current")
_VRtrLdpServFecOutLabel3_Type = Unsigned32
_VRtrLdpServFecOutLabel3_Object = MibTableColumn
vRtrLdpServFecOutLabel3 = _VRtrLdpServFecOutLabel3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 24),
    _VRtrLdpServFecOutLabel3_Type()
)
vRtrLdpServFecOutLabel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabel3.setStatus("current")
_VRtrLdpServFecOutLabelStatus3_Type = TmnxLabelStatus
_VRtrLdpServFecOutLabelStatus3_Object = MibTableColumn
vRtrLdpServFecOutLabelStatus3 = _VRtrLdpServFecOutLabelStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 25),
    _VRtrLdpServFecOutLabelStatus3_Type()
)
vRtrLdpServFecOutLabelStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelStatus3.setStatus("current")
_VRtrLdpServFecOutLabel4_Type = Unsigned32
_VRtrLdpServFecOutLabel4_Object = MibTableColumn
vRtrLdpServFecOutLabel4 = _VRtrLdpServFecOutLabel4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 26),
    _VRtrLdpServFecOutLabel4_Type()
)
vRtrLdpServFecOutLabel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabel4.setStatus("current")
_VRtrLdpServFecOutLabelStatus4_Type = TmnxLabelStatus
_VRtrLdpServFecOutLabelStatus4_Object = MibTableColumn
vRtrLdpServFecOutLabelStatus4 = _VRtrLdpServFecOutLabelStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 27),
    _VRtrLdpServFecOutLabelStatus4_Type()
)
vRtrLdpServFecOutLabelStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelStatus4.setStatus("current")
_VRtrLdpServFecOutLabel5_Type = Unsigned32
_VRtrLdpServFecOutLabel5_Object = MibTableColumn
vRtrLdpServFecOutLabel5 = _VRtrLdpServFecOutLabel5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 28),
    _VRtrLdpServFecOutLabel5_Type()
)
vRtrLdpServFecOutLabel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabel5.setStatus("current")
_VRtrLdpServFecOutLabelStatus5_Type = TmnxLabelStatus
_VRtrLdpServFecOutLabelStatus5_Object = MibTableColumn
vRtrLdpServFecOutLabelStatus5 = _VRtrLdpServFecOutLabelStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 29),
    _VRtrLdpServFecOutLabelStatus5_Type()
)
vRtrLdpServFecOutLabelStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelStatus5.setStatus("current")
_VRtrLdpServFecSdpId_Type = SdpId
_VRtrLdpServFecSdpId_Object = MibTableColumn
vRtrLdpServFecSdpId = _VRtrLdpServFecSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 30),
    _VRtrLdpServFecSdpId_Type()
)
vRtrLdpServFecSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecSdpId.setStatus("current")
_VRtrLdpServFecLocalMTU_Type = Unsigned32
_VRtrLdpServFecLocalMTU_Object = MibTableColumn
vRtrLdpServFecLocalMTU = _VRtrLdpServFecLocalMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 31),
    _VRtrLdpServFecLocalMTU_Type()
)
vRtrLdpServFecLocalMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalMTU.setStatus("current")
_VRtrLdpServFecRemoteMTU_Type = Unsigned32
_VRtrLdpServFecRemoteMTU_Object = MibTableColumn
vRtrLdpServFecRemoteMTU = _VRtrLdpServFecRemoteMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 32),
    _VRtrLdpServFecRemoteMTU_Type()
)
vRtrLdpServFecRemoteMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteMTU.setStatus("current")
_VRtrLdpServFecLocalVlanTag_Type = Unsigned32
_VRtrLdpServFecLocalVlanTag_Object = MibTableColumn
vRtrLdpServFecLocalVlanTag = _VRtrLdpServFecLocalVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 33),
    _VRtrLdpServFecLocalVlanTag_Type()
)
vRtrLdpServFecLocalVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalVlanTag.setStatus("current")
_VRtrLdpServFecRemoteVlanTag_Type = Unsigned32
_VRtrLdpServFecRemoteVlanTag_Object = MibTableColumn
vRtrLdpServFecRemoteVlanTag = _VRtrLdpServFecRemoteVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 34),
    _VRtrLdpServFecRemoteVlanTag_Type()
)
vRtrLdpServFecRemoteVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteVlanTag.setStatus("current")
_VRtrLdpServFecLocalMaxCellConcat_Type = Unsigned32
_VRtrLdpServFecLocalMaxCellConcat_Object = MibTableColumn
vRtrLdpServFecLocalMaxCellConcat = _VRtrLdpServFecLocalMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 35),
    _VRtrLdpServFecLocalMaxCellConcat_Type()
)
vRtrLdpServFecLocalMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecLocalMaxCellConcat.setStatus("current")
_VRtrLdpServFecRemoteMaxCellConcat_Type = Unsigned32
_VRtrLdpServFecRemoteMaxCellConcat_Object = MibTableColumn
vRtrLdpServFecRemoteMaxCellConcat = _VRtrLdpServFecRemoteMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 36),
    _VRtrLdpServFecRemoteMaxCellConcat_Type()
)
vRtrLdpServFecRemoteMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecRemoteMaxCellConcat.setStatus("current")
_VRtrLdpServFecInLabelSigStatus1_Type = TmnxLabelSigStatus
_VRtrLdpServFecInLabelSigStatus1_Object = MibTableColumn
vRtrLdpServFecInLabelSigStatus1 = _VRtrLdpServFecInLabelSigStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 37),
    _VRtrLdpServFecInLabelSigStatus1_Type()
)
vRtrLdpServFecInLabelSigStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelSigStatus1.setStatus("current")
_VRtrLdpServFecInLabelSigStatus2_Type = TmnxLabelSigStatus
_VRtrLdpServFecInLabelSigStatus2_Object = MibTableColumn
vRtrLdpServFecInLabelSigStatus2 = _VRtrLdpServFecInLabelSigStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 38),
    _VRtrLdpServFecInLabelSigStatus2_Type()
)
vRtrLdpServFecInLabelSigStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelSigStatus2.setStatus("current")
_VRtrLdpServFecInLabelSigStatus3_Type = TmnxLabelSigStatus
_VRtrLdpServFecInLabelSigStatus3_Object = MibTableColumn
vRtrLdpServFecInLabelSigStatus3 = _VRtrLdpServFecInLabelSigStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 39),
    _VRtrLdpServFecInLabelSigStatus3_Type()
)
vRtrLdpServFecInLabelSigStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelSigStatus3.setStatus("current")
_VRtrLdpServFecInLabelSigStatus4_Type = TmnxLabelSigStatus
_VRtrLdpServFecInLabelSigStatus4_Object = MibTableColumn
vRtrLdpServFecInLabelSigStatus4 = _VRtrLdpServFecInLabelSigStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 40),
    _VRtrLdpServFecInLabelSigStatus4_Type()
)
vRtrLdpServFecInLabelSigStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelSigStatus4.setStatus("current")
_VRtrLdpServFecInLabelSigStatus5_Type = TmnxLabelSigStatus
_VRtrLdpServFecInLabelSigStatus5_Object = MibTableColumn
vRtrLdpServFecInLabelSigStatus5 = _VRtrLdpServFecInLabelSigStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 41),
    _VRtrLdpServFecInLabelSigStatus5_Type()
)
vRtrLdpServFecInLabelSigStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecInLabelSigStatus5.setStatus("current")
_VRtrLdpServFecOutLabelSigStatus1_Type = TmnxLabelSigStatus
_VRtrLdpServFecOutLabelSigStatus1_Object = MibTableColumn
vRtrLdpServFecOutLabelSigStatus1 = _VRtrLdpServFecOutLabelSigStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 42),
    _VRtrLdpServFecOutLabelSigStatus1_Type()
)
vRtrLdpServFecOutLabelSigStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelSigStatus1.setStatus("current")
_VRtrLdpServFecOutLabelSigStatus2_Type = TmnxLabelSigStatus
_VRtrLdpServFecOutLabelSigStatus2_Object = MibTableColumn
vRtrLdpServFecOutLabelSigStatus2 = _VRtrLdpServFecOutLabelSigStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 43),
    _VRtrLdpServFecOutLabelSigStatus2_Type()
)
vRtrLdpServFecOutLabelSigStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelSigStatus2.setStatus("current")
_VRtrLdpServFecOutLabelSigStatus3_Type = TmnxLabelSigStatus
_VRtrLdpServFecOutLabelSigStatus3_Object = MibTableColumn
vRtrLdpServFecOutLabelSigStatus3 = _VRtrLdpServFecOutLabelSigStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 44),
    _VRtrLdpServFecOutLabelSigStatus3_Type()
)
vRtrLdpServFecOutLabelSigStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelSigStatus3.setStatus("current")
_VRtrLdpServFecOutLabelSigStatus4_Type = TmnxLabelSigStatus
_VRtrLdpServFecOutLabelSigStatus4_Object = MibTableColumn
vRtrLdpServFecOutLabelSigStatus4 = _VRtrLdpServFecOutLabelSigStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 45),
    _VRtrLdpServFecOutLabelSigStatus4_Type()
)
vRtrLdpServFecOutLabelSigStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelSigStatus4.setStatus("current")
_VRtrLdpServFecOutLabelSigStatus5_Type = TmnxLabelSigStatus
_VRtrLdpServFecOutLabelSigStatus5_Object = MibTableColumn
vRtrLdpServFecOutLabelSigStatus5 = _VRtrLdpServFecOutLabelSigStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 46),
    _VRtrLdpServFecOutLabelSigStatus5_Type()
)
vRtrLdpServFecOutLabelSigStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecOutLabelSigStatus5.setStatus("current")
_VRtrLdpServFecMateEndpointVcId_Type = TmnxVcId
_VRtrLdpServFecMateEndpointVcId_Object = MibTableColumn
vRtrLdpServFecMateEndpointVcId = _VRtrLdpServFecMateEndpointVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 47),
    _VRtrLdpServFecMateEndpointVcId_Type()
)
vRtrLdpServFecMateEndpointVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecMateEndpointVcId.setStatus("current")
_VRtrLdpServFecMateEndpointSdpId_Type = SdpId
_VRtrLdpServFecMateEndpointSdpId_Object = MibTableColumn
vRtrLdpServFecMateEndpointSdpId = _VRtrLdpServFecMateEndpointSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 11, 1, 48),
    _VRtrLdpServFecMateEndpointSdpId_Type()
)
vRtrLdpServFecMateEndpointSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecMateEndpointSdpId.setStatus("current")
_VRtrLdpServFecMapTable_Object = MibTable
vRtrLdpServFecMapTable = _VRtrLdpServFecMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 12)
)
if mibBuilder.loadTexts:
    vRtrLdpServFecMapTable.setStatus("obsolete")
_VRtrLdpServFecMapEntry_Object = MibTableRow
vRtrLdpServFecMapEntry = _VRtrLdpServFecMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 12, 1)
)
vRtrLdpServFecMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapFecType"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcType"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcId"),
)
if mibBuilder.loadTexts:
    vRtrLdpServFecMapEntry.setStatus("obsolete")
_VRtrLdpServFecMapFecType_Type = TmnxLdpFECType
_VRtrLdpServFecMapFecType_Object = MibTableColumn
vRtrLdpServFecMapFecType = _VRtrLdpServFecMapFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 12, 1, 1),
    _VRtrLdpServFecMapFecType_Type()
)
vRtrLdpServFecMapFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecMapFecType.setStatus("obsolete")
_VRtrLdpServFecMapVcType_Type = TmnxVcType
_VRtrLdpServFecMapVcType_Object = MibTableColumn
vRtrLdpServFecMapVcType = _VRtrLdpServFecMapVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 12, 1, 2),
    _VRtrLdpServFecMapVcType_Type()
)
vRtrLdpServFecMapVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecMapVcType.setStatus("obsolete")
_VRtrLdpServFecMapVcId_Type = TmnxVcId
_VRtrLdpServFecMapVcId_Object = MibTableColumn
vRtrLdpServFecMapVcId = _VRtrLdpServFecMapVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 12, 1, 3),
    _VRtrLdpServFecMapVcId_Type()
)
vRtrLdpServFecMapVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpServFecMapVcId.setStatus("obsolete")
_VRtrLdpAddrFecTable_Object = MibTable
vRtrLdpAddrFecTable = _VRtrLdpAddrFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13)
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecTable.setStatus("current")
_VRtrLdpAddrFecEntry_Object = MibTableRow
vRtrLdpAddrFecEntry = _VRtrLdpAddrFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1)
)
vRtrLdpAddrFecEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecFecType"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecIpPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecIpMask"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecEntry.setStatus("current")
_VRtrLdpAddrFecFecType_Type = TmnxLdpFECType
_VRtrLdpAddrFecFecType_Object = MibTableColumn
vRtrLdpAddrFecFecType = _VRtrLdpAddrFecFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 1),
    _VRtrLdpAddrFecFecType_Type()
)
vRtrLdpAddrFecFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecFecType.setStatus("current")
_VRtrLdpAddrFecIpPrefix_Type = IpAddress
_VRtrLdpAddrFecIpPrefix_Object = MibTableColumn
vRtrLdpAddrFecIpPrefix = _VRtrLdpAddrFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 2),
    _VRtrLdpAddrFecIpPrefix_Type()
)
vRtrLdpAddrFecIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecIpPrefix.setStatus("current")
_VRtrLdpAddrFecIpMask_Type = IpAddress
_VRtrLdpAddrFecIpMask_Object = MibTableColumn
vRtrLdpAddrFecIpMask = _VRtrLdpAddrFecIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 3),
    _VRtrLdpAddrFecIpMask_Type()
)
vRtrLdpAddrFecIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecIpMask.setStatus("current")
_VRtrLdpAddrFecFlags_Type = TmnxLdpFECFlags
_VRtrLdpAddrFecFlags_Object = MibTableColumn
vRtrLdpAddrFecFlags = _VRtrLdpAddrFecFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 4),
    _VRtrLdpAddrFecFlags_Type()
)
vRtrLdpAddrFecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecFlags.setStatus("current")
_VRtrLdpAddrFecNumInLabels_Type = Unsigned32
_VRtrLdpAddrFecNumInLabels_Object = MibTableColumn
vRtrLdpAddrFecNumInLabels = _VRtrLdpAddrFecNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 5),
    _VRtrLdpAddrFecNumInLabels_Type()
)
vRtrLdpAddrFecNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecNumInLabels.setStatus("current")
_VRtrLdpAddrFecNumOutLabels_Type = Unsigned32
_VRtrLdpAddrFecNumOutLabels_Object = MibTableColumn
vRtrLdpAddrFecNumOutLabels = _VRtrLdpAddrFecNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 6),
    _VRtrLdpAddrFecNumOutLabels_Type()
)
vRtrLdpAddrFecNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecNumOutLabels.setStatus("current")
_VRtrLdpAddrFecInLabel1_Type = Unsigned32
_VRtrLdpAddrFecInLabel1_Object = MibTableColumn
vRtrLdpAddrFecInLabel1 = _VRtrLdpAddrFecInLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 7),
    _VRtrLdpAddrFecInLabel1_Type()
)
vRtrLdpAddrFecInLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabel1.setStatus("current")
_VRtrLdpAddrFecInLabelStatus1_Type = TmnxLabelStatus
_VRtrLdpAddrFecInLabelStatus1_Object = MibTableColumn
vRtrLdpAddrFecInLabelStatus1 = _VRtrLdpAddrFecInLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 8),
    _VRtrLdpAddrFecInLabelStatus1_Type()
)
vRtrLdpAddrFecInLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelStatus1.setStatus("current")
_VRtrLdpAddrFecInLabelIfIndex1_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecInLabelIfIndex1_Object = MibTableColumn
vRtrLdpAddrFecInLabelIfIndex1 = _VRtrLdpAddrFecInLabelIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 9),
    _VRtrLdpAddrFecInLabelIfIndex1_Type()
)
vRtrLdpAddrFecInLabelIfIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelIfIndex1.setStatus("current")
_VRtrLdpAddrFecInLabel2_Type = Unsigned32
_VRtrLdpAddrFecInLabel2_Object = MibTableColumn
vRtrLdpAddrFecInLabel2 = _VRtrLdpAddrFecInLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 10),
    _VRtrLdpAddrFecInLabel2_Type()
)
vRtrLdpAddrFecInLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabel2.setStatus("current")
_VRtrLdpAddrFecInLabelStatus2_Type = TmnxLabelStatus
_VRtrLdpAddrFecInLabelStatus2_Object = MibTableColumn
vRtrLdpAddrFecInLabelStatus2 = _VRtrLdpAddrFecInLabelStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 11),
    _VRtrLdpAddrFecInLabelStatus2_Type()
)
vRtrLdpAddrFecInLabelStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelStatus2.setStatus("current")
_VRtrLdpAddrFecInLabelIfIndex2_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecInLabelIfIndex2_Object = MibTableColumn
vRtrLdpAddrFecInLabelIfIndex2 = _VRtrLdpAddrFecInLabelIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 12),
    _VRtrLdpAddrFecInLabelIfIndex2_Type()
)
vRtrLdpAddrFecInLabelIfIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelIfIndex2.setStatus("current")
_VRtrLdpAddrFecInLabel3_Type = Unsigned32
_VRtrLdpAddrFecInLabel3_Object = MibTableColumn
vRtrLdpAddrFecInLabel3 = _VRtrLdpAddrFecInLabel3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 13),
    _VRtrLdpAddrFecInLabel3_Type()
)
vRtrLdpAddrFecInLabel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabel3.setStatus("current")
_VRtrLdpAddrFecInLabelStatus3_Type = TmnxLabelStatus
_VRtrLdpAddrFecInLabelStatus3_Object = MibTableColumn
vRtrLdpAddrFecInLabelStatus3 = _VRtrLdpAddrFecInLabelStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 14),
    _VRtrLdpAddrFecInLabelStatus3_Type()
)
vRtrLdpAddrFecInLabelStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelStatus3.setStatus("current")
_VRtrLdpAddrFecInLabelIfIndex3_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecInLabelIfIndex3_Object = MibTableColumn
vRtrLdpAddrFecInLabelIfIndex3 = _VRtrLdpAddrFecInLabelIfIndex3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 15),
    _VRtrLdpAddrFecInLabelIfIndex3_Type()
)
vRtrLdpAddrFecInLabelIfIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelIfIndex3.setStatus("current")
_VRtrLdpAddrFecInLabel4_Type = Unsigned32
_VRtrLdpAddrFecInLabel4_Object = MibTableColumn
vRtrLdpAddrFecInLabel4 = _VRtrLdpAddrFecInLabel4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 16),
    _VRtrLdpAddrFecInLabel4_Type()
)
vRtrLdpAddrFecInLabel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabel4.setStatus("current")
_VRtrLdpAddrFecInLabelStatus4_Type = TmnxLabelStatus
_VRtrLdpAddrFecInLabelStatus4_Object = MibTableColumn
vRtrLdpAddrFecInLabelStatus4 = _VRtrLdpAddrFecInLabelStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 17),
    _VRtrLdpAddrFecInLabelStatus4_Type()
)
vRtrLdpAddrFecInLabelStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelStatus4.setStatus("current")
_VRtrLdpAddrFecInLabelIfIndex4_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecInLabelIfIndex4_Object = MibTableColumn
vRtrLdpAddrFecInLabelIfIndex4 = _VRtrLdpAddrFecInLabelIfIndex4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 18),
    _VRtrLdpAddrFecInLabelIfIndex4_Type()
)
vRtrLdpAddrFecInLabelIfIndex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelIfIndex4.setStatus("current")
_VRtrLdpAddrFecInLabel5_Type = Unsigned32
_VRtrLdpAddrFecInLabel5_Object = MibTableColumn
vRtrLdpAddrFecInLabel5 = _VRtrLdpAddrFecInLabel5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 19),
    _VRtrLdpAddrFecInLabel5_Type()
)
vRtrLdpAddrFecInLabel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabel5.setStatus("current")
_VRtrLdpAddrFecInLabelStatus5_Type = TmnxLabelStatus
_VRtrLdpAddrFecInLabelStatus5_Object = MibTableColumn
vRtrLdpAddrFecInLabelStatus5 = _VRtrLdpAddrFecInLabelStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 20),
    _VRtrLdpAddrFecInLabelStatus5_Type()
)
vRtrLdpAddrFecInLabelStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelStatus5.setStatus("current")
_VRtrLdpAddrFecInLabelIfIndex5_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecInLabelIfIndex5_Object = MibTableColumn
vRtrLdpAddrFecInLabelIfIndex5 = _VRtrLdpAddrFecInLabelIfIndex5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 21),
    _VRtrLdpAddrFecInLabelIfIndex5_Type()
)
vRtrLdpAddrFecInLabelIfIndex5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecInLabelIfIndex5.setStatus("current")
_VRtrLdpAddrFecOutLabel1_Type = Unsigned32
_VRtrLdpAddrFecOutLabel1_Object = MibTableColumn
vRtrLdpAddrFecOutLabel1 = _VRtrLdpAddrFecOutLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 22),
    _VRtrLdpAddrFecOutLabel1_Type()
)
vRtrLdpAddrFecOutLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabel1.setStatus("current")
_VRtrLdpAddrFecOutLabelStatus1_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLabelStatus1_Object = MibTableColumn
vRtrLdpAddrFecOutLabelStatus1 = _VRtrLdpAddrFecOutLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 23),
    _VRtrLdpAddrFecOutLabelStatus1_Type()
)
vRtrLdpAddrFecOutLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelStatus1.setStatus("current")
_VRtrLdpAddrFecOutLabelIfIndex1_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLabelIfIndex1_Object = MibTableColumn
vRtrLdpAddrFecOutLabelIfIndex1 = _VRtrLdpAddrFecOutLabelIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 24),
    _VRtrLdpAddrFecOutLabelIfIndex1_Type()
)
vRtrLdpAddrFecOutLabelIfIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelIfIndex1.setStatus("current")
_VRtrLdpAddrFecOutLabelNextHop1_Type = IpAddress
_VRtrLdpAddrFecOutLabelNextHop1_Object = MibTableColumn
vRtrLdpAddrFecOutLabelNextHop1 = _VRtrLdpAddrFecOutLabelNextHop1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 25),
    _VRtrLdpAddrFecOutLabelNextHop1_Type()
)
vRtrLdpAddrFecOutLabelNextHop1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelNextHop1.setStatus("current")
_VRtrLdpAddrFecOutLabel2_Type = Unsigned32
_VRtrLdpAddrFecOutLabel2_Object = MibTableColumn
vRtrLdpAddrFecOutLabel2 = _VRtrLdpAddrFecOutLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 26),
    _VRtrLdpAddrFecOutLabel2_Type()
)
vRtrLdpAddrFecOutLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabel2.setStatus("current")
_VRtrLdpAddrFecOutLabelStatus2_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLabelStatus2_Object = MibTableColumn
vRtrLdpAddrFecOutLabelStatus2 = _VRtrLdpAddrFecOutLabelStatus2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 27),
    _VRtrLdpAddrFecOutLabelStatus2_Type()
)
vRtrLdpAddrFecOutLabelStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelStatus2.setStatus("current")
_VRtrLdpAddrFecOutLabelIfIndex2_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLabelIfIndex2_Object = MibTableColumn
vRtrLdpAddrFecOutLabelIfIndex2 = _VRtrLdpAddrFecOutLabelIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 28),
    _VRtrLdpAddrFecOutLabelIfIndex2_Type()
)
vRtrLdpAddrFecOutLabelIfIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelIfIndex2.setStatus("current")
_VRtrLdpAddrFecOutLabelNextHop2_Type = IpAddress
_VRtrLdpAddrFecOutLabelNextHop2_Object = MibTableColumn
vRtrLdpAddrFecOutLabelNextHop2 = _VRtrLdpAddrFecOutLabelNextHop2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 29),
    _VRtrLdpAddrFecOutLabelNextHop2_Type()
)
vRtrLdpAddrFecOutLabelNextHop2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelNextHop2.setStatus("current")
_VRtrLdpAddrFecOutLabel3_Type = Unsigned32
_VRtrLdpAddrFecOutLabel3_Object = MibTableColumn
vRtrLdpAddrFecOutLabel3 = _VRtrLdpAddrFecOutLabel3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 30),
    _VRtrLdpAddrFecOutLabel3_Type()
)
vRtrLdpAddrFecOutLabel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabel3.setStatus("current")
_VRtrLdpAddrFecOutLabelStatus3_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLabelStatus3_Object = MibTableColumn
vRtrLdpAddrFecOutLabelStatus3 = _VRtrLdpAddrFecOutLabelStatus3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 31),
    _VRtrLdpAddrFecOutLabelStatus3_Type()
)
vRtrLdpAddrFecOutLabelStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelStatus3.setStatus("current")
_VRtrLdpAddrFecOutLabelIfIndex3_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLabelIfIndex3_Object = MibTableColumn
vRtrLdpAddrFecOutLabelIfIndex3 = _VRtrLdpAddrFecOutLabelIfIndex3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 32),
    _VRtrLdpAddrFecOutLabelIfIndex3_Type()
)
vRtrLdpAddrFecOutLabelIfIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelIfIndex3.setStatus("current")
_VRtrLdpAddrFecOutLabelNextHop3_Type = IpAddress
_VRtrLdpAddrFecOutLabelNextHop3_Object = MibTableColumn
vRtrLdpAddrFecOutLabelNextHop3 = _VRtrLdpAddrFecOutLabelNextHop3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 33),
    _VRtrLdpAddrFecOutLabelNextHop3_Type()
)
vRtrLdpAddrFecOutLabelNextHop3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelNextHop3.setStatus("current")
_VRtrLdpAddrFecOutLabel4_Type = Unsigned32
_VRtrLdpAddrFecOutLabel4_Object = MibTableColumn
vRtrLdpAddrFecOutLabel4 = _VRtrLdpAddrFecOutLabel4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 34),
    _VRtrLdpAddrFecOutLabel4_Type()
)
vRtrLdpAddrFecOutLabel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabel4.setStatus("current")
_VRtrLdpAddrFecOutLabelStatus4_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLabelStatus4_Object = MibTableColumn
vRtrLdpAddrFecOutLabelStatus4 = _VRtrLdpAddrFecOutLabelStatus4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 35),
    _VRtrLdpAddrFecOutLabelStatus4_Type()
)
vRtrLdpAddrFecOutLabelStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelStatus4.setStatus("current")
_VRtrLdpAddrFecOutLabelIfIndex4_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLabelIfIndex4_Object = MibTableColumn
vRtrLdpAddrFecOutLabelIfIndex4 = _VRtrLdpAddrFecOutLabelIfIndex4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 36),
    _VRtrLdpAddrFecOutLabelIfIndex4_Type()
)
vRtrLdpAddrFecOutLabelIfIndex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelIfIndex4.setStatus("current")
_VRtrLdpAddrFecOutLabelNextHop4_Type = IpAddress
_VRtrLdpAddrFecOutLabelNextHop4_Object = MibTableColumn
vRtrLdpAddrFecOutLabelNextHop4 = _VRtrLdpAddrFecOutLabelNextHop4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 37),
    _VRtrLdpAddrFecOutLabelNextHop4_Type()
)
vRtrLdpAddrFecOutLabelNextHop4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelNextHop4.setStatus("current")
_VRtrLdpAddrFecOutLabel5_Type = Unsigned32
_VRtrLdpAddrFecOutLabel5_Object = MibTableColumn
vRtrLdpAddrFecOutLabel5 = _VRtrLdpAddrFecOutLabel5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 38),
    _VRtrLdpAddrFecOutLabel5_Type()
)
vRtrLdpAddrFecOutLabel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabel5.setStatus("current")
_VRtrLdpAddrFecOutLabelStatus5_Type = TmnxLabelStatus
_VRtrLdpAddrFecOutLabelStatus5_Object = MibTableColumn
vRtrLdpAddrFecOutLabelStatus5 = _VRtrLdpAddrFecOutLabelStatus5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 39),
    _VRtrLdpAddrFecOutLabelStatus5_Type()
)
vRtrLdpAddrFecOutLabelStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelStatus5.setStatus("current")
_VRtrLdpAddrFecOutLabelIfIndex5_Type = InterfaceIndexOrZero
_VRtrLdpAddrFecOutLabelIfIndex5_Object = MibTableColumn
vRtrLdpAddrFecOutLabelIfIndex5 = _VRtrLdpAddrFecOutLabelIfIndex5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 40),
    _VRtrLdpAddrFecOutLabelIfIndex5_Type()
)
vRtrLdpAddrFecOutLabelIfIndex5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelIfIndex5.setStatus("current")
_VRtrLdpAddrFecOutLabelNextHop5_Type = IpAddress
_VRtrLdpAddrFecOutLabelNextHop5_Object = MibTableColumn
vRtrLdpAddrFecOutLabelNextHop5 = _VRtrLdpAddrFecOutLabelNextHop5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 41),
    _VRtrLdpAddrFecOutLabelNextHop5_Type()
)
vRtrLdpAddrFecOutLabelNextHop5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecOutLabelNextHop5.setStatus("current")
_VRtrLdpAddrFecLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpAddrFecLspId_Object = MibTableColumn
vRtrLdpAddrFecLspId = _VRtrLdpAddrFecLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 13, 1, 42),
    _VRtrLdpAddrFecLspId_Type()
)
vRtrLdpAddrFecLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecLspId.setStatus("current")
_VRtrLdpAddrFecMapTable_Object = MibTable
vRtrLdpAddrFecMapTable = _VRtrLdpAddrFecMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 14)
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecMapTable.setStatus("current")
_VRtrLdpAddrFecMapEntry_Object = MibTableRow
vRtrLdpAddrFecMapEntry = _VRtrLdpAddrFecMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 14, 1)
)
vRtrLdpAddrFecMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapFecType"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpMask"),
)
if mibBuilder.loadTexts:
    vRtrLdpAddrFecMapEntry.setStatus("current")
_VRtrLdpAddrFecMapFecType_Type = TmnxLdpFECType
_VRtrLdpAddrFecMapFecType_Object = MibTableColumn
vRtrLdpAddrFecMapFecType = _VRtrLdpAddrFecMapFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 14, 1, 1),
    _VRtrLdpAddrFecMapFecType_Type()
)
vRtrLdpAddrFecMapFecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecMapFecType.setStatus("current")
_VRtrLdpAddrFecMapIpPrefix_Type = IpAddress
_VRtrLdpAddrFecMapIpPrefix_Object = MibTableColumn
vRtrLdpAddrFecMapIpPrefix = _VRtrLdpAddrFecMapIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 14, 1, 2),
    _VRtrLdpAddrFecMapIpPrefix_Type()
)
vRtrLdpAddrFecMapIpPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecMapIpPrefix.setStatus("current")
_VRtrLdpAddrFecMapIpMask_Type = IpAddress
_VRtrLdpAddrFecMapIpMask_Object = MibTableColumn
vRtrLdpAddrFecMapIpMask = _VRtrLdpAddrFecMapIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 14, 1, 3),
    _VRtrLdpAddrFecMapIpMask_Type()
)
vRtrLdpAddrFecMapIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAddrFecMapIpMask.setStatus("current")
_VRtrLdpAdjBackoffTable_Object = MibTable
vRtrLdpAdjBackoffTable = _VRtrLdpAdjBackoffTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15)
)
if mibBuilder.loadTexts:
    vRtrLdpAdjBackoffTable.setStatus("current")
_VRtrLdpAdjBackoffEntry_Object = MibTableRow
vRtrLdpAdjBackoffEntry = _VRtrLdpAdjBackoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpAdjBackoffEntry.setStatus("current")


class _VRtrLdpAdjInitBackoff_Type(Unsigned32):
    """Custom type vRtrLdpAdjInitBackoff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2592000),
    )


_VRtrLdpAdjInitBackoff_Type.__name__ = "Unsigned32"
_VRtrLdpAdjInitBackoff_Object = MibTableColumn
vRtrLdpAdjInitBackoff = _VRtrLdpAdjInitBackoff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1, 1),
    _VRtrLdpAdjInitBackoff_Type()
)
vRtrLdpAdjInitBackoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAdjInitBackoff.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpAdjInitBackoff.setUnits("seconds")


class _VRtrLdpAdjMaxBackoff_Type(Unsigned32):
    """Custom type vRtrLdpAdjMaxBackoff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2592000),
    )


_VRtrLdpAdjMaxBackoff_Type.__name__ = "Unsigned32"
_VRtrLdpAdjMaxBackoff_Object = MibTableColumn
vRtrLdpAdjMaxBackoff = _VRtrLdpAdjMaxBackoff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1, 2),
    _VRtrLdpAdjMaxBackoff_Type()
)
vRtrLdpAdjMaxBackoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAdjMaxBackoff.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpAdjMaxBackoff.setUnits("seconds")
_VRtrLdpAdjCurrentBackoff_Type = Unsigned32
_VRtrLdpAdjCurrentBackoff_Object = MibTableColumn
vRtrLdpAdjCurrentBackoff = _VRtrLdpAdjCurrentBackoff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1, 3),
    _VRtrLdpAdjCurrentBackoff_Type()
)
vRtrLdpAdjCurrentBackoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAdjCurrentBackoff.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpAdjCurrentBackoff.setUnits("seconds")
_VRtrLdpAdjWaitingTime_Type = Unsigned32
_VRtrLdpAdjWaitingTime_Object = MibTableColumn
vRtrLdpAdjWaitingTime = _VRtrLdpAdjWaitingTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1, 4),
    _VRtrLdpAdjWaitingTime_Type()
)
vRtrLdpAdjWaitingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAdjWaitingTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpAdjWaitingTime.setUnits("seconds")
_VRtrLdpAdjBackoffStatus_Type = TruthValue
_VRtrLdpAdjBackoffStatus_Object = MibTableColumn
vRtrLdpAdjBackoffStatus = _VRtrLdpAdjBackoffStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 15, 1, 5),
    _VRtrLdpAdjBackoffStatus_Type()
)
vRtrLdpAdjBackoffStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpAdjBackoffStatus.setStatus("current")
_VRtrLdpPeerParamsTable_Object = MibTable
vRtrLdpPeerParamsTable = _VRtrLdpPeerParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16)
)
if mibBuilder.loadTexts:
    vRtrLdpPeerParamsTable.setStatus("current")
_VRtrLdpPeerParamsEntry_Object = MibTableRow
vRtrLdpPeerParamsEntry = _VRtrLdpPeerParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1)
)
vRtrLdpPeerParamsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpPeerParamsEntry.setStatus("current")
_VRtrLdpPeerRowStatus_Type = RowStatus
_VRtrLdpPeerRowStatus_Object = MibTableColumn
vRtrLdpPeerRowStatus = _VRtrLdpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 1),
    _VRtrLdpPeerRowStatus_Type()
)
vRtrLdpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerRowStatus.setStatus("current")


class _VRtrLdpPeerAuth_Type(TruthValue):
    """Custom type vRtrLdpPeerAuth based on TruthValue"""


_VRtrLdpPeerAuth_Object = MibTableColumn
vRtrLdpPeerAuth = _VRtrLdpPeerAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 2),
    _VRtrLdpPeerAuth_Type()
)
vRtrLdpPeerAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerAuth.setStatus("current")


class _VRtrLdpPeerAuthKey_Type(OctetString):
    """Custom type vRtrLdpPeerAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VRtrLdpPeerAuthKey_Type.__name__ = "OctetString"
_VRtrLdpPeerAuthKey_Object = MibTableColumn
vRtrLdpPeerAuthKey = _VRtrLdpPeerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 3),
    _VRtrLdpPeerAuthKey_Type()
)
vRtrLdpPeerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerAuthKey.setStatus("current")


class _VRtrLdpPeerMinTTLValue_Type(Unsigned32):
    """Custom type vRtrLdpPeerMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_VRtrLdpPeerMinTTLValue_Type.__name__ = "Unsigned32"
_VRtrLdpPeerMinTTLValue_Object = MibTableColumn
vRtrLdpPeerMinTTLValue = _VRtrLdpPeerMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 4),
    _VRtrLdpPeerMinTTLValue_Type()
)
vRtrLdpPeerMinTTLValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerMinTTLValue.setStatus("current")


class _VRtrLdpPeerTTLLogId_Type(TFilterLogId):
    """Custom type vRtrLdpPeerTTLLogId based on TFilterLogId"""
    defaultValue = 0


_VRtrLdpPeerTTLLogId_Object = MibTableColumn
vRtrLdpPeerTTLLogId = _VRtrLdpPeerTTLLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 5),
    _VRtrLdpPeerTTLLogId_Type()
)
vRtrLdpPeerTTLLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerTTLLogId.setStatus("current")


class _VRtrLdpPeerAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type vRtrLdpPeerAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrLdpPeerAuthKeyChain_Object = MibTableColumn
vRtrLdpPeerAuthKeyChain = _VRtrLdpPeerAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 16, 1, 6),
    _VRtrLdpPeerAuthKeyChain_Type()
)
vRtrLdpPeerAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpPeerAuthKeyChain.setStatus("current")
_TmnxLdpNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxLdpNotificationObjects = _TmnxLdpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17)
)


class _VRtrLdpInstanceNotifyReasonCode_Type(Integer32):
    """Custom type vRtrLdpInstanceNotifyReasonCode based on Integer32"""
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
        *(("adminDown", 2),
          ("adminUp", 1),
          ("operDown", 4),
          ("operUp", 3))
    )


_VRtrLdpInstanceNotifyReasonCode_Type.__name__ = "Integer32"
_VRtrLdpInstanceNotifyReasonCode_Object = MibScalar
vRtrLdpInstanceNotifyReasonCode = _VRtrLdpInstanceNotifyReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 1),
    _VRtrLdpInstanceNotifyReasonCode_Type()
)
vRtrLdpInstanceNotifyReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpInstanceNotifyReasonCode.setStatus("current")


class _VRtrLdpIfNotifyReasonCode_Type(Integer32):
    """Custom type vRtrLdpIfNotifyReasonCode based on Integer32"""
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
        *(("adminDown", 2),
          ("adminUp", 1),
          ("operDown", 4),
          ("operUp", 3),
          ("sysIpDown", 6),
          ("sysIpUp", 5))
    )


_VRtrLdpIfNotifyReasonCode_Type.__name__ = "Integer32"
_VRtrLdpIfNotifyReasonCode_Object = MibScalar
vRtrLdpIfNotifyReasonCode = _VRtrLdpIfNotifyReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 2),
    _VRtrLdpIfNotifyReasonCode_Type()
)
vRtrLdpIfNotifyReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpIfNotifyReasonCode.setStatus("current")


class _VRtrLdpNotifyLocalServiceID_Type(TmnxServId):
    """Custom type vRtrLdpNotifyLocalServiceID based on TmnxServId"""
    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrLdpNotifyLocalServiceID_Type.__name__ = "TmnxServId"
_VRtrLdpNotifyLocalServiceID_Object = MibScalar
vRtrLdpNotifyLocalServiceID = _VRtrLdpNotifyLocalServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 3),
    _VRtrLdpNotifyLocalServiceID_Type()
)
vRtrLdpNotifyLocalServiceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpNotifyLocalServiceID.setStatus("obsolete")


class _VRtrLdpNotifyRemoteServiceID_Type(TmnxServId):
    """Custom type vRtrLdpNotifyRemoteServiceID based on TmnxServId"""
    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrLdpNotifyRemoteServiceID_Type.__name__ = "TmnxServId"
_VRtrLdpNotifyRemoteServiceID_Object = MibScalar
vRtrLdpNotifyRemoteServiceID = _VRtrLdpNotifyRemoteServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 4),
    _VRtrLdpNotifyRemoteServiceID_Type()
)
vRtrLdpNotifyRemoteServiceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpNotifyRemoteServiceID.setStatus("obsolete")
_VRtrLdpNotifyLocalGroupID_Type = TmnxVcId
_VRtrLdpNotifyLocalGroupID_Object = MibScalar
vRtrLdpNotifyLocalGroupID = _VRtrLdpNotifyLocalGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 5),
    _VRtrLdpNotifyLocalGroupID_Type()
)
vRtrLdpNotifyLocalGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpNotifyLocalGroupID.setStatus("current")
_VRtrLdpNotifyRemoteGroupID_Type = TmnxVcId
_VRtrLdpNotifyRemoteGroupID_Object = MibScalar
vRtrLdpNotifyRemoteGroupID = _VRtrLdpNotifyRemoteGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 17, 6),
    _VRtrLdpNotifyRemoteGroupID_Type()
)
vRtrLdpNotifyRemoteGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrLdpNotifyRemoteGroupID.setStatus("current")
_VRtrLdpStaticFecTable_Object = MibTable
vRtrLdpStaticFecTable = _VRtrLdpStaticFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18)
)
if mibBuilder.loadTexts:
    vRtrLdpStaticFecTable.setStatus("current")
_VRtrLdpStaticFecEntry_Object = MibTableRow
vRtrLdpStaticFecEntry = _VRtrLdpStaticFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1)
)
vRtrLdpStaticFecEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecIpPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecIpMask"),
)
if mibBuilder.loadTexts:
    vRtrLdpStaticFecEntry.setStatus("current")
_VRtrLdpStaticFecIpPrefix_Type = IpAddress
_VRtrLdpStaticFecIpPrefix_Object = MibTableColumn
vRtrLdpStaticFecIpPrefix = _VRtrLdpStaticFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 1),
    _VRtrLdpStaticFecIpPrefix_Type()
)
vRtrLdpStaticFecIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecIpPrefix.setStatus("current")
_VRtrLdpStaticFecIpMask_Type = IpAddress
_VRtrLdpStaticFecIpMask_Object = MibTableColumn
vRtrLdpStaticFecIpMask = _VRtrLdpStaticFecIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 2),
    _VRtrLdpStaticFecIpMask_Type()
)
vRtrLdpStaticFecIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecIpMask.setStatus("current")
_VRtrLdpStaticFecRowStatus_Type = RowStatus
_VRtrLdpStaticFecRowStatus_Object = MibTableColumn
vRtrLdpStaticFecRowStatus = _VRtrLdpStaticFecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 3),
    _VRtrLdpStaticFecRowStatus_Type()
)
vRtrLdpStaticFecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecRowStatus.setStatus("current")
_VRtrLdpStaticFecNextNHIndex_Type = Unsigned32
_VRtrLdpStaticFecNextNHIndex_Object = MibTableColumn
vRtrLdpStaticFecNextNHIndex = _VRtrLdpStaticFecNextNHIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 4),
    _VRtrLdpStaticFecNextNHIndex_Type()
)
vRtrLdpStaticFecNextNHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNextNHIndex.setStatus("current")


class _VRtrLdpStaticFecIngLabel_Type(Unsigned32):
    """Custom type vRtrLdpStaticFecIngLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1023),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrLdpStaticFecIngLabel_Type.__name__ = "Unsigned32"
_VRtrLdpStaticFecIngLabel_Object = MibTableColumn
vRtrLdpStaticFecIngLabel = _VRtrLdpStaticFecIngLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 5),
    _VRtrLdpStaticFecIngLabel_Type()
)
vRtrLdpStaticFecIngLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecIngLabel.setStatus("current")
_VRtrLdpStaticFecNumNH_Type = Gauge32
_VRtrLdpStaticFecNumNH_Object = MibTableColumn
vRtrLdpStaticFecNumNH = _VRtrLdpStaticFecNumNH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 6),
    _VRtrLdpStaticFecNumNH_Type()
)
vRtrLdpStaticFecNumNH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNumNH.setStatus("current")
_VRtrLdpStaticFecOperIngLabel_Type = Unsigned32
_VRtrLdpStaticFecOperIngLabel_Object = MibTableColumn
vRtrLdpStaticFecOperIngLabel = _VRtrLdpStaticFecOperIngLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 18, 1, 7),
    _VRtrLdpStaticFecOperIngLabel_Type()
)
vRtrLdpStaticFecOperIngLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecOperIngLabel.setStatus("current")
_VRtrLdpStaticFecNHTable_Object = MibTable
vRtrLdpStaticFecNHTable = _VRtrLdpStaticFecNHTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19)
)
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHTable.setStatus("current")
_VRtrLdpStaticFecNHEntry_Object = MibTableRow
vRtrLdpStaticFecNHEntry = _VRtrLdpStaticFecNHEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1)
)
vRtrLdpStaticFecNHEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecIpPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecIpMask"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHIndex"),
)
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHEntry.setStatus("current")
_VRtrLdpStaticFecNHIndex_Type = Unsigned32
_VRtrLdpStaticFecNHIndex_Object = MibTableColumn
vRtrLdpStaticFecNHIndex = _VRtrLdpStaticFecNHIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 1),
    _VRtrLdpStaticFecNHIndex_Type()
)
vRtrLdpStaticFecNHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHIndex.setStatus("current")
_VRtrLdpStaticFecNHRowStatus_Type = RowStatus
_VRtrLdpStaticFecNHRowStatus_Object = MibTableColumn
vRtrLdpStaticFecNHRowStatus = _VRtrLdpStaticFecNHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 2),
    _VRtrLdpStaticFecNHRowStatus_Type()
)
vRtrLdpStaticFecNHRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHRowStatus.setStatus("current")


class _VRtrLdpStaticFecNHType_Type(Integer32):
    """Custom type vRtrLdpStaticFecNHType based on Integer32"""
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
        *(("ipAddress", 1),
          ("pop", 2),
          ("unknown", 0))
    )


_VRtrLdpStaticFecNHType_Type.__name__ = "Integer32"
_VRtrLdpStaticFecNHType_Object = MibTableColumn
vRtrLdpStaticFecNHType = _VRtrLdpStaticFecNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 3),
    _VRtrLdpStaticFecNHType_Type()
)
vRtrLdpStaticFecNHType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHType.setStatus("current")


class _VRtrLdpStaticFecNHIpAddr_Type(IpAddress):
    """Custom type vRtrLdpStaticFecNHIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrLdpStaticFecNHIpAddr_Object = MibTableColumn
vRtrLdpStaticFecNHIpAddr = _VRtrLdpStaticFecNHIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 4),
    _VRtrLdpStaticFecNHIpAddr_Type()
)
vRtrLdpStaticFecNHIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHIpAddr.setStatus("current")


class _VRtrLdpStaticFecNHEgrLabel_Type(Unsigned32):
    """Custom type vRtrLdpStaticFecNHEgrLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrLdpStaticFecNHEgrLabel_Type.__name__ = "Unsigned32"
_VRtrLdpStaticFecNHEgrLabel_Object = MibTableColumn
vRtrLdpStaticFecNHEgrLabel = _VRtrLdpStaticFecNHEgrLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 19, 1, 5),
    _VRtrLdpStaticFecNHEgrLabel_Type()
)
vRtrLdpStaticFecNHEgrLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStaticFecNHEgrLabel.setStatus("current")
_VRtrLdpTargTable_Object = MibTable
vRtrLdpTargTable = _VRtrLdpTargTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20)
)
if mibBuilder.loadTexts:
    vRtrLdpTargTable.setStatus("current")
_VRtrLdpTargEntry_Object = MibTableRow
vRtrLdpTargEntry = _VRtrLdpTargEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpTargEntry.setStatus("current")


class _VRtrLdpTargImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargImportPolicy1_Object = MibTableColumn
vRtrLdpTargImportPolicy1 = _VRtrLdpTargImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 3),
    _VRtrLdpTargImportPolicy1_Type()
)
vRtrLdpTargImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargImportPolicy1.setStatus("current")


class _VRtrLdpTargImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargImportPolicy2_Object = MibTableColumn
vRtrLdpTargImportPolicy2 = _VRtrLdpTargImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 4),
    _VRtrLdpTargImportPolicy2_Type()
)
vRtrLdpTargImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargImportPolicy2.setStatus("current")


class _VRtrLdpTargImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargImportPolicy3_Object = MibTableColumn
vRtrLdpTargImportPolicy3 = _VRtrLdpTargImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 5),
    _VRtrLdpTargImportPolicy3_Type()
)
vRtrLdpTargImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargImportPolicy3.setStatus("current")


class _VRtrLdpTargImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargImportPolicy4_Object = MibTableColumn
vRtrLdpTargImportPolicy4 = _VRtrLdpTargImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 6),
    _VRtrLdpTargImportPolicy4_Type()
)
vRtrLdpTargImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargImportPolicy4.setStatus("current")


class _VRtrLdpTargImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargImportPolicy5_Object = MibTableColumn
vRtrLdpTargImportPolicy5 = _VRtrLdpTargImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 7),
    _VRtrLdpTargImportPolicy5_Type()
)
vRtrLdpTargImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargImportPolicy5.setStatus("current")


class _VRtrLdpTargExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargExportPolicy1_Object = MibTableColumn
vRtrLdpTargExportPolicy1 = _VRtrLdpTargExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 8),
    _VRtrLdpTargExportPolicy1_Type()
)
vRtrLdpTargExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargExportPolicy1.setStatus("current")


class _VRtrLdpTargExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargExportPolicy2_Object = MibTableColumn
vRtrLdpTargExportPolicy2 = _VRtrLdpTargExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 9),
    _VRtrLdpTargExportPolicy2_Type()
)
vRtrLdpTargExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargExportPolicy2.setStatus("current")


class _VRtrLdpTargExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargExportPolicy3_Object = MibTableColumn
vRtrLdpTargExportPolicy3 = _VRtrLdpTargExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 10),
    _VRtrLdpTargExportPolicy3_Type()
)
vRtrLdpTargExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargExportPolicy3.setStatus("current")


class _VRtrLdpTargExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargExportPolicy4_Object = MibTableColumn
vRtrLdpTargExportPolicy4 = _VRtrLdpTargExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 11),
    _VRtrLdpTargExportPolicy4_Type()
)
vRtrLdpTargExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargExportPolicy4.setStatus("current")


class _VRtrLdpTargExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpTargExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpTargExportPolicy5_Object = MibTableColumn
vRtrLdpTargExportPolicy5 = _VRtrLdpTargExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 12),
    _VRtrLdpTargExportPolicy5_Type()
)
vRtrLdpTargExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargExportPolicy5.setStatus("current")


class _VRtrLdpTargTunnelPreference_Type(TruthValue):
    """Custom type vRtrLdpTargTunnelPreference based on TruthValue"""


_VRtrLdpTargTunnelPreference_Object = MibTableColumn
vRtrLdpTargTunnelPreference = _VRtrLdpTargTunnelPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 20, 1, 13),
    _VRtrLdpTargTunnelPreference_Type()
)
vRtrLdpTargTunnelPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpTargTunnelPreference.setStatus("current")
_VRtrLdpIfTunnelingLspTable_Object = MibTable
vRtrLdpIfTunnelingLspTable = _VRtrLdpIfTunnelingLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 21)
)
if mibBuilder.loadTexts:
    vRtrLdpIfTunnelingLspTable.setStatus("current")
_VRtrLdpIfTunnelingLspEntry_Object = MibTableRow
vRtrLdpIfTunnelingLspEntry = _VRtrLdpIfTunnelingLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 21, 1)
)
vRtrLdpIfTunnelingLspEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfIndex"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerAddress"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfLspId"),
)
if mibBuilder.loadTexts:
    vRtrLdpIfTunnelingLspEntry.setStatus("current")
_VRtrLdpIfLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpIfLspId_Object = MibTableColumn
vRtrLdpIfLspId = _VRtrLdpIfLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 21, 1, 1),
    _VRtrLdpIfLspId_Type()
)
vRtrLdpIfLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpIfLspId.setStatus("current")
_VRtrLdpIfLspRowStatus_Type = RowStatus
_VRtrLdpIfLspRowStatus_Object = MibTableColumn
vRtrLdpIfLspRowStatus = _VRtrLdpIfLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 21, 1, 2),
    _VRtrLdpIfLspRowStatus_Type()
)
vRtrLdpIfLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpIfLspRowStatus.setStatus("current")
_VRtrLdpCepTdmFecTable_Object = MibTable
vRtrLdpCepTdmFecTable = _VRtrLdpCepTdmFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22)
)
if mibBuilder.loadTexts:
    vRtrLdpCepTdmFecTable.setStatus("current")
_VRtrLdpCepTdmFecEntry_Object = MibTableRow
vRtrLdpCepTdmFecEntry = _VRtrLdpCepTdmFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpCepTdmFecEntry.setStatus("current")
_VRtrLdpCepTdmLocalPayloadSize_Type = Unsigned32
_VRtrLdpCepTdmLocalPayloadSize_Object = MibTableColumn
vRtrLdpCepTdmLocalPayloadSize = _VRtrLdpCepTdmLocalPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 4),
    _VRtrLdpCepTdmLocalPayloadSize_Type()
)
vRtrLdpCepTdmLocalPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalPayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalPayloadSize.setUnits("bytes")
_VRtrLdpCepTdmRemotePayloadSize_Type = Unsigned32
_VRtrLdpCepTdmRemotePayloadSize_Object = MibTableColumn
vRtrLdpCepTdmRemotePayloadSize = _VRtrLdpCepTdmRemotePayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 5),
    _VRtrLdpCepTdmRemotePayloadSize_Type()
)
vRtrLdpCepTdmRemotePayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemotePayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemotePayloadSize.setUnits("bytes")
_VRtrLdpCepTdmLocalBitrate_Type = Unsigned32
_VRtrLdpCepTdmLocalBitrate_Object = MibTableColumn
vRtrLdpCepTdmLocalBitrate = _VRtrLdpCepTdmLocalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 6),
    _VRtrLdpCepTdmLocalBitrate_Type()
)
vRtrLdpCepTdmLocalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalBitrate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalBitrate.setUnits("64 Kbits/s")
_VRtrLdpCepTdmRemoteBitrate_Type = Unsigned32
_VRtrLdpCepTdmRemoteBitrate_Object = MibTableColumn
vRtrLdpCepTdmRemoteBitrate = _VRtrLdpCepTdmRemoteBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 7),
    _VRtrLdpCepTdmRemoteBitrate_Type()
)
vRtrLdpCepTdmRemoteBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteBitrate.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteBitrate.setUnits("64 Kbits/s")
_VRtrLdpCepTdmLocalRtpHeader_Type = TruthValue
_VRtrLdpCepTdmLocalRtpHeader_Object = MibTableColumn
vRtrLdpCepTdmLocalRtpHeader = _VRtrLdpCepTdmLocalRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 8),
    _VRtrLdpCepTdmLocalRtpHeader_Type()
)
vRtrLdpCepTdmLocalRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalRtpHeader.setStatus("current")
_VRtrLdpCepTdmRemoteRtpHeader_Type = TruthValue
_VRtrLdpCepTdmRemoteRtpHeader_Object = MibTableColumn
vRtrLdpCepTdmRemoteRtpHeader = _VRtrLdpCepTdmRemoteRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 9),
    _VRtrLdpCepTdmRemoteRtpHeader_Type()
)
vRtrLdpCepTdmRemoteRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteRtpHeader.setStatus("current")
_VRtrLdpCepTdmLocalDiffTimestamp_Type = TruthValue
_VRtrLdpCepTdmLocalDiffTimestamp_Object = MibTableColumn
vRtrLdpCepTdmLocalDiffTimestamp = _VRtrLdpCepTdmLocalDiffTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 10),
    _VRtrLdpCepTdmLocalDiffTimestamp_Type()
)
vRtrLdpCepTdmLocalDiffTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalDiffTimestamp.setStatus("current")
_VRtrLdpCepTdmRemoteDiffTimestamp_Type = TruthValue
_VRtrLdpCepTdmRemoteDiffTimestamp_Object = MibTableColumn
vRtrLdpCepTdmRemoteDiffTimestamp = _VRtrLdpCepTdmRemoteDiffTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 11),
    _VRtrLdpCepTdmRemoteDiffTimestamp_Type()
)
vRtrLdpCepTdmRemoteDiffTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteDiffTimestamp.setStatus("current")
_VRtrLdpCepTdmLocalSigPkts_Type = TdmOptionsSigPkts
_VRtrLdpCepTdmLocalSigPkts_Object = MibTableColumn
vRtrLdpCepTdmLocalSigPkts = _VRtrLdpCepTdmLocalSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 12),
    _VRtrLdpCepTdmLocalSigPkts_Type()
)
vRtrLdpCepTdmLocalSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalSigPkts.setStatus("current")
_VRtrLdpCepTdmRemoteSigPkts_Type = TdmOptionsSigPkts
_VRtrLdpCepTdmRemoteSigPkts_Object = MibTableColumn
vRtrLdpCepTdmRemoteSigPkts = _VRtrLdpCepTdmRemoteSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 13),
    _VRtrLdpCepTdmRemoteSigPkts_Type()
)
vRtrLdpCepTdmRemoteSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteSigPkts.setStatus("current")
_VRtrLdpCepTdmLocalCasTrunk_Type = TdmOptionsCasTrunkFraming
_VRtrLdpCepTdmLocalCasTrunk_Object = MibTableColumn
vRtrLdpCepTdmLocalCasTrunk = _VRtrLdpCepTdmLocalCasTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 14),
    _VRtrLdpCepTdmLocalCasTrunk_Type()
)
vRtrLdpCepTdmLocalCasTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalCasTrunk.setStatus("current")
_VRtrLdpCepTdmRemoteCasTrunk_Type = TdmOptionsCasTrunkFraming
_VRtrLdpCepTdmRemoteCasTrunk_Object = MibTableColumn
vRtrLdpCepTdmRemoteCasTrunk = _VRtrLdpCepTdmRemoteCasTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 15),
    _VRtrLdpCepTdmRemoteCasTrunk_Type()
)
vRtrLdpCepTdmRemoteCasTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteCasTrunk.setStatus("current")
_VRtrLdpCepTdmLocalTimestampFreq_Type = Unsigned32
_VRtrLdpCepTdmLocalTimestampFreq_Object = MibTableColumn
vRtrLdpCepTdmLocalTimestampFreq = _VRtrLdpCepTdmLocalTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 16),
    _VRtrLdpCepTdmLocalTimestampFreq_Type()
)
vRtrLdpCepTdmLocalTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalTimestampFreq.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalTimestampFreq.setUnits("8 KHz")
_VRtrLdpCepTdmRemoteTimestampFreq_Type = Unsigned32
_VRtrLdpCepTdmRemoteTimestampFreq_Object = MibTableColumn
vRtrLdpCepTdmRemoteTimestampFreq = _VRtrLdpCepTdmRemoteTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 17),
    _VRtrLdpCepTdmRemoteTimestampFreq_Type()
)
vRtrLdpCepTdmRemoteTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteTimestampFreq.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteTimestampFreq.setUnits("8 KHz")
_VRtrLdpCepTdmLocalPayloadType_Type = Unsigned32
_VRtrLdpCepTdmLocalPayloadType_Object = MibTableColumn
vRtrLdpCepTdmLocalPayloadType = _VRtrLdpCepTdmLocalPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 18),
    _VRtrLdpCepTdmLocalPayloadType_Type()
)
vRtrLdpCepTdmLocalPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalPayloadType.setStatus("current")
_VRtrLdpCepTdmRemotePayloadType_Type = Unsigned32
_VRtrLdpCepTdmRemotePayloadType_Object = MibTableColumn
vRtrLdpCepTdmRemotePayloadType = _VRtrLdpCepTdmRemotePayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 19),
    _VRtrLdpCepTdmRemotePayloadType_Type()
)
vRtrLdpCepTdmRemotePayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemotePayloadType.setStatus("current")
_VRtrLdpCepTdmLocalSsrcId_Type = Unsigned32
_VRtrLdpCepTdmLocalSsrcId_Object = MibTableColumn
vRtrLdpCepTdmLocalSsrcId = _VRtrLdpCepTdmLocalSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 20),
    _VRtrLdpCepTdmLocalSsrcId_Type()
)
vRtrLdpCepTdmLocalSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmLocalSsrcId.setStatus("current")
_VRtrLdpCepTdmRemoteSsrcId_Type = Unsigned32
_VRtrLdpCepTdmRemoteSsrcId_Object = MibTableColumn
vRtrLdpCepTdmRemoteSsrcId = _VRtrLdpCepTdmRemoteSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 22, 1, 21),
    _VRtrLdpCepTdmRemoteSsrcId_Type()
)
vRtrLdpCepTdmRemoteSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpCepTdmRemoteSsrcId.setStatus("current")
_VLdpServFec129Table_Object = MibTable
vLdpServFec129Table = _VLdpServFec129Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23)
)
if mibBuilder.loadTexts:
    vLdpServFec129Table.setStatus("current")
_VLdpServFec129Entry_Object = MibTableRow
vLdpServFec129Entry = _VLdpServFec129Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1)
)
vLdpServFec129Entry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecVcType"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129AgiTlv"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129SrcAiiTlv"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129TgtAiiTlv"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    vLdpServFec129Entry.setStatus("current")
_VLdpServFec129AgiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129AgiTlv_Object = MibTableColumn
vLdpServFec129AgiTlv = _VLdpServFec129AgiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 1),
    _VLdpServFec129AgiTlv_Type()
)
vLdpServFec129AgiTlv.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpServFec129AgiTlv.setStatus("current")
_VLdpServFec129SrcAiiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129SrcAiiTlv_Object = MibTableColumn
vLdpServFec129SrcAiiTlv = _VLdpServFec129SrcAiiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 2),
    _VLdpServFec129SrcAiiTlv_Type()
)
vLdpServFec129SrcAiiTlv.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpServFec129SrcAiiTlv.setStatus("current")
_VLdpServFec129TgtAiiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129TgtAiiTlv_Object = MibTableColumn
vLdpServFec129TgtAiiTlv = _VLdpServFec129TgtAiiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 3),
    _VLdpServFec129TgtAiiTlv_Type()
)
vLdpServFec129TgtAiiTlv.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpServFec129TgtAiiTlv.setStatus("current")
_VLdpServFec129ServType_Type = ServType
_VLdpServFec129ServType_Object = MibTableColumn
vLdpServFec129ServType = _VLdpServFec129ServType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 4),
    _VLdpServFec129ServType_Type()
)
vLdpServFec129ServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129ServType.setStatus("current")


class _VLdpServFec129ServId_Type(TmnxServId):
    """Custom type vLdpServFec129ServId based on TmnxServId"""
    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VLdpServFec129ServId_Type.__name__ = "TmnxServId"
_VLdpServFec129ServId_Object = MibTableColumn
vLdpServFec129ServId = _VLdpServFec129ServId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 5),
    _VLdpServFec129ServId_Type()
)
vLdpServFec129ServId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129ServId.setStatus("current")
_VLdpServFec129VpnId_Type = TmnxVpnId
_VLdpServFec129VpnId_Object = MibTableColumn
vLdpServFec129VpnId = _VLdpServFec129VpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 6),
    _VLdpServFec129VpnId_Type()
)
vLdpServFec129VpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129VpnId.setStatus("current")
_VLdpServFec129Flags_Type = TmnxLdpFECFlags
_VLdpServFec129Flags_Object = MibTableColumn
vLdpServFec129Flags = _VLdpServFec129Flags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 7),
    _VLdpServFec129Flags_Type()
)
vLdpServFec129Flags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129Flags.setStatus("current")
_VLdpServFec129NumInLabels_Type = Unsigned32
_VLdpServFec129NumInLabels_Object = MibTableColumn
vLdpServFec129NumInLabels = _VLdpServFec129NumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 8),
    _VLdpServFec129NumInLabels_Type()
)
vLdpServFec129NumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129NumInLabels.setStatus("current")
_VLdpServFec129NumOutLabels_Type = Unsigned32
_VLdpServFec129NumOutLabels_Object = MibTableColumn
vLdpServFec129NumOutLabels = _VLdpServFec129NumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 9),
    _VLdpServFec129NumOutLabels_Type()
)
vLdpServFec129NumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129NumOutLabels.setStatus("current")
_VLdpServFec129InLabel1_Type = Unsigned32
_VLdpServFec129InLabel1_Object = MibTableColumn
vLdpServFec129InLabel1 = _VLdpServFec129InLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 10),
    _VLdpServFec129InLabel1_Type()
)
vLdpServFec129InLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129InLabel1.setStatus("current")
_VLdpServFec129InLabelStatus1_Type = TmnxLabelStatus
_VLdpServFec129InLabelStatus1_Object = MibTableColumn
vLdpServFec129InLabelStatus1 = _VLdpServFec129InLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 11),
    _VLdpServFec129InLabelStatus1_Type()
)
vLdpServFec129InLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129InLabelStatus1.setStatus("current")
_VLdpServFec129OutLabel1_Type = Unsigned32
_VLdpServFec129OutLabel1_Object = MibTableColumn
vLdpServFec129OutLabel1 = _VLdpServFec129OutLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 20),
    _VLdpServFec129OutLabel1_Type()
)
vLdpServFec129OutLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129OutLabel1.setStatus("current")
_VLdpServFec129OutLabelStatus1_Type = TmnxLabelStatus
_VLdpServFec129OutLabelStatus1_Object = MibTableColumn
vLdpServFec129OutLabelStatus1 = _VLdpServFec129OutLabelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 21),
    _VLdpServFec129OutLabelStatus1_Type()
)
vLdpServFec129OutLabelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129OutLabelStatus1.setStatus("current")
_VLdpServFec129SdpId_Type = SdpId
_VLdpServFec129SdpId_Object = MibTableColumn
vLdpServFec129SdpId = _VLdpServFec129SdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 22),
    _VLdpServFec129SdpId_Type()
)
vLdpServFec129SdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129SdpId.setStatus("current")
_VLdpServFec129LocalMTU_Type = Unsigned32
_VLdpServFec129LocalMTU_Object = MibTableColumn
vLdpServFec129LocalMTU = _VLdpServFec129LocalMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 23),
    _VLdpServFec129LocalMTU_Type()
)
vLdpServFec129LocalMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalMTU.setStatus("current")
_VLdpServFec129RemoteMTU_Type = Unsigned32
_VLdpServFec129RemoteMTU_Object = MibTableColumn
vLdpServFec129RemoteMTU = _VLdpServFec129RemoteMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 24),
    _VLdpServFec129RemoteMTU_Type()
)
vLdpServFec129RemoteMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteMTU.setStatus("current")
_VLdpServFec129LocalVlanTag_Type = Unsigned32
_VLdpServFec129LocalVlanTag_Object = MibTableColumn
vLdpServFec129LocalVlanTag = _VLdpServFec129LocalVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 25),
    _VLdpServFec129LocalVlanTag_Type()
)
vLdpServFec129LocalVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalVlanTag.setStatus("current")
_VLdpServFec129RemoteVlanTag_Type = Unsigned32
_VLdpServFec129RemoteVlanTag_Object = MibTableColumn
vLdpServFec129RemoteVlanTag = _VLdpServFec129RemoteVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 26),
    _VLdpServFec129RemoteVlanTag_Type()
)
vLdpServFec129RemoteVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteVlanTag.setStatus("current")
_VLdpServFec129LocalMaxCellConcat_Type = Unsigned32
_VLdpServFec129LocalMaxCellConcat_Object = MibTableColumn
vLdpServFec129LocalMaxCellConcat = _VLdpServFec129LocalMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 27),
    _VLdpServFec129LocalMaxCellConcat_Type()
)
vLdpServFec129LocalMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129LocalMaxCellConcat.setStatus("current")
_VLdpServFec129RemoteMaxCellConcat_Type = Unsigned32
_VLdpServFec129RemoteMaxCellConcat_Object = MibTableColumn
vLdpServFec129RemoteMaxCellConcat = _VLdpServFec129RemoteMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 28),
    _VLdpServFec129RemoteMaxCellConcat_Type()
)
vLdpServFec129RemoteMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129RemoteMaxCellConcat.setStatus("current")
_VLdpServFec129InLabelSigStatus1_Type = TmnxLabelSigStatus
_VLdpServFec129InLabelSigStatus1_Object = MibTableColumn
vLdpServFec129InLabelSigStatus1 = _VLdpServFec129InLabelSigStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 29),
    _VLdpServFec129InLabelSigStatus1_Type()
)
vLdpServFec129InLabelSigStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129InLabelSigStatus1.setStatus("current")
_VLdpServFec129OutLabelSigStatus1_Type = TmnxLabelSigStatus
_VLdpServFec129OutLabelSigStatus1_Object = MibTableColumn
vLdpServFec129OutLabelSigStatus1 = _VLdpServFec129OutLabelSigStatus1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 23, 1, 30),
    _VLdpServFec129OutLabelSigStatus1_Type()
)
vLdpServFec129OutLabelSigStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129OutLabelSigStatus1.setStatus("current")
_VLdpServFec129MapTable_Object = MibTable
vLdpServFec129MapTable = _VLdpServFec129MapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24)
)
if mibBuilder.loadTexts:
    vLdpServFec129MapTable.setStatus("obsolete")
_VLdpServFec129MapEntry_Object = MibTableRow
vLdpServFec129MapEntry = _VLdpServFec129MapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24, 1)
)
vLdpServFec129MapEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerLdpId"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129MapVcType"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129MapAgiTlv"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129MapSrcAiiTlv"),
    (0, "ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129MapTgtAiiTlv"),
)
if mibBuilder.loadTexts:
    vLdpServFec129MapEntry.setStatus("obsolete")
_VLdpServFec129MapVcType_Type = TmnxVcType
_VLdpServFec129MapVcType_Object = MibTableColumn
vLdpServFec129MapVcType = _VLdpServFec129MapVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24, 1, 1),
    _VLdpServFec129MapVcType_Type()
)
vLdpServFec129MapVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MapVcType.setStatus("obsolete")
_VLdpServFec129MapAgiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129MapAgiTlv_Object = MibTableColumn
vLdpServFec129MapAgiTlv = _VLdpServFec129MapAgiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24, 1, 2),
    _VLdpServFec129MapAgiTlv_Type()
)
vLdpServFec129MapAgiTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MapAgiTlv.setStatus("obsolete")
_VLdpServFec129MapSrcAiiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129MapSrcAiiTlv_Object = MibTableColumn
vLdpServFec129MapSrcAiiTlv = _VLdpServFec129MapSrcAiiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24, 1, 3),
    _VLdpServFec129MapSrcAiiTlv_Type()
)
vLdpServFec129MapSrcAiiTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MapSrcAiiTlv.setStatus("obsolete")
_VLdpServFec129MapTgtAiiTlv_Type = TmnxLdpFec129Tlv
_VLdpServFec129MapTgtAiiTlv_Object = MibTableColumn
vLdpServFec129MapTgtAiiTlv = _VLdpServFec129MapTgtAiiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 24, 1, 4),
    _VLdpServFec129MapTgtAiiTlv_Type()
)
vLdpServFec129MapTgtAiiTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpServFec129MapTgtAiiTlv.setStatus("obsolete")
_VLdpCepTdmFec129Table_Object = MibTable
vLdpCepTdmFec129Table = _VLdpCepTdmFec129Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25)
)
if mibBuilder.loadTexts:
    vLdpCepTdmFec129Table.setStatus("current")
_VLdpCepTdmFec129Entry_Object = MibTableRow
vLdpCepTdmFec129Entry = _VLdpCepTdmFec129Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1)
)
if mibBuilder.loadTexts:
    vLdpCepTdmFec129Entry.setStatus("current")
_VLdpCepTdmFec129LocalPayloadSize_Type = Unsigned32
_VLdpCepTdmFec129LocalPayloadSize_Object = MibTableColumn
vLdpCepTdmFec129LocalPayloadSize = _VLdpCepTdmFec129LocalPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 4),
    _VLdpCepTdmFec129LocalPayloadSize_Type()
)
vLdpCepTdmFec129LocalPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalPayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalPayloadSize.setUnits("bytes")
_VLdpCepTdmFec129RemotePayloadSize_Type = Unsigned32
_VLdpCepTdmFec129RemotePayloadSize_Object = MibTableColumn
vLdpCepTdmFec129RemotePayloadSize = _VLdpCepTdmFec129RemotePayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 5),
    _VLdpCepTdmFec129RemotePayloadSize_Type()
)
vLdpCepTdmFec129RemotePayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemotePayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemotePayloadSize.setUnits("bytes")
_VLdpCepTdmFec129LocalBitrate_Type = Unsigned32
_VLdpCepTdmFec129LocalBitrate_Object = MibTableColumn
vLdpCepTdmFec129LocalBitrate = _VLdpCepTdmFec129LocalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 6),
    _VLdpCepTdmFec129LocalBitrate_Type()
)
vLdpCepTdmFec129LocalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalBitrate.setStatus("current")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalBitrate.setUnits("64 Kbits/s")
_VLdpCepTdmFec129RemoteBitrate_Type = Unsigned32
_VLdpCepTdmFec129RemoteBitrate_Object = MibTableColumn
vLdpCepTdmFec129RemoteBitrate = _VLdpCepTdmFec129RemoteBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 7),
    _VLdpCepTdmFec129RemoteBitrate_Type()
)
vLdpCepTdmFec129RemoteBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteBitrate.setStatus("current")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteBitrate.setUnits("64 Kbits/s")
_VLdpCepTdmFec129LocalRtpHeader_Type = TruthValue
_VLdpCepTdmFec129LocalRtpHeader_Object = MibTableColumn
vLdpCepTdmFec129LocalRtpHeader = _VLdpCepTdmFec129LocalRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 8),
    _VLdpCepTdmFec129LocalRtpHeader_Type()
)
vLdpCepTdmFec129LocalRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalRtpHeader.setStatus("current")
_VLdpCepTdmFec129RemoteRtpHeader_Type = TruthValue
_VLdpCepTdmFec129RemoteRtpHeader_Object = MibTableColumn
vLdpCepTdmFec129RemoteRtpHeader = _VLdpCepTdmFec129RemoteRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 9),
    _VLdpCepTdmFec129RemoteRtpHeader_Type()
)
vLdpCepTdmFec129RemoteRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteRtpHeader.setStatus("current")
_VLdpCepTdmFec129LocalDiffTimestamp_Type = TruthValue
_VLdpCepTdmFec129LocalDiffTimestamp_Object = MibTableColumn
vLdpCepTdmFec129LocalDiffTimestamp = _VLdpCepTdmFec129LocalDiffTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 10),
    _VLdpCepTdmFec129LocalDiffTimestamp_Type()
)
vLdpCepTdmFec129LocalDiffTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalDiffTimestamp.setStatus("current")
_VLdpCepTdmFec129RemoteDiffTimestamp_Type = TruthValue
_VLdpCepTdmFec129RemoteDiffTimestamp_Object = MibTableColumn
vLdpCepTdmFec129RemoteDiffTimestamp = _VLdpCepTdmFec129RemoteDiffTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 11),
    _VLdpCepTdmFec129RemoteDiffTimestamp_Type()
)
vLdpCepTdmFec129RemoteDiffTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteDiffTimestamp.setStatus("current")
_VLdpCepTdmFec129LocalSigPkts_Type = TdmOptionsSigPkts
_VLdpCepTdmFec129LocalSigPkts_Object = MibTableColumn
vLdpCepTdmFec129LocalSigPkts = _VLdpCepTdmFec129LocalSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 12),
    _VLdpCepTdmFec129LocalSigPkts_Type()
)
vLdpCepTdmFec129LocalSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalSigPkts.setStatus("current")
_VLdpCepTdmFec129RemoteSigPkts_Type = TdmOptionsSigPkts
_VLdpCepTdmFec129RemoteSigPkts_Object = MibTableColumn
vLdpCepTdmFec129RemoteSigPkts = _VLdpCepTdmFec129RemoteSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 13),
    _VLdpCepTdmFec129RemoteSigPkts_Type()
)
vLdpCepTdmFec129RemoteSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteSigPkts.setStatus("current")
_VLdpCepTdmFec129LocalCasTrunk_Type = TdmOptionsCasTrunkFraming
_VLdpCepTdmFec129LocalCasTrunk_Object = MibTableColumn
vLdpCepTdmFec129LocalCasTrunk = _VLdpCepTdmFec129LocalCasTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 14),
    _VLdpCepTdmFec129LocalCasTrunk_Type()
)
vLdpCepTdmFec129LocalCasTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalCasTrunk.setStatus("current")
_VLdpCepTdmFec129RemoteCasTrunk_Type = TdmOptionsCasTrunkFraming
_VLdpCepTdmFec129RemoteCasTrunk_Object = MibTableColumn
vLdpCepTdmFec129RemoteCasTrunk = _VLdpCepTdmFec129RemoteCasTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 15),
    _VLdpCepTdmFec129RemoteCasTrunk_Type()
)
vLdpCepTdmFec129RemoteCasTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteCasTrunk.setStatus("current")
_VLdpCepTdmFec129LocalTimestampFreq_Type = Unsigned32
_VLdpCepTdmFec129LocalTimestampFreq_Object = MibTableColumn
vLdpCepTdmFec129LocalTimestampFreq = _VLdpCepTdmFec129LocalTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 16),
    _VLdpCepTdmFec129LocalTimestampFreq_Type()
)
vLdpCepTdmFec129LocalTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalTimestampFreq.setStatus("current")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalTimestampFreq.setUnits("8 KHz")
_VLdpCepTdmFec129RemoteTimestampFreq_Type = Unsigned32
_VLdpCepTdmFec129RemoteTimestampFreq_Object = MibTableColumn
vLdpCepTdmFec129RemoteTimestampFreq = _VLdpCepTdmFec129RemoteTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 17),
    _VLdpCepTdmFec129RemoteTimestampFreq_Type()
)
vLdpCepTdmFec129RemoteTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteTimestampFreq.setStatus("current")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteTimestampFreq.setUnits("8 KHz")
_VLdpCepTdmFec129LocalPayloadType_Type = Unsigned32
_VLdpCepTdmFec129LocalPayloadType_Object = MibTableColumn
vLdpCepTdmFec129LocalPayloadType = _VLdpCepTdmFec129LocalPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 18),
    _VLdpCepTdmFec129LocalPayloadType_Type()
)
vLdpCepTdmFec129LocalPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalPayloadType.setStatus("current")
_VLdpCepTdmFec129RemotePayloadType_Type = Unsigned32
_VLdpCepTdmFec129RemotePayloadType_Object = MibTableColumn
vLdpCepTdmFec129RemotePayloadType = _VLdpCepTdmFec129RemotePayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 19),
    _VLdpCepTdmFec129RemotePayloadType_Type()
)
vLdpCepTdmFec129RemotePayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemotePayloadType.setStatus("current")
_VLdpCepTdmFec129LocalSsrcId_Type = Unsigned32
_VLdpCepTdmFec129LocalSsrcId_Object = MibTableColumn
vLdpCepTdmFec129LocalSsrcId = _VLdpCepTdmFec129LocalSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 20),
    _VLdpCepTdmFec129LocalSsrcId_Type()
)
vLdpCepTdmFec129LocalSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129LocalSsrcId.setStatus("current")
_VLdpCepTdmFec129RemoteSsrcId_Type = Unsigned32
_VLdpCepTdmFec129RemoteSsrcId_Object = MibTableColumn
vLdpCepTdmFec129RemoteSsrcId = _VLdpCepTdmFec129RemoteSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 8, 25, 1, 21),
    _VLdpCepTdmFec129RemoteSsrcId_Type()
)
vLdpCepTdmFec129RemoteSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpCepTdmFec129RemoteSsrcId.setStatus("current")
_TmnxLdpNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxLdpNotifyPrefix = _TmnxLdpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8)
)
_TmnxLdpNotifications_ObjectIdentity = ObjectIdentity
tmnxLdpNotifications = _TmnxLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0)
)
vRtrLdpGeneralEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-LDP-MIB",
     "vRtrLdpStatsEntry")
)
vRtrLdpStatsEntry.setIndexNames(*vRtrLdpGeneralEntry.getIndexNames())
vRtrLdpIfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-LDP-MIB",
     "vRtrLdpIfStatsEntry")
)
vRtrLdpIfStatsEntry.setIndexNames(*vRtrLdpIfEntry.getIndexNames())
vRtrLdpSessionEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-LDP-MIB",
     "vRtrLdpSessionStatsEntry")
)
vRtrLdpSessionStatsEntry.setIndexNames(*vRtrLdpSessionEntry.getIndexNames())
vRtrLdpHelloAdjEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-LDP-MIB",
     "vRtrLdpAdjBackoffEntry")
)
vRtrLdpAdjBackoffEntry.setIndexNames(*vRtrLdpHelloAdjEntry.getIndexNames())
vRtrLdpGeneralEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-LDP-MIB",
     "vRtrLdpTargEntry")
)
vRtrLdpTargEntry.setIndexNames(*vRtrLdpGeneralEntry.getIndexNames())
vRtrLdpServFecEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-LDP-MIB",
     "vRtrLdpCepTdmFecEntry")
)
vRtrLdpCepTdmFecEntry.setIndexNames(*vRtrLdpServFecEntry.getIndexNames())
vLdpServFec129Entry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-LDP-MIB",
     "vLdpCepTdmFec129Entry")
)
vLdpCepTdmFec129Entry.setIndexNames(*vLdpServFec129Entry.getIndexNames())

# Managed Objects groups

tmnxLdpAddrFecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 6)
)
tmnxLdpAddrFecGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecFlags"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecNumInLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecNumOutLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapFecType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpPrefix"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpMask"))
)
if mibBuilder.loadTexts:
    tmnxLdpAddrFecGroup.setStatus("obsolete")

tmnxLdpNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 7)
)
tmnxLdpNotifyObjsGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpInstanceNotifyReasonCode"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfNotifyReasonCode"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpNotifyLocalGroupID"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpNotifyRemoteGroupID"))
)
if mibBuilder.loadTexts:
    tmnxLdpNotifyObjsGroup.setStatus("current")

tmnxLdpAdjBackoffGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 10)
)
tmnxLdpAdjBackoffGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAdjInitBackoff"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAdjMaxBackoff"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAdjCurrentBackoff"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAdjWaitingTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAdjBackoffStatus"))
)
if mibBuilder.loadTexts:
    tmnxLdpAdjBackoffGroup.setStatus("current")

tmnxLdpObsoleteObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 11)
)
tmnxLdpObsoleteObjsGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpNotifyLocalServiceID"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpNotifyRemoteServiceID"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPolicyName"))
)
if mibBuilder.loadTexts:
    tmnxLdpObsoleteObjsGroup.setStatus("current")

tmnxLdpAdjR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 15)
)
tmnxLdpAdjR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjMapLdpId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalLdpId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjEntityIndex"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjIndex"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjHoldTimeRemaining"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjRemoteConfSeqNum"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjRemoteIpAddress"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjUpTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalConfSeqNum"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalIpAddress"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjInHelloMsgCount"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjOutHelloMsgCount"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjLocalHelloTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpHelloAdjRemoteHelloTimeout"))
)
if mibBuilder.loadTexts:
    tmnxLdpAdjR2r1Group.setStatus("current")

tmnxLdpSessionR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 16)
)
tmnxLdpSessionR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLocalLdpId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessEntityIndex"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLabelDistMethod"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLoopDetectForPV"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPathVectorLimit"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessAdjacencyType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessProtocolVersion"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLocalUdpPort"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPeerUdpPort"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLocalTcpPort"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPeerTcpPort"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLocalAddress"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPeerAddress"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessKAHoldTimeRemaining"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessMaxPduLength"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessUpTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLocalKATimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPeerKATimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsTargAdj"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLinkAdj"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsFECRecv"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsFECSent"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsHelloIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsHelloOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsKeepaliveIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsKeepaliveOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsInitIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsInitOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelMappingIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelMappingOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelRequestIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelRequestOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelReleaseIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelReleaseOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelWithdrawIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelWithdrawOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelAbortIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelAbortOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrWithdrawIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrWithdrawOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsNotificationIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsNotificationOut"))
)
if mibBuilder.loadTexts:
    tmnxLdpSessionR2r1Group.setStatus("obsolete")

tmnxLdpStaticFecV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 17)
)
tmnxLdpStaticFecV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecRowStatus"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecNextNHIndex"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecIngLabel"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecNumNH"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecOperIngLabel"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHRowStatus"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHIpAddr"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStaticFecNHEgrLabel"))
)
if mibBuilder.loadTexts:
    tmnxLdpStaticFecV3v0Group.setStatus("current")

tmnxLdpIfV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 19)
)
tmnxLdpIfV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfTableSpinlock"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfRowStatus"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfLastChange"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfAdminState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfOperState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfInheritance"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfKeepAliveFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfKeepAliveTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfHelloFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfHelloTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfBackoffTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfMaxBackoffTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfTransportAddrType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfPassiveMode"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfAutoCreate"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfOperDownReason"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfExistingAdjacencies"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerRowStatus"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerAuth"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerAuthKey"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerMinTTLValue"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerTTLLogId"))
)
if mibBuilder.loadTexts:
    tmnxLdpIfV3v0Group.setStatus("obsolete")

tmnxLdpGlobalV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 20)
)
tmnxLdpGlobalV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenLastChange"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenAdminState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenOperState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenLdpLsrId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenProtocolVersion"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenDeaggregateFec"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenKeepAliveFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenKeepAliveTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenHelloFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenHelloTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenRoutePreference"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenControlMode"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenDistMethod"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenRetentionMode"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTransportAddrType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenPropagatePolicy"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenLoopDetectCapable"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenHopLimit"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenPathVectorLimit"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenBackoffTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenMaxBackoffTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargKeepAliveFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargKeepAliveTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargPassiveMode"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargetedSessions"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenCreateTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenUpTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTunnelDownDampTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenOperDownReason"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTrustList"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsOperDownEvents"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsActiveSessions"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsActiveAdjacencies"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsActiveInterfaces"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsInactiveInterfaces"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsActiveTargSessions"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsInactiveTargSessions"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsAddrFECRecv"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsAddrFECSent"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSvcFECRecv"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSvcFECSent"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsAttemptedSessions"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejNoHelloErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejAdvErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejMaxPduErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejLabelRangeErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsBadLdpIdentifierErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsBadPduLengthErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsBadMessageLengthErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsBadTlvLengthErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsMalformedTlvValueErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsKeepAliveExpiredErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsShutdownNotifRecv"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsShutdownNotifSent"))
)
if mibBuilder.loadTexts:
    tmnxLdpGlobalV3v0Group.setStatus("obsolete")

tmnxLdpServFecV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 21)
)
tmnxLdpServFecV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecServType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecServId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecVpnId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecFlags"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecNumInLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecNumOutLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecSdpId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMTU"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMTU"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecLocalVlanTag"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteVlanTag"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMaxCellConcat"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMaxCellConcat"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapFecType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus5"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFecV4v0Group.setStatus("obsolete")

tmnxLdpGlobalV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 22)
)
tmnxLdpGlobalV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenLastChange"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenAdminState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenOperState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenLdpLsrId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenProtocolVersion"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenDeaggregateFec"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenKeepAliveFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenKeepAliveTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenHelloFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenHelloTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenRoutePreference"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenControlMode"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenDistMethod"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenRetentionMode"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTransportAddrType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenPropagatePolicy"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenLoopDetectCapable"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenHopLimit"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenPathVectorLimit"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenBackoffTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenMaxBackoffTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargKeepAliveFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargKeepAliveTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargHelloTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargPassiveMode"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTargetedSessions"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenCreateTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenUpTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenImportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenExportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTunnelDownDampTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenOperDownReason"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenGracefulRestart"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenGRNbrLiveTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenGRMaxRecoveryTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargImportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargExportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpTargTunnelPreference"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsOperDownEvents"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsActiveSessions"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsActiveAdjacencies"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsActiveInterfaces"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsInactiveInterfaces"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsActiveTargSessions"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsInactiveTargSessions"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsAddrFECRecv"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsAddrFECSent"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSvcFECRecv"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSvcFECSent"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsAttemptedSessions"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejNoHelloErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejAdvErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejMaxPduErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsSessRejLabelRangeErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsBadLdpIdentifierErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsBadPduLengthErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsBadMessageLengthErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsBadTlvLengthErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsMalformedTlvValueErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsKeepAliveExpiredErrors"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsShutdownNotifRecv"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStatsShutdownNotifSent"))
)
if mibBuilder.loadTexts:
    tmnxLdpGlobalV5v0Group.setStatus("current")

tmnxLdpIfV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 23)
)
tmnxLdpIfV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfTableSpinlock"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfRowStatus"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfLastChange"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfAdminState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfOperState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfInheritance"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfKeepAliveFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfKeepAliveTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfHelloFactor"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfHelloTimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfBackoffTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfMaxBackoffTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfTransportAddrType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfPassiveMode"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfAutoCreate"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfOperDownReason"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfExistingAdjacencies"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfTunneling"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfLspRowStatus"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerRowStatus"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerAuth"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerAuthKey"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerMinTTLValue"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerTTLLogId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpPeerAuthKeyChain"))
)
if mibBuilder.loadTexts:
    tmnxLdpIfV5v0Group.setStatus("current")

tmnxLdpServFecV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 24)
)
tmnxLdpServFecV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecServType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecServId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecVpnId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecFlags"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecNumInLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecNumOutLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecSdpId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMTU"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMTU"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecLocalVlanTag"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteVlanTag"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMaxCellConcat"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMaxCellConcat"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapFecType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMateEndpointVcId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMateEndpointSdpId"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFecV5v0Group.setStatus("obsolete")

tmnxLdpAddrFecV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 25)
)
tmnxLdpAddrFecV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecFlags"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecNumInLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecNumOutLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabel5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecInLabelIfIndex5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabel5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelIfIndex5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecOutLabelNextHop5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecLspId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapFecType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpPrefix"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpAddrFecMapIpMask"))
)
if mibBuilder.loadTexts:
    tmnxLdpAddrFecV5v0Group.setStatus("current")

tmnxLdpSessionV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 26)
)
tmnxLdpSessionV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLocalLdpId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessEntityIndex"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLabelDistMethod"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLoopDetectForPV"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPathVectorLimit"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessAdjacencyType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessProtocolVersion"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLocalUdpPort"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPeerUdpPort"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLocalTcpPort"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPeerTcpPort"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLocalAddress"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPeerAddress"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessKAHoldTimeRemaining"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessMaxPduLength"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessUpTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLocalKATimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPeerKATimeout"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessAdvertise"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessRestartHelperState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessPeerNumRestart"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessLastRestartTime"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessFtReconnectTimeNego"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessFtRecoveryTimeNego"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessFtReconTimeRemaining"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessFtRecovTimeRemaining"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsTargAdj"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLinkAdj"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsFECRecv"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsFECSent"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsHelloIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsHelloOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsKeepaliveIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsKeepaliveOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsInitIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsInitOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelMappingIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelMappingOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelRequestIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelRequestOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelReleaseIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelReleaseOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelWithdrawIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelWithdrawOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelAbortIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsLabelAbortOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrWithdrawIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsAddrWithdrawOut"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsNotificationIn"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSessStatsNotificationOut"))
)
if mibBuilder.loadTexts:
    tmnxLdpSessionV5v0Group.setStatus("current")

tmnxLdpObsoletedV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 27)
)
tmnxLdpObsoletedV5v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenTrustList")
)
if mibBuilder.loadTexts:
    tmnxLdpObsoletedV5v0Group.setStatus("current")

tmnxLdpCepTdmFecV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 28)
)
tmnxLdpCepTdmFecV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalPayloadSize"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemotePayloadSize"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalBitrate"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteBitrate"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalRtpHeader"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteRtpHeader"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalDiffTimestamp"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteDiffTimestamp"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalSigPkts"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteSigPkts"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalCasTrunk"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteCasTrunk"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalTimestampFreq"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteTimestampFreq"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalPayloadType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemotePayloadType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmLocalSsrcId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpCepTdmRemoteSsrcId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalPayloadSize"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemotePayloadSize"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalBitrate"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteBitrate"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalRtpHeader"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteRtpHeader"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalDiffTimestamp"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteDiffTimestamp"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalSigPkts"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteSigPkts"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalCasTrunk"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteCasTrunk"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalTimestampFreq"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteTimestampFreq"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalPayloadType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemotePayloadType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129LocalSsrcId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpCepTdmFec129RemoteSsrcId"))
)
if mibBuilder.loadTexts:
    tmnxLdpCepTdmFecV6v0Group.setStatus("current")

tmnxLdpServFecV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 29)
)
tmnxLdpServFecV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecServType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecServId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecVpnId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecFlags"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecNumInLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecNumOutLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabel5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabel5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecSdpId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMTU"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMTU"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecLocalVlanTag"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteVlanTag"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecLocalMaxCellConcat"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecRemoteMaxCellConcat"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecInLabelSigStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus2"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus3"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus4"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecOutLabelSigStatus5"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMateEndpointVcId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMateEndpointSdpId"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFecV6v0Group.setStatus("current")

tmnxLdpServFec129V6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 30)
)
tmnxLdpServFec129V6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129ServType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129ServId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129VpnId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129Flags"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129NumInLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129NumOutLabels"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129InLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129InLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129OutLabel1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129OutLabelStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129SdpId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129LocalMTU"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129RemoteMTU"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129LocalVlanTag"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129RemoteVlanTag"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129LocalMaxCellConcat"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129RemoteMaxCellConcat"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129InLabelSigStatus1"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129OutLabelSigStatus1"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFec129V6v0Group.setStatus("current")

tmnxLdpServFecObsoletedV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 31)
)
tmnxLdpServFecObsoletedV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapFecType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpServFecMapVcId"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129MapVcType"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129MapAgiTlv"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129MapSrcAiiTlv"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vLdpServFec129MapTgtAiiTlv"))
)
if mibBuilder.loadTexts:
    tmnxLdpServFecObsoletedV6v0Group.setStatus("current")


# Notification objects

vRtrLdpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 1)
)
vRtrLdpStateChange.setObjects(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrLdpStatus")
)
if mibBuilder.loadTexts:
    vRtrLdpStateChange.setStatus(
        "current"
    )

vRtrLdpInstanceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 2)
)
vRtrLdpInstanceStateChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenAdminState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGenOperState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpInstanceNotifyReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrLdpInstanceStateChange.setStatus(
        "current"
    )

vRtrLdpIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 3)
)
vRtrLdpIfStateChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfAdminState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfOperState"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfNotifyReasonCode"))
)
if mibBuilder.loadTexts:
    vRtrLdpIfStateChange.setStatus(
        "current"
    )

vRtrLdpSvcIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 4)
)
vRtrLdpSvcIdMismatch.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpNotifyLocalServiceID"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpNotifyRemoteServiceID"))
)
if mibBuilder.loadTexts:
    vRtrLdpSvcIdMismatch.setStatus(
        "obsolete"
    )

vRtrLdpGroupIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 8, 0, 5)
)
vRtrLdpGroupIdMismatch.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpNotifyLocalGroupID"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpNotifyRemoteGroupID"))
)
if mibBuilder.loadTexts:
    vRtrLdpGroupIdMismatch.setStatus(
        "current"
    )


# Notifications groups

tmnxLdpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 8)
)
tmnxLdpNotificationGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpStateChange"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpInstanceStateChange"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpIfStateChange"),
        ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpGroupIdMismatch"))
)
if mibBuilder.loadTexts:
    tmnxLdpNotificationGroup.setStatus(
        "current"
    )

tmnxLdpObsoleteNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 2, 12)
)
tmnxLdpObsoleteNotificationGroup.setObjects(
    ("ALCATEL-IND1-TIMETRA-LDP-MIB", "vRtrLdpSvcIdMismatch")
)
if mibBuilder.loadTexts:
    tmnxLdpObsoleteNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxLdpV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxLdpV4v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxLdpV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 8, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxLdpV6v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-LDP-MIB",
    **{"TmnxLdpKeepAliveFactor": TmnxLdpKeepAliveFactor,
       "TmnxLdpKeepAliveTimeout": TmnxLdpKeepAliveTimeout,
       "TmnxLdpHelloFactor": TmnxLdpHelloFactor,
       "TmnxLdpHelloTimeout": TmnxLdpHelloTimeout,
       "TmnxLdpBackoffTime": TmnxLdpBackoffTime,
       "TmnxLdpFECPolicy": TmnxLdpFECPolicy,
       "TmnxLdpLabelDistMethod": TmnxLdpLabelDistMethod,
       "TmnxLdpAdjacencyType": TmnxLdpAdjacencyType,
       "TmnxVpnId": TmnxVpnId,
       "TmnxLabelStatus": TmnxLabelStatus,
       "TmnxLabelSigStatus": TmnxLabelSigStatus,
       "TmnxLdpFECType": TmnxLdpFECType,
       "TmnxLdpFECFlags": TmnxLdpFECFlags,
       "TmnxLdpGenOperDownReasonCode": TmnxLdpGenOperDownReasonCode,
       "TmnxLdpIntTargOperDownReasonCode": TmnxLdpIntTargOperDownReasonCode,
       "TmnxLdpFec129Tlv": TmnxLdpFec129Tlv,
       "timetraLdpMIBModule": timetraLdpMIBModule,
       "tmnxLdpConformance": tmnxLdpConformance,
       "tmnxLdpCompliances": tmnxLdpCompliances,
       "tmnxLdpV4v0Compliance": tmnxLdpV4v0Compliance,
       "tmnxLdpV5v0Compliance": tmnxLdpV5v0Compliance,
       "tmnxLdpV6v0Compliance": tmnxLdpV6v0Compliance,
       "tmnxLdpGroups": tmnxLdpGroups,
       "tmnxLdpAddrFecGroup": tmnxLdpAddrFecGroup,
       "tmnxLdpNotifyObjsGroup": tmnxLdpNotifyObjsGroup,
       "tmnxLdpNotificationGroup": tmnxLdpNotificationGroup,
       "tmnxLdpAdjBackoffGroup": tmnxLdpAdjBackoffGroup,
       "tmnxLdpObsoleteObjsGroup": tmnxLdpObsoleteObjsGroup,
       "tmnxLdpObsoleteNotificationGroup": tmnxLdpObsoleteNotificationGroup,
       "tmnxLdpAdjR2r1Group": tmnxLdpAdjR2r1Group,
       "tmnxLdpSessionR2r1Group": tmnxLdpSessionR2r1Group,
       "tmnxLdpStaticFecV3v0Group": tmnxLdpStaticFecV3v0Group,
       "tmnxLdpIfV3v0Group": tmnxLdpIfV3v0Group,
       "tmnxLdpGlobalV3v0Group": tmnxLdpGlobalV3v0Group,
       "tmnxLdpServFecV4v0Group": tmnxLdpServFecV4v0Group,
       "tmnxLdpGlobalV5v0Group": tmnxLdpGlobalV5v0Group,
       "tmnxLdpIfV5v0Group": tmnxLdpIfV5v0Group,
       "tmnxLdpServFecV5v0Group": tmnxLdpServFecV5v0Group,
       "tmnxLdpAddrFecV5v0Group": tmnxLdpAddrFecV5v0Group,
       "tmnxLdpSessionV5v0Group": tmnxLdpSessionV5v0Group,
       "tmnxLdpObsoletedV5v0Group": tmnxLdpObsoletedV5v0Group,
       "tmnxLdpCepTdmFecV6v0Group": tmnxLdpCepTdmFecV6v0Group,
       "tmnxLdpServFecV6v0Group": tmnxLdpServFecV6v0Group,
       "tmnxLdpServFec129V6v0Group": tmnxLdpServFec129V6v0Group,
       "tmnxLdpServFecObsoletedV6v0Group": tmnxLdpServFecObsoletedV6v0Group,
       "tmnxLdpObjs": tmnxLdpObjs,
       "vRtrLdpGeneralTable": vRtrLdpGeneralTable,
       "vRtrLdpGeneralEntry": vRtrLdpGeneralEntry,
       "vRtrLdpGenLastChange": vRtrLdpGenLastChange,
       "vRtrLdpGenAdminState": vRtrLdpGenAdminState,
       "vRtrLdpGenOperState": vRtrLdpGenOperState,
       "vRtrLdpGenLdpLsrId": vRtrLdpGenLdpLsrId,
       "vRtrLdpGenProtocolVersion": vRtrLdpGenProtocolVersion,
       "vRtrLdpGenDeaggregateFec": vRtrLdpGenDeaggregateFec,
       "vRtrLdpGenKeepAliveFactor": vRtrLdpGenKeepAliveFactor,
       "vRtrLdpGenKeepAliveTimeout": vRtrLdpGenKeepAliveTimeout,
       "vRtrLdpGenHelloFactor": vRtrLdpGenHelloFactor,
       "vRtrLdpGenHelloTimeout": vRtrLdpGenHelloTimeout,
       "vRtrLdpGenRoutePreference": vRtrLdpGenRoutePreference,
       "vRtrLdpGenControlMode": vRtrLdpGenControlMode,
       "vRtrLdpGenDistMethod": vRtrLdpGenDistMethod,
       "vRtrLdpGenRetentionMode": vRtrLdpGenRetentionMode,
       "vRtrLdpGenTransportAddrType": vRtrLdpGenTransportAddrType,
       "vRtrLdpGenPropagatePolicy": vRtrLdpGenPropagatePolicy,
       "vRtrLdpGenLoopDetectCapable": vRtrLdpGenLoopDetectCapable,
       "vRtrLdpGenHopLimit": vRtrLdpGenHopLimit,
       "vRtrLdpGenPathVectorLimit": vRtrLdpGenPathVectorLimit,
       "vRtrLdpGenBackoffTime": vRtrLdpGenBackoffTime,
       "vRtrLdpGenMaxBackoffTime": vRtrLdpGenMaxBackoffTime,
       "vRtrLdpGenTargKeepAliveFactor": vRtrLdpGenTargKeepAliveFactor,
       "vRtrLdpGenTargKeepAliveTimeout": vRtrLdpGenTargKeepAliveTimeout,
       "vRtrLdpGenTargHelloFactor": vRtrLdpGenTargHelloFactor,
       "vRtrLdpGenTargHelloTimeout": vRtrLdpGenTargHelloTimeout,
       "vRtrLdpGenTargPassiveMode": vRtrLdpGenTargPassiveMode,
       "vRtrLdpGenTargetedSessions": vRtrLdpGenTargetedSessions,
       "vRtrLdpGenCreateTime": vRtrLdpGenCreateTime,
       "vRtrLdpGenUpTime": vRtrLdpGenUpTime,
       "vRtrLdpGenImportPolicy1": vRtrLdpGenImportPolicy1,
       "vRtrLdpGenImportPolicy2": vRtrLdpGenImportPolicy2,
       "vRtrLdpGenImportPolicy3": vRtrLdpGenImportPolicy3,
       "vRtrLdpGenImportPolicy4": vRtrLdpGenImportPolicy4,
       "vRtrLdpGenImportPolicy5": vRtrLdpGenImportPolicy5,
       "vRtrLdpGenExportPolicy1": vRtrLdpGenExportPolicy1,
       "vRtrLdpGenExportPolicy2": vRtrLdpGenExportPolicy2,
       "vRtrLdpGenExportPolicy3": vRtrLdpGenExportPolicy3,
       "vRtrLdpGenExportPolicy4": vRtrLdpGenExportPolicy4,
       "vRtrLdpGenExportPolicy5": vRtrLdpGenExportPolicy5,
       "vRtrLdpGenTunnelDownDampTime": vRtrLdpGenTunnelDownDampTime,
       "vRtrLdpGenOperDownReason": vRtrLdpGenOperDownReason,
       "vRtrLdpGenTrustList": vRtrLdpGenTrustList,
       "vRtrLdpGenGracefulRestart": vRtrLdpGenGracefulRestart,
       "vRtrLdpGenGRNbrLiveTime": vRtrLdpGenGRNbrLiveTime,
       "vRtrLdpGenGRMaxRecoveryTime": vRtrLdpGenGRMaxRecoveryTime,
       "vRtrLdpStatsTable": vRtrLdpStatsTable,
       "vRtrLdpStatsEntry": vRtrLdpStatsEntry,
       "vRtrLdpStatsOperDownEvents": vRtrLdpStatsOperDownEvents,
       "vRtrLdpStatsActiveSessions": vRtrLdpStatsActiveSessions,
       "vRtrLdpStatsActiveAdjacencies": vRtrLdpStatsActiveAdjacencies,
       "vRtrLdpStatsActiveInterfaces": vRtrLdpStatsActiveInterfaces,
       "vRtrLdpStatsInactiveInterfaces": vRtrLdpStatsInactiveInterfaces,
       "vRtrLdpStatsActiveTargSessions": vRtrLdpStatsActiveTargSessions,
       "vRtrLdpStatsInactiveTargSessions": vRtrLdpStatsInactiveTargSessions,
       "vRtrLdpStatsAddrFECRecv": vRtrLdpStatsAddrFECRecv,
       "vRtrLdpStatsAddrFECSent": vRtrLdpStatsAddrFECSent,
       "vRtrLdpStatsSvcFECRecv": vRtrLdpStatsSvcFECRecv,
       "vRtrLdpStatsSvcFECSent": vRtrLdpStatsSvcFECSent,
       "vRtrLdpStatsAttemptedSessions": vRtrLdpStatsAttemptedSessions,
       "vRtrLdpStatsSessRejNoHelloErrors": vRtrLdpStatsSessRejNoHelloErrors,
       "vRtrLdpStatsSessRejAdvErrors": vRtrLdpStatsSessRejAdvErrors,
       "vRtrLdpStatsSessRejMaxPduErrors": vRtrLdpStatsSessRejMaxPduErrors,
       "vRtrLdpStatsSessRejLabelRangeErrors": vRtrLdpStatsSessRejLabelRangeErrors,
       "vRtrLdpStatsBadLdpIdentifierErrors": vRtrLdpStatsBadLdpIdentifierErrors,
       "vRtrLdpStatsBadPduLengthErrors": vRtrLdpStatsBadPduLengthErrors,
       "vRtrLdpStatsBadMessageLengthErrors": vRtrLdpStatsBadMessageLengthErrors,
       "vRtrLdpStatsBadTlvLengthErrors": vRtrLdpStatsBadTlvLengthErrors,
       "vRtrLdpStatsMalformedTlvValueErrors": vRtrLdpStatsMalformedTlvValueErrors,
       "vRtrLdpStatsKeepAliveExpiredErrors": vRtrLdpStatsKeepAliveExpiredErrors,
       "vRtrLdpStatsShutdownNotifRecv": vRtrLdpStatsShutdownNotifRecv,
       "vRtrLdpStatsShutdownNotifSent": vRtrLdpStatsShutdownNotifSent,
       "vRtrLdpPolicyTable": vRtrLdpPolicyTable,
       "vRtrLdpPolicyEntry": vRtrLdpPolicyEntry,
       "vRtrLdpPolicyType": vRtrLdpPolicyType,
       "vRtrLdpPolicyIndex": vRtrLdpPolicyIndex,
       "vRtrLdpPolicyRowStatus": vRtrLdpPolicyRowStatus,
       "vRtrLdpPolicyName": vRtrLdpPolicyName,
       "vRtrLdpIfTableSpinlock": vRtrLdpIfTableSpinlock,
       "vRtrLdpIfTable": vRtrLdpIfTable,
       "vRtrLdpIfEntry": vRtrLdpIfEntry,
       "vRtrLdpIfIndex": vRtrLdpIfIndex,
       "vRtrLdpPeerAddress": vRtrLdpPeerAddress,
       "vRtrLdpIfRowStatus": vRtrLdpIfRowStatus,
       "vRtrLdpIfLastChange": vRtrLdpIfLastChange,
       "vRtrLdpIfAdminState": vRtrLdpIfAdminState,
       "vRtrLdpIfOperState": vRtrLdpIfOperState,
       "vRtrLdpIfInheritance": vRtrLdpIfInheritance,
       "vRtrLdpIfKeepAliveFactor": vRtrLdpIfKeepAliveFactor,
       "vRtrLdpIfKeepAliveTimeout": vRtrLdpIfKeepAliveTimeout,
       "vRtrLdpIfHelloFactor": vRtrLdpIfHelloFactor,
       "vRtrLdpIfHelloTimeout": vRtrLdpIfHelloTimeout,
       "vRtrLdpIfBackoffTime": vRtrLdpIfBackoffTime,
       "vRtrLdpIfMaxBackoffTime": vRtrLdpIfMaxBackoffTime,
       "vRtrLdpIfTransportAddrType": vRtrLdpIfTransportAddrType,
       "vRtrLdpIfPassiveMode": vRtrLdpIfPassiveMode,
       "vRtrLdpIfAutoCreate": vRtrLdpIfAutoCreate,
       "vRtrLdpIfOperDownReason": vRtrLdpIfOperDownReason,
       "vRtrLdpIfTunneling": vRtrLdpIfTunneling,
       "vRtrLdpIfStatsTable": vRtrLdpIfStatsTable,
       "vRtrLdpIfStatsEntry": vRtrLdpIfStatsEntry,
       "vRtrLdpIfExistingAdjacencies": vRtrLdpIfExistingAdjacencies,
       "vRtrLdpHelloAdjTable": vRtrLdpHelloAdjTable,
       "vRtrLdpHelloAdjEntry": vRtrLdpHelloAdjEntry,
       "vRtrLdpPeerLdpId": vRtrLdpPeerLdpId,
       "vRtrLdpHelloAdjLocalLdpId": vRtrLdpHelloAdjLocalLdpId,
       "vRtrLdpHelloAdjEntityIndex": vRtrLdpHelloAdjEntityIndex,
       "vRtrLdpHelloAdjIndex": vRtrLdpHelloAdjIndex,
       "vRtrLdpHelloAdjHoldTimeRemaining": vRtrLdpHelloAdjHoldTimeRemaining,
       "vRtrLdpHelloAdjType": vRtrLdpHelloAdjType,
       "vRtrLdpHelloAdjRemoteConfSeqNum": vRtrLdpHelloAdjRemoteConfSeqNum,
       "vRtrLdpHelloAdjRemoteIpAddress": vRtrLdpHelloAdjRemoteIpAddress,
       "vRtrLdpHelloAdjUpTime": vRtrLdpHelloAdjUpTime,
       "vRtrLdpHelloAdjLocalConfSeqNum": vRtrLdpHelloAdjLocalConfSeqNum,
       "vRtrLdpHelloAdjLocalIpAddress": vRtrLdpHelloAdjLocalIpAddress,
       "vRtrLdpHelloAdjInHelloMsgCount": vRtrLdpHelloAdjInHelloMsgCount,
       "vRtrLdpHelloAdjOutHelloMsgCount": vRtrLdpHelloAdjOutHelloMsgCount,
       "vRtrLdpHelloAdjLocalHelloTimeout": vRtrLdpHelloAdjLocalHelloTimeout,
       "vRtrLdpHelloAdjRemoteHelloTimeout": vRtrLdpHelloAdjRemoteHelloTimeout,
       "vRtrLdpHelloAdjMapTable": vRtrLdpHelloAdjMapTable,
       "vRtrLdpHelloAdjMapEntry": vRtrLdpHelloAdjMapEntry,
       "vRtrLdpHelloAdjMapLdpId": vRtrLdpHelloAdjMapLdpId,
       "vRtrLdpSessionTable": vRtrLdpSessionTable,
       "vRtrLdpSessionEntry": vRtrLdpSessionEntry,
       "vRtrLdpSessLocalLdpId": vRtrLdpSessLocalLdpId,
       "vRtrLdpSessEntityIndex": vRtrLdpSessEntityIndex,
       "vRtrLdpSessLabelDistMethod": vRtrLdpSessLabelDistMethod,
       "vRtrLdpSessLoopDetectForPV": vRtrLdpSessLoopDetectForPV,
       "vRtrLdpSessPathVectorLimit": vRtrLdpSessPathVectorLimit,
       "vRtrLdpSessState": vRtrLdpSessState,
       "vRtrLdpSessAdjacencyType": vRtrLdpSessAdjacencyType,
       "vRtrLdpSessProtocolVersion": vRtrLdpSessProtocolVersion,
       "vRtrLdpSessLocalUdpPort": vRtrLdpSessLocalUdpPort,
       "vRtrLdpSessPeerUdpPort": vRtrLdpSessPeerUdpPort,
       "vRtrLdpSessLocalTcpPort": vRtrLdpSessLocalTcpPort,
       "vRtrLdpSessPeerTcpPort": vRtrLdpSessPeerTcpPort,
       "vRtrLdpSessLocalAddress": vRtrLdpSessLocalAddress,
       "vRtrLdpSessPeerAddress": vRtrLdpSessPeerAddress,
       "vRtrLdpSessKAHoldTimeRemaining": vRtrLdpSessKAHoldTimeRemaining,
       "vRtrLdpSessMaxPduLength": vRtrLdpSessMaxPduLength,
       "vRtrLdpSessUpTime": vRtrLdpSessUpTime,
       "vRtrLdpSessLocalKATimeout": vRtrLdpSessLocalKATimeout,
       "vRtrLdpSessPeerKATimeout": vRtrLdpSessPeerKATimeout,
       "vRtrLdpSessAdvertise": vRtrLdpSessAdvertise,
       "vRtrLdpSessRestartHelperState": vRtrLdpSessRestartHelperState,
       "vRtrLdpSessPeerNumRestart": vRtrLdpSessPeerNumRestart,
       "vRtrLdpSessLastRestartTime": vRtrLdpSessLastRestartTime,
       "vRtrLdpSessFtReconnectTimeNego": vRtrLdpSessFtReconnectTimeNego,
       "vRtrLdpSessFtRecoveryTimeNego": vRtrLdpSessFtRecoveryTimeNego,
       "vRtrLdpSessFtReconTimeRemaining": vRtrLdpSessFtReconTimeRemaining,
       "vRtrLdpSessFtRecovTimeRemaining": vRtrLdpSessFtRecovTimeRemaining,
       "vRtrLdpSessionStatsTable": vRtrLdpSessionStatsTable,
       "vRtrLdpSessionStatsEntry": vRtrLdpSessionStatsEntry,
       "vRtrLdpSessStatsTargAdj": vRtrLdpSessStatsTargAdj,
       "vRtrLdpSessStatsLinkAdj": vRtrLdpSessStatsLinkAdj,
       "vRtrLdpSessStatsFECRecv": vRtrLdpSessStatsFECRecv,
       "vRtrLdpSessStatsFECSent": vRtrLdpSessStatsFECSent,
       "vRtrLdpSessStatsHelloIn": vRtrLdpSessStatsHelloIn,
       "vRtrLdpSessStatsHelloOut": vRtrLdpSessStatsHelloOut,
       "vRtrLdpSessStatsKeepaliveIn": vRtrLdpSessStatsKeepaliveIn,
       "vRtrLdpSessStatsKeepaliveOut": vRtrLdpSessStatsKeepaliveOut,
       "vRtrLdpSessStatsInitIn": vRtrLdpSessStatsInitIn,
       "vRtrLdpSessStatsInitOut": vRtrLdpSessStatsInitOut,
       "vRtrLdpSessStatsLabelMappingIn": vRtrLdpSessStatsLabelMappingIn,
       "vRtrLdpSessStatsLabelMappingOut": vRtrLdpSessStatsLabelMappingOut,
       "vRtrLdpSessStatsLabelRequestIn": vRtrLdpSessStatsLabelRequestIn,
       "vRtrLdpSessStatsLabelRequestOut": vRtrLdpSessStatsLabelRequestOut,
       "vRtrLdpSessStatsLabelReleaseIn": vRtrLdpSessStatsLabelReleaseIn,
       "vRtrLdpSessStatsLabelReleaseOut": vRtrLdpSessStatsLabelReleaseOut,
       "vRtrLdpSessStatsLabelWithdrawIn": vRtrLdpSessStatsLabelWithdrawIn,
       "vRtrLdpSessStatsLabelWithdrawOut": vRtrLdpSessStatsLabelWithdrawOut,
       "vRtrLdpSessStatsLabelAbortIn": vRtrLdpSessStatsLabelAbortIn,
       "vRtrLdpSessStatsLabelAbortOut": vRtrLdpSessStatsLabelAbortOut,
       "vRtrLdpSessStatsAddrIn": vRtrLdpSessStatsAddrIn,
       "vRtrLdpSessStatsAddrOut": vRtrLdpSessStatsAddrOut,
       "vRtrLdpSessStatsAddrWithdrawIn": vRtrLdpSessStatsAddrWithdrawIn,
       "vRtrLdpSessStatsAddrWithdrawOut": vRtrLdpSessStatsAddrWithdrawOut,
       "vRtrLdpSessStatsNotificationIn": vRtrLdpSessStatsNotificationIn,
       "vRtrLdpSessStatsNotificationOut": vRtrLdpSessStatsNotificationOut,
       "vRtrLdpServFecTable": vRtrLdpServFecTable,
       "vRtrLdpServFecEntry": vRtrLdpServFecEntry,
       "vRtrLdpServFecFecType": vRtrLdpServFecFecType,
       "vRtrLdpServFecVcType": vRtrLdpServFecVcType,
       "vRtrLdpServFecVcId": vRtrLdpServFecVcId,
       "vRtrLdpServFecServType": vRtrLdpServFecServType,
       "vRtrLdpServFecServId": vRtrLdpServFecServId,
       "vRtrLdpServFecVpnId": vRtrLdpServFecVpnId,
       "vRtrLdpServFecFlags": vRtrLdpServFecFlags,
       "vRtrLdpServFecNumInLabels": vRtrLdpServFecNumInLabels,
       "vRtrLdpServFecNumOutLabels": vRtrLdpServFecNumOutLabels,
       "vRtrLdpServFecInLabel1": vRtrLdpServFecInLabel1,
       "vRtrLdpServFecInLabelStatus1": vRtrLdpServFecInLabelStatus1,
       "vRtrLdpServFecInLabel2": vRtrLdpServFecInLabel2,
       "vRtrLdpServFecInLabelStatus2": vRtrLdpServFecInLabelStatus2,
       "vRtrLdpServFecInLabel3": vRtrLdpServFecInLabel3,
       "vRtrLdpServFecInLabelStatus3": vRtrLdpServFecInLabelStatus3,
       "vRtrLdpServFecInLabel4": vRtrLdpServFecInLabel4,
       "vRtrLdpServFecInLabelStatus4": vRtrLdpServFecInLabelStatus4,
       "vRtrLdpServFecInLabel5": vRtrLdpServFecInLabel5,
       "vRtrLdpServFecInLabelStatus5": vRtrLdpServFecInLabelStatus5,
       "vRtrLdpServFecOutLabel1": vRtrLdpServFecOutLabel1,
       "vRtrLdpServFecOutLabelStatus1": vRtrLdpServFecOutLabelStatus1,
       "vRtrLdpServFecOutLabel2": vRtrLdpServFecOutLabel2,
       "vRtrLdpServFecOutLabelStatus2": vRtrLdpServFecOutLabelStatus2,
       "vRtrLdpServFecOutLabel3": vRtrLdpServFecOutLabel3,
       "vRtrLdpServFecOutLabelStatus3": vRtrLdpServFecOutLabelStatus3,
       "vRtrLdpServFecOutLabel4": vRtrLdpServFecOutLabel4,
       "vRtrLdpServFecOutLabelStatus4": vRtrLdpServFecOutLabelStatus4,
       "vRtrLdpServFecOutLabel5": vRtrLdpServFecOutLabel5,
       "vRtrLdpServFecOutLabelStatus5": vRtrLdpServFecOutLabelStatus5,
       "vRtrLdpServFecSdpId": vRtrLdpServFecSdpId,
       "vRtrLdpServFecLocalMTU": vRtrLdpServFecLocalMTU,
       "vRtrLdpServFecRemoteMTU": vRtrLdpServFecRemoteMTU,
       "vRtrLdpServFecLocalVlanTag": vRtrLdpServFecLocalVlanTag,
       "vRtrLdpServFecRemoteVlanTag": vRtrLdpServFecRemoteVlanTag,
       "vRtrLdpServFecLocalMaxCellConcat": vRtrLdpServFecLocalMaxCellConcat,
       "vRtrLdpServFecRemoteMaxCellConcat": vRtrLdpServFecRemoteMaxCellConcat,
       "vRtrLdpServFecInLabelSigStatus1": vRtrLdpServFecInLabelSigStatus1,
       "vRtrLdpServFecInLabelSigStatus2": vRtrLdpServFecInLabelSigStatus2,
       "vRtrLdpServFecInLabelSigStatus3": vRtrLdpServFecInLabelSigStatus3,
       "vRtrLdpServFecInLabelSigStatus4": vRtrLdpServFecInLabelSigStatus4,
       "vRtrLdpServFecInLabelSigStatus5": vRtrLdpServFecInLabelSigStatus5,
       "vRtrLdpServFecOutLabelSigStatus1": vRtrLdpServFecOutLabelSigStatus1,
       "vRtrLdpServFecOutLabelSigStatus2": vRtrLdpServFecOutLabelSigStatus2,
       "vRtrLdpServFecOutLabelSigStatus3": vRtrLdpServFecOutLabelSigStatus3,
       "vRtrLdpServFecOutLabelSigStatus4": vRtrLdpServFecOutLabelSigStatus4,
       "vRtrLdpServFecOutLabelSigStatus5": vRtrLdpServFecOutLabelSigStatus5,
       "vRtrLdpServFecMateEndpointVcId": vRtrLdpServFecMateEndpointVcId,
       "vRtrLdpServFecMateEndpointSdpId": vRtrLdpServFecMateEndpointSdpId,
       "vRtrLdpServFecMapTable": vRtrLdpServFecMapTable,
       "vRtrLdpServFecMapEntry": vRtrLdpServFecMapEntry,
       "vRtrLdpServFecMapFecType": vRtrLdpServFecMapFecType,
       "vRtrLdpServFecMapVcType": vRtrLdpServFecMapVcType,
       "vRtrLdpServFecMapVcId": vRtrLdpServFecMapVcId,
       "vRtrLdpAddrFecTable": vRtrLdpAddrFecTable,
       "vRtrLdpAddrFecEntry": vRtrLdpAddrFecEntry,
       "vRtrLdpAddrFecFecType": vRtrLdpAddrFecFecType,
       "vRtrLdpAddrFecIpPrefix": vRtrLdpAddrFecIpPrefix,
       "vRtrLdpAddrFecIpMask": vRtrLdpAddrFecIpMask,
       "vRtrLdpAddrFecFlags": vRtrLdpAddrFecFlags,
       "vRtrLdpAddrFecNumInLabels": vRtrLdpAddrFecNumInLabels,
       "vRtrLdpAddrFecNumOutLabels": vRtrLdpAddrFecNumOutLabels,
       "vRtrLdpAddrFecInLabel1": vRtrLdpAddrFecInLabel1,
       "vRtrLdpAddrFecInLabelStatus1": vRtrLdpAddrFecInLabelStatus1,
       "vRtrLdpAddrFecInLabelIfIndex1": vRtrLdpAddrFecInLabelIfIndex1,
       "vRtrLdpAddrFecInLabel2": vRtrLdpAddrFecInLabel2,
       "vRtrLdpAddrFecInLabelStatus2": vRtrLdpAddrFecInLabelStatus2,
       "vRtrLdpAddrFecInLabelIfIndex2": vRtrLdpAddrFecInLabelIfIndex2,
       "vRtrLdpAddrFecInLabel3": vRtrLdpAddrFecInLabel3,
       "vRtrLdpAddrFecInLabelStatus3": vRtrLdpAddrFecInLabelStatus3,
       "vRtrLdpAddrFecInLabelIfIndex3": vRtrLdpAddrFecInLabelIfIndex3,
       "vRtrLdpAddrFecInLabel4": vRtrLdpAddrFecInLabel4,
       "vRtrLdpAddrFecInLabelStatus4": vRtrLdpAddrFecInLabelStatus4,
       "vRtrLdpAddrFecInLabelIfIndex4": vRtrLdpAddrFecInLabelIfIndex4,
       "vRtrLdpAddrFecInLabel5": vRtrLdpAddrFecInLabel5,
       "vRtrLdpAddrFecInLabelStatus5": vRtrLdpAddrFecInLabelStatus5,
       "vRtrLdpAddrFecInLabelIfIndex5": vRtrLdpAddrFecInLabelIfIndex5,
       "vRtrLdpAddrFecOutLabel1": vRtrLdpAddrFecOutLabel1,
       "vRtrLdpAddrFecOutLabelStatus1": vRtrLdpAddrFecOutLabelStatus1,
       "vRtrLdpAddrFecOutLabelIfIndex1": vRtrLdpAddrFecOutLabelIfIndex1,
       "vRtrLdpAddrFecOutLabelNextHop1": vRtrLdpAddrFecOutLabelNextHop1,
       "vRtrLdpAddrFecOutLabel2": vRtrLdpAddrFecOutLabel2,
       "vRtrLdpAddrFecOutLabelStatus2": vRtrLdpAddrFecOutLabelStatus2,
       "vRtrLdpAddrFecOutLabelIfIndex2": vRtrLdpAddrFecOutLabelIfIndex2,
       "vRtrLdpAddrFecOutLabelNextHop2": vRtrLdpAddrFecOutLabelNextHop2,
       "vRtrLdpAddrFecOutLabel3": vRtrLdpAddrFecOutLabel3,
       "vRtrLdpAddrFecOutLabelStatus3": vRtrLdpAddrFecOutLabelStatus3,
       "vRtrLdpAddrFecOutLabelIfIndex3": vRtrLdpAddrFecOutLabelIfIndex3,
       "vRtrLdpAddrFecOutLabelNextHop3": vRtrLdpAddrFecOutLabelNextHop3,
       "vRtrLdpAddrFecOutLabel4": vRtrLdpAddrFecOutLabel4,
       "vRtrLdpAddrFecOutLabelStatus4": vRtrLdpAddrFecOutLabelStatus4,
       "vRtrLdpAddrFecOutLabelIfIndex4": vRtrLdpAddrFecOutLabelIfIndex4,
       "vRtrLdpAddrFecOutLabelNextHop4": vRtrLdpAddrFecOutLabelNextHop4,
       "vRtrLdpAddrFecOutLabel5": vRtrLdpAddrFecOutLabel5,
       "vRtrLdpAddrFecOutLabelStatus5": vRtrLdpAddrFecOutLabelStatus5,
       "vRtrLdpAddrFecOutLabelIfIndex5": vRtrLdpAddrFecOutLabelIfIndex5,
       "vRtrLdpAddrFecOutLabelNextHop5": vRtrLdpAddrFecOutLabelNextHop5,
       "vRtrLdpAddrFecLspId": vRtrLdpAddrFecLspId,
       "vRtrLdpAddrFecMapTable": vRtrLdpAddrFecMapTable,
       "vRtrLdpAddrFecMapEntry": vRtrLdpAddrFecMapEntry,
       "vRtrLdpAddrFecMapFecType": vRtrLdpAddrFecMapFecType,
       "vRtrLdpAddrFecMapIpPrefix": vRtrLdpAddrFecMapIpPrefix,
       "vRtrLdpAddrFecMapIpMask": vRtrLdpAddrFecMapIpMask,
       "vRtrLdpAdjBackoffTable": vRtrLdpAdjBackoffTable,
       "vRtrLdpAdjBackoffEntry": vRtrLdpAdjBackoffEntry,
       "vRtrLdpAdjInitBackoff": vRtrLdpAdjInitBackoff,
       "vRtrLdpAdjMaxBackoff": vRtrLdpAdjMaxBackoff,
       "vRtrLdpAdjCurrentBackoff": vRtrLdpAdjCurrentBackoff,
       "vRtrLdpAdjWaitingTime": vRtrLdpAdjWaitingTime,
       "vRtrLdpAdjBackoffStatus": vRtrLdpAdjBackoffStatus,
       "vRtrLdpPeerParamsTable": vRtrLdpPeerParamsTable,
       "vRtrLdpPeerParamsEntry": vRtrLdpPeerParamsEntry,
       "vRtrLdpPeerRowStatus": vRtrLdpPeerRowStatus,
       "vRtrLdpPeerAuth": vRtrLdpPeerAuth,
       "vRtrLdpPeerAuthKey": vRtrLdpPeerAuthKey,
       "vRtrLdpPeerMinTTLValue": vRtrLdpPeerMinTTLValue,
       "vRtrLdpPeerTTLLogId": vRtrLdpPeerTTLLogId,
       "vRtrLdpPeerAuthKeyChain": vRtrLdpPeerAuthKeyChain,
       "tmnxLdpNotificationObjects": tmnxLdpNotificationObjects,
       "vRtrLdpInstanceNotifyReasonCode": vRtrLdpInstanceNotifyReasonCode,
       "vRtrLdpIfNotifyReasonCode": vRtrLdpIfNotifyReasonCode,
       "vRtrLdpNotifyLocalServiceID": vRtrLdpNotifyLocalServiceID,
       "vRtrLdpNotifyRemoteServiceID": vRtrLdpNotifyRemoteServiceID,
       "vRtrLdpNotifyLocalGroupID": vRtrLdpNotifyLocalGroupID,
       "vRtrLdpNotifyRemoteGroupID": vRtrLdpNotifyRemoteGroupID,
       "vRtrLdpStaticFecTable": vRtrLdpStaticFecTable,
       "vRtrLdpStaticFecEntry": vRtrLdpStaticFecEntry,
       "vRtrLdpStaticFecIpPrefix": vRtrLdpStaticFecIpPrefix,
       "vRtrLdpStaticFecIpMask": vRtrLdpStaticFecIpMask,
       "vRtrLdpStaticFecRowStatus": vRtrLdpStaticFecRowStatus,
       "vRtrLdpStaticFecNextNHIndex": vRtrLdpStaticFecNextNHIndex,
       "vRtrLdpStaticFecIngLabel": vRtrLdpStaticFecIngLabel,
       "vRtrLdpStaticFecNumNH": vRtrLdpStaticFecNumNH,
       "vRtrLdpStaticFecOperIngLabel": vRtrLdpStaticFecOperIngLabel,
       "vRtrLdpStaticFecNHTable": vRtrLdpStaticFecNHTable,
       "vRtrLdpStaticFecNHEntry": vRtrLdpStaticFecNHEntry,
       "vRtrLdpStaticFecNHIndex": vRtrLdpStaticFecNHIndex,
       "vRtrLdpStaticFecNHRowStatus": vRtrLdpStaticFecNHRowStatus,
       "vRtrLdpStaticFecNHType": vRtrLdpStaticFecNHType,
       "vRtrLdpStaticFecNHIpAddr": vRtrLdpStaticFecNHIpAddr,
       "vRtrLdpStaticFecNHEgrLabel": vRtrLdpStaticFecNHEgrLabel,
       "vRtrLdpTargTable": vRtrLdpTargTable,
       "vRtrLdpTargEntry": vRtrLdpTargEntry,
       "vRtrLdpTargImportPolicy1": vRtrLdpTargImportPolicy1,
       "vRtrLdpTargImportPolicy2": vRtrLdpTargImportPolicy2,
       "vRtrLdpTargImportPolicy3": vRtrLdpTargImportPolicy3,
       "vRtrLdpTargImportPolicy4": vRtrLdpTargImportPolicy4,
       "vRtrLdpTargImportPolicy5": vRtrLdpTargImportPolicy5,
       "vRtrLdpTargExportPolicy1": vRtrLdpTargExportPolicy1,
       "vRtrLdpTargExportPolicy2": vRtrLdpTargExportPolicy2,
       "vRtrLdpTargExportPolicy3": vRtrLdpTargExportPolicy3,
       "vRtrLdpTargExportPolicy4": vRtrLdpTargExportPolicy4,
       "vRtrLdpTargExportPolicy5": vRtrLdpTargExportPolicy5,
       "vRtrLdpTargTunnelPreference": vRtrLdpTargTunnelPreference,
       "vRtrLdpIfTunnelingLspTable": vRtrLdpIfTunnelingLspTable,
       "vRtrLdpIfTunnelingLspEntry": vRtrLdpIfTunnelingLspEntry,
       "vRtrLdpIfLspId": vRtrLdpIfLspId,
       "vRtrLdpIfLspRowStatus": vRtrLdpIfLspRowStatus,
       "vRtrLdpCepTdmFecTable": vRtrLdpCepTdmFecTable,
       "vRtrLdpCepTdmFecEntry": vRtrLdpCepTdmFecEntry,
       "vRtrLdpCepTdmLocalPayloadSize": vRtrLdpCepTdmLocalPayloadSize,
       "vRtrLdpCepTdmRemotePayloadSize": vRtrLdpCepTdmRemotePayloadSize,
       "vRtrLdpCepTdmLocalBitrate": vRtrLdpCepTdmLocalBitrate,
       "vRtrLdpCepTdmRemoteBitrate": vRtrLdpCepTdmRemoteBitrate,
       "vRtrLdpCepTdmLocalRtpHeader": vRtrLdpCepTdmLocalRtpHeader,
       "vRtrLdpCepTdmRemoteRtpHeader": vRtrLdpCepTdmRemoteRtpHeader,
       "vRtrLdpCepTdmLocalDiffTimestamp": vRtrLdpCepTdmLocalDiffTimestamp,
       "vRtrLdpCepTdmRemoteDiffTimestamp": vRtrLdpCepTdmRemoteDiffTimestamp,
       "vRtrLdpCepTdmLocalSigPkts": vRtrLdpCepTdmLocalSigPkts,
       "vRtrLdpCepTdmRemoteSigPkts": vRtrLdpCepTdmRemoteSigPkts,
       "vRtrLdpCepTdmLocalCasTrunk": vRtrLdpCepTdmLocalCasTrunk,
       "vRtrLdpCepTdmRemoteCasTrunk": vRtrLdpCepTdmRemoteCasTrunk,
       "vRtrLdpCepTdmLocalTimestampFreq": vRtrLdpCepTdmLocalTimestampFreq,
       "vRtrLdpCepTdmRemoteTimestampFreq": vRtrLdpCepTdmRemoteTimestampFreq,
       "vRtrLdpCepTdmLocalPayloadType": vRtrLdpCepTdmLocalPayloadType,
       "vRtrLdpCepTdmRemotePayloadType": vRtrLdpCepTdmRemotePayloadType,
       "vRtrLdpCepTdmLocalSsrcId": vRtrLdpCepTdmLocalSsrcId,
       "vRtrLdpCepTdmRemoteSsrcId": vRtrLdpCepTdmRemoteSsrcId,
       "vLdpServFec129Table": vLdpServFec129Table,
       "vLdpServFec129Entry": vLdpServFec129Entry,
       "vLdpServFec129AgiTlv": vLdpServFec129AgiTlv,
       "vLdpServFec129SrcAiiTlv": vLdpServFec129SrcAiiTlv,
       "vLdpServFec129TgtAiiTlv": vLdpServFec129TgtAiiTlv,
       "vLdpServFec129ServType": vLdpServFec129ServType,
       "vLdpServFec129ServId": vLdpServFec129ServId,
       "vLdpServFec129VpnId": vLdpServFec129VpnId,
       "vLdpServFec129Flags": vLdpServFec129Flags,
       "vLdpServFec129NumInLabels": vLdpServFec129NumInLabels,
       "vLdpServFec129NumOutLabels": vLdpServFec129NumOutLabels,
       "vLdpServFec129InLabel1": vLdpServFec129InLabel1,
       "vLdpServFec129InLabelStatus1": vLdpServFec129InLabelStatus1,
       "vLdpServFec129OutLabel1": vLdpServFec129OutLabel1,
       "vLdpServFec129OutLabelStatus1": vLdpServFec129OutLabelStatus1,
       "vLdpServFec129SdpId": vLdpServFec129SdpId,
       "vLdpServFec129LocalMTU": vLdpServFec129LocalMTU,
       "vLdpServFec129RemoteMTU": vLdpServFec129RemoteMTU,
       "vLdpServFec129LocalVlanTag": vLdpServFec129LocalVlanTag,
       "vLdpServFec129RemoteVlanTag": vLdpServFec129RemoteVlanTag,
       "vLdpServFec129LocalMaxCellConcat": vLdpServFec129LocalMaxCellConcat,
       "vLdpServFec129RemoteMaxCellConcat": vLdpServFec129RemoteMaxCellConcat,
       "vLdpServFec129InLabelSigStatus1": vLdpServFec129InLabelSigStatus1,
       "vLdpServFec129OutLabelSigStatus1": vLdpServFec129OutLabelSigStatus1,
       "vLdpServFec129MapTable": vLdpServFec129MapTable,
       "vLdpServFec129MapEntry": vLdpServFec129MapEntry,
       "vLdpServFec129MapVcType": vLdpServFec129MapVcType,
       "vLdpServFec129MapAgiTlv": vLdpServFec129MapAgiTlv,
       "vLdpServFec129MapSrcAiiTlv": vLdpServFec129MapSrcAiiTlv,
       "vLdpServFec129MapTgtAiiTlv": vLdpServFec129MapTgtAiiTlv,
       "vLdpCepTdmFec129Table": vLdpCepTdmFec129Table,
       "vLdpCepTdmFec129Entry": vLdpCepTdmFec129Entry,
       "vLdpCepTdmFec129LocalPayloadSize": vLdpCepTdmFec129LocalPayloadSize,
       "vLdpCepTdmFec129RemotePayloadSize": vLdpCepTdmFec129RemotePayloadSize,
       "vLdpCepTdmFec129LocalBitrate": vLdpCepTdmFec129LocalBitrate,
       "vLdpCepTdmFec129RemoteBitrate": vLdpCepTdmFec129RemoteBitrate,
       "vLdpCepTdmFec129LocalRtpHeader": vLdpCepTdmFec129LocalRtpHeader,
       "vLdpCepTdmFec129RemoteRtpHeader": vLdpCepTdmFec129RemoteRtpHeader,
       "vLdpCepTdmFec129LocalDiffTimestamp": vLdpCepTdmFec129LocalDiffTimestamp,
       "vLdpCepTdmFec129RemoteDiffTimestamp": vLdpCepTdmFec129RemoteDiffTimestamp,
       "vLdpCepTdmFec129LocalSigPkts": vLdpCepTdmFec129LocalSigPkts,
       "vLdpCepTdmFec129RemoteSigPkts": vLdpCepTdmFec129RemoteSigPkts,
       "vLdpCepTdmFec129LocalCasTrunk": vLdpCepTdmFec129LocalCasTrunk,
       "vLdpCepTdmFec129RemoteCasTrunk": vLdpCepTdmFec129RemoteCasTrunk,
       "vLdpCepTdmFec129LocalTimestampFreq": vLdpCepTdmFec129LocalTimestampFreq,
       "vLdpCepTdmFec129RemoteTimestampFreq": vLdpCepTdmFec129RemoteTimestampFreq,
       "vLdpCepTdmFec129LocalPayloadType": vLdpCepTdmFec129LocalPayloadType,
       "vLdpCepTdmFec129RemotePayloadType": vLdpCepTdmFec129RemotePayloadType,
       "vLdpCepTdmFec129LocalSsrcId": vLdpCepTdmFec129LocalSsrcId,
       "vLdpCepTdmFec129RemoteSsrcId": vLdpCepTdmFec129RemoteSsrcId,
       "tmnxLdpNotifyPrefix": tmnxLdpNotifyPrefix,
       "tmnxLdpNotifications": tmnxLdpNotifications,
       "vRtrLdpStateChange": vRtrLdpStateChange,
       "vRtrLdpInstanceStateChange": vRtrLdpInstanceStateChange,
       "vRtrLdpIfStateChange": vRtrLdpIfStateChange,
       "vRtrLdpSvcIdMismatch": vRtrLdpSvcIdMismatch,
       "vRtrLdpGroupIdMismatch": vRtrLdpGroupIdMismatch}
)
