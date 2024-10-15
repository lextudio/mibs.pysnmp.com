# SNMP MIB module (XUPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XUPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:49 2024
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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

_Powerware_ObjectIdentity = ObjectIdentity
powerware = _Powerware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534)
)
_Xups_ObjectIdentity = ObjectIdentity
xups = _Xups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1)
)
_XupsNull_ObjectIdentity = ObjectIdentity
xupsNull = _XupsNull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 0)
)
_XupsTrapBasic_ObjectIdentity = ObjectIdentity
xupsTrapBasic = _XupsTrapBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0)
)
_XupsIdent_ObjectIdentity = ObjectIdentity
xupsIdent = _XupsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 1)
)


class _XupsIdentManufacturer_Type(DisplayString):
    """Custom type xupsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XupsIdentManufacturer_Type.__name__ = "DisplayString"
_XupsIdentManufacturer_Object = MibScalar
xupsIdentManufacturer = _XupsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 1, 1),
    _XupsIdentManufacturer_Type()
)
xupsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsIdentManufacturer.setStatus("mandatory")


class _XupsIdentModel_Type(DisplayString):
    """Custom type xupsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_XupsIdentModel_Type.__name__ = "DisplayString"
_XupsIdentModel_Object = MibScalar
xupsIdentModel = _XupsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 1, 2),
    _XupsIdentModel_Type()
)
xupsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsIdentModel.setStatus("mandatory")


class _XupsIdentSoftwareVersion_Type(DisplayString):
    """Custom type xupsIdentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_XupsIdentSoftwareVersion_Type.__name__ = "DisplayString"
_XupsIdentSoftwareVersion_Object = MibScalar
xupsIdentSoftwareVersion = _XupsIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 1, 3),
    _XupsIdentSoftwareVersion_Type()
)
xupsIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsIdentSoftwareVersion.setStatus("mandatory")


class _XupsIdentOemCode_Type(Integer32):
    """Custom type xupsIdentOemCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XupsIdentOemCode_Type.__name__ = "Integer32"
_XupsIdentOemCode_Object = MibScalar
xupsIdentOemCode = _XupsIdentOemCode_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 1, 4),
    _XupsIdentOemCode_Type()
)
xupsIdentOemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsIdentOemCode.setStatus("mandatory")
_XupsBattery_ObjectIdentity = ObjectIdentity
xupsBattery = _XupsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 2)
)


class _XupsBatTimeRemaining_Type(Integer32):
    """Custom type xupsBatTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBatTimeRemaining_Type.__name__ = "Integer32"
_XupsBatTimeRemaining_Object = MibScalar
xupsBatTimeRemaining = _XupsBatTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 1),
    _XupsBatTimeRemaining_Type()
)
xupsBatTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatTimeRemaining.setStatus("mandatory")


class _XupsBatVoltage_Type(Integer32):
    """Custom type xupsBatVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBatVoltage_Type.__name__ = "Integer32"
_XupsBatVoltage_Object = MibScalar
xupsBatVoltage = _XupsBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 2),
    _XupsBatVoltage_Type()
)
xupsBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatVoltage.setStatus("mandatory")


class _XupsBatCurrent_Type(Integer32):
    """Custom type xupsBatCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_XupsBatCurrent_Type.__name__ = "Integer32"
_XupsBatCurrent_Object = MibScalar
xupsBatCurrent = _XupsBatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 3),
    _XupsBatCurrent_Type()
)
xupsBatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatCurrent.setStatus("mandatory")


class _XupsBatCapacity_Type(Integer32):
    """Custom type xupsBatCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XupsBatCapacity_Type.__name__ = "Integer32"
_XupsBatCapacity_Object = MibScalar
xupsBatCapacity = _XupsBatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 4),
    _XupsBatCapacity_Type()
)
xupsBatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatCapacity.setStatus("mandatory")


class _XupsBatteryAbmStatus_Type(Integer32):
    """Custom type xupsBatteryAbmStatus based on Integer32"""
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
        *(("batteryCharging", 1),
          ("batteryDischarging", 2),
          ("batteryFloating", 3),
          ("batteryResting", 4),
          ("unknown", 5))
    )


_XupsBatteryAbmStatus_Type.__name__ = "Integer32"
_XupsBatteryAbmStatus_Object = MibScalar
xupsBatteryAbmStatus = _XupsBatteryAbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 2, 5),
    _XupsBatteryAbmStatus_Type()
)
xupsBatteryAbmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBatteryAbmStatus.setStatus("mandatory")
_XupsInput_ObjectIdentity = ObjectIdentity
xupsInput = _XupsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 3)
)


class _XupsInputFrequency_Type(Integer32):
    """Custom type xupsInputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputFrequency_Type.__name__ = "Integer32"
_XupsInputFrequency_Object = MibScalar
xupsInputFrequency = _XupsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 1),
    _XupsInputFrequency_Type()
)
xupsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputFrequency.setStatus("mandatory")
_XupsInputLineBads_Type = Counter32
_XupsInputLineBads_Object = MibScalar
xupsInputLineBads = _XupsInputLineBads_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 2),
    _XupsInputLineBads_Type()
)
xupsInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputLineBads.setStatus("mandatory")


class _XupsInputNumPhases_Type(Integer32):
    """Custom type xupsInputNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsInputNumPhases_Type.__name__ = "Integer32"
_XupsInputNumPhases_Object = MibScalar
xupsInputNumPhases = _XupsInputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 3),
    _XupsInputNumPhases_Type()
)
xupsInputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputNumPhases.setStatus("mandatory")
_XupsInputTable_Object = MibTable
xupsInputTable = _XupsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4)
)
if mibBuilder.loadTexts:
    xupsInputTable.setStatus("mandatory")
_XupsInputEntry_Object = MibTableRow
xupsInputEntry = _XupsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1)
)
xupsInputEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsInputPhase"),
)
if mibBuilder.loadTexts:
    xupsInputEntry.setStatus("mandatory")


class _XupsInputPhase_Type(Integer32):
    """Custom type xupsInputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsInputPhase_Type.__name__ = "Integer32"
_XupsInputPhase_Object = MibTableColumn
xupsInputPhase = _XupsInputPhase_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 1),
    _XupsInputPhase_Type()
)
xupsInputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputPhase.setStatus("mandatory")


class _XupsInputVoltage_Type(Integer32):
    """Custom type xupsInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputVoltage_Type.__name__ = "Integer32"
_XupsInputVoltage_Object = MibTableColumn
xupsInputVoltage = _XupsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 2),
    _XupsInputVoltage_Type()
)
xupsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputVoltage.setStatus("mandatory")


class _XupsInputCurrent_Type(Integer32):
    """Custom type xupsInputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputCurrent_Type.__name__ = "Integer32"
_XupsInputCurrent_Object = MibTableColumn
xupsInputCurrent = _XupsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 3),
    _XupsInputCurrent_Type()
)
xupsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputCurrent.setStatus("mandatory")


class _XupsInputWatts_Type(Integer32):
    """Custom type xupsInputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsInputWatts_Type.__name__ = "Integer32"
_XupsInputWatts_Object = MibTableColumn
xupsInputWatts = _XupsInputWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 4, 1, 4),
    _XupsInputWatts_Type()
)
xupsInputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputWatts.setStatus("mandatory")


class _XupsInputSource_Type(Integer32):
    """Custom type xupsInputSource based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bypassFeed", 4),
          ("flywheel", 7),
          ("fuelcell", 8),
          ("generator", 6),
          ("none", 2),
          ("other", 1),
          ("primaryUtility", 3),
          ("secondaryUtility", 5))
    )


_XupsInputSource_Type.__name__ = "Integer32"
_XupsInputSource_Object = MibScalar
xupsInputSource = _XupsInputSource_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 3, 5),
    _XupsInputSource_Type()
)
xupsInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsInputSource.setStatus("mandatory")
_XupsOutput_ObjectIdentity = ObjectIdentity
xupsOutput = _XupsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 4)
)


class _XupsOutputLoad_Type(Integer32):
    """Custom type xupsOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_XupsOutputLoad_Type.__name__ = "Integer32"
_XupsOutputLoad_Object = MibScalar
xupsOutputLoad = _XupsOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 1),
    _XupsOutputLoad_Type()
)
xupsOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputLoad.setStatus("mandatory")


class _XupsOutputFrequency_Type(Integer32):
    """Custom type xupsOutputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputFrequency_Type.__name__ = "Integer32"
_XupsOutputFrequency_Object = MibScalar
xupsOutputFrequency = _XupsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 2),
    _XupsOutputFrequency_Type()
)
xupsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputFrequency.setStatus("mandatory")


class _XupsOutputNumPhases_Type(Integer32):
    """Custom type xupsOutputNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsOutputNumPhases_Type.__name__ = "Integer32"
_XupsOutputNumPhases_Object = MibScalar
xupsOutputNumPhases = _XupsOutputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 3),
    _XupsOutputNumPhases_Type()
)
xupsOutputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputNumPhases.setStatus("mandatory")
_XupsOutputTable_Object = MibTable
xupsOutputTable = _XupsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4)
)
if mibBuilder.loadTexts:
    xupsOutputTable.setStatus("mandatory")
_XupsOutputEntry_Object = MibTableRow
xupsOutputEntry = _XupsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1)
)
xupsOutputEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsOutputPhase"),
)
if mibBuilder.loadTexts:
    xupsOutputEntry.setStatus("mandatory")


class _XupsOutputPhase_Type(Integer32):
    """Custom type xupsOutputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsOutputPhase_Type.__name__ = "Integer32"
_XupsOutputPhase_Object = MibTableColumn
xupsOutputPhase = _XupsOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 1),
    _XupsOutputPhase_Type()
)
xupsOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputPhase.setStatus("mandatory")


class _XupsOutputVoltage_Type(Integer32):
    """Custom type xupsOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputVoltage_Type.__name__ = "Integer32"
_XupsOutputVoltage_Object = MibTableColumn
xupsOutputVoltage = _XupsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 2),
    _XupsOutputVoltage_Type()
)
xupsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputVoltage.setStatus("mandatory")


