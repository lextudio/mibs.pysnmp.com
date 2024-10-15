# SNMP MIB module (ASCEND-MIBDS1ATMNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDS1ATMNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:29 2024
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

_Mibds1AtmNetworkProfile_ObjectIdentity = ObjectIdentity
mibds1AtmNetworkProfile = _Mibds1AtmNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 25)
)
_Mibds1AtmNetworkProfileTable_Object = MibTable
mibds1AtmNetworkProfileTable = _Mibds1AtmNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1)
)
if mibBuilder.loadTexts:
    mibds1AtmNetworkProfileTable.setStatus("mandatory")
_Mibds1AtmNetworkProfileEntry_Object = MibTableRow
mibds1AtmNetworkProfileEntry = _Mibds1AtmNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1)
)
mibds1AtmNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDS1ATMNET-MIB", "ds1AtmNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBDS1ATMNET-MIB", "ds1AtmNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBDS1ATMNET-MIB", "ds1AtmNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibds1AtmNetworkProfileEntry.setStatus("mandatory")
_Ds1AtmNetworkProfile_Shelf_o_Type = Integer32
_Ds1AtmNetworkProfile_Shelf_o_Object = MibScalar
ds1AtmNetworkProfile_Shelf_o = _Ds1AtmNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 1),
    _Ds1AtmNetworkProfile_Shelf_o_Type()
)
ds1AtmNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_Shelf_o.setStatus("mandatory")
_Ds1AtmNetworkProfile_Slot_o_Type = Integer32
_Ds1AtmNetworkProfile_Slot_o_Object = MibScalar
ds1AtmNetworkProfile_Slot_o = _Ds1AtmNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 2),
    _Ds1AtmNetworkProfile_Slot_o_Type()
)
ds1AtmNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_Slot_o.setStatus("mandatory")
_Ds1AtmNetworkProfile_Item_o_Type = Integer32
_Ds1AtmNetworkProfile_Item_o_Object = MibScalar
ds1AtmNetworkProfile_Item_o = _Ds1AtmNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 3),
    _Ds1AtmNetworkProfile_Item_o_Type()
)
ds1AtmNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_Item_o.setStatus("mandatory")
_Ds1AtmNetworkProfile_Name_Type = DisplayString
_Ds1AtmNetworkProfile_Name_Object = MibScalar
ds1AtmNetworkProfile_Name = _Ds1AtmNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 4),
    _Ds1AtmNetworkProfile_Name_Type()
)
ds1AtmNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_Name.setStatus("mandatory")


class _Ds1AtmNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_Ds1AtmNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
ds1AtmNetworkProfile_PhysicalAddress_Shelf = _Ds1AtmNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 5),
    _Ds1AtmNetworkProfile_PhysicalAddress_Shelf_Type()
)
ds1AtmNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _Ds1AtmNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_Ds1AtmNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
ds1AtmNetworkProfile_PhysicalAddress_Slot = _Ds1AtmNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 6),
    _Ds1AtmNetworkProfile_PhysicalAddress_Slot_Type()
)
ds1AtmNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_Ds1AtmNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_Ds1AtmNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
ds1AtmNetworkProfile_PhysicalAddress_ItemNumber = _Ds1AtmNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 7),
    _Ds1AtmNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
ds1AtmNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _Ds1AtmNetworkProfile_Enabled_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_Enabled based on Integer32"""
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


_Ds1AtmNetworkProfile_Enabled_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_Enabled_Object = MibScalar
ds1AtmNetworkProfile_Enabled = _Ds1AtmNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 8),
    _Ds1AtmNetworkProfile_Enabled_Type()
)
ds1AtmNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_Enabled.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_FrameType_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_FrameType based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_FrameType_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_FrameType_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_FrameType = _Ds1AtmNetworkProfile_LineConfig_FrameType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 9),
    _Ds1AtmNetworkProfile_LineConfig_FrameType_Type()
)
ds1AtmNetworkProfile_LineConfig_FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_FrameType.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_Encoding_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_Encoding based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_Encoding_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_Encoding_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_Encoding = _Ds1AtmNetworkProfile_LineConfig_Encoding_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 10),
    _Ds1AtmNetworkProfile_LineConfig_Encoding_Type()
)
ds1AtmNetworkProfile_LineConfig_Encoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_Encoding.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_NailedGroup = _Ds1AtmNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 11),
    _Ds1AtmNetworkProfile_LineConfig_NailedGroup_Type()
)
ds1AtmNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_Loopback_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_Loopback based on Integer32"""
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
        *(("feLoopback", 2),
          ("lineLoopback", 3),
          ("localLoopback", 5),
          ("noLoopback", 1),
          ("remoteLoopback", 4))
    )


