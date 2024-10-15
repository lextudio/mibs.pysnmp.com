# SNMP MIB module (ELTEK-DISTRIBUTED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEK-DISTRIBUTED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:58 2024
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

eltek = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12148)
)
eltek.setRevisions(
        ("2011-06-05 14:44",
         "2011-03-22 14:41",
         "2010-10-29 08:29",
         "2009-03-12 15:15",
         "2008-01-30 11:49",
         "2007-06-22 11:27",
         "2005-09-07 12:38",
         "2005-06-28 11:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltekDistributedPlantV7_ObjectIdentity = ObjectIdentity
eltekDistributedPlantV7 = _EltekDistributedPlantV7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9)
)
_ControlSystem_ObjectIdentity = ObjectIdentity
controlSystem = _ControlSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1)
)
_SystemTime_ObjectIdentity = ObjectIdentity
systemTime = _SystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 1)
)


class _SystemTimeTime_Type(DisplayString):
    """Custom type systemTimeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemTimeTime_Type.__name__ = "DisplayString"
_SystemTimeTime_Object = MibScalar
systemTimeTime = _SystemTimeTime_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 1, 1),
    _SystemTimeTime_Type()
)
systemTimeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTimeTime.setStatus("current")


class _SystemInfoRefresh_Type(Integer32):
    """Custom type systemInfoRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("refreshdata", 1))
    )


_SystemInfoRefresh_Type.__name__ = "Integer32"
_SystemInfoRefresh_Object = MibScalar
systemInfoRefresh = _SystemInfoRefresh_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 2),
    _SystemInfoRefresh_Type()
)
systemInfoRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemInfoRefresh.setStatus("current")


class _SystemTrapRepeatRate_Type(Integer32):
    """Custom type systemTrapRepeatRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SystemTrapRepeatRate_Type.__name__ = "Integer32"
_SystemTrapRepeatRate_Object = MibScalar
systemTrapRepeatRate = _SystemTrapRepeatRate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 3),
    _SystemTrapRepeatRate_Type()
)
systemTrapRepeatRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTrapRepeatRate.setStatus("current")


class _SystemSendOffTrap_Type(Integer32):
    """Custom type systemSendOffTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SystemSendOffTrap_Type.__name__ = "Integer32"
_SystemSendOffTrap_Object = MibScalar
systemSendOffTrap = _SystemSendOffTrap_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 4),
    _SystemSendOffTrap_Type()
)
systemSendOffTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSendOffTrap.setStatus("current")


class _SystemNumOfControlUnits_Type(Integer32):
    """Custom type systemNumOfControlUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SystemNumOfControlUnits_Type.__name__ = "Integer32"
_SystemNumOfControlUnits_Object = MibScalar
systemNumOfControlUnits = _SystemNumOfControlUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 5),
    _SystemNumOfControlUnits_Type()
)
systemNumOfControlUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNumOfControlUnits.setStatus("current")


class _SystemControlUnitIndex_Type(Integer32):
    """Custom type systemControlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SystemControlUnitIndex_Type.__name__ = "Integer32"
_SystemControlUnitIndex_Object = MibScalar
systemControlUnitIndex = _SystemControlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 6),
    _SystemControlUnitIndex_Type()
)
systemControlUnitIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemControlUnitIndex.setStatus("current")
_SystemControlUnitTable_Object = MibTable
systemControlUnitTable = _SystemControlUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7)
)
if mibBuilder.loadTexts:
    systemControlUnitTable.setStatus("current")
_SystemControlUnitEntry_Object = MibTableRow
systemControlUnitEntry = _SystemControlUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1)
)
systemControlUnitEntry.setIndexNames(
    (0, "ELTEK-DISTRIBUTED-MIB", "systemControlUnitIndex"),
)
if mibBuilder.loadTexts:
    systemControlUnitEntry.setStatus("current")


class _InputControlUnitID_Type(Integer32):
    """Custom type inputControlUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_InputControlUnitID_Type.__name__ = "Integer32"
_InputControlUnitID_Object = MibTableColumn
inputControlUnitID = _InputControlUnitID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 1),
    _InputControlUnitID_Type()
)
inputControlUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputControlUnitID.setStatus("current")


class _InputUserConfigurable1_Type(Integer32):
    """Custom type inputUserConfigurable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_InputUserConfigurable1_Type.__name__ = "Integer32"
_InputUserConfigurable1_Object = MibTableColumn
inputUserConfigurable1 = _InputUserConfigurable1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 2),
    _InputUserConfigurable1_Type()
)
inputUserConfigurable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurable1.setStatus("current")


class _InputUserConfigurable2_Type(Integer32):
    """Custom type inputUserConfigurable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_InputUserConfigurable2_Type.__name__ = "Integer32"
_InputUserConfigurable2_Object = MibTableColumn
inputUserConfigurable2 = _InputUserConfigurable2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 3),
    _InputUserConfigurable2_Type()
)
inputUserConfigurable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurable2.setStatus("current")


class _InputUserConfigurable3_Type(Integer32):
    """Custom type inputUserConfigurable3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_InputUserConfigurable3_Type.__name__ = "Integer32"
_InputUserConfigurable3_Object = MibTableColumn
inputUserConfigurable3 = _InputUserConfigurable3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 4),
    _InputUserConfigurable3_Type()
)
inputUserConfigurable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurable3.setStatus("current")


class _InputUserConfigurable4_Type(Integer32):
    """Custom type inputUserConfigurable4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_InputUserConfigurable4_Type.__name__ = "Integer32"
_InputUserConfigurable4_Object = MibTableColumn
inputUserConfigurable4 = _InputUserConfigurable4_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 5),
    _InputUserConfigurable4_Type()
)
inputUserConfigurable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurable4.setStatus("current")


class _InputUserConfigurable5_Type(Integer32):
    """Custom type inputUserConfigurable5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_InputUserConfigurable5_Type.__name__ = "Integer32"
_InputUserConfigurable5_Object = MibTableColumn
inputUserConfigurable5 = _InputUserConfigurable5_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 6),
    _InputUserConfigurable5_Type()
)
inputUserConfigurable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurable5.setStatus("current")


class _InputUserConfigurable6_Type(Integer32):
    """Custom type inputUserConfigurable6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_InputUserConfigurable6_Type.__name__ = "Integer32"
_InputUserConfigurable6_Object = MibTableColumn
inputUserConfigurable6 = _InputUserConfigurable6_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 7),
    _InputUserConfigurable6_Type()
)
inputUserConfigurable6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurable6.setStatus("current")


class _InputUserConfigurable7_Type(Integer32):
    """Custom type inputUserConfigurable7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_InputUserConfigurable7_Type.__name__ = "Integer32"
_InputUserConfigurable7_Object = MibTableColumn
inputUserConfigurable7 = _InputUserConfigurable7_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 8),
    _InputUserConfigurable7_Type()
)
inputUserConfigurable7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurable7.setStatus("current")


class _InputUserConfigurable8_Type(Integer32):
    """Custom type inputUserConfigurable8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_InputUserConfigurable8_Type.__name__ = "Integer32"
_InputUserConfigurable8_Object = MibTableColumn
inputUserConfigurable8 = _InputUserConfigurable8_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 9),
    _InputUserConfigurable8_Type()
)
inputUserConfigurable8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurable8.setStatus("current")


class _InputUserConfigurable9_Type(Integer32):
    """Custom type inputUserConfigurable9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_InputUserConfigurable9_Type.__name__ = "Integer32"
_InputUserConfigurable9_Object = MibTableColumn
inputUserConfigurable9 = _InputUserConfigurable9_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 10),
    _InputUserConfigurable9_Type()
)
inputUserConfigurable9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurable9.setStatus("current")


class _InputUserConfigurable10_Type(Integer32):
    """Custom type inputUserConfigurable10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_InputUserConfigurable10_Type.__name__ = "Integer32"
_InputUserConfigurable10_Object = MibTableColumn
inputUserConfigurable10 = _InputUserConfigurable10_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 7, 1, 11),
    _InputUserConfigurable10_Type()
)
inputUserConfigurable10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurable10.setStatus("current")


class _SystemLinkStatus_Type(Integer32):
    """Custom type systemLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 0),
          ("linkup", 1))
    )


_SystemLinkStatus_Type.__name__ = "Integer32"
_SystemLinkStatus_Object = MibScalar
systemLinkStatus = _SystemLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 8),
    _SystemLinkStatus_Type()
)
systemLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLinkStatus.setStatus("current")


class _SystemInitiateEEPROM_Type(Integer32):
    """Custom type systemInitiateEEPROM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("start", 1))
    )


_SystemInitiateEEPROM_Type.__name__ = "Integer32"
_SystemInitiateEEPROM_Object = MibScalar
systemInitiateEEPROM = _SystemInitiateEEPROM_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 9),
    _SystemInitiateEEPROM_Type()
)
systemInitiateEEPROM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemInitiateEEPROM.setStatus("deprecated")


class _SystemLastDigInput_Type(Integer32):
    """Custom type systemLastDigInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SystemLastDigInput_Type.__name__ = "Integer32"
_SystemLastDigInput_Object = MibScalar
systemLastDigInput = _SystemLastDigInput_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 10),
    _SystemLastDigInput_Type()
)
systemLastDigInput.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemLastDigInput.setStatus("current")
_SystemTrapCounter_Type = Counter32
_SystemTrapCounter_Object = MibScalar
systemTrapCounter = _SystemTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 11),
    _SystemTrapCounter_Type()
)
systemTrapCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemTrapCounter.setStatus("current")


class _SystemHeartBeatTrapRepeatRate_Type(Integer32):
    """Custom type systemHeartBeatTrapRepeatRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SystemHeartBeatTrapRepeatRate_Type.__name__ = "Integer32"
_SystemHeartBeatTrapRepeatRate_Object = MibScalar
systemHeartBeatTrapRepeatRate = _SystemHeartBeatTrapRepeatRate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 12),
    _SystemHeartBeatTrapRepeatRate_Type()
)
systemHeartBeatTrapRepeatRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemHeartBeatTrapRepeatRate.setStatus("current")


class _SystemResetManualAlarms_Type(Integer32):
    """Custom type systemResetManualAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apply", 1),
          ("pushbutton", 0))
    )


_SystemResetManualAlarms_Type.__name__ = "Integer32"
_SystemResetManualAlarms_Object = MibScalar
systemResetManualAlarms = _SystemResetManualAlarms_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 13),
    _SystemResetManualAlarms_Type()
)
systemResetManualAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResetManualAlarms.setStatus("current")


class _SystemControlUnitInputIndex_Type(Integer32):
    """Custom type systemControlUnitInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SystemControlUnitInputIndex_Type.__name__ = "Integer32"
_SystemControlUnitInputIndex_Object = MibScalar
systemControlUnitInputIndex = _SystemControlUnitInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 14),
    _SystemControlUnitInputIndex_Type()
)
systemControlUnitInputIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemControlUnitInputIndex.setStatus("current")
_SystemControlUnitInputTable_Object = MibTable
systemControlUnitInputTable = _SystemControlUnitInputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15)
)
if mibBuilder.loadTexts:
    systemControlUnitInputTable.setStatus("current")
_SystemControlUnitInputEntry_Object = MibTableRow
systemControlUnitInputEntry = _SystemControlUnitInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1)
)
systemControlUnitInputEntry.setIndexNames(
    (0, "ELTEK-DISTRIBUTED-MIB", "systemControlUnitInputIndex"),
)
if mibBuilder.loadTexts:
    systemControlUnitInputEntry.setStatus("current")
_InputUnitID_Type = Integer32
_InputUnitID_Object = MibTableColumn
inputUnitID = _InputUnitID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 1),
    _InputUnitID_Type()
)
inputUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUnitID.setStatus("current")
_InputUserConfigurableText1_Type = DisplayString
_InputUserConfigurableText1_Object = MibTableColumn
inputUserConfigurableText1 = _InputUserConfigurableText1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 2),
    _InputUserConfigurableText1_Type()
)
inputUserConfigurableText1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurableText1.setStatus("current")
_InputUserConfigurableText2_Type = DisplayString
_InputUserConfigurableText2_Object = MibTableColumn
inputUserConfigurableText2 = _InputUserConfigurableText2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 3),
    _InputUserConfigurableText2_Type()
)
inputUserConfigurableText2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurableText2.setStatus("current")
_InputUserConfigurableText3_Type = DisplayString
_InputUserConfigurableText3_Object = MibTableColumn
inputUserConfigurableText3 = _InputUserConfigurableText3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 4),
    _InputUserConfigurableText3_Type()
)
inputUserConfigurableText3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurableText3.setStatus("current")
_InputUserConfigurableText4_Type = DisplayString
_InputUserConfigurableText4_Object = MibTableColumn
inputUserConfigurableText4 = _InputUserConfigurableText4_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 5),
    _InputUserConfigurableText4_Type()
)
inputUserConfigurableText4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurableText4.setStatus("current")
_InputUserConfigurableText5_Type = DisplayString
_InputUserConfigurableText5_Object = MibTableColumn
inputUserConfigurableText5 = _InputUserConfigurableText5_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 6),
    _InputUserConfigurableText5_Type()
)
inputUserConfigurableText5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurableText5.setStatus("current")
_InputUserConfigurableText6_Type = DisplayString
_InputUserConfigurableText6_Object = MibTableColumn
inputUserConfigurableText6 = _InputUserConfigurableText6_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 7),
    _InputUserConfigurableText6_Type()
)
inputUserConfigurableText6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurableText6.setStatus("current")
_InputUserConfigurableText7_Type = DisplayString
_InputUserConfigurableText7_Object = MibTableColumn
inputUserConfigurableText7 = _InputUserConfigurableText7_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 8),
    _InputUserConfigurableText7_Type()
)
inputUserConfigurableText7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurableText7.setStatus("current")
_InputUserConfigurableText8_Type = DisplayString
_InputUserConfigurableText8_Object = MibTableColumn
inputUserConfigurableText8 = _InputUserConfigurableText8_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 9),
    _InputUserConfigurableText8_Type()
)
inputUserConfigurableText8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurableText8.setStatus("current")
_InputUserConfigurableText9_Type = DisplayString
_InputUserConfigurableText9_Object = MibTableColumn
inputUserConfigurableText9 = _InputUserConfigurableText9_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 10),
    _InputUserConfigurableText9_Type()
)
inputUserConfigurableText9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurableText9.setStatus("current")
_InputUserConfigurableText10_Type = DisplayString
_InputUserConfigurableText10_Object = MibTableColumn
inputUserConfigurableText10 = _InputUserConfigurableText10_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 15, 1, 11),
    _InputUserConfigurableText10_Type()
)
inputUserConfigurableText10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputUserConfigurableText10.setStatus("current")


class _SystemResetCtrlSystem_Type(Integer32):
    """Custom type systemResetCtrlSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("reboot", 1))
    )


_SystemResetCtrlSystem_Type.__name__ = "Integer32"
_SystemResetCtrlSystem_Object = MibScalar
systemResetCtrlSystem = _SystemResetCtrlSystem_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 16),
    _SystemResetCtrlSystem_Type()
)
systemResetCtrlSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResetCtrlSystem.setStatus("deprecated")
_IoUnits_ObjectIdentity = ObjectIdentity
ioUnits = _IoUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17)
)
_IoUnitNumberOfUnits_Type = Integer32
_IoUnitNumberOfUnits_Object = MibScalar
ioUnitNumberOfUnits = _IoUnitNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 1),
    _IoUnitNumberOfUnits_Type()
)
ioUnitNumberOfUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitNumberOfUnits.setStatus("current")


class _IoUnitsIndex_Type(Integer32):
    """Custom type ioUnitsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_IoUnitsIndex_Type.__name__ = "Integer32"
_IoUnitsIndex_Object = MibScalar
ioUnitsIndex = _IoUnitsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 2),
    _IoUnitsIndex_Type()
)
ioUnitsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ioUnitsIndex.setStatus("current")
_IoUnitsTable_Object = MibTable
ioUnitsTable = _IoUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3)
)
if mibBuilder.loadTexts:
    ioUnitsTable.setStatus("current")
_IoUnitsEntry_Object = MibTableRow
ioUnitsEntry = _IoUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1)
)
ioUnitsEntry.setIndexNames(
    (0, "ELTEK-DISTRIBUTED-MIB", "ioUnitsIndex"),
)
if mibBuilder.loadTexts:
    ioUnitsEntry.setStatus("current")
_IoUnitID_Type = Integer32
_IoUnitID_Object = MibTableColumn
ioUnitID = _IoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 1),
    _IoUnitID_Type()
)
ioUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitID.setStatus("current")
_IoUnitOutDoorTemp1_Type = Integer32
_IoUnitOutDoorTemp1_Object = MibTableColumn
ioUnitOutDoorTemp1 = _IoUnitOutDoorTemp1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 2),
    _IoUnitOutDoorTemp1_Type()
)
ioUnitOutDoorTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitOutDoorTemp1.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitOutDoorTemp1.setUnits("Deg. C/F; i.e. 25 = 25 Deg.")
_IoUnitOutDoorTemp2_Type = Integer32
_IoUnitOutDoorTemp2_Object = MibTableColumn
ioUnitOutDoorTemp2 = _IoUnitOutDoorTemp2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 3),
    _IoUnitOutDoorTemp2_Type()
)
ioUnitOutDoorTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitOutDoorTemp2.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitOutDoorTemp2.setUnits("Deg. C/F; i.e. 25 = 25 Deg.")
_IoUnitFanSpeed1_Type = Integer32
_IoUnitFanSpeed1_Object = MibTableColumn
ioUnitFanSpeed1 = _IoUnitFanSpeed1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 4),
    _IoUnitFanSpeed1_Type()
)
ioUnitFanSpeed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitFanSpeed1.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitFanSpeed1.setUnits("Percent %")
_IoUnitFanSpeedDeltaValue1_Type = Integer32
_IoUnitFanSpeedDeltaValue1_Object = MibTableColumn
ioUnitFanSpeedDeltaValue1 = _IoUnitFanSpeedDeltaValue1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 5),
    _IoUnitFanSpeedDeltaValue1_Type()
)
ioUnitFanSpeedDeltaValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitFanSpeedDeltaValue1.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitFanSpeedDeltaValue1.setUnits("Percent %")
_IoUnitFanSpeed2_Type = Integer32
_IoUnitFanSpeed2_Object = MibTableColumn
ioUnitFanSpeed2 = _IoUnitFanSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 6),
    _IoUnitFanSpeed2_Type()
)
ioUnitFanSpeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitFanSpeed2.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitFanSpeed2.setUnits("Percent %")
_IoUnitFanSpeedDeltaValue2_Type = Integer32
_IoUnitFanSpeedDeltaValue2_Object = MibTableColumn
ioUnitFanSpeedDeltaValue2 = _IoUnitFanSpeedDeltaValue2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 7),
    _IoUnitFanSpeedDeltaValue2_Type()
)
ioUnitFanSpeedDeltaValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitFanSpeedDeltaValue2.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitFanSpeedDeltaValue2.setUnits("Percent %")


class _IoUnitProgInputText1_Type(DisplayString):
    """Custom type ioUnitProgInputText1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IoUnitProgInputText1_Type.__name__ = "DisplayString"
