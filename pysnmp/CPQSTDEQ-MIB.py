# SNMP MIB module (CPQSTDEQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQSTDEQ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:32 2024
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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqStdEquipment_ObjectIdentity = ObjectIdentity
cpqStdEquipment = _CpqStdEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1)
)
_CpqSeMibRev_ObjectIdentity = ObjectIdentity
cpqSeMibRev = _CpqSeMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 1)
)


class _CpqSeMibRevMajor_Type(Integer32):
    """Custom type cpqSeMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqSeMibRevMajor_Type.__name__ = "Integer32"
_CpqSeMibRevMajor_Object = MibScalar
cpqSeMibRevMajor = _CpqSeMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 1, 1),
    _CpqSeMibRevMajor_Type()
)
cpqSeMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeMibRevMajor.setStatus("mandatory")


class _CpqSeMibRevMinor_Type(Integer32):
    """Custom type cpqSeMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeMibRevMinor_Type.__name__ = "Integer32"
_CpqSeMibRevMinor_Object = MibScalar
cpqSeMibRevMinor = _CpqSeMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 1, 2),
    _CpqSeMibRevMinor_Type()
)
cpqSeMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeMibRevMinor.setStatus("mandatory")


class _CpqSeMibCondition_Type(Integer32):
    """Custom type cpqSeMibCondition based on Integer32"""
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


_CpqSeMibCondition_Type.__name__ = "Integer32"
_CpqSeMibCondition_Object = MibScalar
cpqSeMibCondition = _CpqSeMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 1, 3),
    _CpqSeMibCondition_Type()
)
cpqSeMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeMibCondition.setStatus("mandatory")
_CpqSeComponent_ObjectIdentity = ObjectIdentity
cpqSeComponent = _CpqSeComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2)
)
_CpqSeInterface_ObjectIdentity = ObjectIdentity
cpqSeInterface = _CpqSeInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 1)
)
_CpqSeOsCommon_ObjectIdentity = ObjectIdentity
cpqSeOsCommon = _CpqSeOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 1, 4)
)


class _CpqSeOsCommonPollFreq_Type(Integer32):
    """Custom type cpqSeOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqSeOsCommonPollFreq_Object = MibScalar
cpqSeOsCommonPollFreq = _CpqSeOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 1, 4, 1),
    _CpqSeOsCommonPollFreq_Type()
)
cpqSeOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSeOsCommonPollFreq.setStatus("mandatory")
_CpqSeOsCommonModuleTable_Object = MibTable
cpqSeOsCommonModuleTable = _CpqSeOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqSeOsCommonModuleTable.setStatus("deprecated")
_CpqSeOsCommonModuleEntry_Object = MibTableRow
cpqSeOsCommonModuleEntry = _CpqSeOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 1, 4, 2, 1)
)
cpqSeOsCommonModuleEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqSeOsCommonModuleEntry.setStatus("deprecated")


class _CpqSeOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqSeOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqSeOsCommonModuleIndex_Object = MibTableColumn
cpqSeOsCommonModuleIndex = _CpqSeOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 1, 4, 2, 1, 1),
    _CpqSeOsCommonModuleIndex_Type()
)
cpqSeOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeOsCommonModuleIndex.setStatus("deprecated")


class _CpqSeOsCommonModuleName_Type(DisplayString):
    """Custom type cpqSeOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqSeOsCommonModuleName_Object = MibTableColumn
cpqSeOsCommonModuleName = _CpqSeOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 1, 4, 2, 1, 2),
    _CpqSeOsCommonModuleName_Type()
)
cpqSeOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeOsCommonModuleName.setStatus("deprecated")


class _CpqSeOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqSeOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqSeOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqSeOsCommonModuleVersion_Object = MibTableColumn
cpqSeOsCommonModuleVersion = _CpqSeOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 1, 4, 2, 1, 3),
    _CpqSeOsCommonModuleVersion_Type()
)
cpqSeOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeOsCommonModuleVersion.setStatus("deprecated")


class _CpqSeOsCommonModuleDate_Type(OctetString):
    """Custom type cpqSeOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqSeOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqSeOsCommonModuleDate_Object = MibTableColumn
cpqSeOsCommonModuleDate = _CpqSeOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 1, 4, 2, 1, 4),
    _CpqSeOsCommonModuleDate_Type()
)
cpqSeOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeOsCommonModuleDate.setStatus("deprecated")


class _CpqSeOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqSeOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqSeOsCommonModulePurpose_Object = MibTableColumn
cpqSeOsCommonModulePurpose = _CpqSeOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 1, 4, 2, 1, 5),
    _CpqSeOsCommonModulePurpose_Type()
)
cpqSeOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeOsCommonModulePurpose.setStatus("deprecated")
_CpqSeProcessor_ObjectIdentity = ObjectIdentity
cpqSeProcessor = _CpqSeProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2)
)
_CpqSeCpuTable_Object = MibTable
cpqSeCpuTable = _CpqSeCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqSeCpuTable.setStatus("mandatory")
_CpqSeCpuEntry_Object = MibTableRow
cpqSeCpuEntry = _CpqSeCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1)
)
cpqSeCpuEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeCpuUnitIndex"),
)
if mibBuilder.loadTexts:
    cpqSeCpuEntry.setStatus("mandatory")


class _CpqSeCpuUnitIndex_Type(Integer32):
    """Custom type cpqSeCpuUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCpuUnitIndex_Type.__name__ = "Integer32"
_CpqSeCpuUnitIndex_Object = MibTableColumn
cpqSeCpuUnitIndex = _CpqSeCpuUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 1),
    _CpqSeCpuUnitIndex_Type()
)
cpqSeCpuUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuUnitIndex.setStatus("mandatory")


class _CpqSeCpuSlot_Type(Integer32):
    """Custom type cpqSeCpuSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeCpuSlot_Type.__name__ = "Integer32"
_CpqSeCpuSlot_Object = MibTableColumn
cpqSeCpuSlot = _CpqSeCpuSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 2),
    _CpqSeCpuSlot_Type()
)
cpqSeCpuSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuSlot.setStatus("mandatory")


class _CpqSeCpuName_Type(DisplayString):
    """Custom type cpqSeCpuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCpuName_Type.__name__ = "DisplayString"
_CpqSeCpuName_Object = MibTableColumn
cpqSeCpuName = _CpqSeCpuName_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 3),
    _CpqSeCpuName_Type()
)
cpqSeCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuName.setStatus("mandatory")


class _CpqSeCpuSpeed_Type(Integer32):
    """Custom type cpqSeCpuSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCpuSpeed_Type.__name__ = "Integer32"
_CpqSeCpuSpeed_Object = MibTableColumn
cpqSeCpuSpeed = _CpqSeCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 4),
    _CpqSeCpuSpeed_Type()
)
cpqSeCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuSpeed.setStatus("mandatory")


class _CpqSeCpuStep_Type(Integer32):
    """Custom type cpqSeCpuStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCpuStep_Type.__name__ = "Integer32"
_CpqSeCpuStep_Object = MibTableColumn
cpqSeCpuStep = _CpqSeCpuStep_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 5),
    _CpqSeCpuStep_Type()
)
cpqSeCpuStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuStep.setStatus("mandatory")


class _CpqSeCpuStatus_Type(Integer32):
    """Custom type cpqSeCpuStatus based on Integer32"""
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
        *(("degraded", 3),
          ("disabled", 5),
          ("failed", 4),
          ("ok", 2),
          ("unknown", 1))
    )


_CpqSeCpuStatus_Type.__name__ = "Integer32"
_CpqSeCpuStatus_Object = MibTableColumn
cpqSeCpuStatus = _CpqSeCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 6),
    _CpqSeCpuStatus_Type()
)
cpqSeCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuStatus.setStatus("mandatory")


class _CpqSeCpuExtSpeed_Type(Integer32):
    """Custom type cpqSeCpuExtSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCpuExtSpeed_Type.__name__ = "Integer32"
_CpqSeCpuExtSpeed_Object = MibTableColumn
cpqSeCpuExtSpeed = _CpqSeCpuExtSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 7),
    _CpqSeCpuExtSpeed_Type()
)
cpqSeCpuExtSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuExtSpeed.setStatus("mandatory")


class _CpqSeCpuDesigner_Type(Integer32):
    """Custom type cpqSeCpuDesigner based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("amd", 3),
          ("compaq", 7),
          ("cyrix", 4),
          ("intel", 2),
          ("mips", 10),
          ("mitsubishi", 9),
          ("nexgen", 6),
          ("samsung", 8),
          ("ti", 5),
          ("unknown", 1))
    )


_CpqSeCpuDesigner_Type.__name__ = "Integer32"
_CpqSeCpuDesigner_Object = MibTableColumn
cpqSeCpuDesigner = _CpqSeCpuDesigner_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 8),
    _CpqSeCpuDesigner_Type()
)
cpqSeCpuDesigner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuDesigner.setStatus("mandatory")


class _CpqSeCpuSocketNumber_Type(Integer32):
    """Custom type cpqSeCpuSocketNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeCpuSocketNumber_Type.__name__ = "Integer32"
_CpqSeCpuSocketNumber_Object = MibTableColumn
cpqSeCpuSocketNumber = _CpqSeCpuSocketNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 9),
    _CpqSeCpuSocketNumber_Type()
)
cpqSeCpuSocketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuSocketNumber.setStatus("mandatory")


class _CpqSeCpuThreshPassed_Type(Integer32):
    """Custom type cpqSeCpuThreshPassed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 3),
          ("unsupported", 1))
    )


_CpqSeCpuThreshPassed_Type.__name__ = "Integer32"
_CpqSeCpuThreshPassed_Object = MibTableColumn
cpqSeCpuThreshPassed = _CpqSeCpuThreshPassed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 10),
    _CpqSeCpuThreshPassed_Type()
)
cpqSeCpuThreshPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuThreshPassed.setStatus("mandatory")


class _CpqSeCpuHwLocation_Type(DisplayString):
    """Custom type cpqSeCpuHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCpuHwLocation_Type.__name__ = "DisplayString"
_CpqSeCpuHwLocation_Object = MibTableColumn
cpqSeCpuHwLocation = _CpqSeCpuHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 11),
    _CpqSeCpuHwLocation_Type()
)
cpqSeCpuHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuHwLocation.setStatus("optional")


class _CpqSeCpuCellTablePtr_Type(Integer32):
    """Custom type cpqSeCpuCellTablePtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CpqSeCpuCellTablePtr_Type.__name__ = "Integer32"
_CpqSeCpuCellTablePtr_Object = MibTableColumn
cpqSeCpuCellTablePtr = _CpqSeCpuCellTablePtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 12),
    _CpqSeCpuCellTablePtr_Type()
)
cpqSeCpuCellTablePtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCellTablePtr.setStatus("optional")


class _CpqSeCpuPowerpodStatus_Type(Integer32):
    """Custom type cpqSeCpuPowerpodStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("notfailed", 1))
    )


_CpqSeCpuPowerpodStatus_Type.__name__ = "Integer32"
_CpqSeCpuPowerpodStatus_Object = MibTableColumn
cpqSeCpuPowerpodStatus = _CpqSeCpuPowerpodStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 13),
    _CpqSeCpuPowerpodStatus_Type()
)
cpqSeCpuPowerpodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuPowerpodStatus.setStatus("optional")


class _CpqSeCpuArchitectureRevision_Type(DisplayString):
    """Custom type cpqSeCpuArchitectureRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCpuArchitectureRevision_Type.__name__ = "DisplayString"
_CpqSeCpuArchitectureRevision_Object = MibTableColumn
cpqSeCpuArchitectureRevision = _CpqSeCpuArchitectureRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 14),
    _CpqSeCpuArchitectureRevision_Type()
)
cpqSeCpuArchitectureRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuArchitectureRevision.setStatus("optional")
_CpqSeCpuCore_Type = Integer32
_CpqSeCpuCore_Object = MibTableColumn
cpqSeCpuCore = _CpqSeCpuCore_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 15),
    _CpqSeCpuCore_Type()
)
cpqSeCpuCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCore.setStatus("optional")


class _CpqSeCPUSerialNumber_Type(DisplayString):
    """Custom type cpqSeCPUSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCPUSerialNumber_Type.__name__ = "DisplayString"
_CpqSeCPUSerialNumber_Object = MibTableColumn
cpqSeCPUSerialNumber = _CpqSeCPUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 16),
    _CpqSeCPUSerialNumber_Type()
)
cpqSeCPUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCPUSerialNumber.setStatus("optional")


class _CpqSeCPUPartNumber_Type(DisplayString):
    """Custom type cpqSeCPUPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCPUPartNumber_Type.__name__ = "DisplayString"
_CpqSeCPUPartNumber_Object = MibTableColumn
cpqSeCPUPartNumber = _CpqSeCPUPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 17),
    _CpqSeCPUPartNumber_Type()
)
cpqSeCPUPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCPUPartNumber.setStatus("optional")


class _CpqSeCPUSerialNumberMfgr_Type(DisplayString):
    """Custom type cpqSeCPUSerialNumberMfgr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCPUSerialNumberMfgr_Type.__name__ = "DisplayString"
_CpqSeCPUSerialNumberMfgr_Object = MibTableColumn
cpqSeCPUSerialNumberMfgr = _CpqSeCPUSerialNumberMfgr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 18),
    _CpqSeCPUSerialNumberMfgr_Type()
)
cpqSeCPUSerialNumberMfgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCPUSerialNumberMfgr.setStatus("optional")


class _CpqSeCPUPartNumberMfgr_Type(DisplayString):
    """Custom type cpqSeCPUPartNumberMfgr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCPUPartNumberMfgr_Type.__name__ = "DisplayString"
_CpqSeCPUPartNumberMfgr_Object = MibTableColumn
cpqSeCPUPartNumberMfgr = _CpqSeCPUPartNumberMfgr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 19),
    _CpqSeCPUPartNumberMfgr_Type()
)
cpqSeCPUPartNumberMfgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCPUPartNumberMfgr.setStatus("optional")


class _CpqSeCPUCoreIndex_Type(Integer32):
    """Custom type cpqSeCPUCoreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCPUCoreIndex_Type.__name__ = "Integer32"
_CpqSeCPUCoreIndex_Object = MibTableColumn
cpqSeCPUCoreIndex = _CpqSeCPUCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 20),
    _CpqSeCPUCoreIndex_Type()
)
cpqSeCPUCoreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCPUCoreIndex.setStatus("optional")


class _CpqSeCPUMaxSpeed_Type(Integer32):
    """Custom type cpqSeCPUMaxSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCPUMaxSpeed_Type.__name__ = "Integer32"
_CpqSeCPUMaxSpeed_Object = MibTableColumn
cpqSeCPUMaxSpeed = _CpqSeCPUMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 21),
    _CpqSeCPUMaxSpeed_Type()
)
cpqSeCPUMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCPUMaxSpeed.setStatus("optional")


class _CpqSeCPUCoreThreadIndex_Type(Integer32):
    """Custom type cpqSeCPUCoreThreadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCPUCoreThreadIndex_Type.__name__ = "Integer32"
_CpqSeCPUCoreThreadIndex_Object = MibTableColumn
cpqSeCPUCoreThreadIndex = _CpqSeCPUCoreThreadIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 22),
    _CpqSeCPUCoreThreadIndex_Type()
)
cpqSeCPUCoreThreadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCPUCoreThreadIndex.setStatus("optional")


class _CpqSeCPUChipGenerationName_Type(DisplayString):
    """Custom type cpqSeCPUChipGenerationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCPUChipGenerationName_Type.__name__ = "DisplayString"
_CpqSeCPUChipGenerationName_Object = MibTableColumn
cpqSeCPUChipGenerationName = _CpqSeCPUChipGenerationName_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 23),
    _CpqSeCPUChipGenerationName_Type()
)
cpqSeCPUChipGenerationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCPUChipGenerationName.setStatus("optional")


class _CpqSeCPUMultiThreadStatus_Type(Integer32):
    """Custom type cpqSeCPUMultiThreadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("unknown", 1))
    )


_CpqSeCPUMultiThreadStatus_Type.__name__ = "Integer32"
_CpqSeCPUMultiThreadStatus_Object = MibTableColumn
cpqSeCPUMultiThreadStatus = _CpqSeCPUMultiThreadStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 24),
    _CpqSeCPUMultiThreadStatus_Type()
)
cpqSeCPUMultiThreadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCPUMultiThreadStatus.setStatus("optional")


class _CpqSeCPUCoreMaxThreads_Type(Integer32):
    """Custom type cpqSeCPUCoreMaxThreads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCPUCoreMaxThreads_Type.__name__ = "Integer32"
_CpqSeCPUCoreMaxThreads_Object = MibTableColumn
cpqSeCPUCoreMaxThreads = _CpqSeCPUCoreMaxThreads_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 25),
    _CpqSeCPUCoreMaxThreads_Type()
)
cpqSeCPUCoreMaxThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCPUCoreMaxThreads.setStatus("optional")


class _CpqSeCpuLowPowerStatus_Type(Integer32):
    """Custom type cpqSeCpuLowPowerStatus based on Integer32"""
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
        *(("highpowered", 4),
          ("lowpowered", 2),
          ("normalpowered", 3),
          ("unknown", 1))
    )


_CpqSeCpuLowPowerStatus_Type.__name__ = "Integer32"
_CpqSeCpuLowPowerStatus_Object = MibTableColumn
cpqSeCpuLowPowerStatus = _CpqSeCpuLowPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 26),
    _CpqSeCpuLowPowerStatus_Type()
)
cpqSeCpuLowPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuLowPowerStatus.setStatus("mandatory")


class _CpqSeCpuPrimary_Type(Integer32):
    """Custom type cpqSeCpuPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 3),
          ("unknown", 1))
    )


_CpqSeCpuPrimary_Type.__name__ = "Integer32"
_CpqSeCpuPrimary_Object = MibTableColumn
cpqSeCpuPrimary = _CpqSeCpuPrimary_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 27),
    _CpqSeCpuPrimary_Type()
)
cpqSeCpuPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuPrimary.setStatus("mandatory")
_CpqSeCpuCoreSteppingText_Type = DisplayString
_CpqSeCpuCoreSteppingText_Object = MibTableColumn
cpqSeCpuCoreSteppingText = _CpqSeCpuCoreSteppingText_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 28),
    _CpqSeCpuCoreSteppingText_Type()
)
cpqSeCpuCoreSteppingText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCoreSteppingText.setStatus("optional")
_CpqSeCpuCurrentPerformanceState_Type = Integer32
_CpqSeCpuCurrentPerformanceState_Object = MibTableColumn
cpqSeCpuCurrentPerformanceState = _CpqSeCpuCurrentPerformanceState_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 29),
    _CpqSeCpuCurrentPerformanceState_Type()
)
cpqSeCpuCurrentPerformanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCurrentPerformanceState.setStatus("optional")
_CpqSeCpuMinPerformanceState_Type = Integer32
_CpqSeCpuMinPerformanceState_Object = MibTableColumn
cpqSeCpuMinPerformanceState = _CpqSeCpuMinPerformanceState_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 30),
    _CpqSeCpuMinPerformanceState_Type()
)
cpqSeCpuMinPerformanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuMinPerformanceState.setStatus("optional")
_CpqSeCpuMaxPerformanceState_Type = Integer32
_CpqSeCpuMaxPerformanceState_Object = MibTableColumn
cpqSeCpuMaxPerformanceState = _CpqSeCpuMaxPerformanceState_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 1, 1, 31),
    _CpqSeCpuMaxPerformanceState_Type()
)
cpqSeCpuMaxPerformanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuMaxPerformanceState.setStatus("optional")
_CpqSeFpuTable_Object = MibTable
cpqSeFpuTable = _CpqSeFpuTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cpqSeFpuTable.setStatus("mandatory")
_CpqSeFpuEntry_Object = MibTableRow
cpqSeFpuEntry = _CpqSeFpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 2, 1)
)
cpqSeFpuEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeFpuUnitIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeFpuChipIndex"),
)
if mibBuilder.loadTexts:
    cpqSeFpuEntry.setStatus("mandatory")


class _CpqSeFpuUnitIndex_Type(Integer32):
    """Custom type cpqSeFpuUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeFpuUnitIndex_Type.__name__ = "Integer32"
_CpqSeFpuUnitIndex_Object = MibTableColumn
cpqSeFpuUnitIndex = _CpqSeFpuUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 2, 1, 1),
    _CpqSeFpuUnitIndex_Type()
)
cpqSeFpuUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFpuUnitIndex.setStatus("mandatory")


class _CpqSeFpuChipIndex_Type(Integer32):
    """Custom type cpqSeFpuChipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeFpuChipIndex_Type.__name__ = "Integer32"
_CpqSeFpuChipIndex_Object = MibTableColumn
cpqSeFpuChipIndex = _CpqSeFpuChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 2, 1, 2),
    _CpqSeFpuChipIndex_Type()
)
cpqSeFpuChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFpuChipIndex.setStatus("mandatory")


class _CpqSeFpuSlot_Type(Integer32):
    """Custom type cpqSeFpuSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeFpuSlot_Type.__name__ = "Integer32"
_CpqSeFpuSlot_Object = MibTableColumn
cpqSeFpuSlot = _CpqSeFpuSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 2, 1, 3),
    _CpqSeFpuSlot_Type()
)
cpqSeFpuSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFpuSlot.setStatus("mandatory")


class _CpqSeFpuName_Type(DisplayString):
    """Custom type cpqSeFpuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeFpuName_Type.__name__ = "DisplayString"
_CpqSeFpuName_Object = MibTableColumn
cpqSeFpuName = _CpqSeFpuName_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 2, 1, 4),
    _CpqSeFpuName_Type()
)
cpqSeFpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFpuName.setStatus("mandatory")


class _CpqSeFpuSpeed_Type(Integer32):
    """Custom type cpqSeFpuSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeFpuSpeed_Type.__name__ = "Integer32"
