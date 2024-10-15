# SNMP MIB module (A3COM-HUAWEI-QOS-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-QOS-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:56 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cQosProfile = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cQoSDirection(Integer32, TextualConvention):
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
        *(("input", 1),
          ("invalid", 0),
          ("ouput", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3cQoSProfObjects_ObjectIdentity = ObjectIdentity
h3cQoSProfObjects = _H3cQoSProfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1)
)
_H3cQoSProf_ObjectIdentity = ObjectIdentity
h3cQoSProf = _H3cQoSProf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 1)
)
_H3cQoSProfTable_Object = MibTable
h3cQoSProfTable = _H3cQoSProfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cQoSProfTable.setStatus("current")
_H3cQoSProfEntry_Object = MibTableRow
h3cQoSProfEntry = _H3cQoSProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 1, 1, 1)
)
h3cQoSProfEntry.setIndexNames(
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfIndex"),
)
if mibBuilder.loadTexts:
    h3cQoSProfEntry.setStatus("current")


class _H3cQoSProfIndex_Type(Integer32):
    """Custom type h3cQoSProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQoSProfIndex_Type.__name__ = "Integer32"
_H3cQoSProfIndex_Object = MibTableColumn
h3cQoSProfIndex = _H3cQoSProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 1, 1, 1, 1),
    _H3cQoSProfIndex_Type()
)
h3cQoSProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSProfIndex.setStatus("current")


class _H3cQoSProfName_Type(OctetString):
    """Custom type h3cQoSProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cQoSProfName_Type.__name__ = "OctetString"
_H3cQoSProfName_Object = MibTableColumn
h3cQoSProfName = _H3cQoSProfName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 1, 1, 1, 2),
    _H3cQoSProfName_Type()
)
h3cQoSProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSProfName.setStatus("current")


class _H3cQoSProfActionNumber_Type(Integer32):
    """Custom type h3cQoSProfActionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cQoSProfActionNumber_Type.__name__ = "Integer32"
_H3cQoSProfActionNumber_Object = MibTableColumn
h3cQoSProfActionNumber = _H3cQoSProfActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 1, 1, 1, 3),
    _H3cQoSProfActionNumber_Type()
)
h3cQoSProfActionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSProfActionNumber.setStatus("current")
_H3cQoSProfRowStatus_Type = RowStatus
_H3cQoSProfRowStatus_Object = MibTableColumn
h3cQoSProfRowStatus = _H3cQoSProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 1, 1, 1, 4),
    _H3cQoSProfRowStatus_Type()
)
h3cQoSProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSProfRowStatus.setStatus("current")
_H3cQoSAction_ObjectIdentity = ObjectIdentity
h3cQoSAction = _H3cQoSAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2)
)
_H3cQoSTrafficLimitTable_Object = MibTable
h3cQoSTrafficLimitTable = _H3cQoSTrafficLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cQoSTrafficLimitTable.setStatus("current")
_H3cQoSTrafficLimitEntry_Object = MibTableRow
h3cQoSTrafficLimitEntry = _H3cQoSTrafficLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1)
)
h3cQoSTrafficLimitEntry.setIndexNames(
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtProfIndex"),
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtActionIndex"),
)
if mibBuilder.loadTexts:
    h3cQoSTrafficLimitEntry.setStatus("current")


class _H3cQoSTrafLmtProfIndex_Type(Integer32):
    """Custom type h3cQoSTrafLmtProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQoSTrafLmtProfIndex_Type.__name__ = "Integer32"
_H3cQoSTrafLmtProfIndex_Object = MibTableColumn
h3cQoSTrafLmtProfIndex = _H3cQoSTrafLmtProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 1),
    _H3cQoSTrafLmtProfIndex_Type()
)
h3cQoSTrafLmtProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtProfIndex.setStatus("current")


class _H3cQoSTrafLmtActionIndex_Type(Integer32):
    """Custom type h3cQoSTrafLmtActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQoSTrafLmtActionIndex_Type.__name__ = "Integer32"
_H3cQoSTrafLmtActionIndex_Object = MibTableColumn
h3cQoSTrafLmtActionIndex = _H3cQoSTrafLmtActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 2),
    _H3cQoSTrafLmtActionIndex_Type()
)
h3cQoSTrafLmtActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtActionIndex.setStatus("current")
_H3cQoSTrafLmtDirection_Type = H3cQoSDirection
_H3cQoSTrafLmtDirection_Object = MibTableColumn
h3cQoSTrafLmtDirection = _H3cQoSTrafLmtDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 3),
    _H3cQoSTrafLmtDirection_Type()
)
h3cQoSTrafLmtDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtDirection.setStatus("current")


class _H3cQoSTrafLmtUserAclNum_Type(Integer32):
    """Custom type h3cQoSTrafLmtUserAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
    )


_H3cQoSTrafLmtUserAclNum_Type.__name__ = "Integer32"
_H3cQoSTrafLmtUserAclNum_Object = MibTableColumn
h3cQoSTrafLmtUserAclNum = _H3cQoSTrafLmtUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 4),
    _H3cQoSTrafLmtUserAclNum_Type()
)
h3cQoSTrafLmtUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtUserAclNum.setStatus("current")


class _H3cQoSTrafLmtUserAclRule_Type(Integer32):
    """Custom type h3cQoSTrafLmtUserAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cQoSTrafLmtUserAclRule_Type.__name__ = "Integer32"
_H3cQoSTrafLmtUserAclRule_Object = MibTableColumn
h3cQoSTrafLmtUserAclRule = _H3cQoSTrafLmtUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 5),
    _H3cQoSTrafLmtUserAclRule_Type()
)
h3cQoSTrafLmtUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtUserAclRule.setStatus("current")


class _H3cQoSTrafLmtIpAclNum_Type(Integer32):
    """Custom type h3cQoSTrafLmtIpAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_H3cQoSTrafLmtIpAclNum_Type.__name__ = "Integer32"
_H3cQoSTrafLmtIpAclNum_Object = MibTableColumn
h3cQoSTrafLmtIpAclNum = _H3cQoSTrafLmtIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 6),
    _H3cQoSTrafLmtIpAclNum_Type()
)
h3cQoSTrafLmtIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtIpAclNum.setStatus("current")


class _H3cQoSTrafLmtIpAclRule_Type(Integer32):
    """Custom type h3cQoSTrafLmtIpAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cQoSTrafLmtIpAclRule_Type.__name__ = "Integer32"
_H3cQoSTrafLmtIpAclRule_Object = MibTableColumn
h3cQoSTrafLmtIpAclRule = _H3cQoSTrafLmtIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 7),
    _H3cQoSTrafLmtIpAclRule_Type()
)
h3cQoSTrafLmtIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtIpAclRule.setStatus("current")


class _H3cQoSTrafLmtLinkAclNum_Type(Integer32):
    """Custom type h3cQoSTrafLmtLinkAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
    )


