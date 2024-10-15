# SNMP MIB module (HUAWEI-IPFPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-IPFPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:05 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hwIpfpmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316)
)
hwIpfpmMib.setRevisions(
        ("2015-10-13 17:00",
         "2015-08-14 20:59",
         "2015-05-07 15:55",
         "2015-07-09 16:58",
         "2015-05-06 12:55",
         "2015-05-05 15:55",
         "2015-04-16 15:27",
         "2015-02-06 11:43",
         "2014-12-29 16:26",
         "2014-06-26 10:00",
         "2014-02-12 10:00",
         "2013-12-17 10:00",
         "2013-10-25 20:00",
         "2013-09-25 20:00",
         "2013-09-23 20:00",
         "2013-08-18 20:38",
         "2013-08-14 20:38",
         "2013-08-05 15:04",
         "2013-07-04 16:12",
         "2013-06-22 14:50",
         "2013-06-04 14:03",
         "2013-04-27 17:30",
         "2013-03-27 10:11",
         "2013-03-26 10:11",
         "2013-03-13 11:50",
         "2013-02-18 11:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWEnabledStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class HWIpfpmStatErrInfo(Integer32, TextualConvention):
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("asynClock", 5),
          ("errDelayVariationBackward", 18),
          ("errDelayVariationBidirection", 19),
          ("errDelayVariationForward", 17),
          ("errFlowDataBackward", 13),
          ("errFlowDataBidirection", 14),
          ("errFlowDataForward", 12),
          ("errMultiSourceSwitch", 20),
          ("incompleteDataBackward", 7),
          ("incompleteDataBidirection", 8),
          ("incompleteDataForward", 6),
          ("inconsistInterval", 4),
          ("initialIntervalBackward", 2),
          ("initialIntervalBidirection", 3),
          ("initialIntervalForward", 1),
          ("multiDataOneDelay", 15),
          ("multiDataTwoDelay", 16),
          ("noErr", 0),
          ("noFlowDataBackward", 10),
          ("noFlowDataBidirection", 11),
          ("noFlowDataForward", 9),
          ("unknownErr", 21))
    )



class HWIpfpmMeasureFlag(Integer32, TextualConvention):
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
        *(("flagsBit0", 1),
          ("tosBit3", 2),
          ("tosBit4", 3),
          ("tosBit5", 4),
          ("tosBit6", 5),
          ("tosBit7", 6))
    )



class HWIpfpmFlowType(Integer32, TextualConvention):
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
        *(("backward", 2),
          ("bidirectional", 3),
          ("forward", 1),
          ("forwardandbackward", 4),
          ("null", 0))
    )



class HWIpfpmMcpFlowType(Integer32, TextualConvention):
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
        *(("backward", 2),
          ("bidirectional", 3),
          ("forward", 1),
          ("none", 0))
    )



class HWIpfpmFlowTlpDirec(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )



class HWIpfpmTlpRole(Integer32, TextualConvention):
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
        *(("in-point", 1),
          ("mid-point", 3),
          ("out-point", 2))
    )



class HWIpfpmDelayTlpRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 1),
          ("section", 2))
    )



class HWIpfpmLossTlpRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 1),
          ("section", 2))
    )



class HWIpfpmMcpTlpRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-group", 1),
          ("out-group", 2))
    )



class HWIpfpmAuthType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("hmac-sha256", 1)
    )



class HWIpfpmDelayMeasType(Integer32, TextualConvention):
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
        *(("null", 0),
          ("oneway", 1),
          ("twoway", 2))
    )



class HWIpfpmMeasTimeRangeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              15,
              30)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("timerange10m", 10),
          ("timerange15m", 15),
          ("timerange30m", 30),
          ("timerange5m", 5))
    )



class HWIpfpmInstIntervalType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              60,
              600)
        )
    )
    namedValues = NamedValues(
        *(("interval10s", 10),
          ("interval1s", 1),
          ("interval600s", 600),
          ("interval60s", 60))
    )



class HWIpfpmInstType(Integer32, TextualConvention):
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
        *(("multicastrecv", 2),
          ("multicastsrc", 1),
          ("unicast", 0))
    )



class HWIpfpmMMSType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )



class HWIpfpmVpnType(Integer32, TextualConvention):
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
        *(("manage-vpn", 1),
          ("none", 0),
          ("vpn-instance", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwIpfpmMcpObjects_ObjectIdentity = ObjectIdentity
hwIpfpmMcpObjects = _HwIpfpmMcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1)
)
_HwIpfpmMcpConfiguration_ObjectIdentity = ObjectIdentity
hwIpfpmMcpConfiguration = _HwIpfpmMcpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1)
)
_HwIpfpmMcpGlobalTable_ObjectIdentity = ObjectIdentity
hwIpfpmMcpGlobalTable = _HwIpfpmMcpGlobalTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 1)
)


class _HwIpfpmMcpEnable_Type(HWEnabledStatus):
    """Custom type hwIpfpmMcpEnable based on HWEnabledStatus"""


_HwIpfpmMcpEnable_Object = MibScalar
hwIpfpmMcpEnable = _HwIpfpmMcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 1, 1),
    _HwIpfpmMcpEnable_Type()
)
hwIpfpmMcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmMcpEnable.setStatus("current")
_HwIpfpmMcpId_Type = IpAddress
_HwIpfpmMcpId_Object = MibScalar
hwIpfpmMcpId = _HwIpfpmMcpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 1, 2),
    _HwIpfpmMcpId_Type()
)
hwIpfpmMcpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmMcpId.setStatus("current")


class _HwIpfpmMcpUdpPort_Type(Integer32):
    """Custom type hwIpfpmMcpUdpPort based on Integer32"""
    defaultValue = 65030

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HwIpfpmMcpUdpPort_Type.__name__ = "Integer32"
_HwIpfpmMcpUdpPort_Object = MibScalar
hwIpfpmMcpUdpPort = _HwIpfpmMcpUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 1, 3),
    _HwIpfpmMcpUdpPort_Type()
)
hwIpfpmMcpUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmMcpUdpPort.setStatus("current")
_HwIpfpmMcpAuthTable_Object = MibTable
hwIpfpmMcpAuthTable = _HwIpfpmMcpAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwIpfpmMcpAuthTable.setStatus("current")
_HwIpfpmMcpAuthEntry_Object = MibTableRow
hwIpfpmMcpAuthEntry = _HwIpfpmMcpAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 4, 1)
)
hwIpfpmMcpAuthEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpAuthKeyId"),
)
if mibBuilder.loadTexts:
    hwIpfpmMcpAuthEntry.setStatus("current")


class _HwIpfpmMcpAuthKeyId_Type(Integer32):
    """Custom type hwIpfpmMcpAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwIpfpmMcpAuthKeyId_Type.__name__ = "Integer32"
_HwIpfpmMcpAuthKeyId_Object = MibTableColumn
hwIpfpmMcpAuthKeyId = _HwIpfpmMcpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 4, 1, 1),
    _HwIpfpmMcpAuthKeyId_Type()
)
hwIpfpmMcpAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmMcpAuthKeyId.setStatus("current")
_HwIpfpmMcpAuthType_Type = HWIpfpmAuthType
_HwIpfpmMcpAuthType_Object = MibTableColumn
hwIpfpmMcpAuthType = _HwIpfpmMcpAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 4, 1, 2),
    _HwIpfpmMcpAuthType_Type()
)
hwIpfpmMcpAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpAuthType.setStatus("current")


class _HwIpfpmMcpAuthKey_Type(OctetString):
    """Custom type hwIpfpmMcpAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwIpfpmMcpAuthKey_Type.__name__ = "OctetString"
_HwIpfpmMcpAuthKey_Object = MibTableColumn
hwIpfpmMcpAuthKey = _HwIpfpmMcpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 4, 1, 3),
    _HwIpfpmMcpAuthKey_Type()
)
hwIpfpmMcpAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpAuthKey.setStatus("current")
_HwIpfpmMcpAuthRowStatus_Type = RowStatus
_HwIpfpmMcpAuthRowStatus_Object = MibTableColumn
hwIpfpmMcpAuthRowStatus = _HwIpfpmMcpAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 4, 1, 4),
    _HwIpfpmMcpAuthRowStatus_Type()
)
hwIpfpmMcpAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpAuthRowStatus.setStatus("current")
_HwIpfpmMcpInstTable_Object = MibTable
hwIpfpmMcpInstTable = _HwIpfpmMcpInstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwIpfpmMcpInstTable.setStatus("current")
_HwIpfpmMcpInstEntry_Object = MibTableRow
hwIpfpmMcpInstEntry = _HwIpfpmMcpInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1)
)
hwIpfpmMcpInstEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstId"),
)
if mibBuilder.loadTexts:
    hwIpfpmMcpInstEntry.setStatus("current")


class _HwIpfpmMcpInstId_Type(Integer32):
    """Custom type hwIpfpmMcpInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8355838),
        ValueRangeConstraint(16711681, 16777214),
    )


_HwIpfpmMcpInstId_Type.__name__ = "Integer32"
_HwIpfpmMcpInstId_Object = MibTableColumn
hwIpfpmMcpInstId = _HwIpfpmMcpInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 1),
    _HwIpfpmMcpInstId_Type()
)
hwIpfpmMcpInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmMcpInstId.setStatus("current")


class _HwIpfpmMcpInstDesc_Type(OctetString):
    """Custom type hwIpfpmMcpInstDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwIpfpmMcpInstDesc_Type.__name__ = "OctetString"
_HwIpfpmMcpInstDesc_Object = MibTableColumn
hwIpfpmMcpInstDesc = _HwIpfpmMcpInstDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 2),
    _HwIpfpmMcpInstDesc_Type()
)
hwIpfpmMcpInstDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpInstDesc.setStatus("current")


class _HwIpfpmMcpLossRatioUpThres_Type(Integer32):
    """Custom type hwIpfpmMcpLossRatioUpThres based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_HwIpfpmMcpLossRatioUpThres_Type.__name__ = "Integer32"
_HwIpfpmMcpLossRatioUpThres_Object = MibTableColumn
hwIpfpmMcpLossRatioUpThres = _HwIpfpmMcpLossRatioUpThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 3),
    _HwIpfpmMcpLossRatioUpThres_Type()
)
hwIpfpmMcpLossRatioUpThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpLossRatioUpThres.setStatus("current")


class _HwIpfpmMcpLossRatioLowThres_Type(Integer32):
    """Custom type hwIpfpmMcpLossRatioLowThres based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_HwIpfpmMcpLossRatioLowThres_Type.__name__ = "Integer32"
_HwIpfpmMcpLossRatioLowThres_Object = MibTableColumn
hwIpfpmMcpLossRatioLowThres = _HwIpfpmMcpLossRatioLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 4),
    _HwIpfpmMcpLossRatioLowThres_Type()
)
hwIpfpmMcpLossRatioLowThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpLossRatioLowThres.setStatus("current")


class _HwIpfpmMcpOneDelayUpThres_Type(Integer32):
    """Custom type hwIpfpmMcpOneDelayUpThres based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwIpfpmMcpOneDelayUpThres_Type.__name__ = "Integer32"
_HwIpfpmMcpOneDelayUpThres_Object = MibTableColumn
hwIpfpmMcpOneDelayUpThres = _HwIpfpmMcpOneDelayUpThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 5),
    _HwIpfpmMcpOneDelayUpThres_Type()
)
hwIpfpmMcpOneDelayUpThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpOneDelayUpThres.setStatus("current")


class _HwIpfpmMcpOneDelayLowThres_Type(Integer32):
    """Custom type hwIpfpmMcpOneDelayLowThres based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwIpfpmMcpOneDelayLowThres_Type.__name__ = "Integer32"
_HwIpfpmMcpOneDelayLowThres_Object = MibTableColumn
hwIpfpmMcpOneDelayLowThres = _HwIpfpmMcpOneDelayLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 6),
    _HwIpfpmMcpOneDelayLowThres_Type()
)
hwIpfpmMcpOneDelayLowThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpOneDelayLowThres.setStatus("current")


class _HwIpfpmMcpTwoDelayUpThres_Type(Integer32):
    """Custom type hwIpfpmMcpTwoDelayUpThres based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwIpfpmMcpTwoDelayUpThres_Type.__name__ = "Integer32"
_HwIpfpmMcpTwoDelayUpThres_Object = MibTableColumn
hwIpfpmMcpTwoDelayUpThres = _HwIpfpmMcpTwoDelayUpThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 7),
    _HwIpfpmMcpTwoDelayUpThres_Type()
)
hwIpfpmMcpTwoDelayUpThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpTwoDelayUpThres.setStatus("current")


class _HwIpfpmMcpTwoDelayLowThres_Type(Integer32):
    """Custom type hwIpfpmMcpTwoDelayLowThres based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwIpfpmMcpTwoDelayLowThres_Type.__name__ = "Integer32"
_HwIpfpmMcpTwoDelayLowThres_Object = MibTableColumn
hwIpfpmMcpTwoDelayLowThres = _HwIpfpmMcpTwoDelayLowThres_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 8),
    _HwIpfpmMcpTwoDelayLowThres_Type()
)
hwIpfpmMcpTwoDelayLowThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpTwoDelayLowThres.setStatus("current")


class _HwIpfpmMcpMeasureEnable_Type(HWEnabledStatus):
    """Custom type hwIpfpmMcpMeasureEnable based on HWEnabledStatus"""


_HwIpfpmMcpMeasureEnable_Object = MibTableColumn
hwIpfpmMcpMeasureEnable = _HwIpfpmMcpMeasureEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 9),
    _HwIpfpmMcpMeasureEnable_Type()
)
hwIpfpmMcpMeasureEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpMeasureEnable.setStatus("current")
_HwIpfpmMcpInstRowStatus_Type = RowStatus
_HwIpfpmMcpInstRowStatus_Object = MibTableColumn
hwIpfpmMcpInstRowStatus = _HwIpfpmMcpInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 10),
    _HwIpfpmMcpInstRowStatus_Type()
)
hwIpfpmMcpInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpInstRowStatus.setStatus("current")
_HwIpfpmMcpInstType_Type = HWIpfpmInstType
_HwIpfpmMcpInstType_Object = MibTableColumn
hwIpfpmMcpInstType = _HwIpfpmMcpInstType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 11),
    _HwIpfpmMcpInstType_Type()
)
hwIpfpmMcpInstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpInstType.setStatus("current")


class _HwIpfpmMcpSourceInstId_Type(Integer32):
    """Custom type hwIpfpmMcpSourceInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16711681, 16777214),
    )


_HwIpfpmMcpSourceInstId_Type.__name__ = "Integer32"
_HwIpfpmMcpSourceInstId_Object = MibTableColumn
hwIpfpmMcpSourceInstId = _HwIpfpmMcpSourceInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 5, 1, 12),
    _HwIpfpmMcpSourceInstId_Type()
)
hwIpfpmMcpSourceInstId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpSourceInstId.setStatus("current")
_HwIpfpmMcpDcpTable_Object = MibTable
hwIpfpmMcpDcpTable = _HwIpfpmMcpDcpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwIpfpmMcpDcpTable.setStatus("current")
_HwIpfpmMcpDcpEntry_Object = MibTableRow
hwIpfpmMcpDcpEntry = _HwIpfpmMcpDcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 6, 1)
)
hwIpfpmMcpDcpEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpDcpId"),
)
if mibBuilder.loadTexts:
    hwIpfpmMcpDcpEntry.setStatus("current")
_HwIpfpmMcpDcpId_Type = IpAddress
_HwIpfpmMcpDcpId_Object = MibTableColumn
hwIpfpmMcpDcpId = _HwIpfpmMcpDcpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 6, 1, 1),
    _HwIpfpmMcpDcpId_Type()
)
hwIpfpmMcpDcpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmMcpDcpId.setStatus("current")
_HwIpfpmMcpDcpRowStatus_Type = RowStatus
_HwIpfpmMcpDcpRowStatus_Object = MibTableColumn
hwIpfpmMcpDcpRowStatus = _HwIpfpmMcpDcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 6, 1, 2),
    _HwIpfpmMcpDcpRowStatus_Type()
)
hwIpfpmMcpDcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpDcpRowStatus.setStatus("current")
_HwIpfpmMcpAchTable_Object = MibTable
hwIpfpmMcpAchTable = _HwIpfpmMcpAchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwIpfpmMcpAchTable.setStatus("current")
_HwIpfpmMcpAchEntry_Object = MibTableRow
hwIpfpmMcpAchEntry = _HwIpfpmMcpAchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 7, 1)
)
hwIpfpmMcpAchEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpAchId"),
)
if mibBuilder.loadTexts:
    hwIpfpmMcpAchEntry.setStatus("current")


class _HwIpfpmMcpAchId_Type(Integer32):
    """Custom type hwIpfpmMcpAchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwIpfpmMcpAchId_Type.__name__ = "Integer32"