_CpqSeFpuSpeed_Object = MibTableColumn
cpqSeFpuSpeed = _CpqSeFpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 2, 1, 5),
    _CpqSeFpuSpeed_Type()
)
cpqSeFpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFpuSpeed.setStatus("mandatory")


class _CpqSeFpuType_Type(Integer32):
    """Custom type cpqSeFpuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("embedded", 2),
          ("external", 3),
          ("other", 1))
    )


_CpqSeFpuType_Type.__name__ = "Integer32"
_CpqSeFpuType_Object = MibTableColumn
cpqSeFpuType = _CpqSeFpuType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 2, 1, 6),
    _CpqSeFpuType_Type()
)
cpqSeFpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFpuType.setStatus("mandatory")


class _CpqSeFpuHwLocation_Type(DisplayString):
    """Custom type cpqSeFpuHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeFpuHwLocation_Type.__name__ = "DisplayString"
_CpqSeFpuHwLocation_Object = MibTableColumn
cpqSeFpuHwLocation = _CpqSeFpuHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 2, 1, 7),
    _CpqSeFpuHwLocation_Type()
)
cpqSeFpuHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFpuHwLocation.setStatus("optional")
_CpqSeCpuCacheTable_Object = MibTable
cpqSeCpuCacheTable = _CpqSeCpuCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cpqSeCpuCacheTable.setStatus("mandatory")
_CpqSeCpuCacheEntry_Object = MibTableRow
cpqSeCpuCacheEntry = _CpqSeCpuCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3, 1)
)
cpqSeCpuCacheEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeCpuCacheUnitIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeCpuCacheLevelIndex"),
)
if mibBuilder.loadTexts:
    cpqSeCpuCacheEntry.setStatus("mandatory")


class _CpqSeCpuCacheUnitIndex_Type(Integer32):
    """Custom type cpqSeCpuCacheUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCpuCacheUnitIndex_Type.__name__ = "Integer32"
_CpqSeCpuCacheUnitIndex_Object = MibTableColumn
cpqSeCpuCacheUnitIndex = _CpqSeCpuCacheUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3, 1, 1),
    _CpqSeCpuCacheUnitIndex_Type()
)
cpqSeCpuCacheUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCacheUnitIndex.setStatus("mandatory")


class _CpqSeCpuCacheLevelIndex_Type(Integer32):
    """Custom type cpqSeCpuCacheLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeCpuCacheLevelIndex_Type.__name__ = "Integer32"
_CpqSeCpuCacheLevelIndex_Object = MibTableColumn
cpqSeCpuCacheLevelIndex = _CpqSeCpuCacheLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3, 1, 2),
    _CpqSeCpuCacheLevelIndex_Type()
)
cpqSeCpuCacheLevelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCacheLevelIndex.setStatus("mandatory")


class _CpqSeCpuCacheSize_Type(Integer32):
    """Custom type cpqSeCpuCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSeCpuCacheSize_Type.__name__ = "Integer32"
_CpqSeCpuCacheSize_Object = MibTableColumn
cpqSeCpuCacheSize = _CpqSeCpuCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3, 1, 3),
    _CpqSeCpuCacheSize_Type()
)
cpqSeCpuCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCacheSize.setStatus("mandatory")


class _CpqSeCpuCacheSpeed_Type(Integer32):
    """Custom type cpqSeCpuCacheSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCpuCacheSpeed_Type.__name__ = "Integer32"
_CpqSeCpuCacheSpeed_Object = MibTableColumn
cpqSeCpuCacheSpeed = _CpqSeCpuCacheSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3, 1, 4),
    _CpqSeCpuCacheSpeed_Type()
)
cpqSeCpuCacheSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCacheSpeed.setStatus("mandatory")


class _CpqSeCpuCacheStatus_Type(Integer32):
    """Custom type cpqSeCpuCacheStatus based on Integer32"""
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


_CpqSeCpuCacheStatus_Type.__name__ = "Integer32"
_CpqSeCpuCacheStatus_Object = MibTableColumn
cpqSeCpuCacheStatus = _CpqSeCpuCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3, 1, 5),
    _CpqSeCpuCacheStatus_Type()
)
cpqSeCpuCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCacheStatus.setStatus("mandatory")


class _CpqSeCpuCacheWritePolicy_Type(Integer32):
    """Custom type cpqSeCpuCacheWritePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("write-back", 3),
          ("write-through", 2))
    )


_CpqSeCpuCacheWritePolicy_Type.__name__ = "Integer32"
_CpqSeCpuCacheWritePolicy_Object = MibTableColumn
cpqSeCpuCacheWritePolicy = _CpqSeCpuCacheWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3, 1, 6),
    _CpqSeCpuCacheWritePolicy_Type()
)
cpqSeCpuCacheWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCacheWritePolicy.setStatus("mandatory")


class _CpqSeCpuCacheHwLocation_Type(DisplayString):
    """Custom type cpqSeCpuCacheHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCpuCacheHwLocation_Type.__name__ = "DisplayString"
_CpqSeCpuCacheHwLocation_Object = MibTableColumn
cpqSeCpuCacheHwLocation = _CpqSeCpuCacheHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3, 1, 7),
    _CpqSeCpuCacheHwLocation_Type()
)
cpqSeCpuCacheHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCacheHwLocation.setStatus("optional")


class _CpqSeCpuCacheCpuSlot_Type(Integer32):
    """Custom type cpqSeCpuCacheCpuSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeCpuCacheCpuSlot_Type.__name__ = "Integer32"
_CpqSeCpuCacheCpuSlot_Object = MibTableColumn
cpqSeCpuCacheCpuSlot = _CpqSeCpuCacheCpuSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3, 1, 8),
    _CpqSeCpuCacheCpuSlot_Type()
)
cpqSeCpuCacheCpuSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCacheCpuSlot.setStatus("optional")
_CpqSeCpuCacheCpuCoreIndex_Type = Integer32
_CpqSeCpuCacheCpuCoreIndex_Object = MibTableColumn
cpqSeCpuCacheCpuCoreIndex = _CpqSeCpuCacheCpuCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 2, 3, 1, 9),
    _CpqSeCpuCacheCpuCoreIndex_Type()
)
cpqSeCpuCacheCpuCoreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCpuCacheCpuCoreIndex.setStatus("optional")
_CpqSeMemory_ObjectIdentity = ObjectIdentity
cpqSeMemory = _CpqSeMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 3)
)


class _CpqSeBaseMem_Type(Integer32):
    """Custom type cpqSeBaseMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeBaseMem_Type.__name__ = "Integer32"
_CpqSeBaseMem_Object = MibScalar
cpqSeBaseMem = _CpqSeBaseMem_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 3, 1),
    _CpqSeBaseMem_Type()
)
cpqSeBaseMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeBaseMem.setStatus("mandatory")


class _CpqSeTotalMem_Type(Integer32):
    """Custom type cpqSeTotalMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSeTotalMem_Type.__name__ = "Integer32"
_CpqSeTotalMem_Object = MibScalar
cpqSeTotalMem = _CpqSeTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 3, 2),
    _CpqSeTotalMem_Type()
)
cpqSeTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeTotalMem.setStatus("mandatory")


class _CpqSeTotalMemMB_Type(Integer32):
    """Custom type cpqSeTotalMemMB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSeTotalMemMB_Type.__name__ = "Integer32"
_CpqSeTotalMemMB_Object = MibScalar
cpqSeTotalMemMB = _CpqSeTotalMemMB_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 3, 3),
    _CpqSeTotalMemMB_Type()
)
cpqSeTotalMemMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeTotalMemMB.setStatus("mandatory")
_CpqSeIsaCmos_ObjectIdentity = ObjectIdentity
cpqSeIsaCmos = _CpqSeIsaCmos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 4)
)


class _CpqSeIsaCmosRaw_Type(OctetString):
    """Custom type cpqSeIsaCmosRaw based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_CpqSeIsaCmosRaw_Type.__name__ = "OctetString"
_CpqSeIsaCmosRaw_Object = MibScalar
cpqSeIsaCmosRaw = _CpqSeIsaCmosRaw_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 4, 1),
    _CpqSeIsaCmosRaw_Type()
)
cpqSeIsaCmosRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeIsaCmosRaw.setStatus("mandatory")
_CpqSeEisaNvram_ObjectIdentity = ObjectIdentity
cpqSeEisaNvram = _CpqSeEisaNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5)
)
_CpqSeEisaSlotTable_Object = MibTable
cpqSeEisaSlotTable = _CpqSeEisaSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqSeEisaSlotTable.setStatus("mandatory")
_CpqSeEisaSlotEntry_Object = MibTableRow
cpqSeEisaSlotEntry = _CpqSeEisaSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 1, 1)
)
cpqSeEisaSlotEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeEisaSlotIndex"),
)
if mibBuilder.loadTexts:
    cpqSeEisaSlotEntry.setStatus("mandatory")


class _CpqSeEisaSlotIndex_Type(Integer32):
    """Custom type cpqSeEisaSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaSlotIndex_Type.__name__ = "Integer32"
_CpqSeEisaSlotIndex_Object = MibTableColumn
cpqSeEisaSlotIndex = _CpqSeEisaSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 1, 1, 1),
    _CpqSeEisaSlotIndex_Type()
)
cpqSeEisaSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaSlotIndex.setStatus("mandatory")


class _CpqSeEisaSlotRaw_Type(OctetString):
    """Custom type cpqSeEisaSlotRaw based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CpqSeEisaSlotRaw_Type.__name__ = "OctetString"
_CpqSeEisaSlotRaw_Object = MibTableColumn
cpqSeEisaSlotRaw = _CpqSeEisaSlotRaw_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 1, 1, 2),
    _CpqSeEisaSlotRaw_Type()
)
cpqSeEisaSlotRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaSlotRaw.setStatus("mandatory")


class _CpqSeEisaSlotBoardId_Type(DisplayString):
    """Custom type cpqSeEisaSlotBoardId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqSeEisaSlotBoardId_Type.__name__ = "DisplayString"
_CpqSeEisaSlotBoardId_Object = MibTableColumn
cpqSeEisaSlotBoardId = _CpqSeEisaSlotBoardId_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 1, 1, 3),
    _CpqSeEisaSlotBoardId_Type()
)
cpqSeEisaSlotBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaSlotBoardId.setStatus("mandatory")


class _CpqSeEisaSlotBoardName_Type(DisplayString):
    """Custom type cpqSeEisaSlotBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeEisaSlotBoardName_Type.__name__ = "DisplayString"
_CpqSeEisaSlotBoardName_Object = MibTableColumn
cpqSeEisaSlotBoardName = _CpqSeEisaSlotBoardName_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 1, 1, 4),
    _CpqSeEisaSlotBoardName_Type()
)
cpqSeEisaSlotBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaSlotBoardName.setStatus("mandatory")


class _CpqSeEisaSlotCfRev_Type(DisplayString):
    """Custom type cpqSeEisaSlotCfRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqSeEisaSlotCfRev_Type.__name__ = "DisplayString"
_CpqSeEisaSlotCfRev_Object = MibTableColumn
cpqSeEisaSlotCfRev = _CpqSeEisaSlotCfRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 1, 1, 5),
    _CpqSeEisaSlotCfRev_Type()
)
cpqSeEisaSlotCfRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaSlotCfRev.setStatus("mandatory")


class _CpqSeEisaSlotType_Type(Integer32):
    """Custom type cpqSeEisaSlotType based on Integer32"""
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
        *(("eisa32Bit", 4),
          ("eisaBusMaster32Bit", 5),
          ("isa16Bit", 3),
          ("isa8Bit", 2),
          ("other", 6),
          ("reserved", 7),
          ("reserved2", 8),
          ("unknown", 1))
    )


_CpqSeEisaSlotType_Type.__name__ = "Integer32"
_CpqSeEisaSlotType_Object = MibTableColumn
cpqSeEisaSlotType = _CpqSeEisaSlotType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 1, 1, 6),
    _CpqSeEisaSlotType_Type()
)
cpqSeEisaSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaSlotType.setStatus("mandatory")
_CpqSeEisaFunctTable_Object = MibTable
cpqSeEisaFunctTable = _CpqSeEisaFunctTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    cpqSeEisaFunctTable.setStatus("mandatory")
_CpqSeEisaFunctEntry_Object = MibTableRow
cpqSeEisaFunctEntry = _CpqSeEisaFunctEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 2, 1)
)
cpqSeEisaFunctEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeEisaFunctSlotIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaFunctIndex"),
)
if mibBuilder.loadTexts:
    cpqSeEisaFunctEntry.setStatus("mandatory")


class _CpqSeEisaFunctSlotIndex_Type(Integer32):
    """Custom type cpqSeEisaFunctSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaFunctSlotIndex_Type.__name__ = "Integer32"
_CpqSeEisaFunctSlotIndex_Object = MibTableColumn
cpqSeEisaFunctSlotIndex = _CpqSeEisaFunctSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 2, 1, 1),
    _CpqSeEisaFunctSlotIndex_Type()
)
cpqSeEisaFunctSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaFunctSlotIndex.setStatus("mandatory")


class _CpqSeEisaFunctIndex_Type(Integer32):
    """Custom type cpqSeEisaFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaFunctIndex_Type.__name__ = "Integer32"
_CpqSeEisaFunctIndex_Object = MibTableColumn
cpqSeEisaFunctIndex = _CpqSeEisaFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 2, 1, 2),
    _CpqSeEisaFunctIndex_Type()
)
cpqSeEisaFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaFunctIndex.setStatus("mandatory")


class _CpqSeEisaFunctStatus_Type(Integer32):
    """Custom type cpqSeEisaFunctStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_CpqSeEisaFunctStatus_Type.__name__ = "Integer32"
_CpqSeEisaFunctStatus_Object = MibTableColumn
cpqSeEisaFunctStatus = _CpqSeEisaFunctStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 2, 1, 3),
    _CpqSeEisaFunctStatus_Type()
)
cpqSeEisaFunctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaFunctStatus.setStatus("mandatory")


class _CpqSeEisaFunctType_Type(DisplayString):
    """Custom type cpqSeEisaFunctType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqSeEisaFunctType_Type.__name__ = "DisplayString"
_CpqSeEisaFunctType_Object = MibTableColumn
cpqSeEisaFunctType = _CpqSeEisaFunctType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 2, 1, 4),
    _CpqSeEisaFunctType_Type()
)
cpqSeEisaFunctType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaFunctType.setStatus("mandatory")


class _CpqSeEisaFunctCfgRev_Type(DisplayString):
    """Custom type cpqSeEisaFunctCfgRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqSeEisaFunctCfgRev_Type.__name__ = "DisplayString"
_CpqSeEisaFunctCfgRev_Object = MibTableColumn
cpqSeEisaFunctCfgRev = _CpqSeEisaFunctCfgRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 2, 1, 5),
    _CpqSeEisaFunctCfgRev_Type()
)
cpqSeEisaFunctCfgRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaFunctCfgRev.setStatus("mandatory")


class _CpqSeEisaFunctSels_Type(OctetString):
    """Custom type cpqSeEisaFunctSels based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_CpqSeEisaFunctSels_Type.__name__ = "OctetString"
_CpqSeEisaFunctSels_Object = MibTableColumn
cpqSeEisaFunctSels = _CpqSeEisaFunctSels_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 2, 1, 6),
    _CpqSeEisaFunctSels_Type()
)
cpqSeEisaFunctSels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaFunctSels.setStatus("mandatory")


class _CpqSeEisaFunctInfo_Type(Integer32):
    """Custom type cpqSeEisaFunctInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaFunctInfo_Type.__name__ = "Integer32"
_CpqSeEisaFunctInfo_Object = MibTableColumn
cpqSeEisaFunctInfo = _CpqSeEisaFunctInfo_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 2, 1, 7),
    _CpqSeEisaFunctInfo_Type()
)
cpqSeEisaFunctInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaFunctInfo.setStatus("mandatory")
_CpqSeEisaMemTable_Object = MibTable
cpqSeEisaMemTable = _CpqSeEisaMemTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    cpqSeEisaMemTable.setStatus("mandatory")
_CpqSeEisaMemEntry_Object = MibTableRow
cpqSeEisaMemEntry = _CpqSeEisaMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1)
)
cpqSeEisaMemEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeEisaMemSlotIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaMemFunctIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaMemAllocIndex"),
)
if mibBuilder.loadTexts:
    cpqSeEisaMemEntry.setStatus("mandatory")


class _CpqSeEisaMemSlotIndex_Type(Integer32):
    """Custom type cpqSeEisaMemSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaMemSlotIndex_Type.__name__ = "Integer32"
_CpqSeEisaMemSlotIndex_Object = MibTableColumn
cpqSeEisaMemSlotIndex = _CpqSeEisaMemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 1),
    _CpqSeEisaMemSlotIndex_Type()
)
cpqSeEisaMemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemSlotIndex.setStatus("mandatory")


class _CpqSeEisaMemFunctIndex_Type(Integer32):
    """Custom type cpqSeEisaMemFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaMemFunctIndex_Type.__name__ = "Integer32"
_CpqSeEisaMemFunctIndex_Object = MibTableColumn
cpqSeEisaMemFunctIndex = _CpqSeEisaMemFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 2),
    _CpqSeEisaMemFunctIndex_Type()
)
cpqSeEisaMemFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemFunctIndex.setStatus("mandatory")


class _CpqSeEisaMemAllocIndex_Type(Integer32):
    """Custom type cpqSeEisaMemAllocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaMemAllocIndex_Type.__name__ = "Integer32"
_CpqSeEisaMemAllocIndex_Object = MibTableColumn
cpqSeEisaMemAllocIndex = _CpqSeEisaMemAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 3),
    _CpqSeEisaMemAllocIndex_Type()
)
cpqSeEisaMemAllocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemAllocIndex.setStatus("mandatory")
_CpqSeEisaMemStartAddr_Type = Integer32
_CpqSeEisaMemStartAddr_Object = MibTableColumn
cpqSeEisaMemStartAddr = _CpqSeEisaMemStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 4),
    _CpqSeEisaMemStartAddr_Type()
)
cpqSeEisaMemStartAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemStartAddr.setStatus("mandatory")


class _CpqSeEisaMemSize_Type(Integer32):
    """Custom type cpqSeEisaMemSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSeEisaMemSize_Type.__name__ = "Integer32"
_CpqSeEisaMemSize_Object = MibTableColumn
cpqSeEisaMemSize = _CpqSeEisaMemSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 5),
    _CpqSeEisaMemSize_Type()
)
cpqSeEisaMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemSize.setStatus("mandatory")


class _CpqSeEisaMemShare_Type(Integer32):
    """Custom type cpqSeEisaMemShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonshareable", 1),
          ("shareable", 2))
    )


_CpqSeEisaMemShare_Type.__name__ = "Integer32"
_CpqSeEisaMemShare_Object = MibTableColumn
cpqSeEisaMemShare = _CpqSeEisaMemShare_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 6),
    _CpqSeEisaMemShare_Type()
)
cpqSeEisaMemShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemShare.setStatus("mandatory")


class _CpqSeEisaMemType_Type(Integer32):
    """Custom type cpqSeEisaMemType based on Integer32"""
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
        *(("expanded", 2),
          ("other", 4),
          ("systemBaseOrExtended", 1),
          ("virtual", 3))
    )


_CpqSeEisaMemType_Type.__name__ = "Integer32"
_CpqSeEisaMemType_Object = MibTableColumn
cpqSeEisaMemType = _CpqSeEisaMemType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 7),
    _CpqSeEisaMemType_Type()
)
cpqSeEisaMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemType.setStatus("mandatory")


class _CpqSeEisaMemCache_Type(Integer32):
    """Custom type cpqSeEisaMemCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notCached", 1),
          ("writeBackCached", 3),
          ("writeThroughCached", 2))
    )


_CpqSeEisaMemCache_Type.__name__ = "Integer32"
_CpqSeEisaMemCache_Object = MibTableColumn
cpqSeEisaMemCache = _CpqSeEisaMemCache_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 8),
    _CpqSeEisaMemCache_Type()
)
cpqSeEisaMemCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemCache.setStatus("mandatory")


class _CpqSeEisaMemAccess_Type(Integer32):
    """Custom type cpqSeEisaMemAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_CpqSeEisaMemAccess_Type.__name__ = "Integer32"
_CpqSeEisaMemAccess_Object = MibTableColumn
cpqSeEisaMemAccess = _CpqSeEisaMemAccess_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 9),
    _CpqSeEisaMemAccess_Type()
)
cpqSeEisaMemAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemAccess.setStatus("mandatory")


class _CpqSeEisaMemDecode_Type(Integer32):
    """Custom type cpqSeEisaMemDecode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CpqSeEisaMemDecode_Type.__name__ = "Integer32"
_CpqSeEisaMemDecode_Object = MibTableColumn
cpqSeEisaMemDecode = _CpqSeEisaMemDecode_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 10),
    _CpqSeEisaMemDecode_Type()
)
cpqSeEisaMemDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemDecode.setStatus("mandatory")


class _CpqSeEisaMemDataSize_Type(Integer32):
    """Custom type cpqSeEisaMemDataSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CpqSeEisaMemDataSize_Type.__name__ = "Integer32"
