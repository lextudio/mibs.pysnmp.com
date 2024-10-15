# SNMP MIB module (TSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:51 2024
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
 Opaque,
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
    "Opaque",
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TslMIB_ObjectIdentity = ObjectIdentity
tslMIB = _TslMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6853)
)
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6853, 2)
)
_AlarmIdent_Type = DisplayString
_AlarmIdent_Object = MibScalar
alarmIdent = _AlarmIdent_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 1),
    _AlarmIdent_Type()
)
alarmIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIdent.setStatus("mandatory")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 2)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("mandatory")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 2, 1)
)
alarmEntry.setIndexNames(
    (0, "TSL-MIB", "alarmTableIndex"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("mandatory")


class _AlarmTableIndex_Type(Integer32):
    """Custom type alarmTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_AlarmTableIndex_Type.__name__ = "Integer32"
_AlarmTableIndex_Object = MibTableColumn
alarmTableIndex = _AlarmTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 2, 1, 1),
    _AlarmTableIndex_Type()
)
alarmTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTableIndex.setStatus("mandatory")


class _AlarmType_Type(Integer32):
    """Custom type alarmType based on Integer32"""
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
        *(("currentAlarm", 5),
          ("gpi", 2),
          ("internal", 1),
          ("outputFail", 3),
          ("psuFail", 4))
    )


_AlarmType_Type.__name__ = "Integer32"
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 2, 1, 2),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("mandatory")
_AlarmIndex_Type = Integer32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 2, 1, 3),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("mandatory")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibTableColumn
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 2, 1, 4),
    _AlarmText_Type()
)
alarmText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmText.setStatus("mandatory")


class _AlarmState_Type(Integer32):
    """Custom type alarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_AlarmState_Type.__name__ = "Integer32"
_AlarmState_Object = MibTableColumn
alarmState = _AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 2, 1, 5),
    _AlarmState_Type()
)
alarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmState.setStatus("mandatory")


class _AlarmPolarity_Type(Integer32):
    """Custom type alarmPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normallyClosed", 3),
          ("normallyOpen", 2),
          ("notApplicable", 1))
    )


_AlarmPolarity_Type.__name__ = "Integer32"
_AlarmPolarity_Object = MibTableColumn
alarmPolarity = _AlarmPolarity_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 2, 1, 6),
    _AlarmPolarity_Type()
)
alarmPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmPolarity.setStatus("mandatory")
_AlarmData_Type = Opaque
_AlarmData_Object = MibTableColumn
alarmData = _AlarmData_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 2, 1, 7),
    _AlarmData_Type()
)
alarmData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmData.setStatus("optional")
_AlarmTotal_Type = Integer32
_AlarmTotal_Object = MibScalar
alarmTotal = _AlarmTotal_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 3),
    _AlarmTotal_Type()
)
alarmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTotal.setStatus("mandatory")
_AlarmLocation_Type = DisplayString
_AlarmLocation_Object = MibScalar
alarmLocation = _AlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 4),
    _AlarmLocation_Type()
)
alarmLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLocation.setStatus("mandatory")
_AlarmEqptTemp_Type = Integer32
_AlarmEqptTemp_Object = MibScalar
alarmEqptTemp = _AlarmEqptTemp_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 5),
    _AlarmEqptTemp_Type()
)
alarmEqptTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEqptTemp.setStatus("optional")
_AlarmEqptTempHi_Type = Integer32
_AlarmEqptTempHi_Object = MibScalar
alarmEqptTempHi = _AlarmEqptTempHi_Object(
    (1, 3, 6, 1, 4, 1, 6853, 2, 6),
    _AlarmEqptTempHi_Type()
)
alarmEqptTempHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmEqptTempHi.setStatus("optional")
_Mdu12_ObjectIdentity = ObjectIdentity
mdu12 = _Mdu12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6853, 3)
)
_Mdu12Ident_Type = DisplayString
_Mdu12Ident_Object = MibScalar
mdu12Ident = _Mdu12Ident_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 1),
    _Mdu12Ident_Type()
)
mdu12Ident.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdu12Ident.setStatus("mandatory")


class _MduPowerOn_Type(Integer32):
    """Custom type mduPowerOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delayed", 3),
          ("sequential", 2),
          ("simultaneous", 1))
    )


_MduPowerOn_Type.__name__ = "Integer32"
_MduPowerOn_Object = MibScalar
mduPowerOn = _MduPowerOn_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 2),
    _MduPowerOn_Type()
)
mduPowerOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduPowerOn.setStatus("mandatory")
_MduSeqDelay_Type = Integer32
_MduSeqDelay_Object = MibScalar
mduSeqDelay = _MduSeqDelay_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 3),
    _MduSeqDelay_Type()
)
mduSeqDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduSeqDelay.setStatus("mandatory")
_MduOutputTable_Object = MibTable
mduOutputTable = _MduOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4)
)
if mibBuilder.loadTexts:
    mduOutputTable.setStatus("mandatory")
_MduOutputEntry_Object = MibTableRow
mduOutputEntry = _MduOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1)
)
mduOutputEntry.setIndexNames(
    (0, "TSL-MIB", "mduOutputIndex"),
)
if mibBuilder.loadTexts:
    mduOutputEntry.setStatus("mandatory")


