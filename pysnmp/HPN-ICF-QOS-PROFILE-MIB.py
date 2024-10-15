# SNMP MIB module (HPN-ICF-QOS-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-QOS-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:37 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfQosProfile = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfQoSDirection(Integer32, TextualConvention):
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

_HpnicfQoSProfObjects_ObjectIdentity = ObjectIdentity
hpnicfQoSProfObjects = _HpnicfQoSProfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1)
)
_HpnicfQoSProf_ObjectIdentity = ObjectIdentity
hpnicfQoSProf = _HpnicfQoSProf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 1)
)
_HpnicfQoSProfTable_Object = MibTable
hpnicfQoSProfTable = _HpnicfQoSProfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfQoSProfTable.setStatus("current")
_HpnicfQoSProfEntry_Object = MibTableRow
hpnicfQoSProfEntry = _HpnicfQoSProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 1, 1, 1)
)
hpnicfQoSProfEntry.setIndexNames(
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQoSProfEntry.setStatus("current")


class _HpnicfQoSProfIndex_Type(Integer32):
    """Custom type hpnicfQoSProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQoSProfIndex_Type.__name__ = "Integer32"
_HpnicfQoSProfIndex_Object = MibTableColumn
hpnicfQoSProfIndex = _HpnicfQoSProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 1, 1, 1, 1),
    _HpnicfQoSProfIndex_Type()
)
hpnicfQoSProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSProfIndex.setStatus("current")


class _HpnicfQoSProfName_Type(OctetString):
    """Custom type hpnicfQoSProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfQoSProfName_Type.__name__ = "OctetString"
_HpnicfQoSProfName_Object = MibTableColumn
hpnicfQoSProfName = _HpnicfQoSProfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 1, 1, 1, 2),
    _HpnicfQoSProfName_Type()
)
hpnicfQoSProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSProfName.setStatus("current")


class _HpnicfQoSProfActionNumber_Type(Integer32):
    """Custom type hpnicfQoSProfActionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSProfActionNumber_Type.__name__ = "Integer32"
_HpnicfQoSProfActionNumber_Object = MibTableColumn
hpnicfQoSProfActionNumber = _HpnicfQoSProfActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 1, 1, 1, 3),
    _HpnicfQoSProfActionNumber_Type()
)
hpnicfQoSProfActionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSProfActionNumber.setStatus("current")
_HpnicfQoSProfRowStatus_Type = RowStatus
_HpnicfQoSProfRowStatus_Object = MibTableColumn
hpnicfQoSProfRowStatus = _HpnicfQoSProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 1, 1, 1, 4),
    _HpnicfQoSProfRowStatus_Type()
)
hpnicfQoSProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSProfRowStatus.setStatus("current")
_HpnicfQoSAction_ObjectIdentity = ObjectIdentity
hpnicfQoSAction = _HpnicfQoSAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2)
)
_HpnicfQoSTrafficLimitTable_Object = MibTable
hpnicfQoSTrafficLimitTable = _HpnicfQoSTrafficLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfQoSTrafficLimitTable.setStatus("current")
_HpnicfQoSTrafficLimitEntry_Object = MibTableRow
hpnicfQoSTrafficLimitEntry = _HpnicfQoSTrafficLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1)
)
hpnicfQoSTrafficLimitEntry.setIndexNames(
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtProfIndex"),
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtActionIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQoSTrafficLimitEntry.setStatus("current")


class _HpnicfQoSTrafLmtProfIndex_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQoSTrafLmtProfIndex_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtProfIndex_Object = MibTableColumn
hpnicfQoSTrafLmtProfIndex = _HpnicfQoSTrafLmtProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 1),
    _HpnicfQoSTrafLmtProfIndex_Type()
)
hpnicfQoSTrafLmtProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtProfIndex.setStatus("current")


class _HpnicfQoSTrafLmtActionIndex_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQoSTrafLmtActionIndex_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtActionIndex_Object = MibTableColumn
hpnicfQoSTrafLmtActionIndex = _HpnicfQoSTrafLmtActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 2),
    _HpnicfQoSTrafLmtActionIndex_Type()
)
hpnicfQoSTrafLmtActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtActionIndex.setStatus("current")
_HpnicfQoSTrafLmtDirection_Type = HpnicfQoSDirection
_HpnicfQoSTrafLmtDirection_Object = MibTableColumn
hpnicfQoSTrafLmtDirection = _HpnicfQoSTrafLmtDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 3),
    _HpnicfQoSTrafLmtDirection_Type()
)
hpnicfQoSTrafLmtDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtDirection.setStatus("current")


class _HpnicfQoSTrafLmtUserAclNum_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtUserAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
    )


_HpnicfQoSTrafLmtUserAclNum_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtUserAclNum_Object = MibTableColumn
hpnicfQoSTrafLmtUserAclNum = _HpnicfQoSTrafLmtUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 4),
    _HpnicfQoSTrafLmtUserAclNum_Type()
)
hpnicfQoSTrafLmtUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtUserAclNum.setStatus("current")


class _HpnicfQoSTrafLmtUserAclRule_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtUserAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSTrafLmtUserAclRule_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtUserAclRule_Object = MibTableColumn
hpnicfQoSTrafLmtUserAclRule = _HpnicfQoSTrafLmtUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 5),
    _HpnicfQoSTrafLmtUserAclRule_Type()
)
hpnicfQoSTrafLmtUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtUserAclRule.setStatus("current")


class _HpnicfQoSTrafLmtIpAclNum_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtIpAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HpnicfQoSTrafLmtIpAclNum_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtIpAclNum_Object = MibTableColumn
hpnicfQoSTrafLmtIpAclNum = _HpnicfQoSTrafLmtIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 6),
    _HpnicfQoSTrafLmtIpAclNum_Type()
)
hpnicfQoSTrafLmtIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtIpAclNum.setStatus("current")


class _HpnicfQoSTrafLmtIpAclRule_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtIpAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSTrafLmtIpAclRule_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtIpAclRule_Object = MibTableColumn
hpnicfQoSTrafLmtIpAclRule = _HpnicfQoSTrafLmtIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 7),
    _HpnicfQoSTrafLmtIpAclRule_Type()
)
hpnicfQoSTrafLmtIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtIpAclRule.setStatus("current")


class _HpnicfQoSTrafLmtLinkAclNum_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtLinkAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
    )


_HpnicfQoSTrafLmtLinkAclNum_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtLinkAclNum_Object = MibTableColumn
hpnicfQoSTrafLmtLinkAclNum = _HpnicfQoSTrafLmtLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 8),
    _HpnicfQoSTrafLmtLinkAclNum_Type()
)
hpnicfQoSTrafLmtLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtLinkAclNum.setStatus("current")


class _HpnicfQoSTrafLmtLinkAclRule_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtLinkAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSTrafLmtLinkAclRule_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtLinkAclRule_Object = MibTableColumn
hpnicfQoSTrafLmtLinkAclRule = _HpnicfQoSTrafLmtLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 9),
    _HpnicfQoSTrafLmtLinkAclRule_Type()
)
hpnicfQoSTrafLmtLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtLinkAclRule.setStatus("current")


class _HpnicfQoSTrafLmtTargetRateMbps_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtTargetRateMbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HpnicfQoSTrafLmtTargetRateMbps_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtTargetRateMbps_Object = MibTableColumn
hpnicfQoSTrafLmtTargetRateMbps = _HpnicfQoSTrafLmtTargetRateMbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 10),
    _HpnicfQoSTrafLmtTargetRateMbps_Type()
)
hpnicfQoSTrafLmtTargetRateMbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtTargetRateMbps.setStatus("current")


class _HpnicfQoSTrafLmtTargetRateKbps_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtTargetRateKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_HpnicfQoSTrafLmtTargetRateKbps_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtTargetRateKbps_Object = MibTableColumn
hpnicfQoSTrafLmtTargetRateKbps = _HpnicfQoSTrafLmtTargetRateKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 11),
    _HpnicfQoSTrafLmtTargetRateKbps_Type()
)
hpnicfQoSTrafLmtTargetRateKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtTargetRateKbps.setStatus("current")


class _HpnicfQoSTrafLmtPeakRate_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 8388608),
    )


_HpnicfQoSTrafLmtPeakRate_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtPeakRate_Object = MibTableColumn
hpnicfQoSTrafLmtPeakRate = _HpnicfQoSTrafLmtPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 12),
    _HpnicfQoSTrafLmtPeakRate_Type()
)
hpnicfQoSTrafLmtPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtPeakRate.setStatus("current")


class _HpnicfQoSTrafLmtCIR_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_HpnicfQoSTrafLmtCIR_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtCIR_Object = MibTableColumn
hpnicfQoSTrafLmtCIR = _HpnicfQoSTrafLmtCIR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 13),
    _HpnicfQoSTrafLmtCIR_Type()
)
hpnicfQoSTrafLmtCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtCIR.setStatus("current")


class _HpnicfQoSTrafLmtCBS_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_HpnicfQoSTrafLmtCBS_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtCBS_Object = MibTableColumn
hpnicfQoSTrafLmtCBS = _HpnicfQoSTrafLmtCBS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 14),
    _HpnicfQoSTrafLmtCBS_Type()
)
hpnicfQoSTrafLmtCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtCBS.setStatus("current")


class _HpnicfQoSTrafLmtEBS_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_HpnicfQoSTrafLmtEBS_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtEBS_Object = MibTableColumn
hpnicfQoSTrafLmtEBS = _HpnicfQoSTrafLmtEBS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 15),
    _HpnicfQoSTrafLmtEBS_Type()
)
hpnicfQoSTrafLmtEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtEBS.setStatus("current")


class _HpnicfQoSTrafLmtPIR_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_HpnicfQoSTrafLmtPIR_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtPIR_Object = MibTableColumn
hpnicfQoSTrafLmtPIR = _HpnicfQoSTrafLmtPIR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 16),
    _HpnicfQoSTrafLmtPIR_Type()
)
hpnicfQoSTrafLmtPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtPIR.setStatus("current")


class _HpnicfQoSTrafLmtConformLocalPre_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtConformLocalPre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfQoSTrafLmtConformLocalPre_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtConformLocalPre_Object = MibTableColumn
hpnicfQoSTrafLmtConformLocalPre = _HpnicfQoSTrafLmtConformLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 17),
    _HpnicfQoSTrafLmtConformLocalPre_Type()
)
hpnicfQoSTrafLmtConformLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtConformLocalPre.setStatus("current")


class _HpnicfQoSTrafLmtConformActionType_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtConformActionType based on Integer32"""
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


