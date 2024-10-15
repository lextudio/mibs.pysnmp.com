# SNMP MIB module (IBM2212-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM2212-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:43 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm2212_ObjectIdentity = ObjectIdentity
ibm2212 = _Ibm2212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149)
)
_Ibm2212admin_ObjectIdentity = ObjectIdentity
ibm2212admin = _Ibm2212admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 1)
)
_Ibm2212adminproducts_ObjectIdentity = ObjectIdentity
ibm2212adminproducts = _Ibm2212adminproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 1, 1)
)
_Ibm2212adminOID_ObjectIdentity = ObjectIdentity
ibm2212adminOID = _Ibm2212adminOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 1, 2)
)
_Ibm2212EnetChipSet_ObjectIdentity = ObjectIdentity
ibm2212EnetChipSet = _Ibm2212EnetChipSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 1, 2, 1)
)
_EnetChipSetUnknown_ObjectIdentity = ObjectIdentity
enetChipSetUnknown = _EnetChipSetUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 1, 2, 1, 1)
)
_EnetChipSetAMD_ObjectIdentity = ObjectIdentity
enetChipSetAMD = _EnetChipSetAMD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 1, 2, 1, 2)
)
_Ibm2212adminDebug_ObjectIdentity = ObjectIdentity
ibm2212adminDebug = _Ibm2212adminDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 1, 3)
)
_Ibm2212system_ObjectIdentity = ObjectIdentity
ibm2212system = _Ibm2212system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 2)
)
_Ibm2212systemInfo_ObjectIdentity = ObjectIdentity
ibm2212systemInfo = _Ibm2212systemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 2, 1)
)
_Ibm2212cfgInfo_ObjectIdentity = ObjectIdentity
ibm2212cfgInfo = _Ibm2212cfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 2, 2)
)
_Ibm2212hardware_ObjectIdentity = ObjectIdentity
ibm2212hardware = _Ibm2212hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3)
)
_Ibm2212hardwareGeneral_ObjectIdentity = ObjectIdentity
ibm2212hardwareGeneral = _Ibm2212hardwareGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1)
)
_Ibm2212AdapTable_Object = MibTable
ibm2212AdapTable = _Ibm2212AdapTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibm2212AdapTable.setStatus("mandatory")
_Ibm2212AdapEntry_Object = MibTableRow
ibm2212AdapEntry = _Ibm2212AdapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1, 1, 1)
)
ibm2212AdapEntry.setIndexNames(
    (0, "IBM2212-MIB", "ibm2212AdapSlotNum"),
)
if mibBuilder.loadTexts:
    ibm2212AdapEntry.setStatus("mandatory")


class _Ibm2212AdapSlotNum_Type(Integer32):
    """Custom type ibm2212AdapSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ibm2212AdapSlotNum_Type.__name__ = "Integer32"
_Ibm2212AdapSlotNum_Object = MibTableColumn
ibm2212AdapSlotNum = _Ibm2212AdapSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1, 1, 1, 1),
    _Ibm2212AdapSlotNum_Type()
)
ibm2212AdapSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2212AdapSlotNum.setStatus("mandatory")


class _Ibm2212AdapType_Type(Integer32):
    """Custom type ibm2212AdapType based on Integer32"""
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
        *(("compression-encryption", 12),
          ("eth-fast-1port", 3),
          ("eth-fast-2port", 5),
          ("isdn-bri-st-2port", 9),
          ("isdn-bri-u-2port", 8),
          ("isdn-pri-e1-1port", 11),
          ("isdn-pri-e1-2port", 15),
          ("isdn-pri-t1j1-1port", 10),
          ("isdn-pri-t1j1-2port", 14),
          ("not-present", 2),
          ("serial-4port-deep", 13),
          ("serial-4port-shallow", 7),
          ("token-ring-1port", 4),
          ("token-ring-2port", 6),
          ("unknown", 1))
    )


_Ibm2212AdapType_Type.__name__ = "Integer32"
_Ibm2212AdapType_Object = MibTableColumn
ibm2212AdapType = _Ibm2212AdapType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1, 1, 1, 2),
    _Ibm2212AdapType_Type()
)
ibm2212AdapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2212AdapType.setStatus("mandatory")


class _Ibm2212AdapOperStatus_Type(Integer32):
    """Custom type ibm2212AdapOperStatus based on Integer32"""
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
        *(("enable-pending", 3),
          ("enabled", 4),
          ("hardware-error", 6),
          ("not-powered", 7),
          ("not-present", 2),
          ("unknown", 1),
          ("unknown-device", 5))
    )


_Ibm2212AdapOperStatus_Type.__name__ = "Integer32"
_Ibm2212AdapOperStatus_Object = MibTableColumn
ibm2212AdapOperStatus = _Ibm2212AdapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1, 1, 1, 3),
    _Ibm2212AdapOperStatus_Type()
)
ibm2212AdapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2212AdapOperStatus.setStatus("mandatory")
_Ibm2212GraphicTable_Object = MibTable
ibm2212GraphicTable = _Ibm2212GraphicTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ibm2212GraphicTable.setStatus("mandatory")
_Ibm2212GraphicEntry_Object = MibTableRow
ibm2212GraphicEntry = _Ibm2212GraphicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1, 2, 1)
)
ibm2212GraphicEntry.setIndexNames(
    (0, "IBM2212-MIB", "ibm2212GraphicSlotNum"),
    (0, "IBM2212-MIB", "ibm2212GraphicPortNum"),
)
if mibBuilder.loadTexts:
    ibm2212GraphicEntry.setStatus("mandatory")


class _Ibm2212GraphicSlotNum_Type(Integer32):
    """Custom type ibm2212GraphicSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ibm2212GraphicSlotNum_Type.__name__ = "Integer32"
