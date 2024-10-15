# SNMP MIB module (ASCEND-MIBSPARING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSPARING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:14 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MiblimSparingConfigProfile_ObjectIdentity = ObjectIdentity
miblimSparingConfigProfile = _MiblimSparingConfigProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 12)
)
_MiblimSparingConfigProfileTable_Object = MibTable
miblimSparingConfigProfileTable = _MiblimSparingConfigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1)
)
if mibBuilder.loadTexts:
    miblimSparingConfigProfileTable.setStatus("mandatory")
_MiblimSparingConfigProfileEntry_Object = MibTableRow
miblimSparingConfigProfileEntry = _MiblimSparingConfigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1)
)
miblimSparingConfigProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSPARING-MIB", "limSparingConfigProfile-Shelf-o"),
    (0, "ASCEND-MIBSPARING-MIB", "limSparingConfigProfile-Slot-o"),
    (0, "ASCEND-MIBSPARING-MIB", "limSparingConfigProfile-Item-o"),
)
if mibBuilder.loadTexts:
    miblimSparingConfigProfileEntry.setStatus("mandatory")


class _LimSparingConfigProfile_SparingMode_Type(Integer32):
    """Custom type limSparingConfigProfile_SparingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 3),
          ("inactive", 1),
          ("manual", 2))
    )


_LimSparingConfigProfile_SparingMode_Type.__name__ = "Integer32"
_LimSparingConfigProfile_SparingMode_Object = MibScalar
limSparingConfigProfile_SparingMode = _LimSparingConfigProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 2),
    _LimSparingConfigProfile_SparingMode_Type()
)
limSparingConfigProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_SparingMode.setStatus("mandatory")


class _LimSparingConfigProfile_SpareSlotNumber_Type(Integer32):
    """Custom type limSparingConfigProfile_SpareSlotNumber based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              45,
              46,
              49,
              50,
              51,
              53,
              54,
              55,
              56,
              57,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("aLim", 55),
          ("anySlot", 1),
          ("bLim", 56),
          ("cLim", 57),
          ("controlModule", 51),
          ("controller", 42),
          ("dLim", 58),
          ("firstControlModule", 53),
          ("leftController", 49),
          ("rightController", 50),
          ("secondControlModule", 54),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot17", 18),
          ("slot18", 19),
          ("slot19", 20),
          ("slot2", 3),
          ("slot20", 21),
          ("slot21", 22),
          ("slot22", 23),
          ("slot23", 24),
          ("slot24", 25),
          ("slot25", 26),
          ("slot26", 27),
          ("slot27", 28),
          ("slot28", 29),
          ("slot29", 30),
          ("slot3", 4),
          ("slot30", 31),
          ("slot31", 32),
          ("slot32", 33),
          ("slot33", 34),
          ("slot34", 35),
          ("slot35", 36),
          ("slot36", 37),
          ("slot37", 38),
          ("slot38", 39),
          ("slot39", 40),
          ("slot4", 5),
          ("slot40", 41),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8),
          ("slot8", 9),
          ("slot9", 10),
          ("slotPrimary", 59),
          ("trunkModule1", 45),
          ("trunkModule2", 46))
    )


_LimSparingConfigProfile_SpareSlotNumber_Type.__name__ = "Integer32"
_LimSparingConfigProfile_SpareSlotNumber_Object = MibScalar
limSparingConfigProfile_SpareSlotNumber = _LimSparingConfigProfile_SpareSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 3),
    _LimSparingConfigProfile_SpareSlotNumber_Type()
)
limSparingConfigProfile_SpareSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_SpareSlotNumber.setStatus("mandatory")


class _LimSparingConfigProfile_ManuallySparedSlotNumber_Type(Integer32):
    """Custom type limSparingConfigProfile_ManuallySparedSlotNumber based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              45,
              46,
              49,
              50,
              51,
              53,
              54,
              55,
              56,
              57,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("aLim", 55),
          ("anySlot", 1),
          ("bLim", 56),
          ("cLim", 57),
          ("controlModule", 51),
          ("controller", 42),
          ("dLim", 58),
          ("firstControlModule", 53),
          ("leftController", 49),
          ("rightController", 50),
          ("secondControlModule", 54),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot17", 18),
          ("slot18", 19),
          ("slot19", 20),
          ("slot2", 3),
          ("slot20", 21),
          ("slot21", 22),
          ("slot22", 23),
          ("slot23", 24),
          ("slot24", 25),
          ("slot25", 26),
          ("slot26", 27),
          ("slot27", 28),
          ("slot28", 29),
          ("slot29", 30),
          ("slot3", 4),
          ("slot30", 31),
          ("slot31", 32),
          ("slot32", 33),
          ("slot33", 34),
          ("slot34", 35),
          ("slot35", 36),
          ("slot36", 37),
          ("slot37", 38),
          ("slot38", 39),
          ("slot39", 40),
          ("slot4", 5),
          ("slot40", 41),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8),
          ("slot8", 9),
          ("slot9", 10),
          ("slotPrimary", 59),
          ("trunkModule1", 45),
          ("trunkModule2", 46))
    )


_LimSparingConfigProfile_ManuallySparedSlotNumber_Type.__name__ = "Integer32"
_LimSparingConfigProfile_ManuallySparedSlotNumber_Object = MibScalar
limSparingConfigProfile_ManuallySparedSlotNumber = _LimSparingConfigProfile_ManuallySparedSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 4),
    _LimSparingConfigProfile_ManuallySparedSlotNumber_Type()
)
limSparingConfigProfile_ManuallySparedSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_ManuallySparedSlotNumber.setStatus("mandatory")


class _LimSparingConfigProfile_Action_o_Type(Integer32):
    """Custom type limSparingConfigProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_LimSparingConfigProfile_Action_o_Type.__name__ = "Integer32"
