# SNMP MIB module (CPQTHRSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQTHRSH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:46 2024
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

_CpqThresholdMgmt_ObjectIdentity = ObjectIdentity
cpqThresholdMgmt = _CpqThresholdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 10)
)
_CpqMeMibRev_ObjectIdentity = ObjectIdentity
cpqMeMibRev = _CpqMeMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 10, 1)
)


class _CpqMeMibRevMajor_Type(Integer32):
    """Custom type cpqMeMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqMeMibRevMajor_Type.__name__ = "Integer32"
_CpqMeMibRevMajor_Object = MibScalar
cpqMeMibRevMajor = _CpqMeMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 1, 1),
    _CpqMeMibRevMajor_Type()
)
cpqMeMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeMibRevMajor.setStatus("mandatory")


class _CpqMeMibRevMinor_Type(Integer32):
    """Custom type cpqMeMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqMeMibRevMinor_Type.__name__ = "Integer32"
_CpqMeMibRevMinor_Object = MibScalar
cpqMeMibRevMinor = _CpqMeMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 1, 2),
    _CpqMeMibRevMinor_Type()
)
cpqMeMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeMibRevMinor.setStatus("mandatory")


class _CpqMeMibCondition_Type(Integer32):
    """Custom type cpqMeMibCondition based on Integer32"""
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


_CpqMeMibCondition_Type.__name__ = "Integer32"
_CpqMeMibCondition_Object = MibScalar
cpqMeMibCondition = _CpqMeMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 1, 3),
    _CpqMeMibCondition_Type()
)
cpqMeMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeMibCondition.setStatus("mandatory")
_CpqMeComponent_ObjectIdentity = ObjectIdentity
cpqMeComponent = _CpqMeComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 10, 2)
)
_CpqMeInterface_ObjectIdentity = ObjectIdentity
cpqMeInterface = _CpqMeInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 1)
)
_CpqMeOsCommon_ObjectIdentity = ObjectIdentity
cpqMeOsCommon = _CpqMeOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4)
)


class _CpqMeOsCommonPollFreq_Type(Integer32):
    """Custom type cpqMeOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpqMeOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqMeOsCommonPollFreq_Object = MibScalar
cpqMeOsCommonPollFreq = _CpqMeOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 1),
    _CpqMeOsCommonPollFreq_Type()
)
cpqMeOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeOsCommonPollFreq.setStatus("mandatory")
_CpqMeOsCommonModuleTable_Object = MibTable
cpqMeOsCommonModuleTable = _CpqMeOsCommonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpqMeOsCommonModuleTable.setStatus("deprecated")
_CpqMeOsCommonModuleEntry_Object = MibTableRow
cpqMeOsCommonModuleEntry = _CpqMeOsCommonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1)
)
cpqMeOsCommonModuleEntry.setIndexNames(
    (0, "CPQTHRSH-MIB", "cpqMeOsCommonModuleIndex"),
)
if mibBuilder.loadTexts:
    cpqMeOsCommonModuleEntry.setStatus("deprecated")


class _CpqMeOsCommonModuleIndex_Type(Integer32):
    """Custom type cpqMeOsCommonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqMeOsCommonModuleIndex_Type.__name__ = "Integer32"
_CpqMeOsCommonModuleIndex_Object = MibTableColumn
cpqMeOsCommonModuleIndex = _CpqMeOsCommonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1, 1),
    _CpqMeOsCommonModuleIndex_Type()
)
cpqMeOsCommonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeOsCommonModuleIndex.setStatus("deprecated")


class _CpqMeOsCommonModuleName_Type(DisplayString):
    """Custom type cpqMeOsCommonModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqMeOsCommonModuleName_Type.__name__ = "DisplayString"
_CpqMeOsCommonModuleName_Object = MibTableColumn
cpqMeOsCommonModuleName = _CpqMeOsCommonModuleName_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1, 2),
    _CpqMeOsCommonModuleName_Type()
)
cpqMeOsCommonModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeOsCommonModuleName.setStatus("deprecated")


class _CpqMeOsCommonModuleVersion_Type(DisplayString):
    """Custom type cpqMeOsCommonModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqMeOsCommonModuleVersion_Type.__name__ = "DisplayString"
