# SNMP MIB module (MRV-IR-HDAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IR-HDAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:48 2024
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

(TrapSeverity,) = mibBuilder.importSymbols(
    "MRV-IR-SYSTEM-MIB",
    "TrapSeverity")

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

irHdamMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 4)
)


# Types definitions



class IrHdamModuleType(Integer32):
    """Custom type IrHdamModuleType based on Integer32"""
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
        *(("alarmModule", 2),
          ("analoglModule", 4),
          ("controlModule", 3),
          ("empty", 1))
    )





class IrContactState(Integer32):
    """Custom type IrContactState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )





class IrAnalogStatus(Integer32):
    """Custom type IrAnalogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MrvBpd_ObjectIdentity = ObjectIdentity
mrvBpd = _MrvBpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33)
)
_MrvLx_ObjectIdentity = ObjectIdentity
mrvLx = _MrvLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100)
)
_IrHdam_ObjectIdentity = ObjectIdentity
irHdam = _IrHdam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1)
)
_IrHdamUnitTable_Object = MibTable
irHdamUnitTable = _IrHdamUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1)
)
if mibBuilder.loadTexts:
    irHdamUnitTable.setStatus("current")
_IrHdamUnitEntry_Object = MibTableRow
irHdamUnitEntry = _IrHdamUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1)
)
irHdamUnitEntry.setIndexNames(
    (0, "MRV-IR-HDAM-MIB", "irHdamUnitPortIndex"),
)
if mibBuilder.loadTexts:
    irHdamUnitEntry.setStatus("current")
_IrHdamUnitPortIndex_Type = Integer32
_IrHdamUnitPortIndex_Object = MibTableColumn
irHdamUnitPortIndex = _IrHdamUnitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1, 1),
    _IrHdamUnitPortIndex_Type()
)
irHdamUnitPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamUnitPortIndex.setStatus("current")


class _IrHdamFwVersion_Type(DisplayString):
    """Custom type irHdamFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrHdamFwVersion_Type.__name__ = "DisplayString"
_IrHdamFwVersion_Object = MibTableColumn
irHdamFwVersion = _IrHdamFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1, 2),
    _IrHdamFwVersion_Type()
)
irHdamFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamFwVersion.setStatus("current")


class _IrHdamConnectStatus_Type(Integer32):
    """Custom type irHdamConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_IrHdamConnectStatus_Type.__name__ = "Integer32"
_IrHdamConnectStatus_Object = MibTableColumn
irHdamConnectStatus = _IrHdamConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1, 3),
    _IrHdamConnectStatus_Type()
)
irHdamConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamConnectStatus.setStatus("current")


class _IrHdamPowerType_Type(Integer32):
    """Custom type irHdamPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerAC", 1),
          ("powerDC", 2))
    )


_IrHdamPowerType_Type.__name__ = "Integer32"
_IrHdamPowerType_Object = MibTableColumn
irHdamPowerType = _IrHdamPowerType_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1, 4),
    _IrHdamPowerType_Type()
)
irHdamPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamPowerType.setStatus("current")


class _IrHdamAction_Type(Integer32):
    """Custom type irHdamAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_IrHdamAction_Type.__name__ = "Integer32"
_IrHdamAction_Object = MibTableColumn
irHdamAction = _IrHdamAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 1, 1, 5),
    _IrHdamAction_Type()
)
irHdamAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irHdamAction.setStatus("current")
_IrHdamModuleTable_Object = MibTable
irHdamModuleTable = _IrHdamModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 2)
)
if mibBuilder.loadTexts:
    irHdamModuleTable.setStatus("current")
_IrHdamModuleEntry_Object = MibTableRow
irHdamModuleEntry = _IrHdamModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 2, 1)
)
irHdamModuleEntry.setIndexNames(
    (0, "MRV-IR-HDAM-MIB", "irHdamPortIndex"),
    (0, "MRV-IR-HDAM-MIB", "irHdamSlotIndex"),
)
if mibBuilder.loadTexts:
    irHdamModuleEntry.setStatus("current")
_IrHdamPortIndex_Type = Integer32
_IrHdamPortIndex_Object = MibTableColumn
irHdamPortIndex = _IrHdamPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 2, 1, 1),
    _IrHdamPortIndex_Type()
)
irHdamPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamPortIndex.setStatus("current")


