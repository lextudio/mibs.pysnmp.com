# SNMP MIB module (HH3C-QOS-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-QOS-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:39 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cQosProfile = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cQoSDirection(Integer32, TextualConvention):
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

_Hh3cQoSProfObjects_ObjectIdentity = ObjectIdentity
hh3cQoSProfObjects = _Hh3cQoSProfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1)
)
_Hh3cQoSProf_ObjectIdentity = ObjectIdentity
hh3cQoSProf = _Hh3cQoSProf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 1)
)
_Hh3cQoSProfTable_Object = MibTable
hh3cQoSProfTable = _Hh3cQoSProfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cQoSProfTable.setStatus("current")
_Hh3cQoSProfEntry_Object = MibTableRow
hh3cQoSProfEntry = _Hh3cQoSProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 1, 1, 1)
)
hh3cQoSProfEntry.setIndexNames(
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSProfIndex"),
)
if mibBuilder.loadTexts:
    hh3cQoSProfEntry.setStatus("current")


class _Hh3cQoSProfIndex_Type(Integer32):
    """Custom type hh3cQoSProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQoSProfIndex_Type.__name__ = "Integer32"
_Hh3cQoSProfIndex_Object = MibTableColumn
hh3cQoSProfIndex = _Hh3cQoSProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 1, 1, 1, 1),
    _Hh3cQoSProfIndex_Type()
)
hh3cQoSProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSProfIndex.setStatus("current")


class _Hh3cQoSProfName_Type(OctetString):
    """Custom type hh3cQoSProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cQoSProfName_Type.__name__ = "OctetString"
_Hh3cQoSProfName_Object = MibTableColumn
hh3cQoSProfName = _Hh3cQoSProfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 1, 1, 1, 2),
    _Hh3cQoSProfName_Type()
)
hh3cQoSProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSProfName.setStatus("current")


class _Hh3cQoSProfActionNumber_Type(Integer32):
    """Custom type hh3cQoSProfActionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cQoSProfActionNumber_Type.__name__ = "Integer32"
_Hh3cQoSProfActionNumber_Object = MibTableColumn
hh3cQoSProfActionNumber = _Hh3cQoSProfActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 1, 1, 1, 3),
    _Hh3cQoSProfActionNumber_Type()
)
hh3cQoSProfActionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSProfActionNumber.setStatus("current")
_Hh3cQoSProfRowStatus_Type = RowStatus
_Hh3cQoSProfRowStatus_Object = MibTableColumn
hh3cQoSProfRowStatus = _Hh3cQoSProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 1, 1, 1, 4),
    _Hh3cQoSProfRowStatus_Type()
)
hh3cQoSProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSProfRowStatus.setStatus("current")
_Hh3cQoSAction_ObjectIdentity = ObjectIdentity
hh3cQoSAction = _Hh3cQoSAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2)
)
_Hh3cQoSTrafficLimitTable_Object = MibTable
hh3cQoSTrafficLimitTable = _Hh3cQoSTrafficLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cQoSTrafficLimitTable.setStatus("current")
_Hh3cQoSTrafficLimitEntry_Object = MibTableRow
hh3cQoSTrafficLimitEntry = _Hh3cQoSTrafficLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1)
)
hh3cQoSTrafficLimitEntry.setIndexNames(
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtProfIndex"),
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtActionIndex"),
)
if mibBuilder.loadTexts:
    hh3cQoSTrafficLimitEntry.setStatus("current")


class _Hh3cQoSTrafLmtProfIndex_Type(Integer32):
    """Custom type hh3cQoSTrafLmtProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQoSTrafLmtProfIndex_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtProfIndex_Object = MibTableColumn
hh3cQoSTrafLmtProfIndex = _Hh3cQoSTrafLmtProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 1),
    _Hh3cQoSTrafLmtProfIndex_Type()
)
hh3cQoSTrafLmtProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtProfIndex.setStatus("current")


class _Hh3cQoSTrafLmtActionIndex_Type(Integer32):
    """Custom type hh3cQoSTrafLmtActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQoSTrafLmtActionIndex_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtActionIndex_Object = MibTableColumn
hh3cQoSTrafLmtActionIndex = _Hh3cQoSTrafLmtActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 2),
    _Hh3cQoSTrafLmtActionIndex_Type()
)
hh3cQoSTrafLmtActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtActionIndex.setStatus("current")
_Hh3cQoSTrafLmtDirection_Type = Hh3cQoSDirection
_Hh3cQoSTrafLmtDirection_Object = MibTableColumn
hh3cQoSTrafLmtDirection = _Hh3cQoSTrafLmtDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 3),
    _Hh3cQoSTrafLmtDirection_Type()
)
hh3cQoSTrafLmtDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtDirection.setStatus("current")


class _Hh3cQoSTrafLmtUserAclNum_Type(Integer32):
    """Custom type hh3cQoSTrafLmtUserAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
    )


_Hh3cQoSTrafLmtUserAclNum_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtUserAclNum_Object = MibTableColumn
hh3cQoSTrafLmtUserAclNum = _Hh3cQoSTrafLmtUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 4),
    _Hh3cQoSTrafLmtUserAclNum_Type()
)
hh3cQoSTrafLmtUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtUserAclNum.setStatus("current")


class _Hh3cQoSTrafLmtUserAclRule_Type(Integer32):
    """Custom type hh3cQoSTrafLmtUserAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cQoSTrafLmtUserAclRule_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtUserAclRule_Object = MibTableColumn
hh3cQoSTrafLmtUserAclRule = _Hh3cQoSTrafLmtUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 5),
    _Hh3cQoSTrafLmtUserAclRule_Type()
)
hh3cQoSTrafLmtUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtUserAclRule.setStatus("current")


class _Hh3cQoSTrafLmtIpAclNum_Type(Integer32):
    """Custom type hh3cQoSTrafLmtIpAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cQoSTrafLmtIpAclNum_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtIpAclNum_Object = MibTableColumn
hh3cQoSTrafLmtIpAclNum = _Hh3cQoSTrafLmtIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 6),
    _Hh3cQoSTrafLmtIpAclNum_Type()
)
hh3cQoSTrafLmtIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtIpAclNum.setStatus("current")


class _Hh3cQoSTrafLmtIpAclRule_Type(Integer32):
    """Custom type hh3cQoSTrafLmtIpAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cQoSTrafLmtIpAclRule_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtIpAclRule_Object = MibTableColumn
hh3cQoSTrafLmtIpAclRule = _Hh3cQoSTrafLmtIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 7),
    _Hh3cQoSTrafLmtIpAclRule_Type()
)
hh3cQoSTrafLmtIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtIpAclRule.setStatus("current")


class _Hh3cQoSTrafLmtLinkAclNum_Type(Integer32):
    """Custom type hh3cQoSTrafLmtLinkAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
    )


