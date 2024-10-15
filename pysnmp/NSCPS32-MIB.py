# SNMP MIB module (NSCPS32-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSCPS32-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:31 2024
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

(nsc,
 nscProducts) = mibBuilder.importSymbols(
    "NSC-MIB",
    "nsc",
    "nscProducts")

(Party,) = mibBuilder.importSymbols(
    "RFC1353-MIB",
    "Party")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NscHippiSwitch_ObjectIdentity = ObjectIdentity
nscHippiSwitch = _NscHippiSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4)
)
_Ps32General_ObjectIdentity = ObjectIdentity
ps32General = _Ps32General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1)
)


class _Ps32SwitchDescr_Type(DisplayString):
    """Custom type ps32SwitchDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_Ps32SwitchDescr_Type.__name__ = "DisplayString"
_Ps32SwitchDescr_Object = MibScalar
ps32SwitchDescr = _Ps32SwitchDescr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 1),
    _Ps32SwitchDescr_Type()
)
ps32SwitchDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SwitchDescr.setStatus("mandatory")


class _Ps32SwitchVersion_Type(DisplayString):
    """Custom type ps32SwitchVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32SwitchVersion_Type.__name__ = "DisplayString"
_Ps32SwitchVersion_Object = MibScalar
ps32SwitchVersion = _Ps32SwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 2),
    _Ps32SwitchVersion_Type()
)
ps32SwitchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SwitchVersion.setStatus("mandatory")


class _Ps32SwitchDate_Type(DisplayString):
    """Custom type ps32SwitchDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_Ps32SwitchDate_Type.__name__ = "DisplayString"
_Ps32SwitchDate_Object = MibScalar
ps32SwitchDate = _Ps32SwitchDate_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 3),
    _Ps32SwitchDate_Type()
)
ps32SwitchDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32SwitchDate.setStatus("mandatory")


class _Ps32SwitchTime_Type(DisplayString):
    """Custom type ps32SwitchTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_Ps32SwitchTime_Type.__name__ = "DisplayString"
_Ps32SwitchTime_Object = MibScalar
ps32SwitchTime = _Ps32SwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 4),
    _Ps32SwitchTime_Type()
)
ps32SwitchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32SwitchTime.setStatus("mandatory")


class _Ps32SwitchAdminStatus_Type(Integer32):
    """Custom type ps32SwitchAdminStatus based on Integer32"""
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
        *(("disable", 3),
          ("enable", 2),
          ("programload", 5),
          ("reset", 4),
          ("test", 6),
          ("unknown", 1))
    )


_Ps32SwitchAdminStatus_Type.__name__ = "Integer32"
_Ps32SwitchAdminStatus_Object = MibScalar
ps32SwitchAdminStatus = _Ps32SwitchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 5),
    _Ps32SwitchAdminStatus_Type()
)
ps32SwitchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32SwitchAdminStatus.setStatus("mandatory")


class _Ps32SwitchOperStatus_Type(Integer32):
    """Custom type ps32SwitchOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("fatalError", 8),
          ("invalid", 2),
          ("loading", 10),
          ("nonFatalError", 7),
          ("operational", 4),
          ("other", 1),
          ("resetInProgress", 5),
          ("testing", 3),
          ("warning", 6))
    )


_Ps32SwitchOperStatus_Type.__name__ = "Integer32"
_Ps32SwitchOperStatus_Object = MibScalar
ps32SwitchOperStatus = _Ps32SwitchOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 6),
    _Ps32SwitchOperStatus_Type()
)
ps32SwitchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SwitchOperStatus.setStatus("mandatory")
_Ps32SwitchPhysicalChanges_Type = Counter32
_Ps32SwitchPhysicalChanges_Object = MibScalar
ps32SwitchPhysicalChanges = _Ps32SwitchPhysicalChanges_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 7),
    _Ps32SwitchPhysicalChanges_Type()
)
ps32SwitchPhysicalChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SwitchPhysicalChanges.setStatus("mandatory")


class _Ps32SwitchDiagnosticReg_Type(DisplayString):
    """Custom type ps32SwitchDiagnosticReg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Ps32SwitchDiagnosticReg_Type.__name__ = "DisplayString"
