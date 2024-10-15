# SNMP MIB module (OMNI-gx2RSW200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2RSW200-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:32 2024
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

(gx2Rsw200,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Rsw200")

(trapChangedObjectId,
 trapChangedValueDisplayString,
 trapChangedValueInteger,
 trapIdentifier,
 trapNETrapLastTrapTimeStamp,
 trapNetworkElemAdminState,
 trapNetworkElemAlarmStatus,
 trapNetworkElemAvailStatus,
 trapNetworkElemModelNumber,
 trapNetworkElemOperState,
 trapNetworkElemSerialNum,
 trapPerceivedSeverity,
 trapText) = mibBuilder.importSymbols(
    "NLSBBN-TRAPS-MIB",
    "trapChangedObjectId",
    "trapChangedValueDisplayString",
    "trapChangedValueInteger",
    "trapIdentifier",
    "trapNETrapLastTrapTimeStamp",
    "trapNetworkElemAdminState",
    "trapNetworkElemAlarmStatus",
    "trapNetworkElemAvailStatus",
    "trapNetworkElemModelNumber",
    "trapNetworkElemOperState",
    "trapNetworkElemSerialNum",
    "trapPerceivedSeverity",
    "trapText")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Float(Counter32):
    """Custom type Float based on Counter32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gx2Rsw200Descriptor_ObjectIdentity = ObjectIdentity
gx2Rsw200Descriptor = _Gx2Rsw200Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 1)
)
_Gx2Rsw200AnalogTable_Object = MibTable
gx2Rsw200AnalogTable = _Gx2Rsw200AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    gx2Rsw200AnalogTable.setStatus("mandatory")
_Gx2Rsw200AnalogEntry_Object = MibTableRow
gx2Rsw200AnalogEntry = _Gx2Rsw200AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1)
)
gx2Rsw200AnalogEntry.setIndexNames(
    (0, "OMNI-gx2RSW200-MIB", "gx2Rsw200AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rsw200AnalogEntry.setStatus("mandatory")


class _Gx2Rsw200AnalogTableIndex_Type(Integer32):
    """Custom type gx2Rsw200AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rsw200AnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Rsw200AnalogTableIndex_Object = MibTableColumn
gx2Rsw200AnalogTableIndex = _Gx2Rsw200AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 1),
    _Gx2Rsw200AnalogTableIndex_Type()
)
gx2Rsw200AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rsw200AnalogTableIndex.setStatus("mandatory")


class _Rsw200labelModTemp_Type(DisplayString):
    """Custom type rsw200labelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelModTemp_Type.__name__ = "DisplayString"
_Rsw200labelModTemp_Object = MibTableColumn
rsw200labelModTemp = _Rsw200labelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 2),
    _Rsw200labelModTemp_Type()
)
rsw200labelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelModTemp.setStatus("optional")


class _Rsw200uomModTemp_Type(DisplayString):
    """Custom type rsw200uomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200uomModTemp_Type.__name__ = "DisplayString"
_Rsw200uomModTemp_Object = MibTableColumn
rsw200uomModTemp = _Rsw200uomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 3),
    _Rsw200uomModTemp_Type()
)
rsw200uomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200uomModTemp.setStatus("optional")
_Rsw200majorHighModTemp_Type = Float
_Rsw200majorHighModTemp_Object = MibTableColumn
rsw200majorHighModTemp = _Rsw200majorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 4),
    _Rsw200majorHighModTemp_Type()
)
rsw200majorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200majorHighModTemp.setStatus("mandatory")
_Rsw200majorLowModTemp_Type = Float
_Rsw200majorLowModTemp_Object = MibTableColumn
rsw200majorLowModTemp = _Rsw200majorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 5),
    _Rsw200majorLowModTemp_Type()
)
rsw200majorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200majorLowModTemp.setStatus("mandatory")
_Rsw200minorHighModTemp_Type = Float
_Rsw200minorHighModTemp_Object = MibTableColumn
rsw200minorHighModTemp = _Rsw200minorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 6),
    _Rsw200minorHighModTemp_Type()
)
rsw200minorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200minorHighModTemp.setStatus("mandatory")
_Rsw200minorLowModTemp_Type = Float
_Rsw200minorLowModTemp_Object = MibTableColumn
rsw200minorLowModTemp = _Rsw200minorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 7),
    _Rsw200minorLowModTemp_Type()
)
rsw200minorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200minorLowModTemp.setStatus("mandatory")
_Rsw200currentValueModTemp_Type = Float
_Rsw200currentValueModTemp_Object = MibTableColumn
rsw200currentValueModTemp = _Rsw200currentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 8),
    _Rsw200currentValueModTemp_Type()
)
rsw200currentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200currentValueModTemp.setStatus("mandatory")


class _Rsw200stateFlagModTemp_Type(Integer32):
    """Custom type rsw200stateFlagModTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateFlagModTemp_Type.__name__ = "Integer32"
_Rsw200stateFlagModTemp_Object = MibTableColumn
rsw200stateFlagModTemp = _Rsw200stateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 9),
    _Rsw200stateFlagModTemp_Type()
)
rsw200stateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateFlagModTemp.setStatus("mandatory")
_Rsw200minValueModTemp_Type = Float
_Rsw200minValueModTemp_Object = MibTableColumn
rsw200minValueModTemp = _Rsw200minValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 10),
    _Rsw200minValueModTemp_Type()
)
rsw200minValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200minValueModTemp.setStatus("mandatory")
_Rsw200maxValueModTemp_Type = Float
_Rsw200maxValueModTemp_Object = MibTableColumn
rsw200maxValueModTemp = _Rsw200maxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 11),
    _Rsw200maxValueModTemp_Type()
)
rsw200maxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200maxValueModTemp.setStatus("mandatory")


class _Rsw200alarmStateModTemp_Type(Integer32):
    """Custom type rsw200alarmStateModTemp based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_Rsw200alarmStateModTemp_Type.__name__ = "Integer32"
_Rsw200alarmStateModTemp_Object = MibTableColumn
rsw200alarmStateModTemp = _Rsw200alarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 12),
    _Rsw200alarmStateModTemp_Type()
)
rsw200alarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200alarmStateModTemp.setStatus("mandatory")


