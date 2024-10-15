# SNMP MIB module (CARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:33 2024
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

(card,
 coriolisMibs) = mibBuilder.importSymbols(
    "CORIOLIS-MIB",
    "card",
    "coriolisMibs")

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
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _CardCount_Type(Integer32):
    """Custom type cardCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_CardCount_Type.__name__ = "Integer32"
_CardCount_Object = MibScalar
cardCount = _CardCount_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 2),
    _CardCount_Type()
)
cardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCount.setStatus("current")
_CardEEPromTable_Object = MibTable
cardEEPromTable = _CardEEPromTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3)
)
if mibBuilder.loadTexts:
    cardEEPromTable.setStatus("current")
_CardEEPromEntry_Object = MibTableRow
cardEEPromEntry = _CardEEPromEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1)
)
cardEEPromEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
)
if mibBuilder.loadTexts:
    cardEEPromEntry.setStatus("current")


class _SlotNo_Type(Integer32):
    """Custom type slotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_SlotNo_Type.__name__ = "Integer32"
_SlotNo_Object = MibTableColumn
slotNo = _SlotNo_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 1),
    _SlotNo_Type()
)
slotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slotNo.setStatus("current")


class _CardSIDFVer_Type(OctetString):
    """Custom type cardSIDFVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CardSIDFVer_Type.__name__ = "OctetString"
_CardSIDFVer_Object = MibTableColumn
cardSIDFVer = _CardSIDFVer_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 2),
    _CardSIDFVer_Type()
)
cardSIDFVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSIDFVer.setStatus("current")


class _CardHwType_Type(Integer32):
    """Custom type cardHwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
        *(("atmOC12c", 10),
          ("atmOC3c", 9),
          ("csOSU", 20),
          ("dwdmOSU", 18),
          ("dwdmOSU14", 23),
          ("eth16", 8),
          ("fmOTU", 22),
          ("gigio", 16),
          ("mm", 1),
          ("oauEth16DS1Fx", 25),
          ("oauEth16Gig1FX", 21),
          ("oauGig4Fx", 26),
          ("posOC12c", 27),
          ("posOC48c", 28),
          ("rx1310", 4),
          ("rxDWDM", 6),
          ("smOSU", 2),
          ("smOTU", 17),
          ("tdmDS1", 11),
          ("tdmDS3", 12),
          ("tdmOC12c", 14),
          ("tdmOC3c", 13),
          ("thirteenTenOSU", 19),
          ("thirteenTenOSU14", 24),
          ("tx1310", 5),
          ("txDWDM", 7))
    )


_CardHwType_Type.__name__ = "Integer32"
_CardHwType_Object = MibTableColumn
cardHwType = _CardHwType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 3),
    _CardHwType_Type()
)
cardHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHwType.setStatus("current")


class _CardHwSubType_Type(OctetString):
    """Custom type cardHwSubType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CardHwSubType_Type.__name__ = "OctetString"
_CardHwSubType_Object = MibTableColumn
cardHwSubType = _CardHwSubType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 4),
    _CardHwSubType_Type()
)
cardHwSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHwSubType.setStatus("current")


class _CardImageType_Type(Integer32):
    """Custom type cardImageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_CardImageType_Type.__name__ = "Integer32"
_CardImageType_Object = MibTableColumn
cardImageType = _CardImageType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 5),
    _CardImageType_Type()
)
cardImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardImageType.setStatus("current")


class _CardMACaddressNum_Type(Integer32):
    """Custom type cardMACaddressNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CardMACaddressNum_Type.__name__ = "Integer32"
_CardMACaddressNum_Object = MibTableColumn
cardMACaddressNum = _CardMACaddressNum_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 6),
    _CardMACaddressNum_Type()
)
cardMACaddressNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMACaddressNum.setStatus("current")


class _CardMacAddress_Type(OctetString):
    """Custom type cardMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CardMacAddress_Type.__name__ = "OctetString"
_CardMacAddress_Object = MibTableColumn
cardMacAddress = _CardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 7),
    _CardMacAddress_Type()
)
cardMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMacAddress.setStatus("current")


