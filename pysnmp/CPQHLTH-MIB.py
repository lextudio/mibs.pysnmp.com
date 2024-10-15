# SNMP MIB module (CPQHLTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQHLTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:24 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(cpqSiMemModuleSize,
 cpqSiServerSystemId) = mibBuilder.importSymbols(
    "CPQSINFO-MIB",
    "cpqSiMemModuleSize",
    "cpqSiServerSystemId")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqHealth_ObjectIdentity = ObjectIdentity
cpqHealth = _CpqHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6)
)
_CpqHeMibRev_ObjectIdentity = ObjectIdentity
cpqHeMibRev = _CpqHeMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 1)
)


class _CpqHeMibRevMajor_Type(Integer32):
    """Custom type cpqHeMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqHeMibRevMajor_Type.__name__ = "Integer32"
_CpqHeMibRevMajor_Object = MibScalar
cpqHeMibRevMajor = _CpqHeMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 1, 1),
    _CpqHeMibRevMajor_Type()
)
cpqHeMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeMibRevMajor.setStatus("mandatory")


class _CpqHeMibRevMinor_Type(Integer32):
    """Custom type cpqHeMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHeMibRevMinor_Type.__name__ = "Integer32"
_CpqHeMibRevMinor_Object = MibScalar
cpqHeMibRevMinor = _CpqHeMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 1, 2),
    _CpqHeMibRevMinor_Type()
)
cpqHeMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeMibRevMinor.setStatus("mandatory")


class _CpqHeMibCondition_Type(Integer32):
    """Custom type cpqHeMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeMibCondition_Type.__name__ = "Integer32"
_CpqHeMibCondition_Object = MibScalar
cpqHeMibCondition = _CpqHeMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 1, 3),
    _CpqHeMibCondition_Type()
)
cpqHeMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeMibCondition.setStatus("mandatory")
_CpqHeComponent_ObjectIdentity = ObjectIdentity
cpqHeComponent = _CpqHeComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2)
)
_CpqHeInterface_ObjectIdentity = ObjectIdentity
cpqHeInterface = _CpqHeInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1)
)
_CpqHeOsNetWare3x_ObjectIdentity = ObjectIdentity
cpqHeOsNetWare3x = _CpqHeOsNetWare3x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 1)
)


class _CpqHeNw3xDriverName_Type(DisplayString):
    """Custom type cpqHeNw3xDriverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeNw3xDriverName_Type.__name__ = "DisplayString"
_CpqHeNw3xDriverName_Object = MibScalar
cpqHeNw3xDriverName = _CpqHeNw3xDriverName_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 1, 1),
    _CpqHeNw3xDriverName_Type()
)
cpqHeNw3xDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeNw3xDriverName.setStatus("deprecated")


class _CpqHeNw3xDriverDate_Type(DisplayString):
    """Custom type cpqHeNw3xDriverDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CpqHeNw3xDriverDate_Type.__name__ = "DisplayString"
_CpqHeNw3xDriverDate_Object = MibScalar
cpqHeNw3xDriverDate = _CpqHeNw3xDriverDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 1, 2),
    _CpqHeNw3xDriverDate_Type()
)
cpqHeNw3xDriverDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeNw3xDriverDate.setStatus("deprecated")


class _CpqHeNw3xDriverVersion_Type(DisplayString):
    """Custom type cpqHeNw3xDriverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqHeNw3xDriverVersion_Type.__name__ = "DisplayString"
_CpqHeNw3xDriverVersion_Object = MibScalar
cpqHeNw3xDriverVersion = _CpqHeNw3xDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 1, 3),
    _CpqHeNw3xDriverVersion_Type()
)
cpqHeNw3xDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeNw3xDriverVersion.setStatus("deprecated")
_CpqHeOsCommon_ObjectIdentity = ObjectIdentity
cpqHeOsCommon = _CpqHeOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 4)
)


class _CpqHeOsCommonPollFreq_Type(Integer32):
    """Custom type cpqHeOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHeOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqHeOsCommonPollFreq_Object = MibScalar
cpqHeOsCommonPollFreq = _CpqHeOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 4, 1),
    _CpqHeOsCommonPollFreq_Type()
)
cpqHeOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeOsCommonPollFreq.setStatus("mandatory")
_CpqHeOsCommonModuleTable_Object = MibTable
cpqHeOsCommonModuleTable = _CpqHeOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqHeOsCommonModuleTable.setStatus("deprecated")
_CpqHeOsCommonModuleEntry_Object = MibTableRow
cpqHeOsCommonModuleEntry = _CpqHeOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 4, 2, 1)
)
cpqHeOsCommonModuleEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqHeOsCommonModuleEntry.setStatus("deprecated")


class _CpqHeOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqHeOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHeOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqHeOsCommonModuleIndex_Object = MibTableColumn
cpqHeOsCommonModuleIndex = _CpqHeOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 4, 2, 1, 1),
    _CpqHeOsCommonModuleIndex_Type()
)
cpqHeOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeOsCommonModuleIndex.setStatus("deprecated")


class _CpqHeOsCommonModuleName_Type(DisplayString):
    """Custom type cpqHeOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqHeOsCommonModuleName_Object = MibTableColumn
cpqHeOsCommonModuleName = _CpqHeOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 4, 2, 1, 2),
    _CpqHeOsCommonModuleName_Type()
)
cpqHeOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeOsCommonModuleName.setStatus("deprecated")


class _CpqHeOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqHeOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqHeOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqHeOsCommonModuleVersion_Object = MibTableColumn
cpqHeOsCommonModuleVersion = _CpqHeOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 4, 2, 1, 3),
    _CpqHeOsCommonModuleVersion_Type()
)
cpqHeOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeOsCommonModuleVersion.setStatus("deprecated")


class _CpqHeOsCommonModuleDate_Type(OctetString):
    """Custom type cpqHeOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqHeOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqHeOsCommonModuleDate_Object = MibTableColumn
cpqHeOsCommonModuleDate = _CpqHeOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 4, 2, 1, 4),
    _CpqHeOsCommonModuleDate_Type()
)
cpqHeOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeOsCommonModuleDate.setStatus("deprecated")


class _CpqHeOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqHeOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqHeOsCommonModulePurpose_Object = MibTableColumn
cpqHeOsCommonModulePurpose = _CpqHeOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 1, 4, 2, 1, 5),
    _CpqHeOsCommonModulePurpose_Type()
)
cpqHeOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeOsCommonModulePurpose.setStatus("deprecated")
_CpqHeCriticalError_ObjectIdentity = ObjectIdentity
cpqHeCriticalError = _CpqHeCriticalError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2)
)


class _CpqHeCritLogSupported_Type(Integer32):
    """Custom type cpqHeCritLogSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("other", 1),
          ("supported", 3))
    )


_CpqHeCritLogSupported_Type.__name__ = "Integer32"
_CpqHeCritLogSupported_Object = MibScalar
cpqHeCritLogSupported = _CpqHeCritLogSupported_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 1),
    _CpqHeCritLogSupported_Type()
)
cpqHeCritLogSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCritLogSupported.setStatus("mandatory")


class _CpqHeCritLogCondition_Type(Integer32):
    """Custom type cpqHeCritLogCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeCritLogCondition_Type.__name__ = "Integer32"
_CpqHeCritLogCondition_Object = MibScalar
cpqHeCritLogCondition = _CpqHeCritLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 2),
    _CpqHeCritLogCondition_Type()
)
cpqHeCritLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCritLogCondition.setStatus("mandatory")


class _CpqHeLastCritErrorAbendMsg_Type(DisplayString):
    """Custom type cpqHeLastCritErrorAbendMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeLastCritErrorAbendMsg_Type.__name__ = "DisplayString"
_CpqHeLastCritErrorAbendMsg_Object = MibScalar
cpqHeLastCritErrorAbendMsg = _CpqHeLastCritErrorAbendMsg_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 3),
    _CpqHeLastCritErrorAbendMsg_Type()
)
cpqHeLastCritErrorAbendMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeLastCritErrorAbendMsg.setStatus("mandatory")
_CpqHeCriticalErrorTable_Object = MibTable
cpqHeCriticalErrorTable = _CpqHeCriticalErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cpqHeCriticalErrorTable.setStatus("mandatory")
_CpqHeCriticalErrorEntry_Object = MibTableRow
cpqHeCriticalErrorEntry = _CpqHeCriticalErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 4, 1)
)
cpqHeCriticalErrorEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeCriticalErrorIndex"),
)
if mibBuilder.loadTexts:
    cpqHeCriticalErrorEntry.setStatus("mandatory")


class _CpqHeCriticalErrorIndex_Type(Integer32):
    """Custom type cpqHeCriticalErrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHeCriticalErrorIndex_Type.__name__ = "Integer32"
_CpqHeCriticalErrorIndex_Object = MibTableColumn
cpqHeCriticalErrorIndex = _CpqHeCriticalErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 4, 1, 1),
    _CpqHeCriticalErrorIndex_Type()
)
cpqHeCriticalErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCriticalErrorIndex.setStatus("mandatory")


class _CpqHeCriticalErrorStatus_Type(Integer32):
    """Custom type cpqHeCriticalErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("corrected", 2),
          ("uncorrected", 1))
    )


_CpqHeCriticalErrorStatus_Type.__name__ = "Integer32"
_CpqHeCriticalErrorStatus_Object = MibTableColumn
cpqHeCriticalErrorStatus = _CpqHeCriticalErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 4, 1, 2),
    _CpqHeCriticalErrorStatus_Type()
)
cpqHeCriticalErrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeCriticalErrorStatus.setStatus("mandatory")


class _CpqHeCriticalErrorType_Type(Integer32):
    """Custom type cpqHeCriticalErrorType based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("abend", 27),
          ("asrBaseMemoryParity", 23),
          ("asrDetectedAtBoot", 32),
          ("asrExtendedMemParity", 24),
          ("asrMemoryParity", 26),
          ("asrResetLimit", 25),
          ("asrTestEvent", 28),
          ("asrTimeoutNmi", 29),
          ("busMasterTimeoutNmi", 4),
          ("cacheParityNmi", 8),
          ("cautionTemperature", 12),
          ("commandBusTimeoutNmi", 5),
          ("cpuInternalThreshPassed", 39),
          ("cpuLocalError", 20),
          ("criticalException", 14),
          ("dcConverterFailure", 38),
          ("diagnosticError", 35),
          ("eisaHostMemReadHit", 10),
          ("empty", 2),
          ("failsafeTimer", 21),
          ("fanFailure", 30),
          ("ioCheckNmi", 6),
          ("nonCorrectableMemErr", 3),
          ("other", 1),
          ("pciBusParityError", 34),
          ("pentiumApcheck", 19),
          ("pentiumAperr", 17),
          ("pentiumBerr", 37),
          ("pentiumIeerr", 18),
          ("pentiumIperr", 16),
          ("postCriticalError", 13),
          ("processorFailure", 11),
          ("processorParityNmi", 9),
          ("redunPowerSupplyFailure", 33),
          ("refreshOverflowNmi", 7),
          ("rtcChipBatteryFailure", 36),
          ("serverManagerIfFail", 15),
          ("softwareNmi", 22),
          ("upsDetectedLineFail", 31))
    )


_CpqHeCriticalErrorType_Type.__name__ = "Integer32"
_CpqHeCriticalErrorType_Object = MibTableColumn
cpqHeCriticalErrorType = _CpqHeCriticalErrorType_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 4, 1, 3),
    _CpqHeCriticalErrorType_Type()
)
cpqHeCriticalErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCriticalErrorType.setStatus("mandatory")


class _CpqHeCriticalErrorTime_Type(OctetString):
    """Custom type cpqHeCriticalErrorTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CpqHeCriticalErrorTime_Type.__name__ = "OctetString"
_CpqHeCriticalErrorTime_Object = MibTableColumn
cpqHeCriticalErrorTime = _CpqHeCriticalErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 4, 1, 4),
    _CpqHeCriticalErrorTime_Type()
)
cpqHeCriticalErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCriticalErrorTime.setStatus("mandatory")


class _CpqHeCriticalErrorInfo_Type(OctetString):
    """Custom type cpqHeCriticalErrorInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CpqHeCriticalErrorInfo_Type.__name__ = "OctetString"
_CpqHeCriticalErrorInfo_Object = MibTableColumn
cpqHeCriticalErrorInfo = _CpqHeCriticalErrorInfo_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 4, 1, 5),
    _CpqHeCriticalErrorInfo_Type()
)
cpqHeCriticalErrorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCriticalErrorInfo.setStatus("mandatory")


class _CpqHeCriticalErrorDesc_Type(DisplayString):
    """Custom type cpqHeCriticalErrorDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeCriticalErrorDesc_Type.__name__ = "DisplayString"
_CpqHeCriticalErrorDesc_Object = MibTableColumn
cpqHeCriticalErrorDesc = _CpqHeCriticalErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 2, 4, 1, 6),
    _CpqHeCriticalErrorDesc_Type()
)
cpqHeCriticalErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCriticalErrorDesc.setStatus("mandatory")
_CpqHeCorrectableMemory_ObjectIdentity = ObjectIdentity
cpqHeCorrectableMemory = _CpqHeCorrectableMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3)
)


class _CpqHeCorrMemLogStatus_Type(Integer32):
    """Custom type cpqHeCorrMemLogStatus based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 4),
          ("notSupported", 2),
          ("other", 1))
    )


_CpqHeCorrMemLogStatus_Type.__name__ = "Integer32"
_CpqHeCorrMemLogStatus_Object = MibScalar
cpqHeCorrMemLogStatus = _CpqHeCorrMemLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 1),
    _CpqHeCorrMemLogStatus_Type()
)
cpqHeCorrMemLogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCorrMemLogStatus.setStatus("mandatory")


class _CpqHeCorrMemLogCondition_Type(Integer32):
    """Custom type cpqHeCorrMemLogCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeCorrMemLogCondition_Type.__name__ = "Integer32"
_CpqHeCorrMemLogCondition_Object = MibScalar
cpqHeCorrMemLogCondition = _CpqHeCorrMemLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 2),
    _CpqHeCorrMemLogCondition_Type()
)
cpqHeCorrMemLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCorrMemLogCondition.setStatus("mandatory")


class _CpqHeCorrMemTotalErrs_Type(Integer32):
    """Custom type cpqHeCorrMemTotalErrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqHeCorrMemTotalErrs_Type.__name__ = "Integer32"
_CpqHeCorrMemTotalErrs_Object = MibScalar
cpqHeCorrMemTotalErrs = _CpqHeCorrMemTotalErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 3),
    _CpqHeCorrMemTotalErrs_Type()
)
cpqHeCorrMemTotalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCorrMemTotalErrs.setStatus("deprecated")
_CpqHeCorrMemErrTable_Object = MibTable
cpqHeCorrMemErrTable = _CpqHeCorrMemErrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 4)
)
if mibBuilder.loadTexts:
    cpqHeCorrMemErrTable.setStatus("mandatory")
_CpqHeCorrMemErrEntry_Object = MibTableRow
cpqHeCorrMemErrEntry = _CpqHeCorrMemErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 4, 1)
)
cpqHeCorrMemErrEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeCorrMemErrIndex"),
)
if mibBuilder.loadTexts:
    cpqHeCorrMemErrEntry.setStatus("mandatory")


class _CpqHeCorrMemErrIndex_Type(Integer32):
    """Custom type cpqHeCorrMemErrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHeCorrMemErrIndex_Type.__name__ = "Integer32"
_CpqHeCorrMemErrIndex_Object = MibTableColumn
cpqHeCorrMemErrIndex = _CpqHeCorrMemErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 4, 1, 1),
    _CpqHeCorrMemErrIndex_Type()
)
cpqHeCorrMemErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCorrMemErrIndex.setStatus("mandatory")


class _CpqHeCorrMemErrCount_Type(Integer32):
    """Custom type cpqHeCorrMemErrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHeCorrMemErrCount_Type.__name__ = "Integer32"
_CpqHeCorrMemErrCount_Object = MibTableColumn
cpqHeCorrMemErrCount = _CpqHeCorrMemErrCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 4, 1, 2),
    _CpqHeCorrMemErrCount_Type()
)
cpqHeCorrMemErrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeCorrMemErrCount.setStatus("mandatory")


class _CpqHeCorrMemErrTime_Type(OctetString):
    """Custom type cpqHeCorrMemErrTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CpqHeCorrMemErrTime_Type.__name__ = "OctetString"
_CpqHeCorrMemErrTime_Object = MibTableColumn
cpqHeCorrMemErrTime = _CpqHeCorrMemErrTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 4, 1, 3),
    _CpqHeCorrMemErrTime_Type()
)
cpqHeCorrMemErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCorrMemErrTime.setStatus("mandatory")


class _CpqHeCorrMemErrDdr_Type(OctetString):
    """Custom type cpqHeCorrMemErrDdr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CpqHeCorrMemErrDdr_Type.__name__ = "OctetString"
_CpqHeCorrMemErrDdr_Object = MibTableColumn
cpqHeCorrMemErrDdr = _CpqHeCorrMemErrDdr_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 4, 1, 4),
    _CpqHeCorrMemErrDdr_Type()
)
cpqHeCorrMemErrDdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCorrMemErrDdr.setStatus("mandatory")


class _CpqHeCorrMemErrSyndrome_Type(OctetString):
    """Custom type cpqHeCorrMemErrSyndrome based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CpqHeCorrMemErrSyndrome_Type.__name__ = "OctetString"
_CpqHeCorrMemErrSyndrome_Object = MibTableColumn
cpqHeCorrMemErrSyndrome = _CpqHeCorrMemErrSyndrome_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 4, 1, 5),
    _CpqHeCorrMemErrSyndrome_Type()
)
cpqHeCorrMemErrSyndrome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCorrMemErrSyndrome.setStatus("mandatory")


class _CpqHeCorrMemErrDesc_Type(DisplayString):
    """Custom type cpqHeCorrMemErrDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeCorrMemErrDesc_Type.__name__ = "DisplayString"
_CpqHeCorrMemErrDesc_Object = MibTableColumn
cpqHeCorrMemErrDesc = _CpqHeCorrMemErrDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 4, 1, 6),
    _CpqHeCorrMemErrDesc_Type()
)
cpqHeCorrMemErrDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCorrMemErrDesc.setStatus("mandatory")


class _CpqHeCorrMemErrHwLocation_Type(DisplayString):
    """Custom type cpqHeCorrMemErrHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeCorrMemErrHwLocation_Type.__name__ = "DisplayString"
_CpqHeCorrMemErrHwLocation_Object = MibTableColumn
cpqHeCorrMemErrHwLocation = _CpqHeCorrMemErrHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 4, 1, 7),
    _CpqHeCorrMemErrHwLocation_Type()
)
cpqHeCorrMemErrHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCorrMemErrHwLocation.setStatus("optional")


class _CpqHeCorrMemErrorCntThresh_Type(Integer32):
    """Custom type cpqHeCorrMemErrorCntThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqHeCorrMemErrorCntThresh_Type.__name__ = "Integer32"
_CpqHeCorrMemErrorCntThresh_Object = MibScalar
cpqHeCorrMemErrorCntThresh = _CpqHeCorrMemErrorCntThresh_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 3, 5),
    _CpqHeCorrMemErrorCntThresh_Type()
)
cpqHeCorrMemErrorCntThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeCorrMemErrorCntThresh.setStatus("mandatory")
_CpqHeAsr_ObjectIdentity = ObjectIdentity
cpqHeAsr = _CpqHeAsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5)
)


class _CpqHeAsrStatus_Type(Integer32):
    """Custom type cpqHeAsrStatus based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 4),
          ("notAvailable", 2),
          ("other", 1))
    )


_CpqHeAsrStatus_Type.__name__ = "Integer32"
_CpqHeAsrStatus_Object = MibScalar
cpqHeAsrStatus = _CpqHeAsrStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 1),
    _CpqHeAsrStatus_Type()
)
cpqHeAsrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrStatus.setStatus("mandatory")


class _CpqHeAsrMajorVersion_Type(Integer32):
    """Custom type cpqHeAsrMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHeAsrMajorVersion_Type.__name__ = "Integer32"
_CpqHeAsrMajorVersion_Object = MibScalar
cpqHeAsrMajorVersion = _CpqHeAsrMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 2),
    _CpqHeAsrMajorVersion_Type()
)
cpqHeAsrMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeAsrMajorVersion.setStatus("mandatory")


class _CpqHeAsrMinorVersion_Type(Integer32):
    """Custom type cpqHeAsrMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHeAsrMinorVersion_Type.__name__ = "Integer32"
_CpqHeAsrMinorVersion_Object = MibScalar
cpqHeAsrMinorVersion = _CpqHeAsrMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 3),
    _CpqHeAsrMinorVersion_Type()
)
cpqHeAsrMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeAsrMinorVersion.setStatus("mandatory")
_CpqHeAsrTimeout_Type = Integer32
_CpqHeAsrTimeout_Object = MibScalar
cpqHeAsrTimeout = _CpqHeAsrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 4),
    _CpqHeAsrTimeout_Type()
)
cpqHeAsrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrTimeout.setStatus("mandatory")
_CpqHeAsrBaseIo_Type = Integer32
_CpqHeAsrBaseIo_Object = MibScalar
cpqHeAsrBaseIo = _CpqHeAsrBaseIo_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 5),
    _CpqHeAsrBaseIo_Type()
)
cpqHeAsrBaseIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeAsrBaseIo.setStatus("mandatory")


