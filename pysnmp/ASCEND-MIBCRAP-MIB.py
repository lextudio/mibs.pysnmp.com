# SNMP MIB module (ASCEND-MIBCRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBCRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:24 2024
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

_MibcrapProfile_ObjectIdentity = ObjectIdentity
mibcrapProfile = _MibcrapProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 70)
)
_MibcrapProfileTable_Object = MibTable
mibcrapProfileTable = _MibcrapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1)
)
if mibBuilder.loadTexts:
    mibcrapProfileTable.setStatus("mandatory")
_MibcrapProfileEntry_Object = MibTableRow
mibcrapProfileEntry = _MibcrapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1)
)
mibcrapProfileEntry.setIndexNames(
    (0, "ASCEND-MIBCRAP-MIB", "crapProfile-Index-DeviceAddress-PhysicalAddress-Shelf"),
    (0, "ASCEND-MIBCRAP-MIB", "crapProfile-Index-DeviceAddress-PhysicalAddress-Slot"),
    (0, "ASCEND-MIBCRAP-MIB", "crapProfile-Index-DeviceAddress-PhysicalAddress-ItemNumber"),
    (0, "ASCEND-MIBCRAP-MIB", "crapProfile-Index-DeviceAddress-LogicalItem"),
    (0, "ASCEND-MIBCRAP-MIB", "crapProfile-Index-EntryNumber"),
)
if mibBuilder.loadTexts:
    mibcrapProfileEntry.setStatus("mandatory")
_CrapProfile_Index_DeviceAddress_PhysicalAddress_Shelf_Type = Integer32
_CrapProfile_Index_DeviceAddress_PhysicalAddress_Shelf_Object = MibScalar
crapProfile_Index_DeviceAddress_PhysicalAddress_Shelf = _CrapProfile_Index_DeviceAddress_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 1),
    _CrapProfile_Index_DeviceAddress_PhysicalAddress_Shelf_Type()
)
crapProfile_Index_DeviceAddress_PhysicalAddress_Shelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crapProfile_Index_DeviceAddress_PhysicalAddress_Shelf.setStatus("mandatory")
_CrapProfile_Index_DeviceAddress_PhysicalAddress_Slot_Type = Integer32
_CrapProfile_Index_DeviceAddress_PhysicalAddress_Slot_Object = MibScalar
crapProfile_Index_DeviceAddress_PhysicalAddress_Slot = _CrapProfile_Index_DeviceAddress_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 2),
    _CrapProfile_Index_DeviceAddress_PhysicalAddress_Slot_Type()
)
crapProfile_Index_DeviceAddress_PhysicalAddress_Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crapProfile_Index_DeviceAddress_PhysicalAddress_Slot.setStatus("mandatory")
_CrapProfile_Index_DeviceAddress_PhysicalAddress_ItemNumber_Type = Integer32
_CrapProfile_Index_DeviceAddress_PhysicalAddress_ItemNumber_Object = MibScalar
crapProfile_Index_DeviceAddress_PhysicalAddress_ItemNumber = _CrapProfile_Index_DeviceAddress_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 3),
    _CrapProfile_Index_DeviceAddress_PhysicalAddress_ItemNumber_Type()
)
crapProfile_Index_DeviceAddress_PhysicalAddress_ItemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crapProfile_Index_DeviceAddress_PhysicalAddress_ItemNumber.setStatus("mandatory")
_CrapProfile_Index_DeviceAddress_LogicalItem_Type = Integer32
_CrapProfile_Index_DeviceAddress_LogicalItem_Object = MibScalar
crapProfile_Index_DeviceAddress_LogicalItem = _CrapProfile_Index_DeviceAddress_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 4),
    _CrapProfile_Index_DeviceAddress_LogicalItem_Type()
)
crapProfile_Index_DeviceAddress_LogicalItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crapProfile_Index_DeviceAddress_LogicalItem.setStatus("mandatory")
_CrapProfile_Index_EntryNumber_Type = Integer32
_CrapProfile_Index_EntryNumber_Object = MibScalar
crapProfile_Index_EntryNumber = _CrapProfile_Index_EntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 5),
    _CrapProfile_Index_EntryNumber_Type()
)
crapProfile_Index_EntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crapProfile_Index_EntryNumber.setStatus("mandatory")
_CrapProfile_TrunkGroup_Type = Integer32
_CrapProfile_TrunkGroup_Object = MibScalar
crapProfile_TrunkGroup = _CrapProfile_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 6),
    _CrapProfile_TrunkGroup_Type()
)
crapProfile_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_TrunkGroup.setStatus("mandatory")
_CrapProfile_PhoneNumber_Type = DisplayString
_CrapProfile_PhoneNumber_Object = MibScalar
crapProfile_PhoneNumber = _CrapProfile_PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 7),
    _CrapProfile_PhoneNumber_Type()
)
crapProfile_PhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_PhoneNumber.setStatus("mandatory")