_IoUnitProgInputText1_Object = MibTableColumn
ioUnitProgInputText1 = _IoUnitProgInputText1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 8),
    _IoUnitProgInputText1_Type()
)
ioUnitProgInputText1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputText1.setStatus("current")


class _IoUnitProgInputStatus1_Type(Integer32):
    """Custom type ioUnitProgInputStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_IoUnitProgInputStatus1_Type.__name__ = "Integer32"
_IoUnitProgInputStatus1_Object = MibTableColumn
ioUnitProgInputStatus1 = _IoUnitProgInputStatus1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 9),
    _IoUnitProgInputStatus1_Type()
)
ioUnitProgInputStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputStatus1.setStatus("current")


class _IoUnitProgInputText2_Type(DisplayString):
    """Custom type ioUnitProgInputText2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IoUnitProgInputText2_Type.__name__ = "DisplayString"
_IoUnitProgInputText2_Object = MibTableColumn
ioUnitProgInputText2 = _IoUnitProgInputText2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 10),
    _IoUnitProgInputText2_Type()
)
ioUnitProgInputText2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputText2.setStatus("current")


class _IoUnitProgInputStatus2_Type(Integer32):
    """Custom type ioUnitProgInputStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_IoUnitProgInputStatus2_Type.__name__ = "Integer32"
_IoUnitProgInputStatus2_Object = MibTableColumn
ioUnitProgInputStatus2 = _IoUnitProgInputStatus2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 11),
    _IoUnitProgInputStatus2_Type()
)
ioUnitProgInputStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputStatus2.setStatus("current")


class _IoUnitProgInputText3_Type(DisplayString):
    """Custom type ioUnitProgInputText3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IoUnitProgInputText3_Type.__name__ = "DisplayString"
_IoUnitProgInputText3_Object = MibTableColumn
ioUnitProgInputText3 = _IoUnitProgInputText3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 12),
    _IoUnitProgInputText3_Type()
)
ioUnitProgInputText3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputText3.setStatus("current")


class _IoUnitProgInputStatus3_Type(Integer32):
    """Custom type ioUnitProgInputStatus3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_IoUnitProgInputStatus3_Type.__name__ = "Integer32"
_IoUnitProgInputStatus3_Object = MibTableColumn
ioUnitProgInputStatus3 = _IoUnitProgInputStatus3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 13),
    _IoUnitProgInputStatus3_Type()
)
ioUnitProgInputStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputStatus3.setStatus("current")


class _IoUnitProgInputText4_Type(DisplayString):
    """Custom type ioUnitProgInputText4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IoUnitProgInputText4_Type.__name__ = "DisplayString"
_IoUnitProgInputText4_Object = MibTableColumn
ioUnitProgInputText4 = _IoUnitProgInputText4_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 14),
    _IoUnitProgInputText4_Type()
)
ioUnitProgInputText4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputText4.setStatus("current")


class _IoUnitProgInputStatus4_Type(Integer32):
    """Custom type ioUnitProgInputStatus4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_IoUnitProgInputStatus4_Type.__name__ = "Integer32"
_IoUnitProgInputStatus4_Object = MibTableColumn
ioUnitProgInputStatus4 = _IoUnitProgInputStatus4_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 15),
    _IoUnitProgInputStatus4_Type()
)
ioUnitProgInputStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputStatus4.setStatus("current")


class _IoUnitProgInputText5_Type(DisplayString):
    """Custom type ioUnitProgInputText5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IoUnitProgInputText5_Type.__name__ = "DisplayString"
_IoUnitProgInputText5_Object = MibTableColumn
ioUnitProgInputText5 = _IoUnitProgInputText5_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 16),
    _IoUnitProgInputText5_Type()
)
ioUnitProgInputText5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputText5.setStatus("current")


class _IoUnitProgInputStatus5_Type(Integer32):
    """Custom type ioUnitProgInputStatus5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_IoUnitProgInputStatus5_Type.__name__ = "Integer32"
_IoUnitProgInputStatus5_Object = MibTableColumn
ioUnitProgInputStatus5 = _IoUnitProgInputStatus5_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 17),
    _IoUnitProgInputStatus5_Type()
)
ioUnitProgInputStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputStatus5.setStatus("current")


class _IoUnitProgInputText6_Type(DisplayString):
    """Custom type ioUnitProgInputText6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IoUnitProgInputText6_Type.__name__ = "DisplayString"
_IoUnitProgInputText6_Object = MibTableColumn
ioUnitProgInputText6 = _IoUnitProgInputText6_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 18),
    _IoUnitProgInputText6_Type()
)
ioUnitProgInputText6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputText6.setStatus("current")


class _IoUnitProgInputStatus6_Type(Integer32):
    """Custom type ioUnitProgInputStatus6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_IoUnitProgInputStatus6_Type.__name__ = "Integer32"
_IoUnitProgInputStatus6_Object = MibTableColumn
ioUnitProgInputStatus6 = _IoUnitProgInputStatus6_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 19),
    _IoUnitProgInputStatus6_Type()
)
ioUnitProgInputStatus6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputStatus6.setStatus("current")
_IoUnitProgInputValue1_Type = Integer32
_IoUnitProgInputValue1_Object = MibTableColumn
ioUnitProgInputValue1 = _IoUnitProgInputValue1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 20),
    _IoUnitProgInputValue1_Type()
)
ioUnitProgInputValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputValue1.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitProgInputValue1.setUnits("1/100 Volt; i.e. 500 = 5.00V")
_IoUnitProgInputValue2_Type = Integer32
_IoUnitProgInputValue2_Object = MibTableColumn
ioUnitProgInputValue2 = _IoUnitProgInputValue2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 21),
    _IoUnitProgInputValue2_Type()
)
ioUnitProgInputValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputValue2.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitProgInputValue2.setUnits("1/100 Volt; i.e. 500 = 5.00V")
_IoUnitProgInputValue3_Type = Integer32
_IoUnitProgInputValue3_Object = MibTableColumn
ioUnitProgInputValue3 = _IoUnitProgInputValue3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 22),
    _IoUnitProgInputValue3_Type()
)
ioUnitProgInputValue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputValue3.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitProgInputValue3.setUnits("1/100 Volt; i.e. 500 = 5.00V")
_IoUnitProgInputValue4_Type = Integer32
_IoUnitProgInputValue4_Object = MibTableColumn
ioUnitProgInputValue4 = _IoUnitProgInputValue4_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 23),
    _IoUnitProgInputValue4_Type()
)
ioUnitProgInputValue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputValue4.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitProgInputValue4.setUnits("1/100 Volt; i.e. 500 = 5.00V")
_IoUnitProgInputValue5_Type = Integer32
_IoUnitProgInputValue5_Object = MibTableColumn
ioUnitProgInputValue5 = _IoUnitProgInputValue5_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 24),
    _IoUnitProgInputValue5_Type()
)
ioUnitProgInputValue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputValue5.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitProgInputValue5.setUnits("1/100 Volt; i.e. 500 = 5.00V")
_IoUnitProgInputValue6_Type = Integer32
_IoUnitProgInputValue6_Object = MibTableColumn
ioUnitProgInputValue6 = _IoUnitProgInputValue6_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 17, 3, 1, 25),
    _IoUnitProgInputValue6_Type()
)
ioUnitProgInputValue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitProgInputValue6.setStatus("current")
if mibBuilder.loadTexts:
    ioUnitProgInputValue6.setUnits("1/100 Volt; i.e. 500 = 5.00V")


class _SystemServiceMode_Type(Integer32):
    """Custom type systemServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 0))
    )


_SystemServiceMode_Type.__name__ = "Integer32"
_SystemServiceMode_Object = MibScalar
systemServiceMode = _SystemServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 1, 18),
    _SystemServiceMode_Type()
)
systemServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemServiceMode.setStatus("deprecated")
_DcSystem_ObjectIdentity = ObjectIdentity
dcSystem = _DcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2)
)
_DcPlant_ObjectIdentity = ObjectIdentity
dcPlant = _DcPlant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1)
)
_SystemSiteInfo_ObjectIdentity = ObjectIdentity
systemSiteInfo = _SystemSiteInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1, 3)
)


class _SystemSiteInfoCustomer_Type(DisplayString):
    """Custom type systemSiteInfoCustomer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemSiteInfoCustomer_Type.__name__ = "DisplayString"
_SystemSiteInfoCustomer_Object = MibScalar
systemSiteInfoCustomer = _SystemSiteInfoCustomer_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1, 3, 1),
    _SystemSiteInfoCustomer_Type()
)
systemSiteInfoCustomer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoCustomer.setStatus("current")


class _SystemSiteInfoLocation_Type(DisplayString):
    """Custom type systemSiteInfoLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemSiteInfoLocation_Type.__name__ = "DisplayString"
_SystemSiteInfoLocation_Object = MibScalar
systemSiteInfoLocation = _SystemSiteInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1, 3, 2),
    _SystemSiteInfoLocation_Type()
)
systemSiteInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoLocation.setStatus("current")


class _SystemSiteInfoMessage1_Type(DisplayString):
    """Custom type systemSiteInfoMessage1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemSiteInfoMessage1_Type.__name__ = "DisplayString"
_SystemSiteInfoMessage1_Object = MibScalar
systemSiteInfoMessage1 = _SystemSiteInfoMessage1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1, 3, 3),
    _SystemSiteInfoMessage1_Type()
)
systemSiteInfoMessage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoMessage1.setStatus("current")


class _SystemSiteInfoMessage2_Type(DisplayString):
    """Custom type systemSiteInfoMessage2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemSiteInfoMessage2_Type.__name__ = "DisplayString"
_SystemSiteInfoMessage2_Object = MibScalar
systemSiteInfoMessage2 = _SystemSiteInfoMessage2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1, 3, 4),
    _SystemSiteInfoMessage2_Type()
)
systemSiteInfoMessage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoMessage2.setStatus("current")


class _SystemSiteInfoInstalledDate_Type(DisplayString):
    """Custom type systemSiteInfoInstalledDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SystemSiteInfoInstalledDate_Type.__name__ = "DisplayString"
_SystemSiteInfoInstalledDate_Object = MibScalar
systemSiteInfoInstalledDate = _SystemSiteInfoInstalledDate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1, 3, 5),
    _SystemSiteInfoInstalledDate_Type()
)
systemSiteInfoInstalledDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoInstalledDate.setStatus("current")


class _SystemSiteInfoControllerType_Type(Integer32):
    """Custom type systemSiteInfoControllerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("al175", 0),
          ("al175oem", 3),
          ("al4000", 1),
          ("al6000", 2),
          ("compack", 6),
          ("mcu", 4),
          ("smartpack", 5),
          ("smartpack2", 7))
    )


_SystemSiteInfoControllerType_Type.__name__ = "Integer32"
_SystemSiteInfoControllerType_Object = MibScalar
systemSiteInfoControllerType = _SystemSiteInfoControllerType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1, 3, 6),
    _SystemSiteInfoControllerType_Type()
)
systemSiteInfoControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoControllerType.setStatus("current")


class _SystemSiteInfoSystemSeriaNum_Type(DisplayString):
    """Custom type systemSiteInfoSystemSeriaNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SystemSiteInfoSystemSeriaNum_Type.__name__ = "DisplayString"
_SystemSiteInfoSystemSeriaNum_Object = MibScalar
systemSiteInfoSystemSeriaNum = _SystemSiteInfoSystemSeriaNum_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1, 3, 7),
    _SystemSiteInfoSystemSeriaNum_Type()
)
systemSiteInfoSystemSeriaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoSystemSeriaNum.setStatus("current")


class _SystemSiteInfoControllerSeriaNum_Type(DisplayString):
    """Custom type systemSiteInfoControllerSeriaNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SystemSiteInfoControllerSeriaNum_Type.__name__ = "DisplayString"
_SystemSiteInfoControllerSeriaNum_Object = MibScalar
systemSiteInfoControllerSeriaNum = _SystemSiteInfoControllerSeriaNum_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1, 3, 8),
    _SystemSiteInfoControllerSeriaNum_Type()
)
systemSiteInfoControllerSeriaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSiteInfoControllerSeriaNum.setStatus("current")


class _SystemNominalVoltage_Type(Integer32):
    """Custom type systemNominalVoltage based on Integer32"""
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
        *(("prs12v", 2),
          ("prs24v", 1),
          ("prs26v", 3),
          ("prs48v", 0),
          ("prs60v", 4))
    )


_SystemNominalVoltage_Type.__name__ = "Integer32"
_SystemNominalVoltage_Object = MibScalar
systemNominalVoltage = _SystemNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 1, 4),
    _SystemNominalVoltage_Type()
)
systemNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNominalVoltage.setStatus("current")


class _SystemOperationalStatus_Type(Integer32):
    """Custom type systemOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("batteryboost", 2),
          ("batterytest", 3),
          ("floattempcomp", 1),
          ("floatvoltreg", 0))
    )


_SystemOperationalStatus_Type.__name__ = "Integer32"
_SystemOperationalStatus_Object = MibScalar
systemOperationalStatus = _SystemOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 2, 2),
    _SystemOperationalStatus_Type()
)
systemOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOperationalStatus.setStatus("current")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3)
)


class _BatteryName_Type(DisplayString):
    """Custom type batteryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BatteryName_Type.__name__ = "DisplayString"
_BatteryName_Object = MibScalar
batteryName = _BatteryName_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 1),
    _BatteryName_Type()
)
batteryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryName.setStatus("current")


class _BatteryVoltage_Type(Integer32):
    """Custom type batteryVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_BatteryVoltage_Type.__name__ = "Integer32"
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 2),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_BatteryCurrent_Type = Integer32
_BatteryCurrent_Object = MibScalar
batteryCurrent = _BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 3),
    _BatteryCurrent_Type()
)
batteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    batteryCurrent.setUnits("Amperes or DeciAmperes")


class _BatteryTemp_Type(Integer32):
    """Custom type batteryTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_BatteryTemp_Type.__name__ = "Integer32"
_BatteryTemp_Object = MibScalar
batteryTemp = _BatteryTemp_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 4),
    _BatteryTemp_Type()
)
batteryTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemp.setStatus("current")
if mibBuilder.loadTexts:
    batteryTemp.setUnits("Deg. C/F; i.e. 25 = 25 Deg.")


class _BatteryBreakerStatus_Type(Integer32):
    """Custom type batteryBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_BatteryBreakerStatus_Type.__name__ = "Integer32"
_BatteryBreakerStatus_Object = MibScalar
batteryBreakerStatus = _BatteryBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 5),
    _BatteryBreakerStatus_Type()
)
batteryBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBreakerStatus.setStatus("current")


class _BatteryChargeCurrentLimitCtrl_Type(Integer32):
    """Custom type batteryChargeCurrentLimitCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryChargeCurrentLimitCtrl_Type.__name__ = "Integer32"
_BatteryChargeCurrentLimitCtrl_Object = MibScalar
batteryChargeCurrentLimitCtrl = _BatteryChargeCurrentLimitCtrl_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 6),
    _BatteryChargeCurrentLimitCtrl_Type()
)
batteryChargeCurrentLimitCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryChargeCurrentLimitCtrl.setStatus("current")


class _BatteryChargeCurrentLimitValue_Type(Integer32):
    """Custom type batteryChargeCurrentLimitValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BatteryChargeCurrentLimitValue_Type.__name__ = "Integer32"
_BatteryChargeCurrentLimitValue_Object = MibScalar
batteryChargeCurrentLimitValue = _BatteryChargeCurrentLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 7),
    _BatteryChargeCurrentLimitValue_Type()
)
batteryChargeCurrentLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryChargeCurrentLimitValue.setStatus("current")
if mibBuilder.loadTexts:
    batteryChargeCurrentLimitValue.setUnits("Amperes or DeciAmperes")


class _BatteryTempCompEnable_Type(Integer32):
    """Custom type batteryTempCompEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryTempCompEnable_Type.__name__ = "Integer32"
_BatteryTempCompEnable_Object = MibScalar
batteryTempCompEnable = _BatteryTempCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 8),
    _BatteryTempCompEnable_Type()
)
batteryTempCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompEnable.setStatus("current")


class _BatteryFloatVoltConfig_Type(Integer32):
    """Custom type batteryFloatVoltConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4300, 6000),
    )


_BatteryFloatVoltConfig_Type.__name__ = "Integer32"
_BatteryFloatVoltConfig_Object = MibScalar
batteryFloatVoltConfig = _BatteryFloatVoltConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 9),
    _BatteryFloatVoltConfig_Type()
)
batteryFloatVoltConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryFloatVoltConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryFloatVoltConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _BatteryBoostVoltConfig_Type(Integer32):
    """Custom type batteryBoostVoltConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4300, 6000),
    )


