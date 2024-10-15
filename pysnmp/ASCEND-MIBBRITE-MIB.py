# SNMP MIB module (ASCEND-MIBBRITE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBBRITE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:18 2024
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

_MibbRINetworkProfile_ObjectIdentity = ObjectIdentity
mibbRINetworkProfile = _MibbRINetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 63)
)
_MibbRINetworkProfileTable_Object = MibTable
mibbRINetworkProfileTable = _MibbRINetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1)
)
if mibBuilder.loadTexts:
    mibbRINetworkProfileTable.setStatus("mandatory")
_MibbRINetworkProfileEntry_Object = MibTableRow
mibbRINetworkProfileEntry = _MibbRINetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1)
)
mibbRINetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-Slot-o"),
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibbRINetworkProfileEntry.setStatus("mandatory")
_BRINetworkProfile_Shelf_o_Type = Integer32
_BRINetworkProfile_Shelf_o_Object = MibScalar
bRINetworkProfile_Shelf_o = _BRINetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 1),
    _BRINetworkProfile_Shelf_o_Type()
)
bRINetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_Shelf_o.setStatus("mandatory")
_BRINetworkProfile_Slot_o_Type = Integer32
_BRINetworkProfile_Slot_o_Object = MibScalar
bRINetworkProfile_Slot_o = _BRINetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 2),
    _BRINetworkProfile_Slot_o_Type()
)
bRINetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_Slot_o.setStatus("mandatory")
_BRINetworkProfile_Item_o_Type = Integer32
_BRINetworkProfile_Item_o_Object = MibScalar
bRINetworkProfile_Item_o = _BRINetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 3),
    _BRINetworkProfile_Item_o_Type()
)
bRINetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_Item_o.setStatus("mandatory")
_BRINetworkProfile_ProfileNumber_Type = Integer32
_BRINetworkProfile_ProfileNumber_Object = MibScalar
bRINetworkProfile_ProfileNumber = _BRINetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 4),
    _BRINetworkProfile_ProfileNumber_Type()
)
bRINetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_ProfileNumber.setStatus("mandatory")
_BRINetworkProfile_Name_Type = DisplayString
_BRINetworkProfile_Name_Object = MibScalar
bRINetworkProfile_Name = _BRINetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 5),
    _BRINetworkProfile_Name_Type()
)
bRINetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_Name.setStatus("mandatory")


class _BRINetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type bRINetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_BRINetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_BRINetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
bRINetworkProfile_PhysicalAddress_Shelf = _BRINetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 6),
    _BRINetworkProfile_PhysicalAddress_Shelf_Type()
)
bRINetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _BRINetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type bRINetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_BRINetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_BRINetworkProfile_PhysicalAddress_Slot_Object = MibScalar
bRINetworkProfile_PhysicalAddress_Slot = _BRINetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 7),
    _BRINetworkProfile_PhysicalAddress_Slot_Type()
)
bRINetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_BRINetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_BRINetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
bRINetworkProfile_PhysicalAddress_ItemNumber = _BRINetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 8),
    _BRINetworkProfile_PhysicalAddress_ItemNumber_Type()
)
bRINetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _BRINetworkProfile_SwitchType_Type(Integer32):
    """Custom type bRINetworkProfile_SwitchType based on Integer32"""
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


_BRINetworkProfile_SwitchType_Type.__name__ = "Integer32"
_BRINetworkProfile_SwitchType_Object = MibScalar
bRINetworkProfile_SwitchType = _BRINetworkProfile_SwitchType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 9),
    _BRINetworkProfile_SwitchType_Type()
)
bRINetworkProfile_SwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_SwitchType.setStatus("mandatory")


class _BRINetworkProfile_AnsVoiceCall_Type(Integer32):
    """Custom type bRINetworkProfile_AnsVoiceCall based on Integer32"""
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