class _XupsOutputCurrent_Type(Integer32):
    """Custom type xupsOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputCurrent_Type.__name__ = "Integer32"
_XupsOutputCurrent_Object = MibTableColumn
xupsOutputCurrent = _XupsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 3),
    _XupsOutputCurrent_Type()
)
xupsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputCurrent.setStatus("mandatory")


class _XupsOutputWatts_Type(Integer32):
    """Custom type xupsOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsOutputWatts_Type.__name__ = "Integer32"
_XupsOutputWatts_Object = MibTableColumn
xupsOutputWatts = _XupsOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 4, 1, 4),
    _XupsOutputWatts_Type()
)
xupsOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputWatts.setStatus("mandatory")


class _XupsOutputSource_Type(Integer32):
    """Custom type xupsOutputSource based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("battery", 5),
          ("booster", 6),
          ("bypass", 4),
          ("highEfficiencyMode", 10),
          ("none", 2),
          ("normal", 3),
          ("other", 1),
          ("parallelCapacity", 8),
          ("parallelRedundant", 9),
          ("reducer", 7))
    )


_XupsOutputSource_Type.__name__ = "Integer32"
_XupsOutputSource_Object = MibScalar
xupsOutputSource = _XupsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 4, 5),
    _XupsOutputSource_Type()
)
xupsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsOutputSource.setStatus("mandatory")
_XupsBypass_ObjectIdentity = ObjectIdentity
xupsBypass = _XupsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 5)
)


class _XupsBypassFrequency_Type(Integer32):
    """Custom type xupsBypassFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBypassFrequency_Type.__name__ = "Integer32"
_XupsBypassFrequency_Object = MibScalar
xupsBypassFrequency = _XupsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 1),
    _XupsBypassFrequency_Type()
)
xupsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassFrequency.setStatus("mandatory")


class _XupsBypassNumPhases_Type(Integer32):
    """Custom type xupsBypassNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsBypassNumPhases_Type.__name__ = "Integer32"
_XupsBypassNumPhases_Object = MibScalar
xupsBypassNumPhases = _XupsBypassNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 2),
    _XupsBypassNumPhases_Type()
)
xupsBypassNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassNumPhases.setStatus("mandatory")
_XupsBypassTable_Object = MibTable
xupsBypassTable = _XupsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3)
)
if mibBuilder.loadTexts:
    xupsBypassTable.setStatus("mandatory")
_XupsBypassEntry_Object = MibTableRow
xupsBypassEntry = _XupsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3, 1)
)
xupsBypassEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsBypassPhase"),
)
if mibBuilder.loadTexts:
    xupsBypassEntry.setStatus("mandatory")


class _XupsBypassPhase_Type(Integer32):
    """Custom type xupsBypassPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_XupsBypassPhase_Type.__name__ = "Integer32"
_XupsBypassPhase_Object = MibTableColumn
xupsBypassPhase = _XupsBypassPhase_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3, 1, 1),
    _XupsBypassPhase_Type()
)
xupsBypassPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassPhase.setStatus("mandatory")


class _XupsBypassVoltage_Type(Integer32):
    """Custom type xupsBypassVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsBypassVoltage_Type.__name__ = "Integer32"
_XupsBypassVoltage_Object = MibTableColumn
xupsBypassVoltage = _XupsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 5, 3, 1, 2),
    _XupsBypassVoltage_Type()
)
xupsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsBypassVoltage.setStatus("mandatory")
_XupsEnvironment_ObjectIdentity = ObjectIdentity
xupsEnvironment = _XupsEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 6)
)


class _XupsEnvAmbientTemp_Type(Integer32):
    """Custom type xupsEnvAmbientTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvAmbientTemp_Type.__name__ = "Integer32"
_XupsEnvAmbientTemp_Object = MibScalar
xupsEnvAmbientTemp = _XupsEnvAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 1),
    _XupsEnvAmbientTemp_Type()
)
xupsEnvAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsEnvAmbientTemp.setStatus("mandatory")


class _XupsEnvAmbientLowerLimit_Type(Integer32):
    """Custom type xupsEnvAmbientLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvAmbientLowerLimit_Type.__name__ = "Integer32"
_XupsEnvAmbientLowerLimit_Object = MibScalar
xupsEnvAmbientLowerLimit = _XupsEnvAmbientLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 2),
    _XupsEnvAmbientLowerLimit_Type()
)
xupsEnvAmbientLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvAmbientLowerLimit.setStatus("mandatory")


class _XupsEnvAmbientUpperLimit_Type(Integer32):
    """Custom type xupsEnvAmbientUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvAmbientUpperLimit_Type.__name__ = "Integer32"
_XupsEnvAmbientUpperLimit_Object = MibScalar
xupsEnvAmbientUpperLimit = _XupsEnvAmbientUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 3),
    _XupsEnvAmbientUpperLimit_Type()
)
xupsEnvAmbientUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvAmbientUpperLimit.setStatus("mandatory")


class _XupsEnvAmbientHumidity_Type(Integer32):
    """Custom type xupsEnvAmbientHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XupsEnvAmbientHumidity_Type.__name__ = "Integer32"
_XupsEnvAmbientHumidity_Object = MibScalar
xupsEnvAmbientHumidity = _XupsEnvAmbientHumidity_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 4),
    _XupsEnvAmbientHumidity_Type()
)
xupsEnvAmbientHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsEnvAmbientHumidity.setStatus("mandatory")


class _XupsEnvRemoteTemp_Type(Integer32):
    """Custom type xupsEnvRemoteTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvRemoteTemp_Type.__name__ = "Integer32"
_XupsEnvRemoteTemp_Object = MibScalar
xupsEnvRemoteTemp = _XupsEnvRemoteTemp_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 5),
    _XupsEnvRemoteTemp_Type()
)
xupsEnvRemoteTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsEnvRemoteTemp.setStatus("mandatory")


class _XupsEnvRemoteHumidity_Type(Integer32):
    """Custom type xupsEnvRemoteHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XupsEnvRemoteHumidity_Type.__name__ = "Integer32"
_XupsEnvRemoteHumidity_Object = MibScalar
xupsEnvRemoteHumidity = _XupsEnvRemoteHumidity_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 6),
    _XupsEnvRemoteHumidity_Type()
)
xupsEnvRemoteHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsEnvRemoteHumidity.setStatus("mandatory")


class _XupsEnvNumContacts_Type(Integer32):
    """Custom type xupsEnvNumContacts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_XupsEnvNumContacts_Type.__name__ = "Integer32"
_XupsEnvNumContacts_Object = MibScalar
xupsEnvNumContacts = _XupsEnvNumContacts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 7),
    _XupsEnvNumContacts_Type()
)
xupsEnvNumContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsEnvNumContacts.setStatus("mandatory")
_XupsContactSenseTable_Object = MibTable
xupsContactSenseTable = _XupsContactSenseTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8)
)
if mibBuilder.loadTexts:
    xupsContactSenseTable.setStatus("mandatory")
_XupsContactsTableEntry_Object = MibTableRow
xupsContactsTableEntry = _XupsContactsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1)
)
xupsContactsTableEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsContactIndex"),
)
if mibBuilder.loadTexts:
    xupsContactsTableEntry.setStatus("mandatory")


class _XupsContactIndex_Type(Integer32):
    """Custom type xupsContactIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_XupsContactIndex_Type.__name__ = "Integer32"
_XupsContactIndex_Object = MibTableColumn
xupsContactIndex = _XupsContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 1),
    _XupsContactIndex_Type()
)
xupsContactIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xupsContactIndex.setStatus("mandatory")


class _XupsContactType_Type(Integer32):
    """Custom type xupsContactType based on Integer32"""
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
        *(("anyChange", 3),
          ("normallyClosed", 2),
          ("normallyOpen", 1),
          ("notUsed", 4))
    )


_XupsContactType_Type.__name__ = "Integer32"
_XupsContactType_Object = MibTableColumn
xupsContactType = _XupsContactType_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 2),
    _XupsContactType_Type()
)
xupsContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsContactType.setStatus("mandatory")


class _XupsContactState_Type(Integer32):
    """Custom type xupsContactState based on Integer32"""
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
        *(("closed", 2),
          ("closedWithNotice", 4),
          ("open", 1),
          ("openWithNotice", 3))
    )


_XupsContactState_Type.__name__ = "Integer32"
_XupsContactState_Object = MibTableColumn
xupsContactState = _XupsContactState_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 3),
    _XupsContactState_Type()
)
xupsContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsContactState.setStatus("mandatory")


class _XupsContactDescr_Type(DisplayString):
    """Custom type xupsContactDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_XupsContactDescr_Type.__name__ = "DisplayString"
_XupsContactDescr_Object = MibTableColumn
xupsContactDescr = _XupsContactDescr_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 8, 1, 4),
    _XupsContactDescr_Type()
)
xupsContactDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsContactDescr.setStatus("mandatory")


class _XupsEnvRemoteTempLowerLimit_Type(Integer32):
    """Custom type xupsEnvRemoteTempLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvRemoteTempLowerLimit_Type.__name__ = "Integer32"
_XupsEnvRemoteTempLowerLimit_Object = MibScalar
xupsEnvRemoteTempLowerLimit = _XupsEnvRemoteTempLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 9),
    _XupsEnvRemoteTempLowerLimit_Type()
)
xupsEnvRemoteTempLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvRemoteTempLowerLimit.setStatus("mandatory")


class _XupsEnvRemoteTempUpperLimit_Type(Integer32):
    """Custom type xupsEnvRemoteTempUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_XupsEnvRemoteTempUpperLimit_Type.__name__ = "Integer32"
_XupsEnvRemoteTempUpperLimit_Object = MibScalar
xupsEnvRemoteTempUpperLimit = _XupsEnvRemoteTempUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 10),
    _XupsEnvRemoteTempUpperLimit_Type()
)
xupsEnvRemoteTempUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvRemoteTempUpperLimit.setStatus("mandatory")


class _XupsEnvRemoteHumidityLowerLimit_Type(Integer32):
    """Custom type xupsEnvRemoteHumidityLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XupsEnvRemoteHumidityLowerLimit_Type.__name__ = "Integer32"
_XupsEnvRemoteHumidityLowerLimit_Object = MibScalar
xupsEnvRemoteHumidityLowerLimit = _XupsEnvRemoteHumidityLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 11),
    _XupsEnvRemoteHumidityLowerLimit_Type()
)
xupsEnvRemoteHumidityLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvRemoteHumidityLowerLimit.setStatus("mandatory")


class _XupsEnvRemoteHumidityUpperLimit_Type(Integer32):
    """Custom type xupsEnvRemoteHumidityUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XupsEnvRemoteHumidityUpperLimit_Type.__name__ = "Integer32"