class _CpqHeAsrPost_Type(Integer32):
    """Custom type cpqHeAsrPost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 3),
          ("other", 1))
    )


_CpqHeAsrPost_Type.__name__ = "Integer32"
_CpqHeAsrPost_Object = MibScalar
cpqHeAsrPost = _CpqHeAsrPost_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 6),
    _CpqHeAsrPost_Type()
)
cpqHeAsrPost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeAsrPost.setStatus("deprecated")


class _CpqHeAsrReset_Type(Integer32):
    """Custom type cpqHeAsrReset based on Integer32"""
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
        *(("asrReset", 3),
          ("manualReset", 2),
          ("other", 1),
          ("viewed-asrReset", 4))
    )


_CpqHeAsrReset_Type.__name__ = "Integer32"
_CpqHeAsrReset_Object = MibScalar
cpqHeAsrReset = _CpqHeAsrReset_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 7),
    _CpqHeAsrReset_Type()
)
cpqHeAsrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrReset.setStatus("mandatory")


class _CpqHeAsrReboot_Type(Integer32):
    """Custom type cpqHeAsrReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootOs", 2),
          ("bootUtilities", 3),
          ("other", 1))
    )


_CpqHeAsrReboot_Type.__name__ = "Integer32"
_CpqHeAsrReboot_Object = MibScalar
cpqHeAsrReboot = _CpqHeAsrReboot_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 8),
    _CpqHeAsrReboot_Type()
)
cpqHeAsrReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrReboot.setStatus("mandatory")
_CpqHeAsrRebootLimit_Type = Integer32
_CpqHeAsrRebootLimit_Object = MibScalar
cpqHeAsrRebootLimit = _CpqHeAsrRebootLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 9),
    _CpqHeAsrRebootLimit_Type()
)
cpqHeAsrRebootLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrRebootLimit.setStatus("mandatory")
_CpqHeAsrRebootCount_Type = Integer32
_CpqHeAsrRebootCount_Object = MibScalar
cpqHeAsrRebootCount = _CpqHeAsrRebootCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 10),
    _CpqHeAsrRebootCount_Type()
)
cpqHeAsrRebootCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrRebootCount.setStatus("mandatory")


class _CpqHeAsrPagerStatus_Type(Integer32):
    """Custom type cpqHeAsrPagerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqHeAsrPagerStatus_Type.__name__ = "Integer32"
_CpqHeAsrPagerStatus_Object = MibScalar
cpqHeAsrPagerStatus = _CpqHeAsrPagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 11),
    _CpqHeAsrPagerStatus_Type()
)
cpqHeAsrPagerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrPagerStatus.setStatus("mandatory")


class _CpqHeAsrPagerNumber_Type(DisplayString):
    """Custom type cpqHeAsrPagerNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_CpqHeAsrPagerNumber_Type.__name__ = "DisplayString"
_CpqHeAsrPagerNumber_Object = MibScalar
cpqHeAsrPagerNumber = _CpqHeAsrPagerNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 12),
    _CpqHeAsrPagerNumber_Type()
)
cpqHeAsrPagerNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrPagerNumber.setStatus("mandatory")
_CpqHeAsrCommPort_Type = Integer32
_CpqHeAsrCommPort_Object = MibScalar
cpqHeAsrCommPort = _CpqHeAsrCommPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 13),
    _CpqHeAsrCommPort_Type()
)
cpqHeAsrCommPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrCommPort.setStatus("mandatory")
_CpqHeAsrBaudRate_Type = Integer32
_CpqHeAsrBaudRate_Object = MibScalar
cpqHeAsrBaudRate = _CpqHeAsrBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 14),
    _CpqHeAsrBaudRate_Type()
)
cpqHeAsrBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeAsrBaudRate.setStatus("mandatory")


class _CpqHeAsrPagerMessage_Type(DisplayString):
    """Custom type cpqHeAsrPagerMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqHeAsrPagerMessage_Type.__name__ = "DisplayString"
_CpqHeAsrPagerMessage_Object = MibScalar
cpqHeAsrPagerMessage = _CpqHeAsrPagerMessage_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 15),
    _CpqHeAsrPagerMessage_Type()
)
cpqHeAsrPagerMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrPagerMessage.setStatus("mandatory")


class _CpqHeAsrBootFail_Type(Integer32):
    """Custom type cpqHeAsrBootFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interrupt18", 2),
          ("other", 1))
    )


_CpqHeAsrBootFail_Type.__name__ = "Integer32"
_CpqHeAsrBootFail_Object = MibScalar
cpqHeAsrBootFail = _CpqHeAsrBootFail_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 16),
    _CpqHeAsrBootFail_Type()
)
cpqHeAsrBootFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeAsrBootFail.setStatus("deprecated")


class _CpqHeAsrCondition_Type(Integer32):
    """Custom type cpqHeAsrCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeAsrCondition_Type.__name__ = "Integer32"
_CpqHeAsrCondition_Object = MibScalar
cpqHeAsrCondition = _CpqHeAsrCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 17),
    _CpqHeAsrCondition_Type()
)
cpqHeAsrCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeAsrCondition.setStatus("mandatory")


class _CpqHeAsrDialInStatus_Type(Integer32):
    """Custom type cpqHeAsrDialInStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqHeAsrDialInStatus_Type.__name__ = "Integer32"
_CpqHeAsrDialInStatus_Object = MibScalar
cpqHeAsrDialInStatus = _CpqHeAsrDialInStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 18),
    _CpqHeAsrDialInStatus_Type()
)
cpqHeAsrDialInStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrDialInStatus.setStatus("mandatory")


class _CpqHeAsrDialOutStatus_Type(Integer32):
    """Custom type cpqHeAsrDialOutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqHeAsrDialOutStatus_Type.__name__ = "Integer32"
_CpqHeAsrDialOutStatus_Object = MibScalar
cpqHeAsrDialOutStatus = _CpqHeAsrDialOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 19),
    _CpqHeAsrDialOutStatus_Type()
)
cpqHeAsrDialOutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrDialOutStatus.setStatus("mandatory")


class _CpqHeAsrDialOutNumber_Type(DisplayString):
    """Custom type cpqHeAsrDialOutNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_CpqHeAsrDialOutNumber_Type.__name__ = "DisplayString"
_CpqHeAsrDialOutNumber_Object = MibScalar
cpqHeAsrDialOutNumber = _CpqHeAsrDialOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 20),
    _CpqHeAsrDialOutNumber_Type()
)
cpqHeAsrDialOutNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrDialOutNumber.setStatus("mandatory")


class _CpqHeAsrNetworkAccessStatus_Type(Integer32):
    """Custom type cpqHeAsrNetworkAccessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqHeAsrNetworkAccessStatus_Type.__name__ = "Integer32"
_CpqHeAsrNetworkAccessStatus_Object = MibScalar
cpqHeAsrNetworkAccessStatus = _CpqHeAsrNetworkAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 21),
    _CpqHeAsrNetworkAccessStatus_Type()
)
cpqHeAsrNetworkAccessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrNetworkAccessStatus.setStatus("mandatory")
_CpqHeAsrPollTime_Type = Integer32
_CpqHeAsrPollTime_Object = MibScalar
cpqHeAsrPollTime = _CpqHeAsrPollTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 5, 22),
    _CpqHeAsrPollTime_Type()
)
cpqHeAsrPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeAsrPollTime.setStatus("optional")
_CpqHeThermal_ObjectIdentity = ObjectIdentity
cpqHeThermal = _CpqHeThermal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6)
)


class _CpqHeThermalCondition_Type(Integer32):
    """Custom type cpqHeThermalCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeThermalCondition_Type.__name__ = "Integer32"
_CpqHeThermalCondition_Object = MibScalar
cpqHeThermalCondition = _CpqHeThermalCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 1),
    _CpqHeThermalCondition_Type()
)
cpqHeThermalCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalCondition.setStatus("mandatory")


class _CpqHeThermalDegradedAction_Type(Integer32):
    """Custom type cpqHeThermalDegradedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continue", 2),
          ("other", 1),
          ("shutdown", 3))
    )


_CpqHeThermalDegradedAction_Type.__name__ = "Integer32"
_CpqHeThermalDegradedAction_Object = MibScalar
cpqHeThermalDegradedAction = _CpqHeThermalDegradedAction_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 2),
    _CpqHeThermalDegradedAction_Type()
)
cpqHeThermalDegradedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeThermalDegradedAction.setStatus("mandatory")


class _CpqHeThermalTempStatus_Type(Integer32):
    """Custom type cpqHeThermalTempStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeThermalTempStatus_Type.__name__ = "Integer32"
_CpqHeThermalTempStatus_Object = MibScalar
cpqHeThermalTempStatus = _CpqHeThermalTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 3),
    _CpqHeThermalTempStatus_Type()
)
cpqHeThermalTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalTempStatus.setStatus("mandatory")


class _CpqHeThermalSystemFanStatus_Type(Integer32):
    """Custom type cpqHeThermalSystemFanStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeThermalSystemFanStatus_Type.__name__ = "Integer32"
_CpqHeThermalSystemFanStatus_Object = MibScalar
cpqHeThermalSystemFanStatus = _CpqHeThermalSystemFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 4),
    _CpqHeThermalSystemFanStatus_Type()
)
cpqHeThermalSystemFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalSystemFanStatus.setStatus("mandatory")


class _CpqHeThermalCpuFanStatus_Type(Integer32):
    """Custom type cpqHeThermalCpuFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeThermalCpuFanStatus_Type.__name__ = "Integer32"
_CpqHeThermalCpuFanStatus_Object = MibScalar
cpqHeThermalCpuFanStatus = _CpqHeThermalCpuFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 5),
    _CpqHeThermalCpuFanStatus_Type()
)
cpqHeThermalCpuFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalCpuFanStatus.setStatus("mandatory")
_CpqHeThermalFanTable_Object = MibTable
cpqHeThermalFanTable = _CpqHeThermalFanTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 6)
)
if mibBuilder.loadTexts:
    cpqHeThermalFanTable.setStatus("mandatory")
_CpqHeThermalFanEntry_Object = MibTableRow
cpqHeThermalFanEntry = _CpqHeThermalFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 6, 1)
)
cpqHeThermalFanEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeThermalFanIndex"),
)
if mibBuilder.loadTexts:
    cpqHeThermalFanEntry.setStatus("mandatory")


class _CpqHeThermalFanIndex_Type(Integer32):
    """Custom type cpqHeThermalFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CpqHeThermalFanIndex_Type.__name__ = "Integer32"
_CpqHeThermalFanIndex_Object = MibTableColumn
cpqHeThermalFanIndex = _CpqHeThermalFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 6, 1, 1),
    _CpqHeThermalFanIndex_Type()
)
cpqHeThermalFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalFanIndex.setStatus("mandatory")


class _CpqHeThermalFanRequired_Type(Integer32):
    """Custom type cpqHeThermalFanRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonRequired", 2),
          ("other", 1),
          ("required", 3))
    )


_CpqHeThermalFanRequired_Type.__name__ = "Integer32"
_CpqHeThermalFanRequired_Object = MibTableColumn
cpqHeThermalFanRequired = _CpqHeThermalFanRequired_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 6, 1, 2),
    _CpqHeThermalFanRequired_Type()
)
cpqHeThermalFanRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalFanRequired.setStatus("mandatory")


class _CpqHeThermalFanPresent_Type(Integer32):
    """Custom type cpqHeThermalFanPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqHeThermalFanPresent_Type.__name__ = "Integer32"
_CpqHeThermalFanPresent_Object = MibTableColumn
cpqHeThermalFanPresent = _CpqHeThermalFanPresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 6, 1, 3),
    _CpqHeThermalFanPresent_Type()
)
cpqHeThermalFanPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalFanPresent.setStatus("mandatory")


class _CpqHeThermalFanCpuFan_Type(Integer32):
    """Custom type cpqHeThermalFanCpuFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpuFan", 3),
          ("other", 1),
          ("systemFan", 2))
    )


_CpqHeThermalFanCpuFan_Type.__name__ = "Integer32"
_CpqHeThermalFanCpuFan_Object = MibTableColumn
cpqHeThermalFanCpuFan = _CpqHeThermalFanCpuFan_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 6, 1, 4),
    _CpqHeThermalFanCpuFan_Type()
)
cpqHeThermalFanCpuFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalFanCpuFan.setStatus("mandatory")


class _CpqHeThermalFanStatus_Type(Integer32):
    """Custom type cpqHeThermalFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeThermalFanStatus_Type.__name__ = "Integer32"
_CpqHeThermalFanStatus_Object = MibTableColumn
cpqHeThermalFanStatus = _CpqHeThermalFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 6, 1, 5),
    _CpqHeThermalFanStatus_Type()
)
cpqHeThermalFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalFanStatus.setStatus("mandatory")


class _CpqHeThermalFanHwLocation_Type(DisplayString):
    """Custom type cpqHeThermalFanHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeThermalFanHwLocation_Type.__name__ = "DisplayString"
_CpqHeThermalFanHwLocation_Object = MibTableColumn
cpqHeThermalFanHwLocation = _CpqHeThermalFanHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 6, 1, 6),
    _CpqHeThermalFanHwLocation_Type()
)
cpqHeThermalFanHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalFanHwLocation.setStatus("optional")
_CpqHeThermalFanCurrentSpeed_Type = Integer32
_CpqHeThermalFanCurrentSpeed_Object = MibTableColumn
cpqHeThermalFanCurrentSpeed = _CpqHeThermalFanCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 6, 1, 7),
    _CpqHeThermalFanCurrentSpeed_Type()
)
cpqHeThermalFanCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeThermalFanCurrentSpeed.setStatus("optional")
_CpqHeFltTolFanTable_Object = MibTable
cpqHeFltTolFanTable = _CpqHeFltTolFanTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7)
)
if mibBuilder.loadTexts:
    cpqHeFltTolFanTable.setStatus("mandatory")
_CpqHeFltTolFanEntry_Object = MibTableRow
cpqHeFltTolFanEntry = _CpqHeFltTolFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1)
)
cpqHeFltTolFanEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeFltTolFanChassis"),
    (0, "CPQHLTH-MIB", "cpqHeFltTolFanIndex"),
)
if mibBuilder.loadTexts:
    cpqHeFltTolFanEntry.setStatus("mandatory")
_CpqHeFltTolFanChassis_Type = Integer32
_CpqHeFltTolFanChassis_Object = MibTableColumn
cpqHeFltTolFanChassis = _CpqHeFltTolFanChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 1),
    _CpqHeFltTolFanChassis_Type()
)
cpqHeFltTolFanChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanChassis.setStatus("mandatory")
_CpqHeFltTolFanIndex_Type = Integer32
_CpqHeFltTolFanIndex_Object = MibTableColumn
cpqHeFltTolFanIndex = _CpqHeFltTolFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 2),
    _CpqHeFltTolFanIndex_Type()
)
cpqHeFltTolFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanIndex.setStatus("mandatory")


class _CpqHeFltTolFanLocale_Type(Integer32):
    """Custom type cpqHeFltTolFanLocale based on Integer32"""
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
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("ambient", 11),
          ("backplane", 15),
          ("bladeSlot", 17),
          ("bridgeCard", 13),
          ("chassis", 12),
          ("cpu", 6),
          ("ioBoard", 5),
          ("managementBoard", 14),
          ("memory", 7),
          ("networkSlot", 16),
          ("other", 1),
          ("powerSupply", 10),
          ("removableMedia", 9),
          ("storage", 8),
          ("system", 3),
          ("systemBoard", 4),
          ("unknown", 2),
          ("virtual", 18))
    )


_CpqHeFltTolFanLocale_Type.__name__ = "Integer32"
_CpqHeFltTolFanLocale_Object = MibTableColumn
cpqHeFltTolFanLocale = _CpqHeFltTolFanLocale_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 3),
    _CpqHeFltTolFanLocale_Type()
)
cpqHeFltTolFanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanLocale.setStatus("mandatory")


class _CpqHeFltTolFanPresent_Type(Integer32):
    """Custom type cpqHeFltTolFanPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqHeFltTolFanPresent_Type.__name__ = "Integer32"
_CpqHeFltTolFanPresent_Object = MibTableColumn
cpqHeFltTolFanPresent = _CpqHeFltTolFanPresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 4),
    _CpqHeFltTolFanPresent_Type()
)
cpqHeFltTolFanPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanPresent.setStatus("mandatory")


class _CpqHeFltTolFanType_Type(Integer32):
    """Custom type cpqHeFltTolFanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("spinDetect", 3),
          ("tachOutput", 2))
    )


_CpqHeFltTolFanType_Type.__name__ = "Integer32"
_CpqHeFltTolFanType_Object = MibTableColumn
cpqHeFltTolFanType = _CpqHeFltTolFanType_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 5),
    _CpqHeFltTolFanType_Type()
)
cpqHeFltTolFanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanType.setStatus("mandatory")


class _CpqHeFltTolFanSpeed_Type(Integer32):
    """Custom type cpqHeFltTolFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("normal", 2),
          ("other", 1))
    )


_CpqHeFltTolFanSpeed_Type.__name__ = "Integer32"
_CpqHeFltTolFanSpeed_Object = MibTableColumn
cpqHeFltTolFanSpeed = _CpqHeFltTolFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 6),
    _CpqHeFltTolFanSpeed_Type()
)
cpqHeFltTolFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanSpeed.setStatus("mandatory")


class _CpqHeFltTolFanRedundant_Type(Integer32):
    """Custom type cpqHeFltTolFanRedundant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRedundant", 2),
          ("other", 1),
          ("redundant", 3))
    )


_CpqHeFltTolFanRedundant_Type.__name__ = "Integer32"
_CpqHeFltTolFanRedundant_Object = MibTableColumn
cpqHeFltTolFanRedundant = _CpqHeFltTolFanRedundant_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 7),
    _CpqHeFltTolFanRedundant_Type()
)
cpqHeFltTolFanRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanRedundant.setStatus("mandatory")
_CpqHeFltTolFanRedundantPartner_Type = Integer32
_CpqHeFltTolFanRedundantPartner_Object = MibTableColumn
cpqHeFltTolFanRedundantPartner = _CpqHeFltTolFanRedundantPartner_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 8),
    _CpqHeFltTolFanRedundantPartner_Type()
)
cpqHeFltTolFanRedundantPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanRedundantPartner.setStatus("mandatory")


class _CpqHeFltTolFanCondition_Type(Integer32):
    """Custom type cpqHeFltTolFanCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeFltTolFanCondition_Type.__name__ = "Integer32"
_CpqHeFltTolFanCondition_Object = MibTableColumn
cpqHeFltTolFanCondition = _CpqHeFltTolFanCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 9),
    _CpqHeFltTolFanCondition_Type()
)
cpqHeFltTolFanCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanCondition.setStatus("mandatory")


class _CpqHeFltTolFanHotPlug_Type(Integer32):
    """Custom type cpqHeFltTolFanHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotPluggable", 3),
          ("nonHotPluggable", 2),
          ("other", 1))
    )


_CpqHeFltTolFanHotPlug_Type.__name__ = "Integer32"
_CpqHeFltTolFanHotPlug_Object = MibTableColumn
cpqHeFltTolFanHotPlug = _CpqHeFltTolFanHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 10),
    _CpqHeFltTolFanHotPlug_Type()
)
cpqHeFltTolFanHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanHotPlug.setStatus("mandatory")


class _CpqHeFltTolFanHwLocation_Type(DisplayString):
    """Custom type cpqHeFltTolFanHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeFltTolFanHwLocation_Type.__name__ = "DisplayString"
_CpqHeFltTolFanHwLocation_Object = MibTableColumn
cpqHeFltTolFanHwLocation = _CpqHeFltTolFanHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 11),
    _CpqHeFltTolFanHwLocation_Type()
)
cpqHeFltTolFanHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanHwLocation.setStatus("optional")
_CpqHeFltTolFanCurrentSpeed_Type = Integer32
_CpqHeFltTolFanCurrentSpeed_Object = MibTableColumn
cpqHeFltTolFanCurrentSpeed = _CpqHeFltTolFanCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 7, 1, 12),
    _CpqHeFltTolFanCurrentSpeed_Type()
)
cpqHeFltTolFanCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolFanCurrentSpeed.setStatus("optional")
_CpqHeTemperatureTable_Object = MibTable
cpqHeTemperatureTable = _CpqHeTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 8)
)
if mibBuilder.loadTexts:
    cpqHeTemperatureTable.setStatus("mandatory")
_CpqHeTemperatureEntry_Object = MibTableRow
cpqHeTemperatureEntry = _CpqHeTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 8, 1)
)
cpqHeTemperatureEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeTemperatureChassis"),
    (0, "CPQHLTH-MIB", "cpqHeTemperatureIndex"),
)
if mibBuilder.loadTexts:
    cpqHeTemperatureEntry.setStatus("mandatory")
_CpqHeTemperatureChassis_Type = Integer32
_CpqHeTemperatureChassis_Object = MibTableColumn
cpqHeTemperatureChassis = _CpqHeTemperatureChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 8, 1, 1),
    _CpqHeTemperatureChassis_Type()
)
cpqHeTemperatureChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTemperatureChassis.setStatus("mandatory")
_CpqHeTemperatureIndex_Type = Integer32
_CpqHeTemperatureIndex_Object = MibTableColumn
cpqHeTemperatureIndex = _CpqHeTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 8, 1, 2),
    _CpqHeTemperatureIndex_Type()
)
cpqHeTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTemperatureIndex.setStatus("mandatory")


class _CpqHeTemperatureLocale_Type(Integer32):
    """Custom type cpqHeTemperatureLocale based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("ambient", 11),
          ("bridgeCard", 13),
          ("chassis", 12),
          ("cpu", 6),
          ("ioBoard", 5),
          ("memory", 7),
          ("other", 1),
          ("powerSupply", 10),
          ("removableMedia", 9),
          ("storage", 8),
          ("system", 3),
          ("systemBoard", 4),
          ("unknown", 2))
    )


