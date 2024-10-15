# SNMP MIB module (WYSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WYSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:29 2024
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

_Wyse_ObjectIdentity = ObjectIdentity
wyse = _Wyse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1)
)
_Old_ObjectIdentity = ObjectIdentity
old = _Old_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 1)
)
_Wysenet_ObjectIdentity = ObjectIdentity
wysenet = _Wysenet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 1, 1)
)
_ThinClient_ObjectIdentity = ObjectIdentity
thinClient = _ThinClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2)
)
_Wbt3_ObjectIdentity = ObjectIdentity
wbt3 = _Wbt3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3)
)
_Wbt3Memory_ObjectIdentity = ObjectIdentity
wbt3Memory = _Wbt3Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1)
)
_Wbt3Ram_ObjectIdentity = ObjectIdentity
wbt3Ram = _Wbt3Ram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 1)
)


class _Wbt3RamNum_Type(Integer32):
    """Custom type wbt3RamNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3RamNum_Type.__name__ = "Integer32"
_Wbt3RamNum_Object = MibScalar
wbt3RamNum = _Wbt3RamNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 1, 1),
    _Wbt3RamNum_Type()
)
wbt3RamNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RamNum.setStatus("mandatory")
_Wbt3RamTable_Object = MibTable
wbt3RamTable = _Wbt3RamTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wbt3RamTable.setStatus("mandatory")
_Wbt3RamEntry_Object = MibTableRow
wbt3RamEntry = _Wbt3RamEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 1, 2, 1)
)
wbt3RamEntry.setIndexNames(
    (0, "WYSE-MIB", "wbt3RamIndex"),
)
if mibBuilder.loadTexts:
    wbt3RamEntry.setStatus("mandatory")
_Wbt3RamIndex_Type = Integer32
_Wbt3RamIndex_Object = MibTableColumn
wbt3RamIndex = _Wbt3RamIndex_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 1, 2, 1, 1),
    _Wbt3RamIndex_Type()
)
wbt3RamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RamIndex.setStatus("mandatory")


class _Wbt3RamType_Type(Integer32):
    """Custom type wbt3RamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("extend", 3),
          ("video", 2))
    )


_Wbt3RamType_Type.__name__ = "Integer32"
_Wbt3RamType_Object = MibTableColumn
wbt3RamType = _Wbt3RamType_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 1, 2, 1, 2),
    _Wbt3RamType_Type()
)
wbt3RamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RamType.setStatus("mandatory")
_Wbt3RamSize_Type = Integer32
_Wbt3RamSize_Object = MibTableColumn
wbt3RamSize = _Wbt3RamSize_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 1, 2, 1, 3),
    _Wbt3RamSize_Type()
)
wbt3RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RamSize.setStatus("mandatory")
_Wbt3Rom_ObjectIdentity = ObjectIdentity
wbt3Rom = _Wbt3Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 2)
)


class _Wbt3RomNum_Type(Integer32):
    """Custom type wbt3RomNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3RomNum_Type.__name__ = "Integer32"
_Wbt3RomNum_Object = MibScalar
wbt3RomNum = _Wbt3RomNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 2, 1),
    _Wbt3RomNum_Type()
)
wbt3RomNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RomNum.setStatus("mandatory")
_Wbt3RomTable_Object = MibTable
wbt3RomTable = _Wbt3RomTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wbt3RomTable.setStatus("mandatory")
_Wbt3RomEntry_Object = MibTableRow
wbt3RomEntry = _Wbt3RomEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 2, 2, 1)
)
wbt3RomEntry.setIndexNames(
    (0, "WYSE-MIB", "wbt3RomIndex"),
)
if mibBuilder.loadTexts:
    wbt3RomEntry.setStatus("mandatory")
_Wbt3RomIndex_Type = Integer32
_Wbt3RomIndex_Object = MibTableColumn
wbt3RomIndex = _Wbt3RomIndex_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 2, 2, 1, 1),
    _Wbt3RomIndex_Type()
)
wbt3RomIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RomIndex.setStatus("mandatory")


class _Wbt3RomType_Type(Integer32):
    """Custom type wbt3RomType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("option", 3),
          ("os", 2))
    )


_Wbt3RomType_Type.__name__ = "Integer32"
_Wbt3RomType_Object = MibTableColumn
wbt3RomType = _Wbt3RomType_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 2, 2, 1, 2),
    _Wbt3RomType_Type()
)
wbt3RomType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RomType.setStatus("mandatory")
_Wbt3RomSize_Type = Integer32
_Wbt3RomSize_Object = MibTableColumn
wbt3RomSize = _Wbt3RomSize_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 1, 2, 2, 1, 3),
    _Wbt3RomSize_Type()
)
wbt3RomSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RomSize.setStatus("mandatory")
_Wbt3PCCard_ObjectIdentity = ObjectIdentity
wbt3PCCard = _Wbt3PCCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 2)
)


class _Wbt3PCCardNum_Type(Integer32):
    """Custom type wbt3PCCardNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3PCCardNum_Type.__name__ = "Integer32"
_Wbt3PCCardNum_Object = MibScalar
wbt3PCCardNum = _Wbt3PCCardNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 2, 1),
    _Wbt3PCCardNum_Type()
)
wbt3PCCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3PCCardNum.setStatus("mandatory")
_Wbt3PCCardTable_Object = MibTable
wbt3PCCardTable = _Wbt3PCCardTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    wbt3PCCardTable.setStatus("mandatory")
_Wbt3PCCardEntry_Object = MibTableRow
wbt3PCCardEntry = _Wbt3PCCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 2, 2, 1)
)
wbt3PCCardEntry.setIndexNames(
    (0, "WYSE-MIB", "wbt3PCCardIndex"),
)
if mibBuilder.loadTexts:
    wbt3PCCardEntry.setStatus("mandatory")
_Wbt3PCCardIndex_Type = Integer32
_Wbt3PCCardIndex_Object = MibTableColumn
wbt3PCCardIndex = _Wbt3PCCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 2, 2, 1, 1),
    _Wbt3PCCardIndex_Type()
)
wbt3PCCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3PCCardIndex.setStatus("mandatory")


class _Wbt3PCCardType_Type(Integer32):
    """Custom type wbt3PCCardType based on Integer32"""
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
              7,
              256)
        )
    )
    namedValues = NamedValues(
        *(("aims", 7),
          ("empty", 256),
          ("fixed-disk", 4),
          ("lan-adapter", 6),
          ("memory", 1),
          ("multifunction", 0),
          ("parallel-port", 3),
          ("serial-port-modem", 2),
          ("video-adaptor", 5))
    )


_Wbt3PCCardType_Type.__name__ = "Integer32"
_Wbt3PCCardType_Object = MibTableColumn
wbt3PCCardType = _Wbt3PCCardType_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 2, 2, 1, 2),
    _Wbt3PCCardType_Type()
)
wbt3PCCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3PCCardType.setStatus("mandatory")
_Wbt3PCCardVendor_Type = DisplayString
_Wbt3PCCardVendor_Object = MibTableColumn
wbt3PCCardVendor = _Wbt3PCCardVendor_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 2, 2, 1, 3),
    _Wbt3PCCardVendor_Type()
)
wbt3PCCardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3PCCardVendor.setStatus("mandatory")
_Wbt3IODevice_ObjectIdentity = ObjectIdentity
wbt3IODevice = _Wbt3IODevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 3)
)


class _Wbt3IODevAttached_Type(Integer32):
    """Custom type wbt3IODevAttached based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Wbt3IODevAttached_Type.__name__ = "Integer32"
_Wbt3IODevAttached_Object = MibScalar
wbt3IODevAttached = _Wbt3IODevAttached_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 3, 1),
    _Wbt3IODevAttached_Type()
)
wbt3IODevAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3IODevAttached.setStatus("mandatory")


class _Wbt3kbLanguage_Type(Integer32):
    """Custom type wbt3kbLanguage based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("belgian-dutch", 16),
          ("belgian-french", 10),
          ("brazilian-abnt", 18),
          ("canadian-eng-multi", 23),
          ("canadian-fr-multi", 22),
          ("canadian-french", 15),
          ("danish", 7),
          ("dutch", 9),
          ("english-uk", 1),
          ("english-us", 0),
          ("finnish", 11),
          ("french", 2),
          ("german", 3),
          ("italian", 5),
          ("italian-142", 19),
          ("japanese", 14),
          ("latin-american", 20),
          ("norwegian", 8),
          ("portuguese", 17),
          ("spanish", 4),
          ("spanish-variation", 24),
          ("swedish", 6),
          ("swiss-french", 12),
          ("swiss-german", 13),
          ("us-international", 21))
    )


_Wbt3kbLanguage_Type.__name__ = "Integer32"
_Wbt3kbLanguage_Object = MibScalar
wbt3kbLanguage = _Wbt3kbLanguage_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 3, 2),
    _Wbt3kbLanguage_Type()
)
wbt3kbLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3kbLanguage.setStatus("mandatory")


class _Wbt3CharacterRepeatDelay_Type(Integer32):
    """Custom type wbt3CharacterRepeatDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(250,
              500,
              750,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("delay-1000", 1000),
          ("delay-250", 250),
          ("delay-500", 500),
          ("delay-750", 750))
    )


_Wbt3CharacterRepeatDelay_Type.__name__ = "Integer32"
_Wbt3CharacterRepeatDelay_Object = MibScalar
wbt3CharacterRepeatDelay = _Wbt3CharacterRepeatDelay_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 3, 3),
    _Wbt3CharacterRepeatDelay_Type()
)
wbt3CharacterRepeatDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3CharacterRepeatDelay.setStatus("mandatory")


class _Wbt3CharacterRepeatRate_Type(Integer32):
    """Custom type wbt3CharacterRepeatRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Wbt3CharacterRepeatRate_Type.__name__ = "Integer32"
_Wbt3CharacterRepeatRate_Object = MibScalar
wbt3CharacterRepeatRate = _Wbt3CharacterRepeatRate_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 3, 4),
    _Wbt3CharacterRepeatRate_Type()
)
wbt3CharacterRepeatRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3CharacterRepeatRate.setStatus("mandatory")
_Wbt3Display_ObjectIdentity = ObjectIdentity
wbt3Display = _Wbt3Display_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4)
)
_Wbt3DispCharacteristic_ObjectIdentity = ObjectIdentity
wbt3DispCharacteristic = _Wbt3DispCharacteristic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 1)
)


class _Wbt3DispFreq_Type(Integer32):
    """Custom type wbt3DispFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Wbt3DispFreq_Type.__name__ = "Integer32"
_Wbt3DispFreq_Object = MibScalar
wbt3DispFreq = _Wbt3DispFreq_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 1, 1),
    _Wbt3DispFreq_Type()
)
wbt3DispFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3DispFreq.setStatus("mandatory")


class _Wbt3DispHorizPix_Type(Integer32):
    """Custom type wbt3DispHorizPix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3DispHorizPix_Type.__name__ = "Integer32"
_Wbt3DispHorizPix_Object = MibScalar
wbt3DispHorizPix = _Wbt3DispHorizPix_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 1, 2),
    _Wbt3DispHorizPix_Type()
)
wbt3DispHorizPix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3DispHorizPix.setStatus("mandatory")


class _Wbt3DispVertPix_Type(Integer32):
    """Custom type wbt3DispVertPix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3DispVertPix_Type.__name__ = "Integer32"
_Wbt3DispVertPix_Object = MibScalar
wbt3DispVertPix = _Wbt3DispVertPix_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 1, 3),
    _Wbt3DispVertPix_Type()
)
wbt3DispVertPix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3DispVertPix.setStatus("mandatory")
_Wbt3DispColor_Type = Integer32
_Wbt3DispColor_Object = MibScalar
wbt3DispColor = _Wbt3DispColor_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 1, 4),
    _Wbt3DispColor_Type()
)
wbt3DispColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DispColor.setStatus("mandatory")


class _Wbt3DispUseDDC_Type(Integer32):
    """Custom type wbt3DispUseDDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3DispUseDDC_Type.__name__ = "Integer32"
_Wbt3DispUseDDC_Object = MibScalar
wbt3DispUseDDC = _Wbt3DispUseDDC_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 1, 5),
    _Wbt3DispUseDDC_Type()
)
wbt3DispUseDDC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3DispUseDDC.setStatus("mandatory")
_Wbt3DispCapability_ObjectIdentity = ObjectIdentity
wbt3DispCapability = _Wbt3DispCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 2)
)


class _Wbt3DispFreqMax_Type(Integer32):
    """Custom type wbt3DispFreqMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Wbt3DispFreqMax_Type.__name__ = "Integer32"
_Wbt3DispFreqMax_Object = MibScalar
wbt3DispFreqMax = _Wbt3DispFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 2, 1),
    _Wbt3DispFreqMax_Type()
)
wbt3DispFreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DispFreqMax.setStatus("mandatory")


class _Wbt3DispHorizPixMax_Type(Integer32):
    """Custom type wbt3DispHorizPixMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3DispHorizPixMax_Type.__name__ = "Integer32"
_Wbt3DispHorizPixMax_Object = MibScalar
wbt3DispHorizPixMax = _Wbt3DispHorizPixMax_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 2, 2),
    _Wbt3DispHorizPixMax_Type()
)
wbt3DispHorizPixMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DispHorizPixMax.setStatus("mandatory")


class _Wbt3DispVertPixMax_Type(Integer32):
    """Custom type wbt3DispVertPixMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3DispVertPixMax_Type.__name__ = "Integer32"
_Wbt3DispVertPixMax_Object = MibScalar
wbt3DispVertPixMax = _Wbt3DispVertPixMax_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 2, 3),
    _Wbt3DispVertPixMax_Type()
)
wbt3DispVertPixMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DispVertPixMax.setStatus("mandatory")
_Wbt3DispColorMax_Type = Integer32
_Wbt3DispColorMax_Object = MibScalar
wbt3DispColorMax = _Wbt3DispColorMax_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 2, 4),
    _Wbt3DispColorMax_Type()
)
wbt3DispColorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DispColorMax.setStatus("mandatory")


class _Wbt3EnergySaver_Type(Integer32):
    """Custom type wbt3EnergySaver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitoroff", 2),
          ("none", 0),
          ("screensaver", 1))
    )


_Wbt3EnergySaver_Type.__name__ = "Integer32"
_Wbt3EnergySaver_Object = MibScalar
wbt3EnergySaver = _Wbt3EnergySaver_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 3),
    _Wbt3EnergySaver_Type()
)
wbt3EnergySaver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3EnergySaver.setStatus("mandatory")


class _Wbt3ScreenTimeOut_Type(Integer32):
    """Custom type wbt3ScreenTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Wbt3ScreenTimeOut_Type.__name__ = "Integer32"
_Wbt3ScreenTimeOut_Object = MibScalar
wbt3ScreenTimeOut = _Wbt3ScreenTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 4),
    _Wbt3ScreenTimeOut_Type()
)
wbt3ScreenTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ScreenTimeOut.setStatus("mandatory")


