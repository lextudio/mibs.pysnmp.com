# SNMP MIB module (CPQIDA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQIDA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:27 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqDriveArray_ObjectIdentity = ObjectIdentity
cpqDriveArray = _CpqDriveArray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3)
)
_CpqDaMibRev_ObjectIdentity = ObjectIdentity
cpqDaMibRev = _CpqDaMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 1)
)


class _CpqDaMibRevMajor_Type(Integer32):
    """Custom type cpqDaMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqDaMibRevMajor_Type.__name__ = "Integer32"
_CpqDaMibRevMajor_Object = MibScalar
cpqDaMibRevMajor = _CpqDaMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 1, 1),
    _CpqDaMibRevMajor_Type()
)
cpqDaMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaMibRevMajor.setStatus("mandatory")


class _CpqDaMibRevMinor_Type(Integer32):
    """Custom type cpqDaMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaMibRevMinor_Type.__name__ = "Integer32"
_CpqDaMibRevMinor_Object = MibScalar
cpqDaMibRevMinor = _CpqDaMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 1, 2),
    _CpqDaMibRevMinor_Type()
)
cpqDaMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaMibRevMinor.setStatus("mandatory")


class _CpqDaMibCondition_Type(Integer32):
    """Custom type cpqDaMibCondition based on Integer32"""
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


_CpqDaMibCondition_Type.__name__ = "Integer32"
_CpqDaMibCondition_Object = MibScalar
cpqDaMibCondition = _CpqDaMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 1, 3),
    _CpqDaMibCondition_Type()
)
cpqDaMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaMibCondition.setStatus("mandatory")
_CpqDaComponent_ObjectIdentity = ObjectIdentity
cpqDaComponent = _CpqDaComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2)
)
_CpqDaInterface_ObjectIdentity = ObjectIdentity
cpqDaInterface = _CpqDaInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1)
)
_CpqDaOsNetWare3x_ObjectIdentity = ObjectIdentity
cpqDaOsNetWare3x = _CpqDaOsNetWare3x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1)
)


class _CpqDaNw3xDriverName_Type(DisplayString):
    """Custom type cpqDaNw3xDriverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaNw3xDriverName_Type.__name__ = "DisplayString"
_CpqDaNw3xDriverName_Object = MibScalar
cpqDaNw3xDriverName = _CpqDaNw3xDriverName_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 1),
    _CpqDaNw3xDriverName_Type()
)
cpqDaNw3xDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xDriverName.setStatus("deprecated")


class _CpqDaNw3xDriverVer_Type(DisplayString):
    """Custom type cpqDaNw3xDriverVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqDaNw3xDriverVer_Type.__name__ = "DisplayString"
_CpqDaNw3xDriverVer_Object = MibScalar
cpqDaNw3xDriverVer = _CpqDaNw3xDriverVer_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 2),
    _CpqDaNw3xDriverVer_Type()
)
cpqDaNw3xDriverVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xDriverVer.setStatus("deprecated")


class _CpqDaNw3xPollType_Type(Integer32):
    """Custom type cpqDaNw3xPollType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demand", 3),
          ("other", 1),
          ("polled", 2))
    )


_CpqDaNw3xPollType_Type.__name__ = "Integer32"
_CpqDaNw3xPollType_Object = MibScalar
cpqDaNw3xPollType = _CpqDaNw3xPollType_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 3),
    _CpqDaNw3xPollType_Type()
)
cpqDaNw3xPollType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xPollType.setStatus("deprecated")


class _CpqDaNw3xPollTime_Type(Integer32):
    """Custom type cpqDaNw3xPollTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CpqDaNw3xPollTime_Type.__name__ = "Integer32"
_CpqDaNw3xPollTime_Object = MibScalar
cpqDaNw3xPollTime = _CpqDaNw3xPollTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 4),
    _CpqDaNw3xPollTime_Type()
)
cpqDaNw3xPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xPollTime.setStatus("deprecated")
_CpqDaNw3xDriverStatTable_Object = MibTable
cpqDaNw3xDriverStatTable = _CpqDaNw3xDriverStatTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cpqDaNw3xDriverStatTable.setStatus("deprecated")
_CpqDaNw3xDriverStatEntry_Object = MibTableRow
cpqDaNw3xDriverStatEntry = _CpqDaNw3xDriverStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 5, 1)
)
cpqDaNw3xDriverStatEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaNw3xCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaNw3xLogDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqDaNw3xDriverStatEntry.setStatus("deprecated")


class _CpqDaNw3xCntlrIndex_Type(Integer32):
    """Custom type cpqDaNw3xCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaNw3xCntlrIndex_Type.__name__ = "Integer32"
_CpqDaNw3xCntlrIndex_Object = MibTableColumn
cpqDaNw3xCntlrIndex = _CpqDaNw3xCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 5, 1, 1),
    _CpqDaNw3xCntlrIndex_Type()
)
cpqDaNw3xCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xCntlrIndex.setStatus("deprecated")


class _CpqDaNw3xLogDrvIndex_Type(Integer32):
    """Custom type cpqDaNw3xLogDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaNw3xLogDrvIndex_Type.__name__ = "Integer32"
_CpqDaNw3xLogDrvIndex_Object = MibTableColumn
cpqDaNw3xLogDrvIndex = _CpqDaNw3xLogDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 5, 1, 2),
    _CpqDaNw3xLogDrvIndex_Type()
)
cpqDaNw3xLogDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xLogDrvIndex.setStatus("deprecated")
_CpqDaNw3xTotalReads_Type = Counter32
_CpqDaNw3xTotalReads_Object = MibTableColumn
cpqDaNw3xTotalReads = _CpqDaNw3xTotalReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 5, 1, 3),
    _CpqDaNw3xTotalReads_Type()
)
cpqDaNw3xTotalReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xTotalReads.setStatus("deprecated")
_CpqDaNw3xTotalWrites_Type = Counter32
_CpqDaNw3xTotalWrites_Object = MibTableColumn
cpqDaNw3xTotalWrites = _CpqDaNw3xTotalWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 5, 1, 4),
    _CpqDaNw3xTotalWrites_Type()
)
cpqDaNw3xTotalWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xTotalWrites.setStatus("deprecated")
_CpqDaNw3xCorrReads_Type = Counter32
_CpqDaNw3xCorrReads_Object = MibTableColumn
cpqDaNw3xCorrReads = _CpqDaNw3xCorrReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 5, 1, 5),
    _CpqDaNw3xCorrReads_Type()
)
cpqDaNw3xCorrReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xCorrReads.setStatus("deprecated")
_CpqDaNw3xCorrWrites_Type = Counter32
_CpqDaNw3xCorrWrites_Object = MibTableColumn
cpqDaNw3xCorrWrites = _CpqDaNw3xCorrWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 5, 1, 6),
    _CpqDaNw3xCorrWrites_Type()
)
cpqDaNw3xCorrWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xCorrWrites.setStatus("deprecated")
_CpqDaNw3xFatalReads_Type = Counter32
_CpqDaNw3xFatalReads_Object = MibTableColumn
cpqDaNw3xFatalReads = _CpqDaNw3xFatalReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 5, 1, 7),
    _CpqDaNw3xFatalReads_Type()
)
cpqDaNw3xFatalReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xFatalReads.setStatus("deprecated")
_CpqDaNw3xFatalWrites_Type = Counter32
_CpqDaNw3xFatalWrites_Object = MibTableColumn
cpqDaNw3xFatalWrites = _CpqDaNw3xFatalWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 5, 1, 8),
    _CpqDaNw3xFatalWrites_Type()
)
cpqDaNw3xFatalWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xFatalWrites.setStatus("deprecated")
_CpqDaNw3xVolMapTable_Object = MibTable
cpqDaNw3xVolMapTable = _CpqDaNw3xVolMapTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cpqDaNw3xVolMapTable.setStatus("deprecated")
_CpqDaNw3xVolMapEntry_Object = MibTableRow
cpqDaNw3xVolMapEntry = _CpqDaNw3xVolMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 6, 1)
)
cpqDaNw3xVolMapEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaNw3xVolCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaNw3xVolLogDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqDaNw3xVolMapEntry.setStatus("deprecated")


class _CpqDaNw3xVolCntlrIndex_Type(Integer32):
    """Custom type cpqDaNw3xVolCntlrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaNw3xVolCntlrIndex_Type.__name__ = "Integer32"
_CpqDaNw3xVolCntlrIndex_Object = MibTableColumn
cpqDaNw3xVolCntlrIndex = _CpqDaNw3xVolCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 6, 1, 1),
    _CpqDaNw3xVolCntlrIndex_Type()
)
cpqDaNw3xVolCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xVolCntlrIndex.setStatus("deprecated")


class _CpqDaNw3xVolLogDrvIndex_Type(Integer32):
    """Custom type cpqDaNw3xVolLogDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaNw3xVolLogDrvIndex_Type.__name__ = "Integer32"
_CpqDaNw3xVolLogDrvIndex_Object = MibTableColumn
cpqDaNw3xVolLogDrvIndex = _CpqDaNw3xVolLogDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 6, 1, 2),
    _CpqDaNw3xVolLogDrvIndex_Type()
)
cpqDaNw3xVolLogDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xVolLogDrvIndex.setStatus("deprecated")


class _CpqDaNw3xVolMap_Type(OctetString):
    """Custom type cpqDaNw3xVolMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaNw3xVolMap_Type.__name__ = "OctetString"
_CpqDaNw3xVolMap_Object = MibTableColumn
cpqDaNw3xVolMap = _CpqDaNw3xVolMap_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 1, 6, 1, 3),
    _CpqDaNw3xVolMap_Type()
)
cpqDaNw3xVolMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaNw3xVolMap.setStatus("deprecated")
_CpqDaOsCommon_ObjectIdentity = ObjectIdentity
cpqDaOsCommon = _CpqDaOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 4)
)


class _CpqDaOsCommonPollFreq_Type(Integer32):
    """Custom type cpqDaOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqDaOsCommonPollFreq_Object = MibScalar
cpqDaOsCommonPollFreq = _CpqDaOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 4, 1),
    _CpqDaOsCommonPollFreq_Type()
)
cpqDaOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqDaOsCommonPollFreq.setStatus("mandatory")
_CpqDaOsCommonModuleTable_Object = MibTable
cpqDaOsCommonModuleTable = _CpqDaOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqDaOsCommonModuleTable.setStatus("deprecated")
_CpqDaOsCommonModuleEntry_Object = MibTableRow
cpqDaOsCommonModuleEntry = _CpqDaOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 4, 2, 1)
)
cpqDaOsCommonModuleEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqDaOsCommonModuleEntry.setStatus("deprecated")


class _CpqDaOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqDaOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqDaOsCommonModuleIndex_Object = MibTableColumn
cpqDaOsCommonModuleIndex = _CpqDaOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 4, 2, 1, 1),
    _CpqDaOsCommonModuleIndex_Type()
)
cpqDaOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaOsCommonModuleIndex.setStatus("deprecated")


class _CpqDaOsCommonModuleName_Type(DisplayString):
    """Custom type cpqDaOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqDaOsCommonModuleName_Object = MibTableColumn
cpqDaOsCommonModuleName = _CpqDaOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 4, 2, 1, 2),
    _CpqDaOsCommonModuleName_Type()
)
cpqDaOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaOsCommonModuleName.setStatus("deprecated")


class _CpqDaOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqDaOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqDaOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqDaOsCommonModuleVersion_Object = MibTableColumn
cpqDaOsCommonModuleVersion = _CpqDaOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 4, 2, 1, 3),
    _CpqDaOsCommonModuleVersion_Type()
)
cpqDaOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaOsCommonModuleVersion.setStatus("deprecated")


class _CpqDaOsCommonModuleDate_Type(OctetString):
    """Custom type cpqDaOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqDaOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqDaOsCommonModuleDate_Object = MibTableColumn
cpqDaOsCommonModuleDate = _CpqDaOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 4, 2, 1, 4),
    _CpqDaOsCommonModuleDate_Type()
)
cpqDaOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaOsCommonModuleDate.setStatus("deprecated")


class _CpqDaOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqDaOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqDaOsCommonModulePurpose_Object = MibTableColumn
cpqDaOsCommonModulePurpose = _CpqDaOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 4, 2, 1, 5),
    _CpqDaOsCommonModulePurpose_Type()
)
cpqDaOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaOsCommonModulePurpose.setStatus("deprecated")


class _CpqDaOsCommonCollectionReset_Type(Integer32):
    """Custom type cpqDaOsCommonCollectionReset based on Integer32"""
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
        *(("doReset", 4),
          ("other", 1),
          ("resetNotSupported", 3),
          ("resetSupported", 2))
    )


_CpqDaOsCommonCollectionReset_Type.__name__ = "Integer32"
_CpqDaOsCommonCollectionReset_Object = MibScalar
cpqDaOsCommonCollectionReset = _CpqDaOsCommonCollectionReset_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 1, 4, 3),
    _CpqDaOsCommonCollectionReset_Type()
)
cpqDaOsCommonCollectionReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqDaOsCommonCollectionReset.setStatus("optional")
_CpqDaCntlr_ObjectIdentity = ObjectIdentity
cpqDaCntlr = _CpqDaCntlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2)
)
_CpqDaCntlrTable_Object = MibTable
cpqDaCntlrTable = _CpqDaCntlrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqDaCntlrTable.setStatus("mandatory")
_CpqDaCntlrEntry_Object = MibTableRow
cpqDaCntlrEntry = _CpqDaCntlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1)
)
cpqDaCntlrEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaCntlrIndex"),
)
if mibBuilder.loadTexts:
    cpqDaCntlrEntry.setStatus("mandatory")
_CpqDaCntlrIndex_Type = Integer32
_CpqDaCntlrIndex_Object = MibTableColumn
cpqDaCntlrIndex = _CpqDaCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 1),
    _CpqDaCntlrIndex_Type()
)
cpqDaCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrIndex.setStatus("mandatory")


class _CpqDaCntlrModel_Type(Integer32):
    """Custom type cpqDaCntlrModel based on Integer32"""
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
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69)
        )
    )
    namedValues = NamedValues(
        *(("hps-1224", 55),
          ("hps-1224e", 59),
          ("hps-1228", 56),
          ("hps-1228e", 60),
          ("hps-1228em", 61),
          ("hps-1228m", 57),
          ("ida", 2),
          ("ida-2", 4),
          ("idaExpansion", 3),
          ("other", 1),
          ("raidLc2", 18),
          ("sa-4200", 14),
          ("sa-4250es", 13),
          ("sa-431", 16),
          ("sa-5300", 17),
          ("sa-5312", 21),
          ("sa-532", 20),
          ("sa-5i", 19),
          ("sa-6400", 24),
          ("sa-6400em", 25),
          ("sa-641", 22),
          ("sa-642", 23),
          ("sa-6i", 26),
          ("sa-b110i", 41),
          ("sa-b120i", 54),
          ("sa-b320i", 51),
          ("sa-e200", 31),
          ("sa-e200i", 32),
          ("sa-e500", 35),
          ("sa-generic", 27),
          ("sa-integrated", 15),
          ("sa-p212", 37),
          ("sa-p220i", 46),
          ("sa-p222", 47),
          ("sa-p230i", 62),
          ("sa-p400", 30),
          ("sa-p400i", 33),
          ("sa-p410", 38),
          ("sa-p410i", 39),
          ("sa-p411", 40),
          ("sa-p420", 48),
          ("sa-p420i", 49),
          ("sa-p421", 50),
          ("sa-p430", 64),
          ("sa-p430i", 63),
          ("sa-p431", 65),
          ("sa-p600", 29),
          ("sa-p700m", 36),
          ("sa-p711m", 43),
          ("sa-p712m", 42),
          ("sa-p721m", 53),
          ("sa-p731m", 66),
          ("sa-p800", 34),
          ("sa-p812", 44),
          ("sa-p822", 52),
          ("sa-p822se", 58),
          ("sa-p830", 68),
          ("sa-p830i", 67),
          ("sa-p831", 69),
          ("smart", 5),
          ("smart-221", 12),
          ("smart-2dh", 11),
          ("smart-2e", 6),
          ("smart-2p", 7),
          ("smart-2sl", 8),
          ("smart-3100es", 9),
          ("smart-3200", 10),
          ("sw-1210m", 45))
    )


_CpqDaCntlrModel_Type.__name__ = "Integer32"
_CpqDaCntlrModel_Object = MibTableColumn
cpqDaCntlrModel = _CpqDaCntlrModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 2),
    _CpqDaCntlrModel_Type()
)
cpqDaCntlrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrModel.setStatus("mandatory")


class _CpqDaCntlrFWRev_Type(DisplayString):
    """Custom type cpqDaCntlrFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqDaCntlrFWRev_Type.__name__ = "DisplayString"
_CpqDaCntlrFWRev_Object = MibTableColumn
cpqDaCntlrFWRev = _CpqDaCntlrFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 3),
    _CpqDaCntlrFWRev_Type()
)
cpqDaCntlrFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrFWRev.setStatus("mandatory")


class _CpqDaCntlrStndIntr_Type(Integer32):
    """Custom type cpqDaCntlrStndIntr based on Integer32"""
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
        *(("disabled", 4),
          ("other", 1),
          ("primary", 2),
          ("secondary", 3),
          ("unavailable", 5))
    )


_CpqDaCntlrStndIntr_Type.__name__ = "Integer32"
_CpqDaCntlrStndIntr_Object = MibTableColumn
cpqDaCntlrStndIntr = _CpqDaCntlrStndIntr_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 4),
    _CpqDaCntlrStndIntr_Type()
)
cpqDaCntlrStndIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrStndIntr.setStatus("mandatory")


class _CpqDaCntlrSlot_Type(Integer32):
    """Custom type cpqDaCntlrSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaCntlrSlot_Type.__name__ = "Integer32"
_CpqDaCntlrSlot_Object = MibTableColumn
cpqDaCntlrSlot = _CpqDaCntlrSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 5),
    _CpqDaCntlrSlot_Type()
)
cpqDaCntlrSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrSlot.setStatus("mandatory")


class _CpqDaCntlrCondition_Type(Integer32):
    """Custom type cpqDaCntlrCondition based on Integer32"""
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


_CpqDaCntlrCondition_Type.__name__ = "Integer32"
_CpqDaCntlrCondition_Object = MibTableColumn
cpqDaCntlrCondition = _CpqDaCntlrCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 6),
    _CpqDaCntlrCondition_Type()
)
cpqDaCntlrCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrCondition.setStatus("mandatory")


class _CpqDaCntlrProductRev_Type(DisplayString):
    """Custom type cpqDaCntlrProductRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_CpqDaCntlrProductRev_Type.__name__ = "DisplayString"
_CpqDaCntlrProductRev_Object = MibTableColumn
cpqDaCntlrProductRev = _CpqDaCntlrProductRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 7),
    _CpqDaCntlrProductRev_Type()
)
cpqDaCntlrProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrProductRev.setStatus("mandatory")
_CpqDaCntlrPartnerSlot_Type = Integer32
_CpqDaCntlrPartnerSlot_Object = MibTableColumn
cpqDaCntlrPartnerSlot = _CpqDaCntlrPartnerSlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 8),
    _CpqDaCntlrPartnerSlot_Type()
)
cpqDaCntlrPartnerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPartnerSlot.setStatus("mandatory")


class _CpqDaCntlrCurrentRole_Type(Integer32):
    """Custom type cpqDaCntlrCurrentRole based on Integer32"""
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
        *(("active", 3),
          ("asymActiveActive", 5),
          ("backup", 4),
          ("notDuplexed", 2),
          ("other", 1))
    )


_CpqDaCntlrCurrentRole_Type.__name__ = "Integer32"
_CpqDaCntlrCurrentRole_Object = MibTableColumn
cpqDaCntlrCurrentRole = _CpqDaCntlrCurrentRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 9),
    _CpqDaCntlrCurrentRole_Type()
)
cpqDaCntlrCurrentRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrCurrentRole.setStatus("mandatory")


class _CpqDaCntlrBoardStatus_Type(Integer32):
    """Custom type cpqDaCntlrBoardStatus based on Integer32"""
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
        *(("cableProblem", 4),
          ("cacheModuleMissing", 6),
          ("generalFailure", 3),
          ("ok", 2),
          ("other", 1),
          ("poweredOff", 5))
    )


_CpqDaCntlrBoardStatus_Type.__name__ = "Integer32"
_CpqDaCntlrBoardStatus_Object = MibTableColumn
cpqDaCntlrBoardStatus = _CpqDaCntlrBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 10),
    _CpqDaCntlrBoardStatus_Type()
)
cpqDaCntlrBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrBoardStatus.setStatus("mandatory")


class _CpqDaCntlrPartnerBoardStatus_Type(Integer32):
    """Custom type cpqDaCntlrPartnerBoardStatus based on Integer32"""
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
        *(("cableProblem", 4),
          ("generalFailure", 3),
          ("ok", 2),
          ("other", 1),
          ("poweredOff", 5))
    )


_CpqDaCntlrPartnerBoardStatus_Type.__name__ = "Integer32"
_CpqDaCntlrPartnerBoardStatus_Object = MibTableColumn
cpqDaCntlrPartnerBoardStatus = _CpqDaCntlrPartnerBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 11),
    _CpqDaCntlrPartnerBoardStatus_Type()
)
cpqDaCntlrPartnerBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPartnerBoardStatus.setStatus("mandatory")


class _CpqDaCntlrBoardCondition_Type(Integer32):
    """Custom type cpqDaCntlrBoardCondition based on Integer32"""
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


_CpqDaCntlrBoardCondition_Type.__name__ = "Integer32"
_CpqDaCntlrBoardCondition_Object = MibTableColumn
cpqDaCntlrBoardCondition = _CpqDaCntlrBoardCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 12),
    _CpqDaCntlrBoardCondition_Type()
)
cpqDaCntlrBoardCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrBoardCondition.setStatus("mandatory")


class _CpqDaCntlrPartnerBoardCondition_Type(Integer32):
    """Custom type cpqDaCntlrPartnerBoardCondition based on Integer32"""
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


_CpqDaCntlrPartnerBoardCondition_Type.__name__ = "Integer32"
_CpqDaCntlrPartnerBoardCondition_Object = MibTableColumn
cpqDaCntlrPartnerBoardCondition = _CpqDaCntlrPartnerBoardCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 13),
    _CpqDaCntlrPartnerBoardCondition_Type()
)
cpqDaCntlrPartnerBoardCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPartnerBoardCondition.setStatus("mandatory")


class _CpqDaCntlrDriveOwnership_Type(Integer32):
    """Custom type cpqDaCntlrDriveOwnership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOwner", 3),
          ("other", 1),
          ("owner", 2))
    )


_CpqDaCntlrDriveOwnership_Type.__name__ = "Integer32"
_CpqDaCntlrDriveOwnership_Object = MibTableColumn
cpqDaCntlrDriveOwnership = _CpqDaCntlrDriveOwnership_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 14),
    _CpqDaCntlrDriveOwnership_Type()
)
cpqDaCntlrDriveOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrDriveOwnership.setStatus("mandatory")


class _CpqDaCntlrSerialNumber_Type(DisplayString):
    """Custom type cpqDaCntlrSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqDaCntlrSerialNumber_Type.__name__ = "DisplayString"
_CpqDaCntlrSerialNumber_Object = MibTableColumn
cpqDaCntlrSerialNumber = _CpqDaCntlrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 15),
    _CpqDaCntlrSerialNumber_Type()
)
cpqDaCntlrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrSerialNumber.setStatus("mandatory")


class _CpqDaCntlrRedundancyType_Type(Integer32):
    """Custom type cpqDaCntlrRedundancyType based on Integer32"""
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
        *(("driverDuplexing", 3),
          ("fwActiveActive", 6),
          ("fwActiveStandby", 4),
          ("fwPrimarySecondary", 5),
          ("notRedundant", 2),
          ("other", 1))
    )


_CpqDaCntlrRedundancyType_Type.__name__ = "Integer32"
_CpqDaCntlrRedundancyType_Object = MibTableColumn
cpqDaCntlrRedundancyType = _CpqDaCntlrRedundancyType_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 16),
    _CpqDaCntlrRedundancyType_Type()
)
cpqDaCntlrRedundancyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrRedundancyType.setStatus("mandatory")


class _CpqDaCntlrRedundancyError_Type(Integer32):
    """Custom type cpqDaCntlrRedundancyError based on Integer32"""
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


_CpqDaCntlrRedundancyError_Type.__name__ = "Integer32"
_CpqDaCntlrRedundancyError_Object = MibTableColumn
cpqDaCntlrRedundancyError = _CpqDaCntlrRedundancyError_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 17),
    _CpqDaCntlrRedundancyError_Type()
)
cpqDaCntlrRedundancyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrRedundancyError.setStatus("mandatory")


class _CpqDaCntlrAccessModuleStatus_Type(Integer32):
    """Custom type cpqDaCntlrAccessModuleStatus based on Integer32"""
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
        *(("badChecksum", 5),
          ("badSignature", 4),
          ("fullyFunctional", 6),
          ("notPresent", 3),
          ("notSupported", 2),
          ("other", 1),
          ("upgradeFirmware", 7))
    )


_CpqDaCntlrAccessModuleStatus_Type.__name__ = "Integer32"
_CpqDaCntlrAccessModuleStatus_Object = MibTableColumn
cpqDaCntlrAccessModuleStatus = _CpqDaCntlrAccessModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 18),
    _CpqDaCntlrAccessModuleStatus_Type()
)
cpqDaCntlrAccessModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrAccessModuleStatus.setStatus("mandatory")


class _CpqDaCntlrDaughterBoardType_Type(Integer32):
    """Custom type cpqDaCntlrDaughterBoardType based on Integer32"""
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
        *(("arrayExpansionModulePresent", 6),
          ("fibreBoardPresent", 5),
          ("notPresent", 3),
          ("notSupported", 2),
          ("other", 1),
          ("scsiBoardPresent", 4))
    )


_CpqDaCntlrDaughterBoardType_Type.__name__ = "Integer32"
_CpqDaCntlrDaughterBoardType_Object = MibTableColumn
cpqDaCntlrDaughterBoardType = _CpqDaCntlrDaughterBoardType_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 19),
    _CpqDaCntlrDaughterBoardType_Type()
)
cpqDaCntlrDaughterBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrDaughterBoardType.setStatus("mandatory")


class _CpqDaCntlrHwLocation_Type(DisplayString):
    """Custom type cpqDaCntlrHwLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaCntlrHwLocation_Type.__name__ = "DisplayString"
_CpqDaCntlrHwLocation_Object = MibTableColumn
cpqDaCntlrHwLocation = _CpqDaCntlrHwLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 20),
    _CpqDaCntlrHwLocation_Type()
)
cpqDaCntlrHwLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrHwLocation.setStatus("mandatory")
_CpqDaCntlrNumberOfBuses_Type = Integer32
_CpqDaCntlrNumberOfBuses_Object = MibTableColumn
cpqDaCntlrNumberOfBuses = _CpqDaCntlrNumberOfBuses_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 21),
    _CpqDaCntlrNumberOfBuses_Type()
)
cpqDaCntlrNumberOfBuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrNumberOfBuses.setStatus("mandatory")
_CpqDaCntlrBlinkTime_Type = Counter32
_CpqDaCntlrBlinkTime_Object = MibTableColumn
cpqDaCntlrBlinkTime = _CpqDaCntlrBlinkTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 22),
    _CpqDaCntlrBlinkTime_Type()
)
cpqDaCntlrBlinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqDaCntlrBlinkTime.setStatus("mandatory")


class _CpqDaCntlrRebuildPriority_Type(Integer32):
    """Custom type cpqDaCntlrRebuildPriority based on Integer32"""
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


_CpqDaCntlrRebuildPriority_Type.__name__ = "Integer32"
_CpqDaCntlrRebuildPriority_Object = MibTableColumn
cpqDaCntlrRebuildPriority = _CpqDaCntlrRebuildPriority_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 23),
    _CpqDaCntlrRebuildPriority_Type()
)
cpqDaCntlrRebuildPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrRebuildPriority.setStatus("mandatory")


class _CpqDaCntlrExpandPriority_Type(Integer32):
    """Custom type cpqDaCntlrExpandPriority based on Integer32"""
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


_CpqDaCntlrExpandPriority_Type.__name__ = "Integer32"
_CpqDaCntlrExpandPriority_Object = MibTableColumn
cpqDaCntlrExpandPriority = _CpqDaCntlrExpandPriority_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 24),
    _CpqDaCntlrExpandPriority_Type()
)
cpqDaCntlrExpandPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrExpandPriority.setStatus("mandatory")
_CpqDaCntlrNumberOfInternalPorts_Type = Integer32
_CpqDaCntlrNumberOfInternalPorts_Object = MibTableColumn
cpqDaCntlrNumberOfInternalPorts = _CpqDaCntlrNumberOfInternalPorts_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 25),
    _CpqDaCntlrNumberOfInternalPorts_Type()
)
cpqDaCntlrNumberOfInternalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrNumberOfInternalPorts.setStatus("mandatory")
_CpqDaCntlrNumberOfExternalPorts_Type = Integer32
_CpqDaCntlrNumberOfExternalPorts_Object = MibTableColumn
cpqDaCntlrNumberOfExternalPorts = _CpqDaCntlrNumberOfExternalPorts_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 26),
    _CpqDaCntlrNumberOfExternalPorts_Type()
)
cpqDaCntlrNumberOfExternalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrNumberOfExternalPorts.setStatus("mandatory")


class _CpqDaCntlrDriveWriteCacheState_Type(Integer32):
    """Custom type cpqDaCntlrDriveWriteCacheState based on Integer32"""
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


_CpqDaCntlrDriveWriteCacheState_Type.__name__ = "Integer32"
_CpqDaCntlrDriveWriteCacheState_Object = MibTableColumn
cpqDaCntlrDriveWriteCacheState = _CpqDaCntlrDriveWriteCacheState_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 27),
    _CpqDaCntlrDriveWriteCacheState_Type()
)
cpqDaCntlrDriveWriteCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrDriveWriteCacheState.setStatus("mandatory")


class _CpqDaCntlrPartnerSerialNumber_Type(DisplayString):
    """Custom type cpqDaCntlrPartnerSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqDaCntlrPartnerSerialNumber_Type.__name__ = "DisplayString"
_CpqDaCntlrPartnerSerialNumber_Object = MibTableColumn
cpqDaCntlrPartnerSerialNumber = _CpqDaCntlrPartnerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 28),
    _CpqDaCntlrPartnerSerialNumber_Type()
)
cpqDaCntlrPartnerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPartnerSerialNumber.setStatus("mandatory")


class _CpqDaCntlrOptionRomRev_Type(DisplayString):
    """Custom type cpqDaCntlrOptionRomRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqDaCntlrOptionRomRev_Type.__name__ = "DisplayString"
_CpqDaCntlrOptionRomRev_Object = MibTableColumn
cpqDaCntlrOptionRomRev = _CpqDaCntlrOptionRomRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 29),
    _CpqDaCntlrOptionRomRev_Type()
)
cpqDaCntlrOptionRomRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrOptionRomRev.setStatus("mandatory")


class _CpqDaCntlrHbaFWRev_Type(DisplayString):
    """Custom type cpqDaCntlrHbaFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CpqDaCntlrHbaFWRev_Type.__name__ = "DisplayString"
_CpqDaCntlrHbaFWRev_Object = MibTableColumn
cpqDaCntlrHbaFWRev = _CpqDaCntlrHbaFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 30),
    _CpqDaCntlrHbaFWRev_Type()
)
cpqDaCntlrHbaFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrHbaFWRev.setStatus("mandatory")


class _CpqDaCntlrHBAModeOptionRomRev_Type(DisplayString):
    """Custom type cpqDaCntlrHBAModeOptionRomRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CpqDaCntlrHBAModeOptionRomRev_Type.__name__ = "DisplayString"
_CpqDaCntlrHBAModeOptionRomRev_Object = MibTableColumn
cpqDaCntlrHBAModeOptionRomRev = _CpqDaCntlrHBAModeOptionRomRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 31),
    _CpqDaCntlrHBAModeOptionRomRev_Type()
)
cpqDaCntlrHBAModeOptionRomRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrHBAModeOptionRomRev.setStatus("mandatory")
_CpqDaCntlrCurrentTemp_Type = Integer32
_CpqDaCntlrCurrentTemp_Object = MibTableColumn
cpqDaCntlrCurrentTemp = _CpqDaCntlrCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 32),
    _CpqDaCntlrCurrentTemp_Type()
)
cpqDaCntlrCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrCurrentTemp.setStatus("mandatory")
_CpqDaCntlrLastLockupCode_Type = Integer32
_CpqDaCntlrLastLockupCode_Object = MibTableColumn
cpqDaCntlrLastLockupCode = _CpqDaCntlrLastLockupCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 33),
    _CpqDaCntlrLastLockupCode_Type()
)
cpqDaCntlrLastLockupCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrLastLockupCode.setStatus("mandatory")


class _CpqDaCntlrEncryptionStatus_Type(Integer32):
    """Custom type cpqDaCntlrEncryptionStatus based on Integer32"""
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
        *(("enabledLocalKeyMode", 3),
          ("enabledRemoteKeyManagerMode", 4),
          ("notEnabled", 2),
          ("other", 1))
    )


_CpqDaCntlrEncryptionStatus_Type.__name__ = "Integer32"
_CpqDaCntlrEncryptionStatus_Object = MibTableColumn
cpqDaCntlrEncryptionStatus = _CpqDaCntlrEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 34),
    _CpqDaCntlrEncryptionStatus_Type()
)
cpqDaCntlrEncryptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrEncryptionStatus.setStatus("mandatory")


class _CpqDaCntlrASICEncptSelfTestStatus_Type(Integer32):
    """Custom type cpqDaCntlrASICEncptSelfTestStatus based on Integer32"""
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
          ("selfTestsFailed", 3),
          ("selfTestsPass", 2))
    )


_CpqDaCntlrASICEncptSelfTestStatus_Type.__name__ = "Integer32"
_CpqDaCntlrASICEncptSelfTestStatus_Object = MibTableColumn
cpqDaCntlrASICEncptSelfTestStatus = _CpqDaCntlrASICEncptSelfTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 35),
    _CpqDaCntlrASICEncptSelfTestStatus_Type()
)
cpqDaCntlrASICEncptSelfTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrASICEncptSelfTestStatus.setStatus("mandatory")