_BatteryBoostVoltConfig_Type.__name__ = "Integer32"
_BatteryBoostVoltConfig_Object = MibScalar
batteryBoostVoltConfig = _BatteryBoostVoltConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 10),
    _BatteryBoostVoltConfig_Type()
)
batteryBoostVoltConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBoostVoltConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryBoostVoltConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_BatteryHighMajorAlarmVoltageConfig_Type = Integer32
_BatteryHighMajorAlarmVoltageConfig_Object = MibScalar
batteryHighMajorAlarmVoltageConfig = _BatteryHighMajorAlarmVoltageConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 11),
    _BatteryHighMajorAlarmVoltageConfig_Type()
)
batteryHighMajorAlarmVoltageConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryHighMajorAlarmVoltageConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryHighMajorAlarmVoltageConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_BatteryHighMinorAlarmVoltageConfig_Type = Integer32
_BatteryHighMinorAlarmVoltageConfig_Object = MibScalar
batteryHighMinorAlarmVoltageConfig = _BatteryHighMinorAlarmVoltageConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 12),
    _BatteryHighMinorAlarmVoltageConfig_Type()
)
batteryHighMinorAlarmVoltageConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryHighMinorAlarmVoltageConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryHighMinorAlarmVoltageConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_BatteryLowMajorAlarmVoltageConfig_Type = Integer32
_BatteryLowMajorAlarmVoltageConfig_Object = MibScalar
batteryLowMajorAlarmVoltageConfig = _BatteryLowMajorAlarmVoltageConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 13),
    _BatteryLowMajorAlarmVoltageConfig_Type()
)
batteryLowMajorAlarmVoltageConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLowMajorAlarmVoltageConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryLowMajorAlarmVoltageConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_BatteryLowMinorAlarmVoltageConfig_Type = Integer32
_BatteryLowMinorAlarmVoltageConfig_Object = MibScalar
batteryLowMinorAlarmVoltageConfig = _BatteryLowMinorAlarmVoltageConfig_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 14),
    _BatteryLowMinorAlarmVoltageConfig_Type()
)
batteryLowMinorAlarmVoltageConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLowMinorAlarmVoltageConfig.setStatus("current")
if mibBuilder.loadTexts:
    batteryLowMinorAlarmVoltageConfig.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _BatteryStartManualTest_Type(Integer32):
    """Custom type batteryStartManualTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("starttest", 1),
          ("stoptest", 2))
    )


_BatteryStartManualTest_Type.__name__ = "Integer32"
_BatteryStartManualTest_Object = MibScalar
batteryStartManualTest = _BatteryStartManualTest_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 15),
    _BatteryStartManualTest_Type()
)
batteryStartManualTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryStartManualTest.setStatus("current")


class _BatteryStartManualBoost_Type(Integer32):
    """Custom type batteryStartManualBoost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("startboost", 1),
          ("stopboost", 2))
    )


_BatteryStartManualBoost_Type.__name__ = "Integer32"
_BatteryStartManualBoost_Object = MibScalar
batteryStartManualBoost = _BatteryStartManualBoost_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 16),
    _BatteryStartManualBoost_Type()
)
batteryStartManualBoost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryStartManualBoost.setStatus("current")
_BatteryLVD_ObjectIdentity = ObjectIdentity
batteryLVD = _BatteryLVD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 17)
)


class _BatteryLVDStatus_Type(Integer32):
    """Custom type batteryLVDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 0),
          ("disabled", 2),
          ("disconnected", 1))
    )


_BatteryLVDStatus_Type.__name__ = "Integer32"
_BatteryLVDStatus_Object = MibScalar
batteryLVDStatus = _BatteryLVDStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 17, 1),
    _BatteryLVDStatus_Type()
)
batteryLVDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLVDStatus.setStatus("current")


class _BatteryLVDDisconnectVoltage_Type(Integer32):
    """Custom type batteryLVDDisconnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_BatteryLVDDisconnectVoltage_Type.__name__ = "Integer32"
_BatteryLVDDisconnectVoltage_Object = MibScalar
batteryLVDDisconnectVoltage = _BatteryLVDDisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 17, 2),
    _BatteryLVDDisconnectVoltage_Type()
)
batteryLVDDisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVDDisconnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryLVDDisconnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _BatteryLVDConnectVoltage_Type(Integer32):
    """Custom type batteryLVDConnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_BatteryLVDConnectVoltage_Type.__name__ = "Integer32"
_BatteryLVDConnectVoltage_Object = MibScalar
batteryLVDConnectVoltage = _BatteryLVDConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 17, 3),
    _BatteryLVDConnectVoltage_Type()
)
batteryLVDConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVDConnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryLVDConnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _BatteryBanksNumofBanks_Type(Integer32):
    """Custom type batteryBanksNumofBanks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryBanksNumofBanks_Type.__name__ = "Integer32"
_BatteryBanksNumofBanks_Object = MibScalar
batteryBanksNumofBanks = _BatteryBanksNumofBanks_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 18),
    _BatteryBanksNumofBanks_Type()
)
batteryBanksNumofBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksNumofBanks.setStatus("current")
_BatteryBanks_ObjectIdentity = ObjectIdentity
batteryBanks = _BatteryBanks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19)
)
_BatterySymmetryDeltaLimitVoltage_Type = Integer32
_BatterySymmetryDeltaLimitVoltage_Object = MibScalar
batterySymmetryDeltaLimitVoltage = _BatterySymmetryDeltaLimitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 1),
    _BatterySymmetryDeltaLimitVoltage_Type()
)
batterySymmetryDeltaLimitVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batterySymmetryDeltaLimitVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batterySymmetryDeltaLimitVoltage.setUnits("1/100 Volt; i.e. 150 = 1.50V")


class _BatteryBanksIndex_Type(Integer32):
    """Custom type batteryBanksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BatteryBanksIndex_Type.__name__ = "Integer32"
_BatteryBanksIndex_Object = MibScalar
batteryBanksIndex = _BatteryBanksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 2),
    _BatteryBanksIndex_Type()
)
batteryBanksIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryBanksIndex.setStatus("current")
_BatteryBanksTable_Object = MibTable
batteryBanksTable = _BatteryBanksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3)
)
if mibBuilder.loadTexts:
    batteryBanksTable.setStatus("current")
_BatteryBanksEntry_Object = MibTableRow
batteryBanksEntry = _BatteryBanksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1)
)
batteryBanksEntry.setIndexNames(
    (0, "ELTEK-DISTRIBUTED-MIB", "batteryBanksIndex"),
)
if mibBuilder.loadTexts:
    batteryBanksEntry.setStatus("current")


class _BatteryBankID_Type(Integer32):
    """Custom type batteryBankID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryBankID_Type.__name__ = "Integer32"
_BatteryBankID_Object = MibTableColumn
batteryBankID = _BatteryBankID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 1),
    _BatteryBankID_Type()
)
batteryBankID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankID.setStatus("current")


class _BatteryBanksSymmetry1enable_Type(Integer32):
    """Custom type batteryBanksSymmetry1enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryBanksSymmetry1enable_Type.__name__ = "Integer32"
_BatteryBanksSymmetry1enable_Object = MibTableColumn
batteryBanksSymmetry1enable = _BatteryBanksSymmetry1enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 2),
    _BatteryBanksSymmetry1enable_Type()
)
batteryBanksSymmetry1enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBanksSymmetry1enable.setStatus("current")


class _BatteryBanksSymmetry1status_Type(Integer32):
    """Custom type batteryBanksSymmetry1status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryBanksSymmetry1status_Type.__name__ = "Integer32"
_BatteryBanksSymmetry1status_Object = MibTableColumn
batteryBanksSymmetry1status = _BatteryBanksSymmetry1status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 3),
    _BatteryBanksSymmetry1status_Type()
)
batteryBanksSymmetry1status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry1status.setStatus("current")
_BatteryBanksSymmetry1deltaVoltage_Type = Integer32
_BatteryBanksSymmetry1deltaVoltage_Object = MibTableColumn
batteryBanksSymmetry1deltaVoltage = _BatteryBanksSymmetry1deltaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 4),
    _BatteryBanksSymmetry1deltaVoltage_Type()
)
batteryBanksSymmetry1deltaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry1deltaVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksSymmetry1deltaVoltage.setUnits("1/100 Volt; i.e. 100 = 1.00V")


class _BatteryBanksSymmetry2enable_Type(Integer32):
    """Custom type batteryBanksSymmetry2enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryBanksSymmetry2enable_Type.__name__ = "Integer32"
_BatteryBanksSymmetry2enable_Object = MibTableColumn
batteryBanksSymmetry2enable = _BatteryBanksSymmetry2enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 5),
    _BatteryBanksSymmetry2enable_Type()
)
batteryBanksSymmetry2enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBanksSymmetry2enable.setStatus("current")


class _BatteryBanksSymmetry2status_Type(Integer32):
    """Custom type batteryBanksSymmetry2status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryBanksSymmetry2status_Type.__name__ = "Integer32"
_BatteryBanksSymmetry2status_Object = MibTableColumn
batteryBanksSymmetry2status = _BatteryBanksSymmetry2status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 6),
    _BatteryBanksSymmetry2status_Type()
)
batteryBanksSymmetry2status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry2status.setStatus("current")
_BatteryBanksSymmetry2deltaVoltage_Type = Integer32
_BatteryBanksSymmetry2deltaVoltage_Object = MibTableColumn
batteryBanksSymmetry2deltaVoltage = _BatteryBanksSymmetry2deltaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 7),
    _BatteryBanksSymmetry2deltaVoltage_Type()
)
batteryBanksSymmetry2deltaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry2deltaVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksSymmetry2deltaVoltage.setUnits("1/100 Volt; i.e. 100 = 1.00V")


class _BatteryBanksSymmetry3enable_Type(Integer32):
    """Custom type batteryBanksSymmetry3enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryBanksSymmetry3enable_Type.__name__ = "Integer32"
_BatteryBanksSymmetry3enable_Object = MibTableColumn
batteryBanksSymmetry3enable = _BatteryBanksSymmetry3enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 8),
    _BatteryBanksSymmetry3enable_Type()
)
batteryBanksSymmetry3enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBanksSymmetry3enable.setStatus("current")


class _BatteryBanksSymmetry3status_Type(Integer32):
    """Custom type batteryBanksSymmetry3status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryBanksSymmetry3status_Type.__name__ = "Integer32"
_BatteryBanksSymmetry3status_Object = MibTableColumn
batteryBanksSymmetry3status = _BatteryBanksSymmetry3status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 9),
    _BatteryBanksSymmetry3status_Type()
)
batteryBanksSymmetry3status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry3status.setStatus("current")
_BatteryBanksSymmetry3deltaVoltage_Type = Integer32
_BatteryBanksSymmetry3deltaVoltage_Object = MibTableColumn
batteryBanksSymmetry3deltaVoltage = _BatteryBanksSymmetry3deltaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 10),
    _BatteryBanksSymmetry3deltaVoltage_Type()
)
batteryBanksSymmetry3deltaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry3deltaVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksSymmetry3deltaVoltage.setUnits("1/100 Volt; i.e. 100 = 1.00V")


class _BatteryBanksSymmetry4enable_Type(Integer32):
    """Custom type batteryBanksSymmetry4enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryBanksSymmetry4enable_Type.__name__ = "Integer32"
_BatteryBanksSymmetry4enable_Object = MibTableColumn
batteryBanksSymmetry4enable = _BatteryBanksSymmetry4enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 11),
    _BatteryBanksSymmetry4enable_Type()
)
batteryBanksSymmetry4enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBanksSymmetry4enable.setStatus("current")


class _BatteryBanksSymmetry4status_Type(Integer32):
    """Custom type batteryBanksSymmetry4status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryBanksSymmetry4status_Type.__name__ = "Integer32"
_BatteryBanksSymmetry4status_Object = MibTableColumn
batteryBanksSymmetry4status = _BatteryBanksSymmetry4status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 12),
    _BatteryBanksSymmetry4status_Type()
)
batteryBanksSymmetry4status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry4status.setStatus("current")
_BatteryBanksSymmetry4deltaVoltage_Type = Integer32
_BatteryBanksSymmetry4deltaVoltage_Object = MibTableColumn
batteryBanksSymmetry4deltaVoltage = _BatteryBanksSymmetry4deltaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 13),
    _BatteryBanksSymmetry4deltaVoltage_Type()
)
batteryBanksSymmetry4deltaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry4deltaVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksSymmetry4deltaVoltage.setUnits("1/100 Volt; i.e. 100 = 1.00V")


class _BatteryBanksSymmetry5enable_Type(Integer32):
    """Custom type batteryBanksSymmetry5enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryBanksSymmetry5enable_Type.__name__ = "Integer32"
_BatteryBanksSymmetry5enable_Object = MibTableColumn
batteryBanksSymmetry5enable = _BatteryBanksSymmetry5enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 14),
    _BatteryBanksSymmetry5enable_Type()
)
batteryBanksSymmetry5enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBanksSymmetry5enable.setStatus("current")


class _BatteryBanksSymmetry5status_Type(Integer32):
    """Custom type batteryBanksSymmetry5status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryBanksSymmetry5status_Type.__name__ = "Integer32"
_BatteryBanksSymmetry5status_Object = MibTableColumn
batteryBanksSymmetry5status = _BatteryBanksSymmetry5status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 15),
    _BatteryBanksSymmetry5status_Type()
)
batteryBanksSymmetry5status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry5status.setStatus("current")
_BatteryBanksSymmetry5deltaVoltage_Type = Integer32
_BatteryBanksSymmetry5deltaVoltage_Object = MibTableColumn
batteryBanksSymmetry5deltaVoltage = _BatteryBanksSymmetry5deltaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 16),
    _BatteryBanksSymmetry5deltaVoltage_Type()
)
batteryBanksSymmetry5deltaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry5deltaVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksSymmetry5deltaVoltage.setUnits("1/100 Volt; i.e. 100 = 1.00V")


class _BatteryBanksSymmetry6enable_Type(Integer32):
    """Custom type batteryBanksSymmetry6enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryBanksSymmetry6enable_Type.__name__ = "Integer32"
_BatteryBanksSymmetry6enable_Object = MibTableColumn
batteryBanksSymmetry6enable = _BatteryBanksSymmetry6enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 17),
    _BatteryBanksSymmetry6enable_Type()
)
batteryBanksSymmetry6enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBanksSymmetry6enable.setStatus("current")


class _BatteryBanksSymmetry6status_Type(Integer32):
    """Custom type batteryBanksSymmetry6status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryBanksSymmetry6status_Type.__name__ = "Integer32"
_BatteryBanksSymmetry6status_Object = MibTableColumn
batteryBanksSymmetry6status = _BatteryBanksSymmetry6status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 18),
    _BatteryBanksSymmetry6status_Type()
)
batteryBanksSymmetry6status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry6status.setStatus("current")
_BatteryBanksSymmetry6deltaVoltage_Type = Integer32
_BatteryBanksSymmetry6deltaVoltage_Object = MibTableColumn
batteryBanksSymmetry6deltaVoltage = _BatteryBanksSymmetry6deltaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 19),
    _BatteryBanksSymmetry6deltaVoltage_Type()
)
batteryBanksSymmetry6deltaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry6deltaVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksSymmetry6deltaVoltage.setUnits("1/100 Volt; i.e. 100 = 1.00V")


class _BatteryBanksSymmetry7enable_Type(Integer32):
    """Custom type batteryBanksSymmetry7enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryBanksSymmetry7enable_Type.__name__ = "Integer32"
_BatteryBanksSymmetry7enable_Object = MibTableColumn
batteryBanksSymmetry7enable = _BatteryBanksSymmetry7enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 20),
    _BatteryBanksSymmetry7enable_Type()
)
batteryBanksSymmetry7enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBanksSymmetry7enable.setStatus("current")


class _BatteryBanksSymmetry7status_Type(Integer32):
    """Custom type batteryBanksSymmetry7status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryBanksSymmetry7status_Type.__name__ = "Integer32"
_BatteryBanksSymmetry7status_Object = MibTableColumn
batteryBanksSymmetry7status = _BatteryBanksSymmetry7status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 21),
    _BatteryBanksSymmetry7status_Type()
)
batteryBanksSymmetry7status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry7status.setStatus("current")
_BatteryBanksSymmetry7deltaVoltage_Type = Integer32
_BatteryBanksSymmetry7deltaVoltage_Object = MibTableColumn
batteryBanksSymmetry7deltaVoltage = _BatteryBanksSymmetry7deltaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 22),
    _BatteryBanksSymmetry7deltaVoltage_Type()
)
batteryBanksSymmetry7deltaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry7deltaVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksSymmetry7deltaVoltage.setUnits("1/100 Volt; i.e. 100 = 1.00V")


class _BatteryBanksSymmetry8enable_Type(Integer32):
    """Custom type batteryBanksSymmetry8enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BatteryBanksSymmetry8enable_Type.__name__ = "Integer32"
_BatteryBanksSymmetry8enable_Object = MibTableColumn
batteryBanksSymmetry8enable = _BatteryBanksSymmetry8enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 23),
    _BatteryBanksSymmetry8enable_Type()
)
batteryBanksSymmetry8enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBanksSymmetry8enable.setStatus("current")


class _BatteryBanksSymmetry8status_Type(Integer32):
    """Custom type batteryBanksSymmetry8status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryBanksSymmetry8status_Type.__name__ = "Integer32"
_BatteryBanksSymmetry8status_Object = MibTableColumn
batteryBanksSymmetry8status = _BatteryBanksSymmetry8status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 24),
    _BatteryBanksSymmetry8status_Type()
)
batteryBanksSymmetry8status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry8status.setStatus("current")
_BatteryBanksSymmetry8deltaVoltage_Type = Integer32
_BatteryBanksSymmetry8deltaVoltage_Object = MibTableColumn
batteryBanksSymmetry8deltaVoltage = _BatteryBanksSymmetry8deltaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 3, 1, 25),
    _BatteryBanksSymmetry8deltaVoltage_Type()
)
batteryBanksSymmetry8deltaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksSymmetry8deltaVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksSymmetry8deltaVoltage.setUnits("1/100 Volt; i.e. 100 = 1.00V")
_BatteryBanksNumberOfStrings_Type = Integer32
_BatteryBanksNumberOfStrings_Object = MibScalar
batteryBanksNumberOfStrings = _BatteryBanksNumberOfStrings_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 4),
    _BatteryBanksNumberOfStrings_Type()
)
batteryBanksNumberOfStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksNumberOfStrings.setStatus("current")