class _Wbt3TouchScreen_Type(Integer32):
    """Custom type wbt3TouchScreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("com1", 1),
          ("com2", 2),
          ("none", 0))
    )


_Wbt3TouchScreen_Type.__name__ = "Integer32"
_Wbt3TouchScreen_Object = MibScalar
wbt3TouchScreen = _Wbt3TouchScreen_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 4, 5),
    _Wbt3TouchScreen_Type()
)
wbt3TouchScreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TouchScreen.setStatus("mandatory")
_Wbt3DhcpInfo_ObjectIdentity = ObjectIdentity
wbt3DhcpInfo = _Wbt3DhcpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5)
)


class _Wbt3DhcpInfoNum_Type(Integer32):
    """Custom type wbt3DhcpInfoNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3DhcpInfoNum_Type.__name__ = "Integer32"
_Wbt3DhcpInfoNum_Object = MibScalar
wbt3DhcpInfoNum = _Wbt3DhcpInfoNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 1),
    _Wbt3DhcpInfoNum_Type()
)
wbt3DhcpInfoNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DhcpInfoNum.setStatus("mandatory")
_Wbt3DhcpInfoTable_Object = MibTable
wbt3DhcpInfoTable = _Wbt3DhcpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    wbt3DhcpInfoTable.setStatus("mandatory")
_Wbt3DhcpInfoEntry_Object = MibTableRow
wbt3DhcpInfoEntry = _Wbt3DhcpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1)
)
wbt3DhcpInfoEntry.setIndexNames(
    (0, "WYSE-MIB", "wbt3DhcpInfoIndex"),
)
if mibBuilder.loadTexts:
    wbt3DhcpInfoEntry.setStatus("mandatory")
_Wbt3DhcpInfoIndex_Type = Integer32
_Wbt3DhcpInfoIndex_Object = MibTableColumn
wbt3DhcpInfoIndex = _Wbt3DhcpInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 1),
    _Wbt3DhcpInfoIndex_Type()
)
wbt3DhcpInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DhcpInfoIndex.setStatus("mandatory")
_Wbt3InterfaceNum_Type = Integer32
_Wbt3InterfaceNum_Object = MibTableColumn
wbt3InterfaceNum = _Wbt3InterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 2),
    _Wbt3InterfaceNum_Type()
)
wbt3InterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3InterfaceNum.setStatus("mandatory")
_Wbt3ServerIP_Type = DisplayString
_Wbt3ServerIP_Object = MibTableColumn
wbt3ServerIP = _Wbt3ServerIP_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 3),
    _Wbt3ServerIP_Type()
)
wbt3ServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3ServerIP.setStatus("mandatory")
_Wbt3Username_Type = DisplayString
_Wbt3Username_Object = MibTableColumn
wbt3Username = _Wbt3Username_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 4),
    _Wbt3Username_Type()
)
wbt3Username.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3Username.setStatus("mandatory")
_Wbt3Domain_Type = DisplayString
_Wbt3Domain_Object = MibTableColumn
wbt3Domain = _Wbt3Domain_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 5),
    _Wbt3Domain_Type()
)
wbt3Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3Domain.setStatus("mandatory")


class _Wbt3Password_Type(Integer32):
    """Custom type wbt3Password based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nopassword", 0),
          ("password", 1))
    )


_Wbt3Password_Type.__name__ = "Integer32"
_Wbt3Password_Object = MibTableColumn
wbt3Password = _Wbt3Password_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 6),
    _Wbt3Password_Type()
)
wbt3Password.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3Password.setStatus("mandatory")
_Wbt3CommandLine_Type = DisplayString
_Wbt3CommandLine_Object = MibTableColumn
wbt3CommandLine = _Wbt3CommandLine_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 7),
    _Wbt3CommandLine_Type()
)
wbt3CommandLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3CommandLine.setStatus("mandatory")
_Wbt3WorkingDir_Type = DisplayString
_Wbt3WorkingDir_Object = MibTableColumn
wbt3WorkingDir = _Wbt3WorkingDir_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 8),
    _Wbt3WorkingDir_Type()
)
wbt3WorkingDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3WorkingDir.setStatus("mandatory")
_Wbt3FileServer_Type = DisplayString
_Wbt3FileServer_Object = MibTableColumn
wbt3FileServer = _Wbt3FileServer_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 9),
    _Wbt3FileServer_Type()
)
wbt3FileServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3FileServer.setStatus("mandatory")
_Wbt3FileRootPath_Type = DisplayString
_Wbt3FileRootPath_Object = MibTableColumn
wbt3FileRootPath = _Wbt3FileRootPath_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 10),
    _Wbt3FileRootPath_Type()
)
wbt3FileRootPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3FileRootPath.setStatus("mandatory")
_Wbt3TrapServerList_Type = DisplayString
_Wbt3TrapServerList_Object = MibTableColumn
wbt3TrapServerList = _Wbt3TrapServerList_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 11),
    _Wbt3TrapServerList_Type()
)
wbt3TrapServerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3TrapServerList.setStatus("mandatory")


class _Wbt3SetCommunity_Type(Integer32):
    """Custom type wbt3SetCommunity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignored", 0),
          ("notprovided", 2),
          ("provided", 1))
    )


_Wbt3SetCommunity_Type.__name__ = "Integer32"
_Wbt3SetCommunity_Object = MibTableColumn
wbt3SetCommunity = _Wbt3SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 12),
    _Wbt3SetCommunity_Type()
)
wbt3SetCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3SetCommunity.setStatus("mandatory")
_Wbt3RDPstartApp_Type = DisplayString
_Wbt3RDPstartApp_Object = MibScalar
wbt3RDPstartApp = _Wbt3RDPstartApp_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 13),
    _Wbt3RDPstartApp_Type()
)
wbt3RDPstartApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RDPstartApp.setStatus("mandatory")
_Wbt3EmulationMode_Type = DisplayString
_Wbt3EmulationMode_Object = MibScalar
wbt3EmulationMode = _Wbt3EmulationMode_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 14),
    _Wbt3EmulationMode_Type()
)
wbt3EmulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3EmulationMode.setStatus("mandatory")
_Wbt3TerminalID_Type = DisplayString
_Wbt3TerminalID_Object = MibScalar
wbt3TerminalID = _Wbt3TerminalID_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 15),
    _Wbt3TerminalID_Type()
)
wbt3TerminalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3TerminalID.setStatus("mandatory")
_Wbt3VirtualPortServer_Type = DisplayString
_Wbt3VirtualPortServer_Object = MibScalar
wbt3VirtualPortServer = _Wbt3VirtualPortServer_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 2, 1, 16),
    _Wbt3VirtualPortServer_Type()
)
wbt3VirtualPortServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3VirtualPortServer.setStatus("mandatory")
_Wbt3DHCPoptionIDs_ObjectIdentity = ObjectIdentity
wbt3DHCPoptionIDs = _Wbt3DHCPoptionIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3)
)


class _RemoteServer_Type(Integer32):
    """Custom type remoteServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_RemoteServer_Type.__name__ = "Integer32"
_RemoteServer_Object = MibScalar
remoteServer = _RemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 1),
    _RemoteServer_Type()
)
remoteServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteServer.setStatus("mandatory")


class _LogonUserName_Type(Integer32):
    """Custom type logonUserName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_LogonUserName_Type.__name__ = "Integer32"
_LogonUserName_Object = MibScalar
logonUserName = _LogonUserName_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 2),
    _LogonUserName_Type()
)
logonUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logonUserName.setStatus("mandatory")


class _Domain_Type(Integer32):
    """Custom type domain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_Domain_Type.__name__ = "Integer32"
_Domain_Object = MibScalar
domain = _Domain_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 3),
    _Domain_Type()
)
domain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domain.setStatus("mandatory")


class _Password_Type(Integer32):
    """Custom type password based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_Password_Type.__name__ = "Integer32"
_Password_Object = MibScalar
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 4),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("mandatory")


class _CommandLine_Type(Integer32):
    """Custom type commandLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_CommandLine_Type.__name__ = "Integer32"
_CommandLine_Object = MibScalar
commandLine = _CommandLine_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 5),
    _CommandLine_Type()
)
commandLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandLine.setStatus("mandatory")


class _WorkingDirectory_Type(Integer32):
    """Custom type workingDirectory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_WorkingDirectory_Type.__name__ = "Integer32"
_WorkingDirectory_Object = MibScalar
workingDirectory = _WorkingDirectory_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 6),
    _WorkingDirectory_Type()
)
workingDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    workingDirectory.setStatus("mandatory")


class _RDPStartupApp_Type(Integer32):
    """Custom type rDPStartupApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_RDPStartupApp_Type.__name__ = "Integer32"
_RDPStartupApp_Object = MibScalar
rDPStartupApp = _RDPStartupApp_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 7),
    _RDPStartupApp_Type()
)
rDPStartupApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rDPStartupApp.setStatus("mandatory")


class _FTPFileServer_Type(Integer32):
    """Custom type fTPFileServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_FTPFileServer_Type.__name__ = "Integer32"
_FTPFileServer_Object = MibScalar
fTPFileServer = _FTPFileServer_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 8),
    _FTPFileServer_Type()
)
fTPFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTPFileServer.setStatus("mandatory")


class _FTPRootPath_Type(Integer32):
    """Custom type fTPRootPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_FTPRootPath_Type.__name__ = "Integer32"
_FTPRootPath_Object = MibScalar
fTPRootPath = _FTPRootPath_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 9),
    _FTPRootPath_Type()
)
fTPRootPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTPRootPath.setStatus("mandatory")


class _TrapServerList_Type(Integer32):
    """Custom type trapServerList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_TrapServerList_Type.__name__ = "Integer32"
_TrapServerList_Object = MibScalar
trapServerList = _TrapServerList_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 10),
    _TrapServerList_Type()
)
trapServerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerList.setStatus("mandatory")


class _SetCommunity_Type(Integer32):
    """Custom type setCommunity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_SetCommunity_Type.__name__ = "Integer32"
_SetCommunity_Object = MibScalar
setCommunity = _SetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 11),
    _SetCommunity_Type()
)
setCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCommunity.setStatus("mandatory")


class _EmulationMode_Type(Integer32):
    """Custom type emulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_EmulationMode_Type.__name__ = "Integer32"
_EmulationMode_Object = MibScalar
emulationMode = _EmulationMode_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 12),
    _EmulationMode_Type()
)
emulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emulationMode.setStatus("mandatory")


class _TerminalID_Type(Integer32):
    """Custom type terminalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_TerminalID_Type.__name__ = "Integer32"
_TerminalID_Object = MibScalar
terminalID = _TerminalID_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 13),
    _TerminalID_Type()
)
terminalID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalID.setStatus("mandatory")


class _VirtualPortServer_Type(Integer32):
    """Custom type virtualPortServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 254),
    )


_VirtualPortServer_Type.__name__ = "Integer32"
_VirtualPortServer_Object = MibScalar
virtualPortServer = _VirtualPortServer_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 5, 3, 14),
    _VirtualPortServer_Type()
)
virtualPortServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualPortServer.setStatus("mandatory")
_Wbt3BuildInfo_ObjectIdentity = ObjectIdentity
wbt3BuildInfo = _Wbt3BuildInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6)
)
_Wbt3CurrentInfo_ObjectIdentity = ObjectIdentity
wbt3CurrentInfo = _Wbt3CurrentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1)
)


class _Wbt3CurInfoNum_Type(Integer32):
    """Custom type wbt3CurInfoNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3CurInfoNum_Type.__name__ = "Integer32"
_Wbt3CurInfoNum_Object = MibScalar
wbt3CurInfoNum = _Wbt3CurInfoNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1, 1),
    _Wbt3CurInfoNum_Type()
)
wbt3CurInfoNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3CurInfoNum.setStatus("mandatory")
_Wbt3CurInfoTable_Object = MibTable
wbt3CurInfoTable = _Wbt3CurInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    wbt3CurInfoTable.setStatus("mandatory")
_Wbt3CurInfoEntry_Object = MibTableRow
wbt3CurInfoEntry = _Wbt3CurInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1, 2, 1)
)
wbt3CurInfoEntry.setIndexNames(
    (0, "WYSE-MIB", "wbt3DhcpInfoIndex"),
)
if mibBuilder.loadTexts:
    wbt3CurInfoEntry.setStatus("mandatory")
_Wbt3CurInfoIndex_Type = Integer32
_Wbt3CurInfoIndex_Object = MibTableColumn
wbt3CurInfoIndex = _Wbt3CurInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1, 2, 1, 1),
    _Wbt3CurInfoIndex_Type()
)
wbt3CurInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3CurInfoIndex.setStatus("mandatory")
_Wbt3CurBuildNum_Type = DisplayString
_Wbt3CurBuildNum_Object = MibTableColumn
wbt3CurBuildNum = _Wbt3CurBuildNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1, 2, 1, 2),
    _Wbt3CurBuildNum_Type()
)
wbt3CurBuildNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3CurBuildNum.setStatus("mandatory")
_Wbt3CurOEMBuildNum_Type = DisplayString
_Wbt3CurOEMBuildNum_Object = MibTableColumn
wbt3CurOEMBuildNum = _Wbt3CurOEMBuildNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1, 2, 1, 3),
    _Wbt3CurOEMBuildNum_Type()
)
wbt3CurOEMBuildNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3CurOEMBuildNum.setStatus("mandatory")
_Wbt3CurModBuildDate_Type = DisplayString
_Wbt3CurModBuildDate_Object = MibTableColumn
wbt3CurModBuildDate = _Wbt3CurModBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1, 2, 1, 4),
    _Wbt3CurModBuildDate_Type()
)
wbt3CurModBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3CurModBuildDate.setStatus("mandatory")
_Wbt3CurOEM_Type = DisplayString
_Wbt3CurOEM_Object = MibTableColumn
wbt3CurOEM = _Wbt3CurOEM_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1, 2, 1, 5),
    _Wbt3CurOEM_Type()
)
wbt3CurOEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3CurOEM.setStatus("mandatory")
_Wbt3CurHWPlatform_Type = DisplayString
_Wbt3CurHWPlatform_Object = MibTableColumn
wbt3CurHWPlatform = _Wbt3CurHWPlatform_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1, 2, 1, 6),
    _Wbt3CurHWPlatform_Type()
)
wbt3CurHWPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3CurHWPlatform.setStatus("mandatory")
_Wbt3CurOS_Type = DisplayString
_Wbt3CurOS_Object = MibTableColumn
wbt3CurOS = _Wbt3CurOS_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 1, 2, 1, 7),
    _Wbt3CurOS_Type()
)
wbt3CurOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3CurOS.setStatus("mandatory")
_Wbt3DhcpUpdateInfo_ObjectIdentity = ObjectIdentity
wbt3DhcpUpdateInfo = _Wbt3DhcpUpdateInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 2)
)


class _Wbt3DUpInfoNum_Type(Integer32):
    """Custom type wbt3DUpInfoNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3DUpInfoNum_Type.__name__ = "Integer32"
_Wbt3DUpInfoNum_Object = MibScalar
wbt3DUpInfoNum = _Wbt3DUpInfoNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 2, 1),
    _Wbt3DUpInfoNum_Type()
)
wbt3DUpInfoNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DUpInfoNum.setStatus("mandatory")
_Wbt3DUpInfoTable_Object = MibTable
wbt3DUpInfoTable = _Wbt3DUpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 2, 2)
)
if mibBuilder.loadTexts:
    wbt3DUpInfoTable.setStatus("mandatory")