class _CpqDaCntlrEncryptCspNvramStatus_Type(Integer32):
    """Custom type cpqDaCntlrEncryptCspNvramStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detectionFailed", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqDaCntlrEncryptCspNvramStatus_Type.__name__ = "Integer32"
_CpqDaCntlrEncryptCspNvramStatus_Object = MibTableColumn
cpqDaCntlrEncryptCspNvramStatus = _CpqDaCntlrEncryptCspNvramStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 36),
    _CpqDaCntlrEncryptCspNvramStatus_Type()
)
cpqDaCntlrEncryptCspNvramStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrEncryptCspNvramStatus.setStatus("mandatory")


class _CpqDaCntlrEncryptCryptoOfficerPwdSetStatus_Type(Integer32):
    """Custom type cpqDaCntlrEncryptCryptoOfficerPwdSetStatus based on Integer32"""
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
          ("other", 1),
          ("true", 3))
    )


_CpqDaCntlrEncryptCryptoOfficerPwdSetStatus_Type.__name__ = "Integer32"
_CpqDaCntlrEncryptCryptoOfficerPwdSetStatus_Object = MibTableColumn
cpqDaCntlrEncryptCryptoOfficerPwdSetStatus = _CpqDaCntlrEncryptCryptoOfficerPwdSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 37),
    _CpqDaCntlrEncryptCryptoOfficerPwdSetStatus_Type()
)
cpqDaCntlrEncryptCryptoOfficerPwdSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrEncryptCryptoOfficerPwdSetStatus.setStatus("mandatory")


class _CpqDaCntlrEncryptCntlrPwdSetStatus_Type(Integer32):
    """Custom type cpqDaCntlrEncryptCntlrPwdSetStatus based on Integer32"""
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
          ("other", 1),
          ("true", 3))
    )


_CpqDaCntlrEncryptCntlrPwdSetStatus_Type.__name__ = "Integer32"
_CpqDaCntlrEncryptCntlrPwdSetStatus_Object = MibTableColumn
cpqDaCntlrEncryptCntlrPwdSetStatus = _CpqDaCntlrEncryptCntlrPwdSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 38),
    _CpqDaCntlrEncryptCntlrPwdSetStatus_Type()
)
cpqDaCntlrEncryptCntlrPwdSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrEncryptCntlrPwdSetStatus.setStatus("mandatory")


class _CpqDaCntlrEncryptCntlrPwdAvailStatus_Type(Integer32):
    """Custom type cpqDaCntlrEncryptCntlrPwdAvailStatus based on Integer32"""
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
          ("passwordActive", 3),
          ("passwordMissing", 2))
    )


_CpqDaCntlrEncryptCntlrPwdAvailStatus_Type.__name__ = "Integer32"
_CpqDaCntlrEncryptCntlrPwdAvailStatus_Object = MibTableColumn
cpqDaCntlrEncryptCntlrPwdAvailStatus = _CpqDaCntlrEncryptCntlrPwdAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 39),
    _CpqDaCntlrEncryptCntlrPwdAvailStatus_Type()
)
cpqDaCntlrEncryptCntlrPwdAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrEncryptCntlrPwdAvailStatus.setStatus("mandatory")


class _CpqDaCntlrUnencryptedLogDrvCreationPolicy_Type(Integer32):
    """Custom type cpqDaCntlrUnencryptedLogDrvCreationPolicy based on Integer32"""
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
          ("other", 1),
          ("true", 3))
    )


_CpqDaCntlrUnencryptedLogDrvCreationPolicy_Type.__name__ = "Integer32"
_CpqDaCntlrUnencryptedLogDrvCreationPolicy_Object = MibTableColumn
cpqDaCntlrUnencryptedLogDrvCreationPolicy = _CpqDaCntlrUnencryptedLogDrvCreationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 40),
    _CpqDaCntlrUnencryptedLogDrvCreationPolicy_Type()
)
cpqDaCntlrUnencryptedLogDrvCreationPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrUnencryptedLogDrvCreationPolicy.setStatus("mandatory")


class _CpqDaCntlrEncryptedLogDrvCreationPolicy_Type(Integer32):
    """Custom type cpqDaCntlrEncryptedLogDrvCreationPolicy based on Integer32"""
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
          ("other", 1),
          ("true", 3))
    )


_CpqDaCntlrEncryptedLogDrvCreationPolicy_Type.__name__ = "Integer32"
_CpqDaCntlrEncryptedLogDrvCreationPolicy_Object = MibTableColumn
cpqDaCntlrEncryptedLogDrvCreationPolicy = _CpqDaCntlrEncryptedLogDrvCreationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 41),
    _CpqDaCntlrEncryptedLogDrvCreationPolicy_Type()
)
cpqDaCntlrEncryptedLogDrvCreationPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrEncryptedLogDrvCreationPolicy.setStatus("mandatory")


class _CpqDaCntlrEncryptFWLockStatus_Type(Integer32):
    """Custom type cpqDaCntlrEncryptFWLockStatus based on Integer32"""
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
          ("other", 1),
          ("true", 3))
    )


_CpqDaCntlrEncryptFWLockStatus_Type.__name__ = "Integer32"
_CpqDaCntlrEncryptFWLockStatus_Object = MibTableColumn
cpqDaCntlrEncryptFWLockStatus = _CpqDaCntlrEncryptFWLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 1, 1, 42),
    _CpqDaCntlrEncryptFWLockStatus_Type()
)
cpqDaCntlrEncryptFWLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrEncryptFWLockStatus.setStatus("mandatory")
_CpqDaAccelTable_Object = MibTable
cpqDaAccelTable = _CpqDaAccelTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cpqDaAccelTable.setStatus("mandatory")
_CpqDaAccelEntry_Object = MibTableRow
cpqDaAccelEntry = _CpqDaAccelEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1)
)
cpqDaAccelEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaAccelCntlrIndex"),
)
if mibBuilder.loadTexts:
    cpqDaAccelEntry.setStatus("mandatory")
_CpqDaAccelCntlrIndex_Type = Integer32
_CpqDaAccelCntlrIndex_Object = MibTableColumn
cpqDaAccelCntlrIndex = _CpqDaAccelCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 1),
    _CpqDaAccelCntlrIndex_Type()
)
cpqDaAccelCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelCntlrIndex.setStatus("mandatory")


class _CpqDaAccelStatus_Type(Integer32):
    """Custom type cpqDaAccelStatus based on Integer32"""
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
        *(("cacheModCriticalFailure", 8),
          ("cacheModDegradedFailsafeSpeed", 7),
          ("cacheModFlashMemNotAttached", 6),
          ("cacheReadCacheNotMapped", 9),
          ("enabled", 3),
          ("invalid", 2),
          ("other", 1),
          ("permDisabled", 5),
          ("tmpDisabled", 4))
    )


_CpqDaAccelStatus_Type.__name__ = "Integer32"
_CpqDaAccelStatus_Object = MibTableColumn
cpqDaAccelStatus = _CpqDaAccelStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 2),
    _CpqDaAccelStatus_Type()
)
cpqDaAccelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelStatus.setStatus("mandatory")
_CpqDaAccelMemory_Type = Integer32
_CpqDaAccelMemory_Object = MibTableColumn
cpqDaAccelMemory = _CpqDaAccelMemory_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 3),
    _CpqDaAccelMemory_Type()
)
cpqDaAccelMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelMemory.setStatus("mandatory")


class _CpqDaAccelBadData_Type(Integer32):
    """Custom type cpqDaAccelBadData based on Integer32"""
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


_CpqDaAccelBadData_Type.__name__ = "Integer32"
_CpqDaAccelBadData_Object = MibTableColumn
cpqDaAccelBadData = _CpqDaAccelBadData_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 4),
    _CpqDaAccelBadData_Type()
)
cpqDaAccelBadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelBadData.setStatus("mandatory")


class _CpqDaAccelErrCode_Type(Integer32):
    """Custom type cpqDaAccelErrCode based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("adgEnablerMissing", 18),
          ("badConfig", 3),
          ("badMirrorData", 8),
          ("batteryHotRemoved", 20),
          ("batteryNotSupported", 24),
          ("cacheModuleNotSupported", 23),
          ("capBasedBackupFailed", 26),
          ("capBasedModuleHWFailure", 28),
          ("capBasedRestoreFailed", 27),
          ("capacitorBasedHWMemBeingErased", 30),
          ("capacitorChargeLow", 21),
          ("capacitorFailedToCharge", 29),
          ("configCmd", 11),
          ("disableCmd", 5),
          ("excessiveEccErrors", 17),
          ("expandInProgress", 12),
          ("fbcmChargerCircuitFailure", 32),
          ("incompatibleCacheModule", 31),
          ("invalid", 2),
          ("lowBattery", 4),
          ("noCapacitorAttached", 25),
          ("noResources", 6),
          ("notConnected", 7),
          ("notEnoughBatteries", 22),
          ("other", 1),
          ("postEccErrors", 19),
          ("readErr", 9),
          ("redundantCacheFailure", 16),
          ("redundantLowBattery", 14),
          ("redundantSizeMismatch", 15),
          ("snapshotInProgress", 13),
          ("writeErr", 10))
    )


_CpqDaAccelErrCode_Type.__name__ = "Integer32"
_CpqDaAccelErrCode_Object = MibTableColumn
cpqDaAccelErrCode = _CpqDaAccelErrCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 5),
    _CpqDaAccelErrCode_Type()
)
cpqDaAccelErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelErrCode.setStatus("mandatory")


class _CpqDaAccelBattery_Type(Integer32):
    """Custom type cpqDaAccelBattery based on Integer32"""
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
        *(("capacitorFailed", 7),
          ("degraded", 5),
          ("failed", 4),
          ("notPresent", 6),
          ("ok", 2),
          ("other", 1),
          ("recharging", 3))
    )


_CpqDaAccelBattery_Type.__name__ = "Integer32"
_CpqDaAccelBattery_Object = MibTableColumn
cpqDaAccelBattery = _CpqDaAccelBattery_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 6),
    _CpqDaAccelBattery_Type()
)
cpqDaAccelBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelBattery.setStatus("mandatory")
_CpqDaAccelReadErrs_Type = Counter32
_CpqDaAccelReadErrs_Object = MibTableColumn
cpqDaAccelReadErrs = _CpqDaAccelReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 7),
    _CpqDaAccelReadErrs_Type()
)
cpqDaAccelReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelReadErrs.setStatus("mandatory")
_CpqDaAccelWriteErrs_Type = Counter32
_CpqDaAccelWriteErrs_Object = MibTableColumn
cpqDaAccelWriteErrs = _CpqDaAccelWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 8),
    _CpqDaAccelWriteErrs_Type()
)
cpqDaAccelWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelWriteErrs.setStatus("mandatory")


class _CpqDaAccelCondition_Type(Integer32):
    """Custom type cpqDaAccelCondition based on Integer32"""
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


_CpqDaAccelCondition_Type.__name__ = "Integer32"
_CpqDaAccelCondition_Object = MibTableColumn
cpqDaAccelCondition = _CpqDaAccelCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 9),
    _CpqDaAccelCondition_Type()
)
cpqDaAccelCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelCondition.setStatus("mandatory")
_CpqDaAccelReadMemory_Type = Integer32
_CpqDaAccelReadMemory_Object = MibTableColumn
cpqDaAccelReadMemory = _CpqDaAccelReadMemory_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 10),
    _CpqDaAccelReadMemory_Type()
)
cpqDaAccelReadMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelReadMemory.setStatus("mandatory")


class _CpqDaAccelSerialNumber_Type(DisplayString):
    """Custom type cpqDaAccelSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpqDaAccelSerialNumber_Type.__name__ = "DisplayString"
_CpqDaAccelSerialNumber_Object = MibTableColumn
cpqDaAccelSerialNumber = _CpqDaAccelSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 11),
    _CpqDaAccelSerialNumber_Type()
)
cpqDaAccelSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelSerialNumber.setStatus("mandatory")
_CpqDaAccelTotalMemory_Type = Integer32
_CpqDaAccelTotalMemory_Object = MibTableColumn
cpqDaAccelTotalMemory = _CpqDaAccelTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 12),
    _CpqDaAccelTotalMemory_Type()
)
cpqDaAccelTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelTotalMemory.setStatus("mandatory")
_CpqDaAccelReadCachePercent_Type = Gauge32
_CpqDaAccelReadCachePercent_Object = MibTableColumn
cpqDaAccelReadCachePercent = _CpqDaAccelReadCachePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 13),
    _CpqDaAccelReadCachePercent_Type()
)
cpqDaAccelReadCachePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelReadCachePercent.setStatus("mandatory")
_CpqDaAccelWriteCachePercent_Type = Gauge32
_CpqDaAccelWriteCachePercent_Object = MibTableColumn
cpqDaAccelWriteCachePercent = _CpqDaAccelWriteCachePercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 14),
    _CpqDaAccelWriteCachePercent_Type()
)
cpqDaAccelWriteCachePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelWriteCachePercent.setStatus("mandatory")


class _CpqDaAccelFailedBatteries_Type(OctetString):
    """Custom type cpqDaAccelFailedBatteries based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqDaAccelFailedBatteries_Type.__name__ = "OctetString"
_CpqDaAccelFailedBatteries_Object = MibTableColumn
cpqDaAccelFailedBatteries = _CpqDaAccelFailedBatteries_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 15),
    _CpqDaAccelFailedBatteries_Type()
)
cpqDaAccelFailedBatteries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelFailedBatteries.setStatus("mandatory")


class _CpqDaAccelBackupPowerSource_Type(Integer32):
    """Custom type cpqDaAccelBackupPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("battery", 2),
          ("capacitor", 3),
          ("other", 1))
    )


_CpqDaAccelBackupPowerSource_Type.__name__ = "Integer32"
_CpqDaAccelBackupPowerSource_Object = MibTableColumn
cpqDaAccelBackupPowerSource = _CpqDaAccelBackupPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 16),
    _CpqDaAccelBackupPowerSource_Type()
)
cpqDaAccelBackupPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelBackupPowerSource.setStatus("mandatory")
_CpqDaAccelBoardCurrentTemp_Type = Integer32
_CpqDaAccelBoardCurrentTemp_Object = MibTableColumn
cpqDaAccelBoardCurrentTemp = _CpqDaAccelBoardCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 17),
    _CpqDaAccelBoardCurrentTemp_Type()
)
cpqDaAccelBoardCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelBoardCurrentTemp.setStatus("mandatory")
_CpqDaAccelCapacitorCurrentTemp_Type = Integer32
_CpqDaAccelCapacitorCurrentTemp_Object = MibTableColumn
cpqDaAccelCapacitorCurrentTemp = _CpqDaAccelCapacitorCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 18),
    _CpqDaAccelCapacitorCurrentTemp_Type()
)
cpqDaAccelCapacitorCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelCapacitorCurrentTemp.setStatus("mandatory")
_CpqDaAccelMemoryDataWidth_Type = Integer32
_CpqDaAccelMemoryDataWidth_Object = MibTableColumn
cpqDaAccelMemoryDataWidth = _CpqDaAccelMemoryDataWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 19),
    _CpqDaAccelMemoryDataWidth_Type()
)
cpqDaAccelMemoryDataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelMemoryDataWidth.setStatus("mandatory")
_CpqDaAccelMemoryTransferRate_Type = Integer32
_CpqDaAccelMemoryTransferRate_Object = MibTableColumn
cpqDaAccelMemoryTransferRate = _CpqDaAccelMemoryTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 2, 1, 20),
    _CpqDaAccelMemoryTransferRate_Type()
)
cpqDaAccelMemoryTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaAccelMemoryTransferRate.setStatus("mandatory")
_CpqDaManagedCableTable_Object = MibTable
cpqDaManagedCableTable = _CpqDaManagedCableTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cpqDaManagedCableTable.setStatus("mandatory")
_CpqDaManagedCableEntry_Object = MibTableRow
cpqDaManagedCableEntry = _CpqDaManagedCableEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3, 1)
)
cpqDaManagedCableEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaManagedCableCntlrIndex"),
)
if mibBuilder.loadTexts:
    cpqDaManagedCableEntry.setStatus("mandatory")
_CpqDaManagedCableIndex_Type = Integer32
_CpqDaManagedCableIndex_Object = MibTableColumn
cpqDaManagedCableIndex = _CpqDaManagedCableIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3, 1, 1),
    _CpqDaManagedCableIndex_Type()
)
cpqDaManagedCableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaManagedCableIndex.setStatus("mandatory")
_CpqDaManagedCableCntlrIndex_Type = Integer32
_CpqDaManagedCableCntlrIndex_Object = MibTableColumn
cpqDaManagedCableCntlrIndex = _CpqDaManagedCableCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3, 1, 2),
    _CpqDaManagedCableCntlrIndex_Type()
)
cpqDaManagedCableCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaManagedCableCntlrIndex.setStatus("mandatory")


class _CpqDaManagedCableHostConnector_Type(DisplayString):
    """Custom type cpqDaManagedCableHostConnector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CpqDaManagedCableHostConnector_Type.__name__ = "DisplayString"
_CpqDaManagedCableHostConnector_Object = MibTableColumn
cpqDaManagedCableHostConnector = _CpqDaManagedCableHostConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3, 1, 3),
    _CpqDaManagedCableHostConnector_Type()
)
cpqDaManagedCableHostConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaManagedCableHostConnector.setStatus("mandatory")


class _CpqDaManagedCableStatus_Type(Integer32):
    """Custom type cpqDaManagedCableStatus based on Integer32"""
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
        *(("fatalFault", 4),
          ("nonFatalFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqDaManagedCableStatus_Type.__name__ = "Integer32"
_CpqDaManagedCableStatus_Object = MibTableColumn
cpqDaManagedCableStatus = _CpqDaManagedCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3, 1, 4),
    _CpqDaManagedCableStatus_Type()
)
cpqDaManagedCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaManagedCableStatus.setStatus("mandatory")


class _CpqDaManagedCableFaultCode_Type(Integer32):
    """Custom type cpqDaManagedCableFaultCode based on Integer32"""
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
        *(("cannotConfigureCable", 5),
          ("linkFault", 3),
          ("noComWithCableMgmtInterface", 4),
          ("none", 2),
          ("other", 1))
    )


_CpqDaManagedCableFaultCode_Type.__name__ = "Integer32"
_CpqDaManagedCableFaultCode_Object = MibTableColumn
cpqDaManagedCableFaultCode = _CpqDaManagedCableFaultCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3, 1, 5),
    _CpqDaManagedCableFaultCode_Type()
)
cpqDaManagedCableFaultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaManagedCableFaultCode.setStatus("mandatory")


class _CpqDaManagedCableVendorRevision_Type(DisplayString):
    """Custom type cpqDaManagedCableVendorRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_CpqDaManagedCableVendorRevision_Type.__name__ = "DisplayString"
_CpqDaManagedCableVendorRevision_Object = MibTableColumn
cpqDaManagedCableVendorRevision = _CpqDaManagedCableVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3, 1, 6),
    _CpqDaManagedCableVendorRevision_Type()
)
cpqDaManagedCableVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaManagedCableVendorRevision.setStatus("mandatory")


class _CpqDaManagedCableVendorSerialNumber_Type(DisplayString):
    """Custom type cpqDaManagedCableVendorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqDaManagedCableVendorSerialNumber_Type.__name__ = "DisplayString"
_CpqDaManagedCableVendorSerialNumber_Object = MibTableColumn
cpqDaManagedCableVendorSerialNumber = _CpqDaManagedCableVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3, 1, 7),
    _CpqDaManagedCableVendorSerialNumber_Type()
)
cpqDaManagedCableVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaManagedCableVendorSerialNumber.setStatus("mandatory")


class _CpqDaManagedCableVendorPartNumber_Type(DisplayString):
    """Custom type cpqDaManagedCableVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CpqDaManagedCableVendorPartNumber_Type.__name__ = "DisplayString"
_CpqDaManagedCableVendorPartNumber_Object = MibTableColumn
cpqDaManagedCableVendorPartNumber = _CpqDaManagedCableVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3, 1, 8),
    _CpqDaManagedCableVendorPartNumber_Type()
)
cpqDaManagedCableVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaManagedCableVendorPartNumber.setStatus("mandatory")
_CpqDaManagedCableLength_Type = Integer32
_CpqDaManagedCableLength_Object = MibTableColumn
cpqDaManagedCableLength = _CpqDaManagedCableLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 2, 3, 1, 9),
    _CpqDaManagedCableLength_Type()
)
cpqDaManagedCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaManagedCableLength.setStatus("mandatory")
_CpqDaLogDrv_ObjectIdentity = ObjectIdentity
cpqDaLogDrv = _CpqDaLogDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3)
)
_CpqDaLogDrvTable_Object = MibTable
cpqDaLogDrvTable = _CpqDaLogDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqDaLogDrvTable.setStatus("mandatory")
_CpqDaLogDrvEntry_Object = MibTableRow
cpqDaLogDrvEntry = _CpqDaLogDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1)
)
cpqDaLogDrvEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaLogDrvCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaLogDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqDaLogDrvEntry.setStatus("mandatory")
_CpqDaLogDrvCntlrIndex_Type = Integer32
_CpqDaLogDrvCntlrIndex_Object = MibTableColumn
cpqDaLogDrvCntlrIndex = _CpqDaLogDrvCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 1),
    _CpqDaLogDrvCntlrIndex_Type()
)
cpqDaLogDrvCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCntlrIndex.setStatus("mandatory")


class _CpqDaLogDrvIndex_Type(Integer32):
    """Custom type cpqDaLogDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaLogDrvIndex_Type.__name__ = "Integer32"
_CpqDaLogDrvIndex_Object = MibTableColumn
cpqDaLogDrvIndex = _CpqDaLogDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 2),
    _CpqDaLogDrvIndex_Type()
)
cpqDaLogDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvIndex.setStatus("mandatory")


class _CpqDaLogDrvFaultTol_Type(Integer32):
    """Custom type cpqDaLogDrvFaultTol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("advancedDataGuard", 7),
          ("dataGuard", 4),
          ("distribDataGuard", 5),
          ("mirroring", 3),
          ("none", 2),
          ("other", 1),
          ("raid10Adm", 11),
          ("raid1Adm", 10),
          ("raid50", 8),
          ("raid60", 9))
    )


_CpqDaLogDrvFaultTol_Type.__name__ = "Integer32"
_CpqDaLogDrvFaultTol_Object = MibTableColumn
cpqDaLogDrvFaultTol = _CpqDaLogDrvFaultTol_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 3),
    _CpqDaLogDrvFaultTol_Type()
)
cpqDaLogDrvFaultTol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvFaultTol.setStatus("mandatory")


class _CpqDaLogDrvStatus_Type(Integer32):
    """Custom type cpqDaLogDrvStatus based on Integer32"""
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
        *(("badConnect", 9),
          ("erasing", 16),
          ("expanding", 12),
          ("failed", 3),
          ("multipathAccessDegraded", 15),
          ("newLogDrvKeyRekeyInProgress", 22),
          ("newLogDrvKeyRekeyRequestReceived", 25),
          ("noAccessEncryptedCntlrEncryptnNotEnbld", 23),
          ("noAccessEncryptedNoCntlrKey", 20),
          ("notAvailable", 13),
          ("ok", 2),
          ("other", 1),
          ("overheating", 10),
          ("predictiveSpareRebuildReady", 17),
          ("queuedForExpansion", 14),
          ("rapidParityInitInProgress", 18),
          ("rapidParityInitPending", 19),
          ("readyForRebuild", 6),
          ("rebuilding", 7),
          ("recovering", 5),
          ("shutdown", 11),
          ("unconfigured", 4),
          ("unencryptedToEncryptedInProgress", 21),
          ("unencryptedToEncryptedNotStarted", 24),
          ("wrongDrive", 8))
    )


_CpqDaLogDrvStatus_Type.__name__ = "Integer32"
_CpqDaLogDrvStatus_Object = MibTableColumn
cpqDaLogDrvStatus = _CpqDaLogDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 4),
    _CpqDaLogDrvStatus_Type()
)
cpqDaLogDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvStatus.setStatus("mandatory")


class _CpqDaLogDrvAutoRel_Type(Integer32):
    """Custom type cpqDaLogDrvAutoRel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqDaLogDrvAutoRel_Type.__name__ = "Integer32"
_CpqDaLogDrvAutoRel_Object = MibTableColumn
cpqDaLogDrvAutoRel = _CpqDaLogDrvAutoRel_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 5),
    _CpqDaLogDrvAutoRel_Type()
)
cpqDaLogDrvAutoRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqDaLogDrvAutoRel.setStatus("mandatory")
_CpqDaLogDrvRebuildBlks_Type = Counter32
_CpqDaLogDrvRebuildBlks_Object = MibTableColumn
cpqDaLogDrvRebuildBlks = _CpqDaLogDrvRebuildBlks_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 6),
    _CpqDaLogDrvRebuildBlks_Type()
)
cpqDaLogDrvRebuildBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvRebuildBlks.setStatus("deprecated")


class _CpqDaLogDrvHasAccel_Type(Integer32):
    """Custom type cpqDaLogDrvHasAccel based on Integer32"""
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


_CpqDaLogDrvHasAccel_Type.__name__ = "Integer32"
_CpqDaLogDrvHasAccel_Object = MibTableColumn
cpqDaLogDrvHasAccel = _CpqDaLogDrvHasAccel_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 7),
    _CpqDaLogDrvHasAccel_Type()
)
cpqDaLogDrvHasAccel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvHasAccel.setStatus("mandatory")


class _CpqDaLogDrvAvailSpares_Type(OctetString):
    """Custom type cpqDaLogDrvAvailSpares based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaLogDrvAvailSpares_Type.__name__ = "OctetString"
_CpqDaLogDrvAvailSpares_Object = MibTableColumn
cpqDaLogDrvAvailSpares = _CpqDaLogDrvAvailSpares_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 8),
    _CpqDaLogDrvAvailSpares_Type()
)
cpqDaLogDrvAvailSpares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvAvailSpares.setStatus("deprecated")


class _CpqDaLogDrvSize_Type(Integer32):
    """Custom type cpqDaLogDrvSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqDaLogDrvSize_Type.__name__ = "Integer32"
_CpqDaLogDrvSize_Object = MibTableColumn
cpqDaLogDrvSize = _CpqDaLogDrvSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 9),
    _CpqDaLogDrvSize_Type()
)
cpqDaLogDrvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvSize.setStatus("mandatory")


class _CpqDaLogDrvPhyDrvIDs_Type(OctetString):
    """Custom type cpqDaLogDrvPhyDrvIDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaLogDrvPhyDrvIDs_Type.__name__ = "OctetString"
_CpqDaLogDrvPhyDrvIDs_Object = MibTableColumn
cpqDaLogDrvPhyDrvIDs = _CpqDaLogDrvPhyDrvIDs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 10),
    _CpqDaLogDrvPhyDrvIDs_Type()
)
cpqDaLogDrvPhyDrvIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPhyDrvIDs.setStatus("deprecated")


class _CpqDaLogDrvCondition_Type(Integer32):
    """Custom type cpqDaLogDrvCondition based on Integer32"""
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


_CpqDaLogDrvCondition_Type.__name__ = "Integer32"
_CpqDaLogDrvCondition_Object = MibTableColumn
cpqDaLogDrvCondition = _CpqDaLogDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 11),
    _CpqDaLogDrvCondition_Type()
)
cpqDaLogDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCondition.setStatus("mandatory")
_CpqDaLogDrvPercentRebuild_Type = Gauge32
_CpqDaLogDrvPercentRebuild_Object = MibTableColumn
cpqDaLogDrvPercentRebuild = _CpqDaLogDrvPercentRebuild_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 12),
    _CpqDaLogDrvPercentRebuild_Type()
)
cpqDaLogDrvPercentRebuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPercentRebuild.setStatus("mandatory")
_CpqDaLogDrvStripeSize_Type = Integer32
_CpqDaLogDrvStripeSize_Object = MibTableColumn
cpqDaLogDrvStripeSize = _CpqDaLogDrvStripeSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 13),
    _CpqDaLogDrvStripeSize_Type()
)
cpqDaLogDrvStripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvStripeSize.setStatus("mandatory")


class _CpqDaLogDrvOsName_Type(DisplayString):
    """Custom type cpqDaLogDrvOsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaLogDrvOsName_Type.__name__ = "DisplayString"
_CpqDaLogDrvOsName_Object = MibTableColumn
cpqDaLogDrvOsName = _CpqDaLogDrvOsName_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 14),
    _CpqDaLogDrvOsName_Type()
)
cpqDaLogDrvOsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvOsName.setStatus("mandatory")
_CpqDaLogDrvBlinkTime_Type = Counter32
_CpqDaLogDrvBlinkTime_Object = MibTableColumn
cpqDaLogDrvBlinkTime = _CpqDaLogDrvBlinkTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 15),
    _CpqDaLogDrvBlinkTime_Type()
)
cpqDaLogDrvBlinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqDaLogDrvBlinkTime.setStatus("mandatory")


class _CpqDaLogDrvSpareReplaceMap_Type(OctetString):
    """Custom type cpqDaLogDrvSpareReplaceMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CpqDaLogDrvSpareReplaceMap_Type.__name__ = "OctetString"
_CpqDaLogDrvSpareReplaceMap_Object = MibTableColumn
cpqDaLogDrvSpareReplaceMap = _CpqDaLogDrvSpareReplaceMap_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 16),
    _CpqDaLogDrvSpareReplaceMap_Type()
)
cpqDaLogDrvSpareReplaceMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvSpareReplaceMap.setStatus("deprecated")


class _CpqDaLogDrvRebuildingPhyDrv_Type(Integer32):
    """Custom type cpqDaLogDrvRebuildingPhyDrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaLogDrvRebuildingPhyDrv_Type.__name__ = "Integer32"
_CpqDaLogDrvRebuildingPhyDrv_Object = MibTableColumn
cpqDaLogDrvRebuildingPhyDrv = _CpqDaLogDrvRebuildingPhyDrv_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 17),
    _CpqDaLogDrvRebuildingPhyDrv_Type()
)
cpqDaLogDrvRebuildingPhyDrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvRebuildingPhyDrv.setStatus("mandatory")


class _CpqDaLogDrvMultipathAccess_Type(Integer32):
    """Custom type cpqDaLogDrvMultipathAccess based on Integer32"""
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
        *(("noRedundantPath", 5),
          ("notConfigured", 3),
          ("notSupported", 2),
          ("other", 1),
          ("pathRedundant", 4))
    )


_CpqDaLogDrvMultipathAccess_Type.__name__ = "Integer32"
_CpqDaLogDrvMultipathAccess_Object = MibTableColumn
cpqDaLogDrvMultipathAccess = _CpqDaLogDrvMultipathAccess_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 18),
    _CpqDaLogDrvMultipathAccess_Type()
)
cpqDaLogDrvMultipathAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvMultipathAccess.setStatus("mandatory")


class _CpqDaLogDrvNmbrOfParityGroups_Type(Integer32):
    """Custom type cpqDaLogDrvNmbrOfParityGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqDaLogDrvNmbrOfParityGroups_Type.__name__ = "Integer32"
_CpqDaLogDrvNmbrOfParityGroups_Object = MibTableColumn
cpqDaLogDrvNmbrOfParityGroups = _CpqDaLogDrvNmbrOfParityGroups_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 19),
    _CpqDaLogDrvNmbrOfParityGroups_Type()
)
cpqDaLogDrvNmbrOfParityGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvNmbrOfParityGroups.setStatus("mandatory")


class _CpqDaLogDrvSplitMirrorBackupLogDrv_Type(Integer32):
    """Custom type cpqDaLogDrvSplitMirrorBackupLogDrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isBackupLogicalDrive", 3),
          ("isNotBackupLogicalDrive", 2),
          ("other", 1))
    )


_CpqDaLogDrvSplitMirrorBackupLogDrv_Type.__name__ = "Integer32"
_CpqDaLogDrvSplitMirrorBackupLogDrv_Object = MibTableColumn
cpqDaLogDrvSplitMirrorBackupLogDrv = _CpqDaLogDrvSplitMirrorBackupLogDrv_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 20),
    _CpqDaLogDrvSplitMirrorBackupLogDrv_Type()
)
cpqDaLogDrvSplitMirrorBackupLogDrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvSplitMirrorBackupLogDrv.setStatus("mandatory")


class _CpqDaLogDrvCacheVolAccelAssocType_Type(Integer32):
    """Custom type cpqDaLogDrvCacheVolAccelAssocType based on Integer32"""
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
        *(("cacheVolumeMember", 4),
          ("logicalDriveMember", 3),
          ("nonMember", 2),
          ("other", 1))
    )


_CpqDaLogDrvCacheVolAccelAssocType_Type.__name__ = "Integer32"
_CpqDaLogDrvCacheVolAccelAssocType_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelAssocType = _CpqDaLogDrvCacheVolAccelAssocType_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 21),
    _CpqDaLogDrvCacheVolAccelAssocType_Type()
)
cpqDaLogDrvCacheVolAccelAssocType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelAssocType.setStatus("mandatory")
_CpqDaLogDrvCacheVolIndex_Type = Integer32
_CpqDaLogDrvCacheVolIndex_Object = MibTableColumn
cpqDaLogDrvCacheVolIndex = _CpqDaLogDrvCacheVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 22),
    _CpqDaLogDrvCacheVolIndex_Type()
)
cpqDaLogDrvCacheVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolIndex.setStatus("mandatory")
_CpqDaLogDrvRPIPercentComplete_Type = Gauge32
_CpqDaLogDrvRPIPercentComplete_Object = MibTableColumn
cpqDaLogDrvRPIPercentComplete = _CpqDaLogDrvRPIPercentComplete_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 23),
    _CpqDaLogDrvRPIPercentComplete_Type()
)
cpqDaLogDrvRPIPercentComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvRPIPercentComplete.setStatus("mandatory")


class _CpqDaLogDrvSSDSmartPathStatus_Type(Integer32):
    """Custom type cpqDaLogDrvSSDSmartPathStatus based on Integer32"""
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
          ("ssdSmartPathDisabled", 3),
          ("ssdSmartPathEnabled", 4),
          ("updateDriver", 2))
    )


_CpqDaLogDrvSSDSmartPathStatus_Type.__name__ = "Integer32"
_CpqDaLogDrvSSDSmartPathStatus_Object = MibTableColumn
cpqDaLogDrvSSDSmartPathStatus = _CpqDaLogDrvSSDSmartPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 24),
    _CpqDaLogDrvSSDSmartPathStatus_Type()
)
cpqDaLogDrvSSDSmartPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvSSDSmartPathStatus.setStatus("mandatory")


