# SNMP MIB module (ASCEND-MIBVDSLNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBVDSLNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:33 2024
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

_MibvdslNetworkProfile_ObjectIdentity = ObjectIdentity
mibvdslNetworkProfile = _MibvdslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 9)
)
_MibvdslNetworkProfileTable_Object = MibTable
mibvdslNetworkProfileTable = _MibvdslNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1)
)
if mibBuilder.loadTexts:
    mibvdslNetworkProfileTable.setStatus("mandatory")
_MibvdslNetworkProfileEntry_Object = MibTableRow
mibvdslNetworkProfileEntry = _MibvdslNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1)
)
mibvdslNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBVDSLNET-MIB", "vdslNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBVDSLNET-MIB", "vdslNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBVDSLNET-MIB", "vdslNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibvdslNetworkProfileEntry.setStatus("mandatory")
_VdslNetworkProfile_Shelf_o_Type = Integer32
_VdslNetworkProfile_Shelf_o_Object = MibScalar
vdslNetworkProfile_Shelf_o = _VdslNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 1),
    _VdslNetworkProfile_Shelf_o_Type()
)
vdslNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslNetworkProfile_Shelf_o.setStatus("mandatory")
_VdslNetworkProfile_Slot_o_Type = Integer32
_VdslNetworkProfile_Slot_o_Object = MibScalar
vdslNetworkProfile_Slot_o = _VdslNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 2),
    _VdslNetworkProfile_Slot_o_Type()
)
vdslNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslNetworkProfile_Slot_o.setStatus("mandatory")
_VdslNetworkProfile_Item_o_Type = Integer32
_VdslNetworkProfile_Item_o_Object = MibScalar
vdslNetworkProfile_Item_o = _VdslNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 3),
    _VdslNetworkProfile_Item_o_Type()
)
vdslNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslNetworkProfile_Item_o.setStatus("mandatory")
_VdslNetworkProfile_Name_Type = DisplayString
_VdslNetworkProfile_Name_Object = MibScalar
vdslNetworkProfile_Name = _VdslNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 4),
    _VdslNetworkProfile_Name_Type()
)
vdslNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_Name.setStatus("mandatory")


class _VdslNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type vdslNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_VdslNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_VdslNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
vdslNetworkProfile_PhysicalAddress_Shelf = _VdslNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 11),
    _VdslNetworkProfile_PhysicalAddress_Shelf_Type()
)
vdslNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _VdslNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type vdslNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_VdslNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_VdslNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
vdslNetworkProfile_PhysicalAddress_Slot = _VdslNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 12),
    _VdslNetworkProfile_PhysicalAddress_Slot_Type()
)
vdslNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_VdslNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_VdslNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
vdslNetworkProfile_PhysicalAddress_ItemNumber = _VdslNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 13),
    _VdslNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
vdslNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _VdslNetworkProfile_Action_o_Type(Integer32):
    """Custom type vdslNetworkProfile_Action_o based on Integer32"""
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


_VdslNetworkProfile_Action_o_Type.__name__ = "Integer32"
_VdslNetworkProfile_Action_o_Object = MibScalar
vdslNetworkProfile_Action_o = _VdslNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 14),
    _VdslNetworkProfile_Action_o_Type()
)
vdslNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_Action_o.setStatus("mandatory")


class _VdslNetworkProfile_Enabled_Type(Integer32):
    """Custom type vdslNetworkProfile_Enabled based on Integer32"""
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


_VdslNetworkProfile_Enabled_Type.__name__ = "Integer32"
_VdslNetworkProfile_Enabled_Object = MibScalar
vdslNetworkProfile_Enabled = _VdslNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 16),
    _VdslNetworkProfile_Enabled_Type()
)
vdslNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_Enabled.setStatus("mandatory")


class _VdslNetworkProfile_SparingMode_Type(Integer32):
    """Custom type vdslNetworkProfile_SparingMode based on Integer32"""
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


_VdslNetworkProfile_SparingMode_Type.__name__ = "Integer32"
_VdslNetworkProfile_SparingMode_Object = MibScalar
vdslNetworkProfile_SparingMode = _VdslNetworkProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 17),
    _VdslNetworkProfile_SparingMode_Type()
)
vdslNetworkProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_SparingMode.setStatus("mandatory")