_CpqMeOsCommonModuleVersion_Object = MibTableColumn
cpqMeOsCommonModuleVersion = _CpqMeOsCommonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1, 3),
    _CpqMeOsCommonModuleVersion_Type()
)
cpqMeOsCommonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeOsCommonModuleVersion.setStatus("deprecated")


class _CpqMeOsCommonModuleDate_Type(OctetString):
    """Custom type cpqMeOsCommonModuleDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CpqMeOsCommonModuleDate_Type.__name__ = "OctetString"
_CpqMeOsCommonModuleDate_Object = MibTableColumn
cpqMeOsCommonModuleDate = _CpqMeOsCommonModuleDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1, 4),
    _CpqMeOsCommonModuleDate_Type()
)
cpqMeOsCommonModuleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeOsCommonModuleDate.setStatus("deprecated")


class _CpqMeOsCommonModulePurpose_Type(DisplayString):
    """Custom type cpqMeOsCommonModulePurpose based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqMeOsCommonModulePurpose_Type.__name__ = "DisplayString"
_CpqMeOsCommonModulePurpose_Object = MibTableColumn
cpqMeOsCommonModulePurpose = _CpqMeOsCommonModulePurpose_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 1, 4, 2, 1, 5),
    _CpqMeOsCommonModulePurpose_Type()
)
cpqMeOsCommonModulePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeOsCommonModulePurpose.setStatus("deprecated")
_CpqMeAlarm_ObjectIdentity = ObjectIdentity
cpqMeAlarm = _CpqMeAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2)
)
_CpqMeAlarmNextIndex_Type = Integer32
_CpqMeAlarmNextIndex_Object = MibScalar
cpqMeAlarmNextIndex = _CpqMeAlarmNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 1),
    _CpqMeAlarmNextIndex_Type()
)
cpqMeAlarmNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeAlarmNextIndex.setStatus("mandatory")
_CpqMeAlarmTable_Object = MibTable
cpqMeAlarmTable = _CpqMeAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cpqMeAlarmTable.setStatus("mandatory")
_CpqMeAlarmEntry_Object = MibTableRow
cpqMeAlarmEntry = _CpqMeAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1)
)
cpqMeAlarmEntry.setIndexNames(
    (0, "CPQTHRSH-MIB", "cpqMeAlarmIndex"),
)
if mibBuilder.loadTexts:
    cpqMeAlarmEntry.setStatus("mandatory")


class _CpqMeAlarmIndex_Type(Integer32):
    """Custom type cpqMeAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqMeAlarmIndex_Type.__name__ = "Integer32"
_CpqMeAlarmIndex_Object = MibTableColumn
cpqMeAlarmIndex = _CpqMeAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 1),
    _CpqMeAlarmIndex_Type()
)
cpqMeAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeAlarmIndex.setStatus("mandatory")


class _CpqMeAlarmInterval_Type(Integer32):
    """Custom type cpqMeAlarmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpqMeAlarmInterval_Type.__name__ = "Integer32"
_CpqMeAlarmInterval_Object = MibTableColumn
cpqMeAlarmInterval = _CpqMeAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 2),
    _CpqMeAlarmInterval_Type()
)
cpqMeAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmInterval.setStatus("mandatory")
_CpqMeAlarmVariable_Type = ObjectIdentifier
_CpqMeAlarmVariable_Object = MibTableColumn
cpqMeAlarmVariable = _CpqMeAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 3),
    _CpqMeAlarmVariable_Type()
)
cpqMeAlarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmVariable.setStatus("mandatory")


class _CpqMeAlarmSampleType_Type(Integer32):
    """Custom type cpqMeAlarmSampleType based on Integer32"""
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
        *(("absSuppressFallingTrap", 4),
          ("absSuppressRisingTrap", 3),
          ("absoluteValue", 1),
          ("deltaValue", 2))
    )