_LimSparingConfigProfile_Action_o_Object = MibScalar
limSparingConfigProfile_Action_o = _LimSparingConfigProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 5),
    _LimSparingConfigProfile_Action_o_Type()
)
limSparingConfigProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_Action_o.setStatus("mandatory")
_LimSparingConfigProfile_Shelf_o_Type = Integer32
_LimSparingConfigProfile_Shelf_o_Object = MibScalar
limSparingConfigProfile_Shelf_o = _LimSparingConfigProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 6),
    _LimSparingConfigProfile_Shelf_o_Type()
)
limSparingConfigProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingConfigProfile_Shelf_o.setStatus("mandatory")
_LimSparingConfigProfile_Slot_o_Type = Integer32
_LimSparingConfigProfile_Slot_o_Object = MibScalar
limSparingConfigProfile_Slot_o = _LimSparingConfigProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 7),
    _LimSparingConfigProfile_Slot_o_Type()
)
limSparingConfigProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingConfigProfile_Slot_o.setStatus("mandatory")
_LimSparingConfigProfile_Item_o_Type = Integer32
_LimSparingConfigProfile_Item_o_Object = MibScalar
limSparingConfigProfile_Item_o = _LimSparingConfigProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 8),
    _LimSparingConfigProfile_Item_o_Type()
)
limSparingConfigProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingConfigProfile_Item_o.setStatus("mandatory")


