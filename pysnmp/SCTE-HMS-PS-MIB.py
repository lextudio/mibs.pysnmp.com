# SNMP MIB module (SCTE-HMS-PS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCTE-HMS-PS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:07 2024
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

(psIdent,) = mibBuilder.importSymbols(
    "SCTE-HMS-ROOTS",
    "psIdent")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PsMonitored_Type(Integer32):
    """Custom type psMonitored based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PsMonitored_Type.__name__ = "Integer32"
_PsMonitored_Object = MibScalar
psMonitored = _PsMonitored_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 1),
    _PsMonitored_Type()
)
psMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMonitored.setStatus("mandatory")
_PsDeviceTable_Object = MibTable
psDeviceTable = _PsDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2)
)
if mibBuilder.loadTexts:
    psDeviceTable.setStatus("mandatory")
_PsDeviceEntry_Object = MibTableRow
psDeviceEntry = _PsDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1)
)
psDeviceEntry.setIndexNames(
    (0, "SCTE-HMS-PS-MIB", "psDeviceAddress"),
)
if mibBuilder.loadTexts:
    psDeviceEntry.setStatus("mandatory")


class _PsDeviceAddress_Type(Integer32):
    """Custom type psDeviceAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PsDeviceAddress_Type.__name__ = "Integer32"
_PsDeviceAddress_Object = MibTableColumn
psDeviceAddress = _PsDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 1),
    _PsDeviceAddress_Type()
)
psDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDeviceAddress.setStatus("mandatory")


class _PsProtocolVersion_Type(Integer32):
    """Custom type psProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_PsProtocolVersion_Type.__name__ = "Integer32"
_PsProtocolVersion_Object = MibTableColumn
psProtocolVersion = _PsProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 2),
    _PsProtocolVersion_Type()
)
psProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProtocolVersion.setStatus("mandatory")


class _PsSoftwareVersion_Type(DisplayString):
    """Custom type psSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PsSoftwareVersion_Type.__name__ = "DisplayString"
_PsSoftwareVersion_Object = MibTableColumn
psSoftwareVersion = _PsSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 3),
    _PsSoftwareVersion_Type()
)
psSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSoftwareVersion.setStatus("mandatory")


class _PsDeviceId_Type(OctetString):
    """Custom type psDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_PsDeviceId_Type.__name__ = "OctetString"
_PsDeviceId_Object = MibTableColumn
psDeviceId = _PsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 4),
    _PsDeviceId_Type()
)
psDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDeviceId.setStatus("mandatory")


class _PsBatteries_Type(Integer32):
    """Custom type psBatteries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PsBatteries_Type.__name__ = "Integer32"
_PsBatteries_Object = MibTableColumn
psBatteries = _PsBatteries_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 5),
    _PsBatteries_Type()
)
psBatteries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteries.setStatus("mandatory")


class _PsBatteryStrings_Type(Integer32):
    """Custom type psBatteryStrings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PsBatteryStrings_Type.__name__ = "Integer32"
_PsBatteryStrings_Object = MibTableColumn
psBatteryStrings = _PsBatteryStrings_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 6),
    _PsBatteryStrings_Type()
)
psBatteryStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryStrings.setStatus("mandatory")


class _PsTempSensors_Type(Integer32):
    """Custom type psTempSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PsTempSensors_Type.__name__ = "Integer32"
_PsTempSensors_Object = MibTableColumn
psTempSensors = _PsTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 7),
    _PsTempSensors_Type()
)
psTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTempSensors.setStatus("mandatory")


class _PsOutputs_Type(Integer32):
    """Custom type psOutputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PsOutputs_Type.__name__ = "Integer32"
_PsOutputs_Object = MibTableColumn
psOutputs = _PsOutputs_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 8),
    _PsOutputs_Type()
)
psOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psOutputs.setStatus("mandatory")
_PsBatteryCurrentSupport_Type = Integer32
_PsBatteryCurrentSupport_Object = MibTableColumn
psBatteryCurrentSupport = _PsBatteryCurrentSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 9),
    _PsBatteryCurrentSupport_Type()
)
psBatteryCurrentSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryCurrentSupport.setStatus("mandatory")
_PsFloatCurrentSupport_Type = Integer32
_PsFloatCurrentSupport_Object = MibTableColumn
psFloatCurrentSupport = _PsFloatCurrentSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 10),
    _PsFloatCurrentSupport_Type()
)
psFloatCurrentSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psFloatCurrentSupport.setStatus("mandatory")


class _PsOutputVoltageSupport_Type(Integer32):
    """Custom type psOutputVoltageSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_PsOutputVoltageSupport_Type.__name__ = "Integer32"
