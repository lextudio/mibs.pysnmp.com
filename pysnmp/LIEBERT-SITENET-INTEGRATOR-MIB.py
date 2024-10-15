# SNMP MIB module (LIEBERT-SITENET-INTEGRATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-SITENET-INTEGRATOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:02 2024
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

(TruthValue,) = mibBuilder.importSymbols(
    "RFC1253-MIB",
    "TruthValue")

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

_Emerson_ObjectIdentity = ObjectIdentity
emerson = _Emerson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476)
)
_LiebertCorp_ObjectIdentity = ObjectIdentity
liebertCorp = _LiebertCorp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1)
)
_LiebertUps_ObjectIdentity = ObjectIdentity
liebertUps = _LiebertUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1)
)
_LiebertEnvironment_ObjectIdentity = ObjectIdentity
liebertEnvironment = _LiebertEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2)
)
_LeExtensions_ObjectIdentity = ObjectIdentity
leExtensions = _LeExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1)
)
_LeSiteNet01_ObjectIdentity = ObjectIdentity
leSiteNet01 = _LeSiteNet01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1)
)
_EnvMIB_ObjectIdentity = ObjectIdentity
envMIB = _EnvMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1)
)
_EnvIdent_ObjectIdentity = ObjectIdentity
envIdent = _EnvIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 1)
)
_EnvIdentManufacturer_Type = DisplayString
_EnvIdentManufacturer_Object = MibScalar
envIdentManufacturer = _EnvIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 1, 1),
    _EnvIdentManufacturer_Type()
)
envIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envIdentManufacturer.setStatus("mandatory")
_EnvIdentModel_Type = DisplayString
_EnvIdentModel_Object = MibScalar
envIdentModel = _EnvIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 1, 2),
    _EnvIdentModel_Type()
)
envIdentModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envIdentModel.setStatus("mandatory")
_EnvIdentSoftwareVersion_Type = DisplayString
_EnvIdentSoftwareVersion_Object = MibScalar
envIdentSoftwareVersion = _EnvIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 1, 3),
    _EnvIdentSoftwareVersion_Type()
)
envIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envIdentSoftwareVersion.setStatus("mandatory")
_EnvIdentSpecific_Type = ObjectIdentifier
_EnvIdentSpecific_Object = MibScalar
envIdentSpecific = _EnvIdentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 1, 4),
    _EnvIdentSpecific_Type()
)
envIdentSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envIdentSpecific.setStatus("mandatory")
_EnvDigitalInputs_ObjectIdentity = ObjectIdentity
envDigitalInputs = _EnvDigitalInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2)
)
_EnvDigInput1_ObjectIdentity = ObjectIdentity
envDigInput1 = _EnvDigInput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 1)
)


class _EnvDigInput1State_Type(Integer32):
    """Custom type envDigInput1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notInstalled", 3),
          ("true", 1))
    )


_EnvDigInput1State_Type.__name__ = "Integer32"
_EnvDigInput1State_Object = MibScalar
envDigInput1State = _EnvDigInput1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 1, 1),
    _EnvDigInput1State_Type()
)
envDigInput1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput1State.setStatus("mandatory")
_EnvDigInput1Label_Type = DisplayString
_EnvDigInput1Label_Object = MibScalar
envDigInput1Label = _EnvDigInput1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 1, 2),
    _EnvDigInput1Label_Type()
)
envDigInput1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput1Label.setStatus("mandatory")


class _EnvDigInput1Polarity_Type(Integer32):
    """Custom type envDigInput1Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput1Polarity_Type.__name__ = "Integer32"
_EnvDigInput1Polarity_Object = MibScalar
envDigInput1Polarity = _EnvDigInput1Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 1, 3),
    _EnvDigInput1Polarity_Type()
)
envDigInput1Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput1Polarity.setStatus("mandatory")
_EnvDigInput1TrapEnabled_Type = TruthValue
_EnvDigInput1TrapEnabled_Object = MibScalar
envDigInput1TrapEnabled = _EnvDigInput1TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 1, 4),
    _EnvDigInput1TrapEnabled_Type()
)
envDigInput1TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput1TrapEnabled.setStatus("mandatory")
_EnvDigInput2_ObjectIdentity = ObjectIdentity
envDigInput2 = _EnvDigInput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 2)
)


class _EnvDigInput2State_Type(Integer32):
    """Custom type envDigInput2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notInstalled", 3),
          ("true", 1))
    )


_EnvDigInput2State_Type.__name__ = "Integer32"
_EnvDigInput2State_Object = MibScalar
envDigInput2State = _EnvDigInput2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 2, 1),
    _EnvDigInput2State_Type()
)
envDigInput2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput2State.setStatus("mandatory")
_EnvDigInput2Label_Type = DisplayString
_EnvDigInput2Label_Object = MibScalar
envDigInput2Label = _EnvDigInput2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 2, 2),
    _EnvDigInput2Label_Type()
)
envDigInput2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput2Label.setStatus("mandatory")


class _EnvDigInput2Polarity_Type(Integer32):
    """Custom type envDigInput2Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput2Polarity_Type.__name__ = "Integer32"
_EnvDigInput2Polarity_Object = MibScalar
envDigInput2Polarity = _EnvDigInput2Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 2, 3),
    _EnvDigInput2Polarity_Type()
)
envDigInput2Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput2Polarity.setStatus("mandatory")
_EnvDigInput2TrapEnabled_Type = TruthValue
_EnvDigInput2TrapEnabled_Object = MibScalar
envDigInput2TrapEnabled = _EnvDigInput2TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 2, 4),
    _EnvDigInput2TrapEnabled_Type()
)
envDigInput2TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput2TrapEnabled.setStatus("mandatory")
_EnvDigInput3_ObjectIdentity = ObjectIdentity
envDigInput3 = _EnvDigInput3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 3)
)


class _EnvDigInput3State_Type(Integer32):
    """Custom type envDigInput3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notInstalled", 3),
          ("true", 1))
    )


_EnvDigInput3State_Type.__name__ = "Integer32"
_EnvDigInput3State_Object = MibScalar
envDigInput3State = _EnvDigInput3State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 3, 1),
    _EnvDigInput3State_Type()
)
envDigInput3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput3State.setStatus("mandatory")
_EnvDigInput3Label_Type = DisplayString
_EnvDigInput3Label_Object = MibScalar
envDigInput3Label = _EnvDigInput3Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 3, 2),
    _EnvDigInput3Label_Type()
)
envDigInput3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput3Label.setStatus("mandatory")


class _EnvDigInput3Polarity_Type(Integer32):
    """Custom type envDigInput3Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput3Polarity_Type.__name__ = "Integer32"
_EnvDigInput3Polarity_Object = MibScalar
envDigInput3Polarity = _EnvDigInput3Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 3, 3),
    _EnvDigInput3Polarity_Type()
)
envDigInput3Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput3Polarity.setStatus("mandatory")
_EnvDigInput3TrapEnabled_Type = TruthValue
_EnvDigInput3TrapEnabled_Object = MibScalar
envDigInput3TrapEnabled = _EnvDigInput3TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 3, 4),
    _EnvDigInput3TrapEnabled_Type()
)
envDigInput3TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput3TrapEnabled.setStatus("mandatory")
_EnvDigInput4_ObjectIdentity = ObjectIdentity
envDigInput4 = _EnvDigInput4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 4)
)