_CpqMeAlarmSampleType_Type.__name__ = "Integer32"
_CpqMeAlarmSampleType_Object = MibTableColumn
cpqMeAlarmSampleType = _CpqMeAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 4),
    _CpqMeAlarmSampleType_Type()
)
cpqMeAlarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmSampleType.setStatus("mandatory")
_CpqMeAlarmValue_Type = Integer32
_CpqMeAlarmValue_Object = MibTableColumn
cpqMeAlarmValue = _CpqMeAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 5),
    _CpqMeAlarmValue_Type()
)
cpqMeAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqMeAlarmValue.setStatus("mandatory")


class _CpqMeAlarmStartupAlarm_Type(Integer32):
    """Custom type cpqMeAlarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1),
          ("risingOrFallingAlarm", 3))
    )


_CpqMeAlarmStartupAlarm_Type.__name__ = "Integer32"
_CpqMeAlarmStartupAlarm_Object = MibTableColumn
cpqMeAlarmStartupAlarm = _CpqMeAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 6),
    _CpqMeAlarmStartupAlarm_Type()
)
cpqMeAlarmStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmStartupAlarm.setStatus("mandatory")
_CpqMeAlarmRisingThreshold_Type = Integer32
_CpqMeAlarmRisingThreshold_Object = MibTableColumn
cpqMeAlarmRisingThreshold = _CpqMeAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 7),
    _CpqMeAlarmRisingThreshold_Type()
)
cpqMeAlarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmRisingThreshold.setStatus("mandatory")
_CpqMeAlarmFallingThreshold_Type = Integer32
_CpqMeAlarmFallingThreshold_Object = MibTableColumn
cpqMeAlarmFallingThreshold = _CpqMeAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 8),
    _CpqMeAlarmFallingThreshold_Type()
)
cpqMeAlarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmFallingThreshold.setStatus("mandatory")


class _CpqMeAlarmPermanence_Type(Integer32):
    """Custom type cpqMeAlarmPermanence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 2),
          ("temporary", 1))
    )


_CpqMeAlarmPermanence_Type.__name__ = "Integer32"
_CpqMeAlarmPermanence_Object = MibTableColumn
cpqMeAlarmPermanence = _CpqMeAlarmPermanence_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 9),
    _CpqMeAlarmPermanence_Type()
)
cpqMeAlarmPermanence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmPermanence.setStatus("mandatory")


class _CpqMeAlarmOwner_Type(DisplayString):
    """Custom type cpqMeAlarmOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CpqMeAlarmOwner_Type.__name__ = "DisplayString"
_CpqMeAlarmOwner_Object = MibTableColumn
cpqMeAlarmOwner = _CpqMeAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 10),
    _CpqMeAlarmOwner_Type()
)
cpqMeAlarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmOwner.setStatus("mandatory")


class _CpqMeAlarmStatus_Type(Integer32):
    """Custom type cpqMeAlarmStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("tempUnavailable", 5),
          ("underCreation", 3),
          ("valid", 1))
    )


_CpqMeAlarmStatus_Type.__name__ = "Integer32"
_CpqMeAlarmStatus_Object = MibTableColumn
cpqMeAlarmStatus = _CpqMeAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 11),
    _CpqMeAlarmStatus_Type()
)
cpqMeAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmStatus.setStatus("mandatory")


class _CpqMeAlarmSeverity_Type(Integer32):
    """Custom type cpqMeAlarmSeverity based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 3),
          ("normal", 2),
          ("unknown", 1),
          ("warning", 4))
    )


_CpqMeAlarmSeverity_Type.__name__ = "Integer32"
_CpqMeAlarmSeverity_Object = MibTableColumn
cpqMeAlarmSeverity = _CpqMeAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 12),
    _CpqMeAlarmSeverity_Type()
)
cpqMeAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmSeverity.setStatus("mandatory")


class _CpqMeAlarmExtendedDescription_Type(DisplayString):
    """Custom type cpqMeAlarmExtendedDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CpqMeAlarmExtendedDescription_Type.__name__ = "DisplayString"
