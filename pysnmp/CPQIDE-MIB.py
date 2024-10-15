# SNMP MIB module (CPQIDE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQIDE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:28 2024
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

_CpqIde_ObjectIdentity = ObjectIdentity
cpqIde = _CpqIde_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 14)
)
_CpqIdeMibRev_ObjectIdentity = ObjectIdentity
cpqIdeMibRev = _CpqIdeMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 14, 1)
)


class _CpqIdeMibRevMajor_Type(Integer32):
    """Custom type cpqIdeMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqIdeMibRevMajor_Type.__name__ = "Integer32"
_CpqIdeMibRevMajor_Object = MibScalar
cpqIdeMibRevMajor = _CpqIdeMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 1, 1),
    _CpqIdeMibRevMajor_Type()
)
cpqIdeMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeMibRevMajor.setStatus("mandatory")


class _CpqIdeMibRevMinor_Type(Integer32):
    """Custom type cpqIdeMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqIdeMibRevMinor_Type.__name__ = "Integer32"
_CpqIdeMibRevMinor_Object = MibScalar
cpqIdeMibRevMinor = _CpqIdeMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 1, 2),
    _CpqIdeMibRevMinor_Type()
)
cpqIdeMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeMibRevMinor.setStatus("mandatory")


class _CpqIdeMibCondition_Type(Integer32):
    """Custom type cpqIdeMibCondition based on Integer32"""
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


_CpqIdeMibCondition_Type.__name__ = "Integer32"
_CpqIdeMibCondition_Object = MibScalar
cpqIdeMibCondition = _CpqIdeMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 1, 3),
    _CpqIdeMibCondition_Type()
)
cpqIdeMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeMibCondition.setStatus("mandatory")
_CpqIdeComponent_ObjectIdentity = ObjectIdentity
cpqIdeComponent = _CpqIdeComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 14, 2)
)
_CpqIdeInterface_ObjectIdentity = ObjectIdentity
cpqIdeInterface = _CpqIdeInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 1)
)
_CpqIdeOsCommon_ObjectIdentity = ObjectIdentity
cpqIdeOsCommon = _CpqIdeOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 1, 4)
)


class _CpqIdeOsCommonPollFreq_Type(Integer32):
    """Custom type cpqIdeOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqIdeOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqIdeOsCommonPollFreq_Object = MibScalar
cpqIdeOsCommonPollFreq = _CpqIdeOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 1, 4, 1),
    _CpqIdeOsCommonPollFreq_Type()
)
cpqIdeOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIdeOsCommonPollFreq.setStatus("mandatory")
_CpqIdeOsCommonModuleTable_Object = MibTable
cpqIdeOsCommonModuleTable = _CpqIdeOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqIdeOsCommonModuleTable.setStatus("deprecated")
_CpqIdeOsCommonModuleEntry_Object = MibTableRow
cpqIdeOsCommonModuleEntry = _CpqIdeOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 1, 4, 2, 1)
)
cpqIdeOsCommonModuleEntry.setIndexNames(
    (0, "CPQIDE-MIB", "cpqIdeOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqIdeOsCommonModuleEntry.setStatus("deprecated")


class _CpqIdeOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqIdeOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqIdeOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqIdeOsCommonModuleIndex_Object = MibTableColumn
cpqIdeOsCommonModuleIndex = _CpqIdeOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 1, 4, 2, 1, 1),
    _CpqIdeOsCommonModuleIndex_Type()
)
cpqIdeOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeOsCommonModuleIndex.setStatus("deprecated")


class _CpqIdeOsCommonModuleName_Type(DisplayString):
    """Custom type cpqIdeOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqIdeOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqIdeOsCommonModuleName_Object = MibTableColumn
cpqIdeOsCommonModuleName = _CpqIdeOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 1, 4, 2, 1, 2),
    _CpqIdeOsCommonModuleName_Type()
)
cpqIdeOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeOsCommonModuleName.setStatus("deprecated")


class _CpqIdeOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqIdeOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqIdeOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqIdeOsCommonModuleVersion_Object = MibTableColumn
cpqIdeOsCommonModuleVersion = _CpqIdeOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 1, 4, 2, 1, 3),
    _CpqIdeOsCommonModuleVersion_Type()
)
cpqIdeOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeOsCommonModuleVersion.setStatus("deprecated")


class _CpqIdeOsCommonModuleDate_Type(OctetString):
    """Custom type cpqIdeOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqIdeOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqIdeOsCommonModuleDate_Object = MibTableColumn
cpqIdeOsCommonModuleDate = _CpqIdeOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 1, 4, 2, 1, 4),
    _CpqIdeOsCommonModuleDate_Type()
)
cpqIdeOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeOsCommonModuleDate.setStatus("deprecated")


class _CpqIdeOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqIdeOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqIdeOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqIdeOsCommonModulePurpose_Object = MibTableColumn
cpqIdeOsCommonModulePurpose = _CpqIdeOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 1, 4, 2, 1, 5),
    _CpqIdeOsCommonModulePurpose_Type()
)
cpqIdeOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeOsCommonModulePurpose.setStatus("deprecated")
_CpqIdeIdent_ObjectIdentity = ObjectIdentity
cpqIdeIdent = _CpqIdeIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2)
)
_CpqIdeIdentTable_Object = MibTable
cpqIdeIdentTable = _CpqIdeIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqIdeIdentTable.setStatus("mandatory")
_CpqIdeIdentEntry_Object = MibTableRow
cpqIdeIdentEntry = _CpqIdeIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1)
)
cpqIdeIdentEntry.setIndexNames(
    (0, "CPQIDE-MIB", "cpqIdeIdentIndex"),
)
if mibBuilder.loadTexts:
    cpqIdeIdentEntry.setStatus("mandatory")


class _CpqIdeIdentIndex_Type(Integer32):
    """Custom type cpqIdeIdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqIdeIdentIndex_Type.__name__ = "Integer32"