_Ps32SwitchDiagnosticReg_Object = MibScalar
ps32SwitchDiagnosticReg = _Ps32SwitchDiagnosticReg_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 8),
    _Ps32SwitchDiagnosticReg_Type()
)
ps32SwitchDiagnosticReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SwitchDiagnosticReg.setStatus("mandatory")


class _Ps32SwitchMiscellanReg_Type(DisplayString):
    """Custom type ps32SwitchMiscellanReg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Ps32SwitchMiscellanReg_Type.__name__ = "DisplayString"
_Ps32SwitchMiscellanReg_Object = MibScalar
ps32SwitchMiscellanReg = _Ps32SwitchMiscellanReg_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 9),
    _Ps32SwitchMiscellanReg_Type()
)
ps32SwitchMiscellanReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SwitchMiscellanReg.setStatus("mandatory")


class _Ps32SwitchDipSwitchReg_Type(DisplayString):
    """Custom type ps32SwitchDipSwitchReg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Ps32SwitchDipSwitchReg_Type.__name__ = "DisplayString"
_Ps32SwitchDipSwitchReg_Object = MibScalar
ps32SwitchDipSwitchReg = _Ps32SwitchDipSwitchReg_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 10),
    _Ps32SwitchDipSwitchReg_Type()
)
ps32SwitchDipSwitchReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SwitchDipSwitchReg.setStatus("mandatory")
_Ps32PowerSupply_ObjectIdentity = ObjectIdentity
ps32PowerSupply = _Ps32PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2)
)


class _Ps32NumPowerSupplies_Type(Integer32):
    """Custom type ps32NumPowerSupplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Ps32NumPowerSupplies_Type.__name__ = "Integer32"
_Ps32NumPowerSupplies_Object = MibScalar
ps32NumPowerSupplies = _Ps32NumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 1),
    _Ps32NumPowerSupplies_Type()
)
ps32NumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32NumPowerSupplies.setStatus("mandatory")
_Ps32PowerSupplyTable_Object = MibTable
ps32PowerSupplyTable = _Ps32PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    ps32PowerSupplyTable.setStatus("mandatory")
_Ps32PowerSupplyEntry_Object = MibTableRow
ps32PowerSupplyEntry = _Ps32PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1)
)
ps32PowerSupplyEntry.setIndexNames(
    (0, "NSCPS32-MIB", "ps32PowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    ps32PowerSupplyEntry.setStatus("mandatory")
_Ps32PowerSupplyIndex_Type = Integer32
_Ps32PowerSupplyIndex_Object = MibTableColumn
ps32PowerSupplyIndex = _Ps32PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 1),
    _Ps32PowerSupplyIndex_Type()
)
ps32PowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerSupplyIndex.setStatus("mandatory")


class _Ps32PowerSupplyDescr_Type(DisplayString):
    """Custom type ps32PowerSupplyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32PowerSupplyDescr_Type.__name__ = "DisplayString"
_Ps32PowerSupplyDescr_Object = MibTableColumn
ps32PowerSupplyDescr = _Ps32PowerSupplyDescr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 2),
    _Ps32PowerSupplyDescr_Type()
)
ps32PowerSupplyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerSupplyDescr.setStatus("mandatory")


class _Ps32PowerSupplyAdminStatus_Type(Integer32):
    """Custom type ps32PowerSupplyAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("unknown", 1))
    )


_Ps32PowerSupplyAdminStatus_Type.__name__ = "Integer32"
_Ps32PowerSupplyAdminStatus_Object = MibTableColumn
ps32PowerSupplyAdminStatus = _Ps32PowerSupplyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 3),
    _Ps32PowerSupplyAdminStatus_Type()
)
ps32PowerSupplyAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32PowerSupplyAdminStatus.setStatus("mandatory")


class _Ps32PowerSupplyOperStatus_Type(Integer32):
    """Custom type ps32PowerSupplyOperStatus based on Integer32"""
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
        *(("bad", 4),
          ("disabled", 3),
          ("empty", 2),
          ("engaged", 7),
          ("redundant", 8),
          ("standby", 6),
          ("unknown", 1),
          ("warning", 5))
    )


_Ps32PowerSupplyOperStatus_Type.__name__ = "Integer32"
_Ps32PowerSupplyOperStatus_Object = MibTableColumn
ps32PowerSupplyOperStatus = _Ps32PowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 4),
    _Ps32PowerSupplyOperStatus_Type()
)
ps32PowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerSupplyOperStatus.setStatus("mandatory")


class _Ps32PowerSupplyHealthText_Type(DisplayString):
    """Custom type ps32PowerSupplyHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ps32PowerSupplyHealthText_Type.__name__ = "DisplayString"