_HwIpfpmMcpAchId_Object = MibTableColumn
hwIpfpmMcpAchId = _HwIpfpmMcpAchId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 7, 1, 1),
    _HwIpfpmMcpAchId_Type()
)
hwIpfpmMcpAchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmMcpAchId.setStatus("current")


class _HwIpfpmMcpFlowType_Type(HWIpfpmMcpFlowType):
    """Custom type hwIpfpmMcpFlowType based on HWIpfpmMcpFlowType"""


_HwIpfpmMcpFlowType_Object = MibTableColumn
hwIpfpmMcpFlowType = _HwIpfpmMcpFlowType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 7, 1, 2),
    _HwIpfpmMcpFlowType_Type()
)
hwIpfpmMcpFlowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpFlowType.setStatus("current")
_HwIpfpmMcpAchRowStatus_Type = RowStatus
_HwIpfpmMcpAchRowStatus_Object = MibTableColumn
hwIpfpmMcpAchRowStatus = _HwIpfpmMcpAchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 7, 1, 3),
    _HwIpfpmMcpAchRowStatus_Type()
)
hwIpfpmMcpAchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpAchRowStatus.setStatus("current")
_HwIpfpmMcpTlpTable_Object = MibTable
hwIpfpmMcpTlpTable = _HwIpfpmMcpTlpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hwIpfpmMcpTlpTable.setStatus("current")
_HwIpfpmMcpTlpEntry_Object = MibTableRow
hwIpfpmMcpTlpEntry = _HwIpfpmMcpTlpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 8, 1)
)
hwIpfpmMcpTlpEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpAchId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpTlpRole"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpTlpDcpId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpTlpId"),
)
if mibBuilder.loadTexts:
    hwIpfpmMcpTlpEntry.setStatus("current")
_HwIpfpmMcpTlpRole_Type = HWIpfpmMcpTlpRole
_HwIpfpmMcpTlpRole_Object = MibTableColumn
hwIpfpmMcpTlpRole = _HwIpfpmMcpTlpRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 8, 1, 1),
    _HwIpfpmMcpTlpRole_Type()
)
hwIpfpmMcpTlpRole.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmMcpTlpRole.setStatus("current")
_HwIpfpmMcpTlpDcpId_Type = IpAddress
_HwIpfpmMcpTlpDcpId_Object = MibTableColumn
hwIpfpmMcpTlpDcpId = _HwIpfpmMcpTlpDcpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 8, 1, 2),
    _HwIpfpmMcpTlpDcpId_Type()
)
hwIpfpmMcpTlpDcpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmMcpTlpDcpId.setStatus("current")


class _HwIpfpmMcpTlpId_Type(Integer32):
    """Custom type hwIpfpmMcpTlpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HwIpfpmMcpTlpId_Type.__name__ = "Integer32"
_HwIpfpmMcpTlpId_Object = MibTableColumn
hwIpfpmMcpTlpId = _HwIpfpmMcpTlpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 8, 1, 3),
    _HwIpfpmMcpTlpId_Type()
)
hwIpfpmMcpTlpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmMcpTlpId.setStatus("current")
_HwIpfpmMcpTlpRowStatus_Type = RowStatus
_HwIpfpmMcpTlpRowStatus_Object = MibTableColumn
hwIpfpmMcpTlpRowStatus = _HwIpfpmMcpTlpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 8, 1, 4),
    _HwIpfpmMcpTlpRowStatus_Type()
)
hwIpfpmMcpTlpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmMcpTlpRowStatus.setStatus("current")
_HwIpfpmMcpSrcInstReferQueryTable_Object = MibTable
hwIpfpmMcpSrcInstReferQueryTable = _HwIpfpmMcpSrcInstReferQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hwIpfpmMcpSrcInstReferQueryTable.setStatus("current")
_HwIpfpmMcpSrcInstReferQueryEntry_Object = MibTableRow
hwIpfpmMcpSrcInstReferQueryEntry = _HwIpfpmMcpSrcInstReferQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 9, 1)
)
hwIpfpmMcpSrcInstReferQueryEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstId"),
)
if mibBuilder.loadTexts:
    hwIpfpmMcpSrcInstReferQueryEntry.setStatus("current")
_HwIpfpmMcpSrcInstReferCnt_Type = Integer32
_HwIpfpmMcpSrcInstReferCnt_Object = MibTableColumn
hwIpfpmMcpSrcInstReferCnt = _HwIpfpmMcpSrcInstReferCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 1, 9, 1, 1),
    _HwIpfpmMcpSrcInstReferCnt_Type()
)
hwIpfpmMcpSrcInstReferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpSrcInstReferCnt.setStatus("current")
_HwIpfpmMcpStatistics_ObjectIdentity = ObjectIdentity
hwIpfpmMcpStatistics = _HwIpfpmMcpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2)
)
_HwIpfpmMcpStatisticsTable_ObjectIdentity = ObjectIdentity
hwIpfpmMcpStatisticsTable = _HwIpfpmMcpStatisticsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 1)
)
_HwIpfpmMcpInstSpec_Type = Integer32
_HwIpfpmMcpInstSpec_Object = MibScalar
hwIpfpmMcpInstSpec = _HwIpfpmMcpInstSpec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 1, 1),
    _HwIpfpmMcpInstSpec_Type()
)
hwIpfpmMcpInstSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpInstSpec.setStatus("current")
_HwIpfpmMcpInstCurNum_Type = Integer32
_HwIpfpmMcpInstCurNum_Object = MibScalar
hwIpfpmMcpInstCurNum = _HwIpfpmMcpInstCurNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 1, 2),
    _HwIpfpmMcpInstCurNum_Type()
)
hwIpfpmMcpInstCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpInstCurNum.setStatus("current")
_HwIpfpmMcpInstAchIndexTable_Object = MibTable
hwIpfpmMcpInstAchIndexTable = _HwIpfpmMcpInstAchIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwIpfpmMcpInstAchIndexTable.setStatus("current")
_HwIpfpmMcpInstAchIndexEntry_Object = MibTableRow
hwIpfpmMcpInstAchIndexEntry = _HwIpfpmMcpInstAchIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 3, 1)
)
hwIpfpmMcpInstAchIndexEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpAchId"),
)
if mibBuilder.loadTexts:
    hwIpfpmMcpInstAchIndexEntry.setStatus("current")
_HwIpfpmMcpSeqNo_Type = Counter64
_HwIpfpmMcpSeqNo_Object = MibTableColumn
hwIpfpmMcpSeqNo = _HwIpfpmMcpSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 3, 1, 1),
    _HwIpfpmMcpSeqNo_Type()
)
hwIpfpmMcpSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpSeqNo.setStatus("current")
_HwIpfpmMcpLossStatsTable_Object = MibTable
hwIpfpmMcpLossStatsTable = _HwIpfpmMcpLossStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwIpfpmMcpLossStatsTable.setStatus("current")
_HwIpfpmMcpLossStatsEntry_Object = MibTableRow
hwIpfpmMcpLossStatsEntry = _HwIpfpmMcpLossStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1)
)
hwIpfpmMcpLossStatsEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpAchId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpSeqNoHigh"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpSeqNoLow"),
)
if mibBuilder.loadTexts:
    hwIpfpmMcpLossStatsEntry.setStatus("current")
_HwIpfpmMcpSeqNoHigh_Type = Unsigned32
_HwIpfpmMcpSeqNoHigh_Object = MibTableColumn
hwIpfpmMcpSeqNoHigh = _HwIpfpmMcpSeqNoHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 1),
    _HwIpfpmMcpSeqNoHigh_Type()
)
hwIpfpmMcpSeqNoHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmMcpSeqNoHigh.setStatus("current")
_HwIpfpmMcpSeqNoLow_Type = Unsigned32
_HwIpfpmMcpSeqNoLow_Object = MibTableColumn
hwIpfpmMcpSeqNoLow = _HwIpfpmMcpSeqNoLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 2),
    _HwIpfpmMcpSeqNoLow_Type()
)
hwIpfpmMcpSeqNoLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmMcpSeqNoLow.setStatus("current")
_HwIpfpmMcpLossErrInfo_Type = HWIpfpmStatErrInfo
_HwIpfpmMcpLossErrInfo_Object = MibTableColumn
hwIpfpmMcpLossErrInfo = _HwIpfpmMcpLossErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 3),
    _HwIpfpmMcpLossErrInfo_Type()
)
hwIpfpmMcpLossErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpLossErrInfo.setStatus("current")
_HwIpfpmMcpForwardLossPkts_Type = Counter64
_HwIpfpmMcpForwardLossPkts_Object = MibTableColumn
hwIpfpmMcpForwardLossPkts = _HwIpfpmMcpForwardLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 4),
    _HwIpfpmMcpForwardLossPkts_Type()
)
hwIpfpmMcpForwardLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardLossPkts.setStatus("current")
_HwIpfpmMcpForwardLossPktsSign_Type = Integer32
_HwIpfpmMcpForwardLossPktsSign_Object = MibTableColumn
hwIpfpmMcpForwardLossPktsSign = _HwIpfpmMcpForwardLossPktsSign_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 5),
    _HwIpfpmMcpForwardLossPktsSign_Type()
)
hwIpfpmMcpForwardLossPktsSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardLossPktsSign.setStatus("current")
_HwIpfpmMcpForwardLossBytes_Type = Counter64
_HwIpfpmMcpForwardLossBytes_Object = MibTableColumn
hwIpfpmMcpForwardLossBytes = _HwIpfpmMcpForwardLossBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 6),
    _HwIpfpmMcpForwardLossBytes_Type()
)
hwIpfpmMcpForwardLossBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardLossBytes.setStatus("current")
_HwIpfpmMcpForwardLossBytesSign_Type = Integer32
_HwIpfpmMcpForwardLossBytesSign_Object = MibTableColumn
hwIpfpmMcpForwardLossBytesSign = _HwIpfpmMcpForwardLossBytesSign_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 7),
    _HwIpfpmMcpForwardLossBytesSign_Type()
)
hwIpfpmMcpForwardLossBytesSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardLossBytesSign.setStatus("current")
_HwIpfpmMcpForwardPkts_Type = Counter64
_HwIpfpmMcpForwardPkts_Object = MibTableColumn
hwIpfpmMcpForwardPkts = _HwIpfpmMcpForwardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 8),
    _HwIpfpmMcpForwardPkts_Type()
)
hwIpfpmMcpForwardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardPkts.setStatus("current")
_HwIpfpmMcpForwardBytes_Type = Counter64
_HwIpfpmMcpForwardBytes_Object = MibTableColumn
hwIpfpmMcpForwardBytes = _HwIpfpmMcpForwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 9),
    _HwIpfpmMcpForwardBytes_Type()
)
hwIpfpmMcpForwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardBytes.setStatus("current")
_HwIpfpmMcpForwardLossRatio_Type = Integer32
_HwIpfpmMcpForwardLossRatio_Object = MibTableColumn
hwIpfpmMcpForwardLossRatio = _HwIpfpmMcpForwardLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 10),
    _HwIpfpmMcpForwardLossRatio_Type()
)
hwIpfpmMcpForwardLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardLossRatio.setStatus("current")
_HwIpfpmMcpBackwardLossPkts_Type = Counter64
_HwIpfpmMcpBackwardLossPkts_Object = MibTableColumn
hwIpfpmMcpBackwardLossPkts = _HwIpfpmMcpBackwardLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 11),
    _HwIpfpmMcpBackwardLossPkts_Type()
)
hwIpfpmMcpBackwardLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardLossPkts.setStatus("current")
_HwIpfpmMcpBackwardLossPktsSign_Type = Integer32
_HwIpfpmMcpBackwardLossPktsSign_Object = MibTableColumn
hwIpfpmMcpBackwardLossPktsSign = _HwIpfpmMcpBackwardLossPktsSign_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 12),
    _HwIpfpmMcpBackwardLossPktsSign_Type()
)
hwIpfpmMcpBackwardLossPktsSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardLossPktsSign.setStatus("current")
_HwIpfpmMcpBackwardLossBytes_Type = Counter64
_HwIpfpmMcpBackwardLossBytes_Object = MibTableColumn
hwIpfpmMcpBackwardLossBytes = _HwIpfpmMcpBackwardLossBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 13),
    _HwIpfpmMcpBackwardLossBytes_Type()
)
hwIpfpmMcpBackwardLossBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardLossBytes.setStatus("current")
_HwIpfpmMcpBackwardLossBytesSign_Type = Integer32
_HwIpfpmMcpBackwardLossBytesSign_Object = MibTableColumn
hwIpfpmMcpBackwardLossBytesSign = _HwIpfpmMcpBackwardLossBytesSign_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 14),
    _HwIpfpmMcpBackwardLossBytesSign_Type()
)
hwIpfpmMcpBackwardLossBytesSign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardLossBytesSign.setStatus("current")
_HwIpfpmMcpBackwardPkts_Type = Counter64
_HwIpfpmMcpBackwardPkts_Object = MibTableColumn
hwIpfpmMcpBackwardPkts = _HwIpfpmMcpBackwardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 15),
    _HwIpfpmMcpBackwardPkts_Type()
)
hwIpfpmMcpBackwardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardPkts.setStatus("current")
_HwIpfpmMcpBackwardBytes_Type = Counter64
_HwIpfpmMcpBackwardBytes_Object = MibTableColumn
hwIpfpmMcpBackwardBytes = _HwIpfpmMcpBackwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 16),
    _HwIpfpmMcpBackwardBytes_Type()
)
hwIpfpmMcpBackwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardBytes.setStatus("current")
_HwIpfpmMcpBackwardLossRatio_Type = Integer32
_HwIpfpmMcpBackwardLossRatio_Object = MibTableColumn
hwIpfpmMcpBackwardLossRatio = _HwIpfpmMcpBackwardLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 17),
    _HwIpfpmMcpBackwardLossRatio_Type()
)
hwIpfpmMcpBackwardLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardLossRatio.setStatus("current")
_HwIpfpmMcpForwardLossMMSType_Type = HWIpfpmMMSType
_HwIpfpmMcpForwardLossMMSType_Object = MibTableColumn
hwIpfpmMcpForwardLossMMSType = _HwIpfpmMcpForwardLossMMSType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 18),
    _HwIpfpmMcpForwardLossMMSType_Type()
)
hwIpfpmMcpForwardLossMMSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardLossMMSType.setStatus("current")
_HwIpfpmMcpForwardLossMMSSwitch_Type = TruthValue
_HwIpfpmMcpForwardLossMMSSwitch_Object = MibTableColumn
hwIpfpmMcpForwardLossMMSSwitch = _HwIpfpmMcpForwardLossMMSSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 4, 1, 19),
    _HwIpfpmMcpForwardLossMMSSwitch_Type()
)
hwIpfpmMcpForwardLossMMSSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardLossMMSSwitch.setStatus("current")
_HwIpfpmMcpOneDelayStatTable_Object = MibTable
hwIpfpmMcpOneDelayStatTable = _HwIpfpmMcpOneDelayStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hwIpfpmMcpOneDelayStatTable.setStatus("current")
_HwIpfpmMcpOneDelayStatEntry_Object = MibTableRow
hwIpfpmMcpOneDelayStatEntry = _HwIpfpmMcpOneDelayStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 5, 1)
)
hwIpfpmMcpOneDelayStatEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpAchId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpSeqNoHigh"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpSeqNoLow"),
)
if mibBuilder.loadTexts:
    hwIpfpmMcpOneDelayStatEntry.setStatus("current")
_HwIpfpmMcpOneDelayErrInfo_Type = HWIpfpmStatErrInfo
_HwIpfpmMcpOneDelayErrInfo_Object = MibTableColumn
hwIpfpmMcpOneDelayErrInfo = _HwIpfpmMcpOneDelayErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 5, 1, 1),
    _HwIpfpmMcpOneDelayErrInfo_Type()
)
hwIpfpmMcpOneDelayErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpOneDelayErrInfo.setStatus("current")
_HwIpfpmMcpForwardOneDelay_Type = Integer32
_HwIpfpmMcpForwardOneDelay_Object = MibTableColumn
hwIpfpmMcpForwardOneDelay = _HwIpfpmMcpForwardOneDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 5, 1, 2),
    _HwIpfpmMcpForwardOneDelay_Type()
)
hwIpfpmMcpForwardOneDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardOneDelay.setStatus("current")
_HwIpfpmMcpForwardOneDelayVariation_Type = Integer32
_HwIpfpmMcpForwardOneDelayVariation_Object = MibTableColumn
hwIpfpmMcpForwardOneDelayVariation = _HwIpfpmMcpForwardOneDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 5, 1, 3),
    _HwIpfpmMcpForwardOneDelayVariation_Type()
)
hwIpfpmMcpForwardOneDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardOneDelayVariation.setStatus("current")
_HwIpfpmMcpBackwardOneDelay_Type = Integer32
_HwIpfpmMcpBackwardOneDelay_Object = MibTableColumn
hwIpfpmMcpBackwardOneDelay = _HwIpfpmMcpBackwardOneDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 5, 1, 4),
    _HwIpfpmMcpBackwardOneDelay_Type()
)
hwIpfpmMcpBackwardOneDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardOneDelay.setStatus("current")
_HwIpfpmMcpBackwardOneDelayVariation_Type = Integer32
_HwIpfpmMcpBackwardOneDelayVariation_Object = MibTableColumn
hwIpfpmMcpBackwardOneDelayVariation = _HwIpfpmMcpBackwardOneDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 5, 1, 5),
    _HwIpfpmMcpBackwardOneDelayVariation_Type()
)
hwIpfpmMcpBackwardOneDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardOneDelayVariation.setStatus("current")
_HwIpfpmMcpForwardOneDelayMMSType_Type = HWIpfpmMMSType
_HwIpfpmMcpForwardOneDelayMMSType_Object = MibTableColumn
hwIpfpmMcpForwardOneDelayMMSType = _HwIpfpmMcpForwardOneDelayMMSType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 5, 1, 6),
    _HwIpfpmMcpForwardOneDelayMMSType_Type()
)
hwIpfpmMcpForwardOneDelayMMSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardOneDelayMMSType.setStatus("current")
_HwIpfpmMcpTwoDelayStatTable_Object = MibTable
hwIpfpmMcpTwoDelayStatTable = _HwIpfpmMcpTwoDelayStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hwIpfpmMcpTwoDelayStatTable.setStatus("current")
_HwIpfpmMcpTwoDelayStatEntry_Object = MibTableRow
hwIpfpmMcpTwoDelayStatEntry = _HwIpfpmMcpTwoDelayStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 6, 1)
)
hwIpfpmMcpTwoDelayStatEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpAchId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpSeqNoHigh"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmMcpSeqNoLow"),
)
if mibBuilder.loadTexts:
    hwIpfpmMcpTwoDelayStatEntry.setStatus("current")
_HwIpfpmMcpTwoDelayErrInfo_Type = HWIpfpmStatErrInfo
_HwIpfpmMcpTwoDelayErrInfo_Object = MibTableColumn
hwIpfpmMcpTwoDelayErrInfo = _HwIpfpmMcpTwoDelayErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 6, 1, 1),
    _HwIpfpmMcpTwoDelayErrInfo_Type()
)
hwIpfpmMcpTwoDelayErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpTwoDelayErrInfo.setStatus("current")
_HwIpfpmMcpTwoDelay_Type = Integer32
_HwIpfpmMcpTwoDelay_Object = MibTableColumn
hwIpfpmMcpTwoDelay = _HwIpfpmMcpTwoDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 6, 1, 2),
    _HwIpfpmMcpTwoDelay_Type()
)
hwIpfpmMcpTwoDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpTwoDelay.setStatus("current")
_HwIpfpmMcpTwoDelayVariation_Type = Integer32
_HwIpfpmMcpTwoDelayVariation_Object = MibTableColumn
hwIpfpmMcpTwoDelayVariation = _HwIpfpmMcpTwoDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 6, 1, 3),
    _HwIpfpmMcpTwoDelayVariation_Type()
)
hwIpfpmMcpTwoDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpTwoDelayVariation.setStatus("current")
_HwIpfpmMcpForwardDelay_Type = Integer32
_HwIpfpmMcpForwardDelay_Object = MibTableColumn
hwIpfpmMcpForwardDelay = _HwIpfpmMcpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 6, 1, 4),
    _HwIpfpmMcpForwardDelay_Type()
)
hwIpfpmMcpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardDelay.setStatus("current")
_HwIpfpmMcpForwardDelayVariation_Type = Integer32
_HwIpfpmMcpForwardDelayVariation_Object = MibTableColumn
hwIpfpmMcpForwardDelayVariation = _HwIpfpmMcpForwardDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 6, 1, 5),
    _HwIpfpmMcpForwardDelayVariation_Type()
)
hwIpfpmMcpForwardDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpForwardDelayVariation.setStatus("current")
_HwIpfpmMcpBackwardDelay_Type = Integer32
_HwIpfpmMcpBackwardDelay_Object = MibTableColumn
hwIpfpmMcpBackwardDelay = _HwIpfpmMcpBackwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 6, 1, 6),
    _HwIpfpmMcpBackwardDelay_Type()
)
hwIpfpmMcpBackwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardDelay.setStatus("current")
_HwIpfpmMcpBackwardDelayVariation_Type = Integer32
_HwIpfpmMcpBackwardDelayVariation_Object = MibTableColumn
hwIpfpmMcpBackwardDelayVariation = _HwIpfpmMcpBackwardDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 1, 2, 6, 1, 7),
    _HwIpfpmMcpBackwardDelayVariation_Type()
)
hwIpfpmMcpBackwardDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmMcpBackwardDelayVariation.setStatus("current")
_HwIpfpmDcpObjects_ObjectIdentity = ObjectIdentity
hwIpfpmDcpObjects = _HwIpfpmDcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2)
)
_HwIpfpmDcpConfiguration_ObjectIdentity = ObjectIdentity
hwIpfpmDcpConfiguration = _HwIpfpmDcpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1)
)
_HwIpfpmDcpGlobalTable_ObjectIdentity = ObjectIdentity
hwIpfpmDcpGlobalTable = _HwIpfpmDcpGlobalTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 1)
)


class _HwIpfpmDcpEnable_Type(HWEnabledStatus):
    """Custom type hwIpfpmDcpEnable based on HWEnabledStatus"""


_HwIpfpmDcpEnable_Object = MibScalar
hwIpfpmDcpEnable = _HwIpfpmDcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 1, 1),
    _HwIpfpmDcpEnable_Type()
)
hwIpfpmDcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpEnable.setStatus("current")
_HwIpfpmDcpId_Type = IpAddress
_HwIpfpmDcpId_Object = MibScalar
hwIpfpmDcpId = _HwIpfpmDcpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 1, 2),
    _HwIpfpmDcpId_Type()
)
hwIpfpmDcpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpId.setStatus("current")


class _HwIpfpmDcpMeasureColorFlag_Type(OctetString):
    """Custom type hwIpfpmDcpMeasureColorFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HwIpfpmDcpMeasureColorFlag_Type.__name__ = "OctetString"
