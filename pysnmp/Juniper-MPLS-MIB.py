# SNMP MIB module (Juniper-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:47 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex")

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

juniMplsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54)
)
juniMplsMIB.setRevisions(
        ("2004-09-15 05:43",
         "2004-04-22 01:23",
         "2004-04-15 13:31",
         "2003-09-29 14:17",
         "2003-01-24 18:23",
         "2002-11-04 15:35",
         "2002-04-03 20:44")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniMajorCfgVciRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 65535),
    )



class JuniMajorCfgVpiRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class JuniMinorCfgBWRanges(Unsigned32, TextualConvention):
    status = "current"


class JuniMinorCfgHoldingAndSetupPriorityRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class JuniMinorCfgRetryTimesAndNorouteRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class JuniMinorCfgRetryIntervalAndNorouteRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )



class JuniProfileCfgBWRanges(Unsigned32, TextualConvention):
    status = "current"


class JuniProfileCfgHoldingAndSetupPriorityRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class JuniProfileCfgRetryTimesAndNorouteRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class JuniProfileCfgRetryIntervalAndNorouteRanges(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )



# MIB Managed Objects in the order of their OIDs

_JuniMplsObjects_ObjectIdentity = ObjectIdentity
juniMplsObjects = _JuniMplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1)
)
_JuniMplsLsrGlobalConfig_ObjectIdentity = ObjectIdentity
juniMplsLsrGlobalConfig = _JuniMplsLsrGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1)
)
_JuniMplsGroup_ObjectIdentity = ObjectIdentity
juniMplsGroup = _JuniMplsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1)
)


class _JuniMplsGroupMplsEnable_Type(Integer32):
    """Custom type juniMplsGroupMplsEnable based on Integer32"""
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


_JuniMplsGroupMplsEnable_Type.__name__ = "Integer32"
_JuniMplsGroupMplsEnable_Object = MibScalar
juniMplsGroupMplsEnable = _JuniMplsGroupMplsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 1),
    _JuniMplsGroupMplsEnable_Type()
)
juniMplsGroupMplsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupMplsEnable.setStatus("current")


class _JuniMplsGroupReopTimer_Type(Integer32):
    """Custom type juniMplsGroupReopTimer based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_JuniMplsGroupReopTimer_Type.__name__ = "Integer32"
_JuniMplsGroupReopTimer_Object = MibScalar
juniMplsGroupReopTimer = _JuniMplsGroupReopTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 2),
    _JuniMplsGroupReopTimer_Type()
)
juniMplsGroupReopTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupReopTimer.setStatus("current")
if mibBuilder.loadTexts:
    juniMplsGroupReopTimer.setUnits("seconds")


class _JuniMplsGroupLabelRangeLow_Type(Integer32):
    """Custom type juniMplsGroupLabelRangeLow based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048576),
    )


_JuniMplsGroupLabelRangeLow_Type.__name__ = "Integer32"
_JuniMplsGroupLabelRangeLow_Object = MibScalar
juniMplsGroupLabelRangeLow = _JuniMplsGroupLabelRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 3),
    _JuniMplsGroupLabelRangeLow_Type()
)
juniMplsGroupLabelRangeLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLabelRangeLow.setStatus("current")


class _JuniMplsGroupLabelRangeHigh_Type(Integer32):
    """Custom type juniMplsGroupLabelRangeHigh based on Integer32"""
    defaultValue = 1048575

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048576),
    )


_JuniMplsGroupLabelRangeHigh_Type.__name__ = "Integer32"
_JuniMplsGroupLabelRangeHigh_Object = MibScalar
juniMplsGroupLabelRangeHigh = _JuniMplsGroupLabelRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 4),
    _JuniMplsGroupLabelRangeHigh_Type()
)
juniMplsGroupLabelRangeHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLabelRangeHigh.setStatus("current")


class _JuniMplsGroupLspRetryTimesNoroute_Type(Integer32):
    """Custom type juniMplsGroupLspRetryTimesNoroute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniMplsGroupLspRetryTimesNoroute_Type.__name__ = "Integer32"
_JuniMplsGroupLspRetryTimesNoroute_Object = MibScalar
juniMplsGroupLspRetryTimesNoroute = _JuniMplsGroupLspRetryTimesNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 5),
    _JuniMplsGroupLspRetryTimesNoroute_Type()
)
juniMplsGroupLspRetryTimesNoroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLspRetryTimesNoroute.setStatus("current")


class _JuniMplsGroupLspRetryIntervalNoroute_Type(Integer32):
    """Custom type juniMplsGroupLspRetryIntervalNoroute based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_JuniMplsGroupLspRetryIntervalNoroute_Type.__name__ = "Integer32"
_JuniMplsGroupLspRetryIntervalNoroute_Object = MibScalar
juniMplsGroupLspRetryIntervalNoroute = _JuniMplsGroupLspRetryIntervalNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 6),
    _JuniMplsGroupLspRetryIntervalNoroute_Type()
)
juniMplsGroupLspRetryIntervalNoroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLspRetryIntervalNoroute.setStatus("current")
if mibBuilder.loadTexts:
    juniMplsGroupLspRetryIntervalNoroute.setUnits("seconds")


class _JuniMplsGroupLspRetryTimes_Type(Integer32):
    """Custom type juniMplsGroupLspRetryTimes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniMplsGroupLspRetryTimes_Type.__name__ = "Integer32"
_JuniMplsGroupLspRetryTimes_Object = MibScalar
juniMplsGroupLspRetryTimes = _JuniMplsGroupLspRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 7),
    _JuniMplsGroupLspRetryTimes_Type()
)
juniMplsGroupLspRetryTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLspRetryTimes.setStatus("current")


class _JuniMplsGroupLspRetryInterval_Type(Integer32):
    """Custom type juniMplsGroupLspRetryInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_JuniMplsGroupLspRetryInterval_Type.__name__ = "Integer32"
_JuniMplsGroupLspRetryInterval_Object = MibScalar
juniMplsGroupLspRetryInterval = _JuniMplsGroupLspRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 8),
    _JuniMplsGroupLspRetryInterval_Type()
)
juniMplsGroupLspRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLspRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniMplsGroupLspRetryInterval.setUnits("seconds")


class _JuniMplsGroupLdpRetryTimesNoroute_Type(Integer32):
    """Custom type juniMplsGroupLdpRetryTimesNoroute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniMplsGroupLdpRetryTimesNoroute_Type.__name__ = "Integer32"
_JuniMplsGroupLdpRetryTimesNoroute_Object = MibScalar
juniMplsGroupLdpRetryTimesNoroute = _JuniMplsGroupLdpRetryTimesNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 9),
    _JuniMplsGroupLdpRetryTimesNoroute_Type()
)
juniMplsGroupLdpRetryTimesNoroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLdpRetryTimesNoroute.setStatus("obsolete")


class _JuniMplsGroupLdpRetryIntervalNoroute_Type(Integer32):
    """Custom type juniMplsGroupLdpRetryIntervalNoroute based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_JuniMplsGroupLdpRetryIntervalNoroute_Type.__name__ = "Integer32"
_JuniMplsGroupLdpRetryIntervalNoroute_Object = MibScalar
juniMplsGroupLdpRetryIntervalNoroute = _JuniMplsGroupLdpRetryIntervalNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 10),
    _JuniMplsGroupLdpRetryIntervalNoroute_Type()
)
juniMplsGroupLdpRetryIntervalNoroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLdpRetryIntervalNoroute.setStatus("obsolete")
if mibBuilder.loadTexts:
    juniMplsGroupLdpRetryIntervalNoroute.setUnits("seconds")


class _JuniMplsGroupLdpRetryTimes_Type(Integer32):
    """Custom type juniMplsGroupLdpRetryTimes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniMplsGroupLdpRetryTimes_Type.__name__ = "Integer32"
_JuniMplsGroupLdpRetryTimes_Object = MibScalar
juniMplsGroupLdpRetryTimes = _JuniMplsGroupLdpRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 11),
    _JuniMplsGroupLdpRetryTimes_Type()
)
juniMplsGroupLdpRetryTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLdpRetryTimes.setStatus("obsolete")


class _JuniMplsGroupLdpRetryInterval_Type(Integer32):
    """Custom type juniMplsGroupLdpRetryInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JuniMplsGroupLdpRetryInterval_Type.__name__ = "Integer32"
_JuniMplsGroupLdpRetryInterval_Object = MibScalar
juniMplsGroupLdpRetryInterval = _JuniMplsGroupLdpRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 12),
    _JuniMplsGroupLdpRetryInterval_Type()
)
juniMplsGroupLdpRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLdpRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniMplsGroupLdpRetryInterval.setUnits("seconds")


class _JuniMplsGroupLdpSessionRetries_Type(Integer32):
    """Custom type juniMplsGroupLdpSessionRetries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniMplsGroupLdpSessionRetries_Type.__name__ = "Integer32"
_JuniMplsGroupLdpSessionRetries_Object = MibScalar
juniMplsGroupLdpSessionRetries = _JuniMplsGroupLdpSessionRetries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 13),
    _JuniMplsGroupLdpSessionRetries_Type()
)
juniMplsGroupLdpSessionRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLdpSessionRetries.setStatus("current")


class _JuniMplsGroupLdpSessionRetryTimer_Type(Integer32):
    """Custom type juniMplsGroupLdpSessionRetryTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JuniMplsGroupLdpSessionRetryTimer_Type.__name__ = "Integer32"
_JuniMplsGroupLdpSessionRetryTimer_Object = MibScalar
juniMplsGroupLdpSessionRetryTimer = _JuniMplsGroupLdpSessionRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 14),
    _JuniMplsGroupLdpSessionRetryTimer_Type()
)
juniMplsGroupLdpSessionRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLdpSessionRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    juniMplsGroupLdpSessionRetryTimer.setUnits("seconds")
_JuniMplsGroupTopologyDrivenIpProfileName_Type = DisplayString
_JuniMplsGroupTopologyDrivenIpProfileName_Object = MibScalar
juniMplsGroupTopologyDrivenIpProfileName = _JuniMplsGroupTopologyDrivenIpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 15),
    _JuniMplsGroupTopologyDrivenIpProfileName_Type()
)
juniMplsGroupTopologyDrivenIpProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupTopologyDrivenIpProfileName.setStatus("current")


class _JuniMplsGroupTopologyDrivenLdpEgressIpIntf_Type(TruthValue):
    """Custom type juniMplsGroupTopologyDrivenLdpEgressIpIntf based on TruthValue"""


_JuniMplsGroupTopologyDrivenLdpEgressIpIntf_Object = MibScalar
juniMplsGroupTopologyDrivenLdpEgressIpIntf = _JuniMplsGroupTopologyDrivenLdpEgressIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 16),
    _JuniMplsGroupTopologyDrivenLdpEgressIpIntf_Type()
)
juniMplsGroupTopologyDrivenLdpEgressIpIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupTopologyDrivenLdpEgressIpIntf.setStatus("current")


class _JuniMplsGroupTopologyDrivenLdpIngressIpIntf_Type(TruthValue):
    """Custom type juniMplsGroupTopologyDrivenLdpIngressIpIntf based on TruthValue"""


_JuniMplsGroupTopologyDrivenLdpIngressIpIntf_Object = MibScalar
juniMplsGroupTopologyDrivenLdpIngressIpIntf = _JuniMplsGroupTopologyDrivenLdpIngressIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 17),
    _JuniMplsGroupTopologyDrivenLdpIngressIpIntf_Type()
)
juniMplsGroupTopologyDrivenLdpIngressIpIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupTopologyDrivenLdpIngressIpIntf.setStatus("current")


class _JuniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly_Type(TruthValue):
    """Custom type juniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly based on TruthValue"""


_JuniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly_Object = MibScalar
juniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly = _JuniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 18),
    _JuniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly_Type()
)
juniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly.setStatus("current")


class _JuniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly_Type(TruthValue):
    """Custom type juniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly based on TruthValue"""


_JuniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly_Object = MibScalar
juniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly = _JuniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 19),
    _JuniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly_Type()
)
juniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly.setStatus("current")


class _JuniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType_Type(Integer32):
    """Custom type juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType based on Integer32"""
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


_JuniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType_Type.__name__ = "Integer32"
_JuniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType_Object = MibScalar
juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType = _JuniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 20),
    _JuniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType_Type()
)
juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType.setStatus("current")


class _JuniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType_Type(Integer32):
    """Custom type juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType based on Integer32"""
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


_JuniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType_Type.__name__ = "Integer32"
_JuniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType_Object = MibScalar
juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType = _JuniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 21),
    _JuniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType_Type()
)
juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType.setStatus("current")
_JuniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList_Type = DisplayString
_JuniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList_Object = MibScalar
juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList = _JuniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 22),
    _JuniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList_Type()
)
juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList.setStatus("current")
_JuniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList_Type = DisplayString
_JuniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList_Object = MibScalar
juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList = _JuniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 23),
    _JuniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList_Type()
)
juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList.setStatus("current")


class _JuniMplsGroupTopologyDrivenLdp_Type(Integer32):
    """Custom type juniMplsGroupTopologyDrivenLdp based on Integer32"""
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


_JuniMplsGroupTopologyDrivenLdp_Type.__name__ = "Integer32"
_JuniMplsGroupTopologyDrivenLdp_Object = MibScalar
juniMplsGroupTopologyDrivenLdp = _JuniMplsGroupTopologyDrivenLdp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 24),
    _JuniMplsGroupTopologyDrivenLdp_Type()
)
juniMplsGroupTopologyDrivenLdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupTopologyDrivenLdp.setStatus("current")


class _JuniMplsGroupLspLabelDistCtrlMode_Type(Integer32):
    """Custom type juniMplsGroupLspLabelDistCtrlMode based on Integer32"""
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


_JuniMplsGroupLspLabelDistCtrlMode_Type.__name__ = "Integer32"
_JuniMplsGroupLspLabelDistCtrlMode_Object = MibScalar
juniMplsGroupLspLabelDistCtrlMode = _JuniMplsGroupLspLabelDistCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 25),
    _JuniMplsGroupLspLabelDistCtrlMode_Type()
)
juniMplsGroupLspLabelDistCtrlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMplsGroupLspLabelDistCtrlMode.setStatus("current")


class _JuniMplsGroupLdpAdvHostOnly_Type(TruthValue):
    """Custom type juniMplsGroupLdpAdvHostOnly based on TruthValue"""


_JuniMplsGroupLdpAdvHostOnly_Object = MibScalar
juniMplsGroupLdpAdvHostOnly = _JuniMplsGroupLdpAdvHostOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 26),
    _JuniMplsGroupLdpAdvHostOnly_Type()
)
juniMplsGroupLdpAdvHostOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupLdpAdvHostOnly.setStatus("current")
_JuniMplsGroupLsrState_Type = DisplayString
_JuniMplsGroupLsrState_Object = MibScalar
juniMplsGroupLsrState = _JuniMplsGroupLsrState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 27),
    _JuniMplsGroupLsrState_Type()
)
juniMplsGroupLsrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMplsGroupLsrState.setStatus("current")


class _JuniMplsGroupReopNow_Type(TruthValue):
    """Custom type juniMplsGroupReopNow based on TruthValue"""


_JuniMplsGroupReopNow_Object = MibScalar
juniMplsGroupReopNow = _JuniMplsGroupReopNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 28),
    _JuniMplsGroupReopNow_Type()
)
juniMplsGroupReopNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupReopNow.setStatus("current")


class _JuniMplsGroupIpTtlPropagate_Type(Integer32):
    """Custom type juniMplsGroupIpTtlPropagate based on Integer32"""
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
        *(("hideForwarded", 2),
          ("hideForwardedAndLocal", 1),
          ("hideLocal", 3),
          ("none", 0))
    )


