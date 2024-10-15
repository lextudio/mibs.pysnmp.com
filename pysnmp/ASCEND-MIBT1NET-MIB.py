# SNMP MIB module (ASCEND-MIBT1NET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBT1NET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:24 2024
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

_Mibt1NetworkProfileV1_ObjectIdentity = ObjectIdentity
mibt1NetworkProfileV1 = _Mibt1NetworkProfileV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 126)
)
_Mibt1NetworkProfileV1Table_Object = MibTable
mibt1NetworkProfileV1Table = _Mibt1NetworkProfileV1Table_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1)
)
if mibBuilder.loadTexts:
    mibt1NetworkProfileV1Table.setStatus("mandatory")
_Mibt1NetworkProfileV1Entry_Object = MibTableRow
mibt1NetworkProfileV1Entry = _Mibt1NetworkProfileV1Entry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1)
)
mibt1NetworkProfileV1Entry.setIndexNames(
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfileV1-Name"),
)
if mibBuilder.loadTexts:
    mibt1NetworkProfileV1Entry.setStatus("mandatory")
_T1NetworkProfileV1_ProfileNumber_Type = Integer32
_T1NetworkProfileV1_ProfileNumber_Object = MibScalar
t1NetworkProfileV1_ProfileNumber = _T1NetworkProfileV1_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1, 1),
    _T1NetworkProfileV1_ProfileNumber_Type()
)
t1NetworkProfileV1_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_ProfileNumber.setStatus("mandatory")
_T1NetworkProfileV1_Name_Type = DisplayString
_T1NetworkProfileV1_Name_Object = MibScalar
t1NetworkProfileV1_Name = _T1NetworkProfileV1_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1, 2),
    _T1NetworkProfileV1_Name_Type()
)
t1NetworkProfileV1_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_Name.setStatus("mandatory")


class _T1NetworkProfileV1_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type t1NetworkProfileV1_PhysicalAddress_Shelf based on Integer32"""
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


_T1NetworkProfileV1_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_T1NetworkProfileV1_PhysicalAddress_Shelf_Object = MibScalar
t1NetworkProfileV1_PhysicalAddress_Shelf = _T1NetworkProfileV1_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1, 3),
    _T1NetworkProfileV1_PhysicalAddress_Shelf_Type()
)
t1NetworkProfileV1_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_PhysicalAddress_Shelf.setStatus("mandatory")


class _T1NetworkProfileV1_PhysicalAddress_Slot_Type(Integer32):
    """Custom type t1NetworkProfileV1_PhysicalAddress_Slot based on Integer32"""
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


_T1NetworkProfileV1_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_T1NetworkProfileV1_PhysicalAddress_Slot_Object = MibScalar
t1NetworkProfileV1_PhysicalAddress_Slot = _T1NetworkProfileV1_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1, 4),
    _T1NetworkProfileV1_PhysicalAddress_Slot_Type()
)
t1NetworkProfileV1_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_PhysicalAddress_Slot.setStatus("mandatory")
_T1NetworkProfileV1_PhysicalAddress_ItemNumber_Type = Integer32
_T1NetworkProfileV1_PhysicalAddress_ItemNumber_Object = MibScalar
t1NetworkProfileV1_PhysicalAddress_ItemNumber = _T1NetworkProfileV1_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1, 5),
    _T1NetworkProfileV1_PhysicalAddress_ItemNumber_Type()
)
t1NetworkProfileV1_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _T1NetworkProfileV1_BackToBack_Type(Integer32):
    """Custom type t1NetworkProfileV1_BackToBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_T1NetworkProfileV1_BackToBack_Type.__name__ = "Integer32"
_T1NetworkProfileV1_BackToBack_Object = MibScalar
t1NetworkProfileV1_BackToBack = _T1NetworkProfileV1_BackToBack_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1, 6),
    _T1NetworkProfileV1_BackToBack_Type()
)
t1NetworkProfileV1_BackToBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_BackToBack.setStatus("mandatory")


class _T1NetworkProfileV1_PrimaryChannelUsage_Type(Integer32):
    """Custom type t1NetworkProfileV1_PrimaryChannelUsage based on Integer32"""
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
        *(("dropAndInsert", 4),
          ("dualNetworkInterface", 5),
          ("lineDisable", 2),
          ("lineUnavailable", 1),
          ("t1LineQuiesce", 3),
          ("tOnlineUsrInterface", 6),
          ("tOnlineZgrInterface", 7))
    )


_T1NetworkProfileV1_PrimaryChannelUsage_Type.__name__ = "Integer32"
_T1NetworkProfileV1_PrimaryChannelUsage_Object = MibScalar
t1NetworkProfileV1_PrimaryChannelUsage = _T1NetworkProfileV1_PrimaryChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1, 7),
    _T1NetworkProfileV1_PrimaryChannelUsage_Type()
)
t1NetworkProfileV1_PrimaryChannelUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_PrimaryChannelUsage.setStatus("mandatory")


class _T1NetworkProfileV1_SecondaryChannelUsage_Type(Integer32):
    """Custom type t1NetworkProfileV1_SecondaryChannelUsage based on Integer32"""
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
        *(("dropAndInsert", 4),
          ("dualNetworkInterface", 5),
          ("lineDisable", 2),
          ("lineUnavailable", 1),
          ("t1LineQuiesce", 3),
          ("tOnlineUsrInterface", 6),
          ("tOnlineZgrInterface", 7))
    )


_T1NetworkProfileV1_SecondaryChannelUsage_Type.__name__ = "Integer32"
_T1NetworkProfileV1_SecondaryChannelUsage_Object = MibScalar
t1NetworkProfileV1_SecondaryChannelUsage = _T1NetworkProfileV1_SecondaryChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1, 8),
    _T1NetworkProfileV1_SecondaryChannelUsage_Type()
)
t1NetworkProfileV1_SecondaryChannelUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_SecondaryChannelUsage.setStatus("mandatory")


class _T1NetworkProfileV1_TertiaryChannelUsage_Type(Integer32):
    """Custom type t1NetworkProfileV1_TertiaryChannelUsage based on Integer32"""
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
        *(("dropAndInsert", 4),
          ("dualNetworkInterface", 5),
          ("lineDisable", 2),
          ("lineUnavailable", 1),
          ("t1LineQuiesce", 3),
          ("tOnlineUsrInterface", 6),
          ("tOnlineZgrInterface", 7))
    )


_T1NetworkProfileV1_TertiaryChannelUsage_Type.__name__ = "Integer32"
_T1NetworkProfileV1_TertiaryChannelUsage_Object = MibScalar
t1NetworkProfileV1_TertiaryChannelUsage = _T1NetworkProfileV1_TertiaryChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1, 9),
    _T1NetworkProfileV1_TertiaryChannelUsage_Type()
)
t1NetworkProfileV1_TertiaryChannelUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_TertiaryChannelUsage.setStatus("mandatory")


class _T1NetworkProfileV1_Action_o_Type(Integer32):
    """Custom type t1NetworkProfileV1_Action_o based on Integer32"""
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


_T1NetworkProfileV1_Action_o_Type.__name__ = "Integer32"
_T1NetworkProfileV1_Action_o_Object = MibScalar
t1NetworkProfileV1_Action_o = _T1NetworkProfileV1_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 1, 1, 10),
    _T1NetworkProfileV1_Action_o_Type()
)
t1NetworkProfileV1_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_Action_o.setStatus("mandatory")
_Mibt1NetworkProfileV1_LineInterfaceTable_Object = MibTable
mibt1NetworkProfileV1_LineInterfaceTable = _Mibt1NetworkProfileV1_LineInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2)
)
if mibBuilder.loadTexts:
    mibt1NetworkProfileV1_LineInterfaceTable.setStatus("mandatory")
_Mibt1NetworkProfileV1_LineInterfaceEntry_Object = MibTableRow
mibt1NetworkProfileV1_LineInterfaceEntry = _Mibt1NetworkProfileV1_LineInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1)
)
mibt1NetworkProfileV1_LineInterfaceEntry.setIndexNames(
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfileV1-LineInterface-Name"),
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfileV1-LineInterface-Index-o"),
)
if mibBuilder.loadTexts:
    mibt1NetworkProfileV1_LineInterfaceEntry.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_Name_Type = DisplayString
_T1NetworkProfileV1_LineInterface_Name_Object = MibScalar
t1NetworkProfileV1_LineInterface_Name = _T1NetworkProfileV1_LineInterface_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 1),
    _T1NetworkProfileV1_LineInterface_Name_Type()
)
t1NetworkProfileV1_LineInterface_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Name.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_Index_o_Type = Integer32
_T1NetworkProfileV1_LineInterface_Index_o_Object = MibScalar
t1NetworkProfileV1_LineInterface_Index_o = _T1NetworkProfileV1_LineInterface_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 2),
    _T1NetworkProfileV1_LineInterface_Index_o_Type()
)
t1NetworkProfileV1_LineInterface_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Index_o.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_Enabled_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_Enabled based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_Enabled_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_Enabled_Object = MibScalar
t1NetworkProfileV1_LineInterface_Enabled = _T1NetworkProfileV1_LineInterface_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 3),
    _T1NetworkProfileV1_LineInterface_Enabled_Type()
)
t1NetworkProfileV1_LineInterface_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Enabled.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_TOnlineType_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_TOnlineType based on Integer32"""
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
        *(("none", 1),
          ("nt", 2),
          ("numberOfTonline", 4),
          ("te", 3))
    )


_T1NetworkProfileV1_LineInterface_TOnlineType_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_TOnlineType_Object = MibScalar
t1NetworkProfileV1_LineInterface_TOnlineType = _T1NetworkProfileV1_LineInterface_TOnlineType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 4),
    _T1NetworkProfileV1_LineInterface_TOnlineType_Type()
)
t1NetworkProfileV1_LineInterface_TOnlineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_TOnlineType.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_FrameType_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_FrameType based on Integer32"""
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
        *(("d4", 1),
          ("esf", 2),
          ("g703", 3),
          ("n-2ds", 4))
    )


_T1NetworkProfileV1_LineInterface_FrameType_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_FrameType_Object = MibScalar
t1NetworkProfileV1_LineInterface_FrameType = _T1NetworkProfileV1_LineInterface_FrameType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 5),
    _T1NetworkProfileV1_LineInterface_FrameType_Type()
)
t1NetworkProfileV1_LineInterface_FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_FrameType.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_Encoding_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_Encoding based on Integer32"""
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
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3),
          ("none", 4))
    )


_T1NetworkProfileV1_LineInterface_Encoding_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_Encoding_Object = MibScalar
t1NetworkProfileV1_LineInterface_Encoding = _T1NetworkProfileV1_LineInterface_Encoding_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 6),
    _T1NetworkProfileV1_LineInterface_Encoding_Type()
)
t1NetworkProfileV1_LineInterface_Encoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Encoding.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_ClockSource_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_ClockSource based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_ClockSource_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_ClockSource_Object = MibScalar
t1NetworkProfileV1_LineInterface_ClockSource = _T1NetworkProfileV1_LineInterface_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 7),
    _T1NetworkProfileV1_LineInterface_ClockSource_Type()
)
t1NetworkProfileV1_LineInterface_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ClockSource.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_ClockPriority_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_ClockPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 2),
          ("lowPriority", 4),
          ("middlePriority", 3))
    )


_T1NetworkProfileV1_LineInterface_ClockPriority_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_ClockPriority_Object = MibScalar
t1NetworkProfileV1_LineInterface_ClockPriority = _T1NetworkProfileV1_LineInterface_ClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 8),
    _T1NetworkProfileV1_LineInterface_ClockPriority_Type()
)
t1NetworkProfileV1_LineInterface_ClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ClockPriority.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_SignalingMode_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_SignalingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              13,
              14,
              15,
              16,
              17,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("dtmfR2Signaling", 25),
          ("e1ArgentinaSignaling", 13),
          ("e1BrazilSignaling", 14),
          ("e1ChineseSignaling", 8),
          ("e1CzechSignaling", 17),
          ("e1DpnssSignaling", 11),
          ("e1IndianSignaling", 16),
          ("e1IsraelSignaling", 21),
          ("e1KoreanSignaling", 6),
          ("e1KuwaitSignaling", 23),
          ("e1MalaysiaSignaling", 19),
          ("e1MeteredSignaling", 9),
          ("e1MexicoSignaling", 24),
          ("e1NewZealandSignaling", 20),
          ("e1NoSignaling", 10),
          ("e1P7Signaling", 7),
          ("e1PhilippineSignaling", 15),
          ("e1R2Signaling", 5),
          ("e1ThailandSignaling", 22),
          ("e1VietnamSignaling", 32),
          ("h248DataTrunk", 34),
          ("inband", 1),
          ("inbandFgcInFgcOut", 30),
          ("inbandFgcInFgdOut", 31),
          ("inbandFgdInFgcOut", 29),
          ("inbandFgdInFgdOut", 28),
          ("isdn", 2),
          ("isdnNfas", 3),
          ("ss7SigTrunk", 33),
          ("tunneledPriSignaling", 27))
    )


_T1NetworkProfileV1_LineInterface_SignalingMode_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_SignalingMode_Object = MibScalar
t1NetworkProfileV1_LineInterface_SignalingMode = _T1NetworkProfileV1_LineInterface_SignalingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 9),
    _T1NetworkProfileV1_LineInterface_SignalingMode_Type()
)
t1NetworkProfileV1_LineInterface_SignalingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_SignalingMode.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_IsdnEmulationSide_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_IsdnEmulationSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nt", 2),
          ("te", 1))
    )


_T1NetworkProfileV1_LineInterface_IsdnEmulationSide_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_IsdnEmulationSide_Object = MibScalar
t1NetworkProfileV1_LineInterface_IsdnEmulationSide = _T1NetworkProfileV1_LineInterface_IsdnEmulationSide_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 10),
    _T1NetworkProfileV1_LineInterface_IsdnEmulationSide_Type()
)
t1NetworkProfileV1_LineInterface_IsdnEmulationSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_IsdnEmulationSide.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_RobbedBitMode_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_RobbedBitMode based on Integer32"""
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
        *(("groundStart", 6),
          ("idleStart", 2),
          ("incW200", 3),
          ("incW400", 4),
          ("loopStart", 5),
          ("winkStart", 1))
    )


