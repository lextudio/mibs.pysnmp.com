# SNMP MIB module (ASCEND-MIBDBA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDBA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:25 2024
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

_MibdBAProfile_ObjectIdentity = ObjectIdentity
mibdBAProfile = _MibdBAProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 71)
)
_MibdBAProfileTable_Object = MibTable
mibdBAProfileTable = _MibdBAProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1)
)
if mibBuilder.loadTexts:
    mibdBAProfileTable.setStatus("mandatory")
_MibdBAProfileEntry_Object = MibTableRow
mibdBAProfileEntry = _MibdBAProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1)
)
mibdBAProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDBA-MIB", "dBAProfile-Shelf-o"),
    (0, "ASCEND-MIBDBA-MIB", "dBAProfile-Slot-o"),
    (0, "ASCEND-MIBDBA-MIB", "dBAProfile-Item-o"),
    (0, "ASCEND-MIBDBA-MIB", "dBAProfile-LogicalItem-o"),
)
if mibBuilder.loadTexts:
    mibdBAProfileEntry.setStatus("mandatory")
_DBAProfile_Shelf_o_Type = Integer32
_DBAProfile_Shelf_o_Object = MibScalar
dBAProfile_Shelf_o = _DBAProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 1),
    _DBAProfile_Shelf_o_Type()
)
dBAProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dBAProfile_Shelf_o.setStatus("mandatory")
_DBAProfile_Slot_o_Type = Integer32
_DBAProfile_Slot_o_Object = MibScalar
dBAProfile_Slot_o = _DBAProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 2),
    _DBAProfile_Slot_o_Type()
)
dBAProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dBAProfile_Slot_o.setStatus("mandatory")
_DBAProfile_Item_o_Type = Integer32
_DBAProfile_Item_o_Object = MibScalar
dBAProfile_Item_o = _DBAProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 3),
    _DBAProfile_Item_o_Type()
)
dBAProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dBAProfile_Item_o.setStatus("mandatory")
_DBAProfile_LogicalItem_o_Type = Integer32
_DBAProfile_LogicalItem_o_Object = MibScalar
dBAProfile_LogicalItem_o = _DBAProfile_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 4),
    _DBAProfile_LogicalItem_o_Type()
)
dBAProfile_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dBAProfile_LogicalItem_o.setStatus("mandatory")