_JuniMplsGroupIpTtlPropagate_Type.__name__ = "Integer32"
_JuniMplsGroupIpTtlPropagate_Object = MibScalar
juniMplsGroupIpTtlPropagate = _JuniMplsGroupIpTtlPropagate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 1, 29),
    _JuniMplsGroupIpTtlPropagate_Type()
)
juniMplsGroupIpTtlPropagate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniMplsGroupIpTtlPropagate.setStatus("current")
_JuniMplsGroupList_ObjectIdentity = ObjectIdentity
juniMplsGroupList = _JuniMplsGroupList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2)
)
_JuniMplsGroupTargetedHelloSendTable_Object = MibTable
juniMplsGroupTargetedHelloSendTable = _JuniMplsGroupTargetedHelloSendTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniMplsGroupTargetedHelloSendTable.setStatus("current")
_JuniMplsGroupTargetedHelloSendEntry_Object = MibTableRow
juniMplsGroupTargetedHelloSendEntry = _JuniMplsGroupTargetedHelloSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 1, 1)
)
juniMplsGroupTargetedHelloSendEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsGroupTargetedHelloSendAddress"),
)
if mibBuilder.loadTexts:
    juniMplsGroupTargetedHelloSendEntry.setStatus("current")
_JuniMplsGroupTargetedHelloSendAddress_Type = IpAddress
_JuniMplsGroupTargetedHelloSendAddress_Object = MibTableColumn
juniMplsGroupTargetedHelloSendAddress = _JuniMplsGroupTargetedHelloSendAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 1, 1, 1),
    _JuniMplsGroupTargetedHelloSendAddress_Type()
)
juniMplsGroupTargetedHelloSendAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsGroupTargetedHelloSendAddress.setStatus("current")


class _JuniMplsGroupLdpTargetedHelloSendMode_Type(Integer32):
    """Custom type juniMplsGroupLdpTargetedHelloSendMode based on Integer32"""
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


_JuniMplsGroupLdpTargetedHelloSendMode_Type.__name__ = "Integer32"
_JuniMplsGroupLdpTargetedHelloSendMode_Object = MibTableColumn
juniMplsGroupLdpTargetedHelloSendMode = _JuniMplsGroupLdpTargetedHelloSendMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 1, 1, 2),
    _JuniMplsGroupLdpTargetedHelloSendMode_Type()
)
juniMplsGroupLdpTargetedHelloSendMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsGroupLdpTargetedHelloSendMode.setStatus("current")
_JuniMplsGroupTargetedHelloReceiveTable_Object = MibTable
juniMplsGroupTargetedHelloReceiveTable = _JuniMplsGroupTargetedHelloReceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniMplsGroupTargetedHelloReceiveTable.setStatus("current")
_JuniMplsGroupTargetedHelloReceiveEntry_Object = MibTableRow
juniMplsGroupTargetedHelloReceiveEntry = _JuniMplsGroupTargetedHelloReceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 2, 1)
)
juniMplsGroupTargetedHelloReceiveEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsGroupTargetedHelloReceiveAddress"),
)
if mibBuilder.loadTexts:
    juniMplsGroupTargetedHelloReceiveEntry.setStatus("current")
_JuniMplsGroupTargetedHelloReceiveAddress_Type = IpAddress
_JuniMplsGroupTargetedHelloReceiveAddress_Object = MibTableColumn
juniMplsGroupTargetedHelloReceiveAddress = _JuniMplsGroupTargetedHelloReceiveAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 2, 1, 1),
    _JuniMplsGroupTargetedHelloReceiveAddress_Type()
)
juniMplsGroupTargetedHelloReceiveAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsGroupTargetedHelloReceiveAddress.setStatus("current")


class _JuniMplsGroupLdpTargetedHelloReceiveMode_Type(Integer32):
    """Custom type juniMplsGroupLdpTargetedHelloReceiveMode based on Integer32"""
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


_JuniMplsGroupLdpTargetedHelloReceiveMode_Type.__name__ = "Integer32"
_JuniMplsGroupLdpTargetedHelloReceiveMode_Object = MibTableColumn
juniMplsGroupLdpTargetedHelloReceiveMode = _JuniMplsGroupLdpTargetedHelloReceiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 2, 1, 2),
    _JuniMplsGroupLdpTargetedHelloReceiveMode_Type()
)
juniMplsGroupLdpTargetedHelloReceiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsGroupLdpTargetedHelloReceiveMode.setStatus("current")
_JuniMplsGroupLdpLabelAdverRouteListTable_Object = MibTable
juniMplsGroupLdpLabelAdverRouteListTable = _JuniMplsGroupLdpLabelAdverRouteListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    juniMplsGroupLdpLabelAdverRouteListTable.setStatus("current")
_JuniMplsGroupLdpLabelAdverRouteListEntry_Object = MibTableRow
juniMplsGroupLdpLabelAdverRouteListEntry = _JuniMplsGroupLdpLabelAdverRouteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 3, 1)
)
juniMplsGroupLdpLabelAdverRouteListEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsGroupLdpLabelAdverRouteListName"),
    (0, "Juniper-MPLS-MIB", "juniMplsGroupLdpLabelAdverNbrListName"),
)
if mibBuilder.loadTexts:
    juniMplsGroupLdpLabelAdverRouteListEntry.setStatus("current")


class _JuniMplsGroupLdpLabelAdverRouteListName_Type(DisplayString):
    """Custom type juniMplsGroupLdpLabelAdverRouteListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniMplsGroupLdpLabelAdverRouteListName_Type.__name__ = "DisplayString"
_JuniMplsGroupLdpLabelAdverRouteListName_Object = MibTableColumn
juniMplsGroupLdpLabelAdverRouteListName = _JuniMplsGroupLdpLabelAdverRouteListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 3, 1, 1),
    _JuniMplsGroupLdpLabelAdverRouteListName_Type()
)
juniMplsGroupLdpLabelAdverRouteListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsGroupLdpLabelAdverRouteListName.setStatus("current")


class _JuniMplsGroupLdpLabelAdverNbrListName_Type(DisplayString):
    """Custom type juniMplsGroupLdpLabelAdverNbrListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniMplsGroupLdpLabelAdverNbrListName_Type.__name__ = "DisplayString"
_JuniMplsGroupLdpLabelAdverNbrListName_Object = MibTableColumn
juniMplsGroupLdpLabelAdverNbrListName = _JuniMplsGroupLdpLabelAdverNbrListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 3, 1, 2),
    _JuniMplsGroupLdpLabelAdverNbrListName_Type()
)
juniMplsGroupLdpLabelAdverNbrListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsGroupLdpLabelAdverNbrListName.setStatus("current")


class _JuniMplsGroupLabelAdverListMode_Type(Integer32):
    """Custom type juniMplsGroupLabelAdverListMode based on Integer32"""
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


_JuniMplsGroupLabelAdverListMode_Type.__name__ = "Integer32"
_JuniMplsGroupLabelAdverListMode_Object = MibTableColumn
juniMplsGroupLabelAdverListMode = _JuniMplsGroupLabelAdverListMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 3, 1, 3),
    _JuniMplsGroupLabelAdverListMode_Type()
)
juniMplsGroupLabelAdverListMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsGroupLabelAdverListMode.setStatus("current")
_JuniMplsGroupLdpProfileTable_Object = MibTable
juniMplsGroupLdpProfileTable = _JuniMplsGroupLdpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    juniMplsGroupLdpProfileTable.setStatus("current")
_JuniMplsGroupLdpProfileEntry_Object = MibTableRow
juniMplsGroupLdpProfileEntry = _JuniMplsGroupLdpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4, 1)
)
juniMplsGroupLdpProfileEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsGroupLdpProfileName"),
)
if mibBuilder.loadTexts:
    juniMplsGroupLdpProfileEntry.setStatus("current")


class _JuniMplsGroupLdpProfileName_Type(DisplayString):
    """Custom type juniMplsGroupLdpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsGroupLdpProfileName_Type.__name__ = "DisplayString"
_JuniMplsGroupLdpProfileName_Object = MibTableColumn
juniMplsGroupLdpProfileName = _JuniMplsGroupLdpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4, 1, 1),
    _JuniMplsGroupLdpProfileName_Type()
)
juniMplsGroupLdpProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsGroupLdpProfileName.setStatus("current")


class _JuniMplsGroupLdpProfileHelloHoldTime_Type(Integer32):
    """Custom type juniMplsGroupLdpProfileHelloHoldTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_JuniMplsGroupLdpProfileHelloHoldTime_Type.__name__ = "Integer32"
_JuniMplsGroupLdpProfileHelloHoldTime_Object = MibTableColumn
juniMplsGroupLdpProfileHelloHoldTime = _JuniMplsGroupLdpProfileHelloHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4, 1, 2),
    _JuniMplsGroupLdpProfileHelloHoldTime_Type()
)
juniMplsGroupLdpProfileHelloHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsGroupLdpProfileHelloHoldTime.setStatus("current")


class _JuniMplsGroupLdpProfileCrLdpAdminState_Type(Integer32):
    """Custom type juniMplsGroupLdpProfileCrLdpAdminState based on Integer32"""
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


_JuniMplsGroupLdpProfileCrLdpAdminState_Type.__name__ = "Integer32"
_JuniMplsGroupLdpProfileCrLdpAdminState_Object = MibTableColumn
juniMplsGroupLdpProfileCrLdpAdminState = _JuniMplsGroupLdpProfileCrLdpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4, 1, 3),
    _JuniMplsGroupLdpProfileCrLdpAdminState_Type()
)
juniMplsGroupLdpProfileCrLdpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsGroupLdpProfileCrLdpAdminState.setStatus("obsolete")
_JuniMplsGroupLdpProfileRowStatus_Type = RowStatus
_JuniMplsGroupLdpProfileRowStatus_Object = MibTableColumn
juniMplsGroupLdpProfileRowStatus = _JuniMplsGroupLdpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 4, 1, 4),
    _JuniMplsGroupLdpProfileRowStatus_Type()
)
juniMplsGroupLdpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsGroupLdpProfileRowStatus.setStatus("current")
_JuniMplsGroupRsvpProfileTable_Object = MibTable
juniMplsGroupRsvpProfileTable = _JuniMplsGroupRsvpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    juniMplsGroupRsvpProfileTable.setStatus("current")
_JuniMplsGroupRsvpProfileEntry_Object = MibTableRow
juniMplsGroupRsvpProfileEntry = _JuniMplsGroupRsvpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5, 1)
)
juniMplsGroupRsvpProfileEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsGroupRsvpProfileName"),
)
if mibBuilder.loadTexts:
    juniMplsGroupRsvpProfileEntry.setStatus("current")


class _JuniMplsGroupRsvpProfileName_Type(DisplayString):
    """Custom type juniMplsGroupRsvpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsGroupRsvpProfileName_Type.__name__ = "DisplayString"
_JuniMplsGroupRsvpProfileName_Object = MibTableColumn
juniMplsGroupRsvpProfileName = _JuniMplsGroupRsvpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5, 1, 1),
    _JuniMplsGroupRsvpProfileName_Type()
)
juniMplsGroupRsvpProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsGroupRsvpProfileName.setStatus("current")


class _JuniMplsGroupRsvpProfileRefreshPeriod_Type(Unsigned32):
    """Custom type juniMplsGroupRsvpProfileRefreshPeriod based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_JuniMplsGroupRsvpProfileRefreshPeriod_Type.__name__ = "Unsigned32"
_JuniMplsGroupRsvpProfileRefreshPeriod_Object = MibTableColumn
juniMplsGroupRsvpProfileRefreshPeriod = _JuniMplsGroupRsvpProfileRefreshPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5, 1, 2),
    _JuniMplsGroupRsvpProfileRefreshPeriod_Type()
)
juniMplsGroupRsvpProfileRefreshPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsGroupRsvpProfileRefreshPeriod.setStatus("current")


class _JuniMplsGroupRsvpProfileCleanupTimeoutFactor_Type(Integer32):
    """Custom type juniMplsGroupRsvpProfileCleanupTimeoutFactor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_JuniMplsGroupRsvpProfileCleanupTimeoutFactor_Type.__name__ = "Integer32"
_JuniMplsGroupRsvpProfileCleanupTimeoutFactor_Object = MibTableColumn
juniMplsGroupRsvpProfileCleanupTimeoutFactor = _JuniMplsGroupRsvpProfileCleanupTimeoutFactor_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5, 1, 3),
    _JuniMplsGroupRsvpProfileCleanupTimeoutFactor_Type()
)
juniMplsGroupRsvpProfileCleanupTimeoutFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsGroupRsvpProfileCleanupTimeoutFactor.setStatus("current")
_JuniMplsGroupRsvpProfileRowStatus_Type = RowStatus
_JuniMplsGroupRsvpProfileRowStatus_Object = MibTableColumn
juniMplsGroupRsvpProfileRowStatus = _JuniMplsGroupRsvpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 1, 2, 5, 1, 4),
    _JuniMplsGroupRsvpProfileRowStatus_Type()
)
juniMplsGroupRsvpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsGroupRsvpProfileRowStatus.setStatus("current")
_JuniMplsMajorLayer_ObjectIdentity = ObjectIdentity
juniMplsMajorLayer = _JuniMplsMajorLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2)
)
_JuniMplsIfMajorLayer_ObjectIdentity = ObjectIdentity
juniMplsIfMajorLayer = _JuniMplsIfMajorLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1)
)
_JuniMplsIfMajorNextIfIndex_Type = JuniNextIfIndex
_JuniMplsIfMajorNextIfIndex_Object = MibScalar
juniMplsIfMajorNextIfIndex = _JuniMplsIfMajorNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 1),
    _JuniMplsIfMajorNextIfIndex_Type()
)
juniMplsIfMajorNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMplsIfMajorNextIfIndex.setStatus("current")
_JuniMplsIfMajorTable_Object = MibTable
juniMplsIfMajorTable = _JuniMplsIfMajorTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniMplsIfMajorTable.setStatus("current")
_JuniMplsIfMajorEntry_Object = MibTableRow
juniMplsIfMajorEntry = _JuniMplsIfMajorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1)
)
juniMplsIfMajorEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsIfMajorIndex"),
)
if mibBuilder.loadTexts:
    juniMplsIfMajorEntry.setStatus("current")
_JuniMplsIfMajorIndex_Type = InterfaceIndex
_JuniMplsIfMajorIndex_Object = MibTableColumn
juniMplsIfMajorIndex = _JuniMplsIfMajorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 1),
    _JuniMplsIfMajorIndex_Type()
)
juniMplsIfMajorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsIfMajorIndex.setStatus("current")
_JuniMplsIfMajorRowStatus_Type = RowStatus
_JuniMplsIfMajorRowStatus_Object = MibTableColumn
juniMplsIfMajorRowStatus = _JuniMplsIfMajorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 2),
    _JuniMplsIfMajorRowStatus_Type()
)
juniMplsIfMajorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorRowStatus.setStatus("current")
_JuniMplsIfMajorLowerIfIndex_Type = InterfaceIndexOrZero
_JuniMplsIfMajorLowerIfIndex_Object = MibTableColumn
juniMplsIfMajorLowerIfIndex = _JuniMplsIfMajorLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 3),
    _JuniMplsIfMajorLowerIfIndex_Type()
)
juniMplsIfMajorLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorLowerIfIndex.setStatus("current")


class _JuniMplsIfMajorAdminStatus_Type(Integer32):
    """Custom type juniMplsIfMajorAdminStatus based on Integer32"""
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


_JuniMplsIfMajorAdminStatus_Type.__name__ = "Integer32"
_JuniMplsIfMajorAdminStatus_Object = MibTableColumn
juniMplsIfMajorAdminStatus = _JuniMplsIfMajorAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 4),
    _JuniMplsIfMajorAdminStatus_Type()
)
juniMplsIfMajorAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorAdminStatus.setStatus("current")


class _JuniMplsIfMajorLdpAdminStatus_Type(Integer32):
    """Custom type juniMplsIfMajorLdpAdminStatus based on Integer32"""
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


_JuniMplsIfMajorLdpAdminStatus_Type.__name__ = "Integer32"
_JuniMplsIfMajorLdpAdminStatus_Object = MibTableColumn
juniMplsIfMajorLdpAdminStatus = _JuniMplsIfMajorLdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 5),
    _JuniMplsIfMajorLdpAdminStatus_Type()
)
juniMplsIfMajorLdpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorLdpAdminStatus.setStatus("current")


class _JuniMplsIfMajorLdpProfileName_Type(DisplayString):
    """Custom type juniMplsIfMajorLdpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsIfMajorLdpProfileName_Type.__name__ = "DisplayString"