_Ds1AtmNetworkProfile_LineConfig_Loopback_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_Loopback_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_Loopback = _Ds1AtmNetworkProfile_LineConfig_Loopback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 12),
    _Ds1AtmNetworkProfile_LineConfig_Loopback_Type()
)
ds1AtmNetworkProfile_LineConfig_Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_Loopback.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_ClockSource_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_ClockSource based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_ClockSource_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_ClockSource_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ClockSource = _Ds1AtmNetworkProfile_LineConfig_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 13),
    _Ds1AtmNetworkProfile_LineConfig_ClockSource_Type()
)
ds1AtmNetworkProfile_LineConfig_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ClockSource.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_ClockPriority_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_ClockPriority based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_ClockPriority_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_ClockPriority_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ClockPriority = _Ds1AtmNetworkProfile_LineConfig_ClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 14),
    _Ds1AtmNetworkProfile_LineConfig_ClockPriority_Type()
)
ds1AtmNetworkProfile_LineConfig_ClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ClockPriority.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_oFDL_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_oFDL based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_oFDL_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_oFDL_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_oFDL = _Ds1AtmNetworkProfile_LineConfig_oFDL_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 15),
    _Ds1AtmNetworkProfile_LineConfig_oFDL_Type()
)
ds1AtmNetworkProfile_LineConfig_oFDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_oFDL.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_FrontEndType_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_FrontEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longHaul", 2),
          ("shortHaul", 1))
    )


_Ds1AtmNetworkProfile_LineConfig_FrontEndType_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_FrontEndType_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_FrontEndType = _Ds1AtmNetworkProfile_LineConfig_FrontEndType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 16),
    _Ds1AtmNetworkProfile_LineConfig_FrontEndType_Type()
)
ds1AtmNetworkProfile_LineConfig_FrontEndType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_FrontEndType.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_PcmMode_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_PcmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 25),
          ("isdn", 24))
    )


_Ds1AtmNetworkProfile_LineConfig_PcmMode_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_PcmMode_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_PcmMode = _Ds1AtmNetworkProfile_LineConfig_PcmMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 18),
    _Ds1AtmNetworkProfile_LineConfig_PcmMode_Type()
)
ds1AtmNetworkProfile_LineConfig_PcmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_PcmMode.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_CosetEnabled_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_CosetEnabled based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_CosetEnabled_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_CosetEnabled_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_CosetEnabled = _Ds1AtmNetworkProfile_LineConfig_CosetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 19),
    _Ds1AtmNetworkProfile_LineConfig_CosetEnabled_Type()
)
ds1AtmNetworkProfile_LineConfig_CosetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_CosetEnabled.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_ScramblingEnabled_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_ScramblingEnabled based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_ScramblingEnabled_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_ScramblingEnabled_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ScramblingEnabled = _Ds1AtmNetworkProfile_LineConfig_ScramblingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 20),
    _Ds1AtmNetworkProfile_LineConfig_ScramblingEnabled_Type()
)
ds1AtmNetworkProfile_LineConfig_ScramblingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ScramblingEnabled.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_HecCorrectionEnabled_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_HecCorrectionEnabled based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_HecCorrectionEnabled_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_HecCorrectionEnabled_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_HecCorrectionEnabled = _Ds1AtmNetworkProfile_LineConfig_HecCorrectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 21),
    _Ds1AtmNetworkProfile_LineConfig_HecCorrectionEnabled_Type()
)
ds1AtmNetworkProfile_LineConfig_HecCorrectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_HecCorrectionEnabled.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_VpSwitchingVpi_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_VpSwitchingVpi_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_VpSwitchingVpi = _Ds1AtmNetworkProfile_LineConfig_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 22),
    _Ds1AtmNetworkProfile_LineConfig_VpSwitchingVpi_Type()
)
ds1AtmNetworkProfile_LineConfig_VpSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_VpSwitchingVpi.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_NeTxLid_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_NeTxLid_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_NeTxLid = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_NeTxLid_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 23),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_NeTxLid_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_NeTxLid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_NeTxLid.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_AddLinkCondTime_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_AddLinkCondTime_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_AddLinkCondTime = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_AddLinkCondTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 24),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_AddLinkCondTime_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_AddLinkCondTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_AddLinkCondTime.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_LinkRecoveryType_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_LinkRecoveryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fast", 4),
          ("manual", 2),
          ("slow", 3))
    )