_XupsEnvRemoteHumidityUpperLimit_Object = MibScalar
xupsEnvRemoteHumidityUpperLimit = _XupsEnvRemoteHumidityUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 6, 12),
    _XupsEnvRemoteHumidityUpperLimit_Type()
)
xupsEnvRemoteHumidityUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsEnvRemoteHumidityUpperLimit.setStatus("mandatory")
_XupsAlarm_ObjectIdentity = ObjectIdentity
xupsAlarm = _XupsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7)
)
_XupsAlarms_Type = Gauge32
_XupsAlarms_Object = MibScalar
xupsAlarms = _XupsAlarms_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 1),
    _XupsAlarms_Type()
)
xupsAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarms.setStatus("mandatory")
_XupsAlarmTable_Object = MibTable
xupsAlarmTable = _XupsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 2)
)
if mibBuilder.loadTexts:
    xupsAlarmTable.setStatus("mandatory")
_XupsAlarmEntry_Object = MibTableRow
xupsAlarmEntry = _XupsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 2, 1)
)
xupsAlarmEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsAlarmID"),
)
if mibBuilder.loadTexts:
    xupsAlarmEntry.setStatus("mandatory")


class _XupsAlarmID_Type(Integer32):
    """Custom type xupsAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XupsAlarmID_Type.__name__ = "Integer32"
_XupsAlarmID_Object = MibTableColumn
xupsAlarmID = _XupsAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 2, 1, 1),
    _XupsAlarmID_Type()
)
xupsAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmID.setStatus("mandatory")
_XupsAlarmDescr_Type = ObjectIdentifier
_XupsAlarmDescr_Object = MibTableColumn
xupsAlarmDescr = _XupsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 2, 1, 2),
    _XupsAlarmDescr_Type()
)
xupsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmDescr.setStatus("mandatory")
_XupsAlarmTime_Type = TimeTicks
_XupsAlarmTime_Object = MibTableColumn
xupsAlarmTime = _XupsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 2, 1, 3),
    _XupsAlarmTime_Type()
)
xupsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmTime.setStatus("mandatory")
_XupsOnBattery_ObjectIdentity = ObjectIdentity
xupsOnBattery = _XupsOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 3)
)
_XupsLowBattery_ObjectIdentity = ObjectIdentity
xupsLowBattery = _XupsLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 4)
)
_XupsUtilityPowerRestored_ObjectIdentity = ObjectIdentity
xupsUtilityPowerRestored = _XupsUtilityPowerRestored_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 5)
)
_XupsReturnFromLowBattery_ObjectIdentity = ObjectIdentity
xupsReturnFromLowBattery = _XupsReturnFromLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 6)
)
_XupsOutputOverload_ObjectIdentity = ObjectIdentity
xupsOutputOverload = _XupsOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 7)
)
_XupsInternalFailure_ObjectIdentity = ObjectIdentity
xupsInternalFailure = _XupsInternalFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 8)
)
_XupsBatteryDischarged_ObjectIdentity = ObjectIdentity
xupsBatteryDischarged = _XupsBatteryDischarged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 9)
)
_XupsInverterFailure_ObjectIdentity = ObjectIdentity
xupsInverterFailure = _XupsInverterFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 10)
)
_XupsOnBypass_ObjectIdentity = ObjectIdentity
xupsOnBypass = _XupsOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 11)
)
_XupsBypassNotAvailable_ObjectIdentity = ObjectIdentity
xupsBypassNotAvailable = _XupsBypassNotAvailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 12)
)
_XupsOutputOff_ObjectIdentity = ObjectIdentity
xupsOutputOff = _XupsOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 13)
)
_XupsInputFailure_ObjectIdentity = ObjectIdentity
xupsInputFailure = _XupsInputFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 14)
)
_XupsBuildingAlarm_ObjectIdentity = ObjectIdentity
xupsBuildingAlarm = _XupsBuildingAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 15)
)
_XupsShutdownImminent_ObjectIdentity = ObjectIdentity
xupsShutdownImminent = _XupsShutdownImminent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 16)
)
_XupsOnInverter_ObjectIdentity = ObjectIdentity
xupsOnInverter = _XupsOnInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 17)
)
_XupsAlarmNumEvents_Type = Gauge32
_XupsAlarmNumEvents_Object = MibScalar
xupsAlarmNumEvents = _XupsAlarmNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 18),
    _XupsAlarmNumEvents_Type()
)
xupsAlarmNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmNumEvents.setStatus("mandatory")
_XupsAlarmEventTable_Object = MibTable
xupsAlarmEventTable = _XupsAlarmEventTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19)
)
if mibBuilder.loadTexts:
    xupsAlarmEventTable.setStatus("mandatory")
_XupsAlarmEventEntry_Object = MibTableRow
xupsAlarmEventEntry = _XupsAlarmEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1)
)
xupsAlarmEventEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsAlarmEventID"),
)
if mibBuilder.loadTexts:
    xupsAlarmEventEntry.setStatus("mandatory")


class _XupsAlarmEventID_Type(Integer32):
    """Custom type xupsAlarmEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_XupsAlarmEventID_Type.__name__ = "Integer32"
_XupsAlarmEventID_Object = MibTableColumn
xupsAlarmEventID = _XupsAlarmEventID_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1, 1),
    _XupsAlarmEventID_Type()
)
xupsAlarmEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmEventID.setStatus("deprecated")


class _XupsAlarmEventDateAndTime_Type(DisplayString):
    """Custom type xupsAlarmEventDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_XupsAlarmEventDateAndTime_Type.__name__ = "DisplayString"
_XupsAlarmEventDateAndTime_Object = MibTableColumn
xupsAlarmEventDateAndTime = _XupsAlarmEventDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1, 2),
    _XupsAlarmEventDateAndTime_Type()
)
xupsAlarmEventDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmEventDateAndTime.setStatus("deprecated")


class _XupsAlarmEventKind_Type(Integer32):
    """Custom type xupsAlarmEventKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 2),
          ("occurred", 1),
          ("unknown", 3))
    )


_XupsAlarmEventKind_Type.__name__ = "Integer32"
_XupsAlarmEventKind_Object = MibTableColumn
xupsAlarmEventKind = _XupsAlarmEventKind_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1, 3),
    _XupsAlarmEventKind_Type()
)
xupsAlarmEventKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmEventKind.setStatus("deprecated")


class _XupsAlarmEventDescr_Type(Integer32):
    """Custom type xupsAlarmEventDescr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsAlarmEventDescr_Type.__name__ = "Integer32"
_XupsAlarmEventDescr_Object = MibTableColumn
xupsAlarmEventDescr = _XupsAlarmEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1, 4),
    _XupsAlarmEventDescr_Type()
)
xupsAlarmEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmEventDescr.setStatus("deprecated")


class _XupsAlarmEventMsg_Type(DisplayString):
    """Custom type xupsAlarmEventMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_XupsAlarmEventMsg_Type.__name__ = "DisplayString"
_XupsAlarmEventMsg_Object = MibTableColumn
xupsAlarmEventMsg = _XupsAlarmEventMsg_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 19, 1, 5),
    _XupsAlarmEventMsg_Type()
)
xupsAlarmEventMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsAlarmEventMsg.setStatus("mandatory")
_XupsBreakerOpen_ObjectIdentity = ObjectIdentity
xupsBreakerOpen = _XupsBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 20)
)
_XupsAlarmEntryAdded_ObjectIdentity = ObjectIdentity
xupsAlarmEntryAdded = _XupsAlarmEntryAdded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 21)
)
_XupsAlarmEntryRemoved_ObjectIdentity = ObjectIdentity
xupsAlarmEntryRemoved = _XupsAlarmEntryRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 22)
)
_XupsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
xupsAlarmBatteryBad = _XupsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 23)
)
_XupsOutputOffAsRequested_ObjectIdentity = ObjectIdentity
xupsOutputOffAsRequested = _XupsOutputOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 24)
)
_XupsDiagnosticTestFailed_ObjectIdentity = ObjectIdentity
xupsDiagnosticTestFailed = _XupsDiagnosticTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 25)
)
_XupsCommunicationsLost_ObjectIdentity = ObjectIdentity
xupsCommunicationsLost = _XupsCommunicationsLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 26)
)
_XupsUpsShutdownPending_ObjectIdentity = ObjectIdentity
xupsUpsShutdownPending = _XupsUpsShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 27)
)
_XupsAlarmTestInProgress_ObjectIdentity = ObjectIdentity
xupsAlarmTestInProgress = _XupsAlarmTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 28)
)
_XupsAmbientTempBad_ObjectIdentity = ObjectIdentity
xupsAmbientTempBad = _XupsAmbientTempBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 29)
)
_XupsLossOfRedundancy_ObjectIdentity = ObjectIdentity
xupsLossOfRedundancy = _XupsLossOfRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 30)
)
_XupsAlarmTempBad_ObjectIdentity = ObjectIdentity
xupsAlarmTempBad = _XupsAlarmTempBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 31)
)
_XupsAlarmChargerFailed_ObjectIdentity = ObjectIdentity
xupsAlarmChargerFailed = _XupsAlarmChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 32)
)
_XupsAlarmFanFailure_ObjectIdentity = ObjectIdentity
xupsAlarmFanFailure = _XupsAlarmFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 33)
)
_XupsAlarmFuseFailure_ObjectIdentity = ObjectIdentity
xupsAlarmFuseFailure = _XupsAlarmFuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 34)
)
_XupsPowerSwitchBad_ObjectIdentity = ObjectIdentity
xupsPowerSwitchBad = _XupsPowerSwitchBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 35)
)
_XupsModuleFailure_ObjectIdentity = ObjectIdentity
xupsModuleFailure = _XupsModuleFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 36)
)
_XupsOnAlternatePowerSource_ObjectIdentity = ObjectIdentity
xupsOnAlternatePowerSource = _XupsOnAlternatePowerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 37)
)
_XupsAltPowerNotAvailable_ObjectIdentity = ObjectIdentity
xupsAltPowerNotAvailable = _XupsAltPowerNotAvailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 38)
)
_XupsNoticeCondition_ObjectIdentity = ObjectIdentity
xupsNoticeCondition = _XupsNoticeCondition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 39)
)
_XupsRemoteTempBad_ObjectIdentity = ObjectIdentity
xupsRemoteTempBad = _XupsRemoteTempBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 40)
)
_XupsRemoteHumidityBad_ObjectIdentity = ObjectIdentity
xupsRemoteHumidityBad = _XupsRemoteHumidityBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 7, 41)
)
_XupsTest_ObjectIdentity = ObjectIdentity
xupsTest = _XupsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 8)
)