_Wbt3DUpInfoEntry_Object = MibTableRow
wbt3DUpInfoEntry = _Wbt3DUpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 2, 2, 1)
)
wbt3DUpInfoEntry.setIndexNames(
    (0, "WYSE-MIB", "wbt3DUpInfoIndex"),
)
if mibBuilder.loadTexts:
    wbt3DUpInfoEntry.setStatus("mandatory")
_Wbt3DUpInfoIndex_Type = Integer32
_Wbt3DUpInfoIndex_Object = MibTableColumn
wbt3DUpInfoIndex = _Wbt3DUpInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 2, 2, 1, 1),
    _Wbt3DUpInfoIndex_Type()
)
wbt3DUpInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DUpInfoIndex.setStatus("mandatory")
_Wbt3DUpBuildNum_Type = DisplayString
_Wbt3DUpBuildNum_Object = MibTableColumn
wbt3DUpBuildNum = _Wbt3DUpBuildNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 2, 2, 1, 2),
    _Wbt3DUpBuildNum_Type()
)
wbt3DUpBuildNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DUpBuildNum.setStatus("mandatory")
_Wbt3DUpOEMBuildNum_Type = DisplayString
_Wbt3DUpOEMBuildNum_Object = MibTableColumn
wbt3DUpOEMBuildNum = _Wbt3DUpOEMBuildNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 2, 2, 1, 3),
    _Wbt3DUpOEMBuildNum_Type()
)
wbt3DUpOEMBuildNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DUpOEMBuildNum.setStatus("mandatory")
_Wbt3DUpModBuildDate_Type = DisplayString
_Wbt3DUpModBuildDate_Object = MibTableColumn
wbt3DUpModBuildDate = _Wbt3DUpModBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 2, 2, 1, 4),
    _Wbt3DUpModBuildDate_Type()
)
wbt3DUpModBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DUpModBuildDate.setStatus("mandatory")
_Wbt3DUpOEMBuildDate_Type = DisplayString
_Wbt3DUpOEMBuildDate_Object = MibScalar
wbt3DUpOEMBuildDate = _Wbt3DUpOEMBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 6, 2, 2, 1, 5),
    _Wbt3DUpOEMBuildDate_Type()
)
wbt3DUpOEMBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3DUpOEMBuildDate.setStatus("mandatory")
_Wbt3CustomFields_ObjectIdentity = ObjectIdentity
wbt3CustomFields = _Wbt3CustomFields_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 7)
)
_Wbt3CustomField1_Type = DisplayString
_Wbt3CustomField1_Object = MibScalar
wbt3CustomField1 = _Wbt3CustomField1_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 7, 1),
    _Wbt3CustomField1_Type()
)
wbt3CustomField1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3CustomField1.setStatus("mandatory")
_Wbt3CustomField2_Type = DisplayString
_Wbt3CustomField2_Object = MibScalar
wbt3CustomField2 = _Wbt3CustomField2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 7, 2),
    _Wbt3CustomField2_Type()
)
wbt3CustomField2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3CustomField2.setStatus("mandatory")
_Wbt3CustomField3_Type = DisplayString
_Wbt3CustomField3_Object = MibScalar
wbt3CustomField3 = _Wbt3CustomField3_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 7, 3),
    _Wbt3CustomField3_Type()
)
wbt3CustomField3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3CustomField3.setStatus("mandatory")
_Wbt3Administration_ObjectIdentity = ObjectIdentity
wbt3Administration = _Wbt3Administration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8)
)
_Wbt3UpDnLoad_ObjectIdentity = ObjectIdentity
wbt3UpDnLoad = _Wbt3UpDnLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1)
)


class _Wbt3UpDnLoadNum_Type(Integer32):
    """Custom type wbt3UpDnLoadNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3UpDnLoadNum_Type.__name__ = "Integer32"
_Wbt3UpDnLoadNum_Object = MibScalar
wbt3UpDnLoadNum = _Wbt3UpDnLoadNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 1),
    _Wbt3UpDnLoadNum_Type()
)
wbt3UpDnLoadNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UpDnLoadNum.setStatus("mandatory")
_Wbt3UpDnLoadTable_Object = MibTable
wbt3UpDnLoadTable = _Wbt3UpDnLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2)
)
if mibBuilder.loadTexts:
    wbt3UpDnLoadTable.setStatus("mandatory")
_Wbt3UpDnLoadEntry_Object = MibTableRow
wbt3UpDnLoadEntry = _Wbt3UpDnLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2, 1)
)
wbt3UpDnLoadEntry.setIndexNames(
    (0, "WYSE-MIB", "wbt3UpDnLoadIndex"),
)
if mibBuilder.loadTexts:
    wbt3UpDnLoadEntry.setStatus("mandatory")
_Wbt3UpDnLoadIndex_Type = Integer32
_Wbt3UpDnLoadIndex_Object = MibTableColumn
wbt3UpDnLoadIndex = _Wbt3UpDnLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2, 1, 1),
    _Wbt3UpDnLoadIndex_Type()
)
wbt3UpDnLoadIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UpDnLoadIndex.setStatus("mandatory")
_Wbt3UpDnLoadId_Type = DisplayString
_Wbt3UpDnLoadId_Object = MibTableColumn
wbt3UpDnLoadId = _Wbt3UpDnLoadId_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2, 1, 2),
    _Wbt3UpDnLoadId_Type()
)
wbt3UpDnLoadId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UpDnLoadId.setStatus("mandatory")


class _Wbt3UpDnLoadOp_Type(Integer32):
    """Custom type wbt3UpDnLoadOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 0))
    )


_Wbt3UpDnLoadOp_Type.__name__ = "Integer32"
_Wbt3UpDnLoadOp_Object = MibTableColumn
wbt3UpDnLoadOp = _Wbt3UpDnLoadOp_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2, 1, 3),
    _Wbt3UpDnLoadOp_Type()
)
wbt3UpDnLoadOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UpDnLoadOp.setStatus("mandatory")
_Wbt3UpDnLoadSrcFile_Type = DisplayString
_Wbt3UpDnLoadSrcFile_Object = MibTableColumn
wbt3UpDnLoadSrcFile = _Wbt3UpDnLoadSrcFile_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2, 1, 4),
    _Wbt3UpDnLoadSrcFile_Type()
)
wbt3UpDnLoadSrcFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UpDnLoadSrcFile.setStatus("mandatory")
_Wbt3UpDnLoadDstFile_Type = DisplayString
_Wbt3UpDnLoadDstFile_Object = MibTableColumn
wbt3UpDnLoadDstFile = _Wbt3UpDnLoadDstFile_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2, 1, 5),
    _Wbt3UpDnLoadDstFile_Type()
)
wbt3UpDnLoadDstFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UpDnLoadDstFile.setStatus("mandatory")


class _Wbt3UpDnLoadFileType_Type(Integer32):
    """Custom type wbt3UpDnLoadFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 0))
    )


_Wbt3UpDnLoadFileType_Type.__name__ = "Integer32"
_Wbt3UpDnLoadFileType_Object = MibTableColumn
wbt3UpDnLoadFileType = _Wbt3UpDnLoadFileType_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2, 1, 6),
    _Wbt3UpDnLoadFileType_Type()
)
wbt3UpDnLoadFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UpDnLoadFileType.setStatus("mandatory")


class _Wbt3UpDnLoadProtocol_Type(Integer32):
    """Custom type wbt3UpDnLoadProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 0),
          ("tftp", 1))
    )


_Wbt3UpDnLoadProtocol_Type.__name__ = "Integer32"
_Wbt3UpDnLoadProtocol_Object = MibTableColumn
wbt3UpDnLoadProtocol = _Wbt3UpDnLoadProtocol_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2, 1, 7),
    _Wbt3UpDnLoadProtocol_Type()
)
wbt3UpDnLoadProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UpDnLoadProtocol.setStatus("mandatory")
_Wbt3UpDnLoadFServer_Type = DisplayString
_Wbt3UpDnLoadFServer_Object = MibTableColumn
wbt3UpDnLoadFServer = _Wbt3UpDnLoadFServer_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2, 1, 8),
    _Wbt3UpDnLoadFServer_Type()
)
wbt3UpDnLoadFServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UpDnLoadFServer.setStatus("mandatory")


class _Wbt3UpDnLoadTimeFlag_Type(Integer32):
    """Custom type wbt3UpDnLoadTimeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("immediate", 0)
    )


_Wbt3UpDnLoadTimeFlag_Type.__name__ = "Integer32"
_Wbt3UpDnLoadTimeFlag_Object = MibTableColumn
wbt3UpDnLoadTimeFlag = _Wbt3UpDnLoadTimeFlag_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 2, 1, 9),
    _Wbt3UpDnLoadTimeFlag_Type()
)
wbt3UpDnLoadTimeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UpDnLoadTimeFlag.setStatus("mandatory")


class _Wbt3AcceptReq_Type(Integer32):
    """Custom type wbt3AcceptReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AcceptReq_Type.__name__ = "Integer32"
_Wbt3AcceptReq_Object = MibScalar
wbt3AcceptReq = _Wbt3AcceptReq_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 3),
    _Wbt3AcceptReq_Type()
)
wbt3AcceptReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AcceptReq.setStatus("mandatory")


class _Wbt3SubmitLoadJob_Type(Integer32):
    """Custom type wbt3SubmitLoadJob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notready", 0),
          ("ready", 1))
    )


_Wbt3SubmitLoadJob_Type.__name__ = "Integer32"
_Wbt3SubmitLoadJob_Object = MibScalar
wbt3SubmitLoadJob = _Wbt3SubmitLoadJob_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 1, 4),
    _Wbt3SubmitLoadJob_Type()
)
wbt3SubmitLoadJob.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3SubmitLoadJob.setStatus("mandatory")
_Wbt3Action_ObjectIdentity = ObjectIdentity
wbt3Action = _Wbt3Action_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 2)
)


class _Wbt3RebootRequest_Type(Integer32):
    """Custom type wbt3RebootRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noreboot", 0),
          ("rebootnow", 1))
    )


_Wbt3RebootRequest_Type.__name__ = "Integer32"
_Wbt3RebootRequest_Object = MibScalar
wbt3RebootRequest = _Wbt3RebootRequest_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 2, 1),
    _Wbt3RebootRequest_Type()
)
wbt3RebootRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3RebootRequest.setStatus("mandatory")


class _Wbt3ResetToFactoryDefault_Type(Integer32):
    """Custom type wbt3ResetToFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 0),
          ("resetnow", 1))
    )


_Wbt3ResetToFactoryDefault_Type.__name__ = "Integer32"
_Wbt3ResetToFactoryDefault_Object = MibScalar
wbt3ResetToFactoryDefault = _Wbt3ResetToFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 2, 2),
    _Wbt3ResetToFactoryDefault_Type()
)
wbt3ResetToFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ResetToFactoryDefault.setStatus("mandatory")
_Wbt3FTPsetting_ObjectIdentity = ObjectIdentity
wbt3FTPsetting = _Wbt3FTPsetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 3)
)
_Wbt3ServerName_Type = DisplayString
_Wbt3ServerName_Object = MibScalar
wbt3ServerName = _Wbt3ServerName_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 3, 1),
    _Wbt3ServerName_Type()
)
wbt3ServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ServerName.setStatus("mandatory")
_Wbt3Directory_Type = DisplayString
_Wbt3Directory_Object = MibScalar
wbt3Directory = _Wbt3Directory_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 3, 2),
    _Wbt3Directory_Type()
)
wbt3Directory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Directory.setStatus("mandatory")
_Wbt3UserID_Type = DisplayString
_Wbt3UserID_Object = MibScalar
wbt3UserID = _Wbt3UserID_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 3, 3),
    _Wbt3UserID_Type()
)
wbt3UserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UserID.setStatus("mandatory")
_Wbt3Password2_Type = DisplayString
_Wbt3Password2_Object = MibScalar
wbt3Password2 = _Wbt3Password2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 3, 4),
    _Wbt3Password2_Type()
)
wbt3Password2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Password2.setStatus("mandatory")


class _Wbt3SavePassword_Type(Integer32):
    """Custom type wbt3SavePassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3SavePassword_Type.__name__ = "Integer32"
_Wbt3SavePassword_Object = MibScalar
wbt3SavePassword = _Wbt3SavePassword_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 3, 5),
    _Wbt3SavePassword_Type()
)
wbt3SavePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3SavePassword.setStatus("mandatory")


class _Wbt3InfoLocation_Type(Integer32):
    """Custom type wbt3InfoLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("usedhcpinfo", 1),
          ("uselocalinfo", 0))
    )


_Wbt3InfoLocation_Type.__name__ = "Integer32"
_Wbt3InfoLocation_Object = MibScalar
wbt3InfoLocation = _Wbt3InfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 3, 6),
    _Wbt3InfoLocation_Type()
)
wbt3InfoLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3InfoLocation.setStatus("mandatory")


class _Wbt3SNMPupdate_Type(Integer32):
    """Custom type wbt3SNMPupdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3SNMPupdate_Type.__name__ = "Integer32"
_Wbt3SNMPupdate_Object = MibScalar
wbt3SNMPupdate = _Wbt3SNMPupdate_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 4),
    _Wbt3SNMPupdate_Type()
)
wbt3SNMPupdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3SNMPupdate.setStatus("mandatory")


class _Wbt3DHCPupdate_Type(Integer32):
    """Custom type wbt3DHCPupdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3DHCPupdate_Type.__name__ = "Integer32"
_Wbt3DHCPupdate_Object = MibScalar
wbt3DHCPupdate = _Wbt3DHCPupdate_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 5),
    _Wbt3DHCPupdate_Type()
)
wbt3DHCPupdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3DHCPupdate.setStatus("mandatory")
_Wbt3Security_ObjectIdentity = ObjectIdentity
wbt3Security = _Wbt3Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7)
)


class _Wbt3SecurityEnable_Type(Integer32):
    """Custom type wbt3SecurityEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3SecurityEnable_Type.__name__ = "Integer32"
_Wbt3SecurityEnable_Object = MibScalar
wbt3SecurityEnable = _Wbt3SecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7, 1),
    _Wbt3SecurityEnable_Type()
)
wbt3SecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3SecurityEnable.setStatus("mandatory")


class _Wbt3HideConfigTab_Type(Integer32):
    """Custom type wbt3HideConfigTab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3HideConfigTab_Type.__name__ = "Integer32"
_Wbt3HideConfigTab_Object = MibScalar
wbt3HideConfigTab = _Wbt3HideConfigTab_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7, 2),
    _Wbt3HideConfigTab_Type()
)
wbt3HideConfigTab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3HideConfigTab.setStatus("mandatory")


class _Wbt3FailOverEnable_Type(Integer32):
    """Custom type wbt3FailOverEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3FailOverEnable_Type.__name__ = "Integer32"
_Wbt3FailOverEnable_Object = MibScalar
wbt3FailOverEnable = _Wbt3FailOverEnable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7, 3),
    _Wbt3FailOverEnable_Type()
)
wbt3FailOverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3FailOverEnable.setStatus("mandatory")


