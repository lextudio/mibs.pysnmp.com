# SNMP MIB module (OKIDATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OKIDATA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:55 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mib_2,
 private) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "private")

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

_Okidata_ObjectIdentity = ObjectIdentity
okidata = _Okidata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001)
)
_Peripheral_ObjectIdentity = ObjectIdentity
peripheral = _Peripheral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1)
)
_Printer_ObjectIdentity = ObjectIdentity
printer = _Printer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1)
)
_Nip_ObjectIdentity = ObjectIdentity
nip = _Nip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1)
)
_Niptype1_ObjectIdentity = ObjectIdentity
niptype1 = _Niptype1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1)
)
_Cfg_ObjectIdentity = ObjectIdentity
cfg = _Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1)
)


class _CfgPersonality_Type(DisplayString):
    """Custom type cfgPersonality based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPersonality_Type.__name__ = "DisplayString"
_CfgPersonality_Object = MibScalar
cfgPersonality = _CfgPersonality_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 20),
    _CfgPersonality_Type()
)
cfgPersonality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPersonality.setStatus("optional")


class _CfgManualFeed_Type(DisplayString):
    """Custom type cfgManualFeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgManualFeed_Type.__name__ = "DisplayString"
_CfgManualFeed_Object = MibScalar
cfgManualFeed = _CfgManualFeed_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 30),
    _CfgManualFeed_Type()
)
cfgManualFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgManualFeed.setStatus("optional")


class _CfgOkiPaperFeed_Type(DisplayString):
    """Custom type cfgOkiPaperFeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiPaperFeed_Type.__name__ = "DisplayString"
_CfgOkiPaperFeed_Object = MibScalar
cfgOkiPaperFeed = _CfgOkiPaperFeed_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 40),
    _CfgOkiPaperFeed_Type()
)
cfgOkiPaperFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiPaperFeed.setStatus("optional")


class _CfgOkiAutoTraySwitch_Type(DisplayString):
    """Custom type cfgOkiAutoTraySwitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiAutoTraySwitch_Type.__name__ = "DisplayString"
_CfgOkiAutoTraySwitch_Object = MibScalar
cfgOkiAutoTraySwitch = _CfgOkiAutoTraySwitch_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 50),
    _CfgOkiAutoTraySwitch_Type()
)
cfgOkiAutoTraySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiAutoTraySwitch.setStatus("optional")


class _CfgOkiPriorityTray_Type(DisplayString):
    """Custom type cfgOkiPriorityTray based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiPriorityTray_Type.__name__ = "DisplayString"
_CfgOkiPriorityTray_Object = MibScalar
cfgOkiPriorityTray = _CfgOkiPriorityTray_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 55),
    _CfgOkiPriorityTray_Type()
)
cfgOkiPriorityTray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiPriorityTray.setStatus("optional")


class _CfgPaper_Type(DisplayString):
    """Custom type cfgPaper based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPaper_Type.__name__ = "DisplayString"
_CfgPaper_Object = MibScalar
cfgPaper = _CfgPaper_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 60),
    _CfgPaper_Type()
)
cfgPaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPaper.setStatus("optional")


class _CfgOkiCustomPaperWidth_Type(DisplayString):
    """Custom type cfgOkiCustomPaperWidth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiCustomPaperWidth_Type.__name__ = "DisplayString"
_CfgOkiCustomPaperWidth_Object = MibScalar
cfgOkiCustomPaperWidth = _CfgOkiCustomPaperWidth_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 61),
    _CfgOkiCustomPaperWidth_Type()
)
cfgOkiCustomPaperWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiCustomPaperWidth.setStatus("optional")


class _CfgOkiCustomPaperLength_Type(DisplayString):
    """Custom type cfgOkiCustomPaperLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiCustomPaperLength_Type.__name__ = "DisplayString"
_CfgOkiCustomPaperLength_Object = MibScalar
cfgOkiCustomPaperLength = _CfgOkiCustomPaperLength_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 62),
    _CfgOkiCustomPaperLength_Type()
)
cfgOkiCustomPaperLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiCustomPaperLength.setStatus("optional")


class _CfgInTray2Size_Type(DisplayString):
    """Custom type cfgInTray2Size based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgInTray2Size_Type.__name__ = "DisplayString"
_CfgInTray2Size_Object = MibScalar
cfgInTray2Size = _CfgInTray2Size_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 70),
    _CfgInTray2Size_Type()
)
cfgInTray2Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgInTray2Size.setStatus("optional")


class _CfgInTray3Size_Type(DisplayString):
    """Custom type cfgInTray3Size based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgInTray3Size_Type.__name__ = "DisplayString"
_CfgInTray3Size_Object = MibScalar
cfgInTray3Size = _CfgInTray3Size_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 80),
    _CfgInTray3Size_Type()
)
cfgInTray3Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgInTray3Size.setStatus("optional")


class _CfgInTray5Size_Type(DisplayString):
    """Custom type cfgInTray5Size based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgInTray5Size_Type.__name__ = "DisplayString"
_CfgInTray5Size_Object = MibScalar
cfgInTray5Size = _CfgInTray5Size_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 90),
    _CfgInTray5Size_Type()
)
cfgInTray5Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgInTray5Size.setStatus("optional")


class _CfgInTray1Size_Type(DisplayString):
    """Custom type cfgInTray1Size based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgInTray1Size_Type.__name__ = "DisplayString"
_CfgInTray1Size_Object = MibScalar
cfgInTray1Size = _CfgInTray1Size_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 100),
    _CfgInTray1Size_Type()
)
cfgInTray1Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgInTray1Size.setStatus("optional")


class _CfgInTray4Size_Type(DisplayString):
    """Custom type cfgInTray4Size based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgInTray4Size_Type.__name__ = "DisplayString"
_CfgInTray4Size_Object = MibScalar
cfgInTray4Size = _CfgInTray4Size_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 110),
    _CfgInTray4Size_Type()
)
cfgInTray4Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgInTray4Size.setStatus("optional")


class _CfgOkiMediaInTray2_Type(DisplayString):
    """Custom type cfgOkiMediaInTray2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiMediaInTray2_Type.__name__ = "DisplayString"
_CfgOkiMediaInTray2_Object = MibScalar
cfgOkiMediaInTray2 = _CfgOkiMediaInTray2_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 120),
    _CfgOkiMediaInTray2_Type()
)
cfgOkiMediaInTray2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiMediaInTray2.setStatus("optional")


class _CfgOkiMediaInTray3_Type(DisplayString):
    """Custom type cfgOkiMediaInTray3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiMediaInTray3_Type.__name__ = "DisplayString"
_CfgOkiMediaInTray3_Object = MibScalar
cfgOkiMediaInTray3 = _CfgOkiMediaInTray3_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 130),
    _CfgOkiMediaInTray3_Type()
)
cfgOkiMediaInTray3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiMediaInTray3.setStatus("optional")


class _CfgOkiMediaInTray5_Type(DisplayString):
    """Custom type cfgOkiMediaInTray5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiMediaInTray5_Type.__name__ = "DisplayString"
_CfgOkiMediaInTray5_Object = MibScalar
cfgOkiMediaInTray5 = _CfgOkiMediaInTray5_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 140),
    _CfgOkiMediaInTray5_Type()
)
cfgOkiMediaInTray5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiMediaInTray5.setStatus("optional")


class _CfgOkiMediaInTray1_Type(DisplayString):
    """Custom type cfgOkiMediaInTray1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiMediaInTray1_Type.__name__ = "DisplayString"
_CfgOkiMediaInTray1_Object = MibScalar
cfgOkiMediaInTray1 = _CfgOkiMediaInTray1_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 150),
    _CfgOkiMediaInTray1_Type()
)
cfgOkiMediaInTray1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiMediaInTray1.setStatus("optional")


class _CfgOkiMediaInTray4_Type(DisplayString):
    """Custom type cfgOkiMediaInTray4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiMediaInTray4_Type.__name__ = "DisplayString"
_CfgOkiMediaInTray4_Object = MibScalar
cfgOkiMediaInTray4 = _CfgOkiMediaInTray4_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 160),
    _CfgOkiMediaInTray4_Type()
)
cfgOkiMediaInTray4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiMediaInTray4.setStatus("optional")


class _CfgOkiPaperSizeCheck_Type(DisplayString):
    """Custom type cfgOkiPaperSizeCheck based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiPaperSizeCheck_Type.__name__ = "DisplayString"
_CfgOkiPaperSizeCheck_Object = MibScalar
cfgOkiPaperSizeCheck = _CfgOkiPaperSizeCheck_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 170),
    _CfgOkiPaperSizeCheck_Type()
)
cfgOkiPaperSizeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiPaperSizeCheck.setStatus("optional")


class _CfgMptray_Type(DisplayString):
    """Custom type cfgMptray based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgMptray_Type.__name__ = "DisplayString"
_CfgMptray_Object = MibScalar
cfgMptray = _CfgMptray_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 180),
    _CfgMptray_Type()
)
cfgMptray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgMptray.setStatus("optional")


class _CfgIntray1_Type(DisplayString):
    """Custom type cfgIntray1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIntray1_Type.__name__ = "DisplayString"
_CfgIntray1_Object = MibScalar
cfgIntray1 = _CfgIntray1_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 190),
    _CfgIntray1_Type()
)
cfgIntray1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgIntray1.setStatus("optional")


class _CfgIntray2_Type(DisplayString):
    """Custom type cfgIntray2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIntray2_Type.__name__ = "DisplayString"
_CfgIntray2_Object = MibScalar
cfgIntray2 = _CfgIntray2_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 200),
    _CfgIntray2_Type()
)
cfgIntray2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgIntray2.setStatus("optional")


class _CfgIntray3_Type(DisplayString):
    """Custom type cfgIntray3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIntray3_Type.__name__ = "DisplayString"
_CfgIntray3_Object = MibScalar
cfgIntray3 = _CfgIntray3_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 210),
    _CfgIntray3_Type()
)
cfgIntray3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgIntray3.setStatus("optional")


class _CfgCopies_Type(DisplayString):
    """Custom type cfgCopies based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgCopies_Type.__name__ = "DisplayString"
_CfgCopies_Object = MibScalar
cfgCopies = _CfgCopies_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 220),
    _CfgCopies_Type()
)
cfgCopies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCopies.setStatus("optional")


class _CfgDuplex_Type(DisplayString):
    """Custom type cfgDuplex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgDuplex_Type.__name__ = "DisplayString"
_CfgDuplex_Object = MibScalar
cfgDuplex = _CfgDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 230),
    _CfgDuplex_Type()
)
cfgDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDuplex.setStatus("optional")


class _CfgBinding_Type(DisplayString):
    """Custom type cfgBinding based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgBinding_Type.__name__ = "DisplayString"
_CfgBinding_Object = MibScalar
cfgBinding = _CfgBinding_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 240),
    _CfgBinding_Type()
)
cfgBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgBinding.setStatus("optional")


class _CfgPclFontSource_Type(DisplayString):
    """Custom type cfgPclFontSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclFontSource_Type.__name__ = "DisplayString"
_CfgPclFontSource_Object = MibScalar
cfgPclFontSource = _CfgPclFontSource_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 250),
    _CfgPclFontSource_Type()
)
cfgPclFontSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPclFontSource.setStatus("optional")


class _CfgPclFontNumber_Type(DisplayString):
    """Custom type cfgPclFontNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclFontNumber_Type.__name__ = "DisplayString"
_CfgPclFontNumber_Object = MibScalar
cfgPclFontNumber = _CfgPclFontNumber_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 260),
    _CfgPclFontNumber_Type()
)
cfgPclFontNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPclFontNumber.setStatus("optional")


class _CfgPclPitch_Type(DisplayString):
    """Custom type cfgPclPitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclPitch_Type.__name__ = "DisplayString"
_CfgPclPitch_Object = MibScalar
cfgPclPitch = _CfgPclPitch_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 270),
    _CfgPclPitch_Type()
)
cfgPclPitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPclPitch.setStatus("optional")


class _CfgPclPtSize_Type(DisplayString):
    """Custom type cfgPclPtSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclPtSize_Type.__name__ = "DisplayString"
_CfgPclPtSize_Object = MibScalar
cfgPclPtSize = _CfgPclPtSize_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 280),
    _CfgPclPtSize_Type()
)
cfgPclPtSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPclPtSize.setStatus("optional")


class _CfgPclSymSet_Type(DisplayString):
    """Custom type cfgPclSymSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclSymSet_Type.__name__ = "DisplayString"
_CfgPclSymSet_Object = MibScalar
cfgPclSymSet = _CfgPclSymSet_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 290),
    _CfgPclSymSet_Type()
)
cfgPclSymSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPclSymSet.setStatus("optional")


class _CfgPclOkiA4PrintWidth_Type(DisplayString):
    """Custom type cfgPclOkiA4PrintWidth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclOkiA4PrintWidth_Type.__name__ = "DisplayString"
_CfgPclOkiA4PrintWidth_Object = MibScalar
cfgPclOkiA4PrintWidth = _CfgPclOkiA4PrintWidth_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 300),
    _CfgPclOkiA4PrintWidth_Type()
)
cfgPclOkiA4PrintWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPclOkiA4PrintWidth.setStatus("optional")


class _CfgPclOkiWhitePageSkip_Type(DisplayString):
    """Custom type cfgPclOkiWhitePageSkip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclOkiWhitePageSkip_Type.__name__ = "DisplayString"
_CfgPclOkiWhitePageSkip_Object = MibScalar
cfgPclOkiWhitePageSkip = _CfgPclOkiWhitePageSkip_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 310),
    _CfgPclOkiWhitePageSkip_Type()
)
cfgPclOkiWhitePageSkip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPclOkiWhitePageSkip.setStatus("optional")


class _CfgPclOkiCrFunction_Type(DisplayString):
    """Custom type cfgPclOkiCrFunction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclOkiCrFunction_Type.__name__ = "DisplayString"
_CfgPclOkiCrFunction_Object = MibScalar
cfgPclOkiCrFunction = _CfgPclOkiCrFunction_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 320),
    _CfgPclOkiCrFunction_Type()
)
cfgPclOkiCrFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPclOkiCrFunction.setStatus("optional")


class _CfgPclOkiLfFunction_Type(DisplayString):
    """Custom type cfgPclOkiLfFunction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclOkiLfFunction_Type.__name__ = "DisplayString"
_CfgPclOkiLfFunction_Object = MibScalar
cfgPclOkiLfFunction = _CfgPclOkiLfFunction_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 330),
    _CfgPclOkiLfFunction_Type()
)
cfgPclOkiLfFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPclOkiLfFunction.setStatus("optional")


class _CfgIbmpprCharacterPitch_Type(DisplayString):
    """Custom type cfgIbmpprCharacterPitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprCharacterPitch_Type.__name__ = "DisplayString"
_CfgIbmpprCharacterPitch_Object = MibScalar
cfgIbmpprCharacterPitch = _CfgIbmpprCharacterPitch_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 340),
    _CfgIbmpprCharacterPitch_Type()
)
cfgIbmpprCharacterPitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprCharacterPitch.setStatus("optional")


class _CfgIbmpprFontCondense_Type(DisplayString):
    """Custom type cfgIbmpprFontCondense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprFontCondense_Type.__name__ = "DisplayString"
_CfgIbmpprFontCondense_Object = MibScalar
cfgIbmpprFontCondense = _CfgIbmpprFontCondense_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 350),
    _CfgIbmpprFontCondense_Type()
)
cfgIbmpprFontCondense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprFontCondense.setStatus("optional")


class _CfgIbmpprCharacterSet_Type(DisplayString):
    """Custom type cfgIbmpprCharacterSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprCharacterSet_Type.__name__ = "DisplayString"
_CfgIbmpprCharacterSet_Object = MibScalar
cfgIbmpprCharacterSet = _CfgIbmpprCharacterSet_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 360),
    _CfgIbmpprCharacterSet_Type()
)
cfgIbmpprCharacterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprCharacterSet.setStatus("optional")


class _CfgIbmpprSymbolSet_Type(DisplayString):
    """Custom type cfgIbmpprSymbolSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprSymbolSet_Type.__name__ = "DisplayString"
_CfgIbmpprSymbolSet_Object = MibScalar
cfgIbmpprSymbolSet = _CfgIbmpprSymbolSet_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 370),
    _CfgIbmpprSymbolSet_Type()
)
cfgIbmpprSymbolSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprSymbolSet.setStatus("optional")


class _CfgIbmpprLetterOStyle_Type(DisplayString):
    """Custom type cfgIbmpprLetterOStyle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprLetterOStyle_Type.__name__ = "DisplayString"
_CfgIbmpprLetterOStyle_Object = MibScalar
cfgIbmpprLetterOStyle = _CfgIbmpprLetterOStyle_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 380),
    _CfgIbmpprLetterOStyle_Type()
)
cfgIbmpprLetterOStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprLetterOStyle.setStatus("optional")


class _CfgIbmpprLinePitch_Type(DisplayString):
    """Custom type cfgIbmpprLinePitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprLinePitch_Type.__name__ = "DisplayString"
_CfgIbmpprLinePitch_Object = MibScalar
cfgIbmpprLinePitch = _CfgIbmpprLinePitch_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 390),
    _CfgIbmpprLinePitch_Type()
)
cfgIbmpprLinePitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprLinePitch.setStatus("optional")


class _CfgIbmpprWhitePageSkip_Type(DisplayString):
    """Custom type cfgIbmpprWhitePageSkip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprWhitePageSkip_Type.__name__ = "DisplayString"
_CfgIbmpprWhitePageSkip_Object = MibScalar
cfgIbmpprWhitePageSkip = _CfgIbmpprWhitePageSkip_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 400),
    _CfgIbmpprWhitePageSkip_Type()
)
cfgIbmpprWhitePageSkip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprWhitePageSkip.setStatus("optional")


class _CfgIbmpprCrFunction_Type(DisplayString):
    """Custom type cfgIbmpprCrFunction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprCrFunction_Type.__name__ = "DisplayString"
_CfgIbmpprCrFunction_Object = MibScalar
cfgIbmpprCrFunction = _CfgIbmpprCrFunction_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 410),
    _CfgIbmpprCrFunction_Type()
)
cfgIbmpprCrFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprCrFunction.setStatus("optional")


class _CfgIbmpprLfFunction_Type(DisplayString):
    """Custom type cfgIbmpprLfFunction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprLfFunction_Type.__name__ = "DisplayString"
_CfgIbmpprLfFunction_Object = MibScalar
cfgIbmpprLfFunction = _CfgIbmpprLfFunction_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 420),
    _CfgIbmpprLfFunction_Type()
)
cfgIbmpprLfFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprLfFunction.setStatus("optional")


class _CfgIbmpprLineLength_Type(DisplayString):
    """Custom type cfgIbmpprLineLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprLineLength_Type.__name__ = "DisplayString"
_CfgIbmpprLineLength_Object = MibScalar
cfgIbmpprLineLength = _CfgIbmpprLineLength_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 430),
    _CfgIbmpprLineLength_Type()
)
cfgIbmpprLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprLineLength.setStatus("optional")


class _CfgIbmpprFormLength_Type(DisplayString):
    """Custom type cfgIbmpprFormLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprFormLength_Type.__name__ = "DisplayString"
_CfgIbmpprFormLength_Object = MibScalar
cfgIbmpprFormLength = _CfgIbmpprFormLength_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 440),
    _CfgIbmpprFormLength_Type()
)
cfgIbmpprFormLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprFormLength.setStatus("optional")


class _CfgIbmpprTofPosition_Type(DisplayString):
    """Custom type cfgIbmpprTofPosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprTofPosition_Type.__name__ = "DisplayString"
_CfgIbmpprTofPosition_Object = MibScalar
cfgIbmpprTofPosition = _CfgIbmpprTofPosition_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 450),
    _CfgIbmpprTofPosition_Type()
)
cfgIbmpprTofPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprTofPosition.setStatus("optional")


class _CfgIbmpprLeftMargine_Type(DisplayString):
    """Custom type cfgIbmpprLeftMargine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgIbmpprLeftMargine_Type.__name__ = "DisplayString"
_CfgIbmpprLeftMargine_Object = MibScalar
cfgIbmpprLeftMargine = _CfgIbmpprLeftMargine_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 460),
    _CfgIbmpprLeftMargine_Type()
)
cfgIbmpprLeftMargine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIbmpprLeftMargine.setStatus("optional")


class _CfgEpsonfxCharacterPitch_Type(DisplayString):
    """Custom type cfgEpsonfxCharacterPitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxCharacterPitch_Type.__name__ = "DisplayString"
_CfgEpsonfxCharacterPitch_Object = MibScalar
cfgEpsonfxCharacterPitch = _CfgEpsonfxCharacterPitch_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 470),
    _CfgEpsonfxCharacterPitch_Type()
)
cfgEpsonfxCharacterPitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxCharacterPitch.setStatus("optional")


class _CfgEpsonfxCharacterSet_Type(DisplayString):
    """Custom type cfgEpsonfxCharacterSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxCharacterSet_Type.__name__ = "DisplayString"
_CfgEpsonfxCharacterSet_Object = MibScalar
cfgEpsonfxCharacterSet = _CfgEpsonfxCharacterSet_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 480),
    _CfgEpsonfxCharacterSet_Type()
)
cfgEpsonfxCharacterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxCharacterSet.setStatus("optional")


class _CfgEpsonfxSymbolSet_Type(DisplayString):
    """Custom type cfgEpsonfxSymbolSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxSymbolSet_Type.__name__ = "DisplayString"
_CfgEpsonfxSymbolSet_Object = MibScalar
cfgEpsonfxSymbolSet = _CfgEpsonfxSymbolSet_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 490),
    _CfgEpsonfxSymbolSet_Type()
)
cfgEpsonfxSymbolSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxSymbolSet.setStatus("optional")


class _CfgEpsonfxLetterOStyle_Type(DisplayString):
    """Custom type cfgEpsonfxLetterOStyle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxLetterOStyle_Type.__name__ = "DisplayString"
_CfgEpsonfxLetterOStyle_Object = MibScalar
cfgEpsonfxLetterOStyle = _CfgEpsonfxLetterOStyle_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 500),
    _CfgEpsonfxLetterOStyle_Type()
)
cfgEpsonfxLetterOStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxLetterOStyle.setStatus("optional")


class _CfgEpsonfxLinePitch_Type(DisplayString):
    """Custom type cfgEpsonfxLinePitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxLinePitch_Type.__name__ = "DisplayString"
_CfgEpsonfxLinePitch_Object = MibScalar
cfgEpsonfxLinePitch = _CfgEpsonfxLinePitch_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 510),
    _CfgEpsonfxLinePitch_Type()
)
cfgEpsonfxLinePitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxLinePitch.setStatus("optional")


class _CfgEpsonfxWhitePageSkip_Type(DisplayString):
    """Custom type cfgEpsonfxWhitePageSkip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxWhitePageSkip_Type.__name__ = "DisplayString"
_CfgEpsonfxWhitePageSkip_Object = MibScalar
cfgEpsonfxWhitePageSkip = _CfgEpsonfxWhitePageSkip_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 520),
    _CfgEpsonfxWhitePageSkip_Type()
)
cfgEpsonfxWhitePageSkip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxWhitePageSkip.setStatus("optional")


class _CfgEpsonfxCrFunction_Type(DisplayString):
    """Custom type cfgEpsonfxCrFunction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxCrFunction_Type.__name__ = "DisplayString"
_CfgEpsonfxCrFunction_Object = MibScalar
cfgEpsonfxCrFunction = _CfgEpsonfxCrFunction_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 530),
    _CfgEpsonfxCrFunction_Type()
)
cfgEpsonfxCrFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxCrFunction.setStatus("optional")


class _CfgEpsonfxLineLength_Type(DisplayString):
    """Custom type cfgEpsonfxLineLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxLineLength_Type.__name__ = "DisplayString"
_CfgEpsonfxLineLength_Object = MibScalar
cfgEpsonfxLineLength = _CfgEpsonfxLineLength_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 540),
    _CfgEpsonfxLineLength_Type()
)
cfgEpsonfxLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxLineLength.setStatus("optional")


class _CfgEpsonfxFormLength_Type(DisplayString):
    """Custom type cfgEpsonfxFormLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxFormLength_Type.__name__ = "DisplayString"
_CfgEpsonfxFormLength_Object = MibScalar
cfgEpsonfxFormLength = _CfgEpsonfxFormLength_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 550),
    _CfgEpsonfxFormLength_Type()
)
cfgEpsonfxFormLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxFormLength.setStatus("optional")


class _CfgEpsonfxTofPosition_Type(DisplayString):
    """Custom type cfgEpsonfxTofPosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxTofPosition_Type.__name__ = "DisplayString"
_CfgEpsonfxTofPosition_Object = MibScalar
cfgEpsonfxTofPosition = _CfgEpsonfxTofPosition_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 560),
    _CfgEpsonfxTofPosition_Type()
)
cfgEpsonfxTofPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxTofPosition.setStatus("optional")


class _CfgEpsonfxLeftMargine_Type(DisplayString):
    """Custom type cfgEpsonfxLeftMargine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEpsonfxLeftMargine_Type.__name__ = "DisplayString"
_CfgEpsonfxLeftMargine_Object = MibScalar
cfgEpsonfxLeftMargine = _CfgEpsonfxLeftMargine_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 570),
    _CfgEpsonfxLeftMargine_Type()
)
cfgEpsonfxLeftMargine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEpsonfxLeftMargine.setStatus("optional")


class _CfgHiperwOkiDensity_Type(DisplayString):
    """Custom type cfgHiperwOkiDensity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgHiperwOkiDensity_Type.__name__ = "DisplayString"
_CfgHiperwOkiDensity_Object = MibScalar
cfgHiperwOkiDensity = _CfgHiperwOkiDensity_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 580),
    _CfgHiperwOkiDensity_Type()
)
cfgHiperwOkiDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHiperwOkiDensity.setStatus("optional")


class _CfgHiperwOkiFirstbit_Type(DisplayString):
    """Custom type cfgHiperwOkiFirstbit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgHiperwOkiFirstbit_Type.__name__ = "DisplayString"
_CfgHiperwOkiFirstbit_Object = MibScalar
cfgHiperwOkiFirstbit = _CfgHiperwOkiFirstbit_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 590),
    _CfgHiperwOkiFirstbit_Type()
)
cfgHiperwOkiFirstbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHiperwOkiFirstbit.setStatus("optional")


class _CfgHiperwOkiReverse_Type(DisplayString):
    """Custom type cfgHiperwOkiReverse based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgHiperwOkiReverse_Type.__name__ = "DisplayString"
_CfgHiperwOkiReverse_Object = MibScalar
cfgHiperwOkiReverse = _CfgHiperwOkiReverse_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 600),
    _CfgHiperwOkiReverse_Type()
)
cfgHiperwOkiReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHiperwOkiReverse.setStatus("optional")


class _CfgHiperwPrintSpeed_Type(DisplayString):
    """Custom type cfgHiperwPrintSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgHiperwPrintSpeed_Type.__name__ = "DisplayString"
_CfgHiperwPrintSpeed_Object = MibScalar
cfgHiperwPrintSpeed = _CfgHiperwPrintSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 610),
    _CfgHiperwPrintSpeed_Type()
)
cfgHiperwPrintSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHiperwPrintSpeed.setStatus("optional")


class _CfgEscpKanjiFont_Type(DisplayString):
    """Custom type cfgEscpKanjiFont based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEscpKanjiFont_Type.__name__ = "DisplayString"
_CfgEscpKanjiFont_Object = MibScalar
cfgEscpKanjiFont = _CfgEscpKanjiFont_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 611),
    _CfgEscpKanjiFont_Type()
)
cfgEscpKanjiFont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEscpKanjiFont.setStatus("optional")


class _CfgEscpAnkFont_Type(DisplayString):
    """Custom type cfgEscpAnkFont based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEscpAnkFont_Type.__name__ = "DisplayString"
_CfgEscpAnkFont_Object = MibScalar
cfgEscpAnkFont = _CfgEscpAnkFont_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 612),
    _CfgEscpAnkFont_Type()
)
cfgEscpAnkFont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEscpAnkFont.setStatus("optional")


class _CfgEscpCharacterSet_Type(DisplayString):
    """Custom type cfgEscpCharacterSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEscpCharacterSet_Type.__name__ = "DisplayString"
_CfgEscpCharacterSet_Object = MibScalar
cfgEscpCharacterSet = _CfgEscpCharacterSet_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 613),
    _CfgEscpCharacterSet_Type()
)
cfgEscpCharacterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEscpCharacterSet.setStatus("optional")


class _CfgEscpZeroCharacter_Type(DisplayString):
    """Custom type cfgEscpZeroCharacter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEscpZeroCharacter_Type.__name__ = "DisplayString"
_CfgEscpZeroCharacter_Object = MibScalar
cfgEscpZeroCharacter = _CfgEscpZeroCharacter_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 614),
    _CfgEscpZeroCharacter_Type()
)
cfgEscpZeroCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEscpZeroCharacter.setStatus("optional")


class _CfgEscpZoom_Type(DisplayString):
    """Custom type cfgEscpZoom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEscpZoom_Type.__name__ = "DisplayString"
_CfgEscpZoom_Object = MibScalar
cfgEscpZoom = _CfgEscpZoom_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 615),
    _CfgEscpZoom_Type()
)
cfgEscpZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEscpZoom.setStatus("optional")


class _CfgEscpTofPosition_Type(DisplayString):
    """Custom type cfgEscpTofPosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEscpTofPosition_Type.__name__ = "DisplayString"
_CfgEscpTofPosition_Object = MibScalar
cfgEscpTofPosition = _CfgEscpTofPosition_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 616),
    _CfgEscpTofPosition_Type()
)
cfgEscpTofPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEscpTofPosition.setStatus("optional")


class _CfgEscpLineLength_Type(DisplayString):
    """Custom type cfgEscpLineLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEscpLineLength_Type.__name__ = "DisplayString"
_CfgEscpLineLength_Object = MibScalar
cfgEscpLineLength = _CfgEscpLineLength_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 617),
    _CfgEscpLineLength_Type()
)
cfgEscpLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEscpLineLength.setStatus("optional")


class _CfgEscpCrFunction_Type(DisplayString):
    """Custom type cfgEscpCrFunction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEscpCrFunction_Type.__name__ = "DisplayString"
_CfgEscpCrFunction_Object = MibScalar
cfgEscpCrFunction = _CfgEscpCrFunction_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 618),
    _CfgEscpCrFunction_Type()
)
cfgEscpCrFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEscpCrFunction.setStatus("optional")


class _CfgEscpAutoLf_Type(DisplayString):
    """Custom type cfgEscpAutoLf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEscpAutoLf_Type.__name__ = "DisplayString"
_CfgEscpAutoLf_Object = MibScalar
cfgEscpAutoLf = _CfgEscpAutoLf_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 619),
    _CfgEscpAutoLf_Type()
)
cfgEscpAutoLf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEscpAutoLf.setStatus("optional")


class _CfgOrientation_Type(DisplayString):
    """Custom type cfgOrientation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOrientation_Type.__name__ = "DisplayString"
_CfgOrientation_Object = MibScalar
cfgOrientation = _CfgOrientation_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 620),
    _CfgOrientation_Type()
)
cfgOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOrientation.setStatus("optional")


class _CfgFormLines_Type(DisplayString):
    """Custom type cfgFormLines based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgFormLines_Type.__name__ = "DisplayString"
_CfgFormLines_Object = MibScalar
cfgFormLines = _CfgFormLines_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 630),
    _CfgFormLines_Type()
)
cfgFormLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFormLines.setStatus("optional")


class _CfgParallel_Type(DisplayString):
    """Custom type cfgParallel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgParallel_Type.__name__ = "DisplayString"
_CfgParallel_Object = MibScalar
cfgParallel = _CfgParallel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 640),
    _CfgParallel_Type()
)
cfgParallel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgParallel.setStatus("optional")


class _CfgRs232c_Type(DisplayString):
    """Custom type cfgRs232c based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs232c_Type.__name__ = "DisplayString"
_CfgRs232c_Object = MibScalar
cfgRs232c = _CfgRs232c_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 650),
    _CfgRs232c_Type()
)
cfgRs232c.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs232c.setStatus("optional")


class _CfgRs422_Type(DisplayString):
    """Custom type cfgRs422 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs422_Type.__name__ = "DisplayString"
_CfgRs422_Object = MibScalar
cfgRs422 = _CfgRs422_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 660),
    _CfgRs422_Type()
)
cfgRs422.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs422.setStatus("optional")


class _CfgLocalTalk_Type(DisplayString):
    """Custom type cfgLocalTalk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgLocalTalk_Type.__name__ = "DisplayString"