class _BatteryBanksExtensionIndex_Type(Integer32):
    """Custom type batteryBanksExtensionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BatteryBanksExtensionIndex_Type.__name__ = "Integer32"
_BatteryBanksExtensionIndex_Object = MibScalar
batteryBanksExtensionIndex = _BatteryBanksExtensionIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 5),
    _BatteryBanksExtensionIndex_Type()
)
batteryBanksExtensionIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryBanksExtensionIndex.setStatus("current")
_BatteryBanksExtensionTable_Object = MibTable
batteryBanksExtensionTable = _BatteryBanksExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6)
)
if mibBuilder.loadTexts:
    batteryBanksExtensionTable.setStatus("current")
_BatteryBanksExtensionEntry_Object = MibTableRow
batteryBanksExtensionEntry = _BatteryBanksExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6, 1)
)
batteryBanksExtensionEntry.setIndexNames(
    (0, "ELTEK-DISTRIBUTED-MIB", "batteryBanksExtensionIndex"),
)
if mibBuilder.loadTexts:
    batteryBanksExtensionEntry.setStatus("current")
_BatteryBanksExtensionID_Type = Integer32
_BatteryBanksExtensionID_Object = MibTableColumn
batteryBanksExtensionID = _BatteryBanksExtensionID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6, 1, 1),
    _BatteryBanksExtensionID_Type()
)
batteryBanksExtensionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksExtensionID.setStatus("current")
_BatteryBanksExtensionSymmetryInputValue1_Type = Integer32
_BatteryBanksExtensionSymmetryInputValue1_Object = MibTableColumn
batteryBanksExtensionSymmetryInputValue1 = _BatteryBanksExtensionSymmetryInputValue1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6, 1, 2),
    _BatteryBanksExtensionSymmetryInputValue1_Type()
)
batteryBanksExtensionSymmetryInputValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue1.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue1.setUnits("1/100 Volt; i.e. 1200 = 12.00V")
_BatteryBanksExtensionSymmetryInputValue2_Type = Integer32
_BatteryBanksExtensionSymmetryInputValue2_Object = MibTableColumn
batteryBanksExtensionSymmetryInputValue2 = _BatteryBanksExtensionSymmetryInputValue2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6, 1, 3),
    _BatteryBanksExtensionSymmetryInputValue2_Type()
)
batteryBanksExtensionSymmetryInputValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue2.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue2.setUnits("1/100 Volt; i.e. 1200 = 12.00V")
_BatteryBanksExtensionSymmetryInputValue3_Type = Integer32
_BatteryBanksExtensionSymmetryInputValue3_Object = MibTableColumn
batteryBanksExtensionSymmetryInputValue3 = _BatteryBanksExtensionSymmetryInputValue3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6, 1, 4),
    _BatteryBanksExtensionSymmetryInputValue3_Type()
)
batteryBanksExtensionSymmetryInputValue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue3.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue3.setUnits("1/100 Volt; i.e. 1200 = 12.00V")
_BatteryBanksExtensionSymmetryInputValue4_Type = Integer32
_BatteryBanksExtensionSymmetryInputValue4_Object = MibTableColumn
batteryBanksExtensionSymmetryInputValue4 = _BatteryBanksExtensionSymmetryInputValue4_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6, 1, 5),
    _BatteryBanksExtensionSymmetryInputValue4_Type()
)
batteryBanksExtensionSymmetryInputValue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue4.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue4.setUnits("1/100 Volt; i.e. 1200 = 12.00V")
_BatteryBanksExtensionSymmetryInputValue5_Type = Integer32
_BatteryBanksExtensionSymmetryInputValue5_Object = MibTableColumn
batteryBanksExtensionSymmetryInputValue5 = _BatteryBanksExtensionSymmetryInputValue5_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6, 1, 6),
    _BatteryBanksExtensionSymmetryInputValue5_Type()
)
batteryBanksExtensionSymmetryInputValue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue5.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue5.setUnits("1/100 Volt; i.e. 1200 = 12.00V")
_BatteryBanksExtensionSymmetryInputValue6_Type = Integer32
_BatteryBanksExtensionSymmetryInputValue6_Object = MibTableColumn
batteryBanksExtensionSymmetryInputValue6 = _BatteryBanksExtensionSymmetryInputValue6_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6, 1, 7),
    _BatteryBanksExtensionSymmetryInputValue6_Type()
)
batteryBanksExtensionSymmetryInputValue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue6.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue6.setUnits("1/100 Volt; i.e. 1200 = 12.00V")
_BatteryBanksExtensionSymmetryInputValue7_Type = Integer32
_BatteryBanksExtensionSymmetryInputValue7_Object = MibTableColumn
batteryBanksExtensionSymmetryInputValue7 = _BatteryBanksExtensionSymmetryInputValue7_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6, 1, 8),
    _BatteryBanksExtensionSymmetryInputValue7_Type()
)
batteryBanksExtensionSymmetryInputValue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue7.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue7.setUnits("1/100 Volt; i.e. 1200 = 12.00V")
_BatteryBanksExtensionSymmetryInputValue8_Type = Integer32
_BatteryBanksExtensionSymmetryInputValue8_Object = MibTableColumn
batteryBanksExtensionSymmetryInputValue8 = _BatteryBanksExtensionSymmetryInputValue8_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 19, 6, 1, 9),
    _BatteryBanksExtensionSymmetryInputValue8_Type()
)
batteryBanksExtensionSymmetryInputValue8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue8.setStatus("current")
if mibBuilder.loadTexts:
    batteryBanksExtensionSymmetryInputValue8.setUnits("1/100 Volt; i.e. 1200 = 12.00V")
_BatteryCapacityData_ObjectIdentity = ObjectIdentity
batteryCapacityData = _BatteryCapacityData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 20)
)
_BatteryTimeToDisconnect_Type = Integer32
_BatteryTimeToDisconnect_Object = MibScalar
batteryTimeToDisconnect = _BatteryTimeToDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 20, 1),
    _BatteryTimeToDisconnect_Type()
)
batteryTimeToDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTimeToDisconnect.setStatus("current")
if mibBuilder.loadTexts:
    batteryTimeToDisconnect.setUnits("Minutes; 40 = 40 minutes")
_BatteryCapacityLeft_Type = Integer32
_BatteryCapacityLeft_Object = MibScalar
batteryCapacityLeft = _BatteryCapacityLeft_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 20, 2),
    _BatteryCapacityLeft_Type()
)
batteryCapacityLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCapacityLeft.setStatus("current")
if mibBuilder.loadTexts:
    batteryCapacityLeft.setUnits("Ah/%; 23 = 23 Ah or in %")
_BatteryCapacityUsed_Type = Integer32
_BatteryCapacityUsed_Object = MibScalar
batteryCapacityUsed = _BatteryCapacityUsed_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 20, 3),
    _BatteryCapacityUsed_Type()
)
batteryCapacityUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCapacityUsed.setStatus("current")
if mibBuilder.loadTexts:
    batteryCapacityUsed.setUnits("Ah/%; 23 = 23 Ah or in %")
_BatteryCapacityTotal_Type = Integer32
_BatteryCapacityTotal_Object = MibScalar
batteryCapacityTotal = _BatteryCapacityTotal_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 20, 4),
    _BatteryCapacityTotal_Type()
)
batteryCapacityTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCapacityTotal.setStatus("current")
if mibBuilder.loadTexts:
    batteryCapacityTotal.setUnits("Ah/%; 23 = 23 Ah or in %")
_BatteryQuality_Type = Integer32
_BatteryQuality_Object = MibScalar
batteryQuality = _BatteryQuality_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 20, 5),
    _BatteryQuality_Type()
)
batteryQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryQuality.setStatus("current")
if mibBuilder.loadTexts:
    batteryQuality.setUnits("%")
_BatteryMonitorUnits_ObjectIdentity = ObjectIdentity
batteryMonitorUnits = _BatteryMonitorUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21)
)
_BattmonNumberOfUnits_Type = Integer32
_BattmonNumberOfUnits_Object = MibScalar
battmonNumberOfUnits = _BattmonNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 1),
    _BattmonNumberOfUnits_Type()
)
battmonNumberOfUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battmonNumberOfUnits.setStatus("current")
_BattmonUnitsIndex_Type = Integer32
_BattmonUnitsIndex_Object = MibScalar
battmonUnitsIndex = _BattmonUnitsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 2),
    _BattmonUnitsIndex_Type()
)
battmonUnitsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    battmonUnitsIndex.setStatus("current")
_BattmonUnitsTable_Object = MibTable
battmonUnitsTable = _BattmonUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3)
)
if mibBuilder.loadTexts:
    battmonUnitsTable.setStatus("current")
_BattmonUnitsEntry_Object = MibTableRow
battmonUnitsEntry = _BattmonUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1)
)
battmonUnitsEntry.setIndexNames(
    (0, "ELTEK-DISTRIBUTED-MIB", "batteryBanksIndex"),
)
if mibBuilder.loadTexts:
    battmonUnitsEntry.setStatus("current")


class _BatteryMonitorID_Type(Integer32):
    """Custom type batteryMonitorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_BatteryMonitorID_Type.__name__ = "Integer32"
_BatteryMonitorID_Object = MibTableColumn
batteryMonitorID = _BatteryMonitorID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 1),
    _BatteryMonitorID_Type()
)
batteryMonitorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorID.setStatus("current")


class _BatteryMonitorSymmetry1status_Type(Integer32):
    """Custom type batteryMonitorSymmetry1status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryMonitorSymmetry1status_Type.__name__ = "Integer32"
_BatteryMonitorSymmetry1status_Object = MibTableColumn
batteryMonitorSymmetry1status = _BatteryMonitorSymmetry1status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 2),
    _BatteryMonitorSymmetry1status_Type()
)
batteryMonitorSymmetry1status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry1status.setStatus("current")
_BatteryMonitorSymmetry1InputValue_Type = Integer32
_BatteryMonitorSymmetry1InputValue_Object = MibTableColumn
batteryMonitorSymmetry1InputValue = _BatteryMonitorSymmetry1InputValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 3),
    _BatteryMonitorSymmetry1InputValue_Type()
)
batteryMonitorSymmetry1InputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry1InputValue.setStatus("current")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry1InputValue.setUnits("1/100 Volt; i.e. 1200 = 12.00V")


class _BatteryMonitorSymmetry2status_Type(Integer32):
    """Custom type batteryMonitorSymmetry2status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryMonitorSymmetry2status_Type.__name__ = "Integer32"
_BatteryMonitorSymmetry2status_Object = MibTableColumn
batteryMonitorSymmetry2status = _BatteryMonitorSymmetry2status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 4),
    _BatteryMonitorSymmetry2status_Type()
)
batteryMonitorSymmetry2status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry2status.setStatus("current")
_BatteryMonitorSymmetry2InputValue_Type = Integer32
_BatteryMonitorSymmetry2InputValue_Object = MibTableColumn
batteryMonitorSymmetry2InputValue = _BatteryMonitorSymmetry2InputValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 5),
    _BatteryMonitorSymmetry2InputValue_Type()
)
batteryMonitorSymmetry2InputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry2InputValue.setStatus("current")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry2InputValue.setUnits("1/100 Volt; i.e. 1200 = 12.00V")


class _BatteryMonitorSymmetry3status_Type(Integer32):
    """Custom type batteryMonitorSymmetry3status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryMonitorSymmetry3status_Type.__name__ = "Integer32"
_BatteryMonitorSymmetry3status_Object = MibTableColumn
batteryMonitorSymmetry3status = _BatteryMonitorSymmetry3status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 6),
    _BatteryMonitorSymmetry3status_Type()
)
batteryMonitorSymmetry3status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry3status.setStatus("current")
_BatteryMonitorSymmetry3InputValue_Type = Integer32
_BatteryMonitorSymmetry3InputValue_Object = MibTableColumn
batteryMonitorSymmetry3InputValue = _BatteryMonitorSymmetry3InputValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 7),
    _BatteryMonitorSymmetry3InputValue_Type()
)
batteryMonitorSymmetry3InputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry3InputValue.setStatus("current")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry3InputValue.setUnits("1/100 Volt; i.e. 1200 = 12.00V")


class _BatteryMonitorSymmetry4status_Type(Integer32):
    """Custom type batteryMonitorSymmetry4status based on Integer32"""
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
        *(("disabled", 3),
          ("error", 4),
          ("majorAlarm", 2),
          ("minorAlarm", 1),
          ("ok", 0))
    )


_BatteryMonitorSymmetry4status_Type.__name__ = "Integer32"
_BatteryMonitorSymmetry4status_Object = MibTableColumn
batteryMonitorSymmetry4status = _BatteryMonitorSymmetry4status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 8),
    _BatteryMonitorSymmetry4status_Type()
)
batteryMonitorSymmetry4status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry4status.setStatus("current")
_BatteryMonitorSymmetry4InputValue_Type = Integer32
_BatteryMonitorSymmetry4InputValue_Object = MibTableColumn
batteryMonitorSymmetry4InputValue = _BatteryMonitorSymmetry4InputValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 9),
    _BatteryMonitorSymmetry4InputValue_Type()
)
batteryMonitorSymmetry4InputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry4InputValue.setStatus("current")
if mibBuilder.loadTexts:
    batteryMonitorSymmetry4InputValue.setUnits("1/100 Volt; i.e. 1200 = 12.00V")
_BatteryMonitorCurrentValue_Type = Integer32
_BatteryMonitorCurrentValue_Object = MibTableColumn
batteryMonitorCurrentValue = _BatteryMonitorCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 10),
    _BatteryMonitorCurrentValue_Type()
)
batteryMonitorCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorCurrentValue.setStatus("current")
if mibBuilder.loadTexts:
    batteryMonitorCurrentValue.setUnits("Amperes or DeciAmperes")


class _BatteryMonitorFuseStatus_Type(Integer32):
    """Custom type batteryMonitorFuseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_BatteryMonitorFuseStatus_Type.__name__ = "Integer32"
_BatteryMonitorFuseStatus_Object = MibTableColumn
batteryMonitorFuseStatus = _BatteryMonitorFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 11),
    _BatteryMonitorFuseStatus_Type()
)
batteryMonitorFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorFuseStatus.setStatus("current")
_BatteryMonitorTemperature_Type = Integer32
_BatteryMonitorTemperature_Object = MibTableColumn
batteryMonitorTemperature = _BatteryMonitorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 21, 3, 1, 12),
    _BatteryMonitorTemperature_Type()
)
batteryMonitorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryMonitorTemperature.setUnits("Deg. C/F; i.e. 25 = 25 Deg.")
_BatteryHighMajorTempAlarmLevel_Type = Integer32
_BatteryHighMajorTempAlarmLevel_Object = MibScalar
batteryHighMajorTempAlarmLevel = _BatteryHighMajorTempAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 22),
    _BatteryHighMajorTempAlarmLevel_Type()
)
batteryHighMajorTempAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryHighMajorTempAlarmLevel.setStatus("current")
if mibBuilder.loadTexts:
    batteryHighMajorTempAlarmLevel.setUnits("Deg. C/F; i.e. 25 = 25 Deg.")
_BatteryHighMinorTempAlarmLevel_Type = Integer32
_BatteryHighMinorTempAlarmLevel_Object = MibScalar
batteryHighMinorTempAlarmLevel = _BatteryHighMinorTempAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 3, 23),
    _BatteryHighMinorTempAlarmLevel_Type()
)
batteryHighMinorTempAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryHighMinorTempAlarmLevel.setStatus("current")
if mibBuilder.loadTexts:
    batteryHighMinorTempAlarmLevel.setUnits("Deg. C/F; i.e. 25 = 25 Deg.")
_LoadDistribution_ObjectIdentity = ObjectIdentity
loadDistribution = _LoadDistribution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4)
)
_LoadDistributionCurrent_Type = Integer32
_LoadDistributionCurrent_Object = MibScalar
loadDistributionCurrent = _LoadDistributionCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 1),
    _LoadDistributionCurrent_Type()
)
loadDistributionCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadDistributionCurrent.setStatus("current")
if mibBuilder.loadTexts:
    loadDistributionCurrent.setUnits("Amperes or DeciAmperes")


class _LoadDistributionBreakerStatus_Type(Integer32):
    """Custom type loadDistributionBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_LoadDistributionBreakerStatus_Type.__name__ = "Integer32"
_LoadDistributionBreakerStatus_Object = MibScalar
loadDistributionBreakerStatus = _LoadDistributionBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 2),
    _LoadDistributionBreakerStatus_Type()
)
loadDistributionBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadDistributionBreakerStatus.setStatus("current")
_LoadDistributionLVDStatus_ObjectIdentity = ObjectIdentity
loadDistributionLVDStatus = _LoadDistributionLVDStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3)
)


class _LoadLVD1Enable_Type(Integer32):
    """Custom type loadLVD1Enable based on Integer32"""
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


_LoadLVD1Enable_Type.__name__ = "Integer32"
_LoadLVD1Enable_Object = MibScalar
loadLVD1Enable = _LoadLVD1Enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 1),
    _LoadLVD1Enable_Type()
)
loadLVD1Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD1Enable.setStatus("current")


class _LoadLVD1Status_Type(Integer32):
    """Custom type loadLVD1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 0),
          ("disabled", 2),
          ("disconnected", 1))
    )


_LoadLVD1Status_Type.__name__ = "Integer32"
_LoadLVD1Status_Object = MibScalar
loadLVD1Status = _LoadLVD1Status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 2),
    _LoadLVD1Status_Type()
)
loadLVD1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD1Status.setStatus("current")


class _LoadLVD1ConnectVoltage_Type(Integer32):
    """Custom type loadLVD1ConnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD1ConnectVoltage_Type.__name__ = "Integer32"
_LoadLVD1ConnectVoltage_Object = MibScalar
loadLVD1ConnectVoltage = _LoadLVD1ConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 3),
    _LoadLVD1ConnectVoltage_Type()
)
loadLVD1ConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD1ConnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD1ConnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _LoadLVD1DisconnectVoltage_Type(Integer32):
    """Custom type loadLVD1DisconnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD1DisconnectVoltage_Type.__name__ = "Integer32"
_LoadLVD1DisconnectVoltage_Object = MibScalar
loadLVD1DisconnectVoltage = _LoadLVD1DisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 4),
    _LoadLVD1DisconnectVoltage_Type()
)
loadLVD1DisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD1DisconnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD1DisconnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _LoadLVD2Enable_Type(Integer32):
    """Custom type loadLVD2Enable based on Integer32"""
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


_LoadLVD2Enable_Type.__name__ = "Integer32"
_LoadLVD2Enable_Object = MibScalar
loadLVD2Enable = _LoadLVD2Enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 5),
    _LoadLVD2Enable_Type()
)
loadLVD2Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD2Enable.setStatus("current")


class _LoadLVD2Status_Type(Integer32):
    """Custom type loadLVD2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 0),
          ("disabled", 2),
          ("disconnected", 1))
    )


_LoadLVD2Status_Type.__name__ = "Integer32"
_LoadLVD2Status_Object = MibScalar
loadLVD2Status = _LoadLVD2Status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 6),
    _LoadLVD2Status_Type()
)
loadLVD2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD2Status.setStatus("current")


class _LoadLVD2ConnectVoltage_Type(Integer32):
    """Custom type loadLVD2ConnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD2ConnectVoltage_Type.__name__ = "Integer32"
