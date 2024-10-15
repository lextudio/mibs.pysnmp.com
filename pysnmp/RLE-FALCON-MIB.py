# SNMP MIB module (RLE-FALCON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RLE-FALCON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:59 2024
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

(PositiveInteger,
 TruthValue) = mibBuilder.importSymbols(
    "RFC1253-MIB",
    "PositiveInteger",
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

_Rle_ObjectIdentity = ObjectIdentity
rle = _Rle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1)
)
_Falcon_ObjectIdentity = ObjectIdentity
falcon = _Falcon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1)
)
_FalconMIB_ObjectIdentity = ObjectIdentity
falconMIB = _FalconMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1)
)
_FalconIdent_ObjectIdentity = ObjectIdentity
falconIdent = _FalconIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 1)
)
_FalconIdentManufacturer_Type = DisplayString
_FalconIdentManufacturer_Object = MibScalar
falconIdentManufacturer = _FalconIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 1, 1),
    _FalconIdentManufacturer_Type()
)
falconIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconIdentManufacturer.setStatus("mandatory")
_FalconIdentModel_Type = DisplayString
_FalconIdentModel_Object = MibScalar
falconIdentModel = _FalconIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 1, 2),
    _FalconIdentModel_Type()
)
falconIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconIdentModel.setStatus("mandatory")
_FalconIdentSoftwareVersion_Type = DisplayString
_FalconIdentSoftwareVersion_Object = MibScalar
falconIdentSoftwareVersion = _FalconIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 1, 3),
    _FalconIdentSoftwareVersion_Type()
)
falconIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconIdentSoftwareVersion.setStatus("mandatory")
_FalconIdentSpecific_Type = ObjectIdentifier
_FalconIdentSpecific_Object = MibScalar
falconIdentSpecific = _FalconIdentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 1, 4),
    _FalconIdentSpecific_Type()
)
falconIdentSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconIdentSpecific.setStatus("mandatory")
_FalconSystem_ObjectIdentity = ObjectIdentity
falconSystem = _FalconSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2)
)
_FalconClock_Type = DisplayString
_FalconClock_Object = MibScalar
falconClock = _FalconClock_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 1),
    _FalconClock_Type()
)
falconClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconClock.setStatus("mandatory")


class _FalconDoorAlarmBypass_Type(Integer32):
    """Custom type falconDoorAlarmBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconDoorAlarmBypass_Type.__name__ = "Integer32"
_FalconDoorAlarmBypass_Object = MibScalar
falconDoorAlarmBypass = _FalconDoorAlarmBypass_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 2),
    _FalconDoorAlarmBypass_Type()
)
falconDoorAlarmBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconDoorAlarmBypass.setStatus("mandatory")
_FalconKeypad_ObjectIdentity = ObjectIdentity
falconKeypad = _FalconKeypad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3)
)
_FalconKeypadCode1_Type = DisplayString
_FalconKeypadCode1_Object = MibScalar
falconKeypadCode1 = _FalconKeypadCode1_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 1),
    _FalconKeypadCode1_Type()
)
falconKeypadCode1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode1.setStatus("mandatory")
_FalconKeypadName1_Type = DisplayString
_FalconKeypadName1_Object = MibScalar
falconKeypadName1 = _FalconKeypadName1_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 2),
    _FalconKeypadName1_Type()
)
falconKeypadName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName1.setStatus("mandatory")
_FalconKeypadCode2_Type = DisplayString
_FalconKeypadCode2_Object = MibScalar
falconKeypadCode2 = _FalconKeypadCode2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 3),
    _FalconKeypadCode2_Type()
)
falconKeypadCode2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode2.setStatus("mandatory")
_FalconKeypadName2_Type = DisplayString
_FalconKeypadName2_Object = MibScalar
falconKeypadName2 = _FalconKeypadName2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 4),
    _FalconKeypadName2_Type()
)
falconKeypadName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName2.setStatus("mandatory")
_FalconKeypadCode3_Type = DisplayString
_FalconKeypadCode3_Object = MibScalar
falconKeypadCode3 = _FalconKeypadCode3_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 5),
    _FalconKeypadCode3_Type()
)
falconKeypadCode3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode3.setStatus("mandatory")
_FalconKeypadName3_Type = DisplayString
_FalconKeypadName3_Object = MibScalar
falconKeypadName3 = _FalconKeypadName3_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 6),
    _FalconKeypadName3_Type()
)
falconKeypadName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName3.setStatus("mandatory")
_FalconKeypadCode4_Type = DisplayString
_FalconKeypadCode4_Object = MibScalar
falconKeypadCode4 = _FalconKeypadCode4_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 7),
    _FalconKeypadCode4_Type()
)
falconKeypadCode4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode4.setStatus("mandatory")
_FalconKeypadName4_Type = DisplayString
_FalconKeypadName4_Object = MibScalar
falconKeypadName4 = _FalconKeypadName4_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 8),
    _FalconKeypadName4_Type()
)
falconKeypadName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName4.setStatus("mandatory")
_FalconKeypadCode5_Type = DisplayString
_FalconKeypadCode5_Object = MibScalar
falconKeypadCode5 = _FalconKeypadCode5_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 9),
    _FalconKeypadCode5_Type()
)
falconKeypadCode5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode5.setStatus("mandatory")
_FalconKeypadName5_Type = DisplayString
_FalconKeypadName5_Object = MibScalar
falconKeypadName5 = _FalconKeypadName5_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 10),
    _FalconKeypadName5_Type()
)
falconKeypadName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName5.setStatus("mandatory")
_FalconKeypadCode6_Type = DisplayString
_FalconKeypadCode6_Object = MibScalar
falconKeypadCode6 = _FalconKeypadCode6_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 11),
    _FalconKeypadCode6_Type()
)
falconKeypadCode6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode6.setStatus("mandatory")
_FalconKeypadName6_Type = DisplayString
_FalconKeypadName6_Object = MibScalar
falconKeypadName6 = _FalconKeypadName6_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 12),
    _FalconKeypadName6_Type()
)
falconKeypadName6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName6.setStatus("mandatory")
_FalconKeypadCode7_Type = DisplayString
_FalconKeypadCode7_Object = MibScalar
falconKeypadCode7 = _FalconKeypadCode7_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 13),
    _FalconKeypadCode7_Type()
)
falconKeypadCode7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode7.setStatus("mandatory")
_FalconKeypadName7_Type = DisplayString
_FalconKeypadName7_Object = MibScalar
falconKeypadName7 = _FalconKeypadName7_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 14),
    _FalconKeypadName7_Type()
)
falconKeypadName7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName7.setStatus("mandatory")
_FalconKeypadCode8_Type = DisplayString
_FalconKeypadCode8_Object = MibScalar
falconKeypadCode8 = _FalconKeypadCode8_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 15),
    _FalconKeypadCode8_Type()
)
falconKeypadCode8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode8.setStatus("mandatory")
_FalconKeypadName8_Type = DisplayString
_FalconKeypadName8_Object = MibScalar
falconKeypadName8 = _FalconKeypadName8_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 16),
    _FalconKeypadName8_Type()
)
falconKeypadName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName8.setStatus("mandatory")
_FalconKeypadCode9_Type = DisplayString
_FalconKeypadCode9_Object = MibScalar
falconKeypadCode9 = _FalconKeypadCode9_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 17),
    _FalconKeypadCode9_Type()
)
falconKeypadCode9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode9.setStatus("mandatory")
_FalconKeypadName9_Type = DisplayString
_FalconKeypadName9_Object = MibScalar
falconKeypadName9 = _FalconKeypadName9_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 18),
    _FalconKeypadName9_Type()
)
falconKeypadName9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName9.setStatus("mandatory")
_FalconKeypadCode10_Type = DisplayString
_FalconKeypadCode10_Object = MibScalar
falconKeypadCode10 = _FalconKeypadCode10_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 19),
    _FalconKeypadCode10_Type()
)
falconKeypadCode10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode10.setStatus("mandatory")
_FalconKeypadName10_Type = DisplayString
_FalconKeypadName10_Object = MibScalar
falconKeypadName10 = _FalconKeypadName10_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 20),
    _FalconKeypadName10_Type()
)
falconKeypadName10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName10.setStatus("mandatory")
_FalconKeypadCode11_Type = DisplayString
_FalconKeypadCode11_Object = MibScalar
falconKeypadCode11 = _FalconKeypadCode11_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 21),
    _FalconKeypadCode11_Type()
)
falconKeypadCode11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode11.setStatus("mandatory")
_FalconKeypadName11_Type = DisplayString
_FalconKeypadName11_Object = MibScalar
falconKeypadName11 = _FalconKeypadName11_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 22),
    _FalconKeypadName11_Type()
)
falconKeypadName11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName11.setStatus("mandatory")
_FalconKeypadCode12_Type = DisplayString
_FalconKeypadCode12_Object = MibScalar
falconKeypadCode12 = _FalconKeypadCode12_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 23),
    _FalconKeypadCode12_Type()
)
falconKeypadCode12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode12.setStatus("mandatory")
_FalconKeypadName12_Type = DisplayString
_FalconKeypadName12_Object = MibScalar
falconKeypadName12 = _FalconKeypadName12_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 24),
    _FalconKeypadName12_Type()
)
falconKeypadName12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName12.setStatus("mandatory")
_FalconKeypadCode13_Type = DisplayString
_FalconKeypadCode13_Object = MibScalar
falconKeypadCode13 = _FalconKeypadCode13_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 25),
    _FalconKeypadCode13_Type()
)
falconKeypadCode13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode13.setStatus("mandatory")
_FalconKeypadName13_Type = DisplayString
_FalconKeypadName13_Object = MibScalar
falconKeypadName13 = _FalconKeypadName13_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 26),
    _FalconKeypadName13_Type()
)
falconKeypadName13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName13.setStatus("mandatory")
_FalconKeypadCode14_Type = DisplayString
_FalconKeypadCode14_Object = MibScalar
falconKeypadCode14 = _FalconKeypadCode14_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 27),
    _FalconKeypadCode14_Type()
)
falconKeypadCode14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode14.setStatus("mandatory")
_FalconKeypadName14_Type = DisplayString
_FalconKeypadName14_Object = MibScalar
falconKeypadName14 = _FalconKeypadName14_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 28),
    _FalconKeypadName14_Type()
)
falconKeypadName14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName14.setStatus("mandatory")
_FalconKeypadCode15_Type = DisplayString
_FalconKeypadCode15_Object = MibScalar
falconKeypadCode15 = _FalconKeypadCode15_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 29),
    _FalconKeypadCode15_Type()
)
falconKeypadCode15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode15.setStatus("mandatory")
_FalconKeypadName15_Type = DisplayString
_FalconKeypadName15_Object = MibScalar
falconKeypadName15 = _FalconKeypadName15_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 30),
    _FalconKeypadName15_Type()
)
falconKeypadName15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName15.setStatus("mandatory")
_FalconKeypadCode16_Type = DisplayString
_FalconKeypadCode16_Object = MibScalar
falconKeypadCode16 = _FalconKeypadCode16_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 31),
    _FalconKeypadCode16_Type()
)
falconKeypadCode16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode16.setStatus("mandatory")
_FalconKeypadName16_Type = DisplayString
_FalconKeypadName16_Object = MibScalar
falconKeypadName16 = _FalconKeypadName16_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 32),
    _FalconKeypadName16_Type()
)
falconKeypadName16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName16.setStatus("mandatory")
_FalconKeypadCode17_Type = DisplayString
_FalconKeypadCode17_Object = MibScalar
falconKeypadCode17 = _FalconKeypadCode17_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 33),
    _FalconKeypadCode17_Type()
)
falconKeypadCode17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode17.setStatus("mandatory")
_FalconKeypadName17_Type = DisplayString
_FalconKeypadName17_Object = MibScalar
falconKeypadName17 = _FalconKeypadName17_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 34),
    _FalconKeypadName17_Type()
)
falconKeypadName17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName17.setStatus("mandatory")
_FalconKeypadCode18_Type = DisplayString
_FalconKeypadCode18_Object = MibScalar
falconKeypadCode18 = _FalconKeypadCode18_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 35),
    _FalconKeypadCode18_Type()
)
falconKeypadCode18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode18.setStatus("mandatory")
_FalconKeypadName18_Type = DisplayString
_FalconKeypadName18_Object = MibScalar
falconKeypadName18 = _FalconKeypadName18_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 36),
    _FalconKeypadName18_Type()
)
falconKeypadName18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName18.setStatus("mandatory")
_FalconKeypadCode19_Type = DisplayString
_FalconKeypadCode19_Object = MibScalar
falconKeypadCode19 = _FalconKeypadCode19_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 37),
    _FalconKeypadCode19_Type()
)
falconKeypadCode19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode19.setStatus("mandatory")
_FalconKeypadName19_Type = DisplayString
_FalconKeypadName19_Object = MibScalar
falconKeypadName19 = _FalconKeypadName19_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 38),
    _FalconKeypadName19_Type()
)
falconKeypadName19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName19.setStatus("mandatory")
_FalconKeypadCode20_Type = DisplayString
_FalconKeypadCode20_Object = MibScalar
falconKeypadCode20 = _FalconKeypadCode20_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 39),
    _FalconKeypadCode20_Type()
)
falconKeypadCode20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadCode20.setStatus("mandatory")
_FalconKeypadName20_Type = DisplayString
_FalconKeypadName20_Object = MibScalar
falconKeypadName20 = _FalconKeypadName20_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 3, 40),
    _FalconKeypadName20_Type()
)
falconKeypadName20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconKeypadName20.setStatus("mandatory")


class _FalconInputVoltage_Type(Integer32):
    """Custom type falconInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInputVoltage_Type.__name__ = "Integer32"
_FalconInputVoltage_Object = MibScalar
falconInputVoltage = _FalconInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 4),
    _FalconInputVoltage_Type()
)
falconInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInputVoltage.setStatus("mandatory")


class _FalconOnBattery_Type(Integer32):
    """Custom type falconOnBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 0))
    )


_FalconOnBattery_Type.__name__ = "Integer32"
_FalconOnBattery_Object = MibScalar
falconOnBattery = _FalconOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 5),
    _FalconOnBattery_Type()
)
falconOnBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconOnBattery.setStatus("mandatory")


class _FalconLowBatteryThreshold_Type(Integer32):
    """Custom type falconLowBatteryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconLowBatteryThreshold_Type.__name__ = "Integer32"
_FalconLowBatteryThreshold_Object = MibScalar
falconLowBatteryThreshold = _FalconLowBatteryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 6),
    _FalconLowBatteryThreshold_Type()
)
falconLowBatteryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconLowBatteryThreshold.setStatus("mandatory")