_CpqIdeIdentIndex_Object = MibTableColumn
cpqIdeIdentIndex = _CpqIdeIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 1),
    _CpqIdeIdentIndex_Type()
)
cpqIdeIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentIndex.setStatus("mandatory")


class _CpqIdeIdentModel_Type(DisplayString):
    """Custom type cpqIdeIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_CpqIdeIdentModel_Type.__name__ = "DisplayString"
_CpqIdeIdentModel_Object = MibTableColumn
cpqIdeIdentModel = _CpqIdeIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 2),
    _CpqIdeIdentModel_Type()
)
cpqIdeIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentModel.setStatus("mandatory")


class _CpqIdeIdentSerNum_Type(DisplayString):
    """Custom type cpqIdeIdentSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_CpqIdeIdentSerNum_Type.__name__ = "DisplayString"
_CpqIdeIdentSerNum_Object = MibTableColumn
cpqIdeIdentSerNum = _CpqIdeIdentSerNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 3),
    _CpqIdeIdentSerNum_Type()
)
cpqIdeIdentSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentSerNum.setStatus("mandatory")


class _CpqIdeIdentFWVers_Type(DisplayString):
    """Custom type cpqIdeIdentFWVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_CpqIdeIdentFWVers_Type.__name__ = "DisplayString"
_CpqIdeIdentFWVers_Object = MibTableColumn
cpqIdeIdentFWVers = _CpqIdeIdentFWVers_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 4),
    _CpqIdeIdentFWVers_Type()
)
cpqIdeIdentFWVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentFWVers.setStatus("mandatory")


class _CpqIdeIdentCondition_Type(Integer32):
    """Custom type cpqIdeIdentCondition based on Integer32"""
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


_CpqIdeIdentCondition_Type.__name__ = "Integer32"
_CpqIdeIdentCondition_Object = MibTableColumn
cpqIdeIdentCondition = _CpqIdeIdentCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 5),
    _CpqIdeIdentCondition_Type()
)
cpqIdeIdentCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentCondition.setStatus("deprecated")


class _CpqIdeIdentErrorNumber_Type(DisplayString):
    """Custom type cpqIdeIdentErrorNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqIdeIdentErrorNumber_Type.__name__ = "DisplayString"
_CpqIdeIdentErrorNumber_Object = MibTableColumn
cpqIdeIdentErrorNumber = _CpqIdeIdentErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 6),
    _CpqIdeIdentErrorNumber_Type()
)
cpqIdeIdentErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentErrorNumber.setStatus("mandatory")


class _CpqIdeIdentType_Type(Integer32):
    """Custom type cpqIdeIdentType based on Integer32"""
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
        *(("cd-rom", 7),
          ("commDev", 11),
          ("disk", 2),
          ("jukeBox", 10),
          ("optical", 9),
          ("other", 1),
          ("printer", 4),
          ("processor", 5),
          ("scanner", 8),
          ("tape", 3),
          ("wormDrive", 6))
    )


_CpqIdeIdentType_Type.__name__ = "Integer32"
_CpqIdeIdentType_Object = MibTableColumn
cpqIdeIdentType = _CpqIdeIdentType_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 7),
    _CpqIdeIdentType_Type()
)
cpqIdeIdentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentType.setStatus("mandatory")


class _CpqIdeIdentTypeExtended_Type(Integer32):
    """Custom type cpqIdeIdentTypeExtended based on Integer32"""
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
          ("pdcd", 2),
          ("removableDisk", 3))
    )


_CpqIdeIdentTypeExtended_Type.__name__ = "Integer32"
_CpqIdeIdentTypeExtended_Object = MibTableColumn
cpqIdeIdentTypeExtended = _CpqIdeIdentTypeExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 8),
    _CpqIdeIdentTypeExtended_Type()
)
cpqIdeIdentTypeExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentTypeExtended.setStatus("mandatory")


class _CpqIdeIdentCondition2_Type(Integer32):
    """Custom type cpqIdeIdentCondition2 based on Integer32"""
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


_CpqIdeIdentCondition2_Type.__name__ = "Integer32"
_CpqIdeIdentCondition2_Object = MibTableColumn
cpqIdeIdentCondition2 = _CpqIdeIdentCondition2_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 9),
    _CpqIdeIdentCondition2_Type()
)
cpqIdeIdentCondition2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentCondition2.setStatus("mandatory")


class _CpqIdeIdentStatus_Type(Integer32):
    """Custom type cpqIdeIdentStatus based on Integer32"""
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
          ("other", 1),
          ("preFailureDegraded", 3),
          ("ultraAtaDegraded", 4))
    )


_CpqIdeIdentStatus_Type.__name__ = "Integer32"
_CpqIdeIdentStatus_Object = MibTableColumn
cpqIdeIdentStatus = _CpqIdeIdentStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 10),
    _CpqIdeIdentStatus_Type()
)
cpqIdeIdentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentStatus.setStatus("mandatory")


class _CpqIdeIdentUltraAtaAvailability_Type(Integer32):
    """Custom type cpqIdeIdentUltraAtaAvailability based on Integer32"""
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
        *(("noDisabledInSetup", 5),
          ("noNotSupportedByController", 4),
          ("noNotSupportedByDevice", 3),
          ("noNotSupportedByDeviceAndController", 2),
          ("other", 1),
          ("yesEnabledInSetup", 6))
    )


_CpqIdeIdentUltraAtaAvailability_Type.__name__ = "Integer32"
_CpqIdeIdentUltraAtaAvailability_Object = MibTableColumn
cpqIdeIdentUltraAtaAvailability = _CpqIdeIdentUltraAtaAvailability_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 2, 1, 1, 11),
    _CpqIdeIdentUltraAtaAvailability_Type()
)
cpqIdeIdentUltraAtaAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeIdentUltraAtaAvailability.setStatus("mandatory")
_CpqIdeController_ObjectIdentity = ObjectIdentity
cpqIdeController = _CpqIdeController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3)
)
_CpqIdeControllerTable_Object = MibTable
cpqIdeControllerTable = _CpqIdeControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqIdeControllerTable.setStatus("mandatory")
_CpqIdeControllerEntry_Object = MibTableRow
cpqIdeControllerEntry = _CpqIdeControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3, 1, 1)
)
cpqIdeControllerEntry.setIndexNames(
    (0, "CPQIDE-MIB", "cpqIdeControllerIndex"),
)
if mibBuilder.loadTexts:
    cpqIdeControllerEntry.setStatus("mandatory")
