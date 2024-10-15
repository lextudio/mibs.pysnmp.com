# SNMP MIB module (Unisphere-Data-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:09 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdMplsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54)
)
usdMplsMIB.setRevisions(
        ("2002-11-04 15:35",
         "2002-04-03 20:44")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdMajorCfgVciRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 65535),
    )



class UsdMajorCfgVpiRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UsdMinorCfgBWRanges(Unsigned32, TextualConvention):
    status = "current"


class UsdMinorCfgHoldingAndSetupPriorityRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class UsdMinorCfgRetryTimesAndNorouteRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class UsdMinorCfgRetryIntervalAndNorouteRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )



class UsdProfileCfgBWRanges(Unsigned32, TextualConvention):
    status = "current"


class UsdProfileCfgHoldingAndSetupPriorityRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class UsdProfileCfgRetryTimesAndNorouteRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class UsdProfileCfgRetryIntervalAndNorouteRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )



# MIB Managed Objects in the order of their OIDs

_UsdMplsObjects_ObjectIdentity = ObjectIdentity
usdMplsObjects = _UsdMplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1)
)
_UsdMplsLsrGlobalConfig_ObjectIdentity = ObjectIdentity
usdMplsLsrGlobalConfig = _UsdMplsLsrGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1)
)
_UsdMplsGroup_ObjectIdentity = ObjectIdentity
usdMplsGroup = _UsdMplsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1)
)


class _UsdMplsGroupMplsEnable_Type(Integer32):
    """Custom type usdMplsGroupMplsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdMplsGroupMplsEnable_Type.__name__ = "Integer32"
_UsdMplsGroupMplsEnable_Object = MibScalar
usdMplsGroupMplsEnable = _UsdMplsGroupMplsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 1),
    _UsdMplsGroupMplsEnable_Type()
)
usdMplsGroupMplsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupMplsEnable.setStatus("current")


class _UsdMplsGroupReopTimer_Type(Integer32):
    """Custom type usdMplsGroupReopTimer based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_UsdMplsGroupReopTimer_Type.__name__ = "Integer32"
_UsdMplsGroupReopTimer_Object = MibScalar
usdMplsGroupReopTimer = _UsdMplsGroupReopTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 2),
    _UsdMplsGroupReopTimer_Type()
)
usdMplsGroupReopTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupReopTimer.setStatus("current")
if mibBuilder.loadTexts:
    usdMplsGroupReopTimer.setUnits("seconds")


class _UsdMplsGroupLabelRangeLow_Type(Integer32):
    """Custom type usdMplsGroupLabelRangeLow based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048576),
    )


_UsdMplsGroupLabelRangeLow_Type.__name__ = "Integer32"
_UsdMplsGroupLabelRangeLow_Object = MibScalar
usdMplsGroupLabelRangeLow = _UsdMplsGroupLabelRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 3),
    _UsdMplsGroupLabelRangeLow_Type()
)
usdMplsGroupLabelRangeLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLabelRangeLow.setStatus("current")


class _UsdMplsGroupLabelRangeHigh_Type(Integer32):
    """Custom type usdMplsGroupLabelRangeHigh based on Integer32"""
    defaultValue = 1048575

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048576),
    )


_UsdMplsGroupLabelRangeHigh_Type.__name__ = "Integer32"
_UsdMplsGroupLabelRangeHigh_Object = MibScalar
usdMplsGroupLabelRangeHigh = _UsdMplsGroupLabelRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 4),
    _UsdMplsGroupLabelRangeHigh_Type()
)
usdMplsGroupLabelRangeHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLabelRangeHigh.setStatus("current")


class _UsdMplsGroupLspRetryTimesNoroute_Type(Integer32):
    """Custom type usdMplsGroupLspRetryTimesNoroute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdMplsGroupLspRetryTimesNoroute_Type.__name__ = "Integer32"
_UsdMplsGroupLspRetryTimesNoroute_Object = MibScalar
usdMplsGroupLspRetryTimesNoroute = _UsdMplsGroupLspRetryTimesNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 5),
    _UsdMplsGroupLspRetryTimesNoroute_Type()
)
usdMplsGroupLspRetryTimesNoroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLspRetryTimesNoroute.setStatus("current")


class _UsdMplsGroupLspRetryIntervalNoroute_Type(Integer32):
    """Custom type usdMplsGroupLspRetryIntervalNoroute based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_UsdMplsGroupLspRetryIntervalNoroute_Type.__name__ = "Integer32"
_UsdMplsGroupLspRetryIntervalNoroute_Object = MibScalar
usdMplsGroupLspRetryIntervalNoroute = _UsdMplsGroupLspRetryIntervalNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 6),
    _UsdMplsGroupLspRetryIntervalNoroute_Type()
)
usdMplsGroupLspRetryIntervalNoroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLspRetryIntervalNoroute.setStatus("current")
if mibBuilder.loadTexts:
    usdMplsGroupLspRetryIntervalNoroute.setUnits("seconds")


class _UsdMplsGroupLspRetryTimes_Type(Integer32):
    """Custom type usdMplsGroupLspRetryTimes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdMplsGroupLspRetryTimes_Type.__name__ = "Integer32"
_UsdMplsGroupLspRetryTimes_Object = MibScalar
usdMplsGroupLspRetryTimes = _UsdMplsGroupLspRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 7),
    _UsdMplsGroupLspRetryTimes_Type()
)
usdMplsGroupLspRetryTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLspRetryTimes.setStatus("current")


class _UsdMplsGroupLspRetryInterval_Type(Integer32):
    """Custom type usdMplsGroupLspRetryInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_UsdMplsGroupLspRetryInterval_Type.__name__ = "Integer32"
_UsdMplsGroupLspRetryInterval_Object = MibScalar
usdMplsGroupLspRetryInterval = _UsdMplsGroupLspRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 8),
    _UsdMplsGroupLspRetryInterval_Type()
)
usdMplsGroupLspRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLspRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdMplsGroupLspRetryInterval.setUnits("seconds")


class _UsdMplsGroupLdpRetryTimesNoroute_Type(Integer32):
    """Custom type usdMplsGroupLdpRetryTimesNoroute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdMplsGroupLdpRetryTimesNoroute_Type.__name__ = "Integer32"
_UsdMplsGroupLdpRetryTimesNoroute_Object = MibScalar
usdMplsGroupLdpRetryTimesNoroute = _UsdMplsGroupLdpRetryTimesNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 9),
    _UsdMplsGroupLdpRetryTimesNoroute_Type()
)
usdMplsGroupLdpRetryTimesNoroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLdpRetryTimesNoroute.setStatus("current")


class _UsdMplsGroupLdpRetryIntervalNoroute_Type(Integer32):
    """Custom type usdMplsGroupLdpRetryIntervalNoroute based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_UsdMplsGroupLdpRetryIntervalNoroute_Type.__name__ = "Integer32"
_UsdMplsGroupLdpRetryIntervalNoroute_Object = MibScalar
usdMplsGroupLdpRetryIntervalNoroute = _UsdMplsGroupLdpRetryIntervalNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 10),
    _UsdMplsGroupLdpRetryIntervalNoroute_Type()
)
usdMplsGroupLdpRetryIntervalNoroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLdpRetryIntervalNoroute.setStatus("current")
if mibBuilder.loadTexts:
    usdMplsGroupLdpRetryIntervalNoroute.setUnits("seconds")


class _UsdMplsGroupLdpRetryTimes_Type(Integer32):
    """Custom type usdMplsGroupLdpRetryTimes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdMplsGroupLdpRetryTimes_Type.__name__ = "Integer32"
_UsdMplsGroupLdpRetryTimes_Object = MibScalar
usdMplsGroupLdpRetryTimes = _UsdMplsGroupLdpRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 11),
    _UsdMplsGroupLdpRetryTimes_Type()
)
usdMplsGroupLdpRetryTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLdpRetryTimes.setStatus("current")


class _UsdMplsGroupLdpRetryInterval_Type(Integer32):
    """Custom type usdMplsGroupLdpRetryInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_UsdMplsGroupLdpRetryInterval_Type.__name__ = "Integer32"
_UsdMplsGroupLdpRetryInterval_Object = MibScalar
usdMplsGroupLdpRetryInterval = _UsdMplsGroupLdpRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 12),
    _UsdMplsGroupLdpRetryInterval_Type()
)
usdMplsGroupLdpRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLdpRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdMplsGroupLdpRetryInterval.setUnits("seconds")


class _UsdMplsGroupLdpSessionRetries_Type(Integer32):
    """Custom type usdMplsGroupLdpSessionRetries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_UsdMplsGroupLdpSessionRetries_Type.__name__ = "Integer32"
_UsdMplsGroupLdpSessionRetries_Object = MibScalar
usdMplsGroupLdpSessionRetries = _UsdMplsGroupLdpSessionRetries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 13),
    _UsdMplsGroupLdpSessionRetries_Type()
)
usdMplsGroupLdpSessionRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLdpSessionRetries.setStatus("current")


class _UsdMplsGroupLdpSessionRetryTimer_Type(Integer32):
    """Custom type usdMplsGroupLdpSessionRetryTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_UsdMplsGroupLdpSessionRetryTimer_Type.__name__ = "Integer32"
_UsdMplsGroupLdpSessionRetryTimer_Object = MibScalar
usdMplsGroupLdpSessionRetryTimer = _UsdMplsGroupLdpSessionRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 14),
    _UsdMplsGroupLdpSessionRetryTimer_Type()
)
usdMplsGroupLdpSessionRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLdpSessionRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    usdMplsGroupLdpSessionRetryTimer.setUnits("seconds")
_UsdMplsGroupTopologyDrivenIpProfileName_Type = DisplayString
_UsdMplsGroupTopologyDrivenIpProfileName_Object = MibScalar
usdMplsGroupTopologyDrivenIpProfileName = _UsdMplsGroupTopologyDrivenIpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 15),
    _UsdMplsGroupTopologyDrivenIpProfileName_Type()
)
usdMplsGroupTopologyDrivenIpProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupTopologyDrivenIpProfileName.setStatus("current")


class _UsdMplsGroupTopologyDrivenLdpEgressIpIntf_Type(TruthValue):
    """Custom type usdMplsGroupTopologyDrivenLdpEgressIpIntf based on TruthValue"""


_UsdMplsGroupTopologyDrivenLdpEgressIpIntf_Object = MibScalar
usdMplsGroupTopologyDrivenLdpEgressIpIntf = _UsdMplsGroupTopologyDrivenLdpEgressIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 16),
    _UsdMplsGroupTopologyDrivenLdpEgressIpIntf_Type()
)
usdMplsGroupTopologyDrivenLdpEgressIpIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupTopologyDrivenLdpEgressIpIntf.setStatus("current")


class _UsdMplsGroupTopologyDrivenLdpIngressIpIntf_Type(TruthValue):
    """Custom type usdMplsGroupTopologyDrivenLdpIngressIpIntf based on TruthValue"""


_UsdMplsGroupTopologyDrivenLdpIngressIpIntf_Object = MibScalar
usdMplsGroupTopologyDrivenLdpIngressIpIntf = _UsdMplsGroupTopologyDrivenLdpIngressIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 17),
    _UsdMplsGroupTopologyDrivenLdpIngressIpIntf_Type()
)
usdMplsGroupTopologyDrivenLdpIngressIpIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupTopologyDrivenLdpIngressIpIntf.setStatus("current")


class _UsdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly_Type(TruthValue):
    """Custom type usdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly based on TruthValue"""


_UsdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly_Object = MibScalar
usdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly = _UsdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 18),
    _UsdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly_Type()
)
usdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly.setStatus("current")


class _UsdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly_Type(TruthValue):
    """Custom type usdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly based on TruthValue"""


_UsdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly_Object = MibScalar
usdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly = _UsdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 19),
    _UsdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly_Type()
)
usdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly.setStatus("current")


class _UsdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType_Type(Integer32):
    """Custom type usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType based on Integer32"""
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
        *(("accessList", 1),
          ("noPolicyList", 3),
          ("prefixList", 2))
    )


_UsdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType_Type.__name__ = "Integer32"
_UsdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType_Object = MibScalar
usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType = _UsdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 20),
    _UsdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType_Type()
)
usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType.setStatus("current")


class _UsdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType_Type(Integer32):
    """Custom type usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType based on Integer32"""
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
        *(("accessList", 1),
          ("noPolicyList", 3),
          ("prefixList", 2))
    )


_UsdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType_Type.__name__ = "Integer32"
_UsdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType_Object = MibScalar
usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType = _UsdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 21),
    _UsdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType_Type()
)
usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType.setStatus("current")
_UsdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList_Type = DisplayString
_UsdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList_Object = MibScalar
usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList = _UsdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 22),
    _UsdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList_Type()
)
usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList.setStatus("current")
_UsdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList_Type = DisplayString
_UsdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList_Object = MibScalar
usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList = _UsdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 23),
    _UsdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList_Type()
)
usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList.setStatus("current")


class _UsdMplsGroupTopologyDrivenLdp_Type(Integer32):
    """Custom type usdMplsGroupTopologyDrivenLdp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdMplsGroupTopologyDrivenLdp_Type.__name__ = "Integer32"
_UsdMplsGroupTopologyDrivenLdp_Object = MibScalar
usdMplsGroupTopologyDrivenLdp = _UsdMplsGroupTopologyDrivenLdp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 24),
    _UsdMplsGroupTopologyDrivenLdp_Type()
)
usdMplsGroupTopologyDrivenLdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupTopologyDrivenLdp.setStatus("current")


class _UsdMplsGroupLspLabelDistCtrlMode_Type(Integer32):
    """Custom type usdMplsGroupLspLabelDistCtrlMode based on Integer32"""
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
        *(("independent", 1),
          ("ordered", 0),
          ("undefined", 2))
    )


_UsdMplsGroupLspLabelDistCtrlMode_Type.__name__ = "Integer32"
_UsdMplsGroupLspLabelDistCtrlMode_Object = MibScalar
usdMplsGroupLspLabelDistCtrlMode = _UsdMplsGroupLspLabelDistCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 25),
    _UsdMplsGroupLspLabelDistCtrlMode_Type()
)
usdMplsGroupLspLabelDistCtrlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdMplsGroupLspLabelDistCtrlMode.setStatus("current")


class _UsdMplsGroupLdpAdvHostOnly_Type(TruthValue):
    """Custom type usdMplsGroupLdpAdvHostOnly based on TruthValue"""


_UsdMplsGroupLdpAdvHostOnly_Object = MibScalar
usdMplsGroupLdpAdvHostOnly = _UsdMplsGroupLdpAdvHostOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 26),
    _UsdMplsGroupLdpAdvHostOnly_Type()
)
usdMplsGroupLdpAdvHostOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupLdpAdvHostOnly.setStatus("current")
_UsdMplsGroupLsrState_Type = DisplayString
_UsdMplsGroupLsrState_Object = MibScalar
usdMplsGroupLsrState = _UsdMplsGroupLsrState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 27),
    _UsdMplsGroupLsrState_Type()
)
usdMplsGroupLsrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdMplsGroupLsrState.setStatus("current")