class _Wbt3MultipleConnect_Type(Integer32):
    """Custom type wbt3MultipleConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3MultipleConnect_Type.__name__ = "Integer32"
_Wbt3MultipleConnect_Object = MibScalar
wbt3MultipleConnect = _Wbt3MultipleConnect_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7, 4),
    _Wbt3MultipleConnect_Type()
)
wbt3MultipleConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3MultipleConnect.setStatus("mandatory")


class _Wbt3PingBeforeConnect_Type(Integer32):
    """Custom type wbt3PingBeforeConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3PingBeforeConnect_Type.__name__ = "Integer32"
_Wbt3PingBeforeConnect_Object = MibScalar
wbt3PingBeforeConnect = _Wbt3PingBeforeConnect_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7, 5),
    _Wbt3PingBeforeConnect_Type()
)
wbt3PingBeforeConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3PingBeforeConnect.setStatus("mandatory")


class _Wbt3Verbose_Type(Integer32):
    """Custom type wbt3Verbose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3Verbose_Type.__name__ = "Integer32"
_Wbt3Verbose_Object = MibScalar
wbt3Verbose = _Wbt3Verbose_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7, 6),
    _Wbt3Verbose_Type()
)
wbt3Verbose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Verbose.setStatus("mandatory")


class _Wbt3AutoLoginEnable_Type(Integer32):
    """Custom type wbt3AutoLoginEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AutoLoginEnable_Type.__name__ = "Integer32"
_Wbt3AutoLoginEnable_Object = MibScalar
wbt3AutoLoginEnable = _Wbt3AutoLoginEnable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7, 7),
    _Wbt3AutoLoginEnable_Type()
)
wbt3AutoLoginEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoLoginEnable.setStatus("mandatory")
_Wbt3AutoLoginUserName_Type = DisplayString
_Wbt3AutoLoginUserName_Object = MibScalar
wbt3AutoLoginUserName = _Wbt3AutoLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7, 8),
    _Wbt3AutoLoginUserName_Type()
)
wbt3AutoLoginUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoLoginUserName.setStatus("mandatory")


class _Wbt3SingleButtonConnect_Type(Integer32):
    """Custom type wbt3SingleButtonConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3SingleButtonConnect_Type.__name__ = "Integer32"
_Wbt3SingleButtonConnect_Object = MibScalar
wbt3SingleButtonConnect = _Wbt3SingleButtonConnect_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7, 9),
    _Wbt3SingleButtonConnect_Type()
)
wbt3SingleButtonConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3SingleButtonConnect.setStatus("mandatory")


class _Wbt3AutoFailRecovery_Type(Integer32):
    """Custom type wbt3AutoFailRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AutoFailRecovery_Type.__name__ = "Integer32"
_Wbt3AutoFailRecovery_Object = MibScalar
wbt3AutoFailRecovery = _Wbt3AutoFailRecovery_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 8, 7, 10),
    _Wbt3AutoFailRecovery_Type()
)
wbt3AutoFailRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoFailRecovery.setStatus("mandatory")
_Wbt3TrapsInfo_ObjectIdentity = ObjectIdentity
wbt3TrapsInfo = _Wbt3TrapsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 9)
)


class _Wbt3TrapStatus_Type(Integer32):
    """Custom type wbt3TrapStatus based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("ls-done", 0),
          ("ls-done-sameversion", 1),
          ("ls-fail-badkey", 28),
          ("ls-fail-checksum", 15),
          ("ls-fail-dir", 7),
          ("ls-fail-dnld-blocked", 5),
          ("ls-fail-dnld-flash", 17),
          ("ls-fail-filenotfound", 6),
          ("ls-fail-flasherror", 16),
          ("ls-fail-nomem", 11),
          ("ls-fail-noresource", 12),
          ("ls-fail-norflash", 19),
          ("ls-fail-noserv", 9),
          ("ls-fail-notbundle", 14),
          ("ls-fail-noupd", 4),
          ("ls-fail-paraminifilenotfound", 26),
          ("ls-fail-parsereg", 21),
          ("ls-fail-parsereg-osincomp", 24),
          ("ls-fail-parsereg-platfincomp", 23),
          ("ls-fail-parsereg-verincomp", 22),
          ("ls-fail-prot", 10),
          ("ls-fail-protnsupport", 20),
          ("ls-fail-reset-defaultfactory", 25),
          ("ls-fail-resolvename", 13),
          ("ls-fail-shutdown", 3),
          ("ls-fail-upld-blocked", 8),
          ("ls-fail-usercancel", 18),
          ("ls-invalid-bootstrap", 27),
          ("ls-notready", 2))
    )


_Wbt3TrapStatus_Type.__name__ = "Integer32"
_Wbt3TrapStatus_Object = MibScalar
wbt3TrapStatus = _Wbt3TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 9, 1),
    _Wbt3TrapStatus_Type()
)
wbt3TrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3TrapStatus.setStatus("mandatory")
_Wbt3TrapReqId_Type = DisplayString
_Wbt3TrapReqId_Object = MibScalar
wbt3TrapReqId = _Wbt3TrapReqId_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 9, 2),
    _Wbt3TrapReqId_Type()
)
wbt3TrapReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3TrapReqId.setStatus("mandatory")
_Wbt3TrapServers_ObjectIdentity = ObjectIdentity
wbt3TrapServers = _Wbt3TrapServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 9, 3)
)
_Wbt3TrapServer1_Type = DisplayString
_Wbt3TrapServer1_Object = MibScalar
wbt3TrapServer1 = _Wbt3TrapServer1_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 9, 3, 1),
    _Wbt3TrapServer1_Type()
)
wbt3TrapServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TrapServer1.setStatus("mandatory")
_Wbt3TrapServer2_Type = DisplayString
_Wbt3TrapServer2_Object = MibScalar
wbt3TrapServer2 = _Wbt3TrapServer2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 9, 3, 2),
    _Wbt3TrapServer2_Type()
)
wbt3TrapServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TrapServer2.setStatus("mandatory")
_Wbt3TrapServer3_Type = DisplayString
_Wbt3TrapServer3_Object = MibScalar
wbt3TrapServer3 = _Wbt3TrapServer3_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 9, 3, 3),
    _Wbt3TrapServer3_Type()
)
wbt3TrapServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TrapServer3.setStatus("mandatory")
_Wbt3TrapServer4_Type = DisplayString
_Wbt3TrapServer4_Object = MibScalar
wbt3TrapServer4 = _Wbt3TrapServer4_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 9, 3, 4),
    _Wbt3TrapServer4_Type()
)
wbt3TrapServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TrapServer4.setStatus("mandatory")
_Wbt3MibRev_ObjectIdentity = ObjectIdentity
wbt3MibRev = _Wbt3MibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 10)
)


class _Wbt3MibRevMajor_Type(Integer32):
    """Custom type wbt3MibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3MibRevMajor_Type.__name__ = "Integer32"
_Wbt3MibRevMajor_Object = MibScalar
wbt3MibRevMajor = _Wbt3MibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 10, 1),
    _Wbt3MibRevMajor_Type()
)
wbt3MibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3MibRevMajor.setStatus("mandatory")


class _Wbt3MibRevMinor_Type(Integer32):
    """Custom type wbt3MibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3MibRevMinor_Type.__name__ = "Integer32"
_Wbt3MibRevMinor_Object = MibScalar
wbt3MibRevMinor = _Wbt3MibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 10, 2),
    _Wbt3MibRevMinor_Type()
)
wbt3MibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3MibRevMinor.setStatus("mandatory")
_Wbt3Network_ObjectIdentity = ObjectIdentity
wbt3Network = _Wbt3Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11)
)


class _Wbt3NetworkNum_Type(Integer32):
    """Custom type wbt3NetworkNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3NetworkNum_Type.__name__ = "Integer32"
_Wbt3NetworkNum_Object = MibScalar
wbt3NetworkNum = _Wbt3NetworkNum_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 1),
    _Wbt3NetworkNum_Type()
)
wbt3NetworkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3NetworkNum.setStatus("mandatory")
_Wbt3NetworkTable_Object = MibTable
wbt3NetworkTable = _Wbt3NetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2)
)
if mibBuilder.loadTexts:
    wbt3NetworkTable.setStatus("mandatory")
_Wbt3NetworkEntry_Object = MibTableRow
wbt3NetworkEntry = _Wbt3NetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1)
)
wbt3NetworkEntry.setIndexNames(
    (0, "WYSE-MIB", "wbt3NetworkIndex"),
)
if mibBuilder.loadTexts:
    wbt3NetworkEntry.setStatus("mandatory")
_Wbt3NetworkIndex_Type = Integer32
_Wbt3NetworkIndex_Object = MibTableColumn
wbt3NetworkIndex = _Wbt3NetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 1),
    _Wbt3NetworkIndex_Type()
)
wbt3NetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3NetworkIndex.setStatus("mandatory")


class _Wbt3dhcpEnable_Type(Integer32):
    """Custom type wbt3dhcpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3dhcpEnable_Type.__name__ = "Integer32"
_Wbt3dhcpEnable_Object = MibScalar
wbt3dhcpEnable = _Wbt3dhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 2),
    _Wbt3dhcpEnable_Type()
)
wbt3dhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3dhcpEnable.setStatus("mandatory")
_Wbt3NetworkAddress_Type = DisplayString
_Wbt3NetworkAddress_Object = MibTableColumn
wbt3NetworkAddress = _Wbt3NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 3),
    _Wbt3NetworkAddress_Type()
)
wbt3NetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3NetworkAddress.setStatus("mandatory")
_Wbt3SubnetMask_Type = DisplayString
_Wbt3SubnetMask_Object = MibTableColumn
wbt3SubnetMask = _Wbt3SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 4),
    _Wbt3SubnetMask_Type()
)
wbt3SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3SubnetMask.setStatus("mandatory")
_Wbt3Gateway_Type = DisplayString
_Wbt3Gateway_Object = MibTableColumn
wbt3Gateway = _Wbt3Gateway_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 5),
    _Wbt3Gateway_Type()
)
wbt3Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Gateway.setStatus("mandatory")


class _Wbt3dnsEnable_Type(Integer32):
    """Custom type wbt3dnsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3dnsEnable_Type.__name__ = "Integer32"
_Wbt3dnsEnable_Object = MibTableColumn
wbt3dnsEnable = _Wbt3dnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 6),
    _Wbt3dnsEnable_Type()
)
wbt3dnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3dnsEnable.setStatus("mandatory")
_Wbt3defaultDomain_Type = DisplayString
_Wbt3defaultDomain_Object = MibTableColumn
wbt3defaultDomain = _Wbt3defaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 7),
    _Wbt3defaultDomain_Type()
)
wbt3defaultDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3defaultDomain.setStatus("mandatory")
_Wbt3primaryDNSserverIPaddress_Type = DisplayString
_Wbt3primaryDNSserverIPaddress_Object = MibTableColumn
wbt3primaryDNSserverIPaddress = _Wbt3primaryDNSserverIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 8),
    _Wbt3primaryDNSserverIPaddress_Type()
)
wbt3primaryDNSserverIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3primaryDNSserverIPaddress.setStatus("mandatory")
_Wbt3secondaryDNSserverIPaddress_Type = DisplayString
_Wbt3secondaryDNSserverIPaddress_Object = MibTableColumn
wbt3secondaryDNSserverIPaddress = _Wbt3secondaryDNSserverIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 9),
    _Wbt3secondaryDNSserverIPaddress_Type()
)
wbt3secondaryDNSserverIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3secondaryDNSserverIPaddress.setStatus("mandatory")


class _Wbt3winsEnable_Type(Integer32):
    """Custom type wbt3winsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3winsEnable_Type.__name__ = "Integer32"
_Wbt3winsEnable_Object = MibTableColumn
wbt3winsEnable = _Wbt3winsEnable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 10),
    _Wbt3winsEnable_Type()
)
wbt3winsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3winsEnable.setStatus("mandatory")
_Wbt3primaryWINSserverIPaddress_Type = DisplayString
_Wbt3primaryWINSserverIPaddress_Object = MibTableColumn
wbt3primaryWINSserverIPaddress = _Wbt3primaryWINSserverIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 11),
    _Wbt3primaryWINSserverIPaddress_Type()
)
wbt3primaryWINSserverIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3primaryWINSserverIPaddress.setStatus("mandatory")
_Wbt3secondaryWINSserverIPaddress_Type = DisplayString
_Wbt3secondaryWINSserverIPaddress_Object = MibTableColumn
wbt3secondaryWINSserverIPaddress = _Wbt3secondaryWINSserverIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 12),
    _Wbt3secondaryWINSserverIPaddress_Type()
)
wbt3secondaryWINSserverIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3secondaryWINSserverIPaddress.setStatus("mandatory")


class _Wbt3NetworkSpeed_Type(Integer32):
    """Custom type wbt3NetworkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("auto-detect", 0),
          ("mbs-100fullduplex", 6),
          ("mbs-100halfduplex", 7),
          ("mbs-10fullduplex", 8),
          ("mbs-10halfduplex", 9))
    )


_Wbt3NetworkSpeed_Type.__name__ = "Integer32"
_Wbt3NetworkSpeed_Object = MibTableColumn
wbt3NetworkSpeed = _Wbt3NetworkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 17),
    _Wbt3NetworkSpeed_Type()
)
wbt3NetworkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3NetworkSpeed.setStatus("mandatory")


class _Wbt3NetworkProtocol_Type(Integer32):
    """Custom type wbt3NetworkProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              256)
        )
    )
    namedValues = NamedValues(
        *(("tcp-ip", 0),
          ("unknown", 256))
    )


_Wbt3NetworkProtocol_Type.__name__ = "Integer32"
_Wbt3NetworkProtocol_Object = MibTableColumn
wbt3NetworkProtocol = _Wbt3NetworkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 11, 2, 1, 20),
    _Wbt3NetworkProtocol_Type()
)
wbt3NetworkProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3NetworkProtocol.setStatus("mandatory")
_Wbt3Apps_ObjectIdentity = ObjectIdentity
wbt3Apps = _Wbt3Apps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12)
)


class _Wbt3RDPencryption_Type(Integer32):
    """Custom type wbt3RDPencryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_Wbt3RDPencryption_Type.__name__ = "Integer32"
_Wbt3RDPencryption_Object = MibScalar
wbt3RDPencryption = _Wbt3RDPencryption_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 1),
    _Wbt3RDPencryption_Type()
)
wbt3RDPencryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3RDPencryption.setStatus("mandatory")
_Wbt3VirtualPortServerIPaddress_Type = DisplayString
_Wbt3VirtualPortServerIPaddress_Object = MibScalar
wbt3VirtualPortServerIPaddress = _Wbt3VirtualPortServerIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 2),
    _Wbt3VirtualPortServerIPaddress_Type()
)
wbt3VirtualPortServerIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3VirtualPortServerIPaddress.setStatus("mandatory")