class _IrHdamSlotIndex_Type(Integer32):
    """Custom type irHdamSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IrHdamSlotIndex_Type.__name__ = "Integer32"
_IrHdamSlotIndex_Object = MibTableColumn
irHdamSlotIndex = _IrHdamSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 2, 1, 2),
    _IrHdamSlotIndex_Type()
)
irHdamSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamSlotIndex.setStatus("current")
_IrHdamModuleType_Type = IrHdamModuleType
_IrHdamModuleType_Object = MibTableColumn
irHdamModuleType = _IrHdamModuleType_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 2, 1, 3),
    _IrHdamModuleType_Type()
)
irHdamModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamModuleType.setStatus("current")
_IrHdamPowerSupplyTable_Object = MibTable
irHdamPowerSupplyTable = _IrHdamPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3)
)
if mibBuilder.loadTexts:
    irHdamPowerSupplyTable.setStatus("current")
_IrHdamPowerSupplyEntry_Object = MibTableRow
irHdamPowerSupplyEntry = _IrHdamPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1)
)
irHdamPowerSupplyEntry.setIndexNames(
    (0, "MRV-IR-HDAM-MIB", "irHdamPortIndex"),
    (0, "MRV-IR-HDAM-MIB", "irHdamPowerIndex"),
)
if mibBuilder.loadTexts:
    irHdamPowerSupplyEntry.setStatus("current")
_IrHdamPowerPortIndex_Type = Integer32
_IrHdamPowerPortIndex_Object = MibTableColumn
irHdamPowerPortIndex = _IrHdamPowerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 1),
    _IrHdamPowerPortIndex_Type()
)
irHdamPowerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamPowerPortIndex.setStatus("current")


class _IrHdamPowerIndex_Type(Integer32):
    """Custom type irHdamPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IrHdamPowerIndex_Type.__name__ = "Integer32"
_IrHdamPowerIndex_Object = MibTableColumn
irHdamPowerIndex = _IrHdamPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 2),
    _IrHdamPowerIndex_Type()
)
irHdamPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamPowerIndex.setStatus("current")


class _IrHdamPowerUnitPresent_Type(Integer32):
    """Custom type irHdamPowerUnitPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_IrHdamPowerUnitPresent_Type.__name__ = "Integer32"
_IrHdamPowerUnitPresent_Object = MibTableColumn
irHdamPowerUnitPresent = _IrHdamPowerUnitPresent_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 3),
    _IrHdamPowerUnitPresent_Type()
)
irHdamPowerUnitPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamPowerUnitPresent.setStatus("current")


class _IrHdamPowerInputStatus_Type(Integer32):
    """Custom type irHdamPowerInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IrHdamPowerInputStatus_Type.__name__ = "Integer32"
_IrHdamPowerInputStatus_Object = MibTableColumn
irHdamPowerInputStatus = _IrHdamPowerInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 4),
    _IrHdamPowerInputStatus_Type()
)
irHdamPowerInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamPowerInputStatus.setStatus("current")


class _IrHdamPowerOutputStatus_Type(Integer32):
    """Custom type irHdamPowerOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IrHdamPowerOutputStatus_Type.__name__ = "Integer32"
_IrHdamPowerOutputStatus_Object = MibTableColumn
irHdamPowerOutputStatus = _IrHdamPowerOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 5),
    _IrHdamPowerOutputStatus_Type()
)
irHdamPowerOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamPowerOutputStatus.setStatus("current")


class _IrHdamPowerStatus_Type(Integer32):
    """Custom type irHdamPowerStatus based on Integer32"""
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
          ("off", 2),
          ("on", 1))
    )


_IrHdamPowerStatus_Type.__name__ = "Integer32"
_IrHdamPowerStatus_Object = MibTableColumn
irHdamPowerStatus = _IrHdamPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 1, 3, 1, 6),
    _IrHdamPowerStatus_Type()
)
irHdamPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHdamPowerStatus.setStatus("current")
_IrHdamAlarm_ObjectIdentity = ObjectIdentity
irHdamAlarm = _IrHdamAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2)
)
_IrAlarmConfigTable_Object = MibTable
irAlarmConfigTable = _IrAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1)
)
if mibBuilder.loadTexts:
    irAlarmConfigTable.setStatus("current")
_IrAlarmConfigEntry_Object = MibTableRow
irAlarmConfigEntry = _IrAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1)
)
irAlarmConfigEntry.setIndexNames(
    (0, "MRV-IR-HDAM-MIB", "irAlarmPortIndex"),
    (0, "MRV-IR-HDAM-MIB", "irAlarmSlotIndex"),
    (0, "MRV-IR-HDAM-MIB", "irAlarmPointIndex"),
)
if mibBuilder.loadTexts:
    irAlarmConfigEntry.setStatus("current")


class _IrAlarmPortIndex_Type(Integer32):
    """Custom type irAlarmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IrAlarmPortIndex_Type.__name__ = "Integer32"