class _UsdMplsGroupReopNow_Type(TruthValue):
    """Custom type usdMplsGroupReopNow based on TruthValue"""


_UsdMplsGroupReopNow_Object = MibScalar
usdMplsGroupReopNow = _UsdMplsGroupReopNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 28),
    _UsdMplsGroupReopNow_Type()
)
usdMplsGroupReopNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdMplsGroupReopNow.setStatus("current")
_UsdMplsGroupList_ObjectIdentity = ObjectIdentity
usdMplsGroupList = _UsdMplsGroupList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2)
)
_UsdMplsGroupTargetedHelloSendTable_Object = MibTable
usdMplsGroupTargetedHelloSendTable = _UsdMplsGroupTargetedHelloSendTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdMplsGroupTargetedHelloSendTable.setStatus("current")
_UsdMplsGroupTargetedHelloSendEntry_Object = MibTableRow
usdMplsGroupTargetedHelloSendEntry = _UsdMplsGroupTargetedHelloSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 1, 1)
)
usdMplsGroupTargetedHelloSendEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsGroupTargetedHelloSendAddress"),
)
if mibBuilder.loadTexts:
    usdMplsGroupTargetedHelloSendEntry.setStatus("current")
_UsdMplsGroupTargetedHelloSendAddress_Type = IpAddress
_UsdMplsGroupTargetedHelloSendAddress_Object = MibTableColumn
usdMplsGroupTargetedHelloSendAddress = _UsdMplsGroupTargetedHelloSendAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 1, 1, 1),
    _UsdMplsGroupTargetedHelloSendAddress_Type()
)
usdMplsGroupTargetedHelloSendAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsGroupTargetedHelloSendAddress.setStatus("current")


class _UsdMplsGroupLdpTargetedHelloSendMode_Type(Integer32):
    """Custom type usdMplsGroupLdpTargetedHelloSendMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("delete", 1),
          ("none", 2))
    )


_UsdMplsGroupLdpTargetedHelloSendMode_Type.__name__ = "Integer32"
_UsdMplsGroupLdpTargetedHelloSendMode_Object = MibTableColumn
usdMplsGroupLdpTargetedHelloSendMode = _UsdMplsGroupLdpTargetedHelloSendMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 1, 1, 2),
    _UsdMplsGroupLdpTargetedHelloSendMode_Type()
)
usdMplsGroupLdpTargetedHelloSendMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsGroupLdpTargetedHelloSendMode.setStatus("current")
_UsdMplsGroupTargetedHelloReceiveTable_Object = MibTable
usdMplsGroupTargetedHelloReceiveTable = _UsdMplsGroupTargetedHelloReceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdMplsGroupTargetedHelloReceiveTable.setStatus("current")
_UsdMplsGroupTargetedHelloReceiveEntry_Object = MibTableRow
usdMplsGroupTargetedHelloReceiveEntry = _UsdMplsGroupTargetedHelloReceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 2, 1)
)
usdMplsGroupTargetedHelloReceiveEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsGroupTargetedHelloReceiveAddress"),
)
if mibBuilder.loadTexts:
    usdMplsGroupTargetedHelloReceiveEntry.setStatus("current")
_UsdMplsGroupTargetedHelloReceiveAddress_Type = IpAddress
_UsdMplsGroupTargetedHelloReceiveAddress_Object = MibTableColumn
usdMplsGroupTargetedHelloReceiveAddress = _UsdMplsGroupTargetedHelloReceiveAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 2, 1, 1),
    _UsdMplsGroupTargetedHelloReceiveAddress_Type()
)
usdMplsGroupTargetedHelloReceiveAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsGroupTargetedHelloReceiveAddress.setStatus("current")


class _UsdMplsGroupLdpTargetedHelloReceiveMode_Type(Integer32):
    """Custom type usdMplsGroupLdpTargetedHelloReceiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("delete", 1),
          ("none", 2))
    )


_UsdMplsGroupLdpTargetedHelloReceiveMode_Type.__name__ = "Integer32"
_UsdMplsGroupLdpTargetedHelloReceiveMode_Object = MibTableColumn
usdMplsGroupLdpTargetedHelloReceiveMode = _UsdMplsGroupLdpTargetedHelloReceiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 2, 1, 2),
    _UsdMplsGroupLdpTargetedHelloReceiveMode_Type()
)
usdMplsGroupLdpTargetedHelloReceiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsGroupLdpTargetedHelloReceiveMode.setStatus("current")
_UsdMplsGroupLdpLabelAdverRouteListTable_Object = MibTable
usdMplsGroupLdpLabelAdverRouteListTable = _UsdMplsGroupLdpLabelAdverRouteListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    usdMplsGroupLdpLabelAdverRouteListTable.setStatus("current")
_UsdMplsGroupLdpLabelAdverRouteListEntry_Object = MibTableRow
usdMplsGroupLdpLabelAdverRouteListEntry = _UsdMplsGroupLdpLabelAdverRouteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 3, 1)
)
usdMplsGroupLdpLabelAdverRouteListEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpLabelAdverRouteListName"),
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpLabelAdverNbrListName"),
)
if mibBuilder.loadTexts:
    usdMplsGroupLdpLabelAdverRouteListEntry.setStatus("current")


class _UsdMplsGroupLdpLabelAdverRouteListName_Type(DisplayString):
    """Custom type usdMplsGroupLdpLabelAdverRouteListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdMplsGroupLdpLabelAdverRouteListName_Type.__name__ = "DisplayString"
_UsdMplsGroupLdpLabelAdverRouteListName_Object = MibTableColumn
usdMplsGroupLdpLabelAdverRouteListName = _UsdMplsGroupLdpLabelAdverRouteListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 3, 1, 1),
    _UsdMplsGroupLdpLabelAdverRouteListName_Type()
)
usdMplsGroupLdpLabelAdverRouteListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsGroupLdpLabelAdverRouteListName.setStatus("current")


class _UsdMplsGroupLdpLabelAdverNbrListName_Type(DisplayString):
    """Custom type usdMplsGroupLdpLabelAdverNbrListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdMplsGroupLdpLabelAdverNbrListName_Type.__name__ = "DisplayString"
_UsdMplsGroupLdpLabelAdverNbrListName_Object = MibTableColumn
usdMplsGroupLdpLabelAdverNbrListName = _UsdMplsGroupLdpLabelAdverNbrListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 3, 1, 2),
    _UsdMplsGroupLdpLabelAdverNbrListName_Type()
)
usdMplsGroupLdpLabelAdverNbrListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsGroupLdpLabelAdverNbrListName.setStatus("current")


class _UsdMplsGroupLabelAdverListMode_Type(Integer32):
    """Custom type usdMplsGroupLabelAdverListMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("delete", 1),
          ("none", 2))
    )


_UsdMplsGroupLabelAdverListMode_Type.__name__ = "Integer32"
_UsdMplsGroupLabelAdverListMode_Object = MibTableColumn
usdMplsGroupLabelAdverListMode = _UsdMplsGroupLabelAdverListMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 3, 1, 3),
    _UsdMplsGroupLabelAdverListMode_Type()
)
usdMplsGroupLabelAdverListMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsGroupLabelAdverListMode.setStatus("current")
_UsdMplsGroupLdpProfileTable_Object = MibTable
usdMplsGroupLdpProfileTable = _UsdMplsGroupLdpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    usdMplsGroupLdpProfileTable.setStatus("current")
_UsdMplsGroupLdpProfileEntry_Object = MibTableRow
usdMplsGroupLdpProfileEntry = _UsdMplsGroupLdpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4, 1)
)
usdMplsGroupLdpProfileEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpProfileName"),
)
if mibBuilder.loadTexts:
    usdMplsGroupLdpProfileEntry.setStatus("current")


class _UsdMplsGroupLdpProfileName_Type(DisplayString):
    """Custom type usdMplsGroupLdpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsGroupLdpProfileName_Type.__name__ = "DisplayString"
_UsdMplsGroupLdpProfileName_Object = MibTableColumn
usdMplsGroupLdpProfileName = _UsdMplsGroupLdpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4, 1, 1),
    _UsdMplsGroupLdpProfileName_Type()
)
usdMplsGroupLdpProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsGroupLdpProfileName.setStatus("current")


class _UsdMplsGroupLdpProfileHelloHoldTime_Type(Integer32):
    """Custom type usdMplsGroupLdpProfileHelloHoldTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_UsdMplsGroupLdpProfileHelloHoldTime_Type.__name__ = "Integer32"
_UsdMplsGroupLdpProfileHelloHoldTime_Object = MibTableColumn
usdMplsGroupLdpProfileHelloHoldTime = _UsdMplsGroupLdpProfileHelloHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4, 1, 2),
    _UsdMplsGroupLdpProfileHelloHoldTime_Type()
)
usdMplsGroupLdpProfileHelloHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsGroupLdpProfileHelloHoldTime.setStatus("current")


class _UsdMplsGroupLdpProfileCrLdpAdminState_Type(Integer32):
    """Custom type usdMplsGroupLdpProfileCrLdpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdMplsGroupLdpProfileCrLdpAdminState_Type.__name__ = "Integer32"
_UsdMplsGroupLdpProfileCrLdpAdminState_Object = MibTableColumn
usdMplsGroupLdpProfileCrLdpAdminState = _UsdMplsGroupLdpProfileCrLdpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4, 1, 3),
    _UsdMplsGroupLdpProfileCrLdpAdminState_Type()
)
usdMplsGroupLdpProfileCrLdpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsGroupLdpProfileCrLdpAdminState.setStatus("current")
_UsdMplsGroupLdpProfileRowStatus_Type = RowStatus
_UsdMplsGroupLdpProfileRowStatus_Object = MibTableColumn
usdMplsGroupLdpProfileRowStatus = _UsdMplsGroupLdpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4, 1, 4),
    _UsdMplsGroupLdpProfileRowStatus_Type()
)
usdMplsGroupLdpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsGroupLdpProfileRowStatus.setStatus("current")
_UsdMplsGroupRsvpProfileTable_Object = MibTable
usdMplsGroupRsvpProfileTable = _UsdMplsGroupRsvpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    usdMplsGroupRsvpProfileTable.setStatus("current")
_UsdMplsGroupRsvpProfileEntry_Object = MibTableRow
usdMplsGroupRsvpProfileEntry = _UsdMplsGroupRsvpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5, 1)
)
usdMplsGroupRsvpProfileEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsGroupRsvpProfileName"),
)
if mibBuilder.loadTexts:
    usdMplsGroupRsvpProfileEntry.setStatus("current")


class _UsdMplsGroupRsvpProfileName_Type(DisplayString):
    """Custom type usdMplsGroupRsvpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsGroupRsvpProfileName_Type.__name__ = "DisplayString"
_UsdMplsGroupRsvpProfileName_Object = MibTableColumn
usdMplsGroupRsvpProfileName = _UsdMplsGroupRsvpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5, 1, 1),
    _UsdMplsGroupRsvpProfileName_Type()
)
usdMplsGroupRsvpProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsGroupRsvpProfileName.setStatus("current")


class _UsdMplsGroupRsvpProfileRefreshPeriod_Type(Unsigned32):
    """Custom type usdMplsGroupRsvpProfileRefreshPeriod based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_UsdMplsGroupRsvpProfileRefreshPeriod_Type.__name__ = "Unsigned32"
_UsdMplsGroupRsvpProfileRefreshPeriod_Object = MibTableColumn
usdMplsGroupRsvpProfileRefreshPeriod = _UsdMplsGroupRsvpProfileRefreshPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5, 1, 2),
    _UsdMplsGroupRsvpProfileRefreshPeriod_Type()
)
usdMplsGroupRsvpProfileRefreshPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsGroupRsvpProfileRefreshPeriod.setStatus("current")


class _UsdMplsGroupRsvpProfileCleanupTimeoutFactor_Type(Integer32):
    """Custom type usdMplsGroupRsvpProfileCleanupTimeoutFactor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_UsdMplsGroupRsvpProfileCleanupTimeoutFactor_Type.__name__ = "Integer32"
_UsdMplsGroupRsvpProfileCleanupTimeoutFactor_Object = MibTableColumn
usdMplsGroupRsvpProfileCleanupTimeoutFactor = _UsdMplsGroupRsvpProfileCleanupTimeoutFactor_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5, 1, 3),
    _UsdMplsGroupRsvpProfileCleanupTimeoutFactor_Type()
)
usdMplsGroupRsvpProfileCleanupTimeoutFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsGroupRsvpProfileCleanupTimeoutFactor.setStatus("current")
_UsdMplsGroupRsvpProfileRowStatus_Type = RowStatus
_UsdMplsGroupRsvpProfileRowStatus_Object = MibTableColumn
usdMplsGroupRsvpProfileRowStatus = _UsdMplsGroupRsvpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5, 1, 4),
    _UsdMplsGroupRsvpProfileRowStatus_Type()
)
usdMplsGroupRsvpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsGroupRsvpProfileRowStatus.setStatus("current")
_UsdMplsMajorLayer_ObjectIdentity = ObjectIdentity
usdMplsMajorLayer = _UsdMplsMajorLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2)
)
_UsdMplsIfMajorLayer_ObjectIdentity = ObjectIdentity
usdMplsIfMajorLayer = _UsdMplsIfMajorLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1)
)
_UsdMplsIfMajorNextIfIndex_Type = UsdNextIfIndex
_UsdMplsIfMajorNextIfIndex_Object = MibScalar
usdMplsIfMajorNextIfIndex = _UsdMplsIfMajorNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 1),
    _UsdMplsIfMajorNextIfIndex_Type()
)
usdMplsIfMajorNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdMplsIfMajorNextIfIndex.setStatus("current")
_UsdMplsIfMajorTable_Object = MibTable
usdMplsIfMajorTable = _UsdMplsIfMajorTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdMplsIfMajorTable.setStatus("current")
_UsdMplsIfMajorEntry_Object = MibTableRow
usdMplsIfMajorEntry = _UsdMplsIfMajorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1)
)
usdMplsIfMajorEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsIfMajorIndex"),
)
if mibBuilder.loadTexts:
    usdMplsIfMajorEntry.setStatus("current")
_UsdMplsIfMajorIndex_Type = InterfaceIndex
_UsdMplsIfMajorIndex_Object = MibTableColumn
usdMplsIfMajorIndex = _UsdMplsIfMajorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 1),
    _UsdMplsIfMajorIndex_Type()
)
usdMplsIfMajorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsIfMajorIndex.setStatus("current")
_UsdMplsIfMajorRowStatus_Type = RowStatus
_UsdMplsIfMajorRowStatus_Object = MibTableColumn
usdMplsIfMajorRowStatus = _UsdMplsIfMajorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 2),
    _UsdMplsIfMajorRowStatus_Type()
)
usdMplsIfMajorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorRowStatus.setStatus("current")
_UsdMplsIfMajorLowerIfIndex_Type = InterfaceIndexOrZero
_UsdMplsIfMajorLowerIfIndex_Object = MibTableColumn
usdMplsIfMajorLowerIfIndex = _UsdMplsIfMajorLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 3),
    _UsdMplsIfMajorLowerIfIndex_Type()
)
usdMplsIfMajorLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorLowerIfIndex.setStatus("current")


class _UsdMplsIfMajorAdminStatus_Type(Integer32):
    """Custom type usdMplsIfMajorAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdMplsIfMajorAdminStatus_Type.__name__ = "Integer32"
