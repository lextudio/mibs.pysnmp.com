# SNMP MIB module (ASCEND-MIBBRILT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBBRILT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:16 2024
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

_MibbRILtProfile_ObjectIdentity = ObjectIdentity
mibbRILtProfile = _MibbRILtProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 27)
)
_MibbRILtProfileTable_Object = MibTable
mibbRILtProfileTable = _MibbRILtProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1)
)
if mibBuilder.loadTexts:
    mibbRILtProfileTable.setStatus("mandatory")
_MibbRILtProfileEntry_Object = MibTableRow
mibbRILtProfileEntry = _MibbRILtProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1)
)
mibbRILtProfileEntry.setIndexNames(
    (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-Shelf-o"),
    (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-Slot-o"),
    (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibbRILtProfileEntry.setStatus("mandatory")
_BRILtProfile_Shelf_o_Type = Integer32
_BRILtProfile_Shelf_o_Object = MibScalar
bRILtProfile_Shelf_o = _BRILtProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 1),
    _BRILtProfile_Shelf_o_Type()
)
bRILtProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRILtProfile_Shelf_o.setStatus("mandatory")
_BRILtProfile_Slot_o_Type = Integer32
_BRILtProfile_Slot_o_Object = MibScalar
bRILtProfile_Slot_o = _BRILtProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 2),
    _BRILtProfile_Slot_o_Type()
)
bRILtProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRILtProfile_Slot_o.setStatus("mandatory")
_BRILtProfile_Item_o_Type = Integer32
_BRILtProfile_Item_o_Object = MibScalar
bRILtProfile_Item_o = _BRILtProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 3),
    _BRILtProfile_Item_o_Type()
)
bRILtProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRILtProfile_Item_o.setStatus("mandatory")
_BRILtProfile_ProfileNumber_Type = Integer32
_BRILtProfile_ProfileNumber_Object = MibScalar
bRILtProfile_ProfileNumber = _BRILtProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 4),
    _BRILtProfile_ProfileNumber_Type()
)
bRILtProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_ProfileNumber.setStatus("mandatory")
_BRILtProfile_Name_Type = DisplayString
_BRILtProfile_Name_Object = MibScalar
bRILtProfile_Name = _BRILtProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 5),
    _BRILtProfile_Name_Type()
)
bRILtProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_Name.setStatus("mandatory")


class _BRILtProfile_LineInterface_Enabled_Type(Integer32):
    """Custom type bRILtProfile_LineInterface_Enabled based on Integer32"""
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


_BRILtProfile_LineInterface_Enabled_Type.__name__ = "Integer32"
_BRILtProfile_LineInterface_Enabled_Object = MibScalar
bRILtProfile_LineInterface_Enabled = _BRILtProfile_LineInterface_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 6),
    _BRILtProfile_LineInterface_Enabled_Type()
)
bRILtProfile_LineInterface_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_Enabled.setStatus("mandatory")
_BRILtProfile_LineInterface_AnswerNumber1_Type = DisplayString
_BRILtProfile_LineInterface_AnswerNumber1_Object = MibScalar
bRILtProfile_LineInterface_AnswerNumber1 = _BRILtProfile_LineInterface_AnswerNumber1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 7),
    _BRILtProfile_LineInterface_AnswerNumber1_Type()
)
bRILtProfile_LineInterface_AnswerNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_AnswerNumber1.setStatus("mandatory")
_BRILtProfile_LineInterface_AnswerNumber2_Type = DisplayString
_BRILtProfile_LineInterface_AnswerNumber2_Object = MibScalar
bRILtProfile_LineInterface_AnswerNumber2 = _BRILtProfile_LineInterface_AnswerNumber2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 8),
    _BRILtProfile_LineInterface_AnswerNumber2_Type()
)
bRILtProfile_LineInterface_AnswerNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_AnswerNumber2.setStatus("mandatory")


class _BRILtProfile_LineInterface_ClockSource_Type(Integer32):
    """Custom type bRILtProfile_LineInterface_ClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eligible", 1),
          ("notEligible", 2))
    )


_BRILtProfile_LineInterface_ClockSource_Type.__name__ = "Integer32"
_BRILtProfile_LineInterface_ClockSource_Object = MibScalar
bRILtProfile_LineInterface_ClockSource = _BRILtProfile_LineInterface_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 9),
    _BRILtProfile_LineInterface_ClockSource_Type()
)
bRILtProfile_LineInterface_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_ClockSource.setStatus("mandatory")


class _BRILtProfile_LineInterface_IdslBandwidth_Type(Integer32):
    """Custom type bRILtProfile_LineInterface_IdslBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idsl128", 1),
          ("idsl144", 2))
    )