class _FalconAnalogAverage_Type(Integer32):
    """Custom type falconAnalogAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_FalconAnalogAverage_Type.__name__ = "Integer32"
_FalconAnalogAverage_Object = MibScalar
falconAnalogAverage = _FalconAnalogAverage_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 2, 7),
    _FalconAnalogAverage_Type()
)
falconAnalogAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconAnalogAverage.setStatus("mandatory")
_FalconInputs_ObjectIdentity = ObjectIdentity
falconInputs = _FalconInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3)
)
_FalconInput1_ObjectIdentity = ObjectIdentity
falconInput1 = _FalconInput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1)
)


class _FalconInput1State_Type(Integer32):
    """Custom type falconInput1State based on Integer32"""
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
        *(("analog-4to20-installed", 2),
          ("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notinstalled", 1))
    )


_FalconInput1State_Type.__name__ = "Integer32"
_FalconInput1State_Object = MibScalar
falconInput1State = _FalconInput1State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 1),
    _FalconInput1State_Type()
)
falconInput1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1State.setStatus("mandatory")


class _FalconInput1Reading_Type(Integer32):
    """Custom type falconInput1Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput1Reading_Type.__name__ = "Integer32"
_FalconInput1Reading_Object = MibScalar
falconInput1Reading = _FalconInput1Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 2),
    _FalconInput1Reading_Type()
)
falconInput1Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput1Reading.setStatus("mandatory")


class _FalconInput1Gain_Type(Integer32):
    """Custom type falconInput1Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput1Gain_Type.__name__ = "Integer32"
_FalconInput1Gain_Object = MibScalar
falconInput1Gain = _FalconInput1Gain_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 3),
    _FalconInput1Gain_Type()
)
falconInput1Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1Gain.setStatus("mandatory")


class _FalconInput1Offset_Type(Integer32):
    """Custom type falconInput1Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput1Offset_Type.__name__ = "Integer32"
_FalconInput1Offset_Object = MibScalar
falconInput1Offset = _FalconInput1Offset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 4),
    _FalconInput1Offset_Type()
)
falconInput1Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1Offset.setStatus("mandatory")
_FalconInput1Label_Type = DisplayString
_FalconInput1Label_Object = MibScalar
falconInput1Label = _FalconInput1Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 5),
    _FalconInput1Label_Type()
)
falconInput1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1Label.setStatus("mandatory")
_FalconInput1UOM_Type = DisplayString
_FalconInput1UOM_Object = MibScalar
falconInput1UOM = _FalconInput1UOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 6),
    _FalconInput1UOM_Type()
)
falconInput1UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1UOM.setStatus("mandatory")


class _FalconInput1HighLimit2_Type(Integer32):
    """Custom type falconInput1HighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput1HighLimit2_Type.__name__ = "Integer32"
_FalconInput1HighLimit2_Object = MibScalar
falconInput1HighLimit2 = _FalconInput1HighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 7),
    _FalconInput1HighLimit2_Type()
)
falconInput1HighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1HighLimit2.setStatus("mandatory")


class _FalconInput1HighLimit_Type(Integer32):
    """Custom type falconInput1HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput1HighLimit_Type.__name__ = "Integer32"
_FalconInput1HighLimit_Object = MibScalar
falconInput1HighLimit = _FalconInput1HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 8),
    _FalconInput1HighLimit_Type()
)
falconInput1HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1HighLimit.setStatus("mandatory")


class _FalconInput1LowLimit_Type(Integer32):
    """Custom type falconInput1LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput1LowLimit_Type.__name__ = "Integer32"
_FalconInput1LowLimit_Object = MibScalar
falconInput1LowLimit = _FalconInput1LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 9),
    _FalconInput1LowLimit_Type()
)
falconInput1LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1LowLimit.setStatus("mandatory")


class _FalconInput1LowLimit2_Type(Integer32):
    """Custom type falconInput1LowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput1LowLimit2_Type.__name__ = "Integer32"
_FalconInput1LowLimit2_Object = MibScalar
falconInput1LowLimit2 = _FalconInput1LowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 10),
    _FalconInput1LowLimit2_Type()
)
falconInput1LowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1LowLimit2.setStatus("mandatory")


class _FalconInput1RlyControl_Type(Integer32):
    """Custom type falconInput1RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput1RlyControl_Type.__name__ = "Integer32"
_FalconInput1RlyControl_Object = MibScalar
falconInput1RlyControl = _FalconInput1RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 11),
    _FalconInput1RlyControl_Type()
)
falconInput1RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1RlyControl.setStatus("mandatory")


class _FalconInput1Delay_Type(Integer32):
    """Custom type falconInput1Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput1Delay_Type.__name__ = "Integer32"
_FalconInput1Delay_Object = MibScalar
falconInput1Delay = _FalconInput1Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 12),
    _FalconInput1Delay_Type()
)
falconInput1Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1Delay.setStatus("mandatory")


class _FalconInput1Hysteresis_Type(Integer32):
    """Custom type falconInput1Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconInput1Hysteresis_Type.__name__ = "Integer32"
_FalconInput1Hysteresis_Object = MibScalar
falconInput1Hysteresis = _FalconInput1Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 1, 13),
    _FalconInput1Hysteresis_Type()
)
falconInput1Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput1Hysteresis.setStatus("mandatory")
_FalconInput2_ObjectIdentity = ObjectIdentity
falconInput2 = _FalconInput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2)
)


class _FalconInput2State_Type(Integer32):
    """Custom type falconInput2State based on Integer32"""
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
        *(("analog-4to20-installed", 2),
          ("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notinstalled", 1))
    )


_FalconInput2State_Type.__name__ = "Integer32"
_FalconInput2State_Object = MibScalar
falconInput2State = _FalconInput2State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 1),
    _FalconInput2State_Type()
)
falconInput2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2State.setStatus("mandatory")


class _FalconInput2Reading_Type(Integer32):
    """Custom type falconInput2Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput2Reading_Type.__name__ = "Integer32"
_FalconInput2Reading_Object = MibScalar
falconInput2Reading = _FalconInput2Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 2),
    _FalconInput2Reading_Type()
)
falconInput2Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput2Reading.setStatus("mandatory")


class _FalconInput2Gain_Type(Integer32):
    """Custom type falconInput2Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput2Gain_Type.__name__ = "Integer32"
_FalconInput2Gain_Object = MibScalar
falconInput2Gain = _FalconInput2Gain_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 3),
    _FalconInput2Gain_Type()
)
falconInput2Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2Gain.setStatus("mandatory")


class _FalconInput2Offset_Type(Integer32):
    """Custom type falconInput2Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput2Offset_Type.__name__ = "Integer32"
_FalconInput2Offset_Object = MibScalar
falconInput2Offset = _FalconInput2Offset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 4),
    _FalconInput2Offset_Type()
)
falconInput2Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2Offset.setStatus("mandatory")
_FalconInput2Label_Type = DisplayString
_FalconInput2Label_Object = MibScalar
falconInput2Label = _FalconInput2Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 5),
    _FalconInput2Label_Type()
)
falconInput2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2Label.setStatus("mandatory")
_FalconInput2UOM_Type = DisplayString
_FalconInput2UOM_Object = MibScalar
falconInput2UOM = _FalconInput2UOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 6),
    _FalconInput2UOM_Type()
)
falconInput2UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2UOM.setStatus("mandatory")


class _FalconInput2HighLimit2_Type(Integer32):
    """Custom type falconInput2HighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput2HighLimit2_Type.__name__ = "Integer32"
_FalconInput2HighLimit2_Object = MibScalar
falconInput2HighLimit2 = _FalconInput2HighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 7),
    _FalconInput2HighLimit2_Type()
)
falconInput2HighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2HighLimit2.setStatus("mandatory")


class _FalconInput2HighLimit_Type(Integer32):
    """Custom type falconInput2HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput2HighLimit_Type.__name__ = "Integer32"
_FalconInput2HighLimit_Object = MibScalar
falconInput2HighLimit = _FalconInput2HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 8),
    _FalconInput2HighLimit_Type()
)
falconInput2HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2HighLimit.setStatus("mandatory")


class _FalconInput2LowLimit_Type(Integer32):
    """Custom type falconInput2LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput2LowLimit_Type.__name__ = "Integer32"
_FalconInput2LowLimit_Object = MibScalar
falconInput2LowLimit = _FalconInput2LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 9),
    _FalconInput2LowLimit_Type()
)
falconInput2LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2LowLimit.setStatus("mandatory")


class _FalconInput2LowLimit2_Type(Integer32):
    """Custom type falconInput2LowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput2LowLimit2_Type.__name__ = "Integer32"
_FalconInput2LowLimit2_Object = MibScalar
falconInput2LowLimit2 = _FalconInput2LowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 10),
    _FalconInput2LowLimit2_Type()
)
falconInput2LowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2LowLimit2.setStatus("mandatory")


class _FalconInput2RlyControl_Type(Integer32):
    """Custom type falconInput2RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput2RlyControl_Type.__name__ = "Integer32"
_FalconInput2RlyControl_Object = MibScalar
falconInput2RlyControl = _FalconInput2RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 11),
    _FalconInput2RlyControl_Type()
)
falconInput2RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2RlyControl.setStatus("mandatory")


class _FalconInput2Delay_Type(Integer32):
    """Custom type falconInput2Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput2Delay_Type.__name__ = "Integer32"
_FalconInput2Delay_Object = MibScalar
falconInput2Delay = _FalconInput2Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 12),
    _FalconInput2Delay_Type()
)
falconInput2Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2Delay.setStatus("mandatory")


class _FalconInput2Hysteresis_Type(Integer32):
    """Custom type falconInput2Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconInput2Hysteresis_Type.__name__ = "Integer32"
_FalconInput2Hysteresis_Object = MibScalar
falconInput2Hysteresis = _FalconInput2Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 2, 13),
    _FalconInput2Hysteresis_Type()
)
falconInput2Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput2Hysteresis.setStatus("mandatory")
_FalconInput3_ObjectIdentity = ObjectIdentity
falconInput3 = _FalconInput3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3)
)


class _FalconInput3State_Type(Integer32):
    """Custom type falconInput3State based on Integer32"""
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
        *(("analog-4to20-installed", 2),
          ("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput3State_Type.__name__ = "Integer32"
_FalconInput3State_Object = MibScalar
falconInput3State = _FalconInput3State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 1),
    _FalconInput3State_Type()
)
falconInput3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3State.setStatus("mandatory")


class _FalconInput3Reading_Type(Integer32):
    """Custom type falconInput3Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput3Reading_Type.__name__ = "Integer32"
_FalconInput3Reading_Object = MibScalar
falconInput3Reading = _FalconInput3Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 2),
    _FalconInput3Reading_Type()
)
falconInput3Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput3Reading.setStatus("mandatory")


class _FalconInput3Gain_Type(Integer32):
    """Custom type falconInput3Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput3Gain_Type.__name__ = "Integer32"
_FalconInput3Gain_Object = MibScalar
falconInput3Gain = _FalconInput3Gain_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 3),
    _FalconInput3Gain_Type()
)
falconInput3Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3Gain.setStatus("mandatory")


class _FalconInput3Offset_Type(Integer32):
    """Custom type falconInput3Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput3Offset_Type.__name__ = "Integer32"
_FalconInput3Offset_Object = MibScalar
falconInput3Offset = _FalconInput3Offset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 4),
    _FalconInput3Offset_Type()
)
falconInput3Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3Offset.setStatus("mandatory")
_FalconInput3Label_Type = DisplayString
_FalconInput3Label_Object = MibScalar
falconInput3Label = _FalconInput3Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 5),
    _FalconInput3Label_Type()
)
falconInput3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3Label.setStatus("mandatory")
_FalconInput3UOM_Type = DisplayString
_FalconInput3UOM_Object = MibScalar
falconInput3UOM = _FalconInput3UOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 6),
    _FalconInput3UOM_Type()
)
falconInput3UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3UOM.setStatus("mandatory")


class _FalconInput3HighLimit2_Type(Integer32):
    """Custom type falconInput3HighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput3HighLimit2_Type.__name__ = "Integer32"
_FalconInput3HighLimit2_Object = MibScalar
falconInput3HighLimit2 = _FalconInput3HighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 7),
    _FalconInput3HighLimit2_Type()
)
falconInput3HighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3HighLimit2.setStatus("mandatory")


class _FalconInput3HighLimit_Type(Integer32):
    """Custom type falconInput3HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput3HighLimit_Type.__name__ = "Integer32"
_FalconInput3HighLimit_Object = MibScalar
falconInput3HighLimit = _FalconInput3HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 8),
    _FalconInput3HighLimit_Type()
)
falconInput3HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3HighLimit.setStatus("mandatory")


class _FalconInput3LowLimit_Type(Integer32):
    """Custom type falconInput3LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput3LowLimit_Type.__name__ = "Integer32"
_FalconInput3LowLimit_Object = MibScalar
falconInput3LowLimit = _FalconInput3LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 9),
    _FalconInput3LowLimit_Type()
)
falconInput3LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3LowLimit.setStatus("mandatory")


class _FalconInput3LowLimit2_Type(Integer32):
    """Custom type falconInput3LowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput3LowLimit2_Type.__name__ = "Integer32"
_FalconInput3LowLimit2_Object = MibScalar
falconInput3LowLimit2 = _FalconInput3LowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 10),
    _FalconInput3LowLimit2_Type()
)
falconInput3LowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3LowLimit2.setStatus("mandatory")


class _FalconInput3RlyControl_Type(Integer32):
    """Custom type falconInput3RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput3RlyControl_Type.__name__ = "Integer32"
_FalconInput3RlyControl_Object = MibScalar
falconInput3RlyControl = _FalconInput3RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 11),
    _FalconInput3RlyControl_Type()
)
falconInput3RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3RlyControl.setStatus("mandatory")


class _FalconInput3Delay_Type(Integer32):
    """Custom type falconInput3Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput3Delay_Type.__name__ = "Integer32"
_FalconInput3Delay_Object = MibScalar
falconInput3Delay = _FalconInput3Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 12),
    _FalconInput3Delay_Type()
)
falconInput3Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3Delay.setStatus("mandatory")


class _FalconInput3Hysteresis_Type(Integer32):
    """Custom type falconInput3Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconInput3Hysteresis_Type.__name__ = "Integer32"
_FalconInput3Hysteresis_Object = MibScalar
falconInput3Hysteresis = _FalconInput3Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 3, 13),
    _FalconInput3Hysteresis_Type()
)
falconInput3Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput3Hysteresis.setStatus("mandatory")
_FalconInput4_ObjectIdentity = ObjectIdentity
falconInput4 = _FalconInput4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4)
)


class _FalconInput4State_Type(Integer32):
    """Custom type falconInput4State based on Integer32"""
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
        *(("analog-4to20-installed", 2),
          ("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput4State_Type.__name__ = "Integer32"
_FalconInput4State_Object = MibScalar
falconInput4State = _FalconInput4State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 1),
    _FalconInput4State_Type()
)
falconInput4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4State.setStatus("mandatory")


class _FalconInput4Reading_Type(Integer32):
    """Custom type falconInput4Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput4Reading_Type.__name__ = "Integer32"
_FalconInput4Reading_Object = MibScalar
falconInput4Reading = _FalconInput4Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 2),
    _FalconInput4Reading_Type()
)
falconInput4Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput4Reading.setStatus("mandatory")


class _FalconInput4Gain_Type(Integer32):
    """Custom type falconInput4Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput4Gain_Type.__name__ = "Integer32"
_FalconInput4Gain_Object = MibScalar
falconInput4Gain = _FalconInput4Gain_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 3),
    _FalconInput4Gain_Type()
)
falconInput4Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4Gain.setStatus("mandatory")


class _FalconInput4Offset_Type(Integer32):
    """Custom type falconInput4Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput4Offset_Type.__name__ = "Integer32"