class _CpqDaLogDrvEncryptionStatus_Type(Integer32):
    """Custom type cpqDaLogDrvEncryptionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 2),
          ("notEncrypted", 3),
          ("other", 1))
    )


_CpqDaLogDrvEncryptionStatus_Type.__name__ = "Integer32"
_CpqDaLogDrvEncryptionStatus_Object = MibTableColumn
cpqDaLogDrvEncryptionStatus = _CpqDaLogDrvEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 1, 1, 25),
    _CpqDaLogDrvEncryptionStatus_Type()
)
cpqDaLogDrvEncryptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvEncryptionStatus.setStatus("mandatory")
_CpqDaLogDrvPhyDrvExtAttachTable_Object = MibTable
cpqDaLogDrvPhyDrvExtAttachTable = _CpqDaLogDrvPhyDrvExtAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cpqDaLogDrvPhyDrvExtAttachTable.setStatus("mandatory")
_CpqDaLogDrvPhyDrvExtAttachEntry_Object = MibTableRow
cpqDaLogDrvPhyDrvExtAttachEntry = _CpqDaLogDrvPhyDrvExtAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 2, 1)
)
cpqDaLogDrvPhyDrvExtAttachEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaLogDrvPhyDrvAttachExtIndex"),
)
if mibBuilder.loadTexts:
    cpqDaLogDrvPhyDrvExtAttachEntry.setStatus("mandatory")


class _CpqDaLogDrvPhyDrvAttachExtIndex_Type(Integer32):
    """Custom type cpqDaLogDrvPhyDrvAttachExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaLogDrvPhyDrvAttachExtIndex_Type.__name__ = "Integer32"
_CpqDaLogDrvPhyDrvAttachExtIndex_Object = MibTableColumn
cpqDaLogDrvPhyDrvAttachExtIndex = _CpqDaLogDrvPhyDrvAttachExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 2, 1, 1),
    _CpqDaLogDrvPhyDrvAttachExtIndex_Type()
)
cpqDaLogDrvPhyDrvAttachExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPhyDrvAttachExtIndex.setStatus("mandatory")
_CpqDaLogDrvCntlrExtended_Type = Integer32
_CpqDaLogDrvCntlrExtended_Object = MibTableColumn
cpqDaLogDrvCntlrExtended = _CpqDaLogDrvCntlrExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 2, 1, 2),
    _CpqDaLogDrvCntlrExtended_Type()
)
cpqDaLogDrvCntlrExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCntlrExtended.setStatus("mandatory")


class _CpqDaLogDrvLogDrvExtended_Type(Integer32):
    """Custom type cpqDaLogDrvLogDrvExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaLogDrvLogDrvExtended_Type.__name__ = "Integer32"
_CpqDaLogDrvLogDrvExtended_Object = MibTableColumn
cpqDaLogDrvLogDrvExtended = _CpqDaLogDrvLogDrvExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 2, 1, 3),
    _CpqDaLogDrvLogDrvExtended_Type()
)
cpqDaLogDrvLogDrvExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvLogDrvExtended.setStatus("mandatory")


class _CpqDaLogDrvPhyDrvExtended_Type(Integer32):
    """Custom type cpqDaLogDrvPhyDrvExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaLogDrvPhyDrvExtended_Type.__name__ = "Integer32"
_CpqDaLogDrvPhyDrvExtended_Object = MibTableColumn
cpqDaLogDrvPhyDrvExtended = _CpqDaLogDrvPhyDrvExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 2, 1, 4),
    _CpqDaLogDrvPhyDrvExtended_Type()
)
cpqDaLogDrvPhyDrvExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPhyDrvExtended.setStatus("mandatory")
_CpqDaLogDrvSprRplcExtAttachTable_Object = MibTable
cpqDaLogDrvSprRplcExtAttachTable = _CpqDaLogDrvSprRplcExtAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    cpqDaLogDrvSprRplcExtAttachTable.setStatus("mandatory")
_CpqDaLogDrvSprRplcExtAttachEntry_Object = MibTableRow
cpqDaLogDrvSprRplcExtAttachEntry = _CpqDaLogDrvSprRplcExtAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 3, 1)
)
cpqDaLogDrvSprRplcExtAttachEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaLogDrvSprRplcAttachExtIndex"),
)
if mibBuilder.loadTexts:
    cpqDaLogDrvSprRplcExtAttachEntry.setStatus("mandatory")


class _CpqDaLogDrvSprRplcAttachExtIndex_Type(Integer32):
    """Custom type cpqDaLogDrvSprRplcAttachExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaLogDrvSprRplcAttachExtIndex_Type.__name__ = "Integer32"
_CpqDaLogDrvSprRplcAttachExtIndex_Object = MibTableColumn
cpqDaLogDrvSprRplcAttachExtIndex = _CpqDaLogDrvSprRplcAttachExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 3, 1, 1),
    _CpqDaLogDrvSprRplcAttachExtIndex_Type()
)
cpqDaLogDrvSprRplcAttachExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvSprRplcAttachExtIndex.setStatus("mandatory")
_CpqDaLogDrvSprRplcCntlrExtended_Type = Integer32
_CpqDaLogDrvSprRplcCntlrExtended_Object = MibTableColumn
cpqDaLogDrvSprRplcCntlrExtended = _CpqDaLogDrvSprRplcCntlrExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 3, 1, 2),
    _CpqDaLogDrvSprRplcCntlrExtended_Type()
)
cpqDaLogDrvSprRplcCntlrExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvSprRplcCntlrExtended.setStatus("mandatory")


class _CpqDaLogDrvSprRplcLogDrvExtended_Type(Integer32):
    """Custom type cpqDaLogDrvSprRplcLogDrvExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaLogDrvSprRplcLogDrvExtended_Type.__name__ = "Integer32"
_CpqDaLogDrvSprRplcLogDrvExtended_Object = MibTableColumn
cpqDaLogDrvSprRplcLogDrvExtended = _CpqDaLogDrvSprRplcLogDrvExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 3, 1, 3),
    _CpqDaLogDrvSprRplcLogDrvExtended_Type()
)
cpqDaLogDrvSprRplcLogDrvExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvSprRplcLogDrvExtended.setStatus("mandatory")


class _CpqDaLogDrvSprRplcReplacedPhysDrvExtended_Type(Integer32):
    """Custom type cpqDaLogDrvSprRplcReplacedPhysDrvExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaLogDrvSprRplcReplacedPhysDrvExtended_Type.__name__ = "Integer32"
_CpqDaLogDrvSprRplcReplacedPhysDrvExtended_Object = MibTableColumn
cpqDaLogDrvSprRplcReplacedPhysDrvExtended = _CpqDaLogDrvSprRplcReplacedPhysDrvExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 3, 1, 4),
    _CpqDaLogDrvSprRplcReplacedPhysDrvExtended_Type()
)
cpqDaLogDrvSprRplcReplacedPhysDrvExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvSprRplcReplacedPhysDrvExtended.setStatus("mandatory")


class _CpqDaLogDrvSprRplcSparePhysDrvExtended_Type(Integer32):
    """Custom type cpqDaLogDrvSprRplcSparePhysDrvExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaLogDrvSprRplcSparePhysDrvExtended_Type.__name__ = "Integer32"
_CpqDaLogDrvSprRplcSparePhysDrvExtended_Object = MibTableColumn
cpqDaLogDrvSprRplcSparePhysDrvExtended = _CpqDaLogDrvSprRplcSparePhysDrvExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 3, 1, 5),
    _CpqDaLogDrvSprRplcSparePhysDrvExtended_Type()
)
cpqDaLogDrvSprRplcSparePhysDrvExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvSprRplcSparePhysDrvExtended.setStatus("mandatory")
_CpqDaLogDrvAvalSprExtAttachTable_Object = MibTable
cpqDaLogDrvAvalSprExtAttachTable = _CpqDaLogDrvAvalSprExtAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    cpqDaLogDrvAvalSprExtAttachTable.setStatus("mandatory")
_CpqDaLogDrvAvalSprExtAttachEntry_Object = MibTableRow
cpqDaLogDrvAvalSprExtAttachEntry = _CpqDaLogDrvAvalSprExtAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 4, 1)
)
cpqDaLogDrvAvalSprExtAttachEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaLogDrvAvailSprAttachExtIndex"),
)
if mibBuilder.loadTexts:
    cpqDaLogDrvAvalSprExtAttachEntry.setStatus("mandatory")


class _CpqDaLogDrvAvailSprAttachExtIndex_Type(Integer32):
    """Custom type cpqDaLogDrvAvailSprAttachExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaLogDrvAvailSprAttachExtIndex_Type.__name__ = "Integer32"
_CpqDaLogDrvAvailSprAttachExtIndex_Object = MibTableColumn
cpqDaLogDrvAvailSprAttachExtIndex = _CpqDaLogDrvAvailSprAttachExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 4, 1, 1),
    _CpqDaLogDrvAvailSprAttachExtIndex_Type()
)
cpqDaLogDrvAvailSprAttachExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvAvailSprAttachExtIndex.setStatus("mandatory")
_CpqDaLogDrvAvailSprCntlrExtended_Type = Integer32
_CpqDaLogDrvAvailSprCntlrExtended_Object = MibTableColumn
cpqDaLogDrvAvailSprCntlrExtended = _CpqDaLogDrvAvailSprCntlrExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 4, 1, 2),
    _CpqDaLogDrvAvailSprCntlrExtended_Type()
)
cpqDaLogDrvAvailSprCntlrExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvAvailSprCntlrExtended.setStatus("mandatory")


class _CpqDaLogDrvAvailSprLogDrvExtended_Type(Integer32):
    """Custom type cpqDaLogDrvAvailSprLogDrvExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaLogDrvAvailSprLogDrvExtended_Type.__name__ = "Integer32"
_CpqDaLogDrvAvailSprLogDrvExtended_Object = MibTableColumn
cpqDaLogDrvAvailSprLogDrvExtended = _CpqDaLogDrvAvailSprLogDrvExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 4, 1, 3),
    _CpqDaLogDrvAvailSprLogDrvExtended_Type()
)
cpqDaLogDrvAvailSprLogDrvExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvAvailSprLogDrvExtended.setStatus("mandatory")


class _CpqDaLogDrvAvailSprAvailableSpareExtended_Type(Integer32):
    """Custom type cpqDaLogDrvAvailSprAvailableSpareExtended based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaLogDrvAvailSprAvailableSpareExtended_Type.__name__ = "Integer32"
_CpqDaLogDrvAvailSprAvailableSpareExtended_Object = MibTableColumn
cpqDaLogDrvAvailSprAvailableSpareExtended = _CpqDaLogDrvAvailSprAvailableSpareExtended_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 4, 1, 4),
    _CpqDaLogDrvAvailSprAvailableSpareExtended_Type()
)
cpqDaLogDrvAvailSprAvailableSpareExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvAvailSprAvailableSpareExtended.setStatus("mandatory")
_CpqDaLogDrvCacheVolumeAccelTable_Object = MibTable
cpqDaLogDrvCacheVolumeAccelTable = _CpqDaLogDrvCacheVolumeAccelTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5)
)
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolumeAccelTable.setStatus("mandatory")
_CpqDaLogDrvCacheVolumeAccelEntry_Object = MibTableRow
cpqDaLogDrvCacheVolumeAccelEntry = _CpqDaLogDrvCacheVolumeAccelEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1)
)
cpqDaLogDrvCacheVolumeAccelEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaLogDrvCacheVolAccelCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaLogDrvCacheVolAccelLogDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolumeAccelEntry.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelCntlrIndex_Type = Integer32
_CpqDaLogDrvCacheVolAccelCntlrIndex_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelCntlrIndex = _CpqDaLogDrvCacheVolAccelCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 1),
    _CpqDaLogDrvCacheVolAccelCntlrIndex_Type()
)
cpqDaLogDrvCacheVolAccelCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelCntlrIndex.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelLogDrvIndex_Type = Integer32
_CpqDaLogDrvCacheVolAccelLogDrvIndex_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelLogDrvIndex = _CpqDaLogDrvCacheVolAccelLogDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 2),
    _CpqDaLogDrvCacheVolAccelLogDrvIndex_Type()
)
cpqDaLogDrvCacheVolAccelLogDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelLogDrvIndex.setStatus("mandatory")


class _CpqDaLogDrvCacheVolAccelCachingAlgorithm_Type(Integer32):
    """Custom type cpqDaLogDrvCacheVolAccelCachingAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiSegment", 2),
          ("other", 1),
          ("singleSegment", 3))
    )


_CpqDaLogDrvCacheVolAccelCachingAlgorithm_Type.__name__ = "Integer32"
_CpqDaLogDrvCacheVolAccelCachingAlgorithm_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelCachingAlgorithm = _CpqDaLogDrvCacheVolAccelCachingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 3),
    _CpqDaLogDrvCacheVolAccelCachingAlgorithm_Type()
)
cpqDaLogDrvCacheVolAccelCachingAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelCachingAlgorithm.setStatus("mandatory")


class _CpqDaLogDrvCacheVolAccelCacheState_Type(Integer32):
    """Custom type cpqDaLogDrvCacheVolAccelCacheState based on Integer32"""
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
        *(("cacheConfigurationFailed", 9),
          ("cacheVolOffline", 4),
          ("configuring", 8),
          ("degraded", 3),
          ("flushing", 7),
          ("logDriveOffline", 5),
          ("neverConfigured", 6),
          ("ok", 2),
          ("other", 1))
    )


_CpqDaLogDrvCacheVolAccelCacheState_Type.__name__ = "Integer32"
_CpqDaLogDrvCacheVolAccelCacheState_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelCacheState = _CpqDaLogDrvCacheVolAccelCacheState_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 4),
    _CpqDaLogDrvCacheVolAccelCacheState_Type()
)
cpqDaLogDrvCacheVolAccelCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelCacheState.setStatus("mandatory")


class _CpqDaLogDrvCacheVolAccelWritePolicy_Type(Integer32):
    """Custom type cpqDaLogDrvCacheVolAccelWritePolicy based on Integer32"""
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
          ("readOnly", 2),
          ("writeBackSafe", 4),
          ("writeBackUnsafe", 5),
          ("writeThrough", 3),
          ("writeThroughNoLoad", 6))
    )


_CpqDaLogDrvCacheVolAccelWritePolicy_Type.__name__ = "Integer32"
_CpqDaLogDrvCacheVolAccelWritePolicy_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelWritePolicy = _CpqDaLogDrvCacheVolAccelWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 5),
    _CpqDaLogDrvCacheVolAccelWritePolicy_Type()
)
cpqDaLogDrvCacheVolAccelWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelWritePolicy.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadHitsH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadHitsH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadHitsH = _CpqDaLogDrvCacheVolAccelNoOfReadHitsH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 6),
    _CpqDaLogDrvCacheVolAccelNoOfReadHitsH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadHitsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadHitsH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadHits_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadHits_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadHits = _CpqDaLogDrvCacheVolAccelNoOfReadHits_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 7),
    _CpqDaLogDrvCacheVolAccelNoOfReadHits_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadHits.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadMissDoLoadH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadMissDoLoadH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadMissDoLoadH = _CpqDaLogDrvCacheVolAccelNoOfReadMissDoLoadH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 8),
    _CpqDaLogDrvCacheVolAccelNoOfReadMissDoLoadH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadMissDoLoadH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadMissDoLoadH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadMissDoLoad_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadMissDoLoad_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadMissDoLoad = _CpqDaLogDrvCacheVolAccelNoOfReadMissDoLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 9),
    _CpqDaLogDrvCacheVolAccelNoOfReadMissDoLoad_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadMissDoLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadMissDoLoad.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadMissLoadingH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadMissLoadingH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadMissLoadingH = _CpqDaLogDrvCacheVolAccelNoOfReadMissLoadingH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 10),
    _CpqDaLogDrvCacheVolAccelNoOfReadMissLoadingH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadMissLoadingH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadMissLoadingH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadMissLoading_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadMissLoading_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadMissLoading = _CpqDaLogDrvCacheVolAccelNoOfReadMissLoading_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 11),
    _CpqDaLogDrvCacheVolAccelNoOfReadMissLoading_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadMissLoading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadMissLoading.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadMissSkipH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadMissSkipH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadMissSkipH = _CpqDaLogDrvCacheVolAccelNoOfReadMissSkipH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 12),
    _CpqDaLogDrvCacheVolAccelNoOfReadMissSkipH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadMissSkipH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadMissSkipH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadMissSkip_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadMissSkip_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadMissSkip = _CpqDaLogDrvCacheVolAccelNoOfReadMissSkip_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 13),
    _CpqDaLogDrvCacheVolAccelNoOfReadMissSkip_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadMissSkip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadMissSkip.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelReadCacheHitRate_Type = Gauge32
_CpqDaLogDrvCacheVolAccelReadCacheHitRate_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelReadCacheHitRate = _CpqDaLogDrvCacheVolAccelReadCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 14),
    _CpqDaLogDrvCacheVolAccelReadCacheHitRate_Type()
)
cpqDaLogDrvCacheVolAccelReadCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelReadCacheHitRate.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteHitsH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteHitsH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteHitsH = _CpqDaLogDrvCacheVolAccelNoOfWriteHitsH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 15),
    _CpqDaLogDrvCacheVolAccelNoOfWriteHitsH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteHitsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteHitsH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteHits_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteHits_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteHits = _CpqDaLogDrvCacheVolAccelNoOfWriteHits_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 16),
    _CpqDaLogDrvCacheVolAccelNoOfWriteHits_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteHits.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoadH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoadH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoadH = _CpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoadH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 17),
    _CpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoadH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoadH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoadH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoad_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoad_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoad = _CpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 18),
    _CpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoad_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoad.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteMissLoadingH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteMissLoadingH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteMissLoadingH = _CpqDaLogDrvCacheVolAccelNoOfWriteMissLoadingH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 19),
    _CpqDaLogDrvCacheVolAccelNoOfWriteMissLoadingH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteMissLoadingH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteMissLoadingH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteMissLoading_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteMissLoading_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteMissLoading = _CpqDaLogDrvCacheVolAccelNoOfWriteMissLoading_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 20),
    _CpqDaLogDrvCacheVolAccelNoOfWriteMissLoading_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteMissLoading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteMissLoading.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteMissSkipH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteMissSkipH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteMissSkipH = _CpqDaLogDrvCacheVolAccelNoOfWriteMissSkipH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 21),
    _CpqDaLogDrvCacheVolAccelNoOfWriteMissSkipH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteMissSkipH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteMissSkipH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteMissSkip_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteMissSkip_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteMissSkip = _CpqDaLogDrvCacheVolAccelNoOfWriteMissSkip_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 22),
    _CpqDaLogDrvCacheVolAccelNoOfWriteMissSkip_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteMissSkip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteMissSkip.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelWriteCacheHitRate_Type = Gauge32
_CpqDaLogDrvCacheVolAccelWriteCacheHitRate_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelWriteCacheHitRate = _CpqDaLogDrvCacheVolAccelWriteCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 23),
    _CpqDaLogDrvCacheVolAccelWriteCacheHitRate_Type()
)
cpqDaLogDrvCacheVolAccelWriteCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelWriteCacheHitRate.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelLoadFailures_Type = Integer32
_CpqDaLogDrvCacheVolAccelLoadFailures_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelLoadFailures = _CpqDaLogDrvCacheVolAccelLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 24),
    _CpqDaLogDrvCacheVolAccelLoadFailures_Type()
)
cpqDaLogDrvCacheVolAccelLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelLoadFailures.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelCacheLineSize_Type = Integer32
_CpqDaLogDrvCacheVolAccelCacheLineSize_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelCacheLineSize = _CpqDaLogDrvCacheVolAccelCacheLineSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 25),
    _CpqDaLogDrvCacheVolAccelCacheLineSize_Type()
)
cpqDaLogDrvCacheVolAccelCacheLineSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelCacheLineSize.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadMissLockedH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadMissLockedH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadMissLockedH = _CpqDaLogDrvCacheVolAccelNoOfReadMissLockedH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 26),
    _CpqDaLogDrvCacheVolAccelNoOfReadMissLockedH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadMissLockedH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadMissLockedH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadMissLocked_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadMissLocked_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadMissLocked = _CpqDaLogDrvCacheVolAccelNoOfReadMissLocked_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 27),
    _CpqDaLogDrvCacheVolAccelNoOfReadMissLocked_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadMissLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadMissLocked.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteMissLockedH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteMissLockedH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteMissLockedH = _CpqDaLogDrvCacheVolAccelNoOfWriteMissLockedH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 28),
    _CpqDaLogDrvCacheVolAccelNoOfWriteMissLockedH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteMissLockedH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteMissLockedH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteMissLocked_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteMissLocked_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteMissLocked = _CpqDaLogDrvCacheVolAccelNoOfWriteMissLocked_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 29),
    _CpqDaLogDrvCacheVolAccelNoOfWriteMissLocked_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteMissLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteMissLocked.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadMissTotalH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadMissTotalH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadMissTotalH = _CpqDaLogDrvCacheVolAccelNoOfReadMissTotalH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 30),
    _CpqDaLogDrvCacheVolAccelNoOfReadMissTotalH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadMissTotalH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadMissTotalH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfReadMissTotal_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfReadMissTotal_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfReadMissTotal = _CpqDaLogDrvCacheVolAccelNoOfReadMissTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 31),
    _CpqDaLogDrvCacheVolAccelNoOfReadMissTotal_Type()
)
cpqDaLogDrvCacheVolAccelNoOfReadMissTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfReadMissTotal.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteMissTotalH_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteMissTotalH_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteMissTotalH = _CpqDaLogDrvCacheVolAccelNoOfWriteMissTotalH_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 32),
    _CpqDaLogDrvCacheVolAccelNoOfWriteMissTotalH_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteMissTotalH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteMissTotalH.setStatus("mandatory")
_CpqDaLogDrvCacheVolAccelNoOfWriteMissTotal_Type = Integer32
_CpqDaLogDrvCacheVolAccelNoOfWriteMissTotal_Object = MibTableColumn
cpqDaLogDrvCacheVolAccelNoOfWriteMissTotal = _CpqDaLogDrvCacheVolAccelNoOfWriteMissTotal_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 3, 5, 1, 33),
    _CpqDaLogDrvCacheVolAccelNoOfWriteMissTotal_Type()
)
cpqDaLogDrvCacheVolAccelNoOfWriteMissTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvCacheVolAccelNoOfWriteMissTotal.setStatus("mandatory")
_CpqDaSpareDrv_ObjectIdentity = ObjectIdentity
cpqDaSpareDrv = _CpqDaSpareDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4)
)
_CpqDaSpareTable_Object = MibTable
cpqDaSpareTable = _CpqDaSpareTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqDaSpareTable.setStatus("mandatory")
_CpqDaSpareEntry_Object = MibTableRow
cpqDaSpareEntry = _CpqDaSpareEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1)
)
cpqDaSpareEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaSpareCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaSparePhyDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqDaSpareEntry.setStatus("mandatory")
_CpqDaSpareCntlrIndex_Type = Integer32
_CpqDaSpareCntlrIndex_Object = MibTableColumn
cpqDaSpareCntlrIndex = _CpqDaSpareCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 1),
    _CpqDaSpareCntlrIndex_Type()
)
cpqDaSpareCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSpareCntlrIndex.setStatus("mandatory")


class _CpqDaSparePhyDrvIndex_Type(Integer32):
    """Custom type cpqDaSparePhyDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaSparePhyDrvIndex_Type.__name__ = "Integer32"
_CpqDaSparePhyDrvIndex_Object = MibTableColumn
cpqDaSparePhyDrvIndex = _CpqDaSparePhyDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 2),
    _CpqDaSparePhyDrvIndex_Type()
)
cpqDaSparePhyDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSparePhyDrvIndex.setStatus("mandatory")


class _CpqDaSpareStatus_Type(Integer32):
    """Custom type cpqDaSpareStatus based on Integer32"""
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
        *(("active", 6),
          ("building", 5),
          ("failed", 3),
          ("inactive", 4),
          ("invalid", 2),
          ("other", 1))
    )


_CpqDaSpareStatus_Type.__name__ = "Integer32"
_CpqDaSpareStatus_Object = MibTableColumn
cpqDaSpareStatus = _CpqDaSpareStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 3),
    _CpqDaSpareStatus_Type()
)
cpqDaSpareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSpareStatus.setStatus("mandatory")


class _CpqDaSpareReplacedDrv_Type(Integer32):
    """Custom type cpqDaSpareReplacedDrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaSpareReplacedDrv_Type.__name__ = "Integer32"
_CpqDaSpareReplacedDrv_Object = MibTableColumn
cpqDaSpareReplacedDrv = _CpqDaSpareReplacedDrv_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 4),
    _CpqDaSpareReplacedDrv_Type()
)
cpqDaSpareReplacedDrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSpareReplacedDrv.setStatus("mandatory")
_CpqDaSpareRebuildBlks_Type = Counter32
_CpqDaSpareRebuildBlks_Object = MibTableColumn
cpqDaSpareRebuildBlks = _CpqDaSpareRebuildBlks_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 5),
    _CpqDaSpareRebuildBlks_Type()
)
cpqDaSpareRebuildBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSpareRebuildBlks.setStatus("deprecated")


class _CpqDaSpareCondition_Type(Integer32):
    """Custom type cpqDaSpareCondition based on Integer32"""
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


_CpqDaSpareCondition_Type.__name__ = "Integer32"
_CpqDaSpareCondition_Object = MibTableColumn
cpqDaSpareCondition = _CpqDaSpareCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 6),
    _CpqDaSpareCondition_Type()
)
cpqDaSpareCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSpareCondition.setStatus("mandatory")
_CpqDaSpareBusNumber_Type = Integer32
_CpqDaSpareBusNumber_Object = MibTableColumn
cpqDaSpareBusNumber = _CpqDaSpareBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 7),
    _CpqDaSpareBusNumber_Type()
)
cpqDaSpareBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSpareBusNumber.setStatus("mandatory")


class _CpqDaSpareBay_Type(Integer32):
    """Custom type cpqDaSpareBay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaSpareBay_Type.__name__ = "Integer32"
_CpqDaSpareBay_Object = MibTableColumn
cpqDaSpareBay = _CpqDaSpareBay_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 8),
    _CpqDaSpareBay_Type()
)
cpqDaSpareBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSpareBay.setStatus("mandatory")
_CpqDaSpareReplacedDrvBusNumber_Type = Integer32
_CpqDaSpareReplacedDrvBusNumber_Object = MibTableColumn
cpqDaSpareReplacedDrvBusNumber = _CpqDaSpareReplacedDrvBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 9),
    _CpqDaSpareReplacedDrvBusNumber_Type()
)
cpqDaSpareReplacedDrvBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSpareReplacedDrvBusNumber.setStatus("mandatory")
_CpqDaSpareReplacedDrvBay_Type = Integer32
_CpqDaSpareReplacedDrvBay_Object = MibTableColumn
cpqDaSpareReplacedDrvBay = _CpqDaSpareReplacedDrvBay_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 10),
    _CpqDaSpareReplacedDrvBay_Type()
)
cpqDaSpareReplacedDrvBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSpareReplacedDrvBay.setStatus("mandatory")
_CpqDaSparePercentRebuild_Type = Gauge32
_CpqDaSparePercentRebuild_Object = MibTableColumn
cpqDaSparePercentRebuild = _CpqDaSparePercentRebuild_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 11),
    _CpqDaSparePercentRebuild_Type()
)
cpqDaSparePercentRebuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSparePercentRebuild.setStatus("mandatory")


class _CpqDaSpareLocationString_Type(DisplayString):
    """Custom type cpqDaSpareLocationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaSpareLocationString_Type.__name__ = "DisplayString"
_CpqDaSpareLocationString_Object = MibTableColumn
cpqDaSpareLocationString = _CpqDaSpareLocationString_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 4, 1, 1, 12),
    _CpqDaSpareLocationString_Type()
)
cpqDaSpareLocationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaSpareLocationString.setStatus("mandatory")
_CpqDaPhyDrv_ObjectIdentity = ObjectIdentity
cpqDaPhyDrv = _CpqDaPhyDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5)
)
_CpqDaPhyDrvTable_Object = MibTable
cpqDaPhyDrvTable = _CpqDaPhyDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvTable.setStatus("mandatory")
_CpqDaPhyDrvEntry_Object = MibTableRow
cpqDaPhyDrvEntry = _CpqDaPhyDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1)
)
cpqDaPhyDrvEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaPhyDrvIndex"),
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvEntry.setStatus("mandatory")
_CpqDaPhyDrvCntlrIndex_Type = Integer32
_CpqDaPhyDrvCntlrIndex_Object = MibTableColumn
cpqDaPhyDrvCntlrIndex = _CpqDaPhyDrvCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 1),
    _CpqDaPhyDrvCntlrIndex_Type()
)
cpqDaPhyDrvCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvCntlrIndex.setStatus("mandatory")


class _CpqDaPhyDrvIndex_Type(Integer32):
    """Custom type cpqDaPhyDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaPhyDrvIndex_Type.__name__ = "Integer32"
_CpqDaPhyDrvIndex_Object = MibTableColumn
cpqDaPhyDrvIndex = _CpqDaPhyDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 2),
    _CpqDaPhyDrvIndex_Type()
)
cpqDaPhyDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvIndex.setStatus("mandatory")


class _CpqDaPhyDrvModel_Type(DisplayString):
    """Custom type cpqDaPhyDrvModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaPhyDrvModel_Type.__name__ = "DisplayString"
_CpqDaPhyDrvModel_Object = MibTableColumn
cpqDaPhyDrvModel = _CpqDaPhyDrvModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 3),
    _CpqDaPhyDrvModel_Type()
)
cpqDaPhyDrvModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvModel.setStatus("mandatory")


class _CpqDaPhyDrvFWRev_Type(DisplayString):
    """Custom type cpqDaPhyDrvFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqDaPhyDrvFWRev_Type.__name__ = "DisplayString"
_CpqDaPhyDrvFWRev_Object = MibTableColumn
cpqDaPhyDrvFWRev = _CpqDaPhyDrvFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 4),
    _CpqDaPhyDrvFWRev_Type()
)
cpqDaPhyDrvFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvFWRev.setStatus("mandatory")


class _CpqDaPhyDrvBay_Type(Integer32):
    """Custom type cpqDaPhyDrvBay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaPhyDrvBay_Type.__name__ = "Integer32"
_CpqDaPhyDrvBay_Object = MibTableColumn
cpqDaPhyDrvBay = _CpqDaPhyDrvBay_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 5),
    _CpqDaPhyDrvBay_Type()
)
cpqDaPhyDrvBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvBay.setStatus("mandatory")


class _CpqDaPhyDrvStatus_Type(Integer32):
    """Custom type cpqDaPhyDrvStatus based on Integer32"""
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
        *(("eraseDone", 6),
          ("eraseQueued", 7),
          ("erasing", 5),
          ("failed", 3),
          ("notAuthenticated", 9),
          ("ok", 2),
          ("other", 1),
          ("predictiveFailure", 4),
          ("ssdWearOut", 8))
    )