class _Wbt3com1Share_Type(Integer32):
    """Custom type wbt3com1Share based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_Wbt3com1Share_Type.__name__ = "Integer32"
_Wbt3com1Share_Object = MibScalar
wbt3com1Share = _Wbt3com1Share_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 3),
    _Wbt3com1Share_Type()
)
wbt3com1Share.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3com1Share.setStatus("mandatory")


class _Wbt3com2Share_Type(Integer32):
    """Custom type wbt3com2Share based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_Wbt3com2Share_Type.__name__ = "Integer32"
_Wbt3com2Share_Object = MibScalar
wbt3com2Share = _Wbt3com2Share_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 4),
    _Wbt3com2Share_Type()
)
wbt3com2Share.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3com2Share.setStatus("mandatory")


class _Wbt3parallelShare_Type(Integer32):
    """Custom type wbt3parallelShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_Wbt3parallelShare_Type.__name__ = "Integer32"
_Wbt3parallelShare_Object = MibScalar
wbt3parallelShare = _Wbt3parallelShare_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 5),
    _Wbt3parallelShare_Type()
)
wbt3parallelShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3parallelShare.setStatus("mandatory")
_ICADefaultHotkeys_Object = MibTable
iCADefaultHotkeys = _ICADefaultHotkeys_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6)
)
if mibBuilder.loadTexts:
    iCADefaultHotkeys.setStatus("mandatory")
_DefaultHotkeysEntry_Object = MibTableRow
defaultHotkeysEntry = _DefaultHotkeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1)
)
if mibBuilder.loadTexts:
    defaultHotkeysEntry.setStatus("mandatory")


class _ICAStatusDialog_Type(Integer32):
    """Custom type iCAStatusDialog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ctrl", 0),
          ("shift", 1))
    )


_ICAStatusDialog_Type.__name__ = "Integer32"
_ICAStatusDialog_Object = MibTableColumn
iCAStatusDialog = _ICAStatusDialog_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 1),
    _ICAStatusDialog_Type()
)
iCAStatusDialog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCAStatusDialog.setStatus("mandatory")


class _ICAStatusDialog2_Type(Integer32):
    """Custom type iCAStatusDialog2 based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nb-0", 0),
          ("nb-1", 1),
          ("nb-2", 2),
          ("nb-3", 3),
          ("nb-4", 4),
          ("nb-5", 5),
          ("nb-6", 6),
          ("nb-7", 7),
          ("nb-8", 8),
          ("nb-9", 9))
    )


_ICAStatusDialog2_Type.__name__ = "Integer32"
_ICAStatusDialog2_Object = MibTableColumn
iCAStatusDialog2 = _ICAStatusDialog2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 2),
    _ICAStatusDialog2_Type()
)
iCAStatusDialog2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCAStatusDialog2.setStatus("mandatory")


class _ICACloseRemoteApplication_Type(Integer32):
    """Custom type iCACloseRemoteApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ctrl", 0),
          ("shift", 1))
    )


_ICACloseRemoteApplication_Type.__name__ = "Integer32"
_ICACloseRemoteApplication_Object = MibTableColumn
iCACloseRemoteApplication = _ICACloseRemoteApplication_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 3),
    _ICACloseRemoteApplication_Type()
)
iCACloseRemoteApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCACloseRemoteApplication.setStatus("mandatory")


class _ICACloseRemoteApplication2_Type(Integer32):
    """Custom type iCACloseRemoteApplication2 based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nb-0", 0),
          ("nb-1", 1),
          ("nb-2", 2),
          ("nb-3", 3),
          ("nb-4", 4),
          ("nb-5", 5),
          ("nb-6", 6),
          ("nb-7", 7),
          ("nb-8", 8),
          ("nb-9", 9))
    )


_ICACloseRemoteApplication2_Type.__name__ = "Integer32"
_ICACloseRemoteApplication2_Object = MibTableColumn
iCACloseRemoteApplication2 = _ICACloseRemoteApplication2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 4),
    _ICACloseRemoteApplication2_Type()
)
iCACloseRemoteApplication2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCACloseRemoteApplication2.setStatus("mandatory")


class _ICAtoggleTitleBar_Type(Integer32):
    """Custom type iCAtoggleTitleBar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ctrl", 0),
          ("shift", 1))
    )


_ICAtoggleTitleBar_Type.__name__ = "Integer32"
_ICAtoggleTitleBar_Object = MibTableColumn
iCAtoggleTitleBar = _ICAtoggleTitleBar_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 5),
    _ICAtoggleTitleBar_Type()
)
iCAtoggleTitleBar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCAtoggleTitleBar.setStatus("mandatory")


class _ICAtoggleTitleBar2_Type(Integer32):
    """Custom type iCAtoggleTitleBar2 based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nb-0", 0),
          ("nb-1", 1),
          ("nb-2", 2),
          ("nb-3", 3),
          ("nb-4", 4),
          ("nb-5", 5),
          ("nb-6", 6),
          ("nb-7", 7),
          ("nb-8", 8),
          ("nb-9", 9))
    )


_ICAtoggleTitleBar2_Type.__name__ = "Integer32"
_ICAtoggleTitleBar2_Object = MibTableColumn
iCAtoggleTitleBar2 = _ICAtoggleTitleBar2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 6),
    _ICAtoggleTitleBar2_Type()
)
iCAtoggleTitleBar2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCAtoggleTitleBar2.setStatus("mandatory")


class _ICActrlAltDel_Type(Integer32):
    """Custom type iCActrlAltDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("ctrl", 0)
    )


_ICActrlAltDel_Type.__name__ = "Integer32"
_ICActrlAltDel_Object = MibTableColumn
iCActrlAltDel = _ICActrlAltDel_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 7),
    _ICActrlAltDel_Type()
)
iCActrlAltDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCActrlAltDel.setStatus("mandatory")


class _ICActrlAltDel2_Type(Integer32):
    """Custom type iCActrlAltDel2 based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nb-0", 0),
          ("nb-1", 1),
          ("nb-2", 2),
          ("nb-3", 3),
          ("nb-4", 4),
          ("nb-5", 5),
          ("nb-6", 6),
          ("nb-7", 7),
          ("nb-8", 8),
          ("nb-9", 9))
    )


_ICActrlAltDel2_Type.__name__ = "Integer32"
_ICActrlAltDel2_Object = MibTableColumn
iCActrlAltDel2 = _ICActrlAltDel2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 8),
    _ICActrlAltDel2_Type()
)
iCActrlAltDel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCActrlAltDel2.setStatus("mandatory")


class _ICActrlEsc_Type(Integer32):
    """Custom type iCActrlEsc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("ctrl", 0)
    )


_ICActrlEsc_Type.__name__ = "Integer32"
_ICActrlEsc_Object = MibTableColumn
iCActrlEsc = _ICActrlEsc_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 9),
    _ICActrlEsc_Type()
)
iCActrlEsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCActrlEsc.setStatus("mandatory")


class _ICActrlEsc2_Type(Integer32):
    """Custom type iCActrlEsc2 based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nb-0", 0),
          ("nb-1", 1),
          ("nb-2", 2),
          ("nb-3", 3),
          ("nb-4", 4),
          ("nb-5", 5),
          ("nb-6", 6),
          ("nb-7", 7),
          ("nb-8", 8),
          ("nb-9", 9))
    )


_ICActrlEsc2_Type.__name__ = "Integer32"
_ICActrlEsc2_Object = MibTableColumn
iCActrlEsc2 = _ICActrlEsc2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 10),
    _ICActrlEsc2_Type()
)
iCActrlEsc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCActrlEsc2.setStatus("mandatory")


class _ICAaltEsc_Type(Integer32):
    """Custom type iCAaltEsc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ctrl", 0),
          ("shift", 1))
    )


_ICAaltEsc_Type.__name__ = "Integer32"
_ICAaltEsc_Object = MibTableColumn
iCAaltEsc = _ICAaltEsc_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 11),
    _ICAaltEsc_Type()
)
iCAaltEsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCAaltEsc.setStatus("mandatory")


class _ICAaltEsc2_Type(Integer32):
    """Custom type iCAaltEsc2 based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nb-0", 0),
          ("nb-1", 1),
          ("nb-2", 2),
          ("nb-3", 3),
          ("nb-4", 4),
          ("nb-5", 5),
          ("nb-6", 6),
          ("nb-7", 7),
          ("nb-8", 8),
          ("nb-9", 9))
    )


_ICAaltEsc2_Type.__name__ = "Integer32"
_ICAaltEsc2_Object = MibTableColumn
iCAaltEsc2 = _ICAaltEsc2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 12),
    _ICAaltEsc2_Type()
)
iCAaltEsc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCAaltEsc2.setStatus("mandatory")


class _ICAaltTab_Type(Integer32):
    """Custom type iCAaltTab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ctrl", 0),
          ("shift", 1))
    )


_ICAaltTab_Type.__name__ = "Integer32"
_ICAaltTab_Object = MibTableColumn
iCAaltTab = _ICAaltTab_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 13),
    _ICAaltTab_Type()
)
iCAaltTab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCAaltTab.setStatus("mandatory")


class _ICAaltTab2_Type(Integer32):
    """Custom type iCAaltTab2 based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nb-0", 0),
          ("nb-1", 1),
          ("nb-2", 2),
          ("nb-3", 3),
          ("nb-4", 4),
          ("nb-5", 5),
          ("nb-6", 6),
          ("nb-7", 7),
          ("nb-8", 8),
          ("nb-9", 9))
    )


_ICAaltTab2_Type.__name__ = "Integer32"
_ICAaltTab2_Object = MibTableColumn
iCAaltTab2 = _ICAaltTab2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 14),
    _ICAaltTab2_Type()
)
iCAaltTab2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCAaltTab2.setStatus("mandatory")


class _ICAaltBackTab_Type(Integer32):
    """Custom type iCAaltBackTab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ctrl", 0),
          ("shift", 1))
    )


_ICAaltBackTab_Type.__name__ = "Integer32"
_ICAaltBackTab_Object = MibTableColumn
iCAaltBackTab = _ICAaltBackTab_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 15),
    _ICAaltBackTab_Type()
)
iCAaltBackTab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCAaltBackTab.setStatus("mandatory")


class _ICAaltBackTab2_Type(Integer32):
    """Custom type iCAaltBackTab2 based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nb-0", 0),
          ("nb-1", 1),
          ("nb-2", 2),
          ("nb-3", 3),
          ("nb-4", 4),
          ("nb-5", 5),
          ("nb-6", 6),
          ("nb-7", 7),
          ("nb-8", 8),
          ("nb-9", 9))
    )


_ICAaltBackTab2_Type.__name__ = "Integer32"
_ICAaltBackTab2_Object = MibTableColumn
iCAaltBackTab2 = _ICAaltBackTab2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 12, 6, 1, 16),
    _ICAaltBackTab2_Type()
)
iCAaltBackTab2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iCAaltBackTab2.setStatus("mandatory")
_Wbt3Connections_ObjectIdentity = ObjectIdentity
wbt3Connections = _Wbt3Connections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13)
)
_Wbt3ConnectionsTable_Object = MibTable
wbt3ConnectionsTable = _Wbt3ConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 2)
)
if mibBuilder.loadTexts:
    wbt3ConnectionsTable.setStatus("mandatory")
_Wbt3ConnectionEntry_Object = MibTableRow
wbt3ConnectionEntry = _Wbt3ConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 2, 1)
)
wbt3ConnectionEntry.setIndexNames(
    (0, "WYSE-MIB", "wbt3ConnectionName"),
)
if mibBuilder.loadTexts:
    wbt3ConnectionEntry.setStatus("mandatory")
_Wbt3ConnectionName_Type = DisplayString
_Wbt3ConnectionName_Object = MibTableColumn
wbt3ConnectionName = _Wbt3ConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 2, 1, 2),
    _Wbt3ConnectionName_Type()
)
wbt3ConnectionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ConnectionName.setStatus("mandatory")


class _Wbt3ConnectionType_Type(Integer32):
    """Custom type wbt3ConnectionType based on Integer32"""
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
        *(("dialup", 3),
          ("ica", 1),
          ("rdp", 0),
          ("tec", 2))
    )


_Wbt3ConnectionType_Type.__name__ = "Integer32"
_Wbt3ConnectionType_Object = MibTableColumn
wbt3ConnectionType = _Wbt3ConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 2, 1, 3),
    _Wbt3ConnectionType_Type()
)
wbt3ConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ConnectionType.setStatus("mandatory")


class _Wbt3ConnectionEntryStatus_Type(Integer32):
    """Custom type wbt3ConnectionEntryStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_Wbt3ConnectionEntryStatus_Type.__name__ = "Integer32"
_Wbt3ConnectionEntryStatus_Object = MibTableColumn
wbt3ConnectionEntryStatus = _Wbt3ConnectionEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 2, 1, 10),
    _Wbt3ConnectionEntryStatus_Type()
)
wbt3ConnectionEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ConnectionEntryStatus.setStatus("mandatory")
_Wbt3RDPConnections_ObjectIdentity = ObjectIdentity
wbt3RDPConnections = _Wbt3RDPConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3)
)
_Wbt3RDPConnTable_Object = MibTable
wbt3RDPConnTable = _Wbt3RDPConnTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1)
)
if mibBuilder.loadTexts:
    wbt3RDPConnTable.setStatus("mandatory")
_Wbt3RDPConnEntry_Object = MibTableRow
wbt3RDPConnEntry = _Wbt3RDPConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wbt3RDPConnEntry.setStatus("mandatory")
_Wbt3RDPConnName_Type = DisplayString
_Wbt3RDPConnName_Object = MibTableColumn
wbt3RDPConnName = _Wbt3RDPConnName_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1, 1),
    _Wbt3RDPConnName_Type()
)
wbt3RDPConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RDPConnName.setStatus("mandatory")
_Wbt3RDPConnServer_Type = DisplayString
_Wbt3RDPConnServer_Object = MibTableColumn
wbt3RDPConnServer = _Wbt3RDPConnServer_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1, 2),
    _Wbt3RDPConnServer_Type()
)
wbt3RDPConnServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3RDPConnServer.setStatus("mandatory")


class _Wbt3RDPConnLowSpeed_Type(Integer32):
    """Custom type wbt3RDPConnLowSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3RDPConnLowSpeed_Type.__name__ = "Integer32"
_Wbt3RDPConnLowSpeed_Object = MibTableColumn
wbt3RDPConnLowSpeed = _Wbt3RDPConnLowSpeed_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1, 3),
    _Wbt3RDPConnLowSpeed_Type()
)
wbt3RDPConnLowSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3RDPConnLowSpeed.setStatus("mandatory")


class _Wbt3RDPConnAutoLogon_Type(Integer32):
    """Custom type wbt3RDPConnAutoLogon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3RDPConnAutoLogon_Type.__name__ = "Integer32"
