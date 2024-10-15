# SNMP MIB module (HPNSAENV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSAENV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:20 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaEnvironment_ObjectIdentity = ObjectIdentity
hpnsaEnvironment = _HpnsaEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26)
)
_HpnsaEnvMibRev_ObjectIdentity = ObjectIdentity
hpnsaEnvMibRev = _HpnsaEnvMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 1)
)


class _HpnsaEnvMibRevMajor_Type(Integer32):
    """Custom type hpnsaEnvMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvMibRevMajor_Type.__name__ = "Integer32"
_HpnsaEnvMibRevMajor_Object = MibScalar
hpnsaEnvMibRevMajor = _HpnsaEnvMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 1, 1),
    _HpnsaEnvMibRevMajor_Type()
)
hpnsaEnvMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvMibRevMajor.setStatus("mandatory")


class _HpnsaEnvMibRevMinor_Type(Integer32):
    """Custom type hpnsaEnvMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvMibRevMinor_Type.__name__ = "Integer32"
_HpnsaEnvMibRevMinor_Object = MibScalar
hpnsaEnvMibRevMinor = _HpnsaEnvMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 1, 2),
    _HpnsaEnvMibRevMinor_Type()
)
hpnsaEnvMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvMibRevMinor.setStatus("mandatory")
_HpnsaEnvVoltageData_ObjectIdentity = ObjectIdentity
hpnsaEnvVoltageData = _HpnsaEnvVoltageData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2)
)
_HpnsaEnvVoltageSensorTable_Object = MibTable
hpnsaEnvVoltageSensorTable = _HpnsaEnvVoltageSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorTable.setStatus("mandatory")
_HpnsaEnvVoltageSensorEntry_Object = MibTableRow
hpnsaEnvVoltageSensorEntry = _HpnsaEnvVoltageSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1)
)
hpnsaEnvVoltageSensorEntry.setIndexNames(
    (0, "HPNSAENV-MIB", "hpnsaEnvVoltageSensorIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorEntry.setStatus("mandatory")


class _HpnsaEnvVoltageSensorIndex_Type(Integer32):
    """Custom type hpnsaEnvVoltageSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEnvVoltageSensorIndex_Type.__name__ = "Integer32"
_HpnsaEnvVoltageSensorIndex_Object = MibTableColumn
hpnsaEnvVoltageSensorIndex = _HpnsaEnvVoltageSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 1),
    _HpnsaEnvVoltageSensorIndex_Type()
)
hpnsaEnvVoltageSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorIndex.setStatus("mandatory")


class _HpnsaEnvVoltageSensorType_Type(Integer32):
    """Custom type hpnsaEnvVoltageSensorType based on Integer32"""
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
        *(("analog", 3),
          ("digital", 4),
          ("four-state-discrete", 6),
          ("other", 1),
          ("three-state-discrete", 5),
          ("unknown", 2))
    )


_HpnsaEnvVoltageSensorType_Type.__name__ = "Integer32"
_HpnsaEnvVoltageSensorType_Object = MibTableColumn
hpnsaEnvVoltageSensorType = _HpnsaEnvVoltageSensorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 2),
    _HpnsaEnvVoltageSensorType_Type()
)
hpnsaEnvVoltageSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorType.setStatus("mandatory")


class _HpnsaEnvVoltageSensorLocation_Type(Integer32):
    """Custom type hpnsaEnvVoltageSensorLocation based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("add-in-card", 11),
          ("disk", 4),
          ("memory-module", 8),
          ("motherboard", 7),
          ("other", 1),
          ("peripheral-bay", 5),
          ("power-unit", 10),
          ("processor", 3),
          ("processor-module", 9),
          ("system-management-module", 6),
          ("unknown", 2))
    )


_HpnsaEnvVoltageSensorLocation_Type.__name__ = "Integer32"
_HpnsaEnvVoltageSensorLocation_Object = MibTableColumn
hpnsaEnvVoltageSensorLocation = _HpnsaEnvVoltageSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 3),
    _HpnsaEnvVoltageSensorLocation_Type()
)
hpnsaEnvVoltageSensorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorLocation.setStatus("mandatory")


class _HpnsaEnvVoltageSensorDescription_Type(Integer32):
    """Custom type hpnsaEnvVoltageSensorDescription based on Integer32"""
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("voltsensor-minus-12-volt", 6),
          ("voltsensor-minus-5-volt", 4),
          ("voltsensor-other", 1),
          ("voltsensor-plus-12-volt", 5),
          ("voltsensor-plus-2-5-volt", 8),
          ("voltsensor-plus-3-3-volt", 7),
          ("voltsensor-plus-5-volt", 3),
          ("voltsensor-processor-1", 10),
          ("voltsensor-processor-2", 11),
          ("voltsensor-processor-3", 12),
          ("voltsensor-processor-4", 13),
          ("voltsensor-scsi-terminator", 9),
          ("voltsensor-unknown", 2))
    )


_HpnsaEnvVoltageSensorDescription_Type.__name__ = "Integer32"
_HpnsaEnvVoltageSensorDescription_Object = MibTableColumn
hpnsaEnvVoltageSensorDescription = _HpnsaEnvVoltageSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 4),
    _HpnsaEnvVoltageSensorDescription_Type()
)
hpnsaEnvVoltageSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorDescription.setStatus("mandatory")