_UsdMplsIfMajorAdminStatus_Object = MibTableColumn
usdMplsIfMajorAdminStatus = _UsdMplsIfMajorAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 4),
    _UsdMplsIfMajorAdminStatus_Type()
)
usdMplsIfMajorAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorAdminStatus.setStatus("current")


class _UsdMplsIfMajorLdpAdminStatus_Type(Integer32):
    """Custom type usdMplsIfMajorLdpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdMplsIfMajorLdpAdminStatus_Type.__name__ = "Integer32"
_UsdMplsIfMajorLdpAdminStatus_Object = MibTableColumn
usdMplsIfMajorLdpAdminStatus = _UsdMplsIfMajorLdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 5),
    _UsdMplsIfMajorLdpAdminStatus_Type()
)
usdMplsIfMajorLdpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorLdpAdminStatus.setStatus("current")


class _UsdMplsIfMajorLdpProfileName_Type(DisplayString):
    """Custom type usdMplsIfMajorLdpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsIfMajorLdpProfileName_Type.__name__ = "DisplayString"
_UsdMplsIfMajorLdpProfileName_Object = MibTableColumn
usdMplsIfMajorLdpProfileName = _UsdMplsIfMajorLdpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 6),
    _UsdMplsIfMajorLdpProfileName_Type()
)
usdMplsIfMajorLdpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorLdpProfileName.setStatus("current")


class _UsdMplsIfMajorLdpVpiStart_Type(UsdMajorCfgVpiRanges):
    """Custom type usdMplsIfMajorLdpVpiStart based on UsdMajorCfgVpiRanges"""
    defaultValue = 0


_UsdMplsIfMajorLdpVpiStart_Object = MibTableColumn
usdMplsIfMajorLdpVpiStart = _UsdMplsIfMajorLdpVpiStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 7),
    _UsdMplsIfMajorLdpVpiStart_Type()
)
usdMplsIfMajorLdpVpiStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorLdpVpiStart.setStatus("current")


class _UsdMplsIfMajorLdpVpiStop_Type(UsdMajorCfgVpiRanges):
    """Custom type usdMplsIfMajorLdpVpiStop based on UsdMajorCfgVpiRanges"""
    defaultValue = 0


_UsdMplsIfMajorLdpVpiStop_Object = MibTableColumn
usdMplsIfMajorLdpVpiStop = _UsdMplsIfMajorLdpVpiStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 8),
    _UsdMplsIfMajorLdpVpiStop_Type()
)
usdMplsIfMajorLdpVpiStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorLdpVpiStop.setStatus("current")
_UsdMplsIfMajorLdpVciStart_Type = UsdMajorCfgVciRanges
_UsdMplsIfMajorLdpVciStart_Object = MibTableColumn
usdMplsIfMajorLdpVciStart = _UsdMplsIfMajorLdpVciStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 9),
    _UsdMplsIfMajorLdpVciStart_Type()
)
usdMplsIfMajorLdpVciStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorLdpVciStart.setStatus("current")
_UsdMplsIfMajorLdpVciStop_Type = UsdMajorCfgVciRanges
_UsdMplsIfMajorLdpVciStop_Object = MibTableColumn
usdMplsIfMajorLdpVciStop = _UsdMplsIfMajorLdpVciStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 10),
    _UsdMplsIfMajorLdpVciStop_Type()
)
usdMplsIfMajorLdpVciStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorLdpVciStop.setStatus("current")


class _UsdMplsIfMajorRsvpAdminStatus_Type(Integer32):
    """Custom type usdMplsIfMajorRsvpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdMplsIfMajorRsvpAdminStatus_Type.__name__ = "Integer32"
_UsdMplsIfMajorRsvpAdminStatus_Object = MibTableColumn
usdMplsIfMajorRsvpAdminStatus = _UsdMplsIfMajorRsvpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 11),
    _UsdMplsIfMajorRsvpAdminStatus_Type()
)
usdMplsIfMajorRsvpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorRsvpAdminStatus.setStatus("current")


class _UsdMplsIfMajorRsvpProfileName_Type(DisplayString):
    """Custom type usdMplsIfMajorRsvpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsIfMajorRsvpProfileName_Type.__name__ = "DisplayString"
_UsdMplsIfMajorRsvpProfileName_Object = MibTableColumn
usdMplsIfMajorRsvpProfileName = _UsdMplsIfMajorRsvpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 12),
    _UsdMplsIfMajorRsvpProfileName_Type()
)
usdMplsIfMajorRsvpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorRsvpProfileName.setStatus("current")


class _UsdMplsIfMajorRsvpVpiStart_Type(UsdMajorCfgVpiRanges):
    """Custom type usdMplsIfMajorRsvpVpiStart based on UsdMajorCfgVpiRanges"""
    defaultValue = 0


_UsdMplsIfMajorRsvpVpiStart_Object = MibTableColumn
usdMplsIfMajorRsvpVpiStart = _UsdMplsIfMajorRsvpVpiStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 13),
    _UsdMplsIfMajorRsvpVpiStart_Type()
)
usdMplsIfMajorRsvpVpiStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorRsvpVpiStart.setStatus("current")


class _UsdMplsIfMajorRsvpVpiStop_Type(UsdMajorCfgVpiRanges):
    """Custom type usdMplsIfMajorRsvpVpiStop based on UsdMajorCfgVpiRanges"""
    defaultValue = 0


_UsdMplsIfMajorRsvpVpiStop_Object = MibTableColumn
usdMplsIfMajorRsvpVpiStop = _UsdMplsIfMajorRsvpVpiStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 14),
    _UsdMplsIfMajorRsvpVpiStop_Type()
)
usdMplsIfMajorRsvpVpiStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorRsvpVpiStop.setStatus("current")
_UsdMplsIfMajorRsvpVciStart_Type = UsdMajorCfgVciRanges
_UsdMplsIfMajorRsvpVciStart_Object = MibTableColumn
usdMplsIfMajorRsvpVciStart = _UsdMplsIfMajorRsvpVciStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 15),
    _UsdMplsIfMajorRsvpVciStart_Type()
)
usdMplsIfMajorRsvpVciStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorRsvpVciStart.setStatus("current")
_UsdMplsIfMajorRsvpVciStop_Type = UsdMajorCfgVciRanges
_UsdMplsIfMajorRsvpVciStop_Object = MibTableColumn
usdMplsIfMajorRsvpVciStop = _UsdMplsIfMajorRsvpVciStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 16),
    _UsdMplsIfMajorRsvpVciStop_Type()
)
usdMplsIfMajorRsvpVciStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMajorRsvpVciStop.setStatus("current")


class _UsdMplsIfMajorLabelSpaceType_Type(Integer32):
    """Custom type usdMplsIfMajorLabelSpaceType based on Integer32"""
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
        *(("ldpVci", 6),
          ("ldpVpi", 5),
          ("ldpVpiVci", 4),
          ("none", 0),
          ("rsvpVci", 3),
          ("rsvpVpi", 2),
          ("rsvpVpiVci", 1))
    )


_UsdMplsIfMajorLabelSpaceType_Type.__name__ = "Integer32"
_UsdMplsIfMajorLabelSpaceType_Object = MibTableColumn
usdMplsIfMajorLabelSpaceType = _UsdMplsIfMajorLabelSpaceType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 17),
    _UsdMplsIfMajorLabelSpaceType_Type()
)
usdMplsIfMajorLabelSpaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdMplsIfMajorLabelSpaceType.setStatus("current")


class _UsdMplsIfMajorOpState_Type(Integer32):
    """Custom type usdMplsIfMajorOpState based on Integer32"""
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
        *(("configIncompleteInterfaceDisabled", 4),
          ("configIncompleteInterfaceEnabled", 3),
          ("interfaceDisabled", 5),
          ("lowerLayerDown", 1),
          ("lowerLayerNotAvailable", 0),
          ("up", 2))
    )


_UsdMplsIfMajorOpState_Type.__name__ = "Integer32"
_UsdMplsIfMajorOpState_Object = MibTableColumn
usdMplsIfMajorOpState = _UsdMplsIfMajorOpState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 18),
    _UsdMplsIfMajorOpState_Type()
)
usdMplsIfMajorOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdMplsIfMajorOpState.setStatus("current")


class _UsdMplsIfMajorCrLdpAdminState_Type(Integer32):
    """Custom type usdMplsIfMajorCrLdpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdMplsIfMajorCrLdpAdminState_Type.__name__ = "Integer32"
_UsdMplsIfMajorCrLdpAdminState_Object = MibTableColumn
usdMplsIfMajorCrLdpAdminState = _UsdMplsIfMajorCrLdpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 19),
    _UsdMplsIfMajorCrLdpAdminState_Type()
)
usdMplsIfMajorCrLdpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdMplsIfMajorCrLdpAdminState.setStatus("current")
_UsdMplsMinorLayer_ObjectIdentity = ObjectIdentity
usdMplsMinorLayer = _UsdMplsMinorLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3)
)
_UsdMplsIfMinorLayer_ObjectIdentity = ObjectIdentity
usdMplsIfMinorLayer = _UsdMplsIfMinorLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1)
)
_UsdMplsIfMinorNextIfIndex_Type = UsdNextIfIndex
_UsdMplsIfMinorNextIfIndex_Object = MibScalar
usdMplsIfMinorNextIfIndex = _UsdMplsIfMinorNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 1),
    _UsdMplsIfMinorNextIfIndex_Type()
)
usdMplsIfMinorNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdMplsIfMinorNextIfIndex.setStatus("current")
_UsdMplsIfMinorTable_Object = MibTable
usdMplsIfMinorTable = _UsdMplsIfMinorTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    usdMplsIfMinorTable.setStatus("current")
_UsdMplsIfMinorEntry_Object = MibTableRow
usdMplsIfMinorEntry = _UsdMplsIfMinorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1)
)
usdMplsIfMinorEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsIfMinorIndex"),
)
if mibBuilder.loadTexts:
    usdMplsIfMinorEntry.setStatus("current")
_UsdMplsIfMinorIndex_Type = InterfaceIndex
_UsdMplsIfMinorIndex_Object = MibTableColumn
usdMplsIfMinorIndex = _UsdMplsIfMinorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 1),
    _UsdMplsIfMinorIndex_Type()
)
usdMplsIfMinorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsIfMinorIndex.setStatus("current")
_UsdMplsIfMinorRowStatus_Type = RowStatus
_UsdMplsIfMinorRowStatus_Object = MibTableColumn
usdMplsIfMinorRowStatus = _UsdMplsIfMinorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 2),
    _UsdMplsIfMinorRowStatus_Type()
)
usdMplsIfMinorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorRowStatus.setStatus("current")
_UsdMplsIfMinorLowerIfIndex_Type = InterfaceIndexOrZero
_UsdMplsIfMinorLowerIfIndex_Object = MibTableColumn
usdMplsIfMinorLowerIfIndex = _UsdMplsIfMinorLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 3),
    _UsdMplsIfMinorLowerIfIndex_Type()
)
usdMplsIfMinorLowerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdMplsIfMinorLowerIfIndex.setStatus("current")


class _UsdMplsIfMinorAdminStatus_Type(Integer32):
    """Custom type usdMplsIfMinorAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdMplsIfMinorAdminStatus_Type.__name__ = "Integer32"
_UsdMplsIfMinorAdminStatus_Object = MibTableColumn
usdMplsIfMinorAdminStatus = _UsdMplsIfMinorAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 4),
    _UsdMplsIfMinorAdminStatus_Type()
)
usdMplsIfMinorAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorAdminStatus.setStatus("current")
_UsdMplsIfMinorEndpointAddress_Type = IpAddress
_UsdMplsIfMinorEndpointAddress_Object = MibTableColumn
usdMplsIfMinorEndpointAddress = _UsdMplsIfMinorEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 5),
    _UsdMplsIfMinorEndpointAddress_Type()
)
usdMplsIfMinorEndpointAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorEndpointAddress.setStatus("current")


class _UsdMplsIfMinorEndpointDstMask_Type(IpAddress):
    """Custom type usdMplsIfMinorEndpointDstMask based on IpAddress"""
    defaultValue = 0


_UsdMplsIfMinorEndpointDstMask_Object = MibTableColumn
usdMplsIfMinorEndpointDstMask = _UsdMplsIfMinorEndpointDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 6),
    _UsdMplsIfMinorEndpointDstMask_Type()
)
usdMplsIfMinorEndpointDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorEndpointDstMask.setStatus("current")


class _UsdMplsIfMinorTunnelMetricMode_Type(Integer32):
    """Custom type usdMplsIfMinorTunnelMetricMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 0),
          ("relative", 1))
    )


_UsdMplsIfMinorTunnelMetricMode_Type.__name__ = "Integer32"
_UsdMplsIfMinorTunnelMetricMode_Object = MibTableColumn
usdMplsIfMinorTunnelMetricMode = _UsdMplsIfMinorTunnelMetricMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 7),
    _UsdMplsIfMinorTunnelMetricMode_Type()
)
usdMplsIfMinorTunnelMetricMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorTunnelMetricMode.setStatus("current")


class _UsdMplsIfMinorAbsoluteTunnelMetric_Type(Unsigned32):
    """Custom type usdMplsIfMinorAbsoluteTunnelMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_UsdMplsIfMinorAbsoluteTunnelMetric_Type.__name__ = "Unsigned32"
_UsdMplsIfMinorAbsoluteTunnelMetric_Object = MibTableColumn
usdMplsIfMinorAbsoluteTunnelMetric = _UsdMplsIfMinorAbsoluteTunnelMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 8),
    _UsdMplsIfMinorAbsoluteTunnelMetric_Type()
)
usdMplsIfMinorAbsoluteTunnelMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorAbsoluteTunnelMetric.setStatus("current")


class _UsdMplsIfMinorRelativeTunnelMetric_Type(Integer32):
    """Custom type usdMplsIfMinorRelativeTunnelMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_UsdMplsIfMinorRelativeTunnelMetric_Type.__name__ = "Integer32"
_UsdMplsIfMinorRelativeTunnelMetric_Object = MibTableColumn
usdMplsIfMinorRelativeTunnelMetric = _UsdMplsIfMinorRelativeTunnelMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 9),
    _UsdMplsIfMinorRelativeTunnelMetric_Type()
)
usdMplsIfMinorRelativeTunnelMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorRelativeTunnelMetric.setStatus("current")


class _UsdMplsIfMinorLabelDistProto_Type(Integer32):
    """Custom type usdMplsIfMinorLabelDistProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crLdp", 0),
          ("rsvpTe", 1),
          ("undefined", 2))
    )