_IrAlarmPortIndex_Object = MibTableColumn
irAlarmPortIndex = _IrAlarmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 1),
    _IrAlarmPortIndex_Type()
)
irAlarmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAlarmPortIndex.setStatus("current")


class _IrAlarmSlotIndex_Type(Integer32):
    """Custom type irAlarmSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IrAlarmSlotIndex_Type.__name__ = "Integer32"
_IrAlarmSlotIndex_Object = MibTableColumn
irAlarmSlotIndex = _IrAlarmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 2),
    _IrAlarmSlotIndex_Type()
)
irAlarmSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAlarmSlotIndex.setStatus("current")


class _IrAlarmPointIndex_Type(Integer32):
    """Custom type irAlarmPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IrAlarmPointIndex_Type.__name__ = "Integer32"
_IrAlarmPointIndex_Object = MibTableColumn
irAlarmPointIndex = _IrAlarmPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 3),
    _IrAlarmPointIndex_Type()
)
irAlarmPointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAlarmPointIndex.setStatus("current")


class _IrAlarmName_Type(DisplayString):
    """Custom type irAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrAlarmName_Type.__name__ = "DisplayString"
_IrAlarmName_Object = MibTableColumn
irAlarmName = _IrAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 4),
    _IrAlarmName_Type()
)
irAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAlarmName.setStatus("current")
_IrAlarmContactState_Type = IrContactState
_IrAlarmContactState_Object = MibTableColumn
irAlarmContactState = _IrAlarmContactState_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 5),
    _IrAlarmContactState_Type()
)
irAlarmContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAlarmContactState.setStatus("current")
_IrAlarmContactFaultState_Type = IrContactState
_IrAlarmContactFaultState_Object = MibTableColumn
irAlarmContactFaultState = _IrAlarmContactFaultState_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 6),
    _IrAlarmContactFaultState_Type()
)
irAlarmContactFaultState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAlarmContactFaultState.setStatus("current")


class _IrAlarmDebounceInterval_Type(Integer32):
    """Custom type irAlarmDebounceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_IrAlarmDebounceInterval_Type.__name__ = "Integer32"
_IrAlarmDebounceInterval_Object = MibTableColumn
irAlarmDebounceInterval = _IrAlarmDebounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 7),
    _IrAlarmDebounceInterval_Type()
)
irAlarmDebounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAlarmDebounceInterval.setStatus("current")


class _IrAlarmAudibleStatus_Type(Integer32):
    """Custom type irAlarmAudibleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IrAlarmAudibleStatus_Type.__name__ = "Integer32"
_IrAlarmAudibleStatus_Object = MibTableColumn
irAlarmAudibleStatus = _IrAlarmAudibleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 8),
    _IrAlarmAudibleStatus_Type()
)
irAlarmAudibleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAlarmAudibleStatus.setStatus("current")


class _IrAlarmTrapStatus_Type(Integer32):
    """Custom type irAlarmTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IrAlarmTrapStatus_Type.__name__ = "Integer32"
_IrAlarmTrapStatus_Object = MibTableColumn
irAlarmTrapStatus = _IrAlarmTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 9),
    _IrAlarmTrapStatus_Type()
)
irAlarmTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAlarmTrapStatus.setStatus("current")
_IrAlarmTrapSeverity_Type = TrapSeverity
_IrAlarmTrapSeverity_Object = MibTableColumn
irAlarmTrapSeverity = _IrAlarmTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 10),
    _IrAlarmTrapSeverity_Type()
)
irAlarmTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAlarmTrapSeverity.setStatus("current")
_IrAlarmCount_Type = Counter32
_IrAlarmCount_Object = MibTableColumn
irAlarmCount = _IrAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 11),
    _IrAlarmCount_Type()
)
irAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAlarmCount.setStatus("current")