_H3cQoSTrafLmtLinkAclNum_Type.__name__ = "Integer32"
_H3cQoSTrafLmtLinkAclNum_Object = MibTableColumn
h3cQoSTrafLmtLinkAclNum = _H3cQoSTrafLmtLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 8),
    _H3cQoSTrafLmtLinkAclNum_Type()
)
h3cQoSTrafLmtLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtLinkAclNum.setStatus("current")


class _H3cQoSTrafLmtLinkAclRule_Type(Integer32):
    """Custom type h3cQoSTrafLmtLinkAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cQoSTrafLmtLinkAclRule_Type.__name__ = "Integer32"
_H3cQoSTrafLmtLinkAclRule_Object = MibTableColumn
h3cQoSTrafLmtLinkAclRule = _H3cQoSTrafLmtLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 9),
    _H3cQoSTrafLmtLinkAclRule_Type()
)
h3cQoSTrafLmtLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtLinkAclRule.setStatus("current")


class _H3cQoSTrafLmtTargetRateMbps_Type(Integer32):
    """Custom type h3cQoSTrafLmtTargetRateMbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_H3cQoSTrafLmtTargetRateMbps_Type.__name__ = "Integer32"
_H3cQoSTrafLmtTargetRateMbps_Object = MibTableColumn
h3cQoSTrafLmtTargetRateMbps = _H3cQoSTrafLmtTargetRateMbps_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 10),
    _H3cQoSTrafLmtTargetRateMbps_Type()
)
h3cQoSTrafLmtTargetRateMbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtTargetRateMbps.setStatus("current")


class _H3cQoSTrafLmtTargetRateKbps_Type(Integer32):
    """Custom type h3cQoSTrafLmtTargetRateKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_H3cQoSTrafLmtTargetRateKbps_Type.__name__ = "Integer32"
_H3cQoSTrafLmtTargetRateKbps_Object = MibTableColumn
h3cQoSTrafLmtTargetRateKbps = _H3cQoSTrafLmtTargetRateKbps_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 11),
    _H3cQoSTrafLmtTargetRateKbps_Type()
)
h3cQoSTrafLmtTargetRateKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtTargetRateKbps.setStatus("current")


class _H3cQoSTrafLmtPeakRate_Type(Integer32):
    """Custom type h3cQoSTrafLmtPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 8388608),
    )


_H3cQoSTrafLmtPeakRate_Type.__name__ = "Integer32"
_H3cQoSTrafLmtPeakRate_Object = MibTableColumn
h3cQoSTrafLmtPeakRate = _H3cQoSTrafLmtPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 12),
    _H3cQoSTrafLmtPeakRate_Type()
)
h3cQoSTrafLmtPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtPeakRate.setStatus("current")


class _H3cQoSTrafLmtCIR_Type(Integer32):
    """Custom type h3cQoSTrafLmtCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_H3cQoSTrafLmtCIR_Type.__name__ = "Integer32"
_H3cQoSTrafLmtCIR_Object = MibTableColumn
h3cQoSTrafLmtCIR = _H3cQoSTrafLmtCIR_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 13),
    _H3cQoSTrafLmtCIR_Type()
)
h3cQoSTrafLmtCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtCIR.setStatus("current")


class _H3cQoSTrafLmtCBS_Type(Integer32):
    """Custom type h3cQoSTrafLmtCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_H3cQoSTrafLmtCBS_Type.__name__ = "Integer32"
_H3cQoSTrafLmtCBS_Object = MibTableColumn
h3cQoSTrafLmtCBS = _H3cQoSTrafLmtCBS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 14),
    _H3cQoSTrafLmtCBS_Type()
)
h3cQoSTrafLmtCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtCBS.setStatus("current")


class _H3cQoSTrafLmtEBS_Type(Integer32):
    """Custom type h3cQoSTrafLmtEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_H3cQoSTrafLmtEBS_Type.__name__ = "Integer32"
_H3cQoSTrafLmtEBS_Object = MibTableColumn
h3cQoSTrafLmtEBS = _H3cQoSTrafLmtEBS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 15),
    _H3cQoSTrafLmtEBS_Type()
)
h3cQoSTrafLmtEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtEBS.setStatus("current")


class _H3cQoSTrafLmtPIR_Type(Integer32):
    """Custom type h3cQoSTrafLmtPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_H3cQoSTrafLmtPIR_Type.__name__ = "Integer32"
_H3cQoSTrafLmtPIR_Object = MibTableColumn
h3cQoSTrafLmtPIR = _H3cQoSTrafLmtPIR_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 16),
    _H3cQoSTrafLmtPIR_Type()
)
h3cQoSTrafLmtPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtPIR.setStatus("current")


class _H3cQoSTrafLmtConformLocalPre_Type(Integer32):
    """Custom type h3cQoSTrafLmtConformLocalPre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cQoSTrafLmtConformLocalPre_Type.__name__ = "Integer32"
_H3cQoSTrafLmtConformLocalPre_Object = MibTableColumn
h3cQoSTrafLmtConformLocalPre = _H3cQoSTrafLmtConformLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 17),
    _H3cQoSTrafLmtConformLocalPre_Type()
)
h3cQoSTrafLmtConformLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtConformLocalPre.setStatus("current")


class _H3cQoSTrafLmtConformActionType_Type(Integer32):
    """Custom type h3cQoSTrafLmtConformActionType based on Integer32"""
    defaultValue = 1

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
        *(("invalid", 0),
          ("remark-cos", 1),
          ("remark-cos-drop-priority", 3),
          ("remark-drop-priority", 2),
          ("remark-dscp", 5),
          ("remark-policed-service", 4))
    )


_H3cQoSTrafLmtConformActionType_Type.__name__ = "Integer32"
_H3cQoSTrafLmtConformActionType_Object = MibTableColumn
h3cQoSTrafLmtConformActionType = _H3cQoSTrafLmtConformActionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 18),
    _H3cQoSTrafLmtConformActionType_Type()
)
h3cQoSTrafLmtConformActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtConformActionType.setStatus("current")


class _H3cQoSTrafLmtExceedActionType_Type(Integer32):
    """Custom type h3cQoSTrafLmtExceedActionType based on Integer32"""
    defaultValue = 1

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
        *(("drop", 2),
          ("exceed-cos", 4),
          ("forward", 1),
          ("invalid", 0),
          ("remarkdscp", 3))
    )


_H3cQoSTrafLmtExceedActionType_Type.__name__ = "Integer32"
_H3cQoSTrafLmtExceedActionType_Object = MibTableColumn
h3cQoSTrafLmtExceedActionType = _H3cQoSTrafLmtExceedActionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 19),
    _H3cQoSTrafLmtExceedActionType_Type()
)
h3cQoSTrafLmtExceedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtExceedActionType.setStatus("current")


class _H3cQoSTrafLmtExceedDscp_Type(Integer32):
    """Custom type h3cQoSTrafLmtExceedDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafLmtExceedDscp_Type.__name__ = "Integer32"