_UsdMplsIfMinorLabelDistProto_Type.__name__ = "Integer32"
_UsdMplsIfMinorLabelDistProto_Object = MibTableColumn
usdMplsIfMinorLabelDistProto = _UsdMplsIfMinorLabelDistProto_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 10),
    _UsdMplsIfMinorLabelDistProto_Type()
)
usdMplsIfMinorLabelDistProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorLabelDistProto.setStatus("current")


class _UsdMplsIfMinorAnnounceToOspf_Type(TruthValue):
    """Custom type usdMplsIfMinorAnnounceToOspf based on TruthValue"""


_UsdMplsIfMinorAnnounceToOspf_Object = MibTableColumn
usdMplsIfMinorAnnounceToOspf = _UsdMplsIfMinorAnnounceToOspf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 11),
    _UsdMplsIfMinorAnnounceToOspf_Type()
)
usdMplsIfMinorAnnounceToOspf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorAnnounceToOspf.setStatus("current")


class _UsdMplsIfMinorAnnounceToIsis_Type(TruthValue):
    """Custom type usdMplsIfMinorAnnounceToIsis based on TruthValue"""


_UsdMplsIfMinorAnnounceToIsis_Object = MibTableColumn
usdMplsIfMinorAnnounceToIsis = _UsdMplsIfMinorAnnounceToIsis_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 12),
    _UsdMplsIfMinorAnnounceToIsis_Type()
)
usdMplsIfMinorAnnounceToIsis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorAnnounceToIsis.setStatus("current")


class _UsdMplsIfMinorAnnounceToBgp_Type(TruthValue):
    """Custom type usdMplsIfMinorAnnounceToBgp based on TruthValue"""


_UsdMplsIfMinorAnnounceToBgp_Object = MibTableColumn
usdMplsIfMinorAnnounceToBgp = _UsdMplsIfMinorAnnounceToBgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 13),
    _UsdMplsIfMinorAnnounceToBgp_Type()
)
usdMplsIfMinorAnnounceToBgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorAnnounceToBgp.setStatus("current")


class _UsdMplsIfMinorBandwidth_Type(UsdMinorCfgBWRanges):
    """Custom type usdMplsIfMinorBandwidth based on UsdMinorCfgBWRanges"""
    defaultValue = 0


_UsdMplsIfMinorBandwidth_Object = MibTableColumn
usdMplsIfMinorBandwidth = _UsdMplsIfMinorBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 14),
    _UsdMplsIfMinorBandwidth_Type()
)
usdMplsIfMinorBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorBandwidth.setStatus("current")


class _UsdMplsIfMinorAffinity_Type(OctetString):
    """Custom type usdMplsIfMinorAffinity based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_UsdMplsIfMinorAffinity_Type.__name__ = "OctetString"
_UsdMplsIfMinorAffinity_Object = MibTableColumn
usdMplsIfMinorAffinity = _UsdMplsIfMinorAffinity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 15),
    _UsdMplsIfMinorAffinity_Type()
)
usdMplsIfMinorAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorAffinity.setStatus("current")


class _UsdMplsIfMinorAffinityMask_Type(OctetString):
    """Custom type usdMplsIfMinorAffinityMask based on OctetString"""
    defaultHexValue = "0000ffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_UsdMplsIfMinorAffinityMask_Type.__name__ = "OctetString"
_UsdMplsIfMinorAffinityMask_Object = MibTableColumn
usdMplsIfMinorAffinityMask = _UsdMplsIfMinorAffinityMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 16),
    _UsdMplsIfMinorAffinityMask_Type()
)
usdMplsIfMinorAffinityMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorAffinityMask.setStatus("current")
_UsdMplsIfMinorSetupPriority_Type = UsdMinorCfgHoldingAndSetupPriorityRanges
_UsdMplsIfMinorSetupPriority_Object = MibTableColumn
usdMplsIfMinorSetupPriority = _UsdMplsIfMinorSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 17),
    _UsdMplsIfMinorSetupPriority_Type()
)
usdMplsIfMinorSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorSetupPriority.setStatus("current")
_UsdMplsIfMinorHoldingPriority_Type = UsdMinorCfgHoldingAndSetupPriorityRanges
_UsdMplsIfMinorHoldingPriority_Object = MibTableColumn
usdMplsIfMinorHoldingPriority = _UsdMplsIfMinorHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 18),
    _UsdMplsIfMinorHoldingPriority_Type()
)
usdMplsIfMinorHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorHoldingPriority.setStatus("current")


class _UsdMplsIfMinorTunnelName_Type(DisplayString):
    """Custom type usdMplsIfMinorTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsIfMinorTunnelName_Type.__name__ = "DisplayString"
_UsdMplsIfMinorTunnelName_Object = MibTableColumn
usdMplsIfMinorTunnelName = _UsdMplsIfMinorTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 19),
    _UsdMplsIfMinorTunnelName_Type()
)
usdMplsIfMinorTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorTunnelName.setStatus("current")


class _UsdMplsIfMinorTunnelRetryTimes_Type(UsdMinorCfgRetryTimesAndNorouteRanges):
    """Custom type usdMplsIfMinorTunnelRetryTimes based on UsdMinorCfgRetryTimesAndNorouteRanges"""
    defaultValue = 0


_UsdMplsIfMinorTunnelRetryTimes_Object = MibTableColumn
usdMplsIfMinorTunnelRetryTimes = _UsdMplsIfMinorTunnelRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 20),
    _UsdMplsIfMinorTunnelRetryTimes_Type()
)
usdMplsIfMinorTunnelRetryTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorTunnelRetryTimes.setStatus("current")


class _UsdMplsIfMinorTunnelRetryInterval_Type(UsdMinorCfgRetryIntervalAndNorouteRanges):
    """Custom type usdMplsIfMinorTunnelRetryInterval based on UsdMinorCfgRetryIntervalAndNorouteRanges"""
    defaultValue = 5


_UsdMplsIfMinorTunnelRetryInterval_Object = MibTableColumn
usdMplsIfMinorTunnelRetryInterval = _UsdMplsIfMinorTunnelRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 21),
    _UsdMplsIfMinorTunnelRetryInterval_Type()
)
usdMplsIfMinorTunnelRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorTunnelRetryInterval.setStatus("current")


class _UsdMplsIfMinorTunnelRetryTimesNoroute_Type(UsdMinorCfgRetryTimesAndNorouteRanges):
    """Custom type usdMplsIfMinorTunnelRetryTimesNoroute based on UsdMinorCfgRetryTimesAndNorouteRanges"""
    defaultValue = 0


_UsdMplsIfMinorTunnelRetryTimesNoroute_Object = MibTableColumn
usdMplsIfMinorTunnelRetryTimesNoroute = _UsdMplsIfMinorTunnelRetryTimesNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 22),
    _UsdMplsIfMinorTunnelRetryTimesNoroute_Type()
)
usdMplsIfMinorTunnelRetryTimesNoroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorTunnelRetryTimesNoroute.setStatus("current")


class _UsdMplsIfMinorTunnelRetryIntervalNoroute_Type(UsdMinorCfgRetryIntervalAndNorouteRanges):
    """Custom type usdMplsIfMinorTunnelRetryIntervalNoroute based on UsdMinorCfgRetryIntervalAndNorouteRanges"""
    defaultValue = 5


_UsdMplsIfMinorTunnelRetryIntervalNoroute_Object = MibTableColumn
usdMplsIfMinorTunnelRetryIntervalNoroute = _UsdMplsIfMinorTunnelRetryIntervalNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 23),
    _UsdMplsIfMinorTunnelRetryIntervalNoroute_Type()
)
usdMplsIfMinorTunnelRetryIntervalNoroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorTunnelRetryIntervalNoroute.setStatus("current")
_UsdMplsIfMinorBaseTunnelName_Type = DisplayString
_UsdMplsIfMinorBaseTunnelName_Object = MibTableColumn
usdMplsIfMinorBaseTunnelName = _UsdMplsIfMinorBaseTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 24),
    _UsdMplsIfMinorBaseTunnelName_Type()
)
usdMplsIfMinorBaseTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorBaseTunnelName.setStatus("current")


class _UsdMplsIfMinorVpnOuiNumber_Type(Integer32):
    """Custom type usdMplsIfMinorVpnOuiNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_UsdMplsIfMinorVpnOuiNumber_Type.__name__ = "Integer32"
_UsdMplsIfMinorVpnOuiNumber_Object = MibTableColumn
usdMplsIfMinorVpnOuiNumber = _UsdMplsIfMinorVpnOuiNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 25),
    _UsdMplsIfMinorVpnOuiNumber_Type()
)
usdMplsIfMinorVpnOuiNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorVpnOuiNumber.setStatus("current")
_UsdMplsIfMinorVpnIndex_Type = IpAddress
_UsdMplsIfMinorVpnIndex_Object = MibTableColumn
usdMplsIfMinorVpnIndex = _UsdMplsIfMinorVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 26),
    _UsdMplsIfMinorVpnIndex_Type()
)
usdMplsIfMinorVpnIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorVpnIndex.setStatus("current")


class _UsdMplsIfMinorTunnelOpState_Type(Integer32):
    """Custom type usdMplsIfMinorTunnelOpState based on Integer32"""
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
        *(("cfgChanged", 4),
          ("cfgIncDis", 6),
          ("cfgIncEn", 5),
          ("disabled", 7),
          ("down", 3),
          ("established", 0),
          ("noChange", 9),
          ("rel", 8),
          ("teNegotiation", 1),
          ("up", 2))
    )


_UsdMplsIfMinorTunnelOpState_Type.__name__ = "Integer32"
_UsdMplsIfMinorTunnelOpState_Object = MibTableColumn
usdMplsIfMinorTunnelOpState = _UsdMplsIfMinorTunnelOpState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 27),
    _UsdMplsIfMinorTunnelOpState_Type()
)
usdMplsIfMinorTunnelOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdMplsIfMinorTunnelOpState.setStatus("current")


class _UsdMplsIfMinorTargetedDynamicTunnel_Type(TruthValue):
    """Custom type usdMplsIfMinorTargetedDynamicTunnel based on TruthValue"""


_UsdMplsIfMinorTargetedDynamicTunnel_Object = MibTableColumn
usdMplsIfMinorTargetedDynamicTunnel = _UsdMplsIfMinorTargetedDynamicTunnel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 28),
    _UsdMplsIfMinorTargetedDynamicTunnel_Type()
)
usdMplsIfMinorTargetedDynamicTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorTargetedDynamicTunnel.setStatus("current")


class _UsdMplsIfMinorReoptimization_Type(TruthValue):
    """Custom type usdMplsIfMinorReoptimization based on TruthValue"""


_UsdMplsIfMinorReoptimization_Object = MibTableColumn
usdMplsIfMinorReoptimization = _UsdMplsIfMinorReoptimization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 29),
    _UsdMplsIfMinorReoptimization_Type()
)
usdMplsIfMinorReoptimization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorReoptimization.setStatus("current")
_UsdMplsMinorLayerList_ObjectIdentity = ObjectIdentity
usdMplsMinorLayerList = _UsdMplsMinorLayerList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2)
)
_UsdMplsIfMinorPathOptionTable_Object = MibTable
usdMplsIfMinorPathOptionTable = _UsdMplsIfMinorPathOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    usdMplsIfMinorPathOptionTable.setStatus("current")
_UsdMplsIfMinorPathOptionEntry_Object = MibTableRow
usdMplsIfMinorPathOptionEntry = _UsdMplsIfMinorPathOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1)
)
usdMplsIfMinorPathOptionEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionIndex"),
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionNumber"),
)
if mibBuilder.loadTexts:
    usdMplsIfMinorPathOptionEntry.setStatus("current")
_UsdMplsIfMinorPathOptionIndex_Type = InterfaceIndex
_UsdMplsIfMinorPathOptionIndex_Object = MibTableColumn
usdMplsIfMinorPathOptionIndex = _UsdMplsIfMinorPathOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 1),
    _UsdMplsIfMinorPathOptionIndex_Type()
)
usdMplsIfMinorPathOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsIfMinorPathOptionIndex.setStatus("current")


class _UsdMplsIfMinorPathOptionNumber_Type(Integer32):
    """Custom type usdMplsIfMinorPathOptionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_UsdMplsIfMinorPathOptionNumber_Type.__name__ = "Integer32"
_UsdMplsIfMinorPathOptionNumber_Object = MibTableColumn
usdMplsIfMinorPathOptionNumber = _UsdMplsIfMinorPathOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 2),
    _UsdMplsIfMinorPathOptionNumber_Type()
)
usdMplsIfMinorPathOptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsIfMinorPathOptionNumber.setStatus("current")


class _UsdMplsIfMinorPathOptionProtocol_Type(Integer32):
    """Custom type usdMplsIfMinorPathOptionProtocol based on Integer32"""
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
        *(("hopByHop", 0),
          ("isis", 1),
          ("none", 3),
          ("ospf", 2))
    )


_UsdMplsIfMinorPathOptionProtocol_Type.__name__ = "Integer32"
_UsdMplsIfMinorPathOptionProtocol_Object = MibTableColumn
usdMplsIfMinorPathOptionProtocol = _UsdMplsIfMinorPathOptionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 3),
    _UsdMplsIfMinorPathOptionProtocol_Type()
)
usdMplsIfMinorPathOptionProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorPathOptionProtocol.setStatus("current")
_UsdMplsIfMinorPathOptionLockdown_Type = TruthValue
_UsdMplsIfMinorPathOptionLockdown_Object = MibTableColumn
usdMplsIfMinorPathOptionLockdown = _UsdMplsIfMinorPathOptionLockdown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 4),
    _UsdMplsIfMinorPathOptionLockdown_Type()
)
usdMplsIfMinorPathOptionLockdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorPathOptionLockdown.setStatus("current")


class _UsdMplsIfMinorPathOptionPathName_Type(DisplayString):
    """Custom type usdMplsIfMinorPathOptionPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsIfMinorPathOptionPathName_Type.__name__ = "DisplayString"
_UsdMplsIfMinorPathOptionPathName_Object = MibTableColumn
usdMplsIfMinorPathOptionPathName = _UsdMplsIfMinorPathOptionPathName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 5),
    _UsdMplsIfMinorPathOptionPathName_Type()
)
usdMplsIfMinorPathOptionPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorPathOptionPathName.setStatus("current")


class _UsdMplsIfMinorPathOptionPathId_Type(Integer32):
    """Custom type usdMplsIfMinorPathOptionPathId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdMplsIfMinorPathOptionPathId_Type.__name__ = "Integer32"