_CfgLocalTalk_Object = MibScalar
cfgLocalTalk = _CfgLocalTalk_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 670),
    _CfgLocalTalk_Type()
)
cfgLocalTalk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgLocalTalk.setStatus("optional")


class _CfgNetwork_Type(DisplayString):
    """Custom type cfgNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgNetwork_Type.__name__ = "DisplayString"
_CfgNetwork_Object = MibScalar
cfgNetwork = _CfgNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 680),
    _CfgNetwork_Type()
)
cfgNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgNetwork.setStatus("optional")


class _CfgUsb_Type(DisplayString):
    """Custom type cfgUsb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgUsb_Type.__name__ = "DisplayString"
_CfgUsb_Object = MibScalar
cfgUsb = _CfgUsb_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 690),
    _CfgUsb_Type()
)
cfgUsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgUsb.setStatus("optional")


class _CfgResolution_Type(DisplayString):
    """Custom type cfgResolution based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgResolution_Type.__name__ = "DisplayString"
_CfgResolution_Object = MibScalar
cfgResolution = _CfgResolution_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2000),
    _CfgResolution_Type()
)
cfgResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgResolution.setStatus("optional")


class _CfgRet_Type(DisplayString):
    """Custom type cfgRet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRet_Type.__name__ = "DisplayString"
_CfgRet_Object = MibScalar
cfgRet = _CfgRet_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2010),
    _CfgRet_Type()
)
cfgRet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRet.setStatus("optional")


class _CfgOkiRasterBuffer_Type(DisplayString):
    """Custom type cfgOkiRasterBuffer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiRasterBuffer_Type.__name__ = "DisplayString"
_CfgOkiRasterBuffer_Object = MibScalar
cfgOkiRasterBuffer = _CfgOkiRasterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2020),
    _CfgOkiRasterBuffer_Type()
)
cfgOkiRasterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiRasterBuffer.setStatus("optional")


class _CfgPageProtect_Type(DisplayString):
    """Custom type cfgPageProtect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPageProtect_Type.__name__ = "DisplayString"
_CfgPageProtect_Object = MibScalar
cfgPageProtect = _CfgPageProtect_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2030),
    _CfgPageProtect_Type()
)
cfgPageProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgPageProtect.setStatus("optional")


class _CfgPrintProtect_Type(DisplayString):
    """Custom type cfgPrintProtect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPrintProtect_Type.__name__ = "DisplayString"
_CfgPrintProtect_Object = MibScalar
cfgPrintProtect = _CfgPrintProtect_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2035),
    _CfgPrintProtect_Type()
)
cfgPrintProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPrintProtect.setStatus("optional")


class _CfgOkiReceiveBuffer_Type(DisplayString):
    """Custom type cfgOkiReceiveBuffer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiReceiveBuffer_Type.__name__ = "DisplayString"
_CfgOkiReceiveBuffer_Object = MibScalar
cfgOkiReceiveBuffer = _CfgOkiReceiveBuffer_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2040),
    _CfgOkiReceiveBuffer_Type()
)
cfgOkiReceiveBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgOkiReceiveBuffer.setStatus("optional")


class _CfgOkiFontProtection_Type(DisplayString):
    """Custom type cfgOkiFontProtection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiFontProtection_Type.__name__ = "DisplayString"
_CfgOkiFontProtection_Object = MibScalar
cfgOkiFontProtection = _CfgOkiFontProtection_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2050),
    _CfgOkiFontProtection_Type()
)
cfgOkiFontProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgOkiFontProtection.setStatus("optional")


class _CfgOkiResourceSave_Type(DisplayString):
    """Custom type cfgOkiResourceSave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiResourceSave_Type.__name__ = "DisplayString"
_CfgOkiResourceSave_Object = MibScalar
cfgOkiResourceSave = _CfgOkiResourceSave_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2060),
    _CfgOkiResourceSave_Type()
)
cfgOkiResourceSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgOkiResourceSave.setStatus("optional")


class _CfgAutoCont_Type(DisplayString):
    """Custom type cfgAutoCont based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgAutoCont_Type.__name__ = "DisplayString"
_CfgAutoCont_Object = MibScalar
cfgAutoCont = _CfgAutoCont_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2070),
    _CfgAutoCont_Type()
)
cfgAutoCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAutoCont.setStatus("optional")


class _CfgOkiAutoEject_Type(DisplayString):
    """Custom type cfgOkiAutoEject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiAutoEject_Type.__name__ = "DisplayString"
_CfgOkiAutoEject_Object = MibScalar
cfgOkiAutoEject = _CfgOkiAutoEject_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2080),
    _CfgOkiAutoEject_Type()
)
cfgOkiAutoEject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiAutoEject.setStatus("optional")


class _CfgManualTimeOut_Type(DisplayString):
    """Custom type cfgManualTimeOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgManualTimeOut_Type.__name__ = "DisplayString"
_CfgManualTimeOut_Object = MibScalar
cfgManualTimeOut = _CfgManualTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2090),
    _CfgManualTimeOut_Type()
)
cfgManualTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgManualTimeOut.setStatus("optional")


class _CfgDensity_Type(DisplayString):
    """Custom type cfgDensity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgDensity_Type.__name__ = "DisplayString"
_CfgDensity_Object = MibScalar
cfgDensity = _CfgDensity_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2100),
    _CfgDensity_Type()
)
cfgDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDensity.setStatus("optional")


class _CfgOkiYellowDarkness_Type(DisplayString):
    """Custom type cfgOkiYellowDarkness based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiYellowDarkness_Type.__name__ = "DisplayString"
_CfgOkiYellowDarkness_Object = MibScalar
cfgOkiYellowDarkness = _CfgOkiYellowDarkness_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2101),
    _CfgOkiYellowDarkness_Type()
)
cfgOkiYellowDarkness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiYellowDarkness.setStatus("optional")


class _CfgOkiMagentaDarkness_Type(DisplayString):
    """Custom type cfgOkiMagentaDarkness based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiMagentaDarkness_Type.__name__ = "DisplayString"
_CfgOkiMagentaDarkness_Object = MibScalar
cfgOkiMagentaDarkness = _CfgOkiMagentaDarkness_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2102),
    _CfgOkiMagentaDarkness_Type()
)
cfgOkiMagentaDarkness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiMagentaDarkness.setStatus("optional")


class _CfgOkiCyanDarkness_Type(DisplayString):
    """Custom type cfgOkiCyanDarkness based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiCyanDarkness_Type.__name__ = "DisplayString"
_CfgOkiCyanDarkness_Object = MibScalar
cfgOkiCyanDarkness = _CfgOkiCyanDarkness_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2103),
    _CfgOkiCyanDarkness_Type()
)
cfgOkiCyanDarkness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiCyanDarkness.setStatus("optional")


class _CfgOkiBlackDarkness_Type(DisplayString):
    """Custom type cfgOkiBlackDarkness based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiBlackDarkness_Type.__name__ = "DisplayString"
_CfgOkiBlackDarkness_Object = MibScalar
cfgOkiBlackDarkness = _CfgOkiBlackDarkness_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2104),
    _CfgOkiBlackDarkness_Type()
)
cfgOkiBlackDarkness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiBlackDarkness.setStatus("optional")


class _CfgOkiPowerSaving_Type(DisplayString):
    """Custom type cfgOkiPowerSaving based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiPowerSaving_Type.__name__ = "DisplayString"
_CfgOkiPowerSaving_Object = MibScalar
cfgOkiPowerSaving = _CfgOkiPowerSaving_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2110),
    _CfgOkiPowerSaving_Type()
)
cfgOkiPowerSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiPowerSaving.setStatus("optional")


class _CfgOkiQuietMode_Type(DisplayString):
    """Custom type cfgOkiQuietMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiQuietMode_Type.__name__ = "DisplayString"
_CfgOkiQuietMode_Object = MibScalar
cfgOkiQuietMode = _CfgOkiQuietMode_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2115),
    _CfgOkiQuietMode_Type()
)
cfgOkiQuietMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiQuietMode.setStatus("optional")


class _CfgLowToner_Type(DisplayString):
    """Custom type cfgLowToner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgLowToner_Type.__name__ = "DisplayString"
_CfgLowToner_Object = MibScalar
cfgLowToner = _CfgLowToner_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2120),
    _CfgLowToner_Type()
)
cfgLowToner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgLowToner.setStatus("optional")


class _CfgEconoMode_Type(DisplayString):
    """Custom type cfgEconoMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEconoMode_Type.__name__ = "DisplayString"
_CfgEconoMode_Object = MibScalar
cfgEconoMode = _CfgEconoMode_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2130),
    _CfgEconoMode_Type()
)
cfgEconoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEconoMode.setStatus("optional")


class _CfgClearableWarnings_Type(DisplayString):
    """Custom type cfgClearableWarnings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgClearableWarnings_Type.__name__ = "DisplayString"
_CfgClearableWarnings_Object = MibScalar
cfgClearableWarnings = _CfgClearableWarnings_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2140),
    _CfgClearableWarnings_Type()
)
cfgClearableWarnings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgClearableWarnings.setStatus("optional")


class _CfgOkiPrintErrors_Type(DisplayString):
    """Custom type cfgOkiPrintErrors based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiPrintErrors_Type.__name__ = "DisplayString"
_CfgOkiPrintErrors_Object = MibScalar
cfgOkiPrintErrors = _CfgOkiPrintErrors_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2150),
    _CfgOkiPrintErrors_Type()
)
cfgOkiPrintErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiPrintErrors.setStatus("optional")


class _CfgParallelSpeed_Type(DisplayString):
    """Custom type cfgParallelSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgParallelSpeed_Type.__name__ = "DisplayString"
_CfgParallelSpeed_Object = MibScalar
cfgParallelSpeed = _CfgParallelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2160),
    _CfgParallelSpeed_Type()
)
cfgParallelSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgParallelSpeed.setStatus("optional")


class _CfgBiDirection_Type(DisplayString):
    """Custom type cfgBiDirection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgBiDirection_Type.__name__ = "DisplayString"
_CfgBiDirection_Object = MibScalar
cfgBiDirection = _CfgBiDirection_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2170),
    _CfgBiDirection_Type()
)
cfgBiDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgBiDirection.setStatus("optional")


class _CfgOkiIPrime_Type(DisplayString):
    """Custom type cfgOkiIPrime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiIPrime_Type.__name__ = "DisplayString"
_CfgOkiIPrime_Object = MibScalar
cfgOkiIPrime = _CfgOkiIPrime_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2180),
    _CfgOkiIPrime_Type()
)
cfgOkiIPrime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiIPrime.setStatus("optional")


class _CfgLang_Type(DisplayString):
    """Custom type cfgLang based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgLang_Type.__name__ = "DisplayString"
_CfgLang_Object = MibScalar
cfgLang = _CfgLang_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2190),
    _CfgLang_Type()
)
cfgLang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgLang.setStatus("optional")


class _CfgOkiJobSwitch_Type(DisplayString):
    """Custom type cfgOkiJobSwitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiJobSwitch_Type.__name__ = "DisplayString"
_CfgOkiJobSwitch_Object = MibScalar
cfgOkiJobSwitch = _CfgOkiJobSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2195),
    _CfgOkiJobSwitch_Type()
)
cfgOkiJobSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiJobSwitch.setStatus("optional")


class _CfgRs232cBaud_Type(DisplayString):
    """Custom type cfgRs232cBaud based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs232cBaud_Type.__name__ = "DisplayString"
_CfgRs232cBaud_Object = MibScalar
cfgRs232cBaud = _CfgRs232cBaud_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2200),
    _CfgRs232cBaud_Type()
)
cfgRs232cBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs232cBaud.setStatus("optional")


class _CfgRs232cDataBits_Type(DisplayString):
    """Custom type cfgRs232cDataBits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs232cDataBits_Type.__name__ = "DisplayString"
_CfgRs232cDataBits_Object = MibScalar
cfgRs232cDataBits = _CfgRs232cDataBits_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2210),
    _CfgRs232cDataBits_Type()
)
cfgRs232cDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs232cDataBits.setStatus("optional")


class _CfgRs232cStopBits_Type(DisplayString):
    """Custom type cfgRs232cStopBits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs232cStopBits_Type.__name__ = "DisplayString"
_CfgRs232cStopBits_Object = MibScalar
cfgRs232cStopBits = _CfgRs232cStopBits_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2215),
    _CfgRs232cStopBits_Type()
)
cfgRs232cStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs232cStopBits.setStatus("optional")


class _CfgRs232cParity_Type(DisplayString):
    """Custom type cfgRs232cParity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs232cParity_Type.__name__ = "DisplayString"
_CfgRs232cParity_Object = MibScalar
cfgRs232cParity = _CfgRs232cParity_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2220),
    _CfgRs232cParity_Type()
)
cfgRs232cParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs232cParity.setStatus("optional")


class _CfgRs232cBusyTime_Type(DisplayString):
    """Custom type cfgRs232cBusyTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs232cBusyTime_Type.__name__ = "DisplayString"
_CfgRs232cBusyTime_Object = MibScalar
cfgRs232cBusyTime = _CfgRs232cBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2230),
    _CfgRs232cBusyTime_Type()
)
cfgRs232cBusyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs232cBusyTime.setStatus("optional")


class _CfgRs232cFlowControl_Type(DisplayString):
    """Custom type cfgRs232cFlowControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs232cFlowControl_Type.__name__ = "DisplayString"
_CfgRs232cFlowControl_Object = MibScalar
cfgRs232cFlowControl = _CfgRs232cFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2240),
    _CfgRs232cFlowControl_Type()
)
cfgRs232cFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs232cFlowControl.setStatus("optional")


class _CfgRs422Baud_Type(DisplayString):
    """Custom type cfgRs422Baud based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs422Baud_Type.__name__ = "DisplayString"
_CfgRs422Baud_Object = MibScalar
cfgRs422Baud = _CfgRs422Baud_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2300),
    _CfgRs422Baud_Type()
)
cfgRs422Baud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs422Baud.setStatus("optional")


class _CfgRs422DataBits_Type(DisplayString):
    """Custom type cfgRs422DataBits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs422DataBits_Type.__name__ = "DisplayString"
_CfgRs422DataBits_Object = MibScalar
cfgRs422DataBits = _CfgRs422DataBits_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2310),
    _CfgRs422DataBits_Type()
)
cfgRs422DataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs422DataBits.setStatus("optional")


class _CfgRs422StopBits_Type(DisplayString):
    """Custom type cfgRs422StopBits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs422StopBits_Type.__name__ = "DisplayString"
_CfgRs422StopBits_Object = MibScalar
cfgRs422StopBits = _CfgRs422StopBits_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2320),
    _CfgRs422StopBits_Type()
)
cfgRs422StopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs422StopBits.setStatus("optional")


class _CfgRs422Parity_Type(DisplayString):
    """Custom type cfgRs422Parity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRs422Parity_Type.__name__ = "DisplayString"
_CfgRs422Parity_Object = MibScalar
cfgRs422Parity = _CfgRs422Parity_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 2330),
    _CfgRs422Parity_Type()
)
cfgRs422Parity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRs422Parity.setStatus("optional")


class _CfgOkiUser_Type(DisplayString):
    """Custom type cfgOkiUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiUser_Type.__name__ = "DisplayString"
_CfgOkiUser_Object = MibScalar
cfgOkiUser = _CfgOkiUser_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3000),
    _CfgOkiUser_Type()
)
cfgOkiUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiUser.setStatus("optional")


class _CfgOkiEcp_Type(DisplayString):
    """Custom type cfgOkiEcp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiEcp_Type.__name__ = "DisplayString"
_CfgOkiEcp_Object = MibScalar
cfgOkiEcp = _CfgOkiEcp_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3005),
    _CfgOkiEcp_Type()
)
cfgOkiEcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiEcp.setStatus("optional")


class _CfgOkiXAdjust_Type(DisplayString):
    """Custom type cfgOkiXAdjust based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiXAdjust_Type.__name__ = "DisplayString"
_CfgOkiXAdjust_Object = MibScalar
cfgOkiXAdjust = _CfgOkiXAdjust_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3010),
    _CfgOkiXAdjust_Type()
)
cfgOkiXAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiXAdjust.setStatus("optional")


class _CfgOkiYAdjust_Type(DisplayString):
    """Custom type cfgOkiYAdjust based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiYAdjust_Type.__name__ = "DisplayString"
_CfgOkiYAdjust_Object = MibScalar
cfgOkiYAdjust = _CfgOkiYAdjust_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3020),
    _CfgOkiYAdjust_Type()
)
cfgOkiYAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiYAdjust.setStatus("optional")


class _CfgOkiDuplexAdjust_Type(DisplayString):
    """Custom type cfgOkiDuplexAdjust based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiDuplexAdjust_Type.__name__ = "DisplayString"
_CfgOkiDuplexAdjust_Object = MibScalar
cfgOkiDuplexAdjust = _CfgOkiDuplexAdjust_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3022),
    _CfgOkiDuplexAdjust_Type()
)
cfgOkiDuplexAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiDuplexAdjust.setStatus("optional")


class _CfgOkiMediaSourceTray2_Type(DisplayString):
    """Custom type cfgOkiMediaSourceTray2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiMediaSourceTray2_Type.__name__ = "DisplayString"
_CfgOkiMediaSourceTray2_Object = MibScalar
cfgOkiMediaSourceTray2 = _CfgOkiMediaSourceTray2_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3024),
    _CfgOkiMediaSourceTray2_Type()
)
cfgOkiMediaSourceTray2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiMediaSourceTray2.setStatus("optional")


class _CfgOkiMediaSourceTray3_Type(DisplayString):
    """Custom type cfgOkiMediaSourceTray3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiMediaSourceTray3_Type.__name__ = "DisplayString"
_CfgOkiMediaSourceTray3_Object = MibScalar
cfgOkiMediaSourceTray3 = _CfgOkiMediaSourceTray3_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3025),
    _CfgOkiMediaSourceTray3_Type()
)
cfgOkiMediaSourceTray3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiMediaSourceTray3.setStatus("optional")


class _CfgOkiMediaSourceFront_Type(DisplayString):
    """Custom type cfgOkiMediaSourceFront based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiMediaSourceFront_Type.__name__ = "DisplayString"
_CfgOkiMediaSourceFront_Object = MibScalar
cfgOkiMediaSourceFront = _CfgOkiMediaSourceFront_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3026),
    _CfgOkiMediaSourceFront_Type()
)
cfgOkiMediaSourceFront.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiMediaSourceFront.setStatus("optional")


class _CfgPlacePage_Type(DisplayString):
    """Custom type cfgPlacePage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPlacePage_Type.__name__ = "DisplayString"
_CfgPlacePage_Object = MibScalar
cfgPlacePage = _CfgPlacePage_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3028),
    _CfgPlacePage_Type()
)
cfgPlacePage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPlacePage.setStatus("optional")


class _CfgOkiColorAdjustPrint_Type(DisplayString):
    """Custom type cfgOkiColorAdjustPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiColorAdjustPrint_Type.__name__ = "DisplayString"
_CfgOkiColorAdjustPrint_Object = MibScalar
cfgOkiColorAdjustPrint = _CfgOkiColorAdjustPrint_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3041),
    _CfgOkiColorAdjustPrint_Type()
)
cfgOkiColorAdjustPrint.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cfgOkiColorAdjustPrint.setStatus("optional")


class _CfgOkiColorAdjustYellow_Type(DisplayString):
    """Custom type cfgOkiColorAdjustYellow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiColorAdjustYellow_Type.__name__ = "DisplayString"
_CfgOkiColorAdjustYellow_Object = MibScalar
cfgOkiColorAdjustYellow = _CfgOkiColorAdjustYellow_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3042),
    _CfgOkiColorAdjustYellow_Type()
)
cfgOkiColorAdjustYellow.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cfgOkiColorAdjustYellow.setStatus("optional")


class _CfgOkiColorAdjustMagenta_Type(DisplayString):
    """Custom type cfgOkiColorAdjustMagenta based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiColorAdjustMagenta_Type.__name__ = "DisplayString"
_CfgOkiColorAdjustMagenta_Object = MibScalar
cfgOkiColorAdjustMagenta = _CfgOkiColorAdjustMagenta_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3043),
    _CfgOkiColorAdjustMagenta_Type()
)
cfgOkiColorAdjustMagenta.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cfgOkiColorAdjustMagenta.setStatus("optional")


class _CfgOkiColorAdjustCyan_Type(DisplayString):
    """Custom type cfgOkiColorAdjustCyan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiColorAdjustCyan_Type.__name__ = "DisplayString"
_CfgOkiColorAdjustCyan_Object = MibScalar
cfgOkiColorAdjustCyan = _CfgOkiColorAdjustCyan_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3044),
    _CfgOkiColorAdjustCyan_Type()
)
cfgOkiColorAdjustCyan.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cfgOkiColorAdjustCyan.setStatus("optional")


class _CfgOkiJamRecovery_Type(DisplayString):
    """Custom type cfgOkiJamRecovery based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgOkiJamRecovery_Type.__name__ = "DisplayString"
_CfgOkiJamRecovery_Object = MibScalar
cfgOkiJamRecovery = _CfgOkiJamRecovery_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3142),
    _CfgOkiJamRecovery_Type()
)
cfgOkiJamRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgOkiJamRecovery.setStatus("optional")


class _CfgFirmCpuVersion_Type(DisplayString):
    """Custom type cfgFirmCpuVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgFirmCpuVersion_Type.__name__ = "DisplayString"
_CfgFirmCpuVersion_Object = MibScalar
cfgFirmCpuVersion = _CfgFirmCpuVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3160),
    _CfgFirmCpuVersion_Type()
)
cfgFirmCpuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgFirmCpuVersion.setStatus("optional")


class _CfgEngineFirmVersion_Type(DisplayString):
    """Custom type cfgEngineFirmVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEngineFirmVersion_Type.__name__ = "DisplayString"
_CfgEngineFirmVersion_Object = MibScalar
cfgEngineFirmVersion = _CfgEngineFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3170),
    _CfgEngineFirmVersion_Type()
)
cfgEngineFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEngineFirmVersion.setStatus("optional")


class _CfgMessageVersion_Type(DisplayString):
    """Custom type cfgMessageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgMessageVersion_Type.__name__ = "DisplayString"
_CfgMessageVersion_Object = MibScalar
cfgMessageVersion = _CfgMessageVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3180),
    _CfgMessageVersion_Type()
)
cfgMessageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgMessageVersion.setStatus("optional")


class _CfgPclFirmVersion_Type(DisplayString):
    """Custom type cfgPclFirmVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclFirmVersion_Type.__name__ = "DisplayString"
_CfgPclFirmVersion_Object = MibScalar
cfgPclFirmVersion = _CfgPclFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3190),
    _CfgPclFirmVersion_Type()
)
cfgPclFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgPclFirmVersion.setStatus("optional")


class _CfgPclxlFirmVersion_Type(DisplayString):
    """Custom type cfgPclxlFirmVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPclxlFirmVersion_Type.__name__ = "DisplayString"
_CfgPclxlFirmVersion_Object = MibScalar
cfgPclxlFirmVersion = _CfgPclxlFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3200),
    _CfgPclxlFirmVersion_Type()
)
cfgPclxlFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgPclxlFirmVersion.setStatus("optional")


class _CfgSidmFirmVersion_Type(DisplayString):
    """Custom type cfgSidmFirmVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgSidmFirmVersion_Type.__name__ = "DisplayString"
_CfgSidmFirmVersion_Object = MibScalar
cfgSidmFirmVersion = _CfgSidmFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3210),
    _CfgSidmFirmVersion_Type()
)
cfgSidmFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgSidmFirmVersion.setStatus("optional")


class _CfgHdFirmVersion_Type(DisplayString):
    """Custom type cfgHdFirmVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgHdFirmVersion_Type.__name__ = "DisplayString"
_CfgHdFirmVersion_Object = MibScalar
cfgHdFirmVersion = _CfgHdFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3220),
    _CfgHdFirmVersion_Type()
)
cfgHdFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgHdFirmVersion.setStatus("optional")


class _CfgPsFirmVersion_Type(DisplayString):
    """Custom type cfgPsFirmVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPsFirmVersion_Type.__name__ = "DisplayString"
_CfgPsFirmVersion_Object = MibScalar
cfgPsFirmVersion = _CfgPsFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3230),
    _CfgPsFirmVersion_Type()
)
cfgPsFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgPsFirmVersion.setStatus("optional")
_CfgEmulationTable_Object = MibTable
cfgEmulationTable = _CfgEmulationTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3500)
)
if mibBuilder.loadTexts:
    cfgEmulationTable.setStatus("optional")
_CfgEmulationEntry_Object = MibTableRow
cfgEmulationEntry = _CfgEmulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3500, 1)
)
cfgEmulationEntry.setIndexNames(
    (0, "OKIDATA-MIB", "cfgEmulationIndex"),
)
if mibBuilder.loadTexts:
    cfgEmulationEntry.setStatus("optional")


class _CfgEmulationIndex_Type(Integer32):
    """Custom type cfgEmulationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CfgEmulationIndex_Type.__name__ = "Integer32"
_CfgEmulationIndex_Object = MibTableColumn
cfgEmulationIndex = _CfgEmulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3500, 1, 1),
    _CfgEmulationIndex_Type()
)
cfgEmulationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEmulationIndex.setStatus("optional")


class _CfgEmulationName_Type(DisplayString):
    """Custom type cfgEmulationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgEmulationName_Type.__name__ = "DisplayString"
_CfgEmulationName_Object = MibTableColumn
cfgEmulationName = _CfgEmulationName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3500, 1, 2),
    _CfgEmulationName_Type()
)
cfgEmulationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEmulationName.setStatus("optional")


class _CfgRamInstalledSize_Type(DisplayString):
    """Custom type cfgRamInstalledSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRamInstalledSize_Type.__name__ = "DisplayString"
_CfgRamInstalledSize_Object = MibScalar
cfgRamInstalledSize = _CfgRamInstalledSize_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3510),
    _CfgRamInstalledSize_Type()
)
cfgRamInstalledSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRamInstalledSize.setStatus("optional")
_CfgTrayTable_Object = MibTable
cfgTrayTable = _CfgTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3520)
)
if mibBuilder.loadTexts:
    cfgTrayTable.setStatus("optional")
_CfgTrayEntry_Object = MibTableRow
cfgTrayEntry = _CfgTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3520, 1)
)
if mibBuilder.loadTexts:
    cfgTrayEntry.setStatus("optional")


class _CfgTrayIndex_Type(Integer32):
    """Custom type cfgTrayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgTrayIndex_Type.__name__ = "Integer32"
_CfgTrayIndex_Object = MibTableColumn
cfgTrayIndex = _CfgTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3520, 1, 1),
    _CfgTrayIndex_Type()
)
cfgTrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgTrayIndex.setStatus("optional")


class _CfgTrayName_Type(DisplayString):
    """Custom type cfgTrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgTrayName_Type.__name__ = "DisplayString"
_CfgTrayName_Object = MibTableColumn
cfgTrayName = _CfgTrayName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3520, 1, 2),
    _CfgTrayName_Type()
)
cfgTrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgTrayName.setStatus("optional")


class _CfgPrinterName_Type(DisplayString):
    """Custom type cfgPrinterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgPrinterName_Type.__name__ = "DisplayString"
_CfgPrinterName_Object = MibScalar
cfgPrinterName = _CfgPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 1, 3530),
    _CfgPrinterName_Type()
)
cfgPrinterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgPrinterName.setStatus("optional")
_Stat_ObjectIdentity = ObjectIdentity
stat = _Stat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 2)
)


class _StPjlStatus_Type(DisplayString):
    """Custom type stPjlStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_StPjlStatus_Type.__name__ = "DisplayString"
_StPjlStatus_Object = MibScalar
stPjlStatus = _StPjlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 2, 10),
    _StPjlStatus_Type()
)
stPjlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stPjlStatus.setStatus("optional")


class _StLcdMessage_Type(DisplayString):
    """Custom type stLcdMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_StLcdMessage_Type.__name__ = "DisplayString"
_StLcdMessage_Object = MibScalar
stLcdMessage = _StLcdMessage_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 2, 20),
    _StLcdMessage_Type()
)
stLcdMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stLcdMessage.setStatus("optional")


class _StOnline_Type(DisplayString):
    """Custom type stOnline based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_StOnline_Type.__name__ = "DisplayString"
_StOnline_Object = MibScalar
stOnline = _StOnline_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 2, 30),
    _StOnline_Type()
)
stOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stOnline.setStatus("optional")


class _StManualLedStatus_Type(DisplayString):
    """Custom type stManualLedStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_StManualLedStatus_Type.__name__ = "DisplayString"
_StManualLedStatus_Object = MibScalar
stManualLedStatus = _StManualLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 2, 100),
    _StManualLedStatus_Type()
)
stManualLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stManualLedStatus.setStatus("optional")


class _StOperatorLedStatus_Type(DisplayString):
    """Custom type stOperatorLedStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_StOperatorLedStatus_Type.__name__ = "DisplayString"
_StOperatorLedStatus_Object = MibScalar
stOperatorLedStatus = _StOperatorLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 2, 110),
    _StOperatorLedStatus_Type()
)
stOperatorLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stOperatorLedStatus.setStatus("optional")


class _StServiceLedStatus_Type(DisplayString):
    """Custom type stServiceLedStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_StServiceLedStatus_Type.__name__ = "DisplayString"
_StServiceLedStatus_Object = MibScalar
stServiceLedStatus = _StServiceLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 2, 120),
    _StServiceLedStatus_Type()
)
stServiceLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stServiceLedStatus.setStatus("optional")


class _StOnlineLedStatus_Type(DisplayString):
    """Custom type stOnlineLedStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_StOnlineLedStatus_Type.__name__ = "DisplayString"
_StOnlineLedStatus_Object = MibScalar
stOnlineLedStatus = _StOnlineLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 2, 130),
    _StOnlineLedStatus_Type()
)
stOnlineLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stOnlineLedStatus.setStatus("optional")


