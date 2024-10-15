# SNMP MIB module (ASCEND-MIBPORT1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBPORT1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:03 2024
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

_MibportProfile_ObjectIdentity = ObjectIdentity
mibportProfile = _MibportProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 102)
)
_MibportProfileTable_Object = MibTable
mibportProfileTable = _MibportProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1)
)
if mibBuilder.loadTexts:
    mibportProfileTable.setStatus("mandatory")
_MibportProfileEntry_Object = MibTableRow
mibportProfileEntry = _MibportProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1)
)
mibportProfileEntry.setIndexNames(
    (0, "ASCEND-MIBPORT1-MIB", "portProfile-Shelf-o"),
    (0, "ASCEND-MIBPORT1-MIB", "portProfile-Slot-o"),
    (0, "ASCEND-MIBPORT1-MIB", "portProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibportProfileEntry.setStatus("mandatory")
_PortProfile_Shelf_o_Type = Integer32
_PortProfile_Shelf_o_Object = MibScalar
portProfile_Shelf_o = _PortProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 1),
    _PortProfile_Shelf_o_Type()
)
portProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portProfile_Shelf_o.setStatus("mandatory")
_PortProfile_Slot_o_Type = Integer32
_PortProfile_Slot_o_Object = MibScalar
portProfile_Slot_o = _PortProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 2),
    _PortProfile_Slot_o_Type()
)
portProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portProfile_Slot_o.setStatus("mandatory")
_PortProfile_Item_o_Type = Integer32
_PortProfile_Item_o_Object = MibScalar
portProfile_Item_o = _PortProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 3),
    _PortProfile_Item_o_Type()
)
portProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portProfile_Item_o.setStatus("mandatory")


class _PortProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type portProfile_PhysicalAddress_Shelf based on Integer32"""
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


_PortProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_PortProfile_PhysicalAddress_Shelf_Object = MibScalar
portProfile_PhysicalAddress_Shelf = _PortProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 4),
    _PortProfile_PhysicalAddress_Shelf_Type()
)
portProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _PortProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type portProfile_PhysicalAddress_Slot based on Integer32"""
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


_PortProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_PortProfile_PhysicalAddress_Slot_Object = MibScalar
portProfile_PhysicalAddress_Slot = _PortProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 5),
    _PortProfile_PhysicalAddress_Slot_Type()
)
portProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PhysicalAddress_Slot.setStatus("mandatory")
_PortProfile_PhysicalAddress_ItemNumber_Type = Integer32
_PortProfile_PhysicalAddress_ItemNumber_Object = MibScalar
portProfile_PhysicalAddress_ItemNumber = _PortProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 6),
    _PortProfile_PhysicalAddress_ItemNumber_Type()
)
portProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")
_PortProfile_Name_Type = DisplayString
_PortProfile_Name_Object = MibScalar
portProfile_Name = _PortProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 7),
    _PortProfile_Name_Type()
)
portProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_Name.setStatus("mandatory")
_PortProfile_LastModificationTime_Type = Integer32
_PortProfile_LastModificationTime_Object = MibScalar
portProfile_LastModificationTime = _PortProfile_LastModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 8),
    _PortProfile_LastModificationTime_Type()
)
portProfile_LastModificationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_LastModificationTime.setStatus("mandatory")
_PortProfile_PortAnswerNumber1_Type = DisplayString
_PortProfile_PortAnswerNumber1_Object = MibScalar
portProfile_PortAnswerNumber1 = _PortProfile_PortAnswerNumber1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 9),
    _PortProfile_PortAnswerNumber1_Type()
)
portProfile_PortAnswerNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PortAnswerNumber1.setStatus("mandatory")
_PortProfile_PortAnswerNumber2_Type = DisplayString
_PortProfile_PortAnswerNumber2_Object = MibScalar
portProfile_PortAnswerNumber2 = _PortProfile_PortAnswerNumber2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 10),
    _PortProfile_PortAnswerNumber2_Type()
)
portProfile_PortAnswerNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PortAnswerNumber2.setStatus("mandatory")
_PortProfile_PortAnswerNumber3_Type = DisplayString
_PortProfile_PortAnswerNumber3_Object = MibScalar
portProfile_PortAnswerNumber3 = _PortProfile_PortAnswerNumber3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 11),
    _PortProfile_PortAnswerNumber3_Type()
)
portProfile_PortAnswerNumber3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PortAnswerNumber3.setStatus("mandatory")
_PortProfile_PortAnswerNumber4_Type = DisplayString
_PortProfile_PortAnswerNumber4_Object = MibScalar
portProfile_PortAnswerNumber4 = _PortProfile_PortAnswerNumber4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 12),
    _PortProfile_PortAnswerNumber4_Type()
)
portProfile_PortAnswerNumber4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PortAnswerNumber4.setStatus("mandatory")


