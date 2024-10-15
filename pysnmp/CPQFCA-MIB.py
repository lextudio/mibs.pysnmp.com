# SNMP MIB module (CPQFCA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQFCA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:22 2024
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

(cpqSsChassisName,
 cpqSsChassisTime) = mibBuilder.importSymbols(
    "CPQSTSYS-MIB",
    "cpqSsChassisName",
    "cpqSsChassisTime")

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

_CpqFibreArray_ObjectIdentity = ObjectIdentity
cpqFibreArray = _CpqFibreArray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16)
)
_CpqFcaMibRev_ObjectIdentity = ObjectIdentity
cpqFcaMibRev = _CpqFcaMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 1)
)


class _CpqFcaMibRevMajor_Type(Integer32):
    """Custom type cpqFcaMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqFcaMibRevMajor_Type.__name__ = "Integer32"
_CpqFcaMibRevMajor_Object = MibScalar
cpqFcaMibRevMajor = _CpqFcaMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 1, 1),
    _CpqFcaMibRevMajor_Type()
)
cpqFcaMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaMibRevMajor.setStatus("mandatory")


class _CpqFcaMibRevMinor_Type(Integer32):
    """Custom type cpqFcaMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcaMibRevMinor_Type.__name__ = "Integer32"
_CpqFcaMibRevMinor_Object = MibScalar
cpqFcaMibRevMinor = _CpqFcaMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 1, 2),
    _CpqFcaMibRevMinor_Type()
)
cpqFcaMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaMibRevMinor.setStatus("mandatory")


class _CpqFcaMibCondition_Type(Integer32):
    """Custom type cpqFcaMibCondition based on Integer32"""
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


_CpqFcaMibCondition_Type.__name__ = "Integer32"
_CpqFcaMibCondition_Object = MibScalar
cpqFcaMibCondition = _CpqFcaMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 1, 3),
    _CpqFcaMibCondition_Type()
)
cpqFcaMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaMibCondition.setStatus("mandatory")
_CpqFcaComponent_ObjectIdentity = ObjectIdentity
cpqFcaComponent = _CpqFcaComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2)
)
_CpqFcaInterface_ObjectIdentity = ObjectIdentity
cpqFcaInterface = _CpqFcaInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 1)
)
_CpqFcaOsCommon_ObjectIdentity = ObjectIdentity
cpqFcaOsCommon = _CpqFcaOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 1, 4)
)


class _CpqFcaOsCommonPollFreq_Type(Integer32):
    """Custom type cpqFcaOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcaOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqFcaOsCommonPollFreq_Object = MibScalar
cpqFcaOsCommonPollFreq = _CpqFcaOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 1, 4, 1),
    _CpqFcaOsCommonPollFreq_Type()
)
cpqFcaOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqFcaOsCommonPollFreq.setStatus("mandatory")
_CpqFcaOsCommonModuleTable_Object = MibTable
cpqFcaOsCommonModuleTable = _CpqFcaOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqFcaOsCommonModuleTable.setStatus("deprecated")
_CpqFcaOsCommonModuleEntry_Object = MibTableRow
cpqFcaOsCommonModuleEntry = _CpqFcaOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 1, 4, 2, 1)
)
cpqFcaOsCommonModuleEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcaOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqFcaOsCommonModuleEntry.setStatus("deprecated")


class _CpqFcaOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqFcaOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcaOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqFcaOsCommonModuleIndex_Object = MibTableColumn
cpqFcaOsCommonModuleIndex = _CpqFcaOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 1, 4, 2, 1, 1),
    _CpqFcaOsCommonModuleIndex_Type()
)
cpqFcaOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaOsCommonModuleIndex.setStatus("deprecated")


class _CpqFcaOsCommonModuleName_Type(DisplayString):
    """Custom type cpqFcaOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqFcaOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqFcaOsCommonModuleName_Object = MibTableColumn
cpqFcaOsCommonModuleName = _CpqFcaOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 1, 4, 2, 1, 2),
    _CpqFcaOsCommonModuleName_Type()
)
cpqFcaOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaOsCommonModuleName.setStatus("deprecated")


class _CpqFcaOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqFcaOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqFcaOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqFcaOsCommonModuleVersion_Object = MibTableColumn
cpqFcaOsCommonModuleVersion = _CpqFcaOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 1, 4, 2, 1, 3),
    _CpqFcaOsCommonModuleVersion_Type()
)
cpqFcaOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaOsCommonModuleVersion.setStatus("deprecated")


class _CpqFcaOsCommonModuleDate_Type(OctetString):
    """Custom type cpqFcaOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqFcaOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqFcaOsCommonModuleDate_Object = MibTableColumn
cpqFcaOsCommonModuleDate = _CpqFcaOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 1, 4, 2, 1, 4),
    _CpqFcaOsCommonModuleDate_Type()
)
cpqFcaOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaOsCommonModuleDate.setStatus("deprecated")


class _CpqFcaOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqFcaOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqFcaOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqFcaOsCommonModulePurpose_Object = MibTableColumn
cpqFcaOsCommonModulePurpose = _CpqFcaOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 1, 4, 2, 1, 5),
    _CpqFcaOsCommonModulePurpose_Type()
)
cpqFcaOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaOsCommonModulePurpose.setStatus("deprecated")
_CpqFcaCntlr_ObjectIdentity = ObjectIdentity
cpqFcaCntlr = _CpqFcaCntlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2)
)
_CpqFcaCntlrTable_Object = MibTable
cpqFcaCntlrTable = _CpqFcaCntlrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqFcaCntlrTable.setStatus("mandatory")
_CpqFcaCntlrEntry_Object = MibTableRow
cpqFcaCntlrEntry = _CpqFcaCntlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1)
)
cpqFcaCntlrEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcaCntlrBoxIndex"),
    (0, "CPQFCA-MIB", "cpqFcaCntlrBoxIoSlot"),
)
if mibBuilder.loadTexts:
    cpqFcaCntlrEntry.setStatus("mandatory")


class _CpqFcaCntlrBoxIndex_Type(Integer32):
    """Custom type cpqFcaCntlrBoxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcaCntlrBoxIndex_Type.__name__ = "Integer32"
_CpqFcaCntlrBoxIndex_Object = MibTableColumn
cpqFcaCntlrBoxIndex = _CpqFcaCntlrBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 1),
    _CpqFcaCntlrBoxIndex_Type()
)
cpqFcaCntlrBoxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrBoxIndex.setStatus("mandatory")


class _CpqFcaCntlrBoxIoSlot_Type(Integer32):
    """Custom type cpqFcaCntlrBoxIoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcaCntlrBoxIoSlot_Type.__name__ = "Integer32"
_CpqFcaCntlrBoxIoSlot_Object = MibTableColumn
cpqFcaCntlrBoxIoSlot = _CpqFcaCntlrBoxIoSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 2),
    _CpqFcaCntlrBoxIoSlot_Type()
)
cpqFcaCntlrBoxIoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrBoxIoSlot.setStatus("mandatory")


class _CpqFcaCntlrModel_Type(Integer32):
    """Custom type cpqFcaCntlrModel based on Integer32"""
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
        *(("fibreArray", 2),
          ("hsg80", 5),
          ("hsv110", 6),
          ("msa1000", 3),
          ("msa1510i", 9),
          ("msa20", 8),
          ("msa500G2", 7),
          ("other", 1),
          ("smartArrayClusterStorage", 4))
    )


_CpqFcaCntlrModel_Type.__name__ = "Integer32"
_CpqFcaCntlrModel_Object = MibTableColumn
cpqFcaCntlrModel = _CpqFcaCntlrModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 3),
    _CpqFcaCntlrModel_Type()
)
cpqFcaCntlrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrModel.setStatus("mandatory")


class _CpqFcaCntlrFWRev_Type(DisplayString):
    """Custom type cpqFcaCntlrFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqFcaCntlrFWRev_Type.__name__ = "DisplayString"
_CpqFcaCntlrFWRev_Object = MibTableColumn
cpqFcaCntlrFWRev = _CpqFcaCntlrFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 4),
    _CpqFcaCntlrFWRev_Type()
)
cpqFcaCntlrFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrFWRev.setStatus("mandatory")


class _CpqFcaCntlrStatus_Type(Integer32):
    """Custom type cpqFcaCntlrStatus based on Integer32"""
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
        *(("failed", 3),
          ("notConnected", 6),
          ("offline", 4),
          ("ok", 2),
          ("other", 1),
          ("redundantPathOffline", 5))
    )


_CpqFcaCntlrStatus_Type.__name__ = "Integer32"
_CpqFcaCntlrStatus_Object = MibTableColumn
cpqFcaCntlrStatus = _CpqFcaCntlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 5),
    _CpqFcaCntlrStatus_Type()
)
cpqFcaCntlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrStatus.setStatus("mandatory")


class _CpqFcaCntlrCondition_Type(Integer32):
    """Custom type cpqFcaCntlrCondition based on Integer32"""
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


_CpqFcaCntlrCondition_Type.__name__ = "Integer32"
_CpqFcaCntlrCondition_Object = MibTableColumn
cpqFcaCntlrCondition = _CpqFcaCntlrCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 6),
    _CpqFcaCntlrCondition_Type()
)
cpqFcaCntlrCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrCondition.setStatus("mandatory")


class _CpqFcaCntlrProductRev_Type(DisplayString):
    """Custom type cpqFcaCntlrProductRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_CpqFcaCntlrProductRev_Type.__name__ = "DisplayString"
_CpqFcaCntlrProductRev_Object = MibTableColumn
cpqFcaCntlrProductRev = _CpqFcaCntlrProductRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 7),
    _CpqFcaCntlrProductRev_Type()
)
cpqFcaCntlrProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrProductRev.setStatus("mandatory")


class _CpqFcaCntlrWorldWideName_Type(DisplayString):
    """Custom type cpqFcaCntlrWorldWideName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqFcaCntlrWorldWideName_Type.__name__ = "DisplayString"
_CpqFcaCntlrWorldWideName_Object = MibTableColumn
cpqFcaCntlrWorldWideName = _CpqFcaCntlrWorldWideName_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 8),
    _CpqFcaCntlrWorldWideName_Type()
)
cpqFcaCntlrWorldWideName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrWorldWideName.setStatus("mandatory")


class _CpqFcaCntlrSerialNumber_Type(DisplayString):
    """Custom type cpqFcaCntlrSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqFcaCntlrSerialNumber_Type.__name__ = "DisplayString"
_CpqFcaCntlrSerialNumber_Object = MibTableColumn
cpqFcaCntlrSerialNumber = _CpqFcaCntlrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 9),
    _CpqFcaCntlrSerialNumber_Type()
)
cpqFcaCntlrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrSerialNumber.setStatus("mandatory")


class _CpqFcaCntlrCurrentRole_Type(Integer32):
    """Custom type cpqFcaCntlrCurrentRole based on Integer32"""
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
        *(("active", 3),
          ("backup", 4),
          ("notDuplexed", 2),
          ("other", 1))
    )


_CpqFcaCntlrCurrentRole_Type.__name__ = "Integer32"
_CpqFcaCntlrCurrentRole_Object = MibTableColumn
cpqFcaCntlrCurrentRole = _CpqFcaCntlrCurrentRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 10),
    _CpqFcaCntlrCurrentRole_Type()
)
cpqFcaCntlrCurrentRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrCurrentRole.setStatus("mandatory")


class _CpqFcaCntlrRedundancyType_Type(Integer32):
    """Custom type cpqFcaCntlrRedundancyType based on Integer32"""
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
        *(("fwActiveActive", 5),
          ("fwActiveStandby", 3),
          ("fwPrimarySecondary", 4),
          ("notRedundant", 2),
          ("other", 1))
    )


_CpqFcaCntlrRedundancyType_Type.__name__ = "Integer32"
_CpqFcaCntlrRedundancyType_Object = MibTableColumn
cpqFcaCntlrRedundancyType = _CpqFcaCntlrRedundancyType_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 11),
    _CpqFcaCntlrRedundancyType_Type()
)
cpqFcaCntlrRedundancyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrRedundancyType.setStatus("mandatory")


class _CpqFcaCntlrRedundancyError_Type(Integer32):
    """Custom type cpqFcaCntlrRedundancyError based on Integer32"""
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
        *(("differentCache", 7),
          ("differentFirmware", 6),
          ("differentHardware", 4),
          ("expandInProgress", 12),
          ("noDrives", 9),
          ("noFailure", 2),
          ("noLink", 5),
          ("noRedundantController", 3),
          ("other", 1),
          ("otherCacheFailure", 8),
          ("otherNoDrives", 10),
          ("unsupportedDrives", 11))
    )


_CpqFcaCntlrRedundancyError_Type.__name__ = "Integer32"
_CpqFcaCntlrRedundancyError_Object = MibTableColumn
cpqFcaCntlrRedundancyError = _CpqFcaCntlrRedundancyError_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 12),
    _CpqFcaCntlrRedundancyError_Type()
)
cpqFcaCntlrRedundancyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrRedundancyError.setStatus("mandatory")
_CpqFcaCntlrBlinkTime_Type = Counter32
_CpqFcaCntlrBlinkTime_Object = MibTableColumn
cpqFcaCntlrBlinkTime = _CpqFcaCntlrBlinkTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 13),
    _CpqFcaCntlrBlinkTime_Type()
)
cpqFcaCntlrBlinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqFcaCntlrBlinkTime.setStatus("mandatory")


class _CpqFcaCntlrWorldWideNodeName_Type(DisplayString):
    """Custom type cpqFcaCntlrWorldWideNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqFcaCntlrWorldWideNodeName_Type.__name__ = "DisplayString"
_CpqFcaCntlrWorldWideNodeName_Object = MibTableColumn
cpqFcaCntlrWorldWideNodeName = _CpqFcaCntlrWorldWideNodeName_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 14),
    _CpqFcaCntlrWorldWideNodeName_Type()
)
cpqFcaCntlrWorldWideNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrWorldWideNodeName.setStatus("mandatory")


class _CpqFcaCntlrRebuildPriority_Type(Integer32):
    """Custom type cpqFcaCntlrRebuildPriority based on Integer32"""
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
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("other", 1))
    )


_CpqFcaCntlrRebuildPriority_Type.__name__ = "Integer32"
_CpqFcaCntlrRebuildPriority_Object = MibTableColumn
cpqFcaCntlrRebuildPriority = _CpqFcaCntlrRebuildPriority_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 15),
    _CpqFcaCntlrRebuildPriority_Type()
)
cpqFcaCntlrRebuildPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrRebuildPriority.setStatus("mandatory")


class _CpqFcaCntlrExpandPriority_Type(Integer32):
    """Custom type cpqFcaCntlrExpandPriority based on Integer32"""
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
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("other", 1))
    )


_CpqFcaCntlrExpandPriority_Type.__name__ = "Integer32"
_CpqFcaCntlrExpandPriority_Object = MibTableColumn
cpqFcaCntlrExpandPriority = _CpqFcaCntlrExpandPriority_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 1, 1, 16),
    _CpqFcaCntlrExpandPriority_Type()
)
cpqFcaCntlrExpandPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaCntlrExpandPriority.setStatus("mandatory")
_CpqFcaAccelTable_Object = MibTable
cpqFcaAccelTable = _CpqFcaAccelTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cpqFcaAccelTable.setStatus("mandatory")
_CpqFcaAccelEntry_Object = MibTableRow
cpqFcaAccelEntry = _CpqFcaAccelEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1)
)
cpqFcaAccelEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcaAccelBoxIndex"),
    (0, "CPQFCA-MIB", "cpqFcaAccelBoxIoSlot"),
)
if mibBuilder.loadTexts:
    cpqFcaAccelEntry.setStatus("mandatory")


class _CpqFcaAccelBoxIndex_Type(Integer32):
    """Custom type cpqFcaAccelBoxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcaAccelBoxIndex_Type.__name__ = "Integer32"
_CpqFcaAccelBoxIndex_Object = MibTableColumn
cpqFcaAccelBoxIndex = _CpqFcaAccelBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 1),
    _CpqFcaAccelBoxIndex_Type()
)
cpqFcaAccelBoxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelBoxIndex.setStatus("mandatory")


class _CpqFcaAccelBoxIoSlot_Type(Integer32):
    """Custom type cpqFcaAccelBoxIoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcaAccelBoxIoSlot_Type.__name__ = "Integer32"
_CpqFcaAccelBoxIoSlot_Object = MibTableColumn
cpqFcaAccelBoxIoSlot = _CpqFcaAccelBoxIoSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 2),
    _CpqFcaAccelBoxIoSlot_Type()
)
cpqFcaAccelBoxIoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelBoxIoSlot.setStatus("mandatory")


class _CpqFcaAccelStatus_Type(Integer32):
    """Custom type cpqFcaAccelStatus based on Integer32"""
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
        *(("enabled", 3),
          ("invalid", 2),
          ("other", 1),
          ("permDisabled", 5),
          ("tmpDisabled", 4))
    )


_CpqFcaAccelStatus_Type.__name__ = "Integer32"
_CpqFcaAccelStatus_Object = MibTableColumn
cpqFcaAccelStatus = _CpqFcaAccelStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 3),
    _CpqFcaAccelStatus_Type()
)
cpqFcaAccelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelStatus.setStatus("mandatory")


class _CpqFcaAccelBadData_Type(Integer32):
    """Custom type cpqFcaAccelBadData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("other", 1),
          ("possible", 3))
    )


_CpqFcaAccelBadData_Type.__name__ = "Integer32"
_CpqFcaAccelBadData_Object = MibTableColumn
cpqFcaAccelBadData = _CpqFcaAccelBadData_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 4),
    _CpqFcaAccelBadData_Type()
)
cpqFcaAccelBadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelBadData.setStatus("mandatory")


class _CpqFcaAccelErrCode_Type(Integer32):
    """Custom type cpqFcaAccelErrCode based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("badConfig", 3),
          ("badMirrorData", 8),
          ("configCmd", 11),
          ("disableCmd", 5),
          ("excessiveEccErrors", 17),
          ("expandInProgress", 12),
          ("invalid", 2),
          ("lowBattery", 4),
          ("noResources", 6),
          ("notConnected", 7),
          ("other", 1),
          ("postEccErrors", 19),
          ("readErr", 9),
          ("redundantCacheFailure", 16),
          ("redundantLowBattery", 14),
          ("redundantSizeMismatch", 15),
          ("snapshotInProgress", 13),
          ("writeErr", 10))
    )


_CpqFcaAccelErrCode_Type.__name__ = "Integer32"
_CpqFcaAccelErrCode_Object = MibTableColumn
cpqFcaAccelErrCode = _CpqFcaAccelErrCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 5),
    _CpqFcaAccelErrCode_Type()
)
cpqFcaAccelErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelErrCode.setStatus("mandatory")


class _CpqFcaAccelBatteryStatus_Type(Integer32):
    """Custom type cpqFcaAccelBatteryStatus based on Integer32"""
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
        *(("degraded", 5),
          ("failed", 4),
          ("notPresent", 6),
          ("ok", 2),
          ("other", 1),
          ("recharging", 3))
    )


_CpqFcaAccelBatteryStatus_Type.__name__ = "Integer32"
_CpqFcaAccelBatteryStatus_Object = MibTableColumn
cpqFcaAccelBatteryStatus = _CpqFcaAccelBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 6),
    _CpqFcaAccelBatteryStatus_Type()
)
cpqFcaAccelBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelBatteryStatus.setStatus("mandatory")
_CpqFcaAccelReadErrs_Type = Counter32
_CpqFcaAccelReadErrs_Object = MibTableColumn
cpqFcaAccelReadErrs = _CpqFcaAccelReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 7),
    _CpqFcaAccelReadErrs_Type()
)
cpqFcaAccelReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelReadErrs.setStatus("mandatory")
_CpqFcaAccelWriteErrs_Type = Counter32
_CpqFcaAccelWriteErrs_Object = MibTableColumn
cpqFcaAccelWriteErrs = _CpqFcaAccelWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 8),
    _CpqFcaAccelWriteErrs_Type()
)
cpqFcaAccelWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelWriteErrs.setStatus("mandatory")


class _CpqFcaAccelCondition_Type(Integer32):
    """Custom type cpqFcaAccelCondition based on Integer32"""
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


_CpqFcaAccelCondition_Type.__name__ = "Integer32"
_CpqFcaAccelCondition_Object = MibTableColumn
cpqFcaAccelCondition = _CpqFcaAccelCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 9),
    _CpqFcaAccelCondition_Type()
)
cpqFcaAccelCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelCondition.setStatus("mandatory")
_CpqFcaAccelWriteCache_Type = Integer32
_CpqFcaAccelWriteCache_Object = MibTableColumn
cpqFcaAccelWriteCache = _CpqFcaAccelWriteCache_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 10),
    _CpqFcaAccelWriteCache_Type()
)
cpqFcaAccelWriteCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelWriteCache.setStatus("mandatory")
_CpqFcaAccelReadCache_Type = Integer32
_CpqFcaAccelReadCache_Object = MibTableColumn
cpqFcaAccelReadCache = _CpqFcaAccelReadCache_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 11),
    _CpqFcaAccelReadCache_Type()
)
cpqFcaAccelReadCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelReadCache.setStatus("mandatory")


class _CpqFcaAccelSerialNumber_Type(DisplayString):
    """Custom type cpqFcaAccelSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqFcaAccelSerialNumber_Type.__name__ = "DisplayString"
_CpqFcaAccelSerialNumber_Object = MibTableColumn
cpqFcaAccelSerialNumber = _CpqFcaAccelSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 12),
    _CpqFcaAccelSerialNumber_Type()
)
cpqFcaAccelSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelSerialNumber.setStatus("mandatory")
_CpqFcaAccelTotalMemory_Type = Integer32
_CpqFcaAccelTotalMemory_Object = MibTableColumn
cpqFcaAccelTotalMemory = _CpqFcaAccelTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 13),
    _CpqFcaAccelTotalMemory_Type()
)
cpqFcaAccelTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelTotalMemory.setStatus("mandatory")


class _CpqFcaAccelFailedBatteries_Type(OctetString):
    """Custom type cpqFcaAccelFailedBatteries based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqFcaAccelFailedBatteries_Type.__name__ = "OctetString"