_BRILtProfile_LineInterface_IdslBandwidth_Type.__name__ = "Integer32"
_BRILtProfile_LineInterface_IdslBandwidth_Object = MibScalar
bRILtProfile_LineInterface_IdslBandwidth = _BRILtProfile_LineInterface_IdslBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 10),
    _BRILtProfile_LineInterface_IdslBandwidth_Type()
)
bRILtProfile_LineInterface_IdslBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_IdslBandwidth.setStatus("mandatory")
_BRILtProfile_LineInterface_Gr303Crv_Type = Integer32
_BRILtProfile_LineInterface_Gr303Crv_Object = MibScalar
bRILtProfile_LineInterface_Gr303Crv = _BRILtProfile_LineInterface_Gr303Crv_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 11),
    _BRILtProfile_LineInterface_Gr303Crv_Type()
)
bRILtProfile_LineInterface_Gr303Crv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_Gr303Crv.setStatus("mandatory")
_BRILtProfile_LineInterface_Gr303InterfaceGroup_Type = Integer32
_BRILtProfile_LineInterface_Gr303InterfaceGroup_Object = MibScalar
bRILtProfile_LineInterface_Gr303InterfaceGroup = _BRILtProfile_LineInterface_Gr303InterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 12),
    _BRILtProfile_LineInterface_Gr303InterfaceGroup_Type()
)
bRILtProfile_LineInterface_Gr303InterfaceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_Gr303InterfaceGroup.setStatus("mandatory")


class _BRILtProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type bRILtProfile_PhysicalAddress_Shelf based on Integer32"""
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


_BRILtProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_BRILtProfile_PhysicalAddress_Shelf_Object = MibScalar
bRILtProfile_PhysicalAddress_Shelf = _BRILtProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 13),
    _BRILtProfile_PhysicalAddress_Shelf_Type()
)
bRILtProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _BRILtProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type bRILtProfile_PhysicalAddress_Slot based on Integer32"""
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


_BRILtProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_BRILtProfile_PhysicalAddress_Slot_Object = MibScalar
bRILtProfile_PhysicalAddress_Slot = _BRILtProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 14),
    _BRILtProfile_PhysicalAddress_Slot_Type()
)
bRILtProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_PhysicalAddress_Slot.setStatus("mandatory")
_BRILtProfile_PhysicalAddress_ItemNumber_Type = Integer32
_BRILtProfile_PhysicalAddress_ItemNumber_Object = MibScalar
bRILtProfile_PhysicalAddress_ItemNumber = _BRILtProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 15),
    _BRILtProfile_PhysicalAddress_ItemNumber_Type()
)
bRILtProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _BRILtProfile_SwitchType_Type(Integer32):
    """Custom type bRILtProfile_SwitchType based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("att5essBri", 16),
          ("attPri", 1),
          ("australBri", 25),
          ("australPri", 9),
          ("belgianBri", 24),
          ("btSs7", 32),
          ("btnr191Bri", 20),
          ("danishPri", 8),
          ("dass2", 14),
          ("dms100Nt1Bri", 17),
          ("dutch1tr6Bri", 28),
          ("german1tr6Bri", 27),
          ("globandPri", 3),
          ("idslPtpBri", 30),
          ("isdxDpnss", 11),
          ("islxDpnss", 12),
          ("japanPri", 4),
          ("kddBri", 23),
          ("mercuryDpnss", 13),
          ("natIsdn2Pri", 10),
          ("net3Bri", 21),
          ("net5Pri", 7),
          ("nisdn1Bri", 18),
          ("ntiPri", 2),
          ("onetr6Pri", 6),
          ("ptpNet3Bri", 22),
          ("swissBri", 26),
          ("switchCas", 29),
          ("taiwanPri", 31),
          ("unknownBri", 15),
          ("vn2Bri", 19),
          ("vn3Pri", 5))
    )


_BRILtProfile_SwitchType_Type.__name__ = "Integer32"
_BRILtProfile_SwitchType_Object = MibScalar
bRILtProfile_SwitchType = _BRILtProfile_SwitchType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 16),
    _BRILtProfile_SwitchType_Type()
)
bRILtProfile_SwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_SwitchType.setStatus("mandatory")


class _BRILtProfile_Action_o_Type(Integer32):
    """Custom type bRILtProfile_Action_o based on Integer32"""
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


_BRILtProfile_Action_o_Type.__name__ = "Integer32"
_BRILtProfile_Action_o_Object = MibScalar
bRILtProfile_Action_o = _BRILtProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 17),
    _BRILtProfile_Action_o_Type()
)
bRILtProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_Action_o.setStatus("mandatory")


class _BRILtProfile_LineInterface_IgnoreLineup_Type(Integer32):
    """Custom type bRILtProfile_LineInterface_IgnoreLineup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("systemDefined", 1),
          ("yes", 3))
    )