_CpqDaPhyDrvStatus_Type.__name__ = "Integer32"
_CpqDaPhyDrvStatus_Object = MibTableColumn
cpqDaPhyDrvStatus = _CpqDaPhyDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 6),
    _CpqDaPhyDrvStatus_Type()
)
cpqDaPhyDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvStatus.setStatus("mandatory")
_CpqDaPhyDrvFactReallocs_Type = Integer32
_CpqDaPhyDrvFactReallocs_Object = MibTableColumn
cpqDaPhyDrvFactReallocs = _CpqDaPhyDrvFactReallocs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 7),
    _CpqDaPhyDrvFactReallocs_Type()
)
cpqDaPhyDrvFactReallocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvFactReallocs.setStatus("mandatory")
_CpqDaPhyDrvUsedReallocs_Type = Counter32
_CpqDaPhyDrvUsedReallocs_Object = MibTableColumn
cpqDaPhyDrvUsedReallocs = _CpqDaPhyDrvUsedReallocs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 8),
    _CpqDaPhyDrvUsedReallocs_Type()
)
cpqDaPhyDrvUsedReallocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvUsedReallocs.setStatus("mandatory")
_CpqDaPhyDrvRefHours_Type = Counter32
_CpqDaPhyDrvRefHours_Object = MibTableColumn
cpqDaPhyDrvRefHours = _CpqDaPhyDrvRefHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 9),
    _CpqDaPhyDrvRefHours_Type()
)
cpqDaPhyDrvRefHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvRefHours.setStatus("mandatory")
_CpqDaPhyDrvHReads_Type = Counter32
_CpqDaPhyDrvHReads_Object = MibTableColumn
cpqDaPhyDrvHReads = _CpqDaPhyDrvHReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 10),
    _CpqDaPhyDrvHReads_Type()
)
cpqDaPhyDrvHReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHReads.setStatus("mandatory")
_CpqDaPhyDrvReads_Type = Counter32
_CpqDaPhyDrvReads_Object = MibTableColumn
cpqDaPhyDrvReads = _CpqDaPhyDrvReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 11),
    _CpqDaPhyDrvReads_Type()
)
cpqDaPhyDrvReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvReads.setStatus("mandatory")
_CpqDaPhyDrvHWrites_Type = Counter32
_CpqDaPhyDrvHWrites_Object = MibTableColumn
cpqDaPhyDrvHWrites = _CpqDaPhyDrvHWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 12),
    _CpqDaPhyDrvHWrites_Type()
)
cpqDaPhyDrvHWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHWrites.setStatus("mandatory")
_CpqDaPhyDrvWrites_Type = Counter32
_CpqDaPhyDrvWrites_Object = MibTableColumn
cpqDaPhyDrvWrites = _CpqDaPhyDrvWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 13),
    _CpqDaPhyDrvWrites_Type()
)
cpqDaPhyDrvWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvWrites.setStatus("mandatory")
_CpqDaPhyDrvHSeeks_Type = Counter32
_CpqDaPhyDrvHSeeks_Object = MibTableColumn
cpqDaPhyDrvHSeeks = _CpqDaPhyDrvHSeeks_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 14),
    _CpqDaPhyDrvHSeeks_Type()
)
cpqDaPhyDrvHSeeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHSeeks.setStatus("mandatory")
_CpqDaPhyDrvSeeks_Type = Counter32
_CpqDaPhyDrvSeeks_Object = MibTableColumn
cpqDaPhyDrvSeeks = _CpqDaPhyDrvSeeks_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 15),
    _CpqDaPhyDrvSeeks_Type()
)
cpqDaPhyDrvSeeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSeeks.setStatus("mandatory")
_CpqDaPhyDrvHardReadErrs_Type = Counter32
_CpqDaPhyDrvHardReadErrs_Object = MibTableColumn
cpqDaPhyDrvHardReadErrs = _CpqDaPhyDrvHardReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 16),
    _CpqDaPhyDrvHardReadErrs_Type()
)
cpqDaPhyDrvHardReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHardReadErrs.setStatus("mandatory")
_CpqDaPhyDrvRecvReadErrs_Type = Counter32
_CpqDaPhyDrvRecvReadErrs_Object = MibTableColumn
cpqDaPhyDrvRecvReadErrs = _CpqDaPhyDrvRecvReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 17),
    _CpqDaPhyDrvRecvReadErrs_Type()
)
cpqDaPhyDrvRecvReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvRecvReadErrs.setStatus("mandatory")
_CpqDaPhyDrvHardWriteErrs_Type = Counter32
_CpqDaPhyDrvHardWriteErrs_Object = MibTableColumn
cpqDaPhyDrvHardWriteErrs = _CpqDaPhyDrvHardWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 18),
    _CpqDaPhyDrvHardWriteErrs_Type()
)
cpqDaPhyDrvHardWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHardWriteErrs.setStatus("mandatory")
_CpqDaPhyDrvRecvWriteErrs_Type = Counter32
_CpqDaPhyDrvRecvWriteErrs_Object = MibTableColumn
cpqDaPhyDrvRecvWriteErrs = _CpqDaPhyDrvRecvWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 19),
    _CpqDaPhyDrvRecvWriteErrs_Type()
)
cpqDaPhyDrvRecvWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvRecvWriteErrs.setStatus("mandatory")
_CpqDaPhyDrvHSeekErrs_Type = Counter32
_CpqDaPhyDrvHSeekErrs_Object = MibTableColumn
cpqDaPhyDrvHSeekErrs = _CpqDaPhyDrvHSeekErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 20),
    _CpqDaPhyDrvHSeekErrs_Type()
)
cpqDaPhyDrvHSeekErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHSeekErrs.setStatus("mandatory")
_CpqDaPhyDrvSeekErrs_Type = Counter32
_CpqDaPhyDrvSeekErrs_Object = MibTableColumn
cpqDaPhyDrvSeekErrs = _CpqDaPhyDrvSeekErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 21),
    _CpqDaPhyDrvSeekErrs_Type()
)
cpqDaPhyDrvSeekErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSeekErrs.setStatus("mandatory")
_CpqDaPhyDrvSpinupTime_Type = Integer32
_CpqDaPhyDrvSpinupTime_Object = MibTableColumn
cpqDaPhyDrvSpinupTime = _CpqDaPhyDrvSpinupTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 22),
    _CpqDaPhyDrvSpinupTime_Type()
)
cpqDaPhyDrvSpinupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSpinupTime.setStatus("mandatory")
_CpqDaPhyDrvFunctTest1_Type = Gauge32
_CpqDaPhyDrvFunctTest1_Object = MibTableColumn
cpqDaPhyDrvFunctTest1 = _CpqDaPhyDrvFunctTest1_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 23),
    _CpqDaPhyDrvFunctTest1_Type()
)
cpqDaPhyDrvFunctTest1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvFunctTest1.setStatus("deprecated")
_CpqDaPhyDrvFunctTest2_Type = Gauge32
_CpqDaPhyDrvFunctTest2_Object = MibTableColumn
cpqDaPhyDrvFunctTest2 = _CpqDaPhyDrvFunctTest2_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 24),
    _CpqDaPhyDrvFunctTest2_Type()
)
cpqDaPhyDrvFunctTest2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvFunctTest2.setStatus("deprecated")
_CpqDaPhyDrvFunctTest3_Type = Gauge32
_CpqDaPhyDrvFunctTest3_Object = MibTableColumn
cpqDaPhyDrvFunctTest3 = _CpqDaPhyDrvFunctTest3_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 25),
    _CpqDaPhyDrvFunctTest3_Type()
)
cpqDaPhyDrvFunctTest3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvFunctTest3.setStatus("deprecated")
_CpqDaPhyDrvDrqTimeouts_Type = Counter32
_CpqDaPhyDrvDrqTimeouts_Object = MibTableColumn
cpqDaPhyDrvDrqTimeouts = _CpqDaPhyDrvDrqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 26),
    _CpqDaPhyDrvDrqTimeouts_Type()
)
cpqDaPhyDrvDrqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvDrqTimeouts.setStatus("mandatory")
_CpqDaPhyDrvOtherTimeouts_Type = Counter32
_CpqDaPhyDrvOtherTimeouts_Object = MibTableColumn
cpqDaPhyDrvOtherTimeouts = _CpqDaPhyDrvOtherTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 27),
    _CpqDaPhyDrvOtherTimeouts_Type()
)
cpqDaPhyDrvOtherTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvOtherTimeouts.setStatus("mandatory")
_CpqDaPhyDrvSpinupRetries_Type = Counter32
_CpqDaPhyDrvSpinupRetries_Object = MibTableColumn
cpqDaPhyDrvSpinupRetries = _CpqDaPhyDrvSpinupRetries_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 28),
    _CpqDaPhyDrvSpinupRetries_Type()
)
cpqDaPhyDrvSpinupRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSpinupRetries.setStatus("mandatory")
_CpqDaPhyDrvBadRecvReads_Type = Counter32
_CpqDaPhyDrvBadRecvReads_Object = MibTableColumn
cpqDaPhyDrvBadRecvReads = _CpqDaPhyDrvBadRecvReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 29),
    _CpqDaPhyDrvBadRecvReads_Type()
)
cpqDaPhyDrvBadRecvReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvBadRecvReads.setStatus("mandatory")
_CpqDaPhyDrvBadRecvWrites_Type = Counter32
_CpqDaPhyDrvBadRecvWrites_Object = MibTableColumn
cpqDaPhyDrvBadRecvWrites = _CpqDaPhyDrvBadRecvWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 30),
    _CpqDaPhyDrvBadRecvWrites_Type()
)
cpqDaPhyDrvBadRecvWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvBadRecvWrites.setStatus("mandatory")
_CpqDaPhyDrvFormatErrs_Type = Counter32
_CpqDaPhyDrvFormatErrs_Object = MibTableColumn
cpqDaPhyDrvFormatErrs = _CpqDaPhyDrvFormatErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 31),
    _CpqDaPhyDrvFormatErrs_Type()
)
cpqDaPhyDrvFormatErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvFormatErrs.setStatus("mandatory")
_CpqDaPhyDrvPostErrs_Type = Counter32
_CpqDaPhyDrvPostErrs_Object = MibTableColumn
cpqDaPhyDrvPostErrs = _CpqDaPhyDrvPostErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 32),
    _CpqDaPhyDrvPostErrs_Type()
)
cpqDaPhyDrvPostErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPostErrs.setStatus("mandatory")
_CpqDaPhyDrvNotReadyErrs_Type = Counter32
_CpqDaPhyDrvNotReadyErrs_Object = MibTableColumn
cpqDaPhyDrvNotReadyErrs = _CpqDaPhyDrvNotReadyErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 33),
    _CpqDaPhyDrvNotReadyErrs_Type()
)
cpqDaPhyDrvNotReadyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvNotReadyErrs.setStatus("mandatory")
_CpqDaPhyDrvReallocAborts_Type = Counter32
_CpqDaPhyDrvReallocAborts_Object = MibTableColumn
cpqDaPhyDrvReallocAborts = _CpqDaPhyDrvReallocAborts_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 34),
    _CpqDaPhyDrvReallocAborts_Type()
)
cpqDaPhyDrvReallocAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvReallocAborts.setStatus("mandatory")


class _CpqDaPhyDrvThreshPassed_Type(Integer32):
    """Custom type cpqDaPhyDrvThreshPassed based on Integer32"""
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


_CpqDaPhyDrvThreshPassed_Type.__name__ = "Integer32"
_CpqDaPhyDrvThreshPassed_Object = MibTableColumn
cpqDaPhyDrvThreshPassed = _CpqDaPhyDrvThreshPassed_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 35),
    _CpqDaPhyDrvThreshPassed_Type()
)
cpqDaPhyDrvThreshPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThreshPassed.setStatus("mandatory")


class _CpqDaPhyDrvHasMonInfo_Type(Integer32):
    """Custom type cpqDaPhyDrvHasMonInfo based on Integer32"""
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


_CpqDaPhyDrvHasMonInfo_Type.__name__ = "Integer32"
_CpqDaPhyDrvHasMonInfo_Object = MibTableColumn
cpqDaPhyDrvHasMonInfo = _CpqDaPhyDrvHasMonInfo_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 36),
    _CpqDaPhyDrvHasMonInfo_Type()
)
cpqDaPhyDrvHasMonInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHasMonInfo.setStatus("mandatory")


class _CpqDaPhyDrvCondition_Type(Integer32):
    """Custom type cpqDaPhyDrvCondition based on Integer32"""
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


_CpqDaPhyDrvCondition_Type.__name__ = "Integer32"
_CpqDaPhyDrvCondition_Object = MibTableColumn
cpqDaPhyDrvCondition = _CpqDaPhyDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 37),
    _CpqDaPhyDrvCondition_Type()
)
cpqDaPhyDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvCondition.setStatus("mandatory")
_CpqDaPhyDrvHotPlugs_Type = Counter32
_CpqDaPhyDrvHotPlugs_Object = MibTableColumn
cpqDaPhyDrvHotPlugs = _CpqDaPhyDrvHotPlugs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 38),
    _CpqDaPhyDrvHotPlugs_Type()
)
cpqDaPhyDrvHotPlugs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHotPlugs.setStatus("mandatory")
_CpqDaPhyDrvMediaErrs_Type = Counter32
_CpqDaPhyDrvMediaErrs_Object = MibTableColumn
cpqDaPhyDrvMediaErrs = _CpqDaPhyDrvMediaErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 39),
    _CpqDaPhyDrvMediaErrs_Type()
)
cpqDaPhyDrvMediaErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvMediaErrs.setStatus("mandatory")
_CpqDaPhyDrvHardwareErrs_Type = Counter32
_CpqDaPhyDrvHardwareErrs_Object = MibTableColumn
cpqDaPhyDrvHardwareErrs = _CpqDaPhyDrvHardwareErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 40),
    _CpqDaPhyDrvHardwareErrs_Type()
)
cpqDaPhyDrvHardwareErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHardwareErrs.setStatus("mandatory")
_CpqDaPhyDrvAbortedCmds_Type = Counter32
_CpqDaPhyDrvAbortedCmds_Object = MibTableColumn
cpqDaPhyDrvAbortedCmds = _CpqDaPhyDrvAbortedCmds_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 41),
    _CpqDaPhyDrvAbortedCmds_Type()
)
cpqDaPhyDrvAbortedCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvAbortedCmds.setStatus("mandatory")
_CpqDaPhyDrvSpinUpErrs_Type = Counter32
_CpqDaPhyDrvSpinUpErrs_Object = MibTableColumn
cpqDaPhyDrvSpinUpErrs = _CpqDaPhyDrvSpinUpErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 42),
    _CpqDaPhyDrvSpinUpErrs_Type()
)
cpqDaPhyDrvSpinUpErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSpinUpErrs.setStatus("mandatory")
_CpqDaPhyDrvBadTargetErrs_Type = Counter32
_CpqDaPhyDrvBadTargetErrs_Object = MibTableColumn
cpqDaPhyDrvBadTargetErrs = _CpqDaPhyDrvBadTargetErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 43),
    _CpqDaPhyDrvBadTargetErrs_Type()
)
cpqDaPhyDrvBadTargetErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvBadTargetErrs.setStatus("mandatory")


class _CpqDaPhyDrvLocation_Type(Integer32):
    """Custom type cpqDaPhyDrvLocation based on Integer32"""
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
        *(("external", 3),
          ("internal", 2),
          ("other", 1),
          ("proLiant", 4))
    )


_CpqDaPhyDrvLocation_Type.__name__ = "Integer32"
_CpqDaPhyDrvLocation_Object = MibTableColumn
cpqDaPhyDrvLocation = _CpqDaPhyDrvLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 44),
    _CpqDaPhyDrvLocation_Type()
)
cpqDaPhyDrvLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvLocation.setStatus("deprecated")
_CpqDaPhyDrvSize_Type = Integer32
_CpqDaPhyDrvSize_Object = MibTableColumn
cpqDaPhyDrvSize = _CpqDaPhyDrvSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 45),
    _CpqDaPhyDrvSize_Type()
)
cpqDaPhyDrvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSize.setStatus("mandatory")
_CpqDaPhyDrvBusFaults_Type = Counter32
_CpqDaPhyDrvBusFaults_Object = MibTableColumn
cpqDaPhyDrvBusFaults = _CpqDaPhyDrvBusFaults_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 46),
    _CpqDaPhyDrvBusFaults_Type()
)
cpqDaPhyDrvBusFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvBusFaults.setStatus("mandatory")
_CpqDaPhyDrvIrqDeglitches_Type = Counter32
_CpqDaPhyDrvIrqDeglitches_Object = MibTableColumn
cpqDaPhyDrvIrqDeglitches = _CpqDaPhyDrvIrqDeglitches_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 47),
    _CpqDaPhyDrvIrqDeglitches_Type()
)
cpqDaPhyDrvIrqDeglitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvIrqDeglitches.setStatus("mandatory")


class _CpqDaPhyDrvHotPlug_Type(Integer32):
    """Custom type cpqDaPhyDrvHotPlug based on Integer32"""
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


_CpqDaPhyDrvHotPlug_Type.__name__ = "Integer32"
_CpqDaPhyDrvHotPlug_Object = MibTableColumn
cpqDaPhyDrvHotPlug = _CpqDaPhyDrvHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 48),
    _CpqDaPhyDrvHotPlug_Type()
)
cpqDaPhyDrvHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHotPlug.setStatus("mandatory")


class _CpqDaPhyDrvPlacement_Type(Integer32):
    """Custom type cpqDaPhyDrvPlacement based on Integer32"""
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


_CpqDaPhyDrvPlacement_Type.__name__ = "Integer32"
_CpqDaPhyDrvPlacement_Object = MibTableColumn
cpqDaPhyDrvPlacement = _CpqDaPhyDrvPlacement_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 49),
    _CpqDaPhyDrvPlacement_Type()
)
cpqDaPhyDrvPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPlacement.setStatus("mandatory")
_CpqDaPhyDrvBusNumber_Type = Integer32
_CpqDaPhyDrvBusNumber_Object = MibTableColumn
cpqDaPhyDrvBusNumber = _CpqDaPhyDrvBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 50),
    _CpqDaPhyDrvBusNumber_Type()
)
cpqDaPhyDrvBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvBusNumber.setStatus("mandatory")


class _CpqDaPhyDrvSerialNum_Type(DisplayString):
    """Custom type cpqDaPhyDrvSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CpqDaPhyDrvSerialNum_Type.__name__ = "DisplayString"
_CpqDaPhyDrvSerialNum_Object = MibTableColumn
cpqDaPhyDrvSerialNum = _CpqDaPhyDrvSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 51),
    _CpqDaPhyDrvSerialNum_Type()
)
cpqDaPhyDrvSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSerialNum.setStatus("mandatory")


class _CpqDaPhyDrvPreFailMonitoring_Type(Integer32):
    """Custom type cpqDaPhyDrvPreFailMonitoring based on Integer32"""
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


_CpqDaPhyDrvPreFailMonitoring_Type.__name__ = "Integer32"
_CpqDaPhyDrvPreFailMonitoring_Object = MibTableColumn
cpqDaPhyDrvPreFailMonitoring = _CpqDaPhyDrvPreFailMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 52),
    _CpqDaPhyDrvPreFailMonitoring_Type()
)
cpqDaPhyDrvPreFailMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPreFailMonitoring.setStatus("mandatory")


class _CpqDaPhyDrvCurrentWidth_Type(Integer32):
    """Custom type cpqDaPhyDrvCurrentWidth based on Integer32"""
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


_CpqDaPhyDrvCurrentWidth_Type.__name__ = "Integer32"
_CpqDaPhyDrvCurrentWidth_Object = MibTableColumn
cpqDaPhyDrvCurrentWidth = _CpqDaPhyDrvCurrentWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 53),
    _CpqDaPhyDrvCurrentWidth_Type()
)
cpqDaPhyDrvCurrentWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvCurrentWidth.setStatus("mandatory")


class _CpqDaPhyDrvCurrentSpeed_Type(Integer32):
    """Custom type cpqDaPhyDrvCurrentSpeed based on Integer32"""
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


_CpqDaPhyDrvCurrentSpeed_Type.__name__ = "Integer32"
_CpqDaPhyDrvCurrentSpeed_Object = MibTableColumn
cpqDaPhyDrvCurrentSpeed = _CpqDaPhyDrvCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 54),
    _CpqDaPhyDrvCurrentSpeed_Type()
)
cpqDaPhyDrvCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvCurrentSpeed.setStatus("mandatory")
_CpqDaPhyDrvFailureCode_Type = Integer32
_CpqDaPhyDrvFailureCode_Object = MibTableColumn
cpqDaPhyDrvFailureCode = _CpqDaPhyDrvFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 55),
    _CpqDaPhyDrvFailureCode_Type()
)
cpqDaPhyDrvFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvFailureCode.setStatus("mandatory")
_CpqDaPhyDrvBlinkTime_Type = Counter32
_CpqDaPhyDrvBlinkTime_Object = MibTableColumn
cpqDaPhyDrvBlinkTime = _CpqDaPhyDrvBlinkTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 56),
    _CpqDaPhyDrvBlinkTime_Type()
)
cpqDaPhyDrvBlinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqDaPhyDrvBlinkTime.setStatus("mandatory")


class _CpqDaPhyDrvSmartStatus_Type(Integer32):
    """Custom type cpqDaPhyDrvSmartStatus based on Integer32"""
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
          ("replaceDrive", 3),
          ("replaceDriveSSDWearOut", 4))
    )


_CpqDaPhyDrvSmartStatus_Type.__name__ = "Integer32"
_CpqDaPhyDrvSmartStatus_Object = MibTableColumn
cpqDaPhyDrvSmartStatus = _CpqDaPhyDrvSmartStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 57),
    _CpqDaPhyDrvSmartStatus_Type()
)
cpqDaPhyDrvSmartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSmartStatus.setStatus("mandatory")


class _CpqDaPhyDrvConfigurationStatus_Type(Integer32):
    """Custom type cpqDaPhyDrvConfigurationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("notConfigured", 3),
          ("other", 1))
    )


_CpqDaPhyDrvConfigurationStatus_Type.__name__ = "Integer32"
_CpqDaPhyDrvConfigurationStatus_Object = MibTableColumn
cpqDaPhyDrvConfigurationStatus = _CpqDaPhyDrvConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 58),
    _CpqDaPhyDrvConfigurationStatus_Type()
)
cpqDaPhyDrvConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvConfigurationStatus.setStatus("mandatory")


class _CpqDaPhyDrvRotationalSpeed_Type(Integer32):
    """Custom type cpqDaPhyDrvRotationalSpeed based on Integer32"""
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
          ("rpm10K", 3),
          ("rpm15K", 4),
          ("rpm7200", 2),
          ("rpmSsd", 5))
    )


_CpqDaPhyDrvRotationalSpeed_Type.__name__ = "Integer32"
_CpqDaPhyDrvRotationalSpeed_Object = MibTableColumn
cpqDaPhyDrvRotationalSpeed = _CpqDaPhyDrvRotationalSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 59),
    _CpqDaPhyDrvRotationalSpeed_Type()
)
cpqDaPhyDrvRotationalSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvRotationalSpeed.setStatus("mandatory")


class _CpqDaPhyDrvType_Type(Integer32):
    """Custom type cpqDaPhyDrvType based on Integer32"""
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


_CpqDaPhyDrvType_Type.__name__ = "Integer32"
_CpqDaPhyDrvType_Object = MibTableColumn
cpqDaPhyDrvType = _CpqDaPhyDrvType_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 60),
    _CpqDaPhyDrvType_Type()
)
cpqDaPhyDrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvType.setStatus("mandatory")


class _CpqDaPhyDrvSataVersion_Type(Integer32):
    """Custom type cpqDaPhyDrvSataVersion based on Integer32"""
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


_CpqDaPhyDrvSataVersion_Type.__name__ = "Integer32"
_CpqDaPhyDrvSataVersion_Object = MibTableColumn
cpqDaPhyDrvSataVersion = _CpqDaPhyDrvSataVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 61),
    _CpqDaPhyDrvSataVersion_Type()
)
cpqDaPhyDrvSataVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSataVersion.setStatus("mandatory")


class _CpqDaPhyDrvHostConnector_Type(DisplayString):
    """Custom type cpqDaPhyDrvHostConnector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CpqDaPhyDrvHostConnector_Type.__name__ = "DisplayString"
_CpqDaPhyDrvHostConnector_Object = MibTableColumn
cpqDaPhyDrvHostConnector = _CpqDaPhyDrvHostConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 62),
    _CpqDaPhyDrvHostConnector_Type()
)
cpqDaPhyDrvHostConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvHostConnector.setStatus("mandatory")
_CpqDaPhyDrvBoxOnConnector_Type = Integer32
_CpqDaPhyDrvBoxOnConnector_Object = MibTableColumn
cpqDaPhyDrvBoxOnConnector = _CpqDaPhyDrvBoxOnConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 63),
    _CpqDaPhyDrvBoxOnConnector_Type()
)
cpqDaPhyDrvBoxOnConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvBoxOnConnector.setStatus("mandatory")


class _CpqDaPhyDrvLocationString_Type(DisplayString):
    """Custom type cpqDaPhyDrvLocationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaPhyDrvLocationString_Type.__name__ = "DisplayString"
_CpqDaPhyDrvLocationString_Object = MibTableColumn
cpqDaPhyDrvLocationString = _CpqDaPhyDrvLocationString_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 64),
    _CpqDaPhyDrvLocationString_Type()
)
cpqDaPhyDrvLocationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvLocationString.setStatus("mandatory")


class _CpqDaPhyDrvNegotiatedLinkRate_Type(Integer32):
    """Custom type cpqDaPhyDrvNegotiatedLinkRate based on Integer32"""
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
          ("rate-1-5", 2),
          ("rate-12-0", 5),
          ("rate-3-0", 3),
          ("rate-6-0", 4))
    )


_CpqDaPhyDrvNegotiatedLinkRate_Type.__name__ = "Integer32"
_CpqDaPhyDrvNegotiatedLinkRate_Object = MibTableColumn
cpqDaPhyDrvNegotiatedLinkRate = _CpqDaPhyDrvNegotiatedLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 65),
    _CpqDaPhyDrvNegotiatedLinkRate_Type()
)
cpqDaPhyDrvNegotiatedLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvNegotiatedLinkRate.setStatus("mandatory")


class _CpqDaPhyDrvNcqSupport_Type(Integer32):
    """Custom type cpqDaPhyDrvNcqSupport based on Integer32"""
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
        *(("ncqDisabled", 4),
          ("ncqEnabled", 5),
          ("noControllerSupport", 2),
          ("noDriveSupport", 3),
          ("other", 1))
    )


_CpqDaPhyDrvNcqSupport_Type.__name__ = "Integer32"
_CpqDaPhyDrvNcqSupport_Object = MibTableColumn
cpqDaPhyDrvNcqSupport = _CpqDaPhyDrvNcqSupport_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 66),
    _CpqDaPhyDrvNcqSupport_Type()
)
cpqDaPhyDrvNcqSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvNcqSupport.setStatus("mandatory")
_CpqDaPhyDrvPhyCount_Type = Integer32
_CpqDaPhyDrvPhyCount_Object = MibTableColumn
cpqDaPhyDrvPhyCount = _CpqDaPhyDrvPhyCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 67),
    _CpqDaPhyDrvPhyCount_Type()
)
cpqDaPhyDrvPhyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPhyCount.setStatus("mandatory")


class _CpqDaPhyDrvMultipathAccess_Type(Integer32):
    """Custom type cpqDaPhyDrvMultipathAccess based on Integer32"""
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
        *(("driveFailed", 6),
          ("noRedundantPath", 5),
          ("notConfigured", 3),
          ("notSupported", 2),
          ("other", 1),
          ("pathRedundant", 4))
    )


_CpqDaPhyDrvMultipathAccess_Type.__name__ = "Integer32"
_CpqDaPhyDrvMultipathAccess_Object = MibTableColumn
cpqDaPhyDrvMultipathAccess = _CpqDaPhyDrvMultipathAccess_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 68),
    _CpqDaPhyDrvMultipathAccess_Type()
)
cpqDaPhyDrvMultipathAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvMultipathAccess.setStatus("mandatory")


class _CpqDaPhyDrvMediaType_Type(Integer32):
    """Custom type cpqDaPhyDrvMediaType based on Integer32"""
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
          ("rotatingPlatters", 2),
          ("solidState", 3))
    )


_CpqDaPhyDrvMediaType_Type.__name__ = "Integer32"
_CpqDaPhyDrvMediaType_Object = MibTableColumn
cpqDaPhyDrvMediaType = _CpqDaPhyDrvMediaType_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 69),
    _CpqDaPhyDrvMediaType_Type()
)
cpqDaPhyDrvMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvMediaType.setStatus("mandatory")
_CpqDaPhyDrvCurrentTemperature_Type = Integer32
_CpqDaPhyDrvCurrentTemperature_Object = MibTableColumn
cpqDaPhyDrvCurrentTemperature = _CpqDaPhyDrvCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 70),
    _CpqDaPhyDrvCurrentTemperature_Type()
)
cpqDaPhyDrvCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvCurrentTemperature.setStatus("mandatory")
_CpqDaPhyDrvTemperatureThreshold_Type = Integer32
_CpqDaPhyDrvTemperatureThreshold_Object = MibTableColumn
cpqDaPhyDrvTemperatureThreshold = _CpqDaPhyDrvTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 71),
    _CpqDaPhyDrvTemperatureThreshold_Type()
)
cpqDaPhyDrvTemperatureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvTemperatureThreshold.setStatus("mandatory")
_CpqDaPhyDrvMaximumTemperature_Type = Integer32
_CpqDaPhyDrvMaximumTemperature_Object = MibTableColumn
cpqDaPhyDrvMaximumTemperature = _CpqDaPhyDrvMaximumTemperature_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 72),
    _CpqDaPhyDrvMaximumTemperature_Type()
)
cpqDaPhyDrvMaximumTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvMaximumTemperature.setStatus("mandatory")


class _CpqDaPhyDrvSSDWearStatus_Type(Integer32):
    """Custom type cpqDaPhyDrvSSDWearStatus based on Integer32"""
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
        *(("fiftySixDayThreshold", 3),
          ("fivePercentThreshold", 4),
          ("ok", 2),
          ("other", 1),
          ("ssdWearOut", 6),
          ("twoPercentThreshold", 5))
    )


_CpqDaPhyDrvSSDWearStatus_Type.__name__ = "Integer32"
_CpqDaPhyDrvSSDWearStatus_Object = MibTableColumn
cpqDaPhyDrvSSDWearStatus = _CpqDaPhyDrvSSDWearStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 73),
    _CpqDaPhyDrvSSDWearStatus_Type()
)
cpqDaPhyDrvSSDWearStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSSDWearStatus.setStatus("mandatory")
_CpqDaPhyDrvPowerOnHours_Type = Counter32
_CpqDaPhyDrvPowerOnHours_Object = MibTableColumn
cpqDaPhyDrvPowerOnHours = _CpqDaPhyDrvPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 74),
    _CpqDaPhyDrvPowerOnHours_Type()
)
cpqDaPhyDrvPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPowerOnHours.setStatus("mandatory")
_CpqDaPhyDrvSSDPercntEndrnceUsed_Type = Gauge32
_CpqDaPhyDrvSSDPercntEndrnceUsed_Object = MibTableColumn
cpqDaPhyDrvSSDPercntEndrnceUsed = _CpqDaPhyDrvSSDPercntEndrnceUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 75),
    _CpqDaPhyDrvSSDPercntEndrnceUsed_Type()
)
cpqDaPhyDrvSSDPercntEndrnceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSSDPercntEndrnceUsed.setStatus("mandatory")
_CpqDaPhyDrvSSDEstTimeRemainingHours_Type = Counter32
_CpqDaPhyDrvSSDEstTimeRemainingHours_Object = MibTableColumn
cpqDaPhyDrvSSDEstTimeRemainingHours = _CpqDaPhyDrvSSDEstTimeRemainingHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 76),
    _CpqDaPhyDrvSSDEstTimeRemainingHours_Type()
)
cpqDaPhyDrvSSDEstTimeRemainingHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSSDEstTimeRemainingHours.setStatus("mandatory")


class _CpqDaPhyDrvAuthenticationStatus_Type(Integer32):
    """Custom type cpqDaPhyDrvAuthenticationStatus based on Integer32"""
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
        *(("authenticationFailed", 3),
          ("authenticationPassed", 4),
          ("notSupported", 2),
          ("other", 1))
    )


_CpqDaPhyDrvAuthenticationStatus_Type.__name__ = "Integer32"
_CpqDaPhyDrvAuthenticationStatus_Object = MibTableColumn
cpqDaPhyDrvAuthenticationStatus = _CpqDaPhyDrvAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 77),
    _CpqDaPhyDrvAuthenticationStatus_Type()
)
cpqDaPhyDrvAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvAuthenticationStatus.setStatus("mandatory")
_CpqDaPhyDrvSmartCarrierAppFWRev_Type = Integer32
_CpqDaPhyDrvSmartCarrierAppFWRev_Object = MibTableColumn
cpqDaPhyDrvSmartCarrierAppFWRev = _CpqDaPhyDrvSmartCarrierAppFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 78),
    _CpqDaPhyDrvSmartCarrierAppFWRev_Type()
)
cpqDaPhyDrvSmartCarrierAppFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSmartCarrierAppFWRev.setStatus("mandatory")
_CpqDaPhyDrvSmartCarrierBootldrFWRev_Type = Integer32
_CpqDaPhyDrvSmartCarrierBootldrFWRev_Object = MibTableColumn
cpqDaPhyDrvSmartCarrierBootldrFWRev = _CpqDaPhyDrvSmartCarrierBootldrFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 79),
    _CpqDaPhyDrvSmartCarrierBootldrFWRev_Type()
)
cpqDaPhyDrvSmartCarrierBootldrFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSmartCarrierBootldrFWRev.setStatus("mandatory")


class _CpqDaPhyDrvEncryptionStatus_Type(Integer32):
    """Custom type cpqDaPhyDrvEncryptionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 2),
          ("notEncrypted", 3),
          ("other", 1))
    )


_CpqDaPhyDrvEncryptionStatus_Type.__name__ = "Integer32"
_CpqDaPhyDrvEncryptionStatus_Object = MibTableColumn
cpqDaPhyDrvEncryptionStatus = _CpqDaPhyDrvEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 1, 1, 80),
    _CpqDaPhyDrvEncryptionStatus_Type()
)
cpqDaPhyDrvEncryptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvEncryptionStatus.setStatus("mandatory")
_CpqDaPhyDrvErrTable_Object = MibTable
cpqDaPhyDrvErrTable = _CpqDaPhyDrvErrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2)
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvErrTable.setStatus("mandatory")
_CpqDaPhyDrvErrEntry_Object = MibTableRow
cpqDaPhyDrvErrEntry = _CpqDaPhyDrvErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1)
)
cpqDaPhyDrvErrEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaPhyDrvErrCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaPhyDrvErrIDIndex"),
    (0, "CPQIDA-MIB", "cpqDaPhyDrvErrIndex"),
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvErrEntry.setStatus("mandatory")
_CpqDaPhyDrvErrCntlrIndex_Type = Integer32
_CpqDaPhyDrvErrCntlrIndex_Object = MibTableColumn
cpqDaPhyDrvErrCntlrIndex = _CpqDaPhyDrvErrCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 1),
    _CpqDaPhyDrvErrCntlrIndex_Type()
)
cpqDaPhyDrvErrCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvErrCntlrIndex.setStatus("mandatory")


class _CpqDaPhyDrvErrIDIndex_Type(Integer32):
    """Custom type cpqDaPhyDrvErrIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaPhyDrvErrIDIndex_Type.__name__ = "Integer32"
_CpqDaPhyDrvErrIDIndex_Object = MibTableColumn
cpqDaPhyDrvErrIDIndex = _CpqDaPhyDrvErrIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 2),
    _CpqDaPhyDrvErrIDIndex_Type()
)
cpqDaPhyDrvErrIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvErrIDIndex.setStatus("mandatory")


class _CpqDaPhyDrvErrIndex_Type(Integer32):
    """Custom type cpqDaPhyDrvErrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqDaPhyDrvErrIndex_Type.__name__ = "Integer32"
_CpqDaPhyDrvErrIndex_Object = MibTableColumn
cpqDaPhyDrvErrIndex = _CpqDaPhyDrvErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 3),
    _CpqDaPhyDrvErrIndex_Type()
)
cpqDaPhyDrvErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvErrIndex.setStatus("mandatory")


class _CpqDaPhyDrvErrType_Type(Integer32):
    """Custom type cpqDaPhyDrvErrType based on Integer32"""
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
        *(("camError", 4),
          ("noError", 2),
          ("other", 1),
          ("scsiError", 3))
    )


_CpqDaPhyDrvErrType_Type.__name__ = "Integer32"
_CpqDaPhyDrvErrType_Object = MibTableColumn
cpqDaPhyDrvErrType = _CpqDaPhyDrvErrType_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 4),
    _CpqDaPhyDrvErrType_Type()
)
cpqDaPhyDrvErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvErrType.setStatus("mandatory")


class _CpqDaPhyDrvScsiOp_Type(Integer32):
    """Custom type cpqDaPhyDrvScsiOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaPhyDrvScsiOp_Type.__name__ = "Integer32"
_CpqDaPhyDrvScsiOp_Object = MibTableColumn
cpqDaPhyDrvScsiOp = _CpqDaPhyDrvScsiOp_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 5),
    _CpqDaPhyDrvScsiOp_Type()
)
cpqDaPhyDrvScsiOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvScsiOp.setStatus("mandatory")