_FalconInput4Offset_Object = MibScalar
falconInput4Offset = _FalconInput4Offset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 4),
    _FalconInput4Offset_Type()
)
falconInput4Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4Offset.setStatus("mandatory")
_FalconInput4Label_Type = DisplayString
_FalconInput4Label_Object = MibScalar
falconInput4Label = _FalconInput4Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 5),
    _FalconInput4Label_Type()
)
falconInput4Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4Label.setStatus("mandatory")
_FalconInput4UOM_Type = DisplayString
_FalconInput4UOM_Object = MibScalar
falconInput4UOM = _FalconInput4UOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 6),
    _FalconInput4UOM_Type()
)
falconInput4UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4UOM.setStatus("mandatory")


class _FalconInput4HighLimit2_Type(Integer32):
    """Custom type falconInput4HighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput4HighLimit2_Type.__name__ = "Integer32"
_FalconInput4HighLimit2_Object = MibScalar
falconInput4HighLimit2 = _FalconInput4HighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 7),
    _FalconInput4HighLimit2_Type()
)
falconInput4HighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4HighLimit2.setStatus("mandatory")


class _FalconInput4HighLimit_Type(Integer32):
    """Custom type falconInput4HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput4HighLimit_Type.__name__ = "Integer32"
_FalconInput4HighLimit_Object = MibScalar
falconInput4HighLimit = _FalconInput4HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 8),
    _FalconInput4HighLimit_Type()
)
falconInput4HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4HighLimit.setStatus("mandatory")


class _FalconInput4LowLimit_Type(Integer32):
    """Custom type falconInput4LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput4LowLimit_Type.__name__ = "Integer32"
_FalconInput4LowLimit_Object = MibScalar
falconInput4LowLimit = _FalconInput4LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 9),
    _FalconInput4LowLimit_Type()
)
falconInput4LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4LowLimit.setStatus("mandatory")


class _FalconInput4LowLimit2_Type(Integer32):
    """Custom type falconInput4LowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput4LowLimit2_Type.__name__ = "Integer32"
_FalconInput4LowLimit2_Object = MibScalar
falconInput4LowLimit2 = _FalconInput4LowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 10),
    _FalconInput4LowLimit2_Type()
)
falconInput4LowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4LowLimit2.setStatus("mandatory")


class _FalconInput4RlyControl_Type(Integer32):
    """Custom type falconInput4RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput4RlyControl_Type.__name__ = "Integer32"
_FalconInput4RlyControl_Object = MibScalar
falconInput4RlyControl = _FalconInput4RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 11),
    _FalconInput4RlyControl_Type()
)
falconInput4RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4RlyControl.setStatus("mandatory")


class _FalconInput4Delay_Type(Integer32):
    """Custom type falconInput4Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput4Delay_Type.__name__ = "Integer32"
_FalconInput4Delay_Object = MibScalar
falconInput4Delay = _FalconInput4Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 12),
    _FalconInput4Delay_Type()
)
falconInput4Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4Delay.setStatus("mandatory")


class _FalconInput4Hysteresis_Type(Integer32):
    """Custom type falconInput4Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconInput4Hysteresis_Type.__name__ = "Integer32"
_FalconInput4Hysteresis_Object = MibScalar
falconInput4Hysteresis = _FalconInput4Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 4, 13),
    _FalconInput4Hysteresis_Type()
)
falconInput4Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput4Hysteresis.setStatus("mandatory")
_FalconInput5_ObjectIdentity = ObjectIdentity
falconInput5 = _FalconInput5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5)
)


class _FalconInput5State_Type(Integer32):
    """Custom type falconInput5State based on Integer32"""
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
        *(("analog-4to20-installed", 2),
          ("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput5State_Type.__name__ = "Integer32"
_FalconInput5State_Object = MibScalar
falconInput5State = _FalconInput5State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 1),
    _FalconInput5State_Type()
)
falconInput5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5State.setStatus("mandatory")


class _FalconInput5Reading_Type(Integer32):
    """Custom type falconInput5Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput5Reading_Type.__name__ = "Integer32"
_FalconInput5Reading_Object = MibScalar
falconInput5Reading = _FalconInput5Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 2),
    _FalconInput5Reading_Type()
)
falconInput5Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput5Reading.setStatus("mandatory")


class _FalconInput5Gain_Type(Integer32):
    """Custom type falconInput5Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput5Gain_Type.__name__ = "Integer32"
_FalconInput5Gain_Object = MibScalar
falconInput5Gain = _FalconInput5Gain_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 3),
    _FalconInput5Gain_Type()
)
falconInput5Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5Gain.setStatus("mandatory")


class _FalconInput5Offset_Type(Integer32):
    """Custom type falconInput5Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput5Offset_Type.__name__ = "Integer32"
_FalconInput5Offset_Object = MibScalar
falconInput5Offset = _FalconInput5Offset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 4),
    _FalconInput5Offset_Type()
)
falconInput5Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5Offset.setStatus("mandatory")
_FalconInput5Label_Type = DisplayString
_FalconInput5Label_Object = MibScalar
falconInput5Label = _FalconInput5Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 5),
    _FalconInput5Label_Type()
)
falconInput5Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5Label.setStatus("mandatory")
_FalconInput5UOM_Type = DisplayString
_FalconInput5UOM_Object = MibScalar
falconInput5UOM = _FalconInput5UOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 6),
    _FalconInput5UOM_Type()
)
falconInput5UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5UOM.setStatus("mandatory")


class _FalconInput5HighLimit2_Type(Integer32):
    """Custom type falconInput5HighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput5HighLimit2_Type.__name__ = "Integer32"
_FalconInput5HighLimit2_Object = MibScalar
falconInput5HighLimit2 = _FalconInput5HighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 7),
    _FalconInput5HighLimit2_Type()
)
falconInput5HighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5HighLimit2.setStatus("mandatory")


class _FalconInput5HighLimit_Type(Integer32):
    """Custom type falconInput5HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput5HighLimit_Type.__name__ = "Integer32"
_FalconInput5HighLimit_Object = MibScalar
falconInput5HighLimit = _FalconInput5HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 8),
    _FalconInput5HighLimit_Type()
)
falconInput5HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5HighLimit.setStatus("mandatory")


class _FalconInput5LowLimit_Type(Integer32):
    """Custom type falconInput5LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput5LowLimit_Type.__name__ = "Integer32"
_FalconInput5LowLimit_Object = MibScalar
falconInput5LowLimit = _FalconInput5LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 9),
    _FalconInput5LowLimit_Type()
)
falconInput5LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5LowLimit.setStatus("mandatory")


class _FalconInput5LowLimit2_Type(Integer32):
    """Custom type falconInput5LowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput5LowLimit2_Type.__name__ = "Integer32"
_FalconInput5LowLimit2_Object = MibScalar
falconInput5LowLimit2 = _FalconInput5LowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 10),
    _FalconInput5LowLimit2_Type()
)
falconInput5LowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5LowLimit2.setStatus("mandatory")


class _FalconInput5RlyControl_Type(Integer32):
    """Custom type falconInput5RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput5RlyControl_Type.__name__ = "Integer32"
_FalconInput5RlyControl_Object = MibScalar
falconInput5RlyControl = _FalconInput5RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 11),
    _FalconInput5RlyControl_Type()
)
falconInput5RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5RlyControl.setStatus("mandatory")


class _FalconInput5Delay_Type(Integer32):
    """Custom type falconInput5Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput5Delay_Type.__name__ = "Integer32"
_FalconInput5Delay_Object = MibScalar
falconInput5Delay = _FalconInput5Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 12),
    _FalconInput5Delay_Type()
)
falconInput5Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5Delay.setStatus("mandatory")


class _FalconInput5Hysteresis_Type(Integer32):
    """Custom type falconInput5Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconInput5Hysteresis_Type.__name__ = "Integer32"
_FalconInput5Hysteresis_Object = MibScalar
falconInput5Hysteresis = _FalconInput5Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 5, 13),
    _FalconInput5Hysteresis_Type()
)
falconInput5Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput5Hysteresis.setStatus("mandatory")
_FalconInput6_ObjectIdentity = ObjectIdentity
falconInput6 = _FalconInput6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6)
)


class _FalconInput6State_Type(Integer32):
    """Custom type falconInput6State based on Integer32"""
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
        *(("analog-4to20-installed", 2),
          ("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput6State_Type.__name__ = "Integer32"
_FalconInput6State_Object = MibScalar
falconInput6State = _FalconInput6State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 1),
    _FalconInput6State_Type()
)
falconInput6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6State.setStatus("mandatory")


class _FalconInput6Reading_Type(Integer32):
    """Custom type falconInput6Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput6Reading_Type.__name__ = "Integer32"
_FalconInput6Reading_Object = MibScalar
falconInput6Reading = _FalconInput6Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 2),
    _FalconInput6Reading_Type()
)
falconInput6Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput6Reading.setStatus("mandatory")


class _FalconInput6Gain_Type(Integer32):
    """Custom type falconInput6Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput6Gain_Type.__name__ = "Integer32"
_FalconInput6Gain_Object = MibScalar
falconInput6Gain = _FalconInput6Gain_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 3),
    _FalconInput6Gain_Type()
)
falconInput6Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6Gain.setStatus("mandatory")


class _FalconInput6Offset_Type(Integer32):
    """Custom type falconInput6Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput6Offset_Type.__name__ = "Integer32"
_FalconInput6Offset_Object = MibScalar
falconInput6Offset = _FalconInput6Offset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 4),
    _FalconInput6Offset_Type()
)
falconInput6Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6Offset.setStatus("mandatory")
_FalconInput6Label_Type = DisplayString
_FalconInput6Label_Object = MibScalar
falconInput6Label = _FalconInput6Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 5),
    _FalconInput6Label_Type()
)
falconInput6Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6Label.setStatus("mandatory")
_FalconInput6UOM_Type = DisplayString
_FalconInput6UOM_Object = MibScalar
falconInput6UOM = _FalconInput6UOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 6),
    _FalconInput6UOM_Type()
)
falconInput6UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6UOM.setStatus("mandatory")


class _FalconInput6HighLimit2_Type(Integer32):
    """Custom type falconInput6HighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput6HighLimit2_Type.__name__ = "Integer32"
_FalconInput6HighLimit2_Object = MibScalar
falconInput6HighLimit2 = _FalconInput6HighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 7),
    _FalconInput6HighLimit2_Type()
)
falconInput6HighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6HighLimit2.setStatus("mandatory")


class _FalconInput6HighLimit_Type(Integer32):
    """Custom type falconInput6HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput6HighLimit_Type.__name__ = "Integer32"
_FalconInput6HighLimit_Object = MibScalar
falconInput6HighLimit = _FalconInput6HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 8),
    _FalconInput6HighLimit_Type()
)
falconInput6HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6HighLimit.setStatus("mandatory")


class _FalconInput6LowLimit_Type(Integer32):
    """Custom type falconInput6LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput6LowLimit_Type.__name__ = "Integer32"
_FalconInput6LowLimit_Object = MibScalar
falconInput6LowLimit = _FalconInput6LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 9),
    _FalconInput6LowLimit_Type()
)
falconInput6LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6LowLimit.setStatus("mandatory")


class _FalconInput6LowLimit2_Type(Integer32):
    """Custom type falconInput6LowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput6LowLimit2_Type.__name__ = "Integer32"
_FalconInput6LowLimit2_Object = MibScalar
falconInput6LowLimit2 = _FalconInput6LowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 10),
    _FalconInput6LowLimit2_Type()
)
falconInput6LowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6LowLimit2.setStatus("mandatory")


class _FalconInput6RlyControl_Type(Integer32):
    """Custom type falconInput6RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput6RlyControl_Type.__name__ = "Integer32"
_FalconInput6RlyControl_Object = MibScalar
falconInput6RlyControl = _FalconInput6RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 11),
    _FalconInput6RlyControl_Type()
)
falconInput6RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6RlyControl.setStatus("mandatory")


class _FalconInput6Delay_Type(Integer32):
    """Custom type falconInput6Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput6Delay_Type.__name__ = "Integer32"
_FalconInput6Delay_Object = MibScalar
falconInput6Delay = _FalconInput6Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 12),
    _FalconInput6Delay_Type()
)
falconInput6Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6Delay.setStatus("mandatory")


class _FalconInput6Hysteresis_Type(Integer32):
    """Custom type falconInput6Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconInput6Hysteresis_Type.__name__ = "Integer32"
_FalconInput6Hysteresis_Object = MibScalar
falconInput6Hysteresis = _FalconInput6Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 6, 13),
    _FalconInput6Hysteresis_Type()
)
falconInput6Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput6Hysteresis.setStatus("mandatory")
_FalconInput7_ObjectIdentity = ObjectIdentity
falconInput7 = _FalconInput7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7)
)


class _FalconInput7State_Type(Integer32):
    """Custom type falconInput7State based on Integer32"""
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
        *(("analog-4to20-installed", 2),
          ("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput7State_Type.__name__ = "Integer32"
_FalconInput7State_Object = MibScalar
falconInput7State = _FalconInput7State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 1),
    _FalconInput7State_Type()
)
falconInput7State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7State.setStatus("mandatory")


class _FalconInput7Reading_Type(Integer32):
    """Custom type falconInput7Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput7Reading_Type.__name__ = "Integer32"
_FalconInput7Reading_Object = MibScalar
falconInput7Reading = _FalconInput7Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 2),
    _FalconInput7Reading_Type()
)
falconInput7Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput7Reading.setStatus("mandatory")


class _FalconInput7Gain_Type(Integer32):
    """Custom type falconInput7Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput7Gain_Type.__name__ = "Integer32"
_FalconInput7Gain_Object = MibScalar
falconInput7Gain = _FalconInput7Gain_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 3),
    _FalconInput7Gain_Type()
)
falconInput7Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7Gain.setStatus("mandatory")


class _FalconInput7Offset_Type(Integer32):
    """Custom type falconInput7Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput7Offset_Type.__name__ = "Integer32"
_FalconInput7Offset_Object = MibScalar
falconInput7Offset = _FalconInput7Offset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 4),
    _FalconInput7Offset_Type()
)
falconInput7Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7Offset.setStatus("mandatory")
_FalconInput7Label_Type = DisplayString
_FalconInput7Label_Object = MibScalar
falconInput7Label = _FalconInput7Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 5),
    _FalconInput7Label_Type()
)
falconInput7Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7Label.setStatus("mandatory")
_FalconInput7UOM_Type = DisplayString
_FalconInput7UOM_Object = MibScalar
falconInput7UOM = _FalconInput7UOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 6),
    _FalconInput7UOM_Type()
)
falconInput7UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7UOM.setStatus("mandatory")


class _FalconInput7HighLimit2_Type(Integer32):
    """Custom type falconInput7HighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput7HighLimit2_Type.__name__ = "Integer32"
_FalconInput7HighLimit2_Object = MibScalar
falconInput7HighLimit2 = _FalconInput7HighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 7),
    _FalconInput7HighLimit2_Type()
)
falconInput7HighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7HighLimit2.setStatus("mandatory")


class _FalconInput7HighLimit_Type(Integer32):
    """Custom type falconInput7HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput7HighLimit_Type.__name__ = "Integer32"
_FalconInput7HighLimit_Object = MibScalar
falconInput7HighLimit = _FalconInput7HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 8),
    _FalconInput7HighLimit_Type()
)
falconInput7HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7HighLimit.setStatus("mandatory")