class _LimSparingConfigProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type limSparingConfigProfile_PhysicalAddress_Shelf based on Integer32"""
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
        *(("anyShelf", 1),
          ("shelf1", 2),
          ("shelf2", 3),
          ("shelf3", 4),
          ("shelf4", 5),
          ("shelf5", 6),
          ("shelf6", 7),
          ("shelf7", 8),
          ("shelf8", 9),
          ("shelf9", 10))
    )


_LimSparingConfigProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_LimSparingConfigProfile_PhysicalAddress_Shelf_Object = MibScalar
limSparingConfigProfile_PhysicalAddress_Shelf = _LimSparingConfigProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 9),
    _LimSparingConfigProfile_PhysicalAddress_Shelf_Type()
)
limSparingConfigProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _LimSparingConfigProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type limSparingConfigProfile_PhysicalAddress_Slot based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              45,
              46,
              49,
              50,
              51,
              53,
              54,
              55,
              56,
              57,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("aLim", 55),
          ("anySlot", 1),
          ("bLim", 56),
          ("cLim", 57),
          ("controlModule", 51),
          ("controller", 42),
          ("dLim", 58),
          ("firstControlModule", 53),
          ("leftController", 49),
          ("rightController", 50),
          ("secondControlModule", 54),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot17", 18),
          ("slot18", 19),
          ("slot19", 20),
          ("slot2", 3),
          ("slot20", 21),
          ("slot21", 22),
          ("slot22", 23),
          ("slot23", 24),
          ("slot24", 25),
          ("slot25", 26),
          ("slot26", 27),
          ("slot27", 28),
          ("slot28", 29),
          ("slot29", 30),
          ("slot3", 4),
          ("slot30", 31),
          ("slot31", 32),
          ("slot32", 33),
          ("slot33", 34),
          ("slot34", 35),
          ("slot35", 36),
          ("slot36", 37),
          ("slot37", 38),
          ("slot38", 39),
          ("slot39", 40),
          ("slot4", 5),
          ("slot40", 41),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8),
          ("slot8", 9),
          ("slot9", 10),
          ("slotPrimary", 59),
          ("trunkModule1", 45),
          ("trunkModule2", 46))
    )


_LimSparingConfigProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_LimSparingConfigProfile_PhysicalAddress_Slot_Object = MibScalar
limSparingConfigProfile_PhysicalAddress_Slot = _LimSparingConfigProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 10),
    _LimSparingConfigProfile_PhysicalAddress_Slot_Type()
)
limSparingConfigProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_PhysicalAddress_Slot.setStatus("mandatory")
_LimSparingConfigProfile_PhysicalAddress_ItemNumber_Type = Integer32
_LimSparingConfigProfile_PhysicalAddress_ItemNumber_Object = MibScalar
limSparingConfigProfile_PhysicalAddress_ItemNumber = _LimSparingConfigProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 11),
    _LimSparingConfigProfile_PhysicalAddress_ItemNumber_Type()
)
limSparingConfigProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _LimSparingConfigProfile_SpareSlotType_Type(Integer32):
    """Custom type limSparingConfigProfile_SpareSlotType based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              43,
              44,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              110,
              111,
              112,
              113,
              116,
              117)
        )
    )
    namedValues = NamedValues(
        *(("alDmtadslAtmCard", 37),
          ("alpmeCard", 111),
          ("alpmtCard", 108),
          ("analogModem2Card", 23),
          ("annexbDadslAtmCard", 59),
          ("annexcDadslAtmCard", 61),
          ("apxenetCard", 117),
          ("aslam32", 98),
          ("capadslCard", 18),
          ("cds3Lim", 74),
          ("clnCard", 107),
          ("clpmeCard", 64),
          ("clpmtCard", 63),
          ("cm", 3),
          ("cmV2", 79),
          ("coc3Lim", 80),
          ("csm3vCard", 38),
          ("csmxCard", 24),
          ("cstm1Lim", 88),
          ("dadslAtm24Card", 49),
          ("dmtadslCard", 19),
          ("ds3Atm2Card", 53),
          ("ds3AtmCard", 26),
          ("ds3AtmHseCard", 95),
          ("ds3AtmTrunkDaughterCard", 40),
          ("dsntscCard", 90),
          ("e3AtmCard", 54),
          ("e3AtmTrunkDaughterCard", 65),
          ("eagleXdslCard", 113),
          ("enetHseCard", 94),
          ("ether3Card", 34),
          ("ether3ndCard", 62),
          ("etherDualCard", 41),
          ("gigeHseCard", 97),
          ("gliteAtm48Card", 52),
          ("hdlc2Card", 28),
          ("hdlc2ecCard", 39),
          ("hdlcCard", 8),
          ("hdsl2Card", 57),
          ("hseCard", 77),
          ("hssiCard", 11),
          ("ima24E1Card", 60),
          ("ima24t1Card", 55),
          ("ima8E1Card", 67),
          ("ima8T1Card", 66),
          ("ima8e1TrunkDaughterCard", 105),
          ("ima8t1TrunkDaughterCard", 104),
          ("ipServicesModule", 110),
          ("madd2Card", 56),
          ("madd3240Card", 89),
          ("madd3Card", 78),
          ("madd3Voip480Card", 101),
          ("maddCard", 30),
          ("modemController", 20),
          ("mrt36AdslCard", 84),
          ("mrtCm", 87),
          ("n-10UnchanE1Card", 22),
          ("n-10UnchanT1Card", 12),
          ("n-16oc3AtmTrunkDaughterCard", 103),
          ("n-24e1Card", 86),
          ("n-24sdslDataCard", 29),
          ("n-24sdslVoiceCard", 31),
          ("n-24t1Card", 85),
          ("n-2ds3Card", 91),
          ("n-2oc34ds3AtmTrunkDaughterCard", 82),
          ("n-2stm14e3AtmTrunkDaughterCard", 92),
          ("n-32idslCard", 21),
          ("n-3ds3Card", 106),
          ("n-48modem56kCard", 15),
          ("n-48modemCard", 7),
          ("n-4ether2Card", 27),
          ("n-4etherCard", 9),
          ("n-4swan2Card", 73),
          ("n-4swanCard", 10),
          ("n-8e1Card", 6),
          ("n-8t1Card", 5),
          ("none", 1),
          ("obsoleteAnalogModemCard", 13),
          ("oc12AtmTrunkDaughterCard", 116),
          ("oc3Atm2Card", 72),
          ("oc3AtmCard", 33),
          ("oc3AtmHseCard", 96),
          ("oc3AtmTrunkDaughterCard", 32),
          ("oc3AtmTrunkDaughterCardVer2", 93),
          ("pctfieCard", 51),
          ("pctfitCard", 50),
          ("r7000Card", 75),
          ("routerCard", 4),
          ("sdslAtmCard", 36),
          ("sdslAtmV2Card", 44),
          ("sdslCard", 17),
          ("shdsl72Card", 81),
          ("shelfForward", 16),
          ("srsEtherCard", 35),
          ("stm0Card", 43),
          ("stngr32IdslCard", 58),
          ("stngr40aAdslCard", 71),
          ("stngr48aAdslCard", 68),
          ("stngr48bAdslCard", 69),
          ("stngr48cAdslCard", 70),
          ("stngr72AdslCard", 83),
          ("stngr72GsAdslCard", 112),
          ("stngr72cAdslCard", 100),
          ("t3Card", 14),
          ("terminatorCard", 48),
          ("trunkModule", 102),
          ("uds3Card", 25),
          ("unknown", 2),
          ("vdslCard", 99),
          ("vpnCard", 76))
    )


_LimSparingConfigProfile_SpareSlotType_Type.__name__ = "Integer32"
_LimSparingConfigProfile_SpareSlotType_Object = MibScalar
limSparingConfigProfile_SpareSlotType = _LimSparingConfigProfile_SpareSlotType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 1, 1, 12),
    _LimSparingConfigProfile_SpareSlotType_Type()
)
limSparingConfigProfile_SpareSlotType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_SpareSlotType.setStatus("mandatory")
_MiblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigTable_Object = MibTable
miblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigTable = _MiblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2)
)
if mibBuilder.loadTexts:
    miblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigTable.setStatus("mandatory")
_MiblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigEntry_Object = MibTableRow
miblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigEntry = _MiblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2, 1)
)
miblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigEntry.setIndexNames(
    (0, "ASCEND-MIBSPARING-MIB", "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-Shelf-o"),
    (0, "ASCEND-MIBSPARING-MIB", "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-Slot-o"),
    (0, "ASCEND-MIBSPARING-MIB", "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-Item-o"),
    (0, "ASCEND-MIBSPARING-MIB", "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-Index-o"),
)
if mibBuilder.loadTexts:
    miblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigEntry.setStatus("mandatory")
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Shelf_o_Type = Integer32
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Shelf_o_Object = MibScalar
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Shelf_o = _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2, 1, 1),
    _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Shelf_o_Type()
)
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Shelf_o.setStatus("mandatory")
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Slot_o_Type = Integer32
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Slot_o_Object = MibScalar
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Slot_o = _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2, 1, 2),
    _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Slot_o_Type()
)
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Slot_o.setStatus("mandatory")
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Item_o_Type = Integer32
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Item_o_Object = MibScalar
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Item_o = _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2, 1, 3),
    _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Item_o_Type()
)
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Item_o.setStatus("mandatory")
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Index_o_Type = Integer32
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Index_o_Object = MibScalar
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Index_o = _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2, 1, 4),
    _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Index_o_Type()
)
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Index_o.setStatus("mandatory")


class _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Active_Type(Integer32):
    """Custom type limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Active based on Integer32"""
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


_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Active_Type.__name__ = "Integer32"
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Active_Object = MibScalar
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Active = _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2, 1, 5),
    _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Active_Type()
)
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Active.setStatus("mandatory")
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorAveragingPeriod_Type = Integer32
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorAveragingPeriod_Object = MibScalar
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorAveragingPeriod = _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorAveragingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2, 1, 6),
    _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorAveragingPeriod_Type()
)
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorAveragingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorAveragingPeriod.setStatus("mandatory")
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorThreshold_Type = Integer32
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorThreshold_Object = MibScalar
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorThreshold = _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2, 1, 7),
    _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorThreshold_Type()
)
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorThreshold.setStatus("mandatory")
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_UpDownThreshold_Type = Integer32
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_UpDownThreshold_Object = MibScalar
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_UpDownThreshold = _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_UpDownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2, 1, 8),
    _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_UpDownThreshold_Type()
)
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_UpDownThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_UpDownThreshold.setStatus("mandatory")
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_PortFailureThreshold_Type = Integer32
_LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_PortFailureThreshold_Object = MibScalar
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_PortFailureThreshold = _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_PortFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 12, 2, 1, 10),
    _LimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_PortFailureThreshold_Type()
)
limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_PortFailureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_PortFailureThreshold.setStatus("mandatory")
_MibifSparingConfigProfile_ObjectIdentity = ObjectIdentity
mibifSparingConfigProfile = _MibifSparingConfigProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 119)
)
_MibifSparingConfigProfileTable_Object = MibTable
mibifSparingConfigProfileTable = _MibifSparingConfigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 119, 1)
)
if mibBuilder.loadTexts:
    mibifSparingConfigProfileTable.setStatus("mandatory")
_MibifSparingConfigProfileEntry_Object = MibTableRow
mibifSparingConfigProfileEntry = _MibifSparingConfigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 119, 1, 1)
)
mibifSparingConfigProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSPARING-MIB", "ifSparingConfigProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibifSparingConfigProfileEntry.setStatus("mandatory")
_IfSparingConfigProfile_Index_o_Type = Integer32
_IfSparingConfigProfile_Index_o_Object = MibScalar
ifSparingConfigProfile_Index_o = _IfSparingConfigProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 119, 1, 1, 1),
    _IfSparingConfigProfile_Index_o_Type()
)
ifSparingConfigProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSparingConfigProfile_Index_o.setStatus("mandatory")


