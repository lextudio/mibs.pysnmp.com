# SNMP MIB module (DLGHWINF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLGHWINF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:37 2024
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

(dialogic,
 dlgHardwareInfo) = mibBuilder.importSymbols(
    "DLGC-GLOBAL-REG",
    "dialogic",
    "dlgHardwareInfo")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlgHiMibRev_ObjectIdentity = ObjectIdentity
dlgHiMibRev = _DlgHiMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 1)
)


class _DlgHiMibRevMajor_Type(Integer32):
    """Custom type dlgHiMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DlgHiMibRevMajor_Type.__name__ = "Integer32"
_DlgHiMibRevMajor_Object = MibScalar
dlgHiMibRevMajor = _DlgHiMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 1, 1),
    _DlgHiMibRevMajor_Type()
)
dlgHiMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiMibRevMajor.setStatus("mandatory")


class _DlgHiMibRevMinor_Type(Integer32):
    """Custom type dlgHiMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlgHiMibRevMinor_Type.__name__ = "Integer32"
_DlgHiMibRevMinor_Object = MibScalar
dlgHiMibRevMinor = _DlgHiMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 1, 2),
    _DlgHiMibRevMinor_Type()
)
dlgHiMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiMibRevMinor.setStatus("mandatory")


class _DlgHiMibCondition_Type(Integer32):
    """Custom type dlgHiMibCondition based on Integer32"""
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


_DlgHiMibCondition_Type.__name__ = "Integer32"
_DlgHiMibCondition_Object = MibScalar
dlgHiMibCondition = _DlgHiMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 1, 3),
    _DlgHiMibCondition_Type()
)
dlgHiMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiMibCondition.setStatus("mandatory")
_DlgHiComponent_ObjectIdentity = ObjectIdentity
dlgHiComponent = _DlgHiComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2)
)
_DlgHiInterface_ObjectIdentity = ObjectIdentity
dlgHiInterface = _DlgHiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1)
)
_DlgHiOsCommon_ObjectIdentity = ObjectIdentity
dlgHiOsCommon = _DlgHiOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1)
)


class _DlgHiOsCommonPollFreq_Type(Integer32):
    """Custom type dlgHiOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlgHiOsCommonPollFreq_Type.__name__ = "Integer32"
_DlgHiOsCommonPollFreq_Object = MibScalar
dlgHiOsCommonPollFreq = _DlgHiOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 1),
    _DlgHiOsCommonPollFreq_Type()
)
dlgHiOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgHiOsCommonPollFreq.setStatus("mandatory")
_DlgHiOsCommonNumberOfModules_Type = Integer32
_DlgHiOsCommonNumberOfModules_Object = MibScalar
dlgHiOsCommonNumberOfModules = _DlgHiOsCommonNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 2),
    _DlgHiOsCommonNumberOfModules_Type()
)
dlgHiOsCommonNumberOfModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiOsCommonNumberOfModules.setStatus("mandatory")
_DlgHiOsCommonModuleTable_Object = MibTable
dlgHiOsCommonModuleTable = _DlgHiOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dlgHiOsCommonModuleTable.setStatus("mandatory")
_DlgHiOsCommonModuleEntry_Object = MibTableRow
dlgHiOsCommonModuleEntry = _DlgHiOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 3, 1)
)
dlgHiOsCommonModuleEntry.setIndexNames(
    (0, "DLGHWINF-MIB", "dlgHiOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    dlgHiOsCommonModuleEntry.setStatus("mandatory")


class _DlgHiOsCommonModuleIndex_Type(Integer32):
    """Custom type dlgHiOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlgHiOsCommonModuleIndex_Type.__name__ = "Integer32"
_DlgHiOsCommonModuleIndex_Object = MibTableColumn
dlgHiOsCommonModuleIndex = _DlgHiOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 3, 1, 1),
    _DlgHiOsCommonModuleIndex_Type()
)
dlgHiOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiOsCommonModuleIndex.setStatus("mandatory")


