# SNMP MIB module (AISPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISPY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:22 2024
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

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSPY_ObjectIdentity = ObjectIdentity
aiSPY = _AiSPY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20)
)
_AiSPYIdent_ObjectIdentity = ObjectIdentity
aiSPYIdent = _AiSPYIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 1)
)
_AiSPYIdentManufacturer_Type = DisplayString
_AiSPYIdentManufacturer_Object = MibScalar
aiSPYIdentManufacturer = _AiSPYIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 1, 1),
    _AiSPYIdentManufacturer_Type()
)
aiSPYIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYIdentManufacturer.setStatus("mandatory")
_AiSPYIdentModel_Type = DisplayString
_AiSPYIdentModel_Object = MibScalar
aiSPYIdentModel = _AiSPYIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 1, 2),
    _AiSPYIdentModel_Type()
)
aiSPYIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYIdentModel.setStatus("mandatory")
_AiSPYIdentSoftwareVersion_Type = DisplayString
_AiSPYIdentSoftwareVersion_Object = MibScalar
aiSPYIdentSoftwareVersion = _AiSPYIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 1, 3),
    _AiSPYIdentSoftwareVersion_Type()
)
aiSPYIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYIdentSoftwareVersion.setStatus("mandatory")
_AiSPYIdentSpecific_Type = ObjectIdentifier
_AiSPYIdentSpecific_Object = MibScalar
aiSPYIdentSpecific = _AiSPYIdentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 1, 4),
    _AiSPYIdentSpecific_Type()
)
aiSPYIdentSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYIdentSpecific.setStatus("mandatory")
_AiSPYSystem_ObjectIdentity = ObjectIdentity
aiSPYSystem = _AiSPYSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 2)
)
_AiSPYClock_Type = DisplayString
_AiSPYClock_Object = MibScalar
aiSPYClock = _AiSPYClock_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 1),
    _AiSPYClock_Type()
)
aiSPYClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYClock.setStatus("mandatory")


class _AiSPYDoorAlarmBypass_Type(Integer32):
    """Custom type aiSPYDoorAlarmBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYDoorAlarmBypass_Type.__name__ = "Integer32"
_AiSPYDoorAlarmBypass_Object = MibScalar
aiSPYDoorAlarmBypass = _AiSPYDoorAlarmBypass_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 2),
    _AiSPYDoorAlarmBypass_Type()
)
aiSPYDoorAlarmBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYDoorAlarmBypass.setStatus("mandatory")
_AiSPYKeypad_ObjectIdentity = ObjectIdentity
aiSPYKeypad = _AiSPYKeypad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3)
)
_AiSPYKeypadCode1_Type = DisplayString
_AiSPYKeypadCode1_Object = MibScalar
aiSPYKeypadCode1 = _AiSPYKeypadCode1_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 1),
    _AiSPYKeypadCode1_Type()
)
aiSPYKeypadCode1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode1.setStatus("mandatory")
_AiSPYKeypadName1_Type = DisplayString
_AiSPYKeypadName1_Object = MibScalar
aiSPYKeypadName1 = _AiSPYKeypadName1_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 2),
    _AiSPYKeypadName1_Type()
)
aiSPYKeypadName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName1.setStatus("mandatory")
_AiSPYKeypadCode2_Type = DisplayString
_AiSPYKeypadCode2_Object = MibScalar
aiSPYKeypadCode2 = _AiSPYKeypadCode2_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 3),
    _AiSPYKeypadCode2_Type()
)
aiSPYKeypadCode2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode2.setStatus("mandatory")
_AiSPYKeypadName2_Type = DisplayString
_AiSPYKeypadName2_Object = MibScalar
aiSPYKeypadName2 = _AiSPYKeypadName2_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 4),
    _AiSPYKeypadName2_Type()
)
aiSPYKeypadName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName2.setStatus("mandatory")
_AiSPYKeypadCode3_Type = DisplayString
_AiSPYKeypadCode3_Object = MibScalar
aiSPYKeypadCode3 = _AiSPYKeypadCode3_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 5),
    _AiSPYKeypadCode3_Type()
)
aiSPYKeypadCode3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode3.setStatus("mandatory")
_AiSPYKeypadName3_Type = DisplayString
_AiSPYKeypadName3_Object = MibScalar
aiSPYKeypadName3 = _AiSPYKeypadName3_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 6),
    _AiSPYKeypadName3_Type()
)
aiSPYKeypadName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName3.setStatus("mandatory")
_AiSPYKeypadCode4_Type = DisplayString
_AiSPYKeypadCode4_Object = MibScalar
aiSPYKeypadCode4 = _AiSPYKeypadCode4_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 7),
    _AiSPYKeypadCode4_Type()
)
aiSPYKeypadCode4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode4.setStatus("mandatory")
_AiSPYKeypadName4_Type = DisplayString
_AiSPYKeypadName4_Object = MibScalar
aiSPYKeypadName4 = _AiSPYKeypadName4_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 8),
    _AiSPYKeypadName4_Type()
)
aiSPYKeypadName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName4.setStatus("mandatory")
_AiSPYKeypadCode5_Type = DisplayString
_AiSPYKeypadCode5_Object = MibScalar
aiSPYKeypadCode5 = _AiSPYKeypadCode5_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 9),
    _AiSPYKeypadCode5_Type()
)
aiSPYKeypadCode5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode5.setStatus("mandatory")
_AiSPYKeypadName5_Type = DisplayString
_AiSPYKeypadName5_Object = MibScalar
aiSPYKeypadName5 = _AiSPYKeypadName5_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 10),
    _AiSPYKeypadName5_Type()
)
aiSPYKeypadName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName5.setStatus("mandatory")
_AiSPYKeypadCode6_Type = DisplayString
_AiSPYKeypadCode6_Object = MibScalar
aiSPYKeypadCode6 = _AiSPYKeypadCode6_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 11),
    _AiSPYKeypadCode6_Type()
)
aiSPYKeypadCode6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode6.setStatus("mandatory")
_AiSPYKeypadName6_Type = DisplayString
_AiSPYKeypadName6_Object = MibScalar
aiSPYKeypadName6 = _AiSPYKeypadName6_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 12),
    _AiSPYKeypadName6_Type()
)
aiSPYKeypadName6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName6.setStatus("mandatory")
_AiSPYKeypadCode7_Type = DisplayString
_AiSPYKeypadCode7_Object = MibScalar
aiSPYKeypadCode7 = _AiSPYKeypadCode7_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 13),
    _AiSPYKeypadCode7_Type()
)
aiSPYKeypadCode7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode7.setStatus("mandatory")
_AiSPYKeypadName7_Type = DisplayString
_AiSPYKeypadName7_Object = MibScalar
aiSPYKeypadName7 = _AiSPYKeypadName7_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 14),
    _AiSPYKeypadName7_Type()
)
aiSPYKeypadName7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName7.setStatus("mandatory")
_AiSPYKeypadCode8_Type = DisplayString
_AiSPYKeypadCode8_Object = MibScalar
aiSPYKeypadCode8 = _AiSPYKeypadCode8_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 15),
    _AiSPYKeypadCode8_Type()
)
aiSPYKeypadCode8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode8.setStatus("mandatory")
_AiSPYKeypadName8_Type = DisplayString
_AiSPYKeypadName8_Object = MibScalar
aiSPYKeypadName8 = _AiSPYKeypadName8_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 16),
    _AiSPYKeypadName8_Type()
)
aiSPYKeypadName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName8.setStatus("mandatory")
_AiSPYKeypadCode9_Type = DisplayString
_AiSPYKeypadCode9_Object = MibScalar
aiSPYKeypadCode9 = _AiSPYKeypadCode9_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 17),
    _AiSPYKeypadCode9_Type()
)
aiSPYKeypadCode9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode9.setStatus("mandatory")
_AiSPYKeypadName9_Type = DisplayString
_AiSPYKeypadName9_Object = MibScalar
aiSPYKeypadName9 = _AiSPYKeypadName9_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 18),
    _AiSPYKeypadName9_Type()
)
aiSPYKeypadName9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName9.setStatus("mandatory")
_AiSPYKeypadCode10_Type = DisplayString
_AiSPYKeypadCode10_Object = MibScalar
aiSPYKeypadCode10 = _AiSPYKeypadCode10_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 19),
    _AiSPYKeypadCode10_Type()
)
aiSPYKeypadCode10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode10.setStatus("mandatory")
_AiSPYKeypadName10_Type = DisplayString
_AiSPYKeypadName10_Object = MibScalar
aiSPYKeypadName10 = _AiSPYKeypadName10_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 20),
    _AiSPYKeypadName10_Type()
)
aiSPYKeypadName10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName10.setStatus("mandatory")
_AiSPYKeypadCode11_Type = DisplayString
_AiSPYKeypadCode11_Object = MibScalar
aiSPYKeypadCode11 = _AiSPYKeypadCode11_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 21),
    _AiSPYKeypadCode11_Type()
)
aiSPYKeypadCode11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode11.setStatus("mandatory")
_AiSPYKeypadName11_Type = DisplayString
_AiSPYKeypadName11_Object = MibScalar
aiSPYKeypadName11 = _AiSPYKeypadName11_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 22),
    _AiSPYKeypadName11_Type()
)
aiSPYKeypadName11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName11.setStatus("mandatory")
_AiSPYKeypadCode12_Type = DisplayString
_AiSPYKeypadCode12_Object = MibScalar
aiSPYKeypadCode12 = _AiSPYKeypadCode12_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 23),
    _AiSPYKeypadCode12_Type()
)
aiSPYKeypadCode12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode12.setStatus("mandatory")
_AiSPYKeypadName12_Type = DisplayString
_AiSPYKeypadName12_Object = MibScalar
aiSPYKeypadName12 = _AiSPYKeypadName12_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 24),
    _AiSPYKeypadName12_Type()
)
aiSPYKeypadName12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName12.setStatus("mandatory")
_AiSPYKeypadCode13_Type = DisplayString
_AiSPYKeypadCode13_Object = MibScalar
aiSPYKeypadCode13 = _AiSPYKeypadCode13_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 25),
    _AiSPYKeypadCode13_Type()
)
aiSPYKeypadCode13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode13.setStatus("mandatory")
_AiSPYKeypadName13_Type = DisplayString
_AiSPYKeypadName13_Object = MibScalar
aiSPYKeypadName13 = _AiSPYKeypadName13_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 26),
    _AiSPYKeypadName13_Type()
)
aiSPYKeypadName13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName13.setStatus("mandatory")
_AiSPYKeypadCode14_Type = DisplayString
_AiSPYKeypadCode14_Object = MibScalar
aiSPYKeypadCode14 = _AiSPYKeypadCode14_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 27),
    _AiSPYKeypadCode14_Type()
)
aiSPYKeypadCode14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode14.setStatus("mandatory")
_AiSPYKeypadName14_Type = DisplayString
_AiSPYKeypadName14_Object = MibScalar
aiSPYKeypadName14 = _AiSPYKeypadName14_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 28),
    _AiSPYKeypadName14_Type()
)
aiSPYKeypadName14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName14.setStatus("mandatory")
_AiSPYKeypadCode15_Type = DisplayString
_AiSPYKeypadCode15_Object = MibScalar
aiSPYKeypadCode15 = _AiSPYKeypadCode15_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 29),
    _AiSPYKeypadCode15_Type()
)
aiSPYKeypadCode15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode15.setStatus("mandatory")
_AiSPYKeypadName15_Type = DisplayString
_AiSPYKeypadName15_Object = MibScalar
aiSPYKeypadName15 = _AiSPYKeypadName15_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 30),
    _AiSPYKeypadName15_Type()
)
aiSPYKeypadName15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName15.setStatus("mandatory")
_AiSPYKeypadCode16_Type = DisplayString
_AiSPYKeypadCode16_Object = MibScalar
aiSPYKeypadCode16 = _AiSPYKeypadCode16_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 31),
    _AiSPYKeypadCode16_Type()
)
aiSPYKeypadCode16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode16.setStatus("mandatory")
_AiSPYKeypadName16_Type = DisplayString
_AiSPYKeypadName16_Object = MibScalar
aiSPYKeypadName16 = _AiSPYKeypadName16_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 32),
    _AiSPYKeypadName16_Type()
)
aiSPYKeypadName16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName16.setStatus("mandatory")
_AiSPYKeypadCode17_Type = DisplayString
_AiSPYKeypadCode17_Object = MibScalar
aiSPYKeypadCode17 = _AiSPYKeypadCode17_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 33),
    _AiSPYKeypadCode17_Type()
)
aiSPYKeypadCode17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode17.setStatus("mandatory")
_AiSPYKeypadName17_Type = DisplayString
_AiSPYKeypadName17_Object = MibScalar
aiSPYKeypadName17 = _AiSPYKeypadName17_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 34),
    _AiSPYKeypadName17_Type()
)
aiSPYKeypadName17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName17.setStatus("mandatory")
_AiSPYKeypadCode18_Type = DisplayString
_AiSPYKeypadCode18_Object = MibScalar
aiSPYKeypadCode18 = _AiSPYKeypadCode18_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 35),
    _AiSPYKeypadCode18_Type()
)
aiSPYKeypadCode18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode18.setStatus("mandatory")
_AiSPYKeypadName18_Type = DisplayString
_AiSPYKeypadName18_Object = MibScalar
aiSPYKeypadName18 = _AiSPYKeypadName18_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 36),
    _AiSPYKeypadName18_Type()
)
aiSPYKeypadName18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName18.setStatus("mandatory")
_AiSPYKeypadCode19_Type = DisplayString
_AiSPYKeypadCode19_Object = MibScalar
aiSPYKeypadCode19 = _AiSPYKeypadCode19_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 37),
    _AiSPYKeypadCode19_Type()
)
aiSPYKeypadCode19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode19.setStatus("mandatory")
_AiSPYKeypadName19_Type = DisplayString
_AiSPYKeypadName19_Object = MibScalar
aiSPYKeypadName19 = _AiSPYKeypadName19_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 38),
    _AiSPYKeypadName19_Type()
)
aiSPYKeypadName19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName19.setStatus("mandatory")
_AiSPYKeypadCode20_Type = DisplayString
_AiSPYKeypadCode20_Object = MibScalar
aiSPYKeypadCode20 = _AiSPYKeypadCode20_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 39),
    _AiSPYKeypadCode20_Type()
)
aiSPYKeypadCode20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadCode20.setStatus("mandatory")
_AiSPYKeypadName20_Type = DisplayString
_AiSPYKeypadName20_Object = MibScalar
aiSPYKeypadName20 = _AiSPYKeypadName20_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 3, 40),
    _AiSPYKeypadName20_Type()
)
aiSPYKeypadName20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYKeypadName20.setStatus("mandatory")


class _AiSPYInputVoltage_Type(Integer32):
    """Custom type aiSPYInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInputVoltage_Type.__name__ = "Integer32"
_AiSPYInputVoltage_Object = MibScalar
aiSPYInputVoltage = _AiSPYInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 4),
    _AiSPYInputVoltage_Type()
)
aiSPYInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInputVoltage.setStatus("mandatory")


class _AiSPYOnBattery_Type(Integer32):
    """Custom type aiSPYOnBattery based on Integer32"""
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


_AiSPYOnBattery_Type.__name__ = "Integer32"
_AiSPYOnBattery_Object = MibScalar
aiSPYOnBattery = _AiSPYOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 5),
    _AiSPYOnBattery_Type()
)
aiSPYOnBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYOnBattery.setStatus("mandatory")


class _AiSPYLowBatteryThreshold_Type(Integer32):
    """Custom type aiSPYLowBatteryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYLowBatteryThreshold_Type.__name__ = "Integer32"
_AiSPYLowBatteryThreshold_Object = MibScalar
aiSPYLowBatteryThreshold = _AiSPYLowBatteryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 6),
    _AiSPYLowBatteryThreshold_Type()
)
aiSPYLowBatteryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYLowBatteryThreshold.setStatus("mandatory")


class _AiSPYAnalogAverage_Type(Integer32):
    """Custom type aiSPYAnalogAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AiSPYAnalogAverage_Type.__name__ = "Integer32"
_AiSPYAnalogAverage_Object = MibScalar
aiSPYAnalogAverage = _AiSPYAnalogAverage_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 2, 7),
    _AiSPYAnalogAverage_Type()
)
aiSPYAnalogAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYAnalogAverage.setStatus("mandatory")
_AiSPYInputs_ObjectIdentity = ObjectIdentity
aiSPYInputs = _AiSPYInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3)
)
_AiSPY8124_ObjectIdentity = ObjectIdentity
aiSPY8124 = _AiSPY8124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3)
)
_AiSPYInput1_ObjectIdentity = ObjectIdentity
aiSPYInput1 = _AiSPYInput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1)
)


class _AiSPYInput1State_Type(Integer32):
    """Custom type aiSPYInput1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog-4to20-installed", 2),
          ("notinstalled", 1))
    )


_AiSPYInput1State_Type.__name__ = "Integer32"
_AiSPYInput1State_Object = MibScalar
aiSPYInput1State = _AiSPYInput1State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 1),
    _AiSPYInput1State_Type()
)
aiSPYInput1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1State.setStatus("mandatory")


class _AiSPYInput1Reading_Type(Integer32):
    """Custom type aiSPYInput1Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput1Reading_Type.__name__ = "Integer32"
_AiSPYInput1Reading_Object = MibScalar
aiSPYInput1Reading = _AiSPYInput1Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 2),
    _AiSPYInput1Reading_Type()
)
aiSPYInput1Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput1Reading.setStatus("mandatory")


class _AiSPYInput1Gain_Type(Integer32):
    """Custom type aiSPYInput1Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput1Gain_Type.__name__ = "Integer32"
_AiSPYInput1Gain_Object = MibScalar
aiSPYInput1Gain = _AiSPYInput1Gain_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 3),
    _AiSPYInput1Gain_Type()
)
aiSPYInput1Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1Gain.setStatus("mandatory")


class _AiSPYInput1Offset_Type(Integer32):
    """Custom type aiSPYInput1Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput1Offset_Type.__name__ = "Integer32"
_AiSPYInput1Offset_Object = MibScalar
aiSPYInput1Offset = _AiSPYInput1Offset_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 4),
    _AiSPYInput1Offset_Type()
)
aiSPYInput1Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1Offset.setStatus("mandatory")
_AiSPYInput1Label_Type = DisplayString
_AiSPYInput1Label_Object = MibScalar
aiSPYInput1Label = _AiSPYInput1Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 5),
    _AiSPYInput1Label_Type()
)
aiSPYInput1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1Label.setStatus("mandatory")
_AiSPYInput1UOM_Type = DisplayString
_AiSPYInput1UOM_Object = MibScalar
aiSPYInput1UOM = _AiSPYInput1UOM_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 6),
    _AiSPYInput1UOM_Type()
)
aiSPYInput1UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1UOM.setStatus("mandatory")


class _AiSPYInput1HighLimit_Type(Integer32):
    """Custom type aiSPYInput1HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput1HighLimit_Type.__name__ = "Integer32"
_AiSPYInput1HighLimit_Object = MibScalar
aiSPYInput1HighLimit = _AiSPYInput1HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 7),
    _AiSPYInput1HighLimit_Type()
)
aiSPYInput1HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1HighLimit.setStatus("mandatory")


class _AiSPYInput1LowLimit_Type(Integer32):
    """Custom type aiSPYInput1LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput1LowLimit_Type.__name__ = "Integer32"