class _FalconInput7LowLimit_Type(Integer32):
    """Custom type falconInput7LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput7LowLimit_Type.__name__ = "Integer32"
_FalconInput7LowLimit_Object = MibScalar
falconInput7LowLimit = _FalconInput7LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 9),
    _FalconInput7LowLimit_Type()
)
falconInput7LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7LowLimit.setStatus("mandatory")


class _FalconInput7LowLimit2_Type(Integer32):
    """Custom type falconInput7LowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput7LowLimit2_Type.__name__ = "Integer32"
_FalconInput7LowLimit2_Object = MibScalar
falconInput7LowLimit2 = _FalconInput7LowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 10),
    _FalconInput7LowLimit2_Type()
)
falconInput7LowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7LowLimit2.setStatus("mandatory")


class _FalconInput7RlyControl_Type(Integer32):
    """Custom type falconInput7RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput7RlyControl_Type.__name__ = "Integer32"
_FalconInput7RlyControl_Object = MibScalar
falconInput7RlyControl = _FalconInput7RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 11),
    _FalconInput7RlyControl_Type()
)
falconInput7RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7RlyControl.setStatus("mandatory")


class _FalconInput7Delay_Type(Integer32):
    """Custom type falconInput7Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput7Delay_Type.__name__ = "Integer32"
_FalconInput7Delay_Object = MibScalar
falconInput7Delay = _FalconInput7Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 12),
    _FalconInput7Delay_Type()
)
falconInput7Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7Delay.setStatus("mandatory")


class _FalconInput7Hysteresis_Type(Integer32):
    """Custom type falconInput7Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconInput7Hysteresis_Type.__name__ = "Integer32"
_FalconInput7Hysteresis_Object = MibScalar
falconInput7Hysteresis = _FalconInput7Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 7, 13),
    _FalconInput7Hysteresis_Type()
)
falconInput7Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput7Hysteresis.setStatus("mandatory")
_FalconInput8_ObjectIdentity = ObjectIdentity
falconInput8 = _FalconInput8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8)
)


class _FalconInput8State_Type(Integer32):
    """Custom type falconInput8State based on Integer32"""
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
        *(("analog-4to20-installed", 2),
          ("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput8State_Type.__name__ = "Integer32"
_FalconInput8State_Object = MibScalar
falconInput8State = _FalconInput8State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 1),
    _FalconInput8State_Type()
)
falconInput8State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8State.setStatus("mandatory")


class _FalconInput8Reading_Type(Integer32):
    """Custom type falconInput8Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput8Reading_Type.__name__ = "Integer32"
_FalconInput8Reading_Object = MibScalar
falconInput8Reading = _FalconInput8Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 2),
    _FalconInput8Reading_Type()
)
falconInput8Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput8Reading.setStatus("mandatory")


class _FalconInput8Gain_Type(Integer32):
    """Custom type falconInput8Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput8Gain_Type.__name__ = "Integer32"
_FalconInput8Gain_Object = MibScalar
falconInput8Gain = _FalconInput8Gain_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 3),
    _FalconInput8Gain_Type()
)
falconInput8Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8Gain.setStatus("mandatory")


class _FalconInput8Offset_Type(Integer32):
    """Custom type falconInput8Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput8Offset_Type.__name__ = "Integer32"
_FalconInput8Offset_Object = MibScalar
falconInput8Offset = _FalconInput8Offset_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 4),
    _FalconInput8Offset_Type()
)
falconInput8Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8Offset.setStatus("mandatory")
_FalconInput8Label_Type = DisplayString
_FalconInput8Label_Object = MibScalar
falconInput8Label = _FalconInput8Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 5),
    _FalconInput8Label_Type()
)
falconInput8Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8Label.setStatus("mandatory")
_FalconInput8UOM_Type = DisplayString
_FalconInput8UOM_Object = MibScalar
falconInput8UOM = _FalconInput8UOM_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 6),
    _FalconInput8UOM_Type()
)
falconInput8UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8UOM.setStatus("mandatory")


class _FalconInput8HighLimit2_Type(Integer32):
    """Custom type falconInput8HighLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput8HighLimit2_Type.__name__ = "Integer32"
_FalconInput8HighLimit2_Object = MibScalar
falconInput8HighLimit2 = _FalconInput8HighLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 7),
    _FalconInput8HighLimit2_Type()
)
falconInput8HighLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8HighLimit2.setStatus("mandatory")


class _FalconInput8HighLimit_Type(Integer32):
    """Custom type falconInput8HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput8HighLimit_Type.__name__ = "Integer32"
_FalconInput8HighLimit_Object = MibScalar
falconInput8HighLimit = _FalconInput8HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 8),
    _FalconInput8HighLimit_Type()
)
falconInput8HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8HighLimit.setStatus("mandatory")


class _FalconInput8LowLimit_Type(Integer32):
    """Custom type falconInput8LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput8LowLimit_Type.__name__ = "Integer32"
_FalconInput8LowLimit_Object = MibScalar
falconInput8LowLimit = _FalconInput8LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 9),
    _FalconInput8LowLimit_Type()
)
falconInput8LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8LowLimit.setStatus("mandatory")


class _FalconInput8RlyControl_Type(Integer32):
    """Custom type falconInput8RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput8RlyControl_Type.__name__ = "Integer32"
_FalconInput8RlyControl_Object = MibScalar
falconInput8RlyControl = _FalconInput8RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 9),
    _FalconInput8RlyControl_Type()
)
falconInput8RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8RlyControl.setStatus("mandatory")


class _FalconInput8LowLimit2_Type(Integer32):
    """Custom type falconInput8LowLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput8LowLimit2_Type.__name__ = "Integer32"
_FalconInput8LowLimit2_Object = MibScalar
falconInput8LowLimit2 = _FalconInput8LowLimit2_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 10),
    _FalconInput8LowLimit2_Type()
)
falconInput8LowLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8LowLimit2.setStatus("mandatory")


class _FalconInput8Delay_Type(Integer32):
    """Custom type falconInput8Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput8Delay_Type.__name__ = "Integer32"
_FalconInput8Delay_Object = MibScalar
falconInput8Delay = _FalconInput8Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 10),
    _FalconInput8Delay_Type()
)
falconInput8Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8Delay.setStatus("mandatory")


class _FalconInput8Hysteresis_Type(Integer32):
    """Custom type falconInput8Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconInput8Hysteresis_Type.__name__ = "Integer32"
_FalconInput8Hysteresis_Object = MibScalar
falconInput8Hysteresis = _FalconInput8Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 8, 11),
    _FalconInput8Hysteresis_Type()
)
falconInput8Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput8Hysteresis.setStatus("mandatory")
_FalconInput9_ObjectIdentity = ObjectIdentity
falconInput9 = _FalconInput9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 25)
)


class _FalconInput9State_Type(Integer32):
    """Custom type falconInput9State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput9State_Type.__name__ = "Integer32"
_FalconInput9State_Object = MibScalar
falconInput9State = _FalconInput9State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 25, 1),
    _FalconInput9State_Type()
)
falconInput9State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput9State.setStatus("mandatory")


class _FalconInput9Reading_Type(Integer32):
    """Custom type falconInput9Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput9Reading_Type.__name__ = "Integer32"
_FalconInput9Reading_Object = MibScalar
falconInput9Reading = _FalconInput9Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 25, 2),
    _FalconInput9Reading_Type()
)
falconInput9Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput9Reading.setStatus("mandatory")
_FalconInput9Label_Type = DisplayString
_FalconInput9Label_Object = MibScalar
falconInput9Label = _FalconInput9Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 25, 3),
    _FalconInput9Label_Type()
)
falconInput9Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput9Label.setStatus("mandatory")


class _FalconInput9RlyControl_Type(Integer32):
    """Custom type falconInput9RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput9RlyControl_Type.__name__ = "Integer32"
_FalconInput9RlyControl_Object = MibScalar
falconInput9RlyControl = _FalconInput9RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 25, 4),
    _FalconInput9RlyControl_Type()
)
falconInput9RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput9RlyControl.setStatus("mandatory")


class _FalconInput9Delay_Type(Integer32):
    """Custom type falconInput9Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput9Delay_Type.__name__ = "Integer32"
_FalconInput9Delay_Object = MibScalar
falconInput9Delay = _FalconInput9Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 25, 5),
    _FalconInput9Delay_Type()
)
falconInput9Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput9Delay.setStatus("mandatory")
_FalconInput10_ObjectIdentity = ObjectIdentity
falconInput10 = _FalconInput10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 26)
)


class _FalconInput10State_Type(Integer32):
    """Custom type falconInput10State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput10State_Type.__name__ = "Integer32"
_FalconInput10State_Object = MibScalar
falconInput10State = _FalconInput10State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 26, 1),
    _FalconInput10State_Type()
)
falconInput10State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput10State.setStatus("mandatory")


class _FalconInput10Reading_Type(Integer32):
    """Custom type falconInput10Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput10Reading_Type.__name__ = "Integer32"
_FalconInput10Reading_Object = MibScalar
falconInput10Reading = _FalconInput10Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 26, 2),
    _FalconInput10Reading_Type()
)
falconInput10Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput10Reading.setStatus("mandatory")
_FalconInput10Label_Type = DisplayString
_FalconInput10Label_Object = MibScalar
falconInput10Label = _FalconInput10Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 26, 3),
    _FalconInput10Label_Type()
)
falconInput10Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput10Label.setStatus("mandatory")


class _FalconInput10RlyControl_Type(Integer32):
    """Custom type falconInput10RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput10RlyControl_Type.__name__ = "Integer32"
_FalconInput10RlyControl_Object = MibScalar
falconInput10RlyControl = _FalconInput10RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 26, 4),
    _FalconInput10RlyControl_Type()
)
falconInput10RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput10RlyControl.setStatus("mandatory")


class _FalconInput10Delay_Type(Integer32):
    """Custom type falconInput10Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput10Delay_Type.__name__ = "Integer32"
_FalconInput10Delay_Object = MibScalar
falconInput10Delay = _FalconInput10Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 26, 5),
    _FalconInput10Delay_Type()
)
falconInput10Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput10Delay.setStatus("mandatory")
_FalconInput11_ObjectIdentity = ObjectIdentity
falconInput11 = _FalconInput11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 27)
)


class _FalconInput11State_Type(Integer32):
    """Custom type falconInput11State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput11State_Type.__name__ = "Integer32"
_FalconInput11State_Object = MibScalar
falconInput11State = _FalconInput11State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 27, 1),
    _FalconInput11State_Type()
)
falconInput11State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput11State.setStatus("mandatory")


class _FalconInput11Reading_Type(Integer32):
    """Custom type falconInput11Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput11Reading_Type.__name__ = "Integer32"
_FalconInput11Reading_Object = MibScalar
falconInput11Reading = _FalconInput11Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 27, 2),
    _FalconInput11Reading_Type()
)
falconInput11Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput11Reading.setStatus("mandatory")
_FalconInput11Label_Type = DisplayString
_FalconInput11Label_Object = MibScalar
falconInput11Label = _FalconInput11Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 27, 3),
    _FalconInput11Label_Type()
)
falconInput11Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput11Label.setStatus("mandatory")


class _FalconInput11RlyControl_Type(Integer32):
    """Custom type falconInput11RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput11RlyControl_Type.__name__ = "Integer32"
_FalconInput11RlyControl_Object = MibScalar
falconInput11RlyControl = _FalconInput11RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 27, 4),
    _FalconInput11RlyControl_Type()
)
falconInput11RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput11RlyControl.setStatus("mandatory")


class _FalconInput11Delay_Type(Integer32):
    """Custom type falconInput11Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput11Delay_Type.__name__ = "Integer32"
_FalconInput11Delay_Object = MibScalar
falconInput11Delay = _FalconInput11Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 27, 5),
    _FalconInput11Delay_Type()
)
falconInput11Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput11Delay.setStatus("mandatory")
_FalconInput12_ObjectIdentity = ObjectIdentity
falconInput12 = _FalconInput12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 28)
)


class _FalconInput12State_Type(Integer32):
    """Custom type falconInput12State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput12State_Type.__name__ = "Integer32"
_FalconInput12State_Object = MibScalar
falconInput12State = _FalconInput12State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 28, 1),
    _FalconInput12State_Type()
)
falconInput12State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput12State.setStatus("mandatory")


class _FalconInput12Reading_Type(Integer32):
    """Custom type falconInput12Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput12Reading_Type.__name__ = "Integer32"
_FalconInput12Reading_Object = MibScalar
falconInput12Reading = _FalconInput12Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 28, 2),
    _FalconInput12Reading_Type()
)
falconInput12Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput12Reading.setStatus("mandatory")
_FalconInput12Label_Type = DisplayString
_FalconInput12Label_Object = MibScalar
falconInput12Label = _FalconInput12Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 28, 3),
    _FalconInput12Label_Type()
)
falconInput12Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput12Label.setStatus("mandatory")


class _FalconInput12RlyControl_Type(Integer32):
    """Custom type falconInput12RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput12RlyControl_Type.__name__ = "Integer32"
_FalconInput12RlyControl_Object = MibScalar
falconInput12RlyControl = _FalconInput12RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 28, 4),
    _FalconInput12RlyControl_Type()
)
falconInput12RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput12RlyControl.setStatus("mandatory")


class _FalconInput12Delay_Type(Integer32):
    """Custom type falconInput12Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput12Delay_Type.__name__ = "Integer32"
_FalconInput12Delay_Object = MibScalar
falconInput12Delay = _FalconInput12Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 28, 5),
    _FalconInput12Delay_Type()
)
falconInput12Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput12Delay.setStatus("mandatory")
_FalconInput13_ObjectIdentity = ObjectIdentity
falconInput13 = _FalconInput13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 29)
)


class _FalconInput13State_Type(Integer32):
    """Custom type falconInput13State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput13State_Type.__name__ = "Integer32"
_FalconInput13State_Object = MibScalar
falconInput13State = _FalconInput13State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 29, 1),
    _FalconInput13State_Type()
)
falconInput13State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput13State.setStatus("mandatory")


class _FalconInput13Reading_Type(Integer32):
    """Custom type falconInput13Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput13Reading_Type.__name__ = "Integer32"
_FalconInput13Reading_Object = MibScalar
falconInput13Reading = _FalconInput13Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 29, 2),
    _FalconInput13Reading_Type()
)
falconInput13Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput13Reading.setStatus("mandatory")
_FalconInput13Label_Type = DisplayString
_FalconInput13Label_Object = MibScalar
falconInput13Label = _FalconInput13Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 29, 3),
    _FalconInput13Label_Type()
)
falconInput13Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput13Label.setStatus("mandatory")


class _FalconInput13RlyControl_Type(Integer32):
    """Custom type falconInput13RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput13RlyControl_Type.__name__ = "Integer32"
_FalconInput13RlyControl_Object = MibScalar
falconInput13RlyControl = _FalconInput13RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 29, 4),
    _FalconInput13RlyControl_Type()
)
falconInput13RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput13RlyControl.setStatus("mandatory")


class _FalconInput13Delay_Type(Integer32):
    """Custom type falconInput13Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput13Delay_Type.__name__ = "Integer32"
_FalconInput13Delay_Object = MibScalar
falconInput13Delay = _FalconInput13Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 29, 5),
    _FalconInput13Delay_Type()
)
falconInput13Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput13Delay.setStatus("mandatory")
_FalconInput14_ObjectIdentity = ObjectIdentity
falconInput14 = _FalconInput14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 30)
)


class _FalconInput14State_Type(Integer32):
    """Custom type falconInput14State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput14State_Type.__name__ = "Integer32"
