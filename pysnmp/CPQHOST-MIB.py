# SNMP MIB module (CPQHOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQHOST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:47 2024
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

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_CpqHostOs_ObjectIdentity = ObjectIdentity
cpqHostOs = _CpqHostOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11)
)
_CpqHoMibRev_ObjectIdentity = ObjectIdentity
cpqHoMibRev = _CpqHoMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 1)
)


class _CpqHoMibRevMajor_Type(Integer32):
    """Custom type cpqHoMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqHoMibRevMajor_Type.__name__ = "Integer32"
_CpqHoMibRevMajor_Object = MibScalar
cpqHoMibRevMajor = _CpqHoMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 1, 1),
    _CpqHoMibRevMajor_Type()
)
cpqHoMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoMibRevMajor.setStatus("mandatory")


class _CpqHoMibRevMinor_Type(Integer32):
    """Custom type cpqHoMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoMibRevMinor_Type.__name__ = "Integer32"
_CpqHoMibRevMinor_Object = MibScalar
cpqHoMibRevMinor = _CpqHoMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 1, 2),
    _CpqHoMibRevMinor_Type()
)
cpqHoMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoMibRevMinor.setStatus("mandatory")


class _CpqHoMibCondition_Type(Integer32):
    """Custom type cpqHoMibCondition based on Integer32"""
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
          ("unknown", 1))
    )


_CpqHoMibCondition_Type.__name__ = "Integer32"
_CpqHoMibCondition_Object = MibScalar
cpqHoMibCondition = _CpqHoMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 1, 3),
    _CpqHoMibCondition_Type()
)
cpqHoMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoMibCondition.setStatus("mandatory")
_CpqHoComponent_ObjectIdentity = ObjectIdentity
cpqHoComponent = _CpqHoComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2)
)
_CpqHoInterface_ObjectIdentity = ObjectIdentity
cpqHoInterface = _CpqHoInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 1)
)
_CpqHoOsCommon_ObjectIdentity = ObjectIdentity
cpqHoOsCommon = _CpqHoOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4)
)


class _CpqHoOsCommonPollFreq_Type(Integer32):
    """Custom type cpqHoOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqHoOsCommonPollFreq_Object = MibScalar
cpqHoOsCommonPollFreq = _CpqHoOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 1),
    _CpqHoOsCommonPollFreq_Type()
)
cpqHoOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoOsCommonPollFreq.setStatus("mandatory")
_CpqHoOsCommonModuleTable_Object = MibTable
cpqHoOsCommonModuleTable = _CpqHoOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqHoOsCommonModuleTable.setStatus("deprecated")
_CpqHoOsCommonModuleEntry_Object = MibTableRow
cpqHoOsCommonModuleEntry = _CpqHoOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1)
)
cpqHoOsCommonModuleEntry.setIndexNames(
    (0, "CPQHOST-MIB", "cpqHoOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqHoOsCommonModuleEntry.setStatus("deprecated")


class _CpqHoOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqHoOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHoOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqHoOsCommonModuleIndex_Object = MibTableColumn
cpqHoOsCommonModuleIndex = _CpqHoOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1, 1),
    _CpqHoOsCommonModuleIndex_Type()
)
cpqHoOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoOsCommonModuleIndex.setStatus("deprecated")


class _CpqHoOsCommonModuleName_Type(DisplayString):
    """Custom type cpqHoOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqHoOsCommonModuleName_Object = MibTableColumn
cpqHoOsCommonModuleName = _CpqHoOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1, 2),
    _CpqHoOsCommonModuleName_Type()
)
cpqHoOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoOsCommonModuleName.setStatus("deprecated")


class _CpqHoOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqHoOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqHoOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqHoOsCommonModuleVersion_Object = MibTableColumn
cpqHoOsCommonModuleVersion = _CpqHoOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1, 3),
    _CpqHoOsCommonModuleVersion_Type()
)
cpqHoOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoOsCommonModuleVersion.setStatus("deprecated")


class _CpqHoOsCommonModuleDate_Type(OctetString):
    """Custom type cpqHoOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqHoOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqHoOsCommonModuleDate_Object = MibTableColumn
cpqHoOsCommonModuleDate = _CpqHoOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1, 4),
    _CpqHoOsCommonModuleDate_Type()
)
cpqHoOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoOsCommonModuleDate.setStatus("deprecated")


class _CpqHoOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqHoOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqHoOsCommonModulePurpose_Object = MibTableColumn
cpqHoOsCommonModulePurpose = _CpqHoOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 1, 4, 2, 1, 5),
    _CpqHoOsCommonModulePurpose_Type()
)
cpqHoOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoOsCommonModulePurpose.setStatus("deprecated")
_CpqHoInfo_ObjectIdentity = ObjectIdentity
cpqHoInfo = _CpqHoInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2)
)


class _CpqHoName_Type(DisplayString):
    """Custom type cpqHoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoName_Type.__name__ = "DisplayString"
_CpqHoName_Object = MibScalar
cpqHoName = _CpqHoName_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 1),
    _CpqHoName_Type()
)
cpqHoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoName.setStatus("mandatory")


class _CpqHoVersion_Type(DisplayString):
    """Custom type cpqHoVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoVersion_Type.__name__ = "DisplayString"
_CpqHoVersion_Object = MibScalar
cpqHoVersion = _CpqHoVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 2),
    _CpqHoVersion_Type()
)
cpqHoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoVersion.setStatus("mandatory")


class _CpqHoDesc_Type(DisplayString):
    """Custom type cpqHoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoDesc_Type.__name__ = "DisplayString"
_CpqHoDesc_Object = MibScalar
cpqHoDesc = _CpqHoDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 3),
    _CpqHoDesc_Type()
)
cpqHoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoDesc.setStatus("mandatory")


class _CpqHoOsType_Type(Integer32):
    """Custom type cpqHoOsType based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("dos-windows", 8),
          ("linux", 14),
          ("ms-dos", 7),
          ("netware", 2),
          ("nsk", 12),
          ("open-vms", 11),
          ("os-2", 6),
          ("other", 1),
          ("sco-unix", 4),
          ("solaris", 19),
          ("tru64UNIX", 16),
          ("unixware", 5),
          ("windows2000", 15),
          ("windows2003", 17),
          ("windows2003-ia64", 20),
          ("windows2003-x64", 18),
          ("windows2008", 21),
          ("windows2008-ia64", 23),
          ("windows2008-x64", 22),
          ("windows95", 9),
          ("windows98", 10),
          ("windowsCE", 13),
          ("windowsnt", 3))
    )


_CpqHoOsType_Type.__name__ = "Integer32"
_CpqHoOsType_Object = MibScalar
cpqHoOsType = _CpqHoOsType_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 4),
    _CpqHoOsType_Type()
)
cpqHoOsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoOsType.setStatus("mandatory")


class _CpqHoTelnet_Type(Integer32):
    """Custom type cpqHoTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notavailable", 3),
          ("other", 1))
    )


_CpqHoTelnet_Type.__name__ = "Integer32"
_CpqHoTelnet_Object = MibScalar
cpqHoTelnet = _CpqHoTelnet_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 5),
    _CpqHoTelnet_Type()
)
cpqHoTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoTelnet.setStatus("mandatory")


class _CpqHoSystemRole_Type(DisplayString):
    """Custom type cpqHoSystemRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqHoSystemRole_Type.__name__ = "DisplayString"
_CpqHoSystemRole_Object = MibScalar
cpqHoSystemRole = _CpqHoSystemRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 6),
    _CpqHoSystemRole_Type()
)
cpqHoSystemRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoSystemRole.setStatus("mandatory")


class _CpqHoSystemRoleDetail_Type(DisplayString):
    """Custom type cpqHoSystemRoleDetail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CpqHoSystemRoleDetail_Type.__name__ = "DisplayString"
_CpqHoSystemRoleDetail_Object = MibScalar
cpqHoSystemRoleDetail = _CpqHoSystemRoleDetail_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 7),
    _CpqHoSystemRoleDetail_Type()
)
cpqHoSystemRoleDetail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoSystemRoleDetail.setStatus("mandatory")


class _CpqHoCrashDumpState_Type(Integer32):
    """Custom type cpqHoCrashDumpState based on Integer32"""
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
        *(("completememorydump", 1),
          ("kernelmemorydump", 2),
          ("none", 4),
          ("smallmemorydump", 3))
    )


_CpqHoCrashDumpState_Type.__name__ = "Integer32"
_CpqHoCrashDumpState_Object = MibScalar
cpqHoCrashDumpState = _CpqHoCrashDumpState_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 8),
    _CpqHoCrashDumpState_Type()
)
cpqHoCrashDumpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoCrashDumpState.setStatus("mandatory")


class _CpqHoCrashDumpCondition_Type(Integer32):
    """Custom type cpqHoCrashDumpCondition based on Integer32"""
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


_CpqHoCrashDumpCondition_Type.__name__ = "Integer32"
_CpqHoCrashDumpCondition_Object = MibScalar
cpqHoCrashDumpCondition = _CpqHoCrashDumpCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 9),
    _CpqHoCrashDumpCondition_Type()
)
cpqHoCrashDumpCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoCrashDumpCondition.setStatus("mandatory")


class _CpqHoCrashDumpMonitoring_Type(Integer32):
    """Custom type cpqHoCrashDumpMonitoring based on Integer32"""
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


_CpqHoCrashDumpMonitoring_Type.__name__ = "Integer32"
_CpqHoCrashDumpMonitoring_Object = MibScalar
cpqHoCrashDumpMonitoring = _CpqHoCrashDumpMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 10),
    _CpqHoCrashDumpMonitoring_Type()
)
cpqHoCrashDumpMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoCrashDumpMonitoring.setStatus("optional")