_CpqSeEisaMemDataSize_Object = MibTableColumn
cpqSeEisaMemDataSize = _CpqSeEisaMemDataSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 3, 1, 11),
    _CpqSeEisaMemDataSize_Type()
)
cpqSeEisaMemDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaMemDataSize.setStatus("mandatory")
_CpqSeEisaIntTable_Object = MibTable
cpqSeEisaIntTable = _CpqSeEisaIntTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    cpqSeEisaIntTable.setStatus("mandatory")
_CpqSeEisaIntEntry_Object = MibTableRow
cpqSeEisaIntEntry = _CpqSeEisaIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 4, 1)
)
cpqSeEisaIntEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeEisaIntSlotIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaIntFunctIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaIntAllocIndex"),
)
if mibBuilder.loadTexts:
    cpqSeEisaIntEntry.setStatus("mandatory")


class _CpqSeEisaIntSlotIndex_Type(Integer32):
    """Custom type cpqSeEisaIntSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaIntSlotIndex_Type.__name__ = "Integer32"
_CpqSeEisaIntSlotIndex_Object = MibTableColumn
cpqSeEisaIntSlotIndex = _CpqSeEisaIntSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 4, 1, 1),
    _CpqSeEisaIntSlotIndex_Type()
)
cpqSeEisaIntSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaIntSlotIndex.setStatus("mandatory")


class _CpqSeEisaIntFunctIndex_Type(Integer32):
    """Custom type cpqSeEisaIntFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaIntFunctIndex_Type.__name__ = "Integer32"
_CpqSeEisaIntFunctIndex_Object = MibTableColumn
cpqSeEisaIntFunctIndex = _CpqSeEisaIntFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 4, 1, 2),
    _CpqSeEisaIntFunctIndex_Type()
)
cpqSeEisaIntFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaIntFunctIndex.setStatus("mandatory")


class _CpqSeEisaIntAllocIndex_Type(Integer32):
    """Custom type cpqSeEisaIntAllocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaIntAllocIndex_Type.__name__ = "Integer32"
_CpqSeEisaIntAllocIndex_Object = MibTableColumn
cpqSeEisaIntAllocIndex = _CpqSeEisaIntAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 4, 1, 3),
    _CpqSeEisaIntAllocIndex_Type()
)
cpqSeEisaIntAllocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaIntAllocIndex.setStatus("mandatory")


class _CpqSeEisaIntNum_Type(Integer32):
    """Custom type cpqSeEisaIntNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeEisaIntNum_Type.__name__ = "Integer32"
_CpqSeEisaIntNum_Object = MibTableColumn
cpqSeEisaIntNum = _CpqSeEisaIntNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 4, 1, 4),
    _CpqSeEisaIntNum_Type()
)
cpqSeEisaIntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaIntNum.setStatus("mandatory")


class _CpqSeEisaIntShare_Type(Integer32):
    """Custom type cpqSeEisaIntShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonshareable", 1),
          ("shareable", 2))
    )


_CpqSeEisaIntShare_Type.__name__ = "Integer32"
_CpqSeEisaIntShare_Object = MibTableColumn
cpqSeEisaIntShare = _CpqSeEisaIntShare_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 4, 1, 5),
    _CpqSeEisaIntShare_Type()
)
cpqSeEisaIntShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaIntShare.setStatus("mandatory")


class _CpqSeEisaIntTrigger_Type(Integer32):
    """Custom type cpqSeEisaIntTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("edge", 1),
          ("level", 2))
    )


_CpqSeEisaIntTrigger_Type.__name__ = "Integer32"
_CpqSeEisaIntTrigger_Object = MibTableColumn
cpqSeEisaIntTrigger = _CpqSeEisaIntTrigger_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 4, 1, 6),
    _CpqSeEisaIntTrigger_Type()
)
cpqSeEisaIntTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaIntTrigger.setStatus("mandatory")
_CpqSeEisaDmaTable_Object = MibTable
cpqSeEisaDmaTable = _CpqSeEisaDmaTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    cpqSeEisaDmaTable.setStatus("mandatory")
_CpqSeEisaDmaEntry_Object = MibTableRow
cpqSeEisaDmaEntry = _CpqSeEisaDmaEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 5, 1)
)
cpqSeEisaDmaEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeEisaDmaSlotIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaDmaFunctIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaDmaAllocIndex"),
)
if mibBuilder.loadTexts:
    cpqSeEisaDmaEntry.setStatus("mandatory")


class _CpqSeEisaDmaSlotIndex_Type(Integer32):
    """Custom type cpqSeEisaDmaSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaDmaSlotIndex_Type.__name__ = "Integer32"
_CpqSeEisaDmaSlotIndex_Object = MibTableColumn
cpqSeEisaDmaSlotIndex = _CpqSeEisaDmaSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 5, 1, 1),
    _CpqSeEisaDmaSlotIndex_Type()
)
cpqSeEisaDmaSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaDmaSlotIndex.setStatus("mandatory")


class _CpqSeEisaDmaFunctIndex_Type(Integer32):
    """Custom type cpqSeEisaDmaFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaDmaFunctIndex_Type.__name__ = "Integer32"
_CpqSeEisaDmaFunctIndex_Object = MibTableColumn
cpqSeEisaDmaFunctIndex = _CpqSeEisaDmaFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 5, 1, 2),
    _CpqSeEisaDmaFunctIndex_Type()
)
cpqSeEisaDmaFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaDmaFunctIndex.setStatus("mandatory")


class _CpqSeEisaDmaAllocIndex_Type(Integer32):
    """Custom type cpqSeEisaDmaAllocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaDmaAllocIndex_Type.__name__ = "Integer32"
_CpqSeEisaDmaAllocIndex_Object = MibTableColumn
cpqSeEisaDmaAllocIndex = _CpqSeEisaDmaAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 5, 1, 3),
    _CpqSeEisaDmaAllocIndex_Type()
)
cpqSeEisaDmaAllocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaDmaAllocIndex.setStatus("mandatory")


class _CpqSeEisaDmaChannel_Type(Integer32):
    """Custom type cpqSeEisaDmaChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeEisaDmaChannel_Type.__name__ = "Integer32"
_CpqSeEisaDmaChannel_Object = MibTableColumn
cpqSeEisaDmaChannel = _CpqSeEisaDmaChannel_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 5, 1, 4),
    _CpqSeEisaDmaChannel_Type()
)
cpqSeEisaDmaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaDmaChannel.setStatus("mandatory")


class _CpqSeEisaDmaShare_Type(Integer32):
    """Custom type cpqSeEisaDmaShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonshareable", 1),
          ("shareable", 2))
    )


_CpqSeEisaDmaShare_Type.__name__ = "Integer32"
_CpqSeEisaDmaShare_Object = MibTableColumn
cpqSeEisaDmaShare = _CpqSeEisaDmaShare_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 5, 1, 5),
    _CpqSeEisaDmaShare_Type()
)
cpqSeEisaDmaShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaDmaShare.setStatus("mandatory")


class _CpqSeEisaDmaTiming_Type(Integer32):
    """Custom type cpqSeEisaDmaTiming based on Integer32"""
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
        *(("burstTypeC", 4),
          ("isaTiming", 1),
          ("typeA", 2),
          ("typeB", 3))
    )


_CpqSeEisaDmaTiming_Type.__name__ = "Integer32"
_CpqSeEisaDmaTiming_Object = MibTableColumn
cpqSeEisaDmaTiming = _CpqSeEisaDmaTiming_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 5, 1, 6),
    _CpqSeEisaDmaTiming_Type()
)
cpqSeEisaDmaTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaDmaTiming.setStatus("mandatory")


class _CpqSeEisaDmaXfer_Type(Integer32):
    """Custom type cpqSeEisaDmaXfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeEisaDmaXfer_Type.__name__ = "Integer32"
_CpqSeEisaDmaXfer_Object = MibTableColumn
cpqSeEisaDmaXfer = _CpqSeEisaDmaXfer_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 5, 1, 7),
    _CpqSeEisaDmaXfer_Type()
)
cpqSeEisaDmaXfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaDmaXfer.setStatus("mandatory")


class _CpqSeEisaDmaXferCount_Type(Integer32):
    """Custom type cpqSeEisaDmaXferCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byte", 1),
          ("word", 2))
    )


_CpqSeEisaDmaXferCount_Type.__name__ = "Integer32"
_CpqSeEisaDmaXferCount_Object = MibTableColumn
cpqSeEisaDmaXferCount = _CpqSeEisaDmaXferCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 5, 1, 8),
    _CpqSeEisaDmaXferCount_Type()
)
cpqSeEisaDmaXferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaDmaXferCount.setStatus("mandatory")
_CpqSeEisaPortTable_Object = MibTable
cpqSeEisaPortTable = _CpqSeEisaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 6)
)
if mibBuilder.loadTexts:
    cpqSeEisaPortTable.setStatus("mandatory")
_CpqSeEisaPortEntry_Object = MibTableRow
cpqSeEisaPortEntry = _CpqSeEisaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 6, 1)
)
cpqSeEisaPortEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeEisaPortSlotIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaPortFunctIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaPortAllocIndex"),
)
if mibBuilder.loadTexts:
    cpqSeEisaPortEntry.setStatus("mandatory")


class _CpqSeEisaPortSlotIndex_Type(Integer32):
    """Custom type cpqSeEisaPortSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaPortSlotIndex_Type.__name__ = "Integer32"
_CpqSeEisaPortSlotIndex_Object = MibTableColumn
cpqSeEisaPortSlotIndex = _CpqSeEisaPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 6, 1, 1),
    _CpqSeEisaPortSlotIndex_Type()
)
cpqSeEisaPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaPortSlotIndex.setStatus("mandatory")


class _CpqSeEisaPortFunctIndex_Type(Integer32):
    """Custom type cpqSeEisaPortFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaPortFunctIndex_Type.__name__ = "Integer32"
_CpqSeEisaPortFunctIndex_Object = MibTableColumn
cpqSeEisaPortFunctIndex = _CpqSeEisaPortFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 6, 1, 2),
    _CpqSeEisaPortFunctIndex_Type()
)
cpqSeEisaPortFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaPortFunctIndex.setStatus("mandatory")


class _CpqSeEisaPortAllocIndex_Type(Integer32):
    """Custom type cpqSeEisaPortAllocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaPortAllocIndex_Type.__name__ = "Integer32"
_CpqSeEisaPortAllocIndex_Object = MibTableColumn
cpqSeEisaPortAllocIndex = _CpqSeEisaPortAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 6, 1, 3),
    _CpqSeEisaPortAllocIndex_Type()
)
cpqSeEisaPortAllocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaPortAllocIndex.setStatus("mandatory")
_CpqSeEisaPortAddr_Type = Integer32
_CpqSeEisaPortAddr_Object = MibTableColumn
cpqSeEisaPortAddr = _CpqSeEisaPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 6, 1, 4),
    _CpqSeEisaPortAddr_Type()
)
cpqSeEisaPortAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaPortAddr.setStatus("mandatory")


class _CpqSeEisaPortShare_Type(Integer32):
    """Custom type cpqSeEisaPortShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonshareable", 1),
          ("shareable", 2))
    )


_CpqSeEisaPortShare_Type.__name__ = "Integer32"
_CpqSeEisaPortShare_Object = MibTableColumn
cpqSeEisaPortShare = _CpqSeEisaPortShare_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 6, 1, 5),
    _CpqSeEisaPortShare_Type()
)
cpqSeEisaPortShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaPortShare.setStatus("mandatory")


class _CpqSeEisaPortSize_Type(Integer32):
    """Custom type cpqSeEisaPortSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeEisaPortSize_Type.__name__ = "Integer32"
_CpqSeEisaPortSize_Object = MibTableColumn
cpqSeEisaPortSize = _CpqSeEisaPortSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 6, 1, 6),
    _CpqSeEisaPortSize_Type()
)
cpqSeEisaPortSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaPortSize.setStatus("mandatory")
_CpqSeEisaFreeFormTable_Object = MibTable
cpqSeEisaFreeFormTable = _CpqSeEisaFreeFormTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 7)
)
if mibBuilder.loadTexts:
    cpqSeEisaFreeFormTable.setStatus("mandatory")
_CpqSeEisaFreeFormEntry_Object = MibTableRow
cpqSeEisaFreeFormEntry = _CpqSeEisaFreeFormEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 7, 1)
)
cpqSeEisaFreeFormEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeEisaFreeFormSlotIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaFreeFormFunctIndex"),
)
if mibBuilder.loadTexts:
    cpqSeEisaFreeFormEntry.setStatus("mandatory")


class _CpqSeEisaFreeFormSlotIndex_Type(Integer32):
    """Custom type cpqSeEisaFreeFormSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaFreeFormSlotIndex_Type.__name__ = "Integer32"
_CpqSeEisaFreeFormSlotIndex_Object = MibTableColumn
cpqSeEisaFreeFormSlotIndex = _CpqSeEisaFreeFormSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 7, 1, 1),
    _CpqSeEisaFreeFormSlotIndex_Type()
)
cpqSeEisaFreeFormSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaFreeFormSlotIndex.setStatus("mandatory")


class _CpqSeEisaFreeFormFunctIndex_Type(Integer32):
    """Custom type cpqSeEisaFreeFormFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaFreeFormFunctIndex_Type.__name__ = "Integer32"
_CpqSeEisaFreeFormFunctIndex_Object = MibTableColumn
cpqSeEisaFreeFormFunctIndex = _CpqSeEisaFreeFormFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 7, 1, 2),
    _CpqSeEisaFreeFormFunctIndex_Type()
)
cpqSeEisaFreeFormFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaFreeFormFunctIndex.setStatus("mandatory")


class _CpqSeEisaFreeFormValue_Type(OctetString):
    """Custom type cpqSeEisaFreeFormValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 205),
    )


_CpqSeEisaFreeFormValue_Type.__name__ = "OctetString"
_CpqSeEisaFreeFormValue_Object = MibTableColumn
cpqSeEisaFreeFormValue = _CpqSeEisaFreeFormValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 7, 1, 3),
    _CpqSeEisaFreeFormValue_Type()
)
cpqSeEisaFreeFormValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaFreeFormValue.setStatus("mandatory")
_CpqSeEisaInitTable_Object = MibTable
cpqSeEisaInitTable = _CpqSeEisaInitTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 8)
)
if mibBuilder.loadTexts:
    cpqSeEisaInitTable.setStatus("mandatory")
_CpqSeEisaInitEntry_Object = MibTableRow
cpqSeEisaInitEntry = _CpqSeEisaInitEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 8, 1)
)
cpqSeEisaInitEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeEisaInitSlotIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaInitFunctIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSeEisaInitAllocIndex"),
)
if mibBuilder.loadTexts:
    cpqSeEisaInitEntry.setStatus("mandatory")


class _CpqSeEisaInitSlotIndex_Type(Integer32):
    """Custom type cpqSeEisaInitSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaInitSlotIndex_Type.__name__ = "Integer32"
_CpqSeEisaInitSlotIndex_Object = MibTableColumn
cpqSeEisaInitSlotIndex = _CpqSeEisaInitSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 8, 1, 1),
    _CpqSeEisaInitSlotIndex_Type()
)
cpqSeEisaInitSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaInitSlotIndex.setStatus("mandatory")


class _CpqSeEisaInitFunctIndex_Type(Integer32):
    """Custom type cpqSeEisaInitFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaInitFunctIndex_Type.__name__ = "Integer32"
_CpqSeEisaInitFunctIndex_Object = MibTableColumn
cpqSeEisaInitFunctIndex = _CpqSeEisaInitFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 8, 1, 2),
    _CpqSeEisaInitFunctIndex_Type()
)
cpqSeEisaInitFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaInitFunctIndex.setStatus("mandatory")


class _CpqSeEisaInitAllocIndex_Type(Integer32):
    """Custom type cpqSeEisaInitAllocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeEisaInitAllocIndex_Type.__name__ = "Integer32"
_CpqSeEisaInitAllocIndex_Object = MibTableColumn
cpqSeEisaInitAllocIndex = _CpqSeEisaInitAllocIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 8, 1, 3),
    _CpqSeEisaInitAllocIndex_Type()
)
cpqSeEisaInitAllocIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaInitAllocIndex.setStatus("mandatory")


class _CpqSeEisaInitUseMask_Type(Integer32):
    """Custom type cpqSeEisaInitUseMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useValueAndMask", 2),
          ("useValueOnly", 1))
    )


_CpqSeEisaInitUseMask_Type.__name__ = "Integer32"
_CpqSeEisaInitUseMask_Object = MibTableColumn
cpqSeEisaInitUseMask = _CpqSeEisaInitUseMask_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 8, 1, 4),
    _CpqSeEisaInitUseMask_Type()
)
cpqSeEisaInitUseMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaInitUseMask.setStatus("mandatory")


class _CpqSeEisaInitAccess_Type(Integer32):
    """Custom type cpqSeEisaInitAccess based on Integer32"""
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
        *(("eightBitAddress", 2),
          ("other", 1),
          ("sixteenBitAddress", 3),
          ("thirtyTwoBitAddress", 4))
    )


_CpqSeEisaInitAccess_Type.__name__ = "Integer32"
_CpqSeEisaInitAccess_Object = MibTableColumn
cpqSeEisaInitAccess = _CpqSeEisaInitAccess_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 8, 1, 5),
    _CpqSeEisaInitAccess_Type()
)
cpqSeEisaInitAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaInitAccess.setStatus("mandatory")
_CpqSeEisaInitAddr_Type = Integer32
_CpqSeEisaInitAddr_Object = MibTableColumn
cpqSeEisaInitAddr = _CpqSeEisaInitAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 8, 1, 6),
    _CpqSeEisaInitAddr_Type()
)
cpqSeEisaInitAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaInitAddr.setStatus("mandatory")
_CpqSeEisaInitValue_Type = Integer32
_CpqSeEisaInitValue_Object = MibTableColumn
cpqSeEisaInitValue = _CpqSeEisaInitValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 8, 1, 7),
    _CpqSeEisaInitValue_Type()
)
cpqSeEisaInitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaInitValue.setStatus("mandatory")
_CpqSeEisaInitMask_Type = Integer32
_CpqSeEisaInitMask_Object = MibTableColumn
cpqSeEisaInitMask = _CpqSeEisaInitMask_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 5, 8, 1, 8),
    _CpqSeEisaInitMask_Type()
)
cpqSeEisaInitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeEisaInitMask.setStatus("mandatory")
_CpqSeRom_ObjectIdentity = ObjectIdentity
cpqSeRom = _CpqSeRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6)
)


class _CpqSeSysRomVer_Type(DisplayString):
    """Custom type cpqSeSysRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeSysRomVer_Type.__name__ = "DisplayString"
_CpqSeSysRomVer_Object = MibScalar
cpqSeSysRomVer = _CpqSeSysRomVer_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 1),
    _CpqSeSysRomVer_Type()
)
cpqSeSysRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeSysRomVer.setStatus("mandatory")
_CpqSeOptRomTable_Object = MibTable
cpqSeOptRomTable = _CpqSeOptRomTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    cpqSeOptRomTable.setStatus("mandatory")
_CpqSeOptRomEntry_Object = MibTableRow
cpqSeOptRomEntry = _CpqSeOptRomEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 2, 1)
)
cpqSeOptRomEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeOptRomAddrIndex"),
)
if mibBuilder.loadTexts:
    cpqSeOptRomEntry.setStatus("mandatory")


class _CpqSeOptRomAddrIndex_Type(Integer32):
    """Custom type cpqSeOptRomAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpqSeOptRomAddrIndex_Type.__name__ = "Integer32"
_CpqSeOptRomAddrIndex_Object = MibTableColumn
cpqSeOptRomAddrIndex = _CpqSeOptRomAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 2, 1, 1),
    _CpqSeOptRomAddrIndex_Type()
)
cpqSeOptRomAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeOptRomAddrIndex.setStatus("mandatory")


class _CpqSeOptRomSize_Type(Integer32):
    """Custom type cpqSeOptRomSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSeOptRomSize_Type.__name__ = "Integer32"
_CpqSeOptRomSize_Object = MibTableColumn
cpqSeOptRomSize = _CpqSeOptRomSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 2, 1, 2),
    _CpqSeOptRomSize_Type()
)
cpqSeOptRomSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeOptRomSize.setStatus("mandatory")


class _CpqSeBiosRomDataRaw_Type(OctetString):
    """Custom type cpqSeBiosRomDataRaw based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_CpqSeBiosRomDataRaw_Type.__name__ = "OctetString"
_CpqSeBiosRomDataRaw_Object = MibScalar
cpqSeBiosRomDataRaw = _CpqSeBiosRomDataRaw_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 3),
    _CpqSeBiosRomDataRaw_Type()
)
cpqSeBiosRomDataRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeBiosRomDataRaw.setStatus("mandatory")


class _CpqSeRedundantSysRomVer_Type(DisplayString):
    """Custom type cpqSeRedundantSysRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeRedundantSysRomVer_Type.__name__ = "DisplayString"
_CpqSeRedundantSysRomVer_Object = MibScalar
cpqSeRedundantSysRomVer = _CpqSeRedundantSysRomVer_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 4),
    _CpqSeRedundantSysRomVer_Type()
)
cpqSeRedundantSysRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeRedundantSysRomVer.setStatus("mandatory")


class _CpqSeSmbiosVer_Type(DisplayString):
    """Custom type cpqSeSmbiosVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeSmbiosVer_Type.__name__ = "DisplayString"
_CpqSeSmbiosVer_Object = MibScalar
cpqSeSmbiosVer = _CpqSeSmbiosVer_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 5),
    _CpqSeSmbiosVer_Type()
)
cpqSeSmbiosVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeSmbiosVer.setStatus("mandatory")


class _CpqSeMPFwVer_Type(DisplayString):
    """Custom type cpqSeMPFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeMPFwVer_Type.__name__ = "DisplayString"