class _DBAProfile_LogicalAddress_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type dBAProfile_LogicalAddress_PhysicalAddress_Shelf based on Integer32"""
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


_DBAProfile_LogicalAddress_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_DBAProfile_LogicalAddress_PhysicalAddress_Shelf_Object = MibScalar
dBAProfile_LogicalAddress_PhysicalAddress_Shelf = _DBAProfile_LogicalAddress_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 5),
    _DBAProfile_LogicalAddress_PhysicalAddress_Shelf_Type()
)
dBAProfile_LogicalAddress_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_LogicalAddress_PhysicalAddress_Shelf.setStatus("mandatory")


class _DBAProfile_LogicalAddress_PhysicalAddress_Slot_Type(Integer32):
    """Custom type dBAProfile_LogicalAddress_PhysicalAddress_Slot based on Integer32"""
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


_DBAProfile_LogicalAddress_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_DBAProfile_LogicalAddress_PhysicalAddress_Slot_Object = MibScalar
dBAProfile_LogicalAddress_PhysicalAddress_Slot = _DBAProfile_LogicalAddress_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 6),
    _DBAProfile_LogicalAddress_PhysicalAddress_Slot_Type()
)
dBAProfile_LogicalAddress_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_LogicalAddress_PhysicalAddress_Slot.setStatus("mandatory")
_DBAProfile_LogicalAddress_PhysicalAddress_ItemNumber_Type = Integer32
_DBAProfile_LogicalAddress_PhysicalAddress_ItemNumber_Object = MibScalar
dBAProfile_LogicalAddress_PhysicalAddress_ItemNumber = _DBAProfile_LogicalAddress_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 7),
    _DBAProfile_LogicalAddress_PhysicalAddress_ItemNumber_Type()
)
dBAProfile_LogicalAddress_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_LogicalAddress_PhysicalAddress_ItemNumber.setStatus("mandatory")
_DBAProfile_LogicalAddress_LogicalItem_Type = Integer32
_DBAProfile_LogicalAddress_LogicalItem_Object = MibScalar
dBAProfile_LogicalAddress_LogicalItem = _DBAProfile_LogicalAddress_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 8),
    _DBAProfile_LogicalAddress_LogicalItem_Type()
)
dBAProfile_LogicalAddress_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_LogicalAddress_LogicalItem.setStatus("mandatory")
_DBAProfile_Name_Type = DisplayString
_DBAProfile_Name_Object = MibScalar
dBAProfile_Name = _DBAProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 9),
    _DBAProfile_Name_Type()
)
dBAProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_Name.setStatus("mandatory")
_DBAProfile_PhoneNumber_Type = DisplayString
_DBAProfile_PhoneNumber_Object = MibScalar
dBAProfile_PhoneNumber = _DBAProfile_PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 10),
    _DBAProfile_PhoneNumber_Type()
)
dBAProfile_PhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_PhoneNumber.setStatus("mandatory")
_DBAProfile_BillingNumber_Type = DisplayString
_DBAProfile_BillingNumber_Object = MibScalar
dBAProfile_BillingNumber = _DBAProfile_BillingNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 11),
    _DBAProfile_BillingNumber_Type()
)
dBAProfile_BillingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_BillingNumber.setStatus("mandatory")


class _DBAProfile_oCallType_Type(Integer32):
    """Custom type dBAProfile_oCallType based on Integer32"""
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
        *(("callCh1Ch", 3),
          ("callCh2Ch", 4),
          ("callChFt1", 5),
          ("callChFt1Aim", 6),
          ("callChFt1Bo", 7),
          ("callChFt1StaticBo", 8),
          ("callChNBy", 1),
          ("callChNByBonding", 2),
          ("numberOfCallChTypes", 9))
    )


_DBAProfile_oCallType_Type.__name__ = "Integer32"
_DBAProfile_oCallType_Object = MibScalar
dBAProfile_oCallType = _DBAProfile_oCallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 12),
    _DBAProfile_oCallType_Type()
)
dBAProfile_oCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_oCallType.setStatus("mandatory")


class _DBAProfile_oCallMgm_Type(Integer32):
    """Custom type dBAProfile_oCallMgm based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("callMgmtBonding0", 8),
          ("callMgmtBonding1", 9),
          ("callMgmtBonding2", 10),
          ("callMgmtBonding3", 11),
          ("callMgmtDeltaRate", 4),
          ("callMgmtDynamicRate", 3),
          ("callMgmtManualRate", 2),
          ("callMgmtOneOfEight", 6),
          ("callMgmtOneOfFourty", 7),
          ("callMgmtStaticRate", 1),
          ("callMgmtTimeOfDay", 5),
          ("numberOfCallMgmtProtocols", 12))
    )


_DBAProfile_oCallMgm_Type.__name__ = "Integer32"
_DBAProfile_oCallMgm_Object = MibScalar
dBAProfile_oCallMgm = _DBAProfile_oCallMgm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 13),
    _DBAProfile_oCallMgm_Type()
)
dBAProfile_oCallMgm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_oCallMgm.setStatus("mandatory")


class _DBAProfile_oDataSvc_Type(Integer32):
    """Custom type dBAProfile_oDataSvc based on Integer32"""
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


_DBAProfile_oDataSvc_Type.__name__ = "Integer32"
_DBAProfile_oDataSvc_Object = MibScalar
dBAProfile_oDataSvc = _DBAProfile_oDataSvc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 14),
    _DBAProfile_oDataSvc_Type()
)
dBAProfile_oDataSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_oDataSvc.setStatus("mandatory")


