# SNMP MIB module (VISINET2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VISINET2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:38 2024
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

_Unisys_ObjectIdentity = ObjectIdentity
unisys = _Unisys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223)
)
_UnisysOpen_ObjectIdentity = ObjectIdentity
unisysOpen = _UnisysOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10)
)
_UnisysEnvMonitor_ObjectIdentity = ObjectIdentity
unisysEnvMonitor = _UnisysEnvMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 6)
)


class _UemAgentRevMajor_Type(Integer32):
    """Custom type uemAgentRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UemAgentRevMajor_Type.__name__ = "Integer32"
_UemAgentRevMajor_Object = MibScalar
uemAgentRevMajor = _UemAgentRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 2),
    _UemAgentRevMajor_Type()
)
uemAgentRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemAgentRevMajor.setStatus("mandatory")


class _UemAgentRevMinor_Type(Integer32):
    """Custom type uemAgentRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UemAgentRevMinor_Type.__name__ = "Integer32"
_UemAgentRevMinor_Object = MibScalar
uemAgentRevMinor = _UemAgentRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 3),
    _UemAgentRevMinor_Type()
)
uemAgentRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemAgentRevMinor.setStatus("mandatory")


class _UemMibRevMajor_Type(Integer32):
    """Custom type uemMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UemMibRevMajor_Type.__name__ = "Integer32"
_UemMibRevMajor_Object = MibScalar
uemMibRevMajor = _UemMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 4),
    _UemMibRevMajor_Type()
)
uemMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemMibRevMajor.setStatus("mandatory")


class _UemMibRevMinor_Type(Integer32):
    """Custom type uemMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UemMibRevMinor_Type.__name__ = "Integer32"
_UemMibRevMinor_Object = MibScalar
uemMibRevMinor = _UemMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 5),
    _UemMibRevMinor_Type()
)
uemMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemMibRevMinor.setStatus("mandatory")


class _UemSystemDescription_Type(DisplayString):
    """Custom type uemSystemDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UemSystemDescription_Type.__name__ = "DisplayString"
_UemSystemDescription_Object = MibScalar
uemSystemDescription = _UemSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 7),
    _UemSystemDescription_Type()
)
uemSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSystemDescription.setStatus("mandatory")


class _UemTrapsEnabled_Type(Integer32):
    """Custom type uemTrapsEnabled based on Integer32"""
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


_UemTrapsEnabled_Type.__name__ = "Integer32"
_UemTrapsEnabled_Object = MibScalar
uemTrapsEnabled = _UemTrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 8),
    _UemTrapsEnabled_Type()
)
uemTrapsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uemTrapsEnabled.setStatus("mandatory")
_UemTrapSeverity_Type = Integer32
_UemTrapSeverity_Object = MibScalar
uemTrapSeverity = _UemTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 9),
    _UemTrapSeverity_Type()
)
uemTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemTrapSeverity.setStatus("mandatory")
_UemEnvMonitorTable_Object = MibTable
uemEnvMonitorTable = _UemEnvMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 16)
)
if mibBuilder.loadTexts:
    uemEnvMonitorTable.setStatus("mandatory")
_UemEnvMonitorTableEntry_Object = MibTableRow
uemEnvMonitorTableEntry = _UemEnvMonitorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 16, 1)
)
uemEnvMonitorTableEntry.setIndexNames(
    (0, "VISINET2-MIB", "uemEnvMonIndex"),
)
if mibBuilder.loadTexts:
    uemEnvMonitorTableEntry.setStatus("mandatory")
_UemEnvMonIndex_Type = Integer32
_UemEnvMonIndex_Object = MibTableColumn
uemEnvMonIndex = _UemEnvMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 16, 1, 1),
    _UemEnvMonIndex_Type()
)
uemEnvMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemEnvMonIndex.setStatus("mandatory")


class _UemEnvMonLocation_Type(DisplayString):
    """Custom type uemEnvMonLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UemEnvMonLocation_Type.__name__ = "DisplayString"
_UemEnvMonLocation_Object = MibTableColumn
uemEnvMonLocation = _UemEnvMonLocation_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 16, 1, 2),
    _UemEnvMonLocation_Type()
)
uemEnvMonLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemEnvMonLocation.setStatus("mandatory")


class _UemEnvMonType_Type(Integer32):
    """Custom type uemEnvMonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alrSHM", 2),
          ("unknown", 1))
    )


_UemEnvMonType_Type.__name__ = "Integer32"
_UemEnvMonType_Object = MibTableColumn
uemEnvMonType = _UemEnvMonType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 16, 1, 3),
    _UemEnvMonType_Type()
)
uemEnvMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemEnvMonType.setStatus("mandatory")


class _UemEnvMonFwRevMajor_Type(Integer32):
    """Custom type uemEnvMonFwRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UemEnvMonFwRevMajor_Type.__name__ = "Integer32"
_UemEnvMonFwRevMajor_Object = MibTableColumn
uemEnvMonFwRevMajor = _UemEnvMonFwRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 16, 1, 5),
    _UemEnvMonFwRevMajor_Type()
)
uemEnvMonFwRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemEnvMonFwRevMajor.setStatus("mandatory")


class _UemEnvMonFwRevMinor_Type(Integer32):
    """Custom type uemEnvMonFwRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UemEnvMonFwRevMinor_Type.__name__ = "Integer32"
_UemEnvMonFwRevMinor_Object = MibTableColumn
uemEnvMonFwRevMinor = _UemEnvMonFwRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 16, 1, 6),
    _UemEnvMonFwRevMinor_Type()
)
uemEnvMonFwRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemEnvMonFwRevMinor.setStatus("mandatory")


class _UemEnvMonFwRelDate_Type(DisplayString):
    """Custom type uemEnvMonFwRelDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UemEnvMonFwRelDate_Type.__name__ = "DisplayString"
_UemEnvMonFwRelDate_Object = MibTableColumn
uemEnvMonFwRelDate = _UemEnvMonFwRelDate_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 16, 1, 7),
    _UemEnvMonFwRelDate_Type()
)
uemEnvMonFwRelDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemEnvMonFwRelDate.setStatus("mandatory")
_UemEnvMonUpTime_Type = TimeTicks
_UemEnvMonUpTime_Object = MibTableColumn
uemEnvMonUpTime = _UemEnvMonUpTime_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 16, 1, 8),
    _UemEnvMonUpTime_Type()
)
uemEnvMonUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemEnvMonUpTime.setStatus("mandatory")
_UemSensorTable_Object = MibTable
uemSensorTable = _UemSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17)
)
if mibBuilder.loadTexts:
    uemSensorTable.setStatus("mandatory")
_UemSensorTableEntry_Object = MibTableRow
uemSensorTableEntry = _UemSensorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1)
)
uemSensorTableEntry.setIndexNames(
    (0, "VISINET2-MIB", "uemSensorIndex"),
)
if mibBuilder.loadTexts:
    uemSensorTableEntry.setStatus("mandatory")
_UemSensorIndex_Type = Integer32
_UemSensorIndex_Object = MibTableColumn
uemSensorIndex = _UemSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 1),
    _UemSensorIndex_Type()
)
uemSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorIndex.setStatus("mandatory")
_UemSensorEnvMonIndex_Type = Integer32
_UemSensorEnvMonIndex_Object = MibTableColumn
uemSensorEnvMonIndex = _UemSensorEnvMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 2),
    _UemSensorEnvMonIndex_Type()
)
uemSensorEnvMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorEnvMonIndex.setStatus("mandatory")


class _UemSensorType_Type(Integer32):
    """Custom type uemSensorType based on Integer32"""
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
        *(("fan", 2),
          ("temperature", 4),
          ("unknown", 1),
          ("voltage", 3))
    )


_UemSensorType_Type.__name__ = "Integer32"
_UemSensorType_Object = MibTableColumn
uemSensorType = _UemSensorType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 3),
    _UemSensorType_Type()
)
uemSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorType.setStatus("mandatory")


class _UemSensorDescription_Type(DisplayString):
    """Custom type uemSensorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UemSensorDescription_Type.__name__ = "DisplayString"
_UemSensorDescription_Object = MibTableColumn
uemSensorDescription = _UemSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 4),
    _UemSensorDescription_Type()
)
uemSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorDescription.setStatus("mandatory")


class _UemSensorStatus_Type(Integer32):
    """Custom type uemSensorStatus based on Integer32"""
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
        *(("critical", 4),
          ("normal", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_UemSensorStatus_Type.__name__ = "Integer32"
_UemSensorStatus_Object = MibTableColumn
uemSensorStatus = _UemSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 5),
    _UemSensorStatus_Type()
)
uemSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorStatus.setStatus("mandatory")
_UemSensorValue_Type = Integer32
_UemSensorValue_Object = MibTableColumn
uemSensorValue = _UemSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 6),
    _UemSensorValue_Type()
)
uemSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorValue.setStatus("mandatory")
_UemSensorNominalValue_Type = Integer32
_UemSensorNominalValue_Object = MibTableColumn
uemSensorNominalValue = _UemSensorNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 7),
    _UemSensorNominalValue_Type()
)
uemSensorNominalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uemSensorNominalValue.setStatus("mandatory")
_UemSensorHighCriticalValue_Type = Integer32
_UemSensorHighCriticalValue_Object = MibTableColumn
uemSensorHighCriticalValue = _UemSensorHighCriticalValue_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 8),
    _UemSensorHighCriticalValue_Type()
)
uemSensorHighCriticalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uemSensorHighCriticalValue.setStatus("mandatory")


class _UemSensorHighCriticalLabel_Type(DisplayString):
    """Custom type uemSensorHighCriticalLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UemSensorHighCriticalLabel_Type.__name__ = "DisplayString"
_UemSensorHighCriticalLabel_Object = MibTableColumn
uemSensorHighCriticalLabel = _UemSensorHighCriticalLabel_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 9),
    _UemSensorHighCriticalLabel_Type()
)
uemSensorHighCriticalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorHighCriticalLabel.setStatus("mandatory")
_UemSensorHighWarningValue_Type = Integer32
_UemSensorHighWarningValue_Object = MibTableColumn
uemSensorHighWarningValue = _UemSensorHighWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 10),
    _UemSensorHighWarningValue_Type()
)
uemSensorHighWarningValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uemSensorHighWarningValue.setStatus("mandatory")


class _UemSensorHighWarningLabel_Type(DisplayString):
    """Custom type uemSensorHighWarningLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UemSensorHighWarningLabel_Type.__name__ = "DisplayString"
_UemSensorHighWarningLabel_Object = MibTableColumn
uemSensorHighWarningLabel = _UemSensorHighWarningLabel_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 11),
    _UemSensorHighWarningLabel_Type()
)
uemSensorHighWarningLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorHighWarningLabel.setStatus("mandatory")
_UemSensorLowWarningValue_Type = Integer32
_UemSensorLowWarningValue_Object = MibTableColumn
uemSensorLowWarningValue = _UemSensorLowWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 12),
    _UemSensorLowWarningValue_Type()
)
uemSensorLowWarningValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uemSensorLowWarningValue.setStatus("mandatory")


class _UemSensorLowWarningLabel_Type(DisplayString):
    """Custom type uemSensorLowWarningLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UemSensorLowWarningLabel_Type.__name__ = "DisplayString"
_UemSensorLowWarningLabel_Object = MibTableColumn
uemSensorLowWarningLabel = _UemSensorLowWarningLabel_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 13),
    _UemSensorLowWarningLabel_Type()
)
uemSensorLowWarningLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorLowWarningLabel.setStatus("mandatory")
_UemSensorLowCriticalValue_Type = Integer32
_UemSensorLowCriticalValue_Object = MibTableColumn
uemSensorLowCriticalValue = _UemSensorLowCriticalValue_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 14),
    _UemSensorLowCriticalValue_Type()
)
uemSensorLowCriticalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uemSensorLowCriticalValue.setStatus("mandatory")


class _UemSensorLowCriticalLabel_Type(DisplayString):
    """Custom type uemSensorLowCriticalLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UemSensorLowCriticalLabel_Type.__name__ = "DisplayString"
_UemSensorLowCriticalLabel_Object = MibTableColumn
uemSensorLowCriticalLabel = _UemSensorLowCriticalLabel_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 15),
    _UemSensorLowCriticalLabel_Type()
)
uemSensorLowCriticalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorLowCriticalLabel.setStatus("mandatory")


class _UemSensorEnabled_Type(Integer32):
    """Custom type uemSensorEnabled based on Integer32"""
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


_UemSensorEnabled_Type.__name__ = "Integer32"
_UemSensorEnabled_Object = MibTableColumn
uemSensorEnabled = _UemSensorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 17, 1, 16),
    _UemSensorEnabled_Type()
)
uemSensorEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSensorEnabled.setStatus("mandatory")
_UemSwitchTable_Object = MibTable
uemSwitchTable = _UemSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 18)
)
if mibBuilder.loadTexts:
    uemSwitchTable.setStatus("mandatory")
_UemSwitchTableEntry_Object = MibTableRow
uemSwitchTableEntry = _UemSwitchTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 18, 1)
)
uemSwitchTableEntry.setIndexNames(
    (0, "VISINET2-MIB", "uemSwitchIndex"),
)
if mibBuilder.loadTexts:
    uemSwitchTableEntry.setStatus("mandatory")
_UemSwitchIndex_Type = Integer32
_UemSwitchIndex_Object = MibTableColumn
uemSwitchIndex = _UemSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 18, 1, 1),
    _UemSwitchIndex_Type()
)
uemSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSwitchIndex.setStatus("mandatory")
_UemSwitchEnvMonIndex_Type = Integer32
_UemSwitchEnvMonIndex_Object = MibTableColumn
uemSwitchEnvMonIndex = _UemSwitchEnvMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 18, 1, 2),
    _UemSwitchEnvMonIndex_Type()
)
uemSwitchEnvMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSwitchEnvMonIndex.setStatus("mandatory")


class _UemSwitchDescription_Type(DisplayString):
    """Custom type uemSwitchDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UemSwitchDescription_Type.__name__ = "DisplayString"