class _DlgHiOsCommonModuleName_Type(DisplayString):
    """Custom type dlgHiOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlgHiOsCommonModuleName_Type.__name__ = "DisplayString"
_DlgHiOsCommonModuleName_Object = MibTableColumn
dlgHiOsCommonModuleName = _DlgHiOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 3, 1, 2),
    _DlgHiOsCommonModuleName_Type()
)
dlgHiOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiOsCommonModuleName.setStatus("mandatory")


class _DlgHiOsCommonModuleVersion_Type(DisplayString):
    """Custom type dlgHiOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_DlgHiOsCommonModuleVersion_Type.__name__ = "DisplayString"
_DlgHiOsCommonModuleVersion_Object = MibTableColumn
dlgHiOsCommonModuleVersion = _DlgHiOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 3, 1, 3),
    _DlgHiOsCommonModuleVersion_Type()
)
dlgHiOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiOsCommonModuleVersion.setStatus("mandatory")


class _DlgHiOsCommonModuleDate_Type(OctetString):
    """Custom type dlgHiOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_DlgHiOsCommonModuleDate_Type.__name__ = "OctetString"
_DlgHiOsCommonModuleDate_Object = MibTableColumn
dlgHiOsCommonModuleDate = _DlgHiOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 3, 1, 4),
    _DlgHiOsCommonModuleDate_Type()
)
dlgHiOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiOsCommonModuleDate.setStatus("mandatory")


class _DlgHiOsCommonModulePurpose_Type(DisplayString):
    """Custom type dlgHiOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlgHiOsCommonModulePurpose_Type.__name__ = "DisplayString"
_DlgHiOsCommonModulePurpose_Object = MibTableColumn
dlgHiOsCommonModulePurpose = _DlgHiOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 3, 1, 5),
    _DlgHiOsCommonModulePurpose_Type()
)
dlgHiOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiOsCommonModulePurpose.setStatus("mandatory")


class _DlgHiOsLogEnable_Type(Integer32):
    """Custom type dlgHiOsLogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DlgHiOsLogEnable_Type.__name__ = "Integer32"
_DlgHiOsLogEnable_Object = MibScalar
dlgHiOsLogEnable = _DlgHiOsLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 4),
    _DlgHiOsLogEnable_Type()
)
dlgHiOsLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgHiOsLogEnable.setStatus("mandatory")


class _DlgHiOsTestTrapEnable_Type(Integer32):
    """Custom type dlgHiOsTestTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_DlgHiOsTestTrapEnable_Type.__name__ = "Integer32"
_DlgHiOsTestTrapEnable_Object = MibScalar
dlgHiOsTestTrapEnable = _DlgHiOsTestTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 5),
    _DlgHiOsTestTrapEnable_Type()
)
dlgHiOsTestTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgHiOsTestTrapEnable.setStatus("mandatory")


class _DlgHiIdentSystemServicesNameForTrap_Type(DisplayString):
    """Custom type dlgHiIdentSystemServicesNameForTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DlgHiIdentSystemServicesNameForTrap_Type.__name__ = "DisplayString"
_DlgHiIdentSystemServicesNameForTrap_Object = MibScalar
dlgHiIdentSystemServicesNameForTrap = _DlgHiIdentSystemServicesNameForTrap_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 6),
    _DlgHiIdentSystemServicesNameForTrap_Type()
)
dlgHiIdentSystemServicesNameForTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentSystemServicesNameForTrap.setStatus("mandatory")


class _DlgHiIdentSystemServicesStatusForTrap_Type(Integer32):
    """Custom type dlgHiIdentSystemServicesStatusForTrap based on Integer32"""
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
          ("start-pending", 5),
          ("started", 2),
          ("stop-pending", 3),
          ("stopped", 4))
    )


_DlgHiIdentSystemServicesStatusForTrap_Type.__name__ = "Integer32"
_DlgHiIdentSystemServicesStatusForTrap_Object = MibScalar
dlgHiIdentSystemServicesStatusForTrap = _DlgHiIdentSystemServicesStatusForTrap_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 7),
    _DlgHiIdentSystemServicesStatusForTrap_Type()
)
dlgHiIdentSystemServicesStatusForTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentSystemServicesStatusForTrap.setStatus("mandatory")


class _DlgHiIdentIndexForTrap_Type(Integer32):
    """Custom type dlgHiIdentIndexForTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlgHiIdentIndexForTrap_Type.__name__ = "Integer32"
