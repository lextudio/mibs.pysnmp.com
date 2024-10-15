# SNMP MIB module (ASCEND-MIBDSLTHRESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDSLTHRESH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:32 2024
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

_MibdslThreshProfile_ObjectIdentity = ObjectIdentity
mibdslThreshProfile = _MibdslThreshProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 75)
)
_MibdslThreshProfileTable_Object = MibTable
mibdslThreshProfileTable = _MibdslThreshProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1)
)
if mibBuilder.loadTexts:
    mibdslThreshProfileTable.setStatus("mandatory")
_MibdslThreshProfileEntry_Object = MibTableRow
mibdslThreshProfileEntry = _MibdslThreshProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1)
)
mibdslThreshProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDSLTHRESH-MIB", "dslThreshProfile-Name"),
)
if mibBuilder.loadTexts:
    mibdslThreshProfileEntry.setStatus("mandatory")
_DslThreshProfile_Name_Type = DisplayString
_DslThreshProfile_Name_Object = MibScalar
dslThreshProfile_Name = _DslThreshProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 1),
    _DslThreshProfile_Name_Type()
)
dslThreshProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslThreshProfile_Name.setStatus("mandatory")


class _DslThreshProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type dslThreshProfile_PhysicalAddress_Shelf based on Integer32"""
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


_DslThreshProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_DslThreshProfile_PhysicalAddress_Shelf_Object = MibScalar
dslThreshProfile_PhysicalAddress_Shelf = _DslThreshProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 2),
    _DslThreshProfile_PhysicalAddress_Shelf_Type()
)
dslThreshProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _DslThreshProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type dslThreshProfile_PhysicalAddress_Slot based on Integer32"""
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


_DslThreshProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_DslThreshProfile_PhysicalAddress_Slot_Object = MibScalar
dslThreshProfile_PhysicalAddress_Slot = _DslThreshProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 3),
    _DslThreshProfile_PhysicalAddress_Slot_Type()
)
dslThreshProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_PhysicalAddress_Slot.setStatus("mandatory")
_DslThreshProfile_PhysicalAddress_ItemNumber_Type = Integer32
_DslThreshProfile_PhysicalAddress_ItemNumber_Object = MibScalar
dslThreshProfile_PhysicalAddress_ItemNumber = _DslThreshProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 4),
    _DslThreshProfile_PhysicalAddress_ItemNumber_Type()
)
dslThreshProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _DslThreshProfile_Enabled_Type(Integer32):
    """Custom type dslThreshProfile_Enabled based on Integer32"""
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