_HpnicfQoSTrafLmtConformActionType_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtConformActionType_Object = MibTableColumn
hpnicfQoSTrafLmtConformActionType = _HpnicfQoSTrafLmtConformActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 18),
    _HpnicfQoSTrafLmtConformActionType_Type()
)
hpnicfQoSTrafLmtConformActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtConformActionType.setStatus("current")


class _HpnicfQoSTrafLmtExceedActionType_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtExceedActionType based on Integer32"""
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


_HpnicfQoSTrafLmtExceedActionType_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtExceedActionType_Object = MibTableColumn
hpnicfQoSTrafLmtExceedActionType = _HpnicfQoSTrafLmtExceedActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 19),
    _HpnicfQoSTrafLmtExceedActionType_Type()
)
hpnicfQoSTrafLmtExceedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtExceedActionType.setStatus("current")


class _HpnicfQoSTrafLmtExceedDscp_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtExceedDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafLmtExceedDscp_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtExceedDscp_Object = MibTableColumn
hpnicfQoSTrafLmtExceedDscp = _HpnicfQoSTrafLmtExceedDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 20),
    _HpnicfQoSTrafLmtExceedDscp_Type()
)
hpnicfQoSTrafLmtExceedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtExceedDscp.setStatus("current")


class _HpnicfQoSTrafLmtExceedCos_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtExceedCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafLmtExceedCos_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtExceedCos_Object = MibTableColumn
hpnicfQoSTrafLmtExceedCos = _HpnicfQoSTrafLmtExceedCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 21),
    _HpnicfQoSTrafLmtExceedCos_Type()
)
hpnicfQoSTrafLmtExceedCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtExceedCos.setStatus("current")
_HpnicfQoSTrafLmtRowStatus_Type = RowStatus
_HpnicfQoSTrafLmtRowStatus_Object = MibTableColumn
hpnicfQoSTrafLmtRowStatus = _HpnicfQoSTrafLmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 22),
    _HpnicfQoSTrafLmtRowStatus_Type()
)
hpnicfQoSTrafLmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtRowStatus.setStatus("current")


class _HpnicfQoSTrafLmtConformCos_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtConformCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafLmtConformCos_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtConformCos_Object = MibTableColumn
hpnicfQoSTrafLmtConformCos = _HpnicfQoSTrafLmtConformCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 23),
    _HpnicfQoSTrafLmtConformCos_Type()
)
hpnicfQoSTrafLmtConformCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtConformCos.setStatus("current")


class _HpnicfQoSTrafLmtConformDscp_Type(Integer32):
    """Custom type hpnicfQoSTrafLmtConformDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafLmtConformDscp_Type.__name__ = "Integer32"