class _StPsStatus_Type(DisplayString):
    """Custom type stPsStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_StPsStatus_Type.__name__ = "DisplayString"
_StPsStatus_Object = MibScalar
stPsStatus = _StPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 2, 140),
    _StPsStatus_Type()
)
stPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stPsStatus.setStatus("optional")
_Cfg2_ObjectIdentity = ObjectIdentity
cfg2 = _Cfg2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11)
)
_Cfg2General_ObjectIdentity = ObjectIdentity
cfg2General = _Cfg2General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1)
)
_Cfg2PrinterInformation_ObjectIdentity = ObjectIdentity
cfg2PrinterInformation = _Cfg2PrinterInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10)
)
_Cfg2Type1MIBVersion_Type = DisplayString
_Cfg2Type1MIBVersion_Object = MibScalar
cfg2Type1MIBVersion = _Cfg2Type1MIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 10),
    _Cfg2Type1MIBVersion_Type()
)
cfg2Type1MIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2Type1MIBVersion.setStatus("optional")
_Cfg2ModelId_Type = DisplayString
_Cfg2ModelId_Object = MibScalar
cfg2ModelId = _Cfg2ModelId_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 30),
    _Cfg2ModelId_Type()
)
cfg2ModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2ModelId.setStatus("optional")
_Cfg2PrinterVersions_ObjectIdentity = ObjectIdentity
cfg2PrinterVersions = _Cfg2PrinterVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50)
)
_Cfg2PrinterVersion1Table_ObjectIdentity = ObjectIdentity
cfg2PrinterVersion1Table = _Cfg2PrinterVersion1Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 1)
)
_Cfg2PrinterVersion1_Type = DisplayString
_Cfg2PrinterVersion1_Object = MibScalar
cfg2PrinterVersion1 = _Cfg2PrinterVersion1_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 1, 2),
    _Cfg2PrinterVersion1_Type()
)
cfg2PrinterVersion1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterVersion1.setStatus("optional")
_Cfg2PrinterVersion2Table_ObjectIdentity = ObjectIdentity
cfg2PrinterVersion2Table = _Cfg2PrinterVersion2Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 2)
)
_Cfg2PrinterVersion2_Type = DisplayString
_Cfg2PrinterVersion2_Object = MibScalar
cfg2PrinterVersion2 = _Cfg2PrinterVersion2_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 2, 2),
    _Cfg2PrinterVersion2_Type()
)
cfg2PrinterVersion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterVersion2.setStatus("optional")
_Cfg2PrinterVersion3Table_ObjectIdentity = ObjectIdentity
cfg2PrinterVersion3Table = _Cfg2PrinterVersion3Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 3)
)
_Cfg2PrinterVersion3_Type = DisplayString
_Cfg2PrinterVersion3_Object = MibScalar
cfg2PrinterVersion3 = _Cfg2PrinterVersion3_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 3, 2),
    _Cfg2PrinterVersion3_Type()
)
cfg2PrinterVersion3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterVersion3.setStatus("optional")
_Cfg2PrinterVersion4Table_ObjectIdentity = ObjectIdentity
cfg2PrinterVersion4Table = _Cfg2PrinterVersion4Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 4)
)
_Cfg2PrinterVersion4_Type = DisplayString
_Cfg2PrinterVersion4_Object = MibScalar
cfg2PrinterVersion4 = _Cfg2PrinterVersion4_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 4, 2),
    _Cfg2PrinterVersion4_Type()
)
cfg2PrinterVersion4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterVersion4.setStatus("optional")
_Cfg2PrinterVersion5Table_ObjectIdentity = ObjectIdentity
cfg2PrinterVersion5Table = _Cfg2PrinterVersion5Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 5)
)
_Cfg2PrinterVersion5_Type = DisplayString
_Cfg2PrinterVersion5_Object = MibScalar
cfg2PrinterVersion5 = _Cfg2PrinterVersion5_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 5, 2),
    _Cfg2PrinterVersion5_Type()
)
cfg2PrinterVersion5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterVersion5.setStatus("optional")
_Cfg2PrinterVersion6Table_ObjectIdentity = ObjectIdentity
cfg2PrinterVersion6Table = _Cfg2PrinterVersion6Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 6)
)
_Cfg2PrinterVersion6_Type = DisplayString
_Cfg2PrinterVersion6_Object = MibScalar
cfg2PrinterVersion6 = _Cfg2PrinterVersion6_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 6, 2),
    _Cfg2PrinterVersion6_Type()
)
cfg2PrinterVersion6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterVersion6.setStatus("optional")
_Cfg2PrinterVersion7Table_ObjectIdentity = ObjectIdentity
cfg2PrinterVersion7Table = _Cfg2PrinterVersion7Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 7)
)
_Cfg2PrinterVersion7_Type = DisplayString
_Cfg2PrinterVersion7_Object = MibScalar
cfg2PrinterVersion7 = _Cfg2PrinterVersion7_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 7, 2),
    _Cfg2PrinterVersion7_Type()
)
cfg2PrinterVersion7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterVersion7.setStatus("optional")
_Cfg2PrinterVersion8Table_ObjectIdentity = ObjectIdentity
cfg2PrinterVersion8Table = _Cfg2PrinterVersion8Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 8)
)
_Cfg2PrinterVersion8_Type = DisplayString
_Cfg2PrinterVersion8_Object = MibScalar
cfg2PrinterVersion8 = _Cfg2PrinterVersion8_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 8, 2),
    _Cfg2PrinterVersion8_Type()
)
cfg2PrinterVersion8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterVersion8.setStatus("optional")
_Cfg2PrinterVersion9Table_ObjectIdentity = ObjectIdentity
cfg2PrinterVersion9Table = _Cfg2PrinterVersion9Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 9)
)
_Cfg2PrinterVersion9_Type = DisplayString
_Cfg2PrinterVersion9_Object = MibScalar
cfg2PrinterVersion9 = _Cfg2PrinterVersion9_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 9, 2),
    _Cfg2PrinterVersion9_Type()
)
cfg2PrinterVersion9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterVersion9.setStatus("optional")
_Cfg2PrinterVersion10Table_ObjectIdentity = ObjectIdentity
cfg2PrinterVersion10Table = _Cfg2PrinterVersion10Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 10)
)
_Cfg2PrinterVersion10_Type = DisplayString
_Cfg2PrinterVersion10_Object = MibScalar
cfg2PrinterVersion10 = _Cfg2PrinterVersion10_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 50, 10, 2),
    _Cfg2PrinterVersion10_Type()
)
cfg2PrinterVersion10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterVersion10.setStatus("optional")
_Cfg2PrinterType_Type = DisplayString
_Cfg2PrinterType_Object = MibScalar
cfg2PrinterType = _Cfg2PrinterType_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 10, 70),
    _Cfg2PrinterType_Type()
)
cfg2PrinterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2PrinterType.setStatus("optional")
_Cfg2PrinterConsumption_ObjectIdentity = ObjectIdentity
cfg2PrinterConsumption = _Cfg2PrinterConsumption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 20)
)
_Cfg2PowerSave_ObjectIdentity = ObjectIdentity
cfg2PowerSave = _Cfg2PowerSave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 20, 10)
)
_Cfg2PowerSaveCurrentValue_Type = DisplayString
_Cfg2PowerSaveCurrentValue_Object = MibScalar
cfg2PowerSaveCurrentValue = _Cfg2PowerSaveCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 20, 10, 2),
    _Cfg2PowerSaveCurrentValue_Type()
)
cfg2PowerSaveCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2PowerSaveCurrentValue.setStatus("optional")
_Cfg2PowerSaveShift_ObjectIdentity = ObjectIdentity
cfg2PowerSaveShift = _Cfg2PowerSaveShift_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 20, 11)
)
_Cfg2PowerSaveShiftCurrentValue_Type = DisplayString
_Cfg2PowerSaveShiftCurrentValue_Object = MibScalar
cfg2PowerSaveShiftCurrentValue = _Cfg2PowerSaveShiftCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 20, 11, 2),
    _Cfg2PowerSaveShiftCurrentValue_Type()
)
cfg2PowerSaveShiftCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2PowerSaveShiftCurrentValue.setStatus("optional")
_Cfg2JamRecovery_ObjectIdentity = ObjectIdentity
cfg2JamRecovery = _Cfg2JamRecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 70)
)
_Cfg2JamRecoveryCurrentValue_Type = DisplayString
_Cfg2JamRecoveryCurrentValue_Object = MibScalar
cfg2JamRecoveryCurrentValue = _Cfg2JamRecoveryCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 70, 2),
    _Cfg2JamRecoveryCurrentValue_Type()
)
cfg2JamRecoveryCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2JamRecoveryCurrentValue.setStatus("optional")
_Cfg2OPPanelLock_ObjectIdentity = ObjectIdentity
cfg2OPPanelLock = _Cfg2OPPanelLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 130)
)
_Cfg2OPPanelLockCurrentValue_Type = DisplayString
_Cfg2OPPanelLockCurrentValue_Object = MibScalar
cfg2OPPanelLockCurrentValue = _Cfg2OPPanelLockCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 130, 2),
    _Cfg2OPPanelLockCurrentValue_Type()
)
cfg2OPPanelLockCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2OPPanelLockCurrentValue.setStatus("optional")
_Cfg2Controlt_ObjectIdentity = ObjectIdentity
cfg2Controlt = _Cfg2Controlt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 160)
)
_Cfg2ControltCurrentValue_Type = DisplayString
_Cfg2ControltCurrentValue_Object = MibScalar
cfg2ControltCurrentValue = _Cfg2ControltCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 1, 160, 2),
    _Cfg2ControltCurrentValue_Type()
)
cfg2ControltCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2ControltCurrentValue.setStatus("optional")
_Cfg2JobControl_ObjectIdentity = ObjectIdentity
cfg2JobControl = _Cfg2JobControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 2)
)
_Cfg2PaperHandling_ObjectIdentity = ObjectIdentity
cfg2PaperHandling = _Cfg2PaperHandling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3)
)
_Cfg2PHCommon_ObjectIdentity = ObjectIdentity
cfg2PHCommon = _Cfg2PHCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 1)
)
_Cfg2MonoPrintSpeed_ObjectIdentity = ObjectIdentity
cfg2MonoPrintSpeed = _Cfg2MonoPrintSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 1, 20)
)
_Cfg2MonoPrintSpeedCurrentValue_Type = DisplayString
_Cfg2MonoPrintSpeedCurrentValue_Object = MibScalar
cfg2MonoPrintSpeedCurrentValue = _Cfg2MonoPrintSpeedCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 1, 20, 2),
    _Cfg2MonoPrintSpeedCurrentValue_Type()
)
cfg2MonoPrintSpeedCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2MonoPrintSpeedCurrentValue.setStatus("optional")
_Cfg2PHInput_ObjectIdentity = ObjectIdentity
cfg2PHInput = _Cfg2PHInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2)
)
_Cfg2PriorityTray_ObjectIdentity = ObjectIdentity
cfg2PriorityTray = _Cfg2PriorityTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 30)
)
_Cfg2PriorityTrayCurrentValue_Type = DisplayString
_Cfg2PriorityTrayCurrentValue_Object = MibScalar
cfg2PriorityTrayCurrentValue = _Cfg2PriorityTrayCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 30, 2),
    _Cfg2PriorityTrayCurrentValue_Type()
)
cfg2PriorityTrayCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2PriorityTrayCurrentValue.setStatus("optional")
_Cfg2TrayTable_ObjectIdentity = ObjectIdentity
cfg2TrayTable = _Cfg2TrayTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40)
)
_Cfg2Tray1Table_ObjectIdentity = ObjectIdentity
cfg2Tray1Table = _Cfg2Tray1Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 1)
)
_Cfg2Tray1PaperSize_ObjectIdentity = ObjectIdentity
cfg2Tray1PaperSize = _Cfg2Tray1PaperSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 1, 1)
)
_Cfg2Tray1PaperSizeCurrentValue_Type = DisplayString
_Cfg2Tray1PaperSizeCurrentValue_Object = MibScalar
cfg2Tray1PaperSizeCurrentValue = _Cfg2Tray1PaperSizeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 1, 1, 2),
    _Cfg2Tray1PaperSizeCurrentValue_Type()
)
cfg2Tray1PaperSizeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray1PaperSizeCurrentValue.setStatus("optional")
_Cfg2Tray1MediaType_ObjectIdentity = ObjectIdentity
cfg2Tray1MediaType = _Cfg2Tray1MediaType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 1, 2)
)
_Cfg2Tray1MediaTypeCurrentValue_Type = DisplayString
_Cfg2Tray1MediaTypeCurrentValue_Object = MibScalar
cfg2Tray1MediaTypeCurrentValue = _Cfg2Tray1MediaTypeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 1, 2, 2),
    _Cfg2Tray1MediaTypeCurrentValue_Type()
)
cfg2Tray1MediaTypeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray1MediaTypeCurrentValue.setStatus("optional")
_Cfg2Tray1MediaWeight_ObjectIdentity = ObjectIdentity
cfg2Tray1MediaWeight = _Cfg2Tray1MediaWeight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 1, 3)
)
_Cfg2Tray1MediaWeightCurrentValue_Type = DisplayString
_Cfg2Tray1MediaWeightCurrentValue_Object = MibScalar
cfg2Tray1MediaWeightCurrentValue = _Cfg2Tray1MediaWeightCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 1, 3, 2),
    _Cfg2Tray1MediaWeightCurrentValue_Type()
)
cfg2Tray1MediaWeightCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray1MediaWeightCurrentValue.setStatus("optional")
_Cfg2Tray2Table_ObjectIdentity = ObjectIdentity
cfg2Tray2Table = _Cfg2Tray2Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 2)
)
_Cfg2Tray2PaperSize_ObjectIdentity = ObjectIdentity
cfg2Tray2PaperSize = _Cfg2Tray2PaperSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 2, 1)
)
_Cfg2Tray2PaperSizeCurrentValue_Type = DisplayString
_Cfg2Tray2PaperSizeCurrentValue_Object = MibScalar
cfg2Tray2PaperSizeCurrentValue = _Cfg2Tray2PaperSizeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 2, 1, 2),
    _Cfg2Tray2PaperSizeCurrentValue_Type()
)
cfg2Tray2PaperSizeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray2PaperSizeCurrentValue.setStatus("optional")
_Cfg2Tray2MediaType_ObjectIdentity = ObjectIdentity
cfg2Tray2MediaType = _Cfg2Tray2MediaType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 2, 2)
)
_Cfg2Tray2MediaTypeCurrentValue_Type = DisplayString
_Cfg2Tray2MediaTypeCurrentValue_Object = MibScalar
cfg2Tray2MediaTypeCurrentValue = _Cfg2Tray2MediaTypeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 2, 2, 2),
    _Cfg2Tray2MediaTypeCurrentValue_Type()
)
cfg2Tray2MediaTypeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray2MediaTypeCurrentValue.setStatus("optional")
_Cfg2Tray2MediaWeight_ObjectIdentity = ObjectIdentity
cfg2Tray2MediaWeight = _Cfg2Tray2MediaWeight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 2, 3)
)
_Cfg2Tray2MediaWeightCurrentValue_Type = DisplayString
_Cfg2Tray2MediaWeightCurrentValue_Object = MibScalar
cfg2Tray2MediaWeightCurrentValue = _Cfg2Tray2MediaWeightCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 2, 3, 2),
    _Cfg2Tray2MediaWeightCurrentValue_Type()
)
cfg2Tray2MediaWeightCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray2MediaWeightCurrentValue.setStatus("optional")
_Cfg2Tray3Table_ObjectIdentity = ObjectIdentity
cfg2Tray3Table = _Cfg2Tray3Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 3)
)
_Cfg2Tray3PaperSize_ObjectIdentity = ObjectIdentity
cfg2Tray3PaperSize = _Cfg2Tray3PaperSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 3, 1)
)
_Cfg2Tray3PaperSizeCurrentValue_Type = DisplayString
_Cfg2Tray3PaperSizeCurrentValue_Object = MibScalar
cfg2Tray3PaperSizeCurrentValue = _Cfg2Tray3PaperSizeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 3, 1, 2),
    _Cfg2Tray3PaperSizeCurrentValue_Type()
)
cfg2Tray3PaperSizeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray3PaperSizeCurrentValue.setStatus("optional")
_Cfg2Tray3MediaType_ObjectIdentity = ObjectIdentity
cfg2Tray3MediaType = _Cfg2Tray3MediaType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 3, 2)
)
_Cfg2Tray3MediaTypeCurrentValue_Type = DisplayString
_Cfg2Tray3MediaTypeCurrentValue_Object = MibScalar
cfg2Tray3MediaTypeCurrentValue = _Cfg2Tray3MediaTypeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 3, 2, 2),
    _Cfg2Tray3MediaTypeCurrentValue_Type()
)
cfg2Tray3MediaTypeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray3MediaTypeCurrentValue.setStatus("optional")
_Cfg2Tray3MediaWeight_ObjectIdentity = ObjectIdentity
cfg2Tray3MediaWeight = _Cfg2Tray3MediaWeight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 3, 3)
)
_Cfg2Tray3MediaWeightCurrentValue_Type = DisplayString
_Cfg2Tray3MediaWeightCurrentValue_Object = MibScalar
cfg2Tray3MediaWeightCurrentValue = _Cfg2Tray3MediaWeightCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 3, 3, 2),
    _Cfg2Tray3MediaWeightCurrentValue_Type()
)
cfg2Tray3MediaWeightCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray3MediaWeightCurrentValue.setStatus("optional")
_Cfg2Tray4Table_ObjectIdentity = ObjectIdentity
cfg2Tray4Table = _Cfg2Tray4Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 4)
)
_Cfg2Tray4PaperSize_ObjectIdentity = ObjectIdentity
cfg2Tray4PaperSize = _Cfg2Tray4PaperSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 4, 1)
)
_Cfg2Tray4PaperSizeCurrentValue_Type = DisplayString
_Cfg2Tray4PaperSizeCurrentValue_Object = MibScalar
cfg2Tray4PaperSizeCurrentValue = _Cfg2Tray4PaperSizeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 4, 1, 2),
    _Cfg2Tray4PaperSizeCurrentValue_Type()
)
cfg2Tray4PaperSizeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray4PaperSizeCurrentValue.setStatus("optional")
_Cfg2Tray4MediaType_ObjectIdentity = ObjectIdentity
cfg2Tray4MediaType = _Cfg2Tray4MediaType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 4, 2)
)
_Cfg2Tray4MediaTypeCurrentValue_Type = DisplayString
_Cfg2Tray4MediaTypeCurrentValue_Object = MibScalar
cfg2Tray4MediaTypeCurrentValue = _Cfg2Tray4MediaTypeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 4, 2, 2),
    _Cfg2Tray4MediaTypeCurrentValue_Type()
)
cfg2Tray4MediaTypeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray4MediaTypeCurrentValue.setStatus("optional")
_Cfg2Tray4MediaWeight_ObjectIdentity = ObjectIdentity
cfg2Tray4MediaWeight = _Cfg2Tray4MediaWeight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 4, 3)
)
_Cfg2Tray4MediaWeightCurrentValue_Type = DisplayString
_Cfg2Tray4MediaWeightCurrentValue_Object = MibScalar
cfg2Tray4MediaWeightCurrentValue = _Cfg2Tray4MediaWeightCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 4, 3, 2),
    _Cfg2Tray4MediaWeightCurrentValue_Type()
)
cfg2Tray4MediaWeightCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray4MediaWeightCurrentValue.setStatus("optional")
_Cfg2Tray5Table_ObjectIdentity = ObjectIdentity
cfg2Tray5Table = _Cfg2Tray5Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 5)
)
_Cfg2Tray5PaperSize_ObjectIdentity = ObjectIdentity
cfg2Tray5PaperSize = _Cfg2Tray5PaperSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 5, 1)
)
_Cfg2Tray5PaperSizeCurrentValue_Type = DisplayString
_Cfg2Tray5PaperSizeCurrentValue_Object = MibScalar
cfg2Tray5PaperSizeCurrentValue = _Cfg2Tray5PaperSizeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 5, 1, 2),
    _Cfg2Tray5PaperSizeCurrentValue_Type()
)
cfg2Tray5PaperSizeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray5PaperSizeCurrentValue.setStatus("optional")
_Cfg2Tray5MediaType_ObjectIdentity = ObjectIdentity
cfg2Tray5MediaType = _Cfg2Tray5MediaType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 5, 2)
)
_Cfg2Tray5MediaTypeCurrentValue_Type = DisplayString
_Cfg2Tray5MediaTypeCurrentValue_Object = MibScalar
cfg2Tray5MediaTypeCurrentValue = _Cfg2Tray5MediaTypeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 5, 2, 2),
    _Cfg2Tray5MediaTypeCurrentValue_Type()
)
cfg2Tray5MediaTypeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray5MediaTypeCurrentValue.setStatus("optional")
_Cfg2Tray5MediaWeight_ObjectIdentity = ObjectIdentity
cfg2Tray5MediaWeight = _Cfg2Tray5MediaWeight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 5, 3)
)
_Cfg2Tray5MediaWeightCurrentValue_Type = DisplayString
_Cfg2Tray5MediaWeightCurrentValue_Object = MibScalar
cfg2Tray5MediaWeightCurrentValue = _Cfg2Tray5MediaWeightCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 5, 3, 2),
    _Cfg2Tray5MediaWeightCurrentValue_Type()
)
cfg2Tray5MediaWeightCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray5MediaWeightCurrentValue.setStatus("optional")
_Cfg2Tray6Table_ObjectIdentity = ObjectIdentity
cfg2Tray6Table = _Cfg2Tray6Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 6)
)
_Cfg2Tray6PaperSize_ObjectIdentity = ObjectIdentity
cfg2Tray6PaperSize = _Cfg2Tray6PaperSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 6, 1)
)
_Cfg2Tray6PaperSizeCurrentValue_Type = DisplayString
_Cfg2Tray6PaperSizeCurrentValue_Object = MibScalar
cfg2Tray6PaperSizeCurrentValue = _Cfg2Tray6PaperSizeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 6, 1, 2),
    _Cfg2Tray6PaperSizeCurrentValue_Type()
)
cfg2Tray6PaperSizeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray6PaperSizeCurrentValue.setStatus("optional")
_Cfg2Tray6MediaType_ObjectIdentity = ObjectIdentity
cfg2Tray6MediaType = _Cfg2Tray6MediaType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 6, 2)
)
_Cfg2Tray6MediaTypeCurrentValue_Type = DisplayString
_Cfg2Tray6MediaTypeCurrentValue_Object = MibScalar
cfg2Tray6MediaTypeCurrentValue = _Cfg2Tray6MediaTypeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 6, 2, 2),
    _Cfg2Tray6MediaTypeCurrentValue_Type()
)
cfg2Tray6MediaTypeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray6MediaTypeCurrentValue.setStatus("optional")
_Cfg2Tray6MediaWeight_ObjectIdentity = ObjectIdentity
cfg2Tray6MediaWeight = _Cfg2Tray6MediaWeight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 6, 3)
)
_Cfg2Tray6MediaWeightCurrentValue_Type = DisplayString
_Cfg2Tray6MediaWeightCurrentValue_Object = MibScalar
cfg2Tray6MediaWeightCurrentValue = _Cfg2Tray6MediaWeightCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 6, 3, 2),
    _Cfg2Tray6MediaWeightCurrentValue_Type()
)
cfg2Tray6MediaWeightCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray6MediaWeightCurrentValue.setStatus("optional")
_Cfg2Tray7Table_ObjectIdentity = ObjectIdentity
cfg2Tray7Table = _Cfg2Tray7Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 7)
)
_Cfg2Tray7PaperSize_ObjectIdentity = ObjectIdentity
cfg2Tray7PaperSize = _Cfg2Tray7PaperSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 7, 1)
)
_Cfg2Tray7PaperSizeCurrentValue_Type = DisplayString
_Cfg2Tray7PaperSizeCurrentValue_Object = MibScalar
cfg2Tray7PaperSizeCurrentValue = _Cfg2Tray7PaperSizeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 7, 1, 2),
    _Cfg2Tray7PaperSizeCurrentValue_Type()
)
cfg2Tray7PaperSizeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray7PaperSizeCurrentValue.setStatus("optional")
_Cfg2Tray7MediaType_ObjectIdentity = ObjectIdentity
cfg2Tray7MediaType = _Cfg2Tray7MediaType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 7, 2)
)
_Cfg2Tray7MediaTypeCurrentValue_Type = DisplayString
_Cfg2Tray7MediaTypeCurrentValue_Object = MibScalar
cfg2Tray7MediaTypeCurrentValue = _Cfg2Tray7MediaTypeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 7, 2, 2),
    _Cfg2Tray7MediaTypeCurrentValue_Type()
)
cfg2Tray7MediaTypeCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray7MediaTypeCurrentValue.setStatus("optional")
_Cfg2Tray7MediaWeight_ObjectIdentity = ObjectIdentity
cfg2Tray7MediaWeight = _Cfg2Tray7MediaWeight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 7, 3)
)
_Cfg2Tray7MediaWeightCurrentValue_Type = DisplayString
_Cfg2Tray7MediaWeightCurrentValue_Object = MibScalar
cfg2Tray7MediaWeightCurrentValue = _Cfg2Tray7MediaWeightCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 40, 7, 3, 2),
    _Cfg2Tray7MediaWeightCurrentValue_Type()
)
cfg2Tray7MediaWeightCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray7MediaWeightCurrentValue.setStatus("optional")
_Cfg2UnitOfMeasure_ObjectIdentity = ObjectIdentity
cfg2UnitOfMeasure = _Cfg2UnitOfMeasure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 50)
)
_Cfg2UnitOfMeasureCurrentValue_Type = DisplayString
_Cfg2UnitOfMeasureCurrentValue_Object = MibScalar
cfg2UnitOfMeasureCurrentValue = _Cfg2UnitOfMeasureCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 50, 2),
    _Cfg2UnitOfMeasureCurrentValue_Type()
)
cfg2UnitOfMeasureCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2UnitOfMeasureCurrentValue.setStatus("optional")
_Cfg2XDimension_ObjectIdentity = ObjectIdentity
cfg2XDimension = _Cfg2XDimension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 60)
)
_Cfg2XDimensionCurrentValue_Type = DisplayString
_Cfg2XDimensionCurrentValue_Object = MibScalar
cfg2XDimensionCurrentValue = _Cfg2XDimensionCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 60, 2),
    _Cfg2XDimensionCurrentValue_Type()
)
cfg2XDimensionCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2XDimensionCurrentValue.setStatus("optional")
_Cfg2YDimension_ObjectIdentity = ObjectIdentity
cfg2YDimension = _Cfg2YDimension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 70)
)
_Cfg2YDimensionCurrentValue_Type = DisplayString
_Cfg2YDimensionCurrentValue_Object = MibScalar
cfg2YDimensionCurrentValue = _Cfg2YDimensionCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 70, 2),
    _Cfg2YDimensionCurrentValue_Type()
)
cfg2YDimensionCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2YDimensionCurrentValue.setStatus("optional")
_Cfg2TrayA3Paper_ObjectIdentity = ObjectIdentity
cfg2TrayA3Paper = _Cfg2TrayA3Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90)
)
_Cfg2Tray1A3Paper_ObjectIdentity = ObjectIdentity
cfg2Tray1A3Paper = _Cfg2Tray1A3Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 1)
)
_Cfg2Tray1A3PaperCurrentValue_Type = DisplayString
_Cfg2Tray1A3PaperCurrentValue_Object = MibScalar
cfg2Tray1A3PaperCurrentValue = _Cfg2Tray1A3PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 1, 2),
    _Cfg2Tray1A3PaperCurrentValue_Type()
)
cfg2Tray1A3PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray1A3PaperCurrentValue.setStatus("optional")
_Cfg2Tray2A3Paper_ObjectIdentity = ObjectIdentity
cfg2Tray2A3Paper = _Cfg2Tray2A3Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 2)
)
_Cfg2Tray2A3PaperCurrentValue_Type = DisplayString
_Cfg2Tray2A3PaperCurrentValue_Object = MibScalar
cfg2Tray2A3PaperCurrentValue = _Cfg2Tray2A3PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 2, 2),
    _Cfg2Tray2A3PaperCurrentValue_Type()
)
cfg2Tray2A3PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray2A3PaperCurrentValue.setStatus("optional")
_Cfg2Tray3A3Paper_ObjectIdentity = ObjectIdentity
cfg2Tray3A3Paper = _Cfg2Tray3A3Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 3)
)
_Cfg2Tray3A3PaperCurrentValue_Type = DisplayString
_Cfg2Tray3A3PaperCurrentValue_Object = MibScalar
cfg2Tray3A3PaperCurrentValue = _Cfg2Tray3A3PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 3, 2),
    _Cfg2Tray3A3PaperCurrentValue_Type()
)
cfg2Tray3A3PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray3A3PaperCurrentValue.setStatus("optional")
_Cfg2Tray4A3Paper_ObjectIdentity = ObjectIdentity
cfg2Tray4A3Paper = _Cfg2Tray4A3Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 4)
)
_Cfg2Tray4A3PaperCurrentValue_Type = DisplayString
_Cfg2Tray4A3PaperCurrentValue_Object = MibScalar
cfg2Tray4A3PaperCurrentValue = _Cfg2Tray4A3PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 4, 2),
    _Cfg2Tray4A3PaperCurrentValue_Type()
)
cfg2Tray4A3PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray4A3PaperCurrentValue.setStatus("optional")
_Cfg2Tray5A3Paper_ObjectIdentity = ObjectIdentity
cfg2Tray5A3Paper = _Cfg2Tray5A3Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 5)
)
_Cfg2Tray5A3PaperCurrentValue_Type = DisplayString
_Cfg2Tray5A3PaperCurrentValue_Object = MibScalar
cfg2Tray5A3PaperCurrentValue = _Cfg2Tray5A3PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 5, 2),
    _Cfg2Tray5A3PaperCurrentValue_Type()
)
cfg2Tray5A3PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray5A3PaperCurrentValue.setStatus("optional")
_Cfg2Tray6A3Paper_ObjectIdentity = ObjectIdentity
cfg2Tray6A3Paper = _Cfg2Tray6A3Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 6)
)
_Cfg2Tray6A3PaperCurrentValue_Type = DisplayString
_Cfg2Tray6A3PaperCurrentValue_Object = MibScalar
cfg2Tray6A3PaperCurrentValue = _Cfg2Tray6A3PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 6, 2),
    _Cfg2Tray6A3PaperCurrentValue_Type()
)
cfg2Tray6A3PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray6A3PaperCurrentValue.setStatus("optional")
_Cfg2Tray7A3Paper_ObjectIdentity = ObjectIdentity
cfg2Tray7A3Paper = _Cfg2Tray7A3Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 7)
)
_Cfg2Tray7A3PaperCurrentValue_Type = DisplayString
_Cfg2Tray7A3PaperCurrentValue_Object = MibScalar
cfg2Tray7A3PaperCurrentValue = _Cfg2Tray7A3PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 90, 7, 2),
    _Cfg2Tray7A3PaperCurrentValue_Type()
)
cfg2Tray7A3PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray7A3PaperCurrentValue.setStatus("optional")
_Cfg2TrayLegal14Paper_ObjectIdentity = ObjectIdentity
cfg2TrayLegal14Paper = _Cfg2TrayLegal14Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100)
)
_Cfg2Tray1Legal14Paper_ObjectIdentity = ObjectIdentity
cfg2Tray1Legal14Paper = _Cfg2Tray1Legal14Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 1)
)
_Cfg2Tray1Legal14PaperCurrentValue_Type = DisplayString
_Cfg2Tray1Legal14PaperCurrentValue_Object = MibScalar
cfg2Tray1Legal14PaperCurrentValue = _Cfg2Tray1Legal14PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 1, 2),
    _Cfg2Tray1Legal14PaperCurrentValue_Type()
)
cfg2Tray1Legal14PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray1Legal14PaperCurrentValue.setStatus("optional")
_Cfg2Tray2Legal14Paper_ObjectIdentity = ObjectIdentity
cfg2Tray2Legal14Paper = _Cfg2Tray2Legal14Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 2)
)
_Cfg2Tray2Legal14PaperCurrentValue_Type = DisplayString
_Cfg2Tray2Legal14PaperCurrentValue_Object = MibScalar
cfg2Tray2Legal14PaperCurrentValue = _Cfg2Tray2Legal14PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 2, 2),
    _Cfg2Tray2Legal14PaperCurrentValue_Type()
)
cfg2Tray2Legal14PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray2Legal14PaperCurrentValue.setStatus("optional")
_Cfg2Tray3Legal14Paper_ObjectIdentity = ObjectIdentity
cfg2Tray3Legal14Paper = _Cfg2Tray3Legal14Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 3)
)
_Cfg2Tray3Legal14PaperCurrentValue_Type = DisplayString
_Cfg2Tray3Legal14PaperCurrentValue_Object = MibScalar
cfg2Tray3Legal14PaperCurrentValue = _Cfg2Tray3Legal14PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 3, 2),
    _Cfg2Tray3Legal14PaperCurrentValue_Type()
)
cfg2Tray3Legal14PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray3Legal14PaperCurrentValue.setStatus("optional")
_Cfg2Tray4Legal14Paper_ObjectIdentity = ObjectIdentity
cfg2Tray4Legal14Paper = _Cfg2Tray4Legal14Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 4)
)
_Cfg2Tray4Legal14PaperCurrentValue_Type = DisplayString
_Cfg2Tray4Legal14PaperCurrentValue_Object = MibScalar
cfg2Tray4Legal14PaperCurrentValue = _Cfg2Tray4Legal14PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 4, 2),
    _Cfg2Tray4Legal14PaperCurrentValue_Type()
)
cfg2Tray4Legal14PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray4Legal14PaperCurrentValue.setStatus("optional")
_Cfg2Tray5Legal14Paper_ObjectIdentity = ObjectIdentity
cfg2Tray5Legal14Paper = _Cfg2Tray5Legal14Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 5)
)
_Cfg2Tray5Legal14PaperCurrentValue_Type = DisplayString
_Cfg2Tray5Legal14PaperCurrentValue_Object = MibScalar
cfg2Tray5Legal14PaperCurrentValue = _Cfg2Tray5Legal14PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 5, 2),
    _Cfg2Tray5Legal14PaperCurrentValue_Type()
)
cfg2Tray5Legal14PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray5Legal14PaperCurrentValue.setStatus("optional")
_Cfg2Tray6Legal14Paper_ObjectIdentity = ObjectIdentity
cfg2Tray6Legal14Paper = _Cfg2Tray6Legal14Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 6)
)
_Cfg2Tray6Legal14PaperCurrentValue_Type = DisplayString
_Cfg2Tray6Legal14PaperCurrentValue_Object = MibScalar
cfg2Tray6Legal14PaperCurrentValue = _Cfg2Tray6Legal14PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 6, 2),
    _Cfg2Tray6Legal14PaperCurrentValue_Type()
)
cfg2Tray6Legal14PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray6Legal14PaperCurrentValue.setStatus("optional")
_Cfg2Tray7Legal14Paper_ObjectIdentity = ObjectIdentity
cfg2Tray7Legal14Paper = _Cfg2Tray7Legal14Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 7)
)
_Cfg2Tray7Legal14PaperCurrentValue_Type = DisplayString
_Cfg2Tray7Legal14PaperCurrentValue_Object = MibScalar
cfg2Tray7Legal14PaperCurrentValue = _Cfg2Tray7Legal14PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 100, 7, 2),
    _Cfg2Tray7Legal14PaperCurrentValue_Type()
)
cfg2Tray7Legal14PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray7Legal14PaperCurrentValue.setStatus("optional")
_Cfg2TrayA5A6Paper_ObjectIdentity = ObjectIdentity
cfg2TrayA5A6Paper = _Cfg2TrayA5A6Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110)
)
_Cfg2Tray1A5A6Paper_ObjectIdentity = ObjectIdentity
cfg2Tray1A5A6Paper = _Cfg2Tray1A5A6Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 1)
)
_Cfg2Tray1A5A6PaperCurrentValue_Type = DisplayString
_Cfg2Tray1A5A6PaperCurrentValue_Object = MibScalar
cfg2Tray1A5A6PaperCurrentValue = _Cfg2Tray1A5A6PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 1, 2),
    _Cfg2Tray1A5A6PaperCurrentValue_Type()
)
cfg2Tray1A5A6PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray1A5A6PaperCurrentValue.setStatus("optional")
_Cfg2Tray2A5A6Paper_ObjectIdentity = ObjectIdentity
cfg2Tray2A5A6Paper = _Cfg2Tray2A5A6Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 2)
)
_Cfg2Tray2A5A6PaperCurrentValue_Type = DisplayString
_Cfg2Tray2A5A6PaperCurrentValue_Object = MibScalar
cfg2Tray2A5A6PaperCurrentValue = _Cfg2Tray2A5A6PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 2, 2),
    _Cfg2Tray2A5A6PaperCurrentValue_Type()
)
cfg2Tray2A5A6PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray2A5A6PaperCurrentValue.setStatus("optional")
_Cfg2Tray3A5A6Paper_ObjectIdentity = ObjectIdentity
cfg2Tray3A5A6Paper = _Cfg2Tray3A5A6Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 3)
)
_Cfg2Tray3A5A6PaperCurrentValue_Type = DisplayString
_Cfg2Tray3A5A6PaperCurrentValue_Object = MibScalar
cfg2Tray3A5A6PaperCurrentValue = _Cfg2Tray3A5A6PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 3, 2),
    _Cfg2Tray3A5A6PaperCurrentValue_Type()
)
cfg2Tray3A5A6PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray3A5A6PaperCurrentValue.setStatus("optional")
_Cfg2Tray4A5A6Paper_ObjectIdentity = ObjectIdentity
cfg2Tray4A5A6Paper = _Cfg2Tray4A5A6Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 4)
)
_Cfg2Tray4A5A6PaperCurrentValue_Type = DisplayString
_Cfg2Tray4A5A6PaperCurrentValue_Object = MibScalar
cfg2Tray4A5A6PaperCurrentValue = _Cfg2Tray4A5A6PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 4, 2),
    _Cfg2Tray4A5A6PaperCurrentValue_Type()
)
cfg2Tray4A5A6PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray4A5A6PaperCurrentValue.setStatus("optional")
_Cfg2Tray5A5A6Paper_ObjectIdentity = ObjectIdentity
cfg2Tray5A5A6Paper = _Cfg2Tray5A5A6Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 5)
)
_Cfg2Tray5A5A6PaperCurrentValue_Type = DisplayString
_Cfg2Tray5A5A6PaperCurrentValue_Object = MibScalar
cfg2Tray5A5A6PaperCurrentValue = _Cfg2Tray5A5A6PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 5, 2),
    _Cfg2Tray5A5A6PaperCurrentValue_Type()
)
cfg2Tray5A5A6PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray5A5A6PaperCurrentValue.setStatus("optional")
_Cfg2Tray6A5A6Paper_ObjectIdentity = ObjectIdentity
cfg2Tray6A5A6Paper = _Cfg2Tray6A5A6Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 6)
)
_Cfg2Tray6A5A6PaperCurrentValue_Type = DisplayString
_Cfg2Tray6A5A6PaperCurrentValue_Object = MibScalar
cfg2Tray6A5A6PaperCurrentValue = _Cfg2Tray6A5A6PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 6, 2),
    _Cfg2Tray6A5A6PaperCurrentValue_Type()
)
cfg2Tray6A5A6PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray6A5A6PaperCurrentValue.setStatus("optional")
_Cfg2Tray7A5A6Paper_ObjectIdentity = ObjectIdentity
cfg2Tray7A5A6Paper = _Cfg2Tray7A5A6Paper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 7)
)
_Cfg2Tray7A5A6PaperCurrentValue_Type = DisplayString
_Cfg2Tray7A5A6PaperCurrentValue_Object = MibScalar
cfg2Tray7A5A6PaperCurrentValue = _Cfg2Tray7A5A6PaperCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 2, 110, 7, 2),
    _Cfg2Tray7A5A6PaperCurrentValue_Type()
)
cfg2Tray7A5A6PaperCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2Tray7A5A6PaperCurrentValue.setStatus("optional")
_Cfg2PHOutput_ObjectIdentity = ObjectIdentity
cfg2PHOutput = _Cfg2PHOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 3)
)
_Cfg2OutputBin_ObjectIdentity = ObjectIdentity
cfg2OutputBin = _Cfg2OutputBin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 3, 10)
)
_Cfg2OutputBinCurrentValue_Type = DisplayString
_Cfg2OutputBinCurrentValue_Object = MibScalar
cfg2OutputBinCurrentValue = _Cfg2OutputBinCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 3, 10, 2),
    _Cfg2OutputBinCurrentValue_Type()
)
cfg2OutputBinCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2OutputBinCurrentValue.setStatus("optional")
_Cfg2PHDuplex_ObjectIdentity = ObjectIdentity
cfg2PHDuplex = _Cfg2PHDuplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 4)
)
_Cfg2Duplex_ObjectIdentity = ObjectIdentity
cfg2Duplex = _Cfg2Duplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 4, 10)
)
_Cfg2DuplexCurrentValue_Type = DisplayString
_Cfg2DuplexCurrentValue_Object = MibScalar
cfg2DuplexCurrentValue = _Cfg2DuplexCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 4, 10, 2),
    _Cfg2DuplexCurrentValue_Type()
)
cfg2DuplexCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2DuplexCurrentValue.setStatus("optional")
_Cfg2Binding_ObjectIdentity = ObjectIdentity
cfg2Binding = _Cfg2Binding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 4, 20)
)
_Cfg2BindingCurrentValue_Type = DisplayString
_Cfg2BindingCurrentValue_Object = MibScalar
cfg2BindingCurrentValue = _Cfg2BindingCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 3, 4, 20, 2),
    _Cfg2BindingCurrentValue_Type()
)
cfg2BindingCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2BindingCurrentValue.setStatus("optional")
_Cfg2PrintProcessControl_ObjectIdentity = ObjectIdentity
cfg2PrintProcessControl = _Cfg2PrintProcessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4)
)
_Cfg2PPCColor_ObjectIdentity = ObjectIdentity
cfg2PPCColor = _Cfg2PPCColor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 1)
)
_Cfg2AutoRegistration_ObjectIdentity = ObjectIdentity
cfg2AutoRegistration = _Cfg2AutoRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 1, 30)
)
_Cfg2AutoRegistrationCurrentValue_Type = DisplayString
_Cfg2AutoRegistrationCurrentValue_Object = MibScalar
cfg2AutoRegistrationCurrentValue = _Cfg2AutoRegistrationCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 1, 30, 2),
    _Cfg2AutoRegistrationCurrentValue_Type()
)
cfg2AutoRegistrationCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2AutoRegistrationCurrentValue.setStatus("optional")
_Cfg2PPCDevelopmentControl_ObjectIdentity = ObjectIdentity
cfg2PPCDevelopmentControl = _Cfg2PPCDevelopmentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 2)
)
_Cfg2JobOffset_ObjectIdentity = ObjectIdentity
cfg2JobOffset = _Cfg2JobOffset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 2, 20)
)
_Cfg2JobOffsetCurrentValue_Type = DisplayString
_Cfg2JobOffsetCurrentValue_Object = MibScalar
cfg2JobOffsetCurrentValue = _Cfg2JobOffsetCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 2, 20, 2),
    _Cfg2JobOffsetCurrentValue_Type()
)
cfg2JobOffsetCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfg2JobOffsetCurrentValue.setStatus("optional")
_Cfg2PPCLEDHeadControl_ObjectIdentity = ObjectIdentity
cfg2PPCLEDHeadControl = _Cfg2PPCLEDHeadControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 3)
)
_Cfg2PPCFusingControl_ObjectIdentity = ObjectIdentity
cfg2PPCFusingControl = _Cfg2PPCFusingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 4)
)
_Cfg2PPCPrintPositionControl_ObjectIdentity = ObjectIdentity
cfg2PPCPrintPositionControl = _Cfg2PPCPrintPositionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 5)
)
_Cfg2PPCTonerControl_ObjectIdentity = ObjectIdentity
cfg2PPCTonerControl = _Cfg2PPCTonerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 6)
)
_Cfg2PPCDrumControl_ObjectIdentity = ObjectIdentity
cfg2PPCDrumControl = _Cfg2PPCDrumControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 4, 7)
)
_Cfg2HostInterface_ObjectIdentity = ObjectIdentity
cfg2HostInterface = _Cfg2HostInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 5)
)
_Cfg2LocalResources_ObjectIdentity = ObjectIdentity
cfg2LocalResources = _Cfg2LocalResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 6)
)
_Cfg2LRCommon_ObjectIdentity = ObjectIdentity
cfg2LRCommon = _Cfg2LRCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 6, 1)
)
_Cfg2StoragePartitionTable_Object = MibTable
cfg2StoragePartitionTable = _Cfg2StoragePartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 6, 1, 1)
)
if mibBuilder.loadTexts:
    cfg2StoragePartitionTable.setStatus("optional")
_Cfg2StoragePartitionEntry_Object = MibTableRow
cfg2StoragePartitionEntry = _Cfg2StoragePartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 6, 1, 1, 1)
)
cfg2StoragePartitionEntry.setIndexNames(
    (0, "OKIDATA-MIB", "hrDeviceIndex"),
    (0, "OKIDATA-MIB", "hrPartitionIndex"),
)
if mibBuilder.loadTexts:
    cfg2StoragePartitionEntry.setStatus("optional")
_Cfg2StoragePartitionIndex_Type = Integer32
_Cfg2StoragePartitionIndex_Object = MibTableColumn
cfg2StoragePartitionIndex = _Cfg2StoragePartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 6, 1, 1, 1, 1),
    _Cfg2StoragePartitionIndex_Type()
)
cfg2StoragePartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2StoragePartitionIndex.setStatus("optional")
_Cfg2StoragePartitionFree_Type = Integer32
_Cfg2StoragePartitionFree_Object = MibTableColumn
cfg2StoragePartitionFree = _Cfg2StoragePartitionFree_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 6, 1, 1, 1, 2),
    _Cfg2StoragePartitionFree_Type()
)
cfg2StoragePartitionFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfg2StoragePartitionFree.setStatus("optional")
_Cfg2LRMemory_ObjectIdentity = ObjectIdentity
cfg2LRMemory = _Cfg2LRMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 6, 2)
)
_Cfg2LRHdd_ObjectIdentity = ObjectIdentity
cfg2LRHdd = _Cfg2LRHdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 6, 3)
)
_Cfg2Emulation_ObjectIdentity = ObjectIdentity
cfg2Emulation = _Cfg2Emulation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 7)
)
_Cfg2Test_ObjectIdentity = ObjectIdentity
cfg2Test = _Cfg2Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 8)
)
_Cfg2Menu_ObjectIdentity = ObjectIdentity
cfg2Menu = _Cfg2Menu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 11, 9)
)
_Usage_ObjectIdentity = ObjectIdentity
usage = _Usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100)
)
_UsagePrinterUnit_ObjectIdentity = ObjectIdentity
usagePrinterUnit = _UsagePrinterUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 1)
)
_UsagePrinterUnitTable_Object = MibTable
usagePrinterUnitTable = _UsagePrinterUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 1, 1)
)
if mibBuilder.loadTexts:
    usagePrinterUnitTable.setStatus("optional")
_UsagePrinterUnitEntry_Object = MibTableRow
usagePrinterUnitEntry = _UsagePrinterUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 1, 1, 1)
)
usagePrinterUnitEntry.setIndexNames(
    (0, "OKIDATA-MIB", "usagePrinterUnitIndex"),
)
if mibBuilder.loadTexts:
    usagePrinterUnitEntry.setStatus("optional")
_UsagePrinterUnitIndex_Type = Integer32
_UsagePrinterUnitIndex_Object = MibTableColumn
usagePrinterUnitIndex = _UsagePrinterUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 1, 1, 1, 1),
    _UsagePrinterUnitIndex_Type()
)
usagePrinterUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usagePrinterUnitIndex.setStatus("optional")
_UsagePrinterUnitCounter_Type = DisplayString
_UsagePrinterUnitCounter_Object = MibTableColumn
usagePrinterUnitCounter = _UsagePrinterUnitCounter_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 1, 1, 1, 3),
    _UsagePrinterUnitCounter_Type()
)
usagePrinterUnitCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usagePrinterUnitCounter.setStatus("optional")
_UsagePrinterUnitCounterLife_Type = DisplayString
_UsagePrinterUnitCounterLife_Object = MibTableColumn
usagePrinterUnitCounterLife = _UsagePrinterUnitCounterLife_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 1, 1, 1, 4),
    _UsagePrinterUnitCounterLife_Type()
)
usagePrinterUnitCounterLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usagePrinterUnitCounterLife.setStatus("optional")
_UsageTray_ObjectIdentity = ObjectIdentity
usageTray = _UsageTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 2)
)
_UsageTrayTable_Object = MibTable
usageTrayTable = _UsageTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    usageTrayTable.setStatus("optional")
_UsageTrayEntry_Object = MibTableRow
usageTrayEntry = _UsageTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 2, 1, 1)
)
usageTrayEntry.setIndexNames(
    (0, "OKIDATA-MIB", "usageTrayIndex"),
)
if mibBuilder.loadTexts:
    usageTrayEntry.setStatus("optional")
_UsageTrayIndex_Type = Integer32
_UsageTrayIndex_Object = MibTableColumn
usageTrayIndex = _UsageTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 2, 1, 1, 1),
    _UsageTrayIndex_Type()
)
usageTrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageTrayIndex.setStatus("optional")
_UsageTrayMaxLevel_Type = DisplayString
_UsageTrayMaxLevel_Object = MibTableColumn
usageTrayMaxLevel = _UsageTrayMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 2, 1, 1, 4),
    _UsageTrayMaxLevel_Type()
)
usageTrayMaxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageTrayMaxLevel.setStatus("optional")
_UsageTrayCounter_Type = DisplayString
_UsageTrayCounter_Object = MibTableColumn
usageTrayCounter = _UsageTrayCounter_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 2, 1, 1, 7),
    _UsageTrayCounter_Type()
)
usageTrayCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageTrayCounter.setStatus("optional")
_UsageToner_ObjectIdentity = ObjectIdentity
usageToner = _UsageToner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 3)
)
_UsageTonerTable_Object = MibTable
usageTonerTable = _UsageTonerTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 3, 1)
)
if mibBuilder.loadTexts:
    usageTonerTable.setStatus("optional")
_UsageTonerEntry_Object = MibTableRow
usageTonerEntry = _UsageTonerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 3, 1, 1)
)
usageTonerEntry.setIndexNames(
    (0, "OKIDATA-MIB", "usageTonerIndex"),
)
if mibBuilder.loadTexts:
    usageTonerEntry.setStatus("optional")
_UsageTonerIndex_Type = Integer32
_UsageTonerIndex_Object = MibTableColumn
usageTonerIndex = _UsageTonerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 3, 1, 1, 1),
    _UsageTonerIndex_Type()
)
usageTonerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageTonerIndex.setStatus("optional")
_UsageTonerDescription_Type = DisplayString
_UsageTonerDescription_Object = MibTableColumn
usageTonerDescription = _UsageTonerDescription_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 3, 1, 1, 2),
    _UsageTonerDescription_Type()
)
usageTonerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageTonerDescription.setStatus("optional")
_UsageTonerCurrentLevel_Type = DisplayString
_UsageTonerCurrentLevel_Object = MibTableColumn
usageTonerCurrentLevel = _UsageTonerCurrentLevel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 3, 1, 1, 3),
    _UsageTonerCurrentLevel_Type()
)
usageTonerCurrentLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageTonerCurrentLevel.setStatus("optional")
_UsageTonerMaxLevel_Type = DisplayString
_UsageTonerMaxLevel_Object = MibTableColumn
usageTonerMaxLevel = _UsageTonerMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 3, 1, 1, 4),
    _UsageTonerMaxLevel_Type()
)
usageTonerMaxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageTonerMaxLevel.setStatus("optional")
_UsageTonerLevelUnit_Type = DisplayString
_UsageTonerLevelUnit_Object = MibTableColumn
usageTonerLevelUnit = _UsageTonerLevelUnit_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 3, 1, 1, 5),
    _UsageTonerLevelUnit_Type()
)
usageTonerLevelUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageTonerLevelUnit.setStatus("optional")
_UsageDrum_ObjectIdentity = ObjectIdentity
usageDrum = _UsageDrum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 4)
)
_UsageDrumTable_Object = MibTable
usageDrumTable = _UsageDrumTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 4, 1)
)
if mibBuilder.loadTexts:
    usageDrumTable.setStatus("optional")
_UsageDrumEntry_Object = MibTableRow
usageDrumEntry = _UsageDrumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 4, 1, 1)
)
usageDrumEntry.setIndexNames(
    (0, "OKIDATA-MIB", "usageDrumIndex"),
)
if mibBuilder.loadTexts:
    usageDrumEntry.setStatus("optional")
_UsageDrumIndex_Type = Integer32
_UsageDrumIndex_Object = MibTableColumn
usageDrumIndex = _UsageDrumIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 4, 1, 1, 1),
    _UsageDrumIndex_Type()
)
usageDrumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageDrumIndex.setStatus("optional")
_UsageDrumCurrentLevel_Type = DisplayString
_UsageDrumCurrentLevel_Object = MibTableColumn
usageDrumCurrentLevel = _UsageDrumCurrentLevel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 4, 1, 1, 3),
    _UsageDrumCurrentLevel_Type()
)
usageDrumCurrentLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageDrumCurrentLevel.setStatus("optional")
_UsageDrumMaxLevel_Type = DisplayString
_UsageDrumMaxLevel_Object = MibTableColumn
usageDrumMaxLevel = _UsageDrumMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 4, 1, 1, 4),
    _UsageDrumMaxLevel_Type()
)
usageDrumMaxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageDrumMaxLevel.setStatus("optional")
_UsageBelt_ObjectIdentity = ObjectIdentity
usageBelt = _UsageBelt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 5)
)
_UsageBeltTable_Object = MibTable
usageBeltTable = _UsageBeltTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 5, 1)
)
if mibBuilder.loadTexts:
    usageBeltTable.setStatus("optional")
_UsageBeltEntry_Object = MibTableRow
usageBeltEntry = _UsageBeltEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 5, 1, 1)
)
usageBeltEntry.setIndexNames(
    (0, "OKIDATA-MIB", "usageBeltIndex"),
)
if mibBuilder.loadTexts:
    usageBeltEntry.setStatus("optional")
_UsageBeltIndex_Type = Integer32
_UsageBeltIndex_Object = MibTableColumn
usageBeltIndex = _UsageBeltIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 5, 1, 1, 1),
    _UsageBeltIndex_Type()
)
usageBeltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageBeltIndex.setStatus("optional")
_UsageBeltCurrentLevel_Type = DisplayString
_UsageBeltCurrentLevel_Object = MibTableColumn
usageBeltCurrentLevel = _UsageBeltCurrentLevel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 5, 1, 1, 3),
    _UsageBeltCurrentLevel_Type()
)
usageBeltCurrentLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageBeltCurrentLevel.setStatus("optional")
_UsageBeltMaxLevel_Type = DisplayString
_UsageBeltMaxLevel_Object = MibTableColumn
usageBeltMaxLevel = _UsageBeltMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 5, 1, 1, 4),
    _UsageBeltMaxLevel_Type()
)
usageBeltMaxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageBeltMaxLevel.setStatus("optional")
_UsageFuser_ObjectIdentity = ObjectIdentity
usageFuser = _UsageFuser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 6)
)
_UsageFuserTable_Object = MibTable
usageFuserTable = _UsageFuserTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 6, 1)
)
if mibBuilder.loadTexts:
    usageFuserTable.setStatus("optional")
_UsageFuserEntry_Object = MibTableRow
usageFuserEntry = _UsageFuserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 6, 1, 1)
)
usageFuserEntry.setIndexNames(
    (0, "OKIDATA-MIB", "usageFuserIndex"),
)
if mibBuilder.loadTexts:
    usageFuserEntry.setStatus("optional")
_UsageFuserIndex_Type = Integer32
_UsageFuserIndex_Object = MibTableColumn
usageFuserIndex = _UsageFuserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 6, 1, 1, 1),
    _UsageFuserIndex_Type()
)
usageFuserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageFuserIndex.setStatus("optional")
_UsageFuserCurrentLevel_Type = DisplayString
_UsageFuserCurrentLevel_Object = MibTableColumn
usageFuserCurrentLevel = _UsageFuserCurrentLevel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 6, 1, 1, 3),
    _UsageFuserCurrentLevel_Type()
)
usageFuserCurrentLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageFuserCurrentLevel.setStatus("optional")
_UsageFuserMaxLevel_Type = DisplayString
_UsageFuserMaxLevel_Object = MibTableColumn
usageFuserMaxLevel = _UsageFuserMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 6, 1, 1, 4),
    _UsageFuserMaxLevel_Type()
)
usageFuserMaxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageFuserMaxLevel.setStatus("optional")
_UsageOil_ObjectIdentity = ObjectIdentity
usageOil = _UsageOil_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 7)
)
_UsageWasteToner_ObjectIdentity = ObjectIdentity
usageWasteToner = _UsageWasteToner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 1, 100, 8)
)
_Niptype2_ObjectIdentity = ObjectIdentity
niptype2 = _Niptype2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 1, 2)
)
_Inkjet_ObjectIdentity = ObjectIdentity
inkjet = _Inkjet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 2)
)
_Fax_ObjectIdentity = ObjectIdentity
fax = _Fax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 3)
)
_Mfp_ObjectIdentity = ObjectIdentity
mfp = _Mfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 4)
)
_Sidm_ObjectIdentity = ObjectIdentity
sidm = _Sidm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 1, 5)
)
_Printserver_ObjectIdentity = ObjectIdentity
printserver = _Printserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2)
)
_PsVendor_ObjectIdentity = ObjectIdentity
psVendor = _PsVendor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 100)
)
_PsVendorId_Type = ObjectIdentifier
_PsVendorId_Object = MibScalar
psVendorId = _PsVendorId_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 100, 1),
    _PsVendorId_Type()
)
psVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psVendorId.setStatus("mandatory")


class _PsMibVersion_Type(DisplayString):
    """Custom type psMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_PsMibVersion_Type.__name__ = "DisplayString"