_AiSPYInput1LowLimit_Object = MibScalar
aiSPYInput1LowLimit = _AiSPYInput1LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 8),
    _AiSPYInput1LowLimit_Type()
)
aiSPYInput1LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1LowLimit.setStatus("mandatory")


class _AiSPYInput1RlyControl_Type(Integer32):
    """Custom type aiSPYInput1RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput1RlyControl_Type.__name__ = "Integer32"
_AiSPYInput1RlyControl_Object = MibScalar
aiSPYInput1RlyControl = _AiSPYInput1RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 9),
    _AiSPYInput1RlyControl_Type()
)
aiSPYInput1RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1RlyControl.setStatus("mandatory")


class _AiSPYInput1Delay_Type(Integer32):
    """Custom type aiSPYInput1Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput1Delay_Type.__name__ = "Integer32"
_AiSPYInput1Delay_Object = MibScalar
aiSPYInput1Delay = _AiSPYInput1Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 10),
    _AiSPYInput1Delay_Type()
)
aiSPYInput1Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1Delay.setStatus("mandatory")


class _AiSPYInput1RTNDelay_Type(Integer32):
    """Custom type aiSPYInput1RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput1RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput1RTNDelay_Object = MibScalar
aiSPYInput1RTNDelay = _AiSPYInput1RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 11),
    _AiSPYInput1RTNDelay_Type()
)
aiSPYInput1RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1RTNDelay.setStatus("mandatory")


class _AiSPYInput1Hysteresis_Type(Integer32):
    """Custom type aiSPYInput1Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AiSPYInput1Hysteresis_Type.__name__ = "Integer32"
_AiSPYInput1Hysteresis_Object = MibScalar
aiSPYInput1Hysteresis = _AiSPYInput1Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 1, 12),
    _AiSPYInput1Hysteresis_Type()
)
aiSPYInput1Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput1Hysteresis.setStatus("mandatory")
_AiSPYInput2_ObjectIdentity = ObjectIdentity
aiSPYInput2 = _AiSPYInput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2)
)


class _AiSPYInput2State_Type(Integer32):
    """Custom type aiSPYInput2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog-4to20-installed", 2),
          ("notInstalled", 1))
    )


_AiSPYInput2State_Type.__name__ = "Integer32"
_AiSPYInput2State_Object = MibScalar
aiSPYInput2State = _AiSPYInput2State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 1),
    _AiSPYInput2State_Type()
)
aiSPYInput2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2State.setStatus("mandatory")


class _AiSPYInput2Reading_Type(Integer32):
    """Custom type aiSPYInput2Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput2Reading_Type.__name__ = "Integer32"
_AiSPYInput2Reading_Object = MibScalar
aiSPYInput2Reading = _AiSPYInput2Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 2),
    _AiSPYInput2Reading_Type()
)
aiSPYInput2Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput2Reading.setStatus("mandatory")


class _AiSPYInput2Gain_Type(Integer32):
    """Custom type aiSPYInput2Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput2Gain_Type.__name__ = "Integer32"
_AiSPYInput2Gain_Object = MibScalar
aiSPYInput2Gain = _AiSPYInput2Gain_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 3),
    _AiSPYInput2Gain_Type()
)
aiSPYInput2Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2Gain.setStatus("mandatory")


class _AiSPYInput2Offset_Type(Integer32):
    """Custom type aiSPYInput2Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput2Offset_Type.__name__ = "Integer32"
_AiSPYInput2Offset_Object = MibScalar
aiSPYInput2Offset = _AiSPYInput2Offset_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 4),
    _AiSPYInput2Offset_Type()
)
aiSPYInput2Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2Offset.setStatus("mandatory")
_AiSPYInput2Label_Type = DisplayString
_AiSPYInput2Label_Object = MibScalar
aiSPYInput2Label = _AiSPYInput2Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 5),
    _AiSPYInput2Label_Type()
)
aiSPYInput2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2Label.setStatus("mandatory")
_AiSPYInput2UOM_Type = DisplayString
_AiSPYInput2UOM_Object = MibScalar
aiSPYInput2UOM = _AiSPYInput2UOM_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 6),
    _AiSPYInput2UOM_Type()
)
aiSPYInput2UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2UOM.setStatus("mandatory")


class _AiSPYInput2HighLimit_Type(Integer32):
    """Custom type aiSPYInput2HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput2HighLimit_Type.__name__ = "Integer32"
_AiSPYInput2HighLimit_Object = MibScalar
aiSPYInput2HighLimit = _AiSPYInput2HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 7),
    _AiSPYInput2HighLimit_Type()
)
aiSPYInput2HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2HighLimit.setStatus("mandatory")


class _AiSPYInput2LowLimit_Type(Integer32):
    """Custom type aiSPYInput2LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput2LowLimit_Type.__name__ = "Integer32"
_AiSPYInput2LowLimit_Object = MibScalar
aiSPYInput2LowLimit = _AiSPYInput2LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 8),
    _AiSPYInput2LowLimit_Type()
)
aiSPYInput2LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2LowLimit.setStatus("mandatory")


class _AiSPYInput2RlyControl_Type(Integer32):
    """Custom type aiSPYInput2RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput2RlyControl_Type.__name__ = "Integer32"
_AiSPYInput2RlyControl_Object = MibScalar
aiSPYInput2RlyControl = _AiSPYInput2RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 9),
    _AiSPYInput2RlyControl_Type()
)
aiSPYInput2RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2RlyControl.setStatus("mandatory")


class _AiSPYInput2Delay_Type(Integer32):
    """Custom type aiSPYInput2Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput2Delay_Type.__name__ = "Integer32"
_AiSPYInput2Delay_Object = MibScalar
aiSPYInput2Delay = _AiSPYInput2Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 10),
    _AiSPYInput2Delay_Type()
)
aiSPYInput2Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2Delay.setStatus("mandatory")


class _AiSPYInput2RTNDelay_Type(Integer32):
    """Custom type aiSPYInput2RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput2RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput2RTNDelay_Object = MibScalar
aiSPYInput2RTNDelay = _AiSPYInput2RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 11),
    _AiSPYInput2RTNDelay_Type()
)
aiSPYInput2RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2RTNDelay.setStatus("mandatory")


class _AiSPYInput2Hysteresis_Type(Integer32):
    """Custom type aiSPYInput2Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AiSPYInput2Hysteresis_Type.__name__ = "Integer32"
_AiSPYInput2Hysteresis_Object = MibScalar
aiSPYInput2Hysteresis = _AiSPYInput2Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 2, 12),
    _AiSPYInput2Hysteresis_Type()
)
aiSPYInput2Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput2Hysteresis.setStatus("mandatory")
_AiSPYInput3_ObjectIdentity = ObjectIdentity
aiSPYInput3 = _AiSPYInput3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3)
)


class _AiSPYInput3State_Type(Integer32):
    """Custom type aiSPYInput3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog-4to20-installed", 2),
          ("notInstalled", 1))
    )


_AiSPYInput3State_Type.__name__ = "Integer32"
_AiSPYInput3State_Object = MibScalar
aiSPYInput3State = _AiSPYInput3State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 1),
    _AiSPYInput3State_Type()
)
aiSPYInput3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3State.setStatus("mandatory")


class _AiSPYInput3Reading_Type(Integer32):
    """Custom type aiSPYInput3Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput3Reading_Type.__name__ = "Integer32"
_AiSPYInput3Reading_Object = MibScalar
aiSPYInput3Reading = _AiSPYInput3Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 2),
    _AiSPYInput3Reading_Type()
)
aiSPYInput3Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput3Reading.setStatus("mandatory")


class _AiSPYInput3Gain_Type(Integer32):
    """Custom type aiSPYInput3Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput3Gain_Type.__name__ = "Integer32"
_AiSPYInput3Gain_Object = MibScalar
aiSPYInput3Gain = _AiSPYInput3Gain_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 3),
    _AiSPYInput3Gain_Type()
)
aiSPYInput3Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3Gain.setStatus("mandatory")


class _AiSPYInput3Offset_Type(Integer32):
    """Custom type aiSPYInput3Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput3Offset_Type.__name__ = "Integer32"
_AiSPYInput3Offset_Object = MibScalar
aiSPYInput3Offset = _AiSPYInput3Offset_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 4),
    _AiSPYInput3Offset_Type()
)
aiSPYInput3Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3Offset.setStatus("mandatory")
_AiSPYInput3Label_Type = DisplayString
_AiSPYInput3Label_Object = MibScalar
aiSPYInput3Label = _AiSPYInput3Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 5),
    _AiSPYInput3Label_Type()
)
aiSPYInput3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3Label.setStatus("mandatory")
_AiSPYInput3UOM_Type = DisplayString
_AiSPYInput3UOM_Object = MibScalar
aiSPYInput3UOM = _AiSPYInput3UOM_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 6),
    _AiSPYInput3UOM_Type()
)
aiSPYInput3UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3UOM.setStatus("mandatory")


class _AiSPYInput3HighLimit_Type(Integer32):
    """Custom type aiSPYInput3HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput3HighLimit_Type.__name__ = "Integer32"
_AiSPYInput3HighLimit_Object = MibScalar
aiSPYInput3HighLimit = _AiSPYInput3HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 7),
    _AiSPYInput3HighLimit_Type()
)
aiSPYInput3HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3HighLimit.setStatus("mandatory")


class _AiSPYInput3LowLimit_Type(Integer32):
    """Custom type aiSPYInput3LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput3LowLimit_Type.__name__ = "Integer32"
_AiSPYInput3LowLimit_Object = MibScalar
aiSPYInput3LowLimit = _AiSPYInput3LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 8),
    _AiSPYInput3LowLimit_Type()
)
aiSPYInput3LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3LowLimit.setStatus("mandatory")


class _AiSPYInput3RlyControl_Type(Integer32):
    """Custom type aiSPYInput3RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput3RlyControl_Type.__name__ = "Integer32"
_AiSPYInput3RlyControl_Object = MibScalar
aiSPYInput3RlyControl = _AiSPYInput3RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 9),
    _AiSPYInput3RlyControl_Type()
)
aiSPYInput3RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3RlyControl.setStatus("mandatory")


class _AiSPYInput3Delay_Type(Integer32):
    """Custom type aiSPYInput3Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput3Delay_Type.__name__ = "Integer32"
_AiSPYInput3Delay_Object = MibScalar
aiSPYInput3Delay = _AiSPYInput3Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 10),
    _AiSPYInput3Delay_Type()
)
aiSPYInput3Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3Delay.setStatus("mandatory")


class _AiSPYInput3RTNDelay_Type(Integer32):
    """Custom type aiSPYInput3RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput3RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput3RTNDelay_Object = MibScalar
aiSPYInput3RTNDelay = _AiSPYInput3RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 11),
    _AiSPYInput3RTNDelay_Type()
)
aiSPYInput3RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3RTNDelay.setStatus("mandatory")


class _AiSPYInput3Hysteresis_Type(Integer32):
    """Custom type aiSPYInput3Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AiSPYInput3Hysteresis_Type.__name__ = "Integer32"
_AiSPYInput3Hysteresis_Object = MibScalar
aiSPYInput3Hysteresis = _AiSPYInput3Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 3, 12),
    _AiSPYInput3Hysteresis_Type()
)
aiSPYInput3Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput3Hysteresis.setStatus("mandatory")
_AiSPYInput4_ObjectIdentity = ObjectIdentity
aiSPYInput4 = _AiSPYInput4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4)
)


class _AiSPYInput4State_Type(Integer32):
    """Custom type aiSPYInput4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog-4to20-installed", 2),
          ("notInstalled", 1))
    )


_AiSPYInput4State_Type.__name__ = "Integer32"
_AiSPYInput4State_Object = MibScalar
aiSPYInput4State = _AiSPYInput4State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 1),
    _AiSPYInput4State_Type()
)
aiSPYInput4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4State.setStatus("mandatory")


class _AiSPYInput4Reading_Type(Integer32):
    """Custom type aiSPYInput4Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput4Reading_Type.__name__ = "Integer32"
_AiSPYInput4Reading_Object = MibScalar
aiSPYInput4Reading = _AiSPYInput4Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 2),
    _AiSPYInput4Reading_Type()
)
aiSPYInput4Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput4Reading.setStatus("mandatory")


class _AiSPYInput4Gain_Type(Integer32):
    """Custom type aiSPYInput4Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput4Gain_Type.__name__ = "Integer32"
_AiSPYInput4Gain_Object = MibScalar
aiSPYInput4Gain = _AiSPYInput4Gain_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 3),
    _AiSPYInput4Gain_Type()
)
aiSPYInput4Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4Gain.setStatus("mandatory")


class _AiSPYInput4Offset_Type(Integer32):
    """Custom type aiSPYInput4Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput4Offset_Type.__name__ = "Integer32"
_AiSPYInput4Offset_Object = MibScalar
aiSPYInput4Offset = _AiSPYInput4Offset_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 4),
    _AiSPYInput4Offset_Type()
)
aiSPYInput4Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4Offset.setStatus("mandatory")
_AiSPYInput4Label_Type = DisplayString
_AiSPYInput4Label_Object = MibScalar
aiSPYInput4Label = _AiSPYInput4Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 5),
    _AiSPYInput4Label_Type()
)
aiSPYInput4Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4Label.setStatus("mandatory")
_AiSPYInput4UOM_Type = DisplayString
_AiSPYInput4UOM_Object = MibScalar
aiSPYInput4UOM = _AiSPYInput4UOM_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 6),
    _AiSPYInput4UOM_Type()
)
aiSPYInput4UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4UOM.setStatus("mandatory")


class _AiSPYInput4HighLimit_Type(Integer32):
    """Custom type aiSPYInput4HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput4HighLimit_Type.__name__ = "Integer32"
_AiSPYInput4HighLimit_Object = MibScalar
aiSPYInput4HighLimit = _AiSPYInput4HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 7),
    _AiSPYInput4HighLimit_Type()
)
aiSPYInput4HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4HighLimit.setStatus("mandatory")


class _AiSPYInput4LowLimit_Type(Integer32):
    """Custom type aiSPYInput4LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput4LowLimit_Type.__name__ = "Integer32"
_AiSPYInput4LowLimit_Object = MibScalar
aiSPYInput4LowLimit = _AiSPYInput4LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 8),
    _AiSPYInput4LowLimit_Type()
)
aiSPYInput4LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4LowLimit.setStatus("mandatory")


class _AiSPYInput4RlyControl_Type(Integer32):
    """Custom type aiSPYInput4RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput4RlyControl_Type.__name__ = "Integer32"
_AiSPYInput4RlyControl_Object = MibScalar
aiSPYInput4RlyControl = _AiSPYInput4RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 9),
    _AiSPYInput4RlyControl_Type()
)
aiSPYInput4RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4RlyControl.setStatus("mandatory")


class _AiSPYInput4Delay_Type(Integer32):
    """Custom type aiSPYInput4Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput4Delay_Type.__name__ = "Integer32"
_AiSPYInput4Delay_Object = MibScalar
aiSPYInput4Delay = _AiSPYInput4Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 10),
    _AiSPYInput4Delay_Type()
)
aiSPYInput4Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4Delay.setStatus("mandatory")


class _AiSPYInput4RTNDelay_Type(Integer32):
    """Custom type aiSPYInput4RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput4RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput4RTNDelay_Object = MibScalar
aiSPYInput4RTNDelay = _AiSPYInput4RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 11),
    _AiSPYInput4RTNDelay_Type()
)
aiSPYInput4RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4RTNDelay.setStatus("mandatory")


class _AiSPYInput4Hysteresis_Type(Integer32):
    """Custom type aiSPYInput4Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AiSPYInput4Hysteresis_Type.__name__ = "Integer32"
_AiSPYInput4Hysteresis_Object = MibScalar
aiSPYInput4Hysteresis = _AiSPYInput4Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 4, 12),
    _AiSPYInput4Hysteresis_Type()
)
aiSPYInput4Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput4Hysteresis.setStatus("mandatory")
_AiSPYInput5_ObjectIdentity = ObjectIdentity
aiSPYInput5 = _AiSPYInput5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5)
)


class _AiSPYInput5State_Type(Integer32):
    """Custom type aiSPYInput5State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog-4to20-installed", 2),
          ("notInstalled", 1))
    )


_AiSPYInput5State_Type.__name__ = "Integer32"
_AiSPYInput5State_Object = MibScalar
aiSPYInput5State = _AiSPYInput5State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 1),
    _AiSPYInput5State_Type()
)
aiSPYInput5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5State.setStatus("mandatory")


class _AiSPYInput5Reading_Type(Integer32):
    """Custom type aiSPYInput5Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput5Reading_Type.__name__ = "Integer32"
_AiSPYInput5Reading_Object = MibScalar
aiSPYInput5Reading = _AiSPYInput5Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 2),
    _AiSPYInput5Reading_Type()
)
aiSPYInput5Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput5Reading.setStatus("mandatory")


class _AiSPYInput5Gain_Type(Integer32):
    """Custom type aiSPYInput5Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput5Gain_Type.__name__ = "Integer32"
_AiSPYInput5Gain_Object = MibScalar
aiSPYInput5Gain = _AiSPYInput5Gain_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 3),
    _AiSPYInput5Gain_Type()
)
aiSPYInput5Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5Gain.setStatus("mandatory")


class _AiSPYInput5Offset_Type(Integer32):
    """Custom type aiSPYInput5Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput5Offset_Type.__name__ = "Integer32"
_AiSPYInput5Offset_Object = MibScalar
aiSPYInput5Offset = _AiSPYInput5Offset_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 4),
    _AiSPYInput5Offset_Type()
)
aiSPYInput5Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5Offset.setStatus("mandatory")
_AiSPYInput5Label_Type = DisplayString
_AiSPYInput5Label_Object = MibScalar
aiSPYInput5Label = _AiSPYInput5Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 5),
    _AiSPYInput5Label_Type()
)
aiSPYInput5Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5Label.setStatus("mandatory")
_AiSPYInput5UOM_Type = DisplayString
_AiSPYInput5UOM_Object = MibScalar
aiSPYInput5UOM = _AiSPYInput5UOM_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 6),
    _AiSPYInput5UOM_Type()
)
aiSPYInput5UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5UOM.setStatus("mandatory")


class _AiSPYInput5HighLimit_Type(Integer32):
    """Custom type aiSPYInput5HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput5HighLimit_Type.__name__ = "Integer32"
_AiSPYInput5HighLimit_Object = MibScalar
aiSPYInput5HighLimit = _AiSPYInput5HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 7),
    _AiSPYInput5HighLimit_Type()
)
aiSPYInput5HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5HighLimit.setStatus("mandatory")


class _AiSPYInput5LowLimit_Type(Integer32):
    """Custom type aiSPYInput5LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput5LowLimit_Type.__name__ = "Integer32"
_AiSPYInput5LowLimit_Object = MibScalar
aiSPYInput5LowLimit = _AiSPYInput5LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 8),
    _AiSPYInput5LowLimit_Type()
)
aiSPYInput5LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5LowLimit.setStatus("mandatory")