class _Rsw200labelFanCurrent_Type(DisplayString):
    """Custom type rsw200labelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelFanCurrent_Type.__name__ = "DisplayString"
_Rsw200labelFanCurrent_Object = MibTableColumn
rsw200labelFanCurrent = _Rsw200labelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 13),
    _Rsw200labelFanCurrent_Type()
)
rsw200labelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelFanCurrent.setStatus("optional")


class _Rsw200uomFanCurrent_Type(DisplayString):
    """Custom type rsw200uomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200uomFanCurrent_Type.__name__ = "DisplayString"
_Rsw200uomFanCurrent_Object = MibTableColumn
rsw200uomFanCurrent = _Rsw200uomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 14),
    _Rsw200uomFanCurrent_Type()
)
rsw200uomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200uomFanCurrent.setStatus("optional")
_Rsw200majorHighFanCurrent_Type = Float
_Rsw200majorHighFanCurrent_Object = MibTableColumn
rsw200majorHighFanCurrent = _Rsw200majorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 15),
    _Rsw200majorHighFanCurrent_Type()
)
rsw200majorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200majorHighFanCurrent.setStatus("mandatory")
_Rsw200majorLowFanCurrent_Type = Float
_Rsw200majorLowFanCurrent_Object = MibTableColumn
rsw200majorLowFanCurrent = _Rsw200majorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 16),
    _Rsw200majorLowFanCurrent_Type()
)
rsw200majorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200majorLowFanCurrent.setStatus("mandatory")
_Rsw200minorHighFanCurrent_Type = Float
_Rsw200minorHighFanCurrent_Object = MibTableColumn
rsw200minorHighFanCurrent = _Rsw200minorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 17),
    _Rsw200minorHighFanCurrent_Type()
)
rsw200minorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200minorHighFanCurrent.setStatus("mandatory")
_Rsw200minorLowFanCurrent_Type = Float
_Rsw200minorLowFanCurrent_Object = MibTableColumn
rsw200minorLowFanCurrent = _Rsw200minorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 18),
    _Rsw200minorLowFanCurrent_Type()
)
rsw200minorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200minorLowFanCurrent.setStatus("mandatory")
_Rsw200currentValueFanCurrent_Type = Float
_Rsw200currentValueFanCurrent_Object = MibTableColumn
rsw200currentValueFanCurrent = _Rsw200currentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 19),
    _Rsw200currentValueFanCurrent_Type()
)
rsw200currentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200currentValueFanCurrent.setStatus("mandatory")


class _Rsw200stateFlagFanCurrent_Type(Integer32):
    """Custom type rsw200stateFlagFanCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateFlagFanCurrent_Type.__name__ = "Integer32"
_Rsw200stateFlagFanCurrent_Object = MibTableColumn
rsw200stateFlagFanCurrent = _Rsw200stateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 20),
    _Rsw200stateFlagFanCurrent_Type()
)
rsw200stateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateFlagFanCurrent.setStatus("mandatory")
_Rsw200minValueFanCurrent_Type = Float
_Rsw200minValueFanCurrent_Object = MibTableColumn
rsw200minValueFanCurrent = _Rsw200minValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 21),
    _Rsw200minValueFanCurrent_Type()
)
rsw200minValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200minValueFanCurrent.setStatus("mandatory")
_Rsw200maxValueFanCurrent_Type = Float
_Rsw200maxValueFanCurrent_Object = MibTableColumn
rsw200maxValueFanCurrent = _Rsw200maxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 22),
    _Rsw200maxValueFanCurrent_Type()
)
rsw200maxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200maxValueFanCurrent.setStatus("mandatory")


class _Rsw200alarmStateFanCurrent_Type(Integer32):
    """Custom type rsw200alarmStateFanCurrent based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_Rsw200alarmStateFanCurrent_Type.__name__ = "Integer32"
_Rsw200alarmStateFanCurrent_Object = MibTableColumn
rsw200alarmStateFanCurrent = _Rsw200alarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 2, 1, 23),
    _Rsw200alarmStateFanCurrent_Type()
)
rsw200alarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200alarmStateFanCurrent.setStatus("mandatory")
_Gx2Rsw200DigitalTable_Object = MibTable
gx2Rsw200DigitalTable = _Gx2Rsw200DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    gx2Rsw200DigitalTable.setStatus("mandatory")
_Gx2Rsw200DigitalEntry_Object = MibTableRow
gx2Rsw200DigitalEntry = _Gx2Rsw200DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2)
)
gx2Rsw200DigitalEntry.setIndexNames(
    (0, "OMNI-gx2RSW200-MIB", "gx2Rsw200DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rsw200DigitalEntry.setStatus("mandatory")


class _Gx2Rsw200DigitalTableIndex_Type(Integer32):
    """Custom type gx2Rsw200DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rsw200DigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Rsw200DigitalTableIndex_Object = MibTableColumn
gx2Rsw200DigitalTableIndex = _Gx2Rsw200DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 1),
    _Gx2Rsw200DigitalTableIndex_Type()
)
gx2Rsw200DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rsw200DigitalTableIndex.setStatus("mandatory")


class _Rsw200labelSwitchControl_Type(DisplayString):
    """Custom type rsw200labelSwitchControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelSwitchControl_Type.__name__ = "DisplayString"
_Rsw200labelSwitchControl_Object = MibTableColumn
rsw200labelSwitchControl = _Rsw200labelSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 2),
    _Rsw200labelSwitchControl_Type()
)
rsw200labelSwitchControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelSwitchControl.setStatus("optional")


class _Rsw200enumSwitchControl_Type(DisplayString):
    """Custom type rsw200enumSwitchControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200enumSwitchControl_Type.__name__ = "DisplayString"
_Rsw200enumSwitchControl_Object = MibTableColumn
rsw200enumSwitchControl = _Rsw200enumSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 3),
    _Rsw200enumSwitchControl_Type()
)
rsw200enumSwitchControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200enumSwitchControl.setStatus("optional")


class _Rsw200valueSwitchControl_Type(Integer32):
    """Custom type rsw200valueSwitchControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_Rsw200valueSwitchControl_Type.__name__ = "Integer32"
_Rsw200valueSwitchControl_Object = MibTableColumn
rsw200valueSwitchControl = _Rsw200valueSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 4),
    _Rsw200valueSwitchControl_Type()
)
rsw200valueSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw200valueSwitchControl.setStatus("mandatory")


