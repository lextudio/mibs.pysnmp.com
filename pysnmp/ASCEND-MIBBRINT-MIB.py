# SNMP MIB module (ASCEND-MIBBRINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBBRINT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:17 2024
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

_MibbRIHostProfile_ObjectIdentity = ObjectIdentity
mibbRIHostProfile = _MibbRIHostProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 62)
)
_MibbRIHostProfileTable_Object = MibTable
mibbRIHostProfileTable = _MibbRIHostProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1)
)
if mibBuilder.loadTexts:
    mibbRIHostProfileTable.setStatus("mandatory")
_MibbRIHostProfileEntry_Object = MibTableRow
mibbRIHostProfileEntry = _MibbRIHostProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1)
)
mibbRIHostProfileEntry.setIndexNames(
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-Shelf-o"),
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-Slot-o"),
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibbRIHostProfileEntry.setStatus("mandatory")
_BRIHostProfile_Shelf_o_Type = Integer32
_BRIHostProfile_Shelf_o_Object = MibScalar
bRIHostProfile_Shelf_o = _BRIHostProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 1),
    _BRIHostProfile_Shelf_o_Type()
)
bRIHostProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_Shelf_o.setStatus("mandatory")
_BRIHostProfile_Slot_o_Type = Integer32
_BRIHostProfile_Slot_o_Object = MibScalar
bRIHostProfile_Slot_o = _BRIHostProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 2),
    _BRIHostProfile_Slot_o_Type()
)
bRIHostProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_Slot_o.setStatus("mandatory")
_BRIHostProfile_Item_o_Type = Integer32
_BRIHostProfile_Item_o_Object = MibScalar
bRIHostProfile_Item_o = _BRIHostProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 3),
    _BRIHostProfile_Item_o_Type()
)
bRIHostProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_Item_o.setStatus("mandatory")
_BRIHostProfile_ProfileNumber_Type = Integer32
_BRIHostProfile_ProfileNumber_Object = MibScalar
bRIHostProfile_ProfileNumber = _BRIHostProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 4),
    _BRIHostProfile_ProfileNumber_Type()
)
bRIHostProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_ProfileNumber.setStatus("mandatory")
_BRIHostProfile_Name_Type = DisplayString
_BRIHostProfile_Name_Object = MibScalar
bRIHostProfile_Name = _BRIHostProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 5),
    _BRIHostProfile_Name_Type()
)
bRIHostProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_Name.setStatus("mandatory")


class _BRIHostProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type bRIHostProfile_PhysicalAddress_Shelf based on Integer32"""
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


_BRIHostProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_BRIHostProfile_PhysicalAddress_Shelf_Object = MibScalar
bRIHostProfile_PhysicalAddress_Shelf = _BRIHostProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 6),
    _BRIHostProfile_PhysicalAddress_Shelf_Type()
)
bRIHostProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _BRIHostProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type bRIHostProfile_PhysicalAddress_Slot based on Integer32"""
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


_BRIHostProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_BRIHostProfile_PhysicalAddress_Slot_Object = MibScalar
bRIHostProfile_PhysicalAddress_Slot = _BRIHostProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 7),
    _BRIHostProfile_PhysicalAddress_Slot_Type()
)
bRIHostProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_PhysicalAddress_Slot.setStatus("mandatory")
_BRIHostProfile_PhysicalAddress_ItemNumber_Type = Integer32
_BRIHostProfile_PhysicalAddress_ItemNumber_Object = MibScalar
bRIHostProfile_PhysicalAddress_ItemNumber = _BRIHostProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 8),
    _BRIHostProfile_PhysicalAddress_ItemNumber_Type()
)
bRIHostProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _BRIHostProfile_SwitchType_Type(Integer32):
    """Custom type bRIHostProfile_SwitchType based on Integer32"""
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


_BRIHostProfile_SwitchType_Type.__name__ = "Integer32"
_BRIHostProfile_SwitchType_Object = MibScalar
bRIHostProfile_SwitchType = _BRIHostProfile_SwitchType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 9),
    _BRIHostProfile_SwitchType_Type()
)
bRIHostProfile_SwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_SwitchType.setStatus("mandatory")


class _BRIHostProfile_DownStreamPriority_Type(Integer32):
    """Custom type bRIHostProfile_DownStreamPriority based on Integer32"""
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


_BRIHostProfile_DownStreamPriority_Type.__name__ = "Integer32"
_BRIHostProfile_DownStreamPriority_Object = MibScalar
bRIHostProfile_DownStreamPriority = _BRIHostProfile_DownStreamPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 10),
    _BRIHostProfile_DownStreamPriority_Type()
)
bRIHostProfile_DownStreamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_DownStreamPriority.setStatus("mandatory")