_DslThreshProfile_Enabled_Type.__name__ = "Integer32"
_DslThreshProfile_Enabled_Object = MibScalar
dslThreshProfile_Enabled = _DslThreshProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 5),
    _DslThreshProfile_Enabled_Type()
)
dslThreshProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Enabled.setStatus("mandatory")
_DslThreshProfile_Atuc15minLofs_Type = Integer32
_DslThreshProfile_Atuc15minLofs_Object = MibScalar
dslThreshProfile_Atuc15minLofs = _DslThreshProfile_Atuc15minLofs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 6),
    _DslThreshProfile_Atuc15minLofs_Type()
)
dslThreshProfile_Atuc15minLofs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Atuc15minLofs.setStatus("mandatory")
_DslThreshProfile_Atuc15minLoss_Type = Integer32
_DslThreshProfile_Atuc15minLoss_Object = MibScalar
dslThreshProfile_Atuc15minLoss = _DslThreshProfile_Atuc15minLoss_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 7),
    _DslThreshProfile_Atuc15minLoss_Type()
)
dslThreshProfile_Atuc15minLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Atuc15minLoss.setStatus("mandatory")
_DslThreshProfile_Atuc15minLols_Type = Integer32
_DslThreshProfile_Atuc15minLols_Object = MibScalar
dslThreshProfile_Atuc15minLols = _DslThreshProfile_Atuc15minLols_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 8),
    _DslThreshProfile_Atuc15minLols_Type()
)
dslThreshProfile_Atuc15minLols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Atuc15minLols.setStatus("mandatory")
_DslThreshProfile_Atuc15minLprs_Type = Integer32
_DslThreshProfile_Atuc15minLprs_Object = MibScalar
dslThreshProfile_Atuc15minLprs = _DslThreshProfile_Atuc15minLprs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 9),
    _DslThreshProfile_Atuc15minLprs_Type()
)
dslThreshProfile_Atuc15minLprs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Atuc15minLprs.setStatus("mandatory")
_DslThreshProfile_Atuc15minEss_Type = Integer32
_DslThreshProfile_Atuc15minEss_Object = MibScalar
dslThreshProfile_Atuc15minEss = _DslThreshProfile_Atuc15minEss_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 10),
    _DslThreshProfile_Atuc15minEss_Type()
)
dslThreshProfile_Atuc15minEss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Atuc15minEss.setStatus("mandatory")
_DslThreshProfile_AtucFastRateUp_Type = Integer32
_DslThreshProfile_AtucFastRateUp_Object = MibScalar
dslThreshProfile_AtucFastRateUp = _DslThreshProfile_AtucFastRateUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 11),
    _DslThreshProfile_AtucFastRateUp_Type()
)
dslThreshProfile_AtucFastRateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_AtucFastRateUp.setStatus("mandatory")
_DslThreshProfile_AtucInterleaveRateUp_Type = Integer32
_DslThreshProfile_AtucInterleaveRateUp_Object = MibScalar
dslThreshProfile_AtucInterleaveRateUp = _DslThreshProfile_AtucInterleaveRateUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 12),
    _DslThreshProfile_AtucInterleaveRateUp_Type()
)
dslThreshProfile_AtucInterleaveRateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_AtucInterleaveRateUp.setStatus("mandatory")
_DslThreshProfile_AtucFastRateDown_Type = Integer32
_DslThreshProfile_AtucFastRateDown_Object = MibScalar
dslThreshProfile_AtucFastRateDown = _DslThreshProfile_AtucFastRateDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 13),
    _DslThreshProfile_AtucFastRateDown_Type()
)
dslThreshProfile_AtucFastRateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_AtucFastRateDown.setStatus("mandatory")
_DslThreshProfile_AtucInterleaveRateDown_Type = Integer32
_DslThreshProfile_AtucInterleaveRateDown_Object = MibScalar
dslThreshProfile_AtucInterleaveRateDown = _DslThreshProfile_AtucInterleaveRateDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 14),
    _DslThreshProfile_AtucInterleaveRateDown_Type()
)
dslThreshProfile_AtucInterleaveRateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_AtucInterleaveRateDown.setStatus("mandatory")