class _PortProfile_oIdle_Type(Integer32):
    """Custom type portProfile_oIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("call", 2),
          ("none", 1))
    )


_PortProfile_oIdle_Type.__name__ = "Integer32"
_PortProfile_oIdle_Object = MibScalar
portProfile_oIdle = _PortProfile_oIdle_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 13),
    _PortProfile_oIdle_Type()
)
portProfile_oIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_oIdle.setStatus("mandatory")


class _PortProfile_oDial_Type(Integer32):
    """Custom type portProfile_oDial based on Integer32"""
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
        *(("numberOfPortDial", 10),
          ("portDialDtr", 2),
          ("portDialRs366", 3),
          ("portDialRs366x", 4),
          ("portDialTerminal", 1),
          ("portDialV25bis", 5),
          ("portDialV25bisC", 6),
          ("portDialX21", 7),
          ("portDialX21Ptel", 9),
          ("portDialX21x", 8))
    )


_PortProfile_oDial_Type.__name__ = "Integer32"
_PortProfile_oDial_Object = MibScalar
portProfile_oDial = _PortProfile_oDial_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 14),
    _PortProfile_oDial_Type()
)
portProfile_oDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_oDial.setStatus("mandatory")


class _PortProfile_PortAnswer_Type(Integer32):
    """Custom type portProfile_PortAnswer based on Integer32"""
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
        *(("numberOfPortAnswer", 10),
          ("portAnswerAuto", 1),
          ("portAnswerAutoManual", 9),
          ("portAnswerDtr", 2),
          ("portAnswerDtrRing", 3),
          ("portAnswerNone", 7),
          ("portAnswerTerminal", 6),
          ("portAnswerV25bis", 4),
          ("portAnswerV25bisC", 5),
          ("portAnswerX21", 8))
    )


_PortProfile_PortAnswer_Type.__name__ = "Integer32"
_PortProfile_PortAnswer_Object = MibScalar
portProfile_PortAnswer = _PortProfile_PortAnswer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 15),
    _PortProfile_PortAnswer_Type()
)
portProfile_PortAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PortAnswer.setStatus("mandatory")


class _PortProfile_oClear_Type(Integer32):
    """Custom type portProfile_oClear based on Integer32"""
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
        *(("dtrActive", 1),
          ("dtrInactive", 2),
          ("rtsActive", 3),
          ("rtsInactive", 4),
          ("terminal", 5))
    )


_PortProfile_oClear_Type.__name__ = "Integer32"
_PortProfile_oClear_Object = MibScalar
portProfile_oClear = _PortProfile_oClear_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 16),
    _PortProfile_oClear_Type()
)
portProfile_oClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_oClear.setStatus("mandatory")
_PortProfile_PortMinPriBw_Type = Integer32
_PortProfile_PortMinPriBw_Object = MibScalar
portProfile_PortMinPriBw = _PortProfile_PortMinPriBw_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 17),
    _PortProfile_PortMinPriBw_Type()
)
portProfile_PortMinPriBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PortMinPriBw.setStatus("mandatory")


class _PortProfile_PortTerminalTiming_Type(Integer32):
    """Custom type portProfile_PortTerminalTiming based on Integer32"""
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


_PortProfile_PortTerminalTiming_Type.__name__ = "Integer32"
_PortProfile_PortTerminalTiming_Object = MibScalar
portProfile_PortTerminalTiming = _PortProfile_PortTerminalTiming_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 18),
    _PortProfile_PortTerminalTiming_Type()
)
portProfile_PortTerminalTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PortTerminalTiming.setStatus("mandatory")


class _PortProfile_oRS366Esc_Type(Integer32):
    """Custom type portProfile_oRS366Esc based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("n-0", 7),
          ("n-00", 8),
          ("n-5", 3),
          ("n-6", 4),
          ("n-7", 5),
          ("n-9", 6),
          ("numberEsc366", 9),
          ("pound", 2),
          ("star", 1))
    )


_PortProfile_oRS366Esc_Type.__name__ = "Integer32"
_PortProfile_oRS366Esc_Object = MibScalar
portProfile_oRS366Esc = _PortProfile_oRS366Esc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 19),
    _PortProfile_oRS366Esc_Type()
)
portProfile_oRS366Esc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_oRS366Esc.setStatus("mandatory")


class _PortProfile_oEarlyCD_Type(Integer32):
    """Custom type portProfile_oEarlyCD based on Integer32"""
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
        *(("answer", 2),
          ("both", 4),
          ("none", 1),
          ("originate", 3))
    )


_PortProfile_oEarlyCD_Type.__name__ = "Integer32"
_PortProfile_oEarlyCD_Object = MibScalar
portProfile_oEarlyCD = _PortProfile_oEarlyCD_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 20),
    _PortProfile_oEarlyCD_Type()
)
portProfile_oEarlyCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_oEarlyCD.setStatus("mandatory")