_LoadLVD2ConnectVoltage_Object = MibScalar
loadLVD2ConnectVoltage = _LoadLVD2ConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 7),
    _LoadLVD2ConnectVoltage_Type()
)
loadLVD2ConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD2ConnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD2ConnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _LoadLVD2DisconnectVoltage_Type(Integer32):
    """Custom type loadLVD2DisconnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD2DisconnectVoltage_Type.__name__ = "Integer32"
_LoadLVD2DisconnectVoltage_Object = MibScalar
loadLVD2DisconnectVoltage = _LoadLVD2DisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 8),
    _LoadLVD2DisconnectVoltage_Type()
)
loadLVD2DisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD2DisconnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD2DisconnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _LoadLVD3Enable_Type(Integer32):
    """Custom type loadLVD3Enable based on Integer32"""
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


_LoadLVD3Enable_Type.__name__ = "Integer32"
_LoadLVD3Enable_Object = MibScalar
loadLVD3Enable = _LoadLVD3Enable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 9),
    _LoadLVD3Enable_Type()
)
loadLVD3Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD3Enable.setStatus("current")


class _LoadLVD3Status_Type(Integer32):
    """Custom type loadLVD3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 0),
          ("disabled", 2),
          ("disconnected", 1))
    )


_LoadLVD3Status_Type.__name__ = "Integer32"
_LoadLVD3Status_Object = MibScalar
loadLVD3Status = _LoadLVD3Status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 10),
    _LoadLVD3Status_Type()
)
loadLVD3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVD3Status.setStatus("current")


class _LoadLVD3ConnectVoltage_Type(Integer32):
    """Custom type loadLVD3ConnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD3ConnectVoltage_Type.__name__ = "Integer32"
_LoadLVD3ConnectVoltage_Object = MibScalar
loadLVD3ConnectVoltage = _LoadLVD3ConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 11),
    _LoadLVD3ConnectVoltage_Type()
)
loadLVD3ConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD3ConnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD3ConnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _LoadLVD3DisconnectVoltage_Type(Integer32):
    """Custom type loadLVD3DisconnectVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_LoadLVD3DisconnectVoltage_Type.__name__ = "Integer32"
_LoadLVD3DisconnectVoltage_Object = MibScalar
loadLVD3DisconnectVoltage = _LoadLVD3DisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 3, 12),
    _LoadLVD3DisconnectVoltage_Type()
)
loadLVD3DisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVD3DisconnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    loadLVD3DisconnectVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")
_LoadMonitorUnits_ObjectIdentity = ObjectIdentity
loadMonitorUnits = _LoadMonitorUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4)
)
_LoadmonitorNumberOfUnits_Type = Integer32
_LoadmonitorNumberOfUnits_Object = MibScalar
loadmonitorNumberOfUnits = _LoadmonitorNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 1),
    _LoadmonitorNumberOfUnits_Type()
)
loadmonitorNumberOfUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadmonitorNumberOfUnits.setStatus("current")


class _LoadMonitorUnitsIndex_Type(Integer32):
    """Custom type loadMonitorUnitsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_LoadMonitorUnitsIndex_Type.__name__ = "Integer32"
_LoadMonitorUnitsIndex_Object = MibScalar
loadMonitorUnitsIndex = _LoadMonitorUnitsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 2),
    _LoadMonitorUnitsIndex_Type()
)
loadMonitorUnitsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loadMonitorUnitsIndex.setStatus("current")
_LoadMonitorUnitsTable_Object = MibTable
loadMonitorUnitsTable = _LoadMonitorUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3)
)
if mibBuilder.loadTexts:
    loadMonitorUnitsTable.setStatus("current")
_LoadMonitorUnitsEntry_Object = MibTableRow
loadMonitorUnitsEntry = _LoadMonitorUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1)
)
loadMonitorUnitsEntry.setIndexNames(
    (0, "ELTEK-DISTRIBUTED-MIB", "loadMonitorUnitsIndex"),
)
if mibBuilder.loadTexts:
    loadMonitorUnitsEntry.setStatus("current")
_LoadMonitorID_Type = Integer32
_LoadMonitorID_Object = MibTableColumn
loadMonitorID = _LoadMonitorID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 1),
    _LoadMonitorID_Type()
)
loadMonitorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorID.setStatus("current")


class _LoadMonitorFuseStatus1_Type(Integer32):
    """Custom type loadMonitorFuseStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_LoadMonitorFuseStatus1_Type.__name__ = "Integer32"
_LoadMonitorFuseStatus1_Object = MibTableColumn
loadMonitorFuseStatus1 = _LoadMonitorFuseStatus1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 2),
    _LoadMonitorFuseStatus1_Type()
)
loadMonitorFuseStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorFuseStatus1.setStatus("current")
_LoadMonitorCurrent1_Type = Integer32
_LoadMonitorCurrent1_Object = MibTableColumn
loadMonitorCurrent1 = _LoadMonitorCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 3),
    _LoadMonitorCurrent1_Type()
)
loadMonitorCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorCurrent1.setStatus("current")
if mibBuilder.loadTexts:
    loadMonitorCurrent1.setUnits("Amperes or DeciAmperes")


class _LoadMonitorFuseStatus2_Type(Integer32):
    """Custom type loadMonitorFuseStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_LoadMonitorFuseStatus2_Type.__name__ = "Integer32"
_LoadMonitorFuseStatus2_Object = MibTableColumn
loadMonitorFuseStatus2 = _LoadMonitorFuseStatus2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 4),
    _LoadMonitorFuseStatus2_Type()
)
loadMonitorFuseStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorFuseStatus2.setStatus("current")
_LoadMonitorCurrent2_Type = Integer32
_LoadMonitorCurrent2_Object = MibTableColumn
loadMonitorCurrent2 = _LoadMonitorCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 5),
    _LoadMonitorCurrent2_Type()
)
loadMonitorCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorCurrent2.setStatus("current")
if mibBuilder.loadTexts:
    loadMonitorCurrent2.setUnits("Amperes or DeciAmperes")


class _LoadMonitorFuseStatus3_Type(Integer32):
    """Custom type loadMonitorFuseStatus3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_LoadMonitorFuseStatus3_Type.__name__ = "Integer32"
_LoadMonitorFuseStatus3_Object = MibTableColumn
loadMonitorFuseStatus3 = _LoadMonitorFuseStatus3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 6),
    _LoadMonitorFuseStatus3_Type()
)
loadMonitorFuseStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorFuseStatus3.setStatus("current")
_LoadMonitorCurrent3_Type = Integer32
_LoadMonitorCurrent3_Object = MibTableColumn
loadMonitorCurrent3 = _LoadMonitorCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 7),
    _LoadMonitorCurrent3_Type()
)
loadMonitorCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorCurrent3.setStatus("current")
if mibBuilder.loadTexts:
    loadMonitorCurrent3.setUnits("Amperes or DeciAmperes")


class _LoadMonitorFuseStatus4_Type(Integer32):
    """Custom type loadMonitorFuseStatus4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_LoadMonitorFuseStatus4_Type.__name__ = "Integer32"
_LoadMonitorFuseStatus4_Object = MibTableColumn
loadMonitorFuseStatus4 = _LoadMonitorFuseStatus4_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 8),
    _LoadMonitorFuseStatus4_Type()
)
loadMonitorFuseStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorFuseStatus4.setStatus("current")
_LoadMonitorCurrent4_Type = Integer32
_LoadMonitorCurrent4_Object = MibTableColumn
loadMonitorCurrent4 = _LoadMonitorCurrent4_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 9),
    _LoadMonitorCurrent4_Type()
)
loadMonitorCurrent4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorCurrent4.setStatus("current")
if mibBuilder.loadTexts:
    loadMonitorCurrent4.setUnits("Amperes or DeciAmperes")


class _LoadMonitorFuseStatus5_Type(Integer32):
    """Custom type loadMonitorFuseStatus5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_LoadMonitorFuseStatus5_Type.__name__ = "Integer32"
_LoadMonitorFuseStatus5_Object = MibTableColumn
loadMonitorFuseStatus5 = _LoadMonitorFuseStatus5_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 10),
    _LoadMonitorFuseStatus5_Type()
)
loadMonitorFuseStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorFuseStatus5.setStatus("current")
_LoadMonitorCurrent5_Type = Integer32
_LoadMonitorCurrent5_Object = MibTableColumn
loadMonitorCurrent5 = _LoadMonitorCurrent5_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 11),
    _LoadMonitorCurrent5_Type()
)
loadMonitorCurrent5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorCurrent5.setStatus("current")
if mibBuilder.loadTexts:
    loadMonitorCurrent5.setUnits("Amperes or DeciAmperes")


class _LoadMonitorFuseStatus6_Type(Integer32):
    """Custom type loadMonitorFuseStatus6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_LoadMonitorFuseStatus6_Type.__name__ = "Integer32"
_LoadMonitorFuseStatus6_Object = MibTableColumn
loadMonitorFuseStatus6 = _LoadMonitorFuseStatus6_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 12),
    _LoadMonitorFuseStatus6_Type()
)
loadMonitorFuseStatus6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorFuseStatus6.setStatus("current")
_LoadMonitorCurrent6_Type = Integer32
_LoadMonitorCurrent6_Object = MibTableColumn
loadMonitorCurrent6 = _LoadMonitorCurrent6_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 13),
    _LoadMonitorCurrent6_Type()
)
loadMonitorCurrent6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorCurrent6.setStatus("current")
if mibBuilder.loadTexts:
    loadMonitorCurrent6.setUnits("Amperes or DeciAmperes")


class _LoadMonitorFuseStatus7_Type(Integer32):
    """Custom type loadMonitorFuseStatus7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_LoadMonitorFuseStatus7_Type.__name__ = "Integer32"
_LoadMonitorFuseStatus7_Object = MibTableColumn
loadMonitorFuseStatus7 = _LoadMonitorFuseStatus7_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 14),
    _LoadMonitorFuseStatus7_Type()
)
loadMonitorFuseStatus7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorFuseStatus7.setStatus("current")
_LoadMonitorCurrent7_Type = Integer32
_LoadMonitorCurrent7_Object = MibTableColumn
loadMonitorCurrent7 = _LoadMonitorCurrent7_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 15),
    _LoadMonitorCurrent7_Type()
)
loadMonitorCurrent7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorCurrent7.setStatus("current")
if mibBuilder.loadTexts:
    loadMonitorCurrent7.setUnits("Amperes or DeciAmperes")


class _LoadMonitorFuseStatus8_Type(Integer32):
    """Custom type loadMonitorFuseStatus8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_LoadMonitorFuseStatus8_Type.__name__ = "Integer32"
_LoadMonitorFuseStatus8_Object = MibTableColumn
loadMonitorFuseStatus8 = _LoadMonitorFuseStatus8_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 16),
    _LoadMonitorFuseStatus8_Type()
)
loadMonitorFuseStatus8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorFuseStatus8.setStatus("current")
_LoadMonitorCurrent8_Type = Integer32
_LoadMonitorCurrent8_Object = MibTableColumn
loadMonitorCurrent8 = _LoadMonitorCurrent8_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 4, 4, 3, 1, 17),
    _LoadMonitorCurrent8_Type()
)
loadMonitorCurrent8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorCurrent8.setStatus("current")
if mibBuilder.loadTexts:
    loadMonitorCurrent8.setUnits("Amperes or DeciAmperes")
_Rectifier_ObjectIdentity = ObjectIdentity
rectifier = _Rectifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5)
)


class _RectifierInstalledRectifiers_Type(Integer32):
    """Custom type rectifierInstalledRectifiers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 101),
    )


_RectifierInstalledRectifiers_Type.__name__ = "Integer32"
_RectifierInstalledRectifiers_Object = MibScalar
rectifierInstalledRectifiers = _RectifierInstalledRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 1),
    _RectifierInstalledRectifiers_Type()
)
rectifierInstalledRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierInstalledRectifiers.setStatus("current")


class _RectifierRectifiersActive_Type(Integer32):
    """Custom type rectifierRectifiersActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 101),
    )


_RectifierRectifiersActive_Type.__name__ = "Integer32"
_RectifierRectifiersActive_Object = MibScalar
rectifierRectifiersActive = _RectifierRectifiersActive_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 2),
    _RectifierRectifiersActive_Type()
)
rectifierRectifiersActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierRectifiersActive.setStatus("current")
_RectifierTotalCurrent_Type = Integer32
_RectifierTotalCurrent_Object = MibScalar
rectifierTotalCurrent = _RectifierTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 3),
    _RectifierTotalCurrent_Type()
)
rectifierTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rectifierTotalCurrent.setUnits("DeciAmperes; i.e. 20 = 2,0 Amperes")


class _RectifierUtilization_Type(Integer32):
    """Custom type rectifierUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RectifierUtilization_Type.__name__ = "Integer32"
_RectifierUtilization_Object = MibScalar
rectifierUtilization = _RectifierUtilization_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 4),
    _RectifierUtilization_Type()
)
rectifierUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierUtilization.setStatus("current")
if mibBuilder.loadTexts:
    rectifierUtilization.setUnits("%")
_RectifierStatus_ObjectIdentity = ObjectIdentity
rectifierStatus = _RectifierStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5)
)


class _RectifierStatusNoIndex_Type(Integer32):
    """Custom type rectifierStatusNoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 95),
    )


_RectifierStatusNoIndex_Type.__name__ = "Integer32"
_RectifierStatusNoIndex_Object = MibScalar
rectifierStatusNoIndex = _RectifierStatusNoIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 1),
    _RectifierStatusNoIndex_Type()
)
rectifierStatusNoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierStatusNoIndex.setStatus("current")
_RectifierStatusTable_Object = MibTable
rectifierStatusTable = _RectifierStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2)
)
if mibBuilder.loadTexts:
    rectifierStatusTable.setStatus("current")
_RectifierStatusEntry_Object = MibTableRow
rectifierStatusEntry = _RectifierStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2, 1)
)
rectifierStatusEntry.setIndexNames(
    (0, "ELTEK-DISTRIBUTED-MIB", "rectifierStatusID"),
)
if mibBuilder.loadTexts:
    rectifierStatusEntry.setStatus("current")


class _RectifierStatusID_Type(Integer32):
    """Custom type rectifierStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RectifierStatusID_Type.__name__ = "Integer32"
_RectifierStatusID_Object = MibTableColumn
rectifierStatusID = _RectifierStatusID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2, 1, 1),
    _RectifierStatusID_Type()
)
rectifierStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusID.setStatus("current")


class _RectifierStatusStatus_Type(Integer32):
    """Custom type rectifierStatusStatus based on Integer32"""
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
        *(("alarm", 2),
          ("disabled", 4),
          ("normal", 1),
          ("notPresent", 0),
          ("notUsed", 3))
    )


_RectifierStatusStatus_Type.__name__ = "Integer32"
_RectifierStatusStatus_Object = MibTableColumn
rectifierStatusStatus = _RectifierStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2, 1, 2),
    _RectifierStatusStatus_Type()
)
rectifierStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusStatus.setStatus("current")


class _RectifierStatusOutputCurrent_Type(Integer32):
    """Custom type rectifierStatusOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RectifierStatusOutputCurrent_Type.__name__ = "Integer32"
_RectifierStatusOutputCurrent_Object = MibTableColumn
rectifierStatusOutputCurrent = _RectifierStatusOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2, 1, 3),
    _RectifierStatusOutputCurrent_Type()
)
rectifierStatusOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rectifierStatusOutputCurrent.setUnits("DeciAmperes")


class _RectifierStatusOutputVoltage_Type(Integer32):
    """Custom type rectifierStatusOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RectifierStatusOutputVoltage_Type.__name__ = "Integer32"
_RectifierStatusOutputVoltage_Object = MibTableColumn
rectifierStatusOutputVoltage = _RectifierStatusOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2, 1, 4),
    _RectifierStatusOutputVoltage_Type()
)
rectifierStatusOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    rectifierStatusOutputVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _RectifierStatusTemp_Type(Integer32):
    """Custom type rectifierStatusTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RectifierStatusTemp_Type.__name__ = "Integer32"
_RectifierStatusTemp_Object = MibTableColumn
rectifierStatusTemp = _RectifierStatusTemp_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2, 1, 5),
    _RectifierStatusTemp_Type()
)
rectifierStatusTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusTemp.setStatus("current")
if mibBuilder.loadTexts:
    rectifierStatusTemp.setUnits("Deg. C/F; i.e. 35 = 35 Degrees")


class _RectifierStatusType_Type(DisplayString):
    """Custom type rectifierStatusType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RectifierStatusType_Type.__name__ = "DisplayString"
_RectifierStatusType_Object = MibTableColumn
rectifierStatusType = _RectifierStatusType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2, 1, 6),
    _RectifierStatusType_Type()
)
rectifierStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusType.setStatus("current")


class _RectifierStatusSKU_Type(DisplayString):
    """Custom type rectifierStatusSKU based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RectifierStatusSKU_Type.__name__ = "DisplayString"
_RectifierStatusSKU_Object = MibTableColumn
rectifierStatusSKU = _RectifierStatusSKU_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2, 1, 7),
    _RectifierStatusSKU_Type()
)
rectifierStatusSKU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusSKU.setStatus("current")


class _RectifierStatusSerialNo_Type(DisplayString):
    """Custom type rectifierStatusSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierStatusSerialNo_Type.__name__ = "DisplayString"
_RectifierStatusSerialNo_Object = MibTableColumn
rectifierStatusSerialNo = _RectifierStatusSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2, 1, 8),
    _RectifierStatusSerialNo_Type()
)
rectifierStatusSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusSerialNo.setStatus("current")


class _RectifierStatusRevisionLevel_Type(DisplayString):
    """Custom type rectifierStatusRevisionLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierStatusRevisionLevel_Type.__name__ = "DisplayString"
_RectifierStatusRevisionLevel_Object = MibTableColumn
rectifierStatusRevisionLevel = _RectifierStatusRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 5, 5, 2, 1, 9),
    _RectifierStatusRevisionLevel_Type()
)
rectifierStatusRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatusRevisionLevel.setStatus("current")
_AcDistribution_ObjectIdentity = ObjectIdentity
acDistribution = _AcDistribution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 6)
)
_AcVoltage1_Type = Integer32
_AcVoltage1_Object = MibScalar
acVoltage1 = _AcVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 6, 1),
    _AcVoltage1_Type()
)
acVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acVoltage1.setStatus("current")
if mibBuilder.loadTexts:
    acVoltage1.setUnits("Volts AC")
_AcVoltage2_Type = Integer32
_AcVoltage2_Object = MibScalar
acVoltage2 = _AcVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 6, 2),
    _AcVoltage2_Type()
)
acVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acVoltage2.setStatus("current")
if mibBuilder.loadTexts:
    acVoltage2.setUnits("Volts AC")
_AcVoltage3_Type = Integer32
_AcVoltage3_Object = MibScalar
acVoltage3 = _AcVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 6, 3),
    _AcVoltage3_Type()
)
acVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acVoltage3.setStatus("current")
if mibBuilder.loadTexts:
    acVoltage3.setUnits("Volts AC")
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7)
)
_AlarmWellknownAlarms_ObjectIdentity = ObjectIdentity
alarmWellknownAlarms = _AlarmWellknownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1)
)


class _AlarmMajorHighBattVolt_Type(Integer32):
    """Custom type alarmMajorHighBattVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMajorHighBattVolt_Type.__name__ = "Integer32"