class _IfSparingConfigProfile_Action_o_Type(Integer32):
    """Custom type ifSparingConfigProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_IfSparingConfigProfile_Action_o_Type.__name__ = "Integer32"
_IfSparingConfigProfile_Action_o_Object = MibScalar
ifSparingConfigProfile_Action_o = _IfSparingConfigProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 119, 1, 1, 2),
    _IfSparingConfigProfile_Action_o_Type()
)
ifSparingConfigProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSparingConfigProfile_Action_o.setStatus("mandatory")
_MiblimSparingStatusProfile_ObjectIdentity = ObjectIdentity
miblimSparingStatusProfile = _MiblimSparingStatusProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 120)
)
_MiblimSparingStatusProfileTable_Object = MibTable
miblimSparingStatusProfileTable = _MiblimSparingStatusProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1)
)
if mibBuilder.loadTexts:
    miblimSparingStatusProfileTable.setStatus("mandatory")
_MiblimSparingStatusProfileEntry_Object = MibTableRow
miblimSparingStatusProfileEntry = _MiblimSparingStatusProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1, 1)
)
miblimSparingStatusProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSPARING-MIB", "limSparingStatusProfile-Index-o"),
)
if mibBuilder.loadTexts:
    miblimSparingStatusProfileEntry.setStatus("mandatory")
_LimSparingStatusProfile_Index_o_Type = Integer32
_LimSparingStatusProfile_Index_o_Object = MibScalar
limSparingStatusProfile_Index_o = _LimSparingStatusProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1, 1, 1),
    _LimSparingStatusProfile_Index_o_Type()
)
limSparingStatusProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_Index_o.setStatus("mandatory")


class _LimSparingStatusProfile_SpareSlotType_Type(Integer32):
    """Custom type limSparingStatusProfile_SpareSlotType based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              43,
              44,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              110,
              111,
              112,
              113,
              116,
              117)
        )
    )
    namedValues = NamedValues(
        *(("alDmtadslAtmCard", 37),
          ("alpmeCard", 111),
          ("alpmtCard", 108),
          ("analogModem2Card", 23),
          ("annexbDadslAtmCard", 59),
          ("annexcDadslAtmCard", 61),
          ("apxenetCard", 117),
          ("aslam32", 98),
          ("capadslCard", 18),
          ("cds3Lim", 74),
          ("clnCard", 107),
          ("clpmeCard", 64),
          ("clpmtCard", 63),
          ("cm", 3),
          ("cmV2", 79),
          ("coc3Lim", 80),
          ("csm3vCard", 38),
          ("csmxCard", 24),
          ("cstm1Lim", 88),
          ("dadslAtm24Card", 49),
          ("dmtadslCard", 19),
          ("ds3Atm2Card", 53),
          ("ds3AtmCard", 26),
          ("ds3AtmHseCard", 95),
          ("ds3AtmTrunkDaughterCard", 40),
          ("dsntscCard", 90),
          ("e3AtmCard", 54),
          ("e3AtmTrunkDaughterCard", 65),
          ("eagleXdslCard", 113),
          ("enetHseCard", 94),
          ("ether3Card", 34),
          ("ether3ndCard", 62),
          ("etherDualCard", 41),
          ("gigeHseCard", 97),
          ("gliteAtm48Card", 52),
          ("hdlc2Card", 28),
          ("hdlc2ecCard", 39),
          ("hdlcCard", 8),
          ("hdsl2Card", 57),
          ("hseCard", 77),
          ("hssiCard", 11),
          ("ima24E1Card", 60),
          ("ima24t1Card", 55),
          ("ima8E1Card", 67),
          ("ima8T1Card", 66),
          ("ima8e1TrunkDaughterCard", 105),
          ("ima8t1TrunkDaughterCard", 104),
          ("ipServicesModule", 110),
          ("madd2Card", 56),
          ("madd3240Card", 89),
          ("madd3Card", 78),
          ("madd3Voip480Card", 101),
          ("maddCard", 30),
          ("modemController", 20),
          ("mrt36AdslCard", 84),
          ("mrtCm", 87),
          ("n-10UnchanE1Card", 22),
          ("n-10UnchanT1Card", 12),
          ("n-16oc3AtmTrunkDaughterCard", 103),
          ("n-24e1Card", 86),
          ("n-24sdslDataCard", 29),
          ("n-24sdslVoiceCard", 31),
          ("n-24t1Card", 85),
          ("n-2ds3Card", 91),
          ("n-2oc34ds3AtmTrunkDaughterCard", 82),
          ("n-2stm14e3AtmTrunkDaughterCard", 92),
          ("n-32idslCard", 21),
          ("n-3ds3Card", 106),
          ("n-48modem56kCard", 15),
          ("n-48modemCard", 7),
          ("n-4ether2Card", 27),
          ("n-4etherCard", 9),
          ("n-4swan2Card", 73),
          ("n-4swanCard", 10),
          ("n-8e1Card", 6),
          ("n-8t1Card", 5),
          ("none", 1),
          ("obsoleteAnalogModemCard", 13),
          ("oc12AtmTrunkDaughterCard", 116),
          ("oc3Atm2Card", 72),
          ("oc3AtmCard", 33),
          ("oc3AtmHseCard", 96),
          ("oc3AtmTrunkDaughterCard", 32),
          ("oc3AtmTrunkDaughterCardVer2", 93),
          ("pctfieCard", 51),
          ("pctfitCard", 50),
          ("r7000Card", 75),
          ("routerCard", 4),
          ("sdslAtmCard", 36),
          ("sdslAtmV2Card", 44),
          ("sdslCard", 17),
          ("shdsl72Card", 81),
          ("shelfForward", 16),
          ("srsEtherCard", 35),
          ("stm0Card", 43),
          ("stngr32IdslCard", 58),
          ("stngr40aAdslCard", 71),
          ("stngr48aAdslCard", 68),
          ("stngr48bAdslCard", 69),
          ("stngr48cAdslCard", 70),
          ("stngr72AdslCard", 83),
          ("stngr72GsAdslCard", 112),
          ("stngr72cAdslCard", 100),
          ("t3Card", 14),
          ("terminatorCard", 48),
          ("trunkModule", 102),
          ("uds3Card", 25),
          ("unknown", 2),
          ("vdslCard", 99),
          ("vpnCard", 76))
    )


_LimSparingStatusProfile_SpareSlotType_Type.__name__ = "Integer32"
_LimSparingStatusProfile_SpareSlotType_Object = MibScalar
limSparingStatusProfile_SpareSlotType = _LimSparingStatusProfile_SpareSlotType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1, 1, 2),
    _LimSparingStatusProfile_SpareSlotType_Type()
)
limSparingStatusProfile_SpareSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_SpareSlotType.setStatus("mandatory")