_Hh3cQoSTrafLmtLinkAclNum_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtLinkAclNum_Object = MibTableColumn
hh3cQoSTrafLmtLinkAclNum = _Hh3cQoSTrafLmtLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 8),
    _Hh3cQoSTrafLmtLinkAclNum_Type()
)
hh3cQoSTrafLmtLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtLinkAclNum.setStatus("current")


class _Hh3cQoSTrafLmtLinkAclRule_Type(Integer32):
    """Custom type hh3cQoSTrafLmtLinkAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cQoSTrafLmtLinkAclRule_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtLinkAclRule_Object = MibTableColumn
hh3cQoSTrafLmtLinkAclRule = _Hh3cQoSTrafLmtLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 9),
    _Hh3cQoSTrafLmtLinkAclRule_Type()
)
hh3cQoSTrafLmtLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtLinkAclRule.setStatus("current")


class _Hh3cQoSTrafLmtTargetRateMbps_Type(Integer32):
    """Custom type hh3cQoSTrafLmtTargetRateMbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Hh3cQoSTrafLmtTargetRateMbps_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtTargetRateMbps_Object = MibTableColumn
hh3cQoSTrafLmtTargetRateMbps = _Hh3cQoSTrafLmtTargetRateMbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 10),
    _Hh3cQoSTrafLmtTargetRateMbps_Type()
)
hh3cQoSTrafLmtTargetRateMbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtTargetRateMbps.setStatus("current")


class _Hh3cQoSTrafLmtTargetRateKbps_Type(Integer32):
    """Custom type hh3cQoSTrafLmtTargetRateKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_Hh3cQoSTrafLmtTargetRateKbps_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtTargetRateKbps_Object = MibTableColumn
hh3cQoSTrafLmtTargetRateKbps = _Hh3cQoSTrafLmtTargetRateKbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 11),
    _Hh3cQoSTrafLmtTargetRateKbps_Type()
)
hh3cQoSTrafLmtTargetRateKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtTargetRateKbps.setStatus("current")


class _Hh3cQoSTrafLmtPeakRate_Type(Integer32):
    """Custom type hh3cQoSTrafLmtPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 8388608),
    )


_Hh3cQoSTrafLmtPeakRate_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtPeakRate_Object = MibTableColumn
hh3cQoSTrafLmtPeakRate = _Hh3cQoSTrafLmtPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 12),
    _Hh3cQoSTrafLmtPeakRate_Type()
)
hh3cQoSTrafLmtPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtPeakRate.setStatus("current")


class _Hh3cQoSTrafLmtCIR_Type(Integer32):
    """Custom type hh3cQoSTrafLmtCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_Hh3cQoSTrafLmtCIR_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtCIR_Object = MibTableColumn
hh3cQoSTrafLmtCIR = _Hh3cQoSTrafLmtCIR_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 13),
    _Hh3cQoSTrafLmtCIR_Type()
)
hh3cQoSTrafLmtCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtCIR.setStatus("current")


class _Hh3cQoSTrafLmtCBS_Type(Integer32):
    """Custom type hh3cQoSTrafLmtCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_Hh3cQoSTrafLmtCBS_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtCBS_Object = MibTableColumn
hh3cQoSTrafLmtCBS = _Hh3cQoSTrafLmtCBS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 14),
    _Hh3cQoSTrafLmtCBS_Type()
)
hh3cQoSTrafLmtCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtCBS.setStatus("current")


class _Hh3cQoSTrafLmtEBS_Type(Integer32):
    """Custom type hh3cQoSTrafLmtEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_Hh3cQoSTrafLmtEBS_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtEBS_Object = MibTableColumn
hh3cQoSTrafLmtEBS = _Hh3cQoSTrafLmtEBS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 15),
    _Hh3cQoSTrafLmtEBS_Type()
)
hh3cQoSTrafLmtEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtEBS.setStatus("current")


class _Hh3cQoSTrafLmtPIR_Type(Integer32):
    """Custom type hh3cQoSTrafLmtPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_Hh3cQoSTrafLmtPIR_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtPIR_Object = MibTableColumn
hh3cQoSTrafLmtPIR = _Hh3cQoSTrafLmtPIR_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 16),
    _Hh3cQoSTrafLmtPIR_Type()
)
hh3cQoSTrafLmtPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtPIR.setStatus("current")


class _Hh3cQoSTrafLmtConformLocalPre_Type(Integer32):
    """Custom type hh3cQoSTrafLmtConformLocalPre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cQoSTrafLmtConformLocalPre_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtConformLocalPre_Object = MibTableColumn
hh3cQoSTrafLmtConformLocalPre = _Hh3cQoSTrafLmtConformLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 17),
    _Hh3cQoSTrafLmtConformLocalPre_Type()
)
hh3cQoSTrafLmtConformLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtConformLocalPre.setStatus("current")


class _Hh3cQoSTrafLmtConformActionType_Type(Integer32):
    """Custom type hh3cQoSTrafLmtConformActionType based on Integer32"""
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


_Hh3cQoSTrafLmtConformActionType_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtConformActionType_Object = MibTableColumn
hh3cQoSTrafLmtConformActionType = _Hh3cQoSTrafLmtConformActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 18),
    _Hh3cQoSTrafLmtConformActionType_Type()
)
hh3cQoSTrafLmtConformActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtConformActionType.setStatus("current")


class _Hh3cQoSTrafLmtExceedActionType_Type(Integer32):
    """Custom type hh3cQoSTrafLmtExceedActionType based on Integer32"""
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


_Hh3cQoSTrafLmtExceedActionType_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtExceedActionType_Object = MibTableColumn
hh3cQoSTrafLmtExceedActionType = _Hh3cQoSTrafLmtExceedActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 19),
    _Hh3cQoSTrafLmtExceedActionType_Type()
)
hh3cQoSTrafLmtExceedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtExceedActionType.setStatus("current")


class _Hh3cQoSTrafLmtExceedDscp_Type(Integer32):
    """Custom type hh3cQoSTrafLmtExceedDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafLmtExceedDscp_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtExceedDscp_Object = MibTableColumn
hh3cQoSTrafLmtExceedDscp = _Hh3cQoSTrafLmtExceedDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 20),
    _Hh3cQoSTrafLmtExceedDscp_Type()
)
hh3cQoSTrafLmtExceedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtExceedDscp.setStatus("current")


class _Hh3cQoSTrafLmtExceedCos_Type(Integer32):
    """Custom type hh3cQoSTrafLmtExceedCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafLmtExceedCos_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtExceedCos_Object = MibTableColumn
hh3cQoSTrafLmtExceedCos = _Hh3cQoSTrafLmtExceedCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 21),
    _Hh3cQoSTrafLmtExceedCos_Type()
)
hh3cQoSTrafLmtExceedCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtExceedCos.setStatus("current")
_Hh3cQoSTrafLmtRowStatus_Type = RowStatus
_Hh3cQoSTrafLmtRowStatus_Object = MibTableColumn
hh3cQoSTrafLmtRowStatus = _Hh3cQoSTrafLmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 22),
    _Hh3cQoSTrafLmtRowStatus_Type()
)
hh3cQoSTrafLmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtRowStatus.setStatus("current")


class _Hh3cQoSTrafLmtConformCos_Type(Integer32):
    """Custom type hh3cQoSTrafLmtConformCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafLmtConformCos_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtConformCos_Object = MibTableColumn