_CpqIdeControllerIndex_Type = Integer32
_CpqIdeControllerIndex_Object = MibTableColumn
cpqIdeControllerIndex = _CpqIdeControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3, 1, 1, 1),
    _CpqIdeControllerIndex_Type()
)
cpqIdeControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeControllerIndex.setStatus("mandatory")


class _CpqIdeControllerOverallCondition_Type(Integer32):
    """Custom type cpqIdeControllerOverallCondition based on Integer32"""
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


_CpqIdeControllerOverallCondition_Type.__name__ = "Integer32"
_CpqIdeControllerOverallCondition_Object = MibTableColumn
cpqIdeControllerOverallCondition = _CpqIdeControllerOverallCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3, 1, 1, 2),
    _CpqIdeControllerOverallCondition_Type()
)
cpqIdeControllerOverallCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeControllerOverallCondition.setStatus("mandatory")
_CpqIdeControllerModel_Type = DisplayString
_CpqIdeControllerModel_Object = MibTableColumn
cpqIdeControllerModel = _CpqIdeControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3, 1, 1, 3),
    _CpqIdeControllerModel_Type()
)
cpqIdeControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeControllerModel.setStatus("mandatory")
_CpqIdeControllerFwRev_Type = DisplayString
_CpqIdeControllerFwRev_Object = MibTableColumn
cpqIdeControllerFwRev = _CpqIdeControllerFwRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3, 1, 1, 4),
    _CpqIdeControllerFwRev_Type()
)
cpqIdeControllerFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeControllerFwRev.setStatus("mandatory")
_CpqIdeControllerSlot_Type = Integer32
_CpqIdeControllerSlot_Object = MibTableColumn
cpqIdeControllerSlot = _CpqIdeControllerSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3, 1, 1, 5),
    _CpqIdeControllerSlot_Type()
)
cpqIdeControllerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeControllerSlot.setStatus("mandatory")