_HwIpfpmDcpMeasureColorFlag_Object = MibScalar
hwIpfpmDcpMeasureColorFlag = _HwIpfpmDcpMeasureColorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 1, 3),
    _HwIpfpmDcpMeasureColorFlag_Type()
)
hwIpfpmDcpMeasureColorFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpMeasureColorFlag.setStatus("current")
_HwIpfpmDcpMcpId_Type = IpAddress
_HwIpfpmDcpMcpId_Object = MibScalar
hwIpfpmDcpMcpId = _HwIpfpmDcpMcpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 1, 6),
    _HwIpfpmDcpMcpId_Type()
)
hwIpfpmDcpMcpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpMcpId.setStatus("current")


class _HwIpfpmDcpMcpPort_Type(Integer32):
    """Custom type hwIpfpmDcpMcpPort based on Integer32"""
    defaultValue = 65030

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HwIpfpmDcpMcpPort_Type.__name__ = "Integer32"
_HwIpfpmDcpMcpPort_Object = MibScalar
hwIpfpmDcpMcpPort = _HwIpfpmDcpMcpPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 1, 7),
    _HwIpfpmDcpMcpPort_Type()
)
hwIpfpmDcpMcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpMcpPort.setStatus("current")


class _HwIpfpmDcpMcpVpnName_Type(OctetString):
    """Custom type hwIpfpmDcpMcpVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwIpfpmDcpMcpVpnName_Type.__name__ = "OctetString"
_HwIpfpmDcpMcpVpnName_Object = MibScalar
hwIpfpmDcpMcpVpnName = _HwIpfpmDcpMcpVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 1, 8),
    _HwIpfpmDcpMcpVpnName_Type()
)
hwIpfpmDcpMcpVpnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpMcpVpnName.setStatus("current")
_HwIpfpmDcpMcpVpnType_Type = HWIpfpmVpnType
_HwIpfpmDcpMcpVpnType_Object = MibScalar
hwIpfpmDcpMcpVpnType = _HwIpfpmDcpMcpVpnType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 1, 9),
    _HwIpfpmDcpMcpVpnType_Type()
)
hwIpfpmDcpMcpVpnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpMcpVpnType.setStatus("current")
_HwIpfpmDcpAuthTable_Object = MibTable
hwIpfpmDcpAuthTable = _HwIpfpmDcpAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpAuthTable.setStatus("current")
_HwIpfpmDcpAuthEntry_Object = MibTableRow
hwIpfpmDcpAuthEntry = _HwIpfpmDcpAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 7, 1)
)
hwIpfpmDcpAuthEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpAuthKeyId"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpAuthEntry.setStatus("current")


class _HwIpfpmDcpAuthKeyId_Type(Integer32):
    """Custom type hwIpfpmDcpAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwIpfpmDcpAuthKeyId_Type.__name__ = "Integer32"
_HwIpfpmDcpAuthKeyId_Object = MibTableColumn
hwIpfpmDcpAuthKeyId = _HwIpfpmDcpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 7, 1, 1),
    _HwIpfpmDcpAuthKeyId_Type()
)
hwIpfpmDcpAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpAuthKeyId.setStatus("current")
_HwIpfpmDcpAuthType_Type = HWIpfpmAuthType
_HwIpfpmDcpAuthType_Object = MibTableColumn
hwIpfpmDcpAuthType = _HwIpfpmDcpAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 7, 1, 2),
    _HwIpfpmDcpAuthType_Type()
)
hwIpfpmDcpAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpAuthType.setStatus("current")


class _HwIpfpmDcpAuthKey_Type(OctetString):
    """Custom type hwIpfpmDcpAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwIpfpmDcpAuthKey_Type.__name__ = "OctetString"
_HwIpfpmDcpAuthKey_Object = MibTableColumn
hwIpfpmDcpAuthKey = _HwIpfpmDcpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 7, 1, 3),
    _HwIpfpmDcpAuthKey_Type()
)
hwIpfpmDcpAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpAuthKey.setStatus("current")
_HwIpfpmDcpAuthRowStatus_Type = RowStatus
_HwIpfpmDcpAuthRowStatus_Object = MibTableColumn
hwIpfpmDcpAuthRowStatus = _HwIpfpmDcpAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 7, 1, 4),
    _HwIpfpmDcpAuthRowStatus_Type()
)
hwIpfpmDcpAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpAuthRowStatus.setStatus("current")
_HwIpfpmDcpInstTable_Object = MibTable
hwIpfpmDcpInstTable = _HwIpfpmDcpInstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTable.setStatus("current")
_HwIpfpmDcpInstEntry_Object = MibTableRow
hwIpfpmDcpInstEntry = _HwIpfpmDcpInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1)
)
hwIpfpmDcpInstEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstId"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpInstEntry.setStatus("current")


class _HwIpfpmDcpInstId_Type(Integer32):
    """Custom type hwIpfpmDcpInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8355838),
        ValueRangeConstraint(16711681, 16777214),
    )


_HwIpfpmDcpInstId_Type.__name__ = "Integer32"
_HwIpfpmDcpInstId_Object = MibTableColumn
hwIpfpmDcpInstId = _HwIpfpmDcpInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 1),
    _HwIpfpmDcpInstId_Type()
)
hwIpfpmDcpInstId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstId.setStatus("current")


class _HwIpfpmDcpInstDesc_Type(OctetString):
    """Custom type hwIpfpmDcpInstDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwIpfpmDcpInstDesc_Type.__name__ = "OctetString"
_HwIpfpmDcpInstDesc_Object = MibTableColumn
hwIpfpmDcpInstDesc = _HwIpfpmDcpInstDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 2),
    _HwIpfpmDcpInstDesc_Type()
)
hwIpfpmDcpInstDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstDesc.setStatus("current")
_HwIpfpmDcpInstMcpId_Type = IpAddress
_HwIpfpmDcpInstMcpId_Object = MibTableColumn
hwIpfpmDcpInstMcpId = _HwIpfpmDcpInstMcpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 3),
    _HwIpfpmDcpInstMcpId_Type()
)
hwIpfpmDcpInstMcpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstMcpId.setStatus("current")


class _HwIpfpmDcpInstMcpPort_Type(Integer32):
    """Custom type hwIpfpmDcpInstMcpPort based on Integer32"""
    defaultValue = 65030

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HwIpfpmDcpInstMcpPort_Type.__name__ = "Integer32"
_HwIpfpmDcpInstMcpPort_Object = MibTableColumn
hwIpfpmDcpInstMcpPort = _HwIpfpmDcpInstMcpPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 4),
    _HwIpfpmDcpInstMcpPort_Type()
)
hwIpfpmDcpInstMcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstMcpPort.setStatus("current")


class _HwIpfpmDcpInstInterval_Type(HWIpfpmInstIntervalType):
    """Custom type hwIpfpmDcpInstInterval based on HWIpfpmInstIntervalType"""


_HwIpfpmDcpInstInterval_Object = MibTableColumn
hwIpfpmDcpInstInterval = _HwIpfpmDcpInstInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 5),
    _HwIpfpmDcpInstInterval_Type()
)
hwIpfpmDcpInstInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstInterval.setStatus("current")
_HwIpfpmDcpInstRowStatus_Type = RowStatus
_HwIpfpmDcpInstRowStatus_Object = MibTableColumn
hwIpfpmDcpInstRowStatus = _HwIpfpmDcpInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 6),
    _HwIpfpmDcpInstRowStatus_Type()
)
hwIpfpmDcpInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstRowStatus.setStatus("current")
_HwIpfpmDcpInstType_Type = HWIpfpmInstType
_HwIpfpmDcpInstType_Object = MibTableColumn
hwIpfpmDcpInstType = _HwIpfpmDcpInstType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 7),
    _HwIpfpmDcpInstType_Type()
)
hwIpfpmDcpInstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstType.setStatus("current")


class _HwIpfpmDcpSourceInstId_Type(Integer32):
    """Custom type hwIpfpmDcpSourceInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16711681, 16777214),
    )


_HwIpfpmDcpSourceInstId_Type.__name__ = "Integer32"
_HwIpfpmDcpSourceInstId_Object = MibTableColumn
hwIpfpmDcpSourceInstId = _HwIpfpmDcpSourceInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 8),
    _HwIpfpmDcpSourceInstId_Type()
)
hwIpfpmDcpSourceInstId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpSourceInstId.setStatus("current")