class _PortProfile_PortDs0MinReset_Type(Integer32):
    """Custom type portProfile_PortDs0MinReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daily", 2),
          ("monthly", 3),
          ("off", 1))
    )


_PortProfile_PortDs0MinReset_Type.__name__ = "Integer32"
_PortProfile_PortDs0MinReset_Object = MibScalar
portProfile_PortDs0MinReset = _PortProfile_PortDs0MinReset_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 21),
    _PortProfile_PortDs0MinReset_Type()
)
portProfile_PortDs0MinReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PortDs0MinReset.setStatus("mandatory")
_PortProfile_MaxPortDs0Mins_Type = Integer32
_PortProfile_MaxPortDs0Mins_Object = MibScalar
portProfile_MaxPortDs0Mins = _PortProfile_MaxPortDs0Mins_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 22),
    _PortProfile_MaxPortDs0Mins_Type()
)
portProfile_MaxPortDs0Mins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_MaxPortDs0Mins.setStatus("mandatory")
_PortProfile_MaxCallDurationTimer_Type = Integer32
_PortProfile_MaxCallDurationTimer_Object = MibScalar
portProfile_MaxCallDurationTimer = _PortProfile_MaxCallDurationTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 23),
    _PortProfile_MaxCallDurationTimer_Type()
)
portProfile_MaxCallDurationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_MaxCallDurationTimer.setStatus("mandatory")
_PortProfile_DialPlan_Type = Integer32
_PortProfile_DialPlan_Object = MibScalar
portProfile_DialPlan = _PortProfile_DialPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 24),
    _PortProfile_DialPlan_Type()
)
portProfile_DialPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_DialPlan.setStatus("mandatory")


class _PortProfile_TrunkGroupsNa_Type(Integer32):
    """Custom type portProfile_TrunkGroupsNa based on Integer32"""
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


_PortProfile_TrunkGroupsNa_Type.__name__ = "Integer32"
_PortProfile_TrunkGroupsNa_Object = MibScalar
portProfile_TrunkGroupsNa = _PortProfile_TrunkGroupsNa_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 25),
    _PortProfile_TrunkGroupsNa_Type()
)
portProfile_TrunkGroupsNa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_TrunkGroupsNa.setStatus("mandatory")
_PortProfile_PortPassword_Type = DisplayString
_PortProfile_PortPassword_Object = MibScalar
portProfile_PortPassword = _PortProfile_PortPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 26),
    _PortProfile_PortPassword_Type()
)
portProfile_PortPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_PortPassword.setStatus("mandatory")


class _PortProfile_Action_o_Type(Integer32):
    """Custom type portProfile_Action_o based on Integer32"""
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


_PortProfile_Action_o_Type.__name__ = "Integer32"
_PortProfile_Action_o_Object = MibScalar
portProfile_Action_o = _PortProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 102, 1, 1, 27),
    _PortProfile_Action_o_Type()
)
portProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBPORT1-MIB",
    **{"DisplayString": DisplayString,
       "mibportProfile": mibportProfile,
       "mibportProfileTable": mibportProfileTable,
       "mibportProfileEntry": mibportProfileEntry,
       "portProfile-Shelf-o": portProfile_Shelf_o,
       "portProfile-Slot-o": portProfile_Slot_o,
       "portProfile-Item-o": portProfile_Item_o,
       "portProfile-PhysicalAddress-Shelf": portProfile_PhysicalAddress_Shelf,
       "portProfile-PhysicalAddress-Slot": portProfile_PhysicalAddress_Slot,
       "portProfile-PhysicalAddress-ItemNumber": portProfile_PhysicalAddress_ItemNumber,
       "portProfile-Name": portProfile_Name,
       "portProfile-LastModificationTime": portProfile_LastModificationTime,
       "portProfile-PortAnswerNumber1": portProfile_PortAnswerNumber1,
       "portProfile-PortAnswerNumber2": portProfile_PortAnswerNumber2,
       "portProfile-PortAnswerNumber3": portProfile_PortAnswerNumber3,
       "portProfile-PortAnswerNumber4": portProfile_PortAnswerNumber4,
       "portProfile-oIdle": portProfile_oIdle,
       "portProfile-oDial": portProfile_oDial,
       "portProfile-PortAnswer": portProfile_PortAnswer,
       "portProfile-oClear": portProfile_oClear,
       "portProfile-PortMinPriBw": portProfile_PortMinPriBw,
       "portProfile-PortTerminalTiming": portProfile_PortTerminalTiming,
       "portProfile-oRS366Esc": portProfile_oRS366Esc,
       "portProfile-oEarlyCD": portProfile_oEarlyCD,
       "portProfile-PortDs0MinReset": portProfile_PortDs0MinReset,
       "portProfile-MaxPortDs0Mins": portProfile_MaxPortDs0Mins,
       "portProfile-MaxCallDurationTimer": portProfile_MaxCallDurationTimer,
       "portProfile-DialPlan": portProfile_DialPlan,
       "portProfile-TrunkGroupsNa": portProfile_TrunkGroupsNa,
       "portProfile-PortPassword": portProfile_PortPassword,
       "portProfile-Action-o": portProfile_Action_o}
)