_H3cQoSTrafLmtExceedDscp_Object = MibTableColumn
h3cQoSTrafLmtExceedDscp = _H3cQoSTrafLmtExceedDscp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 20),
    _H3cQoSTrafLmtExceedDscp_Type()
)
h3cQoSTrafLmtExceedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtExceedDscp.setStatus("current")


class _H3cQoSTrafLmtExceedCos_Type(Integer32):
    """Custom type h3cQoSTrafLmtExceedCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafLmtExceedCos_Type.__name__ = "Integer32"
_H3cQoSTrafLmtExceedCos_Object = MibTableColumn
h3cQoSTrafLmtExceedCos = _H3cQoSTrafLmtExceedCos_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 21),
    _H3cQoSTrafLmtExceedCos_Type()
)
h3cQoSTrafLmtExceedCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtExceedCos.setStatus("current")
_H3cQoSTrafLmtRowStatus_Type = RowStatus
_H3cQoSTrafLmtRowStatus_Object = MibTableColumn
h3cQoSTrafLmtRowStatus = _H3cQoSTrafLmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 22),
    _H3cQoSTrafLmtRowStatus_Type()
)
h3cQoSTrafLmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtRowStatus.setStatus("current")


class _H3cQoSTrafLmtConformCos_Type(Integer32):
    """Custom type h3cQoSTrafLmtConformCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafLmtConformCos_Type.__name__ = "Integer32"
_H3cQoSTrafLmtConformCos_Object = MibTableColumn
h3cQoSTrafLmtConformCos = _H3cQoSTrafLmtConformCos_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 23),
    _H3cQoSTrafLmtConformCos_Type()
)
h3cQoSTrafLmtConformCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtConformCos.setStatus("current")


class _H3cQoSTrafLmtConformDscp_Type(Integer32):
    """Custom type h3cQoSTrafLmtConformDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafLmtConformDscp_Type.__name__ = "Integer32"
_H3cQoSTrafLmtConformDscp_Object = MibTableColumn
h3cQoSTrafLmtConformDscp = _H3cQoSTrafLmtConformDscp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 1, 1, 24),
    _H3cQoSTrafLmtConformDscp_Type()
)
h3cQoSTrafLmtConformDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafLmtConformDscp.setStatus("current")
_H3cQoSTrafficPriorityTable_Object = MibTable
h3cQoSTrafficPriorityTable = _H3cQoSTrafficPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cQoSTrafficPriorityTable.setStatus("current")
_H3cQoSTrafficPriorityEntry_Object = MibTableRow
h3cQoSTrafficPriorityEntry = _H3cQoSTrafficPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1)
)
h3cQoSTrafficPriorityEntry.setIndexNames(
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioProfIndex"),
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioActionIndex"),
)
if mibBuilder.loadTexts:
    h3cQoSTrafficPriorityEntry.setStatus("current")


class _H3cQoSTrafPrioProfIndex_Type(Integer32):
    """Custom type h3cQoSTrafPrioProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQoSTrafPrioProfIndex_Type.__name__ = "Integer32"
_H3cQoSTrafPrioProfIndex_Object = MibTableColumn
h3cQoSTrafPrioProfIndex = _H3cQoSTrafPrioProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 1),
    _H3cQoSTrafPrioProfIndex_Type()
)
h3cQoSTrafPrioProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioProfIndex.setStatus("current")


class _H3cQoSTrafPrioActionIndex_Type(Integer32):
    """Custom type h3cQoSTrafPrioActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQoSTrafPrioActionIndex_Type.__name__ = "Integer32"
_H3cQoSTrafPrioActionIndex_Object = MibTableColumn
h3cQoSTrafPrioActionIndex = _H3cQoSTrafPrioActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 2),
    _H3cQoSTrafPrioActionIndex_Type()
)
h3cQoSTrafPrioActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioActionIndex.setStatus("current")
_H3cQoSTrafPrioDirection_Type = H3cQoSDirection
_H3cQoSTrafPrioDirection_Object = MibTableColumn
h3cQoSTrafPrioDirection = _H3cQoSTrafPrioDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 3),
    _H3cQoSTrafPrioDirection_Type()
)
h3cQoSTrafPrioDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioDirection.setStatus("current")


class _H3cQoSTrafPrioUserAclNum_Type(Integer32):
    """Custom type h3cQoSTrafPrioUserAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
    )


_H3cQoSTrafPrioUserAclNum_Type.__name__ = "Integer32"
_H3cQoSTrafPrioUserAclNum_Object = MibTableColumn
h3cQoSTrafPrioUserAclNum = _H3cQoSTrafPrioUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 4),
    _H3cQoSTrafPrioUserAclNum_Type()
)
h3cQoSTrafPrioUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioUserAclNum.setStatus("current")


class _H3cQoSTrafPrioUserAclRule_Type(Integer32):
    """Custom type h3cQoSTrafPrioUserAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cQoSTrafPrioUserAclRule_Type.__name__ = "Integer32"
_H3cQoSTrafPrioUserAclRule_Object = MibTableColumn
h3cQoSTrafPrioUserAclRule = _H3cQoSTrafPrioUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 5),
    _H3cQoSTrafPrioUserAclRule_Type()
)
h3cQoSTrafPrioUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioUserAclRule.setStatus("current")


class _H3cQoSTrafPrioIpAclNum_Type(Integer32):
    """Custom type h3cQoSTrafPrioIpAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_H3cQoSTrafPrioIpAclNum_Type.__name__ = "Integer32"
_H3cQoSTrafPrioIpAclNum_Object = MibTableColumn
h3cQoSTrafPrioIpAclNum = _H3cQoSTrafPrioIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 6),
    _H3cQoSTrafPrioIpAclNum_Type()
)
h3cQoSTrafPrioIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioIpAclNum.setStatus("current")


class _H3cQoSTrafPrioIpAclRule_Type(Integer32):
    """Custom type h3cQoSTrafPrioIpAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cQoSTrafPrioIpAclRule_Type.__name__ = "Integer32"
_H3cQoSTrafPrioIpAclRule_Object = MibTableColumn
h3cQoSTrafPrioIpAclRule = _H3cQoSTrafPrioIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 7),
    _H3cQoSTrafPrioIpAclRule_Type()
)
h3cQoSTrafPrioIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioIpAclRule.setStatus("current")


class _H3cQoSTrafPrioLinkAclNum_Type(Integer32):
    """Custom type h3cQoSTrafPrioLinkAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
    )


_H3cQoSTrafPrioLinkAclNum_Type.__name__ = "Integer32"
_H3cQoSTrafPrioLinkAclNum_Object = MibTableColumn
h3cQoSTrafPrioLinkAclNum = _H3cQoSTrafPrioLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 8),
    _H3cQoSTrafPrioLinkAclNum_Type()
)
h3cQoSTrafPrioLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioLinkAclNum.setStatus("current")