class _HwIpfpmDcpInstMcpVpnName_Type(OctetString):
    """Custom type hwIpfpmDcpInstMcpVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwIpfpmDcpInstMcpVpnName_Type.__name__ = "OctetString"
_HwIpfpmDcpInstMcpVpnName_Object = MibTableColumn
hwIpfpmDcpInstMcpVpnName = _HwIpfpmDcpInstMcpVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 9),
    _HwIpfpmDcpInstMcpVpnName_Type()
)
hwIpfpmDcpInstMcpVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstMcpVpnName.setStatus("current")
_HwIpfpmDcpInstMcpVpnType_Type = HWIpfpmVpnType
_HwIpfpmDcpInstMcpVpnType_Object = MibTableColumn
hwIpfpmDcpInstMcpVpnType = _HwIpfpmDcpInstMcpVpnType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 10),
    _HwIpfpmDcpInstMcpVpnType_Type()
)
hwIpfpmDcpInstMcpVpnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstMcpVpnType.setStatus("current")


class _HwIpfpmDcpInstGroupId_Type(Integer32):
    """Custom type hwIpfpmDcpInstGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8355838),
    )


_HwIpfpmDcpInstGroupId_Type.__name__ = "Integer32"
_HwIpfpmDcpInstGroupId_Object = MibTableColumn
hwIpfpmDcpInstGroupId = _HwIpfpmDcpInstGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 8, 1, 11),
    _HwIpfpmDcpInstGroupId_Type()
)
hwIpfpmDcpInstGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstGroupId.setStatus("current")
_HwIpfpmDcpInstAuthTable_Object = MibTable
hwIpfpmDcpInstAuthTable = _HwIpfpmDcpInstAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpInstAuthTable.setStatus("current")
_HwIpfpmDcpInstAuthEntry_Object = MibTableRow
hwIpfpmDcpInstAuthEntry = _HwIpfpmDcpInstAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 9, 1)
)
hwIpfpmDcpInstAuthEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstAuthKeyId"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpInstAuthEntry.setStatus("current")


class _HwIpfpmDcpInstAuthKeyId_Type(Integer32):
    """Custom type hwIpfpmDcpInstAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwIpfpmDcpInstAuthKeyId_Type.__name__ = "Integer32"
_HwIpfpmDcpInstAuthKeyId_Object = MibTableColumn
hwIpfpmDcpInstAuthKeyId = _HwIpfpmDcpInstAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 9, 1, 1),
    _HwIpfpmDcpInstAuthKeyId_Type()
)
hwIpfpmDcpInstAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstAuthKeyId.setStatus("current")
_HwIpfpmDcpInstAuthType_Type = HWIpfpmAuthType
_HwIpfpmDcpInstAuthType_Object = MibTableColumn
hwIpfpmDcpInstAuthType = _HwIpfpmDcpInstAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 9, 1, 2),
    _HwIpfpmDcpInstAuthType_Type()
)
hwIpfpmDcpInstAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstAuthType.setStatus("current")


class _HwIpfpmDcpInstAuthKey_Type(OctetString):
    """Custom type hwIpfpmDcpInstAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwIpfpmDcpInstAuthKey_Type.__name__ = "OctetString"
_HwIpfpmDcpInstAuthKey_Object = MibTableColumn
hwIpfpmDcpInstAuthKey = _HwIpfpmDcpInstAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 9, 1, 3),
    _HwIpfpmDcpInstAuthKey_Type()
)
hwIpfpmDcpInstAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstAuthKey.setStatus("current")
_HwIpfpmDcpInstAuthRowStatus_Type = RowStatus
_HwIpfpmDcpInstAuthRowStatus_Object = MibTableColumn
hwIpfpmDcpInstAuthRowStatus = _HwIpfpmDcpInstAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 9, 1, 4),
    _HwIpfpmDcpInstAuthRowStatus_Type()
)
hwIpfpmDcpInstAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstAuthRowStatus.setStatus("current")
_HwIpfpmDcpFlowTable_Object = MibTable
hwIpfpmDcpFlowTable = _HwIpfpmDcpFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowTable.setStatus("current")
_HwIpfpmDcpFlowEntry_Object = MibTableRow
hwIpfpmDcpFlowEntry = _HwIpfpmDcpFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1)
)
hwIpfpmDcpFlowEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowType"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowEntry.setStatus("current")
_HwIpfpmDcpFlowType_Type = HWIpfpmFlowType
_HwIpfpmDcpFlowType_Object = MibTableColumn
hwIpfpmDcpFlowType = _HwIpfpmDcpFlowType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 1),
    _HwIpfpmDcpFlowType_Type()
)
hwIpfpmDcpFlowType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowType.setStatus("current")


class _HwIpfpmDcpFlowProtocol_Type(Integer32):
    """Custom type hwIpfpmDcpFlowProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIpfpmDcpFlowProtocol_Type.__name__ = "Integer32"
_HwIpfpmDcpFlowProtocol_Object = MibTableColumn
hwIpfpmDcpFlowProtocol = _HwIpfpmDcpFlowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 2),
    _HwIpfpmDcpFlowProtocol_Type()
)
hwIpfpmDcpFlowProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowProtocol.setStatus("current")


class _HwIpfpmDcpFlowDscp_Type(Integer32):
    """Custom type hwIpfpmDcpFlowDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_HwIpfpmDcpFlowDscp_Type.__name__ = "Integer32"
_HwIpfpmDcpFlowDscp_Object = MibTableColumn
hwIpfpmDcpFlowDscp = _HwIpfpmDcpFlowDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 3),
    _HwIpfpmDcpFlowDscp_Type()
)
hwIpfpmDcpFlowDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowDscp.setStatus("current")
_HwIpfpmDcpFlowSrcAddr_Type = IpAddress
_HwIpfpmDcpFlowSrcAddr_Object = MibTableColumn
hwIpfpmDcpFlowSrcAddr = _HwIpfpmDcpFlowSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 4),
    _HwIpfpmDcpFlowSrcAddr_Type()
)
hwIpfpmDcpFlowSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowSrcAddr.setStatus("current")


class _HwIpfpmDcpFlowSrcMaskLen_Type(Integer32):
    """Custom type hwIpfpmDcpFlowSrcMaskLen based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwIpfpmDcpFlowSrcMaskLen_Type.__name__ = "Integer32"
_HwIpfpmDcpFlowSrcMaskLen_Object = MibTableColumn
hwIpfpmDcpFlowSrcMaskLen = _HwIpfpmDcpFlowSrcMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 5),
    _HwIpfpmDcpFlowSrcMaskLen_Type()
)
hwIpfpmDcpFlowSrcMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowSrcMaskLen.setStatus("current")
_HwIpfpmDcpFlowDstAddr_Type = IpAddress
_HwIpfpmDcpFlowDstAddr_Object = MibTableColumn
hwIpfpmDcpFlowDstAddr = _HwIpfpmDcpFlowDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 6),
    _HwIpfpmDcpFlowDstAddr_Type()
)
hwIpfpmDcpFlowDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowDstAddr.setStatus("current")


class _HwIpfpmDcpFlowDstMaskLen_Type(Integer32):
    """Custom type hwIpfpmDcpFlowDstMaskLen based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwIpfpmDcpFlowDstMaskLen_Type.__name__ = "Integer32"
_HwIpfpmDcpFlowDstMaskLen_Object = MibTableColumn
hwIpfpmDcpFlowDstMaskLen = _HwIpfpmDcpFlowDstMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 7),
    _HwIpfpmDcpFlowDstMaskLen_Type()
)
hwIpfpmDcpFlowDstMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowDstMaskLen.setStatus("current")


class _HwIpfpmDcpFlowSrcPortBgn_Type(Integer32):
    """Custom type hwIpfpmDcpFlowSrcPortBgn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpfpmDcpFlowSrcPortBgn_Type.__name__ = "Integer32"
_HwIpfpmDcpFlowSrcPortBgn_Object = MibTableColumn
hwIpfpmDcpFlowSrcPortBgn = _HwIpfpmDcpFlowSrcPortBgn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 8),
    _HwIpfpmDcpFlowSrcPortBgn_Type()
)
hwIpfpmDcpFlowSrcPortBgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowSrcPortBgn.setStatus("current")


class _HwIpfpmDcpFlowSrcPortEnd_Type(Integer32):
    """Custom type hwIpfpmDcpFlowSrcPortEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpfpmDcpFlowSrcPortEnd_Type.__name__ = "Integer32"
_HwIpfpmDcpFlowSrcPortEnd_Object = MibTableColumn
hwIpfpmDcpFlowSrcPortEnd = _HwIpfpmDcpFlowSrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 9),
    _HwIpfpmDcpFlowSrcPortEnd_Type()
)
hwIpfpmDcpFlowSrcPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowSrcPortEnd.setStatus("current")


class _HwIpfpmDcpFlowDstPortBgn_Type(Integer32):
    """Custom type hwIpfpmDcpFlowDstPortBgn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpfpmDcpFlowDstPortBgn_Type.__name__ = "Integer32"
_HwIpfpmDcpFlowDstPortBgn_Object = MibTableColumn
hwIpfpmDcpFlowDstPortBgn = _HwIpfpmDcpFlowDstPortBgn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 10),
    _HwIpfpmDcpFlowDstPortBgn_Type()
)
hwIpfpmDcpFlowDstPortBgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowDstPortBgn.setStatus("current")


class _HwIpfpmDcpFlowDstPortEnd_Type(Integer32):
    """Custom type hwIpfpmDcpFlowDstPortEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIpfpmDcpFlowDstPortEnd_Type.__name__ = "Integer32"
_HwIpfpmDcpFlowDstPortEnd_Object = MibTableColumn
hwIpfpmDcpFlowDstPortEnd = _HwIpfpmDcpFlowDstPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 11),
    _HwIpfpmDcpFlowDstPortEnd_Type()
)
hwIpfpmDcpFlowDstPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowDstPortEnd.setStatus("current")
_HwIpfpmDcpFlowRowStatus_Type = RowStatus
_HwIpfpmDcpFlowRowStatus_Object = MibTableColumn
hwIpfpmDcpFlowRowStatus = _HwIpfpmDcpFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 12),
    _HwIpfpmDcpFlowRowStatus_Type()
)
hwIpfpmDcpFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowRowStatus.setStatus("current")


class _HwIpfpmDcpFlowOuterSrcAddr_Type(IpAddress):
    """Custom type hwIpfpmDcpFlowOuterSrcAddr based on IpAddress"""
    defaultValue = 0


_HwIpfpmDcpFlowOuterSrcAddr_Object = MibTableColumn
hwIpfpmDcpFlowOuterSrcAddr = _HwIpfpmDcpFlowOuterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 13),
    _HwIpfpmDcpFlowOuterSrcAddr_Type()
)
hwIpfpmDcpFlowOuterSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowOuterSrcAddr.setStatus("current")


class _HwIpfpmDcpFlowOuterDstAddr_Type(IpAddress):
    """Custom type hwIpfpmDcpFlowOuterDstAddr based on IpAddress"""
    defaultValue = 0


_HwIpfpmDcpFlowOuterDstAddr_Object = MibTableColumn
hwIpfpmDcpFlowOuterDstAddr = _HwIpfpmDcpFlowOuterDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 14),
    _HwIpfpmDcpFlowOuterDstAddr_Type()
)
hwIpfpmDcpFlowOuterDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowOuterDstAddr.setStatus("current")


class _HwIpfpmDcpFlowForwardGtpTeid_Type(Unsigned32):
    """Custom type hwIpfpmDcpFlowForwardGtpTeid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_HwIpfpmDcpFlowForwardGtpTeid_Type.__name__ = "Unsigned32"
_HwIpfpmDcpFlowForwardGtpTeid_Object = MibTableColumn
hwIpfpmDcpFlowForwardGtpTeid = _HwIpfpmDcpFlowForwardGtpTeid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 15),
    _HwIpfpmDcpFlowForwardGtpTeid_Type()
)
hwIpfpmDcpFlowForwardGtpTeid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowForwardGtpTeid.setStatus("current")


class _HwIpfpmDcpFlowBackwardGtpTeid_Type(Unsigned32):
    """Custom type hwIpfpmDcpFlowBackwardGtpTeid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_HwIpfpmDcpFlowBackwardGtpTeid_Type.__name__ = "Unsigned32"
_HwIpfpmDcpFlowBackwardGtpTeid_Object = MibTableColumn
hwIpfpmDcpFlowBackwardGtpTeid = _HwIpfpmDcpFlowBackwardGtpTeid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 10, 1, 16),
    _HwIpfpmDcpFlowBackwardGtpTeid_Type()
)
hwIpfpmDcpFlowBackwardGtpTeid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowBackwardGtpTeid.setStatus("current")
_HwIpfpmDcpInstTlpTable_Object = MibTable
hwIpfpmDcpInstTlpTable = _HwIpfpmDcpInstTlpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpTable.setStatus("current")
_HwIpfpmDcpInstTlpEntry_Object = MibTableRow
hwIpfpmDcpInstTlpEntry = _HwIpfpmDcpInstTlpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1)
)
hwIpfpmDcpInstTlpEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpId"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpEntry.setStatus("current")
_HwIpfpmDcpInstTlpRole_Type = HWIpfpmTlpRole
_HwIpfpmDcpInstTlpRole_Object = MibTableColumn
hwIpfpmDcpInstTlpRole = _HwIpfpmDcpInstTlpRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 1),
    _HwIpfpmDcpInstTlpRole_Type()
)
hwIpfpmDcpInstTlpRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpRole.setStatus("current")
_HwIpfpmDcpInstTlpFlowType_Type = HWIpfpmFlowType
_HwIpfpmDcpInstTlpFlowType_Object = MibTableColumn
hwIpfpmDcpInstTlpFlowType = _HwIpfpmDcpInstTlpFlowType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 2),
    _HwIpfpmDcpInstTlpFlowType_Type()
)
hwIpfpmDcpInstTlpFlowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpFlowType.setStatus("current")
_HwIpfpmDcpInstTlpDirec_Type = HWIpfpmFlowTlpDirec
_HwIpfpmDcpInstTlpDirec_Object = MibTableColumn
hwIpfpmDcpInstTlpDirec = _HwIpfpmDcpInstTlpDirec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 3),
    _HwIpfpmDcpInstTlpDirec_Type()
)
hwIpfpmDcpInstTlpDirec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpDirec.setStatus("current")


class _HwIpfpmDcpInstTlpVpnLabel_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpVpnLabel based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_HwIpfpmDcpInstTlpVpnLabel_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpVpnLabel_Object = MibTableColumn
hwIpfpmDcpInstTlpVpnLabel = _HwIpfpmDcpInstTlpVpnLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 4),
    _HwIpfpmDcpInstTlpVpnLabel_Type()
)
hwIpfpmDcpInstTlpVpnLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpVpnLabel.setStatus("current")


class _HwIpfpmDcpInstTlpCtrlWordFlag_Type(TruthValue):
    """Custom type hwIpfpmDcpInstTlpCtrlWordFlag based on TruthValue"""


_HwIpfpmDcpInstTlpCtrlWordFlag_Object = MibTableColumn
hwIpfpmDcpInstTlpCtrlWordFlag = _HwIpfpmDcpInstTlpCtrlWordFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 5),
    _HwIpfpmDcpInstTlpCtrlWordFlag_Type()
)
hwIpfpmDcpInstTlpCtrlWordFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpCtrlWordFlag.setStatus("current")


class _HwIpfpmDcpInstTlpLspLabel_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpLspLabel based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_HwIpfpmDcpInstTlpLspLabel_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpLspLabel_Object = MibTableColumn
hwIpfpmDcpInstTlpLspLabel = _HwIpfpmDcpInstTlpLspLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 6),
    _HwIpfpmDcpInstTlpLspLabel_Type()
)
hwIpfpmDcpInstTlpLspLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpLspLabel.setStatus("current")


class _HwIpfpmDcpInstTlpL2VpnFlag_Type(TruthValue):
    """Custom type hwIpfpmDcpInstTlpL2VpnFlag based on TruthValue"""


_HwIpfpmDcpInstTlpL2VpnFlag_Object = MibTableColumn
hwIpfpmDcpInstTlpL2VpnFlag = _HwIpfpmDcpInstTlpL2VpnFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 7),
    _HwIpfpmDcpInstTlpL2VpnFlag_Type()
)
hwIpfpmDcpInstTlpL2VpnFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpL2VpnFlag.setStatus("current")


