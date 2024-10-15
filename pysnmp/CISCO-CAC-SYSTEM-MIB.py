# SNMP MIB module (CISCO-CAC-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CAC-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:43 2024
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

(cmgwIndex,
 cmgwSignalProtocolIndex) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "cmgwIndex",
    "cmgwSignalProtocolIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ccacSysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 322)
)
ccacSysMIB.setRevisions(
        ("2003-04-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcacResourceType(Integer32, TextualConvention):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("commBuf", 9),
          ("cpu5Sec", 1),
          ("cpuAvg", 2),
          ("ds0", 13),
          ("dspChannel", 14),
          ("dspQueue", 11),
          ("dynMem", 8),
          ("h248Mem", 15),
          ("ioMem", 3),
          ("msgQueue", 10),
          ("procMem", 4),
          ("staMem", 7),
          ("svc", 12),
          ("totCalls", 6),
          ("totMem", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CcacSysObjects_ObjectIdentity = ObjectIdentity
ccacSysObjects = _CcacSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1)
)
_CcacSysConfig_ObjectIdentity = ObjectIdentity
ccacSysConfig = _CcacSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1)
)
_CcacSysConfigTable_Object = MibTable
ccacSysConfigTable = _CcacSysConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccacSysConfigTable.setStatus("current")
_CcacSysConfigEntry_Object = MibTableRow
ccacSysConfigEntry = _CcacSysConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1)
)
ccacSysConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    ccacSysConfigEntry.setStatus("current")


class _CcacSysCacEnable_Type(TruthValue):
    """Custom type ccacSysCacEnable based on TruthValue"""


_CcacSysCacEnable_Object = MibTableColumn
ccacSysCacEnable = _CcacSysCacEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 1),
    _CcacSysCacEnable_Type()
)
ccacSysCacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysCacEnable.setStatus("current")


class _CcacSysNotifyEnable_Type(TruthValue):
    """Custom type ccacSysNotifyEnable based on TruthValue"""


_CcacSysNotifyEnable_Object = MibTableColumn
ccacSysNotifyEnable = _CcacSysNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 2),
    _CcacSysNotifyEnable_Type()
)
ccacSysNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysNotifyEnable.setStatus("current")


class _CcacSysTreatment_Type(Integer32):
    """Custom type ccacSysTreatment based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hairpin", 1),
          ("playMessage", 3),
          ("reject", 2))
    )


_CcacSysTreatment_Type.__name__ = "Integer32"
_CcacSysTreatment_Object = MibTableColumn
ccacSysTreatment = _CcacSysTreatment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 3),
    _CcacSysTreatment_Type()
)
ccacSysTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysTreatment.setStatus("current")


class _CcacSysRejectCode_Type(Integer32):
    """Custom type ccacSysRejectCode based on Integer32"""
    defaultValue = 44

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcacSysRejectCode_Type.__name__ = "Integer32"
_CcacSysRejectCode_Object = MibTableColumn
ccacSysRejectCode = _CcacSysRejectCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 4),
    _CcacSysRejectCode_Type()
)
ccacSysRejectCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysRejectCode.setStatus("current")


class _CcacSysIsdnRejectCode_Type(Integer32):
    """Custom type ccacSysIsdnRejectCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(34, 47),
    )


_CcacSysIsdnRejectCode_Type.__name__ = "Integer32"
_CcacSysIsdnRejectCode_Object = MibTableColumn
ccacSysIsdnRejectCode = _CcacSysIsdnRejectCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 5),
    _CcacSysIsdnRejectCode_Type()
)
ccacSysIsdnRejectCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysIsdnRejectCode.setStatus("current")
_CcacSysPlayMessageFile_Type = SnmpAdminString
_CcacSysPlayMessageFile_Object = MibTableColumn
ccacSysPlayMessageFile = _CcacSysPlayMessageFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 6),
    _CcacSysPlayMessageFile_Type()
)
ccacSysPlayMessageFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysPlayMessageFile.setStatus("current")