class _CrapProfile_PreferredSource_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type crapProfile_PreferredSource_PhysicalAddress_Shelf based on Integer32"""
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


_CrapProfile_PreferredSource_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_CrapProfile_PreferredSource_PhysicalAddress_Shelf_Object = MibScalar
crapProfile_PreferredSource_PhysicalAddress_Shelf = _CrapProfile_PreferredSource_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 8),
    _CrapProfile_PreferredSource_PhysicalAddress_Shelf_Type()
)
crapProfile_PreferredSource_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_PreferredSource_PhysicalAddress_Shelf.setStatus("mandatory")


class _CrapProfile_PreferredSource_PhysicalAddress_Slot_Type(Integer32):
    """Custom type crapProfile_PreferredSource_PhysicalAddress_Slot based on Integer32"""
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


_CrapProfile_PreferredSource_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_CrapProfile_PreferredSource_PhysicalAddress_Slot_Object = MibScalar
crapProfile_PreferredSource_PhysicalAddress_Slot = _CrapProfile_PreferredSource_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 9),
    _CrapProfile_PreferredSource_PhysicalAddress_Slot_Type()
)
crapProfile_PreferredSource_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_PreferredSource_PhysicalAddress_Slot.setStatus("mandatory")
_CrapProfile_PreferredSource_PhysicalAddress_ItemNumber_Type = Integer32
_CrapProfile_PreferredSource_PhysicalAddress_ItemNumber_Object = MibScalar
crapProfile_PreferredSource_PhysicalAddress_ItemNumber = _CrapProfile_PreferredSource_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 10),
    _CrapProfile_PreferredSource_PhysicalAddress_ItemNumber_Type()
)
crapProfile_PreferredSource_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_PreferredSource_PhysicalAddress_ItemNumber.setStatus("mandatory")
_CrapProfile_PreferredSource_LogicalItem_Type = Integer32
_CrapProfile_PreferredSource_LogicalItem_Object = MibScalar
crapProfile_PreferredSource_LogicalItem = _CrapProfile_PreferredSource_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 11),
    _CrapProfile_PreferredSource_LogicalItem_Type()
)
crapProfile_PreferredSource_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_PreferredSource_LogicalItem.setStatus("mandatory")


class _CrapProfile_CallRouteType_Type(Integer32):
    """Custom type crapProfile_CallRouteType based on Integer32"""
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
        *(("anyCallType", 1),
          ("digitalCallType", 3),
          ("frgsmCallType", 17),
          ("g723CallType", 16),
          ("g728CallType", 15),
          ("g729CallType", 14),
          ("iptoipVoipCallType", 12),
          ("mtpLinkType", 11),
          ("phsCallType", 5),
          ("rt24CallType", 18),
          ("rtfaxCallType", 13),
          ("trunkCallType", 4),
          ("trunkDigitalCallType", 9),
          ("trunkVoiceCallType", 8),
          ("v110CallType", 7),
          ("voiceCallType", 2),
          ("voipCallType", 6),
          ("wormarqCallType", 10))
    )


_CrapProfile_CallRouteType_Type.__name__ = "Integer32"
_CrapProfile_CallRouteType_Object = MibScalar
crapProfile_CallRouteType = _CrapProfile_CallRouteType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 12),
    _CrapProfile_CallRouteType_Type()
)
crapProfile_CallRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_CallRouteType.setStatus("mandatory")
_CrapProfile_LcdIndex_Type = Integer32
_CrapProfile_LcdIndex_Object = MibScalar
crapProfile_LcdIndex = _CrapProfile_LcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 13),
    _CrapProfile_LcdIndex_Type()
)
crapProfile_LcdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_LcdIndex.setStatus("mandatory")
_CrapProfile_Name_Type = DisplayString
_CrapProfile_Name_Object = MibScalar
crapProfile_Name = _CrapProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 14),
    _CrapProfile_Name_Type()
)
crapProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_Name.setStatus("mandatory")


class _CrapProfile_Active_Type(Integer32):
    """Custom type crapProfile_Active based on Integer32"""
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


_CrapProfile_Active_Type.__name__ = "Integer32"
_CrapProfile_Active_Object = MibScalar
crapProfile_Active = _CrapProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 15),
    _CrapProfile_Active_Type()
)
crapProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_Active.setStatus("mandatory")
_CrapProfile_SrcChannelGroup_Type = Integer32
_CrapProfile_SrcChannelGroup_Object = MibScalar
crapProfile_SrcChannelGroup = _CrapProfile_SrcChannelGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 16),
    _CrapProfile_SrcChannelGroup_Type()
)
crapProfile_SrcChannelGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_SrcChannelGroup.setStatus("mandatory")
_CrapProfile_ChannelGroup_Type = Integer32
_CrapProfile_ChannelGroup_Object = MibScalar
crapProfile_ChannelGroup = _CrapProfile_ChannelGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 17),
    _CrapProfile_ChannelGroup_Type()
)
crapProfile_ChannelGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_ChannelGroup.setStatus("mandatory")
_CrapProfile_DialPlan_Type = Integer32
_CrapProfile_DialPlan_Object = MibScalar
crapProfile_DialPlan = _CrapProfile_DialPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 18),
    _CrapProfile_DialPlan_Type()
)
crapProfile_DialPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_DialPlan.setStatus("mandatory")
_CrapProfile_RewritePattern_Type = DisplayString
_CrapProfile_RewritePattern_Object = MibScalar
crapProfile_RewritePattern = _CrapProfile_RewritePattern_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 19),
    _CrapProfile_RewritePattern_Type()
)
crapProfile_RewritePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_RewritePattern.setStatus("mandatory")
_CrapProfile_RewriteReplacement_Type = DisplayString
_CrapProfile_RewriteReplacement_Object = MibScalar
crapProfile_RewriteReplacement = _CrapProfile_RewriteReplacement_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 20),
    _CrapProfile_RewriteReplacement_Type()
)
crapProfile_RewriteReplacement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_RewriteReplacement.setStatus("mandatory")
_CrapProfile_RemoteVoipgw_Type = IpAddress
_CrapProfile_RemoteVoipgw_Object = MibScalar
crapProfile_RemoteVoipgw = _CrapProfile_RemoteVoipgw_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 21),
    _CrapProfile_RemoteVoipgw_Type()
)
crapProfile_RemoteVoipgw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_RemoteVoipgw.setStatus("mandatory")


class _CrapProfile_Action_o_Type(Integer32):
    """Custom type crapProfile_Action_o based on Integer32"""
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


_CrapProfile_Action_o_Type.__name__ = "Integer32"
_CrapProfile_Action_o_Object = MibScalar
crapProfile_Action_o = _CrapProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 22),
    _CrapProfile_Action_o_Type()
)
crapProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_Action_o.setStatus("mandatory")
_CrapProfile_Cost_Type = Integer32
_CrapProfile_Cost_Object = MibScalar
crapProfile_Cost = _CrapProfile_Cost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 70, 1, 1, 23),
    _CrapProfile_Cost_Type()
)
crapProfile_Cost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crapProfile_Cost.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBCRAP-MIB",
    **{"DisplayString": DisplayString,
       "mibcrapProfile": mibcrapProfile,
       "mibcrapProfileTable": mibcrapProfileTable,
       "mibcrapProfileEntry": mibcrapProfileEntry,
       "crapProfile-Index-DeviceAddress-PhysicalAddress-Shelf": crapProfile_Index_DeviceAddress_PhysicalAddress_Shelf,
       "crapProfile-Index-DeviceAddress-PhysicalAddress-Slot": crapProfile_Index_DeviceAddress_PhysicalAddress_Slot,
       "crapProfile-Index-DeviceAddress-PhysicalAddress-ItemNumber": crapProfile_Index_DeviceAddress_PhysicalAddress_ItemNumber,
       "crapProfile-Index-DeviceAddress-LogicalItem": crapProfile_Index_DeviceAddress_LogicalItem,
       "crapProfile-Index-EntryNumber": crapProfile_Index_EntryNumber,
       "crapProfile-TrunkGroup": crapProfile_TrunkGroup,
       "crapProfile-PhoneNumber": crapProfile_PhoneNumber,
       "crapProfile-PreferredSource-PhysicalAddress-Shelf": crapProfile_PreferredSource_PhysicalAddress_Shelf,
       "crapProfile-PreferredSource-PhysicalAddress-Slot": crapProfile_PreferredSource_PhysicalAddress_Slot,
       "crapProfile-PreferredSource-PhysicalAddress-ItemNumber": crapProfile_PreferredSource_PhysicalAddress_ItemNumber,
       "crapProfile-PreferredSource-LogicalItem": crapProfile_PreferredSource_LogicalItem,
       "crapProfile-CallRouteType": crapProfile_CallRouteType,
       "crapProfile-LcdIndex": crapProfile_LcdIndex,
       "crapProfile-Name": crapProfile_Name,
       "crapProfile-Active": crapProfile_Active,
       "crapProfile-SrcChannelGroup": crapProfile_SrcChannelGroup,
       "crapProfile-ChannelGroup": crapProfile_ChannelGroup,
       "crapProfile-DialPlan": crapProfile_DialPlan,
       "crapProfile-RewritePattern": crapProfile_RewritePattern,
       "crapProfile-RewriteReplacement": crapProfile_RewriteReplacement,
       "crapProfile-RemoteVoipgw": crapProfile_RemoteVoipgw,
       "crapProfile-Action-o": crapProfile_Action_o,
       "crapProfile-Cost": crapProfile_Cost}
)
