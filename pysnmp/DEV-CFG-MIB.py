# SNMP MIB module (DEV-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEV-CFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:04 2024
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

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbDeviceConfig_ObjectIdentity = ObjectIdentity
nbDeviceConfig = _NbDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11)
)
_NbDevGen_ObjectIdentity = ObjectIdentity
nbDevGen = _NbDevGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1)
)


class _NbDevOperationMode_Type(Integer32):
    """Custom type nbDevOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accelerouter", 1),
          ("router", 2),
          ("switch", 3))
    )


_NbDevOperationMode_Type.__name__ = "Integer32"
_NbDevOperationMode_Object = MibScalar
nbDevOperationMode = _NbDevOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 1),
    _NbDevOperationMode_Type()
)
nbDevOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevOperationMode.setStatus("mandatory")
_NbDevErrorText_Type = DisplayString
_NbDevErrorText_Object = MibScalar
nbDevErrorText = _NbDevErrorText_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 2),
    _NbDevErrorText_Type()
)
nbDevErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevErrorText.setStatus("mandatory")


class _NbDevRouterSaveConfig_Type(Integer32):
    """Custom type nbDevRouterSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetConfig", 2),
          ("saveConfig", 1))
    )


_NbDevRouterSaveConfig_Type.__name__ = "Integer32"
_NbDevRouterSaveConfig_Object = MibScalar
nbDevRouterSaveConfig = _NbDevRouterSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 4),
    _NbDevRouterSaveConfig_Type()
)
nbDevRouterSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbDevRouterSaveConfig.setStatus("mandatory")
_NbsDevProperties_Type = Integer32
_NbsDevProperties_Object = MibScalar
nbsDevProperties = _NbsDevProperties_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 5),
    _NbsDevProperties_Type()
)
nbsDevProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevProperties.setStatus("mandatory")


class _NbsDevTemperatureMode_Type(Integer32):
    """Custom type nbsDevTemperatureMode based on Integer32"""
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
          ("none", 1),
          ("normal", 2))
    )


_NbsDevTemperatureMode_Type.__name__ = "Integer32"
_NbsDevTemperatureMode_Object = MibScalar
nbsDevTemperatureMode = _NbsDevTemperatureMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 6),
    _NbsDevTemperatureMode_Type()
)
nbsDevTemperatureMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevTemperatureMode.setStatus("mandatory")
_NbsDevPS_ObjectIdentity = ObjectIdentity
nbsDevPS = _NbsDevPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8)
)
_NbsDevPSNumber_Type = Integer32
_NbsDevPSNumber_Object = MibScalar
nbsDevPSNumber = _NbsDevPSNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 1),
    _NbsDevPSNumber_Type()
)
nbsDevPSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSNumber.setStatus("mandatory")
_NbsDevPSTable_Object = MibTable
nbsDevPSTable = _NbsDevPSTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2)
)
if mibBuilder.loadTexts:
    nbsDevPSTable.setStatus("mandatory")
_NbsDevPSEntry_Object = MibTableRow
nbsDevPSEntry = _NbsDevPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1)
)
nbsDevPSEntry.setIndexNames(
    (0, "DEV-CFG-MIB", "nbsDevPSIndex"),
)
if mibBuilder.loadTexts:
    nbsDevPSEntry.setStatus("mandatory")
_NbsDevPSIndex_Type = Integer32
_NbsDevPSIndex_Object = MibTableColumn
nbsDevPSIndex = _NbsDevPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 1),
    _NbsDevPSIndex_Type()
)
nbsDevPSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSIndex.setStatus("mandatory")