_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_LinkRecoveryType_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_LinkRecoveryType_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_LinkRecoveryType = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_LinkRecoveryType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 25),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_LinkRecoveryType_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_LinkRecoveryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_LinkRecoveryType.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingType_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("manual", 2))
    )


_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingType_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingType_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingType = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 26),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingType_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingType.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingTime_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingTime_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingTime = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 27),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingTime_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingTime.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_Priority_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_Priority_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_Priority = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_Priority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 28),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_Priority_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_Priority.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_AddLinkCondTime_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_AddLinkCondTime_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_AddLinkCondTime = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_AddLinkCondTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 29),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_AddLinkCondTime_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_AddLinkCondTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_AddLinkCondTime.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_LinkRecoveryType_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_LinkRecoveryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fast", 4),
          ("manual", 2),
          ("slow", 3))
    )


_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_LinkRecoveryType_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_LinkRecoveryType_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_LinkRecoveryType = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_LinkRecoveryType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 30),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_LinkRecoveryType_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_LinkRecoveryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_LinkRecoveryType.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RecLinkCondTime_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RecLinkCondTime_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RecLinkCondTime = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RecLinkCondTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 31),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RecLinkCondTime_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RecLinkCondTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RecLinkCondTime.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RxLidLearningTime_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RxLidLearningTime_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RxLidLearningTime = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RxLidLearningTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 32),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RxLidLearningTime_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RxLidLearningTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RxLidLearningTime.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingType_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("manual", 2))
    )


_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingType_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingType_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingType = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 33),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingType_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingType.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingTime_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingTime_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingTime = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 34),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingTime_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingTime.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_InDefectIntTime_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_InDefectIntTime_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_InDefectIntTime = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_InDefectIntTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 35),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_InDefectIntTime_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_InDefectIntTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_InDefectIntTime.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_OutDefectIntTime_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_OutDefectIntTime_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_OutDefectIntTime = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_OutDefectIntTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 36),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_OutDefectIntTime_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_OutDefectIntTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_OutDefectIntTime.setStatus("mandatory")
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_DefectRatio_Type = Integer32
_Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_DefectRatio_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_DefectRatio = _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_DefectRatio_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 37),
    _Ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_DefectRatio_Type()
)
ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_DefectRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_DefectRatio.setStatus("mandatory")


class _Ds1AtmNetworkProfile_Action_o_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_Action_o based on Integer32"""
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


_Ds1AtmNetworkProfile_Action_o_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_Action_o_Object = MibScalar
ds1AtmNetworkProfile_Action_o = _Ds1AtmNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 38),
    _Ds1AtmNetworkProfile_Action_o_Type()
)
ds1AtmNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_Action_o.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_LineLength_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_LineLength based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_LineLength_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_LineLength_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_LineLength = _Ds1AtmNetworkProfile_LineConfig_LineLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 39),
    _Ds1AtmNetworkProfile_LineConfig_LineLength_Type()
)
ds1AtmNetworkProfile_LineConfig_LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_LineLength.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_LineBuildOut_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_LineBuildOut based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_LineBuildOut_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_LineBuildOut_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_LineBuildOut = _Ds1AtmNetworkProfile_LineConfig_LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 40),
    _Ds1AtmNetworkProfile_LineConfig_LineBuildOut_Type()
)
ds1AtmNetworkProfile_LineConfig_LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_LineBuildOut.setStatus("mandatory")


class _Ds1AtmNetworkProfile_SparingMode_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_SparingMode based on Integer32"""
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