_UsdMplsIfMinorPathOptionPathId_Object = MibTableColumn
usdMplsIfMinorPathOptionPathId = _UsdMplsIfMinorPathOptionPathId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 6),
    _UsdMplsIfMinorPathOptionPathId_Type()
)
usdMplsIfMinorPathOptionPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorPathOptionPathId.setStatus("current")
_UsdMplsIfMinorPathOptionRowStatus_Type = RowStatus
_UsdMplsIfMinorPathOptionRowStatus_Object = MibTableColumn
usdMplsIfMinorPathOptionRowStatus = _UsdMplsIfMinorPathOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 7),
    _UsdMplsIfMinorPathOptionRowStatus_Type()
)
usdMplsIfMinorPathOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsIfMinorPathOptionRowStatus.setStatus("current")
_UsdMplsTunnelProfile_ObjectIdentity = ObjectIdentity
usdMplsTunnelProfile = _UsdMplsTunnelProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4)
)
_UsdMplsTunnelProfileGroup_ObjectIdentity = ObjectIdentity
usdMplsTunnelProfileGroup = _UsdMplsTunnelProfileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1)
)
_UsdMplsTunnelProfileTable_Object = MibTable
usdMplsTunnelProfileTable = _UsdMplsTunnelProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdMplsTunnelProfileTable.setStatus("current")
_UsdMplsTunnelProfileEntry_Object = MibTableRow
usdMplsTunnelProfileEntry = _UsdMplsTunnelProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1)
)
usdMplsTunnelProfileEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileName"),
)
if mibBuilder.loadTexts:
    usdMplsTunnelProfileEntry.setStatus("current")


class _UsdMplsTunnelProfileName_Type(DisplayString):
    """Custom type usdMplsTunnelProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsTunnelProfileName_Type.__name__ = "DisplayString"
_UsdMplsTunnelProfileName_Object = MibTableColumn
usdMplsTunnelProfileName = _UsdMplsTunnelProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 1),
    _UsdMplsTunnelProfileName_Type()
)
usdMplsTunnelProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileName.setStatus("current")


class _UsdMplsTunnelProfileAdminStatus_Type(Integer32):
    """Custom type usdMplsTunnelProfileAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdMplsTunnelProfileAdminStatus_Type.__name__ = "Integer32"
_UsdMplsTunnelProfileAdminStatus_Object = MibTableColumn
usdMplsTunnelProfileAdminStatus = _UsdMplsTunnelProfileAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 2),
    _UsdMplsTunnelProfileAdminStatus_Type()
)
usdMplsTunnelProfileAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileAdminStatus.setStatus("current")
_UsdMplsTunnelProfileBaseTunnelName_Type = DisplayString
_UsdMplsTunnelProfileBaseTunnelName_Object = MibTableColumn
usdMplsTunnelProfileBaseTunnelName = _UsdMplsTunnelProfileBaseTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 3),
    _UsdMplsTunnelProfileBaseTunnelName_Type()
)
usdMplsTunnelProfileBaseTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileBaseTunnelName.setStatus("current")


class _UsdMplsTunnelProfileIpProfileName_Type(DisplayString):
    """Custom type usdMplsTunnelProfileIpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsTunnelProfileIpProfileName_Type.__name__ = "DisplayString"
_UsdMplsTunnelProfileIpProfileName_Object = MibTableColumn
usdMplsTunnelProfileIpProfileName = _UsdMplsTunnelProfileIpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 4),
    _UsdMplsTunnelProfileIpProfileName_Type()
)
usdMplsTunnelProfileIpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileIpProfileName.setStatus("current")


class _UsdMplsTunnelProfileLabelDistProto_Type(Integer32):
    """Custom type usdMplsTunnelProfileLabelDistProto based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crLdp", 0),
          ("rsvpTe", 1),
          ("undefined", 2))
    )


_UsdMplsTunnelProfileLabelDistProto_Type.__name__ = "Integer32"
_UsdMplsTunnelProfileLabelDistProto_Object = MibTableColumn
usdMplsTunnelProfileLabelDistProto = _UsdMplsTunnelProfileLabelDistProto_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 5),
    _UsdMplsTunnelProfileLabelDistProto_Type()
)
usdMplsTunnelProfileLabelDistProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileLabelDistProto.setStatus("current")


class _UsdMplsTunnelProfileAnnounceToOspf_Type(TruthValue):
    """Custom type usdMplsTunnelProfileAnnounceToOspf based on TruthValue"""


_UsdMplsTunnelProfileAnnounceToOspf_Object = MibTableColumn
usdMplsTunnelProfileAnnounceToOspf = _UsdMplsTunnelProfileAnnounceToOspf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 6),
    _UsdMplsTunnelProfileAnnounceToOspf_Type()
)
usdMplsTunnelProfileAnnounceToOspf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileAnnounceToOspf.setStatus("current")


class _UsdMplsTunnelProfileAnnounceToIsis_Type(TruthValue):
    """Custom type usdMplsTunnelProfileAnnounceToIsis based on TruthValue"""


_UsdMplsTunnelProfileAnnounceToIsis_Object = MibTableColumn
usdMplsTunnelProfileAnnounceToIsis = _UsdMplsTunnelProfileAnnounceToIsis_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 7),
    _UsdMplsTunnelProfileAnnounceToIsis_Type()
)
usdMplsTunnelProfileAnnounceToIsis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileAnnounceToIsis.setStatus("current")


class _UsdMplsTunnelProfileAnnounceToBgp_Type(TruthValue):
    """Custom type usdMplsTunnelProfileAnnounceToBgp based on TruthValue"""


_UsdMplsTunnelProfileAnnounceToBgp_Object = MibTableColumn
usdMplsTunnelProfileAnnounceToBgp = _UsdMplsTunnelProfileAnnounceToBgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 8),
    _UsdMplsTunnelProfileAnnounceToBgp_Type()
)
usdMplsTunnelProfileAnnounceToBgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileAnnounceToBgp.setStatus("current")


class _UsdMplsTunnelProfileMetricMode_Type(Integer32):
    """Custom type usdMplsTunnelProfileMetricMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 0),
          ("relative", 1))
    )


_UsdMplsTunnelProfileMetricMode_Type.__name__ = "Integer32"
_UsdMplsTunnelProfileMetricMode_Object = MibTableColumn
usdMplsTunnelProfileMetricMode = _UsdMplsTunnelProfileMetricMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 9),
    _UsdMplsTunnelProfileMetricMode_Type()
)
usdMplsTunnelProfileMetricMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileMetricMode.setStatus("current")


class _UsdMplsTunnelProfileAbsoluteMetric_Type(Unsigned32):
    """Custom type usdMplsTunnelProfileAbsoluteMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_UsdMplsTunnelProfileAbsoluteMetric_Type.__name__ = "Unsigned32"
_UsdMplsTunnelProfileAbsoluteMetric_Object = MibTableColumn
usdMplsTunnelProfileAbsoluteMetric = _UsdMplsTunnelProfileAbsoluteMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 10),
    _UsdMplsTunnelProfileAbsoluteMetric_Type()
)
usdMplsTunnelProfileAbsoluteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileAbsoluteMetric.setStatus("current")


class _UsdMplsTunnelProfileRelativeMetric_Type(Integer32):
    """Custom type usdMplsTunnelProfileRelativeMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_UsdMplsTunnelProfileRelativeMetric_Type.__name__ = "Integer32"
_UsdMplsTunnelProfileRelativeMetric_Object = MibTableColumn
usdMplsTunnelProfileRelativeMetric = _UsdMplsTunnelProfileRelativeMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 11),
    _UsdMplsTunnelProfileRelativeMetric_Type()
)
usdMplsTunnelProfileRelativeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileRelativeMetric.setStatus("current")


class _UsdMplsTunnelProfileBandwidth_Type(UsdProfileCfgBWRanges):
    """Custom type usdMplsTunnelProfileBandwidth based on UsdProfileCfgBWRanges"""
    defaultValue = 0


_UsdMplsTunnelProfileBandwidth_Object = MibTableColumn
usdMplsTunnelProfileBandwidth = _UsdMplsTunnelProfileBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 12),
    _UsdMplsTunnelProfileBandwidth_Type()
)
usdMplsTunnelProfileBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileBandwidth.setStatus("current")


class _UsdMplsTunnelProfileAffinity_Type(OctetString):
    """Custom type usdMplsTunnelProfileAffinity based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_UsdMplsTunnelProfileAffinity_Type.__name__ = "OctetString"
_UsdMplsTunnelProfileAffinity_Object = MibTableColumn
usdMplsTunnelProfileAffinity = _UsdMplsTunnelProfileAffinity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 13),
    _UsdMplsTunnelProfileAffinity_Type()
)
usdMplsTunnelProfileAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileAffinity.setStatus("current")


class _UsdMplsTunnelProfileAffinityMask_Type(OctetString):
    """Custom type usdMplsTunnelProfileAffinityMask based on OctetString"""
    defaultHexValue = "0000ffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_UsdMplsTunnelProfileAffinityMask_Type.__name__ = "OctetString"
_UsdMplsTunnelProfileAffinityMask_Object = MibTableColumn
usdMplsTunnelProfileAffinityMask = _UsdMplsTunnelProfileAffinityMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 14),
    _UsdMplsTunnelProfileAffinityMask_Type()
)
usdMplsTunnelProfileAffinityMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileAffinityMask.setStatus("current")


class _UsdMplsTunnelProfileSetupPriority_Type(UsdProfileCfgHoldingAndSetupPriorityRanges):
    """Custom type usdMplsTunnelProfileSetupPriority based on UsdProfileCfgHoldingAndSetupPriorityRanges"""
    defaultValue = 0


_UsdMplsTunnelProfileSetupPriority_Object = MibTableColumn
usdMplsTunnelProfileSetupPriority = _UsdMplsTunnelProfileSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 15),
    _UsdMplsTunnelProfileSetupPriority_Type()
)
usdMplsTunnelProfileSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileSetupPriority.setStatus("current")


class _UsdMplsTunnelProfileHoldingPriority_Type(UsdProfileCfgHoldingAndSetupPriorityRanges):
    """Custom type usdMplsTunnelProfileHoldingPriority based on UsdProfileCfgHoldingAndSetupPriorityRanges"""
    defaultValue = 0


_UsdMplsTunnelProfileHoldingPriority_Object = MibTableColumn
usdMplsTunnelProfileHoldingPriority = _UsdMplsTunnelProfileHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 16),
    _UsdMplsTunnelProfileHoldingPriority_Type()
)
usdMplsTunnelProfileHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileHoldingPriority.setStatus("current")


class _UsdMplsTunnelProfileRetryTimes_Type(UsdProfileCfgRetryTimesAndNorouteRanges):
    """Custom type usdMplsTunnelProfileRetryTimes based on UsdProfileCfgRetryTimesAndNorouteRanges"""
    defaultValue = 0


_UsdMplsTunnelProfileRetryTimes_Object = MibTableColumn
usdMplsTunnelProfileRetryTimes = _UsdMplsTunnelProfileRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 17),
    _UsdMplsTunnelProfileRetryTimes_Type()
)
usdMplsTunnelProfileRetryTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileRetryTimes.setStatus("current")


class _UsdMplsTunnelProfileRetryInterval_Type(UsdProfileCfgRetryIntervalAndNorouteRanges):
    """Custom type usdMplsTunnelProfileRetryInterval based on UsdProfileCfgRetryIntervalAndNorouteRanges"""
    defaultValue = 5


_UsdMplsTunnelProfileRetryInterval_Object = MibTableColumn
usdMplsTunnelProfileRetryInterval = _UsdMplsTunnelProfileRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 18),
    _UsdMplsTunnelProfileRetryInterval_Type()
)
usdMplsTunnelProfileRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileRetryInterval.setStatus("current")


class _UsdMplsTunnelProfileRetryTimesNoroute_Type(UsdProfileCfgRetryTimesAndNorouteRanges):
    """Custom type usdMplsTunnelProfileRetryTimesNoroute based on UsdProfileCfgRetryTimesAndNorouteRanges"""
    defaultValue = 0


_UsdMplsTunnelProfileRetryTimesNoroute_Object = MibTableColumn
usdMplsTunnelProfileRetryTimesNoroute = _UsdMplsTunnelProfileRetryTimesNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 19),
    _UsdMplsTunnelProfileRetryTimesNoroute_Type()
)
usdMplsTunnelProfileRetryTimesNoroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileRetryTimesNoroute.setStatus("current")


class _UsdMplsTunnelProfileRetryIntervalNoroute_Type(UsdProfileCfgRetryIntervalAndNorouteRanges):
    """Custom type usdMplsTunnelProfileRetryIntervalNoroute based on UsdProfileCfgRetryIntervalAndNorouteRanges"""
    defaultValue = 5


_UsdMplsTunnelProfileRetryIntervalNoroute_Object = MibTableColumn
usdMplsTunnelProfileRetryIntervalNoroute = _UsdMplsTunnelProfileRetryIntervalNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 20),
    _UsdMplsTunnelProfileRetryIntervalNoroute_Type()
)
usdMplsTunnelProfileRetryIntervalNoroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileRetryIntervalNoroute.setStatus("current")


class _UsdMplsTunnelProfileVpnOuiNumber_Type(Integer32):
    """Custom type usdMplsTunnelProfileVpnOuiNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_UsdMplsTunnelProfileVpnOuiNumber_Type.__name__ = "Integer32"
_UsdMplsTunnelProfileVpnOuiNumber_Object = MibTableColumn
usdMplsTunnelProfileVpnOuiNumber = _UsdMplsTunnelProfileVpnOuiNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 21),
    _UsdMplsTunnelProfileVpnOuiNumber_Type()
)
usdMplsTunnelProfileVpnOuiNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileVpnOuiNumber.setStatus("current")
_UsdMplsTunnelProfileVpnIndex_Type = IpAddress
_UsdMplsTunnelProfileVpnIndex_Object = MibTableColumn
usdMplsTunnelProfileVpnIndex = _UsdMplsTunnelProfileVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 22),
    _UsdMplsTunnelProfileVpnIndex_Type()
)
usdMplsTunnelProfileVpnIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileVpnIndex.setStatus("current")
_UsdMplsTunnelProfileRowStatus_Type = RowStatus
_UsdMplsTunnelProfileRowStatus_Object = MibTableColumn
usdMplsTunnelProfileRowStatus = _UsdMplsTunnelProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 23),
    _UsdMplsTunnelProfileRowStatus_Type()
)
usdMplsTunnelProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileRowStatus.setStatus("current")


class _UsdMplsTunnelProfileTargetedDynamicTunnel_Type(TruthValue):
    """Custom type usdMplsTunnelProfileTargetedDynamicTunnel based on TruthValue"""


_UsdMplsTunnelProfileTargetedDynamicTunnel_Object = MibTableColumn
usdMplsTunnelProfileTargetedDynamicTunnel = _UsdMplsTunnelProfileTargetedDynamicTunnel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 24),
    _UsdMplsTunnelProfileTargetedDynamicTunnel_Type()
)
usdMplsTunnelProfileTargetedDynamicTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileTargetedDynamicTunnel.setStatus("current")
_UsdMplsTunnelProfileList_ObjectIdentity = ObjectIdentity
usdMplsTunnelProfileList = _UsdMplsTunnelProfileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2)
)
_UsdMplsTunnelProfilePathOptionTable_Object = MibTable
usdMplsTunnelProfilePathOptionTable = _UsdMplsTunnelProfilePathOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    usdMplsTunnelProfilePathOptionTable.setStatus("current")
_UsdMplsTunnelProfilePathOptionEntry_Object = MibTableRow
usdMplsTunnelProfilePathOptionEntry = _UsdMplsTunnelProfilePathOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1)
)
usdMplsTunnelProfilePathOptionEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileNamePathOption"),
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfilePathOptionNumber"),
)
if mibBuilder.loadTexts:
    usdMplsTunnelProfilePathOptionEntry.setStatus("current")


class _UsdMplsTunnelProfileNamePathOption_Type(DisplayString):
    """Custom type usdMplsTunnelProfileNamePathOption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsTunnelProfileNamePathOption_Type.__name__ = "DisplayString"