_UemSwitchDescription_Object = MibTableColumn
uemSwitchDescription = _UemSwitchDescription_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 18, 1, 3),
    _UemSwitchDescription_Type()
)
uemSwitchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSwitchDescription.setStatus("mandatory")


class _UemSwitchContext_Type(DisplayString):
    """Custom type uemSwitchContext based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UemSwitchContext_Type.__name__ = "DisplayString"
_UemSwitchContext_Object = MibTableColumn
uemSwitchContext = _UemSwitchContext_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 18, 1, 4),
    _UemSwitchContext_Type()
)
uemSwitchContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSwitchContext.setStatus("mandatory")


class _UemSwitchCurrentState_Type(Integer32):
    """Custom type uemSwitchCurrentState based on Integer32"""
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


_UemSwitchCurrentState_Type.__name__ = "Integer32"
_UemSwitchCurrentState_Object = MibTableColumn
uemSwitchCurrentState = _UemSwitchCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 18, 1, 5),
    _UemSwitchCurrentState_Type()
)
uemSwitchCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSwitchCurrentState.setStatus("mandatory")


class _UemSwitchExpectedState_Type(Integer32):
    """Custom type uemSwitchExpectedState based on Integer32"""
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


_UemSwitchExpectedState_Type.__name__ = "Integer32"
_UemSwitchExpectedState_Object = MibTableColumn
uemSwitchExpectedState = _UemSwitchExpectedState_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 18, 1, 6),
    _UemSwitchExpectedState_Type()
)
uemSwitchExpectedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSwitchExpectedState.setStatus("mandatory")


class _UemSwitchEnabled_Type(Integer32):
    """Custom type uemSwitchEnabled based on Integer32"""
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


_UemSwitchEnabled_Type.__name__ = "Integer32"
_UemSwitchEnabled_Object = MibTableColumn
uemSwitchEnabled = _UemSwitchEnabled_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 18, 1, 7),
    _UemSwitchEnabled_Type()
)
uemSwitchEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uemSwitchEnabled.setStatus("mandatory")
_CfgAgent_ObjectIdentity = ObjectIdentity
cfgAgent = _CfgAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 7)
)
_CfgAgentVersion_Type = Integer32
_CfgAgentVersion_Object = MibScalar
cfgAgentVersion = _CfgAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 1),
    _CfgAgentVersion_Type()
)
cfgAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentVersion.setStatus("mandatory")
_CfgAgentRevision_Type = Integer32
_CfgAgentRevision_Object = MibScalar
cfgAgentRevision = _CfgAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 2),
    _CfgAgentRevision_Type()
)
cfgAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentRevision.setStatus("mandatory")
_CfgAgentMIBVersion_Type = Integer32
_CfgAgentMIBVersion_Object = MibScalar
cfgAgentMIBVersion = _CfgAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 3),
    _CfgAgentMIBVersion_Type()
)
cfgAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMIBVersion.setStatus("mandatory")
_CfgAgentMIBRevision_Type = Integer32
_CfgAgentMIBRevision_Object = MibScalar
cfgAgentMIBRevision = _CfgAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 4),
    _CfgAgentMIBRevision_Type()
)
cfgAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMIBRevision.setStatus("mandatory")
_CfgAgentBIOSVendor_Type = DisplayString
_CfgAgentBIOSVendor_Object = MibScalar
cfgAgentBIOSVendor = _CfgAgentBIOSVendor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 5),
    _CfgAgentBIOSVendor_Type()
)
cfgAgentBIOSVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSVendor.setStatus("mandatory")
_CfgAgentBIOSVersion_Type = DisplayString
_CfgAgentBIOSVersion_Object = MibScalar
cfgAgentBIOSVersion = _CfgAgentBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 6),
    _CfgAgentBIOSVersion_Type()
)
cfgAgentBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSVersion.setStatus("mandatory")
_CfgAgentBIOSDate_Type = DisplayString
_CfgAgentBIOSDate_Object = MibScalar
cfgAgentBIOSDate = _CfgAgentBIOSDate_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 7),
    _CfgAgentBIOSDate_Type()
)
cfgAgentBIOSDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSDate.setStatus("mandatory")
_CfgAgentBIOSsROMInKb_Type = Integer32
_CfgAgentBIOSsROMInKb_Object = MibScalar
cfgAgentBIOSsROMInKb = _CfgAgentBIOSsROMInKb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 8),
    _CfgAgentBIOSsROMInKb_Type()
)
cfgAgentBIOSsROMInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSsROMInKb.setStatus("mandatory")
_CfgAgentBIOSBusSupport_Type = DisplayString
_CfgAgentBIOSBusSupport_Object = MibScalar
cfgAgentBIOSBusSupport = _CfgAgentBIOSBusSupport_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 9),
    _CfgAgentBIOSBusSupport_Type()
)
cfgAgentBIOSBusSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSBusSupport.setStatus("mandatory")
_CfgAgentBIOSAddress_Type = Integer32
_CfgAgentBIOSAddress_Object = MibScalar
cfgAgentBIOSAddress = _CfgAgentBIOSAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 10),
    _CfgAgentBIOSAddress_Type()
)
cfgAgentBIOSAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSAddress.setStatus("mandatory")
_CfgAgentBIOSInterruptId_Type = Integer32
_CfgAgentBIOSInterruptId_Object = MibScalar
cfgAgentBIOSInterruptId = _CfgAgentBIOSInterruptId_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 11),
    _CfgAgentBIOSInterruptId_Type()
)
cfgAgentBIOSInterruptId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentBIOSInterruptId.setStatus("mandatory")
_CfgAgentnCPUs_Type = Integer32
_CfgAgentnCPUs_Object = MibScalar
cfgAgentnCPUs = _CfgAgentnCPUs_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 12),
    _CfgAgentnCPUs_Type()
)
cfgAgentnCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnCPUs.setStatus("mandatory")
_CfgAgentCPUsTbl_Object = MibTable
cfgAgentCPUsTbl = _CfgAgentCPUsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13)
)
if mibBuilder.loadTexts:
    cfgAgentCPUsTbl.setStatus("mandatory")
_CfgAgentCPUsTblEntry_Object = MibTableRow
cfgAgentCPUsTblEntry = _CfgAgentCPUsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1)
)
if mibBuilder.loadTexts:
    cfgAgentCPUsTblEntry.setStatus("mandatory")
_CfgAgentCPUClass_Type = DisplayString
_CfgAgentCPUClass_Object = MibTableColumn
cfgAgentCPUClass = _CfgAgentCPUClass_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 1),
    _CfgAgentCPUClass_Type()
)
cfgAgentCPUClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUClass.setStatus("mandatory")
_CfgAgentCPUName_Type = DisplayString
_CfgAgentCPUName_Object = MibTableColumn
cfgAgentCPUName = _CfgAgentCPUName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 2),
    _CfgAgentCPUName_Type()
)
cfgAgentCPUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUName.setStatus("mandatory")
_CfgAgentCPUVendor_Type = DisplayString
_CfgAgentCPUVendor_Object = MibTableColumn
cfgAgentCPUVendor = _CfgAgentCPUVendor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 3),
    _CfgAgentCPUVendor_Type()
)
cfgAgentCPUVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUVendor.setStatus("mandatory")
_CfgAgentCPUSpeed_Type = Integer32
_CfgAgentCPUSpeed_Object = MibTableColumn
cfgAgentCPUSpeed = _CfgAgentCPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 4),
    _CfgAgentCPUSpeed_Type()
)
cfgAgentCPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUSpeed.setStatus("mandatory")
_CfgAgentCPUsCacheInKb_Type = Integer32
_CfgAgentCPUsCacheInKb_Object = MibTableColumn
cfgAgentCPUsCacheInKb = _CfgAgentCPUsCacheInKb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 5),
    _CfgAgentCPUsCacheInKb_Type()
)
cfgAgentCPUsCacheInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUsCacheInKb.setStatus("mandatory")


class _CfgAgentCPUState_Type(Integer32):
    """Custom type cfgAgentCPUState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disabled", 2))
    )


_CfgAgentCPUState_Type.__name__ = "Integer32"
_CfgAgentCPUState_Object = MibTableColumn
cfgAgentCPUState = _CfgAgentCPUState_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 13, 1, 6),
    _CfgAgentCPUState_Type()
)
cfgAgentCPUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentCPUState.setStatus("mandatory")
_CfgAgentSysName_Type = DisplayString
_CfgAgentSysName_Object = MibScalar
cfgAgentSysName = _CfgAgentSysName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 14),
    _CfgAgentSysName_Type()
)
cfgAgentSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSysName.setStatus("mandatory")
_CfgAgentSysBoardVersion_Type = DisplayString
_CfgAgentSysBoardVersion_Object = MibScalar
cfgAgentSysBoardVersion = _CfgAgentSysBoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 15),
    _CfgAgentSysBoardVersion_Type()
)
cfgAgentSysBoardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSysBoardVersion.setStatus("mandatory")
_CfgAgentSysUptimeMilSec_Type = Integer32
_CfgAgentSysUptimeMilSec_Object = MibScalar
cfgAgentSysUptimeMilSec = _CfgAgentSysUptimeMilSec_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 16),
    _CfgAgentSysUptimeMilSec_Type()
)
cfgAgentSysUptimeMilSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSysUptimeMilSec.setStatus("mandatory")
_CfgAgentSysOS_Type = DisplayString
_CfgAgentSysOS_Object = MibScalar
cfgAgentSysOS = _CfgAgentSysOS_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 17),
    _CfgAgentSysOS_Type()
)
cfgAgentSysOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSysOS.setStatus("mandatory")
_CfgAgentSysnDMAs_Type = Integer32
_CfgAgentSysnDMAs_Object = MibScalar
cfgAgentSysnDMAs = _CfgAgentSysnDMAs_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 18),
    _CfgAgentSysnDMAs_Type()
)
cfgAgentSysnDMAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSysnDMAs.setStatus("mandatory")
_CfgAgentnIRQs_Type = Integer32
_CfgAgentnIRQs_Object = MibScalar
cfgAgentnIRQs = _CfgAgentnIRQs_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 19),
    _CfgAgentnIRQs_Type()
)
cfgAgentnIRQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnIRQs.setStatus("mandatory")
_CfgAgentIRQsTbl_Object = MibTable
cfgAgentIRQsTbl = _CfgAgentIRQsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20)
)
if mibBuilder.loadTexts:
    cfgAgentIRQsTbl.setStatus("mandatory")
_CfgAgentIRQsTblEntry_Object = MibTableRow
cfgAgentIRQsTblEntry = _CfgAgentIRQsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20, 1)
)
if mibBuilder.loadTexts:
    cfgAgentIRQsTblEntry.setStatus("mandatory")
_CfgAgentIRQ_Type = Integer32
_CfgAgentIRQ_Object = MibTableColumn
cfgAgentIRQ = _CfgAgentIRQ_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20, 1, 1),
    _CfgAgentIRQ_Type()
)
cfgAgentIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIRQ.setStatus("mandatory")
_CfgAgentIRQOwner_Type = DisplayString
_CfgAgentIRQOwner_Object = MibTableColumn
cfgAgentIRQOwner = _CfgAgentIRQOwner_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20, 1, 2),
    _CfgAgentIRQOwner_Type()
)
cfgAgentIRQOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIRQOwner.setStatus("mandatory")
_CfgAgentIRQBus_Type = DisplayString
_CfgAgentIRQBus_Object = MibTableColumn
cfgAgentIRQBus = _CfgAgentIRQBus_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20, 1, 3),
    _CfgAgentIRQBus_Type()
)
cfgAgentIRQBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIRQBus.setStatus("mandatory")
_CfgAgentIRQClass_Type = DisplayString
_CfgAgentIRQClass_Object = MibTableColumn
cfgAgentIRQClass = _CfgAgentIRQClass_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 20, 1, 4),
    _CfgAgentIRQClass_Type()
)
cfgAgentIRQClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIRQClass.setStatus("mandatory")
_CfgAgentMemSizeInMb_Type = Integer32
_CfgAgentMemSizeInMb_Object = MibScalar
cfgAgentMemSizeInMb = _CfgAgentMemSizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 21),
    _CfgAgentMemSizeInMb_Type()
)
cfgAgentMemSizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemSizeInMb.setStatus("mandatory")
_CfgAgentMemType_Type = DisplayString
_CfgAgentMemType_Object = MibScalar
cfgAgentMemType = _CfgAgentMemType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 22),
    _CfgAgentMemType_Type()
)
cfgAgentMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemType.setStatus("mandatory")
_CfgAgentMemSpeed_Type = Integer32
_CfgAgentMemSpeed_Object = MibScalar
cfgAgentMemSpeed = _CfgAgentMemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 23),
    _CfgAgentMemSpeed_Type()
)
cfgAgentMemSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemSpeed.setStatus("mandatory")
_CfgAgentMemCacheInKb_Type = Integer32
_CfgAgentMemCacheInKb_Object = MibScalar
cfgAgentMemCacheInKb = _CfgAgentMemCacheInKb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 24),
    _CfgAgentMemCacheInKb_Type()
)
cfgAgentMemCacheInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemCacheInKb.setStatus("mandatory")
_CfgAgentMemBanks_Type = Integer32
_CfgAgentMemBanks_Object = MibScalar
cfgAgentMemBanks = _CfgAgentMemBanks_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 25),
    _CfgAgentMemBanks_Type()
)
cfgAgentMemBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemBanks.setStatus("mandatory")
_CfgAgentMemSpeedSupported_Type = Integer32
_CfgAgentMemSpeedSupported_Object = MibScalar
cfgAgentMemSpeedSupported = _CfgAgentMemSpeedSupported_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 26),
    _CfgAgentMemSpeedSupported_Type()
)
cfgAgentMemSpeedSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentMemSpeedSupported.setStatus("mandatory")
_CfgAgentIOKbdType_Type = DisplayString
_CfgAgentIOKbdType_Object = MibScalar
cfgAgentIOKbdType = _CfgAgentIOKbdType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 27),
    _CfgAgentIOKbdType_Type()
)
cfgAgentIOKbdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIOKbdType.setStatus("mandatory")
_CfgAgentIOMouseType_Type = DisplayString
_CfgAgentIOMouseType_Object = MibScalar
cfgAgentIOMouseType = _CfgAgentIOMouseType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 28),
    _CfgAgentIOMouseType_Type()
)
cfgAgentIOMouseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIOMouseType.setStatus("mandatory")
_CfgAgentIOVidType_Type = DisplayString
_CfgAgentIOVidType_Object = MibScalar
cfgAgentIOVidType = _CfgAgentIOVidType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 29),
    _CfgAgentIOVidType_Type()
)
cfgAgentIOVidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentIOVidType.setStatus("mandatory")
_CfgAgentnSerials_Type = Integer32
_CfgAgentnSerials_Object = MibScalar
cfgAgentnSerials = _CfgAgentnSerials_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 30),
    _CfgAgentnSerials_Type()
)
cfgAgentnSerials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnSerials.setStatus("mandatory")
_CfgAgentSerialsTbl_Object = MibTable
cfgAgentSerialsTbl = _CfgAgentSerialsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 31)
)
if mibBuilder.loadTexts:
    cfgAgentSerialsTbl.setStatus("mandatory")