_HpnicfQoSTrafLmtConformDscp_Object = MibTableColumn
hpnicfQoSTrafLmtConformDscp = _HpnicfQoSTrafLmtConformDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 1, 1, 24),
    _HpnicfQoSTrafLmtConformDscp_Type()
)
hpnicfQoSTrafLmtConformDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafLmtConformDscp.setStatus("current")
_HpnicfQoSTrafficPriorityTable_Object = MibTable
hpnicfQoSTrafficPriorityTable = _HpnicfQoSTrafficPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfQoSTrafficPriorityTable.setStatus("current")
_HpnicfQoSTrafficPriorityEntry_Object = MibTableRow
hpnicfQoSTrafficPriorityEntry = _HpnicfQoSTrafficPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1)
)
hpnicfQoSTrafficPriorityEntry.setIndexNames(
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioProfIndex"),
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioActionIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQoSTrafficPriorityEntry.setStatus("current")


class _HpnicfQoSTrafPrioProfIndex_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQoSTrafPrioProfIndex_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioProfIndex_Object = MibTableColumn
hpnicfQoSTrafPrioProfIndex = _HpnicfQoSTrafPrioProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 1),
    _HpnicfQoSTrafPrioProfIndex_Type()
)
hpnicfQoSTrafPrioProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioProfIndex.setStatus("current")


class _HpnicfQoSTrafPrioActionIndex_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQoSTrafPrioActionIndex_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioActionIndex_Object = MibTableColumn
hpnicfQoSTrafPrioActionIndex = _HpnicfQoSTrafPrioActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 2),
    _HpnicfQoSTrafPrioActionIndex_Type()
)
hpnicfQoSTrafPrioActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioActionIndex.setStatus("current")
_HpnicfQoSTrafPrioDirection_Type = HpnicfQoSDirection
_HpnicfQoSTrafPrioDirection_Object = MibTableColumn
hpnicfQoSTrafPrioDirection = _HpnicfQoSTrafPrioDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 3),
    _HpnicfQoSTrafPrioDirection_Type()
)
hpnicfQoSTrafPrioDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioDirection.setStatus("current")


class _HpnicfQoSTrafPrioUserAclNum_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioUserAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
    )


_HpnicfQoSTrafPrioUserAclNum_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioUserAclNum_Object = MibTableColumn
hpnicfQoSTrafPrioUserAclNum = _HpnicfQoSTrafPrioUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 4),
    _HpnicfQoSTrafPrioUserAclNum_Type()
)
hpnicfQoSTrafPrioUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioUserAclNum.setStatus("current")


class _HpnicfQoSTrafPrioUserAclRule_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioUserAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSTrafPrioUserAclRule_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioUserAclRule_Object = MibTableColumn
hpnicfQoSTrafPrioUserAclRule = _HpnicfQoSTrafPrioUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 5),
    _HpnicfQoSTrafPrioUserAclRule_Type()
)
hpnicfQoSTrafPrioUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioUserAclRule.setStatus("current")


class _HpnicfQoSTrafPrioIpAclNum_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioIpAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HpnicfQoSTrafPrioIpAclNum_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioIpAclNum_Object = MibTableColumn
hpnicfQoSTrafPrioIpAclNum = _HpnicfQoSTrafPrioIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 6),
    _HpnicfQoSTrafPrioIpAclNum_Type()
)
hpnicfQoSTrafPrioIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioIpAclNum.setStatus("current")


class _HpnicfQoSTrafPrioIpAclRule_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioIpAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSTrafPrioIpAclRule_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioIpAclRule_Object = MibTableColumn
hpnicfQoSTrafPrioIpAclRule = _HpnicfQoSTrafPrioIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 7),
    _HpnicfQoSTrafPrioIpAclRule_Type()
)
hpnicfQoSTrafPrioIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioIpAclRule.setStatus("current")


class _HpnicfQoSTrafPrioLinkAclNum_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioLinkAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
    )


_HpnicfQoSTrafPrioLinkAclNum_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioLinkAclNum_Object = MibTableColumn
hpnicfQoSTrafPrioLinkAclNum = _HpnicfQoSTrafPrioLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 8),
    _HpnicfQoSTrafPrioLinkAclNum_Type()
)
hpnicfQoSTrafPrioLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioLinkAclNum.setStatus("current")


class _HpnicfQoSTrafPrioLinkAclRule_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioLinkAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSTrafPrioLinkAclRule_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioLinkAclRule_Object = MibTableColumn
hpnicfQoSTrafPrioLinkAclRule = _HpnicfQoSTrafPrioLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 9),
    _HpnicfQoSTrafPrioLinkAclRule_Type()
)
hpnicfQoSTrafPrioLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioLinkAclRule.setStatus("current")


class _HpnicfQoSTrafPrioDscp_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafPrioDscp_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioDscp_Object = MibTableColumn
hpnicfQoSTrafPrioDscp = _HpnicfQoSTrafPrioDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 10),
    _HpnicfQoSTrafPrioDscp_Type()
)
hpnicfQoSTrafPrioDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioDscp.setStatus("current")


class _HpnicfQoSTrafPrioIpPre_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioIpPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafPrioIpPre_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioIpPre_Object = MibTableColumn
hpnicfQoSTrafPrioIpPre = _HpnicfQoSTrafPrioIpPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 11),
    _HpnicfQoSTrafPrioIpPre_Type()
)
hpnicfQoSTrafPrioIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioIpPre.setStatus("current")


class _HpnicfQoSTrafPrioIpPreFromCos_Type(TruthValue):
    """Custom type hpnicfQoSTrafPrioIpPreFromCos based on TruthValue"""
    defaultValue = 2


_HpnicfQoSTrafPrioIpPreFromCos_Object = MibTableColumn
hpnicfQoSTrafPrioIpPreFromCos = _HpnicfQoSTrafPrioIpPreFromCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 12),
    _HpnicfQoSTrafPrioIpPreFromCos_Type()
)
hpnicfQoSTrafPrioIpPreFromCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioIpPreFromCos.setStatus("current")


class _HpnicfQoSTrafPrioCos_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafPrioCos_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioCos_Object = MibTableColumn
hpnicfQoSTrafPrioCos = _HpnicfQoSTrafPrioCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 13),
    _HpnicfQoSTrafPrioCos_Type()
)
hpnicfQoSTrafPrioCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioCos.setStatus("current")