_FalconInput14State_Object = MibScalar
falconInput14State = _FalconInput14State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 30, 1),
    _FalconInput14State_Type()
)
falconInput14State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput14State.setStatus("mandatory")


class _FalconInput14Reading_Type(Integer32):
    """Custom type falconInput14Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput14Reading_Type.__name__ = "Integer32"
_FalconInput14Reading_Object = MibScalar
falconInput14Reading = _FalconInput14Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 30, 2),
    _FalconInput14Reading_Type()
)
falconInput14Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput14Reading.setStatus("mandatory")
_FalconInput14Label_Type = DisplayString
_FalconInput14Label_Object = MibScalar
falconInput14Label = _FalconInput14Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 30, 3),
    _FalconInput14Label_Type()
)
falconInput14Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput14Label.setStatus("mandatory")


class _FalconInput14RlyControl_Type(Integer32):
    """Custom type falconInput14RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput14RlyControl_Type.__name__ = "Integer32"
_FalconInput14RlyControl_Object = MibScalar
falconInput14RlyControl = _FalconInput14RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 30, 4),
    _FalconInput14RlyControl_Type()
)
falconInput14RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput14RlyControl.setStatus("mandatory")


class _FalconInput14Delay_Type(Integer32):
    """Custom type falconInput14Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput14Delay_Type.__name__ = "Integer32"
_FalconInput14Delay_Object = MibScalar
falconInput14Delay = _FalconInput14Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 30, 5),
    _FalconInput14Delay_Type()
)
falconInput14Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput14Delay.setStatus("mandatory")
_FalconInput15_ObjectIdentity = ObjectIdentity
falconInput15 = _FalconInput15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 31)
)


class _FalconInput15State_Type(Integer32):
    """Custom type falconInput15State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput15State_Type.__name__ = "Integer32"
_FalconInput15State_Object = MibScalar
falconInput15State = _FalconInput15State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 31, 1),
    _FalconInput15State_Type()
)
falconInput15State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput15State.setStatus("mandatory")


class _FalconInput15Reading_Type(Integer32):
    """Custom type falconInput15Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput15Reading_Type.__name__ = "Integer32"
_FalconInput15Reading_Object = MibScalar
falconInput15Reading = _FalconInput15Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 31, 2),
    _FalconInput15Reading_Type()
)
falconInput15Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput15Reading.setStatus("mandatory")
_FalconInput15Label_Type = DisplayString
_FalconInput15Label_Object = MibScalar
falconInput15Label = _FalconInput15Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 31, 3),
    _FalconInput15Label_Type()
)
falconInput15Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput15Label.setStatus("mandatory")


class _FalconInput15RlyControl_Type(Integer32):
    """Custom type falconInput15RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput15RlyControl_Type.__name__ = "Integer32"
_FalconInput15RlyControl_Object = MibScalar
falconInput15RlyControl = _FalconInput15RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 31, 4),
    _FalconInput15RlyControl_Type()
)
falconInput15RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput15RlyControl.setStatus("mandatory")


class _FalconInput15Delay_Type(Integer32):
    """Custom type falconInput15Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput15Delay_Type.__name__ = "Integer32"
_FalconInput15Delay_Object = MibScalar
falconInput15Delay = _FalconInput15Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 31, 50),
    _FalconInput15Delay_Type()
)
falconInput15Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput15Delay.setStatus("mandatory")
_FalconInput16_ObjectIdentity = ObjectIdentity
falconInput16 = _FalconInput16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 32)
)


class _FalconInput16State_Type(Integer32):
    """Custom type falconInput16State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput16State_Type.__name__ = "Integer32"
_FalconInput16State_Object = MibScalar
falconInput16State = _FalconInput16State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 32, 1),
    _FalconInput16State_Type()
)
falconInput16State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput16State.setStatus("mandatory")


class _FalconInput16Reading_Type(Integer32):
    """Custom type falconInput16Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput16Reading_Type.__name__ = "Integer32"
_FalconInput16Reading_Object = MibScalar
falconInput16Reading = _FalconInput16Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 32, 2),
    _FalconInput16Reading_Type()
)
falconInput16Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput16Reading.setStatus("mandatory")
_FalconInput16Label_Type = DisplayString
_FalconInput16Label_Object = MibScalar
falconInput16Label = _FalconInput16Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 32, 3),
    _FalconInput16Label_Type()
)
falconInput16Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput16Label.setStatus("mandatory")


class _FalconInput16RlyControl_Type(Integer32):
    """Custom type falconInput16RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput16RlyControl_Type.__name__ = "Integer32"
_FalconInput16RlyControl_Object = MibScalar
falconInput16RlyControl = _FalconInput16RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 32, 4),
    _FalconInput16RlyControl_Type()
)
falconInput16RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput16RlyControl.setStatus("mandatory")


class _FalconInput16Delay_Type(Integer32):
    """Custom type falconInput16Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput16Delay_Type.__name__ = "Integer32"
_FalconInput16Delay_Object = MibScalar
falconInput16Delay = _FalconInput16Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 32, 5),
    _FalconInput16Delay_Type()
)
falconInput16Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput16Delay.setStatus("mandatory")
_FalconInput17_ObjectIdentity = ObjectIdentity
falconInput17 = _FalconInput17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 33)
)


class _FalconInput17State_Type(Integer32):
    """Custom type falconInput17State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput17State_Type.__name__ = "Integer32"
_FalconInput17State_Object = MibScalar
falconInput17State = _FalconInput17State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 33, 1),
    _FalconInput17State_Type()
)
falconInput17State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput17State.setStatus("mandatory")


class _FalconInput17Reading_Type(Integer32):
    """Custom type falconInput17Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput17Reading_Type.__name__ = "Integer32"
_FalconInput17Reading_Object = MibScalar
falconInput17Reading = _FalconInput17Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 33, 2),
    _FalconInput17Reading_Type()
)
falconInput17Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput17Reading.setStatus("mandatory")
_FalconInput17Label_Type = DisplayString
_FalconInput17Label_Object = MibScalar
falconInput17Label = _FalconInput17Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 33, 3),
    _FalconInput17Label_Type()
)
falconInput17Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput17Label.setStatus("mandatory")


class _FalconInput17RlyControl_Type(Integer32):
    """Custom type falconInput17RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput17RlyControl_Type.__name__ = "Integer32"
_FalconInput17RlyControl_Object = MibScalar
falconInput17RlyControl = _FalconInput17RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 33, 4),
    _FalconInput17RlyControl_Type()
)
falconInput17RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput17RlyControl.setStatus("mandatory")


class _FalconInput17Delay_Type(Integer32):
    """Custom type falconInput17Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput17Delay_Type.__name__ = "Integer32"
_FalconInput17Delay_Object = MibScalar
falconInput17Delay = _FalconInput17Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 33, 5),
    _FalconInput17Delay_Type()
)
falconInput17Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput17Delay.setStatus("mandatory")
_FalconInput18_ObjectIdentity = ObjectIdentity
falconInput18 = _FalconInput18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 34)
)


class _FalconInput18State_Type(Integer32):
    """Custom type falconInput18State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput18State_Type.__name__ = "Integer32"
_FalconInput18State_Object = MibScalar
falconInput18State = _FalconInput18State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 34, 1),
    _FalconInput18State_Type()
)
falconInput18State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput18State.setStatus("mandatory")


class _FalconInput18Reading_Type(Integer32):
    """Custom type falconInput18Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput18Reading_Type.__name__ = "Integer32"
_FalconInput18Reading_Object = MibScalar
falconInput18Reading = _FalconInput18Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 34, 2),
    _FalconInput18Reading_Type()
)
falconInput18Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput18Reading.setStatus("mandatory")
_FalconInput18Label_Type = DisplayString
_FalconInput18Label_Object = MibScalar
falconInput18Label = _FalconInput18Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 34, 3),
    _FalconInput18Label_Type()
)
falconInput18Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput18Label.setStatus("mandatory")


class _FalconInput18RlyControl_Type(Integer32):
    """Custom type falconInput18RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput18RlyControl_Type.__name__ = "Integer32"
_FalconInput18RlyControl_Object = MibScalar
falconInput18RlyControl = _FalconInput18RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 34, 4),
    _FalconInput18RlyControl_Type()
)
falconInput18RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput18RlyControl.setStatus("mandatory")


class _FalconInput18Delay_Type(Integer32):
    """Custom type falconInput18Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput18Delay_Type.__name__ = "Integer32"
_FalconInput18Delay_Object = MibScalar
falconInput18Delay = _FalconInput18Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 34, 5),
    _FalconInput18Delay_Type()
)
falconInput18Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput18Delay.setStatus("mandatory")
_FalconInput19_ObjectIdentity = ObjectIdentity
falconInput19 = _FalconInput19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 35)
)


class _FalconInput19State_Type(Integer32):
    """Custom type falconInput19State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput19State_Type.__name__ = "Integer32"
_FalconInput19State_Object = MibScalar
falconInput19State = _FalconInput19State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 35, 1),
    _FalconInput19State_Type()
)
falconInput19State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput19State.setStatus("mandatory")


class _FalconInput19Reading_Type(Integer32):
    """Custom type falconInput19Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput19Reading_Type.__name__ = "Integer32"
_FalconInput19Reading_Object = MibScalar
falconInput19Reading = _FalconInput19Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 35, 2),
    _FalconInput19Reading_Type()
)
falconInput19Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput19Reading.setStatus("mandatory")
_FalconInput19Label_Type = DisplayString
_FalconInput19Label_Object = MibScalar
falconInput19Label = _FalconInput19Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 35, 3),
    _FalconInput19Label_Type()
)
falconInput19Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput19Label.setStatus("mandatory")


class _FalconInput19RlyControl_Type(Integer32):
    """Custom type falconInput19RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput19RlyControl_Type.__name__ = "Integer32"
_FalconInput19RlyControl_Object = MibScalar
falconInput19RlyControl = _FalconInput19RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 35, 4),
    _FalconInput19RlyControl_Type()
)
falconInput19RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput19RlyControl.setStatus("mandatory")


class _FalconInput19Delay_Type(Integer32):
    """Custom type falconInput19Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput19Delay_Type.__name__ = "Integer32"
_FalconInput19Delay_Object = MibScalar
falconInput19Delay = _FalconInput19Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 35, 5),
    _FalconInput19Delay_Type()
)
falconInput19Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput19Delay.setStatus("mandatory")
_FalconInput20_ObjectIdentity = ObjectIdentity
falconInput20 = _FalconInput20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 36)
)


class _FalconInput20State_Type(Integer32):
    """Custom type falconInput20State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("digital-nc-installed", 4),
          ("digital-no-installed", 3),
          ("notInstalled", 1))
    )


_FalconInput20State_Type.__name__ = "Integer32"
_FalconInput20State_Object = MibScalar
falconInput20State = _FalconInput20State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 36, 1),
    _FalconInput20State_Type()
)
falconInput20State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput20State.setStatus("mandatory")


class _FalconInput20Reading_Type(Integer32):
    """Custom type falconInput20Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FalconInput20Reading_Type.__name__ = "Integer32"
_FalconInput20Reading_Object = MibScalar
falconInput20Reading = _FalconInput20Reading_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 36, 2),
    _FalconInput20Reading_Type()
)
falconInput20Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconInput20Reading.setStatus("mandatory")
_FalconInput20Label_Type = DisplayString
_FalconInput20Label_Object = MibScalar
falconInput20Label = _FalconInput20Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 36, 3),
    _FalconInput20Label_Type()
)
falconInput20Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput20Label.setStatus("mandatory")


class _FalconInput20RlyControl_Type(Integer32):
    """Custom type falconInput20RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconInput20RlyControl_Type.__name__ = "Integer32"
_FalconInput20RlyControl_Object = MibScalar
falconInput20RlyControl = _FalconInput20RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 36, 4),
    _FalconInput20RlyControl_Type()
)
falconInput20RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput20RlyControl.setStatus("mandatory")


class _FalconInput20Delay_Type(Integer32):
    """Custom type falconInput20Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FalconInput20Delay_Type.__name__ = "Integer32"
_FalconInput20Delay_Object = MibScalar
falconInput20Delay = _FalconInput20Delay_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 3, 36, 5),
    _FalconInput20Delay_Type()
)
falconInput20Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconInput20Delay.setStatus("mandatory")
_FalconOutputs_ObjectIdentity = ObjectIdentity
falconOutputs = _FalconOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4)
)
_FalconRelay1_ObjectIdentity = ObjectIdentity
falconRelay1 = _FalconRelay1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 1)
)


class _FalconRelay1State_Type(Integer32):
    """Custom type falconRelay1State based on Integer32"""
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
        *(("forceoff", 4),
          ("forceon", 3),
          ("keypadcontrolled", 5),
          ("normallyoff", 1),
          ("normallyon", 2))
    )


_FalconRelay1State_Type.__name__ = "Integer32"
_FalconRelay1State_Object = MibScalar
falconRelay1State = _FalconRelay1State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 1, 1),
    _FalconRelay1State_Type()
)
falconRelay1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay1State.setStatus("mandatory")


class _FalconRelay1Status_Type(Integer32):
    """Custom type falconRelay1Status based on Integer32"""
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
        *(("alarmedactive", 6),
          ("forcedoff", 4),
          ("forcedon", 3),
          ("keycodeactive", 5),
          ("normaloff", 1),
          ("normalon", 2))
    )


_FalconRelay1Status_Type.__name__ = "Integer32"
_FalconRelay1Status_Object = MibScalar
falconRelay1Status = _FalconRelay1Status_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 1, 2),
    _FalconRelay1Status_Type()
)
falconRelay1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconRelay1Status.setStatus("mandatory")
_FalconRelay1Label_Type = DisplayString
_FalconRelay1Label_Object = MibScalar
falconRelay1Label = _FalconRelay1Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 1, 3),
    _FalconRelay1Label_Type()
)
falconRelay1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay1Label.setStatus("mandatory")


class _FalconRelay1Time_Type(Integer32):
    """Custom type falconRelay1Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconRelay1Time_Type.__name__ = "Integer32"
_FalconRelay1Time_Object = MibScalar
falconRelay1Time = _FalconRelay1Time_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 1, 4),
    _FalconRelay1Time_Type()
)
falconRelay1Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay1Time.setStatus("mandatory")
_FalconRelay2_ObjectIdentity = ObjectIdentity
falconRelay2 = _FalconRelay2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 2)
)


class _FalconRelay2State_Type(Integer32):
    """Custom type falconRelay2State based on Integer32"""
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
        *(("forceoff", 4),
          ("forceon", 3),
          ("keypascontrolled", 5),
          ("normallyoff", 1),
          ("normallyon", 2))
    )


_FalconRelay2State_Type.__name__ = "Integer32"
_FalconRelay2State_Object = MibScalar
falconRelay2State = _FalconRelay2State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 2, 1),
    _FalconRelay2State_Type()
)
falconRelay2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay2State.setStatus("mandatory")


class _FalconRelay2Status_Type(Integer32):
    """Custom type falconRelay2Status based on Integer32"""
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
        *(("alarmedactive", 6),
          ("forcedoff", 4),
          ("forcedon", 3),
          ("keycodeactive", 5),
          ("normaloff", 1),
          ("normalon", 2))
    )