_AlarmMajorHighBattVolt_Object = MibScalar
alarmMajorHighBattVolt = _AlarmMajorHighBattVolt_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 1),
    _AlarmMajorHighBattVolt_Type()
)
alarmMajorHighBattVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorHighBattVolt.setStatus("current")


class _AlarmMinorHighBattVolt_Type(Integer32):
    """Custom type alarmMinorHighBattVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMinorHighBattVolt_Type.__name__ = "Integer32"
_AlarmMinorHighBattVolt_Object = MibScalar
alarmMinorHighBattVolt = _AlarmMinorHighBattVolt_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 2),
    _AlarmMinorHighBattVolt_Type()
)
alarmMinorHighBattVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorHighBattVolt.setStatus("current")


class _AlarmMajorLowBattVolt_Type(Integer32):
    """Custom type alarmMajorLowBattVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMajorLowBattVolt_Type.__name__ = "Integer32"
_AlarmMajorLowBattVolt_Object = MibScalar
alarmMajorLowBattVolt = _AlarmMajorLowBattVolt_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 3),
    _AlarmMajorLowBattVolt_Type()
)
alarmMajorLowBattVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorLowBattVolt.setStatus("current")


class _AlarmMinorLowBattVolt_Type(Integer32):
    """Custom type alarmMinorLowBattVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMinorLowBattVolt_Type.__name__ = "Integer32"
_AlarmMinorLowBattVolt_Object = MibScalar
alarmMinorLowBattVolt = _AlarmMinorLowBattVolt_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 4),
    _AlarmMinorLowBattVolt_Type()
)
alarmMinorLowBattVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorLowBattVolt.setStatus("current")


class _AlarmMajorBatteryHighTemp_Type(Integer32):
    """Custom type alarmMajorBatteryHighTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMajorBatteryHighTemp_Type.__name__ = "Integer32"
_AlarmMajorBatteryHighTemp_Object = MibScalar
alarmMajorBatteryHighTemp = _AlarmMajorBatteryHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 5),
    _AlarmMajorBatteryHighTemp_Type()
)
alarmMajorBatteryHighTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorBatteryHighTemp.setStatus("current")


class _AlarmMinorBatteryHighTemp_Type(Integer32):
    """Custom type alarmMinorBatteryHighTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMinorBatteryHighTemp_Type.__name__ = "Integer32"
_AlarmMinorBatteryHighTemp_Object = MibScalar
alarmMinorBatteryHighTemp = _AlarmMinorBatteryHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 6),
    _AlarmMinorBatteryHighTemp_Type()
)
alarmMinorBatteryHighTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorBatteryHighTemp.setStatus("current")


class _AlarmBatteryDisconnectOpen_Type(Integer32):
    """Custom type alarmBatteryDisconnectOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmBatteryDisconnectOpen_Type.__name__ = "Integer32"
_AlarmBatteryDisconnectOpen_Object = MibScalar
alarmBatteryDisconnectOpen = _AlarmBatteryDisconnectOpen_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 7),
    _AlarmBatteryDisconnectOpen_Type()
)
alarmBatteryDisconnectOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBatteryDisconnectOpen.setStatus("current")


class _AlarmLVD1open_Type(Integer32):
    """Custom type alarmLVD1open based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmLVD1open_Type.__name__ = "Integer32"
_AlarmLVD1open_Object = MibScalar
alarmLVD1open = _AlarmLVD1open_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 8),
    _AlarmLVD1open_Type()
)
alarmLVD1open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLVD1open.setStatus("current")


class _AlarmLVD2open_Type(Integer32):
    """Custom type alarmLVD2open based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmLVD2open_Type.__name__ = "Integer32"
_AlarmLVD2open_Object = MibScalar
alarmLVD2open = _AlarmLVD2open_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 9),
    _AlarmLVD2open_Type()
)
alarmLVD2open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLVD2open.setStatus("current")


class _AlarmLVD3open_Type(Integer32):
    """Custom type alarmLVD3open based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmLVD3open_Type.__name__ = "Integer32"
_AlarmLVD3open_Object = MibScalar
alarmLVD3open = _AlarmLVD3open_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 10),
    _AlarmLVD3open_Type()
)
alarmLVD3open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLVD3open.setStatus("current")


class _AlarmACmains_Type(Integer32):
    """Custom type alarmACmains based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmACmains_Type.__name__ = "Integer32"
_AlarmACmains_Object = MibScalar
alarmACmains = _AlarmACmains_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 11),
    _AlarmACmains_Type()
)
alarmACmains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmACmains.setStatus("current")


class _AlarmBatteryBreakerOpen_Type(Integer32):
    """Custom type alarmBatteryBreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmBatteryBreakerOpen_Type.__name__ = "Integer32"
_AlarmBatteryBreakerOpen_Object = MibScalar
alarmBatteryBreakerOpen = _AlarmBatteryBreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 12),
    _AlarmBatteryBreakerOpen_Type()
)
alarmBatteryBreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBatteryBreakerOpen.setStatus("current")


class _AlarmDistributionBreakerOpen_Type(Integer32):
    """Custom type alarmDistributionBreakerOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmDistributionBreakerOpen_Type.__name__ = "Integer32"
_AlarmDistributionBreakerOpen_Object = MibScalar
alarmDistributionBreakerOpen = _AlarmDistributionBreakerOpen_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 13),
    _AlarmDistributionBreakerOpen_Type()
)
alarmDistributionBreakerOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDistributionBreakerOpen.setStatus("current")


class _AlarmMajorRectifier_Type(Integer32):
    """Custom type alarmMajorRectifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMajorRectifier_Type.__name__ = "Integer32"
_AlarmMajorRectifier_Object = MibScalar
alarmMajorRectifier = _AlarmMajorRectifier_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 14),
    _AlarmMajorRectifier_Type()
)
alarmMajorRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorRectifier.setStatus("current")


class _AlarmMinorRectifier_Type(Integer32):
    """Custom type alarmMinorRectifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMinorRectifier_Type.__name__ = "Integer32"
_AlarmMinorRectifier_Object = MibScalar
alarmMinorRectifier = _AlarmMinorRectifier_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 15),
    _AlarmMinorRectifier_Type()
)
alarmMinorRectifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorRectifier.setStatus("current")


class _AlarmMajorBatterySymmetry_Type(Integer32):
    """Custom type alarmMajorBatterySymmetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMajorBatterySymmetry_Type.__name__ = "Integer32"
_AlarmMajorBatterySymmetry_Object = MibScalar
alarmMajorBatterySymmetry = _AlarmMajorBatterySymmetry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 16),
    _AlarmMajorBatterySymmetry_Type()
)
alarmMajorBatterySymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorBatterySymmetry.setStatus("current")


class _AlarmMinorBatterySymmetry_Type(Integer32):
    """Custom type alarmMinorBatterySymmetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMinorBatterySymmetry_Type.__name__ = "Integer32"
_AlarmMinorBatterySymmetry_Object = MibScalar
alarmMinorBatterySymmetry = _AlarmMinorBatterySymmetry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 17),
    _AlarmMinorBatterySymmetry_Type()
)
alarmMinorBatterySymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorBatterySymmetry.setStatus("current")


class _AlarmBatteryLifeEnded_Type(Integer32):
    """Custom type alarmBatteryLifeEnded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmBatteryLifeEnded_Type.__name__ = "Integer32"
_AlarmBatteryLifeEnded_Object = MibScalar
alarmBatteryLifeEnded = _AlarmBatteryLifeEnded_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 18),
    _AlarmBatteryLifeEnded_Type()
)
alarmBatteryLifeEnded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBatteryLifeEnded.setStatus("current")


class _AlarmBatteryTestmodeEntered_Type(Integer32):
    """Custom type alarmBatteryTestmodeEntered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmBatteryTestmodeEntered_Type.__name__ = "Integer32"
_AlarmBatteryTestmodeEntered_Object = MibScalar
alarmBatteryTestmodeEntered = _AlarmBatteryTestmodeEntered_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 19),
    _AlarmBatteryTestmodeEntered_Type()
)
alarmBatteryTestmodeEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBatteryTestmodeEntered.setStatus("current")


class _AlarmBatteryBoostmodeEntered_Type(Integer32):
    """Custom type alarmBatteryBoostmodeEntered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmBatteryBoostmodeEntered_Type.__name__ = "Integer32"
_AlarmBatteryBoostmodeEntered_Object = MibScalar
alarmBatteryBoostmodeEntered = _AlarmBatteryBoostmodeEntered_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 20),
    _AlarmBatteryBoostmodeEntered_Type()
)
alarmBatteryBoostmodeEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBatteryBoostmodeEntered.setStatus("current")


class _AlarmIoUnitTemp1_Type(Integer32):
    """Custom type alarmIoUnitTemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmIoUnitTemp1_Type.__name__ = "Integer32"
_AlarmIoUnitTemp1_Object = MibScalar
alarmIoUnitTemp1 = _AlarmIoUnitTemp1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 21),
    _AlarmIoUnitTemp1_Type()
)
alarmIoUnitTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIoUnitTemp1.setStatus("current")


class _AlarmIoUnitTemp2_Type(Integer32):
    """Custom type alarmIoUnitTemp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmIoUnitTemp2_Type.__name__ = "Integer32"
_AlarmIoUnitTemp2_Object = MibScalar
alarmIoUnitTemp2 = _AlarmIoUnitTemp2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 22),
    _AlarmIoUnitTemp2_Type()
)
alarmIoUnitTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIoUnitTemp2.setStatus("current")


class _AlarmIoUnitDeltaFanSpeed1_Type(Integer32):
    """Custom type alarmIoUnitDeltaFanSpeed1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmIoUnitDeltaFanSpeed1_Type.__name__ = "Integer32"
_AlarmIoUnitDeltaFanSpeed1_Object = MibScalar
alarmIoUnitDeltaFanSpeed1 = _AlarmIoUnitDeltaFanSpeed1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 23),
    _AlarmIoUnitDeltaFanSpeed1_Type()
)
alarmIoUnitDeltaFanSpeed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIoUnitDeltaFanSpeed1.setStatus("current")


class _AlarmIoUnitDeltaFanSpeed2_Type(Integer32):
    """Custom type alarmIoUnitDeltaFanSpeed2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmIoUnitDeltaFanSpeed2_Type.__name__ = "Integer32"
_AlarmIoUnitDeltaFanSpeed2_Object = MibScalar
alarmIoUnitDeltaFanSpeed2 = _AlarmIoUnitDeltaFanSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 24),
    _AlarmIoUnitDeltaFanSpeed2_Type()
)
alarmIoUnitDeltaFanSpeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIoUnitDeltaFanSpeed2.setStatus("current")


class _AlarmMajorSolar_Type(Integer32):
    """Custom type alarmMajorSolar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMajorSolar_Type.__name__ = "Integer32"
_AlarmMajorSolar_Object = MibScalar
alarmMajorSolar = _AlarmMajorSolar_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 25),
    _AlarmMajorSolar_Type()
)
alarmMajorSolar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorSolar.setStatus("current")


class _AlarmMinorSolar_Type(Integer32):
    """Custom type alarmMinorSolar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMinorSolar_Type.__name__ = "Integer32"
_AlarmMinorSolar_Object = MibScalar
alarmMinorSolar = _AlarmMinorSolar_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 26),
    _AlarmMinorSolar_Type()
)
alarmMinorSolar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorSolar.setStatus("current")


class _AlarmMajorRectifierCapacity_Type(Integer32):
    """Custom type alarmMajorRectifierCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMajorRectifierCapacity_Type.__name__ = "Integer32"
_AlarmMajorRectifierCapacity_Object = MibScalar
alarmMajorRectifierCapacity = _AlarmMajorRectifierCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 27),
    _AlarmMajorRectifierCapacity_Type()
)
alarmMajorRectifierCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMajorRectifierCapacity.setStatus("current")


class _AlarmMinorRectifierCapacity_Type(Integer32):
    """Custom type alarmMinorRectifierCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmMinorRectifierCapacity_Type.__name__ = "Integer32"
_AlarmMinorRectifierCapacity_Object = MibScalar
alarmMinorRectifierCapacity = _AlarmMinorRectifierCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 7, 1, 28),
    _AlarmMinorRectifierCapacity_Type()
)
alarmMinorRectifierCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMinorRectifierCapacity.setStatus("current")
_SolarCharger_ObjectIdentity = ObjectIdentity
solarCharger = _SolarCharger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9)
)


class _SolarChargerInstalledsolarChargers_Type(Integer32):
    """Custom type solarChargerInstalledsolarChargers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 101),
    )


_SolarChargerInstalledsolarChargers_Type.__name__ = "Integer32"
_SolarChargerInstalledsolarChargers_Object = MibScalar
solarChargerInstalledsolarChargers = _SolarChargerInstalledsolarChargers_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 1),
    _SolarChargerInstalledsolarChargers_Type()
)
solarChargerInstalledsolarChargers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerInstalledsolarChargers.setStatus("current")


class _SolarChargersActive_Type(Integer32):
    """Custom type solarChargersActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 101),
    )


_SolarChargersActive_Type.__name__ = "Integer32"
_SolarChargersActive_Object = MibScalar
solarChargersActive = _SolarChargersActive_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 2),
    _SolarChargersActive_Type()
)
solarChargersActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersActive.setStatus("current")
_SolarChargerTotalCurrent_Type = Integer32
_SolarChargerTotalCurrent_Object = MibScalar
solarChargerTotalCurrent = _SolarChargerTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 3),
    _SolarChargerTotalCurrent_Type()
)
solarChargerTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    solarChargerTotalCurrent.setUnits("DeciAmperes; i.e. 20 = 2,0 Amperes")


class _SolarChargerUtilization_Type(Integer32):
    """Custom type solarChargerUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SolarChargerUtilization_Type.__name__ = "Integer32"
_SolarChargerUtilization_Object = MibScalar
solarChargerUtilization = _SolarChargerUtilization_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 4),
    _SolarChargerUtilization_Type()
)
solarChargerUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerUtilization.setStatus("current")
_SolarChargerStatus_ObjectIdentity = ObjectIdentity
solarChargerStatus = _SolarChargerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5)
)


class _SolarChargerStatusNoIndex_Type(Integer32):
    """Custom type solarChargerStatusNoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 95),
    )


_SolarChargerStatusNoIndex_Type.__name__ = "Integer32"
_SolarChargerStatusNoIndex_Object = MibScalar
solarChargerStatusNoIndex = _SolarChargerStatusNoIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 1),
    _SolarChargerStatusNoIndex_Type()
)
solarChargerStatusNoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargerStatusNoIndex.setStatus("current")
_SolarChargerStatusTable_Object = MibTable
solarChargerStatusTable = _SolarChargerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2)
)
if mibBuilder.loadTexts:
    solarChargerStatusTable.setStatus("current")
_SolarChargerStatusEntry_Object = MibTableRow
solarChargerStatusEntry = _SolarChargerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2, 1)
)
solarChargerStatusEntry.setIndexNames(
    (0, "ELTEK-DISTRIBUTED-MIB", "solarChargerStatusID"),
)
if mibBuilder.loadTexts:
    solarChargerStatusEntry.setStatus("current")


class _SolarChargerStatusID_Type(Integer32):
    """Custom type solarChargerStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SolarChargerStatusID_Type.__name__ = "Integer32"
_SolarChargerStatusID_Object = MibTableColumn
solarChargerStatusID = _SolarChargerStatusID_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2, 1, 1),
    _SolarChargerStatusID_Type()
)
solarChargerStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerStatusID.setStatus("current")


class _SolarChargerStatusStatus_Type(Integer32):
    """Custom type solarChargerStatusStatus based on Integer32"""
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
        *(("alarm", 2),
          ("disabled", 4),
          ("normal", 1),
          ("notPresent", 0),
          ("notUsed", 3))
    )


_SolarChargerStatusStatus_Type.__name__ = "Integer32"
_SolarChargerStatusStatus_Object = MibTableColumn
solarChargerStatusStatus = _SolarChargerStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2, 1, 2),
    _SolarChargerStatusStatus_Type()
)
solarChargerStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerStatusStatus.setStatus("current")


class _SolarChargerOutputCurrent_Type(Integer32):
    """Custom type solarChargerOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SolarChargerOutputCurrent_Type.__name__ = "Integer32"
_SolarChargerOutputCurrent_Object = MibTableColumn
solarChargerOutputCurrent = _SolarChargerOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2, 1, 3),
    _SolarChargerOutputCurrent_Type()
)
solarChargerOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    solarChargerOutputCurrent.setUnits("DeciAmperes; i.e. 20 = 2,0 Amperes")


class _SolarChargerOutputVoltage_Type(Integer32):
    """Custom type solarChargerOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SolarChargerOutputVoltage_Type.__name__ = "Integer32"
_SolarChargerOutputVoltage_Object = MibTableColumn
solarChargerOutputVoltage = _SolarChargerOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2, 1, 4),
    _SolarChargerOutputVoltage_Type()
)
solarChargerOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    solarChargerOutputVoltage.setUnits("1/100 Volt; i.e. 5400 = 54.00V")


class _SolarChargerTemp_Type(Integer32):
    """Custom type solarChargerTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SolarChargerTemp_Type.__name__ = "Integer32"
_SolarChargerTemp_Object = MibTableColumn
solarChargerTemp = _SolarChargerTemp_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2, 1, 5),
    _SolarChargerTemp_Type()
)
solarChargerTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerTemp.setStatus("current")


class _SolarChargerType_Type(DisplayString):
    """Custom type solarChargerType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SolarChargerType_Type.__name__ = "DisplayString"
_SolarChargerType_Object = MibTableColumn
solarChargerType = _SolarChargerType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2, 1, 6),
    _SolarChargerType_Type()
)
solarChargerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerType.setStatus("current")