_CpqHeTemperatureLocale_Type.__name__ = "Integer32"
_CpqHeTemperatureLocale_Object = MibTableColumn
cpqHeTemperatureLocale = _CpqHeTemperatureLocale_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 8, 1, 3),
    _CpqHeTemperatureLocale_Type()
)
cpqHeTemperatureLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTemperatureLocale.setStatus("mandatory")
_CpqHeTemperatureCelsius_Type = Integer32
_CpqHeTemperatureCelsius_Object = MibTableColumn
cpqHeTemperatureCelsius = _CpqHeTemperatureCelsius_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 8, 1, 4),
    _CpqHeTemperatureCelsius_Type()
)
cpqHeTemperatureCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTemperatureCelsius.setStatus("mandatory")
_CpqHeTemperatureThreshold_Type = Integer32
_CpqHeTemperatureThreshold_Object = MibTableColumn
cpqHeTemperatureThreshold = _CpqHeTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 8, 1, 5),
    _CpqHeTemperatureThreshold_Type()
)
cpqHeTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeTemperatureThreshold.setStatus("mandatory")


class _CpqHeTemperatureCondition_Type(Integer32):
    """Custom type cpqHeTemperatureCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeTemperatureCondition_Type.__name__ = "Integer32"
_CpqHeTemperatureCondition_Object = MibTableColumn
cpqHeTemperatureCondition = _CpqHeTemperatureCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 8, 1, 6),
    _CpqHeTemperatureCondition_Type()
)
cpqHeTemperatureCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTemperatureCondition.setStatus("mandatory")


class _CpqHeTemperatureThresholdType_Type(Integer32):
    """Custom type cpqHeTemperatureThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              9,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("blowout", 5),
          ("caution", 9),
          ("critical", 15),
          ("noreaction", 16),
          ("other", 1))
    )


_CpqHeTemperatureThresholdType_Type.__name__ = "Integer32"
_CpqHeTemperatureThresholdType_Object = MibTableColumn
cpqHeTemperatureThresholdType = _CpqHeTemperatureThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 8, 1, 7),
    _CpqHeTemperatureThresholdType_Type()
)
cpqHeTemperatureThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTemperatureThresholdType.setStatus("mandatory")


class _CpqHeTemperatureHwLocation_Type(DisplayString):
    """Custom type cpqHeTemperatureHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeTemperatureHwLocation_Type.__name__ = "DisplayString"
_CpqHeTemperatureHwLocation_Object = MibTableColumn
cpqHeTemperatureHwLocation = _CpqHeTemperatureHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 6, 8, 1, 8),
    _CpqHeTemperatureHwLocation_Type()
)
cpqHeTemperatureHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTemperatureHwLocation.setStatus("optional")
_CpqHePostMsg_ObjectIdentity = ObjectIdentity
cpqHePostMsg = _CpqHePostMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 7)
)


class _CpqHePostMsgCondition_Type(Integer32):
    """Custom type cpqHePostMsgCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHePostMsgCondition_Type.__name__ = "Integer32"
_CpqHePostMsgCondition_Object = MibScalar
cpqHePostMsgCondition = _CpqHePostMsgCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 7, 1),
    _CpqHePostMsgCondition_Type()
)
cpqHePostMsgCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePostMsgCondition.setStatus("mandatory")
_CpqHePostMsgTable_Object = MibTable
cpqHePostMsgTable = _CpqHePostMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 7, 2)
)
if mibBuilder.loadTexts:
    cpqHePostMsgTable.setStatus("mandatory")
_CpqHePostMsgEntry_Object = MibTableRow
cpqHePostMsgEntry = _CpqHePostMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 7, 2, 1)
)
cpqHePostMsgEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHePostMsgIndex"),
)
if mibBuilder.loadTexts:
    cpqHePostMsgEntry.setStatus("mandatory")


class _CpqHePostMsgIndex_Type(Integer32):
    """Custom type cpqHePostMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHePostMsgIndex_Type.__name__ = "Integer32"
_CpqHePostMsgIndex_Object = MibTableColumn
cpqHePostMsgIndex = _CpqHePostMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 7, 2, 1, 1),
    _CpqHePostMsgIndex_Type()
)
cpqHePostMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePostMsgIndex.setStatus("mandatory")


class _CpqHePostMsgCode_Type(Integer32):
    """Custom type cpqHePostMsgCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHePostMsgCode_Type.__name__ = "Integer32"
_CpqHePostMsgCode_Object = MibTableColumn
cpqHePostMsgCode = _CpqHePostMsgCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 7, 2, 1, 2),
    _CpqHePostMsgCode_Type()
)
cpqHePostMsgCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePostMsgCode.setStatus("mandatory")


class _CpqHePostMsgDesc_Type(DisplayString):
    """Custom type cpqHePostMsgDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHePostMsgDesc_Type.__name__ = "DisplayString"
_CpqHePostMsgDesc_Object = MibTableColumn
cpqHePostMsgDesc = _CpqHePostMsgDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 7, 2, 1, 3),
    _CpqHePostMsgDesc_Type()
)
cpqHePostMsgDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePostMsgDesc.setStatus("mandatory")


class _CpqHePostMsgEv_Type(OctetString):
    """Custom type cpqHePostMsgEv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqHePostMsgEv_Type.__name__ = "OctetString"
_CpqHePostMsgEv_Object = MibScalar
cpqHePostMsgEv = _CpqHePostMsgEv_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 7, 3),
    _CpqHePostMsgEv_Type()
)
cpqHePostMsgEv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHePostMsgEv.setStatus("mandatory")
_CpqHeSysUtil_ObjectIdentity = ObjectIdentity
cpqHeSysUtil = _CpqHeSysUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8)
)


class _CpqHeSysUtilLifeTime_Type(Integer32):
    """Custom type cpqHeSysUtilLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqHeSysUtilLifeTime_Type.__name__ = "Integer32"
_CpqHeSysUtilLifeTime_Object = MibScalar
cpqHeSysUtilLifeTime = _CpqHeSysUtilLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 1),
    _CpqHeSysUtilLifeTime_Type()
)
cpqHeSysUtilLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilLifeTime.setStatus("mandatory")
_CpqHeSysUtilEisaBusMin_Type = Integer32
_CpqHeSysUtilEisaBusMin_Object = MibScalar
cpqHeSysUtilEisaBusMin = _CpqHeSysUtilEisaBusMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 2),
    _CpqHeSysUtilEisaBusMin_Type()
)
cpqHeSysUtilEisaBusMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilEisaBusMin.setStatus("mandatory")
_CpqHeSysUtilEisaBusFiveMin_Type = Integer32
_CpqHeSysUtilEisaBusFiveMin_Object = MibScalar
cpqHeSysUtilEisaBusFiveMin = _CpqHeSysUtilEisaBusFiveMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 3),
    _CpqHeSysUtilEisaBusFiveMin_Type()
)
cpqHeSysUtilEisaBusFiveMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilEisaBusFiveMin.setStatus("mandatory")
_CpqHeSysUtilEisaBusThirtyMin_Type = Integer32
_CpqHeSysUtilEisaBusThirtyMin_Object = MibScalar
cpqHeSysUtilEisaBusThirtyMin = _CpqHeSysUtilEisaBusThirtyMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 4),
    _CpqHeSysUtilEisaBusThirtyMin_Type()
)
cpqHeSysUtilEisaBusThirtyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilEisaBusThirtyMin.setStatus("mandatory")
_CpqHeSysUtilEisaBusHour_Type = Integer32
_CpqHeSysUtilEisaBusHour_Object = MibScalar
cpqHeSysUtilEisaBusHour = _CpqHeSysUtilEisaBusHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 5),
    _CpqHeSysUtilEisaBusHour_Type()
)
cpqHeSysUtilEisaBusHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilEisaBusHour.setStatus("mandatory")
_CpqHeSysUtilPciTable_Object = MibTable
cpqHeSysUtilPciTable = _CpqHeSysUtilPciTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 6)
)
if mibBuilder.loadTexts:
    cpqHeSysUtilPciTable.setStatus("mandatory")
_CpqHeSysUtilPciEntry_Object = MibTableRow
cpqHeSysUtilPciEntry = _CpqHeSysUtilPciEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 6, 1)
)
cpqHeSysUtilPciEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeSysUtilPciIndex"),
)
if mibBuilder.loadTexts:
    cpqHeSysUtilPciEntry.setStatus("mandatory")


class _CpqHeSysUtilPciIndex_Type(Integer32):
    """Custom type cpqHeSysUtilPciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHeSysUtilPciIndex_Type.__name__ = "Integer32"
_CpqHeSysUtilPciIndex_Object = MibTableColumn
cpqHeSysUtilPciIndex = _CpqHeSysUtilPciIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 6, 1, 1),
    _CpqHeSysUtilPciIndex_Type()
)
cpqHeSysUtilPciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilPciIndex.setStatus("mandatory")


class _CpqHeSysUtilPciBus_Type(Integer32):
    """Custom type cpqHeSysUtilPciBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHeSysUtilPciBus_Type.__name__ = "Integer32"
_CpqHeSysUtilPciBus_Object = MibTableColumn
cpqHeSysUtilPciBus = _CpqHeSysUtilPciBus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 6, 1, 2),
    _CpqHeSysUtilPciBus_Type()
)
cpqHeSysUtilPciBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilPciBus.setStatus("mandatory")
_CpqHeSysUtilPciDevice_Type = Integer32
_CpqHeSysUtilPciDevice_Object = MibTableColumn
cpqHeSysUtilPciDevice = _CpqHeSysUtilPciDevice_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 6, 1, 3),
    _CpqHeSysUtilPciDevice_Type()
)
cpqHeSysUtilPciDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilPciDevice.setStatus("mandatory")
_CpqHeSysUtilPciMin_Type = Integer32
_CpqHeSysUtilPciMin_Object = MibTableColumn
cpqHeSysUtilPciMin = _CpqHeSysUtilPciMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 6, 1, 4),
    _CpqHeSysUtilPciMin_Type()
)
cpqHeSysUtilPciMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilPciMin.setStatus("mandatory")
_CpqHeSysUtilPciFiveMin_Type = Integer32
_CpqHeSysUtilPciFiveMin_Object = MibTableColumn
cpqHeSysUtilPciFiveMin = _CpqHeSysUtilPciFiveMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 6, 1, 5),
    _CpqHeSysUtilPciFiveMin_Type()
)
cpqHeSysUtilPciFiveMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilPciFiveMin.setStatus("mandatory")
_CpqHeSysUtilPciThirtyMin_Type = Integer32
_CpqHeSysUtilPciThirtyMin_Object = MibTableColumn
cpqHeSysUtilPciThirtyMin = _CpqHeSysUtilPciThirtyMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 6, 1, 6),
    _CpqHeSysUtilPciThirtyMin_Type()
)
cpqHeSysUtilPciThirtyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilPciThirtyMin.setStatus("mandatory")
_CpqHeSysUtilPciHour_Type = Integer32
_CpqHeSysUtilPciHour_Object = MibTableColumn
cpqHeSysUtilPciHour = _CpqHeSysUtilPciHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 6, 1, 7),
    _CpqHeSysUtilPciHour_Type()
)
cpqHeSysUtilPciHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilPciHour.setStatus("mandatory")


class _CpqHeSysUtilPciHwLocation_Type(DisplayString):
    """Custom type cpqHeSysUtilPciHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeSysUtilPciHwLocation_Type.__name__ = "DisplayString"
_CpqHeSysUtilPciHwLocation_Object = MibTableColumn
cpqHeSysUtilPciHwLocation = _CpqHeSysUtilPciHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 8, 6, 1, 8),
    _CpqHeSysUtilPciHwLocation_Type()
)
cpqHeSysUtilPciHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeSysUtilPciHwLocation.setStatus("optional")
_CpqHeFltTolPwrSupply_ObjectIdentity = ObjectIdentity
cpqHeFltTolPwrSupply = _CpqHeFltTolPwrSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9)
)


class _CpqHeFltTolPwrSupplyCondition_Type(Integer32):
    """Custom type cpqHeFltTolPwrSupplyCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeFltTolPwrSupplyCondition_Type.__name__ = "Integer32"
_CpqHeFltTolPwrSupplyCondition_Object = MibScalar
cpqHeFltTolPwrSupplyCondition = _CpqHeFltTolPwrSupplyCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 1),
    _CpqHeFltTolPwrSupplyCondition_Type()
)
cpqHeFltTolPwrSupplyCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPwrSupplyCondition.setStatus("mandatory")


class _CpqHeFltTolPwrSupplyStatus_Type(Integer32):
    """Custom type cpqHeFltTolPwrSupplyStatus based on Integer32"""
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
        *(("installed", 4),
          ("notInstalled", 3),
          ("notSupported", 2),
          ("other", 1))
    )


_CpqHeFltTolPwrSupplyStatus_Type.__name__ = "Integer32"
_CpqHeFltTolPwrSupplyStatus_Object = MibScalar
cpqHeFltTolPwrSupplyStatus = _CpqHeFltTolPwrSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 2),
    _CpqHeFltTolPwrSupplyStatus_Type()
)
cpqHeFltTolPwrSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPwrSupplyStatus.setStatus("mandatory")
_CpqHeFltTolPowerSupplyTable_Object = MibTable
cpqHeFltTolPowerSupplyTable = _CpqHeFltTolPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3)
)
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyTable.setStatus("mandatory")
_CpqHeFltTolPowerSupplyEntry_Object = MibTableRow
cpqHeFltTolPowerSupplyEntry = _CpqHeFltTolPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1)
)
cpqHeFltTolPowerSupplyEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"),
    (0, "CPQHLTH-MIB", "cpqHeFltTolPowerSupplyBay"),
)
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyEntry.setStatus("mandatory")
_CpqHeFltTolPowerSupplyChassis_Type = Integer32
_CpqHeFltTolPowerSupplyChassis_Object = MibTableColumn
cpqHeFltTolPowerSupplyChassis = _CpqHeFltTolPowerSupplyChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 1),
    _CpqHeFltTolPowerSupplyChassis_Type()
)
cpqHeFltTolPowerSupplyChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyChassis.setStatus("mandatory")
_CpqHeFltTolPowerSupplyBay_Type = Integer32
_CpqHeFltTolPowerSupplyBay_Object = MibTableColumn
cpqHeFltTolPowerSupplyBay = _CpqHeFltTolPowerSupplyBay_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 2),
    _CpqHeFltTolPowerSupplyBay_Type()
)
cpqHeFltTolPowerSupplyBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyBay.setStatus("mandatory")


class _CpqHeFltTolPowerSupplyPresent_Type(Integer32):
    """Custom type cpqHeFltTolPowerSupplyPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqHeFltTolPowerSupplyPresent_Type.__name__ = "Integer32"
_CpqHeFltTolPowerSupplyPresent_Object = MibTableColumn
cpqHeFltTolPowerSupplyPresent = _CpqHeFltTolPowerSupplyPresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 3),
    _CpqHeFltTolPowerSupplyPresent_Type()
)
cpqHeFltTolPowerSupplyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyPresent.setStatus("mandatory")


class _CpqHeFltTolPowerSupplyCondition_Type(Integer32):
    """Custom type cpqHeFltTolPowerSupplyCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeFltTolPowerSupplyCondition_Type.__name__ = "Integer32"
_CpqHeFltTolPowerSupplyCondition_Object = MibTableColumn
cpqHeFltTolPowerSupplyCondition = _CpqHeFltTolPowerSupplyCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 4),
    _CpqHeFltTolPowerSupplyCondition_Type()
)
cpqHeFltTolPowerSupplyCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyCondition.setStatus("mandatory")


class _CpqHeFltTolPowerSupplyStatus_Type(Integer32):
    """Custom type cpqHeFltTolPowerSupplyStatus based on Integer32"""
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
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bistFailure", 3),
          ("brownOut", 13),
          ("calibrationTableInvalid", 16),
          ("dacFailed", 9),
          ("epromFailed", 7),
          ("fanFailure", 4),
          ("generalFailure", 2),
          ("giveupOnStartup", 14),
          ("interlockOpen", 6),
          ("noError", 1),
          ("nvramInvalid", 15),
          ("orringdiodeFailed", 12),
          ("ramTestFailed", 10),
          ("tempFailure", 5),
          ("voltageChannelFailed", 11),
          ("vrefFailed", 8))
    )


_CpqHeFltTolPowerSupplyStatus_Type.__name__ = "Integer32"
_CpqHeFltTolPowerSupplyStatus_Object = MibTableColumn
cpqHeFltTolPowerSupplyStatus = _CpqHeFltTolPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 5),
    _CpqHeFltTolPowerSupplyStatus_Type()
)
cpqHeFltTolPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyStatus.setStatus("mandatory")
_CpqHeFltTolPowerSupplyMainVoltage_Type = Integer32
_CpqHeFltTolPowerSupplyMainVoltage_Object = MibTableColumn
cpqHeFltTolPowerSupplyMainVoltage = _CpqHeFltTolPowerSupplyMainVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 6),
    _CpqHeFltTolPowerSupplyMainVoltage_Type()
)
cpqHeFltTolPowerSupplyMainVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyMainVoltage.setStatus("mandatory")
_CpqHeFltTolPowerSupplyCapacityUsed_Type = Integer32
_CpqHeFltTolPowerSupplyCapacityUsed_Object = MibTableColumn
cpqHeFltTolPowerSupplyCapacityUsed = _CpqHeFltTolPowerSupplyCapacityUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 7),
    _CpqHeFltTolPowerSupplyCapacityUsed_Type()
)
cpqHeFltTolPowerSupplyCapacityUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyCapacityUsed.setStatus("mandatory")
_CpqHeFltTolPowerSupplyCapacityMaximum_Type = Integer32
_CpqHeFltTolPowerSupplyCapacityMaximum_Object = MibTableColumn
cpqHeFltTolPowerSupplyCapacityMaximum = _CpqHeFltTolPowerSupplyCapacityMaximum_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 8),
    _CpqHeFltTolPowerSupplyCapacityMaximum_Type()
)
cpqHeFltTolPowerSupplyCapacityMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyCapacityMaximum.setStatus("mandatory")


class _CpqHeFltTolPowerSupplyRedundant_Type(Integer32):
    """Custom type cpqHeFltTolPowerSupplyRedundant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRedundant", 2),
          ("other", 1),
          ("redundant", 3))
    )


_CpqHeFltTolPowerSupplyRedundant_Type.__name__ = "Integer32"
_CpqHeFltTolPowerSupplyRedundant_Object = MibTableColumn
cpqHeFltTolPowerSupplyRedundant = _CpqHeFltTolPowerSupplyRedundant_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 9),
    _CpqHeFltTolPowerSupplyRedundant_Type()
)
cpqHeFltTolPowerSupplyRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyRedundant.setStatus("mandatory")


class _CpqHeFltTolPowerSupplyModel_Type(DisplayString):
    """Custom type cpqHeFltTolPowerSupplyModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqHeFltTolPowerSupplyModel_Type.__name__ = "DisplayString"
_CpqHeFltTolPowerSupplyModel_Object = MibTableColumn
cpqHeFltTolPowerSupplyModel = _CpqHeFltTolPowerSupplyModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 10),
    _CpqHeFltTolPowerSupplyModel_Type()
)
cpqHeFltTolPowerSupplyModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyModel.setStatus("mandatory")


class _CpqHeFltTolPowerSupplySerialNumber_Type(DisplayString):
    """Custom type cpqHeFltTolPowerSupplySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqHeFltTolPowerSupplySerialNumber_Type.__name__ = "DisplayString"
_CpqHeFltTolPowerSupplySerialNumber_Object = MibTableColumn
cpqHeFltTolPowerSupplySerialNumber = _CpqHeFltTolPowerSupplySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 11),
    _CpqHeFltTolPowerSupplySerialNumber_Type()
)
cpqHeFltTolPowerSupplySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplySerialNumber.setStatus("mandatory")