class _CardAssemblyClass_Type(Integer32):
    """Custom type cardAssemblyClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CardAssemblyClass_Type.__name__ = "Integer32"
_CardAssemblyClass_Object = MibTableColumn
cardAssemblyClass = _CardAssemblyClass_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 8),
    _CardAssemblyClass_Type()
)
cardAssemblyClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAssemblyClass.setStatus("current")
_CardAssemblyId_Type = OctetString
_CardAssemblyId_Object = MibTableColumn
cardAssemblyId = _CardAssemblyId_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 9),
    _CardAssemblyId_Type()
)
cardAssemblyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAssemblyId.setStatus("current")


class _CardAssemblyTabNum_Type(Integer32):
    """Custom type cardAssemblyTabNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CardAssemblyTabNum_Type.__name__ = "Integer32"
_CardAssemblyTabNum_Object = MibTableColumn
cardAssemblyTabNum = _CardAssemblyTabNum_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 10),
    _CardAssemblyTabNum_Type()
)
cardAssemblyTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAssemblyTabNum.setStatus("current")
_CardAssemblyRev_Type = Unsigned32
_CardAssemblyRev_Object = MibTableColumn
cardAssemblyRev = _CardAssemblyRev_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 11),
    _CardAssemblyRev_Type()
)
cardAssemblyRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAssemblyRev.setStatus("current")
_Cardbrchecksum_Type = Integer32
_Cardbrchecksum_Object = MibTableColumn
cardbrchecksum = _Cardbrchecksum_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 12),
    _Cardbrchecksum_Type()
)
cardbrchecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardbrchecksum.setStatus("current")
_CardSIDInfoVersion_Type = Unsigned32
_CardSIDInfoVersion_Object = MibTableColumn
cardSIDInfoVersion = _CardSIDInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 13),
    _CardSIDInfoVersion_Type()
)
cardSIDInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSIDInfoVersion.setStatus("current")


class _CardSerialNum_Type(OctetString):
    """Custom type cardSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CardSerialNum_Type.__name__ = "OctetString"
_CardSerialNum_Object = MibTableColumn
cardSerialNum = _CardSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 14),
    _CardSerialNum_Type()
)
cardSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSerialNum.setStatus("current")


class _CardAssemblyNumString_Type(OctetString):
    """Custom type cardAssemblyNumString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CardAssemblyNumString_Type.__name__ = "OctetString"
_CardAssemblyNumString_Object = MibTableColumn
cardAssemblyNumString = _CardAssemblyNumString_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 15),
    _CardAssemblyNumString_Type()
)
cardAssemblyNumString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAssemblyNumString.setStatus("current")


class _CardAssemblyRevString_Type(OctetString):
    """Custom type cardAssemblyRevString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CardAssemblyRevString_Type.__name__ = "OctetString"
_CardAssemblyRevString_Object = MibTableColumn
cardAssemblyRevString = _CardAssemblyRevString_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 16),
    _CardAssemblyRevString_Type()
)
cardAssemblyRevString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardAssemblyRevString.setStatus("current")


class _CardCLEICode_Type(OctetString):
    """Custom type cardCLEICode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CardCLEICode_Type.__name__ = "OctetString"
_CardCLEICode_Object = MibTableColumn
cardCLEICode = _CardCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 17),
    _CardCLEICode_Type()
)
cardCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCLEICode.setStatus("current")


class _CardCLEIECICode_Type(OctetString):
    """Custom type cardCLEIECICode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CardCLEIECICode_Type.__name__ = "OctetString"
_CardCLEIECICode_Object = MibTableColumn
cardCLEIECICode = _CardCLEIECICode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 18),
    _CardCLEIECICode_Type()
)
cardCLEIECICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCLEIECICode.setStatus("current")
_CardChecksum_Type = Integer32
_CardChecksum_Object = MibTableColumn
cardChecksum = _CardChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 19),
    _CardChecksum_Type()
)
cardChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardChecksum.setStatus("current")
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("current")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1)
)
slotEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("current")


class _SlotAdminState_Type(Integer32):
    """Custom type slotAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SlotAdminState_Type.__name__ = "Integer32"
_SlotAdminState_Object = MibTableColumn
slotAdminState = _SlotAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 1),
    _SlotAdminState_Type()
)
slotAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotAdminState.setStatus("current")