class _EnvDigInput4State_Type(Integer32):
    """Custom type envDigInput4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notInstalled", 3),
          ("true", 1))
    )


_EnvDigInput4State_Type.__name__ = "Integer32"
_EnvDigInput4State_Object = MibScalar
envDigInput4State = _EnvDigInput4State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 4, 1),
    _EnvDigInput4State_Type()
)
envDigInput4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput4State.setStatus("mandatory")
_EnvDigInput4Label_Type = DisplayString
_EnvDigInput4Label_Object = MibScalar
envDigInput4Label = _EnvDigInput4Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 4, 2),
    _EnvDigInput4Label_Type()
)
envDigInput4Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput4Label.setStatus("mandatory")


class _EnvDigInput4Polarity_Type(Integer32):
    """Custom type envDigInput4Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput4Polarity_Type.__name__ = "Integer32"
_EnvDigInput4Polarity_Object = MibScalar
envDigInput4Polarity = _EnvDigInput4Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 4, 3),
    _EnvDigInput4Polarity_Type()
)
envDigInput4Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput4Polarity.setStatus("mandatory")
_EnvDigInput4TrapEnabled_Type = TruthValue
_EnvDigInput4TrapEnabled_Object = MibScalar
envDigInput4TrapEnabled = _EnvDigInput4TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 4, 4),
    _EnvDigInput4TrapEnabled_Type()
)
envDigInput4TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput4TrapEnabled.setStatus("mandatory")
_EnvDigInput5_ObjectIdentity = ObjectIdentity
envDigInput5 = _EnvDigInput5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 5)
)


class _EnvDigInput5State_Type(Integer32):
    """Custom type envDigInput5State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notInstalled", 3),
          ("true", 1))
    )


_EnvDigInput5State_Type.__name__ = "Integer32"
_EnvDigInput5State_Object = MibScalar
envDigInput5State = _EnvDigInput5State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 5, 1),
    _EnvDigInput5State_Type()
)
envDigInput5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput5State.setStatus("mandatory")
_EnvDigInput5Label_Type = DisplayString
_EnvDigInput5Label_Object = MibScalar
envDigInput5Label = _EnvDigInput5Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 5, 2),
    _EnvDigInput5Label_Type()
)
envDigInput5Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput5Label.setStatus("mandatory")


class _EnvDigInput5Polarity_Type(Integer32):
    """Custom type envDigInput5Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput5Polarity_Type.__name__ = "Integer32"
_EnvDigInput5Polarity_Object = MibScalar
envDigInput5Polarity = _EnvDigInput5Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 5, 3),
    _EnvDigInput5Polarity_Type()
)
envDigInput5Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput5Polarity.setStatus("mandatory")
_EnvDigInput5TrapEnabled_Type = TruthValue
_EnvDigInput5TrapEnabled_Object = MibScalar
envDigInput5TrapEnabled = _EnvDigInput5TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 5, 4),
    _EnvDigInput5TrapEnabled_Type()
)
envDigInput5TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput5TrapEnabled.setStatus("mandatory")
_EnvDigInput6_ObjectIdentity = ObjectIdentity
envDigInput6 = _EnvDigInput6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 6)
)


class _EnvDigInput6State_Type(Integer32):
    """Custom type envDigInput6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notInstalled", 3),
          ("true", 1))
    )


_EnvDigInput6State_Type.__name__ = "Integer32"
_EnvDigInput6State_Object = MibScalar
envDigInput6State = _EnvDigInput6State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 6, 1),
    _EnvDigInput6State_Type()
)
envDigInput6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput6State.setStatus("mandatory")
_EnvDigInput6Label_Type = DisplayString
_EnvDigInput6Label_Object = MibScalar
envDigInput6Label = _EnvDigInput6Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 6, 2),
    _EnvDigInput6Label_Type()
)
envDigInput6Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput6Label.setStatus("mandatory")


class _EnvDigInput6Polarity_Type(Integer32):
    """Custom type envDigInput6Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput6Polarity_Type.__name__ = "Integer32"
_EnvDigInput6Polarity_Object = MibScalar
envDigInput6Polarity = _EnvDigInput6Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 6, 3),
    _EnvDigInput6Polarity_Type()
)
envDigInput6Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput6Polarity.setStatus("mandatory")
_EnvDigInput6TrapEnabled_Type = TruthValue
_EnvDigInput6TrapEnabled_Object = MibScalar
envDigInput6TrapEnabled = _EnvDigInput6TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 6, 4),
    _EnvDigInput6TrapEnabled_Type()
)
envDigInput6TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput6TrapEnabled.setStatus("mandatory")
_EnvDigInput7_ObjectIdentity = ObjectIdentity
envDigInput7 = _EnvDigInput7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 7)
)


class _EnvDigInput7State_Type(Integer32):
    """Custom type envDigInput7State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notInstalled", 3),
          ("true", 1))
    )


_EnvDigInput7State_Type.__name__ = "Integer32"
_EnvDigInput7State_Object = MibScalar
envDigInput7State = _EnvDigInput7State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 7, 1),
    _EnvDigInput7State_Type()
)
envDigInput7State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput7State.setStatus("mandatory")
_EnvDigInput7Label_Type = DisplayString
_EnvDigInput7Label_Object = MibScalar
envDigInput7Label = _EnvDigInput7Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 7, 2),
    _EnvDigInput7Label_Type()
)
envDigInput7Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput7Label.setStatus("mandatory")


class _EnvDigInput7Polarity_Type(Integer32):
    """Custom type envDigInput7Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput7Polarity_Type.__name__ = "Integer32"
_EnvDigInput7Polarity_Object = MibScalar
envDigInput7Polarity = _EnvDigInput7Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 7, 3),
    _EnvDigInput7Polarity_Type()
)
envDigInput7Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput7Polarity.setStatus("mandatory")
_EnvDigInput7TrapEnabled_Type = TruthValue
_EnvDigInput7TrapEnabled_Object = MibScalar
envDigInput7TrapEnabled = _EnvDigInput7TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 7, 4),
    _EnvDigInput7TrapEnabled_Type()
)
envDigInput7TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput7TrapEnabled.setStatus("mandatory")
_EnvDigInput8_ObjectIdentity = ObjectIdentity
envDigInput8 = _EnvDigInput8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 8)
)


class _EnvDigInput8State_Type(Integer32):
    """Custom type envDigInput8State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notInstalled", 3),
          ("true", 1))
    )


_EnvDigInput8State_Type.__name__ = "Integer32"
_EnvDigInput8State_Object = MibScalar
envDigInput8State = _EnvDigInput8State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 8, 1),
    _EnvDigInput8State_Type()
)
envDigInput8State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput8State.setStatus("mandatory")
_EnvDigInput8Label_Type = DisplayString
_EnvDigInput8Label_Object = MibScalar
envDigInput8Label = _EnvDigInput8Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 8, 2),
    _EnvDigInput8Label_Type()
)
envDigInput8Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput8Label.setStatus("mandatory")


class _EnvDigInput8Polarity_Type(Integer32):
    """Custom type envDigInput8Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput8Polarity_Type.__name__ = "Integer32"
_EnvDigInput8Polarity_Object = MibScalar
envDigInput8Polarity = _EnvDigInput8Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 8, 3),
    _EnvDigInput8Polarity_Type()
)
envDigInput8Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput8Polarity.setStatus("mandatory")
_EnvDigInput8TrapEnabled_Type = TruthValue
_EnvDigInput8TrapEnabled_Object = MibScalar
envDigInput8TrapEnabled = _EnvDigInput8TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 8, 4),
    _EnvDigInput8TrapEnabled_Type()
)
envDigInput8TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput8TrapEnabled.setStatus("mandatory")
_EnvDigInput9_ObjectIdentity = ObjectIdentity
envDigInput9 = _EnvDigInput9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 9)
)