_PsOutputVoltageSupport_Object = MibTableColumn
psOutputVoltageSupport = _PsOutputVoltageSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 11),
    _PsOutputVoltageSupport_Type()
)
psOutputVoltageSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psOutputVoltageSupport.setStatus("mandatory")


class _PsInputVoltageSupport_Type(Integer32):
    """Custom type psInputVoltageSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 3),
          ("binary", 2),
          ("none", 1))
    )


_PsInputVoltageSupport_Type.__name__ = "Integer32"
_PsInputVoltageSupport_Object = MibTableColumn
psInputVoltageSupport = _PsInputVoltageSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 12),
    _PsInputVoltageSupport_Type()
)
psInputVoltageSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputVoltageSupport.setStatus("mandatory")


class _PsPowerSupplyTest_Type(Integer32):
    """Custom type psPowerSupplyTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_PsPowerSupplyTest_Type.__name__ = "Integer32"
_PsPowerSupplyTest_Object = MibTableColumn
psPowerSupplyTest = _PsPowerSupplyTest_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 13),
    _PsPowerSupplyTest_Type()
)
psPowerSupplyTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerSupplyTest.setStatus("mandatory")


class _PsMajorAlarmSupport_Type(Integer32):
    """Custom type psMajorAlarmSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_PsMajorAlarmSupport_Type.__name__ = "Integer32"
_PsMajorAlarmSupport_Object = MibTableColumn
psMajorAlarmSupport = _PsMajorAlarmSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 14),
    _PsMajorAlarmSupport_Type()
)
psMajorAlarmSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMajorAlarmSupport.setStatus("mandatory")


class _PsMinorAlarmSupport_Type(Integer32):
    """Custom type psMinorAlarmSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_PsMinorAlarmSupport_Type.__name__ = "Integer32"
_PsMinorAlarmSupport_Object = MibTableColumn
psMinorAlarmSupport = _PsMinorAlarmSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 15),
    _PsMinorAlarmSupport_Type()
)
psMinorAlarmSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMinorAlarmSupport.setStatus("mandatory")


class _PsTamperSupport_Type(Integer32):
    """Custom type psTamperSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_PsTamperSupport_Type.__name__ = "Integer32"
_PsTamperSupport_Object = MibTableColumn
psTamperSupport = _PsTamperSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 16),
    _PsTamperSupport_Type()
)
psTamperSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTamperSupport.setStatus("mandatory")


class _PsBatteryVoltageSupport_Type(Integer32):
    """Custom type psBatteryVoltageSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("noMonitoring", 1),
          ("totalString", 2))
    )


_PsBatteryVoltageSupport_Type.__name__ = "Integer32"
_PsBatteryVoltageSupport_Object = MibTableColumn
psBatteryVoltageSupport = _PsBatteryVoltageSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 17),
    _PsBatteryVoltageSupport_Type()
)
psBatteryVoltageSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryVoltageSupport.setStatus("mandatory")


class _PsOutputPowerSupport_Type(Integer32):
    """Custom type psOutputPowerSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_PsOutputPowerSupport_Type.__name__ = "Integer32"
_PsOutputPowerSupport_Object = MibTableColumn
psOutputPowerSupport = _PsOutputPowerSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 18),
    _PsOutputPowerSupport_Type()
)
psOutputPowerSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psOutputPowerSupport.setStatus("mandatory")


class _PsOutputFrequencySupport_Type(Integer32):
    """Custom type psOutputFrequencySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_PsOutputFrequencySupport_Type.__name__ = "Integer32"
_PsOutputFrequencySupport_Object = MibTableColumn
psOutputFrequencySupport = _PsOutputFrequencySupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 19),
    _PsOutputFrequencySupport_Type()
)
psOutputFrequencySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psOutputFrequencySupport.setStatus("mandatory")