class _MduOutputIndex_Type(Integer32):
    """Custom type mduOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_MduOutputIndex_Type.__name__ = "Integer32"
_MduOutputIndex_Object = MibTableColumn
mduOutputIndex = _MduOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1, 1),
    _MduOutputIndex_Type()
)
mduOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mduOutputIndex.setStatus("mandatory")


class _MduOutputState_Type(Integer32):
    """Custom type mduOutputState based on Integer32"""
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
        *(("locked-Off", 3),
          ("locked-On", 4),
          ("off", 1),
          ("on", 2))
    )


_MduOutputState_Type.__name__ = "Integer32"
_MduOutputState_Object = MibTableColumn
mduOutputState = _MduOutputState_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1, 2),
    _MduOutputState_Type()
)
mduOutputState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduOutputState.setStatus("mandatory")
_MduOutputDelay_Type = Integer32
_MduOutputDelay_Object = MibTableColumn
mduOutputDelay = _MduOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1, 3),
    _MduOutputDelay_Type()
)
mduOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduOutputDelay.setStatus("mandatory")
_MduOutputlowerCurrent_Type = Integer32
_MduOutputlowerCurrent_Object = MibTableColumn
mduOutputlowerCurrent = _MduOutputlowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1, 4),
    _MduOutputlowerCurrent_Type()
)
mduOutputlowerCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduOutputlowerCurrent.setStatus("mandatory")
_MduOutputupperCurrent_Type = Integer32
_MduOutputupperCurrent_Object = MibTableColumn
mduOutputupperCurrent = _MduOutputupperCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1, 5),
    _MduOutputupperCurrent_Type()
)
mduOutputupperCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduOutputupperCurrent.setStatus("mandatory")
_MduOutputCurrent_Type = Integer32
_MduOutputCurrent_Object = MibTableColumn
mduOutputCurrent = _MduOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1, 6),
    _MduOutputCurrent_Type()
)
mduOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mduOutputCurrent.setStatus("mandatory")
_MduOutputpowerFactor_Type = Integer32
_MduOutputpowerFactor_Object = MibTableColumn
mduOutputpowerFactor = _MduOutputpowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1, 7),
    _MduOutputpowerFactor_Type()
)
mduOutputpowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mduOutputpowerFactor.setStatus("mandatory")
_MduOutputVA_Type = Integer32
_MduOutputVA_Object = MibTableColumn
mduOutputVA = _MduOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1, 8),
    _MduOutputVA_Type()
)
mduOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mduOutputVA.setStatus("mandatory")
_MduOutputWatts_Type = Integer32
_MduOutputWatts_Object = MibTableColumn
mduOutputWatts = _MduOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1, 9),
    _MduOutputWatts_Type()
)
mduOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mduOutputWatts.setStatus("mandatory")
_MduOutputCal_Type = Integer32
_MduOutputCal_Object = MibTableColumn
mduOutputCal = _MduOutputCal_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 4, 1, 10),
    _MduOutputCal_Type()
)
mduOutputCal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduOutputCal.setStatus("mandatory")


class _MduPowerStatus_Type(Integer32):
    """Custom type mduPowerStatus based on Integer32"""
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
        *(("allOk", 4),
          ("input1OK", 2),
          ("input2OK", 3),
          ("totalLoss", 1))
    )


_MduPowerStatus_Type.__name__ = "Integer32"
_MduPowerStatus_Object = MibScalar
mduPowerStatus = _MduPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 5),
    _MduPowerStatus_Type()
)
mduPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mduPowerStatus.setStatus("mandatory")
_MduVoltageCal_Type = Integer32
_MduVoltageCal_Object = MibScalar
mduVoltageCal = _MduVoltageCal_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 6),
    _MduVoltageCal_Type()
)
mduVoltageCal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduVoltageCal.setStatus("mandatory")
_MduVoltage_Type = Integer32
_MduVoltage_Object = MibScalar
mduVoltage = _MduVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 7),
    _MduVoltage_Type()
)
mduVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mduVoltage.setStatus("mandatory")
_MduVoltageFloor_Type = Integer32
_MduVoltageFloor_Object = MibScalar
mduVoltageFloor = _MduVoltageFloor_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 8),
    _MduVoltageFloor_Type()
)
mduVoltageFloor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduVoltageFloor.setStatus("mandatory")
_MduVoltageLimit_Type = Integer32
_MduVoltageLimit_Object = MibScalar
mduVoltageLimit = _MduVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 9),
    _MduVoltageLimit_Type()
)
mduVoltageLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduVoltageLimit.setStatus("mandatory")
_MduTotalCurrent_Type = Integer32
_MduTotalCurrent_Object = MibScalar
mduTotalCurrent = _MduTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 10),
    _MduTotalCurrent_Type()
)
mduTotalCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduTotalCurrent.setStatus("mandatory")
_MduCurrentLimit_Type = Integer32
_MduCurrentLimit_Object = MibScalar
mduCurrentLimit = _MduCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 11),
    _MduCurrentLimit_Type()
)
mduCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduCurrentLimit.setStatus("mandatory")


class _MduAuxRly1_Type(Integer32):
    """Custom type mduAuxRly1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MduAuxRly1_Type.__name__ = "Integer32"