_Ps32PowerSupplyHealthText_Object = MibTableColumn
ps32PowerSupplyHealthText = _Ps32PowerSupplyHealthText_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 5),
    _Ps32PowerSupplyHealthText_Type()
)
ps32PowerSupplyHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerSupplyHealthText.setStatus("mandatory")
_Ps32PowerSupplyWarnings_Type = Counter32
_Ps32PowerSupplyWarnings_Object = MibTableColumn
ps32PowerSupplyWarnings = _Ps32PowerSupplyWarnings_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 6),
    _Ps32PowerSupplyWarnings_Type()
)
ps32PowerSupplyWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerSupplyWarnings.setStatus("mandatory")
_Ps32PowerSupplyFailures_Type = Counter32
_Ps32PowerSupplyFailures_Object = MibTableColumn
ps32PowerSupplyFailures = _Ps32PowerSupplyFailures_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 7),
    _Ps32PowerSupplyFailures_Type()
)
ps32PowerSupplyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerSupplyFailures.setStatus("mandatory")


class _Ps32NumPowerOutputs_Type(Integer32):
    """Custom type ps32NumPowerOutputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ps32NumPowerOutputs_Type.__name__ = "Integer32"
_Ps32NumPowerOutputs_Object = MibScalar
ps32NumPowerOutputs = _Ps32NumPowerOutputs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 3),
    _Ps32NumPowerOutputs_Type()
)
ps32NumPowerOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32NumPowerOutputs.setStatus("mandatory")
_Ps32PowerOutputTable_Object = MibTable
ps32PowerOutputTable = _Ps32PowerOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    ps32PowerOutputTable.setStatus("mandatory")
_Ps32PowerOutputEntry_Object = MibTableRow
ps32PowerOutputEntry = _Ps32PowerOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1)
)
ps32PowerOutputEntry.setIndexNames(
    (0, "NSCPS32-MIB", "ps32PowerSupplyIndex"),
    (0, "NSCPS32-MIB", "ps32PowerOutputIndex"),
)
if mibBuilder.loadTexts:
    ps32PowerOutputEntry.setStatus("mandatory")
_Ps32PowerOutputIndex_Type = Integer32
_Ps32PowerOutputIndex_Object = MibTableColumn
ps32PowerOutputIndex = _Ps32PowerOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 1),
    _Ps32PowerOutputIndex_Type()
)
ps32PowerOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerOutputIndex.setStatus("mandatory")


class _Ps32PowerOutputStatus_Type(Integer32):
    """Custom type ps32PowerOutputStatus based on Integer32"""
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
        *(("bad", 2),
          ("good", 4),
          ("unknown", 1),
          ("warning", 3))
    )


_Ps32PowerOutputStatus_Type.__name__ = "Integer32"
_Ps32PowerOutputStatus_Object = MibTableColumn
ps32PowerOutputStatus = _Ps32PowerOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 2),
    _Ps32PowerOutputStatus_Type()
)
ps32PowerOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerOutputStatus.setStatus("mandatory")
_Ps32PowerOutputNominalVoltage_Type = Integer32
_Ps32PowerOutputNominalVoltage_Object = MibTableColumn
ps32PowerOutputNominalVoltage = _Ps32PowerOutputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 3),
    _Ps32PowerOutputNominalVoltage_Type()
)
ps32PowerOutputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerOutputNominalVoltage.setStatus("mandatory")
_Ps32PowerOutputOfferedVoltage_Type = Integer32
_Ps32PowerOutputOfferedVoltage_Object = MibTableColumn
ps32PowerOutputOfferedVoltage = _Ps32PowerOutputOfferedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 4),
    _Ps32PowerOutputOfferedVoltage_Type()
)
ps32PowerOutputOfferedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerOutputOfferedVoltage.setStatus("mandatory")
_Ps32PowerOutputWarnings_Type = Counter32
_Ps32PowerOutputWarnings_Object = MibTableColumn
ps32PowerOutputWarnings = _Ps32PowerOutputWarnings_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 5),
    _Ps32PowerOutputWarnings_Type()
)
ps32PowerOutputWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerOutputWarnings.setStatus("mandatory")
_Ps32PowerOutputFailures_Type = Counter32
_Ps32PowerOutputFailures_Object = MibTableColumn
ps32PowerOutputFailures = _Ps32PowerOutputFailures_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 6),
    _Ps32PowerOutputFailures_Type()
)
ps32PowerOutputFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PowerOutputFailures.setStatus("mandatory")
_Ps32Environ_ObjectIdentity = ObjectIdentity
ps32Environ = _Ps32Environ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3)
)


class _Ps32NumEnvironmentSensors_Type(Integer32):
    """Custom type ps32NumEnvironmentSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ps32NumEnvironmentSensors_Type.__name__ = "Integer32"