class _HpnicfQoSTrafPrioCosFromIpPre_Type(TruthValue):
    """Custom type hpnicfQoSTrafPrioCosFromIpPre based on TruthValue"""
    defaultValue = 2


_HpnicfQoSTrafPrioCosFromIpPre_Object = MibTableColumn
hpnicfQoSTrafPrioCosFromIpPre = _HpnicfQoSTrafPrioCosFromIpPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 14),
    _HpnicfQoSTrafPrioCosFromIpPre_Type()
)
hpnicfQoSTrafPrioCosFromIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioCosFromIpPre.setStatus("current")


class _HpnicfQoSTrafPrioLocalPre_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioLocalPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafPrioLocalPre_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioLocalPre_Object = MibTableColumn
hpnicfQoSTrafPrioLocalPre = _HpnicfQoSTrafPrioLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 15),
    _HpnicfQoSTrafPrioLocalPre_Type()
)
hpnicfQoSTrafPrioLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioLocalPre.setStatus("current")


class _HpnicfQoSTrafPrioPolicedServiceType_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioPolicedServiceType based on Integer32"""
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


_HpnicfQoSTrafPrioPolicedServiceType_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioPolicedServiceType_Object = MibTableColumn
hpnicfQoSTrafPrioPolicedServiceType = _HpnicfQoSTrafPrioPolicedServiceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 16),
    _HpnicfQoSTrafPrioPolicedServiceType_Type()
)
hpnicfQoSTrafPrioPolicedServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioPolicedServiceType.setStatus("current")


class _HpnicfQoSTrafPrioPolicedServiceDscp_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioPolicedServiceDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafPrioPolicedServiceDscp_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioPolicedServiceDscp_Object = MibTableColumn
hpnicfQoSTrafPrioPolicedServiceDscp = _HpnicfQoSTrafPrioPolicedServiceDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 17),
    _HpnicfQoSTrafPrioPolicedServiceDscp_Type()
)
hpnicfQoSTrafPrioPolicedServiceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioPolicedServiceDscp.setStatus("current")


class _HpnicfQoSTrafPrioPolicedServiceExp_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioPolicedServiceExp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafPrioPolicedServiceExp_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioPolicedServiceExp_Object = MibTableColumn
hpnicfQoSTrafPrioPolicedServiceExp = _HpnicfQoSTrafPrioPolicedServiceExp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 18),
    _HpnicfQoSTrafPrioPolicedServiceExp_Type()
)
hpnicfQoSTrafPrioPolicedServiceExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioPolicedServiceExp.setStatus("current")


class _HpnicfQoSTrafPrioPolicedServiceCos_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioPolicedServiceCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafPrioPolicedServiceCos_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioPolicedServiceCos_Object = MibTableColumn
hpnicfQoSTrafPrioPolicedServiceCos = _HpnicfQoSTrafPrioPolicedServiceCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 19),
    _HpnicfQoSTrafPrioPolicedServiceCos_Type()
)
hpnicfQoSTrafPrioPolicedServiceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioPolicedServiceCos.setStatus("current")


class _HpnicfQoSTrafPrioPolicedServiceLoaclPre_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioPolicedServiceLoaclPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafPrioPolicedServiceLoaclPre_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioPolicedServiceLoaclPre_Object = MibTableColumn
hpnicfQoSTrafPrioPolicedServiceLoaclPre = _HpnicfQoSTrafPrioPolicedServiceLoaclPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 20),
    _HpnicfQoSTrafPrioPolicedServiceLoaclPre_Type()
)
hpnicfQoSTrafPrioPolicedServiceLoaclPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioPolicedServiceLoaclPre.setStatus("current")


class _HpnicfQoSTrafPrioPolicedServiceDropPriority_Type(Integer32):
    """Custom type hpnicfQoSTrafPrioPolicedServiceDropPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSTrafPrioPolicedServiceDropPriority_Type.__name__ = "Integer32"
_HpnicfQoSTrafPrioPolicedServiceDropPriority_Object = MibTableColumn
hpnicfQoSTrafPrioPolicedServiceDropPriority = _HpnicfQoSTrafPrioPolicedServiceDropPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 21),
    _HpnicfQoSTrafPrioPolicedServiceDropPriority_Type()
)
hpnicfQoSTrafPrioPolicedServiceDropPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioPolicedServiceDropPriority.setStatus("current")
_HpnicfQoSTrafPrioRowStatus_Type = RowStatus
_HpnicfQoSTrafPrioRowStatus_Object = MibTableColumn
hpnicfQoSTrafPrioRowStatus = _HpnicfQoSTrafPrioRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 2, 1, 22),
    _HpnicfQoSTrafPrioRowStatus_Type()
)
hpnicfQoSTrafPrioRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafPrioRowStatus.setStatus("current")
_HpnicfQoSTrafficFilterTable_Object = MibTable
hpnicfQoSTrafficFilterTable = _HpnicfQoSTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfQoSTrafficFilterTable.setStatus("current")
_HpnicfQoSTrafficFilterEntry_Object = MibTableRow
hpnicfQoSTrafficFilterEntry = _HpnicfQoSTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1)
)
hpnicfQoSTrafficFilterEntry.setIndexNames(
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafFilterProfIndex"),
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafFilterActionIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQoSTrafficFilterEntry.setStatus("current")


class _HpnicfQoSTrafFilterProfIndex_Type(Integer32):
    """Custom type hpnicfQoSTrafFilterProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQoSTrafFilterProfIndex_Type.__name__ = "Integer32"
_HpnicfQoSTrafFilterProfIndex_Object = MibTableColumn
hpnicfQoSTrafFilterProfIndex = _HpnicfQoSTrafFilterProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1, 1),
    _HpnicfQoSTrafFilterProfIndex_Type()
)
hpnicfQoSTrafFilterProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSTrafFilterProfIndex.setStatus("current")


class _HpnicfQoSTrafFilterActionIndex_Type(Integer32):
    """Custom type hpnicfQoSTrafFilterActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQoSTrafFilterActionIndex_Type.__name__ = "Integer32"
_HpnicfQoSTrafFilterActionIndex_Object = MibTableColumn
hpnicfQoSTrafFilterActionIndex = _HpnicfQoSTrafFilterActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1, 2),
    _HpnicfQoSTrafFilterActionIndex_Type()
)
hpnicfQoSTrafFilterActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSTrafFilterActionIndex.setStatus("current")
_HpnicfQoSTrafFilterDirection_Type = HpnicfQoSDirection
_HpnicfQoSTrafFilterDirection_Object = MibTableColumn
hpnicfQoSTrafFilterDirection = _HpnicfQoSTrafFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1, 3),
    _HpnicfQoSTrafFilterDirection_Type()
)
hpnicfQoSTrafFilterDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafFilterDirection.setStatus("current")