_MduAuxRly1_Object = MibScalar
mduAuxRly1 = _MduAuxRly1_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 12),
    _MduAuxRly1_Type()
)
mduAuxRly1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduAuxRly1.setStatus("mandatory")


class _MduAuxRly2_Type(Integer32):
    """Custom type mduAuxRly2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MduAuxRly2_Type.__name__ = "Integer32"
_MduAuxRly2_Object = MibScalar
mduAuxRly2 = _MduAuxRly2_Object(
    (1, 3, 6, 1, 4, 1, 6853, 3, 13),
    _MduAuxRly2_Type()
)
mduAuxRly2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mduAuxRly2.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6853, 0, 4)
)
alarmTrap.setObjects(
      *(("TSL-MIB", "alarmTableIndex"),
        ("TSL-MIB", "alarmType"),
        ("TSL-MIB", "alarmIndex"),
        ("TSL-MIB", "alarmText"),
        ("TSL-MIB", "alarmState"),
        ("TSL-MIB", "alarmPolarity"),
        ("TSL-MIB", "alarmData"))
)
if mibBuilder.loadTexts:
    alarmTrap.setStatus(
        ""
    )

alarmEqptTempHiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6853, 0, 5)
)
alarmEqptTempHiTrap.setObjects(
    ("TSL-MIB", "alarmEqptTemp")
)
if mibBuilder.loadTexts:
    alarmEqptTempHiTrap.setStatus(
        ""
    )

alarmEqptTempOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6853, 0, 6)
)
alarmEqptTempOkTrap.setObjects(
    ("TSL-MIB", "alarmEqptTemp")
)
if mibBuilder.loadTexts:
    alarmEqptTempOkTrap.setStatus(
        ""
    )

mduPowerStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6853, 0, 7)
)
mduPowerStatusTrap.setObjects(
    ("TSL-MIB", "mduPowerStatus")
)
if mibBuilder.loadTexts:
    mduPowerStatusTrap.setStatus(
        ""
    )

mduVoltageStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6853, 0, 8)
)
mduVoltageStatusTrap.setObjects(
    ("TSL-MIB", "mduVoltage")
)
if mibBuilder.loadTexts:
    mduVoltageStatusTrap.setStatus(
        ""
    )

mduTotalCurrentStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6853, 0, 9)
)
mduTotalCurrentStatusTrap.setObjects(
    ("TSL-MIB", "mduTotalCurrent")
)
if mibBuilder.loadTexts:
    mduTotalCurrentStatusTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TSL-MIB",
    **{"DisplayString": DisplayString,
       "tslMIB": tslMIB,
       "alarmTrap": alarmTrap,
       "alarmEqptTempHiTrap": alarmEqptTempHiTrap,
       "alarmEqptTempOkTrap": alarmEqptTempOkTrap,
       "mduPowerStatusTrap": mduPowerStatusTrap,
       "mduVoltageStatusTrap": mduVoltageStatusTrap,
       "mduTotalCurrentStatusTrap": mduTotalCurrentStatusTrap,
       "alarm": alarm,
       "alarmIdent": alarmIdent,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmTableIndex": alarmTableIndex,
       "alarmType": alarmType,
       "alarmIndex": alarmIndex,
       "alarmText": alarmText,
       "alarmState": alarmState,
       "alarmPolarity": alarmPolarity,
       "alarmData": alarmData,
       "alarmTotal": alarmTotal,
       "alarmLocation": alarmLocation,
       "alarmEqptTemp": alarmEqptTemp,
       "alarmEqptTempHi": alarmEqptTempHi,
       "mdu12": mdu12,
       "mdu12Ident": mdu12Ident,
       "mduPowerOn": mduPowerOn,
       "mduSeqDelay": mduSeqDelay,
       "mduOutputTable": mduOutputTable,
       "mduOutputEntry": mduOutputEntry,
       "mduOutputIndex": mduOutputIndex,
       "mduOutputState": mduOutputState,
       "mduOutputDelay": mduOutputDelay,
       "mduOutputlowerCurrent": mduOutputlowerCurrent,
       "mduOutputupperCurrent": mduOutputupperCurrent,
       "mduOutputCurrent": mduOutputCurrent,
       "mduOutputpowerFactor": mduOutputpowerFactor,
       "mduOutputVA": mduOutputVA,
       "mduOutputWatts": mduOutputWatts,
       "mduOutputCal": mduOutputCal,
       "mduPowerStatus": mduPowerStatus,
       "mduVoltageCal": mduVoltageCal,
       "mduVoltage": mduVoltage,
       "mduVoltageFloor": mduVoltageFloor,
       "mduVoltageLimit": mduVoltageLimit,
       "mduTotalCurrent": mduTotalCurrent,
       "mduCurrentLimit": mduCurrentLimit,
       "mduAuxRly1": mduAuxRly1,
       "mduAuxRly2": mduAuxRly2}
)