class _PsInputCurrentSupport_Type(Integer32):
    """Custom type psInputCurrentSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_PsInputCurrentSupport_Type.__name__ = "Integer32"
_PsInputCurrentSupport_Object = MibTableColumn
psInputCurrentSupport = _PsInputCurrentSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 20),
    _PsInputCurrentSupport_Type()
)
psInputCurrentSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputCurrentSupport.setStatus("mandatory")


class _PsInputPowerSupport_Type(Integer32):
    """Custom type psInputPowerSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_PsInputPowerSupport_Type.__name__ = "Integer32"
_PsInputPowerSupport_Object = MibTableColumn
psInputPowerSupport = _PsInputPowerSupport_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 21),
    _PsInputPowerSupport_Type()
)
psInputPowerSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputPowerSupport.setStatus("mandatory")


class _PsOutputVoltage_Type(Integer32):
    """Custom type psOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsOutputVoltage_Type.__name__ = "Integer32"
_PsOutputVoltage_Object = MibTableColumn
psOutputVoltage = _PsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 22),
    _PsOutputVoltage_Type()
)
psOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psOutputVoltage.setStatus("mandatory")


class _PsInputVoltage_Type(Integer32):
    """Custom type psInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsInputVoltage_Type.__name__ = "Integer32"
_PsInputVoltage_Object = MibTableColumn
psInputVoltage = _PsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 23),
    _PsInputVoltage_Type()
)
psInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputVoltage.setStatus("optional")


class _PsInverterStatus_Type(Integer32):
    """Custom type psInverterStatus based on Integer32"""
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
        *(("lineFail", 2),
          ("off", 1),
          ("testCycle", 3),
          ("testFailed", 5),
          ("testStarted", 4))
    )


_PsInverterStatus_Type.__name__ = "Integer32"
_PsInverterStatus_Object = MibTableColumn
psInverterStatus = _PsInverterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 24),
    _PsInverterStatus_Type()
)
psInverterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInverterStatus.setStatus("optional")


class _PsMajorAlarm_Type(Integer32):
    """Custom type psMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("noAlarm", 1))
    )


_PsMajorAlarm_Type.__name__ = "Integer32"
_PsMajorAlarm_Object = MibTableColumn
psMajorAlarm = _PsMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 25),
    _PsMajorAlarm_Type()
)
psMajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMajorAlarm.setStatus("optional")


class _PsMinorAlarm_Type(Integer32):
    """Custom type psMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("noAlarm", 1))
    )


_PsMinorAlarm_Type.__name__ = "Integer32"
_PsMinorAlarm_Object = MibTableColumn
psMinorAlarm = _PsMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 26),
    _PsMinorAlarm_Type()
)
psMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMinorAlarm.setStatus("optional")


class _PsTamper_Type(Integer32):
    """Custom type psTamper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 2))
    )


_PsTamper_Type.__name__ = "Integer32"
_PsTamper_Object = MibTableColumn
psTamper = _PsTamper_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 27),
    _PsTamper_Type()
)
psTamper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTamper.setStatus("optional")


class _PsTotalStringVoltage_Type(Integer32):
    """Custom type psTotalStringVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsTotalStringVoltage_Type.__name__ = "Integer32"
_PsTotalStringVoltage_Object = MibTableColumn
psTotalStringVoltage = _PsTotalStringVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 28),
    _PsTotalStringVoltage_Type()
)
psTotalStringVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTotalStringVoltage.setStatus("optional")


class _PsEquipmentControl_Type(Integer32):
    """Custom type psEquipmentControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startTest", 2),
          ("stopTest", 1))
    )


_PsEquipmentControl_Type.__name__ = "Integer32"
_PsEquipmentControl_Object = MibTableColumn
psEquipmentControl = _PsEquipmentControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 29),
    _PsEquipmentControl_Type()
)
psEquipmentControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEquipmentControl.setStatus("optional")


class _PsPowerOut_Type(Integer32):
    """Custom type psPowerOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsPowerOut_Type.__name__ = "Integer32"
_PsPowerOut_Object = MibTableColumn
psPowerOut = _PsPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 30),
    _PsPowerOut_Type()
)
psPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerOut.setStatus("optional")