_CpqSeMPFwVer_Object = MibScalar
cpqSeMPFwVer = _CpqSeMPFwVer_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 6),
    _CpqSeMPFwVer_Type()
)
cpqSeMPFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeMPFwVer.setStatus("optional")


class _CpqSeBMCFwVer_Type(DisplayString):
    """Custom type cpqSeBMCFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeBMCFwVer_Type.__name__ = "DisplayString"
_CpqSeBMCFwVer_Object = MibScalar
cpqSeBMCFwVer = _CpqSeBMCFwVer_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 7),
    _CpqSeBMCFwVer_Type()
)
cpqSeBMCFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeBMCFwVer.setStatus("optional")


class _CpqSeHPVMFwVer_Type(DisplayString):
    """Custom type cpqSeHPVMFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeHPVMFwVer_Type.__name__ = "DisplayString"
_CpqSeHPVMFwVer_Object = MibScalar
cpqSeHPVMFwVer = _CpqSeHPVMFwVer_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 6, 8),
    _CpqSeHPVMFwVer_Type()
)
cpqSeHPVMFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeHPVMFwVer.setStatus("optional")
_CpqSeKeyboard_ObjectIdentity = ObjectIdentity
cpqSeKeyboard = _CpqSeKeyboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 7)
)


class _CpqSeKeyboardDesc_Type(DisplayString):
    """Custom type cpqSeKeyboardDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeKeyboardDesc_Type.__name__ = "DisplayString"
_CpqSeKeyboardDesc_Object = MibScalar
cpqSeKeyboardDesc = _CpqSeKeyboardDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 7, 1),
    _CpqSeKeyboardDesc_Type()
)
cpqSeKeyboardDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeKeyboardDesc.setStatus("mandatory")
_CpqSeVideo_ObjectIdentity = ObjectIdentity
cpqSeVideo = _CpqSeVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 8)
)


class _CpqSeVideoDesc_Type(DisplayString):
    """Custom type cpqSeVideoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeVideoDesc_Type.__name__ = "DisplayString"
_CpqSeVideoDesc_Object = MibScalar
cpqSeVideoDesc = _CpqSeVideoDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 8, 1),
    _CpqSeVideoDesc_Type()
)
cpqSeVideoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeVideoDesc.setStatus("mandatory")
_CpqSeSerialPort_ObjectIdentity = ObjectIdentity
cpqSeSerialPort = _CpqSeSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 9)
)
_CpqSeSerialPortTable_Object = MibTable
cpqSeSerialPortTable = _CpqSeSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    cpqSeSerialPortTable.setStatus("mandatory")
_CpqSeSerialPortEntry_Object = MibTableRow
cpqSeSerialPortEntry = _CpqSeSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 9, 1, 1)
)
cpqSeSerialPortEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeSerialPortIndex"),
)
if mibBuilder.loadTexts:
    cpqSeSerialPortEntry.setStatus("mandatory")


class _CpqSeSerialPortIndex_Type(Integer32):
    """Custom type cpqSeSerialPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeSerialPortIndex_Type.__name__ = "Integer32"
_CpqSeSerialPortIndex_Object = MibTableColumn
cpqSeSerialPortIndex = _CpqSeSerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 9, 1, 1, 1),
    _CpqSeSerialPortIndex_Type()
)
cpqSeSerialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeSerialPortIndex.setStatus("mandatory")
_CpqSeSerialPortAddr_Type = Integer32
_CpqSeSerialPortAddr_Object = MibTableColumn
cpqSeSerialPortAddr = _CpqSeSerialPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 9, 1, 1, 2),
    _CpqSeSerialPortAddr_Type()
)
cpqSeSerialPortAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeSerialPortAddr.setStatus("mandatory")


class _CpqSeSerialPortDesc_Type(DisplayString):
    """Custom type cpqSeSerialPortDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeSerialPortDesc_Type.__name__ = "DisplayString"
_CpqSeSerialPortDesc_Object = MibTableColumn
cpqSeSerialPortDesc = _CpqSeSerialPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 9, 1, 1, 3),
    _CpqSeSerialPortDesc_Type()
)
cpqSeSerialPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeSerialPortDesc.setStatus("mandatory")


class _CpqSeSerialPortHwLocation_Type(DisplayString):
    """Custom type cpqSeSerialPortHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeSerialPortHwLocation_Type.__name__ = "DisplayString"
_CpqSeSerialPortHwLocation_Object = MibTableColumn
cpqSeSerialPortHwLocation = _CpqSeSerialPortHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 9, 1, 1, 4),
    _CpqSeSerialPortHwLocation_Type()
)
cpqSeSerialPortHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeSerialPortHwLocation.setStatus("optional")
_CpqSeParallelPort_ObjectIdentity = ObjectIdentity
cpqSeParallelPort = _CpqSeParallelPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 10)
)
_CpqSeParallelPortTable_Object = MibTable
cpqSeParallelPortTable = _CpqSeParallelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    cpqSeParallelPortTable.setStatus("mandatory")
_CpqSeParallelPortEntry_Object = MibTableRow
cpqSeParallelPortEntry = _CpqSeParallelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 10, 1, 1)
)
cpqSeParallelPortEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeParallelPortIndex"),
)
if mibBuilder.loadTexts:
    cpqSeParallelPortEntry.setStatus("mandatory")


class _CpqSeParallelPortIndex_Type(Integer32):
    """Custom type cpqSeParallelPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeParallelPortIndex_Type.__name__ = "Integer32"
_CpqSeParallelPortIndex_Object = MibTableColumn
cpqSeParallelPortIndex = _CpqSeParallelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 10, 1, 1, 1),
    _CpqSeParallelPortIndex_Type()
)
cpqSeParallelPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeParallelPortIndex.setStatus("mandatory")
_CpqSeParallelPortAddr_Type = Integer32
_CpqSeParallelPortAddr_Object = MibTableColumn
cpqSeParallelPortAddr = _CpqSeParallelPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 10, 1, 1, 2),
    _CpqSeParallelPortAddr_Type()
)
cpqSeParallelPortAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeParallelPortAddr.setStatus("mandatory")


class _CpqSeParallelPortDesc_Type(DisplayString):
    """Custom type cpqSeParallelPortDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeParallelPortDesc_Type.__name__ = "DisplayString"
_CpqSeParallelPortDesc_Object = MibTableColumn
cpqSeParallelPortDesc = _CpqSeParallelPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 10, 1, 1, 3),
    _CpqSeParallelPortDesc_Type()
)
cpqSeParallelPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeParallelPortDesc.setStatus("mandatory")


class _CpqSeParrallelPortHwLocation_Type(DisplayString):
    """Custom type cpqSeParrallelPortHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeParrallelPortHwLocation_Type.__name__ = "DisplayString"
_CpqSeParrallelPortHwLocation_Object = MibTableColumn
cpqSeParrallelPortHwLocation = _CpqSeParrallelPortHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 10, 1, 1, 4),
    _CpqSeParrallelPortHwLocation_Type()
)
cpqSeParrallelPortHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeParrallelPortHwLocation.setStatus("optional")
_CpqSeFloppyDisk_ObjectIdentity = ObjectIdentity
cpqSeFloppyDisk = _CpqSeFloppyDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 11)
)
_CpqSeFloppyDiskTable_Object = MibTable
cpqSeFloppyDiskTable = _CpqSeFloppyDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    cpqSeFloppyDiskTable.setStatus("mandatory")
_CpqSeFloppyDiskEntry_Object = MibTableRow
cpqSeFloppyDiskEntry = _CpqSeFloppyDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 11, 1, 1)
)
cpqSeFloppyDiskEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeFloppyDiskIndex"),
)
if mibBuilder.loadTexts:
    cpqSeFloppyDiskEntry.setStatus("mandatory")


class _CpqSeFloppyDiskIndex_Type(Integer32):
    """Custom type cpqSeFloppyDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeFloppyDiskIndex_Type.__name__ = "Integer32"
_CpqSeFloppyDiskIndex_Object = MibTableColumn
cpqSeFloppyDiskIndex = _CpqSeFloppyDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 11, 1, 1, 1),
    _CpqSeFloppyDiskIndex_Type()
)
cpqSeFloppyDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFloppyDiskIndex.setStatus("mandatory")


class _CpqSeFloppyDiskType_Type(Integer32):
    """Custom type cpqSeFloppyDiskType based on Integer32"""
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
        *(("drive1200k", 3),
          ("drive120mb", 6),
          ("drive1440k", 5),
          ("drive360k", 2),
          ("drive720k", 4),
          ("other", 1))
    )


_CpqSeFloppyDiskType_Type.__name__ = "Integer32"
_CpqSeFloppyDiskType_Object = MibTableColumn
cpqSeFloppyDiskType = _CpqSeFloppyDiskType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 11, 1, 1, 2),
    _CpqSeFloppyDiskType_Type()
)
cpqSeFloppyDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFloppyDiskType.setStatus("mandatory")


class _CpqSeFloppyDiskHwLocation_Type(DisplayString):
    """Custom type cpqSeFloppyDiskHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeFloppyDiskHwLocation_Type.__name__ = "DisplayString"
_CpqSeFloppyDiskHwLocation_Object = MibTableColumn
cpqSeFloppyDiskHwLocation = _CpqSeFloppyDiskHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 11, 1, 1, 3),
    _CpqSeFloppyDiskHwLocation_Type()
)
cpqSeFloppyDiskHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFloppyDiskHwLocation.setStatus("optional")
_CpqSeFixedDisk_ObjectIdentity = ObjectIdentity
cpqSeFixedDisk = _CpqSeFixedDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 12)
)
_CpqSeFixedDiskTable_Object = MibTable
cpqSeFixedDiskTable = _CpqSeFixedDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    cpqSeFixedDiskTable.setStatus("mandatory")
_CpqSeFixedDiskEntry_Object = MibTableRow
cpqSeFixedDiskEntry = _CpqSeFixedDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 12, 1, 1)
)
cpqSeFixedDiskEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeFixedDiskIndex"),
)
if mibBuilder.loadTexts:
    cpqSeFixedDiskEntry.setStatus("mandatory")


class _CpqSeFixedDiskIndex_Type(Integer32):
    """Custom type cpqSeFixedDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeFixedDiskIndex_Type.__name__ = "Integer32"
_CpqSeFixedDiskIndex_Object = MibTableColumn
cpqSeFixedDiskIndex = _CpqSeFixedDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 12, 1, 1, 1),
    _CpqSeFixedDiskIndex_Type()
)
cpqSeFixedDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFixedDiskIndex.setStatus("mandatory")


class _CpqSeFixedDiskType_Type(Integer32):
    """Custom type cpqSeFixedDiskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSeFixedDiskType_Type.__name__ = "Integer32"
_CpqSeFixedDiskType_Object = MibTableColumn
cpqSeFixedDiskType = _CpqSeFixedDiskType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 12, 1, 1, 2),
    _CpqSeFixedDiskType_Type()
)
cpqSeFixedDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFixedDiskType.setStatus("mandatory")


class _CpqSeFixedDiskCyls_Type(Integer32):
    """Custom type cpqSeFixedDiskCyls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSeFixedDiskCyls_Type.__name__ = "Integer32"
_CpqSeFixedDiskCyls_Object = MibTableColumn
cpqSeFixedDiskCyls = _CpqSeFixedDiskCyls_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 12, 1, 1, 3),
    _CpqSeFixedDiskCyls_Type()
)
cpqSeFixedDiskCyls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFixedDiskCyls.setStatus("mandatory")


class _CpqSeFixedDiskHeads_Type(Integer32):
    """Custom type cpqSeFixedDiskHeads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSeFixedDiskHeads_Type.__name__ = "Integer32"
_CpqSeFixedDiskHeads_Object = MibTableColumn
cpqSeFixedDiskHeads = _CpqSeFixedDiskHeads_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 12, 1, 1, 4),
    _CpqSeFixedDiskHeads_Type()
)
cpqSeFixedDiskHeads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFixedDiskHeads.setStatus("mandatory")


class _CpqSeFixedDiskSectors_Type(Integer32):
    """Custom type cpqSeFixedDiskSectors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSeFixedDiskSectors_Type.__name__ = "Integer32"
_CpqSeFixedDiskSectors_Object = MibTableColumn
cpqSeFixedDiskSectors = _CpqSeFixedDiskSectors_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 12, 1, 1, 5),
    _CpqSeFixedDiskSectors_Type()
)
cpqSeFixedDiskSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFixedDiskSectors.setStatus("mandatory")


class _CpqSeFixedDiskCapacity_Type(Integer32):
    """Custom type cpqSeFixedDiskCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSeFixedDiskCapacity_Type.__name__ = "Integer32"
_CpqSeFixedDiskCapacity_Object = MibTableColumn
cpqSeFixedDiskCapacity = _CpqSeFixedDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 12, 1, 1, 6),
    _CpqSeFixedDiskCapacity_Type()
)
cpqSeFixedDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFixedDiskCapacity.setStatus("mandatory")


class _CpqSeFixedDiskHwLocation_Type(DisplayString):
    """Custom type cpqSeFixedDiskHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeFixedDiskHwLocation_Type.__name__ = "DisplayString"
_CpqSeFixedDiskHwLocation_Object = MibTableColumn
cpqSeFixedDiskHwLocation = _CpqSeFixedDiskHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 12, 1, 1, 7),
    _CpqSeFixedDiskHwLocation_Type()
)
cpqSeFixedDiskHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeFixedDiskHwLocation.setStatus("optional")
_CpqSePci_ObjectIdentity = ObjectIdentity
cpqSePci = _CpqSePci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13)
)
_CpqSePciSlotTable_Object = MibTable
cpqSePciSlotTable = _CpqSePciSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    cpqSePciSlotTable.setStatus("mandatory")
_CpqSePciSlotEntry_Object = MibTableRow
cpqSePciSlotEntry = _CpqSePciSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1)
)
cpqSePciSlotEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSePciSlotBusNumberIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSePciSlotDeviceNumberIndex"),
)
if mibBuilder.loadTexts:
    cpqSePciSlotEntry.setStatus("mandatory")
_CpqSePciSlotBusNumberIndex_Type = Integer32
_CpqSePciSlotBusNumberIndex_Object = MibTableColumn
cpqSePciSlotBusNumberIndex = _CpqSePciSlotBusNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 1),
    _CpqSePciSlotBusNumberIndex_Type()
)
cpqSePciSlotBusNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotBusNumberIndex.setStatus("mandatory")


class _CpqSePciSlotDeviceNumberIndex_Type(Integer32):
    """Custom type cpqSePciSlotDeviceNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSePciSlotDeviceNumberIndex_Type.__name__ = "Integer32"
_CpqSePciSlotDeviceNumberIndex_Object = MibTableColumn
cpqSePciSlotDeviceNumberIndex = _CpqSePciSlotDeviceNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 2),
    _CpqSePciSlotDeviceNumberIndex_Type()
)
cpqSePciSlotDeviceNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotDeviceNumberIndex.setStatus("mandatory")


class _CpqSePciPhysSlot_Type(Integer32):
    """Custom type cpqSePciPhysSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSePciPhysSlot_Type.__name__ = "Integer32"
_CpqSePciPhysSlot_Object = MibTableColumn
cpqSePciPhysSlot = _CpqSePciPhysSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 3),
    _CpqSePciPhysSlot_Type()
)
cpqSePciPhysSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciPhysSlot.setStatus("mandatory")


class _CpqSePciSlotSubSystemID_Type(OctetString):
    """Custom type cpqSePciSlotSubSystemID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_CpqSePciSlotSubSystemID_Type.__name__ = "OctetString"
_CpqSePciSlotSubSystemID_Object = MibTableColumn
cpqSePciSlotSubSystemID = _CpqSePciSlotSubSystemID_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 4),
    _CpqSePciSlotSubSystemID_Type()
)
cpqSePciSlotSubSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotSubSystemID.setStatus("mandatory")


class _CpqSePciSlotBoardName_Type(DisplayString):
    """Custom type cpqSePciSlotBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSePciSlotBoardName_Type.__name__ = "DisplayString"
_CpqSePciSlotBoardName_Object = MibTableColumn
cpqSePciSlotBoardName = _CpqSePciSlotBoardName_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 5),
    _CpqSePciSlotBoardName_Type()
)
cpqSePciSlotBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotBoardName.setStatus("mandatory")


class _CpqSePciSlotWidth_Type(Integer32):
    """Custom type cpqSePciSlotWidth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("oneTwentyEightBit", 5),
          ("other", 1),
          ("sixtyFourBit", 4),
          ("thirtyTwoBit", 3),
          ("unknown", 2),
          ("x1", 6),
          ("x12", 10),
          ("x16", 11),
          ("x2", 7),
          ("x32", 12),
          ("x4", 8),
          ("x8", 9))
    )


_CpqSePciSlotWidth_Type.__name__ = "Integer32"
_CpqSePciSlotWidth_Object = MibTableColumn
cpqSePciSlotWidth = _CpqSePciSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 6),
    _CpqSePciSlotWidth_Type()
)
cpqSePciSlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotWidth.setStatus("mandatory")


class _CpqSePciSlotSpeed_Type(Integer32):
    """Custom type cpqSePciSlotSpeed based on Integer32"""
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
        *(("other", 1),
          ("sixtySixMHz", 4),
          ("thirtyThreeMHz", 3),
          ("unknown", 2))
    )


_CpqSePciSlotSpeed_Type.__name__ = "Integer32"
_CpqSePciSlotSpeed_Object = MibTableColumn
cpqSePciSlotSpeed = _CpqSePciSlotSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 7),
    _CpqSePciSlotSpeed_Type()
)
cpqSePciSlotSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotSpeed.setStatus("deprecated")
_CpqSePciSlotExtendedInfo_Type = Integer32
_CpqSePciSlotExtendedInfo_Object = MibTableColumn
cpqSePciSlotExtendedInfo = _CpqSePciSlotExtendedInfo_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 8),
    _CpqSePciSlotExtendedInfo_Type()
)
cpqSePciSlotExtendedInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotExtendedInfo.setStatus("mandatory")


class _CpqSePciSlotType_Type(Integer32):
    """Custom type cpqSePciSlotType based on Integer32"""
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
        *(("other", 1),
          ("pci", 3),
          ("pci66", 4),
          ("pciexpress", 6),
          ("pcix", 5),
          ("unknown", 2))
    )


_CpqSePciSlotType_Type.__name__ = "Integer32"
_CpqSePciSlotType_Object = MibTableColumn
cpqSePciSlotType = _CpqSePciSlotType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 9),
    _CpqSePciSlotType_Type()
)
cpqSePciSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotType.setStatus("mandatory")


class _CpqSePciSlotCurrentMode_Type(Integer32):
    """Custom type cpqSePciSlotCurrentMode based on Integer32"""
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
        *(("other", 1),
          ("pci", 3),
          ("pci66", 4),
          ("pcix", 5),
          ("unknown", 2))
    )


_CpqSePciSlotCurrentMode_Type.__name__ = "Integer32"
_CpqSePciSlotCurrentMode_Object = MibTableColumn
cpqSePciSlotCurrentMode = _CpqSePciSlotCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 10),
    _CpqSePciSlotCurrentMode_Type()
)
cpqSePciSlotCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotCurrentMode.setStatus("mandatory")
_CpqSePciMaxSlotSpeed_Type = Integer32
_CpqSePciMaxSlotSpeed_Object = MibTableColumn
cpqSePciMaxSlotSpeed = _CpqSePciMaxSlotSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 11),
    _CpqSePciMaxSlotSpeed_Type()
)
cpqSePciMaxSlotSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciMaxSlotSpeed.setStatus("mandatory")
_CpqSePciXMaxSlotSpeed_Type = Integer32
_CpqSePciXMaxSlotSpeed_Object = MibTableColumn
cpqSePciXMaxSlotSpeed = _CpqSePciXMaxSlotSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 12),
    _CpqSePciXMaxSlotSpeed_Type()
)
cpqSePciXMaxSlotSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciXMaxSlotSpeed.setStatus("mandatory")
_CpqSePciCurrentSlotSpeed_Type = Integer32
_CpqSePciCurrentSlotSpeed_Object = MibTableColumn
cpqSePciCurrentSlotSpeed = _CpqSePciCurrentSlotSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 13),
    _CpqSePciCurrentSlotSpeed_Type()
)
cpqSePciCurrentSlotSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciCurrentSlotSpeed.setStatus("mandatory")


class _CpqSePciHwLocation_Type(DisplayString):
    """Custom type cpqSePciHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSePciHwLocation_Type.__name__ = "DisplayString"
_CpqSePciHwLocation_Object = MibTableColumn
cpqSePciHwLocation = _CpqSePciHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 14),
    _CpqSePciHwLocation_Type()
)
cpqSePciHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciHwLocation.setStatus("optional")


class _CpqSePciSlotIOCTablePtr_Type(Integer32):
    """Custom type cpqSePciSlotIOCTablePtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_CpqSePciSlotIOCTablePtr_Type.__name__ = "Integer32"
_CpqSePciSlotIOCTablePtr_Object = MibTableColumn
cpqSePciSlotIOCTablePtr = _CpqSePciSlotIOCTablePtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 15),
    _CpqSePciSlotIOCTablePtr_Type()
)
cpqSePciSlotIOCTablePtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotIOCTablePtr.setStatus("mandatory")
_CpqSePciSlotHeaderType_Type = Integer32
_CpqSePciSlotHeaderType_Object = MibTableColumn
cpqSePciSlotHeaderType = _CpqSePciSlotHeaderType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 16),
    _CpqSePciSlotHeaderType_Type()
)
cpqSePciSlotHeaderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSlotHeaderType.setStatus("mandatory")