_FalconRelay2Status_Type.__name__ = "Integer32"
_FalconRelay2Status_Object = MibScalar
falconRelay2Status = _FalconRelay2Status_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 2, 2),
    _FalconRelay2Status_Type()
)
falconRelay2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconRelay2Status.setStatus("mandatory")
_FalconRelay2Label_Type = DisplayString
_FalconRelay2Label_Object = MibScalar
falconRelay2Label = _FalconRelay2Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 2, 3),
    _FalconRelay2Label_Type()
)
falconRelay2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay2Label.setStatus("mandatory")


class _FalconRelay2Time_Type(Integer32):
    """Custom type falconRelay2Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconRelay2Time_Type.__name__ = "Integer32"
_FalconRelay2Time_Object = MibScalar
falconRelay2Time = _FalconRelay2Time_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 2, 4),
    _FalconRelay2Time_Type()
)
falconRelay2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay2Time.setStatus("mandatory")
_FalconRelay3_ObjectIdentity = ObjectIdentity
falconRelay3 = _FalconRelay3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 3)
)


class _FalconRelay3State_Type(Integer32):
    """Custom type falconRelay3State based on Integer32"""
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
        *(("forceoff", 4),
          ("forceon", 3),
          ("keypascontrolled", 5),
          ("normallyoff", 1),
          ("normallyon", 2))
    )


_FalconRelay3State_Type.__name__ = "Integer32"
_FalconRelay3State_Object = MibScalar
falconRelay3State = _FalconRelay3State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 3, 1),
    _FalconRelay3State_Type()
)
falconRelay3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay3State.setStatus("mandatory")


class _FalconRelay3Status_Type(Integer32):
    """Custom type falconRelay3Status based on Integer32"""
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
        *(("alarmedactive", 6),
          ("forcedoff", 4),
          ("forcedon", 3),
          ("keycodeactive", 5),
          ("normaloff", 1),
          ("normalon", 2))
    )


_FalconRelay3Status_Type.__name__ = "Integer32"
_FalconRelay3Status_Object = MibScalar
falconRelay3Status = _FalconRelay3Status_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 3, 2),
    _FalconRelay3Status_Type()
)
falconRelay3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconRelay3Status.setStatus("mandatory")
_FalconRelay3Label_Type = DisplayString
_FalconRelay3Label_Object = MibScalar
falconRelay3Label = _FalconRelay3Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 3, 3),
    _FalconRelay3Label_Type()
)
falconRelay3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay3Label.setStatus("mandatory")


class _FalconRelay3Time_Type(Integer32):
    """Custom type falconRelay3Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconRelay3Time_Type.__name__ = "Integer32"
_FalconRelay3Time_Object = MibScalar
falconRelay3Time = _FalconRelay3Time_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 3, 4),
    _FalconRelay3Time_Type()
)
falconRelay3Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay3Time.setStatus("mandatory")
_FalconRelay4_ObjectIdentity = ObjectIdentity
falconRelay4 = _FalconRelay4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 4)
)


class _FalconRelay4State_Type(Integer32):
    """Custom type falconRelay4State based on Integer32"""
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
        *(("forceoff", 4),
          ("forceon", 3),
          ("keypascontrolled", 5),
          ("normallyoff", 1),
          ("normallyon", 2))
    )


_FalconRelay4State_Type.__name__ = "Integer32"
_FalconRelay4State_Object = MibScalar
falconRelay4State = _FalconRelay4State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 4, 1),
    _FalconRelay4State_Type()
)
falconRelay4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay4State.setStatus("mandatory")


class _FalconRelay4Status_Type(Integer32):
    """Custom type falconRelay4Status based on Integer32"""
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
        *(("alarmedactive", 6),
          ("forcedoff", 4),
          ("forcedon", 3),
          ("keycodeactive", 5),
          ("normaloff", 1),
          ("normalon", 2))
    )


_FalconRelay4Status_Type.__name__ = "Integer32"
_FalconRelay4Status_Object = MibScalar
falconRelay4Status = _FalconRelay4Status_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 4, 2),
    _FalconRelay4Status_Type()
)
falconRelay4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconRelay4Status.setStatus("mandatory")
_FalconRelay4Label_Type = DisplayString
_FalconRelay4Label_Object = MibScalar
falconRelay4Label = _FalconRelay4Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 4, 3),
    _FalconRelay4Label_Type()
)
falconRelay4Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay4Label.setStatus("mandatory")


class _FalconRelay4Time_Type(Integer32):
    """Custom type falconRelay4Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconRelay4Time_Type.__name__ = "Integer32"
_FalconRelay4Time_Object = MibScalar
falconRelay4Time = _FalconRelay4Time_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 4, 4),
    _FalconRelay4Time_Type()
)
falconRelay4Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay4Time.setStatus("mandatory")
_FalconRelay5_ObjectIdentity = ObjectIdentity
falconRelay5 = _FalconRelay5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 5)
)


class _FalconRelay5State_Type(Integer32):
    """Custom type falconRelay5State based on Integer32"""
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
        *(("forceoff", 4),
          ("forceon", 3),
          ("keypascontrolled", 5),
          ("normallyoff", 1),
          ("normallyon", 2))
    )


_FalconRelay5State_Type.__name__ = "Integer32"
_FalconRelay5State_Object = MibScalar
falconRelay5State = _FalconRelay5State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 5, 1),
    _FalconRelay5State_Type()
)
falconRelay5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay5State.setStatus("mandatory")


class _FalconRelay5Status_Type(Integer32):
    """Custom type falconRelay5Status based on Integer32"""
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
        *(("alarmedactive", 6),
          ("forcedoff", 4),
          ("forcedon", 3),
          ("keycodeactive", 5),
          ("normaloff", 1),
          ("normalon", 2))
    )


_FalconRelay5Status_Type.__name__ = "Integer32"
_FalconRelay5Status_Object = MibScalar
falconRelay5Status = _FalconRelay5Status_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 5, 2),
    _FalconRelay5Status_Type()
)
falconRelay5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconRelay5Status.setStatus("mandatory")
_FalconRelay5Label_Type = DisplayString
_FalconRelay5Label_Object = MibScalar
falconRelay5Label = _FalconRelay5Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 5, 3),
    _FalconRelay5Label_Type()
)
falconRelay5Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay5Label.setStatus("mandatory")


class _FalconRelay5Time_Type(Integer32):
    """Custom type falconRelay5Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconRelay5Time_Type.__name__ = "Integer32"
_FalconRelay5Time_Object = MibScalar
falconRelay5Time = _FalconRelay5Time_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 5, 4),
    _FalconRelay5Time_Type()
)
falconRelay5Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay5Time.setStatus("mandatory")
_FalconRelay6_ObjectIdentity = ObjectIdentity
falconRelay6 = _FalconRelay6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 6)
)


class _FalconRelay6State_Type(Integer32):
    """Custom type falconRelay6State based on Integer32"""
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
        *(("forceoff", 4),
          ("forceon", 3),
          ("keypascontrolled", 5),
          ("normallyoff", 1),
          ("normallyon", 2))
    )


_FalconRelay6State_Type.__name__ = "Integer32"
_FalconRelay6State_Object = MibScalar
falconRelay6State = _FalconRelay6State_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 6, 1),
    _FalconRelay6State_Type()
)
falconRelay6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay6State.setStatus("mandatory")


class _FalconRelay6Status_Type(Integer32):
    """Custom type falconRelay6Status based on Integer32"""
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
        *(("alarmedactive", 6),
          ("forcedoff", 4),
          ("forcedon", 3),
          ("keycodeactive", 5),
          ("normaloff", 1),
          ("normalon", 2))
    )


_FalconRelay6Status_Type.__name__ = "Integer32"
_FalconRelay6Status_Object = MibScalar
falconRelay6Status = _FalconRelay6Status_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 6, 2),
    _FalconRelay6Status_Type()
)
falconRelay6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconRelay6Status.setStatus("mandatory")
_FalconRelay6Label_Type = DisplayString
_FalconRelay6Label_Object = MibScalar
falconRelay6Label = _FalconRelay6Label_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 6, 3),
    _FalconRelay6Label_Type()
)
falconRelay6Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay6Label.setStatus("mandatory")