_Wbt3RDPConnAutoLogon_Object = MibTableColumn
wbt3RDPConnAutoLogon = _Wbt3RDPConnAutoLogon_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1, 4),
    _Wbt3RDPConnAutoLogon_Type()
)
wbt3RDPConnAutoLogon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3RDPConnAutoLogon.setStatus("mandatory")
_Wbt3RDPConnUsername_Type = DisplayString
_Wbt3RDPConnUsername_Object = MibTableColumn
wbt3RDPConnUsername = _Wbt3RDPConnUsername_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1, 5),
    _Wbt3RDPConnUsername_Type()
)
wbt3RDPConnUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3RDPConnUsername.setStatus("mandatory")
_Wbt3RDPConnDomain_Type = DisplayString
_Wbt3RDPConnDomain_Object = MibTableColumn
wbt3RDPConnDomain = _Wbt3RDPConnDomain_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1, 7),
    _Wbt3RDPConnDomain_Type()
)
wbt3RDPConnDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3RDPConnDomain.setStatus("mandatory")


class _Wbt3RDPConnStartApplication_Type(Integer32):
    """Custom type wbt3RDPConnStartApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("desktop", 0),
          ("filename", 2))
    )


_Wbt3RDPConnStartApplication_Type.__name__ = "Integer32"
_Wbt3RDPConnStartApplication_Object = MibTableColumn
wbt3RDPConnStartApplication = _Wbt3RDPConnStartApplication_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1, 8),
    _Wbt3RDPConnStartApplication_Type()
)
wbt3RDPConnStartApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3RDPConnStartApplication.setStatus("mandatory")
_Wbt3RDPConnFilename_Type = DisplayString
_Wbt3RDPConnFilename_Object = MibTableColumn
wbt3RDPConnFilename = _Wbt3RDPConnFilename_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1, 9),
    _Wbt3RDPConnFilename_Type()
)
wbt3RDPConnFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3RDPConnFilename.setStatus("mandatory")
_Wbt3RDPConnWorkingDir_Type = DisplayString
_Wbt3RDPConnWorkingDir_Object = MibTableColumn
wbt3RDPConnWorkingDir = _Wbt3RDPConnWorkingDir_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1, 10),
    _Wbt3RDPConnWorkingDir_Type()
)
wbt3RDPConnWorkingDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3RDPConnWorkingDir.setStatus("mandatory")


class _Wbt3RDPConnModifiable_Type(Integer32):
    """Custom type wbt3RDPConnModifiable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3RDPConnModifiable_Type.__name__ = "Integer32"
_Wbt3RDPConnModifiable_Object = MibTableColumn
wbt3RDPConnModifiable = _Wbt3RDPConnModifiable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 3, 1, 1, 30),
    _Wbt3RDPConnModifiable_Type()
)
wbt3RDPConnModifiable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3RDPConnModifiable.setStatus("mandatory")
_Wbt3ICAConnections_ObjectIdentity = ObjectIdentity
wbt3ICAConnections = _Wbt3ICAConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4)
)
_Wbt3ICAConnTable_Object = MibTable
wbt3ICAConnTable = _Wbt3ICAConnTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1)
)
if mibBuilder.loadTexts:
    wbt3ICAConnTable.setStatus("mandatory")
_Wbt3ICAConnEntry_Object = MibTableRow
wbt3ICAConnEntry = _Wbt3ICAConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1)
)
if mibBuilder.loadTexts:
    wbt3ICAConnEntry.setStatus("mandatory")
_Wbt3ICAConnName_Type = DisplayString
_Wbt3ICAConnName_Object = MibTableColumn
wbt3ICAConnName = _Wbt3ICAConnName_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 1),
    _Wbt3ICAConnName_Type()
)
wbt3ICAConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3ICAConnName.setStatus("mandatory")


class _Wbt3ICAConnCommType_Type(Integer32):
    """Custom type wbt3ICAConnCommType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("network", 0)
    )


_Wbt3ICAConnCommType_Type.__name__ = "Integer32"
_Wbt3ICAConnCommType_Object = MibTableColumn
wbt3ICAConnCommType = _Wbt3ICAConnCommType_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 2),
    _Wbt3ICAConnCommType_Type()
)
wbt3ICAConnCommType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ICAConnCommType.setStatus("mandatory")
_Wbt3ICAConnServer_Type = DisplayString
_Wbt3ICAConnServer_Object = MibTableColumn
wbt3ICAConnServer = _Wbt3ICAConnServer_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 3),
    _Wbt3ICAConnServer_Type()
)
wbt3ICAConnServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ICAConnServer.setStatus("mandatory")
_Wbt3ICAConnCommandLine_Type = DisplayString
_Wbt3ICAConnCommandLine_Object = MibTableColumn
wbt3ICAConnCommandLine = _Wbt3ICAConnCommandLine_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 4),
    _Wbt3ICAConnCommandLine_Type()
)
wbt3ICAConnCommandLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ICAConnCommandLine.setStatus("mandatory")
_Wbt3ICAConnWorkingDir_Type = DisplayString
_Wbt3ICAConnWorkingDir_Object = MibTableColumn
wbt3ICAConnWorkingDir = _Wbt3ICAConnWorkingDir_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 5),
    _Wbt3ICAConnWorkingDir_Type()
)
wbt3ICAConnWorkingDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ICAConnWorkingDir.setStatus("mandatory")
_Wbt3ICAConnUsername_Type = DisplayString
_Wbt3ICAConnUsername_Object = MibTableColumn
wbt3ICAConnUsername = _Wbt3ICAConnUsername_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 6),
    _Wbt3ICAConnUsername_Type()
)
wbt3ICAConnUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ICAConnUsername.setStatus("mandatory")
_Wbt3ICAConnDomain_Type = DisplayString
_Wbt3ICAConnDomain_Object = MibTableColumn
wbt3ICAConnDomain = _Wbt3ICAConnDomain_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 8),
    _Wbt3ICAConnDomain_Type()
)
wbt3ICAConnDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ICAConnDomain.setStatus("mandatory")


class _Wbt3ICAConnColors_Type(Integer32):
    """Custom type wbt3ICAConnColors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nb-16", 0),
          ("nb-256", 1))
    )


_Wbt3ICAConnColors_Type.__name__ = "Integer32"
_Wbt3ICAConnColors_Object = MibTableColumn
wbt3ICAConnColors = _Wbt3ICAConnColors_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 9),
    _Wbt3ICAConnColors_Type()
)
wbt3ICAConnColors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ICAConnColors.setStatus("mandatory")


class _Wbt3ICAConnDataCompress_Type(Integer32):
    """Custom type wbt3ICAConnDataCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3ICAConnDataCompress_Type.__name__ = "Integer32"
_Wbt3ICAConnDataCompress_Object = MibTableColumn
wbt3ICAConnDataCompress = _Wbt3ICAConnDataCompress_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 10),
    _Wbt3ICAConnDataCompress_Type()
)
wbt3ICAConnDataCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ICAConnDataCompress.setStatus("mandatory")


class _Wbt3ICAConnSoundQuality_Type(Integer32):
    """Custom type wbt3ICAConnSoundQuality based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("none", 0))
    )


_Wbt3ICAConnSoundQuality_Type.__name__ = "Integer32"
_Wbt3ICAConnSoundQuality_Object = MibTableColumn
wbt3ICAConnSoundQuality = _Wbt3ICAConnSoundQuality_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 11),
    _Wbt3ICAConnSoundQuality_Type()
)
wbt3ICAConnSoundQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3ICAConnSoundQuality.setStatus("mandatory")


class _Wbt3ICAConnModifiable_Type(Integer32):
    """Custom type wbt3ICAConnModifiable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3ICAConnModifiable_Type.__name__ = "Integer32"
_Wbt3ICAConnModifiable_Object = MibTableColumn
wbt3ICAConnModifiable = _Wbt3ICAConnModifiable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 4, 1, 1, 30),
    _Wbt3ICAConnModifiable_Type()
)
wbt3ICAConnModifiable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3ICAConnModifiable.setStatus("mandatory")
_Wbt3TermConnections_ObjectIdentity = ObjectIdentity
wbt3TermConnections = _Wbt3TermConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5)
)
_Wbt3TermConnTable_Object = MibTable
wbt3TermConnTable = _Wbt3TermConnTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1)
)
if mibBuilder.loadTexts:
    wbt3TermConnTable.setStatus("mandatory")
_Wbt3TermConnEntry_Object = MibTableRow
wbt3TermConnEntry = _Wbt3TermConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1)
)
if mibBuilder.loadTexts:
    wbt3TermConnEntry.setStatus("mandatory")
_Wbt3TermConnName_Type = DisplayString
_Wbt3TermConnName_Object = MibTableColumn
wbt3TermConnName = _Wbt3TermConnName_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 1),
    _Wbt3TermConnName_Type()
)
wbt3TermConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3TermConnName.setStatus("mandatory")


class _Wbt3TermConnCommType_Type(Integer32):
    """Custom type wbt3TermConnCommType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("network", 0)
    )


_Wbt3TermConnCommType_Type.__name__ = "Integer32"
_Wbt3TermConnCommType_Object = MibTableColumn
wbt3TermConnCommType = _Wbt3TermConnCommType_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 2),
    _Wbt3TermConnCommType_Type()
)
wbt3TermConnCommType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnCommType.setStatus("mandatory")
_Wbt3TermConnServer_Type = DisplayString
_Wbt3TermConnServer_Object = MibTableColumn
wbt3TermConnServer = _Wbt3TermConnServer_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 3),
    _Wbt3TermConnServer_Type()
)
wbt3TermConnServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnServer.setStatus("mandatory")


class _Wbt3TermConnEmuType_Type(Integer32):
    """Custom type wbt3TermConnEmuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("adds-a2", 15),
          ("ansi-bbs", 5),
          ("hz1500", 16),
          ("ibm3151", 8),
          ("ibm3270", 7),
          ("ibm5250", 9),
          ("sco-console", 6),
          ("tvi910", 12),
          ("tvi920", 13),
          ("tvi925", 14),
          ("vt100", 1),
          ("vt400-7-bit", 3),
          ("vt400-8-bit", 4),
          ("vt52", 0),
          ("wy50", 10),
          ("wy50-plus", 11),
          ("wy60", 17))
    )


_Wbt3TermConnEmuType_Type.__name__ = "Integer32"
_Wbt3TermConnEmuType_Object = MibTableColumn
wbt3TermConnEmuType = _Wbt3TermConnEmuType_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 4),
    _Wbt3TermConnEmuType_Type()
)
wbt3TermConnEmuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnEmuType.setStatus("mandatory")


class _Wbt3TermConnVTEmuModel_Type(Integer32):
    """Custom type wbt3TermConnVTEmuModel based on Integer32"""
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
              7,
              8,
              9,
              10,
              256)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 256),
          ("vt100", 0),
          ("vt101", 1),
          ("vt102", 2),
          ("vt125", 3),
          ("vt131", 9),
          ("vt132", 10),
          ("vt220", 4),
          ("vt240", 5),
          ("vt320", 6),
          ("vt340", 7),
          ("vt420", 8))
    )


_Wbt3TermConnVTEmuModel_Type.__name__ = "Integer32"
_Wbt3TermConnVTEmuModel_Object = MibScalar
wbt3TermConnVTEmuModel = _Wbt3TermConnVTEmuModel_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 5),
    _Wbt3TermConnVTEmuModel_Type()
)
wbt3TermConnVTEmuModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnVTEmuModel.setStatus("mandatory")


class _Wbt3TermConnIBM3270EmuModel_Type(Integer32):
    """Custom type wbt3TermConnIBM3270EmuModel based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              256)
        )
    )
    namedValues = NamedValues(
        *(("ibm3278-2", 0),
          ("ibm3278-2-e", 4),
          ("ibm3278-3", 1),
          ("ibm3278-3-e", 5),
          ("ibm3278-4", 2),
          ("ibm3278-4-e", 6),
          ("ibm3278-5", 3),
          ("ibm3278-5-e", 7),
          ("ibm3279-2", 8),
          ("ibm3279-3", 9),
          ("ibm3279-4", 10),
          ("ibm3279-5", 11),
          ("ibm3287-1", 12),
          ("not-applicable", 256))
    )


_Wbt3TermConnIBM3270EmuModel_Type.__name__ = "Integer32"
_Wbt3TermConnIBM3270EmuModel_Object = MibScalar
wbt3TermConnIBM3270EmuModel = _Wbt3TermConnIBM3270EmuModel_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 6),
    _Wbt3TermConnIBM3270EmuModel_Type()
)
wbt3TermConnIBM3270EmuModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnIBM3270EmuModel.setStatus("mandatory")


class _Wbt3TermConnIBM5250EmuModel_Type(Integer32):
    """Custom type wbt3TermConnIBM5250EmuModel based on Integer32"""
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
              7,
              8,
              9,
              10,
              256)
        )
    )
    namedValues = NamedValues(
        *(("ibm3179-2", 3),
          ("ibm3180-2", 5),
          ("ibm3196-a1", 4),
          ("ibm3477-fc", 6),
          ("ibm3477-fg", 7),
          ("ibm3486-ba", 8),
          ("ibm3487-ha", 9),
          ("ibm3487-hc", 10),
          ("ibm5251-11", 2),
          ("ibm5291-1", 0),
          ("ibm5292-2", 1),
          ("not-applicable", 256))
    )


_Wbt3TermConnIBM5250EmuModel_Type.__name__ = "Integer32"
_Wbt3TermConnIBM5250EmuModel_Object = MibScalar
wbt3TermConnIBM5250EmuModel = _Wbt3TermConnIBM5250EmuModel_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 7),
    _Wbt3TermConnIBM5250EmuModel_Type()
)
wbt3TermConnIBM5250EmuModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnIBM5250EmuModel.setStatus("mandatory")


class _Wbt3TermConnPortNumber_Type(Integer32):
    """Custom type wbt3TermConnPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wbt3TermConnPortNumber_Type.__name__ = "Integer32"
_Wbt3TermConnPortNumber_Object = MibTableColumn
wbt3TermConnPortNumber = _Wbt3TermConnPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 10),
    _Wbt3TermConnPortNumber_Type()
)
wbt3TermConnPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnPortNumber.setStatus("mandatory")
_Wbt3TermConnTelnetName_Type = DisplayString
_Wbt3TermConnTelnetName_Object = MibTableColumn
wbt3TermConnTelnetName = _Wbt3TermConnTelnetName_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 11),
    _Wbt3TermConnTelnetName_Type()
)
wbt3TermConnTelnetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnTelnetName.setStatus("mandatory")


class _Wbt3TermConnPrinterPort_Type(Integer32):
    """Custom type wbt3TermConnPrinterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("lpt1", 0)
    )


_Wbt3TermConnPrinterPort_Type.__name__ = "Integer32"
_Wbt3TermConnPrinterPort_Object = MibTableColumn
wbt3TermConnPrinterPort = _Wbt3TermConnPrinterPort_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 12),
    _Wbt3TermConnPrinterPort_Type()
)
wbt3TermConnPrinterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnPrinterPort.setStatus("mandatory")


class _Wbt3TermConnFormFeed_Type(Integer32):
    """Custom type wbt3TermConnFormFeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3TermConnFormFeed_Type.__name__ = "Integer32"
_Wbt3TermConnFormFeed_Object = MibTableColumn
wbt3TermConnFormFeed = _Wbt3TermConnFormFeed_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 13),
    _Wbt3TermConnFormFeed_Type()
)
wbt3TermConnFormFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnFormFeed.setStatus("mandatory")


class _Wbt3TermConnAutoLineFeed_Type(Integer32):
    """Custom type wbt3TermConnAutoLineFeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3TermConnAutoLineFeed_Type.__name__ = "Integer32"