_DlgHiIdentIndexForTrap_Object = MibScalar
dlgHiIdentIndexForTrap = _DlgHiIdentIndexForTrap_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 8),
    _DlgHiIdentIndexForTrap_Type()
)
dlgHiIdentIndexForTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentIndexForTrap.setStatus("mandatory")


class _DlgHiIdentModelForTrap_Type(DisplayString):
    """Custom type dlgHiIdentModelForTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DlgHiIdentModelForTrap_Type.__name__ = "DisplayString"
_DlgHiIdentModelForTrap_Object = MibScalar
dlgHiIdentModelForTrap = _DlgHiIdentModelForTrap_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 9),
    _DlgHiIdentModelForTrap_Type()
)
dlgHiIdentModelForTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentModelForTrap.setStatus("mandatory")


class _DlgHiIdentOperStatusForTrap_Type(Integer32):
    """Custom type dlgHiIdentOperStatusForTrap based on Integer32"""
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


_DlgHiIdentOperStatusForTrap_Type.__name__ = "Integer32"
_DlgHiIdentOperStatusForTrap_Object = MibScalar
dlgHiIdentOperStatusForTrap = _DlgHiIdentOperStatusForTrap_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 10),
    _DlgHiIdentOperStatusForTrap_Type()
)
dlgHiIdentOperStatusForTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentOperStatusForTrap.setStatus("mandatory")


class _DlgHiIdentAdminStatusForTrap_Type(Integer32):
    """Custom type dlgHiIdentAdminStatusForTrap based on Integer32"""
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
        *(("diagnose", 5),
          ("disabled", 4),
          ("other", 1),
          ("start-pending", 6),
          ("started", 2),
          ("stop-pending", 7),
          ("stopped", 3))
    )


_DlgHiIdentAdminStatusForTrap_Type.__name__ = "Integer32"
_DlgHiIdentAdminStatusForTrap_Object = MibScalar
dlgHiIdentAdminStatusForTrap = _DlgHiIdentAdminStatusForTrap_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 11),
    _DlgHiIdentAdminStatusForTrap_Type()
)
dlgHiIdentAdminStatusForTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentAdminStatusForTrap.setStatus("mandatory")


class _DlgHiIdentSerNumForTrap_Type(DisplayString):
    """Custom type dlgHiIdentSerNumForTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DlgHiIdentSerNumForTrap_Type.__name__ = "DisplayString"
_DlgHiIdentSerNumForTrap_Object = MibScalar
dlgHiIdentSerNumForTrap = _DlgHiIdentSerNumForTrap_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 12),
    _DlgHiIdentSerNumForTrap_Type()
)
dlgHiIdentSerNumForTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentSerNumForTrap.setStatus("mandatory")


class _DlgHiIdentErrorMessageForTrap_Type(DisplayString):
    """Custom type dlgHiIdentErrorMessageForTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_DlgHiIdentErrorMessageForTrap_Type.__name__ = "DisplayString"
_DlgHiIdentErrorMessageForTrap_Object = MibScalar
dlgHiIdentErrorMessageForTrap = _DlgHiIdentErrorMessageForTrap_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 1, 1, 13),
    _DlgHiIdentErrorMessageForTrap_Type()
)
dlgHiIdentErrorMessageForTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentErrorMessageForTrap.setStatus("mandatory")
_DlgHiIdent_ObjectIdentity = ObjectIdentity
dlgHiIdent = _DlgHiIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2)
)
_DlgHiIdentTable_Object = MibTable
dlgHiIdentTable = _DlgHiIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dlgHiIdentTable.setStatus("mandatory")
_DlgHiIdentEntry_Object = MibTableRow
dlgHiIdentEntry = _DlgHiIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1)
)
dlgHiIdentEntry.setIndexNames(
    (0, "DLGHWINF-MIB", "dlgHiIdentIndex"),
)
if mibBuilder.loadTexts:
    dlgHiIdentEntry.setStatus("mandatory")


class _DlgHiIdentIndex_Type(Integer32):
    """Custom type dlgHiIdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlgHiIdentIndex_Type.__name__ = "Integer32"