class _SlotOperState_Type(Integer32):
    """Custom type slotOperState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("configFailed", 5),
          ("configStarted", 4),
          ("configed", 6),
          ("designModeReady", 10),
          ("ready", 7),
          ("removed", 0),
          ("syncFailed", 3),
          ("syncWait", 1),
          ("synced", 2),
          ("waitDeconfig", 9),
          ("waitSM", 8))
    )


_SlotOperState_Type.__name__ = "Integer32"
_SlotOperState_Object = MibTableColumn
slotOperState = _SlotOperState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 2),
    _SlotOperState_Type()
)
slotOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotOperState.setStatus("current")


class _SlotType_Type(Integer32):
    """Custom type slotType based on Integer32"""
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
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("colorSeparator", 6),
          ("mmSlot", 1),
          ("oauEth", 11),
          ("oauGig", 12),
          ("oauMM", 13),
          ("oauOptics", 15),
          ("oauSM", 14),
          ("optiFlow3xOpticsSlot", 7),
          ("optiFlow3xSMSlot", 2),
          ("optiFlow3xSlotNumber1", 5),
          ("optiFlow5xFramerModuleSlot", 10),
          ("optiFlow5xOpticsSlotType1", 8),
          ("optiFlow5xOpticsSlotType2", 9),
          ("optiFlow5xSMSlot", 3),
          ("regularIOSlot", 4))
    )


_SlotType_Type.__name__ = "Integer32"
_SlotType_Object = MibTableColumn
slotType = _SlotType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 3),
    _SlotType_Type()
)
slotType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotType.setStatus("current")


class _SlotCardType_Type(Integer32):
    """Custom type slotCardType based on Integer32"""
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
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("atmOC12c", 10),
          ("atmOC3c", 9),
          ("csOSU", 20),
          ("dwdmOSU", 18),
          ("eth16", 8),
          ("fifteenFiftyOSU14", 29),
          ("gigio", 16),
          ("islgmac", 15),
          ("mm", 1),
          ("oau1550Eth16Gig1Fx", 31),
          ("oauEth16Ds1Fx", 25),
          ("oauEth16Gig1Fx", 21),
          ("oauFmOTU", 22),
          ("oauGig4Fx", 26),
          ("osu14DWDM", 23),
          ("posOC12c", 27),
          ("posOC48c", 28),
          ("rx1310", 4),
          ("rxDWDM", 6),
          ("smISM", 3),
          ("smOSU", 2),
          ("smOTU", 17),
          ("tdmDS1", 11),
          ("tdmDS3", 12),
          ("tdmOC12c", 14),
          ("tdmOC3c", 13),
          ("thirteenTenOSU", 19),
          ("thirteenTenOSU14", 24),
          ("tx1310", 5),
          ("tx1550", 30),
          ("txDWDM", 7))
    )


_SlotCardType_Type.__name__ = "Integer32"
_SlotCardType_Object = MibTableColumn
slotCardType = _SlotCardType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 4),
    _SlotCardType_Type()
)
slotCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotCardType.setStatus("current")


class _SlotConnectionSize_Type(Integer32):
    """Custom type slotConnectionSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("sm16", 2),
          ("sm8", 1))
    )


_SlotConnectionSize_Type.__name__ = "Integer32"
_SlotConnectionSize_Object = MibTableColumn
slotConnectionSize = _SlotConnectionSize_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 5),
    _SlotConnectionSize_Type()
)
slotConnectionSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotConnectionSize.setStatus("current")
_SlotSMSlot_Type = Integer32
_SlotSMSlot_Object = MibTableColumn
slotSMSlot = _SlotSMSlot_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 6),
    _SlotSMSlot_Type()
)
slotSMSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotSMSlot.setStatus("current")


class _SlotInsertState_Type(Integer32):
    """Custom type slotInsertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SlotInsertState_Type.__name__ = "Integer32"
_SlotInsertState_Object = MibTableColumn
slotInsertState = _SlotInsertState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 7),
    _SlotInsertState_Type()
)
slotInsertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotInsertState.setStatus("current")


class _SlotFileState_Type(Integer32):
    """Custom type slotFileState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("locked", 3),
          ("ready", 2))
    )


_SlotFileState_Type.__name__ = "Integer32"
_SlotFileState_Object = MibTableColumn
slotFileState = _SlotFileState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 8),
    _SlotFileState_Type()
)
slotFileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotFileState.setStatus("current")