hh3cQoSTrafLmtConformCos = _Hh3cQoSTrafLmtConformCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 23),
    _Hh3cQoSTrafLmtConformCos_Type()
)
hh3cQoSTrafLmtConformCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtConformCos.setStatus("current")


class _Hh3cQoSTrafLmtConformDscp_Type(Integer32):
    """Custom type hh3cQoSTrafLmtConformDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafLmtConformDscp_Type.__name__ = "Integer32"
_Hh3cQoSTrafLmtConformDscp_Object = MibTableColumn
hh3cQoSTrafLmtConformDscp = _Hh3cQoSTrafLmtConformDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 1, 1, 24),
    _Hh3cQoSTrafLmtConformDscp_Type()
)
hh3cQoSTrafLmtConformDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafLmtConformDscp.setStatus("current")
_Hh3cQoSTrafficPriorityTable_Object = MibTable
hh3cQoSTrafficPriorityTable = _Hh3cQoSTrafficPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cQoSTrafficPriorityTable.setStatus("current")
_Hh3cQoSTrafficPriorityEntry_Object = MibTableRow
hh3cQoSTrafficPriorityEntry = _Hh3cQoSTrafficPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1)
)
hh3cQoSTrafficPriorityEntry.setIndexNames(
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioProfIndex"),
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioActionIndex"),
)
if mibBuilder.loadTexts:
    hh3cQoSTrafficPriorityEntry.setStatus("current")


class _Hh3cQoSTrafPrioProfIndex_Type(Integer32):
    """Custom type hh3cQoSTrafPrioProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQoSTrafPrioProfIndex_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioProfIndex_Object = MibTableColumn
hh3cQoSTrafPrioProfIndex = _Hh3cQoSTrafPrioProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 1),
    _Hh3cQoSTrafPrioProfIndex_Type()
)
hh3cQoSTrafPrioProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioProfIndex.setStatus("current")


class _Hh3cQoSTrafPrioActionIndex_Type(Integer32):
    """Custom type hh3cQoSTrafPrioActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQoSTrafPrioActionIndex_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioActionIndex_Object = MibTableColumn
hh3cQoSTrafPrioActionIndex = _Hh3cQoSTrafPrioActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 2),
    _Hh3cQoSTrafPrioActionIndex_Type()
)
hh3cQoSTrafPrioActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioActionIndex.setStatus("current")
_Hh3cQoSTrafPrioDirection_Type = Hh3cQoSDirection
_Hh3cQoSTrafPrioDirection_Object = MibTableColumn
hh3cQoSTrafPrioDirection = _Hh3cQoSTrafPrioDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 3),
    _Hh3cQoSTrafPrioDirection_Type()
)
hh3cQoSTrafPrioDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioDirection.setStatus("current")


class _Hh3cQoSTrafPrioUserAclNum_Type(Integer32):
    """Custom type hh3cQoSTrafPrioUserAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
    )


_Hh3cQoSTrafPrioUserAclNum_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioUserAclNum_Object = MibTableColumn
hh3cQoSTrafPrioUserAclNum = _Hh3cQoSTrafPrioUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 4),
    _Hh3cQoSTrafPrioUserAclNum_Type()
)
hh3cQoSTrafPrioUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioUserAclNum.setStatus("current")


class _Hh3cQoSTrafPrioUserAclRule_Type(Integer32):
    """Custom type hh3cQoSTrafPrioUserAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cQoSTrafPrioUserAclRule_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioUserAclRule_Object = MibTableColumn
hh3cQoSTrafPrioUserAclRule = _Hh3cQoSTrafPrioUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 5),
    _Hh3cQoSTrafPrioUserAclRule_Type()
)
hh3cQoSTrafPrioUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioUserAclRule.setStatus("current")


class _Hh3cQoSTrafPrioIpAclNum_Type(Integer32):
    """Custom type hh3cQoSTrafPrioIpAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cQoSTrafPrioIpAclNum_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioIpAclNum_Object = MibTableColumn
hh3cQoSTrafPrioIpAclNum = _Hh3cQoSTrafPrioIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 6),
    _Hh3cQoSTrafPrioIpAclNum_Type()
)
hh3cQoSTrafPrioIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioIpAclNum.setStatus("current")


class _Hh3cQoSTrafPrioIpAclRule_Type(Integer32):
    """Custom type hh3cQoSTrafPrioIpAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cQoSTrafPrioIpAclRule_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioIpAclRule_Object = MibTableColumn
hh3cQoSTrafPrioIpAclRule = _Hh3cQoSTrafPrioIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 7),
    _Hh3cQoSTrafPrioIpAclRule_Type()
)
hh3cQoSTrafPrioIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioIpAclRule.setStatus("current")


class _Hh3cQoSTrafPrioLinkAclNum_Type(Integer32):
    """Custom type hh3cQoSTrafPrioLinkAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
    )


_Hh3cQoSTrafPrioLinkAclNum_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioLinkAclNum_Object = MibTableColumn
hh3cQoSTrafPrioLinkAclNum = _Hh3cQoSTrafPrioLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 8),
    _Hh3cQoSTrafPrioLinkAclNum_Type()
)
hh3cQoSTrafPrioLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioLinkAclNum.setStatus("current")


class _Hh3cQoSTrafPrioLinkAclRule_Type(Integer32):
    """Custom type hh3cQoSTrafPrioLinkAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cQoSTrafPrioLinkAclRule_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioLinkAclRule_Object = MibTableColumn
hh3cQoSTrafPrioLinkAclRule = _Hh3cQoSTrafPrioLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 9),
    _Hh3cQoSTrafPrioLinkAclRule_Type()
)
hh3cQoSTrafPrioLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioLinkAclRule.setStatus("current")


class _Hh3cQoSTrafPrioDscp_Type(Integer32):
    """Custom type hh3cQoSTrafPrioDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafPrioDscp_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioDscp_Object = MibTableColumn
hh3cQoSTrafPrioDscp = _Hh3cQoSTrafPrioDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 10),
    _Hh3cQoSTrafPrioDscp_Type()
)
hh3cQoSTrafPrioDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioDscp.setStatus("current")