class _CpqHoMaxLogicalCPUSupported_Type(Integer32):
    """Custom type cpqHoMaxLogicalCPUSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoMaxLogicalCPUSupported_Type.__name__ = "Integer32"
_CpqHoMaxLogicalCPUSupported_Object = MibScalar
cpqHoMaxLogicalCPUSupported = _CpqHoMaxLogicalCPUSupported_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 2, 11),
    _CpqHoMaxLogicalCPUSupported_Type()
)
cpqHoMaxLogicalCPUSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoMaxLogicalCPUSupported.setStatus("optional")
_CpqHoUtil_ObjectIdentity = ObjectIdentity
cpqHoUtil = _CpqHoUtil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 3)
)
_CpqHoCpuUtilTable_Object = MibTable
cpqHoCpuUtilTable = _CpqHoCpuUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqHoCpuUtilTable.setStatus("mandatory")
_CpqHoCpuUtilEntry_Object = MibTableRow
cpqHoCpuUtilEntry = _CpqHoCpuUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1)
)
cpqHoCpuUtilEntry.setIndexNames(
    (0, "CPQHOST-MIB", "cpqHoCpuUtilUnitIndex"),
)
if mibBuilder.loadTexts:
    cpqHoCpuUtilEntry.setStatus("mandatory")


class _CpqHoCpuUtilUnitIndex_Type(Integer32):
    """Custom type cpqHoCpuUtilUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoCpuUtilUnitIndex_Type.__name__ = "Integer32"
_CpqHoCpuUtilUnitIndex_Object = MibTableColumn
cpqHoCpuUtilUnitIndex = _CpqHoCpuUtilUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 1),
    _CpqHoCpuUtilUnitIndex_Type()
)
cpqHoCpuUtilUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoCpuUtilUnitIndex.setStatus("mandatory")
_CpqHoCpuUtilMin_Type = Integer32
_CpqHoCpuUtilMin_Object = MibTableColumn
cpqHoCpuUtilMin = _CpqHoCpuUtilMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 2),
    _CpqHoCpuUtilMin_Type()
)
cpqHoCpuUtilMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoCpuUtilMin.setStatus("mandatory")
_CpqHoCpuUtilFiveMin_Type = Integer32
_CpqHoCpuUtilFiveMin_Object = MibTableColumn
cpqHoCpuUtilFiveMin = _CpqHoCpuUtilFiveMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 3),
    _CpqHoCpuUtilFiveMin_Type()
)
cpqHoCpuUtilFiveMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoCpuUtilFiveMin.setStatus("mandatory")
_CpqHoCpuUtilThirtyMin_Type = Integer32
_CpqHoCpuUtilThirtyMin_Object = MibTableColumn
cpqHoCpuUtilThirtyMin = _CpqHoCpuUtilThirtyMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 4),
    _CpqHoCpuUtilThirtyMin_Type()
)
cpqHoCpuUtilThirtyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoCpuUtilThirtyMin.setStatus("mandatory")
_CpqHoCpuUtilHour_Type = Integer32
_CpqHoCpuUtilHour_Object = MibTableColumn
cpqHoCpuUtilHour = _CpqHoCpuUtilHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 5),
    _CpqHoCpuUtilHour_Type()
)
cpqHoCpuUtilHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoCpuUtilHour.setStatus("mandatory")


class _CpqHoCpuUtilHwLocation_Type(DisplayString):
    """Custom type cpqHoCpuUtilHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoCpuUtilHwLocation_Type.__name__ = "DisplayString"
_CpqHoCpuUtilHwLocation_Object = MibTableColumn
cpqHoCpuUtilHwLocation = _CpqHoCpuUtilHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 3, 1, 1, 6),
    _CpqHoCpuUtilHwLocation_Type()
)
cpqHoCpuUtilHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoCpuUtilHwLocation.setStatus("optional")
_CpqHoFileSys_ObjectIdentity = ObjectIdentity
cpqHoFileSys = _CpqHoFileSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4)
)
_CpqHoFileSysTable_Object = MibTable
cpqHoFileSysTable = _CpqHoFileSysTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqHoFileSysTable.setStatus("mandatory")
_CpqHoFileSysEntry_Object = MibTableRow
cpqHoFileSysEntry = _CpqHoFileSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1)
)
cpqHoFileSysEntry.setIndexNames(
    (0, "CPQHOST-MIB", "cpqHoFileSysIndex"),
)
if mibBuilder.loadTexts:
    cpqHoFileSysEntry.setStatus("mandatory")


class _CpqHoFileSysIndex_Type(Integer32):
    """Custom type cpqHoFileSysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoFileSysIndex_Type.__name__ = "Integer32"
_CpqHoFileSysIndex_Object = MibTableColumn
cpqHoFileSysIndex = _CpqHoFileSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 1),
    _CpqHoFileSysIndex_Type()
)
cpqHoFileSysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFileSysIndex.setStatus("mandatory")


class _CpqHoFileSysDesc_Type(DisplayString):
    """Custom type cpqHoFileSysDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoFileSysDesc_Type.__name__ = "DisplayString"
_CpqHoFileSysDesc_Object = MibTableColumn
cpqHoFileSysDesc = _CpqHoFileSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 2),
    _CpqHoFileSysDesc_Type()
)
cpqHoFileSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFileSysDesc.setStatus("mandatory")
_CpqHoFileSysSpaceTotal_Type = Integer32
_CpqHoFileSysSpaceTotal_Object = MibTableColumn
cpqHoFileSysSpaceTotal = _CpqHoFileSysSpaceTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 3),
    _CpqHoFileSysSpaceTotal_Type()
)
cpqHoFileSysSpaceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFileSysSpaceTotal.setStatus("mandatory")
_CpqHoFileSysSpaceUsed_Type = Integer32
_CpqHoFileSysSpaceUsed_Object = MibTableColumn
cpqHoFileSysSpaceUsed = _CpqHoFileSysSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 4),
    _CpqHoFileSysSpaceUsed_Type()
)
cpqHoFileSysSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFileSysSpaceUsed.setStatus("mandatory")
_CpqHoFileSysPercentSpaceUsed_Type = Integer32
_CpqHoFileSysPercentSpaceUsed_Object = MibTableColumn
cpqHoFileSysPercentSpaceUsed = _CpqHoFileSysPercentSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 5),
    _CpqHoFileSysPercentSpaceUsed_Type()
)
cpqHoFileSysPercentSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFileSysPercentSpaceUsed.setStatus("mandatory")
_CpqHoFileSysAllocUnitsTotal_Type = Integer32
_CpqHoFileSysAllocUnitsTotal_Object = MibTableColumn
cpqHoFileSysAllocUnitsTotal = _CpqHoFileSysAllocUnitsTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 6),
    _CpqHoFileSysAllocUnitsTotal_Type()
)
cpqHoFileSysAllocUnitsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFileSysAllocUnitsTotal.setStatus("mandatory")
_CpqHoFileSysAllocUnitsUsed_Type = Integer32
_CpqHoFileSysAllocUnitsUsed_Object = MibTableColumn
cpqHoFileSysAllocUnitsUsed = _CpqHoFileSysAllocUnitsUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 7),
    _CpqHoFileSysAllocUnitsUsed_Type()
)
cpqHoFileSysAllocUnitsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFileSysAllocUnitsUsed.setStatus("mandatory")


class _CpqHoFileSysStatus_Type(Integer32):
    """Custom type cpqHoFileSysStatus based on Integer32"""
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
          ("unknown", 1))
    )


_CpqHoFileSysStatus_Type.__name__ = "Integer32"
_CpqHoFileSysStatus_Object = MibTableColumn
cpqHoFileSysStatus = _CpqHoFileSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 1, 1, 8),
    _CpqHoFileSysStatus_Type()
)
cpqHoFileSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFileSysStatus.setStatus("mandatory")


class _CpqHoFileSysCondition_Type(Integer32):
    """Custom type cpqHoFileSysCondition based on Integer32"""
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
          ("unknown", 1))
    )


_CpqHoFileSysCondition_Type.__name__ = "Integer32"
_CpqHoFileSysCondition_Object = MibScalar
cpqHoFileSysCondition = _CpqHoFileSysCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 4, 2),
    _CpqHoFileSysCondition_Type()
)
cpqHoFileSysCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFileSysCondition.setStatus("mandatory")
_CpqHoIfPhysMap_ObjectIdentity = ObjectIdentity
cpqHoIfPhysMap = _CpqHoIfPhysMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5)
)
_CpqHoIfPhysMapTable_Object = MibTable
cpqHoIfPhysMapTable = _CpqHoIfPhysMapTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqHoIfPhysMapTable.setStatus("deprecated")
_CpqHoIfPhysMapEntry_Object = MibTableRow
cpqHoIfPhysMapEntry = _CpqHoIfPhysMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1)
)
cpqHoIfPhysMapEntry.setIndexNames(
    (0, "CPQHOST-MIB", "cpqHoIfPhysMapIndex"),
)
if mibBuilder.loadTexts:
    cpqHoIfPhysMapEntry.setStatus("deprecated")


class _CpqHoIfPhysMapIndex_Type(Integer32):
    """Custom type cpqHoIfPhysMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoIfPhysMapIndex_Type.__name__ = "Integer32"
_CpqHoIfPhysMapIndex_Object = MibTableColumn
cpqHoIfPhysMapIndex = _CpqHoIfPhysMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 1),
    _CpqHoIfPhysMapIndex_Type()
)
cpqHoIfPhysMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoIfPhysMapIndex.setStatus("deprecated")