class _CpqDaPhyDrvScsiStatus_Type(Integer32):
    """Custom type cpqDaPhyDrvScsiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaPhyDrvScsiStatus_Type.__name__ = "Integer32"
_CpqDaPhyDrvScsiStatus_Object = MibTableColumn
cpqDaPhyDrvScsiStatus = _CpqDaPhyDrvScsiStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 6),
    _CpqDaPhyDrvScsiStatus_Type()
)
cpqDaPhyDrvScsiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvScsiStatus.setStatus("mandatory")


class _CpqDaPhyDrvCamStatus_Type(Integer32):
    """Custom type cpqDaPhyDrvCamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaPhyDrvCamStatus_Type.__name__ = "Integer32"
_CpqDaPhyDrvCamStatus_Object = MibTableColumn
cpqDaPhyDrvCamStatus = _CpqDaPhyDrvCamStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 7),
    _CpqDaPhyDrvCamStatus_Type()
)
cpqDaPhyDrvCamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvCamStatus.setStatus("mandatory")


class _CpqDaPhyDrvSenseKey_Type(Integer32):
    """Custom type cpqDaPhyDrvSenseKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaPhyDrvSenseKey_Type.__name__ = "Integer32"
_CpqDaPhyDrvSenseKey_Object = MibTableColumn
cpqDaPhyDrvSenseKey = _CpqDaPhyDrvSenseKey_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 8),
    _CpqDaPhyDrvSenseKey_Type()
)
cpqDaPhyDrvSenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSenseKey.setStatus("mandatory")


class _CpqDaPhyDrvQualifier_Type(Integer32):
    """Custom type cpqDaPhyDrvQualifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaPhyDrvQualifier_Type.__name__ = "Integer32"
_CpqDaPhyDrvQualifier_Object = MibTableColumn
cpqDaPhyDrvQualifier = _CpqDaPhyDrvQualifier_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 9),
    _CpqDaPhyDrvQualifier_Type()
)
cpqDaPhyDrvQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvQualifier.setStatus("mandatory")


class _CpqDaPhyDrvSenseCode_Type(Integer32):
    """Custom type cpqDaPhyDrvSenseCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaPhyDrvSenseCode_Type.__name__ = "Integer32"
_CpqDaPhyDrvSenseCode_Object = MibTableColumn
cpqDaPhyDrvSenseCode = _CpqDaPhyDrvSenseCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 10),
    _CpqDaPhyDrvSenseCode_Type()
)
cpqDaPhyDrvSenseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvSenseCode.setStatus("mandatory")


class _CpqDaPhyDrvBlockValid_Type(Integer32):
    """Custom type cpqDaPhyDrvBlockValid based on Integer32"""
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


_CpqDaPhyDrvBlockValid_Type.__name__ = "Integer32"
_CpqDaPhyDrvBlockValid_Object = MibTableColumn
cpqDaPhyDrvBlockValid = _CpqDaPhyDrvBlockValid_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 11),
    _CpqDaPhyDrvBlockValid_Type()
)
cpqDaPhyDrvBlockValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvBlockValid.setStatus("mandatory")
_CpqDaPhyDrvBlock_Type = Integer32
_CpqDaPhyDrvBlock_Object = MibTableColumn
cpqDaPhyDrvBlock = _CpqDaPhyDrvBlock_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 12),
    _CpqDaPhyDrvBlock_Type()
)
cpqDaPhyDrvBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvBlock.setStatus("mandatory")


class _CpqDaPhyDrvTime_Type(Integer32):
    """Custom type cpqDaPhyDrvTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqDaPhyDrvTime_Type.__name__ = "Integer32"
_CpqDaPhyDrvTime_Object = MibTableColumn
cpqDaPhyDrvTime = _CpqDaPhyDrvTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 13),
    _CpqDaPhyDrvTime_Type()
)
cpqDaPhyDrvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvTime.setStatus("mandatory")


class _CpqDaPhyDrvUserDesc_Type(DisplayString):
    """Custom type cpqDaPhyDrvUserDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaPhyDrvUserDesc_Type.__name__ = "DisplayString"
_CpqDaPhyDrvUserDesc_Object = MibTableColumn
cpqDaPhyDrvUserDesc = _CpqDaPhyDrvUserDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 14),
    _CpqDaPhyDrvUserDesc_Type()
)
cpqDaPhyDrvUserDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvUserDesc.setStatus("deprecated")


class _CpqDaPhyDrvErrDesc_Type(Integer32):
    """Custom type cpqDaPhyDrvErrDesc based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("camErrorOutOfRange", 13),
          ("commFailure", 2),
          ("compaqUpgradeRequired", 5),
          ("controllerFailure", 9),
          ("driveFailure", 1),
          ("driveIOError", 3),
          ("driveWriteProtected", 6),
          ("errorTypeOutOfRange", 14),
          ("internExternConflict", 10),
          ("internalDriveFailure", 11),
          ("invalidRequest", 7),
          ("scsiCommError", 4),
          ("scsiErrorOutOfRange", 12),
          ("scsiMessageError", 8))
    )


_CpqDaPhyDrvErrDesc_Type.__name__ = "Integer32"
_CpqDaPhyDrvErrDesc_Object = MibTableColumn
cpqDaPhyDrvErrDesc = _CpqDaPhyDrvErrDesc_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 2, 1, 15),
    _CpqDaPhyDrvErrDesc_Type()
)
cpqDaPhyDrvErrDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvErrDesc.setStatus("mandatory")
_CpqDaPhyDrvPathTable_Object = MibTable
cpqDaPhyDrvPathTable = _CpqDaPhyDrvPathTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 3)
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvPathTable.setStatus("mandatory")
_CpqDaPhyDrvPathEntry_Object = MibTableRow
cpqDaPhyDrvPathEntry = _CpqDaPhyDrvPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 3, 1)
)
cpqDaPhyDrvPathEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaPhyDrvPathCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaPhyDrvPathDrvIndex"),
    (0, "CPQIDA-MIB", "cpqDaPhyDrvPathIndex"),
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvPathEntry.setStatus("mandatory")
_CpqDaPhyDrvPathCntlrIndex_Type = Integer32
_CpqDaPhyDrvPathCntlrIndex_Object = MibTableColumn
cpqDaPhyDrvPathCntlrIndex = _CpqDaPhyDrvPathCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 3, 1, 1),
    _CpqDaPhyDrvPathCntlrIndex_Type()
)
cpqDaPhyDrvPathCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPathCntlrIndex.setStatus("mandatory")


class _CpqDaPhyDrvPathDrvIndex_Type(Integer32):
    """Custom type cpqDaPhyDrvPathDrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaPhyDrvPathDrvIndex_Type.__name__ = "Integer32"
_CpqDaPhyDrvPathDrvIndex_Object = MibTableColumn
cpqDaPhyDrvPathDrvIndex = _CpqDaPhyDrvPathDrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 3, 1, 2),
    _CpqDaPhyDrvPathDrvIndex_Type()
)
cpqDaPhyDrvPathDrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPathDrvIndex.setStatus("mandatory")


class _CpqDaPhyDrvPathIndex_Type(Integer32):
    """Custom type cpqDaPhyDrvPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CpqDaPhyDrvPathIndex_Type.__name__ = "Integer32"
_CpqDaPhyDrvPathIndex_Object = MibTableColumn
cpqDaPhyDrvPathIndex = _CpqDaPhyDrvPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 3, 1, 3),
    _CpqDaPhyDrvPathIndex_Type()
)
cpqDaPhyDrvPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPathIndex.setStatus("mandatory")


class _CpqDaPhyDrvPathStatus_Type(Integer32):
    """Custom type cpqDaPhyDrvPathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqDaPhyDrvPathStatus_Type.__name__ = "Integer32"
_CpqDaPhyDrvPathStatus_Object = MibTableColumn
cpqDaPhyDrvPathStatus = _CpqDaPhyDrvPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 3, 1, 4),
    _CpqDaPhyDrvPathStatus_Type()
)
cpqDaPhyDrvPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPathStatus.setStatus("mandatory")


class _CpqDaPhyDrvPathCurrentRole_Type(Integer32):
    """Custom type cpqDaPhyDrvPathCurrentRole based on Integer32"""
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
          ("alternate", 3),
          ("other", 1))
    )


_CpqDaPhyDrvPathCurrentRole_Type.__name__ = "Integer32"
_CpqDaPhyDrvPathCurrentRole_Object = MibTableColumn
cpqDaPhyDrvPathCurrentRole = _CpqDaPhyDrvPathCurrentRole_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 3, 1, 5),
    _CpqDaPhyDrvPathCurrentRole_Type()
)
cpqDaPhyDrvPathCurrentRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPathCurrentRole.setStatus("mandatory")


class _CpqDaPhyDrvPathHostConnector_Type(DisplayString):
    """Custom type cpqDaPhyDrvPathHostConnector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CpqDaPhyDrvPathHostConnector_Type.__name__ = "DisplayString"
_CpqDaPhyDrvPathHostConnector_Object = MibTableColumn
cpqDaPhyDrvPathHostConnector = _CpqDaPhyDrvPathHostConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 3, 1, 6),
    _CpqDaPhyDrvPathHostConnector_Type()
)
cpqDaPhyDrvPathHostConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPathHostConnector.setStatus("mandatory")
_CpqDaPhyDrvPathBoxOnConnector_Type = Integer32
_CpqDaPhyDrvPathBoxOnConnector_Object = MibTableColumn
cpqDaPhyDrvPathBoxOnConnector = _CpqDaPhyDrvPathBoxOnConnector_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 3, 1, 7),
    _CpqDaPhyDrvPathBoxOnConnector_Type()
)
cpqDaPhyDrvPathBoxOnConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPathBoxOnConnector.setStatus("mandatory")


class _CpqDaPhyDrvPathLocationString_Type(DisplayString):
    """Custom type cpqDaPhyDrvPathLocationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaPhyDrvPathLocationString_Type.__name__ = "DisplayString"
_CpqDaPhyDrvPathLocationString_Object = MibTableColumn
cpqDaPhyDrvPathLocationString = _CpqDaPhyDrvPathLocationString_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 5, 3, 1, 8),
    _CpqDaPhyDrvPathLocationString_Type()
)
cpqDaPhyDrvPathLocationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvPathLocationString.setStatus("mandatory")
_CpqDaPhyDrvThr_ObjectIdentity = ObjectIdentity
cpqDaPhyDrvThr = _CpqDaPhyDrvThr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6)
)
_CpqDaPhyDrvThrTable_Object = MibTable
cpqDaPhyDrvThrTable = _CpqDaPhyDrvThrTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrTable.setStatus("mandatory")
_CpqDaPhyDrvThrEntry_Object = MibTableRow
cpqDaPhyDrvThrEntry = _CpqDaPhyDrvThrEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1)
)
cpqDaPhyDrvThrEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaPhyDrvThrCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaPhyDrvThrIndex"),
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrEntry.setStatus("mandatory")
_CpqDaPhyDrvThrCntlrIndex_Type = Integer32
_CpqDaPhyDrvThrCntlrIndex_Object = MibTableColumn
cpqDaPhyDrvThrCntlrIndex = _CpqDaPhyDrvThrCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 1),
    _CpqDaPhyDrvThrCntlrIndex_Type()
)
cpqDaPhyDrvThrCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrCntlrIndex.setStatus("mandatory")


class _CpqDaPhyDrvThrIndex_Type(Integer32):
    """Custom type cpqDaPhyDrvThrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaPhyDrvThrIndex_Type.__name__ = "Integer32"
_CpqDaPhyDrvThrIndex_Object = MibTableColumn
cpqDaPhyDrvThrIndex = _CpqDaPhyDrvThrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 2),
    _CpqDaPhyDrvThrIndex_Type()
)
cpqDaPhyDrvThrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrIndex.setStatus("mandatory")
_CpqDaPhyDrvThrUsedReallocs_Type = Integer32
_CpqDaPhyDrvThrUsedReallocs_Object = MibTableColumn
cpqDaPhyDrvThrUsedReallocs = _CpqDaPhyDrvThrUsedReallocs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 3),
    _CpqDaPhyDrvThrUsedReallocs_Type()
)
cpqDaPhyDrvThrUsedReallocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrUsedReallocs.setStatus("mandatory")
_CpqDaPhyDrvThrRefHours_Type = Integer32
_CpqDaPhyDrvThrRefHours_Object = MibTableColumn
cpqDaPhyDrvThrRefHours = _CpqDaPhyDrvThrRefHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 4),
    _CpqDaPhyDrvThrRefHours_Type()
)
cpqDaPhyDrvThrRefHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrRefHours.setStatus("mandatory")
_CpqDaPhyDrvThrHardReadErrs_Type = Integer32
_CpqDaPhyDrvThrHardReadErrs_Object = MibTableColumn
cpqDaPhyDrvThrHardReadErrs = _CpqDaPhyDrvThrHardReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 5),
    _CpqDaPhyDrvThrHardReadErrs_Type()
)
cpqDaPhyDrvThrHardReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrHardReadErrs.setStatus("mandatory")
_CpqDaPhyDrvThrRecvReadErrs_Type = Integer32
_CpqDaPhyDrvThrRecvReadErrs_Object = MibTableColumn
cpqDaPhyDrvThrRecvReadErrs = _CpqDaPhyDrvThrRecvReadErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 6),
    _CpqDaPhyDrvThrRecvReadErrs_Type()
)
cpqDaPhyDrvThrRecvReadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrRecvReadErrs.setStatus("mandatory")
_CpqDaPhyDrvThrHardWriteErrs_Type = Integer32
_CpqDaPhyDrvThrHardWriteErrs_Object = MibTableColumn
cpqDaPhyDrvThrHardWriteErrs = _CpqDaPhyDrvThrHardWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 7),
    _CpqDaPhyDrvThrHardWriteErrs_Type()
)
cpqDaPhyDrvThrHardWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrHardWriteErrs.setStatus("mandatory")
_CpqDaPhyDrvThrRecvWriteErrs_Type = Integer32
_CpqDaPhyDrvThrRecvWriteErrs_Object = MibTableColumn
cpqDaPhyDrvThrRecvWriteErrs = _CpqDaPhyDrvThrRecvWriteErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 8),
    _CpqDaPhyDrvThrRecvWriteErrs_Type()
)
cpqDaPhyDrvThrRecvWriteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrRecvWriteErrs.setStatus("mandatory")
_CpqDaPhyDrvThrHSeekErrs_Type = Integer32
_CpqDaPhyDrvThrHSeekErrs_Object = MibTableColumn
cpqDaPhyDrvThrHSeekErrs = _CpqDaPhyDrvThrHSeekErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 9),
    _CpqDaPhyDrvThrHSeekErrs_Type()
)
cpqDaPhyDrvThrHSeekErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrHSeekErrs.setStatus("mandatory")
_CpqDaPhyDrvThrSeekErrs_Type = Integer32
_CpqDaPhyDrvThrSeekErrs_Object = MibTableColumn
cpqDaPhyDrvThrSeekErrs = _CpqDaPhyDrvThrSeekErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 10),
    _CpqDaPhyDrvThrSeekErrs_Type()
)
cpqDaPhyDrvThrSeekErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrSeekErrs.setStatus("mandatory")
_CpqDaPhyDrvThrSpinupTime_Type = Integer32
_CpqDaPhyDrvThrSpinupTime_Object = MibTableColumn
cpqDaPhyDrvThrSpinupTime = _CpqDaPhyDrvThrSpinupTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 11),
    _CpqDaPhyDrvThrSpinupTime_Type()
)
cpqDaPhyDrvThrSpinupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrSpinupTime.setStatus("mandatory")
_CpqDaPhyDrvThrFunctTest1_Type = Integer32
_CpqDaPhyDrvThrFunctTest1_Object = MibTableColumn
cpqDaPhyDrvThrFunctTest1 = _CpqDaPhyDrvThrFunctTest1_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 12),
    _CpqDaPhyDrvThrFunctTest1_Type()
)
cpqDaPhyDrvThrFunctTest1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrFunctTest1.setStatus("deprecated")
_CpqDaPhyDrvThrFunctTest2_Type = Integer32
_CpqDaPhyDrvThrFunctTest2_Object = MibTableColumn
cpqDaPhyDrvThrFunctTest2 = _CpqDaPhyDrvThrFunctTest2_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 13),
    _CpqDaPhyDrvThrFunctTest2_Type()
)
cpqDaPhyDrvThrFunctTest2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrFunctTest2.setStatus("deprecated")
_CpqDaPhyDrvThrFunctTest3_Type = Integer32
_CpqDaPhyDrvThrFunctTest3_Object = MibTableColumn
cpqDaPhyDrvThrFunctTest3 = _CpqDaPhyDrvThrFunctTest3_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 14),
    _CpqDaPhyDrvThrFunctTest3_Type()
)
cpqDaPhyDrvThrFunctTest3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrFunctTest3.setStatus("deprecated")
_CpqDaPhyDrvThrDrqTimeouts_Type = Integer32
_CpqDaPhyDrvThrDrqTimeouts_Object = MibTableColumn
cpqDaPhyDrvThrDrqTimeouts = _CpqDaPhyDrvThrDrqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 15),
    _CpqDaPhyDrvThrDrqTimeouts_Type()
)
cpqDaPhyDrvThrDrqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrDrqTimeouts.setStatus("mandatory")
_CpqDaPhyDrvThrOtherTimeouts_Type = Integer32
_CpqDaPhyDrvThrOtherTimeouts_Object = MibTableColumn
cpqDaPhyDrvThrOtherTimeouts = _CpqDaPhyDrvThrOtherTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 16),
    _CpqDaPhyDrvThrOtherTimeouts_Type()
)
cpqDaPhyDrvThrOtherTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrOtherTimeouts.setStatus("mandatory")
_CpqDaPhyDrvThrSpinupRetries_Type = Integer32
_CpqDaPhyDrvThrSpinupRetries_Object = MibTableColumn
cpqDaPhyDrvThrSpinupRetries = _CpqDaPhyDrvThrSpinupRetries_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 17),
    _CpqDaPhyDrvThrSpinupRetries_Type()
)
cpqDaPhyDrvThrSpinupRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrSpinupRetries.setStatus("mandatory")
_CpqDaPhyDrvThrBadRecvReads_Type = Integer32
_CpqDaPhyDrvThrBadRecvReads_Object = MibTableColumn
cpqDaPhyDrvThrBadRecvReads = _CpqDaPhyDrvThrBadRecvReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 18),
    _CpqDaPhyDrvThrBadRecvReads_Type()
)
cpqDaPhyDrvThrBadRecvReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrBadRecvReads.setStatus("mandatory")
_CpqDaPhyDrvThrBadRecvWrites_Type = Integer32
_CpqDaPhyDrvThrBadRecvWrites_Object = MibTableColumn
cpqDaPhyDrvThrBadRecvWrites = _CpqDaPhyDrvThrBadRecvWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 19),
    _CpqDaPhyDrvThrBadRecvWrites_Type()
)
cpqDaPhyDrvThrBadRecvWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrBadRecvWrites.setStatus("mandatory")
_CpqDaPhyDrvThrFormatErrs_Type = Integer32
_CpqDaPhyDrvThrFormatErrs_Object = MibTableColumn
cpqDaPhyDrvThrFormatErrs = _CpqDaPhyDrvThrFormatErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 20),
    _CpqDaPhyDrvThrFormatErrs_Type()
)
cpqDaPhyDrvThrFormatErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrFormatErrs.setStatus("mandatory")
_CpqDaPhyDrvThrPostErrs_Type = Integer32
_CpqDaPhyDrvThrPostErrs_Object = MibTableColumn
cpqDaPhyDrvThrPostErrs = _CpqDaPhyDrvThrPostErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 21),
    _CpqDaPhyDrvThrPostErrs_Type()
)
cpqDaPhyDrvThrPostErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrPostErrs.setStatus("mandatory")
_CpqDaPhyDrvThrNotReadyErrs_Type = Integer32
_CpqDaPhyDrvThrNotReadyErrs_Object = MibTableColumn
cpqDaPhyDrvThrNotReadyErrs = _CpqDaPhyDrvThrNotReadyErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 22),
    _CpqDaPhyDrvThrNotReadyErrs_Type()
)
cpqDaPhyDrvThrNotReadyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrNotReadyErrs.setStatus("mandatory")
_CpqDaPhyDrvThrReallocAborts_Type = Integer32
_CpqDaPhyDrvThrReallocAborts_Object = MibTableColumn
cpqDaPhyDrvThrReallocAborts = _CpqDaPhyDrvThrReallocAborts_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 23),
    _CpqDaPhyDrvThrReallocAborts_Type()
)
cpqDaPhyDrvThrReallocAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrReallocAborts.setStatus("mandatory")
_CpqDaPhyDrvThrHotPlugs_Type = Integer32
_CpqDaPhyDrvThrHotPlugs_Object = MibTableColumn
cpqDaPhyDrvThrHotPlugs = _CpqDaPhyDrvThrHotPlugs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 24),
    _CpqDaPhyDrvThrHotPlugs_Type()
)
cpqDaPhyDrvThrHotPlugs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrHotPlugs.setStatus("mandatory")
_CpqDaPhyDrvThrMediaErrs_Type = Integer32
_CpqDaPhyDrvThrMediaErrs_Object = MibTableColumn
cpqDaPhyDrvThrMediaErrs = _CpqDaPhyDrvThrMediaErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 25),
    _CpqDaPhyDrvThrMediaErrs_Type()
)
cpqDaPhyDrvThrMediaErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrMediaErrs.setStatus("mandatory")
_CpqDaPhyDrvThrHardwareErrs_Type = Integer32
_CpqDaPhyDrvThrHardwareErrs_Object = MibTableColumn
cpqDaPhyDrvThrHardwareErrs = _CpqDaPhyDrvThrHardwareErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 26),
    _CpqDaPhyDrvThrHardwareErrs_Type()
)
cpqDaPhyDrvThrHardwareErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrHardwareErrs.setStatus("mandatory")
_CpqDaPhyDrvThrAbortedCmds_Type = Integer32
_CpqDaPhyDrvThrAbortedCmds_Object = MibTableColumn
cpqDaPhyDrvThrAbortedCmds = _CpqDaPhyDrvThrAbortedCmds_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 27),
    _CpqDaPhyDrvThrAbortedCmds_Type()
)
cpqDaPhyDrvThrAbortedCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrAbortedCmds.setStatus("mandatory")
_CpqDaPhyDrvThrSpinUpErrs_Type = Integer32
_CpqDaPhyDrvThrSpinUpErrs_Object = MibTableColumn
cpqDaPhyDrvThrSpinUpErrs = _CpqDaPhyDrvThrSpinUpErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 28),
    _CpqDaPhyDrvThrSpinUpErrs_Type()
)
cpqDaPhyDrvThrSpinUpErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrSpinUpErrs.setStatus("mandatory")
_CpqDaPhyDrvThrBadTargetErrs_Type = Integer32
_CpqDaPhyDrvThrBadTargetErrs_Object = MibTableColumn
cpqDaPhyDrvThrBadTargetErrs = _CpqDaPhyDrvThrBadTargetErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 29),
    _CpqDaPhyDrvThrBadTargetErrs_Type()
)
cpqDaPhyDrvThrBadTargetErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrBadTargetErrs.setStatus("mandatory")


class _CpqDaPhyDrvThrViUsedReallocs_Type(Integer32):
    """Custom type cpqDaPhyDrvThrViUsedReallocs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4294967295)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 4294967295))
    )


_CpqDaPhyDrvThrViUsedReallocs_Type.__name__ = "Integer32"
_CpqDaPhyDrvThrViUsedReallocs_Object = MibTableColumn
cpqDaPhyDrvThrViUsedReallocs = _CpqDaPhyDrvThrViUsedReallocs_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 30),
    _CpqDaPhyDrvThrViUsedReallocs_Type()
)
cpqDaPhyDrvThrViUsedReallocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrViUsedReallocs.setStatus("mandatory")


class _CpqDaPhyDrvThrViSpinupTime_Type(Integer32):
    """Custom type cpqDaPhyDrvThrViSpinupTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4294967295)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 4294967295))
    )


_CpqDaPhyDrvThrViSpinupTime_Type.__name__ = "Integer32"
_CpqDaPhyDrvThrViSpinupTime_Object = MibTableColumn
cpqDaPhyDrvThrViSpinupTime = _CpqDaPhyDrvThrViSpinupTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 31),
    _CpqDaPhyDrvThrViSpinupTime_Type()
)
cpqDaPhyDrvThrViSpinupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrViSpinupTime.setStatus("mandatory")


class _CpqDaPhyDrvThrViFunctTest1_Type(Integer32):
    """Custom type cpqDaPhyDrvThrViFunctTest1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4294967295)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 4294967295))
    )


_CpqDaPhyDrvThrViFunctTest1_Type.__name__ = "Integer32"
_CpqDaPhyDrvThrViFunctTest1_Object = MibTableColumn
cpqDaPhyDrvThrViFunctTest1 = _CpqDaPhyDrvThrViFunctTest1_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 32),
    _CpqDaPhyDrvThrViFunctTest1_Type()
)
cpqDaPhyDrvThrViFunctTest1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrViFunctTest1.setStatus("mandatory")


class _CpqDaPhyDrvThrViFunctTest2_Type(Integer32):
    """Custom type cpqDaPhyDrvThrViFunctTest2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4294967295)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 4294967295))
    )


_CpqDaPhyDrvThrViFunctTest2_Type.__name__ = "Integer32"
_CpqDaPhyDrvThrViFunctTest2_Object = MibTableColumn
cpqDaPhyDrvThrViFunctTest2 = _CpqDaPhyDrvThrViFunctTest2_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 33),
    _CpqDaPhyDrvThrViFunctTest2_Type()
)
cpqDaPhyDrvThrViFunctTest2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrViFunctTest2.setStatus("mandatory")


class _CpqDaPhyDrvThrViFunctTest3_Type(Integer32):
    """Custom type cpqDaPhyDrvThrViFunctTest3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4294967295)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2),
          ("unknown", 4294967295))
    )


_CpqDaPhyDrvThrViFunctTest3_Type.__name__ = "Integer32"
_CpqDaPhyDrvThrViFunctTest3_Object = MibTableColumn
cpqDaPhyDrvThrViFunctTest3 = _CpqDaPhyDrvThrViFunctTest3_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 34),
    _CpqDaPhyDrvThrViFunctTest3_Type()
)
cpqDaPhyDrvThrViFunctTest3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrViFunctTest3.setStatus("mandatory")
_CpqDaPhyDrvThrBusFaults_Type = Integer32
_CpqDaPhyDrvThrBusFaults_Object = MibTableColumn
cpqDaPhyDrvThrBusFaults = _CpqDaPhyDrvThrBusFaults_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 35),
    _CpqDaPhyDrvThrBusFaults_Type()
)
cpqDaPhyDrvThrBusFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrBusFaults.setStatus("mandatory")
_CpqDaPhyDrvThrIrqDeglitches_Type = Integer32
_CpqDaPhyDrvThrIrqDeglitches_Object = MibTableColumn
cpqDaPhyDrvThrIrqDeglitches = _CpqDaPhyDrvThrIrqDeglitches_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 6, 1, 1, 36),
    _CpqDaPhyDrvThrIrqDeglitches_Type()
)
cpqDaPhyDrvThrIrqDeglitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaPhyDrvThrIrqDeglitches.setStatus("mandatory")
_CpqDaCntlrPerf_ObjectIdentity = ObjectIdentity
cpqDaCntlrPerf = _CpqDaCntlrPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 7)
)
_CpqDaCntlrPerfTable_Object = MibTable
cpqDaCntlrPerfTable = _CpqDaCntlrPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 7, 1)
)
if mibBuilder.loadTexts:
    cpqDaCntlrPerfTable.setStatus("mandatory")
_CpqDaCntlrPerfEntry_Object = MibTableRow
cpqDaCntlrPerfEntry = _CpqDaCntlrPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 7, 1, 1)
)
cpqDaCntlrPerfEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaCntlrPerfCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaCntlrPerfInstance"),
)
if mibBuilder.loadTexts:
    cpqDaCntlrPerfEntry.setStatus("mandatory")
_CpqDaCntlrPerfCntlrIndex_Type = Integer32
_CpqDaCntlrPerfCntlrIndex_Object = MibTableColumn
cpqDaCntlrPerfCntlrIndex = _CpqDaCntlrPerfCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 7, 1, 1, 1),
    _CpqDaCntlrPerfCntlrIndex_Type()
)
cpqDaCntlrPerfCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPerfCntlrIndex.setStatus("mandatory")
_CpqDaCntlrPerfInstance_Type = Integer32
_CpqDaCntlrPerfInstance_Object = MibTableColumn
cpqDaCntlrPerfInstance = _CpqDaCntlrPerfInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 7, 1, 1, 2),
    _CpqDaCntlrPerfInstance_Type()
)
cpqDaCntlrPerfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPerfInstance.setStatus("mandatory")
_CpqDaCntlrPerfSampleInterval_Type = Integer32
_CpqDaCntlrPerfSampleInterval_Object = MibTableColumn
cpqDaCntlrPerfSampleInterval = _CpqDaCntlrPerfSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 7, 1, 1, 3),
    _CpqDaCntlrPerfSampleInterval_Type()
)
cpqDaCntlrPerfSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPerfSampleInterval.setStatus("mandatory")
_CpqDaCntlrPerfVersion_Type = Integer32
_CpqDaCntlrPerfVersion_Object = MibTableColumn
cpqDaCntlrPerfVersion = _CpqDaCntlrPerfVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 7, 1, 1, 4),
    _CpqDaCntlrPerfVersion_Type()
)
cpqDaCntlrPerfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPerfVersion.setStatus("mandatory")
_CpqDaCntlrPerfCpuPercentBusy_Type = Integer32
_CpqDaCntlrPerfCpuPercentBusy_Object = MibTableColumn
cpqDaCntlrPerfCpuPercentBusy = _CpqDaCntlrPerfCpuPercentBusy_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 7, 1, 1, 5),
    _CpqDaCntlrPerfCpuPercentBusy_Type()
)
cpqDaCntlrPerfCpuPercentBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPerfCpuPercentBusy.setStatus("mandatory")
_CpqDaCntlrPerfCommandCount_Type = Integer32
_CpqDaCntlrPerfCommandCount_Object = MibTableColumn
cpqDaCntlrPerfCommandCount = _CpqDaCntlrPerfCommandCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 7, 1, 1, 6),
    _CpqDaCntlrPerfCommandCount_Type()
)
cpqDaCntlrPerfCommandCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPerfCommandCount.setStatus("mandatory")
_CpqDaCntlrPerfAvgLatency_Type = Integer32
_CpqDaCntlrPerfAvgLatency_Object = MibTableColumn
cpqDaCntlrPerfAvgLatency = _CpqDaCntlrPerfAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 7, 1, 1, 7),
    _CpqDaCntlrPerfAvgLatency_Type()
)
cpqDaCntlrPerfAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaCntlrPerfAvgLatency.setStatus("mandatory")
_CpqDaLogDrvPerf_ObjectIdentity = ObjectIdentity
cpqDaLogDrvPerf = _CpqDaLogDrvPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8)
)
_CpqDaLogDrvPerfTable_Object = MibTable
cpqDaLogDrvPerfTable = _CpqDaLogDrvPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1)
)
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfTable.setStatus("mandatory")
_CpqDaLogDrvPerfEntry_Object = MibTableRow
cpqDaLogDrvPerfEntry = _CpqDaLogDrvPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1)
)
cpqDaLogDrvPerfEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaLogDrvPerfCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaLogDrvPerfIndex"),
    (0, "CPQIDA-MIB", "cpqDaLogDrvPerfInstance"),
)
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfEntry.setStatus("mandatory")
_CpqDaLogDrvPerfCntlrIndex_Type = Integer32
_CpqDaLogDrvPerfCntlrIndex_Object = MibTableColumn
cpqDaLogDrvPerfCntlrIndex = _CpqDaLogDrvPerfCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 1),
    _CpqDaLogDrvPerfCntlrIndex_Type()
)
cpqDaLogDrvPerfCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfCntlrIndex.setStatus("mandatory")


class _CpqDaLogDrvPerfIndex_Type(Integer32):
    """Custom type cpqDaLogDrvPerfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaLogDrvPerfIndex_Type.__name__ = "Integer32"