class _HpnsaEnvVoltageSensorStatus_Type(Integer32):
    """Custom type hpnsaEnvVoltageSensorStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-critical", 4),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_HpnsaEnvVoltageSensorStatus_Type.__name__ = "Integer32"
_HpnsaEnvVoltageSensorStatus_Object = MibTableColumn
hpnsaEnvVoltageSensorStatus = _HpnsaEnvVoltageSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 5),
    _HpnsaEnvVoltageSensorStatus_Type()
)
hpnsaEnvVoltageSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorStatus.setStatus("mandatory")
_HpnsaEnvVoltageSensorLevel_Type = Integer32
_HpnsaEnvVoltageSensorLevel_Object = MibTableColumn
hpnsaEnvVoltageSensorLevel = _HpnsaEnvVoltageSensorLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 6),
    _HpnsaEnvVoltageSensorLevel_Type()
)
hpnsaEnvVoltageSensorLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorLevel.setStatus("mandatory")
_HpnsaEnvVoltageSensorNominalLevel_Type = Integer32
_HpnsaEnvVoltageSensorNominalLevel_Object = MibTableColumn
hpnsaEnvVoltageSensorNominalLevel = _HpnsaEnvVoltageSensorNominalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 7),
    _HpnsaEnvVoltageSensorNominalLevel_Type()
)
hpnsaEnvVoltageSensorNominalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorNominalLevel.setStatus("mandatory")
_HpnsaEnvVoltageSensorNormalMaximum_Type = Integer32
_HpnsaEnvVoltageSensorNormalMaximum_Object = MibTableColumn
hpnsaEnvVoltageSensorNormalMaximum = _HpnsaEnvVoltageSensorNormalMaximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 8),
    _HpnsaEnvVoltageSensorNormalMaximum_Type()
)
hpnsaEnvVoltageSensorNormalMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorNormalMaximum.setStatus("mandatory")
_HpnsaEnvVoltageSensorNormalMinimum_Type = Integer32
_HpnsaEnvVoltageSensorNormalMinimum_Object = MibTableColumn
hpnsaEnvVoltageSensorNormalMinimum = _HpnsaEnvVoltageSensorNormalMinimum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 9),
    _HpnsaEnvVoltageSensorNormalMinimum_Type()
)
hpnsaEnvVoltageSensorNormalMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorNormalMinimum.setStatus("mandatory")
_HpnsaEnvVoltageSensorMaximum_Type = Integer32
_HpnsaEnvVoltageSensorMaximum_Object = MibTableColumn
hpnsaEnvVoltageSensorMaximum = _HpnsaEnvVoltageSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 10),
    _HpnsaEnvVoltageSensorMaximum_Type()
)
hpnsaEnvVoltageSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorMaximum.setStatus("mandatory")
_HpnsaEnvVoltageSensorMinimum_Type = Integer32
_HpnsaEnvVoltageSensorMinimum_Object = MibTableColumn
hpnsaEnvVoltageSensorMinimum = _HpnsaEnvVoltageSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 11),
    _HpnsaEnvVoltageSensorMinimum_Type()
)
hpnsaEnvVoltageSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorMinimum.setStatus("mandatory")
_HpnsaEnvVoltageSensorLowerNonCriticalThreshold_Type = Integer32
_HpnsaEnvVoltageSensorLowerNonCriticalThreshold_Object = MibTableColumn
hpnsaEnvVoltageSensorLowerNonCriticalThreshold = _HpnsaEnvVoltageSensorLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 12),
    _HpnsaEnvVoltageSensorLowerNonCriticalThreshold_Type()
)
hpnsaEnvVoltageSensorLowerNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorLowerNonCriticalThreshold.setStatus("mandatory")
_HpnsaEnvVoltageSensorUpperNonCriticalThreshold_Type = Integer32
_HpnsaEnvVoltageSensorUpperNonCriticalThreshold_Object = MibTableColumn
hpnsaEnvVoltageSensorUpperNonCriticalThreshold = _HpnsaEnvVoltageSensorUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 13),
    _HpnsaEnvVoltageSensorUpperNonCriticalThreshold_Type()
)
hpnsaEnvVoltageSensorUpperNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorUpperNonCriticalThreshold.setStatus("mandatory")
_HpnsaEnvVoltageSensorLowerCriticalThreshold_Type = Integer32
_HpnsaEnvVoltageSensorLowerCriticalThreshold_Object = MibTableColumn
hpnsaEnvVoltageSensorLowerCriticalThreshold = _HpnsaEnvVoltageSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 14),
    _HpnsaEnvVoltageSensorLowerCriticalThreshold_Type()
)
hpnsaEnvVoltageSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorLowerCriticalThreshold.setStatus("mandatory")
_HpnsaEnvVoltageSensorUpperCriticalThreshold_Type = Integer32
_HpnsaEnvVoltageSensorUpperCriticalThreshold_Object = MibTableColumn
hpnsaEnvVoltageSensorUpperCriticalThreshold = _HpnsaEnvVoltageSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 15),
    _HpnsaEnvVoltageSensorUpperCriticalThreshold_Type()
)
hpnsaEnvVoltageSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorUpperCriticalThreshold.setStatus("mandatory")
_HpnsaEnvVoltageSensorLowerNonRecoverableThreshold_Type = Integer32
_HpnsaEnvVoltageSensorLowerNonRecoverableThreshold_Object = MibTableColumn
hpnsaEnvVoltageSensorLowerNonRecoverableThreshold = _HpnsaEnvVoltageSensorLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 16),
    _HpnsaEnvVoltageSensorLowerNonRecoverableThreshold_Type()
)
hpnsaEnvVoltageSensorLowerNonRecoverableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorLowerNonRecoverableThreshold.setStatus("mandatory")
_HpnsaEnvVoltageSensorUpperNonRecoverableThreshold_Type = Integer32
_HpnsaEnvVoltageSensorUpperNonRecoverableThreshold_Object = MibTableColumn
hpnsaEnvVoltageSensorUpperNonRecoverableThreshold = _HpnsaEnvVoltageSensorUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 17),
    _HpnsaEnvVoltageSensorUpperNonRecoverableThreshold_Type()
)
hpnsaEnvVoltageSensorUpperNonRecoverableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorUpperNonRecoverableThreshold.setStatus("mandatory")
_HpnsaEnvVoltageSensorResolution_Type = Integer32
_HpnsaEnvVoltageSensorResolution_Object = MibTableColumn
hpnsaEnvVoltageSensorResolution = _HpnsaEnvVoltageSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 18),
    _HpnsaEnvVoltageSensorResolution_Type()
)
hpnsaEnvVoltageSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorResolution.setStatus("mandatory")
_HpnsaEnvVoltageSensorTolerance_Type = Integer32
_HpnsaEnvVoltageSensorTolerance_Object = MibTableColumn
hpnsaEnvVoltageSensorTolerance = _HpnsaEnvVoltageSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 19),
    _HpnsaEnvVoltageSensorTolerance_Type()
)
hpnsaEnvVoltageSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorTolerance.setStatus("mandatory")
_HpnsaEnvVoltageSensorAccuracy_Type = Integer32
_HpnsaEnvVoltageSensorAccuracy_Object = MibTableColumn
hpnsaEnvVoltageSensorAccuracy = _HpnsaEnvVoltageSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 20),
    _HpnsaEnvVoltageSensorAccuracy_Type()
)
hpnsaEnvVoltageSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorAccuracy.setStatus("mandatory")
_HpnsaEnvVoltageSensorPositiveHysterisis_Type = Integer32
_HpnsaEnvVoltageSensorPositiveHysterisis_Object = MibTableColumn
hpnsaEnvVoltageSensorPositiveHysterisis = _HpnsaEnvVoltageSensorPositiveHysterisis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 21),
    _HpnsaEnvVoltageSensorPositiveHysterisis_Type()
)
hpnsaEnvVoltageSensorPositiveHysterisis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorPositiveHysterisis.setStatus("mandatory")
_HpnsaEnvVoltageSensorNegativeHysterisis_Type = Integer32
_HpnsaEnvVoltageSensorNegativeHysterisis_Object = MibTableColumn
hpnsaEnvVoltageSensorNegativeHysterisis = _HpnsaEnvVoltageSensorNegativeHysterisis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 2, 1, 1, 22),
    _HpnsaEnvVoltageSensorNegativeHysterisis_Type()
)
hpnsaEnvVoltageSensorNegativeHysterisis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvVoltageSensorNegativeHysterisis.setStatus("mandatory")
_HpnsaEnvTemperatureData_ObjectIdentity = ObjectIdentity
hpnsaEnvTemperatureData = _HpnsaEnvTemperatureData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3)
)
_HpnsaEnvTemperatureSensorTable_Object = MibTable
hpnsaEnvTemperatureSensorTable = _HpnsaEnvTemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1)
)
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorTable.setStatus("mandatory")
_HpnsaEnvTemperatureSensorEntry_Object = MibTableRow
hpnsaEnvTemperatureSensorEntry = _HpnsaEnvTemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1)
)
hpnsaEnvTemperatureSensorEntry.setIndexNames(
    (0, "HPNSAENV-MIB", "hpnsaEnvTemperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorEntry.setStatus("mandatory")


class _HpnsaEnvTemperatureSensorIndex_Type(Integer32):
    """Custom type hpnsaEnvTemperatureSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEnvTemperatureSensorIndex_Type.__name__ = "Integer32"