class _EnvDigInput9State_Type(Integer32):
    """Custom type envDigInput9State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notInstalled", 3),
          ("true", 1))
    )


_EnvDigInput9State_Type.__name__ = "Integer32"
_EnvDigInput9State_Object = MibScalar
envDigInput9State = _EnvDigInput9State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 9, 1),
    _EnvDigInput9State_Type()
)
envDigInput9State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput9State.setStatus("mandatory")
_EnvDigInput9Label_Type = DisplayString
_EnvDigInput9Label_Object = MibScalar
envDigInput9Label = _EnvDigInput9Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 9, 2),
    _EnvDigInput9Label_Type()
)
envDigInput9Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput9Label.setStatus("mandatory")


class _EnvDigInput9Polarity_Type(Integer32):
    """Custom type envDigInput9Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput9Polarity_Type.__name__ = "Integer32"
_EnvDigInput9Polarity_Object = MibScalar
envDigInput9Polarity = _EnvDigInput9Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 9, 3),
    _EnvDigInput9Polarity_Type()
)
envDigInput9Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput9Polarity.setStatus("mandatory")
_EnvDigInput9TrapEnabled_Type = TruthValue
_EnvDigInput9TrapEnabled_Object = MibScalar
envDigInput9TrapEnabled = _EnvDigInput9TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 9, 4),
    _EnvDigInput9TrapEnabled_Type()
)
envDigInput9TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput9TrapEnabled.setStatus("mandatory")
_EnvDigInput10_ObjectIdentity = ObjectIdentity
envDigInput10 = _EnvDigInput10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 10)
)


class _EnvDigInput10State_Type(Integer32):
    """Custom type envDigInput10State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notInstalled", 3),
          ("true", 1))
    )


_EnvDigInput10State_Type.__name__ = "Integer32"
_EnvDigInput10State_Object = MibScalar
envDigInput10State = _EnvDigInput10State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 10, 1),
    _EnvDigInput10State_Type()
)
envDigInput10State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput10State.setStatus("mandatory")
_EnvDigInput10Label_Type = DisplayString
_EnvDigInput10Label_Object = MibScalar
envDigInput10Label = _EnvDigInput10Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 10, 2),
    _EnvDigInput10Label_Type()
)
envDigInput10Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput10Label.setStatus("mandatory")


class _EnvDigInput10Polarity_Type(Integer32):
    """Custom type envDigInput10Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput10Polarity_Type.__name__ = "Integer32"
_EnvDigInput10Polarity_Object = MibScalar
envDigInput10Polarity = _EnvDigInput10Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 10, 3),
    _EnvDigInput10Polarity_Type()
)
envDigInput10Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput10Polarity.setStatus("mandatory")
_EnvDigInput10TrapEnabled_Type = TruthValue
_EnvDigInput10TrapEnabled_Object = MibScalar
envDigInput10TrapEnabled = _EnvDigInput10TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 10, 4),
    _EnvDigInput10TrapEnabled_Type()
)
envDigInput10TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput10TrapEnabled.setStatus("mandatory")
_EnvRelays_ObjectIdentity = ObjectIdentity
envRelays = _EnvRelays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3)
)
_EnvRelay1_ObjectIdentity = ObjectIdentity
envRelay1 = _EnvRelay1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 1)
)


class _EnvRelay1State_Type(Integer32):
    """Custom type envRelay1State based on Integer32"""
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


_EnvRelay1State_Type.__name__ = "Integer32"
_EnvRelay1State_Object = MibScalar
envRelay1State = _EnvRelay1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 1, 1),
    _EnvRelay1State_Type()
)
envRelay1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay1State.setStatus("mandatory")
_EnvRelay1Label_Type = DisplayString
_EnvRelay1Label_Object = MibScalar
envRelay1Label = _EnvRelay1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 1, 2),
    _EnvRelay1Label_Type()
)
envRelay1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay1Label.setStatus("mandatory")


class _EnvRelay1Control_Type(Integer32):
    """Custom type envRelay1Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvRelay1Control_Type.__name__ = "Integer32"
_EnvRelay1Control_Object = MibScalar
envRelay1Control = _EnvRelay1Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 1, 3),
    _EnvRelay1Control_Type()
)
envRelay1Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay1Control.setStatus("mandatory")
_EnvRelay2_ObjectIdentity = ObjectIdentity
envRelay2 = _EnvRelay2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 2)
)


class _EnvRelay2State_Type(Integer32):
    """Custom type envRelay2State based on Integer32"""
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


_EnvRelay2State_Type.__name__ = "Integer32"
_EnvRelay2State_Object = MibScalar
envRelay2State = _EnvRelay2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 2, 1),
    _EnvRelay2State_Type()
)
envRelay2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay2State.setStatus("mandatory")
_EnvRelay2Label_Type = DisplayString
_EnvRelay2Label_Object = MibScalar
envRelay2Label = _EnvRelay2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 2, 2),
    _EnvRelay2Label_Type()
)
envRelay2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay2Label.setStatus("mandatory")


class _EnvRelay2Control_Type(Integer32):
    """Custom type envRelay2Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvRelay2Control_Type.__name__ = "Integer32"
_EnvRelay2Control_Object = MibScalar
envRelay2Control = _EnvRelay2Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 2, 3),
    _EnvRelay2Control_Type()
)
envRelay2Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay2Control.setStatus("mandatory")
_EnvOutputs_ObjectIdentity = ObjectIdentity
envOutputs = _EnvOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4)
)
_EnvAudible_ObjectIdentity = ObjectIdentity
envAudible = _EnvAudible_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 1)
)


class _EnvAudibleState_Type(Integer32):
    """Custom type envAudibleState based on Integer32"""
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


_EnvAudibleState_Type.__name__ = "Integer32"
_EnvAudibleState_Object = MibScalar
envAudibleState = _EnvAudibleState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 1, 1),
    _EnvAudibleState_Type()
)
envAudibleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envAudibleState.setStatus("mandatory")


class _EnvAudibleControl_Type(Integer32):
    """Custom type envAudibleControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvAudibleControl_Type.__name__ = "Integer32"
_EnvAudibleControl_Object = MibScalar
envAudibleControl = _EnvAudibleControl_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 1, 2),
    _EnvAudibleControl_Type()
)
envAudibleControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envAudibleControl.setStatus("mandatory")
_EnvLED1_ObjectIdentity = ObjectIdentity
envLED1 = _EnvLED1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 2)
)


class _EnvLED1State_Type(Integer32):
    """Custom type envLED1State based on Integer32"""
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


_EnvLED1State_Type.__name__ = "Integer32"
_EnvLED1State_Object = MibScalar
envLED1State = _EnvLED1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 2, 1),
    _EnvLED1State_Type()
)
envLED1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED1State.setStatus("mandatory")
_EnvLED1Label_Type = DisplayString
_EnvLED1Label_Object = MibScalar
envLED1Label = _EnvLED1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 2, 2),
    _EnvLED1Label_Type()
)
envLED1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED1Label.setStatus("mandatory")


class _EnvLED1Control_Type(Integer32):
    """Custom type envLED1Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvLED1Control_Type.__name__ = "Integer32"
_EnvLED1Control_Object = MibScalar
envLED1Control = _EnvLED1Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 2, 3),
    _EnvLED1Control_Type()
)
envLED1Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED1Control.setStatus("mandatory")
_EnvLED2_ObjectIdentity = ObjectIdentity
envLED2 = _EnvLED2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 3)
)


class _EnvLED2State_Type(Integer32):
    """Custom type envLED2State based on Integer32"""
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


_EnvLED2State_Type.__name__ = "Integer32"
_EnvLED2State_Object = MibScalar
envLED2State = _EnvLED2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 3, 1),
    _EnvLED2State_Type()
)
envLED2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED2State.setStatus("mandatory")
_EnvLED2Label_Type = DisplayString
_EnvLED2Label_Object = MibScalar
envLED2Label = _EnvLED2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 3, 2),
    _EnvLED2Label_Type()
)
envLED2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED2Label.setStatus("mandatory")