_Ps32NumEnvironmentSensors_Object = MibScalar
ps32NumEnvironmentSensors = _Ps32NumEnvironmentSensors_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 1),
    _Ps32NumEnvironmentSensors_Type()
)
ps32NumEnvironmentSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32NumEnvironmentSensors.setStatus("mandatory")
_Ps32EnvironTable_Object = MibTable
ps32EnvironTable = _Ps32EnvironTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    ps32EnvironTable.setStatus("mandatory")
_Ps32EnvironEntry_Object = MibTableRow
ps32EnvironEntry = _Ps32EnvironEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1)
)
ps32EnvironEntry.setIndexNames(
    (0, "NSCPS32-MIB", "ps32EnvironIndex"),
)
if mibBuilder.loadTexts:
    ps32EnvironEntry.setStatus("mandatory")
_Ps32EnvironIndex_Type = Integer32
_Ps32EnvironIndex_Object = MibTableColumn
ps32EnvironIndex = _Ps32EnvironIndex_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 1),
    _Ps32EnvironIndex_Type()
)
ps32EnvironIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32EnvironIndex.setStatus("mandatory")


class _Ps32EnvironSensor_Type(Integer32):
    """Custom type ps32EnvironSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fanfailure", 3),
          ("logicovertemp", 2),
          ("unknown", 1))
    )


_Ps32EnvironSensor_Type.__name__ = "Integer32"
_Ps32EnvironSensor_Object = MibTableColumn
ps32EnvironSensor = _Ps32EnvironSensor_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 2),
    _Ps32EnvironSensor_Type()
)
ps32EnvironSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32EnvironSensor.setStatus("mandatory")


class _Ps32EnvironStatus_Type(Integer32):
    """Custom type ps32EnvironStatus based on Integer32"""
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
        *(("bad", 2),
          ("good", 4),
          ("unknown", 1),
          ("warning", 3))
    )


_Ps32EnvironStatus_Type.__name__ = "Integer32"
_Ps32EnvironStatus_Object = MibTableColumn
ps32EnvironStatus = _Ps32EnvironStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 3),
    _Ps32EnvironStatus_Type()
)
ps32EnvironStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32EnvironStatus.setStatus("mandatory")
_Ps32EnvironWarnings_Type = Counter32
_Ps32EnvironWarnings_Object = MibTableColumn
ps32EnvironWarnings = _Ps32EnvironWarnings_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 4),
    _Ps32EnvironWarnings_Type()
)
ps32EnvironWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32EnvironWarnings.setStatus("mandatory")
_Ps32EnvironFailures_Type = Counter32
_Ps32EnvironFailures_Object = MibTableColumn
ps32EnvironFailures = _Ps32EnvironFailures_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 5),
    _Ps32EnvironFailures_Type()
)
ps32EnvironFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32EnvironFailures.setStatus("mandatory")


class _Ps32EnvironDescriptor_Type(DisplayString):
    """Custom type ps32EnvironDescriptor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_Ps32EnvironDescriptor_Type.__name__ = "DisplayString"
_Ps32EnvironDescriptor_Object = MibTableColumn
ps32EnvironDescriptor = _Ps32EnvironDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 6),
    _Ps32EnvironDescriptor_Type()
)
ps32EnvironDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32EnvironDescriptor.setStatus("mandatory")