_HpnsaEnvTemperatureSensorIndex_Object = MibTableColumn
hpnsaEnvTemperatureSensorIndex = _HpnsaEnvTemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 1),
    _HpnsaEnvTemperatureSensorIndex_Type()
)
hpnsaEnvTemperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorIndex.setStatus("mandatory")


class _HpnsaEnvTemperatureSensorType_Type(Integer32):
    """Custom type hpnsaEnvTemperatureSensorType based on Integer32"""
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
        *(("analog", 3),
          ("digital", 4),
          ("four-state-discrete", 6),
          ("other", 1),
          ("three-state-discrete", 5),
          ("unknown", 2))
    )


_HpnsaEnvTemperatureSensorType_Type.__name__ = "Integer32"
_HpnsaEnvTemperatureSensorType_Object = MibTableColumn
hpnsaEnvTemperatureSensorType = _HpnsaEnvTemperatureSensorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 2),
    _HpnsaEnvTemperatureSensorType_Type()
)
hpnsaEnvTemperatureSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorType.setStatus("mandatory")


class _HpnsaEnvTemperatureSensorLocation_Type(Integer32):
    """Custom type hpnsaEnvTemperatureSensorLocation based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("add-in-card", 11),
          ("disk", 4),
          ("memory-module", 8),
          ("motherboard", 7),
          ("other", 1),
          ("peripheral-bay", 5),
          ("power-unit", 10),
          ("processor", 3),
          ("processor-module", 9),
          ("system-management-module", 6),
          ("unknown", 2))
    )


_HpnsaEnvTemperatureSensorLocation_Type.__name__ = "Integer32"
_HpnsaEnvTemperatureSensorLocation_Object = MibTableColumn
hpnsaEnvTemperatureSensorLocation = _HpnsaEnvTemperatureSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 3),
    _HpnsaEnvTemperatureSensorLocation_Type()
)
hpnsaEnvTemperatureSensorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorLocation.setStatus("mandatory")


class _HpnsaEnvTemperatureSensorDescription_Type(Integer32):
    """Custom type hpnsaEnvTemperatureSensorDescription based on Integer32"""
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
        *(("temperature-sensor-disk-backplane", 12),
          ("temperature-sensor-other", 1),
          ("temperature-sensor-processor-1", 3),
          ("temperature-sensor-processor-2", 4),
          ("temperature-sensor-processor-3", 5),
          ("temperature-sensor-processor-4", 6),
          ("temperature-sensor-processor-5", 7),
          ("temperature-sensor-processor-6", 8),
          ("temperature-sensor-processor-7", 9),
          ("temperature-sensor-processor-8", 10),
          ("temperature-sensor-system-board", 11),
          ("temperature-sensor-unknown", 2))
    )


_HpnsaEnvTemperatureSensorDescription_Type.__name__ = "Integer32"
_HpnsaEnvTemperatureSensorDescription_Object = MibTableColumn
hpnsaEnvTemperatureSensorDescription = _HpnsaEnvTemperatureSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 4),
    _HpnsaEnvTemperatureSensorDescription_Type()
)
hpnsaEnvTemperatureSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorDescription.setStatus("mandatory")


class _HpnsaEnvTemperatureSensorStatus_Type(Integer32):
    """Custom type hpnsaEnvTemperatureSensorStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-critical", 4),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_HpnsaEnvTemperatureSensorStatus_Type.__name__ = "Integer32"