_Ibm2212GraphicSlotNum_Object = MibTableColumn
ibm2212GraphicSlotNum = _Ibm2212GraphicSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1, 2, 1, 1),
    _Ibm2212GraphicSlotNum_Type()
)
ibm2212GraphicSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2212GraphicSlotNum.setStatus("mandatory")


class _Ibm2212GraphicPortNum_Type(Integer32):
    """Custom type ibm2212GraphicPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ibm2212GraphicPortNum_Type.__name__ = "Integer32"
_Ibm2212GraphicPortNum_Object = MibTableColumn
ibm2212GraphicPortNum = _Ibm2212GraphicPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1, 2, 1, 2),
    _Ibm2212GraphicPortNum_Type()
)
ibm2212GraphicPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2212GraphicPortNum.setStatus("mandatory")
_Ibm2212GraphicifIndex_Type = Integer32
_Ibm2212GraphicifIndex_Object = MibTableColumn
ibm2212GraphicifIndex = _Ibm2212GraphicifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 3, 1, 2, 1, 3),
    _Ibm2212GraphicifIndex_Type()
)
ibm2212GraphicifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2212GraphicifIndex.setStatus("mandatory")
_Ibm2212routing_ObjectIdentity = ObjectIdentity
ibm2212routing = _Ibm2212routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 4)
)
_Ibm2212switching_ObjectIdentity = ObjectIdentity
ibm2212switching = _Ibm2212switching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 149, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM2212-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm2212": ibm2212,
       "ibm2212admin": ibm2212admin,
       "ibm2212adminproducts": ibm2212adminproducts,
       "ibm2212adminOID": ibm2212adminOID,
       "ibm2212EnetChipSet": ibm2212EnetChipSet,
       "enetChipSetUnknown": enetChipSetUnknown,
       "enetChipSetAMD": enetChipSetAMD,
       "ibm2212adminDebug": ibm2212adminDebug,
       "ibm2212system": ibm2212system,
       "ibm2212systemInfo": ibm2212systemInfo,
       "ibm2212cfgInfo": ibm2212cfgInfo,
       "ibm2212hardware": ibm2212hardware,
       "ibm2212hardwareGeneral": ibm2212hardwareGeneral,
       "ibm2212AdapTable": ibm2212AdapTable,
       "ibm2212AdapEntry": ibm2212AdapEntry,
       "ibm2212AdapSlotNum": ibm2212AdapSlotNum,
       "ibm2212AdapType": ibm2212AdapType,
       "ibm2212AdapOperStatus": ibm2212AdapOperStatus,
       "ibm2212GraphicTable": ibm2212GraphicTable,
       "ibm2212GraphicEntry": ibm2212GraphicEntry,
       "ibm2212GraphicSlotNum": ibm2212GraphicSlotNum,
       "ibm2212GraphicPortNum": ibm2212GraphicPortNum,
       "ibm2212GraphicifIndex": ibm2212GraphicifIndex,
       "ibm2212routing": ibm2212routing,
       "ibm2212switching": ibm2212switching}
)