class _CpqHoIfPhysMapSlot_Type(Integer32):
    """Custom type cpqHoIfPhysMapSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHoIfPhysMapSlot_Type.__name__ = "Integer32"
_CpqHoIfPhysMapSlot_Object = MibTableColumn
cpqHoIfPhysMapSlot = _CpqHoIfPhysMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 2),
    _CpqHoIfPhysMapSlot_Type()
)
cpqHoIfPhysMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoIfPhysMapSlot.setStatus("deprecated")
_CpqHoIfPhysMapIoBaseAddr_Type = Integer32
_CpqHoIfPhysMapIoBaseAddr_Object = MibTableColumn
cpqHoIfPhysMapIoBaseAddr = _CpqHoIfPhysMapIoBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 3),
    _CpqHoIfPhysMapIoBaseAddr_Type()
)
cpqHoIfPhysMapIoBaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoIfPhysMapIoBaseAddr.setStatus("deprecated")


class _CpqHoIfPhysMapIrq_Type(Integer32):
    """Custom type cpqHoIfPhysMapIrq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqHoIfPhysMapIrq_Type.__name__ = "Integer32"
_CpqHoIfPhysMapIrq_Object = MibTableColumn
cpqHoIfPhysMapIrq = _CpqHoIfPhysMapIrq_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 4),
    _CpqHoIfPhysMapIrq_Type()
)
cpqHoIfPhysMapIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoIfPhysMapIrq.setStatus("deprecated")
_CpqHoIfPhysMapDma_Type = Integer32
_CpqHoIfPhysMapDma_Object = MibTableColumn
cpqHoIfPhysMapDma = _CpqHoIfPhysMapDma_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 5),
    _CpqHoIfPhysMapDma_Type()
)
cpqHoIfPhysMapDma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoIfPhysMapDma.setStatus("deprecated")
_CpqHoIfPhysMapMemBaseAddr_Type = Integer32
_CpqHoIfPhysMapMemBaseAddr_Object = MibTableColumn
cpqHoIfPhysMapMemBaseAddr = _CpqHoIfPhysMapMemBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 6),
    _CpqHoIfPhysMapMemBaseAddr_Type()
)
cpqHoIfPhysMapMemBaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoIfPhysMapMemBaseAddr.setStatus("deprecated")
_CpqHoIfPhysMapPort_Type = Integer32
_CpqHoIfPhysMapPort_Object = MibTableColumn
cpqHoIfPhysMapPort = _CpqHoIfPhysMapPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 7),
    _CpqHoIfPhysMapPort_Type()
)
cpqHoIfPhysMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoIfPhysMapPort.setStatus("deprecated")


class _CpqHoIfPhysMapDuplexState_Type(Integer32):
    """Custom type cpqHoIfPhysMapDuplexState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("half", 2),
          ("other", 1))
    )


_CpqHoIfPhysMapDuplexState_Type.__name__ = "Integer32"
_CpqHoIfPhysMapDuplexState_Object = MibTableColumn
cpqHoIfPhysMapDuplexState = _CpqHoIfPhysMapDuplexState_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 8),
    _CpqHoIfPhysMapDuplexState_Type()
)
cpqHoIfPhysMapDuplexState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoIfPhysMapDuplexState.setStatus("deprecated")


class _CpqHoIfPhysMapCondition_Type(Integer32):
    """Custom type cpqHoIfPhysMapCondition based on Integer32"""
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


_CpqHoIfPhysMapCondition_Type.__name__ = "Integer32"
_CpqHoIfPhysMapCondition_Object = MibTableColumn
cpqHoIfPhysMapCondition = _CpqHoIfPhysMapCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 1, 1, 9),
    _CpqHoIfPhysMapCondition_Type()
)
cpqHoIfPhysMapCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoIfPhysMapCondition.setStatus("deprecated")


class _CpqHoIfPhysMapOverallCondition_Type(Integer32):
    """Custom type cpqHoIfPhysMapOverallCondition based on Integer32"""
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


_CpqHoIfPhysMapOverallCondition_Type.__name__ = "Integer32"
_CpqHoIfPhysMapOverallCondition_Object = MibScalar
cpqHoIfPhysMapOverallCondition = _CpqHoIfPhysMapOverallCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 5, 2),
    _CpqHoIfPhysMapOverallCondition_Type()
)
cpqHoIfPhysMapOverallCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoIfPhysMapOverallCondition.setStatus("deprecated")
_CpqHoSWRunning_ObjectIdentity = ObjectIdentity
cpqHoSWRunning = _CpqHoSWRunning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6)
)
_CpqHoSWRunningTable_Object = MibTable
cpqHoSWRunningTable = _CpqHoSWRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cpqHoSWRunningTable.setStatus("mandatory")
_CpqHoSWRunningEntry_Object = MibTableRow
cpqHoSWRunningEntry = _CpqHoSWRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1)
)
cpqHoSWRunningEntry.setIndexNames(
    (0, "CPQHOST-MIB", "cpqHoSWRunningIndex"),
)
if mibBuilder.loadTexts:
    cpqHoSWRunningEntry.setStatus("mandatory")


class _CpqHoSWRunningIndex_Type(Integer32):
    """Custom type cpqHoSWRunningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoSWRunningIndex_Type.__name__ = "Integer32"
_CpqHoSWRunningIndex_Object = MibTableColumn
cpqHoSWRunningIndex = _CpqHoSWRunningIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 1),
    _CpqHoSWRunningIndex_Type()
)
cpqHoSWRunningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningIndex.setStatus("mandatory")


class _CpqHoSWRunningName_Type(DisplayString):
    """Custom type cpqHoSWRunningName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoSWRunningName_Type.__name__ = "DisplayString"
_CpqHoSWRunningName_Object = MibTableColumn
cpqHoSWRunningName = _CpqHoSWRunningName_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 2),
    _CpqHoSWRunningName_Type()
)
cpqHoSWRunningName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningName.setStatus("mandatory")


class _CpqHoSWRunningDesc_Type(DisplayString):
    """Custom type cpqHoSWRunningDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoSWRunningDesc_Type.__name__ = "DisplayString"
_CpqHoSWRunningDesc_Object = MibTableColumn
cpqHoSWRunningDesc = _CpqHoSWRunningDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 3),
    _CpqHoSWRunningDesc_Type()
)
cpqHoSWRunningDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningDesc.setStatus("mandatory")


class _CpqHoSWRunningVersion_Type(DisplayString):
    """Custom type cpqHoSWRunningVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoSWRunningVersion_Type.__name__ = "DisplayString"
_CpqHoSWRunningVersion_Object = MibTableColumn
cpqHoSWRunningVersion = _CpqHoSWRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 4),
    _CpqHoSWRunningVersion_Type()
)
cpqHoSWRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningVersion.setStatus("mandatory")


class _CpqHoSWRunningDate_Type(OctetString):
    """Custom type cpqHoSWRunningDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqHoSWRunningDate_Type.__name__ = "OctetString"
_CpqHoSWRunningDate_Object = MibTableColumn
cpqHoSWRunningDate = _CpqHoSWRunningDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 5),
    _CpqHoSWRunningDate_Type()
)
cpqHoSWRunningDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningDate.setStatus("mandatory")


class _CpqHoSWRunningMonitor_Type(Integer32):
    """Custom type cpqHoSWRunningMonitor based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("count", 5),
          ("countAndStop", 7),
          ("other", 1),
          ("start", 2),
          ("startAndCount", 6),
          ("startAndStop", 4),
          ("startCountAndStop", 8),
          ("stop", 3))
    )


_CpqHoSWRunningMonitor_Type.__name__ = "Integer32"
_CpqHoSWRunningMonitor_Object = MibTableColumn
cpqHoSWRunningMonitor = _CpqHoSWRunningMonitor_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 6),
    _CpqHoSWRunningMonitor_Type()
)
cpqHoSWRunningMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningMonitor.setStatus("mandatory")


class _CpqHoSWRunningState_Type(Integer32):
    """Custom type cpqHoSWRunningState based on Integer32"""
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
          ("started", 2),
          ("stopped", 3))
    )


_CpqHoSWRunningState_Type.__name__ = "Integer32"
_CpqHoSWRunningState_Object = MibTableColumn
cpqHoSWRunningState = _CpqHoSWRunningState_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 7),
    _CpqHoSWRunningState_Type()
)
cpqHoSWRunningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningState.setStatus("mandatory")


class _CpqHoSWRunningCount_Type(Integer32):
    """Custom type cpqHoSWRunningCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoSWRunningCount_Type.__name__ = "Integer32"
_CpqHoSWRunningCount_Object = MibTableColumn
cpqHoSWRunningCount = _CpqHoSWRunningCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 8),
    _CpqHoSWRunningCount_Type()
)
cpqHoSWRunningCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningCount.setStatus("optional")


class _CpqHoSWRunningCountMin_Type(Integer32):
    """Custom type cpqHoSWRunningCountMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoSWRunningCountMin_Type.__name__ = "Integer32"
_CpqHoSWRunningCountMin_Object = MibTableColumn
cpqHoSWRunningCountMin = _CpqHoSWRunningCountMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 9),
    _CpqHoSWRunningCountMin_Type()
)
cpqHoSWRunningCountMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoSWRunningCountMin.setStatus("optional")


class _CpqHoSWRunningCountMax_Type(Integer32):
    """Custom type cpqHoSWRunningCountMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoSWRunningCountMax_Type.__name__ = "Integer32"
_CpqHoSWRunningCountMax_Object = MibTableColumn
cpqHoSWRunningCountMax = _CpqHoSWRunningCountMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 10),
    _CpqHoSWRunningCountMax_Type()
)
cpqHoSWRunningCountMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoSWRunningCountMax.setStatus("optional")