_PsMibVersion_Object = MibScalar
psMibVersion = _PsMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 100, 3),
    _PsMibVersion_Type()
)
psMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psMibVersion.setStatus("mandatory")
_Okips_ObjectIdentity = ObjectIdentity
okips = _Okips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1)
)
_GenGroupVersion_Type = Integer32
_GenGroupVersion_Object = MibScalar
genGroupVersion = _GenGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 1),
    _GenGroupVersion_Type()
)
genGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupVersion.setStatus("mandatory")
_GenMIBVersion_Type = Integer32
_GenMIBVersion_Object = MibScalar
genMIBVersion = _GenMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 2),
    _GenMIBVersion_Type()
)
genMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMIBVersion.setStatus("mandatory")


class _GenProductName_Type(DisplayString):
    """Custom type genProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_GenProductName_Type.__name__ = "DisplayString"
_GenProductName_Object = MibScalar
genProductName = _GenProductName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 3),
    _GenProductName_Type()
)
genProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProductName.setStatus("mandatory")


class _GenProductNumber_Type(DisplayString):
    """Custom type genProductNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_GenProductNumber_Type.__name__ = "DisplayString"
_GenProductNumber_Object = MibScalar
genProductNumber = _GenProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 4),
    _GenProductNumber_Type()
)
genProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProductNumber.setStatus("mandatory")


class _GenSerialNumber_Type(DisplayString):
    """Custom type genSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_GenSerialNumber_Type.__name__ = "DisplayString"
_GenSerialNumber_Object = MibScalar
genSerialNumber = _GenSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 5),
    _GenSerialNumber_Type()
)
genSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSerialNumber.setStatus("mandatory")


class _GenHWAddress_Type(OctetString):
    """Custom type genHWAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GenHWAddress_Type.__name__ = "OctetString"
_GenHWAddress_Object = MibScalar
genHWAddress = _GenHWAddress_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 6),
    _GenHWAddress_Type()
)
genHWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHWAddress.setStatus("mandatory")


class _GenCableType_Type(Integer32):
    """Custom type genCableType based on Integer32"""
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
        *(("aui", 3),
          ("fiber100fx", 6),
          ("stp", 5),
          ("tenbase2", 1),
          ("tenbaseT", 2),
          ("utp", 4))
    )


_GenCableType_Type.__name__ = "Integer32"
_GenCableType_Object = MibScalar
genCableType = _GenCableType_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 7),
    _GenCableType_Type()
)
genCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCableType.setStatus("mandatory")


class _GenDateCode_Type(DisplayString):
    """Custom type genDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GenDateCode_Type.__name__ = "DisplayString"
_GenDateCode_Object = MibScalar
genDateCode = _GenDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 8),
    _GenDateCode_Type()
)
genDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDateCode.setStatus("mandatory")


class _GenVersion_Type(DisplayString):
    """Custom type genVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GenVersion_Type.__name__ = "DisplayString"
_GenVersion_Object = MibScalar
genVersion = _GenVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 9),
    _GenVersion_Type()
)
genVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVersion.setStatus("mandatory")


class _GenConfigurationDirty_Type(Integer32):
    """Custom type genConfigurationDirty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_GenConfigurationDirty_Type.__name__ = "Integer32"
_GenConfigurationDirty_Object = MibScalar
genConfigurationDirty = _GenConfigurationDirty_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 10),
    _GenConfigurationDirty_Type()
)
genConfigurationDirty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genConfigurationDirty.setStatus("mandatory")


class _GenCompanyName_Type(DisplayString):
    """Custom type genCompanyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GenCompanyName_Type.__name__ = "DisplayString"
_GenCompanyName_Object = MibScalar
genCompanyName = _GenCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 11),
    _GenCompanyName_Type()
)
genCompanyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCompanyName.setStatus("mandatory")


class _GenCompanyLoc_Type(DisplayString):
    """Custom type genCompanyLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_GenCompanyLoc_Type.__name__ = "DisplayString"
_GenCompanyLoc_Object = MibScalar
genCompanyLoc = _GenCompanyLoc_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 12),
    _GenCompanyLoc_Type()
)
genCompanyLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCompanyLoc.setStatus("mandatory")


class _GenCompanyPhone_Type(DisplayString):
    """Custom type genCompanyPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GenCompanyPhone_Type.__name__ = "DisplayString"
_GenCompanyPhone_Object = MibScalar
genCompanyPhone = _GenCompanyPhone_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 13),
    _GenCompanyPhone_Type()
)
genCompanyPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCompanyPhone.setStatus("mandatory")


class _GenCompanyTechSupport_Type(DisplayString):
    """Custom type genCompanyTechSupport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenCompanyTechSupport_Type.__name__ = "DisplayString"
_GenCompanyTechSupport_Object = MibScalar
genCompanyTechSupport = _GenCompanyTechSupport_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 14),
    _GenCompanyTechSupport_Type()
)
genCompanyTechSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCompanyTechSupport.setStatus("mandatory")
_GenProtocols_ObjectIdentity = ObjectIdentity
genProtocols = _GenProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 15)
)
_GenNumProtocols_Type = Integer32
_GenNumProtocols_Object = MibScalar
genNumProtocols = _GenNumProtocols_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 15, 1),
    _GenNumProtocols_Type()
)
genNumProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genNumProtocols.setStatus("mandatory")
_GenProtocolTable_Object = MibTable
genProtocolTable = _GenProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 15, 2)
)
if mibBuilder.loadTexts:
    genProtocolTable.setStatus("mandatory")
_GenProtocolEntry_Object = MibTableRow
genProtocolEntry = _GenProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 15, 2, 1)
)
genProtocolEntry.setIndexNames(
    (0, "OKIDATA-MIB", "genProtocolIndex"),
)
if mibBuilder.loadTexts:
    genProtocolEntry.setStatus("mandatory")
_GenProtocolIndex_Type = Integer32
_GenProtocolIndex_Object = MibTableColumn
genProtocolIndex = _GenProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 15, 2, 1, 1),
    _GenProtocolIndex_Type()
)
genProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProtocolIndex.setStatus("mandatory")


class _GenProtocolDescr_Type(DisplayString):
    """Custom type genProtocolDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenProtocolDescr_Type.__name__ = "DisplayString"
_GenProtocolDescr_Object = MibTableColumn
genProtocolDescr = _GenProtocolDescr_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 15, 2, 1, 2),
    _GenProtocolDescr_Type()
)
genProtocolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProtocolDescr.setStatus("mandatory")


class _GenProtocolID_Type(Integer32):
    """Custom type genProtocolID based on Integer32"""
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
        *(("ethertalk", 5),
          ("lanmanger", 4),
          ("netware", 2),
          ("tcp-ip", 1),
          ("vines", 3))
    )


_GenProtocolID_Type.__name__ = "Integer32"
_GenProtocolID_Object = MibTableColumn
genProtocolID = _GenProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 15, 2, 1, 3),
    _GenProtocolID_Type()
)
genProtocolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProtocolID.setStatus("mandatory")


class _GenSysUpTimeString_Type(DisplayString):
    """Custom type genSysUpTimeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_GenSysUpTimeString_Type.__name__ = "DisplayString"
_GenSysUpTimeString_Object = MibScalar
genSysUpTimeString = _GenSysUpTimeString_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 1, 16),
    _GenSysUpTimeString_Type()
)
genSysUpTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSysUpTimeString.setStatus("mandatory")
_Commands_ObjectIdentity = ObjectIdentity
commands = _Commands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 2)
)
_CmdGroupVersion_Type = Integer32
_CmdGroupVersion_Object = MibScalar
cmdGroupVersion = _CmdGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 2, 1),
    _CmdGroupVersion_Type()
)
cmdGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdGroupVersion.setStatus("mandatory")


class _CmdReset_Type(Integer32):
    """Custom type cmdReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmdReset_Type.__name__ = "Integer32"
_CmdReset_Object = MibScalar
cmdReset = _CmdReset_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 2, 2),
    _CmdReset_Type()
)
cmdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdReset.setStatus("optional")


class _CmdPrintConfig_Type(Integer32):
    """Custom type cmdPrintConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmdPrintConfig_Type.__name__ = "Integer32"
_CmdPrintConfig_Object = MibScalar
cmdPrintConfig = _CmdPrintConfig_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 2, 3),
    _CmdPrintConfig_Type()
)
cmdPrintConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdPrintConfig.setStatus("optional")


class _CmdRestoreDefaults_Type(Integer32):
    """Custom type cmdRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmdRestoreDefaults_Type.__name__ = "Integer32"
_CmdRestoreDefaults_Object = MibScalar
cmdRestoreDefaults = _CmdRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 2, 4),
    _CmdRestoreDefaults_Type()
)
cmdRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdRestoreDefaults.setStatus("optional")
_OkipsSNMP_ObjectIdentity = ObjectIdentity
okipsSNMP = _OkipsSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3)
)
_SnmpGroupVersion_Type = Integer32
_SnmpGroupVersion_Object = MibScalar
snmpGroupVersion = _SnmpGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 1),
    _SnmpGroupVersion_Type()
)
snmpGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGroupVersion.setStatus("mandatory")
_OkipsSNMPCommands_ObjectIdentity = ObjectIdentity
okipsSNMPCommands = _OkipsSNMPCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 2)
)