class _CpqSePciIsSlot0Embedded_Type(Integer32):
    """Custom type cpqSePciIsSlot0Embedded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CpqSePciIsSlot0Embedded_Type.__name__ = "Integer32"
_CpqSePciIsSlot0Embedded_Object = MibTableColumn
cpqSePciIsSlot0Embedded = _CpqSePciIsSlot0Embedded_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 17),
    _CpqSePciIsSlot0Embedded_Type()
)
cpqSePciIsSlot0Embedded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciIsSlot0Embedded.setStatus("optional")
_CpqSePcieSlotMaxLinkSpeed_Type = Integer32
_CpqSePcieSlotMaxLinkSpeed_Object = MibTableColumn
cpqSePcieSlotMaxLinkSpeed = _CpqSePcieSlotMaxLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 18),
    _CpqSePcieSlotMaxLinkSpeed_Type()
)
cpqSePcieSlotMaxLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePcieSlotMaxLinkSpeed.setStatus("optional")
_CpqSePcieSlotMaxLinkWidth_Type = Integer32
_CpqSePcieSlotMaxLinkWidth_Object = MibTableColumn
cpqSePcieSlotMaxLinkWidth = _CpqSePcieSlotMaxLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 1, 1, 19),
    _CpqSePcieSlotMaxLinkWidth_Type()
)
cpqSePcieSlotMaxLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePcieSlotMaxLinkWidth.setStatus("optional")
_CpqSePciFunctTable_Object = MibTable
cpqSePciFunctTable = _CpqSePciFunctTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    cpqSePciFunctTable.setStatus("mandatory")
_CpqSePciFunctEntry_Object = MibTableRow
cpqSePciFunctEntry = _CpqSePciFunctEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1)
)
cpqSePciFunctEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSePciFunctBusNumberIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSePciFunctDeviceNumberIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSePciFunctIndex"),
)
if mibBuilder.loadTexts:
    cpqSePciFunctEntry.setStatus("mandatory")
_CpqSePciFunctBusNumberIndex_Type = Integer32
_CpqSePciFunctBusNumberIndex_Object = MibTableColumn
cpqSePciFunctBusNumberIndex = _CpqSePciFunctBusNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 1),
    _CpqSePciFunctBusNumberIndex_Type()
)
cpqSePciFunctBusNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctBusNumberIndex.setStatus("mandatory")


class _CpqSePciFunctDeviceNumberIndex_Type(Integer32):
    """Custom type cpqSePciFunctDeviceNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSePciFunctDeviceNumberIndex_Type.__name__ = "Integer32"
_CpqSePciFunctDeviceNumberIndex_Object = MibTableColumn
cpqSePciFunctDeviceNumberIndex = _CpqSePciFunctDeviceNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 2),
    _CpqSePciFunctDeviceNumberIndex_Type()
)
cpqSePciFunctDeviceNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctDeviceNumberIndex.setStatus("mandatory")


class _CpqSePciFunctIndex_Type(Integer32):
    """Custom type cpqSePciFunctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CpqSePciFunctIndex_Type.__name__ = "Integer32"
_CpqSePciFunctIndex_Object = MibTableColumn
cpqSePciFunctIndex = _CpqSePciFunctIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 3),
    _CpqSePciFunctIndex_Type()
)
cpqSePciFunctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctIndex.setStatus("mandatory")


class _CpqSePciFunctClassCode_Type(OctetString):
    """Custom type cpqSePciFunctClassCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CpqSePciFunctClassCode_Type.__name__ = "OctetString"
_CpqSePciFunctClassCode_Object = MibTableColumn
cpqSePciFunctClassCode = _CpqSePciFunctClassCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 4),
    _CpqSePciFunctClassCode_Type()
)
cpqSePciFunctClassCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctClassCode.setStatus("mandatory")


class _CpqSePciFunctClassDescription_Type(DisplayString):
    """Custom type cpqSePciFunctClassDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqSePciFunctClassDescription_Type.__name__ = "DisplayString"
_CpqSePciFunctClassDescription_Object = MibTableColumn
cpqSePciFunctClassDescription = _CpqSePciFunctClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 5),
    _CpqSePciFunctClassDescription_Type()
)
cpqSePciFunctClassDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctClassDescription.setStatus("mandatory")


class _CpqSePciFunctDeviceID_Type(Integer32):
    """Custom type cpqSePciFunctDeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSePciFunctDeviceID_Type.__name__ = "Integer32"
_CpqSePciFunctDeviceID_Object = MibTableColumn
cpqSePciFunctDeviceID = _CpqSePciFunctDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 6),
    _CpqSePciFunctDeviceID_Type()
)
cpqSePciFunctDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctDeviceID.setStatus("mandatory")


class _CpqSePciFunctVendorID_Type(Integer32):
    """Custom type cpqSePciFunctVendorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSePciFunctVendorID_Type.__name__ = "Integer32"
_CpqSePciFunctVendorID_Object = MibTableColumn
cpqSePciFunctVendorID = _CpqSePciFunctVendorID_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 7),
    _CpqSePciFunctVendorID_Type()
)
cpqSePciFunctVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctVendorID.setStatus("mandatory")


class _CpqSePciFunctRevID_Type(Integer32):
    """Custom type cpqSePciFunctRevID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSePciFunctRevID_Type.__name__ = "Integer32"
_CpqSePciFunctRevID_Object = MibTableColumn
cpqSePciFunctRevID = _CpqSePciFunctRevID_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 8),
    _CpqSePciFunctRevID_Type()
)
cpqSePciFunctRevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctRevID.setStatus("mandatory")


class _CpqSePciFunctIntLine_Type(Integer32):
    """Custom type cpqSePciFunctIntLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSePciFunctIntLine_Type.__name__ = "Integer32"
_CpqSePciFunctIntLine_Object = MibTableColumn
cpqSePciFunctIntLine = _CpqSePciFunctIntLine_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 9),
    _CpqSePciFunctIntLine_Type()
)
cpqSePciFunctIntLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctIntLine.setStatus("mandatory")


class _CpqSePciFunctDevStatus_Type(Integer32):
    """Custom type cpqSePciFunctDevStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("unknown", 1))
    )


_CpqSePciFunctDevStatus_Type.__name__ = "Integer32"
_CpqSePciFunctDevStatus_Object = MibTableColumn
cpqSePciFunctDevStatus = _CpqSePciFunctDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 10),
    _CpqSePciFunctDevStatus_Type()
)
cpqSePciFunctDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctDevStatus.setStatus("mandatory")


class _CpqSePciFunctHwLocation_Type(DisplayString):
    """Custom type cpqSePciFunctHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSePciFunctHwLocation_Type.__name__ = "DisplayString"
_CpqSePciFunctHwLocation_Object = MibTableColumn
cpqSePciFunctHwLocation = _CpqSePciFunctHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 11),
    _CpqSePciFunctHwLocation_Type()
)
cpqSePciFunctHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciFunctHwLocation.setStatus("optional")
_CpqSePcieFunctNegotiatedLinkSpeed_Type = Integer32
_CpqSePcieFunctNegotiatedLinkSpeed_Object = MibTableColumn
cpqSePcieFunctNegotiatedLinkSpeed = _CpqSePcieFunctNegotiatedLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 12),
    _CpqSePcieFunctNegotiatedLinkSpeed_Type()
)
cpqSePcieFunctNegotiatedLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePcieFunctNegotiatedLinkSpeed.setStatus("optional")
_CpqSePcieFunctNegotiatedLinkWidth_Type = Integer32
_CpqSePcieFunctNegotiatedLinkWidth_Object = MibTableColumn
cpqSePcieFunctNegotiatedLinkWidth = _CpqSePcieFunctNegotiatedLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 13),
    _CpqSePcieFunctNegotiatedLinkWidth_Type()
)
cpqSePcieFunctNegotiatedLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePcieFunctNegotiatedLinkWidth.setStatus("optional")
_CpqSePcieFunctMaxLinkSpeed_Type = Integer32
_CpqSePcieFunctMaxLinkSpeed_Object = MibTableColumn
cpqSePcieFunctMaxLinkSpeed = _CpqSePcieFunctMaxLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 14),
    _CpqSePcieFunctMaxLinkSpeed_Type()
)
cpqSePcieFunctMaxLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePcieFunctMaxLinkSpeed.setStatus("optional")
_CpqSePcieFunctMaxLinkWidth_Type = Integer32
_CpqSePcieFunctMaxLinkWidth_Object = MibTableColumn
cpqSePcieFunctMaxLinkWidth = _CpqSePcieFunctMaxLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 2, 1, 15),
    _CpqSePcieFunctMaxLinkWidth_Type()
)
cpqSePcieFunctMaxLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePcieFunctMaxLinkWidth.setStatus("optional")
_CpqSePciMemoryTable_Object = MibTable
cpqSePciMemoryTable = _CpqSePciMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 3)
)
if mibBuilder.loadTexts:
    cpqSePciMemoryTable.setStatus("mandatory")
_CpqSePciMemoryEntry_Object = MibTableRow
cpqSePciMemoryEntry = _CpqSePciMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 3, 1)
)
cpqSePciMemoryEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSePciMemoryBusNumberIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSePciMemoryDeviceNumberIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSePciMemoryFunctionIndex"),
    (0, "CPQSTDEQ-MIB", "cpqSePciMemoryIndex"),
)
if mibBuilder.loadTexts:
    cpqSePciMemoryEntry.setStatus("mandatory")
_CpqSePciMemoryBusNumberIndex_Type = Integer32
_CpqSePciMemoryBusNumberIndex_Object = MibTableColumn
cpqSePciMemoryBusNumberIndex = _CpqSePciMemoryBusNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 3, 1, 1),
    _CpqSePciMemoryBusNumberIndex_Type()
)
cpqSePciMemoryBusNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciMemoryBusNumberIndex.setStatus("mandatory")


class _CpqSePciMemoryDeviceNumberIndex_Type(Integer32):
    """Custom type cpqSePciMemoryDeviceNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSePciMemoryDeviceNumberIndex_Type.__name__ = "Integer32"
_CpqSePciMemoryDeviceNumberIndex_Object = MibTableColumn
cpqSePciMemoryDeviceNumberIndex = _CpqSePciMemoryDeviceNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 3, 1, 2),
    _CpqSePciMemoryDeviceNumberIndex_Type()
)
cpqSePciMemoryDeviceNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciMemoryDeviceNumberIndex.setStatus("mandatory")


class _CpqSePciMemoryFunctionIndex_Type(Integer32):
    """Custom type cpqSePciMemoryFunctionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CpqSePciMemoryFunctionIndex_Type.__name__ = "Integer32"
_CpqSePciMemoryFunctionIndex_Object = MibTableColumn
cpqSePciMemoryFunctionIndex = _CpqSePciMemoryFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 3, 1, 3),
    _CpqSePciMemoryFunctionIndex_Type()
)
cpqSePciMemoryFunctionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciMemoryFunctionIndex.setStatus("mandatory")


class _CpqSePciMemoryIndex_Type(Integer32):
    """Custom type cpqSePciMemoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_CpqSePciMemoryIndex_Type.__name__ = "Integer32"
_CpqSePciMemoryIndex_Object = MibTableColumn
cpqSePciMemoryIndex = _CpqSePciMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 3, 1, 4),
    _CpqSePciMemoryIndex_Type()
)
cpqSePciMemoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciMemoryIndex.setStatus("mandatory")
_CpqSePciMemoryBaseAddr_Type = Integer32
_CpqSePciMemoryBaseAddr_Object = MibTableColumn
cpqSePciMemoryBaseAddr = _CpqSePciMemoryBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 3, 1, 5),
    _CpqSePciMemoryBaseAddr_Type()
)
cpqSePciMemoryBaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciMemoryBaseAddr.setStatus("mandatory")


class _CpqSePciMemoryType_Type(Integer32):
    """Custom type cpqSePciMemoryType based on Integer32"""
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
        *(("exp-rom", 4),
          ("io", 2),
          ("memory-mapped", 3),
          ("unknown", 1))
    )


_CpqSePciMemoryType_Type.__name__ = "Integer32"
_CpqSePciMemoryType_Object = MibTableColumn
cpqSePciMemoryType = _CpqSePciMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 3, 1, 6),
    _CpqSePciMemoryType_Type()
)
cpqSePciMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciMemoryType.setStatus("mandatory")
_CpqSePciMemorySize_Type = Integer32
_CpqSePciMemorySize_Object = MibTableColumn
cpqSePciMemorySize = _CpqSePciMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 3, 1, 7),
    _CpqSePciMemorySize_Type()
)
cpqSePciMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciMemorySize.setStatus("mandatory")


class _CpqSePciMemoryHwLocation_Type(DisplayString):
    """Custom type cpqSePciMemoryHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSePciMemoryHwLocation_Type.__name__ = "DisplayString"
_CpqSePciMemoryHwLocation_Object = MibTableColumn
cpqSePciMemoryHwLocation = _CpqSePciMemoryHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 3, 1, 8),
    _CpqSePciMemoryHwLocation_Type()
)
cpqSePciMemoryHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciMemoryHwLocation.setStatus("optional")


class _CpqSePciSegmentMode_Type(Integer32):
    """Custom type cpqSePciSegmentMode based on Integer32"""
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
        *(("auto-segment", 4),
          ("multi-segment", 3),
          ("single-segment", 2),
          ("unknown", 1))
    )


_CpqSePciSegmentMode_Type.__name__ = "Integer32"
_CpqSePciSegmentMode_Object = MibScalar
cpqSePciSegmentMode = _CpqSePciSegmentMode_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 13, 4),
    _CpqSePciSegmentMode_Type()
)
cpqSePciSegmentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePciSegmentMode.setStatus("optional")
_CpqSePCCard_ObjectIdentity = ObjectIdentity
cpqSePCCard = _CpqSePCCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14)
)
_CpqSePCCardSlotTable_Object = MibTable
cpqSePCCardSlotTable = _CpqSePCCardSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1)
)
if mibBuilder.loadTexts:
    cpqSePCCardSlotTable.setStatus("mandatory")
_CpqSePCCardSlotEntry_Object = MibTableRow
cpqSePCCardSlotEntry = _CpqSePCCardSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1)
)
cpqSePCCardSlotEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSePCCardSlotIndex"),
)
if mibBuilder.loadTexts:
    cpqSePCCardSlotEntry.setStatus("mandatory")
_CpqSePCCardSlotIndex_Type = Integer32
_CpqSePCCardSlotIndex_Object = MibTableColumn
cpqSePCCardSlotIndex = _CpqSePCCardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 1),
    _CpqSePCCardSlotIndex_Type()
)
cpqSePCCardSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardSlotIndex.setStatus("mandatory")


class _CpqSePCCardCondition_Type(Integer32):
    """Custom type cpqSePCCardCondition based on Integer32"""
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


_CpqSePCCardCondition_Type.__name__ = "Integer32"
_CpqSePCCardCondition_Object = MibTableColumn
cpqSePCCardCondition = _CpqSePCCardCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 2),
    _CpqSePCCardCondition_Type()
)
cpqSePCCardCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardCondition.setStatus("mandatory")


class _CpqSePCCardPhysLocation_Type(DisplayString):
    """Custom type cpqSePCCardPhysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpqSePCCardPhysLocation_Type.__name__ = "DisplayString"
_CpqSePCCardPhysLocation_Object = MibTableColumn
cpqSePCCardPhysLocation = _CpqSePCCardPhysLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 3),
    _CpqSePCCardPhysLocation_Type()
)
cpqSePCCardPhysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardPhysLocation.setStatus("mandatory")
_CpqSePCCardSlotType_Type = Integer32
_CpqSePCCardSlotType_Object = MibTableColumn
cpqSePCCardSlotType = _CpqSePCCardSlotType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 4),
    _CpqSePCCardSlotType_Type()
)
cpqSePCCardSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardSlotType.setStatus("mandatory")


class _CpqSePCCardSlotWidth_Type(Integer32):
    """Custom type cpqSePCCardSlotWidth based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("width128bit", 7),
          ("width16bit", 4),
          ("width32bit", 5),
          ("width64bit", 6),
          ("width8bit", 3))
    )


_CpqSePCCardSlotWidth_Type.__name__ = "Integer32"
_CpqSePCCardSlotWidth_Object = MibTableColumn
cpqSePCCardSlotWidth = _CpqSePCCardSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 5),
    _CpqSePCCardSlotWidth_Type()
)
cpqSePCCardSlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardSlotWidth.setStatus("mandatory")
_CpqSePCCardSlotThermalCapacity_Type = Integer32
_CpqSePCCardSlotThermalCapacity_Object = MibTableColumn
cpqSePCCardSlotThermalCapacity = _CpqSePCCardSlotThermalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 6),
    _CpqSePCCardSlotThermalCapacity_Type()
)
cpqSePCCardSlotThermalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardSlotThermalCapacity.setStatus("mandatory")


class _CpqSePCCardSlotThermalSensor_Type(Integer32):
    """Custom type cpqSePCCardSlotThermalSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSePCCardSlotThermalSensor_Type.__name__ = "Integer32"
_CpqSePCCardSlotThermalSensor_Object = MibTableColumn
cpqSePCCardSlotThermalSensor = _CpqSePCCardSlotThermalSensor_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 7),
    _CpqSePCCardSlotThermalSensor_Type()
)
cpqSePCCardSlotThermalSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardSlotThermalSensor.setStatus("mandatory")


class _CpqSePCCardSlotPowerState_Type(Integer32):
    """Custom type cpqSePCCardSlotPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("unknown", 1))
    )


_CpqSePCCardSlotPowerState_Type.__name__ = "Integer32"
_CpqSePCCardSlotPowerState_Object = MibTableColumn
cpqSePCCardSlotPowerState = _CpqSePCCardSlotPowerState_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 8),
    _CpqSePCCardSlotPowerState_Type()
)
cpqSePCCardSlotPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardSlotPowerState.setStatus("mandatory")


class _CpqSePCCardStatus_Type(Integer32):
    """Custom type cpqSePCCardStatus based on Integer32"""
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
        *(("ok", 2),
          ("thermalDegraded", 3),
          ("thermalFailure", 4),
          ("unknown", 1))
    )


_CpqSePCCardStatus_Type.__name__ = "Integer32"
_CpqSePCCardStatus_Object = MibTableColumn
cpqSePCCardStatus = _CpqSePCCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 9),
    _CpqSePCCardStatus_Type()
)
cpqSePCCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardStatus.setStatus("mandatory")


class _CpqSePCCardDeviceInfo_Type(DisplayString):
    """Custom type cpqSePCCardDeviceInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqSePCCardDeviceInfo_Type.__name__ = "DisplayString"
_CpqSePCCardDeviceInfo_Object = MibTableColumn
cpqSePCCardDeviceInfo = _CpqSePCCardDeviceInfo_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 10),
    _CpqSePCCardDeviceInfo_Type()
)
cpqSePCCardDeviceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardDeviceInfo.setStatus("mandatory")


class _CpqSePCCardProductInfo_Type(DisplayString):
    """Custom type cpqSePCCardProductInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqSePCCardProductInfo_Type.__name__ = "DisplayString"
_CpqSePCCardProductInfo_Object = MibTableColumn
cpqSePCCardProductInfo = _CpqSePCCardProductInfo_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 11),
    _CpqSePCCardProductInfo_Type()
)
cpqSePCCardProductInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardProductInfo.setStatus("mandatory")


class _CpqSePCCardSerialNumber_Type(DisplayString):
    """Custom type cpqSePCCardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqSePCCardSerialNumber_Type.__name__ = "DisplayString"
_CpqSePCCardSerialNumber_Object = MibTableColumn
cpqSePCCardSerialNumber = _CpqSePCCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 12),
    _CpqSePCCardSerialNumber_Type()
)
cpqSePCCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardSerialNumber.setStatus("mandatory")


class _CpqSePCCardAssetTag_Type(DisplayString):
    """Custom type cpqSePCCardAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqSePCCardAssetTag_Type.__name__ = "DisplayString"
_CpqSePCCardAssetTag_Object = MibTableColumn
cpqSePCCardAssetTag = _CpqSePCCardAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 14, 1, 1, 13),
    _CpqSePCCardAssetTag_Type()
)
cpqSePCCardAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePCCardAssetTag.setStatus("mandatory")
_CpqSeUSBPort_ObjectIdentity = ObjectIdentity
cpqSeUSBPort = _CpqSeUSBPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 15)
)
_CpqSeUSBPortTable_Object = MibTable
cpqSeUSBPortTable = _CpqSeUSBPortTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    cpqSeUSBPortTable.setStatus("mandatory")
_CpqSeUSBPortEntry_Object = MibTableRow
cpqSeUSBPortEntry = _CpqSeUSBPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 15, 1, 1)
)
cpqSeUSBPortEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeUSBPortIndex"),
)
if mibBuilder.loadTexts:
    cpqSeUSBPortEntry.setStatus("mandatory")


class _CpqSeUSBPortIndex_Type(Integer32):
    """Custom type cpqSeUSBPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqSeUSBPortIndex_Type.__name__ = "Integer32"
_CpqSeUSBPortIndex_Object = MibTableColumn
cpqSeUSBPortIndex = _CpqSeUSBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 15, 1, 1, 1),
    _CpqSeUSBPortIndex_Type()
)
cpqSeUSBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeUSBPortIndex.setStatus("mandatory")