_CfgAgentSerialsTblEntry_Object = MibTableRow
cfgAgentSerialsTblEntry = _CfgAgentSerialsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 31, 1)
)
if mibBuilder.loadTexts:
    cfgAgentSerialsTblEntry.setStatus("mandatory")
_CfgAgentSerialPort_Type = Integer32
_CfgAgentSerialPort_Object = MibTableColumn
cfgAgentSerialPort = _CfgAgentSerialPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 31, 1, 1),
    _CfgAgentSerialPort_Type()
)
cfgAgentSerialPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentSerialPort.setStatus("mandatory")
_CfgAgentnParallels_Type = Integer32
_CfgAgentnParallels_Object = MibScalar
cfgAgentnParallels = _CfgAgentnParallels_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 32),
    _CfgAgentnParallels_Type()
)
cfgAgentnParallels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnParallels.setStatus("mandatory")
_CfgAgentParallelsTbl_Object = MibTable
cfgAgentParallelsTbl = _CfgAgentParallelsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 33)
)
if mibBuilder.loadTexts:
    cfgAgentParallelsTbl.setStatus("mandatory")
_CfgAgentParallelsTblEntry_Object = MibTableRow
cfgAgentParallelsTblEntry = _CfgAgentParallelsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 33, 1)
)
if mibBuilder.loadTexts:
    cfgAgentParallelsTblEntry.setStatus("mandatory")
_CfgAgentParallelPort_Type = Integer32
_CfgAgentParallelPort_Object = MibTableColumn
cfgAgentParallelPort = _CfgAgentParallelPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 33, 1, 1),
    _CfgAgentParallelPort_Type()
)
cfgAgentParallelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentParallelPort.setStatus("mandatory")
_CfgAgentnControllers_Type = Integer32
_CfgAgentnControllers_Object = MibScalar
cfgAgentnControllers = _CfgAgentnControllers_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 34),
    _CfgAgentnControllers_Type()
)
cfgAgentnControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnControllers.setStatus("mandatory")
_CfgAgentControllersTbl_Object = MibTable
cfgAgentControllersTbl = _CfgAgentControllersTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 35)
)
if mibBuilder.loadTexts:
    cfgAgentControllersTbl.setStatus("mandatory")
_CfgAgentControllersTblEntry_Object = MibTableRow
cfgAgentControllersTblEntry = _CfgAgentControllersTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 35, 1)
)
if mibBuilder.loadTexts:
    cfgAgentControllersTblEntry.setStatus("mandatory")
_CfgAgentControllerType_Type = DisplayString
_CfgAgentControllerType_Object = MibTableColumn
cfgAgentControllerType = _CfgAgentControllerType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 35, 1, 1),
    _CfgAgentControllerType_Type()
)
cfgAgentControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentControllerType.setStatus("mandatory")
_CfgAgentControllerName_Type = DisplayString
_CfgAgentControllerName_Object = MibTableColumn
cfgAgentControllerName = _CfgAgentControllerName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 35, 1, 2),
    _CfgAgentControllerName_Type()
)
cfgAgentControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentControllerName.setStatus("mandatory")
_CfgAgentControllerIRQ_Type = Integer32
_CfgAgentControllerIRQ_Object = MibTableColumn
cfgAgentControllerIRQ = _CfgAgentControllerIRQ_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 35, 1, 3),
    _CfgAgentControllerIRQ_Type()
)
cfgAgentControllerIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentControllerIRQ.setStatus("mandatory")
_CfgAgentnTrapDests_Type = Integer32
_CfgAgentnTrapDests_Object = MibScalar
cfgAgentnTrapDests = _CfgAgentnTrapDests_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 36),
    _CfgAgentnTrapDests_Type()
)
cfgAgentnTrapDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentnTrapDests.setStatus("mandatory")
_CfgAgentTrapDestsTbl_Object = MibTable
cfgAgentTrapDestsTbl = _CfgAgentTrapDestsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 37)
)
if mibBuilder.loadTexts:
    cfgAgentTrapDestsTbl.setStatus("mandatory")
_CfgAgentTrapDestsTblEntry_Object = MibTableRow
cfgAgentTrapDestsTblEntry = _CfgAgentTrapDestsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 37, 1)
)
if mibBuilder.loadTexts:
    cfgAgentTrapDestsTblEntry.setStatus("mandatory")
_CfgAgentTrapDestId_Type = DisplayString
_CfgAgentTrapDestId_Object = MibTableColumn
cfgAgentTrapDestId = _CfgAgentTrapDestId_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 37, 1, 1),
    _CfgAgentTrapDestId_Type()
)
cfgAgentTrapDestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgAgentTrapDestId.setStatus("mandatory")
_CfgAgentTrapDestIPAddr_Type = DisplayString
_CfgAgentTrapDestIPAddr_Object = MibTableColumn
cfgAgentTrapDestIPAddr = _CfgAgentTrapDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 7, 37, 1, 2),
    _CfgAgentTrapDestIPAddr_Type()
)
cfgAgentTrapDestIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAgentTrapDestIPAddr.setStatus("mandatory")
_NetAgent_ObjectIdentity = ObjectIdentity
netAgent = _NetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 8)
)
_NetAgentVersion_Type = Integer32
_NetAgentVersion_Object = MibScalar
netAgentVersion = _NetAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 1),
    _NetAgentVersion_Type()
)
netAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentVersion.setStatus("mandatory")
_NetAgentRevision_Type = Integer32
_NetAgentRevision_Object = MibScalar
netAgentRevision = _NetAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 2),
    _NetAgentRevision_Type()
)
netAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentRevision.setStatus("mandatory")
_NetAgentMIBVersion_Type = Integer32
_NetAgentMIBVersion_Object = MibScalar
netAgentMIBVersion = _NetAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 3),
    _NetAgentMIBVersion_Type()
)
netAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentMIBVersion.setStatus("mandatory")
_NetAgentMIBRevision_Type = Integer32
_NetAgentMIBRevision_Object = MibScalar
netAgentMIBRevision = _NetAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 4),
    _NetAgentMIBRevision_Type()
)
netAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentMIBRevision.setStatus("mandatory")
_NetAgentMachineName_Type = DisplayString
_NetAgentMachineName_Object = MibScalar
netAgentMachineName = _NetAgentMachineName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 5),
    _NetAgentMachineName_Type()
)
netAgentMachineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentMachineName.setStatus("mandatory")
_NetAgentLogonServer_Type = DisplayString
_NetAgentLogonServer_Object = MibScalar
netAgentLogonServer = _NetAgentLogonServer_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 6),
    _NetAgentLogonServer_Type()
)
netAgentLogonServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentLogonServer.setStatus("mandatory")
_NetAgentnNICs_Type = Integer32
_NetAgentnNICs_Object = MibScalar
netAgentnNICs = _NetAgentnNICs_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 7),
    _NetAgentnNICs_Type()
)
netAgentnNICs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentnNICs.setStatus("mandatory")
_NetAgentNICsTbl_Object = MibTable
netAgentNICsTbl = _NetAgentNICsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8)
)
if mibBuilder.loadTexts:
    netAgentNICsTbl.setStatus("mandatory")
_NetAgentNICTblEntry_Object = MibTableRow
netAgentNICTblEntry = _NetAgentNICTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1)
)
if mibBuilder.loadTexts:
    netAgentNICTblEntry.setStatus("mandatory")
_NetAgentVendorID_Type = DisplayString
_NetAgentVendorID_Object = MibTableColumn
netAgentVendorID = _NetAgentVendorID_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 1),
    _NetAgentVendorID_Type()
)
netAgentVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentVendorID.setStatus("mandatory")
_NetAgentMACAddress_Type = DisplayString
_NetAgentMACAddress_Object = MibTableColumn
netAgentMACAddress = _NetAgentMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 2),
    _NetAgentMACAddress_Type()
)
netAgentMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentMACAddress.setStatus("mandatory")
_NetAgentFirmwareVersion_Type = Integer32
_NetAgentFirmwareVersion_Object = MibTableColumn
netAgentFirmwareVersion = _NetAgentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 3),
    _NetAgentFirmwareVersion_Type()
)
netAgentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentFirmwareVersion.setStatus("mandatory")
_NetAgentFirmwareRevision_Type = Integer32
_NetAgentFirmwareRevision_Object = MibTableColumn
netAgentFirmwareRevision = _NetAgentFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 4),
    _NetAgentFirmwareRevision_Type()
)
netAgentFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentFirmwareRevision.setStatus("mandatory")
_NetAgentControllerType_Type = DisplayString
_NetAgentControllerType_Object = MibTableColumn
netAgentControllerType = _NetAgentControllerType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 5),
    _NetAgentControllerType_Type()
)
netAgentControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentControllerType.setStatus("mandatory")
_NetAgentControllerPort_Type = Integer32
_NetAgentControllerPort_Object = MibTableColumn
netAgentControllerPort = _NetAgentControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 6),
    _NetAgentControllerPort_Type()
)
netAgentControllerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentControllerPort.setStatus("mandatory")
_NetAgentControllerIRQ_Type = Integer32
_NetAgentControllerIRQ_Object = MibTableColumn
netAgentControllerIRQ = _NetAgentControllerIRQ_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 7),
    _NetAgentControllerIRQ_Type()
)
netAgentControllerIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentControllerIRQ.setStatus("mandatory")
_NetAgentControllerBaseIO_Type = Integer32
_NetAgentControllerBaseIO_Object = MibTableColumn
netAgentControllerBaseIO = _NetAgentControllerBaseIO_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 8),
    _NetAgentControllerBaseIO_Type()
)
netAgentControllerBaseIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentControllerBaseIO.setStatus("mandatory")
_NetAgentDataSent_Type = Integer32
_NetAgentDataSent_Object = MibTableColumn
netAgentDataSent = _NetAgentDataSent_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 9),
    _NetAgentDataSent_Type()
)
netAgentDataSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentDataSent.setStatus("mandatory")
_NetAgentDataReceived_Type = Integer32
_NetAgentDataReceived_Object = MibTableColumn
netAgentDataReceived = _NetAgentDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 10),
    _NetAgentDataReceived_Type()
)
netAgentDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentDataReceived.setStatus("mandatory")
_NetAgentNICDriver_Type = DisplayString
_NetAgentNICDriver_Object = MibTableColumn
netAgentNICDriver = _NetAgentNICDriver_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 11),
    _NetAgentNICDriver_Type()
)
netAgentNICDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentNICDriver.setStatus("mandatory")
_NetAgentDriverName_Type = DisplayString
_NetAgentDriverName_Object = MibTableColumn
netAgentDriverName = _NetAgentDriverName_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 8, 8, 1, 12),
    _NetAgentDriverName_Type()
)
netAgentDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netAgentDriverName.setStatus("mandatory")
_SftAgent_ObjectIdentity = ObjectIdentity
sftAgent = _SftAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 9)
)
_SftAgentVersion_Type = Integer32
_SftAgentVersion_Object = MibScalar
sftAgentVersion = _SftAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 1),
    _SftAgentVersion_Type()
)
sftAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentVersion.setStatus("mandatory")
_SftAgentRevision_Type = Integer32
_SftAgentRevision_Object = MibScalar
sftAgentRevision = _SftAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 2),
    _SftAgentRevision_Type()
)
sftAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentRevision.setStatus("mandatory")
_SftAgentMIBVersion_Type = Integer32
_SftAgentMIBVersion_Object = MibScalar
sftAgentMIBVersion = _SftAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 3),
    _SftAgentMIBVersion_Type()
)
sftAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentMIBVersion.setStatus("mandatory")
_SftAgentMIBRevision_Type = Integer32
_SftAgentMIBRevision_Object = MibScalar
sftAgentMIBRevision = _SftAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 4),
    _SftAgentMIBRevision_Type()
)
sftAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentMIBRevision.setStatus("mandatory")
_SftAgentnPackages_Type = Integer32
_SftAgentnPackages_Object = MibScalar
sftAgentnPackages = _SftAgentnPackages_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 5),
    _SftAgentnPackages_Type()
)
sftAgentnPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentnPackages.setStatus("mandatory")
_SftAgentPackagesTbl_Object = MibTable
sftAgentPackagesTbl = _SftAgentPackagesTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 6)
)
if mibBuilder.loadTexts:
    sftAgentPackagesTbl.setStatus("mandatory")