_Wbt3TermConnAutoLineFeed_Object = MibTableColumn
wbt3TermConnAutoLineFeed = _Wbt3TermConnAutoLineFeed_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 14),
    _Wbt3TermConnAutoLineFeed_Type()
)
wbt3TermConnAutoLineFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnAutoLineFeed.setStatus("mandatory")
_Wbt3TermConnScript_Type = DisplayString
_Wbt3TermConnScript_Object = MibScalar
wbt3TermConnScript = _Wbt3TermConnScript_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 15),
    _Wbt3TermConnScript_Type()
)
wbt3TermConnScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3TermConnScript.setStatus("mandatory")


class _Wbt3TermConnModifiable_Type(Integer32):
    """Custom type wbt3TermConnModifiable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3TermConnModifiable_Type.__name__ = "Integer32"
_Wbt3TermConnModifiable_Object = MibTableColumn
wbt3TermConnModifiable = _Wbt3TermConnModifiable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 13, 5, 1, 1, 30),
    _Wbt3TermConnModifiable_Type()
)
wbt3TermConnModifiable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbt3TermConnModifiable.setStatus("mandatory")
_Wbt3Users_ObjectIdentity = ObjectIdentity
wbt3Users = _Wbt3Users_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14)
)
_Wbt3UsersTable_Object = MibTable
wbt3UsersTable = _Wbt3UsersTable_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2)
)
if mibBuilder.loadTexts:
    wbt3UsersTable.setStatus("mandatory")
_Wbt3UsersEntry_Object = MibTableRow
wbt3UsersEntry = _Wbt3UsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1)
)
wbt3UsersEntry.setIndexNames(
    (0, "WYSE-MIB", "wbt3userName"),
)
if mibBuilder.loadTexts:
    wbt3UsersEntry.setStatus("mandatory")


class _Wbt3UsersStatus_Type(Integer32):
    """Custom type wbt3UsersStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_Wbt3UsersStatus_Type.__name__ = "Integer32"
_Wbt3UsersStatus_Object = MibTableColumn
wbt3UsersStatus = _Wbt3UsersStatus_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 2),
    _Wbt3UsersStatus_Type()
)
wbt3UsersStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UsersStatus.setStatus("mandatory")
_Wbt3userName_Type = DisplayString
_Wbt3userName_Object = MibTableColumn
wbt3userName = _Wbt3userName_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 3),
    _Wbt3userName_Type()
)
wbt3userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3userName.setStatus("mandatory")
_Wbt3password_Type = DisplayString
_Wbt3password_Object = MibTableColumn
wbt3password = _Wbt3password_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 4),
    _Wbt3password_Type()
)
wbt3password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3password.setStatus("mandatory")


class _Wbt3privilege_Type(Integer32):
    """Custom type wbt3privilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 0),
          ("guest", 2),
          ("user", 1))
    )


_Wbt3privilege_Type.__name__ = "Integer32"
_Wbt3privilege_Object = MibTableColumn
wbt3privilege = _Wbt3privilege_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 5),
    _Wbt3privilege_Type()
)
wbt3privilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3privilege.setStatus("mandatory")
_Wbt3Connection1_Type = DisplayString
_Wbt3Connection1_Object = MibTableColumn
wbt3Connection1 = _Wbt3Connection1_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 7),
    _Wbt3Connection1_Type()
)
wbt3Connection1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Connection1.setStatus("mandatory")
_Wbt3Connection2_Type = DisplayString
_Wbt3Connection2_Object = MibTableColumn
wbt3Connection2 = _Wbt3Connection2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 8),
    _Wbt3Connection2_Type()
)
wbt3Connection2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Connection2.setStatus("mandatory")
_Wbt3Connection3_Type = DisplayString
_Wbt3Connection3_Object = MibTableColumn
wbt3Connection3 = _Wbt3Connection3_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 9),
    _Wbt3Connection3_Type()
)
wbt3Connection3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Connection3.setStatus("mandatory")
_Wbt3Connection4_Type = DisplayString
_Wbt3Connection4_Object = MibTableColumn
wbt3Connection4 = _Wbt3Connection4_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 10),
    _Wbt3Connection4_Type()
)
wbt3Connection4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Connection4.setStatus("mandatory")
_Wbt3Connection5_Type = DisplayString
_Wbt3Connection5_Object = MibTableColumn
wbt3Connection5 = _Wbt3Connection5_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 11),
    _Wbt3Connection5_Type()
)
wbt3Connection5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Connection5.setStatus("mandatory")
_Wbt3Connection6_Type = DisplayString
_Wbt3Connection6_Object = MibTableColumn
wbt3Connection6 = _Wbt3Connection6_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 12),
    _Wbt3Connection6_Type()
)
wbt3Connection6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Connection6.setStatus("mandatory")
_Wbt3Connection7_Type = DisplayString
_Wbt3Connection7_Object = MibTableColumn
wbt3Connection7 = _Wbt3Connection7_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 13),
    _Wbt3Connection7_Type()
)
wbt3Connection7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Connection7.setStatus("mandatory")
_Wbt3Connection8_Type = DisplayString
_Wbt3Connection8_Object = MibTableColumn
wbt3Connection8 = _Wbt3Connection8_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 14),
    _Wbt3Connection8_Type()
)
wbt3Connection8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3Connection8.setStatus("mandatory")


class _Wbt3AutoStart1_Type(Integer32):
    """Custom type wbt3AutoStart1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AutoStart1_Type.__name__ = "Integer32"
_Wbt3AutoStart1_Object = MibScalar
wbt3AutoStart1 = _Wbt3AutoStart1_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 15),
    _Wbt3AutoStart1_Type()
)
wbt3AutoStart1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoStart1.setStatus("mandatory")


class _Wbt3AutoStart2_Type(Integer32):
    """Custom type wbt3AutoStart2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AutoStart2_Type.__name__ = "Integer32"
_Wbt3AutoStart2_Object = MibScalar
wbt3AutoStart2 = _Wbt3AutoStart2_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 16),
    _Wbt3AutoStart2_Type()
)
wbt3AutoStart2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoStart2.setStatus("mandatory")


class _Wbt3AutoStart3_Type(Integer32):
    """Custom type wbt3AutoStart3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AutoStart3_Type.__name__ = "Integer32"
_Wbt3AutoStart3_Object = MibScalar
wbt3AutoStart3 = _Wbt3AutoStart3_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 17),
    _Wbt3AutoStart3_Type()
)
wbt3AutoStart3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoStart3.setStatus("mandatory")


class _Wbt3AutoStart4_Type(Integer32):
    """Custom type wbt3AutoStart4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AutoStart4_Type.__name__ = "Integer32"
_Wbt3AutoStart4_Object = MibScalar
wbt3AutoStart4 = _Wbt3AutoStart4_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 18),
    _Wbt3AutoStart4_Type()
)
wbt3AutoStart4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoStart4.setStatus("mandatory")


class _Wbt3AutoStart5_Type(Integer32):
    """Custom type wbt3AutoStart5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AutoStart5_Type.__name__ = "Integer32"
_Wbt3AutoStart5_Object = MibScalar
wbt3AutoStart5 = _Wbt3AutoStart5_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 19),
    _Wbt3AutoStart5_Type()
)
wbt3AutoStart5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoStart5.setStatus("mandatory")


class _Wbt3AutoStart6_Type(Integer32):
    """Custom type wbt3AutoStart6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AutoStart6_Type.__name__ = "Integer32"
_Wbt3AutoStart6_Object = MibScalar
wbt3AutoStart6 = _Wbt3AutoStart6_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 20),
    _Wbt3AutoStart6_Type()
)
wbt3AutoStart6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoStart6.setStatus("mandatory")


class _Wbt3AutoStart7_Type(Integer32):
    """Custom type wbt3AutoStart7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AutoStart7_Type.__name__ = "Integer32"
_Wbt3AutoStart7_Object = MibScalar
wbt3AutoStart7 = _Wbt3AutoStart7_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 21),
    _Wbt3AutoStart7_Type()
)
wbt3AutoStart7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoStart7.setStatus("mandatory")


class _Wbt3AutoStart8_Type(Integer32):
    """Custom type wbt3AutoStart8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3AutoStart8_Type.__name__ = "Integer32"
_Wbt3AutoStart8_Object = MibScalar
wbt3AutoStart8 = _Wbt3AutoStart8_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 22),
    _Wbt3AutoStart8_Type()
)
wbt3AutoStart8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3AutoStart8.setStatus("mandatory")


class _Wbt3UserPasswordChange_Type(Integer32):
    """Custom type wbt3UserPasswordChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Wbt3UserPasswordChange_Type.__name__ = "Integer32"
_Wbt3UserPasswordChange_Object = MibTableColumn
wbt3UserPasswordChange = _Wbt3UserPasswordChange_Object(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 14, 2, 1, 23),
    _Wbt3UserPasswordChange_Type()
)
wbt3UserPasswordChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wbt3UserPasswordChange.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wbt3TrapDHCPBuildMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 0, 1)
)
wbt3TrapDHCPBuildMismatch.setObjects(
      *(("WYSE-MIB", "wbt3CurBuildNum"),
        ("WYSE-MIB", "wbt3CurOEMBuildNum"),
        ("WYSE-MIB", "wbt3CurModBuildDate"),
        ("WYSE-MIB", "wbt3DUpBuildNum"),
        ("WYSE-MIB", "wbt3DUpOEMBuildNum"),
        ("WYSE-MIB", "wbt3DUpOEMBuildDate"))
)
if mibBuilder.loadTexts:
    wbt3TrapDHCPBuildMismatch.setStatus(
        ""
    )

wbt3TrapDHCPUpdDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 0, 2)
)
wbt3TrapDHCPUpdDone.setObjects(
      *(("WYSE-MIB", "wbt3CurBuildNum"),
        ("WYSE-MIB", "wbt3CurOEMBuildNum"),
        ("WYSE-MIB", "wbt3CurModBuildDate"),
        ("WYSE-MIB", "wbt3DUpBuildNum"),
        ("WYSE-MIB", "wbt3DUpOEMBuildNum"),
        ("WYSE-MIB", "wbt3DUpOEMBuildDate"))
)
if mibBuilder.loadTexts:
    wbt3TrapDHCPUpdDone.setStatus(
        ""
    )

wbt3TrapDHCPUpdNotComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 0, 3)
)
wbt3TrapDHCPUpdNotComplete.setObjects(
      *(("WYSE-MIB", "wbt3CurBuildNum"),
        ("WYSE-MIB", "wbt3CurOEMBuildNum"),
        ("WYSE-MIB", "wbt3CurModBuildDate"),
        ("WYSE-MIB", "wbt3DUpBuildNum"),
        ("WYSE-MIB", "wbt3DUpOEMBuildNum"),
        ("WYSE-MIB", "wbt3DUpOEMBuildDate"),
        ("WYSE-MIB", "wbt3TrapStatus"))
)
if mibBuilder.loadTexts:
    wbt3TrapDHCPUpdNotComplete.setStatus(
        ""
    )

wbt3TrapSNMPAccptLd = NotificationType(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 0, 4)
)
wbt3TrapSNMPAccptLd.setObjects(
    ("WYSE-MIB", "wbt3SubmitLoadJob")
)
if mibBuilder.loadTexts:
    wbt3TrapSNMPAccptLd.setStatus(
        ""
    )

wbt3TrapSNMPLdDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 0, 5)
)
wbt3TrapSNMPLdDone.setObjects(
    ("WYSE-MIB", "wbt3TrapReqId")
)
if mibBuilder.loadTexts:
    wbt3TrapSNMPLdDone.setStatus(
        ""
    )

wbt3TrapSNMPLdNotComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 0, 6)
)
wbt3TrapSNMPLdNotComplete.setObjects(
      *(("WYSE-MIB", "wbt3TrapReqId"),
        ("WYSE-MIB", "wbt3TrapStatus"))
)
if mibBuilder.loadTexts:
    wbt3TrapSNMPLdNotComplete.setStatus(
        ""
    )