class _Rsw200stateflagSwitchControl_Type(Integer32):
    """Custom type rsw200stateflagSwitchControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagSwitchControl_Type.__name__ = "Integer32"
_Rsw200stateflagSwitchControl_Object = MibTableColumn
rsw200stateflagSwitchControl = _Rsw200stateflagSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 5),
    _Rsw200stateflagSwitchControl_Type()
)
rsw200stateflagSwitchControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagSwitchControl.setStatus("mandatory")


class _Rsw200labelRevertMode_Type(DisplayString):
    """Custom type rsw200labelRevertMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelRevertMode_Type.__name__ = "DisplayString"
_Rsw200labelRevertMode_Object = MibTableColumn
rsw200labelRevertMode = _Rsw200labelRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 6),
    _Rsw200labelRevertMode_Type()
)
rsw200labelRevertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelRevertMode.setStatus("optional")


class _Rsw200enumRevertMode_Type(DisplayString):
    """Custom type rsw200enumRevertMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200enumRevertMode_Type.__name__ = "DisplayString"
_Rsw200enumRevertMode_Object = MibTableColumn
rsw200enumRevertMode = _Rsw200enumRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 7),
    _Rsw200enumRevertMode_Type()
)
rsw200enumRevertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200enumRevertMode.setStatus("optional")


class _Rsw200valueRevertMode_Type(Integer32):
    """Custom type rsw200valueRevertMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autorevert", 2),
          ("manual", 1),
          ("nonrevert", 3))
    )


_Rsw200valueRevertMode_Type.__name__ = "Integer32"
_Rsw200valueRevertMode_Object = MibTableColumn
rsw200valueRevertMode = _Rsw200valueRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 8),
    _Rsw200valueRevertMode_Type()
)
rsw200valueRevertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw200valueRevertMode.setStatus("mandatory")


class _Rsw200stateflagRevertMode_Type(Integer32):
    """Custom type rsw200stateflagRevertMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagRevertMode_Type.__name__ = "Integer32"
_Rsw200stateflagRevertMode_Object = MibTableColumn
rsw200stateflagRevertMode = _Rsw200stateflagRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 9),
    _Rsw200stateflagRevertMode_Type()
)
rsw200stateflagRevertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagRevertMode.setStatus("mandatory")


class _Rsw200labelRevertTime_Type(DisplayString):
    """Custom type rsw200labelRevertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelRevertTime_Type.__name__ = "DisplayString"
_Rsw200labelRevertTime_Object = MibTableColumn
rsw200labelRevertTime = _Rsw200labelRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 10),
    _Rsw200labelRevertTime_Type()
)
rsw200labelRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelRevertTime.setStatus("optional")


class _Rsw200enumRevertTime_Type(DisplayString):
    """Custom type rsw200enumRevertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200enumRevertTime_Type.__name__ = "DisplayString"
_Rsw200enumRevertTime_Object = MibTableColumn
rsw200enumRevertTime = _Rsw200enumRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 11),
    _Rsw200enumRevertTime_Type()
)
rsw200enumRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200enumRevertTime.setStatus("optional")


class _Rsw200valueRevertTime_Type(Integer32):
    """Custom type rsw200valueRevertTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sixhundredsec", 3),
          ("sixtysec", 2),
          ("tensec", 1))
    )


_Rsw200valueRevertTime_Type.__name__ = "Integer32"
_Rsw200valueRevertTime_Object = MibTableColumn
rsw200valueRevertTime = _Rsw200valueRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 12),
    _Rsw200valueRevertTime_Type()
)
rsw200valueRevertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw200valueRevertTime.setStatus("mandatory")


class _Rsw200stateflagRevertTime_Type(Integer32):
    """Custom type rsw200stateflagRevertTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagRevertTime_Type.__name__ = "Integer32"
_Rsw200stateflagRevertTime_Object = MibTableColumn
rsw200stateflagRevertTime = _Rsw200stateflagRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 13),
    _Rsw200stateflagRevertTime_Type()
)
rsw200stateflagRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagRevertTime.setStatus("mandatory")


class _Rsw200labelSwitchState_Type(DisplayString):
    """Custom type rsw200labelSwitchState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelSwitchState_Type.__name__ = "DisplayString"
_Rsw200labelSwitchState_Object = MibTableColumn
rsw200labelSwitchState = _Rsw200labelSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 14),
    _Rsw200labelSwitchState_Type()
)
rsw200labelSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelSwitchState.setStatus("optional")


class _Rsw200enumSwitchState_Type(DisplayString):
    """Custom type rsw200enumSwitchState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200enumSwitchState_Type.__name__ = "DisplayString"
_Rsw200enumSwitchState_Object = MibTableColumn
rsw200enumSwitchState = _Rsw200enumSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 15),
    _Rsw200enumSwitchState_Type()
)
rsw200enumSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200enumSwitchState.setStatus("optional")


class _Rsw200valueSwitchState_Type(Integer32):
    """Custom type rsw200valueSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_Rsw200valueSwitchState_Type.__name__ = "Integer32"
_Rsw200valueSwitchState_Object = MibTableColumn
rsw200valueSwitchState = _Rsw200valueSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 16),
    _Rsw200valueSwitchState_Type()
)
rsw200valueSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200valueSwitchState.setStatus("mandatory")


class _Rsw200stateflagSwitchState_Type(Integer32):
    """Custom type rsw200stateflagSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagSwitchState_Type.__name__ = "Integer32"
_Rsw200stateflagSwitchState_Object = MibTableColumn
rsw200stateflagSwitchState = _Rsw200stateflagSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 17),
    _Rsw200stateflagSwitchState_Type()
)
rsw200stateflagSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagSwitchState.setStatus("mandatory")


class _Rsw200labelPriStatus_Type(DisplayString):
    """Custom type rsw200labelPriStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelPriStatus_Type.__name__ = "DisplayString"
_Rsw200labelPriStatus_Object = MibTableColumn
rsw200labelPriStatus = _Rsw200labelPriStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 18),
    _Rsw200labelPriStatus_Type()
)
rsw200labelPriStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelPriStatus.setStatus("optional")


