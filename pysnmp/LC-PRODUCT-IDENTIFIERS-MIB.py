# SNMP MIB module (LC-PRODUCT-IDENTIFIERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LC-PRODUCT-IDENTIFIERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:33 2024
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

(lancastMibModulesA,) = mibBuilder.importSymbols(
    "LANCAST-MIB",
    "lancastMibModulesA")

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

productIdentifiers = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4)
)
productIdentifiers.setRevisions(
        ("1999-07-16 12:00",
         "1999-07-08 12:00",
         "1999-03-03 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChassisIdentifiers_ObjectIdentity = ObjectIdentity
chassisIdentifiers = _ChassisIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2)
)
_Lc7500Chassis_ObjectIdentity = ObjectIdentity
lc7500Chassis = _Lc7500Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 1)
)
_TwelveSlot2PS750012_Type = ObjectIdentifier
_TwelveSlot2PS750012_Object = MibScalar
twelveSlot2PS750012 = _TwelveSlot2PS750012_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 1, 1),
    _TwelveSlot2PS750012_Type()
)
twelveSlot2PS750012.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twelveSlot2PS750012.setStatus("current")
_ThirteenSlotTelco2PS750013_Type = ObjectIdentifier
_ThirteenSlotTelco2PS750013_Object = MibScalar
thirteenSlotTelco2PS750013 = _ThirteenSlotTelco2PS750013_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 1, 2),
    _ThirteenSlotTelco2PS750013_Type()
)
thirteenSlotTelco2PS750013.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thirteenSlotTelco2PS750013.setStatus("current")
_SeventeenSlot1PSFixed75001701_Type = ObjectIdentifier
_SeventeenSlot1PSFixed75001701_Object = MibScalar
seventeenSlot1PSFixed75001701 = _SeventeenSlot1PSFixed75001701_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 1, 3),
    _SeventeenSlot1PSFixed75001701_Type()
)
seventeenSlot1PSFixed75001701.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    seventeenSlot1PSFixed75001701.setStatus("current")
_SeventeenSlot2PSFixed75001702_Type = ObjectIdentifier
_SeventeenSlot2PSFixed75001702_Object = MibScalar
seventeenSlot2PSFixed75001702 = _SeventeenSlot2PSFixed75001702_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 1, 4),
    _SeventeenSlot2PSFixed75001702_Type()
)
seventeenSlot2PSFixed75001702.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    seventeenSlot2PSFixed75001702.setStatus("current")
_SeventeenSlot2PSHotSwapSwitch750017DX_Type = ObjectIdentifier
_SeventeenSlot2PSHotSwapSwitch750017DX_Object = MibScalar
seventeenSlot2PSHotSwapSwitch750017DX = _SeventeenSlot2PSHotSwapSwitch750017DX_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 1, 5),
    _SeventeenSlot2PSHotSwapSwitch750017DX_Type()
)
seventeenSlot2PSHotSwapSwitch750017DX.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    seventeenSlot2PSHotSwapSwitch750017DX.setStatus("current")
_Oem17500Chassis_ObjectIdentity = ObjectIdentity
oem17500Chassis = _Oem17500Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 2)
)
_Oem1TwelveSlot2PS750012_Type = ObjectIdentifier
_Oem1TwelveSlot2PS750012_Object = MibScalar
oem1TwelveSlot2PS750012 = _Oem1TwelveSlot2PS750012_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 2, 1),
    _Oem1TwelveSlot2PS750012_Type()
)
oem1TwelveSlot2PS750012.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oem1TwelveSlot2PS750012.setStatus("current")
_Oem1SeventeenSlot1PSFixed75001701_Type = ObjectIdentifier
_Oem1SeventeenSlot1PSFixed75001701_Object = MibScalar
oem1SeventeenSlot1PSFixed75001701 = _Oem1SeventeenSlot1PSFixed75001701_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 2, 2),
    _Oem1SeventeenSlot1PSFixed75001701_Type()
)
oem1SeventeenSlot1PSFixed75001701.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oem1SeventeenSlot1PSFixed75001701.setStatus("current")
_Oem1SeventeenSlot2PSFixed75001702_Type = ObjectIdentifier
_Oem1SeventeenSlot2PSFixed75001702_Object = MibScalar
oem1SeventeenSlot2PSFixed75001702 = _Oem1SeventeenSlot2PSFixed75001702_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 2, 3),
    _Oem1SeventeenSlot2PSFixed75001702_Type()
)
oem1SeventeenSlot2PSFixed75001702.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oem1SeventeenSlot2PSFixed75001702.setStatus("current")
_Oem1SeventeenSlot2PSHotSwapSwitch750017DX_Type = ObjectIdentifier
_Oem1SeventeenSlot2PSHotSwapSwitch750017DX_Object = MibScalar
oem1SeventeenSlot2PSHotSwapSwitch750017DX = _Oem1SeventeenSlot2PSHotSwapSwitch750017DX_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 2, 2, 4),
    _Oem1SeventeenSlot2PSHotSwapSwitch750017DX_Type()
)
oem1SeventeenSlot2PSHotSwapSwitch750017DX.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oem1SeventeenSlot2PSHotSwapSwitch750017DX.setStatus("current")
_PowerSupplyIdentifiers_ObjectIdentity = ObjectIdentity
powerSupplyIdentifiers = _PowerSupplyIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 3)
)
_Lc7500PowerSupply_ObjectIdentity = ObjectIdentity
lc7500PowerSupply = _Lc7500PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 3, 1)
)
_AcPowerSupply7500AC_Type = ObjectIdentifier
_AcPowerSupply7500AC_Object = MibScalar
acPowerSupply7500AC = _AcPowerSupply7500AC_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 3, 1, 1),
    _AcPowerSupply7500AC_Type()
)
acPowerSupply7500AC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPowerSupply7500AC.setStatus("current")
_DcPowerSupply7500DC_Type = ObjectIdentifier
_DcPowerSupply7500DC_Object = MibScalar
dcPowerSupply7500DC = _DcPowerSupply7500DC_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 3, 1, 2),
    _DcPowerSupply7500DC_Type()
)
dcPowerSupply7500DC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcPowerSupply7500DC.setStatus("current")
_ModuleIdentifiers_ObjectIdentity = ObjectIdentity
moduleIdentifiers = _ModuleIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4)
)
_MgmntModuleIdentifiers_ObjectIdentity = ObjectIdentity
mgmntModuleIdentifiers = _MgmntModuleIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 1)
)
_SingleEthernetMgmntModule7501M_Type = ObjectIdentifier
_SingleEthernetMgmntModule7501M_Object = MibScalar
singleEthernetMgmntModule7501M = _SingleEthernetMgmntModule7501M_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 1, 1),
    _SingleEthernetMgmntModule7501M_Type()
)
singleEthernetMgmntModule7501M.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    singleEthernetMgmntModule7501M.setStatus("current")
_DualEthernetMgmntModule7502M_Type = ObjectIdentifier
_DualEthernetMgmntModule7502M_Object = MibScalar
dualEthernetMgmntModule7502M = _DualEthernetMgmntModule7502M_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 1, 2),
    _DualEthernetMgmntModule7502M_Type()
)
dualEthernetMgmntModule7502M.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dualEthernetMgmntModule7502M.setStatus("current")
_RedundantMgmntModule7501RM_Type = ObjectIdentifier
_RedundantMgmntModule7501RM_Object = MibScalar
redundantMgmntModule7501RM = _RedundantMgmntModule7501RM_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 1, 3),
    _RedundantMgmntModule7501RM_Type()
)
redundantMgmntModule7501RM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redundantMgmntModule7501RM.setStatus("current")
_SingleTwisterIdentifiers_ObjectIdentity = ObjectIdentity
singleTwisterIdentifiers = _SingleTwisterIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2)
)
_TpToBnc10MSingleTwisterModule71111275_Type = ObjectIdentifier
_TpToBnc10MSingleTwisterModule71111275_Object = MibScalar
tpToBnc10MSingleTwisterModule71111275 = _TpToBnc10MSingleTwisterModule71111275_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 1),
    _TpToBnc10MSingleTwisterModule71111275_Type()
)
tpToBnc10MSingleTwisterModule71111275.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpToBnc10MSingleTwisterModule71111275.setStatus("current")
_TpToFlMmSt10MSingleTwisterModule71111575_Type = ObjectIdentifier
_TpToFlMmSt10MSingleTwisterModule71111575_Object = MibScalar
tpToFlMmSt10MSingleTwisterModule71111575 = _TpToFlMmSt10MSingleTwisterModule71111575_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 2),
    _TpToFlMmSt10MSingleTwisterModule71111575_Type()
)
tpToFlMmSt10MSingleTwisterModule71111575.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpToFlMmSt10MSingleTwisterModule71111575.setStatus("current")
_TpToFlSmSt10MSingleTwisterModule71111675_Type = ObjectIdentifier
_TpToFlSmSt10MSingleTwisterModule71111675_Object = MibScalar
tpToFlSmSt10MSingleTwisterModule71111675 = _TpToFlSmSt10MSingleTwisterModule71111675_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 3),
    _TpToFlSmSt10MSingleTwisterModule71111675_Type()
)
tpToFlSmSt10MSingleTwisterModule71111675.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpToFlSmSt10MSingleTwisterModule71111675.setStatus("current")
_TpToSmaMm10MSingleTwisterModule71111875_Type = ObjectIdentifier
_TpToSmaMm10MSingleTwisterModule71111875_Object = MibScalar
tpToSmaMm10MSingleTwisterModule71111875 = _TpToSmaMm10MSingleTwisterModule71111875_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 4),
    _TpToSmaMm10MSingleTwisterModule71111875_Type()
)
tpToSmaMm10MSingleTwisterModule71111875.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpToSmaMm10MSingleTwisterModule71111875.setStatus("current")
_TxToFxMmSc100MSingleTwisterModule71311375_Type = ObjectIdentifier
_TxToFxMmSc100MSingleTwisterModule71311375_Object = MibScalar
txToFxMmSc100MSingleTwisterModule71311375 = _TxToFxMmSc100MSingleTwisterModule71311375_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 5),
    _TxToFxMmSc100MSingleTwisterModule71311375_Type()
)
txToFxMmSc100MSingleTwisterModule71311375.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToFxMmSc100MSingleTwisterModule71311375.setStatus("current")
_TxToFxMmSt100MSingleTwisterModule71311575_Type = ObjectIdentifier
_TxToFxMmSt100MSingleTwisterModule71311575_Object = MibScalar
txToFxMmSt100MSingleTwisterModule71311575 = _TxToFxMmSt100MSingleTwisterModule71311575_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 6),
    _TxToFxMmSt100MSingleTwisterModule71311575_Type()
)
txToFxMmSt100MSingleTwisterModule71311575.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToFxMmSt100MSingleTwisterModule71311575.setStatus("current")
_TxToFxSmSc100MSingleTwisterModule71311475_Type = ObjectIdentifier
_TxToFxSmSc100MSingleTwisterModule71311475_Object = MibScalar
txToFxSmSc100MSingleTwisterModule71311475 = _TxToFxSmSc100MSingleTwisterModule71311475_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 7),
    _TxToFxSmSc100MSingleTwisterModule71311475_Type()
)
txToFxSmSc100MSingleTwisterModule71311475.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToFxSmSc100MSingleTwisterModule71311475.setStatus("current")
_TxToFxSmSc40Km100MSingleTwisterModule71311775_Type = ObjectIdentifier
_TxToFxSmSc40Km100MSingleTwisterModule71311775_Object = MibScalar
txToFxSmSc40Km100MSingleTwisterModule71311775 = _TxToFxSmSc40Km100MSingleTwisterModule71311775_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 8),
    _TxToFxSmSc40Km100MSingleTwisterModule71311775_Type()
)
txToFxSmSc40Km100MSingleTwisterModule71311775.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToFxSmSc40Km100MSingleTwisterModule71311775.setStatus("current")
_FxMmScToFxSmSc100MSingleTwisterModule71313475_Type = ObjectIdentifier
_FxMmScToFxSmSc100MSingleTwisterModule71313475_Object = MibScalar
fxMmScToFxSmSc100MSingleTwisterModule71313475 = _FxMmScToFxSmSc100MSingleTwisterModule71313475_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 9),
    _FxMmScToFxSmSc100MSingleTwisterModule71313475_Type()
)
fxMmScToFxSmSc100MSingleTwisterModule71313475.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fxMmScToFxSmSc100MSingleTwisterModule71313475.setStatus("current")
_FxMmStToFxSmSc100MSingleTwisterModule71315475_Type = ObjectIdentifier
_FxMmStToFxSmSc100MSingleTwisterModule71315475_Object = MibScalar
fxMmStToFxSmSc100MSingleTwisterModule71315475 = _FxMmStToFxSmSc100MSingleTwisterModule71315475_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 10),
    _FxMmStToFxSmSc100MSingleTwisterModule71315475_Type()
)
fxMmStToFxSmSc100MSingleTwisterModule71315475.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fxMmStToFxSmSc100MSingleTwisterModule71315475.setStatus("current")
_TxToFxSmSt100MSingleTwisterModule71311675_Type = ObjectIdentifier
_TxToFxSmSt100MSingleTwisterModule71311675_Object = MibScalar
txToFxSmSt100MSingleTwisterModule71311675 = _TxToFxSmSt100MSingleTwisterModule71311675_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 11),
    _TxToFxSmSt100MSingleTwisterModule71311675_Type()
)
txToFxSmSt100MSingleTwisterModule71311675.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToFxSmSt100MSingleTwisterModule71311675.setStatus("current")
_FxMmScToFxSmSt100MSingleTwisterModule71313675_Type = ObjectIdentifier
_FxMmScToFxSmSt100MSingleTwisterModule71313675_Object = MibScalar
fxMmScToFxSmSt100MSingleTwisterModule71313675 = _FxMmScToFxSmSt100MSingleTwisterModule71313675_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 12),
    _FxMmScToFxSmSt100MSingleTwisterModule71313675_Type()
)
fxMmScToFxSmSt100MSingleTwisterModule71313675.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fxMmScToFxSmSt100MSingleTwisterModule71313675.setStatus("current")
_FxMmStToFxSmSt100MSingleTwisterModule71315675_Type = ObjectIdentifier
_FxMmStToFxSmSt100MSingleTwisterModule71315675_Object = MibScalar
fxMmStToFxSmSt100MSingleTwisterModule71315675 = _FxMmStToFxSmSt100MSingleTwisterModule71315675_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 13),
    _FxMmStToFxSmSt100MSingleTwisterModule71315675_Type()
)
fxMmStToFxSmSt100MSingleTwisterModule71315675.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fxMmStToFxSmSt100MSingleTwisterModule71315675.setStatus("current")
_TpToTp10MSingleTwisterModule78111175_Type = ObjectIdentifier
_TpToTp10MSingleTwisterModule78111175_Object = MibScalar
tpToTp10MSingleTwisterModule78111175 = _TpToTp10MSingleTwisterModule78111175_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 14),
    _TpToTp10MSingleTwisterModule78111175_Type()
)
tpToTp10MSingleTwisterModule78111175.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpToTp10MSingleTwisterModule78111175.setStatus("current")
_TpToMmSc10MSingleTwisterModule71111375_Type = ObjectIdentifier
_TpToMmSc10MSingleTwisterModule71111375_Object = MibScalar
tpToMmSc10MSingleTwisterModule71111375 = _TpToMmSc10MSingleTwisterModule71111375_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 15),
    _TpToMmSc10MSingleTwisterModule71111375_Type()
)
tpToMmSc10MSingleTwisterModule71111375.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpToMmSc10MSingleTwisterModule71111375.setStatus("current")
_TxToTx10MSingleTwisterModule78311175_Type = ObjectIdentifier
_TxToTx10MSingleTwisterModule78311175_Object = MibScalar
txToTx10MSingleTwisterModule78311175 = _TxToTx10MSingleTwisterModule78311175_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 16),
    _TxToTx10MSingleTwisterModule78311175_Type()
)
txToTx10MSingleTwisterModule78311175.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToTx10MSingleTwisterModule78311175.setStatus("current")
_MmScToMmSc100MSingleTwisterModule78313375_Type = ObjectIdentifier
_MmScToMmSc100MSingleTwisterModule78313375_Object = MibScalar
mmScToMmSc100MSingleTwisterModule78313375 = _MmScToMmSc100MSingleTwisterModule78313375_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 17),
    _MmScToMmSc100MSingleTwisterModule78313375_Type()
)
mmScToMmSc100MSingleTwisterModule78313375.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmScToMmSc100MSingleTwisterModule78313375.setStatus("current")
_MmStToMmSt100MSingleTwisterModule78315575_Type = ObjectIdentifier
_MmStToMmSt100MSingleTwisterModule78315575_Object = MibScalar
mmStToMmSt100MSingleTwisterModule78315575 = _MmStToMmSt100MSingleTwisterModule78315575_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 18),
    _MmStToMmSt100MSingleTwisterModule78315575_Type()
)
mmStToMmSt100MSingleTwisterModule78315575.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmStToMmSt100MSingleTwisterModule78315575.setStatus("current")
_TxToMmScSx100MSingleTwisterModule71311A75_Type = ObjectIdentifier
_TxToMmScSx100MSingleTwisterModule71311A75_Object = MibScalar
txToMmScSx100MSingleTwisterModule71311A75 = _TxToMmScSx100MSingleTwisterModule71311A75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 19),
    _TxToMmScSx100MSingleTwisterModule71311A75_Type()
)
txToMmScSx100MSingleTwisterModule71311A75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToMmScSx100MSingleTwisterModule71311A75.setStatus("current")
_TxToMmStSx100MSingleTwisterModule71311B75_Type = ObjectIdentifier
_TxToMmStSx100MSingleTwisterModule71311B75_Object = MibScalar
txToMmStSx100MSingleTwisterModule71311B75 = _TxToMmStSx100MSingleTwisterModule71311B75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 20),
    _TxToMmStSx100MSingleTwisterModule71311B75_Type()
)
txToMmStSx100MSingleTwisterModule71311B75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToMmStSx100MSingleTwisterModule71311B75.setStatus("current")
_TpToMmMtrj100MSingleTwisterModule71311E75_Type = ObjectIdentifier
_TpToMmMtrj100MSingleTwisterModule71311E75_Object = MibScalar
tpToMmMtrj100MSingleTwisterModule71311E75 = _TpToMmMtrj100MSingleTwisterModule71311E75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 21),
    _TpToMmMtrj100MSingleTwisterModule71311E75_Type()
)
tpToMmMtrj100MSingleTwisterModule71311E75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpToMmMtrj100MSingleTwisterModule71311E75.setStatus("current")
_TpToSmMtrj100MSingleTwisterModule71311F75_Type = ObjectIdentifier
_TpToSmMtrj100MSingleTwisterModule71311F75_Object = MibScalar
tpToSmMtrj100MSingleTwisterModule71311F75 = _TpToSmMtrj100MSingleTwisterModule71311F75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 22),
    _TpToSmMtrj100MSingleTwisterModule71311F75_Type()
)
tpToSmMtrj100MSingleTwisterModule71311F75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpToSmMtrj100MSingleTwisterModule71311F75.setStatus("current")
_TpToMmVf45100MSingleTwisterModule71311G75_Type = ObjectIdentifier
_TpToMmVf45100MSingleTwisterModule71311G75_Object = MibScalar
tpToMmVf45100MSingleTwisterModule71311G75 = _TpToMmVf45100MSingleTwisterModule71311G75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 23),
    _TpToMmVf45100MSingleTwisterModule71311G75_Type()
)
tpToMmVf45100MSingleTwisterModule71311G75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpToMmVf45100MSingleTwisterModule71311G75.setStatus("current")
_MmMtrjToScSm100MSingleTwisterModule7131E475_Type = ObjectIdentifier
_MmMtrjToScSm100MSingleTwisterModule7131E475_Object = MibScalar
mmMtrjToScSm100MSingleTwisterModule7131E475 = _MmMtrjToScSm100MSingleTwisterModule7131E475_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 24),
    _MmMtrjToScSm100MSingleTwisterModule7131E475_Type()
)
mmMtrjToScSm100MSingleTwisterModule7131E475.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmMtrjToScSm100MSingleTwisterModule7131E475.setStatus("current")
_MmMtrjToStSm100MSingleTwisterModule7131E675_Type = ObjectIdentifier
_MmMtrjToStSm100MSingleTwisterModule7131E675_Object = MibScalar
mmMtrjToStSm100MSingleTwisterModule7131E675 = _MmMtrjToStSm100MSingleTwisterModule7131E675_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 25),
    _MmMtrjToStSm100MSingleTwisterModule7131E675_Type()
)
mmMtrjToStSm100MSingleTwisterModule7131E675.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmMtrjToStSm100MSingleTwisterModule7131E675.setStatus("current")
_MmMtrjToMmMtrj100MSingleTwisterModule7831EE75_Type = ObjectIdentifier
_MmMtrjToMmMtrj100MSingleTwisterModule7831EE75_Object = MibScalar
mmMtrjToMmMtrj100MSingleTwisterModule7831EE75 = _MmMtrjToMmMtrj100MSingleTwisterModule7831EE75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 26),
    _MmMtrjToMmMtrj100MSingleTwisterModule7831EE75_Type()
)
mmMtrjToMmMtrj100MSingleTwisterModule7831EE75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmMtrjToMmMtrj100MSingleTwisterModule7831EE75.setStatus("current")
_MmMtrjToSmMtrj100MSingleTwisterModule7131EF75_Type = ObjectIdentifier
_MmMtrjToSmMtrj100MSingleTwisterModule7131EF75_Object = MibScalar
mmMtrjToSmMtrj100MSingleTwisterModule7131EF75 = _MmMtrjToSmMtrj100MSingleTwisterModule7131EF75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 27),
    _MmMtrjToSmMtrj100MSingleTwisterModule7131EF75_Type()
)
mmMtrjToSmMtrj100MSingleTwisterModule7131EF75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmMtrjToSmMtrj100MSingleTwisterModule7131EF75.setStatus("current")
_TxToScSm100MSingleTwisterModuleExLongHaul71311J75_Type = ObjectIdentifier
_TxToScSm100MSingleTwisterModuleExLongHaul71311J75_Object = MibScalar
txToScSm100MSingleTwisterModuleExLongHaul71311J75 = _TxToScSm100MSingleTwisterModuleExLongHaul71311J75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 2, 28),
    _TxToScSm100MSingleTwisterModuleExLongHaul71311J75_Type()
)
txToScSm100MSingleTwisterModuleExLongHaul71311J75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToScSm100MSingleTwisterModuleExLongHaul71311J75.setStatus("current")
_DualTwisterIdentifiers_ObjectIdentity = ObjectIdentity
dualTwisterIdentifiers = _DualTwisterIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 3)
)
_TpDualTwisterModule72111175_Type = ObjectIdentifier
_TpDualTwisterModule72111175_Object = MibScalar
tpDualTwisterModule72111175 = _TpDualTwisterModule72111175_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 3, 1),
    _TpDualTwisterModule72111175_Type()
)
tpDualTwisterModule72111175.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpDualTwisterModule72111175.setStatus("current")
_FlMmScDualTwisterModule72113375_Type = ObjectIdentifier
_FlMmScDualTwisterModule72113375_Object = MibScalar
flMmScDualTwisterModule72113375 = _FlMmScDualTwisterModule72113375_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 3, 2),
    _FlMmScDualTwisterModule72113375_Type()
)
flMmScDualTwisterModule72113375.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flMmScDualTwisterModule72113375.setStatus("current")
_FlMmStDualTwisterModule72115575_Type = ObjectIdentifier
_FlMmStDualTwisterModule72115575_Object = MibScalar
flMmStDualTwisterModule72115575 = _FlMmStDualTwisterModule72115575_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 3, 3),
    _FlMmStDualTwisterModule72115575_Type()
)
flMmStDualTwisterModule72115575.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flMmStDualTwisterModule72115575.setStatus("current")
_FlSmStDualTwisterModule72116675_Type = ObjectIdentifier
_FlSmStDualTwisterModule72116675_Object = MibScalar
flSmStDualTwisterModule72116675 = _FlSmStDualTwisterModule72116675_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 3, 4),
    _FlSmStDualTwisterModule72116675_Type()
)
flSmStDualTwisterModule72116675.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flSmStDualTwisterModule72116675.setStatus("current")
_RedundantTwisterIdentifiers_ObjectIdentity = ObjectIdentity
redundantTwisterIdentifiers = _RedundantTwisterIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 4)
)
_TxToDualTx100MRedundantTwisterModule77311175_Type = ObjectIdentifier
_TxToDualTx100MRedundantTwisterModule77311175_Object = MibScalar
txToDualTx100MRedundantTwisterModule77311175 = _TxToDualTx100MRedundantTwisterModule77311175_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 4, 1),
    _TxToDualTx100MRedundantTwisterModule77311175_Type()
)
txToDualTx100MRedundantTwisterModule77311175.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToDualTx100MRedundantTwisterModule77311175.setStatus("current")
_TxToDualFxMmSc100MRedundantTwisterModule77311375_Type = ObjectIdentifier
_TxToDualFxMmSc100MRedundantTwisterModule77311375_Object = MibScalar
txToDualFxMmSc100MRedundantTwisterModule77311375 = _TxToDualFxMmSc100MRedundantTwisterModule77311375_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 4, 2),
    _TxToDualFxMmSc100MRedundantTwisterModule77311375_Type()
)
txToDualFxMmSc100MRedundantTwisterModule77311375.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToDualFxMmSc100MRedundantTwisterModule77311375.setStatus("current")
_TxToDualfxSmSc100MRedundantTwisterModule77311475_Type = ObjectIdentifier
_TxToDualfxSmSc100MRedundantTwisterModule77311475_Object = MibScalar
txToDualfxSmSc100MRedundantTwisterModule77311475 = _TxToDualfxSmSc100MRedundantTwisterModule77311475_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 4, 3),
    _TxToDualfxSmSc100MRedundantTwisterModule77311475_Type()
)
txToDualfxSmSc100MRedundantTwisterModule77311475.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToDualfxSmSc100MRedundantTwisterModule77311475.setStatus("current")
_TxToDualFxMmSt100MRedundantTwisterModule77311575_Type = ObjectIdentifier
_TxToDualFxMmSt100MRedundantTwisterModule77311575_Object = MibScalar
txToDualFxMmSt100MRedundantTwisterModule77311575 = _TxToDualFxMmSt100MRedundantTwisterModule77311575_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 4, 4),
    _TxToDualFxMmSt100MRedundantTwisterModule77311575_Type()
)
txToDualFxMmSt100MRedundantTwisterModule77311575.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToDualFxMmSt100MRedundantTwisterModule77311575.setStatus("current")
_TxToDualFxSmSt100MRedundantTwisterModule77311675_Type = ObjectIdentifier
_TxToDualFxSmSt100MRedundantTwisterModule77311675_Object = MibScalar
txToDualFxSmSt100MRedundantTwisterModule77311675 = _TxToDualFxSmSt100MRedundantTwisterModule77311675_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 4, 5),
    _TxToDualFxSmSt100MRedundantTwisterModule77311675_Type()
)
txToDualFxSmSt100MRedundantTwisterModule77311675.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    txToDualFxSmSt100MRedundantTwisterModule77311675.setStatus("current")
_TpToDualTp10MRedundantTwisterModule77111175_Type = ObjectIdentifier
_TpToDualTp10MRedundantTwisterModule77111175_Object = MibScalar
tpToDualTp10MRedundantTwisterModule77111175 = _TpToDualTp10MRedundantTwisterModule77111175_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 4, 6),
    _TpToDualTp10MRedundantTwisterModule77111175_Type()
)
tpToDualTp10MRedundantTwisterModule77111175.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpToDualTp10MRedundantTwisterModule77111175.setStatus("current")
_DisplayModuleIdentifiers_ObjectIdentity = ObjectIdentity
displayModuleIdentifiers = _DisplayModuleIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 5)
)
_DisplayModule7500D_Type = ObjectIdentifier
_DisplayModule7500D_Object = MibScalar
displayModule7500D = _DisplayModule7500D_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 5, 1),
    _DisplayModule7500D_Type()
)
displayModule7500D.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    displayModule7500D.setStatus("current")
_RateAdapterIdentifiers_ObjectIdentity = ObjectIdentity
rateAdapterIdentifiers = _RateAdapterIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6)
)
_Tx10M100MToTx10M100MRateAdapterModule76211175_Type = ObjectIdentifier
_Tx10M100MToTx10M100MRateAdapterModule76211175_Object = MibScalar
tx10M100MToTx10M100MRateAdapterModule76211175 = _Tx10M100MToTx10M100MRateAdapterModule76211175_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6, 1),
    _Tx10M100MToTx10M100MRateAdapterModule76211175_Type()
)
tx10M100MToTx10M100MRateAdapterModule76211175.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tx10M100MToTx10M100MRateAdapterModule76211175.setStatus("current")
_Tx10M100MToFxMmSc10M100MRateAdapterModule76411375_Type = ObjectIdentifier
_Tx10M100MToFxMmSc10M100MRateAdapterModule76411375_Object = MibScalar
tx10M100MToFxMmSc10M100MRateAdapterModule76411375 = _Tx10M100MToFxMmSc10M100MRateAdapterModule76411375_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6, 2),
    _Tx10M100MToFxMmSc10M100MRateAdapterModule76411375_Type()
)
tx10M100MToFxMmSc10M100MRateAdapterModule76411375.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tx10M100MToFxMmSc10M100MRateAdapterModule76411375.setStatus("current")
_Tx10M100MToFxMmSt10M100MRateAdapterModule76411575_Type = ObjectIdentifier
_Tx10M100MToFxMmSt10M100MRateAdapterModule76411575_Object = MibScalar
tx10M100MToFxMmSt10M100MRateAdapterModule76411575 = _Tx10M100MToFxMmSt10M100MRateAdapterModule76411575_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6, 3),
    _Tx10M100MToFxMmSt10M100MRateAdapterModule76411575_Type()
)
tx10M100MToFxMmSt10M100MRateAdapterModule76411575.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tx10M100MToFxMmSt10M100MRateAdapterModule76411575.setStatus("current")
_Tx10M100MToFxMmMt10M100MRateAdapterModule76411E75_Type = ObjectIdentifier
_Tx10M100MToFxMmMt10M100MRateAdapterModule76411E75_Object = MibScalar
tx10M100MToFxMmMt10M100MRateAdapterModule76411E75 = _Tx10M100MToFxMmMt10M100MRateAdapterModule76411E75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6, 4),
    _Tx10M100MToFxMmMt10M100MRateAdapterModule76411E75_Type()
)
tx10M100MToFxMmMt10M100MRateAdapterModule76411E75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tx10M100MToFxMmMt10M100MRateAdapterModule76411E75.setStatus("current")
_Tx10M100MToFxMmVf10M100MRateAdapterModule76411G75_Type = ObjectIdentifier
_Tx10M100MToFxMmVf10M100MRateAdapterModule76411G75_Object = MibScalar
tx10M100MToFxMmVf10M100MRateAdapterModule76411G75 = _Tx10M100MToFxMmVf10M100MRateAdapterModule76411G75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6, 5),
    _Tx10M100MToFxMmVf10M100MRateAdapterModule76411G75_Type()
)
tx10M100MToFxMmVf10M100MRateAdapterModule76411G75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tx10M100MToFxMmVf10M100MRateAdapterModule76411G75.setStatus("current")
_Tx10M100MToFxScSm100MRateAdapterModule76411475_Type = ObjectIdentifier
_Tx10M100MToFxScSm100MRateAdapterModule76411475_Object = MibScalar
tx10M100MToFxScSm100MRateAdapterModule76411475 = _Tx10M100MToFxScSm100MRateAdapterModule76411475_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6, 6),
    _Tx10M100MToFxScSm100MRateAdapterModule76411475_Type()
)
tx10M100MToFxScSm100MRateAdapterModule76411475.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tx10M100MToFxScSm100MRateAdapterModule76411475.setStatus("current")
_Tx10M100MToFxScSMLongHaul100MRateAdapterModule76411775_Type = ObjectIdentifier
_Tx10M100MToFxScSMLongHaul100MRateAdapterModule76411775_Object = MibScalar
tx10M100MToFxScSMLongHaul100MRateAdapterModule76411775 = _Tx10M100MToFxScSMLongHaul100MRateAdapterModule76411775_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6, 7),
    _Tx10M100MToFxScSMLongHaul100MRateAdapterModule76411775_Type()
)
tx10M100MToFxScSMLongHaul100MRateAdapterModule76411775.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tx10M100MToFxScSMLongHaul100MRateAdapterModule76411775.setStatus("current")
_FlMmSt10MToTx10M100MRateAdapterModule76115175_Type = ObjectIdentifier
_FlMmSt10MToTx10M100MRateAdapterModule76115175_Object = MibScalar
flMmSt10MToTx10M100MRateAdapterModule76115175 = _FlMmSt10MToTx10M100MRateAdapterModule76115175_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6, 8),
    _FlMmSt10MToTx10M100MRateAdapterModule76115175_Type()
)
flMmSt10MToTx10M100MRateAdapterModule76115175.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flMmSt10MToTx10M100MRateAdapterModule76115175.setStatus("current")
_FlMmSt10MToFxMmSc100MRateAdapterModule76415375_Type = ObjectIdentifier
_FlMmSt10MToFxMmSc100MRateAdapterModule76415375_Object = MibScalar
flMmSt10MToFxMmSc100MRateAdapterModule76415375 = _FlMmSt10MToFxMmSc100MRateAdapterModule76415375_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6, 9),
    _FlMmSt10MToFxMmSc100MRateAdapterModule76415375_Type()
)
flMmSt10MToFxMmSc100MRateAdapterModule76415375.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flMmSt10MToFxMmSc100MRateAdapterModule76415375.setStatus("current")
_FlMmSt10MToFxMmSt100MRateAdapterModule76415575_Type = ObjectIdentifier
_FlMmSt10MToFxMmSt100MRateAdapterModule76415575_Object = MibScalar
flMmSt10MToFxMmSt100MRateAdapterModule76415575 = _FlMmSt10MToFxMmSt100MRateAdapterModule76415575_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 6, 10),
    _FlMmSt10MToFxMmSt100MRateAdapterModule76415575_Type()
)
flMmSt10MToFxMmSt100MRateAdapterModule76415575.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flMmSt10MToFxMmSt100MRateAdapterModule76415575.setStatus("current")
_FixedPortIdentifiers_ObjectIdentity = ObjectIdentity
fixedPortIdentifiers = _FixedPortIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 7)
)
_TwelvePort10MTelcoToFlMmStModule371295M_Type = ObjectIdentifier
_TwelvePort10MTelcoToFlMmStModule371295M_Object = MibScalar
twelvePort10MTelcoToFlMmStModule371295M = _TwelvePort10MTelcoToFlMmStModule371295M_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 7, 1),
    _TwelvePort10MTelcoToFlMmStModule371295M_Type()
)
twelvePort10MTelcoToFlMmStModule371295M.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twelvePort10MTelcoToFlMmStModule371295M.setStatus("current")
_TwelvePort10MTelcoToFlVf45Module37129GM_Type = ObjectIdentifier
_TwelvePort10MTelcoToFlVf45Module37129GM_Object = MibScalar
twelvePort10MTelcoToFlVf45Module37129GM = _TwelvePort10MTelcoToFlVf45Module37129GM_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 7, 2),
    _TwelvePort10MTelcoToFlVf45Module37129GM_Type()
)
twelvePort10MTelcoToFlVf45Module37129GM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    twelvePort10MTelcoToFlVf45Module37129GM.setStatus("current")
_SixPort10MTelcoToFlMmStModule370615M_Type = ObjectIdentifier
_SixPort10MTelcoToFlMmStModule370615M_Object = MibScalar
sixPort10MTelcoToFlMmStModule370615M = _SixPort10MTelcoToFlMmStModule370615M_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 7, 3),
    _SixPort10MTelcoToFlMmStModule370615M_Type()
)
sixPort10MTelcoToFlMmStModule370615M.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sixPort10MTelcoToFlMmStModule370615M.setStatus("current")
_SixPort10MTelcoToFlSmStModule370616M_Type = ObjectIdentifier
_SixPort10MTelcoToFlSmStModule370616M_Object = MibScalar
sixPort10MTelcoToFlSmStModule370616M = _SixPort10MTelcoToFlSmStModule370616M_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 7, 4),
    _SixPort10MTelcoToFlSmStModule370616M_Type()
)
sixPort10MTelcoToFlSmStModule370616M.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sixPort10MTelcoToFlSmStModule370616M.setStatus("current")
_SixPort10MTelcoToFlMmVf45Module37061GM_Type = ObjectIdentifier
_SixPort10MTelcoToFlMmVf45Module37061GM_Object = MibScalar
sixPort10MTelcoToFlMmVf45Module37061GM = _SixPort10MTelcoToFlMmVf45Module37061GM_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 7, 5),
    _SixPort10MTelcoToFlMmVf45Module37061GM_Type()
)
sixPort10MTelcoToFlMmVf45Module37061GM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sixPort10MTelcoToFlMmVf45Module37061GM.setStatus("current")
_ProtocolIndependentIdentifiers_ObjectIdentity = ObjectIdentity
protocolIndependentIdentifiers = _ProtocolIndependentIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 8)
)
_MmSCSXToScSmLX1000MGigTwisterModule7151AD75_Type = ObjectIdentifier
_MmSCSXToScSmLX1000MGigTwisterModule7151AD75_Object = MibScalar
mmSCSXToScSmLX1000MGigTwisterModule7151AD75 = _MmSCSXToScSmLX1000MGigTwisterModule7151AD75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 8, 1),
    _MmSCSXToScSmLX1000MGigTwisterModule7151AD75_Type()
)
mmSCSXToScSmLX1000MGigTwisterModule7151AD75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmSCSXToScSmLX1000MGigTwisterModule7151AD75.setStatus("current")
_MmSCSXToMtrjSmLX1000MGigTwisterModule7151AF75_Type = ObjectIdentifier
_MmSCSXToMtrjSmLX1000MGigTwisterModule7151AF75_Object = MibScalar
mmSCSXToMtrjSmLX1000MGigTwisterModule7151AF75 = _MmSCSXToMtrjSmLX1000MGigTwisterModule7151AF75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 8, 2),
    _MmSCSXToMtrjSmLX1000MGigTwisterModule7151AF75_Type()
)
mmSCSXToMtrjSmLX1000MGigTwisterModule7151AF75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmSCSXToMtrjSmLX1000MGigTwisterModule7151AF75.setStatus("current")
_MmMtrjSXToScSmLX1000MGigTwisterModule7151ED75_Type = ObjectIdentifier
_MmMtrjSXToScSmLX1000MGigTwisterModule7151ED75_Object = MibScalar
mmMtrjSXToScSmLX1000MGigTwisterModule7151ED75 = _MmMtrjSXToScSmLX1000MGigTwisterModule7151ED75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 8, 3),
    _MmMtrjSXToScSmLX1000MGigTwisterModule7151ED75_Type()
)
mmMtrjSXToScSmLX1000MGigTwisterModule7151ED75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmMtrjSXToScSmLX1000MGigTwisterModule7151ED75.setStatus("current")
_MmMtrjSXToMtrjSmLX1000MGigTwisterModule7151EF75_Type = ObjectIdentifier
_MmMtrjSXToMtrjSmLX1000MGigTwisterModule7151EF75_Object = MibScalar
mmMtrjSXToMtrjSmLX1000MGigTwisterModule7151EF75 = _MmMtrjSXToMtrjSmLX1000MGigTwisterModule7151EF75_Object(
    (1, 3, 6, 1, 4, 1, 2745, 1, 4, 4, 8, 4),
    _MmMtrjSXToMtrjSmLX1000MGigTwisterModule7151EF75_Type()
)
mmMtrjSXToMtrjSmLX1000MGigTwisterModule7151EF75.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmMtrjSXToMtrjSmLX1000MGigTwisterModule7151EF75.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LC-PRODUCT-IDENTIFIERS-MIB",
    **{"productIdentifiers": productIdentifiers,
       "chassisIdentifiers": chassisIdentifiers,
       "lc7500Chassis": lc7500Chassis,
       "twelveSlot2PS750012": twelveSlot2PS750012,
       "thirteenSlotTelco2PS750013": thirteenSlotTelco2PS750013,
       "seventeenSlot1PSFixed75001701": seventeenSlot1PSFixed75001701,
       "seventeenSlot2PSFixed75001702": seventeenSlot2PSFixed75001702,
       "seventeenSlot2PSHotSwapSwitch750017DX": seventeenSlot2PSHotSwapSwitch750017DX,
       "oem17500Chassis": oem17500Chassis,
       "oem1TwelveSlot2PS750012": oem1TwelveSlot2PS750012,
       "oem1SeventeenSlot1PSFixed75001701": oem1SeventeenSlot1PSFixed75001701,
       "oem1SeventeenSlot2PSFixed75001702": oem1SeventeenSlot2PSFixed75001702,
       "oem1SeventeenSlot2PSHotSwapSwitch750017DX": oem1SeventeenSlot2PSHotSwapSwitch750017DX,
       "powerSupplyIdentifiers": powerSupplyIdentifiers,
       "lc7500PowerSupply": lc7500PowerSupply,
       "acPowerSupply7500AC": acPowerSupply7500AC,
       "dcPowerSupply7500DC": dcPowerSupply7500DC,
       "moduleIdentifiers": moduleIdentifiers,
       "mgmntModuleIdentifiers": mgmntModuleIdentifiers,
       "singleEthernetMgmntModule7501M": singleEthernetMgmntModule7501M,
       "dualEthernetMgmntModule7502M": dualEthernetMgmntModule7502M,
       "redundantMgmntModule7501RM": redundantMgmntModule7501RM,
       "singleTwisterIdentifiers": singleTwisterIdentifiers,
       "tpToBnc10MSingleTwisterModule71111275": tpToBnc10MSingleTwisterModule71111275,
       "tpToFlMmSt10MSingleTwisterModule71111575": tpToFlMmSt10MSingleTwisterModule71111575,
       "tpToFlSmSt10MSingleTwisterModule71111675": tpToFlSmSt10MSingleTwisterModule71111675,
       "tpToSmaMm10MSingleTwisterModule71111875": tpToSmaMm10MSingleTwisterModule71111875,
       "txToFxMmSc100MSingleTwisterModule71311375": txToFxMmSc100MSingleTwisterModule71311375,
       "txToFxMmSt100MSingleTwisterModule71311575": txToFxMmSt100MSingleTwisterModule71311575,
       "txToFxSmSc100MSingleTwisterModule71311475": txToFxSmSc100MSingleTwisterModule71311475,
       "txToFxSmSc40Km100MSingleTwisterModule71311775": txToFxSmSc40Km100MSingleTwisterModule71311775,
       "fxMmScToFxSmSc100MSingleTwisterModule71313475": fxMmScToFxSmSc100MSingleTwisterModule71313475,
       "fxMmStToFxSmSc100MSingleTwisterModule71315475": fxMmStToFxSmSc100MSingleTwisterModule71315475,
       "txToFxSmSt100MSingleTwisterModule71311675": txToFxSmSt100MSingleTwisterModule71311675,
       "fxMmScToFxSmSt100MSingleTwisterModule71313675": fxMmScToFxSmSt100MSingleTwisterModule71313675,
       "fxMmStToFxSmSt100MSingleTwisterModule71315675": fxMmStToFxSmSt100MSingleTwisterModule71315675,
       "tpToTp10MSingleTwisterModule78111175": tpToTp10MSingleTwisterModule78111175,
       "tpToMmSc10MSingleTwisterModule71111375": tpToMmSc10MSingleTwisterModule71111375,
       "txToTx10MSingleTwisterModule78311175": txToTx10MSingleTwisterModule78311175,
       "mmScToMmSc100MSingleTwisterModule78313375": mmScToMmSc100MSingleTwisterModule78313375,
       "mmStToMmSt100MSingleTwisterModule78315575": mmStToMmSt100MSingleTwisterModule78315575,
       "txToMmScSx100MSingleTwisterModule71311A75": txToMmScSx100MSingleTwisterModule71311A75,
       "txToMmStSx100MSingleTwisterModule71311B75": txToMmStSx100MSingleTwisterModule71311B75,
       "tpToMmMtrj100MSingleTwisterModule71311E75": tpToMmMtrj100MSingleTwisterModule71311E75,
       "tpToSmMtrj100MSingleTwisterModule71311F75": tpToSmMtrj100MSingleTwisterModule71311F75,
       "tpToMmVf45100MSingleTwisterModule71311G75": tpToMmVf45100MSingleTwisterModule71311G75,
       "mmMtrjToScSm100MSingleTwisterModule7131E475": mmMtrjToScSm100MSingleTwisterModule7131E475,
       "mmMtrjToStSm100MSingleTwisterModule7131E675": mmMtrjToStSm100MSingleTwisterModule7131E675,
       "mmMtrjToMmMtrj100MSingleTwisterModule7831EE75": mmMtrjToMmMtrj100MSingleTwisterModule7831EE75,
       "mmMtrjToSmMtrj100MSingleTwisterModule7131EF75": mmMtrjToSmMtrj100MSingleTwisterModule7131EF75,
       "txToScSm100MSingleTwisterModuleExLongHaul71311J75": txToScSm100MSingleTwisterModuleExLongHaul71311J75,
       "dualTwisterIdentifiers": dualTwisterIdentifiers,
       "tpDualTwisterModule72111175": tpDualTwisterModule72111175,
       "flMmScDualTwisterModule72113375": flMmScDualTwisterModule72113375,
       "flMmStDualTwisterModule72115575": flMmStDualTwisterModule72115575,
       "flSmStDualTwisterModule72116675": flSmStDualTwisterModule72116675,
       "redundantTwisterIdentifiers": redundantTwisterIdentifiers,
       "txToDualTx100MRedundantTwisterModule77311175": txToDualTx100MRedundantTwisterModule77311175,
       "txToDualFxMmSc100MRedundantTwisterModule77311375": txToDualFxMmSc100MRedundantTwisterModule77311375,
       "txToDualfxSmSc100MRedundantTwisterModule77311475": txToDualfxSmSc100MRedundantTwisterModule77311475,
       "txToDualFxMmSt100MRedundantTwisterModule77311575": txToDualFxMmSt100MRedundantTwisterModule77311575,
       "txToDualFxSmSt100MRedundantTwisterModule77311675": txToDualFxSmSt100MRedundantTwisterModule77311675,
       "tpToDualTp10MRedundantTwisterModule77111175": tpToDualTp10MRedundantTwisterModule77111175,
       "displayModuleIdentifiers": displayModuleIdentifiers,
       "displayModule7500D": displayModule7500D,
       "rateAdapterIdentifiers": rateAdapterIdentifiers,
       "tx10M100MToTx10M100MRateAdapterModule76211175": tx10M100MToTx10M100MRateAdapterModule76211175,
       "tx10M100MToFxMmSc10M100MRateAdapterModule76411375": tx10M100MToFxMmSc10M100MRateAdapterModule76411375,
       "tx10M100MToFxMmSt10M100MRateAdapterModule76411575": tx10M100MToFxMmSt10M100MRateAdapterModule76411575,
       "tx10M100MToFxMmMt10M100MRateAdapterModule76411E75": tx10M100MToFxMmMt10M100MRateAdapterModule76411E75,
       "tx10M100MToFxMmVf10M100MRateAdapterModule76411G75": tx10M100MToFxMmVf10M100MRateAdapterModule76411G75,
       "tx10M100MToFxScSm100MRateAdapterModule76411475": tx10M100MToFxScSm100MRateAdapterModule76411475,
       "tx10M100MToFxScSMLongHaul100MRateAdapterModule76411775": tx10M100MToFxScSMLongHaul100MRateAdapterModule76411775,
       "flMmSt10MToTx10M100MRateAdapterModule76115175": flMmSt10MToTx10M100MRateAdapterModule76115175,
       "flMmSt10MToFxMmSc100MRateAdapterModule76415375": flMmSt10MToFxMmSc100MRateAdapterModule76415375,
       "flMmSt10MToFxMmSt100MRateAdapterModule76415575": flMmSt10MToFxMmSt100MRateAdapterModule76415575,
       "fixedPortIdentifiers": fixedPortIdentifiers,
       "twelvePort10MTelcoToFlMmStModule371295M": twelvePort10MTelcoToFlMmStModule371295M,
       "twelvePort10MTelcoToFlVf45Module37129GM": twelvePort10MTelcoToFlVf45Module37129GM,
       "sixPort10MTelcoToFlMmStModule370615M": sixPort10MTelcoToFlMmStModule370615M,
       "sixPort10MTelcoToFlSmStModule370616M": sixPort10MTelcoToFlSmStModule370616M,
       "sixPort10MTelcoToFlMmVf45Module37061GM": sixPort10MTelcoToFlMmVf45Module37061GM,
       "protocolIndependentIdentifiers": protocolIndependentIdentifiers,
       "mmSCSXToScSmLX1000MGigTwisterModule7151AD75": mmSCSXToScSmLX1000MGigTwisterModule7151AD75,
       "mmSCSXToMtrjSmLX1000MGigTwisterModule7151AF75": mmSCSXToMtrjSmLX1000MGigTwisterModule7151AF75,
       "mmMtrjSXToScSmLX1000MGigTwisterModule7151ED75": mmMtrjSXToScSmLX1000MGigTwisterModule7151ED75,
       "mmMtrjSXToMtrjSmLX1000MGigTwisterModule7151EF75": mmMtrjSXToMtrjSmLX1000MGigTwisterModule7151EF75}
)