class _CpqHeFltTolPowerSupplyAutoRev_Type(OctetString):
    """Custom type cpqHeFltTolPowerSupplyAutoRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CpqHeFltTolPowerSupplyAutoRev_Type.__name__ = "OctetString"
_CpqHeFltTolPowerSupplyAutoRev_Object = MibTableColumn
cpqHeFltTolPowerSupplyAutoRev = _CpqHeFltTolPowerSupplyAutoRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 12),
    _CpqHeFltTolPowerSupplyAutoRev_Type()
)
cpqHeFltTolPowerSupplyAutoRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyAutoRev.setStatus("mandatory")


class _CpqHeFltTolPowerSupplyHotPlug_Type(Integer32):
    """Custom type cpqHeFltTolPowerSupplyHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotPluggable", 3),
          ("nonHotPluggable", 2),
          ("other", 1))
    )


_CpqHeFltTolPowerSupplyHotPlug_Type.__name__ = "Integer32"
_CpqHeFltTolPowerSupplyHotPlug_Object = MibTableColumn
cpqHeFltTolPowerSupplyHotPlug = _CpqHeFltTolPowerSupplyHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 13),
    _CpqHeFltTolPowerSupplyHotPlug_Type()
)
cpqHeFltTolPowerSupplyHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyHotPlug.setStatus("mandatory")


class _CpqHeFltTolPowerSupplyFirmwareRev_Type(DisplayString):
    """Custom type cpqHeFltTolPowerSupplyFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqHeFltTolPowerSupplyFirmwareRev_Type.__name__ = "DisplayString"
_CpqHeFltTolPowerSupplyFirmwareRev_Object = MibTableColumn
cpqHeFltTolPowerSupplyFirmwareRev = _CpqHeFltTolPowerSupplyFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 14),
    _CpqHeFltTolPowerSupplyFirmwareRev_Type()
)
cpqHeFltTolPowerSupplyFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyFirmwareRev.setStatus("mandatory")


class _CpqHeFltTolPowerSupplyHwLocation_Type(DisplayString):
    """Custom type cpqHeFltTolPowerSupplyHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeFltTolPowerSupplyHwLocation_Type.__name__ = "DisplayString"
_CpqHeFltTolPowerSupplyHwLocation_Object = MibTableColumn
cpqHeFltTolPowerSupplyHwLocation = _CpqHeFltTolPowerSupplyHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 15),
    _CpqHeFltTolPowerSupplyHwLocation_Type()
)
cpqHeFltTolPowerSupplyHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyHwLocation.setStatus("optional")


class _CpqHeFltTolPowerSupplySparePartNum_Type(DisplayString):
    """Custom type cpqHeFltTolPowerSupplySparePartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqHeFltTolPowerSupplySparePartNum_Type.__name__ = "DisplayString"
_CpqHeFltTolPowerSupplySparePartNum_Object = MibTableColumn
cpqHeFltTolPowerSupplySparePartNum = _CpqHeFltTolPowerSupplySparePartNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 16),
    _CpqHeFltTolPowerSupplySparePartNum_Type()
)
cpqHeFltTolPowerSupplySparePartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplySparePartNum.setStatus("optional")
_CpqHeFltTolPowerSupplyRedundantPartner_Type = Integer32
_CpqHeFltTolPowerSupplyRedundantPartner_Object = MibTableColumn
cpqHeFltTolPowerSupplyRedundantPartner = _CpqHeFltTolPowerSupplyRedundantPartner_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 17),
    _CpqHeFltTolPowerSupplyRedundantPartner_Type()
)
cpqHeFltTolPowerSupplyRedundantPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyRedundantPartner.setStatus("mandatory")


class _CpqHeFltTolPowerSupplyErrorCondition_Type(Integer32):
    """Custom type cpqHeFltTolPowerSupplyErrorCondition based on Integer32"""
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
        *(("fanfailure", 7),
          ("generalFailure", 2),
          ("iinternaltemphighwarning", 13),
          ("inlettemphighwarning", 12),
          ("noError", 1),
          ("overcurrent", 4),
          ("overtemperature", 5),
          ("overvoltage", 3),
          ("powerinputloss", 6),
          ("vauxhighwarning", 14),
          ("vauxlowwarning", 15),
          ("vinhighwarning", 8),
          ("vinlowwarning", 9),
          ("vouthighwarning", 10),
          ("voutlowwarning", 11))
    )


_CpqHeFltTolPowerSupplyErrorCondition_Type.__name__ = "Integer32"
_CpqHeFltTolPowerSupplyErrorCondition_Object = MibTableColumn
cpqHeFltTolPowerSupplyErrorCondition = _CpqHeFltTolPowerSupplyErrorCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 9, 3, 1, 18),
    _CpqHeFltTolPowerSupplyErrorCondition_Type()
)
cpqHeFltTolPowerSupplyErrorCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeFltTolPowerSupplyErrorCondition.setStatus("mandatory")
_CpqHeIRC_ObjectIdentity = ObjectIdentity
cpqHeIRC = _CpqHeIRC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 10)
)


class _CpqHeIRCStatus_Type(Integer32):
    """Custom type cpqHeIRCStatus based on Integer32"""
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
        *(("disabled", 3),
          ("enabled", 4),
          ("notavailable", 2),
          ("unknown", 1))
    )


_CpqHeIRCStatus_Type.__name__ = "Integer32"
_CpqHeIRCStatus_Object = MibScalar
cpqHeIRCStatus = _CpqHeIRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 10, 1),
    _CpqHeIRCStatus_Type()
)
cpqHeIRCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeIRCStatus.setStatus("mandatory")
_CpqHeEventLog_ObjectIdentity = ObjectIdentity
cpqHeEventLog = _CpqHeEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11)
)


class _CpqHeEventLogSupported_Type(Integer32):
    """Custom type cpqHeEventLogSupported based on Integer32"""
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
        *(("clear", 4),
          ("notSupported", 2),
          ("other", 1),
          ("supported", 3))
    )


_CpqHeEventLogSupported_Type.__name__ = "Integer32"
_CpqHeEventLogSupported_Object = MibScalar
cpqHeEventLogSupported = _CpqHeEventLogSupported_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 1),
    _CpqHeEventLogSupported_Type()
)
cpqHeEventLogSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeEventLogSupported.setStatus("mandatory")


class _CpqHeEventLogCondition_Type(Integer32):
    """Custom type cpqHeEventLogCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeEventLogCondition_Type.__name__ = "Integer32"
_CpqHeEventLogCondition_Object = MibScalar
cpqHeEventLogCondition = _CpqHeEventLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 2),
    _CpqHeEventLogCondition_Type()
)
cpqHeEventLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeEventLogCondition.setStatus("mandatory")
_CpqHeEventLogTable_Object = MibTable
cpqHeEventLogTable = _CpqHeEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3)
)
if mibBuilder.loadTexts:
    cpqHeEventLogTable.setStatus("mandatory")
_CpqHeEventLogEntry_Object = MibTableRow
cpqHeEventLogEntry = _CpqHeEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3, 1)
)
cpqHeEventLogEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeEventLogEntryNumber"),
)
if mibBuilder.loadTexts:
    cpqHeEventLogEntry.setStatus("mandatory")
_CpqHeEventLogEntryNumber_Type = Integer32
_CpqHeEventLogEntryNumber_Object = MibTableColumn
cpqHeEventLogEntryNumber = _CpqHeEventLogEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3, 1, 1),
    _CpqHeEventLogEntryNumber_Type()
)
cpqHeEventLogEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeEventLogEntryNumber.setStatus("mandatory")


class _CpqHeEventLogEntrySeverity_Type(Integer32):
    """Custom type cpqHeEventLogEntrySeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              6,
              9,
              15)
        )
    )
    namedValues = NamedValues(
        *(("caution", 9),
          ("critical", 15),
          ("infoWithAlert", 3),
          ("informational", 2),
          ("repaired", 6))
    )


_CpqHeEventLogEntrySeverity_Type.__name__ = "Integer32"
_CpqHeEventLogEntrySeverity_Object = MibTableColumn
cpqHeEventLogEntrySeverity = _CpqHeEventLogEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3, 1, 2),
    _CpqHeEventLogEntrySeverity_Type()
)
cpqHeEventLogEntrySeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeEventLogEntrySeverity.setStatus("mandatory")
_CpqHeEventLogEntryClass_Type = Integer32
_CpqHeEventLogEntryClass_Object = MibTableColumn
cpqHeEventLogEntryClass = _CpqHeEventLogEntryClass_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3, 1, 3),
    _CpqHeEventLogEntryClass_Type()
)
cpqHeEventLogEntryClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeEventLogEntryClass.setStatus("mandatory")
_CpqHeEventLogEntryCode_Type = Integer32
_CpqHeEventLogEntryCode_Object = MibTableColumn
cpqHeEventLogEntryCode = _CpqHeEventLogEntryCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3, 1, 4),
    _CpqHeEventLogEntryCode_Type()
)
cpqHeEventLogEntryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeEventLogEntryCode.setStatus("mandatory")
_CpqHeEventLogEntryCount_Type = Integer32
_CpqHeEventLogEntryCount_Object = MibTableColumn
cpqHeEventLogEntryCount = _CpqHeEventLogEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3, 1, 5),
    _CpqHeEventLogEntryCount_Type()
)
cpqHeEventLogEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeEventLogEntryCount.setStatus("mandatory")


class _CpqHeEventLogInitialTime_Type(OctetString):
    """Custom type cpqHeEventLogInitialTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CpqHeEventLogInitialTime_Type.__name__ = "OctetString"
_CpqHeEventLogInitialTime_Object = MibTableColumn
cpqHeEventLogInitialTime = _CpqHeEventLogInitialTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3, 1, 6),
    _CpqHeEventLogInitialTime_Type()
)
cpqHeEventLogInitialTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeEventLogInitialTime.setStatus("mandatory")


class _CpqHeEventLogUpdateTime_Type(OctetString):
    """Custom type cpqHeEventLogUpdateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CpqHeEventLogUpdateTime_Type.__name__ = "OctetString"
_CpqHeEventLogUpdateTime_Object = MibTableColumn
cpqHeEventLogUpdateTime = _CpqHeEventLogUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3, 1, 7),
    _CpqHeEventLogUpdateTime_Type()
)
cpqHeEventLogUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeEventLogUpdateTime.setStatus("mandatory")


class _CpqHeEventLogErrorDesc_Type(DisplayString):
    """Custom type cpqHeEventLogErrorDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeEventLogErrorDesc_Type.__name__ = "DisplayString"
_CpqHeEventLogErrorDesc_Object = MibTableColumn
cpqHeEventLogErrorDesc = _CpqHeEventLogErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3, 1, 8),
    _CpqHeEventLogErrorDesc_Type()
)
cpqHeEventLogErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeEventLogErrorDesc.setStatus("mandatory")


class _CpqHeEventLogFreeFormData_Type(OctetString):
    """Custom type cpqHeEventLogFreeFormData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqHeEventLogFreeFormData_Type.__name__ = "OctetString"
_CpqHeEventLogFreeFormData_Object = MibTableColumn
cpqHeEventLogFreeFormData = _CpqHeEventLogFreeFormData_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 11, 3, 1, 9),
    _CpqHeEventLogFreeFormData_Type()
)
cpqHeEventLogFreeFormData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeEventLogFreeFormData.setStatus("mandatory")
_CpqHeMgmtDisplay_ObjectIdentity = ObjectIdentity
cpqHeMgmtDisplay = _CpqHeMgmtDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 12)
)


class _CpqHeMgmtDisplayType_Type(Integer32):
    """Custom type cpqHeMgmtDisplayType based on Integer32"""
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
        *(("imd4x16", 3),
          ("none", 2),
          ("ocp1x16", 4),
          ("other", 1))
    )


_CpqHeMgmtDisplayType_Type.__name__ = "Integer32"
_CpqHeMgmtDisplayType_Object = MibScalar
cpqHeMgmtDisplayType = _CpqHeMgmtDisplayType_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 12, 1),
    _CpqHeMgmtDisplayType_Type()
)
cpqHeMgmtDisplayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeMgmtDisplayType.setStatus("mandatory")


class _CpqHeMgmtDisplayText_Type(DisplayString):
    """Custom type cpqHeMgmtDisplayText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeMgmtDisplayText_Type.__name__ = "DisplayString"
_CpqHeMgmtDisplayText_Object = MibScalar
cpqHeMgmtDisplayText = _CpqHeMgmtDisplayText_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 12, 2),
    _CpqHeMgmtDisplayText_Type()
)
cpqHeMgmtDisplayText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeMgmtDisplayText.setStatus("mandatory")


class _CpqHeMgmtUID_Type(Integer32):
    """Custom type cpqHeMgmtUID based on Integer32"""
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
        *(("ledBlinking", 5),
          ("ledOff", 4),
          ("ledOn", 3),
          ("none", 2),
          ("other", 1))
    )


_CpqHeMgmtUID_Type.__name__ = "Integer32"
_CpqHeMgmtUID_Object = MibScalar
cpqHeMgmtUID = _CpqHeMgmtUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 12, 3),
    _CpqHeMgmtUID_Type()
)
cpqHeMgmtUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeMgmtUID.setStatus("mandatory")
_CpqHePowerConverter_ObjectIdentity = ObjectIdentity
cpqHePowerConverter = _CpqHePowerConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13)
)


class _CpqHePowerConverterSupported_Type(Integer32):
    """Custom type cpqHePowerConverterSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("other", 1),
          ("supported", 3))
    )


_CpqHePowerConverterSupported_Type.__name__ = "Integer32"
_CpqHePowerConverterSupported_Object = MibScalar
cpqHePowerConverterSupported = _CpqHePowerConverterSupported_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 1),
    _CpqHePowerConverterSupported_Type()
)
cpqHePowerConverterSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePowerConverterSupported.setStatus("mandatory")


class _CpqHePowerConverterCondition_Type(Integer32):
    """Custom type cpqHePowerConverterCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHePowerConverterCondition_Type.__name__ = "Integer32"
_CpqHePowerConverterCondition_Object = MibScalar
cpqHePowerConverterCondition = _CpqHePowerConverterCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 2),
    _CpqHePowerConverterCondition_Type()
)
cpqHePowerConverterCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePowerConverterCondition.setStatus("mandatory")
_CpqHePowerConverterTable_Object = MibTable
cpqHePowerConverterTable = _CpqHePowerConverterTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3)
)
if mibBuilder.loadTexts:
    cpqHePowerConverterTable.setStatus("mandatory")
_CpqHePowerConverterEntry_Object = MibTableRow
cpqHePowerConverterEntry = _CpqHePowerConverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3, 1)
)
cpqHePowerConverterEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHePwrConvChassis"),
    (0, "CPQHLTH-MIB", "cpqHePwrConvIndex"),
)
if mibBuilder.loadTexts:
    cpqHePowerConverterEntry.setStatus("mandatory")
_CpqHePwrConvChassis_Type = Integer32
_CpqHePwrConvChassis_Object = MibTableColumn
cpqHePwrConvChassis = _CpqHePwrConvChassis_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3, 1, 1),
    _CpqHePwrConvChassis_Type()
)
cpqHePwrConvChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePwrConvChassis.setStatus("mandatory")
_CpqHePwrConvIndex_Type = Integer32
_CpqHePwrConvIndex_Object = MibTableColumn
cpqHePwrConvIndex = _CpqHePwrConvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3, 1, 2),
    _CpqHePwrConvIndex_Type()
)
cpqHePwrConvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePwrConvIndex.setStatus("mandatory")


class _CpqHePwrConvPresent_Type(Integer32):
    """Custom type cpqHePwrConvPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("other", 1),
          ("present", 3))
    )


_CpqHePwrConvPresent_Type.__name__ = "Integer32"
_CpqHePwrConvPresent_Object = MibTableColumn
cpqHePwrConvPresent = _CpqHePwrConvPresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3, 1, 3),
    _CpqHePwrConvPresent_Type()
)
cpqHePwrConvPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePwrConvPresent.setStatus("mandatory")
_CpqHePwrConvSlot_Type = Integer32
_CpqHePwrConvSlot_Object = MibTableColumn
cpqHePwrConvSlot = _CpqHePwrConvSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3, 1, 4),
    _CpqHePwrConvSlot_Type()
)
cpqHePwrConvSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePwrConvSlot.setStatus("mandatory")
_CpqHePwrConvSocket_Type = Integer32
_CpqHePwrConvSocket_Object = MibTableColumn
cpqHePwrConvSocket = _CpqHePwrConvSocket_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3, 1, 5),
    _CpqHePwrConvSocket_Type()
)
cpqHePwrConvSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePwrConvSocket.setStatus("mandatory")


class _CpqHePwrConvRedundant_Type(Integer32):
    """Custom type cpqHePwrConvRedundant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonRedundant", 2),
          ("other", 1),
          ("redundant", 3))
    )


_CpqHePwrConvRedundant_Type.__name__ = "Integer32"
_CpqHePwrConvRedundant_Object = MibTableColumn
cpqHePwrConvRedundant = _CpqHePwrConvRedundant_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3, 1, 6),
    _CpqHePwrConvRedundant_Type()
)
cpqHePwrConvRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePwrConvRedundant.setStatus("mandatory")
_CpqHePwrConvRedundantGroupId_Type = Integer32
_CpqHePwrConvRedundantGroupId_Object = MibTableColumn
cpqHePwrConvRedundantGroupId = _CpqHePwrConvRedundantGroupId_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3, 1, 7),
    _CpqHePwrConvRedundantGroupId_Type()
)
cpqHePwrConvRedundantGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePwrConvRedundantGroupId.setStatus("mandatory")


class _CpqHePwrConvCondition_Type(Integer32):
    """Custom type cpqHePwrConvCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHePwrConvCondition_Type.__name__ = "Integer32"
_CpqHePwrConvCondition_Object = MibTableColumn
cpqHePwrConvCondition = _CpqHePwrConvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3, 1, 8),
    _CpqHePwrConvCondition_Type()
)
cpqHePwrConvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePwrConvCondition.setStatus("mandatory")


class _CpqHePwrConvHwLocation_Type(DisplayString):
    """Custom type cpqHePwrConvHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHePwrConvHwLocation_Type.__name__ = "DisplayString"
_CpqHePwrConvHwLocation_Object = MibTableColumn
cpqHePwrConvHwLocation = _CpqHePwrConvHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 13, 3, 1, 9),
    _CpqHePwrConvHwLocation_Type()
)
cpqHePwrConvHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePwrConvHwLocation.setStatus("optional")
_CpqHeResilientMemory_ObjectIdentity = ObjectIdentity
cpqHeResilientMemory = _CpqHeResilientMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14)
)


class _CpqHeResilientMemTypeActive_Type(Integer32):
    """Custom type cpqHeResilientMemTypeActive based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("advancedEcc", 5),
          ("lockStep", 9),
          ("mirrored", 4),
          ("mirroredDualBoard", 7),
          ("mirroredSingleBoard", 6),
          ("mirroringIntersocket", 13),
          ("mirroringIntrasocket", 12),
          ("none", 2),
          ("onLineSpare", 3),
          ("onLineSpareChannel", 10),
          ("onLineSpareRank", 11),
          ("other", 1),
          ("xor", 8))
    )


_CpqHeResilientMemTypeActive_Type.__name__ = "Integer32"
_CpqHeResilientMemTypeActive_Object = MibScalar
cpqHeResilientMemTypeActive = _CpqHeResilientMemTypeActive_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 1),
    _CpqHeResilientMemTypeActive_Type()
)
cpqHeResilientMemTypeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResilientMemTypeActive.setStatus("mandatory")
_CpqHeResilientMemTypeAvailable_Type = Integer32
_CpqHeResilientMemTypeAvailable_Object = MibScalar
cpqHeResilientMemTypeAvailable = _CpqHeResilientMemTypeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 2),
    _CpqHeResilientMemTypeAvailable_Type()
)
cpqHeResilientMemTypeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResilientMemTypeAvailable.setStatus("mandatory")


class _CpqHeResilientMemStatus_Type(Integer32):
    """Custom type cpqHeResilientMemStatus based on Integer32"""
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
        *(("advancedEcc", 12),
          ("advancedEccWithFaults", 13),
          ("degraded", 4),
          ("dimmEcc", 5),
          ("hotSpareNoFaults", 8),
          ("hotSpareWithFaults", 9),
          ("lockStep", 14),
          ("lockStepWithFaults", 15),
          ("mirrorNoFaults", 6),
          ("mirrorWithFaults", 7),
          ("notProtected", 2),
          ("other", 1),
          ("protected", 3),
          ("xorNoFaults", 10),
          ("xorWithFaults", 11))
    )


_CpqHeResilientMemStatus_Type.__name__ = "Integer32"
_CpqHeResilientMemStatus_Object = MibScalar
cpqHeResilientMemStatus = _CpqHeResilientMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 3),
    _CpqHeResilientMemStatus_Type()
)
cpqHeResilientMemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResilientMemStatus.setStatus("mandatory")


class _CpqHeResilientMemCondition_Type(Integer32):
    """Custom type cpqHeResilientMemCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeResilientMemCondition_Type.__name__ = "Integer32"