_HpnsaEnvTemperatureSensorStatus_Object = MibTableColumn
hpnsaEnvTemperatureSensorStatus = _HpnsaEnvTemperatureSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 5),
    _HpnsaEnvTemperatureSensorStatus_Type()
)
hpnsaEnvTemperatureSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorStatus.setStatus("mandatory")
_HpnsaEnvTemperatureSensorReading_Type = Integer32
_HpnsaEnvTemperatureSensorReading_Object = MibTableColumn
hpnsaEnvTemperatureSensorReading = _HpnsaEnvTemperatureSensorReading_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 6),
    _HpnsaEnvTemperatureSensorReading_Type()
)
hpnsaEnvTemperatureSensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorReading.setStatus("mandatory")
_HpnsaEnvTemperatureSensorNominalReading_Type = Integer32
_HpnsaEnvTemperatureSensorNominalReading_Object = MibTableColumn
hpnsaEnvTemperatureSensorNominalReading = _HpnsaEnvTemperatureSensorNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 7),
    _HpnsaEnvTemperatureSensorNominalReading_Type()
)
hpnsaEnvTemperatureSensorNominalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorNominalReading.setStatus("mandatory")
_HpnsaEnvTemperatureSensorNormalMaximum_Type = Integer32
_HpnsaEnvTemperatureSensorNormalMaximum_Object = MibTableColumn
hpnsaEnvTemperatureSensorNormalMaximum = _HpnsaEnvTemperatureSensorNormalMaximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 8),
    _HpnsaEnvTemperatureSensorNormalMaximum_Type()
)
hpnsaEnvTemperatureSensorNormalMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorNormalMaximum.setStatus("mandatory")
_HpnsaEnvTemperatureSensorNormalMinimum_Type = Integer32
_HpnsaEnvTemperatureSensorNormalMinimum_Object = MibTableColumn
hpnsaEnvTemperatureSensorNormalMinimum = _HpnsaEnvTemperatureSensorNormalMinimum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 9),
    _HpnsaEnvTemperatureSensorNormalMinimum_Type()
)
hpnsaEnvTemperatureSensorNormalMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorNormalMinimum.setStatus("mandatory")
_HpnsaEnvTemperatureSensorMaximum_Type = Integer32
_HpnsaEnvTemperatureSensorMaximum_Object = MibTableColumn
hpnsaEnvTemperatureSensorMaximum = _HpnsaEnvTemperatureSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 10),
    _HpnsaEnvTemperatureSensorMaximum_Type()
)
hpnsaEnvTemperatureSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorMaximum.setStatus("mandatory")
_HpnsaEnvTemperatureSensorMinimum_Type = Integer32
_HpnsaEnvTemperatureSensorMinimum_Object = MibTableColumn
hpnsaEnvTemperatureSensorMinimum = _HpnsaEnvTemperatureSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 11),
    _HpnsaEnvTemperatureSensorMinimum_Type()
)
hpnsaEnvTemperatureSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorMinimum.setStatus("mandatory")
_HpnsaEnvTemperatureSensorLowerNonCriticalThreshold_Type = Integer32
_HpnsaEnvTemperatureSensorLowerNonCriticalThreshold_Object = MibTableColumn
hpnsaEnvTemperatureSensorLowerNonCriticalThreshold = _HpnsaEnvTemperatureSensorLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 12),
    _HpnsaEnvTemperatureSensorLowerNonCriticalThreshold_Type()
)
hpnsaEnvTemperatureSensorLowerNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorLowerNonCriticalThreshold.setStatus("mandatory")
_HpnsaEnvTemperatureSensorUpperNonCriticalThreshold_Type = Integer32
_HpnsaEnvTemperatureSensorUpperNonCriticalThreshold_Object = MibTableColumn
hpnsaEnvTemperatureSensorUpperNonCriticalThreshold = _HpnsaEnvTemperatureSensorUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 13),
    _HpnsaEnvTemperatureSensorUpperNonCriticalThreshold_Type()
)
hpnsaEnvTemperatureSensorUpperNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorUpperNonCriticalThreshold.setStatus("mandatory")
_HpnsaEnvTemperatureSensorLowerCriticalThreshold_Type = Integer32
_HpnsaEnvTemperatureSensorLowerCriticalThreshold_Object = MibTableColumn
hpnsaEnvTemperatureSensorLowerCriticalThreshold = _HpnsaEnvTemperatureSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 14),
    _HpnsaEnvTemperatureSensorLowerCriticalThreshold_Type()
)
hpnsaEnvTemperatureSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorLowerCriticalThreshold.setStatus("mandatory")
_HpnsaEnvTemperatureSensorUpperCriticalThreshold_Type = Integer32
_HpnsaEnvTemperatureSensorUpperCriticalThreshold_Object = MibTableColumn
hpnsaEnvTemperatureSensorUpperCriticalThreshold = _HpnsaEnvTemperatureSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 15),
    _HpnsaEnvTemperatureSensorUpperCriticalThreshold_Type()
)
hpnsaEnvTemperatureSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorUpperCriticalThreshold.setStatus("mandatory")
_HpnsaEnvTemperatureSensorLowerNonRecoverableThreshold_Type = Integer32
_HpnsaEnvTemperatureSensorLowerNonRecoverableThreshold_Object = MibTableColumn
hpnsaEnvTemperatureSensorLowerNonRecoverableThreshold = _HpnsaEnvTemperatureSensorLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 16),
    _HpnsaEnvTemperatureSensorLowerNonRecoverableThreshold_Type()
)
hpnsaEnvTemperatureSensorLowerNonRecoverableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorLowerNonRecoverableThreshold.setStatus("mandatory")
_HpnsaEnvTemperatureSensorUpperNonRecoverableThreshold_Type = Integer32
_HpnsaEnvTemperatureSensorUpperNonRecoverableThreshold_Object = MibTableColumn
hpnsaEnvTemperatureSensorUpperNonRecoverableThreshold = _HpnsaEnvTemperatureSensorUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 17),
    _HpnsaEnvTemperatureSensorUpperNonRecoverableThreshold_Type()
)
hpnsaEnvTemperatureSensorUpperNonRecoverableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorUpperNonRecoverableThreshold.setStatus("mandatory")
_HpnsaEnvTemperatureSensorResolution_Type = Integer32
_HpnsaEnvTemperatureSensorResolution_Object = MibTableColumn
hpnsaEnvTemperatureSensorResolution = _HpnsaEnvTemperatureSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 18),
    _HpnsaEnvTemperatureSensorResolution_Type()
)
hpnsaEnvTemperatureSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorResolution.setStatus("mandatory")
_HpnsaEnvTemperatureSensorTolerance_Type = Integer32
_HpnsaEnvTemperatureSensorTolerance_Object = MibTableColumn
hpnsaEnvTemperatureSensorTolerance = _HpnsaEnvTemperatureSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 19),
    _HpnsaEnvTemperatureSensorTolerance_Type()
)
hpnsaEnvTemperatureSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorTolerance.setStatus("mandatory")
_HpnsaEnvTemperatureSensorAccuracy_Type = Integer32
_HpnsaEnvTemperatureSensorAccuracy_Object = MibTableColumn
hpnsaEnvTemperatureSensorAccuracy = _HpnsaEnvTemperatureSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 20),
    _HpnsaEnvTemperatureSensorAccuracy_Type()
)
hpnsaEnvTemperatureSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorAccuracy.setStatus("mandatory")
_HpnsaEnvTemperatureSensorPositiveHysterisis_Type = Integer32
_HpnsaEnvTemperatureSensorPositiveHysterisis_Object = MibTableColumn
hpnsaEnvTemperatureSensorPositiveHysterisis = _HpnsaEnvTemperatureSensorPositiveHysterisis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 21),
    _HpnsaEnvTemperatureSensorPositiveHysterisis_Type()
)
hpnsaEnvTemperatureSensorPositiveHysterisis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorPositiveHysterisis.setStatus("mandatory")
_HpnsaEnvTemperatureSensorNegativeHysterisis_Type = Integer32
_HpnsaEnvTemperatureSensorNegativeHysterisis_Object = MibTableColumn
hpnsaEnvTemperatureSensorNegativeHysterisis = _HpnsaEnvTemperatureSensorNegativeHysterisis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 3, 1, 1, 22),
    _HpnsaEnvTemperatureSensorNegativeHysterisis_Type()
)
hpnsaEnvTemperatureSensorNegativeHysterisis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvTemperatureSensorNegativeHysterisis.setStatus("mandatory")
_HpnsaEnvFanSensorData_ObjectIdentity = ObjectIdentity
hpnsaEnvFanSensorData = _HpnsaEnvFanSensorData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4)
)
_HpnsaEnvFanSensorTable_Object = MibTable
hpnsaEnvFanSensorTable = _HpnsaEnvFanSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1)
)
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorTable.setStatus("mandatory")
_HpnsaEnvFanSensorEntry_Object = MibTableRow
hpnsaEnvFanSensorEntry = _HpnsaEnvFanSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1)
)
hpnsaEnvFanSensorEntry.setIndexNames(
    (0, "HPNSAENV-MIB", "hpnsaEnvFanSensorIndex"),
)
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorEntry.setStatus("mandatory")