class _HpnicfQoSTrafFilterUserAclNum_Type(Integer32):
    """Custom type hpnicfQoSTrafFilterUserAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
    )


_HpnicfQoSTrafFilterUserAclNum_Type.__name__ = "Integer32"
_HpnicfQoSTrafFilterUserAclNum_Object = MibTableColumn
hpnicfQoSTrafFilterUserAclNum = _HpnicfQoSTrafFilterUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1, 4),
    _HpnicfQoSTrafFilterUserAclNum_Type()
)
hpnicfQoSTrafFilterUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafFilterUserAclNum.setStatus("current")


class _HpnicfQoSTrafFilterUserAclRule_Type(Integer32):
    """Custom type hpnicfQoSTrafFilterUserAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSTrafFilterUserAclRule_Type.__name__ = "Integer32"
_HpnicfQoSTrafFilterUserAclRule_Object = MibTableColumn
hpnicfQoSTrafFilterUserAclRule = _HpnicfQoSTrafFilterUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1, 5),
    _HpnicfQoSTrafFilterUserAclRule_Type()
)
hpnicfQoSTrafFilterUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafFilterUserAclRule.setStatus("current")


class _HpnicfQoSTrafFilterIpAclNum_Type(Integer32):
    """Custom type hpnicfQoSTrafFilterIpAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HpnicfQoSTrafFilterIpAclNum_Type.__name__ = "Integer32"
_HpnicfQoSTrafFilterIpAclNum_Object = MibTableColumn
hpnicfQoSTrafFilterIpAclNum = _HpnicfQoSTrafFilterIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1, 6),
    _HpnicfQoSTrafFilterIpAclNum_Type()
)
hpnicfQoSTrafFilterIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafFilterIpAclNum.setStatus("current")


class _HpnicfQoSTrafFilterIpAclRule_Type(Integer32):
    """Custom type hpnicfQoSTrafFilterIpAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSTrafFilterIpAclRule_Type.__name__ = "Integer32"
_HpnicfQoSTrafFilterIpAclRule_Object = MibTableColumn
hpnicfQoSTrafFilterIpAclRule = _HpnicfQoSTrafFilterIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1, 7),
    _HpnicfQoSTrafFilterIpAclRule_Type()
)
hpnicfQoSTrafFilterIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafFilterIpAclRule.setStatus("current")


class _HpnicfQoSTrafFilterLinkAclNum_Type(Integer32):
    """Custom type hpnicfQoSTrafFilterLinkAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
    )


_HpnicfQoSTrafFilterLinkAclNum_Type.__name__ = "Integer32"
_HpnicfQoSTrafFilterLinkAclNum_Object = MibTableColumn
hpnicfQoSTrafFilterLinkAclNum = _HpnicfQoSTrafFilterLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1, 8),
    _HpnicfQoSTrafFilterLinkAclNum_Type()
)
hpnicfQoSTrafFilterLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafFilterLinkAclNum.setStatus("current")


class _HpnicfQoSTrafFilterLinkAclRule_Type(Integer32):
    """Custom type hpnicfQoSTrafFilterLinkAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSTrafFilterLinkAclRule_Type.__name__ = "Integer32"