class _CpqHoSWRunningEventTime_Type(OctetString):
    """Custom type cpqHoSWRunningEventTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqHoSWRunningEventTime_Type.__name__ = "OctetString"
_CpqHoSWRunningEventTime_Object = MibTableColumn
cpqHoSWRunningEventTime = _CpqHoSWRunningEventTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 11),
    _CpqHoSWRunningEventTime_Type()
)
cpqHoSWRunningEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningEventTime.setStatus("optional")


class _CpqHoSWRunningStatus_Type(Integer32):
    """Custom type cpqHoSWRunningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("disabled", 7),
          ("major", 5),
          ("minor", 4),
          ("normal", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_CpqHoSWRunningStatus_Type.__name__ = "Integer32"
_CpqHoSWRunningStatus_Object = MibTableColumn
cpqHoSWRunningStatus = _CpqHoSWRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 12),
    _CpqHoSWRunningStatus_Type()
)
cpqHoSWRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningStatus.setStatus("optional")


class _CpqHoSWRunningConfigStatus_Type(Integer32):
    """Custom type cpqHoSWRunningConfigStatus based on Integer32"""
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
        *(("configured", 4),
          ("initialized", 3),
          ("operational", 5),
          ("starting", 2),
          ("unknown", 1))
    )


_CpqHoSWRunningConfigStatus_Type.__name__ = "Integer32"
_CpqHoSWRunningConfigStatus_Object = MibTableColumn
cpqHoSWRunningConfigStatus = _CpqHoSWRunningConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 13),
    _CpqHoSWRunningConfigStatus_Type()
)
cpqHoSWRunningConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningConfigStatus.setStatus("optional")


class _CpqHoSWRunningIdentifier_Type(DisplayString):
    """Custom type cpqHoSWRunningIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoSWRunningIdentifier_Type.__name__ = "DisplayString"
_CpqHoSWRunningIdentifier_Object = MibTableColumn
cpqHoSWRunningIdentifier = _CpqHoSWRunningIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 14),
    _CpqHoSWRunningIdentifier_Type()
)
cpqHoSWRunningIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningIdentifier.setStatus("optional")


class _CpqHoSWRunningRedundancyMode_Type(Integer32):
    """Custom type cpqHoSWRunningRedundancyMode based on Integer32"""
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
        *(("backup", 3),
          ("master", 2),
          ("slave", 4),
          ("unknown", 1))
    )


_CpqHoSWRunningRedundancyMode_Type.__name__ = "Integer32"
_CpqHoSWRunningRedundancyMode_Object = MibTableColumn
cpqHoSWRunningRedundancyMode = _CpqHoSWRunningRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 1, 1, 15),
    _CpqHoSWRunningRedundancyMode_Type()
)
cpqHoSWRunningRedundancyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSWRunningRedundancyMode.setStatus("optional")


class _CpqHoSwRunningTrapDesc_Type(DisplayString):
    """Custom type cpqHoSwRunningTrapDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoSwRunningTrapDesc_Type.__name__ = "DisplayString"
_CpqHoSwRunningTrapDesc_Object = MibScalar
cpqHoSwRunningTrapDesc = _CpqHoSwRunningTrapDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 6, 2),
    _CpqHoSwRunningTrapDesc_Type()
)
cpqHoSwRunningTrapDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSwRunningTrapDesc.setStatus("mandatory")
_CpqHoSwVer_ObjectIdentity = ObjectIdentity
cpqHoSwVer = _CpqHoSwVer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7)
)
_CpqHoSwVerNextIndex_Type = Integer32
_CpqHoSwVerNextIndex_Object = MibScalar
cpqHoSwVerNextIndex = _CpqHoSwVerNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 1),
    _CpqHoSwVerNextIndex_Type()
)
cpqHoSwVerNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSwVerNextIndex.setStatus("mandatory")
_CpqHoSwVerTable_Object = MibTable
cpqHoSwVerTable = _CpqHoSwVerTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2)
)
if mibBuilder.loadTexts:
    cpqHoSwVerTable.setStatus("mandatory")
_CpqHoSwVerEntry_Object = MibTableRow
cpqHoSwVerEntry = _CpqHoSwVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1)
)
cpqHoSwVerEntry.setIndexNames(
    (0, "CPQHOST-MIB", "cpqHoSwVerIndex"),
)
if mibBuilder.loadTexts:
    cpqHoSwVerEntry.setStatus("mandatory")


class _CpqHoSwVerIndex_Type(Integer32):
    """Custom type cpqHoSwVerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoSwVerIndex_Type.__name__ = "Integer32"
_CpqHoSwVerIndex_Object = MibTableColumn
cpqHoSwVerIndex = _CpqHoSwVerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 1),
    _CpqHoSwVerIndex_Type()
)
cpqHoSwVerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSwVerIndex.setStatus("mandatory")


class _CpqHoSwVerStatus_Type(Integer32):
    """Custom type cpqHoSwVerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 2),
          ("notloaded", 3),
          ("other", 1))
    )


_CpqHoSwVerStatus_Type.__name__ = "Integer32"
_CpqHoSwVerStatus_Object = MibTableColumn
cpqHoSwVerStatus = _CpqHoSwVerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 2),
    _CpqHoSwVerStatus_Type()
)
cpqHoSwVerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSwVerStatus.setStatus("mandatory")


class _CpqHoSwVerType_Type(Integer32):
    """Custom type cpqHoSwVerType based on Integer32"""
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
        *(("agent", 3),
          ("application", 5),
          ("driver", 2),
          ("keyfile", 6),
          ("other", 1),
          ("sysutil", 4))
    )


_CpqHoSwVerType_Type.__name__ = "Integer32"
_CpqHoSwVerType_Object = MibTableColumn
cpqHoSwVerType = _CpqHoSwVerType_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 3),
    _CpqHoSwVerType_Type()
)
cpqHoSwVerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoSwVerType.setStatus("mandatory")


class _CpqHoSwVerName_Type(DisplayString):
    """Custom type cpqHoSwVerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CpqHoSwVerName_Type.__name__ = "DisplayString"
_CpqHoSwVerName_Object = MibTableColumn
cpqHoSwVerName = _CpqHoSwVerName_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 4),
    _CpqHoSwVerName_Type()
)
cpqHoSwVerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoSwVerName.setStatus("mandatory")


class _CpqHoSwVerDescription_Type(DisplayString):
    """Custom type cpqHoSwVerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CpqHoSwVerDescription_Type.__name__ = "DisplayString"
_CpqHoSwVerDescription_Object = MibTableColumn
cpqHoSwVerDescription = _CpqHoSwVerDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 5),
    _CpqHoSwVerDescription_Type()
)
cpqHoSwVerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoSwVerDescription.setStatus("mandatory")


class _CpqHoSwVerDate_Type(OctetString):
    """Custom type cpqHoSwVerDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqHoSwVerDate_Type.__name__ = "OctetString"
_CpqHoSwVerDate_Object = MibTableColumn
cpqHoSwVerDate = _CpqHoSwVerDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 6),
    _CpqHoSwVerDate_Type()
)
cpqHoSwVerDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSwVerDate.setStatus("mandatory")


class _CpqHoSwVerLocation_Type(DisplayString):
    """Custom type cpqHoSwVerLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoSwVerLocation_Type.__name__ = "DisplayString"
_CpqHoSwVerLocation_Object = MibTableColumn
cpqHoSwVerLocation = _CpqHoSwVerLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 7),
    _CpqHoSwVerLocation_Type()
)
cpqHoSwVerLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoSwVerLocation.setStatus("mandatory")


class _CpqHoSwVerVersion_Type(DisplayString):
    """Custom type cpqHoSwVerVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqHoSwVerVersion_Type.__name__ = "DisplayString"
_CpqHoSwVerVersion_Object = MibTableColumn
cpqHoSwVerVersion = _CpqHoSwVerVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 8),
    _CpqHoSwVerVersion_Type()
)
cpqHoSwVerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSwVerVersion.setStatus("mandatory")


class _CpqHoSwVerVersionBinary_Type(DisplayString):
    """Custom type cpqHoSwVerVersionBinary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqHoSwVerVersionBinary_Type.__name__ = "DisplayString"
_CpqHoSwVerVersionBinary_Object = MibTableColumn
cpqHoSwVerVersionBinary = _CpqHoSwVerVersionBinary_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 2, 1, 9),
    _CpqHoSwVerVersionBinary_Type()
)
cpqHoSwVerVersionBinary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSwVerVersionBinary.setStatus("mandatory")


class _CpqHoSwVerAgentsVer_Type(DisplayString):
    """Custom type cpqHoSwVerAgentsVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqHoSwVerAgentsVer_Type.__name__ = "DisplayString"
_CpqHoSwVerAgentsVer_Object = MibScalar
cpqHoSwVerAgentsVer = _CpqHoSwVerAgentsVer_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 7, 3),
    _CpqHoSwVerAgentsVer_Type()
)
cpqHoSwVerAgentsVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSwVerAgentsVer.setStatus("mandatory")
_CpqHoGeneric_ObjectIdentity = ObjectIdentity
cpqHoGeneric = _CpqHoGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 8)
)


class _CpqHoGenericData_Type(DisplayString):
    """Custom type cpqHoGenericData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CpqHoGenericData_Type.__name__ = "DisplayString"
_CpqHoGenericData_Object = MibScalar
cpqHoGenericData = _CpqHoGenericData_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 8, 1),
    _CpqHoGenericData_Type()
)
cpqHoGenericData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoGenericData.setStatus("mandatory")


class _CpqHoCriticalSoftwareUpdateData_Type(DisplayString):
    """Custom type cpqHoCriticalSoftwareUpdateData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CpqHoCriticalSoftwareUpdateData_Type.__name__ = "DisplayString"
_CpqHoCriticalSoftwareUpdateData_Object = MibScalar
cpqHoCriticalSoftwareUpdateData = _CpqHoCriticalSoftwareUpdateData_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 8, 2),
    _CpqHoCriticalSoftwareUpdateData_Type()
)
cpqHoCriticalSoftwareUpdateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoCriticalSoftwareUpdateData.setStatus("mandatory")
_CpqHoSwPerf_ObjectIdentity = ObjectIdentity
cpqHoSwPerf = _CpqHoSwPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 9)
)


class _CpqHoSwPerfAppErrorDesc_Type(DisplayString):
    """Custom type cpqHoSwPerfAppErrorDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CpqHoSwPerfAppErrorDesc_Type.__name__ = "DisplayString"