class _NbsDevPSType_Type(Integer32):
    """Custom type nbsDevPSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acPS", 2),
          ("dcPS", 3),
          ("none", 1))
    )


_NbsDevPSType_Type.__name__ = "Integer32"
_NbsDevPSType_Object = MibTableColumn
nbsDevPSType = _NbsDevPSType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 2),
    _NbsDevPSType_Type()
)
nbsDevPSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSType.setStatus("mandatory")
_NbsDevPSDescription_Type = DisplayString
_NbsDevPSDescription_Object = MibTableColumn
nbsDevPSDescription = _NbsDevPSDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 3),
    _NbsDevPSDescription_Type()
)
nbsDevPSDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSDescription.setStatus("mandatory")


class _NbsDevPSRedundantMode_Type(Integer32):
    """Custom type nbsDevPSRedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mainPS", 2),
          ("none", 1),
          ("secondaryPS", 3))
    )


_NbsDevPSRedundantMode_Type.__name__ = "Integer32"
_NbsDevPSRedundantMode_Object = MibTableColumn
nbsDevPSRedundantMode = _NbsDevPSRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 4),
    _NbsDevPSRedundantMode_Type()
)
nbsDevPSRedundantMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSRedundantMode.setStatus("mandatory")


class _NbsDevPSOperStatus_Type(Integer32):
    """Custom type nbsDevPSOperStatus based on Integer32"""
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
          ("none", 1),
          ("notActive", 3))
    )


_NbsDevPSOperStatus_Type.__name__ = "Integer32"
_NbsDevPSOperStatus_Object = MibTableColumn
nbsDevPSOperStatus = _NbsDevPSOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 5),
    _NbsDevPSOperStatus_Type()
)
nbsDevPSOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSOperStatus.setStatus("mandatory")


class _NbsDevPSAdminStatus_Type(Integer32):
    """Custom type nbsDevPSAdminStatus based on Integer32"""
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
          ("none", 1),
          ("notActive", 3))
    )


_NbsDevPSAdminStatus_Type.__name__ = "Integer32"
_NbsDevPSAdminStatus_Object = MibTableColumn
nbsDevPSAdminStatus = _NbsDevPSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 6),
    _NbsDevPSAdminStatus_Type()
)
nbsDevPSAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevPSAdminStatus.setStatus("mandatory")
_NbsDevPSInput_ObjectIdentity = ObjectIdentity
nbsDevPSInput = _NbsDevPSInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9)
)
_NbsDevPSInputNumber_Type = Integer32
_NbsDevPSInputNumber_Object = MibScalar
nbsDevPSInputNumber = _NbsDevPSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 1),
    _NbsDevPSInputNumber_Type()
)
nbsDevPSInputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputNumber.setStatus("mandatory")
_NbsDevPSInputTable_Object = MibTable
nbsDevPSInputTable = _NbsDevPSInputTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2)
)
if mibBuilder.loadTexts:
    nbsDevPSInputTable.setStatus("mandatory")
_NbsDevPSInputEntry_Object = MibTableRow
nbsDevPSInputEntry = _NbsDevPSInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1)
)
nbsDevPSInputEntry.setIndexNames(
    (0, "DEV-CFG-MIB", "nbsDevPSInputIndex"),
)
if mibBuilder.loadTexts:
    nbsDevPSInputEntry.setStatus("mandatory")
_NbsDevPSInputIndex_Type = Integer32
_NbsDevPSInputIndex_Object = MibTableColumn
nbsDevPSInputIndex = _NbsDevPSInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 1),
    _NbsDevPSInputIndex_Type()
)
nbsDevPSInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputIndex.setStatus("mandatory")


class _NbsDevPSInputType_Type(Integer32):
    """Custom type nbsDevPSInputType based on Integer32"""
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
        *(("acInput", 2),
          ("dcInput", 3),
          ("dcRedundInput", 4),
          ("none", 1))
    )


_NbsDevPSInputType_Type.__name__ = "Integer32"
_NbsDevPSInputType_Object = MibTableColumn
nbsDevPSInputType = _NbsDevPSInputType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 2),
    _NbsDevPSInputType_Type()
)
nbsDevPSInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputType.setStatus("mandatory")
_NbsDevPSInputDescription_Type = DisplayString
_NbsDevPSInputDescription_Object = MibTableColumn
nbsDevPSInputDescription = _NbsDevPSInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 3),
    _NbsDevPSInputDescription_Type()
)
nbsDevPSInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputDescription.setStatus("mandatory")