_JuniMplsIfMajorLdpProfileName_Object = MibTableColumn
juniMplsIfMajorLdpProfileName = _JuniMplsIfMajorLdpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 6),
    _JuniMplsIfMajorLdpProfileName_Type()
)
juniMplsIfMajorLdpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorLdpProfileName.setStatus("current")


class _JuniMplsIfMajorLdpVpiStart_Type(JuniMajorCfgVpiRanges):
    """Custom type juniMplsIfMajorLdpVpiStart based on JuniMajorCfgVpiRanges"""
    defaultValue = 0


_JuniMplsIfMajorLdpVpiStart_Object = MibTableColumn
juniMplsIfMajorLdpVpiStart = _JuniMplsIfMajorLdpVpiStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 7),
    _JuniMplsIfMajorLdpVpiStart_Type()
)
juniMplsIfMajorLdpVpiStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorLdpVpiStart.setStatus("current")


class _JuniMplsIfMajorLdpVpiStop_Type(JuniMajorCfgVpiRanges):
    """Custom type juniMplsIfMajorLdpVpiStop based on JuniMajorCfgVpiRanges"""
    defaultValue = 0


_JuniMplsIfMajorLdpVpiStop_Object = MibTableColumn
juniMplsIfMajorLdpVpiStop = _JuniMplsIfMajorLdpVpiStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 8),
    _JuniMplsIfMajorLdpVpiStop_Type()
)
juniMplsIfMajorLdpVpiStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorLdpVpiStop.setStatus("current")
_JuniMplsIfMajorLdpVciStart_Type = JuniMajorCfgVciRanges
_JuniMplsIfMajorLdpVciStart_Object = MibTableColumn
juniMplsIfMajorLdpVciStart = _JuniMplsIfMajorLdpVciStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 9),
    _JuniMplsIfMajorLdpVciStart_Type()
)
juniMplsIfMajorLdpVciStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorLdpVciStart.setStatus("current")
_JuniMplsIfMajorLdpVciStop_Type = JuniMajorCfgVciRanges
_JuniMplsIfMajorLdpVciStop_Object = MibTableColumn
juniMplsIfMajorLdpVciStop = _JuniMplsIfMajorLdpVciStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 10),
    _JuniMplsIfMajorLdpVciStop_Type()
)
juniMplsIfMajorLdpVciStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorLdpVciStop.setStatus("current")


class _JuniMplsIfMajorRsvpAdminStatus_Type(Integer32):
    """Custom type juniMplsIfMajorRsvpAdminStatus based on Integer32"""
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


_JuniMplsIfMajorRsvpAdminStatus_Type.__name__ = "Integer32"
_JuniMplsIfMajorRsvpAdminStatus_Object = MibTableColumn
juniMplsIfMajorRsvpAdminStatus = _JuniMplsIfMajorRsvpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 11),
    _JuniMplsIfMajorRsvpAdminStatus_Type()
)
juniMplsIfMajorRsvpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorRsvpAdminStatus.setStatus("current")


class _JuniMplsIfMajorRsvpProfileName_Type(DisplayString):
    """Custom type juniMplsIfMajorRsvpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsIfMajorRsvpProfileName_Type.__name__ = "DisplayString"
_JuniMplsIfMajorRsvpProfileName_Object = MibTableColumn
juniMplsIfMajorRsvpProfileName = _JuniMplsIfMajorRsvpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 12),
    _JuniMplsIfMajorRsvpProfileName_Type()
)
juniMplsIfMajorRsvpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorRsvpProfileName.setStatus("current")


class _JuniMplsIfMajorRsvpVpiStart_Type(JuniMajorCfgVpiRanges):
    """Custom type juniMplsIfMajorRsvpVpiStart based on JuniMajorCfgVpiRanges"""
    defaultValue = 0


_JuniMplsIfMajorRsvpVpiStart_Object = MibTableColumn
juniMplsIfMajorRsvpVpiStart = _JuniMplsIfMajorRsvpVpiStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 13),
    _JuniMplsIfMajorRsvpVpiStart_Type()
)
juniMplsIfMajorRsvpVpiStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorRsvpVpiStart.setStatus("current")


class _JuniMplsIfMajorRsvpVpiStop_Type(JuniMajorCfgVpiRanges):
    """Custom type juniMplsIfMajorRsvpVpiStop based on JuniMajorCfgVpiRanges"""
    defaultValue = 0


_JuniMplsIfMajorRsvpVpiStop_Object = MibTableColumn
juniMplsIfMajorRsvpVpiStop = _JuniMplsIfMajorRsvpVpiStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 14),
    _JuniMplsIfMajorRsvpVpiStop_Type()
)
juniMplsIfMajorRsvpVpiStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorRsvpVpiStop.setStatus("current")
_JuniMplsIfMajorRsvpVciStart_Type = JuniMajorCfgVciRanges
_JuniMplsIfMajorRsvpVciStart_Object = MibTableColumn
juniMplsIfMajorRsvpVciStart = _JuniMplsIfMajorRsvpVciStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 15),
    _JuniMplsIfMajorRsvpVciStart_Type()
)
juniMplsIfMajorRsvpVciStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorRsvpVciStart.setStatus("current")
_JuniMplsIfMajorRsvpVciStop_Type = JuniMajorCfgVciRanges
_JuniMplsIfMajorRsvpVciStop_Object = MibTableColumn
juniMplsIfMajorRsvpVciStop = _JuniMplsIfMajorRsvpVciStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 16),
    _JuniMplsIfMajorRsvpVciStop_Type()
)
juniMplsIfMajorRsvpVciStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMajorRsvpVciStop.setStatus("current")


class _JuniMplsIfMajorLabelSpaceType_Type(Integer32):
    """Custom type juniMplsIfMajorLabelSpaceType based on Integer32"""
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


_JuniMplsIfMajorLabelSpaceType_Type.__name__ = "Integer32"
_JuniMplsIfMajorLabelSpaceType_Object = MibTableColumn
juniMplsIfMajorLabelSpaceType = _JuniMplsIfMajorLabelSpaceType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 17),
    _JuniMplsIfMajorLabelSpaceType_Type()
)
juniMplsIfMajorLabelSpaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMplsIfMajorLabelSpaceType.setStatus("current")


class _JuniMplsIfMajorOpState_Type(Integer32):
    """Custom type juniMplsIfMajorOpState based on Integer32"""
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


_JuniMplsIfMajorOpState_Type.__name__ = "Integer32"
_JuniMplsIfMajorOpState_Object = MibTableColumn
juniMplsIfMajorOpState = _JuniMplsIfMajorOpState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 18),
    _JuniMplsIfMajorOpState_Type()
)
juniMplsIfMajorOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMplsIfMajorOpState.setStatus("current")


class _JuniMplsIfMajorCrLdpAdminState_Type(Integer32):
    """Custom type juniMplsIfMajorCrLdpAdminState based on Integer32"""
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


_JuniMplsIfMajorCrLdpAdminState_Type.__name__ = "Integer32"
_JuniMplsIfMajorCrLdpAdminState_Object = MibTableColumn
juniMplsIfMajorCrLdpAdminState = _JuniMplsIfMajorCrLdpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 2, 1, 2, 1, 19),
    _JuniMplsIfMajorCrLdpAdminState_Type()
)
juniMplsIfMajorCrLdpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMplsIfMajorCrLdpAdminState.setStatus("obsolete")
_JuniMplsMinorLayer_ObjectIdentity = ObjectIdentity
juniMplsMinorLayer = _JuniMplsMinorLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3)
)
_JuniMplsIfMinorLayer_ObjectIdentity = ObjectIdentity
juniMplsIfMinorLayer = _JuniMplsIfMinorLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1)
)
_JuniMplsIfMinorNextIfIndex_Type = JuniNextIfIndex
_JuniMplsIfMinorNextIfIndex_Object = MibScalar
juniMplsIfMinorNextIfIndex = _JuniMplsIfMinorNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 1),
    _JuniMplsIfMinorNextIfIndex_Type()
)
juniMplsIfMinorNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMplsIfMinorNextIfIndex.setStatus("current")
_JuniMplsIfMinorTable_Object = MibTable
juniMplsIfMinorTable = _JuniMplsIfMinorTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    juniMplsIfMinorTable.setStatus("current")
_JuniMplsIfMinorEntry_Object = MibTableRow
juniMplsIfMinorEntry = _JuniMplsIfMinorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1)
)
juniMplsIfMinorEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsIfMinorIndex"),
)
if mibBuilder.loadTexts:
    juniMplsIfMinorEntry.setStatus("current")
_JuniMplsIfMinorIndex_Type = InterfaceIndex
_JuniMplsIfMinorIndex_Object = MibTableColumn
juniMplsIfMinorIndex = _JuniMplsIfMinorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 1),
    _JuniMplsIfMinorIndex_Type()
)
juniMplsIfMinorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsIfMinorIndex.setStatus("current")
_JuniMplsIfMinorRowStatus_Type = RowStatus
_JuniMplsIfMinorRowStatus_Object = MibTableColumn
juniMplsIfMinorRowStatus = _JuniMplsIfMinorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 2),
    _JuniMplsIfMinorRowStatus_Type()
)
juniMplsIfMinorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorRowStatus.setStatus("current")
_JuniMplsIfMinorLowerIfIndex_Type = InterfaceIndexOrZero
_JuniMplsIfMinorLowerIfIndex_Object = MibTableColumn
juniMplsIfMinorLowerIfIndex = _JuniMplsIfMinorLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 3),
    _JuniMplsIfMinorLowerIfIndex_Type()
)
juniMplsIfMinorLowerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMplsIfMinorLowerIfIndex.setStatus("current")


class _JuniMplsIfMinorAdminStatus_Type(Integer32):
    """Custom type juniMplsIfMinorAdminStatus based on Integer32"""
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


_JuniMplsIfMinorAdminStatus_Type.__name__ = "Integer32"
_JuniMplsIfMinorAdminStatus_Object = MibTableColumn
juniMplsIfMinorAdminStatus = _JuniMplsIfMinorAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 4),
    _JuniMplsIfMinorAdminStatus_Type()
)
juniMplsIfMinorAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorAdminStatus.setStatus("current")
_JuniMplsIfMinorEndpointAddress_Type = IpAddress
_JuniMplsIfMinorEndpointAddress_Object = MibTableColumn
juniMplsIfMinorEndpointAddress = _JuniMplsIfMinorEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 5),
    _JuniMplsIfMinorEndpointAddress_Type()
)
juniMplsIfMinorEndpointAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorEndpointAddress.setStatus("current")


class _JuniMplsIfMinorEndpointDstMask_Type(IpAddress):
    """Custom type juniMplsIfMinorEndpointDstMask based on IpAddress"""
    defaultValue = 0


_JuniMplsIfMinorEndpointDstMask_Object = MibTableColumn
juniMplsIfMinorEndpointDstMask = _JuniMplsIfMinorEndpointDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 6),
    _JuniMplsIfMinorEndpointDstMask_Type()
)
juniMplsIfMinorEndpointDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorEndpointDstMask.setStatus("current")


class _JuniMplsIfMinorTunnelMetricMode_Type(Integer32):
    """Custom type juniMplsIfMinorTunnelMetricMode based on Integer32"""
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


_JuniMplsIfMinorTunnelMetricMode_Type.__name__ = "Integer32"
_JuniMplsIfMinorTunnelMetricMode_Object = MibTableColumn
juniMplsIfMinorTunnelMetricMode = _JuniMplsIfMinorTunnelMetricMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 7),
    _JuniMplsIfMinorTunnelMetricMode_Type()
)
juniMplsIfMinorTunnelMetricMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorTunnelMetricMode.setStatus("current")


class _JuniMplsIfMinorAbsoluteTunnelMetric_Type(Unsigned32):
    """Custom type juniMplsIfMinorAbsoluteTunnelMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JuniMplsIfMinorAbsoluteTunnelMetric_Type.__name__ = "Unsigned32"
_JuniMplsIfMinorAbsoluteTunnelMetric_Object = MibTableColumn
juniMplsIfMinorAbsoluteTunnelMetric = _JuniMplsIfMinorAbsoluteTunnelMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 8),
    _JuniMplsIfMinorAbsoluteTunnelMetric_Type()
)
juniMplsIfMinorAbsoluteTunnelMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorAbsoluteTunnelMetric.setStatus("current")


class _JuniMplsIfMinorRelativeTunnelMetric_Type(Integer32):
    """Custom type juniMplsIfMinorRelativeTunnelMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_JuniMplsIfMinorRelativeTunnelMetric_Type.__name__ = "Integer32"
_JuniMplsIfMinorRelativeTunnelMetric_Object = MibTableColumn
juniMplsIfMinorRelativeTunnelMetric = _JuniMplsIfMinorRelativeTunnelMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 9),
    _JuniMplsIfMinorRelativeTunnelMetric_Type()
)
juniMplsIfMinorRelativeTunnelMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorRelativeTunnelMetric.setStatus("current")


class _JuniMplsIfMinorLabelDistProto_Type(Integer32):
    """Custom type juniMplsIfMinorLabelDistProto based on Integer32"""
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


_JuniMplsIfMinorLabelDistProto_Type.__name__ = "Integer32"
_JuniMplsIfMinorLabelDistProto_Object = MibTableColumn
juniMplsIfMinorLabelDistProto = _JuniMplsIfMinorLabelDistProto_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 10),
    _JuniMplsIfMinorLabelDistProto_Type()
)
juniMplsIfMinorLabelDistProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorLabelDistProto.setStatus("obsolete")


class _JuniMplsIfMinorAnnounceToOspf_Type(TruthValue):
    """Custom type juniMplsIfMinorAnnounceToOspf based on TruthValue"""


_JuniMplsIfMinorAnnounceToOspf_Object = MibTableColumn
juniMplsIfMinorAnnounceToOspf = _JuniMplsIfMinorAnnounceToOspf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 11),
    _JuniMplsIfMinorAnnounceToOspf_Type()
)
juniMplsIfMinorAnnounceToOspf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorAnnounceToOspf.setStatus("current")


class _JuniMplsIfMinorAnnounceToIsis_Type(TruthValue):
    """Custom type juniMplsIfMinorAnnounceToIsis based on TruthValue"""


_JuniMplsIfMinorAnnounceToIsis_Object = MibTableColumn
juniMplsIfMinorAnnounceToIsis = _JuniMplsIfMinorAnnounceToIsis_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 12),
    _JuniMplsIfMinorAnnounceToIsis_Type()
)
juniMplsIfMinorAnnounceToIsis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorAnnounceToIsis.setStatus("current")


class _JuniMplsIfMinorAnnounceToBgp_Type(TruthValue):
    """Custom type juniMplsIfMinorAnnounceToBgp based on TruthValue"""


_JuniMplsIfMinorAnnounceToBgp_Object = MibTableColumn
juniMplsIfMinorAnnounceToBgp = _JuniMplsIfMinorAnnounceToBgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 13),
    _JuniMplsIfMinorAnnounceToBgp_Type()
)
juniMplsIfMinorAnnounceToBgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorAnnounceToBgp.setStatus("current")


class _JuniMplsIfMinorBandwidth_Type(JuniMinorCfgBWRanges):
    """Custom type juniMplsIfMinorBandwidth based on JuniMinorCfgBWRanges"""
    defaultValue = 0


_JuniMplsIfMinorBandwidth_Object = MibTableColumn
juniMplsIfMinorBandwidth = _JuniMplsIfMinorBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 14),
    _JuniMplsIfMinorBandwidth_Type()
)
juniMplsIfMinorBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorBandwidth.setStatus("current")


class _JuniMplsIfMinorAffinity_Type(OctetString):
    """Custom type juniMplsIfMinorAffinity based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_JuniMplsIfMinorAffinity_Type.__name__ = "OctetString"