class _PsFrequencyOut_Type(Integer32):
    """Custom type psFrequencyOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsFrequencyOut_Type.__name__ = "Integer32"
_PsFrequencyOut_Object = MibTableColumn
psFrequencyOut = _PsFrequencyOut_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 31),
    _PsFrequencyOut_Type()
)
psFrequencyOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psFrequencyOut.setStatus("optional")


class _PsRMSCurrentIn_Type(Integer32):
    """Custom type psRMSCurrentIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsRMSCurrentIn_Type.__name__ = "Integer32"
_PsRMSCurrentIn_Object = MibTableColumn
psRMSCurrentIn = _PsRMSCurrentIn_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 32),
    _PsRMSCurrentIn_Type()
)
psRMSCurrentIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRMSCurrentIn.setStatus("optional")


class _PsPowerIn_Type(Integer32):
    """Custom type psPowerIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsPowerIn_Type.__name__ = "Integer32"
_PsPowerIn_Object = MibTableColumn
psPowerIn = _PsPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 33),
    _PsPowerIn_Type()
)
psPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPowerIn.setStatus("optional")


class _PsInputVoltagePresence_Type(Integer32):
    """Custom type psInputVoltagePresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lost", 1),
          ("ok", 2))
    )


_PsInputVoltagePresence_Type.__name__ = "Integer32"
_PsInputVoltagePresence_Object = MibTableColumn
psInputVoltagePresence = _PsInputVoltagePresence_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 34),
    _PsInputVoltagePresence_Type()
)
psInputVoltagePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputVoltagePresence.setStatus("optional")


class _PsFrequencyIn_Type(Integer32):
    """Custom type psFrequencyIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiftyHz", 1),
          ("sixtyHz", 2))
    )


_PsFrequencyIn_Type.__name__ = "Integer32"
_PsFrequencyIn_Object = MibTableColumn
psFrequencyIn = _PsFrequencyIn_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 35),
    _PsFrequencyIn_Type()
)
psFrequencyIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psFrequencyIn.setStatus("mandatory")
_PsStringTable_Object = MibTable
psStringTable = _PsStringTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 3)
)
if mibBuilder.loadTexts:
    psStringTable.setStatus("mandatory")
_PsStringEntry_Object = MibTableRow
psStringEntry = _PsStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1)
)
psStringEntry.setIndexNames(
    (0, "SCTE-HMS-PS-MIB", "psStringDeviceAddress"),
    (0, "SCTE-HMS-PS-MIB", "psString"),
)
if mibBuilder.loadTexts:
    psStringEntry.setStatus("mandatory")


class _PsStringDeviceAddress_Type(Integer32):
    """Custom type psStringDeviceAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PsStringDeviceAddress_Type.__name__ = "Integer32"
_PsStringDeviceAddress_Object = MibTableColumn
psStringDeviceAddress = _PsStringDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 1),
    _PsStringDeviceAddress_Type()
)
psStringDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringDeviceAddress.setStatus("mandatory")


class _PsString_Type(Integer32):
    """Custom type psString based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PsString_Type.__name__ = "Integer32"
_PsString_Object = MibTableColumn
psString = _PsString_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 2),
    _PsString_Type()
)
psString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psString.setStatus("mandatory")


class _PsStringChargeCurrent_Type(Integer32):
    """Custom type psStringChargeCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsStringChargeCurrent_Type.__name__ = "Integer32"
_PsStringChargeCurrent_Object = MibTableColumn
psStringChargeCurrent = _PsStringChargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 3),
    _PsStringChargeCurrent_Type()
)
psStringChargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringChargeCurrent.setStatus("optional")


class _PsStringDischargeCurrent_Type(Integer32):
    """Custom type psStringDischargeCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsStringDischargeCurrent_Type.__name__ = "Integer32"
_PsStringDischargeCurrent_Object = MibTableColumn
psStringDischargeCurrent = _PsStringDischargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 4),
    _PsStringDischargeCurrent_Type()
)
psStringDischargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringDischargeCurrent.setStatus("optional")


class _PsStringFloat_Type(Integer32):
    """Custom type psStringFloat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsStringFloat_Type.__name__ = "Integer32"
_PsStringFloat_Object = MibTableColumn
psStringFloat = _PsStringFloat_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 5),
    _PsStringFloat_Type()
)
psStringFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStringFloat.setStatus("optional")
_PsBatteryTable_Object = MibTable
psBatteryTable = _PsBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 4)
)
if mibBuilder.loadTexts:
    psBatteryTable.setStatus("mandatory")