class _HwIpfpmDcpInstTlpTpId_Type(OctetString):
    """Custom type hwIpfpmDcpInstTlpTpId based on OctetString"""
    defaultValue = 8100

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_HwIpfpmDcpInstTlpTpId_Type.__name__ = "OctetString"
_HwIpfpmDcpInstTlpTpId_Object = MibTableColumn
hwIpfpmDcpInstTlpTpId = _HwIpfpmDcpInstTlpTpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 8),
    _HwIpfpmDcpInstTlpTpId_Type()
)
hwIpfpmDcpInstTlpTpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpTpId.setStatus("current")
_HwIpfpmDcpInstTlpRowStatus_Type = RowStatus
_HwIpfpmDcpInstTlpRowStatus_Object = MibTableColumn
hwIpfpmDcpInstTlpRowStatus = _HwIpfpmDcpInstTlpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 9),
    _HwIpfpmDcpInstTlpRowStatus_Type()
)
hwIpfpmDcpInstTlpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpRowStatus.setStatus("current")
_HwIpfpmDcpInstTlpMultiSrcType_Type = HWIpfpmMMSType
_HwIpfpmDcpInstTlpMultiSrcType_Object = MibTableColumn
hwIpfpmDcpInstTlpMultiSrcType = _HwIpfpmDcpInstTlpMultiSrcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 10),
    _HwIpfpmDcpInstTlpMultiSrcType_Type()
)
hwIpfpmDcpInstTlpMultiSrcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpMultiSrcType.setStatus("current")


class _HwIpfpmDcpInstTlpFlowLabelFlag_Type(TruthValue):
    """Custom type hwIpfpmDcpInstTlpFlowLabelFlag based on TruthValue"""


_HwIpfpmDcpInstTlpFlowLabelFlag_Object = MibTableColumn
hwIpfpmDcpInstTlpFlowLabelFlag = _HwIpfpmDcpInstTlpFlowLabelFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 11),
    _HwIpfpmDcpInstTlpFlowLabelFlag_Type()
)
hwIpfpmDcpInstTlpFlowLabelFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpFlowLabelFlag.setStatus("current")


class _HwIpfpmDcpInstTlpLspLabel2_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpLspLabel2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_HwIpfpmDcpInstTlpLspLabel2_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpLspLabel2_Object = MibTableColumn
hwIpfpmDcpInstTlpLspLabel2 = _HwIpfpmDcpInstTlpLspLabel2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 12),
    _HwIpfpmDcpInstTlpLspLabel2_Type()
)
hwIpfpmDcpInstTlpLspLabel2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpLspLabel2.setStatus("current")


class _HwIpfpmDcpInstTlpLspLabel3_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpLspLabel3 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_HwIpfpmDcpInstTlpLspLabel3_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpLspLabel3_Object = MibTableColumn
hwIpfpmDcpInstTlpLspLabel3 = _HwIpfpmDcpInstTlpLspLabel3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 13),
    _HwIpfpmDcpInstTlpLspLabel3_Type()
)
hwIpfpmDcpInstTlpLspLabel3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpLspLabel3.setStatus("current")


class _HwIpfpmDcpInstTlpOuterVlan_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpOuterVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwIpfpmDcpInstTlpOuterVlan_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpOuterVlan_Object = MibTableColumn
hwIpfpmDcpInstTlpOuterVlan = _HwIpfpmDcpInstTlpOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 14),
    _HwIpfpmDcpInstTlpOuterVlan_Type()
)
hwIpfpmDcpInstTlpOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpOuterVlan.setStatus("current")


class _HwIpfpmDcpInstTlpInnerVlan_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpInnerVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwIpfpmDcpInstTlpInnerVlan_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpInnerVlan_Object = MibTableColumn
hwIpfpmDcpInstTlpInnerVlan = _HwIpfpmDcpInstTlpInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 15),
    _HwIpfpmDcpInstTlpInnerVlan_Type()
)
hwIpfpmDcpInstTlpInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpInnerVlan.setStatus("current")


class _HwIpfpmDcpInstTlpBackwardVpnLabel_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpBackwardVpnLabel based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_HwIpfpmDcpInstTlpBackwardVpnLabel_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpBackwardVpnLabel_Object = MibTableColumn
hwIpfpmDcpInstTlpBackwardVpnLabel = _HwIpfpmDcpInstTlpBackwardVpnLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 16),
    _HwIpfpmDcpInstTlpBackwardVpnLabel_Type()
)
hwIpfpmDcpInstTlpBackwardVpnLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpBackwardVpnLabel.setStatus("current")


class _HwIpfpmDcpInstTlpBackwardCtrlWordFlag_Type(TruthValue):
    """Custom type hwIpfpmDcpInstTlpBackwardCtrlWordFlag based on TruthValue"""


_HwIpfpmDcpInstTlpBackwardCtrlWordFlag_Object = MibTableColumn
hwIpfpmDcpInstTlpBackwardCtrlWordFlag = _HwIpfpmDcpInstTlpBackwardCtrlWordFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 17),
    _HwIpfpmDcpInstTlpBackwardCtrlWordFlag_Type()
)
hwIpfpmDcpInstTlpBackwardCtrlWordFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpBackwardCtrlWordFlag.setStatus("current")


class _HwIpfpmDcpInstTlpBackwardLspLabel_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpBackwardLspLabel based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_HwIpfpmDcpInstTlpBackwardLspLabel_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpBackwardLspLabel_Object = MibTableColumn
hwIpfpmDcpInstTlpBackwardLspLabel = _HwIpfpmDcpInstTlpBackwardLspLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 18),
    _HwIpfpmDcpInstTlpBackwardLspLabel_Type()
)
hwIpfpmDcpInstTlpBackwardLspLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpBackwardLspLabel.setStatus("current")


class _HwIpfpmDcpInstTlpBackwardLspLabel2_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpBackwardLspLabel2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_HwIpfpmDcpInstTlpBackwardLspLabel2_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpBackwardLspLabel2_Object = MibTableColumn
hwIpfpmDcpInstTlpBackwardLspLabel2 = _HwIpfpmDcpInstTlpBackwardLspLabel2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 19),
    _HwIpfpmDcpInstTlpBackwardLspLabel2_Type()
)
hwIpfpmDcpInstTlpBackwardLspLabel2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpBackwardLspLabel2.setStatus("current")


class _HwIpfpmDcpInstTlpBackwardLspLabel3_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpBackwardLspLabel3 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1048575),
    )


_HwIpfpmDcpInstTlpBackwardLspLabel3_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpBackwardLspLabel3_Object = MibTableColumn
hwIpfpmDcpInstTlpBackwardLspLabel3 = _HwIpfpmDcpInstTlpBackwardLspLabel3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 20),
    _HwIpfpmDcpInstTlpBackwardLspLabel3_Type()
)
hwIpfpmDcpInstTlpBackwardLspLabel3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpBackwardLspLabel3.setStatus("current")


class _HwIpfpmDcpInstTlpBackwardL2VpnFlag_Type(TruthValue):
    """Custom type hwIpfpmDcpInstTlpBackwardL2VpnFlag based on TruthValue"""


_HwIpfpmDcpInstTlpBackwardL2VpnFlag_Object = MibTableColumn
hwIpfpmDcpInstTlpBackwardL2VpnFlag = _HwIpfpmDcpInstTlpBackwardL2VpnFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 21),
    _HwIpfpmDcpInstTlpBackwardL2VpnFlag_Type()
)
hwIpfpmDcpInstTlpBackwardL2VpnFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpBackwardL2VpnFlag.setStatus("current")


class _HwIpfpmDcpInstTlpBackwardFlowLabelFlag_Type(TruthValue):
    """Custom type hwIpfpmDcpInstTlpBackwardFlowLabelFlag based on TruthValue"""


_HwIpfpmDcpInstTlpBackwardFlowLabelFlag_Object = MibTableColumn
hwIpfpmDcpInstTlpBackwardFlowLabelFlag = _HwIpfpmDcpInstTlpBackwardFlowLabelFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 22),
    _HwIpfpmDcpInstTlpBackwardFlowLabelFlag_Type()
)
hwIpfpmDcpInstTlpBackwardFlowLabelFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpBackwardFlowLabelFlag.setStatus("current")


class _HwIpfpmDcpInstTlpBackwardOuterVlan_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpBackwardOuterVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwIpfpmDcpInstTlpBackwardOuterVlan_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpBackwardOuterVlan_Object = MibTableColumn
hwIpfpmDcpInstTlpBackwardOuterVlan = _HwIpfpmDcpInstTlpBackwardOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 23),
    _HwIpfpmDcpInstTlpBackwardOuterVlan_Type()
)
hwIpfpmDcpInstTlpBackwardOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpBackwardOuterVlan.setStatus("current")


class _HwIpfpmDcpInstTlpBackwardInnerVlan_Type(Integer32):
    """Custom type hwIpfpmDcpInstTlpBackwardInnerVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwIpfpmDcpInstTlpBackwardInnerVlan_Type.__name__ = "Integer32"
_HwIpfpmDcpInstTlpBackwardInnerVlan_Object = MibTableColumn
hwIpfpmDcpInstTlpBackwardInnerVlan = _HwIpfpmDcpInstTlpBackwardInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 24),
    _HwIpfpmDcpInstTlpBackwardInnerVlan_Type()
)
hwIpfpmDcpInstTlpBackwardInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpBackwardInnerVlan.setStatus("current")


class _HwIpfpmDcpInstTlpBackwardTpId_Type(OctetString):
    """Custom type hwIpfpmDcpInstTlpBackwardTpId based on OctetString"""
    defaultValue = 8100

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_HwIpfpmDcpInstTlpBackwardTpId_Type.__name__ = "OctetString"
_HwIpfpmDcpInstTlpBackwardTpId_Object = MibTableColumn
hwIpfpmDcpInstTlpBackwardTpId = _HwIpfpmDcpInstTlpBackwardTpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 11, 1, 25),
    _HwIpfpmDcpInstTlpBackwardTpId_Type()
)
hwIpfpmDcpInstTlpBackwardTpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpInstTlpBackwardTpId.setStatus("current")
_HwIpfpmDcpLossMeasTable_Object = MibTable
hwIpfpmDcpLossMeasTable = _HwIpfpmDcpLossMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 12)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpLossMeasTable.setStatus("current")
_HwIpfpmDcpLossMeasEntry_Object = MibTableRow
hwIpfpmDcpLossMeasEntry = _HwIpfpmDcpLossMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 12, 1)
)
hwIpfpmDcpLossMeasEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpLossTlpRole"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpLossMeasEntry.setStatus("current")


class _HwIpfpmDcpLossEnable_Type(HWEnabledStatus):
    """Custom type hwIpfpmDcpLossEnable based on HWEnabledStatus"""


_HwIpfpmDcpLossEnable_Object = MibTableColumn
hwIpfpmDcpLossEnable = _HwIpfpmDcpLossEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 12, 1, 1),
    _HwIpfpmDcpLossEnable_Type()
)
hwIpfpmDcpLossEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpLossEnable.setStatus("current")


class _HwIpfpmDcpLossContEnable_Type(HWEnabledStatus):
    """Custom type hwIpfpmDcpLossContEnable based on HWEnabledStatus"""


_HwIpfpmDcpLossContEnable_Object = MibTableColumn
hwIpfpmDcpLossContEnable = _HwIpfpmDcpLossContEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 12, 1, 2),
    _HwIpfpmDcpLossContEnable_Type()
)
hwIpfpmDcpLossContEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpLossContEnable.setStatus("current")
_HwIpfpmDcpLossTimeRange_Type = HWIpfpmMeasTimeRangeType
_HwIpfpmDcpLossTimeRange_Object = MibTableColumn
hwIpfpmDcpLossTimeRange = _HwIpfpmDcpLossTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 12, 1, 3),
    _HwIpfpmDcpLossTimeRange_Type()
)
hwIpfpmDcpLossTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpLossTimeRange.setStatus("current")


class _HwIpfpmDcpLossTlpRole_Type(HWIpfpmLossTlpRole):
    """Custom type hwIpfpmDcpLossTlpRole based on HWIpfpmLossTlpRole"""


_HwIpfpmDcpLossTlpRole_Object = MibTableColumn
hwIpfpmDcpLossTlpRole = _HwIpfpmDcpLossTlpRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 12, 1, 4),
    _HwIpfpmDcpLossTlpRole_Type()
)
hwIpfpmDcpLossTlpRole.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpLossTlpRole.setStatus("current")
_HwIpfpmDcpDelayMeasTable_Object = MibTable
hwIpfpmDcpDelayMeasTable = _HwIpfpmDcpDelayMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 13)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpDelayMeasTable.setStatus("current")
_HwIpfpmDcpDelayMeasEntry_Object = MibTableRow
hwIpfpmDcpDelayMeasEntry = _HwIpfpmDcpDelayMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 13, 1)
)
hwIpfpmDcpDelayMeasEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpDelayTlpRole"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpDelayMeasEntry.setStatus("current")


class _HwIpfpmDcpDelayEnable_Type(HWEnabledStatus):
    """Custom type hwIpfpmDcpDelayEnable based on HWEnabledStatus"""


_HwIpfpmDcpDelayEnable_Object = MibTableColumn
hwIpfpmDcpDelayEnable = _HwIpfpmDcpDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 13, 1, 1),
    _HwIpfpmDcpDelayEnable_Type()
)
hwIpfpmDcpDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpDelayEnable.setStatus("current")


class _HwIpfpmDcpDelayContEnable_Type(HWEnabledStatus):
    """Custom type hwIpfpmDcpDelayContEnable based on HWEnabledStatus"""


_HwIpfpmDcpDelayContEnable_Object = MibTableColumn
hwIpfpmDcpDelayContEnable = _HwIpfpmDcpDelayContEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 13, 1, 2),
    _HwIpfpmDcpDelayContEnable_Type()
)
hwIpfpmDcpDelayContEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpDelayContEnable.setStatus("current")
_HwIpfpmDcpDelayMeasType_Type = HWIpfpmDelayMeasType
_HwIpfpmDcpDelayMeasType_Object = MibTableColumn
hwIpfpmDcpDelayMeasType = _HwIpfpmDcpDelayMeasType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 13, 1, 3),
    _HwIpfpmDcpDelayMeasType_Type()
)
hwIpfpmDcpDelayMeasType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpDelayMeasType.setStatus("current")
_HwIpfpmDcpDelayTimeRange_Type = HWIpfpmMeasTimeRangeType
_HwIpfpmDcpDelayTimeRange_Object = MibTableColumn
hwIpfpmDcpDelayTimeRange = _HwIpfpmDcpDelayTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 13, 1, 4),
    _HwIpfpmDcpDelayTimeRange_Type()
)
hwIpfpmDcpDelayTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpDelayTimeRange.setStatus("current")


class _HwIpfpmDcpDelayTlpRole_Type(HWIpfpmDelayTlpRole):
    """Custom type hwIpfpmDcpDelayTlpRole based on HWIpfpmDelayTlpRole"""


_HwIpfpmDcpDelayTlpRole_Object = MibTableColumn
hwIpfpmDcpDelayTlpRole = _HwIpfpmDcpDelayTlpRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 13, 1, 5),
    _HwIpfpmDcpDelayTlpRole_Type()
)
hwIpfpmDcpDelayTlpRole.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpDelayTlpRole.setStatus("current")


class _HwIpfpmDcpDelayForwardTlpId_Type(Integer32):
    """Custom type hwIpfpmDcpDelayForwardTlpId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HwIpfpmDcpDelayForwardTlpId_Type.__name__ = "Integer32"
_HwIpfpmDcpDelayForwardTlpId_Object = MibTableColumn
hwIpfpmDcpDelayForwardTlpId = _HwIpfpmDcpDelayForwardTlpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 13, 1, 6),
    _HwIpfpmDcpDelayForwardTlpId_Type()
)
hwIpfpmDcpDelayForwardTlpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpDelayForwardTlpId.setStatus("current")