class _NbsDevPSInputRedundantMode_Type(Integer32):
    """Custom type nbsDevPSInputRedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mainInput", 2),
          ("none", 1),
          ("secondaryInput", 3))
    )


_NbsDevPSInputRedundantMode_Type.__name__ = "Integer32"
_NbsDevPSInputRedundantMode_Object = MibTableColumn
nbsDevPSInputRedundantMode = _NbsDevPSInputRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 4),
    _NbsDevPSInputRedundantMode_Type()
)
nbsDevPSInputRedundantMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputRedundantMode.setStatus("mandatory")


class _NbsDevPSInputOperStatus_Type(Integer32):
    """Custom type nbsDevPSInputOperStatus based on Integer32"""
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
          ("none", 1),
          ("notActive", 3))
    )


_NbsDevPSInputOperStatus_Type.__name__ = "Integer32"
_NbsDevPSInputOperStatus_Object = MibTableColumn
nbsDevPSInputOperStatus = _NbsDevPSInputOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 5),
    _NbsDevPSInputOperStatus_Type()
)
nbsDevPSInputOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputOperStatus.setStatus("mandatory")


class _NbsDevPSInputAdminStatus_Type(Integer32):
    """Custom type nbsDevPSInputAdminStatus based on Integer32"""
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
          ("none", 1),
          ("notActive", 3))
    )


_NbsDevPSInputAdminStatus_Type.__name__ = "Integer32"
_NbsDevPSInputAdminStatus_Object = MibTableColumn
nbsDevPSInputAdminStatus = _NbsDevPSInputAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 6),
    _NbsDevPSInputAdminStatus_Type()
)
nbsDevPSInputAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevPSInputAdminStatus.setStatus("mandatory")
_NbsDevCPU_ObjectIdentity = ObjectIdentity
nbsDevCPU = _NbsDevCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10)
)
_NbsDevCPUNumber_Type = Integer32
_NbsDevCPUNumber_Object = MibScalar
nbsDevCPUNumber = _NbsDevCPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 1),
    _NbsDevCPUNumber_Type()
)
nbsDevCPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUNumber.setStatus("mandatory")
_NbsDevCPUTable_Object = MibTable
nbsDevCPUTable = _NbsDevCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2)
)
if mibBuilder.loadTexts:
    nbsDevCPUTable.setStatus("mandatory")
_NbsDevCPUEntry_Object = MibTableRow
nbsDevCPUEntry = _NbsDevCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1)
)
nbsDevCPUEntry.setIndexNames(
    (0, "DEV-CFG-MIB", "nbsDevCPUIndex"),
)
if mibBuilder.loadTexts:
    nbsDevCPUEntry.setStatus("mandatory")
_NbsDevCPUIndex_Type = Integer32
_NbsDevCPUIndex_Object = MibTableColumn
nbsDevCPUIndex = _NbsDevCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 1),
    _NbsDevCPUIndex_Type()
)
nbsDevCPUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUIndex.setStatus("mandatory")


class _NbsDevCPUType_Type(Integer32):
    """Custom type nbsDevCPUType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cx33CPU", 2),
          ("none", 1))
    )


_NbsDevCPUType_Type.__name__ = "Integer32"
_NbsDevCPUType_Object = MibTableColumn
nbsDevCPUType = _NbsDevCPUType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 2),
    _NbsDevCPUType_Type()
)
nbsDevCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUType.setStatus("mandatory")
_NbsDevCPUDescription_Type = DisplayString
_NbsDevCPUDescription_Object = MibTableColumn
nbsDevCPUDescription = _NbsDevCPUDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 3),
    _NbsDevCPUDescription_Type()
)
nbsDevCPUDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUDescription.setStatus("mandatory")


