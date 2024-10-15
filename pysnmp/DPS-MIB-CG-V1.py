# SNMP MIB module (DPS-MIB-CG-V1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DPS-MIB-CG-V1
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:21 2024
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

dpsCellguard = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 2)
)
dpsCellguard.setRevisions(
        ("2013-10-18 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpsInc_ObjectIdentity = ObjectIdentity
dpsInc = _DpsInc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682)
)
_CgStringChannels_Object = MibTable
cgStringChannels = _CgStringChannels_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1)
)
if mibBuilder.loadTexts:
    cgStringChannels.setStatus("current")
_CgStringEntry_Object = MibTableRow
cgStringEntry = _CgStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1, 1)
)
cgStringEntry.setIndexNames(
    (0, "DPS-MIB-CG-V1", "cgStrNumber"),
)
if mibBuilder.loadTexts:
    cgStringEntry.setStatus("current")


class _CgStrNumber_Type(Integer32):
    """Custom type cgStrNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CgStrNumber_Type.__name__ = "Integer32"
_CgStrNumber_Object = MibTableColumn
cgStrNumber = _CgStrNumber_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 1),
    _CgStrNumber_Type()
)
cgStrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStrNumber.setStatus("current")


class _CgStrEnabled_Type(Integer32):
    """Custom type cgStrEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CgStrEnabled_Type.__name__ = "Integer32"
_CgStrEnabled_Object = MibTableColumn
cgStrEnabled = _CgStrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 2),
    _CgStrEnabled_Type()
)
cgStrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStrEnabled.setStatus("current")
_CgStrStatus_Type = DisplayString
_CgStrStatus_Object = MibTableColumn
cgStrStatus = _CgStrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 3),
    _CgStrStatus_Type()
)
cgStrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStrStatus.setStatus("current")
_CgStrVoltage_Type = DisplayString
_CgStrVoltage_Object = MibTableColumn
cgStrVoltage = _CgStrVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 4),
    _CgStrVoltage_Type()
)
cgStrVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStrVoltage.setStatus("current")
_CgStrCurrent_Type = DisplayString
_CgStrCurrent_Object = MibTableColumn
cgStrCurrent = _CgStrCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 5),
    _CgStrCurrent_Type()
)
cgStrCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStrCurrent.setStatus("current")
_CgStrTempA_Type = DisplayString
_CgStrTempA_Object = MibTableColumn
cgStrTempA = _CgStrTempA_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 6),
    _CgStrTempA_Type()
)
cgStrTempA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStrTempA.setStatus("current")
_CgStrTempB_Type = DisplayString
_CgStrTempB_Object = MibTableColumn
cgStrTempB = _CgStrTempB_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 7),
    _CgStrTempB_Type()
)
cgStrTempB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStrTempB.setStatus("current")
_CgStrConductance_Type = DisplayString
_CgStrConductance_Object = MibTableColumn
cgStrConductance = _CgStrConductance_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 8),
    _CgStrConductance_Type()
)
cgStrConductance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStrConductance.setStatus("current")
_CgStrLife_Type = DisplayString
_CgStrLife_Object = MibTableColumn
cgStrLife = _CgStrLife_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 9),
    _CgStrLife_Type()
)
cgStrLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStrLife.setStatus("current")
_CgBatteryChannels_Object = MibTable
cgBatteryChannels = _CgBatteryChannels_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 2)
)
if mibBuilder.loadTexts:
    cgBatteryChannels.setStatus("current")
_CgBatteryEntry_Object = MibTableRow
cgBatteryEntry = _CgBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 2, 1)
)
cgBatteryEntry.setIndexNames(
    (0, "DPS-MIB-CG-V1", "cgStringNumber"),
    (0, "DPS-MIB-CG-V1", "cgBatteryNumber"),
)
if mibBuilder.loadTexts:
    cgBatteryEntry.setStatus("current")


class _CgStringNumber_Type(Integer32):
    """Custom type cgStringNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CgStringNumber_Type.__name__ = "Integer32"
_CgStringNumber_Object = MibTableColumn
cgStringNumber = _CgStringNumber_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 1),
    _CgStringNumber_Type()
)
cgStringNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStringNumber.setStatus("current")


class _CgBatteryNumber_Type(Integer32):
    """Custom type cgBatteryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_CgBatteryNumber_Type.__name__ = "Integer32"