_DlgHiIdentIndex_Object = MibTableColumn
dlgHiIdentIndex = _DlgHiIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 1),
    _DlgHiIdentIndex_Type()
)
dlgHiIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentIndex.setStatus("mandatory")


class _DlgHiIdentModel_Type(DisplayString):
    """Custom type dlgHiIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DlgHiIdentModel_Type.__name__ = "DisplayString"
_DlgHiIdentModel_Object = MibTableColumn
dlgHiIdentModel = _DlgHiIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 2),
    _DlgHiIdentModel_Type()
)
dlgHiIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentModel.setStatus("mandatory")


class _DlgHiIdentType_Type(Integer32):
    """Custom type dlgHiIdentType based on Integer32"""
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
        *(("dm3", 3),
          ("gammaCP", 4),
          ("other", 1),
          ("release4span", 2))
    )


_DlgHiIdentType_Type.__name__ = "Integer32"
_DlgHiIdentType_Object = MibTableColumn
dlgHiIdentType = _DlgHiIdentType_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 3),
    _DlgHiIdentType_Type()
)
dlgHiIdentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentType.setStatus("mandatory")


class _DlgHiIdentFuncDescr_Type(DisplayString):
    """Custom type dlgHiIdentFuncDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DlgHiIdentFuncDescr_Type.__name__ = "DisplayString"
_DlgHiIdentFuncDescr_Object = MibTableColumn
dlgHiIdentFuncDescr = _DlgHiIdentFuncDescr_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 4),
    _DlgHiIdentFuncDescr_Type()
)
dlgHiIdentFuncDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentFuncDescr.setStatus("mandatory")


class _DlgHiIdentSerNum_Type(DisplayString):
    """Custom type dlgHiIdentSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DlgHiIdentSerNum_Type.__name__ = "DisplayString"
_DlgHiIdentSerNum_Object = MibTableColumn
dlgHiIdentSerNum = _DlgHiIdentSerNum_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 5),
    _DlgHiIdentSerNum_Type()
)
dlgHiIdentSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentSerNum.setStatus("mandatory")


class _DlgHiIdentFWName_Type(DisplayString):
    """Custom type dlgHiIdentFWName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DlgHiIdentFWName_Type.__name__ = "DisplayString"
_DlgHiIdentFWName_Object = MibTableColumn
dlgHiIdentFWName = _DlgHiIdentFWName_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 6),
    _DlgHiIdentFWName_Type()
)
dlgHiIdentFWName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentFWName.setStatus("mandatory")