class _Rsw200enumPriStatus_Type(DisplayString):
    """Custom type rsw200enumPriStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200enumPriStatus_Type.__name__ = "DisplayString"
_Rsw200enumPriStatus_Object = MibTableColumn
rsw200enumPriStatus = _Rsw200enumPriStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 19),
    _Rsw200enumPriStatus_Type()
)
rsw200enumPriStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200enumPriStatus.setStatus("optional")


class _Rsw200valuePriStatus_Type(Integer32):
    """Custom type rsw200valuePriStatus based on Integer32"""
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
        *(("invalid", 3),
          ("open", 4),
          ("short", 1),
          ("valid", 2))
    )


_Rsw200valuePriStatus_Type.__name__ = "Integer32"
_Rsw200valuePriStatus_Object = MibTableColumn
rsw200valuePriStatus = _Rsw200valuePriStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 20),
    _Rsw200valuePriStatus_Type()
)
rsw200valuePriStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200valuePriStatus.setStatus("mandatory")


class _Rsw200stateflagPriStatus_Type(Integer32):
    """Custom type rsw200stateflagPriStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagPriStatus_Type.__name__ = "Integer32"
_Rsw200stateflagPriStatus_Object = MibTableColumn
rsw200stateflagPriStatus = _Rsw200stateflagPriStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 21),
    _Rsw200stateflagPriStatus_Type()
)
rsw200stateflagPriStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagPriStatus.setStatus("mandatory")


class _Rsw200labelSecStatus_Type(DisplayString):
    """Custom type rsw200labelSecStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelSecStatus_Type.__name__ = "DisplayString"
_Rsw200labelSecStatus_Object = MibTableColumn
rsw200labelSecStatus = _Rsw200labelSecStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 22),
    _Rsw200labelSecStatus_Type()
)
rsw200labelSecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelSecStatus.setStatus("optional")


class _Rsw200enumSecStatus_Type(DisplayString):
    """Custom type rsw200enumSecStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200enumSecStatus_Type.__name__ = "DisplayString"
_Rsw200enumSecStatus_Object = MibTableColumn
rsw200enumSecStatus = _Rsw200enumSecStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 23),
    _Rsw200enumSecStatus_Type()
)
rsw200enumSecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200enumSecStatus.setStatus("optional")


class _Rsw200valueSecStatus_Type(Integer32):
    """Custom type rsw200valueSecStatus based on Integer32"""
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
        *(("invalid", 3),
          ("open", 4),
          ("short", 1),
          ("valid", 2))
    )


_Rsw200valueSecStatus_Type.__name__ = "Integer32"
_Rsw200valueSecStatus_Object = MibTableColumn
rsw200valueSecStatus = _Rsw200valueSecStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 24),
    _Rsw200valueSecStatus_Type()
)
rsw200valueSecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200valueSecStatus.setStatus("mandatory")


class _Rsw200stateflagSecStatus_Type(Integer32):
    """Custom type rsw200stateflagSecStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagSecStatus_Type.__name__ = "Integer32"
_Rsw200stateflagSecStatus_Object = MibTableColumn
rsw200stateflagSecStatus = _Rsw200stateflagSecStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 25),
    _Rsw200stateflagSecStatus_Type()
)
rsw200stateflagSecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagSecStatus.setStatus("mandatory")


class _Rsw200labelFactoryDefault_Type(DisplayString):
    """Custom type rsw200labelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelFactoryDefault_Type.__name__ = "DisplayString"
_Rsw200labelFactoryDefault_Object = MibTableColumn
rsw200labelFactoryDefault = _Rsw200labelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 26),
    _Rsw200labelFactoryDefault_Type()
)
rsw200labelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelFactoryDefault.setStatus("optional")


class _Rsw200enumFactoryDefault_Type(DisplayString):
    """Custom type rsw200enumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200enumFactoryDefault_Type.__name__ = "DisplayString"
_Rsw200enumFactoryDefault_Object = MibTableColumn
rsw200enumFactoryDefault = _Rsw200enumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 27),
    _Rsw200enumFactoryDefault_Type()
)
rsw200enumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200enumFactoryDefault.setStatus("optional")


class _Rsw200valueFactoryDefault_Type(Integer32):
    """Custom type rsw200valueFactoryDefault based on Integer32"""
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


_Rsw200valueFactoryDefault_Type.__name__ = "Integer32"
_Rsw200valueFactoryDefault_Object = MibTableColumn
rsw200valueFactoryDefault = _Rsw200valueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 28),
    _Rsw200valueFactoryDefault_Type()
)
rsw200valueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw200valueFactoryDefault.setStatus("mandatory")


class _Rsw200stateflagFactoryDefault_Type(Integer32):
    """Custom type rsw200stateflagFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagFactoryDefault_Type.__name__ = "Integer32"
_Rsw200stateflagFactoryDefault_Object = MibTableColumn
rsw200stateflagFactoryDefault = _Rsw200stateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 3, 2, 29),
    _Rsw200stateflagFactoryDefault_Type()
)
rsw200stateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagFactoryDefault.setStatus("mandatory")
_Gx2Rsw200StatusTable_Object = MibTable
gx2Rsw200StatusTable = _Gx2Rsw200StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    gx2Rsw200StatusTable.setStatus("mandatory")
_Gx2Rsw200StatusEntry_Object = MibTableRow
gx2Rsw200StatusEntry = _Gx2Rsw200StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3)
)
gx2Rsw200StatusEntry.setIndexNames(
    (0, "OMNI-gx2RSW200-MIB", "gx2Rsw200StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rsw200StatusEntry.setStatus("mandatory")


class _Gx2Rsw200StatusTableIndex_Type(Integer32):
    """Custom type gx2Rsw200StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rsw200StatusTableIndex_Type.__name__ = "Integer32"
_Gx2Rsw200StatusTableIndex_Object = MibTableColumn
gx2Rsw200StatusTableIndex = _Gx2Rsw200StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 1),
    _Gx2Rsw200StatusTableIndex_Type()
)
gx2Rsw200StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rsw200StatusTableIndex.setStatus("mandatory")


class _Rsw200labelBoot_Type(DisplayString):
    """Custom type rsw200labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelBoot_Type.__name__ = "DisplayString"
_Rsw200labelBoot_Object = MibTableColumn
rsw200labelBoot = _Rsw200labelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 2),
    _Rsw200labelBoot_Type()
)
rsw200labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelBoot.setStatus("optional")


class _Rsw200valueBoot_Type(Integer32):
    """Custom type rsw200valueBoot based on Integer32"""
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
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Rsw200valueBoot_Type.__name__ = "Integer32"
_Rsw200valueBoot_Object = MibTableColumn
rsw200valueBoot = _Rsw200valueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 3),
    _Rsw200valueBoot_Type()
)
rsw200valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200valueBoot.setStatus("mandatory")