_T1NetworkProfileV1_LineInterface_RobbedBitMode_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_RobbedBitMode_Object = MibScalar
t1NetworkProfileV1_LineInterface_RobbedBitMode = _T1NetworkProfileV1_LineInterface_RobbedBitMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 11),
    _T1NetworkProfileV1_LineInterface_RobbedBitMode_Type()
)
t1NetworkProfileV1_LineInterface_RobbedBitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_RobbedBitMode.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_DefaultCallType_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_DefaultCallType based on Integer32"""
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
        *(("digital", 1),
          ("dnisOrDigital", 4),
          ("dnisOrVoice", 3),
          ("dnisOrVoip", 6),
          ("voice", 2),
          ("voip", 5))
    )


_T1NetworkProfileV1_LineInterface_DefaultCallType_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_DefaultCallType_Object = MibScalar
t1NetworkProfileV1_LineInterface_DefaultCallType = _T1NetworkProfileV1_LineInterface_DefaultCallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 12),
    _T1NetworkProfileV1_LineInterface_DefaultCallType_Type()
)
t1NetworkProfileV1_LineInterface_DefaultCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_DefaultCallType.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_SwitchType_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_SwitchType based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_SwitchType_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_SwitchType_Object = MibScalar
t1NetworkProfileV1_LineInterface_SwitchType = _T1NetworkProfileV1_LineInterface_SwitchType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 13),
    _T1NetworkProfileV1_LineInterface_SwitchType_Type()
)
t1NetworkProfileV1_LineInterface_SwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_SwitchType.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_NfasGroupId_Type = Integer32
_T1NetworkProfileV1_LineInterface_NfasGroupId_Object = MibScalar
t1NetworkProfileV1_LineInterface_NfasGroupId = _T1NetworkProfileV1_LineInterface_NfasGroupId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 14),
    _T1NetworkProfileV1_LineInterface_NfasGroupId_Type()
)
t1NetworkProfileV1_LineInterface_NfasGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_NfasGroupId.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_NfasId_Type = Integer32
_T1NetworkProfileV1_LineInterface_NfasId_Object = MibScalar
t1NetworkProfileV1_LineInterface_NfasId = _T1NetworkProfileV1_LineInterface_NfasId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 15),
    _T1NetworkProfileV1_LineInterface_NfasId_Type()
)
t1NetworkProfileV1_LineInterface_NfasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_NfasId.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_IncomingCallHandling_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_IncomingCallHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalProcessing", 2),
          ("rejectAll", 1),
          ("ss7GatewayProcessing", 3))
    )


_T1NetworkProfileV1_LineInterface_IncomingCallHandling_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_IncomingCallHandling_Object = MibScalar
t1NetworkProfileV1_LineInterface_IncomingCallHandling = _T1NetworkProfileV1_LineInterface_IncomingCallHandling_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 16),
    _T1NetworkProfileV1_LineInterface_IncomingCallHandling_Type()
)
t1NetworkProfileV1_LineInterface_IncomingCallHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_IncomingCallHandling.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_DeleteDigits_Type = Integer32
_T1NetworkProfileV1_LineInterface_DeleteDigits_Object = MibScalar
t1NetworkProfileV1_LineInterface_DeleteDigits = _T1NetworkProfileV1_LineInterface_DeleteDigits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 17),
    _T1NetworkProfileV1_LineInterface_DeleteDigits_Type()
)
t1NetworkProfileV1_LineInterface_DeleteDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_DeleteDigits.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_AddDigitString_Type = DisplayString
_T1NetworkProfileV1_LineInterface_AddDigitString_Object = MibScalar
t1NetworkProfileV1_LineInterface_AddDigitString = _T1NetworkProfileV1_LineInterface_AddDigitString_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 18),
    _T1NetworkProfileV1_LineInterface_AddDigitString_Type()
)
t1NetworkProfileV1_LineInterface_AddDigitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_AddDigitString.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_CallByCall_Type = Integer32
_T1NetworkProfileV1_LineInterface_CallByCall_Object = MibScalar
t1NetworkProfileV1_LineInterface_CallByCall = _T1NetworkProfileV1_LineInterface_CallByCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 19),
    _T1NetworkProfileV1_LineInterface_CallByCall_Type()
)
t1NetworkProfileV1_LineInterface_CallByCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_CallByCall.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_PbxAnswerNumber_Type = DisplayString
_T1NetworkProfileV1_LineInterface_PbxAnswerNumber_Object = MibScalar
t1NetworkProfileV1_LineInterface_PbxAnswerNumber = _T1NetworkProfileV1_LineInterface_PbxAnswerNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 20),
    _T1NetworkProfileV1_LineInterface_PbxAnswerNumber_Type()
)
t1NetworkProfileV1_LineInterface_PbxAnswerNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_PbxAnswerNumber.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_AnswerService_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_AnswerService based on Integer32"""
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
              39,
              40,
              41,
              42,
              43,
              44,
              46,
              47,
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
              255,
              263)
        )
    )
    namedValues = NamedValues(
        *(("atmSvc", 70),
          ("atmodem", 44),
          ("dws384Clear", 14),
          ("frameRelaySvc", 71),
          ("iptoip", 263),
          ("modem", 43),
          ("modem31khzAudio", 82),
          ("n-1024Clear", 24),
          ("n-1088Clear", 25),
          ("n-1152Clear", 26),
          ("n-1216Clear", 27),
          ("n-1280Clear", 28),
          ("n-128kClear", 10),
          ("n-1344Clear", 29),
          ("n-1408Clear", 30),
          ("n-14456kV110", 74),
          ("n-14456krV110", 76),
          ("n-14464kV110", 78),
          ("n-14464krV110", 80),
          ("n-144kClear", 255),
          ("n-1472Clear", 31),
          ("n-1536kClear", 8),
          ("n-1536kRestricted", 9),
          ("n-1600Clear", 32),
          ("n-1664Clear", 33),
          ("n-1728Clear", 34),
          ("n-1792Clear", 35),
          ("n-1856Clear", 36),
          ("n-1920Clear", 37),
          ("n-19256kV110", 49),
          ("n-19256krV110", 54),
          ("n-19264kV110", 59),
          ("n-19264krV110", 64),
          ("n-192kClear", 11),
          ("n-2456kV110", 46),
          ("n-2456krV110", 51),
          ("n-2464kV110", 56),
          ("n-2464krV110", 61),
          ("n-256kClear", 12),
          ("n-28856kV110", 75),
          ("n-28856krV110", 77),
          ("n-28864kV110", 79),
          ("n-28864krV110", 81),
          ("n-320kClear", 13),
          ("n-38456kV110", 50),
          ("n-38456krV110", 55),
          ("n-38464kV110", 60),
          ("n-38464krV110", 65),
          ("n-384kClear", 7),
          ("n-384kRestricted", 6),
          ("n-448Clear", 15),
          ("n-4856kV110", 47),
          ("n-4856krV110", 52),
          ("n-4864kV110", 57),
          ("n-4864krV110", 62),
          ("n-512Clear", 16),
          ("n-56kClear", 5),
          ("n-56kRestricted", 2),
          ("n-56kV110Clear", 42),
          ("n-576Clear", 17),
          ("n-640Clear", 18),
          ("n-64kClear", 3),
          ("n-64kRestricted", 4),
          ("n-64kX30Restricted", 41),
          ("n-704Clear", 19),
          ("n-768Clear", 20),
          ("n-832Clear", 21),
          ("n-896Clear", 22),
          ("n-960Clear", 23),
          ("n-9656kV110", 48),
          ("n-9656krV110", 53),
          ("n-9664kV110", 58),
          ("n-9664krV110", 63),
          ("phs64k", 67),
          ("v110ClearBearer", 40),
          ("v32", 66),
          ("voice", 1),
          ("voiceOverIp", 68),
          ("vpnTunnel", 72),
          ("wormarq", 73),
          ("x25Svc", 83),
          ("x30RestrictedBearer", 39))
    )


_T1NetworkProfileV1_LineInterface_AnswerService_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_AnswerService_Object = MibScalar
t1NetworkProfileV1_LineInterface_AnswerService = _T1NetworkProfileV1_LineInterface_AnswerService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 21),
    _T1NetworkProfileV1_LineInterface_AnswerService_Type()
)
t1NetworkProfileV1_LineInterface_AnswerService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_AnswerService.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_oPBXType_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_oPBXType based on Integer32"""
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
        *(("hostPbxData", 2),
          ("hostPbxLeased11", 4),
          ("hostPbxLeasedData", 3),
          ("hostPbxVoice", 1))
    )


_T1NetworkProfileV1_LineInterface_oPBXType_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_oPBXType_Object = MibScalar
t1NetworkProfileV1_LineInterface_oPBXType = _T1NetworkProfileV1_LineInterface_oPBXType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 22),
    _T1NetworkProfileV1_LineInterface_oPBXType_Type()
)
t1NetworkProfileV1_LineInterface_oPBXType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_oPBXType.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_DataSense_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_DataSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inv", 2),
          ("normal", 1))
    )


_T1NetworkProfileV1_LineInterface_DataSense_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_DataSense_Object = MibScalar
t1NetworkProfileV1_LineInterface_DataSense = _T1NetworkProfileV1_LineInterface_DataSense_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 23),
    _T1NetworkProfileV1_LineInterface_DataSense_Type()
)
t1NetworkProfileV1_LineInterface_DataSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_DataSense.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_IdleMode_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_IdleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flagIdle", 2),
          ("markIdle", 1))
    )


_T1NetworkProfileV1_LineInterface_IdleMode_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_IdleMode_Object = MibScalar
t1NetworkProfileV1_LineInterface_IdleMode = _T1NetworkProfileV1_LineInterface_IdleMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 24),
    _T1NetworkProfileV1_LineInterface_IdleMode_Type()
)
t1NetworkProfileV1_LineInterface_IdleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_IdleMode.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_oFDL_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_oFDL based on Integer32"""
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
        *(("ansi", 3),
          ("atNT", 2),
          ("none", 1),
          ("sprint", 4))
    )


_T1NetworkProfileV1_LineInterface_oFDL_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_oFDL_Object = MibScalar
t1NetworkProfileV1_LineInterface_oFDL = _T1NetworkProfileV1_LineInterface_oFDL_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 25),
    _T1NetworkProfileV1_LineInterface_oFDL_Type()
)
t1NetworkProfileV1_LineInterface_oFDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_oFDL.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_FrontEndType_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_FrontEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csu", 1),
          ("dsx", 2))
    )


_T1NetworkProfileV1_LineInterface_FrontEndType_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_FrontEndType_Object = MibScalar
t1NetworkProfileV1_LineInterface_FrontEndType = _T1NetworkProfileV1_LineInterface_FrontEndType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 26),
    _T1NetworkProfileV1_LineInterface_FrontEndType_Type()
)
t1NetworkProfileV1_LineInterface_FrontEndType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_FrontEndType.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_oDSXLineLength_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_oDSXLineLength based on Integer32"""
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
        *(("n-1133", 1),
          ("n-134266", 2),
          ("n-267399", 3),
          ("n-400533", 4),
          ("n-534655", 5))
    )


_T1NetworkProfileV1_LineInterface_oDSXLineLength_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_oDSXLineLength_Object = MibScalar
t1NetworkProfileV1_LineInterface_oDSXLineLength = _T1NetworkProfileV1_LineInterface_oDSXLineLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 27),
    _T1NetworkProfileV1_LineInterface_oDSXLineLength_Type()
)
t1NetworkProfileV1_LineInterface_oDSXLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_oDSXLineLength.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_oCSUBuildOut_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_oCSUBuildOut based on Integer32"""
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
        *(("n-0Db", 1),
          ("n-15Db", 3),
          ("n-2255Db", 4),
          ("n-75Db", 2))
    )


_T1NetworkProfileV1_LineInterface_oCSUBuildOut_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_oCSUBuildOut_Object = MibScalar
t1NetworkProfileV1_LineInterface_oCSUBuildOut = _T1NetworkProfileV1_LineInterface_oCSUBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 28),
    _T1NetworkProfileV1_LineInterface_oCSUBuildOut_Type()
)
t1NetworkProfileV1_LineInterface_oCSUBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_oCSUBuildOut.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_OverlapReceiving_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_OverlapReceiving based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_OverlapReceiving_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_OverlapReceiving_Object = MibScalar
t1NetworkProfileV1_LineInterface_OverlapReceiving = _T1NetworkProfileV1_LineInterface_OverlapReceiving_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 29),
    _T1NetworkProfileV1_LineInterface_OverlapReceiving_Type()
)
t1NetworkProfileV1_LineInterface_OverlapReceiving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_OverlapReceiving.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_PriPrefixNumber_Type = DisplayString
_T1NetworkProfileV1_LineInterface_PriPrefixNumber_Object = MibScalar
t1NetworkProfileV1_LineInterface_PriPrefixNumber = _T1NetworkProfileV1_LineInterface_PriPrefixNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 30),
    _T1NetworkProfileV1_LineInterface_PriPrefixNumber_Type()
)
t1NetworkProfileV1_LineInterface_PriPrefixNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_PriPrefixNumber.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_TrailingDigits_Type = Integer32
_T1NetworkProfileV1_LineInterface_TrailingDigits_Object = MibScalar
t1NetworkProfileV1_LineInterface_TrailingDigits = _T1NetworkProfileV1_LineInterface_TrailingDigits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 31),
    _T1NetworkProfileV1_LineInterface_TrailingDigits_Type()
)
t1NetworkProfileV1_LineInterface_TrailingDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_TrailingDigits.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_T302Timer_Type = Integer32
_T1NetworkProfileV1_LineInterface_T302Timer_Object = MibScalar
t1NetworkProfileV1_LineInterface_T302Timer = _T1NetworkProfileV1_LineInterface_T302Timer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 32),
    _T1NetworkProfileV1_LineInterface_T302Timer_Type()
)
t1NetworkProfileV1_LineInterface_T302Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_T302Timer.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_Layer3End_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_Layer3End based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_T1NetworkProfileV1_LineInterface_Layer3End_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_Layer3End_Object = MibScalar
t1NetworkProfileV1_LineInterface_Layer3End = _T1NetworkProfileV1_LineInterface_Layer3End_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 33),
    _T1NetworkProfileV1_LineInterface_Layer3End_Type()
)
t1NetworkProfileV1_LineInterface_Layer3End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Layer3End.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_Layer2End_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_Layer2End based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_T1NetworkProfileV1_LineInterface_Layer2End_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_Layer2End_Object = MibScalar
t1NetworkProfileV1_LineInterface_Layer2End = _T1NetworkProfileV1_LineInterface_Layer2End_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 34),
    _T1NetworkProfileV1_LineInterface_Layer2End_Type()
)
t1NetworkProfileV1_LineInterface_Layer2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Layer2End.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_NlValue_Type = Integer32
_T1NetworkProfileV1_LineInterface_NlValue_Object = MibScalar
t1NetworkProfileV1_LineInterface_NlValue = _T1NetworkProfileV1_LineInterface_NlValue_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 35),
    _T1NetworkProfileV1_LineInterface_NlValue_Type()
)
t1NetworkProfileV1_LineInterface_NlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_NlValue.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_LoopAvoidance_Type = Integer32
_T1NetworkProfileV1_LineInterface_LoopAvoidance_Object = MibScalar
t1NetworkProfileV1_LineInterface_LoopAvoidance = _T1NetworkProfileV1_LineInterface_LoopAvoidance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 36),
    _T1NetworkProfileV1_LineInterface_LoopAvoidance_Type()
)
t1NetworkProfileV1_LineInterface_LoopAvoidance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_LoopAvoidance.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_MaintenanceState_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_MaintenanceState based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_MaintenanceState_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_MaintenanceState_Object = MibScalar
t1NetworkProfileV1_LineInterface_MaintenanceState = _T1NetworkProfileV1_LineInterface_MaintenanceState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 37),
    _T1NetworkProfileV1_LineInterface_MaintenanceState_Type()
)
t1NetworkProfileV1_LineInterface_MaintenanceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_MaintenanceState.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_NumberComplete_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_NumberComplete based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("endOfPulsing", 11),
          ("n-0Digits", 12),
          ("n-10Digits", 10),
          ("n-11Digits", 13),
          ("n-12Digits", 14),
          ("n-13Digits", 15),
          ("n-14Digits", 16),
          ("n-15Digits", 17),
          ("n-1Digits", 1),
          ("n-2Digits", 2),
          ("n-3Digits", 3),
          ("n-4Digits", 4),
          ("n-5Digits", 5),
          ("n-6Digits", 6),
          ("n-7Digits", 7),
          ("n-8Digits", 8),
          ("n-9Digits", 9),
          ("timeOut", 18))
    )


_T1NetworkProfileV1_LineInterface_NumberComplete_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_NumberComplete_Object = MibScalar
t1NetworkProfileV1_LineInterface_NumberComplete = _T1NetworkProfileV1_LineInterface_NumberComplete_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 38),
    _T1NetworkProfileV1_LineInterface_NumberComplete_Type()
)
t1NetworkProfileV1_LineInterface_NumberComplete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_NumberComplete.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_GroupBAnswerSignal_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_GroupBAnswerSignal based on Integer32"""
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
        *(("signalB1", 1),
          ("signalB10", 10),
          ("signalB11", 11),
          ("signalB12", 12),
          ("signalB13", 13),
          ("signalB14", 14),
          ("signalB15", 15),
          ("signalB2", 2),
          ("signalB3", 3),
          ("signalB4", 4),
          ("signalB5", 5),
          ("signalB6", 6),
          ("signalB7", 7),
          ("signalB8", 8),
          ("signalB9", 9))
    )


_T1NetworkProfileV1_LineInterface_GroupBAnswerSignal_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_GroupBAnswerSignal_Object = MibScalar
t1NetworkProfileV1_LineInterface_GroupBAnswerSignal = _T1NetworkProfileV1_LineInterface_GroupBAnswerSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 39),
    _T1NetworkProfileV1_LineInterface_GroupBAnswerSignal_Type()
)
t1NetworkProfileV1_LineInterface_GroupBAnswerSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_GroupBAnswerSignal.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_GroupBBusySignal_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_GroupBBusySignal based on Integer32"""
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
        *(("signalB1", 1),
          ("signalB10", 10),
          ("signalB11", 11),
          ("signalB12", 12),
          ("signalB13", 13),
          ("signalB14", 14),
          ("signalB15", 15),
          ("signalB2", 2),
          ("signalB3", 3),
          ("signalB4", 4),
          ("signalB5", 5),
          ("signalB6", 6),
          ("signalB7", 7),
          ("signalB8", 8),
          ("signalB9", 9))
    )


_T1NetworkProfileV1_LineInterface_GroupBBusySignal_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_GroupBBusySignal_Object = MibScalar
t1NetworkProfileV1_LineInterface_GroupBBusySignal = _T1NetworkProfileV1_LineInterface_GroupBBusySignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 40),
    _T1NetworkProfileV1_LineInterface_GroupBBusySignal_Type()
)
t1NetworkProfileV1_LineInterface_GroupBBusySignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_GroupBBusySignal.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_GroupBNoMatchSignal_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_GroupBNoMatchSignal based on Integer32"""
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
        *(("signalB1", 1),
          ("signalB10", 10),
          ("signalB11", 11),
          ("signalB12", 12),
          ("signalB13", 13),
          ("signalB14", 14),
          ("signalB15", 15),
          ("signalB2", 2),
          ("signalB3", 3),
          ("signalB4", 4),
          ("signalB5", 5),
          ("signalB6", 6),
          ("signalB7", 7),
          ("signalB8", 8),
          ("signalB9", 9))
    )


_T1NetworkProfileV1_LineInterface_GroupBNoMatchSignal_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_GroupBNoMatchSignal_Object = MibScalar
t1NetworkProfileV1_LineInterface_GroupBNoMatchSignal = _T1NetworkProfileV1_LineInterface_GroupBNoMatchSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 41),
    _T1NetworkProfileV1_LineInterface_GroupBNoMatchSignal_Type()
)
t1NetworkProfileV1_LineInterface_GroupBNoMatchSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_GroupBNoMatchSignal.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_GroupBCollectSignal_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_GroupBCollectSignal based on Integer32"""
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
        *(("signalB1", 1),
          ("signalB10", 10),
          ("signalB11", 11),
          ("signalB12", 12),
          ("signalB13", 13),
          ("signalB14", 14),
          ("signalB15", 15),
          ("signalB2", 2),
          ("signalB3", 3),
          ("signalB4", 4),
          ("signalB5", 5),
          ("signalB6", 6),
          ("signalB7", 7),
          ("signalB8", 8),
          ("signalB9", 9))
    )