_CpqHoSwPerfAppErrorDesc_Object = MibScalar
cpqHoSwPerfAppErrorDesc = _CpqHoSwPerfAppErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 9, 1),
    _CpqHoSwPerfAppErrorDesc_Type()
)
cpqHoSwPerfAppErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoSwPerfAppErrorDesc.setStatus("mandatory")
_CpqHoSystemStatus_ObjectIdentity = ObjectIdentity
cpqHoSystemStatus = _CpqHoSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 10)
)


class _CpqHoMibStatusArray_Type(OctetString):
    """Custom type cpqHoMibStatusArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 256),
    )


_CpqHoMibStatusArray_Type.__name__ = "OctetString"
_CpqHoMibStatusArray_Object = MibScalar
cpqHoMibStatusArray = _CpqHoMibStatusArray_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 1),
    _CpqHoMibStatusArray_Type()
)
cpqHoMibStatusArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoMibStatusArray.setStatus("mandatory")


class _CpqHoConfigChangedDate_Type(OctetString):
    """Custom type cpqHoConfigChangedDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqHoConfigChangedDate_Type.__name__ = "OctetString"
_CpqHoConfigChangedDate_Object = MibScalar
cpqHoConfigChangedDate = _CpqHoConfigChangedDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 2),
    _CpqHoConfigChangedDate_Type()
)
cpqHoConfigChangedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoConfigChangedDate.setStatus("mandatory")


class _CpqHoGUID_Type(OctetString):
    """Custom type cpqHoGUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 17),
    )


_CpqHoGUID_Type.__name__ = "OctetString"
_CpqHoGUID_Object = MibScalar
cpqHoGUID = _CpqHoGUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 3),
    _CpqHoGUID_Type()
)
cpqHoGUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoGUID.setStatus("mandatory")
_CpqHoCodeServer_Type = Integer32
_CpqHoCodeServer_Object = MibScalar
cpqHoCodeServer = _CpqHoCodeServer_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 4),
    _CpqHoCodeServer_Type()
)
cpqHoCodeServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoCodeServer.setStatus("mandatory")
_CpqHoWebMgmtPort_Type = Integer32
_CpqHoWebMgmtPort_Object = MibScalar
cpqHoWebMgmtPort = _CpqHoWebMgmtPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 5),
    _CpqHoWebMgmtPort_Type()
)
cpqHoWebMgmtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoWebMgmtPort.setStatus("mandatory")


class _CpqHoGUIDCanonical_Type(OctetString):
    """Custom type cpqHoGUIDCanonical based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 36),
    )


_CpqHoGUIDCanonical_Type.__name__ = "OctetString"
_CpqHoGUIDCanonical_Object = MibScalar
cpqHoGUIDCanonical = _CpqHoGUIDCanonical_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 10, 6),
    _CpqHoGUIDCanonical_Type()
)
cpqHoGUIDCanonical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoGUIDCanonical.setStatus("mandatory")
_CpqHoTrapInfo_ObjectIdentity = ObjectIdentity
cpqHoTrapInfo = _CpqHoTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 11)
)
_CpqHoTrapFlags_Type = Integer32
_CpqHoTrapFlags_Object = MibScalar
cpqHoTrapFlags = _CpqHoTrapFlags_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 11, 1),
    _CpqHoTrapFlags_Type()
)
cpqHoTrapFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoTrapFlags.setStatus("mandatory")
_CpqHoClients_ObjectIdentity = ObjectIdentity
cpqHoClients = _CpqHoClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12)
)


class _CpqHoClientLastModified_Type(OctetString):
    """Custom type cpqHoClientLastModified based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqHoClientLastModified_Type.__name__ = "OctetString"
_CpqHoClientLastModified_Object = MibScalar
cpqHoClientLastModified = _CpqHoClientLastModified_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 1),
    _CpqHoClientLastModified_Type()
)
cpqHoClientLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientLastModified.setStatus("mandatory")


class _CpqHoClientDelete_Type(DisplayString):
    """Custom type cpqHoClientDelete based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqHoClientDelete_Type.__name__ = "DisplayString"
_CpqHoClientDelete_Object = MibScalar
cpqHoClientDelete = _CpqHoClientDelete_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 2),
    _CpqHoClientDelete_Type()
)
cpqHoClientDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoClientDelete.setStatus("mandatory")
_CpqHoClientTable_Object = MibTable
cpqHoClientTable = _CpqHoClientTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3)
)
if mibBuilder.loadTexts:
    cpqHoClientTable.setStatus("mandatory")
_CpqHoClientEntry_Object = MibTableRow
cpqHoClientEntry = _CpqHoClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1)
)
cpqHoClientEntry.setIndexNames(
    (0, "CPQHOST-MIB", "cpqHoClientIndex"),
)
if mibBuilder.loadTexts:
    cpqHoClientEntry.setStatus("mandatory")


class _CpqHoClientIndex_Type(Integer32):
    """Custom type cpqHoClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoClientIndex_Type.__name__ = "Integer32"
_CpqHoClientIndex_Object = MibTableColumn
cpqHoClientIndex = _CpqHoClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 1),
    _CpqHoClientIndex_Type()
)
cpqHoClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientIndex.setStatus("mandatory")


class _CpqHoClientName_Type(DisplayString):
    """Custom type cpqHoClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqHoClientName_Type.__name__ = "DisplayString"
_CpqHoClientName_Object = MibTableColumn
cpqHoClientName = _CpqHoClientName_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 2),
    _CpqHoClientName_Type()
)
cpqHoClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientName.setStatus("mandatory")


class _CpqHoClientIpxAddress_Type(OctetString):
    """Custom type cpqHoClientIpxAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_CpqHoClientIpxAddress_Type.__name__ = "OctetString"
_CpqHoClientIpxAddress_Object = MibTableColumn
cpqHoClientIpxAddress = _CpqHoClientIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 3),
    _CpqHoClientIpxAddress_Type()
)
cpqHoClientIpxAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientIpxAddress.setStatus("mandatory")
_CpqHoClientIpAddress_Type = IpAddress
_CpqHoClientIpAddress_Object = MibTableColumn
cpqHoClientIpAddress = _CpqHoClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 4),
    _CpqHoClientIpAddress_Type()
)
cpqHoClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientIpAddress.setStatus("mandatory")


class _CpqHoClientCommunity_Type(DisplayString):
    """Custom type cpqHoClientCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_CpqHoClientCommunity_Type.__name__ = "DisplayString"
_CpqHoClientCommunity_Object = MibTableColumn
cpqHoClientCommunity = _CpqHoClientCommunity_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 5),
    _CpqHoClientCommunity_Type()
)
cpqHoClientCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientCommunity.setStatus("mandatory")


class _CpqHoClientID_Type(OctetString):
    """Custom type cpqHoClientID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CpqHoClientID_Type.__name__ = "OctetString"
_CpqHoClientID_Object = MibTableColumn
cpqHoClientID = _CpqHoClientID_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 6),
    _CpqHoClientID_Type()
)
cpqHoClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientID.setStatus("mandatory")
_CpqHoMemory_ObjectIdentity = ObjectIdentity
cpqHoMemory = _CpqHoMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 13)
)
_CpqHoPhysicalMemorySize_Type = Integer32
_CpqHoPhysicalMemorySize_Object = MibScalar
cpqHoPhysicalMemorySize = _CpqHoPhysicalMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 1),
    _CpqHoPhysicalMemorySize_Type()
)
cpqHoPhysicalMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoPhysicalMemorySize.setStatus("mandatory")
_CpqHoPhysicalMemoryFree_Type = Integer32
_CpqHoPhysicalMemoryFree_Object = MibScalar
cpqHoPhysicalMemoryFree = _CpqHoPhysicalMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 2),
    _CpqHoPhysicalMemoryFree_Type()
)
cpqHoPhysicalMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoPhysicalMemoryFree.setStatus("mandatory")
_CpqHoPagingMemorySize_Type = Integer32
_CpqHoPagingMemorySize_Object = MibScalar
cpqHoPagingMemorySize = _CpqHoPagingMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 3),
    _CpqHoPagingMemorySize_Type()
)
cpqHoPagingMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoPagingMemorySize.setStatus("mandatory")
_CpqHoPagingMemoryFree_Type = Integer32
_CpqHoPagingMemoryFree_Object = MibScalar
cpqHoPagingMemoryFree = _CpqHoPagingMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 4),
    _CpqHoPagingMemoryFree_Type()
)
cpqHoPagingMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoPagingMemoryFree.setStatus("mandatory")


class _CpqHoBootPagingFileSize_Type(DisplayString):
    """Custom type cpqHoBootPagingFileSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CpqHoBootPagingFileSize_Type.__name__ = "DisplayString"
_CpqHoBootPagingFileSize_Object = MibScalar
cpqHoBootPagingFileSize = _CpqHoBootPagingFileSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 5),
    _CpqHoBootPagingFileSize_Type()
)
cpqHoBootPagingFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoBootPagingFileSize.setStatus("mandatory")


class _CpqHoBootPagingFileMinimumSize_Type(DisplayString):
    """Custom type cpqHoBootPagingFileMinimumSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CpqHoBootPagingFileMinimumSize_Type.__name__ = "DisplayString"
_CpqHoBootPagingFileMinimumSize_Object = MibScalar
cpqHoBootPagingFileMinimumSize = _CpqHoBootPagingFileMinimumSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 6),
    _CpqHoBootPagingFileMinimumSize_Type()
)
cpqHoBootPagingFileMinimumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoBootPagingFileMinimumSize.setStatus("mandatory")


class _CpqHoBootPagingFileVolumeFreeSpace_Type(DisplayString):
    """Custom type cpqHoBootPagingFileVolumeFreeSpace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CpqHoBootPagingFileVolumeFreeSpace_Type.__name__ = "DisplayString"