class _EnvLED2Control_Type(Integer32):
    """Custom type envLED2Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvLED2Control_Type.__name__ = "Integer32"
_EnvLED2Control_Object = MibScalar
envLED2Control = _EnvLED2Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 3, 3),
    _EnvLED2Control_Type()
)
envLED2Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED2Control.setStatus("mandatory")
_EnvLED3_ObjectIdentity = ObjectIdentity
envLED3 = _EnvLED3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 4)
)


class _EnvLED3State_Type(Integer32):
    """Custom type envLED3State based on Integer32"""
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


_EnvLED3State_Type.__name__ = "Integer32"
_EnvLED3State_Object = MibScalar
envLED3State = _EnvLED3State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 4, 1),
    _EnvLED3State_Type()
)
envLED3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED3State.setStatus("mandatory")
_EnvLED3Label_Type = DisplayString
_EnvLED3Label_Object = MibScalar
envLED3Label = _EnvLED3Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 4, 2),
    _EnvLED3Label_Type()
)
envLED3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED3Label.setStatus("mandatory")


class _EnvLED3Control_Type(Integer32):
    """Custom type envLED3Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvLED3Control_Type.__name__ = "Integer32"
_EnvLED3Control_Object = MibScalar
envLED3Control = _EnvLED3Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 4, 3),
    _EnvLED3Control_Type()
)
envLED3Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED3Control.setStatus("mandatory")
_EnvReceptacles_ObjectIdentity = ObjectIdentity
envReceptacles = _EnvReceptacles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5)
)
_EnvReceptacle1_ObjectIdentity = ObjectIdentity
envReceptacle1 = _EnvReceptacle1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 1)
)


class _EnvReceptacle1State_Type(Integer32):
    """Custom type envReceptacle1State based on Integer32"""
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


_EnvReceptacle1State_Type.__name__ = "Integer32"
_EnvReceptacle1State_Object = MibScalar
envReceptacle1State = _EnvReceptacle1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 1, 1),
    _EnvReceptacle1State_Type()
)
envReceptacle1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle1State.setStatus("mandatory")
_EnvReceptacle1Label_Type = DisplayString
_EnvReceptacle1Label_Object = MibScalar
envReceptacle1Label = _EnvReceptacle1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 1, 2),
    _EnvReceptacle1Label_Type()
)
envReceptacle1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle1Label.setStatus("mandatory")
_EnvReceptacle2_ObjectIdentity = ObjectIdentity
envReceptacle2 = _EnvReceptacle2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 2)
)


class _EnvReceptacle2State_Type(Integer32):
    """Custom type envReceptacle2State based on Integer32"""
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


_EnvReceptacle2State_Type.__name__ = "Integer32"
_EnvReceptacle2State_Object = MibScalar
envReceptacle2State = _EnvReceptacle2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 2, 1),
    _EnvReceptacle2State_Type()
)
envReceptacle2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle2State.setStatus("mandatory")
_EnvReceptacle2Label_Type = DisplayString
_EnvReceptacle2Label_Object = MibScalar
envReceptacle2Label = _EnvReceptacle2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 2, 2),
    _EnvReceptacle2Label_Type()
)
envReceptacle2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle2Label.setStatus("mandatory")
_EnvReceptacle3_ObjectIdentity = ObjectIdentity
envReceptacle3 = _EnvReceptacle3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 3)
)


class _EnvReceptacle3State_Type(Integer32):
    """Custom type envReceptacle3State based on Integer32"""
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


_EnvReceptacle3State_Type.__name__ = "Integer32"
_EnvReceptacle3State_Object = MibScalar
envReceptacle3State = _EnvReceptacle3State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 3, 1),
    _EnvReceptacle3State_Type()
)
envReceptacle3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle3State.setStatus("mandatory")
_EnvReceptacle3Label_Type = DisplayString
_EnvReceptacle3Label_Object = MibScalar
envReceptacle3Label = _EnvReceptacle3Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 3, 2),
    _EnvReceptacle3Label_Type()
)
envReceptacle3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle3Label.setStatus("mandatory")
_EnvReceptacle4_ObjectIdentity = ObjectIdentity
envReceptacle4 = _EnvReceptacle4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 4)
)


class _EnvReceptacle4State_Type(Integer32):
    """Custom type envReceptacle4State based on Integer32"""
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


_EnvReceptacle4State_Type.__name__ = "Integer32"
_EnvReceptacle4State_Object = MibScalar
envReceptacle4State = _EnvReceptacle4State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 4, 1),
    _EnvReceptacle4State_Type()
)
envReceptacle4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle4State.setStatus("mandatory")
_EnvReceptacle4Label_Type = DisplayString
_EnvReceptacle4Label_Object = MibScalar
envReceptacle4Label = _EnvReceptacle4Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 4, 2),
    _EnvReceptacle4Label_Type()
)
envReceptacle4Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle4Label.setStatus("mandatory")
_EnvAlarms_ObjectIdentity = ObjectIdentity
envAlarms = _EnvAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 6)
)


class _EnvSummaryAlarm_Type(Integer32):
    """Custom type envSummaryAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvSummaryAlarm_Type.__name__ = "Integer32"
_EnvSummaryAlarm_Object = MibScalar
envSummaryAlarm = _EnvSummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 6, 1),
    _EnvSummaryAlarm_Type()
)
envSummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envSummaryAlarm.setStatus("mandatory")
_EnvTemperatureSensors_ObjectIdentity = ObjectIdentity
envTemperatureSensors = _EnvTemperatureSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7)
)
_EnvTemperature1_ObjectIdentity = ObjectIdentity
envTemperature1 = _EnvTemperature1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1)
)


class _EnvTemperature1State_Type(Integer32):
    """Custom type envTemperature1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_EnvTemperature1State_Type.__name__ = "Integer32"
_EnvTemperature1State_Object = MibScalar
envTemperature1State = _EnvTemperature1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 1),
    _EnvTemperature1State_Type()
)
envTemperature1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature1State.setStatus("mandatory")


class _EnvTemperature1F_Type(Integer32):
    """Custom type envTemperature1F based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature1F_Type.__name__ = "Integer32"
_EnvTemperature1F_Object = MibScalar
envTemperature1F = _EnvTemperature1F_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 2),
    _EnvTemperature1F_Type()
)
envTemperature1F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature1F.setStatus("mandatory")


class _EnvTemperature1C_Type(Integer32):
    """Custom type envTemperature1C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature1C_Type.__name__ = "Integer32"
_EnvTemperature1C_Object = MibScalar
envTemperature1C = _EnvTemperature1C_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 3),
    _EnvTemperature1C_Type()
)
envTemperature1C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature1C.setStatus("mandatory")
_EnvTemperature1Label_Type = DisplayString
_EnvTemperature1Label_Object = MibScalar
envTemperature1Label = _EnvTemperature1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 4),
    _EnvTemperature1Label_Type()
)
envTemperature1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature1Label.setStatus("mandatory")


class _EnvTemperature1OffsetF_Type(Integer32):
    """Custom type envTemperature1OffsetF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature1OffsetF_Type.__name__ = "Integer32"
_EnvTemperature1OffsetF_Object = MibScalar
envTemperature1OffsetF = _EnvTemperature1OffsetF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 5),
    _EnvTemperature1OffsetF_Type()
)
envTemperature1OffsetF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature1OffsetF.setStatus("mandatory")


class _EnvTemperature1OffsetC_Type(Integer32):
    """Custom type envTemperature1OffsetC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature1OffsetC_Type.__name__ = "Integer32"
_EnvTemperature1OffsetC_Object = MibScalar
envTemperature1OffsetC = _EnvTemperature1OffsetC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 6),
    _EnvTemperature1OffsetC_Type()
)
envTemperature1OffsetC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature1OffsetC.setStatus("mandatory")