_JuniMplsIfMinorAffinity_Object = MibTableColumn
juniMplsIfMinorAffinity = _JuniMplsIfMinorAffinity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 15),
    _JuniMplsIfMinorAffinity_Type()
)
juniMplsIfMinorAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorAffinity.setStatus("current")


class _JuniMplsIfMinorAffinityMask_Type(OctetString):
    """Custom type juniMplsIfMinorAffinityMask based on OctetString"""
    defaultHexValue = "0000ffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_JuniMplsIfMinorAffinityMask_Type.__name__ = "OctetString"
_JuniMplsIfMinorAffinityMask_Object = MibTableColumn
juniMplsIfMinorAffinityMask = _JuniMplsIfMinorAffinityMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 16),
    _JuniMplsIfMinorAffinityMask_Type()
)
juniMplsIfMinorAffinityMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorAffinityMask.setStatus("current")
_JuniMplsIfMinorSetupPriority_Type = JuniMinorCfgHoldingAndSetupPriorityRanges
_JuniMplsIfMinorSetupPriority_Object = MibTableColumn
juniMplsIfMinorSetupPriority = _JuniMplsIfMinorSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 17),
    _JuniMplsIfMinorSetupPriority_Type()
)
juniMplsIfMinorSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorSetupPriority.setStatus("current")
_JuniMplsIfMinorHoldingPriority_Type = JuniMinorCfgHoldingAndSetupPriorityRanges
_JuniMplsIfMinorHoldingPriority_Object = MibTableColumn
juniMplsIfMinorHoldingPriority = _JuniMplsIfMinorHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 18),
    _JuniMplsIfMinorHoldingPriority_Type()
)
juniMplsIfMinorHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorHoldingPriority.setStatus("current")


class _JuniMplsIfMinorTunnelName_Type(DisplayString):
    """Custom type juniMplsIfMinorTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsIfMinorTunnelName_Type.__name__ = "DisplayString"
_JuniMplsIfMinorTunnelName_Object = MibTableColumn
juniMplsIfMinorTunnelName = _JuniMplsIfMinorTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 19),
    _JuniMplsIfMinorTunnelName_Type()
)
juniMplsIfMinorTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorTunnelName.setStatus("current")


class _JuniMplsIfMinorTunnelRetryTimes_Type(JuniMinorCfgRetryTimesAndNorouteRanges):
    """Custom type juniMplsIfMinorTunnelRetryTimes based on JuniMinorCfgRetryTimesAndNorouteRanges"""
    defaultValue = 0


_JuniMplsIfMinorTunnelRetryTimes_Object = MibTableColumn
juniMplsIfMinorTunnelRetryTimes = _JuniMplsIfMinorTunnelRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 20),
    _JuniMplsIfMinorTunnelRetryTimes_Type()
)
juniMplsIfMinorTunnelRetryTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorTunnelRetryTimes.setStatus("current")


class _JuniMplsIfMinorTunnelRetryInterval_Type(JuniMinorCfgRetryIntervalAndNorouteRanges):
    """Custom type juniMplsIfMinorTunnelRetryInterval based on JuniMinorCfgRetryIntervalAndNorouteRanges"""
    defaultValue = 5


_JuniMplsIfMinorTunnelRetryInterval_Object = MibTableColumn
juniMplsIfMinorTunnelRetryInterval = _JuniMplsIfMinorTunnelRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 21),
    _JuniMplsIfMinorTunnelRetryInterval_Type()
)
juniMplsIfMinorTunnelRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorTunnelRetryInterval.setStatus("current")


class _JuniMplsIfMinorTunnelRetryTimesNoroute_Type(JuniMinorCfgRetryTimesAndNorouteRanges):
    """Custom type juniMplsIfMinorTunnelRetryTimesNoroute based on JuniMinorCfgRetryTimesAndNorouteRanges"""
    defaultValue = 0


_JuniMplsIfMinorTunnelRetryTimesNoroute_Object = MibTableColumn
juniMplsIfMinorTunnelRetryTimesNoroute = _JuniMplsIfMinorTunnelRetryTimesNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 22),
    _JuniMplsIfMinorTunnelRetryTimesNoroute_Type()
)
juniMplsIfMinorTunnelRetryTimesNoroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorTunnelRetryTimesNoroute.setStatus("current")


class _JuniMplsIfMinorTunnelRetryIntervalNoroute_Type(JuniMinorCfgRetryIntervalAndNorouteRanges):
    """Custom type juniMplsIfMinorTunnelRetryIntervalNoroute based on JuniMinorCfgRetryIntervalAndNorouteRanges"""
    defaultValue = 5


_JuniMplsIfMinorTunnelRetryIntervalNoroute_Object = MibTableColumn
juniMplsIfMinorTunnelRetryIntervalNoroute = _JuniMplsIfMinorTunnelRetryIntervalNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 23),
    _JuniMplsIfMinorTunnelRetryIntervalNoroute_Type()
)
juniMplsIfMinorTunnelRetryIntervalNoroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorTunnelRetryIntervalNoroute.setStatus("current")
_JuniMplsIfMinorBaseTunnelName_Type = DisplayString
_JuniMplsIfMinorBaseTunnelName_Object = MibTableColumn
juniMplsIfMinorBaseTunnelName = _JuniMplsIfMinorBaseTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 24),
    _JuniMplsIfMinorBaseTunnelName_Type()
)
juniMplsIfMinorBaseTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorBaseTunnelName.setStatus("obsolete")


class _JuniMplsIfMinorVpnOuiNumber_Type(Integer32):
    """Custom type juniMplsIfMinorVpnOuiNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_JuniMplsIfMinorVpnOuiNumber_Type.__name__ = "Integer32"
_JuniMplsIfMinorVpnOuiNumber_Object = MibTableColumn
juniMplsIfMinorVpnOuiNumber = _JuniMplsIfMinorVpnOuiNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 25),
    _JuniMplsIfMinorVpnOuiNumber_Type()
)
juniMplsIfMinorVpnOuiNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorVpnOuiNumber.setStatus("obsolete")
_JuniMplsIfMinorVpnIndex_Type = IpAddress
_JuniMplsIfMinorVpnIndex_Object = MibTableColumn
juniMplsIfMinorVpnIndex = _JuniMplsIfMinorVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 26),
    _JuniMplsIfMinorVpnIndex_Type()
)
juniMplsIfMinorVpnIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorVpnIndex.setStatus("obsolete")


class _JuniMplsIfMinorTunnelOpState_Type(Integer32):
    """Custom type juniMplsIfMinorTunnelOpState based on Integer32"""
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


_JuniMplsIfMinorTunnelOpState_Type.__name__ = "Integer32"
_JuniMplsIfMinorTunnelOpState_Object = MibTableColumn
juniMplsIfMinorTunnelOpState = _JuniMplsIfMinorTunnelOpState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 27),
    _JuniMplsIfMinorTunnelOpState_Type()
)
juniMplsIfMinorTunnelOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniMplsIfMinorTunnelOpState.setStatus("current")


class _JuniMplsIfMinorTargetedDynamicTunnel_Type(TruthValue):
    """Custom type juniMplsIfMinorTargetedDynamicTunnel based on TruthValue"""


_JuniMplsIfMinorTargetedDynamicTunnel_Object = MibTableColumn
juniMplsIfMinorTargetedDynamicTunnel = _JuniMplsIfMinorTargetedDynamicTunnel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 28),
    _JuniMplsIfMinorTargetedDynamicTunnel_Type()
)
juniMplsIfMinorTargetedDynamicTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorTargetedDynamicTunnel.setStatus("obsolete")


class _JuniMplsIfMinorReoptimization_Type(TruthValue):
    """Custom type juniMplsIfMinorReoptimization based on TruthValue"""


_JuniMplsIfMinorReoptimization_Object = MibTableColumn
juniMplsIfMinorReoptimization = _JuniMplsIfMinorReoptimization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 1, 2, 1, 29),
    _JuniMplsIfMinorReoptimization_Type()
)
juniMplsIfMinorReoptimization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorReoptimization.setStatus("current")
_JuniMplsMinorLayerList_ObjectIdentity = ObjectIdentity
juniMplsMinorLayerList = _JuniMplsMinorLayerList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2)
)
_JuniMplsIfMinorPathOptionTable_Object = MibTable
juniMplsIfMinorPathOptionTable = _JuniMplsIfMinorPathOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    juniMplsIfMinorPathOptionTable.setStatus("current")
_JuniMplsIfMinorPathOptionEntry_Object = MibTableRow
juniMplsIfMinorPathOptionEntry = _JuniMplsIfMinorPathOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1)
)
juniMplsIfMinorPathOptionEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionIndex"),
    (0, "Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionNumber"),
)
if mibBuilder.loadTexts:
    juniMplsIfMinorPathOptionEntry.setStatus("current")
_JuniMplsIfMinorPathOptionIndex_Type = InterfaceIndex
_JuniMplsIfMinorPathOptionIndex_Object = MibTableColumn
juniMplsIfMinorPathOptionIndex = _JuniMplsIfMinorPathOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 1),
    _JuniMplsIfMinorPathOptionIndex_Type()
)
juniMplsIfMinorPathOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsIfMinorPathOptionIndex.setStatus("current")


class _JuniMplsIfMinorPathOptionNumber_Type(Integer32):
    """Custom type juniMplsIfMinorPathOptionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JuniMplsIfMinorPathOptionNumber_Type.__name__ = "Integer32"
_JuniMplsIfMinorPathOptionNumber_Object = MibTableColumn
juniMplsIfMinorPathOptionNumber = _JuniMplsIfMinorPathOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 2),
    _JuniMplsIfMinorPathOptionNumber_Type()
)
juniMplsIfMinorPathOptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsIfMinorPathOptionNumber.setStatus("current")


class _JuniMplsIfMinorPathOptionProtocol_Type(Integer32):
    """Custom type juniMplsIfMinorPathOptionProtocol based on Integer32"""
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


_JuniMplsIfMinorPathOptionProtocol_Type.__name__ = "Integer32"
_JuniMplsIfMinorPathOptionProtocol_Object = MibTableColumn
juniMplsIfMinorPathOptionProtocol = _JuniMplsIfMinorPathOptionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 3),
    _JuniMplsIfMinorPathOptionProtocol_Type()
)
juniMplsIfMinorPathOptionProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorPathOptionProtocol.setStatus("current")
_JuniMplsIfMinorPathOptionLockdown_Type = TruthValue
_JuniMplsIfMinorPathOptionLockdown_Object = MibTableColumn
juniMplsIfMinorPathOptionLockdown = _JuniMplsIfMinorPathOptionLockdown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 4),
    _JuniMplsIfMinorPathOptionLockdown_Type()
)
juniMplsIfMinorPathOptionLockdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorPathOptionLockdown.setStatus("current")


class _JuniMplsIfMinorPathOptionPathName_Type(DisplayString):
    """Custom type juniMplsIfMinorPathOptionPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsIfMinorPathOptionPathName_Type.__name__ = "DisplayString"
_JuniMplsIfMinorPathOptionPathName_Object = MibTableColumn
juniMplsIfMinorPathOptionPathName = _JuniMplsIfMinorPathOptionPathName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 5),
    _JuniMplsIfMinorPathOptionPathName_Type()
)
juniMplsIfMinorPathOptionPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorPathOptionPathName.setStatus("current")


class _JuniMplsIfMinorPathOptionPathId_Type(Integer32):
    """Custom type juniMplsIfMinorPathOptionPathId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniMplsIfMinorPathOptionPathId_Type.__name__ = "Integer32"
_JuniMplsIfMinorPathOptionPathId_Object = MibTableColumn
juniMplsIfMinorPathOptionPathId = _JuniMplsIfMinorPathOptionPathId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 6),
    _JuniMplsIfMinorPathOptionPathId_Type()
)
juniMplsIfMinorPathOptionPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorPathOptionPathId.setStatus("current")
_JuniMplsIfMinorPathOptionRowStatus_Type = RowStatus
_JuniMplsIfMinorPathOptionRowStatus_Object = MibTableColumn
juniMplsIfMinorPathOptionRowStatus = _JuniMplsIfMinorPathOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 3, 2, 1, 1, 7),
    _JuniMplsIfMinorPathOptionRowStatus_Type()
)
juniMplsIfMinorPathOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsIfMinorPathOptionRowStatus.setStatus("current")
_JuniMplsTunnelProfile_ObjectIdentity = ObjectIdentity
juniMplsTunnelProfile = _JuniMplsTunnelProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4)
)
_JuniMplsTunnelProfileGroup_ObjectIdentity = ObjectIdentity
juniMplsTunnelProfileGroup = _JuniMplsTunnelProfileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1)
)
_JuniMplsTunnelProfileTable_Object = MibTable
juniMplsTunnelProfileTable = _JuniMplsTunnelProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfileTable.setStatus("current")
_JuniMplsTunnelProfileEntry_Object = MibTableRow
juniMplsTunnelProfileEntry = _JuniMplsTunnelProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1)
)
juniMplsTunnelProfileEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsTunnelProfileName"),
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfileEntry.setStatus("current")


class _JuniMplsTunnelProfileName_Type(DisplayString):
    """Custom type juniMplsTunnelProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsTunnelProfileName_Type.__name__ = "DisplayString"
_JuniMplsTunnelProfileName_Object = MibTableColumn
juniMplsTunnelProfileName = _JuniMplsTunnelProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 1),
    _JuniMplsTunnelProfileName_Type()
)
juniMplsTunnelProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileName.setStatus("current")


class _JuniMplsTunnelProfileAdminStatus_Type(Integer32):
    """Custom type juniMplsTunnelProfileAdminStatus based on Integer32"""
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


_JuniMplsTunnelProfileAdminStatus_Type.__name__ = "Integer32"
_JuniMplsTunnelProfileAdminStatus_Object = MibTableColumn
juniMplsTunnelProfileAdminStatus = _JuniMplsTunnelProfileAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 2),
    _JuniMplsTunnelProfileAdminStatus_Type()
)
juniMplsTunnelProfileAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileAdminStatus.setStatus("current")
_JuniMplsTunnelProfileBaseTunnelName_Type = DisplayString
_JuniMplsTunnelProfileBaseTunnelName_Object = MibTableColumn
juniMplsTunnelProfileBaseTunnelName = _JuniMplsTunnelProfileBaseTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 3),
    _JuniMplsTunnelProfileBaseTunnelName_Type()
)
juniMplsTunnelProfileBaseTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileBaseTunnelName.setStatus("obsolete")