_CpqFcaAccelFailedBatteries_Object = MibTableColumn
cpqFcaAccelFailedBatteries = _CpqFcaAccelFailedBatteries_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 2, 2, 1, 14),
    _CpqFcaAccelFailedBatteries_Type()
)
cpqFcaAccelFailedBatteries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaAccelFailedBatteries.setStatus("mandatory")
_CpqFcaLogDrv_ObjectIdentity = ObjectIdentity
cpqFcaLogDrv = _CpqFcaLogDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3)
)
_CpqFcaLogDrvTable_Object = MibTable
cpqFcaLogDrvTable = _CpqFcaLogDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqFcaLogDrvTable.setStatus("mandatory")
_CpqFcaLogDrvEntry_Object = MibTableRow
cpqFcaLogDrvEntry = _CpqFcaLogDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1)
)
cpqFcaLogDrvEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcaLogDrvBoxIndex"),
    (0, "CPQFCA-MIB", "cpqFcaLogDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqFcaLogDrvEntry.setStatus("mandatory")


class _CpqFcaLogDrvBoxIndex_Type(Integer32):
    """Custom type cpqFcaLogDrvBoxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcaLogDrvBoxIndex_Type.__name__ = "Integer32"
_CpqFcaLogDrvBoxIndex_Object = MibTableColumn
cpqFcaLogDrvBoxIndex = _CpqFcaLogDrvBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 1),
    _CpqFcaLogDrvBoxIndex_Type()
)
cpqFcaLogDrvBoxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvBoxIndex.setStatus("mandatory")


class _CpqFcaLogDrvIndex_Type(Integer32):
    """Custom type cpqFcaLogDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcaLogDrvIndex_Type.__name__ = "Integer32"
_CpqFcaLogDrvIndex_Object = MibTableColumn
cpqFcaLogDrvIndex = _CpqFcaLogDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 2),
    _CpqFcaLogDrvIndex_Type()
)
cpqFcaLogDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvIndex.setStatus("mandatory")


class _CpqFcaLogDrvFaultTol_Type(Integer32):
    """Custom type cpqFcaLogDrvFaultTol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("advancedDataGuard", 7),
          ("dataGuard", 4),
          ("distribDataGuard", 5),
          ("mirroring", 3),
          ("none", 2),
          ("other", 1))
    )


_CpqFcaLogDrvFaultTol_Type.__name__ = "Integer32"
_CpqFcaLogDrvFaultTol_Object = MibTableColumn
cpqFcaLogDrvFaultTol = _CpqFcaLogDrvFaultTol_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 3),
    _CpqFcaLogDrvFaultTol_Type()
)
cpqFcaLogDrvFaultTol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvFaultTol.setStatus("mandatory")


class _CpqFcaLogDrvStatus_Type(Integer32):
    """Custom type cpqFcaLogDrvStatus based on Integer32"""
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
        *(("badConnect", 9),
          ("expanding", 12),
          ("failed", 3),
          ("hardError", 15),
          ("notAvailable", 13),
          ("ok", 2),
          ("other", 1),
          ("overheating", 10),
          ("queuedForExpansion", 14),
          ("readyForRebuild", 6),
          ("rebuilding", 7),
          ("recovering", 5),
          ("shutdown", 11),
          ("unconfigured", 4),
          ("wrongDrive", 8))
    )


_CpqFcaLogDrvStatus_Type.__name__ = "Integer32"
_CpqFcaLogDrvStatus_Object = MibTableColumn
cpqFcaLogDrvStatus = _CpqFcaLogDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 4),
    _CpqFcaLogDrvStatus_Type()
)
cpqFcaLogDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvStatus.setStatus("mandatory")
_CpqFcaLogDrvAutoRel_Type = Integer32
_CpqFcaLogDrvAutoRel_Object = MibTableColumn
cpqFcaLogDrvAutoRel = _CpqFcaLogDrvAutoRel_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 5),
    _CpqFcaLogDrvAutoRel_Type()
)
cpqFcaLogDrvAutoRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvAutoRel.setStatus("mandatory")
_CpqFcaLogDrvPercentRebuild_Type = Gauge32
_CpqFcaLogDrvPercentRebuild_Object = MibTableColumn
cpqFcaLogDrvPercentRebuild = _CpqFcaLogDrvPercentRebuild_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 6),
    _CpqFcaLogDrvPercentRebuild_Type()
)
cpqFcaLogDrvPercentRebuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvPercentRebuild.setStatus("mandatory")


class _CpqFcaLogDrvHasAccel_Type(Integer32):
    """Custom type cpqFcaLogDrvHasAccel based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("other", 1),
          ("unavailable", 2))
    )


_CpqFcaLogDrvHasAccel_Type.__name__ = "Integer32"
_CpqFcaLogDrvHasAccel_Object = MibTableColumn
cpqFcaLogDrvHasAccel = _CpqFcaLogDrvHasAccel_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 7),
    _CpqFcaLogDrvHasAccel_Type()
)
cpqFcaLogDrvHasAccel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvHasAccel.setStatus("mandatory")


class _CpqFcaLogDrvAvailSpares_Type(OctetString):
    """Custom type cpqFcaLogDrvAvailSpares based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqFcaLogDrvAvailSpares_Type.__name__ = "OctetString"
_CpqFcaLogDrvAvailSpares_Object = MibTableColumn
cpqFcaLogDrvAvailSpares = _CpqFcaLogDrvAvailSpares_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 8),
    _CpqFcaLogDrvAvailSpares_Type()
)
cpqFcaLogDrvAvailSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvAvailSpares.setStatus("mandatory")


class _CpqFcaLogDrvSize_Type(Integer32):
    """Custom type cpqFcaLogDrvSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqFcaLogDrvSize_Type.__name__ = "Integer32"
_CpqFcaLogDrvSize_Object = MibTableColumn
cpqFcaLogDrvSize = _CpqFcaLogDrvSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 9),
    _CpqFcaLogDrvSize_Type()
)
cpqFcaLogDrvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvSize.setStatus("mandatory")


class _CpqFcaLogDrvPhyDrvIDs_Type(OctetString):
    """Custom type cpqFcaLogDrvPhyDrvIDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqFcaLogDrvPhyDrvIDs_Type.__name__ = "OctetString"
_CpqFcaLogDrvPhyDrvIDs_Object = MibTableColumn
cpqFcaLogDrvPhyDrvIDs = _CpqFcaLogDrvPhyDrvIDs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 10),
    _CpqFcaLogDrvPhyDrvIDs_Type()
)
cpqFcaLogDrvPhyDrvIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvPhyDrvIDs.setStatus("mandatory")


class _CpqFcaLogDrvCondition_Type(Integer32):
    """Custom type cpqFcaLogDrvCondition based on Integer32"""
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


_CpqFcaLogDrvCondition_Type.__name__ = "Integer32"
_CpqFcaLogDrvCondition_Object = MibTableColumn
cpqFcaLogDrvCondition = _CpqFcaLogDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 11),
    _CpqFcaLogDrvCondition_Type()
)
cpqFcaLogDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvCondition.setStatus("mandatory")
_CpqFcaLogDrvStripeSize_Type = Integer32
_CpqFcaLogDrvStripeSize_Object = MibTableColumn
cpqFcaLogDrvStripeSize = _CpqFcaLogDrvStripeSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 12),
    _CpqFcaLogDrvStripeSize_Type()
)
cpqFcaLogDrvStripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvStripeSize.setStatus("mandatory")


class _CpqFcaLogDrvOsName_Type(DisplayString):
    """Custom type cpqFcaLogDrvOsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqFcaLogDrvOsName_Type.__name__ = "DisplayString"
_CpqFcaLogDrvOsName_Object = MibTableColumn
cpqFcaLogDrvOsName = _CpqFcaLogDrvOsName_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 13),
    _CpqFcaLogDrvOsName_Type()
)
cpqFcaLogDrvOsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvOsName.setStatus("mandatory")
_CpqFcaLogDrvBlinkTime_Type = Counter32
_CpqFcaLogDrvBlinkTime_Object = MibTableColumn
cpqFcaLogDrvBlinkTime = _CpqFcaLogDrvBlinkTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 14),
    _CpqFcaLogDrvBlinkTime_Type()
)
cpqFcaLogDrvBlinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqFcaLogDrvBlinkTime.setStatus("mandatory")


class _CpqFcaLogDrvSpareReplaceMap_Type(OctetString):
    """Custom type cpqFcaLogDrvSpareReplaceMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CpqFcaLogDrvSpareReplaceMap_Type.__name__ = "OctetString"
_CpqFcaLogDrvSpareReplaceMap_Object = MibTableColumn
cpqFcaLogDrvSpareReplaceMap = _CpqFcaLogDrvSpareReplaceMap_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 15),
    _CpqFcaLogDrvSpareReplaceMap_Type()
)
cpqFcaLogDrvSpareReplaceMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvSpareReplaceMap.setStatus("mandatory")
_CpqFcaLogDrvRebuildingPhyDrv_Type = Integer32
_CpqFcaLogDrvRebuildingPhyDrv_Object = MibTableColumn
cpqFcaLogDrvRebuildingPhyDrv = _CpqFcaLogDrvRebuildingPhyDrv_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 16),
    _CpqFcaLogDrvRebuildingPhyDrv_Type()
)
cpqFcaLogDrvRebuildingPhyDrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvRebuildingPhyDrv.setStatus("mandatory")
_CpqFcaLogDrvSnapshotResourceDrvIndex_Type = Integer32
_CpqFcaLogDrvSnapshotResourceDrvIndex_Object = MibTableColumn
cpqFcaLogDrvSnapshotResourceDrvIndex = _CpqFcaLogDrvSnapshotResourceDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 17),
    _CpqFcaLogDrvSnapshotResourceDrvIndex_Type()
)
cpqFcaLogDrvSnapshotResourceDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvSnapshotResourceDrvIndex.setStatus("mandatory")
_CpqFcaLogDrvSnapshotSourceDrvIndex_Type = Integer32
_CpqFcaLogDrvSnapshotSourceDrvIndex_Object = MibTableColumn
cpqFcaLogDrvSnapshotSourceDrvIndex = _CpqFcaLogDrvSnapshotSourceDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 18),
    _CpqFcaLogDrvSnapshotSourceDrvIndex_Type()
)
cpqFcaLogDrvSnapshotSourceDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvSnapshotSourceDrvIndex.setStatus("mandatory")
_CpqFcaLogDrvPreferredPath_Type = Integer32
_CpqFcaLogDrvPreferredPath_Object = MibTableColumn
cpqFcaLogDrvPreferredPath = _CpqFcaLogDrvPreferredPath_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 19),
    _CpqFcaLogDrvPreferredPath_Type()
)
cpqFcaLogDrvPreferredPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvPreferredPath.setStatus("mandatory")
_CpqFcaLogDrvCurrentPath_Type = Integer32
_CpqFcaLogDrvCurrentPath_Object = MibTableColumn
cpqFcaLogDrvCurrentPath = _CpqFcaLogDrvCurrentPath_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 3, 1, 1, 20),
    _CpqFcaLogDrvCurrentPath_Type()
)
cpqFcaLogDrvCurrentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaLogDrvCurrentPath.setStatus("mandatory")
_CpqFcaSpareDrv_ObjectIdentity = ObjectIdentity
cpqFcaSpareDrv = _CpqFcaSpareDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4)
)
_CpqFcaSpareTable_Object = MibTable
cpqFcaSpareTable = _CpqFcaSpareTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqFcaSpareTable.setStatus("mandatory")
_CpqFcaSpareEntry_Object = MibTableRow
cpqFcaSpareEntry = _CpqFcaSpareEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1)
)
cpqFcaSpareEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcaSpareBoxIndex"),
    (0, "CPQFCA-MIB", "cpqFcaSparePhyDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqFcaSpareEntry.setStatus("mandatory")


class _CpqFcaSpareBoxIndex_Type(Integer32):
    """Custom type cpqFcaSpareBoxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcaSpareBoxIndex_Type.__name__ = "Integer32"
_CpqFcaSpareBoxIndex_Object = MibTableColumn
cpqFcaSpareBoxIndex = _CpqFcaSpareBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1, 1),
    _CpqFcaSpareBoxIndex_Type()
)
cpqFcaSpareBoxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaSpareBoxIndex.setStatus("mandatory")


class _CpqFcaSparePhyDrvIndex_Type(Integer32):
    """Custom type cpqFcaSparePhyDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcaSparePhyDrvIndex_Type.__name__ = "Integer32"
_CpqFcaSparePhyDrvIndex_Object = MibTableColumn
cpqFcaSparePhyDrvIndex = _CpqFcaSparePhyDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1, 2),
    _CpqFcaSparePhyDrvIndex_Type()
)
cpqFcaSparePhyDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaSparePhyDrvIndex.setStatus("mandatory")


class _CpqFcaSpareStatus_Type(Integer32):
    """Custom type cpqFcaSpareStatus based on Integer32"""
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
        *(("active", 5),
          ("building", 4),
          ("failed", 3),
          ("inactive", 2),
          ("other", 1))
    )


_CpqFcaSpareStatus_Type.__name__ = "Integer32"
_CpqFcaSpareStatus_Object = MibTableColumn
cpqFcaSpareStatus = _CpqFcaSpareStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1, 3),
    _CpqFcaSpareStatus_Type()
)
cpqFcaSpareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaSpareStatus.setStatus("mandatory")
_CpqFcaSpareReplacedDrvBay_Type = Integer32
_CpqFcaSpareReplacedDrvBay_Object = MibTableColumn
cpqFcaSpareReplacedDrvBay = _CpqFcaSpareReplacedDrvBay_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1, 4),
    _CpqFcaSpareReplacedDrvBay_Type()
)
cpqFcaSpareReplacedDrvBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaSpareReplacedDrvBay.setStatus("mandatory")
_CpqFcaSparePercentRebuild_Type = Gauge32
_CpqFcaSparePercentRebuild_Object = MibTableColumn
cpqFcaSparePercentRebuild = _CpqFcaSparePercentRebuild_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1, 5),
    _CpqFcaSparePercentRebuild_Type()
)
cpqFcaSparePercentRebuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaSparePercentRebuild.setStatus("mandatory")


class _CpqFcaSpareCondition_Type(Integer32):
    """Custom type cpqFcaSpareCondition based on Integer32"""
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


_CpqFcaSpareCondition_Type.__name__ = "Integer32"
_CpqFcaSpareCondition_Object = MibTableColumn
cpqFcaSpareCondition = _CpqFcaSpareCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1, 6),
    _CpqFcaSpareCondition_Type()
)
cpqFcaSpareCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaSpareCondition.setStatus("mandatory")
_CpqFcaSpareBusNumber_Type = Integer32
_CpqFcaSpareBusNumber_Object = MibTableColumn
cpqFcaSpareBusNumber = _CpqFcaSpareBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1, 7),
    _CpqFcaSpareBusNumber_Type()
)
cpqFcaSpareBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaSpareBusNumber.setStatus("mandatory")


class _CpqFcaSpareBay_Type(Integer32):
    """Custom type cpqFcaSpareBay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcaSpareBay_Type.__name__ = "Integer32"
_CpqFcaSpareBay_Object = MibTableColumn
cpqFcaSpareBay = _CpqFcaSpareBay_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1, 8),
    _CpqFcaSpareBay_Type()
)
cpqFcaSpareBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaSpareBay.setStatus("mandatory")
_CpqFcaSpareReplacedDrvBusNumber_Type = Integer32
_CpqFcaSpareReplacedDrvBusNumber_Object = MibTableColumn
cpqFcaSpareReplacedDrvBusNumber = _CpqFcaSpareReplacedDrvBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1, 9),
    _CpqFcaSpareReplacedDrvBusNumber_Type()
)
cpqFcaSpareReplacedDrvBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaSpareReplacedDrvBusNumber.setStatus("mandatory")


class _CpqFcaSpareLocationString_Type(DisplayString):
    """Custom type cpqFcaSpareLocationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqFcaSpareLocationString_Type.__name__ = "DisplayString"
_CpqFcaSpareLocationString_Object = MibTableColumn
cpqFcaSpareLocationString = _CpqFcaSpareLocationString_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 4, 1, 1, 10),
    _CpqFcaSpareLocationString_Type()
)
cpqFcaSpareLocationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaSpareLocationString.setStatus("mandatory")
_CpqFcaPhyDrv_ObjectIdentity = ObjectIdentity
cpqFcaPhyDrv = _CpqFcaPhyDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5)
)
_CpqFcaPhyDrvTable_Object = MibTable
cpqFcaPhyDrvTable = _CpqFcaPhyDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqFcaPhyDrvTable.setStatus("mandatory")
_CpqFcaPhyDrvEntry_Object = MibTableRow
cpqFcaPhyDrvEntry = _CpqFcaPhyDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1)
)
cpqFcaPhyDrvEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcaPhyDrvBoxIndex"),
    (0, "CPQFCA-MIB", "cpqFcaPhyDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqFcaPhyDrvEntry.setStatus("mandatory")


class _CpqFcaPhyDrvBoxIndex_Type(Integer32):
    """Custom type cpqFcaPhyDrvBoxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcaPhyDrvBoxIndex_Type.__name__ = "Integer32"
_CpqFcaPhyDrvBoxIndex_Object = MibTableColumn
cpqFcaPhyDrvBoxIndex = _CpqFcaPhyDrvBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 1),
    _CpqFcaPhyDrvBoxIndex_Type()
)
cpqFcaPhyDrvBoxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvBoxIndex.setStatus("mandatory")


class _CpqFcaPhyDrvIndex_Type(Integer32):
    """Custom type cpqFcaPhyDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcaPhyDrvIndex_Type.__name__ = "Integer32"
_CpqFcaPhyDrvIndex_Object = MibTableColumn
cpqFcaPhyDrvIndex = _CpqFcaPhyDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 2),
    _CpqFcaPhyDrvIndex_Type()
)
cpqFcaPhyDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvIndex.setStatus("mandatory")


class _CpqFcaPhyDrvModel_Type(DisplayString):
    """Custom type cpqFcaPhyDrvModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_CpqFcaPhyDrvModel_Type.__name__ = "DisplayString"
_CpqFcaPhyDrvModel_Object = MibTableColumn
cpqFcaPhyDrvModel = _CpqFcaPhyDrvModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 3),
    _CpqFcaPhyDrvModel_Type()
)
cpqFcaPhyDrvModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvModel.setStatus("mandatory")


class _CpqFcaPhyDrvFWRev_Type(DisplayString):
    """Custom type cpqFcaPhyDrvFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqFcaPhyDrvFWRev_Type.__name__ = "DisplayString"
_CpqFcaPhyDrvFWRev_Object = MibTableColumn
cpqFcaPhyDrvFWRev = _CpqFcaPhyDrvFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 4),
    _CpqFcaPhyDrvFWRev_Type()
)
cpqFcaPhyDrvFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvFWRev.setStatus("mandatory")


class _CpqFcaPhyDrvBay_Type(Integer32):
    """Custom type cpqFcaPhyDrvBay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcaPhyDrvBay_Type.__name__ = "Integer32"
_CpqFcaPhyDrvBay_Object = MibTableColumn
cpqFcaPhyDrvBay = _CpqFcaPhyDrvBay_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 5),
    _CpqFcaPhyDrvBay_Type()
)
cpqFcaPhyDrvBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvBay.setStatus("mandatory")


class _CpqFcaPhyDrvStatus_Type(Integer32):
    """Custom type cpqFcaPhyDrvStatus based on Integer32"""
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
        *(("failed", 6),
          ("ok", 3),
          ("other", 1),
          ("predictiveFailure", 5),
          ("threshExceeded", 4),
          ("unconfigured", 2),
          ("unsupportedDrive", 7))
    )