class _BRIHostProfile_DownStreamBriWan_Type(Integer32):
    """Custom type bRIHostProfile_DownStreamBriWan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aatNone", 1),
          ("aatOne", 2),
          ("aatTwo", 3))
    )


_BRIHostProfile_DownStreamBriWan_Type.__name__ = "Integer32"
_BRIHostProfile_DownStreamBriWan_Object = MibScalar
bRIHostProfile_DownStreamBriWan = _BRIHostProfile_DownStreamBriWan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 11),
    _BRIHostProfile_DownStreamBriWan_Type()
)
bRIHostProfile_DownStreamBriWan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_DownStreamBriWan.setStatus("mandatory")


class _BRIHostProfile_Action_o_Type(Integer32):
    """Custom type bRIHostProfile_Action_o based on Integer32"""
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


_BRIHostProfile_Action_o_Type.__name__ = "Integer32"
_BRIHostProfile_Action_o_Object = MibScalar
bRIHostProfile_Action_o = _BRIHostProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 1, 1, 12),
    _BRIHostProfile_Action_o_Type()
)
bRIHostProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_Action_o.setStatus("mandatory")
_MibbRIHostProfile_LineInterfaceTable_Object = MibTable
mibbRIHostProfile_LineInterfaceTable = _MibbRIHostProfile_LineInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 2)
)
if mibBuilder.loadTexts:
    mibbRIHostProfile_LineInterfaceTable.setStatus("mandatory")
_MibbRIHostProfile_LineInterfaceEntry_Object = MibTableRow
mibbRIHostProfile_LineInterfaceEntry = _MibbRIHostProfile_LineInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 2, 1)
)
mibbRIHostProfile_LineInterfaceEntry.setIndexNames(
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-LineInterface-Shelf-o"),
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-LineInterface-Slot-o"),
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-LineInterface-Item-o"),
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-LineInterface-Index-o"),
)
if mibBuilder.loadTexts:
    mibbRIHostProfile_LineInterfaceEntry.setStatus("mandatory")
_BRIHostProfile_LineInterface_Shelf_o_Type = Integer32
_BRIHostProfile_LineInterface_Shelf_o_Object = MibScalar
bRIHostProfile_LineInterface_Shelf_o = _BRIHostProfile_LineInterface_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 2, 1, 1),
    _BRIHostProfile_LineInterface_Shelf_o_Type()
)
bRIHostProfile_LineInterface_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_Shelf_o.setStatus("mandatory")
_BRIHostProfile_LineInterface_Slot_o_Type = Integer32
_BRIHostProfile_LineInterface_Slot_o_Object = MibScalar
bRIHostProfile_LineInterface_Slot_o = _BRIHostProfile_LineInterface_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 2, 1, 2),
    _BRIHostProfile_LineInterface_Slot_o_Type()
)
bRIHostProfile_LineInterface_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_Slot_o.setStatus("mandatory")
_BRIHostProfile_LineInterface_Item_o_Type = Integer32
_BRIHostProfile_LineInterface_Item_o_Object = MibScalar
bRIHostProfile_LineInterface_Item_o = _BRIHostProfile_LineInterface_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 2, 1, 3),
    _BRIHostProfile_LineInterface_Item_o_Type()
)
bRIHostProfile_LineInterface_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_Item_o.setStatus("mandatory")
_BRIHostProfile_LineInterface_Index_o_Type = Integer32
_BRIHostProfile_LineInterface_Index_o_Object = MibScalar
bRIHostProfile_LineInterface_Index_o = _BRIHostProfile_LineInterface_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 2, 1, 4),
    _BRIHostProfile_LineInterface_Index_o_Type()
)
bRIHostProfile_LineInterface_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_Index_o.setStatus("mandatory")


class _BRIHostProfile_LineInterface_LineEnabled_Type(Integer32):
    """Custom type bRIHostProfile_LineInterface_LineEnabled based on Integer32"""
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


_BRIHostProfile_LineInterface_LineEnabled_Type.__name__ = "Integer32"
_BRIHostProfile_LineInterface_LineEnabled_Object = MibScalar
bRIHostProfile_LineInterface_LineEnabled = _BRIHostProfile_LineInterface_LineEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 2, 1, 5),
    _BRIHostProfile_LineInterface_LineEnabled_Type()
)
bRIHostProfile_LineInterface_LineEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_LineEnabled.setStatus("mandatory")
_BRIHostProfile_LineInterface_DialPlan_Type = Integer32
_BRIHostProfile_LineInterface_DialPlan_Object = MibScalar
bRIHostProfile_LineInterface_DialPlan = _BRIHostProfile_LineInterface_DialPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 2, 1, 6),
    _BRIHostProfile_LineInterface_DialPlan_Type()
)
bRIHostProfile_LineInterface_DialPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_DialPlan.setStatus("mandatory")
_BRIHostProfile_LineInterface_AnswerNumber1_Type = DisplayString
_BRIHostProfile_LineInterface_AnswerNumber1_Object = MibScalar
bRIHostProfile_LineInterface_AnswerNumber1 = _BRIHostProfile_LineInterface_AnswerNumber1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 2, 1, 7),
    _BRIHostProfile_LineInterface_AnswerNumber1_Type()
)
bRIHostProfile_LineInterface_AnswerNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_AnswerNumber1.setStatus("mandatory")
_BRIHostProfile_LineInterface_AnswerNumber2_Type = DisplayString
_BRIHostProfile_LineInterface_AnswerNumber2_Object = MibScalar
bRIHostProfile_LineInterface_AnswerNumber2 = _BRIHostProfile_LineInterface_AnswerNumber2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 2, 1, 8),
    _BRIHostProfile_LineInterface_AnswerNumber2_Type()
)
bRIHostProfile_LineInterface_AnswerNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_AnswerNumber2.setStatus("mandatory")
_MibbRIHostProfile_LineInterface_DownStreamLlinkTable_Object = MibTable
mibbRIHostProfile_LineInterface_DownStreamLlinkTable = _MibbRIHostProfile_LineInterface_DownStreamLlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 3)
)
if mibBuilder.loadTexts:
    mibbRIHostProfile_LineInterface_DownStreamLlinkTable.setStatus("mandatory")
_MibbRIHostProfile_LineInterface_DownStreamLlinkEntry_Object = MibTableRow
mibbRIHostProfile_LineInterface_DownStreamLlinkEntry = _MibbRIHostProfile_LineInterface_DownStreamLlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 3, 1)
)
mibbRIHostProfile_LineInterface_DownStreamLlinkEntry.setIndexNames(
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-LineInterface-DownStreamLlink-Shelf-o"),
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-LineInterface-DownStreamLlink-Slot-o"),
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-LineInterface-DownStreamLlink-Item-o"),
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-LineInterface-DownStreamLlink-Index-o"),
    (0, "ASCEND-MIBBRINT-MIB", "bRIHostProfile-LineInterface-DownStreamLlink-Index1-o"),
)
if mibBuilder.loadTexts:
    mibbRIHostProfile_LineInterface_DownStreamLlinkEntry.setStatus("mandatory")
_BRIHostProfile_LineInterface_DownStreamLlink_Shelf_o_Type = Integer32
_BRIHostProfile_LineInterface_DownStreamLlink_Shelf_o_Object = MibScalar
bRIHostProfile_LineInterface_DownStreamLlink_Shelf_o = _BRIHostProfile_LineInterface_DownStreamLlink_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 3, 1, 1),
    _BRIHostProfile_LineInterface_DownStreamLlink_Shelf_o_Type()
)
bRIHostProfile_LineInterface_DownStreamLlink_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_DownStreamLlink_Shelf_o.setStatus("mandatory")
_BRIHostProfile_LineInterface_DownStreamLlink_Slot_o_Type = Integer32
_BRIHostProfile_LineInterface_DownStreamLlink_Slot_o_Object = MibScalar
bRIHostProfile_LineInterface_DownStreamLlink_Slot_o = _BRIHostProfile_LineInterface_DownStreamLlink_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 3, 1, 2),
    _BRIHostProfile_LineInterface_DownStreamLlink_Slot_o_Type()
)
bRIHostProfile_LineInterface_DownStreamLlink_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_DownStreamLlink_Slot_o.setStatus("mandatory")
_BRIHostProfile_LineInterface_DownStreamLlink_Item_o_Type = Integer32
_BRIHostProfile_LineInterface_DownStreamLlink_Item_o_Object = MibScalar
bRIHostProfile_LineInterface_DownStreamLlink_Item_o = _BRIHostProfile_LineInterface_DownStreamLlink_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 3, 1, 3),
    _BRIHostProfile_LineInterface_DownStreamLlink_Item_o_Type()
)
bRIHostProfile_LineInterface_DownStreamLlink_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_DownStreamLlink_Item_o.setStatus("mandatory")
_BRIHostProfile_LineInterface_DownStreamLlink_Index_o_Type = Integer32
_BRIHostProfile_LineInterface_DownStreamLlink_Index_o_Object = MibScalar
bRIHostProfile_LineInterface_DownStreamLlink_Index_o = _BRIHostProfile_LineInterface_DownStreamLlink_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 3, 1, 4),
    _BRIHostProfile_LineInterface_DownStreamLlink_Index_o_Type()
)
bRIHostProfile_LineInterface_DownStreamLlink_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_DownStreamLlink_Index_o.setStatus("mandatory")
_BRIHostProfile_LineInterface_DownStreamLlink_Index1_o_Type = Integer32
_BRIHostProfile_LineInterface_DownStreamLlink_Index1_o_Object = MibScalar
bRIHostProfile_LineInterface_DownStreamLlink_Index1_o = _BRIHostProfile_LineInterface_DownStreamLlink_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 62, 3, 1, 5),
    _BRIHostProfile_LineInterface_DownStreamLlink_Index1_o_Type()
)
bRIHostProfile_LineInterface_DownStreamLlink_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRIHostProfile_LineInterface_DownStreamLlink_Index1_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBBRINT-MIB",
    **{"DisplayString": DisplayString,
       "mibbRIHostProfile": mibbRIHostProfile,
       "mibbRIHostProfileTable": mibbRIHostProfileTable,
       "mibbRIHostProfileEntry": mibbRIHostProfileEntry,
       "bRIHostProfile-Shelf-o": bRIHostProfile_Shelf_o,
       "bRIHostProfile-Slot-o": bRIHostProfile_Slot_o,
       "bRIHostProfile-Item-o": bRIHostProfile_Item_o,
       "bRIHostProfile-ProfileNumber": bRIHostProfile_ProfileNumber,
       "bRIHostProfile-Name": bRIHostProfile_Name,
       "bRIHostProfile-PhysicalAddress-Shelf": bRIHostProfile_PhysicalAddress_Shelf,
       "bRIHostProfile-PhysicalAddress-Slot": bRIHostProfile_PhysicalAddress_Slot,
       "bRIHostProfile-PhysicalAddress-ItemNumber": bRIHostProfile_PhysicalAddress_ItemNumber,
       "bRIHostProfile-SwitchType": bRIHostProfile_SwitchType,
       "bRIHostProfile-DownStreamPriority": bRIHostProfile_DownStreamPriority,
       "bRIHostProfile-DownStreamBriWan": bRIHostProfile_DownStreamBriWan,
       "bRIHostProfile-Action-o": bRIHostProfile_Action_o,
       "mibbRIHostProfile-LineInterfaceTable": mibbRIHostProfile_LineInterfaceTable,
       "mibbRIHostProfile-LineInterfaceEntry": mibbRIHostProfile_LineInterfaceEntry,
       "bRIHostProfile-LineInterface-Shelf-o": bRIHostProfile_LineInterface_Shelf_o,
       "bRIHostProfile-LineInterface-Slot-o": bRIHostProfile_LineInterface_Slot_o,
       "bRIHostProfile-LineInterface-Item-o": bRIHostProfile_LineInterface_Item_o,
       "bRIHostProfile-LineInterface-Index-o": bRIHostProfile_LineInterface_Index_o,
       "bRIHostProfile-LineInterface-LineEnabled": bRIHostProfile_LineInterface_LineEnabled,
       "bRIHostProfile-LineInterface-DialPlan": bRIHostProfile_LineInterface_DialPlan,
       "bRIHostProfile-LineInterface-AnswerNumber1": bRIHostProfile_LineInterface_AnswerNumber1,
       "bRIHostProfile-LineInterface-AnswerNumber2": bRIHostProfile_LineInterface_AnswerNumber2,
       "mibbRIHostProfile-LineInterface-DownStreamLlinkTable": mibbRIHostProfile_LineInterface_DownStreamLlinkTable,
       "mibbRIHostProfile-LineInterface-DownStreamLlinkEntry": mibbRIHostProfile_LineInterface_DownStreamLlinkEntry,
       "bRIHostProfile-LineInterface-DownStreamLlink-Shelf-o": bRIHostProfile_LineInterface_DownStreamLlink_Shelf_o,
       "bRIHostProfile-LineInterface-DownStreamLlink-Slot-o": bRIHostProfile_LineInterface_DownStreamLlink_Slot_o,
       "bRIHostProfile-LineInterface-DownStreamLlink-Item-o": bRIHostProfile_LineInterface_DownStreamLlink_Item_o,
       "bRIHostProfile-LineInterface-DownStreamLlink-Index-o": bRIHostProfile_LineInterface_DownStreamLlink_Index_o,
       "bRIHostProfile-LineInterface-DownStreamLlink-Index1-o": bRIHostProfile_LineInterface_DownStreamLlink_Index1_o}
)
