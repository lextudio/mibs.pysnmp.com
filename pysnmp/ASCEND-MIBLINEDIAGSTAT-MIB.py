# SNMP MIB module (ASCEND-MIBLINEDIAGSTAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBLINEDIAGSTAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:51 2024
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

_MibmibProfLineDiagStat_ObjectIdentity = ObjectIdentity
mibmibProfLineDiagStat = _MibmibProfLineDiagStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 146)
)
_MibmibProfLineDiagStatTable_Object = MibTable
mibmibProfLineDiagStatTable = _MibmibProfLineDiagStatTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1)
)
if mibBuilder.loadTexts:
    mibmibProfLineDiagStatTable.setStatus("mandatory")
_MibmibProfLineDiagStatEntry_Object = MibTableRow
mibmibProfLineDiagStatEntry = _MibmibProfLineDiagStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1)
)
mibmibProfLineDiagStatEntry.setIndexNames(
    (0, "ASCEND-MIBLINEDIAGSTAT-MIB", "mibProfLineDiagStat-Shelf-o"),
    (0, "ASCEND-MIBLINEDIAGSTAT-MIB", "mibProfLineDiagStat-Slot-o"),
    (0, "ASCEND-MIBLINEDIAGSTAT-MIB", "mibProfLineDiagStat-Item-o"),
)
if mibBuilder.loadTexts:
    mibmibProfLineDiagStatEntry.setStatus("mandatory")
_MibProfLineDiagStat_Shelf_o_Type = Integer32
_MibProfLineDiagStat_Shelf_o_Object = MibScalar
mibProfLineDiagStat_Shelf_o = _MibProfLineDiagStat_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 1),
    _MibProfLineDiagStat_Shelf_o_Type()
)
mibProfLineDiagStat_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_Shelf_o.setStatus("mandatory")
_MibProfLineDiagStat_Slot_o_Type = Integer32
_MibProfLineDiagStat_Slot_o_Object = MibScalar
mibProfLineDiagStat_Slot_o = _MibProfLineDiagStat_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 2),
    _MibProfLineDiagStat_Slot_o_Type()
)
mibProfLineDiagStat_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_Slot_o.setStatus("mandatory")
_MibProfLineDiagStat_Item_o_Type = Integer32
_MibProfLineDiagStat_Item_o_Object = MibScalar
mibProfLineDiagStat_Item_o = _MibProfLineDiagStat_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 3),
    _MibProfLineDiagStat_Item_o_Type()
)
mibProfLineDiagStat_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_Item_o.setStatus("mandatory")


class _MibProfLineDiagStat_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type mibProfLineDiagStat_PhysicalAddress_Shelf based on Integer32"""
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


_MibProfLineDiagStat_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_MibProfLineDiagStat_PhysicalAddress_Shelf_Object = MibScalar
mibProfLineDiagStat_PhysicalAddress_Shelf = _MibProfLineDiagStat_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 4),
    _MibProfLineDiagStat_PhysicalAddress_Shelf_Type()
)
mibProfLineDiagStat_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_PhysicalAddress_Shelf.setStatus("mandatory")


class _MibProfLineDiagStat_PhysicalAddress_Slot_Type(Integer32):
    """Custom type mibProfLineDiagStat_PhysicalAddress_Slot based on Integer32"""
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


_MibProfLineDiagStat_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_MibProfLineDiagStat_PhysicalAddress_Slot_Object = MibScalar
mibProfLineDiagStat_PhysicalAddress_Slot = _MibProfLineDiagStat_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 5),
    _MibProfLineDiagStat_PhysicalAddress_Slot_Type()
)
mibProfLineDiagStat_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_PhysicalAddress_Slot.setStatus("mandatory")
_MibProfLineDiagStat_PhysicalAddress_ItemNumber_Type = Integer32
_MibProfLineDiagStat_PhysicalAddress_ItemNumber_Object = MibScalar
mibProfLineDiagStat_PhysicalAddress_ItemNumber = _MibProfLineDiagStat_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 6),
    _MibProfLineDiagStat_PhysicalAddress_ItemNumber_Type()
)
mibProfLineDiagStat_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _MibProfLineDiagStat_BertOperationState_Type(Integer32):
    """Custom type mibProfLineDiagStat_BertOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("active", 4),
          ("dataOverflow", 8),
          ("localLoopActive", 3),
          ("loopBackSetup", 6),
          ("n-511SyncLoss", 9),
          ("pendingActive", 13),
          ("startUp", 7),
          ("stopped", 5),
          ("waitForLoopBack", 14),
          ("waiting", 12),
          ("waitingFor511Sync", 2),
          ("waitingForBertTxToSettle", 11),
          ("waitingForRemoteNodeToEnterBert", 10))
    )