_CpqFcaPhyDrvStatus_Type.__name__ = "Integer32"
_CpqFcaPhyDrvStatus_Object = MibTableColumn
cpqFcaPhyDrvStatus = _CpqFcaPhyDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 6),
    _CpqFcaPhyDrvStatus_Type()
)
cpqFcaPhyDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvStatus.setStatus("mandatory")
_CpqFcaPhyDrvUsedReallocs_Type = Counter32
_CpqFcaPhyDrvUsedReallocs_Object = MibTableColumn
cpqFcaPhyDrvUsedReallocs = _CpqFcaPhyDrvUsedReallocs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 7),
    _CpqFcaPhyDrvUsedReallocs_Type()
)
cpqFcaPhyDrvUsedReallocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvUsedReallocs.setStatus("mandatory")
_CpqFcaPhyDrvRefHours_Type = Counter32
_CpqFcaPhyDrvRefHours_Object = MibTableColumn
cpqFcaPhyDrvRefHours = _CpqFcaPhyDrvRefHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 8),
    _CpqFcaPhyDrvRefHours_Type()
)
cpqFcaPhyDrvRefHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvRefHours.setStatus("mandatory")
_CpqFcaPhyDrvHReads_Type = Counter32
_CpqFcaPhyDrvHReads_Object = MibTableColumn
cpqFcaPhyDrvHReads = _CpqFcaPhyDrvHReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 9),
    _CpqFcaPhyDrvHReads_Type()
)
cpqFcaPhyDrvHReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvHReads.setStatus("mandatory")
_CpqFcaPhyDrvReads_Type = Counter32
_CpqFcaPhyDrvReads_Object = MibTableColumn
cpqFcaPhyDrvReads = _CpqFcaPhyDrvReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 10),
    _CpqFcaPhyDrvReads_Type()
)
cpqFcaPhyDrvReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvReads.setStatus("mandatory")
_CpqFcaPhyDrvHWrites_Type = Counter32
_CpqFcaPhyDrvHWrites_Object = MibTableColumn
cpqFcaPhyDrvHWrites = _CpqFcaPhyDrvHWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 11),
    _CpqFcaPhyDrvHWrites_Type()
)
cpqFcaPhyDrvHWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvHWrites.setStatus("mandatory")
_CpqFcaPhyDrvWrites_Type = Counter32
_CpqFcaPhyDrvWrites_Object = MibTableColumn
cpqFcaPhyDrvWrites = _CpqFcaPhyDrvWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 12),
    _CpqFcaPhyDrvWrites_Type()
)
cpqFcaPhyDrvWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvWrites.setStatus("mandatory")
_CpqFcaPhyDrvHSeeks_Type = Counter32
_CpqFcaPhyDrvHSeeks_Object = MibTableColumn
cpqFcaPhyDrvHSeeks = _CpqFcaPhyDrvHSeeks_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 13),
    _CpqFcaPhyDrvHSeeks_Type()
)
cpqFcaPhyDrvHSeeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvHSeeks.setStatus("mandatory")
_CpqFcaPhyDrvSeeks_Type = Counter32
_CpqFcaPhyDrvSeeks_Object = MibTableColumn
cpqFcaPhyDrvSeeks = _CpqFcaPhyDrvSeeks_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 14),
    _CpqFcaPhyDrvSeeks_Type()
)
cpqFcaPhyDrvSeeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvSeeks.setStatus("mandatory")
_CpqFcaPhyDrvHardReadErrs_Type = Counter32
_CpqFcaPhyDrvHardReadErrs_Object = MibTableColumn
cpqFcaPhyDrvHardReadErrs = _CpqFcaPhyDrvHardReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 15),
    _CpqFcaPhyDrvHardReadErrs_Type()
)
cpqFcaPhyDrvHardReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvHardReadErrs.setStatus("mandatory")
_CpqFcaPhyDrvRecvReadErrs_Type = Counter32
_CpqFcaPhyDrvRecvReadErrs_Object = MibTableColumn
cpqFcaPhyDrvRecvReadErrs = _CpqFcaPhyDrvRecvReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 16),
    _CpqFcaPhyDrvRecvReadErrs_Type()
)
cpqFcaPhyDrvRecvReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvRecvReadErrs.setStatus("mandatory")
_CpqFcaPhyDrvHardWriteErrs_Type = Counter32
_CpqFcaPhyDrvHardWriteErrs_Object = MibTableColumn
cpqFcaPhyDrvHardWriteErrs = _CpqFcaPhyDrvHardWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 17),
    _CpqFcaPhyDrvHardWriteErrs_Type()
)
cpqFcaPhyDrvHardWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvHardWriteErrs.setStatus("mandatory")
_CpqFcaPhyDrvRecvWriteErrs_Type = Counter32
_CpqFcaPhyDrvRecvWriteErrs_Object = MibTableColumn
cpqFcaPhyDrvRecvWriteErrs = _CpqFcaPhyDrvRecvWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 18),
    _CpqFcaPhyDrvRecvWriteErrs_Type()
)
cpqFcaPhyDrvRecvWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvRecvWriteErrs.setStatus("mandatory")
_CpqFcaPhyDrvHSeekErrs_Type = Counter32
_CpqFcaPhyDrvHSeekErrs_Object = MibTableColumn
cpqFcaPhyDrvHSeekErrs = _CpqFcaPhyDrvHSeekErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 19),
    _CpqFcaPhyDrvHSeekErrs_Type()
)
cpqFcaPhyDrvHSeekErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvHSeekErrs.setStatus("mandatory")
_CpqFcaPhyDrvSeekErrs_Type = Counter32
_CpqFcaPhyDrvSeekErrs_Object = MibTableColumn
cpqFcaPhyDrvSeekErrs = _CpqFcaPhyDrvSeekErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 20),
    _CpqFcaPhyDrvSeekErrs_Type()
)
cpqFcaPhyDrvSeekErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvSeekErrs.setStatus("mandatory")
_CpqFcaPhyDrvSpinupTime_Type = Integer32
_CpqFcaPhyDrvSpinupTime_Object = MibTableColumn
cpqFcaPhyDrvSpinupTime = _CpqFcaPhyDrvSpinupTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 21),
    _CpqFcaPhyDrvSpinupTime_Type()
)
cpqFcaPhyDrvSpinupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvSpinupTime.setStatus("mandatory")
_CpqFcaPhyDrvFunctTest1_Type = Gauge32
_CpqFcaPhyDrvFunctTest1_Object = MibTableColumn
cpqFcaPhyDrvFunctTest1 = _CpqFcaPhyDrvFunctTest1_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 22),
    _CpqFcaPhyDrvFunctTest1_Type()
)
cpqFcaPhyDrvFunctTest1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvFunctTest1.setStatus("deprecated")
_CpqFcaPhyDrvFunctTest2_Type = Gauge32
_CpqFcaPhyDrvFunctTest2_Object = MibTableColumn
cpqFcaPhyDrvFunctTest2 = _CpqFcaPhyDrvFunctTest2_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 23),
    _CpqFcaPhyDrvFunctTest2_Type()
)
cpqFcaPhyDrvFunctTest2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvFunctTest2.setStatus("deprecated")
_CpqFcaPhyDrvFunctTest3_Type = Gauge32
_CpqFcaPhyDrvFunctTest3_Object = MibTableColumn
cpqFcaPhyDrvFunctTest3 = _CpqFcaPhyDrvFunctTest3_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 24),
    _CpqFcaPhyDrvFunctTest3_Type()
)
cpqFcaPhyDrvFunctTest3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvFunctTest3.setStatus("deprecated")
_CpqFcaPhyDrvOtherTimeouts_Type = Counter32
_CpqFcaPhyDrvOtherTimeouts_Object = MibTableColumn
cpqFcaPhyDrvOtherTimeouts = _CpqFcaPhyDrvOtherTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 25),
    _CpqFcaPhyDrvOtherTimeouts_Type()
)
cpqFcaPhyDrvOtherTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvOtherTimeouts.setStatus("mandatory")
_CpqFcaPhyDrvBadRecvReads_Type = Counter32
_CpqFcaPhyDrvBadRecvReads_Object = MibTableColumn
cpqFcaPhyDrvBadRecvReads = _CpqFcaPhyDrvBadRecvReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 26),
    _CpqFcaPhyDrvBadRecvReads_Type()
)
cpqFcaPhyDrvBadRecvReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvBadRecvReads.setStatus("mandatory")
_CpqFcaPhyDrvBadRecvWrites_Type = Counter32
_CpqFcaPhyDrvBadRecvWrites_Object = MibTableColumn
cpqFcaPhyDrvBadRecvWrites = _CpqFcaPhyDrvBadRecvWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 27),
    _CpqFcaPhyDrvBadRecvWrites_Type()
)
cpqFcaPhyDrvBadRecvWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvBadRecvWrites.setStatus("mandatory")
_CpqFcaPhyDrvFormatErrs_Type = Counter32
_CpqFcaPhyDrvFormatErrs_Object = MibTableColumn
cpqFcaPhyDrvFormatErrs = _CpqFcaPhyDrvFormatErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 28),
    _CpqFcaPhyDrvFormatErrs_Type()
)
cpqFcaPhyDrvFormatErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvFormatErrs.setStatus("mandatory")
_CpqFcaPhyDrvNotReadyErrs_Type = Counter32
_CpqFcaPhyDrvNotReadyErrs_Object = MibTableColumn
cpqFcaPhyDrvNotReadyErrs = _CpqFcaPhyDrvNotReadyErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 29),
    _CpqFcaPhyDrvNotReadyErrs_Type()
)
cpqFcaPhyDrvNotReadyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvNotReadyErrs.setStatus("mandatory")


class _CpqFcaPhyDrvHasMonInfo_Type(Integer32):
    """Custom type cpqFcaPhyDrvHasMonInfo based on Integer32"""
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


_CpqFcaPhyDrvHasMonInfo_Type.__name__ = "Integer32"
_CpqFcaPhyDrvHasMonInfo_Object = MibTableColumn
cpqFcaPhyDrvHasMonInfo = _CpqFcaPhyDrvHasMonInfo_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 30),
    _CpqFcaPhyDrvHasMonInfo_Type()
)
cpqFcaPhyDrvHasMonInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvHasMonInfo.setStatus("mandatory")


class _CpqFcaPhyDrvCondition_Type(Integer32):
    """Custom type cpqFcaPhyDrvCondition based on Integer32"""
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


_CpqFcaPhyDrvCondition_Type.__name__ = "Integer32"
_CpqFcaPhyDrvCondition_Object = MibTableColumn
cpqFcaPhyDrvCondition = _CpqFcaPhyDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 31),
    _CpqFcaPhyDrvCondition_Type()
)
cpqFcaPhyDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvCondition.setStatus("mandatory")
_CpqFcaPhyDrvHotPlugs_Type = Counter32
_CpqFcaPhyDrvHotPlugs_Object = MibTableColumn
cpqFcaPhyDrvHotPlugs = _CpqFcaPhyDrvHotPlugs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 32),
    _CpqFcaPhyDrvHotPlugs_Type()
)
cpqFcaPhyDrvHotPlugs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvHotPlugs.setStatus("mandatory")
_CpqFcaPhyDrvMediaErrs_Type = Counter32
_CpqFcaPhyDrvMediaErrs_Object = MibTableColumn
cpqFcaPhyDrvMediaErrs = _CpqFcaPhyDrvMediaErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 33),
    _CpqFcaPhyDrvMediaErrs_Type()
)
cpqFcaPhyDrvMediaErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvMediaErrs.setStatus("mandatory")
_CpqFcaPhyDrvHardwareErrs_Type = Counter32
_CpqFcaPhyDrvHardwareErrs_Object = MibTableColumn
cpqFcaPhyDrvHardwareErrs = _CpqFcaPhyDrvHardwareErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 34),
    _CpqFcaPhyDrvHardwareErrs_Type()
)
cpqFcaPhyDrvHardwareErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvHardwareErrs.setStatus("mandatory")
_CpqFcaPhyDrvAbortedCmds_Type = Counter32
_CpqFcaPhyDrvAbortedCmds_Object = MibTableColumn
cpqFcaPhyDrvAbortedCmds = _CpqFcaPhyDrvAbortedCmds_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 35),
    _CpqFcaPhyDrvAbortedCmds_Type()
)
cpqFcaPhyDrvAbortedCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvAbortedCmds.setStatus("mandatory")
_CpqFcaPhyDrvSpinUpErrs_Type = Counter32
_CpqFcaPhyDrvSpinUpErrs_Object = MibTableColumn
cpqFcaPhyDrvSpinUpErrs = _CpqFcaPhyDrvSpinUpErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 36),
    _CpqFcaPhyDrvSpinUpErrs_Type()
)
cpqFcaPhyDrvSpinUpErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvSpinUpErrs.setStatus("mandatory")
_CpqFcaPhyDrvBadTargetErrs_Type = Counter32
_CpqFcaPhyDrvBadTargetErrs_Object = MibTableColumn
cpqFcaPhyDrvBadTargetErrs = _CpqFcaPhyDrvBadTargetErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 37),
    _CpqFcaPhyDrvBadTargetErrs_Type()
)
cpqFcaPhyDrvBadTargetErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvBadTargetErrs.setStatus("mandatory")
_CpqFcaPhyDrvSize_Type = Integer32
_CpqFcaPhyDrvSize_Object = MibTableColumn
cpqFcaPhyDrvSize = _CpqFcaPhyDrvSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 38),
    _CpqFcaPhyDrvSize_Type()
)
cpqFcaPhyDrvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvSize.setStatus("mandatory")
_CpqFcaPhyDrvBusFaults_Type = Counter32
_CpqFcaPhyDrvBusFaults_Object = MibTableColumn
cpqFcaPhyDrvBusFaults = _CpqFcaPhyDrvBusFaults_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 39),
    _CpqFcaPhyDrvBusFaults_Type()
)
cpqFcaPhyDrvBusFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvBusFaults.setStatus("mandatory")


class _CpqFcaPhyDrvHotPlug_Type(Integer32):
    """Custom type cpqFcaPhyDrvHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotPlug", 2),
          ("nonHotPlug", 3),
          ("other", 1))
    )


_CpqFcaPhyDrvHotPlug_Type.__name__ = "Integer32"
_CpqFcaPhyDrvHotPlug_Object = MibTableColumn
cpqFcaPhyDrvHotPlug = _CpqFcaPhyDrvHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 40),
    _CpqFcaPhyDrvHotPlug_Type()
)
cpqFcaPhyDrvHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvHotPlug.setStatus("mandatory")


class _CpqFcaPhyDrvPlacement_Type(Integer32):
    """Custom type cpqFcaPhyDrvPlacement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("other", 1))
    )


_CpqFcaPhyDrvPlacement_Type.__name__ = "Integer32"
_CpqFcaPhyDrvPlacement_Object = MibTableColumn
cpqFcaPhyDrvPlacement = _CpqFcaPhyDrvPlacement_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 41),
    _CpqFcaPhyDrvPlacement_Type()
)
cpqFcaPhyDrvPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvPlacement.setStatus("mandatory")
_CpqFcaPhyDrvBusNumber_Type = Integer32
_CpqFcaPhyDrvBusNumber_Object = MibTableColumn
cpqFcaPhyDrvBusNumber = _CpqFcaPhyDrvBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 42),
    _CpqFcaPhyDrvBusNumber_Type()
)
cpqFcaPhyDrvBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvBusNumber.setStatus("mandatory")


class _CpqFcaPhyDrvSerialNum_Type(DisplayString):
    """Custom type cpqFcaPhyDrvSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpqFcaPhyDrvSerialNum_Type.__name__ = "DisplayString"
_CpqFcaPhyDrvSerialNum_Object = MibTableColumn
cpqFcaPhyDrvSerialNum = _CpqFcaPhyDrvSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 43),
    _CpqFcaPhyDrvSerialNum_Type()
)
cpqFcaPhyDrvSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvSerialNum.setStatus("mandatory")


class _CpqFcaPhyDrvPreFailMonitoring_Type(Integer32):
    """Custom type cpqFcaPhyDrvPreFailMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 3),
          ("notAvailable", 2),
          ("other", 1))
    )


_CpqFcaPhyDrvPreFailMonitoring_Type.__name__ = "Integer32"
_CpqFcaPhyDrvPreFailMonitoring_Object = MibTableColumn
cpqFcaPhyDrvPreFailMonitoring = _CpqFcaPhyDrvPreFailMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 44),
    _CpqFcaPhyDrvPreFailMonitoring_Type()
)
cpqFcaPhyDrvPreFailMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvPreFailMonitoring.setStatus("mandatory")


class _CpqFcaPhyDrvCurrentWidth_Type(Integer32):
    """Custom type cpqFcaPhyDrvCurrentWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("narrow", 2),
          ("other", 1),
          ("wide16", 3))
    )


_CpqFcaPhyDrvCurrentWidth_Type.__name__ = "Integer32"
_CpqFcaPhyDrvCurrentWidth_Object = MibTableColumn
cpqFcaPhyDrvCurrentWidth = _CpqFcaPhyDrvCurrentWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 45),
    _CpqFcaPhyDrvCurrentWidth_Type()
)
cpqFcaPhyDrvCurrentWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvCurrentWidth.setStatus("mandatory")


class _CpqFcaPhyDrvCurrentSpeed_Type(Integer32):
    """Custom type cpqFcaPhyDrvCurrentSpeed based on Integer32"""
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
        *(("asynchronous", 2),
          ("fast", 3),
          ("other", 1),
          ("ultra", 4),
          ("ultra2", 5),
          ("ultra3", 6),
          ("ultra320", 7))
    )


_CpqFcaPhyDrvCurrentSpeed_Type.__name__ = "Integer32"
_CpqFcaPhyDrvCurrentSpeed_Object = MibTableColumn
cpqFcaPhyDrvCurrentSpeed = _CpqFcaPhyDrvCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 46),
    _CpqFcaPhyDrvCurrentSpeed_Type()
)
cpqFcaPhyDrvCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvCurrentSpeed.setStatus("mandatory")
_CpqFcaPhyDrvFailureCode_Type = Integer32
_CpqFcaPhyDrvFailureCode_Object = MibTableColumn
cpqFcaPhyDrvFailureCode = _CpqFcaPhyDrvFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 47),
    _CpqFcaPhyDrvFailureCode_Type()
)
cpqFcaPhyDrvFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvFailureCode.setStatus("mandatory")
_CpqFcaPhyDrvBlinkTime_Type = Counter32
_CpqFcaPhyDrvBlinkTime_Object = MibTableColumn
cpqFcaPhyDrvBlinkTime = _CpqFcaPhyDrvBlinkTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 48),
    _CpqFcaPhyDrvBlinkTime_Type()
)
cpqFcaPhyDrvBlinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvBlinkTime.setStatus("mandatory")


class _CpqFcaPhyDrvSmartStatus_Type(Integer32):
    """Custom type cpqFcaPhyDrvSmartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 2),
          ("other", 1),
          ("replaceDrive", 3))
    )


_CpqFcaPhyDrvSmartStatus_Type.__name__ = "Integer32"
_CpqFcaPhyDrvSmartStatus_Object = MibTableColumn
cpqFcaPhyDrvSmartStatus = _CpqFcaPhyDrvSmartStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 49),
    _CpqFcaPhyDrvSmartStatus_Type()
)
cpqFcaPhyDrvSmartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvSmartStatus.setStatus("mandatory")


class _CpqFcaPhyDrvRotationalSpeed_Type(Integer32):
    """Custom type cpqFcaPhyDrvRotationalSpeed based on Integer32"""
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
          ("rpm10K", 3),
          ("rpm15K", 4),
          ("rpm7200", 2))
    )


_CpqFcaPhyDrvRotationalSpeed_Type.__name__ = "Integer32"
_CpqFcaPhyDrvRotationalSpeed_Object = MibTableColumn
cpqFcaPhyDrvRotationalSpeed = _CpqFcaPhyDrvRotationalSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 50),
    _CpqFcaPhyDrvRotationalSpeed_Type()
)
cpqFcaPhyDrvRotationalSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvRotationalSpeed.setStatus("mandatory")


class _CpqFcaPhyDrvType_Type(Integer32):
    """Custom type cpqFcaPhyDrvType based on Integer32"""
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
          ("parallelScsi", 2),
          ("sas", 4),
          ("sata", 3))
    )


_CpqFcaPhyDrvType_Type.__name__ = "Integer32"
_CpqFcaPhyDrvType_Object = MibTableColumn
cpqFcaPhyDrvType = _CpqFcaPhyDrvType_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 51),
    _CpqFcaPhyDrvType_Type()
)
cpqFcaPhyDrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvType.setStatus("mandatory")


class _CpqFcaPhyDrvSataVersion_Type(Integer32):
    """Custom type cpqFcaPhyDrvSataVersion based on Integer32"""
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
          ("sataOne", 2),
          ("sataTwo", 3))
    )


_CpqFcaPhyDrvSataVersion_Type.__name__ = "Integer32"
_CpqFcaPhyDrvSataVersion_Object = MibTableColumn
cpqFcaPhyDrvSataVersion = _CpqFcaPhyDrvSataVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 52),
    _CpqFcaPhyDrvSataVersion_Type()
)
cpqFcaPhyDrvSataVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvSataVersion.setStatus("mandatory")


class _CpqFcaPhyDrvBoxConnector_Type(DisplayString):
    """Custom type cpqFcaPhyDrvBoxConnector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CpqFcaPhyDrvBoxConnector_Type.__name__ = "DisplayString"
_CpqFcaPhyDrvBoxConnector_Object = MibTableColumn
cpqFcaPhyDrvBoxConnector = _CpqFcaPhyDrvBoxConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 53),
    _CpqFcaPhyDrvBoxConnector_Type()
)
cpqFcaPhyDrvBoxConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvBoxConnector.setStatus("mandatory")
_CpqFcaPhyDrvBoxOnConnector_Type = Integer32
_CpqFcaPhyDrvBoxOnConnector_Object = MibTableColumn
cpqFcaPhyDrvBoxOnConnector = _CpqFcaPhyDrvBoxOnConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 54),
    _CpqFcaPhyDrvBoxOnConnector_Type()
)
cpqFcaPhyDrvBoxOnConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvBoxOnConnector.setStatus("mandatory")


class _CpqFcaPhyDrvLocationString_Type(DisplayString):
    """Custom type cpqFcaPhyDrvLocationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqFcaPhyDrvLocationString_Type.__name__ = "DisplayString"
_CpqFcaPhyDrvLocationString_Object = MibTableColumn
cpqFcaPhyDrvLocationString = _CpqFcaPhyDrvLocationString_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 55),
    _CpqFcaPhyDrvLocationString_Type()
)
cpqFcaPhyDrvLocationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvLocationString.setStatus("mandatory")


class _CpqFcaPhyDrvNegotiatedLinkRate_Type(Integer32):
    """Custom type cpqFcaPhyDrvNegotiatedLinkRate based on Integer32"""
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
          ("rate-1-5", 2),
          ("rate-3-0", 3))
    )


_CpqFcaPhyDrvNegotiatedLinkRate_Type.__name__ = "Integer32"
_CpqFcaPhyDrvNegotiatedLinkRate_Object = MibTableColumn
cpqFcaPhyDrvNegotiatedLinkRate = _CpqFcaPhyDrvNegotiatedLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 56),
    _CpqFcaPhyDrvNegotiatedLinkRate_Type()
)
cpqFcaPhyDrvNegotiatedLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvNegotiatedLinkRate.setStatus("mandatory")
_CpqFcaPhyDrvPhyCount_Type = Integer32
_CpqFcaPhyDrvPhyCount_Object = MibTableColumn
cpqFcaPhyDrvPhyCount = _CpqFcaPhyDrvPhyCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 57),
    _CpqFcaPhyDrvPhyCount_Type()
)
cpqFcaPhyDrvPhyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvPhyCount.setStatus("mandatory")