class _CpqIdeControllerStatus_Type(Integer32):
    """Custom type cpqIdeControllerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqIdeControllerStatus_Type.__name__ = "Integer32"
_CpqIdeControllerStatus_Object = MibTableColumn
cpqIdeControllerStatus = _CpqIdeControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3, 1, 1, 6),
    _CpqIdeControllerStatus_Type()
)
cpqIdeControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeControllerStatus.setStatus("mandatory")


class _CpqIdeControllerCondition_Type(Integer32):
    """Custom type cpqIdeControllerCondition based on Integer32"""
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


_CpqIdeControllerCondition_Type.__name__ = "Integer32"
_CpqIdeControllerCondition_Object = MibTableColumn
cpqIdeControllerCondition = _CpqIdeControllerCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3, 1, 1, 7),
    _CpqIdeControllerCondition_Type()
)
cpqIdeControllerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeControllerCondition.setStatus("mandatory")
_CpqIdeControllerSerialNumber_Type = DisplayString
_CpqIdeControllerSerialNumber_Object = MibTableColumn
cpqIdeControllerSerialNumber = _CpqIdeControllerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 3, 1, 1, 8),
    _CpqIdeControllerSerialNumber_Type()
)
cpqIdeControllerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeControllerSerialNumber.setStatus("mandatory")
_CpqIdeAtaDisk_ObjectIdentity = ObjectIdentity
cpqIdeAtaDisk = _CpqIdeAtaDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4)
)
_CpqIdeAtaDiskTable_Object = MibTable
cpqIdeAtaDiskTable = _CpqIdeAtaDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqIdeAtaDiskTable.setStatus("mandatory")
_CpqIdeAtaDiskEntry_Object = MibTableRow
cpqIdeAtaDiskEntry = _CpqIdeAtaDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1)
)
cpqIdeAtaDiskEntry.setIndexNames(
    (0, "CPQIDE-MIB", "cpqIdeAtaDiskControllerIndex"),
    (0, "CPQIDE-MIB", "cpqIdeAtaDiskIndex"),
)
if mibBuilder.loadTexts:
    cpqIdeAtaDiskEntry.setStatus("mandatory")
_CpqIdeAtaDiskControllerIndex_Type = Integer32
_CpqIdeAtaDiskControllerIndex_Object = MibTableColumn
cpqIdeAtaDiskControllerIndex = _CpqIdeAtaDiskControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 1),
    _CpqIdeAtaDiskControllerIndex_Type()
)
cpqIdeAtaDiskControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskControllerIndex.setStatus("mandatory")
_CpqIdeAtaDiskIndex_Type = Integer32
_CpqIdeAtaDiskIndex_Object = MibTableColumn
cpqIdeAtaDiskIndex = _CpqIdeAtaDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 2),
    _CpqIdeAtaDiskIndex_Type()
)
cpqIdeAtaDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskIndex.setStatus("mandatory")
_CpqIdeAtaDiskModel_Type = DisplayString
_CpqIdeAtaDiskModel_Object = MibTableColumn
cpqIdeAtaDiskModel = _CpqIdeAtaDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 3),
    _CpqIdeAtaDiskModel_Type()
)
cpqIdeAtaDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskModel.setStatus("mandatory")
_CpqIdeAtaDiskFwRev_Type = DisplayString
_CpqIdeAtaDiskFwRev_Object = MibTableColumn
cpqIdeAtaDiskFwRev = _CpqIdeAtaDiskFwRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 4),
    _CpqIdeAtaDiskFwRev_Type()
)
cpqIdeAtaDiskFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskFwRev.setStatus("mandatory")
_CpqIdeAtaDiskSerialNumber_Type = DisplayString
_CpqIdeAtaDiskSerialNumber_Object = MibTableColumn
cpqIdeAtaDiskSerialNumber = _CpqIdeAtaDiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 5),
    _CpqIdeAtaDiskSerialNumber_Type()
)
cpqIdeAtaDiskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskSerialNumber.setStatus("mandatory")


class _CpqIdeAtaDiskStatus_Type(Integer32):
    """Custom type cpqIdeAtaDiskStatus based on Integer32"""
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
        *(("failed", 4),
          ("ok", 2),
          ("other", 1),
          ("smartError", 3))
    )


_CpqIdeAtaDiskStatus_Type.__name__ = "Integer32"
_CpqIdeAtaDiskStatus_Object = MibTableColumn
cpqIdeAtaDiskStatus = _CpqIdeAtaDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 6),
    _CpqIdeAtaDiskStatus_Type()
)
cpqIdeAtaDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskStatus.setStatus("mandatory")


class _CpqIdeAtaDiskCondition_Type(Integer32):
    """Custom type cpqIdeAtaDiskCondition based on Integer32"""
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


_CpqIdeAtaDiskCondition_Type.__name__ = "Integer32"
_CpqIdeAtaDiskCondition_Object = MibTableColumn
cpqIdeAtaDiskCondition = _CpqIdeAtaDiskCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 7),
    _CpqIdeAtaDiskCondition_Type()
)
cpqIdeAtaDiskCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskCondition.setStatus("mandatory")
_CpqIdeAtaDiskCapacity_Type = Integer32
_CpqIdeAtaDiskCapacity_Object = MibTableColumn
cpqIdeAtaDiskCapacity = _CpqIdeAtaDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 8),
    _CpqIdeAtaDiskCapacity_Type()
)
cpqIdeAtaDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskCapacity.setStatus("mandatory")


class _CpqIdeAtaDiskSmartEnabled_Type(Integer32):
    """Custom type cpqIdeAtaDiskSmartEnabled based on Integer32"""
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


_CpqIdeAtaDiskSmartEnabled_Type.__name__ = "Integer32"
_CpqIdeAtaDiskSmartEnabled_Object = MibTableColumn
cpqIdeAtaDiskSmartEnabled = _CpqIdeAtaDiskSmartEnabled_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 9),
    _CpqIdeAtaDiskSmartEnabled_Type()
)
cpqIdeAtaDiskSmartEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskSmartEnabled.setStatus("mandatory")


class _CpqIdeAtaDiskTransferMode_Type(Integer32):
    """Custom type cpqIdeAtaDiskTransferMode based on Integer32"""
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
        *(("dmaMode0", 7),
          ("dmaMode1", 8),
          ("dmaMode2", 9),
          ("other", 1),
          ("pioMode0", 2),
          ("pioMode1", 3),
          ("pioMode2", 4),
          ("pioMode3", 5),
          ("pioMode4", 6),
          ("ultraDmaMode0", 10),
          ("ultraDmaMode1", 11),
          ("ultraDmaMode2", 12),
          ("ultraDmaMode3", 13),
          ("ultraDmaMode4", 14),
          ("ultraDmaMode5", 15))
    )


_CpqIdeAtaDiskTransferMode_Type.__name__ = "Integer32"
_CpqIdeAtaDiskTransferMode_Object = MibTableColumn
cpqIdeAtaDiskTransferMode = _CpqIdeAtaDiskTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 10),
    _CpqIdeAtaDiskTransferMode_Type()
)
cpqIdeAtaDiskTransferMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskTransferMode.setStatus("mandatory")


class _CpqIdeAtaDiskChannel_Type(Integer32):
    """Custom type cpqIdeAtaDiskChannel based on Integer32"""
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
        *(("channel0", 2),
          ("channel1", 3),
          ("other", 1),
          ("serial", 4))
    )


_CpqIdeAtaDiskChannel_Type.__name__ = "Integer32"
_CpqIdeAtaDiskChannel_Object = MibTableColumn
cpqIdeAtaDiskChannel = _CpqIdeAtaDiskChannel_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 11),
    _CpqIdeAtaDiskChannel_Type()
)
cpqIdeAtaDiskChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskChannel.setStatus("mandatory")


class _CpqIdeAtaDiskNumber_Type(Integer32):
    """Custom type cpqIdeAtaDiskNumber based on Integer32"""
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
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("bay1", 21),
          ("bay2", 22),
          ("bay3", 23),
          ("bay4", 24),
          ("bay5", 25),
          ("bay6", 26),
          ("bay7", 27),
          ("bay8", 28),
          ("device0", 2),
          ("device1", 3),
          ("other", 1),
          ("sataDevice0", 4),
          ("sataDevice1", 5),
          ("sataDevice2", 6),
          ("sataDevice3", 7),
          ("sataDevice4", 8),
          ("sataDevice5", 9),
          ("sataDevice6", 10),
          ("sataDevice7", 11))
    )


_CpqIdeAtaDiskNumber_Type.__name__ = "Integer32"
_CpqIdeAtaDiskNumber_Object = MibTableColumn
cpqIdeAtaDiskNumber = _CpqIdeAtaDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 12),
    _CpqIdeAtaDiskNumber_Type()
)
cpqIdeAtaDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskNumber.setStatus("mandatory")


class _CpqIdeAtaDiskLogicalDriveMember_Type(Integer32):
    """Custom type cpqIdeAtaDiskLogicalDriveMember based on Integer32"""
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


_CpqIdeAtaDiskLogicalDriveMember_Type.__name__ = "Integer32"
_CpqIdeAtaDiskLogicalDriveMember_Object = MibTableColumn
cpqIdeAtaDiskLogicalDriveMember = _CpqIdeAtaDiskLogicalDriveMember_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 13),
    _CpqIdeAtaDiskLogicalDriveMember_Type()
)
cpqIdeAtaDiskLogicalDriveMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskLogicalDriveMember.setStatus("mandatory")


class _CpqIdeAtaDiskIsSpare_Type(Integer32):
    """Custom type cpqIdeAtaDiskIsSpare based on Integer32"""
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


_CpqIdeAtaDiskIsSpare_Type.__name__ = "Integer32"
_CpqIdeAtaDiskIsSpare_Object = MibTableColumn
cpqIdeAtaDiskIsSpare = _CpqIdeAtaDiskIsSpare_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 14),
    _CpqIdeAtaDiskIsSpare_Type()
)
cpqIdeAtaDiskIsSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskIsSpare.setStatus("mandatory")


class _CpqIdeAtaDiskOsName_Type(DisplayString):
    """Custom type cpqIdeAtaDiskOsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqIdeAtaDiskOsName_Type.__name__ = "DisplayString"