class _EnvTemp1HighLimitF_Type(Integer32):
    """Custom type envTemp1HighLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp1HighLimitF_Type.__name__ = "Integer32"
_EnvTemp1HighLimitF_Object = MibScalar
envTemp1HighLimitF = _EnvTemp1HighLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 7),
    _EnvTemp1HighLimitF_Type()
)
envTemp1HighLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp1HighLimitF.setStatus("mandatory")


class _EnvTemp1HighLimitC_Type(Integer32):
    """Custom type envTemp1HighLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp1HighLimitC_Type.__name__ = "Integer32"
_EnvTemp1HighLimitC_Object = MibScalar
envTemp1HighLimitC = _EnvTemp1HighLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 8),
    _EnvTemp1HighLimitC_Type()
)
envTemp1HighLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp1HighLimitC.setStatus("mandatory")


class _EnvTemp1LowLimitF_Type(Integer32):
    """Custom type envTemp1LowLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp1LowLimitF_Type.__name__ = "Integer32"
_EnvTemp1LowLimitF_Object = MibScalar
envTemp1LowLimitF = _EnvTemp1LowLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 9),
    _EnvTemp1LowLimitF_Type()
)
envTemp1LowLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp1LowLimitF.setStatus("mandatory")


class _EnvTemp1LowLimitC_Type(Integer32):
    """Custom type envTemp1LowLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp1LowLimitC_Type.__name__ = "Integer32"
_EnvTemp1LowLimitC_Object = MibScalar
envTemp1LowLimitC = _EnvTemp1LowLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 10),
    _EnvTemp1LowLimitC_Type()
)
envTemp1LowLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp1LowLimitC.setStatus("mandatory")
_EnvTemperature2_ObjectIdentity = ObjectIdentity
envTemperature2 = _EnvTemperature2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2)
)


class _EnvTemperature2State_Type(Integer32):
    """Custom type envTemperature2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_EnvTemperature2State_Type.__name__ = "Integer32"
_EnvTemperature2State_Object = MibScalar
envTemperature2State = _EnvTemperature2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 1),
    _EnvTemperature2State_Type()
)
envTemperature2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature2State.setStatus("mandatory")


class _EnvTemperature2F_Type(Integer32):
    """Custom type envTemperature2F based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature2F_Type.__name__ = "Integer32"
_EnvTemperature2F_Object = MibScalar
envTemperature2F = _EnvTemperature2F_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 2),
    _EnvTemperature2F_Type()
)
envTemperature2F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature2F.setStatus("mandatory")


class _EnvTemperature2C_Type(Integer32):
    """Custom type envTemperature2C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature2C_Type.__name__ = "Integer32"
_EnvTemperature2C_Object = MibScalar
envTemperature2C = _EnvTemperature2C_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 3),
    _EnvTemperature2C_Type()
)
envTemperature2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature2C.setStatus("mandatory")
_EnvTemperature2Label_Type = DisplayString
_EnvTemperature2Label_Object = MibScalar
envTemperature2Label = _EnvTemperature2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 4),
    _EnvTemperature2Label_Type()
)
envTemperature2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature2Label.setStatus("mandatory")


class _EnvTemperature2OffsetF_Type(Integer32):
    """Custom type envTemperature2OffsetF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature2OffsetF_Type.__name__ = "Integer32"
_EnvTemperature2OffsetF_Object = MibScalar
envTemperature2OffsetF = _EnvTemperature2OffsetF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 5),
    _EnvTemperature2OffsetF_Type()
)
envTemperature2OffsetF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature2OffsetF.setStatus("mandatory")


class _EnvTemperature2OffsetC_Type(Integer32):
    """Custom type envTemperature2OffsetC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature2OffsetC_Type.__name__ = "Integer32"
_EnvTemperature2OffsetC_Object = MibScalar
envTemperature2OffsetC = _EnvTemperature2OffsetC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 6),
    _EnvTemperature2OffsetC_Type()
)
envTemperature2OffsetC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature2OffsetC.setStatus("mandatory")


class _EnvTemp2HighLimitF_Type(Integer32):
    """Custom type envTemp2HighLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp2HighLimitF_Type.__name__ = "Integer32"
_EnvTemp2HighLimitF_Object = MibScalar
envTemp2HighLimitF = _EnvTemp2HighLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 7),
    _EnvTemp2HighLimitF_Type()
)
envTemp2HighLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp2HighLimitF.setStatus("mandatory")


class _EnvTemp2HighLimitC_Type(Integer32):
    """Custom type envTemp2HighLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp2HighLimitC_Type.__name__ = "Integer32"
_EnvTemp2HighLimitC_Object = MibScalar
envTemp2HighLimitC = _EnvTemp2HighLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 8),
    _EnvTemp2HighLimitC_Type()
)
envTemp2HighLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp2HighLimitC.setStatus("mandatory")


class _EnvTemp2LowLimitF_Type(Integer32):
    """Custom type envTemp2LowLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp2LowLimitF_Type.__name__ = "Integer32"
_EnvTemp2LowLimitF_Object = MibScalar
envTemp2LowLimitF = _EnvTemp2LowLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 9),
    _EnvTemp2LowLimitF_Type()
)
envTemp2LowLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp2LowLimitF.setStatus("mandatory")


class _EnvTemp2LowLimitC_Type(Integer32):
    """Custom type envTemp2LowLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp2LowLimitC_Type.__name__ = "Integer32"
_EnvTemp2LowLimitC_Object = MibScalar
envTemp2LowLimitC = _EnvTemp2LowLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 10),
    _EnvTemp2LowLimitC_Type()
)
envTemp2LowLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp2LowLimitC.setStatus("mandatory")
_EnvTemperature3_ObjectIdentity = ObjectIdentity
envTemperature3 = _EnvTemperature3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3)
)


class _EnvTemperature3State_Type(Integer32):
    """Custom type envTemperature3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("airSensorInstalled", 2),
          ("notInstalled", 1),
          ("waterSensorInstalled", 3))
    )


_EnvTemperature3State_Type.__name__ = "Integer32"
_EnvTemperature3State_Object = MibScalar
envTemperature3State = _EnvTemperature3State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 1),
    _EnvTemperature3State_Type()
)
envTemperature3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature3State.setStatus("mandatory")


class _EnvTemperature3F_Type(Integer32):
    """Custom type envTemperature3F based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature3F_Type.__name__ = "Integer32"
_EnvTemperature3F_Object = MibScalar
envTemperature3F = _EnvTemperature3F_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 2),
    _EnvTemperature3F_Type()
)
envTemperature3F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature3F.setStatus("mandatory")


class _EnvTemperature3C_Type(Integer32):
    """Custom type envTemperature3C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature3C_Type.__name__ = "Integer32"
_EnvTemperature3C_Object = MibScalar
envTemperature3C = _EnvTemperature3C_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 3),
    _EnvTemperature3C_Type()
)
envTemperature3C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature3C.setStatus("mandatory")
_EnvTemperature3Label_Type = DisplayString
_EnvTemperature3Label_Object = MibScalar
envTemperature3Label = _EnvTemperature3Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 4),
    _EnvTemperature3Label_Type()
)
envTemperature3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature3Label.setStatus("mandatory")


class _EnvTemperature3OffsetF_Type(Integer32):
    """Custom type envTemperature3OffsetF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature3OffsetF_Type.__name__ = "Integer32"
_EnvTemperature3OffsetF_Object = MibScalar
envTemperature3OffsetF = _EnvTemperature3OffsetF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 5),
    _EnvTemperature3OffsetF_Type()
)
envTemperature3OffsetF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature3OffsetF.setStatus("mandatory")


class _EnvTemperature3OffsetC_Type(Integer32):
    """Custom type envTemperature3OffsetC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature3OffsetC_Type.__name__ = "Integer32"