class _NbsDevCPURedundantMode_Type(Integer32):
    """Custom type nbsDevCPURedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mainCPU", 2),
          ("none", 1),
          ("redundantCPU", 3))
    )


_NbsDevCPURedundantMode_Type.__name__ = "Integer32"
_NbsDevCPURedundantMode_Object = MibTableColumn
nbsDevCPURedundantMode = _NbsDevCPURedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 4),
    _NbsDevCPURedundantMode_Type()
)
nbsDevCPURedundantMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPURedundantMode.setStatus("mandatory")


class _NbsDevCPUOperStatus_Type(Integer32):
    """Custom type nbsDevCPUOperStatus based on Integer32"""
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
          ("none", 1))
    )


_NbsDevCPUOperStatus_Type.__name__ = "Integer32"
_NbsDevCPUOperStatus_Object = MibTableColumn
nbsDevCPUOperStatus = _NbsDevCPUOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 5),
    _NbsDevCPUOperStatus_Type()
)
nbsDevCPUOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUOperStatus.setStatus("mandatory")


class _NbsDevCPUAdminStatus_Type(Integer32):
    """Custom type nbsDevCPUAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("none", 1))
    )


_NbsDevCPUAdminStatus_Type.__name__ = "Integer32"
_NbsDevCPUAdminStatus_Object = MibTableColumn
nbsDevCPUAdminStatus = _NbsDevCPUAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 6),
    _NbsDevCPUAdminStatus_Type()
)
nbsDevCPUAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevCPUAdminStatus.setStatus("mandatory")
_NbsDevCPUOrderNumber_Type = Integer32
_NbsDevCPUOrderNumber_Object = MibTableColumn
nbsDevCPUOrderNumber = _NbsDevCPUOrderNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 7),
    _NbsDevCPUOrderNumber_Type()
)
nbsDevCPUOrderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUOrderNumber.setStatus("mandatory")
_NbsDevFAN_ObjectIdentity = ObjectIdentity
nbsDevFAN = _NbsDevFAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11)
)
_NbsDevFANsNumber_Type = Integer32
_NbsDevFANsNumber_Object = MibScalar
nbsDevFANsNumber = _NbsDevFANsNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 1),
    _NbsDevFANsNumber_Type()
)
nbsDevFANsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANsNumber.setStatus("mandatory")
_NbsDevFANTable_Object = MibTable
nbsDevFANTable = _NbsDevFANTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2)
)
if mibBuilder.loadTexts:
    nbsDevFANTable.setStatus("mandatory")
_NbsDevFANEntry_Object = MibTableRow
nbsDevFANEntry = _NbsDevFANEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1)
)
nbsDevFANEntry.setIndexNames(
    (0, "DEV-CFG-MIB", "nbsDevFANIndex"),
)
if mibBuilder.loadTexts:
    nbsDevFANEntry.setStatus("mandatory")
_NbsDevFANIndex_Type = Integer32
_NbsDevFANIndex_Object = MibTableColumn
nbsDevFANIndex = _NbsDevFANIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 1),
    _NbsDevFANIndex_Type()
)
nbsDevFANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANIndex.setStatus("mandatory")