class _CpqSeUSBPortType_Type(Integer32):
    """Custom type cpqSeUSBPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("usbPort", 2))
    )


_CpqSeUSBPortType_Type.__name__ = "Integer32"
_CpqSeUSBPortType_Object = MibTableColumn
cpqSeUSBPortType = _CpqSeUSBPortType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 15, 1, 1, 2),
    _CpqSeUSBPortType_Type()
)
cpqSeUSBPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeUSBPortType.setStatus("mandatory")


class _CpqSeUSBPortHwLocation_Type(DisplayString):
    """Custom type cpqSeUSBPortHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeUSBPortHwLocation_Type.__name__ = "DisplayString"
_CpqSeUSBPortHwLocation_Object = MibTableColumn
cpqSeUSBPortHwLocation = _CpqSeUSBPortHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 15, 1, 1, 3),
    _CpqSeUSBPortHwLocation_Type()
)
cpqSeUSBPortHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeUSBPortHwLocation.setStatus("optional")
_CpqSeCell_ObjectIdentity = ObjectIdentity
cpqSeCell = _CpqSeCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16)
)
_CpqSeCellTable_Object = MibTable
cpqSeCellTable = _CpqSeCellTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1)
)
if mibBuilder.loadTexts:
    cpqSeCellTable.setStatus("optional")
_CpqSeCellEntry_Object = MibTableRow
cpqSeCellEntry = _CpqSeCellEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1)
)
cpqSeCellEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeCellUnitIndex"),
)
if mibBuilder.loadTexts:
    cpqSeCellEntry.setStatus("optional")


class _CpqSeCellUnitIndex_Type(Integer32):
    """Custom type cpqSeCellUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CpqSeCellUnitIndex_Type.__name__ = "Integer32"
_CpqSeCellUnitIndex_Object = MibTableColumn
cpqSeCellUnitIndex = _CpqSeCellUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 1),
    _CpqSeCellUnitIndex_Type()
)
cpqSeCellUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellUnitIndex.setStatus("optional")


class _CpqSeCellCabinetNumber_Type(Integer32):
    """Custom type cpqSeCellCabinetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CpqSeCellCabinetNumber_Type.__name__ = "Integer32"
_CpqSeCellCabinetNumber_Object = MibTableColumn
cpqSeCellCabinetNumber = _CpqSeCellCabinetNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 2),
    _CpqSeCellCabinetNumber_Type()
)
cpqSeCellCabinetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellCabinetNumber.setStatus("optional")


class _CpqSeCellCellNumber_Type(Integer32):
    """Custom type cpqSeCellCellNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CpqSeCellCellNumber_Type.__name__ = "Integer32"
_CpqSeCellCellNumber_Object = MibTableColumn
cpqSeCellCellNumber = _CpqSeCellCellNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 3),
    _CpqSeCellCellNumber_Type()
)
cpqSeCellCellNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellCellNumber.setStatus("optional")


class _CpqSeCellIOCTablePtr_Type(Integer32):
    """Custom type cpqSeCellIOCTablePtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_CpqSeCellIOCTablePtr_Type.__name__ = "Integer32"
_CpqSeCellIOCTablePtr_Object = MibTableColumn
cpqSeCellIOCTablePtr = _CpqSeCellIOCTablePtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 4),
    _CpqSeCellIOCTablePtr_Type()
)
cpqSeCellIOCTablePtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellIOCTablePtr.setStatus("optional")


class _CpqSeCellPDHCFirmwareRevision_Type(DisplayString):
    """Custom type cpqSeCellPDHCFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCellPDHCFirmwareRevision_Type.__name__ = "DisplayString"
_CpqSeCellPDHCFirmwareRevision_Object = MibTableColumn
cpqSeCellPDHCFirmwareRevision = _CpqSeCellPDHCFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 5),
    _CpqSeCellPDHCFirmwareRevision_Type()
)
cpqSeCellPDHCFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellPDHCFirmwareRevision.setStatus("optional")


class _CpqSeCellSysFwVersion_Type(DisplayString):
    """Custom type cpqSeCellSysFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCellSysFwVersion_Type.__name__ = "DisplayString"
_CpqSeCellSysFwVersion_Object = MibTableColumn
cpqSeCellSysFwVersion = _CpqSeCellSysFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 6),
    _CpqSeCellSysFwVersion_Type()
)
cpqSeCellSysFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellSysFwVersion.setStatus("optional")
_CpqSeCellBootInhibited_Type = TruthValue
_CpqSeCellBootInhibited_Object = MibTableColumn
cpqSeCellBootInhibited = _CpqSeCellBootInhibited_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 7),
    _CpqSeCellBootInhibited_Type()
)
cpqSeCellBootInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellBootInhibited.setStatus("optional")
_CpqSeCellToScanBusConnectionStatus_Type = Integer32
_CpqSeCellToScanBusConnectionStatus_Object = MibTableColumn
cpqSeCellToScanBusConnectionStatus = _CpqSeCellToScanBusConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 8),
    _CpqSeCellToScanBusConnectionStatus_Type()
)
cpqSeCellToScanBusConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellToScanBusConnectionStatus.setStatus("optional")
_CpqSeCellHasCoreIO_Type = TruthValue
_CpqSeCellHasCoreIO_Object = MibTableColumn
cpqSeCellHasCoreIO = _CpqSeCellHasCoreIO_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 9),
    _CpqSeCellHasCoreIO_Type()
)
cpqSeCellHasCoreIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellHasCoreIO.setStatus("optional")
_CpqSeCellBoardSpeed_Type = Integer32
_CpqSeCellBoardSpeed_Object = MibTableColumn
cpqSeCellBoardSpeed = _CpqSeCellBoardSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 10),
    _CpqSeCellBoardSpeed_Type()
)
cpqSeCellBoardSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellBoardSpeed.setStatus("optional")
_CpqSeCellPresent_Type = TruthValue
_CpqSeCellPresent_Object = MibTableColumn
cpqSeCellPresent = _CpqSeCellPresent_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 11),
    _CpqSeCellPresent_Type()
)
cpqSeCellPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellPresent.setStatus("optional")
_CpqSeCellHasPower_Type = TruthValue
_CpqSeCellHasPower_Object = MibTableColumn
cpqSeCellHasPower = _CpqSeCellHasPower_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 12),
    _CpqSeCellHasPower_Type()
)
cpqSeCellHasPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellHasPower.setStatus("optional")
_CpqSeCellReadyForReconfig_Type = TruthValue
_CpqSeCellReadyForReconfig_Object = MibTableColumn
cpqSeCellReadyForReconfig = _CpqSeCellReadyForReconfig_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 13),
    _CpqSeCellReadyForReconfig_Type()
)
cpqSeCellReadyForReconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellReadyForReconfig.setStatus("optional")
_CpqSeCellTotalMemory_Type = Integer32
_CpqSeCellTotalMemory_Object = MibTableColumn
cpqSeCellTotalMemory = _CpqSeCellTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 14),
    _CpqSeCellTotalMemory_Type()
)
cpqSeCellTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellTotalMemory.setStatus("optional")
_CpqSeCellLEDState_Type = Integer32
_CpqSeCellLEDState_Object = MibTableColumn
cpqSeCellLEDState = _CpqSeCellLEDState_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 15),
    _CpqSeCellLEDState_Type()
)
cpqSeCellLEDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSeCellLEDState.setStatus("optional")
_CpqSeCellState_Type = Integer32
_CpqSeCellState_Object = MibTableColumn
cpqSeCellState = _CpqSeCellState_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 16),
    _CpqSeCellState_Type()
)
cpqSeCellState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSeCellState.setStatus("optional")
_CpqSeCellCLMRequestPercentage_Type = Integer32
_CpqSeCellCLMRequestPercentage_Object = MibTableColumn
cpqSeCellCLMRequestPercentage = _CpqSeCellCLMRequestPercentage_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 17),
    _CpqSeCellCLMRequestPercentage_Type()
)
cpqSeCellCLMRequestPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellCLMRequestPercentage.setStatus("optional")
_CpqSeCellCLMRequestSize_Type = Integer32
_CpqSeCellCLMRequestSize_Object = MibTableColumn
cpqSeCellCLMRequestSize = _CpqSeCellCLMRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 18),
    _CpqSeCellCLMRequestSize_Type()
)
cpqSeCellCLMRequestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellCLMRequestSize.setStatus("optional")
_CpqSeCellCLMAllocatedSize_Type = Integer32
_CpqSeCellCLMAllocatedSize_Object = MibTableColumn
cpqSeCellCLMAllocatedSize = _CpqSeCellCLMAllocatedSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 19),
    _CpqSeCellCLMAllocatedSize_Type()
)
cpqSeCellCLMAllocatedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellCLMAllocatedSize.setStatus("optional")
_CpqSeCellInterleaveAllocatedSize_Type = Integer32
_CpqSeCellInterleaveAllocatedSize_Object = MibTableColumn
cpqSeCellInterleaveAllocatedSize = _CpqSeCellInterleaveAllocatedSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 20),
    _CpqSeCellInterleaveAllocatedSize_Type()
)
cpqSeCellInterleaveAllocatedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellInterleaveAllocatedSize.setStatus("optional")
_CpqSeCellHasInterleaveMem_Type = Integer32
_CpqSeCellHasInterleaveMem_Object = MibTableColumn
cpqSeCellHasInterleaveMem = _CpqSeCellHasInterleaveMem_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 21),
    _CpqSeCellHasInterleaveMem_Type()
)
cpqSeCellHasInterleaveMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellHasInterleaveMem.setStatus("optional")


class _CpqSeCellSerialNumber_Type(DisplayString):
    """Custom type cpqSeCellSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeCellSerialNumber_Type.__name__ = "DisplayString"
_CpqSeCellSerialNumber_Object = MibTableColumn
cpqSeCellSerialNumber = _CpqSeCellSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 22),
    _CpqSeCellSerialNumber_Type()
)
cpqSeCellSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellSerialNumber.setStatus("optional")


class _CpqSeCellCLMCondition_Type(Integer32):
    """Custom type cpqSeCellCLMCondition based on Integer32"""
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


_CpqSeCellCLMCondition_Type.__name__ = "Integer32"
_CpqSeCellCLMCondition_Object = MibTableColumn
cpqSeCellCLMCondition = _CpqSeCellCLMCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 16, 1, 1, 23),
    _CpqSeCellCLMCondition_Type()
)
cpqSeCellCLMCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCellCLMCondition.setStatus("optional")
_CpqSeIOC_ObjectIdentity = ObjectIdentity
cpqSeIOC = _CpqSeIOC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 17)
)
_CpqSeIOCTable_Object = MibTable
cpqSeIOCTable = _CpqSeIOCTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    cpqSeIOCTable.setStatus("optional")
_CpqSeIOCEntry_Object = MibTableRow
cpqSeIOCEntry = _CpqSeIOCEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 17, 1, 1)
)
cpqSeIOCEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeIOCUnitIndex"),
)
if mibBuilder.loadTexts:
    cpqSeIOCEntry.setStatus("optional")


class _CpqSeIOCUnitIndex_Type(Integer32):
    """Custom type cpqSeIOCUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_CpqSeIOCUnitIndex_Type.__name__ = "Integer32"
_CpqSeIOCUnitIndex_Object = MibTableColumn
cpqSeIOCUnitIndex = _CpqSeIOCUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 17, 1, 1, 1),
    _CpqSeIOCUnitIndex_Type()
)
cpqSeIOCUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeIOCUnitIndex.setStatus("optional")


class _CpqSeIOCCabinetNumber_Type(Integer32):
    """Custom type cpqSeIOCCabinetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSeIOCCabinetNumber_Type.__name__ = "Integer32"
_CpqSeIOCCabinetNumber_Object = MibTableColumn
cpqSeIOCCabinetNumber = _CpqSeIOCCabinetNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 17, 1, 1, 2),
    _CpqSeIOCCabinetNumber_Type()
)
cpqSeIOCCabinetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeIOCCabinetNumber.setStatus("optional")


class _CpqSeIOCBayNumber_Type(Integer32):
    """Custom type cpqSeIOCBayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CpqSeIOCBayNumber_Type.__name__ = "Integer32"
_CpqSeIOCBayNumber_Object = MibTableColumn
cpqSeIOCBayNumber = _CpqSeIOCBayNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 17, 1, 1, 3),
    _CpqSeIOCBayNumber_Type()
)
cpqSeIOCBayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeIOCBayNumber.setStatus("optional")


class _CpqSeIOCIOCNumber_Type(Integer32):
    """Custom type cpqSeIOCIOCNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CpqSeIOCIOCNumber_Type.__name__ = "Integer32"
_CpqSeIOCIOCNumber_Object = MibTableColumn
cpqSeIOCIOCNumber = _CpqSeIOCIOCNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 17, 1, 1, 4),
    _CpqSeIOCIOCNumber_Type()
)
cpqSeIOCIOCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeIOCIOCNumber.setStatus("optional")


class _CpqSeIOCPowerState_Type(Integer32):
    """Custom type cpqSeIOCPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("powered-off", 2),
          ("powered-on", 3),
          ("unknown", 1))
    )


_CpqSeIOCPowerState_Type.__name__ = "Integer32"
_CpqSeIOCPowerState_Object = MibTableColumn
cpqSeIOCPowerState = _CpqSeIOCPowerState_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 17, 1, 1, 5),
    _CpqSeIOCPowerState_Type()
)
cpqSeIOCPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeIOCPowerState.setStatus("optional")
_CpqSeIOCLEDState_Type = Integer32
_CpqSeIOCLEDState_Object = MibTableColumn
cpqSeIOCLEDState = _CpqSeIOCLEDState_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 17, 1, 1, 6),
    _CpqSeIOCLEDState_Type()
)
cpqSeIOCLEDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSeIOCLEDState.setStatus("optional")
_CpqSePartition_ObjectIdentity = ObjectIdentity
cpqSePartition = _CpqSePartition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18)
)
_CpqSePartitionTotalCPU_Type = Integer32
_CpqSePartitionTotalCPU_Object = MibScalar
cpqSePartitionTotalCPU = _CpqSePartitionTotalCPU_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 1),
    _CpqSePartitionTotalCPU_Type()
)
cpqSePartitionTotalCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionTotalCPU.setStatus("optional")
_CpqSePartitionAvailableCellSlots_Type = Integer32
_CpqSePartitionAvailableCellSlots_Object = MibScalar
cpqSePartitionAvailableCellSlots = _CpqSePartitionAvailableCellSlots_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 2),
    _CpqSePartitionAvailableCellSlots_Type()
)
cpqSePartitionAvailableCellSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionAvailableCellSlots.setStatus("optional")
_CpqSePartitionInstalledCells_Type = Integer32
_CpqSePartitionInstalledCells_Object = MibScalar
cpqSePartitionInstalledCells = _CpqSePartitionInstalledCells_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 3),
    _CpqSePartitionInstalledCells_Type()
)
cpqSePartitionInstalledCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionInstalledCells.setStatus("optional")
_CpqSePartitionPoweredOnCells_Type = Integer32
_CpqSePartitionPoweredOnCells_Object = MibScalar
cpqSePartitionPoweredOnCells = _CpqSePartitionPoweredOnCells_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 4),
    _CpqSePartitionPoweredOnCells_Type()
)
cpqSePartitionPoweredOnCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionPoweredOnCells.setStatus("optional")
_CpqSePartitionReadyForReconfigCells_Type = Integer32
_CpqSePartitionReadyForReconfigCells_Object = MibScalar
cpqSePartitionReadyForReconfigCells = _CpqSePartitionReadyForReconfigCells_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 5),
    _CpqSePartitionReadyForReconfigCells_Type()
)
cpqSePartitionReadyForReconfigCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionReadyForReconfigCells.setStatus("optional")
_CpqSePartitionMemInterleavingType_Type = Integer32
_CpqSePartitionMemInterleavingType_Object = MibScalar
cpqSePartitionMemInterleavingType = _CpqSePartitionMemInterleavingType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 6),
    _CpqSePartitionMemInterleavingType_Type()
)
cpqSePartitionMemInterleavingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionMemInterleavingType.setStatus("optional")


class _CpqSePartitionName_Type(DisplayString):
    """Custom type cpqSePartitionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSePartitionName_Type.__name__ = "DisplayString"
_CpqSePartitionName_Object = MibScalar
cpqSePartitionName = _CpqSePartitionName_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 7),
    _CpqSePartitionName_Type()
)
cpqSePartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionName.setStatus("optional")
_CpqSePartitionCoreCell_Type = Integer32
_CpqSePartitionCoreCell_Object = MibScalar
cpqSePartitionCoreCell = _CpqSePartitionCoreCell_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 8),
    _CpqSePartitionCoreCell_Type()
)
cpqSePartitionCoreCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionCoreCell.setStatus("optional")
_CpqSePartitionCoreCellCabinet_Type = Integer32
_CpqSePartitionCoreCellCabinet_Object = MibScalar
cpqSePartitionCoreCellCabinet = _CpqSePartitionCoreCellCabinet_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 9),
    _CpqSePartitionCoreCellCabinet_Type()
)
cpqSePartitionCoreCellCabinet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionCoreCellCabinet.setStatus("optional")
_CpqSePartitionCLMRequestPercentage_Type = Integer32
_CpqSePartitionCLMRequestPercentage_Object = MibScalar
cpqSePartitionCLMRequestPercentage = _CpqSePartitionCLMRequestPercentage_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 10),
    _CpqSePartitionCLMRequestPercentage_Type()
)
cpqSePartitionCLMRequestPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionCLMRequestPercentage.setStatus("optional")
_CpqSePartitionCLMRequestSize_Type = Integer32
_CpqSePartitionCLMRequestSize_Object = MibScalar
cpqSePartitionCLMRequestSize = _CpqSePartitionCLMRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 11),
    _CpqSePartitionCLMRequestSize_Type()
)
cpqSePartitionCLMRequestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionCLMRequestSize.setStatus("optional")
_CpqSePartitionCLMAllocatedSize_Type = Integer32
_CpqSePartitionCLMAllocatedSize_Object = MibScalar
cpqSePartitionCLMAllocatedSize = _CpqSePartitionCLMAllocatedSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 12),
    _CpqSePartitionCLMAllocatedSize_Type()
)
cpqSePartitionCLMAllocatedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionCLMAllocatedSize.setStatus("optional")
_CpqSePartitionInterleaveAllocatedSize_Type = Integer32
_CpqSePartitionInterleaveAllocatedSize_Object = MibScalar
cpqSePartitionInterleaveAllocatedSize = _CpqSePartitionInterleaveAllocatedSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 13),
    _CpqSePartitionInterleaveAllocatedSize_Type()
)
cpqSePartitionInterleaveAllocatedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionInterleaveAllocatedSize.setStatus("optional")
_CpqSePartitionHasInterleaveMem_Type = Integer32
_CpqSePartitionHasInterleaveMem_Object = MibScalar
cpqSePartitionHasInterleaveMem = _CpqSePartitionHasInterleaveMem_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 14),
    _CpqSePartitionHasInterleaveMem_Type()
)
cpqSePartitionHasInterleaveMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionHasInterleaveMem.setStatus("optional")
_CpqSePartitionNumber_Type = Integer32
_CpqSePartitionNumber_Object = MibScalar
cpqSePartitionNumber = _CpqSePartitionNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 18, 15),
    _CpqSePartitionNumber_Type()
)
cpqSePartitionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSePartitionNumber.setStatus("optional")
_CpqSeCabinet_ObjectIdentity = ObjectIdentity
cpqSeCabinet = _CpqSeCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 19)
)
_CpqSeCabinetTable_Object = MibTable
cpqSeCabinetTable = _CpqSeCabinetTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 19, 1)
)
if mibBuilder.loadTexts:
    cpqSeCabinetTable.setStatus("optional")
_CpqSeCabinetEntry_Object = MibTableRow
cpqSeCabinetEntry = _CpqSeCabinetEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 19, 1, 1)
)
cpqSeCabinetEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeCabinetUnitIndex"),
)
if mibBuilder.loadTexts:
    cpqSeCabinetEntry.setStatus("optional")


class _CpqSeCabinetUnitIndex_Type(Integer32):
    """Custom type cpqSeCabinetUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CpqSeCabinetUnitIndex_Type.__name__ = "Integer32"
_CpqSeCabinetUnitIndex_Object = MibTableColumn
cpqSeCabinetUnitIndex = _CpqSeCabinetUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 19, 1, 1, 1),
    _CpqSeCabinetUnitIndex_Type()
)
cpqSeCabinetUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCabinetUnitIndex.setStatus("optional")
_CpqSeCabinetCPULED_Type = TruthValue
_CpqSeCabinetCPULED_Object = MibTableColumn
cpqSeCabinetCPULED = _CpqSeCabinetCPULED_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 19, 1, 1, 2),
    _CpqSeCabinetCPULED_Type()
)
cpqSeCabinetCPULED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCabinetCPULED.setStatus("optional")
_CpqSeCabinetIOXLED_Type = TruthValue
_CpqSeCabinetIOXLED_Object = MibTableColumn
cpqSeCabinetIOXLED = _CpqSeCabinetIOXLED_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 19, 1, 1, 3),
    _CpqSeCabinetIOXLED_Type()
)
cpqSeCabinetIOXLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCabinetIOXLED.setStatus("optional")
_CpqSeCabinetTypeNum_Type = Integer32
_CpqSeCabinetTypeNum_Object = MibTableColumn
cpqSeCabinetTypeNum = _CpqSeCabinetTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 19, 1, 1, 4),
    _CpqSeCabinetTypeNum_Type()
)
cpqSeCabinetTypeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeCabinetTypeNum.setStatus("optional")
_CpqSeCabinetLED_Type = Integer32
_CpqSeCabinetLED_Object = MibTableColumn
cpqSeCabinetLED = _CpqSeCabinetLED_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 19, 1, 1, 5),
    _CpqSeCabinetLED_Type()
)
cpqSeCabinetLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSeCabinetLED.setStatus("optional")
_CpqSeComplex_ObjectIdentity = ObjectIdentity
cpqSeComplex = _CpqSeComplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20)
)