class _DBAProfile_Force56_Type(Integer32):
    """Custom type dBAProfile_Force56 based on Integer32"""
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


_DBAProfile_Force56_Type.__name__ = "Integer32"
_DBAProfile_Force56_Object = MibScalar
dBAProfile_Force56 = _DBAProfile_Force56_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 15),
    _DBAProfile_Force56_Type()
)
dBAProfile_Force56.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_Force56.setStatus("mandatory")
_DBAProfile_BaseChannelCount_Type = Integer32
_DBAProfile_BaseChannelCount_Object = MibScalar
dBAProfile_BaseChannelCount = _DBAProfile_BaseChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 16),
    _DBAProfile_BaseChannelCount_Type()
)
dBAProfile_BaseChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_BaseChannelCount.setStatus("mandatory")
_DBAProfile_IncrementChannelCount_Type = Integer32
_DBAProfile_IncrementChannelCount_Object = MibScalar
dBAProfile_IncrementChannelCount = _DBAProfile_IncrementChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 17),
    _DBAProfile_IncrementChannelCount_Type()
)
dBAProfile_IncrementChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_IncrementChannelCount.setStatus("mandatory")
_DBAProfile_DecrementChannelCount_Type = Integer32
_DBAProfile_DecrementChannelCount_Object = MibScalar
dBAProfile_DecrementChannelCount = _DBAProfile_DecrementChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 18),
    _DBAProfile_DecrementChannelCount_Type()
)
dBAProfile_DecrementChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_DecrementChannelCount.setStatus("mandatory")


class _DBAProfile_oFailAction_Type(Integer32):
    """Custom type dBAProfile_oFailAction based on Integer32"""
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
        *(("disc", 1),
          ("numberOfFailureActions", 4),
          ("reduce", 2),
          ("retry", 3))
    )


_DBAProfile_oFailAction_Type.__name__ = "Integer32"
_DBAProfile_oFailAction_Object = MibScalar
dBAProfile_oFailAction = _DBAProfile_oFailAction_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 19),
    _DBAProfile_oFailAction_Type()
)
dBAProfile_oFailAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_oFailAction.setStatus("mandatory")


class _DBAProfile_BitInversionRequired_Type(Integer32):
    """Custom type dBAProfile_BitInversionRequired based on Integer32"""
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


_DBAProfile_BitInversionRequired_Type.__name__ = "Integer32"
_DBAProfile_BitInversionRequired_Object = MibScalar
dBAProfile_BitInversionRequired = _DBAProfile_BitInversionRequired_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 20),
    _DBAProfile_BitInversionRequired_Type()
)
dBAProfile_BitInversionRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_BitInversionRequired.setStatus("mandatory")


class _DBAProfile_Ft1Caller_Type(Integer32):
    """Custom type dBAProfile_Ft1Caller based on Integer32"""
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


_DBAProfile_Ft1Caller_Type.__name__ = "Integer32"
_DBAProfile_Ft1Caller_Object = MibScalar
dBAProfile_Ft1Caller = _DBAProfile_Ft1Caller_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 21),
    _DBAProfile_Ft1Caller_Type()
)
dBAProfile_Ft1Caller.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_Ft1Caller.setStatus("mandatory")
_DBAProfile_Ft1Timeout_Type = Integer32
_DBAProfile_Ft1Timeout_Object = MibScalar
dBAProfile_Ft1Timeout = _DBAProfile_Ft1Timeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 22),
    _DBAProfile_Ft1Timeout_Type()
)
dBAProfile_Ft1Timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_Ft1Timeout.setStatus("mandatory")
_DBAProfile_CallByCallID_Type = Integer32
_DBAProfile_CallByCallID_Object = MibScalar
dBAProfile_CallByCallID = _DBAProfile_CallByCallID_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 23),
    _DBAProfile_CallByCallID_Type()
)
dBAProfile_CallByCallID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_CallByCallID.setStatus("mandatory")
_DBAProfile_CalledNumberType_Type = Integer32
_DBAProfile_CalledNumberType_Object = MibScalar
dBAProfile_CalledNumberType = _DBAProfile_CalledNumberType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 24),
    _DBAProfile_CalledNumberType_Type()
)
dBAProfile_CalledNumberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_CalledNumberType.setStatus("mandatory")


