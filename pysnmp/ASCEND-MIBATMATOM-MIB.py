# SNMP MIB module (ASCEND-MIBATMATOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMATOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:06 2024
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

_MibatmVplProfile_ObjectIdentity = ObjectIdentity
mibatmVplProfile = _MibatmVplProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 38)
)
_MibatmVplProfileTable_Object = MibTable
mibatmVplProfileTable = _MibatmVplProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1)
)
if mibBuilder.loadTexts:
    mibatmVplProfileTable.setStatus("mandatory")
_MibatmVplProfileEntry_Object = MibTableRow
mibatmVplProfileEntry = _MibatmVplProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1)
)
mibatmVplProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMATOM-MIB", "atmVplProfile-Id-Address-PhysicalAddress-Shelf"),
    (0, "ASCEND-MIBATMATOM-MIB", "atmVplProfile-Id-Address-PhysicalAddress-Slot"),
    (0, "ASCEND-MIBATMATOM-MIB", "atmVplProfile-Id-Address-PhysicalAddress-ItemNumber"),
    (0, "ASCEND-MIBATMATOM-MIB", "atmVplProfile-Id-Address-LogicalItem"),
    (0, "ASCEND-MIBATMATOM-MIB", "atmVplProfile-Id-Vpi"),
)
if mibBuilder.loadTexts:
    mibatmVplProfileEntry.setStatus("mandatory")
_AtmVplProfile_Id_Address_PhysicalAddress_Shelf_Type = Integer32
_AtmVplProfile_Id_Address_PhysicalAddress_Shelf_Object = MibScalar
atmVplProfile_Id_Address_PhysicalAddress_Shelf = _AtmVplProfile_Id_Address_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 1),
    _AtmVplProfile_Id_Address_PhysicalAddress_Shelf_Type()
)
atmVplProfile_Id_Address_PhysicalAddress_Shelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplProfile_Id_Address_PhysicalAddress_Shelf.setStatus("mandatory")
_AtmVplProfile_Id_Address_PhysicalAddress_Slot_Type = Integer32
_AtmVplProfile_Id_Address_PhysicalAddress_Slot_Object = MibScalar
atmVplProfile_Id_Address_PhysicalAddress_Slot = _AtmVplProfile_Id_Address_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 2),
    _AtmVplProfile_Id_Address_PhysicalAddress_Slot_Type()
)
atmVplProfile_Id_Address_PhysicalAddress_Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplProfile_Id_Address_PhysicalAddress_Slot.setStatus("mandatory")
_AtmVplProfile_Id_Address_PhysicalAddress_ItemNumber_Type = Integer32
_AtmVplProfile_Id_Address_PhysicalAddress_ItemNumber_Object = MibScalar
atmVplProfile_Id_Address_PhysicalAddress_ItemNumber = _AtmVplProfile_Id_Address_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 3),
    _AtmVplProfile_Id_Address_PhysicalAddress_ItemNumber_Type()
)
atmVplProfile_Id_Address_PhysicalAddress_ItemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplProfile_Id_Address_PhysicalAddress_ItemNumber.setStatus("mandatory")
_AtmVplProfile_Id_Address_LogicalItem_Type = Integer32
_AtmVplProfile_Id_Address_LogicalItem_Object = MibScalar
atmVplProfile_Id_Address_LogicalItem = _AtmVplProfile_Id_Address_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 4),
    _AtmVplProfile_Id_Address_LogicalItem_Type()
)
atmVplProfile_Id_Address_LogicalItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplProfile_Id_Address_LogicalItem.setStatus("mandatory")
_AtmVplProfile_Id_Vpi_Type = Integer32
_AtmVplProfile_Id_Vpi_Object = MibScalar
atmVplProfile_Id_Vpi = _AtmVplProfile_Id_Vpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 5),
    _AtmVplProfile_Id_Vpi_Type()
)
atmVplProfile_Id_Vpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplProfile_Id_Vpi.setStatus("mandatory")
_AtmVplProfile_RxTrafficDesc_Type = Integer32
_AtmVplProfile_RxTrafficDesc_Object = MibScalar
atmVplProfile_RxTrafficDesc = _AtmVplProfile_RxTrafficDesc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 6),
    _AtmVplProfile_RxTrafficDesc_Type()
)
atmVplProfile_RxTrafficDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplProfile_RxTrafficDesc.setStatus("mandatory")
_AtmVplProfile_TxTrafficDesc_Type = Integer32
_AtmVplProfile_TxTrafficDesc_Object = MibScalar
atmVplProfile_TxTrafficDesc = _AtmVplProfile_TxTrafficDesc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 7),
    _AtmVplProfile_TxTrafficDesc_Type()
)
atmVplProfile_TxTrafficDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplProfile_TxTrafficDesc.setStatus("mandatory")