class _JuniMplsTunnelProfileIpProfileName_Type(DisplayString):
    """Custom type juniMplsTunnelProfileIpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsTunnelProfileIpProfileName_Type.__name__ = "DisplayString"
_JuniMplsTunnelProfileIpProfileName_Object = MibTableColumn
juniMplsTunnelProfileIpProfileName = _JuniMplsTunnelProfileIpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 4),
    _JuniMplsTunnelProfileIpProfileName_Type()
)
juniMplsTunnelProfileIpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileIpProfileName.setStatus("current")


class _JuniMplsTunnelProfileLabelDistProto_Type(Integer32):
    """Custom type juniMplsTunnelProfileLabelDistProto based on Integer32"""
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


_JuniMplsTunnelProfileLabelDistProto_Type.__name__ = "Integer32"
_JuniMplsTunnelProfileLabelDistProto_Object = MibTableColumn
juniMplsTunnelProfileLabelDistProto = _JuniMplsTunnelProfileLabelDistProto_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 5),
    _JuniMplsTunnelProfileLabelDistProto_Type()
)
juniMplsTunnelProfileLabelDistProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileLabelDistProto.setStatus("obsolete")


class _JuniMplsTunnelProfileAnnounceToOspf_Type(TruthValue):
    """Custom type juniMplsTunnelProfileAnnounceToOspf based on TruthValue"""


_JuniMplsTunnelProfileAnnounceToOspf_Object = MibTableColumn
juniMplsTunnelProfileAnnounceToOspf = _JuniMplsTunnelProfileAnnounceToOspf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 6),
    _JuniMplsTunnelProfileAnnounceToOspf_Type()
)
juniMplsTunnelProfileAnnounceToOspf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileAnnounceToOspf.setStatus("current")


class _JuniMplsTunnelProfileAnnounceToIsis_Type(TruthValue):
    """Custom type juniMplsTunnelProfileAnnounceToIsis based on TruthValue"""


_JuniMplsTunnelProfileAnnounceToIsis_Object = MibTableColumn
juniMplsTunnelProfileAnnounceToIsis = _JuniMplsTunnelProfileAnnounceToIsis_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 7),
    _JuniMplsTunnelProfileAnnounceToIsis_Type()
)
juniMplsTunnelProfileAnnounceToIsis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileAnnounceToIsis.setStatus("current")


class _JuniMplsTunnelProfileAnnounceToBgp_Type(TruthValue):
    """Custom type juniMplsTunnelProfileAnnounceToBgp based on TruthValue"""


_JuniMplsTunnelProfileAnnounceToBgp_Object = MibTableColumn
juniMplsTunnelProfileAnnounceToBgp = _JuniMplsTunnelProfileAnnounceToBgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 8),
    _JuniMplsTunnelProfileAnnounceToBgp_Type()
)
juniMplsTunnelProfileAnnounceToBgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileAnnounceToBgp.setStatus("current")


class _JuniMplsTunnelProfileMetricMode_Type(Integer32):
    """Custom type juniMplsTunnelProfileMetricMode based on Integer32"""
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


_JuniMplsTunnelProfileMetricMode_Type.__name__ = "Integer32"
_JuniMplsTunnelProfileMetricMode_Object = MibTableColumn
juniMplsTunnelProfileMetricMode = _JuniMplsTunnelProfileMetricMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 9),
    _JuniMplsTunnelProfileMetricMode_Type()
)
juniMplsTunnelProfileMetricMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileMetricMode.setStatus("current")


class _JuniMplsTunnelProfileAbsoluteMetric_Type(Unsigned32):
    """Custom type juniMplsTunnelProfileAbsoluteMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JuniMplsTunnelProfileAbsoluteMetric_Type.__name__ = "Unsigned32"
_JuniMplsTunnelProfileAbsoluteMetric_Object = MibTableColumn
juniMplsTunnelProfileAbsoluteMetric = _JuniMplsTunnelProfileAbsoluteMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 10),
    _JuniMplsTunnelProfileAbsoluteMetric_Type()
)
juniMplsTunnelProfileAbsoluteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileAbsoluteMetric.setStatus("current")


class _JuniMplsTunnelProfileRelativeMetric_Type(Integer32):
    """Custom type juniMplsTunnelProfileRelativeMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_JuniMplsTunnelProfileRelativeMetric_Type.__name__ = "Integer32"
_JuniMplsTunnelProfileRelativeMetric_Object = MibTableColumn
juniMplsTunnelProfileRelativeMetric = _JuniMplsTunnelProfileRelativeMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 11),
    _JuniMplsTunnelProfileRelativeMetric_Type()
)
juniMplsTunnelProfileRelativeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileRelativeMetric.setStatus("current")


class _JuniMplsTunnelProfileBandwidth_Type(JuniProfileCfgBWRanges):
    """Custom type juniMplsTunnelProfileBandwidth based on JuniProfileCfgBWRanges"""
    defaultValue = 0


_JuniMplsTunnelProfileBandwidth_Object = MibTableColumn
juniMplsTunnelProfileBandwidth = _JuniMplsTunnelProfileBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 12),
    _JuniMplsTunnelProfileBandwidth_Type()
)
juniMplsTunnelProfileBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileBandwidth.setStatus("current")


class _JuniMplsTunnelProfileAffinity_Type(OctetString):
    """Custom type juniMplsTunnelProfileAffinity based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_JuniMplsTunnelProfileAffinity_Type.__name__ = "OctetString"
_JuniMplsTunnelProfileAffinity_Object = MibTableColumn
juniMplsTunnelProfileAffinity = _JuniMplsTunnelProfileAffinity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 13),
    _JuniMplsTunnelProfileAffinity_Type()
)
juniMplsTunnelProfileAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileAffinity.setStatus("current")


class _JuniMplsTunnelProfileAffinityMask_Type(OctetString):
    """Custom type juniMplsTunnelProfileAffinityMask based on OctetString"""
    defaultHexValue = "0000ffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_JuniMplsTunnelProfileAffinityMask_Type.__name__ = "OctetString"
_JuniMplsTunnelProfileAffinityMask_Object = MibTableColumn
juniMplsTunnelProfileAffinityMask = _JuniMplsTunnelProfileAffinityMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 14),
    _JuniMplsTunnelProfileAffinityMask_Type()
)
juniMplsTunnelProfileAffinityMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileAffinityMask.setStatus("current")


class _JuniMplsTunnelProfileSetupPriority_Type(JuniProfileCfgHoldingAndSetupPriorityRanges):
    """Custom type juniMplsTunnelProfileSetupPriority based on JuniProfileCfgHoldingAndSetupPriorityRanges"""
    defaultValue = 0


_JuniMplsTunnelProfileSetupPriority_Object = MibTableColumn
juniMplsTunnelProfileSetupPriority = _JuniMplsTunnelProfileSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 15),
    _JuniMplsTunnelProfileSetupPriority_Type()
)
juniMplsTunnelProfileSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileSetupPriority.setStatus("current")


class _JuniMplsTunnelProfileHoldingPriority_Type(JuniProfileCfgHoldingAndSetupPriorityRanges):
    """Custom type juniMplsTunnelProfileHoldingPriority based on JuniProfileCfgHoldingAndSetupPriorityRanges"""
    defaultValue = 0


_JuniMplsTunnelProfileHoldingPriority_Object = MibTableColumn
juniMplsTunnelProfileHoldingPriority = _JuniMplsTunnelProfileHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 16),
    _JuniMplsTunnelProfileHoldingPriority_Type()
)
juniMplsTunnelProfileHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileHoldingPriority.setStatus("current")


class _JuniMplsTunnelProfileRetryTimes_Type(JuniProfileCfgRetryTimesAndNorouteRanges):
    """Custom type juniMplsTunnelProfileRetryTimes based on JuniProfileCfgRetryTimesAndNorouteRanges"""
    defaultValue = 0


_JuniMplsTunnelProfileRetryTimes_Object = MibTableColumn
juniMplsTunnelProfileRetryTimes = _JuniMplsTunnelProfileRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 17),
    _JuniMplsTunnelProfileRetryTimes_Type()
)
juniMplsTunnelProfileRetryTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileRetryTimes.setStatus("current")


class _JuniMplsTunnelProfileRetryInterval_Type(JuniProfileCfgRetryIntervalAndNorouteRanges):
    """Custom type juniMplsTunnelProfileRetryInterval based on JuniProfileCfgRetryIntervalAndNorouteRanges"""
    defaultValue = 5


_JuniMplsTunnelProfileRetryInterval_Object = MibTableColumn
juniMplsTunnelProfileRetryInterval = _JuniMplsTunnelProfileRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 18),
    _JuniMplsTunnelProfileRetryInterval_Type()
)
juniMplsTunnelProfileRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileRetryInterval.setStatus("current")


class _JuniMplsTunnelProfileRetryTimesNoroute_Type(JuniProfileCfgRetryTimesAndNorouteRanges):
    """Custom type juniMplsTunnelProfileRetryTimesNoroute based on JuniProfileCfgRetryTimesAndNorouteRanges"""
    defaultValue = 0


_JuniMplsTunnelProfileRetryTimesNoroute_Object = MibTableColumn
juniMplsTunnelProfileRetryTimesNoroute = _JuniMplsTunnelProfileRetryTimesNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 19),
    _JuniMplsTunnelProfileRetryTimesNoroute_Type()
)
juniMplsTunnelProfileRetryTimesNoroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileRetryTimesNoroute.setStatus("current")


class _JuniMplsTunnelProfileRetryIntervalNoroute_Type(JuniProfileCfgRetryIntervalAndNorouteRanges):
    """Custom type juniMplsTunnelProfileRetryIntervalNoroute based on JuniProfileCfgRetryIntervalAndNorouteRanges"""
    defaultValue = 5


_JuniMplsTunnelProfileRetryIntervalNoroute_Object = MibTableColumn
juniMplsTunnelProfileRetryIntervalNoroute = _JuniMplsTunnelProfileRetryIntervalNoroute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 20),
    _JuniMplsTunnelProfileRetryIntervalNoroute_Type()
)
juniMplsTunnelProfileRetryIntervalNoroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileRetryIntervalNoroute.setStatus("current")


class _JuniMplsTunnelProfileVpnOuiNumber_Type(Integer32):
    """Custom type juniMplsTunnelProfileVpnOuiNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_JuniMplsTunnelProfileVpnOuiNumber_Type.__name__ = "Integer32"
_JuniMplsTunnelProfileVpnOuiNumber_Object = MibTableColumn
juniMplsTunnelProfileVpnOuiNumber = _JuniMplsTunnelProfileVpnOuiNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 21),
    _JuniMplsTunnelProfileVpnOuiNumber_Type()
)
juniMplsTunnelProfileVpnOuiNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileVpnOuiNumber.setStatus("obsolete")
_JuniMplsTunnelProfileVpnIndex_Type = IpAddress
_JuniMplsTunnelProfileVpnIndex_Object = MibTableColumn
juniMplsTunnelProfileVpnIndex = _JuniMplsTunnelProfileVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 22),
    _JuniMplsTunnelProfileVpnIndex_Type()
)
juniMplsTunnelProfileVpnIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileVpnIndex.setStatus("obsolete")
_JuniMplsTunnelProfileRowStatus_Type = RowStatus
_JuniMplsTunnelProfileRowStatus_Object = MibTableColumn
juniMplsTunnelProfileRowStatus = _JuniMplsTunnelProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 23),
    _JuniMplsTunnelProfileRowStatus_Type()
)
juniMplsTunnelProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileRowStatus.setStatus("current")


class _JuniMplsTunnelProfileTargetedDynamicTunnel_Type(TruthValue):
    """Custom type juniMplsTunnelProfileTargetedDynamicTunnel based on TruthValue"""


_JuniMplsTunnelProfileTargetedDynamicTunnel_Object = MibTableColumn
juniMplsTunnelProfileTargetedDynamicTunnel = _JuniMplsTunnelProfileTargetedDynamicTunnel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 1, 1, 1, 24),
    _JuniMplsTunnelProfileTargetedDynamicTunnel_Type()
)
juniMplsTunnelProfileTargetedDynamicTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileTargetedDynamicTunnel.setStatus("obsolete")
_JuniMplsTunnelProfileList_ObjectIdentity = ObjectIdentity
juniMplsTunnelProfileList = _JuniMplsTunnelProfileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2)
)
_JuniMplsTunnelProfilePathOptionTable_Object = MibTable
juniMplsTunnelProfilePathOptionTable = _JuniMplsTunnelProfilePathOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfilePathOptionTable.setStatus("current")
_JuniMplsTunnelProfilePathOptionEntry_Object = MibTableRow
juniMplsTunnelProfilePathOptionEntry = _JuniMplsTunnelProfilePathOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1)
)
juniMplsTunnelProfilePathOptionEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsTunnelProfileNamePathOption"),
    (0, "Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionNumber"),
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfilePathOptionEntry.setStatus("current")


class _JuniMplsTunnelProfileNamePathOption_Type(DisplayString):
    """Custom type juniMplsTunnelProfileNamePathOption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsTunnelProfileNamePathOption_Type.__name__ = "DisplayString"
_JuniMplsTunnelProfileNamePathOption_Object = MibTableColumn
juniMplsTunnelProfileNamePathOption = _JuniMplsTunnelProfileNamePathOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 1),
    _JuniMplsTunnelProfileNamePathOption_Type()
)
juniMplsTunnelProfileNamePathOption.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileNamePathOption.setStatus("current")


class _JuniMplsTunnelProfilePathOptionNumber_Type(Integer32):
    """Custom type juniMplsTunnelProfilePathOptionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JuniMplsTunnelProfilePathOptionNumber_Type.__name__ = "Integer32"
_JuniMplsTunnelProfilePathOptionNumber_Object = MibTableColumn
juniMplsTunnelProfilePathOptionNumber = _JuniMplsTunnelProfilePathOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 2),
    _JuniMplsTunnelProfilePathOptionNumber_Type()
)
juniMplsTunnelProfilePathOptionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsTunnelProfilePathOptionNumber.setStatus("current")


class _JuniMplsTunnelProfilePathOptionProtocol_Type(Integer32):
    """Custom type juniMplsTunnelProfilePathOptionProtocol based on Integer32"""
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


_JuniMplsTunnelProfilePathOptionProtocol_Type.__name__ = "Integer32"
_JuniMplsTunnelProfilePathOptionProtocol_Object = MibTableColumn
juniMplsTunnelProfilePathOptionProtocol = _JuniMplsTunnelProfilePathOptionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 3),
    _JuniMplsTunnelProfilePathOptionProtocol_Type()
)
juniMplsTunnelProfilePathOptionProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfilePathOptionProtocol.setStatus("current")
_JuniMplsTunnelProfilePathOptionLockdown_Type = TruthValue
_JuniMplsTunnelProfilePathOptionLockdown_Object = MibTableColumn
juniMplsTunnelProfilePathOptionLockdown = _JuniMplsTunnelProfilePathOptionLockdown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 4),
    _JuniMplsTunnelProfilePathOptionLockdown_Type()
)
juniMplsTunnelProfilePathOptionLockdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfilePathOptionLockdown.setStatus("current")


class _JuniMplsTunnelProfilePathOptionPathName_Type(DisplayString):
    """Custom type juniMplsTunnelProfilePathOptionPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsTunnelProfilePathOptionPathName_Type.__name__ = "DisplayString"
_JuniMplsTunnelProfilePathOptionPathName_Object = MibTableColumn
juniMplsTunnelProfilePathOptionPathName = _JuniMplsTunnelProfilePathOptionPathName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 5),
    _JuniMplsTunnelProfilePathOptionPathName_Type()
)
juniMplsTunnelProfilePathOptionPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfilePathOptionPathName.setStatus("current")