class _AiSPYInput5RlyControl_Type(Integer32):
    """Custom type aiSPYInput5RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput5RlyControl_Type.__name__ = "Integer32"
_AiSPYInput5RlyControl_Object = MibScalar
aiSPYInput5RlyControl = _AiSPYInput5RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 9),
    _AiSPYInput5RlyControl_Type()
)
aiSPYInput5RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5RlyControl.setStatus("mandatory")


class _AiSPYInput5Delay_Type(Integer32):
    """Custom type aiSPYInput5Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput5Delay_Type.__name__ = "Integer32"
_AiSPYInput5Delay_Object = MibScalar
aiSPYInput5Delay = _AiSPYInput5Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 10),
    _AiSPYInput5Delay_Type()
)
aiSPYInput5Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5Delay.setStatus("mandatory")


class _AiSPYInput5RTNDelay_Type(Integer32):
    """Custom type aiSPYInput5RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput5RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput5RTNDelay_Object = MibScalar
aiSPYInput5RTNDelay = _AiSPYInput5RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 11),
    _AiSPYInput5RTNDelay_Type()
)
aiSPYInput5RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5RTNDelay.setStatus("mandatory")


class _AiSPYInput5Hysteresis_Type(Integer32):
    """Custom type aiSPYInput5Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AiSPYInput5Hysteresis_Type.__name__ = "Integer32"
_AiSPYInput5Hysteresis_Object = MibScalar
aiSPYInput5Hysteresis = _AiSPYInput5Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 5, 12),
    _AiSPYInput5Hysteresis_Type()
)
aiSPYInput5Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput5Hysteresis.setStatus("mandatory")
_AiSPYInput6_ObjectIdentity = ObjectIdentity
aiSPYInput6 = _AiSPYInput6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6)
)


class _AiSPYInput6State_Type(Integer32):
    """Custom type aiSPYInput6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog-4to20-installed", 2),
          ("notInstalled", 1))
    )


_AiSPYInput6State_Type.__name__ = "Integer32"
_AiSPYInput6State_Object = MibScalar
aiSPYInput6State = _AiSPYInput6State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 1),
    _AiSPYInput6State_Type()
)
aiSPYInput6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6State.setStatus("mandatory")


class _AiSPYInput6Reading_Type(Integer32):
    """Custom type aiSPYInput6Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput6Reading_Type.__name__ = "Integer32"
_AiSPYInput6Reading_Object = MibScalar
aiSPYInput6Reading = _AiSPYInput6Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 2),
    _AiSPYInput6Reading_Type()
)
aiSPYInput6Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput6Reading.setStatus("mandatory")


class _AiSPYInput6Gain_Type(Integer32):
    """Custom type aiSPYInput6Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput6Gain_Type.__name__ = "Integer32"
_AiSPYInput6Gain_Object = MibScalar
aiSPYInput6Gain = _AiSPYInput6Gain_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 3),
    _AiSPYInput6Gain_Type()
)
aiSPYInput6Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6Gain.setStatus("mandatory")


class _AiSPYInput6Offset_Type(Integer32):
    """Custom type aiSPYInput6Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput6Offset_Type.__name__ = "Integer32"
_AiSPYInput6Offset_Object = MibScalar
aiSPYInput6Offset = _AiSPYInput6Offset_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 4),
    _AiSPYInput6Offset_Type()
)
aiSPYInput6Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6Offset.setStatus("mandatory")
_AiSPYInput6Label_Type = DisplayString
_AiSPYInput6Label_Object = MibScalar
aiSPYInput6Label = _AiSPYInput6Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 5),
    _AiSPYInput6Label_Type()
)
aiSPYInput6Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6Label.setStatus("mandatory")
_AiSPYInput6UOM_Type = DisplayString
_AiSPYInput6UOM_Object = MibScalar
aiSPYInput6UOM = _AiSPYInput6UOM_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 6),
    _AiSPYInput6UOM_Type()
)
aiSPYInput6UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6UOM.setStatus("mandatory")


class _AiSPYInput6HighLimit_Type(Integer32):
    """Custom type aiSPYInput6HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput6HighLimit_Type.__name__ = "Integer32"
_AiSPYInput6HighLimit_Object = MibScalar
aiSPYInput6HighLimit = _AiSPYInput6HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 7),
    _AiSPYInput6HighLimit_Type()
)
aiSPYInput6HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6HighLimit.setStatus("mandatory")


class _AiSPYInput6LowLimit_Type(Integer32):
    """Custom type aiSPYInput6LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput6LowLimit_Type.__name__ = "Integer32"
_AiSPYInput6LowLimit_Object = MibScalar
aiSPYInput6LowLimit = _AiSPYInput6LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 8),
    _AiSPYInput6LowLimit_Type()
)
aiSPYInput6LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6LowLimit.setStatus("mandatory")


class _AiSPYInput6RlyControl_Type(Integer32):
    """Custom type aiSPYInput6RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput6RlyControl_Type.__name__ = "Integer32"
_AiSPYInput6RlyControl_Object = MibScalar
aiSPYInput6RlyControl = _AiSPYInput6RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 9),
    _AiSPYInput6RlyControl_Type()
)
aiSPYInput6RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6RlyControl.setStatus("mandatory")


class _AiSPYInput6Delay_Type(Integer32):
    """Custom type aiSPYInput6Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput6Delay_Type.__name__ = "Integer32"
_AiSPYInput6Delay_Object = MibScalar
aiSPYInput6Delay = _AiSPYInput6Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 10),
    _AiSPYInput6Delay_Type()
)
aiSPYInput6Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6Delay.setStatus("mandatory")


class _AiSPYInput6RTNDelay_Type(Integer32):
    """Custom type aiSPYInput6RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput6RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput6RTNDelay_Object = MibScalar
aiSPYInput6RTNDelay = _AiSPYInput6RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 11),
    _AiSPYInput6RTNDelay_Type()
)
aiSPYInput6RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6RTNDelay.setStatus("mandatory")


class _AiSPYInput6Hysteresis_Type(Integer32):
    """Custom type aiSPYInput6Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AiSPYInput6Hysteresis_Type.__name__ = "Integer32"
_AiSPYInput6Hysteresis_Object = MibScalar
aiSPYInput6Hysteresis = _AiSPYInput6Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 6, 12),
    _AiSPYInput6Hysteresis_Type()
)
aiSPYInput6Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput6Hysteresis.setStatus("mandatory")
_AiSPYInput7_ObjectIdentity = ObjectIdentity
aiSPYInput7 = _AiSPYInput7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7)
)


class _AiSPYInput7State_Type(Integer32):
    """Custom type aiSPYInput7State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog-4to20-installed", 2),
          ("notInstalled", 1))
    )


_AiSPYInput7State_Type.__name__ = "Integer32"
_AiSPYInput7State_Object = MibScalar
aiSPYInput7State = _AiSPYInput7State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 1),
    _AiSPYInput7State_Type()
)
aiSPYInput7State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7State.setStatus("mandatory")


class _AiSPYInput7Reading_Type(Integer32):
    """Custom type aiSPYInput7Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput7Reading_Type.__name__ = "Integer32"
_AiSPYInput7Reading_Object = MibScalar
aiSPYInput7Reading = _AiSPYInput7Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 2),
    _AiSPYInput7Reading_Type()
)
aiSPYInput7Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput7Reading.setStatus("mandatory")


class _AiSPYInput7Gain_Type(Integer32):
    """Custom type aiSPYInput7Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput7Gain_Type.__name__ = "Integer32"
_AiSPYInput7Gain_Object = MibScalar
aiSPYInput7Gain = _AiSPYInput7Gain_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 3),
    _AiSPYInput7Gain_Type()
)
aiSPYInput7Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7Gain.setStatus("mandatory")


class _AiSPYInput7Offset_Type(Integer32):
    """Custom type aiSPYInput7Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput7Offset_Type.__name__ = "Integer32"
_AiSPYInput7Offset_Object = MibScalar
aiSPYInput7Offset = _AiSPYInput7Offset_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 4),
    _AiSPYInput7Offset_Type()
)
aiSPYInput7Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7Offset.setStatus("mandatory")
_AiSPYInput7Label_Type = DisplayString
_AiSPYInput7Label_Object = MibScalar
aiSPYInput7Label = _AiSPYInput7Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 5),
    _AiSPYInput7Label_Type()
)
aiSPYInput7Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7Label.setStatus("mandatory")
_AiSPYInput7UOM_Type = DisplayString
_AiSPYInput7UOM_Object = MibScalar
aiSPYInput7UOM = _AiSPYInput7UOM_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 6),
    _AiSPYInput7UOM_Type()
)
aiSPYInput7UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7UOM.setStatus("mandatory")


class _AiSPYInput7HighLimit_Type(Integer32):
    """Custom type aiSPYInput7HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput7HighLimit_Type.__name__ = "Integer32"
_AiSPYInput7HighLimit_Object = MibScalar
aiSPYInput7HighLimit = _AiSPYInput7HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 7),
    _AiSPYInput7HighLimit_Type()
)
aiSPYInput7HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7HighLimit.setStatus("mandatory")


class _AiSPYInput7LowLimit_Type(Integer32):
    """Custom type aiSPYInput7LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput7LowLimit_Type.__name__ = "Integer32"
_AiSPYInput7LowLimit_Object = MibScalar
aiSPYInput7LowLimit = _AiSPYInput7LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 8),
    _AiSPYInput7LowLimit_Type()
)
aiSPYInput7LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7LowLimit.setStatus("mandatory")


class _AiSPYInput7RlyControl_Type(Integer32):
    """Custom type aiSPYInput7RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput7RlyControl_Type.__name__ = "Integer32"
_AiSPYInput7RlyControl_Object = MibScalar
aiSPYInput7RlyControl = _AiSPYInput7RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 9),
    _AiSPYInput7RlyControl_Type()
)
aiSPYInput7RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7RlyControl.setStatus("mandatory")


class _AiSPYInput7Delay_Type(Integer32):
    """Custom type aiSPYInput7Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput7Delay_Type.__name__ = "Integer32"
_AiSPYInput7Delay_Object = MibScalar
aiSPYInput7Delay = _AiSPYInput7Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 10),
    _AiSPYInput7Delay_Type()
)
aiSPYInput7Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7Delay.setStatus("mandatory")


class _AiSPYInput7RTNDelay_Type(Integer32):
    """Custom type aiSPYInput7RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput7RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput7RTNDelay_Object = MibScalar
aiSPYInput7RTNDelay = _AiSPYInput7RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 11),
    _AiSPYInput7RTNDelay_Type()
)
aiSPYInput7RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7RTNDelay.setStatus("mandatory")


class _AiSPYInput7Hysteresis_Type(Integer32):
    """Custom type aiSPYInput7Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AiSPYInput7Hysteresis_Type.__name__ = "Integer32"
_AiSPYInput7Hysteresis_Object = MibScalar
aiSPYInput7Hysteresis = _AiSPYInput7Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 7, 12),
    _AiSPYInput7Hysteresis_Type()
)
aiSPYInput7Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput7Hysteresis.setStatus("mandatory")
_AiSPYInput8_ObjectIdentity = ObjectIdentity
aiSPYInput8 = _AiSPYInput8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8)
)


class _AiSPYInput8State_Type(Integer32):
    """Custom type aiSPYInput8State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog-4to20-installed", 2),
          ("notInstalled", 1))
    )


_AiSPYInput8State_Type.__name__ = "Integer32"
_AiSPYInput8State_Object = MibScalar
aiSPYInput8State = _AiSPYInput8State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 1),
    _AiSPYInput8State_Type()
)
aiSPYInput8State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8State.setStatus("mandatory")


class _AiSPYInput8Reading_Type(Integer32):
    """Custom type aiSPYInput8Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput8Reading_Type.__name__ = "Integer32"
_AiSPYInput8Reading_Object = MibScalar
aiSPYInput8Reading = _AiSPYInput8Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 2),
    _AiSPYInput8Reading_Type()
)
aiSPYInput8Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput8Reading.setStatus("mandatory")


class _AiSPYInput8Gain_Type(Integer32):
    """Custom type aiSPYInput8Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput8Gain_Type.__name__ = "Integer32"
_AiSPYInput8Gain_Object = MibScalar
aiSPYInput8Gain = _AiSPYInput8Gain_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 3),
    _AiSPYInput8Gain_Type()
)
aiSPYInput8Gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8Gain.setStatus("mandatory")


class _AiSPYInput8Offset_Type(Integer32):
    """Custom type aiSPYInput8Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput8Offset_Type.__name__ = "Integer32"
_AiSPYInput8Offset_Object = MibScalar
aiSPYInput8Offset = _AiSPYInput8Offset_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 4),
    _AiSPYInput8Offset_Type()
)
aiSPYInput8Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8Offset.setStatus("mandatory")
_AiSPYInput8Label_Type = DisplayString
_AiSPYInput8Label_Object = MibScalar
aiSPYInput8Label = _AiSPYInput8Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 5),
    _AiSPYInput8Label_Type()
)
aiSPYInput8Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8Label.setStatus("mandatory")
_AiSPYInput8UOM_Type = DisplayString
_AiSPYInput8UOM_Object = MibScalar
aiSPYInput8UOM = _AiSPYInput8UOM_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 6),
    _AiSPYInput8UOM_Type()
)
aiSPYInput8UOM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8UOM.setStatus("mandatory")


class _AiSPYInput8HighLimit_Type(Integer32):
    """Custom type aiSPYInput8HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput8HighLimit_Type.__name__ = "Integer32"
_AiSPYInput8HighLimit_Object = MibScalar
aiSPYInput8HighLimit = _AiSPYInput8HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 7),
    _AiSPYInput8HighLimit_Type()
)
aiSPYInput8HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8HighLimit.setStatus("mandatory")


class _AiSPYInput8LowLimit_Type(Integer32):
    """Custom type aiSPYInput8LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput8LowLimit_Type.__name__ = "Integer32"
_AiSPYInput8LowLimit_Object = MibScalar
aiSPYInput8LowLimit = _AiSPYInput8LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 8),
    _AiSPYInput8LowLimit_Type()
)
aiSPYInput8LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8LowLimit.setStatus("mandatory")


class _AiSPYInput8RlyControl_Type(Integer32):
    """Custom type aiSPYInput8RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput8RlyControl_Type.__name__ = "Integer32"
_AiSPYInput8RlyControl_Object = MibScalar
aiSPYInput8RlyControl = _AiSPYInput8RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 9),
    _AiSPYInput8RlyControl_Type()
)
aiSPYInput8RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8RlyControl.setStatus("mandatory")


class _AiSPYInput8Delay_Type(Integer32):
    """Custom type aiSPYInput8Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput8Delay_Type.__name__ = "Integer32"
_AiSPYInput8Delay_Object = MibScalar
aiSPYInput8Delay = _AiSPYInput8Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 10),
    _AiSPYInput8Delay_Type()
)
aiSPYInput8Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8Delay.setStatus("mandatory")


class _AiSPYInput8RTNDelay_Type(Integer32):
    """Custom type aiSPYInput8RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput8RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput8RTNDelay_Object = MibScalar
aiSPYInput8RTNDelay = _AiSPYInput8RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 11),
    _AiSPYInput8RTNDelay_Type()
)
aiSPYInput8RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8RTNDelay.setStatus("mandatory")


class _AiSPYInput8Hysteresis_Type(Integer32):
    """Custom type aiSPYInput8Hysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AiSPYInput8Hysteresis_Type.__name__ = "Integer32"
_AiSPYInput8Hysteresis_Object = MibScalar
aiSPYInput8Hysteresis = _AiSPYInput8Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 8, 12),
    _AiSPYInput8Hysteresis_Type()
)
aiSPYInput8Hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput8Hysteresis.setStatus("mandatory")
_AiSPYInput9_ObjectIdentity = ObjectIdentity
aiSPYInput9 = _AiSPYInput9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 25)
)


class _AiSPYInput9State_Type(Integer32):
    """Custom type aiSPYInput9State based on Integer32"""
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


_AiSPYInput9State_Type.__name__ = "Integer32"
_AiSPYInput9State_Object = MibScalar
aiSPYInput9State = _AiSPYInput9State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 25, 1),
    _AiSPYInput9State_Type()
)
aiSPYInput9State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput9State.setStatus("mandatory")


class _AiSPYInput9Reading_Type(Integer32):
    """Custom type aiSPYInput9Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput9Reading_Type.__name__ = "Integer32"
_AiSPYInput9Reading_Object = MibScalar
aiSPYInput9Reading = _AiSPYInput9Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 25, 2),
    _AiSPYInput9Reading_Type()
)
aiSPYInput9Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput9Reading.setStatus("mandatory")
_AiSPYInput9Label_Type = DisplayString
_AiSPYInput9Label_Object = MibScalar
aiSPYInput9Label = _AiSPYInput9Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 25, 3),
    _AiSPYInput9Label_Type()
)
aiSPYInput9Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput9Label.setStatus("mandatory")


class _AiSPYInput9RlyControl_Type(Integer32):
    """Custom type aiSPYInput9RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput9RlyControl_Type.__name__ = "Integer32"
_AiSPYInput9RlyControl_Object = MibScalar
aiSPYInput9RlyControl = _AiSPYInput9RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 25, 4),
    _AiSPYInput9RlyControl_Type()
)
aiSPYInput9RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput9RlyControl.setStatus("mandatory")


class _AiSPYInput9Delay_Type(Integer32):
    """Custom type aiSPYInput9Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput9Delay_Type.__name__ = "Integer32"
_AiSPYInput9Delay_Object = MibScalar
aiSPYInput9Delay = _AiSPYInput9Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 25, 5),
    _AiSPYInput9Delay_Type()
)
aiSPYInput9Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput9Delay.setStatus("mandatory")


class _AiSPYInput9RTNDelay_Type(Integer32):
    """Custom type aiSPYInput9RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput9RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput9RTNDelay_Object = MibScalar
aiSPYInput9RTNDelay = _AiSPYInput9RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 25, 6),
    _AiSPYInput9RTNDelay_Type()
)
aiSPYInput9RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput9RTNDelay.setStatus("mandatory")
_AiSPYInput10_ObjectIdentity = ObjectIdentity
aiSPYInput10 = _AiSPYInput10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 26)
)


class _AiSPYInput10State_Type(Integer32):
    """Custom type aiSPYInput10State based on Integer32"""
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


_AiSPYInput10State_Type.__name__ = "Integer32"
_AiSPYInput10State_Object = MibScalar
aiSPYInput10State = _AiSPYInput10State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 26, 1),
    _AiSPYInput10State_Type()
)
aiSPYInput10State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput10State.setStatus("mandatory")


class _AiSPYInput10Reading_Type(Integer32):
    """Custom type aiSPYInput10Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput10Reading_Type.__name__ = "Integer32"
_AiSPYInput10Reading_Object = MibScalar
aiSPYInput10Reading = _AiSPYInput10Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 26, 2),
    _AiSPYInput10Reading_Type()
)
aiSPYInput10Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput10Reading.setStatus("mandatory")
_AiSPYInput10Label_Type = DisplayString
_AiSPYInput10Label_Object = MibScalar
aiSPYInput10Label = _AiSPYInput10Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 26, 3),
    _AiSPYInput10Label_Type()
)
aiSPYInput10Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput10Label.setStatus("mandatory")


class _AiSPYInput10RlyControl_Type(Integer32):
    """Custom type aiSPYInput10RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput10RlyControl_Type.__name__ = "Integer32"