class _Rsw200stateflagBoot_Type(Integer32):
    """Custom type rsw200stateflagBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagBoot_Type.__name__ = "Integer32"
_Rsw200stateflagBoot_Object = MibTableColumn
rsw200stateflagBoot = _Rsw200stateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 4),
    _Rsw200stateflagBoot_Type()
)
rsw200stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagBoot.setStatus("mandatory")


class _Rsw200labelFlash_Type(DisplayString):
    """Custom type rsw200labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelFlash_Type.__name__ = "DisplayString"
_Rsw200labelFlash_Object = MibTableColumn
rsw200labelFlash = _Rsw200labelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 5),
    _Rsw200labelFlash_Type()
)
rsw200labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelFlash.setStatus("optional")


class _Rsw200valueFlash_Type(Integer32):
    """Custom type rsw200valueFlash based on Integer32"""
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
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Rsw200valueFlash_Type.__name__ = "Integer32"
_Rsw200valueFlash_Object = MibTableColumn
rsw200valueFlash = _Rsw200valueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 6),
    _Rsw200valueFlash_Type()
)
rsw200valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200valueFlash.setStatus("mandatory")


class _Rsw200stateflagFlash_Type(Integer32):
    """Custom type rsw200stateflagFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagFlash_Type.__name__ = "Integer32"
_Rsw200stateflagFlash_Object = MibTableColumn
rsw200stateflagFlash = _Rsw200stateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 7),
    _Rsw200stateflagFlash_Type()
)
rsw200stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagFlash.setStatus("mandatory")


class _Rsw200labelFactoryDataCRC_Type(DisplayString):
    """Custom type rsw200labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelFactoryDataCRC_Type.__name__ = "DisplayString"
_Rsw200labelFactoryDataCRC_Object = MibTableColumn
rsw200labelFactoryDataCRC = _Rsw200labelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 8),
    _Rsw200labelFactoryDataCRC_Type()
)
rsw200labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelFactoryDataCRC.setStatus("optional")


class _Rsw200valueFactoryDataCRC_Type(Integer32):
    """Custom type rsw200valueFactoryDataCRC based on Integer32"""
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
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Rsw200valueFactoryDataCRC_Type.__name__ = "Integer32"
_Rsw200valueFactoryDataCRC_Object = MibTableColumn
rsw200valueFactoryDataCRC = _Rsw200valueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 9),
    _Rsw200valueFactoryDataCRC_Type()
)
rsw200valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200valueFactoryDataCRC.setStatus("mandatory")


class _Rsw200stateflagFactoryDataCRC_Type(Integer32):
    """Custom type rsw200stateflagFactoryDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Rsw200stateflagFactoryDataCRC_Object = MibTableColumn
rsw200stateflagFactoryDataCRC = _Rsw200stateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 10),
    _Rsw200stateflagFactoryDataCRC_Type()
)
rsw200stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagFactoryDataCRC.setStatus("mandatory")


class _Rsw200labelAlarmDataCrc_Type(DisplayString):
    """Custom type rsw200labelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelAlarmDataCrc_Type.__name__ = "DisplayString"
_Rsw200labelAlarmDataCrc_Object = MibTableColumn
rsw200labelAlarmDataCrc = _Rsw200labelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 11),
    _Rsw200labelAlarmDataCrc_Type()
)
rsw200labelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelAlarmDataCrc.setStatus("optional")


class _Rsw200valueAlarmDataCrc_Type(Integer32):
    """Custom type rsw200valueAlarmDataCrc based on Integer32"""
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
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Rsw200valueAlarmDataCrc_Type.__name__ = "Integer32"
_Rsw200valueAlarmDataCrc_Object = MibTableColumn
rsw200valueAlarmDataCrc = _Rsw200valueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 12),
    _Rsw200valueAlarmDataCrc_Type()
)
rsw200valueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200valueAlarmDataCrc.setStatus("mandatory")


class _Rsw200stateflagAlarmDataCrc_Type(Integer32):
    """Custom type rsw200stateflagAlarmDataCrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Rsw200stateflagAlarmDataCrc_Object = MibTableColumn
rsw200stateflagAlarmDataCrc = _Rsw200stateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 13),
    _Rsw200stateflagAlarmDataCrc_Type()
)
rsw200stateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagAlarmDataCrc.setStatus("mandatory")


class _Rsw200labelRFSignalStatus_Type(DisplayString):
    """Custom type rsw200labelRFSignalStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelRFSignalStatus_Type.__name__ = "DisplayString"
_Rsw200labelRFSignalStatus_Object = MibTableColumn
rsw200labelRFSignalStatus = _Rsw200labelRFSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 14),
    _Rsw200labelRFSignalStatus_Type()
)
rsw200labelRFSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelRFSignalStatus.setStatus("optional")


class _Rsw200valueRFSignalStatus_Type(Integer32):
    """Custom type rsw200valueRFSignalStatus based on Integer32"""
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
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Rsw200valueRFSignalStatus_Type.__name__ = "Integer32"
_Rsw200valueRFSignalStatus_Object = MibTableColumn
rsw200valueRFSignalStatus = _Rsw200valueRFSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 15),
    _Rsw200valueRFSignalStatus_Type()
)
rsw200valueRFSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200valueRFSignalStatus.setStatus("mandatory")


class _Rsw200stateflagRFSignalStatus_Type(Integer32):
    """Custom type rsw200stateflagRFSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagRFSignalStatus_Type.__name__ = "Integer32"
_Rsw200stateflagRFSignalStatus_Object = MibTableColumn
rsw200stateflagRFSignalStatus = _Rsw200stateflagRFSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 16),
    _Rsw200stateflagRFSignalStatus_Type()
)
rsw200stateflagRFSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagRFSignalStatus.setStatus("mandatory")


class _Rsw200labelPriActiveStatus_Type(DisplayString):
    """Custom type rsw200labelPriActiveStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200labelPriActiveStatus_Type.__name__ = "DisplayString"
_Rsw200labelPriActiveStatus_Object = MibTableColumn
rsw200labelPriActiveStatus = _Rsw200labelPriActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 17),
    _Rsw200labelPriActiveStatus_Type()
)
rsw200labelPriActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200labelPriActiveStatus.setStatus("optional")