class _SlotModuleChangeStatus_Type(Integer32):
    """Custom type slotModuleChangeStatus based on Integer32"""
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
        *(("configDeleted", 8),
          ("configFailCardTypeMismatch", 9),
          ("configFailOutOfSwitchPorts", 11),
          ("configFailSMNotAvailable", 10),
          ("configFailure", 7),
          ("configured", 5),
          ("failover", 4),
          ("failure", 3),
          ("inserted", 1),
          ("moduleConfigurationCorrupt", 12),
          ("removed", 2),
          ("syncpointFailure", 6),
          ("warmBoot", 13))
    )


_SlotModuleChangeStatus_Type.__name__ = "Integer32"
_SlotModuleChangeStatus_Object = MibTableColumn
slotModuleChangeStatus = _SlotModuleChangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 9),
    _SlotModuleChangeStatus_Type()
)
slotModuleChangeStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slotModuleChangeStatus.setStatus("current")


class _SlotModuleTempStatus_Type(Integer32):
    """Custom type slotModuleTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hot", 1),
          ("normal", 2))
    )


_SlotModuleTempStatus_Type.__name__ = "Integer32"
_SlotModuleTempStatus_Object = MibTableColumn
slotModuleTempStatus = _SlotModuleTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 10),
    _SlotModuleTempStatus_Type()
)
slotModuleTempStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slotModuleTempStatus.setStatus("current")


class _SlotIoCardStatus_Type(Integer32):
    """Custom type slotIoCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("responsive", 2),
          ("unresponsive", 1))
    )


_SlotIoCardStatus_Type.__name__ = "Integer32"
_SlotIoCardStatus_Object = MibTableColumn
slotIoCardStatus = _SlotIoCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 11),
    _SlotIoCardStatus_Type()
)
slotIoCardStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slotIoCardStatus.setStatus("current")
_SlotFlashThreshold_Type = Integer32
_SlotFlashThreshold_Object = MibTableColumn
slotFlashThreshold = _SlotFlashThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 12),
    _SlotFlashThreshold_Type()
)
slotFlashThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slotFlashThreshold.setStatus("current")
_SlotFlashSectorsOverThreshold_Type = Integer32
_SlotFlashSectorsOverThreshold_Object = MibTableColumn
slotFlashSectorsOverThreshold = _SlotFlashSectorsOverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 13),
    _SlotFlashSectorsOverThreshold_Type()
)
slotFlashSectorsOverThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slotFlashSectorsOverThreshold.setStatus("current")
_TdmIoCardTable_Object = MibTable
tdmIoCardTable = _TdmIoCardTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 5)
)
if mibBuilder.loadTexts:
    tdmIoCardTable.setStatus("current")
_TdmIoCardEntry_Object = MibTableRow
tdmIoCardEntry = _TdmIoCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 5, 1)
)
tdmIoCardEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
)
if mibBuilder.loadTexts:
    tdmIoCardEntry.setStatus("current")


class _TdmIoCardType_Type(Integer32):
    """Custom type tdmIoCardType based on Integer32"""
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
        *(("ds1", 1),
          ("ds3", 2),
          ("e1", 5),
          ("e3", 6),
          ("oc12", 4),
          ("oc3", 3))
    )


_TdmIoCardType_Type.__name__ = "Integer32"
_TdmIoCardType_Object = MibTableColumn
tdmIoCardType = _TdmIoCardType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 1),
    _TdmIoCardType_Type()
)
tdmIoCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoCardType.setStatus("current")


class _TdmIoCardOperState_Type(Integer32):
    """Custom type tdmIoCardOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TdmIoCardOperState_Type.__name__ = "Integer32"
_TdmIoCardOperState_Object = MibTableColumn
tdmIoCardOperState = _TdmIoCardOperState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 2),
    _TdmIoCardOperState_Type()
)
tdmIoCardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIoCardOperState.setStatus("current")


class _TdmIoCardMode_Type(Integer32):
    """Custom type tdmIoCardMode based on Integer32"""
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
        *(("au3mode", 4),
          ("channelized", 2),
          ("ds3Channelized", 6),
          ("ds3ClearChannel", 5),
          ("sts1mode", 3),
          ("unchannelized", 1))
    )


_TdmIoCardMode_Type.__name__ = "Integer32"
_TdmIoCardMode_Object = MibTableColumn
tdmIoCardMode = _TdmIoCardMode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 3),
    _TdmIoCardMode_Type()
)
tdmIoCardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoCardMode.setStatus("current")
_TdmIoCardConfiguredPorts_Type = Unsigned32
_TdmIoCardConfiguredPorts_Object = MibTableColumn
tdmIoCardConfiguredPorts = _TdmIoCardConfiguredPorts_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 4),
    _TdmIoCardConfiguredPorts_Type()
)
tdmIoCardConfiguredPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmIoCardConfiguredPorts.setStatus("current")


class _TdmIoCardRowStatus_Type(Integer32):
    """Custom type tdmIoCardRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
          ("notInService", 2))
    )