class _NbsDevFANType_Type(Integer32):
    """Custom type nbsDevFANType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("none", 1)
    )


_NbsDevFANType_Type.__name__ = "Integer32"
_NbsDevFANType_Object = MibTableColumn
nbsDevFANType = _NbsDevFANType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 2),
    _NbsDevFANType_Type()
)
nbsDevFANType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANType.setStatus("mandatory")
_NbsDevFANDescription_Type = DisplayString
_NbsDevFANDescription_Object = MibTableColumn
nbsDevFANDescription = _NbsDevFANDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 3),
    _NbsDevFANDescription_Type()
)
nbsDevFANDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANDescription.setStatus("mandatory")


class _NbsDevFANOperStatus_Type(Integer32):
    """Custom type nbsDevFANOperStatus based on Integer32"""
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
          ("none", 1),
          ("notActive", 3))
    )


_NbsDevFANOperStatus_Type.__name__ = "Integer32"
_NbsDevFANOperStatus_Object = MibTableColumn
nbsDevFANOperStatus = _NbsDevFANOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 5),
    _NbsDevFANOperStatus_Type()
)
nbsDevFANOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANOperStatus.setStatus("mandatory")


class _NbsDevFANAdminStatus_Type(Integer32):
    """Custom type nbsDevFANAdminStatus based on Integer32"""
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
          ("none", 1),
          ("notActive", 3))
    )


_NbsDevFANAdminStatus_Type.__name__ = "Integer32"
_NbsDevFANAdminStatus_Object = MibTableColumn
nbsDevFANAdminStatus = _NbsDevFANAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 6),
    _NbsDevFANAdminStatus_Type()
)
nbsDevFANAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevFANAdminStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEV-CFG-MIB",
    **{"nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbDeviceConfig": nbDeviceConfig,
       "nbDevGen": nbDevGen,
       "nbDevOperationMode": nbDevOperationMode,
       "nbDevErrorText": nbDevErrorText,
       "nbDevRouterSaveConfig": nbDevRouterSaveConfig,
       "nbsDevProperties": nbsDevProperties,
       "nbsDevTemperatureMode": nbsDevTemperatureMode,
       "nbsDevPS": nbsDevPS,
       "nbsDevPSNumber": nbsDevPSNumber,
       "nbsDevPSTable": nbsDevPSTable,
       "nbsDevPSEntry": nbsDevPSEntry,
       "nbsDevPSIndex": nbsDevPSIndex,
       "nbsDevPSType": nbsDevPSType,
       "nbsDevPSDescription": nbsDevPSDescription,
       "nbsDevPSRedundantMode": nbsDevPSRedundantMode,
       "nbsDevPSOperStatus": nbsDevPSOperStatus,
       "nbsDevPSAdminStatus": nbsDevPSAdminStatus,
       "nbsDevPSInput": nbsDevPSInput,
       "nbsDevPSInputNumber": nbsDevPSInputNumber,
       "nbsDevPSInputTable": nbsDevPSInputTable,
       "nbsDevPSInputEntry": nbsDevPSInputEntry,
       "nbsDevPSInputIndex": nbsDevPSInputIndex,
       "nbsDevPSInputType": nbsDevPSInputType,
       "nbsDevPSInputDescription": nbsDevPSInputDescription,
       "nbsDevPSInputRedundantMode": nbsDevPSInputRedundantMode,
       "nbsDevPSInputOperStatus": nbsDevPSInputOperStatus,
       "nbsDevPSInputAdminStatus": nbsDevPSInputAdminStatus,
       "nbsDevCPU": nbsDevCPU,
       "nbsDevCPUNumber": nbsDevCPUNumber,
       "nbsDevCPUTable": nbsDevCPUTable,
       "nbsDevCPUEntry": nbsDevCPUEntry,
       "nbsDevCPUIndex": nbsDevCPUIndex,
       "nbsDevCPUType": nbsDevCPUType,
       "nbsDevCPUDescription": nbsDevCPUDescription,
       "nbsDevCPURedundantMode": nbsDevCPURedundantMode,
       "nbsDevCPUOperStatus": nbsDevCPUOperStatus,
       "nbsDevCPUAdminStatus": nbsDevCPUAdminStatus,
       "nbsDevCPUOrderNumber": nbsDevCPUOrderNumber,
       "nbsDevFAN": nbsDevFAN,
       "nbsDevFANsNumber": nbsDevFANsNumber,
       "nbsDevFANTable": nbsDevFANTable,
       "nbsDevFANEntry": nbsDevFANEntry,
       "nbsDevFANIndex": nbsDevFANIndex,
       "nbsDevFANType": nbsDevFANType,
       "nbsDevFANDescription": nbsDevFANDescription,
       "nbsDevFANOperStatus": nbsDevFANOperStatus,
       "nbsDevFANAdminStatus": nbsDevFANAdminStatus}
)