class _H3cQoSTrafPrioLinkAclRule_Type(Integer32):
    """Custom type h3cQoSTrafPrioLinkAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cQoSTrafPrioLinkAclRule_Type.__name__ = "Integer32"
_H3cQoSTrafPrioLinkAclRule_Object = MibTableColumn
h3cQoSTrafPrioLinkAclRule = _H3cQoSTrafPrioLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 9),
    _H3cQoSTrafPrioLinkAclRule_Type()
)
h3cQoSTrafPrioLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioLinkAclRule.setStatus("current")


class _H3cQoSTrafPrioDscp_Type(Integer32):
    """Custom type h3cQoSTrafPrioDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafPrioDscp_Type.__name__ = "Integer32"
_H3cQoSTrafPrioDscp_Object = MibTableColumn
h3cQoSTrafPrioDscp = _H3cQoSTrafPrioDscp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 10),
    _H3cQoSTrafPrioDscp_Type()
)
h3cQoSTrafPrioDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioDscp.setStatus("current")


class _H3cQoSTrafPrioIpPre_Type(Integer32):
    """Custom type h3cQoSTrafPrioIpPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafPrioIpPre_Type.__name__ = "Integer32"
_H3cQoSTrafPrioIpPre_Object = MibTableColumn
h3cQoSTrafPrioIpPre = _H3cQoSTrafPrioIpPre_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 11),
    _H3cQoSTrafPrioIpPre_Type()
)
h3cQoSTrafPrioIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioIpPre.setStatus("current")


class _H3cQoSTrafPrioIpPreFromCos_Type(TruthValue):
    """Custom type h3cQoSTrafPrioIpPreFromCos based on TruthValue"""
    defaultValue = 2


_H3cQoSTrafPrioIpPreFromCos_Object = MibTableColumn
h3cQoSTrafPrioIpPreFromCos = _H3cQoSTrafPrioIpPreFromCos_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 12),
    _H3cQoSTrafPrioIpPreFromCos_Type()
)
h3cQoSTrafPrioIpPreFromCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioIpPreFromCos.setStatus("current")


class _H3cQoSTrafPrioCos_Type(Integer32):
    """Custom type h3cQoSTrafPrioCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafPrioCos_Type.__name__ = "Integer32"
_H3cQoSTrafPrioCos_Object = MibTableColumn
h3cQoSTrafPrioCos = _H3cQoSTrafPrioCos_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 13),
    _H3cQoSTrafPrioCos_Type()
)
h3cQoSTrafPrioCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioCos.setStatus("current")


class _H3cQoSTrafPrioCosFromIpPre_Type(TruthValue):
    """Custom type h3cQoSTrafPrioCosFromIpPre based on TruthValue"""
    defaultValue = 2


_H3cQoSTrafPrioCosFromIpPre_Object = MibTableColumn
h3cQoSTrafPrioCosFromIpPre = _H3cQoSTrafPrioCosFromIpPre_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 14),
    _H3cQoSTrafPrioCosFromIpPre_Type()
)
h3cQoSTrafPrioCosFromIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioCosFromIpPre.setStatus("current")


class _H3cQoSTrafPrioLocalPre_Type(Integer32):
    """Custom type h3cQoSTrafPrioLocalPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafPrioLocalPre_Type.__name__ = "Integer32"
_H3cQoSTrafPrioLocalPre_Object = MibTableColumn
h3cQoSTrafPrioLocalPre = _H3cQoSTrafPrioLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 15),
    _H3cQoSTrafPrioLocalPre_Type()
)
h3cQoSTrafPrioLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioLocalPre.setStatus("current")


class _H3cQoSTrafPrioPolicedServiceType_Type(Integer32):
    """Custom type h3cQoSTrafPrioPolicedServiceType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("new-dscp", 3),
          ("trust-dscp", 2),
          ("untrusted", 4))
    )


_H3cQoSTrafPrioPolicedServiceType_Type.__name__ = "Integer32"
_H3cQoSTrafPrioPolicedServiceType_Object = MibTableColumn
h3cQoSTrafPrioPolicedServiceType = _H3cQoSTrafPrioPolicedServiceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 16),
    _H3cQoSTrafPrioPolicedServiceType_Type()
)
h3cQoSTrafPrioPolicedServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioPolicedServiceType.setStatus("current")


class _H3cQoSTrafPrioPolicedServiceDscp_Type(Integer32):
    """Custom type h3cQoSTrafPrioPolicedServiceDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafPrioPolicedServiceDscp_Type.__name__ = "Integer32"
_H3cQoSTrafPrioPolicedServiceDscp_Object = MibTableColumn
h3cQoSTrafPrioPolicedServiceDscp = _H3cQoSTrafPrioPolicedServiceDscp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 17),
    _H3cQoSTrafPrioPolicedServiceDscp_Type()
)
h3cQoSTrafPrioPolicedServiceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioPolicedServiceDscp.setStatus("current")


class _H3cQoSTrafPrioPolicedServiceExp_Type(Integer32):
    """Custom type h3cQoSTrafPrioPolicedServiceExp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafPrioPolicedServiceExp_Type.__name__ = "Integer32"
_H3cQoSTrafPrioPolicedServiceExp_Object = MibTableColumn
h3cQoSTrafPrioPolicedServiceExp = _H3cQoSTrafPrioPolicedServiceExp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 18),
    _H3cQoSTrafPrioPolicedServiceExp_Type()
)
h3cQoSTrafPrioPolicedServiceExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioPolicedServiceExp.setStatus("current")


class _H3cQoSTrafPrioPolicedServiceCos_Type(Integer32):
    """Custom type h3cQoSTrafPrioPolicedServiceCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafPrioPolicedServiceCos_Type.__name__ = "Integer32"
_H3cQoSTrafPrioPolicedServiceCos_Object = MibTableColumn
h3cQoSTrafPrioPolicedServiceCos = _H3cQoSTrafPrioPolicedServiceCos_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 19),
    _H3cQoSTrafPrioPolicedServiceCos_Type()
)
h3cQoSTrafPrioPolicedServiceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioPolicedServiceCos.setStatus("current")


class _H3cQoSTrafPrioPolicedServiceLoaclPre_Type(Integer32):
    """Custom type h3cQoSTrafPrioPolicedServiceLoaclPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafPrioPolicedServiceLoaclPre_Type.__name__ = "Integer32"
_H3cQoSTrafPrioPolicedServiceLoaclPre_Object = MibTableColumn
h3cQoSTrafPrioPolicedServiceLoaclPre = _H3cQoSTrafPrioPolicedServiceLoaclPre_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 20),
    _H3cQoSTrafPrioPolicedServiceLoaclPre_Type()
)
h3cQoSTrafPrioPolicedServiceLoaclPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioPolicedServiceLoaclPre.setStatus("current")