_T1NetworkProfileV1_LineInterface_GroupBCollectSignal_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_GroupBCollectSignal_Object = MibScalar
t1NetworkProfileV1_LineInterface_GroupBCollectSignal = _T1NetworkProfileV1_LineInterface_GroupBCollectSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 42),
    _T1NetworkProfileV1_LineInterface_GroupBCollectSignal_Type()
)
t1NetworkProfileV1_LineInterface_GroupBCollectSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_GroupBCollectSignal.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_GroupIiSignal_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_GroupIiSignal based on Integer32"""
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
        *(("signalIi1", 1),
          ("signalIi10", 10),
          ("signalIi11", 11),
          ("signalIi12", 12),
          ("signalIi13", 13),
          ("signalIi14", 14),
          ("signalIi15", 15),
          ("signalIi2", 2),
          ("signalIi3", 3),
          ("signalIi4", 4),
          ("signalIi5", 5),
          ("signalIi6", 6),
          ("signalIi7", 7),
          ("signalIi8", 8),
          ("signalIi9", 9))
    )


_T1NetworkProfileV1_LineInterface_GroupIiSignal_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_GroupIiSignal_Object = MibScalar
t1NetworkProfileV1_LineInterface_GroupIiSignal = _T1NetworkProfileV1_LineInterface_GroupIiSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 43),
    _T1NetworkProfileV1_LineInterface_GroupIiSignal_Type()
)
t1NetworkProfileV1_LineInterface_GroupIiSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_GroupIiSignal.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_InputSampleCount_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_InputSampleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneSample", 1),
          ("twoSamples", 2))
    )


_T1NetworkProfileV1_LineInterface_InputSampleCount_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_InputSampleCount_Object = MibScalar
t1NetworkProfileV1_LineInterface_InputSampleCount = _T1NetworkProfileV1_LineInterface_InputSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 44),
    _T1NetworkProfileV1_LineInterface_InputSampleCount_Type()
)
t1NetworkProfileV1_LineInterface_InputSampleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_InputSampleCount.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_AnswerDelay_Type = Integer32
_T1NetworkProfileV1_LineInterface_AnswerDelay_Object = MibScalar
t1NetworkProfileV1_LineInterface_AnswerDelay = _T1NetworkProfileV1_LineInterface_AnswerDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 45),
    _T1NetworkProfileV1_LineInterface_AnswerDelay_Type()
)
t1NetworkProfileV1_LineInterface_AnswerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_AnswerDelay.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_CallerId_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_CallerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("getCallerId", 2),
          ("noCallerId", 1))
    )


_T1NetworkProfileV1_LineInterface_CallerId_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_CallerId_Object = MibScalar
t1NetworkProfileV1_LineInterface_CallerId = _T1NetworkProfileV1_LineInterface_CallerId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 46),
    _T1NetworkProfileV1_LineInterface_CallerId_Type()
)
t1NetworkProfileV1_LineInterface_CallerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_CallerId.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_LineSignaling_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_LineSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aBitOnly0EqualBBit", 2),
          ("aBitOnly1EqualBBit", 3),
          ("abBitsLineSignaling", 1))
    )


_T1NetworkProfileV1_LineInterface_LineSignaling_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_LineSignaling_Object = MibScalar
t1NetworkProfileV1_LineInterface_LineSignaling = _T1NetworkProfileV1_LineInterface_LineSignaling_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 47),
    _T1NetworkProfileV1_LineInterface_LineSignaling_Type()
)
t1NetworkProfileV1_LineInterface_LineSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_LineSignaling.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_Timer1CollectCall_Type = Integer32
_T1NetworkProfileV1_LineInterface_Timer1CollectCall_Object = MibScalar
t1NetworkProfileV1_LineInterface_Timer1CollectCall = _T1NetworkProfileV1_LineInterface_Timer1CollectCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 48),
    _T1NetworkProfileV1_LineInterface_Timer1CollectCall_Type()
)
t1NetworkProfileV1_LineInterface_Timer1CollectCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Timer1CollectCall.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_Timer2CollectCall_Type = Integer32
_T1NetworkProfileV1_LineInterface_Timer2CollectCall_Object = MibScalar
t1NetworkProfileV1_LineInterface_Timer2CollectCall = _T1NetworkProfileV1_LineInterface_Timer2CollectCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 49),
    _T1NetworkProfileV1_LineInterface_Timer2CollectCall_Type()
)
t1NetworkProfileV1_LineInterface_Timer2CollectCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Timer2CollectCall.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_SendDiscVal_Type = Integer32
_T1NetworkProfileV1_LineInterface_SendDiscVal_Object = MibScalar
t1NetworkProfileV1_LineInterface_SendDiscVal = _T1NetworkProfileV1_LineInterface_SendDiscVal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 50),
    _T1NetworkProfileV1_LineInterface_SendDiscVal_Type()
)
t1NetworkProfileV1_LineInterface_SendDiscVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_SendDiscVal.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber1_Type = DisplayString
_T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber1_Object = MibScalar
t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber1 = _T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 51),
    _T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber1_Type()
)
t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber1.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber2_Type = DisplayString
_T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber2_Object = MibScalar
t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber2 = _T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 52),
    _T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber2_Type()
)
t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber2.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber3_Type = DisplayString
_T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber3_Object = MibScalar
t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber3 = _T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 53),
    _T1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber3_Type()
)
t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber3.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_PriTypeOfNumber_Type = Integer32
_T1NetworkProfileV1_LineInterface_PriTypeOfNumber_Object = MibScalar
t1NetworkProfileV1_LineInterface_PriTypeOfNumber = _T1NetworkProfileV1_LineInterface_PriTypeOfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 54),
    _T1NetworkProfileV1_LineInterface_PriTypeOfNumber_Type()
)
t1NetworkProfileV1_LineInterface_PriTypeOfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_PriTypeOfNumber.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_PriNumberingPlanId_Type = Integer32
_T1NetworkProfileV1_LineInterface_PriNumberingPlanId_Object = MibScalar
t1NetworkProfileV1_LineInterface_PriNumberingPlanId = _T1NetworkProfileV1_LineInterface_PriNumberingPlanId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 55),
    _T1NetworkProfileV1_LineInterface_PriNumberingPlanId_Type()
)
t1NetworkProfileV1_LineInterface_PriNumberingPlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_PriNumberingPlanId.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_SuperFrameSrcLineNumber_Type = Integer32
_T1NetworkProfileV1_LineInterface_SuperFrameSrcLineNumber_Object = MibScalar
t1NetworkProfileV1_LineInterface_SuperFrameSrcLineNumber = _T1NetworkProfileV1_LineInterface_SuperFrameSrcLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 56),
    _T1NetworkProfileV1_LineInterface_SuperFrameSrcLineNumber_Type()
)
t1NetworkProfileV1_LineInterface_SuperFrameSrcLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_SuperFrameSrcLineNumber.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_CollectIncomingDigits_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_CollectIncomingDigits based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_CollectIncomingDigits_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_CollectIncomingDigits_Object = MibScalar
t1NetworkProfileV1_LineInterface_CollectIncomingDigits = _T1NetworkProfileV1_LineInterface_CollectIncomingDigits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 57),
    _T1NetworkProfileV1_LineInterface_CollectIncomingDigits_Type()
)
t1NetworkProfileV1_LineInterface_CollectIncomingDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_CollectIncomingDigits.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_T1InterDigitTimeout_Type = Integer32
_T1NetworkProfileV1_LineInterface_T1InterDigitTimeout_Object = MibScalar
t1NetworkProfileV1_LineInterface_T1InterDigitTimeout = _T1NetworkProfileV1_LineInterface_T1InterDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 58),
    _T1NetworkProfileV1_LineInterface_T1InterDigitTimeout_Type()
)
t1NetworkProfileV1_LineInterface_T1InterDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_T1InterDigitTimeout.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_R1UseAnir_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_R1UseAnir based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_R1UseAnir_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_R1UseAnir_Object = MibScalar
t1NetworkProfileV1_LineInterface_R1UseAnir = _T1NetworkProfileV1_LineInterface_R1UseAnir_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 59),
    _T1NetworkProfileV1_LineInterface_R1UseAnir_Type()
)
t1NetworkProfileV1_LineInterface_R1UseAnir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_R1UseAnir.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_R1FirstDigitTimer_Type = Integer32
_T1NetworkProfileV1_LineInterface_R1FirstDigitTimer_Object = MibScalar
t1NetworkProfileV1_LineInterface_R1FirstDigitTimer = _T1NetworkProfileV1_LineInterface_R1FirstDigitTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 60),
    _T1NetworkProfileV1_LineInterface_R1FirstDigitTimer_Type()
)
t1NetworkProfileV1_LineInterface_R1FirstDigitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_R1FirstDigitTimer.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_R1AnirDelay_Type = Integer32
_T1NetworkProfileV1_LineInterface_R1AnirDelay_Object = MibScalar
t1NetworkProfileV1_LineInterface_R1AnirDelay = _T1NetworkProfileV1_LineInterface_R1AnirDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 61),
    _T1NetworkProfileV1_LineInterface_R1AnirDelay_Type()
)
t1NetworkProfileV1_LineInterface_R1AnirDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_R1AnirDelay.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_R1AnirTimer_Type = Integer32
_T1NetworkProfileV1_LineInterface_R1AnirTimer_Object = MibScalar
t1NetworkProfileV1_LineInterface_R1AnirTimer = _T1NetworkProfileV1_LineInterface_R1AnirTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 62),
    _T1NetworkProfileV1_LineInterface_R1AnirTimer_Type()
)
t1NetworkProfileV1_LineInterface_R1AnirTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_R1AnirTimer.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_R1Modified_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_R1Modified based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_R1Modified_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_R1Modified_Object = MibScalar
t1NetworkProfileV1_LineInterface_R1Modified = _T1NetworkProfileV1_LineInterface_R1Modified_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 63),
    _T1NetworkProfileV1_LineInterface_R1Modified_Type()
)
t1NetworkProfileV1_LineInterface_R1Modified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_R1Modified.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_FirstDs0_Type = Integer32
_T1NetworkProfileV1_LineInterface_FirstDs0_Object = MibScalar
t1NetworkProfileV1_LineInterface_FirstDs0 = _T1NetworkProfileV1_LineInterface_FirstDs0_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 64),
    _T1NetworkProfileV1_LineInterface_FirstDs0_Type()
)
t1NetworkProfileV1_LineInterface_FirstDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_FirstDs0.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_LastDs0_Type = Integer32
_T1NetworkProfileV1_LineInterface_LastDs0_Object = MibScalar
t1NetworkProfileV1_LineInterface_LastDs0 = _T1NetworkProfileV1_LineInterface_LastDs0_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 65),
    _T1NetworkProfileV1_LineInterface_LastDs0_Type()
)
t1NetworkProfileV1_LineInterface_LastDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_LastDs0.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_NailedGroup_Type = Integer32
_T1NetworkProfileV1_LineInterface_NailedGroup_Object = MibScalar
t1NetworkProfileV1_LineInterface_NailedGroup = _T1NetworkProfileV1_LineInterface_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 66),
    _T1NetworkProfileV1_LineInterface_NailedGroup_Type()
)
t1NetworkProfileV1_LineInterface_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_NailedGroup.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_Ss7Continuity_IncomingProcedure_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_Ss7Continuity_IncomingProcedure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 2),
          ("transponder", 3))
    )


_T1NetworkProfileV1_LineInterface_Ss7Continuity_IncomingProcedure_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_Ss7Continuity_IncomingProcedure_Object = MibScalar
t1NetworkProfileV1_LineInterface_Ss7Continuity_IncomingProcedure = _T1NetworkProfileV1_LineInterface_Ss7Continuity_IncomingProcedure_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 67),
    _T1NetworkProfileV1_LineInterface_Ss7Continuity_IncomingProcedure_Type()
)
t1NetworkProfileV1_LineInterface_Ss7Continuity_IncomingProcedure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Ss7Continuity_IncomingProcedure.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_Ss7Continuity_OutgoingProcedure_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_Ss7Continuity_OutgoingProcedure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("send1780Expect2000", 7),
          ("send1780Expect2010", 4),
          ("send2000Expect1780", 6),
          ("send2010Expect1780", 3),
          ("singleTone2000", 5),
          ("singleTone2010", 2))
    )


_T1NetworkProfileV1_LineInterface_Ss7Continuity_OutgoingProcedure_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_Ss7Continuity_OutgoingProcedure_Object = MibScalar
t1NetworkProfileV1_LineInterface_Ss7Continuity_OutgoingProcedure = _T1NetworkProfileV1_LineInterface_Ss7Continuity_OutgoingProcedure_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 68),
    _T1NetworkProfileV1_LineInterface_Ss7Continuity_OutgoingProcedure_Type()
)
t1NetworkProfileV1_LineInterface_Ss7Continuity_OutgoingProcedure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Ss7Continuity_OutgoingProcedure.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_LineProvision_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_LineProvision based on Integer32"""
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
        *(("lineProvisionH0", 2),
          ("lineProvisionH0H11", 4),
          ("lineProvisionH0H11H12", 8),
          ("lineProvisionH0H12", 6),
          ("lineProvisionH11", 3),
          ("lineProvisionH11H12", 7),
          ("lineProvisionH12", 5),
          ("lineProvisionNone", 1))
    )


_T1NetworkProfileV1_LineInterface_LineProvision_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_LineProvision_Object = MibScalar
t1NetworkProfileV1_LineInterface_LineProvision = _T1NetworkProfileV1_LineInterface_LineProvision_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 69),
    _T1NetworkProfileV1_LineInterface_LineProvision_Type()
)
t1NetworkProfileV1_LineInterface_LineProvision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_LineProvision.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_Gr303Mode_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_Gr303Mode based on Integer32"""
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
        *(("gr3035essPri", 2),
          ("gr303Disabled", 1),
          ("gr303DmsPri", 3),
          ("gr303Normal", 5),
          ("gr303Secondary", 4))
    )


_T1NetworkProfileV1_LineInterface_Gr303Mode_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_Gr303Mode_Object = MibScalar
t1NetworkProfileV1_LineInterface_Gr303Mode = _T1NetworkProfileV1_LineInterface_Gr303Mode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 70),
    _T1NetworkProfileV1_LineInterface_Gr303Mode_Type()
)
t1NetworkProfileV1_LineInterface_Gr303Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Gr303Mode.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_Gr303GroupId_Type = Integer32
_T1NetworkProfileV1_LineInterface_Gr303GroupId_Object = MibScalar
t1NetworkProfileV1_LineInterface_Gr303GroupId = _T1NetworkProfileV1_LineInterface_Gr303GroupId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 71),
    _T1NetworkProfileV1_LineInterface_Gr303GroupId_Type()
)
t1NetworkProfileV1_LineInterface_Gr303GroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Gr303GroupId.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_Gr303Ds1Id_Type = Integer32
_T1NetworkProfileV1_LineInterface_Gr303Ds1Id_Object = MibScalar
t1NetworkProfileV1_LineInterface_Gr303Ds1Id = _T1NetworkProfileV1_LineInterface_Gr303Ds1Id_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 72),
    _T1NetworkProfileV1_LineInterface_Gr303Ds1Id_Type()
)
t1NetworkProfileV1_LineInterface_Gr303Ds1Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_Gr303Ds1Id.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_SwitchVersion_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_SwitchVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchVersionDefinityG3v4", 2),
          ("switchVersionGeneric", 1))
    )


_T1NetworkProfileV1_LineInterface_SwitchVersion_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_SwitchVersion_Object = MibScalar
t1NetworkProfileV1_LineInterface_SwitchVersion = _T1NetworkProfileV1_LineInterface_SwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 73),
    _T1NetworkProfileV1_LineInterface_SwitchVersion_Type()
)
t1NetworkProfileV1_LineInterface_SwitchVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_SwitchVersion.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_GroupBNoChargeSignal_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_GroupBNoChargeSignal based on Integer32"""
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
        *(("signalB1", 1),
          ("signalB10", 10),
          ("signalB11", 11),
          ("signalB12", 12),
          ("signalB13", 13),
          ("signalB14", 14),
          ("signalB15", 15),
          ("signalB2", 2),
          ("signalB3", 3),
          ("signalB4", 4),
          ("signalB5", 5),
          ("signalB6", 6),
          ("signalB7", 7),
          ("signalB8", 8),
          ("signalB9", 9))
    )


_T1NetworkProfileV1_LineInterface_GroupBNoChargeSignal_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_GroupBNoChargeSignal_Object = MibScalar
t1NetworkProfileV1_LineInterface_GroupBNoChargeSignal = _T1NetworkProfileV1_LineInterface_GroupBNoChargeSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 74),
    _T1NetworkProfileV1_LineInterface_GroupBNoChargeSignal_Type()
)
t1NetworkProfileV1_LineInterface_GroupBNoChargeSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_GroupBNoChargeSignal.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_StatusChangeTrapEnable_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_StatusChangeTrapEnable based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_StatusChangeTrapEnable_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_StatusChangeTrapEnable_Object = MibScalar
t1NetworkProfileV1_LineInterface_StatusChangeTrapEnable = _T1NetworkProfileV1_LineInterface_StatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 75),
    _T1NetworkProfileV1_LineInterface_StatusChangeTrapEnable_Type()
)
t1NetworkProfileV1_LineInterface_StatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_StatusChangeTrapEnable.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_DownTransDelay_Type = Integer32
_T1NetworkProfileV1_LineInterface_DownTransDelay_Object = MibScalar
t1NetworkProfileV1_LineInterface_DownTransDelay = _T1NetworkProfileV1_LineInterface_DownTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 76),
    _T1NetworkProfileV1_LineInterface_DownTransDelay_Type()
)
t1NetworkProfileV1_LineInterface_DownTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_DownTransDelay.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_UpTransDelay_Type = Integer32
_T1NetworkProfileV1_LineInterface_UpTransDelay_Object = MibScalar
t1NetworkProfileV1_LineInterface_UpTransDelay = _T1NetworkProfileV1_LineInterface_UpTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 77),
    _T1NetworkProfileV1_LineInterface_UpTransDelay_Type()
)
t1NetworkProfileV1_LineInterface_UpTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_UpTransDelay.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_NetworkSpecificFacilities_Type = Integer32
_T1NetworkProfileV1_LineInterface_NetworkSpecificFacilities_Object = MibScalar
t1NetworkProfileV1_LineInterface_NetworkSpecificFacilities = _T1NetworkProfileV1_LineInterface_NetworkSpecificFacilities_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 79),
    _T1NetworkProfileV1_LineInterface_NetworkSpecificFacilities_Type()
)
t1NetworkProfileV1_LineInterface_NetworkSpecificFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_NetworkSpecificFacilities.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_CauseCodeVerificationEnable_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_CauseCodeVerificationEnable based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_CauseCodeVerificationEnable_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_CauseCodeVerificationEnable_Object = MibScalar
t1NetworkProfileV1_LineInterface_CauseCodeVerificationEnable = _T1NetworkProfileV1_LineInterface_CauseCodeVerificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 2, 1, 80),
    _T1NetworkProfileV1_LineInterface_CauseCodeVerificationEnable_Type()
)
t1NetworkProfileV1_LineInterface_CauseCodeVerificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_CauseCodeVerificationEnable.setStatus("mandatory")
_Mibt1NetworkProfileV1_LineInterface_ChannelConfigTable_Object = MibTable
mibt1NetworkProfileV1_LineInterface_ChannelConfigTable = _Mibt1NetworkProfileV1_LineInterface_ChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3)
)
if mibBuilder.loadTexts:
    mibt1NetworkProfileV1_LineInterface_ChannelConfigTable.setStatus("mandatory")