class _AtmVplProfile_McastType_Type(Integer32):
    """Custom type atmVplProfile_McastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("p2mpleaf", 4),
          ("p2mproot", 3),
          ("p2p", 2))
    )


_AtmVplProfile_McastType_Type.__name__ = "Integer32"
_AtmVplProfile_McastType_Object = MibScalar
atmVplProfile_McastType = _AtmVplProfile_McastType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 8),
    _AtmVplProfile_McastType_Type()
)
atmVplProfile_McastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplProfile_McastType.setStatus("mandatory")


class _AtmVplProfile_CallKind_Type(Integer32):
    """Custom type atmVplProfile_CallKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 2),
          ("spvcInitiator", 5),
          ("spvcTarget", 6),
          ("svcIncoming", 3),
          ("svcOutgoing", 4))
    )


_AtmVplProfile_CallKind_Type.__name__ = "Integer32"
_AtmVplProfile_CallKind_Object = MibScalar
atmVplProfile_CallKind = _AtmVplProfile_CallKind_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 9),
    _AtmVplProfile_CallKind_Type()
)
atmVplProfile_CallKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplProfile_CallKind.setStatus("mandatory")


class _AtmVplProfile_Action_o_Type(Integer32):
    """Custom type atmVplProfile_Action_o based on Integer32"""
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


_AtmVplProfile_Action_o_Type.__name__ = "Integer32"
_AtmVplProfile_Action_o_Object = MibScalar
atmVplProfile_Action_o = _AtmVplProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 38, 1, 1, 10),
    _AtmVplProfile_Action_o_Type()
)
atmVplProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmVplProfile_Action_o.setStatus("mandatory")
_MibatmVclProfile_ObjectIdentity = ObjectIdentity
mibatmVclProfile = _MibatmVclProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 39)
)
_MibatmVclProfileTable_Object = MibTable
mibatmVclProfileTable = _MibatmVclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1)
)
if mibBuilder.loadTexts:
    mibatmVclProfileTable.setStatus("mandatory")
_MibatmVclProfileEntry_Object = MibTableRow
mibatmVclProfileEntry = _MibatmVclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1)
)
mibatmVclProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Address-PhysicalAddress-Shelf"),
    (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Address-PhysicalAddress-Slot"),
    (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Address-PhysicalAddress-ItemNumber"),
    (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Address-LogicalItem"),
    (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Vpi"),
    (0, "ASCEND-MIBATMATOM-MIB", "atmVclProfile-Id-Vci"),
)
if mibBuilder.loadTexts:
    mibatmVclProfileEntry.setStatus("mandatory")
_AtmVclProfile_Id_Address_PhysicalAddress_Shelf_Type = Integer32
_AtmVclProfile_Id_Address_PhysicalAddress_Shelf_Object = MibScalar
atmVclProfile_Id_Address_PhysicalAddress_Shelf = _AtmVclProfile_Id_Address_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 1),
    _AtmVclProfile_Id_Address_PhysicalAddress_Shelf_Type()
)
atmVclProfile_Id_Address_PhysicalAddress_Shelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_Id_Address_PhysicalAddress_Shelf.setStatus("mandatory")
_AtmVclProfile_Id_Address_PhysicalAddress_Slot_Type = Integer32
_AtmVclProfile_Id_Address_PhysicalAddress_Slot_Object = MibScalar
atmVclProfile_Id_Address_PhysicalAddress_Slot = _AtmVclProfile_Id_Address_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 2),
    _AtmVclProfile_Id_Address_PhysicalAddress_Slot_Type()
)
atmVclProfile_Id_Address_PhysicalAddress_Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_Id_Address_PhysicalAddress_Slot.setStatus("mandatory")
_AtmVclProfile_Id_Address_PhysicalAddress_ItemNumber_Type = Integer32
_AtmVclProfile_Id_Address_PhysicalAddress_ItemNumber_Object = MibScalar
atmVclProfile_Id_Address_PhysicalAddress_ItemNumber = _AtmVclProfile_Id_Address_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 3),
    _AtmVclProfile_Id_Address_PhysicalAddress_ItemNumber_Type()
)
atmVclProfile_Id_Address_PhysicalAddress_ItemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_Id_Address_PhysicalAddress_ItemNumber.setStatus("mandatory")
_AtmVclProfile_Id_Address_LogicalItem_Type = Integer32
_AtmVclProfile_Id_Address_LogicalItem_Object = MibScalar
atmVclProfile_Id_Address_LogicalItem = _AtmVclProfile_Id_Address_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 4),
    _AtmVclProfile_Id_Address_LogicalItem_Type()
)
atmVclProfile_Id_Address_LogicalItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_Id_Address_LogicalItem.setStatus("mandatory")
_AtmVclProfile_Id_Vpi_Type = Integer32
_AtmVclProfile_Id_Vpi_Object = MibScalar
atmVclProfile_Id_Vpi = _AtmVclProfile_Id_Vpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 5),
    _AtmVclProfile_Id_Vpi_Type()
)
atmVclProfile_Id_Vpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_Id_Vpi.setStatus("mandatory")
_AtmVclProfile_Id_Vci_Type = Integer32
_AtmVclProfile_Id_Vci_Object = MibScalar
atmVclProfile_Id_Vci = _AtmVclProfile_Id_Vci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 6),
    _AtmVclProfile_Id_Vci_Type()
)
atmVclProfile_Id_Vci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_Id_Vci.setStatus("mandatory")
_AtmVclProfile_RxTrafficDesc_Type = Integer32
_AtmVclProfile_RxTrafficDesc_Object = MibScalar
atmVclProfile_RxTrafficDesc = _AtmVclProfile_RxTrafficDesc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 7),
    _AtmVclProfile_RxTrafficDesc_Type()
)
atmVclProfile_RxTrafficDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_RxTrafficDesc.setStatus("mandatory")
_AtmVclProfile_TxTrafficDesc_Type = Integer32
_AtmVclProfile_TxTrafficDesc_Object = MibScalar
atmVclProfile_TxTrafficDesc = _AtmVclProfile_TxTrafficDesc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 8),
    _AtmVclProfile_TxTrafficDesc_Type()
)
atmVclProfile_TxTrafficDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_TxTrafficDesc.setStatus("mandatory")