class _SnmpRestoreDefaults_Type(Integer32):
    """Custom type snmpRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SnmpRestoreDefaults_Type.__name__ = "Integer32"
_SnmpRestoreDefaults_Object = MibScalar
snmpRestoreDefaults = _SnmpRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 2, 1),
    _SnmpRestoreDefaults_Type()
)
snmpRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpRestoreDefaults.setStatus("optional")


class _SnmpGetCommunityName_Type(DisplayString):
    """Custom type snmpGetCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SnmpGetCommunityName_Type.__name__ = "DisplayString"
_SnmpGetCommunityName_Object = MibScalar
snmpGetCommunityName = _SnmpGetCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 3),
    _SnmpGetCommunityName_Type()
)
snmpGetCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGetCommunityName.setStatus("optional")


class _SnmpSetCommunityName_Type(DisplayString):
    """Custom type snmpSetCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SnmpSetCommunityName_Type.__name__ = "DisplayString"
_SnmpSetCommunityName_Object = MibScalar
snmpSetCommunityName = _SnmpSetCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 4),
    _SnmpSetCommunityName_Type()
)
snmpSetCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSetCommunityName.setStatus("optional")


class _SnmpTrapCommunityName_Type(DisplayString):
    """Custom type snmpTrapCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SnmpTrapCommunityName_Type.__name__ = "DisplayString"
_SnmpTrapCommunityName_Object = MibScalar
snmpTrapCommunityName = _SnmpTrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 5),
    _SnmpTrapCommunityName_Type()
)
snmpTrapCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunityName.setStatus("optional")
_OkipsSNMPTrapMasks_ObjectIdentity = ObjectIdentity
okipsSNMPTrapMasks = _OkipsSNMPTrapMasks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 6)
)
_SnmpPrinterTrapMaskUsed_Type = Integer32
_SnmpPrinterTrapMaskUsed_Object = MibScalar
snmpPrinterTrapMaskUsed = _SnmpPrinterTrapMaskUsed_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 6, 1),
    _SnmpPrinterTrapMaskUsed_Type()
)
snmpPrinterTrapMaskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPrinterTrapMaskUsed.setStatus("optional")
_SnmpPrinter2TrapMaskUsed_Type = Integer32
_SnmpPrinter2TrapMaskUsed_Object = MibScalar
snmpPrinter2TrapMaskUsed = _SnmpPrinter2TrapMaskUsed_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 6, 2),
    _SnmpPrinter2TrapMaskUsed_Type()
)
snmpPrinter2TrapMaskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPrinter2TrapMaskUsed.setStatus("optional")
_SnmpTrapMaskTable_Object = MibTable
snmpTrapMaskTable = _SnmpTrapMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 6, 3)
)
if mibBuilder.loadTexts:
    snmpTrapMaskTable.setStatus("mandatory")
_SnmpTrapEntry_Object = MibTableRow
snmpTrapEntry = _SnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 6, 3, 1)
)
snmpTrapEntry.setIndexNames(
    (0, "OKIDATA-MIB", "SNMPTrapMaskIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapEntry.setStatus("mandatory")
_SnmpTrapMaskIndex_Type = Integer32
_SnmpTrapMaskIndex_Object = MibTableColumn
snmpTrapMaskIndex = _SnmpTrapMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 6, 3, 1, 1),
    _SnmpTrapMaskIndex_Type()
)
snmpTrapMaskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapMaskIndex.setStatus("mandatory")


class _SnmpTrapMaskString_Type(OctetString):
    """Custom type snmpTrapMaskString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_SnmpTrapMaskString_Type.__name__ = "OctetString"
_SnmpTrapMaskString_Object = MibTableColumn
snmpTrapMaskString = _SnmpTrapMaskString_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 3, 6, 3, 1, 2),
    _SnmpTrapMaskString_Type()
)
snmpTrapMaskString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapMaskString.setStatus("optional")
_Driver_ObjectIdentity = ObjectIdentity
driver = _Driver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 4)
)
_DriverGroupVersion_Type = Integer32
_DriverGroupVersion_Object = MibScalar
driverGroupVersion = _DriverGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 4, 1),
    _DriverGroupVersion_Type()
)
driverGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverGroupVersion.setStatus("mandatory")
_DriverRXPackets_Type = Counter32
_DriverRXPackets_Object = MibScalar
driverRXPackets = _DriverRXPackets_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 4, 2),
    _DriverRXPackets_Type()
)
driverRXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverRXPackets.setStatus("mandatory")
_DriverTXPackets_Type = Counter32
_DriverTXPackets_Object = MibScalar
driverTXPackets = _DriverTXPackets_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 4, 3),
    _DriverTXPackets_Type()
)
driverTXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverTXPackets.setStatus("mandatory")
_DriverRXPacketsUnavailable_Type = Counter32
_DriverRXPacketsUnavailable_Object = MibScalar
driverRXPacketsUnavailable = _DriverRXPacketsUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 4, 4),
    _DriverRXPacketsUnavailable_Type()
)
driverRXPacketsUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverRXPacketsUnavailable.setStatus("mandatory")
_DriverRXPacketErrors_Type = Counter32
_DriverRXPacketErrors_Object = MibScalar
driverRXPacketErrors = _DriverRXPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 4, 5),
    _DriverRXPacketErrors_Type()
)
driverRXPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverRXPacketErrors.setStatus("mandatory")
_DriverTXPacketErrors_Type = Counter32
_DriverTXPacketErrors_Object = MibScalar
driverTXPacketErrors = _DriverTXPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 4, 6),
    _DriverTXPacketErrors_Type()
)
driverTXPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverTXPacketErrors.setStatus("mandatory")
_DriverTXPacketRetries_Type = Counter32
_DriverTXPacketRetries_Object = MibScalar
driverTXPacketRetries = _DriverTXPacketRetries_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 4, 7),
    _DriverTXPacketRetries_Type()
)
driverTXPacketRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverTXPacketRetries.setStatus("mandatory")
_DriverChecksumErrors_Type = Counter32
_DriverChecksumErrors_Object = MibScalar
driverChecksumErrors = _DriverChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 4, 8),
    _DriverChecksumErrors_Type()
)
driverChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverChecksumErrors.setStatus("mandatory")
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 5)
)
_TrGroupVersion_Type = Integer32
_TrGroupVersion_Object = MibScalar
trGroupVersion = _TrGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 5, 1),
    _TrGroupVersion_Type()
)
trGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trGroupVersion.setStatus("mandatory")
_TrCommands_ObjectIdentity = ObjectIdentity
trCommands = _TrCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 5, 2)
)


class _TrRestoreDefaults_Type(Integer32):
    """Custom type trRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrRestoreDefaults_Type.__name__ = "Integer32"
_TrRestoreDefaults_Object = MibScalar
trRestoreDefaults = _TrRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 5, 2, 1),
    _TrRestoreDefaults_Type()
)
trRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trRestoreDefaults.setStatus("optional")
_TrConfigure_ObjectIdentity = ObjectIdentity
trConfigure = _TrConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 5, 3)
)


class _TrPriority_Type(Integer32):
    """Custom type trPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_TrPriority_Type.__name__ = "Integer32"
_TrPriority_Object = MibScalar
trPriority = _TrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 5, 3, 1),
    _TrPriority_Type()
)
trPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trPriority.setStatus("optional")


class _TrEarlyTokenRelease_Type(Integer32):
    """Custom type trEarlyTokenRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrEarlyTokenRelease_Type.__name__ = "Integer32"
_TrEarlyTokenRelease_Object = MibScalar
trEarlyTokenRelease = _TrEarlyTokenRelease_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 5, 3, 2),
    _TrEarlyTokenRelease_Type()
)
trEarlyTokenRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trEarlyTokenRelease.setStatus("optional")


class _TrPacketSize_Type(Integer32):
    """Custom type trPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("four-k", 3),
          ("one-k", 1),
          ("two-k", 2))
    )


_TrPacketSize_Type.__name__ = "Integer32"
_TrPacketSize_Object = MibScalar
trPacketSize = _TrPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 5, 3, 3),
    _TrPacketSize_Type()
)
trPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trPacketSize.setStatus("optional")


class _TrRouting_Type(Integer32):
    """Custom type trRouting based on Integer32"""
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
        *(("all-None", 2),
          ("off", 1),
          ("single-All", 3),
          ("single-None", 4))
    )


_TrRouting_Type.__name__ = "Integer32"
_TrRouting_Object = MibScalar
trRouting = _TrRouting_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 5, 3, 4),
    _TrRouting_Type()
)
trRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trRouting.setStatus("optional")


class _TrLocallyAdminAddr_Type(OctetString):
    """Custom type trLocallyAdminAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TrLocallyAdminAddr_Type.__name__ = "OctetString"
_TrLocallyAdminAddr_Object = MibScalar
trLocallyAdminAddr = _TrLocallyAdminAddr_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 5, 3, 5),
    _TrLocallyAdminAddr_Type()
)
trLocallyAdminAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trLocallyAdminAddr.setStatus("optional")
_PrintServers_ObjectIdentity = ObjectIdentity
printServers = _PrintServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6)
)
_PsGeneral_ObjectIdentity = ObjectIdentity
psGeneral = _PsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 1)
)
_PsGroupVersion_Type = Integer32
_PsGroupVersion_Object = MibScalar
psGroupVersion = _PsGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 1, 1),
    _PsGroupVersion_Type()
)
psGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psGroupVersion.setStatus("mandatory")


class _PsJetAdminEnabled_Type(Integer32):
    """Custom type psJetAdminEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PsJetAdminEnabled_Type.__name__ = "Integer32"
_PsJetAdminEnabled_Object = MibScalar
psJetAdminEnabled = _PsJetAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 1, 2),
    _PsJetAdminEnabled_Type()
)
psJetAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psJetAdminEnabled.setStatus("mandatory")


class _PsVerifyConfiguration_Type(Integer32):
    """Custom type psVerifyConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("getvalue", 0),
          ("serial-configuration", 1))
    )


_PsVerifyConfiguration_Type.__name__ = "Integer32"
_PsVerifyConfiguration_Object = MibScalar
psVerifyConfiguration = _PsVerifyConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 1, 3),
    _PsVerifyConfiguration_Type()
)
psVerifyConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psVerifyConfiguration.setStatus("optional")
_PsOutput_ObjectIdentity = ObjectIdentity
psOutput = _PsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2)
)
_OutputGroupVersion_Type = Integer32
_OutputGroupVersion_Object = MibScalar
outputGroupVersion = _OutputGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 1),
    _OutputGroupVersion_Type()
)
outputGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputGroupVersion.setStatus("mandatory")
_OutputCommands_ObjectIdentity = ObjectIdentity
outputCommands = _OutputCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 2)
)


class _OutputRestoreDefaults_Type(Integer32):
    """Custom type outputRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_OutputRestoreDefaults_Type.__name__ = "Integer32"
_OutputRestoreDefaults_Object = MibScalar
outputRestoreDefaults = _OutputRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 2, 1),
    _OutputRestoreDefaults_Type()
)
outputRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputRestoreDefaults.setStatus("mandatory")
_OutputCommandsTable_Object = MibTable
outputCommandsTable = _OutputCommandsTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    outputCommandsTable.setStatus("mandatory")
_OutputCommandsEntry_Object = MibTableRow
outputCommandsEntry = _OutputCommandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 2, 2, 1)
)
outputCommandsEntry.setIndexNames(
    (0, "OKIDATA-MIB", "outputIndex"),
)
if mibBuilder.loadTexts:
    outputCommandsEntry.setStatus("mandatory")


class _OutputCancelCurrentJob_Type(Integer32):
    """Custom type outputCancelCurrentJob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_OutputCancelCurrentJob_Type.__name__ = "Integer32"
_OutputCancelCurrentJob_Object = MibTableColumn
outputCancelCurrentJob = _OutputCancelCurrentJob_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 2, 2, 1, 1),
    _OutputCancelCurrentJob_Type()
)
outputCancelCurrentJob.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputCancelCurrentJob.setStatus("optional")
_OutputConfigure_ObjectIdentity = ObjectIdentity
outputConfigure = _OutputConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3)
)
_OutputNumPorts_Type = Integer32
_OutputNumPorts_Object = MibScalar
outputNumPorts = _OutputNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 1),
    _OutputNumPorts_Type()
)
outputNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputNumPorts.setStatus("mandatory")
_OutputTable_Object = MibTable
outputTable = _OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2)
)
if mibBuilder.loadTexts:
    outputTable.setStatus("mandatory")
_OutputEntry_Object = MibTableRow
outputEntry = _OutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1)
)
outputEntry.setIndexNames(
    (0, "OKIDATA-MIB", "outputIndex"),
)
if mibBuilder.loadTexts:
    outputEntry.setStatus("mandatory")
_OutputIndex_Type = Integer32
_OutputIndex_Object = MibTableColumn
outputIndex = _OutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 1),
    _OutputIndex_Type()
)
outputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputIndex.setStatus("mandatory")


class _OutputName_Type(DisplayString):
    """Custom type outputName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OutputName_Type.__name__ = "DisplayString"
_OutputName_Object = MibTableColumn
outputName = _OutputName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 2),
    _OutputName_Type()
)
outputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputName.setStatus("mandatory")


class _OutputStatusString_Type(DisplayString):
    """Custom type outputStatusString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_OutputStatusString_Type.__name__ = "DisplayString"
_OutputStatusString_Object = MibTableColumn
outputStatusString = _OutputStatusString_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 3),
    _OutputStatusString_Type()
)
outputStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputStatusString.setStatus("mandatory")


class _OutputStatus_Type(Integer32):
    """Custom type outputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-Line", 2),
          ("on-Line", 1))
    )


_OutputStatus_Type.__name__ = "Integer32"
_OutputStatus_Object = MibTableColumn
outputStatus = _OutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 4),
    _OutputStatus_Type()
)
outputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputStatus.setStatus("mandatory")


class _OutputExtendedStatus_Type(Integer32):
    """Custom type outputExtendedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              15)
        )
    )
    namedValues = NamedValues(
        *(("door-Open", 6),
          ("no-Printer-Attached", 2),
          ("none", 1),
          ("paper-Jam", 5),
          ("paper-Out", 4),
          ("printer-Error", 15),
          ("toner-Low", 3))
    )


_OutputExtendedStatus_Type.__name__ = "Integer32"
_OutputExtendedStatus_Object = MibTableColumn
outputExtendedStatus = _OutputExtendedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 5),
    _OutputExtendedStatus_Type()
)
outputExtendedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputExtendedStatus.setStatus("mandatory")


class _OutputPrinter_Type(Integer32):
    """Custom type outputPrinter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no-Specific-Printer", 4),
          ("okidata", 2))
    )


_OutputPrinter_Type.__name__ = "Integer32"
_OutputPrinter_Object = MibTableColumn
outputPrinter = _OutputPrinter_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 6),
    _OutputPrinter_Type()
)
outputPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputPrinter.setStatus("optional")


class _OutputLanguageSwitching_Type(Integer32):
    """Custom type outputLanguageSwitching based on Integer32"""
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
        *(("als", 4),
          ("off", 1),
          ("pcl", 2),
          ("postScript", 3))
    )


_OutputLanguageSwitching_Type.__name__ = "Integer32"
_OutputLanguageSwitching_Object = MibTableColumn
outputLanguageSwitching = _OutputLanguageSwitching_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 7),
    _OutputLanguageSwitching_Type()
)
outputLanguageSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputLanguageSwitching.setStatus("optional")


class _OutputConfigLanguage_Type(Integer32):
    """Custom type outputConfigLanguage based on Integer32"""
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
        *(("off", 4),
          ("pcl", 2),
          ("postScript", 3),
          ("text", 1))
    )


_OutputConfigLanguage_Type.__name__ = "Integer32"
_OutputConfigLanguage_Object = MibTableColumn
outputConfigLanguage = _OutputConfigLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 8),
    _OutputConfigLanguage_Type()
)
outputConfigLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigLanguage.setStatus("mandatory")


class _OutputPCLString_Type(OctetString):
    """Custom type outputPCLString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )


_OutputPCLString_Type.__name__ = "OctetString"
_OutputPCLString_Object = MibTableColumn
outputPCLString = _OutputPCLString_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 9),
    _OutputPCLString_Type()
)
outputPCLString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputPCLString.setStatus("optional")


class _OutputPSString_Type(OctetString):
    """Custom type outputPSString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )


_OutputPSString_Type.__name__ = "OctetString"
_OutputPSString_Object = MibTableColumn
outputPSString = _OutputPSString_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 10),
    _OutputPSString_Type()
)
outputPSString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputPSString.setStatus("optional")


class _OutputSetting_Type(Integer32):
    """Custom type outputSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32758,
              32759,
              32760,
              32761,
              32762,
              32763,
              32764,
              32765,
              32766,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("extendedLink", 32767),
          ("ieee-1284-ecp-or-fast-nibble-mode", 32766),
          ("ieee-1284-std-nibble-mode", 32763),
          ("internal", 32765),
          ("parallel-compatibility-no-bidi", 32762),
          ("serial-bidirectional", 32759),
          ("serial-infrared", 32758),
          ("serial-input", 32761),
          ("serial-unidirectional", 32760),
          ("z-Link", 32764))
    )


_OutputSetting_Type.__name__ = "Integer32"
_OutputSetting_Object = MibTableColumn
outputSetting = _OutputSetting_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 12),
    _OutputSetting_Type()
)
outputSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputSetting.setStatus("mandatory")


class _OutputOwner_Type(Integer32):
    """Custom type outputOwner based on Integer32"""
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
        *(("config-Page", 7),
          ("etherTalk", 6),
          ("lanManager", 5),
          ("netware", 3),
          ("no-Owner", 1),
          ("tcpip", 2),
          ("vines", 4))
    )


_OutputOwner_Type.__name__ = "Integer32"
_OutputOwner_Object = MibTableColumn
outputOwner = _OutputOwner_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 13),
    _OutputOwner_Type()
)
outputOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputOwner.setStatus("mandatory")


class _OutputBIDIStatusEnabled_Type(Integer32):
    """Custom type outputBIDIStatusEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_OutputBIDIStatusEnabled_Type.__name__ = "Integer32"
_OutputBIDIStatusEnabled_Object = MibTableColumn
outputBIDIStatusEnabled = _OutputBIDIStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 14),
    _OutputBIDIStatusEnabled_Type()
)
outputBIDIStatusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputBIDIStatusEnabled.setStatus("optional")


class _OutputPrinterModel_Type(DisplayString):
    """Custom type outputPrinterModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_OutputPrinterModel_Type.__name__ = "DisplayString"
_OutputPrinterModel_Object = MibTableColumn
outputPrinterModel = _OutputPrinterModel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 15),
    _OutputPrinterModel_Type()
)
outputPrinterModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPrinterModel.setStatus("optional")


class _OutputPrinterDisplay_Type(DisplayString):
    """Custom type outputPrinterDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_OutputPrinterDisplay_Type.__name__ = "DisplayString"
_OutputPrinterDisplay_Object = MibTableColumn
outputPrinterDisplay = _OutputPrinterDisplay_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 16),
    _OutputPrinterDisplay_Type()
)
outputPrinterDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPrinterDisplay.setStatus("optional")


class _OutputCapabilities_Type(Integer32):
    """Custom type outputCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              524288,
              1048576,
              2097152,
              4194304,
              8388608,
              33554432,
              67108864,
              134217728,
              536870912,
              1073741824)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 33554432),
          ("ieee-1284-ecp-or-fast-nibble-mode", 1073741824),
          ("ieee-1284-std-nibble-mode", 8388608),
          ("internal", 536870912),
          ("parallel-compatibility-no-bidi", 4194304),
          ("serial-Output", 134217728),
          ("serial-Software-Handshake", 67108864),
          ("serial-Uni-Baud-115200", 16),
          ("serial-Uni-Baud-19200", 2),
          ("serial-Uni-Baud-38400", 4),
          ("serial-Uni-Baud-57600", 8),
          ("serial-Uni-Baud-9600", 1),
          ("serial-bidi-Baud-19200", 64),
          ("serial-bidi-Baud-38400", 128),
          ("serial-bidi-Baud-57600", 256),
          ("serial-bidi-Baud-9600", 32),
          ("serial-config-settings", 2097152),
          ("serial-in", 1048576),
          ("serial-irin", 524288))
    )


_OutputCapabilities_Type.__name__ = "Integer32"
_OutputCapabilities_Object = MibTableColumn
outputCapabilities = _OutputCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 17),
    _OutputCapabilities_Type()
)
outputCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCapabilities.setStatus("mandatory")


class _OutputHandshake_Type(Integer32):
    """Custom type outputHandshake based on Integer32"""
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
        *(("hardware", 3),
          ("hardware-Software", 2),
          ("not-Supported", 1),
          ("software", 4))
    )


_OutputHandshake_Type.__name__ = "Integer32"
_OutputHandshake_Object = MibTableColumn
outputHandshake = _OutputHandshake_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 18),
    _OutputHandshake_Type()
)
outputHandshake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputHandshake.setStatus("optional")


class _OutputProtocolManager_Type(Integer32):
    """Custom type outputProtocolManager based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protocol-1284-4", 2),
          ("protocol-compatibility", 1),
          ("protocol-none", 0))
    )


_OutputProtocolManager_Type.__name__ = "Integer32"
_OutputProtocolManager_Object = MibTableColumn
outputProtocolManager = _OutputProtocolManager_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 3, 2, 1, 23),
    _OutputProtocolManager_Type()
)
outputProtocolManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputProtocolManager.setStatus("optional")
_OutputDisplayMask_Type = Integer32
_OutputDisplayMask_Object = MibScalar
outputDisplayMask = _OutputDisplayMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 4),
    _OutputDisplayMask_Type()
)
outputDisplayMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputDisplayMask.setStatus("mandatory")
_OutputAvailableTrapsMask_Type = Integer32
_OutputAvailableTrapsMask_Object = MibScalar
outputAvailableTrapsMask = _OutputAvailableTrapsMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 5),
    _OutputAvailableTrapsMask_Type()
)
outputAvailableTrapsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputAvailableTrapsMask.setStatus("mandatory")
_OutputJobLog_ObjectIdentity = ObjectIdentity
outputJobLog = _OutputJobLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 6)
)
_OutputNumLogEntries_Type = Integer32
_OutputNumLogEntries_Object = MibScalar
outputNumLogEntries = _OutputNumLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 6, 1),
    _OutputNumLogEntries_Type()
)
outputNumLogEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputNumLogEntries.setStatus("mandatory")
_OutputJobLogTable_Object = MibTable
outputJobLogTable = _OutputJobLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 6, 2)
)
if mibBuilder.loadTexts:
    outputJobLogTable.setStatus("mandatory")
_OutputJobLogEntry_Object = MibTableRow
outputJobLogEntry = _OutputJobLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 6, 2, 1)
)
outputJobLogEntry.setIndexNames(
    (0, "OKIDATA-MIB", "outputIndex"),
)
if mibBuilder.loadTexts:
    outputJobLogEntry.setStatus("mandatory")


class _OutputJobLogInformation_Type(DisplayString):
    """Custom type outputJobLogInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_OutputJobLogInformation_Type.__name__ = "DisplayString"
_OutputJobLogInformation_Object = MibTableColumn
outputJobLogInformation = _OutputJobLogInformation_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 6, 2, 1, 1),
    _OutputJobLogInformation_Type()
)
outputJobLogInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputJobLogInformation.setStatus("mandatory")


class _OutputJobLogTime_Type(DisplayString):
    """Custom type outputJobLogTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_OutputJobLogTime_Type.__name__ = "DisplayString"
_OutputJobLogTime_Object = MibTableColumn
outputJobLogTime = _OutputJobLogTime_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 6, 2, 1, 2),
    _OutputJobLogTime_Type()
)
outputJobLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputJobLogTime.setStatus("mandatory")
_OutputTotalJobTable_Object = MibTable
outputTotalJobTable = _OutputTotalJobTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 6, 3)
)
if mibBuilder.loadTexts:
    outputTotalJobTable.setStatus("mandatory")
_OutputTotalJobEntry_Object = MibTableRow
outputTotalJobEntry = _OutputTotalJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 6, 3, 1)
)
outputTotalJobEntry.setIndexNames(
    (0, "OKIDATA-MIB", "outputTotalJobIndex"),
)
if mibBuilder.loadTexts:
    outputTotalJobEntry.setStatus("mandatory")
_OutputTotalJobIndex_Type = Integer32
_OutputTotalJobIndex_Object = MibTableColumn
outputTotalJobIndex = _OutputTotalJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 6, 3, 1, 1),
    _OutputTotalJobIndex_Type()
)
outputTotalJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTotalJobIndex.setStatus("mandatory")
_OutputTotalJobsLogged_Type = Integer32
_OutputTotalJobsLogged_Object = MibTableColumn
outputTotalJobsLogged = _OutputTotalJobsLogged_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 2, 6, 3, 1, 2),
    _OutputTotalJobsLogged_Type()
)
outputTotalJobsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTotalJobsLogged.setStatus("mandatory")
_PsProtocols_ObjectIdentity = ObjectIdentity
psProtocols = _PsProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3)
)
_Tcpip_ObjectIdentity = ObjectIdentity
tcpip = _Tcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1)
)
_TcpipGroupVersion_Type = Integer32
_TcpipGroupVersion_Object = MibScalar
tcpipGroupVersion = _TcpipGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 1),
    _TcpipGroupVersion_Type()
)
tcpipGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipGroupVersion.setStatus("mandatory")


class _TcpipEnabled_Type(Integer32):
    """Custom type tcpipEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipEnabled_Type.__name__ = "Integer32"
_TcpipEnabled_Object = MibScalar
tcpipEnabled = _TcpipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 2),
    _TcpipEnabled_Type()
)
tcpipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipEnabled.setStatus("optional")
_TcpipCommands_ObjectIdentity = ObjectIdentity
tcpipCommands = _TcpipCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 3)
)


class _TcpipRestoreDefaults_Type(Integer32):
    """Custom type tcpipRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipRestoreDefaults_Type.__name__ = "Integer32"
_TcpipRestoreDefaults_Object = MibScalar
tcpipRestoreDefaults = _TcpipRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 3, 1),
    _TcpipRestoreDefaults_Type()
)
tcpipRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipRestoreDefaults.setStatus("optional")


class _TcpipFirmwareUpgrade_Type(Integer32):
    """Custom type tcpipFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipFirmwareUpgrade_Type.__name__ = "Integer32"
_TcpipFirmwareUpgrade_Object = MibScalar
tcpipFirmwareUpgrade = _TcpipFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 3, 2),
    _TcpipFirmwareUpgrade_Type()
)
tcpipFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipFirmwareUpgrade.setStatus("optional")
_TcpipConfigure_ObjectIdentity = ObjectIdentity
tcpipConfigure = _TcpipConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4)
)
_TcpipIPAddress_Type = IpAddress
_TcpipIPAddress_Object = MibScalar
tcpipIPAddress = _TcpipIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 1),
    _TcpipIPAddress_Type()
)
tcpipIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipIPAddress.setStatus("optional")
_TcpipDefaultGateway_Type = IpAddress
_TcpipDefaultGateway_Object = MibScalar
tcpipDefaultGateway = _TcpipDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 2),
    _TcpipDefaultGateway_Type()
)
tcpipDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipDefaultGateway.setStatus("optional")
_TcpipSubnetMask_Type = IpAddress
_TcpipSubnetMask_Object = MibScalar
tcpipSubnetMask = _TcpipSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 3),
    _TcpipSubnetMask_Type()
)
tcpipSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSubnetMask.setStatus("optional")


class _TcpipUsingNetProtocols_Type(Integer32):
    """Custom type tcpipUsingNetProtocols based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipUsingNetProtocols_Type.__name__ = "Integer32"
_TcpipUsingNetProtocols_Object = MibScalar
tcpipUsingNetProtocols = _TcpipUsingNetProtocols_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 4),
    _TcpipUsingNetProtocols_Type()
)
tcpipUsingNetProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipUsingNetProtocols.setStatus("optional")
_TcpipBootProtocolsEnabled_Type = Integer32
_TcpipBootProtocolsEnabled_Object = MibScalar
tcpipBootProtocolsEnabled = _TcpipBootProtocolsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 5),
    _TcpipBootProtocolsEnabled_Type()
)
tcpipBootProtocolsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipBootProtocolsEnabled.setStatus("optional")


class _TcpipIPAddressSource_Type(Integer32):
    """Custom type tcpipIPAddressSource based on Integer32"""
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
        *(("bootp", 4),
          ("default", 2),
          ("dhcp", 5),
          ("glean", 6),
          ("permanent", 1),
          ("rarp", 3))
    )


_TcpipIPAddressSource_Type.__name__ = "Integer32"
_TcpipIPAddressSource_Object = MibScalar
tcpipIPAddressSource = _TcpipIPAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 6),
    _TcpipIPAddressSource_Type()
)
tcpipIPAddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipIPAddressSource.setStatus("optional")
_TcpipIPAddressServerAddress_Type = IpAddress
_TcpipIPAddressServerAddress_Object = MibScalar
tcpipIPAddressServerAddress = _TcpipIPAddressServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 7),
    _TcpipIPAddressServerAddress_Type()
)
tcpipIPAddressServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipIPAddressServerAddress.setStatus("optional")


class _TcpipTimeoutChecking_Type(Integer32):
    """Custom type tcpipTimeoutChecking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipTimeoutChecking_Type.__name__ = "Integer32"
_TcpipTimeoutChecking_Object = MibScalar
tcpipTimeoutChecking = _TcpipTimeoutChecking_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 8),
    _TcpipTimeoutChecking_Type()
)
tcpipTimeoutChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipTimeoutChecking.setStatus("optional")
_TcpipNumTraps_Type = Integer32
_TcpipNumTraps_Object = MibScalar
tcpipNumTraps = _TcpipNumTraps_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 9),
    _TcpipNumTraps_Type()
)
tcpipNumTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipNumTraps.setStatus("mandatory")
_TcpipTrapTable_Object = MibTable
tcpipTrapTable = _TcpipTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 10)
)
if mibBuilder.loadTexts:
    tcpipTrapTable.setStatus("mandatory")
_TcpipTrapEntry_Object = MibTableRow
tcpipTrapEntry = _TcpipTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 10, 1)
)
tcpipTrapEntry.setIndexNames(
    (0, "OKIDATA-MIB", "tcpipTrapIndex"),
)
if mibBuilder.loadTexts:
    tcpipTrapEntry.setStatus("mandatory")
_TcpipTrapIndex_Type = Integer32
_TcpipTrapIndex_Object = MibTableColumn
tcpipTrapIndex = _TcpipTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 10, 1, 1),
    _TcpipTrapIndex_Type()
)
tcpipTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipTrapIndex.setStatus("mandatory")
_TcpipTrapDestination_Type = IpAddress
_TcpipTrapDestination_Object = MibTableColumn
tcpipTrapDestination = _TcpipTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 10, 1, 2),
    _TcpipTrapDestination_Type()
)
tcpipTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipTrapDestination.setStatus("optional")
_TcpipPrinter2TrapMask_Type = Integer32
_TcpipPrinter2TrapMask_Object = MibTableColumn
tcpipPrinter2TrapMask = _TcpipPrinter2TrapMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 10, 1, 3),
    _TcpipPrinter2TrapMask_Type()
)
tcpipPrinter2TrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPrinter2TrapMask.setStatus("optional")
_TcpipPrinterTrapMask_Type = Integer32
_TcpipPrinterTrapMask_Object = MibTableColumn
tcpipPrinterTrapMask = _TcpipPrinterTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 10, 1, 4),
    _TcpipPrinterTrapMask_Type()
)
tcpipPrinterTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPrinterTrapMask.setStatus("optional")
_TcpipOutputTrapMask_Type = Integer32
_TcpipOutputTrapMask_Object = MibTableColumn
tcpipOutputTrapMask = _TcpipOutputTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 10, 1, 5),
    _TcpipOutputTrapMask_Type()
)
tcpipOutputTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipOutputTrapMask.setStatus("optional")