class _Ps32EnvironHealthText_Type(DisplayString):
    """Custom type ps32EnvironHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_Ps32EnvironHealthText_Type.__name__ = "DisplayString"
_Ps32EnvironHealthText_Object = MibTableColumn
ps32EnvironHealthText = _Ps32EnvironHealthText_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 7),
    _Ps32EnvironHealthText_Type()
)
ps32EnvironHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32EnvironHealthText.setStatus("mandatory")
_Ps32Slot_ObjectIdentity = ObjectIdentity
ps32Slot = _Ps32Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4)
)


class _Ps32NumSlots_Type(Integer32):
    """Custom type ps32NumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ps32NumSlots_Type.__name__ = "Integer32"
_Ps32NumSlots_Object = MibScalar
ps32NumSlots = _Ps32NumSlots_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 1),
    _Ps32NumSlots_Type()
)
ps32NumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32NumSlots.setStatus("mandatory")
_Ps32SlotTable_Object = MibTable
ps32SlotTable = _Ps32SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    ps32SlotTable.setStatus("mandatory")
_Ps32SlotEntry_Object = MibTableRow
ps32SlotEntry = _Ps32SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1)
)
ps32SlotEntry.setIndexNames(
    (0, "NSCPS32-MIB", "ps32SlotNumber"),
)
if mibBuilder.loadTexts:
    ps32SlotEntry.setStatus("mandatory")


class _Ps32SlotNumber_Type(Integer32):
    """Custom type ps32SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_Ps32SlotNumber_Type.__name__ = "Integer32"
_Ps32SlotNumber_Object = MibTableColumn
ps32SlotNumber = _Ps32SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1, 1),
    _Ps32SlotNumber_Type()
)
ps32SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SlotNumber.setStatus("mandatory")


class _Ps32SlotPartNumber_Type(DisplayString):
    """Custom type ps32SlotPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Ps32SlotPartNumber_Type.__name__ = "DisplayString"
_Ps32SlotPartNumber_Object = MibTableColumn
ps32SlotPartNumber = _Ps32SlotPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1, 2),
    _Ps32SlotPartNumber_Type()
)
ps32SlotPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SlotPartNumber.setStatus("mandatory")


class _Ps32SlotBoardID_Type(DisplayString):
    """Custom type ps32SlotBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_Ps32SlotBoardID_Type.__name__ = "DisplayString"
_Ps32SlotBoardID_Object = MibTableColumn
ps32SlotBoardID = _Ps32SlotBoardID_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1, 3),
    _Ps32SlotBoardID_Type()
)
ps32SlotBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SlotBoardID.setStatus("mandatory")


class _Ps32SlotBoardText_Type(DisplayString):
    """Custom type ps32SlotBoardText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_Ps32SlotBoardText_Type.__name__ = "DisplayString"
_Ps32SlotBoardText_Object = MibTableColumn
ps32SlotBoardText = _Ps32SlotBoardText_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1, 4),
    _Ps32SlotBoardText_Type()
)
ps32SlotBoardText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SlotBoardText.setStatus("mandatory")
_Ps32SlotLastChange_Type = TimeTicks
_Ps32SlotLastChange_Object = MibTableColumn
ps32SlotLastChange = _Ps32SlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1, 5),
    _Ps32SlotLastChange_Type()
)
ps32SlotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32SlotLastChange.setStatus("mandatory")
_Ps32Port_ObjectIdentity = ObjectIdentity
ps32Port = _Ps32Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5)
)


class _Ps32MaximumPorts_Type(Integer32):
    """Custom type ps32MaximumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ps32MaximumPorts_Type.__name__ = "Integer32"
_Ps32MaximumPorts_Object = MibScalar
ps32MaximumPorts = _Ps32MaximumPorts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 1),
    _Ps32MaximumPorts_Type()
)
ps32MaximumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32MaximumPorts.setStatus("mandatory")


class _Ps32InstalledPorts_Type(Integer32):
    """Custom type ps32InstalledPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ps32InstalledPorts_Type.__name__ = "Integer32"
_Ps32InstalledPorts_Object = MibScalar
ps32InstalledPorts = _Ps32InstalledPorts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 2),
    _Ps32InstalledPorts_Type()
)
ps32InstalledPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32InstalledPorts.setStatus("mandatory")
_Ps32PortTable_Object = MibTable
ps32PortTable = _Ps32PortTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3)
)
if mibBuilder.loadTexts:
    ps32PortTable.setStatus("mandatory")