class _CcacSysSlidingWindowSteps_Type(Integer32):
    """Custom type ccacSysSlidingWindowSteps based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_CcacSysSlidingWindowSteps_Type.__name__ = "Integer32"
_CcacSysSlidingWindowSteps_Object = MibTableColumn
ccacSysSlidingWindowSteps = _CcacSysSlidingWindowSteps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 7),
    _CcacSysSlidingWindowSteps_Type()
)
ccacSysSlidingWindowSteps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysSlidingWindowSteps.setStatus("current")


class _CcacSysSlidingWindowSize_Type(Integer32):
    """Custom type ccacSysSlidingWindowSize based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2000),
    )


_CcacSysSlidingWindowSize_Type.__name__ = "Integer32"
_CcacSysSlidingWindowSize_Object = MibTableColumn
ccacSysSlidingWindowSize = _CcacSysSlidingWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 8),
    _CcacSysSlidingWindowSize_Type()
)
ccacSysSlidingWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysSlidingWindowSize.setStatus("current")
if mibBuilder.loadTexts:
    ccacSysSlidingWindowSize.setUnits("millisecond")


class _CcacSysCallSpike_Type(Integer32):
    """Custom type ccacSysCallSpike based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcacSysCallSpike_Type.__name__ = "Integer32"
_CcacSysCallSpike_Object = MibTableColumn
ccacSysCallSpike = _CcacSysCallSpike_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 1, 1, 1, 9),
    _CcacSysCallSpike_Type()
)
ccacSysCallSpike.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysCallSpike.setStatus("current")
if mibBuilder.loadTexts:
    ccacSysCallSpike.setUnits("calls")
_CcacSysResPolicy_ObjectIdentity = ObjectIdentity
ccacSysResPolicy = _CcacSysResPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2)
)
_CcacSysGatewayResTable_Object = MibTable
ccacSysGatewayResTable = _CcacSysGatewayResTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccacSysGatewayResTable.setStatus("current")
_CcacSysGatewayResEntry_Object = MibTableRow
ccacSysGatewayResEntry = _CcacSysGatewayResEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 1, 1)
)
ccacSysGatewayResEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAC-SYSTEM-MIB", "ccacSysGwResIndex"),
)
if mibBuilder.loadTexts:
    ccacSysGatewayResEntry.setStatus("current")


class _CcacSysGwResIndex_Type(Integer32):
    """Custom type ccacSysGwResIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CcacSysGwResIndex_Type.__name__ = "Integer32"
_CcacSysGwResIndex_Object = MibTableColumn
ccacSysGwResIndex = _CcacSysGwResIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 1, 1, 1),
    _CcacSysGwResIndex_Type()
)
ccacSysGwResIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacSysGwResIndex.setStatus("current")
_CcacSysGwResType_Type = CcacResourceType
_CcacSysGwResType_Object = MibTableColumn
ccacSysGwResType = _CcacSysGwResType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 1, 1, 2),
    _CcacSysGwResType_Type()
)
ccacSysGwResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysGwResType.setStatus("current")


class _CcacSysGwResPolicyIndex_Type(Integer32):
    """Custom type ccacSysGwResPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcacSysGwResPolicyIndex_Type.__name__ = "Integer32"
_CcacSysGwResPolicyIndex_Object = MibTableColumn
ccacSysGwResPolicyIndex = _CcacSysGwResPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 1, 1, 3),
    _CcacSysGwResPolicyIndex_Type()
)
ccacSysGwResPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysGwResPolicyIndex.setStatus("current")
_CcacSysProtocolResTable_Object = MibTable
ccacSysProtocolResTable = _CcacSysProtocolResTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccacSysProtocolResTable.setStatus("current")
_CcacSysProtocolResEntry_Object = MibTableRow
ccacSysProtocolResEntry = _CcacSysProtocolResEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 2, 1)
)
ccacSysProtocolResEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwSignalProtocolIndex"),
    (0, "CISCO-CAC-SYSTEM-MIB", "ccacSysProResIndex"),
)
if mibBuilder.loadTexts:
    ccacSysProtocolResEntry.setStatus("current")


class _CcacSysProResIndex_Type(Integer32):
    """Custom type ccacSysProResIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CcacSysProResIndex_Type.__name__ = "Integer32"