_BRILtProfile_LineInterface_IgnoreLineup_Type.__name__ = "Integer32"
_BRILtProfile_LineInterface_IgnoreLineup_Object = MibScalar
bRILtProfile_LineInterface_IgnoreLineup = _BRILtProfile_LineInterface_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 18),
    _BRILtProfile_LineInterface_IgnoreLineup_Type()
)
bRILtProfile_LineInterface_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_IgnoreLineup.setStatus("mandatory")


class _BRILtProfile_SparingMode_Type(Integer32):
    """Custom type bRILtProfile_SparingMode based on Integer32"""
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


_BRILtProfile_SparingMode_Type.__name__ = "Integer32"
_BRILtProfile_SparingMode_Object = MibScalar
bRILtProfile_SparingMode = _BRILtProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 19),
    _BRILtProfile_SparingMode_Type()
)
bRILtProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_SparingMode.setStatus("mandatory")
_MibbRILtProfile_LineInterface_ChannelConfigTable_Object = MibTable
mibbRILtProfile_LineInterface_ChannelConfigTable = _MibbRILtProfile_LineInterface_ChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 2)
)
if mibBuilder.loadTexts:
    mibbRILtProfile_LineInterface_ChannelConfigTable.setStatus("mandatory")
_MibbRILtProfile_LineInterface_ChannelConfigEntry_Object = MibTableRow
mibbRILtProfile_LineInterface_ChannelConfigEntry = _MibbRILtProfile_LineInterface_ChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1)
)
mibbRILtProfile_LineInterface_ChannelConfigEntry.setIndexNames(
    (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-LineInterface-ChannelConfig-Shelf-o"),
    (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-LineInterface-ChannelConfig-Slot-o"),
    (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-LineInterface-ChannelConfig-Item-o"),
    (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-LineInterface-ChannelConfig-Index-o"),
)
if mibBuilder.loadTexts:
    mibbRILtProfile_LineInterface_ChannelConfigEntry.setStatus("mandatory")
_BRILtProfile_LineInterface_ChannelConfig_Shelf_o_Type = Integer32
_BRILtProfile_LineInterface_ChannelConfig_Shelf_o_Object = MibScalar
bRILtProfile_LineInterface_ChannelConfig_Shelf_o = _BRILtProfile_LineInterface_ChannelConfig_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 1),
    _BRILtProfile_LineInterface_ChannelConfig_Shelf_o_Type()
)
bRILtProfile_LineInterface_ChannelConfig_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_ChannelConfig_Shelf_o.setStatus("mandatory")
_BRILtProfile_LineInterface_ChannelConfig_Slot_o_Type = Integer32
_BRILtProfile_LineInterface_ChannelConfig_Slot_o_Object = MibScalar
bRILtProfile_LineInterface_ChannelConfig_Slot_o = _BRILtProfile_LineInterface_ChannelConfig_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 2),
    _BRILtProfile_LineInterface_ChannelConfig_Slot_o_Type()
)
bRILtProfile_LineInterface_ChannelConfig_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_ChannelConfig_Slot_o.setStatus("mandatory")
_BRILtProfile_LineInterface_ChannelConfig_Item_o_Type = Integer32
_BRILtProfile_LineInterface_ChannelConfig_Item_o_Object = MibScalar
bRILtProfile_LineInterface_ChannelConfig_Item_o = _BRILtProfile_LineInterface_ChannelConfig_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 3),
    _BRILtProfile_LineInterface_ChannelConfig_Item_o_Type()
)
bRILtProfile_LineInterface_ChannelConfig_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_ChannelConfig_Item_o.setStatus("mandatory")
_BRILtProfile_LineInterface_ChannelConfig_Index_o_Type = Integer32
_BRILtProfile_LineInterface_ChannelConfig_Index_o_Object = MibScalar
bRILtProfile_LineInterface_ChannelConfig_Index_o = _BRILtProfile_LineInterface_ChannelConfig_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 4),
    _BRILtProfile_LineInterface_ChannelConfig_Index_o_Type()
)
bRILtProfile_LineInterface_ChannelConfig_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_ChannelConfig_Index_o.setStatus("mandatory")


class _BRILtProfile_LineInterface_ChannelConfig_ChannelUsage_Type(Integer32):
    """Custom type bRILtProfile_LineInterface_ChannelConfig_ChannelUsage based on Integer32"""
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
        *(("dChannel", 4),
          ("nailed64Channel", 3),
          ("nfasPrimaryDChannel", 5),
          ("nfasSecondaryDChannel", 6),
          ("semiPermChannel", 7),
          ("ss7SignalingChannel", 8),
          ("switchedChannel", 2),
          ("unusedChannel", 1))
    )