_CgBatteryNumber_Object = MibTableColumn
cgBatteryNumber = _CgBatteryNumber_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 2),
    _CgBatteryNumber_Type()
)
cgBatteryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgBatteryNumber.setStatus("current")
_CgStatus_Type = DisplayString
_CgStatus_Object = MibTableColumn
cgStatus = _CgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 3),
    _CgStatus_Type()
)
cgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStatus.setStatus("current")
_CgVoltage_Type = DisplayString
_CgVoltage_Object = MibTableColumn
cgVoltage = _CgVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 4),
    _CgVoltage_Type()
)
cgVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgVoltage.setStatus("current")
_CgTemperature_Type = DisplayString
_CgTemperature_Object = MibTableColumn
cgTemperature = _CgTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 5),
    _CgTemperature_Type()
)
cgTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgTemperature.setStatus("current")
_CgStrapResist_Type = DisplayString
_CgStrapResist_Object = MibTableColumn
cgStrapResist = _CgStrapResist_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 6),
    _CgStrapResist_Type()
)
cgStrapResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgStrapResist.setStatus("current")
_CgConductance_Type = DisplayString
_CgConductance_Object = MibTableColumn
cgConductance = _CgConductance_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 7),
    _CgConductance_Type()
)
cgConductance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgConductance.setStatus("current")
_CgBatteryLife_Type = DisplayString
_CgBatteryLife_Object = MibTableColumn
cgBatteryLife = _CgBatteryLife_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 8),
    _CgBatteryLife_Type()
)
cgBatteryLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgBatteryLife.setStatus("current")
_CellguardTrap_ObjectIdentity = ObjectIdentity
cellguardTrap = _CellguardTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 2, 8000)
)


class _CgTrapType_Type(Integer32):
    """Custom type cgTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("conductance", 6),
          ("current", 2),
          ("life", 5),
          ("strapResistance", 4),
          ("temperature", 3),
          ("unknown", 0),
          ("voltage", 1))
    )


_CgTrapType_Type.__name__ = "Integer32"
_CgTrapType_Object = MibScalar
cgTrapType = _CgTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 8000, 2),
    _CgTrapType_Type()
)
cgTrapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgTrapType.setStatus("current")


class _CgTrapStatus_Type(Integer32):
    """Custom type cgTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("majorOver", 4),
          ("majorUnder", 3),
          ("minorOver", 2),
          ("minorUnder", 1),
          ("noAlarm", 0),
          ("notDetected", 5))
    )


_CgTrapStatus_Type.__name__ = "Integer32"
_CgTrapStatus_Object = MibScalar
cgTrapStatus = _CgTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 8000, 3),
    _CgTrapStatus_Type()
)
cgTrapStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgTrapStatus.setStatus("current")
_CgTrapValue_Type = DisplayString
_CgTrapValue_Object = MibScalar
cgTrapValue = _CgTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 2682, 2, 8000, 4),
    _CgTrapValue_Type()
)
cgTrapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgTrapValue.setStatus("current")

# Managed Objects groups


# Notification objects

cgAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 2, 8000, 1)
)
if mibBuilder.loadTexts:
    cgAlarmTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPS-MIB-CG-V1",
    **{"dpsInc": dpsInc,
       "dpsCellguard": dpsCellguard,
       "cgStringChannels": cgStringChannels,
       "cgStringEntry": cgStringEntry,
       "cgStrNumber": cgStrNumber,
       "cgStrEnabled": cgStrEnabled,
       "cgStrStatus": cgStrStatus,
       "cgStrVoltage": cgStrVoltage,
       "cgStrCurrent": cgStrCurrent,
       "cgStrTempA": cgStrTempA,
       "cgStrTempB": cgStrTempB,
       "cgStrConductance": cgStrConductance,
       "cgStrLife": cgStrLife,
       "cgBatteryChannels": cgBatteryChannels,
       "cgBatteryEntry": cgBatteryEntry,
       "cgStringNumber": cgStringNumber,
       "cgBatteryNumber": cgBatteryNumber,
       "cgStatus": cgStatus,
       "cgVoltage": cgVoltage,
       "cgTemperature": cgTemperature,
       "cgStrapResist": cgStrapResist,
       "cgConductance": cgConductance,
       "cgBatteryLife": cgBatteryLife,
       "cellguardTrap": cellguardTrap,
       "cgAlarmTrap": cgAlarmTrap,
       "cgTrapType": cgTrapType,
       "cgTrapStatus": cgTrapStatus,
       "cgTrapValue": cgTrapValue}
)