class _Rsw200valuePriActiveStatus_Type(Integer32):
    """Custom type rsw200valuePriActiveStatus based on Integer32"""
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
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_Rsw200valuePriActiveStatus_Type.__name__ = "Integer32"
_Rsw200valuePriActiveStatus_Object = MibTableColumn
rsw200valuePriActiveStatus = _Rsw200valuePriActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 18),
    _Rsw200valuePriActiveStatus_Type()
)
rsw200valuePriActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200valuePriActiveStatus.setStatus("mandatory")


class _Rsw200stateflagPriActiveStatus_Type(Integer32):
    """Custom type rsw200stateflagPriActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_Rsw200stateflagPriActiveStatus_Type.__name__ = "Integer32"
_Rsw200stateflagPriActiveStatus_Object = MibTableColumn
rsw200stateflagPriActiveStatus = _Rsw200stateflagPriActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 4, 3, 19),
    _Rsw200stateflagPriActiveStatus_Type()
)
rsw200stateflagPriActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200stateflagPriActiveStatus.setStatus("mandatory")
_Gx2Rsw200FactoryTable_Object = MibTable
gx2Rsw200FactoryTable = _Gx2Rsw200FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5)
)
if mibBuilder.loadTexts:
    gx2Rsw200FactoryTable.setStatus("mandatory")
_Gx2Rsw200FactoryEntry_Object = MibTableRow
gx2Rsw200FactoryEntry = _Gx2Rsw200FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4)
)
gx2Rsw200FactoryEntry.setIndexNames(
    (0, "OMNI-gx2RSW200-MIB", "gx2Rsw200FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rsw200FactoryEntry.setStatus("mandatory")


class _Gx2Rsw200FactoryTableIndex_Type(Integer32):
    """Custom type gx2Rsw200FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rsw200FactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Rsw200FactoryTableIndex_Object = MibTableColumn
gx2Rsw200FactoryTableIndex = _Gx2Rsw200FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 1),
    _Gx2Rsw200FactoryTableIndex_Type()
)
gx2Rsw200FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rsw200FactoryTableIndex.setStatus("mandatory")
_Rsw200bootControlByte_Type = Integer32
_Rsw200bootControlByte_Object = MibTableColumn
rsw200bootControlByte = _Rsw200bootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 2),
    _Rsw200bootControlByte_Type()
)
rsw200bootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200bootControlByte.setStatus("mandatory")
_Rsw200bootStatusByte_Type = Integer32
_Rsw200bootStatusByte_Object = MibTableColumn
rsw200bootStatusByte = _Rsw200bootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 3),
    _Rsw200bootStatusByte_Type()
)
rsw200bootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200bootStatusByte.setStatus("mandatory")
_Rsw200bank1CRC_Type = Integer32
_Rsw200bank1CRC_Object = MibTableColumn
rsw200bank1CRC = _Rsw200bank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 4),
    _Rsw200bank1CRC_Type()
)
rsw200bank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200bank1CRC.setStatus("mandatory")
_Rsw200bank2CRC_Type = Integer32
_Rsw200bank2CRC_Object = MibTableColumn
rsw200bank2CRC = _Rsw200bank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 5),
    _Rsw200bank2CRC_Type()
)
rsw200bank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200bank2CRC.setStatus("mandatory")
_Rsw200prgEEPROMByte_Type = Integer32
_Rsw200prgEEPROMByte_Object = MibTableColumn
rsw200prgEEPROMByte = _Rsw200prgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 6),
    _Rsw200prgEEPROMByte_Type()
)
rsw200prgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200prgEEPROMByte.setStatus("mandatory")
_Rsw200factoryCRC_Type = Integer32
_Rsw200factoryCRC_Object = MibTableColumn
rsw200factoryCRC = _Rsw200factoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 7),
    _Rsw200factoryCRC_Type()
)
rsw200factoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200factoryCRC.setStatus("mandatory")


class _Rsw200calculateCRC_Type(Integer32):
    """Custom type rsw200calculateCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("factory", 1),
          ("na", 3))
    )


_Rsw200calculateCRC_Type.__name__ = "Integer32"
_Rsw200calculateCRC_Object = MibTableColumn
rsw200calculateCRC = _Rsw200calculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 8),
    _Rsw200calculateCRC_Type()
)
rsw200calculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200calculateCRC.setStatus("mandatory")
_Rsw200hourMeter_Type = Integer32
_Rsw200hourMeter_Object = MibTableColumn
rsw200hourMeter = _Rsw200hourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 9),
    _Rsw200hourMeter_Type()
)
rsw200hourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200hourMeter.setStatus("mandatory")
_Rsw200flashPrgCntA_Type = Integer32
_Rsw200flashPrgCntA_Object = MibTableColumn
rsw200flashPrgCntA = _Rsw200flashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 10),
    _Rsw200flashPrgCntA_Type()
)
rsw200flashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200flashPrgCntA.setStatus("mandatory")
_Rsw200flashPrgCntB_Type = Integer32
_Rsw200flashPrgCntB_Object = MibTableColumn
rsw200flashPrgCntB = _Rsw200flashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 11),
    _Rsw200flashPrgCntB_Type()
)
rsw200flashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200flashPrgCntB.setStatus("mandatory")


class _Rsw200flashBankARev_Type(DisplayString):
    """Custom type rsw200flashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200flashBankARev_Type.__name__ = "DisplayString"
_Rsw200flashBankARev_Object = MibTableColumn
rsw200flashBankARev = _Rsw200flashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 12),
    _Rsw200flashBankARev_Type()
)
rsw200flashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200flashBankARev.setStatus("mandatory")