_EnvTemperature3OffsetC_Object = MibScalar
envTemperature3OffsetC = _EnvTemperature3OffsetC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 6),
    _EnvTemperature3OffsetC_Type()
)
envTemperature3OffsetC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature3OffsetC.setStatus("mandatory")


class _EnvTemp3HighLimitF_Type(Integer32):
    """Custom type envTemp3HighLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp3HighLimitF_Type.__name__ = "Integer32"
_EnvTemp3HighLimitF_Object = MibScalar
envTemp3HighLimitF = _EnvTemp3HighLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 7),
    _EnvTemp3HighLimitF_Type()
)
envTemp3HighLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp3HighLimitF.setStatus("mandatory")


class _EnvTemp3HighLimitC_Type(Integer32):
    """Custom type envTemp3HighLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp3HighLimitC_Type.__name__ = "Integer32"
_EnvTemp3HighLimitC_Object = MibScalar
envTemp3HighLimitC = _EnvTemp3HighLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 8),
    _EnvTemp3HighLimitC_Type()
)
envTemp3HighLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp3HighLimitC.setStatus("mandatory")


class _EnvTemp3LowLimitF_Type(Integer32):
    """Custom type envTemp3LowLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp3LowLimitF_Type.__name__ = "Integer32"
_EnvTemp3LowLimitF_Object = MibScalar
envTemp3LowLimitF = _EnvTemp3LowLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 9),
    _EnvTemp3LowLimitF_Type()
)
envTemp3LowLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp3LowLimitF.setStatus("mandatory")


class _EnvTemp3LowLimitC_Type(Integer32):
    """Custom type envTemp3LowLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp3LowLimitC_Type.__name__ = "Integer32"
_EnvTemp3LowLimitC_Object = MibScalar
envTemp3LowLimitC = _EnvTemp3LowLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 10),
    _EnvTemp3LowLimitC_Type()
)
envTemp3LowLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp3LowLimitC.setStatus("mandatory")


class _EnvTemp3Calibrate_Type(Integer32):
    """Custom type envTemp3Calibrate based on Integer32"""
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


_EnvTemp3Calibrate_Type.__name__ = "Integer32"
_EnvTemp3Calibrate_Object = MibScalar
envTemp3Calibrate = _EnvTemp3Calibrate_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 11),
    _EnvTemp3Calibrate_Type()
)
envTemp3Calibrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp3Calibrate.setStatus("mandatory")
_EnvHumiditySensors_ObjectIdentity = ObjectIdentity
envHumiditySensors = _EnvHumiditySensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8)
)
_EnvHumidity1_ObjectIdentity = ObjectIdentity
envHumidity1 = _EnvHumidity1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1)
)


class _EnvHumidity1State_Type(Integer32):
    """Custom type envHumidity1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_EnvHumidity1State_Type.__name__ = "Integer32"
_EnvHumidity1State_Object = MibScalar
envHumidity1State = _EnvHumidity1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 1),
    _EnvHumidity1State_Type()
)
envHumidity1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity1State.setStatus("mandatory")


class _EnvHumidity1RH_Type(Integer32):
    """Custom type envHumidity1RH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity1RH_Type.__name__ = "Integer32"
_EnvHumidity1RH_Object = MibScalar
envHumidity1RH = _EnvHumidity1RH_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 2),
    _EnvHumidity1RH_Type()
)
envHumidity1RH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envHumidity1RH.setStatus("mandatory")
_EnvHumidity1Label_Type = DisplayString
_EnvHumidity1Label_Object = MibScalar
envHumidity1Label = _EnvHumidity1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 3),
    _EnvHumidity1Label_Type()
)
envHumidity1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity1Label.setStatus("mandatory")


class _EnvHumidity1Offset_Type(Integer32):
    """Custom type envHumidity1Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity1Offset_Type.__name__ = "Integer32"
_EnvHumidity1Offset_Object = MibScalar
envHumidity1Offset = _EnvHumidity1Offset_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 4),
    _EnvHumidity1Offset_Type()
)
envHumidity1Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity1Offset.setStatus("mandatory")


class _EnvHumidity1HighLimit_Type(Integer32):
    """Custom type envHumidity1HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity1HighLimit_Type.__name__ = "Integer32"
_EnvHumidity1HighLimit_Object = MibScalar
envHumidity1HighLimit = _EnvHumidity1HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 5),
    _EnvHumidity1HighLimit_Type()
)
envHumidity1HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity1HighLimit.setStatus("mandatory")


class _EnvHumidity1LowLimit_Type(Integer32):
    """Custom type envHumidity1LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity1LowLimit_Type.__name__ = "Integer32"
_EnvHumidity1LowLimit_Object = MibScalar
envHumidity1LowLimit = _EnvHumidity1LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 6),
    _EnvHumidity1LowLimit_Type()
)
envHumidity1LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity1LowLimit.setStatus("mandatory")
_EnvHumidity2_ObjectIdentity = ObjectIdentity
envHumidity2 = _EnvHumidity2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2)
)


class _EnvHumidity2State_Type(Integer32):
    """Custom type envHumidity2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_EnvHumidity2State_Type.__name__ = "Integer32"
_EnvHumidity2State_Object = MibScalar
envHumidity2State = _EnvHumidity2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 1),
    _EnvHumidity2State_Type()
)
envHumidity2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity2State.setStatus("mandatory")


class _EnvHumidity2RH_Type(Integer32):
    """Custom type envHumidity2RH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity2RH_Type.__name__ = "Integer32"
_EnvHumidity2RH_Object = MibScalar
envHumidity2RH = _EnvHumidity2RH_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 2),
    _EnvHumidity2RH_Type()
)
envHumidity2RH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envHumidity2RH.setStatus("mandatory")
_EnvHumidity2Label_Type = DisplayString
_EnvHumidity2Label_Object = MibScalar
envHumidity2Label = _EnvHumidity2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 3),
    _EnvHumidity2Label_Type()
)
envHumidity2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity2Label.setStatus("mandatory")


class _EnvHumidity2Offset_Type(Integer32):
    """Custom type envHumidity2Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity2Offset_Type.__name__ = "Integer32"
_EnvHumidity2Offset_Object = MibScalar
envHumidity2Offset = _EnvHumidity2Offset_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 4),
    _EnvHumidity2Offset_Type()
)
envHumidity2Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity2Offset.setStatus("mandatory")


class _EnvHumidity2HighLimit_Type(Integer32):
    """Custom type envHumidity2HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity2HighLimit_Type.__name__ = "Integer32"
_EnvHumidity2HighLimit_Object = MibScalar
envHumidity2HighLimit = _EnvHumidity2HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 5),
    _EnvHumidity2HighLimit_Type()
)
envHumidity2HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity2HighLimit.setStatus("mandatory")


class _EnvHumidity2LowLimit_Type(Integer32):
    """Custom type envHumidity2LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity2LowLimit_Type.__name__ = "Integer32"
_EnvHumidity2LowLimit_Object = MibScalar
envHumidity2LowLimit = _EnvHumidity2LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 6),
    _EnvHumidity2LowLimit_Type()
)
envHumidity2LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity2LowLimit.setStatus("mandatory")
_EnvTraps_ObjectIdentity = ObjectIdentity
envTraps = _EnvTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11)
)
_LeExperimental_ObjectIdentity = ObjectIdentity
leExperimental = _LeExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 2)
)
_LePrivate_ObjectIdentity = ObjectIdentity
lePrivate = _LePrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 3)
)

# Managed Objects groups


# Notification objects

envSummaryAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 1)
)
if mibBuilder.loadTexts:
    envSummaryAlarmTrap.setStatus(
        ""
    )