class _HpnsaEnvFanSensorIndex_Type(Integer32):
    """Custom type hpnsaEnvFanSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaEnvFanSensorIndex_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorIndex_Object = MibTableColumn
hpnsaEnvFanSensorIndex = _HpnsaEnvFanSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 1),
    _HpnsaEnvFanSensorIndex_Type()
)
hpnsaEnvFanSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorIndex.setStatus("mandatory")


class _HpnsaEnvFanSensorType_Type(Integer32):
    """Custom type hpnsaEnvFanSensorType based on Integer32"""
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
        *(("analog", 3),
          ("digital", 4),
          ("four-state-discrete", 6),
          ("other", 1),
          ("three-state-discrete", 5),
          ("unknown", 2))
    )


_HpnsaEnvFanSensorType_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorType_Object = MibTableColumn
hpnsaEnvFanSensorType = _HpnsaEnvFanSensorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 2),
    _HpnsaEnvFanSensorType_Type()
)
hpnsaEnvFanSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorType.setStatus("mandatory")


class _HpnsaEnvFanSensorLocation_Type(Integer32):
    """Custom type hpnsaEnvFanSensorLocation based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("add-in-card", 11),
          ("disk", 4),
          ("memory-module", 8),
          ("motherboard", 7),
          ("other", 1),
          ("peripheral-bay", 5),
          ("power-unit", 10),
          ("processor", 3),
          ("processor-module", 9),
          ("system-management-module", 6),
          ("unknown", 2))
    )


_HpnsaEnvFanSensorLocation_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorLocation_Object = MibTableColumn
hpnsaEnvFanSensorLocation = _HpnsaEnvFanSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 3),
    _HpnsaEnvFanSensorLocation_Type()
)
hpnsaEnvFanSensorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorLocation.setStatus("mandatory")


class _HpnsaEnvFanSensorDescription_Type(Integer32):
    """Custom type hpnsaEnvFanSensorDescription based on Integer32"""
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
        *(("fan-sensor-chassis", 4),
          ("fan-sensor-cpu-board", 3),
          ("fan-sensor-other", 1),
          ("fan-sensor-unknown", 2))
    )


_HpnsaEnvFanSensorDescription_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorDescription_Object = MibTableColumn
hpnsaEnvFanSensorDescription = _HpnsaEnvFanSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 4),
    _HpnsaEnvFanSensorDescription_Type()
)
hpnsaEnvFanSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorDescription.setStatus("mandatory")


class _HpnsaEnvFanSensorStatus_Type(Integer32):
    """Custom type hpnsaEnvFanSensorStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-critical", 4),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_HpnsaEnvFanSensorStatus_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorStatus_Object = MibTableColumn
hpnsaEnvFanSensorStatus = _HpnsaEnvFanSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 5),
    _HpnsaEnvFanSensorStatus_Type()
)
hpnsaEnvFanSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorStatus.setStatus("mandatory")


class _HpnsaEnvFanSensorReading_Type(Integer32):
    """Custom type hpnsaEnvFanSensorReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorReading_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorReading_Object = MibTableColumn