_Ps32PortEntry_Object = MibTableRow
ps32PortEntry = _Ps32PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1)
)
ps32PortEntry.setIndexNames(
    (0, "NSCPS32-MIB", "ps32PortNumber"),
)
if mibBuilder.loadTexts:
    ps32PortEntry.setStatus("mandatory")


class _Ps32PortNumber_Type(Integer32):
    """Custom type ps32PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Ps32PortNumber_Type.__name__ = "Integer32"
_Ps32PortNumber_Object = MibTableColumn
ps32PortNumber = _Ps32PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 1),
    _Ps32PortNumber_Type()
)
ps32PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PortNumber.setStatus("mandatory")
_Ps32PortBoard_Type = ObjectIdentifier
_Ps32PortBoard_Object = MibTableColumn
ps32PortBoard = _Ps32PortBoard_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 2),
    _Ps32PortBoard_Type()
)
ps32PortBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PortBoard.setStatus("mandatory")
_Ps32PortInput_Type = ObjectIdentifier
_Ps32PortInput_Object = MibTableColumn
ps32PortInput = _Ps32PortInput_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 3),
    _Ps32PortInput_Type()
)
ps32PortInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PortInput.setStatus("mandatory")
_Ps32PortOutput_Type = ObjectIdentifier
_Ps32PortOutput_Object = MibTableColumn
ps32PortOutput = _Ps32PortOutput_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 4),
    _Ps32PortOutput_Type()
)
ps32PortOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PortOutput.setStatus("mandatory")
_Ps32PortForce_Type = Integer32
_Ps32PortForce_Object = MibTableColumn
ps32PortForce = _Ps32PortForce_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 5),
    _Ps32PortForce_Type()
)
ps32PortForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32PortForce.setStatus("mandatory")
_Ps32PortCounterStatus_Type = Integer32
_Ps32PortCounterStatus_Object = MibTableColumn
ps32PortCounterStatus = _Ps32PortCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 6),
    _Ps32PortCounterStatus_Type()
)
ps32PortCounterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32PortCounterStatus.setStatus("mandatory")
_Ps32PortOverrunCount_Type = Integer32
_Ps32PortOverrunCount_Object = MibTableColumn
ps32PortOverrunCount = _Ps32PortOverrunCount_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 7),
    _Ps32PortOverrunCount_Type()
)
ps32PortOverrunCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32PortOverrunCount.setStatus("mandatory")
_Ps32PortSwitchRejectCount_Type = Integer32
_Ps32PortSwitchRejectCount_Object = MibTableColumn
ps32PortSwitchRejectCount = _Ps32PortSwitchRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 8),
    _Ps32PortSwitchRejectCount_Type()
)
ps32PortSwitchRejectCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32PortSwitchRejectCount.setStatus("mandatory")
_Ps32PortCamponDelayCount_Type = Integer32
_Ps32PortCamponDelayCount_Object = MibTableColumn
ps32PortCamponDelayCount = _Ps32PortCamponDelayCount_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 9),
    _Ps32PortCamponDelayCount_Type()
)
ps32PortCamponDelayCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32PortCamponDelayCount.setStatus("mandatory")


class _Ps32PortCurrentStatus_Type(DisplayString):
    """Custom type ps32PortCurrentStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Ps32PortCurrentStatus_Type.__name__ = "DisplayString"
_Ps32PortCurrentStatus_Object = MibTableColumn
ps32PortCurrentStatus = _Ps32PortCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 10),
    _Ps32PortCurrentStatus_Type()
)
ps32PortCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PortCurrentStatus.setStatus("mandatory")