class _H3cQoSTrafPrioPolicedServiceDropPriority_Type(Integer32):
    """Custom type h3cQoSTrafPrioPolicedServiceDropPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(255, 255),
    )


_H3cQoSTrafPrioPolicedServiceDropPriority_Type.__name__ = "Integer32"
_H3cQoSTrafPrioPolicedServiceDropPriority_Object = MibTableColumn
h3cQoSTrafPrioPolicedServiceDropPriority = _H3cQoSTrafPrioPolicedServiceDropPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 21),
    _H3cQoSTrafPrioPolicedServiceDropPriority_Type()
)
h3cQoSTrafPrioPolicedServiceDropPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioPolicedServiceDropPriority.setStatus("current")
_H3cQoSTrafPrioRowStatus_Type = RowStatus
_H3cQoSTrafPrioRowStatus_Object = MibTableColumn
h3cQoSTrafPrioRowStatus = _H3cQoSTrafPrioRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 2, 1, 22),
    _H3cQoSTrafPrioRowStatus_Type()
)
h3cQoSTrafPrioRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafPrioRowStatus.setStatus("current")
_H3cQoSTrafficFilterTable_Object = MibTable
h3cQoSTrafficFilterTable = _H3cQoSTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cQoSTrafficFilterTable.setStatus("current")
_H3cQoSTrafficFilterEntry_Object = MibTableRow
h3cQoSTrafficFilterEntry = _H3cQoSTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1)
)
h3cQoSTrafficFilterEntry.setIndexNames(
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafFilterProfIndex"),
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafFilterActionIndex"),
)
if mibBuilder.loadTexts:
    h3cQoSTrafficFilterEntry.setStatus("current")


class _H3cQoSTrafFilterProfIndex_Type(Integer32):
    """Custom type h3cQoSTrafFilterProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQoSTrafFilterProfIndex_Type.__name__ = "Integer32"
_H3cQoSTrafFilterProfIndex_Object = MibTableColumn
h3cQoSTrafFilterProfIndex = _H3cQoSTrafFilterProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1, 1),
    _H3cQoSTrafFilterProfIndex_Type()
)
h3cQoSTrafFilterProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSTrafFilterProfIndex.setStatus("current")


class _H3cQoSTrafFilterActionIndex_Type(Integer32):
    """Custom type h3cQoSTrafFilterActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQoSTrafFilterActionIndex_Type.__name__ = "Integer32"
_H3cQoSTrafFilterActionIndex_Object = MibTableColumn
h3cQoSTrafFilterActionIndex = _H3cQoSTrafFilterActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1, 2),
    _H3cQoSTrafFilterActionIndex_Type()
)
h3cQoSTrafFilterActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSTrafFilterActionIndex.setStatus("current")
_H3cQoSTrafFilterDirection_Type = H3cQoSDirection
_H3cQoSTrafFilterDirection_Object = MibTableColumn
h3cQoSTrafFilterDirection = _H3cQoSTrafFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1, 3),
    _H3cQoSTrafFilterDirection_Type()
)
h3cQoSTrafFilterDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafFilterDirection.setStatus("current")


class _H3cQoSTrafFilterUserAclNum_Type(Integer32):
    """Custom type h3cQoSTrafFilterUserAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
    )


_H3cQoSTrafFilterUserAclNum_Type.__name__ = "Integer32"
_H3cQoSTrafFilterUserAclNum_Object = MibTableColumn
h3cQoSTrafFilterUserAclNum = _H3cQoSTrafFilterUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1, 4),
    _H3cQoSTrafFilterUserAclNum_Type()
)
h3cQoSTrafFilterUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafFilterUserAclNum.setStatus("current")


class _H3cQoSTrafFilterUserAclRule_Type(Integer32):
    """Custom type h3cQoSTrafFilterUserAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cQoSTrafFilterUserAclRule_Type.__name__ = "Integer32"
_H3cQoSTrafFilterUserAclRule_Object = MibTableColumn
h3cQoSTrafFilterUserAclRule = _H3cQoSTrafFilterUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1, 5),
    _H3cQoSTrafFilterUserAclRule_Type()
)
h3cQoSTrafFilterUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafFilterUserAclRule.setStatus("current")


class _H3cQoSTrafFilterIpAclNum_Type(Integer32):
    """Custom type h3cQoSTrafFilterIpAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_H3cQoSTrafFilterIpAclNum_Type.__name__ = "Integer32"
_H3cQoSTrafFilterIpAclNum_Object = MibTableColumn
h3cQoSTrafFilterIpAclNum = _H3cQoSTrafFilterIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1, 6),
    _H3cQoSTrafFilterIpAclNum_Type()
)
h3cQoSTrafFilterIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafFilterIpAclNum.setStatus("current")


class _H3cQoSTrafFilterIpAclRule_Type(Integer32):
    """Custom type h3cQoSTrafFilterIpAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cQoSTrafFilterIpAclRule_Type.__name__ = "Integer32"
_H3cQoSTrafFilterIpAclRule_Object = MibTableColumn
h3cQoSTrafFilterIpAclRule = _H3cQoSTrafFilterIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1, 7),
    _H3cQoSTrafFilterIpAclRule_Type()
)
h3cQoSTrafFilterIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafFilterIpAclRule.setStatus("current")


class _H3cQoSTrafFilterLinkAclNum_Type(Integer32):
    """Custom type h3cQoSTrafFilterLinkAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
    )


_H3cQoSTrafFilterLinkAclNum_Type.__name__ = "Integer32"
_H3cQoSTrafFilterLinkAclNum_Object = MibTableColumn
h3cQoSTrafFilterLinkAclNum = _H3cQoSTrafFilterLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1, 8),
    _H3cQoSTrafFilterLinkAclNum_Type()
)
h3cQoSTrafFilterLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafFilterLinkAclNum.setStatus("current")


class _H3cQoSTrafFilterLinkAclRule_Type(Integer32):
    """Custom type h3cQoSTrafFilterLinkAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cQoSTrafFilterLinkAclRule_Type.__name__ = "Integer32"
_H3cQoSTrafFilterLinkAclRule_Object = MibTableColumn
h3cQoSTrafFilterLinkAclRule = _H3cQoSTrafFilterLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1, 9),
    _H3cQoSTrafFilterLinkAclRule_Type()
)
h3cQoSTrafFilterLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafFilterLinkAclRule.setStatus("current")
_H3cQoSTrafFilterRowStatus_Type = RowStatus
_H3cQoSTrafFilterRowStatus_Object = MibTableColumn
h3cQoSTrafFilterRowStatus = _H3cQoSTrafFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 2, 3, 1, 10),
    _H3cQoSTrafFilterRowStatus_Type()
)
h3cQoSTrafFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSTrafFilterRowStatus.setStatus("current")
_H3cQoSProfPortMapping_ObjectIdentity = ObjectIdentity
h3cQoSProfPortMapping = _H3cQoSProfPortMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3)
)
_H3cQoSProfPortMappingTable_Object = MibTable
h3cQoSProfPortMappingTable = _H3cQoSProfPortMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingTable.setStatus("current")
_H3cQoSProfPortMappingEntry_Object = MibTableRow
h3cQoSProfPortMappingEntry = _H3cQoSProfPortMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 1, 1)
)
h3cQoSProfPortMappingEntry.setIndexNames(
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfPortMappingIfIndex"),
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfPortMappingProfIndex"),
)
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingEntry.setStatus("current")


class _H3cQoSProfPortMappingIfIndex_Type(Integer32):
    """Custom type h3cQoSProfPortMappingIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cQoSProfPortMappingIfIndex_Type.__name__ = "Integer32"