_CpqHoBootPagingFileVolumeFreeSpace_Object = MibScalar
cpqHoBootPagingFileVolumeFreeSpace = _CpqHoBootPagingFileVolumeFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 13, 7),
    _CpqHoBootPagingFileVolumeFreeSpace_Type()
)
cpqHoBootPagingFileVolumeFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoBootPagingFileVolumeFreeSpace.setStatus("optional")
_CpqHoFwVer_ObjectIdentity = ObjectIdentity
cpqHoFwVer = _CpqHoFwVer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14)
)
_CpqHoFwVerTable_Object = MibTable
cpqHoFwVerTable = _CpqHoFwVerTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1)
)
if mibBuilder.loadTexts:
    cpqHoFwVerTable.setStatus("mandatory")
_CpqHoFwVerEntry_Object = MibTableRow
cpqHoFwVerEntry = _CpqHoFwVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1)
)
cpqHoFwVerEntry.setIndexNames(
    (0, "CPQHOST-MIB", "cpqHoFwVerIndex"),
)
if mibBuilder.loadTexts:
    cpqHoFwVerEntry.setStatus("mandatory")
_CpqHoFwVerIndex_Type = Integer32
_CpqHoFwVerIndex_Object = MibTableColumn
cpqHoFwVerIndex = _CpqHoFwVerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 1),
    _CpqHoFwVerIndex_Type()
)
cpqHoFwVerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFwVerIndex.setStatus("mandatory")


class _CpqHoFwVerCategory_Type(Integer32):
    """Custom type cpqHoFwVerCategory based on Integer32"""
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
        *(("nic", 3),
          ("other", 1),
          ("rib", 4),
          ("storage", 2),
          ("system", 5))
    )


_CpqHoFwVerCategory_Type.__name__ = "Integer32"
_CpqHoFwVerCategory_Object = MibTableColumn
cpqHoFwVerCategory = _CpqHoFwVerCategory_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 2),
    _CpqHoFwVerCategory_Type()
)
cpqHoFwVerCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFwVerCategory.setStatus("mandatory")


class _CpqHoFwVerDeviceType_Type(Integer32):
    """Custom type cpqHoFwVerDeviceType based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("fibreArrayController", 3),
          ("fibreChannelTapeController", 5),
          ("ideCdRomDrive", 7),
          ("ideDiskDrive", 8),
          ("internalArrayController", 2),
          ("modularDataRouter", 6),
          ("networkInterfaceController", 24),
          ("other", 1),
          ("remoteInsightBoard", 25),
          ("scsiCdRom-ScsiAttached", 9),
          ("scsiController", 4),
          ("scsiDiskDrive-ArrayAttached", 13),
          ("scsiDiskDrive-FibreAttached", 16),
          ("scsiDiskDrive-ScsiAttached", 10),
          ("scsiEnclosureBackplaneRom-ArrayAttached", 20),
          ("scsiEnclosureBackplaneRom-FibreAttached", 21),
          ("scsiEnclosureBackplaneRom-ScsiAttached", 19),
          ("scsiEnclosureBackplaneRom-ra4x00", 22),
          ("scsiTapeDrive-ArrayAttached", 14),
          ("scsiTapeDrive-FibreAttached", 17),
          ("scsiTapeDrive-ScsiAttached", 11),
          ("scsiTapeLibrary-ArrayAttached", 15),
          ("scsiTapeLibrary-FibreAttached", 18),
          ("scsiTapeLibrary-ScsiAttached", 12),
          ("systemRom", 23))
    )


_CpqHoFwVerDeviceType_Type.__name__ = "Integer32"
_CpqHoFwVerDeviceType_Object = MibTableColumn
cpqHoFwVerDeviceType = _CpqHoFwVerDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 3),
    _CpqHoFwVerDeviceType_Type()
)
cpqHoFwVerDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFwVerDeviceType.setStatus("mandatory")


class _CpqHoFwVerDisplayName_Type(DisplayString):
    """Custom type cpqHoFwVerDisplayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CpqHoFwVerDisplayName_Type.__name__ = "DisplayString"
_CpqHoFwVerDisplayName_Object = MibTableColumn
cpqHoFwVerDisplayName = _CpqHoFwVerDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 4),
    _CpqHoFwVerDisplayName_Type()
)
cpqHoFwVerDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFwVerDisplayName.setStatus("mandatory")


class _CpqHoFwVerVersion_Type(DisplayString):
    """Custom type cpqHoFwVerVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CpqHoFwVerVersion_Type.__name__ = "DisplayString"
_CpqHoFwVerVersion_Object = MibTableColumn
cpqHoFwVerVersion = _CpqHoFwVerVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 5),
    _CpqHoFwVerVersion_Type()
)
cpqHoFwVerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFwVerVersion.setStatus("mandatory")


class _CpqHoFwVerLocation_Type(DisplayString):
    """Custom type cpqHoFwVerLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoFwVerLocation_Type.__name__ = "DisplayString"
_CpqHoFwVerLocation_Object = MibTableColumn
cpqHoFwVerLocation = _CpqHoFwVerLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 6),
    _CpqHoFwVerLocation_Type()
)
cpqHoFwVerLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFwVerLocation.setStatus("mandatory")


class _CpqHoFwVerXmlString_Type(DisplayString):
    """Custom type cpqHoFwVerXmlString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqHoFwVerXmlString_Type.__name__ = "DisplayString"
_CpqHoFwVerXmlString_Object = MibTableColumn
cpqHoFwVerXmlString = _CpqHoFwVerXmlString_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 7),
    _CpqHoFwVerXmlString_Type()
)
cpqHoFwVerXmlString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFwVerXmlString.setStatus("mandatory")


class _CpqHoFwVerKeyString_Type(DisplayString):
    """Custom type cpqHoFwVerKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CpqHoFwVerKeyString_Type.__name__ = "DisplayString"
_CpqHoFwVerKeyString_Object = MibTableColumn
cpqHoFwVerKeyString = _CpqHoFwVerKeyString_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 8),
    _CpqHoFwVerKeyString_Type()
)
cpqHoFwVerKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFwVerKeyString.setStatus("mandatory")


class _CpqHoFwVerUpdateMethod_Type(Integer32):
    """Custom type cpqHoFwVerUpdateMethod based on Integer32"""
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
        *(("noUpdate", 2),
          ("other", 1),
          ("replacePhysicalRom", 4),
          ("softwareflash", 3))
    )


_CpqHoFwVerUpdateMethod_Type.__name__ = "Integer32"
_CpqHoFwVerUpdateMethod_Object = MibTableColumn
cpqHoFwVerUpdateMethod = _CpqHoFwVerUpdateMethod_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 14, 1, 1, 9),
    _CpqHoFwVerUpdateMethod_Type()
)
cpqHoFwVerUpdateMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoFwVerUpdateMethod.setStatus("mandatory")
_CpqHoHWInfo_ObjectIdentity = ObjectIdentity
cpqHoHWInfo = _CpqHoHWInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 15)
)


class _CpqHoHWInfoPlatform_Type(Integer32):
    """Custom type cpqHoHWInfoPlatform based on Integer32"""
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
        *(("cellular", 2),
          ("foundation", 3),
          ("serverBlade", 5),
          ("unknown", 1),
          ("virtualMachine", 4))
    )


_CpqHoHWInfoPlatform_Type.__name__ = "Integer32"
_CpqHoHWInfoPlatform_Object = MibScalar
cpqHoHWInfoPlatform = _CpqHoHWInfoPlatform_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 15, 1),
    _CpqHoHWInfoPlatform_Type()
)
cpqHoHWInfoPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoHWInfoPlatform.setStatus("optional")
_CpqPwrThreshold_ObjectIdentity = ObjectIdentity
cpqPwrThreshold = _CpqPwrThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 16)
)


class _CpqPwrWarnType_Type(DisplayString):
    """Custom type cpqPwrWarnType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CpqPwrWarnType_Type.__name__ = "DisplayString"
_CpqPwrWarnType_Object = MibScalar
cpqPwrWarnType = _CpqPwrWarnType_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 16, 1),
    _CpqPwrWarnType_Type()
)
cpqPwrWarnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqPwrWarnType.setStatus("mandatory")
_CpqPwrWarnThreshold_Type = Integer32
_CpqPwrWarnThreshold_Object = MibScalar
cpqPwrWarnThreshold = _CpqPwrWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 16, 2),
    _CpqPwrWarnThreshold_Type()
)
cpqPwrWarnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqPwrWarnThreshold.setStatus("mandatory")
_CpqPwrWarnDuration_Type = Integer32
_CpqPwrWarnDuration_Object = MibScalar
cpqPwrWarnDuration = _CpqPwrWarnDuration_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 16, 3),
    _CpqPwrWarnDuration_Type()
)
cpqPwrWarnDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqPwrWarnDuration.setStatus("mandatory")


class _CpqSerialNum_Type(DisplayString):
    """Custom type cpqSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CpqSerialNum_Type.__name__ = "DisplayString"
_CpqSerialNum_Object = MibScalar
cpqSerialNum = _CpqSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 16, 4),
    _CpqSerialNum_Type()
)
cpqSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSerialNum.setStatus("mandatory")