_CpqMeAlarmExtendedDescription_Object = MibTableColumn
cpqMeAlarmExtendedDescription = _CpqMeAlarmExtendedDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 10, 2, 2, 2, 1, 13),
    _CpqMeAlarmExtendedDescription_Type()
)
cpqMeAlarmExtendedDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqMeAlarmExtendedDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqMeRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 10001)
)
cpqMeRisingAlarm.setObjects(
      *(("CPQTHRSH-MIB", "cpqMeAlarmVariable"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"),
        ("CPQTHRSH-MIB", "cpqMeAlarmValue"),
        ("CPQTHRSH-MIB", "cpqMeAlarmRisingThreshold"),
        ("CPQTHRSH-MIB", "cpqMeAlarmOwner"))
)
if mibBuilder.loadTexts:
    cpqMeRisingAlarm.setStatus(
        ""
    )

cpqMeFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 10002)
)
cpqMeFallingAlarm.setObjects(
      *(("CPQTHRSH-MIB", "cpqMeAlarmVariable"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"),
        ("CPQTHRSH-MIB", "cpqMeAlarmValue"),
        ("CPQTHRSH-MIB", "cpqMeAlarmFallingThreshold"),
        ("CPQTHRSH-MIB", "cpqMeAlarmOwner"))
)
if mibBuilder.loadTexts:
    cpqMeFallingAlarm.setStatus(
        ""
    )

cpqMe2RisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 10003)
)
cpqMe2RisingAlarm.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQTHRSH-MIB", "cpqMeAlarmVariable"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"),
        ("CPQTHRSH-MIB", "cpqMeAlarmValue"),
        ("CPQTHRSH-MIB", "cpqMeAlarmRisingThreshold"),
        ("CPQTHRSH-MIB", "cpqMeAlarmOwner"))
)
if mibBuilder.loadTexts:
    cpqMe2RisingAlarm.setStatus(
        ""
    )

cpqMe2FallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 10004)
)
cpqMe2FallingAlarm.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQTHRSH-MIB", "cpqMeAlarmVariable"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"),
        ("CPQTHRSH-MIB", "cpqMeAlarmValue"),
        ("CPQTHRSH-MIB", "cpqMeAlarmFallingThreshold"),
        ("CPQTHRSH-MIB", "cpqMeAlarmOwner"))
)
if mibBuilder.loadTexts:
    cpqMe2FallingAlarm.setStatus(
        ""
    )

cpqMeRisingAlarmExtended = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 10005)
)
cpqMeRisingAlarmExtended.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQTHRSH-MIB", "cpqMeAlarmVariable"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"),
        ("CPQTHRSH-MIB", "cpqMeAlarmValue"),
        ("CPQTHRSH-MIB", "cpqMeAlarmRisingThreshold"),
        ("CPQTHRSH-MIB", "cpqMeAlarmOwner"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSeverity"),
        ("CPQTHRSH-MIB", "cpqMeAlarmExtendedDescription"))
)
if mibBuilder.loadTexts:
    cpqMeRisingAlarmExtended.setStatus(
        ""
    )

cpqMeFallingAlarmExtended = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 10006)
)
cpqMeFallingAlarmExtended.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQTHRSH-MIB", "cpqMeAlarmVariable"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"),
        ("CPQTHRSH-MIB", "cpqMeAlarmValue"),
        ("CPQTHRSH-MIB", "cpqMeAlarmFallingThreshold"),
        ("CPQTHRSH-MIB", "cpqMeAlarmOwner"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSeverity"),
        ("CPQTHRSH-MIB", "cpqMeAlarmExtendedDescription"))
)
if mibBuilder.loadTexts:
    cpqMeFallingAlarmExtended.setStatus(
        ""
    )

cpqMeCriticalRisingAlarmExtended = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 10007)
)
cpqMeCriticalRisingAlarmExtended.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQTHRSH-MIB", "cpqMeAlarmVariable"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"),
        ("CPQTHRSH-MIB", "cpqMeAlarmValue"),
        ("CPQTHRSH-MIB", "cpqMeAlarmRisingThreshold"),
        ("CPQTHRSH-MIB", "cpqMeAlarmOwner"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSeverity"),
        ("CPQTHRSH-MIB", "cpqMeAlarmExtendedDescription"))
)
if mibBuilder.loadTexts:
    cpqMeCriticalRisingAlarmExtended.setStatus(
        ""
    )