_UsdMplsTunnelProfileNamePathOption_Object = MibTableColumn
usdMplsTunnelProfileNamePathOption = _UsdMplsTunnelProfileNamePathOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 1),
    _UsdMplsTunnelProfileNamePathOption_Type()
)
usdMplsTunnelProfileNamePathOption.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileNamePathOption.setStatus("current")


class _UsdMplsTunnelProfilePathOptionNumber_Type(Integer32):
    """Custom type usdMplsTunnelProfilePathOptionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_UsdMplsTunnelProfilePathOptionNumber_Type.__name__ = "Integer32"
_UsdMplsTunnelProfilePathOptionNumber_Object = MibTableColumn
usdMplsTunnelProfilePathOptionNumber = _UsdMplsTunnelProfilePathOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 2),
    _UsdMplsTunnelProfilePathOptionNumber_Type()
)
usdMplsTunnelProfilePathOptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsTunnelProfilePathOptionNumber.setStatus("current")


class _UsdMplsTunnelProfilePathOptionProtocol_Type(Integer32):
    """Custom type usdMplsTunnelProfilePathOptionProtocol based on Integer32"""
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
        *(("hopByHop", 0),
          ("isis", 1),
          ("none", 3),
          ("ospf", 2))
    )


_UsdMplsTunnelProfilePathOptionProtocol_Type.__name__ = "Integer32"
_UsdMplsTunnelProfilePathOptionProtocol_Object = MibTableColumn
usdMplsTunnelProfilePathOptionProtocol = _UsdMplsTunnelProfilePathOptionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 3),
    _UsdMplsTunnelProfilePathOptionProtocol_Type()
)
usdMplsTunnelProfilePathOptionProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfilePathOptionProtocol.setStatus("current")
_UsdMplsTunnelProfilePathOptionLockdown_Type = TruthValue
_UsdMplsTunnelProfilePathOptionLockdown_Object = MibTableColumn
usdMplsTunnelProfilePathOptionLockdown = _UsdMplsTunnelProfilePathOptionLockdown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 4),
    _UsdMplsTunnelProfilePathOptionLockdown_Type()
)
usdMplsTunnelProfilePathOptionLockdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfilePathOptionLockdown.setStatus("current")


class _UsdMplsTunnelProfilePathOptionPathName_Type(DisplayString):
    """Custom type usdMplsTunnelProfilePathOptionPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsTunnelProfilePathOptionPathName_Type.__name__ = "DisplayString"
_UsdMplsTunnelProfilePathOptionPathName_Object = MibTableColumn
usdMplsTunnelProfilePathOptionPathName = _UsdMplsTunnelProfilePathOptionPathName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 5),
    _UsdMplsTunnelProfilePathOptionPathName_Type()
)
usdMplsTunnelProfilePathOptionPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfilePathOptionPathName.setStatus("current")


class _UsdMplsTunnelProfilePathOptionPathId_Type(Integer32):
    """Custom type usdMplsTunnelProfilePathOptionPathId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdMplsTunnelProfilePathOptionPathId_Type.__name__ = "Integer32"
_UsdMplsTunnelProfilePathOptionPathId_Object = MibTableColumn
usdMplsTunnelProfilePathOptionPathId = _UsdMplsTunnelProfilePathOptionPathId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 6),
    _UsdMplsTunnelProfilePathOptionPathId_Type()
)
usdMplsTunnelProfilePathOptionPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfilePathOptionPathId.setStatus("current")
_UsdMplsTunnelProfilePathOptionRowStatus_Type = RowStatus
_UsdMplsTunnelProfilePathOptionRowStatus_Object = MibTableColumn
usdMplsTunnelProfilePathOptionRowStatus = _UsdMplsTunnelProfilePathOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 7),
    _UsdMplsTunnelProfilePathOptionRowStatus_Type()
)
usdMplsTunnelProfilePathOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfilePathOptionRowStatus.setStatus("current")
_UsdMplsTunnelProfileDynamicEndpointTable_Object = MibTable
usdMplsTunnelProfileDynamicEndpointTable = _UsdMplsTunnelProfileDynamicEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    usdMplsTunnelProfileDynamicEndpointTable.setStatus("current")
_UsdMplsTunnelProfileDynamicEndpointEntry_Object = MibTableRow
usdMplsTunnelProfileDynamicEndpointEntry = _UsdMplsTunnelProfileDynamicEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1)
)
usdMplsTunnelProfileDynamicEndpointEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileNameDynamicEndpoint"),
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileDynamicEndpointType"),
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileDynamicEndpointPolicyListType"),
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileDynamicEndpointListName"),
)
if mibBuilder.loadTexts:
    usdMplsTunnelProfileDynamicEndpointEntry.setStatus("current")


class _UsdMplsTunnelProfileNameDynamicEndpoint_Type(DisplayString):
    """Custom type usdMplsTunnelProfileNameDynamicEndpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsTunnelProfileNameDynamicEndpoint_Type.__name__ = "DisplayString"
_UsdMplsTunnelProfileNameDynamicEndpoint_Object = MibTableColumn
usdMplsTunnelProfileNameDynamicEndpoint = _UsdMplsTunnelProfileNameDynamicEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1, 1),
    _UsdMplsTunnelProfileNameDynamicEndpoint_Type()
)
usdMplsTunnelProfileNameDynamicEndpoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileNameDynamicEndpoint.setStatus("current")


class _UsdMplsTunnelProfileDynamicEndpointType_Type(Integer32):
    """Custom type usdMplsTunnelProfileDynamicEndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isisLevel2", 0),
          ("ospfBorder", 1))
    )


_UsdMplsTunnelProfileDynamicEndpointType_Type.__name__ = "Integer32"
_UsdMplsTunnelProfileDynamicEndpointType_Object = MibTableColumn
usdMplsTunnelProfileDynamicEndpointType = _UsdMplsTunnelProfileDynamicEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1, 2),
    _UsdMplsTunnelProfileDynamicEndpointType_Type()
)
usdMplsTunnelProfileDynamicEndpointType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileDynamicEndpointType.setStatus("current")


class _UsdMplsTunnelProfileDynamicEndpointPolicyListType_Type(Integer32):
    """Custom type usdMplsTunnelProfileDynamicEndpointPolicyListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accessList", 1),
          ("noPolicyList", 3),
          ("prefixList", 2))
    )


_UsdMplsTunnelProfileDynamicEndpointPolicyListType_Type.__name__ = "Integer32"
_UsdMplsTunnelProfileDynamicEndpointPolicyListType_Object = MibTableColumn
usdMplsTunnelProfileDynamicEndpointPolicyListType = _UsdMplsTunnelProfileDynamicEndpointPolicyListType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1, 3),
    _UsdMplsTunnelProfileDynamicEndpointPolicyListType_Type()
)
usdMplsTunnelProfileDynamicEndpointPolicyListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileDynamicEndpointPolicyListType.setStatus("current")


class _UsdMplsTunnelProfileDynamicEndpointListName_Type(DisplayString):
    """Custom type usdMplsTunnelProfileDynamicEndpointListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsTunnelProfileDynamicEndpointListName_Type.__name__ = "DisplayString"
_UsdMplsTunnelProfileDynamicEndpointListName_Object = MibTableColumn
usdMplsTunnelProfileDynamicEndpointListName = _UsdMplsTunnelProfileDynamicEndpointListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1, 4),
    _UsdMplsTunnelProfileDynamicEndpointListName_Type()
)
usdMplsTunnelProfileDynamicEndpointListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileDynamicEndpointListName.setStatus("current")
_UsdMplsTunnelProfileDynamicEndpointRowStatus_Type = RowStatus
_UsdMplsTunnelProfileDynamicEndpointRowStatus_Object = MibTableColumn
usdMplsTunnelProfileDynamicEndpointRowStatus = _UsdMplsTunnelProfileDynamicEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1, 5),
    _UsdMplsTunnelProfileDynamicEndpointRowStatus_Type()
)
usdMplsTunnelProfileDynamicEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileDynamicEndpointRowStatus.setStatus("current")
_UsdMplsTunnelProfileTunnelEndpointTable_Object = MibTable
usdMplsTunnelProfileTunnelEndpointTable = _UsdMplsTunnelProfileTunnelEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    usdMplsTunnelProfileTunnelEndpointTable.setStatus("current")
_UsdMplsTunnelProfileTunnelEndpointEntry_Object = MibTableRow
usdMplsTunnelProfileTunnelEndpointEntry = _UsdMplsTunnelProfileTunnelEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3, 1)
)
usdMplsTunnelProfileTunnelEndpointEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileNameTunnelEndpoint"),
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileTunnelEndpointAddress"),
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileTunnelEndpointDstMask"),
)
if mibBuilder.loadTexts:
    usdMplsTunnelProfileTunnelEndpointEntry.setStatus("current")


class _UsdMplsTunnelProfileNameTunnelEndpoint_Type(DisplayString):
    """Custom type usdMplsTunnelProfileNameTunnelEndpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsTunnelProfileNameTunnelEndpoint_Type.__name__ = "DisplayString"
_UsdMplsTunnelProfileNameTunnelEndpoint_Object = MibTableColumn
usdMplsTunnelProfileNameTunnelEndpoint = _UsdMplsTunnelProfileNameTunnelEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3, 1, 1),
    _UsdMplsTunnelProfileNameTunnelEndpoint_Type()
)
usdMplsTunnelProfileNameTunnelEndpoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileNameTunnelEndpoint.setStatus("current")
_UsdMplsTunnelProfileTunnelEndpointAddress_Type = IpAddress
_UsdMplsTunnelProfileTunnelEndpointAddress_Object = MibTableColumn
usdMplsTunnelProfileTunnelEndpointAddress = _UsdMplsTunnelProfileTunnelEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3, 1, 2),
    _UsdMplsTunnelProfileTunnelEndpointAddress_Type()
)
usdMplsTunnelProfileTunnelEndpointAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileTunnelEndpointAddress.setStatus("current")
_UsdMplsTunnelProfileTunnelEndpointDstMask_Type = IpAddress
_UsdMplsTunnelProfileTunnelEndpointDstMask_Object = MibTableColumn
usdMplsTunnelProfileTunnelEndpointDstMask = _UsdMplsTunnelProfileTunnelEndpointDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3, 1, 3),
    _UsdMplsTunnelProfileTunnelEndpointDstMask_Type()
)
usdMplsTunnelProfileTunnelEndpointDstMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileTunnelEndpointDstMask.setStatus("current")
_UsdMplsTunnelProfileTunnelEndpointRowStatus_Type = RowStatus
_UsdMplsTunnelProfileTunnelEndpointRowStatus_Object = MibTableColumn
usdMplsTunnelProfileTunnelEndpointRowStatus = _UsdMplsTunnelProfileTunnelEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3, 1, 4),
    _UsdMplsTunnelProfileTunnelEndpointRowStatus_Type()
)
usdMplsTunnelProfileTunnelEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsTunnelProfileTunnelEndpointRowStatus.setStatus("current")
_UsdMplsExplicitPath_ObjectIdentity = ObjectIdentity
usdMplsExplicitPath = _UsdMplsExplicitPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5)
)
_UsdMplsExplicitPathGroup_ObjectIdentity = ObjectIdentity
usdMplsExplicitPathGroup = _UsdMplsExplicitPathGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1)
)
_UsdMplsExplicitPathTable_Object = MibTable
usdMplsExplicitPathTable = _UsdMplsExplicitPathTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    usdMplsExplicitPathTable.setStatus("current")
_UsdMplsExplicitPathEntry_Object = MibTableRow
usdMplsExplicitPathEntry = _UsdMplsExplicitPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 1, 1)
)
usdMplsExplicitPathEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsExplicitPathName"),
)
if mibBuilder.loadTexts:
    usdMplsExplicitPathEntry.setStatus("current")


class _UsdMplsExplicitPathName_Type(DisplayString):
    """Custom type usdMplsExplicitPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsExplicitPathName_Type.__name__ = "DisplayString"
_UsdMplsExplicitPathName_Object = MibTableColumn
usdMplsExplicitPathName = _UsdMplsExplicitPathName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 1, 1, 1),
    _UsdMplsExplicitPathName_Type()
)
usdMplsExplicitPathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsExplicitPathName.setStatus("current")


class _UsdMplsExplicitPathAdminState_Type(Integer32):
    """Custom type usdMplsExplicitPathAdminState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UsdMplsExplicitPathAdminState_Type.__name__ = "Integer32"
_UsdMplsExplicitPathAdminState_Object = MibTableColumn
usdMplsExplicitPathAdminState = _UsdMplsExplicitPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 1, 1, 2),
    _UsdMplsExplicitPathAdminState_Type()
)
usdMplsExplicitPathAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsExplicitPathAdminState.setStatus("current")
_UsdMplsExplicitPathRowStatus_Type = RowStatus
_UsdMplsExplicitPathRowStatus_Object = MibTableColumn
usdMplsExplicitPathRowStatus = _UsdMplsExplicitPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 1, 1, 3),
    _UsdMplsExplicitPathRowStatus_Type()
)
usdMplsExplicitPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsExplicitPathRowStatus.setStatus("current")
_UsdMplsExplicitPathNodeTable_Object = MibTable
usdMplsExplicitPathNodeTable = _UsdMplsExplicitPathNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    usdMplsExplicitPathNodeTable.setStatus("current")
_UsdMplsExplicitPathNodeEntry_Object = MibTableRow
usdMplsExplicitPathNodeEntry = _UsdMplsExplicitPathNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1)
)
usdMplsExplicitPathNodeEntry.setIndexNames(
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsExplicitPathNodeName"),
    (0, "Unisphere-Data-MPLS-MIB", "usdMplsExplicitPathNodeIndexNumber"),
)
if mibBuilder.loadTexts:
    usdMplsExplicitPathNodeEntry.setStatus("current")


class _UsdMplsExplicitPathNodeName_Type(DisplayString):
    """Custom type usdMplsExplicitPathNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_UsdMplsExplicitPathNodeName_Type.__name__ = "DisplayString"
_UsdMplsExplicitPathNodeName_Object = MibTableColumn
usdMplsExplicitPathNodeName = _UsdMplsExplicitPathNodeName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 1),
    _UsdMplsExplicitPathNodeName_Type()
)
usdMplsExplicitPathNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsExplicitPathNodeName.setStatus("current")


class _UsdMplsExplicitPathNodeIndexNumber_Type(Integer32):
    """Custom type usdMplsExplicitPathNodeIndexNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdMplsExplicitPathNodeIndexNumber_Type.__name__ = "Integer32"