class _FalconRelay6Time_Type(Integer32):
    """Custom type falconRelay6Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FalconRelay6Time_Type.__name__ = "Integer32"
_FalconRelay6Time_Object = MibScalar
falconRelay6Time = _FalconRelay6Time_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 4, 6, 4),
    _FalconRelay6Time_Type()
)
falconRelay6Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconRelay6Time.setStatus("mandatory")
_FalconAlarms_ObjectIdentity = ObjectIdentity
falconAlarms = _FalconAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5)
)
_FalconAlarmsPresent_Type = Gauge32
_FalconAlarmsPresent_Object = MibScalar
falconAlarmsPresent = _FalconAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 1),
    _FalconAlarmsPresent_Type()
)
falconAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconAlarmsPresent.setStatus("current")
_FalconAlarmTable_Object = MibTable
falconAlarmTable = _FalconAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    falconAlarmTable.setStatus("current")
_FalconAlarmEntry_Object = MibTableRow
falconAlarmEntry = _FalconAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 2, 1)
)
falconAlarmEntry.setIndexNames(
    (0, "RLE-FALCON-MIB", "falconAlarmId"),
)
if mibBuilder.loadTexts:
    falconAlarmEntry.setStatus("current")
_FalconAlarmId_Type = PositiveInteger
_FalconAlarmId_Object = MibTableColumn
falconAlarmId = _FalconAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 2, 1, 1),
    _FalconAlarmId_Type()
)
falconAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    falconAlarmId.setStatus("current")
_FalconAlarmDescr_Type = ObjectIdentifier
_FalconAlarmDescr_Object = MibTableColumn
falconAlarmDescr = _FalconAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 2, 1, 2),
    _FalconAlarmDescr_Type()
)
falconAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconAlarmDescr.setStatus("current")
_FalconWellKnownAlarms_ObjectIdentity = ObjectIdentity
falconWellKnownAlarms = _FalconWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3)
)
_FalconInput1HighAlarm_ObjectIdentity = ObjectIdentity
falconInput1HighAlarm = _FalconInput1HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    falconInput1HighAlarm.setStatus("current")
_FalconInput1LowAlarm_ObjectIdentity = ObjectIdentity
falconInput1LowAlarm = _FalconInput1LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    falconInput1LowAlarm.setStatus("current")
_FalconInput1High2Alarm_ObjectIdentity = ObjectIdentity
falconInput1High2Alarm = _FalconInput1High2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    falconInput1High2Alarm.setStatus("current")
_FalconInput1Low2Alarm_ObjectIdentity = ObjectIdentity
falconInput1Low2Alarm = _FalconInput1Low2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 4)
)
if mibBuilder.loadTexts:
    falconInput1Low2Alarm.setStatus("current")
_FalconInput2HighAlarm_ObjectIdentity = ObjectIdentity
falconInput2HighAlarm = _FalconInput2HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 5)
)
if mibBuilder.loadTexts:
    falconInput2HighAlarm.setStatus("current")
_FalconInput2LowAlarm_ObjectIdentity = ObjectIdentity
falconInput2LowAlarm = _FalconInput2LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 6)
)
if mibBuilder.loadTexts:
    falconInput2LowAlarm.setStatus("current")
_FalconInput2High2Alarm_ObjectIdentity = ObjectIdentity
falconInput2High2Alarm = _FalconInput2High2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 7)
)
if mibBuilder.loadTexts:
    falconInput2High2Alarm.setStatus("current")
_FalconInput2Low2Alarm_ObjectIdentity = ObjectIdentity
falconInput2Low2Alarm = _FalconInput2Low2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    falconInput2Low2Alarm.setStatus("current")
_FalconInput3HighAlarm_ObjectIdentity = ObjectIdentity
falconInput3HighAlarm = _FalconInput3HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 9)
)
if mibBuilder.loadTexts:
    falconInput3HighAlarm.setStatus("current")
_FalconInput3LowAlarm_ObjectIdentity = ObjectIdentity
falconInput3LowAlarm = _FalconInput3LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 10)
)
if mibBuilder.loadTexts:
    falconInput3LowAlarm.setStatus("current")
_FalconInput3High2Alarm_ObjectIdentity = ObjectIdentity
falconInput3High2Alarm = _FalconInput3High2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 11)
)
if mibBuilder.loadTexts:
    falconInput3High2Alarm.setStatus("current")
_FalconInput3Low2Alarm_ObjectIdentity = ObjectIdentity
falconInput3Low2Alarm = _FalconInput3Low2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 12)
)
if mibBuilder.loadTexts:
    falconInput3Low2Alarm.setStatus("current")
_FalconInput4HighAlarm_ObjectIdentity = ObjectIdentity
falconInput4HighAlarm = _FalconInput4HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 13)
)
if mibBuilder.loadTexts:
    falconInput4HighAlarm.setStatus("current")
_FalconInput4LowAlarm_ObjectIdentity = ObjectIdentity
falconInput4LowAlarm = _FalconInput4LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 14)
)
if mibBuilder.loadTexts:
    falconInput4LowAlarm.setStatus("current")
_FalconInput4High2Alarm_ObjectIdentity = ObjectIdentity
falconInput4High2Alarm = _FalconInput4High2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 15)
)
if mibBuilder.loadTexts:
    falconInput4High2Alarm.setStatus("current")
_FalconInput4Low2Alarm_ObjectIdentity = ObjectIdentity
falconInput4Low2Alarm = _FalconInput4Low2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 16)
)
if mibBuilder.loadTexts:
    falconInput4Low2Alarm.setStatus("current")
_FalconInput5HighAlarm_ObjectIdentity = ObjectIdentity
falconInput5HighAlarm = _FalconInput5HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 17)
)
if mibBuilder.loadTexts:
    falconInput5HighAlarm.setStatus("current")
_FalconInput5LowAlarm_ObjectIdentity = ObjectIdentity
falconInput5LowAlarm = _FalconInput5LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 18)
)
if mibBuilder.loadTexts:
    falconInput5LowAlarm.setStatus("current")
_FalconInput5High2Alarm_ObjectIdentity = ObjectIdentity
falconInput5High2Alarm = _FalconInput5High2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 19)
)
if mibBuilder.loadTexts:
    falconInput5High2Alarm.setStatus("current")
_FalconInput5Low2Alarm_ObjectIdentity = ObjectIdentity
falconInput5Low2Alarm = _FalconInput5Low2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 20)
)
if mibBuilder.loadTexts:
    falconInput5Low2Alarm.setStatus("current")
_FalconInput6HighAlarm_ObjectIdentity = ObjectIdentity
falconInput6HighAlarm = _FalconInput6HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 21)
)
if mibBuilder.loadTexts:
    falconInput6HighAlarm.setStatus("current")
_FalconInput6LowAlarm_ObjectIdentity = ObjectIdentity
falconInput6LowAlarm = _FalconInput6LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 22)
)
if mibBuilder.loadTexts:
    falconInput6LowAlarm.setStatus("current")
_FalconInput6High2Alarm_ObjectIdentity = ObjectIdentity
falconInput6High2Alarm = _FalconInput6High2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 23)
)
if mibBuilder.loadTexts:
    falconInput6High2Alarm.setStatus("current")
_FalconInput6Low2Alarm_ObjectIdentity = ObjectIdentity
falconInput6Low2Alarm = _FalconInput6Low2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 24)
)
if mibBuilder.loadTexts:
    falconInput6Low2Alarm.setStatus("current")
_FalconInput7HighAlarm_ObjectIdentity = ObjectIdentity
falconInput7HighAlarm = _FalconInput7HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 25)
)
if mibBuilder.loadTexts:
    falconInput7HighAlarm.setStatus("current")
_FalconInput7LowAlarm_ObjectIdentity = ObjectIdentity
falconInput7LowAlarm = _FalconInput7LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 26)
)
if mibBuilder.loadTexts:
    falconInput7LowAlarm.setStatus("current")
_FalconInput7High2Alarm_ObjectIdentity = ObjectIdentity
falconInput7High2Alarm = _FalconInput7High2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 27)
)
if mibBuilder.loadTexts:
    falconInput7High2Alarm.setStatus("current")
_FalconInput7Low2Alarm_ObjectIdentity = ObjectIdentity
falconInput7Low2Alarm = _FalconInput7Low2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 28)
)
if mibBuilder.loadTexts:
    falconInput7Low2Alarm.setStatus("current")
_FalconInput8HighAlarm_ObjectIdentity = ObjectIdentity
falconInput8HighAlarm = _FalconInput8HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 29)
)
if mibBuilder.loadTexts:
    falconInput8HighAlarm.setStatus("current")
_FalconInput8LowAlarm_ObjectIdentity = ObjectIdentity
falconInput8LowAlarm = _FalconInput8LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 30)
)
if mibBuilder.loadTexts:
    falconInput8LowAlarm.setStatus("current")
_FalconInput8High2Alarm_ObjectIdentity = ObjectIdentity
falconInput8High2Alarm = _FalconInput8High2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 31)
)
if mibBuilder.loadTexts:
    falconInput8High2Alarm.setStatus("current")
_FalconInput8Low2Alarm_ObjectIdentity = ObjectIdentity
falconInput8Low2Alarm = _FalconInput8Low2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 32)
)
if mibBuilder.loadTexts:
    falconInput8Low2Alarm.setStatus("current")
_FalconInput1DigAlarm_ObjectIdentity = ObjectIdentity
falconInput1DigAlarm = _FalconInput1DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 81)
)
if mibBuilder.loadTexts:
    falconInput1DigAlarm.setStatus("current")
_FalconInput2DigAlarm_ObjectIdentity = ObjectIdentity
falconInput2DigAlarm = _FalconInput2DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 82)
)
if mibBuilder.loadTexts:
    falconInput2DigAlarm.setStatus("current")
_FalconInput3DigAlarm_ObjectIdentity = ObjectIdentity
falconInput3DigAlarm = _FalconInput3DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 83)
)
if mibBuilder.loadTexts:
    falconInput3DigAlarm.setStatus("current")
_FalconInput4DigAlarm_ObjectIdentity = ObjectIdentity
falconInput4DigAlarm = _FalconInput4DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 84)
)
if mibBuilder.loadTexts:
    falconInput4DigAlarm.setStatus("current")
_FalconInput5DigAlarm_ObjectIdentity = ObjectIdentity
falconInput5DigAlarm = _FalconInput5DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 85)
)
if mibBuilder.loadTexts:
    falconInput5DigAlarm.setStatus("current")
_FalconInput6DigAlarm_ObjectIdentity = ObjectIdentity
falconInput6DigAlarm = _FalconInput6DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 86)
)
if mibBuilder.loadTexts:
    falconInput6DigAlarm.setStatus("current")
_FalconInput7DigAlarm_ObjectIdentity = ObjectIdentity
falconInput7DigAlarm = _FalconInput7DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 87)
)
if mibBuilder.loadTexts:
    falconInput7DigAlarm.setStatus("current")
_FalconInput8DigAlarm_ObjectIdentity = ObjectIdentity
falconInput8DigAlarm = _FalconInput8DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 88)
)
if mibBuilder.loadTexts:
    falconInput8DigAlarm.setStatus("current")
_FalconInput9DigAlarm_ObjectIdentity = ObjectIdentity
falconInput9DigAlarm = _FalconInput9DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 89)
)
if mibBuilder.loadTexts:
    falconInput9DigAlarm.setStatus("current")
_FalconInput10DigAlarm_ObjectIdentity = ObjectIdentity
falconInput10DigAlarm = _FalconInput10DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 90)
)
if mibBuilder.loadTexts:
    falconInput10DigAlarm.setStatus("current")
_FalconInput11DigAlarm_ObjectIdentity = ObjectIdentity
falconInput11DigAlarm = _FalconInput11DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 91)
)
if mibBuilder.loadTexts:
    falconInput11DigAlarm.setStatus("current")
_FalconInput12DigAlarm_ObjectIdentity = ObjectIdentity
falconInput12DigAlarm = _FalconInput12DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 92)
)
if mibBuilder.loadTexts:
    falconInput12DigAlarm.setStatus("current")
_FalconInput13DigAlarm_ObjectIdentity = ObjectIdentity
falconInput13DigAlarm = _FalconInput13DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 93)
)
if mibBuilder.loadTexts:
    falconInput13DigAlarm.setStatus("current")
_FalconInput14DigAlarm_ObjectIdentity = ObjectIdentity
falconInput14DigAlarm = _FalconInput14DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 94)
)
if mibBuilder.loadTexts:
    falconInput14DigAlarm.setStatus("current")
_FalconInput15DigAlarm_ObjectIdentity = ObjectIdentity
falconInput15DigAlarm = _FalconInput15DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 95)
)
if mibBuilder.loadTexts:
    falconInput15DigAlarm.setStatus("current")
_FalconInput16DigAlarm_ObjectIdentity = ObjectIdentity
falconInput16DigAlarm = _FalconInput16DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 96)
)
if mibBuilder.loadTexts:
    falconInput16DigAlarm.setStatus("current")
_FalconInput17DigAlarm_ObjectIdentity = ObjectIdentity
falconInput17DigAlarm = _FalconInput17DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 97)
)
if mibBuilder.loadTexts:
    falconInput17DigAlarm.setStatus("current")
_FalconInput18DigAlarm_ObjectIdentity = ObjectIdentity
falconInput18DigAlarm = _FalconInput18DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 98)
)
if mibBuilder.loadTexts:
    falconInput18DigAlarm.setStatus("current")
_FalconInput19DigAlarm_ObjectIdentity = ObjectIdentity
falconInput19DigAlarm = _FalconInput19DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 99)
)
if mibBuilder.loadTexts:
    falconInput19DigAlarm.setStatus("current")
_FalconInput20DigAlarm_ObjectIdentity = ObjectIdentity
falconInput20DigAlarm = _FalconInput20DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 100)
)
if mibBuilder.loadTexts:
    falconInput20DigAlarm.setStatus("current")
_FalconOnBatteryAlarm_ObjectIdentity = ObjectIdentity
falconOnBatteryAlarm = _FalconOnBatteryAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 102)
)
if mibBuilder.loadTexts:
    falconOnBatteryAlarm.setStatus("current")
_FalconLowBatteryAlarm_ObjectIdentity = ObjectIdentity
falconLowBatteryAlarm = _FalconLowBatteryAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 5, 3, 103)
)
if mibBuilder.loadTexts:
    falconLowBatteryAlarm.setStatus("current")
_FalconTraps_ObjectIdentity = ObjectIdentity
falconTraps = _FalconTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 6)
)
_FalconAlarmHistory_ObjectIdentity = ObjectIdentity
falconAlarmHistory = _FalconAlarmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 7)
)
_FalconAlarmHistoryEntries_Type = Gauge32
_FalconAlarmHistoryEntries_Object = MibScalar
falconAlarmHistoryEntries = _FalconAlarmHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 7, 1),
    _FalconAlarmHistoryEntries_Type()
)
falconAlarmHistoryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconAlarmHistoryEntries.setStatus("current")


class _FalconAlarmHistoryClear_Type(Integer32):
    """Custom type falconAlarmHistoryClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearbuffer", 1)
    )


_FalconAlarmHistoryClear_Type.__name__ = "Integer32"
_FalconAlarmHistoryClear_Object = MibScalar
falconAlarmHistoryClear = _FalconAlarmHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 7, 2),
    _FalconAlarmHistoryClear_Type()
)
falconAlarmHistoryClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconAlarmHistoryClear.setStatus("mandatory")
_FalconAlarmHistoryTable_Object = MibTable
falconAlarmHistoryTable = _FalconAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    falconAlarmHistoryTable.setStatus("current")
_FalconAlarmHistoryEntry_Object = MibTableRow
falconAlarmHistoryEntry = _FalconAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 7, 3, 1)
)
falconAlarmHistoryEntry.setIndexNames(
    (0, "RLE-FALCON-MIB", "falconAlarmHistoryId"),
)
if mibBuilder.loadTexts:
    falconAlarmHistoryEntry.setStatus("current")
_FalconAlarmHistoryId_Type = PositiveInteger
_FalconAlarmHistoryId_Object = MibTableColumn
falconAlarmHistoryId = _FalconAlarmHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 7, 3, 1, 1),
    _FalconAlarmHistoryId_Type()
)
falconAlarmHistoryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    falconAlarmHistoryId.setStatus("current")
_FalconAlarmHistoryText_Type = DisplayString
_FalconAlarmHistoryText_Object = MibTableColumn
falconAlarmHistoryText = _FalconAlarmHistoryText_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 7, 3, 1, 2),
    _FalconAlarmHistoryText_Type()
)
falconAlarmHistoryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falconAlarmHistoryText.setStatus("current")
_FalconTrapSettings_ObjectIdentity = ObjectIdentity
falconTrapSettings = _FalconTrapSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 8)
)


class _FalconPersistantTraps_Type(Integer32):
    """Custom type falconPersistantTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FalconPersistantTraps_Type.__name__ = "Integer32"
_FalconPersistantTraps_Object = MibScalar
falconPersistantTraps = _FalconPersistantTraps_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 8, 1),
    _FalconPersistantTraps_Type()
)
falconPersistantTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconPersistantTraps.setStatus("mandatory")


class _FalconAlarmAcknowledge_Type(Integer32):
    """Custom type falconAlarmAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("acknowledgeAlarms", 1)
    )


_FalconAlarmAcknowledge_Type.__name__ = "Integer32"
_FalconAlarmAcknowledge_Object = MibScalar
falconAlarmAcknowledge = _FalconAlarmAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 8, 2),
    _FalconAlarmAcknowledge_Type()
)
falconAlarmAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    falconAlarmAcknowledge.setStatus("mandatory")
_Falcon8124_ObjectIdentity = ObjectIdentity
falcon8124 = _Falcon8124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 3)
)

# Managed Objects groups


# Notification objects

falconAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 6, 0, 1)
)
if mibBuilder.loadTexts:
    falconAlarmEntryAdded.setStatus(
        ""
    )

falconAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 6, 0, 2)
)
if mibBuilder.loadTexts:
    falconAlarmEntryRemoved.setStatus(
        ""
    )

falconAccessGranted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 6, 0, 3)
)
if mibBuilder.loadTexts:
    falconAccessGranted.setStatus(
        ""
    )

falconAccessDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 3184, 1, 1, 1, 6, 0, 4)
)
if mibBuilder.loadTexts:
    falconAccessDenied.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RLE-FALCON-MIB",
    **{"rle": rle,
       "products": products,
       "falcon": falcon,
       "falconMIB": falconMIB,
       "falconIdent": falconIdent,
       "falconIdentManufacturer": falconIdentManufacturer,
       "falconIdentModel": falconIdentModel,
       "falconIdentSoftwareVersion": falconIdentSoftwareVersion,
       "falconIdentSpecific": falconIdentSpecific,
       "falconSystem": falconSystem,
       "falconClock": falconClock,
       "falconDoorAlarmBypass": falconDoorAlarmBypass,
       "falconKeypad": falconKeypad,
       "falconKeypadCode1": falconKeypadCode1,
       "falconKeypadName1": falconKeypadName1,
       "falconKeypadCode2": falconKeypadCode2,
       "falconKeypadName2": falconKeypadName2,
       "falconKeypadCode3": falconKeypadCode3,
       "falconKeypadName3": falconKeypadName3,
       "falconKeypadCode4": falconKeypadCode4,
       "falconKeypadName4": falconKeypadName4,
       "falconKeypadCode5": falconKeypadCode5,
       "falconKeypadName5": falconKeypadName5,
       "falconKeypadCode6": falconKeypadCode6,
       "falconKeypadName6": falconKeypadName6,
       "falconKeypadCode7": falconKeypadCode7,
       "falconKeypadName7": falconKeypadName7,
       "falconKeypadCode8": falconKeypadCode8,
       "falconKeypadName8": falconKeypadName8,
       "falconKeypadCode9": falconKeypadCode9,
       "falconKeypadName9": falconKeypadName9,
       "falconKeypadCode10": falconKeypadCode10,
       "falconKeypadName10": falconKeypadName10,
       "falconKeypadCode11": falconKeypadCode11,
       "falconKeypadName11": falconKeypadName11,
       "falconKeypadCode12": falconKeypadCode12,
       "falconKeypadName12": falconKeypadName12,
       "falconKeypadCode13": falconKeypadCode13,
       "falconKeypadName13": falconKeypadName13,
       "falconKeypadCode14": falconKeypadCode14,
       "falconKeypadName14": falconKeypadName14,
       "falconKeypadCode15": falconKeypadCode15,
       "falconKeypadName15": falconKeypadName15,
       "falconKeypadCode16": falconKeypadCode16,
       "falconKeypadName16": falconKeypadName16,
       "falconKeypadCode17": falconKeypadCode17,
       "falconKeypadName17": falconKeypadName17,
       "falconKeypadCode18": falconKeypadCode18,
       "falconKeypadName18": falconKeypadName18,
       "falconKeypadCode19": falconKeypadCode19,
       "falconKeypadName19": falconKeypadName19,
       "falconKeypadCode20": falconKeypadCode20,
       "falconKeypadName20": falconKeypadName20,
       "falconInputVoltage": falconInputVoltage,
       "falconOnBattery": falconOnBattery,
       "falconLowBatteryThreshold": falconLowBatteryThreshold,
       "falconAnalogAverage": falconAnalogAverage,
       "falconInputs": falconInputs,
       "falconInput1": falconInput1,
       "falconInput1State": falconInput1State,
       "falconInput1Reading": falconInput1Reading,
       "falconInput1Gain": falconInput1Gain,
       "falconInput1Offset": falconInput1Offset,
       "falconInput1Label": falconInput1Label,
       "falconInput1UOM": falconInput1UOM,
       "falconInput1HighLimit2": falconInput1HighLimit2,
       "falconInput1HighLimit": falconInput1HighLimit,
       "falconInput1LowLimit": falconInput1LowLimit,
       "falconInput1LowLimit2": falconInput1LowLimit2,
       "falconInput1RlyControl": falconInput1RlyControl,
       "falconInput1Delay": falconInput1Delay,
       "falconInput1Hysteresis": falconInput1Hysteresis,
       "falconInput2": falconInput2,
       "falconInput2State": falconInput2State,
       "falconInput2Reading": falconInput2Reading,
       "falconInput2Gain": falconInput2Gain,
       "falconInput2Offset": falconInput2Offset,
       "falconInput2Label": falconInput2Label,
       "falconInput2UOM": falconInput2UOM,
       "falconInput2HighLimit2": falconInput2HighLimit2,
       "falconInput2HighLimit": falconInput2HighLimit,
       "falconInput2LowLimit": falconInput2LowLimit,
       "falconInput2LowLimit2": falconInput2LowLimit2,
       "falconInput2RlyControl": falconInput2RlyControl,
       "falconInput2Delay": falconInput2Delay,
       "falconInput2Hysteresis": falconInput2Hysteresis,
       "falconInput3": falconInput3,
       "falconInput3State": falconInput3State,
       "falconInput3Reading": falconInput3Reading,
       "falconInput3Gain": falconInput3Gain,
       "falconInput3Offset": falconInput3Offset,
       "falconInput3Label": falconInput3Label,
       "falconInput3UOM": falconInput3UOM,
       "falconInput3HighLimit2": falconInput3HighLimit2,
       "falconInput3HighLimit": falconInput3HighLimit,
       "falconInput3LowLimit": falconInput3LowLimit,
       "falconInput3LowLimit2": falconInput3LowLimit2,
       "falconInput3RlyControl": falconInput3RlyControl,
       "falconInput3Delay": falconInput3Delay,
       "falconInput3Hysteresis": falconInput3Hysteresis,
       "falconInput4": falconInput4,
       "falconInput4State": falconInput4State,
       "falconInput4Reading": falconInput4Reading,
       "falconInput4Gain": falconInput4Gain,
       "falconInput4Offset": falconInput4Offset,
       "falconInput4Label": falconInput4Label,
       "falconInput4UOM": falconInput4UOM,
       "falconInput4HighLimit2": falconInput4HighLimit2,
       "falconInput4HighLimit": falconInput4HighLimit,
       "falconInput4LowLimit": falconInput4LowLimit,
       "falconInput4LowLimit2": falconInput4LowLimit2,
       "falconInput4RlyControl": falconInput4RlyControl,
       "falconInput4Delay": falconInput4Delay,
       "falconInput4Hysteresis": falconInput4Hysteresis,
       "falconInput5": falconInput5,
       "falconInput5State": falconInput5State,
       "falconInput5Reading": falconInput5Reading,
       "falconInput5Gain": falconInput5Gain,
       "falconInput5Offset": falconInput5Offset,
       "falconInput5Label": falconInput5Label,
       "falconInput5UOM": falconInput5UOM,
       "falconInput5HighLimit2": falconInput5HighLimit2,
       "falconInput5HighLimit": falconInput5HighLimit,
       "falconInput5LowLimit": falconInput5LowLimit,
       "falconInput5LowLimit2": falconInput5LowLimit2,
       "falconInput5RlyControl": falconInput5RlyControl,
       "falconInput5Delay": falconInput5Delay,
       "falconInput5Hysteresis": falconInput5Hysteresis,
       "falconInput6": falconInput6,
       "falconInput6State": falconInput6State,
       "falconInput6Reading": falconInput6Reading,
       "falconInput6Gain": falconInput6Gain,
       "falconInput6Offset": falconInput6Offset,
       "falconInput6Label": falconInput6Label,
       "falconInput6UOM": falconInput6UOM,
       "falconInput6HighLimit2": falconInput6HighLimit2,
       "falconInput6HighLimit": falconInput6HighLimit,
       "falconInput6LowLimit": falconInput6LowLimit,
       "falconInput6LowLimit2": falconInput6LowLimit2,
       "falconInput6RlyControl": falconInput6RlyControl,
       "falconInput6Delay": falconInput6Delay,
       "falconInput6Hysteresis": falconInput6Hysteresis,
       "falconInput7": falconInput7,
       "falconInput7State": falconInput7State,
       "falconInput7Reading": falconInput7Reading,
       "falconInput7Gain": falconInput7Gain,
       "falconInput7Offset": falconInput7Offset,
       "falconInput7Label": falconInput7Label,
       "falconInput7UOM": falconInput7UOM,
       "falconInput7HighLimit2": falconInput7HighLimit2,
       "falconInput7HighLimit": falconInput7HighLimit,
       "falconInput7LowLimit": falconInput7LowLimit,
       "falconInput7LowLimit2": falconInput7LowLimit2,
       "falconInput7RlyControl": falconInput7RlyControl,
       "falconInput7Delay": falconInput7Delay,
       "falconInput7Hysteresis": falconInput7Hysteresis,
       "falconInput8": falconInput8,
       "falconInput8State": falconInput8State,
       "falconInput8Reading": falconInput8Reading,
       "falconInput8Gain": falconInput8Gain,
       "falconInput8Offset": falconInput8Offset,
       "falconInput8Label": falconInput8Label,
       "falconInput8UOM": falconInput8UOM,
       "falconInput8HighLimit2": falconInput8HighLimit2,
       "falconInput8HighLimit": falconInput8HighLimit,
       "falconInput8LowLimit": falconInput8LowLimit,
       "falconInput8RlyControl": falconInput8RlyControl,
       "falconInput8LowLimit2": falconInput8LowLimit2,
       "falconInput8Delay": falconInput8Delay,
       "falconInput8Hysteresis": falconInput8Hysteresis,
       "falconInput9": falconInput9,
       "falconInput9State": falconInput9State,
       "falconInput9Reading": falconInput9Reading,
       "falconInput9Label": falconInput9Label,
       "falconInput9RlyControl": falconInput9RlyControl,
       "falconInput9Delay": falconInput9Delay,
       "falconInput10": falconInput10,
       "falconInput10State": falconInput10State,
       "falconInput10Reading": falconInput10Reading,
       "falconInput10Label": falconInput10Label,
       "falconInput10RlyControl": falconInput10RlyControl,
       "falconInput10Delay": falconInput10Delay,
       "falconInput11": falconInput11,
       "falconInput11State": falconInput11State,
       "falconInput11Reading": falconInput11Reading,
       "falconInput11Label": falconInput11Label,
       "falconInput11RlyControl": falconInput11RlyControl,
       "falconInput11Delay": falconInput11Delay,
       "falconInput12": falconInput12,
       "falconInput12State": falconInput12State,
       "falconInput12Reading": falconInput12Reading,
       "falconInput12Label": falconInput12Label,
       "falconInput12RlyControl": falconInput12RlyControl,
       "falconInput12Delay": falconInput12Delay,
       "falconInput13": falconInput13,
       "falconInput13State": falconInput13State,
       "falconInput13Reading": falconInput13Reading,
       "falconInput13Label": falconInput13Label,
       "falconInput13RlyControl": falconInput13RlyControl,
       "falconInput13Delay": falconInput13Delay,
       "falconInput14": falconInput14,
       "falconInput14State": falconInput14State,
       "falconInput14Reading": falconInput14Reading,
       "falconInput14Label": falconInput14Label,
       "falconInput14RlyControl": falconInput14RlyControl,
       "falconInput14Delay": falconInput14Delay,
       "falconInput15": falconInput15,
       "falconInput15State": falconInput15State,
       "falconInput15Reading": falconInput15Reading,
       "falconInput15Label": falconInput15Label,
       "falconInput15RlyControl": falconInput15RlyControl,
       "falconInput15Delay": falconInput15Delay,
       "falconInput16": falconInput16,
       "falconInput16State": falconInput16State,
       "falconInput16Reading": falconInput16Reading,
       "falconInput16Label": falconInput16Label,
       "falconInput16RlyControl": falconInput16RlyControl,
       "falconInput16Delay": falconInput16Delay,
       "falconInput17": falconInput17,
       "falconInput17State": falconInput17State,
       "falconInput17Reading": falconInput17Reading,
       "falconInput17Label": falconInput17Label,
       "falconInput17RlyControl": falconInput17RlyControl,
       "falconInput17Delay": falconInput17Delay,
       "falconInput18": falconInput18,
       "falconInput18State": falconInput18State,
       "falconInput18Reading": falconInput18Reading,
       "falconInput18Label": falconInput18Label,
       "falconInput18RlyControl": falconInput18RlyControl,
       "falconInput18Delay": falconInput18Delay,
       "falconInput19": falconInput19,
       "falconInput19State": falconInput19State,
       "falconInput19Reading": falconInput19Reading,
       "falconInput19Label": falconInput19Label,
       "falconInput19RlyControl": falconInput19RlyControl,
       "falconInput19Delay": falconInput19Delay,
       "falconInput20": falconInput20,
       "falconInput20State": falconInput20State,
       "falconInput20Reading": falconInput20Reading,
       "falconInput20Label": falconInput20Label,
       "falconInput20RlyControl": falconInput20RlyControl,
       "falconInput20Delay": falconInput20Delay,
       "falconOutputs": falconOutputs,
       "falconRelay1": falconRelay1,
       "falconRelay1State": falconRelay1State,
       "falconRelay1Status": falconRelay1Status,
       "falconRelay1Label": falconRelay1Label,
       "falconRelay1Time": falconRelay1Time,
       "falconRelay2": falconRelay2,
       "falconRelay2State": falconRelay2State,
       "falconRelay2Status": falconRelay2Status,
       "falconRelay2Label": falconRelay2Label,
       "falconRelay2Time": falconRelay2Time,
       "falconRelay3": falconRelay3,
       "falconRelay3State": falconRelay3State,
       "falconRelay3Status": falconRelay3Status,
       "falconRelay3Label": falconRelay3Label,
       "falconRelay3Time": falconRelay3Time,
       "falconRelay4": falconRelay4,
       "falconRelay4State": falconRelay4State,
       "falconRelay4Status": falconRelay4Status,
       "falconRelay4Label": falconRelay4Label,
       "falconRelay4Time": falconRelay4Time,
       "falconRelay5": falconRelay5,
       "falconRelay5State": falconRelay5State,
       "falconRelay5Status": falconRelay5Status,
       "falconRelay5Label": falconRelay5Label,
       "falconRelay5Time": falconRelay5Time,
       "falconRelay6": falconRelay6,
       "falconRelay6State": falconRelay6State,
       "falconRelay6Status": falconRelay6Status,
       "falconRelay6Label": falconRelay6Label,
       "falconRelay6Time": falconRelay6Time,
       "falconAlarms": falconAlarms,
       "falconAlarmsPresent": falconAlarmsPresent,
       "falconAlarmTable": falconAlarmTable,
       "falconAlarmEntry": falconAlarmEntry,
       "falconAlarmId": falconAlarmId,
       "falconAlarmDescr": falconAlarmDescr,
       "falconWellKnownAlarms": falconWellKnownAlarms,
       "falconInput1HighAlarm": falconInput1HighAlarm,
       "falconInput1LowAlarm": falconInput1LowAlarm,
       "falconInput1High2Alarm": falconInput1High2Alarm,
       "falconInput1Low2Alarm": falconInput1Low2Alarm,
       "falconInput2HighAlarm": falconInput2HighAlarm,
       "falconInput2LowAlarm": falconInput2LowAlarm,
       "falconInput2High2Alarm": falconInput2High2Alarm,
       "falconInput2Low2Alarm": falconInput2Low2Alarm,
       "falconInput3HighAlarm": falconInput3HighAlarm,
       "falconInput3LowAlarm": falconInput3LowAlarm,
       "falconInput3High2Alarm": falconInput3High2Alarm,
       "falconInput3Low2Alarm": falconInput3Low2Alarm,
       "falconInput4HighAlarm": falconInput4HighAlarm,
       "falconInput4LowAlarm": falconInput4LowAlarm,
       "falconInput4High2Alarm": falconInput4High2Alarm,
       "falconInput4Low2Alarm": falconInput4Low2Alarm,
       "falconInput5HighAlarm": falconInput5HighAlarm,
       "falconInput5LowAlarm": falconInput5LowAlarm,
       "falconInput5High2Alarm": falconInput5High2Alarm,
       "falconInput5Low2Alarm": falconInput5Low2Alarm,
       "falconInput6HighAlarm": falconInput6HighAlarm,
       "falconInput6LowAlarm": falconInput6LowAlarm,
       "falconInput6High2Alarm": falconInput6High2Alarm,
       "falconInput6Low2Alarm": falconInput6Low2Alarm,
       "falconInput7HighAlarm": falconInput7HighAlarm,
       "falconInput7LowAlarm": falconInput7LowAlarm,
       "falconInput7High2Alarm": falconInput7High2Alarm,
       "falconInput7Low2Alarm": falconInput7Low2Alarm,
       "falconInput8HighAlarm": falconInput8HighAlarm,
       "falconInput8LowAlarm": falconInput8LowAlarm,
       "falconInput8High2Alarm": falconInput8High2Alarm,
       "falconInput8Low2Alarm": falconInput8Low2Alarm,
       "falconInput1DigAlarm": falconInput1DigAlarm,
       "falconInput2DigAlarm": falconInput2DigAlarm,
       "falconInput3DigAlarm": falconInput3DigAlarm,
       "falconInput4DigAlarm": falconInput4DigAlarm,
       "falconInput5DigAlarm": falconInput5DigAlarm,
       "falconInput6DigAlarm": falconInput6DigAlarm,
       "falconInput7DigAlarm": falconInput7DigAlarm,
       "falconInput8DigAlarm": falconInput8DigAlarm,
       "falconInput9DigAlarm": falconInput9DigAlarm,
       "falconInput10DigAlarm": falconInput10DigAlarm,
       "falconInput11DigAlarm": falconInput11DigAlarm,
       "falconInput12DigAlarm": falconInput12DigAlarm,
       "falconInput13DigAlarm": falconInput13DigAlarm,
       "falconInput14DigAlarm": falconInput14DigAlarm,
       "falconInput15DigAlarm": falconInput15DigAlarm,
       "falconInput16DigAlarm": falconInput16DigAlarm,
       "falconInput17DigAlarm": falconInput17DigAlarm,
       "falconInput18DigAlarm": falconInput18DigAlarm,
       "falconInput19DigAlarm": falconInput19DigAlarm,
       "falconInput20DigAlarm": falconInput20DigAlarm,
       "falconOnBatteryAlarm": falconOnBatteryAlarm,
       "falconLowBatteryAlarm": falconLowBatteryAlarm,
       "falconTraps": falconTraps,
       "falconAlarmEntryAdded": falconAlarmEntryAdded,
       "falconAlarmEntryRemoved": falconAlarmEntryRemoved,
       "falconAccessGranted": falconAccessGranted,
       "falconAccessDenied": falconAccessDenied,
       "falconAlarmHistory": falconAlarmHistory,
       "falconAlarmHistoryEntries": falconAlarmHistoryEntries,
       "falconAlarmHistoryClear": falconAlarmHistoryClear,
       "falconAlarmHistoryTable": falconAlarmHistoryTable,
       "falconAlarmHistoryEntry": falconAlarmHistoryEntry,
       "falconAlarmHistoryId": falconAlarmHistoryId,
       "falconAlarmHistoryText": falconAlarmHistoryText,
       "falconTrapSettings": falconTrapSettings,
       "falconPersistantTraps": falconPersistantTraps,
       "falconAlarmAcknowledge": falconAlarmAcknowledge,
       "falcon8124": falcon8124}
)