_PsBatteryEntry_Object = MibTableRow
psBatteryEntry = _PsBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1)
)
psBatteryEntry.setIndexNames(
    (0, "SCTE-HMS-PS-MIB", "psBatteryDeviceAddress"),
    (0, "SCTE-HMS-PS-MIB", "psBatteryString"),
    (0, "SCTE-HMS-PS-MIB", "psBattery"),
)
if mibBuilder.loadTexts:
    psBatteryEntry.setStatus("mandatory")


class _PsBatteryDeviceAddress_Type(Integer32):
    """Custom type psBatteryDeviceAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PsBatteryDeviceAddress_Type.__name__ = "Integer32"
_PsBatteryDeviceAddress_Object = MibTableColumn
psBatteryDeviceAddress = _PsBatteryDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 1),
    _PsBatteryDeviceAddress_Type()
)
psBatteryDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryDeviceAddress.setStatus("mandatory")


class _PsBatteryString_Type(Integer32):
    """Custom type psBatteryString based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PsBatteryString_Type.__name__ = "Integer32"
_PsBatteryString_Object = MibTableColumn
psBatteryString = _PsBatteryString_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 2),
    _PsBatteryString_Type()
)
psBatteryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryString.setStatus("mandatory")


class _PsBattery_Type(Integer32):
    """Custom type psBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PsBattery_Type.__name__ = "Integer32"
_PsBattery_Object = MibTableColumn
psBattery = _PsBattery_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 3),
    _PsBattery_Type()
)
psBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBattery.setStatus("mandatory")


class _PsBatteryVoltage_Type(Integer32):
    """Custom type psBatteryVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsBatteryVoltage_Type.__name__ = "Integer32"
_PsBatteryVoltage_Object = MibTableColumn
psBatteryVoltage = _PsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 4),
    _PsBatteryVoltage_Type()
)
psBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryVoltage.setStatus("optional")
_PsOutputTable_Object = MibTable
psOutputTable = _PsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 5)
)
if mibBuilder.loadTexts:
    psOutputTable.setStatus("mandatory")
_PsOutputEntry_Object = MibTableRow
psOutputEntry = _PsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1)
)
psOutputEntry.setIndexNames(
    (0, "SCTE-HMS-PS-MIB", "psOutputDeviceAddress"),
    (0, "SCTE-HMS-PS-MIB", "psOutput"),
)
if mibBuilder.loadTexts:
    psOutputEntry.setStatus("mandatory")


class _PsOutputDeviceAddress_Type(Integer32):
    """Custom type psOutputDeviceAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PsOutputDeviceAddress_Type.__name__ = "Integer32"
_PsOutputDeviceAddress_Object = MibTableColumn
psOutputDeviceAddress = _PsOutputDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1, 1),
    _PsOutputDeviceAddress_Type()
)
psOutputDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psOutputDeviceAddress.setStatus("mandatory")


class _PsOutput_Type(Integer32):
    """Custom type psOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PsOutput_Type.__name__ = "Integer32"
_PsOutput_Object = MibTableColumn
psOutput = _PsOutput_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1, 2),
    _PsOutput_Type()
)
psOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psOutput.setStatus("mandatory")


class _PsOutputCurrent_Type(Integer32):
    """Custom type psOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsOutputCurrent_Type.__name__ = "Integer32"
_PsOutputCurrent_Object = MibTableColumn
psOutputCurrent = _PsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1, 3),
    _PsOutputCurrent_Type()
)
psOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psOutputCurrent.setStatus("optional")
_PsTemperatureSensorTable_Object = MibTable
psTemperatureSensorTable = _PsTemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 6)
)
if mibBuilder.loadTexts:
    psTemperatureSensorTable.setStatus("mandatory")
_PsTemperatureSensorEntry_Object = MibTableRow
psTemperatureSensorEntry = _PsTemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1)
)
psTemperatureSensorEntry.setIndexNames(
    (0, "SCTE-HMS-PS-MIB", "psTempDeviceAddress"),
    (0, "SCTE-HMS-PS-MIB", "psTemperatureSensor"),
)
if mibBuilder.loadTexts:
    psTemperatureSensorEntry.setStatus("mandatory")


class _PsTempDeviceAddress_Type(Integer32):
    """Custom type psTempDeviceAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PsTempDeviceAddress_Type.__name__ = "Integer32"