class _TcpipBanners_Type(Integer32):
    """Custom type tcpipBanners based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipBanners_Type.__name__ = "Integer32"
_TcpipBanners_Object = MibScalar
tcpipBanners = _TcpipBanners_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 11),
    _TcpipBanners_Type()
)
tcpipBanners.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipBanners.setStatus("optional")
_TcpipWinsAddress_Type = IpAddress
_TcpipWinsAddress_Object = MibScalar
tcpipWinsAddress = _TcpipWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 12),
    _TcpipWinsAddress_Type()
)
tcpipWinsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWinsAddress.setStatus("optional")


class _TcpipWinsAddressSource_Type(Integer32):
    """Custom type tcpipWinsAddressSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("permanent", 2))
    )


_TcpipWinsAddressSource_Type.__name__ = "Integer32"
_TcpipWinsAddressSource_Object = MibScalar
tcpipWinsAddressSource = _TcpipWinsAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 13),
    _TcpipWinsAddressSource_Type()
)
tcpipWinsAddressSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWinsAddressSource.setStatus("optional")


class _TcpipConfigPassword_Type(DisplayString):
    """Custom type tcpipConfigPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 24),
    )


_TcpipConfigPassword_Type.__name__ = "DisplayString"
_TcpipConfigPassword_Object = MibScalar
tcpipConfigPassword = _TcpipConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 14),
    _TcpipConfigPassword_Type()
)
tcpipConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipConfigPassword.setStatus("optional")


class _TcpipTimeoutCheckingValue_Type(Integer32):
    """Custom type tcpipTimeoutCheckingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TcpipTimeoutCheckingValue_Type.__name__ = "Integer32"
_TcpipTimeoutCheckingValue_Object = MibScalar
tcpipTimeoutCheckingValue = _TcpipTimeoutCheckingValue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 15),
    _TcpipTimeoutCheckingValue_Type()
)
tcpipTimeoutCheckingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipTimeoutCheckingValue.setStatus("optional")


class _TcpipArpInterval_Type(Integer32):
    """Custom type tcpipArpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_TcpipArpInterval_Type.__name__ = "Integer32"
_TcpipArpInterval_Object = MibScalar
tcpipArpInterval = _TcpipArpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 16),
    _TcpipArpInterval_Type()
)
tcpipArpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipArpInterval.setStatus("optional")
_TcpipRawPortNumber_Type = Integer32
_TcpipRawPortNumber_Object = MibScalar
tcpipRawPortNumber = _TcpipRawPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 17),
    _TcpipRawPortNumber_Type()
)
tcpipRawPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipRawPortNumber.setStatus("optional")
_TcpipNumSecurity_Type = Integer32
_TcpipNumSecurity_Object = MibScalar
tcpipNumSecurity = _TcpipNumSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 18),
    _TcpipNumSecurity_Type()
)
tcpipNumSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipNumSecurity.setStatus("mandatory")
_TcpipSecurityTable_Object = MibTable
tcpipSecurityTable = _TcpipSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 19)
)
if mibBuilder.loadTexts:
    tcpipSecurityTable.setStatus("mandatory")
_TcpipSecurityEntry_Object = MibTableRow
tcpipSecurityEntry = _TcpipSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 19, 1)
)
tcpipSecurityEntry.setIndexNames(
    (0, "OKIDATA-MIB", "tcpipSecurityIndex"),
)
if mibBuilder.loadTexts:
    tcpipSecurityEntry.setStatus("mandatory")
_TcpipSecurityIndex_Type = Integer32
_TcpipSecurityIndex_Object = MibTableColumn
tcpipSecurityIndex = _TcpipSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 19, 1, 1),
    _TcpipSecurityIndex_Type()
)
tcpipSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipSecurityIndex.setStatus("mandatory")
_TcpipSecureStartIPAddress_Type = IpAddress
_TcpipSecureStartIPAddress_Object = MibTableColumn
tcpipSecureStartIPAddress = _TcpipSecureStartIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 19, 1, 2),
    _TcpipSecureStartIPAddress_Type()
)
tcpipSecureStartIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSecureStartIPAddress.setStatus("optional")
_TcpipSecureEndIPAddress_Type = IpAddress
_TcpipSecureEndIPAddress_Object = MibTableColumn
tcpipSecureEndIPAddress = _TcpipSecureEndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 19, 1, 3),
    _TcpipSecureEndIPAddress_Type()
)
tcpipSecureEndIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSecureEndIPAddress.setStatus("optional")
_TcpipSecurePrinterMask_Type = Integer32
_TcpipSecurePrinterMask_Object = MibTableColumn
tcpipSecurePrinterMask = _TcpipSecurePrinterMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 19, 1, 4),
    _TcpipSecurePrinterMask_Type()
)
tcpipSecurePrinterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSecurePrinterMask.setStatus("optional")


class _TcpipSecureAdminEnabled_Type(Integer32):
    """Custom type tcpipSecureAdminEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipSecureAdminEnabled_Type.__name__ = "Integer32"
_TcpipSecureAdminEnabled_Object = MibTableColumn
tcpipSecureAdminEnabled = _TcpipSecureAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 19, 1, 5),
    _TcpipSecureAdminEnabled_Type()
)
tcpipSecureAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSecureAdminEnabled.setStatus("optional")


class _TcpipLowBandwidth_Type(Integer32):
    """Custom type tcpipLowBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipLowBandwidth_Type.__name__ = "Integer32"
_TcpipLowBandwidth_Object = MibScalar
tcpipLowBandwidth = _TcpipLowBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 20),
    _TcpipLowBandwidth_Type()
)
tcpipLowBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipLowBandwidth.setStatus("optional")
_TcpipNumLogicalPrinters_Type = Integer32
_TcpipNumLogicalPrinters_Object = MibScalar
tcpipNumLogicalPrinters = _TcpipNumLogicalPrinters_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 21),
    _TcpipNumLogicalPrinters_Type()
)
tcpipNumLogicalPrinters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipNumLogicalPrinters.setStatus("mandatory")
_TcpipMLPTable_Object = MibTable
tcpipMLPTable = _TcpipMLPTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 22)
)
if mibBuilder.loadTexts:
    tcpipMLPTable.setStatus("mandatory")
_TcpipMLPEntry_Object = MibTableRow
tcpipMLPEntry = _TcpipMLPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 22, 1)
)
tcpipMLPEntry.setIndexNames(
    (0, "OKIDATA-MIB", "tcpipMLPIndex"),
)
if mibBuilder.loadTexts:
    tcpipMLPEntry.setStatus("mandatory")
_TcpipMLPIndex_Type = Integer32
_TcpipMLPIndex_Object = MibTableColumn
tcpipMLPIndex = _TcpipMLPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 22, 1, 1),
    _TcpipMLPIndex_Type()
)
tcpipMLPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipMLPIndex.setStatus("optional")


class _TcpipMLPName_Type(DisplayString):
    """Custom type tcpipMLPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TcpipMLPName_Type.__name__ = "DisplayString"
_TcpipMLPName_Object = MibTableColumn
tcpipMLPName = _TcpipMLPName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 22, 1, 2),
    _TcpipMLPName_Type()
)
tcpipMLPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPName.setStatus("optional")
_TcpipMLPPort_Type = Integer32
_TcpipMLPPort_Object = MibTableColumn
tcpipMLPPort = _TcpipMLPPort_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 22, 1, 3),
    _TcpipMLPPort_Type()
)
tcpipMLPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPPort.setStatus("optional")
_TcpipMLPTCPPort_Type = Integer32
_TcpipMLPTCPPort_Object = MibTableColumn
tcpipMLPTCPPort = _TcpipMLPTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 22, 1, 4),
    _TcpipMLPTCPPort_Type()
)
tcpipMLPTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPTCPPort.setStatus("optional")


class _TcpipMLPPreString_Type(DisplayString):
    """Custom type tcpipMLPPreString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TcpipMLPPreString_Type.__name__ = "DisplayString"
_TcpipMLPPreString_Object = MibTableColumn
tcpipMLPPreString = _TcpipMLPPreString_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 22, 1, 5),
    _TcpipMLPPreString_Type()
)
tcpipMLPPreString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPPreString.setStatus("optional")


class _TcpipMLPPostString_Type(DisplayString):
    """Custom type tcpipMLPPostString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TcpipMLPPostString_Type.__name__ = "DisplayString"
_TcpipMLPPostString_Object = MibTableColumn
tcpipMLPPostString = _TcpipMLPPostString_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 22, 1, 6),
    _TcpipMLPPostString_Type()
)
tcpipMLPPostString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPPostString.setStatus("optional")
_TcpipMLPDeleteBytes_Type = Integer32
_TcpipMLPDeleteBytes_Object = MibTableColumn
tcpipMLPDeleteBytes = _TcpipMLPDeleteBytes_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 22, 1, 7),
    _TcpipMLPDeleteBytes_Type()
)
tcpipMLPDeleteBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPDeleteBytes.setStatus("optional")
_TcpipSmtpServerAddr_Type = IpAddress
_TcpipSmtpServerAddr_Object = MibScalar
tcpipSmtpServerAddr = _TcpipSmtpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 23),
    _TcpipSmtpServerAddr_Type()
)
tcpipSmtpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSmtpServerAddr.setStatus("optional")
_TcpipNumSmtpDestinations_Type = Integer32
_TcpipNumSmtpDestinations_Object = MibScalar
tcpipNumSmtpDestinations = _TcpipNumSmtpDestinations_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 24),
    _TcpipNumSmtpDestinations_Type()
)
tcpipNumSmtpDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipNumSmtpDestinations.setStatus("mandatory")
_TcpipSmtpTable_Object = MibTable
tcpipSmtpTable = _TcpipSmtpTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 25)
)
if mibBuilder.loadTexts:
    tcpipSmtpTable.setStatus("mandatory")
_TcpipSmtpEntry_Object = MibTableRow
tcpipSmtpEntry = _TcpipSmtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 25, 1)
)
tcpipSmtpEntry.setIndexNames(
    (0, "OKIDATA-MIB", "tcpipSmtpIndex"),
)
if mibBuilder.loadTexts:
    tcpipSmtpEntry.setStatus("mandatory")
_TcpipSmtpIndex_Type = Integer32
_TcpipSmtpIndex_Object = MibTableColumn
tcpipSmtpIndex = _TcpipSmtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 25, 1, 1),
    _TcpipSmtpIndex_Type()
)
tcpipSmtpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipSmtpIndex.setStatus("mandatory")


class _TcpipSmtpEmailAddr_Type(OctetString):
    """Custom type tcpipSmtpEmailAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipSmtpEmailAddr_Type.__name__ = "OctetString"
_TcpipSmtpEmailAddr_Object = MibTableColumn
tcpipSmtpEmailAddr = _TcpipSmtpEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 25, 1, 2),
    _TcpipSmtpEmailAddr_Type()
)
tcpipSmtpEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSmtpEmailAddr.setStatus("optional")
_TcpipSmtpProtocolMask_Type = Integer32
_TcpipSmtpProtocolMask_Object = MibTableColumn
tcpipSmtpProtocolMask = _TcpipSmtpProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 25, 1, 3),
    _TcpipSmtpProtocolMask_Type()
)
tcpipSmtpProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSmtpProtocolMask.setStatus("optional")
_TcpipSmtpPrinterMask_Type = Integer32
_TcpipSmtpPrinterMask_Object = MibTableColumn
tcpipSmtpPrinterMask = _TcpipSmtpPrinterMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 25, 1, 4),
    _TcpipSmtpPrinterMask_Type()
)
tcpipSmtpPrinterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSmtpPrinterMask.setStatus("optional")
_TcpipSmtpOutputMask_Type = Integer32
_TcpipSmtpOutputMask_Object = MibTableColumn
tcpipSmtpOutputMask = _TcpipSmtpOutputMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 25, 1, 5),
    _TcpipSmtpOutputMask_Type()
)
tcpipSmtpOutputMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSmtpOutputMask.setStatus("optional")


class _TcpipWebAdminName_Type(OctetString):
    """Custom type tcpipWebAdminName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_TcpipWebAdminName_Type.__name__ = "OctetString"
_TcpipWebAdminName_Object = MibScalar
tcpipWebAdminName = _TcpipWebAdminName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 26),
    _TcpipWebAdminName_Type()
)
tcpipWebAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebAdminName.setStatus("optional")


class _TcpipWebAdminPassword_Type(OctetString):
    """Custom type tcpipWebAdminPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_TcpipWebAdminPassword_Type.__name__ = "OctetString"
_TcpipWebAdminPassword_Object = MibScalar
tcpipWebAdminPassword = _TcpipWebAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 27),
    _TcpipWebAdminPassword_Type()
)
tcpipWebAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebAdminPassword.setStatus("optional")


class _TcpipWebUserName_Type(OctetString):
    """Custom type tcpipWebUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_TcpipWebUserName_Type.__name__ = "OctetString"
_TcpipWebUserName_Object = MibScalar
tcpipWebUserName = _TcpipWebUserName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 28),
    _TcpipWebUserName_Type()
)
tcpipWebUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebUserName.setStatus("optional")


class _TcpipWebUserPassword_Type(OctetString):
    """Custom type tcpipWebUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_TcpipWebUserPassword_Type.__name__ = "OctetString"
_TcpipWebUserPassword_Object = MibScalar
tcpipWebUserPassword = _TcpipWebUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 29),
    _TcpipWebUserPassword_Type()
)
tcpipWebUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebUserPassword.setStatus("optional")
_TcpipWebHtttpPort_Type = Integer32
_TcpipWebHtttpPort_Object = MibScalar
tcpipWebHtttpPort = _TcpipWebHtttpPort_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 30),
    _TcpipWebHtttpPort_Type()
)
tcpipWebHtttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebHtttpPort.setStatus("optional")


class _TcpipWebFaqURL_Type(OctetString):
    """Custom type tcpipWebFaqURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipWebFaqURL_Type.__name__ = "OctetString"
_TcpipWebFaqURL_Object = MibScalar
tcpipWebFaqURL = _TcpipWebFaqURL_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 31),
    _TcpipWebFaqURL_Type()
)
tcpipWebFaqURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebFaqURL.setStatus("optional")


class _TcpipWebUpdateURL_Type(OctetString):
    """Custom type tcpipWebUpdateURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipWebUpdateURL_Type.__name__ = "OctetString"
_TcpipWebUpdateURL_Object = MibScalar
tcpipWebUpdateURL = _TcpipWebUpdateURL_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 32),
    _TcpipWebUpdateURL_Type()
)
tcpipWebUpdateURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebUpdateURL.setStatus("optional")


class _TcpipWebCustomLinkName_Type(OctetString):
    """Custom type tcpipWebCustomLinkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_TcpipWebCustomLinkName_Type.__name__ = "OctetString"
_TcpipWebCustomLinkName_Object = MibScalar
tcpipWebCustomLinkName = _TcpipWebCustomLinkName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 33),
    _TcpipWebCustomLinkName_Type()
)
tcpipWebCustomLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebCustomLinkName.setStatus("optional")


class _TcpipWebCustomLinkURL_Type(OctetString):
    """Custom type tcpipWebCustomLinkURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipWebCustomLinkURL_Type.__name__ = "OctetString"
_TcpipWebCustomLinkURL_Object = MibScalar
tcpipWebCustomLinkURL = _TcpipWebCustomLinkURL_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 34),
    _TcpipWebCustomLinkURL_Type()
)
tcpipWebCustomLinkURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebCustomLinkURL.setStatus("optional")
_TcpipPOP3ServerAddress_Type = IpAddress
_TcpipPOP3ServerAddress_Object = MibScalar
tcpipPOP3ServerAddress = _TcpipPOP3ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 35),
    _TcpipPOP3ServerAddress_Type()
)
tcpipPOP3ServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPOP3ServerAddress.setStatus("optional")
_TcpipPOP3PollInterval_Type = Integer32
_TcpipPOP3PollInterval_Object = MibScalar
tcpipPOP3PollInterval = _TcpipPOP3PollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 36),
    _TcpipPOP3PollInterval_Type()
)
tcpipPOP3PollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPOP3PollInterval.setStatus("mandatory")


class _TcpipPOP3UserName_Type(OctetString):
    """Custom type tcpipPOP3UserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipPOP3UserName_Type.__name__ = "OctetString"
_TcpipPOP3UserName_Object = MibScalar
tcpipPOP3UserName = _TcpipPOP3UserName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 37),
    _TcpipPOP3UserName_Type()
)
tcpipPOP3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPOP3UserName.setStatus("optional")


class _TcpipPOP3Password_Type(OctetString):
    """Custom type tcpipPOP3Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_TcpipPOP3Password_Type.__name__ = "OctetString"
_TcpipPOP3Password_Object = MibScalar
tcpipPOP3Password = _TcpipPOP3Password_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 38),
    _TcpipPOP3Password_Type()
)
tcpipPOP3Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPOP3Password.setStatus("optional")


class _TcpipDomainName_Type(OctetString):
    """Custom type tcpipDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipDomainName_Type.__name__ = "OctetString"
_TcpipDomainName_Object = MibScalar
tcpipDomainName = _TcpipDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 39),
    _TcpipDomainName_Type()
)
tcpipDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipDomainName.setStatus("optional")
_TcpipCapabilities_Type = Integer32
_TcpipCapabilities_Object = MibScalar
tcpipCapabilities = _TcpipCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 4, 40),
    _TcpipCapabilities_Type()
)
tcpipCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipCapabilities.setStatus("mandatory")
_TcpipStatus_ObjectIdentity = ObjectIdentity
tcpipStatus = _TcpipStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 5)
)


class _TcpipError_Type(DisplayString):
    """Custom type tcpipError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TcpipError_Type.__name__ = "DisplayString"
_TcpipError_Object = MibScalar
tcpipError = _TcpipError_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 5, 1),
    _TcpipError_Type()
)
tcpipError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipError.setStatus("optional")
_TcpipDisplayMask_Type = Integer32
_TcpipDisplayMask_Object = MibScalar
tcpipDisplayMask = _TcpipDisplayMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 1, 6),
    _TcpipDisplayMask_Type()
)
tcpipDisplayMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipDisplayMask.setStatus("mandatory")
_Netware_ObjectIdentity = ObjectIdentity
netware = _Netware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2)
)
_NwGroupVersion_Type = Integer32
_NwGroupVersion_Object = MibScalar
nwGroupVersion = _NwGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 1),
    _NwGroupVersion_Type()
)
nwGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwGroupVersion.setStatus("mandatory")


class _NwEnabled_Type(Integer32):
    """Custom type nwEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwEnabled_Type.__name__ = "Integer32"
_NwEnabled_Object = MibScalar
nwEnabled = _NwEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 2),
    _NwEnabled_Type()
)
nwEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwEnabled.setStatus("optional")
_NwCommands_ObjectIdentity = ObjectIdentity
nwCommands = _NwCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 3)
)


class _NwRestoreDefaults_Type(Integer32):
    """Custom type nwRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwRestoreDefaults_Type.__name__ = "Integer32"
_NwRestoreDefaults_Object = MibScalar
nwRestoreDefaults = _NwRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 3, 1),
    _NwRestoreDefaults_Type()
)
nwRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwRestoreDefaults.setStatus("optional")


class _NwFirmwareUpgrade_Type(Integer32):
    """Custom type nwFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwFirmwareUpgrade_Type.__name__ = "Integer32"
_NwFirmwareUpgrade_Object = MibScalar
nwFirmwareUpgrade = _NwFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 3, 2),
    _NwFirmwareUpgrade_Type()
)
nwFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwFirmwareUpgrade.setStatus("optional")
_NwConfigure_ObjectIdentity = ObjectIdentity
nwConfigure = _NwConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4)
)


class _NwFrameFormat_Type(Integer32):
    """Custom type nwFrameFormat based on Integer32"""
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
        *(("ethernet-802-2", 4),
          ("ethernet-802-3", 3),
          ("ethernet-II", 2),
          ("ethernet-Snap", 5),
          ("token-Ring", 6),
          ("token-Ring-Snap", 7),
          ("unknown", 1))
    )


_NwFrameFormat_Type.__name__ = "Integer32"
_NwFrameFormat_Object = MibScalar
nwFrameFormat = _NwFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 1),
    _NwFrameFormat_Type()
)
nwFrameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFrameFormat.setStatus("optional")


class _NwSetFrameFormat_Type(Integer32):
    """Custom type nwSetFrameFormat based on Integer32"""
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
        *(("auto-Sense", 1),
          ("forced-Ethernet-802-2", 4),
          ("forced-Ethernet-802-3", 3),
          ("forced-Ethernet-II", 2),
          ("forced-Ethernet-Snap", 5),
          ("forced-Token-Ring", 6),
          ("forced-Token-Ring-Snap", 7))
    )


_NwSetFrameFormat_Type.__name__ = "Integer32"
_NwSetFrameFormat_Object = MibScalar
nwSetFrameFormat = _NwSetFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 2),
    _NwSetFrameFormat_Type()
)
nwSetFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwSetFrameFormat.setStatus("optional")


class _NwMode_Type(Integer32):
    """Custom type nwMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pserver", 2),
          ("rprinter", 3),
          ("unknown", 1))
    )


_NwMode_Type.__name__ = "Integer32"
_NwMode_Object = MibScalar
nwMode = _NwMode_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 3),
    _NwMode_Type()
)
nwMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwMode.setStatus("optional")


class _NwPrintServerName_Type(DisplayString):
    """Custom type nwPrintServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwPrintServerName_Type.__name__ = "DisplayString"
_NwPrintServerName_Object = MibScalar
nwPrintServerName = _NwPrintServerName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 4),
    _NwPrintServerName_Type()
)
nwPrintServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPrintServerName.setStatus("optional")


class _NwPrintServerPassword_Type(DisplayString):
    """Custom type nwPrintServerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_NwPrintServerPassword_Type.__name__ = "DisplayString"
_NwPrintServerPassword_Object = MibScalar
nwPrintServerPassword = _NwPrintServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 5),
    _NwPrintServerPassword_Type()
)
nwPrintServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPrintServerPassword.setStatus("optional")


class _NwQueueScanTime_Type(Integer32):
    """Custom type nwQueueScanTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NwQueueScanTime_Type.__name__ = "Integer32"
_NwQueueScanTime_Object = MibScalar
nwQueueScanTime = _NwQueueScanTime_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 6),
    _NwQueueScanTime_Type()
)
nwQueueScanTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwQueueScanTime.setStatus("optional")


class _NwNetworkNumber_Type(OctetString):
    """Custom type nwNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NwNetworkNumber_Type.__name__ = "OctetString"
_NwNetworkNumber_Object = MibScalar
nwNetworkNumber = _NwNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 7),
    _NwNetworkNumber_Type()
)
nwNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNetworkNumber.setStatus("optional")
_NwMaxFileServers_Type = Integer32
_NwMaxFileServers_Object = MibScalar
nwMaxFileServers = _NwMaxFileServers_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 8),
    _NwMaxFileServers_Type()
)
nwMaxFileServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwMaxFileServers.setStatus("optional")
_NwFileServerTable_Object = MibTable
nwFileServerTable = _NwFileServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 9)
)
if mibBuilder.loadTexts:
    nwFileServerTable.setStatus("optional")
_NwFileServerEntry_Object = MibTableRow
nwFileServerEntry = _NwFileServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 9, 1)
)
nwFileServerEntry.setIndexNames(
    (0, "OKIDATA-MIB", "nwFileServerIndex"),
)
if mibBuilder.loadTexts:
    nwFileServerEntry.setStatus("optional")
_NwFileServerIndex_Type = Integer32
_NwFileServerIndex_Object = MibTableColumn
nwFileServerIndex = _NwFileServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 9, 1, 1),
    _NwFileServerIndex_Type()
)
nwFileServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFileServerIndex.setStatus("optional")


class _NwFileServerName_Type(DisplayString):
    """Custom type nwFileServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwFileServerName_Type.__name__ = "DisplayString"
_NwFileServerName_Object = MibTableColumn
nwFileServerName = _NwFileServerName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 9, 1, 2),
    _NwFileServerName_Type()
)
nwFileServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwFileServerName.setStatus("optional")


class _NwFileServerConnectionStatus_Type(Integer32):
    """Custom type nwFileServerConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              258,
              261,
              276,
              512,
              515,
              768,
              769,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("bad-CONNECTION", 768),
          ("bad-SERVICE-CONNECTION", 769),
          ("down", 2),
          ("other", 32767),
          ("pse-CANT-LOGIN", 276),
          ("pse-NO-RESPONSE", 261),
          ("pse-NO-SUCH-QUEUE", 512),
          ("pse-UNABLE-TO-ATTACH-TO-QUEUE", 515),
          ("pse-UNKNOWN-FILE-SERVER", 258),
          ("serverNeverAttached", 5),
          ("serverReattaching", 4),
          ("startupInProgress", 3),
          ("up", 1))
    )


_NwFileServerConnectionStatus_Type.__name__ = "Integer32"
_NwFileServerConnectionStatus_Object = MibTableColumn
nwFileServerConnectionStatus = _NwFileServerConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 9, 1, 3),
    _NwFileServerConnectionStatus_Type()
)
nwFileServerConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFileServerConnectionStatus.setStatus("optional")
_NwPortTable_Object = MibTable
nwPortTable = _NwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10)
)
if mibBuilder.loadTexts:
    nwPortTable.setStatus("optional")
_NwPortEntry_Object = MibTableRow
nwPortEntry = _NwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10, 1)
)
nwPortEntry.setIndexNames(
    (0, "OKIDATA-MIB", "nwPortIndex"),
)
if mibBuilder.loadTexts:
    nwPortEntry.setStatus("optional")
_NwPortIndex_Type = Integer32
_NwPortIndex_Object = MibTableColumn
nwPortIndex = _NwPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10, 1, 1),
    _NwPortIndex_Type()
)
nwPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwPortIndex.setStatus("optional")


class _NwPortStatus_Type(DisplayString):
    """Custom type nwPortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NwPortStatus_Type.__name__ = "DisplayString"
_NwPortStatus_Object = MibTableColumn
nwPortStatus = _NwPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10, 1, 2),
    _NwPortStatus_Type()
)
nwPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwPortStatus.setStatus("optional")


class _NwPortPrinterNumber_Type(Integer32):
    """Custom type nwPortPrinterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwPortPrinterNumber_Type.__name__ = "Integer32"
_NwPortPrinterNumber_Object = MibTableColumn
nwPortPrinterNumber = _NwPortPrinterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10, 1, 3),
    _NwPortPrinterNumber_Type()
)
nwPortPrinterNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortPrinterNumber.setStatus("optional")


class _NwPortFontDownload_Type(Integer32):
    """Custom type nwPortFontDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled-No-Power-Sense", 2),
          ("enabled-Power-Sense", 3))
    )


_NwPortFontDownload_Type.__name__ = "Integer32"
_NwPortFontDownload_Object = MibTableColumn
nwPortFontDownload = _NwPortFontDownload_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10, 1, 4),
    _NwPortFontDownload_Type()
)
nwPortFontDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortFontDownload.setStatus("optional")


class _NwPortPCLQueue_Type(DisplayString):
    """Custom type nwPortPCLQueue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwPortPCLQueue_Type.__name__ = "DisplayString"
_NwPortPCLQueue_Object = MibTableColumn
nwPortPCLQueue = _NwPortPCLQueue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10, 1, 5),
    _NwPortPCLQueue_Type()
)
nwPortPCLQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortPCLQueue.setStatus("optional")


class _NwPortPSQueue_Type(DisplayString):
    """Custom type nwPortPSQueue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwPortPSQueue_Type.__name__ = "DisplayString"
_NwPortPSQueue_Object = MibTableColumn
nwPortPSQueue = _NwPortPSQueue_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10, 1, 6),
    _NwPortPSQueue_Type()
)
nwPortPSQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortPSQueue.setStatus("optional")


class _NwPortFormsOn_Type(Integer32):
    """Custom type nwPortFormsOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwPortFormsOn_Type.__name__ = "Integer32"
_NwPortFormsOn_Object = MibTableColumn
nwPortFormsOn = _NwPortFormsOn_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10, 1, 7),
    _NwPortFormsOn_Type()
)
nwPortFormsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortFormsOn.setStatus("optional")


class _NwPortFormNumber_Type(Integer32):
    """Custom type nwPortFormNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwPortFormNumber_Type.__name__ = "Integer32"
_NwPortFormNumber_Object = MibTableColumn
nwPortFormNumber = _NwPortFormNumber_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10, 1, 8),
    _NwPortFormNumber_Type()
)
nwPortFormNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortFormNumber.setStatus("optional")


class _NwPortNotification_Type(Integer32):
    """Custom type nwPortNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwPortNotification_Type.__name__ = "Integer32"
_NwPortNotification_Object = MibTableColumn
nwPortNotification = _NwPortNotification_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 10, 1, 9),
    _NwPortNotification_Type()
)
nwPortNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortNotification.setStatus("optional")
_NwNumTraps_Type = Integer32
_NwNumTraps_Object = MibScalar
nwNumTraps = _NwNumTraps_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 11),
    _NwNumTraps_Type()
)
nwNumTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNumTraps.setStatus("mandatory")
_NwTrapTable_Object = MibTable
nwTrapTable = _NwTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 12)
)
if mibBuilder.loadTexts:
    nwTrapTable.setStatus("mandatory")
_NwTrapEntry_Object = MibTableRow
nwTrapEntry = _NwTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 12, 1)
)
nwTrapEntry.setIndexNames(
    (0, "OKIDATA-MIB", "nwTrapIndex"),
)
if mibBuilder.loadTexts:
    nwTrapEntry.setStatus("mandatory")
_NwTrapIndex_Type = Integer32
_NwTrapIndex_Object = MibTableColumn
nwTrapIndex = _NwTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 12, 1, 1),
    _NwTrapIndex_Type()
)
nwTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwTrapIndex.setStatus("mandatory")


class _NwTrapDestination_Type(OctetString):
    """Custom type nwTrapDestination based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NwTrapDestination_Type.__name__ = "OctetString"
_NwTrapDestination_Object = MibTableColumn
nwTrapDestination = _NwTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 12, 1, 2),
    _NwTrapDestination_Type()
)
nwTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwTrapDestination.setStatus("optional")


class _NwTrapDestinationNet_Type(OctetString):
    """Custom type nwTrapDestinationNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NwTrapDestinationNet_Type.__name__ = "OctetString"
_NwTrapDestinationNet_Object = MibTableColumn
nwTrapDestinationNet = _NwTrapDestinationNet_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 12, 1, 3),
    _NwTrapDestinationNet_Type()
)
nwTrapDestinationNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwTrapDestinationNet.setStatus("mandatory")
_NwPrinter2TrapMask_Type = Integer32
_NwPrinter2TrapMask_Object = MibTableColumn
nwPrinter2TrapMask = _NwPrinter2TrapMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 12, 1, 4),
    _NwPrinter2TrapMask_Type()
)
nwPrinter2TrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPrinter2TrapMask.setStatus("optional")
_NwPrinterTrapMask_Type = Integer32
_NwPrinterTrapMask_Object = MibTableColumn
nwPrinterTrapMask = _NwPrinterTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 12, 1, 5),
    _NwPrinterTrapMask_Type()
)
nwPrinterTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPrinterTrapMask.setStatus("optional")
_NwOutputTrapMask_Type = Integer32
_NwOutputTrapMask_Object = MibTableColumn
nwOutputTrapMask = _NwOutputTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 12, 1, 6),
    _NwOutputTrapMask_Type()
)
nwOutputTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwOutputTrapMask.setStatus("optional")


class _NwNDSPrintServerName_Type(DisplayString):
    """Custom type nwNDSPrintServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_NwNDSPrintServerName_Type.__name__ = "DisplayString"
_NwNDSPrintServerName_Object = MibScalar
nwNDSPrintServerName = _NwNDSPrintServerName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 13),
    _NwNDSPrintServerName_Type()
)
nwNDSPrintServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPrintServerName.setStatus("optional")


class _NwNDSPreferredDSTree_Type(DisplayString):
    """Custom type nwNDSPreferredDSTree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwNDSPreferredDSTree_Type.__name__ = "DisplayString"
_NwNDSPreferredDSTree_Object = MibScalar
nwNDSPreferredDSTree = _NwNDSPreferredDSTree_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 14),
    _NwNDSPreferredDSTree_Type()
)
nwNDSPreferredDSTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPreferredDSTree.setStatus("optional")


class _NwNDSPreferredDSFileServer_Type(DisplayString):
    """Custom type nwNDSPreferredDSFileServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwNDSPreferredDSFileServer_Type.__name__ = "DisplayString"