_CpqHeResilientMemCondition_Object = MibScalar
cpqHeResilientMemCondition = _CpqHeResilientMemCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 4),
    _CpqHeResilientMemCondition_Type()
)
cpqHeResilientMemCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResilientMemCondition.setStatus("mandatory")


class _CpqHeResilientMemHotPlug_Type(Integer32):
    """Custom type cpqHeResilientMemHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotPluggable", 3),
          ("nonHotPluggable", 2),
          ("other", 1))
    )


_CpqHeResilientMemHotPlug_Type.__name__ = "Integer32"
_CpqHeResilientMemHotPlug_Object = MibScalar
cpqHeResilientMemHotPlug = _CpqHeResilientMemHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 5),
    _CpqHeResilientMemHotPlug_Type()
)
cpqHeResilientMemHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResilientMemHotPlug.setStatus("mandatory")
_CpqHeResilientMemOperatingSpeed_Type = Integer32
_CpqHeResilientMemOperatingSpeed_Object = MibScalar
cpqHeResilientMemOperatingSpeed = _CpqHeResilientMemOperatingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 6),
    _CpqHeResilientMemOperatingSpeed_Type()
)
cpqHeResilientMemOperatingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResilientMemOperatingSpeed.setStatus("mandatory")
_CpqHeResilientMemOsMemSize_Type = Integer32
_CpqHeResilientMemOsMemSize_Object = MibScalar
cpqHeResilientMemOsMemSize = _CpqHeResilientMemOsMemSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 7),
    _CpqHeResilientMemOsMemSize_Type()
)
cpqHeResilientMemOsMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResilientMemOsMemSize.setStatus("mandatory")
_CpqHeResilientMemTotalMemSize_Type = Integer32
_CpqHeResilientMemTotalMemSize_Object = MibScalar
cpqHeResilientMemTotalMemSize = _CpqHeResilientMemTotalMemSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 8),
    _CpqHeResilientMemTotalMemSize_Type()
)
cpqHeResilientMemTotalMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResilientMemTotalMemSize.setStatus("mandatory")


class _CpqHeResilientMemRivState_Type(Integer32):
    """Custom type cpqHeResilientMemRivState based on Integer32"""
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
        *(("inactive", 2),
          ("initializing", 4),
          ("other", 1),
          ("rebuilding", 3),
          ("verifying", 5))
    )


_CpqHeResilientMemRivState_Type.__name__ = "Integer32"
_CpqHeResilientMemRivState_Object = MibScalar
cpqHeResilientMemRivState = _CpqHeResilientMemRivState_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 9),
    _CpqHeResilientMemRivState_Type()
)
cpqHeResilientMemRivState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResilientMemRivState.setStatus("mandatory")
_CpqHeResMemBoardTable_Object = MibTable
cpqHeResMemBoardTable = _CpqHeResMemBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10)
)
if mibBuilder.loadTexts:
    cpqHeResMemBoardTable.setStatus("mandatory")
_CpqHeResMemBoardEntry_Object = MibTableRow
cpqHeResMemBoardEntry = _CpqHeResMemBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10, 1)
)
cpqHeResMemBoardEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeResMemBoardSlotIndex"),
)
if mibBuilder.loadTexts:
    cpqHeResMemBoardEntry.setStatus("mandatory")
_CpqHeResMemBoardSlotIndex_Type = Integer32
_CpqHeResMemBoardSlotIndex_Object = MibTableColumn
cpqHeResMemBoardSlotIndex = _CpqHeResMemBoardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10, 1, 1),
    _CpqHeResMemBoardSlotIndex_Type()
)
cpqHeResMemBoardSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemBoardSlotIndex.setStatus("mandatory")


class _CpqHeResMemBoardOnlineStatus_Type(Integer32):
    """Custom type cpqHeResMemBoardOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("other", 1),
          ("present", 2))
    )


_CpqHeResMemBoardOnlineStatus_Type.__name__ = "Integer32"
_CpqHeResMemBoardOnlineStatus_Object = MibTableColumn
cpqHeResMemBoardOnlineStatus = _CpqHeResMemBoardOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10, 1, 2),
    _CpqHeResMemBoardOnlineStatus_Type()
)
cpqHeResMemBoardOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemBoardOnlineStatus.setStatus("mandatory")


class _CpqHeResMemBoardErrorStatus_Type(Integer32):
    """Custom type cpqHeResMemBoardErrorStatus based on Integer32"""
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
        *(("advancedEcc", 8),
          ("busError", 6),
          ("configError", 5),
          ("dimmEccError", 3),
          ("lockstep", 14),
          ("lockstepDimmError", 15),
          ("memoryRaid", 12),
          ("mirrored", 10),
          ("mirroredDimmError", 11),
          ("noError", 2),
          ("onlineSpare", 9),
          ("other", 1),
          ("powerError", 7),
          ("raidDimmError", 13),
          ("unlockError", 4))
    )


_CpqHeResMemBoardErrorStatus_Type.__name__ = "Integer32"
_CpqHeResMemBoardErrorStatus_Object = MibTableColumn
cpqHeResMemBoardErrorStatus = _CpqHeResMemBoardErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10, 1, 3),
    _CpqHeResMemBoardErrorStatus_Type()
)
cpqHeResMemBoardErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemBoardErrorStatus.setStatus("mandatory")


class _CpqHeResMemBoardLocked_Type(Integer32):
    """Custom type cpqHeResMemBoardLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 3),
          ("other", 1),
          ("unlocked", 2))
    )


_CpqHeResMemBoardLocked_Type.__name__ = "Integer32"
_CpqHeResMemBoardLocked_Object = MibTableColumn
cpqHeResMemBoardLocked = _CpqHeResMemBoardLocked_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10, 1, 4),
    _CpqHeResMemBoardLocked_Type()
)
cpqHeResMemBoardLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemBoardLocked.setStatus("mandatory")
_CpqHeResMemBoardNumSockets_Type = Integer32
_CpqHeResMemBoardNumSockets_Object = MibTableColumn
cpqHeResMemBoardNumSockets = _CpqHeResMemBoardNumSockets_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10, 1, 5),
    _CpqHeResMemBoardNumSockets_Type()
)
cpqHeResMemBoardNumSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemBoardNumSockets.setStatus("mandatory")
_CpqHeResMemBoardOsMemSize_Type = Integer32
_CpqHeResMemBoardOsMemSize_Object = MibTableColumn
cpqHeResMemBoardOsMemSize = _CpqHeResMemBoardOsMemSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10, 1, 6),
    _CpqHeResMemBoardOsMemSize_Type()
)
cpqHeResMemBoardOsMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemBoardOsMemSize.setStatus("mandatory")
_CpqHeResMemBoardTotalMemSize_Type = Integer32
_CpqHeResMemBoardTotalMemSize_Object = MibTableColumn
cpqHeResMemBoardTotalMemSize = _CpqHeResMemBoardTotalMemSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10, 1, 7),
    _CpqHeResMemBoardTotalMemSize_Type()
)
cpqHeResMemBoardTotalMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemBoardTotalMemSize.setStatus("mandatory")


class _CpqHeResMemBoardCondition_Type(Integer32):
    """Custom type cpqHeResMemBoardCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeResMemBoardCondition_Type.__name__ = "Integer32"
_CpqHeResMemBoardCondition_Object = MibTableColumn
cpqHeResMemBoardCondition = _CpqHeResMemBoardCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10, 1, 8),
    _CpqHeResMemBoardCondition_Type()
)
cpqHeResMemBoardCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemBoardCondition.setStatus("mandatory")


class _CpqHeResMemBoardHotPlug_Type(Integer32):
    """Custom type cpqHeResMemBoardHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotPluggable", 3),
          ("nonHotPluggable", 2),
          ("other", 1))
    )


_CpqHeResMemBoardHotPlug_Type.__name__ = "Integer32"
_CpqHeResMemBoardHotPlug_Object = MibTableColumn
cpqHeResMemBoardHotPlug = _CpqHeResMemBoardHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 10, 1, 9),
    _CpqHeResMemBoardHotPlug_Type()
)
cpqHeResMemBoardHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemBoardHotPlug.setStatus("mandatory")
_CpqHeResMemModuleTable_Object = MibTable
cpqHeResMemModuleTable = _CpqHeResMemModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 11)
)
if mibBuilder.loadTexts:
    cpqHeResMemModuleTable.setStatus("mandatory")
_CpqHeResMemModuleEntry_Object = MibTableRow
cpqHeResMemModuleEntry = _CpqHeResMemModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 11, 1)
)
cpqHeResMemModuleEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeResMemBoardIndex"),
    (0, "CPQHLTH-MIB", "cpqHeResMemModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqHeResMemModuleEntry.setStatus("mandatory")
_CpqHeResMemBoardIndex_Type = Integer32
_CpqHeResMemBoardIndex_Object = MibTableColumn
cpqHeResMemBoardIndex = _CpqHeResMemBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 11, 1, 1),
    _CpqHeResMemBoardIndex_Type()
)
cpqHeResMemBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemBoardIndex.setStatus("mandatory")
_CpqHeResMemModuleIndex_Type = Integer32
_CpqHeResMemModuleIndex_Object = MibTableColumn
cpqHeResMemModuleIndex = _CpqHeResMemModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 11, 1, 2),
    _CpqHeResMemModuleIndex_Type()
)
cpqHeResMemModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemModuleIndex.setStatus("mandatory")


class _CpqHeResMemModuleSparePartNo_Type(DisplayString):
    """Custom type cpqHeResMemModuleSparePartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqHeResMemModuleSparePartNo_Type.__name__ = "DisplayString"
_CpqHeResMemModuleSparePartNo_Object = MibTableColumn
cpqHeResMemModuleSparePartNo = _CpqHeResMemModuleSparePartNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 11, 1, 3),
    _CpqHeResMemModuleSparePartNo_Type()
)
cpqHeResMemModuleSparePartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemModuleSparePartNo.setStatus("mandatory")


class _CpqHeResMemModuleStatus_Type(Integer32):
    """Custom type cpqHeResMemModuleStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("add", 5),
          ("badConfig", 10),
          ("degraded", 11),
          ("doesNotMatch", 8),
          ("good", 4),
          ("missing", 7),
          ("notPresent", 2),
          ("notSupported", 9),
          ("other", 1),
          ("present", 3),
          ("upgrade", 6))
    )


_CpqHeResMemModuleStatus_Type.__name__ = "Integer32"
_CpqHeResMemModuleStatus_Object = MibTableColumn
cpqHeResMemModuleStatus = _CpqHeResMemModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 11, 1, 4),
    _CpqHeResMemModuleStatus_Type()
)
cpqHeResMemModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemModuleStatus.setStatus("mandatory")


class _CpqHeResMemModuleCondition_Type(Integer32):
    """Custom type cpqHeResMemModuleCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeResMemModuleCondition_Type.__name__ = "Integer32"
_CpqHeResMemModuleCondition_Object = MibTableColumn
cpqHeResMemModuleCondition = _CpqHeResMemModuleCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 11, 1, 5),
    _CpqHeResMemModuleCondition_Type()
)
cpqHeResMemModuleCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemModuleCondition.setStatus("mandatory")


class _CpqHeResMemModuleSpd_Type(OctetString):
    """Custom type cpqHeResMemModuleSpd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CpqHeResMemModuleSpd_Type.__name__ = "OctetString"
_CpqHeResMemModuleSpd_Object = MibTableColumn
cpqHeResMemModuleSpd = _CpqHeResMemModuleSpd_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 11, 1, 6),
    _CpqHeResMemModuleSpd_Type()
)
cpqHeResMemModuleSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMemModuleSpd.setStatus("mandatory")
_CpqHeResMem2BoardTable_Object = MibTable
cpqHeResMem2BoardTable = _CpqHeResMem2BoardTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12)
)
if mibBuilder.loadTexts:
    cpqHeResMem2BoardTable.setStatus("mandatory")
_CpqHeResMem2BoardEntry_Object = MibTableRow
cpqHeResMem2BoardEntry = _CpqHeResMem2BoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1)
)
cpqHeResMem2BoardEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeResMem2BoardIndex"),
)
if mibBuilder.loadTexts:
    cpqHeResMem2BoardEntry.setStatus("mandatory")
_CpqHeResMem2BoardIndex_Type = Integer32
_CpqHeResMem2BoardIndex_Object = MibTableColumn
cpqHeResMem2BoardIndex = _CpqHeResMem2BoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 1),
    _CpqHeResMem2BoardIndex_Type()
)
cpqHeResMem2BoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardIndex.setStatus("mandatory")
_CpqHeResMem2BoardSlotNum_Type = Integer32
_CpqHeResMem2BoardSlotNum_Object = MibTableColumn
cpqHeResMem2BoardSlotNum = _CpqHeResMem2BoardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 2),
    _CpqHeResMem2BoardSlotNum_Type()
)
cpqHeResMem2BoardSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardSlotNum.setStatus("mandatory")
_CpqHeResMem2BoardCpuNum_Type = Integer32
_CpqHeResMem2BoardCpuNum_Object = MibTableColumn
cpqHeResMem2BoardCpuNum = _CpqHeResMem2BoardCpuNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 3),
    _CpqHeResMem2BoardCpuNum_Type()
)
cpqHeResMem2BoardCpuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardCpuNum.setStatus("mandatory")
_CpqHeResMem2BoardRiserNum_Type = Integer32
_CpqHeResMem2BoardRiserNum_Object = MibTableColumn
cpqHeResMem2BoardRiserNum = _CpqHeResMem2BoardRiserNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 4),
    _CpqHeResMem2BoardRiserNum_Type()
)
cpqHeResMem2BoardRiserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardRiserNum.setStatus("mandatory")


class _CpqHeResMem2BoardOnlineStatus_Type(Integer32):
    """Custom type cpqHeResMem2BoardOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("other", 1),
          ("present", 2))
    )


_CpqHeResMem2BoardOnlineStatus_Type.__name__ = "Integer32"
_CpqHeResMem2BoardOnlineStatus_Object = MibTableColumn
cpqHeResMem2BoardOnlineStatus = _CpqHeResMem2BoardOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 5),
    _CpqHeResMem2BoardOnlineStatus_Type()
)
cpqHeResMem2BoardOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardOnlineStatus.setStatus("mandatory")


class _CpqHeResMem2BoardErrorStatus_Type(Integer32):
    """Custom type cpqHeResMem2BoardErrorStatus based on Integer32"""
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
        *(("advancedEcc", 8),
          ("busError", 6),
          ("configError", 5),
          ("dimmEccError", 3),
          ("lockStep", 14),
          ("lockStepError", 15),
          ("memoryRaid", 12),
          ("mirrored", 10),
          ("mirroredDimmError", 11),
          ("noError", 2),
          ("onlineSpare", 9),
          ("other", 1),
          ("powerError", 7),
          ("raidDimmError", 13),
          ("unlockError", 4))
    )


_CpqHeResMem2BoardErrorStatus_Type.__name__ = "Integer32"
_CpqHeResMem2BoardErrorStatus_Object = MibTableColumn
cpqHeResMem2BoardErrorStatus = _CpqHeResMem2BoardErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 6),
    _CpqHeResMem2BoardErrorStatus_Type()
)
cpqHeResMem2BoardErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardErrorStatus.setStatus("mandatory")


class _CpqHeResMem2BoardLocked_Type(Integer32):
    """Custom type cpqHeResMem2BoardLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 3),
          ("other", 1),
          ("unlocked", 2))
    )


_CpqHeResMem2BoardLocked_Type.__name__ = "Integer32"
_CpqHeResMem2BoardLocked_Object = MibTableColumn
cpqHeResMem2BoardLocked = _CpqHeResMem2BoardLocked_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 7),
    _CpqHeResMem2BoardLocked_Type()
)
cpqHeResMem2BoardLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardLocked.setStatus("mandatory")
_CpqHeResMem2BoardNumSockets_Type = Integer32
_CpqHeResMem2BoardNumSockets_Object = MibTableColumn
cpqHeResMem2BoardNumSockets = _CpqHeResMem2BoardNumSockets_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 8),
    _CpqHeResMem2BoardNumSockets_Type()
)
cpqHeResMem2BoardNumSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardNumSockets.setStatus("mandatory")
_CpqHeResMem2BoardOsMemSize_Type = Integer32
_CpqHeResMem2BoardOsMemSize_Object = MibTableColumn
cpqHeResMem2BoardOsMemSize = _CpqHeResMem2BoardOsMemSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 9),
    _CpqHeResMem2BoardOsMemSize_Type()
)
cpqHeResMem2BoardOsMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardOsMemSize.setStatus("mandatory")
_CpqHeResMem2BoardTotalMemSize_Type = Integer32
_CpqHeResMem2BoardTotalMemSize_Object = MibTableColumn
cpqHeResMem2BoardTotalMemSize = _CpqHeResMem2BoardTotalMemSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 10),
    _CpqHeResMem2BoardTotalMemSize_Type()
)
cpqHeResMem2BoardTotalMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardTotalMemSize.setStatus("mandatory")


class _CpqHeResMem2BoardCondition_Type(Integer32):
    """Custom type cpqHeResMem2BoardCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeResMem2BoardCondition_Type.__name__ = "Integer32"
_CpqHeResMem2BoardCondition_Object = MibTableColumn
cpqHeResMem2BoardCondition = _CpqHeResMem2BoardCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 11),
    _CpqHeResMem2BoardCondition_Type()
)
cpqHeResMem2BoardCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardCondition.setStatus("mandatory")


class _CpqHeResMem2BoardHotPlug_Type(Integer32):
    """Custom type cpqHeResMem2BoardHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotPluggable", 3),
          ("nonHotPluggable", 2),
          ("other", 1))
    )


_CpqHeResMem2BoardHotPlug_Type.__name__ = "Integer32"
_CpqHeResMem2BoardHotPlug_Object = MibTableColumn
cpqHeResMem2BoardHotPlug = _CpqHeResMem2BoardHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 12),
    _CpqHeResMem2BoardHotPlug_Type()
)
cpqHeResMem2BoardHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardHotPlug.setStatus("mandatory")
_CpqHeResMem2BoardOperatingFrequency_Type = Integer32
_CpqHeResMem2BoardOperatingFrequency_Object = MibTableColumn
cpqHeResMem2BoardOperatingFrequency = _CpqHeResMem2BoardOperatingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 13),
    _CpqHeResMem2BoardOperatingFrequency_Type()
)
cpqHeResMem2BoardOperatingFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardOperatingFrequency.setStatus("mandatory")
_CpqHeResMem2BoardOperatingVoltage_Type = Integer32
_CpqHeResMem2BoardOperatingVoltage_Object = MibTableColumn
cpqHeResMem2BoardOperatingVoltage = _CpqHeResMem2BoardOperatingVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 12, 1, 14),
    _CpqHeResMem2BoardOperatingVoltage_Type()
)
cpqHeResMem2BoardOperatingVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardOperatingVoltage.setStatus("mandatory")
_CpqHeResMem2ModuleTable_Object = MibTable
cpqHeResMem2ModuleTable = _CpqHeResMem2ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13)
)
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleTable.setStatus("mandatory")
_CpqHeResMem2ModuleEntry_Object = MibTableRow
cpqHeResMem2ModuleEntry = _CpqHeResMem2ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1)
)
cpqHeResMem2ModuleEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeResMem2Module"),
)
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleEntry.setStatus("mandatory")
_CpqHeResMem2Module_Type = Integer32
_CpqHeResMem2Module_Object = MibTableColumn
cpqHeResMem2Module = _CpqHeResMem2Module_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 1),
    _CpqHeResMem2Module_Type()
)
cpqHeResMem2Module.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2Module.setStatus("mandatory")
_CpqHeResMem2BoardNum_Type = Integer32
_CpqHeResMem2BoardNum_Object = MibTableColumn
cpqHeResMem2BoardNum = _CpqHeResMem2BoardNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 2),
    _CpqHeResMem2BoardNum_Type()
)
cpqHeResMem2BoardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2BoardNum.setStatus("mandatory")
_CpqHeResMem2CpuNum_Type = Integer32
_CpqHeResMem2CpuNum_Object = MibTableColumn
cpqHeResMem2CpuNum = _CpqHeResMem2CpuNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 3),
    _CpqHeResMem2CpuNum_Type()
)
cpqHeResMem2CpuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2CpuNum.setStatus("mandatory")
_CpqHeResMem2RiserNum_Type = Integer32
_CpqHeResMem2RiserNum_Object = MibTableColumn
cpqHeResMem2RiserNum = _CpqHeResMem2RiserNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 4),
    _CpqHeResMem2RiserNum_Type()
)
cpqHeResMem2RiserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2RiserNum.setStatus("mandatory")
_CpqHeResMem2ModuleNum_Type = Integer32
_CpqHeResMem2ModuleNum_Object = MibTableColumn
cpqHeResMem2ModuleNum = _CpqHeResMem2ModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 5),
    _CpqHeResMem2ModuleNum_Type()
)
cpqHeResMem2ModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleNum.setStatus("mandatory")


class _CpqHeResMem2ModuleSize_Type(Integer32):
    """Custom type cpqHeResMem2ModuleSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqHeResMem2ModuleSize_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleSize_Object = MibTableColumn