class _HwIpfpmDcpDelayBackwardTlpId_Type(Integer32):
    """Custom type hwIpfpmDcpDelayBackwardTlpId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HwIpfpmDcpDelayBackwardTlpId_Type.__name__ = "Integer32"
_HwIpfpmDcpDelayBackwardTlpId_Object = MibTableColumn
hwIpfpmDcpDelayBackwardTlpId = _HwIpfpmDcpDelayBackwardTlpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 13, 1, 7),
    _HwIpfpmDcpDelayBackwardTlpId_Type()
)
hwIpfpmDcpDelayBackwardTlpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpfpmDcpDelayBackwardTlpId.setStatus("current")
_HwIpfpmDcpTlpTable_Object = MibTable
hwIpfpmDcpTlpTable = _HwIpfpmDcpTlpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 14)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpTable.setStatus("current")
_HwIpfpmDcpTlpEntry_Object = MibTableRow
hwIpfpmDcpTlpEntry = _HwIpfpmDcpTlpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 14, 1)
)
hwIpfpmDcpTlpEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpId"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpEntry.setStatus("current")


class _HwIpfpmDcpTlpId_Type(Integer32):
    """Custom type hwIpfpmDcpTlpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HwIpfpmDcpTlpId_Type.__name__ = "Integer32"
_HwIpfpmDcpTlpId_Object = MibTableColumn
hwIpfpmDcpTlpId = _HwIpfpmDcpTlpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 14, 1, 1),
    _HwIpfpmDcpTlpId_Type()
)
hwIpfpmDcpTlpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpId.setStatus("current")
_HwIpfpmDcpTlpIfIndex_Type = InterfaceIndex
_HwIpfpmDcpTlpIfIndex_Object = MibTableColumn
hwIpfpmDcpTlpIfIndex = _HwIpfpmDcpTlpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 14, 1, 2),
    _HwIpfpmDcpTlpIfIndex_Type()
)
hwIpfpmDcpTlpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpIfIndex.setStatus("current")
_HwIpfpmDcpTlpRowStatus_Type = RowStatus
_HwIpfpmDcpTlpRowStatus_Object = MibTableColumn
hwIpfpmDcpTlpRowStatus = _HwIpfpmDcpTlpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 14, 1, 3),
    _HwIpfpmDcpTlpRowStatus_Type()
)
hwIpfpmDcpTlpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpRowStatus.setStatus("current")


class _HwIpfpmDcpTlpVlanId_Type(Integer32):
    """Custom type hwIpfpmDcpTlpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HwIpfpmDcpTlpVlanId_Type.__name__ = "Integer32"
_HwIpfpmDcpTlpVlanId_Object = MibTableColumn
hwIpfpmDcpTlpVlanId = _HwIpfpmDcpTlpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 14, 1, 4),
    _HwIpfpmDcpTlpVlanId_Type()
)
hwIpfpmDcpTlpVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpVlanId.setStatus("current")
_HwIpfpmDcpTlpQueryTable_Object = MibTable
hwIpfpmDcpTlpQueryTable = _HwIpfpmDcpTlpQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 15)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryTable.setStatus("current")
_HwIpfpmDcpTlpQueryEntry_Object = MibTableRow
hwIpfpmDcpTlpQueryEntry = _HwIpfpmDcpTlpQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 15, 1)
)
hwIpfpmDcpTlpQueryEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpQueryIfIndex"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpQueryVlanId"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryEntry.setStatus("current")
_HwIpfpmDcpTlpQueryIfIndex_Type = InterfaceIndex
_HwIpfpmDcpTlpQueryIfIndex_Object = MibTableColumn
hwIpfpmDcpTlpQueryIfIndex = _HwIpfpmDcpTlpQueryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 15, 1, 1),
    _HwIpfpmDcpTlpQueryIfIndex_Type()
)
hwIpfpmDcpTlpQueryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryIfIndex.setStatus("current")


class _HwIpfpmDcpTlpQueryTlpId_Type(Integer32):
    """Custom type hwIpfpmDcpTlpQueryTlpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HwIpfpmDcpTlpQueryTlpId_Type.__name__ = "Integer32"
_HwIpfpmDcpTlpQueryTlpId_Object = MibTableColumn
hwIpfpmDcpTlpQueryTlpId = _HwIpfpmDcpTlpQueryTlpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 15, 1, 2),
    _HwIpfpmDcpTlpQueryTlpId_Type()
)
hwIpfpmDcpTlpQueryTlpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryTlpId.setStatus("current")


class _HwIpfpmDcpTlpQueryVlanId_Type(Integer32):
    """Custom type hwIpfpmDcpTlpQueryVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HwIpfpmDcpTlpQueryVlanId_Type.__name__ = "Integer32"
_HwIpfpmDcpTlpQueryVlanId_Object = MibTableColumn
hwIpfpmDcpTlpQueryVlanId = _HwIpfpmDcpTlpQueryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 15, 1, 3),
    _HwIpfpmDcpTlpQueryVlanId_Type()
)
hwIpfpmDcpTlpQueryVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryVlanId.setStatus("current")
_HwIpfpmDcpSrcInstReferQueryTable_Object = MibTable
hwIpfpmDcpSrcInstReferQueryTable = _HwIpfpmDcpSrcInstReferQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 16)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpSrcInstReferQueryTable.setStatus("current")
_HwIpfpmDcpSrcInstReferQueryEntry_Object = MibTableRow
hwIpfpmDcpSrcInstReferQueryEntry = _HwIpfpmDcpSrcInstReferQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 16, 1)
)
hwIpfpmDcpSrcInstReferQueryEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstId"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpSrcInstReferQueryEntry.setStatus("current")
_HwIpfpmDcpSrcInstReferCnt_Type = Integer32
_HwIpfpmDcpSrcInstReferCnt_Object = MibTableColumn
hwIpfpmDcpSrcInstReferCnt = _HwIpfpmDcpSrcInstReferCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 16, 1, 1),
    _HwIpfpmDcpSrcInstReferCnt_Type()
)
hwIpfpmDcpSrcInstReferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmDcpSrcInstReferCnt.setStatus("current")
_HwIpfpmDcpTlpQueryExtTable_Object = MibTable
hwIpfpmDcpTlpQueryExtTable = _HwIpfpmDcpTlpQueryExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 17)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryExtTable.setStatus("current")
_HwIpfpmDcpTlpQueryExtEntry_Object = MibTableRow
hwIpfpmDcpTlpQueryExtEntry = _HwIpfpmDcpTlpQueryExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 17, 1)
)
hwIpfpmDcpTlpQueryExtEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpQueryExtIfIndex"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpQueryExtVlanId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpQueryExtOntId"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpQueryExtOntPortType"),
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpQueryExtOntPortId"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryExtEntry.setStatus("current")
_HwIpfpmDcpTlpQueryExtIfIndex_Type = InterfaceIndex
_HwIpfpmDcpTlpQueryExtIfIndex_Object = MibTableColumn
hwIpfpmDcpTlpQueryExtIfIndex = _HwIpfpmDcpTlpQueryExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 17, 1, 1),
    _HwIpfpmDcpTlpQueryExtIfIndex_Type()
)
hwIpfpmDcpTlpQueryExtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryExtIfIndex.setStatus("current")


class _HwIpfpmDcpTlpQueryExtTlpId_Type(Integer32):
    """Custom type hwIpfpmDcpTlpQueryExtTlpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HwIpfpmDcpTlpQueryExtTlpId_Type.__name__ = "Integer32"
_HwIpfpmDcpTlpQueryExtTlpId_Object = MibTableColumn
hwIpfpmDcpTlpQueryExtTlpId = _HwIpfpmDcpTlpQueryExtTlpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 17, 1, 2),
    _HwIpfpmDcpTlpQueryExtTlpId_Type()
)
hwIpfpmDcpTlpQueryExtTlpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryExtTlpId.setStatus("current")


class _HwIpfpmDcpTlpQueryExtVlanId_Type(Integer32):
    """Custom type hwIpfpmDcpTlpQueryExtVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HwIpfpmDcpTlpQueryExtVlanId_Type.__name__ = "Integer32"
_HwIpfpmDcpTlpQueryExtVlanId_Object = MibTableColumn
hwIpfpmDcpTlpQueryExtVlanId = _HwIpfpmDcpTlpQueryExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 17, 1, 3),
    _HwIpfpmDcpTlpQueryExtVlanId_Type()
)
hwIpfpmDcpTlpQueryExtVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryExtVlanId.setStatus("current")
_HwIpfpmDcpTlpQueryExtOntId_Type = Integer32
_HwIpfpmDcpTlpQueryExtOntId_Object = MibTableColumn
hwIpfpmDcpTlpQueryExtOntId = _HwIpfpmDcpTlpQueryExtOntId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 17, 1, 4),
    _HwIpfpmDcpTlpQueryExtOntId_Type()
)
hwIpfpmDcpTlpQueryExtOntId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryExtOntId.setStatus("current")


class _HwIpfpmDcpTlpQueryExtOntPortType_Type(Integer32):
    """Custom type hwIpfpmDcpTlpQueryExtOntPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              47)
        )
    )
    namedValues = NamedValues(
        *(("eth", 47),
          ("invalid", -1))
    )


_HwIpfpmDcpTlpQueryExtOntPortType_Type.__name__ = "Integer32"
_HwIpfpmDcpTlpQueryExtOntPortType_Object = MibTableColumn
hwIpfpmDcpTlpQueryExtOntPortType = _HwIpfpmDcpTlpQueryExtOntPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 17, 1, 5),
    _HwIpfpmDcpTlpQueryExtOntPortType_Type()
)
hwIpfpmDcpTlpQueryExtOntPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryExtOntPortType.setStatus("current")
_HwIpfpmDcpTlpQueryExtOntPortId_Type = Integer32
_HwIpfpmDcpTlpQueryExtOntPortId_Object = MibTableColumn
hwIpfpmDcpTlpQueryExtOntPortId = _HwIpfpmDcpTlpQueryExtOntPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 17, 1, 6),
    _HwIpfpmDcpTlpQueryExtOntPortId_Type()
)
hwIpfpmDcpTlpQueryExtOntPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpQueryExtOntPortId.setStatus("current")
_HwIpfpmDcpTlpExtTable_Object = MibTable
hwIpfpmDcpTlpExtTable = _HwIpfpmDcpTlpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 18)
)
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpExtTable.setStatus("current")
_HwIpfpmDcpTlpExtEntry_Object = MibTableRow
hwIpfpmDcpTlpExtEntry = _HwIpfpmDcpTlpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 18, 1)
)
hwIpfpmDcpTlpExtEntry.setIndexNames(
    (0, "HUAWEI-IPFPM-MIB", "hwIpfpmDcpExtTlpId"),
)
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpExtEntry.setStatus("current")


class _HwIpfpmDcpExtTlpId_Type(Integer32):
    """Custom type hwIpfpmDcpExtTlpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HwIpfpmDcpExtTlpId_Type.__name__ = "Integer32"
_HwIpfpmDcpExtTlpId_Object = MibTableColumn
hwIpfpmDcpExtTlpId = _HwIpfpmDcpExtTlpId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 18, 1, 1),
    _HwIpfpmDcpExtTlpId_Type()
)
hwIpfpmDcpExtTlpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpfpmDcpExtTlpId.setStatus("current")
_HwIpfpmDcpTlpExtIfIndex_Type = Integer32
_HwIpfpmDcpTlpExtIfIndex_Object = MibTableColumn
hwIpfpmDcpTlpExtIfIndex = _HwIpfpmDcpTlpExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 18, 1, 2),
    _HwIpfpmDcpTlpExtIfIndex_Type()
)
hwIpfpmDcpTlpExtIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpExtIfIndex.setStatus("current")
_HwIpfpmDcpTlpExtRowStatus_Type = RowStatus
_HwIpfpmDcpTlpExtRowStatus_Object = MibTableColumn
hwIpfpmDcpTlpExtRowStatus = _HwIpfpmDcpTlpExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 18, 1, 3),
    _HwIpfpmDcpTlpExtRowStatus_Type()
)
hwIpfpmDcpTlpExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpExtRowStatus.setStatus("current")


class _HwIpfpmDcpTlpExtVlanId_Type(Integer32):
    """Custom type hwIpfpmDcpTlpExtVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HwIpfpmDcpTlpExtVlanId_Type.__name__ = "Integer32"
_HwIpfpmDcpTlpExtVlanId_Object = MibTableColumn
hwIpfpmDcpTlpExtVlanId = _HwIpfpmDcpTlpExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 18, 1, 4),
    _HwIpfpmDcpTlpExtVlanId_Type()
)
hwIpfpmDcpTlpExtVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpExtVlanId.setStatus("current")
_HwIpfpmDcpTlpExtOntId_Type = Integer32
_HwIpfpmDcpTlpExtOntId_Object = MibTableColumn
hwIpfpmDcpTlpExtOntId = _HwIpfpmDcpTlpExtOntId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 18, 1, 5),
    _HwIpfpmDcpTlpExtOntId_Type()
)
hwIpfpmDcpTlpExtOntId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpExtOntId.setStatus("current")