class _Ps32PortAdminStatus_Type(Integer32):
    """Custom type ps32PortAdminStatus based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("clrall", 9),
          ("clrerrors", 6),
          ("clrpaths", 7),
          ("clrstats", 8),
          ("disable", 3),
          ("enable", 2),
          ("reset", 4),
          ("rstrpath", 10),
          ("savecfg", 11),
          ("savepath", 12),
          ("test", 5),
          ("unknown", 1))
    )


_Ps32PortAdminStatus_Type.__name__ = "Integer32"
_Ps32PortAdminStatus_Object = MibTableColumn
ps32PortAdminStatus = _Ps32PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 11),
    _Ps32PortAdminStatus_Type()
)
ps32PortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32PortAdminStatus.setStatus("mandatory")


class _Ps32PortOperStatus_Type(Integer32):
    """Custom type ps32PortOperStatus based on Integer32"""
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
        *(("connected", 5),
          ("disabled", 3),
          ("inerror", 7),
          ("intest", 6),
          ("notinstalled", 2),
          ("operational", 4),
          ("unknown", 1))
    )


_Ps32PortOperStatus_Type.__name__ = "Integer32"
_Ps32PortOperStatus_Object = MibTableColumn
ps32PortOperStatus = _Ps32PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 12),
    _Ps32PortOperStatus_Type()
)
ps32PortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PortOperStatus.setStatus("mandatory")
_Ps32Pathway_ObjectIdentity = ObjectIdentity
ps32Pathway = _Ps32Pathway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6)
)


class _Ps32MaximumPathways_Type(Integer32):
    """Custom type ps32MaximumPathways based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ps32MaximumPathways_Type.__name__ = "Integer32"
_Ps32MaximumPathways_Object = MibScalar
ps32MaximumPathways = _Ps32MaximumPathways_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 1),
    _Ps32MaximumPathways_Type()
)
ps32MaximumPathways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32MaximumPathways.setStatus("mandatory")
_Ps32PathwayTable_Object = MibTable
ps32PathwayTable = _Ps32PathwayTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2)
)
if mibBuilder.loadTexts:
    ps32PathwayTable.setStatus("mandatory")
_Ps32PathwayEntry_Object = MibTableRow
ps32PathwayEntry = _Ps32PathwayEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2, 1)
)
ps32PathwayEntry.setIndexNames(
    (0, "NSCPS32-MIB", "ps32PathwayPortNumber"),
    (0, "NSCPS32-MIB", "ps32PathwayHDA"),
)
if mibBuilder.loadTexts:
    ps32PathwayEntry.setStatus("mandatory")
_Ps32PathwayPortNumber_Type = Integer32
_Ps32PathwayPortNumber_Object = MibTableColumn
ps32PathwayPortNumber = _Ps32PathwayPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2, 1, 1),
    _Ps32PathwayPortNumber_Type()
)
ps32PathwayPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PathwayPortNumber.setStatus("mandatory")