wbt3TrapRebootNotComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 714, 1, 2, 3, 0, 7)
)
wbt3TrapRebootNotComplete.setObjects(
    ("WYSE-MIB", "wbt3TrapStatus")
)
if mibBuilder.loadTexts:
    wbt3TrapRebootNotComplete.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WYSE-MIB",
    **{"wyse": wyse,
       "product": product,
       "old": old,
       "wysenet": wysenet,
       "thinClient": thinClient,
       "wbt3": wbt3,
       "wbt3TrapDHCPBuildMismatch": wbt3TrapDHCPBuildMismatch,
       "wbt3TrapDHCPUpdDone": wbt3TrapDHCPUpdDone,
       "wbt3TrapDHCPUpdNotComplete": wbt3TrapDHCPUpdNotComplete,
       "wbt3TrapSNMPAccptLd": wbt3TrapSNMPAccptLd,
       "wbt3TrapSNMPLdDone": wbt3TrapSNMPLdDone,
       "wbt3TrapSNMPLdNotComplete": wbt3TrapSNMPLdNotComplete,
       "wbt3TrapRebootNotComplete": wbt3TrapRebootNotComplete,
       "wbt3Memory": wbt3Memory,
       "wbt3Ram": wbt3Ram,
       "wbt3RamNum": wbt3RamNum,
       "wbt3RamTable": wbt3RamTable,
       "wbt3RamEntry": wbt3RamEntry,
       "wbt3RamIndex": wbt3RamIndex,
       "wbt3RamType": wbt3RamType,
       "wbt3RamSize": wbt3RamSize,
       "wbt3Rom": wbt3Rom,
       "wbt3RomNum": wbt3RomNum,
       "wbt3RomTable": wbt3RomTable,
       "wbt3RomEntry": wbt3RomEntry,
       "wbt3RomIndex": wbt3RomIndex,
       "wbt3RomType": wbt3RomType,
       "wbt3RomSize": wbt3RomSize,
       "wbt3PCCard": wbt3PCCard,
       "wbt3PCCardNum": wbt3PCCardNum,
       "wbt3PCCardTable": wbt3PCCardTable,
       "wbt3PCCardEntry": wbt3PCCardEntry,
       "wbt3PCCardIndex": wbt3PCCardIndex,
       "wbt3PCCardType": wbt3PCCardType,
       "wbt3PCCardVendor": wbt3PCCardVendor,
       "wbt3IODevice": wbt3IODevice,
       "wbt3IODevAttached": wbt3IODevAttached,
       "wbt3kbLanguage": wbt3kbLanguage,
       "wbt3CharacterRepeatDelay": wbt3CharacterRepeatDelay,
       "wbt3CharacterRepeatRate": wbt3CharacterRepeatRate,
       "wbt3Display": wbt3Display,
       "wbt3DispCharacteristic": wbt3DispCharacteristic,
       "wbt3DispFreq": wbt3DispFreq,
       "wbt3DispHorizPix": wbt3DispHorizPix,
       "wbt3DispVertPix": wbt3DispVertPix,
       "wbt3DispColor": wbt3DispColor,
       "wbt3DispUseDDC": wbt3DispUseDDC,
       "wbt3DispCapability": wbt3DispCapability,
       "wbt3DispFreqMax": wbt3DispFreqMax,
       "wbt3DispHorizPixMax": wbt3DispHorizPixMax,
       "wbt3DispVertPixMax": wbt3DispVertPixMax,
       "wbt3DispColorMax": wbt3DispColorMax,
       "wbt3EnergySaver": wbt3EnergySaver,
       "wbt3ScreenTimeOut": wbt3ScreenTimeOut,
       "wbt3TouchScreen": wbt3TouchScreen,
       "wbt3DhcpInfo": wbt3DhcpInfo,
       "wbt3DhcpInfoNum": wbt3DhcpInfoNum,
       "wbt3DhcpInfoTable": wbt3DhcpInfoTable,
       "wbt3DhcpInfoEntry": wbt3DhcpInfoEntry,
       "wbt3DhcpInfoIndex": wbt3DhcpInfoIndex,
       "wbt3InterfaceNum": wbt3InterfaceNum,
       "wbt3ServerIP": wbt3ServerIP,
       "wbt3Username": wbt3Username,
       "wbt3Domain": wbt3Domain,
       "wbt3Password": wbt3Password,
       "wbt3CommandLine": wbt3CommandLine,
       "wbt3WorkingDir": wbt3WorkingDir,
       "wbt3FileServer": wbt3FileServer,
       "wbt3FileRootPath": wbt3FileRootPath,
       "wbt3TrapServerList": wbt3TrapServerList,
       "wbt3SetCommunity": wbt3SetCommunity,
       "wbt3RDPstartApp": wbt3RDPstartApp,
       "wbt3EmulationMode": wbt3EmulationMode,
       "wbt3TerminalID": wbt3TerminalID,
       "wbt3VirtualPortServer": wbt3VirtualPortServer,
       "wbt3DHCPoptionIDs": wbt3DHCPoptionIDs,
       "remoteServer": remoteServer,
       "logonUserName": logonUserName,
       "domain": domain,
       "password": password,
       "commandLine": commandLine,
       "workingDirectory": workingDirectory,
       "rDPStartupApp": rDPStartupApp,
       "fTPFileServer": fTPFileServer,
       "fTPRootPath": fTPRootPath,
       "trapServerList": trapServerList,
       "setCommunity": setCommunity,
       "emulationMode": emulationMode,
       "terminalID": terminalID,
       "virtualPortServer": virtualPortServer,
       "wbt3BuildInfo": wbt3BuildInfo,
       "wbt3CurrentInfo": wbt3CurrentInfo,
       "wbt3CurInfoNum": wbt3CurInfoNum,
       "wbt3CurInfoTable": wbt3CurInfoTable,
       "wbt3CurInfoEntry": wbt3CurInfoEntry,
       "wbt3CurInfoIndex": wbt3CurInfoIndex,
       "wbt3CurBuildNum": wbt3CurBuildNum,
       "wbt3CurOEMBuildNum": wbt3CurOEMBuildNum,
       "wbt3CurModBuildDate": wbt3CurModBuildDate,
       "wbt3CurOEM": wbt3CurOEM,
       "wbt3CurHWPlatform": wbt3CurHWPlatform,
       "wbt3CurOS": wbt3CurOS,
       "wbt3DhcpUpdateInfo": wbt3DhcpUpdateInfo,
       "wbt3DUpInfoNum": wbt3DUpInfoNum,
       "wbt3DUpInfoTable": wbt3DUpInfoTable,
       "wbt3DUpInfoEntry": wbt3DUpInfoEntry,
       "wbt3DUpInfoIndex": wbt3DUpInfoIndex,
       "wbt3DUpBuildNum": wbt3DUpBuildNum,
       "wbt3DUpOEMBuildNum": wbt3DUpOEMBuildNum,
       "wbt3DUpModBuildDate": wbt3DUpModBuildDate,
       "wbt3DUpOEMBuildDate": wbt3DUpOEMBuildDate,
       "wbt3CustomFields": wbt3CustomFields,
       "wbt3CustomField1": wbt3CustomField1,
       "wbt3CustomField2": wbt3CustomField2,
       "wbt3CustomField3": wbt3CustomField3,
       "wbt3Administration": wbt3Administration,
       "wbt3UpDnLoad": wbt3UpDnLoad,
       "wbt3UpDnLoadNum": wbt3UpDnLoadNum,
       "wbt3UpDnLoadTable": wbt3UpDnLoadTable,
       "wbt3UpDnLoadEntry": wbt3UpDnLoadEntry,
       "wbt3UpDnLoadIndex": wbt3UpDnLoadIndex,
       "wbt3UpDnLoadId": wbt3UpDnLoadId,
       "wbt3UpDnLoadOp": wbt3UpDnLoadOp,
       "wbt3UpDnLoadSrcFile": wbt3UpDnLoadSrcFile,
       "wbt3UpDnLoadDstFile": wbt3UpDnLoadDstFile,
       "wbt3UpDnLoadFileType": wbt3UpDnLoadFileType,
       "wbt3UpDnLoadProtocol": wbt3UpDnLoadProtocol,
       "wbt3UpDnLoadFServer": wbt3UpDnLoadFServer,
       "wbt3UpDnLoadTimeFlag": wbt3UpDnLoadTimeFlag,
       "wbt3AcceptReq": wbt3AcceptReq,
       "wbt3SubmitLoadJob": wbt3SubmitLoadJob,
       "wbt3Action": wbt3Action,
       "wbt3RebootRequest": wbt3RebootRequest,
       "wbt3ResetToFactoryDefault": wbt3ResetToFactoryDefault,
       "wbt3FTPsetting": wbt3FTPsetting,
       "wbt3ServerName": wbt3ServerName,
       "wbt3Directory": wbt3Directory,
       "wbt3UserID": wbt3UserID,
       "wbt3Password2": wbt3Password2,
       "wbt3SavePassword": wbt3SavePassword,
       "wbt3InfoLocation": wbt3InfoLocation,
       "wbt3SNMPupdate": wbt3SNMPupdate,
       "wbt3DHCPupdate": wbt3DHCPupdate,
       "wbt3Security": wbt3Security,
       "wbt3SecurityEnable": wbt3SecurityEnable,
       "wbt3HideConfigTab": wbt3HideConfigTab,
       "wbt3FailOverEnable": wbt3FailOverEnable,
       "wbt3MultipleConnect": wbt3MultipleConnect,
       "wbt3PingBeforeConnect": wbt3PingBeforeConnect,
       "wbt3Verbose": wbt3Verbose,
       "wbt3AutoLoginEnable": wbt3AutoLoginEnable,
       "wbt3AutoLoginUserName": wbt3AutoLoginUserName,
       "wbt3SingleButtonConnect": wbt3SingleButtonConnect,
       "wbt3AutoFailRecovery": wbt3AutoFailRecovery,
       "wbt3TrapsInfo": wbt3TrapsInfo,
       "wbt3TrapStatus": wbt3TrapStatus,
       "wbt3TrapReqId": wbt3TrapReqId,
       "wbt3TrapServers": wbt3TrapServers,
       "wbt3TrapServer1": wbt3TrapServer1,
       "wbt3TrapServer2": wbt3TrapServer2,
       "wbt3TrapServer3": wbt3TrapServer3,
       "wbt3TrapServer4": wbt3TrapServer4,
       "wbt3MibRev": wbt3MibRev,
       "wbt3MibRevMajor": wbt3MibRevMajor,
       "wbt3MibRevMinor": wbt3MibRevMinor,
       "wbt3Network": wbt3Network,
       "wbt3NetworkNum": wbt3NetworkNum,
       "wbt3NetworkTable": wbt3NetworkTable,
       "wbt3NetworkEntry": wbt3NetworkEntry,
       "wbt3NetworkIndex": wbt3NetworkIndex,
       "wbt3dhcpEnable": wbt3dhcpEnable,
       "wbt3NetworkAddress": wbt3NetworkAddress,
       "wbt3SubnetMask": wbt3SubnetMask,
       "wbt3Gateway": wbt3Gateway,
       "wbt3dnsEnable": wbt3dnsEnable,
       "wbt3defaultDomain": wbt3defaultDomain,
       "wbt3primaryDNSserverIPaddress": wbt3primaryDNSserverIPaddress,
       "wbt3secondaryDNSserverIPaddress": wbt3secondaryDNSserverIPaddress,
       "wbt3winsEnable": wbt3winsEnable,
       "wbt3primaryWINSserverIPaddress": wbt3primaryWINSserverIPaddress,
       "wbt3secondaryWINSserverIPaddress": wbt3secondaryWINSserverIPaddress,
       "wbt3NetworkSpeed": wbt3NetworkSpeed,
       "wbt3NetworkProtocol": wbt3NetworkProtocol,
       "wbt3Apps": wbt3Apps,
       "wbt3RDPencryption": wbt3RDPencryption,
       "wbt3VirtualPortServerIPaddress": wbt3VirtualPortServerIPaddress,
       "wbt3com1Share": wbt3com1Share,
       "wbt3com2Share": wbt3com2Share,
       "wbt3parallelShare": wbt3parallelShare,
       "iCADefaultHotkeys": iCADefaultHotkeys,
       "defaultHotkeysEntry": defaultHotkeysEntry,
       "iCAStatusDialog": iCAStatusDialog,
       "iCAStatusDialog2": iCAStatusDialog2,
       "iCACloseRemoteApplication": iCACloseRemoteApplication,
       "iCACloseRemoteApplication2": iCACloseRemoteApplication2,
       "iCAtoggleTitleBar": iCAtoggleTitleBar,
       "iCAtoggleTitleBar2": iCAtoggleTitleBar2,
       "iCActrlAltDel": iCActrlAltDel,
       "iCActrlAltDel2": iCActrlAltDel2,
       "iCActrlEsc": iCActrlEsc,
       "iCActrlEsc2": iCActrlEsc2,
       "iCAaltEsc": iCAaltEsc,
       "iCAaltEsc2": iCAaltEsc2,
       "iCAaltTab": iCAaltTab,
       "iCAaltTab2": iCAaltTab2,
       "iCAaltBackTab": iCAaltBackTab,
       "iCAaltBackTab2": iCAaltBackTab2,
       "wbt3Connections": wbt3Connections,
       "wbt3ConnectionsTable": wbt3ConnectionsTable,
       "wbt3ConnectionEntry": wbt3ConnectionEntry,
       "wbt3ConnectionName": wbt3ConnectionName,
       "wbt3ConnectionType": wbt3ConnectionType,
       "wbt3ConnectionEntryStatus": wbt3ConnectionEntryStatus,
       "wbt3RDPConnections": wbt3RDPConnections,
       "wbt3RDPConnTable": wbt3RDPConnTable,
       "wbt3RDPConnEntry": wbt3RDPConnEntry,
       "wbt3RDPConnName": wbt3RDPConnName,
       "wbt3RDPConnServer": wbt3RDPConnServer,
       "wbt3RDPConnLowSpeed": wbt3RDPConnLowSpeed,
       "wbt3RDPConnAutoLogon": wbt3RDPConnAutoLogon,
       "wbt3RDPConnUsername": wbt3RDPConnUsername,
       "wbt3RDPConnDomain": wbt3RDPConnDomain,
       "wbt3RDPConnStartApplication": wbt3RDPConnStartApplication,
       "wbt3RDPConnFilename": wbt3RDPConnFilename,
       "wbt3RDPConnWorkingDir": wbt3RDPConnWorkingDir,
       "wbt3RDPConnModifiable": wbt3RDPConnModifiable,
       "wbt3ICAConnections": wbt3ICAConnections,
       "wbt3ICAConnTable": wbt3ICAConnTable,
       "wbt3ICAConnEntry": wbt3ICAConnEntry,
       "wbt3ICAConnName": wbt3ICAConnName,
       "wbt3ICAConnCommType": wbt3ICAConnCommType,
       "wbt3ICAConnServer": wbt3ICAConnServer,
       "wbt3ICAConnCommandLine": wbt3ICAConnCommandLine,
       "wbt3ICAConnWorkingDir": wbt3ICAConnWorkingDir,
       "wbt3ICAConnUsername": wbt3ICAConnUsername,
       "wbt3ICAConnDomain": wbt3ICAConnDomain,
       "wbt3ICAConnColors": wbt3ICAConnColors,
       "wbt3ICAConnDataCompress": wbt3ICAConnDataCompress,
       "wbt3ICAConnSoundQuality": wbt3ICAConnSoundQuality,
       "wbt3ICAConnModifiable": wbt3ICAConnModifiable,
       "wbt3TermConnections": wbt3TermConnections,
       "wbt3TermConnTable": wbt3TermConnTable,
       "wbt3TermConnEntry": wbt3TermConnEntry,
       "wbt3TermConnName": wbt3TermConnName,
       "wbt3TermConnCommType": wbt3TermConnCommType,
       "wbt3TermConnServer": wbt3TermConnServer,
       "wbt3TermConnEmuType": wbt3TermConnEmuType,
       "wbt3TermConnVTEmuModel": wbt3TermConnVTEmuModel,
       "wbt3TermConnIBM3270EmuModel": wbt3TermConnIBM3270EmuModel,
       "wbt3TermConnIBM5250EmuModel": wbt3TermConnIBM5250EmuModel,
       "wbt3TermConnPortNumber": wbt3TermConnPortNumber,
       "wbt3TermConnTelnetName": wbt3TermConnTelnetName,
       "wbt3TermConnPrinterPort": wbt3TermConnPrinterPort,
       "wbt3TermConnFormFeed": wbt3TermConnFormFeed,
       "wbt3TermConnAutoLineFeed": wbt3TermConnAutoLineFeed,
       "wbt3TermConnScript": wbt3TermConnScript,
       "wbt3TermConnModifiable": wbt3TermConnModifiable,
       "wbt3Users": wbt3Users,
       "wbt3UsersTable": wbt3UsersTable,
       "wbt3UsersEntry": wbt3UsersEntry,
       "wbt3UsersStatus": wbt3UsersStatus,
       "wbt3userName": wbt3userName,
       "wbt3password": wbt3password,
       "wbt3privilege": wbt3privilege,
       "wbt3Connection1": wbt3Connection1,
       "wbt3Connection2": wbt3Connection2,
       "wbt3Connection3": wbt3Connection3,
       "wbt3Connection4": wbt3Connection4,
       "wbt3Connection5": wbt3Connection5,
       "wbt3Connection6": wbt3Connection6,
       "wbt3Connection7": wbt3Connection7,
       "wbt3Connection8": wbt3Connection8,
       "wbt3AutoStart1": wbt3AutoStart1,
       "wbt3AutoStart2": wbt3AutoStart2,
       "wbt3AutoStart3": wbt3AutoStart3,
       "wbt3AutoStart4": wbt3AutoStart4,
       "wbt3AutoStart5": wbt3AutoStart5,
       "wbt3AutoStart6": wbt3AutoStart6,
       "wbt3AutoStart7": wbt3AutoStart7,
       "wbt3AutoStart8": wbt3AutoStart8,
       "wbt3UserPasswordChange": wbt3UserPasswordChange}
)