class _IrAlarmTimestamp_Type(DisplayString):
    """Custom type irAlarmTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrAlarmTimestamp_Type.__name__ = "DisplayString"
_IrAlarmTimestamp_Object = MibTableColumn
irAlarmTimestamp = _IrAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 12),
    _IrAlarmTimestamp_Type()
)
irAlarmTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAlarmTimestamp.setStatus("current")


class _IrAlarmDescription_Type(DisplayString):
    """Custom type irAlarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IrAlarmDescription_Type.__name__ = "DisplayString"
_IrAlarmDescription_Object = MibTableColumn
irAlarmDescription = _IrAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 2, 1, 1, 13),
    _IrAlarmDescription_Type()
)
irAlarmDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAlarmDescription.setStatus("current")
_IrHdamControl_ObjectIdentity = ObjectIdentity
irHdamControl = _IrHdamControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 3)
)
_IrControlConfigTable_Object = MibTable
irControlConfigTable = _IrControlConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1)
)
if mibBuilder.loadTexts:
    irControlConfigTable.setStatus("current")
_IrControlConfigEntry_Object = MibTableRow
irControlConfigEntry = _IrControlConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1)
)
irControlConfigEntry.setIndexNames(
    (0, "MRV-IR-HDAM-MIB", "irControlPortIndex"),
    (0, "MRV-IR-HDAM-MIB", "irControlSlotIndex"),
    (0, "MRV-IR-HDAM-MIB", "irControlPointIndex"),
)
if mibBuilder.loadTexts:
    irControlConfigEntry.setStatus("current")


class _IrControlPortIndex_Type(Integer32):
    """Custom type irControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IrControlPortIndex_Type.__name__ = "Integer32"
_IrControlPortIndex_Object = MibTableColumn
irControlPortIndex = _IrControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 1),
    _IrControlPortIndex_Type()
)
irControlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irControlPortIndex.setStatus("current")


class _IrControlSlotIndex_Type(Integer32):
    """Custom type irControlSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IrControlSlotIndex_Type.__name__ = "Integer32"
_IrControlSlotIndex_Object = MibTableColumn
irControlSlotIndex = _IrControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 2),
    _IrControlSlotIndex_Type()
)
irControlSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irControlSlotIndex.setStatus("current")


class _IrControlPointIndex_Type(Integer32):
    """Custom type irControlPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IrControlPointIndex_Type.__name__ = "Integer32"
_IrControlPointIndex_Object = MibTableColumn
irControlPointIndex = _IrControlPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 3),
    _IrControlPointIndex_Type()
)
irControlPointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irControlPointIndex.setStatus("current")


class _IrControlName_Type(DisplayString):
    """Custom type irControlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrControlName_Type.__name__ = "DisplayString"
_IrControlName_Object = MibTableColumn
irControlName = _IrControlName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 4),
    _IrControlName_Type()
)
irControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irControlName.setStatus("current")
_IrControlState_Type = IrContactState
_IrControlState_Object = MibTableColumn
irControlState = _IrControlState_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 5),
    _IrControlState_Type()
)
irControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irControlState.setStatus("current")
_IrControlActiveState_Type = IrContactState
_IrControlActiveState_Object = MibTableColumn
irControlActiveState = _IrControlActiveState_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 6),
    _IrControlActiveState_Type()
)
irControlActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irControlActiveState.setStatus("current")


class _IrControlDescription_Type(DisplayString):
    """Custom type irControlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IrControlDescription_Type.__name__ = "DisplayString"
_IrControlDescription_Object = MibTableColumn
irControlDescription = _IrControlDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 3, 1, 1, 7),
    _IrControlDescription_Type()
)
irControlDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irControlDescription.setStatus("current")
_IrHdamAnalog_ObjectIdentity = ObjectIdentity
irHdamAnalog = _IrHdamAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4)
)
_IrAnalogConfigTable_Object = MibTable
irAnalogConfigTable = _IrAnalogConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1)
)
if mibBuilder.loadTexts:
    irAnalogConfigTable.setStatus("current")
_IrAnalogConfigEntry_Object = MibTableRow
irAnalogConfigEntry = _IrAnalogConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1)
)
irAnalogConfigEntry.setIndexNames(
    (0, "MRV-IR-HDAM-MIB", "irAnalogPortIndex"),
    (0, "MRV-IR-HDAM-MIB", "irAnalogSlotIndex"),
    (0, "MRV-IR-HDAM-MIB", "irAnalogPointIndex"),
)
if mibBuilder.loadTexts:
    irAnalogConfigEntry.setStatus("current")


class _IrAnalogPortIndex_Type(Integer32):
    """Custom type irAnalogPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IrAnalogPortIndex_Type.__name__ = "Integer32"
