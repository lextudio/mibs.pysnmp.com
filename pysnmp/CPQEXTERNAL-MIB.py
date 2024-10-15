# SNMP MIB module (CPQEXTERNAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQEXTERNAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:21 2024
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

(compaq,) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq")

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

_CpqExternalMgmt_ObjectIdentity = ObjectIdentity
cpqExternalMgmt = _CpqExternalMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 17)
)
_CpqExMibRev_ObjectIdentity = ObjectIdentity
cpqExMibRev = _CpqExMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 17, 1)
)


class _CpqExMibRevMajor_Type(Integer32):
    """Custom type cpqExMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqExMibRevMajor_Type.__name__ = "Integer32"
_CpqExMibRevMajor_Object = MibScalar
cpqExMibRevMajor = _CpqExMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 1, 1),
    _CpqExMibRevMajor_Type()
)
cpqExMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExMibRevMajor.setStatus("mandatory")


class _CpqExMibRevMinor_Type(Integer32):
    """Custom type cpqExMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqExMibRevMinor_Type.__name__ = "Integer32"
_CpqExMibRevMinor_Object = MibScalar
cpqExMibRevMinor = _CpqExMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 1, 2),
    _CpqExMibRevMinor_Type()
)
cpqExMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExMibRevMinor.setStatus("mandatory")


class _CpqExMibCondition_Type(Integer32):
    """Custom type cpqExMibCondition based on Integer32"""
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


_CpqExMibCondition_Type.__name__ = "Integer32"
_CpqExMibCondition_Object = MibScalar
cpqExMibCondition = _CpqExMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 1, 3),
    _CpqExMibCondition_Type()
)
cpqExMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExMibCondition.setStatus("mandatory")
_CpqExComponent_ObjectIdentity = ObjectIdentity
cpqExComponent = _CpqExComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 17, 2)
)
_CpqExInterface_ObjectIdentity = ObjectIdentity
cpqExInterface = _CpqExInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 1)
)
_CpqExOsCommon_ObjectIdentity = ObjectIdentity
cpqExOsCommon = _CpqExOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4)
)


class _CpqExOsCommonPollFreq_Type(Integer32):
    """Custom type cpqExOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqExOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqExOsCommonPollFreq_Object = MibScalar
cpqExOsCommonPollFreq = _CpqExOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 1),
    _CpqExOsCommonPollFreq_Type()
)
cpqExOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqExOsCommonPollFreq.setStatus("mandatory")
_CpqExOsCommonModuleTable_Object = MibTable
cpqExOsCommonModuleTable = _CpqExOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqExOsCommonModuleTable.setStatus("deprecated")
_CpqExOsCommonModuleEntry_Object = MibTableRow
cpqExOsCommonModuleEntry = _CpqExOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1)
)
cpqExOsCommonModuleEntry.setIndexNames(
    (0, "CPQEXTERNAL-MIB", "cpqExOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqExOsCommonModuleEntry.setStatus("deprecated")


class _CpqExOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqExOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqExOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqExOsCommonModuleIndex_Object = MibTableColumn
cpqExOsCommonModuleIndex = _CpqExOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1, 1),
    _CpqExOsCommonModuleIndex_Type()
)
cpqExOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExOsCommonModuleIndex.setStatus("deprecated")


class _CpqExOsCommonModuleName_Type(DisplayString):
    """Custom type cpqExOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqExOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqExOsCommonModuleName_Object = MibTableColumn
cpqExOsCommonModuleName = _CpqExOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1, 2),
    _CpqExOsCommonModuleName_Type()
)
cpqExOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExOsCommonModuleName.setStatus("deprecated")


class _CpqExOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqExOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqExOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqExOsCommonModuleVersion_Object = MibTableColumn
cpqExOsCommonModuleVersion = _CpqExOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1, 3),
    _CpqExOsCommonModuleVersion_Type()
)
cpqExOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExOsCommonModuleVersion.setStatus("deprecated")