_TdmIoCardRowStatus_Type.__name__ = "Integer32"
_TdmIoCardRowStatus_Object = MibTableColumn
tdmIoCardRowStatus = _TdmIoCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 5),
    _TdmIoCardRowStatus_Type()
)
tdmIoCardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoCardRowStatus.setStatus("current")
_TdmIoCardNumPMIntervals_Type = Unsigned32
_TdmIoCardNumPMIntervals_Object = MibTableColumn
tdmIoCardNumPMIntervals = _TdmIoCardNumPMIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 6),
    _TdmIoCardNumPMIntervals_Type()
)
tdmIoCardNumPMIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdmIoCardNumPMIntervals.setStatus("current")
_EtherCardTable_Object = MibTable
etherCardTable = _EtherCardTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 6)
)
if mibBuilder.loadTexts:
    etherCardTable.setStatus("current")
_EtherCardEntry_Object = MibTableRow
etherCardEntry = _EtherCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 6, 1)
)
etherCardEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
)
if mibBuilder.loadTexts:
    etherCardEntry.setStatus("current")


class _EtherCardOperState_Type(Integer32):
    """Custom type etherCardOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EtherCardOperState_Type.__name__ = "Integer32"
_EtherCardOperState_Object = MibTableColumn
etherCardOperState = _EtherCardOperState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 1),
    _EtherCardOperState_Type()
)
etherCardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherCardOperState.setStatus("current")


class _EtherCardActivePortMask_Type(Integer32):
    """Custom type etherCardActivePortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtherCardActivePortMask_Type.__name__ = "Integer32"
_EtherCardActivePortMask_Object = MibTableColumn
etherCardActivePortMask = _EtherCardActivePortMask_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 2),
    _EtherCardActivePortMask_Type()
)
etherCardActivePortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherCardActivePortMask.setStatus("current")


class _EtherCardPhyResetState_Type(Integer32):
    """Custom type etherCardPhyResetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inReset", 1),
          ("outOfReset", 2))
    )


_EtherCardPhyResetState_Type.__name__ = "Integer32"
_EtherCardPhyResetState_Object = MibTableColumn
etherCardPhyResetState = _EtherCardPhyResetState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 3),
    _EtherCardPhyResetState_Type()
)
etherCardPhyResetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherCardPhyResetState.setStatus("current")


class _EtherCardRowStatus_Type(Integer32):
    """Custom type etherCardRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
          ("notInService", 2))
    )


_EtherCardRowStatus_Type.__name__ = "Integer32"
_EtherCardRowStatus_Object = MibTableColumn
etherCardRowStatus = _EtherCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 4),
    _EtherCardRowStatus_Type()
)
etherCardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherCardRowStatus.setStatus("current")
_AtmCardTable_Object = MibTable
atmCardTable = _AtmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 7)
)
if mibBuilder.loadTexts:
    atmCardTable.setStatus("current")
_AtmCardEntry_Object = MibTableRow
atmCardEntry = _AtmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 7, 1)
)
atmCardEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
)
if mibBuilder.loadTexts:
    atmCardEntry.setStatus("current")


class _AtmCardOperState_Type(Integer32):
    """Custom type atmCardOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmCardOperState_Type.__name__ = "Integer32"
_AtmCardOperState_Object = MibTableColumn
atmCardOperState = _AtmCardOperState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 7, 1, 1),
    _AtmCardOperState_Type()
)
atmCardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCardOperState.setStatus("current")


class _AtmCardActivePortMask_Type(Integer32):
    """Custom type atmCardActivePortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AtmCardActivePortMask_Type.__name__ = "Integer32"