_IrAnalogPortIndex_Object = MibTableColumn
irAnalogPortIndex = _IrAnalogPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 1),
    _IrAnalogPortIndex_Type()
)
irAnalogPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAnalogPortIndex.setStatus("current")


class _IrAnalogSlotIndex_Type(Integer32):
    """Custom type irAnalogSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IrAnalogSlotIndex_Type.__name__ = "Integer32"
_IrAnalogSlotIndex_Object = MibTableColumn
irAnalogSlotIndex = _IrAnalogSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 2),
    _IrAnalogSlotIndex_Type()
)
irAnalogSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAnalogSlotIndex.setStatus("current")


class _IrAnalogPointIndex_Type(Integer32):
    """Custom type irAnalogPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IrAnalogPointIndex_Type.__name__ = "Integer32"
_IrAnalogPointIndex_Object = MibTableColumn
irAnalogPointIndex = _IrAnalogPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 3),
    _IrAnalogPointIndex_Type()
)
irAnalogPointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAnalogPointIndex.setStatus("current")


class _IrAnalogName_Type(DisplayString):
    """Custom type irAnalogName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrAnalogName_Type.__name__ = "DisplayString"
_IrAnalogName_Object = MibTableColumn
irAnalogName = _IrAnalogName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 4),
    _IrAnalogName_Type()
)
irAnalogName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogName.setStatus("current")


class _IrAnalogDescription_Type(DisplayString):
    """Custom type irAnalogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IrAnalogDescription_Type.__name__ = "DisplayString"
_IrAnalogDescription_Object = MibTableColumn
irAnalogDescription = _IrAnalogDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 5),
    _IrAnalogDescription_Type()
)
irAnalogDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogDescription.setStatus("current")
_IrAnalogStatus_Type = IrAnalogStatus
_IrAnalogStatus_Object = MibTableColumn
irAnalogStatus = _IrAnalogStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 6),
    _IrAnalogStatus_Type()
)
irAnalogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogStatus.setStatus("current")


class _IrAnalogValue_Type(DisplayString):
    """Custom type irAnalogValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_IrAnalogValue_Type.__name__ = "DisplayString"
_IrAnalogValue_Object = MibTableColumn
irAnalogValue = _IrAnalogValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 7),
    _IrAnalogValue_Type()
)
irAnalogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAnalogValue.setStatus("current")


class _IrAnalogCalValue_Type(DisplayString):
    """Custom type irAnalogCalValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IrAnalogCalValue_Type.__name__ = "DisplayString"
_IrAnalogCalValue_Object = MibTableColumn
irAnalogCalValue = _IrAnalogCalValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 8),
    _IrAnalogCalValue_Type()
)
irAnalogCalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAnalogCalValue.setStatus("current")


class _IrAnalogCalMinValue_Type(DisplayString):
    """Custom type irAnalogCalMinValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IrAnalogCalMinValue_Type.__name__ = "DisplayString"
_IrAnalogCalMinValue_Object = MibTableColumn
irAnalogCalMinValue = _IrAnalogCalMinValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 9),
    _IrAnalogCalMinValue_Type()
)
irAnalogCalMinValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogCalMinValue.setStatus("current")


class _IrAnalogCalMaxValue_Type(DisplayString):
    """Custom type irAnalogCalMaxValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IrAnalogCalMaxValue_Type.__name__ = "DisplayString"
_IrAnalogCalMaxValue_Object = MibTableColumn
irAnalogCalMaxValue = _IrAnalogCalMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 10),
    _IrAnalogCalMaxValue_Type()
)
irAnalogCalMaxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogCalMaxValue.setStatus("current")


class _IrAnalogCalMargin_Type(DisplayString):
    """Custom type irAnalogCalMargin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IrAnalogCalMargin_Type.__name__ = "DisplayString"
_IrAnalogCalMargin_Object = MibTableColumn
irAnalogCalMargin = _IrAnalogCalMargin_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 11),
    _IrAnalogCalMargin_Type()
)
irAnalogCalMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogCalMargin.setStatus("current")


class _IrAnalogCalUnits_Type(DisplayString):
    """Custom type irAnalogCalUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IrAnalogCalUnits_Type.__name__ = "DisplayString"