class _DBAProfile_UnknownPlanUnknown_Type(Integer32):
    """Custom type dBAProfile_UnknownPlanUnknown based on Integer32"""
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


_DBAProfile_UnknownPlanUnknown_Type.__name__ = "Integer32"
_DBAProfile_UnknownPlanUnknown_Object = MibScalar
dBAProfile_UnknownPlanUnknown = _DBAProfile_UnknownPlanUnknown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 25),
    _DBAProfile_UnknownPlanUnknown_Type()
)
dBAProfile_UnknownPlanUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_UnknownPlanUnknown.setStatus("mandatory")


class _DBAProfile_LocalPlanIsdn_Type(Integer32):
    """Custom type dBAProfile_LocalPlanIsdn based on Integer32"""
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


_DBAProfile_LocalPlanIsdn_Type.__name__ = "Integer32"
_DBAProfile_LocalPlanIsdn_Object = MibScalar
dBAProfile_LocalPlanIsdn = _DBAProfile_LocalPlanIsdn_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 26),
    _DBAProfile_LocalPlanIsdn_Type()
)
dBAProfile_LocalPlanIsdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_LocalPlanIsdn.setStatus("mandatory")
_DBAProfile_TransitNumber_Type = DisplayString
_DBAProfile_TransitNumber_Object = MibScalar
dBAProfile_TransitNumber = _DBAProfile_TransitNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 27),
    _DBAProfile_TransitNumber_Type()
)
dBAProfile_TransitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_TransitNumber.setStatus("mandatory")


class _DBAProfile_oAutoBERT_Type(Integer32):
    """Custom type dBAProfile_oAutoBERT based on Integer32"""
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
        *(("n-120Sec", 6),
          ("n-15Sec", 2),
          ("n-30Sec", 3),
          ("n-60Sec", 4),
          ("n-90Sec", 5),
          ("numberOfBertTestOptions", 7),
          ("off", 1))
    )


_DBAProfile_oAutoBERT_Type.__name__ = "Integer32"
_DBAProfile_oAutoBERT_Object = MibScalar
dBAProfile_oAutoBERT = _DBAProfile_oAutoBERT_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 28),
    _DBAProfile_oAutoBERT_Type()
)
dBAProfile_oAutoBERT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_oAutoBERT.setStatus("mandatory")


class _DBAProfile_TimedCall_Type(Integer32):
    """Custom type dBAProfile_TimedCall based on Integer32"""
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


_DBAProfile_TimedCall_Type.__name__ = "Integer32"
_DBAProfile_TimedCall_Object = MibScalar
dBAProfile_TimedCall = _DBAProfile_TimedCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 29),
    _DBAProfile_TimedCall_Type()
)
dBAProfile_TimedCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_TimedCall.setStatus("mandatory")


class _DBAProfile_FlagIdle_Type(Integer32):
    """Custom type dBAProfile_FlagIdle based on Integer32"""
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


_DBAProfile_FlagIdle_Type.__name__ = "Integer32"
_DBAProfile_FlagIdle_Object = MibScalar
dBAProfile_FlagIdle = _DBAProfile_FlagIdle_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 30),
    _DBAProfile_FlagIdle_Type()
)
dBAProfile_FlagIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_FlagIdle.setStatus("mandatory")