class _AtmVclProfile_AalType_Type(Integer32):
    """Custom type atmVclProfile_AalType based on Integer32"""
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
        *(("aal1", 2),
          ("aal2", 7),
          ("aal34", 3),
          ("aal5", 4),
          ("aalOther", 5),
          ("aalUnknown", 6),
          ("notPresent", 1))
    )


_AtmVclProfile_AalType_Type.__name__ = "Integer32"
_AtmVclProfile_AalType_Object = MibScalar
atmVclProfile_AalType = _AtmVclProfile_AalType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 9),
    _AtmVclProfile_AalType_Type()
)
atmVclProfile_AalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_AalType.setStatus("mandatory")
_AtmVclProfile_TxSduSize_Type = Integer32
_AtmVclProfile_TxSduSize_Object = MibScalar
atmVclProfile_TxSduSize = _AtmVclProfile_TxSduSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 10),
    _AtmVclProfile_TxSduSize_Type()
)
atmVclProfile_TxSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_TxSduSize.setStatus("mandatory")
_AtmVclProfile_RxSduSize_Type = Integer32
_AtmVclProfile_RxSduSize_Object = MibScalar
atmVclProfile_RxSduSize = _AtmVclProfile_RxSduSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 11),
    _AtmVclProfile_RxSduSize_Type()
)
atmVclProfile_RxSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_RxSduSize.setStatus("mandatory")


class _AtmVclProfile_Aal5Encaps_Type(Integer32):
    """Custom type atmVclProfile_Aal5Encaps based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("llcEncapsulation", 8),
          ("multiFrameRelaySscs", 9),
          ("otherEncapsulation", 10),
          ("unknownEncapsulation", 11),
          ("vcmuxBridged8023", 3),
          ("vcmuxBridged8025", 4),
          ("vcmuxBridged8026", 5),
          ("vcmuxLanemul8023", 6),
          ("vcmuxLanemul8025", 7),
          ("vcmuxRouted", 2))
    )


_AtmVclProfile_Aal5Encaps_Type.__name__ = "Integer32"
_AtmVclProfile_Aal5Encaps_Object = MibScalar
atmVclProfile_Aal5Encaps = _AtmVclProfile_Aal5Encaps_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 12),
    _AtmVclProfile_Aal5Encaps_Type()
)
atmVclProfile_Aal5Encaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_Aal5Encaps.setStatus("mandatory")


class _AtmVclProfile_McastType_Type(Integer32):
    """Custom type atmVclProfile_McastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("p2mpleaf", 4),
          ("p2mproot", 3),
          ("p2p", 2))
    )