class _Hh3cQoSTrafPrioIpPre_Type(Integer32):
    """Custom type hh3cQoSTrafPrioIpPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafPrioIpPre_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioIpPre_Object = MibTableColumn
hh3cQoSTrafPrioIpPre = _Hh3cQoSTrafPrioIpPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 11),
    _Hh3cQoSTrafPrioIpPre_Type()
)
hh3cQoSTrafPrioIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioIpPre.setStatus("current")


class _Hh3cQoSTrafPrioIpPreFromCos_Type(TruthValue):
    """Custom type hh3cQoSTrafPrioIpPreFromCos based on TruthValue"""
    defaultValue = 2


_Hh3cQoSTrafPrioIpPreFromCos_Object = MibTableColumn
hh3cQoSTrafPrioIpPreFromCos = _Hh3cQoSTrafPrioIpPreFromCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 12),
    _Hh3cQoSTrafPrioIpPreFromCos_Type()
)
hh3cQoSTrafPrioIpPreFromCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioIpPreFromCos.setStatus("current")


class _Hh3cQoSTrafPrioCos_Type(Integer32):
    """Custom type hh3cQoSTrafPrioCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafPrioCos_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioCos_Object = MibTableColumn
hh3cQoSTrafPrioCos = _Hh3cQoSTrafPrioCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 13),
    _Hh3cQoSTrafPrioCos_Type()
)
hh3cQoSTrafPrioCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioCos.setStatus("current")


class _Hh3cQoSTrafPrioCosFromIpPre_Type(TruthValue):
    """Custom type hh3cQoSTrafPrioCosFromIpPre based on TruthValue"""
    defaultValue = 2


_Hh3cQoSTrafPrioCosFromIpPre_Object = MibTableColumn
hh3cQoSTrafPrioCosFromIpPre = _Hh3cQoSTrafPrioCosFromIpPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 14),
    _Hh3cQoSTrafPrioCosFromIpPre_Type()
)
hh3cQoSTrafPrioCosFromIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioCosFromIpPre.setStatus("current")


class _Hh3cQoSTrafPrioLocalPre_Type(Integer32):
    """Custom type hh3cQoSTrafPrioLocalPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafPrioLocalPre_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioLocalPre_Object = MibTableColumn
hh3cQoSTrafPrioLocalPre = _Hh3cQoSTrafPrioLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 15),
    _Hh3cQoSTrafPrioLocalPre_Type()
)
hh3cQoSTrafPrioLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioLocalPre.setStatus("current")


class _Hh3cQoSTrafPrioPolicedServiceType_Type(Integer32):
    """Custom type hh3cQoSTrafPrioPolicedServiceType based on Integer32"""
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


_Hh3cQoSTrafPrioPolicedServiceType_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioPolicedServiceType_Object = MibTableColumn
hh3cQoSTrafPrioPolicedServiceType = _Hh3cQoSTrafPrioPolicedServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 16),
    _Hh3cQoSTrafPrioPolicedServiceType_Type()
)
hh3cQoSTrafPrioPolicedServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioPolicedServiceType.setStatus("current")


class _Hh3cQoSTrafPrioPolicedServiceDscp_Type(Integer32):
    """Custom type hh3cQoSTrafPrioPolicedServiceDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafPrioPolicedServiceDscp_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioPolicedServiceDscp_Object = MibTableColumn
hh3cQoSTrafPrioPolicedServiceDscp = _Hh3cQoSTrafPrioPolicedServiceDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 17),
    _Hh3cQoSTrafPrioPolicedServiceDscp_Type()
)
hh3cQoSTrafPrioPolicedServiceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioPolicedServiceDscp.setStatus("current")


class _Hh3cQoSTrafPrioPolicedServiceExp_Type(Integer32):
    """Custom type hh3cQoSTrafPrioPolicedServiceExp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafPrioPolicedServiceExp_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioPolicedServiceExp_Object = MibTableColumn
hh3cQoSTrafPrioPolicedServiceExp = _Hh3cQoSTrafPrioPolicedServiceExp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 18),
    _Hh3cQoSTrafPrioPolicedServiceExp_Type()
)
hh3cQoSTrafPrioPolicedServiceExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioPolicedServiceExp.setStatus("current")


class _Hh3cQoSTrafPrioPolicedServiceCos_Type(Integer32):
    """Custom type hh3cQoSTrafPrioPolicedServiceCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafPrioPolicedServiceCos_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioPolicedServiceCos_Object = MibTableColumn
hh3cQoSTrafPrioPolicedServiceCos = _Hh3cQoSTrafPrioPolicedServiceCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 19),
    _Hh3cQoSTrafPrioPolicedServiceCos_Type()
)
hh3cQoSTrafPrioPolicedServiceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioPolicedServiceCos.setStatus("current")


class _Hh3cQoSTrafPrioPolicedServiceLoaclPre_Type(Integer32):
    """Custom type hh3cQoSTrafPrioPolicedServiceLoaclPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafPrioPolicedServiceLoaclPre_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioPolicedServiceLoaclPre_Object = MibTableColumn
hh3cQoSTrafPrioPolicedServiceLoaclPre = _Hh3cQoSTrafPrioPolicedServiceLoaclPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 20),
    _Hh3cQoSTrafPrioPolicedServiceLoaclPre_Type()
)
hh3cQoSTrafPrioPolicedServiceLoaclPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioPolicedServiceLoaclPre.setStatus("current")


class _Hh3cQoSTrafPrioPolicedServiceDropPriority_Type(Integer32):
    """Custom type hh3cQoSTrafPrioPolicedServiceDropPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(255, 255),
    )


_Hh3cQoSTrafPrioPolicedServiceDropPriority_Type.__name__ = "Integer32"
_Hh3cQoSTrafPrioPolicedServiceDropPriority_Object = MibTableColumn
hh3cQoSTrafPrioPolicedServiceDropPriority = _Hh3cQoSTrafPrioPolicedServiceDropPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 21),
    _Hh3cQoSTrafPrioPolicedServiceDropPriority_Type()
)
hh3cQoSTrafPrioPolicedServiceDropPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioPolicedServiceDropPriority.setStatus("current")
_Hh3cQoSTrafPrioRowStatus_Type = RowStatus
_Hh3cQoSTrafPrioRowStatus_Object = MibTableColumn
hh3cQoSTrafPrioRowStatus = _Hh3cQoSTrafPrioRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 2, 1, 22),
    _Hh3cQoSTrafPrioRowStatus_Type()
)
hh3cQoSTrafPrioRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafPrioRowStatus.setStatus("current")
_Hh3cQoSTrafficFilterTable_Object = MibTable
hh3cQoSTrafficFilterTable = _Hh3cQoSTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cQoSTrafficFilterTable.setStatus("current")
_Hh3cQoSTrafficFilterEntry_Object = MibTableRow
hh3cQoSTrafficFilterEntry = _Hh3cQoSTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1)
)
hh3cQoSTrafficFilterEntry.setIndexNames(
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafFilterProfIndex"),
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafFilterActionIndex"),
)
if mibBuilder.loadTexts:
    hh3cQoSTrafficFilterEntry.setStatus("current")