_Mibt1NetworkProfileV1_LineInterface_ChannelConfigEntry_Object = MibTableRow
mibt1NetworkProfileV1_LineInterface_ChannelConfigEntry = _Mibt1NetworkProfileV1_LineInterface_ChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1)
)
mibt1NetworkProfileV1_LineInterface_ChannelConfigEntry.setIndexNames(
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfileV1-LineInterface-ChannelConfig-Name"),
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfileV1-LineInterface-ChannelConfig-Index-o"),
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfileV1-LineInterface-ChannelConfig-Index1-o"),
)
if mibBuilder.loadTexts:
    mibt1NetworkProfileV1_LineInterface_ChannelConfigEntry.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_Name_Type = DisplayString
_T1NetworkProfileV1_LineInterface_ChannelConfig_Name_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_Name = _T1NetworkProfileV1_LineInterface_ChannelConfig_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 1),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_Name_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_Name.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_Index_o_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_Index_o_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_Index_o = _T1NetworkProfileV1_LineInterface_ChannelConfig_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 2),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_Index_o_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_Index_o.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_Index1_o_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_Index1_o_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_Index1_o = _T1NetworkProfileV1_LineInterface_ChannelConfig_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 3),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_Index1_o_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_Index1_o.setStatus("mandatory")


class _T1NetworkProfileV1_LineInterface_ChannelConfig_ChannelUsage_Type(Integer32):
    """Custom type t1NetworkProfileV1_LineInterface_ChannelConfig_ChannelUsage based on Integer32"""
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


_T1NetworkProfileV1_LineInterface_ChannelConfig_ChannelUsage_Type.__name__ = "Integer32"
_T1NetworkProfileV1_LineInterface_ChannelConfig_ChannelUsage_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_ChannelUsage = _T1NetworkProfileV1_LineInterface_ChannelConfig_ChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 4),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_ChannelUsage_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_ChannelUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_ChannelUsage.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_TrunkGroup_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_TrunkGroup_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_TrunkGroup = _T1NetworkProfileV1_LineInterface_ChannelConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 5),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_TrunkGroup_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_TrunkGroup.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_PhoneNumber_Type = DisplayString
_T1NetworkProfileV1_LineInterface_ChannelConfig_PhoneNumber_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_PhoneNumber = _T1NetworkProfileV1_LineInterface_ChannelConfig_PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 6),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_PhoneNumber_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_PhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_PhoneNumber.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber = _T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 7),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber = _T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 8),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber = _T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 9),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_NailedGroup_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_NailedGroup_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_NailedGroup = _T1NetworkProfileV1_LineInterface_ChannelConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 13),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_NailedGroup_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_NailedGroup.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_ChanGroup_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_ChanGroup_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_ChanGroup = _T1NetworkProfileV1_LineInterface_ChannelConfig_ChanGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 14),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_ChanGroup_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_ChanGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_ChanGroup.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_DestChanGroup_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_DestChanGroup_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_DestChanGroup = _T1NetworkProfileV1_LineInterface_ChannelConfig_DestChanGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 15),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_DestChanGroup_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_DestChanGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_DestChanGroup.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_DialPlanNumber_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_DialPlanNumber_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_DialPlanNumber = _T1NetworkProfileV1_LineInterface_ChannelConfig_DialPlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 16),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_DialPlanNumber_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_DialPlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_DialPlanNumber.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits = _T1NetworkProfileV1_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 17),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits.setStatus("mandatory")
_T1NetworkProfileV1_LineInterface_ChannelConfig_IdlePattern_Type = Integer32
_T1NetworkProfileV1_LineInterface_ChannelConfig_IdlePattern_Object = MibScalar
t1NetworkProfileV1_LineInterface_ChannelConfig_IdlePattern = _T1NetworkProfileV1_LineInterface_ChannelConfig_IdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 126, 3, 1, 18),
    _T1NetworkProfileV1_LineInterface_ChannelConfig_IdlePattern_Type()
)
t1NetworkProfileV1_LineInterface_ChannelConfig_IdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfileV1_LineInterface_ChannelConfig_IdlePattern.setStatus("mandatory")
_Mibt1NetworkProfile_ObjectIdentity = ObjectIdentity
mibt1NetworkProfile = _Mibt1NetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 127)
)
_Mibt1NetworkProfileTable_Object = MibTable
mibt1NetworkProfileTable = _Mibt1NetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1)
)
if mibBuilder.loadTexts:
    mibt1NetworkProfileTable.setStatus("mandatory")
_Mibt1NetworkProfileEntry_Object = MibTableRow
mibt1NetworkProfileEntry = _Mibt1NetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1)
)
mibt1NetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfile-Slot-o"),
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibt1NetworkProfileEntry.setStatus("mandatory")
_T1NetworkProfile_Shelf_o_Type = Integer32
_T1NetworkProfile_Shelf_o_Object = MibScalar
t1NetworkProfile_Shelf_o = _T1NetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 1),
    _T1NetworkProfile_Shelf_o_Type()
)
t1NetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfile_Shelf_o.setStatus("mandatory")
_T1NetworkProfile_Slot_o_Type = Integer32
_T1NetworkProfile_Slot_o_Object = MibScalar
t1NetworkProfile_Slot_o = _T1NetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 2),
    _T1NetworkProfile_Slot_o_Type()
)
t1NetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfile_Slot_o.setStatus("mandatory")
_T1NetworkProfile_Item_o_Type = Integer32
_T1NetworkProfile_Item_o_Object = MibScalar
t1NetworkProfile_Item_o = _T1NetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 3),
    _T1NetworkProfile_Item_o_Type()
)
t1NetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfile_Item_o.setStatus("mandatory")
_T1NetworkProfile_Name_Type = DisplayString
_T1NetworkProfile_Name_Object = MibScalar
t1NetworkProfile_Name = _T1NetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 4),
    _T1NetworkProfile_Name_Type()
)
t1NetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_Name.setStatus("mandatory")


class _T1NetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type t1NetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_T1NetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_T1NetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
t1NetworkProfile_PhysicalAddress_Shelf = _T1NetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 5),
    _T1NetworkProfile_PhysicalAddress_Shelf_Type()
)
t1NetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _T1NetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type t1NetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_T1NetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_T1NetworkProfile_PhysicalAddress_Slot_Object = MibScalar
t1NetworkProfile_PhysicalAddress_Slot = _T1NetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 6),
    _T1NetworkProfile_PhysicalAddress_Slot_Type()
)
t1NetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_T1NetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_T1NetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
t1NetworkProfile_PhysicalAddress_ItemNumber = _T1NetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 7),
    _T1NetworkProfile_PhysicalAddress_ItemNumber_Type()
)
t1NetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_Enabled_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_Enabled based on Integer32"""
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


_T1NetworkProfile_LineInterface_Enabled_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_Enabled_Object = MibScalar
t1NetworkProfile_LineInterface_Enabled = _T1NetworkProfile_LineInterface_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 8),
    _T1NetworkProfile_LineInterface_Enabled_Type()
)
t1NetworkProfile_LineInterface_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Enabled.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_TOnlineType_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_TOnlineType based on Integer32"""
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
        *(("none", 1),
          ("nt", 2),
          ("numberOfTonline", 4),
          ("te", 3))
    )


_T1NetworkProfile_LineInterface_TOnlineType_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_TOnlineType_Object = MibScalar
t1NetworkProfile_LineInterface_TOnlineType = _T1NetworkProfile_LineInterface_TOnlineType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 9),
    _T1NetworkProfile_LineInterface_TOnlineType_Type()
)
t1NetworkProfile_LineInterface_TOnlineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_TOnlineType.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_FrameType_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_FrameType based on Integer32"""
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
        *(("d4", 1),
          ("esf", 2),
          ("g703", 3),
          ("n-2ds", 4))
    )


_T1NetworkProfile_LineInterface_FrameType_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_FrameType_Object = MibScalar
t1NetworkProfile_LineInterface_FrameType = _T1NetworkProfile_LineInterface_FrameType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 10),
    _T1NetworkProfile_LineInterface_FrameType_Type()
)
t1NetworkProfile_LineInterface_FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_FrameType.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_Encoding_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_Encoding based on Integer32"""
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
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3),
          ("none", 4))
    )


_T1NetworkProfile_LineInterface_Encoding_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_Encoding_Object = MibScalar
t1NetworkProfile_LineInterface_Encoding = _T1NetworkProfile_LineInterface_Encoding_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 11),
    _T1NetworkProfile_LineInterface_Encoding_Type()
)
t1NetworkProfile_LineInterface_Encoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Encoding.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_ClockSource_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_ClockSource based on Integer32"""
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


_T1NetworkProfile_LineInterface_ClockSource_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_ClockSource_Object = MibScalar
t1NetworkProfile_LineInterface_ClockSource = _T1NetworkProfile_LineInterface_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 12),
    _T1NetworkProfile_LineInterface_ClockSource_Type()
)
t1NetworkProfile_LineInterface_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ClockSource.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_ClockPriority_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_ClockPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 2),
          ("lowPriority", 4),
          ("middlePriority", 3))
    )


_T1NetworkProfile_LineInterface_ClockPriority_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_ClockPriority_Object = MibScalar
t1NetworkProfile_LineInterface_ClockPriority = _T1NetworkProfile_LineInterface_ClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 13),
    _T1NetworkProfile_LineInterface_ClockPriority_Type()
)
t1NetworkProfile_LineInterface_ClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ClockPriority.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_SignalingMode_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_SignalingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              13,
              14,
              15,
              16,
              17,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("dtmfR2Signaling", 25),
          ("e1ArgentinaSignaling", 13),
          ("e1BrazilSignaling", 14),
          ("e1ChineseSignaling", 8),
          ("e1CzechSignaling", 17),
          ("e1DpnssSignaling", 11),
          ("e1IndianSignaling", 16),
          ("e1IsraelSignaling", 21),
          ("e1KoreanSignaling", 6),
          ("e1KuwaitSignaling", 23),
          ("e1MalaysiaSignaling", 19),
          ("e1MeteredSignaling", 9),
          ("e1MexicoSignaling", 24),
          ("e1NewZealandSignaling", 20),
          ("e1NoSignaling", 10),
          ("e1P7Signaling", 7),
          ("e1PhilippineSignaling", 15),
          ("e1R2Signaling", 5),
          ("e1ThailandSignaling", 22),
          ("e1VietnamSignaling", 32),
          ("h248DataTrunk", 34),
          ("inband", 1),
          ("inbandFgcInFgcOut", 30),
          ("inbandFgcInFgdOut", 31),
          ("inbandFgdInFgcOut", 29),
          ("inbandFgdInFgdOut", 28),
          ("isdn", 2),
          ("isdnNfas", 3),
          ("ss7SigTrunk", 33),
          ("tunneledPriSignaling", 27))
    )


_T1NetworkProfile_LineInterface_SignalingMode_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_SignalingMode_Object = MibScalar
t1NetworkProfile_LineInterface_SignalingMode = _T1NetworkProfile_LineInterface_SignalingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 14),
    _T1NetworkProfile_LineInterface_SignalingMode_Type()
)
t1NetworkProfile_LineInterface_SignalingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_SignalingMode.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_IsdnEmulationSide_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_IsdnEmulationSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nt", 2),
          ("te", 1))
    )


_T1NetworkProfile_LineInterface_IsdnEmulationSide_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_IsdnEmulationSide_Object = MibScalar
t1NetworkProfile_LineInterface_IsdnEmulationSide = _T1NetworkProfile_LineInterface_IsdnEmulationSide_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 15),
    _T1NetworkProfile_LineInterface_IsdnEmulationSide_Type()
)
t1NetworkProfile_LineInterface_IsdnEmulationSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_IsdnEmulationSide.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_RobbedBitMode_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_RobbedBitMode based on Integer32"""
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
        *(("groundStart", 6),
          ("idleStart", 2),
          ("incW200", 3),
          ("incW400", 4),
          ("loopStart", 5),
          ("winkStart", 1))
    )


_T1NetworkProfile_LineInterface_RobbedBitMode_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_RobbedBitMode_Object = MibScalar
t1NetworkProfile_LineInterface_RobbedBitMode = _T1NetworkProfile_LineInterface_RobbedBitMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 16),
    _T1NetworkProfile_LineInterface_RobbedBitMode_Type()
)
t1NetworkProfile_LineInterface_RobbedBitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_RobbedBitMode.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_DefaultCallType_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_DefaultCallType based on Integer32"""
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
        *(("digital", 1),
          ("dnisOrDigital", 4),
          ("dnisOrVoice", 3),
          ("dnisOrVoip", 6),
          ("voice", 2),
          ("voip", 5))
    )


_T1NetworkProfile_LineInterface_DefaultCallType_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_DefaultCallType_Object = MibScalar
t1NetworkProfile_LineInterface_DefaultCallType = _T1NetworkProfile_LineInterface_DefaultCallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 17),
    _T1NetworkProfile_LineInterface_DefaultCallType_Type()
)
t1NetworkProfile_LineInterface_DefaultCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_DefaultCallType.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_SwitchType_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_SwitchType based on Integer32"""
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


_T1NetworkProfile_LineInterface_SwitchType_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_SwitchType_Object = MibScalar
t1NetworkProfile_LineInterface_SwitchType = _T1NetworkProfile_LineInterface_SwitchType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 18),
    _T1NetworkProfile_LineInterface_SwitchType_Type()
)
t1NetworkProfile_LineInterface_SwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_SwitchType.setStatus("mandatory")
_T1NetworkProfile_LineInterface_NfasGroupId_Type = Integer32
_T1NetworkProfile_LineInterface_NfasGroupId_Object = MibScalar
t1NetworkProfile_LineInterface_NfasGroupId = _T1NetworkProfile_LineInterface_NfasGroupId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 19),
    _T1NetworkProfile_LineInterface_NfasGroupId_Type()
)
t1NetworkProfile_LineInterface_NfasGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_NfasGroupId.setStatus("mandatory")
_T1NetworkProfile_LineInterface_NfasId_Type = Integer32
_T1NetworkProfile_LineInterface_NfasId_Object = MibScalar
t1NetworkProfile_LineInterface_NfasId = _T1NetworkProfile_LineInterface_NfasId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 20),
    _T1NetworkProfile_LineInterface_NfasId_Type()
)
t1NetworkProfile_LineInterface_NfasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_NfasId.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_IncomingCallHandling_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_IncomingCallHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalProcessing", 2),
          ("rejectAll", 1),
          ("ss7GatewayProcessing", 3))
    )