class _DlgHiIdentFWVers_Type(DisplayString):
    """Custom type dlgHiIdentFWVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DlgHiIdentFWVers_Type.__name__ = "DisplayString"
_DlgHiIdentFWVers_Object = MibTableColumn
dlgHiIdentFWVers = _DlgHiIdentFWVers_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 7),
    _DlgHiIdentFWVers_Type()
)
dlgHiIdentFWVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentFWVers.setStatus("mandatory")
_DlgHiIdentMemBaseAddr_Type = Integer32
_DlgHiIdentMemBaseAddr_Object = MibTableColumn
dlgHiIdentMemBaseAddr = _DlgHiIdentMemBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 8),
    _DlgHiIdentMemBaseAddr_Type()
)
dlgHiIdentMemBaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentMemBaseAddr.setStatus("mandatory")
_DlgHiIdentIOBaseAddr_Type = Integer32
_DlgHiIdentIOBaseAddr_Object = MibTableColumn
dlgHiIdentIOBaseAddr = _DlgHiIdentIOBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 9),
    _DlgHiIdentIOBaseAddr_Type()
)
dlgHiIdentIOBaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentIOBaseAddr.setStatus("mandatory")
_DlgHiIdentIrq_Type = Integer32
_DlgHiIdentIrq_Object = MibTableColumn
dlgHiIdentIrq = _DlgHiIdentIrq_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 10),
    _DlgHiIdentIrq_Type()
)
dlgHiIdentIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentIrq.setStatus("mandatory")
_DlgHiIdentBoardID_Type = Integer32
_DlgHiIdentBoardID_Object = MibTableColumn
dlgHiIdentBoardID = _DlgHiIdentBoardID_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 11),
    _DlgHiIdentBoardID_Type()
)
dlgHiIdentBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentBoardID.setStatus("mandatory")
_DlgHiIdentPCISlotID_Type = Integer32
_DlgHiIdentPCISlotID_Object = MibTableColumn
dlgHiIdentPCISlotID = _DlgHiIdentPCISlotID_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 12),
    _DlgHiIdentPCISlotID_Type()
)
dlgHiIdentPCISlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentPCISlotID.setStatus("mandatory")


class _DlgHiIdentOperStatus_Type(Integer32):
    """Custom type dlgHiIdentOperStatus based on Integer32"""
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


_DlgHiIdentOperStatus_Type.__name__ = "Integer32"
_DlgHiIdentOperStatus_Object = MibTableColumn
dlgHiIdentOperStatus = _DlgHiIdentOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 13),
    _DlgHiIdentOperStatus_Type()
)
dlgHiIdentOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentOperStatus.setStatus("mandatory")


class _DlgHiIdentAdminStatus_Type(Integer32):
    """Custom type dlgHiIdentAdminStatus based on Integer32"""
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
        *(("diagnose", 5),
          ("disabled", 4),
          ("other", 1),
          ("start-pending", 6),
          ("started", 2),
          ("stop-pending", 7),
          ("stopped", 3))
    )


_DlgHiIdentAdminStatus_Type.__name__ = "Integer32"
_DlgHiIdentAdminStatus_Object = MibTableColumn
dlgHiIdentAdminStatus = _DlgHiIdentAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 14),
    _DlgHiIdentAdminStatus_Type()
)
dlgHiIdentAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgHiIdentAdminStatus.setStatus("mandatory")


class _DlgHiIdentErrorMessage_Type(DisplayString):
    """Custom type dlgHiIdentErrorMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_DlgHiIdentErrorMessage_Type.__name__ = "DisplayString"
_DlgHiIdentErrorMessage_Object = MibTableColumn
dlgHiIdentErrorMessage = _DlgHiIdentErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 15),
    _DlgHiIdentErrorMessage_Type()
)
dlgHiIdentErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentErrorMessage.setStatus("mandatory")


class _DlgHiIdentDeviceChangeDate_Type(OctetString):
    """Custom type dlgHiIdentDeviceChangeDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_DlgHiIdentDeviceChangeDate_Type.__name__ = "OctetString"
_DlgHiIdentDeviceChangeDate_Object = MibTableColumn
dlgHiIdentDeviceChangeDate = _DlgHiIdentDeviceChangeDate_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 16),
    _DlgHiIdentDeviceChangeDate_Type()
)
dlgHiIdentDeviceChangeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentDeviceChangeDate.setStatus("mandatory")
_DlgHiIdentSpecific_Type = ObjectIdentifier
_DlgHiIdentSpecific_Object = MibTableColumn
dlgHiIdentSpecific = _DlgHiIdentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 17),
    _DlgHiIdentSpecific_Type()
)
dlgHiIdentSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentSpecific.setStatus("mandatory")
_DlgHiIdentPCIBusID_Type = Integer32
_DlgHiIdentPCIBusID_Object = MibTableColumn
dlgHiIdentPCIBusID = _DlgHiIdentPCIBusID_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 1, 1, 18),
    _DlgHiIdentPCIBusID_Type()
)
dlgHiIdentPCIBusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentPCIBusID.setStatus("mandatory")
_DlgHiIdentNumberOfDevices_Type = Integer32
_DlgHiIdentNumberOfDevices_Object = MibScalar
dlgHiIdentNumberOfDevices = _DlgHiIdentNumberOfDevices_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 2),
    _DlgHiIdentNumberOfDevices_Type()
)
dlgHiIdentNumberOfDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentNumberOfDevices.setStatus("mandatory")


class _DlgHiIdentServiceStatus_Type(Integer32):
    """Custom type dlgHiIdentServiceStatus based on Integer32"""
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
          ("start-pending", 5),
          ("started", 2),
          ("stop-pending", 3),
          ("stopped", 4))
    )


_DlgHiIdentServiceStatus_Type.__name__ = "Integer32"
_DlgHiIdentServiceStatus_Object = MibScalar
dlgHiIdentServiceStatus = _DlgHiIdentServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 3),
    _DlgHiIdentServiceStatus_Type()
)
dlgHiIdentServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgHiIdentServiceStatus.setStatus("mandatory")


class _DlgHiIdentServiceChangeDate_Type(OctetString):
    """Custom type dlgHiIdentServiceChangeDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_DlgHiIdentServiceChangeDate_Type.__name__ = "OctetString"