class _VdslNetworkProfile_IgnoreLineup_Type(Integer32):
    """Custom type vdslNetworkProfile_IgnoreLineup based on Integer32"""
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


_VdslNetworkProfile_IgnoreLineup_Type.__name__ = "Integer32"
_VdslNetworkProfile_IgnoreLineup_Object = MibScalar
vdslNetworkProfile_IgnoreLineup = _VdslNetworkProfile_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 18),
    _VdslNetworkProfile_IgnoreLineup_Type()
)
vdslNetworkProfile_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_IgnoreLineup.setStatus("mandatory")
_VdslNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_VdslNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
vdslNetworkProfile_LineConfig_NailedGroup = _VdslNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 19),
    _VdslNetworkProfile_LineConfig_NailedGroup_Type()
)
vdslNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")
_VdslNetworkProfile_LineConfig_VpSwitchingVpi_Type = Integer32
_VdslNetworkProfile_LineConfig_VpSwitchingVpi_Object = MibScalar
vdslNetworkProfile_LineConfig_VpSwitchingVpi = _VdslNetworkProfile_LineConfig_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 20),
    _VdslNetworkProfile_LineConfig_VpSwitchingVpi_Type()
)
vdslNetworkProfile_LineConfig_VpSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_LineConfig_VpSwitchingVpi.setStatus("mandatory")


class _VdslNetworkProfile_LineConfig_UpStreamFixedRate_Type(Integer32):
    """Custom type vdslNetworkProfile_LineConfig_UpStreamFixedRate based on Integer32"""
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
        *(("n-1206667", 1),
          ("n-1930667", 3),
          ("n-3861333", 4),
          ("n-965333", 2))
    )


_VdslNetworkProfile_LineConfig_UpStreamFixedRate_Type.__name__ = "Integer32"
_VdslNetworkProfile_LineConfig_UpStreamFixedRate_Object = MibScalar
vdslNetworkProfile_LineConfig_UpStreamFixedRate = _VdslNetworkProfile_LineConfig_UpStreamFixedRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 22),
    _VdslNetworkProfile_LineConfig_UpStreamFixedRate_Type()
)
vdslNetworkProfile_LineConfig_UpStreamFixedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_LineConfig_UpStreamFixedRate.setStatus("mandatory")


class _VdslNetworkProfile_LineConfig_DownStreamFixedRate_Type(Integer32):
    """Custom type vdslNetworkProfile_LineConfig_DownStreamFixedRate based on Integer32"""
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
        *(("n-11463333", 2),
          ("n-1206667", 1),
          ("n-15626333", 3),
          ("n-19306667", 4))
    )


_VdslNetworkProfile_LineConfig_DownStreamFixedRate_Type.__name__ = "Integer32"
_VdslNetworkProfile_LineConfig_DownStreamFixedRate_Object = MibScalar
vdslNetworkProfile_LineConfig_DownStreamFixedRate = _VdslNetworkProfile_LineConfig_DownStreamFixedRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 23),
    _VdslNetworkProfile_LineConfig_DownStreamFixedRate_Type()
)
vdslNetworkProfile_LineConfig_DownStreamFixedRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_LineConfig_DownStreamFixedRate.setStatus("mandatory")


class _VdslNetworkProfile_LineConfig_ConfigLoopback_Type(Integer32):
    """Custom type vdslNetworkProfile_LineConfig_ConfigLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 3),
          ("digital", 2),
          ("disable", 1))
    )


_VdslNetworkProfile_LineConfig_ConfigLoopback_Type.__name__ = "Integer32"
_VdslNetworkProfile_LineConfig_ConfigLoopback_Object = MibScalar
vdslNetworkProfile_LineConfig_ConfigLoopback = _VdslNetworkProfile_LineConfig_ConfigLoopback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 24),
    _VdslNetworkProfile_LineConfig_ConfigLoopback_Type()
)
vdslNetworkProfile_LineConfig_ConfigLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_LineConfig_ConfigLoopback.setStatus("mandatory")


class _VdslNetworkProfile_LineConfig_PsdValue_Type(Integer32):
    """Custom type vdslNetworkProfile_LineConfig_PsdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-53dbm", 1),
          ("n-60dbm", 2))
    )