_AiSPYInput10RlyControl_Object = MibScalar
aiSPYInput10RlyControl = _AiSPYInput10RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 26, 4),
    _AiSPYInput10RlyControl_Type()
)
aiSPYInput10RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput10RlyControl.setStatus("mandatory")


class _AiSPYInput10Delay_Type(Integer32):
    """Custom type aiSPYInput10Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput10Delay_Type.__name__ = "Integer32"
_AiSPYInput10Delay_Object = MibScalar
aiSPYInput10Delay = _AiSPYInput10Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 26, 5),
    _AiSPYInput10Delay_Type()
)
aiSPYInput10Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput10Delay.setStatus("mandatory")


class _AiSPYInput10RTNDelay_Type(Integer32):
    """Custom type aiSPYInput10RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput10RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput10RTNDelay_Object = MibScalar
aiSPYInput10RTNDelay = _AiSPYInput10RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 26, 6),
    _AiSPYInput10RTNDelay_Type()
)
aiSPYInput10RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput10RTNDelay.setStatus("mandatory")
_AiSPYInput11_ObjectIdentity = ObjectIdentity
aiSPYInput11 = _AiSPYInput11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 27)
)


class _AiSPYInput11State_Type(Integer32):
    """Custom type aiSPYInput11State based on Integer32"""
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


_AiSPYInput11State_Type.__name__ = "Integer32"
_AiSPYInput11State_Object = MibScalar
aiSPYInput11State = _AiSPYInput11State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 27, 1),
    _AiSPYInput11State_Type()
)
aiSPYInput11State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput11State.setStatus("mandatory")


class _AiSPYInput11Reading_Type(Integer32):
    """Custom type aiSPYInput11Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput11Reading_Type.__name__ = "Integer32"
_AiSPYInput11Reading_Object = MibScalar
aiSPYInput11Reading = _AiSPYInput11Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 27, 2),
    _AiSPYInput11Reading_Type()
)
aiSPYInput11Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput11Reading.setStatus("mandatory")
_AiSPYInput11Label_Type = DisplayString
_AiSPYInput11Label_Object = MibScalar
aiSPYInput11Label = _AiSPYInput11Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 27, 3),
    _AiSPYInput11Label_Type()
)
aiSPYInput11Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput11Label.setStatus("mandatory")


class _AiSPYInput11RlyControl_Type(Integer32):
    """Custom type aiSPYInput11RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput11RlyControl_Type.__name__ = "Integer32"
_AiSPYInput11RlyControl_Object = MibScalar
aiSPYInput11RlyControl = _AiSPYInput11RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 27, 4),
    _AiSPYInput11RlyControl_Type()
)
aiSPYInput11RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput11RlyControl.setStatus("mandatory")


class _AiSPYInput11Delay_Type(Integer32):
    """Custom type aiSPYInput11Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput11Delay_Type.__name__ = "Integer32"
_AiSPYInput11Delay_Object = MibScalar
aiSPYInput11Delay = _AiSPYInput11Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 27, 5),
    _AiSPYInput11Delay_Type()
)
aiSPYInput11Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput11Delay.setStatus("mandatory")


class _AiSPYInput11RTNDelay_Type(Integer32):
    """Custom type aiSPYInput11RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput11RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput11RTNDelay_Object = MibScalar
aiSPYInput11RTNDelay = _AiSPYInput11RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 27, 6),
    _AiSPYInput11RTNDelay_Type()
)
aiSPYInput11RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput11RTNDelay.setStatus("mandatory")
_AiSPYInput12_ObjectIdentity = ObjectIdentity
aiSPYInput12 = _AiSPYInput12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 28)
)


class _AiSPYInput12State_Type(Integer32):
    """Custom type aiSPYInput12State based on Integer32"""
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


_AiSPYInput12State_Type.__name__ = "Integer32"
_AiSPYInput12State_Object = MibScalar
aiSPYInput12State = _AiSPYInput12State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 28, 1),
    _AiSPYInput12State_Type()
)
aiSPYInput12State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput12State.setStatus("mandatory")


class _AiSPYInput12Reading_Type(Integer32):
    """Custom type aiSPYInput12Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput12Reading_Type.__name__ = "Integer32"
_AiSPYInput12Reading_Object = MibScalar
aiSPYInput12Reading = _AiSPYInput12Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 28, 2),
    _AiSPYInput12Reading_Type()
)
aiSPYInput12Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput12Reading.setStatus("mandatory")
_AiSPYInput12Label_Type = DisplayString
_AiSPYInput12Label_Object = MibScalar
aiSPYInput12Label = _AiSPYInput12Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 28, 3),
    _AiSPYInput12Label_Type()
)
aiSPYInput12Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput12Label.setStatus("mandatory")


class _AiSPYInput12RlyControl_Type(Integer32):
    """Custom type aiSPYInput12RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput12RlyControl_Type.__name__ = "Integer32"
_AiSPYInput12RlyControl_Object = MibScalar
aiSPYInput12RlyControl = _AiSPYInput12RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 28, 4),
    _AiSPYInput12RlyControl_Type()
)
aiSPYInput12RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput12RlyControl.setStatus("mandatory")


class _AiSPYInput12Delay_Type(Integer32):
    """Custom type aiSPYInput12Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput12Delay_Type.__name__ = "Integer32"
_AiSPYInput12Delay_Object = MibScalar
aiSPYInput12Delay = _AiSPYInput12Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 28, 5),
    _AiSPYInput12Delay_Type()
)
aiSPYInput12Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput12Delay.setStatus("mandatory")


class _AiSPYInput12RTNDelay_Type(Integer32):
    """Custom type aiSPYInput12RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput12RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput12RTNDelay_Object = MibScalar
aiSPYInput12RTNDelay = _AiSPYInput12RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 28, 6),
    _AiSPYInput12RTNDelay_Type()
)
aiSPYInput12RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput12RTNDelay.setStatus("mandatory")
_AiSPYInput13_ObjectIdentity = ObjectIdentity
aiSPYInput13 = _AiSPYInput13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 29)
)


class _AiSPYInput13State_Type(Integer32):
    """Custom type aiSPYInput13State based on Integer32"""
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


_AiSPYInput13State_Type.__name__ = "Integer32"
_AiSPYInput13State_Object = MibScalar
aiSPYInput13State = _AiSPYInput13State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 29, 1),
    _AiSPYInput13State_Type()
)
aiSPYInput13State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput13State.setStatus("mandatory")


class _AiSPYInput13Reading_Type(Integer32):
    """Custom type aiSPYInput13Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput13Reading_Type.__name__ = "Integer32"
_AiSPYInput13Reading_Object = MibScalar
aiSPYInput13Reading = _AiSPYInput13Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 29, 2),
    _AiSPYInput13Reading_Type()
)
aiSPYInput13Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput13Reading.setStatus("mandatory")
_AiSPYInput13Label_Type = DisplayString
_AiSPYInput13Label_Object = MibScalar
aiSPYInput13Label = _AiSPYInput13Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 29, 3),
    _AiSPYInput13Label_Type()
)
aiSPYInput13Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput13Label.setStatus("mandatory")


class _AiSPYInput13RlyControl_Type(Integer32):
    """Custom type aiSPYInput13RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput13RlyControl_Type.__name__ = "Integer32"
_AiSPYInput13RlyControl_Object = MibScalar
aiSPYInput13RlyControl = _AiSPYInput13RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 29, 4),
    _AiSPYInput13RlyControl_Type()
)
aiSPYInput13RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput13RlyControl.setStatus("mandatory")


class _AiSPYInput13Delay_Type(Integer32):
    """Custom type aiSPYInput13Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput13Delay_Type.__name__ = "Integer32"
_AiSPYInput13Delay_Object = MibScalar
aiSPYInput13Delay = _AiSPYInput13Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 29, 5),
    _AiSPYInput13Delay_Type()
)
aiSPYInput13Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput13Delay.setStatus("mandatory")


class _AiSPYInput13RTNDelay_Type(Integer32):
    """Custom type aiSPYInput13RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput13RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput13RTNDelay_Object = MibScalar
aiSPYInput13RTNDelay = _AiSPYInput13RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 29, 6),
    _AiSPYInput13RTNDelay_Type()
)
aiSPYInput13RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput13RTNDelay.setStatus("mandatory")
_AiSPYInput14_ObjectIdentity = ObjectIdentity
aiSPYInput14 = _AiSPYInput14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 30)
)


class _AiSPYInput14State_Type(Integer32):
    """Custom type aiSPYInput14State based on Integer32"""
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


_AiSPYInput14State_Type.__name__ = "Integer32"
_AiSPYInput14State_Object = MibScalar
aiSPYInput14State = _AiSPYInput14State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 30, 1),
    _AiSPYInput14State_Type()
)
aiSPYInput14State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput14State.setStatus("mandatory")


class _AiSPYInput14Reading_Type(Integer32):
    """Custom type aiSPYInput14Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput14Reading_Type.__name__ = "Integer32"
_AiSPYInput14Reading_Object = MibScalar
aiSPYInput14Reading = _AiSPYInput14Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 30, 2),
    _AiSPYInput14Reading_Type()
)
aiSPYInput14Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput14Reading.setStatus("mandatory")
_AiSPYInput14Label_Type = DisplayString
_AiSPYInput14Label_Object = MibScalar
aiSPYInput14Label = _AiSPYInput14Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 30, 3),
    _AiSPYInput14Label_Type()
)
aiSPYInput14Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput14Label.setStatus("mandatory")


class _AiSPYInput14RlyControl_Type(Integer32):
    """Custom type aiSPYInput14RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput14RlyControl_Type.__name__ = "Integer32"
_AiSPYInput14RlyControl_Object = MibScalar
aiSPYInput14RlyControl = _AiSPYInput14RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 30, 4),
    _AiSPYInput14RlyControl_Type()
)
aiSPYInput14RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput14RlyControl.setStatus("mandatory")


class _AiSPYInput14Delay_Type(Integer32):
    """Custom type aiSPYInput14Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput14Delay_Type.__name__ = "Integer32"
_AiSPYInput14Delay_Object = MibScalar
aiSPYInput14Delay = _AiSPYInput14Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 30, 5),
    _AiSPYInput14Delay_Type()
)
aiSPYInput14Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput14Delay.setStatus("mandatory")


class _AiSPYInput14RTNDelay_Type(Integer32):
    """Custom type aiSPYInput14RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput14RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput14RTNDelay_Object = MibScalar
aiSPYInput14RTNDelay = _AiSPYInput14RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 30, 6),
    _AiSPYInput14RTNDelay_Type()
)
aiSPYInput14RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput14RTNDelay.setStatus("mandatory")
_AiSPYInput15_ObjectIdentity = ObjectIdentity
aiSPYInput15 = _AiSPYInput15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 31)
)


class _AiSPYInput15State_Type(Integer32):
    """Custom type aiSPYInput15State based on Integer32"""
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


_AiSPYInput15State_Type.__name__ = "Integer32"
_AiSPYInput15State_Object = MibScalar
aiSPYInput15State = _AiSPYInput15State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 31, 1),
    _AiSPYInput15State_Type()
)
aiSPYInput15State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput15State.setStatus("mandatory")


class _AiSPYInput15Reading_Type(Integer32):
    """Custom type aiSPYInput15Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput15Reading_Type.__name__ = "Integer32"
_AiSPYInput15Reading_Object = MibScalar
aiSPYInput15Reading = _AiSPYInput15Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 31, 2),
    _AiSPYInput15Reading_Type()
)
aiSPYInput15Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput15Reading.setStatus("mandatory")
_AiSPYInput15Label_Type = DisplayString
_AiSPYInput15Label_Object = MibScalar
aiSPYInput15Label = _AiSPYInput15Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 31, 3),
    _AiSPYInput15Label_Type()
)
aiSPYInput15Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput15Label.setStatus("mandatory")


class _AiSPYInput15RlyControl_Type(Integer32):
    """Custom type aiSPYInput15RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput15RlyControl_Type.__name__ = "Integer32"
_AiSPYInput15RlyControl_Object = MibScalar
aiSPYInput15RlyControl = _AiSPYInput15RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 31, 4),
    _AiSPYInput15RlyControl_Type()
)
aiSPYInput15RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput15RlyControl.setStatus("mandatory")


class _AiSPYInput15Delay_Type(Integer32):
    """Custom type aiSPYInput15Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput15Delay_Type.__name__ = "Integer32"
_AiSPYInput15Delay_Object = MibScalar
aiSPYInput15Delay = _AiSPYInput15Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 31, 5),
    _AiSPYInput15Delay_Type()
)
aiSPYInput15Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput15Delay.setStatus("mandatory")


class _AiSPYInput15RTNDelay_Type(Integer32):
    """Custom type aiSPYInput15RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput15RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput15RTNDelay_Object = MibScalar
aiSPYInput15RTNDelay = _AiSPYInput15RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 31, 6),
    _AiSPYInput15RTNDelay_Type()
)
aiSPYInput15RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput15RTNDelay.setStatus("mandatory")
_AiSPYInput16_ObjectIdentity = ObjectIdentity
aiSPYInput16 = _AiSPYInput16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 32)
)


class _AiSPYInput16State_Type(Integer32):
    """Custom type aiSPYInput16State based on Integer32"""
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


_AiSPYInput16State_Type.__name__ = "Integer32"
_AiSPYInput16State_Object = MibScalar
aiSPYInput16State = _AiSPYInput16State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 32, 1),
    _AiSPYInput16State_Type()
)
aiSPYInput16State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput16State.setStatus("mandatory")


class _AiSPYInput16Reading_Type(Integer32):
    """Custom type aiSPYInput16Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput16Reading_Type.__name__ = "Integer32"
_AiSPYInput16Reading_Object = MibScalar
aiSPYInput16Reading = _AiSPYInput16Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 32, 2),
    _AiSPYInput16Reading_Type()
)
aiSPYInput16Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput16Reading.setStatus("mandatory")
_AiSPYInput16Label_Type = DisplayString
_AiSPYInput16Label_Object = MibScalar
aiSPYInput16Label = _AiSPYInput16Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 32, 3),
    _AiSPYInput16Label_Type()
)
aiSPYInput16Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput16Label.setStatus("mandatory")


class _AiSPYInput16RlyControl_Type(Integer32):
    """Custom type aiSPYInput16RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput16RlyControl_Type.__name__ = "Integer32"
_AiSPYInput16RlyControl_Object = MibScalar
aiSPYInput16RlyControl = _AiSPYInput16RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 32, 4),
    _AiSPYInput16RlyControl_Type()
)
aiSPYInput16RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput16RlyControl.setStatus("mandatory")


class _AiSPYInput16Delay_Type(Integer32):
    """Custom type aiSPYInput16Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput16Delay_Type.__name__ = "Integer32"
_AiSPYInput16Delay_Object = MibScalar
aiSPYInput16Delay = _AiSPYInput16Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 32, 5),
    _AiSPYInput16Delay_Type()
)
aiSPYInput16Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput16Delay.setStatus("mandatory")


class _AiSPYInput16RTNDelay_Type(Integer32):
    """Custom type aiSPYInput16RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput16RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput16RTNDelay_Object = MibScalar
aiSPYInput16RTNDelay = _AiSPYInput16RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 32, 6),
    _AiSPYInput16RTNDelay_Type()
)
aiSPYInput16RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput16RTNDelay.setStatus("mandatory")
_AiSPYInput17_ObjectIdentity = ObjectIdentity
aiSPYInput17 = _AiSPYInput17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 33)
)


class _AiSPYInput17State_Type(Integer32):
    """Custom type aiSPYInput17State based on Integer32"""
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


_AiSPYInput17State_Type.__name__ = "Integer32"
_AiSPYInput17State_Object = MibScalar
aiSPYInput17State = _AiSPYInput17State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 33, 1),
    _AiSPYInput17State_Type()
)
aiSPYInput17State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput17State.setStatus("mandatory")


class _AiSPYInput17Reading_Type(Integer32):
    """Custom type aiSPYInput17Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput17Reading_Type.__name__ = "Integer32"
_AiSPYInput17Reading_Object = MibScalar
aiSPYInput17Reading = _AiSPYInput17Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 33, 2),
    _AiSPYInput17Reading_Type()
)
aiSPYInput17Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput17Reading.setStatus("mandatory")
_AiSPYInput17Label_Type = DisplayString
_AiSPYInput17Label_Object = MibScalar
aiSPYInput17Label = _AiSPYInput17Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 33, 3),
    _AiSPYInput17Label_Type()
)
aiSPYInput17Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput17Label.setStatus("mandatory")


class _AiSPYInput17RlyControl_Type(Integer32):
    """Custom type aiSPYInput17RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput17RlyControl_Type.__name__ = "Integer32"
_AiSPYInput17RlyControl_Object = MibScalar
aiSPYInput17RlyControl = _AiSPYInput17RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 33, 4),
    _AiSPYInput17RlyControl_Type()
)
aiSPYInput17RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput17RlyControl.setStatus("mandatory")


class _AiSPYInput17Delay_Type(Integer32):
    """Custom type aiSPYInput17Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput17Delay_Type.__name__ = "Integer32"
_AiSPYInput17Delay_Object = MibScalar
aiSPYInput17Delay = _AiSPYInput17Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 33, 5),
    _AiSPYInput17Delay_Type()
)
aiSPYInput17Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput17Delay.setStatus("mandatory")


class _AiSPYInput17RTNDelay_Type(Integer32):
    """Custom type aiSPYInput17RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput17RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput17RTNDelay_Object = MibScalar
aiSPYInput17RTNDelay = _AiSPYInput17RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 33, 6),
    _AiSPYInput17RTNDelay_Type()
)
aiSPYInput17RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput17RTNDelay.setStatus("mandatory")
_AiSPYInput18_ObjectIdentity = ObjectIdentity
aiSPYInput18 = _AiSPYInput18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 34)
)


class _AiSPYInput18State_Type(Integer32):
    """Custom type aiSPYInput18State based on Integer32"""
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


_AiSPYInput18State_Type.__name__ = "Integer32"
_AiSPYInput18State_Object = MibScalar
aiSPYInput18State = _AiSPYInput18State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 34, 1),
    _AiSPYInput18State_Type()
)
aiSPYInput18State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput18State.setStatus("mandatory")


class _AiSPYInput18Reading_Type(Integer32):
    """Custom type aiSPYInput18Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput18Reading_Type.__name__ = "Integer32"
_AiSPYInput18Reading_Object = MibScalar
aiSPYInput18Reading = _AiSPYInput18Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 34, 2),
    _AiSPYInput18Reading_Type()
)
aiSPYInput18Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput18Reading.setStatus("mandatory")
_AiSPYInput18Label_Type = DisplayString
_AiSPYInput18Label_Object = MibScalar
aiSPYInput18Label = _AiSPYInput18Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 34, 3),
    _AiSPYInput18Label_Type()
)
aiSPYInput18Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput18Label.setStatus("mandatory")


class _AiSPYInput18RlyControl_Type(Integer32):
    """Custom type aiSPYInput18RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput18RlyControl_Type.__name__ = "Integer32"
_AiSPYInput18RlyControl_Object = MibScalar
aiSPYInput18RlyControl = _AiSPYInput18RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 34, 4),
    _AiSPYInput18RlyControl_Type()
)
aiSPYInput18RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput18RlyControl.setStatus("mandatory")