_CpqIdeAtaDiskOsName_Object = MibTableColumn
cpqIdeAtaDiskOsName = _CpqIdeAtaDiskOsName_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 15),
    _CpqIdeAtaDiskOsName_Type()
)
cpqIdeAtaDiskOsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskOsName.setStatus("mandatory")


class _CpqIdeAtaDiskType_Type(Integer32):
    """Custom type cpqIdeAtaDiskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ata", 2),
          ("other", 1),
          ("sata", 3))
    )


_CpqIdeAtaDiskType_Type.__name__ = "Integer32"
_CpqIdeAtaDiskType_Object = MibTableColumn
cpqIdeAtaDiskType = _CpqIdeAtaDiskType_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 16),
    _CpqIdeAtaDiskType_Type()
)
cpqIdeAtaDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskType.setStatus("mandatory")


class _CpqIdeAtaDiskSataVersion_Type(Integer32):
    """Custom type cpqIdeAtaDiskSataVersion based on Integer32"""
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


_CpqIdeAtaDiskSataVersion_Type.__name__ = "Integer32"
_CpqIdeAtaDiskSataVersion_Object = MibTableColumn
cpqIdeAtaDiskSataVersion = _CpqIdeAtaDiskSataVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 4, 1, 1, 17),
    _CpqIdeAtaDiskSataVersion_Type()
)
cpqIdeAtaDiskSataVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtaDiskSataVersion.setStatus("mandatory")
_CpqIdeAtapiDevice_ObjectIdentity = ObjectIdentity
cpqIdeAtapiDevice = _CpqIdeAtapiDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5)
)
_CpqIdeAtapiDeviceTable_Object = MibTable
cpqIdeAtapiDeviceTable = _CpqIdeAtapiDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqIdeAtapiDeviceTable.setStatus("mandatory")
_CpqIdeAtapiDeviceEntry_Object = MibTableRow
cpqIdeAtapiDeviceEntry = _CpqIdeAtapiDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5, 1, 1)
)
cpqIdeAtapiDeviceEntry.setIndexNames(
    (0, "CPQIDE-MIB", "cpqIdeAtapiDeviceControllerIndex"),
    (0, "CPQIDE-MIB", "cpqIdeAtapiDeviceIndex"),
)
if mibBuilder.loadTexts:
    cpqIdeAtapiDeviceEntry.setStatus("mandatory")
_CpqIdeAtapiDeviceControllerIndex_Type = Integer32
_CpqIdeAtapiDeviceControllerIndex_Object = MibTableColumn
cpqIdeAtapiDeviceControllerIndex = _CpqIdeAtapiDeviceControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5, 1, 1, 1),
    _CpqIdeAtapiDeviceControllerIndex_Type()
)
cpqIdeAtapiDeviceControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtapiDeviceControllerIndex.setStatus("mandatory")
_CpqIdeAtapiDeviceIndex_Type = Integer32
_CpqIdeAtapiDeviceIndex_Object = MibTableColumn
cpqIdeAtapiDeviceIndex = _CpqIdeAtapiDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5, 1, 1, 2),
    _CpqIdeAtapiDeviceIndex_Type()
)
cpqIdeAtapiDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtapiDeviceIndex.setStatus("mandatory")
_CpqIdeAtapiDeviceModel_Type = DisplayString
_CpqIdeAtapiDeviceModel_Object = MibTableColumn
cpqIdeAtapiDeviceModel = _CpqIdeAtapiDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5, 1, 1, 3),
    _CpqIdeAtapiDeviceModel_Type()
)
cpqIdeAtapiDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtapiDeviceModel.setStatus("mandatory")
_CpqIdeAtapiDeviceFwRev_Type = DisplayString
_CpqIdeAtapiDeviceFwRev_Object = MibTableColumn
cpqIdeAtapiDeviceFwRev = _CpqIdeAtapiDeviceFwRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5, 1, 1, 4),
    _CpqIdeAtapiDeviceFwRev_Type()
)
cpqIdeAtapiDeviceFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtapiDeviceFwRev.setStatus("mandatory")


class _CpqIdeAtapiDeviceType_Type(Integer32):
    """Custom type cpqIdeAtapiDeviceType based on Integer32"""
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
        *(("cd-rom", 7),
          ("commDev", 11),
          ("disk", 2),
          ("jukeBox", 10),
          ("optical", 9),
          ("other", 1),
          ("printer", 4),
          ("processor", 5),
          ("scanner", 8),
          ("tape", 3),
          ("wormDrive", 6))
    )


_CpqIdeAtapiDeviceType_Type.__name__ = "Integer32"
_CpqIdeAtapiDeviceType_Object = MibTableColumn
cpqIdeAtapiDeviceType = _CpqIdeAtapiDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5, 1, 1, 5),
    _CpqIdeAtapiDeviceType_Type()
)
cpqIdeAtapiDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtapiDeviceType.setStatus("mandatory")


class _CpqIdeAtapiDeviceTypeExtended_Type(Integer32):
    """Custom type cpqIdeAtapiDeviceTypeExtended based on Integer32"""
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
          ("pdcd", 2),
          ("removableDisk", 3))
    )


_CpqIdeAtapiDeviceTypeExtended_Type.__name__ = "Integer32"
_CpqIdeAtapiDeviceTypeExtended_Object = MibTableColumn
cpqIdeAtapiDeviceTypeExtended = _CpqIdeAtapiDeviceTypeExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5, 1, 1, 6),
    _CpqIdeAtapiDeviceTypeExtended_Type()
)
cpqIdeAtapiDeviceTypeExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtapiDeviceTypeExtended.setStatus("mandatory")


class _CpqIdeAtapiDeviceChannel_Type(Integer32):
    """Custom type cpqIdeAtapiDeviceChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channel0", 2),
          ("channel1", 3),
          ("other", 1))
    )