_T1NetworkProfile_LineInterface_IncomingCallHandling_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_IncomingCallHandling_Object = MibScalar
t1NetworkProfile_LineInterface_IncomingCallHandling = _T1NetworkProfile_LineInterface_IncomingCallHandling_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 21),
    _T1NetworkProfile_LineInterface_IncomingCallHandling_Type()
)
t1NetworkProfile_LineInterface_IncomingCallHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_IncomingCallHandling.setStatus("mandatory")
_T1NetworkProfile_LineInterface_DeleteDigits_Type = Integer32
_T1NetworkProfile_LineInterface_DeleteDigits_Object = MibScalar
t1NetworkProfile_LineInterface_DeleteDigits = _T1NetworkProfile_LineInterface_DeleteDigits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 22),
    _T1NetworkProfile_LineInterface_DeleteDigits_Type()
)
t1NetworkProfile_LineInterface_DeleteDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_DeleteDigits.setStatus("mandatory")
_T1NetworkProfile_LineInterface_AddDigitString_Type = DisplayString
_T1NetworkProfile_LineInterface_AddDigitString_Object = MibScalar
t1NetworkProfile_LineInterface_AddDigitString = _T1NetworkProfile_LineInterface_AddDigitString_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 23),
    _T1NetworkProfile_LineInterface_AddDigitString_Type()
)
t1NetworkProfile_LineInterface_AddDigitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_AddDigitString.setStatus("mandatory")
_T1NetworkProfile_LineInterface_CallByCall_Type = Integer32
_T1NetworkProfile_LineInterface_CallByCall_Object = MibScalar
t1NetworkProfile_LineInterface_CallByCall = _T1NetworkProfile_LineInterface_CallByCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 24),
    _T1NetworkProfile_LineInterface_CallByCall_Type()
)
t1NetworkProfile_LineInterface_CallByCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_CallByCall.setStatus("mandatory")
_T1NetworkProfile_LineInterface_PbxAnswerNumber_Type = DisplayString
_T1NetworkProfile_LineInterface_PbxAnswerNumber_Object = MibScalar
t1NetworkProfile_LineInterface_PbxAnswerNumber = _T1NetworkProfile_LineInterface_PbxAnswerNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 25),
    _T1NetworkProfile_LineInterface_PbxAnswerNumber_Type()
)
t1NetworkProfile_LineInterface_PbxAnswerNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_PbxAnswerNumber.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_AnswerService_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_AnswerService based on Integer32"""
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
              39,
              40,
              41,
              42,
              43,
              44,
              46,
              47,
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
              255,
              263)
        )
    )
    namedValues = NamedValues(
        *(("atmSvc", 70),
          ("atmodem", 44),
          ("dws384Clear", 14),
          ("frameRelaySvc", 71),
          ("iptoip", 263),
          ("modem", 43),
          ("modem31khzAudio", 82),
          ("n-1024Clear", 24),
          ("n-1088Clear", 25),
          ("n-1152Clear", 26),
          ("n-1216Clear", 27),
          ("n-1280Clear", 28),
          ("n-128kClear", 10),
          ("n-1344Clear", 29),
          ("n-1408Clear", 30),
          ("n-14456kV110", 74),
          ("n-14456krV110", 76),
          ("n-14464kV110", 78),
          ("n-14464krV110", 80),
          ("n-144kClear", 255),
          ("n-1472Clear", 31),
          ("n-1536kClear", 8),
          ("n-1536kRestricted", 9),
          ("n-1600Clear", 32),
          ("n-1664Clear", 33),
          ("n-1728Clear", 34),
          ("n-1792Clear", 35),
          ("n-1856Clear", 36),
          ("n-1920Clear", 37),
          ("n-19256kV110", 49),
          ("n-19256krV110", 54),
          ("n-19264kV110", 59),
          ("n-19264krV110", 64),
          ("n-192kClear", 11),
          ("n-2456kV110", 46),
          ("n-2456krV110", 51),
          ("n-2464kV110", 56),
          ("n-2464krV110", 61),
          ("n-256kClear", 12),
          ("n-28856kV110", 75),
          ("n-28856krV110", 77),
          ("n-28864kV110", 79),
          ("n-28864krV110", 81),
          ("n-320kClear", 13),
          ("n-38456kV110", 50),
          ("n-38456krV110", 55),
          ("n-38464kV110", 60),
          ("n-38464krV110", 65),
          ("n-384kClear", 7),
          ("n-384kRestricted", 6),
          ("n-448Clear", 15),
          ("n-4856kV110", 47),
          ("n-4856krV110", 52),
          ("n-4864kV110", 57),
          ("n-4864krV110", 62),
          ("n-512Clear", 16),
          ("n-56kClear", 5),
          ("n-56kRestricted", 2),
          ("n-56kV110Clear", 42),
          ("n-576Clear", 17),
          ("n-640Clear", 18),
          ("n-64kClear", 3),
          ("n-64kRestricted", 4),
          ("n-64kX30Restricted", 41),
          ("n-704Clear", 19),
          ("n-768Clear", 20),
          ("n-832Clear", 21),
          ("n-896Clear", 22),
          ("n-960Clear", 23),
          ("n-9656kV110", 48),
          ("n-9656krV110", 53),
          ("n-9664kV110", 58),
          ("n-9664krV110", 63),
          ("phs64k", 67),
          ("v110ClearBearer", 40),
          ("v32", 66),
          ("voice", 1),
          ("voiceOverIp", 68),
          ("vpnTunnel", 72),
          ("wormarq", 73),
          ("x25Svc", 83),
          ("x30RestrictedBearer", 39))
    )


_T1NetworkProfile_LineInterface_AnswerService_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_AnswerService_Object = MibScalar
t1NetworkProfile_LineInterface_AnswerService = _T1NetworkProfile_LineInterface_AnswerService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 26),
    _T1NetworkProfile_LineInterface_AnswerService_Type()
)
t1NetworkProfile_LineInterface_AnswerService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_AnswerService.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_oPBXType_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_oPBXType based on Integer32"""
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
        *(("hostPbxData", 2),
          ("hostPbxLeased11", 4),
          ("hostPbxLeasedData", 3),
          ("hostPbxVoice", 1))
    )


_T1NetworkProfile_LineInterface_oPBXType_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_oPBXType_Object = MibScalar
t1NetworkProfile_LineInterface_oPBXType = _T1NetworkProfile_LineInterface_oPBXType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 27),
    _T1NetworkProfile_LineInterface_oPBXType_Type()
)
t1NetworkProfile_LineInterface_oPBXType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_oPBXType.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_DataSense_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_DataSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inv", 2),
          ("normal", 1))
    )


_T1NetworkProfile_LineInterface_DataSense_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_DataSense_Object = MibScalar
t1NetworkProfile_LineInterface_DataSense = _T1NetworkProfile_LineInterface_DataSense_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 28),
    _T1NetworkProfile_LineInterface_DataSense_Type()
)
t1NetworkProfile_LineInterface_DataSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_DataSense.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_IdleMode_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_IdleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flagIdle", 2),
          ("markIdle", 1))
    )


_T1NetworkProfile_LineInterface_IdleMode_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_IdleMode_Object = MibScalar
t1NetworkProfile_LineInterface_IdleMode = _T1NetworkProfile_LineInterface_IdleMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 29),
    _T1NetworkProfile_LineInterface_IdleMode_Type()
)
t1NetworkProfile_LineInterface_IdleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_IdleMode.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_oFDL_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_oFDL based on Integer32"""
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
        *(("ansi", 3),
          ("atNT", 2),
          ("none", 1),
          ("sprint", 4))
    )


_T1NetworkProfile_LineInterface_oFDL_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_oFDL_Object = MibScalar
t1NetworkProfile_LineInterface_oFDL = _T1NetworkProfile_LineInterface_oFDL_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 30),
    _T1NetworkProfile_LineInterface_oFDL_Type()
)
t1NetworkProfile_LineInterface_oFDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_oFDL.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_FrontEndType_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_FrontEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csu", 1),
          ("dsx", 2))
    )


_T1NetworkProfile_LineInterface_FrontEndType_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_FrontEndType_Object = MibScalar
t1NetworkProfile_LineInterface_FrontEndType = _T1NetworkProfile_LineInterface_FrontEndType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 31),
    _T1NetworkProfile_LineInterface_FrontEndType_Type()
)
t1NetworkProfile_LineInterface_FrontEndType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_FrontEndType.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_oDSXLineLength_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_oDSXLineLength based on Integer32"""
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
        *(("n-1133", 1),
          ("n-134266", 2),
          ("n-267399", 3),
          ("n-400533", 4),
          ("n-534655", 5))
    )


_T1NetworkProfile_LineInterface_oDSXLineLength_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_oDSXLineLength_Object = MibScalar
t1NetworkProfile_LineInterface_oDSXLineLength = _T1NetworkProfile_LineInterface_oDSXLineLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 32),
    _T1NetworkProfile_LineInterface_oDSXLineLength_Type()
)
t1NetworkProfile_LineInterface_oDSXLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_oDSXLineLength.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_oCSUBuildOut_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_oCSUBuildOut based on Integer32"""
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
        *(("n-0Db", 1),
          ("n-15Db", 3),
          ("n-2255Db", 4),
          ("n-75Db", 2))
    )


_T1NetworkProfile_LineInterface_oCSUBuildOut_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_oCSUBuildOut_Object = MibScalar
t1NetworkProfile_LineInterface_oCSUBuildOut = _T1NetworkProfile_LineInterface_oCSUBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 33),
    _T1NetworkProfile_LineInterface_oCSUBuildOut_Type()
)
t1NetworkProfile_LineInterface_oCSUBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_oCSUBuildOut.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_OverlapReceiving_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_OverlapReceiving based on Integer32"""
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


_T1NetworkProfile_LineInterface_OverlapReceiving_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_OverlapReceiving_Object = MibScalar
t1NetworkProfile_LineInterface_OverlapReceiving = _T1NetworkProfile_LineInterface_OverlapReceiving_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 34),
    _T1NetworkProfile_LineInterface_OverlapReceiving_Type()
)
t1NetworkProfile_LineInterface_OverlapReceiving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_OverlapReceiving.setStatus("mandatory")
_T1NetworkProfile_LineInterface_PriPrefixNumber_Type = DisplayString
_T1NetworkProfile_LineInterface_PriPrefixNumber_Object = MibScalar
t1NetworkProfile_LineInterface_PriPrefixNumber = _T1NetworkProfile_LineInterface_PriPrefixNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 35),
    _T1NetworkProfile_LineInterface_PriPrefixNumber_Type()
)
t1NetworkProfile_LineInterface_PriPrefixNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_PriPrefixNumber.setStatus("mandatory")
_T1NetworkProfile_LineInterface_TrailingDigits_Type = Integer32
_T1NetworkProfile_LineInterface_TrailingDigits_Object = MibScalar
t1NetworkProfile_LineInterface_TrailingDigits = _T1NetworkProfile_LineInterface_TrailingDigits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 36),
    _T1NetworkProfile_LineInterface_TrailingDigits_Type()
)
t1NetworkProfile_LineInterface_TrailingDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_TrailingDigits.setStatus("mandatory")
_T1NetworkProfile_LineInterface_T302Timer_Type = Integer32
_T1NetworkProfile_LineInterface_T302Timer_Object = MibScalar
t1NetworkProfile_LineInterface_T302Timer = _T1NetworkProfile_LineInterface_T302Timer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 37),
    _T1NetworkProfile_LineInterface_T302Timer_Type()
)
t1NetworkProfile_LineInterface_T302Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_T302Timer.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_Layer3End_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_Layer3End based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_T1NetworkProfile_LineInterface_Layer3End_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_Layer3End_Object = MibScalar
t1NetworkProfile_LineInterface_Layer3End = _T1NetworkProfile_LineInterface_Layer3End_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 38),
    _T1NetworkProfile_LineInterface_Layer3End_Type()
)
t1NetworkProfile_LineInterface_Layer3End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Layer3End.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_Layer2End_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_Layer2End based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_T1NetworkProfile_LineInterface_Layer2End_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_Layer2End_Object = MibScalar
t1NetworkProfile_LineInterface_Layer2End = _T1NetworkProfile_LineInterface_Layer2End_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 39),
    _T1NetworkProfile_LineInterface_Layer2End_Type()
)
t1NetworkProfile_LineInterface_Layer2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Layer2End.setStatus("mandatory")
_T1NetworkProfile_LineInterface_NlValue_Type = Integer32
_T1NetworkProfile_LineInterface_NlValue_Object = MibScalar
t1NetworkProfile_LineInterface_NlValue = _T1NetworkProfile_LineInterface_NlValue_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 40),
    _T1NetworkProfile_LineInterface_NlValue_Type()
)
t1NetworkProfile_LineInterface_NlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_NlValue.setStatus("mandatory")
_T1NetworkProfile_LineInterface_LoopAvoidance_Type = Integer32
_T1NetworkProfile_LineInterface_LoopAvoidance_Object = MibScalar
t1NetworkProfile_LineInterface_LoopAvoidance = _T1NetworkProfile_LineInterface_LoopAvoidance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 41),
    _T1NetworkProfile_LineInterface_LoopAvoidance_Type()
)
t1NetworkProfile_LineInterface_LoopAvoidance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_LoopAvoidance.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_MaintenanceState_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_MaintenanceState based on Integer32"""
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


_T1NetworkProfile_LineInterface_MaintenanceState_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_MaintenanceState_Object = MibScalar
t1NetworkProfile_LineInterface_MaintenanceState = _T1NetworkProfile_LineInterface_MaintenanceState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 42),
    _T1NetworkProfile_LineInterface_MaintenanceState_Type()
)
t1NetworkProfile_LineInterface_MaintenanceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_MaintenanceState.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_NumberComplete_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_NumberComplete based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("endOfPulsing", 11),
          ("n-0Digits", 12),
          ("n-10Digits", 10),
          ("n-11Digits", 13),
          ("n-12Digits", 14),
          ("n-13Digits", 15),
          ("n-14Digits", 16),
          ("n-15Digits", 17),
          ("n-1Digits", 1),
          ("n-2Digits", 2),
          ("n-3Digits", 3),
          ("n-4Digits", 4),
          ("n-5Digits", 5),
          ("n-6Digits", 6),
          ("n-7Digits", 7),
          ("n-8Digits", 8),
          ("n-9Digits", 9),
          ("timeOut", 18))
    )


_T1NetworkProfile_LineInterface_NumberComplete_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_NumberComplete_Object = MibScalar
t1NetworkProfile_LineInterface_NumberComplete = _T1NetworkProfile_LineInterface_NumberComplete_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 43),
    _T1NetworkProfile_LineInterface_NumberComplete_Type()
)
t1NetworkProfile_LineInterface_NumberComplete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_NumberComplete.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_GroupBAnswerSignal_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_GroupBAnswerSignal based on Integer32"""
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
        *(("signalB1", 1),
          ("signalB10", 10),
          ("signalB11", 11),
          ("signalB12", 12),
          ("signalB13", 13),
          ("signalB14", 14),
          ("signalB15", 15),
          ("signalB2", 2),
          ("signalB3", 3),
          ("signalB4", 4),
          ("signalB5", 5),
          ("signalB6", 6),
          ("signalB7", 7),
          ("signalB8", 8),
          ("signalB9", 9))
    )


_T1NetworkProfile_LineInterface_GroupBAnswerSignal_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_GroupBAnswerSignal_Object = MibScalar
t1NetworkProfile_LineInterface_GroupBAnswerSignal = _T1NetworkProfile_LineInterface_GroupBAnswerSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 44),
    _T1NetworkProfile_LineInterface_GroupBAnswerSignal_Type()
)
t1NetworkProfile_LineInterface_GroupBAnswerSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_GroupBAnswerSignal.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_GroupBBusySignal_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_GroupBBusySignal based on Integer32"""
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
        *(("signalB1", 1),
          ("signalB10", 10),
          ("signalB11", 11),
          ("signalB12", 12),
          ("signalB13", 13),
          ("signalB14", 14),
          ("signalB15", 15),
          ("signalB2", 2),
          ("signalB3", 3),
          ("signalB4", 4),
          ("signalB5", 5),
          ("signalB6", 6),
          ("signalB7", 7),
          ("signalB8", 8),
          ("signalB9", 9))
    )


_T1NetworkProfile_LineInterface_GroupBBusySignal_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_GroupBBusySignal_Object = MibScalar
t1NetworkProfile_LineInterface_GroupBBusySignal = _T1NetworkProfile_LineInterface_GroupBBusySignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 45),
    _T1NetworkProfile_LineInterface_GroupBBusySignal_Type()
)
t1NetworkProfile_LineInterface_GroupBBusySignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_GroupBBusySignal.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_GroupBNoMatchSignal_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_GroupBNoMatchSignal based on Integer32"""
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
        *(("signalB1", 1),
          ("signalB10", 10),
          ("signalB11", 11),
          ("signalB12", 12),
          ("signalB13", 13),
          ("signalB14", 14),
          ("signalB15", 15),
          ("signalB2", 2),
          ("signalB3", 3),
          ("signalB4", 4),
          ("signalB5", 5),
          ("signalB6", 6),
          ("signalB7", 7),
          ("signalB8", 8),
          ("signalB9", 9))
    )


_T1NetworkProfile_LineInterface_GroupBNoMatchSignal_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_GroupBNoMatchSignal_Object = MibScalar
t1NetworkProfile_LineInterface_GroupBNoMatchSignal = _T1NetworkProfile_LineInterface_GroupBNoMatchSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 46),
    _T1NetworkProfile_LineInterface_GroupBNoMatchSignal_Type()
)
t1NetworkProfile_LineInterface_GroupBNoMatchSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_GroupBNoMatchSignal.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_GroupBCollectSignal_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_GroupBCollectSignal based on Integer32"""
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
        *(("signalB1", 1),
          ("signalB10", 10),
          ("signalB11", 11),
          ("signalB12", 12),
          ("signalB13", 13),
          ("signalB14", 14),
          ("signalB15", 15),
          ("signalB2", 2),
          ("signalB3", 3),
          ("signalB4", 4),
          ("signalB5", 5),
          ("signalB6", 6),
          ("signalB7", 7),
          ("signalB8", 8),
          ("signalB9", 9))
    )


_T1NetworkProfile_LineInterface_GroupBCollectSignal_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_GroupBCollectSignal_Object = MibScalar
t1NetworkProfile_LineInterface_GroupBCollectSignal = _T1NetworkProfile_LineInterface_GroupBCollectSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 47),
    _T1NetworkProfile_LineInterface_GroupBCollectSignal_Type()
)
t1NetworkProfile_LineInterface_GroupBCollectSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_GroupBCollectSignal.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_GroupIiSignal_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_GroupIiSignal based on Integer32"""
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
        *(("signalIi1", 1),
          ("signalIi10", 10),
          ("signalIi11", 11),
          ("signalIi12", 12),
          ("signalIi13", 13),
          ("signalIi14", 14),
          ("signalIi15", 15),
          ("signalIi2", 2),
          ("signalIi3", 3),
          ("signalIi4", 4),
          ("signalIi5", 5),
          ("signalIi6", 6),
          ("signalIi7", 7),
          ("signalIi8", 8),
          ("signalIi9", 9))
    )


_T1NetworkProfile_LineInterface_GroupIiSignal_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_GroupIiSignal_Object = MibScalar
t1NetworkProfile_LineInterface_GroupIiSignal = _T1NetworkProfile_LineInterface_GroupIiSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 48),
    _T1NetworkProfile_LineInterface_GroupIiSignal_Type()
)
t1NetworkProfile_LineInterface_GroupIiSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_GroupIiSignal.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_InputSampleCount_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_InputSampleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneSample", 1),
          ("twoSamples", 2))
    )


_T1NetworkProfile_LineInterface_InputSampleCount_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_InputSampleCount_Object = MibScalar
t1NetworkProfile_LineInterface_InputSampleCount = _T1NetworkProfile_LineInterface_InputSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 49),
    _T1NetworkProfile_LineInterface_InputSampleCount_Type()
)
t1NetworkProfile_LineInterface_InputSampleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_InputSampleCount.setStatus("mandatory")
_T1NetworkProfile_LineInterface_AnswerDelay_Type = Integer32
_T1NetworkProfile_LineInterface_AnswerDelay_Object = MibScalar
t1NetworkProfile_LineInterface_AnswerDelay = _T1NetworkProfile_LineInterface_AnswerDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 50),
    _T1NetworkProfile_LineInterface_AnswerDelay_Type()
)
t1NetworkProfile_LineInterface_AnswerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_AnswerDelay.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_CallerId_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_CallerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("getCallerId", 2),
          ("noCallerId", 1))
    )