_UsdMplsExplicitPathNodeIndexNumber_Object = MibTableColumn
usdMplsExplicitPathNodeIndexNumber = _UsdMplsExplicitPathNodeIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 2),
    _UsdMplsExplicitPathNodeIndexNumber_Type()
)
usdMplsExplicitPathNodeIndexNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdMplsExplicitPathNodeIndexNumber.setStatus("current")


class _UsdMplsExplicitPathNodeLoose_Type(TruthValue):
    """Custom type usdMplsExplicitPathNodeLoose based on TruthValue"""


_UsdMplsExplicitPathNodeLoose_Object = MibTableColumn
usdMplsExplicitPathNodeLoose = _UsdMplsExplicitPathNodeLoose_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 3),
    _UsdMplsExplicitPathNodeLoose_Type()
)
usdMplsExplicitPathNodeLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsExplicitPathNodeLoose.setStatus("current")
_UsdMplsExplicitPathNodeHopAddress_Type = IpAddress
_UsdMplsExplicitPathNodeHopAddress_Object = MibTableColumn
usdMplsExplicitPathNodeHopAddress = _UsdMplsExplicitPathNodeHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 4),
    _UsdMplsExplicitPathNodeHopAddress_Type()
)
usdMplsExplicitPathNodeHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsExplicitPathNodeHopAddress.setStatus("current")