class _CpqExOsCommonModuleDate_Type(OctetString):
    """Custom type cpqExOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqExOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqExOsCommonModuleDate_Object = MibTableColumn
cpqExOsCommonModuleDate = _CpqExOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1, 4),
    _CpqExOsCommonModuleDate_Type()
)
cpqExOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExOsCommonModuleDate.setStatus("deprecated")


class _CpqExOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqExOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqExOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqExOsCommonModulePurpose_Object = MibTableColumn
cpqExOsCommonModulePurpose = _CpqExOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 1, 4, 2, 1, 5),
    _CpqExOsCommonModulePurpose_Type()
)
cpqExOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExOsCommonModulePurpose.setStatus("deprecated")
_CpqExStatus_ObjectIdentity = ObjectIdentity
cpqExStatus = _CpqExStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2)
)


class _CpqExExternalCondition_Type(Integer32):
    """Custom type cpqExExternalCondition based on Integer32"""
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


_CpqExExternalCondition_Type.__name__ = "Integer32"
_CpqExExternalCondition_Object = MibScalar
cpqExExternalCondition = _CpqExExternalCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 1),
    _CpqExExternalCondition_Type()
)
cpqExExternalCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExExternalCondition.setStatus("mandatory")
_CpqExExternalStatusTable_Object = MibTable
cpqExExternalStatusTable = _CpqExExternalStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cpqExExternalStatusTable.setStatus("mandatory")
_CpqExExternalStatusEntry_Object = MibTableRow
cpqExExternalStatusEntry = _CpqExExternalStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1)
)
cpqExExternalStatusEntry.setIndexNames(
    (0, "CPQEXTERNAL-MIB", "cpqExExternalStatusIndex"),
)
if mibBuilder.loadTexts:
    cpqExExternalStatusEntry.setStatus("mandatory")
_CpqExExternalStatusIndex_Type = Integer32
_CpqExExternalStatusIndex_Object = MibTableColumn
cpqExExternalStatusIndex = _CpqExExternalStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 1),
    _CpqExExternalStatusIndex_Type()
)
cpqExExternalStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExExternalStatusIndex.setStatus("mandatory")
_CpqExExternalStatusInterval_Type = Integer32
_CpqExExternalStatusInterval_Object = MibTableColumn
cpqExExternalStatusInterval = _CpqExExternalStatusInterval_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 2),
    _CpqExExternalStatusInterval_Type()
)
cpqExExternalStatusInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExExternalStatusInterval.setStatus("mandatory")
_CpqExExternalStatusVariable_Type = ObjectIdentifier
_CpqExExternalStatusVariable_Object = MibTableColumn
cpqExExternalStatusVariable = _CpqExExternalStatusVariable_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 3),
    _CpqExExternalStatusVariable_Type()
)
cpqExExternalStatusVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExExternalStatusVariable.setStatus("mandatory")


class _CpqExExternalStatusValid_Type(Integer32):
    """Custom type cpqExExternalStatusValid based on Integer32"""
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


_CpqExExternalStatusValid_Type.__name__ = "Integer32"
_CpqExExternalStatusValid_Object = MibTableColumn
cpqExExternalStatusValid = _CpqExExternalStatusValid_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 4),
    _CpqExExternalStatusValid_Type()
)
cpqExExternalStatusValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExExternalStatusValid.setStatus("mandatory")
_CpqExExternalStatusValue_Type = Integer32
_CpqExExternalStatusValue_Object = MibTableColumn
cpqExExternalStatusValue = _CpqExExternalStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 5),
    _CpqExExternalStatusValue_Type()
)
cpqExExternalStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExExternalStatusValue.setStatus("mandatory")


class _CpqExExternalStatusCondition_Type(Integer32):
    """Custom type cpqExExternalStatusCondition based on Integer32"""
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


_CpqExExternalStatusCondition_Type.__name__ = "Integer32"
_CpqExExternalStatusCondition_Object = MibTableColumn
cpqExExternalStatusCondition = _CpqExExternalStatusCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 6),
    _CpqExExternalStatusCondition_Type()
)
cpqExExternalStatusCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExExternalStatusCondition.setStatus("mandatory")


class _CpqExExternalStatusOkValues_Type(DisplayString):
    """Custom type cpqExExternalStatusOkValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqExExternalStatusOkValues_Type.__name__ = "DisplayString"