class _JuniMplsTunnelProfilePathOptionPathId_Type(Integer32):
    """Custom type juniMplsTunnelProfilePathOptionPathId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniMplsTunnelProfilePathOptionPathId_Type.__name__ = "Integer32"
_JuniMplsTunnelProfilePathOptionPathId_Object = MibTableColumn
juniMplsTunnelProfilePathOptionPathId = _JuniMplsTunnelProfilePathOptionPathId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 6),
    _JuniMplsTunnelProfilePathOptionPathId_Type()
)
juniMplsTunnelProfilePathOptionPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfilePathOptionPathId.setStatus("current")
_JuniMplsTunnelProfilePathOptionRowStatus_Type = RowStatus
_JuniMplsTunnelProfilePathOptionRowStatus_Object = MibTableColumn
juniMplsTunnelProfilePathOptionRowStatus = _JuniMplsTunnelProfilePathOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 1, 1, 7),
    _JuniMplsTunnelProfilePathOptionRowStatus_Type()
)
juniMplsTunnelProfilePathOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfilePathOptionRowStatus.setStatus("current")
_JuniMplsTunnelProfileDynamicEndpointTable_Object = MibTable
juniMplsTunnelProfileDynamicEndpointTable = _JuniMplsTunnelProfileDynamicEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfileDynamicEndpointTable.setStatus("current")
_JuniMplsTunnelProfileDynamicEndpointEntry_Object = MibTableRow
juniMplsTunnelProfileDynamicEndpointEntry = _JuniMplsTunnelProfileDynamicEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1)
)
juniMplsTunnelProfileDynamicEndpointEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsTunnelProfileNameDynamicEndpoint"),
    (0, "Juniper-MPLS-MIB", "juniMplsTunnelProfileDynamicEndpointType"),
    (0, "Juniper-MPLS-MIB", "juniMplsTunnelProfileDynamicEndpointPolicyListType"),
    (0, "Juniper-MPLS-MIB", "juniMplsTunnelProfileDynamicEndpointListName"),
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfileDynamicEndpointEntry.setStatus("current")


class _JuniMplsTunnelProfileNameDynamicEndpoint_Type(DisplayString):
    """Custom type juniMplsTunnelProfileNameDynamicEndpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsTunnelProfileNameDynamicEndpoint_Type.__name__ = "DisplayString"
_JuniMplsTunnelProfileNameDynamicEndpoint_Object = MibTableColumn
juniMplsTunnelProfileNameDynamicEndpoint = _JuniMplsTunnelProfileNameDynamicEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1, 1),
    _JuniMplsTunnelProfileNameDynamicEndpoint_Type()
)
juniMplsTunnelProfileNameDynamicEndpoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileNameDynamicEndpoint.setStatus("current")


class _JuniMplsTunnelProfileDynamicEndpointType_Type(Integer32):
    """Custom type juniMplsTunnelProfileDynamicEndpointType based on Integer32"""
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


_JuniMplsTunnelProfileDynamicEndpointType_Type.__name__ = "Integer32"
_JuniMplsTunnelProfileDynamicEndpointType_Object = MibTableColumn
juniMplsTunnelProfileDynamicEndpointType = _JuniMplsTunnelProfileDynamicEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1, 2),
    _JuniMplsTunnelProfileDynamicEndpointType_Type()
)
juniMplsTunnelProfileDynamicEndpointType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileDynamicEndpointType.setStatus("current")


class _JuniMplsTunnelProfileDynamicEndpointPolicyListType_Type(Integer32):
    """Custom type juniMplsTunnelProfileDynamicEndpointPolicyListType based on Integer32"""
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


_JuniMplsTunnelProfileDynamicEndpointPolicyListType_Type.__name__ = "Integer32"
_JuniMplsTunnelProfileDynamicEndpointPolicyListType_Object = MibTableColumn
juniMplsTunnelProfileDynamicEndpointPolicyListType = _JuniMplsTunnelProfileDynamicEndpointPolicyListType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1, 3),
    _JuniMplsTunnelProfileDynamicEndpointPolicyListType_Type()
)
juniMplsTunnelProfileDynamicEndpointPolicyListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileDynamicEndpointPolicyListType.setStatus("current")


class _JuniMplsTunnelProfileDynamicEndpointListName_Type(DisplayString):
    """Custom type juniMplsTunnelProfileDynamicEndpointListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsTunnelProfileDynamicEndpointListName_Type.__name__ = "DisplayString"
_JuniMplsTunnelProfileDynamicEndpointListName_Object = MibTableColumn
juniMplsTunnelProfileDynamicEndpointListName = _JuniMplsTunnelProfileDynamicEndpointListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1, 4),
    _JuniMplsTunnelProfileDynamicEndpointListName_Type()
)
juniMplsTunnelProfileDynamicEndpointListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileDynamicEndpointListName.setStatus("current")
_JuniMplsTunnelProfileDynamicEndpointRowStatus_Type = RowStatus
_JuniMplsTunnelProfileDynamicEndpointRowStatus_Object = MibTableColumn
juniMplsTunnelProfileDynamicEndpointRowStatus = _JuniMplsTunnelProfileDynamicEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 2, 1, 5),
    _JuniMplsTunnelProfileDynamicEndpointRowStatus_Type()
)
juniMplsTunnelProfileDynamicEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileDynamicEndpointRowStatus.setStatus("current")
_JuniMplsTunnelProfileTunnelEndpointTable_Object = MibTable
juniMplsTunnelProfileTunnelEndpointTable = _JuniMplsTunnelProfileTunnelEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfileTunnelEndpointTable.setStatus("current")
_JuniMplsTunnelProfileTunnelEndpointEntry_Object = MibTableRow
juniMplsTunnelProfileTunnelEndpointEntry = _JuniMplsTunnelProfileTunnelEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3, 1)
)
juniMplsTunnelProfileTunnelEndpointEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsTunnelProfileNameTunnelEndpoint"),
    (0, "Juniper-MPLS-MIB", "juniMplsTunnelProfileTunnelEndpointAddress"),
    (0, "Juniper-MPLS-MIB", "juniMplsTunnelProfileTunnelEndpointDstMask"),
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfileTunnelEndpointEntry.setStatus("current")


class _JuniMplsTunnelProfileNameTunnelEndpoint_Type(DisplayString):
    """Custom type juniMplsTunnelProfileNameTunnelEndpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsTunnelProfileNameTunnelEndpoint_Type.__name__ = "DisplayString"
_JuniMplsTunnelProfileNameTunnelEndpoint_Object = MibTableColumn
juniMplsTunnelProfileNameTunnelEndpoint = _JuniMplsTunnelProfileNameTunnelEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3, 1, 1),
    _JuniMplsTunnelProfileNameTunnelEndpoint_Type()
)
juniMplsTunnelProfileNameTunnelEndpoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileNameTunnelEndpoint.setStatus("current")
_JuniMplsTunnelProfileTunnelEndpointAddress_Type = IpAddress
_JuniMplsTunnelProfileTunnelEndpointAddress_Object = MibTableColumn
juniMplsTunnelProfileTunnelEndpointAddress = _JuniMplsTunnelProfileTunnelEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3, 1, 2),
    _JuniMplsTunnelProfileTunnelEndpointAddress_Type()
)
juniMplsTunnelProfileTunnelEndpointAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileTunnelEndpointAddress.setStatus("current")
_JuniMplsTunnelProfileTunnelEndpointDstMask_Type = IpAddress
_JuniMplsTunnelProfileTunnelEndpointDstMask_Object = MibTableColumn
juniMplsTunnelProfileTunnelEndpointDstMask = _JuniMplsTunnelProfileTunnelEndpointDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3, 1, 3),
    _JuniMplsTunnelProfileTunnelEndpointDstMask_Type()
)
juniMplsTunnelProfileTunnelEndpointDstMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileTunnelEndpointDstMask.setStatus("current")
_JuniMplsTunnelProfileTunnelEndpointRowStatus_Type = RowStatus
_JuniMplsTunnelProfileTunnelEndpointRowStatus_Object = MibTableColumn
juniMplsTunnelProfileTunnelEndpointRowStatus = _JuniMplsTunnelProfileTunnelEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 4, 2, 3, 1, 4),
    _JuniMplsTunnelProfileTunnelEndpointRowStatus_Type()
)
juniMplsTunnelProfileTunnelEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsTunnelProfileTunnelEndpointRowStatus.setStatus("current")
_JuniMplsExplicitPath_ObjectIdentity = ObjectIdentity
juniMplsExplicitPath = _JuniMplsExplicitPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5)
)
_JuniMplsExplicitPathGroup_ObjectIdentity = ObjectIdentity
juniMplsExplicitPathGroup = _JuniMplsExplicitPathGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1)
)
_JuniMplsExplicitPathTable_Object = MibTable
juniMplsExplicitPathTable = _JuniMplsExplicitPathTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    juniMplsExplicitPathTable.setStatus("current")
_JuniMplsExplicitPathEntry_Object = MibTableRow
juniMplsExplicitPathEntry = _JuniMplsExplicitPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 1, 1)
)
juniMplsExplicitPathEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsExplicitPathName"),
)
if mibBuilder.loadTexts:
    juniMplsExplicitPathEntry.setStatus("current")


class _JuniMplsExplicitPathName_Type(DisplayString):
    """Custom type juniMplsExplicitPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsExplicitPathName_Type.__name__ = "DisplayString"
_JuniMplsExplicitPathName_Object = MibTableColumn
juniMplsExplicitPathName = _JuniMplsExplicitPathName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 1, 1, 1),
    _JuniMplsExplicitPathName_Type()
)
juniMplsExplicitPathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsExplicitPathName.setStatus("current")


class _JuniMplsExplicitPathAdminState_Type(Integer32):
    """Custom type juniMplsExplicitPathAdminState based on Integer32"""
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


_JuniMplsExplicitPathAdminState_Type.__name__ = "Integer32"
_JuniMplsExplicitPathAdminState_Object = MibTableColumn
juniMplsExplicitPathAdminState = _JuniMplsExplicitPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 1, 1, 2),
    _JuniMplsExplicitPathAdminState_Type()
)
juniMplsExplicitPathAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsExplicitPathAdminState.setStatus("current")
_JuniMplsExplicitPathRowStatus_Type = RowStatus
_JuniMplsExplicitPathRowStatus_Object = MibTableColumn
juniMplsExplicitPathRowStatus = _JuniMplsExplicitPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 1, 1, 3),
    _JuniMplsExplicitPathRowStatus_Type()
)
juniMplsExplicitPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsExplicitPathRowStatus.setStatus("current")
_JuniMplsExplicitPathNodeTable_Object = MibTable
juniMplsExplicitPathNodeTable = _JuniMplsExplicitPathNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    juniMplsExplicitPathNodeTable.setStatus("current")
_JuniMplsExplicitPathNodeEntry_Object = MibTableRow
juniMplsExplicitPathNodeEntry = _JuniMplsExplicitPathNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1)
)
juniMplsExplicitPathNodeEntry.setIndexNames(
    (0, "Juniper-MPLS-MIB", "juniMplsExplicitPathNodeName"),
    (0, "Juniper-MPLS-MIB", "juniMplsExplicitPathNodeIndexNumber"),
)
if mibBuilder.loadTexts:
    juniMplsExplicitPathNodeEntry.setStatus("current")


class _JuniMplsExplicitPathNodeName_Type(DisplayString):
    """Custom type juniMplsExplicitPathNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_JuniMplsExplicitPathNodeName_Type.__name__ = "DisplayString"
_JuniMplsExplicitPathNodeName_Object = MibTableColumn
juniMplsExplicitPathNodeName = _JuniMplsExplicitPathNodeName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 1),
    _JuniMplsExplicitPathNodeName_Type()
)
juniMplsExplicitPathNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsExplicitPathNodeName.setStatus("current")


class _JuniMplsExplicitPathNodeIndexNumber_Type(Integer32):
    """Custom type juniMplsExplicitPathNodeIndexNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniMplsExplicitPathNodeIndexNumber_Type.__name__ = "Integer32"
_JuniMplsExplicitPathNodeIndexNumber_Object = MibTableColumn
juniMplsExplicitPathNodeIndexNumber = _JuniMplsExplicitPathNodeIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 2),
    _JuniMplsExplicitPathNodeIndexNumber_Type()
)
juniMplsExplicitPathNodeIndexNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniMplsExplicitPathNodeIndexNumber.setStatus("current")


class _JuniMplsExplicitPathNodeLoose_Type(TruthValue):
    """Custom type juniMplsExplicitPathNodeLoose based on TruthValue"""


_JuniMplsExplicitPathNodeLoose_Object = MibTableColumn
juniMplsExplicitPathNodeLoose = _JuniMplsExplicitPathNodeLoose_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 3),
    _JuniMplsExplicitPathNodeLoose_Type()
)
juniMplsExplicitPathNodeLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsExplicitPathNodeLoose.setStatus("current")
_JuniMplsExplicitPathNodeHopAddress_Type = IpAddress
_JuniMplsExplicitPathNodeHopAddress_Object = MibTableColumn
juniMplsExplicitPathNodeHopAddress = _JuniMplsExplicitPathNodeHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 4),
    _JuniMplsExplicitPathNodeHopAddress_Type()
)
juniMplsExplicitPathNodeHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsExplicitPathNodeHopAddress.setStatus("current")


class _JuniMplsExplicitPathNodeHopAddressMask_Type(IpAddress):
    """Custom type juniMplsExplicitPathNodeHopAddressMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_JuniMplsExplicitPathNodeHopAddressMask_Object = MibTableColumn
juniMplsExplicitPathNodeHopAddressMask = _JuniMplsExplicitPathNodeHopAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 5),
    _JuniMplsExplicitPathNodeHopAddressMask_Type()
)
juniMplsExplicitPathNodeHopAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsExplicitPathNodeHopAddressMask.setStatus("current")
_JuniMplsExplicitPathNodeRowStatus_Type = RowStatus
_JuniMplsExplicitPathNodeRowStatus_Object = MibTableColumn
juniMplsExplicitPathNodeRowStatus = _JuniMplsExplicitPathNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 1, 5, 1, 2, 1, 6),
    _JuniMplsExplicitPathNodeRowStatus_Type()
)
juniMplsExplicitPathNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMplsExplicitPathNodeRowStatus.setStatus("current")
_JuniMplsConformance_ObjectIdentity = ObjectIdentity
juniMplsConformance = _JuniMplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2)
)
_JuniMplsCompliances_ObjectIdentity = ObjectIdentity
juniMplsCompliances = _JuniMplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 1)
)
_JuniMplsConfGroups_ObjectIdentity = ObjectIdentity
juniMplsConfGroups = _JuniMplsConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2)
)

# Managed Objects groups

juniMplsLsrGlobalConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 1)
)
juniMplsLsrGlobalConfGroup.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsGroupMplsEnable"),
        ("Juniper-MPLS-MIB", "juniMplsGroupReopTimer"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLabelRangeLow"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLabelRangeHigh"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpSessionRetries"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpSessionRetryTimer"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenIpProfileName"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntf"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntf"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdp"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspLabelDistCtrlMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpAdvHostOnly"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLsrState"),
        ("Juniper-MPLS-MIB", "juniMplsGroupReopNow"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpTargetedHelloSendMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpTargetedHelloReceiveMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLabelAdverListMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpProfileHelloHoldTime"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpProfileCrLdpAdminState"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpProfileRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsGroupRsvpProfileRefreshPeriod"),
        ("Juniper-MPLS-MIB", "juniMplsGroupRsvpProfileCleanupTimeoutFactor"),
        ("Juniper-MPLS-MIB", "juniMplsGroupRsvpProfileRowStatus"))
)
if mibBuilder.loadTexts:
    juniMplsLsrGlobalConfGroup.setStatus("obsolete")

juniMplsMajorLayerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 2)
)
juniMplsMajorLayerConfGroup.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsIfMajorNextIfIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLowerIfIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpProfileName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpVpiStart"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpVpiStop"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpVciStart"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpVciStop"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpProfileName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpVpiStart"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpVpiStop"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpVciStart"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpVciStop"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLabelSpaceType"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorOpState"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorCrLdpAdminState"))
)
if mibBuilder.loadTexts:
    juniMplsMajorLayerConfGroup.setStatus("obsolete")

juniMplsMinorLayerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 3)
)
juniMplsMinorLayerConfGroup.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsIfMinorNextIfIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorLowerIfIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorEndpointAddress"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorEndpointDstMask"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelMetricMode"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAbsoluteTunnelMetric"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorRelativeTunnelMetric"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorLabelDistProto"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAnnounceToOspf"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAnnounceToIsis"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAnnounceToBgp"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorBandwidth"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAffinity"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAffinityMask"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorSetupPriority"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorHoldingPriority"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorBaseTunnelName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorVpnOuiNumber"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorVpnIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelOpState"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTargetedDynamicTunnel"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorReoptimization"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionProtocol"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionLockdown"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionPathName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionPathId"))
)
if mibBuilder.loadTexts:
    juniMplsMinorLayerConfGroup.setStatus("obsolete")

juniMplsTunnelProfileConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 4)
)
juniMplsTunnelProfileConfGroup.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsTunnelProfileAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileBaseTunnelName"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileIpProfileName"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileLabelDistProto"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAnnounceToOspf"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAnnounceToIsis"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAnnounceToBgp"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileMetricMode"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAbsoluteMetric"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRelativeMetric"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileBandwidth"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAffinity"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAffinityMask"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileSetupPriority"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileHoldingPriority"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileVpnOuiNumber"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileVpnIndex"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileTargetedDynamicTunnel"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionProtocol"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionLockdown"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionPathName"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionPathId"))
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfileConfGroup.setStatus("obsolete")

juniMplsExplicitPathConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 5)
)
juniMplsExplicitPathConfGroup.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsExplicitPathAdminState"),
        ("Juniper-MPLS-MIB", "juniMplsExplicitPathRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsExplicitPathNodeLoose"),
        ("Juniper-MPLS-MIB", "juniMplsExplicitPathNodeHopAddress"),
        ("Juniper-MPLS-MIB", "juniMplsExplicitPathNodeHopAddressMask"),
        ("Juniper-MPLS-MIB", "juniMplsExplicitPathNodeRowStatus"))
)
if mibBuilder.loadTexts:
    juniMplsExplicitPathConfGroup.setStatus("current")

juniMplsMinorLayerConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 6)
)
juniMplsMinorLayerConfGroup2.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsIfMinorNextIfIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorLowerIfIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorEndpointAddress"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorEndpointDstMask"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelMetricMode"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAbsoluteTunnelMetric"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorRelativeTunnelMetric"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorLabelDistProto"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAnnounceToOspf"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAnnounceToIsis"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAnnounceToBgp"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorBandwidth"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAffinity"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAffinityMask"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorSetupPriority"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorHoldingPriority"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorBaseTunnelName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorVpnOuiNumber"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorVpnIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelOpState"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTargetedDynamicTunnel"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorReoptimization"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionProtocol"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionLockdown"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionPathName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionPathId"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionRowStatus"))
)
if mibBuilder.loadTexts:
    juniMplsMinorLayerConfGroup2.setStatus("obsolete")

juniMplsTunnelProfileConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 7)
)
juniMplsTunnelProfileConfGroup2.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsTunnelProfileAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileBaseTunnelName"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileIpProfileName"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileLabelDistProto"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAnnounceToOspf"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAnnounceToIsis"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAnnounceToBgp"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileMetricMode"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAbsoluteMetric"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRelativeMetric"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileBandwidth"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAffinity"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAffinityMask"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileSetupPriority"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileHoldingPriority"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileVpnOuiNumber"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileVpnIndex"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileTargetedDynamicTunnel"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionProtocol"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionLockdown"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionPathName"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionPathId"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileDynamicEndpointRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileTunnelEndpointRowStatus"))
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfileConfGroup2.setStatus("obsolete")

juniMplsLsrGlobalConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 8)
)
juniMplsLsrGlobalConfGroup2.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsGroupMplsEnable"),
        ("Juniper-MPLS-MIB", "juniMplsGroupReopTimer"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLabelRangeLow"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLabelRangeHigh"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpSessionRetries"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpSessionRetryTimer"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenIpProfileName"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntf"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntf"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdp"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspLabelDistCtrlMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpAdvHostOnly"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLsrState"),
        ("Juniper-MPLS-MIB", "juniMplsGroupReopNow"),
        ("Juniper-MPLS-MIB", "juniMplsGroupIpTtlPropagate"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpTargetedHelloSendMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpTargetedHelloReceiveMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLabelAdverListMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpProfileHelloHoldTime"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpProfileCrLdpAdminState"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpProfileRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsGroupRsvpProfileRefreshPeriod"),
        ("Juniper-MPLS-MIB", "juniMplsGroupRsvpProfileCleanupTimeoutFactor"),
        ("Juniper-MPLS-MIB", "juniMplsGroupRsvpProfileRowStatus"))
)
if mibBuilder.loadTexts:
    juniMplsLsrGlobalConfGroup2.setStatus("obsolete")

juniMplsLsrGlobalConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 9)
)
juniMplsLsrGlobalConfGroup3.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsGroupMplsEnable"),
        ("Juniper-MPLS-MIB", "juniMplsGroupReopTimer"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLabelRangeLow"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLabelRangeHigh"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpSessionRetries"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpSessionRetryTimer"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenIpProfileName"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntf"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntf"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList"),
        ("Juniper-MPLS-MIB", "juniMplsGroupTopologyDrivenLdp"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLspLabelDistCtrlMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpAdvHostOnly"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLsrState"),
        ("Juniper-MPLS-MIB", "juniMplsGroupReopNow"),
        ("Juniper-MPLS-MIB", "juniMplsGroupIpTtlPropagate"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpTargetedHelloSendMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpTargetedHelloReceiveMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLabelAdverListMode"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpProfileHelloHoldTime"),
        ("Juniper-MPLS-MIB", "juniMplsGroupLdpProfileRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsGroupRsvpProfileRefreshPeriod"),
        ("Juniper-MPLS-MIB", "juniMplsGroupRsvpProfileCleanupTimeoutFactor"),
        ("Juniper-MPLS-MIB", "juniMplsGroupRsvpProfileRowStatus"))
)
if mibBuilder.loadTexts:
    juniMplsLsrGlobalConfGroup3.setStatus("current")

juniMplsMajorLayerConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 10)
)
juniMplsMajorLayerConfGroup2.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsIfMajorNextIfIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLowerIfIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpProfileName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpVpiStart"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpVpiStop"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpVciStart"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLdpVciStop"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpProfileName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpVpiStart"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpVpiStop"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpVciStart"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorRsvpVciStop"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorLabelSpaceType"),
        ("Juniper-MPLS-MIB", "juniMplsIfMajorOpState"))
)
if mibBuilder.loadTexts:
    juniMplsMajorLayerConfGroup2.setStatus("current")

juniMplsMinorLayerConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 11)
)
juniMplsMinorLayerConfGroup3.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsIfMinorNextIfIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorLowerIfIndex"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorEndpointAddress"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorEndpointDstMask"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelMetricMode"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAbsoluteTunnelMetric"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorRelativeTunnelMetric"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAnnounceToOspf"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAnnounceToIsis"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAnnounceToBgp"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorBandwidth"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAffinity"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorAffinityMask"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorSetupPriority"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorHoldingPriority"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorTunnelOpState"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorReoptimization"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionProtocol"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionLockdown"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionPathName"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionPathId"),
        ("Juniper-MPLS-MIB", "juniMplsIfMinorPathOptionRowStatus"))
)
if mibBuilder.loadTexts:
    juniMplsMinorLayerConfGroup3.setStatus("current")

juniMplsTunnelProfileConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 2, 12)
)
juniMplsTunnelProfileConfGroup3.setObjects(
      *(("Juniper-MPLS-MIB", "juniMplsTunnelProfileAdminStatus"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileIpProfileName"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAnnounceToOspf"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAnnounceToIsis"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAnnounceToBgp"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileMetricMode"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAbsoluteMetric"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRelativeMetric"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileBandwidth"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAffinity"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileAffinityMask"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileSetupPriority"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileHoldingPriority"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryTimes"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryInterval"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryTimesNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRetryIntervalNoroute"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionProtocol"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionLockdown"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionPathName"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionPathId"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfilePathOptionRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileDynamicEndpointRowStatus"),
        ("Juniper-MPLS-MIB", "juniMplsTunnelProfileTunnelEndpointRowStatus"))
)
if mibBuilder.loadTexts:
    juniMplsTunnelProfileConfGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniMplsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniMplsCompliance.setStatus(
        "obsolete"
    )

juniMplsCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniMplsCompliance2.setStatus(
        "obsolete"
    )

juniMplsCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniMplsCompliance3.setStatus(
        "obsolete"
    )

juniMplsCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54, 2, 1, 4)
)
if mibBuilder.loadTexts:
    juniMplsCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-MPLS-MIB",
    **{"JuniMajorCfgVciRanges": JuniMajorCfgVciRanges,
       "JuniMajorCfgVpiRanges": JuniMajorCfgVpiRanges,
       "JuniMinorCfgBWRanges": JuniMinorCfgBWRanges,
       "JuniMinorCfgHoldingAndSetupPriorityRanges": JuniMinorCfgHoldingAndSetupPriorityRanges,
       "JuniMinorCfgRetryTimesAndNorouteRanges": JuniMinorCfgRetryTimesAndNorouteRanges,
       "JuniMinorCfgRetryIntervalAndNorouteRanges": JuniMinorCfgRetryIntervalAndNorouteRanges,
       "JuniProfileCfgBWRanges": JuniProfileCfgBWRanges,
       "JuniProfileCfgHoldingAndSetupPriorityRanges": JuniProfileCfgHoldingAndSetupPriorityRanges,
       "JuniProfileCfgRetryTimesAndNorouteRanges": JuniProfileCfgRetryTimesAndNorouteRanges,
       "JuniProfileCfgRetryIntervalAndNorouteRanges": JuniProfileCfgRetryIntervalAndNorouteRanges,
       "juniMplsMIB": juniMplsMIB,
       "juniMplsObjects": juniMplsObjects,
       "juniMplsLsrGlobalConfig": juniMplsLsrGlobalConfig,
       "juniMplsGroup": juniMplsGroup,
       "juniMplsGroupMplsEnable": juniMplsGroupMplsEnable,
       "juniMplsGroupReopTimer": juniMplsGroupReopTimer,
       "juniMplsGroupLabelRangeLow": juniMplsGroupLabelRangeLow,
       "juniMplsGroupLabelRangeHigh": juniMplsGroupLabelRangeHigh,
       "juniMplsGroupLspRetryTimesNoroute": juniMplsGroupLspRetryTimesNoroute,
       "juniMplsGroupLspRetryIntervalNoroute": juniMplsGroupLspRetryIntervalNoroute,
       "juniMplsGroupLspRetryTimes": juniMplsGroupLspRetryTimes,
       "juniMplsGroupLspRetryInterval": juniMplsGroupLspRetryInterval,
       "juniMplsGroupLdpRetryTimesNoroute": juniMplsGroupLdpRetryTimesNoroute,
       "juniMplsGroupLdpRetryIntervalNoroute": juniMplsGroupLdpRetryIntervalNoroute,
       "juniMplsGroupLdpRetryTimes": juniMplsGroupLdpRetryTimes,
       "juniMplsGroupLdpRetryInterval": juniMplsGroupLdpRetryInterval,
       "juniMplsGroupLdpSessionRetries": juniMplsGroupLdpSessionRetries,
       "juniMplsGroupLdpSessionRetryTimer": juniMplsGroupLdpSessionRetryTimer,
       "juniMplsGroupTopologyDrivenIpProfileName": juniMplsGroupTopologyDrivenIpProfileName,
       "juniMplsGroupTopologyDrivenLdpEgressIpIntf": juniMplsGroupTopologyDrivenLdpEgressIpIntf,
       "juniMplsGroupTopologyDrivenLdpIngressIpIntf": juniMplsGroupTopologyDrivenLdpIngressIpIntf,
       "juniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly": juniMplsGroupTopologyDrivenLdpEgressIpIntfHostOnly,
       "juniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly": juniMplsGroupTopologyDrivenLdpIngressIpIntfHostOnly,
       "juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType": juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyListType,
       "juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType": juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyListType,
       "juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList": juniMplsGroupTopologyDrivenLdpEgressIpIntfPolicyList,
       "juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList": juniMplsGroupTopologyDrivenLdpIngressIpIntfPolicyList,
       "juniMplsGroupTopologyDrivenLdp": juniMplsGroupTopologyDrivenLdp,
       "juniMplsGroupLspLabelDistCtrlMode": juniMplsGroupLspLabelDistCtrlMode,
       "juniMplsGroupLdpAdvHostOnly": juniMplsGroupLdpAdvHostOnly,
       "juniMplsGroupLsrState": juniMplsGroupLsrState,
       "juniMplsGroupReopNow": juniMplsGroupReopNow,
       "juniMplsGroupIpTtlPropagate": juniMplsGroupIpTtlPropagate,
       "juniMplsGroupList": juniMplsGroupList,
       "juniMplsGroupTargetedHelloSendTable": juniMplsGroupTargetedHelloSendTable,
       "juniMplsGroupTargetedHelloSendEntry": juniMplsGroupTargetedHelloSendEntry,
       "juniMplsGroupTargetedHelloSendAddress": juniMplsGroupTargetedHelloSendAddress,
       "juniMplsGroupLdpTargetedHelloSendMode": juniMplsGroupLdpTargetedHelloSendMode,
       "juniMplsGroupTargetedHelloReceiveTable": juniMplsGroupTargetedHelloReceiveTable,
       "juniMplsGroupTargetedHelloReceiveEntry": juniMplsGroupTargetedHelloReceiveEntry,
       "juniMplsGroupTargetedHelloReceiveAddress": juniMplsGroupTargetedHelloReceiveAddress,
       "juniMplsGroupLdpTargetedHelloReceiveMode": juniMplsGroupLdpTargetedHelloReceiveMode,
       "juniMplsGroupLdpLabelAdverRouteListTable": juniMplsGroupLdpLabelAdverRouteListTable,
       "juniMplsGroupLdpLabelAdverRouteListEntry": juniMplsGroupLdpLabelAdverRouteListEntry,
       "juniMplsGroupLdpLabelAdverRouteListName": juniMplsGroupLdpLabelAdverRouteListName,
       "juniMplsGroupLdpLabelAdverNbrListName": juniMplsGroupLdpLabelAdverNbrListName,
       "juniMplsGroupLabelAdverListMode": juniMplsGroupLabelAdverListMode,
       "juniMplsGroupLdpProfileTable": juniMplsGroupLdpProfileTable,
       "juniMplsGroupLdpProfileEntry": juniMplsGroupLdpProfileEntry,
       "juniMplsGroupLdpProfileName": juniMplsGroupLdpProfileName,
       "juniMplsGroupLdpProfileHelloHoldTime": juniMplsGroupLdpProfileHelloHoldTime,
       "juniMplsGroupLdpProfileCrLdpAdminState": juniMplsGroupLdpProfileCrLdpAdminState,
       "juniMplsGroupLdpProfileRowStatus": juniMplsGroupLdpProfileRowStatus,
       "juniMplsGroupRsvpProfileTable": juniMplsGroupRsvpProfileTable,
       "juniMplsGroupRsvpProfileEntry": juniMplsGroupRsvpProfileEntry,
       "juniMplsGroupRsvpProfileName": juniMplsGroupRsvpProfileName,
       "juniMplsGroupRsvpProfileRefreshPeriod": juniMplsGroupRsvpProfileRefreshPeriod,
       "juniMplsGroupRsvpProfileCleanupTimeoutFactor": juniMplsGroupRsvpProfileCleanupTimeoutFactor,
       "juniMplsGroupRsvpProfileRowStatus": juniMplsGroupRsvpProfileRowStatus,
       "juniMplsMajorLayer": juniMplsMajorLayer,
       "juniMplsIfMajorLayer": juniMplsIfMajorLayer,
       "juniMplsIfMajorNextIfIndex": juniMplsIfMajorNextIfIndex,
       "juniMplsIfMajorTable": juniMplsIfMajorTable,
       "juniMplsIfMajorEntry": juniMplsIfMajorEntry,
       "juniMplsIfMajorIndex": juniMplsIfMajorIndex,
       "juniMplsIfMajorRowStatus": juniMplsIfMajorRowStatus,
       "juniMplsIfMajorLowerIfIndex": juniMplsIfMajorLowerIfIndex,
       "juniMplsIfMajorAdminStatus": juniMplsIfMajorAdminStatus,
       "juniMplsIfMajorLdpAdminStatus": juniMplsIfMajorLdpAdminStatus,
       "juniMplsIfMajorLdpProfileName": juniMplsIfMajorLdpProfileName,
       "juniMplsIfMajorLdpVpiStart": juniMplsIfMajorLdpVpiStart,
       "juniMplsIfMajorLdpVpiStop": juniMplsIfMajorLdpVpiStop,
       "juniMplsIfMajorLdpVciStart": juniMplsIfMajorLdpVciStart,
       "juniMplsIfMajorLdpVciStop": juniMplsIfMajorLdpVciStop,
       "juniMplsIfMajorRsvpAdminStatus": juniMplsIfMajorRsvpAdminStatus,
       "juniMplsIfMajorRsvpProfileName": juniMplsIfMajorRsvpProfileName,
       "juniMplsIfMajorRsvpVpiStart": juniMplsIfMajorRsvpVpiStart,
       "juniMplsIfMajorRsvpVpiStop": juniMplsIfMajorRsvpVpiStop,
       "juniMplsIfMajorRsvpVciStart": juniMplsIfMajorRsvpVciStart,
       "juniMplsIfMajorRsvpVciStop": juniMplsIfMajorRsvpVciStop,
       "juniMplsIfMajorLabelSpaceType": juniMplsIfMajorLabelSpaceType,
       "juniMplsIfMajorOpState": juniMplsIfMajorOpState,
       "juniMplsIfMajorCrLdpAdminState": juniMplsIfMajorCrLdpAdminState,
       "juniMplsMinorLayer": juniMplsMinorLayer,
       "juniMplsIfMinorLayer": juniMplsIfMinorLayer,
       "juniMplsIfMinorNextIfIndex": juniMplsIfMinorNextIfIndex,
       "juniMplsIfMinorTable": juniMplsIfMinorTable,
       "juniMplsIfMinorEntry": juniMplsIfMinorEntry,
       "juniMplsIfMinorIndex": juniMplsIfMinorIndex,
       "juniMplsIfMinorRowStatus": juniMplsIfMinorRowStatus,
       "juniMplsIfMinorLowerIfIndex": juniMplsIfMinorLowerIfIndex,
       "juniMplsIfMinorAdminStatus": juniMplsIfMinorAdminStatus,
       "juniMplsIfMinorEndpointAddress": juniMplsIfMinorEndpointAddress,
       "juniMplsIfMinorEndpointDstMask": juniMplsIfMinorEndpointDstMask,
       "juniMplsIfMinorTunnelMetricMode": juniMplsIfMinorTunnelMetricMode,
       "juniMplsIfMinorAbsoluteTunnelMetric": juniMplsIfMinorAbsoluteTunnelMetric,
       "juniMplsIfMinorRelativeTunnelMetric": juniMplsIfMinorRelativeTunnelMetric,
       "juniMplsIfMinorLabelDistProto": juniMplsIfMinorLabelDistProto,
       "juniMplsIfMinorAnnounceToOspf": juniMplsIfMinorAnnounceToOspf,
       "juniMplsIfMinorAnnounceToIsis": juniMplsIfMinorAnnounceToIsis,
       "juniMplsIfMinorAnnounceToBgp": juniMplsIfMinorAnnounceToBgp,
       "juniMplsIfMinorBandwidth": juniMplsIfMinorBandwidth,
       "juniMplsIfMinorAffinity": juniMplsIfMinorAffinity,
       "juniMplsIfMinorAffinityMask": juniMplsIfMinorAffinityMask,
       "juniMplsIfMinorSetupPriority": juniMplsIfMinorSetupPriority,
       "juniMplsIfMinorHoldingPriority": juniMplsIfMinorHoldingPriority,
       "juniMplsIfMinorTunnelName": juniMplsIfMinorTunnelName,
       "juniMplsIfMinorTunnelRetryTimes": juniMplsIfMinorTunnelRetryTimes,
       "juniMplsIfMinorTunnelRetryInterval": juniMplsIfMinorTunnelRetryInterval,
       "juniMplsIfMinorTunnelRetryTimesNoroute": juniMplsIfMinorTunnelRetryTimesNoroute,
       "juniMplsIfMinorTunnelRetryIntervalNoroute": juniMplsIfMinorTunnelRetryIntervalNoroute,
       "juniMplsIfMinorBaseTunnelName": juniMplsIfMinorBaseTunnelName,
       "juniMplsIfMinorVpnOuiNumber": juniMplsIfMinorVpnOuiNumber,
       "juniMplsIfMinorVpnIndex": juniMplsIfMinorVpnIndex,
       "juniMplsIfMinorTunnelOpState": juniMplsIfMinorTunnelOpState,
       "juniMplsIfMinorTargetedDynamicTunnel": juniMplsIfMinorTargetedDynamicTunnel,
       "juniMplsIfMinorReoptimization": juniMplsIfMinorReoptimization,
       "juniMplsMinorLayerList": juniMplsMinorLayerList,
       "juniMplsIfMinorPathOptionTable": juniMplsIfMinorPathOptionTable,
       "juniMplsIfMinorPathOptionEntry": juniMplsIfMinorPathOptionEntry,
       "juniMplsIfMinorPathOptionIndex": juniMplsIfMinorPathOptionIndex,
       "juniMplsIfMinorPathOptionNumber": juniMplsIfMinorPathOptionNumber,
       "juniMplsIfMinorPathOptionProtocol": juniMplsIfMinorPathOptionProtocol,
       "juniMplsIfMinorPathOptionLockdown": juniMplsIfMinorPathOptionLockdown,
       "juniMplsIfMinorPathOptionPathName": juniMplsIfMinorPathOptionPathName,
       "juniMplsIfMinorPathOptionPathId": juniMplsIfMinorPathOptionPathId,
       "juniMplsIfMinorPathOptionRowStatus": juniMplsIfMinorPathOptionRowStatus,
       "juniMplsTunnelProfile": juniMplsTunnelProfile,
       "juniMplsTunnelProfileGroup": juniMplsTunnelProfileGroup,
       "juniMplsTunnelProfileTable": juniMplsTunnelProfileTable,
       "juniMplsTunnelProfileEntry": juniMplsTunnelProfileEntry,
       "juniMplsTunnelProfileName": juniMplsTunnelProfileName,
       "juniMplsTunnelProfileAdminStatus": juniMplsTunnelProfileAdminStatus,
       "juniMplsTunnelProfileBaseTunnelName": juniMplsTunnelProfileBaseTunnelName,
       "juniMplsTunnelProfileIpProfileName": juniMplsTunnelProfileIpProfileName,
       "juniMplsTunnelProfileLabelDistProto": juniMplsTunnelProfileLabelDistProto,
       "juniMplsTunnelProfileAnnounceToOspf": juniMplsTunnelProfileAnnounceToOspf,
       "juniMplsTunnelProfileAnnounceToIsis": juniMplsTunnelProfileAnnounceToIsis,
       "juniMplsTunnelProfileAnnounceToBgp": juniMplsTunnelProfileAnnounceToBgp,
       "juniMplsTunnelProfileMetricMode": juniMplsTunnelProfileMetricMode,
       "juniMplsTunnelProfileAbsoluteMetric": juniMplsTunnelProfileAbsoluteMetric,
       "juniMplsTunnelProfileRelativeMetric": juniMplsTunnelProfileRelativeMetric,
       "juniMplsTunnelProfileBandwidth": juniMplsTunnelProfileBandwidth,
       "juniMplsTunnelProfileAffinity": juniMplsTunnelProfileAffinity,
       "juniMplsTunnelProfileAffinityMask": juniMplsTunnelProfileAffinityMask,
       "juniMplsTunnelProfileSetupPriority": juniMplsTunnelProfileSetupPriority,
       "juniMplsTunnelProfileHoldingPriority": juniMplsTunnelProfileHoldingPriority,
       "juniMplsTunnelProfileRetryTimes": juniMplsTunnelProfileRetryTimes,
       "juniMplsTunnelProfileRetryInterval": juniMplsTunnelProfileRetryInterval,
       "juniMplsTunnelProfileRetryTimesNoroute": juniMplsTunnelProfileRetryTimesNoroute,
       "juniMplsTunnelProfileRetryIntervalNoroute": juniMplsTunnelProfileRetryIntervalNoroute,
       "juniMplsTunnelProfileVpnOuiNumber": juniMplsTunnelProfileVpnOuiNumber,
       "juniMplsTunnelProfileVpnIndex": juniMplsTunnelProfileVpnIndex,
       "juniMplsTunnelProfileRowStatus": juniMplsTunnelProfileRowStatus,
       "juniMplsTunnelProfileTargetedDynamicTunnel": juniMplsTunnelProfileTargetedDynamicTunnel,
       "juniMplsTunnelProfileList": juniMplsTunnelProfileList,
       "juniMplsTunnelProfilePathOptionTable": juniMplsTunnelProfilePathOptionTable,
       "juniMplsTunnelProfilePathOptionEntry": juniMplsTunnelProfilePathOptionEntry,
       "juniMplsTunnelProfileNamePathOption": juniMplsTunnelProfileNamePathOption,
       "juniMplsTunnelProfilePathOptionNumber": juniMplsTunnelProfilePathOptionNumber,
       "juniMplsTunnelProfilePathOptionProtocol": juniMplsTunnelProfilePathOptionProtocol,
       "juniMplsTunnelProfilePathOptionLockdown": juniMplsTunnelProfilePathOptionLockdown,
       "juniMplsTunnelProfilePathOptionPathName": juniMplsTunnelProfilePathOptionPathName,
       "juniMplsTunnelProfilePathOptionPathId": juniMplsTunnelProfilePathOptionPathId,
       "juniMplsTunnelProfilePathOptionRowStatus": juniMplsTunnelProfilePathOptionRowStatus,
       "juniMplsTunnelProfileDynamicEndpointTable": juniMplsTunnelProfileDynamicEndpointTable,
       "juniMplsTunnelProfileDynamicEndpointEntry": juniMplsTunnelProfileDynamicEndpointEntry,
       "juniMplsTunnelProfileNameDynamicEndpoint": juniMplsTunnelProfileNameDynamicEndpoint,
       "juniMplsTunnelProfileDynamicEndpointType": juniMplsTunnelProfileDynamicEndpointType,
       "juniMplsTunnelProfileDynamicEndpointPolicyListType": juniMplsTunnelProfileDynamicEndpointPolicyListType,
       "juniMplsTunnelProfileDynamicEndpointListName": juniMplsTunnelProfileDynamicEndpointListName,
       "juniMplsTunnelProfileDynamicEndpointRowStatus": juniMplsTunnelProfileDynamicEndpointRowStatus,
       "juniMplsTunnelProfileTunnelEndpointTable": juniMplsTunnelProfileTunnelEndpointTable,
       "juniMplsTunnelProfileTunnelEndpointEntry": juniMplsTunnelProfileTunnelEndpointEntry,
       "juniMplsTunnelProfileNameTunnelEndpoint": juniMplsTunnelProfileNameTunnelEndpoint,
       "juniMplsTunnelProfileTunnelEndpointAddress": juniMplsTunnelProfileTunnelEndpointAddress,
       "juniMplsTunnelProfileTunnelEndpointDstMask": juniMplsTunnelProfileTunnelEndpointDstMask,
       "juniMplsTunnelProfileTunnelEndpointRowStatus": juniMplsTunnelProfileTunnelEndpointRowStatus,
       "juniMplsExplicitPath": juniMplsExplicitPath,
       "juniMplsExplicitPathGroup": juniMplsExplicitPathGroup,
       "juniMplsExplicitPathTable": juniMplsExplicitPathTable,
       "juniMplsExplicitPathEntry": juniMplsExplicitPathEntry,
       "juniMplsExplicitPathName": juniMplsExplicitPathName,
       "juniMplsExplicitPathAdminState": juniMplsExplicitPathAdminState,
       "juniMplsExplicitPathRowStatus": juniMplsExplicitPathRowStatus,
       "juniMplsExplicitPathNodeTable": juniMplsExplicitPathNodeTable,
       "juniMplsExplicitPathNodeEntry": juniMplsExplicitPathNodeEntry,
       "juniMplsExplicitPathNodeName": juniMplsExplicitPathNodeName,
       "juniMplsExplicitPathNodeIndexNumber": juniMplsExplicitPathNodeIndexNumber,
       "juniMplsExplicitPathNodeLoose": juniMplsExplicitPathNodeLoose,
       "juniMplsExplicitPathNodeHopAddress": juniMplsExplicitPathNodeHopAddress,
       "juniMplsExplicitPathNodeHopAddressMask": juniMplsExplicitPathNodeHopAddressMask,
       "juniMplsExplicitPathNodeRowStatus": juniMplsExplicitPathNodeRowStatus,
       "juniMplsConformance": juniMplsConformance,
       "juniMplsCompliances": juniMplsCompliances,
       "juniMplsCompliance": juniMplsCompliance,
       "juniMplsCompliance2": juniMplsCompliance2,
       "juniMplsCompliance3": juniMplsCompliance3,
       "juniMplsCompliance4": juniMplsCompliance4,
       "juniMplsConfGroups": juniMplsConfGroups,
       "juniMplsLsrGlobalConfGroup": juniMplsLsrGlobalConfGroup,
       "juniMplsMajorLayerConfGroup": juniMplsMajorLayerConfGroup,
       "juniMplsMinorLayerConfGroup": juniMplsMinorLayerConfGroup,
       "juniMplsTunnelProfileConfGroup": juniMplsTunnelProfileConfGroup,
       "juniMplsExplicitPathConfGroup": juniMplsExplicitPathConfGroup,
       "juniMplsMinorLayerConfGroup2": juniMplsMinorLayerConfGroup2,
       "juniMplsTunnelProfileConfGroup2": juniMplsTunnelProfileConfGroup2,
       "juniMplsLsrGlobalConfGroup2": juniMplsLsrGlobalConfGroup2,
       "juniMplsLsrGlobalConfGroup3": juniMplsLsrGlobalConfGroup3,
       "juniMplsMajorLayerConfGroup2": juniMplsMajorLayerConfGroup2,
       "juniMplsMinorLayerConfGroup3": juniMplsMinorLayerConfGroup3,
       "juniMplsTunnelProfileConfGroup3": juniMplsTunnelProfileConfGroup3}
)