class _Hh3cQoSTrafFilterProfIndex_Type(Integer32):
    """Custom type hh3cQoSTrafFilterProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQoSTrafFilterProfIndex_Type.__name__ = "Integer32"
_Hh3cQoSTrafFilterProfIndex_Object = MibTableColumn
hh3cQoSTrafFilterProfIndex = _Hh3cQoSTrafFilterProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1, 1),
    _Hh3cQoSTrafFilterProfIndex_Type()
)
hh3cQoSTrafFilterProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSTrafFilterProfIndex.setStatus("current")


class _Hh3cQoSTrafFilterActionIndex_Type(Integer32):
    """Custom type hh3cQoSTrafFilterActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQoSTrafFilterActionIndex_Type.__name__ = "Integer32"
_Hh3cQoSTrafFilterActionIndex_Object = MibTableColumn
hh3cQoSTrafFilterActionIndex = _Hh3cQoSTrafFilterActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1, 2),
    _Hh3cQoSTrafFilterActionIndex_Type()
)
hh3cQoSTrafFilterActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSTrafFilterActionIndex.setStatus("current")
_Hh3cQoSTrafFilterDirection_Type = Hh3cQoSDirection
_Hh3cQoSTrafFilterDirection_Object = MibTableColumn
hh3cQoSTrafFilterDirection = _Hh3cQoSTrafFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1, 3),
    _Hh3cQoSTrafFilterDirection_Type()
)
hh3cQoSTrafFilterDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafFilterDirection.setStatus("current")


class _Hh3cQoSTrafFilterUserAclNum_Type(Integer32):
    """Custom type hh3cQoSTrafFilterUserAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
    )


_Hh3cQoSTrafFilterUserAclNum_Type.__name__ = "Integer32"
_Hh3cQoSTrafFilterUserAclNum_Object = MibTableColumn
hh3cQoSTrafFilterUserAclNum = _Hh3cQoSTrafFilterUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1, 4),
    _Hh3cQoSTrafFilterUserAclNum_Type()
)
hh3cQoSTrafFilterUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafFilterUserAclNum.setStatus("current")


class _Hh3cQoSTrafFilterUserAclRule_Type(Integer32):
    """Custom type hh3cQoSTrafFilterUserAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cQoSTrafFilterUserAclRule_Type.__name__ = "Integer32"
_Hh3cQoSTrafFilterUserAclRule_Object = MibTableColumn
hh3cQoSTrafFilterUserAclRule = _Hh3cQoSTrafFilterUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1, 5),
    _Hh3cQoSTrafFilterUserAclRule_Type()
)
hh3cQoSTrafFilterUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafFilterUserAclRule.setStatus("current")


class _Hh3cQoSTrafFilterIpAclNum_Type(Integer32):
    """Custom type hh3cQoSTrafFilterIpAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cQoSTrafFilterIpAclNum_Type.__name__ = "Integer32"
_Hh3cQoSTrafFilterIpAclNum_Object = MibTableColumn
hh3cQoSTrafFilterIpAclNum = _Hh3cQoSTrafFilterIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1, 6),
    _Hh3cQoSTrafFilterIpAclNum_Type()
)
hh3cQoSTrafFilterIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafFilterIpAclNum.setStatus("current")


class _Hh3cQoSTrafFilterIpAclRule_Type(Integer32):
    """Custom type hh3cQoSTrafFilterIpAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cQoSTrafFilterIpAclRule_Type.__name__ = "Integer32"
_Hh3cQoSTrafFilterIpAclRule_Object = MibTableColumn
hh3cQoSTrafFilterIpAclRule = _Hh3cQoSTrafFilterIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1, 7),
    _Hh3cQoSTrafFilterIpAclRule_Type()
)
hh3cQoSTrafFilterIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafFilterIpAclRule.setStatus("current")


class _Hh3cQoSTrafFilterLinkAclNum_Type(Integer32):
    """Custom type hh3cQoSTrafFilterLinkAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
    )


_Hh3cQoSTrafFilterLinkAclNum_Type.__name__ = "Integer32"
_Hh3cQoSTrafFilterLinkAclNum_Object = MibTableColumn
hh3cQoSTrafFilterLinkAclNum = _Hh3cQoSTrafFilterLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1, 8),
    _Hh3cQoSTrafFilterLinkAclNum_Type()
)
hh3cQoSTrafFilterLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafFilterLinkAclNum.setStatus("current")


class _Hh3cQoSTrafFilterLinkAclRule_Type(Integer32):
    """Custom type hh3cQoSTrafFilterLinkAclRule based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cQoSTrafFilterLinkAclRule_Type.__name__ = "Integer32"
_Hh3cQoSTrafFilterLinkAclRule_Object = MibTableColumn
hh3cQoSTrafFilterLinkAclRule = _Hh3cQoSTrafFilterLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1, 9),
    _Hh3cQoSTrafFilterLinkAclRule_Type()
)
hh3cQoSTrafFilterLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafFilterLinkAclRule.setStatus("current")
_Hh3cQoSTrafFilterRowStatus_Type = RowStatus
_Hh3cQoSTrafFilterRowStatus_Object = MibTableColumn
hh3cQoSTrafFilterRowStatus = _Hh3cQoSTrafFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 2, 3, 1, 10),
    _Hh3cQoSTrafFilterRowStatus_Type()
)
hh3cQoSTrafFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSTrafFilterRowStatus.setStatus("current")
_Hh3cQoSProfPortMapping_ObjectIdentity = ObjectIdentity
hh3cQoSProfPortMapping = _Hh3cQoSProfPortMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3)
)
_Hh3cQoSProfPortMappingTable_Object = MibTable
hh3cQoSProfPortMappingTable = _Hh3cQoSProfPortMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingTable.setStatus("current")
_Hh3cQoSProfPortMappingEntry_Object = MibTableRow
hh3cQoSProfPortMappingEntry = _Hh3cQoSProfPortMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 1, 1)
)
hh3cQoSProfPortMappingEntry.setIndexNames(
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSProfPortMappingIfIndex"),
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSProfPortMappingProfIndex"),
)
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingEntry.setStatus("current")


class _Hh3cQoSProfPortMappingIfIndex_Type(Integer32):
    """Custom type hh3cQoSProfPortMappingIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cQoSProfPortMappingIfIndex_Type.__name__ = "Integer32"
_Hh3cQoSProfPortMappingIfIndex_Object = MibTableColumn
hh3cQoSProfPortMappingIfIndex = _Hh3cQoSProfPortMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 1, 1, 1),
    _Hh3cQoSProfPortMappingIfIndex_Type()
)
hh3cQoSProfPortMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingIfIndex.setStatus("current")


class _Hh3cQoSProfPortMappingProfIndex_Type(Integer32):
    """Custom type hh3cQoSProfPortMappingProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQoSProfPortMappingProfIndex_Type.__name__ = "Integer32"