_H3cQoSProfPortMappingIfIndex_Object = MibTableColumn
h3cQoSProfPortMappingIfIndex = _H3cQoSProfPortMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 1, 1, 1),
    _H3cQoSProfPortMappingIfIndex_Type()
)
h3cQoSProfPortMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingIfIndex.setStatus("current")


class _H3cQoSProfPortMappingProfIndex_Type(Integer32):
    """Custom type h3cQoSProfPortMappingProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQoSProfPortMappingProfIndex_Type.__name__ = "Integer32"
_H3cQoSProfPortMappingProfIndex_Object = MibTableColumn
h3cQoSProfPortMappingProfIndex = _H3cQoSProfPortMappingProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 1, 1, 2),
    _H3cQoSProfPortMappingProfIndex_Type()
)
h3cQoSProfPortMappingProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingProfIndex.setStatus("current")
_H3cQoSProfPortMappingRowStatus_Type = RowStatus
_H3cQoSProfPortMappingRowStatus_Object = MibTableColumn
h3cQoSProfPortMappingRowStatus = _H3cQoSProfPortMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 1, 1, 3),
    _H3cQoSProfPortMappingRowStatus_Type()
)
h3cQoSProfPortMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingRowStatus.setStatus("current")
_H3cQoSProfPortMappingModeTable_Object = MibTable
h3cQoSProfPortMappingModeTable = _H3cQoSProfPortMappingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingModeTable.setStatus("current")
_H3cQoSProfPortMappingModeEntry_Object = MibTableRow
h3cQoSProfPortMappingModeEntry = _H3cQoSProfPortMappingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 2, 1)
)
h3cQoSProfPortMappingModeEntry.setIndexNames(
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfPortMappingModeIfIndex"),
)
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingModeEntry.setStatus("current")


class _H3cQoSProfPortMappingModeIfIndex_Type(Integer32):
    """Custom type h3cQoSProfPortMappingModeIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cQoSProfPortMappingModeIfIndex_Type.__name__ = "Integer32"
_H3cQoSProfPortMappingModeIfIndex_Object = MibTableColumn
h3cQoSProfPortMappingModeIfIndex = _H3cQoSProfPortMappingModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 2, 1, 1),
    _H3cQoSProfPortMappingModeIfIndex_Type()
)
h3cQoSProfPortMappingModeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingModeIfIndex.setStatus("current")


class _H3cQoSProfPortMappingMode_Type(Integer32):
    """Custom type h3cQoSProfPortMappingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-based", 2),
          ("user-based", 1))
    )


_H3cQoSProfPortMappingMode_Type.__name__ = "Integer32"
_H3cQoSProfPortMappingMode_Object = MibTableColumn
h3cQoSProfPortMappingMode = _H3cQoSProfPortMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 2, 1, 2),
    _H3cQoSProfPortMappingMode_Type()
)
h3cQoSProfPortMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingMode.setStatus("current")
_H3cQoSProfDynPortMappingTable_Object = MibTable
h3cQoSProfDynPortMappingTable = _H3cQoSProfDynPortMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 3)
)
if mibBuilder.loadTexts:
    h3cQoSProfDynPortMappingTable.setStatus("current")
_H3cQoSProfDynPortMappingEntry_Object = MibTableRow
h3cQoSProfDynPortMappingEntry = _H3cQoSProfDynPortMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 3, 1)
)
h3cQoSProfDynPortMappingEntry.setIndexNames(
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingIfIndex"),
    (0, "A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingUserSrcMAC"),
)
if mibBuilder.loadTexts:
    h3cQoSProfDynPortMappingEntry.setStatus("current")


class _H3cQoSProfDynPortMappingIfIndex_Type(Integer32):
    """Custom type h3cQoSProfDynPortMappingIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cQoSProfDynPortMappingIfIndex_Type.__name__ = "Integer32"
_H3cQoSProfDynPortMappingIfIndex_Object = MibTableColumn
h3cQoSProfDynPortMappingIfIndex = _H3cQoSProfDynPortMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 3, 1, 1),
    _H3cQoSProfDynPortMappingIfIndex_Type()
)
h3cQoSProfDynPortMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSProfDynPortMappingIfIndex.setStatus("current")
_H3cQoSProfDynPortMappingUserSrcMAC_Type = MacAddress
_H3cQoSProfDynPortMappingUserSrcMAC_Object = MibTableColumn
h3cQoSProfDynPortMappingUserSrcMAC = _H3cQoSProfDynPortMappingUserSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 3, 1, 2),
    _H3cQoSProfDynPortMappingUserSrcMAC_Type()
)
h3cQoSProfDynPortMappingUserSrcMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSProfDynPortMappingUserSrcMAC.setStatus("current")


class _H3cQoSProfDynPortMappingUserName_Type(OctetString):
    """Custom type h3cQoSProfDynPortMappingUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cQoSProfDynPortMappingUserName_Type.__name__ = "OctetString"
_H3cQoSProfDynPortMappingUserName_Object = MibTableColumn
h3cQoSProfDynPortMappingUserName = _H3cQoSProfDynPortMappingUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 3, 1, 3),
    _H3cQoSProfDynPortMappingUserName_Type()
)
h3cQoSProfDynPortMappingUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSProfDynPortMappingUserName.setStatus("current")
_H3cQoSProfDynPortMappingUserIPAddr_Type = IpAddress
_H3cQoSProfDynPortMappingUserIPAddr_Object = MibTableColumn
h3cQoSProfDynPortMappingUserIPAddr = _H3cQoSProfDynPortMappingUserIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 3, 1, 4),
    _H3cQoSProfDynPortMappingUserIPAddr_Type()
)
h3cQoSProfDynPortMappingUserIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSProfDynPortMappingUserIPAddr.setStatus("current")


class _H3cQoSProfDynPortMappingUserVLANID_Type(Integer32):
    """Custom type h3cQoSProfDynPortMappingUserVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cQoSProfDynPortMappingUserVLANID_Type.__name__ = "Integer32"