hpnsaEnvFanSensorReading = _HpnsaEnvFanSensorReading_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 6),
    _HpnsaEnvFanSensorReading_Type()
)
hpnsaEnvFanSensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorReading.setStatus("mandatory")


class _HpnsaEnvFanSensorNominalReading_Type(Integer32):
    """Custom type hpnsaEnvFanSensorNominalReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorNominalReading_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorNominalReading_Object = MibTableColumn
hpnsaEnvFanSensorNominalReading = _HpnsaEnvFanSensorNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 7),
    _HpnsaEnvFanSensorNominalReading_Type()
)
hpnsaEnvFanSensorNominalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorNominalReading.setStatus("mandatory")


class _HpnsaEnvFanSensorNormalMaximum_Type(Integer32):
    """Custom type hpnsaEnvFanSensorNormalMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorNormalMaximum_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorNormalMaximum_Object = MibTableColumn
hpnsaEnvFanSensorNormalMaximum = _HpnsaEnvFanSensorNormalMaximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 8),
    _HpnsaEnvFanSensorNormalMaximum_Type()
)
hpnsaEnvFanSensorNormalMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorNormalMaximum.setStatus("mandatory")


class _HpnsaEnvFanSensorNormalMinimum_Type(Integer32):
    """Custom type hpnsaEnvFanSensorNormalMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorNormalMinimum_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorNormalMinimum_Object = MibTableColumn
hpnsaEnvFanSensorNormalMinimum = _HpnsaEnvFanSensorNormalMinimum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 9),
    _HpnsaEnvFanSensorNormalMinimum_Type()
)
hpnsaEnvFanSensorNormalMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorNormalMinimum.setStatus("mandatory")


class _HpnsaEnvFanSensorMaximum_Type(Integer32):
    """Custom type hpnsaEnvFanSensorMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorMaximum_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorMaximum_Object = MibTableColumn
hpnsaEnvFanSensorMaximum = _HpnsaEnvFanSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 10),
    _HpnsaEnvFanSensorMaximum_Type()
)
hpnsaEnvFanSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorMaximum.setStatus("mandatory")


class _HpnsaEnvFanSensorMinimum_Type(Integer32):
    """Custom type hpnsaEnvFanSensorMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorMinimum_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorMinimum_Object = MibTableColumn
hpnsaEnvFanSensorMinimum = _HpnsaEnvFanSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 11),
    _HpnsaEnvFanSensorMinimum_Type()
)
hpnsaEnvFanSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorMinimum.setStatus("mandatory")


class _HpnsaEnvFanSensorLowerNonCriticalThreshold_Type(Integer32):
    """Custom type hpnsaEnvFanSensorLowerNonCriticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorLowerNonCriticalThreshold_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorLowerNonCriticalThreshold_Object = MibTableColumn
hpnsaEnvFanSensorLowerNonCriticalThreshold = _HpnsaEnvFanSensorLowerNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 12),
    _HpnsaEnvFanSensorLowerNonCriticalThreshold_Type()
)
hpnsaEnvFanSensorLowerNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorLowerNonCriticalThreshold.setStatus("mandatory")


class _HpnsaEnvFanSensorUpperNonCriticalThreshold_Type(Integer32):
    """Custom type hpnsaEnvFanSensorUpperNonCriticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorUpperNonCriticalThreshold_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorUpperNonCriticalThreshold_Object = MibTableColumn
hpnsaEnvFanSensorUpperNonCriticalThreshold = _HpnsaEnvFanSensorUpperNonCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 13),
    _HpnsaEnvFanSensorUpperNonCriticalThreshold_Type()
)
hpnsaEnvFanSensorUpperNonCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorUpperNonCriticalThreshold.setStatus("mandatory")


class _HpnsaEnvFanSensorLowerCriticalThreshold_Type(Integer32):
    """Custom type hpnsaEnvFanSensorLowerCriticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorLowerCriticalThreshold_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorLowerCriticalThreshold_Object = MibTableColumn
hpnsaEnvFanSensorLowerCriticalThreshold = _HpnsaEnvFanSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 14),
    _HpnsaEnvFanSensorLowerCriticalThreshold_Type()
)
hpnsaEnvFanSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorLowerCriticalThreshold.setStatus("mandatory")


class _HpnsaEnvFanSensorUpperCriticalThreshold_Type(Integer32):
    """Custom type hpnsaEnvFanSensorUpperCriticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorUpperCriticalThreshold_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorUpperCriticalThreshold_Object = MibTableColumn
hpnsaEnvFanSensorUpperCriticalThreshold = _HpnsaEnvFanSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 15),
    _HpnsaEnvFanSensorUpperCriticalThreshold_Type()
)
hpnsaEnvFanSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorUpperCriticalThreshold.setStatus("mandatory")


class _HpnsaEnvFanSensorLowerNonRecoverableThreshold_Type(Integer32):
    """Custom type hpnsaEnvFanSensorLowerNonRecoverableThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorLowerNonRecoverableThreshold_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorLowerNonRecoverableThreshold_Object = MibTableColumn
hpnsaEnvFanSensorLowerNonRecoverableThreshold = _HpnsaEnvFanSensorLowerNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 16),
    _HpnsaEnvFanSensorLowerNonRecoverableThreshold_Type()
)
hpnsaEnvFanSensorLowerNonRecoverableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorLowerNonRecoverableThreshold.setStatus("mandatory")


class _HpnsaEnvFanSensorUpperNonRecoverableThreshold_Type(Integer32):
    """Custom type hpnsaEnvFanSensorUpperNonRecoverableThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorUpperNonRecoverableThreshold_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorUpperNonRecoverableThreshold_Object = MibTableColumn
hpnsaEnvFanSensorUpperNonRecoverableThreshold = _HpnsaEnvFanSensorUpperNonRecoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 17),
    _HpnsaEnvFanSensorUpperNonRecoverableThreshold_Type()
)
hpnsaEnvFanSensorUpperNonRecoverableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorUpperNonRecoverableThreshold.setStatus("mandatory")


class _HpnsaEnvFanSensorResolution_Type(Integer32):
    """Custom type hpnsaEnvFanSensorResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorResolution_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorResolution_Object = MibTableColumn