_MibProfLineDiagStat_BertOperationState_Type.__name__ = "Integer32"
_MibProfLineDiagStat_BertOperationState_Object = MibScalar
mibProfLineDiagStat_BertOperationState = _MibProfLineDiagStat_BertOperationState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 7),
    _MibProfLineDiagStat_BertOperationState_Type()
)
mibProfLineDiagStat_BertOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_BertOperationState.setStatus("mandatory")


class _MibProfLineDiagStat_IdtOperationState_Type(Integer32):
    """Custom type mibProfLineDiagStat_IdtOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("stopped", 3))
    )


_MibProfLineDiagStat_IdtOperationState_Type.__name__ = "Integer32"
_MibProfLineDiagStat_IdtOperationState_Object = MibScalar
mibProfLineDiagStat_IdtOperationState = _MibProfLineDiagStat_IdtOperationState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 8),
    _MibProfLineDiagStat_IdtOperationState_Type()
)
mibProfLineDiagStat_IdtOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_IdtOperationState.setStatus("mandatory")
_MibProfLineDiagStat_BertErrorCounter_Type = Integer32
_MibProfLineDiagStat_BertErrorCounter_Object = MibScalar
mibProfLineDiagStat_BertErrorCounter = _MibProfLineDiagStat_BertErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 9),
    _MibProfLineDiagStat_BertErrorCounter_Type()
)
mibProfLineDiagStat_BertErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_BertErrorCounter.setStatus("mandatory")
_MibProfLineDiagStat_IdtSendCount_Type = Integer32
_MibProfLineDiagStat_IdtSendCount_Object = MibScalar
mibProfLineDiagStat_IdtSendCount = _MibProfLineDiagStat_IdtSendCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 10),
    _MibProfLineDiagStat_IdtSendCount_Type()
)
mibProfLineDiagStat_IdtSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_IdtSendCount.setStatus("mandatory")
_MibProfLineDiagStat_IdtRecvCount_Type = Integer32
_MibProfLineDiagStat_IdtRecvCount_Object = MibScalar
mibProfLineDiagStat_IdtRecvCount = _MibProfLineDiagStat_IdtRecvCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 11),
    _MibProfLineDiagStat_IdtRecvCount_Type()
)
mibProfLineDiagStat_IdtRecvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_IdtRecvCount.setStatus("mandatory")
_MibProfLineDiagStat_IdtErrorCounter_Type = Integer32
_MibProfLineDiagStat_IdtErrorCounter_Object = MibScalar
mibProfLineDiagStat_IdtErrorCounter = _MibProfLineDiagStat_IdtErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 12),
    _MibProfLineDiagStat_IdtErrorCounter_Type()
)
mibProfLineDiagStat_IdtErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_IdtErrorCounter.setStatus("mandatory")


class _MibProfLineDiagStat_Action_o_Type(Integer32):
    """Custom type mibProfLineDiagStat_Action_o based on Integer32"""
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


_MibProfLineDiagStat_Action_o_Type.__name__ = "Integer32"
_MibProfLineDiagStat_Action_o_Object = MibScalar
mibProfLineDiagStat_Action_o = _MibProfLineDiagStat_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 146, 1, 1, 13),
    _MibProfLineDiagStat_Action_o_Type()
)
mibProfLineDiagStat_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiagStat_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBLINEDIAGSTAT-MIB",
    **{"DisplayString": DisplayString,
       "mibmibProfLineDiagStat": mibmibProfLineDiagStat,
       "mibmibProfLineDiagStatTable": mibmibProfLineDiagStatTable,
       "mibmibProfLineDiagStatEntry": mibmibProfLineDiagStatEntry,
       "mibProfLineDiagStat-Shelf-o": mibProfLineDiagStat_Shelf_o,
       "mibProfLineDiagStat-Slot-o": mibProfLineDiagStat_Slot_o,
       "mibProfLineDiagStat-Item-o": mibProfLineDiagStat_Item_o,
       "mibProfLineDiagStat-PhysicalAddress-Shelf": mibProfLineDiagStat_PhysicalAddress_Shelf,
       "mibProfLineDiagStat-PhysicalAddress-Slot": mibProfLineDiagStat_PhysicalAddress_Slot,
       "mibProfLineDiagStat-PhysicalAddress-ItemNumber": mibProfLineDiagStat_PhysicalAddress_ItemNumber,
       "mibProfLineDiagStat-BertOperationState": mibProfLineDiagStat_BertOperationState,
       "mibProfLineDiagStat-IdtOperationState": mibProfLineDiagStat_IdtOperationState,
       "mibProfLineDiagStat-BertErrorCounter": mibProfLineDiagStat_BertErrorCounter,
       "mibProfLineDiagStat-IdtSendCount": mibProfLineDiagStat_IdtSendCount,
       "mibProfLineDiagStat-IdtRecvCount": mibProfLineDiagStat_IdtRecvCount,
       "mibProfLineDiagStat-IdtErrorCounter": mibProfLineDiagStat_IdtErrorCounter,
       "mibProfLineDiagStat-Action-o": mibProfLineDiagStat_Action_o}
)