_IrAnalogCalUnits_Object = MibTableColumn
irAnalogCalUnits = _IrAnalogCalUnits_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 12),
    _IrAnalogCalUnits_Type()
)
irAnalogCalUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogCalUnits.setStatus("current")


class _IrAnalogThresholdHigh_Type(DisplayString):
    """Custom type irAnalogThresholdHigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IrAnalogThresholdHigh_Type.__name__ = "DisplayString"
_IrAnalogThresholdHigh_Object = MibTableColumn
irAnalogThresholdHigh = _IrAnalogThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 13),
    _IrAnalogThresholdHigh_Type()
)
irAnalogThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogThresholdHigh.setStatus("current")


class _IrAnalogThresholdLow_Type(DisplayString):
    """Custom type irAnalogThresholdLow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IrAnalogThresholdLow_Type.__name__ = "DisplayString"
_IrAnalogThresholdLow_Object = MibTableColumn
irAnalogThresholdLow = _IrAnalogThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 14),
    _IrAnalogThresholdLow_Type()
)
irAnalogThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogThresholdLow.setStatus("current")
_IrAnalogThresholdSeverity_Type = TrapSeverity
_IrAnalogThresholdSeverity_Object = MibTableColumn
irAnalogThresholdSeverity = _IrAnalogThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 15),
    _IrAnalogThresholdSeverity_Type()
)
irAnalogThresholdSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogThresholdSeverity.setStatus("current")


class _IrAnalogThresholdHysteresis_Type(DisplayString):
    """Custom type irAnalogThresholdHysteresis based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IrAnalogThresholdHysteresis_Type.__name__ = "DisplayString"
_IrAnalogThresholdHysteresis_Object = MibTableColumn
irAnalogThresholdHysteresis = _IrAnalogThresholdHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 16),
    _IrAnalogThresholdHysteresis_Type()
)
irAnalogThresholdHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irAnalogThresholdHysteresis.setStatus("current")
_IrAnalogThresholdHighAlarmCount_Type = Counter32
_IrAnalogThresholdHighAlarmCount_Object = MibTableColumn
irAnalogThresholdHighAlarmCount = _IrAnalogThresholdHighAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 17),
    _IrAnalogThresholdHighAlarmCount_Type()
)
irAnalogThresholdHighAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAnalogThresholdHighAlarmCount.setStatus("current")
_IrAnalogThresholdLowAlarmCount_Type = Counter32
_IrAnalogThresholdLowAlarmCount_Object = MibTableColumn
irAnalogThresholdLowAlarmCount = _IrAnalogThresholdLowAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 18),
    _IrAnalogThresholdLowAlarmCount_Type()
)
irAnalogThresholdLowAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAnalogThresholdLowAlarmCount.setStatus("current")


class _IrAnalogThresholdHighTimestamp_Type(DisplayString):
    """Custom type irAnalogThresholdHighTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrAnalogThresholdHighTimestamp_Type.__name__ = "DisplayString"
_IrAnalogThresholdHighTimestamp_Object = MibTableColumn
irAnalogThresholdHighTimestamp = _IrAnalogThresholdHighTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 19),
    _IrAnalogThresholdHighTimestamp_Type()
)
irAnalogThresholdHighTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAnalogThresholdHighTimestamp.setStatus("current")