_VdslNetworkProfile_LineConfig_PsdValue_Type.__name__ = "Integer32"
_VdslNetworkProfile_LineConfig_PsdValue_Object = MibScalar
vdslNetworkProfile_LineConfig_PsdValue = _VdslNetworkProfile_LineConfig_PsdValue_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 25),
    _VdslNetworkProfile_LineConfig_PsdValue_Type()
)
vdslNetworkProfile_LineConfig_PsdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_LineConfig_PsdValue.setStatus("mandatory")


class _VdslNetworkProfile_LineConfig_LinkStatecmd_Type(Integer32):
    """Custom type vdslNetworkProfile_LineConfig_LinkStatecmd based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("autoConnectCmd", 16),
          ("backToServState", 5),
          ("changeCurrentParamState", 8),
          ("changeIdleParamState", 6),
          ("changeWarmStartParamState", 7),
          ("connectState", 2),
          ("disconnectState", 1),
          ("idleReqState", 4),
          ("quietState", 3))
    )


_VdslNetworkProfile_LineConfig_LinkStatecmd_Type.__name__ = "Integer32"
_VdslNetworkProfile_LineConfig_LinkStatecmd_Object = MibScalar
vdslNetworkProfile_LineConfig_LinkStatecmd = _VdslNetworkProfile_LineConfig_LinkStatecmd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 9, 1, 1, 26),
    _VdslNetworkProfile_LineConfig_LinkStatecmd_Type()
)
vdslNetworkProfile_LineConfig_LinkStatecmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslNetworkProfile_LineConfig_LinkStatecmd.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBVDSLNET-MIB",
    **{"DisplayString": DisplayString,
       "mibvdslNetworkProfile": mibvdslNetworkProfile,
       "mibvdslNetworkProfileTable": mibvdslNetworkProfileTable,
       "mibvdslNetworkProfileEntry": mibvdslNetworkProfileEntry,
       "vdslNetworkProfile-Shelf-o": vdslNetworkProfile_Shelf_o,
       "vdslNetworkProfile-Slot-o": vdslNetworkProfile_Slot_o,
       "vdslNetworkProfile-Item-o": vdslNetworkProfile_Item_o,
       "vdslNetworkProfile-Name": vdslNetworkProfile_Name,
       "vdslNetworkProfile-PhysicalAddress-Shelf": vdslNetworkProfile_PhysicalAddress_Shelf,
       "vdslNetworkProfile-PhysicalAddress-Slot": vdslNetworkProfile_PhysicalAddress_Slot,
       "vdslNetworkProfile-PhysicalAddress-ItemNumber": vdslNetworkProfile_PhysicalAddress_ItemNumber,
       "vdslNetworkProfile-Action-o": vdslNetworkProfile_Action_o,
       "vdslNetworkProfile-Enabled": vdslNetworkProfile_Enabled,
       "vdslNetworkProfile-SparingMode": vdslNetworkProfile_SparingMode,
       "vdslNetworkProfile-IgnoreLineup": vdslNetworkProfile_IgnoreLineup,
       "vdslNetworkProfile-LineConfig-NailedGroup": vdslNetworkProfile_LineConfig_NailedGroup,
       "vdslNetworkProfile-LineConfig-VpSwitchingVpi": vdslNetworkProfile_LineConfig_VpSwitchingVpi,
       "vdslNetworkProfile-LineConfig-UpStreamFixedRate": vdslNetworkProfile_LineConfig_UpStreamFixedRate,
       "vdslNetworkProfile-LineConfig-DownStreamFixedRate": vdslNetworkProfile_LineConfig_DownStreamFixedRate,
       "vdslNetworkProfile-LineConfig-ConfigLoopback": vdslNetworkProfile_LineConfig_ConfigLoopback,
       "vdslNetworkProfile-LineConfig-PsdValue": vdslNetworkProfile_LineConfig_PsdValue,
       "vdslNetworkProfile-LineConfig-LinkStatecmd": vdslNetworkProfile_LineConfig_LinkStatecmd}
)