_DlgHiIdentServiceChangeDate_Object = MibScalar
dlgHiIdentServiceChangeDate = _DlgHiIdentServiceChangeDate_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 4),
    _DlgHiIdentServiceChangeDate_Type()
)
dlgHiIdentServiceChangeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentServiceChangeDate.setStatus("mandatory")
_DlgHiIdentTrapMask_Type = Integer32
_DlgHiIdentTrapMask_Object = MibScalar
dlgHiIdentTrapMask = _DlgHiIdentTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 5),
    _DlgHiIdentTrapMask_Type()
)
dlgHiIdentTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgHiIdentTrapMask.setStatus("mandatory")
_DlgHiIdentSystemServicesTable_Object = MibTable
dlgHiIdentSystemServicesTable = _DlgHiIdentSystemServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    dlgHiIdentSystemServicesTable.setStatus("mandatory")
_DlgHiIdentSystemServicesEntry_Object = MibTableRow
dlgHiIdentSystemServicesEntry = _DlgHiIdentSystemServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 6, 1)
)
dlgHiIdentSystemServicesEntry.setIndexNames(
    (0, "DLGHWINF-MIB", "dlgHiIdentSystemServicesIndex"),
)
if mibBuilder.loadTexts:
    dlgHiIdentSystemServicesEntry.setStatus("mandatory")


class _DlgHiIdentSystemServicesIndex_Type(Integer32):
    """Custom type dlgHiIdentSystemServicesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlgHiIdentSystemServicesIndex_Type.__name__ = "Integer32"
_DlgHiIdentSystemServicesIndex_Object = MibTableColumn
dlgHiIdentSystemServicesIndex = _DlgHiIdentSystemServicesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 6, 1, 1),
    _DlgHiIdentSystemServicesIndex_Type()
)
dlgHiIdentSystemServicesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentSystemServicesIndex.setStatus("mandatory")


class _DlgHiIdentSystemServicesName_Type(DisplayString):
    """Custom type dlgHiIdentSystemServicesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DlgHiIdentSystemServicesName_Type.__name__ = "DisplayString"
_DlgHiIdentSystemServicesName_Object = MibTableColumn
dlgHiIdentSystemServicesName = _DlgHiIdentSystemServicesName_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 6, 1, 2),
    _DlgHiIdentSystemServicesName_Type()
)
dlgHiIdentSystemServicesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentSystemServicesName.setStatus("mandatory")