_T1NetworkProfile_LineInterface_CallerId_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_CallerId_Object = MibScalar
t1NetworkProfile_LineInterface_CallerId = _T1NetworkProfile_LineInterface_CallerId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 51),
    _T1NetworkProfile_LineInterface_CallerId_Type()
)
t1NetworkProfile_LineInterface_CallerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_CallerId.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_LineSignaling_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_LineSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aBitOnly0EqualBBit", 2),
          ("aBitOnly1EqualBBit", 3),
          ("abBitsLineSignaling", 1))
    )


_T1NetworkProfile_LineInterface_LineSignaling_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_LineSignaling_Object = MibScalar
t1NetworkProfile_LineInterface_LineSignaling = _T1NetworkProfile_LineInterface_LineSignaling_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 52),
    _T1NetworkProfile_LineInterface_LineSignaling_Type()
)
t1NetworkProfile_LineInterface_LineSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_LineSignaling.setStatus("mandatory")
_T1NetworkProfile_LineInterface_Timer1CollectCall_Type = Integer32
_T1NetworkProfile_LineInterface_Timer1CollectCall_Object = MibScalar
t1NetworkProfile_LineInterface_Timer1CollectCall = _T1NetworkProfile_LineInterface_Timer1CollectCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 53),
    _T1NetworkProfile_LineInterface_Timer1CollectCall_Type()
)
t1NetworkProfile_LineInterface_Timer1CollectCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Timer1CollectCall.setStatus("mandatory")
_T1NetworkProfile_LineInterface_Timer2CollectCall_Type = Integer32
_T1NetworkProfile_LineInterface_Timer2CollectCall_Object = MibScalar
t1NetworkProfile_LineInterface_Timer2CollectCall = _T1NetworkProfile_LineInterface_Timer2CollectCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 54),
    _T1NetworkProfile_LineInterface_Timer2CollectCall_Type()
)
t1NetworkProfile_LineInterface_Timer2CollectCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Timer2CollectCall.setStatus("mandatory")
_T1NetworkProfile_LineInterface_SendDiscVal_Type = Integer32
_T1NetworkProfile_LineInterface_SendDiscVal_Object = MibScalar
t1NetworkProfile_LineInterface_SendDiscVal = _T1NetworkProfile_LineInterface_SendDiscVal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 55),
    _T1NetworkProfile_LineInterface_SendDiscVal_Type()
)
t1NetworkProfile_LineInterface_SendDiscVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_SendDiscVal.setStatus("mandatory")
_T1NetworkProfile_LineInterface_HuntGrpPhoneNumber1_Type = DisplayString
_T1NetworkProfile_LineInterface_HuntGrpPhoneNumber1_Object = MibScalar
t1NetworkProfile_LineInterface_HuntGrpPhoneNumber1 = _T1NetworkProfile_LineInterface_HuntGrpPhoneNumber1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 56),
    _T1NetworkProfile_LineInterface_HuntGrpPhoneNumber1_Type()
)
t1NetworkProfile_LineInterface_HuntGrpPhoneNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_HuntGrpPhoneNumber1.setStatus("mandatory")
_T1NetworkProfile_LineInterface_HuntGrpPhoneNumber2_Type = DisplayString
_T1NetworkProfile_LineInterface_HuntGrpPhoneNumber2_Object = MibScalar
t1NetworkProfile_LineInterface_HuntGrpPhoneNumber2 = _T1NetworkProfile_LineInterface_HuntGrpPhoneNumber2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 57),
    _T1NetworkProfile_LineInterface_HuntGrpPhoneNumber2_Type()
)
t1NetworkProfile_LineInterface_HuntGrpPhoneNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_HuntGrpPhoneNumber2.setStatus("mandatory")
_T1NetworkProfile_LineInterface_HuntGrpPhoneNumber3_Type = DisplayString
_T1NetworkProfile_LineInterface_HuntGrpPhoneNumber3_Object = MibScalar
t1NetworkProfile_LineInterface_HuntGrpPhoneNumber3 = _T1NetworkProfile_LineInterface_HuntGrpPhoneNumber3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 58),
    _T1NetworkProfile_LineInterface_HuntGrpPhoneNumber3_Type()
)
t1NetworkProfile_LineInterface_HuntGrpPhoneNumber3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_HuntGrpPhoneNumber3.setStatus("mandatory")
_T1NetworkProfile_LineInterface_PriTypeOfNumber_Type = Integer32
_T1NetworkProfile_LineInterface_PriTypeOfNumber_Object = MibScalar
t1NetworkProfile_LineInterface_PriTypeOfNumber = _T1NetworkProfile_LineInterface_PriTypeOfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 59),
    _T1NetworkProfile_LineInterface_PriTypeOfNumber_Type()
)
t1NetworkProfile_LineInterface_PriTypeOfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_PriTypeOfNumber.setStatus("mandatory")
_T1NetworkProfile_LineInterface_PriNumberingPlanId_Type = Integer32
_T1NetworkProfile_LineInterface_PriNumberingPlanId_Object = MibScalar
t1NetworkProfile_LineInterface_PriNumberingPlanId = _T1NetworkProfile_LineInterface_PriNumberingPlanId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 60),
    _T1NetworkProfile_LineInterface_PriNumberingPlanId_Type()
)
t1NetworkProfile_LineInterface_PriNumberingPlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_PriNumberingPlanId.setStatus("mandatory")
_T1NetworkProfile_LineInterface_SuperFrameSrcLineNumber_Type = Integer32
_T1NetworkProfile_LineInterface_SuperFrameSrcLineNumber_Object = MibScalar
t1NetworkProfile_LineInterface_SuperFrameSrcLineNumber = _T1NetworkProfile_LineInterface_SuperFrameSrcLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 61),
    _T1NetworkProfile_LineInterface_SuperFrameSrcLineNumber_Type()
)
t1NetworkProfile_LineInterface_SuperFrameSrcLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_SuperFrameSrcLineNumber.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_CollectIncomingDigits_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_CollectIncomingDigits based on Integer32"""
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


_T1NetworkProfile_LineInterface_CollectIncomingDigits_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_CollectIncomingDigits_Object = MibScalar
t1NetworkProfile_LineInterface_CollectIncomingDigits = _T1NetworkProfile_LineInterface_CollectIncomingDigits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 62),
    _T1NetworkProfile_LineInterface_CollectIncomingDigits_Type()
)
t1NetworkProfile_LineInterface_CollectIncomingDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_CollectIncomingDigits.setStatus("mandatory")
_T1NetworkProfile_LineInterface_T1InterDigitTimeout_Type = Integer32
_T1NetworkProfile_LineInterface_T1InterDigitTimeout_Object = MibScalar
t1NetworkProfile_LineInterface_T1InterDigitTimeout = _T1NetworkProfile_LineInterface_T1InterDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 63),
    _T1NetworkProfile_LineInterface_T1InterDigitTimeout_Type()
)
t1NetworkProfile_LineInterface_T1InterDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_T1InterDigitTimeout.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_R1UseAnir_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_R1UseAnir based on Integer32"""
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


_T1NetworkProfile_LineInterface_R1UseAnir_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_R1UseAnir_Object = MibScalar
t1NetworkProfile_LineInterface_R1UseAnir = _T1NetworkProfile_LineInterface_R1UseAnir_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 64),
    _T1NetworkProfile_LineInterface_R1UseAnir_Type()
)
t1NetworkProfile_LineInterface_R1UseAnir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_R1UseAnir.setStatus("mandatory")
_T1NetworkProfile_LineInterface_R1FirstDigitTimer_Type = Integer32
_T1NetworkProfile_LineInterface_R1FirstDigitTimer_Object = MibScalar
t1NetworkProfile_LineInterface_R1FirstDigitTimer = _T1NetworkProfile_LineInterface_R1FirstDigitTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 65),
    _T1NetworkProfile_LineInterface_R1FirstDigitTimer_Type()
)
t1NetworkProfile_LineInterface_R1FirstDigitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_R1FirstDigitTimer.setStatus("mandatory")
_T1NetworkProfile_LineInterface_R1AnirDelay_Type = Integer32
_T1NetworkProfile_LineInterface_R1AnirDelay_Object = MibScalar
t1NetworkProfile_LineInterface_R1AnirDelay = _T1NetworkProfile_LineInterface_R1AnirDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 66),
    _T1NetworkProfile_LineInterface_R1AnirDelay_Type()
)
t1NetworkProfile_LineInterface_R1AnirDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_R1AnirDelay.setStatus("mandatory")
_T1NetworkProfile_LineInterface_R1AnirTimer_Type = Integer32
_T1NetworkProfile_LineInterface_R1AnirTimer_Object = MibScalar
t1NetworkProfile_LineInterface_R1AnirTimer = _T1NetworkProfile_LineInterface_R1AnirTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 67),
    _T1NetworkProfile_LineInterface_R1AnirTimer_Type()
)
t1NetworkProfile_LineInterface_R1AnirTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_R1AnirTimer.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_R1Modified_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_R1Modified based on Integer32"""
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


_T1NetworkProfile_LineInterface_R1Modified_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_R1Modified_Object = MibScalar
t1NetworkProfile_LineInterface_R1Modified = _T1NetworkProfile_LineInterface_R1Modified_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 68),
    _T1NetworkProfile_LineInterface_R1Modified_Type()
)
t1NetworkProfile_LineInterface_R1Modified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_R1Modified.setStatus("mandatory")
_T1NetworkProfile_LineInterface_FirstDs0_Type = Integer32
_T1NetworkProfile_LineInterface_FirstDs0_Object = MibScalar
t1NetworkProfile_LineInterface_FirstDs0 = _T1NetworkProfile_LineInterface_FirstDs0_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 69),
    _T1NetworkProfile_LineInterface_FirstDs0_Type()
)
t1NetworkProfile_LineInterface_FirstDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_FirstDs0.setStatus("mandatory")
_T1NetworkProfile_LineInterface_LastDs0_Type = Integer32
_T1NetworkProfile_LineInterface_LastDs0_Object = MibScalar
t1NetworkProfile_LineInterface_LastDs0 = _T1NetworkProfile_LineInterface_LastDs0_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 70),
    _T1NetworkProfile_LineInterface_LastDs0_Type()
)
t1NetworkProfile_LineInterface_LastDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_LastDs0.setStatus("mandatory")
_T1NetworkProfile_LineInterface_NailedGroup_Type = Integer32
_T1NetworkProfile_LineInterface_NailedGroup_Object = MibScalar
t1NetworkProfile_LineInterface_NailedGroup = _T1NetworkProfile_LineInterface_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 71),
    _T1NetworkProfile_LineInterface_NailedGroup_Type()
)
t1NetworkProfile_LineInterface_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_NailedGroup.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_Ss7Continuity_IncomingProcedure_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_Ss7Continuity_IncomingProcedure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 2),
          ("transponder", 3))
    )


_T1NetworkProfile_LineInterface_Ss7Continuity_IncomingProcedure_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_Ss7Continuity_IncomingProcedure_Object = MibScalar
t1NetworkProfile_LineInterface_Ss7Continuity_IncomingProcedure = _T1NetworkProfile_LineInterface_Ss7Continuity_IncomingProcedure_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 72),
    _T1NetworkProfile_LineInterface_Ss7Continuity_IncomingProcedure_Type()
)
t1NetworkProfile_LineInterface_Ss7Continuity_IncomingProcedure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Ss7Continuity_IncomingProcedure.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_Ss7Continuity_OutgoingProcedure_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_Ss7Continuity_OutgoingProcedure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("send1780Expect2000", 7),
          ("send1780Expect2010", 4),
          ("send2000Expect1780", 6),
          ("send2010Expect1780", 3),
          ("singleTone2000", 5),
          ("singleTone2010", 2))
    )


_T1NetworkProfile_LineInterface_Ss7Continuity_OutgoingProcedure_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_Ss7Continuity_OutgoingProcedure_Object = MibScalar
t1NetworkProfile_LineInterface_Ss7Continuity_OutgoingProcedure = _T1NetworkProfile_LineInterface_Ss7Continuity_OutgoingProcedure_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 73),
    _T1NetworkProfile_LineInterface_Ss7Continuity_OutgoingProcedure_Type()
)
t1NetworkProfile_LineInterface_Ss7Continuity_OutgoingProcedure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Ss7Continuity_OutgoingProcedure.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_LineProvision_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_LineProvision based on Integer32"""
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
        *(("lineProvisionH0", 2),
          ("lineProvisionH0H11", 4),
          ("lineProvisionH0H11H12", 8),
          ("lineProvisionH0H12", 6),
          ("lineProvisionH11", 3),
          ("lineProvisionH11H12", 7),
          ("lineProvisionH12", 5),
          ("lineProvisionNone", 1))
    )


_T1NetworkProfile_LineInterface_LineProvision_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_LineProvision_Object = MibScalar
t1NetworkProfile_LineInterface_LineProvision = _T1NetworkProfile_LineInterface_LineProvision_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 74),
    _T1NetworkProfile_LineInterface_LineProvision_Type()
)
t1NetworkProfile_LineInterface_LineProvision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_LineProvision.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_Gr303Mode_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_Gr303Mode based on Integer32"""
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
        *(("gr3035essPri", 2),
          ("gr303Disabled", 1),
          ("gr303DmsPri", 3),
          ("gr303Normal", 5),
          ("gr303Secondary", 4))
    )


_T1NetworkProfile_LineInterface_Gr303Mode_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_Gr303Mode_Object = MibScalar
t1NetworkProfile_LineInterface_Gr303Mode = _T1NetworkProfile_LineInterface_Gr303Mode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 75),
    _T1NetworkProfile_LineInterface_Gr303Mode_Type()
)
t1NetworkProfile_LineInterface_Gr303Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Gr303Mode.setStatus("mandatory")
_T1NetworkProfile_LineInterface_Gr303GroupId_Type = Integer32
_T1NetworkProfile_LineInterface_Gr303GroupId_Object = MibScalar
t1NetworkProfile_LineInterface_Gr303GroupId = _T1NetworkProfile_LineInterface_Gr303GroupId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 76),
    _T1NetworkProfile_LineInterface_Gr303GroupId_Type()
)
t1NetworkProfile_LineInterface_Gr303GroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Gr303GroupId.setStatus("mandatory")
_T1NetworkProfile_LineInterface_Gr303Ds1Id_Type = Integer32
_T1NetworkProfile_LineInterface_Gr303Ds1Id_Object = MibScalar
t1NetworkProfile_LineInterface_Gr303Ds1Id = _T1NetworkProfile_LineInterface_Gr303Ds1Id_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 77),
    _T1NetworkProfile_LineInterface_Gr303Ds1Id_Type()
)
t1NetworkProfile_LineInterface_Gr303Ds1Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_Gr303Ds1Id.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_SwitchVersion_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_SwitchVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchVersionDefinityG3v4", 2),
          ("switchVersionGeneric", 1))
    )


_T1NetworkProfile_LineInterface_SwitchVersion_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_SwitchVersion_Object = MibScalar
t1NetworkProfile_LineInterface_SwitchVersion = _T1NetworkProfile_LineInterface_SwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 78),
    _T1NetworkProfile_LineInterface_SwitchVersion_Type()
)
t1NetworkProfile_LineInterface_SwitchVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_SwitchVersion.setStatus("mandatory")


class _T1NetworkProfile_BackToBack_Type(Integer32):
    """Custom type t1NetworkProfile_BackToBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_T1NetworkProfile_BackToBack_Type.__name__ = "Integer32"
_T1NetworkProfile_BackToBack_Object = MibScalar
t1NetworkProfile_BackToBack = _T1NetworkProfile_BackToBack_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 79),
    _T1NetworkProfile_BackToBack_Type()
)
t1NetworkProfile_BackToBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_BackToBack.setStatus("mandatory")


class _T1NetworkProfile_ChannelUsage_Type(Integer32):
    """Custom type t1NetworkProfile_ChannelUsage based on Integer32"""
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
        *(("dropAndInsert", 4),
          ("dualNetworkInterface", 5),
          ("lineDisable", 2),
          ("lineUnavailable", 1),
          ("t1LineQuiesce", 3),
          ("tOnlineUsrInterface", 6),
          ("tOnlineZgrInterface", 7))
    )


_T1NetworkProfile_ChannelUsage_Type.__name__ = "Integer32"
_T1NetworkProfile_ChannelUsage_Object = MibScalar
t1NetworkProfile_ChannelUsage = _T1NetworkProfile_ChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 80),
    _T1NetworkProfile_ChannelUsage_Type()
)
t1NetworkProfile_ChannelUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_ChannelUsage.setStatus("mandatory")


class _T1NetworkProfile_Action_o_Type(Integer32):
    """Custom type t1NetworkProfile_Action_o based on Integer32"""
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


_T1NetworkProfile_Action_o_Type.__name__ = "Integer32"
_T1NetworkProfile_Action_o_Object = MibScalar
t1NetworkProfile_Action_o = _T1NetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 81),
    _T1NetworkProfile_Action_o_Type()
)
t1NetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_Action_o.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_GroupBNoChargeSignal_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_GroupBNoChargeSignal based on Integer32"""
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
        *(("signalB1", 1),
          ("signalB10", 10),
          ("signalB11", 11),
          ("signalB12", 12),
          ("signalB13", 13),
          ("signalB14", 14),
          ("signalB15", 15),
          ("signalB2", 2),
          ("signalB3", 3),
          ("signalB4", 4),
          ("signalB5", 5),
          ("signalB6", 6),
          ("signalB7", 7),
          ("signalB8", 8),
          ("signalB9", 9))
    )


_T1NetworkProfile_LineInterface_GroupBNoChargeSignal_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_GroupBNoChargeSignal_Object = MibScalar
t1NetworkProfile_LineInterface_GroupBNoChargeSignal = _T1NetworkProfile_LineInterface_GroupBNoChargeSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 82),
    _T1NetworkProfile_LineInterface_GroupBNoChargeSignal_Type()
)
t1NetworkProfile_LineInterface_GroupBNoChargeSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_GroupBNoChargeSignal.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_StatusChangeTrapEnable_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_StatusChangeTrapEnable based on Integer32"""
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