class _LimSparingStatusProfile_SparingMode_Type(Integer32):
    """Custom type limSparingStatusProfile_SparingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 3),
          ("inactive", 1),
          ("manual", 2))
    )


_LimSparingStatusProfile_SparingMode_Type.__name__ = "Integer32"
_LimSparingStatusProfile_SparingMode_Object = MibScalar
limSparingStatusProfile_SparingMode = _LimSparingStatusProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1, 1, 3),
    _LimSparingStatusProfile_SparingMode_Type()
)
limSparingStatusProfile_SparingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_SparingMode.setStatus("mandatory")


class _LimSparingStatusProfile_SpareSlotNumber_Type(Integer32):
    """Custom type limSparingStatusProfile_SpareSlotNumber based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              45,
              46,
              49,
              50,
              51,
              53,
              54,
              55,
              56,
              57,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("aLim", 55),
          ("anySlot", 1),
          ("bLim", 56),
          ("cLim", 57),
          ("controlModule", 51),
          ("controller", 42),
          ("dLim", 58),
          ("firstControlModule", 53),
          ("leftController", 49),
          ("rightController", 50),
          ("secondControlModule", 54),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot17", 18),
          ("slot18", 19),
          ("slot19", 20),
          ("slot2", 3),
          ("slot20", 21),
          ("slot21", 22),
          ("slot22", 23),
          ("slot23", 24),
          ("slot24", 25),
          ("slot25", 26),
          ("slot26", 27),
          ("slot27", 28),
          ("slot28", 29),
          ("slot29", 30),
          ("slot3", 4),
          ("slot30", 31),
          ("slot31", 32),
          ("slot32", 33),
          ("slot33", 34),
          ("slot34", 35),
          ("slot35", 36),
          ("slot36", 37),
          ("slot37", 38),
          ("slot38", 39),
          ("slot39", 40),
          ("slot4", 5),
          ("slot40", 41),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8),
          ("slot8", 9),
          ("slot9", 10),
          ("slotPrimary", 59),
          ("trunkModule1", 45),
          ("trunkModule2", 46))
    )


_LimSparingStatusProfile_SpareSlotNumber_Type.__name__ = "Integer32"
_LimSparingStatusProfile_SpareSlotNumber_Object = MibScalar
limSparingStatusProfile_SpareSlotNumber = _LimSparingStatusProfile_SpareSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1, 1, 4),
    _LimSparingStatusProfile_SpareSlotNumber_Type()
)
limSparingStatusProfile_SpareSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_SpareSlotNumber.setStatus("mandatory")


class _LimSparingStatusProfile_SparedSlotNumber_Type(Integer32):
    """Custom type limSparingStatusProfile_SparedSlotNumber based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              45,
              46,
              49,
              50,
              51,
              53,
              54,
              55,
              56,
              57,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("aLim", 55),
          ("anySlot", 1),
          ("bLim", 56),
          ("cLim", 57),
          ("controlModule", 51),
          ("controller", 42),
          ("dLim", 58),
          ("firstControlModule", 53),
          ("leftController", 49),
          ("rightController", 50),
          ("secondControlModule", 54),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot17", 18),
          ("slot18", 19),
          ("slot19", 20),
          ("slot2", 3),
          ("slot20", 21),
          ("slot21", 22),
          ("slot22", 23),
          ("slot23", 24),
          ("slot24", 25),
          ("slot25", 26),
          ("slot26", 27),
          ("slot27", 28),
          ("slot28", 29),
          ("slot29", 30),
          ("slot3", 4),
          ("slot30", 31),
          ("slot31", 32),
          ("slot32", 33),
          ("slot33", 34),
          ("slot34", 35),
          ("slot35", 36),
          ("slot36", 37),
          ("slot37", 38),
          ("slot38", 39),
          ("slot39", 40),
          ("slot4", 5),
          ("slot40", 41),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8),
          ("slot8", 9),
          ("slot9", 10),
          ("slotPrimary", 59),
          ("trunkModule1", 45),
          ("trunkModule2", 46))
    )


_LimSparingStatusProfile_SparedSlotNumber_Type.__name__ = "Integer32"
_LimSparingStatusProfile_SparedSlotNumber_Object = MibScalar
limSparingStatusProfile_SparedSlotNumber = _LimSparingStatusProfile_SparedSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1, 1, 5),
    _LimSparingStatusProfile_SparedSlotNumber_Type()
)
limSparingStatusProfile_SparedSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_SparedSlotNumber.setStatus("mandatory")


class _LimSparingStatusProfile_SparingChangeReason_Type(Integer32):
    """Custom type limSparingStatusProfile_SparingChangeReason based on Integer32"""
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
        *(("automatic", 3),
          ("manual", 2),
          ("test", 4),
          ("unknown", 1))
    )


_LimSparingStatusProfile_SparingChangeReason_Type.__name__ = "Integer32"
_LimSparingStatusProfile_SparingChangeReason_Object = MibScalar
limSparingStatusProfile_SparingChangeReason = _LimSparingStatusProfile_SparingChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1, 1, 6),
    _LimSparingStatusProfile_SparingChangeReason_Type()
)
limSparingStatusProfile_SparingChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_SparingChangeReason.setStatus("mandatory")
_LimSparingStatusProfile_SparingChangeTime_Type = Integer32
_LimSparingStatusProfile_SparingChangeTime_Object = MibScalar
limSparingStatusProfile_SparingChangeTime = _LimSparingStatusProfile_SparingChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1, 1, 7),
    _LimSparingStatusProfile_SparingChangeTime_Type()
)
limSparingStatusProfile_SparingChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_SparingChangeTime.setStatus("mandatory")
_LimSparingStatusProfile_SparingChangeCounter_Type = Integer32
_LimSparingStatusProfile_SparingChangeCounter_Object = MibScalar
limSparingStatusProfile_SparingChangeCounter = _LimSparingStatusProfile_SparingChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1, 1, 8),
    _LimSparingStatusProfile_SparingChangeCounter_Type()
)
limSparingStatusProfile_SparingChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_SparingChangeCounter.setStatus("mandatory")


class _LimSparingStatusProfile_Action_o_Type(Integer32):
    """Custom type limSparingStatusProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_LimSparingStatusProfile_Action_o_Type.__name__ = "Integer32"