class _XupsTestBattery_Type(Integer32):
    """Custom type xupsTestBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("startTest", 1)
    )


_XupsTestBattery_Type.__name__ = "Integer32"
_XupsTestBattery_Object = MibScalar
xupsTestBattery = _XupsTestBattery_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 8, 1),
    _XupsTestBattery_Type()
)
xupsTestBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsTestBattery.setStatus("mandatory")


class _XupsTestBatteryStatus_Type(Integer32):
    """Custom type xupsTestBatteryStatus based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 4),
          ("inhibited", 6),
          ("notSupported", 5),
          ("passed", 2),
          ("scheduled", 7),
          ("unknown", 1))
    )


_XupsTestBatteryStatus_Type.__name__ = "Integer32"
_XupsTestBatteryStatus_Object = MibScalar
xupsTestBatteryStatus = _XupsTestBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 8, 2),
    _XupsTestBatteryStatus_Type()
)
xupsTestBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsTestBatteryStatus.setStatus("mandatory")
_XupsControl_ObjectIdentity = ObjectIdentity
xupsControl = _XupsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 9)
)


class _XupsControlOutputOffDelay_Type(Integer32):
    """Custom type xupsControlOutputOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsControlOutputOffDelay_Type.__name__ = "Integer32"
_XupsControlOutputOffDelay_Object = MibScalar
xupsControlOutputOffDelay = _XupsControlOutputOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 1),
    _XupsControlOutputOffDelay_Type()
)
xupsControlOutputOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsControlOutputOffDelay.setStatus("mandatory")


class _XupsControlOutputOnDelay_Type(Integer32):
    """Custom type xupsControlOutputOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsControlOutputOnDelay_Type.__name__ = "Integer32"
_XupsControlOutputOnDelay_Object = MibScalar
xupsControlOutputOnDelay = _XupsControlOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 2),
    _XupsControlOutputOnDelay_Type()
)
xupsControlOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsControlOutputOnDelay.setStatus("mandatory")


class _XupsControlOutputOffTrapDelay_Type(Integer32):
    """Custom type xupsControlOutputOffTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsControlOutputOffTrapDelay_Type.__name__ = "Integer32"
_XupsControlOutputOffTrapDelay_Object = MibScalar
xupsControlOutputOffTrapDelay = _XupsControlOutputOffTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 3),
    _XupsControlOutputOffTrapDelay_Type()
)
xupsControlOutputOffTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsControlOutputOffTrapDelay.setStatus("mandatory")


class _XupsControlOutputOnTrapDelay_Type(Integer32):
    """Custom type xupsControlOutputOnTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsControlOutputOnTrapDelay_Type.__name__ = "Integer32"
_XupsControlOutputOnTrapDelay_Object = MibScalar
xupsControlOutputOnTrapDelay = _XupsControlOutputOnTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 4),
    _XupsControlOutputOnTrapDelay_Type()
)
xupsControlOutputOnTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsControlOutputOnTrapDelay.setStatus("deprecated")


class _XupsControlToBypassDelay_Type(Integer32):
    """Custom type xupsControlToBypassDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsControlToBypassDelay_Type.__name__ = "Integer32"
_XupsControlToBypassDelay_Object = MibScalar
xupsControlToBypassDelay = _XupsControlToBypassDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 5),
    _XupsControlToBypassDelay_Type()
)
xupsControlToBypassDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsControlToBypassDelay.setStatus("mandatory")


class _XupsLoadShedSecsWithRestart_Type(Integer32):
    """Custom type xupsLoadShedSecsWithRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsLoadShedSecsWithRestart_Type.__name__ = "Integer32"
_XupsLoadShedSecsWithRestart_Object = MibScalar
xupsLoadShedSecsWithRestart = _XupsLoadShedSecsWithRestart_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 9, 6),
    _XupsLoadShedSecsWithRestart_Type()
)
xupsLoadShedSecsWithRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsLoadShedSecsWithRestart.setStatus("mandatory")
_XupsConfig_ObjectIdentity = ObjectIdentity
xupsConfig = _XupsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 10)
)


class _XupsConfigOutputVoltage_Type(Integer32):
    """Custom type xupsConfigOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigOutputVoltage_Type.__name__ = "Integer32"
_XupsConfigOutputVoltage_Object = MibScalar
xupsConfigOutputVoltage = _XupsConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 1),
    _XupsConfigOutputVoltage_Type()
)
xupsConfigOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigOutputVoltage.setStatus("mandatory")


class _XupsConfigInputVoltage_Type(Integer32):
    """Custom type xupsConfigInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigInputVoltage_Type.__name__ = "Integer32"
_XupsConfigInputVoltage_Object = MibScalar
xupsConfigInputVoltage = _XupsConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 2),
    _XupsConfigInputVoltage_Type()
)
xupsConfigInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigInputVoltage.setStatus("mandatory")


class _XupsConfigOutputWatts_Type(Integer32):
    """Custom type xupsConfigOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigOutputWatts_Type.__name__ = "Integer32"
_XupsConfigOutputWatts_Object = MibScalar
xupsConfigOutputWatts = _XupsConfigOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 3),
    _XupsConfigOutputWatts_Type()
)
xupsConfigOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigOutputWatts.setStatus("mandatory")


class _XupsConfigOutputFreq_Type(Integer32):
    """Custom type xupsConfigOutputFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigOutputFreq_Type.__name__ = "Integer32"
_XupsConfigOutputFreq_Object = MibScalar
xupsConfigOutputFreq = _XupsConfigOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 4),
    _XupsConfigOutputFreq_Type()
)
xupsConfigOutputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigOutputFreq.setStatus("mandatory")


class _XupsConfigDateAndTime_Type(DisplayString):
    """Custom type xupsConfigDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_XupsConfigDateAndTime_Type.__name__ = "DisplayString"
_XupsConfigDateAndTime_Object = MibScalar
xupsConfigDateAndTime = _XupsConfigDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 5),
    _XupsConfigDateAndTime_Type()
)
xupsConfigDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsConfigDateAndTime.setStatus("mandatory")


class _XupsConfigLowOutputVoltageLimit_Type(Integer32):
    """Custom type xupsConfigLowOutputVoltageLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigLowOutputVoltageLimit_Type.__name__ = "Integer32"
_XupsConfigLowOutputVoltageLimit_Object = MibScalar
xupsConfigLowOutputVoltageLimit = _XupsConfigLowOutputVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 6),
    _XupsConfigLowOutputVoltageLimit_Type()
)
xupsConfigLowOutputVoltageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigLowOutputVoltageLimit.setStatus("mandatory")


class _XupsConfigHighOutputVoltageLimit_Type(Integer32):
    """Custom type xupsConfigHighOutputVoltageLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsConfigHighOutputVoltageLimit_Type.__name__ = "Integer32"
_XupsConfigHighOutputVoltageLimit_Object = MibScalar
xupsConfigHighOutputVoltageLimit = _XupsConfigHighOutputVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 10, 7),
    _XupsConfigHighOutputVoltageLimit_Type()
)
xupsConfigHighOutputVoltageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsConfigHighOutputVoltageLimit.setStatus("mandatory")
_XupsTrapControl_ObjectIdentity = ObjectIdentity
xupsTrapControl = _XupsTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 11)
)


class _XupsMaxTrapLevel_Type(Integer32):
    """Custom type xupsMaxTrapLevel based on Integer32"""
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
        *(("allTraps", 4),
          ("critical", 2),
          ("major", 3),
          ("none", 1))
    )


_XupsMaxTrapLevel_Type.__name__ = "Integer32"
_XupsMaxTrapLevel_Object = MibScalar
xupsMaxTrapLevel = _XupsMaxTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 1),
    _XupsMaxTrapLevel_Type()
)
xupsMaxTrapLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsMaxTrapLevel.setStatus("mandatory")


class _XupsSendTrapType_Type(Integer32):
    """Custom type xupsSendTrapType based on Integer32"""
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
        *(("stnd", 1),
          ("stndPlus", 3),
          ("xups", 2),
          ("xupsPlus", 4))
    )


_XupsSendTrapType_Type.__name__ = "Integer32"
_XupsSendTrapType_Object = MibScalar
xupsSendTrapType = _XupsSendTrapType_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 2),
    _XupsSendTrapType_Type()
)
xupsSendTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsSendTrapType.setStatus("mandatory")


class _XupsTrapMessage_Type(DisplayString):
    """Custom type xupsTrapMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_XupsTrapMessage_Type.__name__ = "DisplayString"
_XupsTrapMessage_Object = MibScalar
xupsTrapMessage = _XupsTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 3),
    _XupsTrapMessage_Type()
)
xupsTrapMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xupsTrapMessage.setStatus("mandatory")
_XupsTrapSource_ObjectIdentity = ObjectIdentity
xupsTrapSource = _XupsTrapSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4)
)
_XupsTrapDefined_ObjectIdentity = ObjectIdentity
xupsTrapDefined = _XupsTrapDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1)
)
_XupsTrapPortN_ObjectIdentity = ObjectIdentity
xupsTrapPortN = _XupsTrapPortN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2)
)
_XupsRecep_ObjectIdentity = ObjectIdentity
xupsRecep = _XupsRecep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 12)
)