cpqMeCriticalFallingAlarmExtended = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 10008)
)
cpqMeCriticalFallingAlarmExtended.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQTHRSH-MIB", "cpqMeAlarmVariable"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSampleType"),
        ("CPQTHRSH-MIB", "cpqMeAlarmValue"),
        ("CPQTHRSH-MIB", "cpqMeAlarmFallingThreshold"),
        ("CPQTHRSH-MIB", "cpqMeAlarmOwner"),
        ("CPQTHRSH-MIB", "cpqMeAlarmSeverity"),
        ("CPQTHRSH-MIB", "cpqMeAlarmExtendedDescription"))
)
if mibBuilder.loadTexts:
    cpqMeCriticalFallingAlarmExtended.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQTHRSH-MIB",
    **{"cpqMeRisingAlarm": cpqMeRisingAlarm,
       "cpqMeFallingAlarm": cpqMeFallingAlarm,
       "cpqMe2RisingAlarm": cpqMe2RisingAlarm,
       "cpqMe2FallingAlarm": cpqMe2FallingAlarm,
       "cpqMeRisingAlarmExtended": cpqMeRisingAlarmExtended,
       "cpqMeFallingAlarmExtended": cpqMeFallingAlarmExtended,
       "cpqMeCriticalRisingAlarmExtended": cpqMeCriticalRisingAlarmExtended,
       "cpqMeCriticalFallingAlarmExtended": cpqMeCriticalFallingAlarmExtended,
       "cpqThresholdMgmt": cpqThresholdMgmt,
       "cpqMeMibRev": cpqMeMibRev,
       "cpqMeMibRevMajor": cpqMeMibRevMajor,
       "cpqMeMibRevMinor": cpqMeMibRevMinor,
       "cpqMeMibCondition": cpqMeMibCondition,
       "cpqMeComponent": cpqMeComponent,
       "cpqMeInterface": cpqMeInterface,
       "cpqMeOsCommon": cpqMeOsCommon,
       "cpqMeOsCommonPollFreq": cpqMeOsCommonPollFreq,
       "cpqMeOsCommonModuleTable": cpqMeOsCommonModuleTable,
       "cpqMeOsCommonModuleEntry": cpqMeOsCommonModuleEntry,
       "cpqMeOsCommonModuleIndex": cpqMeOsCommonModuleIndex,
       "cpqMeOsCommonModuleName": cpqMeOsCommonModuleName,
       "cpqMeOsCommonModuleVersion": cpqMeOsCommonModuleVersion,
       "cpqMeOsCommonModuleDate": cpqMeOsCommonModuleDate,
       "cpqMeOsCommonModulePurpose": cpqMeOsCommonModulePurpose,
       "cpqMeAlarm": cpqMeAlarm,
       "cpqMeAlarmNextIndex": cpqMeAlarmNextIndex,
       "cpqMeAlarmTable": cpqMeAlarmTable,
       "cpqMeAlarmEntry": cpqMeAlarmEntry,
       "cpqMeAlarmIndex": cpqMeAlarmIndex,
       "cpqMeAlarmInterval": cpqMeAlarmInterval,
       "cpqMeAlarmVariable": cpqMeAlarmVariable,
       "cpqMeAlarmSampleType": cpqMeAlarmSampleType,
       "cpqMeAlarmValue": cpqMeAlarmValue,
       "cpqMeAlarmStartupAlarm": cpqMeAlarmStartupAlarm,
       "cpqMeAlarmRisingThreshold": cpqMeAlarmRisingThreshold,
       "cpqMeAlarmFallingThreshold": cpqMeAlarmFallingThreshold,
       "cpqMeAlarmPermanence": cpqMeAlarmPermanence,
       "cpqMeAlarmOwner": cpqMeAlarmOwner,
       "cpqMeAlarmStatus": cpqMeAlarmStatus,
       "cpqMeAlarmSeverity": cpqMeAlarmSeverity,
       "cpqMeAlarmExtendedDescription": cpqMeAlarmExtendedDescription}
)