_PsTempDeviceAddress_Object = MibTableColumn
psTempDeviceAddress = _PsTempDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1, 1),
    _PsTempDeviceAddress_Type()
)
psTempDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTempDeviceAddress.setStatus("mandatory")


class _PsTemperatureSensor_Type(Integer32):
    """Custom type psTemperatureSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PsTemperatureSensor_Type.__name__ = "Integer32"
_PsTemperatureSensor_Object = MibTableColumn
psTemperatureSensor = _PsTemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1, 2),
    _PsTemperatureSensor_Type()
)
psTemperatureSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureSensor.setStatus("mandatory")


class _PsTemperature_Type(Integer32):
    """Custom type psTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 80),
    )


_PsTemperature_Type.__name__ = "Integer32"
_PsTemperature_Object = MibTableColumn
psTemperature = _PsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1, 3),
    _PsTemperature_Type()
)
psTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperature.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-PS-MIB",
    **{"psMonitored": psMonitored,
       "psDeviceTable": psDeviceTable,
       "psDeviceEntry": psDeviceEntry,
       "psDeviceAddress": psDeviceAddress,
       "psProtocolVersion": psProtocolVersion,
       "psSoftwareVersion": psSoftwareVersion,
       "psDeviceId": psDeviceId,
       "psBatteries": psBatteries,
       "psBatteryStrings": psBatteryStrings,
       "psTempSensors": psTempSensors,
       "psOutputs": psOutputs,
       "psBatteryCurrentSupport": psBatteryCurrentSupport,
       "psFloatCurrentSupport": psFloatCurrentSupport,
       "psOutputVoltageSupport": psOutputVoltageSupport,
       "psInputVoltageSupport": psInputVoltageSupport,
       "psPowerSupplyTest": psPowerSupplyTest,
       "psMajorAlarmSupport": psMajorAlarmSupport,
       "psMinorAlarmSupport": psMinorAlarmSupport,
       "psTamperSupport": psTamperSupport,
       "psBatteryVoltageSupport": psBatteryVoltageSupport,
       "psOutputPowerSupport": psOutputPowerSupport,
       "psOutputFrequencySupport": psOutputFrequencySupport,
       "psInputCurrentSupport": psInputCurrentSupport,
       "psInputPowerSupport": psInputPowerSupport,
       "psOutputVoltage": psOutputVoltage,
       "psInputVoltage": psInputVoltage,
       "psInverterStatus": psInverterStatus,
       "psMajorAlarm": psMajorAlarm,
       "psMinorAlarm": psMinorAlarm,
       "psTamper": psTamper,
       "psTotalStringVoltage": psTotalStringVoltage,
       "psEquipmentControl": psEquipmentControl,
       "psPowerOut": psPowerOut,
       "psFrequencyOut": psFrequencyOut,
       "psRMSCurrentIn": psRMSCurrentIn,
       "psPowerIn": psPowerIn,
       "psInputVoltagePresence": psInputVoltagePresence,
       "psFrequencyIn": psFrequencyIn,
       "psStringTable": psStringTable,
       "psStringEntry": psStringEntry,
       "psStringDeviceAddress": psStringDeviceAddress,
       "psString": psString,
       "psStringChargeCurrent": psStringChargeCurrent,
       "psStringDischargeCurrent": psStringDischargeCurrent,
       "psStringFloat": psStringFloat,
       "psBatteryTable": psBatteryTable,
       "psBatteryEntry": psBatteryEntry,
       "psBatteryDeviceAddress": psBatteryDeviceAddress,
       "psBatteryString": psBatteryString,
       "psBattery": psBattery,
       "psBatteryVoltage": psBatteryVoltage,
       "psOutputTable": psOutputTable,
       "psOutputEntry": psOutputEntry,
       "psOutputDeviceAddress": psOutputDeviceAddress,
       "psOutput": psOutput,
       "psOutputCurrent": psOutputCurrent,
       "psTemperatureSensorTable": psTemperatureSensorTable,
       "psTemperatureSensorEntry": psTemperatureSensorEntry,
       "psTempDeviceAddress": psTempDeviceAddress,
       "psTemperatureSensor": psTemperatureSensor,
       "psTemperature": psTemperature}
)