_H3cQoSProfDynPortMappingUserVLANID_Object = MibTableColumn
h3cQoSProfDynPortMappingUserVLANID = _H3cQoSProfDynPortMappingUserVLANID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 3, 1, 5),
    _H3cQoSProfDynPortMappingUserVLANID_Type()
)
h3cQoSProfDynPortMappingUserVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSProfDynPortMappingUserVLANID.setStatus("current")


class _H3cQoSProfDynPortMappingUserProfName_Type(OctetString):
    """Custom type h3cQoSProfDynPortMappingUserProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cQoSProfDynPortMappingUserProfName_Type.__name__ = "OctetString"
_H3cQoSProfDynPortMappingUserProfName_Object = MibTableColumn
h3cQoSProfDynPortMappingUserProfName = _H3cQoSProfDynPortMappingUserProfName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 1, 3, 3, 1, 6),
    _H3cQoSProfDynPortMappingUserProfName_Type()
)
h3cQoSProfDynPortMappingUserProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSProfDynPortMappingUserProfName.setStatus("current")
_H3cQoSProfPortMappingTraps_ObjectIdentity = ObjectIdentity
h3cQoSProfPortMappingTraps = _H3cQoSProfPortMappingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 2)
)
_H3cQoSProfMibConformance_ObjectIdentity = ObjectIdentity
h3cQoSProfMibConformance = _H3cQoSProfMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 3)
)
_H3cQoSProfMibCompliances_ObjectIdentity = ObjectIdentity
h3cQoSProfMibCompliances = _H3cQoSProfMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 3, 1)
)
_H3cQoSProfMibGroups_ObjectIdentity = ObjectIdentity
h3cQoSProfMibGroups = _H3cQoSProfMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 3, 2)
)

# Managed Objects groups

h3cQoSProfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 3, 2, 1)
)
h3cQoSProfGroup.setObjects(
      *(("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfName"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfActionNumber"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfRowStatus"))
)
if mibBuilder.loadTexts:
    h3cQoSProfGroup.setStatus("current")

h3cQoSActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 3, 2, 2)
)
h3cQoSActionGroup.setObjects(
      *(("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtDirection"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtUserAclNum"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtUserAclRule"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtIpAclNum"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtIpAclRule"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtLinkAclNum"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtLinkAclRule"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtTargetRateMbps"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtTargetRateKbps"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtPeakRate"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtCIR"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtCBS"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtEBS"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtPIR"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtConformLocalPre"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtConformActionType"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtExceedActionType"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtExceedDscp"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtExceedCos"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtRowStatus"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtConformCos"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafLmtConformDscp"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioDirection"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioUserAclNum"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioUserAclRule"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioIpAclNum"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioIpAclRule"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioLinkAclNum"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioLinkAclRule"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioDscp"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioIpPre"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioIpPreFromCos"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioCos"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioCosFromIpPre"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioLocalPre"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceType"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceDscp"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceExp"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceCos"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceLoaclPre"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioPolicedServiceDropPriority"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafPrioRowStatus"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafFilterDirection"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafFilterUserAclNum"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafFilterUserAclRule"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafFilterIpAclNum"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafFilterIpAclRule"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafFilterLinkAclNum"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafFilterLinkAclRule"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSTrafFilterRowStatus"))
)
if mibBuilder.loadTexts:
    h3cQoSActionGroup.setStatus("current")

h3cQoSProfPortMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 3, 2, 3)
)
h3cQoSProfPortMappingGroup.setObjects(
      *(("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfPortMappingRowStatus"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfPortMappingMode"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingUserName"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingUserIPAddr"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingUserVLANID"),
        ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfDynPortMappingUserProfName"))
)
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingGroup.setStatus("current")


# Notification objects

h3cQoSProfPortMappingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 2, 1)
)
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingError.setStatus(
        "current"
    )


# Notifications groups

h3cQoSProfPortMappingTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 3, 2, 4)
)
h3cQoSProfPortMappingTrapsGroup.setObjects(
    ("A3COM-HUAWEI-QOS-PROFILE-MIB", "h3cQoSProfPortMappingError")
)
if mibBuilder.loadTexts:
    h3cQoSProfPortMappingTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cQoSProfMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 17, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cQoSProfMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-QOS-PROFILE-MIB",
    **{"H3cQoSDirection": H3cQoSDirection,
       "h3cQosProfile": h3cQosProfile,
       "h3cQoSProfObjects": h3cQoSProfObjects,
       "h3cQoSProf": h3cQoSProf,
       "h3cQoSProfTable": h3cQoSProfTable,
       "h3cQoSProfEntry": h3cQoSProfEntry,
       "h3cQoSProfIndex": h3cQoSProfIndex,
       "h3cQoSProfName": h3cQoSProfName,
       "h3cQoSProfActionNumber": h3cQoSProfActionNumber,
       "h3cQoSProfRowStatus": h3cQoSProfRowStatus,
       "h3cQoSAction": h3cQoSAction,
       "h3cQoSTrafficLimitTable": h3cQoSTrafficLimitTable,
       "h3cQoSTrafficLimitEntry": h3cQoSTrafficLimitEntry,
       "h3cQoSTrafLmtProfIndex": h3cQoSTrafLmtProfIndex,
       "h3cQoSTrafLmtActionIndex": h3cQoSTrafLmtActionIndex,
       "h3cQoSTrafLmtDirection": h3cQoSTrafLmtDirection,
       "h3cQoSTrafLmtUserAclNum": h3cQoSTrafLmtUserAclNum,
       "h3cQoSTrafLmtUserAclRule": h3cQoSTrafLmtUserAclRule,
       "h3cQoSTrafLmtIpAclNum": h3cQoSTrafLmtIpAclNum,
       "h3cQoSTrafLmtIpAclRule": h3cQoSTrafLmtIpAclRule,
       "h3cQoSTrafLmtLinkAclNum": h3cQoSTrafLmtLinkAclNum,
       "h3cQoSTrafLmtLinkAclRule": h3cQoSTrafLmtLinkAclRule,
       "h3cQoSTrafLmtTargetRateMbps": h3cQoSTrafLmtTargetRateMbps,
       "h3cQoSTrafLmtTargetRateKbps": h3cQoSTrafLmtTargetRateKbps,
       "h3cQoSTrafLmtPeakRate": h3cQoSTrafLmtPeakRate,
       "h3cQoSTrafLmtCIR": h3cQoSTrafLmtCIR,
       "h3cQoSTrafLmtCBS": h3cQoSTrafLmtCBS,
       "h3cQoSTrafLmtEBS": h3cQoSTrafLmtEBS,
       "h3cQoSTrafLmtPIR": h3cQoSTrafLmtPIR,
       "h3cQoSTrafLmtConformLocalPre": h3cQoSTrafLmtConformLocalPre,
       "h3cQoSTrafLmtConformActionType": h3cQoSTrafLmtConformActionType,
       "h3cQoSTrafLmtExceedActionType": h3cQoSTrafLmtExceedActionType,
       "h3cQoSTrafLmtExceedDscp": h3cQoSTrafLmtExceedDscp,
       "h3cQoSTrafLmtExceedCos": h3cQoSTrafLmtExceedCos,
       "h3cQoSTrafLmtRowStatus": h3cQoSTrafLmtRowStatus,
       "h3cQoSTrafLmtConformCos": h3cQoSTrafLmtConformCos,
       "h3cQoSTrafLmtConformDscp": h3cQoSTrafLmtConformDscp,
       "h3cQoSTrafficPriorityTable": h3cQoSTrafficPriorityTable,
       "h3cQoSTrafficPriorityEntry": h3cQoSTrafficPriorityEntry,
       "h3cQoSTrafPrioProfIndex": h3cQoSTrafPrioProfIndex,
       "h3cQoSTrafPrioActionIndex": h3cQoSTrafPrioActionIndex,
       "h3cQoSTrafPrioDirection": h3cQoSTrafPrioDirection,
       "h3cQoSTrafPrioUserAclNum": h3cQoSTrafPrioUserAclNum,
       "h3cQoSTrafPrioUserAclRule": h3cQoSTrafPrioUserAclRule,
       "h3cQoSTrafPrioIpAclNum": h3cQoSTrafPrioIpAclNum,
       "h3cQoSTrafPrioIpAclRule": h3cQoSTrafPrioIpAclRule,
       "h3cQoSTrafPrioLinkAclNum": h3cQoSTrafPrioLinkAclNum,
       "h3cQoSTrafPrioLinkAclRule": h3cQoSTrafPrioLinkAclRule,
       "h3cQoSTrafPrioDscp": h3cQoSTrafPrioDscp,
       "h3cQoSTrafPrioIpPre": h3cQoSTrafPrioIpPre,
       "h3cQoSTrafPrioIpPreFromCos": h3cQoSTrafPrioIpPreFromCos,
       "h3cQoSTrafPrioCos": h3cQoSTrafPrioCos,
       "h3cQoSTrafPrioCosFromIpPre": h3cQoSTrafPrioCosFromIpPre,
       "h3cQoSTrafPrioLocalPre": h3cQoSTrafPrioLocalPre,
       "h3cQoSTrafPrioPolicedServiceType": h3cQoSTrafPrioPolicedServiceType,
       "h3cQoSTrafPrioPolicedServiceDscp": h3cQoSTrafPrioPolicedServiceDscp,
       "h3cQoSTrafPrioPolicedServiceExp": h3cQoSTrafPrioPolicedServiceExp,
       "h3cQoSTrafPrioPolicedServiceCos": h3cQoSTrafPrioPolicedServiceCos,
       "h3cQoSTrafPrioPolicedServiceLoaclPre": h3cQoSTrafPrioPolicedServiceLoaclPre,
       "h3cQoSTrafPrioPolicedServiceDropPriority": h3cQoSTrafPrioPolicedServiceDropPriority,
       "h3cQoSTrafPrioRowStatus": h3cQoSTrafPrioRowStatus,
       "h3cQoSTrafficFilterTable": h3cQoSTrafficFilterTable,
       "h3cQoSTrafficFilterEntry": h3cQoSTrafficFilterEntry,
       "h3cQoSTrafFilterProfIndex": h3cQoSTrafFilterProfIndex,
       "h3cQoSTrafFilterActionIndex": h3cQoSTrafFilterActionIndex,
       "h3cQoSTrafFilterDirection": h3cQoSTrafFilterDirection,
       "h3cQoSTrafFilterUserAclNum": h3cQoSTrafFilterUserAclNum,
       "h3cQoSTrafFilterUserAclRule": h3cQoSTrafFilterUserAclRule,
       "h3cQoSTrafFilterIpAclNum": h3cQoSTrafFilterIpAclNum,
       "h3cQoSTrafFilterIpAclRule": h3cQoSTrafFilterIpAclRule,
       "h3cQoSTrafFilterLinkAclNum": h3cQoSTrafFilterLinkAclNum,
       "h3cQoSTrafFilterLinkAclRule": h3cQoSTrafFilterLinkAclRule,
       "h3cQoSTrafFilterRowStatus": h3cQoSTrafFilterRowStatus,
       "h3cQoSProfPortMapping": h3cQoSProfPortMapping,
       "h3cQoSProfPortMappingTable": h3cQoSProfPortMappingTable,
       "h3cQoSProfPortMappingEntry": h3cQoSProfPortMappingEntry,
       "h3cQoSProfPortMappingIfIndex": h3cQoSProfPortMappingIfIndex,
       "h3cQoSProfPortMappingProfIndex": h3cQoSProfPortMappingProfIndex,
       "h3cQoSProfPortMappingRowStatus": h3cQoSProfPortMappingRowStatus,
       "h3cQoSProfPortMappingModeTable": h3cQoSProfPortMappingModeTable,
       "h3cQoSProfPortMappingModeEntry": h3cQoSProfPortMappingModeEntry,
       "h3cQoSProfPortMappingModeIfIndex": h3cQoSProfPortMappingModeIfIndex,
       "h3cQoSProfPortMappingMode": h3cQoSProfPortMappingMode,
       "h3cQoSProfDynPortMappingTable": h3cQoSProfDynPortMappingTable,
       "h3cQoSProfDynPortMappingEntry": h3cQoSProfDynPortMappingEntry,
       "h3cQoSProfDynPortMappingIfIndex": h3cQoSProfDynPortMappingIfIndex,
       "h3cQoSProfDynPortMappingUserSrcMAC": h3cQoSProfDynPortMappingUserSrcMAC,
       "h3cQoSProfDynPortMappingUserName": h3cQoSProfDynPortMappingUserName,
       "h3cQoSProfDynPortMappingUserIPAddr": h3cQoSProfDynPortMappingUserIPAddr,
       "h3cQoSProfDynPortMappingUserVLANID": h3cQoSProfDynPortMappingUserVLANID,
       "h3cQoSProfDynPortMappingUserProfName": h3cQoSProfDynPortMappingUserProfName,
       "h3cQoSProfPortMappingTraps": h3cQoSProfPortMappingTraps,
       "h3cQoSProfPortMappingError": h3cQoSProfPortMappingError,
       "h3cQoSProfMibConformance": h3cQoSProfMibConformance,
       "h3cQoSProfMibCompliances": h3cQoSProfMibCompliances,
       "h3cQoSProfMibCompliance": h3cQoSProfMibCompliance,
       "h3cQoSProfMibGroups": h3cQoSProfMibGroups,
       "h3cQoSProfGroup": h3cQoSProfGroup,
       "h3cQoSActionGroup": h3cQoSActionGroup,
       "h3cQoSProfPortMappingGroup": h3cQoSProfPortMappingGroup,
       "h3cQoSProfPortMappingTrapsGroup": h3cQoSProfPortMappingTrapsGroup}
)