class _AiSPYInput18Delay_Type(Integer32):
    """Custom type aiSPYInput18Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput18Delay_Type.__name__ = "Integer32"
_AiSPYInput18Delay_Object = MibScalar
aiSPYInput18Delay = _AiSPYInput18Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 34, 5),
    _AiSPYInput18Delay_Type()
)
aiSPYInput18Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput18Delay.setStatus("mandatory")


class _AiSPYInput18RTNDelay_Type(Integer32):
    """Custom type aiSPYInput18RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput18RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput18RTNDelay_Object = MibScalar
aiSPYInput18RTNDelay = _AiSPYInput18RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 34, 6),
    _AiSPYInput18RTNDelay_Type()
)
aiSPYInput18RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput18RTNDelay.setStatus("mandatory")
_AiSPYInput19_ObjectIdentity = ObjectIdentity
aiSPYInput19 = _AiSPYInput19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 35)
)


class _AiSPYInput19State_Type(Integer32):
    """Custom type aiSPYInput19State based on Integer32"""
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


_AiSPYInput19State_Type.__name__ = "Integer32"
_AiSPYInput19State_Object = MibScalar
aiSPYInput19State = _AiSPYInput19State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 35, 1),
    _AiSPYInput19State_Type()
)
aiSPYInput19State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput19State.setStatus("mandatory")


class _AiSPYInput19Reading_Type(Integer32):
    """Custom type aiSPYInput19Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput19Reading_Type.__name__ = "Integer32"
_AiSPYInput19Reading_Object = MibScalar
aiSPYInput19Reading = _AiSPYInput19Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 35, 2),
    _AiSPYInput19Reading_Type()
)
aiSPYInput19Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput19Reading.setStatus("mandatory")
_AiSPYInput19Label_Type = DisplayString
_AiSPYInput19Label_Object = MibScalar
aiSPYInput19Label = _AiSPYInput19Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 35, 3),
    _AiSPYInput19Label_Type()
)
aiSPYInput19Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput19Label.setStatus("mandatory")


class _AiSPYInput19RlyControl_Type(Integer32):
    """Custom type aiSPYInput19RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput19RlyControl_Type.__name__ = "Integer32"
_AiSPYInput19RlyControl_Object = MibScalar
aiSPYInput19RlyControl = _AiSPYInput19RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 35, 4),
    _AiSPYInput19RlyControl_Type()
)
aiSPYInput19RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput19RlyControl.setStatus("mandatory")


class _AiSPYInput19Delay_Type(Integer32):
    """Custom type aiSPYInput19Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput19Delay_Type.__name__ = "Integer32"
_AiSPYInput19Delay_Object = MibScalar
aiSPYInput19Delay = _AiSPYInput19Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 35, 5),
    _AiSPYInput19Delay_Type()
)
aiSPYInput19Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput19Delay.setStatus("mandatory")


class _AiSPYInput19RTNDelay_Type(Integer32):
    """Custom type aiSPYInput19RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput19RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput19RTNDelay_Object = MibScalar
aiSPYInput19RTNDelay = _AiSPYInput19RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 35, 6),
    _AiSPYInput19RTNDelay_Type()
)
aiSPYInput19RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput19RTNDelay.setStatus("mandatory")
_AiSPYInput20_ObjectIdentity = ObjectIdentity
aiSPYInput20 = _AiSPYInput20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 36)
)


class _AiSPYInput20State_Type(Integer32):
    """Custom type aiSPYInput20State based on Integer32"""
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


_AiSPYInput20State_Type.__name__ = "Integer32"
_AiSPYInput20State_Object = MibScalar
aiSPYInput20State = _AiSPYInput20State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 36, 1),
    _AiSPYInput20State_Type()
)
aiSPYInput20State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput20State.setStatus("mandatory")


class _AiSPYInput20Reading_Type(Integer32):
    """Custom type aiSPYInput20Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput20Reading_Type.__name__ = "Integer32"
_AiSPYInput20Reading_Object = MibScalar
aiSPYInput20Reading = _AiSPYInput20Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 36, 2),
    _AiSPYInput20Reading_Type()
)
aiSPYInput20Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput20Reading.setStatus("mandatory")
_AiSPYInput20Label_Type = DisplayString
_AiSPYInput20Label_Object = MibScalar
aiSPYInput20Label = _AiSPYInput20Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 36, 3),
    _AiSPYInput20Label_Type()
)
aiSPYInput20Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput20Label.setStatus("mandatory")


class _AiSPYInput20RlyControl_Type(Integer32):
    """Custom type aiSPYInput20RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput20RlyControl_Type.__name__ = "Integer32"
_AiSPYInput20RlyControl_Object = MibScalar
aiSPYInput20RlyControl = _AiSPYInput20RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 36, 4),
    _AiSPYInput20RlyControl_Type()
)
aiSPYInput20RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput20RlyControl.setStatus("mandatory")


class _AiSPYInput20Delay_Type(Integer32):
    """Custom type aiSPYInput20Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput20Delay_Type.__name__ = "Integer32"
_AiSPYInput20Delay_Object = MibScalar
aiSPYInput20Delay = _AiSPYInput20Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 36, 5),
    _AiSPYInput20Delay_Type()
)
aiSPYInput20Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput20Delay.setStatus("mandatory")


class _AiSPYInput20RTNDelay_Type(Integer32):
    """Custom type aiSPYInput20RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput20RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput20RTNDelay_Object = MibScalar
aiSPYInput20RTNDelay = _AiSPYInput20RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 36, 6),
    _AiSPYInput20RTNDelay_Type()
)
aiSPYInput20RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput20RTNDelay.setStatus("mandatory")
_AiSPYInput21_ObjectIdentity = ObjectIdentity
aiSPYInput21 = _AiSPYInput21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 37)
)


class _AiSPYInput21State_Type(Integer32):
    """Custom type aiSPYInput21State based on Integer32"""
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


_AiSPYInput21State_Type.__name__ = "Integer32"
_AiSPYInput21State_Object = MibScalar
aiSPYInput21State = _AiSPYInput21State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 37, 1),
    _AiSPYInput21State_Type()
)
aiSPYInput21State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput21State.setStatus("mandatory")


class _AiSPYInput21Reading_Type(Integer32):
    """Custom type aiSPYInput21Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput21Reading_Type.__name__ = "Integer32"
_AiSPYInput21Reading_Object = MibScalar
aiSPYInput21Reading = _AiSPYInput21Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 37, 2),
    _AiSPYInput21Reading_Type()
)
aiSPYInput21Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput21Reading.setStatus("mandatory")
_AiSPYInput21Label_Type = DisplayString
_AiSPYInput21Label_Object = MibScalar
aiSPYInput21Label = _AiSPYInput21Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 37, 3),
    _AiSPYInput21Label_Type()
)
aiSPYInput21Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput21Label.setStatus("mandatory")


class _AiSPYInput21RlyControl_Type(Integer32):
    """Custom type aiSPYInput21RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput21RlyControl_Type.__name__ = "Integer32"
_AiSPYInput21RlyControl_Object = MibScalar
aiSPYInput21RlyControl = _AiSPYInput21RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 37, 4),
    _AiSPYInput21RlyControl_Type()
)
aiSPYInput21RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput21RlyControl.setStatus("mandatory")


class _AiSPYInput21Delay_Type(Integer32):
    """Custom type aiSPYInput21Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput21Delay_Type.__name__ = "Integer32"
_AiSPYInput21Delay_Object = MibScalar
aiSPYInput21Delay = _AiSPYInput21Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 37, 5),
    _AiSPYInput21Delay_Type()
)
aiSPYInput21Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput21Delay.setStatus("mandatory")


class _AiSPYInput21RTNDelay_Type(Integer32):
    """Custom type aiSPYInput21RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput21RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput21RTNDelay_Object = MibScalar
aiSPYInput21RTNDelay = _AiSPYInput21RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 37, 6),
    _AiSPYInput21RTNDelay_Type()
)
aiSPYInput21RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput21RTNDelay.setStatus("mandatory")
_AiSPYInput22_ObjectIdentity = ObjectIdentity
aiSPYInput22 = _AiSPYInput22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 38)
)


class _AiSPYInput22State_Type(Integer32):
    """Custom type aiSPYInput22State based on Integer32"""
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


_AiSPYInput22State_Type.__name__ = "Integer32"
_AiSPYInput22State_Object = MibScalar
aiSPYInput22State = _AiSPYInput22State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 38, 1),
    _AiSPYInput22State_Type()
)
aiSPYInput22State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput22State.setStatus("mandatory")


class _AiSPYInput22Reading_Type(Integer32):
    """Custom type aiSPYInput22Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput22Reading_Type.__name__ = "Integer32"
_AiSPYInput22Reading_Object = MibScalar
aiSPYInput22Reading = _AiSPYInput22Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 38, 2),
    _AiSPYInput22Reading_Type()
)
aiSPYInput22Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput22Reading.setStatus("mandatory")
_AiSPYInput22Label_Type = DisplayString
_AiSPYInput22Label_Object = MibScalar
aiSPYInput22Label = _AiSPYInput22Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 38, 3),
    _AiSPYInput22Label_Type()
)
aiSPYInput22Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput22Label.setStatus("mandatory")


class _AiSPYInput22RlyControl_Type(Integer32):
    """Custom type aiSPYInput22RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput22RlyControl_Type.__name__ = "Integer32"
_AiSPYInput22RlyControl_Object = MibScalar
aiSPYInput22RlyControl = _AiSPYInput22RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 38, 4),
    _AiSPYInput22RlyControl_Type()
)
aiSPYInput22RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput22RlyControl.setStatus("mandatory")


class _AiSPYInput22Delay_Type(Integer32):
    """Custom type aiSPYInput22Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput22Delay_Type.__name__ = "Integer32"
_AiSPYInput22Delay_Object = MibScalar
aiSPYInput22Delay = _AiSPYInput22Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 38, 5),
    _AiSPYInput22Delay_Type()
)
aiSPYInput22Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput22Delay.setStatus("mandatory")


class _AiSPYInput22RTNDelay_Type(Integer32):
    """Custom type aiSPYInput22RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput22RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput22RTNDelay_Object = MibScalar
aiSPYInput22RTNDelay = _AiSPYInput22RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 38, 6),
    _AiSPYInput22RTNDelay_Type()
)
aiSPYInput22RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput22RTNDelay.setStatus("mandatory")
_AiSPYInput23_ObjectIdentity = ObjectIdentity
aiSPYInput23 = _AiSPYInput23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 39)
)


class _AiSPYInput23State_Type(Integer32):
    """Custom type aiSPYInput23State based on Integer32"""
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


_AiSPYInput23State_Type.__name__ = "Integer32"
_AiSPYInput23State_Object = MibScalar
aiSPYInput23State = _AiSPYInput23State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 39, 1),
    _AiSPYInput23State_Type()
)
aiSPYInput23State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput23State.setStatus("mandatory")


class _AiSPYInput23Reading_Type(Integer32):
    """Custom type aiSPYInput23Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput23Reading_Type.__name__ = "Integer32"
_AiSPYInput23Reading_Object = MibScalar
aiSPYInput23Reading = _AiSPYInput23Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 39, 2),
    _AiSPYInput23Reading_Type()
)
aiSPYInput23Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput23Reading.setStatus("mandatory")
_AiSPYInput23Label_Type = DisplayString
_AiSPYInput23Label_Object = MibScalar
aiSPYInput23Label = _AiSPYInput23Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 39, 3),
    _AiSPYInput23Label_Type()
)
aiSPYInput23Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput23Label.setStatus("mandatory")


class _AiSPYInput23RlyControl_Type(Integer32):
    """Custom type aiSPYInput23RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput23RlyControl_Type.__name__ = "Integer32"
_AiSPYInput23RlyControl_Object = MibScalar
aiSPYInput23RlyControl = _AiSPYInput23RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 39, 4),
    _AiSPYInput23RlyControl_Type()
)
aiSPYInput23RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput23RlyControl.setStatus("mandatory")


class _AiSPYInput23Delay_Type(Integer32):
    """Custom type aiSPYInput23Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput23Delay_Type.__name__ = "Integer32"
_AiSPYInput23Delay_Object = MibScalar
aiSPYInput23Delay = _AiSPYInput23Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 39, 5),
    _AiSPYInput23Delay_Type()
)
aiSPYInput23Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput23Delay.setStatus("mandatory")


class _AiSPYInput23RTNDelay_Type(Integer32):
    """Custom type aiSPYInput23RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput23RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput23RTNDelay_Object = MibScalar
aiSPYInput23RTNDelay = _AiSPYInput23RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 39, 6),
    _AiSPYInput23RTNDelay_Type()
)
aiSPYInput23RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput23RTNDelay.setStatus("mandatory")
_AiSPYInput24_ObjectIdentity = ObjectIdentity
aiSPYInput24 = _AiSPYInput24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 40)
)


class _AiSPYInput24State_Type(Integer32):
    """Custom type aiSPYInput24State based on Integer32"""
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


_AiSPYInput24State_Type.__name__ = "Integer32"
_AiSPYInput24State_Object = MibScalar
aiSPYInput24State = _AiSPYInput24State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 40, 1),
    _AiSPYInput24State_Type()
)
aiSPYInput24State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput24State.setStatus("mandatory")


class _AiSPYInput24Reading_Type(Integer32):
    """Custom type aiSPYInput24Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput24Reading_Type.__name__ = "Integer32"
_AiSPYInput24Reading_Object = MibScalar
aiSPYInput24Reading = _AiSPYInput24Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 40, 2),
    _AiSPYInput24Reading_Type()
)
aiSPYInput24Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput24Reading.setStatus("mandatory")
_AiSPYInput24Label_Type = DisplayString
_AiSPYInput24Label_Object = MibScalar
aiSPYInput24Label = _AiSPYInput24Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 40, 3),
    _AiSPYInput24Label_Type()
)
aiSPYInput24Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput24Label.setStatus("mandatory")


class _AiSPYInput24RlyControl_Type(Integer32):
    """Custom type aiSPYInput24RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput24RlyControl_Type.__name__ = "Integer32"
_AiSPYInput24RlyControl_Object = MibScalar
aiSPYInput24RlyControl = _AiSPYInput24RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 40, 4),
    _AiSPYInput24RlyControl_Type()
)
aiSPYInput24RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput24RlyControl.setStatus("mandatory")


class _AiSPYInput24Delay_Type(Integer32):
    """Custom type aiSPYInput24Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput24Delay_Type.__name__ = "Integer32"
_AiSPYInput24Delay_Object = MibScalar
aiSPYInput24Delay = _AiSPYInput24Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 40, 5),
    _AiSPYInput24Delay_Type()
)
aiSPYInput24Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput24Delay.setStatus("mandatory")


class _AiSPYInput24RTNDelay_Type(Integer32):
    """Custom type aiSPYInput24RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput24RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput24RTNDelay_Object = MibScalar
aiSPYInput24RTNDelay = _AiSPYInput24RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 40, 6),
    _AiSPYInput24RTNDelay_Type()
)
aiSPYInput24RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput24RTNDelay.setStatus("mandatory")
_AiSPYInput25_ObjectIdentity = ObjectIdentity
aiSPYInput25 = _AiSPYInput25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 41)
)


class _AiSPYInput25State_Type(Integer32):
    """Custom type aiSPYInput25State based on Integer32"""
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


_AiSPYInput25State_Type.__name__ = "Integer32"
_AiSPYInput25State_Object = MibScalar
aiSPYInput25State = _AiSPYInput25State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 41, 1),
    _AiSPYInput25State_Type()
)
aiSPYInput25State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput25State.setStatus("mandatory")


class _AiSPYInput25Reading_Type(Integer32):
    """Custom type aiSPYInput25Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput25Reading_Type.__name__ = "Integer32"
_AiSPYInput25Reading_Object = MibScalar
aiSPYInput25Reading = _AiSPYInput25Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 41, 2),
    _AiSPYInput25Reading_Type()
)
aiSPYInput25Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput25Reading.setStatus("mandatory")
_AiSPYInput25Label_Type = DisplayString
_AiSPYInput25Label_Object = MibScalar
aiSPYInput25Label = _AiSPYInput25Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 41, 3),
    _AiSPYInput25Label_Type()
)
aiSPYInput25Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput25Label.setStatus("mandatory")


class _AiSPYInput25RlyControl_Type(Integer32):
    """Custom type aiSPYInput25RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput25RlyControl_Type.__name__ = "Integer32"
_AiSPYInput25RlyControl_Object = MibScalar
aiSPYInput25RlyControl = _AiSPYInput25RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 41, 4),
    _AiSPYInput25RlyControl_Type()
)
aiSPYInput25RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput25RlyControl.setStatus("mandatory")


class _AiSPYInput25Delay_Type(Integer32):
    """Custom type aiSPYInput25Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput25Delay_Type.__name__ = "Integer32"
_AiSPYInput25Delay_Object = MibScalar
aiSPYInput25Delay = _AiSPYInput25Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 41, 5),
    _AiSPYInput25Delay_Type()
)
aiSPYInput25Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput25Delay.setStatus("mandatory")


class _AiSPYInput25RTNDelay_Type(Integer32):
    """Custom type aiSPYInput25RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput25RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput25RTNDelay_Object = MibScalar
aiSPYInput25RTNDelay = _AiSPYInput25RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 41, 6),
    _AiSPYInput25RTNDelay_Type()
)
aiSPYInput25RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput25RTNDelay.setStatus("mandatory")
_AiSPYInput26_ObjectIdentity = ObjectIdentity
aiSPYInput26 = _AiSPYInput26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 42)
)


class _AiSPYInput26State_Type(Integer32):
    """Custom type aiSPYInput26State based on Integer32"""
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


_AiSPYInput26State_Type.__name__ = "Integer32"
_AiSPYInput26State_Object = MibScalar
aiSPYInput26State = _AiSPYInput26State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 42, 1),
    _AiSPYInput26State_Type()
)
aiSPYInput26State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput26State.setStatus("mandatory")


class _AiSPYInput26Reading_Type(Integer32):
    """Custom type aiSPYInput26Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput26Reading_Type.__name__ = "Integer32"
_AiSPYInput26Reading_Object = MibScalar
aiSPYInput26Reading = _AiSPYInput26Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 42, 2),
    _AiSPYInput26Reading_Type()
)
aiSPYInput26Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput26Reading.setStatus("mandatory")
_AiSPYInput26Label_Type = DisplayString
_AiSPYInput26Label_Object = MibScalar
aiSPYInput26Label = _AiSPYInput26Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 42, 3),
    _AiSPYInput26Label_Type()
)
aiSPYInput26Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput26Label.setStatus("mandatory")


class _AiSPYInput26RlyControl_Type(Integer32):
    """Custom type aiSPYInput26RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput26RlyControl_Type.__name__ = "Integer32"
_AiSPYInput26RlyControl_Object = MibScalar
aiSPYInput26RlyControl = _AiSPYInput26RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 42, 4),
    _AiSPYInput26RlyControl_Type()
)
aiSPYInput26RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput26RlyControl.setStatus("mandatory")


class _AiSPYInput26Delay_Type(Integer32):
    """Custom type aiSPYInput26Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput26Delay_Type.__name__ = "Integer32"
_AiSPYInput26Delay_Object = MibScalar
aiSPYInput26Delay = _AiSPYInput26Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 42, 5),
    _AiSPYInput26Delay_Type()
)
aiSPYInput26Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput26Delay.setStatus("mandatory")


class _AiSPYInput26RTNDelay_Type(Integer32):
    """Custom type aiSPYInput26RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput26RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput26RTNDelay_Object = MibScalar