cpqHeResMem2ModuleSize = _CpqHeResMem2ModuleSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 6),
    _CpqHeResMem2ModuleSize_Type()
)
cpqHeResMem2ModuleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleSize.setStatus("mandatory")


class _CpqHeResMem2ModuleType_Type(Integer32):
    """Custom type cpqHeResMem2ModuleType based on Integer32"""
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
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("board", 2),
          ("compaq-specific", 7),
          ("cpqDoubleWidthModule", 4),
          ("cpqSingleWidthModule", 3),
          ("dimm", 8),
          ("dimmddr", 13),
          ("dimmddr2", 14),
          ("dimmddr3", 15),
          ("dimmfbd2", 16),
          ("fb-dimm", 12),
          ("fb-dimmddr2", 17),
          ("fb-dimmddr3", 18),
          ("other", 1),
          ("pcmcia", 6),
          ("rimm", 10),
          ("simm", 5),
          ("smallOutlineDimm", 9),
          ("srimm", 11))
    )


_CpqHeResMem2ModuleType_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleType_Object = MibTableColumn
cpqHeResMem2ModuleType = _CpqHeResMem2ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 7),
    _CpqHeResMem2ModuleType_Type()
)
cpqHeResMem2ModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleType.setStatus("mandatory")


class _CpqHeResMem2ModuleTechnology_Type(Integer32):
    """Custom type cpqHeResMem2ModuleTechnology based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("burstEdoPageMode", 4),
          ("edoPageMode", 3),
          ("fastPageMode", 2),
          ("lrdimm", 9),
          ("other", 1),
          ("rdimm", 7),
          ("rdram", 6),
          ("synchronous", 5),
          ("udimm", 8))
    )


_CpqHeResMem2ModuleTechnology_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleTechnology_Object = MibTableColumn
cpqHeResMem2ModuleTechnology = _CpqHeResMem2ModuleTechnology_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 8),
    _CpqHeResMem2ModuleTechnology_Type()
)
cpqHeResMem2ModuleTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleTechnology.setStatus("mandatory")


class _CpqHeResMem2ModuleManufacturer_Type(DisplayString):
    """Custom type cpqHeResMem2ModuleManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeResMem2ModuleManufacturer_Type.__name__ = "DisplayString"
_CpqHeResMem2ModuleManufacturer_Object = MibTableColumn
cpqHeResMem2ModuleManufacturer = _CpqHeResMem2ModuleManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 9),
    _CpqHeResMem2ModuleManufacturer_Type()
)
cpqHeResMem2ModuleManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleManufacturer.setStatus("mandatory")


class _CpqHeResMem2ModulePartNo_Type(DisplayString):
    """Custom type cpqHeResMem2ModulePartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeResMem2ModulePartNo_Type.__name__ = "DisplayString"
_CpqHeResMem2ModulePartNo_Object = MibTableColumn
cpqHeResMem2ModulePartNo = _CpqHeResMem2ModulePartNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 10),
    _CpqHeResMem2ModulePartNo_Type()
)
cpqHeResMem2ModulePartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModulePartNo.setStatus("mandatory")


class _CpqHeResMem2ModuleDate_Type(OctetString):
    """Custom type cpqHeResMem2ModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqHeResMem2ModuleDate_Type.__name__ = "OctetString"
_CpqHeResMem2ModuleDate_Object = MibTableColumn
cpqHeResMem2ModuleDate = _CpqHeResMem2ModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 11),
    _CpqHeResMem2ModuleDate_Type()
)
cpqHeResMem2ModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleDate.setStatus("mandatory")


class _CpqHeResMem2ModuleSerialNo_Type(DisplayString):
    """Custom type cpqHeResMem2ModuleSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeResMem2ModuleSerialNo_Type.__name__ = "DisplayString"
_CpqHeResMem2ModuleSerialNo_Object = MibTableColumn
cpqHeResMem2ModuleSerialNo = _CpqHeResMem2ModuleSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 12),
    _CpqHeResMem2ModuleSerialNo_Type()
)
cpqHeResMem2ModuleSerialNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleSerialNo.setStatus("mandatory")


class _CpqHeResMem2ModuleHwLocation_Type(DisplayString):
    """Custom type cpqHeResMem2ModuleHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeResMem2ModuleHwLocation_Type.__name__ = "DisplayString"
_CpqHeResMem2ModuleHwLocation_Object = MibTableColumn
cpqHeResMem2ModuleHwLocation = _CpqHeResMem2ModuleHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 13),
    _CpqHeResMem2ModuleHwLocation_Type()
)
cpqHeResMem2ModuleHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleHwLocation.setStatus("optional")


class _CpqHeResMem2ModuleFrequency_Type(Integer32):
    """Custom type cpqHeResMem2ModuleFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHeResMem2ModuleFrequency_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleFrequency_Object = MibTableColumn
cpqHeResMem2ModuleFrequency = _CpqHeResMem2ModuleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 14),
    _CpqHeResMem2ModuleFrequency_Type()
)
cpqHeResMem2ModuleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleFrequency.setStatus("mandatory")


class _CpqHeResMem2ModuleCellTablePtr_Type(Integer32):
    """Custom type cpqHeResMem2ModuleCellTablePtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CpqHeResMem2ModuleCellTablePtr_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleCellTablePtr_Object = MibTableColumn
cpqHeResMem2ModuleCellTablePtr = _CpqHeResMem2ModuleCellTablePtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 15),
    _CpqHeResMem2ModuleCellTablePtr_Type()
)
cpqHeResMem2ModuleCellTablePtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleCellTablePtr.setStatus("optional")


class _CpqHeResMem2ModuleCellStatus_Type(Integer32):
    """Custom type cpqHeResMem2ModuleCellStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deconfigured", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeResMem2ModuleCellStatus_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleCellStatus_Object = MibTableColumn
cpqHeResMem2ModuleCellStatus = _CpqHeResMem2ModuleCellStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 16),
    _CpqHeResMem2ModuleCellStatus_Type()
)
cpqHeResMem2ModuleCellStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleCellStatus.setStatus("optional")


class _CpqHeResMem2ModulePartNoMfgr_Type(DisplayString):
    """Custom type cpqHeResMem2ModulePartNoMfgr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeResMem2ModulePartNoMfgr_Type.__name__ = "DisplayString"
_CpqHeResMem2ModulePartNoMfgr_Object = MibTableColumn
cpqHeResMem2ModulePartNoMfgr = _CpqHeResMem2ModulePartNoMfgr_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 17),
    _CpqHeResMem2ModulePartNoMfgr_Type()
)
cpqHeResMem2ModulePartNoMfgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModulePartNoMfgr.setStatus("optional")


class _CpqHeResMem2ModuleSerialNoMfgr_Type(DisplayString):
    """Custom type cpqHeResMem2ModuleSerialNoMfgr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHeResMem2ModuleSerialNoMfgr_Type.__name__ = "DisplayString"
_CpqHeResMem2ModuleSerialNoMfgr_Object = MibTableColumn
cpqHeResMem2ModuleSerialNoMfgr = _CpqHeResMem2ModuleSerialNoMfgr_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 18),
    _CpqHeResMem2ModuleSerialNoMfgr_Type()
)
cpqHeResMem2ModuleSerialNoMfgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleSerialNoMfgr.setStatus("optional")


class _CpqHeResMem2ModuleStatus_Type(Integer32):
    """Custom type cpqHeResMem2ModuleStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("add", 5),
          ("badConfig", 10),
          ("degraded", 11),
          ("doesNotMatch", 8),
          ("good", 4),
          ("missing", 7),
          ("notPresent", 2),
          ("notSupported", 9),
          ("other", 1),
          ("partial", 13),
          ("present", 3),
          ("spare", 12),
          ("upgrade", 6))
    )


_CpqHeResMem2ModuleStatus_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleStatus_Object = MibTableColumn
cpqHeResMem2ModuleStatus = _CpqHeResMem2ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 19),
    _CpqHeResMem2ModuleStatus_Type()
)
cpqHeResMem2ModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleStatus.setStatus("mandatory")


class _CpqHeResMem2ModuleCondition_Type(Integer32):
    """Custom type cpqHeResMem2ModuleCondition based on Integer32"""
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
        *(("degraded", 3),
          ("degradedModuleIndexUnknown", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqHeResMem2ModuleCondition_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleCondition_Object = MibTableColumn
cpqHeResMem2ModuleCondition = _CpqHeResMem2ModuleCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 20),
    _CpqHeResMem2ModuleCondition_Type()
)
cpqHeResMem2ModuleCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleCondition.setStatus("mandatory")


class _CpqHeResMem2ModuleSpd_Type(OctetString):
    """Custom type cpqHeResMem2ModuleSpd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CpqHeResMem2ModuleSpd_Type.__name__ = "OctetString"
_CpqHeResMem2ModuleSpd_Object = MibTableColumn
cpqHeResMem2ModuleSpd = _CpqHeResMem2ModuleSpd_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 21),
    _CpqHeResMem2ModuleSpd_Type()
)
cpqHeResMem2ModuleSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleSpd.setStatus("mandatory")


class _CpqHeResMem2ModuleSmartMemory_Type(Integer32):
    """Custom type cpqHeResMem2ModuleSmartMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isHPSmartMemory", 3),
          ("notHPSmartMemory", 2),
          ("other", 1))
    )


_CpqHeResMem2ModuleSmartMemory_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleSmartMemory_Object = MibTableColumn
cpqHeResMem2ModuleSmartMemory = _CpqHeResMem2ModuleSmartMemory_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 22),
    _CpqHeResMem2ModuleSmartMemory_Type()
)
cpqHeResMem2ModuleSmartMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleSmartMemory.setStatus("mandatory")


class _CpqHeResMem2ModuleMinVoltage_Type(Integer32):
    """Custom type cpqHeResMem2ModuleMinVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHeResMem2ModuleMinVoltage_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleMinVoltage_Object = MibTableColumn
cpqHeResMem2ModuleMinVoltage = _CpqHeResMem2ModuleMinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 23),
    _CpqHeResMem2ModuleMinVoltage_Type()
)
cpqHeResMem2ModuleMinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleMinVoltage.setStatus("mandatory")


class _CpqHeResMem2ModuleRanks_Type(Integer32):
    """Custom type cpqHeResMem2ModuleRanks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHeResMem2ModuleRanks_Type.__name__ = "Integer32"
_CpqHeResMem2ModuleRanks_Object = MibTableColumn
cpqHeResMem2ModuleRanks = _CpqHeResMem2ModuleRanks_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 14, 13, 1, 24),
    _CpqHeResMem2ModuleRanks_Type()
)
cpqHeResMem2ModuleRanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeResMem2ModuleRanks.setStatus("mandatory")
_CpqHePowerMeter_ObjectIdentity = ObjectIdentity
cpqHePowerMeter = _CpqHePowerMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 15)
)


class _CpqHePowerMeterSupport_Type(Integer32):
    """Custom type cpqHePowerMeterSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("supported", 2),
          ("unsupported", 3))
    )


_CpqHePowerMeterSupport_Type.__name__ = "Integer32"
_CpqHePowerMeterSupport_Object = MibScalar
cpqHePowerMeterSupport = _CpqHePowerMeterSupport_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 15, 1),
    _CpqHePowerMeterSupport_Type()
)
cpqHePowerMeterSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePowerMeterSupport.setStatus("mandatory")


class _CpqHePowerMeterStatus_Type(Integer32):
    """Custom type cpqHePowerMeterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("other", 1),
          ("present", 2))
    )


_CpqHePowerMeterStatus_Type.__name__ = "Integer32"
_CpqHePowerMeterStatus_Object = MibScalar
cpqHePowerMeterStatus = _CpqHePowerMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 15, 2),
    _CpqHePowerMeterStatus_Type()
)
cpqHePowerMeterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePowerMeterStatus.setStatus("mandatory")
_CpqHePowerMeterCurrReading_Type = Integer32
_CpqHePowerMeterCurrReading_Object = MibScalar
cpqHePowerMeterCurrReading = _CpqHePowerMeterCurrReading_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 15, 3),
    _CpqHePowerMeterCurrReading_Type()
)
cpqHePowerMeterCurrReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePowerMeterCurrReading.setStatus("mandatory")
_CpqHePowerMeterPrevReading_Type = Integer32
_CpqHePowerMeterPrevReading_Object = MibScalar
cpqHePowerMeterPrevReading = _CpqHePowerMeterPrevReading_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 2, 15, 4),
    _CpqHePowerMeterPrevReading_Type()
)
cpqHePowerMeterPrevReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHePowerMeterPrevReading.setStatus("mandatory")
_CpqHeTrap_ObjectIdentity = ObjectIdentity
cpqHeTrap = _CpqHeTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 6, 3)
)
_CpqHeTrapPkts_Type = Counter32
_CpqHeTrapPkts_Object = MibScalar
cpqHeTrapPkts = _CpqHeTrapPkts_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 3, 1),
    _CpqHeTrapPkts_Type()
)
cpqHeTrapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTrapPkts.setStatus("deprecated")


class _CpqHeTrapLogMaxSize_Type(Integer32):
    """Custom type cpqHeTrapLogMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqHeTrapLogMaxSize_Type.__name__ = "Integer32"
_CpqHeTrapLogMaxSize_Object = MibScalar
cpqHeTrapLogMaxSize = _CpqHeTrapLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 3, 2),
    _CpqHeTrapLogMaxSize_Type()
)
cpqHeTrapLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTrapLogMaxSize.setStatus("deprecated")
_CpqHeTrapLogTable_Object = MibTable
cpqHeTrapLogTable = _CpqHeTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 3, 3)
)
if mibBuilder.loadTexts:
    cpqHeTrapLogTable.setStatus("deprecated")
_CpqHeTrapLogEntry_Object = MibTableRow
cpqHeTrapLogEntry = _CpqHeTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 3, 3, 1)
)
cpqHeTrapLogEntry.setIndexNames(
    (0, "CPQHLTH-MIB", "cpqHeTrapLogIndex"),
)
if mibBuilder.loadTexts:
    cpqHeTrapLogEntry.setStatus("deprecated")


class _CpqHeTrapLogIndex_Type(Integer32):
    """Custom type cpqHeTrapLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqHeTrapLogIndex_Type.__name__ = "Integer32"
_CpqHeTrapLogIndex_Object = MibTableColumn
cpqHeTrapLogIndex = _CpqHeTrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 3, 3, 1, 1),
    _CpqHeTrapLogIndex_Type()
)
cpqHeTrapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTrapLogIndex.setStatus("deprecated")


class _CpqHeTrapType_Type(Integer32):
    """Custom type cpqHeTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6001,
              6002,
              6003,
              6004,
              6005,
              6006,
              6007,
              6008,
              6009,
              6010,
              6011,
              6012,
              6013)
        )
    )
    namedValues = NamedValues(
        *(("cpqHe2CorrectableMemoryError", 6001),
          ("cpqHe2CorrectableMemoryLogDisabled", 6002),
          ("cpqHeAsrConfirmation", 6011),
          ("cpqHeCorrectableMemoryError", 1),
          ("cpqHeCorrectableMemoryLogDisabled", 2),
          ("cpqHePostError", 6013),
          ("cpqHeThermalConfirmation", 6012),
          ("cpqHeThermalCpuFanFailed", 6009),
          ("cpqHeThermalCpuFanOk", 6010),
          ("cpqHeThermalSystemFanDegraded", 6007),
          ("cpqHeThermalSystemFanFailed", 6006),
          ("cpqHeThermalSystemFanOk", 6008),
          ("cpqHeThermalTempDegraded", 6004),
          ("cpqHeThermalTempFailed", 6003),
          ("cpqHeThermalTempOk", 6005))
    )


_CpqHeTrapType_Type.__name__ = "Integer32"
_CpqHeTrapType_Object = MibTableColumn
cpqHeTrapType = _CpqHeTrapType_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 3, 3, 1, 2),
    _CpqHeTrapType_Type()
)
cpqHeTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTrapType.setStatus("deprecated")


class _CpqHeTrapTime_Type(OctetString):
    """Custom type cpqHeTrapTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CpqHeTrapTime_Type.__name__ = "OctetString"
_CpqHeTrapTime_Object = MibTableColumn
cpqHeTrapTime = _CpqHeTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 6, 3, 3, 1, 3),
    _CpqHeTrapTime_Type()
)
cpqHeTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHeTrapTime.setStatus("deprecated")

# Managed Objects groups


# Notification objects

cpqHe2CorrectableMemoryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6001)
)
cpqHe2CorrectableMemoryError.setObjects(
    ("CPQHLTH-MIB", "cpqHeCorrMemTotalErrs")
)
if mibBuilder.loadTexts:
    cpqHe2CorrectableMemoryError.setStatus(
        ""
    )

cpqHe2CorrectableMemoryLogDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6002)
)
cpqHe2CorrectableMemoryLogDisabled.setObjects(
    ("CPQHLTH-MIB", "cpqHeCorrMemLogStatus")
)
if mibBuilder.loadTexts:
    cpqHe2CorrectableMemoryLogDisabled.setStatus(
        ""
    )

cpqHeThermalTempFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6003)
)
if mibBuilder.loadTexts:
    cpqHeThermalTempFailed.setStatus(
        ""
    )

cpqHeThermalTempDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6004)
)
cpqHeThermalTempDegraded.setObjects(
    ("CPQHLTH-MIB", "cpqHeThermalDegradedAction")
)
if mibBuilder.loadTexts:
    cpqHeThermalTempDegraded.setStatus(
        ""
    )

cpqHeThermalTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6005)
)
if mibBuilder.loadTexts:
    cpqHeThermalTempOk.setStatus(
        ""
    )

cpqHeThermalSystemFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6006)
)
cpqHeThermalSystemFanFailed.setObjects(
    ("CPQHLTH-MIB", "cpqHeThermalDegradedAction")
)
if mibBuilder.loadTexts:
    cpqHeThermalSystemFanFailed.setStatus(
        ""
    )

cpqHeThermalSystemFanDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6007)
)
if mibBuilder.loadTexts:
    cpqHeThermalSystemFanDegraded.setStatus(
        ""
    )

cpqHeThermalSystemFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6008)
)
if mibBuilder.loadTexts:
    cpqHeThermalSystemFanOk.setStatus(
        ""
    )

cpqHeThermalCpuFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6009)
)
if mibBuilder.loadTexts:
    cpqHeThermalCpuFanFailed.setStatus(
        ""
    )

cpqHeThermalCpuFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6010)
)
if mibBuilder.loadTexts:
    cpqHeThermalCpuFanOk.setStatus(
        ""
    )

cpqHeAsrConfirmation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6011)
)
if mibBuilder.loadTexts:
    cpqHeAsrConfirmation.setStatus(
        ""
    )

cpqHeThermalConfirmation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6012)
)
if mibBuilder.loadTexts:
    cpqHeThermalConfirmation.setStatus(
        ""
    )

cpqHePostError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6013)
)
if mibBuilder.loadTexts:
    cpqHePostError.setStatus(
        ""
    )

cpqHeFltTolPwrSupplyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6014)
)
if mibBuilder.loadTexts:
    cpqHeFltTolPwrSupplyDegraded.setStatus(
        ""
    )

cpqHe3CorrectableMemoryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6015)
)
cpqHe3CorrectableMemoryError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeCorrMemTotalErrs"))
)
if mibBuilder.loadTexts:
    cpqHe3CorrectableMemoryError.setStatus(
        ""
    )

cpqHe3CorrectableMemoryLogDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6016)
)
cpqHe3CorrectableMemoryLogDisabled.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeCorrMemLogStatus"))
)
if mibBuilder.loadTexts:
    cpqHe3CorrectableMemoryLogDisabled.setStatus(
        ""
    )

cpqHe3ThermalTempFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6017)
)
cpqHe3ThermalTempFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3ThermalTempFailed.setStatus(
        ""
    )

cpqHe3ThermalTempDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6018)
)
cpqHe3ThermalTempDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeThermalDegradedAction"))
)
if mibBuilder.loadTexts:
    cpqHe3ThermalTempDegraded.setStatus(
        ""
    )

cpqHe3ThermalTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6019)
)
cpqHe3ThermalTempOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3ThermalTempOk.setStatus(
        ""
    )

cpqHe3ThermalSystemFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6020)
)
cpqHe3ThermalSystemFanFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeThermalDegradedAction"))
)
if mibBuilder.loadTexts:
    cpqHe3ThermalSystemFanFailed.setStatus(
        ""
    )

cpqHe3ThermalSystemFanDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6021)
)
cpqHe3ThermalSystemFanDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3ThermalSystemFanDegraded.setStatus(
        ""
    )

cpqHe3ThermalSystemFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6022)
)
cpqHe3ThermalSystemFanOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3ThermalSystemFanOk.setStatus(
        ""
    )

cpqHe3ThermalCpuFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6023)
)
cpqHe3ThermalCpuFanFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3ThermalCpuFanFailed.setStatus(
        ""
    )