_LimSparingStatusProfile_Action_o_Object = MibScalar
limSparingStatusProfile_Action_o = _LimSparingStatusProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 1, 1, 9),
    _LimSparingStatusProfile_Action_o_Type()
)
limSparingStatusProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limSparingStatusProfile_Action_o.setStatus("mandatory")
_MiblimSparingStatusProfile_LimSparingStatusTable_Object = MibTable
miblimSparingStatusProfile_LimSparingStatusTable = _MiblimSparingStatusProfile_LimSparingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 2)
)
if mibBuilder.loadTexts:
    miblimSparingStatusProfile_LimSparingStatusTable.setStatus("mandatory")
_MiblimSparingStatusProfile_LimSparingStatusEntry_Object = MibTableRow
miblimSparingStatusProfile_LimSparingStatusEntry = _MiblimSparingStatusProfile_LimSparingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 2, 1)
)
miblimSparingStatusProfile_LimSparingStatusEntry.setIndexNames(
    (0, "ASCEND-MIBSPARING-MIB", "limSparingStatusProfile-LimSparingStatus-Index-o"),
    (0, "ASCEND-MIBSPARING-MIB", "limSparingStatusProfile-LimSparingStatus-Index1-o"),
)
if mibBuilder.loadTexts:
    miblimSparingStatusProfile_LimSparingStatusEntry.setStatus("mandatory")
_LimSparingStatusProfile_LimSparingStatus_Index_o_Type = Integer32
_LimSparingStatusProfile_LimSparingStatus_Index_o_Object = MibScalar
limSparingStatusProfile_LimSparingStatus_Index_o = _LimSparingStatusProfile_LimSparingStatus_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 2, 1, 1),
    _LimSparingStatusProfile_LimSparingStatus_Index_o_Type()
)
limSparingStatusProfile_LimSparingStatus_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_LimSparingStatus_Index_o.setStatus("mandatory")
_LimSparingStatusProfile_LimSparingStatus_Index1_o_Type = Integer32
_LimSparingStatusProfile_LimSparingStatus_Index1_o_Object = MibScalar
limSparingStatusProfile_LimSparingStatus_Index1_o = _LimSparingStatusProfile_LimSparingStatus_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 2, 1, 2),
    _LimSparingStatusProfile_LimSparingStatus_Index1_o_Type()
)
limSparingStatusProfile_LimSparingStatus_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_LimSparingStatus_Index1_o.setStatus("mandatory")


class _LimSparingStatusProfile_LimSparingStatus_Active_Type(Integer32):
    """Custom type limSparingStatusProfile_LimSparingStatus_Active based on Integer32"""
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


_LimSparingStatusProfile_LimSparingStatus_Active_Type.__name__ = "Integer32"
_LimSparingStatusProfile_LimSparingStatus_Active_Object = MibScalar
limSparingStatusProfile_LimSparingStatus_Active = _LimSparingStatusProfile_LimSparingStatus_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 2, 1, 3),
    _LimSparingStatusProfile_LimSparingStatus_Active_Type()
)
limSparingStatusProfile_LimSparingStatus_Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_LimSparingStatus_Active.setStatus("mandatory")


class _LimSparingStatusProfile_LimSparingStatus_LimStatusOk_Type(Integer32):
    """Custom type limSparingStatusProfile_LimSparingStatus_LimStatusOk based on Integer32"""
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


_LimSparingStatusProfile_LimSparingStatus_LimStatusOk_Type.__name__ = "Integer32"
_LimSparingStatusProfile_LimSparingStatus_LimStatusOk_Object = MibScalar
limSparingStatusProfile_LimSparingStatus_LimStatusOk = _LimSparingStatusProfile_LimSparingStatus_LimStatusOk_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 2, 1, 4),
    _LimSparingStatusProfile_LimSparingStatus_LimStatusOk_Type()
)
limSparingStatusProfile_LimSparingStatus_LimStatusOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_LimSparingStatus_LimStatusOk.setStatus("mandatory")


class _LimSparingStatusProfile_LimSparingStatus_SparingState_Type(Integer32):
    """Custom type limSparingStatusProfile_LimSparingStatus_SparingState based on Integer32"""
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
        *(("notApplicable", 6),
          ("primaryActive", 2),
          ("primaryInactive", 3),
          ("secondaryActive", 4),
          ("secondaryInactive", 5),
          ("sparingNone", 1))
    )