class _SolarChargerSKU_Type(DisplayString):
    """Custom type solarChargerSKU based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SolarChargerSKU_Type.__name__ = "DisplayString"
_SolarChargerSKU_Object = MibTableColumn
solarChargerSKU = _SolarChargerSKU_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2, 1, 7),
    _SolarChargerSKU_Type()
)
solarChargerSKU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerSKU.setStatus("current")


class _SolarChargerSerialNo_Type(DisplayString):
    """Custom type solarChargerSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SolarChargerSerialNo_Type.__name__ = "DisplayString"
_SolarChargerSerialNo_Object = MibTableColumn
solarChargerSerialNo = _SolarChargerSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2, 1, 8),
    _SolarChargerSerialNo_Type()
)
solarChargerSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerSerialNo.setStatus("current")


class _SolarChargerRevisionLevel_Type(DisplayString):
    """Custom type solarChargerRevisionLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SolarChargerRevisionLevel_Type.__name__ = "DisplayString"
_SolarChargerRevisionLevel_Object = MibTableColumn
solarChargerRevisionLevel = _SolarChargerRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 9, 9, 5, 2, 1, 9),
    _SolarChargerRevisionLevel_Type()
)
solarChargerRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerRevisionLevel.setStatus("current")

# Managed Objects groups


# Notification objects

alarmMajorHighBattVoltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 1)
)
alarmMajorHighBattVoltTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMajorHighBattVolt"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMajorHighBattVoltTrap.setStatus(
        "current"
    )

alarmMinorHighBattVoltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 2)
)
alarmMinorHighBattVoltTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMinorHighBattVolt"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMinorHighBattVoltTrap.setStatus(
        "current"
    )

alarmMajorLowBattVoltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 3)
)
alarmMajorLowBattVoltTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMajorLowBattVolt"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMajorLowBattVoltTrap.setStatus(
        "current"
    )

alarmMinorLowBattVoltTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 4)
)
alarmMinorLowBattVoltTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMinorLowBattVolt"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMinorLowBattVoltTrap.setStatus(
        "current"
    )

alarmMajorBatteryHighTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 5)
)
alarmMajorBatteryHighTempTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMajorBatteryHighTemp"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMajorBatteryHighTempTrap.setStatus(
        "current"
    )

alarmMinorBatteryHighTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 6)
)
alarmMinorBatteryHighTempTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMinorBatteryHighTemp"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMinorBatteryHighTempTrap.setStatus(
        "current"
    )

alarmBatteryDisconnectOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 7)
)
alarmBatteryDisconnectOpenTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmBatteryDisconnectOpen"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmBatteryDisconnectOpenTrap.setStatus(
        "current"
    )

alarmLVD1openTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 8)
)
alarmLVD1openTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmLVD1open"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmLVD1openTrap.setStatus(
        "current"
    )

alarmLVD2openTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 9)
)
alarmLVD2openTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmLVD2open"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmLVD2openTrap.setStatus(
        "current"
    )

alarmLVD3openTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 10)
)
alarmLVD3openTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmLVD3open"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmLVD3openTrap.setStatus(
        "current"
    )

alarmACmainsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 11)
)
alarmACmainsTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmACmains"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmACmainsTrap.setStatus(
        "current"
    )

alarmBatteryBreakerOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 12)
)
alarmBatteryBreakerOpenTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmBatteryBreakerOpen"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmBatteryBreakerOpenTrap.setStatus(
        "current"
    )

alarmDistributionBreakerOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 13)
)
alarmDistributionBreakerOpenTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmDistributionBreakerOpen"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmDistributionBreakerOpenTrap.setStatus(
        "current"
    )

alarmMajorRectifierTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 14)
)
alarmMajorRectifierTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMajorRectifier"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMajorRectifierTrap.setStatus(
        "current"
    )

alarmMinorRectifierTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 15)
)
alarmMinorRectifierTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMinorRectifier"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMinorRectifierTrap.setStatus(
        "current"
    )

alarmMajorBatterySymmetryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 16)
)
alarmMajorBatterySymmetryTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMajorBatterySymmetry"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMajorBatterySymmetryTrap.setStatus(
        "current"
    )

alarmMinorBatterySymmetryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 17)
)
alarmMinorBatterySymmetryTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMinorBatterySymmetry"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMinorBatterySymmetryTrap.setStatus(
        "current"
    )

alarmBatteryLifeEndedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 18)
)
alarmBatteryLifeEndedTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmBatteryLifeEnded"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmBatteryLifeEndedTrap.setStatus(
        "current"
    )

alarmBatteryTestmodeEnteredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 19)
)
alarmBatteryTestmodeEnteredTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmBatteryTestmodeEntered"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmBatteryTestmodeEnteredTrap.setStatus(
        "current"
    )

alarmBatteryBoostmodeEnteredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 20)
)
alarmBatteryBoostmodeEnteredTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmBatteryBoostmodeEntered"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmBatteryBoostmodeEnteredTrap.setStatus(
        "current"
    )

alarmController1proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 21)
)
alarmController1proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurable1"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurableText1"))
)
if mibBuilder.loadTexts:
    alarmController1proginputTrap.setStatus(
        "current"
    )

alarmController2proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 22)
)
alarmController2proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurable2"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurableText2"))
)
if mibBuilder.loadTexts:
    alarmController2proginputTrap.setStatus(
        "current"
    )

alarmController3proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 23)
)
alarmController3proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurable3"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurableText3"))
)
if mibBuilder.loadTexts:
    alarmController3proginputTrap.setStatus(
        "current"
    )

alarmController4proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 24)
)
alarmController4proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurable4"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurableText4"))
)
if mibBuilder.loadTexts:
    alarmController4proginputTrap.setStatus(
        "current"
    )

alarmController5proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 25)
)
alarmController5proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurable5"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurableText5"))
)
if mibBuilder.loadTexts:
    alarmController5proginputTrap.setStatus(
        "current"
    )

alarmController6proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 26)
)
alarmController6proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurable6"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurableText6"))
)
if mibBuilder.loadTexts:
    alarmController6proginputTrap.setStatus(
        "current"
    )

alarmController7proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 27)
)
alarmController7proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurable7"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurableText7"))
)
if mibBuilder.loadTexts:
    alarmController7proginputTrap.setStatus(
        "current"
    )

alarmController8proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 28)
)
alarmController8proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurable8"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "inputUserConfigurableText8"))
)
if mibBuilder.loadTexts:
    alarmController8proginputTrap.setStatus(
        "current"
    )

infoHeartBeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 29)
)
infoHeartBeatTrap.setObjects(
    ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter")
)
if mibBuilder.loadTexts:
    infoHeartBeatTrap.setStatus(
        "current"
    )

alarmIoUnitTemp1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 30)
)
alarmIoUnitTemp1Trap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmIoUnitTemp1"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmIoUnitTemp1Trap.setStatus(
        "current"
    )

alarmIoUnitTemp2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 31)
)
alarmIoUnitTemp2Trap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmIoUnitTemp2"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmIoUnitTemp2Trap.setStatus(
        "current"
    )

alarmIoUnitDeltaFanSpeed1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 32)
)
alarmIoUnitDeltaFanSpeed1Trap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmIoUnitDeltaFanSpeed1"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmIoUnitDeltaFanSpeed1Trap.setStatus(
        "current"
    )

alarmIoUnitDeltaFanSpeed2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 33)
)
alarmIoUnitDeltaFanSpeed2Trap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmIoUnitDeltaFanSpeed2"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmIoUnitDeltaFanSpeed2Trap.setStatus(
        "current"
    )

alarmIoUnit1proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 34)
)
alarmIoUnit1proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus1"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText1"))
)
if mibBuilder.loadTexts:
    alarmIoUnit1proginputTrap.setStatus(
        "current"
    )

alarmIoUnit2proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 35)
)
alarmIoUnit2proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus2"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText2"))
)
if mibBuilder.loadTexts:
    alarmIoUnit2proginputTrap.setStatus(
        "current"
    )

alarmIoUnit3proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 36)
)
alarmIoUnit3proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus3"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText3"))
)
if mibBuilder.loadTexts:
    alarmIoUnit3proginputTrap.setStatus(
        "current"
    )

alarmIoUnit4proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 37)
)
alarmIoUnit4proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus4"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText4"))
)
if mibBuilder.loadTexts:
    alarmIoUnit4proginputTrap.setStatus(
        "current"
    )

alarmIoUnit5proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 38)
)
alarmIoUnit5proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus5"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText5"))
)
if mibBuilder.loadTexts:
    alarmIoUnit5proginputTrap.setStatus(
        "current"
    )

alarmIoUnit6proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 39)
)
alarmIoUnit6proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus6"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText6"))
)
if mibBuilder.loadTexts:
    alarmIoUnit6proginputTrap.setStatus(
        "current"
    )

alarmIoUnit7proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 40)
)
alarmIoUnit7proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus6"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText6"))
)
if mibBuilder.loadTexts:
    alarmIoUnit7proginputTrap.setStatus(
        "current"
    )

alarmIoUnit8proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 41)
)
alarmIoUnit8proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus6"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText6"))
)
if mibBuilder.loadTexts:
    alarmIoUnit8proginputTrap.setStatus(
        "current"
    )

alarmIoUnit9proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 42)
)
alarmIoUnit9proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus6"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText6"))
)
if mibBuilder.loadTexts:
    alarmIoUnit9proginputTrap.setStatus(
        "current"
    )

alarmIoUnit10proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 43)
)
alarmIoUnit10proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus6"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText6"))
)
if mibBuilder.loadTexts:
    alarmIoUnit10proginputTrap.setStatus(
        "current"
    )

alarmIoUnit11proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 44)
)
alarmIoUnit11proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus6"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText6"))
)
if mibBuilder.loadTexts:
    alarmIoUnit11proginputTrap.setStatus(
        "current"
    )

alarmIoUnit12proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 45)
)
alarmIoUnit12proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus6"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText6"))
)
if mibBuilder.loadTexts:
    alarmIoUnit12proginputTrap.setStatus(
        "current"
    )

alarmIoUnit13proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 46)
)
alarmIoUnit13proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus6"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText6"))
)
if mibBuilder.loadTexts:
    alarmIoUnit13proginputTrap.setStatus(
        "current"
    )

alarmIoUnit14proginputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 47)
)
alarmIoUnit14proginputTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputStatus6"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"),
        ("ELTEK-DISTRIBUTED-MIB", "systemLastDigInput"),
        ("ELTEK-DISTRIBUTED-MIB", "ioUnitProgInputText6"))
)
if mibBuilder.loadTexts:
    alarmIoUnit14proginputTrap.setStatus(
        "current"
    )

alarmMajorSolarChargerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 48)
)
alarmMajorSolarChargerTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMajorSolar"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMajorSolarChargerTrap.setStatus(
        "current"
    )

alarmMinorSolarChargerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 49)
)
alarmMinorSolarChargerTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMinorSolar"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMinorSolarChargerTrap.setStatus(
        "current"
    )

alarmMajorRectifierCapacityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 50)
)
alarmMajorRectifierCapacityTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMajorRectifierCapacity"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMajorRectifierCapacityTrap.setStatus(
        "current"
    )

alarmMinorRectifierCapacityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8, 51)
)
alarmMinorRectifierCapacityTrap.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMinorRectifierCapacity"),
        ("ELTEK-DISTRIBUTED-MIB", "systemTrapCounter"))
)
if mibBuilder.loadTexts:
    alarmMinorRectifierCapacityTrap.setStatus(
        "current"
    )


# Notifications groups

dcSystemTraps = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12148, 9, 8)
)
dcSystemTraps.setObjects(
      *(("ELTEK-DISTRIBUTED-MIB", "alarmMajorHighBattVoltTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMinorHighBattVoltTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMajorLowBattVoltTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMinorLowBattVoltTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMajorBatteryHighTempTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMinorBatteryHighTempTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmBatteryDisconnectOpenTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmLVD1openTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmLVD2openTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmLVD3openTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmACmainsTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmBatteryBreakerOpenTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmDistributionBreakerOpenTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMajorRectifierTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMinorRectifierTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMajorBatterySymmetryTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMinorBatterySymmetryTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmBatteryLifeEndedTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmBatteryTestmodeEnteredTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmBatteryBoostmodeEnteredTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmController1proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmController2proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmController3proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmController4proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmController5proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmController6proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmController7proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmController8proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "infoHeartBeatTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnitTemp1Trap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnitTemp2Trap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnitDeltaFanSpeed1Trap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnitDeltaFanSpeed2Trap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit1proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit2proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit3proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit4proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit5proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit6proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit7proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit8proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit9proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit10proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit11proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit12proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit13proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmIoUnit14proginputTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMajorSolarChargerTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMinorSolarChargerTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMajorRectifierCapacityTrap"),
        ("ELTEK-DISTRIBUTED-MIB", "alarmMinorRectifierCapacityTrap"))
)
if mibBuilder.loadTexts:
    dcSystemTraps.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEK-DISTRIBUTED-MIB",
    **{"eltek": eltek,
       "eltekDistributedPlantV7": eltekDistributedPlantV7,
       "controlSystem": controlSystem,
       "systemTime": systemTime,
       "systemTimeTime": systemTimeTime,
       "systemInfoRefresh": systemInfoRefresh,
       "systemTrapRepeatRate": systemTrapRepeatRate,
       "systemSendOffTrap": systemSendOffTrap,
       "systemNumOfControlUnits": systemNumOfControlUnits,
       "systemControlUnitIndex": systemControlUnitIndex,
       "systemControlUnitTable": systemControlUnitTable,
       "systemControlUnitEntry": systemControlUnitEntry,
       "inputControlUnitID": inputControlUnitID,
       "inputUserConfigurable1": inputUserConfigurable1,
       "inputUserConfigurable2": inputUserConfigurable2,
       "inputUserConfigurable3": inputUserConfigurable3,
       "inputUserConfigurable4": inputUserConfigurable4,
       "inputUserConfigurable5": inputUserConfigurable5,
       "inputUserConfigurable6": inputUserConfigurable6,
       "inputUserConfigurable7": inputUserConfigurable7,
       "inputUserConfigurable8": inputUserConfigurable8,
       "inputUserConfigurable9": inputUserConfigurable9,
       "inputUserConfigurable10": inputUserConfigurable10,
       "systemLinkStatus": systemLinkStatus,
       "systemInitiateEEPROM": systemInitiateEEPROM,
       "systemLastDigInput": systemLastDigInput,
       "systemTrapCounter": systemTrapCounter,
       "systemHeartBeatTrapRepeatRate": systemHeartBeatTrapRepeatRate,
       "systemResetManualAlarms": systemResetManualAlarms,
       "systemControlUnitInputIndex": systemControlUnitInputIndex,
       "systemControlUnitInputTable": systemControlUnitInputTable,
       "systemControlUnitInputEntry": systemControlUnitInputEntry,
       "inputUnitID": inputUnitID,
       "inputUserConfigurableText1": inputUserConfigurableText1,
       "inputUserConfigurableText2": inputUserConfigurableText2,
       "inputUserConfigurableText3": inputUserConfigurableText3,
       "inputUserConfigurableText4": inputUserConfigurableText4,
       "inputUserConfigurableText5": inputUserConfigurableText5,
       "inputUserConfigurableText6": inputUserConfigurableText6,
       "inputUserConfigurableText7": inputUserConfigurableText7,
       "inputUserConfigurableText8": inputUserConfigurableText8,
       "inputUserConfigurableText9": inputUserConfigurableText9,
       "inputUserConfigurableText10": inputUserConfigurableText10,
       "systemResetCtrlSystem": systemResetCtrlSystem,
       "ioUnits": ioUnits,
       "ioUnitNumberOfUnits": ioUnitNumberOfUnits,
       "ioUnitsIndex": ioUnitsIndex,
       "ioUnitsTable": ioUnitsTable,
       "ioUnitsEntry": ioUnitsEntry,
       "ioUnitID": ioUnitID,
       "ioUnitOutDoorTemp1": ioUnitOutDoorTemp1,
       "ioUnitOutDoorTemp2": ioUnitOutDoorTemp2,
       "ioUnitFanSpeed1": ioUnitFanSpeed1,
       "ioUnitFanSpeedDeltaValue1": ioUnitFanSpeedDeltaValue1,
       "ioUnitFanSpeed2": ioUnitFanSpeed2,
       "ioUnitFanSpeedDeltaValue2": ioUnitFanSpeedDeltaValue2,
       "ioUnitProgInputText1": ioUnitProgInputText1,
       "ioUnitProgInputStatus1": ioUnitProgInputStatus1,
       "ioUnitProgInputText2": ioUnitProgInputText2,
       "ioUnitProgInputStatus2": ioUnitProgInputStatus2,
       "ioUnitProgInputText3": ioUnitProgInputText3,
       "ioUnitProgInputStatus3": ioUnitProgInputStatus3,
       "ioUnitProgInputText4": ioUnitProgInputText4,
       "ioUnitProgInputStatus4": ioUnitProgInputStatus4,
       "ioUnitProgInputText5": ioUnitProgInputText5,
       "ioUnitProgInputStatus5": ioUnitProgInputStatus5,
       "ioUnitProgInputText6": ioUnitProgInputText6,
       "ioUnitProgInputStatus6": ioUnitProgInputStatus6,
       "ioUnitProgInputValue1": ioUnitProgInputValue1,
       "ioUnitProgInputValue2": ioUnitProgInputValue2,
       "ioUnitProgInputValue3": ioUnitProgInputValue3,
       "ioUnitProgInputValue4": ioUnitProgInputValue4,
       "ioUnitProgInputValue5": ioUnitProgInputValue5,
       "ioUnitProgInputValue6": ioUnitProgInputValue6,
       "systemServiceMode": systemServiceMode,
       "dcSystem": dcSystem,
       "dcPlant": dcPlant,
       "systemSiteInfo": systemSiteInfo,
       "systemSiteInfoCustomer": systemSiteInfoCustomer,
       "systemSiteInfoLocation": systemSiteInfoLocation,
       "systemSiteInfoMessage1": systemSiteInfoMessage1,
       "systemSiteInfoMessage2": systemSiteInfoMessage2,
       "systemSiteInfoInstalledDate": systemSiteInfoInstalledDate,
       "systemSiteInfoControllerType": systemSiteInfoControllerType,
       "systemSiteInfoSystemSeriaNum": systemSiteInfoSystemSeriaNum,
       "systemSiteInfoControllerSeriaNum": systemSiteInfoControllerSeriaNum,
       "systemNominalVoltage": systemNominalVoltage,
       "systemOperationalStatus": systemOperationalStatus,
       "battery": battery,
       "batteryName": batteryName,
       "batteryVoltage": batteryVoltage,
       "batteryCurrent": batteryCurrent,
       "batteryTemp": batteryTemp,
       "batteryBreakerStatus": batteryBreakerStatus,
       "batteryChargeCurrentLimitCtrl": batteryChargeCurrentLimitCtrl,
       "batteryChargeCurrentLimitValue": batteryChargeCurrentLimitValue,
       "batteryTempCompEnable": batteryTempCompEnable,
       "batteryFloatVoltConfig": batteryFloatVoltConfig,
       "batteryBoostVoltConfig": batteryBoostVoltConfig,
       "batteryHighMajorAlarmVoltageConfig": batteryHighMajorAlarmVoltageConfig,
       "batteryHighMinorAlarmVoltageConfig": batteryHighMinorAlarmVoltageConfig,
       "batteryLowMajorAlarmVoltageConfig": batteryLowMajorAlarmVoltageConfig,
       "batteryLowMinorAlarmVoltageConfig": batteryLowMinorAlarmVoltageConfig,
       "batteryStartManualTest": batteryStartManualTest,
       "batteryStartManualBoost": batteryStartManualBoost,
       "batteryLVD": batteryLVD,
       "batteryLVDStatus": batteryLVDStatus,
       "batteryLVDDisconnectVoltage": batteryLVDDisconnectVoltage,
       "batteryLVDConnectVoltage": batteryLVDConnectVoltage,
       "batteryBanksNumofBanks": batteryBanksNumofBanks,
       "batteryBanks": batteryBanks,
       "batterySymmetryDeltaLimitVoltage": batterySymmetryDeltaLimitVoltage,
       "batteryBanksIndex": batteryBanksIndex,
       "batteryBanksTable": batteryBanksTable,
       "batteryBanksEntry": batteryBanksEntry,
       "batteryBankID": batteryBankID,
       "batteryBanksSymmetry1enable": batteryBanksSymmetry1enable,
       "batteryBanksSymmetry1status": batteryBanksSymmetry1status,
       "batteryBanksSymmetry1deltaVoltage": batteryBanksSymmetry1deltaVoltage,
       "batteryBanksSymmetry2enable": batteryBanksSymmetry2enable,
       "batteryBanksSymmetry2status": batteryBanksSymmetry2status,
       "batteryBanksSymmetry2deltaVoltage": batteryBanksSymmetry2deltaVoltage,
       "batteryBanksSymmetry3enable": batteryBanksSymmetry3enable,
       "batteryBanksSymmetry3status": batteryBanksSymmetry3status,
       "batteryBanksSymmetry3deltaVoltage": batteryBanksSymmetry3deltaVoltage,
       "batteryBanksSymmetry4enable": batteryBanksSymmetry4enable,
       "batteryBanksSymmetry4status": batteryBanksSymmetry4status,
       "batteryBanksSymmetry4deltaVoltage": batteryBanksSymmetry4deltaVoltage,
       "batteryBanksSymmetry5enable": batteryBanksSymmetry5enable,
       "batteryBanksSymmetry5status": batteryBanksSymmetry5status,
       "batteryBanksSymmetry5deltaVoltage": batteryBanksSymmetry5deltaVoltage,
       "batteryBanksSymmetry6enable": batteryBanksSymmetry6enable,
       "batteryBanksSymmetry6status": batteryBanksSymmetry6status,
       "batteryBanksSymmetry6deltaVoltage": batteryBanksSymmetry6deltaVoltage,
       "batteryBanksSymmetry7enable": batteryBanksSymmetry7enable,
       "batteryBanksSymmetry7status": batteryBanksSymmetry7status,
       "batteryBanksSymmetry7deltaVoltage": batteryBanksSymmetry7deltaVoltage,
       "batteryBanksSymmetry8enable": batteryBanksSymmetry8enable,
       "batteryBanksSymmetry8status": batteryBanksSymmetry8status,
       "batteryBanksSymmetry8deltaVoltage": batteryBanksSymmetry8deltaVoltage,
       "batteryBanksNumberOfStrings": batteryBanksNumberOfStrings,
       "batteryBanksExtensionIndex": batteryBanksExtensionIndex,
       "batteryBanksExtensionTable": batteryBanksExtensionTable,
       "batteryBanksExtensionEntry": batteryBanksExtensionEntry,
       "batteryBanksExtensionID": batteryBanksExtensionID,
       "batteryBanksExtensionSymmetryInputValue1": batteryBanksExtensionSymmetryInputValue1,
       "batteryBanksExtensionSymmetryInputValue2": batteryBanksExtensionSymmetryInputValue2,
       "batteryBanksExtensionSymmetryInputValue3": batteryBanksExtensionSymmetryInputValue3,
       "batteryBanksExtensionSymmetryInputValue4": batteryBanksExtensionSymmetryInputValue4,
       "batteryBanksExtensionSymmetryInputValue5": batteryBanksExtensionSymmetryInputValue5,
       "batteryBanksExtensionSymmetryInputValue6": batteryBanksExtensionSymmetryInputValue6,
       "batteryBanksExtensionSymmetryInputValue7": batteryBanksExtensionSymmetryInputValue7,
       "batteryBanksExtensionSymmetryInputValue8": batteryBanksExtensionSymmetryInputValue8,
       "batteryCapacityData": batteryCapacityData,
       "batteryTimeToDisconnect": batteryTimeToDisconnect,
       "batteryCapacityLeft": batteryCapacityLeft,
       "batteryCapacityUsed": batteryCapacityUsed,
       "batteryCapacityTotal": batteryCapacityTotal,
       "batteryQuality": batteryQuality,
       "batteryMonitorUnits": batteryMonitorUnits,
       "battmonNumberOfUnits": battmonNumberOfUnits,
       "battmonUnitsIndex": battmonUnitsIndex,
       "battmonUnitsTable": battmonUnitsTable,
       "battmonUnitsEntry": battmonUnitsEntry,
       "batteryMonitorID": batteryMonitorID,
       "batteryMonitorSymmetry1status": batteryMonitorSymmetry1status,
       "batteryMonitorSymmetry1InputValue": batteryMonitorSymmetry1InputValue,
       "batteryMonitorSymmetry2status": batteryMonitorSymmetry2status,
       "batteryMonitorSymmetry2InputValue": batteryMonitorSymmetry2InputValue,
       "batteryMonitorSymmetry3status": batteryMonitorSymmetry3status,
       "batteryMonitorSymmetry3InputValue": batteryMonitorSymmetry3InputValue,
       "batteryMonitorSymmetry4status": batteryMonitorSymmetry4status,
       "batteryMonitorSymmetry4InputValue": batteryMonitorSymmetry4InputValue,
       "batteryMonitorCurrentValue": batteryMonitorCurrentValue,
       "batteryMonitorFuseStatus": batteryMonitorFuseStatus,
       "batteryMonitorTemperature": batteryMonitorTemperature,
       "batteryHighMajorTempAlarmLevel": batteryHighMajorTempAlarmLevel,
       "batteryHighMinorTempAlarmLevel": batteryHighMinorTempAlarmLevel,
       "loadDistribution": loadDistribution,
       "loadDistributionCurrent": loadDistributionCurrent,
       "loadDistributionBreakerStatus": loadDistributionBreakerStatus,
       "loadDistributionLVDStatus": loadDistributionLVDStatus,
       "loadLVD1Enable": loadLVD1Enable,
       "loadLVD1Status": loadLVD1Status,
       "loadLVD1ConnectVoltage": loadLVD1ConnectVoltage,
       "loadLVD1DisconnectVoltage": loadLVD1DisconnectVoltage,
       "loadLVD2Enable": loadLVD2Enable,
       "loadLVD2Status": loadLVD2Status,
       "loadLVD2ConnectVoltage": loadLVD2ConnectVoltage,
       "loadLVD2DisconnectVoltage": loadLVD2DisconnectVoltage,
       "loadLVD3Enable": loadLVD3Enable,
       "loadLVD3Status": loadLVD3Status,
       "loadLVD3ConnectVoltage": loadLVD3ConnectVoltage,
       "loadLVD3DisconnectVoltage": loadLVD3DisconnectVoltage,
       "loadMonitorUnits": loadMonitorUnits,
       "loadmonitorNumberOfUnits": loadmonitorNumberOfUnits,
       "loadMonitorUnitsIndex": loadMonitorUnitsIndex,
       "loadMonitorUnitsTable": loadMonitorUnitsTable,
       "loadMonitorUnitsEntry": loadMonitorUnitsEntry,
       "loadMonitorID": loadMonitorID,
       "loadMonitorFuseStatus1": loadMonitorFuseStatus1,
       "loadMonitorCurrent1": loadMonitorCurrent1,
       "loadMonitorFuseStatus2": loadMonitorFuseStatus2,
       "loadMonitorCurrent2": loadMonitorCurrent2,
       "loadMonitorFuseStatus3": loadMonitorFuseStatus3,
       "loadMonitorCurrent3": loadMonitorCurrent3,
       "loadMonitorFuseStatus4": loadMonitorFuseStatus4,
       "loadMonitorCurrent4": loadMonitorCurrent4,
       "loadMonitorFuseStatus5": loadMonitorFuseStatus5,
       "loadMonitorCurrent5": loadMonitorCurrent5,
       "loadMonitorFuseStatus6": loadMonitorFuseStatus6,
       "loadMonitorCurrent6": loadMonitorCurrent6,
       "loadMonitorFuseStatus7": loadMonitorFuseStatus7,
       "loadMonitorCurrent7": loadMonitorCurrent7,
       "loadMonitorFuseStatus8": loadMonitorFuseStatus8,
       "loadMonitorCurrent8": loadMonitorCurrent8,
       "rectifier": rectifier,
       "rectifierInstalledRectifiers": rectifierInstalledRectifiers,
       "rectifierRectifiersActive": rectifierRectifiersActive,
       "rectifierTotalCurrent": rectifierTotalCurrent,
       "rectifierUtilization": rectifierUtilization,
       "rectifierStatus": rectifierStatus,
       "rectifierStatusNoIndex": rectifierStatusNoIndex,
       "rectifierStatusTable": rectifierStatusTable,
       "rectifierStatusEntry": rectifierStatusEntry,
       "rectifierStatusID": rectifierStatusID,
       "rectifierStatusStatus": rectifierStatusStatus,
       "rectifierStatusOutputCurrent": rectifierStatusOutputCurrent,
       "rectifierStatusOutputVoltage": rectifierStatusOutputVoltage,
       "rectifierStatusTemp": rectifierStatusTemp,
       "rectifierStatusType": rectifierStatusType,
       "rectifierStatusSKU": rectifierStatusSKU,
       "rectifierStatusSerialNo": rectifierStatusSerialNo,
       "rectifierStatusRevisionLevel": rectifierStatusRevisionLevel,
       "acDistribution": acDistribution,
       "acVoltage1": acVoltage1,
       "acVoltage2": acVoltage2,
       "acVoltage3": acVoltage3,
       "alarmGroup": alarmGroup,
       "alarmWellknownAlarms": alarmWellknownAlarms,
       "alarmMajorHighBattVolt": alarmMajorHighBattVolt,
       "alarmMinorHighBattVolt": alarmMinorHighBattVolt,
       "alarmMajorLowBattVolt": alarmMajorLowBattVolt,
       "alarmMinorLowBattVolt": alarmMinorLowBattVolt,
       "alarmMajorBatteryHighTemp": alarmMajorBatteryHighTemp,
       "alarmMinorBatteryHighTemp": alarmMinorBatteryHighTemp,
       "alarmBatteryDisconnectOpen": alarmBatteryDisconnectOpen,
       "alarmLVD1open": alarmLVD1open,
       "alarmLVD2open": alarmLVD2open,
       "alarmLVD3open": alarmLVD3open,
       "alarmACmains": alarmACmains,
       "alarmBatteryBreakerOpen": alarmBatteryBreakerOpen,
       "alarmDistributionBreakerOpen": alarmDistributionBreakerOpen,
       "alarmMajorRectifier": alarmMajorRectifier,
       "alarmMinorRectifier": alarmMinorRectifier,
       "alarmMajorBatterySymmetry": alarmMajorBatterySymmetry,
       "alarmMinorBatterySymmetry": alarmMinorBatterySymmetry,
       "alarmBatteryLifeEnded": alarmBatteryLifeEnded,
       "alarmBatteryTestmodeEntered": alarmBatteryTestmodeEntered,
       "alarmBatteryBoostmodeEntered": alarmBatteryBoostmodeEntered,
       "alarmIoUnitTemp1": alarmIoUnitTemp1,
       "alarmIoUnitTemp2": alarmIoUnitTemp2,
       "alarmIoUnitDeltaFanSpeed1": alarmIoUnitDeltaFanSpeed1,
       "alarmIoUnitDeltaFanSpeed2": alarmIoUnitDeltaFanSpeed2,
       "alarmMajorSolar": alarmMajorSolar,
       "alarmMinorSolar": alarmMinorSolar,
       "alarmMajorRectifierCapacity": alarmMajorRectifierCapacity,
       "alarmMinorRectifierCapacity": alarmMinorRectifierCapacity,
       "dcSystemTraps": dcSystemTraps,
       "alarmMajorHighBattVoltTrap": alarmMajorHighBattVoltTrap,
       "alarmMinorHighBattVoltTrap": alarmMinorHighBattVoltTrap,
       "alarmMajorLowBattVoltTrap": alarmMajorLowBattVoltTrap,
       "alarmMinorLowBattVoltTrap": alarmMinorLowBattVoltTrap,
       "alarmMajorBatteryHighTempTrap": alarmMajorBatteryHighTempTrap,
       "alarmMinorBatteryHighTempTrap": alarmMinorBatteryHighTempTrap,
       "alarmBatteryDisconnectOpenTrap": alarmBatteryDisconnectOpenTrap,
       "alarmLVD1openTrap": alarmLVD1openTrap,
       "alarmLVD2openTrap": alarmLVD2openTrap,
       "alarmLVD3openTrap": alarmLVD3openTrap,
       "alarmACmainsTrap": alarmACmainsTrap,
       "alarmBatteryBreakerOpenTrap": alarmBatteryBreakerOpenTrap,
       "alarmDistributionBreakerOpenTrap": alarmDistributionBreakerOpenTrap,
       "alarmMajorRectifierTrap": alarmMajorRectifierTrap,
       "alarmMinorRectifierTrap": alarmMinorRectifierTrap,
       "alarmMajorBatterySymmetryTrap": alarmMajorBatterySymmetryTrap,
       "alarmMinorBatterySymmetryTrap": alarmMinorBatterySymmetryTrap,
       "alarmBatteryLifeEndedTrap": alarmBatteryLifeEndedTrap,
       "alarmBatteryTestmodeEnteredTrap": alarmBatteryTestmodeEnteredTrap,
       "alarmBatteryBoostmodeEnteredTrap": alarmBatteryBoostmodeEnteredTrap,
       "alarmController1proginputTrap": alarmController1proginputTrap,
       "alarmController2proginputTrap": alarmController2proginputTrap,
       "alarmController3proginputTrap": alarmController3proginputTrap,
       "alarmController4proginputTrap": alarmController4proginputTrap,
       "alarmController5proginputTrap": alarmController5proginputTrap,
       "alarmController6proginputTrap": alarmController6proginputTrap,
       "alarmController7proginputTrap": alarmController7proginputTrap,
       "alarmController8proginputTrap": alarmController8proginputTrap,
       "infoHeartBeatTrap": infoHeartBeatTrap,
       "alarmIoUnitTemp1Trap": alarmIoUnitTemp1Trap,
       "alarmIoUnitTemp2Trap": alarmIoUnitTemp2Trap,
       "alarmIoUnitDeltaFanSpeed1Trap": alarmIoUnitDeltaFanSpeed1Trap,
       "alarmIoUnitDeltaFanSpeed2Trap": alarmIoUnitDeltaFanSpeed2Trap,
       "alarmIoUnit1proginputTrap": alarmIoUnit1proginputTrap,
       "alarmIoUnit2proginputTrap": alarmIoUnit2proginputTrap,
       "alarmIoUnit3proginputTrap": alarmIoUnit3proginputTrap,
       "alarmIoUnit4proginputTrap": alarmIoUnit4proginputTrap,
       "alarmIoUnit5proginputTrap": alarmIoUnit5proginputTrap,
       "alarmIoUnit6proginputTrap": alarmIoUnit6proginputTrap,
       "alarmIoUnit7proginputTrap": alarmIoUnit7proginputTrap,
       "alarmIoUnit8proginputTrap": alarmIoUnit8proginputTrap,
       "alarmIoUnit9proginputTrap": alarmIoUnit9proginputTrap,
       "alarmIoUnit10proginputTrap": alarmIoUnit10proginputTrap,
       "alarmIoUnit11proginputTrap": alarmIoUnit11proginputTrap,
       "alarmIoUnit12proginputTrap": alarmIoUnit12proginputTrap,
       "alarmIoUnit13proginputTrap": alarmIoUnit13proginputTrap,
       "alarmIoUnit14proginputTrap": alarmIoUnit14proginputTrap,
       "alarmMajorSolarChargerTrap": alarmMajorSolarChargerTrap,
       "alarmMinorSolarChargerTrap": alarmMinorSolarChargerTrap,
       "alarmMajorRectifierCapacityTrap": alarmMajorRectifierCapacityTrap,
       "alarmMinorRectifierCapacityTrap": alarmMinorRectifierCapacityTrap,
       "solarCharger": solarCharger,
       "solarChargerInstalledsolarChargers": solarChargerInstalledsolarChargers,
       "solarChargersActive": solarChargersActive,
       "solarChargerTotalCurrent": solarChargerTotalCurrent,
       "solarChargerUtilization": solarChargerUtilization,
       "solarChargerStatus": solarChargerStatus,
       "solarChargerStatusNoIndex": solarChargerStatusNoIndex,
       "solarChargerStatusTable": solarChargerStatusTable,
       "solarChargerStatusEntry": solarChargerStatusEntry,
       "solarChargerStatusID": solarChargerStatusID,
       "solarChargerStatusStatus": solarChargerStatusStatus,
       "solarChargerOutputCurrent": solarChargerOutputCurrent,
       "solarChargerOutputVoltage": solarChargerOutputVoltage,
       "solarChargerTemp": solarChargerTemp,
       "solarChargerType": solarChargerType,
       "solarChargerSKU": solarChargerSKU,
       "solarChargerSerialNo": solarChargerSerialNo,
       "solarChargerRevisionLevel": solarChargerRevisionLevel}
)