class _CpqSeComplexUUID_Type(DisplayString):
    """Custom type cpqSeComplexUUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeComplexUUID_Type.__name__ = "DisplayString"
_CpqSeComplexUUID_Object = MibScalar
cpqSeComplexUUID = _CpqSeComplexUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 1),
    _CpqSeComplexUUID_Type()
)
cpqSeComplexUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexUUID.setStatus("optional")


class _CpqSeComplexTotalCabinet_Type(Integer32):
    """Custom type cpqSeComplexTotalCabinet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CpqSeComplexTotalCabinet_Type.__name__ = "Integer32"
_CpqSeComplexTotalCabinet_Object = MibScalar
cpqSeComplexTotalCabinet = _CpqSeComplexTotalCabinet_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 2),
    _CpqSeComplexTotalCabinet_Type()
)
cpqSeComplexTotalCabinet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexTotalCabinet.setStatus("optional")


class _CpqSeComplexComputeCabinet_Type(Integer32):
    """Custom type cpqSeComplexComputeCabinet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CpqSeComplexComputeCabinet_Type.__name__ = "Integer32"
_CpqSeComplexComputeCabinet_Object = MibScalar
cpqSeComplexComputeCabinet = _CpqSeComplexComputeCabinet_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 3),
    _CpqSeComplexComputeCabinet_Type()
)
cpqSeComplexComputeCabinet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexComputeCabinet.setStatus("optional")


class _CpqSeComplexIOXCabinet_Type(Integer32):
    """Custom type cpqSeComplexIOXCabinet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CpqSeComplexIOXCabinet_Type.__name__ = "Integer32"
_CpqSeComplexIOXCabinet_Object = MibScalar
cpqSeComplexIOXCabinet = _CpqSeComplexIOXCabinet_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 4),
    _CpqSeComplexIOXCabinet_Type()
)
cpqSeComplexIOXCabinet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexIOXCabinet.setStatus("optional")


class _CpqSeComplexName_Type(DisplayString):
    """Custom type cpqSeComplexName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeComplexName_Type.__name__ = "DisplayString"
_CpqSeComplexName_Object = MibScalar
cpqSeComplexName = _CpqSeComplexName_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 5),
    _CpqSeComplexName_Type()
)
cpqSeComplexName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexName.setStatus("optional")
_CpqSeComplexLockedProperty_Type = Integer32
_CpqSeComplexLockedProperty_Object = MibScalar
cpqSeComplexLockedProperty = _CpqSeComplexLockedProperty_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 6),
    _CpqSeComplexLockedProperty_Type()
)
cpqSeComplexLockedProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexLockedProperty.setStatus("optional")
_CpqSeComplexCellSlotStatusTable_Object = MibTable
cpqSeComplexCellSlotStatusTable = _CpqSeComplexCellSlotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 7)
)
if mibBuilder.loadTexts:
    cpqSeComplexCellSlotStatusTable.setStatus("optional")
_CpqSeComplexCellSlotStatusEntry_Object = MibTableRow
cpqSeComplexCellSlotStatusEntry = _CpqSeComplexCellSlotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 7, 1)
)
cpqSeComplexCellSlotStatusEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeComplexCellSlotStatusIndex"),
)
if mibBuilder.loadTexts:
    cpqSeComplexCellSlotStatusEntry.setStatus("optional")
_CpqSeComplexCellSlotStatusIndex_Type = Integer32
_CpqSeComplexCellSlotStatusIndex_Object = MibTableColumn
cpqSeComplexCellSlotStatusIndex = _CpqSeComplexCellSlotStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 7, 1, 1),
    _CpqSeComplexCellSlotStatusIndex_Type()
)
cpqSeComplexCellSlotStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexCellSlotStatusIndex.setStatus("optional")
_CpqSeComplexCellSlotStatusCabinetNo_Type = Integer32
_CpqSeComplexCellSlotStatusCabinetNo_Object = MibTableColumn
cpqSeComplexCellSlotStatusCabinetNo = _CpqSeComplexCellSlotStatusCabinetNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 7, 1, 2),
    _CpqSeComplexCellSlotStatusCabinetNo_Type()
)
cpqSeComplexCellSlotStatusCabinetNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexCellSlotStatusCabinetNo.setStatus("optional")
_CpqSeComplexCellSlotStatusSlotNo_Type = Integer32
_CpqSeComplexCellSlotStatusSlotNo_Object = MibTableColumn
cpqSeComplexCellSlotStatusSlotNo = _CpqSeComplexCellSlotStatusSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 7, 1, 3),
    _CpqSeComplexCellSlotStatusSlotNo_Type()
)
cpqSeComplexCellSlotStatusSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexCellSlotStatusSlotNo.setStatus("optional")


class _CpqSeComplexCellSlotStatus_Type(Integer32):
    """Custom type cpqSeComplexCellSlotStatus based on Integer32"""
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
        *(("active", 2),
          ("assigned-powered-off", 4),
          ("empty", 7),
          ("free-powered-off", 6),
          ("free-powered-on", 5),
          ("inactive", 3),
          ("unknown", 1))
    )


_CpqSeComplexCellSlotStatus_Type.__name__ = "Integer32"
_CpqSeComplexCellSlotStatus_Object = MibTableColumn
cpqSeComplexCellSlotStatus = _CpqSeComplexCellSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 7, 1, 4),
    _CpqSeComplexCellSlotStatus_Type()
)
cpqSeComplexCellSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexCellSlotStatus.setStatus("optional")
_CpqSeComplexCellSlotPartitionNo_Type = Integer32
_CpqSeComplexCellSlotPartitionNo_Object = MibTableColumn
cpqSeComplexCellSlotPartitionNo = _CpqSeComplexCellSlotPartitionNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 7, 1, 5),
    _CpqSeComplexCellSlotPartitionNo_Type()
)
cpqSeComplexCellSlotPartitionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexCellSlotPartitionNo.setStatus("optional")


class _CpqSeComplexCellSlotPartitionName_Type(DisplayString):
    """Custom type cpqSeComplexCellSlotPartitionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeComplexCellSlotPartitionName_Type.__name__ = "DisplayString"
_CpqSeComplexCellSlotPartitionName_Object = MibTableColumn
cpqSeComplexCellSlotPartitionName = _CpqSeComplexCellSlotPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 20, 7, 1, 6),
    _CpqSeComplexCellSlotPartitionName_Type()
)
cpqSeComplexCellSlotPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeComplexCellSlotPartitionName.setStatus("optional")
_CpqSeLED_ObjectIdentity = ObjectIdentity
cpqSeLED = _CpqSeLED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 21)
)
_CpqSeLEDTable_Object = MibTable
cpqSeLEDTable = _CpqSeLEDTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 21, 1)
)
if mibBuilder.loadTexts:
    cpqSeLEDTable.setStatus("optional")
_CpqSeLEDEntry_Object = MibTableRow
cpqSeLEDEntry = _CpqSeLEDEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 21, 1, 1)
)
cpqSeLEDEntry.setIndexNames(
    (0, "CPQSTDEQ-MIB", "cpqSeLEDIndex"),
)
if mibBuilder.loadTexts:
    cpqSeLEDEntry.setStatus("optional")


class _CpqSeLEDIndex_Type(Integer32):
    """Custom type cpqSeLEDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSeLEDIndex_Type.__name__ = "Integer32"
_CpqSeLEDIndex_Object = MibTableColumn
cpqSeLEDIndex = _CpqSeLEDIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 21, 1, 1, 1),
    _CpqSeLEDIndex_Type()
)
cpqSeLEDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeLEDIndex.setStatus("optional")
_CpqSeLEDState_Type = Integer32
_CpqSeLEDState_Object = MibTableColumn
cpqSeLEDState = _CpqSeLEDState_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 21, 1, 1, 2),
    _CpqSeLEDState_Type()
)
cpqSeLEDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSeLEDState.setStatus("optional")
_CpqSeLEDStateDuration_Type = Integer32
_CpqSeLEDStateDuration_Object = MibTableColumn
cpqSeLEDStateDuration = _CpqSeLEDStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 21, 1, 1, 3),
    _CpqSeLEDStateDuration_Type()
)
cpqSeLEDStateDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqSeLEDStateDuration.setStatus("optional")
_CpqSeLEDLocationType_Type = Integer32
_CpqSeLEDLocationType_Object = MibTableColumn
cpqSeLEDLocationType = _CpqSeLEDLocationType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 21, 1, 1, 4),
    _CpqSeLEDLocationType_Type()
)
cpqSeLEDLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeLEDLocationType.setStatus("optional")


class _CpqSeLEDDescription_Type(DisplayString):
    """Custom type cpqSeLEDDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeLEDDescription_Type.__name__ = "DisplayString"
_CpqSeLEDDescription_Object = MibTableColumn
cpqSeLEDDescription = _CpqSeLEDDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 21, 1, 1, 5),
    _CpqSeLEDDescription_Type()
)
cpqSeLEDDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeLEDDescription.setStatus("optional")


class _CpqSeLEDHardwareLocation_Type(DisplayString):
    """Custom type cpqSeLEDHardwareLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeLEDHardwareLocation_Type.__name__ = "DisplayString"
_CpqSeLEDHardwareLocation_Object = MibTableColumn
cpqSeLEDHardwareLocation = _CpqSeLEDHardwareLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 21, 1, 1, 6),
    _CpqSeLEDHardwareLocation_Type()
)
cpqSeLEDHardwareLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeLEDHardwareLocation.setStatus("optional")
_CpqSeUSBDevice_ObjectIdentity = ObjectIdentity
cpqSeUSBDevice = _CpqSeUSBDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 22)
)


class _CpqSeUSBDeviceType_Type(DisplayString):
    """Custom type cpqSeUSBDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeUSBDeviceType_Type.__name__ = "DisplayString"
_CpqSeUSBDeviceType_Object = MibScalar
cpqSeUSBDeviceType = _CpqSeUSBDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 22, 1),
    _CpqSeUSBDeviceType_Type()
)
cpqSeUSBDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeUSBDeviceType.setStatus("optional")