_SftAgentPackagesTblEntry_Object = MibTableRow
sftAgentPackagesTblEntry = _SftAgentPackagesTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 6, 1)
)
if mibBuilder.loadTexts:
    sftAgentPackagesTblEntry.setStatus("mandatory")
_SftAgentPackage_Type = DisplayString
_SftAgentPackage_Object = MibTableColumn
sftAgentPackage = _SftAgentPackage_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 6, 1, 1),
    _SftAgentPackage_Type()
)
sftAgentPackage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentPackage.setStatus("mandatory")
_SftAgentnServices_Type = Integer32
_SftAgentnServices_Object = MibScalar
sftAgentnServices = _SftAgentnServices_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 7),
    _SftAgentnServices_Type()
)
sftAgentnServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentnServices.setStatus("mandatory")
_SftAgentServicesTbl_Object = MibTable
sftAgentServicesTbl = _SftAgentServicesTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 8)
)
if mibBuilder.loadTexts:
    sftAgentServicesTbl.setStatus("mandatory")
_SftAgentServicesTblEntry_Object = MibTableRow
sftAgentServicesTblEntry = _SftAgentServicesTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 8, 1)
)
if mibBuilder.loadTexts:
    sftAgentServicesTblEntry.setStatus("mandatory")
_SftAgentService_Type = DisplayString
_SftAgentService_Object = MibTableColumn
sftAgentService = _SftAgentService_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 8, 1, 1),
    _SftAgentService_Type()
)
sftAgentService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentService.setStatus("mandatory")


class _SftAgentServiceStartup_Type(Integer32):
    """Custom type sftAgentServiceStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("boot", 0),
          ("disabled", 4),
          ("manual", 3),
          ("system", 1))
    )


_SftAgentServiceStartup_Type.__name__ = "Integer32"
_SftAgentServiceStartup_Object = MibTableColumn
sftAgentServiceStartup = _SftAgentServiceStartup_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 8, 1, 2),
    _SftAgentServiceStartup_Type()
)
sftAgentServiceStartup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentServiceStartup.setStatus("mandatory")
_SftAgentnDevices_Type = Integer32
_SftAgentnDevices_Object = MibScalar
sftAgentnDevices = _SftAgentnDevices_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 9),
    _SftAgentnDevices_Type()
)
sftAgentnDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentnDevices.setStatus("mandatory")
_SftAgentDevicesTbl_Object = MibTable
sftAgentDevicesTbl = _SftAgentDevicesTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 10)
)
if mibBuilder.loadTexts:
    sftAgentDevicesTbl.setStatus("mandatory")
_SftAgentDevicesTblEntry_Object = MibTableRow
sftAgentDevicesTblEntry = _SftAgentDevicesTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 10, 1)
)
if mibBuilder.loadTexts:
    sftAgentDevicesTblEntry.setStatus("mandatory")
_SftAgentDevice_Type = DisplayString
_SftAgentDevice_Object = MibTableColumn
sftAgentDevice = _SftAgentDevice_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 10, 1, 1),
    _SftAgentDevice_Type()
)
sftAgentDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentDevice.setStatus("mandatory")


class _SftAgentDeviceStartup_Type(Integer32):
    """Custom type sftAgentDeviceStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("boot", 0),
          ("disabled", 4),
          ("manual", 3),
          ("system", 1))
    )


_SftAgentDeviceStartup_Type.__name__ = "Integer32"
_SftAgentDeviceStartup_Object = MibTableColumn
sftAgentDeviceStartup = _SftAgentDeviceStartup_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 9, 10, 1, 2),
    _SftAgentDeviceStartup_Type()
)
sftAgentDeviceStartup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sftAgentDeviceStartup.setStatus("mandatory")
_StrAgent_ObjectIdentity = ObjectIdentity
strAgent = _StrAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 10)
)
_StrAgentVersion_Type = Integer32
_StrAgentVersion_Object = MibScalar
strAgentVersion = _StrAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 1),
    _StrAgentVersion_Type()
)
strAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVersion.setStatus("mandatory")
_StrAgentRevision_Type = Integer32
_StrAgentRevision_Object = MibScalar
strAgentRevision = _StrAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 2),
    _StrAgentRevision_Type()
)
strAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentRevision.setStatus("mandatory")
_StrAgentMIBVersion_Type = Integer32
_StrAgentMIBVersion_Object = MibScalar
strAgentMIBVersion = _StrAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 3),
    _StrAgentMIBVersion_Type()
)
strAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentMIBVersion.setStatus("mandatory")
_StrAgentMIBRevision_Type = Integer32
_StrAgentMIBRevision_Object = MibScalar
strAgentMIBRevision = _StrAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 4),
    _StrAgentMIBRevision_Type()
)
strAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentMIBRevision.setStatus("mandatory")
_StrAgentnControllers_Type = Integer32
_StrAgentnControllers_Object = MibScalar
strAgentnControllers = _StrAgentnControllers_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 5),
    _StrAgentnControllers_Type()
)
strAgentnControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentnControllers.setStatus("mandatory")
_StrAgentControllersTbl_Object = MibTable
strAgentControllersTbl = _StrAgentControllersTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6)
)
if mibBuilder.loadTexts:
    strAgentControllersTbl.setStatus("mandatory")
_StrAgentControllersTblEntry_Object = MibTableRow
strAgentControllersTblEntry = _StrAgentControllersTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1)
)
if mibBuilder.loadTexts:
    strAgentControllersTblEntry.setStatus("mandatory")
_StrAgentCtlrType_Type = DisplayString
_StrAgentCtlrType_Object = MibTableColumn
strAgentCtlrType = _StrAgentCtlrType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 1),
    _StrAgentCtlrType_Type()
)
strAgentCtlrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrType.setStatus("mandatory")
_StrAgentCtlrVendor_Type = DisplayString
_StrAgentCtlrVendor_Object = MibTableColumn
strAgentCtlrVendor = _StrAgentCtlrVendor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 2),
    _StrAgentCtlrVendor_Type()
)
strAgentCtlrVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrVendor.setStatus("mandatory")
_StrAgentCtlrFirmware_Type = DisplayString
_StrAgentCtlrFirmware_Object = MibTableColumn
strAgentCtlrFirmware = _StrAgentCtlrFirmware_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 3),
    _StrAgentCtlrFirmware_Type()
)
strAgentCtlrFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrFirmware.setStatus("mandatory")
_StrAgentCtlrSerialNo_Type = DisplayString
_StrAgentCtlrSerialNo_Object = MibTableColumn
strAgentCtlrSerialNo = _StrAgentCtlrSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 4),
    _StrAgentCtlrSerialNo_Type()
)
strAgentCtlrSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrSerialNo.setStatus("mandatory")
_StrAgentCtlrDMA_Type = Integer32
_StrAgentCtlrDMA_Object = MibTableColumn
strAgentCtlrDMA = _StrAgentCtlrDMA_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 5),
    _StrAgentCtlrDMA_Type()
)
strAgentCtlrDMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrDMA.setStatus("mandatory")
_StrAgentCtlrIRQ_Type = Integer32
_StrAgentCtlrIRQ_Object = MibTableColumn
strAgentCtlrIRQ = _StrAgentCtlrIRQ_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 6),
    _StrAgentCtlrIRQ_Type()
)
strAgentCtlrIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrIRQ.setStatus("mandatory")
_StrAgentCtlrAddress_Type = Integer32
_StrAgentCtlrAddress_Object = MibTableColumn
strAgentCtlrAddress = _StrAgentCtlrAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 7),
    _StrAgentCtlrAddress_Type()
)
strAgentCtlrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrAddress.setStatus("mandatory")
_StrAgentCtlrIOPort_Type = Integer32
_StrAgentCtlrIOPort_Object = MibTableColumn
strAgentCtlrIOPort = _StrAgentCtlrIOPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 6, 1, 8),
    _StrAgentCtlrIOPort_Type()
)
strAgentCtlrIOPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentCtlrIOPort.setStatus("mandatory")
_StrAgentnDisks_Type = Integer32
_StrAgentnDisks_Object = MibScalar
strAgentnDisks = _StrAgentnDisks_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 7),
    _StrAgentnDisks_Type()
)
strAgentnDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentnDisks.setStatus("mandatory")
_StrAgentDisksTbl_Object = MibTable
strAgentDisksTbl = _StrAgentDisksTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8)
)
if mibBuilder.loadTexts:
    strAgentDisksTbl.setStatus("mandatory")
_StrAgentDisksTblEntry_Object = MibTableRow
strAgentDisksTblEntry = _StrAgentDisksTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1)
)
if mibBuilder.loadTexts:
    strAgentDisksTblEntry.setStatus("mandatory")
_StrAgentDiskVendor_Type = DisplayString
_StrAgentDiskVendor_Object = MibTableColumn
strAgentDiskVendor = _StrAgentDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 1),
    _StrAgentDiskVendor_Type()
)
strAgentDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskVendor.setStatus("mandatory")
_StrAgentDiskDescription_Type = DisplayString
_StrAgentDiskDescription_Object = MibTableColumn
strAgentDiskDescription = _StrAgentDiskDescription_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 2),
    _StrAgentDiskDescription_Type()
)
strAgentDiskDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskDescription.setStatus("mandatory")
_StrAgentDiskFirmware_Type = DisplayString
_StrAgentDiskFirmware_Object = MibTableColumn
strAgentDiskFirmware = _StrAgentDiskFirmware_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 3),
    _StrAgentDiskFirmware_Type()
)
strAgentDiskFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskFirmware.setStatus("mandatory")
_StrAgentDiskPort_Type = Integer32
_StrAgentDiskPort_Object = MibTableColumn
strAgentDiskPort = _StrAgentDiskPort_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 4),
    _StrAgentDiskPort_Type()
)
strAgentDiskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskPort.setStatus("mandatory")
_StrAgentDiskBus_Type = Integer32
_StrAgentDiskBus_Object = MibTableColumn
strAgentDiskBus = _StrAgentDiskBus_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 5),
    _StrAgentDiskBus_Type()
)
strAgentDiskBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskBus.setStatus("mandatory")
_StrAgentDiskLUN_Type = Integer32
_StrAgentDiskLUN_Object = MibTableColumn
strAgentDiskLUN = _StrAgentDiskLUN_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 6),
    _StrAgentDiskLUN_Type()
)
strAgentDiskLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskLUN.setStatus("mandatory")
_StrAgentDiskID_Type = Integer32
_StrAgentDiskID_Object = MibTableColumn
strAgentDiskID = _StrAgentDiskID_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 7),
    _StrAgentDiskID_Type()
)
strAgentDiskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskID.setStatus("mandatory")
_StrAgentDiskSerialNo_Type = DisplayString
_StrAgentDiskSerialNo_Object = MibTableColumn
strAgentDiskSerialNo = _StrAgentDiskSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 8),
    _StrAgentDiskSerialNo_Type()
)
strAgentDiskSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskSerialNo.setStatus("mandatory")
_StrAgentDisknSectors_Type = Integer32
_StrAgentDisknSectors_Object = MibTableColumn
strAgentDisknSectors = _StrAgentDisknSectors_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 9),
    _StrAgentDisknSectors_Type()
)
strAgentDisknSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDisknSectors.setStatus("mandatory")
_StrAgentDiskDriveLetters_Type = DisplayString
_StrAgentDiskDriveLetters_Object = MibTableColumn
strAgentDiskDriveLetters = _StrAgentDiskDriveLetters_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 10),
    _StrAgentDiskDriveLetters_Type()
)
strAgentDiskDriveLetters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskDriveLetters.setStatus("mandatory")
_StrAgentDiskSizeInMb_Type = Integer32
_StrAgentDiskSizeInMb_Object = MibTableColumn
strAgentDiskSizeInMb = _StrAgentDiskSizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 11),
    _StrAgentDiskSizeInMb_Type()
)
strAgentDiskSizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskSizeInMb.setStatus("mandatory")


class _StrAgentDiskState_Type(Integer32):
    """Custom type strAgentDiskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessable", 1),
          ("offline", 2))
    )


_StrAgentDiskState_Type.__name__ = "Integer32"
_StrAgentDiskState_Object = MibTableColumn
strAgentDiskState = _StrAgentDiskState_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 12),
    _StrAgentDiskState_Type()
)
strAgentDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskState.setStatus("mandatory")
_StrAgentDiskXfersPerSec_Type = Integer32
_StrAgentDiskXfersPerSec_Object = MibTableColumn
strAgentDiskXfersPerSec = _StrAgentDiskXfersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 13),
    _StrAgentDiskXfersPerSec_Type()
)
strAgentDiskXfersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskXfersPerSec.setStatus("mandatory")


class _StrAgentDiskSmartCond_Type(Integer32):
    """Custom type strAgentDiskSmartCond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 2),
          ("safe", 1),
          ("unknown", 0))
    )


_StrAgentDiskSmartCond_Type.__name__ = "Integer32"
_StrAgentDiskSmartCond_Object = MibTableColumn
strAgentDiskSmartCond = _StrAgentDiskSmartCond_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 8, 1, 14),
    _StrAgentDiskSmartCond_Type()
)
strAgentDiskSmartCond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentDiskSmartCond.setStatus("mandatory")
_StrAgentnFloppies_Type = Integer32
_StrAgentnFloppies_Object = MibScalar
strAgentnFloppies = _StrAgentnFloppies_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 9),
    _StrAgentnFloppies_Type()
)
strAgentnFloppies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentnFloppies.setStatus("mandatory")
_StrAgentFloppyTbl_Object = MibTable
strAgentFloppyTbl = _StrAgentFloppyTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10)
)
if mibBuilder.loadTexts:
    strAgentFloppyTbl.setStatus("mandatory")
_StrAgentFloppyTblEntry_Object = MibTableRow
strAgentFloppyTblEntry = _StrAgentFloppyTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10, 1)
)
if mibBuilder.loadTexts:
    strAgentFloppyTblEntry.setStatus("mandatory")