_CcacSysProResIndex_Object = MibTableColumn
ccacSysProResIndex = _CcacSysProResIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 2, 1, 1),
    _CcacSysProResIndex_Type()
)
ccacSysProResIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacSysProResIndex.setStatus("current")
_CcacSysProResType_Type = CcacResourceType
_CcacSysProResType_Object = MibTableColumn
ccacSysProResType = _CcacSysProResType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 2, 1, 2),
    _CcacSysProResType_Type()
)
ccacSysProResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysProResType.setStatus("current")


class _CcacSysProResPolicyIndex_Type(Integer32):
    """Custom type ccacSysProResPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcacSysProResPolicyIndex_Type.__name__ = "Integer32"
_CcacSysProResPolicyIndex_Object = MibTableColumn
ccacSysProResPolicyIndex = _CcacSysProResPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 2, 1, 3),
    _CcacSysProResPolicyIndex_Type()
)
ccacSysProResPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysProResPolicyIndex.setStatus("current")
_CcacSysResPolicyTable_Object = MibTable
ccacSysResPolicyTable = _CcacSysResPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ccacSysResPolicyTable.setStatus("current")
_CcacSysResPolicyEntry_Object = MibTableRow
ccacSysResPolicyEntry = _CcacSysResPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1)
)
ccacSysResPolicyEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAC-SYSTEM-MIB", "ccacSysRpIndex"),
)
if mibBuilder.loadTexts:
    ccacSysResPolicyEntry.setStatus("current")


class _CcacSysRpIndex_Type(Integer32):
    """Custom type ccacSysRpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcacSysRpIndex_Type.__name__ = "Integer32"
_CcacSysRpIndex_Object = MibTableColumn
ccacSysRpIndex = _CcacSysRpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 1),
    _CcacSysRpIndex_Type()
)
ccacSysRpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacSysRpIndex.setStatus("current")
_CcacSysRpResType_Type = CcacResourceType
_CcacSysRpResType_Object = MibTableColumn
ccacSysRpResType = _CcacSysRpResType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 2),
    _CcacSysRpResType_Type()
)
ccacSysRpResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRpResType.setStatus("current")
_CcacSysRpUserTunable_Type = TruthValue
_CcacSysRpUserTunable_Object = MibTableColumn
ccacSysRpUserTunable = _CcacSysRpUserTunable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 3),
    _CcacSysRpUserTunable_Type()
)
ccacSysRpUserTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRpUserTunable.setStatus("current")
_CcacSysRpAvgUtilization_Type = TruthValue
_CcacSysRpAvgUtilization_Object = MibTableColumn
ccacSysRpAvgUtilization = _CcacSysRpAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 4),
    _CcacSysRpAvgUtilization_Type()
)
ccacSysRpAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRpAvgUtilization.setStatus("current")


class _CcacSysRpPercentOrAbsNum_Type(Integer32):
    """Custom type ccacSysRpPercentOrAbsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unitAbsoluteNum", 2),
          ("unitPercent", 1))
    )


_CcacSysRpPercentOrAbsNum_Type.__name__ = "Integer32"
_CcacSysRpPercentOrAbsNum_Object = MibTableColumn
ccacSysRpPercentOrAbsNum = _CcacSysRpPercentOrAbsNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 5),
    _CcacSysRpPercentOrAbsNum_Type()
)
ccacSysRpPercentOrAbsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRpPercentOrAbsNum.setStatus("current")


class _CcacSysRpHighThreshold_Type(Integer32):
    """Custom type ccacSysRpHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcacSysRpHighThreshold_Type.__name__ = "Integer32"
_CcacSysRpHighThreshold_Object = MibTableColumn
ccacSysRpHighThreshold = _CcacSysRpHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 6),
    _CcacSysRpHighThreshold_Type()
)
ccacSysRpHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysRpHighThreshold.setStatus("current")


class _CcacSysRpMedThreshold_Type(Integer32):
    """Custom type ccacSysRpMedThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcacSysRpMedThreshold_Type.__name__ = "Integer32"
_CcacSysRpMedThreshold_Object = MibTableColumn
ccacSysRpMedThreshold = _CcacSysRpMedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 7),
    _CcacSysRpMedThreshold_Type()
)
ccacSysRpMedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysRpMedThreshold.setStatus("current")


class _CcacSysRpLowThreshold_Type(Integer32):
    """Custom type ccacSysRpLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcacSysRpLowThreshold_Type.__name__ = "Integer32"