class _CpqSeUSBDeviceName_Type(DisplayString):
    """Custom type cpqSeUSBDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSeUSBDeviceName_Type.__name__ = "DisplayString"
_CpqSeUSBDeviceName_Object = MibScalar
cpqSeUSBDeviceName = _CpqSeUSBDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 232, 1, 2, 22, 2),
    _CpqSeUSBDeviceName_Type()
)
cpqSeUSBDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSeUSBDeviceName.setStatus("optional")

# Managed Objects groups


# Notification objects

cpqSeCpuThresholdPassed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 1001)
)
cpqSeCpuThresholdPassed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSlot"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSocketNumber"))
)
if mibBuilder.loadTexts:
    cpqSeCpuThresholdPassed.setStatus(
        ""
    )

cpqSePCCardThermalDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 1002)
)
cpqSePCCardThermalDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTDEQ-MIB", "cpqSePCCardDeviceInfo"),
        ("CPQSTDEQ-MIB", "cpqSePCCardProductInfo"),
        ("CPQSTDEQ-MIB", "cpqSePCCardSlotIndex"))
)
if mibBuilder.loadTexts:
    cpqSePCCardThermalDegraded.setStatus(
        ""
    )

cpqSePCCardThermalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 1003)
)
cpqSePCCardThermalFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTDEQ-MIB", "cpqSePCCardDeviceInfo"),
        ("CPQSTDEQ-MIB", "cpqSePCCardProductInfo"),
        ("CPQSTDEQ-MIB", "cpqSePCCardSlotIndex"))
)
if mibBuilder.loadTexts:
    cpqSePCCardThermalFailure.setStatus(
        ""
    )

cpqSePCCardThermalSafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 1004)
)
cpqSePCCardThermalSafe.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTDEQ-MIB", "cpqSePCCardSlotIndex"))
)
if mibBuilder.loadTexts:
    cpqSePCCardThermalSafe.setStatus(
        ""
    )

cpqSe2CpuThresholdPassed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 1005)
)
cpqSe2CpuThresholdPassed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSlot"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSocketNumber"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSpeed"),
        ("CPQSTDEQ-MIB", "cpqSeCpuExtSpeed"),
        ("CPQSTDEQ-MIB", "cpqSeCpuCacheSize"))
)
if mibBuilder.loadTexts:
    cpqSe2CpuThresholdPassed.setStatus(
        ""
    )

cpqSeCpuStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 1006)
)
cpqSeCpuStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTDEQ-MIB", "cpqSeCpuUnitIndex"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSlot"),
        ("CPQSTDEQ-MIB", "cpqSeCpuName"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSpeed"),
        ("CPQSTDEQ-MIB", "cpqSeCpuStep"),
        ("CPQSTDEQ-MIB", "cpqSeCpuStatus"),
        ("CPQSTDEQ-MIB", "cpqSeCpuExtSpeed"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSocketNumber"),
        ("CPQSTDEQ-MIB", "cpqSeCpuHwLocation"))
)
if mibBuilder.loadTexts:
    cpqSeCpuStatusChange.setStatus(
        ""
    )

cpqSeCpuPowerPodstatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 1007)
)
cpqSeCpuPowerPodstatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTDEQ-MIB", "cpqSeCpuUnitIndex"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSlot"),
        ("CPQSTDEQ-MIB", "cpqSeCpuName"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSpeed"),
        ("CPQSTDEQ-MIB", "cpqSeCpuStep"),
        ("CPQSTDEQ-MIB", "cpqSeCpuPowerpodStatus"),
        ("CPQSTDEQ-MIB", "cpqSeCpuExtSpeed"),
        ("CPQSTDEQ-MIB", "cpqSeCpuSocketNumber"),
        ("CPQSTDEQ-MIB", "cpqSeCpuHwLocation"))
)
if mibBuilder.loadTexts:
    cpqSeCpuPowerPodstatusChange.setStatus(
        ""
    )

cpqSeUSBStorageDeviceAttached = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 1008)
)
cpqSeUSBStorageDeviceAttached.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTDEQ-MIB", "cpqSeUSBDeviceType"),
        ("CPQSTDEQ-MIB", "cpqSeUSBDeviceName"))
)
if mibBuilder.loadTexts:
    cpqSeUSBStorageDeviceAttached.setStatus(
        ""
    )

cpqSeUSBStorageDeviceRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 1009)
)
cpqSeUSBStorageDeviceRemoved.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTDEQ-MIB", "cpqSeUSBDeviceType"),
        ("CPQSTDEQ-MIB", "cpqSeUSBDeviceName"))
)
if mibBuilder.loadTexts:
    cpqSeUSBStorageDeviceRemoved.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSTDEQ-MIB",
    **{"TruthValue": TruthValue,
       "cpqSeCpuThresholdPassed": cpqSeCpuThresholdPassed,
       "cpqSePCCardThermalDegraded": cpqSePCCardThermalDegraded,
       "cpqSePCCardThermalFailure": cpqSePCCardThermalFailure,
       "cpqSePCCardThermalSafe": cpqSePCCardThermalSafe,
       "cpqSe2CpuThresholdPassed": cpqSe2CpuThresholdPassed,
       "cpqSeCpuStatusChange": cpqSeCpuStatusChange,
       "cpqSeCpuPowerPodstatusChange": cpqSeCpuPowerPodstatusChange,
       "cpqSeUSBStorageDeviceAttached": cpqSeUSBStorageDeviceAttached,
       "cpqSeUSBStorageDeviceRemoved": cpqSeUSBStorageDeviceRemoved,
       "cpqStdEquipment": cpqStdEquipment,
       "cpqSeMibRev": cpqSeMibRev,
       "cpqSeMibRevMajor": cpqSeMibRevMajor,
       "cpqSeMibRevMinor": cpqSeMibRevMinor,
       "cpqSeMibCondition": cpqSeMibCondition,
       "cpqSeComponent": cpqSeComponent,
       "cpqSeInterface": cpqSeInterface,
       "cpqSeOsCommon": cpqSeOsCommon,
       "cpqSeOsCommonPollFreq": cpqSeOsCommonPollFreq,
       "cpqSeOsCommonModuleTable": cpqSeOsCommonModuleTable,
       "cpqSeOsCommonModuleEntry": cpqSeOsCommonModuleEntry,
       "cpqSeOsCommonModuleIndex": cpqSeOsCommonModuleIndex,
       "cpqSeOsCommonModuleName": cpqSeOsCommonModuleName,
       "cpqSeOsCommonModuleVersion": cpqSeOsCommonModuleVersion,
       "cpqSeOsCommonModuleDate": cpqSeOsCommonModuleDate,
       "cpqSeOsCommonModulePurpose": cpqSeOsCommonModulePurpose,
       "cpqSeProcessor": cpqSeProcessor,
       "cpqSeCpuTable": cpqSeCpuTable,
       "cpqSeCpuEntry": cpqSeCpuEntry,
       "cpqSeCpuUnitIndex": cpqSeCpuUnitIndex,
       "cpqSeCpuSlot": cpqSeCpuSlot,
       "cpqSeCpuName": cpqSeCpuName,
       "cpqSeCpuSpeed": cpqSeCpuSpeed,
       "cpqSeCpuStep": cpqSeCpuStep,
       "cpqSeCpuStatus": cpqSeCpuStatus,
       "cpqSeCpuExtSpeed": cpqSeCpuExtSpeed,
       "cpqSeCpuDesigner": cpqSeCpuDesigner,
       "cpqSeCpuSocketNumber": cpqSeCpuSocketNumber,
       "cpqSeCpuThreshPassed": cpqSeCpuThreshPassed,
       "cpqSeCpuHwLocation": cpqSeCpuHwLocation,
       "cpqSeCpuCellTablePtr": cpqSeCpuCellTablePtr,
       "cpqSeCpuPowerpodStatus": cpqSeCpuPowerpodStatus,
       "cpqSeCpuArchitectureRevision": cpqSeCpuArchitectureRevision,
       "cpqSeCpuCore": cpqSeCpuCore,
       "cpqSeCPUSerialNumber": cpqSeCPUSerialNumber,
       "cpqSeCPUPartNumber": cpqSeCPUPartNumber,
       "cpqSeCPUSerialNumberMfgr": cpqSeCPUSerialNumberMfgr,
       "cpqSeCPUPartNumberMfgr": cpqSeCPUPartNumberMfgr,
       "cpqSeCPUCoreIndex": cpqSeCPUCoreIndex,
       "cpqSeCPUMaxSpeed": cpqSeCPUMaxSpeed,
       "cpqSeCPUCoreThreadIndex": cpqSeCPUCoreThreadIndex,
       "cpqSeCPUChipGenerationName": cpqSeCPUChipGenerationName,
       "cpqSeCPUMultiThreadStatus": cpqSeCPUMultiThreadStatus,
       "cpqSeCPUCoreMaxThreads": cpqSeCPUCoreMaxThreads,
       "cpqSeCpuLowPowerStatus": cpqSeCpuLowPowerStatus,
       "cpqSeCpuPrimary": cpqSeCpuPrimary,
       "cpqSeCpuCoreSteppingText": cpqSeCpuCoreSteppingText,
       "cpqSeCpuCurrentPerformanceState": cpqSeCpuCurrentPerformanceState,
       "cpqSeCpuMinPerformanceState": cpqSeCpuMinPerformanceState,
       "cpqSeCpuMaxPerformanceState": cpqSeCpuMaxPerformanceState,
       "cpqSeFpuTable": cpqSeFpuTable,
       "cpqSeFpuEntry": cpqSeFpuEntry,
       "cpqSeFpuUnitIndex": cpqSeFpuUnitIndex,
       "cpqSeFpuChipIndex": cpqSeFpuChipIndex,
       "cpqSeFpuSlot": cpqSeFpuSlot,
       "cpqSeFpuName": cpqSeFpuName,
       "cpqSeFpuSpeed": cpqSeFpuSpeed,
       "cpqSeFpuType": cpqSeFpuType,
       "cpqSeFpuHwLocation": cpqSeFpuHwLocation,
       "cpqSeCpuCacheTable": cpqSeCpuCacheTable,
       "cpqSeCpuCacheEntry": cpqSeCpuCacheEntry,
       "cpqSeCpuCacheUnitIndex": cpqSeCpuCacheUnitIndex,
       "cpqSeCpuCacheLevelIndex": cpqSeCpuCacheLevelIndex,
       "cpqSeCpuCacheSize": cpqSeCpuCacheSize,
       "cpqSeCpuCacheSpeed": cpqSeCpuCacheSpeed,
       "cpqSeCpuCacheStatus": cpqSeCpuCacheStatus,
       "cpqSeCpuCacheWritePolicy": cpqSeCpuCacheWritePolicy,
       "cpqSeCpuCacheHwLocation": cpqSeCpuCacheHwLocation,
       "cpqSeCpuCacheCpuSlot": cpqSeCpuCacheCpuSlot,
       "cpqSeCpuCacheCpuCoreIndex": cpqSeCpuCacheCpuCoreIndex,
       "cpqSeMemory": cpqSeMemory,
       "cpqSeBaseMem": cpqSeBaseMem,
       "cpqSeTotalMem": cpqSeTotalMem,
       "cpqSeTotalMemMB": cpqSeTotalMemMB,
       "cpqSeIsaCmos": cpqSeIsaCmos,
       "cpqSeIsaCmosRaw": cpqSeIsaCmosRaw,
       "cpqSeEisaNvram": cpqSeEisaNvram,
       "cpqSeEisaSlotTable": cpqSeEisaSlotTable,
       "cpqSeEisaSlotEntry": cpqSeEisaSlotEntry,
       "cpqSeEisaSlotIndex": cpqSeEisaSlotIndex,
       "cpqSeEisaSlotRaw": cpqSeEisaSlotRaw,
       "cpqSeEisaSlotBoardId": cpqSeEisaSlotBoardId,
       "cpqSeEisaSlotBoardName": cpqSeEisaSlotBoardName,
       "cpqSeEisaSlotCfRev": cpqSeEisaSlotCfRev,
       "cpqSeEisaSlotType": cpqSeEisaSlotType,
       "cpqSeEisaFunctTable": cpqSeEisaFunctTable,
       "cpqSeEisaFunctEntry": cpqSeEisaFunctEntry,
       "cpqSeEisaFunctSlotIndex": cpqSeEisaFunctSlotIndex,
       "cpqSeEisaFunctIndex": cpqSeEisaFunctIndex,
       "cpqSeEisaFunctStatus": cpqSeEisaFunctStatus,
       "cpqSeEisaFunctType": cpqSeEisaFunctType,
       "cpqSeEisaFunctCfgRev": cpqSeEisaFunctCfgRev,
       "cpqSeEisaFunctSels": cpqSeEisaFunctSels,
       "cpqSeEisaFunctInfo": cpqSeEisaFunctInfo,
       "cpqSeEisaMemTable": cpqSeEisaMemTable,
       "cpqSeEisaMemEntry": cpqSeEisaMemEntry,
       "cpqSeEisaMemSlotIndex": cpqSeEisaMemSlotIndex,
       "cpqSeEisaMemFunctIndex": cpqSeEisaMemFunctIndex,
       "cpqSeEisaMemAllocIndex": cpqSeEisaMemAllocIndex,
       "cpqSeEisaMemStartAddr": cpqSeEisaMemStartAddr,
       "cpqSeEisaMemSize": cpqSeEisaMemSize,
       "cpqSeEisaMemShare": cpqSeEisaMemShare,
       "cpqSeEisaMemType": cpqSeEisaMemType,
       "cpqSeEisaMemCache": cpqSeEisaMemCache,
       "cpqSeEisaMemAccess": cpqSeEisaMemAccess,
       "cpqSeEisaMemDecode": cpqSeEisaMemDecode,
       "cpqSeEisaMemDataSize": cpqSeEisaMemDataSize,
       "cpqSeEisaIntTable": cpqSeEisaIntTable,
       "cpqSeEisaIntEntry": cpqSeEisaIntEntry,
       "cpqSeEisaIntSlotIndex": cpqSeEisaIntSlotIndex,
       "cpqSeEisaIntFunctIndex": cpqSeEisaIntFunctIndex,
       "cpqSeEisaIntAllocIndex": cpqSeEisaIntAllocIndex,
       "cpqSeEisaIntNum": cpqSeEisaIntNum,
       "cpqSeEisaIntShare": cpqSeEisaIntShare,
       "cpqSeEisaIntTrigger": cpqSeEisaIntTrigger,
       "cpqSeEisaDmaTable": cpqSeEisaDmaTable,
       "cpqSeEisaDmaEntry": cpqSeEisaDmaEntry,
       "cpqSeEisaDmaSlotIndex": cpqSeEisaDmaSlotIndex,
       "cpqSeEisaDmaFunctIndex": cpqSeEisaDmaFunctIndex,
       "cpqSeEisaDmaAllocIndex": cpqSeEisaDmaAllocIndex,
       "cpqSeEisaDmaChannel": cpqSeEisaDmaChannel,
       "cpqSeEisaDmaShare": cpqSeEisaDmaShare,
       "cpqSeEisaDmaTiming": cpqSeEisaDmaTiming,
       "cpqSeEisaDmaXfer": cpqSeEisaDmaXfer,
       "cpqSeEisaDmaXferCount": cpqSeEisaDmaXferCount,
       "cpqSeEisaPortTable": cpqSeEisaPortTable,
       "cpqSeEisaPortEntry": cpqSeEisaPortEntry,
       "cpqSeEisaPortSlotIndex": cpqSeEisaPortSlotIndex,
       "cpqSeEisaPortFunctIndex": cpqSeEisaPortFunctIndex,
       "cpqSeEisaPortAllocIndex": cpqSeEisaPortAllocIndex,
       "cpqSeEisaPortAddr": cpqSeEisaPortAddr,
       "cpqSeEisaPortShare": cpqSeEisaPortShare,
       "cpqSeEisaPortSize": cpqSeEisaPortSize,
       "cpqSeEisaFreeFormTable": cpqSeEisaFreeFormTable,
       "cpqSeEisaFreeFormEntry": cpqSeEisaFreeFormEntry,
       "cpqSeEisaFreeFormSlotIndex": cpqSeEisaFreeFormSlotIndex,
       "cpqSeEisaFreeFormFunctIndex": cpqSeEisaFreeFormFunctIndex,
       "cpqSeEisaFreeFormValue": cpqSeEisaFreeFormValue,
       "cpqSeEisaInitTable": cpqSeEisaInitTable,
       "cpqSeEisaInitEntry": cpqSeEisaInitEntry,
       "cpqSeEisaInitSlotIndex": cpqSeEisaInitSlotIndex,
       "cpqSeEisaInitFunctIndex": cpqSeEisaInitFunctIndex,
       "cpqSeEisaInitAllocIndex": cpqSeEisaInitAllocIndex,
       "cpqSeEisaInitUseMask": cpqSeEisaInitUseMask,
       "cpqSeEisaInitAccess": cpqSeEisaInitAccess,
       "cpqSeEisaInitAddr": cpqSeEisaInitAddr,
       "cpqSeEisaInitValue": cpqSeEisaInitValue,
       "cpqSeEisaInitMask": cpqSeEisaInitMask,
       "cpqSeRom": cpqSeRom,
       "cpqSeSysRomVer": cpqSeSysRomVer,
       "cpqSeOptRomTable": cpqSeOptRomTable,
       "cpqSeOptRomEntry": cpqSeOptRomEntry,
       "cpqSeOptRomAddrIndex": cpqSeOptRomAddrIndex,
       "cpqSeOptRomSize": cpqSeOptRomSize,
       "cpqSeBiosRomDataRaw": cpqSeBiosRomDataRaw,
       "cpqSeRedundantSysRomVer": cpqSeRedundantSysRomVer,
       "cpqSeSmbiosVer": cpqSeSmbiosVer,
       "cpqSeMPFwVer": cpqSeMPFwVer,
       "cpqSeBMCFwVer": cpqSeBMCFwVer,
       "cpqSeHPVMFwVer": cpqSeHPVMFwVer,
       "cpqSeKeyboard": cpqSeKeyboard,
       "cpqSeKeyboardDesc": cpqSeKeyboardDesc,
       "cpqSeVideo": cpqSeVideo,
       "cpqSeVideoDesc": cpqSeVideoDesc,
       "cpqSeSerialPort": cpqSeSerialPort,
       "cpqSeSerialPortTable": cpqSeSerialPortTable,
       "cpqSeSerialPortEntry": cpqSeSerialPortEntry,
       "cpqSeSerialPortIndex": cpqSeSerialPortIndex,
       "cpqSeSerialPortAddr": cpqSeSerialPortAddr,
       "cpqSeSerialPortDesc": cpqSeSerialPortDesc,
       "cpqSeSerialPortHwLocation": cpqSeSerialPortHwLocation,
       "cpqSeParallelPort": cpqSeParallelPort,
       "cpqSeParallelPortTable": cpqSeParallelPortTable,
       "cpqSeParallelPortEntry": cpqSeParallelPortEntry,
       "cpqSeParallelPortIndex": cpqSeParallelPortIndex,
       "cpqSeParallelPortAddr": cpqSeParallelPortAddr,
       "cpqSeParallelPortDesc": cpqSeParallelPortDesc,
       "cpqSeParrallelPortHwLocation": cpqSeParrallelPortHwLocation,
       "cpqSeFloppyDisk": cpqSeFloppyDisk,
       "cpqSeFloppyDiskTable": cpqSeFloppyDiskTable,
       "cpqSeFloppyDiskEntry": cpqSeFloppyDiskEntry,
       "cpqSeFloppyDiskIndex": cpqSeFloppyDiskIndex,
       "cpqSeFloppyDiskType": cpqSeFloppyDiskType,
       "cpqSeFloppyDiskHwLocation": cpqSeFloppyDiskHwLocation,
       "cpqSeFixedDisk": cpqSeFixedDisk,
       "cpqSeFixedDiskTable": cpqSeFixedDiskTable,
       "cpqSeFixedDiskEntry": cpqSeFixedDiskEntry,
       "cpqSeFixedDiskIndex": cpqSeFixedDiskIndex,
       "cpqSeFixedDiskType": cpqSeFixedDiskType,
       "cpqSeFixedDiskCyls": cpqSeFixedDiskCyls,
       "cpqSeFixedDiskHeads": cpqSeFixedDiskHeads,
       "cpqSeFixedDiskSectors": cpqSeFixedDiskSectors,
       "cpqSeFixedDiskCapacity": cpqSeFixedDiskCapacity,
       "cpqSeFixedDiskHwLocation": cpqSeFixedDiskHwLocation,
       "cpqSePci": cpqSePci,
       "cpqSePciSlotTable": cpqSePciSlotTable,
       "cpqSePciSlotEntry": cpqSePciSlotEntry,
       "cpqSePciSlotBusNumberIndex": cpqSePciSlotBusNumberIndex,
       "cpqSePciSlotDeviceNumberIndex": cpqSePciSlotDeviceNumberIndex,
       "cpqSePciPhysSlot": cpqSePciPhysSlot,
       "cpqSePciSlotSubSystemID": cpqSePciSlotSubSystemID,
       "cpqSePciSlotBoardName": cpqSePciSlotBoardName,
       "cpqSePciSlotWidth": cpqSePciSlotWidth,
       "cpqSePciSlotSpeed": cpqSePciSlotSpeed,
       "cpqSePciSlotExtendedInfo": cpqSePciSlotExtendedInfo,
       "cpqSePciSlotType": cpqSePciSlotType,
       "cpqSePciSlotCurrentMode": cpqSePciSlotCurrentMode,
       "cpqSePciMaxSlotSpeed": cpqSePciMaxSlotSpeed,
       "cpqSePciXMaxSlotSpeed": cpqSePciXMaxSlotSpeed,
       "cpqSePciCurrentSlotSpeed": cpqSePciCurrentSlotSpeed,
       "cpqSePciHwLocation": cpqSePciHwLocation,
       "cpqSePciSlotIOCTablePtr": cpqSePciSlotIOCTablePtr,
       "cpqSePciSlotHeaderType": cpqSePciSlotHeaderType,
       "cpqSePciIsSlot0Embedded": cpqSePciIsSlot0Embedded,
       "cpqSePcieSlotMaxLinkSpeed": cpqSePcieSlotMaxLinkSpeed,
       "cpqSePcieSlotMaxLinkWidth": cpqSePcieSlotMaxLinkWidth,
       "cpqSePciFunctTable": cpqSePciFunctTable,
       "cpqSePciFunctEntry": cpqSePciFunctEntry,
       "cpqSePciFunctBusNumberIndex": cpqSePciFunctBusNumberIndex,
       "cpqSePciFunctDeviceNumberIndex": cpqSePciFunctDeviceNumberIndex,
       "cpqSePciFunctIndex": cpqSePciFunctIndex,
       "cpqSePciFunctClassCode": cpqSePciFunctClassCode,
       "cpqSePciFunctClassDescription": cpqSePciFunctClassDescription,
       "cpqSePciFunctDeviceID": cpqSePciFunctDeviceID,
       "cpqSePciFunctVendorID": cpqSePciFunctVendorID,
       "cpqSePciFunctRevID": cpqSePciFunctRevID,
       "cpqSePciFunctIntLine": cpqSePciFunctIntLine,
       "cpqSePciFunctDevStatus": cpqSePciFunctDevStatus,
       "cpqSePciFunctHwLocation": cpqSePciFunctHwLocation,
       "cpqSePcieFunctNegotiatedLinkSpeed": cpqSePcieFunctNegotiatedLinkSpeed,
       "cpqSePcieFunctNegotiatedLinkWidth": cpqSePcieFunctNegotiatedLinkWidth,
       "cpqSePcieFunctMaxLinkSpeed": cpqSePcieFunctMaxLinkSpeed,
       "cpqSePcieFunctMaxLinkWidth": cpqSePcieFunctMaxLinkWidth,
       "cpqSePciMemoryTable": cpqSePciMemoryTable,
       "cpqSePciMemoryEntry": cpqSePciMemoryEntry,
       "cpqSePciMemoryBusNumberIndex": cpqSePciMemoryBusNumberIndex,
       "cpqSePciMemoryDeviceNumberIndex": cpqSePciMemoryDeviceNumberIndex,
       "cpqSePciMemoryFunctionIndex": cpqSePciMemoryFunctionIndex,
       "cpqSePciMemoryIndex": cpqSePciMemoryIndex,
       "cpqSePciMemoryBaseAddr": cpqSePciMemoryBaseAddr,
       "cpqSePciMemoryType": cpqSePciMemoryType,
       "cpqSePciMemorySize": cpqSePciMemorySize,
       "cpqSePciMemoryHwLocation": cpqSePciMemoryHwLocation,
       "cpqSePciSegmentMode": cpqSePciSegmentMode,
       "cpqSePCCard": cpqSePCCard,
       "cpqSePCCardSlotTable": cpqSePCCardSlotTable,
       "cpqSePCCardSlotEntry": cpqSePCCardSlotEntry,
       "cpqSePCCardSlotIndex": cpqSePCCardSlotIndex,
       "cpqSePCCardCondition": cpqSePCCardCondition,
       "cpqSePCCardPhysLocation": cpqSePCCardPhysLocation,
       "cpqSePCCardSlotType": cpqSePCCardSlotType,
       "cpqSePCCardSlotWidth": cpqSePCCardSlotWidth,
       "cpqSePCCardSlotThermalCapacity": cpqSePCCardSlotThermalCapacity,
       "cpqSePCCardSlotThermalSensor": cpqSePCCardSlotThermalSensor,
       "cpqSePCCardSlotPowerState": cpqSePCCardSlotPowerState,
       "cpqSePCCardStatus": cpqSePCCardStatus,
       "cpqSePCCardDeviceInfo": cpqSePCCardDeviceInfo,
       "cpqSePCCardProductInfo": cpqSePCCardProductInfo,
       "cpqSePCCardSerialNumber": cpqSePCCardSerialNumber,
       "cpqSePCCardAssetTag": cpqSePCCardAssetTag,
       "cpqSeUSBPort": cpqSeUSBPort,
       "cpqSeUSBPortTable": cpqSeUSBPortTable,
       "cpqSeUSBPortEntry": cpqSeUSBPortEntry,
       "cpqSeUSBPortIndex": cpqSeUSBPortIndex,
       "cpqSeUSBPortType": cpqSeUSBPortType,
       "cpqSeUSBPortHwLocation": cpqSeUSBPortHwLocation,
       "cpqSeCell": cpqSeCell,
       "cpqSeCellTable": cpqSeCellTable,
       "cpqSeCellEntry": cpqSeCellEntry,
       "cpqSeCellUnitIndex": cpqSeCellUnitIndex,
       "cpqSeCellCabinetNumber": cpqSeCellCabinetNumber,
       "cpqSeCellCellNumber": cpqSeCellCellNumber,
       "cpqSeCellIOCTablePtr": cpqSeCellIOCTablePtr,
       "cpqSeCellPDHCFirmwareRevision": cpqSeCellPDHCFirmwareRevision,
       "cpqSeCellSysFwVersion": cpqSeCellSysFwVersion,
       "cpqSeCellBootInhibited": cpqSeCellBootInhibited,
       "cpqSeCellToScanBusConnectionStatus": cpqSeCellToScanBusConnectionStatus,
       "cpqSeCellHasCoreIO": cpqSeCellHasCoreIO,
       "cpqSeCellBoardSpeed": cpqSeCellBoardSpeed,
       "cpqSeCellPresent": cpqSeCellPresent,
       "cpqSeCellHasPower": cpqSeCellHasPower,
       "cpqSeCellReadyForReconfig": cpqSeCellReadyForReconfig,
       "cpqSeCellTotalMemory": cpqSeCellTotalMemory,
       "cpqSeCellLEDState": cpqSeCellLEDState,
       "cpqSeCellState": cpqSeCellState,
       "cpqSeCellCLMRequestPercentage": cpqSeCellCLMRequestPercentage,
       "cpqSeCellCLMRequestSize": cpqSeCellCLMRequestSize,
       "cpqSeCellCLMAllocatedSize": cpqSeCellCLMAllocatedSize,
       "cpqSeCellInterleaveAllocatedSize": cpqSeCellInterleaveAllocatedSize,
       "cpqSeCellHasInterleaveMem": cpqSeCellHasInterleaveMem,
       "cpqSeCellSerialNumber": cpqSeCellSerialNumber,
       "cpqSeCellCLMCondition": cpqSeCellCLMCondition,
       "cpqSeIOC": cpqSeIOC,
       "cpqSeIOCTable": cpqSeIOCTable,
       "cpqSeIOCEntry": cpqSeIOCEntry,
       "cpqSeIOCUnitIndex": cpqSeIOCUnitIndex,
       "cpqSeIOCCabinetNumber": cpqSeIOCCabinetNumber,
       "cpqSeIOCBayNumber": cpqSeIOCBayNumber,
       "cpqSeIOCIOCNumber": cpqSeIOCIOCNumber,
       "cpqSeIOCPowerState": cpqSeIOCPowerState,
       "cpqSeIOCLEDState": cpqSeIOCLEDState,
       "cpqSePartition": cpqSePartition,
       "cpqSePartitionTotalCPU": cpqSePartitionTotalCPU,
       "cpqSePartitionAvailableCellSlots": cpqSePartitionAvailableCellSlots,
       "cpqSePartitionInstalledCells": cpqSePartitionInstalledCells,
       "cpqSePartitionPoweredOnCells": cpqSePartitionPoweredOnCells,
       "cpqSePartitionReadyForReconfigCells": cpqSePartitionReadyForReconfigCells,
       "cpqSePartitionMemInterleavingType": cpqSePartitionMemInterleavingType,
       "cpqSePartitionName": cpqSePartitionName,
       "cpqSePartitionCoreCell": cpqSePartitionCoreCell,
       "cpqSePartitionCoreCellCabinet": cpqSePartitionCoreCellCabinet,
       "cpqSePartitionCLMRequestPercentage": cpqSePartitionCLMRequestPercentage,
       "cpqSePartitionCLMRequestSize": cpqSePartitionCLMRequestSize,
       "cpqSePartitionCLMAllocatedSize": cpqSePartitionCLMAllocatedSize,
       "cpqSePartitionInterleaveAllocatedSize": cpqSePartitionInterleaveAllocatedSize,
       "cpqSePartitionHasInterleaveMem": cpqSePartitionHasInterleaveMem,
       "cpqSePartitionNumber": cpqSePartitionNumber,
       "cpqSeCabinet": cpqSeCabinet,
       "cpqSeCabinetTable": cpqSeCabinetTable,
       "cpqSeCabinetEntry": cpqSeCabinetEntry,
       "cpqSeCabinetUnitIndex": cpqSeCabinetUnitIndex,
       "cpqSeCabinetCPULED": cpqSeCabinetCPULED,
       "cpqSeCabinetIOXLED": cpqSeCabinetIOXLED,
       "cpqSeCabinetTypeNum": cpqSeCabinetTypeNum,
       "cpqSeCabinetLED": cpqSeCabinetLED,
       "cpqSeComplex": cpqSeComplex,
       "cpqSeComplexUUID": cpqSeComplexUUID,
       "cpqSeComplexTotalCabinet": cpqSeComplexTotalCabinet,
       "cpqSeComplexComputeCabinet": cpqSeComplexComputeCabinet,
       "cpqSeComplexIOXCabinet": cpqSeComplexIOXCabinet,
       "cpqSeComplexName": cpqSeComplexName,
       "cpqSeComplexLockedProperty": cpqSeComplexLockedProperty,
       "cpqSeComplexCellSlotStatusTable": cpqSeComplexCellSlotStatusTable,
       "cpqSeComplexCellSlotStatusEntry": cpqSeComplexCellSlotStatusEntry,
       "cpqSeComplexCellSlotStatusIndex": cpqSeComplexCellSlotStatusIndex,
       "cpqSeComplexCellSlotStatusCabinetNo": cpqSeComplexCellSlotStatusCabinetNo,
       "cpqSeComplexCellSlotStatusSlotNo": cpqSeComplexCellSlotStatusSlotNo,
       "cpqSeComplexCellSlotStatus": cpqSeComplexCellSlotStatus,
       "cpqSeComplexCellSlotPartitionNo": cpqSeComplexCellSlotPartitionNo,
       "cpqSeComplexCellSlotPartitionName": cpqSeComplexCellSlotPartitionName,
       "cpqSeLED": cpqSeLED,
       "cpqSeLEDTable": cpqSeLEDTable,
       "cpqSeLEDEntry": cpqSeLEDEntry,
       "cpqSeLEDIndex": cpqSeLEDIndex,
       "cpqSeLEDState": cpqSeLEDState,
       "cpqSeLEDStateDuration": cpqSeLEDStateDuration,
       "cpqSeLEDLocationType": cpqSeLEDLocationType,
       "cpqSeLEDDescription": cpqSeLEDDescription,
       "cpqSeLEDHardwareLocation": cpqSeLEDHardwareLocation,
       "cpqSeUSBDevice": cpqSeUSBDevice,
       "cpqSeUSBDeviceType": cpqSeUSBDeviceType,
       "cpqSeUSBDeviceName": cpqSeUSBDeviceName}
)