_BRILtProfile_LineInterface_ChannelConfig_ChannelUsage_Type.__name__ = "Integer32"
_BRILtProfile_LineInterface_ChannelConfig_ChannelUsage_Object = MibScalar
bRILtProfile_LineInterface_ChannelConfig_ChannelUsage = _BRILtProfile_LineInterface_ChannelConfig_ChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 5),
    _BRILtProfile_LineInterface_ChannelConfig_ChannelUsage_Type()
)
bRILtProfile_LineInterface_ChannelConfig_ChannelUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_ChannelConfig_ChannelUsage.setStatus("mandatory")
_BRILtProfile_LineInterface_ChannelConfig_NailedGroup_Type = Integer32
_BRILtProfile_LineInterface_ChannelConfig_NailedGroup_Object = MibScalar
bRILtProfile_LineInterface_ChannelConfig_NailedGroup = _BRILtProfile_LineInterface_ChannelConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 6),
    _BRILtProfile_LineInterface_ChannelConfig_NailedGroup_Type()
)
bRILtProfile_LineInterface_ChannelConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRILtProfile_LineInterface_ChannelConfig_NailedGroup.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBBRILT-MIB",
    **{"DisplayString": DisplayString,
       "mibbRILtProfile": mibbRILtProfile,
       "mibbRILtProfileTable": mibbRILtProfileTable,
       "mibbRILtProfileEntry": mibbRILtProfileEntry,
       "bRILtProfile-Shelf-o": bRILtProfile_Shelf_o,
       "bRILtProfile-Slot-o": bRILtProfile_Slot_o,
       "bRILtProfile-Item-o": bRILtProfile_Item_o,
       "bRILtProfile-ProfileNumber": bRILtProfile_ProfileNumber,
       "bRILtProfile-Name": bRILtProfile_Name,
       "bRILtProfile-LineInterface-Enabled": bRILtProfile_LineInterface_Enabled,
       "bRILtProfile-LineInterface-AnswerNumber1": bRILtProfile_LineInterface_AnswerNumber1,
       "bRILtProfile-LineInterface-AnswerNumber2": bRILtProfile_LineInterface_AnswerNumber2,
       "bRILtProfile-LineInterface-ClockSource": bRILtProfile_LineInterface_ClockSource,
       "bRILtProfile-LineInterface-IdslBandwidth": bRILtProfile_LineInterface_IdslBandwidth,
       "bRILtProfile-LineInterface-Gr303Crv": bRILtProfile_LineInterface_Gr303Crv,
       "bRILtProfile-LineInterface-Gr303InterfaceGroup": bRILtProfile_LineInterface_Gr303InterfaceGroup,
       "bRILtProfile-PhysicalAddress-Shelf": bRILtProfile_PhysicalAddress_Shelf,
       "bRILtProfile-PhysicalAddress-Slot": bRILtProfile_PhysicalAddress_Slot,
       "bRILtProfile-PhysicalAddress-ItemNumber": bRILtProfile_PhysicalAddress_ItemNumber,
       "bRILtProfile-SwitchType": bRILtProfile_SwitchType,
       "bRILtProfile-Action-o": bRILtProfile_Action_o,
       "bRILtProfile-LineInterface-IgnoreLineup": bRILtProfile_LineInterface_IgnoreLineup,
       "bRILtProfile-SparingMode": bRILtProfile_SparingMode,
       "mibbRILtProfile-LineInterface-ChannelConfigTable": mibbRILtProfile_LineInterface_ChannelConfigTable,
       "mibbRILtProfile-LineInterface-ChannelConfigEntry": mibbRILtProfile_LineInterface_ChannelConfigEntry,
       "bRILtProfile-LineInterface-ChannelConfig-Shelf-o": bRILtProfile_LineInterface_ChannelConfig_Shelf_o,
       "bRILtProfile-LineInterface-ChannelConfig-Slot-o": bRILtProfile_LineInterface_ChannelConfig_Slot_o,
       "bRILtProfile-LineInterface-ChannelConfig-Item-o": bRILtProfile_LineInterface_ChannelConfig_Item_o,
       "bRILtProfile-LineInterface-ChannelConfig-Index-o": bRILtProfile_LineInterface_ChannelConfig_Index_o,
       "bRILtProfile-LineInterface-ChannelConfig-ChannelUsage": bRILtProfile_LineInterface_ChannelConfig_ChannelUsage,
       "bRILtProfile-LineInterface-ChannelConfig-NailedGroup": bRILtProfile_LineInterface_ChannelConfig_NailedGroup}
)