class _DslThreshProfile_AtucInitFailureTrap_Type(Integer32):
    """Custom type dslThreshProfile_AtucInitFailureTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_DslThreshProfile_AtucInitFailureTrap_Type.__name__ = "Integer32"
_DslThreshProfile_AtucInitFailureTrap_Object = MibScalar
dslThreshProfile_AtucInitFailureTrap = _DslThreshProfile_AtucInitFailureTrap_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 15),
    _DslThreshProfile_AtucInitFailureTrap_Type()
)
dslThreshProfile_AtucInitFailureTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_AtucInitFailureTrap.setStatus("mandatory")


class _DslThreshProfile_Action_o_Type(Integer32):
    """Custom type dslThreshProfile_Action_o based on Integer32"""
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


_DslThreshProfile_Action_o_Type.__name__ = "Integer32"
_DslThreshProfile_Action_o_Object = MibScalar
dslThreshProfile_Action_o = _DslThreshProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 16),
    _DslThreshProfile_Action_o_Type()
)
dslThreshProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Action_o.setStatus("mandatory")
_DslThreshProfile_Atur15minLofs_Type = Integer32
_DslThreshProfile_Atur15minLofs_Object = MibScalar
dslThreshProfile_Atur15minLofs = _DslThreshProfile_Atur15minLofs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 17),
    _DslThreshProfile_Atur15minLofs_Type()
)
dslThreshProfile_Atur15minLofs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Atur15minLofs.setStatus("mandatory")
_DslThreshProfile_Atur15minLoss_Type = Integer32
_DslThreshProfile_Atur15minLoss_Object = MibScalar
dslThreshProfile_Atur15minLoss = _DslThreshProfile_Atur15minLoss_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 18),
    _DslThreshProfile_Atur15minLoss_Type()
)
dslThreshProfile_Atur15minLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Atur15minLoss.setStatus("mandatory")
_DslThreshProfile_Atur15minLprs_Type = Integer32
_DslThreshProfile_Atur15minLprs_Object = MibScalar
dslThreshProfile_Atur15minLprs = _DslThreshProfile_Atur15minLprs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 19),
    _DslThreshProfile_Atur15minLprs_Type()
)
dslThreshProfile_Atur15minLprs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Atur15minLprs.setStatus("mandatory")
_DslThreshProfile_Atur15minEss_Type = Integer32
_DslThreshProfile_Atur15minEss_Object = MibScalar
dslThreshProfile_Atur15minEss = _DslThreshProfile_Atur15minEss_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 20),
    _DslThreshProfile_Atur15minEss_Type()
)
dslThreshProfile_Atur15minEss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_Atur15minEss.setStatus("mandatory")
_DslThreshProfile_AturFastRateUp_Type = Integer32
_DslThreshProfile_AturFastRateUp_Object = MibScalar
dslThreshProfile_AturFastRateUp = _DslThreshProfile_AturFastRateUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 21),
    _DslThreshProfile_AturFastRateUp_Type()
)
dslThreshProfile_AturFastRateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_AturFastRateUp.setStatus("mandatory")
_DslThreshProfile_AturInterleaveRateUp_Type = Integer32
_DslThreshProfile_AturInterleaveRateUp_Object = MibScalar
dslThreshProfile_AturInterleaveRateUp = _DslThreshProfile_AturInterleaveRateUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 22),
    _DslThreshProfile_AturInterleaveRateUp_Type()
)
dslThreshProfile_AturInterleaveRateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_AturInterleaveRateUp.setStatus("mandatory")
_DslThreshProfile_AturFastRateDown_Type = Integer32
_DslThreshProfile_AturFastRateDown_Object = MibScalar
dslThreshProfile_AturFastRateDown = _DslThreshProfile_AturFastRateDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 23),
    _DslThreshProfile_AturFastRateDown_Type()
)
dslThreshProfile_AturFastRateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_AturFastRateDown.setStatus("mandatory")
_DslThreshProfile_AturInterleaveRateDown_Type = Integer32
_DslThreshProfile_AturInterleaveRateDown_Object = MibScalar
dslThreshProfile_AturInterleaveRateDown = _DslThreshProfile_AturInterleaveRateDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 75, 1, 1, 24),
    _DslThreshProfile_AturInterleaveRateDown_Type()
)
dslThreshProfile_AturInterleaveRateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslThreshProfile_AturInterleaveRateDown.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDSLTHRESH-MIB",
    **{"DisplayString": DisplayString,
       "mibdslThreshProfile": mibdslThreshProfile,
       "mibdslThreshProfileTable": mibdslThreshProfileTable,
       "mibdslThreshProfileEntry": mibdslThreshProfileEntry,
       "dslThreshProfile-Name": dslThreshProfile_Name,
       "dslThreshProfile-PhysicalAddress-Shelf": dslThreshProfile_PhysicalAddress_Shelf,
       "dslThreshProfile-PhysicalAddress-Slot": dslThreshProfile_PhysicalAddress_Slot,
       "dslThreshProfile-PhysicalAddress-ItemNumber": dslThreshProfile_PhysicalAddress_ItemNumber,
       "dslThreshProfile-Enabled": dslThreshProfile_Enabled,
       "dslThreshProfile-Atuc15minLofs": dslThreshProfile_Atuc15minLofs,
       "dslThreshProfile-Atuc15minLoss": dslThreshProfile_Atuc15minLoss,
       "dslThreshProfile-Atuc15minLols": dslThreshProfile_Atuc15minLols,
       "dslThreshProfile-Atuc15minLprs": dslThreshProfile_Atuc15minLprs,
       "dslThreshProfile-Atuc15minEss": dslThreshProfile_Atuc15minEss,
       "dslThreshProfile-AtucFastRateUp": dslThreshProfile_AtucFastRateUp,
       "dslThreshProfile-AtucInterleaveRateUp": dslThreshProfile_AtucInterleaveRateUp,
       "dslThreshProfile-AtucFastRateDown": dslThreshProfile_AtucFastRateDown,
       "dslThreshProfile-AtucInterleaveRateDown": dslThreshProfile_AtucInterleaveRateDown,
       "dslThreshProfile-AtucInitFailureTrap": dslThreshProfile_AtucInitFailureTrap,
       "dslThreshProfile-Action-o": dslThreshProfile_Action_o,
       "dslThreshProfile-Atur15minLofs": dslThreshProfile_Atur15minLofs,
       "dslThreshProfile-Atur15minLoss": dslThreshProfile_Atur15minLoss,
       "dslThreshProfile-Atur15minLprs": dslThreshProfile_Atur15minLprs,
       "dslThreshProfile-Atur15minEss": dslThreshProfile_Atur15minEss,
       "dslThreshProfile-AturFastRateUp": dslThreshProfile_AturFastRateUp,
       "dslThreshProfile-AturInterleaveRateUp": dslThreshProfile_AturInterleaveRateUp,
       "dslThreshProfile-AturFastRateDown": dslThreshProfile_AturFastRateDown,
       "dslThreshProfile-AturInterleaveRateDown": dslThreshProfile_AturInterleaveRateDown}
)