class _IrAnalogThresholdLowTimestamp_Type(DisplayString):
    """Custom type irAnalogThresholdLowTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrAnalogThresholdLowTimestamp_Type.__name__ = "DisplayString"
_IrAnalogThresholdLowTimestamp_Object = MibTableColumn
irAnalogThresholdLowTimestamp = _IrAnalogThresholdLowTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 4, 4, 1, 1, 20),
    _IrAnalogThresholdLowTimestamp_Type()
)
irAnalogThresholdLowTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irAnalogThresholdLowTimestamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IR-HDAM-MIB",
    **{"IrHdamModuleType": IrHdamModuleType,
       "IrContactState": IrContactState,
       "IrAnalogStatus": IrAnalogStatus,
       "mrvBpd": mrvBpd,
       "mrvLx": mrvLx,
       "irHdamMib": irHdamMib,
       "irHdam": irHdam,
       "irHdamUnitTable": irHdamUnitTable,
       "irHdamUnitEntry": irHdamUnitEntry,
       "irHdamUnitPortIndex": irHdamUnitPortIndex,
       "irHdamFwVersion": irHdamFwVersion,
       "irHdamConnectStatus": irHdamConnectStatus,
       "irHdamPowerType": irHdamPowerType,
       "irHdamAction": irHdamAction,
       "irHdamModuleTable": irHdamModuleTable,
       "irHdamModuleEntry": irHdamModuleEntry,
       "irHdamPortIndex": irHdamPortIndex,
       "irHdamSlotIndex": irHdamSlotIndex,
       "irHdamModuleType": irHdamModuleType,
       "irHdamPowerSupplyTable": irHdamPowerSupplyTable,
       "irHdamPowerSupplyEntry": irHdamPowerSupplyEntry,
       "irHdamPowerPortIndex": irHdamPowerPortIndex,
       "irHdamPowerIndex": irHdamPowerIndex,
       "irHdamPowerUnitPresent": irHdamPowerUnitPresent,
       "irHdamPowerInputStatus": irHdamPowerInputStatus,
       "irHdamPowerOutputStatus": irHdamPowerOutputStatus,
       "irHdamPowerStatus": irHdamPowerStatus,
       "irHdamAlarm": irHdamAlarm,
       "irAlarmConfigTable": irAlarmConfigTable,
       "irAlarmConfigEntry": irAlarmConfigEntry,
       "irAlarmPortIndex": irAlarmPortIndex,
       "irAlarmSlotIndex": irAlarmSlotIndex,
       "irAlarmPointIndex": irAlarmPointIndex,
       "irAlarmName": irAlarmName,
       "irAlarmContactState": irAlarmContactState,
       "irAlarmContactFaultState": irAlarmContactFaultState,
       "irAlarmDebounceInterval": irAlarmDebounceInterval,
       "irAlarmAudibleStatus": irAlarmAudibleStatus,
       "irAlarmTrapStatus": irAlarmTrapStatus,
       "irAlarmTrapSeverity": irAlarmTrapSeverity,
       "irAlarmCount": irAlarmCount,
       "irAlarmTimestamp": irAlarmTimestamp,
       "irAlarmDescription": irAlarmDescription,
       "irHdamControl": irHdamControl,
       "irControlConfigTable": irControlConfigTable,
       "irControlConfigEntry": irControlConfigEntry,
       "irControlPortIndex": irControlPortIndex,
       "irControlSlotIndex": irControlSlotIndex,
       "irControlPointIndex": irControlPointIndex,
       "irControlName": irControlName,
       "irControlState": irControlState,
       "irControlActiveState": irControlActiveState,
       "irControlDescription": irControlDescription,
       "irHdamAnalog": irHdamAnalog,
       "irAnalogConfigTable": irAnalogConfigTable,
       "irAnalogConfigEntry": irAnalogConfigEntry,
       "irAnalogPortIndex": irAnalogPortIndex,
       "irAnalogSlotIndex": irAnalogSlotIndex,
       "irAnalogPointIndex": irAnalogPointIndex,
       "irAnalogName": irAnalogName,
       "irAnalogDescription": irAnalogDescription,
       "irAnalogStatus": irAnalogStatus,
       "irAnalogValue": irAnalogValue,
       "irAnalogCalValue": irAnalogCalValue,
       "irAnalogCalMinValue": irAnalogCalMinValue,
       "irAnalogCalMaxValue": irAnalogCalMaxValue,
       "irAnalogCalMargin": irAnalogCalMargin,
       "irAnalogCalUnits": irAnalogCalUnits,
       "irAnalogThresholdHigh": irAnalogThresholdHigh,
       "irAnalogThresholdLow": irAnalogThresholdLow,
       "irAnalogThresholdSeverity": irAnalogThresholdSeverity,
       "irAnalogThresholdHysteresis": irAnalogThresholdHysteresis,
       "irAnalogThresholdHighAlarmCount": irAnalogThresholdHighAlarmCount,
       "irAnalogThresholdLowAlarmCount": irAnalogThresholdLowAlarmCount,
       "irAnalogThresholdHighTimestamp": irAnalogThresholdHighTimestamp,
       "irAnalogThresholdLowTimestamp": irAnalogThresholdLowTimestamp}
)