aiSPYInput26RTNDelay = _AiSPYInput26RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 42, 6),
    _AiSPYInput26RTNDelay_Type()
)
aiSPYInput26RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput26RTNDelay.setStatus("mandatory")
_AiSPYInput27_ObjectIdentity = ObjectIdentity
aiSPYInput27 = _AiSPYInput27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 43)
)


class _AiSPYInput27State_Type(Integer32):
    """Custom type aiSPYInput27State based on Integer32"""
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


_AiSPYInput27State_Type.__name__ = "Integer32"
_AiSPYInput27State_Object = MibScalar
aiSPYInput27State = _AiSPYInput27State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 43, 1),
    _AiSPYInput27State_Type()
)
aiSPYInput27State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput27State.setStatus("mandatory")


class _AiSPYInput27Reading_Type(Integer32):
    """Custom type aiSPYInput27Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput27Reading_Type.__name__ = "Integer32"
_AiSPYInput27Reading_Object = MibScalar
aiSPYInput27Reading = _AiSPYInput27Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 43, 2),
    _AiSPYInput27Reading_Type()
)
aiSPYInput27Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput27Reading.setStatus("mandatory")
_AiSPYInput27Label_Type = DisplayString
_AiSPYInput27Label_Object = MibScalar
aiSPYInput27Label = _AiSPYInput27Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 43, 3),
    _AiSPYInput27Label_Type()
)
aiSPYInput27Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput27Label.setStatus("mandatory")


class _AiSPYInput27RlyControl_Type(Integer32):
    """Custom type aiSPYInput27RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput27RlyControl_Type.__name__ = "Integer32"
_AiSPYInput27RlyControl_Object = MibScalar
aiSPYInput27RlyControl = _AiSPYInput27RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 43, 4),
    _AiSPYInput27RlyControl_Type()
)
aiSPYInput27RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput27RlyControl.setStatus("mandatory")


class _AiSPYInput27Delay_Type(Integer32):
    """Custom type aiSPYInput27Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput27Delay_Type.__name__ = "Integer32"
_AiSPYInput27Delay_Object = MibScalar
aiSPYInput27Delay = _AiSPYInput27Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 43, 5),
    _AiSPYInput27Delay_Type()
)
aiSPYInput27Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput27Delay.setStatus("mandatory")


class _AiSPYInput27RTNDelay_Type(Integer32):
    """Custom type aiSPYInput27RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput27RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput27RTNDelay_Object = MibScalar
aiSPYInput27RTNDelay = _AiSPYInput27RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 43, 6),
    _AiSPYInput27RTNDelay_Type()
)
aiSPYInput27RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput27RTNDelay.setStatus("mandatory")
_AiSPYInput28_ObjectIdentity = ObjectIdentity
aiSPYInput28 = _AiSPYInput28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 44)
)


class _AiSPYInput28State_Type(Integer32):
    """Custom type aiSPYInput28State based on Integer32"""
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


_AiSPYInput28State_Type.__name__ = "Integer32"
_AiSPYInput28State_Object = MibScalar
aiSPYInput28State = _AiSPYInput28State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 44, 1),
    _AiSPYInput28State_Type()
)
aiSPYInput28State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput28State.setStatus("mandatory")


class _AiSPYInput28Reading_Type(Integer32):
    """Custom type aiSPYInput28Reading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiSPYInput28Reading_Type.__name__ = "Integer32"
_AiSPYInput28Reading_Object = MibScalar
aiSPYInput28Reading = _AiSPYInput28Reading_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 44, 2),
    _AiSPYInput28Reading_Type()
)
aiSPYInput28Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYInput28Reading.setStatus("mandatory")
_AiSPYInput28Label_Type = DisplayString
_AiSPYInput28Label_Object = MibScalar
aiSPYInput28Label = _AiSPYInput28Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 44, 3),
    _AiSPYInput28Label_Type()
)
aiSPYInput28Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput28Label.setStatus("mandatory")


class _AiSPYInput28RlyControl_Type(Integer32):
    """Custom type aiSPYInput28RlyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYInput28RlyControl_Type.__name__ = "Integer32"
_AiSPYInput28RlyControl_Object = MibScalar
aiSPYInput28RlyControl = _AiSPYInput28RlyControl_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 44, 4),
    _AiSPYInput28RlyControl_Type()
)
aiSPYInput28RlyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput28RlyControl.setStatus("mandatory")


class _AiSPYInput28Delay_Type(Integer32):
    """Custom type aiSPYInput28Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput28Delay_Type.__name__ = "Integer32"
_AiSPYInput28Delay_Object = MibScalar
aiSPYInput28Delay = _AiSPYInput28Delay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 44, 5),
    _AiSPYInput28Delay_Type()
)
aiSPYInput28Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput28Delay.setStatus("mandatory")


class _AiSPYInput28RTNDelay_Type(Integer32):
    """Custom type aiSPYInput28RTNDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiSPYInput28RTNDelay_Type.__name__ = "Integer32"
_AiSPYInput28RTNDelay_Object = MibScalar
aiSPYInput28RTNDelay = _AiSPYInput28RTNDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 3, 44, 6),
    _AiSPYInput28RTNDelay_Type()
)
aiSPYInput28RTNDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYInput28RTNDelay.setStatus("mandatory")
_AiSPYOutputs_ObjectIdentity = ObjectIdentity
aiSPYOutputs = _AiSPYOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 4)
)
_AiSPYRelay1_ObjectIdentity = ObjectIdentity
aiSPYRelay1 = _AiSPYRelay1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 1)
)


class _AiSPYRelay1State_Type(Integer32):
    """Custom type aiSPYRelay1State based on Integer32"""
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


_AiSPYRelay1State_Type.__name__ = "Integer32"
_AiSPYRelay1State_Object = MibScalar
aiSPYRelay1State = _AiSPYRelay1State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 1, 1),
    _AiSPYRelay1State_Type()
)
aiSPYRelay1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay1State.setStatus("mandatory")


class _AiSPYRelay1Status_Type(Integer32):
    """Custom type aiSPYRelay1Status based on Integer32"""
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


_AiSPYRelay1Status_Type.__name__ = "Integer32"
_AiSPYRelay1Status_Object = MibScalar
aiSPYRelay1Status = _AiSPYRelay1Status_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 1, 2),
    _AiSPYRelay1Status_Type()
)
aiSPYRelay1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYRelay1Status.setStatus("mandatory")
_AiSPYRelay1Label_Type = DisplayString
_AiSPYRelay1Label_Object = MibScalar
aiSPYRelay1Label = _AiSPYRelay1Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 1, 3),
    _AiSPYRelay1Label_Type()
)
aiSPYRelay1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay1Label.setStatus("mandatory")


class _AiSPYRelay1Time_Type(Integer32):
    """Custom type aiSPYRelay1Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYRelay1Time_Type.__name__ = "Integer32"
_AiSPYRelay1Time_Object = MibScalar
aiSPYRelay1Time = _AiSPYRelay1Time_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 1, 4),
    _AiSPYRelay1Time_Type()
)
aiSPYRelay1Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay1Time.setStatus("mandatory")
_AiSPYRelay2_ObjectIdentity = ObjectIdentity
aiSPYRelay2 = _AiSPYRelay2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 2)
)


class _AiSPYRelay2State_Type(Integer32):
    """Custom type aiSPYRelay2State based on Integer32"""
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


_AiSPYRelay2State_Type.__name__ = "Integer32"
_AiSPYRelay2State_Object = MibScalar
aiSPYRelay2State = _AiSPYRelay2State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 2, 1),
    _AiSPYRelay2State_Type()
)
aiSPYRelay2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay2State.setStatus("mandatory")


class _AiSPYRelay2Status_Type(Integer32):
    """Custom type aiSPYRelay2Status based on Integer32"""
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


_AiSPYRelay2Status_Type.__name__ = "Integer32"
_AiSPYRelay2Status_Object = MibScalar
aiSPYRelay2Status = _AiSPYRelay2Status_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 2, 2),
    _AiSPYRelay2Status_Type()
)
aiSPYRelay2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYRelay2Status.setStatus("mandatory")
_AiSPYRelay2Label_Type = DisplayString
_AiSPYRelay2Label_Object = MibScalar
aiSPYRelay2Label = _AiSPYRelay2Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 2, 3),
    _AiSPYRelay2Label_Type()
)
aiSPYRelay2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay2Label.setStatus("mandatory")


class _AiSPYRelay2Time_Type(Integer32):
    """Custom type aiSPYRelay2Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYRelay2Time_Type.__name__ = "Integer32"
_AiSPYRelay2Time_Object = MibScalar
aiSPYRelay2Time = _AiSPYRelay2Time_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 2, 4),
    _AiSPYRelay2Time_Type()
)
aiSPYRelay2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay2Time.setStatus("mandatory")
_AiSPYRelay3_ObjectIdentity = ObjectIdentity
aiSPYRelay3 = _AiSPYRelay3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 3)
)


class _AiSPYRelay3State_Type(Integer32):
    """Custom type aiSPYRelay3State based on Integer32"""
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


_AiSPYRelay3State_Type.__name__ = "Integer32"
_AiSPYRelay3State_Object = MibScalar
aiSPYRelay3State = _AiSPYRelay3State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 3, 1),
    _AiSPYRelay3State_Type()
)
aiSPYRelay3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay3State.setStatus("mandatory")


class _AiSPYRelay3Status_Type(Integer32):
    """Custom type aiSPYRelay3Status based on Integer32"""
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


_AiSPYRelay3Status_Type.__name__ = "Integer32"
_AiSPYRelay3Status_Object = MibScalar
aiSPYRelay3Status = _AiSPYRelay3Status_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 3, 2),
    _AiSPYRelay3Status_Type()
)
aiSPYRelay3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYRelay3Status.setStatus("mandatory")
_AiSPYRelay3Label_Type = DisplayString
_AiSPYRelay3Label_Object = MibScalar
aiSPYRelay3Label = _AiSPYRelay3Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 3, 3),
    _AiSPYRelay3Label_Type()
)
aiSPYRelay3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay3Label.setStatus("mandatory")


class _AiSPYRelay3Time_Type(Integer32):
    """Custom type aiSPYRelay3Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYRelay3Time_Type.__name__ = "Integer32"
_AiSPYRelay3Time_Object = MibScalar
aiSPYRelay3Time = _AiSPYRelay3Time_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 3, 4),
    _AiSPYRelay3Time_Type()
)
aiSPYRelay3Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay3Time.setStatus("mandatory")
_AiSPYRelay4_ObjectIdentity = ObjectIdentity
aiSPYRelay4 = _AiSPYRelay4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 4)
)


class _AiSPYRelay4State_Type(Integer32):
    """Custom type aiSPYRelay4State based on Integer32"""
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


_AiSPYRelay4State_Type.__name__ = "Integer32"
_AiSPYRelay4State_Object = MibScalar
aiSPYRelay4State = _AiSPYRelay4State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 4, 1),
    _AiSPYRelay4State_Type()
)
aiSPYRelay4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay4State.setStatus("mandatory")


class _AiSPYRelay4Status_Type(Integer32):
    """Custom type aiSPYRelay4Status based on Integer32"""
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


_AiSPYRelay4Status_Type.__name__ = "Integer32"
_AiSPYRelay4Status_Object = MibScalar
aiSPYRelay4Status = _AiSPYRelay4Status_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 4, 2),
    _AiSPYRelay4Status_Type()
)
aiSPYRelay4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYRelay4Status.setStatus("mandatory")
_AiSPYRelay4Label_Type = DisplayString
_AiSPYRelay4Label_Object = MibScalar
aiSPYRelay4Label = _AiSPYRelay4Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 4, 3),
    _AiSPYRelay4Label_Type()
)
aiSPYRelay4Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay4Label.setStatus("mandatory")


class _AiSPYRelay4Time_Type(Integer32):
    """Custom type aiSPYRelay4Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYRelay4Time_Type.__name__ = "Integer32"
_AiSPYRelay4Time_Object = MibScalar
aiSPYRelay4Time = _AiSPYRelay4Time_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 4, 4),
    _AiSPYRelay4Time_Type()
)
aiSPYRelay4Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay4Time.setStatus("mandatory")
_AiSPYRelay5_ObjectIdentity = ObjectIdentity
aiSPYRelay5 = _AiSPYRelay5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 5)
)


class _AiSPYRelay5State_Type(Integer32):
    """Custom type aiSPYRelay5State based on Integer32"""
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


_AiSPYRelay5State_Type.__name__ = "Integer32"
_AiSPYRelay5State_Object = MibScalar
aiSPYRelay5State = _AiSPYRelay5State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 5, 1),
    _AiSPYRelay5State_Type()
)
aiSPYRelay5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay5State.setStatus("mandatory")


class _AiSPYRelay5Status_Type(Integer32):
    """Custom type aiSPYRelay5Status based on Integer32"""
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


_AiSPYRelay5Status_Type.__name__ = "Integer32"
_AiSPYRelay5Status_Object = MibScalar
aiSPYRelay5Status = _AiSPYRelay5Status_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 5, 2),
    _AiSPYRelay5Status_Type()
)
aiSPYRelay5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYRelay5Status.setStatus("mandatory")
_AiSPYRelay5Label_Type = DisplayString
_AiSPYRelay5Label_Object = MibScalar
aiSPYRelay5Label = _AiSPYRelay5Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 5, 3),
    _AiSPYRelay5Label_Type()
)
aiSPYRelay5Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay5Label.setStatus("mandatory")


class _AiSPYRelay5Time_Type(Integer32):
    """Custom type aiSPYRelay5Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYRelay5Time_Type.__name__ = "Integer32"
_AiSPYRelay5Time_Object = MibScalar
aiSPYRelay5Time = _AiSPYRelay5Time_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 5, 4),
    _AiSPYRelay5Time_Type()
)
aiSPYRelay5Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay5Time.setStatus("mandatory")
_AiSPYRelay6_ObjectIdentity = ObjectIdentity
aiSPYRelay6 = _AiSPYRelay6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 6)
)


class _AiSPYRelay6State_Type(Integer32):
    """Custom type aiSPYRelay6State based on Integer32"""
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


_AiSPYRelay6State_Type.__name__ = "Integer32"
_AiSPYRelay6State_Object = MibScalar
aiSPYRelay6State = _AiSPYRelay6State_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 6, 1),
    _AiSPYRelay6State_Type()
)
aiSPYRelay6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay6State.setStatus("mandatory")


class _AiSPYRelay6Status_Type(Integer32):
    """Custom type aiSPYRelay6Status based on Integer32"""
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


_AiSPYRelay6Status_Type.__name__ = "Integer32"
_AiSPYRelay6Status_Object = MibScalar
aiSPYRelay6Status = _AiSPYRelay6Status_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 6, 2),
    _AiSPYRelay6Status_Type()
)
aiSPYRelay6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYRelay6Status.setStatus("mandatory")
_AiSPYRelay6Label_Type = DisplayString
_AiSPYRelay6Label_Object = MibScalar
aiSPYRelay6Label = _AiSPYRelay6Label_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 6, 3),
    _AiSPYRelay6Label_Type()
)
aiSPYRelay6Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay6Label.setStatus("mandatory")


class _AiSPYRelay6Time_Type(Integer32):
    """Custom type aiSPYRelay6Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AiSPYRelay6Time_Type.__name__ = "Integer32"
_AiSPYRelay6Time_Object = MibScalar
aiSPYRelay6Time = _AiSPYRelay6Time_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 4, 6, 4),
    _AiSPYRelay6Time_Type()
)
aiSPYRelay6Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYRelay6Time.setStatus("mandatory")
_AiSPYAlarms_ObjectIdentity = ObjectIdentity
aiSPYAlarms = _AiSPYAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5)
)
_AiSPYAlarmsPresent_Type = Gauge32
_AiSPYAlarmsPresent_Object = MibScalar
aiSPYAlarmsPresent = _AiSPYAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 1),
    _AiSPYAlarmsPresent_Type()
)
aiSPYAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYAlarmsPresent.setStatus("current")
_AiSPYAlarmTable_Object = MibTable
aiSPYAlarmTable = _AiSPYAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 2)
)
if mibBuilder.loadTexts:
    aiSPYAlarmTable.setStatus("current")
_AiSPYAlarmEntry_Object = MibTableRow
aiSPYAlarmEntry = _AiSPYAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 2, 1)
)
aiSPYAlarmEntry.setIndexNames(
    (0, "AISPY-MIB", "aiSPYAlarmId"),
)
if mibBuilder.loadTexts:
    aiSPYAlarmEntry.setStatus("current")
_AiSPYAlarmId_Type = Integer32
_AiSPYAlarmId_Object = MibTableColumn
aiSPYAlarmId = _AiSPYAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 2, 1, 1),
    _AiSPYAlarmId_Type()
)
aiSPYAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aiSPYAlarmId.setStatus("current")
_AiSPYAlarmDescr_Type = ObjectIdentifier
_AiSPYAlarmDescr_Object = MibTableColumn
aiSPYAlarmDescr = _AiSPYAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 2, 1, 2),
    _AiSPYAlarmDescr_Type()
)
aiSPYAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYAlarmDescr.setStatus("current")
_AiSPYWellKnownAlarms_ObjectIdentity = ObjectIdentity
aiSPYWellKnownAlarms = _AiSPYWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3)
)
_AiSPYInput1HighAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput1HighAlarm = _AiSPYInput1HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 1)
)
if mibBuilder.loadTexts:
    aiSPYInput1HighAlarm.setStatus("current")
_AiSPYInput1LowAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput1LowAlarm = _AiSPYInput1LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 2)
)
if mibBuilder.loadTexts:
    aiSPYInput1LowAlarm.setStatus("current")
_AiSPYInput2HighAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput2HighAlarm = _AiSPYInput2HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 3)
)
if mibBuilder.loadTexts:
    aiSPYInput2HighAlarm.setStatus("current")
_AiSPYInput2LowAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput2LowAlarm = _AiSPYInput2LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 4)
)
if mibBuilder.loadTexts:
    aiSPYInput2LowAlarm.setStatus("current")
_AiSPYInput3HighAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput3HighAlarm = _AiSPYInput3HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 5)
)
if mibBuilder.loadTexts:
    aiSPYInput3HighAlarm.setStatus("current")
_AiSPYInput3LowAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput3LowAlarm = _AiSPYInput3LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 6)
)
if mibBuilder.loadTexts:
    aiSPYInput3LowAlarm.setStatus("current")
_AiSPYInput4HighAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput4HighAlarm = _AiSPYInput4HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 7)
)
if mibBuilder.loadTexts:
    aiSPYInput4HighAlarm.setStatus("current")
_AiSPYInput4LowAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput4LowAlarm = _AiSPYInput4LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 8)
)
if mibBuilder.loadTexts:
    aiSPYInput4LowAlarm.setStatus("current")
_AiSPYInput5HighAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput5HighAlarm = _AiSPYInput5HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 9)
)
if mibBuilder.loadTexts:
    aiSPYInput5HighAlarm.setStatus("current")
_AiSPYInput5LowAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput5LowAlarm = _AiSPYInput5LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 10)
)
if mibBuilder.loadTexts:
    aiSPYInput5LowAlarm.setStatus("current")
_AiSPYInput6HighAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput6HighAlarm = _AiSPYInput6HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 11)
)
if mibBuilder.loadTexts:
    aiSPYInput6HighAlarm.setStatus("current")