_CpqExExternalStatusOkValues_Object = MibTableColumn
cpqExExternalStatusOkValues = _CpqExExternalStatusOkValues_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 7),
    _CpqExExternalStatusOkValues_Type()
)
cpqExExternalStatusOkValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExExternalStatusOkValues.setStatus("mandatory")


class _CpqExExternalStatusDegradedValues_Type(DisplayString):
    """Custom type cpqExExternalStatusDegradedValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqExExternalStatusDegradedValues_Type.__name__ = "DisplayString"
_CpqExExternalStatusDegradedValues_Object = MibTableColumn
cpqExExternalStatusDegradedValues = _CpqExExternalStatusDegradedValues_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 8),
    _CpqExExternalStatusDegradedValues_Type()
)
cpqExExternalStatusDegradedValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExExternalStatusDegradedValues.setStatus("mandatory")


class _CpqExExternalStatusFailedValues_Type(DisplayString):
    """Custom type cpqExExternalStatusFailedValues based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqExExternalStatusFailedValues_Type.__name__ = "DisplayString"
_CpqExExternalStatusFailedValues_Object = MibTableColumn
cpqExExternalStatusFailedValues = _CpqExExternalStatusFailedValues_Object(
    (1, 3, 6, 1, 4, 1, 232, 17, 2, 2, 2, 1, 9),
    _CpqExExternalStatusFailedValues_Type()
)
cpqExExternalStatusFailedValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqExExternalStatusFailedValues.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQEXTERNAL-MIB",
    **{"cpqExternalMgmt": cpqExternalMgmt,
       "cpqExMibRev": cpqExMibRev,
       "cpqExMibRevMajor": cpqExMibRevMajor,
       "cpqExMibRevMinor": cpqExMibRevMinor,
       "cpqExMibCondition": cpqExMibCondition,
       "cpqExComponent": cpqExComponent,
       "cpqExInterface": cpqExInterface,
       "cpqExOsCommon": cpqExOsCommon,
       "cpqExOsCommonPollFreq": cpqExOsCommonPollFreq,
       "cpqExOsCommonModuleTable": cpqExOsCommonModuleTable,
       "cpqExOsCommonModuleEntry": cpqExOsCommonModuleEntry,
       "cpqExOsCommonModuleIndex": cpqExOsCommonModuleIndex,
       "cpqExOsCommonModuleName": cpqExOsCommonModuleName,
       "cpqExOsCommonModuleVersion": cpqExOsCommonModuleVersion,
       "cpqExOsCommonModuleDate": cpqExOsCommonModuleDate,
       "cpqExOsCommonModulePurpose": cpqExOsCommonModulePurpose,
       "cpqExStatus": cpqExStatus,
       "cpqExExternalCondition": cpqExExternalCondition,
       "cpqExExternalStatusTable": cpqExExternalStatusTable,
       "cpqExExternalStatusEntry": cpqExExternalStatusEntry,
       "cpqExExternalStatusIndex": cpqExExternalStatusIndex,
       "cpqExExternalStatusInterval": cpqExExternalStatusInterval,
       "cpqExExternalStatusVariable": cpqExExternalStatusVariable,
       "cpqExExternalStatusValid": cpqExExternalStatusValid,
       "cpqExExternalStatusValue": cpqExExternalStatusValue,
       "cpqExExternalStatusCondition": cpqExExternalStatusCondition,
       "cpqExExternalStatusOkValues": cpqExExternalStatusOkValues,
       "cpqExExternalStatusDegradedValues": cpqExExternalStatusDegradedValues,
       "cpqExExternalStatusFailedValues": cpqExExternalStatusFailedValues}
)