_AtmCardActivePortMask_Object = MibTableColumn
atmCardActivePortMask = _AtmCardActivePortMask_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 7, 1, 2),
    _AtmCardActivePortMask_Type()
)
atmCardActivePortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCardActivePortMask.setStatus("current")


class _AtmCardRowStatus_Type(Integer32):
    """Custom type atmCardRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
          ("notInService", 2))
    )


_AtmCardRowStatus_Type.__name__ = "Integer32"
_AtmCardRowStatus_Object = MibTableColumn
atmCardRowStatus = _AtmCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 7, 1, 3),
    _AtmCardRowStatus_Type()
)
atmCardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCardRowStatus.setStatus("current")
_OpticalCardTable_Object = MibTable
opticalCardTable = _OpticalCardTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 8)
)
if mibBuilder.loadTexts:
    opticalCardTable.setStatus("current")
_OpticalCardEntry_Object = MibTableRow
opticalCardEntry = _OpticalCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 8, 1)
)
opticalCardEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
)
if mibBuilder.loadTexts:
    opticalCardEntry.setStatus("current")


class _OpticalCardSlotType_Type(Integer32):
    """Custom type opticalCardSlotType based on Integer32"""
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
        *(("oauEth16Gig1", 5),
          ("rxOTU", 1),
          ("txOTU", 2),
          ("txRxOSU", 3),
          ("txRxOSU14", 4))
    )


_OpticalCardSlotType_Type.__name__ = "Integer32"
_OpticalCardSlotType_Object = MibTableColumn
opticalCardSlotType = _OpticalCardSlotType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 8, 1, 1),
    _OpticalCardSlotType_Type()
)
opticalCardSlotType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalCardSlotType.setStatus("current")


class _OpticalCardOpticsType_Type(Integer32):
    """Custom type opticalCardOpticsType based on Integer32"""
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
        *(("dwdm", 1),
          ("fifteenFifty", 3),
          ("thirteenTen", 2),
          ("thirteenTenFifteenFifty", 4))
    )


_OpticalCardOpticsType_Type.__name__ = "Integer32"
_OpticalCardOpticsType_Object = MibTableColumn
opticalCardOpticsType = _OpticalCardOpticsType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 8, 1, 2),
    _OpticalCardOpticsType_Type()
)
opticalCardOpticsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalCardOpticsType.setStatus("current")


class _OpticalCardRowStatus_Type(Integer32):
    """Custom type opticalCardRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createAndGo", 4),
          ("destroy", 6))
    )


_OpticalCardRowStatus_Type.__name__ = "Integer32"
_OpticalCardRowStatus_Object = MibTableColumn
opticalCardRowStatus = _OpticalCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 8, 1, 3),
    _OpticalCardRowStatus_Type()
)
opticalCardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalCardRowStatus.setStatus("current")
_PosCardTable_Object = MibTable
posCardTable = _PosCardTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 9)
)
if mibBuilder.loadTexts:
    posCardTable.setStatus("current")
_PosCardEntry_Object = MibTableRow
posCardEntry = _PosCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 9, 1)
)
posCardEntry.setIndexNames(
    (0, "CARD-MIB", "slotNo"),
)
if mibBuilder.loadTexts:
    posCardEntry.setStatus("current")
_PosCardActivePortMask_Type = Unsigned32
_PosCardActivePortMask_Object = MibTableColumn
posCardActivePortMask = _PosCardActivePortMask_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 9, 1, 1),
    _PosCardActivePortMask_Type()
)
posCardActivePortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posCardActivePortMask.setStatus("current")