_AtmVclProfile_McastType_Type.__name__ = "Integer32"
_AtmVclProfile_McastType_Object = MibScalar
atmVclProfile_McastType = _AtmVclProfile_McastType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 13),
    _AtmVclProfile_McastType_Type()
)
atmVclProfile_McastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_McastType.setStatus("mandatory")


class _AtmVclProfile_CallKind_Type(Integer32):
    """Custom type atmVclProfile_CallKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 2),
          ("spvcInitiator", 5),
          ("spvcTarget", 6),
          ("svcIncoming", 3),
          ("svcOutgoing", 4))
    )


_AtmVclProfile_CallKind_Type.__name__ = "Integer32"
_AtmVclProfile_CallKind_Object = MibScalar
atmVclProfile_CallKind = _AtmVclProfile_CallKind_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 14),
    _AtmVclProfile_CallKind_Type()
)
atmVclProfile_CallKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclProfile_CallKind.setStatus("mandatory")


class _AtmVclProfile_Action_o_Type(Integer32):
    """Custom type atmVclProfile_Action_o based on Integer32"""
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


_AtmVclProfile_Action_o_Type.__name__ = "Integer32"
_AtmVclProfile_Action_o_Object = MibScalar
atmVclProfile_Action_o = _AtmVclProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 39, 1, 1, 15),
    _AtmVclProfile_Action_o_Type()
)
atmVclProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmVclProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMATOM-MIB",
    **{"DisplayString": DisplayString,
       "mibatmVplProfile": mibatmVplProfile,
       "mibatmVplProfileTable": mibatmVplProfileTable,
       "mibatmVplProfileEntry": mibatmVplProfileEntry,
       "atmVplProfile-Id-Address-PhysicalAddress-Shelf": atmVplProfile_Id_Address_PhysicalAddress_Shelf,
       "atmVplProfile-Id-Address-PhysicalAddress-Slot": atmVplProfile_Id_Address_PhysicalAddress_Slot,
       "atmVplProfile-Id-Address-PhysicalAddress-ItemNumber": atmVplProfile_Id_Address_PhysicalAddress_ItemNumber,
       "atmVplProfile-Id-Address-LogicalItem": atmVplProfile_Id_Address_LogicalItem,
       "atmVplProfile-Id-Vpi": atmVplProfile_Id_Vpi,
       "atmVplProfile-RxTrafficDesc": atmVplProfile_RxTrafficDesc,
       "atmVplProfile-TxTrafficDesc": atmVplProfile_TxTrafficDesc,
       "atmVplProfile-McastType": atmVplProfile_McastType,
       "atmVplProfile-CallKind": atmVplProfile_CallKind,
       "atmVplProfile-Action-o": atmVplProfile_Action_o,
       "mibatmVclProfile": mibatmVclProfile,
       "mibatmVclProfileTable": mibatmVclProfileTable,
       "mibatmVclProfileEntry": mibatmVclProfileEntry,
       "atmVclProfile-Id-Address-PhysicalAddress-Shelf": atmVclProfile_Id_Address_PhysicalAddress_Shelf,
       "atmVclProfile-Id-Address-PhysicalAddress-Slot": atmVclProfile_Id_Address_PhysicalAddress_Slot,
       "atmVclProfile-Id-Address-PhysicalAddress-ItemNumber": atmVclProfile_Id_Address_PhysicalAddress_ItemNumber,
       "atmVclProfile-Id-Address-LogicalItem": atmVclProfile_Id_Address_LogicalItem,
       "atmVclProfile-Id-Vpi": atmVclProfile_Id_Vpi,
       "atmVclProfile-Id-Vci": atmVclProfile_Id_Vci,
       "atmVclProfile-RxTrafficDesc": atmVclProfile_RxTrafficDesc,
       "atmVclProfile-TxTrafficDesc": atmVclProfile_TxTrafficDesc,
       "atmVclProfile-AalType": atmVclProfile_AalType,
       "atmVclProfile-TxSduSize": atmVclProfile_TxSduSize,
       "atmVclProfile-RxSduSize": atmVclProfile_RxSduSize,
       "atmVclProfile-Aal5Encaps": atmVclProfile_Aal5Encaps,
       "atmVclProfile-McastType": atmVclProfile_McastType,
       "atmVclProfile-CallKind": atmVclProfile_CallKind,
       "atmVclProfile-Action-o": atmVclProfile_Action_o}
)