_HpnicfQoSTrafFilterLinkAclRule_Object = MibTableColumn
hpnicfQoSTrafFilterLinkAclRule = _HpnicfQoSTrafFilterLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1, 9),
    _HpnicfQoSTrafFilterLinkAclRule_Type()
)
hpnicfQoSTrafFilterLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafFilterLinkAclRule.setStatus("current")
_HpnicfQoSTrafFilterRowStatus_Type = RowStatus
_HpnicfQoSTrafFilterRowStatus_Object = MibTableColumn
hpnicfQoSTrafFilterRowStatus = _HpnicfQoSTrafFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 2, 3, 1, 10),
    _HpnicfQoSTrafFilterRowStatus_Type()
)
hpnicfQoSTrafFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSTrafFilterRowStatus.setStatus("current")
_HpnicfQoSProfPortMapping_ObjectIdentity = ObjectIdentity
hpnicfQoSProfPortMapping = _HpnicfQoSProfPortMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3)
)
_HpnicfQoSProfPortMappingTable_Object = MibTable
hpnicfQoSProfPortMappingTable = _HpnicfQoSProfPortMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingTable.setStatus("current")
_HpnicfQoSProfPortMappingEntry_Object = MibTableRow
hpnicfQoSProfPortMappingEntry = _HpnicfQoSProfPortMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 1, 1)
)
hpnicfQoSProfPortMappingEntry.setIndexNames(
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfPortMappingIfIndex"),
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfPortMappingProfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingEntry.setStatus("current")


class _HpnicfQoSProfPortMappingIfIndex_Type(Integer32):
    """Custom type hpnicfQoSProfPortMappingIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfQoSProfPortMappingIfIndex_Type.__name__ = "Integer32"
_HpnicfQoSProfPortMappingIfIndex_Object = MibTableColumn
hpnicfQoSProfPortMappingIfIndex = _HpnicfQoSProfPortMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 1, 1, 1),
    _HpnicfQoSProfPortMappingIfIndex_Type()
)
hpnicfQoSProfPortMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingIfIndex.setStatus("current")


class _HpnicfQoSProfPortMappingProfIndex_Type(Integer32):
    """Custom type hpnicfQoSProfPortMappingProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQoSProfPortMappingProfIndex_Type.__name__ = "Integer32"
_HpnicfQoSProfPortMappingProfIndex_Object = MibTableColumn
hpnicfQoSProfPortMappingProfIndex = _HpnicfQoSProfPortMappingProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 1, 1, 2),
    _HpnicfQoSProfPortMappingProfIndex_Type()
)
hpnicfQoSProfPortMappingProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingProfIndex.setStatus("current")
_HpnicfQoSProfPortMappingRowStatus_Type = RowStatus
_HpnicfQoSProfPortMappingRowStatus_Object = MibTableColumn
hpnicfQoSProfPortMappingRowStatus = _HpnicfQoSProfPortMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 1, 1, 3),
    _HpnicfQoSProfPortMappingRowStatus_Type()
)
hpnicfQoSProfPortMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingRowStatus.setStatus("current")
_HpnicfQoSProfPortMappingModeTable_Object = MibTable
hpnicfQoSProfPortMappingModeTable = _HpnicfQoSProfPortMappingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingModeTable.setStatus("current")
_HpnicfQoSProfPortMappingModeEntry_Object = MibTableRow
hpnicfQoSProfPortMappingModeEntry = _HpnicfQoSProfPortMappingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 2, 1)
)
hpnicfQoSProfPortMappingModeEntry.setIndexNames(
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfPortMappingModeIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingModeEntry.setStatus("current")


class _HpnicfQoSProfPortMappingModeIfIndex_Type(Integer32):
    """Custom type hpnicfQoSProfPortMappingModeIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfQoSProfPortMappingModeIfIndex_Type.__name__ = "Integer32"
_HpnicfQoSProfPortMappingModeIfIndex_Object = MibTableColumn
hpnicfQoSProfPortMappingModeIfIndex = _HpnicfQoSProfPortMappingModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 2, 1, 1),
    _HpnicfQoSProfPortMappingModeIfIndex_Type()
)
hpnicfQoSProfPortMappingModeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingModeIfIndex.setStatus("current")


class _HpnicfQoSProfPortMappingMode_Type(Integer32):
    """Custom type hpnicfQoSProfPortMappingMode based on Integer32"""
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


_HpnicfQoSProfPortMappingMode_Type.__name__ = "Integer32"
_HpnicfQoSProfPortMappingMode_Object = MibTableColumn
hpnicfQoSProfPortMappingMode = _HpnicfQoSProfPortMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 2, 1, 2),
    _HpnicfQoSProfPortMappingMode_Type()
)
hpnicfQoSProfPortMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingMode.setStatus("current")
_HpnicfQoSProfDynPortMappingTable_Object = MibTable
hpnicfQoSProfDynPortMappingTable = _HpnicfQoSProfDynPortMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfQoSProfDynPortMappingTable.setStatus("current")
_HpnicfQoSProfDynPortMappingEntry_Object = MibTableRow
hpnicfQoSProfDynPortMappingEntry = _HpnicfQoSProfDynPortMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 3, 1)
)
hpnicfQoSProfDynPortMappingEntry.setIndexNames(
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfDynPortMappingIfIndex"),
    (0, "HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfDynPortMappingUserSrcMAC"),
)
if mibBuilder.loadTexts:
    hpnicfQoSProfDynPortMappingEntry.setStatus("current")


class _HpnicfQoSProfDynPortMappingIfIndex_Type(Integer32):
    """Custom type hpnicfQoSProfDynPortMappingIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfQoSProfDynPortMappingIfIndex_Type.__name__ = "Integer32"
_HpnicfQoSProfDynPortMappingIfIndex_Object = MibTableColumn
hpnicfQoSProfDynPortMappingIfIndex = _HpnicfQoSProfDynPortMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 3, 1, 1),
    _HpnicfQoSProfDynPortMappingIfIndex_Type()
)
hpnicfQoSProfDynPortMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSProfDynPortMappingIfIndex.setStatus("current")
_HpnicfQoSProfDynPortMappingUserSrcMAC_Type = MacAddress
_HpnicfQoSProfDynPortMappingUserSrcMAC_Object = MibTableColumn
hpnicfQoSProfDynPortMappingUserSrcMAC = _HpnicfQoSProfDynPortMappingUserSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 3, 1, 2),
    _HpnicfQoSProfDynPortMappingUserSrcMAC_Type()
)
hpnicfQoSProfDynPortMappingUserSrcMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSProfDynPortMappingUserSrcMAC.setStatus("current")


class _HpnicfQoSProfDynPortMappingUserName_Type(OctetString):
    """Custom type hpnicfQoSProfDynPortMappingUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfQoSProfDynPortMappingUserName_Type.__name__ = "OctetString"
_HpnicfQoSProfDynPortMappingUserName_Object = MibTableColumn
hpnicfQoSProfDynPortMappingUserName = _HpnicfQoSProfDynPortMappingUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 3, 1, 3),
    _HpnicfQoSProfDynPortMappingUserName_Type()
)
hpnicfQoSProfDynPortMappingUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSProfDynPortMappingUserName.setStatus("current")
_HpnicfQoSProfDynPortMappingUserIPAddr_Type = IpAddress
_HpnicfQoSProfDynPortMappingUserIPAddr_Object = MibTableColumn
hpnicfQoSProfDynPortMappingUserIPAddr = _HpnicfQoSProfDynPortMappingUserIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 3, 1, 4),
    _HpnicfQoSProfDynPortMappingUserIPAddr_Type()
)
hpnicfQoSProfDynPortMappingUserIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSProfDynPortMappingUserIPAddr.setStatus("current")


class _HpnicfQoSProfDynPortMappingUserVLANID_Type(Integer32):
    """Custom type hpnicfQoSProfDynPortMappingUserVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfQoSProfDynPortMappingUserVLANID_Type.__name__ = "Integer32"
_HpnicfQoSProfDynPortMappingUserVLANID_Object = MibTableColumn
hpnicfQoSProfDynPortMappingUserVLANID = _HpnicfQoSProfDynPortMappingUserVLANID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 3, 1, 5),
    _HpnicfQoSProfDynPortMappingUserVLANID_Type()
)
hpnicfQoSProfDynPortMappingUserVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSProfDynPortMappingUserVLANID.setStatus("current")