class _PosCardPhyResetState_Type(Integer32):
    """Custom type posCardPhyResetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inReset", 1),
          ("outOfReset", 2))
    )


_PosCardPhyResetState_Type.__name__ = "Integer32"
_PosCardPhyResetState_Object = MibTableColumn
posCardPhyResetState = _PosCardPhyResetState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 2, 9, 1, 2),
    _PosCardPhyResetState_Type()
)
posCardPhyResetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posCardPhyResetState.setStatus("current")

# Managed Objects groups


# Notification objects

moduleStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 2)
)
moduleStatusChange.setObjects(
      *(("CARD-MIB", "slotModuleChangeStatus"),
        ("CARD-MIB", "cardHwType"))
)
if mibBuilder.loadTexts:
    moduleStatusChange.setStatus(
        ""
    )

moduleTempChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 44)
)
moduleTempChange.setObjects(
    ("CARD-MIB", "slotModuleTempStatus")
)
if mibBuilder.loadTexts:
    moduleTempChange.setStatus(
        ""
    )

ioCardStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 45)
)
ioCardStatusChange.setObjects(
    ("CARD-MIB", "slotIoCardStatus")
)
if mibBuilder.loadTexts:
    ioCardStatusChange.setStatus(
        ""
    )

emFlashLife = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 46)
)
emFlashLife.setObjects(
      *(("CARD-MIB", "slotFlashThreshold"),
        ("CARD-MIB", "slotFlashSectorsOverThreshold"))
)
if mibBuilder.loadTexts:
    emFlashLife.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CARD-MIB",
    **{"moduleStatusChange": moduleStatusChange,
       "moduleTempChange": moduleTempChange,
       "ioCardStatusChange": ioCardStatusChange,
       "emFlashLife": emFlashLife,
       "cardMIB": cardMIB,
       "cardCount": cardCount,
       "cardEEPromTable": cardEEPromTable,
       "cardEEPromEntry": cardEEPromEntry,
       "slotNo": slotNo,
       "cardSIDFVer": cardSIDFVer,
       "cardHwType": cardHwType,
       "cardHwSubType": cardHwSubType,
       "cardImageType": cardImageType,
       "cardMACaddressNum": cardMACaddressNum,
       "cardMacAddress": cardMacAddress,
       "cardAssemblyClass": cardAssemblyClass,
       "cardAssemblyId": cardAssemblyId,
       "cardAssemblyTabNum": cardAssemblyTabNum,
       "cardAssemblyRev": cardAssemblyRev,
       "cardbrchecksum": cardbrchecksum,
       "cardSIDInfoVersion": cardSIDInfoVersion,
       "cardSerialNum": cardSerialNum,
       "cardAssemblyNumString": cardAssemblyNumString,
       "cardAssemblyRevString": cardAssemblyRevString,
       "cardCLEICode": cardCLEICode,
       "cardCLEIECICode": cardCLEIECICode,
       "cardChecksum": cardChecksum,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "slotAdminState": slotAdminState,
       "slotOperState": slotOperState,
       "slotType": slotType,
       "slotCardType": slotCardType,
       "slotConnectionSize": slotConnectionSize,
       "slotSMSlot": slotSMSlot,
       "slotInsertState": slotInsertState,
       "slotFileState": slotFileState,
       "slotModuleChangeStatus": slotModuleChangeStatus,
       "slotModuleTempStatus": slotModuleTempStatus,
       "slotIoCardStatus": slotIoCardStatus,
       "slotFlashThreshold": slotFlashThreshold,
       "slotFlashSectorsOverThreshold": slotFlashSectorsOverThreshold,
       "tdmIoCardTable": tdmIoCardTable,
       "tdmIoCardEntry": tdmIoCardEntry,
       "tdmIoCardType": tdmIoCardType,
       "tdmIoCardOperState": tdmIoCardOperState,
       "tdmIoCardMode": tdmIoCardMode,
       "tdmIoCardConfiguredPorts": tdmIoCardConfiguredPorts,
       "tdmIoCardRowStatus": tdmIoCardRowStatus,
       "tdmIoCardNumPMIntervals": tdmIoCardNumPMIntervals,
       "etherCardTable": etherCardTable,
       "etherCardEntry": etherCardEntry,
       "etherCardOperState": etherCardOperState,
       "etherCardActivePortMask": etherCardActivePortMask,
       "etherCardPhyResetState": etherCardPhyResetState,
       "etherCardRowStatus": etherCardRowStatus,
       "atmCardTable": atmCardTable,
       "atmCardEntry": atmCardEntry,
       "atmCardOperState": atmCardOperState,
       "atmCardActivePortMask": atmCardActivePortMask,
       "atmCardRowStatus": atmCardRowStatus,
       "opticalCardTable": opticalCardTable,
       "opticalCardEntry": opticalCardEntry,
       "opticalCardSlotType": opticalCardSlotType,
       "opticalCardOpticsType": opticalCardOpticsType,
       "opticalCardRowStatus": opticalCardRowStatus,
       "posCardTable": posCardTable,
       "posCardEntry": posCardEntry,
       "posCardActivePortMask": posCardActivePortMask,
       "posCardPhyResetState": posCardPhyResetState}
)