class _UsdMplsExplicitPathNodeHopAddressMask_Type(IpAddress):
    """Custom type usdMplsExplicitPathNodeHopAddressMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_UsdMplsExplicitPathNodeHopAddressMask_Object = MibTableColumn
usdMplsExplicitPathNodeHopAddressMask = _UsdMplsExplicitPathNodeHopAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 5),
    _UsdMplsExplicitPathNodeHopAddressMask_Type()
)
usdMplsExplicitPathNodeHopAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsExplicitPathNodeHopAddressMask.setStatus("current")
_UsdMplsExplicitPathNodeRowStatus_Type = RowStatus
_UsdMplsExplicitPathNodeRowStatus_Object = MibTableColumn
usdMplsExplicitPathNodeRowStatus = _UsdMplsExplicitPathNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 6),
    _UsdMplsExplicitPathNodeRowStatus_Type()
)
usdMplsExplicitPathNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMplsExplicitPathNodeRowStatus.setStatus("current")
_UsdMplsConformance_ObjectIdentity = ObjectIdentity
usdMplsConformance = _UsdMplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2)
)
_UsdMplsCompliances_ObjectIdentity = ObjectIdentity
usdMplsCompliances = _UsdMplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 1)
)
_UsdMplsConfGroups_ObjectIdentity = ObjectIdentity
usdMplsConfGroups = _UsdMplsConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2)
)

# Managed Objects groups

usdMplsLsrGlobalConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 1)
)
usdMplsLsrGlobalConfGroup.setObjects(
      *(("Unisphere-Data-MPLS-MIB", "usdMplsGroupMplsEnable"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupReopTimer"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLabelRangeLow"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLabelRangeHigh"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLspRetryTimesNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLspRetryIntervalNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLspRetryTimes"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLspRetryInterval"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpRetryTimesNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpRetryIntervalNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpRetryTimes"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpRetryInterval"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpSessionRetries"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpSessionRetryTimer"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupTopologyDrivenIpProfileName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupTopologyDrivenLdpEgressIpIntf"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupTopologyDrivenLdpIngressIpIntf"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupTopologyDrivenLdp"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLspLabelDistCtrlMode"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpAdvHostOnly"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLsrState"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupReopNow"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpTargetedHelloSendMode"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpTargetedHelloReceiveMode"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLabelAdverListMode"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpProfileHelloHoldTime"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpProfileCrLdpAdminState"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupLdpProfileRowStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupRsvpProfileRefreshPeriod"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupRsvpProfileCleanupTimeoutFactor"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsGroupRsvpProfileRowStatus"))
)
if mibBuilder.loadTexts:
    usdMplsLsrGlobalConfGroup.setStatus("current")

usdMplsMajorLayerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 2)
)
usdMplsMajorLayerConfGroup.setObjects(
      *(("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorNextIfIndex"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorRowStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorLowerIfIndex"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorAdminStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorLdpAdminStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorLdpProfileName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorLdpVpiStart"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorLdpVpiStop"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorLdpVciStart"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorLdpVciStop"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorRsvpAdminStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorRsvpProfileName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorRsvpVpiStart"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorRsvpVpiStop"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorRsvpVciStart"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorRsvpVciStop"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorLabelSpaceType"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorOpState"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMajorCrLdpAdminState"))
)
if mibBuilder.loadTexts:
    usdMplsMajorLayerConfGroup.setStatus("current")

usdMplsMinorLayerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 3)
)
usdMplsMinorLayerConfGroup.setObjects(
      *(("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorNextIfIndex"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorRowStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorLowerIfIndex"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAdminStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorEndpointAddress"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorEndpointDstMask"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelMetricMode"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAbsoluteTunnelMetric"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorRelativeTunnelMetric"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorLabelDistProto"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAnnounceToOspf"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAnnounceToIsis"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAnnounceToBgp"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorBandwidth"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAffinity"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAffinityMask"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorSetupPriority"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorHoldingPriority"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelRetryTimes"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelRetryInterval"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelRetryTimesNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelRetryIntervalNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorBaseTunnelName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorVpnOuiNumber"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorVpnIndex"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelOpState"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTargetedDynamicTunnel"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorReoptimization"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionProtocol"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionLockdown"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionPathName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionPathId"))
)
if mibBuilder.loadTexts:
    usdMplsMinorLayerConfGroup.setStatus("obsolete")

usdMplsTunnelProfileConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 4)
)
usdMplsTunnelProfileConfGroup.setObjects(
      *(("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAdminStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileBaseTunnelName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileIpProfileName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileLabelDistProto"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAnnounceToOspf"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAnnounceToIsis"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAnnounceToBgp"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileMetricMode"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAbsoluteMetric"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRelativeMetric"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileBandwidth"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAffinity"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAffinityMask"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileSetupPriority"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileHoldingPriority"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRetryTimes"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRetryInterval"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRetryTimesNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRetryIntervalNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileVpnOuiNumber"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileVpnIndex"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRowStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileTargetedDynamicTunnel"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfilePathOptionProtocol"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfilePathOptionLockdown"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfilePathOptionPathName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfilePathOptionPathId"))
)
if mibBuilder.loadTexts:
    usdMplsTunnelProfileConfGroup.setStatus("obsolete")

usdMplsExplicitPathConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 5)
)
usdMplsExplicitPathConfGroup.setObjects(
      *(("Unisphere-Data-MPLS-MIB", "usdMplsExplicitPathAdminState"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsExplicitPathRowStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsExplicitPathNodeLoose"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsExplicitPathNodeHopAddress"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsExplicitPathNodeHopAddressMask"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsExplicitPathNodeRowStatus"))
)
if mibBuilder.loadTexts:
    usdMplsExplicitPathConfGroup.setStatus("current")

usdMplsMinorLayerConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 6)
)
usdMplsMinorLayerConfGroup2.setObjects(
      *(("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorNextIfIndex"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorRowStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorLowerIfIndex"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAdminStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorEndpointAddress"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorEndpointDstMask"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelMetricMode"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAbsoluteTunnelMetric"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorRelativeTunnelMetric"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorLabelDistProto"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAnnounceToOspf"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAnnounceToIsis"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAnnounceToBgp"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorBandwidth"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAffinity"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorAffinityMask"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorSetupPriority"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorHoldingPriority"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelRetryTimes"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelRetryInterval"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelRetryTimesNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelRetryIntervalNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorBaseTunnelName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorVpnOuiNumber"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorVpnIndex"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTunnelOpState"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorTargetedDynamicTunnel"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorReoptimization"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionProtocol"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionLockdown"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionPathName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionPathId"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsIfMinorPathOptionRowStatus"))
)
if mibBuilder.loadTexts:
    usdMplsMinorLayerConfGroup2.setStatus("current")

usdMplsTunnelProfileConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 7)
)
usdMplsTunnelProfileConfGroup2.setObjects(
      *(("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAdminStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileBaseTunnelName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileIpProfileName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileLabelDistProto"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAnnounceToOspf"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAnnounceToIsis"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAnnounceToBgp"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileMetricMode"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAbsoluteMetric"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRelativeMetric"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileBandwidth"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAffinity"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileAffinityMask"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileSetupPriority"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileHoldingPriority"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRetryTimes"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRetryInterval"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRetryTimesNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRetryIntervalNoroute"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileVpnOuiNumber"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileVpnIndex"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileRowStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileTargetedDynamicTunnel"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfilePathOptionProtocol"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfilePathOptionLockdown"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfilePathOptionPathName"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfilePathOptionPathId"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfilePathOptionRowStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileDynamicEndpointRowStatus"),
        ("Unisphere-Data-MPLS-MIB", "usdMplsTunnelProfileTunnelEndpointRowStatus"))
)
if mibBuilder.loadTexts:
    usdMplsTunnelProfileConfGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdMplsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdMplsCompliance.setStatus(
        "obsolete"
    )

usdMplsCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdMplsCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-MPLS-MIB",
    **{"UsdMajorCfgVciRanges": UsdMajorCfgVciRanges,
       "UsdMajorCfgVpiRanges": UsdMajorCfgVpiRanges,
       "UsdMinorCfgBWRanges": UsdMinorCfgBWRanges,
       "UsdMinorCfgHoldingAndSetupPriorityRanges": UsdMinorCfgHoldingAndSetupPriorityRanges,
       "UsdMinorCfgRetryTimesAndNorouteRanges": UsdMinorCfgRetryTimesAndNorouteRanges,
       "UsdMinorCfgRetryIntervalAndNorouteRanges": UsdMinorCfgRetryIntervalAndNorouteRanges,
       "UsdProfileCfgBWRanges": UsdProfileCfgBWRanges,
       "UsdProfileCfgHoldingAndSetupPriorityRanges": UsdProfileCfgHoldingAndSetupPriorityRanges,
       "UsdProfileCfgRetryTimesAndNorouteRanges": UsdProfileCfgRetryTimesAndNorouteRanges,
       "UsdProfileCfgRetryIntervalAndNorouteRanges": UsdProfileCfgRetryIntervalAndNorouteRanges,
       "usdMplsMIB": usdMplsMIB,
       "usdMplsObjects": usdMplsObjects,
       "usdMplsLsrGlobalConfig": usdMplsLsrGlobalConfig,
       "usdMplsGroup": usdMplsGroup,
       "usdMplsGroupMplsEnable": usdMplsGroupMplsEnable,
       "usdMplsGroupReopTimer": usdMplsGroupReopTimer,
       "usdMplsGroupLabelRangeLow": usdMplsGroupLabelRangeLow,
       "usdMplsGroupLabelRangeHigh": usdMplsGroupLabelRangeHigh,
       "usdMplsGroupLspRetryTimesNoroute": usdMplsGroupLspRetryTimesNoroute,
       "usdMplsGroupLspRetryIntervalNoroute": usdMplsGroupLspRetryIntervalNoroute,
       "usdMplsGroupLspRetryTimes": usdMplsGroupLspRetryTimes,
       "usdMplsGroupLspRetryInterval": usdMplsGroupLspRetryInterval,
       "usdMplsGroupLdpRetryTimesNoroute": usdMplsGroupLdpRetryTimesNoroute,
       "usdMplsGroupLdpRetryIntervalNoroute": usdMplsGroupLdpRetryIntervalNoroute,
       "usdMplsGroupLdpRetryTimes": usdMplsGroupLdpRetryTimes,
       "usdMplsGroupLdpRetryInterval": usdMplsGroupLdpRetryInterval,
       "usdMplsGroupLdpSessionRetries": usdMplsGroupLdpSessionRetries,
       "usdMplsGroupLdpSessionRetryTimer": usdMplsGroupLdpSessionRetryTimer,
       "usdMplsGroupTopologyDrivenIpProfileName": usdMplsGroupTopologyDrivenIpProfileName,
       "usdMplsGroupTopologyDrivenLdpEgressIpIntf": usdMplsGroupTopologyDrivenLdpEgressIpIntf,
       "usdMplsGroupTopologyDrivenLdpIngressIpIntf": usdMplsGroupTopologyDrivenLdpIngressIpIntf,
       "usdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly": usdMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly,
       "usdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly": usdMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly,
       "usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType": usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType,
       "usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType": usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType,
       "usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList": usdMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList,
       "usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList": usdMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList,
       "usdMplsGroupTopologyDrivenLdp": usdMplsGroupTopologyDrivenLdp,
       "usdMplsGroupLspLabelDistCtrlMode": usdMplsGroupLspLabelDistCtrlMode,
       "usdMplsGroupLdpAdvHostOnly": usdMplsGroupLdpAdvHostOnly,
       "usdMplsGroupLsrState": usdMplsGroupLsrState,
       "usdMplsGroupReopNow": usdMplsGroupReopNow,
       "usdMplsGroupList": usdMplsGroupList,
       "usdMplsGroupTargetedHelloSendTable": usdMplsGroupTargetedHelloSendTable,
       "usdMplsGroupTargetedHelloSendEntry": usdMplsGroupTargetedHelloSendEntry,
       "usdMplsGroupTargetedHelloSendAddress": usdMplsGroupTargetedHelloSendAddress,
       "usdMplsGroupLdpTargetedHelloSendMode": usdMplsGroupLdpTargetedHelloSendMode,
       "usdMplsGroupTargetedHelloReceiveTable": usdMplsGroupTargetedHelloReceiveTable,
       "usdMplsGroupTargetedHelloReceiveEntry": usdMplsGroupTargetedHelloReceiveEntry,
       "usdMplsGroupTargetedHelloReceiveAddress": usdMplsGroupTargetedHelloReceiveAddress,
       "usdMplsGroupLdpTargetedHelloReceiveMode": usdMplsGroupLdpTargetedHelloReceiveMode,
       "usdMplsGroupLdpLabelAdverRouteListTable": usdMplsGroupLdpLabelAdverRouteListTable,
       "usdMplsGroupLdpLabelAdverRouteListEntry": usdMplsGroupLdpLabelAdverRouteListEntry,
       "usdMplsGroupLdpLabelAdverRouteListName": usdMplsGroupLdpLabelAdverRouteListName,
       "usdMplsGroupLdpLabelAdverNbrListName": usdMplsGroupLdpLabelAdverNbrListName,
       "usdMplsGroupLabelAdverListMode": usdMplsGroupLabelAdverListMode,
       "usdMplsGroupLdpProfileTable": usdMplsGroupLdpProfileTable,
       "usdMplsGroupLdpProfileEntry": usdMplsGroupLdpProfileEntry,
       "usdMplsGroupLdpProfileName": usdMplsGroupLdpProfileName,
       "usdMplsGroupLdpProfileHelloHoldTime": usdMplsGroupLdpProfileHelloHoldTime,
       "usdMplsGroupLdpProfileCrLdpAdminState": usdMplsGroupLdpProfileCrLdpAdminState,
       "usdMplsGroupLdpProfileRowStatus": usdMplsGroupLdpProfileRowStatus,
       "usdMplsGroupRsvpProfileTable": usdMplsGroupRsvpProfileTable,
       "usdMplsGroupRsvpProfileEntry": usdMplsGroupRsvpProfileEntry,
       "usdMplsGroupRsvpProfileName": usdMplsGroupRsvpProfileName,
       "usdMplsGroupRsvpProfileRefreshPeriod": usdMplsGroupRsvpProfileRefreshPeriod,
       "usdMplsGroupRsvpProfileCleanupTimeoutFactor": usdMplsGroupRsvpProfileCleanupTimeoutFactor,
       "usdMplsGroupRsvpProfileRowStatus": usdMplsGroupRsvpProfileRowStatus,
       "usdMplsMajorLayer": usdMplsMajorLayer,
       "usdMplsIfMajorLayer": usdMplsIfMajorLayer,
       "usdMplsIfMajorNextIfIndex": usdMplsIfMajorNextIfIndex,
       "usdMplsIfMajorTable": usdMplsIfMajorTable,
       "usdMplsIfMajorEntry": usdMplsIfMajorEntry,
       "usdMplsIfMajorIndex": usdMplsIfMajorIndex,
       "usdMplsIfMajorRowStatus": usdMplsIfMajorRowStatus,
       "usdMplsIfMajorLowerIfIndex": usdMplsIfMajorLowerIfIndex,
       "usdMplsIfMajorAdminStatus": usdMplsIfMajorAdminStatus,
       "usdMplsIfMajorLdpAdminStatus": usdMplsIfMajorLdpAdminStatus,
       "usdMplsIfMajorLdpProfileName": usdMplsIfMajorLdpProfileName,
       "usdMplsIfMajorLdpVpiStart": usdMplsIfMajorLdpVpiStart,
       "usdMplsIfMajorLdpVpiStop": usdMplsIfMajorLdpVpiStop,
       "usdMplsIfMajorLdpVciStart": usdMplsIfMajorLdpVciStart,
       "usdMplsIfMajorLdpVciStop": usdMplsIfMajorLdpVciStop,
       "usdMplsIfMajorRsvpAdminStatus": usdMplsIfMajorRsvpAdminStatus,
       "usdMplsIfMajorRsvpProfileName": usdMplsIfMajorRsvpProfileName,
       "usdMplsIfMajorRsvpVpiStart": usdMplsIfMajorRsvpVpiStart,
       "usdMplsIfMajorRsvpVpiStop": usdMplsIfMajorRsvpVpiStop,
       "usdMplsIfMajorRsvpVciStart": usdMplsIfMajorRsvpVciStart,
       "usdMplsIfMajorRsvpVciStop": usdMplsIfMajorRsvpVciStop,
       "usdMplsIfMajorLabelSpaceType": usdMplsIfMajorLabelSpaceType,
       "usdMplsIfMajorOpState": usdMplsIfMajorOpState,
       "usdMplsIfMajorCrLdpAdminState": usdMplsIfMajorCrLdpAdminState,
       "usdMplsMinorLayer": usdMplsMinorLayer,
       "usdMplsIfMinorLayer": usdMplsIfMinorLayer,
       "usdMplsIfMinorNextIfIndex": usdMplsIfMinorNextIfIndex,
       "usdMplsIfMinorTable": usdMplsIfMinorTable,
       "usdMplsIfMinorEntry": usdMplsIfMinorEntry,
       "usdMplsIfMinorIndex": usdMplsIfMinorIndex,
       "usdMplsIfMinorRowStatus": usdMplsIfMinorRowStatus,
       "usdMplsIfMinorLowerIfIndex": usdMplsIfMinorLowerIfIndex,
       "usdMplsIfMinorAdminStatus": usdMplsIfMinorAdminStatus,
       "usdMplsIfMinorEndpointAddress": usdMplsIfMinorEndpointAddress,
       "usdMplsIfMinorEndpointDstMask": usdMplsIfMinorEndpointDstMask,
       "usdMplsIfMinorTunnelMetricMode": usdMplsIfMinorTunnelMetricMode,
       "usdMplsIfMinorAbsoluteTunnelMetric": usdMplsIfMinorAbsoluteTunnelMetric,
       "usdMplsIfMinorRelativeTunnelMetric": usdMplsIfMinorRelativeTunnelMetric,
       "usdMplsIfMinorLabelDistProto": usdMplsIfMinorLabelDistProto,
       "usdMplsIfMinorAnnounceToOspf": usdMplsIfMinorAnnounceToOspf,
       "usdMplsIfMinorAnnounceToIsis": usdMplsIfMinorAnnounceToIsis,
       "usdMplsIfMinorAnnounceToBgp": usdMplsIfMinorAnnounceToBgp,
       "usdMplsIfMinorBandwidth": usdMplsIfMinorBandwidth,
       "usdMplsIfMinorAffinity": usdMplsIfMinorAffinity,
       "usdMplsIfMinorAffinityMask": usdMplsIfMinorAffinityMask,
       "usdMplsIfMinorSetupPriority": usdMplsIfMinorSetupPriority,
       "usdMplsIfMinorHoldingPriority": usdMplsIfMinorHoldingPriority,
       "usdMplsIfMinorTunnelName": usdMplsIfMinorTunnelName,
       "usdMplsIfMinorTunnelRetryTimes": usdMplsIfMinorTunnelRetryTimes,
       "usdMplsIfMinorTunnelRetryInterval": usdMplsIfMinorTunnelRetryInterval,
       "usdMplsIfMinorTunnelRetryTimesNoroute": usdMplsIfMinorTunnelRetryTimesNoroute,
       "usdMplsIfMinorTunnelRetryIntervalNoroute": usdMplsIfMinorTunnelRetryIntervalNoroute,
       "usdMplsIfMinorBaseTunnelName": usdMplsIfMinorBaseTunnelName,
       "usdMplsIfMinorVpnOuiNumber": usdMplsIfMinorVpnOuiNumber,
       "usdMplsIfMinorVpnIndex": usdMplsIfMinorVpnIndex,
       "usdMplsIfMinorTunnelOpState": usdMplsIfMinorTunnelOpState,
       "usdMplsIfMinorTargetedDynamicTunnel": usdMplsIfMinorTargetedDynamicTunnel,
       "usdMplsIfMinorReoptimization": usdMplsIfMinorReoptimization,
       "usdMplsMinorLayerList": usdMplsMinorLayerList,
       "usdMplsIfMinorPathOptionTable": usdMplsIfMinorPathOptionTable,
       "usdMplsIfMinorPathOptionEntry": usdMplsIfMinorPathOptionEntry,
       "usdMplsIfMinorPathOptionIndex": usdMplsIfMinorPathOptionIndex,
       "usdMplsIfMinorPathOptionNumber": usdMplsIfMinorPathOptionNumber,
       "usdMplsIfMinorPathOptionProtocol": usdMplsIfMinorPathOptionProtocol,
       "usdMplsIfMinorPathOptionLockdown": usdMplsIfMinorPathOptionLockdown,
       "usdMplsIfMinorPathOptionPathName": usdMplsIfMinorPathOptionPathName,
       "usdMplsIfMinorPathOptionPathId": usdMplsIfMinorPathOptionPathId,
       "usdMplsIfMinorPathOptionRowStatus": usdMplsIfMinorPathOptionRowStatus,
       "usdMplsTunnelProfile": usdMplsTunnelProfile,
       "usdMplsTunnelProfileGroup": usdMplsTunnelProfileGroup,
       "usdMplsTunnelProfileTable": usdMplsTunnelProfileTable,
       "usdMplsTunnelProfileEntry": usdMplsTunnelProfileEntry,
       "usdMplsTunnelProfileName": usdMplsTunnelProfileName,
       "usdMplsTunnelProfileAdminStatus": usdMplsTunnelProfileAdminStatus,
       "usdMplsTunnelProfileBaseTunnelName": usdMplsTunnelProfileBaseTunnelName,
       "usdMplsTunnelProfileIpProfileName": usdMplsTunnelProfileIpProfileName,
       "usdMplsTunnelProfileLabelDistProto": usdMplsTunnelProfileLabelDistProto,
       "usdMplsTunnelProfileAnnounceToOspf": usdMplsTunnelProfileAnnounceToOspf,
       "usdMplsTunnelProfileAnnounceToIsis": usdMplsTunnelProfileAnnounceToIsis,
       "usdMplsTunnelProfileAnnounceToBgp": usdMplsTunnelProfileAnnounceToBgp,
       "usdMplsTunnelProfileMetricMode": usdMplsTunnelProfileMetricMode,
       "usdMplsTunnelProfileAbsoluteMetric": usdMplsTunnelProfileAbsoluteMetric,
       "usdMplsTunnelProfileRelativeMetric": usdMplsTunnelProfileRelativeMetric,
       "usdMplsTunnelProfileBandwidth": usdMplsTunnelProfileBandwidth,
       "usdMplsTunnelProfileAffinity": usdMplsTunnelProfileAffinity,
       "usdMplsTunnelProfileAffinityMask": usdMplsTunnelProfileAffinityMask,
       "usdMplsTunnelProfileSetupPriority": usdMplsTunnelProfileSetupPriority,
       "usdMplsTunnelProfileHoldingPriority": usdMplsTunnelProfileHoldingPriority,
       "usdMplsTunnelProfileRetryTimes": usdMplsTunnelProfileRetryTimes,
       "usdMplsTunnelProfileRetryInterval": usdMplsTunnelProfileRetryInterval,
       "usdMplsTunnelProfileRetryTimesNoroute": usdMplsTunnelProfileRetryTimesNoroute,
       "usdMplsTunnelProfileRetryIntervalNoroute": usdMplsTunnelProfileRetryIntervalNoroute,
       "usdMplsTunnelProfileVpnOuiNumber": usdMplsTunnelProfileVpnOuiNumber,
       "usdMplsTunnelProfileVpnIndex": usdMplsTunnelProfileVpnIndex,
       "usdMplsTunnelProfileRowStatus": usdMplsTunnelProfileRowStatus,
       "usdMplsTunnelProfileTargetedDynamicTunnel": usdMplsTunnelProfileTargetedDynamicTunnel,
       "usdMplsTunnelProfileList": usdMplsTunnelProfileList,
       "usdMplsTunnelProfilePathOptionTable": usdMplsTunnelProfilePathOptionTable,
       "usdMplsTunnelProfilePathOptionEntry": usdMplsTunnelProfilePathOptionEntry,
       "usdMplsTunnelProfileNamePathOption": usdMplsTunnelProfileNamePathOption,
       "usdMplsTunnelProfilePathOptionNumber": usdMplsTunnelProfilePathOptionNumber,
       "usdMplsTunnelProfilePathOptionProtocol": usdMplsTunnelProfilePathOptionProtocol,
       "usdMplsTunnelProfilePathOptionLockdown": usdMplsTunnelProfilePathOptionLockdown,
       "usdMplsTunnelProfilePathOptionPathName": usdMplsTunnelProfilePathOptionPathName,
       "usdMplsTunnelProfilePathOptionPathId": usdMplsTunnelProfilePathOptionPathId,
       "usdMplsTunnelProfilePathOptionRowStatus": usdMplsTunnelProfilePathOptionRowStatus,
       "usdMplsTunnelProfileDynamicEndpointTable": usdMplsTunnelProfileDynamicEndpointTable,
       "usdMplsTunnelProfileDynamicEndpointEntry": usdMplsTunnelProfileDynamicEndpointEntry,
       "usdMplsTunnelProfileNameDynamicEndpoint": usdMplsTunnelProfileNameDynamicEndpoint,
       "usdMplsTunnelProfileDynamicEndpointType": usdMplsTunnelProfileDynamicEndpointType,
       "usdMplsTunnelProfileDynamicEndpointPolicyListType": usdMplsTunnelProfileDynamicEndpointPolicyListType,
       "usdMplsTunnelProfileDynamicEndpointListName": usdMplsTunnelProfileDynamicEndpointListName,
       "usdMplsTunnelProfileDynamicEndpointRowStatus": usdMplsTunnelProfileDynamicEndpointRowStatus,
       "usdMplsTunnelProfileTunnelEndpointTable": usdMplsTunnelProfileTunnelEndpointTable,
       "usdMplsTunnelProfileTunnelEndpointEntry": usdMplsTunnelProfileTunnelEndpointEntry,
       "usdMplsTunnelProfileNameTunnelEndpoint": usdMplsTunnelProfileNameTunnelEndpoint,
       "usdMplsTunnelProfileTunnelEndpointAddress": usdMplsTunnelProfileTunnelEndpointAddress,
       "usdMplsTunnelProfileTunnelEndpointDstMask": usdMplsTunnelProfileTunnelEndpointDstMask,
       "usdMplsTunnelProfileTunnelEndpointRowStatus": usdMplsTunnelProfileTunnelEndpointRowStatus,
       "usdMplsExplicitPath": usdMplsExplicitPath,
       "usdMplsExplicitPathGroup": usdMplsExplicitPathGroup,
       "usdMplsExplicitPathTable": usdMplsExplicitPathTable,
       "usdMplsExplicitPathEntry": usdMplsExplicitPathEntry,
       "usdMplsExplicitPathName": usdMplsExplicitPathName,
       "usdMplsExplicitPathAdminState": usdMplsExplicitPathAdminState,
       "usdMplsExplicitPathRowStatus": usdMplsExplicitPathRowStatus,
       "usdMplsExplicitPathNodeTable": usdMplsExplicitPathNodeTable,
       "usdMplsExplicitPathNodeEntry": usdMplsExplicitPathNodeEntry,
       "usdMplsExplicitPathNodeName": usdMplsExplicitPathNodeName,
       "usdMplsExplicitPathNodeIndexNumber": usdMplsExplicitPathNodeIndexNumber,
       "usdMplsExplicitPathNodeLoose": usdMplsExplicitPathNodeLoose,
       "usdMplsExplicitPathNodeHopAddress": usdMplsExplicitPathNodeHopAddress,
       "usdMplsExplicitPathNodeHopAddressMask": usdMplsExplicitPathNodeHopAddressMask,
       "usdMplsExplicitPathNodeRowStatus": usdMplsExplicitPathNodeRowStatus,
       "usdMplsConformance": usdMplsConformance,
       "usdMplsCompliances": usdMplsCompliances,
       "usdMplsCompliance": usdMplsCompliance,
       "usdMplsCompliance2": usdMplsCompliance2,
       "usdMplsConfGroups": usdMplsConfGroups,
       "usdMplsLsrGlobalConfGroup": usdMplsLsrGlobalConfGroup,
       "usdMplsMajorLayerConfGroup": usdMplsMajorLayerConfGroup,
       "usdMplsMinorLayerConfGroup": usdMplsMinorLayerConfGroup,
       "usdMplsTunnelProfileConfGroup": usdMplsTunnelProfileConfGroup,
       "usdMplsExplicitPathConfGroup": usdMplsExplicitPathConfGroup,
       "usdMplsMinorLayerConfGroup2": usdMplsMinorLayerConfGroup2,
       "usdMplsTunnelProfileConfGroup2": usdMplsTunnelProfileConfGroup2}
)