class _Rsw200flashBankBRev_Type(DisplayString):
    """Custom type rsw200flashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw200flashBankBRev_Type.__name__ = "DisplayString"
_Rsw200flashBankBRev_Object = MibTableColumn
rsw200flashBankBRev = _Rsw200flashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 5, 4, 13),
    _Rsw200flashBankBRev_Type()
)
rsw200flashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw200flashBankBRev.setStatus("mandatory")
_Gx2Rsw200bHoldTimeTable_Object = MibTable
gx2Rsw200bHoldTimeTable = _Gx2Rsw200bHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 6)
)
if mibBuilder.loadTexts:
    gx2Rsw200bHoldTimeTable.setStatus("mandatory")
_Gx2Rsw200bHoldTimeEntry_Object = MibTableRow
gx2Rsw200bHoldTimeEntry = _Gx2Rsw200bHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 6, 5)
)
gx2Rsw200bHoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2RSW200-MIB", "rxgx2Rsw200bHoldTimeTableIndex"),
    (0, "OMNI-gx2RSW200-MIB", "rxgx2Rsw200bHoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2Rsw200bHoldTimeEntry.setStatus("mandatory")


class _Rxgx2Rsw200bHoldTimeTableIndex_Type(Integer32):
    """Custom type rxgx2Rsw200bHoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Rsw200bHoldTimeTableIndex_Type.__name__ = "Integer32"
_Rxgx2Rsw200bHoldTimeTableIndex_Object = MibTableColumn
rxgx2Rsw200bHoldTimeTableIndex = _Rxgx2Rsw200bHoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 6, 5, 1),
    _Rxgx2Rsw200bHoldTimeTableIndex_Type()
)
rxgx2Rsw200bHoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Rsw200bHoldTimeTableIndex.setStatus("mandatory")