class _DBAProfile_oDynAlg_Type(Integer32):
    """Custom type dBAProfile_oDynAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("constant", 1),
          ("linear", 2),
          ("quadratic", 3))
    )


_DBAProfile_oDynAlg_Type.__name__ = "Integer32"
_DBAProfile_oDynAlg_Object = MibScalar
dBAProfile_oDynAlg = _DBAProfile_oDynAlg_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 31),
    _DBAProfile_oDynAlg_Type()
)
dBAProfile_oDynAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_oDynAlg.setStatus("mandatory")
_DBAProfile_SecondsOfHistory_Type = Integer32
_DBAProfile_SecondsOfHistory_Object = MibScalar
dBAProfile_SecondsOfHistory = _DBAProfile_SecondsOfHistory_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 32),
    _DBAProfile_SecondsOfHistory_Type()
)
dBAProfile_SecondsOfHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_SecondsOfHistory.setStatus("mandatory")
_DBAProfile_AddSecondsOfPersistence_Type = Integer32
_DBAProfile_AddSecondsOfPersistence_Object = MibScalar
dBAProfile_AddSecondsOfPersistence = _DBAProfile_AddSecondsOfPersistence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 33),
    _DBAProfile_AddSecondsOfPersistence_Type()
)
dBAProfile_AddSecondsOfPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_AddSecondsOfPersistence.setStatus("mandatory")
_DBAProfile_RemoveSecondsOfPersistence_Type = Integer32
_DBAProfile_RemoveSecondsOfPersistence_Object = MibScalar
dBAProfile_RemoveSecondsOfPersistence = _DBAProfile_RemoveSecondsOfPersistence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 34),
    _DBAProfile_RemoveSecondsOfPersistence_Type()
)
dBAProfile_RemoveSecondsOfPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_RemoveSecondsOfPersistence.setStatus("mandatory")
_DBAProfile_NailedUpGroup_Type = Integer32
_DBAProfile_NailedUpGroup_Object = MibScalar
dBAProfile_NailedUpGroup = _DBAProfile_NailedUpGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 35),
    _DBAProfile_NailedUpGroup_Type()
)
dBAProfile_NailedUpGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_NailedUpGroup.setStatus("mandatory")
_DBAProfile_CallPassword_Type = DisplayString
_DBAProfile_CallPassword_Object = MibScalar
dBAProfile_CallPassword = _DBAProfile_CallPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 36),
    _DBAProfile_CallPassword_Type()
)
dBAProfile_CallPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_CallPassword.setStatus("mandatory")
_DBAProfile_DbaPriNumberingPlanId_Type = Integer32
_DBAProfile_DbaPriNumberingPlanId_Object = MibScalar
dBAProfile_DbaPriNumberingPlanId = _DBAProfile_DbaPriNumberingPlanId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 37),
    _DBAProfile_DbaPriNumberingPlanId_Type()
)
dBAProfile_DbaPriNumberingPlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_DbaPriNumberingPlanId.setStatus("mandatory")


class _DBAProfile_Action_o_Type(Integer32):
    """Custom type dBAProfile_Action_o based on Integer32"""
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


_DBAProfile_Action_o_Type.__name__ = "Integer32"
_DBAProfile_Action_o_Object = MibScalar
dBAProfile_Action_o = _DBAProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 1, 1, 38),
    _DBAProfile_Action_o_Type()
)
dBAProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_Action_o.setStatus("mandatory")
_MibdBAProfile_TimerPeriodParametersTable_Object = MibTable
mibdBAProfile_TimerPeriodParametersTable = _MibdBAProfile_TimerPeriodParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2)
)
if mibBuilder.loadTexts:
    mibdBAProfile_TimerPeriodParametersTable.setStatus("mandatory")
_MibdBAProfile_TimerPeriodParametersEntry_Object = MibTableRow
mibdBAProfile_TimerPeriodParametersEntry = _MibdBAProfile_TimerPeriodParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1)
)
mibdBAProfile_TimerPeriodParametersEntry.setIndexNames(
    (0, "ASCEND-MIBDBA-MIB", "dBAProfile-TimerPeriodParameters-Shelf-o"),
    (0, "ASCEND-MIBDBA-MIB", "dBAProfile-TimerPeriodParameters-Slot-o"),
    (0, "ASCEND-MIBDBA-MIB", "dBAProfile-TimerPeriodParameters-Item-o"),
    (0, "ASCEND-MIBDBA-MIB", "dBAProfile-TimerPeriodParameters-LogicalItem-o"),
    (0, "ASCEND-MIBDBA-MIB", "dBAProfile-TimerPeriodParameters-Index-o"),
)
if mibBuilder.loadTexts:
    mibdBAProfile_TimerPeriodParametersEntry.setStatus("mandatory")
_DBAProfile_TimerPeriodParameters_Shelf_o_Type = Integer32
_DBAProfile_TimerPeriodParameters_Shelf_o_Object = MibScalar
dBAProfile_TimerPeriodParameters_Shelf_o = _DBAProfile_TimerPeriodParameters_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 1),
    _DBAProfile_TimerPeriodParameters_Shelf_o_Type()
)
dBAProfile_TimerPeriodParameters_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_Shelf_o.setStatus("mandatory")
_DBAProfile_TimerPeriodParameters_Slot_o_Type = Integer32
_DBAProfile_TimerPeriodParameters_Slot_o_Object = MibScalar
dBAProfile_TimerPeriodParameters_Slot_o = _DBAProfile_TimerPeriodParameters_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 2),
    _DBAProfile_TimerPeriodParameters_Slot_o_Type()
)
dBAProfile_TimerPeriodParameters_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_Slot_o.setStatus("mandatory")
_DBAProfile_TimerPeriodParameters_Item_o_Type = Integer32
_DBAProfile_TimerPeriodParameters_Item_o_Object = MibScalar
dBAProfile_TimerPeriodParameters_Item_o = _DBAProfile_TimerPeriodParameters_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 3),
    _DBAProfile_TimerPeriodParameters_Item_o_Type()
)
dBAProfile_TimerPeriodParameters_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_Item_o.setStatus("mandatory")
_DBAProfile_TimerPeriodParameters_LogicalItem_o_Type = Integer32
_DBAProfile_TimerPeriodParameters_LogicalItem_o_Object = MibScalar
dBAProfile_TimerPeriodParameters_LogicalItem_o = _DBAProfile_TimerPeriodParameters_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 4),
    _DBAProfile_TimerPeriodParameters_LogicalItem_o_Type()
)
dBAProfile_TimerPeriodParameters_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_LogicalItem_o.setStatus("mandatory")
_DBAProfile_TimerPeriodParameters_Index_o_Type = Integer32
_DBAProfile_TimerPeriodParameters_Index_o_Object = MibScalar
dBAProfile_TimerPeriodParameters_Index_o = _DBAProfile_TimerPeriodParameters_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 5),
    _DBAProfile_TimerPeriodParameters_Index_o_Type()
)
dBAProfile_TimerPeriodParameters_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_Index_o.setStatus("mandatory")


class _DBAProfile_TimerPeriodParameters_oActiv_Type(Integer32):
    """Custom type dBAProfile_TimerPeriodParameters_oActiv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("shutdown", 3))
    )