_Hh3cQoSProfPortMappingProfIndex_Object = MibTableColumn
hh3cQoSProfPortMappingProfIndex = _Hh3cQoSProfPortMappingProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 1, 1, 2),
    _Hh3cQoSProfPortMappingProfIndex_Type()
)
hh3cQoSProfPortMappingProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingProfIndex.setStatus("current")
_Hh3cQoSProfPortMappingRowStatus_Type = RowStatus
_Hh3cQoSProfPortMappingRowStatus_Object = MibTableColumn
hh3cQoSProfPortMappingRowStatus = _Hh3cQoSProfPortMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 1, 1, 3),
    _Hh3cQoSProfPortMappingRowStatus_Type()
)
hh3cQoSProfPortMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingRowStatus.setStatus("current")
_Hh3cQoSProfPortMappingModeTable_Object = MibTable
hh3cQoSProfPortMappingModeTable = _Hh3cQoSProfPortMappingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingModeTable.setStatus("current")
_Hh3cQoSProfPortMappingModeEntry_Object = MibTableRow
hh3cQoSProfPortMappingModeEntry = _Hh3cQoSProfPortMappingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 2, 1)
)
hh3cQoSProfPortMappingModeEntry.setIndexNames(
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSProfPortMappingModeIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingModeEntry.setStatus("current")


class _Hh3cQoSProfPortMappingModeIfIndex_Type(Integer32):
    """Custom type hh3cQoSProfPortMappingModeIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cQoSProfPortMappingModeIfIndex_Type.__name__ = "Integer32"
_Hh3cQoSProfPortMappingModeIfIndex_Object = MibTableColumn
hh3cQoSProfPortMappingModeIfIndex = _Hh3cQoSProfPortMappingModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 2, 1, 1),
    _Hh3cQoSProfPortMappingModeIfIndex_Type()
)
hh3cQoSProfPortMappingModeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingModeIfIndex.setStatus("current")


class _Hh3cQoSProfPortMappingMode_Type(Integer32):
    """Custom type hh3cQoSProfPortMappingMode based on Integer32"""
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


_Hh3cQoSProfPortMappingMode_Type.__name__ = "Integer32"
_Hh3cQoSProfPortMappingMode_Object = MibTableColumn
hh3cQoSProfPortMappingMode = _Hh3cQoSProfPortMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 2, 1, 2),
    _Hh3cQoSProfPortMappingMode_Type()
)
hh3cQoSProfPortMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingMode.setStatus("current")
_Hh3cQoSProfDynPortMappingTable_Object = MibTable
hh3cQoSProfDynPortMappingTable = _Hh3cQoSProfDynPortMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cQoSProfDynPortMappingTable.setStatus("current")
_Hh3cQoSProfDynPortMappingEntry_Object = MibTableRow
hh3cQoSProfDynPortMappingEntry = _Hh3cQoSProfDynPortMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 3, 1)
)
hh3cQoSProfDynPortMappingEntry.setIndexNames(
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSProfDynPortMappingIfIndex"),
    (0, "HH3C-QOS-PROFILE-MIB", "hh3cQoSProfDynPortMappingUserSrcMAC"),
)
if mibBuilder.loadTexts:
    hh3cQoSProfDynPortMappingEntry.setStatus("current")


class _Hh3cQoSProfDynPortMappingIfIndex_Type(Integer32):
    """Custom type hh3cQoSProfDynPortMappingIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cQoSProfDynPortMappingIfIndex_Type.__name__ = "Integer32"
_Hh3cQoSProfDynPortMappingIfIndex_Object = MibTableColumn
hh3cQoSProfDynPortMappingIfIndex = _Hh3cQoSProfDynPortMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 3, 1, 1),
    _Hh3cQoSProfDynPortMappingIfIndex_Type()
)
hh3cQoSProfDynPortMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSProfDynPortMappingIfIndex.setStatus("current")
_Hh3cQoSProfDynPortMappingUserSrcMAC_Type = MacAddress
_Hh3cQoSProfDynPortMappingUserSrcMAC_Object = MibTableColumn
hh3cQoSProfDynPortMappingUserSrcMAC = _Hh3cQoSProfDynPortMappingUserSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 3, 1, 2),
    _Hh3cQoSProfDynPortMappingUserSrcMAC_Type()
)
hh3cQoSProfDynPortMappingUserSrcMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSProfDynPortMappingUserSrcMAC.setStatus("current")


class _Hh3cQoSProfDynPortMappingUserName_Type(OctetString):
    """Custom type hh3cQoSProfDynPortMappingUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cQoSProfDynPortMappingUserName_Type.__name__ = "OctetString"
_Hh3cQoSProfDynPortMappingUserName_Object = MibTableColumn
hh3cQoSProfDynPortMappingUserName = _Hh3cQoSProfDynPortMappingUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 3, 1, 3),
    _Hh3cQoSProfDynPortMappingUserName_Type()
)
hh3cQoSProfDynPortMappingUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSProfDynPortMappingUserName.setStatus("current")
_Hh3cQoSProfDynPortMappingUserIPAddr_Type = IpAddress
_Hh3cQoSProfDynPortMappingUserIPAddr_Object = MibTableColumn
hh3cQoSProfDynPortMappingUserIPAddr = _Hh3cQoSProfDynPortMappingUserIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 3, 1, 4),
    _Hh3cQoSProfDynPortMappingUserIPAddr_Type()
)
hh3cQoSProfDynPortMappingUserIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSProfDynPortMappingUserIPAddr.setStatus("current")


class _Hh3cQoSProfDynPortMappingUserVLANID_Type(Integer32):
    """Custom type hh3cQoSProfDynPortMappingUserVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQoSProfDynPortMappingUserVLANID_Type.__name__ = "Integer32"
_Hh3cQoSProfDynPortMappingUserVLANID_Object = MibTableColumn
hh3cQoSProfDynPortMappingUserVLANID = _Hh3cQoSProfDynPortMappingUserVLANID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 3, 1, 5),
    _Hh3cQoSProfDynPortMappingUserVLANID_Type()
)
hh3cQoSProfDynPortMappingUserVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSProfDynPortMappingUserVLANID.setStatus("current")