hpnsaEnvFanSensorResolution = _HpnsaEnvFanSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 18),
    _HpnsaEnvFanSensorResolution_Type()
)
hpnsaEnvFanSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorResolution.setStatus("mandatory")


class _HpnsaEnvFanSensorTolerance_Type(Integer32):
    """Custom type hpnsaEnvFanSensorTolerance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorTolerance_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorTolerance_Object = MibTableColumn
hpnsaEnvFanSensorTolerance = _HpnsaEnvFanSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 19),
    _HpnsaEnvFanSensorTolerance_Type()
)
hpnsaEnvFanSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorTolerance.setStatus("mandatory")


class _HpnsaEnvFanSensorAccuracy_Type(Integer32):
    """Custom type hpnsaEnvFanSensorAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorAccuracy_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorAccuracy_Object = MibTableColumn
hpnsaEnvFanSensorAccuracy = _HpnsaEnvFanSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 20),
    _HpnsaEnvFanSensorAccuracy_Type()
)
hpnsaEnvFanSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorAccuracy.setStatus("mandatory")


class _HpnsaEnvFanSensorPositiveHysterisis_Type(Integer32):
    """Custom type hpnsaEnvFanSensorPositiveHysterisis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorPositiveHysterisis_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorPositiveHysterisis_Object = MibTableColumn
hpnsaEnvFanSensorPositiveHysterisis = _HpnsaEnvFanSensorPositiveHysterisis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 21),
    _HpnsaEnvFanSensorPositiveHysterisis_Type()
)
hpnsaEnvFanSensorPositiveHysterisis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorPositiveHysterisis.setStatus("mandatory")


class _HpnsaEnvFanSensorNegativeHysterisis_Type(Integer32):
    """Custom type hpnsaEnvFanSensorNegativeHysterisis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaEnvFanSensorNegativeHysterisis_Type.__name__ = "Integer32"
_HpnsaEnvFanSensorNegativeHysterisis_Object = MibTableColumn
hpnsaEnvFanSensorNegativeHysterisis = _HpnsaEnvFanSensorNegativeHysterisis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 4, 1, 1, 22),
    _HpnsaEnvFanSensorNegativeHysterisis_Type()
)
hpnsaEnvFanSensorNegativeHysterisis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaEnvFanSensorNegativeHysterisis.setStatus("mandatory")
_HpnsaEnvChassisData_ObjectIdentity = ObjectIdentity
hpnsaEnvChassisData = _HpnsaEnvChassisData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 5)
)