_CpqDaLogDrvPerfIndex_Object = MibTableColumn
cpqDaLogDrvPerfIndex = _CpqDaLogDrvPerfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 2),
    _CpqDaLogDrvPerfIndex_Type()
)
cpqDaLogDrvPerfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfIndex.setStatus("mandatory")
_CpqDaLogDrvPerfInstance_Type = Integer32
_CpqDaLogDrvPerfInstance_Object = MibTableColumn
cpqDaLogDrvPerfInstance = _CpqDaLogDrvPerfInstance_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 3),
    _CpqDaLogDrvPerfInstance_Type()
)
cpqDaLogDrvPerfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfInstance.setStatus("mandatory")
_CpqDaLogDrvPerfSampleInterval_Type = Integer32
_CpqDaLogDrvPerfSampleInterval_Object = MibTableColumn
cpqDaLogDrvPerfSampleInterval = _CpqDaLogDrvPerfSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 4),
    _CpqDaLogDrvPerfSampleInterval_Type()
)
cpqDaLogDrvPerfSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfSampleInterval.setStatus("mandatory")
_CpqDaLogDrvPerfAvgQueueDepth_Type = Integer32
_CpqDaLogDrvPerfAvgQueueDepth_Object = MibTableColumn
cpqDaLogDrvPerfAvgQueueDepth = _CpqDaLogDrvPerfAvgQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 5),
    _CpqDaLogDrvPerfAvgQueueDepth_Type()
)
cpqDaLogDrvPerfAvgQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfAvgQueueDepth.setStatus("mandatory")
_CpqDaLogDrvPerfReads_Type = Integer32
_CpqDaLogDrvPerfReads_Object = MibTableColumn
cpqDaLogDrvPerfReads = _CpqDaLogDrvPerfReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 6),
    _CpqDaLogDrvPerfReads_Type()
)
cpqDaLogDrvPerfReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfReads.setStatus("mandatory")
_CpqDaLogDrvPerfWrites_Type = Integer32
_CpqDaLogDrvPerfWrites_Object = MibTableColumn
cpqDaLogDrvPerfWrites = _CpqDaLogDrvPerfWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 7),
    _CpqDaLogDrvPerfWrites_Type()
)
cpqDaLogDrvPerfWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfWrites.setStatus("mandatory")
_CpqDaLogDrvPerfTotalIO_Type = Integer32
_CpqDaLogDrvPerfTotalIO_Object = MibTableColumn
cpqDaLogDrvPerfTotalIO = _CpqDaLogDrvPerfTotalIO_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 8),
    _CpqDaLogDrvPerfTotalIO_Type()
)
cpqDaLogDrvPerfTotalIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfTotalIO.setStatus("mandatory")
_CpqDaLogDrvPerfCacheHits_Type = Integer32
_CpqDaLogDrvPerfCacheHits_Object = MibTableColumn
cpqDaLogDrvPerfCacheHits = _CpqDaLogDrvPerfCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 9),
    _CpqDaLogDrvPerfCacheHits_Type()
)
cpqDaLogDrvPerfCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfCacheHits.setStatus("mandatory")
_CpqDaLogDrvPerfCacheMisses_Type = Integer32
_CpqDaLogDrvPerfCacheMisses_Object = MibTableColumn
cpqDaLogDrvPerfCacheMisses = _CpqDaLogDrvPerfCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 10),
    _CpqDaLogDrvPerfCacheMisses_Type()
)
cpqDaLogDrvPerfCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfCacheMisses.setStatus("mandatory")
_CpqDaLogDrvPerfReadAheadSectors_Type = Integer32
_CpqDaLogDrvPerfReadAheadSectors_Object = MibTableColumn
cpqDaLogDrvPerfReadAheadSectors = _CpqDaLogDrvPerfReadAheadSectors_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 11),
    _CpqDaLogDrvPerfReadAheadSectors_Type()
)
cpqDaLogDrvPerfReadAheadSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfReadAheadSectors.setStatus("mandatory")
_CpqDaLogDrvPerfSectorsRead_Type = Integer32
_CpqDaLogDrvPerfSectorsRead_Object = MibTableColumn
cpqDaLogDrvPerfSectorsRead = _CpqDaLogDrvPerfSectorsRead_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 12),
    _CpqDaLogDrvPerfSectorsRead_Type()
)
cpqDaLogDrvPerfSectorsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfSectorsRead.setStatus("mandatory")
_CpqDaLogDrvPerfSectorsWritten_Type = Integer32
_CpqDaLogDrvPerfSectorsWritten_Object = MibTableColumn
cpqDaLogDrvPerfSectorsWritten = _CpqDaLogDrvPerfSectorsWritten_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 8, 1, 1, 13),
    _CpqDaLogDrvPerfSectorsWritten_Type()
)
cpqDaLogDrvPerfSectorsWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaLogDrvPerfSectorsWritten.setStatus("mandatory")
_CpqDaTapeDrv_ObjectIdentity = ObjectIdentity
cpqDaTapeDrv = _CpqDaTapeDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9)
)
_CpqDaTapeDrvTable_Object = MibTable
cpqDaTapeDrvTable = _CpqDaTapeDrvTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1)
)
if mibBuilder.loadTexts:
    cpqDaTapeDrvTable.setStatus("mandatory")
_CpqDaTapeDrvEntry_Object = MibTableRow
cpqDaTapeDrvEntry = _CpqDaTapeDrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1)
)
cpqDaTapeDrvEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaTapeDrvCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaTapeDrvBusIndex"),
    (0, "CPQIDA-MIB", "cpqDaTapeDrvScsiIdIndex"),
    (0, "CPQIDA-MIB", "cpqDaTapeDrvLunIndex"),
)
if mibBuilder.loadTexts:
    cpqDaTapeDrvEntry.setStatus("mandatory")
_CpqDaTapeDrvCntlrIndex_Type = Integer32
_CpqDaTapeDrvCntlrIndex_Object = MibTableColumn
cpqDaTapeDrvCntlrIndex = _CpqDaTapeDrvCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 1),
    _CpqDaTapeDrvCntlrIndex_Type()
)
cpqDaTapeDrvCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvCntlrIndex.setStatus("mandatory")


class _CpqDaTapeDrvBusIndex_Type(Integer32):
    """Custom type cpqDaTapeDrvBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaTapeDrvBusIndex_Type.__name__ = "Integer32"
_CpqDaTapeDrvBusIndex_Object = MibTableColumn
cpqDaTapeDrvBusIndex = _CpqDaTapeDrvBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 2),
    _CpqDaTapeDrvBusIndex_Type()
)
cpqDaTapeDrvBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvBusIndex.setStatus("mandatory")


class _CpqDaTapeDrvScsiIdIndex_Type(Integer32):
    """Custom type cpqDaTapeDrvScsiIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaTapeDrvScsiIdIndex_Type.__name__ = "Integer32"
_CpqDaTapeDrvScsiIdIndex_Object = MibTableColumn
cpqDaTapeDrvScsiIdIndex = _CpqDaTapeDrvScsiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 3),
    _CpqDaTapeDrvScsiIdIndex_Type()
)
cpqDaTapeDrvScsiIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvScsiIdIndex.setStatus("mandatory")


class _CpqDaTapeDrvLunIndex_Type(Integer32):
    """Custom type cpqDaTapeDrvLunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaTapeDrvLunIndex_Type.__name__ = "Integer32"
_CpqDaTapeDrvLunIndex_Object = MibTableColumn
cpqDaTapeDrvLunIndex = _CpqDaTapeDrvLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 4),
    _CpqDaTapeDrvLunIndex_Type()
)
cpqDaTapeDrvLunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvLunIndex.setStatus("mandatory")


class _CpqDaTapeDrvName_Type(DisplayString):
    """Custom type cpqDaTapeDrvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqDaTapeDrvName_Type.__name__ = "DisplayString"
_CpqDaTapeDrvName_Object = MibTableColumn
cpqDaTapeDrvName = _CpqDaTapeDrvName_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 5),
    _CpqDaTapeDrvName_Type()
)
cpqDaTapeDrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvName.setStatus("mandatory")


class _CpqDaTapeDrvSerialNumber_Type(DisplayString):
    """Custom type cpqDaTapeDrvSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqDaTapeDrvSerialNumber_Type.__name__ = "DisplayString"
_CpqDaTapeDrvSerialNumber_Object = MibTableColumn
cpqDaTapeDrvSerialNumber = _CpqDaTapeDrvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 6),
    _CpqDaTapeDrvSerialNumber_Type()
)
cpqDaTapeDrvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvSerialNumber.setStatus("mandatory")


class _CpqDaTapeDrvFwRev_Type(DisplayString):
    """Custom type cpqDaTapeDrvFwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqDaTapeDrvFwRev_Type.__name__ = "DisplayString"
_CpqDaTapeDrvFwRev_Object = MibTableColumn
cpqDaTapeDrvFwRev = _CpqDaTapeDrvFwRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 7),
    _CpqDaTapeDrvFwRev_Type()
)
cpqDaTapeDrvFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvFwRev.setStatus("mandatory")


class _CpqDaTapeDrvStatus_Type(Integer32):
    """Custom type cpqDaTapeDrvStatus based on Integer32"""
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


_CpqDaTapeDrvStatus_Type.__name__ = "Integer32"
_CpqDaTapeDrvStatus_Object = MibTableColumn
cpqDaTapeDrvStatus = _CpqDaTapeDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 8),
    _CpqDaTapeDrvStatus_Type()
)
cpqDaTapeDrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvStatus.setStatus("mandatory")
_CpqDaTapeDrvCondition_Type = Integer32
_CpqDaTapeDrvCondition_Object = MibTableColumn
cpqDaTapeDrvCondition = _CpqDaTapeDrvCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 9),
    _CpqDaTapeDrvCondition_Type()
)
cpqDaTapeDrvCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvCondition.setStatus("mandatory")


class _CpqDaTapeDrvFwSubtype_Type(Integer32):
    """Custom type cpqDaTapeDrvFwSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaTapeDrvFwSubtype_Type.__name__ = "Integer32"
_CpqDaTapeDrvFwSubtype_Object = MibTableColumn
cpqDaTapeDrvFwSubtype = _CpqDaTapeDrvFwSubtype_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 10),
    _CpqDaTapeDrvFwSubtype_Type()
)
cpqDaTapeDrvFwSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvFwSubtype.setStatus("mandatory")


class _CpqDaTapeDrvType_Type(Integer32):
    """Custom type cpqDaTapeDrvType based on Integer32"""
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
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("cpqAit35", 14),
          ("cpqAit50", 15),
          ("cpqDat12-24", 11),
          ("cpqDat2-8", 4),
          ("cpqDat20-40", 16),
          ("cpqDat4-16", 2),
          ("cpqDat4-8", 9),
          ("cpqDatAuto", 3),
          ("cpqDatAuto12-24", 12),
          ("cpqDatAuto20-40", 18),
          ("cpqDlt10-20", 5),
          ("cpqDlt15-30", 7),
          ("cpqDlt20-40", 6),
          ("cpqDlt35-70", 8),
          ("cpqDlt40-80", 17),
          ("cpqSlr4-8", 10),
          ("other", 1))
    )


_CpqDaTapeDrvType_Type.__name__ = "Integer32"
_CpqDaTapeDrvType_Object = MibTableColumn
cpqDaTapeDrvType = _CpqDaTapeDrvType_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 11),
    _CpqDaTapeDrvType_Type()
)
cpqDaTapeDrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvType.setStatus("mandatory")


class _CpqDaTapeDrvCleanReq_Type(Integer32):
    """Custom type cpqDaTapeDrvCleanReq based on Integer32"""
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


_CpqDaTapeDrvCleanReq_Type.__name__ = "Integer32"
_CpqDaTapeDrvCleanReq_Object = MibTableColumn
cpqDaTapeDrvCleanReq = _CpqDaTapeDrvCleanReq_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 12),
    _CpqDaTapeDrvCleanReq_Type()
)
cpqDaTapeDrvCleanReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvCleanReq.setStatus("mandatory")


class _CpqDaTapeDrvCleanTapeRepl_Type(Integer32):
    """Custom type cpqDaTapeDrvCleanTapeRepl based on Integer32"""
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


_CpqDaTapeDrvCleanTapeRepl_Type.__name__ = "Integer32"
_CpqDaTapeDrvCleanTapeRepl_Object = MibTableColumn
cpqDaTapeDrvCleanTapeRepl = _CpqDaTapeDrvCleanTapeRepl_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 13),
    _CpqDaTapeDrvCleanTapeRepl_Type()
)
cpqDaTapeDrvCleanTapeRepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvCleanTapeRepl.setStatus("mandatory")
_CpqDaTapeDrvCleanTapeCount_Type = Integer32
_CpqDaTapeDrvCleanTapeCount_Object = MibTableColumn
cpqDaTapeDrvCleanTapeCount = _CpqDaTapeDrvCleanTapeCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 14),
    _CpqDaTapeDrvCleanTapeCount_Type()
)
cpqDaTapeDrvCleanTapeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvCleanTapeCount.setStatus("mandatory")


class _CpqDaTapeDrvLibraryDrive_Type(Integer32):
    """Custom type cpqDaTapeDrvLibraryDrive based on Integer32"""
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


_CpqDaTapeDrvLibraryDrive_Type.__name__ = "Integer32"
_CpqDaTapeDrvLibraryDrive_Object = MibTableColumn
cpqDaTapeDrvLibraryDrive = _CpqDaTapeDrvLibraryDrive_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 15),
    _CpqDaTapeDrvLibraryDrive_Type()
)
cpqDaTapeDrvLibraryDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvLibraryDrive.setStatus("mandatory")
_CpqDaTapeDrvMagSize_Type = Integer32
_CpqDaTapeDrvMagSize_Object = MibTableColumn
cpqDaTapeDrvMagSize = _CpqDaTapeDrvMagSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 16),
    _CpqDaTapeDrvMagSize_Type()
)
cpqDaTapeDrvMagSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvMagSize.setStatus("mandatory")


class _CpqDaTapeDrvHotPlug_Type(Integer32):
    """Custom type cpqDaTapeDrvHotPlug based on Integer32"""
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


_CpqDaTapeDrvHotPlug_Type.__name__ = "Integer32"
_CpqDaTapeDrvHotPlug_Object = MibTableColumn
cpqDaTapeDrvHotPlug = _CpqDaTapeDrvHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 17),
    _CpqDaTapeDrvHotPlug_Type()
)
cpqDaTapeDrvHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvHotPlug.setStatus("mandatory")


class _CpqDaTapeDrvPlacement_Type(Integer32):
    """Custom type cpqDaTapeDrvPlacement based on Integer32"""
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


_CpqDaTapeDrvPlacement_Type.__name__ = "Integer32"
_CpqDaTapeDrvPlacement_Object = MibTableColumn
cpqDaTapeDrvPlacement = _CpqDaTapeDrvPlacement_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 18),
    _CpqDaTapeDrvPlacement_Type()
)
cpqDaTapeDrvPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvPlacement.setStatus("mandatory")


class _CpqDaTapeDrvCurrentWidth_Type(Integer32):
    """Custom type cpqDaTapeDrvCurrentWidth based on Integer32"""
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


_CpqDaTapeDrvCurrentWidth_Type.__name__ = "Integer32"
_CpqDaTapeDrvCurrentWidth_Object = MibTableColumn
cpqDaTapeDrvCurrentWidth = _CpqDaTapeDrvCurrentWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 19),
    _CpqDaTapeDrvCurrentWidth_Type()
)
cpqDaTapeDrvCurrentWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvCurrentWidth.setStatus("mandatory")


class _CpqDaTapeDrvCurrentSpeed_Type(Integer32):
    """Custom type cpqDaTapeDrvCurrentSpeed based on Integer32"""
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


_CpqDaTapeDrvCurrentSpeed_Type.__name__ = "Integer32"
_CpqDaTapeDrvCurrentSpeed_Object = MibTableColumn
cpqDaTapeDrvCurrentSpeed = _CpqDaTapeDrvCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 20),
    _CpqDaTapeDrvCurrentSpeed_Type()
)
cpqDaTapeDrvCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvCurrentSpeed.setStatus("mandatory")


class _CpqDaTapeDrvProtocol_Type(Integer32):
    """Custom type cpqDaTapeDrvProtocol based on Integer32"""
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


_CpqDaTapeDrvProtocol_Type.__name__ = "Integer32"
_CpqDaTapeDrvProtocol_Object = MibTableColumn
cpqDaTapeDrvProtocol = _CpqDaTapeDrvProtocol_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 21),
    _CpqDaTapeDrvProtocol_Type()
)
cpqDaTapeDrvProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvProtocol.setStatus("mandatory")


class _CpqDaTapeDrvNegotiatedLinkRate_Type(Integer32):
    """Custom type cpqDaTapeDrvNegotiatedLinkRate based on Integer32"""
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


_CpqDaTapeDrvNegotiatedLinkRate_Type.__name__ = "Integer32"
_CpqDaTapeDrvNegotiatedLinkRate_Object = MibTableColumn
cpqDaTapeDrvNegotiatedLinkRate = _CpqDaTapeDrvNegotiatedLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 9, 1, 1, 22),
    _CpqDaTapeDrvNegotiatedLinkRate_Type()
)
cpqDaTapeDrvNegotiatedLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeDrvNegotiatedLinkRate.setStatus("mandatory")
_CpqDaTapeCounters_ObjectIdentity = ObjectIdentity
cpqDaTapeCounters = _CpqDaTapeCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10)
)
_CpqDaTapeCountersTable_Object = MibTable
cpqDaTapeCountersTable = _CpqDaTapeCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1)
)
if mibBuilder.loadTexts:
    cpqDaTapeCountersTable.setStatus("mandatory")
_CpqDaTapeCountersEntry_Object = MibTableRow
cpqDaTapeCountersEntry = _CpqDaTapeCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1, 1)
)
cpqDaTapeCountersEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaTapeCountersCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaTapeCountersBusIndex"),
    (0, "CPQIDA-MIB", "cpqDaTapeCountersScsiIdIndex"),
    (0, "CPQIDA-MIB", "cpqDaTapeCountersLunIndex"),
)
if mibBuilder.loadTexts:
    cpqDaTapeCountersEntry.setStatus("mandatory")
_CpqDaTapeCountersCntlrIndex_Type = Integer32
_CpqDaTapeCountersCntlrIndex_Object = MibTableColumn
cpqDaTapeCountersCntlrIndex = _CpqDaTapeCountersCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1, 1, 1),
    _CpqDaTapeCountersCntlrIndex_Type()
)
cpqDaTapeCountersCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeCountersCntlrIndex.setStatus("mandatory")


class _CpqDaTapeCountersBusIndex_Type(Integer32):
    """Custom type cpqDaTapeCountersBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaTapeCountersBusIndex_Type.__name__ = "Integer32"
_CpqDaTapeCountersBusIndex_Object = MibTableColumn
cpqDaTapeCountersBusIndex = _CpqDaTapeCountersBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1, 1, 2),
    _CpqDaTapeCountersBusIndex_Type()
)
cpqDaTapeCountersBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeCountersBusIndex.setStatus("mandatory")


class _CpqDaTapeCountersScsiIdIndex_Type(Integer32):
    """Custom type cpqDaTapeCountersScsiIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaTapeCountersScsiIdIndex_Type.__name__ = "Integer32"
_CpqDaTapeCountersScsiIdIndex_Object = MibTableColumn
cpqDaTapeCountersScsiIdIndex = _CpqDaTapeCountersScsiIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1, 1, 3),
    _CpqDaTapeCountersScsiIdIndex_Type()
)
cpqDaTapeCountersScsiIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeCountersScsiIdIndex.setStatus("mandatory")


class _CpqDaTapeCountersLunIndex_Type(Integer32):
    """Custom type cpqDaTapeCountersLunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaTapeCountersLunIndex_Type.__name__ = "Integer32"
_CpqDaTapeCountersLunIndex_Object = MibTableColumn
cpqDaTapeCountersLunIndex = _CpqDaTapeCountersLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1, 1, 4),
    _CpqDaTapeCountersLunIndex_Type()
)
cpqDaTapeCountersLunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeCountersLunIndex.setStatus("mandatory")
_CpqDaTapeCountersReWrites_Type = Counter32
_CpqDaTapeCountersReWrites_Object = MibTableColumn
cpqDaTapeCountersReWrites = _CpqDaTapeCountersReWrites_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1, 1, 5),
    _CpqDaTapeCountersReWrites_Type()
)
cpqDaTapeCountersReWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeCountersReWrites.setStatus("mandatory")
_CpqDaTapeCountersReReads_Type = Counter32
_CpqDaTapeCountersReReads_Object = MibTableColumn
cpqDaTapeCountersReReads = _CpqDaTapeCountersReReads_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1, 1, 6),
    _CpqDaTapeCountersReReads_Type()
)
cpqDaTapeCountersReReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeCountersReReads.setStatus("mandatory")
_CpqDaTapeCountersTotalErrors_Type = Counter32
_CpqDaTapeCountersTotalErrors_Object = MibTableColumn
cpqDaTapeCountersTotalErrors = _CpqDaTapeCountersTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1, 1, 7),
    _CpqDaTapeCountersTotalErrors_Type()
)
cpqDaTapeCountersTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeCountersTotalErrors.setStatus("mandatory")
_CpqDaTapeCountersTotalUncorrectable_Type = Counter32
_CpqDaTapeCountersTotalUncorrectable_Object = MibTableColumn
cpqDaTapeCountersTotalUncorrectable = _CpqDaTapeCountersTotalUncorrectable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1, 1, 8),
    _CpqDaTapeCountersTotalUncorrectable_Type()
)
cpqDaTapeCountersTotalUncorrectable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeCountersTotalUncorrectable.setStatus("mandatory")
_CpqDaTapeCountersTotalBytes_Type = Counter32
_CpqDaTapeCountersTotalBytes_Object = MibTableColumn
cpqDaTapeCountersTotalBytes = _CpqDaTapeCountersTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 10, 1, 1, 9),
    _CpqDaTapeCountersTotalBytes_Type()
)
cpqDaTapeCountersTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeCountersTotalBytes.setStatus("mandatory")
_CpqDaTapeLibrary_ObjectIdentity = ObjectIdentity
cpqDaTapeLibrary = _CpqDaTapeLibrary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11)
)
_CpqDaTapeLibraryTable_Object = MibTable
cpqDaTapeLibraryTable = _CpqDaTapeLibraryTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1)
)
if mibBuilder.loadTexts:
    cpqDaTapeLibraryTable.setStatus("mandatory")
_CpqDaTapeLibraryEntry_Object = MibTableRow
cpqDaTapeLibraryEntry = _CpqDaTapeLibraryEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1)
)
cpqDaTapeLibraryEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaTapeLibraryCntlrIndex"),
    (0, "CPQIDA-MIB", "cpqDaTapeLibraryScsiBus"),
    (0, "CPQIDA-MIB", "cpqDaTapeLibraryScsiTarget"),
    (0, "CPQIDA-MIB", "cpqDaTapeLibraryScsiLun"),
)
if mibBuilder.loadTexts:
    cpqDaTapeLibraryEntry.setStatus("mandatory")
_CpqDaTapeLibraryCntlrIndex_Type = Integer32
_CpqDaTapeLibraryCntlrIndex_Object = MibTableColumn
cpqDaTapeLibraryCntlrIndex = _CpqDaTapeLibraryCntlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 1),
    _CpqDaTapeLibraryCntlrIndex_Type()
)
cpqDaTapeLibraryCntlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryCntlrIndex.setStatus("mandatory")


class _CpqDaTapeLibraryScsiBus_Type(Integer32):
    """Custom type cpqDaTapeLibraryScsiBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaTapeLibraryScsiBus_Type.__name__ = "Integer32"
_CpqDaTapeLibraryScsiBus_Object = MibTableColumn
cpqDaTapeLibraryScsiBus = _CpqDaTapeLibraryScsiBus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 2),
    _CpqDaTapeLibraryScsiBus_Type()
)
cpqDaTapeLibraryScsiBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryScsiBus.setStatus("mandatory")


class _CpqDaTapeLibraryScsiTarget_Type(Integer32):
    """Custom type cpqDaTapeLibraryScsiTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaTapeLibraryScsiTarget_Type.__name__ = "Integer32"
_CpqDaTapeLibraryScsiTarget_Object = MibTableColumn
cpqDaTapeLibraryScsiTarget = _CpqDaTapeLibraryScsiTarget_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 3),
    _CpqDaTapeLibraryScsiTarget_Type()
)
cpqDaTapeLibraryScsiTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryScsiTarget.setStatus("mandatory")


class _CpqDaTapeLibraryScsiLun_Type(Integer32):
    """Custom type cpqDaTapeLibraryScsiLun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqDaTapeLibraryScsiLun_Type.__name__ = "Integer32"
_CpqDaTapeLibraryScsiLun_Object = MibTableColumn
cpqDaTapeLibraryScsiLun = _CpqDaTapeLibraryScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 4),
    _CpqDaTapeLibraryScsiLun_Type()
)
cpqDaTapeLibraryScsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryScsiLun.setStatus("mandatory")


class _CpqDaTapeLibrarySerialNumber_Type(DisplayString):
    """Custom type cpqDaTapeLibrarySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpqDaTapeLibrarySerialNumber_Type.__name__ = "DisplayString"
_CpqDaTapeLibrarySerialNumber_Object = MibTableColumn
cpqDaTapeLibrarySerialNumber = _CpqDaTapeLibrarySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 5),
    _CpqDaTapeLibrarySerialNumber_Type()
)
cpqDaTapeLibrarySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibrarySerialNumber.setStatus("mandatory")


class _CpqDaTapeLibraryModel_Type(DisplayString):
    """Custom type cpqDaTapeLibraryModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqDaTapeLibraryModel_Type.__name__ = "DisplayString"
_CpqDaTapeLibraryModel_Object = MibTableColumn
cpqDaTapeLibraryModel = _CpqDaTapeLibraryModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 6),
    _CpqDaTapeLibraryModel_Type()
)
cpqDaTapeLibraryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryModel.setStatus("mandatory")


class _CpqDaTapeLibraryFWRev_Type(DisplayString):
    """Custom type cpqDaTapeLibraryFWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqDaTapeLibraryFWRev_Type.__name__ = "DisplayString"
_CpqDaTapeLibraryFWRev_Object = MibTableColumn
cpqDaTapeLibraryFWRev = _CpqDaTapeLibraryFWRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 7),
    _CpqDaTapeLibraryFWRev_Type()
)
cpqDaTapeLibraryFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryFWRev.setStatus("mandatory")


class _CpqDaTapeLibraryStatus_Type(Integer32):
    """Custom type cpqDaTapeLibraryStatus based on Integer32"""
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


_CpqDaTapeLibraryStatus_Type.__name__ = "Integer32"
_CpqDaTapeLibraryStatus_Object = MibTableColumn
cpqDaTapeLibraryStatus = _CpqDaTapeLibraryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 8),
    _CpqDaTapeLibraryStatus_Type()
)
cpqDaTapeLibraryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryStatus.setStatus("mandatory")


class _CpqDaTapeLibraryDoorStatus_Type(Integer32):
    """Custom type cpqDaTapeLibraryDoorStatus based on Integer32"""
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


_CpqDaTapeLibraryDoorStatus_Type.__name__ = "Integer32"
_CpqDaTapeLibraryDoorStatus_Object = MibTableColumn
cpqDaTapeLibraryDoorStatus = _CpqDaTapeLibraryDoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 9),
    _CpqDaTapeLibraryDoorStatus_Type()
)
cpqDaTapeLibraryDoorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryDoorStatus.setStatus("mandatory")
_CpqDaTapeLibraryCondition_Type = Integer32
_CpqDaTapeLibraryCondition_Object = MibTableColumn
cpqDaTapeLibraryCondition = _CpqDaTapeLibraryCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 10),
    _CpqDaTapeLibraryCondition_Type()
)
cpqDaTapeLibraryCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryCondition.setStatus("mandatory")
_CpqDaTapeLibraryOverallCondition_Type = Integer32
_CpqDaTapeLibraryOverallCondition_Object = MibTableColumn
cpqDaTapeLibraryOverallCondition = _CpqDaTapeLibraryOverallCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 11),
    _CpqDaTapeLibraryOverallCondition_Type()
)
cpqDaTapeLibraryOverallCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryOverallCondition.setStatus("mandatory")


class _CpqDaTapeLibraryLastError_Type(Integer32):
    """Custom type cpqDaTapeLibraryLastError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqDaTapeLibraryLastError_Type.__name__ = "Integer32"
_CpqDaTapeLibraryLastError_Object = MibTableColumn
cpqDaTapeLibraryLastError = _CpqDaTapeLibraryLastError_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 12),
    _CpqDaTapeLibraryLastError_Type()
)
cpqDaTapeLibraryLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryLastError.setStatus("deprecated")
_CpqDaTapeLibraryStatHours_Type = Counter32
_CpqDaTapeLibraryStatHours_Object = MibTableColumn
cpqDaTapeLibraryStatHours = _CpqDaTapeLibraryStatHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 13),
    _CpqDaTapeLibraryStatHours_Type()
)
cpqDaTapeLibraryStatHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryStatHours.setStatus("mandatory")
_CpqDaTapeLibraryStatMoves_Type = Counter32
_CpqDaTapeLibraryStatMoves_Object = MibTableColumn
cpqDaTapeLibraryStatMoves = _CpqDaTapeLibraryStatMoves_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 14),
    _CpqDaTapeLibraryStatMoves_Type()
)
cpqDaTapeLibraryStatMoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryStatMoves.setStatus("mandatory")


class _CpqDaTapeLibraryDriveList_Type(OctetString):
    """Custom type cpqDaTapeLibraryDriveList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_CpqDaTapeLibraryDriveList_Type.__name__ = "OctetString"
_CpqDaTapeLibraryDriveList_Object = MibTableColumn
cpqDaTapeLibraryDriveList = _CpqDaTapeLibraryDriveList_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 15),
    _CpqDaTapeLibraryDriveList_Type()
)
cpqDaTapeLibraryDriveList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryDriveList.setStatus("deprecated")


class _CpqDaTapeLibraryCurrentWidth_Type(Integer32):
    """Custom type cpqDaTapeLibraryCurrentWidth based on Integer32"""
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


_CpqDaTapeLibraryCurrentWidth_Type.__name__ = "Integer32"
_CpqDaTapeLibraryCurrentWidth_Object = MibTableColumn
cpqDaTapeLibraryCurrentWidth = _CpqDaTapeLibraryCurrentWidth_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 16),
    _CpqDaTapeLibraryCurrentWidth_Type()
)
cpqDaTapeLibraryCurrentWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryCurrentWidth.setStatus("mandatory")


class _CpqDaTapeLibraryCurrentSpeed_Type(Integer32):
    """Custom type cpqDaTapeLibraryCurrentSpeed based on Integer32"""
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


_CpqDaTapeLibraryCurrentSpeed_Type.__name__ = "Integer32"
_CpqDaTapeLibraryCurrentSpeed_Object = MibTableColumn
cpqDaTapeLibraryCurrentSpeed = _CpqDaTapeLibraryCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 17),
    _CpqDaTapeLibraryCurrentSpeed_Type()
)
cpqDaTapeLibraryCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryCurrentSpeed.setStatus("mandatory")


class _CpqDaTapeLibraryDriveList2_Type(OctetString):
    """Custom type cpqDaTapeLibraryDriveList2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqDaTapeLibraryDriveList2_Type.__name__ = "OctetString"
_CpqDaTapeLibraryDriveList2_Object = MibTableColumn
cpqDaTapeLibraryDriveList2 = _CpqDaTapeLibraryDriveList2_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 18),
    _CpqDaTapeLibraryDriveList2_Type()
)
cpqDaTapeLibraryDriveList2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryDriveList2.setStatus("mandatory")


class _CpqDaTapeLibraryProtocol_Type(Integer32):
    """Custom type cpqDaTapeLibraryProtocol based on Integer32"""
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


_CpqDaTapeLibraryProtocol_Type.__name__ = "Integer32"
_CpqDaTapeLibraryProtocol_Object = MibTableColumn
cpqDaTapeLibraryProtocol = _CpqDaTapeLibraryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 19),
    _CpqDaTapeLibraryProtocol_Type()
)
cpqDaTapeLibraryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryProtocol.setStatus("mandatory")


class _CpqDaTapeLibraryNegotiatedLinkRate_Type(Integer32):
    """Custom type cpqDaTapeLibraryNegotiatedLinkRate based on Integer32"""
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


_CpqDaTapeLibraryNegotiatedLinkRate_Type.__name__ = "Integer32"
_CpqDaTapeLibraryNegotiatedLinkRate_Object = MibTableColumn
cpqDaTapeLibraryNegotiatedLinkRate = _CpqDaTapeLibraryNegotiatedLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 2, 11, 1, 1, 20),
    _CpqDaTapeLibraryNegotiatedLinkRate_Type()
)
cpqDaTapeLibraryNegotiatedLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTapeLibraryNegotiatedLinkRate.setStatus("mandatory")
_CpqDaTrap_ObjectIdentity = ObjectIdentity
cpqDaTrap = _CpqDaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 3, 3)
)
_CpqDaTrapPkts_Type = Counter32
_CpqDaTrapPkts_Object = MibScalar
cpqDaTrapPkts = _CpqDaTrapPkts_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 3, 1),
    _CpqDaTrapPkts_Type()
)
cpqDaTrapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTrapPkts.setStatus("deprecated")


class _CpqDaTrapLogMaxSize_Type(Integer32):
    """Custom type cpqDaTrapLogMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqDaTrapLogMaxSize_Type.__name__ = "Integer32"
_CpqDaTrapLogMaxSize_Object = MibScalar
cpqDaTrapLogMaxSize = _CpqDaTrapLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 3, 2),
    _CpqDaTrapLogMaxSize_Type()
)
cpqDaTrapLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTrapLogMaxSize.setStatus("deprecated")
_CpqDaTrapLogTable_Object = MibTable
cpqDaTrapLogTable = _CpqDaTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 3, 3)
)
if mibBuilder.loadTexts:
    cpqDaTrapLogTable.setStatus("deprecated")
_CpqDaTrapLogEntry_Object = MibTableRow
cpqDaTrapLogEntry = _CpqDaTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 3, 3, 1)
)
cpqDaTrapLogEntry.setIndexNames(
    (0, "CPQIDA-MIB", "cpqDaTrapLogIndex"),
)
if mibBuilder.loadTexts:
    cpqDaTrapLogEntry.setStatus("deprecated")


class _CpqDaTrapLogIndex_Type(Integer32):
    """Custom type cpqDaTrapLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqDaTrapLogIndex_Type.__name__ = "Integer32"
_CpqDaTrapLogIndex_Object = MibTableColumn
cpqDaTrapLogIndex = _CpqDaTrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 3, 3, 1, 1),
    _CpqDaTrapLogIndex_Type()
)
cpqDaTrapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTrapLogIndex.setStatus("deprecated")


class _CpqDaTrapType_Type(Integer32):
    """Custom type cpqDaTrapType based on Integer32"""
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
              3001,
              3002,
              3003,
              3004,
              3005,
              3006,
              3007)
        )
    )
    namedValues = NamedValues(
        *(("cpqDa2AccelBadDataTrap", 3006),
          ("cpqDa2AccelBatteryFailed", 3007),
          ("cpqDa2AccelStatusChange", 3005),
          ("cpqDa2LogDrvStatusChange", 3001),
          ("cpqDa2PhyDrvStatusChange", 3003),
          ("cpqDa2PhyDrvThreshExceededTrap", 3004),
          ("cpqDa2SpareStatusChange", 3002),
          ("cpqDaAccelBadDataTrap", 6),
          ("cpqDaAccelBatteryFailed", 7),
          ("cpqDaAccelStatusChange", 5),
          ("cpqDaLogDrvStatusChange", 1),
          ("cpqDaPhyDrvStatusChange", 3),
          ("cpqDaPhyDrvThreshExceededTrap", 4),
          ("cpqDaSpareStatusChange", 2))
    )


_CpqDaTrapType_Type.__name__ = "Integer32"
_CpqDaTrapType_Object = MibTableColumn
cpqDaTrapType = _CpqDaTrapType_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 3, 3, 1, 2),
    _CpqDaTrapType_Type()
)
cpqDaTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTrapType.setStatus("deprecated")


class _CpqDaTrapTime_Type(OctetString):
    """Custom type cpqDaTrapTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CpqDaTrapTime_Type.__name__ = "OctetString"
_CpqDaTrapTime_Object = MibTableColumn
cpqDaTrapTime = _CpqDaTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 3, 3, 3, 1, 3),
    _CpqDaTrapTime_Type()
)
cpqDaTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqDaTrapTime.setStatus("deprecated")

# Managed Objects groups


# Notification objects

cpqDa2LogDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3001)
)
cpqDa2LogDrvStatusChange.setObjects(
    ("CPQIDA-MIB", "cpqDaLogDrvStatus")
)
if mibBuilder.loadTexts:
    cpqDa2LogDrvStatusChange.setStatus(
        ""
    )