class _CpqFcaPhyDrvUnsupportedDrive_Type(Integer32):
    """Custom type cpqFcaPhyDrvUnsupportedDrive based on Integer32"""
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
          ("supported", 2),
          ("unsupported-SATA", 4),
          ("unsupported-SinglePorted", 3),
          ("unsupported-TooSmall", 5))
    )


_CpqFcaPhyDrvUnsupportedDrive_Type.__name__ = "Integer32"
_CpqFcaPhyDrvUnsupportedDrive_Object = MibTableColumn
cpqFcaPhyDrvUnsupportedDrive = _CpqFcaPhyDrvUnsupportedDrive_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 5, 1, 1, 58),
    _CpqFcaPhyDrvUnsupportedDrive_Type()
)
cpqFcaPhyDrvUnsupportedDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvUnsupportedDrive.setStatus("mandatory")
_CpqFcaPhyDrvThr_ObjectIdentity = ObjectIdentity
cpqFcaPhyDrvThr = _CpqFcaPhyDrvThr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6)
)
_CpqFcaPhyDrvThrTable_Object = MibTable
cpqFcaPhyDrvThrTable = _CpqFcaPhyDrvThrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrTable.setStatus("mandatory")
_CpqFcaPhyDrvThrEntry_Object = MibTableRow
cpqFcaPhyDrvThrEntry = _CpqFcaPhyDrvThrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1)
)
cpqFcaPhyDrvThrEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcaPhyDrvThrBoxIndex"),
    (0, "CPQFCA-MIB", "cpqFcaPhyDrvThrIndex"),
)
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrEntry.setStatus("mandatory")


class _CpqFcaPhyDrvThrBoxIndex_Type(Integer32):
    """Custom type cpqFcaPhyDrvThrBoxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcaPhyDrvThrBoxIndex_Type.__name__ = "Integer32"
_CpqFcaPhyDrvThrBoxIndex_Object = MibTableColumn
cpqFcaPhyDrvThrBoxIndex = _CpqFcaPhyDrvThrBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 1),
    _CpqFcaPhyDrvThrBoxIndex_Type()
)
cpqFcaPhyDrvThrBoxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrBoxIndex.setStatus("mandatory")


class _CpqFcaPhyDrvThrIndex_Type(Integer32):
    """Custom type cpqFcaPhyDrvThrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcaPhyDrvThrIndex_Type.__name__ = "Integer32"
_CpqFcaPhyDrvThrIndex_Object = MibTableColumn
cpqFcaPhyDrvThrIndex = _CpqFcaPhyDrvThrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 2),
    _CpqFcaPhyDrvThrIndex_Type()
)
cpqFcaPhyDrvThrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrIndex.setStatus("mandatory")
_CpqFcaPhyDrvThrUsedReallocs_Type = Integer32
_CpqFcaPhyDrvThrUsedReallocs_Object = MibTableColumn
cpqFcaPhyDrvThrUsedReallocs = _CpqFcaPhyDrvThrUsedReallocs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 3),
    _CpqFcaPhyDrvThrUsedReallocs_Type()
)
cpqFcaPhyDrvThrUsedReallocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrUsedReallocs.setStatus("mandatory")
_CpqFcaPhyDrvThrSpinupTime_Type = Integer32
_CpqFcaPhyDrvThrSpinupTime_Object = MibTableColumn
cpqFcaPhyDrvThrSpinupTime = _CpqFcaPhyDrvThrSpinupTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 4),
    _CpqFcaPhyDrvThrSpinupTime_Type()
)
cpqFcaPhyDrvThrSpinupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrSpinupTime.setStatus("mandatory")
_CpqFcaPhyDrvThrFunctTest1_Type = Integer32
_CpqFcaPhyDrvThrFunctTest1_Object = MibTableColumn
cpqFcaPhyDrvThrFunctTest1 = _CpqFcaPhyDrvThrFunctTest1_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 5),
    _CpqFcaPhyDrvThrFunctTest1_Type()
)
cpqFcaPhyDrvThrFunctTest1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrFunctTest1.setStatus("deprecated")
_CpqFcaPhyDrvThrFunctTest2_Type = Integer32
_CpqFcaPhyDrvThrFunctTest2_Object = MibTableColumn
cpqFcaPhyDrvThrFunctTest2 = _CpqFcaPhyDrvThrFunctTest2_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 6),
    _CpqFcaPhyDrvThrFunctTest2_Type()
)
cpqFcaPhyDrvThrFunctTest2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrFunctTest2.setStatus("deprecated")
_CpqFcaPhyDrvThrFunctTest3_Type = Integer32
_CpqFcaPhyDrvThrFunctTest3_Object = MibTableColumn
cpqFcaPhyDrvThrFunctTest3 = _CpqFcaPhyDrvThrFunctTest3_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 7),
    _CpqFcaPhyDrvThrFunctTest3_Type()
)
cpqFcaPhyDrvThrFunctTest3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrFunctTest3.setStatus("deprecated")


class _CpqFcaPhyDrvThrViUsedReallocs_Type(Integer32):
    """Custom type cpqFcaPhyDrvThrViUsedReallocs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 3))
    )


_CpqFcaPhyDrvThrViUsedReallocs_Type.__name__ = "Integer32"
_CpqFcaPhyDrvThrViUsedReallocs_Object = MibTableColumn
cpqFcaPhyDrvThrViUsedReallocs = _CpqFcaPhyDrvThrViUsedReallocs_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 8),
    _CpqFcaPhyDrvThrViUsedReallocs_Type()
)
cpqFcaPhyDrvThrViUsedReallocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrViUsedReallocs.setStatus("mandatory")


class _CpqFcaPhyDrvThrViSpinupTime_Type(Integer32):
    """Custom type cpqFcaPhyDrvThrViSpinupTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 3))
    )


_CpqFcaPhyDrvThrViSpinupTime_Type.__name__ = "Integer32"
_CpqFcaPhyDrvThrViSpinupTime_Object = MibTableColumn
cpqFcaPhyDrvThrViSpinupTime = _CpqFcaPhyDrvThrViSpinupTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 9),
    _CpqFcaPhyDrvThrViSpinupTime_Type()
)
cpqFcaPhyDrvThrViSpinupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrViSpinupTime.setStatus("mandatory")


class _CpqFcaPhyDrvThrViFunctTest1_Type(Integer32):
    """Custom type cpqFcaPhyDrvThrViFunctTest1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 3))
    )


_CpqFcaPhyDrvThrViFunctTest1_Type.__name__ = "Integer32"
_CpqFcaPhyDrvThrViFunctTest1_Object = MibTableColumn
cpqFcaPhyDrvThrViFunctTest1 = _CpqFcaPhyDrvThrViFunctTest1_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 10),
    _CpqFcaPhyDrvThrViFunctTest1_Type()
)
cpqFcaPhyDrvThrViFunctTest1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrViFunctTest1.setStatus("mandatory")


class _CpqFcaPhyDrvThrViFunctTest2_Type(Integer32):
    """Custom type cpqFcaPhyDrvThrViFunctTest2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 3))
    )


_CpqFcaPhyDrvThrViFunctTest2_Type.__name__ = "Integer32"
_CpqFcaPhyDrvThrViFunctTest2_Object = MibTableColumn
cpqFcaPhyDrvThrViFunctTest2 = _CpqFcaPhyDrvThrViFunctTest2_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 11),
    _CpqFcaPhyDrvThrViFunctTest2_Type()
)
cpqFcaPhyDrvThrViFunctTest2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrViFunctTest2.setStatus("mandatory")


class _CpqFcaPhyDrvThrViFunctTest3_Type(Integer32):
    """Custom type cpqFcaPhyDrvThrViFunctTest3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 3))
    )


_CpqFcaPhyDrvThrViFunctTest3_Type.__name__ = "Integer32"
_CpqFcaPhyDrvThrViFunctTest3_Object = MibTableColumn
cpqFcaPhyDrvThrViFunctTest3 = _CpqFcaPhyDrvThrViFunctTest3_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 6, 1, 1, 12),
    _CpqFcaPhyDrvThrViFunctTest3_Type()
)
cpqFcaPhyDrvThrViFunctTest3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaPhyDrvThrViFunctTest3.setStatus("mandatory")
_CpqFcaHostCntlr_ObjectIdentity = ObjectIdentity
cpqFcaHostCntlr = _CpqFcaHostCntlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7)
)
_CpqFcaHostCntlrTable_Object = MibTable
cpqFcaHostCntlrTable = _CpqFcaHostCntlrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1)
)
if mibBuilder.loadTexts:
    cpqFcaHostCntlrTable.setStatus("mandatory")
_CpqFcaHostCntlrEntry_Object = MibTableRow
cpqFcaHostCntlrEntry = _CpqFcaHostCntlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1)
)
cpqFcaHostCntlrEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcaHostCntlrIndex"),
)
if mibBuilder.loadTexts:
    cpqFcaHostCntlrEntry.setStatus("mandatory")
_CpqFcaHostCntlrIndex_Type = Integer32
_CpqFcaHostCntlrIndex_Object = MibTableColumn
cpqFcaHostCntlrIndex = _CpqFcaHostCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 1),
    _CpqFcaHostCntlrIndex_Type()
)
cpqFcaHostCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrIndex.setStatus("mandatory")


class _CpqFcaHostCntlrSlot_Type(Integer32):
    """Custom type cpqFcaHostCntlrSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcaHostCntlrSlot_Type.__name__ = "Integer32"
_CpqFcaHostCntlrSlot_Object = MibTableColumn
cpqFcaHostCntlrSlot = _CpqFcaHostCntlrSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 2),
    _CpqFcaHostCntlrSlot_Type()
)
cpqFcaHostCntlrSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrSlot.setStatus("mandatory")


class _CpqFcaHostCntlrModel_Type(Integer32):
    """Custom type cpqFcaHostCntlrModel based on Integer32"""
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
              36)
        )
    )
    namedValues = NamedValues(
        *(("a6826a", 14),
          ("a7298a", 12),
          ("ab46xa", 17),
          ("dpfcmc", 9),
          ("fc-generic", 18),
          ("fca-1050", 23),
          ("fca-1142sr", 26),
          ("fca-1143", 19),
          ("fca-1205", 36),
          ("fca-1242sr", 27),
          ("fca-1243", 20),
          ("fca-2101", 6),
          ("fca-2142sr", 28),
          ("fca-2143", 21),
          ("fca-2214", 11),
          ("fca-2214dc", 13),
          ("fca-221x", 8),
          ("fca-2242sr", 29),
          ("fca-2243", 22),
          ("fca-2404", 10),
          ("fca-81e", 34),
          ("fca-81q", 31),
          ("fca-82e", 35),
          ("fca-82q", 32),
          ("fca-lpe1105", 24),
          ("fca-qmh2462", 25),
          ("fca-qmh2562", 33),
          ("fchc-e", 3),
          ("fchc-p", 2),
          ("fchc64", 4),
          ("fcmc20pe", 30),
          ("fcmcG3", 15),
          ("fcmcG4", 16),
          ("other", 1),
          ("sa-sam", 5),
          ("sw64-33", 7))
    )


_CpqFcaHostCntlrModel_Type.__name__ = "Integer32"
_CpqFcaHostCntlrModel_Object = MibTableColumn
cpqFcaHostCntlrModel = _CpqFcaHostCntlrModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 3),
    _CpqFcaHostCntlrModel_Type()
)
cpqFcaHostCntlrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrModel.setStatus("mandatory")


class _CpqFcaHostCntlrStatus_Type(Integer32):
    """Custom type cpqFcaHostCntlrStatus based on Integer32"""
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
        *(("failed", 3),
          ("loopDegraded", 5),
          ("loopFailed", 6),
          ("notConnected", 7),
          ("ok", 2),
          ("other", 1),
          ("shutdown", 4))
    )


_CpqFcaHostCntlrStatus_Type.__name__ = "Integer32"
_CpqFcaHostCntlrStatus_Object = MibTableColumn
cpqFcaHostCntlrStatus = _CpqFcaHostCntlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 4),
    _CpqFcaHostCntlrStatus_Type()
)
cpqFcaHostCntlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrStatus.setStatus("mandatory")


class _CpqFcaHostCntlrCondition_Type(Integer32):
    """Custom type cpqFcaHostCntlrCondition based on Integer32"""
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


_CpqFcaHostCntlrCondition_Type.__name__ = "Integer32"
_CpqFcaHostCntlrCondition_Object = MibTableColumn
cpqFcaHostCntlrCondition = _CpqFcaHostCntlrCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 5),
    _CpqFcaHostCntlrCondition_Type()
)
cpqFcaHostCntlrCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrCondition.setStatus("mandatory")


class _CpqFcaHostCntlrWorldWideName_Type(DisplayString):
    """Custom type cpqFcaHostCntlrWorldWideName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqFcaHostCntlrWorldWideName_Type.__name__ = "DisplayString"
_CpqFcaHostCntlrWorldWideName_Object = MibTableColumn
cpqFcaHostCntlrWorldWideName = _CpqFcaHostCntlrWorldWideName_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 6),
    _CpqFcaHostCntlrWorldWideName_Type()
)
cpqFcaHostCntlrWorldWideName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrWorldWideName.setStatus("mandatory")
_CpqFcaHostCntlrStorBoxList_Type = OctetString
_CpqFcaHostCntlrStorBoxList_Object = MibTableColumn
cpqFcaHostCntlrStorBoxList = _CpqFcaHostCntlrStorBoxList_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 7),
    _CpqFcaHostCntlrStorBoxList_Type()
)
cpqFcaHostCntlrStorBoxList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrStorBoxList.setStatus("mandatory")


class _CpqFcaHostCntlrOverallCondition_Type(Integer32):
    """Custom type cpqFcaHostCntlrOverallCondition based on Integer32"""
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


_CpqFcaHostCntlrOverallCondition_Type.__name__ = "Integer32"
_CpqFcaHostCntlrOverallCondition_Object = MibTableColumn
cpqFcaHostCntlrOverallCondition = _CpqFcaHostCntlrOverallCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 8),
    _CpqFcaHostCntlrOverallCondition_Type()
)
cpqFcaHostCntlrOverallCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrOverallCondition.setStatus("mandatory")
_CpqFcaHostCntlrTapeCntlrList_Type = OctetString
_CpqFcaHostCntlrTapeCntlrList_Object = MibTableColumn
cpqFcaHostCntlrTapeCntlrList = _CpqFcaHostCntlrTapeCntlrList_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 9),
    _CpqFcaHostCntlrTapeCntlrList_Type()
)
cpqFcaHostCntlrTapeCntlrList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrTapeCntlrList.setStatus("mandatory")


class _CpqFcaHostCntlrSerialNumber_Type(DisplayString):
    """Custom type cpqFcaHostCntlrSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqFcaHostCntlrSerialNumber_Type.__name__ = "DisplayString"
_CpqFcaHostCntlrSerialNumber_Object = MibTableColumn
cpqFcaHostCntlrSerialNumber = _CpqFcaHostCntlrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 10),
    _CpqFcaHostCntlrSerialNumber_Type()
)
cpqFcaHostCntlrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrSerialNumber.setStatus("mandatory")


class _CpqFcaHostCntlrHwLocation_Type(DisplayString):
    """Custom type cpqFcaHostCntlrHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqFcaHostCntlrHwLocation_Type.__name__ = "DisplayString"
_CpqFcaHostCntlrHwLocation_Object = MibTableColumn
cpqFcaHostCntlrHwLocation = _CpqFcaHostCntlrHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 11),
    _CpqFcaHostCntlrHwLocation_Type()
)
cpqFcaHostCntlrHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrHwLocation.setStatus("optional")


class _CpqFcaHostCntlrWorldWidePortName_Type(DisplayString):
    """Custom type cpqFcaHostCntlrWorldWidePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqFcaHostCntlrWorldWidePortName_Type.__name__ = "DisplayString"
_CpqFcaHostCntlrWorldWidePortName_Object = MibTableColumn
cpqFcaHostCntlrWorldWidePortName = _CpqFcaHostCntlrWorldWidePortName_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 12),
    _CpqFcaHostCntlrWorldWidePortName_Type()
)
cpqFcaHostCntlrWorldWidePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrWorldWidePortName.setStatus("mandatory")
_CpqFcaHostCntlrFirmwareVersion_Type = DisplayString
_CpqFcaHostCntlrFirmwareVersion_Object = MibTableColumn
cpqFcaHostCntlrFirmwareVersion = _CpqFcaHostCntlrFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 13),
    _CpqFcaHostCntlrFirmwareVersion_Type()
)
cpqFcaHostCntlrFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrFirmwareVersion.setStatus("mandatory")
_CpqFcaHostCntlrOptionRomVersion_Type = DisplayString
_CpqFcaHostCntlrOptionRomVersion_Object = MibTableColumn
cpqFcaHostCntlrOptionRomVersion = _CpqFcaHostCntlrOptionRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 7, 1, 1, 14),
    _CpqFcaHostCntlrOptionRomVersion_Type()
)
cpqFcaHostCntlrOptionRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcaHostCntlrOptionRomVersion.setStatus("mandatory")
_CpqExtArrRsrcVol_ObjectIdentity = ObjectIdentity
cpqExtArrRsrcVol = _CpqExtArrRsrcVol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8)
)
_CpqExtArrRsrcVolTable_Object = MibTable
cpqExtArrRsrcVolTable = _CpqExtArrRsrcVolTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1)
)
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolTable.setStatus("mandatory")
_CpqExtArrRsrcVolEntry_Object = MibTableRow
cpqExtArrRsrcVolEntry = _CpqExtArrRsrcVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1)
)
cpqExtArrRsrcVolEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqExtArrRsrcVolBoxIndex"),
    (0, "CPQFCA-MIB", "cpqExtArrRsrcVolIndex"),
)
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolEntry.setStatus("mandatory")


class _CpqExtArrRsrcVolBoxIndex_Type(Integer32):
    """Custom type cpqExtArrRsrcVolBoxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqExtArrRsrcVolBoxIndex_Type.__name__ = "Integer32"
_CpqExtArrRsrcVolBoxIndex_Object = MibTableColumn
cpqExtArrRsrcVolBoxIndex = _CpqExtArrRsrcVolBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 1),
    _CpqExtArrRsrcVolBoxIndex_Type()
)
cpqExtArrRsrcVolBoxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolBoxIndex.setStatus("mandatory")


class _CpqExtArrRsrcVolIndex_Type(Integer32):
    """Custom type cpqExtArrRsrcVolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqExtArrRsrcVolIndex_Type.__name__ = "Integer32"
_CpqExtArrRsrcVolIndex_Object = MibTableColumn
cpqExtArrRsrcVolIndex = _CpqExtArrRsrcVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 2),
    _CpqExtArrRsrcVolIndex_Type()
)
cpqExtArrRsrcVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolIndex.setStatus("mandatory")
_CpqExtArrRsrcVolActiveInstances_Type = Integer32
_CpqExtArrRsrcVolActiveInstances_Object = MibTableColumn
cpqExtArrRsrcVolActiveInstances = _CpqExtArrRsrcVolActiveInstances_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 3),
    _CpqExtArrRsrcVolActiveInstances_Type()
)
cpqExtArrRsrcVolActiveInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolActiveInstances.setStatus("mandatory")
_CpqExtArrRsrcVolDisabledInstances_Type = Integer32
_CpqExtArrRsrcVolDisabledInstances_Object = MibTableColumn
cpqExtArrRsrcVolDisabledInstances = _CpqExtArrRsrcVolDisabledInstances_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 4),
    _CpqExtArrRsrcVolDisabledInstances_Type()
)
cpqExtArrRsrcVolDisabledInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolDisabledInstances.setStatus("mandatory")


class _CpqExtArrRsrcVolAllowCreation_Type(Integer32):
    """Custom type cpqExtArrRsrcVolAllowCreation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 2),
          ("notAllowed", 3),
          ("other", 1))
    )


_CpqExtArrRsrcVolAllowCreation_Type.__name__ = "Integer32"
_CpqExtArrRsrcVolAllowCreation_Object = MibTableColumn
cpqExtArrRsrcVolAllowCreation = _CpqExtArrRsrcVolAllowCreation_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 5),
    _CpqExtArrRsrcVolAllowCreation_Type()
)
cpqExtArrRsrcVolAllowCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolAllowCreation.setStatus("mandatory")


class _CpqExtArrRsrcVolVolumeId_Type(DisplayString):
    """Custom type cpqExtArrRsrcVolVolumeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqExtArrRsrcVolVolumeId_Type.__name__ = "DisplayString"
_CpqExtArrRsrcVolVolumeId_Object = MibTableColumn
cpqExtArrRsrcVolVolumeId = _CpqExtArrRsrcVolVolumeId_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 6),
    _CpqExtArrRsrcVolVolumeId_Type()
)
cpqExtArrRsrcVolVolumeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolVolumeId.setStatus("mandatory")