envDigInput1TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 2)
)
if mibBuilder.loadTexts:
    envDigInput1TrueTrap.setStatus(
        ""
    )

envDigInput1FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 3)
)
if mibBuilder.loadTexts:
    envDigInput1FalseTrap.setStatus(
        ""
    )

envDigInput2TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 4)
)
if mibBuilder.loadTexts:
    envDigInput2TrueTrap.setStatus(
        ""
    )

envDigInput2FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 5)
)
if mibBuilder.loadTexts:
    envDigInput2FalseTrap.setStatus(
        ""
    )

envDigInput3TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 6)
)
if mibBuilder.loadTexts:
    envDigInput3TrueTrap.setStatus(
        ""
    )

envDigInput3FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 7)
)
if mibBuilder.loadTexts:
    envDigInput3FalseTrap.setStatus(
        ""
    )

envDigInput4TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 8)
)
if mibBuilder.loadTexts:
    envDigInput4TrueTrap.setStatus(
        ""
    )

envDigInput4FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 9)
)
if mibBuilder.loadTexts:
    envDigInput4FalseTrap.setStatus(
        ""
    )

envDigInput5TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 10)
)
if mibBuilder.loadTexts:
    envDigInput5TrueTrap.setStatus(
        ""
    )

envDigInput5FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 11)
)
if mibBuilder.loadTexts:
    envDigInput5FalseTrap.setStatus(
        ""
    )

envDigInput6TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 12)
)
if mibBuilder.loadTexts:
    envDigInput6TrueTrap.setStatus(
        ""
    )

envDigInput6FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 13)
)
if mibBuilder.loadTexts:
    envDigInput6FalseTrap.setStatus(
        ""
    )

envDigInput7TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 14)
)
if mibBuilder.loadTexts:
    envDigInput7TrueTrap.setStatus(
        ""
    )

envDigInput7FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 15)
)
if mibBuilder.loadTexts:
    envDigInput7FalseTrap.setStatus(
        ""
    )

envDigInput8TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 16)
)
if mibBuilder.loadTexts:
    envDigInput8TrueTrap.setStatus(
        ""
    )

envDigInput8FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 17)
)
if mibBuilder.loadTexts:
    envDigInput8FalseTrap.setStatus(
        ""
    )

envDigInput9TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 18)
)
if mibBuilder.loadTexts:
    envDigInput9TrueTrap.setStatus(
        ""
    )

envDigInput9FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 19)
)
if mibBuilder.loadTexts:
    envDigInput9FalseTrap.setStatus(
        ""
    )

envDigInput10TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 20)
)
if mibBuilder.loadTexts:
    envDigInput10TrueTrap.setStatus(
        ""
    )

envDigInput10FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 21)
)
if mibBuilder.loadTexts:
    envDigInput10FalseTrap.setStatus(
        ""
    )

envTemperature1HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 22)
)
if mibBuilder.loadTexts:
    envTemperature1HighTrap.setStatus(
        ""
    )

envTemperature1LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 23)
)
if mibBuilder.loadTexts:
    envTemperature1LowTrap.setStatus(
        ""
    )

envTemperature1NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 24)
)
if mibBuilder.loadTexts:
    envTemperature1NormalTrap.setStatus(
        ""
    )

envTemperature2HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 25)
)
if mibBuilder.loadTexts:
    envTemperature2HighTrap.setStatus(
        ""
    )

envTemperature2LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 26)
)
if mibBuilder.loadTexts:
    envTemperature2LowTrap.setStatus(
        ""
    )

envTemperature2NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 27)
)
if mibBuilder.loadTexts:
    envTemperature2NormalTrap.setStatus(
        ""
    )

envTemperature3HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 28)
)
if mibBuilder.loadTexts:
    envTemperature3HighTrap.setStatus(
        ""
    )

envTemperature3LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 29)
)
if mibBuilder.loadTexts:
    envTemperature3LowTrap.setStatus(
        ""
    )

envTemperature3NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 30)
)
if mibBuilder.loadTexts:
    envTemperature3NormalTrap.setStatus(
        ""
    )

envHumidity1HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 31)
)
if mibBuilder.loadTexts:
    envHumidity1HighTrap.setStatus(
        ""
    )

envHumidity1LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 32)
)
if mibBuilder.loadTexts:
    envHumidity1LowTrap.setStatus(
        ""
    )

envHumidity1NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 33)
)
if mibBuilder.loadTexts:
    envHumidity1NormalTrap.setStatus(
        ""
    )

envHumidity2HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 34)
)
if mibBuilder.loadTexts:
    envHumidity2HighTrap.setStatus(
        ""
    )

envHumidity2LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 35)
)
if mibBuilder.loadTexts:
    envHumidity2LowTrap.setStatus(
        ""
    )

