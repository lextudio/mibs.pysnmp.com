# SNMP MIB module (IBM2216-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM2216-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:44 2024
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
_Ibm2216_ObjectIdentity = ObjectIdentity
ibm2216 = _Ibm2216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131)
)
_Ibm2216admin_ObjectIdentity = ObjectIdentity
ibm2216admin = _Ibm2216admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 1)
)
_Ibm2216adminproducts_ObjectIdentity = ObjectIdentity
ibm2216adminproducts = _Ibm2216adminproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 1)
)
_Ibm2216mod400_ObjectIdentity = ObjectIdentity
ibm2216mod400 = _Ibm2216mod400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 1, 1)
)
_Ibm2216adminOID_ObjectIdentity = ObjectIdentity
ibm2216adminOID = _Ibm2216adminOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 2)
)
_Ibm2216EnetChipSet_ObjectIdentity = ObjectIdentity
ibm2216EnetChipSet = _Ibm2216EnetChipSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 2, 1)
)
_EnetChipSetToshiba_ObjectIdentity = ObjectIdentity
enetChipSetToshiba = _EnetChipSetToshiba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 2, 1, 1)
)
_EnetChipSetAMD_ObjectIdentity = ObjectIdentity
enetChipSetAMD = _EnetChipSetAMD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 2, 1, 2)
)
_Ibm2216adminDebug_ObjectIdentity = ObjectIdentity
ibm2216adminDebug = _Ibm2216adminDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 3)
)
_Ibm2216system_ObjectIdentity = ObjectIdentity
ibm2216system = _Ibm2216system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 2)
)
_Ibm2216systemInfo_ObjectIdentity = ObjectIdentity
ibm2216systemInfo = _Ibm2216systemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 2, 1)
)
_Ibm2216cfgInfo_ObjectIdentity = ObjectIdentity
ibm2216cfgInfo = _Ibm2216cfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 2, 2)
)
_Ibm2216hardware_ObjectIdentity = ObjectIdentity
ibm2216hardware = _Ibm2216hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3)
)
_Ibm2216hardwareGeneral_ObjectIdentity = ObjectIdentity
ibm2216hardwareGeneral = _Ibm2216hardwareGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1)
)
_Ibm2216PCIAdapTable_Object = MibTable
ibm2216PCIAdapTable = _Ibm2216PCIAdapTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibm2216PCIAdapTable.setStatus("mandatory")
_Ibm2216PCIAdapEntry_Object = MibTableRow
ibm2216PCIAdapEntry = _Ibm2216PCIAdapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 1, 1)
)
ibm2216PCIAdapEntry.setIndexNames(
    (0, "IBM2216-MIB", "ibm2216PCIAdapSlotNum"),
)
if mibBuilder.loadTexts:
    ibm2216PCIAdapEntry.setStatus("mandatory")


class _Ibm2216PCIAdapSlotNum_Type(Integer32):
    """Custom type ibm2216PCIAdapSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ibm2216PCIAdapSlotNum_Type.__name__ = "Integer32"
_Ibm2216PCIAdapSlotNum_Object = MibTableColumn
ibm2216PCIAdapSlotNum = _Ibm2216PCIAdapSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 1, 1, 1),
    _Ibm2216PCIAdapSlotNum_Type()
)
ibm2216PCIAdapSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2216PCIAdapSlotNum.setStatus("mandatory")


class _Ibm2216PCIAdapType_Type(Integer32):
    """Custom type ibm2216PCIAdapType based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("atm-mmf-lic284", 4),
          ("atm-mmf-lic294", 3),
          ("atm-smf-lic293", 6),
          ("atm-smf-lic295", 5),
          ("escon-lic287", 8),
          ("ethernet-fast-lic288", 15),
          ("ethernet-lic281", 14),
          ("fddi-lic286", 17),
          ("isdn-e1-lic292", 10),
          ("isdn-e1-lic298", 19),
          ("isdn-t1j1-lic283", 9),
          ("isdn-t1j1-lic297", 18),
          ("not-present", 2),
          ("parallel-channel-lic299", 20),
          ("serial-hssi-lic289", 16),
          ("serial-rs232-lic282", 11),
          ("serial-v35-lic290", 12),
          ("serial-x21-lic291", 13),
          ("token-ring-lic280", 7),
          ("unknown", 1))
    )


_Ibm2216PCIAdapType_Type.__name__ = "Integer32"
_Ibm2216PCIAdapType_Object = MibTableColumn
ibm2216PCIAdapType = _Ibm2216PCIAdapType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 1, 1, 2),
    _Ibm2216PCIAdapType_Type()
)
ibm2216PCIAdapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2216PCIAdapType.setStatus("mandatory")