class _HpnsaEnvChassisStatus_Type(Integer32):
    """Custom type hpnsaEnvChassisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chassis-closed", 2),
          ("chassis-open", 1))
    )


_HpnsaEnvChassisStatus_Type.__name__ = "Integer32"
_HpnsaEnvChassisStatus_Object = MibScalar
hpnsaEnvChassisStatus = _HpnsaEnvChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 26, 5, 1),
    _HpnsaEnvChassisStatus_Type()
)
hpnsaEnvChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaEnvChassisStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSAENV-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaEnvironment": hpnsaEnvironment,
       "hpnsaEnvMibRev": hpnsaEnvMibRev,
       "hpnsaEnvMibRevMajor": hpnsaEnvMibRevMajor,
       "hpnsaEnvMibRevMinor": hpnsaEnvMibRevMinor,
       "hpnsaEnvVoltageData": hpnsaEnvVoltageData,
       "hpnsaEnvVoltageSensorTable": hpnsaEnvVoltageSensorTable,
       "hpnsaEnvVoltageSensorEntry": hpnsaEnvVoltageSensorEntry,
       "hpnsaEnvVoltageSensorIndex": hpnsaEnvVoltageSensorIndex,
       "hpnsaEnvVoltageSensorType": hpnsaEnvVoltageSensorType,
       "hpnsaEnvVoltageSensorLocation": hpnsaEnvVoltageSensorLocation,
       "hpnsaEnvVoltageSensorDescription": hpnsaEnvVoltageSensorDescription,
       "hpnsaEnvVoltageSensorStatus": hpnsaEnvVoltageSensorStatus,
       "hpnsaEnvVoltageSensorLevel": hpnsaEnvVoltageSensorLevel,
       "hpnsaEnvVoltageSensorNominalLevel": hpnsaEnvVoltageSensorNominalLevel,
       "hpnsaEnvVoltageSensorNormalMaximum": hpnsaEnvVoltageSensorNormalMaximum,
       "hpnsaEnvVoltageSensorNormalMinimum": hpnsaEnvVoltageSensorNormalMinimum,
       "hpnsaEnvVoltageSensorMaximum": hpnsaEnvVoltageSensorMaximum,
       "hpnsaEnvVoltageSensorMinimum": hpnsaEnvVoltageSensorMinimum,
       "hpnsaEnvVoltageSensorLowerNonCriticalThreshold": hpnsaEnvVoltageSensorLowerNonCriticalThreshold,
       "hpnsaEnvVoltageSensorUpperNonCriticalThreshold": hpnsaEnvVoltageSensorUpperNonCriticalThreshold,
       "hpnsaEnvVoltageSensorLowerCriticalThreshold": hpnsaEnvVoltageSensorLowerCriticalThreshold,
       "hpnsaEnvVoltageSensorUpperCriticalThreshold": hpnsaEnvVoltageSensorUpperCriticalThreshold,
       "hpnsaEnvVoltageSensorLowerNonRecoverableThreshold": hpnsaEnvVoltageSensorLowerNonRecoverableThreshold,
       "hpnsaEnvVoltageSensorUpperNonRecoverableThreshold": hpnsaEnvVoltageSensorUpperNonRecoverableThreshold,
       "hpnsaEnvVoltageSensorResolution": hpnsaEnvVoltageSensorResolution,
       "hpnsaEnvVoltageSensorTolerance": hpnsaEnvVoltageSensorTolerance,
       "hpnsaEnvVoltageSensorAccuracy": hpnsaEnvVoltageSensorAccuracy,
       "hpnsaEnvVoltageSensorPositiveHysterisis": hpnsaEnvVoltageSensorPositiveHysterisis,
       "hpnsaEnvVoltageSensorNegativeHysterisis": hpnsaEnvVoltageSensorNegativeHysterisis,
       "hpnsaEnvTemperatureData": hpnsaEnvTemperatureData,
       "hpnsaEnvTemperatureSensorTable": hpnsaEnvTemperatureSensorTable,
       "hpnsaEnvTemperatureSensorEntry": hpnsaEnvTemperatureSensorEntry,
       "hpnsaEnvTemperatureSensorIndex": hpnsaEnvTemperatureSensorIndex,
       "hpnsaEnvTemperatureSensorType": hpnsaEnvTemperatureSensorType,
       "hpnsaEnvTemperatureSensorLocation": hpnsaEnvTemperatureSensorLocation,
       "hpnsaEnvTemperatureSensorDescription": hpnsaEnvTemperatureSensorDescription,
       "hpnsaEnvTemperatureSensorStatus": hpnsaEnvTemperatureSensorStatus,
       "hpnsaEnvTemperatureSensorReading": hpnsaEnvTemperatureSensorReading,
       "hpnsaEnvTemperatureSensorNominalReading": hpnsaEnvTemperatureSensorNominalReading,
       "hpnsaEnvTemperatureSensorNormalMaximum": hpnsaEnvTemperatureSensorNormalMaximum,
       "hpnsaEnvTemperatureSensorNormalMinimum": hpnsaEnvTemperatureSensorNormalMinimum,
       "hpnsaEnvTemperatureSensorMaximum": hpnsaEnvTemperatureSensorMaximum,
       "hpnsaEnvTemperatureSensorMinimum": hpnsaEnvTemperatureSensorMinimum,
       "hpnsaEnvTemperatureSensorLowerNonCriticalThreshold": hpnsaEnvTemperatureSensorLowerNonCriticalThreshold,
       "hpnsaEnvTemperatureSensorUpperNonCriticalThreshold": hpnsaEnvTemperatureSensorUpperNonCriticalThreshold,
       "hpnsaEnvTemperatureSensorLowerCriticalThreshold": hpnsaEnvTemperatureSensorLowerCriticalThreshold,
       "hpnsaEnvTemperatureSensorUpperCriticalThreshold": hpnsaEnvTemperatureSensorUpperCriticalThreshold,
       "hpnsaEnvTemperatureSensorLowerNonRecoverableThreshold": hpnsaEnvTemperatureSensorLowerNonRecoverableThreshold,
       "hpnsaEnvTemperatureSensorUpperNonRecoverableThreshold": hpnsaEnvTemperatureSensorUpperNonRecoverableThreshold,
       "hpnsaEnvTemperatureSensorResolution": hpnsaEnvTemperatureSensorResolution,
       "hpnsaEnvTemperatureSensorTolerance": hpnsaEnvTemperatureSensorTolerance,
       "hpnsaEnvTemperatureSensorAccuracy": hpnsaEnvTemperatureSensorAccuracy,
       "hpnsaEnvTemperatureSensorPositiveHysterisis": hpnsaEnvTemperatureSensorPositiveHysterisis,
       "hpnsaEnvTemperatureSensorNegativeHysterisis": hpnsaEnvTemperatureSensorNegativeHysterisis,
       "hpnsaEnvFanSensorData": hpnsaEnvFanSensorData,
       "hpnsaEnvFanSensorTable": hpnsaEnvFanSensorTable,
       "hpnsaEnvFanSensorEntry": hpnsaEnvFanSensorEntry,
       "hpnsaEnvFanSensorIndex": hpnsaEnvFanSensorIndex,
       "hpnsaEnvFanSensorType": hpnsaEnvFanSensorType,
       "hpnsaEnvFanSensorLocation": hpnsaEnvFanSensorLocation,
       "hpnsaEnvFanSensorDescription": hpnsaEnvFanSensorDescription,
       "hpnsaEnvFanSensorStatus": hpnsaEnvFanSensorStatus,
       "hpnsaEnvFanSensorReading": hpnsaEnvFanSensorReading,
       "hpnsaEnvFanSensorNominalReading": hpnsaEnvFanSensorNominalReading,
       "hpnsaEnvFanSensorNormalMaximum": hpnsaEnvFanSensorNormalMaximum,
       "hpnsaEnvFanSensorNormalMinimum": hpnsaEnvFanSensorNormalMinimum,
       "hpnsaEnvFanSensorMaximum": hpnsaEnvFanSensorMaximum,
       "hpnsaEnvFanSensorMinimum": hpnsaEnvFanSensorMinimum,
       "hpnsaEnvFanSensorLowerNonCriticalThreshold": hpnsaEnvFanSensorLowerNonCriticalThreshold,
       "hpnsaEnvFanSensorUpperNonCriticalThreshold": hpnsaEnvFanSensorUpperNonCriticalThreshold,
       "hpnsaEnvFanSensorLowerCriticalThreshold": hpnsaEnvFanSensorLowerCriticalThreshold,
       "hpnsaEnvFanSensorUpperCriticalThreshold": hpnsaEnvFanSensorUpperCriticalThreshold,
       "hpnsaEnvFanSensorLowerNonRecoverableThreshold": hpnsaEnvFanSensorLowerNonRecoverableThreshold,
       "hpnsaEnvFanSensorUpperNonRecoverableThreshold": hpnsaEnvFanSensorUpperNonRecoverableThreshold,
       "hpnsaEnvFanSensorResolution": hpnsaEnvFanSensorResolution,
       "hpnsaEnvFanSensorTolerance": hpnsaEnvFanSensorTolerance,
       "hpnsaEnvFanSensorAccuracy": hpnsaEnvFanSensorAccuracy,
       "hpnsaEnvFanSensorPositiveHysterisis": hpnsaEnvFanSensorPositiveHysterisis,
       "hpnsaEnvFanSensorNegativeHysterisis": hpnsaEnvFanSensorNegativeHysterisis,
       "hpnsaEnvChassisData": hpnsaEnvChassisData,
       "hpnsaEnvChassisStatus": hpnsaEnvChassisStatus}
)