_StrAgentFlopVendor_Type = DisplayString
_StrAgentFlopVendor_Object = MibTableColumn
strAgentFlopVendor = _StrAgentFlopVendor_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10, 1, 1),
    _StrAgentFlopVendor_Type()
)
strAgentFlopVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentFlopVendor.setStatus("mandatory")
_StrAgentFlopDescription_Type = DisplayString
_StrAgentFlopDescription_Object = MibTableColumn
strAgentFlopDescription = _StrAgentFlopDescription_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10, 1, 2),
    _StrAgentFlopDescription_Type()
)
strAgentFlopDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentFlopDescription.setStatus("mandatory")
_StrAgentFlopFirmware_Type = DisplayString
_StrAgentFlopFirmware_Object = MibTableColumn
strAgentFlopFirmware = _StrAgentFlopFirmware_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10, 1, 3),
    _StrAgentFlopFirmware_Type()
)
strAgentFlopFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentFlopFirmware.setStatus("mandatory")
_StrAgentFlopSerialNo_Type = DisplayString
_StrAgentFlopSerialNo_Object = MibTableColumn
strAgentFlopSerialNo = _StrAgentFlopSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 10, 1, 4),
    _StrAgentFlopSerialNo_Type()
)
strAgentFlopSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentFlopSerialNo.setStatus("mandatory")
_StrAgentnVolumes_Type = Integer32
_StrAgentnVolumes_Object = MibScalar
strAgentnVolumes = _StrAgentnVolumes_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 11),
    _StrAgentnVolumes_Type()
)
strAgentnVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentnVolumes.setStatus("mandatory")
_StrAgentVolumesTbl_Object = MibTable
strAgentVolumesTbl = _StrAgentVolumesTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12)
)
if mibBuilder.loadTexts:
    strAgentVolumesTbl.setStatus("mandatory")
_StrAgentVolumesTblEntry_Object = MibTableRow
strAgentVolumesTblEntry = _StrAgentVolumesTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1)
)
if mibBuilder.loadTexts:
    strAgentVolumesTblEntry.setStatus("mandatory")
_StrAgentVolDriveLetter_Type = DisplayString
_StrAgentVolDriveLetter_Object = MibTableColumn
strAgentVolDriveLetter = _StrAgentVolDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 1),
    _StrAgentVolDriveLetter_Type()
)
strAgentVolDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolDriveLetter.setStatus("mandatory")
_StrAgentVolDriveLabel_Type = DisplayString
_StrAgentVolDriveLabel_Object = MibTableColumn
strAgentVolDriveLabel = _StrAgentVolDriveLabel_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 2),
    _StrAgentVolDriveLabel_Type()
)
strAgentVolDriveLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolDriveLabel.setStatus("mandatory")
_StrAgentVolFileSystemType_Type = DisplayString
_StrAgentVolFileSystemType_Object = MibTableColumn
strAgentVolFileSystemType = _StrAgentVolFileSystemType_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 3),
    _StrAgentVolFileSystemType_Type()
)
strAgentVolFileSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolFileSystemType.setStatus("mandatory")
_StrAgentVolCapacityInMb_Type = Integer32
_StrAgentVolCapacityInMb_Object = MibTableColumn
strAgentVolCapacityInMb = _StrAgentVolCapacityInMb_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 4),
    _StrAgentVolCapacityInMb_Type()
)
strAgentVolCapacityInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolCapacityInMb.setStatus("mandatory")
_StrAgentVolClusterSize_Type = Integer32
_StrAgentVolClusterSize_Object = MibTableColumn
strAgentVolClusterSize = _StrAgentVolClusterSize_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 5),
    _StrAgentVolClusterSize_Type()
)
strAgentVolClusterSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolClusterSize.setStatus("mandatory")
_StrAgentVolPercentUsed_Type = Integer32
_StrAgentVolPercentUsed_Object = MibTableColumn
strAgentVolPercentUsed = _StrAgentVolPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 12, 1, 6),
    _StrAgentVolPercentUsed_Type()
)
strAgentVolPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strAgentVolPercentUsed.setStatus("mandatory")
_StrAgentStateThreshhold_Type = Integer32
_StrAgentStateThreshhold_Object = MibScalar
strAgentStateThreshhold = _StrAgentStateThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 13),
    _StrAgentStateThreshhold_Type()
)
strAgentStateThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strAgentStateThreshhold.setStatus("mandatory")
_StrAgentSpaceThreshhold_Type = Integer32
_StrAgentSpaceThreshhold_Object = MibScalar
strAgentSpaceThreshhold = _StrAgentSpaceThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 14),
    _StrAgentSpaceThreshhold_Type()
)
strAgentSpaceThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strAgentSpaceThreshhold.setStatus("mandatory")
_StrAgentIndex_Type = Integer32
_StrAgentIndex_Object = MibScalar
strAgentIndex = _StrAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 99),
    _StrAgentIndex_Type()
)
strAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    strAgentIndex.setStatus("mandatory")
_SysAgent_ObjectIdentity = ObjectIdentity
sysAgent = _SysAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 11)
)
_SysAgentVersion_Type = Integer32
_SysAgentVersion_Object = MibScalar
sysAgentVersion = _SysAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 1),
    _SysAgentVersion_Type()
)
sysAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentVersion.setStatus("mandatory")
_SysAgentRevision_Type = Integer32
_SysAgentRevision_Object = MibScalar
sysAgentRevision = _SysAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 2),
    _SysAgentRevision_Type()
)
sysAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentRevision.setStatus("mandatory")
_SysAgentMIBVersion_Type = Integer32
_SysAgentMIBVersion_Object = MibScalar
sysAgentMIBVersion = _SysAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 3),
    _SysAgentMIBVersion_Type()
)
sysAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentMIBVersion.setStatus("mandatory")
_SysAgentMIBRevision_Type = Integer32
_SysAgentMIBRevision_Object = MibScalar
sysAgentMIBRevision = _SysAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 4),
    _SysAgentMIBRevision_Type()
)
sysAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentMIBRevision.setStatus("mandatory")
_SysAgentCPUCyclesUsed_Type = Integer32
_SysAgentCPUCyclesUsed_Object = MibScalar
sysAgentCPUCyclesUsed = _SysAgentCPUCyclesUsed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 5),
    _SysAgentCPUCyclesUsed_Type()
)
sysAgentCPUCyclesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentCPUCyclesUsed.setStatus("mandatory")
_SysAgentPCICyclesUsed_Type = Integer32
_SysAgentPCICyclesUsed_Object = MibScalar
sysAgentPCICyclesUsed = _SysAgentPCICyclesUsed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 6),
    _SysAgentPCICyclesUsed_Type()
)
sysAgentPCICyclesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentPCICyclesUsed.setStatus("mandatory")
_SysAgentInterrupts_Type = Integer32
_SysAgentInterrupts_Object = MibScalar
sysAgentInterrupts = _SysAgentInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 7),
    _SysAgentInterrupts_Type()
)
sysAgentInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentInterrupts.setStatus("mandatory")
_SysAgentMemorySize_Type = Integer32
_SysAgentMemorySize_Object = MibScalar
sysAgentMemorySize = _SysAgentMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 8),
    _SysAgentMemorySize_Type()
)
sysAgentMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentMemorySize.setStatus("mandatory")
_SysAgentMemoryUsed_Type = Integer32
_SysAgentMemoryUsed_Object = MibScalar
sysAgentMemoryUsed = _SysAgentMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 9),
    _SysAgentMemoryUsed_Type()
)
sysAgentMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentMemoryUsed.setStatus("mandatory")
_SysAgentPageFaults_Type = Integer32
_SysAgentPageFaults_Object = MibScalar
sysAgentPageFaults = _SysAgentPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 10),
    _SysAgentPageFaults_Type()
)
sysAgentPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAgentPageFaults.setStatus("mandatory")
_SysAgentPageFaultThreshhold_Type = Integer32
_SysAgentPageFaultThreshhold_Object = MibScalar
sysAgentPageFaultThreshhold = _SysAgentPageFaultThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 11),
    _SysAgentPageFaultThreshhold_Type()
)
sysAgentPageFaultThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAgentPageFaultThreshhold.setStatus("mandatory")
_SysAgentMemoryThreshhold_Type = Integer32
_SysAgentMemoryThreshhold_Object = MibScalar
sysAgentMemoryThreshhold = _SysAgentMemoryThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 12),
    _SysAgentMemoryThreshhold_Type()
)
sysAgentMemoryThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAgentMemoryThreshhold.setStatus("mandatory")
_SysAgentIndex_Type = Integer32
_SysAgentIndex_Object = MibScalar
sysAgentIndex = _SysAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 99),
    _SysAgentIndex_Type()
)
sysAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysAgentIndex.setStatus("mandatory")
_EcmAgent_ObjectIdentity = ObjectIdentity
ecmAgent = _EcmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 12)
)
_EcmAgentVersion_Type = Integer32
_EcmAgentVersion_Object = MibScalar
ecmAgentVersion = _EcmAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 1),
    _EcmAgentVersion_Type()
)
ecmAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentVersion.setStatus("mandatory")
_EcmAgentRevision_Type = Integer32
_EcmAgentRevision_Object = MibScalar
ecmAgentRevision = _EcmAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 2),
    _EcmAgentRevision_Type()
)
ecmAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentRevision.setStatus("mandatory")
_EcmAgentMIBVersion_Type = Integer32
_EcmAgentMIBVersion_Object = MibScalar
ecmAgentMIBVersion = _EcmAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 3),
    _EcmAgentMIBVersion_Type()
)
ecmAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentMIBVersion.setStatus("mandatory")
_EcmAgentMIBRevision_Type = Integer32
_EcmAgentMIBRevision_Object = MibScalar
ecmAgentMIBRevision = _EcmAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 4),
    _EcmAgentMIBRevision_Type()
)
ecmAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentMIBRevision.setStatus("mandatory")
_EcmAgentFirmwareVersion_Type = Integer32
_EcmAgentFirmwareVersion_Object = MibScalar
ecmAgentFirmwareVersion = _EcmAgentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 5),
    _EcmAgentFirmwareVersion_Type()
)
ecmAgentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentFirmwareVersion.setStatus("mandatory")
_EcmAgentnFans_Type = Integer32
_EcmAgentnFans_Object = MibScalar
ecmAgentnFans = _EcmAgentnFans_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 6),
    _EcmAgentnFans_Type()
)
ecmAgentnFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentnFans.setStatus("mandatory")
_EcmAgentFansTbl_Object = MibTable
ecmAgentFansTbl = _EcmAgentFansTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 7)
)
if mibBuilder.loadTexts:
    ecmAgentFansTbl.setStatus("mandatory")
_EcmAgentFanTblEntry_Object = MibTableRow
ecmAgentFanTblEntry = _EcmAgentFanTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 7, 1)
)
if mibBuilder.loadTexts:
    ecmAgentFanTblEntry.setStatus("mandatory")
_EcmAgentFanPresent_Type = Integer32
_EcmAgentFanPresent_Object = MibTableColumn
ecmAgentFanPresent = _EcmAgentFanPresent_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 7, 1, 1),
    _EcmAgentFanPresent_Type()
)
ecmAgentFanPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentFanPresent.setStatus("mandatory")
_EcmAgentFanState_Type = Integer32
_EcmAgentFanState_Object = MibTableColumn
ecmAgentFanState = _EcmAgentFanState_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 7, 1, 2),
    _EcmAgentFanState_Type()
)
ecmAgentFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentFanState.setStatus("mandatory")
_EcmAgentnPowers_Type = Integer32
_EcmAgentnPowers_Object = MibScalar
ecmAgentnPowers = _EcmAgentnPowers_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 8),
    _EcmAgentnPowers_Type()
)
ecmAgentnPowers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentnPowers.setStatus("mandatory")
_EcmAgentPowersTbl_Object = MibTable
ecmAgentPowersTbl = _EcmAgentPowersTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 9)
)
if mibBuilder.loadTexts:
    ecmAgentPowersTbl.setStatus("mandatory")
_EcmAgentPowerTblEntry_Object = MibTableRow
ecmAgentPowerTblEntry = _EcmAgentPowerTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 9, 1)
)
if mibBuilder.loadTexts:
    ecmAgentPowerTblEntry.setStatus("mandatory")
_EcmAgentPowerPresent_Type = Integer32
_EcmAgentPowerPresent_Object = MibTableColumn
ecmAgentPowerPresent = _EcmAgentPowerPresent_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 9, 1, 1),
    _EcmAgentPowerPresent_Type()
)
ecmAgentPowerPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentPowerPresent.setStatus("mandatory")
_EcmAgentPowerState_Type = Integer32
_EcmAgentPowerState_Object = MibTableColumn
ecmAgentPowerState = _EcmAgentPowerState_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 9, 1, 2),
    _EcmAgentPowerState_Type()
)
ecmAgentPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentPowerState.setStatus("mandatory")
_EcmAgentnVolts_Type = Integer32
_EcmAgentnVolts_Object = MibScalar
ecmAgentnVolts = _EcmAgentnVolts_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 10),
    _EcmAgentnVolts_Type()
)
ecmAgentnVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentnVolts.setStatus("mandatory")
_EcmAgentVoltsTbl_Object = MibTable
ecmAgentVoltsTbl = _EcmAgentVoltsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 11)
)
if mibBuilder.loadTexts:
    ecmAgentVoltsTbl.setStatus("mandatory")
_EcmAgentVoltTblEntry_Object = MibTableRow
ecmAgentVoltTblEntry = _EcmAgentVoltTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 11, 1)
)
if mibBuilder.loadTexts:
    ecmAgentVoltTblEntry.setStatus("mandatory")