_DBAProfile_TimerPeriodParameters_oActiv_Type.__name__ = "Integer32"
_DBAProfile_TimerPeriodParameters_oActiv_Object = MibScalar
dBAProfile_TimerPeriodParameters_oActiv = _DBAProfile_TimerPeriodParameters_oActiv_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 6),
    _DBAProfile_TimerPeriodParameters_oActiv_Type()
)
dBAProfile_TimerPeriodParameters_oActiv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_oActiv.setStatus("mandatory")
_DBAProfile_TimerPeriodParameters_StartingTime_Type = Integer32
_DBAProfile_TimerPeriodParameters_StartingTime_Object = MibScalar
dBAProfile_TimerPeriodParameters_StartingTime = _DBAProfile_TimerPeriodParameters_StartingTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 7),
    _DBAProfile_TimerPeriodParameters_StartingTime_Type()
)
dBAProfile_TimerPeriodParameters_StartingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_StartingTime.setStatus("mandatory")
_DBAProfile_TimerPeriodParameters_MinimumChannelCount_Type = Integer32
_DBAProfile_TimerPeriodParameters_MinimumChannelCount_Object = MibScalar
dBAProfile_TimerPeriodParameters_MinimumChannelCount = _DBAProfile_TimerPeriodParameters_MinimumChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 8),
    _DBAProfile_TimerPeriodParameters_MinimumChannelCount_Type()
)
dBAProfile_TimerPeriodParameters_MinimumChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_MinimumChannelCount.setStatus("mandatory")
_DBAProfile_TimerPeriodParameters_MaximumChannelCount_Type = Integer32
_DBAProfile_TimerPeriodParameters_MaximumChannelCount_Object = MibScalar
dBAProfile_TimerPeriodParameters_MaximumChannelCount = _DBAProfile_TimerPeriodParameters_MaximumChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 9),
    _DBAProfile_TimerPeriodParameters_MaximumChannelCount_Type()
)
dBAProfile_TimerPeriodParameters_MaximumChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_MaximumChannelCount.setStatus("mandatory")
_DBAProfile_TimerPeriodParameters_TargetUtilization_Type = Integer32
_DBAProfile_TimerPeriodParameters_TargetUtilization_Object = MibScalar
dBAProfile_TimerPeriodParameters_TargetUtilization = _DBAProfile_TimerPeriodParameters_TargetUtilization_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 10),
    _DBAProfile_TimerPeriodParameters_TargetUtilization_Type()
)
dBAProfile_TimerPeriodParameters_TargetUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_TargetUtilization.setStatus("mandatory")
_DBAProfile_TimerPeriodParameters_X25chanTargetUtilization_Type = Integer32
_DBAProfile_TimerPeriodParameters_X25chanTargetUtilization_Object = MibScalar
dBAProfile_TimerPeriodParameters_X25chanTargetUtilization = _DBAProfile_TimerPeriodParameters_X25chanTargetUtilization_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 71, 2, 1, 11),
    _DBAProfile_TimerPeriodParameters_X25chanTargetUtilization_Type()
)
dBAProfile_TimerPeriodParameters_X25chanTargetUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dBAProfile_TimerPeriodParameters_X25chanTargetUtilization.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDBA-MIB",
    **{"DisplayString": DisplayString,
       "mibdBAProfile": mibdBAProfile,
       "mibdBAProfileTable": mibdBAProfileTable,
       "mibdBAProfileEntry": mibdBAProfileEntry,
       "dBAProfile-Shelf-o": dBAProfile_Shelf_o,
       "dBAProfile-Slot-o": dBAProfile_Slot_o,
       "dBAProfile-Item-o": dBAProfile_Item_o,
       "dBAProfile-LogicalItem-o": dBAProfile_LogicalItem_o,
       "dBAProfile-LogicalAddress-PhysicalAddress-Shelf": dBAProfile_LogicalAddress_PhysicalAddress_Shelf,
       "dBAProfile-LogicalAddress-PhysicalAddress-Slot": dBAProfile_LogicalAddress_PhysicalAddress_Slot,
       "dBAProfile-LogicalAddress-PhysicalAddress-ItemNumber": dBAProfile_LogicalAddress_PhysicalAddress_ItemNumber,
       "dBAProfile-LogicalAddress-LogicalItem": dBAProfile_LogicalAddress_LogicalItem,
       "dBAProfile-Name": dBAProfile_Name,
       "dBAProfile-PhoneNumber": dBAProfile_PhoneNumber,
       "dBAProfile-BillingNumber": dBAProfile_BillingNumber,
       "dBAProfile-oCallType": dBAProfile_oCallType,
       "dBAProfile-oCallMgm": dBAProfile_oCallMgm,
       "dBAProfile-oDataSvc": dBAProfile_oDataSvc,
       "dBAProfile-Force56": dBAProfile_Force56,
       "dBAProfile-BaseChannelCount": dBAProfile_BaseChannelCount,
       "dBAProfile-IncrementChannelCount": dBAProfile_IncrementChannelCount,
       "dBAProfile-DecrementChannelCount": dBAProfile_DecrementChannelCount,
       "dBAProfile-oFailAction": dBAProfile_oFailAction,
       "dBAProfile-BitInversionRequired": dBAProfile_BitInversionRequired,
       "dBAProfile-Ft1Caller": dBAProfile_Ft1Caller,
       "dBAProfile-Ft1Timeout": dBAProfile_Ft1Timeout,
       "dBAProfile-CallByCallID": dBAProfile_CallByCallID,
       "dBAProfile-CalledNumberType": dBAProfile_CalledNumberType,
       "dBAProfile-UnknownPlanUnknown": dBAProfile_UnknownPlanUnknown,
       "dBAProfile-LocalPlanIsdn": dBAProfile_LocalPlanIsdn,
       "dBAProfile-TransitNumber": dBAProfile_TransitNumber,
       "dBAProfile-oAutoBERT": dBAProfile_oAutoBERT,
       "dBAProfile-TimedCall": dBAProfile_TimedCall,
       "dBAProfile-FlagIdle": dBAProfile_FlagIdle,
       "dBAProfile-oDynAlg": dBAProfile_oDynAlg,
       "dBAProfile-SecondsOfHistory": dBAProfile_SecondsOfHistory,
       "dBAProfile-AddSecondsOfPersistence": dBAProfile_AddSecondsOfPersistence,
       "dBAProfile-RemoveSecondsOfPersistence": dBAProfile_RemoveSecondsOfPersistence,
       "dBAProfile-NailedUpGroup": dBAProfile_NailedUpGroup,
       "dBAProfile-CallPassword": dBAProfile_CallPassword,
       "dBAProfile-DbaPriNumberingPlanId": dBAProfile_DbaPriNumberingPlanId,
       "dBAProfile-Action-o": dBAProfile_Action_o,
       "mibdBAProfile-TimerPeriodParametersTable": mibdBAProfile_TimerPeriodParametersTable,
       "mibdBAProfile-TimerPeriodParametersEntry": mibdBAProfile_TimerPeriodParametersEntry,
       "dBAProfile-TimerPeriodParameters-Shelf-o": dBAProfile_TimerPeriodParameters_Shelf_o,
       "dBAProfile-TimerPeriodParameters-Slot-o": dBAProfile_TimerPeriodParameters_Slot_o,
       "dBAProfile-TimerPeriodParameters-Item-o": dBAProfile_TimerPeriodParameters_Item_o,
       "dBAProfile-TimerPeriodParameters-LogicalItem-o": dBAProfile_TimerPeriodParameters_LogicalItem_o,
       "dBAProfile-TimerPeriodParameters-Index-o": dBAProfile_TimerPeriodParameters_Index_o,
       "dBAProfile-TimerPeriodParameters-oActiv": dBAProfile_TimerPeriodParameters_oActiv,
       "dBAProfile-TimerPeriodParameters-StartingTime": dBAProfile_TimerPeriodParameters_StartingTime,
       "dBAProfile-TimerPeriodParameters-MinimumChannelCount": dBAProfile_TimerPeriodParameters_MinimumChannelCount,
       "dBAProfile-TimerPeriodParameters-MaximumChannelCount": dBAProfile_TimerPeriodParameters_MaximumChannelCount,
       "dBAProfile-TimerPeriodParameters-TargetUtilization": dBAProfile_TimerPeriodParameters_TargetUtilization,
       "dBAProfile-TimerPeriodParameters-X25chanTargetUtilization": dBAProfile_TimerPeriodParameters_X25chanTargetUtilization}
)