_Ds1AtmNetworkProfile_SparingMode_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_SparingMode_Object = MibScalar
ds1AtmNetworkProfile_SparingMode = _Ds1AtmNetworkProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 41),
    _Ds1AtmNetworkProfile_SparingMode_Type()
)
ds1AtmNetworkProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_SparingMode.setStatus("mandatory")


class _Ds1AtmNetworkProfile_IgnoreLineup_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_IgnoreLineup based on Integer32"""
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


_Ds1AtmNetworkProfile_IgnoreLineup_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_IgnoreLineup_Object = MibScalar
ds1AtmNetworkProfile_IgnoreLineup = _Ds1AtmNetworkProfile_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 42),
    _Ds1AtmNetworkProfile_IgnoreLineup_Type()
)
ds1AtmNetworkProfile_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_IgnoreLineup.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_SendCode_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_SendCode based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("allOnesPattern", 9),
          ("allZerosPattern", 10),
          ("altOnesZerosPattern", 11),
          ("dblAltOnesZerosPattern", 12),
          ("inbandloopCode", 14),
          ("lineCode", 2),
          ("n-1In16Pattern", 8),
          ("n-2Pow20Pattern", 13),
          ("n-3In24Pattern", 7),
          ("n-511Pattern", 6),
          ("noCode", 1),
          ("payloadCode", 3),
          ("qrsCode", 5),
          ("resetCode", 4))
    )


_Ds1AtmNetworkProfile_LineConfig_SendCode_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_SendCode_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_SendCode = _Ds1AtmNetworkProfile_LineConfig_SendCode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 43),
    _Ds1AtmNetworkProfile_LineConfig_SendCode_Type()
)
ds1AtmNetworkProfile_LineConfig_SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_SendCode.setStatus("mandatory")


class _Ds1AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Type(Integer32):
    """Custom type ds1AtmNetworkProfile_LineConfig_StatusChangeTrapEnable based on Integer32"""
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


_Ds1AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Type.__name__ = "Integer32"
_Ds1AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Object = MibScalar
ds1AtmNetworkProfile_LineConfig_StatusChangeTrapEnable = _Ds1AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 25, 1, 1, 44),
    _Ds1AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Type()
)
ds1AtmNetworkProfile_LineConfig_StatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1AtmNetworkProfile_LineConfig_StatusChangeTrapEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDS1ATMNET-MIB",
    **{"DisplayString": DisplayString,
       "mibds1AtmNetworkProfile": mibds1AtmNetworkProfile,
       "mibds1AtmNetworkProfileTable": mibds1AtmNetworkProfileTable,
       "mibds1AtmNetworkProfileEntry": mibds1AtmNetworkProfileEntry,
       "ds1AtmNetworkProfile-Shelf-o": ds1AtmNetworkProfile_Shelf_o,
       "ds1AtmNetworkProfile-Slot-o": ds1AtmNetworkProfile_Slot_o,
       "ds1AtmNetworkProfile-Item-o": ds1AtmNetworkProfile_Item_o,
       "ds1AtmNetworkProfile-Name": ds1AtmNetworkProfile_Name,
       "ds1AtmNetworkProfile-PhysicalAddress-Shelf": ds1AtmNetworkProfile_PhysicalAddress_Shelf,
       "ds1AtmNetworkProfile-PhysicalAddress-Slot": ds1AtmNetworkProfile_PhysicalAddress_Slot,
       "ds1AtmNetworkProfile-PhysicalAddress-ItemNumber": ds1AtmNetworkProfile_PhysicalAddress_ItemNumber,
       "ds1AtmNetworkProfile-Enabled": ds1AtmNetworkProfile_Enabled,
       "ds1AtmNetworkProfile-LineConfig-FrameType": ds1AtmNetworkProfile_LineConfig_FrameType,
       "ds1AtmNetworkProfile-LineConfig-Encoding": ds1AtmNetworkProfile_LineConfig_Encoding,
       "ds1AtmNetworkProfile-LineConfig-NailedGroup": ds1AtmNetworkProfile_LineConfig_NailedGroup,
       "ds1AtmNetworkProfile-LineConfig-Loopback": ds1AtmNetworkProfile_LineConfig_Loopback,
       "ds1AtmNetworkProfile-LineConfig-ClockSource": ds1AtmNetworkProfile_LineConfig_ClockSource,
       "ds1AtmNetworkProfile-LineConfig-ClockPriority": ds1AtmNetworkProfile_LineConfig_ClockPriority,
       "ds1AtmNetworkProfile-LineConfig-oFDL": ds1AtmNetworkProfile_LineConfig_oFDL,
       "ds1AtmNetworkProfile-LineConfig-FrontEndType": ds1AtmNetworkProfile_LineConfig_FrontEndType,
       "ds1AtmNetworkProfile-LineConfig-PcmMode": ds1AtmNetworkProfile_LineConfig_PcmMode,
       "ds1AtmNetworkProfile-LineConfig-CosetEnabled": ds1AtmNetworkProfile_LineConfig_CosetEnabled,
       "ds1AtmNetworkProfile-LineConfig-ScramblingEnabled": ds1AtmNetworkProfile_LineConfig_ScramblingEnabled,
       "ds1AtmNetworkProfile-LineConfig-HecCorrectionEnabled": ds1AtmNetworkProfile_LineConfig_HecCorrectionEnabled,
       "ds1AtmNetworkProfile-LineConfig-VpSwitchingVpi": ds1AtmNetworkProfile_LineConfig_VpSwitchingVpi,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-TxlinkConfig-NeTxLid": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_NeTxLid,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-TxlinkConfig-AddLinkCondTime": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_AddLinkCondTime,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-TxlinkConfig-LinkRecoveryType": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_LinkRecoveryType,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-TxlinkConfig-FaultClearingType": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingType,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-TxlinkConfig-FaultClearingTime": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_FaultClearingTime,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-TxlinkConfig-Priority": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_TxlinkConfig_Priority,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-RxlinkConfig-AddLinkCondTime": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_AddLinkCondTime,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-RxlinkConfig-LinkRecoveryType": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_LinkRecoveryType,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-RxlinkConfig-RecLinkCondTime": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RecLinkCondTime,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-RxlinkConfig-RxLidLearningTime": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_RxLidLearningTime,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-RxlinkConfig-FaultClearingType": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingType,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-RxlinkConfig-FaultClearingTime": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_FaultClearingTime,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-RxlinkConfig-InDefectIntTime": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_InDefectIntTime,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-RxlinkConfig-OutDefectIntTime": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_OutDefectIntTime,
       "ds1AtmNetworkProfile-LineConfig-ImaOptionConfig-RxlinkConfig-DefectRatio": ds1AtmNetworkProfile_LineConfig_ImaOptionConfig_RxlinkConfig_DefectRatio,
       "ds1AtmNetworkProfile-Action-o": ds1AtmNetworkProfile_Action_o,
       "ds1AtmNetworkProfile-LineConfig-LineLength": ds1AtmNetworkProfile_LineConfig_LineLength,
       "ds1AtmNetworkProfile-LineConfig-LineBuildOut": ds1AtmNetworkProfile_LineConfig_LineBuildOut,
       "ds1AtmNetworkProfile-SparingMode": ds1AtmNetworkProfile_SparingMode,
       "ds1AtmNetworkProfile-IgnoreLineup": ds1AtmNetworkProfile_IgnoreLineup,
       "ds1AtmNetworkProfile-LineConfig-SendCode": ds1AtmNetworkProfile_LineConfig_SendCode,
       "ds1AtmNetworkProfile-LineConfig-StatusChangeTrapEnable": ds1AtmNetworkProfile_LineConfig_StatusChangeTrapEnable}
)