class _CpqServerUUID_Type(DisplayString):
    """Custom type cpqServerUUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_CpqServerUUID_Type.__name__ = "DisplayString"
_CpqServerUUID_Object = MibScalar
cpqServerUUID = _CpqServerUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 16, 5),
    _CpqServerUUID_Type()
)
cpqServerUUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqServerUUID.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqHoGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11001)
)
cpqHoGenericTrap.setObjects(
    ("CPQHOST-MIB", "cpqHoGenericData")
)
if mibBuilder.loadTexts:
    cpqHoGenericTrap.setStatus(
        ""
    )

cpqHoAppErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11002)
)
cpqHoAppErrorTrap.setObjects(
    ("CPQHOST-MIB", "cpqHoSwPerfAppErrorDesc")
)
if mibBuilder.loadTexts:
    cpqHoAppErrorTrap.setStatus(
        ""
    )

cpqHo2GenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11003)
)
cpqHo2GenericTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoGenericData"))
)
if mibBuilder.loadTexts:
    cpqHo2GenericTrap.setStatus(
        ""
    )

cpqHo2AppErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11004)
)
cpqHo2AppErrorTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoSwPerfAppErrorDesc"))
)
if mibBuilder.loadTexts:
    cpqHo2AppErrorTrap.setStatus(
        ""
    )

cpqHo2NicStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11005)
)
cpqHo2NicStatusOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapSlot"))
)
if mibBuilder.loadTexts:
    cpqHo2NicStatusOk.setStatus(
        ""
    )

cpqHo2NicStatusFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11006)
)
cpqHo2NicStatusFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapSlot"))
)
if mibBuilder.loadTexts:
    cpqHo2NicStatusFailed.setStatus(
        ""
    )

cpqHo2NicSwitchoverOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11007)
)
cpqHo2NicSwitchoverOccurred.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapSlot"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapSlot"))
)
if mibBuilder.loadTexts:
    cpqHo2NicSwitchoverOccurred.setStatus(
        ""
    )

cpqHo2NicStatusOk2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11008)
)
cpqHo2NicStatusOk2.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapSlot"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapPort"))
)
if mibBuilder.loadTexts:
    cpqHo2NicStatusOk2.setStatus(
        ""
    )

cpqHo2NicStatusFailed2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11009)
)
cpqHo2NicStatusFailed2.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapSlot"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapPort"))
)
if mibBuilder.loadTexts:
    cpqHo2NicStatusFailed2.setStatus(
        ""
    )

cpqHo2NicSwitchoverOccurred2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11010)
)
cpqHo2NicSwitchoverOccurred2.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapSlot"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapPort"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapSlot"),
        ("CPQHOST-MIB", "cpqHoIfPhysMapPort"))
)
if mibBuilder.loadTexts:
    cpqHo2NicSwitchoverOccurred2.setStatus(
        ""
    )

cpqHoProcessEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11011)
)
cpqHoProcessEventTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoSwRunningTrapDesc"))
)
if mibBuilder.loadTexts:
    cpqHoProcessEventTrap.setStatus(
        ""
    )

cpqHoProcessCountWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11012)
)
cpqHoProcessCountWarning.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoSWRunningName"),
        ("CPQHOST-MIB", "cpqHoSWRunningCount"),
        ("CPQHOST-MIB", "cpqHoSWRunningCountMin"),
        ("CPQHOST-MIB", "cpqHoSWRunningCountMax"),
        ("CPQHOST-MIB", "cpqHoSWRunningEventTime"))
)
if mibBuilder.loadTexts:
    cpqHoProcessCountWarning.setStatus(
        ""
    )

cpqHoProcessCountNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11013)
)
cpqHoProcessCountNormal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoSWRunningName"),
        ("CPQHOST-MIB", "cpqHoSWRunningCount"),
        ("CPQHOST-MIB", "cpqHoSWRunningCountMin"),
        ("CPQHOST-MIB", "cpqHoSWRunningCountMax"),
        ("CPQHOST-MIB", "cpqHoSWRunningEventTime"))
)
if mibBuilder.loadTexts:
    cpqHoProcessCountNormal.setStatus(
        ""
    )

cpqHoCriticalSoftwareUpdateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11014)
)
cpqHoCriticalSoftwareUpdateTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoCriticalSoftwareUpdateData"))
)
if mibBuilder.loadTexts:
    cpqHoCriticalSoftwareUpdateTrap.setStatus(
        ""
    )

cpqHoCrashDumpNotEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11015)
)
cpqHoCrashDumpNotEnabledTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoCrashDumpState"))
)
if mibBuilder.loadTexts:
    cpqHoCrashDumpNotEnabledTrap.setStatus(
        ""
    )

cpqHoBootPagingFileTooSmallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11016)
)
cpqHoBootPagingFileTooSmallTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoCrashDumpState"),
        ("CPQHOST-MIB", "cpqHoBootPagingFileSize"),
        ("CPQHOST-MIB", "cpqHoBootPagingFileMinimumSize"))
)
if mibBuilder.loadTexts:
    cpqHoBootPagingFileTooSmallTrap.setStatus(
        ""
    )

cpqHoSWRunningStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11017)
)
cpqHoSWRunningStatusChangeTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoSWRunningName"),
        ("CPQHOST-MIB", "cpqHoSWRunningDesc"),
        ("CPQHOST-MIB", "cpqHoSwRunningTrapDesc"),
        ("CPQHOST-MIB", "cpqHoSWRunningVersion"),
        ("CPQHOST-MIB", "cpqHoSWRunningStatus"),
        ("CPQHOST-MIB", "cpqHoSWRunningConfigStatus"),
        ("CPQHOST-MIB", "cpqHoSWRunningIdentifier"),
        ("CPQHOST-MIB", "cpqHoSWRunningRedundancyMode"))
)
if mibBuilder.loadTexts:
    cpqHoSWRunningStatusChangeTrap.setStatus(
        ""
    )

cpqHo2PowerThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11018)
)
cpqHo2PowerThresholdTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqPwrWarnType"),
        ("CPQHOST-MIB", "cpqPwrWarnThreshold"),
        ("CPQHOST-MIB", "cpqPwrWarnDuration"),
        ("CPQHOST-MIB", "cpqSerialNum"),
        ("CPQHOST-MIB", "cpqServerUUID"))
)
if mibBuilder.loadTexts:
    cpqHo2PowerThresholdTrap.setStatus(
        ""
    )

cpqHoBootPagingFileOrFreeSpaceTooSmallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 11019)
)
cpqHoBootPagingFileOrFreeSpaceTooSmallTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHOST-MIB", "cpqHoCrashDumpState"),
        ("CPQHOST-MIB", "cpqHoBootPagingFileSize"),
        ("CPQHOST-MIB", "cpqHoBootPagingFileVolumeFreeSpace"),
        ("CPQHOST-MIB", "cpqHoBootPagingFileMinimumSize"))
)
if mibBuilder.loadTexts:
    cpqHoBootPagingFileOrFreeSpaceTooSmallTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQHOST-MIB",
    **{"compaq": compaq,
       "cpqHoGenericTrap": cpqHoGenericTrap,
       "cpqHoAppErrorTrap": cpqHoAppErrorTrap,
       "cpqHo2GenericTrap": cpqHo2GenericTrap,
       "cpqHo2AppErrorTrap": cpqHo2AppErrorTrap,
       "cpqHo2NicStatusOk": cpqHo2NicStatusOk,
       "cpqHo2NicStatusFailed": cpqHo2NicStatusFailed,
       "cpqHo2NicSwitchoverOccurred": cpqHo2NicSwitchoverOccurred,
       "cpqHo2NicStatusOk2": cpqHo2NicStatusOk2,
       "cpqHo2NicStatusFailed2": cpqHo2NicStatusFailed2,
       "cpqHo2NicSwitchoverOccurred2": cpqHo2NicSwitchoverOccurred2,
       "cpqHoProcessEventTrap": cpqHoProcessEventTrap,
       "cpqHoProcessCountWarning": cpqHoProcessCountWarning,
       "cpqHoProcessCountNormal": cpqHoProcessCountNormal,
       "cpqHoCriticalSoftwareUpdateTrap": cpqHoCriticalSoftwareUpdateTrap,
       "cpqHoCrashDumpNotEnabledTrap": cpqHoCrashDumpNotEnabledTrap,
       "cpqHoBootPagingFileTooSmallTrap": cpqHoBootPagingFileTooSmallTrap,
       "cpqHoSWRunningStatusChangeTrap": cpqHoSWRunningStatusChangeTrap,
       "cpqHo2PowerThresholdTrap": cpqHo2PowerThresholdTrap,
       "cpqHoBootPagingFileOrFreeSpaceTooSmallTrap": cpqHoBootPagingFileOrFreeSpaceTooSmallTrap,
       "cpqHostOs": cpqHostOs,
       "cpqHoMibRev": cpqHoMibRev,
       "cpqHoMibRevMajor": cpqHoMibRevMajor,
       "cpqHoMibRevMinor": cpqHoMibRevMinor,
       "cpqHoMibCondition": cpqHoMibCondition,
       "cpqHoComponent": cpqHoComponent,
       "cpqHoInterface": cpqHoInterface,
       "cpqHoOsCommon": cpqHoOsCommon,
       "cpqHoOsCommonPollFreq": cpqHoOsCommonPollFreq,
       "cpqHoOsCommonModuleTable": cpqHoOsCommonModuleTable,
       "cpqHoOsCommonModuleEntry": cpqHoOsCommonModuleEntry,
       "cpqHoOsCommonModuleIndex": cpqHoOsCommonModuleIndex,
       "cpqHoOsCommonModuleName": cpqHoOsCommonModuleName,
       "cpqHoOsCommonModuleVersion": cpqHoOsCommonModuleVersion,
       "cpqHoOsCommonModuleDate": cpqHoOsCommonModuleDate,
       "cpqHoOsCommonModulePurpose": cpqHoOsCommonModulePurpose,
       "cpqHoInfo": cpqHoInfo,
       "cpqHoName": cpqHoName,
       "cpqHoVersion": cpqHoVersion,
       "cpqHoDesc": cpqHoDesc,
       "cpqHoOsType": cpqHoOsType,
       "cpqHoTelnet": cpqHoTelnet,
       "cpqHoSystemRole": cpqHoSystemRole,
       "cpqHoSystemRoleDetail": cpqHoSystemRoleDetail,
       "cpqHoCrashDumpState": cpqHoCrashDumpState,
       "cpqHoCrashDumpCondition": cpqHoCrashDumpCondition,
       "cpqHoCrashDumpMonitoring": cpqHoCrashDumpMonitoring,
       "cpqHoMaxLogicalCPUSupported": cpqHoMaxLogicalCPUSupported,
       "cpqHoUtil": cpqHoUtil,
       "cpqHoCpuUtilTable": cpqHoCpuUtilTable,
       "cpqHoCpuUtilEntry": cpqHoCpuUtilEntry,
       "cpqHoCpuUtilUnitIndex": cpqHoCpuUtilUnitIndex,
       "cpqHoCpuUtilMin": cpqHoCpuUtilMin,
       "cpqHoCpuUtilFiveMin": cpqHoCpuUtilFiveMin,
       "cpqHoCpuUtilThirtyMin": cpqHoCpuUtilThirtyMin,
       "cpqHoCpuUtilHour": cpqHoCpuUtilHour,
       "cpqHoCpuUtilHwLocation": cpqHoCpuUtilHwLocation,
       "cpqHoFileSys": cpqHoFileSys,
       "cpqHoFileSysTable": cpqHoFileSysTable,
       "cpqHoFileSysEntry": cpqHoFileSysEntry,
       "cpqHoFileSysIndex": cpqHoFileSysIndex,
       "cpqHoFileSysDesc": cpqHoFileSysDesc,
       "cpqHoFileSysSpaceTotal": cpqHoFileSysSpaceTotal,
       "cpqHoFileSysSpaceUsed": cpqHoFileSysSpaceUsed,
       "cpqHoFileSysPercentSpaceUsed": cpqHoFileSysPercentSpaceUsed,
       "cpqHoFileSysAllocUnitsTotal": cpqHoFileSysAllocUnitsTotal,
       "cpqHoFileSysAllocUnitsUsed": cpqHoFileSysAllocUnitsUsed,
       "cpqHoFileSysStatus": cpqHoFileSysStatus,
       "cpqHoFileSysCondition": cpqHoFileSysCondition,
       "cpqHoIfPhysMap": cpqHoIfPhysMap,
       "cpqHoIfPhysMapTable": cpqHoIfPhysMapTable,
       "cpqHoIfPhysMapEntry": cpqHoIfPhysMapEntry,
       "cpqHoIfPhysMapIndex": cpqHoIfPhysMapIndex,
       "cpqHoIfPhysMapSlot": cpqHoIfPhysMapSlot,
       "cpqHoIfPhysMapIoBaseAddr": cpqHoIfPhysMapIoBaseAddr,
       "cpqHoIfPhysMapIrq": cpqHoIfPhysMapIrq,
       "cpqHoIfPhysMapDma": cpqHoIfPhysMapDma,
       "cpqHoIfPhysMapMemBaseAddr": cpqHoIfPhysMapMemBaseAddr,
       "cpqHoIfPhysMapPort": cpqHoIfPhysMapPort,
       "cpqHoIfPhysMapDuplexState": cpqHoIfPhysMapDuplexState,
       "cpqHoIfPhysMapCondition": cpqHoIfPhysMapCondition,
       "cpqHoIfPhysMapOverallCondition": cpqHoIfPhysMapOverallCondition,
       "cpqHoSWRunning": cpqHoSWRunning,
       "cpqHoSWRunningTable": cpqHoSWRunningTable,
       "cpqHoSWRunningEntry": cpqHoSWRunningEntry,
       "cpqHoSWRunningIndex": cpqHoSWRunningIndex,
       "cpqHoSWRunningName": cpqHoSWRunningName,
       "cpqHoSWRunningDesc": cpqHoSWRunningDesc,
       "cpqHoSWRunningVersion": cpqHoSWRunningVersion,
       "cpqHoSWRunningDate": cpqHoSWRunningDate,
       "cpqHoSWRunningMonitor": cpqHoSWRunningMonitor,
       "cpqHoSWRunningState": cpqHoSWRunningState,
       "cpqHoSWRunningCount": cpqHoSWRunningCount,
       "cpqHoSWRunningCountMin": cpqHoSWRunningCountMin,
       "cpqHoSWRunningCountMax": cpqHoSWRunningCountMax,
       "cpqHoSWRunningEventTime": cpqHoSWRunningEventTime,
       "cpqHoSWRunningStatus": cpqHoSWRunningStatus,
       "cpqHoSWRunningConfigStatus": cpqHoSWRunningConfigStatus,
       "cpqHoSWRunningIdentifier": cpqHoSWRunningIdentifier,
       "cpqHoSWRunningRedundancyMode": cpqHoSWRunningRedundancyMode,
       "cpqHoSwRunningTrapDesc": cpqHoSwRunningTrapDesc,
       "cpqHoSwVer": cpqHoSwVer,
       "cpqHoSwVerNextIndex": cpqHoSwVerNextIndex,
       "cpqHoSwVerTable": cpqHoSwVerTable,
       "cpqHoSwVerEntry": cpqHoSwVerEntry,
       "cpqHoSwVerIndex": cpqHoSwVerIndex,
       "cpqHoSwVerStatus": cpqHoSwVerStatus,
       "cpqHoSwVerType": cpqHoSwVerType,
       "cpqHoSwVerName": cpqHoSwVerName,
       "cpqHoSwVerDescription": cpqHoSwVerDescription,
       "cpqHoSwVerDate": cpqHoSwVerDate,
       "cpqHoSwVerLocation": cpqHoSwVerLocation,
       "cpqHoSwVerVersion": cpqHoSwVerVersion,
       "cpqHoSwVerVersionBinary": cpqHoSwVerVersionBinary,
       "cpqHoSwVerAgentsVer": cpqHoSwVerAgentsVer,
       "cpqHoGeneric": cpqHoGeneric,
       "cpqHoGenericData": cpqHoGenericData,
       "cpqHoCriticalSoftwareUpdateData": cpqHoCriticalSoftwareUpdateData,
       "cpqHoSwPerf": cpqHoSwPerf,
       "cpqHoSwPerfAppErrorDesc": cpqHoSwPerfAppErrorDesc,
       "cpqHoSystemStatus": cpqHoSystemStatus,
       "cpqHoMibStatusArray": cpqHoMibStatusArray,
       "cpqHoConfigChangedDate": cpqHoConfigChangedDate,
       "cpqHoGUID": cpqHoGUID,
       "cpqHoCodeServer": cpqHoCodeServer,
       "cpqHoWebMgmtPort": cpqHoWebMgmtPort,
       "cpqHoGUIDCanonical": cpqHoGUIDCanonical,
       "cpqHoTrapInfo": cpqHoTrapInfo,
       "cpqHoTrapFlags": cpqHoTrapFlags,
       "cpqHoClients": cpqHoClients,
       "cpqHoClientLastModified": cpqHoClientLastModified,
       "cpqHoClientDelete": cpqHoClientDelete,
       "cpqHoClientTable": cpqHoClientTable,
       "cpqHoClientEntry": cpqHoClientEntry,
       "cpqHoClientIndex": cpqHoClientIndex,
       "cpqHoClientName": cpqHoClientName,
       "cpqHoClientIpxAddress": cpqHoClientIpxAddress,
       "cpqHoClientIpAddress": cpqHoClientIpAddress,
       "cpqHoClientCommunity": cpqHoClientCommunity,
       "cpqHoClientID": cpqHoClientID,
       "cpqHoMemory": cpqHoMemory,
       "cpqHoPhysicalMemorySize": cpqHoPhysicalMemorySize,
       "cpqHoPhysicalMemoryFree": cpqHoPhysicalMemoryFree,
       "cpqHoPagingMemorySize": cpqHoPagingMemorySize,
       "cpqHoPagingMemoryFree": cpqHoPagingMemoryFree,
       "cpqHoBootPagingFileSize": cpqHoBootPagingFileSize,
       "cpqHoBootPagingFileMinimumSize": cpqHoBootPagingFileMinimumSize,
       "cpqHoBootPagingFileVolumeFreeSpace": cpqHoBootPagingFileVolumeFreeSpace,
       "cpqHoFwVer": cpqHoFwVer,
       "cpqHoFwVerTable": cpqHoFwVerTable,
       "cpqHoFwVerEntry": cpqHoFwVerEntry,
       "cpqHoFwVerIndex": cpqHoFwVerIndex,
       "cpqHoFwVerCategory": cpqHoFwVerCategory,
       "cpqHoFwVerDeviceType": cpqHoFwVerDeviceType,
       "cpqHoFwVerDisplayName": cpqHoFwVerDisplayName,
       "cpqHoFwVerVersion": cpqHoFwVerVersion,
       "cpqHoFwVerLocation": cpqHoFwVerLocation,
       "cpqHoFwVerXmlString": cpqHoFwVerXmlString,
       "cpqHoFwVerKeyString": cpqHoFwVerKeyString,
       "cpqHoFwVerUpdateMethod": cpqHoFwVerUpdateMethod,
       "cpqHoHWInfo": cpqHoHWInfo,
       "cpqHoHWInfoPlatform": cpqHoHWInfoPlatform,
       "cpqPwrThreshold": cpqPwrThreshold,
       "cpqPwrWarnType": cpqPwrWarnType,
       "cpqPwrWarnThreshold": cpqPwrWarnThreshold,
       "cpqPwrWarnDuration": cpqPwrWarnDuration,
       "cpqSerialNum": cpqSerialNum,
       "cpqServerUUID": cpqServerUUID}
)