class _HpnicfQoSProfDynPortMappingUserProfName_Type(OctetString):
    """Custom type hpnicfQoSProfDynPortMappingUserProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfQoSProfDynPortMappingUserProfName_Type.__name__ = "OctetString"
_HpnicfQoSProfDynPortMappingUserProfName_Object = MibTableColumn
hpnicfQoSProfDynPortMappingUserProfName = _HpnicfQoSProfDynPortMappingUserProfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 1, 3, 3, 1, 6),
    _HpnicfQoSProfDynPortMappingUserProfName_Type()
)
hpnicfQoSProfDynPortMappingUserProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSProfDynPortMappingUserProfName.setStatus("current")
_HpnicfQoSProfPortMappingTraps_ObjectIdentity = ObjectIdentity
hpnicfQoSProfPortMappingTraps = _HpnicfQoSProfPortMappingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 2)
)
_HpnicfQoSProfMibConformance_ObjectIdentity = ObjectIdentity
hpnicfQoSProfMibConformance = _HpnicfQoSProfMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 3)
)
_HpnicfQoSProfMibCompliances_ObjectIdentity = ObjectIdentity
hpnicfQoSProfMibCompliances = _HpnicfQoSProfMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 3, 1)
)
_HpnicfQoSProfMibGroups_ObjectIdentity = ObjectIdentity
hpnicfQoSProfMibGroups = _HpnicfQoSProfMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 3, 2)
)

# Managed Objects groups

hpnicfQoSProfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 3, 2, 1)
)
hpnicfQoSProfGroup.setObjects(
      *(("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfName"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfActionNumber"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfQoSProfGroup.setStatus("current")

hpnicfQoSActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 3, 2, 2)
)
hpnicfQoSActionGroup.setObjects(
      *(("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtDirection"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtUserAclNum"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtUserAclRule"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtIpAclNum"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtIpAclRule"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtLinkAclNum"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtLinkAclRule"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtTargetRateMbps"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtTargetRateKbps"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtPeakRate"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtCIR"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtCBS"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtEBS"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtPIR"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtConformLocalPre"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtConformActionType"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtExceedActionType"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtExceedDscp"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtExceedCos"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtRowStatus"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtConformCos"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafLmtConformDscp"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioDirection"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioUserAclNum"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioUserAclRule"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioIpAclNum"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioIpAclRule"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioLinkAclNum"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioLinkAclRule"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioDscp"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioIpPre"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioIpPreFromCos"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioCos"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioCosFromIpPre"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioLocalPre"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioPolicedServiceType"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioPolicedServiceDscp"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioPolicedServiceExp"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioPolicedServiceCos"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioPolicedServiceLoaclPre"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioPolicedServiceDropPriority"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafPrioRowStatus"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafFilterDirection"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafFilterUserAclNum"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafFilterUserAclRule"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafFilterIpAclNum"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafFilterIpAclRule"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafFilterLinkAclNum"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafFilterLinkAclRule"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSTrafFilterRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfQoSActionGroup.setStatus("current")

hpnicfQoSProfPortMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 3, 2, 3)
)
hpnicfQoSProfPortMappingGroup.setObjects(
      *(("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfPortMappingRowStatus"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfPortMappingMode"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfDynPortMappingUserName"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfDynPortMappingUserIPAddr"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfDynPortMappingUserVLANID"),
        ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfDynPortMappingUserProfName"))
)
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingGroup.setStatus("current")


# Notification objects

hpnicfQoSProfPortMappingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingError.setStatus(
        "current"
    )


# Notifications groups

hpnicfQoSProfPortMappingTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 3, 2, 4)
)
hpnicfQoSProfPortMappingTrapsGroup.setObjects(
    ("HPN-ICF-QOS-PROFILE-MIB", "hpnicfQoSProfPortMappingError")
)
if mibBuilder.loadTexts:
    hpnicfQoSProfPortMappingTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfQoSProfMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfQoSProfMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-QOS-PROFILE-MIB",
    **{"HpnicfQoSDirection": HpnicfQoSDirection,
       "hpnicfQosProfile": hpnicfQosProfile,
       "hpnicfQoSProfObjects": hpnicfQoSProfObjects,
       "hpnicfQoSProf": hpnicfQoSProf,
       "hpnicfQoSProfTable": hpnicfQoSProfTable,
       "hpnicfQoSProfEntry": hpnicfQoSProfEntry,
       "hpnicfQoSProfIndex": hpnicfQoSProfIndex,
       "hpnicfQoSProfName": hpnicfQoSProfName,
       "hpnicfQoSProfActionNumber": hpnicfQoSProfActionNumber,
       "hpnicfQoSProfRowStatus": hpnicfQoSProfRowStatus,
       "hpnicfQoSAction": hpnicfQoSAction,
       "hpnicfQoSTrafficLimitTable": hpnicfQoSTrafficLimitTable,
       "hpnicfQoSTrafficLimitEntry": hpnicfQoSTrafficLimitEntry,
       "hpnicfQoSTrafLmtProfIndex": hpnicfQoSTrafLmtProfIndex,
       "hpnicfQoSTrafLmtActionIndex": hpnicfQoSTrafLmtActionIndex,
       "hpnicfQoSTrafLmtDirection": hpnicfQoSTrafLmtDirection,
       "hpnicfQoSTrafLmtUserAclNum": hpnicfQoSTrafLmtUserAclNum,
       "hpnicfQoSTrafLmtUserAclRule": hpnicfQoSTrafLmtUserAclRule,
       "hpnicfQoSTrafLmtIpAclNum": hpnicfQoSTrafLmtIpAclNum,
       "hpnicfQoSTrafLmtIpAclRule": hpnicfQoSTrafLmtIpAclRule,
       "hpnicfQoSTrafLmtLinkAclNum": hpnicfQoSTrafLmtLinkAclNum,
       "hpnicfQoSTrafLmtLinkAclRule": hpnicfQoSTrafLmtLinkAclRule,
       "hpnicfQoSTrafLmtTargetRateMbps": hpnicfQoSTrafLmtTargetRateMbps,
       "hpnicfQoSTrafLmtTargetRateKbps": hpnicfQoSTrafLmtTargetRateKbps,
       "hpnicfQoSTrafLmtPeakRate": hpnicfQoSTrafLmtPeakRate,
       "hpnicfQoSTrafLmtCIR": hpnicfQoSTrafLmtCIR,
       "hpnicfQoSTrafLmtCBS": hpnicfQoSTrafLmtCBS,
       "hpnicfQoSTrafLmtEBS": hpnicfQoSTrafLmtEBS,
       "hpnicfQoSTrafLmtPIR": hpnicfQoSTrafLmtPIR,
       "hpnicfQoSTrafLmtConformLocalPre": hpnicfQoSTrafLmtConformLocalPre,
       "hpnicfQoSTrafLmtConformActionType": hpnicfQoSTrafLmtConformActionType,
       "hpnicfQoSTrafLmtExceedActionType": hpnicfQoSTrafLmtExceedActionType,
       "hpnicfQoSTrafLmtExceedDscp": hpnicfQoSTrafLmtExceedDscp,
       "hpnicfQoSTrafLmtExceedCos": hpnicfQoSTrafLmtExceedCos,
       "hpnicfQoSTrafLmtRowStatus": hpnicfQoSTrafLmtRowStatus,
       "hpnicfQoSTrafLmtConformCos": hpnicfQoSTrafLmtConformCos,
       "hpnicfQoSTrafLmtConformDscp": hpnicfQoSTrafLmtConformDscp,
       "hpnicfQoSTrafficPriorityTable": hpnicfQoSTrafficPriorityTable,
       "hpnicfQoSTrafficPriorityEntry": hpnicfQoSTrafficPriorityEntry,
       "hpnicfQoSTrafPrioProfIndex": hpnicfQoSTrafPrioProfIndex,
       "hpnicfQoSTrafPrioActionIndex": hpnicfQoSTrafPrioActionIndex,
       "hpnicfQoSTrafPrioDirection": hpnicfQoSTrafPrioDirection,
       "hpnicfQoSTrafPrioUserAclNum": hpnicfQoSTrafPrioUserAclNum,
       "hpnicfQoSTrafPrioUserAclRule": hpnicfQoSTrafPrioUserAclRule,
       "hpnicfQoSTrafPrioIpAclNum": hpnicfQoSTrafPrioIpAclNum,
       "hpnicfQoSTrafPrioIpAclRule": hpnicfQoSTrafPrioIpAclRule,
       "hpnicfQoSTrafPrioLinkAclNum": hpnicfQoSTrafPrioLinkAclNum,
       "hpnicfQoSTrafPrioLinkAclRule": hpnicfQoSTrafPrioLinkAclRule,
       "hpnicfQoSTrafPrioDscp": hpnicfQoSTrafPrioDscp,
       "hpnicfQoSTrafPrioIpPre": hpnicfQoSTrafPrioIpPre,
       "hpnicfQoSTrafPrioIpPreFromCos": hpnicfQoSTrafPrioIpPreFromCos,
       "hpnicfQoSTrafPrioCos": hpnicfQoSTrafPrioCos,
       "hpnicfQoSTrafPrioCosFromIpPre": hpnicfQoSTrafPrioCosFromIpPre,
       "hpnicfQoSTrafPrioLocalPre": hpnicfQoSTrafPrioLocalPre,
       "hpnicfQoSTrafPrioPolicedServiceType": hpnicfQoSTrafPrioPolicedServiceType,
       "hpnicfQoSTrafPrioPolicedServiceDscp": hpnicfQoSTrafPrioPolicedServiceDscp,
       "hpnicfQoSTrafPrioPolicedServiceExp": hpnicfQoSTrafPrioPolicedServiceExp,
       "hpnicfQoSTrafPrioPolicedServiceCos": hpnicfQoSTrafPrioPolicedServiceCos,
       "hpnicfQoSTrafPrioPolicedServiceLoaclPre": hpnicfQoSTrafPrioPolicedServiceLoaclPre,
       "hpnicfQoSTrafPrioPolicedServiceDropPriority": hpnicfQoSTrafPrioPolicedServiceDropPriority,
       "hpnicfQoSTrafPrioRowStatus": hpnicfQoSTrafPrioRowStatus,
       "hpnicfQoSTrafficFilterTable": hpnicfQoSTrafficFilterTable,
       "hpnicfQoSTrafficFilterEntry": hpnicfQoSTrafficFilterEntry,
       "hpnicfQoSTrafFilterProfIndex": hpnicfQoSTrafFilterProfIndex,
       "hpnicfQoSTrafFilterActionIndex": hpnicfQoSTrafFilterActionIndex,
       "hpnicfQoSTrafFilterDirection": hpnicfQoSTrafFilterDirection,
       "hpnicfQoSTrafFilterUserAclNum": hpnicfQoSTrafFilterUserAclNum,
       "hpnicfQoSTrafFilterUserAclRule": hpnicfQoSTrafFilterUserAclRule,
       "hpnicfQoSTrafFilterIpAclNum": hpnicfQoSTrafFilterIpAclNum,
       "hpnicfQoSTrafFilterIpAclRule": hpnicfQoSTrafFilterIpAclRule,
       "hpnicfQoSTrafFilterLinkAclNum": hpnicfQoSTrafFilterLinkAclNum,
       "hpnicfQoSTrafFilterLinkAclRule": hpnicfQoSTrafFilterLinkAclRule,
       "hpnicfQoSTrafFilterRowStatus": hpnicfQoSTrafFilterRowStatus,
       "hpnicfQoSProfPortMapping": hpnicfQoSProfPortMapping,
       "hpnicfQoSProfPortMappingTable": hpnicfQoSProfPortMappingTable,
       "hpnicfQoSProfPortMappingEntry": hpnicfQoSProfPortMappingEntry,
       "hpnicfQoSProfPortMappingIfIndex": hpnicfQoSProfPortMappingIfIndex,
       "hpnicfQoSProfPortMappingProfIndex": hpnicfQoSProfPortMappingProfIndex,
       "hpnicfQoSProfPortMappingRowStatus": hpnicfQoSProfPortMappingRowStatus,
       "hpnicfQoSProfPortMappingModeTable": hpnicfQoSProfPortMappingModeTable,
       "hpnicfQoSProfPortMappingModeEntry": hpnicfQoSProfPortMappingModeEntry,
       "hpnicfQoSProfPortMappingModeIfIndex": hpnicfQoSProfPortMappingModeIfIndex,
       "hpnicfQoSProfPortMappingMode": hpnicfQoSProfPortMappingMode,
       "hpnicfQoSProfDynPortMappingTable": hpnicfQoSProfDynPortMappingTable,
       "hpnicfQoSProfDynPortMappingEntry": hpnicfQoSProfDynPortMappingEntry,
       "hpnicfQoSProfDynPortMappingIfIndex": hpnicfQoSProfDynPortMappingIfIndex,
       "hpnicfQoSProfDynPortMappingUserSrcMAC": hpnicfQoSProfDynPortMappingUserSrcMAC,
       "hpnicfQoSProfDynPortMappingUserName": hpnicfQoSProfDynPortMappingUserName,
       "hpnicfQoSProfDynPortMappingUserIPAddr": hpnicfQoSProfDynPortMappingUserIPAddr,
       "hpnicfQoSProfDynPortMappingUserVLANID": hpnicfQoSProfDynPortMappingUserVLANID,
       "hpnicfQoSProfDynPortMappingUserProfName": hpnicfQoSProfDynPortMappingUserProfName,
       "hpnicfQoSProfPortMappingTraps": hpnicfQoSProfPortMappingTraps,
       "hpnicfQoSProfPortMappingError": hpnicfQoSProfPortMappingError,
       "hpnicfQoSProfMibConformance": hpnicfQoSProfMibConformance,
       "hpnicfQoSProfMibCompliances": hpnicfQoSProfMibCompliances,
       "hpnicfQoSProfMibCompliance": hpnicfQoSProfMibCompliance,
       "hpnicfQoSProfMibGroups": hpnicfQoSProfMibGroups,
       "hpnicfQoSProfGroup": hpnicfQoSProfGroup,
       "hpnicfQoSActionGroup": hpnicfQoSActionGroup,
       "hpnicfQoSProfPortMappingGroup": hpnicfQoSProfPortMappingGroup,
       "hpnicfQoSProfPortMappingTrapsGroup": hpnicfQoSProfPortMappingTrapsGroup}
)