_NwNDSPreferredDSFileServer_Object = MibScalar
nwNDSPreferredDSFileServer = _NwNDSPreferredDSFileServer_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 15),
    _NwNDSPreferredDSFileServer_Type()
)
nwNDSPreferredDSFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPreferredDSFileServer.setStatus("optional")
_NwNDSPacketCheckSumEnabled_Type = Integer32
_NwNDSPacketCheckSumEnabled_Object = MibScalar
nwNDSPacketCheckSumEnabled = _NwNDSPacketCheckSumEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 16),
    _NwNDSPacketCheckSumEnabled_Type()
)
nwNDSPacketCheckSumEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPacketCheckSumEnabled.setStatus("optional")
_NwNDSPacketSignatureLevel_Type = Integer32
_NwNDSPacketSignatureLevel_Object = MibScalar
nwNDSPacketSignatureLevel = _NwNDSPacketSignatureLevel_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 17),
    _NwNDSPacketSignatureLevel_Type()
)
nwNDSPacketSignatureLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPacketSignatureLevel.setStatus("optional")
_NwAvailablePrintModes_Type = Integer32
_NwAvailablePrintModes_Object = MibScalar
nwAvailablePrintModes = _NwAvailablePrintModes_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 18),
    _NwAvailablePrintModes_Type()
)
nwAvailablePrintModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAvailablePrintModes.setStatus("optional")


class _NwDirectPrintEnabled_Type(Integer32):
    """Custom type nwDirectPrintEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwDirectPrintEnabled_Type.__name__ = "Integer32"
_NwDirectPrintEnabled_Object = MibScalar
nwDirectPrintEnabled = _NwDirectPrintEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 19),
    _NwDirectPrintEnabled_Type()
)
nwDirectPrintEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDirectPrintEnabled.setStatus("optional")


class _NwJAConfig_Type(Integer32):
    """Custom type nwJAConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwJAConfig_Type.__name__ = "Integer32"
_NwJAConfig_Object = MibScalar
nwJAConfig = _NwJAConfig_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 20),
    _NwJAConfig_Type()
)
nwJAConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwJAConfig.setStatus("optional")


class _NwDisableSAP_Type(Integer32):
    """Custom type nwDisableSAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwDisableSAP_Type.__name__ = "Integer32"
_NwDisableSAP_Object = MibScalar
nwDisableSAP = _NwDisableSAP_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 4, 21),
    _NwDisableSAP_Type()
)
nwDisableSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDisableSAP.setStatus("optional")
_NwStatus_ObjectIdentity = ObjectIdentity
nwStatus = _NwStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 5)
)


class _NwError_Type(DisplayString):
    """Custom type nwError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_NwError_Type.__name__ = "DisplayString"
_NwError_Object = MibScalar
nwError = _NwError_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 5, 1),
    _NwError_Type()
)
nwError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwError.setStatus("optional")
_NwDisplayMask_Type = Integer32
_NwDisplayMask_Object = MibScalar
nwDisplayMask = _NwDisplayMask_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 2, 6),
    _NwDisplayMask_Type()
)
nwDisplayMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDisplayMask.setStatus("mandatory")
_Vines_ObjectIdentity = ObjectIdentity
vines = _Vines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3)
)
_BvGroupVersion_Type = Integer32
_BvGroupVersion_Object = MibScalar
bvGroupVersion = _BvGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 1),
    _BvGroupVersion_Type()
)
bvGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvGroupVersion.setStatus("mandatory")


class _BvEnabled_Type(Integer32):
    """Custom type bvEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BvEnabled_Type.__name__ = "Integer32"
_BvEnabled_Object = MibScalar
bvEnabled = _BvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 2),
    _BvEnabled_Type()
)
bvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvEnabled.setStatus("optional")
_BvCommands_ObjectIdentity = ObjectIdentity
bvCommands = _BvCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 3)
)


class _BvRestoreDefaults_Type(Integer32):
    """Custom type bvRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BvRestoreDefaults_Type.__name__ = "Integer32"
_BvRestoreDefaults_Object = MibScalar
bvRestoreDefaults = _BvRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 3, 1),
    _BvRestoreDefaults_Type()
)
bvRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvRestoreDefaults.setStatus("optional")


class _BvFirmwareUpgrade_Type(Integer32):
    """Custom type bvFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BvFirmwareUpgrade_Type.__name__ = "Integer32"
_BvFirmwareUpgrade_Object = MibScalar
bvFirmwareUpgrade = _BvFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 3, 2),
    _BvFirmwareUpgrade_Type()
)
bvFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvFirmwareUpgrade.setStatus("optional")


class _BvSetSequenceRouting_Type(Integer32):
    """Custom type bvSetSequenceRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic-Routing", 1),
          ("force-Non-Sequenced-Routing", 3),
          ("force-Sequenced-Routing", 2))
    )


_BvSetSequenceRouting_Type.__name__ = "Integer32"
_BvSetSequenceRouting_Object = MibScalar
bvSetSequenceRouting = _BvSetSequenceRouting_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 3, 3),
    _BvSetSequenceRouting_Type()
)
bvSetSequenceRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvSetSequenceRouting.setStatus("optional")


class _BvDisableVPMan_Type(Integer32):
    """Custom type bvDisableVPMan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BvDisableVPMan_Type.__name__ = "Integer32"
_BvDisableVPMan_Object = MibScalar
bvDisableVPMan = _BvDisableVPMan_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 3, 4),
    _BvDisableVPMan_Type()
)
bvDisableVPMan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvDisableVPMan.setStatus("optional")
_BvConfigure_ObjectIdentity = ObjectIdentity
bvConfigure = _BvConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 4)
)


class _BvLoginName_Type(DisplayString):
    """Custom type bvLoginName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 63),
    )


_BvLoginName_Type.__name__ = "DisplayString"
_BvLoginName_Object = MibScalar
bvLoginName = _BvLoginName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 4, 1),
    _BvLoginName_Type()
)
bvLoginName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvLoginName.setStatus("optional")


class _BvLoginPassword_Type(DisplayString):
    """Custom type bvLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BvLoginPassword_Type.__name__ = "DisplayString"
_BvLoginPassword_Object = MibScalar
bvLoginPassword = _BvLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 4, 2),
    _BvLoginPassword_Type()
)
bvLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvLoginPassword.setStatus("optional")
_BvNumberPrintServices_Type = Integer32
_BvNumberPrintServices_Object = MibScalar
bvNumberPrintServices = _BvNumberPrintServices_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 4, 3),
    _BvNumberPrintServices_Type()
)
bvNumberPrintServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvNumberPrintServices.setStatus("optional")
_BvPrintServiceTable_Object = MibTable
bvPrintServiceTable = _BvPrintServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 4, 4)
)
if mibBuilder.loadTexts:
    bvPrintServiceTable.setStatus("optional")
_BvPrintServiceEntry_Object = MibTableRow
bvPrintServiceEntry = _BvPrintServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 4, 4, 1)
)
bvPrintServiceEntry.setIndexNames(
    (0, "OKIDATA-MIB", "bvPrintServiceIndex"),
)
if mibBuilder.loadTexts:
    bvPrintServiceEntry.setStatus("optional")
_BvPrintServiceIndex_Type = Integer32
_BvPrintServiceIndex_Object = MibTableColumn
bvPrintServiceIndex = _BvPrintServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 4, 4, 1, 1),
    _BvPrintServiceIndex_Type()
)
bvPrintServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPrintServiceIndex.setStatus("optional")


class _BvPrintServiceName_Type(DisplayString):
    """Custom type bvPrintServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BvPrintServiceName_Type.__name__ = "DisplayString"
_BvPrintServiceName_Object = MibTableColumn
bvPrintServiceName = _BvPrintServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 4, 4, 1, 2),
    _BvPrintServiceName_Type()
)
bvPrintServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvPrintServiceName.setStatus("optional")
_BvPrintServiceRouting_Type = Integer32
_BvPrintServiceRouting_Object = MibTableColumn
bvPrintServiceRouting = _BvPrintServiceRouting_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 4, 4, 1, 3),
    _BvPrintServiceRouting_Type()
)
bvPrintServiceRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvPrintServiceRouting.setStatus("optional")


class _BvPnicDescription_Type(DisplayString):
    """Custom type bvPnicDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BvPnicDescription_Type.__name__ = "DisplayString"
_BvPnicDescription_Object = MibScalar
bvPnicDescription = _BvPnicDescription_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 4, 5),
    _BvPnicDescription_Type()
)
bvPnicDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvPnicDescription.setStatus("optional")
_BvStatus_ObjectIdentity = ObjectIdentity
bvStatus = _BvStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5)
)


class _BvError_Type(DisplayString):
    """Custom type bvError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_BvError_Type.__name__ = "DisplayString"
_BvError_Object = MibScalar
bvError = _BvError_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 1),
    _BvError_Type()
)
bvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvError.setStatus("optional")


class _BvRouting_Type(Integer32):
    """Custom type bvRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              32766,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("non-Sequenced-Routing", 2),
          ("protocol-Disabled", 32767),
          ("sequenced-Routing", 1),
          ("unknown-Routing", 32766))
    )


_BvRouting_Type.__name__ = "Integer32"
_BvRouting_Object = MibScalar
bvRouting = _BvRouting_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 2),
    _BvRouting_Type()
)
bvRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvRouting.setStatus("optional")
_BvNumPrintServices_Type = Integer32
_BvNumPrintServices_Object = MibScalar
bvNumPrintServices = _BvNumPrintServices_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 3),
    _BvNumPrintServices_Type()
)
bvNumPrintServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvNumPrintServices.setStatus("optional")
_BvPrintServiceStatusTable_Object = MibTable
bvPrintServiceStatusTable = _BvPrintServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4)
)
if mibBuilder.loadTexts:
    bvPrintServiceStatusTable.setStatus("optional")
_BvPrintServiceStatusEntry_Object = MibTableRow
bvPrintServiceStatusEntry = _BvPrintServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1)
)
bvPrintServiceStatusEntry.setIndexNames(
    (0, "OKIDATA-MIB", "bvPSStatusIndex"),
)
if mibBuilder.loadTexts:
    bvPrintServiceStatusEntry.setStatus("optional")
_BvPSStatusIndex_Type = Integer32
_BvPSStatusIndex_Object = MibTableColumn
bvPSStatusIndex = _BvPSStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1, 1),
    _BvPSStatusIndex_Type()
)
bvPSStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPSStatusIndex.setStatus("optional")


class _BvPSName_Type(DisplayString):
    """Custom type bvPSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BvPSName_Type.__name__ = "DisplayString"
_BvPSName_Object = MibTableColumn
bvPSName = _BvPSName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1, 2),
    _BvPSName_Type()
)
bvPSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPSName.setStatus("optional")


class _BvPSStatus_Type(DisplayString):
    """Custom type bvPSStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_BvPSStatus_Type.__name__ = "DisplayString"
_BvPSStatus_Object = MibTableColumn
bvPSStatus = _BvPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1, 3),
    _BvPSStatus_Type()
)
bvPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPSStatus.setStatus("optional")
_BvPSDestination_Type = Integer32
_BvPSDestination_Object = MibTableColumn
bvPSDestination = _BvPSDestination_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1, 4),
    _BvPSDestination_Type()
)
bvPSDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPSDestination.setStatus("optional")


class _BvPrinterStatus_Type(DisplayString):
    """Custom type bvPrinterStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BvPrinterStatus_Type.__name__ = "DisplayString"
_BvPrinterStatus_Object = MibTableColumn
bvPrinterStatus = _BvPrinterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1, 5),
    _BvPrinterStatus_Type()
)
bvPrinterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPrinterStatus.setStatus("optional")


class _BvJobActive_Type(Integer32):
    """Custom type bvJobActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BvJobActive_Type.__name__ = "Integer32"
_BvJobActive_Object = MibTableColumn
bvJobActive = _BvJobActive_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1, 6),
    _BvJobActive_Type()
)
bvJobActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvJobActive.setStatus("optional")


class _BvJobSource_Type(DisplayString):
    """Custom type bvJobSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BvJobSource_Type.__name__ = "DisplayString"
_BvJobSource_Object = MibTableColumn
bvJobSource = _BvJobSource_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1, 7),
    _BvJobSource_Type()
)
bvJobSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvJobSource.setStatus("optional")


class _BvJobTitle_Type(DisplayString):
    """Custom type bvJobTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BvJobTitle_Type.__name__ = "DisplayString"
_BvJobTitle_Object = MibTableColumn
bvJobTitle = _BvJobTitle_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1, 8),
    _BvJobTitle_Type()
)
bvJobTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvJobTitle.setStatus("optional")


class _BvJobSize_Type(DisplayString):
    """Custom type bvJobSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_BvJobSize_Type.__name__ = "DisplayString"
_BvJobSize_Object = MibTableColumn
bvJobSize = _BvJobSize_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1, 9),
    _BvJobSize_Type()
)
bvJobSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvJobSize.setStatus("optional")


class _BvJobNumber_Type(DisplayString):
    """Custom type bvJobNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BvJobNumber_Type.__name__ = "DisplayString"
_BvJobNumber_Object = MibTableColumn
bvJobNumber = _BvJobNumber_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 3, 5, 4, 1, 10),
    _BvJobNumber_Type()
)
bvJobNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvJobNumber.setStatus("optional")
_LanManager_ObjectIdentity = ObjectIdentity
lanManager = _LanManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 4)
)
_LmGroupVersion_Type = Integer32
_LmGroupVersion_Object = MibScalar
lmGroupVersion = _LmGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 4, 1),
    _LmGroupVersion_Type()
)
lmGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmGroupVersion.setStatus("mandatory")


class _LmEnabled_Type(Integer32):
    """Custom type lmEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LmEnabled_Type.__name__ = "Integer32"
_LmEnabled_Object = MibScalar
lmEnabled = _LmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 4, 2),
    _LmEnabled_Type()
)
lmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmEnabled.setStatus("optional")
_ETalk_ObjectIdentity = ObjectIdentity
eTalk = _ETalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5)
)
_ETalkGroupVersion_Type = Integer32
_ETalkGroupVersion_Object = MibScalar
eTalkGroupVersion = _ETalkGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 1),
    _ETalkGroupVersion_Type()
)
eTalkGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkGroupVersion.setStatus("mandatory")


class _ETalkEnabled_Type(Integer32):
    """Custom type eTalkEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ETalkEnabled_Type.__name__ = "Integer32"
_ETalkEnabled_Object = MibScalar
eTalkEnabled = _ETalkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 2),
    _ETalkEnabled_Type()
)
eTalkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkEnabled.setStatus("optional")
_ETalkCommands_ObjectIdentity = ObjectIdentity
eTalkCommands = _ETalkCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 3)
)


class _ETalkRestoreDefaults_Type(Integer32):
    """Custom type eTalkRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ETalkRestoreDefaults_Type.__name__ = "Integer32"
_ETalkRestoreDefaults_Object = MibScalar
eTalkRestoreDefaults = _ETalkRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 3, 1),
    _ETalkRestoreDefaults_Type()
)
eTalkRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkRestoreDefaults.setStatus("optional")
_ETalkConfigure_ObjectIdentity = ObjectIdentity
eTalkConfigure = _ETalkConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4)
)


class _ETalkNetwork_Type(OctetString):
    """Custom type eTalkNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ETalkNetwork_Type.__name__ = "OctetString"
_ETalkNetwork_Object = MibScalar
eTalkNetwork = _ETalkNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 1),
    _ETalkNetwork_Type()
)
eTalkNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkNetwork.setStatus("optional")


class _ETalkNode_Type(OctetString):
    """Custom type eTalkNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ETalkNode_Type.__name__ = "OctetString"
_ETalkNode_Object = MibScalar
eTalkNode = _ETalkNode_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 2),
    _ETalkNode_Type()
)
eTalkNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkNode.setStatus("optional")
_ETalkNumPorts_Type = Integer32
_ETalkNumPorts_Object = MibScalar
eTalkNumPorts = _ETalkNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 3),
    _ETalkNumPorts_Type()
)
eTalkNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkNumPorts.setStatus("optional")
_ETalkPortTable_Object = MibTable
eTalkPortTable = _ETalkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 4)
)
if mibBuilder.loadTexts:
    eTalkPortTable.setStatus("optional")
_ETalkPortEntry_Object = MibTableRow
eTalkPortEntry = _ETalkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 4, 1)
)
eTalkPortEntry.setIndexNames(
    (0, "OKIDATA-MIB", "eTalkPortIndex"),
)
if mibBuilder.loadTexts:
    eTalkPortEntry.setStatus("optional")
_ETalkPortIndex_Type = Integer32
_ETalkPortIndex_Object = MibTableColumn
eTalkPortIndex = _ETalkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 4, 1, 1),
    _ETalkPortIndex_Type()
)
eTalkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkPortIndex.setStatus("optional")


class _ETalkPortEnable_Type(Integer32):
    """Custom type eTalkPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ETalkPortEnable_Type.__name__ = "Integer32"
_ETalkPortEnable_Object = MibTableColumn
eTalkPortEnable = _ETalkPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 4, 1, 2),
    _ETalkPortEnable_Type()
)
eTalkPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkPortEnable.setStatus("optional")


class _ETalkName_Type(DisplayString):
    """Custom type eTalkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ETalkName_Type.__name__ = "DisplayString"
_ETalkName_Object = MibTableColumn
eTalkName = _ETalkName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 4, 1, 3),
    _ETalkName_Type()
)
eTalkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkName.setStatus("optional")


class _ETalkActiveName_Type(DisplayString):
    """Custom type eTalkActiveName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ETalkActiveName_Type.__name__ = "DisplayString"
_ETalkActiveName_Object = MibTableColumn
eTalkActiveName = _ETalkActiveName_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 4, 1, 4),
    _ETalkActiveName_Type()
)
eTalkActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkActiveName.setStatus("optional")


class _ETalkType1_Type(DisplayString):
    """Custom type eTalkType1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ETalkType1_Type.__name__ = "DisplayString"
_ETalkType1_Object = MibTableColumn
eTalkType1 = _ETalkType1_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 4, 1, 5),
    _ETalkType1_Type()
)
eTalkType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkType1.setStatus("optional")


class _ETalkType2_Type(DisplayString):
    """Custom type eTalkType2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ETalkType2_Type.__name__ = "DisplayString"
_ETalkType2_Object = MibTableColumn
eTalkType2 = _ETalkType2_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 4, 1, 6),
    _ETalkType2_Type()
)
eTalkType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkType2.setStatus("optional")


class _ETalkZone_Type(DisplayString):
    """Custom type eTalkZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ETalkZone_Type.__name__ = "DisplayString"
_ETalkZone_Object = MibTableColumn
eTalkZone = _ETalkZone_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 4, 1, 7),
    _ETalkZone_Type()
)
eTalkZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkZone.setStatus("optional")


class _ETalkActiveZone_Type(DisplayString):
    """Custom type eTalkActiveZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ETalkActiveZone_Type.__name__ = "DisplayString"
_ETalkActiveZone_Object = MibTableColumn
eTalkActiveZone = _ETalkActiveZone_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 4, 4, 1, 8),
    _ETalkActiveZone_Type()
)
eTalkActiveZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkActiveZone.setStatus("optional")
_ETalkStatus_ObjectIdentity = ObjectIdentity
eTalkStatus = _ETalkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 5)
)


class _ETalkError_Type(DisplayString):
    """Custom type eTalkError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ETalkError_Type.__name__ = "DisplayString"
_ETalkError_Object = MibScalar
eTalkError = _ETalkError_Object(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 3, 5, 5, 1),
    _ETalkError_Type()
)
eTalkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkError.setStatus("optional")

# Managed Objects groups


# Notification objects

trapPrinterOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 0, 1)
)
trapPrinterOnline.setObjects(
    ("OKIDATA-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterOnline.setStatus(
        ""
    )

trapPrinterOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 0, 2)
)
trapPrinterOffline.setObjects(
    ("OKIDATA-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterOffline.setStatus(
        ""
    )

trapNoPrinterAttached = NotificationType(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 0, 3)
)
trapNoPrinterAttached.setObjects(
    ("OKIDATA-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapNoPrinterAttached.setStatus(
        ""
    )

trapPrinterTonerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 0, 4)
)
trapPrinterTonerLow.setObjects(
    ("OKIDATA-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterTonerLow.setStatus(
        ""
    )

trapPrinterPaperOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 0, 5)
)
trapPrinterPaperOut.setObjects(
    ("OKIDATA-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterPaperOut.setStatus(
        ""
    )

trapPrinterPaperJam = NotificationType(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 0, 6)
)
trapPrinterPaperJam.setObjects(
    ("OKIDATA-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterPaperJam.setStatus(
        ""
    )

trapPrinterDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 0, 7)
)
trapPrinterDoorOpen.setObjects(
    ("OKIDATA-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterDoorOpen.setStatus(
        ""
    )

trapPrinterError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2001, 1, 2, 683, 6, 0, 16)
)
trapPrinterError.setObjects(
    ("OKIDATA-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OKIDATA-MIB",
    **{"okidata": okidata,
       "peripheral": peripheral,
       "printer": printer,
       "nip": nip,
       "niptype1": niptype1,
       "cfg": cfg,
       "cfgPersonality": cfgPersonality,
       "cfgManualFeed": cfgManualFeed,
       "cfgOkiPaperFeed": cfgOkiPaperFeed,
       "cfgOkiAutoTraySwitch": cfgOkiAutoTraySwitch,
       "cfgOkiPriorityTray": cfgOkiPriorityTray,
       "cfgPaper": cfgPaper,
       "cfgOkiCustomPaperWidth": cfgOkiCustomPaperWidth,
       "cfgOkiCustomPaperLength": cfgOkiCustomPaperLength,
       "cfgInTray2Size": cfgInTray2Size,
       "cfgInTray3Size": cfgInTray3Size,
       "cfgInTray5Size": cfgInTray5Size,
       "cfgInTray1Size": cfgInTray1Size,
       "cfgInTray4Size": cfgInTray4Size,
       "cfgOkiMediaInTray2": cfgOkiMediaInTray2,
       "cfgOkiMediaInTray3": cfgOkiMediaInTray3,
       "cfgOkiMediaInTray5": cfgOkiMediaInTray5,
       "cfgOkiMediaInTray1": cfgOkiMediaInTray1,
       "cfgOkiMediaInTray4": cfgOkiMediaInTray4,
       "cfgOkiPaperSizeCheck": cfgOkiPaperSizeCheck,
       "cfgMptray": cfgMptray,
       "cfgIntray1": cfgIntray1,
       "cfgIntray2": cfgIntray2,
       "cfgIntray3": cfgIntray3,
       "cfgCopies": cfgCopies,
       "cfgDuplex": cfgDuplex,
       "cfgBinding": cfgBinding,
       "cfgPclFontSource": cfgPclFontSource,
       "cfgPclFontNumber": cfgPclFontNumber,
       "cfgPclPitch": cfgPclPitch,
       "cfgPclPtSize": cfgPclPtSize,
       "cfgPclSymSet": cfgPclSymSet,
       "cfgPclOkiA4PrintWidth": cfgPclOkiA4PrintWidth,
       "cfgPclOkiWhitePageSkip": cfgPclOkiWhitePageSkip,
       "cfgPclOkiCrFunction": cfgPclOkiCrFunction,
       "cfgPclOkiLfFunction": cfgPclOkiLfFunction,
       "cfgIbmpprCharacterPitch": cfgIbmpprCharacterPitch,
       "cfgIbmpprFontCondense": cfgIbmpprFontCondense,
       "cfgIbmpprCharacterSet": cfgIbmpprCharacterSet,
       "cfgIbmpprSymbolSet": cfgIbmpprSymbolSet,
       "cfgIbmpprLetterOStyle": cfgIbmpprLetterOStyle,
       "cfgIbmpprLinePitch": cfgIbmpprLinePitch,
       "cfgIbmpprWhitePageSkip": cfgIbmpprWhitePageSkip,
       "cfgIbmpprCrFunction": cfgIbmpprCrFunction,
       "cfgIbmpprLfFunction": cfgIbmpprLfFunction,
       "cfgIbmpprLineLength": cfgIbmpprLineLength,
       "cfgIbmpprFormLength": cfgIbmpprFormLength,
       "cfgIbmpprTofPosition": cfgIbmpprTofPosition,
       "cfgIbmpprLeftMargine": cfgIbmpprLeftMargine,
       "cfgEpsonfxCharacterPitch": cfgEpsonfxCharacterPitch,
       "cfgEpsonfxCharacterSet": cfgEpsonfxCharacterSet,
       "cfgEpsonfxSymbolSet": cfgEpsonfxSymbolSet,
       "cfgEpsonfxLetterOStyle": cfgEpsonfxLetterOStyle,
       "cfgEpsonfxLinePitch": cfgEpsonfxLinePitch,
       "cfgEpsonfxWhitePageSkip": cfgEpsonfxWhitePageSkip,
       "cfgEpsonfxCrFunction": cfgEpsonfxCrFunction,
       "cfgEpsonfxLineLength": cfgEpsonfxLineLength,
       "cfgEpsonfxFormLength": cfgEpsonfxFormLength,
       "cfgEpsonfxTofPosition": cfgEpsonfxTofPosition,
       "cfgEpsonfxLeftMargine": cfgEpsonfxLeftMargine,
       "cfgHiperwOkiDensity": cfgHiperwOkiDensity,
       "cfgHiperwOkiFirstbit": cfgHiperwOkiFirstbit,
       "cfgHiperwOkiReverse": cfgHiperwOkiReverse,
       "cfgHiperwPrintSpeed": cfgHiperwPrintSpeed,
       "cfgEscpKanjiFont": cfgEscpKanjiFont,
       "cfgEscpAnkFont": cfgEscpAnkFont,
       "cfgEscpCharacterSet": cfgEscpCharacterSet,
       "cfgEscpZeroCharacter": cfgEscpZeroCharacter,
       "cfgEscpZoom": cfgEscpZoom,
       "cfgEscpTofPosition": cfgEscpTofPosition,
       "cfgEscpLineLength": cfgEscpLineLength,
       "cfgEscpCrFunction": cfgEscpCrFunction,
       "cfgEscpAutoLf": cfgEscpAutoLf,
       "cfgOrientation": cfgOrientation,
       "cfgFormLines": cfgFormLines,
       "cfgParallel": cfgParallel,
       "cfgRs232c": cfgRs232c,
       "cfgRs422": cfgRs422,
       "cfgLocalTalk": cfgLocalTalk,
       "cfgNetwork": cfgNetwork,
       "cfgUsb": cfgUsb,
       "cfgResolution": cfgResolution,
       "cfgRet": cfgRet,
       "cfgOkiRasterBuffer": cfgOkiRasterBuffer,
       "cfgPageProtect": cfgPageProtect,
       "cfgPrintProtect": cfgPrintProtect,
       "cfgOkiReceiveBuffer": cfgOkiReceiveBuffer,
       "cfgOkiFontProtection": cfgOkiFontProtection,
       "cfgOkiResourceSave": cfgOkiResourceSave,
       "cfgAutoCont": cfgAutoCont,
       "cfgOkiAutoEject": cfgOkiAutoEject,
       "cfgManualTimeOut": cfgManualTimeOut,
       "cfgDensity": cfgDensity,
       "cfgOkiYellowDarkness": cfgOkiYellowDarkness,
       "cfgOkiMagentaDarkness": cfgOkiMagentaDarkness,
       "cfgOkiCyanDarkness": cfgOkiCyanDarkness,
       "cfgOkiBlackDarkness": cfgOkiBlackDarkness,
       "cfgOkiPowerSaving": cfgOkiPowerSaving,
       "cfgOkiQuietMode": cfgOkiQuietMode,
       "cfgLowToner": cfgLowToner,
       "cfgEconoMode": cfgEconoMode,
       "cfgClearableWarnings": cfgClearableWarnings,
       "cfgOkiPrintErrors": cfgOkiPrintErrors,
       "cfgParallelSpeed": cfgParallelSpeed,
       "cfgBiDirection": cfgBiDirection,
       "cfgOkiIPrime": cfgOkiIPrime,
       "cfgLang": cfgLang,
       "cfgOkiJobSwitch": cfgOkiJobSwitch,
       "cfgRs232cBaud": cfgRs232cBaud,
       "cfgRs232cDataBits": cfgRs232cDataBits,
       "cfgRs232cStopBits": cfgRs232cStopBits,
       "cfgRs232cParity": cfgRs232cParity,
       "cfgRs232cBusyTime": cfgRs232cBusyTime,
       "cfgRs232cFlowControl": cfgRs232cFlowControl,
       "cfgRs422Baud": cfgRs422Baud,
       "cfgRs422DataBits": cfgRs422DataBits,
       "cfgRs422StopBits": cfgRs422StopBits,
       "cfgRs422Parity": cfgRs422Parity,
       "cfgOkiUser": cfgOkiUser,
       "cfgOkiEcp": cfgOkiEcp,
       "cfgOkiXAdjust": cfgOkiXAdjust,
       "cfgOkiYAdjust": cfgOkiYAdjust,
       "cfgOkiDuplexAdjust": cfgOkiDuplexAdjust,
       "cfgOkiMediaSourceTray2": cfgOkiMediaSourceTray2,
       "cfgOkiMediaSourceTray3": cfgOkiMediaSourceTray3,
       "cfgOkiMediaSourceFront": cfgOkiMediaSourceFront,
       "cfgPlacePage": cfgPlacePage,
       "cfgOkiColorAdjustPrint": cfgOkiColorAdjustPrint,
       "cfgOkiColorAdjustYellow": cfgOkiColorAdjustYellow,
       "cfgOkiColorAdjustMagenta": cfgOkiColorAdjustMagenta,
       "cfgOkiColorAdjustCyan": cfgOkiColorAdjustCyan,
       "cfgOkiJamRecovery": cfgOkiJamRecovery,
       "cfgFirmCpuVersion": cfgFirmCpuVersion,
       "cfgEngineFirmVersion": cfgEngineFirmVersion,
       "cfgMessageVersion": cfgMessageVersion,
       "cfgPclFirmVersion": cfgPclFirmVersion,
       "cfgPclxlFirmVersion": cfgPclxlFirmVersion,
       "cfgSidmFirmVersion": cfgSidmFirmVersion,
       "cfgHdFirmVersion": cfgHdFirmVersion,
       "cfgPsFirmVersion": cfgPsFirmVersion,
       "cfgEmulationTable": cfgEmulationTable,
       "cfgEmulationEntry": cfgEmulationEntry,
       "cfgEmulationIndex": cfgEmulationIndex,
       "cfgEmulationName": cfgEmulationName,
       "cfgRamInstalledSize": cfgRamInstalledSize,
       "cfgTrayTable": cfgTrayTable,
       "cfgTrayEntry": cfgTrayEntry,
       "cfgTrayIndex": cfgTrayIndex,
       "cfgTrayName": cfgTrayName,
       "cfgPrinterName": cfgPrinterName,
       "stat": stat,
       "stPjlStatus": stPjlStatus,
       "stLcdMessage": stLcdMessage,
       "stOnline": stOnline,
       "stManualLedStatus": stManualLedStatus,
       "stOperatorLedStatus": stOperatorLedStatus,
       "stServiceLedStatus": stServiceLedStatus,
       "stOnlineLedStatus": stOnlineLedStatus,
       "stPsStatus": stPsStatus,
       "cfg2": cfg2,
       "cfg2General": cfg2General,
       "cfg2PrinterInformation": cfg2PrinterInformation,
       "cfg2Type1MIBVersion": cfg2Type1MIBVersion,
       "cfg2ModelId": cfg2ModelId,
       "cfg2PrinterVersions": cfg2PrinterVersions,
       "cfg2PrinterVersion1Table": cfg2PrinterVersion1Table,
       "cfg2PrinterVersion1": cfg2PrinterVersion1,
       "cfg2PrinterVersion2Table": cfg2PrinterVersion2Table,
       "cfg2PrinterVersion2": cfg2PrinterVersion2,
       "cfg2PrinterVersion3Table": cfg2PrinterVersion3Table,
       "cfg2PrinterVersion3": cfg2PrinterVersion3,
       "cfg2PrinterVersion4Table": cfg2PrinterVersion4Table,
       "cfg2PrinterVersion4": cfg2PrinterVersion4,
       "cfg2PrinterVersion5Table": cfg2PrinterVersion5Table,
       "cfg2PrinterVersion5": cfg2PrinterVersion5,
       "cfg2PrinterVersion6Table": cfg2PrinterVersion6Table,
       "cfg2PrinterVersion6": cfg2PrinterVersion6,
       "cfg2PrinterVersion7Table": cfg2PrinterVersion7Table,
       "cfg2PrinterVersion7": cfg2PrinterVersion7,
       "cfg2PrinterVersion8Table": cfg2PrinterVersion8Table,
       "cfg2PrinterVersion8": cfg2PrinterVersion8,
       "cfg2PrinterVersion9Table": cfg2PrinterVersion9Table,
       "cfg2PrinterVersion9": cfg2PrinterVersion9,
       "cfg2PrinterVersion10Table": cfg2PrinterVersion10Table,
       "cfg2PrinterVersion10": cfg2PrinterVersion10,
       "cfg2PrinterType": cfg2PrinterType,
       "cfg2PrinterConsumption": cfg2PrinterConsumption,
       "cfg2PowerSave": cfg2PowerSave,
       "cfg2PowerSaveCurrentValue": cfg2PowerSaveCurrentValue,
       "cfg2PowerSaveShift": cfg2PowerSaveShift,
       "cfg2PowerSaveShiftCurrentValue": cfg2PowerSaveShiftCurrentValue,
       "cfg2JamRecovery": cfg2JamRecovery,
       "cfg2JamRecoveryCurrentValue": cfg2JamRecoveryCurrentValue,
       "cfg2OPPanelLock": cfg2OPPanelLock,
       "cfg2OPPanelLockCurrentValue": cfg2OPPanelLockCurrentValue,
       "cfg2Controlt": cfg2Controlt,
       "cfg2ControltCurrentValue": cfg2ControltCurrentValue,
       "cfg2JobControl": cfg2JobControl,
       "cfg2PaperHandling": cfg2PaperHandling,
       "cfg2PHCommon": cfg2PHCommon,
       "cfg2MonoPrintSpeed": cfg2MonoPrintSpeed,
       "cfg2MonoPrintSpeedCurrentValue": cfg2MonoPrintSpeedCurrentValue,
       "cfg2PHInput": cfg2PHInput,
       "cfg2PriorityTray": cfg2PriorityTray,
       "cfg2PriorityTrayCurrentValue": cfg2PriorityTrayCurrentValue,
       "cfg2TrayTable": cfg2TrayTable,
       "cfg2Tray1Table": cfg2Tray1Table,
       "cfg2Tray1PaperSize": cfg2Tray1PaperSize,
       "cfg2Tray1PaperSizeCurrentValue": cfg2Tray1PaperSizeCurrentValue,
       "cfg2Tray1MediaType": cfg2Tray1MediaType,
       "cfg2Tray1MediaTypeCurrentValue": cfg2Tray1MediaTypeCurrentValue,
       "cfg2Tray1MediaWeight": cfg2Tray1MediaWeight,
       "cfg2Tray1MediaWeightCurrentValue": cfg2Tray1MediaWeightCurrentValue,
       "cfg2Tray2Table": cfg2Tray2Table,
       "cfg2Tray2PaperSize": cfg2Tray2PaperSize,
       "cfg2Tray2PaperSizeCurrentValue": cfg2Tray2PaperSizeCurrentValue,
       "cfg2Tray2MediaType": cfg2Tray2MediaType,
       "cfg2Tray2MediaTypeCurrentValue": cfg2Tray2MediaTypeCurrentValue,
       "cfg2Tray2MediaWeight": cfg2Tray2MediaWeight,
       "cfg2Tray2MediaWeightCurrentValue": cfg2Tray2MediaWeightCurrentValue,
       "cfg2Tray3Table": cfg2Tray3Table,
       "cfg2Tray3PaperSize": cfg2Tray3PaperSize,
       "cfg2Tray3PaperSizeCurrentValue": cfg2Tray3PaperSizeCurrentValue,
       "cfg2Tray3MediaType": cfg2Tray3MediaType,
       "cfg2Tray3MediaTypeCurrentValue": cfg2Tray3MediaTypeCurrentValue,
       "cfg2Tray3MediaWeight": cfg2Tray3MediaWeight,
       "cfg2Tray3MediaWeightCurrentValue": cfg2Tray3MediaWeightCurrentValue,
       "cfg2Tray4Table": cfg2Tray4Table,
       "cfg2Tray4PaperSize": cfg2Tray4PaperSize,
       "cfg2Tray4PaperSizeCurrentValue": cfg2Tray4PaperSizeCurrentValue,
       "cfg2Tray4MediaType": cfg2Tray4MediaType,
       "cfg2Tray4MediaTypeCurrentValue": cfg2Tray4MediaTypeCurrentValue,
       "cfg2Tray4MediaWeight": cfg2Tray4MediaWeight,
       "cfg2Tray4MediaWeightCurrentValue": cfg2Tray4MediaWeightCurrentValue,
       "cfg2Tray5Table": cfg2Tray5Table,
       "cfg2Tray5PaperSize": cfg2Tray5PaperSize,
       "cfg2Tray5PaperSizeCurrentValue": cfg2Tray5PaperSizeCurrentValue,
       "cfg2Tray5MediaType": cfg2Tray5MediaType,
       "cfg2Tray5MediaTypeCurrentValue": cfg2Tray5MediaTypeCurrentValue,
       "cfg2Tray5MediaWeight": cfg2Tray5MediaWeight,
       "cfg2Tray5MediaWeightCurrentValue": cfg2Tray5MediaWeightCurrentValue,
       "cfg2Tray6Table": cfg2Tray6Table,
       "cfg2Tray6PaperSize": cfg2Tray6PaperSize,
       "cfg2Tray6PaperSizeCurrentValue": cfg2Tray6PaperSizeCurrentValue,
       "cfg2Tray6MediaType": cfg2Tray6MediaType,
       "cfg2Tray6MediaTypeCurrentValue": cfg2Tray6MediaTypeCurrentValue,
       "cfg2Tray6MediaWeight": cfg2Tray6MediaWeight,
       "cfg2Tray6MediaWeightCurrentValue": cfg2Tray6MediaWeightCurrentValue,
       "cfg2Tray7Table": cfg2Tray7Table,
       "cfg2Tray7PaperSize": cfg2Tray7PaperSize,
       "cfg2Tray7PaperSizeCurrentValue": cfg2Tray7PaperSizeCurrentValue,
       "cfg2Tray7MediaType": cfg2Tray7MediaType,
       "cfg2Tray7MediaTypeCurrentValue": cfg2Tray7MediaTypeCurrentValue,
       "cfg2Tray7MediaWeight": cfg2Tray7MediaWeight,
       "cfg2Tray7MediaWeightCurrentValue": cfg2Tray7MediaWeightCurrentValue,
       "cfg2UnitOfMeasure": cfg2UnitOfMeasure,
       "cfg2UnitOfMeasureCurrentValue": cfg2UnitOfMeasureCurrentValue,
       "cfg2XDimension": cfg2XDimension,
       "cfg2XDimensionCurrentValue": cfg2XDimensionCurrentValue,
       "cfg2YDimension": cfg2YDimension,
       "cfg2YDimensionCurrentValue": cfg2YDimensionCurrentValue,
       "cfg2TrayA3Paper": cfg2TrayA3Paper,
       "cfg2Tray1A3Paper": cfg2Tray1A3Paper,
       "cfg2Tray1A3PaperCurrentValue": cfg2Tray1A3PaperCurrentValue,
       "cfg2Tray2A3Paper": cfg2Tray2A3Paper,
       "cfg2Tray2A3PaperCurrentValue": cfg2Tray2A3PaperCurrentValue,
       "cfg2Tray3A3Paper": cfg2Tray3A3Paper,
       "cfg2Tray3A3PaperCurrentValue": cfg2Tray3A3PaperCurrentValue,
       "cfg2Tray4A3Paper": cfg2Tray4A3Paper,
       "cfg2Tray4A3PaperCurrentValue": cfg2Tray4A3PaperCurrentValue,
       "cfg2Tray5A3Paper": cfg2Tray5A3Paper,
       "cfg2Tray5A3PaperCurrentValue": cfg2Tray5A3PaperCurrentValue,
       "cfg2Tray6A3Paper": cfg2Tray6A3Paper,
       "cfg2Tray6A3PaperCurrentValue": cfg2Tray6A3PaperCurrentValue,
       "cfg2Tray7A3Paper": cfg2Tray7A3Paper,
       "cfg2Tray7A3PaperCurrentValue": cfg2Tray7A3PaperCurrentValue,
       "cfg2TrayLegal14Paper": cfg2TrayLegal14Paper,
       "cfg2Tray1Legal14Paper": cfg2Tray1Legal14Paper,
       "cfg2Tray1Legal14PaperCurrentValue": cfg2Tray1Legal14PaperCurrentValue,
       "cfg2Tray2Legal14Paper": cfg2Tray2Legal14Paper,
       "cfg2Tray2Legal14PaperCurrentValue": cfg2Tray2Legal14PaperCurrentValue,
       "cfg2Tray3Legal14Paper": cfg2Tray3Legal14Paper,
       "cfg2Tray3Legal14PaperCurrentValue": cfg2Tray3Legal14PaperCurrentValue,
       "cfg2Tray4Legal14Paper": cfg2Tray4Legal14Paper,
       "cfg2Tray4Legal14PaperCurrentValue": cfg2Tray4Legal14PaperCurrentValue,
       "cfg2Tray5Legal14Paper": cfg2Tray5Legal14Paper,
       "cfg2Tray5Legal14PaperCurrentValue": cfg2Tray5Legal14PaperCurrentValue,
       "cfg2Tray6Legal14Paper": cfg2Tray6Legal14Paper,
       "cfg2Tray6Legal14PaperCurrentValue": cfg2Tray6Legal14PaperCurrentValue,
       "cfg2Tray7Legal14Paper": cfg2Tray7Legal14Paper,
       "cfg2Tray7Legal14PaperCurrentValue": cfg2Tray7Legal14PaperCurrentValue,
       "cfg2TrayA5A6Paper": cfg2TrayA5A6Paper,
       "cfg2Tray1A5A6Paper": cfg2Tray1A5A6Paper,
       "cfg2Tray1A5A6PaperCurrentValue": cfg2Tray1A5A6PaperCurrentValue,
       "cfg2Tray2A5A6Paper": cfg2Tray2A5A6Paper,
       "cfg2Tray2A5A6PaperCurrentValue": cfg2Tray2A5A6PaperCurrentValue,
       "cfg2Tray3A5A6Paper": cfg2Tray3A5A6Paper,
       "cfg2Tray3A5A6PaperCurrentValue": cfg2Tray3A5A6PaperCurrentValue,
       "cfg2Tray4A5A6Paper": cfg2Tray4A5A6Paper,
       "cfg2Tray4A5A6PaperCurrentValue": cfg2Tray4A5A6PaperCurrentValue,
       "cfg2Tray5A5A6Paper": cfg2Tray5A5A6Paper,
       "cfg2Tray5A5A6PaperCurrentValue": cfg2Tray5A5A6PaperCurrentValue,
       "cfg2Tray6A5A6Paper": cfg2Tray6A5A6Paper,
       "cfg2Tray6A5A6PaperCurrentValue": cfg2Tray6A5A6PaperCurrentValue,
       "cfg2Tray7A5A6Paper": cfg2Tray7A5A6Paper,
       "cfg2Tray7A5A6PaperCurrentValue": cfg2Tray7A5A6PaperCurrentValue,
       "cfg2PHOutput": cfg2PHOutput,
       "cfg2OutputBin": cfg2OutputBin,
       "cfg2OutputBinCurrentValue": cfg2OutputBinCurrentValue,
       "cfg2PHDuplex": cfg2PHDuplex,
       "cfg2Duplex": cfg2Duplex,
       "cfg2DuplexCurrentValue": cfg2DuplexCurrentValue,
       "cfg2Binding": cfg2Binding,
       "cfg2BindingCurrentValue": cfg2BindingCurrentValue,
       "cfg2PrintProcessControl": cfg2PrintProcessControl,
       "cfg2PPCColor": cfg2PPCColor,
       "cfg2AutoRegistration": cfg2AutoRegistration,
       "cfg2AutoRegistrationCurrentValue": cfg2AutoRegistrationCurrentValue,
       "cfg2PPCDevelopmentControl": cfg2PPCDevelopmentControl,
       "cfg2JobOffset": cfg2JobOffset,
       "cfg2JobOffsetCurrentValue": cfg2JobOffsetCurrentValue,
       "cfg2PPCLEDHeadControl": cfg2PPCLEDHeadControl,
       "cfg2PPCFusingControl": cfg2PPCFusingControl,
       "cfg2PPCPrintPositionControl": cfg2PPCPrintPositionControl,
       "cfg2PPCTonerControl": cfg2PPCTonerControl,
       "cfg2PPCDrumControl": cfg2PPCDrumControl,
       "cfg2HostInterface": cfg2HostInterface,
       "cfg2LocalResources": cfg2LocalResources,
       "cfg2LRCommon": cfg2LRCommon,
       "cfg2StoragePartitionTable": cfg2StoragePartitionTable,
       "cfg2StoragePartitionEntry": cfg2StoragePartitionEntry,
       "cfg2StoragePartitionIndex": cfg2StoragePartitionIndex,
       "cfg2StoragePartitionFree": cfg2StoragePartitionFree,
       "cfg2LRMemory": cfg2LRMemory,
       "cfg2LRHdd": cfg2LRHdd,
       "cfg2Emulation": cfg2Emulation,
       "cfg2Test": cfg2Test,
       "cfg2Menu": cfg2Menu,
       "usage": usage,
       "usagePrinterUnit": usagePrinterUnit,
       "usagePrinterUnitTable": usagePrinterUnitTable,
       "usagePrinterUnitEntry": usagePrinterUnitEntry,
       "usagePrinterUnitIndex": usagePrinterUnitIndex,
       "usagePrinterUnitCounter": usagePrinterUnitCounter,
       "usagePrinterUnitCounterLife": usagePrinterUnitCounterLife,
       "usageTray": usageTray,
       "usageTrayTable": usageTrayTable,
       "usageTrayEntry": usageTrayEntry,
       "usageTrayIndex": usageTrayIndex,
       "usageTrayMaxLevel": usageTrayMaxLevel,
       "usageTrayCounter": usageTrayCounter,
       "usageToner": usageToner,
       "usageTonerTable": usageTonerTable,
       "usageTonerEntry": usageTonerEntry,
       "usageTonerIndex": usageTonerIndex,
       "usageTonerDescription": usageTonerDescription,
       "usageTonerCurrentLevel": usageTonerCurrentLevel,
       "usageTonerMaxLevel": usageTonerMaxLevel,
       "usageTonerLevelUnit": usageTonerLevelUnit,
       "usageDrum": usageDrum,
       "usageDrumTable": usageDrumTable,
       "usageDrumEntry": usageDrumEntry,
       "usageDrumIndex": usageDrumIndex,
       "usageDrumCurrentLevel": usageDrumCurrentLevel,
       "usageDrumMaxLevel": usageDrumMaxLevel,
       "usageBelt": usageBelt,
       "usageBeltTable": usageBeltTable,
       "usageBeltEntry": usageBeltEntry,
       "usageBeltIndex": usageBeltIndex,
       "usageBeltCurrentLevel": usageBeltCurrentLevel,
       "usageBeltMaxLevel": usageBeltMaxLevel,
       "usageFuser": usageFuser,
       "usageFuserTable": usageFuserTable,
       "usageFuserEntry": usageFuserEntry,
       "usageFuserIndex": usageFuserIndex,
       "usageFuserCurrentLevel": usageFuserCurrentLevel,
       "usageFuserMaxLevel": usageFuserMaxLevel,
       "usageOil": usageOil,
       "usageWasteToner": usageWasteToner,
       "niptype2": niptype2,
       "inkjet": inkjet,
       "fax": fax,
       "mfp": mfp,
       "sidm": sidm,
       "printserver": printserver,
       "psVendor": psVendor,
       "psVendorId": psVendorId,
       "psMibVersion": psMibVersion,
       "okips": okips,
       "general": general,
       "genGroupVersion": genGroupVersion,
       "genMIBVersion": genMIBVersion,
       "genProductName": genProductName,
       "genProductNumber": genProductNumber,
       "genSerialNumber": genSerialNumber,
       "genHWAddress": genHWAddress,
       "genCableType": genCableType,
       "genDateCode": genDateCode,
       "genVersion": genVersion,
       "genConfigurationDirty": genConfigurationDirty,
       "genCompanyName": genCompanyName,
       "genCompanyLoc": genCompanyLoc,
       "genCompanyPhone": genCompanyPhone,
       "genCompanyTechSupport": genCompanyTechSupport,
       "genProtocols": genProtocols,
       "genNumProtocols": genNumProtocols,
       "genProtocolTable": genProtocolTable,
       "genProtocolEntry": genProtocolEntry,
       "genProtocolIndex": genProtocolIndex,
       "genProtocolDescr": genProtocolDescr,
       "genProtocolID": genProtocolID,
       "genSysUpTimeString": genSysUpTimeString,
       "commands": commands,
       "cmdGroupVersion": cmdGroupVersion,
       "cmdReset": cmdReset,
       "cmdPrintConfig": cmdPrintConfig,
       "cmdRestoreDefaults": cmdRestoreDefaults,
       "okipsSNMP": okipsSNMP,
       "snmpGroupVersion": snmpGroupVersion,
       "okipsSNMPCommands": okipsSNMPCommands,
       "snmpRestoreDefaults": snmpRestoreDefaults,
       "snmpGetCommunityName": snmpGetCommunityName,
       "snmpSetCommunityName": snmpSetCommunityName,
       "snmpTrapCommunityName": snmpTrapCommunityName,
       "okipsSNMPTrapMasks": okipsSNMPTrapMasks,
       "snmpPrinterTrapMaskUsed": snmpPrinterTrapMaskUsed,
       "snmpPrinter2TrapMaskUsed": snmpPrinter2TrapMaskUsed,
       "snmpTrapMaskTable": snmpTrapMaskTable,
       "snmpTrapEntry": snmpTrapEntry,
       "snmpTrapMaskIndex": snmpTrapMaskIndex,
       "snmpTrapMaskString": snmpTrapMaskString,
       "driver": driver,
       "driverGroupVersion": driverGroupVersion,
       "driverRXPackets": driverRXPackets,
       "driverTXPackets": driverTXPackets,
       "driverRXPacketsUnavailable": driverRXPacketsUnavailable,
       "driverRXPacketErrors": driverRXPacketErrors,
       "driverTXPacketErrors": driverTXPacketErrors,
       "driverTXPacketRetries": driverTXPacketRetries,
       "driverChecksumErrors": driverChecksumErrors,
       "tokenRing": tokenRing,
       "trGroupVersion": trGroupVersion,
       "trCommands": trCommands,
       "trRestoreDefaults": trRestoreDefaults,
       "trConfigure": trConfigure,
       "trPriority": trPriority,
       "trEarlyTokenRelease": trEarlyTokenRelease,
       "trPacketSize": trPacketSize,
       "trRouting": trRouting,
       "trLocallyAdminAddr": trLocallyAdminAddr,
       "printServers": printServers,
       "trapPrinterOnline": trapPrinterOnline,
       "trapPrinterOffline": trapPrinterOffline,
       "trapNoPrinterAttached": trapNoPrinterAttached,
       "trapPrinterTonerLow": trapPrinterTonerLow,
       "trapPrinterPaperOut": trapPrinterPaperOut,
       "trapPrinterPaperJam": trapPrinterPaperJam,
       "trapPrinterDoorOpen": trapPrinterDoorOpen,
       "trapPrinterError": trapPrinterError,
       "psGeneral": psGeneral,
       "psGroupVersion": psGroupVersion,
       "psJetAdminEnabled": psJetAdminEnabled,
       "psVerifyConfiguration": psVerifyConfiguration,
       "psOutput": psOutput,
       "outputGroupVersion": outputGroupVersion,
       "outputCommands": outputCommands,
       "outputRestoreDefaults": outputRestoreDefaults,
       "outputCommandsTable": outputCommandsTable,
       "outputCommandsEntry": outputCommandsEntry,
       "outputCancelCurrentJob": outputCancelCurrentJob,
       "outputConfigure": outputConfigure,
       "outputNumPorts": outputNumPorts,
       "outputTable": outputTable,
       "outputEntry": outputEntry,
       "outputIndex": outputIndex,
       "outputName": outputName,
       "outputStatusString": outputStatusString,
       "outputStatus": outputStatus,
       "outputExtendedStatus": outputExtendedStatus,
       "outputPrinter": outputPrinter,
       "outputLanguageSwitching": outputLanguageSwitching,
       "outputConfigLanguage": outputConfigLanguage,
       "outputPCLString": outputPCLString,
       "outputPSString": outputPSString,
       "outputSetting": outputSetting,
       "outputOwner": outputOwner,
       "outputBIDIStatusEnabled": outputBIDIStatusEnabled,
       "outputPrinterModel": outputPrinterModel,
       "outputPrinterDisplay": outputPrinterDisplay,
       "outputCapabilities": outputCapabilities,
       "outputHandshake": outputHandshake,
       "outputProtocolManager": outputProtocolManager,
       "outputDisplayMask": outputDisplayMask,
       "outputAvailableTrapsMask": outputAvailableTrapsMask,
       "outputJobLog": outputJobLog,
       "outputNumLogEntries": outputNumLogEntries,
       "outputJobLogTable": outputJobLogTable,
       "outputJobLogEntry": outputJobLogEntry,
       "outputJobLogInformation": outputJobLogInformation,
       "outputJobLogTime": outputJobLogTime,
       "outputTotalJobTable": outputTotalJobTable,
       "outputTotalJobEntry": outputTotalJobEntry,
       "outputTotalJobIndex": outputTotalJobIndex,
       "outputTotalJobsLogged": outputTotalJobsLogged,
       "psProtocols": psProtocols,
       "tcpip": tcpip,
       "tcpipGroupVersion": tcpipGroupVersion,
       "tcpipEnabled": tcpipEnabled,
       "tcpipCommands": tcpipCommands,
       "tcpipRestoreDefaults": tcpipRestoreDefaults,
       "tcpipFirmwareUpgrade": tcpipFirmwareUpgrade,
       "tcpipConfigure": tcpipConfigure,
       "tcpipIPAddress": tcpipIPAddress,
       "tcpipDefaultGateway": tcpipDefaultGateway,
       "tcpipSubnetMask": tcpipSubnetMask,
       "tcpipUsingNetProtocols": tcpipUsingNetProtocols,
       "tcpipBootProtocolsEnabled": tcpipBootProtocolsEnabled,
       "tcpipIPAddressSource": tcpipIPAddressSource,
       "tcpipIPAddressServerAddress": tcpipIPAddressServerAddress,
       "tcpipTimeoutChecking": tcpipTimeoutChecking,
       "tcpipNumTraps": tcpipNumTraps,
       "tcpipTrapTable": tcpipTrapTable,
       "tcpipTrapEntry": tcpipTrapEntry,
       "tcpipTrapIndex": tcpipTrapIndex,
       "tcpipTrapDestination": tcpipTrapDestination,
       "tcpipPrinter2TrapMask": tcpipPrinter2TrapMask,
       "tcpipPrinterTrapMask": tcpipPrinterTrapMask,
       "tcpipOutputTrapMask": tcpipOutputTrapMask,
       "tcpipBanners": tcpipBanners,
       "tcpipWinsAddress": tcpipWinsAddress,
       "tcpipWinsAddressSource": tcpipWinsAddressSource,
       "tcpipConfigPassword": tcpipConfigPassword,
       "tcpipTimeoutCheckingValue": tcpipTimeoutCheckingValue,
       "tcpipArpInterval": tcpipArpInterval,
       "tcpipRawPortNumber": tcpipRawPortNumber,
       "tcpipNumSecurity": tcpipNumSecurity,
       "tcpipSecurityTable": tcpipSecurityTable,
       "tcpipSecurityEntry": tcpipSecurityEntry,
       "tcpipSecurityIndex": tcpipSecurityIndex,
       "tcpipSecureStartIPAddress": tcpipSecureStartIPAddress,
       "tcpipSecureEndIPAddress": tcpipSecureEndIPAddress,
       "tcpipSecurePrinterMask": tcpipSecurePrinterMask,
       "tcpipSecureAdminEnabled": tcpipSecureAdminEnabled,
       "tcpipLowBandwidth": tcpipLowBandwidth,
       "tcpipNumLogicalPrinters": tcpipNumLogicalPrinters,
       "tcpipMLPTable": tcpipMLPTable,
       "tcpipMLPEntry": tcpipMLPEntry,
       "tcpipMLPIndex": tcpipMLPIndex,
       "tcpipMLPName": tcpipMLPName,
       "tcpipMLPPort": tcpipMLPPort,
       "tcpipMLPTCPPort": tcpipMLPTCPPort,
       "tcpipMLPPreString": tcpipMLPPreString,
       "tcpipMLPPostString": tcpipMLPPostString,
       "tcpipMLPDeleteBytes": tcpipMLPDeleteBytes,
       "tcpipSmtpServerAddr": tcpipSmtpServerAddr,
       "tcpipNumSmtpDestinations": tcpipNumSmtpDestinations,
       "tcpipSmtpTable": tcpipSmtpTable,
       "tcpipSmtpEntry": tcpipSmtpEntry,
       "tcpipSmtpIndex": tcpipSmtpIndex,
       "tcpipSmtpEmailAddr": tcpipSmtpEmailAddr,
       "tcpipSmtpProtocolMask": tcpipSmtpProtocolMask,
       "tcpipSmtpPrinterMask": tcpipSmtpPrinterMask,
       "tcpipSmtpOutputMask": tcpipSmtpOutputMask,
       "tcpipWebAdminName": tcpipWebAdminName,
       "tcpipWebAdminPassword": tcpipWebAdminPassword,
       "tcpipWebUserName": tcpipWebUserName,
       "tcpipWebUserPassword": tcpipWebUserPassword,
       "tcpipWebHtttpPort": tcpipWebHtttpPort,
       "tcpipWebFaqURL": tcpipWebFaqURL,
       "tcpipWebUpdateURL": tcpipWebUpdateURL,
       "tcpipWebCustomLinkName": tcpipWebCustomLinkName,
       "tcpipWebCustomLinkURL": tcpipWebCustomLinkURL,
       "tcpipPOP3ServerAddress": tcpipPOP3ServerAddress,
       "tcpipPOP3PollInterval": tcpipPOP3PollInterval,
       "tcpipPOP3UserName": tcpipPOP3UserName,
       "tcpipPOP3Password": tcpipPOP3Password,
       "tcpipDomainName": tcpipDomainName,
       "tcpipCapabilities": tcpipCapabilities,
       "tcpipStatus": tcpipStatus,
       "tcpipError": tcpipError,
       "tcpipDisplayMask": tcpipDisplayMask,
       "netware": netware,
       "nwGroupVersion": nwGroupVersion,
       "nwEnabled": nwEnabled,
       "nwCommands": nwCommands,
       "nwRestoreDefaults": nwRestoreDefaults,
       "nwFirmwareUpgrade": nwFirmwareUpgrade,
       "nwConfigure": nwConfigure,
       "nwFrameFormat": nwFrameFormat,
       "nwSetFrameFormat": nwSetFrameFormat,
       "nwMode": nwMode,
       "nwPrintServerName": nwPrintServerName,
       "nwPrintServerPassword": nwPrintServerPassword,
       "nwQueueScanTime": nwQueueScanTime,
       "nwNetworkNumber": nwNetworkNumber,
       "nwMaxFileServers": nwMaxFileServers,
       "nwFileServerTable": nwFileServerTable,
       "nwFileServerEntry": nwFileServerEntry,
       "nwFileServerIndex": nwFileServerIndex,
       "nwFileServerName": nwFileServerName,
       "nwFileServerConnectionStatus": nwFileServerConnectionStatus,
       "nwPortTable": nwPortTable,
       "nwPortEntry": nwPortEntry,
       "nwPortIndex": nwPortIndex,
       "nwPortStatus": nwPortStatus,
       "nwPortPrinterNumber": nwPortPrinterNumber,
       "nwPortFontDownload": nwPortFontDownload,
       "nwPortPCLQueue": nwPortPCLQueue,
       "nwPortPSQueue": nwPortPSQueue,
       "nwPortFormsOn": nwPortFormsOn,
       "nwPortFormNumber": nwPortFormNumber,
       "nwPortNotification": nwPortNotification,
       "nwNumTraps": nwNumTraps,
       "nwTrapTable": nwTrapTable,
       "nwTrapEntry": nwTrapEntry,
       "nwTrapIndex": nwTrapIndex,
       "nwTrapDestination": nwTrapDestination,
       "nwTrapDestinationNet": nwTrapDestinationNet,
       "nwPrinter2TrapMask": nwPrinter2TrapMask,
       "nwPrinterTrapMask": nwPrinterTrapMask,
       "nwOutputTrapMask": nwOutputTrapMask,
       "nwNDSPrintServerName": nwNDSPrintServerName,
       "nwNDSPreferredDSTree": nwNDSPreferredDSTree,
       "nwNDSPreferredDSFileServer": nwNDSPreferredDSFileServer,
       "nwNDSPacketCheckSumEnabled": nwNDSPacketCheckSumEnabled,
       "nwNDSPacketSignatureLevel": nwNDSPacketSignatureLevel,
       "nwAvailablePrintModes": nwAvailablePrintModes,
       "nwDirectPrintEnabled": nwDirectPrintEnabled,
       "nwJAConfig": nwJAConfig,
       "nwDisableSAP": nwDisableSAP,
       "nwStatus": nwStatus,
       "nwError": nwError,
       "nwDisplayMask": nwDisplayMask,
       "vines": vines,
       "bvGroupVersion": bvGroupVersion,
       "bvEnabled": bvEnabled,
       "bvCommands": bvCommands,
       "bvRestoreDefaults": bvRestoreDefaults,
       "bvFirmwareUpgrade": bvFirmwareUpgrade,
       "bvSetSequenceRouting": bvSetSequenceRouting,
       "bvDisableVPMan": bvDisableVPMan,
       "bvConfigure": bvConfigure,
       "bvLoginName": bvLoginName,
       "bvLoginPassword": bvLoginPassword,
       "bvNumberPrintServices": bvNumberPrintServices,
       "bvPrintServiceTable": bvPrintServiceTable,
       "bvPrintServiceEntry": bvPrintServiceEntry,
       "bvPrintServiceIndex": bvPrintServiceIndex,
       "bvPrintServiceName": bvPrintServiceName,
       "bvPrintServiceRouting": bvPrintServiceRouting,
       "bvPnicDescription": bvPnicDescription,
       "bvStatus": bvStatus,
       "bvError": bvError,
       "bvRouting": bvRouting,
       "bvNumPrintServices": bvNumPrintServices,
       "bvPrintServiceStatusTable": bvPrintServiceStatusTable,
       "bvPrintServiceStatusEntry": bvPrintServiceStatusEntry,
       "bvPSStatusIndex": bvPSStatusIndex,
       "bvPSName": bvPSName,
       "bvPSStatus": bvPSStatus,
       "bvPSDestination": bvPSDestination,
       "bvPrinterStatus": bvPrinterStatus,
       "bvJobActive": bvJobActive,
       "bvJobSource": bvJobSource,
       "bvJobTitle": bvJobTitle,
       "bvJobSize": bvJobSize,
       "bvJobNumber": bvJobNumber,
       "lanManager": lanManager,
       "lmGroupVersion": lmGroupVersion,
       "lmEnabled": lmEnabled,
       "eTalk": eTalk,
       "eTalkGroupVersion": eTalkGroupVersion,
       "eTalkEnabled": eTalkEnabled,
       "eTalkCommands": eTalkCommands,
       "eTalkRestoreDefaults": eTalkRestoreDefaults,
       "eTalkConfigure": eTalkConfigure,
       "eTalkNetwork": eTalkNetwork,
       "eTalkNode": eTalkNode,
       "eTalkNumPorts": eTalkNumPorts,
       "eTalkPortTable": eTalkPortTable,
       "eTalkPortEntry": eTalkPortEntry,
       "eTalkPortIndex": eTalkPortIndex,
       "eTalkPortEnable": eTalkPortEnable,
       "eTalkName": eTalkName,
       "eTalkActiveName": eTalkActiveName,
       "eTalkType1": eTalkType1,
       "eTalkType2": eTalkType2,
       "eTalkZone": eTalkZone,
       "eTalkActiveZone": eTalkActiveZone,
       "eTalkStatus": eTalkStatus,
       "eTalkError": eTalkError}
)