class _XupsNumReceptacles_Type(Integer32):
    """Custom type xupsNumReceptacles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_XupsNumReceptacles_Type.__name__ = "Integer32"
_XupsNumReceptacles_Object = MibScalar
xupsNumReceptacles = _XupsNumReceptacles_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 1),
    _XupsNumReceptacles_Type()
)
xupsNumReceptacles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsNumReceptacles.setStatus("mandatory")
_XupsRecepTable_Object = MibTable
xupsRecepTable = _XupsRecepTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2)
)
if mibBuilder.loadTexts:
    xupsRecepTable.setStatus("mandatory")
_XupsRecepEntry_Object = MibTableRow
xupsRecepEntry = _XupsRecepEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1)
)
xupsRecepEntry.setIndexNames(
    (0, "XUPS-MIB", "xupsRecepIndex"),
)
if mibBuilder.loadTexts:
    xupsRecepEntry.setStatus("mandatory")


class _XupsRecepIndex_Type(Integer32):
    """Custom type xupsRecepIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_XupsRecepIndex_Type.__name__ = "Integer32"
_XupsRecepIndex_Object = MibTableColumn
xupsRecepIndex = _XupsRecepIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 1),
    _XupsRecepIndex_Type()
)
xupsRecepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsRecepIndex.setStatus("mandatory")


class _XupsRecepStatus_Type(Integer32):
    """Custom type xupsRecepStatus based on Integer32"""
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
        *(("off", 2),
          ("on", 1),
          ("pendingOff", 3),
          ("pendingOn", 4),
          ("unknown", 5))
    )


_XupsRecepStatus_Type.__name__ = "Integer32"
_XupsRecepStatus_Object = MibTableColumn
xupsRecepStatus = _XupsRecepStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 2),
    _XupsRecepStatus_Type()
)
xupsRecepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsRecepStatus.setStatus("mandatory")


class _XupsRecepOffDelaySecs_Type(Integer32):
    """Custom type xupsRecepOffDelaySecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_XupsRecepOffDelaySecs_Type.__name__ = "Integer32"
_XupsRecepOffDelaySecs_Object = MibTableColumn
xupsRecepOffDelaySecs = _XupsRecepOffDelaySecs_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 3),
    _XupsRecepOffDelaySecs_Type()
)
xupsRecepOffDelaySecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepOffDelaySecs.setStatus("mandatory")


class _XupsRecepOnDelaySecs_Type(Integer32):
    """Custom type xupsRecepOnDelaySecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_XupsRecepOnDelaySecs_Type.__name__ = "Integer32"
_XupsRecepOnDelaySecs_Object = MibTableColumn
xupsRecepOnDelaySecs = _XupsRecepOnDelaySecs_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 4),
    _XupsRecepOnDelaySecs_Type()
)
xupsRecepOnDelaySecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepOnDelaySecs.setStatus("mandatory")


class _XupsRecepAutoOffDelay_Type(Integer32):
    """Custom type xupsRecepAutoOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_XupsRecepAutoOffDelay_Type.__name__ = "Integer32"
_XupsRecepAutoOffDelay_Object = MibTableColumn
xupsRecepAutoOffDelay = _XupsRecepAutoOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 5),
    _XupsRecepAutoOffDelay_Type()
)
xupsRecepAutoOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepAutoOffDelay.setStatus("mandatory")


class _XupsRecepAutoOnDelay_Type(Integer32):
    """Custom type xupsRecepAutoOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_XupsRecepAutoOnDelay_Type.__name__ = "Integer32"
_XupsRecepAutoOnDelay_Object = MibTableColumn
xupsRecepAutoOnDelay = _XupsRecepAutoOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 6),
    _XupsRecepAutoOnDelay_Type()
)
xupsRecepAutoOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepAutoOnDelay.setStatus("mandatory")


class _XupsRecepShedSecsWithRestart_Type(Integer32):
    """Custom type xupsRecepShedSecsWithRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XupsRecepShedSecsWithRestart_Type.__name__ = "Integer32"
_XupsRecepShedSecsWithRestart_Object = MibTableColumn
xupsRecepShedSecsWithRestart = _XupsRecepShedSecsWithRestart_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 12, 2, 1, 7),
    _XupsRecepShedSecsWithRestart_Type()
)
xupsRecepShedSecsWithRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsRecepShedSecsWithRestart.setStatus("mandatory")
_XupsTopology_ObjectIdentity = ObjectIdentity
xupsTopology = _XupsTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 1, 13)
)


class _XupsTopologyType_Type(Integer32):
    """Custom type xupsTopologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_XupsTopologyType_Type.__name__ = "Integer32"
_XupsTopologyType_Object = MibScalar
xupsTopologyType = _XupsTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 13, 1),
    _XupsTopologyType_Type()
)
xupsTopologyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsTopologyType.setStatus("mandatory")


class _XupsTopoMachineCode_Type(Integer32):
    """Custom type xupsTopoMachineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_XupsTopoMachineCode_Type.__name__ = "Integer32"
_XupsTopoMachineCode_Object = MibScalar
xupsTopoMachineCode = _XupsTopoMachineCode_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 13, 2),
    _XupsTopoMachineCode_Type()
)
xupsTopoMachineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsTopoMachineCode.setStatus("mandatory")


class _XupsTopoUnitNumber_Type(Integer32):
    """Custom type xupsTopoUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_XupsTopoUnitNumber_Type.__name__ = "Integer32"
_XupsTopoUnitNumber_Object = MibScalar
xupsTopoUnitNumber = _XupsTopoUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 13, 3),
    _XupsTopoUnitNumber_Type()
)
xupsTopoUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xupsTopoUnitNumber.setStatus("mandatory")


class _XupsTopoPowerStrategy_Type(Integer32):
    """Custom type xupsTopoPowerStrategy based on Integer32"""
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
        *(("enableHighEfficiency", 3),
          ("highAlert", 1),
          ("immediateHighEfficiency", 4),
          ("standard", 2))
    )


_XupsTopoPowerStrategy_Type.__name__ = "Integer32"
_XupsTopoPowerStrategy_Object = MibScalar
xupsTopoPowerStrategy = _XupsTopoPowerStrategy_Object(
    (1, 3, 6, 1, 4, 1, 534, 1, 13, 4),
    _XupsTopoPowerStrategy_Type()
)
xupsTopoPowerStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xupsTopoPowerStrategy.setStatus("mandatory")
_XupsObjectId_ObjectIdentity = ObjectIdentity
xupsObjectId = _XupsObjectId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2)
)
_PowerwareEthernetSnmpAdapter_ObjectIdentity = ObjectIdentity
powerwareEthernetSnmpAdapter = _PowerwareEthernetSnmpAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 1)
)
_PowerwareNetworkSnmpAdapterEther_ObjectIdentity = ObjectIdentity
powerwareNetworkSnmpAdapterEther = _PowerwareNetworkSnmpAdapterEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 2)
)
_PowerwareNetworkSnmpAdapterToken_ObjectIdentity = ObjectIdentity
powerwareNetworkSnmpAdapterToken = _PowerwareNetworkSnmpAdapterToken_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 3)
)
_OnlinetDaemon_ObjectIdentity = ObjectIdentity
onlinetDaemon = _OnlinetDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 4)
)
_ConnectUPSAdapterEthernet_ObjectIdentity = ObjectIdentity
connectUPSAdapterEthernet = _ConnectUPSAdapterEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 5)
)
_PowerwareNetworkDigitalIOEther_ObjectIdentity = ObjectIdentity
powerwareNetworkDigitalIOEther = _PowerwareNetworkDigitalIOEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 6)
)
_ConnectUPSAdapterTokenRing_ObjectIdentity = ObjectIdentity
connectUPSAdapterTokenRing = _ConnectUPSAdapterTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 7)
)
_SimpleSnmpAdapter_ObjectIdentity = ObjectIdentity
simpleSnmpAdapter = _SimpleSnmpAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 2, 8)
)

# Managed Objects groups


# Notification objects

xupstbControlOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 1)
)
if mibBuilder.loadTexts:
    xupstbControlOff.setStatus(
        ""
    )

xupstbControlOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 2)
)
if mibBuilder.loadTexts:
    xupstbControlOn.setStatus(
        ""
    )

xupstbOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 3)
)
if mibBuilder.loadTexts:
    xupstbOnBattery.setStatus(
        ""
    )

xupstbLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 4)
)
if mibBuilder.loadTexts:
    xupstbLowBattery.setStatus(
        ""
    )

xupstbUtilityPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 5)
)
if mibBuilder.loadTexts:
    xupstbUtilityPowerRestored.setStatus(
        ""
    )

xupstbReturnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 6)
)
if mibBuilder.loadTexts:
    xupstbReturnFromLowBattery.setStatus(
        ""
    )

xupstbOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 7)
)
if mibBuilder.loadTexts:
    xupstbOutputOverload.setStatus(
        ""
    )

xupstbInternalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 8)
)
if mibBuilder.loadTexts:
    xupstbInternalFailure.setStatus(
        ""
    )

xupstbBatteryDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 9)
)
if mibBuilder.loadTexts:
    xupstbBatteryDischarged.setStatus(
        ""
    )

xupstbInverterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 10)
)
if mibBuilder.loadTexts:
    xupstbInverterFailure.setStatus(
        ""
    )

xupstbOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 11)
)
if mibBuilder.loadTexts:
    xupstbOnBypass.setStatus(
        ""
    )

xupstbBypassNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 12)
)
if mibBuilder.loadTexts:
    xupstbBypassNotAvailable.setStatus(
        ""
    )

xupstbOutputOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 13)
)
if mibBuilder.loadTexts:
    xupstbOutputOff.setStatus(
        ""
    )

xupstbInputFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 14)
)
if mibBuilder.loadTexts:
    xupstbInputFailure.setStatus(
        ""
    )

xupstbBuildingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 15)
)
if mibBuilder.loadTexts:
    xupstbBuildingAlarm.setStatus(
        ""
    )

xupstbShutdownImminent = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 16)
)
if mibBuilder.loadTexts:
    xupstbShutdownImminent.setStatus(
        ""
    )

xupstbOnInverter = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 17)
)
if mibBuilder.loadTexts:
    xupstbOnInverter.setStatus(
        ""
    )

xupstbBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 20)
)
if mibBuilder.loadTexts:
    xupstbBreakerOpen.setStatus(
        ""
    )

xupstbAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 21)
)
if mibBuilder.loadTexts:
    xupstbAlarmEntryAdded.setStatus(
        ""
    )

xupstbAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 0, 0, 0, 22)
)
if mibBuilder.loadTexts:
    xupstbAlarmEntryRemoved.setStatus(
        ""
    )

xupstdControlOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 1)
)
xupstdControlOff.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdControlOff.setStatus(
        ""
    )

xupstdControlOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 2)
)
xupstdControlOn.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdControlOn.setStatus(
        ""
    )

xupstdOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 3)
)
xupstdOnBattery.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOnBattery.setStatus(
        ""
    )

xupstdLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 4)
)
xupstdLowBattery.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdLowBattery.setStatus(
        ""
    )

xupstdUtilityPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 5)
)
xupstdUtilityPowerRestored.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdUtilityPowerRestored.setStatus(
        ""
    )

xupstdReturnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 6)
)
xupstdReturnFromLowBattery.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdReturnFromLowBattery.setStatus(
        ""
    )

xupstdOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 7)
)
xupstdOutputOverload.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOutputOverload.setStatus(
        ""
    )

xupstdInternalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 8)
)
xupstdInternalFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdInternalFailure.setStatus(
        ""
    )

xupstdBatteryDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 9)
)
xupstdBatteryDischarged.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdBatteryDischarged.setStatus(
        ""
    )

xupstdInverterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 10)
)
xupstdInverterFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdInverterFailure.setStatus(
        ""
    )

xupstdOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 11)
)
xupstdOnBypass.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOnBypass.setStatus(
        ""
    )

xupstdBypassNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 12)
)
xupstdBypassNotAvailable.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdBypassNotAvailable.setStatus(
        ""
    )

xupstdOutputOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 13)
)
xupstdOutputOff.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOutputOff.setStatus(
        ""
    )

xupstdInputFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 14)
)
xupstdInputFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdInputFailure.setStatus(
        ""
    )

xupstdBuildingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 15)
)
xupstdBuildingAlarm.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdBuildingAlarm.setStatus(
        ""
    )

xupstdShutdownImminent = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 16)
)
xupstdShutdownImminent.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdShutdownImminent.setStatus(
        ""
    )

xupstdOnInverter = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 17)
)
xupstdOnInverter.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOnInverter.setStatus(
        ""
    )

xupstdBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 20)
)
xupstdBreakerOpen.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdBreakerOpen.setStatus(
        ""
    )

xupstdAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 21)
)
xupstdAlarmEntryAdded.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmEntryAdded.setStatus(
        ""
    )

xupstdAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 22)
)
xupstdAlarmEntryRemoved.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmEntryRemoved.setStatus(
        ""
    )

xupstdAlarmBatteryBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 23)
)
xupstdAlarmBatteryBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmBatteryBad.setStatus(
        ""
    )

xupstdOutputOffAsRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 24)
)
xupstdOutputOffAsRequested.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdOutputOffAsRequested.setStatus(
        ""
    )

xupstdDiagnosticTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 25)
)
xupstdDiagnosticTestFailed.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdDiagnosticTestFailed.setStatus(
        ""
    )

xupstdCommunicationsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 26)
)
xupstdCommunicationsLost.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdCommunicationsLost.setStatus(
        ""
    )

xupstdUpsShutdownPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 27)
)
xupstdUpsShutdownPending.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdUpsShutdownPending.setStatus(
        ""
    )

xupstdAlarmTestInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 28)
)
xupstdAlarmTestInProgress.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmTestInProgress.setStatus(
        ""
    )

xupstdAmbientTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 29)
)
xupstdAmbientTempBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("XUPS-MIB", "xupsEnvAmbientTemp"),
        ("XUPS-MIB", "xupsEnvAmbientLowerLimit"),
        ("XUPS-MIB", "xupsEnvAmbientUpperLimit"))
)
if mibBuilder.loadTexts:
    xupstdAmbientTempBad.setStatus(
        ""
    )

xupstdContactActiveNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 30)
)
xupstdContactActiveNotice.setObjects(
      *(("XUPS-MIB", "xupsContactIndex"),
        ("XUPS-MIB", "xupsContactType"),
        ("XUPS-MIB", "xupsContactState"),
        ("XUPS-MIB", "xupsContactDescr"))
)
if mibBuilder.loadTexts:
    xupstdContactActiveNotice.setStatus(
        ""
    )

xupstdContactInactiveNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 31)
)
xupstdContactInactiveNotice.setObjects(
      *(("XUPS-MIB", "xupsContactIndex"),
        ("XUPS-MIB", "xupsContactType"),
        ("XUPS-MIB", "xupsContactState"),
        ("XUPS-MIB", "xupsContactDescr"))
)
if mibBuilder.loadTexts:
    xupstdContactInactiveNotice.setStatus(
        ""
    )

xupstdLossOfRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 32)
)
xupstdLossOfRedundancy.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdLossOfRedundancy.setStatus(
        ""
    )

xupstdAlarmTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 33)
)
xupstdAlarmTempBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmTempBad.setStatus(
        ""
    )

xupstdAlarmChargerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 34)
)
xupstdAlarmChargerFailed.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmChargerFailed.setStatus(
        ""
    )

xupstdAlarmFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 35)
)
xupstdAlarmFanFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmFanFailure.setStatus(
        ""
    )

xupstdAlarmFuseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 36)
)
xupstdAlarmFuseFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAlarmFuseFailure.setStatus(
        ""
    )

xupstdPowerSwitchBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 37)
)
xupstdPowerSwitchBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdPowerSwitchBad.setStatus(
        ""
    )

xupstdModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 38)
)
xupstdModuleFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdModuleFailure.setStatus(
        ""
    )

xupstdOnAlternatePowerSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 39)
)
xupstdOnAlternatePowerSource.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("XUPS-MIB", "xupsInputSource"))
)
if mibBuilder.loadTexts:
    xupstdOnAlternatePowerSource.setStatus(
        ""
    )

xupstdAltPowerNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 40)
)
xupstdAltPowerNotAvailable.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdAltPowerNotAvailable.setStatus(
        ""
    )

xupstdNoticeCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 41)
)
xupstdNoticeCondition.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"))
)
if mibBuilder.loadTexts:
    xupstdNoticeCondition.setStatus(
        ""
    )

xupstdRemoteTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 42)
)
xupstdRemoteTempBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("XUPS-MIB", "xupsEnvRemoteTemp"),
        ("XUPS-MIB", "xupsEnvRemoteTempLowerLimit"),
        ("XUPS-MIB", "xupsEnvRemoteTempUpperLimit"))
)
if mibBuilder.loadTexts:
    xupstdRemoteTempBad.setStatus(
        ""
    )

xupstdRemoteHumidityBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 1, 0, 43)
)
xupstdRemoteHumidityBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("XUPS-MIB", "xupsEnvRemoteHumidity"),
        ("XUPS-MIB", "xupsEnvRemoteHumidityLowerLimit"),
        ("XUPS-MIB", "xupsEnvRemoteHumidityUpperLimit"))
)
if mibBuilder.loadTexts:
    xupstdRemoteHumidityBad.setStatus(
        ""
    )

xupstpControlOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 1)
)
xupstpControlOff.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpControlOff.setStatus(
        ""
    )

xupstpControlOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 2)
)
xupstpControlOn.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpControlOn.setStatus(
        ""
    )

xupstpOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 3)
)
xupstpOnBattery.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpOnBattery.setStatus(
        ""
    )

xupstpLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 4)
)
xupstpLowBattery.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpLowBattery.setStatus(
        ""
    )

xupstpUtilityPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 5)
)
xupstpUtilityPowerRestored.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpUtilityPowerRestored.setStatus(
        ""
    )

xupstpReturnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 6)
)
xupstpReturnFromLowBattery.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpReturnFromLowBattery.setStatus(
        ""
    )

xupstpOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 7)
)
xupstpOutputOverload.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpOutputOverload.setStatus(
        ""
    )

xupstpInternalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 8)
)
xupstpInternalFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpInternalFailure.setStatus(
        ""
    )

xupstpBatteryDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 9)
)
xupstpBatteryDischarged.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpBatteryDischarged.setStatus(
        ""
    )

xupstpInverterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 10)
)
xupstpInverterFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpInverterFailure.setStatus(
        ""
    )

xupstpOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 11)
)
xupstpOnBypass.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpOnBypass.setStatus(
        ""
    )

xupstpBypassNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 12)
)
xupstpBypassNotAvailable.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpBypassNotAvailable.setStatus(
        ""
    )

xupstpOutputOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 13)
)
xupstpOutputOff.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpOutputOff.setStatus(
        ""
    )

xupstpInputFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 14)
)
xupstpInputFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpInputFailure.setStatus(
        ""
    )

xupstpBuildingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 15)
)
xupstpBuildingAlarm.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpBuildingAlarm.setStatus(
        ""
    )

xupstpShutdownImminent = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 16)
)
xupstpShutdownImminent.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpShutdownImminent.setStatus(
        ""
    )

xupstpOnInverter = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 17)
)
xupstpOnInverter.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpOnInverter.setStatus(
        ""
    )

xupstpBreakerOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 20)
)
xupstpBreakerOpen.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpBreakerOpen.setStatus(
        ""
    )

xupstpAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 21)
)
xupstpAlarmEntryAdded.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpAlarmEntryAdded.setStatus(
        ""
    )

xupstpAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 22)
)
xupstpAlarmEntryRemoved.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpAlarmEntryRemoved.setStatus(
        ""
    )

xupstpAlarmBatteryBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 23)
)
xupstpAlarmBatteryBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpAlarmBatteryBad.setStatus(
        ""
    )

xupstpOutputOffAsRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 24)
)
xupstpOutputOffAsRequested.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpOutputOffAsRequested.setStatus(
        ""
    )

xupstpDiagnosticTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 25)
)
xupstpDiagnosticTestFailed.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpDiagnosticTestFailed.setStatus(
        ""
    )

xupstpCommunicationsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 26)
)
xupstpCommunicationsLost.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpCommunicationsLost.setStatus(
        ""
    )

xupstpUpsShutdownPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 27)
)
xupstpUpsShutdownPending.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpUpsShutdownPending.setStatus(
        ""
    )

xupstpAlarmTestInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 28)
)
xupstpAlarmTestInProgress.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpAlarmTestInProgress.setStatus(
        ""
    )

xupstpAmbientTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 29)
)
xupstpAmbientTempBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("XUPS-MIB", "xupsEnvAmbientTemp"),
        ("XUPS-MIB", "xupsEnvAmbientLowerLimit"),
        ("XUPS-MIB", "xupsEnvAmbientUpperLimit"))
)
if mibBuilder.loadTexts:
    xupstpAmbientTempBad.setStatus(
        ""
    )

xupstpLossOfRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 32)
)
xupstpLossOfRedundancy.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpLossOfRedundancy.setStatus(
        ""
    )

xupstpAlarmTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 33)
)
xupstpAlarmTempBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpAlarmTempBad.setStatus(
        ""
    )

xupstpAlarmChargerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 34)
)
xupstpAlarmChargerFailed.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpAlarmChargerFailed.setStatus(
        ""
    )

xupstpAlarmFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 35)
)
xupstpAlarmFanFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpAlarmFanFailure.setStatus(
        ""
    )

xupstpAlarmFuseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 36)
)
xupstpAlarmFuseFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpAlarmFuseFailure.setStatus(
        ""
    )

xupstpPowerSwitchBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 37)
)
xupstpPowerSwitchBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpPowerSwitchBad.setStatus(
        ""
    )

xupstpModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 38)
)
xupstpModuleFailure.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpModuleFailure.setStatus(
        ""
    )

xupstpOnAlternatePowerSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 39)
)
xupstpOnAlternatePowerSource.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("XUPS-MIB", "xupsInputSource"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpOnAlternatePowerSource.setStatus(
        ""
    )

xupstpAltPowerNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 40)
)
xupstpAltPowerNotAvailable.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpAltPowerNotAvailable.setStatus(
        ""
    )

xupstpNoticeCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 41)
)
xupstpNoticeCondition.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    xupstpNoticeCondition.setStatus(
        ""
    )

xupstpRemoteTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 42)
)
xupstpRemoteTempBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("XUPS-MIB", "xupsEnvRemoteTemp"),
        ("XUPS-MIB", "xupsEnvRemoteTempLowerLimit"),
        ("XUPS-MIB", "xupsEnvRemoteTempUpperLimit"))
)
if mibBuilder.loadTexts:
    xupstpRemoteTempBad.setStatus(
        ""
    )

xupstpRemoteHumidityBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 1, 11, 4, 2, 0, 43)
)
xupstpRemoteHumidityBad.setObjects(
      *(("XUPS-MIB", "xupsAlarmID"),
        ("XUPS-MIB", "xupsAlarmDescr"),
        ("XUPS-MIB", "xupsTrapMessage"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("XUPS-MIB", "xupsEnvRemoteHumidity"),
        ("XUPS-MIB", "xupsEnvRemoteHumidityLowerLimit"),
        ("XUPS-MIB", "xupsEnvRemoteHumidityUpperLimit"))
)
if mibBuilder.loadTexts:
    xupstpRemoteHumidityBad.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XUPS-MIB",
    **{"powerware": powerware,
       "xups": xups,
       "xupsNull": xupsNull,
       "xupsTrapBasic": xupsTrapBasic,
       "xupstbControlOff": xupstbControlOff,
       "xupstbControlOn": xupstbControlOn,
       "xupstbOnBattery": xupstbOnBattery,
       "xupstbLowBattery": xupstbLowBattery,
       "xupstbUtilityPowerRestored": xupstbUtilityPowerRestored,
       "xupstbReturnFromLowBattery": xupstbReturnFromLowBattery,
       "xupstbOutputOverload": xupstbOutputOverload,
       "xupstbInternalFailure": xupstbInternalFailure,
       "xupstbBatteryDischarged": xupstbBatteryDischarged,
       "xupstbInverterFailure": xupstbInverterFailure,
       "xupstbOnBypass": xupstbOnBypass,
       "xupstbBypassNotAvailable": xupstbBypassNotAvailable,
       "xupstbOutputOff": xupstbOutputOff,
       "xupstbInputFailure": xupstbInputFailure,
       "xupstbBuildingAlarm": xupstbBuildingAlarm,
       "xupstbShutdownImminent": xupstbShutdownImminent,
       "xupstbOnInverter": xupstbOnInverter,
       "xupstbBreakerOpen": xupstbBreakerOpen,
       "xupstbAlarmEntryAdded": xupstbAlarmEntryAdded,
       "xupstbAlarmEntryRemoved": xupstbAlarmEntryRemoved,
       "xupsIdent": xupsIdent,
       "xupsIdentManufacturer": xupsIdentManufacturer,
       "xupsIdentModel": xupsIdentModel,
       "xupsIdentSoftwareVersion": xupsIdentSoftwareVersion,
       "xupsIdentOemCode": xupsIdentOemCode,
       "xupsBattery": xupsBattery,
       "xupsBatTimeRemaining": xupsBatTimeRemaining,
       "xupsBatVoltage": xupsBatVoltage,
       "xupsBatCurrent": xupsBatCurrent,
       "xupsBatCapacity": xupsBatCapacity,
       "xupsBatteryAbmStatus": xupsBatteryAbmStatus,
       "xupsInput": xupsInput,
       "xupsInputFrequency": xupsInputFrequency,
       "xupsInputLineBads": xupsInputLineBads,
       "xupsInputNumPhases": xupsInputNumPhases,
       "xupsInputTable": xupsInputTable,
       "xupsInputEntry": xupsInputEntry,
       "xupsInputPhase": xupsInputPhase,
       "xupsInputVoltage": xupsInputVoltage,
       "xupsInputCurrent": xupsInputCurrent,
       "xupsInputWatts": xupsInputWatts,
       "xupsInputSource": xupsInputSource,
       "xupsOutput": xupsOutput,
       "xupsOutputLoad": xupsOutputLoad,
       "xupsOutputFrequency": xupsOutputFrequency,
       "xupsOutputNumPhases": xupsOutputNumPhases,
       "xupsOutputTable": xupsOutputTable,
       "xupsOutputEntry": xupsOutputEntry,
       "xupsOutputPhase": xupsOutputPhase,
       "xupsOutputVoltage": xupsOutputVoltage,
       "xupsOutputCurrent": xupsOutputCurrent,
       "xupsOutputWatts": xupsOutputWatts,
       "xupsOutputSource": xupsOutputSource,
       "xupsBypass": xupsBypass,
       "xupsBypassFrequency": xupsBypassFrequency,
       "xupsBypassNumPhases": xupsBypassNumPhases,
       "xupsBypassTable": xupsBypassTable,
       "xupsBypassEntry": xupsBypassEntry,
       "xupsBypassPhase": xupsBypassPhase,
       "xupsBypassVoltage": xupsBypassVoltage,
       "xupsEnvironment": xupsEnvironment,
       "xupsEnvAmbientTemp": xupsEnvAmbientTemp,
       "xupsEnvAmbientLowerLimit": xupsEnvAmbientLowerLimit,
       "xupsEnvAmbientUpperLimit": xupsEnvAmbientUpperLimit,
       "xupsEnvAmbientHumidity": xupsEnvAmbientHumidity,
       "xupsEnvRemoteTemp": xupsEnvRemoteTemp,
       "xupsEnvRemoteHumidity": xupsEnvRemoteHumidity,
       "xupsEnvNumContacts": xupsEnvNumContacts,
       "xupsContactSenseTable": xupsContactSenseTable,
       "xupsContactsTableEntry": xupsContactsTableEntry,
       "xupsContactIndex": xupsContactIndex,
       "xupsContactType": xupsContactType,
       "xupsContactState": xupsContactState,
       "xupsContactDescr": xupsContactDescr,
       "xupsEnvRemoteTempLowerLimit": xupsEnvRemoteTempLowerLimit,
       "xupsEnvRemoteTempUpperLimit": xupsEnvRemoteTempUpperLimit,
       "xupsEnvRemoteHumidityLowerLimit": xupsEnvRemoteHumidityLowerLimit,
       "xupsEnvRemoteHumidityUpperLimit": xupsEnvRemoteHumidityUpperLimit,
       "xupsAlarm": xupsAlarm,
       "xupsAlarms": xupsAlarms,
       "xupsAlarmTable": xupsAlarmTable,
       "xupsAlarmEntry": xupsAlarmEntry,
       "xupsAlarmID": xupsAlarmID,
       "xupsAlarmDescr": xupsAlarmDescr,
       "xupsAlarmTime": xupsAlarmTime,
       "xupsOnBattery": xupsOnBattery,
       "xupsLowBattery": xupsLowBattery,
       "xupsUtilityPowerRestored": xupsUtilityPowerRestored,
       "xupsReturnFromLowBattery": xupsReturnFromLowBattery,
       "xupsOutputOverload": xupsOutputOverload,
       "xupsInternalFailure": xupsInternalFailure,
       "xupsBatteryDischarged": xupsBatteryDischarged,
       "xupsInverterFailure": xupsInverterFailure,
       "xupsOnBypass": xupsOnBypass,
       "xupsBypassNotAvailable": xupsBypassNotAvailable,
       "xupsOutputOff": xupsOutputOff,
       "xupsInputFailure": xupsInputFailure,
       "xupsBuildingAlarm": xupsBuildingAlarm,
       "xupsShutdownImminent": xupsShutdownImminent,
       "xupsOnInverter": xupsOnInverter,
       "xupsAlarmNumEvents": xupsAlarmNumEvents,
       "xupsAlarmEventTable": xupsAlarmEventTable,
       "xupsAlarmEventEntry": xupsAlarmEventEntry,
       "xupsAlarmEventID": xupsAlarmEventID,
       "xupsAlarmEventDateAndTime": xupsAlarmEventDateAndTime,
       "xupsAlarmEventKind": xupsAlarmEventKind,
       "xupsAlarmEventDescr": xupsAlarmEventDescr,
       "xupsAlarmEventMsg": xupsAlarmEventMsg,
       "xupsBreakerOpen": xupsBreakerOpen,
       "xupsAlarmEntryAdded": xupsAlarmEntryAdded,
       "xupsAlarmEntryRemoved": xupsAlarmEntryRemoved,
       "xupsAlarmBatteryBad": xupsAlarmBatteryBad,
       "xupsOutputOffAsRequested": xupsOutputOffAsRequested,
       "xupsDiagnosticTestFailed": xupsDiagnosticTestFailed,
       "xupsCommunicationsLost": xupsCommunicationsLost,
       "xupsUpsShutdownPending": xupsUpsShutdownPending,
       "xupsAlarmTestInProgress": xupsAlarmTestInProgress,
       "xupsAmbientTempBad": xupsAmbientTempBad,
       "xupsLossOfRedundancy": xupsLossOfRedundancy,
       "xupsAlarmTempBad": xupsAlarmTempBad,
       "xupsAlarmChargerFailed": xupsAlarmChargerFailed,
       "xupsAlarmFanFailure": xupsAlarmFanFailure,
       "xupsAlarmFuseFailure": xupsAlarmFuseFailure,
       "xupsPowerSwitchBad": xupsPowerSwitchBad,
       "xupsModuleFailure": xupsModuleFailure,
       "xupsOnAlternatePowerSource": xupsOnAlternatePowerSource,
       "xupsAltPowerNotAvailable": xupsAltPowerNotAvailable,
       "xupsNoticeCondition": xupsNoticeCondition,
       "xupsRemoteTempBad": xupsRemoteTempBad,
       "xupsRemoteHumidityBad": xupsRemoteHumidityBad,
       "xupsTest": xupsTest,
       "xupsTestBattery": xupsTestBattery,
       "xupsTestBatteryStatus": xupsTestBatteryStatus,
       "xupsControl": xupsControl,
       "xupsControlOutputOffDelay": xupsControlOutputOffDelay,
       "xupsControlOutputOnDelay": xupsControlOutputOnDelay,
       "xupsControlOutputOffTrapDelay": xupsControlOutputOffTrapDelay,
       "xupsControlOutputOnTrapDelay": xupsControlOutputOnTrapDelay,
       "xupsControlToBypassDelay": xupsControlToBypassDelay,
       "xupsLoadShedSecsWithRestart": xupsLoadShedSecsWithRestart,
       "xupsConfig": xupsConfig,
       "xupsConfigOutputVoltage": xupsConfigOutputVoltage,
       "xupsConfigInputVoltage": xupsConfigInputVoltage,
       "xupsConfigOutputWatts": xupsConfigOutputWatts,
       "xupsConfigOutputFreq": xupsConfigOutputFreq,
       "xupsConfigDateAndTime": xupsConfigDateAndTime,
       "xupsConfigLowOutputVoltageLimit": xupsConfigLowOutputVoltageLimit,
       "xupsConfigHighOutputVoltageLimit": xupsConfigHighOutputVoltageLimit,
       "xupsTrapControl": xupsTrapControl,
       "xupsMaxTrapLevel": xupsMaxTrapLevel,
       "xupsSendTrapType": xupsSendTrapType,
       "xupsTrapMessage": xupsTrapMessage,
       "xupsTrapSource": xupsTrapSource,
       "xupsTrapDefined": xupsTrapDefined,
       "xupstdControlOff": xupstdControlOff,
       "xupstdControlOn": xupstdControlOn,
       "xupstdOnBattery": xupstdOnBattery,
       "xupstdLowBattery": xupstdLowBattery,
       "xupstdUtilityPowerRestored": xupstdUtilityPowerRestored,
       "xupstdReturnFromLowBattery": xupstdReturnFromLowBattery,
       "xupstdOutputOverload": xupstdOutputOverload,
       "xupstdInternalFailure": xupstdInternalFailure,
       "xupstdBatteryDischarged": xupstdBatteryDischarged,
       "xupstdInverterFailure": xupstdInverterFailure,
       "xupstdOnBypass": xupstdOnBypass,
       "xupstdBypassNotAvailable": xupstdBypassNotAvailable,
       "xupstdOutputOff": xupstdOutputOff,
       "xupstdInputFailure": xupstdInputFailure,
       "xupstdBuildingAlarm": xupstdBuildingAlarm,
       "xupstdShutdownImminent": xupstdShutdownImminent,
       "xupstdOnInverter": xupstdOnInverter,
       "xupstdBreakerOpen": xupstdBreakerOpen,
       "xupstdAlarmEntryAdded": xupstdAlarmEntryAdded,
       "xupstdAlarmEntryRemoved": xupstdAlarmEntryRemoved,
       "xupstdAlarmBatteryBad": xupstdAlarmBatteryBad,
       "xupstdOutputOffAsRequested": xupstdOutputOffAsRequested,
       "xupstdDiagnosticTestFailed": xupstdDiagnosticTestFailed,
       "xupstdCommunicationsLost": xupstdCommunicationsLost,
       "xupstdUpsShutdownPending": xupstdUpsShutdownPending,
       "xupstdAlarmTestInProgress": xupstdAlarmTestInProgress,
       "xupstdAmbientTempBad": xupstdAmbientTempBad,
       "xupstdContactActiveNotice": xupstdContactActiveNotice,
       "xupstdContactInactiveNotice": xupstdContactInactiveNotice,
       "xupstdLossOfRedundancy": xupstdLossOfRedundancy,
       "xupstdAlarmTempBad": xupstdAlarmTempBad,
       "xupstdAlarmChargerFailed": xupstdAlarmChargerFailed,
       "xupstdAlarmFanFailure": xupstdAlarmFanFailure,
       "xupstdAlarmFuseFailure": xupstdAlarmFuseFailure,
       "xupstdPowerSwitchBad": xupstdPowerSwitchBad,
       "xupstdModuleFailure": xupstdModuleFailure,
       "xupstdOnAlternatePowerSource": xupstdOnAlternatePowerSource,
       "xupstdAltPowerNotAvailable": xupstdAltPowerNotAvailable,
       "xupstdNoticeCondition": xupstdNoticeCondition,
       "xupstdRemoteTempBad": xupstdRemoteTempBad,
       "xupstdRemoteHumidityBad": xupstdRemoteHumidityBad,
       "xupsTrapPortN": xupsTrapPortN,
       "xupstpControlOff": xupstpControlOff,
       "xupstpControlOn": xupstpControlOn,
       "xupstpOnBattery": xupstpOnBattery,
       "xupstpLowBattery": xupstpLowBattery,
       "xupstpUtilityPowerRestored": xupstpUtilityPowerRestored,
       "xupstpReturnFromLowBattery": xupstpReturnFromLowBattery,
       "xupstpOutputOverload": xupstpOutputOverload,
       "xupstpInternalFailure": xupstpInternalFailure,
       "xupstpBatteryDischarged": xupstpBatteryDischarged,
       "xupstpInverterFailure": xupstpInverterFailure,
       "xupstpOnBypass": xupstpOnBypass,
       "xupstpBypassNotAvailable": xupstpBypassNotAvailable,
       "xupstpOutputOff": xupstpOutputOff,
       "xupstpInputFailure": xupstpInputFailure,
       "xupstpBuildingAlarm": xupstpBuildingAlarm,
       "xupstpShutdownImminent": xupstpShutdownImminent,
       "xupstpOnInverter": xupstpOnInverter,
       "xupstpBreakerOpen": xupstpBreakerOpen,
       "xupstpAlarmEntryAdded": xupstpAlarmEntryAdded,
       "xupstpAlarmEntryRemoved": xupstpAlarmEntryRemoved,
       "xupstpAlarmBatteryBad": xupstpAlarmBatteryBad,
       "xupstpOutputOffAsRequested": xupstpOutputOffAsRequested,
       "xupstpDiagnosticTestFailed": xupstpDiagnosticTestFailed,
       "xupstpCommunicationsLost": xupstpCommunicationsLost,
       "xupstpUpsShutdownPending": xupstpUpsShutdownPending,
       "xupstpAlarmTestInProgress": xupstpAlarmTestInProgress,
       "xupstpAmbientTempBad": xupstpAmbientTempBad,
       "xupstpLossOfRedundancy": xupstpLossOfRedundancy,
       "xupstpAlarmTempBad": xupstpAlarmTempBad,
       "xupstpAlarmChargerFailed": xupstpAlarmChargerFailed,
       "xupstpAlarmFanFailure": xupstpAlarmFanFailure,
       "xupstpAlarmFuseFailure": xupstpAlarmFuseFailure,
       "xupstpPowerSwitchBad": xupstpPowerSwitchBad,
       "xupstpModuleFailure": xupstpModuleFailure,
       "xupstpOnAlternatePowerSource": xupstpOnAlternatePowerSource,
       "xupstpAltPowerNotAvailable": xupstpAltPowerNotAvailable,
       "xupstpNoticeCondition": xupstpNoticeCondition,
       "xupstpRemoteTempBad": xupstpRemoteTempBad,
       "xupstpRemoteHumidityBad": xupstpRemoteHumidityBad,
       "xupsRecep": xupsRecep,
       "xupsNumReceptacles": xupsNumReceptacles,
       "xupsRecepTable": xupsRecepTable,
       "xupsRecepEntry": xupsRecepEntry,
       "xupsRecepIndex": xupsRecepIndex,
       "xupsRecepStatus": xupsRecepStatus,
       "xupsRecepOffDelaySecs": xupsRecepOffDelaySecs,
       "xupsRecepOnDelaySecs": xupsRecepOnDelaySecs,
       "xupsRecepAutoOffDelay": xupsRecepAutoOffDelay,
       "xupsRecepAutoOnDelay": xupsRecepAutoOnDelay,
       "xupsRecepShedSecsWithRestart": xupsRecepShedSecsWithRestart,
       "xupsTopology": xupsTopology,
       "xupsTopologyType": xupsTopologyType,
       "xupsTopoMachineCode": xupsTopoMachineCode,
       "xupsTopoUnitNumber": xupsTopoUnitNumber,
       "xupsTopoPowerStrategy": xupsTopoPowerStrategy,
       "xupsObjectId": xupsObjectId,
       "powerwareEthernetSnmpAdapter": powerwareEthernetSnmpAdapter,
       "powerwareNetworkSnmpAdapterEther": powerwareNetworkSnmpAdapterEther,
       "powerwareNetworkSnmpAdapterToken": powerwareNetworkSnmpAdapterToken,
       "onlinetDaemon": onlinetDaemon,
       "connectUPSAdapterEthernet": connectUPSAdapterEthernet,
       "powerwareNetworkDigitalIOEther": powerwareNetworkDigitalIOEther,
       "connectUPSAdapterTokenRing": connectUPSAdapterTokenRing,
       "simpleSnmpAdapter": simpleSnmpAdapter}
)