class _Hh3cQoSProfDynPortMappingUserProfName_Type(OctetString):
    """Custom type hh3cQoSProfDynPortMappingUserProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cQoSProfDynPortMappingUserProfName_Type.__name__ = "OctetString"
_Hh3cQoSProfDynPortMappingUserProfName_Object = MibTableColumn
hh3cQoSProfDynPortMappingUserProfName = _Hh3cQoSProfDynPortMappingUserProfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 1, 3, 3, 1, 6),
    _Hh3cQoSProfDynPortMappingUserProfName_Type()
)
hh3cQoSProfDynPortMappingUserProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSProfDynPortMappingUserProfName.setStatus("current")
_Hh3cQoSProfPortMappingTraps_ObjectIdentity = ObjectIdentity
hh3cQoSProfPortMappingTraps = _Hh3cQoSProfPortMappingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 2)
)
_Hh3cQoSProfMibConformance_ObjectIdentity = ObjectIdentity
hh3cQoSProfMibConformance = _Hh3cQoSProfMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 3)
)
_Hh3cQoSProfMibCompliances_ObjectIdentity = ObjectIdentity
hh3cQoSProfMibCompliances = _Hh3cQoSProfMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 3, 1)
)
_Hh3cQoSProfMibGroups_ObjectIdentity = ObjectIdentity
hh3cQoSProfMibGroups = _Hh3cQoSProfMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 3, 2)
)

# Managed Objects groups

hh3cQoSProfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 3, 2, 1)
)
hh3cQoSProfGroup.setObjects(
      *(("HH3C-QOS-PROFILE-MIB", "hh3cQoSProfName"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSProfActionNumber"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSProfRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cQoSProfGroup.setStatus("current")

hh3cQoSActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 3, 2, 2)
)
hh3cQoSActionGroup.setObjects(
      *(("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtDirection"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtUserAclNum"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtUserAclRule"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtIpAclNum"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtIpAclRule"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtLinkAclNum"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtLinkAclRule"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtTargetRateMbps"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtTargetRateKbps"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtPeakRate"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtCIR"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtCBS"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtEBS"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtPIR"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtConformLocalPre"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtConformActionType"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtExceedActionType"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtExceedDscp"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtExceedCos"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtRowStatus"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtConformCos"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafLmtConformDscp"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioDirection"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioUserAclNum"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioUserAclRule"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioIpAclNum"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioIpAclRule"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioLinkAclNum"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioLinkAclRule"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioDscp"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioIpPre"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioIpPreFromCos"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioCos"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioCosFromIpPre"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioLocalPre"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioPolicedServiceType"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioPolicedServiceDscp"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioPolicedServiceExp"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioPolicedServiceCos"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioPolicedServiceLoaclPre"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioPolicedServiceDropPriority"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafPrioRowStatus"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafFilterDirection"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafFilterUserAclNum"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafFilterUserAclRule"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafFilterIpAclNum"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafFilterIpAclRule"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafFilterLinkAclNum"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafFilterLinkAclRule"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSTrafFilterRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cQoSActionGroup.setStatus("current")

hh3cQoSProfPortMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 3, 2, 3)
)
hh3cQoSProfPortMappingGroup.setObjects(
      *(("HH3C-QOS-PROFILE-MIB", "hh3cQoSProfPortMappingRowStatus"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSProfPortMappingMode"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSProfDynPortMappingUserName"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSProfDynPortMappingUserIPAddr"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSProfDynPortMappingUserVLANID"),
        ("HH3C-QOS-PROFILE-MIB", "hh3cQoSProfDynPortMappingUserProfName"))
)
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingGroup.setStatus("current")


# Notification objects

hh3cQoSProfPortMappingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingError.setStatus(
        "current"
    )


# Notifications groups

hh3cQoSProfPortMappingTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 3, 2, 4)
)
hh3cQoSProfPortMappingTrapsGroup.setObjects(
    ("HH3C-QOS-PROFILE-MIB", "hh3cQoSProfPortMappingError")
)
if mibBuilder.loadTexts:
    hh3cQoSProfPortMappingTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cQoSProfMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cQoSProfMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-QOS-PROFILE-MIB",
    **{"Hh3cQoSDirection": Hh3cQoSDirection,
       "hh3cQosProfile": hh3cQosProfile,
       "hh3cQoSProfObjects": hh3cQoSProfObjects,
       "hh3cQoSProf": hh3cQoSProf,
       "hh3cQoSProfTable": hh3cQoSProfTable,
       "hh3cQoSProfEntry": hh3cQoSProfEntry,
       "hh3cQoSProfIndex": hh3cQoSProfIndex,
       "hh3cQoSProfName": hh3cQoSProfName,
       "hh3cQoSProfActionNumber": hh3cQoSProfActionNumber,
       "hh3cQoSProfRowStatus": hh3cQoSProfRowStatus,
       "hh3cQoSAction": hh3cQoSAction,
       "hh3cQoSTrafficLimitTable": hh3cQoSTrafficLimitTable,
       "hh3cQoSTrafficLimitEntry": hh3cQoSTrafficLimitEntry,
       "hh3cQoSTrafLmtProfIndex": hh3cQoSTrafLmtProfIndex,
       "hh3cQoSTrafLmtActionIndex": hh3cQoSTrafLmtActionIndex,
       "hh3cQoSTrafLmtDirection": hh3cQoSTrafLmtDirection,
       "hh3cQoSTrafLmtUserAclNum": hh3cQoSTrafLmtUserAclNum,
       "hh3cQoSTrafLmtUserAclRule": hh3cQoSTrafLmtUserAclRule,
       "hh3cQoSTrafLmtIpAclNum": hh3cQoSTrafLmtIpAclNum,
       "hh3cQoSTrafLmtIpAclRule": hh3cQoSTrafLmtIpAclRule,
       "hh3cQoSTrafLmtLinkAclNum": hh3cQoSTrafLmtLinkAclNum,
       "hh3cQoSTrafLmtLinkAclRule": hh3cQoSTrafLmtLinkAclRule,
       "hh3cQoSTrafLmtTargetRateMbps": hh3cQoSTrafLmtTargetRateMbps,
       "hh3cQoSTrafLmtTargetRateKbps": hh3cQoSTrafLmtTargetRateKbps,
       "hh3cQoSTrafLmtPeakRate": hh3cQoSTrafLmtPeakRate,
       "hh3cQoSTrafLmtCIR": hh3cQoSTrafLmtCIR,
       "hh3cQoSTrafLmtCBS": hh3cQoSTrafLmtCBS,
       "hh3cQoSTrafLmtEBS": hh3cQoSTrafLmtEBS,
       "hh3cQoSTrafLmtPIR": hh3cQoSTrafLmtPIR,
       "hh3cQoSTrafLmtConformLocalPre": hh3cQoSTrafLmtConformLocalPre,
       "hh3cQoSTrafLmtConformActionType": hh3cQoSTrafLmtConformActionType,
       "hh3cQoSTrafLmtExceedActionType": hh3cQoSTrafLmtExceedActionType,
       "hh3cQoSTrafLmtExceedDscp": hh3cQoSTrafLmtExceedDscp,
       "hh3cQoSTrafLmtExceedCos": hh3cQoSTrafLmtExceedCos,
       "hh3cQoSTrafLmtRowStatus": hh3cQoSTrafLmtRowStatus,
       "hh3cQoSTrafLmtConformCos": hh3cQoSTrafLmtConformCos,
       "hh3cQoSTrafLmtConformDscp": hh3cQoSTrafLmtConformDscp,
       "hh3cQoSTrafficPriorityTable": hh3cQoSTrafficPriorityTable,
       "hh3cQoSTrafficPriorityEntry": hh3cQoSTrafficPriorityEntry,
       "hh3cQoSTrafPrioProfIndex": hh3cQoSTrafPrioProfIndex,
       "hh3cQoSTrafPrioActionIndex": hh3cQoSTrafPrioActionIndex,
       "hh3cQoSTrafPrioDirection": hh3cQoSTrafPrioDirection,
       "hh3cQoSTrafPrioUserAclNum": hh3cQoSTrafPrioUserAclNum,
       "hh3cQoSTrafPrioUserAclRule": hh3cQoSTrafPrioUserAclRule,
       "hh3cQoSTrafPrioIpAclNum": hh3cQoSTrafPrioIpAclNum,
       "hh3cQoSTrafPrioIpAclRule": hh3cQoSTrafPrioIpAclRule,
       "hh3cQoSTrafPrioLinkAclNum": hh3cQoSTrafPrioLinkAclNum,
       "hh3cQoSTrafPrioLinkAclRule": hh3cQoSTrafPrioLinkAclRule,
       "hh3cQoSTrafPrioDscp": hh3cQoSTrafPrioDscp,
       "hh3cQoSTrafPrioIpPre": hh3cQoSTrafPrioIpPre,
       "hh3cQoSTrafPrioIpPreFromCos": hh3cQoSTrafPrioIpPreFromCos,
       "hh3cQoSTrafPrioCos": hh3cQoSTrafPrioCos,
       "hh3cQoSTrafPrioCosFromIpPre": hh3cQoSTrafPrioCosFromIpPre,
       "hh3cQoSTrafPrioLocalPre": hh3cQoSTrafPrioLocalPre,
       "hh3cQoSTrafPrioPolicedServiceType": hh3cQoSTrafPrioPolicedServiceType,
       "hh3cQoSTrafPrioPolicedServiceDscp": hh3cQoSTrafPrioPolicedServiceDscp,
       "hh3cQoSTrafPrioPolicedServiceExp": hh3cQoSTrafPrioPolicedServiceExp,
       "hh3cQoSTrafPrioPolicedServiceCos": hh3cQoSTrafPrioPolicedServiceCos,
       "hh3cQoSTrafPrioPolicedServiceLoaclPre": hh3cQoSTrafPrioPolicedServiceLoaclPre,
       "hh3cQoSTrafPrioPolicedServiceDropPriority": hh3cQoSTrafPrioPolicedServiceDropPriority,
       "hh3cQoSTrafPrioRowStatus": hh3cQoSTrafPrioRowStatus,
       "hh3cQoSTrafficFilterTable": hh3cQoSTrafficFilterTable,
       "hh3cQoSTrafficFilterEntry": hh3cQoSTrafficFilterEntry,
       "hh3cQoSTrafFilterProfIndex": hh3cQoSTrafFilterProfIndex,
       "hh3cQoSTrafFilterActionIndex": hh3cQoSTrafFilterActionIndex,
       "hh3cQoSTrafFilterDirection": hh3cQoSTrafFilterDirection,
       "hh3cQoSTrafFilterUserAclNum": hh3cQoSTrafFilterUserAclNum,
       "hh3cQoSTrafFilterUserAclRule": hh3cQoSTrafFilterUserAclRule,
       "hh3cQoSTrafFilterIpAclNum": hh3cQoSTrafFilterIpAclNum,
       "hh3cQoSTrafFilterIpAclRule": hh3cQoSTrafFilterIpAclRule,
       "hh3cQoSTrafFilterLinkAclNum": hh3cQoSTrafFilterLinkAclNum,
       "hh3cQoSTrafFilterLinkAclRule": hh3cQoSTrafFilterLinkAclRule,
       "hh3cQoSTrafFilterRowStatus": hh3cQoSTrafFilterRowStatus,
       "hh3cQoSProfPortMapping": hh3cQoSProfPortMapping,
       "hh3cQoSProfPortMappingTable": hh3cQoSProfPortMappingTable,
       "hh3cQoSProfPortMappingEntry": hh3cQoSProfPortMappingEntry,
       "hh3cQoSProfPortMappingIfIndex": hh3cQoSProfPortMappingIfIndex,
       "hh3cQoSProfPortMappingProfIndex": hh3cQoSProfPortMappingProfIndex,
       "hh3cQoSProfPortMappingRowStatus": hh3cQoSProfPortMappingRowStatus,
       "hh3cQoSProfPortMappingModeTable": hh3cQoSProfPortMappingModeTable,
       "hh3cQoSProfPortMappingModeEntry": hh3cQoSProfPortMappingModeEntry,
       "hh3cQoSProfPortMappingModeIfIndex": hh3cQoSProfPortMappingModeIfIndex,
       "hh3cQoSProfPortMappingMode": hh3cQoSProfPortMappingMode,
       "hh3cQoSProfDynPortMappingTable": hh3cQoSProfDynPortMappingTable,
       "hh3cQoSProfDynPortMappingEntry": hh3cQoSProfDynPortMappingEntry,
       "hh3cQoSProfDynPortMappingIfIndex": hh3cQoSProfDynPortMappingIfIndex,
       "hh3cQoSProfDynPortMappingUserSrcMAC": hh3cQoSProfDynPortMappingUserSrcMAC,
       "hh3cQoSProfDynPortMappingUserName": hh3cQoSProfDynPortMappingUserName,
       "hh3cQoSProfDynPortMappingUserIPAddr": hh3cQoSProfDynPortMappingUserIPAddr,
       "hh3cQoSProfDynPortMappingUserVLANID": hh3cQoSProfDynPortMappingUserVLANID,
       "hh3cQoSProfDynPortMappingUserProfName": hh3cQoSProfDynPortMappingUserProfName,
       "hh3cQoSProfPortMappingTraps": hh3cQoSProfPortMappingTraps,
       "hh3cQoSProfPortMappingError": hh3cQoSProfPortMappingError,
       "hh3cQoSProfMibConformance": hh3cQoSProfMibConformance,
       "hh3cQoSProfMibCompliances": hh3cQoSProfMibCompliances,
       "hh3cQoSProfMibCompliance": hh3cQoSProfMibCompliance,
       "hh3cQoSProfMibGroups": hh3cQoSProfMibGroups,
       "hh3cQoSProfGroup": hh3cQoSProfGroup,
       "hh3cQoSActionGroup": hh3cQoSActionGroup,
       "hh3cQoSProfPortMappingGroup": hh3cQoSProfPortMappingGroup,
       "hh3cQoSProfPortMappingTrapsGroup": hh3cQoSProfPortMappingTrapsGroup}
)