class _Ibm2216PCIAdapOperStatus_Type(Integer32):
    """Custom type ibm2216PCIAdapOperStatus based on Integer32"""
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
        *(("diagnostics", 13),
          ("disable-pending", 7),
          ("disabled", 8),
          ("does-not-apply", 4),
          ("enable-pending", 5),
          ("enabled", 6),
          ("hardware-error", 11),
          ("mis-configured", 15),
          ("not-configured", 2),
          ("not-initialized", 9),
          ("not-powered", 12),
          ("not-present", 3),
          ("unknown", 1),
          ("unknown-device", 10),
          ("wrs-available", 14))
    )


_Ibm2216PCIAdapOperStatus_Type.__name__ = "Integer32"
_Ibm2216PCIAdapOperStatus_Object = MibTableColumn
ibm2216PCIAdapOperStatus = _Ibm2216PCIAdapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 1, 1, 3),
    _Ibm2216PCIAdapOperStatus_Type()
)
ibm2216PCIAdapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2216PCIAdapOperStatus.setStatus("mandatory")
_Ibm2216GraphicTable_Object = MibTable
ibm2216GraphicTable = _Ibm2216GraphicTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ibm2216GraphicTable.setStatus("mandatory")
_Ibm2216GraphicEntry_Object = MibTableRow
ibm2216GraphicEntry = _Ibm2216GraphicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 2, 1)
)
ibm2216GraphicEntry.setIndexNames(
    (0, "IBM2216-MIB", "ibm2216GraphicSlotNum"),
    (0, "IBM2216-MIB", "ibm2216GraphicPortNum"),
)
if mibBuilder.loadTexts:
    ibm2216GraphicEntry.setStatus("mandatory")


class _Ibm2216GraphicSlotNum_Type(Integer32):
    """Custom type ibm2216GraphicSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ibm2216GraphicSlotNum_Type.__name__ = "Integer32"
_Ibm2216GraphicSlotNum_Object = MibTableColumn
ibm2216GraphicSlotNum = _Ibm2216GraphicSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 2, 1, 1),
    _Ibm2216GraphicSlotNum_Type()
)
ibm2216GraphicSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2216GraphicSlotNum.setStatus("mandatory")


class _Ibm2216GraphicPortNum_Type(Integer32):
    """Custom type ibm2216GraphicPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Ibm2216GraphicPortNum_Type.__name__ = "Integer32"
_Ibm2216GraphicPortNum_Object = MibTableColumn
ibm2216GraphicPortNum = _Ibm2216GraphicPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 2, 1, 2),
    _Ibm2216GraphicPortNum_Type()
)
ibm2216GraphicPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2216GraphicPortNum.setStatus("mandatory")
_Ibm2216GraphicifIndex_Type = Integer32
_Ibm2216GraphicifIndex_Object = MibTableColumn
ibm2216GraphicifIndex = _Ibm2216GraphicifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 2, 1, 3),
    _Ibm2216GraphicifIndex_Type()
)
ibm2216GraphicifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibm2216GraphicifIndex.setStatus("mandatory")
_Ibm2216hardware400Specific_ObjectIdentity = ObjectIdentity
ibm2216hardware400Specific = _Ibm2216hardware400Specific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 2)
)
_Ibm2216routing_ObjectIdentity = ObjectIdentity
ibm2216routing = _Ibm2216routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 4)
)
_Ibm2216switching_ObjectIdentity = ObjectIdentity
ibm2216switching = _Ibm2216switching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 131, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM2216-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm2216": ibm2216,
       "ibm2216admin": ibm2216admin,
       "ibm2216adminproducts": ibm2216adminproducts,
       "ibm2216mod400": ibm2216mod400,
       "ibm2216adminOID": ibm2216adminOID,
       "ibm2216EnetChipSet": ibm2216EnetChipSet,
       "enetChipSetToshiba": enetChipSetToshiba,
       "enetChipSetAMD": enetChipSetAMD,
       "ibm2216adminDebug": ibm2216adminDebug,
       "ibm2216system": ibm2216system,
       "ibm2216systemInfo": ibm2216systemInfo,
       "ibm2216cfgInfo": ibm2216cfgInfo,
       "ibm2216hardware": ibm2216hardware,
       "ibm2216hardwareGeneral": ibm2216hardwareGeneral,
       "ibm2216PCIAdapTable": ibm2216PCIAdapTable,
       "ibm2216PCIAdapEntry": ibm2216PCIAdapEntry,
       "ibm2216PCIAdapSlotNum": ibm2216PCIAdapSlotNum,
       "ibm2216PCIAdapType": ibm2216PCIAdapType,
       "ibm2216PCIAdapOperStatus": ibm2216PCIAdapOperStatus,
       "ibm2216GraphicTable": ibm2216GraphicTable,
       "ibm2216GraphicEntry": ibm2216GraphicEntry,
       "ibm2216GraphicSlotNum": ibm2216GraphicSlotNum,
       "ibm2216GraphicPortNum": ibm2216GraphicPortNum,
       "ibm2216GraphicifIndex": ibm2216GraphicifIndex,
       "ibm2216hardware400Specific": ibm2216hardware400Specific,
       "ibm2216routing": ibm2216routing,
       "ibm2216switching": ibm2216switching}
)