class _CpqExtArrRsrcVolSourceVolumeId_Type(DisplayString):
    """Custom type cpqExtArrRsrcVolSourceVolumeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqExtArrRsrcVolSourceVolumeId_Type.__name__ = "DisplayString"
_CpqExtArrRsrcVolSourceVolumeId_Object = MibTableColumn
cpqExtArrRsrcVolSourceVolumeId = _CpqExtArrRsrcVolSourceVolumeId_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 7),
    _CpqExtArrRsrcVolSourceVolumeId_Type()
)
cpqExtArrRsrcVolSourceVolumeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolSourceVolumeId.setStatus("mandatory")
_CpqExtArrRsrcVolTotalSpace_Type = Counter32
_CpqExtArrRsrcVolTotalSpace_Object = MibTableColumn
cpqExtArrRsrcVolTotalSpace = _CpqExtArrRsrcVolTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 8),
    _CpqExtArrRsrcVolTotalSpace_Type()
)
cpqExtArrRsrcVolTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolTotalSpace.setStatus("mandatory")
_CpqExtArrRsrcVolFreeActiveSpace_Type = Counter32
_CpqExtArrRsrcVolFreeActiveSpace_Object = MibTableColumn
cpqExtArrRsrcVolFreeActiveSpace = _CpqExtArrRsrcVolFreeActiveSpace_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 9),
    _CpqExtArrRsrcVolFreeActiveSpace_Type()
)
cpqExtArrRsrcVolFreeActiveSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolFreeActiveSpace.setStatus("mandatory")
_CpqExtArrRsrcVolFreeNewSpace_Type = Counter32
_CpqExtArrRsrcVolFreeNewSpace_Object = MibTableColumn
cpqExtArrRsrcVolFreeNewSpace = _CpqExtArrRsrcVolFreeNewSpace_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 10),
    _CpqExtArrRsrcVolFreeNewSpace_Type()
)
cpqExtArrRsrcVolFreeNewSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolFreeNewSpace.setStatus("mandatory")


class _CpqExtArrRsrcVolStatus_Type(Integer32):
    """Custom type cpqExtArrRsrcVolStatus based on Integer32"""
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
        *(("ok", 2),
          ("other", 1),
          ("resourceVolDisconnected", 4),
          ("resourceVolFailed", 8),
          ("resourceVolNotAvail", 10),
          ("resourceVolNotLocated", 6),
          ("resourceVolObsolete", 11),
          ("resourceVolObsoleteFailed", 12),
          ("sourceVolFailed", 7),
          ("sourceVolNotAvail", 9),
          ("sourceVolNotLocated", 5),
          ("unknownFailure", 3))
    )


_CpqExtArrRsrcVolStatus_Type.__name__ = "Integer32"
_CpqExtArrRsrcVolStatus_Object = MibTableColumn
cpqExtArrRsrcVolStatus = _CpqExtArrRsrcVolStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 8, 1, 1, 11),
    _CpqExtArrRsrcVolStatus_Type()
)
cpqExtArrRsrcVolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrRsrcVolStatus.setStatus("mandatory")
_CpqExtArrSnapshot_ObjectIdentity = ObjectIdentity
cpqExtArrSnapshot = _CpqExtArrSnapshot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9)
)
_CpqExtArrSnapshotTable_Object = MibTable
cpqExtArrSnapshotTable = _CpqExtArrSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1)
)
if mibBuilder.loadTexts:
    cpqExtArrSnapshotTable.setStatus("mandatory")
_CpqExtArrSnapshotEntry_Object = MibTableRow
cpqExtArrSnapshotEntry = _CpqExtArrSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1, 1)
)
cpqExtArrSnapshotEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqExtArrSnapshotBoxIndex"),
    (0, "CPQFCA-MIB", "cpqExtArrSnapshotRsrcVolIndex"),
    (0, "CPQFCA-MIB", "cpqExtArrSnapshotIndex"),
)
if mibBuilder.loadTexts:
    cpqExtArrSnapshotEntry.setStatus("mandatory")


class _CpqExtArrSnapshotBoxIndex_Type(Integer32):
    """Custom type cpqExtArrSnapshotBoxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqExtArrSnapshotBoxIndex_Type.__name__ = "Integer32"
_CpqExtArrSnapshotBoxIndex_Object = MibTableColumn
cpqExtArrSnapshotBoxIndex = _CpqExtArrSnapshotBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1, 1, 1),
    _CpqExtArrSnapshotBoxIndex_Type()
)
cpqExtArrSnapshotBoxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrSnapshotBoxIndex.setStatus("mandatory")


class _CpqExtArrSnapshotRsrcVolIndex_Type(Integer32):
    """Custom type cpqExtArrSnapshotRsrcVolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqExtArrSnapshotRsrcVolIndex_Type.__name__ = "Integer32"
_CpqExtArrSnapshotRsrcVolIndex_Object = MibTableColumn
cpqExtArrSnapshotRsrcVolIndex = _CpqExtArrSnapshotRsrcVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1, 1, 2),
    _CpqExtArrSnapshotRsrcVolIndex_Type()
)
cpqExtArrSnapshotRsrcVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrSnapshotRsrcVolIndex.setStatus("mandatory")
_CpqExtArrSnapshotIndex_Type = Integer32
_CpqExtArrSnapshotIndex_Object = MibTableColumn
cpqExtArrSnapshotIndex = _CpqExtArrSnapshotIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1, 1, 3),
    _CpqExtArrSnapshotIndex_Type()
)
cpqExtArrSnapshotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrSnapshotIndex.setStatus("mandatory")


class _CpqExtArrSnapshotInstance_Type(Integer32):
    """Custom type cpqExtArrSnapshotInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqExtArrSnapshotInstance_Type.__name__ = "Integer32"
_CpqExtArrSnapshotInstance_Object = MibTableColumn
cpqExtArrSnapshotInstance = _CpqExtArrSnapshotInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1, 1, 4),
    _CpqExtArrSnapshotInstance_Type()
)
cpqExtArrSnapshotInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrSnapshotInstance.setStatus("mandatory")
_CpqExtArrSnapshotUsedSpace_Type = Counter32
_CpqExtArrSnapshotUsedSpace_Object = MibTableColumn
cpqExtArrSnapshotUsedSpace = _CpqExtArrSnapshotUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1, 1, 5),
    _CpqExtArrSnapshotUsedSpace_Type()
)
cpqExtArrSnapshotUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrSnapshotUsedSpace.setStatus("mandatory")


class _CpqExtArrSnapshotDateTime_Type(OctetString):
    """Custom type cpqExtArrSnapshotDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqExtArrSnapshotDateTime_Type.__name__ = "OctetString"
_CpqExtArrSnapshotDateTime_Object = MibTableColumn
cpqExtArrSnapshotDateTime = _CpqExtArrSnapshotDateTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1, 1, 6),
    _CpqExtArrSnapshotDateTime_Type()
)
cpqExtArrSnapshotDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrSnapshotDateTime.setStatus("deprecated")


class _CpqExtArrSnapshotType_Type(Integer32):
    """Custom type cpqExtArrSnapshotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cow", 2),
          ("other", 1))
    )


_CpqExtArrSnapshotType_Type.__name__ = "Integer32"
_CpqExtArrSnapshotType_Object = MibTableColumn
cpqExtArrSnapshotType = _CpqExtArrSnapshotType_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1, 1, 7),
    _CpqExtArrSnapshotType_Type()
)
cpqExtArrSnapshotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrSnapshotType.setStatus("mandatory")


class _CpqExtArrSnapshotMounted_Type(Integer32):
    """Custom type cpqExtArrSnapshotMounted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mounted", 2),
          ("notMounted", 3),
          ("other", 1))
    )


_CpqExtArrSnapshotMounted_Type.__name__ = "Integer32"
_CpqExtArrSnapshotMounted_Object = MibTableColumn
cpqExtArrSnapshotMounted = _CpqExtArrSnapshotMounted_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1, 1, 8),
    _CpqExtArrSnapshotMounted_Type()
)
cpqExtArrSnapshotMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrSnapshotMounted.setStatus("mandatory")


class _CpqExtArrSnapshotAccess_Type(Integer32):
    """Custom type cpqExtArrSnapshotAccess based on Integer32"""
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
          ("readOnly", 3),
          ("readWrite", 2))
    )


_CpqExtArrSnapshotAccess_Type.__name__ = "Integer32"
_CpqExtArrSnapshotAccess_Object = MibTableColumn
cpqExtArrSnapshotAccess = _CpqExtArrSnapshotAccess_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 2, 9, 1, 1, 9),
    _CpqExtArrSnapshotAccess_Type()
)
cpqExtArrSnapshotAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExtArrSnapshotAccess.setStatus("mandatory")
_CpqFcTapeComponent_ObjectIdentity = ObjectIdentity
cpqFcTapeComponent = _CpqFcTapeComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 3)
)
_CpqFcTapeCntlr_ObjectIdentity = ObjectIdentity
cpqFcTapeCntlr = _CpqFcTapeCntlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1)
)
_CpqFcTapeCntlrTable_Object = MibTable
cpqFcTapeCntlrTable = _CpqFcTapeCntlrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cpqFcTapeCntlrTable.setStatus("mandatory")
_CpqFcTapeCntlrEntry_Object = MibTableRow
cpqFcTapeCntlrEntry = _CpqFcTapeCntlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1, 1)
)
cpqFcTapeCntlrEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcTapeCntlrIndex"),
)
if mibBuilder.loadTexts:
    cpqFcTapeCntlrEntry.setStatus("mandatory")


class _CpqFcTapeCntlrIndex_Type(Integer32):
    """Custom type cpqFcTapeCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcTapeCntlrIndex_Type.__name__ = "Integer32"
_CpqFcTapeCntlrIndex_Object = MibTableColumn
cpqFcTapeCntlrIndex = _CpqFcTapeCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1, 1, 1),
    _CpqFcTapeCntlrIndex_Type()
)
cpqFcTapeCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCntlrIndex.setStatus("mandatory")


class _CpqFcTapeCntlrStatus_Type(Integer32):
    """Custom type cpqFcTapeCntlrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqFcTapeCntlrStatus_Type.__name__ = "Integer32"
_CpqFcTapeCntlrStatus_Object = MibTableColumn
cpqFcTapeCntlrStatus = _CpqFcTapeCntlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1, 1, 2),
    _CpqFcTapeCntlrStatus_Type()
)
cpqFcTapeCntlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCntlrStatus.setStatus("mandatory")


class _CpqFcTapeCntlrCondition_Type(Integer32):
    """Custom type cpqFcTapeCntlrCondition based on Integer32"""
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


_CpqFcTapeCntlrCondition_Type.__name__ = "Integer32"
_CpqFcTapeCntlrCondition_Object = MibTableColumn
cpqFcTapeCntlrCondition = _CpqFcTapeCntlrCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1, 1, 3),
    _CpqFcTapeCntlrCondition_Type()
)
cpqFcTapeCntlrCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCntlrCondition.setStatus("mandatory")


class _CpqFcTapeCntlrOverallCondition_Type(Integer32):
    """Custom type cpqFcTapeCntlrOverallCondition based on Integer32"""
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


_CpqFcTapeCntlrOverallCondition_Type.__name__ = "Integer32"
_CpqFcTapeCntlrOverallCondition_Object = MibTableColumn
cpqFcTapeCntlrOverallCondition = _CpqFcTapeCntlrOverallCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1, 1, 4),
    _CpqFcTapeCntlrOverallCondition_Type()
)
cpqFcTapeCntlrOverallCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCntlrOverallCondition.setStatus("mandatory")


class _CpqFcTapeCntlrWWN_Type(DisplayString):
    """Custom type cpqFcTapeCntlrWWN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqFcTapeCntlrWWN_Type.__name__ = "DisplayString"
_CpqFcTapeCntlrWWN_Object = MibTableColumn
cpqFcTapeCntlrWWN = _CpqFcTapeCntlrWWN_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1, 1, 5),
    _CpqFcTapeCntlrWWN_Type()
)
cpqFcTapeCntlrWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCntlrWWN.setStatus("mandatory")


class _CpqFcTapeCntlrFWRev_Type(DisplayString):
    """Custom type cpqFcTapeCntlrFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqFcTapeCntlrFWRev_Type.__name__ = "DisplayString"
_CpqFcTapeCntlrFWRev_Object = MibTableColumn
cpqFcTapeCntlrFWRev = _CpqFcTapeCntlrFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1, 1, 6),
    _CpqFcTapeCntlrFWRev_Type()
)
cpqFcTapeCntlrFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCntlrFWRev.setStatus("mandatory")


class _CpqFcTapeCntlrType_Type(Integer32):
    """Custom type cpqFcTapeCntlrType based on Integer32"""
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
        *(("extended", 4),
          ("fiberTape", 2),
          ("modularDataRouter", 3),
          ("other", 1))
    )


_CpqFcTapeCntlrType_Type.__name__ = "Integer32"
_CpqFcTapeCntlrType_Object = MibTableColumn
cpqFcTapeCntlrType = _CpqFcTapeCntlrType_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1, 1, 7),
    _CpqFcTapeCntlrType_Type()
)
cpqFcTapeCntlrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCntlrType.setStatus("mandatory")


class _CpqFcTapeCntlrModel_Type(DisplayString):
    """Custom type cpqFcTapeCntlrModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqFcTapeCntlrModel_Type.__name__ = "DisplayString"
_CpqFcTapeCntlrModel_Object = MibTableColumn
cpqFcTapeCntlrModel = _CpqFcTapeCntlrModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1, 1, 8),
    _CpqFcTapeCntlrModel_Type()
)
cpqFcTapeCntlrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCntlrModel.setStatus("mandatory")


class _CpqFcTapeCntlrSerialNumber_Type(DisplayString):
    """Custom type cpqFcTapeCntlrSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqFcTapeCntlrSerialNumber_Type.__name__ = "DisplayString"
_CpqFcTapeCntlrSerialNumber_Object = MibTableColumn
cpqFcTapeCntlrSerialNumber = _CpqFcTapeCntlrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 1, 1, 1, 9),
    _CpqFcTapeCntlrSerialNumber_Type()
)
cpqFcTapeCntlrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCntlrSerialNumber.setStatus("mandatory")
_CpqFcTapeLibrary_ObjectIdentity = ObjectIdentity
cpqFcTapeLibrary = _CpqFcTapeLibrary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2)
)
_CpqFcTapeLibraryTable_Object = MibTable
cpqFcTapeLibraryTable = _CpqFcTapeLibraryTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cpqFcTapeLibraryTable.setStatus("mandatory")
_CpqFcTapeLibraryEntry_Object = MibTableRow
cpqFcTapeLibraryEntry = _CpqFcTapeLibraryEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1)
)
cpqFcTapeLibraryEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcTapeLibraryCntlrIndex"),
    (0, "CPQFCA-MIB", "cpqFcTapeLibraryScsiBus"),
    (0, "CPQFCA-MIB", "cpqFcTapeLibraryScsiTarget"),
    (0, "CPQFCA-MIB", "cpqFcTapeLibraryScsiLun"),
)
if mibBuilder.loadTexts:
    cpqFcTapeLibraryEntry.setStatus("mandatory")


class _CpqFcTapeLibraryCntlrIndex_Type(Integer32):
    """Custom type cpqFcTapeLibraryCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcTapeLibraryCntlrIndex_Type.__name__ = "Integer32"
_CpqFcTapeLibraryCntlrIndex_Object = MibTableColumn
cpqFcTapeLibraryCntlrIndex = _CpqFcTapeLibraryCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 1),
    _CpqFcTapeLibraryCntlrIndex_Type()
)
cpqFcTapeLibraryCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryCntlrIndex.setStatus("mandatory")


class _CpqFcTapeLibraryScsiBus_Type(Integer32):
    """Custom type cpqFcTapeLibraryScsiBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcTapeLibraryScsiBus_Type.__name__ = "Integer32"
_CpqFcTapeLibraryScsiBus_Object = MibTableColumn
cpqFcTapeLibraryScsiBus = _CpqFcTapeLibraryScsiBus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 2),
    _CpqFcTapeLibraryScsiBus_Type()
)
cpqFcTapeLibraryScsiBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryScsiBus.setStatus("mandatory")


class _CpqFcTapeLibraryScsiTarget_Type(Integer32):
    """Custom type cpqFcTapeLibraryScsiTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcTapeLibraryScsiTarget_Type.__name__ = "Integer32"
_CpqFcTapeLibraryScsiTarget_Object = MibTableColumn
cpqFcTapeLibraryScsiTarget = _CpqFcTapeLibraryScsiTarget_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 3),
    _CpqFcTapeLibraryScsiTarget_Type()
)
cpqFcTapeLibraryScsiTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryScsiTarget.setStatus("mandatory")


class _CpqFcTapeLibraryScsiLun_Type(Integer32):
    """Custom type cpqFcTapeLibraryScsiLun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcTapeLibraryScsiLun_Type.__name__ = "Integer32"
_CpqFcTapeLibraryScsiLun_Object = MibTableColumn
cpqFcTapeLibraryScsiLun = _CpqFcTapeLibraryScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 4),
    _CpqFcTapeLibraryScsiLun_Type()
)
cpqFcTapeLibraryScsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryScsiLun.setStatus("mandatory")


class _CpqFcTapeLibrarySerialNumber_Type(DisplayString):
    """Custom type cpqFcTapeLibrarySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqFcTapeLibrarySerialNumber_Type.__name__ = "DisplayString"
_CpqFcTapeLibrarySerialNumber_Object = MibTableColumn
cpqFcTapeLibrarySerialNumber = _CpqFcTapeLibrarySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 5),
    _CpqFcTapeLibrarySerialNumber_Type()
)
cpqFcTapeLibrarySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibrarySerialNumber.setStatus("mandatory")


class _CpqFcTapeLibraryModel_Type(DisplayString):
    """Custom type cpqFcTapeLibraryModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqFcTapeLibraryModel_Type.__name__ = "DisplayString"
_CpqFcTapeLibraryModel_Object = MibTableColumn
cpqFcTapeLibraryModel = _CpqFcTapeLibraryModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 6),
    _CpqFcTapeLibraryModel_Type()
)
cpqFcTapeLibraryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryModel.setStatus("mandatory")


class _CpqFcTapeLibraryFWRev_Type(DisplayString):
    """Custom type cpqFcTapeLibraryFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqFcTapeLibraryFWRev_Type.__name__ = "DisplayString"
_CpqFcTapeLibraryFWRev_Object = MibTableColumn
cpqFcTapeLibraryFWRev = _CpqFcTapeLibraryFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 7),
    _CpqFcTapeLibraryFWRev_Type()
)
cpqFcTapeLibraryFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryFWRev.setStatus("mandatory")


class _CpqFcTapeLibraryStatus_Type(Integer32):
    """Custom type cpqFcTapeLibraryStatus based on Integer32"""
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
          ("failed", 4),
          ("offline", 5),
          ("ok", 2),
          ("other", 1))
    )


_CpqFcTapeLibraryStatus_Type.__name__ = "Integer32"
_CpqFcTapeLibraryStatus_Object = MibTableColumn
cpqFcTapeLibraryStatus = _CpqFcTapeLibraryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 8),
    _CpqFcTapeLibraryStatus_Type()
)
cpqFcTapeLibraryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryStatus.setStatus("mandatory")


class _CpqFcTapeLibraryDoorStatus_Type(Integer32):
    """Custom type cpqFcTapeLibraryDoorStatus based on Integer32"""
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
        *(("closed", 3),
          ("notSupported", 2),
          ("open", 4),
          ("other", 1))
    )


_CpqFcTapeLibraryDoorStatus_Type.__name__ = "Integer32"
_CpqFcTapeLibraryDoorStatus_Object = MibTableColumn
cpqFcTapeLibraryDoorStatus = _CpqFcTapeLibraryDoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 9),
    _CpqFcTapeLibraryDoorStatus_Type()
)
cpqFcTapeLibraryDoorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryDoorStatus.setStatus("mandatory")
_CpqFcTapeLibraryCondition_Type = Integer32
_CpqFcTapeLibraryCondition_Object = MibTableColumn
cpqFcTapeLibraryCondition = _CpqFcTapeLibraryCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 10),
    _CpqFcTapeLibraryCondition_Type()
)
cpqFcTapeLibraryCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryCondition.setStatus("mandatory")
_CpqFcTapeLibraryOverallCondition_Type = Integer32
_CpqFcTapeLibraryOverallCondition_Object = MibTableColumn
cpqFcTapeLibraryOverallCondition = _CpqFcTapeLibraryOverallCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 11),
    _CpqFcTapeLibraryOverallCondition_Type()
)
cpqFcTapeLibraryOverallCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryOverallCondition.setStatus("mandatory")


class _CpqFcTapeLibraryLastError_Type(Integer32):
    """Custom type cpqFcTapeLibraryLastError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcTapeLibraryLastError_Type.__name__ = "Integer32"
_CpqFcTapeLibraryLastError_Object = MibTableColumn
cpqFcTapeLibraryLastError = _CpqFcTapeLibraryLastError_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 12),
    _CpqFcTapeLibraryLastError_Type()
)
cpqFcTapeLibraryLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryLastError.setStatus("mandatory")
_CpqFcTapeLibraryStatHours_Type = Counter32
_CpqFcTapeLibraryStatHours_Object = MibTableColumn
cpqFcTapeLibraryStatHours = _CpqFcTapeLibraryStatHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 13),
    _CpqFcTapeLibraryStatHours_Type()
)
cpqFcTapeLibraryStatHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryStatHours.setStatus("mandatory")
_CpqFcTapeLibraryStatMoves_Type = Counter32
_CpqFcTapeLibraryStatMoves_Object = MibTableColumn
cpqFcTapeLibraryStatMoves = _CpqFcTapeLibraryStatMoves_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 14),
    _CpqFcTapeLibraryStatMoves_Type()
)
cpqFcTapeLibraryStatMoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryStatMoves.setStatus("mandatory")


class _CpqFcTapeLibraryDriveList_Type(OctetString):
    """Custom type cpqFcTapeLibraryDriveList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_CpqFcTapeLibraryDriveList_Type.__name__ = "OctetString"
_CpqFcTapeLibraryDriveList_Object = MibTableColumn
cpqFcTapeLibraryDriveList = _CpqFcTapeLibraryDriveList_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 15),
    _CpqFcTapeLibraryDriveList_Type()
)
cpqFcTapeLibraryDriveList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryDriveList.setStatus("mandatory")