_BRINetworkProfile_AnsVoiceCall_Type.__name__ = "Integer32"
_BRINetworkProfile_AnsVoiceCall_Object = MibScalar
bRINetworkProfile_AnsVoiceCall = _BRINetworkProfile_AnsVoiceCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 10),
    _BRINetworkProfile_AnsVoiceCall_Type()
)
bRINetworkProfile_AnsVoiceCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_AnsVoiceCall.setStatus("mandatory")


class _BRINetworkProfile_ConcatNailedLines_Type(Integer32):
    """Custom type bRINetworkProfile_ConcatNailedLines based on Integer32"""
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


_BRINetworkProfile_ConcatNailedLines_Type.__name__ = "Integer32"
_BRINetworkProfile_ConcatNailedLines_Object = MibScalar
bRINetworkProfile_ConcatNailedLines = _BRINetworkProfile_ConcatNailedLines_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 11),
    _BRINetworkProfile_ConcatNailedLines_Type()
)
bRINetworkProfile_ConcatNailedLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_ConcatNailedLines.setStatus("mandatory")


class _BRINetworkProfile_BriAnalogEncode_Type(Integer32):
    """Custom type bRINetworkProfile_BriAnalogEncode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 3),
          ("muLaw", 2),
          ("switchType", 1))
    )


_BRINetworkProfile_BriAnalogEncode_Type.__name__ = "Integer32"
_BRINetworkProfile_BriAnalogEncode_Object = MibScalar
bRINetworkProfile_BriAnalogEncode = _BRINetworkProfile_BriAnalogEncode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 12),
    _BRINetworkProfile_BriAnalogEncode_Type()
)
bRINetworkProfile_BriAnalogEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_BriAnalogEncode.setStatus("mandatory")


class _BRINetworkProfile_Action_o_Type(Integer32):
    """Custom type bRINetworkProfile_Action_o based on Integer32"""
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


_BRINetworkProfile_Action_o_Type.__name__ = "Integer32"
_BRINetworkProfile_Action_o_Object = MibScalar
bRINetworkProfile_Action_o = _BRINetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 1, 1, 13),
    _BRINetworkProfile_Action_o_Type()
)
bRINetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_Action_o.setStatus("mandatory")
_MibbRINetworkProfile_LineInterfaceTable_Object = MibTable
mibbRINetworkProfile_LineInterfaceTable = _MibbRINetworkProfile_LineInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2)
)
if mibBuilder.loadTexts:
    mibbRINetworkProfile_LineInterfaceTable.setStatus("mandatory")
_MibbRINetworkProfile_LineInterfaceEntry_Object = MibTableRow
mibbRINetworkProfile_LineInterfaceEntry = _MibbRINetworkProfile_LineInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1)
)
mibbRINetworkProfile_LineInterfaceEntry.setIndexNames(
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-LineInterface-Shelf-o"),
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-LineInterface-Slot-o"),
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-LineInterface-Item-o"),
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-LineInterface-Index-o"),
)
if mibBuilder.loadTexts:
    mibbRINetworkProfile_LineInterfaceEntry.setStatus("mandatory")
_BRINetworkProfile_LineInterface_Shelf_o_Type = Integer32
_BRINetworkProfile_LineInterface_Shelf_o_Object = MibScalar
bRINetworkProfile_LineInterface_Shelf_o = _BRINetworkProfile_LineInterface_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 1),
    _BRINetworkProfile_LineInterface_Shelf_o_Type()
)
bRINetworkProfile_LineInterface_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_Shelf_o.setStatus("mandatory")
_BRINetworkProfile_LineInterface_Slot_o_Type = Integer32
_BRINetworkProfile_LineInterface_Slot_o_Object = MibScalar
bRINetworkProfile_LineInterface_Slot_o = _BRINetworkProfile_LineInterface_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 2),
    _BRINetworkProfile_LineInterface_Slot_o_Type()
)
bRINetworkProfile_LineInterface_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_Slot_o.setStatus("mandatory")
_BRINetworkProfile_LineInterface_Item_o_Type = Integer32
_BRINetworkProfile_LineInterface_Item_o_Object = MibScalar
bRINetworkProfile_LineInterface_Item_o = _BRINetworkProfile_LineInterface_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 3),
    _BRINetworkProfile_LineInterface_Item_o_Type()
)
bRINetworkProfile_LineInterface_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_Item_o.setStatus("mandatory")
_BRINetworkProfile_LineInterface_Index_o_Type = Integer32
_BRINetworkProfile_LineInterface_Index_o_Object = MibScalar
bRINetworkProfile_LineInterface_Index_o = _BRINetworkProfile_LineInterface_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 4),
    _BRINetworkProfile_LineInterface_Index_o_Type()
)
bRINetworkProfile_LineInterface_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_Index_o.setStatus("mandatory")


class _BRINetworkProfile_LineInterface_Enabled_Type(Integer32):
    """Custom type bRINetworkProfile_LineInterface_Enabled based on Integer32"""
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


_BRINetworkProfile_LineInterface_Enabled_Type.__name__ = "Integer32"
_BRINetworkProfile_LineInterface_Enabled_Object = MibScalar
bRINetworkProfile_LineInterface_Enabled = _BRINetworkProfile_LineInterface_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 5),
    _BRINetworkProfile_LineInterface_Enabled_Type()
)
bRINetworkProfile_LineInterface_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_Enabled.setStatus("mandatory")
_BRINetworkProfile_LineInterface_AnswerNumber1_Type = DisplayString
_BRINetworkProfile_LineInterface_AnswerNumber1_Object = MibScalar
bRINetworkProfile_LineInterface_AnswerNumber1 = _BRINetworkProfile_LineInterface_AnswerNumber1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 6),
    _BRINetworkProfile_LineInterface_AnswerNumber1_Type()
)
bRINetworkProfile_LineInterface_AnswerNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_AnswerNumber1.setStatus("mandatory")
_BRINetworkProfile_LineInterface_AnswerNumber2_Type = DisplayString
_BRINetworkProfile_LineInterface_AnswerNumber2_Object = MibScalar
bRINetworkProfile_LineInterface_AnswerNumber2 = _BRINetworkProfile_LineInterface_AnswerNumber2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 7),
    _BRINetworkProfile_LineInterface_AnswerNumber2_Type()
)
bRINetworkProfile_LineInterface_AnswerNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_AnswerNumber2.setStatus("mandatory")


class _BRINetworkProfile_LineInterface_ClockSource_Type(Integer32):
    """Custom type bRINetworkProfile_LineInterface_ClockSource based on Integer32"""
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


_BRINetworkProfile_LineInterface_ClockSource_Type.__name__ = "Integer32"
_BRINetworkProfile_LineInterface_ClockSource_Object = MibScalar
bRINetworkProfile_LineInterface_ClockSource = _BRINetworkProfile_LineInterface_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 8),
    _BRINetworkProfile_LineInterface_ClockSource_Type()
)
bRINetworkProfile_LineInterface_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_ClockSource.setStatus("mandatory")


class _BRINetworkProfile_LineInterface_IdslBandwidth_Type(Integer32):
    """Custom type bRINetworkProfile_LineInterface_IdslBandwidth based on Integer32"""
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


_BRINetworkProfile_LineInterface_IdslBandwidth_Type.__name__ = "Integer32"
_BRINetworkProfile_LineInterface_IdslBandwidth_Object = MibScalar
bRINetworkProfile_LineInterface_IdslBandwidth = _BRINetworkProfile_LineInterface_IdslBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 9),
    _BRINetworkProfile_LineInterface_IdslBandwidth_Type()
)
bRINetworkProfile_LineInterface_IdslBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_IdslBandwidth.setStatus("mandatory")
_BRINetworkProfile_LineInterface_Gr303Crv_Type = Integer32
_BRINetworkProfile_LineInterface_Gr303Crv_Object = MibScalar
bRINetworkProfile_LineInterface_Gr303Crv = _BRINetworkProfile_LineInterface_Gr303Crv_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 10),
    _BRINetworkProfile_LineInterface_Gr303Crv_Type()
)
bRINetworkProfile_LineInterface_Gr303Crv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_Gr303Crv.setStatus("mandatory")
_BRINetworkProfile_LineInterface_Gr303InterfaceGroup_Type = Integer32
_BRINetworkProfile_LineInterface_Gr303InterfaceGroup_Object = MibScalar
bRINetworkProfile_LineInterface_Gr303InterfaceGroup = _BRINetworkProfile_LineInterface_Gr303InterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 11),
    _BRINetworkProfile_LineInterface_Gr303InterfaceGroup_Type()
)
bRINetworkProfile_LineInterface_Gr303InterfaceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_Gr303InterfaceGroup.setStatus("mandatory")


class _BRINetworkProfile_LineInterface_IgnoreLineup_Type(Integer32):
    """Custom type bRINetworkProfile_LineInterface_IgnoreLineup based on Integer32"""
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


_BRINetworkProfile_LineInterface_IgnoreLineup_Type.__name__ = "Integer32"
_BRINetworkProfile_LineInterface_IgnoreLineup_Object = MibScalar
bRINetworkProfile_LineInterface_IgnoreLineup = _BRINetworkProfile_LineInterface_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 2, 1, 12),
    _BRINetworkProfile_LineInterface_IgnoreLineup_Type()
)
bRINetworkProfile_LineInterface_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_IgnoreLineup.setStatus("mandatory")
_MibbRINetworkProfile_LineInterface_ChannelConfigTable_Object = MibTable
mibbRINetworkProfile_LineInterface_ChannelConfigTable = _MibbRINetworkProfile_LineInterface_ChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 3)
)
if mibBuilder.loadTexts:
    mibbRINetworkProfile_LineInterface_ChannelConfigTable.setStatus("mandatory")
_MibbRINetworkProfile_LineInterface_ChannelConfigEntry_Object = MibTableRow
mibbRINetworkProfile_LineInterface_ChannelConfigEntry = _MibbRINetworkProfile_LineInterface_ChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 3, 1)
)
mibbRINetworkProfile_LineInterface_ChannelConfigEntry.setIndexNames(
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-LineInterface-ChannelConfig-Shelf-o"),
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-LineInterface-ChannelConfig-Slot-o"),
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-LineInterface-ChannelConfig-Item-o"),
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-LineInterface-ChannelConfig-Index-o"),
    (0, "ASCEND-MIBBRITE-MIB", "bRINetworkProfile-LineInterface-ChannelConfig-Index1-o"),
)
if mibBuilder.loadTexts:
    mibbRINetworkProfile_LineInterface_ChannelConfigEntry.setStatus("mandatory")
_BRINetworkProfile_LineInterface_ChannelConfig_Shelf_o_Type = Integer32
_BRINetworkProfile_LineInterface_ChannelConfig_Shelf_o_Object = MibScalar
bRINetworkProfile_LineInterface_ChannelConfig_Shelf_o = _BRINetworkProfile_LineInterface_ChannelConfig_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 3, 1, 1),
    _BRINetworkProfile_LineInterface_ChannelConfig_Shelf_o_Type()
)
bRINetworkProfile_LineInterface_ChannelConfig_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_ChannelConfig_Shelf_o.setStatus("mandatory")
_BRINetworkProfile_LineInterface_ChannelConfig_Slot_o_Type = Integer32
_BRINetworkProfile_LineInterface_ChannelConfig_Slot_o_Object = MibScalar
bRINetworkProfile_LineInterface_ChannelConfig_Slot_o = _BRINetworkProfile_LineInterface_ChannelConfig_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 3, 1, 2),
    _BRINetworkProfile_LineInterface_ChannelConfig_Slot_o_Type()
)
bRINetworkProfile_LineInterface_ChannelConfig_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_ChannelConfig_Slot_o.setStatus("mandatory")
_BRINetworkProfile_LineInterface_ChannelConfig_Item_o_Type = Integer32
_BRINetworkProfile_LineInterface_ChannelConfig_Item_o_Object = MibScalar
bRINetworkProfile_LineInterface_ChannelConfig_Item_o = _BRINetworkProfile_LineInterface_ChannelConfig_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 3, 1, 3),
    _BRINetworkProfile_LineInterface_ChannelConfig_Item_o_Type()
)
bRINetworkProfile_LineInterface_ChannelConfig_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_ChannelConfig_Item_o.setStatus("mandatory")
_BRINetworkProfile_LineInterface_ChannelConfig_Index_o_Type = Integer32
_BRINetworkProfile_LineInterface_ChannelConfig_Index_o_Object = MibScalar
bRINetworkProfile_LineInterface_ChannelConfig_Index_o = _BRINetworkProfile_LineInterface_ChannelConfig_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 3, 1, 4),
    _BRINetworkProfile_LineInterface_ChannelConfig_Index_o_Type()
)
bRINetworkProfile_LineInterface_ChannelConfig_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_ChannelConfig_Index_o.setStatus("mandatory")
_BRINetworkProfile_LineInterface_ChannelConfig_Index1_o_Type = Integer32
_BRINetworkProfile_LineInterface_ChannelConfig_Index1_o_Object = MibScalar
bRINetworkProfile_LineInterface_ChannelConfig_Index1_o = _BRINetworkProfile_LineInterface_ChannelConfig_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 3, 1, 5),
    _BRINetworkProfile_LineInterface_ChannelConfig_Index1_o_Type()
)
bRINetworkProfile_LineInterface_ChannelConfig_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_ChannelConfig_Index1_o.setStatus("mandatory")


class _BRINetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Type(Integer32):
    """Custom type bRINetworkProfile_LineInterface_ChannelConfig_ChannelUsage based on Integer32"""
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


_BRINetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Type.__name__ = "Integer32"
_BRINetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Object = MibScalar
bRINetworkProfile_LineInterface_ChannelConfig_ChannelUsage = _BRINetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 3, 1, 6),
    _BRINetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Type()
)
bRINetworkProfile_LineInterface_ChannelConfig_ChannelUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_ChannelConfig_ChannelUsage.setStatus("mandatory")
_BRINetworkProfile_LineInterface_ChannelConfig_NailedGroup_Type = Integer32
_BRINetworkProfile_LineInterface_ChannelConfig_NailedGroup_Object = MibScalar
bRINetworkProfile_LineInterface_ChannelConfig_NailedGroup = _BRINetworkProfile_LineInterface_ChannelConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 63, 3, 1, 7),
    _BRINetworkProfile_LineInterface_ChannelConfig_NailedGroup_Type()
)
bRINetworkProfile_LineInterface_ChannelConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkProfile_LineInterface_ChannelConfig_NailedGroup.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBBRITE-MIB",
    **{"DisplayString": DisplayString,
       "mibbRINetworkProfile": mibbRINetworkProfile,
       "mibbRINetworkProfileTable": mibbRINetworkProfileTable,
       "mibbRINetworkProfileEntry": mibbRINetworkProfileEntry,
       "bRINetworkProfile-Shelf-o": bRINetworkProfile_Shelf_o,
       "bRINetworkProfile-Slot-o": bRINetworkProfile_Slot_o,
       "bRINetworkProfile-Item-o": bRINetworkProfile_Item_o,
       "bRINetworkProfile-ProfileNumber": bRINetworkProfile_ProfileNumber,
       "bRINetworkProfile-Name": bRINetworkProfile_Name,
       "bRINetworkProfile-PhysicalAddress-Shelf": bRINetworkProfile_PhysicalAddress_Shelf,
       "bRINetworkProfile-PhysicalAddress-Slot": bRINetworkProfile_PhysicalAddress_Slot,
       "bRINetworkProfile-PhysicalAddress-ItemNumber": bRINetworkProfile_PhysicalAddress_ItemNumber,
       "bRINetworkProfile-SwitchType": bRINetworkProfile_SwitchType,
       "bRINetworkProfile-AnsVoiceCall": bRINetworkProfile_AnsVoiceCall,
       "bRINetworkProfile-ConcatNailedLines": bRINetworkProfile_ConcatNailedLines,
       "bRINetworkProfile-BriAnalogEncode": bRINetworkProfile_BriAnalogEncode,
       "bRINetworkProfile-Action-o": bRINetworkProfile_Action_o,
       "mibbRINetworkProfile-LineInterfaceTable": mibbRINetworkProfile_LineInterfaceTable,
       "mibbRINetworkProfile-LineInterfaceEntry": mibbRINetworkProfile_LineInterfaceEntry,
       "bRINetworkProfile-LineInterface-Shelf-o": bRINetworkProfile_LineInterface_Shelf_o,
       "bRINetworkProfile-LineInterface-Slot-o": bRINetworkProfile_LineInterface_Slot_o,
       "bRINetworkProfile-LineInterface-Item-o": bRINetworkProfile_LineInterface_Item_o,
       "bRINetworkProfile-LineInterface-Index-o": bRINetworkProfile_LineInterface_Index_o,
       "bRINetworkProfile-LineInterface-Enabled": bRINetworkProfile_LineInterface_Enabled,
       "bRINetworkProfile-LineInterface-AnswerNumber1": bRINetworkProfile_LineInterface_AnswerNumber1,
       "bRINetworkProfile-LineInterface-AnswerNumber2": bRINetworkProfile_LineInterface_AnswerNumber2,
       "bRINetworkProfile-LineInterface-ClockSource": bRINetworkProfile_LineInterface_ClockSource,
       "bRINetworkProfile-LineInterface-IdslBandwidth": bRINetworkProfile_LineInterface_IdslBandwidth,
       "bRINetworkProfile-LineInterface-Gr303Crv": bRINetworkProfile_LineInterface_Gr303Crv,
       "bRINetworkProfile-LineInterface-Gr303InterfaceGroup": bRINetworkProfile_LineInterface_Gr303InterfaceGroup,
       "bRINetworkProfile-LineInterface-IgnoreLineup": bRINetworkProfile_LineInterface_IgnoreLineup,
       "mibbRINetworkProfile-LineInterface-ChannelConfigTable": mibbRINetworkProfile_LineInterface_ChannelConfigTable,
       "mibbRINetworkProfile-LineInterface-ChannelConfigEntry": mibbRINetworkProfile_LineInterface_ChannelConfigEntry,
       "bRINetworkProfile-LineInterface-ChannelConfig-Shelf-o": bRINetworkProfile_LineInterface_ChannelConfig_Shelf_o,
       "bRINetworkProfile-LineInterface-ChannelConfig-Slot-o": bRINetworkProfile_LineInterface_ChannelConfig_Slot_o,
       "bRINetworkProfile-LineInterface-ChannelConfig-Item-o": bRINetworkProfile_LineInterface_ChannelConfig_Item_o,
       "bRINetworkProfile-LineInterface-ChannelConfig-Index-o": bRINetworkProfile_LineInterface_ChannelConfig_Index_o,
       "bRINetworkProfile-LineInterface-ChannelConfig-Index1-o": bRINetworkProfile_LineInterface_ChannelConfig_Index1_o,
       "bRINetworkProfile-LineInterface-ChannelConfig-ChannelUsage": bRINetworkProfile_LineInterface_ChannelConfig_ChannelUsage,
       "bRINetworkProfile-LineInterface-ChannelConfig-NailedGroup": bRINetworkProfile_LineInterface_ChannelConfig_NailedGroup}
)