_CpqIdeAtapiDeviceChannel_Type.__name__ = "Integer32"
_CpqIdeAtapiDeviceChannel_Object = MibTableColumn
cpqIdeAtapiDeviceChannel = _CpqIdeAtapiDeviceChannel_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5, 1, 1, 7),
    _CpqIdeAtapiDeviceChannel_Type()
)
cpqIdeAtapiDeviceChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtapiDeviceChannel.setStatus("mandatory")


class _CpqIdeAtapiDeviceNumber_Type(Integer32):
    """Custom type cpqIdeAtapiDeviceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("device0", 2),
          ("device1", 3),
          ("other", 1))
    )


_CpqIdeAtapiDeviceNumber_Type.__name__ = "Integer32"
_CpqIdeAtapiDeviceNumber_Object = MibTableColumn
cpqIdeAtapiDeviceNumber = _CpqIdeAtapiDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 5, 1, 1, 8),
    _CpqIdeAtapiDeviceNumber_Type()
)
cpqIdeAtapiDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeAtapiDeviceNumber.setStatus("mandatory")
_CpqIdeLogicalDrive_ObjectIdentity = ObjectIdentity
cpqIdeLogicalDrive = _CpqIdeLogicalDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6)
)
_CpqIdeLogicalDriveTable_Object = MibTable
cpqIdeLogicalDriveTable = _CpqIdeLogicalDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveTable.setStatus("mandatory")
_CpqIdeLogicalDriveEntry_Object = MibTableRow
cpqIdeLogicalDriveEntry = _CpqIdeLogicalDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1)
)
cpqIdeLogicalDriveEntry.setIndexNames(
    (0, "CPQIDE-MIB", "cpqIdeLogicalDriveControllerIndex"),
    (0, "CPQIDE-MIB", "cpqIdeLogicalDriveIndex"),
)
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveEntry.setStatus("mandatory")
_CpqIdeLogicalDriveControllerIndex_Type = Integer32
_CpqIdeLogicalDriveControllerIndex_Object = MibTableColumn
cpqIdeLogicalDriveControllerIndex = _CpqIdeLogicalDriveControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 1),
    _CpqIdeLogicalDriveControllerIndex_Type()
)
cpqIdeLogicalDriveControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveControllerIndex.setStatus("mandatory")
_CpqIdeLogicalDriveIndex_Type = Integer32
_CpqIdeLogicalDriveIndex_Object = MibTableColumn
cpqIdeLogicalDriveIndex = _CpqIdeLogicalDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 2),
    _CpqIdeLogicalDriveIndex_Type()
)
cpqIdeLogicalDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveIndex.setStatus("mandatory")


class _CpqIdeLogicalDriveRaidLevel_Type(Integer32):
    """Custom type cpqIdeLogicalDriveRaidLevel based on Integer32"""
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
          ("raid0", 2),
          ("raid0plus1", 4),
          ("raid1", 3),
          ("raid15", 6),
          ("raid5", 5),
          ("volume", 7))
    )


_CpqIdeLogicalDriveRaidLevel_Type.__name__ = "Integer32"
_CpqIdeLogicalDriveRaidLevel_Object = MibTableColumn
cpqIdeLogicalDriveRaidLevel = _CpqIdeLogicalDriveRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 3),
    _CpqIdeLogicalDriveRaidLevel_Type()
)
cpqIdeLogicalDriveRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveRaidLevel.setStatus("mandatory")
_CpqIdeLogicalDriveCapacity_Type = Integer32
_CpqIdeLogicalDriveCapacity_Object = MibTableColumn
cpqIdeLogicalDriveCapacity = _CpqIdeLogicalDriveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 4),
    _CpqIdeLogicalDriveCapacity_Type()
)
cpqIdeLogicalDriveCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveCapacity.setStatus("mandatory")


class _CpqIdeLogicalDriveStatus_Type(Integer32):
    """Custom type cpqIdeLogicalDriveStatus based on Integer32"""
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
          ("failed", 5),
          ("ok", 2),
          ("other", 1),
          ("rebuilding", 4))
    )


_CpqIdeLogicalDriveStatus_Type.__name__ = "Integer32"
_CpqIdeLogicalDriveStatus_Object = MibTableColumn
cpqIdeLogicalDriveStatus = _CpqIdeLogicalDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 5),
    _CpqIdeLogicalDriveStatus_Type()
)
cpqIdeLogicalDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveStatus.setStatus("mandatory")


class _CpqIdeLogicalDriveCondition_Type(Integer32):
    """Custom type cpqIdeLogicalDriveCondition based on Integer32"""
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


_CpqIdeLogicalDriveCondition_Type.__name__ = "Integer32"
_CpqIdeLogicalDriveCondition_Object = MibTableColumn
cpqIdeLogicalDriveCondition = _CpqIdeLogicalDriveCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 6),
    _CpqIdeLogicalDriveCondition_Type()
)
cpqIdeLogicalDriveCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveCondition.setStatus("mandatory")


class _CpqIdeLogicalDriveDiskIds_Type(OctetString):
    """Custom type cpqIdeLogicalDriveDiskIds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqIdeLogicalDriveDiskIds_Type.__name__ = "OctetString"
_CpqIdeLogicalDriveDiskIds_Object = MibTableColumn
cpqIdeLogicalDriveDiskIds = _CpqIdeLogicalDriveDiskIds_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 7),
    _CpqIdeLogicalDriveDiskIds_Type()
)
cpqIdeLogicalDriveDiskIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveDiskIds.setStatus("mandatory")
_CpqIdeLogicalDriveStripeSize_Type = Integer32
_CpqIdeLogicalDriveStripeSize_Object = MibTableColumn
cpqIdeLogicalDriveStripeSize = _CpqIdeLogicalDriveStripeSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 8),
    _CpqIdeLogicalDriveStripeSize_Type()
)
cpqIdeLogicalDriveStripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveStripeSize.setStatus("mandatory")