class _CpqFcTapeLibraryLocation_Type(DisplayString):
    """Custom type cpqFcTapeLibraryLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqFcTapeLibraryLocation_Type.__name__ = "DisplayString"
_CpqFcTapeLibraryLocation_Object = MibTableColumn
cpqFcTapeLibraryLocation = _CpqFcTapeLibraryLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 16),
    _CpqFcTapeLibraryLocation_Type()
)
cpqFcTapeLibraryLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryLocation.setStatus("mandatory")


class _CpqFcTapeLibraryTemperature_Type(Integer32):
    """Custom type cpqFcTapeLibraryTemperature based on Integer32"""
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
        *(("maxTempExceeded", 5),
          ("notSupported", 2),
          ("ok", 3),
          ("other", 1),
          ("safeTempExceeded", 4))
    )


_CpqFcTapeLibraryTemperature_Type.__name__ = "Integer32"
_CpqFcTapeLibraryTemperature_Object = MibTableColumn
cpqFcTapeLibraryTemperature = _CpqFcTapeLibraryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 17),
    _CpqFcTapeLibraryTemperature_Type()
)
cpqFcTapeLibraryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryTemperature.setStatus("mandatory")


class _CpqFcTapeLibraryRedundancy_Type(Integer32):
    """Custom type cpqFcTapeLibraryRedundancy based on Integer32"""
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
        *(("active", 5),
          ("capable", 3),
          ("notCapable", 4),
          ("notSupported", 2),
          ("other", 1))
    )


_CpqFcTapeLibraryRedundancy_Type.__name__ = "Integer32"
_CpqFcTapeLibraryRedundancy_Object = MibTableColumn
cpqFcTapeLibraryRedundancy = _CpqFcTapeLibraryRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 18),
    _CpqFcTapeLibraryRedundancy_Type()
)
cpqFcTapeLibraryRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryRedundancy.setStatus("mandatory")


class _CpqFcTapeLibraryHotSwap_Type(Integer32):
    """Custom type cpqFcTapeLibraryHotSwap based on Integer32"""
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
        *(("capable", 3),
          ("notCapable", 4),
          ("notSupported", 2),
          ("other", 1))
    )


_CpqFcTapeLibraryHotSwap_Type.__name__ = "Integer32"
_CpqFcTapeLibraryHotSwap_Object = MibTableColumn
cpqFcTapeLibraryHotSwap = _CpqFcTapeLibraryHotSwap_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 2, 1, 1, 19),
    _CpqFcTapeLibraryHotSwap_Type()
)
cpqFcTapeLibraryHotSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeLibraryHotSwap.setStatus("mandatory")
_CpqFcTapeDrive_ObjectIdentity = ObjectIdentity
cpqFcTapeDrive = _CpqFcTapeDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3)
)
_CpqFcTapeDriveTable_Object = MibTable
cpqFcTapeDriveTable = _CpqFcTapeDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cpqFcTapeDriveTable.setStatus("mandatory")
_CpqFcTapeDriveEntry_Object = MibTableRow
cpqFcTapeDriveEntry = _CpqFcTapeDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1)
)
cpqFcTapeDriveEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcTapeDriveCntlrIndex"),
    (0, "CPQFCA-MIB", "cpqFcTapeDriveScsiBus"),
    (0, "CPQFCA-MIB", "cpqFcTapeDriveScsiTarget"),
    (0, "CPQFCA-MIB", "cpqFcTapeDriveScsiLun"),
)
if mibBuilder.loadTexts:
    cpqFcTapeDriveEntry.setStatus("mandatory")


class _CpqFcTapeDriveCntlrIndex_Type(Integer32):
    """Custom type cpqFcTapeDriveCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcTapeDriveCntlrIndex_Type.__name__ = "Integer32"
_CpqFcTapeDriveCntlrIndex_Object = MibTableColumn
cpqFcTapeDriveCntlrIndex = _CpqFcTapeDriveCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 1),
    _CpqFcTapeDriveCntlrIndex_Type()
)
cpqFcTapeDriveCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveCntlrIndex.setStatus("mandatory")


class _CpqFcTapeDriveScsiBus_Type(Integer32):
    """Custom type cpqFcTapeDriveScsiBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcTapeDriveScsiBus_Type.__name__ = "Integer32"
_CpqFcTapeDriveScsiBus_Object = MibTableColumn
cpqFcTapeDriveScsiBus = _CpqFcTapeDriveScsiBus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 2),
    _CpqFcTapeDriveScsiBus_Type()
)
cpqFcTapeDriveScsiBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveScsiBus.setStatus("mandatory")


class _CpqFcTapeDriveScsiTarget_Type(Integer32):
    """Custom type cpqFcTapeDriveScsiTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcTapeDriveScsiTarget_Type.__name__ = "Integer32"
_CpqFcTapeDriveScsiTarget_Object = MibTableColumn
cpqFcTapeDriveScsiTarget = _CpqFcTapeDriveScsiTarget_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 3),
    _CpqFcTapeDriveScsiTarget_Type()
)
cpqFcTapeDriveScsiTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveScsiTarget.setStatus("mandatory")


class _CpqFcTapeDriveScsiLun_Type(Integer32):
    """Custom type cpqFcTapeDriveScsiLun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcTapeDriveScsiLun_Type.__name__ = "Integer32"
_CpqFcTapeDriveScsiLun_Object = MibTableColumn
cpqFcTapeDriveScsiLun = _CpqFcTapeDriveScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 4),
    _CpqFcTapeDriveScsiLun_Type()
)
cpqFcTapeDriveScsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveScsiLun.setStatus("mandatory")


class _CpqFcTapeDriveSerialNumber_Type(DisplayString):
    """Custom type cpqFcTapeDriveSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqFcTapeDriveSerialNumber_Type.__name__ = "DisplayString"
_CpqFcTapeDriveSerialNumber_Object = MibTableColumn
cpqFcTapeDriveSerialNumber = _CpqFcTapeDriveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 5),
    _CpqFcTapeDriveSerialNumber_Type()
)
cpqFcTapeDriveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveSerialNumber.setStatus("mandatory")


class _CpqFcTapeDriveModel_Type(DisplayString):
    """Custom type cpqFcTapeDriveModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqFcTapeDriveModel_Type.__name__ = "DisplayString"
_CpqFcTapeDriveModel_Object = MibTableColumn
cpqFcTapeDriveModel = _CpqFcTapeDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 6),
    _CpqFcTapeDriveModel_Type()
)
cpqFcTapeDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveModel.setStatus("mandatory")


class _CpqFcTapeDriveFWRev_Type(DisplayString):
    """Custom type cpqFcTapeDriveFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqFcTapeDriveFWRev_Type.__name__ = "DisplayString"
_CpqFcTapeDriveFWRev_Object = MibTableColumn
cpqFcTapeDriveFWRev = _CpqFcTapeDriveFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 7),
    _CpqFcTapeDriveFWRev_Type()
)
cpqFcTapeDriveFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveFWRev.setStatus("mandatory")


class _CpqFcTapeDriveType_Type(Integer32):
    """Custom type cpqFcTapeDriveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpqDlt35-70", 2),
          ("other", 1))
    )


_CpqFcTapeDriveType_Type.__name__ = "Integer32"
_CpqFcTapeDriveType_Object = MibTableColumn
cpqFcTapeDriveType = _CpqFcTapeDriveType_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 8),
    _CpqFcTapeDriveType_Type()
)
cpqFcTapeDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveType.setStatus("deprecated")


class _CpqFcTapeDriveFWSubtype_Type(Integer32):
    """Custom type cpqFcTapeDriveFWSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcTapeDriveFWSubtype_Type.__name__ = "Integer32"
_CpqFcTapeDriveFWSubtype_Object = MibTableColumn
cpqFcTapeDriveFWSubtype = _CpqFcTapeDriveFWSubtype_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 9),
    _CpqFcTapeDriveFWSubtype_Type()
)
cpqFcTapeDriveFWSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveFWSubtype.setStatus("mandatory")


class _CpqFcTapeDriveStatus_Type(Integer32):
    """Custom type cpqFcTapeDriveStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("missingWasOffline", 7),
          ("missingWasOk", 6),
          ("offline", 5),
          ("ok", 2),
          ("other", 1))
    )


_CpqFcTapeDriveStatus_Type.__name__ = "Integer32"
_CpqFcTapeDriveStatus_Object = MibTableColumn
cpqFcTapeDriveStatus = _CpqFcTapeDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 10),
    _CpqFcTapeDriveStatus_Type()
)
cpqFcTapeDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveStatus.setStatus("mandatory")


class _CpqFcTapeDriveCleanReq_Type(Integer32):
    """Custom type cpqFcTapeDriveCleanReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("other", 1),
          ("true", 2))
    )


_CpqFcTapeDriveCleanReq_Type.__name__ = "Integer32"
_CpqFcTapeDriveCleanReq_Object = MibTableColumn
cpqFcTapeDriveCleanReq = _CpqFcTapeDriveCleanReq_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 11),
    _CpqFcTapeDriveCleanReq_Type()
)
cpqFcTapeDriveCleanReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveCleanReq.setStatus("mandatory")


class _CpqFcTapeDriveCleanTapeRepl_Type(Integer32):
    """Custom type cpqFcTapeDriveCleanTapeRepl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("other", 1),
          ("true", 2))
    )


_CpqFcTapeDriveCleanTapeRepl_Type.__name__ = "Integer32"
_CpqFcTapeDriveCleanTapeRepl_Object = MibTableColumn
cpqFcTapeDriveCleanTapeRepl = _CpqFcTapeDriveCleanTapeRepl_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 12),
    _CpqFcTapeDriveCleanTapeRepl_Type()
)
cpqFcTapeDriveCleanTapeRepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveCleanTapeRepl.setStatus("mandatory")
_CpqFcTapeDriveCondition_Type = Integer32
_CpqFcTapeDriveCondition_Object = MibTableColumn
cpqFcTapeDriveCondition = _CpqFcTapeDriveCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 13),
    _CpqFcTapeDriveCondition_Type()
)
cpqFcTapeDriveCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveCondition.setStatus("mandatory")
_CpqFcTapeDriveCleanTapeCount_Type = Integer32
_CpqFcTapeDriveCleanTapeCount_Object = MibTableColumn
cpqFcTapeDriveCleanTapeCount = _CpqFcTapeDriveCleanTapeCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 14),
    _CpqFcTapeDriveCleanTapeCount_Type()
)
cpqFcTapeDriveCleanTapeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveCleanTapeCount.setStatus("mandatory")


class _CpqFcTapeDriveLibraryDrive_Type(Integer32):
    """Custom type cpqFcTapeDriveLibraryDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("other", 1),
          ("true", 2))
    )


_CpqFcTapeDriveLibraryDrive_Type.__name__ = "Integer32"
_CpqFcTapeDriveLibraryDrive_Object = MibTableColumn
cpqFcTapeDriveLibraryDrive = _CpqFcTapeDriveLibraryDrive_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 15),
    _CpqFcTapeDriveLibraryDrive_Type()
)
cpqFcTapeDriveLibraryDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveLibraryDrive.setStatus("mandatory")


class _CpqFcTapeDriveLocation_Type(DisplayString):
    """Custom type cpqFcTapeDriveLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqFcTapeDriveLocation_Type.__name__ = "DisplayString"
_CpqFcTapeDriveLocation_Object = MibTableColumn
cpqFcTapeDriveLocation = _CpqFcTapeDriveLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 16),
    _CpqFcTapeDriveLocation_Type()
)
cpqFcTapeDriveLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveLocation.setStatus("mandatory")


class _CpqFcTapeDriveHotPlug_Type(Integer32):
    """Custom type cpqFcTapeDriveHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hotPlug", 2),
          ("nonHotPlug", 3),
          ("other", 1))
    )


_CpqFcTapeDriveHotPlug_Type.__name__ = "Integer32"
_CpqFcTapeDriveHotPlug_Object = MibTableColumn
cpqFcTapeDriveHotPlug = _CpqFcTapeDriveHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 17),
    _CpqFcTapeDriveHotPlug_Type()
)
cpqFcTapeDriveHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveHotPlug.setStatus("mandatory")
_CpqFcTapeDriveBay_Type = Integer32
_CpqFcTapeDriveBay_Object = MibTableColumn
cpqFcTapeDriveBay = _CpqFcTapeDriveBay_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 18),
    _CpqFcTapeDriveBay_Type()
)
cpqFcTapeDriveBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveBay.setStatus("mandatory")


class _CpqFcTapeDriveCurrentWidth_Type(Integer32):
    """Custom type cpqFcTapeDriveCurrentWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("narrow", 2),
          ("other", 1),
          ("wide16", 3))
    )


_CpqFcTapeDriveCurrentWidth_Type.__name__ = "Integer32"
_CpqFcTapeDriveCurrentWidth_Object = MibTableColumn
cpqFcTapeDriveCurrentWidth = _CpqFcTapeDriveCurrentWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 19),
    _CpqFcTapeDriveCurrentWidth_Type()
)
cpqFcTapeDriveCurrentWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveCurrentWidth.setStatus("mandatory")


class _CpqFcTapeDriveCurrentSpeed_Type(Integer32):
    """Custom type cpqFcTapeDriveCurrentSpeed based on Integer32"""
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
        *(("asynchronous", 2),
          ("fast", 3),
          ("other", 1),
          ("ultra", 4),
          ("ultra2", 5),
          ("ultra3", 6))
    )


_CpqFcTapeDriveCurrentSpeed_Type.__name__ = "Integer32"
_CpqFcTapeDriveCurrentSpeed_Object = MibTableColumn
cpqFcTapeDriveCurrentSpeed = _CpqFcTapeDriveCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 3, 1, 1, 20),
    _CpqFcTapeDriveCurrentSpeed_Type()
)
cpqFcTapeDriveCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeDriveCurrentSpeed.setStatus("mandatory")
_CpqFcTapeCounters_ObjectIdentity = ObjectIdentity
cpqFcTapeCounters = _CpqFcTapeCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4)
)
_CpqFcTapeCountersTable_Object = MibTable
cpqFcTapeCountersTable = _CpqFcTapeCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cpqFcTapeCountersTable.setStatus("mandatory")
_CpqFcTapeCountersEntry_Object = MibTableRow
cpqFcTapeCountersEntry = _CpqFcTapeCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1, 1)
)
cpqFcTapeCountersEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcTapeCountersCntlrIndex"),
    (0, "CPQFCA-MIB", "cpqFcTapeCountersScsiBus"),
    (0, "CPQFCA-MIB", "cpqFcTapeCountersScsiTarget"),
    (0, "CPQFCA-MIB", "cpqFcTapeCountersScsiLun"),
)
if mibBuilder.loadTexts:
    cpqFcTapeCountersEntry.setStatus("mandatory")


class _CpqFcTapeCountersCntlrIndex_Type(Integer32):
    """Custom type cpqFcTapeCountersCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcTapeCountersCntlrIndex_Type.__name__ = "Integer32"
_CpqFcTapeCountersCntlrIndex_Object = MibTableColumn
cpqFcTapeCountersCntlrIndex = _CpqFcTapeCountersCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1, 1, 1),
    _CpqFcTapeCountersCntlrIndex_Type()
)
cpqFcTapeCountersCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCountersCntlrIndex.setStatus("mandatory")


class _CpqFcTapeCountersScsiBus_Type(Integer32):
    """Custom type cpqFcTapeCountersScsiBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcTapeCountersScsiBus_Type.__name__ = "Integer32"
_CpqFcTapeCountersScsiBus_Object = MibTableColumn
cpqFcTapeCountersScsiBus = _CpqFcTapeCountersScsiBus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1, 1, 2),
    _CpqFcTapeCountersScsiBus_Type()
)
cpqFcTapeCountersScsiBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCountersScsiBus.setStatus("mandatory")


class _CpqFcTapeCountersScsiTarget_Type(Integer32):
    """Custom type cpqFcTapeCountersScsiTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcTapeCountersScsiTarget_Type.__name__ = "Integer32"
_CpqFcTapeCountersScsiTarget_Object = MibTableColumn
cpqFcTapeCountersScsiTarget = _CpqFcTapeCountersScsiTarget_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1, 1, 3),
    _CpqFcTapeCountersScsiTarget_Type()
)
cpqFcTapeCountersScsiTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCountersScsiTarget.setStatus("mandatory")


class _CpqFcTapeCountersScsiLun_Type(Integer32):
    """Custom type cpqFcTapeCountersScsiLun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcTapeCountersScsiLun_Type.__name__ = "Integer32"
_CpqFcTapeCountersScsiLun_Object = MibTableColumn
cpqFcTapeCountersScsiLun = _CpqFcTapeCountersScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1, 1, 4),
    _CpqFcTapeCountersScsiLun_Type()
)
cpqFcTapeCountersScsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCountersScsiLun.setStatus("mandatory")
_CpqFcTapeCountersReWrites_Type = Counter32
_CpqFcTapeCountersReWrites_Object = MibTableColumn
cpqFcTapeCountersReWrites = _CpqFcTapeCountersReWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1, 1, 5),
    _CpqFcTapeCountersReWrites_Type()
)
cpqFcTapeCountersReWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCountersReWrites.setStatus("mandatory")
_CpqFcTapeCountersReReads_Type = Counter32
_CpqFcTapeCountersReReads_Object = MibTableColumn
cpqFcTapeCountersReReads = _CpqFcTapeCountersReReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1, 1, 6),
    _CpqFcTapeCountersReReads_Type()
)
cpqFcTapeCountersReReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCountersReReads.setStatus("mandatory")
_CpqFcTapeCountersTotalErrors_Type = Counter32
_CpqFcTapeCountersTotalErrors_Object = MibTableColumn
cpqFcTapeCountersTotalErrors = _CpqFcTapeCountersTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1, 1, 7),
    _CpqFcTapeCountersTotalErrors_Type()
)
cpqFcTapeCountersTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCountersTotalErrors.setStatus("mandatory")
_CpqFcTapeCountersTotalUncorrectable_Type = Counter32
_CpqFcTapeCountersTotalUncorrectable_Object = MibTableColumn
cpqFcTapeCountersTotalUncorrectable = _CpqFcTapeCountersTotalUncorrectable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1, 1, 8),
    _CpqFcTapeCountersTotalUncorrectable_Type()
)
cpqFcTapeCountersTotalUncorrectable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCountersTotalUncorrectable.setStatus("mandatory")
_CpqFcTapeCountersTotalBytes_Type = Counter32
_CpqFcTapeCountersTotalBytes_Object = MibTableColumn
cpqFcTapeCountersTotalBytes = _CpqFcTapeCountersTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 3, 4, 1, 1, 9),
    _CpqFcTapeCountersTotalBytes_Type()
)
cpqFcTapeCountersTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcTapeCountersTotalBytes.setStatus("mandatory")
_CpqFcSwitchComponent_ObjectIdentity = ObjectIdentity
cpqFcSwitchComponent = _CpqFcSwitchComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 4)
)
_CpqFcSwitch_ObjectIdentity = ObjectIdentity
cpqFcSwitch = _CpqFcSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1)
)
_CpqFcSwitchTable_Object = MibTable
cpqFcSwitchTable = _CpqFcSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cpqFcSwitchTable.setStatus("mandatory")
_CpqFcSwitchEntry_Object = MibTableRow
cpqFcSwitchEntry = _CpqFcSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1)
)
cpqFcSwitchEntry.setIndexNames(
    (0, "CPQFCA-MIB", "cpqFcSwitchIndex"),
)
if mibBuilder.loadTexts:
    cpqFcSwitchEntry.setStatus("mandatory")


class _CpqFcSwitchIndex_Type(Integer32):
    """Custom type cpqFcSwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcSwitchIndex_Type.__name__ = "Integer32"
_CpqFcSwitchIndex_Object = MibTableColumn
cpqFcSwitchIndex = _CpqFcSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 1),
    _CpqFcSwitchIndex_Type()
)
cpqFcSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchIndex.setStatus("mandatory")


class _CpqFcSwitchLocation_Type(Integer32):
    """Custom type cpqFcSwitchLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("other", 1))
    )


_CpqFcSwitchLocation_Type.__name__ = "Integer32"
_CpqFcSwitchLocation_Object = MibTableColumn
cpqFcSwitchLocation = _CpqFcSwitchLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 2),
    _CpqFcSwitchLocation_Type()
)
cpqFcSwitchLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchLocation.setStatus("mandatory")


class _CpqFcSwitchChassisIndex_Type(Integer32):
    """Custom type cpqFcSwitchChassisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqFcSwitchChassisIndex_Type.__name__ = "Integer32"
_CpqFcSwitchChassisIndex_Object = MibTableColumn
cpqFcSwitchChassisIndex = _CpqFcSwitchChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 3),
    _CpqFcSwitchChassisIndex_Type()
)
cpqFcSwitchChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchChassisIndex.setStatus("mandatory")


class _CpqFcSwitchChassisSlot_Type(Integer32):
    """Custom type cpqFcSwitchChassisSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqFcSwitchChassisSlot_Type.__name__ = "Integer32"
_CpqFcSwitchChassisSlot_Object = MibTableColumn
cpqFcSwitchChassisSlot = _CpqFcSwitchChassisSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 4),
    _CpqFcSwitchChassisSlot_Type()
)
cpqFcSwitchChassisSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchChassisSlot.setStatus("mandatory")


class _CpqFcSwitchWorldWideNodeName_Type(DisplayString):
    """Custom type cpqFcSwitchWorldWideNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqFcSwitchWorldWideNodeName_Type.__name__ = "DisplayString"
_CpqFcSwitchWorldWideNodeName_Object = MibTableColumn
cpqFcSwitchWorldWideNodeName = _CpqFcSwitchWorldWideNodeName_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 5),
    _CpqFcSwitchWorldWideNodeName_Type()
)
cpqFcSwitchWorldWideNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchWorldWideNodeName.setStatus("mandatory")


class _CpqFcSwitchWorldWidePortName_Type(DisplayString):
    """Custom type cpqFcSwitchWorldWidePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqFcSwitchWorldWidePortName_Type.__name__ = "DisplayString"
_CpqFcSwitchWorldWidePortName_Object = MibTableColumn
cpqFcSwitchWorldWidePortName = _CpqFcSwitchWorldWidePortName_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 6),
    _CpqFcSwitchWorldWidePortName_Type()
)
cpqFcSwitchWorldWidePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchWorldWidePortName.setStatus("mandatory")


class _CpqFcSwitchIpAddress_Type(DisplayString):
    """Custom type cpqFcSwitchIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqFcSwitchIpAddress_Type.__name__ = "DisplayString"