_EcmAgentVoltage_Type = Integer32
_EcmAgentVoltage_Object = MibTableColumn
ecmAgentVoltage = _EcmAgentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 11, 1, 1),
    _EcmAgentVoltage_Type()
)
ecmAgentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentVoltage.setStatus("mandatory")
_EcmAgentVoltLowFail_Type = Integer32
_EcmAgentVoltLowFail_Object = MibTableColumn
ecmAgentVoltLowFail = _EcmAgentVoltLowFail_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 11, 1, 2),
    _EcmAgentVoltLowFail_Type()
)
ecmAgentVoltLowFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentVoltLowFail.setStatus("mandatory")
_EcmAgentVoltLowWarn_Type = Integer32
_EcmAgentVoltLowWarn_Object = MibTableColumn
ecmAgentVoltLowWarn = _EcmAgentVoltLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 11, 1, 3),
    _EcmAgentVoltLowWarn_Type()
)
ecmAgentVoltLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentVoltLowWarn.setStatus("mandatory")
_EcmAgentVoltHighWarn_Type = Integer32
_EcmAgentVoltHighWarn_Object = MibTableColumn
ecmAgentVoltHighWarn = _EcmAgentVoltHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 11, 1, 4),
    _EcmAgentVoltHighWarn_Type()
)
ecmAgentVoltHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentVoltHighWarn.setStatus("mandatory")
_EcmAgentVoltHighFail_Type = Integer32
_EcmAgentVoltHighFail_Object = MibTableColumn
ecmAgentVoltHighFail = _EcmAgentVoltHighFail_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 11, 1, 5),
    _EcmAgentVoltHighFail_Type()
)
ecmAgentVoltHighFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentVoltHighFail.setStatus("mandatory")
_EcmAgentVoltState_Type = Integer32
_EcmAgentVoltState_Object = MibTableColumn
ecmAgentVoltState = _EcmAgentVoltState_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 11, 1, 6),
    _EcmAgentVoltState_Type()
)
ecmAgentVoltState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentVoltState.setStatus("mandatory")
_EcmAgentnTemps_Type = Integer32
_EcmAgentnTemps_Object = MibScalar
ecmAgentnTemps = _EcmAgentnTemps_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 12),
    _EcmAgentnTemps_Type()
)
ecmAgentnTemps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentnTemps.setStatus("mandatory")
_EcmAgentTempsTbl_Object = MibTable
ecmAgentTempsTbl = _EcmAgentTempsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 13)
)
if mibBuilder.loadTexts:
    ecmAgentTempsTbl.setStatus("mandatory")
_EcmAgentTempTblEntry_Object = MibTableRow
ecmAgentTempTblEntry = _EcmAgentTempTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 13, 1)
)
if mibBuilder.loadTexts:
    ecmAgentTempTblEntry.setStatus("mandatory")
_EcmAgentTemperature_Type = Integer32
_EcmAgentTemperature_Object = MibTableColumn
ecmAgentTemperature = _EcmAgentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 13, 1, 1),
    _EcmAgentTemperature_Type()
)
ecmAgentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentTemperature.setStatus("mandatory")
_EcmAgentTempLowFail_Type = Integer32
_EcmAgentTempLowFail_Object = MibTableColumn
ecmAgentTempLowFail = _EcmAgentTempLowFail_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 13, 1, 2),
    _EcmAgentTempLowFail_Type()
)
ecmAgentTempLowFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentTempLowFail.setStatus("mandatory")
_EcmAgentTempLowWarn_Type = Integer32
_EcmAgentTempLowWarn_Object = MibTableColumn
ecmAgentTempLowWarn = _EcmAgentTempLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 13, 1, 3),
    _EcmAgentTempLowWarn_Type()
)
ecmAgentTempLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentTempLowWarn.setStatus("mandatory")
_EcmAgentTempHighWarn_Type = Integer32
_EcmAgentTempHighWarn_Object = MibTableColumn
ecmAgentTempHighWarn = _EcmAgentTempHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 13, 1, 4),
    _EcmAgentTempHighWarn_Type()
)
ecmAgentTempHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentTempHighWarn.setStatus("mandatory")
_EcmAgentTempHighFail_Type = Integer32
_EcmAgentTempHighFail_Object = MibTableColumn
ecmAgentTempHighFail = _EcmAgentTempHighFail_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 13, 1, 5),
    _EcmAgentTempHighFail_Type()
)
ecmAgentTempHighFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentTempHighFail.setStatus("mandatory")
_EcmAgentTempState_Type = Integer32
_EcmAgentTempState_Object = MibTableColumn
ecmAgentTempState = _EcmAgentTempState_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 13, 1, 6),
    _EcmAgentTempState_Type()
)
ecmAgentTempState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentTempState.setStatus("mandatory")
_EcmAgentnCPUs_Type = Integer32
_EcmAgentnCPUs_Object = MibScalar
ecmAgentnCPUs = _EcmAgentnCPUs_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 14),
    _EcmAgentnCPUs_Type()
)
ecmAgentnCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentnCPUs.setStatus("mandatory")
_EcmAgentCPUsTbl_Object = MibTable
ecmAgentCPUsTbl = _EcmAgentCPUsTbl_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 15)
)
if mibBuilder.loadTexts:
    ecmAgentCPUsTbl.setStatus("mandatory")
_EcmAgentCPUTblEntry_Object = MibTableRow
ecmAgentCPUTblEntry = _EcmAgentCPUTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 15, 1)
)
if mibBuilder.loadTexts:
    ecmAgentCPUTblEntry.setStatus("mandatory")
_EcmAgentCPUUsage_Type = Integer32
_EcmAgentCPUUsage_Object = MibTableColumn
ecmAgentCPUUsage = _EcmAgentCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 15, 1, 4),
    _EcmAgentCPUUsage_Type()
)
ecmAgentCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecmAgentCPUUsage.setStatus("mandatory")
_EcmAgentIndex_Type = Integer32
_EcmAgentIndex_Object = MibScalar
ecmAgentIndex = _EcmAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 99),
    _EcmAgentIndex_Type()
)
ecmAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ecmAgentIndex.setStatus("mandatory")
_EvtAgent_ObjectIdentity = ObjectIdentity
evtAgent = _EvtAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 999)
)
_EvtAgentVersion_Type = Integer32
_EvtAgentVersion_Object = MibScalar
evtAgentVersion = _EvtAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 1),
    _EvtAgentVersion_Type()
)
evtAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtAgentVersion.setStatus("mandatory")
_EvtAgentRevision_Type = Integer32
_EvtAgentRevision_Object = MibScalar
evtAgentRevision = _EvtAgentRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2),
    _EvtAgentRevision_Type()
)
evtAgentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtAgentRevision.setStatus("mandatory")
_EvtAgentMIBVersion_Type = Integer32
_EvtAgentMIBVersion_Object = MibScalar
evtAgentMIBVersion = _EvtAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 3),
    _EvtAgentMIBVersion_Type()
)
evtAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtAgentMIBVersion.setStatus("mandatory")
_EvtAgentMIBRevision_Type = Integer32
_EvtAgentMIBRevision_Object = MibScalar
evtAgentMIBRevision = _EvtAgentMIBRevision_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 4),
    _EvtAgentMIBRevision_Type()
)
evtAgentMIBRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtAgentMIBRevision.setStatus("mandatory")
_EvtAgentnEventsQueued_Type = Integer32
_EvtAgentnEventsQueued_Object = MibScalar
evtAgentnEventsQueued = _EvtAgentnEventsQueued_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 5),
    _EvtAgentnEventsQueued_Type()
)
evtAgentnEventsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtAgentnEventsQueued.setStatus("mandatory")
_EvtAgentnEventsReceived_Type = Integer32
_EvtAgentnEventsReceived_Object = MibScalar
evtAgentnEventsReceived = _EvtAgentnEventsReceived_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 6),
    _EvtAgentnEventsReceived_Type()
)
evtAgentnEventsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtAgentnEventsReceived.setStatus("mandatory")
_EvtAgentIPAddress_Type = Integer32
_EvtAgentIPAddress_Object = MibScalar
evtAgentIPAddress = _EvtAgentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 1000),
    _EvtAgentIPAddress_Type()
)
evtAgentIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evtAgentIPAddress.setStatus("mandatory")
_EvtAgentSeverity_Type = Integer32
_EvtAgentSeverity_Object = MibScalar
evtAgentSeverity = _EvtAgentSeverity_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 1001),
    _EvtAgentSeverity_Type()
)
evtAgentSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evtAgentSeverity.setStatus("mandatory")
_EvtAgentClass_Type = Integer32
_EvtAgentClass_Object = MibScalar
evtAgentClass = _EvtAgentClass_Object(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 1002),
    _EvtAgentClass_Type()
)
evtAgentClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evtAgentClass.setStatus("mandatory")
_DmiVirusAgent_ObjectIdentity = ObjectIdentity
dmiVirusAgent = _DmiVirusAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2001)
)
_DmiMemoryAgent_ObjectIdentity = ObjectIdentity
dmiMemoryAgent = _DmiMemoryAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2003)
)
_DmiGDIAgent_ObjectIdentity = ObjectIdentity
dmiGDIAgent = _DmiGDIAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2005)
)
_DmiDiskAgent_ObjectIdentity = ObjectIdentity
dmiDiskAgent = _DmiDiskAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2007)
)
_DmiSMARTAgent_ObjectIdentity = ObjectIdentity
dmiSMARTAgent = _DmiSMARTAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2009)
)
_DmiParityAgent_ObjectIdentity = ObjectIdentity
dmiParityAgent = _DmiParityAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2015)
)
_DmiPOSTAgent_ObjectIdentity = ObjectIdentity
dmiPOSTAgent = _DmiPOSTAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2017)
)

# Managed Objects groups


# Notification objects

uemTrapConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 0, 1)
)
if mibBuilder.loadTexts:
    uemTrapConfigurationChange.setStatus(
        ""
    )

uemTrapSensorCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 0, 2)
)
uemTrapSensorCritical.setObjects(
      *(("VISINET2-MIB", "uemSensorIndex"),
        ("VISINET2-MIB", "uemSensorType"),
        ("VISINET2-MIB", "uemSensorDescription"),
        ("VISINET2-MIB", "uemSensorStatus"),
        ("VISINET2-MIB", "uemSensorValue"),
        ("VISINET2-MIB", "uemSensorNominalValue"),
        ("VISINET2-MIB", "uemTrapSeverity"))
)
if mibBuilder.loadTexts:
    uemTrapSensorCritical.setStatus(
        ""
    )

uemTrapSensorWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 0, 3)
)
uemTrapSensorWarning.setObjects(
      *(("VISINET2-MIB", "uemSensorIndex"),
        ("VISINET2-MIB", "uemSensorType"),
        ("VISINET2-MIB", "uemSensorDescription"),
        ("VISINET2-MIB", "uemSensorStatus"),
        ("VISINET2-MIB", "uemSensorValue"),
        ("VISINET2-MIB", "uemSensorNominalValue"),
        ("VISINET2-MIB", "uemTrapSeverity"))
)
if mibBuilder.loadTexts:
    uemTrapSensorWarning.setStatus(
        ""
    )

uemTrapSensorNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 0, 4)
)
uemTrapSensorNormal.setObjects(
      *(("VISINET2-MIB", "uemSensorIndex"),
        ("VISINET2-MIB", "uemSensorType"),
        ("VISINET2-MIB", "uemSensorDescription"),
        ("VISINET2-MIB", "uemSensorStatus"),
        ("VISINET2-MIB", "uemSensorValue"),
        ("VISINET2-MIB", "uemSensorNominalValue"),
        ("VISINET2-MIB", "uemTrapSeverity"))
)
if mibBuilder.loadTexts:
    uemTrapSensorNormal.setStatus(
        ""
    )

uemTrapSwitchAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 0, 5)
)
uemTrapSwitchAlert.setObjects(
      *(("VISINET2-MIB", "uemSwitchIndex"),
        ("VISINET2-MIB", "uemSwitchDescription"),
        ("VISINET2-MIB", "uemSwitchContext"),
        ("VISINET2-MIB", "uemTrapSeverity"))
)
if mibBuilder.loadTexts:
    uemTrapSwitchAlert.setStatus(
        ""
    )

uemTrapSwitchNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 6, 0, 6)
)
uemTrapSwitchNormal.setObjects(
      *(("VISINET2-MIB", "uemSwitchIndex"),
        ("VISINET2-MIB", "uemSwitchDescription"),
        ("VISINET2-MIB", "uemSwitchContext"),
        ("VISINET2-MIB", "uemTrapSeverity"))
)
if mibBuilder.loadTexts:
    uemTrapSwitchNormal.setStatus(
        ""
    )

strAgentStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 1)
)
strAgentStateTrap.setObjects(
      *(("VISINET2-MIB", "strAgentDiskState"),
        ("VISINET2-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentStateTrap.setStatus(
        ""
    )

strAgentSpaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 2)
)
strAgentSpaceTrap.setObjects(
      *(("VISINET2-MIB", "strAgentVolPercentUsed"),
        ("VISINET2-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentSpaceTrap.setStatus(
        ""
    )

strAgentSmartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 3)
)
strAgentSmartTrap.setObjects(
      *(("VISINET2-MIB", "strAgentDiskSmartCond"),
        ("VISINET2-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentSmartTrap.setStatus(
        ""
    )

strAgentStateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 11)
)
strAgentStateOkTrap.setObjects(
      *(("VISINET2-MIB", "strAgentDiskState"),
        ("VISINET2-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentStateOkTrap.setStatus(
        ""
    )

strAgentSpaceOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 12)
)
strAgentSpaceOkTrap.setObjects(
      *(("VISINET2-MIB", "strAgentVolPercentUsed"),
        ("VISINET2-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentSpaceOkTrap.setStatus(
        ""
    )

strAgentSmartOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 10, 0, 13)
)
strAgentSmartOKTrap.setObjects(
      *(("VISINET2-MIB", "strAgentDiskSmartCond"),
        ("VISINET2-MIB", "strAgentIndex"))
)
if mibBuilder.loadTexts:
    strAgentSmartOKTrap.setStatus(
        ""
    )

sysAgentMemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 1)
)
sysAgentMemTrap.setObjects(
      *(("VISINET2-MIB", "sysAgentMemoryUsed"),
        ("VISINET2-MIB", "sysAgentIndex"))
)
if mibBuilder.loadTexts:
    sysAgentMemTrap.setStatus(
        ""
    )

sysAgentPageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 2)
)
sysAgentPageTrap.setObjects(
      *(("VISINET2-MIB", "sysAgentPageFaults"),
        ("VISINET2-MIB", "sysAgentIndex"))
)
if mibBuilder.loadTexts:
    sysAgentPageTrap.setStatus(
        ""
    )

sysAgentMemOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 11)
)
sysAgentMemOkTrap.setObjects(
      *(("VISINET2-MIB", "sysAgentMemoryUsed"),
        ("VISINET2-MIB", "sysAgentIndex"))
)
if mibBuilder.loadTexts:
    sysAgentMemOkTrap.setStatus(
        ""
    )

sysAgentPageOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 11, 0, 12)
)
sysAgentPageOkTrap.setObjects(
      *(("VISINET2-MIB", "sysAgentPageFaults"),
        ("VISINET2-MIB", "sysAgentIndex"))
)
if mibBuilder.loadTexts:
    sysAgentPageOkTrap.setStatus(
        ""
    )

ecmAgentFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 0, 1)
)
ecmAgentFanTrap.setObjects(
      *(("VISINET2-MIB", "ecmAgentFanState"),
        ("VISINET2-MIB", "ecmAgentIndex"))
)
if mibBuilder.loadTexts:
    ecmAgentFanTrap.setStatus(
        ""
    )

ecmAgentPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 0, 2)
)
ecmAgentPowerTrap.setObjects(
      *(("VISINET2-MIB", "ecmAgentPowerState"),
        ("VISINET2-MIB", "ecmAgentIndex"))
)
if mibBuilder.loadTexts:
    ecmAgentPowerTrap.setStatus(
        ""
    )

ecmAgentVoltCritTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 0, 3)
)
ecmAgentVoltCritTrap.setObjects(
      *(("VISINET2-MIB", "ecmAgentVoltState"),
        ("VISINET2-MIB", "ecmAgentIndex"))
)
if mibBuilder.loadTexts:
    ecmAgentVoltCritTrap.setStatus(
        ""
    )

ecmAgentVoltWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 0, 4)
)
ecmAgentVoltWarnTrap.setObjects(
      *(("VISINET2-MIB", "ecmAgentVoltState"),
        ("VISINET2-MIB", "ecmAgentIndex"))
)
if mibBuilder.loadTexts:
    ecmAgentVoltWarnTrap.setStatus(
        ""
    )

ecmAgentVoltNormTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 0, 5)
)
ecmAgentVoltNormTrap.setObjects(
      *(("VISINET2-MIB", "ecmAgentVoltState"),
        ("VISINET2-MIB", "ecmAgentIndex"))
)
if mibBuilder.loadTexts:
    ecmAgentVoltNormTrap.setStatus(
        ""
    )

ecmAgentTempCritTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 0, 6)
)
ecmAgentTempCritTrap.setObjects(
      *(("VISINET2-MIB", "ecmAgentTempState"),
        ("VISINET2-MIB", "ecmAgentIndex"))
)
if mibBuilder.loadTexts:
    ecmAgentTempCritTrap.setStatus(
        ""
    )

ecmAgentTempWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 0, 7)
)
ecmAgentTempWarnTrap.setObjects(
      *(("VISINET2-MIB", "ecmAgentTempState"),
        ("VISINET2-MIB", "ecmAgentIndex"))
)
if mibBuilder.loadTexts:
    ecmAgentTempWarnTrap.setStatus(
        ""
    )

ecmAgentTempNormTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 0, 8)
)
ecmAgentTempNormTrap.setObjects(
      *(("VISINET2-MIB", "ecmAgentTempState"),
        ("VISINET2-MIB", "ecmAgentIndex"))
)
if mibBuilder.loadTexts:
    ecmAgentTempNormTrap.setStatus(
        ""
    )

ecmAgentFanOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 0, 11)
)
ecmAgentFanOKTrap.setObjects(
      *(("VISINET2-MIB", "ecmAgentFanState"),
        ("VISINET2-MIB", "ecmAgentIndex"))
)
if mibBuilder.loadTexts:
    ecmAgentFanOKTrap.setStatus(
        ""
    )

ecmAgentPowerOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 12, 0, 12)
)
ecmAgentPowerOKTrap.setObjects(
      *(("VISINET2-MIB", "ecmAgentPowerState"),
        ("VISINET2-MIB", "ecmAgentIndex"))
)
if mibBuilder.loadTexts:
    ecmAgentPowerOKTrap.setStatus(
        ""
    )

dmiVirusDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2001, 0, 1)
)
dmiVirusDetected.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiVirusDetected.setStatus(
        ""
    )

dmiVirtualMemoryOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2003, 0, 0)
)
dmiVirtualMemoryOK.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiVirtualMemoryOK.setStatus(
        ""
    )

dmiVirtualMemoryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2003, 0, 1)
)
dmiVirtualMemoryLow.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiVirtualMemoryLow.setStatus(
        ""
    )

dmiVirtualMemoryOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2003, 0, 2)
)
dmiVirtualMemoryOut.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiVirtualMemoryOut.setStatus(
        ""
    )

dmiGDIResourceOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2005, 0, 0)
)
dmiGDIResourceOK.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiGDIResourceOK.setStatus(
        ""
    )

dmiGDIResourceLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2005, 0, 1)
)
dmiGDIResourceLow.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiGDIResourceLow.setStatus(
        ""
    )

dmiGDIResourceOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2005, 0, 2)
)
dmiGDIResourceOut.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiGDIResourceOut.setStatus(
        ""
    )

dmiDiskSpaceOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2007, 0, 0)
)
dmiDiskSpaceOK.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiDiskSpaceOK.setStatus(
        ""
    )

dmiDiskSpaceLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2007, 0, 1)
)
dmiDiskSpaceLow.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiDiskSpaceLow.setStatus(
        ""
    )

dmiDiskSpaceOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2007, 0, 2)
)
dmiDiskSpaceOut.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiDiskSpaceOut.setStatus(
        ""
    )

dmiSMARTFailing = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2009, 0, 1)
)
dmiSMARTFailing.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiSMARTFailing.setStatus(
        ""
    )

dmiSMARTNowOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2009, 0, 2)
)
dmiSMARTNowOK.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiSMARTNowOK.setStatus(
        ""
    )

dmiParityCorrection = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2015, 0, 1)
)
dmiParityCorrection.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiParityCorrection.setStatus(
        ""
    )

dmiParityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2015, 0, 2)
)
dmiParityFailure.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiParityFailure.setStatus(
        ""
    )