cpqHe3ThermalCpuFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6024)
)
cpqHe3ThermalCpuFanOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3ThermalCpuFanOk.setStatus(
        ""
    )

cpqHe3AsrConfirmation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6025)
)
cpqHe3AsrConfirmation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3AsrConfirmation.setStatus(
        ""
    )

cpqHe3ThermalConfirmation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6026)
)
cpqHe3ThermalConfirmation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3ThermalConfirmation.setStatus(
        ""
    )

cpqHe3PostError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6027)
)
cpqHe3PostError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3PostError.setStatus(
        ""
    )

cpqHe3FltTolPwrSupplyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6028)
)
cpqHe3FltTolPwrSupplyDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolPwrSupplyDegraded.setStatus(
        ""
    )

cpqHe3CorrMemReplaceMemModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6029)
)
cpqHe3CorrMemReplaceMemModule.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3CorrMemReplaceMemModule.setStatus(
        ""
    )

cpqHe3FltTolPowerSupplyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6030)
)
cpqHe3FltTolPowerSupplyDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyBay"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolPowerSupplyDegraded.setStatus(
        ""
    )

cpqHe3FltTolPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6031)
)
cpqHe3FltTolPowerSupplyFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyBay"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolPowerSupplyFailed.setStatus(
        ""
    )

cpqHe3FltTolPowerRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6032)
)
cpqHe3FltTolPowerRedundancyLost.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolPowerRedundancyLost.setStatus(
        ""
    )

cpqHe3FltTolPowerSupplyInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6033)
)
cpqHe3FltTolPowerSupplyInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyBay"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolPowerSupplyInserted.setStatus(
        ""
    )

cpqHe3FltTolPowerSupplyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6034)
)
cpqHe3FltTolPowerSupplyRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyBay"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolPowerSupplyRemoved.setStatus(
        ""
    )

cpqHe3FltTolFanDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6035)
)
cpqHe3FltTolFanDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolFanChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolFanIndex"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolFanDegraded.setStatus(
        ""
    )

cpqHe3FltTolFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6036)
)
cpqHe3FltTolFanFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolFanChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolFanIndex"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolFanFailed.setStatus(
        ""
    )

cpqHe3FltTolFanRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6037)
)
cpqHe3FltTolFanRedundancyLost.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolFanChassis"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolFanRedundancyLost.setStatus(
        ""
    )

cpqHe3FltTolFanInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6038)
)
cpqHe3FltTolFanInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolFanChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolFanIndex"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolFanInserted.setStatus(
        ""
    )

cpqHe3FltTolFanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6039)
)
cpqHe3FltTolFanRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolFanChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolFanIndex"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolFanRemoved.setStatus(
        ""
    )

cpqHe3TemperatureFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6040)
)
cpqHe3TemperatureFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeTemperatureChassis"),
        ("CPQHLTH-MIB", "cpqHeTemperatureLocale"))
)
if mibBuilder.loadTexts:
    cpqHe3TemperatureFailed.setStatus(
        ""
    )

cpqHe3TemperatureDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6041)
)
cpqHe3TemperatureDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeThermalDegradedAction"),
        ("CPQHLTH-MIB", "cpqHeTemperatureChassis"),
        ("CPQHLTH-MIB", "cpqHeTemperatureLocale"))
)
if mibBuilder.loadTexts:
    cpqHe3TemperatureDegraded.setStatus(
        ""
    )

cpqHe3TemperatureOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6042)
)
cpqHe3TemperatureOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeTemperatureChassis"),
        ("CPQHLTH-MIB", "cpqHeTemperatureLocale"))
)
if mibBuilder.loadTexts:
    cpqHe3TemperatureOk.setStatus(
        ""
    )

cpqHe3PowerConverterDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6043)
)
cpqHe3PowerConverterDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHePwrConvChassis"),
        ("CPQHLTH-MIB", "cpqHePwrConvSlot"),
        ("CPQHLTH-MIB", "cpqHePwrConvSocket"))
)
if mibBuilder.loadTexts:
    cpqHe3PowerConverterDegraded.setStatus(
        ""
    )

cpqHe3PowerConverterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6044)
)
cpqHe3PowerConverterFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHePwrConvChassis"),
        ("CPQHLTH-MIB", "cpqHePwrConvSlot"),
        ("CPQHLTH-MIB", "cpqHePwrConvSocket"))
)
if mibBuilder.loadTexts:
    cpqHe3PowerConverterFailed.setStatus(
        ""
    )

cpqHe3PowerConverterRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6045)
)
cpqHe3PowerConverterRedundancyLost.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHePwrConvChassis"))
)
if mibBuilder.loadTexts:
    cpqHe3PowerConverterRedundancyLost.setStatus(
        ""
    )

cpqHe3CacheAccelParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6046)
)
cpqHe3CacheAccelParityError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHe3CacheAccelParityError.setStatus(
        ""
    )

cpqHeResilientMemOnlineSpareEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6047)
)
cpqHeResilientMemOnlineSpareEngaged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHeResilientMemOnlineSpareEngaged.setStatus(
        ""
    )

cpqHe4FltTolPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6048)
)
cpqHe4FltTolPowerSupplyOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyBay"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyStatus"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyModel"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplySerialNumber"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyAutoRev"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyFirmwareRev"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplySparePartNum"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"))
)
if mibBuilder.loadTexts:
    cpqHe4FltTolPowerSupplyOk.setStatus(
        ""
    )

cpqHe4FltTolPowerSupplyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6049)
)
cpqHe4FltTolPowerSupplyDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyBay"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyStatus"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyModel"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplySerialNumber"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyAutoRev"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyFirmwareRev"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplySparePartNum"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"))
)
if mibBuilder.loadTexts:
    cpqHe4FltTolPowerSupplyDegraded.setStatus(
        ""
    )

cpqHe4FltTolPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6050)
)
cpqHe4FltTolPowerSupplyFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyBay"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyStatus"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyModel"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplySerialNumber"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyAutoRev"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyFirmwareRev"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplySparePartNum"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"))
)
if mibBuilder.loadTexts:
    cpqHe4FltTolPowerSupplyFailed.setStatus(
        ""
    )

cpqHeResilientMemMirroredMemoryEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6051)
)
cpqHeResilientMemMirroredMemoryEngaged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHeResilientMemMirroredMemoryEngaged.setStatus(
        ""
    )

cpqHeResilientAdvancedECCMemoryEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6052)
)
cpqHeResilientAdvancedECCMemoryEngaged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHeResilientAdvancedECCMemoryEngaged.setStatus(
        ""
    )

cpqHeResilientMemXorMemoryEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6053)
)
cpqHeResilientMemXorMemoryEngaged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHeResilientMemXorMemoryEngaged.setStatus(
        ""
    )

cpqHe3FltTolPowerRedundancyRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6054)
)
cpqHe3FltTolPowerRedundancyRestored.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolPowerRedundancyRestored.setStatus(
        ""
    )

cpqHe3FltTolFanRedundancyRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6055)
)
cpqHe3FltTolFanRedundancyRestored.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolFanChassis"))
)
if mibBuilder.loadTexts:
    cpqHe3FltTolFanRedundancyRestored.setStatus(
        ""
    )

cpqHe4CorrMemReplaceMemModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6056)
)
cpqHe4CorrMemReplaceMemModule.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeResMemBoardIndex"),
        ("CPQHLTH-MIB", "cpqHeResMemModuleIndex"),
        ("CPQHLTH-MIB", "cpqHeResMemModuleSparePartNo"),
        ("CPQSINFO-MIB", "cpqSiMemModuleSize"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"))
)
if mibBuilder.loadTexts:
    cpqHe4CorrMemReplaceMemModule.setStatus(
        ""
    )

cpqHeResMemBoardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6057)
)
cpqHeResMemBoardRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeResMemBoardSlotIndex"))
)
if mibBuilder.loadTexts:
    cpqHeResMemBoardRemoved.setStatus(
        ""
    )

cpqHeResMemBoardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6058)
)
cpqHeResMemBoardInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeResMemBoardSlotIndex"))
)
if mibBuilder.loadTexts:
    cpqHeResMemBoardInserted.setStatus(
        ""
    )

cpqHeResMemBoardBusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6059)
)
cpqHeResMemBoardBusError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeResMemBoardSlotIndex"))
)
if mibBuilder.loadTexts:
    cpqHeResMemBoardBusError.setStatus(
        ""
    )

cpqHeEventOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6060)
)
cpqHeEventOccurred.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeEventLogEntryNumber"),
        ("CPQHLTH-MIB", "cpqHeEventLogEntrySeverity"),
        ("CPQHLTH-MIB", "cpqHeEventLogUpdateTime"),
        ("CPQHLTH-MIB", "cpqHeEventLogErrorDesc"))
)
if mibBuilder.loadTexts:
    cpqHeEventOccurred.setStatus(
        ""
    )

cpqHeManagementProcInReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6061)
)
cpqHeManagementProcInReset.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHeManagementProcInReset.setStatus(
        ""
    )

cpqHeManagementProcReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6062)
)
cpqHeManagementProcReady.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHeManagementProcReady.setStatus(
        ""
    )

cpqHeManagementProcFailedReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6063)
)
cpqHeManagementProcFailedReset.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHeManagementProcFailedReset.setStatus(
        ""
    )

cpqHe5CorrMemReplaceMemModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6064)
)
cpqHe5CorrMemReplaceMemModule.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeResMem2BoardNum"),
        ("CPQHLTH-MIB", "cpqHeResMem2CpuNum"),
        ("CPQHLTH-MIB", "cpqHeResMem2RiserNum"),
        ("CPQHLTH-MIB", "cpqHeResMem2ModuleNum"),
        ("CPQHLTH-MIB", "cpqHeResMem2ModulePartNo"),
        ("CPQHLTH-MIB", "cpqHeResMem2ModuleSize"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"))
)
if mibBuilder.loadTexts:
    cpqHe5CorrMemReplaceMemModule.setStatus(
        ""
    )

cpqHe5ResMemBoardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6065)
)
cpqHe5ResMemBoardRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeResMem2BoardSlotNum"),
        ("CPQHLTH-MIB", "cpqHeResMem2BoardCpuNum"),
        ("CPQHLTH-MIB", "cpqHeResMem2BoardRiserNum"))
)
if mibBuilder.loadTexts:
    cpqHe5ResMemBoardRemoved.setStatus(
        ""
    )

cpqHe5ResMemBoardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6066)
)
cpqHe5ResMemBoardInserted.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeResMem2BoardSlotNum"),
        ("CPQHLTH-MIB", "cpqHeResMem2BoardCpuNum"),
        ("CPQHLTH-MIB", "cpqHeResMem2BoardRiserNum"))
)
if mibBuilder.loadTexts:
    cpqHe5ResMemBoardInserted.setStatus(
        ""
    )

cpqHe5ResMemBoardBusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6067)
)
cpqHe5ResMemBoardBusError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeResMem2BoardSlotNum"),
        ("CPQHLTH-MIB", "cpqHeResMem2BoardCpuNum"),
        ("CPQHLTH-MIB", "cpqHeResMem2BoardRiserNum"))
)
if mibBuilder.loadTexts:
    cpqHe5ResMemBoardBusError.setStatus(
        ""
    )

cpqHeResilientMemLockStepMemoryEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6068)
)
cpqHeResilientMemLockStepMemoryEngaged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqHeResilientMemLockStepMemoryEngaged.setStatus(
        ""
    )

cpqHe4FltTolPowerSupplyACpowerloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 6069)
)
cpqHe4FltTolPowerSupplyACpowerloss.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyChassis"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyBay"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyStatus"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyModel"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplySerialNumber"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyAutoRev"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplyFirmwareRev"),
        ("CPQHLTH-MIB", "cpqHeFltTolPowerSupplySparePartNum"),
        ("CPQSINFO-MIB", "cpqSiServerSystemId"))
)
if mibBuilder.loadTexts:
    cpqHe4FltTolPowerSupplyACpowerloss.setStatus(
        ""
    )

cpqHeCorrectableMemoryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 6, 0, 1)
)
cpqHeCorrectableMemoryError.setObjects(
    ("CPQHLTH-MIB", "cpqHeCorrMemTotalErrs")
)
if mibBuilder.loadTexts:
    cpqHeCorrectableMemoryError.setStatus(
        ""
    )

cpqHeCorrectableMemoryLogDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 6, 0, 2)
)
cpqHeCorrectableMemoryLogDisabled.setObjects(
    ("CPQHLTH-MIB", "cpqHeCorrMemLogStatus")
)
if mibBuilder.loadTexts:
    cpqHeCorrectableMemoryLogDisabled.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQHLTH-MIB",
    **{"cpqHe2CorrectableMemoryError": cpqHe2CorrectableMemoryError,
       "cpqHe2CorrectableMemoryLogDisabled": cpqHe2CorrectableMemoryLogDisabled,
       "cpqHeThermalTempFailed": cpqHeThermalTempFailed,
       "cpqHeThermalTempDegraded": cpqHeThermalTempDegraded,
       "cpqHeThermalTempOk": cpqHeThermalTempOk,
       "cpqHeThermalSystemFanFailed": cpqHeThermalSystemFanFailed,
       "cpqHeThermalSystemFanDegraded": cpqHeThermalSystemFanDegraded,
       "cpqHeThermalSystemFanOk": cpqHeThermalSystemFanOk,
       "cpqHeThermalCpuFanFailed": cpqHeThermalCpuFanFailed,
       "cpqHeThermalCpuFanOk": cpqHeThermalCpuFanOk,
       "cpqHeAsrConfirmation": cpqHeAsrConfirmation,
       "cpqHeThermalConfirmation": cpqHeThermalConfirmation,
       "cpqHePostError": cpqHePostError,
       "cpqHeFltTolPwrSupplyDegraded": cpqHeFltTolPwrSupplyDegraded,
       "cpqHe3CorrectableMemoryError": cpqHe3CorrectableMemoryError,
       "cpqHe3CorrectableMemoryLogDisabled": cpqHe3CorrectableMemoryLogDisabled,
       "cpqHe3ThermalTempFailed": cpqHe3ThermalTempFailed,
       "cpqHe3ThermalTempDegraded": cpqHe3ThermalTempDegraded,
       "cpqHe3ThermalTempOk": cpqHe3ThermalTempOk,
       "cpqHe3ThermalSystemFanFailed": cpqHe3ThermalSystemFanFailed,
       "cpqHe3ThermalSystemFanDegraded": cpqHe3ThermalSystemFanDegraded,
       "cpqHe3ThermalSystemFanOk": cpqHe3ThermalSystemFanOk,
       "cpqHe3ThermalCpuFanFailed": cpqHe3ThermalCpuFanFailed,
       "cpqHe3ThermalCpuFanOk": cpqHe3ThermalCpuFanOk,
       "cpqHe3AsrConfirmation": cpqHe3AsrConfirmation,
       "cpqHe3ThermalConfirmation": cpqHe3ThermalConfirmation,
       "cpqHe3PostError": cpqHe3PostError,
       "cpqHe3FltTolPwrSupplyDegraded": cpqHe3FltTolPwrSupplyDegraded,
       "cpqHe3CorrMemReplaceMemModule": cpqHe3CorrMemReplaceMemModule,
       "cpqHe3FltTolPowerSupplyDegraded": cpqHe3FltTolPowerSupplyDegraded,
       "cpqHe3FltTolPowerSupplyFailed": cpqHe3FltTolPowerSupplyFailed,
       "cpqHe3FltTolPowerRedundancyLost": cpqHe3FltTolPowerRedundancyLost,
       "cpqHe3FltTolPowerSupplyInserted": cpqHe3FltTolPowerSupplyInserted,
       "cpqHe3FltTolPowerSupplyRemoved": cpqHe3FltTolPowerSupplyRemoved,
       "cpqHe3FltTolFanDegraded": cpqHe3FltTolFanDegraded,
       "cpqHe3FltTolFanFailed": cpqHe3FltTolFanFailed,
       "cpqHe3FltTolFanRedundancyLost": cpqHe3FltTolFanRedundancyLost,
       "cpqHe3FltTolFanInserted": cpqHe3FltTolFanInserted,
       "cpqHe3FltTolFanRemoved": cpqHe3FltTolFanRemoved,
       "cpqHe3TemperatureFailed": cpqHe3TemperatureFailed,
       "cpqHe3TemperatureDegraded": cpqHe3TemperatureDegraded,
       "cpqHe3TemperatureOk": cpqHe3TemperatureOk,
       "cpqHe3PowerConverterDegraded": cpqHe3PowerConverterDegraded,
       "cpqHe3PowerConverterFailed": cpqHe3PowerConverterFailed,
       "cpqHe3PowerConverterRedundancyLost": cpqHe3PowerConverterRedundancyLost,
       "cpqHe3CacheAccelParityError": cpqHe3CacheAccelParityError,
       "cpqHeResilientMemOnlineSpareEngaged": cpqHeResilientMemOnlineSpareEngaged,
       "cpqHe4FltTolPowerSupplyOk": cpqHe4FltTolPowerSupplyOk,
       "cpqHe4FltTolPowerSupplyDegraded": cpqHe4FltTolPowerSupplyDegraded,
       "cpqHe4FltTolPowerSupplyFailed": cpqHe4FltTolPowerSupplyFailed,
       "cpqHeResilientMemMirroredMemoryEngaged": cpqHeResilientMemMirroredMemoryEngaged,
       "cpqHeResilientAdvancedECCMemoryEngaged": cpqHeResilientAdvancedECCMemoryEngaged,
       "cpqHeResilientMemXorMemoryEngaged": cpqHeResilientMemXorMemoryEngaged,
       "cpqHe3FltTolPowerRedundancyRestored": cpqHe3FltTolPowerRedundancyRestored,
       "cpqHe3FltTolFanRedundancyRestored": cpqHe3FltTolFanRedundancyRestored,
       "cpqHe4CorrMemReplaceMemModule": cpqHe4CorrMemReplaceMemModule,
       "cpqHeResMemBoardRemoved": cpqHeResMemBoardRemoved,
       "cpqHeResMemBoardInserted": cpqHeResMemBoardInserted,
       "cpqHeResMemBoardBusError": cpqHeResMemBoardBusError,
       "cpqHeEventOccurred": cpqHeEventOccurred,
       "cpqHeManagementProcInReset": cpqHeManagementProcInReset,
       "cpqHeManagementProcReady": cpqHeManagementProcReady,
       "cpqHeManagementProcFailedReset": cpqHeManagementProcFailedReset,
       "cpqHe5CorrMemReplaceMemModule": cpqHe5CorrMemReplaceMemModule,
       "cpqHe5ResMemBoardRemoved": cpqHe5ResMemBoardRemoved,
       "cpqHe5ResMemBoardInserted": cpqHe5ResMemBoardInserted,
       "cpqHe5ResMemBoardBusError": cpqHe5ResMemBoardBusError,
       "cpqHeResilientMemLockStepMemoryEngaged": cpqHeResilientMemLockStepMemoryEngaged,
       "cpqHe4FltTolPowerSupplyACpowerloss": cpqHe4FltTolPowerSupplyACpowerloss,
       "cpqHealth": cpqHealth,
       "cpqHeCorrectableMemoryError": cpqHeCorrectableMemoryError,
       "cpqHeCorrectableMemoryLogDisabled": cpqHeCorrectableMemoryLogDisabled,
       "cpqHeMibRev": cpqHeMibRev,
       "cpqHeMibRevMajor": cpqHeMibRevMajor,
       "cpqHeMibRevMinor": cpqHeMibRevMinor,
       "cpqHeMibCondition": cpqHeMibCondition,
       "cpqHeComponent": cpqHeComponent,
       "cpqHeInterface": cpqHeInterface,
       "cpqHeOsNetWare3x": cpqHeOsNetWare3x,
       "cpqHeNw3xDriverName": cpqHeNw3xDriverName,
       "cpqHeNw3xDriverDate": cpqHeNw3xDriverDate,
       "cpqHeNw3xDriverVersion": cpqHeNw3xDriverVersion,
       "cpqHeOsCommon": cpqHeOsCommon,
       "cpqHeOsCommonPollFreq": cpqHeOsCommonPollFreq,
       "cpqHeOsCommonModuleTable": cpqHeOsCommonModuleTable,
       "cpqHeOsCommonModuleEntry": cpqHeOsCommonModuleEntry,
       "cpqHeOsCommonModuleIndex": cpqHeOsCommonModuleIndex,
       "cpqHeOsCommonModuleName": cpqHeOsCommonModuleName,
       "cpqHeOsCommonModuleVersion": cpqHeOsCommonModuleVersion,
       "cpqHeOsCommonModuleDate": cpqHeOsCommonModuleDate,
       "cpqHeOsCommonModulePurpose": cpqHeOsCommonModulePurpose,
       "cpqHeCriticalError": cpqHeCriticalError,
       "cpqHeCritLogSupported": cpqHeCritLogSupported,
       "cpqHeCritLogCondition": cpqHeCritLogCondition,
       "cpqHeLastCritErrorAbendMsg": cpqHeLastCritErrorAbendMsg,
       "cpqHeCriticalErrorTable": cpqHeCriticalErrorTable,
       "cpqHeCriticalErrorEntry": cpqHeCriticalErrorEntry,
       "cpqHeCriticalErrorIndex": cpqHeCriticalErrorIndex,
       "cpqHeCriticalErrorStatus": cpqHeCriticalErrorStatus,
       "cpqHeCriticalErrorType": cpqHeCriticalErrorType,
       "cpqHeCriticalErrorTime": cpqHeCriticalErrorTime,
       "cpqHeCriticalErrorInfo": cpqHeCriticalErrorInfo,
       "cpqHeCriticalErrorDesc": cpqHeCriticalErrorDesc,
       "cpqHeCorrectableMemory": cpqHeCorrectableMemory,
       "cpqHeCorrMemLogStatus": cpqHeCorrMemLogStatus,
       "cpqHeCorrMemLogCondition": cpqHeCorrMemLogCondition,
       "cpqHeCorrMemTotalErrs": cpqHeCorrMemTotalErrs,
       "cpqHeCorrMemErrTable": cpqHeCorrMemErrTable,
       "cpqHeCorrMemErrEntry": cpqHeCorrMemErrEntry,
       "cpqHeCorrMemErrIndex": cpqHeCorrMemErrIndex,
       "cpqHeCorrMemErrCount": cpqHeCorrMemErrCount,
       "cpqHeCorrMemErrTime": cpqHeCorrMemErrTime,
       "cpqHeCorrMemErrDdr": cpqHeCorrMemErrDdr,
       "cpqHeCorrMemErrSyndrome": cpqHeCorrMemErrSyndrome,
       "cpqHeCorrMemErrDesc": cpqHeCorrMemErrDesc,
       "cpqHeCorrMemErrHwLocation": cpqHeCorrMemErrHwLocation,
       "cpqHeCorrMemErrorCntThresh": cpqHeCorrMemErrorCntThresh,
       "cpqHeAsr": cpqHeAsr,
       "cpqHeAsrStatus": cpqHeAsrStatus,
       "cpqHeAsrMajorVersion": cpqHeAsrMajorVersion,
       "cpqHeAsrMinorVersion": cpqHeAsrMinorVersion,
       "cpqHeAsrTimeout": cpqHeAsrTimeout,
       "cpqHeAsrBaseIo": cpqHeAsrBaseIo,
       "cpqHeAsrPost": cpqHeAsrPost,
       "cpqHeAsrReset": cpqHeAsrReset,
       "cpqHeAsrReboot": cpqHeAsrReboot,
       "cpqHeAsrRebootLimit": cpqHeAsrRebootLimit,
       "cpqHeAsrRebootCount": cpqHeAsrRebootCount,
       "cpqHeAsrPagerStatus": cpqHeAsrPagerStatus,
       "cpqHeAsrPagerNumber": cpqHeAsrPagerNumber,
       "cpqHeAsrCommPort": cpqHeAsrCommPort,
       "cpqHeAsrBaudRate": cpqHeAsrBaudRate,
       "cpqHeAsrPagerMessage": cpqHeAsrPagerMessage,
       "cpqHeAsrBootFail": cpqHeAsrBootFail,
       "cpqHeAsrCondition": cpqHeAsrCondition,
       "cpqHeAsrDialInStatus": cpqHeAsrDialInStatus,
       "cpqHeAsrDialOutStatus": cpqHeAsrDialOutStatus,
       "cpqHeAsrDialOutNumber": cpqHeAsrDialOutNumber,
       "cpqHeAsrNetworkAccessStatus": cpqHeAsrNetworkAccessStatus,
       "cpqHeAsrPollTime": cpqHeAsrPollTime,
       "cpqHeThermal": cpqHeThermal,
       "cpqHeThermalCondition": cpqHeThermalCondition,
       "cpqHeThermalDegradedAction": cpqHeThermalDegradedAction,
       "cpqHeThermalTempStatus": cpqHeThermalTempStatus,
       "cpqHeThermalSystemFanStatus": cpqHeThermalSystemFanStatus,
       "cpqHeThermalCpuFanStatus": cpqHeThermalCpuFanStatus,
       "cpqHeThermalFanTable": cpqHeThermalFanTable,
       "cpqHeThermalFanEntry": cpqHeThermalFanEntry,
       "cpqHeThermalFanIndex": cpqHeThermalFanIndex,
       "cpqHeThermalFanRequired": cpqHeThermalFanRequired,
       "cpqHeThermalFanPresent": cpqHeThermalFanPresent,
       "cpqHeThermalFanCpuFan": cpqHeThermalFanCpuFan,
       "cpqHeThermalFanStatus": cpqHeThermalFanStatus,
       "cpqHeThermalFanHwLocation": cpqHeThermalFanHwLocation,
       "cpqHeThermalFanCurrentSpeed": cpqHeThermalFanCurrentSpeed,
       "cpqHeFltTolFanTable": cpqHeFltTolFanTable,
       "cpqHeFltTolFanEntry": cpqHeFltTolFanEntry,
       "cpqHeFltTolFanChassis": cpqHeFltTolFanChassis,
       "cpqHeFltTolFanIndex": cpqHeFltTolFanIndex,
       "cpqHeFltTolFanLocale": cpqHeFltTolFanLocale,
       "cpqHeFltTolFanPresent": cpqHeFltTolFanPresent,
       "cpqHeFltTolFanType": cpqHeFltTolFanType,
       "cpqHeFltTolFanSpeed": cpqHeFltTolFanSpeed,
       "cpqHeFltTolFanRedundant": cpqHeFltTolFanRedundant,
       "cpqHeFltTolFanRedundantPartner": cpqHeFltTolFanRedundantPartner,
       "cpqHeFltTolFanCondition": cpqHeFltTolFanCondition,
       "cpqHeFltTolFanHotPlug": cpqHeFltTolFanHotPlug,
       "cpqHeFltTolFanHwLocation": cpqHeFltTolFanHwLocation,
       "cpqHeFltTolFanCurrentSpeed": cpqHeFltTolFanCurrentSpeed,
       "cpqHeTemperatureTable": cpqHeTemperatureTable,
       "cpqHeTemperatureEntry": cpqHeTemperatureEntry,
       "cpqHeTemperatureChassis": cpqHeTemperatureChassis,
       "cpqHeTemperatureIndex": cpqHeTemperatureIndex,
       "cpqHeTemperatureLocale": cpqHeTemperatureLocale,
       "cpqHeTemperatureCelsius": cpqHeTemperatureCelsius,
       "cpqHeTemperatureThreshold": cpqHeTemperatureThreshold,
       "cpqHeTemperatureCondition": cpqHeTemperatureCondition,
       "cpqHeTemperatureThresholdType": cpqHeTemperatureThresholdType,
       "cpqHeTemperatureHwLocation": cpqHeTemperatureHwLocation,
       "cpqHePostMsg": cpqHePostMsg,
       "cpqHePostMsgCondition": cpqHePostMsgCondition,
       "cpqHePostMsgTable": cpqHePostMsgTable,
       "cpqHePostMsgEntry": cpqHePostMsgEntry,
       "cpqHePostMsgIndex": cpqHePostMsgIndex,
       "cpqHePostMsgCode": cpqHePostMsgCode,
       "cpqHePostMsgDesc": cpqHePostMsgDesc,
       "cpqHePostMsgEv": cpqHePostMsgEv,
       "cpqHeSysUtil": cpqHeSysUtil,
       "cpqHeSysUtilLifeTime": cpqHeSysUtilLifeTime,
       "cpqHeSysUtilEisaBusMin": cpqHeSysUtilEisaBusMin,
       "cpqHeSysUtilEisaBusFiveMin": cpqHeSysUtilEisaBusFiveMin,
       "cpqHeSysUtilEisaBusThirtyMin": cpqHeSysUtilEisaBusThirtyMin,
       "cpqHeSysUtilEisaBusHour": cpqHeSysUtilEisaBusHour,
       "cpqHeSysUtilPciTable": cpqHeSysUtilPciTable,
       "cpqHeSysUtilPciEntry": cpqHeSysUtilPciEntry,
       "cpqHeSysUtilPciIndex": cpqHeSysUtilPciIndex,
       "cpqHeSysUtilPciBus": cpqHeSysUtilPciBus,
       "cpqHeSysUtilPciDevice": cpqHeSysUtilPciDevice,
       "cpqHeSysUtilPciMin": cpqHeSysUtilPciMin,
       "cpqHeSysUtilPciFiveMin": cpqHeSysUtilPciFiveMin,
       "cpqHeSysUtilPciThirtyMin": cpqHeSysUtilPciThirtyMin,
       "cpqHeSysUtilPciHour": cpqHeSysUtilPciHour,
       "cpqHeSysUtilPciHwLocation": cpqHeSysUtilPciHwLocation,
       "cpqHeFltTolPwrSupply": cpqHeFltTolPwrSupply,
       "cpqHeFltTolPwrSupplyCondition": cpqHeFltTolPwrSupplyCondition,
       "cpqHeFltTolPwrSupplyStatus": cpqHeFltTolPwrSupplyStatus,
       "cpqHeFltTolPowerSupplyTable": cpqHeFltTolPowerSupplyTable,
       "cpqHeFltTolPowerSupplyEntry": cpqHeFltTolPowerSupplyEntry,
       "cpqHeFltTolPowerSupplyChassis": cpqHeFltTolPowerSupplyChassis,
       "cpqHeFltTolPowerSupplyBay": cpqHeFltTolPowerSupplyBay,
       "cpqHeFltTolPowerSupplyPresent": cpqHeFltTolPowerSupplyPresent,
       "cpqHeFltTolPowerSupplyCondition": cpqHeFltTolPowerSupplyCondition,
       "cpqHeFltTolPowerSupplyStatus": cpqHeFltTolPowerSupplyStatus,
       "cpqHeFltTolPowerSupplyMainVoltage": cpqHeFltTolPowerSupplyMainVoltage,
       "cpqHeFltTolPowerSupplyCapacityUsed": cpqHeFltTolPowerSupplyCapacityUsed,
       "cpqHeFltTolPowerSupplyCapacityMaximum": cpqHeFltTolPowerSupplyCapacityMaximum,
       "cpqHeFltTolPowerSupplyRedundant": cpqHeFltTolPowerSupplyRedundant,
       "cpqHeFltTolPowerSupplyModel": cpqHeFltTolPowerSupplyModel,
       "cpqHeFltTolPowerSupplySerialNumber": cpqHeFltTolPowerSupplySerialNumber,
       "cpqHeFltTolPowerSupplyAutoRev": cpqHeFltTolPowerSupplyAutoRev,
       "cpqHeFltTolPowerSupplyHotPlug": cpqHeFltTolPowerSupplyHotPlug,
       "cpqHeFltTolPowerSupplyFirmwareRev": cpqHeFltTolPowerSupplyFirmwareRev,
       "cpqHeFltTolPowerSupplyHwLocation": cpqHeFltTolPowerSupplyHwLocation,
       "cpqHeFltTolPowerSupplySparePartNum": cpqHeFltTolPowerSupplySparePartNum,
       "cpqHeFltTolPowerSupplyRedundantPartner": cpqHeFltTolPowerSupplyRedundantPartner,
       "cpqHeFltTolPowerSupplyErrorCondition": cpqHeFltTolPowerSupplyErrorCondition,
       "cpqHeIRC": cpqHeIRC,
       "cpqHeIRCStatus": cpqHeIRCStatus,
       "cpqHeEventLog": cpqHeEventLog,
       "cpqHeEventLogSupported": cpqHeEventLogSupported,
       "cpqHeEventLogCondition": cpqHeEventLogCondition,
       "cpqHeEventLogTable": cpqHeEventLogTable,
       "cpqHeEventLogEntry": cpqHeEventLogEntry,
       "cpqHeEventLogEntryNumber": cpqHeEventLogEntryNumber,
       "cpqHeEventLogEntrySeverity": cpqHeEventLogEntrySeverity,
       "cpqHeEventLogEntryClass": cpqHeEventLogEntryClass,
       "cpqHeEventLogEntryCode": cpqHeEventLogEntryCode,
       "cpqHeEventLogEntryCount": cpqHeEventLogEntryCount,
       "cpqHeEventLogInitialTime": cpqHeEventLogInitialTime,
       "cpqHeEventLogUpdateTime": cpqHeEventLogUpdateTime,
       "cpqHeEventLogErrorDesc": cpqHeEventLogErrorDesc,
       "cpqHeEventLogFreeFormData": cpqHeEventLogFreeFormData,
       "cpqHeMgmtDisplay": cpqHeMgmtDisplay,
       "cpqHeMgmtDisplayType": cpqHeMgmtDisplayType,
       "cpqHeMgmtDisplayText": cpqHeMgmtDisplayText,
       "cpqHeMgmtUID": cpqHeMgmtUID,
       "cpqHePowerConverter": cpqHePowerConverter,
       "cpqHePowerConverterSupported": cpqHePowerConverterSupported,
       "cpqHePowerConverterCondition": cpqHePowerConverterCondition,
       "cpqHePowerConverterTable": cpqHePowerConverterTable,
       "cpqHePowerConverterEntry": cpqHePowerConverterEntry,
       "cpqHePwrConvChassis": cpqHePwrConvChassis,
       "cpqHePwrConvIndex": cpqHePwrConvIndex,
       "cpqHePwrConvPresent": cpqHePwrConvPresent,
       "cpqHePwrConvSlot": cpqHePwrConvSlot,
       "cpqHePwrConvSocket": cpqHePwrConvSocket,
       "cpqHePwrConvRedundant": cpqHePwrConvRedundant,
       "cpqHePwrConvRedundantGroupId": cpqHePwrConvRedundantGroupId,
       "cpqHePwrConvCondition": cpqHePwrConvCondition,
       "cpqHePwrConvHwLocation": cpqHePwrConvHwLocation,
       "cpqHeResilientMemory": cpqHeResilientMemory,
       "cpqHeResilientMemTypeActive": cpqHeResilientMemTypeActive,
       "cpqHeResilientMemTypeAvailable": cpqHeResilientMemTypeAvailable,
       "cpqHeResilientMemStatus": cpqHeResilientMemStatus,
       "cpqHeResilientMemCondition": cpqHeResilientMemCondition,
       "cpqHeResilientMemHotPlug": cpqHeResilientMemHotPlug,
       "cpqHeResilientMemOperatingSpeed": cpqHeResilientMemOperatingSpeed,
       "cpqHeResilientMemOsMemSize": cpqHeResilientMemOsMemSize,
       "cpqHeResilientMemTotalMemSize": cpqHeResilientMemTotalMemSize,
       "cpqHeResilientMemRivState": cpqHeResilientMemRivState,
       "cpqHeResMemBoardTable": cpqHeResMemBoardTable,
       "cpqHeResMemBoardEntry": cpqHeResMemBoardEntry,
       "cpqHeResMemBoardSlotIndex": cpqHeResMemBoardSlotIndex,
       "cpqHeResMemBoardOnlineStatus": cpqHeResMemBoardOnlineStatus,
       "cpqHeResMemBoardErrorStatus": cpqHeResMemBoardErrorStatus,
       "cpqHeResMemBoardLocked": cpqHeResMemBoardLocked,
       "cpqHeResMemBoardNumSockets": cpqHeResMemBoardNumSockets,
       "cpqHeResMemBoardOsMemSize": cpqHeResMemBoardOsMemSize,
       "cpqHeResMemBoardTotalMemSize": cpqHeResMemBoardTotalMemSize,
       "cpqHeResMemBoardCondition": cpqHeResMemBoardCondition,
       "cpqHeResMemBoardHotPlug": cpqHeResMemBoardHotPlug,
       "cpqHeResMemModuleTable": cpqHeResMemModuleTable,
       "cpqHeResMemModuleEntry": cpqHeResMemModuleEntry,
       "cpqHeResMemBoardIndex": cpqHeResMemBoardIndex,
       "cpqHeResMemModuleIndex": cpqHeResMemModuleIndex,
       "cpqHeResMemModuleSparePartNo": cpqHeResMemModuleSparePartNo,
       "cpqHeResMemModuleStatus": cpqHeResMemModuleStatus,
       "cpqHeResMemModuleCondition": cpqHeResMemModuleCondition,
       "cpqHeResMemModuleSpd": cpqHeResMemModuleSpd,
       "cpqHeResMem2BoardTable": cpqHeResMem2BoardTable,
       "cpqHeResMem2BoardEntry": cpqHeResMem2BoardEntry,
       "cpqHeResMem2BoardIndex": cpqHeResMem2BoardIndex,
       "cpqHeResMem2BoardSlotNum": cpqHeResMem2BoardSlotNum,
       "cpqHeResMem2BoardCpuNum": cpqHeResMem2BoardCpuNum,
       "cpqHeResMem2BoardRiserNum": cpqHeResMem2BoardRiserNum,
       "cpqHeResMem2BoardOnlineStatus": cpqHeResMem2BoardOnlineStatus,
       "cpqHeResMem2BoardErrorStatus": cpqHeResMem2BoardErrorStatus,
       "cpqHeResMem2BoardLocked": cpqHeResMem2BoardLocked,
       "cpqHeResMem2BoardNumSockets": cpqHeResMem2BoardNumSockets,
       "cpqHeResMem2BoardOsMemSize": cpqHeResMem2BoardOsMemSize,
       "cpqHeResMem2BoardTotalMemSize": cpqHeResMem2BoardTotalMemSize,
       "cpqHeResMem2BoardCondition": cpqHeResMem2BoardCondition,
       "cpqHeResMem2BoardHotPlug": cpqHeResMem2BoardHotPlug,
       "cpqHeResMem2BoardOperatingFrequency": cpqHeResMem2BoardOperatingFrequency,
       "cpqHeResMem2BoardOperatingVoltage": cpqHeResMem2BoardOperatingVoltage,
       "cpqHeResMem2ModuleTable": cpqHeResMem2ModuleTable,
       "cpqHeResMem2ModuleEntry": cpqHeResMem2ModuleEntry,
       "cpqHeResMem2Module": cpqHeResMem2Module,
       "cpqHeResMem2BoardNum": cpqHeResMem2BoardNum,
       "cpqHeResMem2CpuNum": cpqHeResMem2CpuNum,
       "cpqHeResMem2RiserNum": cpqHeResMem2RiserNum,
       "cpqHeResMem2ModuleNum": cpqHeResMem2ModuleNum,
       "cpqHeResMem2ModuleSize": cpqHeResMem2ModuleSize,
       "cpqHeResMem2ModuleType": cpqHeResMem2ModuleType,
       "cpqHeResMem2ModuleTechnology": cpqHeResMem2ModuleTechnology,
       "cpqHeResMem2ModuleManufacturer": cpqHeResMem2ModuleManufacturer,
       "cpqHeResMem2ModulePartNo": cpqHeResMem2ModulePartNo,
       "cpqHeResMem2ModuleDate": cpqHeResMem2ModuleDate,
       "cpqHeResMem2ModuleSerialNo": cpqHeResMem2ModuleSerialNo,
       "cpqHeResMem2ModuleHwLocation": cpqHeResMem2ModuleHwLocation,
       "cpqHeResMem2ModuleFrequency": cpqHeResMem2ModuleFrequency,
       "cpqHeResMem2ModuleCellTablePtr": cpqHeResMem2ModuleCellTablePtr,
       "cpqHeResMem2ModuleCellStatus": cpqHeResMem2ModuleCellStatus,
       "cpqHeResMem2ModulePartNoMfgr": cpqHeResMem2ModulePartNoMfgr,
       "cpqHeResMem2ModuleSerialNoMfgr": cpqHeResMem2ModuleSerialNoMfgr,
       "cpqHeResMem2ModuleStatus": cpqHeResMem2ModuleStatus,
       "cpqHeResMem2ModuleCondition": cpqHeResMem2ModuleCondition,
       "cpqHeResMem2ModuleSpd": cpqHeResMem2ModuleSpd,
       "cpqHeResMem2ModuleSmartMemory": cpqHeResMem2ModuleSmartMemory,
       "cpqHeResMem2ModuleMinVoltage": cpqHeResMem2ModuleMinVoltage,
       "cpqHeResMem2ModuleRanks": cpqHeResMem2ModuleRanks,
       "cpqHePowerMeter": cpqHePowerMeter,
       "cpqHePowerMeterSupport": cpqHePowerMeterSupport,
       "cpqHePowerMeterStatus": cpqHePowerMeterStatus,
       "cpqHePowerMeterCurrReading": cpqHePowerMeterCurrReading,
       "cpqHePowerMeterPrevReading": cpqHePowerMeterPrevReading,
       "cpqHeTrap": cpqHeTrap,
       "cpqHeTrapPkts": cpqHeTrapPkts,
       "cpqHeTrapLogMaxSize": cpqHeTrapLogMaxSize,
       "cpqHeTrapLogTable": cpqHeTrapLogTable,
       "cpqHeTrapLogEntry": cpqHeTrapLogEntry,
       "cpqHeTrapLogIndex": cpqHeTrapLogIndex,
       "cpqHeTrapType": cpqHeTrapType,
       "cpqHeTrapTime": cpqHeTrapTime}
)