_CpqFcSwitchIpAddress_Object = MibTableColumn
cpqFcSwitchIpAddress = _CpqFcSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 7),
    _CpqFcSwitchIpAddress_Type()
)
cpqFcSwitchIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchIpAddress.setStatus("mandatory")


class _CpqFcSwitchIpGateway_Type(DisplayString):
    """Custom type cpqFcSwitchIpGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqFcSwitchIpGateway_Type.__name__ = "DisplayString"
_CpqFcSwitchIpGateway_Object = MibTableColumn
cpqFcSwitchIpGateway = _CpqFcSwitchIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 8),
    _CpqFcSwitchIpGateway_Type()
)
cpqFcSwitchIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchIpGateway.setStatus("mandatory")


class _CpqFcSwitchIpSubnet_Type(DisplayString):
    """Custom type cpqFcSwitchIpSubnet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqFcSwitchIpSubnet_Type.__name__ = "DisplayString"
_CpqFcSwitchIpSubnet_Object = MibTableColumn
cpqFcSwitchIpSubnet = _CpqFcSwitchIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 9),
    _CpqFcSwitchIpSubnet_Type()
)
cpqFcSwitchIpSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchIpSubnet.setStatus("mandatory")


class _CpqFcSwitchName_Type(DisplayString):
    """Custom type cpqFcSwitchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqFcSwitchName_Type.__name__ = "DisplayString"
_CpqFcSwitchName_Object = MibTableColumn
cpqFcSwitchName = _CpqFcSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 10),
    _CpqFcSwitchName_Type()
)
cpqFcSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchName.setStatus("mandatory")


class _CpqFcSwitchNetworkLinkStatus_Type(Integer32):
    """Custom type cpqFcSwitchNetworkLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 3),
          ("other", 1))
    )


_CpqFcSwitchNetworkLinkStatus_Type.__name__ = "Integer32"
_CpqFcSwitchNetworkLinkStatus_Object = MibTableColumn
cpqFcSwitchNetworkLinkStatus = _CpqFcSwitchNetworkLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 11),
    _CpqFcSwitchNetworkLinkStatus_Type()
)
cpqFcSwitchNetworkLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchNetworkLinkStatus.setStatus("mandatory")


class _CpqFcSwitchFibreConnectStatus_Type(Integer32):
    """Custom type cpqFcSwitchFibreConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqFcSwitchFibreConnectStatus_Type.__name__ = "Integer32"
_CpqFcSwitchFibreConnectStatus_Object = MibTableColumn
cpqFcSwitchFibreConnectStatus = _CpqFcSwitchFibreConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 12),
    _CpqFcSwitchFibreConnectStatus_Type()
)
cpqFcSwitchFibreConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchFibreConnectStatus.setStatus("mandatory")


class _CpqFcSwitchFWRev_Type(DisplayString):
    """Custom type cpqFcSwitchFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqFcSwitchFWRev_Type.__name__ = "DisplayString"
_CpqFcSwitchFWRev_Object = MibTableColumn
cpqFcSwitchFWRev = _CpqFcSwitchFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 16, 4, 1, 1, 1, 13),
    _CpqFcSwitchFWRev_Type()
)
cpqFcSwitchFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqFcSwitchFWRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqFcaLogDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16001)
)
cpqFcaLogDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaLogDrvIndex"),
        ("CPQFCA-MIB", "cpqFcaLogDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqFcaLogDrvStatusChange.setStatus(
        ""
    )

cpqFcaSpareStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16002)
)
cpqFcaSpareStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaSpareBusNumber"),
        ("CPQFCA-MIB", "cpqFcaSpareBay"),
        ("CPQFCA-MIB", "cpqFcaSpareStatus"))
)
if mibBuilder.loadTexts:
    cpqFcaSpareStatusChange.setStatus(
        ""
    )

cpqFcaPhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16003)
)
cpqFcaPhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaPhyDrvBusNumber"),
        ("CPQFCA-MIB", "cpqFcaPhyDrvBay"),
        ("CPQFCA-MIB", "cpqFcaPhyDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqFcaPhyDrvStatusChange.setStatus(
        ""
    )

cpqFcaAccelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16004)
)
cpqFcaAccelStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaAccelBoxIoSlot"),
        ("CPQFCA-MIB", "cpqFcaAccelStatus"))
)
if mibBuilder.loadTexts:
    cpqFcaAccelStatusChange.setStatus(
        ""
    )

cpqFcaAccelBadDataTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16005)
)
cpqFcaAccelBadDataTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaAccelBoxIoSlot"))
)
if mibBuilder.loadTexts:
    cpqFcaAccelBadDataTrap.setStatus(
        ""
    )

cpqFcaAccelBatteryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16006)
)
cpqFcaAccelBatteryFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaAccelBoxIoSlot"))
)
if mibBuilder.loadTexts:
    cpqFcaAccelBatteryFailed.setStatus(
        ""
    )

cpqFcaCntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16007)
)
cpqFcaCntlrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaCntlrBoxIoSlot"),
        ("CPQFCA-MIB", "cpqFcaCntlrStatus"))
)
if mibBuilder.loadTexts:
    cpqFcaCntlrStatusChange.setStatus(
        ""
    )

cpqFcTapeCntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16008)
)
cpqFcTapeCntlrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeCntlrWWN"),
        ("CPQFCA-MIB", "cpqFcTapeCntlrStatus"))
)
if mibBuilder.loadTexts:
    cpqFcTapeCntlrStatusChange.setStatus(
        ""
    )

cpqFcTapeLibraryStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16009)
)
cpqFcTapeLibraryStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeCntlrWWN"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiBus"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiTarget"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiLun"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryStatus"))
)
if mibBuilder.loadTexts:
    cpqFcTapeLibraryStatusChange.setStatus(
        ""
    )

cpqFcTapeLibraryDoorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16010)
)
cpqFcTapeLibraryDoorStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeCntlrWWN"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiBus"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiTarget"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiLun"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryDoorStatus"))
)
if mibBuilder.loadTexts:
    cpqFcTapeLibraryDoorStatusChange.setStatus(
        ""
    )

cpqFcTapeDriveStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16011)
)
cpqFcTapeDriveStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeCntlrWWN"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiBus"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiTarget"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiLun"),
        ("CPQFCA-MIB", "cpqFcTapeDriveStatus"))
)
if mibBuilder.loadTexts:
    cpqFcTapeDriveStatusChange.setStatus(
        ""
    )

cpqFcTapeDriveCleaningRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16012)
)
cpqFcTapeDriveCleaningRequired.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeCntlrWWN"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiBus"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiTarget"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiLun"))
)
if mibBuilder.loadTexts:
    cpqFcTapeDriveCleaningRequired.setStatus(
        ""
    )

cpqFcTapeDriveCleanTapeReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16013)
)
cpqFcTapeDriveCleanTapeReplace.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeCntlrWWN"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiBus"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiTarget"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiLun"))
)
if mibBuilder.loadTexts:
    cpqFcTapeDriveCleanTapeReplace.setStatus(
        ""
    )

cpqFcaCntlrActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16014)
)
cpqFcaCntlrActive.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaCntlrBoxIoSlot"))
)
if mibBuilder.loadTexts:
    cpqFcaCntlrActive.setStatus(
        ""
    )

cpqFcaHostCntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16015)
)
cpqFcaHostCntlrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrSlot"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrStatus"))
)
if mibBuilder.loadTexts:
    cpqFcaHostCntlrStatusChange.setStatus(
        ""
    )

cpqFca2PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16016)
)
cpqFca2PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaPhyDrvBusNumber"),
        ("CPQFCA-MIB", "cpqFcaPhyDrvBay"),
        ("CPQFCA-MIB", "cpqFcaPhyDrvStatus"),
        ("CPQFCA-MIB", "cpqFcaPhyDrvModel"),
        ("CPQFCA-MIB", "cpqFcaPhyDrvSerialNum"),
        ("CPQFCA-MIB", "cpqFcaPhyDrvFWRev"),
        ("CPQFCA-MIB", "cpqFcaPhyDrvFailureCode"))
)
if mibBuilder.loadTexts:
    cpqFca2PhyDrvStatusChange.setStatus(
        ""
    )

cpqFca2AccelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16017)
)
cpqFca2AccelStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaAccelBoxIoSlot"),
        ("CPQFCA-MIB", "cpqFcaAccelStatus"),
        ("CPQFCA-MIB", "cpqFcaCntlrModel"),
        ("CPQFCA-MIB", "cpqFcaAccelSerialNumber"),
        ("CPQFCA-MIB", "cpqFcaAccelTotalMemory"),
        ("CPQFCA-MIB", "cpqFcaAccelErrCode"))
)
if mibBuilder.loadTexts:
    cpqFca2AccelStatusChange.setStatus(
        ""
    )

cpqFca2AccelBadDataTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16018)
)
cpqFca2AccelBadDataTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaAccelBoxIoSlot"),
        ("CPQFCA-MIB", "cpqFcaCntlrModel"),
        ("CPQFCA-MIB", "cpqFcaAccelSerialNumber"),
        ("CPQFCA-MIB", "cpqFcaAccelTotalMemory"))
)
if mibBuilder.loadTexts:
    cpqFca2AccelBadDataTrap.setStatus(
        ""
    )

cpqFca2AccelBatteryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16019)
)
cpqFca2AccelBatteryFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaAccelBoxIoSlot"),
        ("CPQFCA-MIB", "cpqFcaCntlrModel"),
        ("CPQFCA-MIB", "cpqFcaAccelSerialNumber"),
        ("CPQFCA-MIB", "cpqFcaAccelTotalMemory"))
)
if mibBuilder.loadTexts:
    cpqFca2AccelBatteryFailed.setStatus(
        ""
    )

cpqFca2CntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16020)
)
cpqFca2CntlrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaCntlrBoxIoSlot"),
        ("CPQFCA-MIB", "cpqFcaCntlrStatus"),
        ("CPQFCA-MIB", "cpqFcaCntlrModel"),
        ("CPQFCA-MIB", "cpqFcaCntlrSerialNumber"),
        ("CPQFCA-MIB", "cpqFcaAccelTotalMemory"))
)
if mibBuilder.loadTexts:
    cpqFca2CntlrStatusChange.setStatus(
        ""
    )

cpqFca2HostCntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16021)
)
cpqFca2HostCntlrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrSlot"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrStatus"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrModel"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrWorldWideName"))
)
if mibBuilder.loadTexts:
    cpqFca2HostCntlrStatusChange.setStatus(
        ""
    )

cpqExtArrayLogDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16022)
)
cpqExtArrayLogDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQSTSYS-MIB", "cpqSsChassisName"),
        ("CPQSTSYS-MIB", "cpqSsChassisTime"),
        ("CPQFCA-MIB", "cpqFcaLogDrvBoxIndex"),
        ("CPQFCA-MIB", "cpqFcaLogDrvIndex"),
        ("CPQFCA-MIB", "cpqFcaLogDrvStatus"),
        ("CPQFCA-MIB", "cpqFcaLogDrvOsName"),
        ("CPQFCA-MIB", "cpqFcaLogDrvFaultTol"),
        ("CPQFCA-MIB", "cpqFcaLogDrvSize"))
)
if mibBuilder.loadTexts:
    cpqExtArrayLogDrvStatusChange.setStatus(
        ""
    )

cpqExtTapeDriveStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16023)
)
cpqExtTapeDriveStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeDriveCntlrIndex"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiBus"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiTarget"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiLun"),
        ("CPQFCA-MIB", "cpqFcTapeDriveModel"),
        ("CPQFCA-MIB", "cpqFcTapeDriveFWRev"),
        ("CPQFCA-MIB", "cpqFcTapeDriveSerialNumber"),
        ("CPQFCA-MIB", "cpqFcTapeDriveLocation"),
        ("CPQFCA-MIB", "cpqFcTapeDriveStatus"))
)
if mibBuilder.loadTexts:
    cpqExtTapeDriveStatusChange.setStatus(
        ""
    )

cpqExtTapeDriveCleaningRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16024)
)
cpqExtTapeDriveCleaningRequired.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeDriveCntlrIndex"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiBus"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiTarget"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiLun"),
        ("CPQFCA-MIB", "cpqFcTapeDriveModel"),
        ("CPQFCA-MIB", "cpqFcTapeDriveFWRev"),
        ("CPQFCA-MIB", "cpqFcTapeDriveSerialNumber"),
        ("CPQFCA-MIB", "cpqFcTapeDriveLocation"))
)
if mibBuilder.loadTexts:
    cpqExtTapeDriveCleaningRequired.setStatus(
        ""
    )

cpqExtTapeDriveCleanTapeReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16025)
)
cpqExtTapeDriveCleanTapeReplace.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeDriveCntlrIndex"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiBus"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiTarget"),
        ("CPQFCA-MIB", "cpqFcTapeDriveScsiLun"),
        ("CPQFCA-MIB", "cpqFcTapeDriveModel"),
        ("CPQFCA-MIB", "cpqFcTapeDriveFWRev"),
        ("CPQFCA-MIB", "cpqFcTapeDriveSerialNumber"),
        ("CPQFCA-MIB", "cpqFcTapeDriveLocation"))
)
if mibBuilder.loadTexts:
    cpqExtTapeDriveCleanTapeReplace.setStatus(
        ""
    )

cpqExtTapeLibraryStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16026)
)
cpqExtTapeLibraryStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryCntlrIndex"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiBus"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiTarget"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiLun"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryModel"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryFWRev"),
        ("CPQFCA-MIB", "cpqFcTapeLibrarySerialNumber"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryLocation"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryStatus"))
)
if mibBuilder.loadTexts:
    cpqExtTapeLibraryStatusChange.setStatus(
        ""
    )

cpqExtTapeLibraryDoorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16027)
)
cpqExtTapeLibraryDoorStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryCntlrIndex"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiBus"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiTarget"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryScsiLun"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryModel"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryFWRev"),
        ("CPQFCA-MIB", "cpqFcTapeLibrarySerialNumber"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryLocation"),
        ("CPQFCA-MIB", "cpqFcTapeLibraryDoorStatus"))
)
if mibBuilder.loadTexts:
    cpqExtTapeLibraryDoorStatusChange.setStatus(
        ""
    )