dmiPOSTError = NotificationType(
    (1, 3, 6, 1, 4, 1, 223, 10, 999, 2017, 0, 1)
)
dmiPOSTError.setObjects(
      *(("VISINET2-MIB", "evtAgentIPAddress"),
        ("VISINET2-MIB", "evtAgentSeverity"),
        ("VISINET2-MIB", "evtAgentClass"))
)
if mibBuilder.loadTexts:
    dmiPOSTError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VISINET2-MIB",
    **{"unisys": unisys,
       "unisysOpen": unisysOpen,
       "unisysEnvMonitor": unisysEnvMonitor,
       "uemTrapConfigurationChange": uemTrapConfigurationChange,
       "uemTrapSensorCritical": uemTrapSensorCritical,
       "uemTrapSensorWarning": uemTrapSensorWarning,
       "uemTrapSensorNormal": uemTrapSensorNormal,
       "uemTrapSwitchAlert": uemTrapSwitchAlert,
       "uemTrapSwitchNormal": uemTrapSwitchNormal,
       "uemAgentRevMajor": uemAgentRevMajor,
       "uemAgentRevMinor": uemAgentRevMinor,
       "uemMibRevMajor": uemMibRevMajor,
       "uemMibRevMinor": uemMibRevMinor,
       "uemSystemDescription": uemSystemDescription,
       "uemTrapsEnabled": uemTrapsEnabled,
       "uemTrapSeverity": uemTrapSeverity,
       "uemEnvMonitorTable": uemEnvMonitorTable,
       "uemEnvMonitorTableEntry": uemEnvMonitorTableEntry,
       "uemEnvMonIndex": uemEnvMonIndex,
       "uemEnvMonLocation": uemEnvMonLocation,
       "uemEnvMonType": uemEnvMonType,
       "uemEnvMonFwRevMajor": uemEnvMonFwRevMajor,
       "uemEnvMonFwRevMinor": uemEnvMonFwRevMinor,
       "uemEnvMonFwRelDate": uemEnvMonFwRelDate,
       "uemEnvMonUpTime": uemEnvMonUpTime,
       "uemSensorTable": uemSensorTable,
       "uemSensorTableEntry": uemSensorTableEntry,
       "uemSensorIndex": uemSensorIndex,
       "uemSensorEnvMonIndex": uemSensorEnvMonIndex,
       "uemSensorType": uemSensorType,
       "uemSensorDescription": uemSensorDescription,
       "uemSensorStatus": uemSensorStatus,
       "uemSensorValue": uemSensorValue,
       "uemSensorNominalValue": uemSensorNominalValue,
       "uemSensorHighCriticalValue": uemSensorHighCriticalValue,
       "uemSensorHighCriticalLabel": uemSensorHighCriticalLabel,
       "uemSensorHighWarningValue": uemSensorHighWarningValue,
       "uemSensorHighWarningLabel": uemSensorHighWarningLabel,
       "uemSensorLowWarningValue": uemSensorLowWarningValue,
       "uemSensorLowWarningLabel": uemSensorLowWarningLabel,
       "uemSensorLowCriticalValue": uemSensorLowCriticalValue,
       "uemSensorLowCriticalLabel": uemSensorLowCriticalLabel,
       "uemSensorEnabled": uemSensorEnabled,
       "uemSwitchTable": uemSwitchTable,
       "uemSwitchTableEntry": uemSwitchTableEntry,
       "uemSwitchIndex": uemSwitchIndex,
       "uemSwitchEnvMonIndex": uemSwitchEnvMonIndex,
       "uemSwitchDescription": uemSwitchDescription,
       "uemSwitchContext": uemSwitchContext,
       "uemSwitchCurrentState": uemSwitchCurrentState,
       "uemSwitchExpectedState": uemSwitchExpectedState,
       "uemSwitchEnabled": uemSwitchEnabled,
       "cfgAgent": cfgAgent,
       "cfgAgentVersion": cfgAgentVersion,
       "cfgAgentRevision": cfgAgentRevision,
       "cfgAgentMIBVersion": cfgAgentMIBVersion,
       "cfgAgentMIBRevision": cfgAgentMIBRevision,
       "cfgAgentBIOSVendor": cfgAgentBIOSVendor,
       "cfgAgentBIOSVersion": cfgAgentBIOSVersion,
       "cfgAgentBIOSDate": cfgAgentBIOSDate,
       "cfgAgentBIOSsROMInKb": cfgAgentBIOSsROMInKb,
       "cfgAgentBIOSBusSupport": cfgAgentBIOSBusSupport,
       "cfgAgentBIOSAddress": cfgAgentBIOSAddress,
       "cfgAgentBIOSInterruptId": cfgAgentBIOSInterruptId,
       "cfgAgentnCPUs": cfgAgentnCPUs,
       "cfgAgentCPUsTbl": cfgAgentCPUsTbl,
       "cfgAgentCPUsTblEntry": cfgAgentCPUsTblEntry,
       "cfgAgentCPUClass": cfgAgentCPUClass,
       "cfgAgentCPUName": cfgAgentCPUName,
       "cfgAgentCPUVendor": cfgAgentCPUVendor,
       "cfgAgentCPUSpeed": cfgAgentCPUSpeed,
       "cfgAgentCPUsCacheInKb": cfgAgentCPUsCacheInKb,
       "cfgAgentCPUState": cfgAgentCPUState,
       "cfgAgentSysName": cfgAgentSysName,
       "cfgAgentSysBoardVersion": cfgAgentSysBoardVersion,
       "cfgAgentSysUptimeMilSec": cfgAgentSysUptimeMilSec,
       "cfgAgentSysOS": cfgAgentSysOS,
       "cfgAgentSysnDMAs": cfgAgentSysnDMAs,
       "cfgAgentnIRQs": cfgAgentnIRQs,
       "cfgAgentIRQsTbl": cfgAgentIRQsTbl,
       "cfgAgentIRQsTblEntry": cfgAgentIRQsTblEntry,
       "cfgAgentIRQ": cfgAgentIRQ,
       "cfgAgentIRQOwner": cfgAgentIRQOwner,
       "cfgAgentIRQBus": cfgAgentIRQBus,
       "cfgAgentIRQClass": cfgAgentIRQClass,
       "cfgAgentMemSizeInMb": cfgAgentMemSizeInMb,
       "cfgAgentMemType": cfgAgentMemType,
       "cfgAgentMemSpeed": cfgAgentMemSpeed,
       "cfgAgentMemCacheInKb": cfgAgentMemCacheInKb,
       "cfgAgentMemBanks": cfgAgentMemBanks,
       "cfgAgentMemSpeedSupported": cfgAgentMemSpeedSupported,
       "cfgAgentIOKbdType": cfgAgentIOKbdType,
       "cfgAgentIOMouseType": cfgAgentIOMouseType,
       "cfgAgentIOVidType": cfgAgentIOVidType,
       "cfgAgentnSerials": cfgAgentnSerials,
       "cfgAgentSerialsTbl": cfgAgentSerialsTbl,
       "cfgAgentSerialsTblEntry": cfgAgentSerialsTblEntry,
       "cfgAgentSerialPort": cfgAgentSerialPort,
       "cfgAgentnParallels": cfgAgentnParallels,
       "cfgAgentParallelsTbl": cfgAgentParallelsTbl,
       "cfgAgentParallelsTblEntry": cfgAgentParallelsTblEntry,
       "cfgAgentParallelPort": cfgAgentParallelPort,
       "cfgAgentnControllers": cfgAgentnControllers,
       "cfgAgentControllersTbl": cfgAgentControllersTbl,
       "cfgAgentControllersTblEntry": cfgAgentControllersTblEntry,
       "cfgAgentControllerType": cfgAgentControllerType,
       "cfgAgentControllerName": cfgAgentControllerName,
       "cfgAgentControllerIRQ": cfgAgentControllerIRQ,
       "cfgAgentnTrapDests": cfgAgentnTrapDests,
       "cfgAgentTrapDestsTbl": cfgAgentTrapDestsTbl,
       "cfgAgentTrapDestsTblEntry": cfgAgentTrapDestsTblEntry,
       "cfgAgentTrapDestId": cfgAgentTrapDestId,
       "cfgAgentTrapDestIPAddr": cfgAgentTrapDestIPAddr,
       "netAgent": netAgent,
       "netAgentVersion": netAgentVersion,
       "netAgentRevision": netAgentRevision,
       "netAgentMIBVersion": netAgentMIBVersion,
       "netAgentMIBRevision": netAgentMIBRevision,
       "netAgentMachineName": netAgentMachineName,
       "netAgentLogonServer": netAgentLogonServer,
       "netAgentnNICs": netAgentnNICs,
       "netAgentNICsTbl": netAgentNICsTbl,
       "netAgentNICTblEntry": netAgentNICTblEntry,
       "netAgentVendorID": netAgentVendorID,
       "netAgentMACAddress": netAgentMACAddress,
       "netAgentFirmwareVersion": netAgentFirmwareVersion,
       "netAgentFirmwareRevision": netAgentFirmwareRevision,
       "netAgentControllerType": netAgentControllerType,
       "netAgentControllerPort": netAgentControllerPort,
       "netAgentControllerIRQ": netAgentControllerIRQ,
       "netAgentControllerBaseIO": netAgentControllerBaseIO,
       "netAgentDataSent": netAgentDataSent,
       "netAgentDataReceived": netAgentDataReceived,
       "netAgentNICDriver": netAgentNICDriver,
       "netAgentDriverName": netAgentDriverName,
       "sftAgent": sftAgent,
       "sftAgentVersion": sftAgentVersion,
       "sftAgentRevision": sftAgentRevision,
       "sftAgentMIBVersion": sftAgentMIBVersion,
       "sftAgentMIBRevision": sftAgentMIBRevision,
       "sftAgentnPackages": sftAgentnPackages,
       "sftAgentPackagesTbl": sftAgentPackagesTbl,
       "sftAgentPackagesTblEntry": sftAgentPackagesTblEntry,
       "sftAgentPackage": sftAgentPackage,
       "sftAgentnServices": sftAgentnServices,
       "sftAgentServicesTbl": sftAgentServicesTbl,
       "sftAgentServicesTblEntry": sftAgentServicesTblEntry,
       "sftAgentService": sftAgentService,
       "sftAgentServiceStartup": sftAgentServiceStartup,
       "sftAgentnDevices": sftAgentnDevices,
       "sftAgentDevicesTbl": sftAgentDevicesTbl,
       "sftAgentDevicesTblEntry": sftAgentDevicesTblEntry,
       "sftAgentDevice": sftAgentDevice,
       "sftAgentDeviceStartup": sftAgentDeviceStartup,
       "strAgent": strAgent,
       "strAgentStateTrap": strAgentStateTrap,
       "strAgentSpaceTrap": strAgentSpaceTrap,
       "strAgentSmartTrap": strAgentSmartTrap,
       "strAgentStateOkTrap": strAgentStateOkTrap,
       "strAgentSpaceOkTrap": strAgentSpaceOkTrap,
       "strAgentSmartOKTrap": strAgentSmartOKTrap,
       "strAgentVersion": strAgentVersion,
       "strAgentRevision": strAgentRevision,
       "strAgentMIBVersion": strAgentMIBVersion,
       "strAgentMIBRevision": strAgentMIBRevision,
       "strAgentnControllers": strAgentnControllers,
       "strAgentControllersTbl": strAgentControllersTbl,
       "strAgentControllersTblEntry": strAgentControllersTblEntry,
       "strAgentCtlrType": strAgentCtlrType,
       "strAgentCtlrVendor": strAgentCtlrVendor,
       "strAgentCtlrFirmware": strAgentCtlrFirmware,
       "strAgentCtlrSerialNo": strAgentCtlrSerialNo,
       "strAgentCtlrDMA": strAgentCtlrDMA,
       "strAgentCtlrIRQ": strAgentCtlrIRQ,
       "strAgentCtlrAddress": strAgentCtlrAddress,
       "strAgentCtlrIOPort": strAgentCtlrIOPort,
       "strAgentnDisks": strAgentnDisks,
       "strAgentDisksTbl": strAgentDisksTbl,
       "strAgentDisksTblEntry": strAgentDisksTblEntry,
       "strAgentDiskVendor": strAgentDiskVendor,
       "strAgentDiskDescription": strAgentDiskDescription,
       "strAgentDiskFirmware": strAgentDiskFirmware,
       "strAgentDiskPort": strAgentDiskPort,
       "strAgentDiskBus": strAgentDiskBus,
       "strAgentDiskLUN": strAgentDiskLUN,
       "strAgentDiskID": strAgentDiskID,
       "strAgentDiskSerialNo": strAgentDiskSerialNo,
       "strAgentDisknSectors": strAgentDisknSectors,
       "strAgentDiskDriveLetters": strAgentDiskDriveLetters,
       "strAgentDiskSizeInMb": strAgentDiskSizeInMb,
       "strAgentDiskState": strAgentDiskState,
       "strAgentDiskXfersPerSec": strAgentDiskXfersPerSec,
       "strAgentDiskSmartCond": strAgentDiskSmartCond,
       "strAgentnFloppies": strAgentnFloppies,
       "strAgentFloppyTbl": strAgentFloppyTbl,
       "strAgentFloppyTblEntry": strAgentFloppyTblEntry,
       "strAgentFlopVendor": strAgentFlopVendor,
       "strAgentFlopDescription": strAgentFlopDescription,
       "strAgentFlopFirmware": strAgentFlopFirmware,
       "strAgentFlopSerialNo": strAgentFlopSerialNo,
       "strAgentnVolumes": strAgentnVolumes,
       "strAgentVolumesTbl": strAgentVolumesTbl,
       "strAgentVolumesTblEntry": strAgentVolumesTblEntry,
       "strAgentVolDriveLetter": strAgentVolDriveLetter,
       "strAgentVolDriveLabel": strAgentVolDriveLabel,
       "strAgentVolFileSystemType": strAgentVolFileSystemType,
       "strAgentVolCapacityInMb": strAgentVolCapacityInMb,
       "strAgentVolClusterSize": strAgentVolClusterSize,
       "strAgentVolPercentUsed": strAgentVolPercentUsed,
       "strAgentStateThreshhold": strAgentStateThreshhold,
       "strAgentSpaceThreshhold": strAgentSpaceThreshhold,
       "strAgentIndex": strAgentIndex,
       "sysAgent": sysAgent,
       "sysAgentMemTrap": sysAgentMemTrap,
       "sysAgentPageTrap": sysAgentPageTrap,
       "sysAgentMemOkTrap": sysAgentMemOkTrap,
       "sysAgentPageOkTrap": sysAgentPageOkTrap,
       "sysAgentVersion": sysAgentVersion,
       "sysAgentRevision": sysAgentRevision,
       "sysAgentMIBVersion": sysAgentMIBVersion,
       "sysAgentMIBRevision": sysAgentMIBRevision,
       "sysAgentCPUCyclesUsed": sysAgentCPUCyclesUsed,
       "sysAgentPCICyclesUsed": sysAgentPCICyclesUsed,
       "sysAgentInterrupts": sysAgentInterrupts,
       "sysAgentMemorySize": sysAgentMemorySize,
       "sysAgentMemoryUsed": sysAgentMemoryUsed,
       "sysAgentPageFaults": sysAgentPageFaults,
       "sysAgentPageFaultThreshhold": sysAgentPageFaultThreshhold,
       "sysAgentMemoryThreshhold": sysAgentMemoryThreshhold,
       "sysAgentIndex": sysAgentIndex,
       "ecmAgent": ecmAgent,
       "ecmAgentFanTrap": ecmAgentFanTrap,
       "ecmAgentPowerTrap": ecmAgentPowerTrap,
       "ecmAgentVoltCritTrap": ecmAgentVoltCritTrap,
       "ecmAgentVoltWarnTrap": ecmAgentVoltWarnTrap,
       "ecmAgentVoltNormTrap": ecmAgentVoltNormTrap,
       "ecmAgentTempCritTrap": ecmAgentTempCritTrap,
       "ecmAgentTempWarnTrap": ecmAgentTempWarnTrap,
       "ecmAgentTempNormTrap": ecmAgentTempNormTrap,
       "ecmAgentFanOKTrap": ecmAgentFanOKTrap,
       "ecmAgentPowerOKTrap": ecmAgentPowerOKTrap,
       "ecmAgentVersion": ecmAgentVersion,
       "ecmAgentRevision": ecmAgentRevision,
       "ecmAgentMIBVersion": ecmAgentMIBVersion,
       "ecmAgentMIBRevision": ecmAgentMIBRevision,
       "ecmAgentFirmwareVersion": ecmAgentFirmwareVersion,
       "ecmAgentnFans": ecmAgentnFans,
       "ecmAgentFansTbl": ecmAgentFansTbl,
       "ecmAgentFanTblEntry": ecmAgentFanTblEntry,
       "ecmAgentFanPresent": ecmAgentFanPresent,
       "ecmAgentFanState": ecmAgentFanState,
       "ecmAgentnPowers": ecmAgentnPowers,
       "ecmAgentPowersTbl": ecmAgentPowersTbl,
       "ecmAgentPowerTblEntry": ecmAgentPowerTblEntry,
       "ecmAgentPowerPresent": ecmAgentPowerPresent,
       "ecmAgentPowerState": ecmAgentPowerState,
       "ecmAgentnVolts": ecmAgentnVolts,
       "ecmAgentVoltsTbl": ecmAgentVoltsTbl,
       "ecmAgentVoltTblEntry": ecmAgentVoltTblEntry,
       "ecmAgentVoltage": ecmAgentVoltage,
       "ecmAgentVoltLowFail": ecmAgentVoltLowFail,
       "ecmAgentVoltLowWarn": ecmAgentVoltLowWarn,
       "ecmAgentVoltHighWarn": ecmAgentVoltHighWarn,
       "ecmAgentVoltHighFail": ecmAgentVoltHighFail,
       "ecmAgentVoltState": ecmAgentVoltState,
       "ecmAgentnTemps": ecmAgentnTemps,
       "ecmAgentTempsTbl": ecmAgentTempsTbl,
       "ecmAgentTempTblEntry": ecmAgentTempTblEntry,
       "ecmAgentTemperature": ecmAgentTemperature,
       "ecmAgentTempLowFail": ecmAgentTempLowFail,
       "ecmAgentTempLowWarn": ecmAgentTempLowWarn,
       "ecmAgentTempHighWarn": ecmAgentTempHighWarn,
       "ecmAgentTempHighFail": ecmAgentTempHighFail,
       "ecmAgentTempState": ecmAgentTempState,
       "ecmAgentnCPUs": ecmAgentnCPUs,
       "ecmAgentCPUsTbl": ecmAgentCPUsTbl,
       "ecmAgentCPUTblEntry": ecmAgentCPUTblEntry,
       "ecmAgentCPUUsage": ecmAgentCPUUsage,
       "ecmAgentIndex": ecmAgentIndex,
       "evtAgent": evtAgent,
       "evtAgentVersion": evtAgentVersion,
       "evtAgentRevision": evtAgentRevision,
       "evtAgentMIBVersion": evtAgentMIBVersion,
       "evtAgentMIBRevision": evtAgentMIBRevision,
       "evtAgentnEventsQueued": evtAgentnEventsQueued,
       "evtAgentnEventsReceived": evtAgentnEventsReceived,
       "evtAgentIPAddress": evtAgentIPAddress,
       "evtAgentSeverity": evtAgentSeverity,
       "evtAgentClass": evtAgentClass,
       "dmiVirusAgent": dmiVirusAgent,
       "dmiVirusDetected": dmiVirusDetected,
       "dmiMemoryAgent": dmiMemoryAgent,
       "dmiVirtualMemoryOK": dmiVirtualMemoryOK,
       "dmiVirtualMemoryLow": dmiVirtualMemoryLow,
       "dmiVirtualMemoryOut": dmiVirtualMemoryOut,
       "dmiGDIAgent": dmiGDIAgent,
       "dmiGDIResourceOK": dmiGDIResourceOK,
       "dmiGDIResourceLow": dmiGDIResourceLow,
       "dmiGDIResourceOut": dmiGDIResourceOut,
       "dmiDiskAgent": dmiDiskAgent,
       "dmiDiskSpaceOK": dmiDiskSpaceOK,
       "dmiDiskSpaceLow": dmiDiskSpaceLow,
       "dmiDiskSpaceOut": dmiDiskSpaceOut,
       "dmiSMARTAgent": dmiSMARTAgent,
       "dmiSMARTFailing": dmiSMARTFailing,
       "dmiSMARTNowOK": dmiSMARTNowOK,
       "dmiParityAgent": dmiParityAgent,
       "dmiParityCorrection": dmiParityCorrection,
       "dmiParityFailure": dmiParityFailure,
       "dmiPOSTAgent": dmiPOSTAgent,
       "dmiPOSTError": dmiPOSTError}
)