_CcacSysRpLowThreshold_Object = MibTableColumn
ccacSysRpLowThreshold = _CcacSysRpLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 8),
    _CcacSysRpLowThreshold_Type()
)
ccacSysRpLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysRpLowThreshold.setStatus("current")


class _CcacSysRpInterval_Type(Integer32):
    """Custom type ccacSysRpInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CcacSysRpInterval_Type.__name__ = "Integer32"
_CcacSysRpInterval_Object = MibTableColumn
ccacSysRpInterval = _CcacSysRpInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 9),
    _CcacSysRpInterval_Type()
)
ccacSysRpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysRpInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccacSysRpInterval.setUnits("seconds")


class _CcacSysRpAction_Type(Integer32):
    """Custom type ccacSysRpAction based on Integer32"""
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
        *(("busyout", 2),
          ("busyoutAndTreatment", 4),
          ("none", 1),
          ("treatment", 3))
    )


_CcacSysRpAction_Type.__name__ = "Integer32"
_CcacSysRpAction_Object = MibTableColumn
ccacSysRpAction = _CcacSysRpAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 10),
    _CcacSysRpAction_Type()
)
ccacSysRpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacSysRpAction.setStatus("current")


class _CcacSysRpCurReading_Type(Integer32):
    """Custom type ccacSysRpCurReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcacSysRpCurReading_Type.__name__ = "Integer32"
_CcacSysRpCurReading_Object = MibTableColumn
ccacSysRpCurReading = _CcacSysRpCurReading_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 11),
    _CcacSysRpCurReading_Type()
)
ccacSysRpCurReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRpCurReading.setStatus("current")
_CcacSysRpAvailable_Type = TruthValue
_CcacSysRpAvailable_Object = MibTableColumn
ccacSysRpAvailable = _CcacSysRpAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 2, 3, 1, 12),
    _CcacSysRpAvailable_Type()
)
ccacSysRpAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRpAvailable.setStatus("current")
_CcacSysStat_ObjectIdentity = ObjectIdentity
ccacSysStat = _CcacSysStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3)
)
_CcacSysResStatTable_Object = MibTable
ccacSysResStatTable = _CcacSysResStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccacSysResStatTable.setStatus("current")
_CcacSysResStatEntry_Object = MibTableRow
ccacSysResStatEntry = _CcacSysResStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1)
)
ccacSysResStatEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAC-SYSTEM-MIB", "ccacSysRpIndex"),
)
if mibBuilder.loadTexts:
    ccacSysResStatEntry.setStatus("current")