class _HwIpfpmDcpTlpExtOntPortType_Type(Integer32):
    """Custom type hwIpfpmDcpTlpExtOntPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              47)
        )
    )
    namedValues = NamedValues(
        *(("eth", 47),
          ("invalid", -1))
    )


_HwIpfpmDcpTlpExtOntPortType_Type.__name__ = "Integer32"
_HwIpfpmDcpTlpExtOntPortType_Object = MibTableColumn
hwIpfpmDcpTlpExtOntPortType = _HwIpfpmDcpTlpExtOntPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 18, 1, 6),
    _HwIpfpmDcpTlpExtOntPortType_Type()
)
hwIpfpmDcpTlpExtOntPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpExtOntPortType.setStatus("current")
_HwIpfpmDcpTlpExtOntPortId_Type = Integer32
_HwIpfpmDcpTlpExtOntPortId_Object = MibTableColumn
hwIpfpmDcpTlpExtOntPortId = _HwIpfpmDcpTlpExtOntPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 1, 18, 1, 7),
    _HwIpfpmDcpTlpExtOntPortId_Type()
)
hwIpfpmDcpTlpExtOntPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpExtOntPortId.setStatus("current")
_HwIpfpmDcpTrapObjects_ObjectIdentity = ObjectIdentity
hwIpfpmDcpTrapObjects = _HwIpfpmDcpTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 2)
)
_HwIpfpmTlpExceedBoardId_Type = Integer32
_HwIpfpmTlpExceedBoardId_Object = MibScalar
hwIpfpmTlpExceedBoardId = _HwIpfpmTlpExceedBoardId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 2, 1),
    _HwIpfpmTlpExceedBoardId_Type()
)
hwIpfpmTlpExceedBoardId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpfpmTlpExceedBoardId.setStatus("current")
_HwIpfpmTlpNumber_Type = Integer32
_HwIpfpmTlpNumber_Object = MibScalar
hwIpfpmTlpNumber = _HwIpfpmTlpNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 2, 2),
    _HwIpfpmTlpNumber_Type()
)
hwIpfpmTlpNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpfpmTlpNumber.setStatus("current")
_HwIpfpmTlpThreshold_Type = Integer32
_HwIpfpmTlpThreshold_Object = MibScalar
hwIpfpmTlpThreshold = _HwIpfpmTlpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 2, 2, 3),
    _HwIpfpmTlpThreshold_Type()
)
hwIpfpmTlpThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpfpmTlpThreshold.setStatus("current")
_HwIpfpmTraps_ObjectIdentity = ObjectIdentity
hwIpfpmTraps = _HwIpfpmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 3)
)
_HwIpfpmConformance_ObjectIdentity = ObjectIdentity
hwIpfpmConformance = _HwIpfpmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4)
)
_HwIpfpmCompliances_ObjectIdentity = ObjectIdentity
hwIpfpmCompliances = _HwIpfpmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4, 1)
)
_HwIpfpmGroups_ObjectIdentity = ObjectIdentity
hwIpfpmGroups = _HwIpfpmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4, 2)
)

# Managed Objects groups

hwIpfpmMcpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4, 2, 1)
)
hwIpfpmMcpConfigGroup.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmMcpEnable"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpUdpPort"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpAuthType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpAuthKey"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpAuthRowStatus"))
)
if mibBuilder.loadTexts:
    hwIpfpmMcpConfigGroup.setStatus("current")

hwIpfpmMcpInstConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4, 2, 2)
)
hwIpfpmMcpInstConfigGroup.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstDesc"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpLossRatioUpThres"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpLossRatioLowThres"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpOneDelayUpThres"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpOneDelayLowThres"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpTwoDelayUpThres"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpTwoDelayLowThres"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpMeasureEnable"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstRowStatus"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpSourceInstId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpDcpRowStatus"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpFlowType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpAchRowStatus"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpTlpRowStatus"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpSrcInstReferCnt"))
)
if mibBuilder.loadTexts:
    hwIpfpmMcpInstConfigGroup.setStatus("current")

hwIpfpmMcpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4, 2, 3)
)
hwIpfpmMcpStatsGroup.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstSpec"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstCurNum"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpSeqNo"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpLossErrInfo"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardLossPkts"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardLossPktsSign"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardLossBytes"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardLossBytesSign"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardPkts"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardBytes"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardLossRatio"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardLossPkts"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardLossPktsSign"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardLossBytes"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardLossBytesSign"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardPkts"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardBytes"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardLossRatio"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardLossMMSType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardLossMMSSwitch"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpOneDelayErrInfo"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardOneDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardOneDelayVariation"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardOneDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardOneDelayVariation"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardOneDelayMMSType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpTwoDelayErrInfo"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpTwoDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpTwoDelayVariation"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardDelayVariation"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardDelayVariation"))
)
if mibBuilder.loadTexts:
    hwIpfpmMcpStatsGroup.setStatus("current")

hwIpfpmDcpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4, 2, 4)
)
hwIpfpmDcpConfigGroup.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmDcpEnable"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpMeasureColorFlag"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpMcpId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpMcpPort"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpMcpVpnName"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpMcpVpnType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpAuthType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpAuthKey"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpAuthRowStatus"))
)
if mibBuilder.loadTexts:
    hwIpfpmDcpConfigGroup.setStatus("current")

hwIpfpmDcpInstConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4, 2, 5)
)
hwIpfpmDcpInstConfigGroup.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstDesc"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstMcpId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstMcpPort"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstInterval"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstAuthType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstAuthKey"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstAuthRowStatus"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstRowStatus"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpSourceInstId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstMcpVpnName"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstMcpVpnType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstGroupId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowProtocol"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowDscp"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowSrcAddr"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowSrcMaskLen"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowDstAddr"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowDstMaskLen"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowSrcPortBgn"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowSrcPortEnd"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowDstPortBgn"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowDstPortEnd"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowRowStatus"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowOuterSrcAddr"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowOuterDstAddr"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowForwardGtpTeid"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowBackwardGtpTeid"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpRole"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpFlowType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpDirec"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpVpnLabel"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpCtrlWordFlag"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpLspLabel"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpL2VpnFlag"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpTpId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpRowStatus"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpMultiSrcType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpFlowLabelFlag"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpLspLabel2"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpLspLabel3"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpOuterVlan"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpInnerVlan"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpBackwardVpnLabel"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpBackwardCtrlWordFlag"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpBackwardLspLabel"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpBackwardLspLabel2"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpBackwardLspLabel3"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpBackwardL2VpnFlag"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpBackwardFlowLabelFlag"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpBackwardOuterVlan"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpBackwardInnerVlan"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstTlpBackwardTpId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpLossEnable"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpLossContEnable"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpLossTimeRange"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpDelayEnable"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpDelayContEnable"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpDelayMeasType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpDelayTimeRange"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpDelayForwardTlpId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpDelayBackwardTlpId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpSrcInstReferCnt"))
)
if mibBuilder.loadTexts:
    hwIpfpmDcpInstConfigGroup.setStatus("current")

hwIpfpmDcpTlpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4, 2, 6)
)
hwIpfpmDcpTlpConfigGroup.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpIfIndex"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpRowStatus"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpVlanId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpTlpQueryTlpId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTlpExceedBoardId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTlpNumber"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTlpThreshold"))
)
if mibBuilder.loadTexts:
    hwIpfpmDcpTlpConfigGroup.setStatus("current")


# Notification objects

hwIpfpmLossRatioExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 3, 1)
)
hwIpfpmLossRatioExceed.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmMcpFlowType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardLossRatio"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardLossRatio"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstDesc"))
)
if mibBuilder.loadTexts:
    hwIpfpmLossRatioExceed.setStatus(
        "current"
    )

hwIpfpmLossRatioRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 3, 2)
)
hwIpfpmLossRatioRecovery.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmMcpFlowType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardLossRatio"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardLossRatio"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstDesc"))
)
if mibBuilder.loadTexts:
    hwIpfpmLossRatioRecovery.setStatus(
        "current"
    )

hwIpfpmOneDelayExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 3, 3)
)
hwIpfpmOneDelayExceed.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmMcpFlowType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardOneDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardOneDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstDesc"))
)
if mibBuilder.loadTexts:
    hwIpfpmOneDelayExceed.setStatus(
        "current"
    )

hwIpfpmOneDelayRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 3, 4)
)
hwIpfpmOneDelayRecovery.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmMcpFlowType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpForwardOneDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpBackwardOneDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstDesc"))
)
if mibBuilder.loadTexts:
    hwIpfpmOneDelayRecovery.setStatus(
        "current"
    )

hwIpfpmTwoDelayExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 3, 5)
)
hwIpfpmTwoDelayExceed.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmMcpTwoDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstDesc"))
)
if mibBuilder.loadTexts:
    hwIpfpmTwoDelayExceed.setStatus(
        "current"
    )

hwIpfpmTwoDelayRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 3, 6)
)
hwIpfpmTwoDelayRecovery.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmMcpTwoDelay"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmMcpInstDesc"))
)
if mibBuilder.loadTexts:
    hwIpfpmTwoDelayRecovery.setStatus(
        "current"
    )

hwIpfpmDcpFlowConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 3, 7)
)
hwIpfpmDcpFlowConflict.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowType"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpInstId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowType"))
)
if mibBuilder.loadTexts:
    hwIpfpmDcpFlowConflict.setStatus(
        "current"
    )

hwIpfpmTlpExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 3, 8)
)
hwIpfpmTlpExceed.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmTlpExceedBoardId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTlpNumber"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTlpThreshold"))
)
if mibBuilder.loadTexts:
    hwIpfpmTlpExceed.setStatus(
        "current"
    )

hwIpfpmTlpRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 3, 9)
)
hwIpfpmTlpRecovery.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmTlpExceedBoardId"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTlpNumber"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTlpThreshold"))
)
if mibBuilder.loadTexts:
    hwIpfpmTlpRecovery.setStatus(
        "current"
    )


# Notifications groups

hwIpfpmTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4, 2, 7)
)
hwIpfpmTrapsGroup.setObjects(
      *(("HUAWEI-IPFPM-MIB", "hwIpfpmLossRatioExceed"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmLossRatioRecovery"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmOneDelayExceed"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmOneDelayRecovery"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTwoDelayExceed"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTwoDelayRecovery"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmDcpFlowConflict"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTlpExceed"),
        ("HUAWEI-IPFPM-MIB", "hwIpfpmTlpRecovery"))
)
if mibBuilder.loadTexts:
    hwIpfpmTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIpfpmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 316, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwIpfpmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-IPFPM-MIB",
    **{"HWEnabledStatus": HWEnabledStatus,
       "HWIpfpmStatErrInfo": HWIpfpmStatErrInfo,
       "HWIpfpmMeasureFlag": HWIpfpmMeasureFlag,
       "HWIpfpmFlowType": HWIpfpmFlowType,
       "HWIpfpmMcpFlowType": HWIpfpmMcpFlowType,
       "HWIpfpmFlowTlpDirec": HWIpfpmFlowTlpDirec,
       "HWIpfpmTlpRole": HWIpfpmTlpRole,
       "HWIpfpmDelayTlpRole": HWIpfpmDelayTlpRole,
       "HWIpfpmLossTlpRole": HWIpfpmLossTlpRole,
       "HWIpfpmMcpTlpRole": HWIpfpmMcpTlpRole,
       "HWIpfpmAuthType": HWIpfpmAuthType,
       "HWIpfpmDelayMeasType": HWIpfpmDelayMeasType,
       "HWIpfpmMeasTimeRangeType": HWIpfpmMeasTimeRangeType,
       "HWIpfpmInstIntervalType": HWIpfpmInstIntervalType,
       "HWIpfpmInstType": HWIpfpmInstType,
       "HWIpfpmMMSType": HWIpfpmMMSType,
       "HWIpfpmVpnType": HWIpfpmVpnType,
       "hwIpfpmMib": hwIpfpmMib,
       "hwIpfpmMcpObjects": hwIpfpmMcpObjects,
       "hwIpfpmMcpConfiguration": hwIpfpmMcpConfiguration,
       "hwIpfpmMcpGlobalTable": hwIpfpmMcpGlobalTable,
       "hwIpfpmMcpEnable": hwIpfpmMcpEnable,
       "hwIpfpmMcpId": hwIpfpmMcpId,
       "hwIpfpmMcpUdpPort": hwIpfpmMcpUdpPort,
       "hwIpfpmMcpAuthTable": hwIpfpmMcpAuthTable,
       "hwIpfpmMcpAuthEntry": hwIpfpmMcpAuthEntry,
       "hwIpfpmMcpAuthKeyId": hwIpfpmMcpAuthKeyId,
       "hwIpfpmMcpAuthType": hwIpfpmMcpAuthType,
       "hwIpfpmMcpAuthKey": hwIpfpmMcpAuthKey,
       "hwIpfpmMcpAuthRowStatus": hwIpfpmMcpAuthRowStatus,
       "hwIpfpmMcpInstTable": hwIpfpmMcpInstTable,
       "hwIpfpmMcpInstEntry": hwIpfpmMcpInstEntry,
       "hwIpfpmMcpInstId": hwIpfpmMcpInstId,
       "hwIpfpmMcpInstDesc": hwIpfpmMcpInstDesc,
       "hwIpfpmMcpLossRatioUpThres": hwIpfpmMcpLossRatioUpThres,
       "hwIpfpmMcpLossRatioLowThres": hwIpfpmMcpLossRatioLowThres,
       "hwIpfpmMcpOneDelayUpThres": hwIpfpmMcpOneDelayUpThres,
       "hwIpfpmMcpOneDelayLowThres": hwIpfpmMcpOneDelayLowThres,
       "hwIpfpmMcpTwoDelayUpThres": hwIpfpmMcpTwoDelayUpThres,
       "hwIpfpmMcpTwoDelayLowThres": hwIpfpmMcpTwoDelayLowThres,
       "hwIpfpmMcpMeasureEnable": hwIpfpmMcpMeasureEnable,
       "hwIpfpmMcpInstRowStatus": hwIpfpmMcpInstRowStatus,
       "hwIpfpmMcpInstType": hwIpfpmMcpInstType,
       "hwIpfpmMcpSourceInstId": hwIpfpmMcpSourceInstId,
       "hwIpfpmMcpDcpTable": hwIpfpmMcpDcpTable,
       "hwIpfpmMcpDcpEntry": hwIpfpmMcpDcpEntry,
       "hwIpfpmMcpDcpId": hwIpfpmMcpDcpId,
       "hwIpfpmMcpDcpRowStatus": hwIpfpmMcpDcpRowStatus,
       "hwIpfpmMcpAchTable": hwIpfpmMcpAchTable,
       "hwIpfpmMcpAchEntry": hwIpfpmMcpAchEntry,
       "hwIpfpmMcpAchId": hwIpfpmMcpAchId,
       "hwIpfpmMcpFlowType": hwIpfpmMcpFlowType,
       "hwIpfpmMcpAchRowStatus": hwIpfpmMcpAchRowStatus,
       "hwIpfpmMcpTlpTable": hwIpfpmMcpTlpTable,
       "hwIpfpmMcpTlpEntry": hwIpfpmMcpTlpEntry,
       "hwIpfpmMcpTlpRole": hwIpfpmMcpTlpRole,
       "hwIpfpmMcpTlpDcpId": hwIpfpmMcpTlpDcpId,
       "hwIpfpmMcpTlpId": hwIpfpmMcpTlpId,
       "hwIpfpmMcpTlpRowStatus": hwIpfpmMcpTlpRowStatus,
       "hwIpfpmMcpSrcInstReferQueryTable": hwIpfpmMcpSrcInstReferQueryTable,
       "hwIpfpmMcpSrcInstReferQueryEntry": hwIpfpmMcpSrcInstReferQueryEntry,
       "hwIpfpmMcpSrcInstReferCnt": hwIpfpmMcpSrcInstReferCnt,
       "hwIpfpmMcpStatistics": hwIpfpmMcpStatistics,
       "hwIpfpmMcpStatisticsTable": hwIpfpmMcpStatisticsTable,
       "hwIpfpmMcpInstSpec": hwIpfpmMcpInstSpec,
       "hwIpfpmMcpInstCurNum": hwIpfpmMcpInstCurNum,
       "hwIpfpmMcpInstAchIndexTable": hwIpfpmMcpInstAchIndexTable,
       "hwIpfpmMcpInstAchIndexEntry": hwIpfpmMcpInstAchIndexEntry,
       "hwIpfpmMcpSeqNo": hwIpfpmMcpSeqNo,
       "hwIpfpmMcpLossStatsTable": hwIpfpmMcpLossStatsTable,
       "hwIpfpmMcpLossStatsEntry": hwIpfpmMcpLossStatsEntry,
       "hwIpfpmMcpSeqNoHigh": hwIpfpmMcpSeqNoHigh,
       "hwIpfpmMcpSeqNoLow": hwIpfpmMcpSeqNoLow,
       "hwIpfpmMcpLossErrInfo": hwIpfpmMcpLossErrInfo,
       "hwIpfpmMcpForwardLossPkts": hwIpfpmMcpForwardLossPkts,
       "hwIpfpmMcpForwardLossPktsSign": hwIpfpmMcpForwardLossPktsSign,
       "hwIpfpmMcpForwardLossBytes": hwIpfpmMcpForwardLossBytes,
       "hwIpfpmMcpForwardLossBytesSign": hwIpfpmMcpForwardLossBytesSign,
       "hwIpfpmMcpForwardPkts": hwIpfpmMcpForwardPkts,
       "hwIpfpmMcpForwardBytes": hwIpfpmMcpForwardBytes,
       "hwIpfpmMcpForwardLossRatio": hwIpfpmMcpForwardLossRatio,
       "hwIpfpmMcpBackwardLossPkts": hwIpfpmMcpBackwardLossPkts,
       "hwIpfpmMcpBackwardLossPktsSign": hwIpfpmMcpBackwardLossPktsSign,
       "hwIpfpmMcpBackwardLossBytes": hwIpfpmMcpBackwardLossBytes,
       "hwIpfpmMcpBackwardLossBytesSign": hwIpfpmMcpBackwardLossBytesSign,
       "hwIpfpmMcpBackwardPkts": hwIpfpmMcpBackwardPkts,
       "hwIpfpmMcpBackwardBytes": hwIpfpmMcpBackwardBytes,
       "hwIpfpmMcpBackwardLossRatio": hwIpfpmMcpBackwardLossRatio,
       "hwIpfpmMcpForwardLossMMSType": hwIpfpmMcpForwardLossMMSType,
       "hwIpfpmMcpForwardLossMMSSwitch": hwIpfpmMcpForwardLossMMSSwitch,
       "hwIpfpmMcpOneDelayStatTable": hwIpfpmMcpOneDelayStatTable,
       "hwIpfpmMcpOneDelayStatEntry": hwIpfpmMcpOneDelayStatEntry,
       "hwIpfpmMcpOneDelayErrInfo": hwIpfpmMcpOneDelayErrInfo,
       "hwIpfpmMcpForwardOneDelay": hwIpfpmMcpForwardOneDelay,
       "hwIpfpmMcpForwardOneDelayVariation": hwIpfpmMcpForwardOneDelayVariation,
       "hwIpfpmMcpBackwardOneDelay": hwIpfpmMcpBackwardOneDelay,
       "hwIpfpmMcpBackwardOneDelayVariation": hwIpfpmMcpBackwardOneDelayVariation,
       "hwIpfpmMcpForwardOneDelayMMSType": hwIpfpmMcpForwardOneDelayMMSType,
       "hwIpfpmMcpTwoDelayStatTable": hwIpfpmMcpTwoDelayStatTable,
       "hwIpfpmMcpTwoDelayStatEntry": hwIpfpmMcpTwoDelayStatEntry,
       "hwIpfpmMcpTwoDelayErrInfo": hwIpfpmMcpTwoDelayErrInfo,
       "hwIpfpmMcpTwoDelay": hwIpfpmMcpTwoDelay,
       "hwIpfpmMcpTwoDelayVariation": hwIpfpmMcpTwoDelayVariation,
       "hwIpfpmMcpForwardDelay": hwIpfpmMcpForwardDelay,
       "hwIpfpmMcpForwardDelayVariation": hwIpfpmMcpForwardDelayVariation,
       "hwIpfpmMcpBackwardDelay": hwIpfpmMcpBackwardDelay,
       "hwIpfpmMcpBackwardDelayVariation": hwIpfpmMcpBackwardDelayVariation,
       "hwIpfpmDcpObjects": hwIpfpmDcpObjects,
       "hwIpfpmDcpConfiguration": hwIpfpmDcpConfiguration,
       "hwIpfpmDcpGlobalTable": hwIpfpmDcpGlobalTable,
       "hwIpfpmDcpEnable": hwIpfpmDcpEnable,
       "hwIpfpmDcpId": hwIpfpmDcpId,
       "hwIpfpmDcpMeasureColorFlag": hwIpfpmDcpMeasureColorFlag,
       "hwIpfpmDcpMcpId": hwIpfpmDcpMcpId,
       "hwIpfpmDcpMcpPort": hwIpfpmDcpMcpPort,
       "hwIpfpmDcpMcpVpnName": hwIpfpmDcpMcpVpnName,
       "hwIpfpmDcpMcpVpnType": hwIpfpmDcpMcpVpnType,
       "hwIpfpmDcpAuthTable": hwIpfpmDcpAuthTable,
       "hwIpfpmDcpAuthEntry": hwIpfpmDcpAuthEntry,
       "hwIpfpmDcpAuthKeyId": hwIpfpmDcpAuthKeyId,
       "hwIpfpmDcpAuthType": hwIpfpmDcpAuthType,
       "hwIpfpmDcpAuthKey": hwIpfpmDcpAuthKey,
       "hwIpfpmDcpAuthRowStatus": hwIpfpmDcpAuthRowStatus,
       "hwIpfpmDcpInstTable": hwIpfpmDcpInstTable,
       "hwIpfpmDcpInstEntry": hwIpfpmDcpInstEntry,
       "hwIpfpmDcpInstId": hwIpfpmDcpInstId,
       "hwIpfpmDcpInstDesc": hwIpfpmDcpInstDesc,
       "hwIpfpmDcpInstMcpId": hwIpfpmDcpInstMcpId,
       "hwIpfpmDcpInstMcpPort": hwIpfpmDcpInstMcpPort,
       "hwIpfpmDcpInstInterval": hwIpfpmDcpInstInterval,
       "hwIpfpmDcpInstRowStatus": hwIpfpmDcpInstRowStatus,
       "hwIpfpmDcpInstType": hwIpfpmDcpInstType,
       "hwIpfpmDcpSourceInstId": hwIpfpmDcpSourceInstId,
       "hwIpfpmDcpInstMcpVpnName": hwIpfpmDcpInstMcpVpnName,
       "hwIpfpmDcpInstMcpVpnType": hwIpfpmDcpInstMcpVpnType,
       "hwIpfpmDcpInstGroupId": hwIpfpmDcpInstGroupId,
       "hwIpfpmDcpInstAuthTable": hwIpfpmDcpInstAuthTable,
       "hwIpfpmDcpInstAuthEntry": hwIpfpmDcpInstAuthEntry,
       "hwIpfpmDcpInstAuthKeyId": hwIpfpmDcpInstAuthKeyId,
       "hwIpfpmDcpInstAuthType": hwIpfpmDcpInstAuthType,
       "hwIpfpmDcpInstAuthKey": hwIpfpmDcpInstAuthKey,
       "hwIpfpmDcpInstAuthRowStatus": hwIpfpmDcpInstAuthRowStatus,
       "hwIpfpmDcpFlowTable": hwIpfpmDcpFlowTable,
       "hwIpfpmDcpFlowEntry": hwIpfpmDcpFlowEntry,
       "hwIpfpmDcpFlowType": hwIpfpmDcpFlowType,
       "hwIpfpmDcpFlowProtocol": hwIpfpmDcpFlowProtocol,
       "hwIpfpmDcpFlowDscp": hwIpfpmDcpFlowDscp,
       "hwIpfpmDcpFlowSrcAddr": hwIpfpmDcpFlowSrcAddr,
       "hwIpfpmDcpFlowSrcMaskLen": hwIpfpmDcpFlowSrcMaskLen,
       "hwIpfpmDcpFlowDstAddr": hwIpfpmDcpFlowDstAddr,
       "hwIpfpmDcpFlowDstMaskLen": hwIpfpmDcpFlowDstMaskLen,
       "hwIpfpmDcpFlowSrcPortBgn": hwIpfpmDcpFlowSrcPortBgn,
       "hwIpfpmDcpFlowSrcPortEnd": hwIpfpmDcpFlowSrcPortEnd,
       "hwIpfpmDcpFlowDstPortBgn": hwIpfpmDcpFlowDstPortBgn,
       "hwIpfpmDcpFlowDstPortEnd": hwIpfpmDcpFlowDstPortEnd,
       "hwIpfpmDcpFlowRowStatus": hwIpfpmDcpFlowRowStatus,
       "hwIpfpmDcpFlowOuterSrcAddr": hwIpfpmDcpFlowOuterSrcAddr,
       "hwIpfpmDcpFlowOuterDstAddr": hwIpfpmDcpFlowOuterDstAddr,
       "hwIpfpmDcpFlowForwardGtpTeid": hwIpfpmDcpFlowForwardGtpTeid,
       "hwIpfpmDcpFlowBackwardGtpTeid": hwIpfpmDcpFlowBackwardGtpTeid,
       "hwIpfpmDcpInstTlpTable": hwIpfpmDcpInstTlpTable,
       "hwIpfpmDcpInstTlpEntry": hwIpfpmDcpInstTlpEntry,
       "hwIpfpmDcpInstTlpRole": hwIpfpmDcpInstTlpRole,
       "hwIpfpmDcpInstTlpFlowType": hwIpfpmDcpInstTlpFlowType,
       "hwIpfpmDcpInstTlpDirec": hwIpfpmDcpInstTlpDirec,
       "hwIpfpmDcpInstTlpVpnLabel": hwIpfpmDcpInstTlpVpnLabel,
       "hwIpfpmDcpInstTlpCtrlWordFlag": hwIpfpmDcpInstTlpCtrlWordFlag,
       "hwIpfpmDcpInstTlpLspLabel": hwIpfpmDcpInstTlpLspLabel,
       "hwIpfpmDcpInstTlpL2VpnFlag": hwIpfpmDcpInstTlpL2VpnFlag,
       "hwIpfpmDcpInstTlpTpId": hwIpfpmDcpInstTlpTpId,
       "hwIpfpmDcpInstTlpRowStatus": hwIpfpmDcpInstTlpRowStatus,
       "hwIpfpmDcpInstTlpMultiSrcType": hwIpfpmDcpInstTlpMultiSrcType,
       "hwIpfpmDcpInstTlpFlowLabelFlag": hwIpfpmDcpInstTlpFlowLabelFlag,
       "hwIpfpmDcpInstTlpLspLabel2": hwIpfpmDcpInstTlpLspLabel2,
       "hwIpfpmDcpInstTlpLspLabel3": hwIpfpmDcpInstTlpLspLabel3,
       "hwIpfpmDcpInstTlpOuterVlan": hwIpfpmDcpInstTlpOuterVlan,
       "hwIpfpmDcpInstTlpInnerVlan": hwIpfpmDcpInstTlpInnerVlan,
       "hwIpfpmDcpInstTlpBackwardVpnLabel": hwIpfpmDcpInstTlpBackwardVpnLabel,
       "hwIpfpmDcpInstTlpBackwardCtrlWordFlag": hwIpfpmDcpInstTlpBackwardCtrlWordFlag,
       "hwIpfpmDcpInstTlpBackwardLspLabel": hwIpfpmDcpInstTlpBackwardLspLabel,
       "hwIpfpmDcpInstTlpBackwardLspLabel2": hwIpfpmDcpInstTlpBackwardLspLabel2,
       "hwIpfpmDcpInstTlpBackwardLspLabel3": hwIpfpmDcpInstTlpBackwardLspLabel3,
       "hwIpfpmDcpInstTlpBackwardL2VpnFlag": hwIpfpmDcpInstTlpBackwardL2VpnFlag,
       "hwIpfpmDcpInstTlpBackwardFlowLabelFlag": hwIpfpmDcpInstTlpBackwardFlowLabelFlag,
       "hwIpfpmDcpInstTlpBackwardOuterVlan": hwIpfpmDcpInstTlpBackwardOuterVlan,
       "hwIpfpmDcpInstTlpBackwardInnerVlan": hwIpfpmDcpInstTlpBackwardInnerVlan,
       "hwIpfpmDcpInstTlpBackwardTpId": hwIpfpmDcpInstTlpBackwardTpId,
       "hwIpfpmDcpLossMeasTable": hwIpfpmDcpLossMeasTable,
       "hwIpfpmDcpLossMeasEntry": hwIpfpmDcpLossMeasEntry,
       "hwIpfpmDcpLossEnable": hwIpfpmDcpLossEnable,
       "hwIpfpmDcpLossContEnable": hwIpfpmDcpLossContEnable,
       "hwIpfpmDcpLossTimeRange": hwIpfpmDcpLossTimeRange,
       "hwIpfpmDcpLossTlpRole": hwIpfpmDcpLossTlpRole,
       "hwIpfpmDcpDelayMeasTable": hwIpfpmDcpDelayMeasTable,
       "hwIpfpmDcpDelayMeasEntry": hwIpfpmDcpDelayMeasEntry,
       "hwIpfpmDcpDelayEnable": hwIpfpmDcpDelayEnable,
       "hwIpfpmDcpDelayContEnable": hwIpfpmDcpDelayContEnable,
       "hwIpfpmDcpDelayMeasType": hwIpfpmDcpDelayMeasType,
       "hwIpfpmDcpDelayTimeRange": hwIpfpmDcpDelayTimeRange,
       "hwIpfpmDcpDelayTlpRole": hwIpfpmDcpDelayTlpRole,
       "hwIpfpmDcpDelayForwardTlpId": hwIpfpmDcpDelayForwardTlpId,
       "hwIpfpmDcpDelayBackwardTlpId": hwIpfpmDcpDelayBackwardTlpId,
       "hwIpfpmDcpTlpTable": hwIpfpmDcpTlpTable,
       "hwIpfpmDcpTlpEntry": hwIpfpmDcpTlpEntry,
       "hwIpfpmDcpTlpId": hwIpfpmDcpTlpId,
       "hwIpfpmDcpTlpIfIndex": hwIpfpmDcpTlpIfIndex,
       "hwIpfpmDcpTlpRowStatus": hwIpfpmDcpTlpRowStatus,
       "hwIpfpmDcpTlpVlanId": hwIpfpmDcpTlpVlanId,
       "hwIpfpmDcpTlpQueryTable": hwIpfpmDcpTlpQueryTable,
       "hwIpfpmDcpTlpQueryEntry": hwIpfpmDcpTlpQueryEntry,
       "hwIpfpmDcpTlpQueryIfIndex": hwIpfpmDcpTlpQueryIfIndex,
       "hwIpfpmDcpTlpQueryTlpId": hwIpfpmDcpTlpQueryTlpId,
       "hwIpfpmDcpTlpQueryVlanId": hwIpfpmDcpTlpQueryVlanId,
       "hwIpfpmDcpSrcInstReferQueryTable": hwIpfpmDcpSrcInstReferQueryTable,
       "hwIpfpmDcpSrcInstReferQueryEntry": hwIpfpmDcpSrcInstReferQueryEntry,
       "hwIpfpmDcpSrcInstReferCnt": hwIpfpmDcpSrcInstReferCnt,
       "hwIpfpmDcpTlpQueryExtTable": hwIpfpmDcpTlpQueryExtTable,
       "hwIpfpmDcpTlpQueryExtEntry": hwIpfpmDcpTlpQueryExtEntry,
       "hwIpfpmDcpTlpQueryExtIfIndex": hwIpfpmDcpTlpQueryExtIfIndex,
       "hwIpfpmDcpTlpQueryExtTlpId": hwIpfpmDcpTlpQueryExtTlpId,
       "hwIpfpmDcpTlpQueryExtVlanId": hwIpfpmDcpTlpQueryExtVlanId,
       "hwIpfpmDcpTlpQueryExtOntId": hwIpfpmDcpTlpQueryExtOntId,
       "hwIpfpmDcpTlpQueryExtOntPortType": hwIpfpmDcpTlpQueryExtOntPortType,
       "hwIpfpmDcpTlpQueryExtOntPortId": hwIpfpmDcpTlpQueryExtOntPortId,
       "hwIpfpmDcpTlpExtTable": hwIpfpmDcpTlpExtTable,
       "hwIpfpmDcpTlpExtEntry": hwIpfpmDcpTlpExtEntry,
       "hwIpfpmDcpExtTlpId": hwIpfpmDcpExtTlpId,
       "hwIpfpmDcpTlpExtIfIndex": hwIpfpmDcpTlpExtIfIndex,
       "hwIpfpmDcpTlpExtRowStatus": hwIpfpmDcpTlpExtRowStatus,
       "hwIpfpmDcpTlpExtVlanId": hwIpfpmDcpTlpExtVlanId,
       "hwIpfpmDcpTlpExtOntId": hwIpfpmDcpTlpExtOntId,
       "hwIpfpmDcpTlpExtOntPortType": hwIpfpmDcpTlpExtOntPortType,
       "hwIpfpmDcpTlpExtOntPortId": hwIpfpmDcpTlpExtOntPortId,
       "hwIpfpmDcpTrapObjects": hwIpfpmDcpTrapObjects,
       "hwIpfpmTlpExceedBoardId": hwIpfpmTlpExceedBoardId,
       "hwIpfpmTlpNumber": hwIpfpmTlpNumber,
       "hwIpfpmTlpThreshold": hwIpfpmTlpThreshold,
       "hwIpfpmTraps": hwIpfpmTraps,
       "hwIpfpmLossRatioExceed": hwIpfpmLossRatioExceed,
       "hwIpfpmLossRatioRecovery": hwIpfpmLossRatioRecovery,
       "hwIpfpmOneDelayExceed": hwIpfpmOneDelayExceed,
       "hwIpfpmOneDelayRecovery": hwIpfpmOneDelayRecovery,
       "hwIpfpmTwoDelayExceed": hwIpfpmTwoDelayExceed,
       "hwIpfpmTwoDelayRecovery": hwIpfpmTwoDelayRecovery,
       "hwIpfpmDcpFlowConflict": hwIpfpmDcpFlowConflict,
       "hwIpfpmTlpExceed": hwIpfpmTlpExceed,
       "hwIpfpmTlpRecovery": hwIpfpmTlpRecovery,
       "hwIpfpmConformance": hwIpfpmConformance,
       "hwIpfpmCompliances": hwIpfpmCompliances,
       "hwIpfpmCompliance": hwIpfpmCompliance,
       "hwIpfpmGroups": hwIpfpmGroups,
       "hwIpfpmMcpConfigGroup": hwIpfpmMcpConfigGroup,
       "hwIpfpmMcpInstConfigGroup": hwIpfpmMcpInstConfigGroup,
       "hwIpfpmMcpStatsGroup": hwIpfpmMcpStatsGroup,
       "hwIpfpmDcpConfigGroup": hwIpfpmDcpConfigGroup,
       "hwIpfpmDcpInstConfigGroup": hwIpfpmDcpInstConfigGroup,
       "hwIpfpmDcpTlpConfigGroup": hwIpfpmDcpTlpConfigGroup,
       "hwIpfpmTrapsGroup": hwIpfpmTrapsGroup}
)