_T1NetworkProfile_LineInterface_StatusChangeTrapEnable_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_StatusChangeTrapEnable_Object = MibScalar
t1NetworkProfile_LineInterface_StatusChangeTrapEnable = _T1NetworkProfile_LineInterface_StatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 83),
    _T1NetworkProfile_LineInterface_StatusChangeTrapEnable_Type()
)
t1NetworkProfile_LineInterface_StatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_StatusChangeTrapEnable.setStatus("mandatory")
_T1NetworkProfile_LineInterface_DownTransDelay_Type = Integer32
_T1NetworkProfile_LineInterface_DownTransDelay_Object = MibScalar
t1NetworkProfile_LineInterface_DownTransDelay = _T1NetworkProfile_LineInterface_DownTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 84),
    _T1NetworkProfile_LineInterface_DownTransDelay_Type()
)
t1NetworkProfile_LineInterface_DownTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_DownTransDelay.setStatus("mandatory")
_T1NetworkProfile_LineInterface_UpTransDelay_Type = Integer32
_T1NetworkProfile_LineInterface_UpTransDelay_Object = MibScalar
t1NetworkProfile_LineInterface_UpTransDelay = _T1NetworkProfile_LineInterface_UpTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 85),
    _T1NetworkProfile_LineInterface_UpTransDelay_Type()
)
t1NetworkProfile_LineInterface_UpTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_UpTransDelay.setStatus("mandatory")
_T1NetworkProfile_LineInterface_NetworkSpecificFacilities_Type = Integer32
_T1NetworkProfile_LineInterface_NetworkSpecificFacilities_Object = MibScalar
t1NetworkProfile_LineInterface_NetworkSpecificFacilities = _T1NetworkProfile_LineInterface_NetworkSpecificFacilities_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 87),
    _T1NetworkProfile_LineInterface_NetworkSpecificFacilities_Type()
)
t1NetworkProfile_LineInterface_NetworkSpecificFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_NetworkSpecificFacilities.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_CauseCodeVerificationEnable_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_CauseCodeVerificationEnable based on Integer32"""
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


_T1NetworkProfile_LineInterface_CauseCodeVerificationEnable_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_CauseCodeVerificationEnable_Object = MibScalar
t1NetworkProfile_LineInterface_CauseCodeVerificationEnable = _T1NetworkProfile_LineInterface_CauseCodeVerificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 1, 1, 88),
    _T1NetworkProfile_LineInterface_CauseCodeVerificationEnable_Type()
)
t1NetworkProfile_LineInterface_CauseCodeVerificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_CauseCodeVerificationEnable.setStatus("mandatory")
_Mibt1NetworkProfile_LineInterface_ChannelConfigTable_Object = MibTable
mibt1NetworkProfile_LineInterface_ChannelConfigTable = _Mibt1NetworkProfile_LineInterface_ChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2)
)
if mibBuilder.loadTexts:
    mibt1NetworkProfile_LineInterface_ChannelConfigTable.setStatus("mandatory")
_Mibt1NetworkProfile_LineInterface_ChannelConfigEntry_Object = MibTableRow
mibt1NetworkProfile_LineInterface_ChannelConfigEntry = _Mibt1NetworkProfile_LineInterface_ChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1)
)
mibt1NetworkProfile_LineInterface_ChannelConfigEntry.setIndexNames(
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfile-LineInterface-ChannelConfig-Shelf-o"),
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfile-LineInterface-ChannelConfig-Slot-o"),
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfile-LineInterface-ChannelConfig-Item-o"),
    (0, "ASCEND-MIBT1NET-MIB", "t1NetworkProfile-LineInterface-ChannelConfig-Index-o"),
)
if mibBuilder.loadTexts:
    mibt1NetworkProfile_LineInterface_ChannelConfigEntry.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_Shelf_o_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_Shelf_o_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_Shelf_o = _T1NetworkProfile_LineInterface_ChannelConfig_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 1),
    _T1NetworkProfile_LineInterface_ChannelConfig_Shelf_o_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_Shelf_o.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_Slot_o_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_Slot_o_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_Slot_o = _T1NetworkProfile_LineInterface_ChannelConfig_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 2),
    _T1NetworkProfile_LineInterface_ChannelConfig_Slot_o_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_Slot_o.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_Item_o_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_Item_o_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_Item_o = _T1NetworkProfile_LineInterface_ChannelConfig_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 3),
    _T1NetworkProfile_LineInterface_ChannelConfig_Item_o_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_Item_o.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_Index_o_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_Index_o_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_Index_o = _T1NetworkProfile_LineInterface_ChannelConfig_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 4),
    _T1NetworkProfile_LineInterface_ChannelConfig_Index_o_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_Index_o.setStatus("mandatory")


class _T1NetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Type(Integer32):
    """Custom type t1NetworkProfile_LineInterface_ChannelConfig_ChannelUsage based on Integer32"""
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


_T1NetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Type.__name__ = "Integer32"
_T1NetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_ChannelUsage = _T1NetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 5),
    _T1NetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_ChannelUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_ChannelUsage.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_TrunkGroup_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_TrunkGroup_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_TrunkGroup = _T1NetworkProfile_LineInterface_ChannelConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 6),
    _T1NetworkProfile_LineInterface_ChannelConfig_TrunkGroup_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_TrunkGroup.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_PhoneNumber_Type = DisplayString
_T1NetworkProfile_LineInterface_ChannelConfig_PhoneNumber_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_PhoneNumber = _T1NetworkProfile_LineInterface_ChannelConfig_PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 7),
    _T1NetworkProfile_LineInterface_ChannelConfig_PhoneNumber_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_PhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_PhoneNumber.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber = _T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 8),
    _T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber = _T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 9),
    _T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber = _T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 10),
    _T1NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_NailedGroup_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_NailedGroup_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_NailedGroup = _T1NetworkProfile_LineInterface_ChannelConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 14),
    _T1NetworkProfile_LineInterface_ChannelConfig_NailedGroup_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_NailedGroup.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_ChanGroup_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_ChanGroup_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_ChanGroup = _T1NetworkProfile_LineInterface_ChannelConfig_ChanGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 15),
    _T1NetworkProfile_LineInterface_ChannelConfig_ChanGroup_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_ChanGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_ChanGroup.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_DestChanGroup_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_DestChanGroup_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_DestChanGroup = _T1NetworkProfile_LineInterface_ChannelConfig_DestChanGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 16),
    _T1NetworkProfile_LineInterface_ChannelConfig_DestChanGroup_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_DestChanGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_DestChanGroup.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_DialPlanNumber_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_DialPlanNumber_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_DialPlanNumber = _T1NetworkProfile_LineInterface_ChannelConfig_DialPlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 17),
    _T1NetworkProfile_LineInterface_ChannelConfig_DialPlanNumber_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_DialPlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_DialPlanNumber.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits = _T1NetworkProfile_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 18),
    _T1NetworkProfile_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits.setStatus("mandatory")
_T1NetworkProfile_LineInterface_ChannelConfig_IdlePattern_Type = Integer32
_T1NetworkProfile_LineInterface_ChannelConfig_IdlePattern_Object = MibScalar
t1NetworkProfile_LineInterface_ChannelConfig_IdlePattern = _T1NetworkProfile_LineInterface_ChannelConfig_IdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 127, 2, 1, 19),
    _T1NetworkProfile_LineInterface_ChannelConfig_IdlePattern_Type()
)
t1NetworkProfile_LineInterface_ChannelConfig_IdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1NetworkProfile_LineInterface_ChannelConfig_IdlePattern.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBT1NET-MIB",
    **{"DisplayString": DisplayString,
       "mibt1NetworkProfileV1": mibt1NetworkProfileV1,
       "mibt1NetworkProfileV1Table": mibt1NetworkProfileV1Table,
       "mibt1NetworkProfileV1Entry": mibt1NetworkProfileV1Entry,
       "t1NetworkProfileV1-ProfileNumber": t1NetworkProfileV1_ProfileNumber,
       "t1NetworkProfileV1-Name": t1NetworkProfileV1_Name,
       "t1NetworkProfileV1-PhysicalAddress-Shelf": t1NetworkProfileV1_PhysicalAddress_Shelf,
       "t1NetworkProfileV1-PhysicalAddress-Slot": t1NetworkProfileV1_PhysicalAddress_Slot,
       "t1NetworkProfileV1-PhysicalAddress-ItemNumber": t1NetworkProfileV1_PhysicalAddress_ItemNumber,
       "t1NetworkProfileV1-BackToBack": t1NetworkProfileV1_BackToBack,
       "t1NetworkProfileV1-PrimaryChannelUsage": t1NetworkProfileV1_PrimaryChannelUsage,
       "t1NetworkProfileV1-SecondaryChannelUsage": t1NetworkProfileV1_SecondaryChannelUsage,
       "t1NetworkProfileV1-TertiaryChannelUsage": t1NetworkProfileV1_TertiaryChannelUsage,
       "t1NetworkProfileV1-Action-o": t1NetworkProfileV1_Action_o,
       "mibt1NetworkProfileV1-LineInterfaceTable": mibt1NetworkProfileV1_LineInterfaceTable,
       "mibt1NetworkProfileV1-LineInterfaceEntry": mibt1NetworkProfileV1_LineInterfaceEntry,
       "t1NetworkProfileV1-LineInterface-Name": t1NetworkProfileV1_LineInterface_Name,
       "t1NetworkProfileV1-LineInterface-Index-o": t1NetworkProfileV1_LineInterface_Index_o,
       "t1NetworkProfileV1-LineInterface-Enabled": t1NetworkProfileV1_LineInterface_Enabled,
       "t1NetworkProfileV1-LineInterface-TOnlineType": t1NetworkProfileV1_LineInterface_TOnlineType,
       "t1NetworkProfileV1-LineInterface-FrameType": t1NetworkProfileV1_LineInterface_FrameType,
       "t1NetworkProfileV1-LineInterface-Encoding": t1NetworkProfileV1_LineInterface_Encoding,
       "t1NetworkProfileV1-LineInterface-ClockSource": t1NetworkProfileV1_LineInterface_ClockSource,
       "t1NetworkProfileV1-LineInterface-ClockPriority": t1NetworkProfileV1_LineInterface_ClockPriority,
       "t1NetworkProfileV1-LineInterface-SignalingMode": t1NetworkProfileV1_LineInterface_SignalingMode,
       "t1NetworkProfileV1-LineInterface-IsdnEmulationSide": t1NetworkProfileV1_LineInterface_IsdnEmulationSide,
       "t1NetworkProfileV1-LineInterface-RobbedBitMode": t1NetworkProfileV1_LineInterface_RobbedBitMode,
       "t1NetworkProfileV1-LineInterface-DefaultCallType": t1NetworkProfileV1_LineInterface_DefaultCallType,
       "t1NetworkProfileV1-LineInterface-SwitchType": t1NetworkProfileV1_LineInterface_SwitchType,
       "t1NetworkProfileV1-LineInterface-NfasGroupId": t1NetworkProfileV1_LineInterface_NfasGroupId,
       "t1NetworkProfileV1-LineInterface-NfasId": t1NetworkProfileV1_LineInterface_NfasId,
       "t1NetworkProfileV1-LineInterface-IncomingCallHandling": t1NetworkProfileV1_LineInterface_IncomingCallHandling,
       "t1NetworkProfileV1-LineInterface-DeleteDigits": t1NetworkProfileV1_LineInterface_DeleteDigits,
       "t1NetworkProfileV1-LineInterface-AddDigitString": t1NetworkProfileV1_LineInterface_AddDigitString,
       "t1NetworkProfileV1-LineInterface-CallByCall": t1NetworkProfileV1_LineInterface_CallByCall,
       "t1NetworkProfileV1-LineInterface-PbxAnswerNumber": t1NetworkProfileV1_LineInterface_PbxAnswerNumber,
       "t1NetworkProfileV1-LineInterface-AnswerService": t1NetworkProfileV1_LineInterface_AnswerService,
       "t1NetworkProfileV1-LineInterface-oPBXType": t1NetworkProfileV1_LineInterface_oPBXType,
       "t1NetworkProfileV1-LineInterface-DataSense": t1NetworkProfileV1_LineInterface_DataSense,
       "t1NetworkProfileV1-LineInterface-IdleMode": t1NetworkProfileV1_LineInterface_IdleMode,
       "t1NetworkProfileV1-LineInterface-oFDL": t1NetworkProfileV1_LineInterface_oFDL,
       "t1NetworkProfileV1-LineInterface-FrontEndType": t1NetworkProfileV1_LineInterface_FrontEndType,
       "t1NetworkProfileV1-LineInterface-oDSXLineLength": t1NetworkProfileV1_LineInterface_oDSXLineLength,
       "t1NetworkProfileV1-LineInterface-oCSUBuildOut": t1NetworkProfileV1_LineInterface_oCSUBuildOut,
       "t1NetworkProfileV1-LineInterface-OverlapReceiving": t1NetworkProfileV1_LineInterface_OverlapReceiving,
       "t1NetworkProfileV1-LineInterface-PriPrefixNumber": t1NetworkProfileV1_LineInterface_PriPrefixNumber,
       "t1NetworkProfileV1-LineInterface-TrailingDigits": t1NetworkProfileV1_LineInterface_TrailingDigits,
       "t1NetworkProfileV1-LineInterface-T302Timer": t1NetworkProfileV1_LineInterface_T302Timer,
       "t1NetworkProfileV1-LineInterface-Layer3End": t1NetworkProfileV1_LineInterface_Layer3End,
       "t1NetworkProfileV1-LineInterface-Layer2End": t1NetworkProfileV1_LineInterface_Layer2End,
       "t1NetworkProfileV1-LineInterface-NlValue": t1NetworkProfileV1_LineInterface_NlValue,
       "t1NetworkProfileV1-LineInterface-LoopAvoidance": t1NetworkProfileV1_LineInterface_LoopAvoidance,
       "t1NetworkProfileV1-LineInterface-MaintenanceState": t1NetworkProfileV1_LineInterface_MaintenanceState,
       "t1NetworkProfileV1-LineInterface-NumberComplete": t1NetworkProfileV1_LineInterface_NumberComplete,
       "t1NetworkProfileV1-LineInterface-GroupBAnswerSignal": t1NetworkProfileV1_LineInterface_GroupBAnswerSignal,
       "t1NetworkProfileV1-LineInterface-GroupBBusySignal": t1NetworkProfileV1_LineInterface_GroupBBusySignal,
       "t1NetworkProfileV1-LineInterface-GroupBNoMatchSignal": t1NetworkProfileV1_LineInterface_GroupBNoMatchSignal,
       "t1NetworkProfileV1-LineInterface-GroupBCollectSignal": t1NetworkProfileV1_LineInterface_GroupBCollectSignal,
       "t1NetworkProfileV1-LineInterface-GroupIiSignal": t1NetworkProfileV1_LineInterface_GroupIiSignal,
       "t1NetworkProfileV1-LineInterface-InputSampleCount": t1NetworkProfileV1_LineInterface_InputSampleCount,
       "t1NetworkProfileV1-LineInterface-AnswerDelay": t1NetworkProfileV1_LineInterface_AnswerDelay,
       "t1NetworkProfileV1-LineInterface-CallerId": t1NetworkProfileV1_LineInterface_CallerId,
       "t1NetworkProfileV1-LineInterface-LineSignaling": t1NetworkProfileV1_LineInterface_LineSignaling,
       "t1NetworkProfileV1-LineInterface-Timer1CollectCall": t1NetworkProfileV1_LineInterface_Timer1CollectCall,
       "t1NetworkProfileV1-LineInterface-Timer2CollectCall": t1NetworkProfileV1_LineInterface_Timer2CollectCall,
       "t1NetworkProfileV1-LineInterface-SendDiscVal": t1NetworkProfileV1_LineInterface_SendDiscVal,
       "t1NetworkProfileV1-LineInterface-HuntGrpPhoneNumber1": t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber1,
       "t1NetworkProfileV1-LineInterface-HuntGrpPhoneNumber2": t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber2,
       "t1NetworkProfileV1-LineInterface-HuntGrpPhoneNumber3": t1NetworkProfileV1_LineInterface_HuntGrpPhoneNumber3,
       "t1NetworkProfileV1-LineInterface-PriTypeOfNumber": t1NetworkProfileV1_LineInterface_PriTypeOfNumber,
       "t1NetworkProfileV1-LineInterface-PriNumberingPlanId": t1NetworkProfileV1_LineInterface_PriNumberingPlanId,
       "t1NetworkProfileV1-LineInterface-SuperFrameSrcLineNumber": t1NetworkProfileV1_LineInterface_SuperFrameSrcLineNumber,
       "t1NetworkProfileV1-LineInterface-CollectIncomingDigits": t1NetworkProfileV1_LineInterface_CollectIncomingDigits,
       "t1NetworkProfileV1-LineInterface-T1InterDigitTimeout": t1NetworkProfileV1_LineInterface_T1InterDigitTimeout,
       "t1NetworkProfileV1-LineInterface-R1UseAnir": t1NetworkProfileV1_LineInterface_R1UseAnir,
       "t1NetworkProfileV1-LineInterface-R1FirstDigitTimer": t1NetworkProfileV1_LineInterface_R1FirstDigitTimer,
       "t1NetworkProfileV1-LineInterface-R1AnirDelay": t1NetworkProfileV1_LineInterface_R1AnirDelay,
       "t1NetworkProfileV1-LineInterface-R1AnirTimer": t1NetworkProfileV1_LineInterface_R1AnirTimer,
       "t1NetworkProfileV1-LineInterface-R1Modified": t1NetworkProfileV1_LineInterface_R1Modified,
       "t1NetworkProfileV1-LineInterface-FirstDs0": t1NetworkProfileV1_LineInterface_FirstDs0,
       "t1NetworkProfileV1-LineInterface-LastDs0": t1NetworkProfileV1_LineInterface_LastDs0,
       "t1NetworkProfileV1-LineInterface-NailedGroup": t1NetworkProfileV1_LineInterface_NailedGroup,
       "t1NetworkProfileV1-LineInterface-Ss7Continuity-IncomingProcedure": t1NetworkProfileV1_LineInterface_Ss7Continuity_IncomingProcedure,
       "t1NetworkProfileV1-LineInterface-Ss7Continuity-OutgoingProcedure": t1NetworkProfileV1_LineInterface_Ss7Continuity_OutgoingProcedure,
       "t1NetworkProfileV1-LineInterface-LineProvision": t1NetworkProfileV1_LineInterface_LineProvision,
       "t1NetworkProfileV1-LineInterface-Gr303Mode": t1NetworkProfileV1_LineInterface_Gr303Mode,
       "t1NetworkProfileV1-LineInterface-Gr303GroupId": t1NetworkProfileV1_LineInterface_Gr303GroupId,
       "t1NetworkProfileV1-LineInterface-Gr303Ds1Id": t1NetworkProfileV1_LineInterface_Gr303Ds1Id,
       "t1NetworkProfileV1-LineInterface-SwitchVersion": t1NetworkProfileV1_LineInterface_SwitchVersion,
       "t1NetworkProfileV1-LineInterface-GroupBNoChargeSignal": t1NetworkProfileV1_LineInterface_GroupBNoChargeSignal,
       "t1NetworkProfileV1-LineInterface-StatusChangeTrapEnable": t1NetworkProfileV1_LineInterface_StatusChangeTrapEnable,
       "t1NetworkProfileV1-LineInterface-DownTransDelay": t1NetworkProfileV1_LineInterface_DownTransDelay,
       "t1NetworkProfileV1-LineInterface-UpTransDelay": t1NetworkProfileV1_LineInterface_UpTransDelay,
       "t1NetworkProfileV1-LineInterface-NetworkSpecificFacilities": t1NetworkProfileV1_LineInterface_NetworkSpecificFacilities,
       "t1NetworkProfileV1-LineInterface-CauseCodeVerificationEnable": t1NetworkProfileV1_LineInterface_CauseCodeVerificationEnable,
       "mibt1NetworkProfileV1-LineInterface-ChannelConfigTable": mibt1NetworkProfileV1_LineInterface_ChannelConfigTable,
       "mibt1NetworkProfileV1-LineInterface-ChannelConfigEntry": mibt1NetworkProfileV1_LineInterface_ChannelConfigEntry,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-Name": t1NetworkProfileV1_LineInterface_ChannelConfig_Name,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-Index-o": t1NetworkProfileV1_LineInterface_ChannelConfig_Index_o,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-Index1-o": t1NetworkProfileV1_LineInterface_ChannelConfig_Index1_o,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-ChannelUsage": t1NetworkProfileV1_LineInterface_ChannelConfig_ChannelUsage,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-TrunkGroup": t1NetworkProfileV1_LineInterface_ChannelConfig_TrunkGroup,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-PhoneNumber": t1NetworkProfileV1_LineInterface_ChannelConfig_PhoneNumber,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-RoutePort-SlotNumber-SlotNumber": t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-RoutePort-SlotNumber-ShelfNumber": t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-RoutePort-RelativePortNumber-RelativePortNumber": t1NetworkProfileV1_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-NailedGroup": t1NetworkProfileV1_LineInterface_ChannelConfig_NailedGroup,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-ChanGroup": t1NetworkProfileV1_LineInterface_ChannelConfig_ChanGroup,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-DestChanGroup": t1NetworkProfileV1_LineInterface_ChannelConfig_DestChanGroup,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-DialPlanNumber": t1NetworkProfileV1_LineInterface_ChannelConfig_DialPlanNumber,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-NumberOfDialPlanSelectDigits": t1NetworkProfileV1_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits,
       "t1NetworkProfileV1-LineInterface-ChannelConfig-IdlePattern": t1NetworkProfileV1_LineInterface_ChannelConfig_IdlePattern,
       "mibt1NetworkProfile": mibt1NetworkProfile,
       "mibt1NetworkProfileTable": mibt1NetworkProfileTable,
       "mibt1NetworkProfileEntry": mibt1NetworkProfileEntry,
       "t1NetworkProfile-Shelf-o": t1NetworkProfile_Shelf_o,
       "t1NetworkProfile-Slot-o": t1NetworkProfile_Slot_o,
       "t1NetworkProfile-Item-o": t1NetworkProfile_Item_o,
       "t1NetworkProfile-Name": t1NetworkProfile_Name,
       "t1NetworkProfile-PhysicalAddress-Shelf": t1NetworkProfile_PhysicalAddress_Shelf,
       "t1NetworkProfile-PhysicalAddress-Slot": t1NetworkProfile_PhysicalAddress_Slot,
       "t1NetworkProfile-PhysicalAddress-ItemNumber": t1NetworkProfile_PhysicalAddress_ItemNumber,
       "t1NetworkProfile-LineInterface-Enabled": t1NetworkProfile_LineInterface_Enabled,
       "t1NetworkProfile-LineInterface-TOnlineType": t1NetworkProfile_LineInterface_TOnlineType,
       "t1NetworkProfile-LineInterface-FrameType": t1NetworkProfile_LineInterface_FrameType,
       "t1NetworkProfile-LineInterface-Encoding": t1NetworkProfile_LineInterface_Encoding,
       "t1NetworkProfile-LineInterface-ClockSource": t1NetworkProfile_LineInterface_ClockSource,
       "t1NetworkProfile-LineInterface-ClockPriority": t1NetworkProfile_LineInterface_ClockPriority,
       "t1NetworkProfile-LineInterface-SignalingMode": t1NetworkProfile_LineInterface_SignalingMode,
       "t1NetworkProfile-LineInterface-IsdnEmulationSide": t1NetworkProfile_LineInterface_IsdnEmulationSide,
       "t1NetworkProfile-LineInterface-RobbedBitMode": t1NetworkProfile_LineInterface_RobbedBitMode,
       "t1NetworkProfile-LineInterface-DefaultCallType": t1NetworkProfile_LineInterface_DefaultCallType,
       "t1NetworkProfile-LineInterface-SwitchType": t1NetworkProfile_LineInterface_SwitchType,
       "t1NetworkProfile-LineInterface-NfasGroupId": t1NetworkProfile_LineInterface_NfasGroupId,
       "t1NetworkProfile-LineInterface-NfasId": t1NetworkProfile_LineInterface_NfasId,
       "t1NetworkProfile-LineInterface-IncomingCallHandling": t1NetworkProfile_LineInterface_IncomingCallHandling,
       "t1NetworkProfile-LineInterface-DeleteDigits": t1NetworkProfile_LineInterface_DeleteDigits,
       "t1NetworkProfile-LineInterface-AddDigitString": t1NetworkProfile_LineInterface_AddDigitString,
       "t1NetworkProfile-LineInterface-CallByCall": t1NetworkProfile_LineInterface_CallByCall,
       "t1NetworkProfile-LineInterface-PbxAnswerNumber": t1NetworkProfile_LineInterface_PbxAnswerNumber,
       "t1NetworkProfile-LineInterface-AnswerService": t1NetworkProfile_LineInterface_AnswerService,
       "t1NetworkProfile-LineInterface-oPBXType": t1NetworkProfile_LineInterface_oPBXType,
       "t1NetworkProfile-LineInterface-DataSense": t1NetworkProfile_LineInterface_DataSense,
       "t1NetworkProfile-LineInterface-IdleMode": t1NetworkProfile_LineInterface_IdleMode,
       "t1NetworkProfile-LineInterface-oFDL": t1NetworkProfile_LineInterface_oFDL,
       "t1NetworkProfile-LineInterface-FrontEndType": t1NetworkProfile_LineInterface_FrontEndType,
       "t1NetworkProfile-LineInterface-oDSXLineLength": t1NetworkProfile_LineInterface_oDSXLineLength,
       "t1NetworkProfile-LineInterface-oCSUBuildOut": t1NetworkProfile_LineInterface_oCSUBuildOut,
       "t1NetworkProfile-LineInterface-OverlapReceiving": t1NetworkProfile_LineInterface_OverlapReceiving,
       "t1NetworkProfile-LineInterface-PriPrefixNumber": t1NetworkProfile_LineInterface_PriPrefixNumber,
       "t1NetworkProfile-LineInterface-TrailingDigits": t1NetworkProfile_LineInterface_TrailingDigits,
       "t1NetworkProfile-LineInterface-T302Timer": t1NetworkProfile_LineInterface_T302Timer,
       "t1NetworkProfile-LineInterface-Layer3End": t1NetworkProfile_LineInterface_Layer3End,
       "t1NetworkProfile-LineInterface-Layer2End": t1NetworkProfile_LineInterface_Layer2End,
       "t1NetworkProfile-LineInterface-NlValue": t1NetworkProfile_LineInterface_NlValue,
       "t1NetworkProfile-LineInterface-LoopAvoidance": t1NetworkProfile_LineInterface_LoopAvoidance,
       "t1NetworkProfile-LineInterface-MaintenanceState": t1NetworkProfile_LineInterface_MaintenanceState,
       "t1NetworkProfile-LineInterface-NumberComplete": t1NetworkProfile_LineInterface_NumberComplete,
       "t1NetworkProfile-LineInterface-GroupBAnswerSignal": t1NetworkProfile_LineInterface_GroupBAnswerSignal,
       "t1NetworkProfile-LineInterface-GroupBBusySignal": t1NetworkProfile_LineInterface_GroupBBusySignal,
       "t1NetworkProfile-LineInterface-GroupBNoMatchSignal": t1NetworkProfile_LineInterface_GroupBNoMatchSignal,
       "t1NetworkProfile-LineInterface-GroupBCollectSignal": t1NetworkProfile_LineInterface_GroupBCollectSignal,
       "t1NetworkProfile-LineInterface-GroupIiSignal": t1NetworkProfile_LineInterface_GroupIiSignal,
       "t1NetworkProfile-LineInterface-InputSampleCount": t1NetworkProfile_LineInterface_InputSampleCount,
       "t1NetworkProfile-LineInterface-AnswerDelay": t1NetworkProfile_LineInterface_AnswerDelay,
       "t1NetworkProfile-LineInterface-CallerId": t1NetworkProfile_LineInterface_CallerId,
       "t1NetworkProfile-LineInterface-LineSignaling": t1NetworkProfile_LineInterface_LineSignaling,
       "t1NetworkProfile-LineInterface-Timer1CollectCall": t1NetworkProfile_LineInterface_Timer1CollectCall,
       "t1NetworkProfile-LineInterface-Timer2CollectCall": t1NetworkProfile_LineInterface_Timer2CollectCall,
       "t1NetworkProfile-LineInterface-SendDiscVal": t1NetworkProfile_LineInterface_SendDiscVal,
       "t1NetworkProfile-LineInterface-HuntGrpPhoneNumber1": t1NetworkProfile_LineInterface_HuntGrpPhoneNumber1,
       "t1NetworkProfile-LineInterface-HuntGrpPhoneNumber2": t1NetworkProfile_LineInterface_HuntGrpPhoneNumber2,
       "t1NetworkProfile-LineInterface-HuntGrpPhoneNumber3": t1NetworkProfile_LineInterface_HuntGrpPhoneNumber3,
       "t1NetworkProfile-LineInterface-PriTypeOfNumber": t1NetworkProfile_LineInterface_PriTypeOfNumber,
       "t1NetworkProfile-LineInterface-PriNumberingPlanId": t1NetworkProfile_LineInterface_PriNumberingPlanId,
       "t1NetworkProfile-LineInterface-SuperFrameSrcLineNumber": t1NetworkProfile_LineInterface_SuperFrameSrcLineNumber,
       "t1NetworkProfile-LineInterface-CollectIncomingDigits": t1NetworkProfile_LineInterface_CollectIncomingDigits,
       "t1NetworkProfile-LineInterface-T1InterDigitTimeout": t1NetworkProfile_LineInterface_T1InterDigitTimeout,
       "t1NetworkProfile-LineInterface-R1UseAnir": t1NetworkProfile_LineInterface_R1UseAnir,
       "t1NetworkProfile-LineInterface-R1FirstDigitTimer": t1NetworkProfile_LineInterface_R1FirstDigitTimer,
       "t1NetworkProfile-LineInterface-R1AnirDelay": t1NetworkProfile_LineInterface_R1AnirDelay,
       "t1NetworkProfile-LineInterface-R1AnirTimer": t1NetworkProfile_LineInterface_R1AnirTimer,
       "t1NetworkProfile-LineInterface-R1Modified": t1NetworkProfile_LineInterface_R1Modified,
       "t1NetworkProfile-LineInterface-FirstDs0": t1NetworkProfile_LineInterface_FirstDs0,
       "t1NetworkProfile-LineInterface-LastDs0": t1NetworkProfile_LineInterface_LastDs0,
       "t1NetworkProfile-LineInterface-NailedGroup": t1NetworkProfile_LineInterface_NailedGroup,
       "t1NetworkProfile-LineInterface-Ss7Continuity-IncomingProcedure": t1NetworkProfile_LineInterface_Ss7Continuity_IncomingProcedure,
       "t1NetworkProfile-LineInterface-Ss7Continuity-OutgoingProcedure": t1NetworkProfile_LineInterface_Ss7Continuity_OutgoingProcedure,
       "t1NetworkProfile-LineInterface-LineProvision": t1NetworkProfile_LineInterface_LineProvision,
       "t1NetworkProfile-LineInterface-Gr303Mode": t1NetworkProfile_LineInterface_Gr303Mode,
       "t1NetworkProfile-LineInterface-Gr303GroupId": t1NetworkProfile_LineInterface_Gr303GroupId,
       "t1NetworkProfile-LineInterface-Gr303Ds1Id": t1NetworkProfile_LineInterface_Gr303Ds1Id,
       "t1NetworkProfile-LineInterface-SwitchVersion": t1NetworkProfile_LineInterface_SwitchVersion,
       "t1NetworkProfile-BackToBack": t1NetworkProfile_BackToBack,
       "t1NetworkProfile-ChannelUsage": t1NetworkProfile_ChannelUsage,
       "t1NetworkProfile-Action-o": t1NetworkProfile_Action_o,
       "t1NetworkProfile-LineInterface-GroupBNoChargeSignal": t1NetworkProfile_LineInterface_GroupBNoChargeSignal,
       "t1NetworkProfile-LineInterface-StatusChangeTrapEnable": t1NetworkProfile_LineInterface_StatusChangeTrapEnable,
       "t1NetworkProfile-LineInterface-DownTransDelay": t1NetworkProfile_LineInterface_DownTransDelay,
       "t1NetworkProfile-LineInterface-UpTransDelay": t1NetworkProfile_LineInterface_UpTransDelay,
       "t1NetworkProfile-LineInterface-NetworkSpecificFacilities": t1NetworkProfile_LineInterface_NetworkSpecificFacilities,
       "t1NetworkProfile-LineInterface-CauseCodeVerificationEnable": t1NetworkProfile_LineInterface_CauseCodeVerificationEnable,
       "mibt1NetworkProfile-LineInterface-ChannelConfigTable": mibt1NetworkProfile_LineInterface_ChannelConfigTable,
       "mibt1NetworkProfile-LineInterface-ChannelConfigEntry": mibt1NetworkProfile_LineInterface_ChannelConfigEntry,
       "t1NetworkProfile-LineInterface-ChannelConfig-Shelf-o": t1NetworkProfile_LineInterface_ChannelConfig_Shelf_o,
       "t1NetworkProfile-LineInterface-ChannelConfig-Slot-o": t1NetworkProfile_LineInterface_ChannelConfig_Slot_o,
       "t1NetworkProfile-LineInterface-ChannelConfig-Item-o": t1NetworkProfile_LineInterface_ChannelConfig_Item_o,
       "t1NetworkProfile-LineInterface-ChannelConfig-Index-o": t1NetworkProfile_LineInterface_ChannelConfig_Index_o,
       "t1NetworkProfile-LineInterface-ChannelConfig-ChannelUsage": t1NetworkProfile_LineInterface_ChannelConfig_ChannelUsage,
       "t1NetworkProfile-LineInterface-ChannelConfig-TrunkGroup": t1NetworkProfile_LineInterface_ChannelConfig_TrunkGroup,
       "t1NetworkProfile-LineInterface-ChannelConfig-PhoneNumber": t1NetworkProfile_LineInterface_ChannelConfig_PhoneNumber,
       "t1NetworkProfile-LineInterface-ChannelConfig-RoutePort-SlotNumber-SlotNumber": t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber,
       "t1NetworkProfile-LineInterface-ChannelConfig-RoutePort-SlotNumber-ShelfNumber": t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber,
       "t1NetworkProfile-LineInterface-ChannelConfig-RoutePort-RelativePortNumber-RelativePortNumber": t1NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "t1NetworkProfile-LineInterface-ChannelConfig-NailedGroup": t1NetworkProfile_LineInterface_ChannelConfig_NailedGroup,
       "t1NetworkProfile-LineInterface-ChannelConfig-ChanGroup": t1NetworkProfile_LineInterface_ChannelConfig_ChanGroup,
       "t1NetworkProfile-LineInterface-ChannelConfig-DestChanGroup": t1NetworkProfile_LineInterface_ChannelConfig_DestChanGroup,
       "t1NetworkProfile-LineInterface-ChannelConfig-DialPlanNumber": t1NetworkProfile_LineInterface_ChannelConfig_DialPlanNumber,
       "t1NetworkProfile-LineInterface-ChannelConfig-NumberOfDialPlanSelectDigits": t1NetworkProfile_LineInterface_ChannelConfig_NumberOfDialPlanSelectDigits,
       "t1NetworkProfile-LineInterface-ChannelConfig-IdlePattern": t1NetworkProfile_LineInterface_ChannelConfig_IdlePattern}
)