class _DlgHiIdentSystemServicesScmName_Type(DisplayString):
    """Custom type dlgHiIdentSystemServicesScmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DlgHiIdentSystemServicesScmName_Type.__name__ = "DisplayString"
_DlgHiIdentSystemServicesScmName_Object = MibTableColumn
dlgHiIdentSystemServicesScmName = _DlgHiIdentSystemServicesScmName_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 6, 1, 3),
    _DlgHiIdentSystemServicesScmName_Type()
)
dlgHiIdentSystemServicesScmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentSystemServicesScmName.setStatus("mandatory")


class _DlgHiIdentSystemServicesStatus_Type(Integer32):
    """Custom type dlgHiIdentSystemServicesStatus based on Integer32"""
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
          ("start-pending", 5),
          ("started", 2),
          ("stop-pending", 3),
          ("stopped", 4))
    )


_DlgHiIdentSystemServicesStatus_Type.__name__ = "Integer32"
_DlgHiIdentSystemServicesStatus_Object = MibTableColumn
dlgHiIdentSystemServicesStatus = _DlgHiIdentSystemServicesStatus_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 6, 1, 4),
    _DlgHiIdentSystemServicesStatus_Type()
)
dlgHiIdentSystemServicesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgHiIdentSystemServicesStatus.setStatus("mandatory")


class _DlgHiIdentSystemServicesChangeDate_Type(OctetString):
    """Custom type dlgHiIdentSystemServicesChangeDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_DlgHiIdentSystemServicesChangeDate_Type.__name__ = "OctetString"
_DlgHiIdentSystemServicesChangeDate_Object = MibTableColumn
dlgHiIdentSystemServicesChangeDate = _DlgHiIdentSystemServicesChangeDate_Object(
    (1, 3, 6, 1, 4, 1, 3028, 1, 1, 2, 2, 6, 1, 5),
    _DlgHiIdentSystemServicesChangeDate_Type()
)
dlgHiIdentSystemServicesChangeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgHiIdentSystemServicesChangeDate.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dlgHiServiceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3028, 0, 1001)
)
dlgHiServiceChanged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("DLGHWINF-MIB", "dlgHiIdentServiceStatus"))
)
if mibBuilder.loadTexts:
    dlgHiServiceChanged.setStatus(
        ""
    )

dlgHiboardStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3028, 0, 1002)
)
dlgHiboardStatusChanged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("DLGHWINF-MIB", "dlgHiIdentIndexForTrap"),
        ("DLGHWINF-MIB", "dlgHiIdentOperStatusForTrap"),
        ("DLGHWINF-MIB", "dlgHiIdentAdminStatusForTrap"),
        ("DLGHWINF-MIB", "dlgHiIdentModelForTrap"),
        ("DLGHWINF-MIB", "dlgHiIdentSerNumForTrap"),
        ("DLGHWINF-MIB", "dlgHiIdentErrorMessageForTrap"))
)
if mibBuilder.loadTexts:
    dlgHiboardStatusChanged.setStatus(
        ""
    )

dlgHiNonDlgcServiceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3028, 0, 1003)
)
dlgHiNonDlgcServiceChanged.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("DLGHWINF-MIB", "dlgHiIdentSystemServicesNameForTrap"),
        ("DLGHWINF-MIB", "dlgHiIdentSystemServicesStatusForTrap"))
)
if mibBuilder.loadTexts:
    dlgHiNonDlgcServiceChanged.setStatus(
        ""
    )

dlgHiTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3028, 0, 1004)
)
dlgHiTestTrap.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    dlgHiTestTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLGHWINF-MIB",
    **{"dlgHiServiceChanged": dlgHiServiceChanged,
       "dlgHiboardStatusChanged": dlgHiboardStatusChanged,
       "dlgHiNonDlgcServiceChanged": dlgHiNonDlgcServiceChanged,
       "dlgHiTestTrap": dlgHiTestTrap,
       "dlgHiMibRev": dlgHiMibRev,
       "dlgHiMibRevMajor": dlgHiMibRevMajor,
       "dlgHiMibRevMinor": dlgHiMibRevMinor,
       "dlgHiMibCondition": dlgHiMibCondition,
       "dlgHiComponent": dlgHiComponent,
       "dlgHiInterface": dlgHiInterface,
       "dlgHiOsCommon": dlgHiOsCommon,
       "dlgHiOsCommonPollFreq": dlgHiOsCommonPollFreq,
       "dlgHiOsCommonNumberOfModules": dlgHiOsCommonNumberOfModules,
       "dlgHiOsCommonModuleTable": dlgHiOsCommonModuleTable,
       "dlgHiOsCommonModuleEntry": dlgHiOsCommonModuleEntry,
       "dlgHiOsCommonModuleIndex": dlgHiOsCommonModuleIndex,
       "dlgHiOsCommonModuleName": dlgHiOsCommonModuleName,
       "dlgHiOsCommonModuleVersion": dlgHiOsCommonModuleVersion,
       "dlgHiOsCommonModuleDate": dlgHiOsCommonModuleDate,
       "dlgHiOsCommonModulePurpose": dlgHiOsCommonModulePurpose,
       "dlgHiOsLogEnable": dlgHiOsLogEnable,
       "dlgHiOsTestTrapEnable": dlgHiOsTestTrapEnable,
       "dlgHiIdentSystemServicesNameForTrap": dlgHiIdentSystemServicesNameForTrap,
       "dlgHiIdentSystemServicesStatusForTrap": dlgHiIdentSystemServicesStatusForTrap,
       "dlgHiIdentIndexForTrap": dlgHiIdentIndexForTrap,
       "dlgHiIdentModelForTrap": dlgHiIdentModelForTrap,
       "dlgHiIdentOperStatusForTrap": dlgHiIdentOperStatusForTrap,
       "dlgHiIdentAdminStatusForTrap": dlgHiIdentAdminStatusForTrap,
       "dlgHiIdentSerNumForTrap": dlgHiIdentSerNumForTrap,
       "dlgHiIdentErrorMessageForTrap": dlgHiIdentErrorMessageForTrap,
       "dlgHiIdent": dlgHiIdent,
       "dlgHiIdentTable": dlgHiIdentTable,
       "dlgHiIdentEntry": dlgHiIdentEntry,
       "dlgHiIdentIndex": dlgHiIdentIndex,
       "dlgHiIdentModel": dlgHiIdentModel,
       "dlgHiIdentType": dlgHiIdentType,
       "dlgHiIdentFuncDescr": dlgHiIdentFuncDescr,
       "dlgHiIdentSerNum": dlgHiIdentSerNum,
       "dlgHiIdentFWName": dlgHiIdentFWName,
       "dlgHiIdentFWVers": dlgHiIdentFWVers,
       "dlgHiIdentMemBaseAddr": dlgHiIdentMemBaseAddr,
       "dlgHiIdentIOBaseAddr": dlgHiIdentIOBaseAddr,
       "dlgHiIdentIrq": dlgHiIdentIrq,
       "dlgHiIdentBoardID": dlgHiIdentBoardID,
       "dlgHiIdentPCISlotID": dlgHiIdentPCISlotID,
       "dlgHiIdentOperStatus": dlgHiIdentOperStatus,
       "dlgHiIdentAdminStatus": dlgHiIdentAdminStatus,
       "dlgHiIdentErrorMessage": dlgHiIdentErrorMessage,
       "dlgHiIdentDeviceChangeDate": dlgHiIdentDeviceChangeDate,
       "dlgHiIdentSpecific": dlgHiIdentSpecific,
       "dlgHiIdentPCIBusID": dlgHiIdentPCIBusID,
       "dlgHiIdentNumberOfDevices": dlgHiIdentNumberOfDevices,
       "dlgHiIdentServiceStatus": dlgHiIdentServiceStatus,
       "dlgHiIdentServiceChangeDate": dlgHiIdentServiceChangeDate,
       "dlgHiIdentTrapMask": dlgHiIdentTrapMask,
       "dlgHiIdentSystemServicesTable": dlgHiIdentSystemServicesTable,
       "dlgHiIdentSystemServicesEntry": dlgHiIdentSystemServicesEntry,
       "dlgHiIdentSystemServicesIndex": dlgHiIdentSystemServicesIndex,
       "dlgHiIdentSystemServicesName": dlgHiIdentSystemServicesName,
       "dlgHiIdentSystemServicesScmName": dlgHiIdentSystemServicesScmName,
       "dlgHiIdentSystemServicesStatus": dlgHiIdentSystemServicesStatus,
       "dlgHiIdentSystemServicesChangeDate": dlgHiIdentSystemServicesChangeDate}
)