class _Rxgx2Rsw200bHoldTimeSpecIndex_Type(Integer32):
    """Custom type rxgx2Rsw200bHoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Rsw200bHoldTimeSpecIndex_Type.__name__ = "Integer32"
_Rxgx2Rsw200bHoldTimeSpecIndex_Object = MibTableColumn
rxgx2Rsw200bHoldTimeSpecIndex = _Rxgx2Rsw200bHoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 6, 5, 2),
    _Rxgx2Rsw200bHoldTimeSpecIndex_Type()
)
rxgx2Rsw200bHoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Rsw200bHoldTimeSpecIndex.setStatus("mandatory")
_Rxgx2Rsw200bHoldTimeData_Type = Integer32
_Rxgx2Rsw200bHoldTimeData_Object = MibTableColumn
rxgx2Rsw200bHoldTimeData = _Rxgx2Rsw200bHoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 6, 5, 3),
    _Rxgx2Rsw200bHoldTimeData_Type()
)
rxgx2Rsw200bHoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxgx2Rsw200bHoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapRSW200ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 1)
)
trapRSW200ConfigChangeInteger.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200ConfigChangeInteger.setStatus(
        ""
    )

trapRSW200ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 2)
)
trapRSW200ConfigChangeDisplayString.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueDisplayString"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200ConfigChangeDisplayString.setStatus(
        ""
    )

trapRSW200RFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 3)
)
trapRSW200RFInputAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200RFInputAlarm.setStatus(
        ""
    )

trapRSW200FanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 4)
)
trapRSW200FanCurrentAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200FanCurrentAlarm.setStatus(
        ""
    )

trapRSW200ModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 5)
)
trapRSW200ModuleTempAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200ModuleTempAlarm.setStatus(
        ""
    )

trapRSW200FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 6)
)
trapRSW200FlashAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200FlashAlarm.setStatus(
        ""
    )

trapRSW200BankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 7)
)
trapRSW200BankBootAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200BankBootAlarm.setStatus(
        ""
    )

trapRSW200AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 8)
)
trapRSW200AlarmDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200AlarmDataCRCAlarm.setStatus(
        ""
    )

trapRSW200FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 9)
)
trapRSW200FactoryDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200FactoryDataCRCAlarm.setStatus(
        ""
    )

trapRSW200InputSwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 10)
)
trapRSW200InputSwitchedAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200InputSwitchedAlarm.setStatus(
        ""
    )

trapRSW200ResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 11)
)
trapRSW200ResetFactoryDefaultAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200ResetFactoryDefaultAlarm.setStatus(
        ""
    )

trapRSW200SecondaryInputActiveAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8, 0, 12)
)
trapRSW200SecondaryInputActiveAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRSW200SecondaryInputActiveAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2RSW200-MIB",
    **{"Float": Float,
       "trapRSW200ConfigChangeInteger": trapRSW200ConfigChangeInteger,
       "trapRSW200ConfigChangeDisplayString": trapRSW200ConfigChangeDisplayString,
       "trapRSW200RFInputAlarm": trapRSW200RFInputAlarm,
       "trapRSW200FanCurrentAlarm": trapRSW200FanCurrentAlarm,
       "trapRSW200ModuleTempAlarm": trapRSW200ModuleTempAlarm,
       "trapRSW200FlashAlarm": trapRSW200FlashAlarm,
       "trapRSW200BankBootAlarm": trapRSW200BankBootAlarm,
       "trapRSW200AlarmDataCRCAlarm": trapRSW200AlarmDataCRCAlarm,
       "trapRSW200FactoryDataCRCAlarm": trapRSW200FactoryDataCRCAlarm,
       "trapRSW200InputSwitchedAlarm": trapRSW200InputSwitchedAlarm,
       "trapRSW200ResetFactoryDefaultAlarm": trapRSW200ResetFactoryDefaultAlarm,
       "trapRSW200SecondaryInputActiveAlarm": trapRSW200SecondaryInputActiveAlarm,
       "gx2Rsw200Descriptor": gx2Rsw200Descriptor,
       "gx2Rsw200AnalogTable": gx2Rsw200AnalogTable,
       "gx2Rsw200AnalogEntry": gx2Rsw200AnalogEntry,
       "gx2Rsw200AnalogTableIndex": gx2Rsw200AnalogTableIndex,
       "rsw200labelModTemp": rsw200labelModTemp,
       "rsw200uomModTemp": rsw200uomModTemp,
       "rsw200majorHighModTemp": rsw200majorHighModTemp,
       "rsw200majorLowModTemp": rsw200majorLowModTemp,
       "rsw200minorHighModTemp": rsw200minorHighModTemp,
       "rsw200minorLowModTemp": rsw200minorLowModTemp,
       "rsw200currentValueModTemp": rsw200currentValueModTemp,
       "rsw200stateFlagModTemp": rsw200stateFlagModTemp,
       "rsw200minValueModTemp": rsw200minValueModTemp,
       "rsw200maxValueModTemp": rsw200maxValueModTemp,
       "rsw200alarmStateModTemp": rsw200alarmStateModTemp,
       "rsw200labelFanCurrent": rsw200labelFanCurrent,
       "rsw200uomFanCurrent": rsw200uomFanCurrent,
       "rsw200majorHighFanCurrent": rsw200majorHighFanCurrent,
       "rsw200majorLowFanCurrent": rsw200majorLowFanCurrent,
       "rsw200minorHighFanCurrent": rsw200minorHighFanCurrent,
       "rsw200minorLowFanCurrent": rsw200minorLowFanCurrent,
       "rsw200currentValueFanCurrent": rsw200currentValueFanCurrent,
       "rsw200stateFlagFanCurrent": rsw200stateFlagFanCurrent,
       "rsw200minValueFanCurrent": rsw200minValueFanCurrent,
       "rsw200maxValueFanCurrent": rsw200maxValueFanCurrent,
       "rsw200alarmStateFanCurrent": rsw200alarmStateFanCurrent,
       "gx2Rsw200DigitalTable": gx2Rsw200DigitalTable,
       "gx2Rsw200DigitalEntry": gx2Rsw200DigitalEntry,
       "gx2Rsw200DigitalTableIndex": gx2Rsw200DigitalTableIndex,
       "rsw200labelSwitchControl": rsw200labelSwitchControl,
       "rsw200enumSwitchControl": rsw200enumSwitchControl,
       "rsw200valueSwitchControl": rsw200valueSwitchControl,
       "rsw200stateflagSwitchControl": rsw200stateflagSwitchControl,
       "rsw200labelRevertMode": rsw200labelRevertMode,
       "rsw200enumRevertMode": rsw200enumRevertMode,
       "rsw200valueRevertMode": rsw200valueRevertMode,
       "rsw200stateflagRevertMode": rsw200stateflagRevertMode,
       "rsw200labelRevertTime": rsw200labelRevertTime,
       "rsw200enumRevertTime": rsw200enumRevertTime,
       "rsw200valueRevertTime": rsw200valueRevertTime,
       "rsw200stateflagRevertTime": rsw200stateflagRevertTime,
       "rsw200labelSwitchState": rsw200labelSwitchState,
       "rsw200enumSwitchState": rsw200enumSwitchState,
       "rsw200valueSwitchState": rsw200valueSwitchState,
       "rsw200stateflagSwitchState": rsw200stateflagSwitchState,
       "rsw200labelPriStatus": rsw200labelPriStatus,
       "rsw200enumPriStatus": rsw200enumPriStatus,
       "rsw200valuePriStatus": rsw200valuePriStatus,
       "rsw200stateflagPriStatus": rsw200stateflagPriStatus,
       "rsw200labelSecStatus": rsw200labelSecStatus,
       "rsw200enumSecStatus": rsw200enumSecStatus,
       "rsw200valueSecStatus": rsw200valueSecStatus,
       "rsw200stateflagSecStatus": rsw200stateflagSecStatus,
       "rsw200labelFactoryDefault": rsw200labelFactoryDefault,
       "rsw200enumFactoryDefault": rsw200enumFactoryDefault,
       "rsw200valueFactoryDefault": rsw200valueFactoryDefault,
       "rsw200stateflagFactoryDefault": rsw200stateflagFactoryDefault,
       "gx2Rsw200StatusTable": gx2Rsw200StatusTable,
       "gx2Rsw200StatusEntry": gx2Rsw200StatusEntry,
       "gx2Rsw200StatusTableIndex": gx2Rsw200StatusTableIndex,
       "rsw200labelBoot": rsw200labelBoot,
       "rsw200valueBoot": rsw200valueBoot,
       "rsw200stateflagBoot": rsw200stateflagBoot,
       "rsw200labelFlash": rsw200labelFlash,
       "rsw200valueFlash": rsw200valueFlash,
       "rsw200stateflagFlash": rsw200stateflagFlash,
       "rsw200labelFactoryDataCRC": rsw200labelFactoryDataCRC,
       "rsw200valueFactoryDataCRC": rsw200valueFactoryDataCRC,
       "rsw200stateflagFactoryDataCRC": rsw200stateflagFactoryDataCRC,
       "rsw200labelAlarmDataCrc": rsw200labelAlarmDataCrc,
       "rsw200valueAlarmDataCrc": rsw200valueAlarmDataCrc,
       "rsw200stateflagAlarmDataCrc": rsw200stateflagAlarmDataCrc,
       "rsw200labelRFSignalStatus": rsw200labelRFSignalStatus,
       "rsw200valueRFSignalStatus": rsw200valueRFSignalStatus,
       "rsw200stateflagRFSignalStatus": rsw200stateflagRFSignalStatus,
       "rsw200labelPriActiveStatus": rsw200labelPriActiveStatus,
       "rsw200valuePriActiveStatus": rsw200valuePriActiveStatus,
       "rsw200stateflagPriActiveStatus": rsw200stateflagPriActiveStatus,
       "gx2Rsw200FactoryTable": gx2Rsw200FactoryTable,
       "gx2Rsw200FactoryEntry": gx2Rsw200FactoryEntry,
       "gx2Rsw200FactoryTableIndex": gx2Rsw200FactoryTableIndex,
       "rsw200bootControlByte": rsw200bootControlByte,
       "rsw200bootStatusByte": rsw200bootStatusByte,
       "rsw200bank1CRC": rsw200bank1CRC,
       "rsw200bank2CRC": rsw200bank2CRC,
       "rsw200prgEEPROMByte": rsw200prgEEPROMByte,
       "rsw200factoryCRC": rsw200factoryCRC,
       "rsw200calculateCRC": rsw200calculateCRC,
       "rsw200hourMeter": rsw200hourMeter,
       "rsw200flashPrgCntA": rsw200flashPrgCntA,
       "rsw200flashPrgCntB": rsw200flashPrgCntB,
       "rsw200flashBankARev": rsw200flashBankARev,
       "rsw200flashBankBRev": rsw200flashBankBRev,
       "gx2Rsw200bHoldTimeTable": gx2Rsw200bHoldTimeTable,
       "gx2Rsw200bHoldTimeEntry": gx2Rsw200bHoldTimeEntry,
       "rxgx2Rsw200bHoldTimeTableIndex": rxgx2Rsw200bHoldTimeTableIndex,
       "rxgx2Rsw200bHoldTimeSpecIndex": rxgx2Rsw200bHoldTimeSpecIndex,
       "rxgx2Rsw200bHoldTimeData": rxgx2Rsw200bHoldTimeData}
)