cpqFca3HostCntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 16028)
)
cpqFca3HostCntlrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrHwLocation"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrIndex"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrStatus"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrModel"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrSerialNumber"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrWorldWideName"),
        ("CPQFCA-MIB", "cpqFcaHostCntlrWorldWidePortName"))
)
if mibBuilder.loadTexts:
    cpqFca3HostCntlrStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQFCA-MIB",
    **{"cpqFcaLogDrvStatusChange": cpqFcaLogDrvStatusChange,
       "cpqFcaSpareStatusChange": cpqFcaSpareStatusChange,
       "cpqFcaPhyDrvStatusChange": cpqFcaPhyDrvStatusChange,
       "cpqFcaAccelStatusChange": cpqFcaAccelStatusChange,
       "cpqFcaAccelBadDataTrap": cpqFcaAccelBadDataTrap,
       "cpqFcaAccelBatteryFailed": cpqFcaAccelBatteryFailed,
       "cpqFcaCntlrStatusChange": cpqFcaCntlrStatusChange,
       "cpqFcTapeCntlrStatusChange": cpqFcTapeCntlrStatusChange,
       "cpqFcTapeLibraryStatusChange": cpqFcTapeLibraryStatusChange,
       "cpqFcTapeLibraryDoorStatusChange": cpqFcTapeLibraryDoorStatusChange,
       "cpqFcTapeDriveStatusChange": cpqFcTapeDriveStatusChange,
       "cpqFcTapeDriveCleaningRequired": cpqFcTapeDriveCleaningRequired,
       "cpqFcTapeDriveCleanTapeReplace": cpqFcTapeDriveCleanTapeReplace,
       "cpqFcaCntlrActive": cpqFcaCntlrActive,
       "cpqFcaHostCntlrStatusChange": cpqFcaHostCntlrStatusChange,
       "cpqFca2PhyDrvStatusChange": cpqFca2PhyDrvStatusChange,
       "cpqFca2AccelStatusChange": cpqFca2AccelStatusChange,
       "cpqFca2AccelBadDataTrap": cpqFca2AccelBadDataTrap,
       "cpqFca2AccelBatteryFailed": cpqFca2AccelBatteryFailed,
       "cpqFca2CntlrStatusChange": cpqFca2CntlrStatusChange,
       "cpqFca2HostCntlrStatusChange": cpqFca2HostCntlrStatusChange,
       "cpqExtArrayLogDrvStatusChange": cpqExtArrayLogDrvStatusChange,
       "cpqExtTapeDriveStatusChange": cpqExtTapeDriveStatusChange,
       "cpqExtTapeDriveCleaningRequired": cpqExtTapeDriveCleaningRequired,
       "cpqExtTapeDriveCleanTapeReplace": cpqExtTapeDriveCleanTapeReplace,
       "cpqExtTapeLibraryStatusChange": cpqExtTapeLibraryStatusChange,
       "cpqExtTapeLibraryDoorStatusChange": cpqExtTapeLibraryDoorStatusChange,
       "cpqFca3HostCntlrStatusChange": cpqFca3HostCntlrStatusChange,
       "cpqFibreArray": cpqFibreArray,
       "cpqFcaMibRev": cpqFcaMibRev,
       "cpqFcaMibRevMajor": cpqFcaMibRevMajor,
       "cpqFcaMibRevMinor": cpqFcaMibRevMinor,
       "cpqFcaMibCondition": cpqFcaMibCondition,
       "cpqFcaComponent": cpqFcaComponent,
       "cpqFcaInterface": cpqFcaInterface,
       "cpqFcaOsCommon": cpqFcaOsCommon,
       "cpqFcaOsCommonPollFreq": cpqFcaOsCommonPollFreq,
       "cpqFcaOsCommonModuleTable": cpqFcaOsCommonModuleTable,
       "cpqFcaOsCommonModuleEntry": cpqFcaOsCommonModuleEntry,
       "cpqFcaOsCommonModuleIndex": cpqFcaOsCommonModuleIndex,
       "cpqFcaOsCommonModuleName": cpqFcaOsCommonModuleName,
       "cpqFcaOsCommonModuleVersion": cpqFcaOsCommonModuleVersion,
       "cpqFcaOsCommonModuleDate": cpqFcaOsCommonModuleDate,
       "cpqFcaOsCommonModulePurpose": cpqFcaOsCommonModulePurpose,
       "cpqFcaCntlr": cpqFcaCntlr,
       "cpqFcaCntlrTable": cpqFcaCntlrTable,
       "cpqFcaCntlrEntry": cpqFcaCntlrEntry,
       "cpqFcaCntlrBoxIndex": cpqFcaCntlrBoxIndex,
       "cpqFcaCntlrBoxIoSlot": cpqFcaCntlrBoxIoSlot,
       "cpqFcaCntlrModel": cpqFcaCntlrModel,
       "cpqFcaCntlrFWRev": cpqFcaCntlrFWRev,
       "cpqFcaCntlrStatus": cpqFcaCntlrStatus,
       "cpqFcaCntlrCondition": cpqFcaCntlrCondition,
       "cpqFcaCntlrProductRev": cpqFcaCntlrProductRev,
       "cpqFcaCntlrWorldWideName": cpqFcaCntlrWorldWideName,
       "cpqFcaCntlrSerialNumber": cpqFcaCntlrSerialNumber,
       "cpqFcaCntlrCurrentRole": cpqFcaCntlrCurrentRole,
       "cpqFcaCntlrRedundancyType": cpqFcaCntlrRedundancyType,
       "cpqFcaCntlrRedundancyError": cpqFcaCntlrRedundancyError,
       "cpqFcaCntlrBlinkTime": cpqFcaCntlrBlinkTime,
       "cpqFcaCntlrWorldWideNodeName": cpqFcaCntlrWorldWideNodeName,
       "cpqFcaCntlrRebuildPriority": cpqFcaCntlrRebuildPriority,
       "cpqFcaCntlrExpandPriority": cpqFcaCntlrExpandPriority,
       "cpqFcaAccelTable": cpqFcaAccelTable,
       "cpqFcaAccelEntry": cpqFcaAccelEntry,
       "cpqFcaAccelBoxIndex": cpqFcaAccelBoxIndex,
       "cpqFcaAccelBoxIoSlot": cpqFcaAccelBoxIoSlot,
       "cpqFcaAccelStatus": cpqFcaAccelStatus,
       "cpqFcaAccelBadData": cpqFcaAccelBadData,
       "cpqFcaAccelErrCode": cpqFcaAccelErrCode,
       "cpqFcaAccelBatteryStatus": cpqFcaAccelBatteryStatus,
       "cpqFcaAccelReadErrs": cpqFcaAccelReadErrs,
       "cpqFcaAccelWriteErrs": cpqFcaAccelWriteErrs,
       "cpqFcaAccelCondition": cpqFcaAccelCondition,
       "cpqFcaAccelWriteCache": cpqFcaAccelWriteCache,
       "cpqFcaAccelReadCache": cpqFcaAccelReadCache,
       "cpqFcaAccelSerialNumber": cpqFcaAccelSerialNumber,
       "cpqFcaAccelTotalMemory": cpqFcaAccelTotalMemory,
       "cpqFcaAccelFailedBatteries": cpqFcaAccelFailedBatteries,
       "cpqFcaLogDrv": cpqFcaLogDrv,
       "cpqFcaLogDrvTable": cpqFcaLogDrvTable,
       "cpqFcaLogDrvEntry": cpqFcaLogDrvEntry,
       "cpqFcaLogDrvBoxIndex": cpqFcaLogDrvBoxIndex,
       "cpqFcaLogDrvIndex": cpqFcaLogDrvIndex,
       "cpqFcaLogDrvFaultTol": cpqFcaLogDrvFaultTol,
       "cpqFcaLogDrvStatus": cpqFcaLogDrvStatus,
       "cpqFcaLogDrvAutoRel": cpqFcaLogDrvAutoRel,
       "cpqFcaLogDrvPercentRebuild": cpqFcaLogDrvPercentRebuild,
       "cpqFcaLogDrvHasAccel": cpqFcaLogDrvHasAccel,
       "cpqFcaLogDrvAvailSpares": cpqFcaLogDrvAvailSpares,
       "cpqFcaLogDrvSize": cpqFcaLogDrvSize,
       "cpqFcaLogDrvPhyDrvIDs": cpqFcaLogDrvPhyDrvIDs,
       "cpqFcaLogDrvCondition": cpqFcaLogDrvCondition,
       "cpqFcaLogDrvStripeSize": cpqFcaLogDrvStripeSize,
       "cpqFcaLogDrvOsName": cpqFcaLogDrvOsName,
       "cpqFcaLogDrvBlinkTime": cpqFcaLogDrvBlinkTime,
       "cpqFcaLogDrvSpareReplaceMap": cpqFcaLogDrvSpareReplaceMap,
       "cpqFcaLogDrvRebuildingPhyDrv": cpqFcaLogDrvRebuildingPhyDrv,
       "cpqFcaLogDrvSnapshotResourceDrvIndex": cpqFcaLogDrvSnapshotResourceDrvIndex,
       "cpqFcaLogDrvSnapshotSourceDrvIndex": cpqFcaLogDrvSnapshotSourceDrvIndex,
       "cpqFcaLogDrvPreferredPath": cpqFcaLogDrvPreferredPath,
       "cpqFcaLogDrvCurrentPath": cpqFcaLogDrvCurrentPath,
       "cpqFcaSpareDrv": cpqFcaSpareDrv,
       "cpqFcaSpareTable": cpqFcaSpareTable,
       "cpqFcaSpareEntry": cpqFcaSpareEntry,
       "cpqFcaSpareBoxIndex": cpqFcaSpareBoxIndex,
       "cpqFcaSparePhyDrvIndex": cpqFcaSparePhyDrvIndex,
       "cpqFcaSpareStatus": cpqFcaSpareStatus,
       "cpqFcaSpareReplacedDrvBay": cpqFcaSpareReplacedDrvBay,
       "cpqFcaSparePercentRebuild": cpqFcaSparePercentRebuild,
       "cpqFcaSpareCondition": cpqFcaSpareCondition,
       "cpqFcaSpareBusNumber": cpqFcaSpareBusNumber,
       "cpqFcaSpareBay": cpqFcaSpareBay,
       "cpqFcaSpareReplacedDrvBusNumber": cpqFcaSpareReplacedDrvBusNumber,
       "cpqFcaSpareLocationString": cpqFcaSpareLocationString,
       "cpqFcaPhyDrv": cpqFcaPhyDrv,
       "cpqFcaPhyDrvTable": cpqFcaPhyDrvTable,
       "cpqFcaPhyDrvEntry": cpqFcaPhyDrvEntry,
       "cpqFcaPhyDrvBoxIndex": cpqFcaPhyDrvBoxIndex,
       "cpqFcaPhyDrvIndex": cpqFcaPhyDrvIndex,
       "cpqFcaPhyDrvModel": cpqFcaPhyDrvModel,
       "cpqFcaPhyDrvFWRev": cpqFcaPhyDrvFWRev,
       "cpqFcaPhyDrvBay": cpqFcaPhyDrvBay,
       "cpqFcaPhyDrvStatus": cpqFcaPhyDrvStatus,
       "cpqFcaPhyDrvUsedReallocs": cpqFcaPhyDrvUsedReallocs,
       "cpqFcaPhyDrvRefHours": cpqFcaPhyDrvRefHours,
       "cpqFcaPhyDrvHReads": cpqFcaPhyDrvHReads,
       "cpqFcaPhyDrvReads": cpqFcaPhyDrvReads,
       "cpqFcaPhyDrvHWrites": cpqFcaPhyDrvHWrites,
       "cpqFcaPhyDrvWrites": cpqFcaPhyDrvWrites,
       "cpqFcaPhyDrvHSeeks": cpqFcaPhyDrvHSeeks,
       "cpqFcaPhyDrvSeeks": cpqFcaPhyDrvSeeks,
       "cpqFcaPhyDrvHardReadErrs": cpqFcaPhyDrvHardReadErrs,
       "cpqFcaPhyDrvRecvReadErrs": cpqFcaPhyDrvRecvReadErrs,
       "cpqFcaPhyDrvHardWriteErrs": cpqFcaPhyDrvHardWriteErrs,
       "cpqFcaPhyDrvRecvWriteErrs": cpqFcaPhyDrvRecvWriteErrs,
       "cpqFcaPhyDrvHSeekErrs": cpqFcaPhyDrvHSeekErrs,
       "cpqFcaPhyDrvSeekErrs": cpqFcaPhyDrvSeekErrs,
       "cpqFcaPhyDrvSpinupTime": cpqFcaPhyDrvSpinupTime,
       "cpqFcaPhyDrvFunctTest1": cpqFcaPhyDrvFunctTest1,
       "cpqFcaPhyDrvFunctTest2": cpqFcaPhyDrvFunctTest2,
       "cpqFcaPhyDrvFunctTest3": cpqFcaPhyDrvFunctTest3,
       "cpqFcaPhyDrvOtherTimeouts": cpqFcaPhyDrvOtherTimeouts,
       "cpqFcaPhyDrvBadRecvReads": cpqFcaPhyDrvBadRecvReads,
       "cpqFcaPhyDrvBadRecvWrites": cpqFcaPhyDrvBadRecvWrites,
       "cpqFcaPhyDrvFormatErrs": cpqFcaPhyDrvFormatErrs,
       "cpqFcaPhyDrvNotReadyErrs": cpqFcaPhyDrvNotReadyErrs,
       "cpqFcaPhyDrvHasMonInfo": cpqFcaPhyDrvHasMonInfo,
       "cpqFcaPhyDrvCondition": cpqFcaPhyDrvCondition,
       "cpqFcaPhyDrvHotPlugs": cpqFcaPhyDrvHotPlugs,
       "cpqFcaPhyDrvMediaErrs": cpqFcaPhyDrvMediaErrs,
       "cpqFcaPhyDrvHardwareErrs": cpqFcaPhyDrvHardwareErrs,
       "cpqFcaPhyDrvAbortedCmds": cpqFcaPhyDrvAbortedCmds,
       "cpqFcaPhyDrvSpinUpErrs": cpqFcaPhyDrvSpinUpErrs,
       "cpqFcaPhyDrvBadTargetErrs": cpqFcaPhyDrvBadTargetErrs,
       "cpqFcaPhyDrvSize": cpqFcaPhyDrvSize,
       "cpqFcaPhyDrvBusFaults": cpqFcaPhyDrvBusFaults,
       "cpqFcaPhyDrvHotPlug": cpqFcaPhyDrvHotPlug,
       "cpqFcaPhyDrvPlacement": cpqFcaPhyDrvPlacement,
       "cpqFcaPhyDrvBusNumber": cpqFcaPhyDrvBusNumber,
       "cpqFcaPhyDrvSerialNum": cpqFcaPhyDrvSerialNum,
       "cpqFcaPhyDrvPreFailMonitoring": cpqFcaPhyDrvPreFailMonitoring,
       "cpqFcaPhyDrvCurrentWidth": cpqFcaPhyDrvCurrentWidth,
       "cpqFcaPhyDrvCurrentSpeed": cpqFcaPhyDrvCurrentSpeed,
       "cpqFcaPhyDrvFailureCode": cpqFcaPhyDrvFailureCode,
       "cpqFcaPhyDrvBlinkTime": cpqFcaPhyDrvBlinkTime,
       "cpqFcaPhyDrvSmartStatus": cpqFcaPhyDrvSmartStatus,
       "cpqFcaPhyDrvRotationalSpeed": cpqFcaPhyDrvRotationalSpeed,
       "cpqFcaPhyDrvType": cpqFcaPhyDrvType,
       "cpqFcaPhyDrvSataVersion": cpqFcaPhyDrvSataVersion,
       "cpqFcaPhyDrvBoxConnector": cpqFcaPhyDrvBoxConnector,
       "cpqFcaPhyDrvBoxOnConnector": cpqFcaPhyDrvBoxOnConnector,
       "cpqFcaPhyDrvLocationString": cpqFcaPhyDrvLocationString,
       "cpqFcaPhyDrvNegotiatedLinkRate": cpqFcaPhyDrvNegotiatedLinkRate,
       "cpqFcaPhyDrvPhyCount": cpqFcaPhyDrvPhyCount,
       "cpqFcaPhyDrvUnsupportedDrive": cpqFcaPhyDrvUnsupportedDrive,
       "cpqFcaPhyDrvThr": cpqFcaPhyDrvThr,
       "cpqFcaPhyDrvThrTable": cpqFcaPhyDrvThrTable,
       "cpqFcaPhyDrvThrEntry": cpqFcaPhyDrvThrEntry,
       "cpqFcaPhyDrvThrBoxIndex": cpqFcaPhyDrvThrBoxIndex,
       "cpqFcaPhyDrvThrIndex": cpqFcaPhyDrvThrIndex,
       "cpqFcaPhyDrvThrUsedReallocs": cpqFcaPhyDrvThrUsedReallocs,
       "cpqFcaPhyDrvThrSpinupTime": cpqFcaPhyDrvThrSpinupTime,
       "cpqFcaPhyDrvThrFunctTest1": cpqFcaPhyDrvThrFunctTest1,
       "cpqFcaPhyDrvThrFunctTest2": cpqFcaPhyDrvThrFunctTest2,
       "cpqFcaPhyDrvThrFunctTest3": cpqFcaPhyDrvThrFunctTest3,
       "cpqFcaPhyDrvThrViUsedReallocs": cpqFcaPhyDrvThrViUsedReallocs,
       "cpqFcaPhyDrvThrViSpinupTime": cpqFcaPhyDrvThrViSpinupTime,
       "cpqFcaPhyDrvThrViFunctTest1": cpqFcaPhyDrvThrViFunctTest1,
       "cpqFcaPhyDrvThrViFunctTest2": cpqFcaPhyDrvThrViFunctTest2,
       "cpqFcaPhyDrvThrViFunctTest3": cpqFcaPhyDrvThrViFunctTest3,
       "cpqFcaHostCntlr": cpqFcaHostCntlr,
       "cpqFcaHostCntlrTable": cpqFcaHostCntlrTable,
       "cpqFcaHostCntlrEntry": cpqFcaHostCntlrEntry,
       "cpqFcaHostCntlrIndex": cpqFcaHostCntlrIndex,
       "cpqFcaHostCntlrSlot": cpqFcaHostCntlrSlot,
       "cpqFcaHostCntlrModel": cpqFcaHostCntlrModel,
       "cpqFcaHostCntlrStatus": cpqFcaHostCntlrStatus,
       "cpqFcaHostCntlrCondition": cpqFcaHostCntlrCondition,
       "cpqFcaHostCntlrWorldWideName": cpqFcaHostCntlrWorldWideName,
       "cpqFcaHostCntlrStorBoxList": cpqFcaHostCntlrStorBoxList,
       "cpqFcaHostCntlrOverallCondition": cpqFcaHostCntlrOverallCondition,
       "cpqFcaHostCntlrTapeCntlrList": cpqFcaHostCntlrTapeCntlrList,
       "cpqFcaHostCntlrSerialNumber": cpqFcaHostCntlrSerialNumber,
       "cpqFcaHostCntlrHwLocation": cpqFcaHostCntlrHwLocation,
       "cpqFcaHostCntlrWorldWidePortName": cpqFcaHostCntlrWorldWidePortName,
       "cpqFcaHostCntlrFirmwareVersion": cpqFcaHostCntlrFirmwareVersion,
       "cpqFcaHostCntlrOptionRomVersion": cpqFcaHostCntlrOptionRomVersion,
       "cpqExtArrRsrcVol": cpqExtArrRsrcVol,
       "cpqExtArrRsrcVolTable": cpqExtArrRsrcVolTable,
       "cpqExtArrRsrcVolEntry": cpqExtArrRsrcVolEntry,
       "cpqExtArrRsrcVolBoxIndex": cpqExtArrRsrcVolBoxIndex,
       "cpqExtArrRsrcVolIndex": cpqExtArrRsrcVolIndex,
       "cpqExtArrRsrcVolActiveInstances": cpqExtArrRsrcVolActiveInstances,
       "cpqExtArrRsrcVolDisabledInstances": cpqExtArrRsrcVolDisabledInstances,
       "cpqExtArrRsrcVolAllowCreation": cpqExtArrRsrcVolAllowCreation,
       "cpqExtArrRsrcVolVolumeId": cpqExtArrRsrcVolVolumeId,
       "cpqExtArrRsrcVolSourceVolumeId": cpqExtArrRsrcVolSourceVolumeId,
       "cpqExtArrRsrcVolTotalSpace": cpqExtArrRsrcVolTotalSpace,
       "cpqExtArrRsrcVolFreeActiveSpace": cpqExtArrRsrcVolFreeActiveSpace,
       "cpqExtArrRsrcVolFreeNewSpace": cpqExtArrRsrcVolFreeNewSpace,
       "cpqExtArrRsrcVolStatus": cpqExtArrRsrcVolStatus,
       "cpqExtArrSnapshot": cpqExtArrSnapshot,
       "cpqExtArrSnapshotTable": cpqExtArrSnapshotTable,
       "cpqExtArrSnapshotEntry": cpqExtArrSnapshotEntry,
       "cpqExtArrSnapshotBoxIndex": cpqExtArrSnapshotBoxIndex,
       "cpqExtArrSnapshotRsrcVolIndex": cpqExtArrSnapshotRsrcVolIndex,
       "cpqExtArrSnapshotIndex": cpqExtArrSnapshotIndex,
       "cpqExtArrSnapshotInstance": cpqExtArrSnapshotInstance,
       "cpqExtArrSnapshotUsedSpace": cpqExtArrSnapshotUsedSpace,
       "cpqExtArrSnapshotDateTime": cpqExtArrSnapshotDateTime,
       "cpqExtArrSnapshotType": cpqExtArrSnapshotType,
       "cpqExtArrSnapshotMounted": cpqExtArrSnapshotMounted,
       "cpqExtArrSnapshotAccess": cpqExtArrSnapshotAccess,
       "cpqFcTapeComponent": cpqFcTapeComponent,
       "cpqFcTapeCntlr": cpqFcTapeCntlr,
       "cpqFcTapeCntlrTable": cpqFcTapeCntlrTable,
       "cpqFcTapeCntlrEntry": cpqFcTapeCntlrEntry,
       "cpqFcTapeCntlrIndex": cpqFcTapeCntlrIndex,
       "cpqFcTapeCntlrStatus": cpqFcTapeCntlrStatus,
       "cpqFcTapeCntlrCondition": cpqFcTapeCntlrCondition,
       "cpqFcTapeCntlrOverallCondition": cpqFcTapeCntlrOverallCondition,
       "cpqFcTapeCntlrWWN": cpqFcTapeCntlrWWN,
       "cpqFcTapeCntlrFWRev": cpqFcTapeCntlrFWRev,
       "cpqFcTapeCntlrType": cpqFcTapeCntlrType,
       "cpqFcTapeCntlrModel": cpqFcTapeCntlrModel,
       "cpqFcTapeCntlrSerialNumber": cpqFcTapeCntlrSerialNumber,
       "cpqFcTapeLibrary": cpqFcTapeLibrary,
       "cpqFcTapeLibraryTable": cpqFcTapeLibraryTable,
       "cpqFcTapeLibraryEntry": cpqFcTapeLibraryEntry,
       "cpqFcTapeLibraryCntlrIndex": cpqFcTapeLibraryCntlrIndex,
       "cpqFcTapeLibraryScsiBus": cpqFcTapeLibraryScsiBus,
       "cpqFcTapeLibraryScsiTarget": cpqFcTapeLibraryScsiTarget,
       "cpqFcTapeLibraryScsiLun": cpqFcTapeLibraryScsiLun,
       "cpqFcTapeLibrarySerialNumber": cpqFcTapeLibrarySerialNumber,
       "cpqFcTapeLibraryModel": cpqFcTapeLibraryModel,
       "cpqFcTapeLibraryFWRev": cpqFcTapeLibraryFWRev,
       "cpqFcTapeLibraryStatus": cpqFcTapeLibraryStatus,
       "cpqFcTapeLibraryDoorStatus": cpqFcTapeLibraryDoorStatus,
       "cpqFcTapeLibraryCondition": cpqFcTapeLibraryCondition,
       "cpqFcTapeLibraryOverallCondition": cpqFcTapeLibraryOverallCondition,
       "cpqFcTapeLibraryLastError": cpqFcTapeLibraryLastError,
       "cpqFcTapeLibraryStatHours": cpqFcTapeLibraryStatHours,
       "cpqFcTapeLibraryStatMoves": cpqFcTapeLibraryStatMoves,
       "cpqFcTapeLibraryDriveList": cpqFcTapeLibraryDriveList,
       "cpqFcTapeLibraryLocation": cpqFcTapeLibraryLocation,
       "cpqFcTapeLibraryTemperature": cpqFcTapeLibraryTemperature,
       "cpqFcTapeLibraryRedundancy": cpqFcTapeLibraryRedundancy,
       "cpqFcTapeLibraryHotSwap": cpqFcTapeLibraryHotSwap,
       "cpqFcTapeDrive": cpqFcTapeDrive,
       "cpqFcTapeDriveTable": cpqFcTapeDriveTable,
       "cpqFcTapeDriveEntry": cpqFcTapeDriveEntry,
       "cpqFcTapeDriveCntlrIndex": cpqFcTapeDriveCntlrIndex,
       "cpqFcTapeDriveScsiBus": cpqFcTapeDriveScsiBus,
       "cpqFcTapeDriveScsiTarget": cpqFcTapeDriveScsiTarget,
       "cpqFcTapeDriveScsiLun": cpqFcTapeDriveScsiLun,
       "cpqFcTapeDriveSerialNumber": cpqFcTapeDriveSerialNumber,
       "cpqFcTapeDriveModel": cpqFcTapeDriveModel,
       "cpqFcTapeDriveFWRev": cpqFcTapeDriveFWRev,
       "cpqFcTapeDriveType": cpqFcTapeDriveType,
       "cpqFcTapeDriveFWSubtype": cpqFcTapeDriveFWSubtype,
       "cpqFcTapeDriveStatus": cpqFcTapeDriveStatus,
       "cpqFcTapeDriveCleanReq": cpqFcTapeDriveCleanReq,
       "cpqFcTapeDriveCleanTapeRepl": cpqFcTapeDriveCleanTapeRepl,
       "cpqFcTapeDriveCondition": cpqFcTapeDriveCondition,
       "cpqFcTapeDriveCleanTapeCount": cpqFcTapeDriveCleanTapeCount,
       "cpqFcTapeDriveLibraryDrive": cpqFcTapeDriveLibraryDrive,
       "cpqFcTapeDriveLocation": cpqFcTapeDriveLocation,
       "cpqFcTapeDriveHotPlug": cpqFcTapeDriveHotPlug,
       "cpqFcTapeDriveBay": cpqFcTapeDriveBay,
       "cpqFcTapeDriveCurrentWidth": cpqFcTapeDriveCurrentWidth,
       "cpqFcTapeDriveCurrentSpeed": cpqFcTapeDriveCurrentSpeed,
       "cpqFcTapeCounters": cpqFcTapeCounters,
       "cpqFcTapeCountersTable": cpqFcTapeCountersTable,
       "cpqFcTapeCountersEntry": cpqFcTapeCountersEntry,
       "cpqFcTapeCountersCntlrIndex": cpqFcTapeCountersCntlrIndex,
       "cpqFcTapeCountersScsiBus": cpqFcTapeCountersScsiBus,
       "cpqFcTapeCountersScsiTarget": cpqFcTapeCountersScsiTarget,
       "cpqFcTapeCountersScsiLun": cpqFcTapeCountersScsiLun,
       "cpqFcTapeCountersReWrites": cpqFcTapeCountersReWrites,
       "cpqFcTapeCountersReReads": cpqFcTapeCountersReReads,
       "cpqFcTapeCountersTotalErrors": cpqFcTapeCountersTotalErrors,
       "cpqFcTapeCountersTotalUncorrectable": cpqFcTapeCountersTotalUncorrectable,
       "cpqFcTapeCountersTotalBytes": cpqFcTapeCountersTotalBytes,
       "cpqFcSwitchComponent": cpqFcSwitchComponent,
       "cpqFcSwitch": cpqFcSwitch,
       "cpqFcSwitchTable": cpqFcSwitchTable,
       "cpqFcSwitchEntry": cpqFcSwitchEntry,
       "cpqFcSwitchIndex": cpqFcSwitchIndex,
       "cpqFcSwitchLocation": cpqFcSwitchLocation,
       "cpqFcSwitchChassisIndex": cpqFcSwitchChassisIndex,
       "cpqFcSwitchChassisSlot": cpqFcSwitchChassisSlot,
       "cpqFcSwitchWorldWideNodeName": cpqFcSwitchWorldWideNodeName,
       "cpqFcSwitchWorldWidePortName": cpqFcSwitchWorldWidePortName,
       "cpqFcSwitchIpAddress": cpqFcSwitchIpAddress,
       "cpqFcSwitchIpGateway": cpqFcSwitchIpGateway,
       "cpqFcSwitchIpSubnet": cpqFcSwitchIpSubnet,
       "cpqFcSwitchName": cpqFcSwitchName,
       "cpqFcSwitchNetworkLinkStatus": cpqFcSwitchNetworkLinkStatus,
       "cpqFcSwitchFibreConnectStatus": cpqFcSwitchFibreConnectStatus,
       "cpqFcSwitchFWRev": cpqFcSwitchFWRev}
)