class _Ps32PathwayHDA_Type(PhysAddress):
    """Custom type ps32PathwayHDA based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Ps32PathwayHDA_Type.__name__ = "PhysAddress"
_Ps32PathwayHDA_Object = MibTableColumn
ps32PathwayHDA = _Ps32PathwayHDA_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2, 1, 2),
    _Ps32PathwayHDA_Type()
)
ps32PathwayHDA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ps32PathwayHDA.setStatus("mandatory")
_Ps32PathwayDest_Type = DisplayString
_Ps32PathwayDest_Object = MibTableColumn
ps32PathwayDest = _Ps32PathwayDest_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2, 1, 3),
    _Ps32PathwayDest_Type()
)
ps32PathwayDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32PathwayDest.setStatus("mandatory")
_Ps32PathwayClear_Type = Integer32
_Ps32PathwayClear_Object = MibTableColumn
ps32PathwayClear = _Ps32PathwayClear_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2, 1, 4),
    _Ps32PathwayClear_Type()
)
ps32PathwayClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ps32PathwayClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCPS32-MIB",
    **{"nscHippiSwitch": nscHippiSwitch,
       "ps32General": ps32General,
       "ps32SwitchDescr": ps32SwitchDescr,
       "ps32SwitchVersion": ps32SwitchVersion,
       "ps32SwitchDate": ps32SwitchDate,
       "ps32SwitchTime": ps32SwitchTime,
       "ps32SwitchAdminStatus": ps32SwitchAdminStatus,
       "ps32SwitchOperStatus": ps32SwitchOperStatus,
       "ps32SwitchPhysicalChanges": ps32SwitchPhysicalChanges,
       "ps32SwitchDiagnosticReg": ps32SwitchDiagnosticReg,
       "ps32SwitchMiscellanReg": ps32SwitchMiscellanReg,
       "ps32SwitchDipSwitchReg": ps32SwitchDipSwitchReg,
       "ps32PowerSupply": ps32PowerSupply,
       "ps32NumPowerSupplies": ps32NumPowerSupplies,
       "ps32PowerSupplyTable": ps32PowerSupplyTable,
       "ps32PowerSupplyEntry": ps32PowerSupplyEntry,
       "ps32PowerSupplyIndex": ps32PowerSupplyIndex,
       "ps32PowerSupplyDescr": ps32PowerSupplyDescr,
       "ps32PowerSupplyAdminStatus": ps32PowerSupplyAdminStatus,
       "ps32PowerSupplyOperStatus": ps32PowerSupplyOperStatus,
       "ps32PowerSupplyHealthText": ps32PowerSupplyHealthText,
       "ps32PowerSupplyWarnings": ps32PowerSupplyWarnings,
       "ps32PowerSupplyFailures": ps32PowerSupplyFailures,
       "ps32NumPowerOutputs": ps32NumPowerOutputs,
       "ps32PowerOutputTable": ps32PowerOutputTable,
       "ps32PowerOutputEntry": ps32PowerOutputEntry,
       "ps32PowerOutputIndex": ps32PowerOutputIndex,
       "ps32PowerOutputStatus": ps32PowerOutputStatus,
       "ps32PowerOutputNominalVoltage": ps32PowerOutputNominalVoltage,
       "ps32PowerOutputOfferedVoltage": ps32PowerOutputOfferedVoltage,
       "ps32PowerOutputWarnings": ps32PowerOutputWarnings,
       "ps32PowerOutputFailures": ps32PowerOutputFailures,
       "ps32Environ": ps32Environ,
       "ps32NumEnvironmentSensors": ps32NumEnvironmentSensors,
       "ps32EnvironTable": ps32EnvironTable,
       "ps32EnvironEntry": ps32EnvironEntry,
       "ps32EnvironIndex": ps32EnvironIndex,
       "ps32EnvironSensor": ps32EnvironSensor,
       "ps32EnvironStatus": ps32EnvironStatus,
       "ps32EnvironWarnings": ps32EnvironWarnings,
       "ps32EnvironFailures": ps32EnvironFailures,
       "ps32EnvironDescriptor": ps32EnvironDescriptor,
       "ps32EnvironHealthText": ps32EnvironHealthText,
       "ps32Slot": ps32Slot,
       "ps32NumSlots": ps32NumSlots,
       "ps32SlotTable": ps32SlotTable,
       "ps32SlotEntry": ps32SlotEntry,
       "ps32SlotNumber": ps32SlotNumber,
       "ps32SlotPartNumber": ps32SlotPartNumber,
       "ps32SlotBoardID": ps32SlotBoardID,
       "ps32SlotBoardText": ps32SlotBoardText,
       "ps32SlotLastChange": ps32SlotLastChange,
       "ps32Port": ps32Port,
       "ps32MaximumPorts": ps32MaximumPorts,
       "ps32InstalledPorts": ps32InstalledPorts,
       "ps32PortTable": ps32PortTable,
       "ps32PortEntry": ps32PortEntry,
       "ps32PortNumber": ps32PortNumber,
       "ps32PortBoard": ps32PortBoard,
       "ps32PortInput": ps32PortInput,
       "ps32PortOutput": ps32PortOutput,
       "ps32PortForce": ps32PortForce,
       "ps32PortCounterStatus": ps32PortCounterStatus,
       "ps32PortOverrunCount": ps32PortOverrunCount,
       "ps32PortSwitchRejectCount": ps32PortSwitchRejectCount,
       "ps32PortCamponDelayCount": ps32PortCamponDelayCount,
       "ps32PortCurrentStatus": ps32PortCurrentStatus,
       "ps32PortAdminStatus": ps32PortAdminStatus,
       "ps32PortOperStatus": ps32PortOperStatus,
       "ps32Pathway": ps32Pathway,
       "ps32MaximumPathways": ps32MaximumPathways,
       "ps32PathwayTable": ps32PathwayTable,
       "ps32PathwayEntry": ps32PathwayEntry,
       "ps32PathwayPortNumber": ps32PathwayPortNumber,
       "ps32PathwayHDA": ps32PathwayHDA,
       "ps32PathwayDest": ps32PathwayDest,
       "ps32PathwayClear": ps32PathwayClear}
)