class _CpqIdeLogicalDriveSpareIds_Type(OctetString):
    """Custom type cpqIdeLogicalDriveSpareIds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqIdeLogicalDriveSpareIds_Type.__name__ = "OctetString"
_CpqIdeLogicalDriveSpareIds_Object = MibTableColumn
cpqIdeLogicalDriveSpareIds = _CpqIdeLogicalDriveSpareIds_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 9),
    _CpqIdeLogicalDriveSpareIds_Type()
)
cpqIdeLogicalDriveSpareIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveSpareIds.setStatus("mandatory")
_CpqIdeLogicalDriveRebuildingDisk_Type = Integer32
_CpqIdeLogicalDriveRebuildingDisk_Object = MibTableColumn
cpqIdeLogicalDriveRebuildingDisk = _CpqIdeLogicalDriveRebuildingDisk_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 10),
    _CpqIdeLogicalDriveRebuildingDisk_Type()
)
cpqIdeLogicalDriveRebuildingDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveRebuildingDisk.setStatus("mandatory")


class _CpqIdeLogicalDriveOsName_Type(DisplayString):
    """Custom type cpqIdeLogicalDriveOsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqIdeLogicalDriveOsName_Type.__name__ = "DisplayString"
_CpqIdeLogicalDriveOsName_Object = MibTableColumn
cpqIdeLogicalDriveOsName = _CpqIdeLogicalDriveOsName_Object(
    (1, 3, 6, 1, 4, 1, 232, 14, 2, 6, 1, 1, 11),
    _CpqIdeLogicalDriveOsName_Type()
)
cpqIdeLogicalDriveOsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveOsName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqIdeDriveDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 14001)
)
cpqIdeDriveDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDE-MIB", "cpqIdeIdentIndex"))
)
if mibBuilder.loadTexts:
    cpqIdeDriveDegraded.setStatus(
        ""
    )

cpqIdeDriveOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 14002)
)
cpqIdeDriveOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDE-MIB", "cpqIdeIdentIndex"))
)
if mibBuilder.loadTexts:
    cpqIdeDriveOk.setStatus(
        ""
    )

cpqIdeDriveUltraAtaDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 14003)
)
cpqIdeDriveUltraAtaDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDE-MIB", "cpqIdeIdentIndex"))
)
if mibBuilder.loadTexts:
    cpqIdeDriveUltraAtaDegraded.setStatus(
        ""
    )

cpqIdeAtaDiskStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 14004)
)
cpqIdeAtaDiskStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDE-MIB", "cpqIdeAtaDiskControllerIndex"),
        ("CPQIDE-MIB", "cpqIdeAtaDiskIndex"),
        ("CPQIDE-MIB", "cpqIdeAtaDiskModel"),
        ("CPQIDE-MIB", "cpqIdeAtaDiskFwRev"),
        ("CPQIDE-MIB", "cpqIdeAtaDiskSerialNumber"),
        ("CPQIDE-MIB", "cpqIdeAtaDiskStatus"),
        ("CPQIDE-MIB", "cpqIdeAtaDiskChannel"),
        ("CPQIDE-MIB", "cpqIdeAtaDiskNumber"))
)
if mibBuilder.loadTexts:
    cpqIdeAtaDiskStatusChange.setStatus(
        ""
    )

cpqIdeLogicalDriveStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 14005)
)
cpqIdeLogicalDriveStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDE-MIB", "cpqIdeControllerModel"),
        ("CPQIDE-MIB", "cpqIdeControllerSlot"),
        ("CPQIDE-MIB", "cpqIdeLogicalDriveControllerIndex"),
        ("CPQIDE-MIB", "cpqIdeLogicalDriveIndex"),
        ("CPQIDE-MIB", "cpqIdeLogicalDriveStatus"))
)
if mibBuilder.loadTexts:
    cpqIdeLogicalDriveStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQIDE-MIB",
    **{"cpqIdeDriveDegraded": cpqIdeDriveDegraded,
       "cpqIdeDriveOk": cpqIdeDriveOk,
       "cpqIdeDriveUltraAtaDegraded": cpqIdeDriveUltraAtaDegraded,
       "cpqIdeAtaDiskStatusChange": cpqIdeAtaDiskStatusChange,
       "cpqIdeLogicalDriveStatusChange": cpqIdeLogicalDriveStatusChange,
       "cpqIde": cpqIde,
       "cpqIdeMibRev": cpqIdeMibRev,
       "cpqIdeMibRevMajor": cpqIdeMibRevMajor,
       "cpqIdeMibRevMinor": cpqIdeMibRevMinor,
       "cpqIdeMibCondition": cpqIdeMibCondition,
       "cpqIdeComponent": cpqIdeComponent,
       "cpqIdeInterface": cpqIdeInterface,
       "cpqIdeOsCommon": cpqIdeOsCommon,
       "cpqIdeOsCommonPollFreq": cpqIdeOsCommonPollFreq,
       "cpqIdeOsCommonModuleTable": cpqIdeOsCommonModuleTable,
       "cpqIdeOsCommonModuleEntry": cpqIdeOsCommonModuleEntry,
       "cpqIdeOsCommonModuleIndex": cpqIdeOsCommonModuleIndex,
       "cpqIdeOsCommonModuleName": cpqIdeOsCommonModuleName,
       "cpqIdeOsCommonModuleVersion": cpqIdeOsCommonModuleVersion,
       "cpqIdeOsCommonModuleDate": cpqIdeOsCommonModuleDate,
       "cpqIdeOsCommonModulePurpose": cpqIdeOsCommonModulePurpose,
       "cpqIdeIdent": cpqIdeIdent,
       "cpqIdeIdentTable": cpqIdeIdentTable,
       "cpqIdeIdentEntry": cpqIdeIdentEntry,
       "cpqIdeIdentIndex": cpqIdeIdentIndex,
       "cpqIdeIdentModel": cpqIdeIdentModel,
       "cpqIdeIdentSerNum": cpqIdeIdentSerNum,
       "cpqIdeIdentFWVers": cpqIdeIdentFWVers,
       "cpqIdeIdentCondition": cpqIdeIdentCondition,
       "cpqIdeIdentErrorNumber": cpqIdeIdentErrorNumber,
       "cpqIdeIdentType": cpqIdeIdentType,
       "cpqIdeIdentTypeExtended": cpqIdeIdentTypeExtended,
       "cpqIdeIdentCondition2": cpqIdeIdentCondition2,
       "cpqIdeIdentStatus": cpqIdeIdentStatus,
       "cpqIdeIdentUltraAtaAvailability": cpqIdeIdentUltraAtaAvailability,
       "cpqIdeController": cpqIdeController,
       "cpqIdeControllerTable": cpqIdeControllerTable,
       "cpqIdeControllerEntry": cpqIdeControllerEntry,
       "cpqIdeControllerIndex": cpqIdeControllerIndex,
       "cpqIdeControllerOverallCondition": cpqIdeControllerOverallCondition,
       "cpqIdeControllerModel": cpqIdeControllerModel,
       "cpqIdeControllerFwRev": cpqIdeControllerFwRev,
       "cpqIdeControllerSlot": cpqIdeControllerSlot,
       "cpqIdeControllerStatus": cpqIdeControllerStatus,
       "cpqIdeControllerCondition": cpqIdeControllerCondition,
       "cpqIdeControllerSerialNumber": cpqIdeControllerSerialNumber,
       "cpqIdeAtaDisk": cpqIdeAtaDisk,
       "cpqIdeAtaDiskTable": cpqIdeAtaDiskTable,
       "cpqIdeAtaDiskEntry": cpqIdeAtaDiskEntry,
       "cpqIdeAtaDiskControllerIndex": cpqIdeAtaDiskControllerIndex,
       "cpqIdeAtaDiskIndex": cpqIdeAtaDiskIndex,
       "cpqIdeAtaDiskModel": cpqIdeAtaDiskModel,
       "cpqIdeAtaDiskFwRev": cpqIdeAtaDiskFwRev,
       "cpqIdeAtaDiskSerialNumber": cpqIdeAtaDiskSerialNumber,
       "cpqIdeAtaDiskStatus": cpqIdeAtaDiskStatus,
       "cpqIdeAtaDiskCondition": cpqIdeAtaDiskCondition,
       "cpqIdeAtaDiskCapacity": cpqIdeAtaDiskCapacity,
       "cpqIdeAtaDiskSmartEnabled": cpqIdeAtaDiskSmartEnabled,
       "cpqIdeAtaDiskTransferMode": cpqIdeAtaDiskTransferMode,
       "cpqIdeAtaDiskChannel": cpqIdeAtaDiskChannel,
       "cpqIdeAtaDiskNumber": cpqIdeAtaDiskNumber,
       "cpqIdeAtaDiskLogicalDriveMember": cpqIdeAtaDiskLogicalDriveMember,
       "cpqIdeAtaDiskIsSpare": cpqIdeAtaDiskIsSpare,
       "cpqIdeAtaDiskOsName": cpqIdeAtaDiskOsName,
       "cpqIdeAtaDiskType": cpqIdeAtaDiskType,
       "cpqIdeAtaDiskSataVersion": cpqIdeAtaDiskSataVersion,
       "cpqIdeAtapiDevice": cpqIdeAtapiDevice,
       "cpqIdeAtapiDeviceTable": cpqIdeAtapiDeviceTable,
       "cpqIdeAtapiDeviceEntry": cpqIdeAtapiDeviceEntry,
       "cpqIdeAtapiDeviceControllerIndex": cpqIdeAtapiDeviceControllerIndex,
       "cpqIdeAtapiDeviceIndex": cpqIdeAtapiDeviceIndex,
       "cpqIdeAtapiDeviceModel": cpqIdeAtapiDeviceModel,
       "cpqIdeAtapiDeviceFwRev": cpqIdeAtapiDeviceFwRev,
       "cpqIdeAtapiDeviceType": cpqIdeAtapiDeviceType,
       "cpqIdeAtapiDeviceTypeExtended": cpqIdeAtapiDeviceTypeExtended,
       "cpqIdeAtapiDeviceChannel": cpqIdeAtapiDeviceChannel,
       "cpqIdeAtapiDeviceNumber": cpqIdeAtapiDeviceNumber,
       "cpqIdeLogicalDrive": cpqIdeLogicalDrive,
       "cpqIdeLogicalDriveTable": cpqIdeLogicalDriveTable,
       "cpqIdeLogicalDriveEntry": cpqIdeLogicalDriveEntry,
       "cpqIdeLogicalDriveControllerIndex": cpqIdeLogicalDriveControllerIndex,
       "cpqIdeLogicalDriveIndex": cpqIdeLogicalDriveIndex,
       "cpqIdeLogicalDriveRaidLevel": cpqIdeLogicalDriveRaidLevel,
       "cpqIdeLogicalDriveCapacity": cpqIdeLogicalDriveCapacity,
       "cpqIdeLogicalDriveStatus": cpqIdeLogicalDriveStatus,
       "cpqIdeLogicalDriveCondition": cpqIdeLogicalDriveCondition,
       "cpqIdeLogicalDriveDiskIds": cpqIdeLogicalDriveDiskIds,
       "cpqIdeLogicalDriveStripeSize": cpqIdeLogicalDriveStripeSize,
       "cpqIdeLogicalDriveSpareIds": cpqIdeLogicalDriveSpareIds,
       "cpqIdeLogicalDriveRebuildingDisk": cpqIdeLogicalDriveRebuildingDisk,
       "cpqIdeLogicalDriveOsName": cpqIdeLogicalDriveOsName}
)