_LimSparingStatusProfile_LimSparingStatus_SparingState_Type.__name__ = "Integer32"
_LimSparingStatusProfile_LimSparingStatus_SparingState_Object = MibScalar
limSparingStatusProfile_LimSparingStatus_SparingState = _LimSparingStatusProfile_LimSparingStatus_SparingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 120, 2, 1, 5),
    _LimSparingStatusProfile_LimSparingStatus_SparingState_Type()
)
limSparingStatusProfile_LimSparingStatus_SparingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limSparingStatusProfile_LimSparingStatus_SparingState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSPARING-MIB",
    **{"DisplayString": DisplayString,
       "miblimSparingConfigProfile": miblimSparingConfigProfile,
       "miblimSparingConfigProfileTable": miblimSparingConfigProfileTable,
       "miblimSparingConfigProfileEntry": miblimSparingConfigProfileEntry,
       "limSparingConfigProfile-SparingMode": limSparingConfigProfile_SparingMode,
       "limSparingConfigProfile-SpareSlotNumber": limSparingConfigProfile_SpareSlotNumber,
       "limSparingConfigProfile-ManuallySparedSlotNumber": limSparingConfigProfile_ManuallySparedSlotNumber,
       "limSparingConfigProfile-Action-o": limSparingConfigProfile_Action_o,
       "limSparingConfigProfile-Shelf-o": limSparingConfigProfile_Shelf_o,
       "limSparingConfigProfile-Slot-o": limSparingConfigProfile_Slot_o,
       "limSparingConfigProfile-Item-o": limSparingConfigProfile_Item_o,
       "limSparingConfigProfile-PhysicalAddress-Shelf": limSparingConfigProfile_PhysicalAddress_Shelf,
       "limSparingConfigProfile-PhysicalAddress-Slot": limSparingConfigProfile_PhysicalAddress_Slot,
       "limSparingConfigProfile-PhysicalAddress-ItemNumber": limSparingConfigProfile_PhysicalAddress_ItemNumber,
       "limSparingConfigProfile-SpareSlotType": limSparingConfigProfile_SpareSlotType,
       "miblimSparingConfigProfile-AutoLimSparingConfig-LimSparingConfigTable": miblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigTable,
       "miblimSparingConfigProfile-AutoLimSparingConfig-LimSparingConfigEntry": miblimSparingConfigProfile_AutoLimSparingConfig_LimSparingConfigEntry,
       "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-Shelf-o": limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Shelf_o,
       "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-Slot-o": limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Slot_o,
       "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-Item-o": limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Item_o,
       "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-Index-o": limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Index_o,
       "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-Active": limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_Active,
       "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-ErrorAveragingPeriod": limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorAveragingPeriod,
       "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-ErrorThreshold": limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_ErrorThreshold,
       "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-UpDownThreshold": limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_UpDownThreshold,
       "limSparingConfigProfile-AutoLimSparingConfig-LimSparingConfig-PortFailureThreshold": limSparingConfigProfile_AutoLimSparingConfig_LimSparingConfig_PortFailureThreshold,
       "mibifSparingConfigProfile": mibifSparingConfigProfile,
       "mibifSparingConfigProfileTable": mibifSparingConfigProfileTable,
       "mibifSparingConfigProfileEntry": mibifSparingConfigProfileEntry,
       "ifSparingConfigProfile-Index-o": ifSparingConfigProfile_Index_o,
       "ifSparingConfigProfile-Action-o": ifSparingConfigProfile_Action_o,
       "miblimSparingStatusProfile": miblimSparingStatusProfile,
       "miblimSparingStatusProfileTable": miblimSparingStatusProfileTable,
       "miblimSparingStatusProfileEntry": miblimSparingStatusProfileEntry,
       "limSparingStatusProfile-Index-o": limSparingStatusProfile_Index_o,
       "limSparingStatusProfile-SpareSlotType": limSparingStatusProfile_SpareSlotType,
       "limSparingStatusProfile-SparingMode": limSparingStatusProfile_SparingMode,
       "limSparingStatusProfile-SpareSlotNumber": limSparingStatusProfile_SpareSlotNumber,
       "limSparingStatusProfile-SparedSlotNumber": limSparingStatusProfile_SparedSlotNumber,
       "limSparingStatusProfile-SparingChangeReason": limSparingStatusProfile_SparingChangeReason,
       "limSparingStatusProfile-SparingChangeTime": limSparingStatusProfile_SparingChangeTime,
       "limSparingStatusProfile-SparingChangeCounter": limSparingStatusProfile_SparingChangeCounter,
       "limSparingStatusProfile-Action-o": limSparingStatusProfile_Action_o,
       "miblimSparingStatusProfile-LimSparingStatusTable": miblimSparingStatusProfile_LimSparingStatusTable,
       "miblimSparingStatusProfile-LimSparingStatusEntry": miblimSparingStatusProfile_LimSparingStatusEntry,
       "limSparingStatusProfile-LimSparingStatus-Index-o": limSparingStatusProfile_LimSparingStatus_Index_o,
       "limSparingStatusProfile-LimSparingStatus-Index1-o": limSparingStatusProfile_LimSparingStatus_Index1_o,
       "limSparingStatusProfile-LimSparingStatus-Active": limSparingStatusProfile_LimSparingStatus_Active,
       "limSparingStatusProfile-LimSparingStatus-LimStatusOk": limSparingStatusProfile_LimSparingStatus_LimStatusOk,
       "limSparingStatusProfile-LimSparingStatus-SparingState": limSparingStatusProfile_LimSparingStatus_SparingState}
)