cpqDa2SpareStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3002)
)
cpqDa2SpareStatusChange.setObjects(
      *(("CPQIDA-MIB", "cpqDaSpareStatus"),
        ("CPQIDA-MIB", "cpqDaSpareBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDa2SpareStatusChange.setStatus(
        ""
    )

cpqDa2PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3003)
)
cpqDa2PhyDrvStatusChange.setObjects(
      *(("CPQIDA-MIB", "cpqDaPhyDrvStatus"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDa2PhyDrvStatusChange.setStatus(
        ""
    )

cpqDa2PhyDrvThreshPassedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3004)
)
cpqDa2PhyDrvThreshPassedTrap.setObjects(
      *(("CPQIDA-MIB", "cpqDaPhyDrvThreshPassed"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDa2PhyDrvThreshPassedTrap.setStatus(
        ""
    )

cpqDa2AccelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3005)
)
cpqDa2AccelStatusChange.setObjects(
    ("CPQIDA-MIB", "cpqDaAccelStatus")
)
if mibBuilder.loadTexts:
    cpqDa2AccelStatusChange.setStatus(
        ""
    )

cpqDa2AccelBadDataTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3006)
)
cpqDa2AccelBadDataTrap.setObjects(
    ("CPQIDA-MIB", "cpqDaAccelBadData")
)
if mibBuilder.loadTexts:
    cpqDa2AccelBadDataTrap.setStatus(
        ""
    )

cpqDa2AccelBatteryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3007)
)
cpqDa2AccelBatteryFailed.setObjects(
    ("CPQIDA-MIB", "cpqDaAccelBattery")
)
if mibBuilder.loadTexts:
    cpqDa2AccelBatteryFailed.setStatus(
        ""
    )

cpqDa3LogDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3008)
)
cpqDa3LogDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaLogDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqDa3LogDrvStatusChange.setStatus(
        ""
    )

cpqDa3SpareStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3009)
)
cpqDa3SpareStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaSpareStatus"),
        ("CPQIDA-MIB", "cpqDaSpareBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDa3SpareStatusChange.setStatus(
        ""
    )

cpqDa3PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3010)
)
cpqDa3PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaPhyDrvStatus"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDa3PhyDrvStatusChange.setStatus(
        ""
    )

cpqDa3PhyDrvThreshPassedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3011)
)
cpqDa3PhyDrvThreshPassedTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaPhyDrvThreshPassed"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDa3PhyDrvThreshPassedTrap.setStatus(
        ""
    )

cpqDa3AccelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3012)
)
cpqDa3AccelStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaAccelStatus"))
)
if mibBuilder.loadTexts:
    cpqDa3AccelStatusChange.setStatus(
        ""
    )

cpqDa3AccelBadDataTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3013)
)
cpqDa3AccelBadDataTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaAccelBadData"))
)
if mibBuilder.loadTexts:
    cpqDa3AccelBadDataTrap.setStatus(
        ""
    )

cpqDa3AccelBatteryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3014)
)
cpqDa3AccelBatteryFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaAccelBattery"))
)
if mibBuilder.loadTexts:
    cpqDa3AccelBatteryFailed.setStatus(
        ""
    )

cpqDaCntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3015)
)
cpqDaCntlrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrSlot"),
        ("CPQIDA-MIB", "cpqDaCntlrBoardStatus"))
)
if mibBuilder.loadTexts:
    cpqDaCntlrStatusChange.setStatus(
        ""
    )

cpqDaCntlrActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3016)
)
cpqDaCntlrActive.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrSlot"),
        ("CPQIDA-MIB", "cpqDaCntlrPartnerSlot"))
)
if mibBuilder.loadTexts:
    cpqDaCntlrActive.setStatus(
        ""
    )

cpqDa4SpareStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3017)
)
cpqDa4SpareStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaSpareStatus"),
        ("CPQIDA-MIB", "cpqDaSpareCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaSpareBusNumber"),
        ("CPQIDA-MIB", "cpqDaSpareBay"))
)
if mibBuilder.loadTexts:
    cpqDa4SpareStatusChange.setStatus(
        ""
    )

cpqDa4PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3018)
)
cpqDa4PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaPhyDrvStatus"),
        ("CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBay"))
)
if mibBuilder.loadTexts:
    cpqDa4PhyDrvStatusChange.setStatus(
        ""
    )

cpqDa4PhyDrvThreshPassedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3019)
)
cpqDa4PhyDrvThreshPassedTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBay"))
)
if mibBuilder.loadTexts:
    cpqDa4PhyDrvThreshPassedTrap.setStatus(
        ""
    )

cpqDaTapeLibraryStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3020)
)
cpqDaTapeLibraryStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiBus"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiTarget"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiLun"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryStatus"))
)
if mibBuilder.loadTexts:
    cpqDaTapeLibraryStatusChange.setStatus(
        ""
    )

cpqDaTapeLibraryDoorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3021)
)
cpqDaTapeLibraryDoorStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiBus"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiTarget"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiLun"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryDoorStatus"))
)
if mibBuilder.loadTexts:
    cpqDaTapeLibraryDoorStatusChange.setStatus(
        ""
    )

cpqDaTapeDriveStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3022)
)
cpqDaTapeDriveStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaTapeDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvBusIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvScsiIdIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvLunIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqDaTapeDriveStatusChange.setStatus(
        ""
    )

cpqDaTapeDriveCleaningRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3023)
)
cpqDaTapeDriveCleaningRequired.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaTapeDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvBusIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvScsiIdIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvLunIndex"))
)
if mibBuilder.loadTexts:
    cpqDaTapeDriveCleaningRequired.setStatus(
        ""
    )

cpqDaTapeDriveCleanTapeReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3024)
)
cpqDaTapeDriveCleanTapeReplace.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaTapeDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvBusIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvScsiIdIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvLunIndex"))
)
if mibBuilder.loadTexts:
    cpqDaTapeDriveCleanTapeReplace.setStatus(
        ""
    )

cpqDa5AccelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3025)
)
cpqDa5AccelStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrSlot"),
        ("CPQIDA-MIB", "cpqDaCntlrModel"),
        ("CPQIDA-MIB", "cpqDaAccelSerialNumber"),
        ("CPQIDA-MIB", "cpqDaAccelTotalMemory"),
        ("CPQIDA-MIB", "cpqDaAccelStatus"),
        ("CPQIDA-MIB", "cpqDaAccelErrCode"))
)
if mibBuilder.loadTexts:
    cpqDa5AccelStatusChange.setStatus(
        ""
    )

cpqDa5AccelBadDataTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3026)
)
cpqDa5AccelBadDataTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrSlot"),
        ("CPQIDA-MIB", "cpqDaCntlrModel"),
        ("CPQIDA-MIB", "cpqDaAccelSerialNumber"),
        ("CPQIDA-MIB", "cpqDaAccelTotalMemory"))
)
if mibBuilder.loadTexts:
    cpqDa5AccelBadDataTrap.setStatus(
        ""
    )

cpqDa5AccelBatteryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3027)
)
cpqDa5AccelBatteryFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrSlot"),
        ("CPQIDA-MIB", "cpqDaCntlrModel"),
        ("CPQIDA-MIB", "cpqDaAccelSerialNumber"),
        ("CPQIDA-MIB", "cpqDaAccelTotalMemory"))
)
if mibBuilder.loadTexts:
    cpqDa5AccelBatteryFailed.setStatus(
        ""
    )

cpqDa5CntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3028)
)
cpqDa5CntlrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrSlot"),
        ("CPQIDA-MIB", "cpqDaCntlrBoardStatus"),
        ("CPQIDA-MIB", "cpqDaCntlrModel"),
        ("CPQIDA-MIB", "cpqDaCntlrSerialNumber"),
        ("CPQIDA-MIB", "cpqDaCntlrFWRev"),
        ("CPQIDA-MIB", "cpqDaAccelTotalMemory"))
)
if mibBuilder.loadTexts:
    cpqDa5CntlrStatusChange.setStatus(
        ""
    )

cpqDa5PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3029)
)
cpqDa5PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaPhyDrvStatus"),
        ("CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBay"),
        ("CPQIDA-MIB", "cpqDaPhyDrvModel"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFWRev"),
        ("CPQIDA-MIB", "cpqDaPhyDrvSerialNum"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFailureCode"))
)
if mibBuilder.loadTexts:
    cpqDa5PhyDrvStatusChange.setStatus(
        ""
    )

cpqDa5PhyDrvThreshPassedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3030)
)
cpqDa5PhyDrvThreshPassedTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBay"),
        ("CPQIDA-MIB", "cpqDaPhyDrvModel"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFWRev"),
        ("CPQIDA-MIB", "cpqDaPhyDrvSerialNum"))
)
if mibBuilder.loadTexts:
    cpqDa5PhyDrvThreshPassedTrap.setStatus(
        ""
    )

cpqDa2TapeLibraryStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3031)
)
cpqDa2TapeLibraryStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiBus"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiTarget"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiLun"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryModel"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryFWRev"),
        ("CPQIDA-MIB", "cpqDaTapeLibrarySerialNumber"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryStatus"))
)
if mibBuilder.loadTexts:
    cpqDa2TapeLibraryStatusChange.setStatus(
        ""
    )

cpqDa2TapeDriveStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3032)
)
cpqDa2TapeDriveStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaTapeDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvBusIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvScsiIdIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvLunIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvName"),
        ("CPQIDA-MIB", "cpqDaTapeDrvFwRev"),
        ("CPQIDA-MIB", "cpqDaTapeDrvSerialNumber"),
        ("CPQIDA-MIB", "cpqDaTapeDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqDa2TapeDriveStatusChange.setStatus(
        ""
    )

cpqDa6CntlrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3033)
)
cpqDa6CntlrStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaCntlrBoardStatus"),
        ("CPQIDA-MIB", "cpqDaCntlrModel"),
        ("CPQIDA-MIB", "cpqDaCntlrSerialNumber"),
        ("CPQIDA-MIB", "cpqDaCntlrFWRev"),
        ("CPQIDA-MIB", "cpqDaAccelTotalMemory"))
)
if mibBuilder.loadTexts:
    cpqDa6CntlrStatusChange.setStatus(
        ""
    )

cpqDa6LogDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3034)
)
cpqDa6LogDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaLogDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaLogDrvIndex"),
        ("CPQIDA-MIB", "cpqDaLogDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqDa6LogDrvStatusChange.setStatus(
        ""
    )

cpqDa6SpareStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3035)
)
cpqDa6SpareStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaSpareCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaSparePhyDrvIndex"),
        ("CPQIDA-MIB", "cpqDaSpareStatus"),
        ("CPQIDA-MIB", "cpqDaSpareBusNumber"),
        ("CPQIDA-MIB", "cpqDaSpareBay"))
)
if mibBuilder.loadTexts:
    cpqDa6SpareStatusChange.setStatus(
        ""
    )

cpqDa6PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3036)
)
cpqDa6PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBay"),
        ("CPQIDA-MIB", "cpqDaPhyDrvModel"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFWRev"),
        ("CPQIDA-MIB", "cpqDaPhyDrvSerialNum"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFailureCode"),
        ("CPQIDA-MIB", "cpqDaPhyDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqDa6PhyDrvStatusChange.setStatus(
        ""
    )

cpqDa6PhyDrvThreshPassedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3037)
)
cpqDa6PhyDrvThreshPassedTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBay"),
        ("CPQIDA-MIB", "cpqDaPhyDrvModel"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFWRev"),
        ("CPQIDA-MIB", "cpqDaPhyDrvSerialNum"))
)
if mibBuilder.loadTexts:
    cpqDa6PhyDrvThreshPassedTrap.setStatus(
        ""
    )

cpqDa6AccelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3038)
)
cpqDa6AccelStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaCntlrModel"),
        ("CPQIDA-MIB", "cpqDaAccelCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaAccelSerialNumber"),
        ("CPQIDA-MIB", "cpqDaAccelTotalMemory"),
        ("CPQIDA-MIB", "cpqDaAccelStatus"),
        ("CPQIDA-MIB", "cpqDaAccelErrCode"))
)
if mibBuilder.loadTexts:
    cpqDa6AccelStatusChange.setStatus(
        ""
    )

cpqDa6AccelBadDataTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3039)
)
cpqDa6AccelBadDataTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaCntlrModel"),
        ("CPQIDA-MIB", "cpqDaAccelCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaAccelSerialNumber"),
        ("CPQIDA-MIB", "cpqDaAccelTotalMemory"))
)
if mibBuilder.loadTexts:
    cpqDa6AccelBadDataTrap.setStatus(
        ""
    )

cpqDa6AccelBatteryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3040)
)
cpqDa6AccelBatteryFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaCntlrModel"),
        ("CPQIDA-MIB", "cpqDaAccelCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaAccelSerialNumber"),
        ("CPQIDA-MIB", "cpqDaAccelTotalMemory"))
)
if mibBuilder.loadTexts:
    cpqDa6AccelBatteryFailed.setStatus(
        ""
    )

cpqDa6TapeLibraryStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3041)
)
cpqDa6TapeLibraryStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiBus"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiTarget"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiLun"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryModel"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryFWRev"),
        ("CPQIDA-MIB", "cpqDaTapeLibrarySerialNumber"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryStatus"))
)
if mibBuilder.loadTexts:
    cpqDa6TapeLibraryStatusChange.setStatus(
        ""
    )

cpqDa6TapeLibraryDoorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3042)
)
cpqDa6TapeLibraryDoorStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiBus"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiTarget"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryScsiLun"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryModel"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryFWRev"),
        ("CPQIDA-MIB", "cpqDaTapeLibrarySerialNumber"),
        ("CPQIDA-MIB", "cpqDaTapeLibraryDoorStatus"))
)
if mibBuilder.loadTexts:
    cpqDa6TapeLibraryDoorStatusChange.setStatus(
        ""
    )

cpqDa6TapeDriveStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3043)
)
cpqDa6TapeDriveStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaTapeDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvBusIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvScsiIdIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvLunIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvName"),
        ("CPQIDA-MIB", "cpqDaTapeDrvFwRev"),
        ("CPQIDA-MIB", "cpqDaTapeDrvSerialNumber"),
        ("CPQIDA-MIB", "cpqDaTapeDrvStatus"))
)
if mibBuilder.loadTexts:
    cpqDa6TapeDriveStatusChange.setStatus(
        ""
    )

cpqDa6TapeDriveCleaningRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3044)
)
cpqDa6TapeDriveCleaningRequired.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaTapeDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvBusIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvScsiIdIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvLunIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvName"),
        ("CPQIDA-MIB", "cpqDaTapeDrvFwRev"),
        ("CPQIDA-MIB", "cpqDaTapeDrvSerialNumber"))
)
if mibBuilder.loadTexts:
    cpqDa6TapeDriveCleaningRequired.setStatus(
        ""
    )

cpqDa6TapeDriveCleanTapeReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3045)
)
cpqDa6TapeDriveCleanTapeReplace.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaTapeDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvBusIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvScsiIdIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvLunIndex"),
        ("CPQIDA-MIB", "cpqDaTapeDrvName"),
        ("CPQIDA-MIB", "cpqDaTapeDrvFwRev"),
        ("CPQIDA-MIB", "cpqDaTapeDrvSerialNumber"))
)
if mibBuilder.loadTexts:
    cpqDa6TapeDriveCleanTapeReplace.setStatus(
        ""
    )

cpqDa7PhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3046)
)
cpqDa7PhyDrvStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvLocationString"),
        ("CPQIDA-MIB", "cpqDaPhyDrvType"),
        ("CPQIDA-MIB", "cpqDaPhyDrvModel"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFWRev"),
        ("CPQIDA-MIB", "cpqDaPhyDrvSerialNum"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFailureCode"),
        ("CPQIDA-MIB", "cpqDaPhyDrvStatus"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDa7PhyDrvStatusChange.setStatus(
        ""
    )

cpqDa7SpareStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3047)
)
cpqDa7SpareStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaSpareCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaSparePhyDrvIndex"),
        ("CPQIDA-MIB", "cpqDaSpareStatus"),
        ("CPQIDA-MIB", "cpqDaSpareLocationString"),
        ("CPQIDA-MIB", "cpqDaSpareBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDa7SpareStatusChange.setStatus(
        ""
    )

cpqDaCntlrPartnerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3048)
)
cpqDaCntlrPartnerStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaCntlrModel"),
        ("CPQIDA-MIB", "cpqDaCntlrSerialNumber"),
        ("CPQIDA-MIB", "cpqDaCntlrPartnerSerialNumber"),
        ("CPQIDA-MIB", "cpqDaCntlrPartnerBoardStatus"))
)
if mibBuilder.loadTexts:
    cpqDaCntlrPartnerStatusChange.setStatus(
        ""
    )

cpqDaPhyDrvSSDWearStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 3049)
)
cpqDaPhyDrvSSDWearStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIDA-MIB", "cpqDaCntlrHwLocation"),
        ("CPQIDA-MIB", "cpqDaPhyDrvCntlrIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvIndex"),
        ("CPQIDA-MIB", "cpqDaPhyDrvLocationString"),
        ("CPQIDA-MIB", "cpqDaPhyDrvType"),
        ("CPQIDA-MIB", "cpqDaPhyDrvModel"),
        ("CPQIDA-MIB", "cpqDaPhyDrvFWRev"),
        ("CPQIDA-MIB", "cpqDaPhyDrvSerialNum"),
        ("CPQIDA-MIB", "cpqDaPhyDrvSSDWearStatus"))
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvSSDWearStatusChange.setStatus(
        ""
    )

cpqDaLogDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 3, 0, 1)
)
cpqDaLogDrvStatusChange.setObjects(
    ("CPQIDA-MIB", "cpqDaLogDrvStatus")
)
if mibBuilder.loadTexts:
    cpqDaLogDrvStatusChange.setStatus(
        ""
    )

cpqDaSpareStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 3, 0, 2)
)
cpqDaSpareStatusChange.setObjects(
      *(("CPQIDA-MIB", "cpqDaSpareStatus"),
        ("CPQIDA-MIB", "cpqDaSpareBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDaSpareStatusChange.setStatus(
        ""
    )

cpqDaPhyDrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 3, 0, 3)
)
cpqDaPhyDrvStatusChange.setObjects(
      *(("CPQIDA-MIB", "cpqDaPhyDrvStatus"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvStatusChange.setStatus(
        ""
    )

cpqDaPhyDrvThreshPassedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 3, 0, 4)
)
cpqDaPhyDrvThreshPassedTrap.setObjects(
      *(("CPQIDA-MIB", "cpqDaPhyDrvThreshPassed"),
        ("CPQIDA-MIB", "cpqDaPhyDrvBusNumber"))
)
if mibBuilder.loadTexts:
    cpqDaPhyDrvThreshPassedTrap.setStatus(
        ""
    )

cpqDaAccelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 3, 0, 5)
)
cpqDaAccelStatusChange.setObjects(
    ("CPQIDA-MIB", "cpqDaAccelStatus")
)
if mibBuilder.loadTexts:
    cpqDaAccelStatusChange.setStatus(
        ""
    )

cpqDaAccelBadDataTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 3, 0, 6)
)
cpqDaAccelBadDataTrap.setObjects(
    ("CPQIDA-MIB", "cpqDaAccelBadData")
)
if mibBuilder.loadTexts:
    cpqDaAccelBadDataTrap.setStatus(
        ""
    )

cpqDaAccelBatteryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 3, 0, 7)
)
cpqDaAccelBatteryFailed.setObjects(
    ("CPQIDA-MIB", "cpqDaAccelBattery")
)
if mibBuilder.loadTexts:
    cpqDaAccelBatteryFailed.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQIDA-MIB",
    **{"cpqDa2LogDrvStatusChange": cpqDa2LogDrvStatusChange,
       "cpqDa2SpareStatusChange": cpqDa2SpareStatusChange,
       "cpqDa2PhyDrvStatusChange": cpqDa2PhyDrvStatusChange,
       "cpqDa2PhyDrvThreshPassedTrap": cpqDa2PhyDrvThreshPassedTrap,
       "cpqDa2AccelStatusChange": cpqDa2AccelStatusChange,
       "cpqDa2AccelBadDataTrap": cpqDa2AccelBadDataTrap,
       "cpqDa2AccelBatteryFailed": cpqDa2AccelBatteryFailed,
       "cpqDa3LogDrvStatusChange": cpqDa3LogDrvStatusChange,
       "cpqDa3SpareStatusChange": cpqDa3SpareStatusChange,
       "cpqDa3PhyDrvStatusChange": cpqDa3PhyDrvStatusChange,
       "cpqDa3PhyDrvThreshPassedTrap": cpqDa3PhyDrvThreshPassedTrap,
       "cpqDa3AccelStatusChange": cpqDa3AccelStatusChange,
       "cpqDa3AccelBadDataTrap": cpqDa3AccelBadDataTrap,
       "cpqDa3AccelBatteryFailed": cpqDa3AccelBatteryFailed,
       "cpqDaCntlrStatusChange": cpqDaCntlrStatusChange,
       "cpqDaCntlrActive": cpqDaCntlrActive,
       "cpqDa4SpareStatusChange": cpqDa4SpareStatusChange,
       "cpqDa4PhyDrvStatusChange": cpqDa4PhyDrvStatusChange,
       "cpqDa4PhyDrvThreshPassedTrap": cpqDa4PhyDrvThreshPassedTrap,
       "cpqDaTapeLibraryStatusChange": cpqDaTapeLibraryStatusChange,
       "cpqDaTapeLibraryDoorStatusChange": cpqDaTapeLibraryDoorStatusChange,
       "cpqDaTapeDriveStatusChange": cpqDaTapeDriveStatusChange,
       "cpqDaTapeDriveCleaningRequired": cpqDaTapeDriveCleaningRequired,
       "cpqDaTapeDriveCleanTapeReplace": cpqDaTapeDriveCleanTapeReplace,
       "cpqDa5AccelStatusChange": cpqDa5AccelStatusChange,
       "cpqDa5AccelBadDataTrap": cpqDa5AccelBadDataTrap,
       "cpqDa5AccelBatteryFailed": cpqDa5AccelBatteryFailed,
       "cpqDa5CntlrStatusChange": cpqDa5CntlrStatusChange,
       "cpqDa5PhyDrvStatusChange": cpqDa5PhyDrvStatusChange,
       "cpqDa5PhyDrvThreshPassedTrap": cpqDa5PhyDrvThreshPassedTrap,
       "cpqDa2TapeLibraryStatusChange": cpqDa2TapeLibraryStatusChange,
       "cpqDa2TapeDriveStatusChange": cpqDa2TapeDriveStatusChange,
       "cpqDa6CntlrStatusChange": cpqDa6CntlrStatusChange,
       "cpqDa6LogDrvStatusChange": cpqDa6LogDrvStatusChange,
       "cpqDa6SpareStatusChange": cpqDa6SpareStatusChange,
       "cpqDa6PhyDrvStatusChange": cpqDa6PhyDrvStatusChange,
       "cpqDa6PhyDrvThreshPassedTrap": cpqDa6PhyDrvThreshPassedTrap,
       "cpqDa6AccelStatusChange": cpqDa6AccelStatusChange,
       "cpqDa6AccelBadDataTrap": cpqDa6AccelBadDataTrap,
       "cpqDa6AccelBatteryFailed": cpqDa6AccelBatteryFailed,
       "cpqDa6TapeLibraryStatusChange": cpqDa6TapeLibraryStatusChange,
       "cpqDa6TapeLibraryDoorStatusChange": cpqDa6TapeLibraryDoorStatusChange,
       "cpqDa6TapeDriveStatusChange": cpqDa6TapeDriveStatusChange,
       "cpqDa6TapeDriveCleaningRequired": cpqDa6TapeDriveCleaningRequired,
       "cpqDa6TapeDriveCleanTapeReplace": cpqDa6TapeDriveCleanTapeReplace,
       "cpqDa7PhyDrvStatusChange": cpqDa7PhyDrvStatusChange,
       "cpqDa7SpareStatusChange": cpqDa7SpareStatusChange,
       "cpqDaCntlrPartnerStatusChange": cpqDaCntlrPartnerStatusChange,
       "cpqDaPhyDrvSSDWearStatusChange": cpqDaPhyDrvSSDWearStatusChange,
       "cpqDriveArray": cpqDriveArray,
       "cpqDaLogDrvStatusChange": cpqDaLogDrvStatusChange,
       "cpqDaSpareStatusChange": cpqDaSpareStatusChange,
       "cpqDaPhyDrvStatusChange": cpqDaPhyDrvStatusChange,
       "cpqDaPhyDrvThreshPassedTrap": cpqDaPhyDrvThreshPassedTrap,
       "cpqDaAccelStatusChange": cpqDaAccelStatusChange,
       "cpqDaAccelBadDataTrap": cpqDaAccelBadDataTrap,
       "cpqDaAccelBatteryFailed": cpqDaAccelBatteryFailed,
       "cpqDaMibRev": cpqDaMibRev,
       "cpqDaMibRevMajor": cpqDaMibRevMajor,
       "cpqDaMibRevMinor": cpqDaMibRevMinor,
       "cpqDaMibCondition": cpqDaMibCondition,
       "cpqDaComponent": cpqDaComponent,
       "cpqDaInterface": cpqDaInterface,
       "cpqDaOsNetWare3x": cpqDaOsNetWare3x,
       "cpqDaNw3xDriverName": cpqDaNw3xDriverName,
       "cpqDaNw3xDriverVer": cpqDaNw3xDriverVer,
       "cpqDaNw3xPollType": cpqDaNw3xPollType,
       "cpqDaNw3xPollTime": cpqDaNw3xPollTime,
       "cpqDaNw3xDriverStatTable": cpqDaNw3xDriverStatTable,
       "cpqDaNw3xDriverStatEntry": cpqDaNw3xDriverStatEntry,
       "cpqDaNw3xCntlrIndex": cpqDaNw3xCntlrIndex,
       "cpqDaNw3xLogDrvIndex": cpqDaNw3xLogDrvIndex,
       "cpqDaNw3xTotalReads": cpqDaNw3xTotalReads,
       "cpqDaNw3xTotalWrites": cpqDaNw3xTotalWrites,
       "cpqDaNw3xCorrReads": cpqDaNw3xCorrReads,
       "cpqDaNw3xCorrWrites": cpqDaNw3xCorrWrites,
       "cpqDaNw3xFatalReads": cpqDaNw3xFatalReads,
       "cpqDaNw3xFatalWrites": cpqDaNw3xFatalWrites,
       "cpqDaNw3xVolMapTable": cpqDaNw3xVolMapTable,
       "cpqDaNw3xVolMapEntry": cpqDaNw3xVolMapEntry,
       "cpqDaNw3xVolCntlrIndex": cpqDaNw3xVolCntlrIndex,
       "cpqDaNw3xVolLogDrvIndex": cpqDaNw3xVolLogDrvIndex,
       "cpqDaNw3xVolMap": cpqDaNw3xVolMap,
       "cpqDaOsCommon": cpqDaOsCommon,
       "cpqDaOsCommonPollFreq": cpqDaOsCommonPollFreq,
       "cpqDaOsCommonModuleTable": cpqDaOsCommonModuleTable,
       "cpqDaOsCommonModuleEntry": cpqDaOsCommonModuleEntry,
       "cpqDaOsCommonModuleIndex": cpqDaOsCommonModuleIndex,
       "cpqDaOsCommonModuleName": cpqDaOsCommonModuleName,
       "cpqDaOsCommonModuleVersion": cpqDaOsCommonModuleVersion,
       "cpqDaOsCommonModuleDate": cpqDaOsCommonModuleDate,
       "cpqDaOsCommonModulePurpose": cpqDaOsCommonModulePurpose,
       "cpqDaOsCommonCollectionReset": cpqDaOsCommonCollectionReset,
       "cpqDaCntlr": cpqDaCntlr,
       "cpqDaCntlrTable": cpqDaCntlrTable,
       "cpqDaCntlrEntry": cpqDaCntlrEntry,
       "cpqDaCntlrIndex": cpqDaCntlrIndex,
       "cpqDaCntlrModel": cpqDaCntlrModel,
       "cpqDaCntlrFWRev": cpqDaCntlrFWRev,
       "cpqDaCntlrStndIntr": cpqDaCntlrStndIntr,
       "cpqDaCntlrSlot": cpqDaCntlrSlot,
       "cpqDaCntlrCondition": cpqDaCntlrCondition,
       "cpqDaCntlrProductRev": cpqDaCntlrProductRev,
       "cpqDaCntlrPartnerSlot": cpqDaCntlrPartnerSlot,
       "cpqDaCntlrCurrentRole": cpqDaCntlrCurrentRole,
       "cpqDaCntlrBoardStatus": cpqDaCntlrBoardStatus,
       "cpqDaCntlrPartnerBoardStatus": cpqDaCntlrPartnerBoardStatus,
       "cpqDaCntlrBoardCondition": cpqDaCntlrBoardCondition,
       "cpqDaCntlrPartnerBoardCondition": cpqDaCntlrPartnerBoardCondition,
       "cpqDaCntlrDriveOwnership": cpqDaCntlrDriveOwnership,
       "cpqDaCntlrSerialNumber": cpqDaCntlrSerialNumber,
       "cpqDaCntlrRedundancyType": cpqDaCntlrRedundancyType,
       "cpqDaCntlrRedundancyError": cpqDaCntlrRedundancyError,
       "cpqDaCntlrAccessModuleStatus": cpqDaCntlrAccessModuleStatus,
       "cpqDaCntlrDaughterBoardType": cpqDaCntlrDaughterBoardType,
       "cpqDaCntlrHwLocation": cpqDaCntlrHwLocation,
       "cpqDaCntlrNumberOfBuses": cpqDaCntlrNumberOfBuses,
       "cpqDaCntlrBlinkTime": cpqDaCntlrBlinkTime,
       "cpqDaCntlrRebuildPriority": cpqDaCntlrRebuildPriority,
       "cpqDaCntlrExpandPriority": cpqDaCntlrExpandPriority,
       "cpqDaCntlrNumberOfInternalPorts": cpqDaCntlrNumberOfInternalPorts,
       "cpqDaCntlrNumberOfExternalPorts": cpqDaCntlrNumberOfExternalPorts,
       "cpqDaCntlrDriveWriteCacheState": cpqDaCntlrDriveWriteCacheState,
       "cpqDaCntlrPartnerSerialNumber": cpqDaCntlrPartnerSerialNumber,
       "cpqDaCntlrOptionRomRev": cpqDaCntlrOptionRomRev,
       "cpqDaCntlrHbaFWRev": cpqDaCntlrHbaFWRev,
       "cpqDaCntlrHBAModeOptionRomRev": cpqDaCntlrHBAModeOptionRomRev,
       "cpqDaCntlrCurrentTemp": cpqDaCntlrCurrentTemp,
       "cpqDaCntlrLastLockupCode": cpqDaCntlrLastLockupCode,
       "cpqDaCntlrEncryptionStatus": cpqDaCntlrEncryptionStatus,
       "cpqDaCntlrASICEncptSelfTestStatus": cpqDaCntlrASICEncptSelfTestStatus,
       "cpqDaCntlrEncryptCspNvramStatus": cpqDaCntlrEncryptCspNvramStatus,
       "cpqDaCntlrEncryptCryptoOfficerPwdSetStatus": cpqDaCntlrEncryptCryptoOfficerPwdSetStatus,
       "cpqDaCntlrEncryptCntlrPwdSetStatus": cpqDaCntlrEncryptCntlrPwdSetStatus,
       "cpqDaCntlrEncryptCntlrPwdAvailStatus": cpqDaCntlrEncryptCntlrPwdAvailStatus,
       "cpqDaCntlrUnencryptedLogDrvCreationPolicy": cpqDaCntlrUnencryptedLogDrvCreationPolicy,
       "cpqDaCntlrEncryptedLogDrvCreationPolicy": cpqDaCntlrEncryptedLogDrvCreationPolicy,
       "cpqDaCntlrEncryptFWLockStatus": cpqDaCntlrEncryptFWLockStatus,
       "cpqDaAccelTable": cpqDaAccelTable,
       "cpqDaAccelEntry": cpqDaAccelEntry,
       "cpqDaAccelCntlrIndex": cpqDaAccelCntlrIndex,
       "cpqDaAccelStatus": cpqDaAccelStatus,
       "cpqDaAccelMemory": cpqDaAccelMemory,
       "cpqDaAccelBadData": cpqDaAccelBadData,
       "cpqDaAccelErrCode": cpqDaAccelErrCode,
       "cpqDaAccelBattery": cpqDaAccelBattery,
       "cpqDaAccelReadErrs": cpqDaAccelReadErrs,
       "cpqDaAccelWriteErrs": cpqDaAccelWriteErrs,
       "cpqDaAccelCondition": cpqDaAccelCondition,
       "cpqDaAccelReadMemory": cpqDaAccelReadMemory,
       "cpqDaAccelSerialNumber": cpqDaAccelSerialNumber,
       "cpqDaAccelTotalMemory": cpqDaAccelTotalMemory,
       "cpqDaAccelReadCachePercent": cpqDaAccelReadCachePercent,
       "cpqDaAccelWriteCachePercent": cpqDaAccelWriteCachePercent,
       "cpqDaAccelFailedBatteries": cpqDaAccelFailedBatteries,
       "cpqDaAccelBackupPowerSource": cpqDaAccelBackupPowerSource,
       "cpqDaAccelBoardCurrentTemp": cpqDaAccelBoardCurrentTemp,
       "cpqDaAccelCapacitorCurrentTemp": cpqDaAccelCapacitorCurrentTemp,
       "cpqDaAccelMemoryDataWidth": cpqDaAccelMemoryDataWidth,
       "cpqDaAccelMemoryTransferRate": cpqDaAccelMemoryTransferRate,
       "cpqDaManagedCableTable": cpqDaManagedCableTable,
       "cpqDaManagedCableEntry": cpqDaManagedCableEntry,
       "cpqDaManagedCableIndex": cpqDaManagedCableIndex,
       "cpqDaManagedCableCntlrIndex": cpqDaManagedCableCntlrIndex,
       "cpqDaManagedCableHostConnector": cpqDaManagedCableHostConnector,
       "cpqDaManagedCableStatus": cpqDaManagedCableStatus,
       "cpqDaManagedCableFaultCode": cpqDaManagedCableFaultCode,
       "cpqDaManagedCableVendorRevision": cpqDaManagedCableVendorRevision,
       "cpqDaManagedCableVendorSerialNumber": cpqDaManagedCableVendorSerialNumber,
       "cpqDaManagedCableVendorPartNumber": cpqDaManagedCableVendorPartNumber,
       "cpqDaManagedCableLength": cpqDaManagedCableLength,
       "cpqDaLogDrv": cpqDaLogDrv,
       "cpqDaLogDrvTable": cpqDaLogDrvTable,
       "cpqDaLogDrvEntry": cpqDaLogDrvEntry,
       "cpqDaLogDrvCntlrIndex": cpqDaLogDrvCntlrIndex,
       "cpqDaLogDrvIndex": cpqDaLogDrvIndex,
       "cpqDaLogDrvFaultTol": cpqDaLogDrvFaultTol,
       "cpqDaLogDrvStatus": cpqDaLogDrvStatus,
       "cpqDaLogDrvAutoRel": cpqDaLogDrvAutoRel,
       "cpqDaLogDrvRebuildBlks": cpqDaLogDrvRebuildBlks,
       "cpqDaLogDrvHasAccel": cpqDaLogDrvHasAccel,
       "cpqDaLogDrvAvailSpares": cpqDaLogDrvAvailSpares,
       "cpqDaLogDrvSize": cpqDaLogDrvSize,
       "cpqDaLogDrvPhyDrvIDs": cpqDaLogDrvPhyDrvIDs,
       "cpqDaLogDrvCondition": cpqDaLogDrvCondition,
       "cpqDaLogDrvPercentRebuild": cpqDaLogDrvPercentRebuild,
       "cpqDaLogDrvStripeSize": cpqDaLogDrvStripeSize,
       "cpqDaLogDrvOsName": cpqDaLogDrvOsName,
       "cpqDaLogDrvBlinkTime": cpqDaLogDrvBlinkTime,
       "cpqDaLogDrvSpareReplaceMap": cpqDaLogDrvSpareReplaceMap,
       "cpqDaLogDrvRebuildingPhyDrv": cpqDaLogDrvRebuildingPhyDrv,
       "cpqDaLogDrvMultipathAccess": cpqDaLogDrvMultipathAccess,
       "cpqDaLogDrvNmbrOfParityGroups": cpqDaLogDrvNmbrOfParityGroups,
       "cpqDaLogDrvSplitMirrorBackupLogDrv": cpqDaLogDrvSplitMirrorBackupLogDrv,
       "cpqDaLogDrvCacheVolAccelAssocType": cpqDaLogDrvCacheVolAccelAssocType,
       "cpqDaLogDrvCacheVolIndex": cpqDaLogDrvCacheVolIndex,
       "cpqDaLogDrvRPIPercentComplete": cpqDaLogDrvRPIPercentComplete,
       "cpqDaLogDrvSSDSmartPathStatus": cpqDaLogDrvSSDSmartPathStatus,
       "cpqDaLogDrvEncryptionStatus": cpqDaLogDrvEncryptionStatus,
       "cpqDaLogDrvPhyDrvExtAttachTable": cpqDaLogDrvPhyDrvExtAttachTable,
       "cpqDaLogDrvPhyDrvExtAttachEntry": cpqDaLogDrvPhyDrvExtAttachEntry,
       "cpqDaLogDrvPhyDrvAttachExtIndex": cpqDaLogDrvPhyDrvAttachExtIndex,
       "cpqDaLogDrvCntlrExtended": cpqDaLogDrvCntlrExtended,
       "cpqDaLogDrvLogDrvExtended": cpqDaLogDrvLogDrvExtended,
       "cpqDaLogDrvPhyDrvExtended": cpqDaLogDrvPhyDrvExtended,
       "cpqDaLogDrvSprRplcExtAttachTable": cpqDaLogDrvSprRplcExtAttachTable,
       "cpqDaLogDrvSprRplcExtAttachEntry": cpqDaLogDrvSprRplcExtAttachEntry,
       "cpqDaLogDrvSprRplcAttachExtIndex": cpqDaLogDrvSprRplcAttachExtIndex,
       "cpqDaLogDrvSprRplcCntlrExtended": cpqDaLogDrvSprRplcCntlrExtended,
       "cpqDaLogDrvSprRplcLogDrvExtended": cpqDaLogDrvSprRplcLogDrvExtended,
       "cpqDaLogDrvSprRplcReplacedPhysDrvExtended": cpqDaLogDrvSprRplcReplacedPhysDrvExtended,
       "cpqDaLogDrvSprRplcSparePhysDrvExtended": cpqDaLogDrvSprRplcSparePhysDrvExtended,
       "cpqDaLogDrvAvalSprExtAttachTable": cpqDaLogDrvAvalSprExtAttachTable,
       "cpqDaLogDrvAvalSprExtAttachEntry": cpqDaLogDrvAvalSprExtAttachEntry,
       "cpqDaLogDrvAvailSprAttachExtIndex": cpqDaLogDrvAvailSprAttachExtIndex,
       "cpqDaLogDrvAvailSprCntlrExtended": cpqDaLogDrvAvailSprCntlrExtended,
       "cpqDaLogDrvAvailSprLogDrvExtended": cpqDaLogDrvAvailSprLogDrvExtended,
       "cpqDaLogDrvAvailSprAvailableSpareExtended": cpqDaLogDrvAvailSprAvailableSpareExtended,
       "cpqDaLogDrvCacheVolumeAccelTable": cpqDaLogDrvCacheVolumeAccelTable,
       "cpqDaLogDrvCacheVolumeAccelEntry": cpqDaLogDrvCacheVolumeAccelEntry,
       "cpqDaLogDrvCacheVolAccelCntlrIndex": cpqDaLogDrvCacheVolAccelCntlrIndex,
       "cpqDaLogDrvCacheVolAccelLogDrvIndex": cpqDaLogDrvCacheVolAccelLogDrvIndex,
       "cpqDaLogDrvCacheVolAccelCachingAlgorithm": cpqDaLogDrvCacheVolAccelCachingAlgorithm,
       "cpqDaLogDrvCacheVolAccelCacheState": cpqDaLogDrvCacheVolAccelCacheState,
       "cpqDaLogDrvCacheVolAccelWritePolicy": cpqDaLogDrvCacheVolAccelWritePolicy,
       "cpqDaLogDrvCacheVolAccelNoOfReadHitsH": cpqDaLogDrvCacheVolAccelNoOfReadHitsH,
       "cpqDaLogDrvCacheVolAccelNoOfReadHits": cpqDaLogDrvCacheVolAccelNoOfReadHits,
       "cpqDaLogDrvCacheVolAccelNoOfReadMissDoLoadH": cpqDaLogDrvCacheVolAccelNoOfReadMissDoLoadH,
       "cpqDaLogDrvCacheVolAccelNoOfReadMissDoLoad": cpqDaLogDrvCacheVolAccelNoOfReadMissDoLoad,
       "cpqDaLogDrvCacheVolAccelNoOfReadMissLoadingH": cpqDaLogDrvCacheVolAccelNoOfReadMissLoadingH,
       "cpqDaLogDrvCacheVolAccelNoOfReadMissLoading": cpqDaLogDrvCacheVolAccelNoOfReadMissLoading,
       "cpqDaLogDrvCacheVolAccelNoOfReadMissSkipH": cpqDaLogDrvCacheVolAccelNoOfReadMissSkipH,
       "cpqDaLogDrvCacheVolAccelNoOfReadMissSkip": cpqDaLogDrvCacheVolAccelNoOfReadMissSkip,
       "cpqDaLogDrvCacheVolAccelReadCacheHitRate": cpqDaLogDrvCacheVolAccelReadCacheHitRate,
       "cpqDaLogDrvCacheVolAccelNoOfWriteHitsH": cpqDaLogDrvCacheVolAccelNoOfWriteHitsH,
       "cpqDaLogDrvCacheVolAccelNoOfWriteHits": cpqDaLogDrvCacheVolAccelNoOfWriteHits,
       "cpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoadH": cpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoadH,
       "cpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoad": cpqDaLogDrvCacheVolAccelNoOfWriteMissDoLoad,
       "cpqDaLogDrvCacheVolAccelNoOfWriteMissLoadingH": cpqDaLogDrvCacheVolAccelNoOfWriteMissLoadingH,
       "cpqDaLogDrvCacheVolAccelNoOfWriteMissLoading": cpqDaLogDrvCacheVolAccelNoOfWriteMissLoading,
       "cpqDaLogDrvCacheVolAccelNoOfWriteMissSkipH": cpqDaLogDrvCacheVolAccelNoOfWriteMissSkipH,
       "cpqDaLogDrvCacheVolAccelNoOfWriteMissSkip": cpqDaLogDrvCacheVolAccelNoOfWriteMissSkip,
       "cpqDaLogDrvCacheVolAccelWriteCacheHitRate": cpqDaLogDrvCacheVolAccelWriteCacheHitRate,
       "cpqDaLogDrvCacheVolAccelLoadFailures": cpqDaLogDrvCacheVolAccelLoadFailures,
       "cpqDaLogDrvCacheVolAccelCacheLineSize": cpqDaLogDrvCacheVolAccelCacheLineSize,
       "cpqDaLogDrvCacheVolAccelNoOfReadMissLockedH": cpqDaLogDrvCacheVolAccelNoOfReadMissLockedH,
       "cpqDaLogDrvCacheVolAccelNoOfReadMissLocked": cpqDaLogDrvCacheVolAccelNoOfReadMissLocked,
       "cpqDaLogDrvCacheVolAccelNoOfWriteMissLockedH": cpqDaLogDrvCacheVolAccelNoOfWriteMissLockedH,
       "cpqDaLogDrvCacheVolAccelNoOfWriteMissLocked": cpqDaLogDrvCacheVolAccelNoOfWriteMissLocked,
       "cpqDaLogDrvCacheVolAccelNoOfReadMissTotalH": cpqDaLogDrvCacheVolAccelNoOfReadMissTotalH,
       "cpqDaLogDrvCacheVolAccelNoOfReadMissTotal": cpqDaLogDrvCacheVolAccelNoOfReadMissTotal,
       "cpqDaLogDrvCacheVolAccelNoOfWriteMissTotalH": cpqDaLogDrvCacheVolAccelNoOfWriteMissTotalH,
       "cpqDaLogDrvCacheVolAccelNoOfWriteMissTotal": cpqDaLogDrvCacheVolAccelNoOfWriteMissTotal,
       "cpqDaSpareDrv": cpqDaSpareDrv,
       "cpqDaSpareTable": cpqDaSpareTable,
       "cpqDaSpareEntry": cpqDaSpareEntry,
       "cpqDaSpareCntlrIndex": cpqDaSpareCntlrIndex,
       "cpqDaSparePhyDrvIndex": cpqDaSparePhyDrvIndex,
       "cpqDaSpareStatus": cpqDaSpareStatus,
       "cpqDaSpareReplacedDrv": cpqDaSpareReplacedDrv,
       "cpqDaSpareRebuildBlks": cpqDaSpareRebuildBlks,
       "cpqDaSpareCondition": cpqDaSpareCondition,
       "cpqDaSpareBusNumber": cpqDaSpareBusNumber,
       "cpqDaSpareBay": cpqDaSpareBay,
       "cpqDaSpareReplacedDrvBusNumber": cpqDaSpareReplacedDrvBusNumber,
       "cpqDaSpareReplacedDrvBay": cpqDaSpareReplacedDrvBay,
       "cpqDaSparePercentRebuild": cpqDaSparePercentRebuild,
       "cpqDaSpareLocationString": cpqDaSpareLocationString,
       "cpqDaPhyDrv": cpqDaPhyDrv,
       "cpqDaPhyDrvTable": cpqDaPhyDrvTable,
       "cpqDaPhyDrvEntry": cpqDaPhyDrvEntry,
       "cpqDaPhyDrvCntlrIndex": cpqDaPhyDrvCntlrIndex,
       "cpqDaPhyDrvIndex": cpqDaPhyDrvIndex,
       "cpqDaPhyDrvModel": cpqDaPhyDrvModel,
       "cpqDaPhyDrvFWRev": cpqDaPhyDrvFWRev,
       "cpqDaPhyDrvBay": cpqDaPhyDrvBay,
       "cpqDaPhyDrvStatus": cpqDaPhyDrvStatus,
       "cpqDaPhyDrvFactReallocs": cpqDaPhyDrvFactReallocs,
       "cpqDaPhyDrvUsedReallocs": cpqDaPhyDrvUsedReallocs,
       "cpqDaPhyDrvRefHours": cpqDaPhyDrvRefHours,
       "cpqDaPhyDrvHReads": cpqDaPhyDrvHReads,
       "cpqDaPhyDrvReads": cpqDaPhyDrvReads,
       "cpqDaPhyDrvHWrites": cpqDaPhyDrvHWrites,
       "cpqDaPhyDrvWrites": cpqDaPhyDrvWrites,
       "cpqDaPhyDrvHSeeks": cpqDaPhyDrvHSeeks,
       "cpqDaPhyDrvSeeks": cpqDaPhyDrvSeeks,
       "cpqDaPhyDrvHardReadErrs": cpqDaPhyDrvHardReadErrs,
       "cpqDaPhyDrvRecvReadErrs": cpqDaPhyDrvRecvReadErrs,
       "cpqDaPhyDrvHardWriteErrs": cpqDaPhyDrvHardWriteErrs,
       "cpqDaPhyDrvRecvWriteErrs": cpqDaPhyDrvRecvWriteErrs,
       "cpqDaPhyDrvHSeekErrs": cpqDaPhyDrvHSeekErrs,
       "cpqDaPhyDrvSeekErrs": cpqDaPhyDrvSeekErrs,
       "cpqDaPhyDrvSpinupTime": cpqDaPhyDrvSpinupTime,
       "cpqDaPhyDrvFunctTest1": cpqDaPhyDrvFunctTest1,
       "cpqDaPhyDrvFunctTest2": cpqDaPhyDrvFunctTest2,
       "cpqDaPhyDrvFunctTest3": cpqDaPhyDrvFunctTest3,
       "cpqDaPhyDrvDrqTimeouts": cpqDaPhyDrvDrqTimeouts,
       "cpqDaPhyDrvOtherTimeouts": cpqDaPhyDrvOtherTimeouts,
       "cpqDaPhyDrvSpinupRetries": cpqDaPhyDrvSpinupRetries,
       "cpqDaPhyDrvBadRecvReads": cpqDaPhyDrvBadRecvReads,
       "cpqDaPhyDrvBadRecvWrites": cpqDaPhyDrvBadRecvWrites,
       "cpqDaPhyDrvFormatErrs": cpqDaPhyDrvFormatErrs,
       "cpqDaPhyDrvPostErrs": cpqDaPhyDrvPostErrs,
       "cpqDaPhyDrvNotReadyErrs": cpqDaPhyDrvNotReadyErrs,
       "cpqDaPhyDrvReallocAborts": cpqDaPhyDrvReallocAborts,
       "cpqDaPhyDrvThreshPassed": cpqDaPhyDrvThreshPassed,
       "cpqDaPhyDrvHasMonInfo": cpqDaPhyDrvHasMonInfo,
       "cpqDaPhyDrvCondition": cpqDaPhyDrvCondition,
       "cpqDaPhyDrvHotPlugs": cpqDaPhyDrvHotPlugs,
       "cpqDaPhyDrvMediaErrs": cpqDaPhyDrvMediaErrs,
       "cpqDaPhyDrvHardwareErrs": cpqDaPhyDrvHardwareErrs,
       "cpqDaPhyDrvAbortedCmds": cpqDaPhyDrvAbortedCmds,
       "cpqDaPhyDrvSpinUpErrs": cpqDaPhyDrvSpinUpErrs,
       "cpqDaPhyDrvBadTargetErrs": cpqDaPhyDrvBadTargetErrs,
       "cpqDaPhyDrvLocation": cpqDaPhyDrvLocation,
       "cpqDaPhyDrvSize": cpqDaPhyDrvSize,
       "cpqDaPhyDrvBusFaults": cpqDaPhyDrvBusFaults,
       "cpqDaPhyDrvIrqDeglitches": cpqDaPhyDrvIrqDeglitches,
       "cpqDaPhyDrvHotPlug": cpqDaPhyDrvHotPlug,
       "cpqDaPhyDrvPlacement": cpqDaPhyDrvPlacement,
       "cpqDaPhyDrvBusNumber": cpqDaPhyDrvBusNumber,
       "cpqDaPhyDrvSerialNum": cpqDaPhyDrvSerialNum,
       "cpqDaPhyDrvPreFailMonitoring": cpqDaPhyDrvPreFailMonitoring,
       "cpqDaPhyDrvCurrentWidth": cpqDaPhyDrvCurrentWidth,
       "cpqDaPhyDrvCurrentSpeed": cpqDaPhyDrvCurrentSpeed,
       "cpqDaPhyDrvFailureCode": cpqDaPhyDrvFailureCode,
       "cpqDaPhyDrvBlinkTime": cpqDaPhyDrvBlinkTime,
       "cpqDaPhyDrvSmartStatus": cpqDaPhyDrvSmartStatus,
       "cpqDaPhyDrvConfigurationStatus": cpqDaPhyDrvConfigurationStatus,
       "cpqDaPhyDrvRotationalSpeed": cpqDaPhyDrvRotationalSpeed,
       "cpqDaPhyDrvType": cpqDaPhyDrvType,
       "cpqDaPhyDrvSataVersion": cpqDaPhyDrvSataVersion,
       "cpqDaPhyDrvHostConnector": cpqDaPhyDrvHostConnector,
       "cpqDaPhyDrvBoxOnConnector": cpqDaPhyDrvBoxOnConnector,
       "cpqDaPhyDrvLocationString": cpqDaPhyDrvLocationString,
       "cpqDaPhyDrvNegotiatedLinkRate": cpqDaPhyDrvNegotiatedLinkRate,
       "cpqDaPhyDrvNcqSupport": cpqDaPhyDrvNcqSupport,
       "cpqDaPhyDrvPhyCount": cpqDaPhyDrvPhyCount,
       "cpqDaPhyDrvMultipathAccess": cpqDaPhyDrvMultipathAccess,
       "cpqDaPhyDrvMediaType": cpqDaPhyDrvMediaType,
       "cpqDaPhyDrvCurrentTemperature": cpqDaPhyDrvCurrentTemperature,
       "cpqDaPhyDrvTemperatureThreshold": cpqDaPhyDrvTemperatureThreshold,
       "cpqDaPhyDrvMaximumTemperature": cpqDaPhyDrvMaximumTemperature,
       "cpqDaPhyDrvSSDWearStatus": cpqDaPhyDrvSSDWearStatus,
       "cpqDaPhyDrvPowerOnHours": cpqDaPhyDrvPowerOnHours,
       "cpqDaPhyDrvSSDPercntEndrnceUsed": cpqDaPhyDrvSSDPercntEndrnceUsed,
       "cpqDaPhyDrvSSDEstTimeRemainingHours": cpqDaPhyDrvSSDEstTimeRemainingHours,
       "cpqDaPhyDrvAuthenticationStatus": cpqDaPhyDrvAuthenticationStatus,
       "cpqDaPhyDrvSmartCarrierAppFWRev": cpqDaPhyDrvSmartCarrierAppFWRev,
       "cpqDaPhyDrvSmartCarrierBootldrFWRev": cpqDaPhyDrvSmartCarrierBootldrFWRev,
       "cpqDaPhyDrvEncryptionStatus": cpqDaPhyDrvEncryptionStatus,
       "cpqDaPhyDrvErrTable": cpqDaPhyDrvErrTable,
       "cpqDaPhyDrvErrEntry": cpqDaPhyDrvErrEntry,
       "cpqDaPhyDrvErrCntlrIndex": cpqDaPhyDrvErrCntlrIndex,
       "cpqDaPhyDrvErrIDIndex": cpqDaPhyDrvErrIDIndex,
       "cpqDaPhyDrvErrIndex": cpqDaPhyDrvErrIndex,
       "cpqDaPhyDrvErrType": cpqDaPhyDrvErrType,
       "cpqDaPhyDrvScsiOp": cpqDaPhyDrvScsiOp,
       "cpqDaPhyDrvScsiStatus": cpqDaPhyDrvScsiStatus,
       "cpqDaPhyDrvCamStatus": cpqDaPhyDrvCamStatus,
       "cpqDaPhyDrvSenseKey": cpqDaPhyDrvSenseKey,
       "cpqDaPhyDrvQualifier": cpqDaPhyDrvQualifier,
       "cpqDaPhyDrvSenseCode": cpqDaPhyDrvSenseCode,
       "cpqDaPhyDrvBlockValid": cpqDaPhyDrvBlockValid,
       "cpqDaPhyDrvBlock": cpqDaPhyDrvBlock,
       "cpqDaPhyDrvTime": cpqDaPhyDrvTime,
       "cpqDaPhyDrvUserDesc": cpqDaPhyDrvUserDesc,
       "cpqDaPhyDrvErrDesc": cpqDaPhyDrvErrDesc,
       "cpqDaPhyDrvPathTable": cpqDaPhyDrvPathTable,
       "cpqDaPhyDrvPathEntry": cpqDaPhyDrvPathEntry,
       "cpqDaPhyDrvPathCntlrIndex": cpqDaPhyDrvPathCntlrIndex,
       "cpqDaPhyDrvPathDrvIndex": cpqDaPhyDrvPathDrvIndex,
       "cpqDaPhyDrvPathIndex": cpqDaPhyDrvPathIndex,
       "cpqDaPhyDrvPathStatus": cpqDaPhyDrvPathStatus,
       "cpqDaPhyDrvPathCurrentRole": cpqDaPhyDrvPathCurrentRole,
       "cpqDaPhyDrvPathHostConnector": cpqDaPhyDrvPathHostConnector,
       "cpqDaPhyDrvPathBoxOnConnector": cpqDaPhyDrvPathBoxOnConnector,
       "cpqDaPhyDrvPathLocationString": cpqDaPhyDrvPathLocationString,
       "cpqDaPhyDrvThr": cpqDaPhyDrvThr,
       "cpqDaPhyDrvThrTable": cpqDaPhyDrvThrTable,
       "cpqDaPhyDrvThrEntry": cpqDaPhyDrvThrEntry,
       "cpqDaPhyDrvThrCntlrIndex": cpqDaPhyDrvThrCntlrIndex,
       "cpqDaPhyDrvThrIndex": cpqDaPhyDrvThrIndex,
       "cpqDaPhyDrvThrUsedReallocs": cpqDaPhyDrvThrUsedReallocs,
       "cpqDaPhyDrvThrRefHours": cpqDaPhyDrvThrRefHours,
       "cpqDaPhyDrvThrHardReadErrs": cpqDaPhyDrvThrHardReadErrs,
       "cpqDaPhyDrvThrRecvReadErrs": cpqDaPhyDrvThrRecvReadErrs,
       "cpqDaPhyDrvThrHardWriteErrs": cpqDaPhyDrvThrHardWriteErrs,
       "cpqDaPhyDrvThrRecvWriteErrs": cpqDaPhyDrvThrRecvWriteErrs,
       "cpqDaPhyDrvThrHSeekErrs": cpqDaPhyDrvThrHSeekErrs,
       "cpqDaPhyDrvThrSeekErrs": cpqDaPhyDrvThrSeekErrs,
       "cpqDaPhyDrvThrSpinupTime": cpqDaPhyDrvThrSpinupTime,
       "cpqDaPhyDrvThrFunctTest1": cpqDaPhyDrvThrFunctTest1,
       "cpqDaPhyDrvThrFunctTest2": cpqDaPhyDrvThrFunctTest2,
       "cpqDaPhyDrvThrFunctTest3": cpqDaPhyDrvThrFunctTest3,
       "cpqDaPhyDrvThrDrqTimeouts": cpqDaPhyDrvThrDrqTimeouts,
       "cpqDaPhyDrvThrOtherTimeouts": cpqDaPhyDrvThrOtherTimeouts,
       "cpqDaPhyDrvThrSpinupRetries": cpqDaPhyDrvThrSpinupRetries,
       "cpqDaPhyDrvThrBadRecvReads": cpqDaPhyDrvThrBadRecvReads,
       "cpqDaPhyDrvThrBadRecvWrites": cpqDaPhyDrvThrBadRecvWrites,
       "cpqDaPhyDrvThrFormatErrs": cpqDaPhyDrvThrFormatErrs,
       "cpqDaPhyDrvThrPostErrs": cpqDaPhyDrvThrPostErrs,
       "cpqDaPhyDrvThrNotReadyErrs": cpqDaPhyDrvThrNotReadyErrs,
       "cpqDaPhyDrvThrReallocAborts": cpqDaPhyDrvThrReallocAborts,
       "cpqDaPhyDrvThrHotPlugs": cpqDaPhyDrvThrHotPlugs,
       "cpqDaPhyDrvThrMediaErrs": cpqDaPhyDrvThrMediaErrs,
       "cpqDaPhyDrvThrHardwareErrs": cpqDaPhyDrvThrHardwareErrs,
       "cpqDaPhyDrvThrAbortedCmds": cpqDaPhyDrvThrAbortedCmds,
       "cpqDaPhyDrvThrSpinUpErrs": cpqDaPhyDrvThrSpinUpErrs,
       "cpqDaPhyDrvThrBadTargetErrs": cpqDaPhyDrvThrBadTargetErrs,
       "cpqDaPhyDrvThrViUsedReallocs": cpqDaPhyDrvThrViUsedReallocs,
       "cpqDaPhyDrvThrViSpinupTime": cpqDaPhyDrvThrViSpinupTime,
       "cpqDaPhyDrvThrViFunctTest1": cpqDaPhyDrvThrViFunctTest1,
       "cpqDaPhyDrvThrViFunctTest2": cpqDaPhyDrvThrViFunctTest2,
       "cpqDaPhyDrvThrViFunctTest3": cpqDaPhyDrvThrViFunctTest3,
       "cpqDaPhyDrvThrBusFaults": cpqDaPhyDrvThrBusFaults,
       "cpqDaPhyDrvThrIrqDeglitches": cpqDaPhyDrvThrIrqDeglitches,
       "cpqDaCntlrPerf": cpqDaCntlrPerf,
       "cpqDaCntlrPerfTable": cpqDaCntlrPerfTable,
       "cpqDaCntlrPerfEntry": cpqDaCntlrPerfEntry,
       "cpqDaCntlrPerfCntlrIndex": cpqDaCntlrPerfCntlrIndex,
       "cpqDaCntlrPerfInstance": cpqDaCntlrPerfInstance,
       "cpqDaCntlrPerfSampleInterval": cpqDaCntlrPerfSampleInterval,
       "cpqDaCntlrPerfVersion": cpqDaCntlrPerfVersion,
       "cpqDaCntlrPerfCpuPercentBusy": cpqDaCntlrPerfCpuPercentBusy,
       "cpqDaCntlrPerfCommandCount": cpqDaCntlrPerfCommandCount,
       "cpqDaCntlrPerfAvgLatency": cpqDaCntlrPerfAvgLatency,
       "cpqDaLogDrvPerf": cpqDaLogDrvPerf,
       "cpqDaLogDrvPerfTable": cpqDaLogDrvPerfTable,
       "cpqDaLogDrvPerfEntry": cpqDaLogDrvPerfEntry,
       "cpqDaLogDrvPerfCntlrIndex": cpqDaLogDrvPerfCntlrIndex,
       "cpqDaLogDrvPerfIndex": cpqDaLogDrvPerfIndex,
       "cpqDaLogDrvPerfInstance": cpqDaLogDrvPerfInstance,
       "cpqDaLogDrvPerfSampleInterval": cpqDaLogDrvPerfSampleInterval,
       "cpqDaLogDrvPerfAvgQueueDepth": cpqDaLogDrvPerfAvgQueueDepth,
       "cpqDaLogDrvPerfReads": cpqDaLogDrvPerfReads,
       "cpqDaLogDrvPerfWrites": cpqDaLogDrvPerfWrites,
       "cpqDaLogDrvPerfTotalIO": cpqDaLogDrvPerfTotalIO,
       "cpqDaLogDrvPerfCacheHits": cpqDaLogDrvPerfCacheHits,
       "cpqDaLogDrvPerfCacheMisses": cpqDaLogDrvPerfCacheMisses,
       "cpqDaLogDrvPerfReadAheadSectors": cpqDaLogDrvPerfReadAheadSectors,
       "cpqDaLogDrvPerfSectorsRead": cpqDaLogDrvPerfSectorsRead,
       "cpqDaLogDrvPerfSectorsWritten": cpqDaLogDrvPerfSectorsWritten,
       "cpqDaTapeDrv": cpqDaTapeDrv,
       "cpqDaTapeDrvTable": cpqDaTapeDrvTable,
       "cpqDaTapeDrvEntry": cpqDaTapeDrvEntry,
       "cpqDaTapeDrvCntlrIndex": cpqDaTapeDrvCntlrIndex,
       "cpqDaTapeDrvBusIndex": cpqDaTapeDrvBusIndex,
       "cpqDaTapeDrvScsiIdIndex": cpqDaTapeDrvScsiIdIndex,
       "cpqDaTapeDrvLunIndex": cpqDaTapeDrvLunIndex,
       "cpqDaTapeDrvName": cpqDaTapeDrvName,
       "cpqDaTapeDrvSerialNumber": cpqDaTapeDrvSerialNumber,
       "cpqDaTapeDrvFwRev": cpqDaTapeDrvFwRev,
       "cpqDaTapeDrvStatus": cpqDaTapeDrvStatus,
       "cpqDaTapeDrvCondition": cpqDaTapeDrvCondition,
       "cpqDaTapeDrvFwSubtype": cpqDaTapeDrvFwSubtype,
       "cpqDaTapeDrvType": cpqDaTapeDrvType,
       "cpqDaTapeDrvCleanReq": cpqDaTapeDrvCleanReq,
       "cpqDaTapeDrvCleanTapeRepl": cpqDaTapeDrvCleanTapeRepl,
       "cpqDaTapeDrvCleanTapeCount": cpqDaTapeDrvCleanTapeCount,
       "cpqDaTapeDrvLibraryDrive": cpqDaTapeDrvLibraryDrive,
       "cpqDaTapeDrvMagSize": cpqDaTapeDrvMagSize,
       "cpqDaTapeDrvHotPlug": cpqDaTapeDrvHotPlug,
       "cpqDaTapeDrvPlacement": cpqDaTapeDrvPlacement,
       "cpqDaTapeDrvCurrentWidth": cpqDaTapeDrvCurrentWidth,
       "cpqDaTapeDrvCurrentSpeed": cpqDaTapeDrvCurrentSpeed,
       "cpqDaTapeDrvProtocol": cpqDaTapeDrvProtocol,
       "cpqDaTapeDrvNegotiatedLinkRate": cpqDaTapeDrvNegotiatedLinkRate,
       "cpqDaTapeCounters": cpqDaTapeCounters,
       "cpqDaTapeCountersTable": cpqDaTapeCountersTable,
       "cpqDaTapeCountersEntry": cpqDaTapeCountersEntry,
       "cpqDaTapeCountersCntlrIndex": cpqDaTapeCountersCntlrIndex,
       "cpqDaTapeCountersBusIndex": cpqDaTapeCountersBusIndex,
       "cpqDaTapeCountersScsiIdIndex": cpqDaTapeCountersScsiIdIndex,
       "cpqDaTapeCountersLunIndex": cpqDaTapeCountersLunIndex,
       "cpqDaTapeCountersReWrites": cpqDaTapeCountersReWrites,
       "cpqDaTapeCountersReReads": cpqDaTapeCountersReReads,
       "cpqDaTapeCountersTotalErrors": cpqDaTapeCountersTotalErrors,
       "cpqDaTapeCountersTotalUncorrectable": cpqDaTapeCountersTotalUncorrectable,
       "cpqDaTapeCountersTotalBytes": cpqDaTapeCountersTotalBytes,
       "cpqDaTapeLibrary": cpqDaTapeLibrary,
       "cpqDaTapeLibraryTable": cpqDaTapeLibraryTable,
       "cpqDaTapeLibraryEntry": cpqDaTapeLibraryEntry,
       "cpqDaTapeLibraryCntlrIndex": cpqDaTapeLibraryCntlrIndex,
       "cpqDaTapeLibraryScsiBus": cpqDaTapeLibraryScsiBus,
       "cpqDaTapeLibraryScsiTarget": cpqDaTapeLibraryScsiTarget,
       "cpqDaTapeLibraryScsiLun": cpqDaTapeLibraryScsiLun,
       "cpqDaTapeLibrarySerialNumber": cpqDaTapeLibrarySerialNumber,
       "cpqDaTapeLibraryModel": cpqDaTapeLibraryModel,
       "cpqDaTapeLibraryFWRev": cpqDaTapeLibraryFWRev,
       "cpqDaTapeLibraryStatus": cpqDaTapeLibraryStatus,
       "cpqDaTapeLibraryDoorStatus": cpqDaTapeLibraryDoorStatus,
       "cpqDaTapeLibraryCondition": cpqDaTapeLibraryCondition,
       "cpqDaTapeLibraryOverallCondition": cpqDaTapeLibraryOverallCondition,
       "cpqDaTapeLibraryLastError": cpqDaTapeLibraryLastError,
       "cpqDaTapeLibraryStatHours": cpqDaTapeLibraryStatHours,
       "cpqDaTapeLibraryStatMoves": cpqDaTapeLibraryStatMoves,
       "cpqDaTapeLibraryDriveList": cpqDaTapeLibraryDriveList,
       "cpqDaTapeLibraryCurrentWidth": cpqDaTapeLibraryCurrentWidth,
       "cpqDaTapeLibraryCurrentSpeed": cpqDaTapeLibraryCurrentSpeed,
       "cpqDaTapeLibraryDriveList2": cpqDaTapeLibraryDriveList2,
       "cpqDaTapeLibraryProtocol": cpqDaTapeLibraryProtocol,
       "cpqDaTapeLibraryNegotiatedLinkRate": cpqDaTapeLibraryNegotiatedLinkRate,
       "cpqDaTrap": cpqDaTrap,
       "cpqDaTrapPkts": cpqDaTrapPkts,
       "cpqDaTrapLogMaxSize": cpqDaTrapLogMaxSize,
       "cpqDaTrapLogTable": cpqDaTrapLogTable,
       "cpqDaTrapLogEntry": cpqDaTrapLogEntry,
       "cpqDaTrapLogIndex": cpqDaTrapLogIndex,
       "cpqDaTrapType": cpqDaTrapType,
       "cpqDaTrapTime": cpqDaTrapTime}
)