envHumidity2NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 36)
)
if mibBuilder.loadTexts:
    envHumidity2NormalTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-SITENET-INTEGRATOR-MIB",
    **{"emerson": emerson,
       "liebertCorp": liebertCorp,
       "liebertUps": liebertUps,
       "liebertEnvironment": liebertEnvironment,
       "leExtensions": leExtensions,
       "leSiteNet01": leSiteNet01,
       "envMIB": envMIB,
       "envIdent": envIdent,
       "envIdentManufacturer": envIdentManufacturer,
       "envIdentModel": envIdentModel,
       "envIdentSoftwareVersion": envIdentSoftwareVersion,
       "envIdentSpecific": envIdentSpecific,
       "envDigitalInputs": envDigitalInputs,
       "envDigInput1": envDigInput1,
       "envDigInput1State": envDigInput1State,
       "envDigInput1Label": envDigInput1Label,
       "envDigInput1Polarity": envDigInput1Polarity,
       "envDigInput1TrapEnabled": envDigInput1TrapEnabled,
       "envDigInput2": envDigInput2,
       "envDigInput2State": envDigInput2State,
       "envDigInput2Label": envDigInput2Label,
       "envDigInput2Polarity": envDigInput2Polarity,
       "envDigInput2TrapEnabled": envDigInput2TrapEnabled,
       "envDigInput3": envDigInput3,
       "envDigInput3State": envDigInput3State,
       "envDigInput3Label": envDigInput3Label,
       "envDigInput3Polarity": envDigInput3Polarity,
       "envDigInput3TrapEnabled": envDigInput3TrapEnabled,
       "envDigInput4": envDigInput4,
       "envDigInput4State": envDigInput4State,
       "envDigInput4Label": envDigInput4Label,
       "envDigInput4Polarity": envDigInput4Polarity,
       "envDigInput4TrapEnabled": envDigInput4TrapEnabled,
       "envDigInput5": envDigInput5,
       "envDigInput5State": envDigInput5State,
       "envDigInput5Label": envDigInput5Label,
       "envDigInput5Polarity": envDigInput5Polarity,
       "envDigInput5TrapEnabled": envDigInput5TrapEnabled,
       "envDigInput6": envDigInput6,
       "envDigInput6State": envDigInput6State,
       "envDigInput6Label": envDigInput6Label,
       "envDigInput6Polarity": envDigInput6Polarity,
       "envDigInput6TrapEnabled": envDigInput6TrapEnabled,
       "envDigInput7": envDigInput7,
       "envDigInput7State": envDigInput7State,
       "envDigInput7Label": envDigInput7Label,
       "envDigInput7Polarity": envDigInput7Polarity,
       "envDigInput7TrapEnabled": envDigInput7TrapEnabled,
       "envDigInput8": envDigInput8,
       "envDigInput8State": envDigInput8State,
       "envDigInput8Label": envDigInput8Label,
       "envDigInput8Polarity": envDigInput8Polarity,
       "envDigInput8TrapEnabled": envDigInput8TrapEnabled,
       "envDigInput9": envDigInput9,
       "envDigInput9State": envDigInput9State,
       "envDigInput9Label": envDigInput9Label,
       "envDigInput9Polarity": envDigInput9Polarity,
       "envDigInput9TrapEnabled": envDigInput9TrapEnabled,
       "envDigInput10": envDigInput10,
       "envDigInput10State": envDigInput10State,
       "envDigInput10Label": envDigInput10Label,
       "envDigInput10Polarity": envDigInput10Polarity,
       "envDigInput10TrapEnabled": envDigInput10TrapEnabled,
       "envRelays": envRelays,
       "envRelay1": envRelay1,
       "envRelay1State": envRelay1State,
       "envRelay1Label": envRelay1Label,
       "envRelay1Control": envRelay1Control,
       "envRelay2": envRelay2,
       "envRelay2State": envRelay2State,
       "envRelay2Label": envRelay2Label,
       "envRelay2Control": envRelay2Control,
       "envOutputs": envOutputs,
       "envAudible": envAudible,
       "envAudibleState": envAudibleState,
       "envAudibleControl": envAudibleControl,
       "envLED1": envLED1,
       "envLED1State": envLED1State,
       "envLED1Label": envLED1Label,
       "envLED1Control": envLED1Control,
       "envLED2": envLED2,
       "envLED2State": envLED2State,
       "envLED2Label": envLED2Label,
       "envLED2Control": envLED2Control,
       "envLED3": envLED3,
       "envLED3State": envLED3State,
       "envLED3Label": envLED3Label,
       "envLED3Control": envLED3Control,
       "envReceptacles": envReceptacles,
       "envReceptacle1": envReceptacle1,
       "envReceptacle1State": envReceptacle1State,
       "envReceptacle1Label": envReceptacle1Label,
       "envReceptacle2": envReceptacle2,
       "envReceptacle2State": envReceptacle2State,
       "envReceptacle2Label": envReceptacle2Label,
       "envReceptacle3": envReceptacle3,
       "envReceptacle3State": envReceptacle3State,
       "envReceptacle3Label": envReceptacle3Label,
       "envReceptacle4": envReceptacle4,
       "envReceptacle4State": envReceptacle4State,
       "envReceptacle4Label": envReceptacle4Label,
       "envAlarms": envAlarms,
       "envSummaryAlarm": envSummaryAlarm,
       "envTemperatureSensors": envTemperatureSensors,
       "envTemperature1": envTemperature1,
       "envTemperature1State": envTemperature1State,
       "envTemperature1F": envTemperature1F,
       "envTemperature1C": envTemperature1C,
       "envTemperature1Label": envTemperature1Label,
       "envTemperature1OffsetF": envTemperature1OffsetF,
       "envTemperature1OffsetC": envTemperature1OffsetC,
       "envTemp1HighLimitF": envTemp1HighLimitF,
       "envTemp1HighLimitC": envTemp1HighLimitC,
       "envTemp1LowLimitF": envTemp1LowLimitF,
       "envTemp1LowLimitC": envTemp1LowLimitC,
       "envTemperature2": envTemperature2,
       "envTemperature2State": envTemperature2State,
       "envTemperature2F": envTemperature2F,
       "envTemperature2C": envTemperature2C,
       "envTemperature2Label": envTemperature2Label,
       "envTemperature2OffsetF": envTemperature2OffsetF,
       "envTemperature2OffsetC": envTemperature2OffsetC,
       "envTemp2HighLimitF": envTemp2HighLimitF,
       "envTemp2HighLimitC": envTemp2HighLimitC,
       "envTemp2LowLimitF": envTemp2LowLimitF,
       "envTemp2LowLimitC": envTemp2LowLimitC,
       "envTemperature3": envTemperature3,
       "envTemperature3State": envTemperature3State,
       "envTemperature3F": envTemperature3F,
       "envTemperature3C": envTemperature3C,
       "envTemperature3Label": envTemperature3Label,
       "envTemperature3OffsetF": envTemperature3OffsetF,
       "envTemperature3OffsetC": envTemperature3OffsetC,
       "envTemp3HighLimitF": envTemp3HighLimitF,
       "envTemp3HighLimitC": envTemp3HighLimitC,
       "envTemp3LowLimitF": envTemp3LowLimitF,
       "envTemp3LowLimitC": envTemp3LowLimitC,
       "envTemp3Calibrate": envTemp3Calibrate,
       "envHumiditySensors": envHumiditySensors,
       "envHumidity1": envHumidity1,
       "envHumidity1State": envHumidity1State,
       "envHumidity1RH": envHumidity1RH,
       "envHumidity1Label": envHumidity1Label,
       "envHumidity1Offset": envHumidity1Offset,
       "envHumidity1HighLimit": envHumidity1HighLimit,
       "envHumidity1LowLimit": envHumidity1LowLimit,
       "envHumidity2": envHumidity2,
       "envHumidity2State": envHumidity2State,
       "envHumidity2RH": envHumidity2RH,
       "envHumidity2Label": envHumidity2Label,
       "envHumidity2Offset": envHumidity2Offset,
       "envHumidity2HighLimit": envHumidity2HighLimit,
       "envHumidity2LowLimit": envHumidity2LowLimit,
       "envTraps": envTraps,
       "envSummaryAlarmTrap": envSummaryAlarmTrap,
       "envDigInput1TrueTrap": envDigInput1TrueTrap,
       "envDigInput1FalseTrap": envDigInput1FalseTrap,
       "envDigInput2TrueTrap": envDigInput2TrueTrap,
       "envDigInput2FalseTrap": envDigInput2FalseTrap,
       "envDigInput3TrueTrap": envDigInput3TrueTrap,
       "envDigInput3FalseTrap": envDigInput3FalseTrap,
       "envDigInput4TrueTrap": envDigInput4TrueTrap,
       "envDigInput4FalseTrap": envDigInput4FalseTrap,
       "envDigInput5TrueTrap": envDigInput5TrueTrap,
       "envDigInput5FalseTrap": envDigInput5FalseTrap,
       "envDigInput6TrueTrap": envDigInput6TrueTrap,
       "envDigInput6FalseTrap": envDigInput6FalseTrap,
       "envDigInput7TrueTrap": envDigInput7TrueTrap,
       "envDigInput7FalseTrap": envDigInput7FalseTrap,
       "envDigInput8TrueTrap": envDigInput8TrueTrap,
       "envDigInput8FalseTrap": envDigInput8FalseTrap,
       "envDigInput9TrueTrap": envDigInput9TrueTrap,
       "envDigInput9FalseTrap": envDigInput9FalseTrap,
       "envDigInput10TrueTrap": envDigInput10TrueTrap,
       "envDigInput10FalseTrap": envDigInput10FalseTrap,
       "envTemperature1HighTrap": envTemperature1HighTrap,
       "envTemperature1LowTrap": envTemperature1LowTrap,
       "envTemperature1NormalTrap": envTemperature1NormalTrap,
       "envTemperature2HighTrap": envTemperature2HighTrap,
       "envTemperature2LowTrap": envTemperature2LowTrap,
       "envTemperature2NormalTrap": envTemperature2NormalTrap,
       "envTemperature3HighTrap": envTemperature3HighTrap,
       "envTemperature3LowTrap": envTemperature3LowTrap,
       "envTemperature3NormalTrap": envTemperature3NormalTrap,
       "envHumidity1HighTrap": envHumidity1HighTrap,
       "envHumidity1LowTrap": envHumidity1LowTrap,
       "envHumidity1NormalTrap": envHumidity1NormalTrap,
       "envHumidity2HighTrap": envHumidity2HighTrap,
       "envHumidity2LowTrap": envHumidity2LowTrap,
       "envHumidity2NormalTrap": envHumidity2NormalTrap,
       "leExperimental": leExperimental,
       "lePrivate": lePrivate}
)