_AiSPYInput6LowAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput6LowAlarm = _AiSPYInput6LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 12)
)
if mibBuilder.loadTexts:
    aiSPYInput6LowAlarm.setStatus("current")
_AiSPYInput7HighAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput7HighAlarm = _AiSPYInput7HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 13)
)
if mibBuilder.loadTexts:
    aiSPYInput7HighAlarm.setStatus("current")
_AiSPYInput7LowAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput7LowAlarm = _AiSPYInput7LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 14)
)
if mibBuilder.loadTexts:
    aiSPYInput7LowAlarm.setStatus("current")
_AiSPYInput8HighAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput8HighAlarm = _AiSPYInput8HighAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 15)
)
if mibBuilder.loadTexts:
    aiSPYInput8HighAlarm.setStatus("current")
_AiSPYInput8LowAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput8LowAlarm = _AiSPYInput8LowAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 16)
)
if mibBuilder.loadTexts:
    aiSPYInput8LowAlarm.setStatus("current")
_AiSPYInput1DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput1DigAlarm = _AiSPYInput1DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 17)
)
if mibBuilder.loadTexts:
    aiSPYInput1DigAlarm.setStatus("current")
_AiSPYInput2DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput2DigAlarm = _AiSPYInput2DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 18)
)
if mibBuilder.loadTexts:
    aiSPYInput2DigAlarm.setStatus("current")
_AiSPYInput3DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput3DigAlarm = _AiSPYInput3DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 19)
)
if mibBuilder.loadTexts:
    aiSPYInput3DigAlarm.setStatus("current")
_AiSPYInput4DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput4DigAlarm = _AiSPYInput4DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 20)
)
if mibBuilder.loadTexts:
    aiSPYInput4DigAlarm.setStatus("current")
_AiSPYInput5DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput5DigAlarm = _AiSPYInput5DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 21)
)
if mibBuilder.loadTexts:
    aiSPYInput5DigAlarm.setStatus("current")
_AiSPYInput6DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput6DigAlarm = _AiSPYInput6DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 22)
)
if mibBuilder.loadTexts:
    aiSPYInput6DigAlarm.setStatus("current")
_AiSPYInput7DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput7DigAlarm = _AiSPYInput7DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 23)
)
if mibBuilder.loadTexts:
    aiSPYInput7DigAlarm.setStatus("current")
_AiSPYInput8DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput8DigAlarm = _AiSPYInput8DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 24)
)
if mibBuilder.loadTexts:
    aiSPYInput8DigAlarm.setStatus("current")
_AiSPYInput9DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput9DigAlarm = _AiSPYInput9DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 25)
)
if mibBuilder.loadTexts:
    aiSPYInput9DigAlarm.setStatus("current")
_AiSPYInput10DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput10DigAlarm = _AiSPYInput10DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 26)
)
if mibBuilder.loadTexts:
    aiSPYInput10DigAlarm.setStatus("current")
_AiSPYInput11DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput11DigAlarm = _AiSPYInput11DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 27)
)
if mibBuilder.loadTexts:
    aiSPYInput11DigAlarm.setStatus("current")
_AiSPYInput12DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput12DigAlarm = _AiSPYInput12DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 28)
)
if mibBuilder.loadTexts:
    aiSPYInput12DigAlarm.setStatus("current")
_AiSPYInput13DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput13DigAlarm = _AiSPYInput13DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 29)
)
if mibBuilder.loadTexts:
    aiSPYInput13DigAlarm.setStatus("current")
_AiSPYInput14DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput14DigAlarm = _AiSPYInput14DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 30)
)
if mibBuilder.loadTexts:
    aiSPYInput14DigAlarm.setStatus("current")
_AiSPYInput15DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput15DigAlarm = _AiSPYInput15DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 31)
)
if mibBuilder.loadTexts:
    aiSPYInput15DigAlarm.setStatus("current")
_AiSPYInput16DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput16DigAlarm = _AiSPYInput16DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 32)
)
if mibBuilder.loadTexts:
    aiSPYInput16DigAlarm.setStatus("current")
_AiSPYInput17DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput17DigAlarm = _AiSPYInput17DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 33)
)
if mibBuilder.loadTexts:
    aiSPYInput17DigAlarm.setStatus("current")
_AiSPYInput18DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput18DigAlarm = _AiSPYInput18DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 34)
)
if mibBuilder.loadTexts:
    aiSPYInput18DigAlarm.setStatus("current")
_AiSPYInput19DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput19DigAlarm = _AiSPYInput19DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 35)
)
if mibBuilder.loadTexts:
    aiSPYInput19DigAlarm.setStatus("current")
_AiSPYInput20DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput20DigAlarm = _AiSPYInput20DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 36)
)
if mibBuilder.loadTexts:
    aiSPYInput20DigAlarm.setStatus("current")
_AiSPYInput21DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput21DigAlarm = _AiSPYInput21DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 37)
)
if mibBuilder.loadTexts:
    aiSPYInput21DigAlarm.setStatus("current")
_AiSPYInput22DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput22DigAlarm = _AiSPYInput22DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 38)
)
if mibBuilder.loadTexts:
    aiSPYInput22DigAlarm.setStatus("current")
_AiSPYInput23DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput23DigAlarm = _AiSPYInput23DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 39)
)
if mibBuilder.loadTexts:
    aiSPYInput23DigAlarm.setStatus("current")
_AiSPYInput24DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput24DigAlarm = _AiSPYInput24DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 40)
)
if mibBuilder.loadTexts:
    aiSPYInput24DigAlarm.setStatus("current")
_AiSPYInput25DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput25DigAlarm = _AiSPYInput25DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 41)
)
if mibBuilder.loadTexts:
    aiSPYInput25DigAlarm.setStatus("current")
_AiSPYInput26DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput26DigAlarm = _AiSPYInput26DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 42)
)
if mibBuilder.loadTexts:
    aiSPYInput26DigAlarm.setStatus("current")
_AiSPYInput27DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput27DigAlarm = _AiSPYInput27DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 43)
)
if mibBuilder.loadTexts:
    aiSPYInput27DigAlarm.setStatus("current")
_AiSPYInput28DigAlarm_ObjectIdentity = ObjectIdentity
aiSPYInput28DigAlarm = _AiSPYInput28DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 44)
)
if mibBuilder.loadTexts:
    aiSPYInput28DigAlarm.setStatus("current")
_AiSPYOnBatteryAlarm_ObjectIdentity = ObjectIdentity
aiSPYOnBatteryAlarm = _AiSPYOnBatteryAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 96)
)
if mibBuilder.loadTexts:
    aiSPYOnBatteryAlarm.setStatus("current")
_AiSPYLowBatteryAlarm_ObjectIdentity = ObjectIdentity
aiSPYLowBatteryAlarm = _AiSPYLowBatteryAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 5, 3, 97)
)
if mibBuilder.loadTexts:
    aiSPYLowBatteryAlarm.setStatus("current")
_AiSPYTraps_ObjectIdentity = ObjectIdentity
aiSPYTraps = _AiSPYTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 6)
)
_AiSPYAlarmHistory_ObjectIdentity = ObjectIdentity
aiSPYAlarmHistory = _AiSPYAlarmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 7)
)
_AiSPYAlarmHistoryEntries_Type = Gauge32
_AiSPYAlarmHistoryEntries_Object = MibScalar
aiSPYAlarmHistoryEntries = _AiSPYAlarmHistoryEntries_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 7, 1),
    _AiSPYAlarmHistoryEntries_Type()
)
aiSPYAlarmHistoryEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYAlarmHistoryEntries.setStatus("current")


class _AiSPYAlarmHistoryClear_Type(Integer32):
    """Custom type aiSPYAlarmHistoryClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearbuffer", 1)
    )


_AiSPYAlarmHistoryClear_Type.__name__ = "Integer32"
_AiSPYAlarmHistoryClear_Object = MibScalar
aiSPYAlarmHistoryClear = _AiSPYAlarmHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 7, 2),
    _AiSPYAlarmHistoryClear_Type()
)
aiSPYAlarmHistoryClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYAlarmHistoryClear.setStatus("mandatory")
_AiSPYAlarmHistoryTable_Object = MibTable
aiSPYAlarmHistoryTable = _AiSPYAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 7, 3)
)
if mibBuilder.loadTexts:
    aiSPYAlarmHistoryTable.setStatus("current")
_AiSPYAlarmHistoryEntry_Object = MibTableRow
aiSPYAlarmHistoryEntry = _AiSPYAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 7, 3, 1)
)
aiSPYAlarmHistoryEntry.setIndexNames(
    (0, "AISPY-MIB", "aiSPYAlarmHistoryId"),
)
if mibBuilder.loadTexts:
    aiSPYAlarmHistoryEntry.setStatus("current")
_AiSPYAlarmHistoryId_Type = Integer32
_AiSPYAlarmHistoryId_Object = MibTableColumn
aiSPYAlarmHistoryId = _AiSPYAlarmHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 7, 3, 1, 1),
    _AiSPYAlarmHistoryId_Type()
)
aiSPYAlarmHistoryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aiSPYAlarmHistoryId.setStatus("current")
_AiSPYAlarmHistoryText_Type = DisplayString
_AiSPYAlarmHistoryText_Object = MibTableColumn
aiSPYAlarmHistoryText = _AiSPYAlarmHistoryText_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 7, 3, 1, 2),
    _AiSPYAlarmHistoryText_Type()
)
aiSPYAlarmHistoryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSPYAlarmHistoryText.setStatus("current")
_AiSPYTrapSettings_ObjectIdentity = ObjectIdentity
aiSPYTrapSettings = _AiSPYTrapSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 20, 8)
)


class _AiSPYPersistantTraps_Type(Integer32):
    """Custom type aiSPYPersistantTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AiSPYPersistantTraps_Type.__name__ = "Integer32"
_AiSPYPersistantTraps_Object = MibScalar
aiSPYPersistantTraps = _AiSPYPersistantTraps_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 8, 1),
    _AiSPYPersistantTraps_Type()
)
aiSPYPersistantTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYPersistantTraps.setStatus("mandatory")