class _CcacSysRsState_Type(Integer32):
    """Custom type ccacSysRsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("thresholdClear", 1),
          ("thresholdExceed", 2),
          ("thresholdWarn", 3))
    )


_CcacSysRsState_Type.__name__ = "Integer32"
_CcacSysRsState_Object = MibTableColumn
ccacSysRsState = _CcacSysRsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1, 1),
    _CcacSysRsState_Type()
)
ccacSysRsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRsState.setStatus("current")
_CcacSysRsDuration_Type = TimeInterval
_CcacSysRsDuration_Object = MibTableColumn
ccacSysRsDuration = _CcacSysRsDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1, 2),
    _CcacSysRsDuration_Type()
)
ccacSysRsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRsDuration.setStatus("current")
_CcacSysRsPrevDuration_Type = TimeInterval
_CcacSysRsPrevDuration_Object = MibTableColumn
ccacSysRsPrevDuration = _CcacSysRsPrevDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1, 3),
    _CcacSysRsPrevDuration_Type()
)
ccacSysRsPrevDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRsPrevDuration.setStatus("current")
_CcacSysRsExceedCount_Type = Counter32
_CcacSysRsExceedCount_Object = MibTableColumn
ccacSysRsExceedCount = _CcacSysRsExceedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1, 4),
    _CcacSysRsExceedCount_Type()
)
ccacSysRsExceedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRsExceedCount.setStatus("current")
_CcacSysRsCallsWhenExceed_Type = Counter32
_CcacSysRsCallsWhenExceed_Object = MibTableColumn
ccacSysRsCallsWhenExceed = _CcacSysRsCallsWhenExceed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 1, 1, 5),
    _CcacSysRsCallsWhenExceed_Type()
)
ccacSysRsCallsWhenExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRsCallsWhenExceed.setStatus("current")
_CcacSysStatTable_Object = MibTable
ccacSysStatTable = _CcacSysStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ccacSysStatTable.setStatus("current")
_CcacSysStatEntry_Object = MibTableRow
ccacSysStatEntry = _CcacSysStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ccacSysStatEntry.setStatus("current")
_CcacSysCallRejections_Type = Counter32
_CcacSysCallRejections_Object = MibTableColumn
ccacSysCallRejections = _CcacSysCallRejections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 2, 1, 1),
    _CcacSysCallRejections_Type()
)
ccacSysCallRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysCallRejections.setStatus("current")
_CcacSysCallsInSWindow_Type = Counter32
_CcacSysCallsInSWindow_Object = MibTableColumn
ccacSysCallsInSWindow = _CcacSysCallsInSWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 1, 3, 2, 1, 2),
    _CcacSysCallsInSWindow_Type()
)
ccacSysCallsInSWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysCallsInSWindow.setStatus("current")
_CcacSysConformance_ObjectIdentity = ObjectIdentity
ccacSysConformance = _CcacSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 2)
)
_CcacSysCompliances_ObjectIdentity = ObjectIdentity
ccacSysCompliances = _CcacSysCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 1)
)
_CcacSysGroups_ObjectIdentity = ObjectIdentity
ccacSysGroups = _CcacSysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2)
)
ccacSysConfigEntry.registerAugmentions(
    ("CISCO-CAC-SYSTEM-MIB",
     "ccacSysStatEntry")
)
ccacSysStatEntry.setIndexNames(*ccacSysConfigEntry.getIndexNames())

# Managed Objects groups

ccacSysConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 1)
)
ccacSysConfigGroup.setObjects(
      *(("CISCO-CAC-SYSTEM-MIB", "ccacSysCacEnable"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysNotifyEnable"))
)
if mibBuilder.loadTexts:
    ccacSysConfigGroup.setStatus("current")

ccacSysDialCtrlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 2)
)
ccacSysDialCtrlConfigGroup.setObjects(
      *(("CISCO-CAC-SYSTEM-MIB", "ccacSysTreatment"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRejectCode"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysIsdnRejectCode"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysPlayMessageFile"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysSlidingWindowSteps"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysSlidingWindowSize"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysCallSpike"))
)
if mibBuilder.loadTexts:
    ccacSysDialCtrlConfigGroup.setStatus("current")

ccacSysResPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 3)
)
ccacSysResPolicyGroup.setObjects(
      *(("CISCO-CAC-SYSTEM-MIB", "ccacSysRpResType"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpUserTunable"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpAvgUtilization"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpPercentOrAbsNum"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpHighThreshold"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpMedThreshold"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpLowThreshold"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpInterval"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpAction"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpCurReading"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRpAvailable"))
)
if mibBuilder.loadTexts:
    ccacSysResPolicyGroup.setStatus("current")

ccacSysStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 4)
)
ccacSysStatGroup.setObjects(
      *(("CISCO-CAC-SYSTEM-MIB", "ccacSysRsState"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRsDuration"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRsPrevDuration"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRsExceedCount"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysRsCallsWhenExceed"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysCallRejections"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysCallsInSWindow"))
)
if mibBuilder.loadTexts:
    ccacSysStatGroup.setStatus("current")

ccacSysGatewayResGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 5)
)
ccacSysGatewayResGroup.setObjects(
      *(("CISCO-CAC-SYSTEM-MIB", "ccacSysGwResType"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysGwResPolicyIndex"))
)
if mibBuilder.loadTexts:
    ccacSysGatewayResGroup.setStatus("current")

ccacSysProtocolResGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 2, 6)
)
ccacSysProtocolResGroup.setObjects(
      *(("CISCO-CAC-SYSTEM-MIB", "ccacSysProResType"),
        ("CISCO-CAC-SYSTEM-MIB", "ccacSysProResPolicyIndex"))
)
if mibBuilder.loadTexts:
    ccacSysProtocolResGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ccacSysCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 322, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ccacSysCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CAC-SYSTEM-MIB",
    **{"CcacResourceType": CcacResourceType,
       "ccacSysMIB": ccacSysMIB,
       "ccacSysObjects": ccacSysObjects,
       "ccacSysConfig": ccacSysConfig,
       "ccacSysConfigTable": ccacSysConfigTable,
       "ccacSysConfigEntry": ccacSysConfigEntry,
       "ccacSysCacEnable": ccacSysCacEnable,
       "ccacSysNotifyEnable": ccacSysNotifyEnable,
       "ccacSysTreatment": ccacSysTreatment,
       "ccacSysRejectCode": ccacSysRejectCode,
       "ccacSysIsdnRejectCode": ccacSysIsdnRejectCode,
       "ccacSysPlayMessageFile": ccacSysPlayMessageFile,
       "ccacSysSlidingWindowSteps": ccacSysSlidingWindowSteps,
       "ccacSysSlidingWindowSize": ccacSysSlidingWindowSize,
       "ccacSysCallSpike": ccacSysCallSpike,
       "ccacSysResPolicy": ccacSysResPolicy,
       "ccacSysGatewayResTable": ccacSysGatewayResTable,
       "ccacSysGatewayResEntry": ccacSysGatewayResEntry,
       "ccacSysGwResIndex": ccacSysGwResIndex,
       "ccacSysGwResType": ccacSysGwResType,
       "ccacSysGwResPolicyIndex": ccacSysGwResPolicyIndex,
       "ccacSysProtocolResTable": ccacSysProtocolResTable,
       "ccacSysProtocolResEntry": ccacSysProtocolResEntry,
       "ccacSysProResIndex": ccacSysProResIndex,
       "ccacSysProResType": ccacSysProResType,
       "ccacSysProResPolicyIndex": ccacSysProResPolicyIndex,
       "ccacSysResPolicyTable": ccacSysResPolicyTable,
       "ccacSysResPolicyEntry": ccacSysResPolicyEntry,
       "ccacSysRpIndex": ccacSysRpIndex,
       "ccacSysRpResType": ccacSysRpResType,
       "ccacSysRpUserTunable": ccacSysRpUserTunable,
       "ccacSysRpAvgUtilization": ccacSysRpAvgUtilization,
       "ccacSysRpPercentOrAbsNum": ccacSysRpPercentOrAbsNum,
       "ccacSysRpHighThreshold": ccacSysRpHighThreshold,
       "ccacSysRpMedThreshold": ccacSysRpMedThreshold,
       "ccacSysRpLowThreshold": ccacSysRpLowThreshold,
       "ccacSysRpInterval": ccacSysRpInterval,
       "ccacSysRpAction": ccacSysRpAction,
       "ccacSysRpCurReading": ccacSysRpCurReading,
       "ccacSysRpAvailable": ccacSysRpAvailable,
       "ccacSysStat": ccacSysStat,
       "ccacSysResStatTable": ccacSysResStatTable,
       "ccacSysResStatEntry": ccacSysResStatEntry,
       "ccacSysRsState": ccacSysRsState,
       "ccacSysRsDuration": ccacSysRsDuration,
       "ccacSysRsPrevDuration": ccacSysRsPrevDuration,
       "ccacSysRsExceedCount": ccacSysRsExceedCount,
       "ccacSysRsCallsWhenExceed": ccacSysRsCallsWhenExceed,
       "ccacSysStatTable": ccacSysStatTable,
       "ccacSysStatEntry": ccacSysStatEntry,
       "ccacSysCallRejections": ccacSysCallRejections,
       "ccacSysCallsInSWindow": ccacSysCallsInSWindow,
       "ccacSysConformance": ccacSysConformance,
       "ccacSysCompliances": ccacSysCompliances,
       "ccacSysCompliance": ccacSysCompliance,
       "ccacSysGroups": ccacSysGroups,
       "ccacSysConfigGroup": ccacSysConfigGroup,
       "ccacSysDialCtrlConfigGroup": ccacSysDialCtrlConfigGroup,
       "ccacSysResPolicyGroup": ccacSysResPolicyGroup,
       "ccacSysStatGroup": ccacSysStatGroup,
       "ccacSysGatewayResGroup": ccacSysGatewayResGroup,
       "ccacSysProtocolResGroup": ccacSysProtocolResGroup}
)