class _AiSPYAlarmAcknowledge_Type(Integer32):
    """Custom type aiSPYAlarmAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("acknowledgealarms", 1)
    )


_AiSPYAlarmAcknowledge_Type.__name__ = "Integer32"
_AiSPYAlarmAcknowledge_Object = MibScalar
aiSPYAlarmAcknowledge = _AiSPYAlarmAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 539, 20, 8, 2),
    _AiSPYAlarmAcknowledge_Type()
)
aiSPYAlarmAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSPYAlarmAcknowledge.setStatus("mandatory")

# Managed Objects groups


# Notification objects

aiSPYAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 20, 6, 0, 1)
)
if mibBuilder.loadTexts:
    aiSPYAlarmEntryAdded.setStatus(
        ""
    )

aiSPYAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 20, 6, 0, 2)
)
if mibBuilder.loadTexts:
    aiSPYAlarmEntryRemoved.setStatus(
        ""
    )

aiSPYAccessGranted = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 20, 6, 0, 3)
)
if mibBuilder.loadTexts:
    aiSPYAccessGranted.setStatus(
        ""
    )

aiSPYAccessDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 20, 6, 0, 4)
)
if mibBuilder.loadTexts:
    aiSPYAccessDenied.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISPY-MIB",
    **{"aii": aii,
       "aiSPY": aiSPY,
       "aiSPYIdent": aiSPYIdent,
       "aiSPYIdentManufacturer": aiSPYIdentManufacturer,
       "aiSPYIdentModel": aiSPYIdentModel,
       "aiSPYIdentSoftwareVersion": aiSPYIdentSoftwareVersion,
       "aiSPYIdentSpecific": aiSPYIdentSpecific,
       "aiSPYSystem": aiSPYSystem,
       "aiSPYClock": aiSPYClock,
       "aiSPYDoorAlarmBypass": aiSPYDoorAlarmBypass,
       "aiSPYKeypad": aiSPYKeypad,
       "aiSPYKeypadCode1": aiSPYKeypadCode1,
       "aiSPYKeypadName1": aiSPYKeypadName1,
       "aiSPYKeypadCode2": aiSPYKeypadCode2,
       "aiSPYKeypadName2": aiSPYKeypadName2,
       "aiSPYKeypadCode3": aiSPYKeypadCode3,
       "aiSPYKeypadName3": aiSPYKeypadName3,
       "aiSPYKeypadCode4": aiSPYKeypadCode4,
       "aiSPYKeypadName4": aiSPYKeypadName4,
       "aiSPYKeypadCode5": aiSPYKeypadCode5,
       "aiSPYKeypadName5": aiSPYKeypadName5,
       "aiSPYKeypadCode6": aiSPYKeypadCode6,
       "aiSPYKeypadName6": aiSPYKeypadName6,
       "aiSPYKeypadCode7": aiSPYKeypadCode7,
       "aiSPYKeypadName7": aiSPYKeypadName7,
       "aiSPYKeypadCode8": aiSPYKeypadCode8,
       "aiSPYKeypadName8": aiSPYKeypadName8,
       "aiSPYKeypadCode9": aiSPYKeypadCode9,
       "aiSPYKeypadName9": aiSPYKeypadName9,
       "aiSPYKeypadCode10": aiSPYKeypadCode10,
       "aiSPYKeypadName10": aiSPYKeypadName10,
       "aiSPYKeypadCode11": aiSPYKeypadCode11,
       "aiSPYKeypadName11": aiSPYKeypadName11,
       "aiSPYKeypadCode12": aiSPYKeypadCode12,
       "aiSPYKeypadName12": aiSPYKeypadName12,
       "aiSPYKeypadCode13": aiSPYKeypadCode13,
       "aiSPYKeypadName13": aiSPYKeypadName13,
       "aiSPYKeypadCode14": aiSPYKeypadCode14,
       "aiSPYKeypadName14": aiSPYKeypadName14,
       "aiSPYKeypadCode15": aiSPYKeypadCode15,
       "aiSPYKeypadName15": aiSPYKeypadName15,
       "aiSPYKeypadCode16": aiSPYKeypadCode16,
       "aiSPYKeypadName16": aiSPYKeypadName16,
       "aiSPYKeypadCode17": aiSPYKeypadCode17,
       "aiSPYKeypadName17": aiSPYKeypadName17,
       "aiSPYKeypadCode18": aiSPYKeypadCode18,
       "aiSPYKeypadName18": aiSPYKeypadName18,
       "aiSPYKeypadCode19": aiSPYKeypadCode19,
       "aiSPYKeypadName19": aiSPYKeypadName19,
       "aiSPYKeypadCode20": aiSPYKeypadCode20,
       "aiSPYKeypadName20": aiSPYKeypadName20,
       "aiSPYInputVoltage": aiSPYInputVoltage,
       "aiSPYOnBattery": aiSPYOnBattery,
       "aiSPYLowBatteryThreshold": aiSPYLowBatteryThreshold,
       "aiSPYAnalogAverage": aiSPYAnalogAverage,
       "aiSPYInputs": aiSPYInputs,
       "aiSPY8124": aiSPY8124,
       "aiSPYInput1": aiSPYInput1,
       "aiSPYInput1State": aiSPYInput1State,
       "aiSPYInput1Reading": aiSPYInput1Reading,
       "aiSPYInput1Gain": aiSPYInput1Gain,
       "aiSPYInput1Offset": aiSPYInput1Offset,
       "aiSPYInput1Label": aiSPYInput1Label,
       "aiSPYInput1UOM": aiSPYInput1UOM,
       "aiSPYInput1HighLimit": aiSPYInput1HighLimit,
       "aiSPYInput1LowLimit": aiSPYInput1LowLimit,
       "aiSPYInput1RlyControl": aiSPYInput1RlyControl,
       "aiSPYInput1Delay": aiSPYInput1Delay,
       "aiSPYInput1RTNDelay": aiSPYInput1RTNDelay,
       "aiSPYInput1Hysteresis": aiSPYInput1Hysteresis,
       "aiSPYInput2": aiSPYInput2,
       "aiSPYInput2State": aiSPYInput2State,
       "aiSPYInput2Reading": aiSPYInput2Reading,
       "aiSPYInput2Gain": aiSPYInput2Gain,
       "aiSPYInput2Offset": aiSPYInput2Offset,
       "aiSPYInput2Label": aiSPYInput2Label,
       "aiSPYInput2UOM": aiSPYInput2UOM,
       "aiSPYInput2HighLimit": aiSPYInput2HighLimit,
       "aiSPYInput2LowLimit": aiSPYInput2LowLimit,
       "aiSPYInput2RlyControl": aiSPYInput2RlyControl,
       "aiSPYInput2Delay": aiSPYInput2Delay,
       "aiSPYInput2RTNDelay": aiSPYInput2RTNDelay,
       "aiSPYInput2Hysteresis": aiSPYInput2Hysteresis,
       "aiSPYInput3": aiSPYInput3,
       "aiSPYInput3State": aiSPYInput3State,
       "aiSPYInput3Reading": aiSPYInput3Reading,
       "aiSPYInput3Gain": aiSPYInput3Gain,
       "aiSPYInput3Offset": aiSPYInput3Offset,
       "aiSPYInput3Label": aiSPYInput3Label,
       "aiSPYInput3UOM": aiSPYInput3UOM,
       "aiSPYInput3HighLimit": aiSPYInput3HighLimit,
       "aiSPYInput3LowLimit": aiSPYInput3LowLimit,
       "aiSPYInput3RlyControl": aiSPYInput3RlyControl,
       "aiSPYInput3Delay": aiSPYInput3Delay,
       "aiSPYInput3RTNDelay": aiSPYInput3RTNDelay,
       "aiSPYInput3Hysteresis": aiSPYInput3Hysteresis,
       "aiSPYInput4": aiSPYInput4,
       "aiSPYInput4State": aiSPYInput4State,
       "aiSPYInput4Reading": aiSPYInput4Reading,
       "aiSPYInput4Gain": aiSPYInput4Gain,
       "aiSPYInput4Offset": aiSPYInput4Offset,
       "aiSPYInput4Label": aiSPYInput4Label,
       "aiSPYInput4UOM": aiSPYInput4UOM,
       "aiSPYInput4HighLimit": aiSPYInput4HighLimit,
       "aiSPYInput4LowLimit": aiSPYInput4LowLimit,
       "aiSPYInput4RlyControl": aiSPYInput4RlyControl,
       "aiSPYInput4Delay": aiSPYInput4Delay,
       "aiSPYInput4RTNDelay": aiSPYInput4RTNDelay,
       "aiSPYInput4Hysteresis": aiSPYInput4Hysteresis,
       "aiSPYInput5": aiSPYInput5,
       "aiSPYInput5State": aiSPYInput5State,
       "aiSPYInput5Reading": aiSPYInput5Reading,
       "aiSPYInput5Gain": aiSPYInput5Gain,
       "aiSPYInput5Offset": aiSPYInput5Offset,
       "aiSPYInput5Label": aiSPYInput5Label,
       "aiSPYInput5UOM": aiSPYInput5UOM,
       "aiSPYInput5HighLimit": aiSPYInput5HighLimit,
       "aiSPYInput5LowLimit": aiSPYInput5LowLimit,
       "aiSPYInput5RlyControl": aiSPYInput5RlyControl,
       "aiSPYInput5Delay": aiSPYInput5Delay,
       "aiSPYInput5RTNDelay": aiSPYInput5RTNDelay,
       "aiSPYInput5Hysteresis": aiSPYInput5Hysteresis,
       "aiSPYInput6": aiSPYInput6,
       "aiSPYInput6State": aiSPYInput6State,
       "aiSPYInput6Reading": aiSPYInput6Reading,
       "aiSPYInput6Gain": aiSPYInput6Gain,
       "aiSPYInput6Offset": aiSPYInput6Offset,
       "aiSPYInput6Label": aiSPYInput6Label,
       "aiSPYInput6UOM": aiSPYInput6UOM,
       "aiSPYInput6HighLimit": aiSPYInput6HighLimit,
       "aiSPYInput6LowLimit": aiSPYInput6LowLimit,
       "aiSPYInput6RlyControl": aiSPYInput6RlyControl,
       "aiSPYInput6Delay": aiSPYInput6Delay,
       "aiSPYInput6RTNDelay": aiSPYInput6RTNDelay,
       "aiSPYInput6Hysteresis": aiSPYInput6Hysteresis,
       "aiSPYInput7": aiSPYInput7,
       "aiSPYInput7State": aiSPYInput7State,
       "aiSPYInput7Reading": aiSPYInput7Reading,
       "aiSPYInput7Gain": aiSPYInput7Gain,
       "aiSPYInput7Offset": aiSPYInput7Offset,
       "aiSPYInput7Label": aiSPYInput7Label,
       "aiSPYInput7UOM": aiSPYInput7UOM,
       "aiSPYInput7HighLimit": aiSPYInput7HighLimit,
       "aiSPYInput7LowLimit": aiSPYInput7LowLimit,
       "aiSPYInput7RlyControl": aiSPYInput7RlyControl,
       "aiSPYInput7Delay": aiSPYInput7Delay,
       "aiSPYInput7RTNDelay": aiSPYInput7RTNDelay,
       "aiSPYInput7Hysteresis": aiSPYInput7Hysteresis,
       "aiSPYInput8": aiSPYInput8,
       "aiSPYInput8State": aiSPYInput8State,
       "aiSPYInput8Reading": aiSPYInput8Reading,
       "aiSPYInput8Gain": aiSPYInput8Gain,
       "aiSPYInput8Offset": aiSPYInput8Offset,
       "aiSPYInput8Label": aiSPYInput8Label,
       "aiSPYInput8UOM": aiSPYInput8UOM,
       "aiSPYInput8HighLimit": aiSPYInput8HighLimit,
       "aiSPYInput8LowLimit": aiSPYInput8LowLimit,
       "aiSPYInput8RlyControl": aiSPYInput8RlyControl,
       "aiSPYInput8Delay": aiSPYInput8Delay,
       "aiSPYInput8RTNDelay": aiSPYInput8RTNDelay,
       "aiSPYInput8Hysteresis": aiSPYInput8Hysteresis,
       "aiSPYInput9": aiSPYInput9,
       "aiSPYInput9State": aiSPYInput9State,
       "aiSPYInput9Reading": aiSPYInput9Reading,
       "aiSPYInput9Label": aiSPYInput9Label,
       "aiSPYInput9RlyControl": aiSPYInput9RlyControl,
       "aiSPYInput9Delay": aiSPYInput9Delay,
       "aiSPYInput9RTNDelay": aiSPYInput9RTNDelay,
       "aiSPYInput10": aiSPYInput10,
       "aiSPYInput10State": aiSPYInput10State,
       "aiSPYInput10Reading": aiSPYInput10Reading,
       "aiSPYInput10Label": aiSPYInput10Label,
       "aiSPYInput10RlyControl": aiSPYInput10RlyControl,
       "aiSPYInput10Delay": aiSPYInput10Delay,
       "aiSPYInput10RTNDelay": aiSPYInput10RTNDelay,
       "aiSPYInput11": aiSPYInput11,
       "aiSPYInput11State": aiSPYInput11State,
       "aiSPYInput11Reading": aiSPYInput11Reading,
       "aiSPYInput11Label": aiSPYInput11Label,
       "aiSPYInput11RlyControl": aiSPYInput11RlyControl,
       "aiSPYInput11Delay": aiSPYInput11Delay,
       "aiSPYInput11RTNDelay": aiSPYInput11RTNDelay,
       "aiSPYInput12": aiSPYInput12,
       "aiSPYInput12State": aiSPYInput12State,
       "aiSPYInput12Reading": aiSPYInput12Reading,
       "aiSPYInput12Label": aiSPYInput12Label,
       "aiSPYInput12RlyControl": aiSPYInput12RlyControl,
       "aiSPYInput12Delay": aiSPYInput12Delay,
       "aiSPYInput12RTNDelay": aiSPYInput12RTNDelay,
       "aiSPYInput13": aiSPYInput13,
       "aiSPYInput13State": aiSPYInput13State,
       "aiSPYInput13Reading": aiSPYInput13Reading,
       "aiSPYInput13Label": aiSPYInput13Label,
       "aiSPYInput13RlyControl": aiSPYInput13RlyControl,
       "aiSPYInput13Delay": aiSPYInput13Delay,
       "aiSPYInput13RTNDelay": aiSPYInput13RTNDelay,
       "aiSPYInput14": aiSPYInput14,
       "aiSPYInput14State": aiSPYInput14State,
       "aiSPYInput14Reading": aiSPYInput14Reading,
       "aiSPYInput14Label": aiSPYInput14Label,
       "aiSPYInput14RlyControl": aiSPYInput14RlyControl,
       "aiSPYInput14Delay": aiSPYInput14Delay,
       "aiSPYInput14RTNDelay": aiSPYInput14RTNDelay,
       "aiSPYInput15": aiSPYInput15,
       "aiSPYInput15State": aiSPYInput15State,
       "aiSPYInput15Reading": aiSPYInput15Reading,
       "aiSPYInput15Label": aiSPYInput15Label,
       "aiSPYInput15RlyControl": aiSPYInput15RlyControl,
       "aiSPYInput15Delay": aiSPYInput15Delay,
       "aiSPYInput15RTNDelay": aiSPYInput15RTNDelay,
       "aiSPYInput16": aiSPYInput16,
       "aiSPYInput16State": aiSPYInput16State,
       "aiSPYInput16Reading": aiSPYInput16Reading,
       "aiSPYInput16Label": aiSPYInput16Label,
       "aiSPYInput16RlyControl": aiSPYInput16RlyControl,
       "aiSPYInput16Delay": aiSPYInput16Delay,
       "aiSPYInput16RTNDelay": aiSPYInput16RTNDelay,
       "aiSPYInput17": aiSPYInput17,
       "aiSPYInput17State": aiSPYInput17State,
       "aiSPYInput17Reading": aiSPYInput17Reading,
       "aiSPYInput17Label": aiSPYInput17Label,
       "aiSPYInput17RlyControl": aiSPYInput17RlyControl,
       "aiSPYInput17Delay": aiSPYInput17Delay,
       "aiSPYInput17RTNDelay": aiSPYInput17RTNDelay,
       "aiSPYInput18": aiSPYInput18,
       "aiSPYInput18State": aiSPYInput18State,
       "aiSPYInput18Reading": aiSPYInput18Reading,
       "aiSPYInput18Label": aiSPYInput18Label,
       "aiSPYInput18RlyControl": aiSPYInput18RlyControl,
       "aiSPYInput18Delay": aiSPYInput18Delay,
       "aiSPYInput18RTNDelay": aiSPYInput18RTNDelay,
       "aiSPYInput19": aiSPYInput19,
       "aiSPYInput19State": aiSPYInput19State,
       "aiSPYInput19Reading": aiSPYInput19Reading,
       "aiSPYInput19Label": aiSPYInput19Label,
       "aiSPYInput19RlyControl": aiSPYInput19RlyControl,
       "aiSPYInput19Delay": aiSPYInput19Delay,
       "aiSPYInput19RTNDelay": aiSPYInput19RTNDelay,
       "aiSPYInput20": aiSPYInput20,
       "aiSPYInput20State": aiSPYInput20State,
       "aiSPYInput20Reading": aiSPYInput20Reading,
       "aiSPYInput20Label": aiSPYInput20Label,
       "aiSPYInput20RlyControl": aiSPYInput20RlyControl,
       "aiSPYInput20Delay": aiSPYInput20Delay,
       "aiSPYInput20RTNDelay": aiSPYInput20RTNDelay,
       "aiSPYInput21": aiSPYInput21,
       "aiSPYInput21State": aiSPYInput21State,
       "aiSPYInput21Reading": aiSPYInput21Reading,
       "aiSPYInput21Label": aiSPYInput21Label,
       "aiSPYInput21RlyControl": aiSPYInput21RlyControl,
       "aiSPYInput21Delay": aiSPYInput21Delay,
       "aiSPYInput21RTNDelay": aiSPYInput21RTNDelay,
       "aiSPYInput22": aiSPYInput22,
       "aiSPYInput22State": aiSPYInput22State,
       "aiSPYInput22Reading": aiSPYInput22Reading,
       "aiSPYInput22Label": aiSPYInput22Label,
       "aiSPYInput22RlyControl": aiSPYInput22RlyControl,
       "aiSPYInput22Delay": aiSPYInput22Delay,
       "aiSPYInput22RTNDelay": aiSPYInput22RTNDelay,
       "aiSPYInput23": aiSPYInput23,
       "aiSPYInput23State": aiSPYInput23State,
       "aiSPYInput23Reading": aiSPYInput23Reading,
       "aiSPYInput23Label": aiSPYInput23Label,
       "aiSPYInput23RlyControl": aiSPYInput23RlyControl,
       "aiSPYInput23Delay": aiSPYInput23Delay,
       "aiSPYInput23RTNDelay": aiSPYInput23RTNDelay,
       "aiSPYInput24": aiSPYInput24,
       "aiSPYInput24State": aiSPYInput24State,
       "aiSPYInput24Reading": aiSPYInput24Reading,
       "aiSPYInput24Label": aiSPYInput24Label,
       "aiSPYInput24RlyControl": aiSPYInput24RlyControl,
       "aiSPYInput24Delay": aiSPYInput24Delay,
       "aiSPYInput24RTNDelay": aiSPYInput24RTNDelay,
       "aiSPYInput25": aiSPYInput25,
       "aiSPYInput25State": aiSPYInput25State,
       "aiSPYInput25Reading": aiSPYInput25Reading,
       "aiSPYInput25Label": aiSPYInput25Label,
       "aiSPYInput25RlyControl": aiSPYInput25RlyControl,
       "aiSPYInput25Delay": aiSPYInput25Delay,
       "aiSPYInput25RTNDelay": aiSPYInput25RTNDelay,
       "aiSPYInput26": aiSPYInput26,
       "aiSPYInput26State": aiSPYInput26State,
       "aiSPYInput26Reading": aiSPYInput26Reading,
       "aiSPYInput26Label": aiSPYInput26Label,
       "aiSPYInput26RlyControl": aiSPYInput26RlyControl,
       "aiSPYInput26Delay": aiSPYInput26Delay,
       "aiSPYInput26RTNDelay": aiSPYInput26RTNDelay,
       "aiSPYInput27": aiSPYInput27,
       "aiSPYInput27State": aiSPYInput27State,
       "aiSPYInput27Reading": aiSPYInput27Reading,
       "aiSPYInput27Label": aiSPYInput27Label,
       "aiSPYInput27RlyControl": aiSPYInput27RlyControl,
       "aiSPYInput27Delay": aiSPYInput27Delay,
       "aiSPYInput27RTNDelay": aiSPYInput27RTNDelay,
       "aiSPYInput28": aiSPYInput28,
       "aiSPYInput28State": aiSPYInput28State,
       "aiSPYInput28Reading": aiSPYInput28Reading,
       "aiSPYInput28Label": aiSPYInput28Label,
       "aiSPYInput28RlyControl": aiSPYInput28RlyControl,
       "aiSPYInput28Delay": aiSPYInput28Delay,
       "aiSPYInput28RTNDelay": aiSPYInput28RTNDelay,
       "aiSPYOutputs": aiSPYOutputs,
       "aiSPYRelay1": aiSPYRelay1,
       "aiSPYRelay1State": aiSPYRelay1State,
       "aiSPYRelay1Status": aiSPYRelay1Status,
       "aiSPYRelay1Label": aiSPYRelay1Label,
       "aiSPYRelay1Time": aiSPYRelay1Time,
       "aiSPYRelay2": aiSPYRelay2,
       "aiSPYRelay2State": aiSPYRelay2State,
       "aiSPYRelay2Status": aiSPYRelay2Status,
       "aiSPYRelay2Label": aiSPYRelay2Label,
       "aiSPYRelay2Time": aiSPYRelay2Time,
       "aiSPYRelay3": aiSPYRelay3,
       "aiSPYRelay3State": aiSPYRelay3State,
       "aiSPYRelay3Status": aiSPYRelay3Status,
       "aiSPYRelay3Label": aiSPYRelay3Label,
       "aiSPYRelay3Time": aiSPYRelay3Time,
       "aiSPYRelay4": aiSPYRelay4,
       "aiSPYRelay4State": aiSPYRelay4State,
       "aiSPYRelay4Status": aiSPYRelay4Status,
       "aiSPYRelay4Label": aiSPYRelay4Label,
       "aiSPYRelay4Time": aiSPYRelay4Time,
       "aiSPYRelay5": aiSPYRelay5,
       "aiSPYRelay5State": aiSPYRelay5State,
       "aiSPYRelay5Status": aiSPYRelay5Status,
       "aiSPYRelay5Label": aiSPYRelay5Label,
       "aiSPYRelay5Time": aiSPYRelay5Time,
       "aiSPYRelay6": aiSPYRelay6,
       "aiSPYRelay6State": aiSPYRelay6State,
       "aiSPYRelay6Status": aiSPYRelay6Status,
       "aiSPYRelay6Label": aiSPYRelay6Label,
       "aiSPYRelay6Time": aiSPYRelay6Time,
       "aiSPYAlarms": aiSPYAlarms,
       "aiSPYAlarmsPresent": aiSPYAlarmsPresent,
       "aiSPYAlarmTable": aiSPYAlarmTable,
       "aiSPYAlarmEntry": aiSPYAlarmEntry,
       "aiSPYAlarmId": aiSPYAlarmId,
       "aiSPYAlarmDescr": aiSPYAlarmDescr,
       "aiSPYWellKnownAlarms": aiSPYWellKnownAlarms,
       "aiSPYInput1HighAlarm": aiSPYInput1HighAlarm,
       "aiSPYInput1LowAlarm": aiSPYInput1LowAlarm,
       "aiSPYInput2HighAlarm": aiSPYInput2HighAlarm,
       "aiSPYInput2LowAlarm": aiSPYInput2LowAlarm,
       "aiSPYInput3HighAlarm": aiSPYInput3HighAlarm,
       "aiSPYInput3LowAlarm": aiSPYInput3LowAlarm,
       "aiSPYInput4HighAlarm": aiSPYInput4HighAlarm,
       "aiSPYInput4LowAlarm": aiSPYInput4LowAlarm,
       "aiSPYInput5HighAlarm": aiSPYInput5HighAlarm,
       "aiSPYInput5LowAlarm": aiSPYInput5LowAlarm,
       "aiSPYInput6HighAlarm": aiSPYInput6HighAlarm,
       "aiSPYInput6LowAlarm": aiSPYInput6LowAlarm,
       "aiSPYInput7HighAlarm": aiSPYInput7HighAlarm,
       "aiSPYInput7LowAlarm": aiSPYInput7LowAlarm,
       "aiSPYInput8HighAlarm": aiSPYInput8HighAlarm,
       "aiSPYInput8LowAlarm": aiSPYInput8LowAlarm,
       "aiSPYInput1DigAlarm": aiSPYInput1DigAlarm,
       "aiSPYInput2DigAlarm": aiSPYInput2DigAlarm,
       "aiSPYInput3DigAlarm": aiSPYInput3DigAlarm,
       "aiSPYInput4DigAlarm": aiSPYInput4DigAlarm,
       "aiSPYInput5DigAlarm": aiSPYInput5DigAlarm,
       "aiSPYInput6DigAlarm": aiSPYInput6DigAlarm,
       "aiSPYInput7DigAlarm": aiSPYInput7DigAlarm,
       "aiSPYInput8DigAlarm": aiSPYInput8DigAlarm,
       "aiSPYInput9DigAlarm": aiSPYInput9DigAlarm,
       "aiSPYInput10DigAlarm": aiSPYInput10DigAlarm,
       "aiSPYInput11DigAlarm": aiSPYInput11DigAlarm,
       "aiSPYInput12DigAlarm": aiSPYInput12DigAlarm,
       "aiSPYInput13DigAlarm": aiSPYInput13DigAlarm,
       "aiSPYInput14DigAlarm": aiSPYInput14DigAlarm,
       "aiSPYInput15DigAlarm": aiSPYInput15DigAlarm,
       "aiSPYInput16DigAlarm": aiSPYInput16DigAlarm,
       "aiSPYInput17DigAlarm": aiSPYInput17DigAlarm,
       "aiSPYInput18DigAlarm": aiSPYInput18DigAlarm,
       "aiSPYInput19DigAlarm": aiSPYInput19DigAlarm,
       "aiSPYInput20DigAlarm": aiSPYInput20DigAlarm,
       "aiSPYInput21DigAlarm": aiSPYInput21DigAlarm,
       "aiSPYInput22DigAlarm": aiSPYInput22DigAlarm,
       "aiSPYInput23DigAlarm": aiSPYInput23DigAlarm,
       "aiSPYInput24DigAlarm": aiSPYInput24DigAlarm,
       "aiSPYInput25DigAlarm": aiSPYInput25DigAlarm,
       "aiSPYInput26DigAlarm": aiSPYInput26DigAlarm,
       "aiSPYInput27DigAlarm": aiSPYInput27DigAlarm,
       "aiSPYInput28DigAlarm": aiSPYInput28DigAlarm,
       "aiSPYOnBatteryAlarm": aiSPYOnBatteryAlarm,
       "aiSPYLowBatteryAlarm": aiSPYLowBatteryAlarm,
       "aiSPYTraps": aiSPYTraps,
       "aiSPYAlarmEntryAdded": aiSPYAlarmEntryAdded,
       "aiSPYAlarmEntryRemoved": aiSPYAlarmEntryRemoved,
       "aiSPYAccessGranted": aiSPYAccessGranted,
       "aiSPYAccessDenied": aiSPYAccessDenied,
       "aiSPYAlarmHistory": aiSPYAlarmHistory,
       "aiSPYAlarmHistoryEntries": aiSPYAlarmHistoryEntries,
       "aiSPYAlarmHistoryClear": aiSPYAlarmHistoryClear,
       "aiSPYAlarmHistoryTable": aiSPYAlarmHistoryTable,
       "aiSPYAlarmHistoryEntry": aiSPYAlarmHistoryEntry,
       "aiSPYAlarmHistoryId": aiSPYAlarmHistoryId,
       "aiSPYAlarmHistoryText": aiSPYAlarmHistoryText,
       "aiSPYTrapSettings": aiSPYTrapSettings,
       "aiSPYPersistantTraps": aiSPYPersistantTraps,
       "aiSPYAlarmAcknowledge": aiSPYAlarmAcknowledge}
)
