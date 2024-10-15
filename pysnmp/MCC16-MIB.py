# SNMP MIB module (MCC16-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MCC16-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:43 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class CpsConnector(Integer32):
    """Custom type CpsConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
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
              35)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 20),
          ("bncdual", 30),
          ("db9rsxxx", 31),
          ("lc", 19),
          ("mtrjmm", 18),
          ("mtrjsm", 25),
          ("rj-45", 10),
          ("rj11", 33),
          ("sc125km", 35),
          ("sc40km", 34),
          ("scmm", 13),
          ("scmm1300", 23),
          ("scsimplex", 29),
          ("scsm", 14),
          ("scsmelh", 16),
          ("scsmlh", 15),
          ("scsmlhlw", 17),
          ("scsmsh", 28),
          ("serial26", 26),
          ("stmm", 11),
          ("stmm1300", 24),
          ("stmmlh", 27),
          ("stsm", 12),
          ("stsmelh", 22),
          ("stsmlh", 21),
          ("termblock", 32))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Transition_ObjectIdentity = ObjectIdentity
transition = _Transition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868)
)
_ProductId_ObjectIdentity = ObjectIdentity
productId = _ProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1)
)
_ChassisProdsId_ObjectIdentity = ObjectIdentity
chassisProdsId = _ChassisProdsId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4)
)
_ChassisSlotTypes_ObjectIdentity = ObjectIdentity
chassisSlotTypes = _ChassisSlotTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1)
)
_ChSlMc20p_ObjectIdentity = ObjectIdentity
chSlMc20p = _ChSlMc20p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1)
)
_CeTbtFrl03Id_ObjectIdentity = ObjectIdentity
ceTbtFrl03Id = _CeTbtFrl03Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 1)
)
_CeCxTbt04Id_ObjectIdentity = ObjectIdentity
ceCxTbt04Id = _CeCxTbt04Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 2)
)
_CeCxFrl04Id_ObjectIdentity = ObjectIdentity
ceCxFrl04Id = _CeCxFrl04Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 3)
)
_CfSmMm02Id_ObjectIdentity = ObjectIdentity
cfSmMm02Id = _CfSmMm02Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 4)
)
_CfSmMm05Id_ObjectIdentity = ObjectIdentity
cfSmMm05Id = _CfSmMm05Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 5)
)
_CaCf02Id_ObjectIdentity = ObjectIdentity
caCf02Id = _CaCf02Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 6)
)
_CfSmMm06Id_ObjectIdentity = ObjectIdentity
cfSmMm06Id = _CfSmMm06Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 7)
)
_Ct1e1Cf01Id_ObjectIdentity = ObjectIdentity
ct1e1Cf01Id = _Ct1e1Cf01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 8)
)
_CeRTxFx01Id_ObjectIdentity = ObjectIdentity
ceRTxFx01Id = _CeRTxFx01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 9)
)
_Ce100BtxFx04Id_ObjectIdentity = ObjectIdentity
ce100BtxFx04Id = _Ce100BtxFx04Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 10)
)
_CpsCf01Id_ObjectIdentity = ObjectIdentity
cpsCf01Id = _CpsCf01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 12)
)
_CbCf01Id_ObjectIdentity = ObjectIdentity
cbCf01Id = _CbCf01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 13)
)
_CarCf01Id_ObjectIdentity = ObjectIdentity
carCf01Id = _CarCf01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 14)
)
_CarCf02Id_ObjectIdentity = ObjectIdentity
carCf02Id = _CarCf02Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 15)
)
_CePswFx03Id_ObjectIdentity = ObjectIdentity
cePswFx03Id = _CePswFx03Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 16)
)
_CePswSx01Id_ObjectIdentity = ObjectIdentity
cePswSx01Id = _CePswSx01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 17)
)
_CRs232Cf01Id_ObjectIdentity = ObjectIdentity
cRs232Cf01Id = _CRs232Cf01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 18)
)
_CfSmMm04Id_ObjectIdentity = ObjectIdentity
cfSmMm04Id = _CfSmMm04Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 24)
)
_Ce100BtxSx01Id_ObjectIdentity = ObjectIdentity
ce100BtxSx01Id = _Ce100BtxSx01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 26)
)
_Ce100BtxFx04MtId_ObjectIdentity = ObjectIdentity
ce100BtxFx04MtId = _Ce100BtxFx04MtId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 27)
)
_CfdCd01Id_ObjectIdentity = ObjectIdentity
cfdCd01Id = _CfdCd01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 28)
)
_CtrCf01Id_ObjectIdentity = ObjectIdentity
ctrCf01Id = _CtrCf01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 29)
)
_Ce100BtxFrl03Id_ObjectIdentity = ObjectIdentity
ce100BtxFrl03Id = _Ce100BtxFrl03Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 30)
)
_Mc20pEmptyId_ObjectIdentity = ObjectIdentity
mc20pEmptyId = _Mc20pEmptyId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 31)
)
_Mc20pErrorId_ObjectIdentity = ObjectIdentity
mc20pErrorId = _Mc20pErrorId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 32)
)
_Mc20pDblWideId_ObjectIdentity = ObjectIdentity
mc20pDblWideId = _Mc20pDblWideId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 33)
)
_ChstrCf01Id_ObjectIdentity = ObjectIdentity
chstrCf01Id = _ChstrCf01Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 34)
)
_CeTxSx02Id_ObjectIdentity = ObjectIdentity
ceTxSx02Id = _CeTxSx02Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 35)
)
_CeTbtFrl04Id_ObjectIdentity = ObjectIdentity
ceTbtFrl04Id = _CeTbtFrl04Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 1, 36)
)
_ChSlcps_ObjectIdentity = ObjectIdentity
chSlcps = _ChSlcps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2)
)
_CpsmM100Id_ObjectIdentity = ObjectIdentity
cpsmM100Id = _CpsmM100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1)
)
_CpsmM200Id_ObjectIdentity = ObjectIdentity
cpsmM200Id = _CpsmM200Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 2)
)
_Cettf100Id_ObjectIdentity = ObjectIdentity
cettf100Id = _Cettf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 3)
)
_Cfetf100Id_ObjectIdentity = ObjectIdentity
cfetf100Id = _Cfetf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 4)
)
_Cfmff100Id_ObjectIdentity = ObjectIdentity
cfmff100Id = _Cfmff100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 5)
)
_Cpsmp100Id_ObjectIdentity = ObjectIdentity
cpsmp100Id = _Cpsmp100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 6)
)
_Csetf100Id_ObjectIdentity = ObjectIdentity
csetf100Id = _Csetf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 7)
)
_Cgetf100Id_ObjectIdentity = ObjectIdentity
cgetf100Id = _Cgetf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 8)
)
_Csdtf100Id_ObjectIdentity = ObjectIdentity
csdtf100Id = _Csdtf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 9)
)
_Cpsmp110Id_ObjectIdentity = ObjectIdentity
cpsmp110Id = _Cpsmp110Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 10)
)
_Cbftf100Id_ObjectIdentity = ObjectIdentity
cbftf100Id = _Cbftf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 11)
)
_Cetct100Id_ObjectIdentity = ObjectIdentity
cetct100Id = _Cetct100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 12)
)
_Ccscf100Id_ObjectIdentity = ObjectIdentity
ccscf100Id = _Ccscf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 13)
)
_Cfetf105Id_ObjectIdentity = ObjectIdentity
cfetf105Id = _Cfetf105Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 14)
)
_Smacf100PId_ObjectIdentity = ObjectIdentity
smacf100PId = _Smacf100PId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 15)
)
_Cpsld100Id_ObjectIdentity = ObjectIdentity
cpsld100Id = _Cpsld100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 16)
)
_Cdftf100Id_ObjectIdentity = ObjectIdentity
cdftf100Id = _Cdftf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 17)
)
_Cpsvt100Id_ObjectIdentity = ObjectIdentity
cpsvt100Id = _Cpsvt100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 18)
)
_Cemtf100Id_ObjectIdentity = ObjectIdentity
cemtf100Id = _Cemtf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 19)
)
_Captf100Id_ObjectIdentity = ObjectIdentity
captf100Id = _Captf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 20)
)
_Cfetf205Id_ObjectIdentity = ObjectIdentity
cfetf205Id = _Cfetf205Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 21)
)
_Cbftf150Id_ObjectIdentity = ObjectIdentity
cbftf150Id = _Cbftf150Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 22)
)
_Cgfeb100Id_ObjectIdentity = ObjectIdentity
cgfeb100Id = _Cgfeb100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 23)
)
_Crmfe100Id_ObjectIdentity = ObjectIdentity
crmfe100Id = _Crmfe100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 24)
)
_Crs2f100Id_ObjectIdentity = ObjectIdentity
crs2f100Id = _Crs2f100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 25)
)
_Crs4f100Id_ObjectIdentity = ObjectIdentity
crs4f100Id = _Crs4f100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 26)
)
_Cmefg100Id_ObjectIdentity = ObjectIdentity
cmefg100Id = _Cmefg100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 27)
)
_CpsEmptyId_ObjectIdentity = ObjectIdentity
cpsEmptyId = _CpsEmptyId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1001)
)
_CpsDblWideId_ObjectIdentity = ObjectIdentity
cpsDblWideId = _CpsDblWideId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1002)
)
_CpsUnknownDeviceId_ObjectIdentity = ObjectIdentity
cpsUnknownDeviceId = _CpsUnknownDeviceId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1003)
)
_ChassisMcc16Id_ObjectIdentity = ObjectIdentity
chassisMcc16Id = _ChassisMcc16Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 2)
)
_ChassisCpsmc1800Id_ObjectIdentity = ObjectIdentity
chassisCpsmc1800Id = _ChassisCpsmc1800Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 3)
)
_ChassisCpsmc1850Id_ObjectIdentity = ObjectIdentity
chassisCpsmc1850Id = _ChassisCpsmc1850Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 4)
)
_ChassisCpsmc0800Id_ObjectIdentity = ObjectIdentity
chassisCpsmc0800Id = _ChassisCpsmc0800Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 5)
)
_ChassisCpsmc1300Id_ObjectIdentity = ObjectIdentity
chassisCpsmc1300Id = _ChassisCpsmc1300Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 6)
)
_ChassisCpsmc0200Id_ObjectIdentity = ObjectIdentity
chassisCpsmc0200Id = _ChassisCpsmc0200Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 7)
)
_ChassisSmacf100LCId_ObjectIdentity = ObjectIdentity
chassisSmacf100LCId = _ChassisSmacf100LCId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 8)
)
_ChassisCpsmc1900Id_ObjectIdentity = ObjectIdentity
chassisCpsmc1900Id = _ChassisCpsmc1900Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 9)
)
_ChassisSmacf100Id_ObjectIdentity = ObjectIdentity
chassisSmacf100Id = _ChassisSmacf100Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 10)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4)
)
_Card_ObjectIdentity = ObjectIdentity
card = _Card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1)
)
_SlotMc20p_ObjectIdentity = ObjectIdentity
slotMc20p = _SlotMc20p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1)
)
_CeTbtFrl03Table_Object = MibTable
ceTbtFrl03Table = _CeTbtFrl03Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ceTbtFrl03Table.setStatus("mandatory")
_CeTbtFrl03Entry_Object = MibTableRow
ceTbtFrl03Entry = _CeTbtFrl03Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 1, 1)
)
ceTbtFrl03Entry.setIndexNames(
    (0, "MCC16-MIB", "ceTbtFrl03Index"),
)
if mibBuilder.loadTexts:
    ceTbtFrl03Entry.setStatus("mandatory")
_CeTbtFrl03Index_Type = Integer32
_CeTbtFrl03Index_Object = MibTableColumn
ceTbtFrl03Index = _CeTbtFrl03Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 1, 1, 1),
    _CeTbtFrl03Index_Type()
)
ceTbtFrl03Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl03Index.setStatus("mandatory")


class _CeTbtFrl03FiberRecv_Type(Integer32):
    """Custom type ceTbtFrl03FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTbtFrl03FiberRecv_Type.__name__ = "Integer32"
_CeTbtFrl03FiberRecv_Object = MibTableColumn
ceTbtFrl03FiberRecv = _CeTbtFrl03FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 1, 1, 2),
    _CeTbtFrl03FiberRecv_Type()
)
ceTbtFrl03FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl03FiberRecv.setStatus("mandatory")


class _CeTbtFrl03FiberLink_Type(Integer32):
    """Custom type ceTbtFrl03FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTbtFrl03FiberLink_Type.__name__ = "Integer32"
_CeTbtFrl03FiberLink_Object = MibTableColumn
ceTbtFrl03FiberLink = _CeTbtFrl03FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 1, 1, 3),
    _CeTbtFrl03FiberLink_Type()
)
ceTbtFrl03FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl03FiberLink.setStatus("mandatory")


class _CeTbtFrl03TPRecv_Type(Integer32):
    """Custom type ceTbtFrl03TPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTbtFrl03TPRecv_Type.__name__ = "Integer32"
_CeTbtFrl03TPRecv_Object = MibTableColumn
ceTbtFrl03TPRecv = _CeTbtFrl03TPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 1, 1, 4),
    _CeTbtFrl03TPRecv_Type()
)
ceTbtFrl03TPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl03TPRecv.setStatus("mandatory")


class _CeTbtFrl03TPLink_Type(Integer32):
    """Custom type ceTbtFrl03TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTbtFrl03TPLink_Type.__name__ = "Integer32"
_CeTbtFrl03TPLink_Object = MibTableColumn
ceTbtFrl03TPLink = _CeTbtFrl03TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 1, 1, 5),
    _CeTbtFrl03TPLink_Type()
)
ceTbtFrl03TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl03TPLink.setStatus("mandatory")


class _CeTbtFrl03Power_Type(Integer32):
    """Custom type ceTbtFrl03Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTbtFrl03Power_Type.__name__ = "Integer32"
_CeTbtFrl03Power_Object = MibTableColumn
ceTbtFrl03Power = _CeTbtFrl03Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 1, 1, 6),
    _CeTbtFrl03Power_Type()
)
ceTbtFrl03Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl03Power.setStatus("mandatory")
_CeCxTbt04Table_Object = MibTable
ceCxTbt04Table = _CeCxTbt04Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ceCxTbt04Table.setStatus("mandatory")
_CeCxTbt04Entry_Object = MibTableRow
ceCxTbt04Entry = _CeCxTbt04Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 2, 1)
)
ceCxTbt04Entry.setIndexNames(
    (0, "MCC16-MIB", "ceCxTbt04Index"),
)
if mibBuilder.loadTexts:
    ceCxTbt04Entry.setStatus("mandatory")
_CeCxTbt04Index_Type = Integer32
_CeCxTbt04Index_Object = MibTableColumn
ceCxTbt04Index = _CeCxTbt04Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 2, 1, 1),
    _CeCxTbt04Index_Type()
)
ceCxTbt04Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxTbt04Index.setStatus("mandatory")


class _CeCxTbt04Jabber_Type(Integer32):
    """Custom type ceCxTbt04Jabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeCxTbt04Jabber_Type.__name__ = "Integer32"
_CeCxTbt04Jabber_Object = MibTableColumn
ceCxTbt04Jabber = _CeCxTbt04Jabber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 2, 1, 2),
    _CeCxTbt04Jabber_Type()
)
ceCxTbt04Jabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxTbt04Jabber.setStatus("mandatory")


class _CeCxTbt04CoaxRecv_Type(Integer32):
    """Custom type ceCxTbt04CoaxRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeCxTbt04CoaxRecv_Type.__name__ = "Integer32"
_CeCxTbt04CoaxRecv_Object = MibTableColumn
ceCxTbt04CoaxRecv = _CeCxTbt04CoaxRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 2, 1, 3),
    _CeCxTbt04CoaxRecv_Type()
)
ceCxTbt04CoaxRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxTbt04CoaxRecv.setStatus("mandatory")


class _CeCxTbt04TPRecv_Type(Integer32):
    """Custom type ceCxTbt04TPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeCxTbt04TPRecv_Type.__name__ = "Integer32"
_CeCxTbt04TPRecv_Object = MibTableColumn
ceCxTbt04TPRecv = _CeCxTbt04TPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 2, 1, 4),
    _CeCxTbt04TPRecv_Type()
)
ceCxTbt04TPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxTbt04TPRecv.setStatus("mandatory")


class _CeCxTbt04TPLink_Type(Integer32):
    """Custom type ceCxTbt04TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeCxTbt04TPLink_Type.__name__ = "Integer32"
_CeCxTbt04TPLink_Object = MibTableColumn
ceCxTbt04TPLink = _CeCxTbt04TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 2, 1, 5),
    _CeCxTbt04TPLink_Type()
)
ceCxTbt04TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxTbt04TPLink.setStatus("mandatory")


class _CeCxTbt04Power_Type(Integer32):
    """Custom type ceCxTbt04Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeCxTbt04Power_Type.__name__ = "Integer32"
_CeCxTbt04Power_Object = MibTableColumn
ceCxTbt04Power = _CeCxTbt04Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 2, 1, 6),
    _CeCxTbt04Power_Type()
)
ceCxTbt04Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxTbt04Power.setStatus("mandatory")
_CeCxFrl04Table_Object = MibTable
ceCxFrl04Table = _CeCxFrl04Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ceCxFrl04Table.setStatus("mandatory")
_CeCxFrl04Entry_Object = MibTableRow
ceCxFrl04Entry = _CeCxFrl04Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 3, 1)
)
ceCxFrl04Entry.setIndexNames(
    (0, "MCC16-MIB", "ceCxFrl04Index"),
)
if mibBuilder.loadTexts:
    ceCxFrl04Entry.setStatus("mandatory")
_CeCxFrl04Index_Type = Integer32
_CeCxFrl04Index_Object = MibTableColumn
ceCxFrl04Index = _CeCxFrl04Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 3, 1, 1),
    _CeCxFrl04Index_Type()
)
ceCxFrl04Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxFrl04Index.setStatus("mandatory")


class _CeCxFrl04Jabber_Type(Integer32):
    """Custom type ceCxFrl04Jabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeCxFrl04Jabber_Type.__name__ = "Integer32"
_CeCxFrl04Jabber_Object = MibTableColumn
ceCxFrl04Jabber = _CeCxFrl04Jabber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 3, 1, 2),
    _CeCxFrl04Jabber_Type()
)
ceCxFrl04Jabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxFrl04Jabber.setStatus("mandatory")


class _CeCxFrl04CoaxRecv_Type(Integer32):
    """Custom type ceCxFrl04CoaxRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeCxFrl04CoaxRecv_Type.__name__ = "Integer32"
_CeCxFrl04CoaxRecv_Object = MibTableColumn
ceCxFrl04CoaxRecv = _CeCxFrl04CoaxRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 3, 1, 3),
    _CeCxFrl04CoaxRecv_Type()
)
ceCxFrl04CoaxRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxFrl04CoaxRecv.setStatus("mandatory")


class _CeCxFrl04FLRecv_Type(Integer32):
    """Custom type ceCxFrl04FLRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeCxFrl04FLRecv_Type.__name__ = "Integer32"
_CeCxFrl04FLRecv_Object = MibTableColumn
ceCxFrl04FLRecv = _CeCxFrl04FLRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 3, 1, 4),
    _CeCxFrl04FLRecv_Type()
)
ceCxFrl04FLRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxFrl04FLRecv.setStatus("mandatory")


class _CeCxFrl04FLLink_Type(Integer32):
    """Custom type ceCxFrl04FLLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeCxFrl04FLLink_Type.__name__ = "Integer32"
_CeCxFrl04FLLink_Object = MibTableColumn
ceCxFrl04FLLink = _CeCxFrl04FLLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 3, 1, 5),
    _CeCxFrl04FLLink_Type()
)
ceCxFrl04FLLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxFrl04FLLink.setStatus("mandatory")


class _CeCxFrl04Power_Type(Integer32):
    """Custom type ceCxFrl04Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeCxFrl04Power_Type.__name__ = "Integer32"
_CeCxFrl04Power_Object = MibTableColumn
ceCxFrl04Power = _CeCxFrl04Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 3, 1, 6),
    _CeCxFrl04Power_Type()
)
ceCxFrl04Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceCxFrl04Power.setStatus("mandatory")
_CfSmMm02Table_Object = MibTable
cfSmMm02Table = _CfSmMm02Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cfSmMm02Table.setStatus("mandatory")
_CfSmMm02Entry_Object = MibTableRow
cfSmMm02Entry = _CfSmMm02Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 4, 1)
)
cfSmMm02Entry.setIndexNames(
    (0, "MCC16-MIB", "cfSmMm02Index"),
)
if mibBuilder.loadTexts:
    cfSmMm02Entry.setStatus("mandatory")
_CfSmMm02Index_Type = Integer32
_CfSmMm02Index_Object = MibTableColumn
cfSmMm02Index = _CfSmMm02Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 4, 1, 1),
    _CfSmMm02Index_Type()
)
cfSmMm02Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm02Index.setStatus("mandatory")


class _CfSmMm02MMSignalDetect_Type(Integer32):
    """Custom type cfSmMm02MMSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm02MMSignalDetect_Type.__name__ = "Integer32"
_CfSmMm02MMSignalDetect_Object = MibTableColumn
cfSmMm02MMSignalDetect = _CfSmMm02MMSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 4, 1, 2),
    _CfSmMm02MMSignalDetect_Type()
)
cfSmMm02MMSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm02MMSignalDetect.setStatus("mandatory")


class _CfSmMm02SMSignalDetect_Type(Integer32):
    """Custom type cfSmMm02SMSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm02SMSignalDetect_Type.__name__ = "Integer32"
_CfSmMm02SMSignalDetect_Object = MibTableColumn
cfSmMm02SMSignalDetect = _CfSmMm02SMSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 4, 1, 3),
    _CfSmMm02SMSignalDetect_Type()
)
cfSmMm02SMSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm02SMSignalDetect.setStatus("mandatory")


class _CfSmMm02Power_Type(Integer32):
    """Custom type cfSmMm02Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm02Power_Type.__name__ = "Integer32"
_CfSmMm02Power_Object = MibTableColumn
cfSmMm02Power = _CfSmMm02Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 4, 1, 4),
    _CfSmMm02Power_Type()
)
cfSmMm02Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm02Power.setStatus("mandatory")
_CfSmMm05Table_Object = MibTable
cfSmMm05Table = _CfSmMm05Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cfSmMm05Table.setStatus("mandatory")
_CfSmMm05Entry_Object = MibTableRow
cfSmMm05Entry = _CfSmMm05Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 5, 1)
)
cfSmMm05Entry.setIndexNames(
    (0, "MCC16-MIB", "cfSmMm05Index"),
)
if mibBuilder.loadTexts:
    cfSmMm05Entry.setStatus("mandatory")
_CfSmMm05Index_Type = Integer32
_CfSmMm05Index_Object = MibTableColumn
cfSmMm05Index = _CfSmMm05Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 5, 1, 1),
    _CfSmMm05Index_Type()
)
cfSmMm05Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm05Index.setStatus("mandatory")


class _CfSmMm05SMSignalDetect_Type(Integer32):
    """Custom type cfSmMm05SMSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm05SMSignalDetect_Type.__name__ = "Integer32"
_CfSmMm05SMSignalDetect_Object = MibTableColumn
cfSmMm05SMSignalDetect = _CfSmMm05SMSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 5, 1, 2),
    _CfSmMm05SMSignalDetect_Type()
)
cfSmMm05SMSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm05SMSignalDetect.setStatus("mandatory")


class _CfSmMm05MMSignalDetect_Type(Integer32):
    """Custom type cfSmMm05MMSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm05MMSignalDetect_Type.__name__ = "Integer32"
_CfSmMm05MMSignalDetect_Object = MibTableColumn
cfSmMm05MMSignalDetect = _CfSmMm05MMSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 5, 1, 3),
    _CfSmMm05MMSignalDetect_Type()
)
cfSmMm05MMSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm05MMSignalDetect.setStatus("mandatory")


class _CfSmMm05Power_Type(Integer32):
    """Custom type cfSmMm05Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm05Power_Type.__name__ = "Integer32"
_CfSmMm05Power_Object = MibTableColumn
cfSmMm05Power = _CfSmMm05Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 5, 1, 4),
    _CfSmMm05Power_Type()
)
cfSmMm05Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm05Power.setStatus("mandatory")
_CaCf02Table_Object = MibTable
caCf02Table = _CaCf02Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    caCf02Table.setStatus("mandatory")
_CaCf02Entry_Object = MibTableRow
caCf02Entry = _CaCf02Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 6, 1)
)
caCf02Entry.setIndexNames(
    (0, "MCC16-MIB", "caCf02Index"),
)
if mibBuilder.loadTexts:
    caCf02Entry.setStatus("mandatory")
_CaCf02Index_Type = Integer32
_CaCf02Index_Object = MibTableColumn
caCf02Index = _CaCf02Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 6, 1, 1),
    _CaCf02Index_Type()
)
caCf02Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caCf02Index.setStatus("mandatory")


class _CaCf02CopperSignalDetect_Type(Integer32):
    """Custom type caCf02CopperSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CaCf02CopperSignalDetect_Type.__name__ = "Integer32"
_CaCf02CopperSignalDetect_Object = MibTableColumn
caCf02CopperSignalDetect = _CaCf02CopperSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 6, 1, 2),
    _CaCf02CopperSignalDetect_Type()
)
caCf02CopperSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caCf02CopperSignalDetect.setStatus("mandatory")


class _CaCf02FiberSignalDetect_Type(Integer32):
    """Custom type caCf02FiberSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CaCf02FiberSignalDetect_Type.__name__ = "Integer32"
_CaCf02FiberSignalDetect_Object = MibTableColumn
caCf02FiberSignalDetect = _CaCf02FiberSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 6, 1, 3),
    _CaCf02FiberSignalDetect_Type()
)
caCf02FiberSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caCf02FiberSignalDetect.setStatus("mandatory")


class _CaCf02Power_Type(Integer32):
    """Custom type caCf02Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CaCf02Power_Type.__name__ = "Integer32"
_CaCf02Power_Object = MibTableColumn
caCf02Power = _CaCf02Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 6, 1, 4),
    _CaCf02Power_Type()
)
caCf02Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caCf02Power.setStatus("mandatory")
_CfSmMm06Table_Object = MibTable
cfSmMm06Table = _CfSmMm06Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cfSmMm06Table.setStatus("mandatory")
_CfSmMm06Entry_Object = MibTableRow
cfSmMm06Entry = _CfSmMm06Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 7, 1)
)
cfSmMm06Entry.setIndexNames(
    (0, "MCC16-MIB", "cfSmMm06Index"),
)
if mibBuilder.loadTexts:
    cfSmMm06Entry.setStatus("mandatory")
_CfSmMm06Index_Type = Integer32
_CfSmMm06Index_Object = MibTableColumn
cfSmMm06Index = _CfSmMm06Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 7, 1, 1),
    _CfSmMm06Index_Type()
)
cfSmMm06Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm06Index.setStatus("mandatory")


class _CfSmMm06MMSignalDetect_Type(Integer32):
    """Custom type cfSmMm06MMSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm06MMSignalDetect_Type.__name__ = "Integer32"
_CfSmMm06MMSignalDetect_Object = MibTableColumn
cfSmMm06MMSignalDetect = _CfSmMm06MMSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 7, 1, 2),
    _CfSmMm06MMSignalDetect_Type()
)
cfSmMm06MMSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm06MMSignalDetect.setStatus("mandatory")


class _CfSmMm06SMSignalDetect_Type(Integer32):
    """Custom type cfSmMm06SMSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm06SMSignalDetect_Type.__name__ = "Integer32"
_CfSmMm06SMSignalDetect_Object = MibTableColumn
cfSmMm06SMSignalDetect = _CfSmMm06SMSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 7, 1, 3),
    _CfSmMm06SMSignalDetect_Type()
)
cfSmMm06SMSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm06SMSignalDetect.setStatus("mandatory")


class _CfSmMm06Power_Type(Integer32):
    """Custom type cfSmMm06Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm06Power_Type.__name__ = "Integer32"
_CfSmMm06Power_Object = MibTableColumn
cfSmMm06Power = _CfSmMm06Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 7, 1, 4),
    _CfSmMm06Power_Type()
)
cfSmMm06Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm06Power.setStatus("mandatory")
_Ct1e1Cf01Table_Object = MibTable
ct1e1Cf01Table = _Ct1e1Cf01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ct1e1Cf01Table.setStatus("mandatory")
_Ct1e1Cf01Entry_Object = MibTableRow
ct1e1Cf01Entry = _Ct1e1Cf01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 8, 1)
)
ct1e1Cf01Entry.setIndexNames(
    (0, "MCC16-MIB", "ct1e1Cf01Index"),
)
if mibBuilder.loadTexts:
    ct1e1Cf01Entry.setStatus("mandatory")
_Ct1e1Cf01Index_Type = Integer32
_Ct1e1Cf01Index_Object = MibTableColumn
ct1e1Cf01Index = _Ct1e1Cf01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 8, 1, 1),
    _Ct1e1Cf01Index_Type()
)
ct1e1Cf01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ct1e1Cf01Index.setStatus("mandatory")


class _Ct1e1Cf01CopperSignalDetect_Type(Integer32):
    """Custom type ct1e1Cf01CopperSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ct1e1Cf01CopperSignalDetect_Type.__name__ = "Integer32"
_Ct1e1Cf01CopperSignalDetect_Object = MibTableColumn
ct1e1Cf01CopperSignalDetect = _Ct1e1Cf01CopperSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 8, 1, 2),
    _Ct1e1Cf01CopperSignalDetect_Type()
)
ct1e1Cf01CopperSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ct1e1Cf01CopperSignalDetect.setStatus("mandatory")


class _Ct1e1Cf01FiberSignalDetect_Type(Integer32):
    """Custom type ct1e1Cf01FiberSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ct1e1Cf01FiberSignalDetect_Type.__name__ = "Integer32"
_Ct1e1Cf01FiberSignalDetect_Object = MibTableColumn
ct1e1Cf01FiberSignalDetect = _Ct1e1Cf01FiberSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 8, 1, 3),
    _Ct1e1Cf01FiberSignalDetect_Type()
)
ct1e1Cf01FiberSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ct1e1Cf01FiberSignalDetect.setStatus("mandatory")


class _Ct1e1Cf01CoaxActive_Type(Integer32):
    """Custom type ct1e1Cf01CoaxActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ct1e1Cf01CoaxActive_Type.__name__ = "Integer32"
_Ct1e1Cf01CoaxActive_Object = MibTableColumn
ct1e1Cf01CoaxActive = _Ct1e1Cf01CoaxActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 8, 1, 4),
    _Ct1e1Cf01CoaxActive_Type()
)
ct1e1Cf01CoaxActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ct1e1Cf01CoaxActive.setStatus("mandatory")
_CeRTxFx01Table_Object = MibTable
ceRTxFx01Table = _CeRTxFx01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    ceRTxFx01Table.setStatus("mandatory")
_CeRTxFx01Entry_Object = MibTableRow
ceRTxFx01Entry = _CeRTxFx01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 9, 1)
)
ceRTxFx01Entry.setIndexNames(
    (0, "MCC16-MIB", "ceRTxFx01Index"),
)
if mibBuilder.loadTexts:
    ceRTxFx01Entry.setStatus("mandatory")
_CeRTxFx01Index_Type = Integer32
_CeRTxFx01Index_Object = MibTableColumn
ceRTxFx01Index = _CeRTxFx01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 9, 1, 1),
    _CeRTxFx01Index_Type()
)
ceRTxFx01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRTxFx01Index.setStatus("mandatory")


class _CeRTxFx01TPPrimary_Type(Integer32):
    """Custom type ceRTxFx01TPPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeRTxFx01TPPrimary_Type.__name__ = "Integer32"
_CeRTxFx01TPPrimary_Object = MibTableColumn
ceRTxFx01TPPrimary = _CeRTxFx01TPPrimary_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 9, 1, 2),
    _CeRTxFx01TPPrimary_Type()
)
ceRTxFx01TPPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRTxFx01TPPrimary.setStatus("mandatory")


class _CeRTxFx01FiberPrimary_Type(Integer32):
    """Custom type ceRTxFx01FiberPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeRTxFx01FiberPrimary_Type.__name__ = "Integer32"
_CeRTxFx01FiberPrimary_Object = MibTableColumn
ceRTxFx01FiberPrimary = _CeRTxFx01FiberPrimary_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 9, 1, 3),
    _CeRTxFx01FiberPrimary_Type()
)
ceRTxFx01FiberPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRTxFx01FiberPrimary.setStatus("mandatory")


class _CeRTxFx01TPSignalDetect_Type(Integer32):
    """Custom type ceRTxFx01TPSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeRTxFx01TPSignalDetect_Type.__name__ = "Integer32"
_CeRTxFx01TPSignalDetect_Object = MibTableColumn
ceRTxFx01TPSignalDetect = _CeRTxFx01TPSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 9, 1, 4),
    _CeRTxFx01TPSignalDetect_Type()
)
ceRTxFx01TPSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRTxFx01TPSignalDetect.setStatus("mandatory")


class _CeRTxFx01FiberSignalDetect_Type(Integer32):
    """Custom type ceRTxFx01FiberSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeRTxFx01FiberSignalDetect_Type.__name__ = "Integer32"
_CeRTxFx01FiberSignalDetect_Object = MibTableColumn
ceRTxFx01FiberSignalDetect = _CeRTxFx01FiberSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 9, 1, 5),
    _CeRTxFx01FiberSignalDetect_Type()
)
ceRTxFx01FiberSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceRTxFx01FiberSignalDetect.setStatus("mandatory")
_Ce100BtxFx04Table_Object = MibTable
ce100BtxFx04Table = _Ce100BtxFx04Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    ce100BtxFx04Table.setStatus("mandatory")
_Ce100BtxFx04Entry_Object = MibTableRow
ce100BtxFx04Entry = _Ce100BtxFx04Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 10, 1)
)
ce100BtxFx04Entry.setIndexNames(
    (0, "MCC16-MIB", "ce100BtxFx04Index"),
)
if mibBuilder.loadTexts:
    ce100BtxFx04Entry.setStatus("mandatory")
_Ce100BtxFx04Index_Type = Integer32
_Ce100BtxFx04Index_Object = MibTableColumn
ce100BtxFx04Index = _Ce100BtxFx04Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 10, 1, 1),
    _Ce100BtxFx04Index_Type()
)
ce100BtxFx04Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04Index.setStatus("mandatory")


class _Ce100BtxFx04TPRecv_Type(Integer32):
    """Custom type ce100BtxFx04TPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFx04TPRecv_Type.__name__ = "Integer32"
_Ce100BtxFx04TPRecv_Object = MibTableColumn
ce100BtxFx04TPRecv = _Ce100BtxFx04TPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 10, 1, 2),
    _Ce100BtxFx04TPRecv_Type()
)
ce100BtxFx04TPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04TPRecv.setStatus("mandatory")


class _Ce100BtxFx04FiberRecv_Type(Integer32):
    """Custom type ce100BtxFx04FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFx04FiberRecv_Type.__name__ = "Integer32"
_Ce100BtxFx04FiberRecv_Object = MibTableColumn
ce100BtxFx04FiberRecv = _Ce100BtxFx04FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 10, 1, 3),
    _Ce100BtxFx04FiberRecv_Type()
)
ce100BtxFx04FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04FiberRecv.setStatus("mandatory")


class _Ce100BtxFx04TPSignalDetect_Type(Integer32):
    """Custom type ce100BtxFx04TPSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFx04TPSignalDetect_Type.__name__ = "Integer32"
_Ce100BtxFx04TPSignalDetect_Object = MibTableColumn
ce100BtxFx04TPSignalDetect = _Ce100BtxFx04TPSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 10, 1, 4),
    _Ce100BtxFx04TPSignalDetect_Type()
)
ce100BtxFx04TPSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04TPSignalDetect.setStatus("mandatory")


class _Ce100BtxFx04FiberSignalDetect_Type(Integer32):
    """Custom type ce100BtxFx04FiberSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFx04FiberSignalDetect_Type.__name__ = "Integer32"
_Ce100BtxFx04FiberSignalDetect_Object = MibTableColumn
ce100BtxFx04FiberSignalDetect = _Ce100BtxFx04FiberSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 10, 1, 5),
    _Ce100BtxFx04FiberSignalDetect_Type()
)
ce100BtxFx04FiberSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04FiberSignalDetect.setStatus("mandatory")


class _Ce100BtxFx04Power_Type(Integer32):
    """Custom type ce100BtxFx04Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFx04Power_Type.__name__ = "Integer32"
_Ce100BtxFx04Power_Object = MibTableColumn
ce100BtxFx04Power = _Ce100BtxFx04Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 10, 1, 6),
    _Ce100BtxFx04Power_Type()
)
ce100BtxFx04Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04Power.setStatus("mandatory")
_CpsCf01Table_Object = MibTable
cpsCf01Table = _CpsCf01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cpsCf01Table.setStatus("mandatory")
_CpsCf01Entry_Object = MibTableRow
cpsCf01Entry = _CpsCf01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 12, 1)
)
cpsCf01Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsCf01Index"),
)
if mibBuilder.loadTexts:
    cpsCf01Entry.setStatus("mandatory")
_CpsCf01Index_Type = Integer32
_CpsCf01Index_Object = MibTableColumn
cpsCf01Index = _CpsCf01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 12, 1, 1),
    _CpsCf01Index_Type()
)
cpsCf01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsCf01Index.setStatus("mandatory")


class _CpsCf01FiberRecv_Type(Integer32):
    """Custom type cpsCf01FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CpsCf01FiberRecv_Type.__name__ = "Integer32"
_CpsCf01FiberRecv_Object = MibTableColumn
cpsCf01FiberRecv = _CpsCf01FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 12, 1, 2),
    _CpsCf01FiberRecv_Type()
)
cpsCf01FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsCf01FiberRecv.setStatus("mandatory")


class _CpsCf01TPRecv_Type(Integer32):
    """Custom type cpsCf01TPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CpsCf01TPRecv_Type.__name__ = "Integer32"
_CpsCf01TPRecv_Object = MibTableColumn
cpsCf01TPRecv = _CpsCf01TPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 12, 1, 3),
    _CpsCf01TPRecv_Type()
)
cpsCf01TPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsCf01TPRecv.setStatus("mandatory")


class _CpsCf01Power_Type(Integer32):
    """Custom type cpsCf01Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CpsCf01Power_Type.__name__ = "Integer32"
_CpsCf01Power_Object = MibTableColumn
cpsCf01Power = _CpsCf01Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 12, 1, 4),
    _CpsCf01Power_Type()
)
cpsCf01Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsCf01Power.setStatus("mandatory")
_CbCf01Table_Object = MibTable
cbCf01Table = _CbCf01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cbCf01Table.setStatus("mandatory")
_CbCf01Entry_Object = MibTableRow
cbCf01Entry = _CbCf01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 13, 1)
)
cbCf01Entry.setIndexNames(
    (0, "MCC16-MIB", "cbCf01Index"),
)
if mibBuilder.loadTexts:
    cbCf01Entry.setStatus("mandatory")
_CbCf01Index_Type = Integer32
_CbCf01Index_Object = MibTableColumn
cbCf01Index = _CbCf01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 13, 1, 1),
    _CbCf01Index_Type()
)
cbCf01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCf01Index.setStatus("mandatory")


class _CbCf01FiberRecv_Type(Integer32):
    """Custom type cbCf01FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CbCf01FiberRecv_Type.__name__ = "Integer32"
_CbCf01FiberRecv_Object = MibTableColumn
cbCf01FiberRecv = _CbCf01FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 13, 1, 2),
    _CbCf01FiberRecv_Type()
)
cbCf01FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCf01FiberRecv.setStatus("mandatory")


class _CbCf01TPCoaxRecv_Type(Integer32):
    """Custom type cbCf01TPCoaxRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CbCf01TPCoaxRecv_Type.__name__ = "Integer32"
_CbCf01TPCoaxRecv_Object = MibTableColumn
cbCf01TPCoaxRecv = _CbCf01TPCoaxRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 13, 1, 3),
    _CbCf01TPCoaxRecv_Type()
)
cbCf01TPCoaxRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCf01TPCoaxRecv.setStatus("mandatory")


class _CbCf01Power_Type(Integer32):
    """Custom type cbCf01Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CbCf01Power_Type.__name__ = "Integer32"
_CbCf01Power_Object = MibTableColumn
cbCf01Power = _CbCf01Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 13, 1, 4),
    _CbCf01Power_Type()
)
cbCf01Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCf01Power.setStatus("mandatory")
_CarCf01Table_Object = MibTable
carCf01Table = _CarCf01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 14)
)
if mibBuilder.loadTexts:
    carCf01Table.setStatus("mandatory")
_CarCf01Entry_Object = MibTableRow
carCf01Entry = _CarCf01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 14, 1)
)
carCf01Entry.setIndexNames(
    (0, "MCC16-MIB", "carCf01Index"),
)
if mibBuilder.loadTexts:
    carCf01Entry.setStatus("mandatory")
_CarCf01Index_Type = Integer32
_CarCf01Index_Object = MibTableColumn
carCf01Index = _CarCf01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 14, 1, 1),
    _CarCf01Index_Type()
)
carCf01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carCf01Index.setStatus("mandatory")


class _CarCf01FiberRecv_Type(Integer32):
    """Custom type carCf01FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CarCf01FiberRecv_Type.__name__ = "Integer32"
_CarCf01FiberRecv_Object = MibTableColumn
carCf01FiberRecv = _CarCf01FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 14, 1, 2),
    _CarCf01FiberRecv_Type()
)
carCf01FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carCf01FiberRecv.setStatus("mandatory")


class _CarCf01TPRecv_Type(Integer32):
    """Custom type carCf01TPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CarCf01TPRecv_Type.__name__ = "Integer32"
_CarCf01TPRecv_Object = MibTableColumn
carCf01TPRecv = _CarCf01TPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 14, 1, 3),
    _CarCf01TPRecv_Type()
)
carCf01TPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carCf01TPRecv.setStatus("mandatory")


class _CarCf01Power_Type(Integer32):
    """Custom type carCf01Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CarCf01Power_Type.__name__ = "Integer32"
_CarCf01Power_Object = MibTableColumn
carCf01Power = _CarCf01Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 14, 1, 4),
    _CarCf01Power_Type()
)
carCf01Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carCf01Power.setStatus("mandatory")
_CarCf02Table_Object = MibTable
carCf02Table = _CarCf02Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 15)
)
if mibBuilder.loadTexts:
    carCf02Table.setStatus("mandatory")
_CarCf02Entry_Object = MibTableRow
carCf02Entry = _CarCf02Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 15, 1)
)
carCf02Entry.setIndexNames(
    (0, "MCC16-MIB", "carCf02Index"),
)
if mibBuilder.loadTexts:
    carCf02Entry.setStatus("mandatory")
_CarCf02Index_Type = Integer32
_CarCf02Index_Object = MibTableColumn
carCf02Index = _CarCf02Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 15, 1, 1),
    _CarCf02Index_Type()
)
carCf02Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carCf02Index.setStatus("mandatory")


class _CarCf02FiberRecv_Type(Integer32):
    """Custom type carCf02FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CarCf02FiberRecv_Type.__name__ = "Integer32"
_CarCf02FiberRecv_Object = MibTableColumn
carCf02FiberRecv = _CarCf02FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 15, 1, 2),
    _CarCf02FiberRecv_Type()
)
carCf02FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carCf02FiberRecv.setStatus("mandatory")


class _CarCf02CoaxRecv_Type(Integer32):
    """Custom type carCf02CoaxRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CarCf02CoaxRecv_Type.__name__ = "Integer32"
_CarCf02CoaxRecv_Object = MibTableColumn
carCf02CoaxRecv = _CarCf02CoaxRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 15, 1, 3),
    _CarCf02CoaxRecv_Type()
)
carCf02CoaxRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carCf02CoaxRecv.setStatus("mandatory")


class _CarCf02Power_Type(Integer32):
    """Custom type carCf02Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CarCf02Power_Type.__name__ = "Integer32"
_CarCf02Power_Object = MibTableColumn
carCf02Power = _CarCf02Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 15, 1, 4),
    _CarCf02Power_Type()
)
carCf02Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carCf02Power.setStatus("mandatory")
_CePswFx03Table_Object = MibTable
cePswFx03Table = _CePswFx03Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cePswFx03Table.setStatus("mandatory")
_CePswFx03Entry_Object = MibTableRow
cePswFx03Entry = _CePswFx03Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 16, 1)
)
cePswFx03Entry.setIndexNames(
    (0, "MCC16-MIB", "cePswFx03Index"),
)
if mibBuilder.loadTexts:
    cePswFx03Entry.setStatus("mandatory")
_CePswFx03Index_Type = Integer32
_CePswFx03Index_Object = MibTableColumn
cePswFx03Index = _CePswFx03Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 16, 1, 1),
    _CePswFx03Index_Type()
)
cePswFx03Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswFx03Index.setStatus("mandatory")


class _CePswFx03TPFullDuplex_Type(Integer32):
    """Custom type cePswFx03TPFullDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CePswFx03TPFullDuplex_Type.__name__ = "Integer32"
_CePswFx03TPFullDuplex_Object = MibTableColumn
cePswFx03TPFullDuplex = _CePswFx03TPFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 16, 1, 2),
    _CePswFx03TPFullDuplex_Type()
)
cePswFx03TPFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswFx03TPFullDuplex.setStatus("mandatory")


class _CePswFx03FiberFullDuplex_Type(Integer32):
    """Custom type cePswFx03FiberFullDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CePswFx03FiberFullDuplex_Type.__name__ = "Integer32"
_CePswFx03FiberFullDuplex_Object = MibTableColumn
cePswFx03FiberFullDuplex = _CePswFx03FiberFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 16, 1, 3),
    _CePswFx03FiberFullDuplex_Type()
)
cePswFx03FiberFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswFx03FiberFullDuplex.setStatus("mandatory")


class _CePswFx03TPLink_Type(Integer32):
    """Custom type cePswFx03TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CePswFx03TPLink_Type.__name__ = "Integer32"
_CePswFx03TPLink_Object = MibTableColumn
cePswFx03TPLink = _CePswFx03TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 16, 1, 4),
    _CePswFx03TPLink_Type()
)
cePswFx03TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswFx03TPLink.setStatus("mandatory")


class _CePswFx03FiberLink_Type(Integer32):
    """Custom type cePswFx03FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CePswFx03FiberLink_Type.__name__ = "Integer32"
_CePswFx03FiberLink_Object = MibTableColumn
cePswFx03FiberLink = _CePswFx03FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 16, 1, 5),
    _CePswFx03FiberLink_Type()
)
cePswFx03FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswFx03FiberLink.setStatus("mandatory")


class _CePswFx03TP100Mbps_Type(Integer32):
    """Custom type cePswFx03TP100Mbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CePswFx03TP100Mbps_Type.__name__ = "Integer32"
_CePswFx03TP100Mbps_Object = MibTableColumn
cePswFx03TP100Mbps = _CePswFx03TP100Mbps_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 16, 1, 6),
    _CePswFx03TP100Mbps_Type()
)
cePswFx03TP100Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswFx03TP100Mbps.setStatus("mandatory")
_CePswSx01Table_Object = MibTable
cePswSx01Table = _CePswSx01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 17)
)
if mibBuilder.loadTexts:
    cePswSx01Table.setStatus("mandatory")
_CePswSx01Entry_Object = MibTableRow
cePswSx01Entry = _CePswSx01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 17, 1)
)
cePswSx01Entry.setIndexNames(
    (0, "MCC16-MIB", "cePswSx01Index"),
)
if mibBuilder.loadTexts:
    cePswSx01Entry.setStatus("mandatory")
_CePswSx01Index_Type = Integer32
_CePswSx01Index_Object = MibTableColumn
cePswSx01Index = _CePswSx01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 17, 1, 1),
    _CePswSx01Index_Type()
)
cePswSx01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswSx01Index.setStatus("mandatory")


class _CePswSx01TPFullDuplex_Type(Integer32):
    """Custom type cePswSx01TPFullDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CePswSx01TPFullDuplex_Type.__name__ = "Integer32"
_CePswSx01TPFullDuplex_Object = MibTableColumn
cePswSx01TPFullDuplex = _CePswSx01TPFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 17, 1, 2),
    _CePswSx01TPFullDuplex_Type()
)
cePswSx01TPFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswSx01TPFullDuplex.setStatus("mandatory")


class _CePswSx01FiberFullDuplex_Type(Integer32):
    """Custom type cePswSx01FiberFullDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CePswSx01FiberFullDuplex_Type.__name__ = "Integer32"
_CePswSx01FiberFullDuplex_Object = MibTableColumn
cePswSx01FiberFullDuplex = _CePswSx01FiberFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 17, 1, 3),
    _CePswSx01FiberFullDuplex_Type()
)
cePswSx01FiberFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswSx01FiberFullDuplex.setStatus("mandatory")


class _CePswSx01TPLink_Type(Integer32):
    """Custom type cePswSx01TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CePswSx01TPLink_Type.__name__ = "Integer32"
_CePswSx01TPLink_Object = MibTableColumn
cePswSx01TPLink = _CePswSx01TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 17, 1, 4),
    _CePswSx01TPLink_Type()
)
cePswSx01TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswSx01TPLink.setStatus("mandatory")


class _CePswSx01FiberLink_Type(Integer32):
    """Custom type cePswSx01FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CePswSx01FiberLink_Type.__name__ = "Integer32"
_CePswSx01FiberLink_Object = MibTableColumn
cePswSx01FiberLink = _CePswSx01FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 17, 1, 5),
    _CePswSx01FiberLink_Type()
)
cePswSx01FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswSx01FiberLink.setStatus("mandatory")


class _CePswSx01TP100Mbps_Type(Integer32):
    """Custom type cePswSx01TP100Mbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CePswSx01TP100Mbps_Type.__name__ = "Integer32"
_CePswSx01TP100Mbps_Object = MibTableColumn
cePswSx01TP100Mbps = _CePswSx01TP100Mbps_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 17, 1, 6),
    _CePswSx01TP100Mbps_Type()
)
cePswSx01TP100Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cePswSx01TP100Mbps.setStatus("mandatory")
_CRs232Cf01Table_Object = MibTable
cRs232Cf01Table = _CRs232Cf01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cRs232Cf01Table.setStatus("mandatory")
_CRs232Cf01Entry_Object = MibTableRow
cRs232Cf01Entry = _CRs232Cf01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 18, 1)
)
cRs232Cf01Entry.setIndexNames(
    (0, "MCC16-MIB", "cRs232Cf01Index"),
)
if mibBuilder.loadTexts:
    cRs232Cf01Entry.setStatus("mandatory")
_CRs232Cf01Index_Type = Integer32
_CRs232Cf01Index_Object = MibTableColumn
cRs232Cf01Index = _CRs232Cf01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 18, 1, 1),
    _CRs232Cf01Index_Type()
)
cRs232Cf01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRs232Cf01Index.setStatus("mandatory")


class _CRs232Cf01FiberLock_Type(Integer32):
    """Custom type cRs232Cf01FiberLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CRs232Cf01FiberLock_Type.__name__ = "Integer32"
_CRs232Cf01FiberLock_Object = MibTableColumn
cRs232Cf01FiberLock = _CRs232Cf01FiberLock_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 18, 1, 2),
    _CRs232Cf01FiberLock_Type()
)
cRs232Cf01FiberLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRs232Cf01FiberLock.setStatus("mandatory")
_CfSmMm04Table_Object = MibTable
cfSmMm04Table = _CfSmMm04Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 24)
)
if mibBuilder.loadTexts:
    cfSmMm04Table.setStatus("mandatory")
_CfSmMm04Entry_Object = MibTableRow
cfSmMm04Entry = _CfSmMm04Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 24, 1)
)
cfSmMm04Entry.setIndexNames(
    (0, "MCC16-MIB", "cfSmMm04Index"),
)
if mibBuilder.loadTexts:
    cfSmMm04Entry.setStatus("mandatory")
_CfSmMm04Index_Type = Integer32
_CfSmMm04Index_Object = MibTableColumn
cfSmMm04Index = _CfSmMm04Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 24, 1, 1),
    _CfSmMm04Index_Type()
)
cfSmMm04Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm04Index.setStatus("mandatory")


class _CfSmMm04MMSignalDetect_Type(Integer32):
    """Custom type cfSmMm04MMSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm04MMSignalDetect_Type.__name__ = "Integer32"
_CfSmMm04MMSignalDetect_Object = MibTableColumn
cfSmMm04MMSignalDetect = _CfSmMm04MMSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 24, 1, 2),
    _CfSmMm04MMSignalDetect_Type()
)
cfSmMm04MMSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm04MMSignalDetect.setStatus("mandatory")


class _CfSmMm04SMSignalDetect_Type(Integer32):
    """Custom type cfSmMm04SMSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm04SMSignalDetect_Type.__name__ = "Integer32"
_CfSmMm04SMSignalDetect_Object = MibTableColumn
cfSmMm04SMSignalDetect = _CfSmMm04SMSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 24, 1, 3),
    _CfSmMm04SMSignalDetect_Type()
)
cfSmMm04SMSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm04SMSignalDetect.setStatus("mandatory")


class _CfSmMm04Power_Type(Integer32):
    """Custom type cfSmMm04Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfSmMm04Power_Type.__name__ = "Integer32"
_CfSmMm04Power_Object = MibTableColumn
cfSmMm04Power = _CfSmMm04Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 24, 1, 4),
    _CfSmMm04Power_Type()
)
cfSmMm04Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfSmMm04Power.setStatus("mandatory")
_Ce100BtxSx01Table_Object = MibTable
ce100BtxSx01Table = _Ce100BtxSx01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 26)
)
if mibBuilder.loadTexts:
    ce100BtxSx01Table.setStatus("mandatory")
_Ce100BtxSx01Entry_Object = MibTableRow
ce100BtxSx01Entry = _Ce100BtxSx01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 26, 1)
)
ce100BtxSx01Entry.setIndexNames(
    (0, "MCC16-MIB", "ce100BtxSx01Index"),
)
if mibBuilder.loadTexts:
    ce100BtxSx01Entry.setStatus("mandatory")
_Ce100BtxSx01Index_Type = Integer32
_Ce100BtxSx01Index_Object = MibTableColumn
ce100BtxSx01Index = _Ce100BtxSx01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 26, 1, 1),
    _Ce100BtxSx01Index_Type()
)
ce100BtxSx01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxSx01Index.setStatus("mandatory")


class _Ce100BtxSx01TPRecv_Type(Integer32):
    """Custom type ce100BtxSx01TPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxSx01TPRecv_Type.__name__ = "Integer32"
_Ce100BtxSx01TPRecv_Object = MibTableColumn
ce100BtxSx01TPRecv = _Ce100BtxSx01TPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 26, 1, 2),
    _Ce100BtxSx01TPRecv_Type()
)
ce100BtxSx01TPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxSx01TPRecv.setStatus("mandatory")


class _Ce100BtxSx01FiberRecv_Type(Integer32):
    """Custom type ce100BtxSx01FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxSx01FiberRecv_Type.__name__ = "Integer32"
_Ce100BtxSx01FiberRecv_Object = MibTableColumn
ce100BtxSx01FiberRecv = _Ce100BtxSx01FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 26, 1, 3),
    _Ce100BtxSx01FiberRecv_Type()
)
ce100BtxSx01FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxSx01FiberRecv.setStatus("mandatory")


class _Ce100BtxSx01TPSignalDetect_Type(Integer32):
    """Custom type ce100BtxSx01TPSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxSx01TPSignalDetect_Type.__name__ = "Integer32"
_Ce100BtxSx01TPSignalDetect_Object = MibTableColumn
ce100BtxSx01TPSignalDetect = _Ce100BtxSx01TPSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 26, 1, 4),
    _Ce100BtxSx01TPSignalDetect_Type()
)
ce100BtxSx01TPSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxSx01TPSignalDetect.setStatus("mandatory")


class _Ce100BtxSx01FiberSignalDetect_Type(Integer32):
    """Custom type ce100BtxSx01FiberSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxSx01FiberSignalDetect_Type.__name__ = "Integer32"
_Ce100BtxSx01FiberSignalDetect_Object = MibTableColumn
ce100BtxSx01FiberSignalDetect = _Ce100BtxSx01FiberSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 26, 1, 5),
    _Ce100BtxSx01FiberSignalDetect_Type()
)
ce100BtxSx01FiberSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxSx01FiberSignalDetect.setStatus("mandatory")


class _Ce100BtxSx01Power_Type(Integer32):
    """Custom type ce100BtxSx01Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxSx01Power_Type.__name__ = "Integer32"
_Ce100BtxSx01Power_Object = MibTableColumn
ce100BtxSx01Power = _Ce100BtxSx01Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 26, 1, 6),
    _Ce100BtxSx01Power_Type()
)
ce100BtxSx01Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxSx01Power.setStatus("mandatory")
_Ce100BtxFx04MtTable_Object = MibTable
ce100BtxFx04MtTable = _Ce100BtxFx04MtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 27)
)
if mibBuilder.loadTexts:
    ce100BtxFx04MtTable.setStatus("mandatory")
_Ce100BtxFx04MtEntry_Object = MibTableRow
ce100BtxFx04MtEntry = _Ce100BtxFx04MtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 27, 1)
)
ce100BtxFx04MtEntry.setIndexNames(
    (0, "MCC16-MIB", "ce100BtxFx04MtIndex"),
)
if mibBuilder.loadTexts:
    ce100BtxFx04MtEntry.setStatus("mandatory")
_Ce100BtxFx04MtIndex_Type = Integer32
_Ce100BtxFx04MtIndex_Object = MibTableColumn
ce100BtxFx04MtIndex = _Ce100BtxFx04MtIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 27, 1, 1),
    _Ce100BtxFx04MtIndex_Type()
)
ce100BtxFx04MtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04MtIndex.setStatus("mandatory")


class _Ce100BtxFx04MtTPRecv_Type(Integer32):
    """Custom type ce100BtxFx04MtTPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFx04MtTPRecv_Type.__name__ = "Integer32"
_Ce100BtxFx04MtTPRecv_Object = MibTableColumn
ce100BtxFx04MtTPRecv = _Ce100BtxFx04MtTPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 27, 1, 2),
    _Ce100BtxFx04MtTPRecv_Type()
)
ce100BtxFx04MtTPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04MtTPRecv.setStatus("mandatory")


class _Ce100BtxFx04MtFiberRecv_Type(Integer32):
    """Custom type ce100BtxFx04MtFiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFx04MtFiberRecv_Type.__name__ = "Integer32"
_Ce100BtxFx04MtFiberRecv_Object = MibTableColumn
ce100BtxFx04MtFiberRecv = _Ce100BtxFx04MtFiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 27, 1, 3),
    _Ce100BtxFx04MtFiberRecv_Type()
)
ce100BtxFx04MtFiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04MtFiberRecv.setStatus("mandatory")


class _Ce100BtxFx04MtTPSignalDetect_Type(Integer32):
    """Custom type ce100BtxFx04MtTPSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFx04MtTPSignalDetect_Type.__name__ = "Integer32"
_Ce100BtxFx04MtTPSignalDetect_Object = MibTableColumn
ce100BtxFx04MtTPSignalDetect = _Ce100BtxFx04MtTPSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 27, 1, 4),
    _Ce100BtxFx04MtTPSignalDetect_Type()
)
ce100BtxFx04MtTPSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04MtTPSignalDetect.setStatus("mandatory")


class _Ce100BtxFx04MtFiberSignalDetect_Type(Integer32):
    """Custom type ce100BtxFx04MtFiberSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFx04MtFiberSignalDetect_Type.__name__ = "Integer32"
_Ce100BtxFx04MtFiberSignalDetect_Object = MibTableColumn
ce100BtxFx04MtFiberSignalDetect = _Ce100BtxFx04MtFiberSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 27, 1, 5),
    _Ce100BtxFx04MtFiberSignalDetect_Type()
)
ce100BtxFx04MtFiberSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04MtFiberSignalDetect.setStatus("mandatory")


class _Ce100BtxFx04MtPower_Type(Integer32):
    """Custom type ce100BtxFx04MtPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFx04MtPower_Type.__name__ = "Integer32"
_Ce100BtxFx04MtPower_Object = MibTableColumn
ce100BtxFx04MtPower = _Ce100BtxFx04MtPower_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 27, 1, 6),
    _Ce100BtxFx04MtPower_Type()
)
ce100BtxFx04MtPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFx04MtPower.setStatus("mandatory")
_CfdCd01Table_Object = MibTable
cfdCd01Table = _CfdCd01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 28)
)
if mibBuilder.loadTexts:
    cfdCd01Table.setStatus("mandatory")
_CfdCd01Entry_Object = MibTableRow
cfdCd01Entry = _CfdCd01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 28, 1)
)
cfdCd01Entry.setIndexNames(
    (0, "MCC16-MIB", "cfdCd01Index"),
)
if mibBuilder.loadTexts:
    cfdCd01Entry.setStatus("mandatory")
_CfdCd01Index_Type = Integer32
_CfdCd01Index_Object = MibTableColumn
cfdCd01Index = _CfdCd01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 28, 1, 1),
    _CfdCd01Index_Type()
)
cfdCd01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdCd01Index.setStatus("mandatory")


class _CfdCd01Lock_Type(Integer32):
    """Custom type cfdCd01Lock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfdCd01Lock_Type.__name__ = "Integer32"
_CfdCd01Lock_Object = MibTableColumn
cfdCd01Lock = _CfdCd01Lock_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 28, 1, 2),
    _CfdCd01Lock_Type()
)
cfdCd01Lock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdCd01Lock.setStatus("mandatory")


class _CfdCd01TPRecv_Type(Integer32):
    """Custom type cfdCd01TPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfdCd01TPRecv_Type.__name__ = "Integer32"
_CfdCd01TPRecv_Object = MibTableColumn
cfdCd01TPRecv = _CfdCd01TPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 28, 1, 3),
    _CfdCd01TPRecv_Type()
)
cfdCd01TPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdCd01TPRecv.setStatus("mandatory")


class _CfdCd01FiberRecv_Type(Integer32):
    """Custom type cfdCd01FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfdCd01FiberRecv_Type.__name__ = "Integer32"
_CfdCd01FiberRecv_Object = MibTableColumn
cfdCd01FiberRecv = _CfdCd01FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 28, 1, 4),
    _CfdCd01FiberRecv_Type()
)
cfdCd01FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdCd01FiberRecv.setStatus("mandatory")


class _CfdCd01TPSignalDetect_Type(Integer32):
    """Custom type cfdCd01TPSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfdCd01TPSignalDetect_Type.__name__ = "Integer32"
_CfdCd01TPSignalDetect_Object = MibTableColumn
cfdCd01TPSignalDetect = _CfdCd01TPSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 28, 1, 5),
    _CfdCd01TPSignalDetect_Type()
)
cfdCd01TPSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdCd01TPSignalDetect.setStatus("mandatory")


class _CfdCd01FiberSignalDetect_Type(Integer32):
    """Custom type cfdCd01FiberSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CfdCd01FiberSignalDetect_Type.__name__ = "Integer32"
_CfdCd01FiberSignalDetect_Object = MibTableColumn
cfdCd01FiberSignalDetect = _CfdCd01FiberSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 28, 1, 6),
    _CfdCd01FiberSignalDetect_Type()
)
cfdCd01FiberSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdCd01FiberSignalDetect.setStatus("mandatory")
_CtrCf01Table_Object = MibTable
ctrCf01Table = _CtrCf01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 29)
)
if mibBuilder.loadTexts:
    ctrCf01Table.setStatus("mandatory")
_CtrCf01Entry_Object = MibTableRow
ctrCf01Entry = _CtrCf01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 29, 1)
)
ctrCf01Entry.setIndexNames(
    (0, "MCC16-MIB", "ctrCf01Index"),
)
if mibBuilder.loadTexts:
    ctrCf01Entry.setStatus("mandatory")
_CtrCf01Index_Type = Integer32
_CtrCf01Index_Object = MibTableColumn
ctrCf01Index = _CtrCf01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 29, 1, 1),
    _CtrCf01Index_Type()
)
ctrCf01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrCf01Index.setStatus("mandatory")


class _CtrCf01FiberinOK_Type(Integer32):
    """Custom type ctrCf01FiberinOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CtrCf01FiberinOK_Type.__name__ = "Integer32"
_CtrCf01FiberinOK_Object = MibTableColumn
ctrCf01FiberinOK = _CtrCf01FiberinOK_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 29, 1, 2),
    _CtrCf01FiberinOK_Type()
)
ctrCf01FiberinOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrCf01FiberinOK.setStatus("mandatory")


class _CtrCf01TPinOK_Type(Integer32):
    """Custom type ctrCf01TPinOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CtrCf01TPinOK_Type.__name__ = "Integer32"
_CtrCf01TPinOK_Object = MibTableColumn
ctrCf01TPinOK = _CtrCf01TPinOK_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 29, 1, 3),
    _CtrCf01TPinOK_Type()
)
ctrCf01TPinOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrCf01TPinOK.setStatus("mandatory")


class _CtrCf01Inserted_Type(Integer32):
    """Custom type ctrCf01Inserted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CtrCf01Inserted_Type.__name__ = "Integer32"
_CtrCf01Inserted_Object = MibTableColumn
ctrCf01Inserted = _CtrCf01Inserted_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 29, 1, 4),
    _CtrCf01Inserted_Type()
)
ctrCf01Inserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrCf01Inserted.setStatus("mandatory")
_Ce100BtxFrl03Table_Object = MibTable
ce100BtxFrl03Table = _Ce100BtxFrl03Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 30)
)
if mibBuilder.loadTexts:
    ce100BtxFrl03Table.setStatus("mandatory")
_Ce100BtxFrl03Entry_Object = MibTableRow
ce100BtxFrl03Entry = _Ce100BtxFrl03Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 30, 1)
)
ce100BtxFrl03Entry.setIndexNames(
    (0, "MCC16-MIB", "ce100BtxFrl03Index"),
)
if mibBuilder.loadTexts:
    ce100BtxFrl03Entry.setStatus("mandatory")
_Ce100BtxFrl03Index_Type = Integer32
_Ce100BtxFrl03Index_Object = MibTableColumn
ce100BtxFrl03Index = _Ce100BtxFrl03Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 30, 1, 1),
    _Ce100BtxFrl03Index_Type()
)
ce100BtxFrl03Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFrl03Index.setStatus("mandatory")


class _Ce100BtxFrl03Lock_Type(Integer32):
    """Custom type ce100BtxFrl03Lock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFrl03Lock_Type.__name__ = "Integer32"
_Ce100BtxFrl03Lock_Object = MibTableColumn
ce100BtxFrl03Lock = _Ce100BtxFrl03Lock_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 30, 1, 2),
    _Ce100BtxFrl03Lock_Type()
)
ce100BtxFrl03Lock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFrl03Lock.setStatus("mandatory")


class _Ce100BtxFrl03TPRecv_Type(Integer32):
    """Custom type ce100BtxFrl03TPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFrl03TPRecv_Type.__name__ = "Integer32"
_Ce100BtxFrl03TPRecv_Object = MibTableColumn
ce100BtxFrl03TPRecv = _Ce100BtxFrl03TPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 30, 1, 3),
    _Ce100BtxFrl03TPRecv_Type()
)
ce100BtxFrl03TPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFrl03TPRecv.setStatus("mandatory")


class _Ce100BtxFrl03FiberRecv_Type(Integer32):
    """Custom type ce100BtxFrl03FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFrl03FiberRecv_Type.__name__ = "Integer32"
_Ce100BtxFrl03FiberRecv_Object = MibTableColumn
ce100BtxFrl03FiberRecv = _Ce100BtxFrl03FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 30, 1, 4),
    _Ce100BtxFrl03FiberRecv_Type()
)
ce100BtxFrl03FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFrl03FiberRecv.setStatus("mandatory")


class _Ce100BtxFrl03TPSignalDetect_Type(Integer32):
    """Custom type ce100BtxFrl03TPSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFrl03TPSignalDetect_Type.__name__ = "Integer32"
_Ce100BtxFrl03TPSignalDetect_Object = MibTableColumn
ce100BtxFrl03TPSignalDetect = _Ce100BtxFrl03TPSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 30, 1, 5),
    _Ce100BtxFrl03TPSignalDetect_Type()
)
ce100BtxFrl03TPSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFrl03TPSignalDetect.setStatus("mandatory")


class _Ce100BtxFrl03FiberSignalDetect_Type(Integer32):
    """Custom type ce100BtxFrl03FiberSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Ce100BtxFrl03FiberSignalDetect_Type.__name__ = "Integer32"
_Ce100BtxFrl03FiberSignalDetect_Object = MibTableColumn
ce100BtxFrl03FiberSignalDetect = _Ce100BtxFrl03FiberSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 30, 1, 6),
    _Ce100BtxFrl03FiberSignalDetect_Type()
)
ce100BtxFrl03FiberSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ce100BtxFrl03FiberSignalDetect.setStatus("mandatory")
_ChstrCf01Table_Object = MibTable
chstrCf01Table = _ChstrCf01Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 34)
)
if mibBuilder.loadTexts:
    chstrCf01Table.setStatus("mandatory")
_ChstrCf01Entry_Object = MibTableRow
chstrCf01Entry = _ChstrCf01Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 34, 1)
)
chstrCf01Entry.setIndexNames(
    (0, "MCC16-MIB", "chstrCf01Index"),
)
if mibBuilder.loadTexts:
    chstrCf01Entry.setStatus("mandatory")
_ChstrCf01Index_Type = Integer32
_ChstrCf01Index_Object = MibTableColumn
chstrCf01Index = _ChstrCf01Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 34, 1, 1),
    _ChstrCf01Index_Type()
)
chstrCf01Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chstrCf01Index.setStatus("mandatory")


class _ChstrCf01TPRecv_Type(Integer32):
    """Custom type chstrCf01TPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ChstrCf01TPRecv_Type.__name__ = "Integer32"
_ChstrCf01TPRecv_Object = MibTableColumn
chstrCf01TPRecv = _ChstrCf01TPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 34, 1, 2),
    _ChstrCf01TPRecv_Type()
)
chstrCf01TPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chstrCf01TPRecv.setStatus("mandatory")


class _ChstrCf01FiberRecv_Type(Integer32):
    """Custom type chstrCf01FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ChstrCf01FiberRecv_Type.__name__ = "Integer32"
_ChstrCf01FiberRecv_Object = MibTableColumn
chstrCf01FiberRecv = _ChstrCf01FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 34, 1, 3),
    _ChstrCf01FiberRecv_Type()
)
chstrCf01FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chstrCf01FiberRecv.setStatus("mandatory")


class _ChstrCf01TPSignalDetect_Type(Integer32):
    """Custom type chstrCf01TPSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ChstrCf01TPSignalDetect_Type.__name__ = "Integer32"
_ChstrCf01TPSignalDetect_Object = MibTableColumn
chstrCf01TPSignalDetect = _ChstrCf01TPSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 34, 1, 4),
    _ChstrCf01TPSignalDetect_Type()
)
chstrCf01TPSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chstrCf01TPSignalDetect.setStatus("mandatory")


class _ChstrCf01FiberSignalDetect_Type(Integer32):
    """Custom type chstrCf01FiberSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ChstrCf01FiberSignalDetect_Type.__name__ = "Integer32"
_ChstrCf01FiberSignalDetect_Object = MibTableColumn
chstrCf01FiberSignalDetect = _ChstrCf01FiberSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 34, 1, 5),
    _ChstrCf01FiberSignalDetect_Type()
)
chstrCf01FiberSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chstrCf01FiberSignalDetect.setStatus("mandatory")
_CeTxSx02Table_Object = MibTable
ceTxSx02Table = _CeTxSx02Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 35)
)
if mibBuilder.loadTexts:
    ceTxSx02Table.setStatus("mandatory")
_CeTxSx02Entry_Object = MibTableRow
ceTxSx02Entry = _CeTxSx02Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 35, 1)
)
ceTxSx02Entry.setIndexNames(
    (0, "MCC16-MIB", "ceTxSx02Index"),
)
if mibBuilder.loadTexts:
    ceTxSx02Entry.setStatus("mandatory")
_CeTxSx02Index_Type = Integer32
_CeTxSx02Index_Object = MibTableColumn
ceTxSx02Index = _CeTxSx02Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 35, 1, 1),
    _CeTxSx02Index_Type()
)
ceTxSx02Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTxSx02Index.setStatus("mandatory")


class _CeTxSx02TPLink_Type(Integer32):
    """Custom type ceTxSx02TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTxSx02TPLink_Type.__name__ = "Integer32"
_CeTxSx02TPLink_Object = MibTableColumn
ceTxSx02TPLink = _CeTxSx02TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 35, 1, 2),
    _CeTxSx02TPLink_Type()
)
ceTxSx02TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTxSx02TPLink.setStatus("mandatory")


class _CeTxSx02FiberLink_Type(Integer32):
    """Custom type ceTxSx02FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTxSx02FiberLink_Type.__name__ = "Integer32"
_CeTxSx02FiberLink_Object = MibTableColumn
ceTxSx02FiberLink = _CeTxSx02FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 35, 1, 3),
    _CeTxSx02FiberLink_Type()
)
ceTxSx02FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTxSx02FiberLink.setStatus("mandatory")


class _CeTxSx02100Mbps_Type(Integer32):
    """Custom type ceTxSx02100Mbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTxSx02100Mbps_Type.__name__ = "Integer32"
_CeTxSx02100Mbps_Object = MibTableColumn
ceTxSx02100Mbps = _CeTxSx02100Mbps_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 35, 1, 4),
    _CeTxSx02100Mbps_Type()
)
ceTxSx02100Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTxSx02100Mbps.setStatus("mandatory")
_CeTbtFrl04Table_Object = MibTable
ceTbtFrl04Table = _CeTbtFrl04Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 36)
)
if mibBuilder.loadTexts:
    ceTbtFrl04Table.setStatus("mandatory")
_CeTbtFrl04Entry_Object = MibTableRow
ceTbtFrl04Entry = _CeTbtFrl04Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 36, 1)
)
ceTbtFrl04Entry.setIndexNames(
    (0, "MCC16-MIB", "ceTbtFrl04Index"),
)
if mibBuilder.loadTexts:
    ceTbtFrl04Entry.setStatus("mandatory")
_CeTbtFrl04Index_Type = Integer32
_CeTbtFrl04Index_Object = MibTableColumn
ceTbtFrl04Index = _CeTbtFrl04Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 36, 1, 1),
    _CeTbtFrl04Index_Type()
)
ceTbtFrl04Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl04Index.setStatus("mandatory")


class _CeTbtFrl04FiberRecv_Type(Integer32):
    """Custom type ceTbtFrl04FiberRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTbtFrl04FiberRecv_Type.__name__ = "Integer32"
_CeTbtFrl04FiberRecv_Object = MibTableColumn
ceTbtFrl04FiberRecv = _CeTbtFrl04FiberRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 36, 1, 2),
    _CeTbtFrl04FiberRecv_Type()
)
ceTbtFrl04FiberRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl04FiberRecv.setStatus("mandatory")


class _CeTbtFrl04FiberLink_Type(Integer32):
    """Custom type ceTbtFrl04FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTbtFrl04FiberLink_Type.__name__ = "Integer32"
_CeTbtFrl04FiberLink_Object = MibTableColumn
ceTbtFrl04FiberLink = _CeTbtFrl04FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 36, 1, 3),
    _CeTbtFrl04FiberLink_Type()
)
ceTbtFrl04FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl04FiberLink.setStatus("mandatory")


class _CeTbtFrl04TPRecv_Type(Integer32):
    """Custom type ceTbtFrl04TPRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTbtFrl04TPRecv_Type.__name__ = "Integer32"
_CeTbtFrl04TPRecv_Object = MibTableColumn
ceTbtFrl04TPRecv = _CeTbtFrl04TPRecv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 36, 1, 4),
    _CeTbtFrl04TPRecv_Type()
)
ceTbtFrl04TPRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl04TPRecv.setStatus("mandatory")


class _CeTbtFrl04TPLink_Type(Integer32):
    """Custom type ceTbtFrl04TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CeTbtFrl04TPLink_Type.__name__ = "Integer32"
_CeTbtFrl04TPLink_Object = MibTableColumn
ceTbtFrl04TPLink = _CeTbtFrl04TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 1, 36, 1, 5),
    _CeTbtFrl04TPLink_Type()
)
ceTbtFrl04TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceTbtFrl04TPLink.setStatus("mandatory")
_SlotCps_ObjectIdentity = ObjectIdentity
slotCps = _SlotCps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2)
)
_CpsSlotSummary_ObjectIdentity = ObjectIdentity
cpsSlotSummary = _CpsSlotSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 1)
)
_CpsModuleTable_Object = MibTable
cpsModuleTable = _CpsModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpsModuleTable.setStatus("mandatory")
_CpsModuleEntry_Object = MibTableRow
cpsModuleEntry = _CpsModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 1, 1, 1)
)
cpsModuleEntry.setIndexNames(
    (0, "MCC16-MIB", "cpsModuleBiaIndex"),
    (0, "MCC16-MIB", "cpsModuleSlotIndex"),
)
if mibBuilder.loadTexts:
    cpsModuleEntry.setStatus("mandatory")
_CpsModuleBiaIndex_Type = Integer32
_CpsModuleBiaIndex_Object = MibTableColumn
cpsModuleBiaIndex = _CpsModuleBiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 1, 1, 1, 1),
    _CpsModuleBiaIndex_Type()
)
cpsModuleBiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsModuleBiaIndex.setStatus("mandatory")
_CpsModuleSlotIndex_Type = Integer32
_CpsModuleSlotIndex_Object = MibTableColumn
cpsModuleSlotIndex = _CpsModuleSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 1, 1, 1, 2),
    _CpsModuleSlotIndex_Type()
)
cpsModuleSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsModuleSlotIndex.setStatus("mandatory")
_CpsModuleModel_Type = ObjectIdentifier
_CpsModuleModel_Object = MibTableColumn
cpsModuleModel = _CpsModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 1, 1, 1, 3),
    _CpsModuleModel_Type()
)
cpsModuleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsModuleModel.setStatus("mandatory")
_CpsSlotDetail_ObjectIdentity = ObjectIdentity
cpsSlotDetail = _CpsSlotDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2)
)
_Cpsmm100Table_Object = MibTable
cpsmm100Table = _Cpsmm100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpsmm100Table.setStatus("mandatory")
_Cpsmm100Entry_Object = MibTableRow
cpsmm100Entry = _Cpsmm100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1)
)
cpsmm100Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsmm100BiaIndex"),
    (0, "MCC16-MIB", "cpsmm100SlotIndex"),
)
if mibBuilder.loadTexts:
    cpsmm100Entry.setStatus("mandatory")
_Cpsmm100BiaIndex_Type = Integer32
_Cpsmm100BiaIndex_Object = MibTableColumn
cpsmm100BiaIndex = _Cpsmm100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 1),
    _Cpsmm100BiaIndex_Type()
)
cpsmm100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100BiaIndex.setStatus("mandatory")
_Cpsmm100SlotIndex_Type = Integer32
_Cpsmm100SlotIndex_Object = MibTableColumn
cpsmm100SlotIndex = _Cpsmm100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 2),
    _Cpsmm100SlotIndex_Type()
)
cpsmm100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100SlotIndex.setStatus("mandatory")
_Cpsmm100Groups_Type = DisplayString
_Cpsmm100Groups_Object = MibTableColumn
cpsmm100Groups = _Cpsmm100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 3),
    _Cpsmm100Groups_Type()
)
cpsmm100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100Groups.setStatus("mandatory")


class _Cpsmm100Reset_Type(Integer32):
    """Custom type cpsmm100Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_Cpsmm100Reset_Type.__name__ = "Integer32"
_Cpsmm100Reset_Object = MibTableColumn
cpsmm100Reset = _Cpsmm100Reset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 4),
    _Cpsmm100Reset_Type()
)
cpsmm100Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100Reset.setStatus("mandatory")


class _Cpsmm100SaveConfig_Type(Integer32):
    """Custom type cpsmm100SaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSaveConfig", 2),
          ("saveConfig", 1))
    )


_Cpsmm100SaveConfig_Type.__name__ = "Integer32"
_Cpsmm100SaveConfig_Object = MibTableColumn
cpsmm100SaveConfig = _Cpsmm100SaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 5),
    _Cpsmm100SaveConfig_Type()
)
cpsmm100SaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100SaveConfig.setStatus("mandatory")
_Cpsmm100HwRevision_Type = DisplayString
_Cpsmm100HwRevision_Object = MibTableColumn
cpsmm100HwRevision = _Cpsmm100HwRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 6),
    _Cpsmm100HwRevision_Type()
)
cpsmm100HwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100HwRevision.setStatus("mandatory")
_Cpsmm100SwRevision_Type = DisplayString
_Cpsmm100SwRevision_Object = MibTableColumn
cpsmm100SwRevision = _Cpsmm100SwRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 7),
    _Cpsmm100SwRevision_Type()
)
cpsmm100SwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100SwRevision.setStatus("mandatory")
_Cpsmm100IPAddress_Type = IpAddress
_Cpsmm100IPAddress_Object = MibTableColumn
cpsmm100IPAddress = _Cpsmm100IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 8),
    _Cpsmm100IPAddress_Type()
)
cpsmm100IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100IPAddress.setStatus("mandatory")
_Cpsmm100SubnetMask_Type = IpAddress
_Cpsmm100SubnetMask_Object = MibTableColumn
cpsmm100SubnetMask = _Cpsmm100SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 9),
    _Cpsmm100SubnetMask_Type()
)
cpsmm100SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100SubnetMask.setStatus("mandatory")
_Cpsmm100Gateway_Type = IpAddress
_Cpsmm100Gateway_Object = MibTableColumn
cpsmm100Gateway = _Cpsmm100Gateway_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 10),
    _Cpsmm100Gateway_Type()
)
cpsmm100Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100Gateway.setStatus("mandatory")


class _Cpsmm100IsPrimary_Type(Integer32):
    """Custom type cpsmm100IsPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmm100IsPrimary_Type.__name__ = "Integer32"
_Cpsmm100IsPrimary_Object = MibTableColumn
cpsmm100IsPrimary = _Cpsmm100IsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 11),
    _Cpsmm100IsPrimary_Type()
)
cpsmm100IsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100IsPrimary.setStatus("mandatory")


class _Cpsmm100WantPrimary_Type(Integer32):
    """Custom type cpsmm100WantPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 3),
          ("no", 2),
          ("yes", 1))
    )


_Cpsmm100WantPrimary_Type.__name__ = "Integer32"
_Cpsmm100WantPrimary_Object = MibTableColumn
cpsmm100WantPrimary = _Cpsmm100WantPrimary_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 12),
    _Cpsmm100WantPrimary_Type()
)
cpsmm100WantPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100WantPrimary.setStatus("mandatory")


class _Cpsmm100CanPrimary_Type(Integer32):
    """Custom type cpsmm100CanPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmm100CanPrimary_Type.__name__ = "Integer32"
_Cpsmm100CanPrimary_Object = MibTableColumn
cpsmm100CanPrimary = _Cpsmm100CanPrimary_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 13),
    _Cpsmm100CanPrimary_Type()
)
cpsmm100CanPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100CanPrimary.setStatus("mandatory")


class _Cpsmm100EthernetLink_Type(Integer32):
    """Custom type cpsmm100EthernetLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Cpsmm100EthernetLink_Type.__name__ = "Integer32"
_Cpsmm100EthernetLink_Object = MibTableColumn
cpsmm100EthernetLink = _Cpsmm100EthernetLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 14),
    _Cpsmm100EthernetLink_Type()
)
cpsmm100EthernetLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100EthernetLink.setStatus("mandatory")
_Cpsmm100TntRIP_Type = IpAddress
_Cpsmm100TntRIP_Object = MibTableColumn
cpsmm100TntRIP = _Cpsmm100TntRIP_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 15),
    _Cpsmm100TntRIP_Type()
)
cpsmm100TntRIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100TntRIP.setStatus("mandatory")
_Cpsmm100TntRIPMask_Type = IpAddress
_Cpsmm100TntRIPMask_Object = MibTableColumn
cpsmm100TntRIPMask = _Cpsmm100TntRIPMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 16),
    _Cpsmm100TntRIPMask_Type()
)
cpsmm100TntRIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100TntRIPMask.setStatus("mandatory")
_Cpsmm100SNMPTrapMgr_Type = IpAddress
_Cpsmm100SNMPTrapMgr_Object = MibTableColumn
cpsmm100SNMPTrapMgr = _Cpsmm100SNMPTrapMgr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 17),
    _Cpsmm100SNMPTrapMgr_Type()
)
cpsmm100SNMPTrapMgr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100SNMPTrapMgr.setStatus("mandatory")
_Cpsmm100SNMPTrapInterval_Type = Integer32
_Cpsmm100SNMPTrapInterval_Object = MibTableColumn
cpsmm100SNMPTrapInterval = _Cpsmm100SNMPTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 18),
    _Cpsmm100SNMPTrapInterval_Type()
)
cpsmm100SNMPTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100SNMPTrapInterval.setStatus("mandatory")
_Cpsmm100SysUpTime_Type = TimeTicks
_Cpsmm100SysUpTime_Object = MibTableColumn
cpsmm100SysUpTime = _Cpsmm100SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 19),
    _Cpsmm100SysUpTime_Type()
)
cpsmm100SysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100SysUpTime.setStatus("mandatory")
_Cpsmm100SysContact_Type = DisplayString
_Cpsmm100SysContact_Object = MibTableColumn
cpsmm100SysContact = _Cpsmm100SysContact_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 20),
    _Cpsmm100SysContact_Type()
)
cpsmm100SysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100SysContact.setStatus("mandatory")
_Cpsmm100SysName_Type = DisplayString
_Cpsmm100SysName_Object = MibTableColumn
cpsmm100SysName = _Cpsmm100SysName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 21),
    _Cpsmm100SysName_Type()
)
cpsmm100SysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100SysName.setStatus("mandatory")
_Cpsmm100SysLocation_Type = DisplayString
_Cpsmm100SysLocation_Object = MibTableColumn
cpsmm100SysLocation = _Cpsmm100SysLocation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 22),
    _Cpsmm100SysLocation_Type()
)
cpsmm100SysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100SysLocation.setStatus("mandatory")


class _Cpsmm100CfgMatch_Type(Integer32):
    """Custom type cpsmm100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cpsmm100CfgMatch_Type.__name__ = "Integer32"
_Cpsmm100CfgMatch_Object = MibTableColumn
cpsmm100CfgMatch = _Cpsmm100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 23),
    _Cpsmm100CfgMatch_Type()
)
cpsmm100CfgMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100CfgMatch.setStatus("mandatory")
_Cpsmm100SerialNumber_Type = Integer32
_Cpsmm100SerialNumber_Object = MibTableColumn
cpsmm100SerialNumber = _Cpsmm100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 24),
    _Cpsmm100SerialNumber_Type()
)
cpsmm100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100SerialNumber.setStatus("mandatory")


class _Cpsmm100ICIF_Type(Integer32):
    """Custom type cpsmm100ICIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmm100ICIF_Type.__name__ = "Integer32"
_Cpsmm100ICIF_Object = MibTableColumn
cpsmm100ICIF = _Cpsmm100ICIF_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 25),
    _Cpsmm100ICIF_Type()
)
cpsmm100ICIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100ICIF.setStatus("mandatory")
_Cpsmm100MRevision_Type = Integer32
_Cpsmm100MRevision_Object = MibTableColumn
cpsmm100MRevision = _Cpsmm100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 26),
    _Cpsmm100MRevision_Type()
)
cpsmm100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100MRevision.setStatus("mandatory")


class _Cpsmm100LastGasp_Type(Integer32):
    """Custom type cpsmm100LastGasp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmm100LastGasp_Type.__name__ = "Integer32"
_Cpsmm100LastGasp_Object = MibTableColumn
cpsmm100LastGasp = _Cpsmm100LastGasp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 27),
    _Cpsmm100LastGasp_Type()
)
cpsmm100LastGasp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100LastGasp.setStatus("mandatory")
_Cpsmm100SNMPTrapMgr2_Type = IpAddress
_Cpsmm100SNMPTrapMgr2_Object = MibTableColumn
cpsmm100SNMPTrapMgr2 = _Cpsmm100SNMPTrapMgr2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 28),
    _Cpsmm100SNMPTrapMgr2_Type()
)
cpsmm100SNMPTrapMgr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100SNMPTrapMgr2.setStatus("mandatory")
_Cpsmm100SNMPTrapMgr3_Type = IpAddress
_Cpsmm100SNMPTrapMgr3_Object = MibTableColumn
cpsmm100SNMPTrapMgr3 = _Cpsmm100SNMPTrapMgr3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 29),
    _Cpsmm100SNMPTrapMgr3_Type()
)
cpsmm100SNMPTrapMgr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100SNMPTrapMgr3.setStatus("mandatory")
_Cpsmm100SNMPTrapMgr4_Type = IpAddress
_Cpsmm100SNMPTrapMgr4_Object = MibTableColumn
cpsmm100SNMPTrapMgr4 = _Cpsmm100SNMPTrapMgr4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 30),
    _Cpsmm100SNMPTrapMgr4_Type()
)
cpsmm100SNMPTrapMgr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmm100SNMPTrapMgr4.setStatus("mandatory")


class _Cpsmm100CacheClean_Type(Integer32):
    """Custom type cpsmm100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cpsmm100CacheClean_Type.__name__ = "Integer32"
_Cpsmm100CacheClean_Object = MibTableColumn
cpsmm100CacheClean = _Cpsmm100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 1, 1, 31),
    _Cpsmm100CacheClean_Type()
)
cpsmm100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm100CacheClean.setStatus("mandatory")
_Cpsmm200Table_Object = MibTable
cpsmm200Table = _Cpsmm200Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cpsmm200Table.setStatus("mandatory")
_Cpsmm200Entry_Object = MibTableRow
cpsmm200Entry = _Cpsmm200Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 2, 1)
)
cpsmm200Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsmm200BiaIndex"),
    (0, "MCC16-MIB", "cpsmm200SlotIndex"),
)
if mibBuilder.loadTexts:
    cpsmm200Entry.setStatus("mandatory")
_Cpsmm200BiaIndex_Type = Integer32
_Cpsmm200BiaIndex_Object = MibTableColumn
cpsmm200BiaIndex = _Cpsmm200BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 2, 1, 1),
    _Cpsmm200BiaIndex_Type()
)
cpsmm200BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm200BiaIndex.setStatus("mandatory")
_Cpsmm200SlotIndex_Type = Integer32
_Cpsmm200SlotIndex_Object = MibTableColumn
cpsmm200SlotIndex = _Cpsmm200SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 2, 1, 2),
    _Cpsmm200SlotIndex_Type()
)
cpsmm200SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm200SlotIndex.setStatus("mandatory")
_Cpsmm200SerialNumber_Type = Integer32
_Cpsmm200SerialNumber_Object = MibTableColumn
cpsmm200SerialNumber = _Cpsmm200SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 2, 1, 3),
    _Cpsmm200SerialNumber_Type()
)
cpsmm200SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm200SerialNumber.setStatus("mandatory")


class _Cpsmm200ICIF_Type(Integer32):
    """Custom type cpsmm200ICIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmm200ICIF_Type.__name__ = "Integer32"
_Cpsmm200ICIF_Object = MibTableColumn
cpsmm200ICIF = _Cpsmm200ICIF_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 2, 1, 4),
    _Cpsmm200ICIF_Type()
)
cpsmm200ICIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm200ICIF.setStatus("mandatory")
_Cpsmm200MRevision_Type = Integer32
_Cpsmm200MRevision_Object = MibTableColumn
cpsmm200MRevision = _Cpsmm200MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 2, 1, 5),
    _Cpsmm200MRevision_Type()
)
cpsmm200MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmm200MRevision.setStatus("mandatory")
_Cettf100Table_Object = MibTable
cettf100Table = _Cettf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cettf100Table.setStatus("mandatory")
_Cettf100Entry_Object = MibTableRow
cettf100Entry = _Cettf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1)
)
cettf100Entry.setIndexNames(
    (0, "MCC16-MIB", "cettf100BiaIndex"),
    (0, "MCC16-MIB", "cettf100SlotIndex"),
)
if mibBuilder.loadTexts:
    cettf100Entry.setStatus("mandatory")
_Cettf100BiaIndex_Type = Integer32
_Cettf100BiaIndex_Object = MibTableColumn
cettf100BiaIndex = _Cettf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 1),
    _Cettf100BiaIndex_Type()
)
cettf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100BiaIndex.setStatus("mandatory")
_Cettf100SlotIndex_Type = Integer32
_Cettf100SlotIndex_Object = MibTableColumn
cettf100SlotIndex = _Cettf100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 2),
    _Cettf100SlotIndex_Type()
)
cettf100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100SlotIndex.setStatus("mandatory")
_Cettf100Groups_Type = DisplayString
_Cettf100Groups_Object = MibTableColumn
cettf100Groups = _Cettf100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 3),
    _Cettf100Groups_Type()
)
cettf100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cettf100Groups.setStatus("mandatory")
_Cettf100MRevision_Type = Integer32
_Cettf100MRevision_Object = MibTableColumn
cettf100MRevision = _Cettf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 4),
    _Cettf100MRevision_Type()
)
cettf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100MRevision.setStatus("mandatory")


class _Cettf100CfgMatch_Type(Integer32):
    """Custom type cettf100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cettf100CfgMatch_Type.__name__ = "Integer32"
_Cettf100CfgMatch_Object = MibTableColumn
cettf100CfgMatch = _Cettf100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 5),
    _Cettf100CfgMatch_Type()
)
cettf100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100CfgMatch.setStatus("mandatory")
_Cettf100SerialNumber_Type = Integer32
_Cettf100SerialNumber_Object = MibTableColumn
cettf100SerialNumber = _Cettf100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 6),
    _Cettf100SerialNumber_Type()
)
cettf100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100SerialNumber.setStatus("mandatory")
_Cettf100ConnA_Type = CpsConnector
_Cettf100ConnA_Object = MibTableColumn
cettf100ConnA = _Cettf100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 7),
    _Cettf100ConnA_Type()
)
cettf100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100ConnA.setStatus("mandatory")
_Cettf100ConnB_Type = CpsConnector
_Cettf100ConnB_Object = MibTableColumn
cettf100ConnB = _Cettf100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 8),
    _Cettf100ConnB_Type()
)
cettf100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100ConnB.setStatus("mandatory")


class _Cettf100TPLink_Type(Integer32):
    """Custom type cettf100TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cettf100TPLink_Type.__name__ = "Integer32"
_Cettf100TPLink_Object = MibTableColumn
cettf100TPLink = _Cettf100TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 9),
    _Cettf100TPLink_Type()
)
cettf100TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100TPLink.setStatus("mandatory")


class _Cettf100FiberLink_Type(Integer32):
    """Custom type cettf100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cettf100FiberLink_Type.__name__ = "Integer32"
_Cettf100FiberLink_Object = MibTableColumn
cettf100FiberLink = _Cettf100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 10),
    _Cettf100FiberLink_Type()
)
cettf100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100FiberLink.setStatus("mandatory")


class _Cettf100Fault_Type(Integer32):
    """Custom type cettf100Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cettf100Fault_Type.__name__ = "Integer32"
_Cettf100Fault_Object = MibTableColumn
cettf100Fault = _Cettf100Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 11),
    _Cettf100Fault_Type()
)
cettf100Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100Fault.setStatus("mandatory")


class _Cettf100TPActivity_Type(Integer32):
    """Custom type cettf100TPActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cettf100TPActivity_Type.__name__ = "Integer32"
_Cettf100TPActivity_Object = MibTableColumn
cettf100TPActivity = _Cettf100TPActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 12),
    _Cettf100TPActivity_Type()
)
cettf100TPActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100TPActivity.setStatus("mandatory")


class _Cettf100FiberActivity_Type(Integer32):
    """Custom type cettf100FiberActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cettf100FiberActivity_Type.__name__ = "Integer32"
_Cettf100FiberActivity_Object = MibTableColumn
cettf100FiberActivity = _Cettf100FiberActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 13),
    _Cettf100FiberActivity_Type()
)
cettf100FiberActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100FiberActivity.setStatus("mandatory")


class _Cettf100AutoCross_Type(Integer32):
    """Custom type cettf100AutoCross based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Cettf100AutoCross_Type.__name__ = "Integer32"
_Cettf100AutoCross_Object = MibTableColumn
cettf100AutoCross = _Cettf100AutoCross_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 14),
    _Cettf100AutoCross_Type()
)
cettf100AutoCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cettf100AutoCross.setStatus("mandatory")


class _Cettf100LinkPassThrough_Type(Integer32):
    """Custom type cettf100LinkPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Cettf100LinkPassThrough_Type.__name__ = "Integer32"
_Cettf100LinkPassThrough_Object = MibTableColumn
cettf100LinkPassThrough = _Cettf100LinkPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 15),
    _Cettf100LinkPassThrough_Type()
)
cettf100LinkPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cettf100LinkPassThrough.setStatus("mandatory")


class _Cettf100ConfigMode_Type(Integer32):
    """Custom type cettf100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cettf100ConfigMode_Type.__name__ = "Integer32"
_Cettf100ConfigMode_Object = MibTableColumn
cettf100ConfigMode = _Cettf100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 16),
    _Cettf100ConfigMode_Type()
)
cettf100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100ConfigMode.setStatus("mandatory")


class _Cettf100Enabled_Type(Integer32):
    """Custom type cettf100Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cettf100Enabled_Type.__name__ = "Integer32"
_Cettf100Enabled_Object = MibTableColumn
cettf100Enabled = _Cettf100Enabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 17),
    _Cettf100Enabled_Type()
)
cettf100Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cettf100Enabled.setStatus("mandatory")


class _Cettf100CacheClean_Type(Integer32):
    """Custom type cettf100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cettf100CacheClean_Type.__name__ = "Integer32"
_Cettf100CacheClean_Object = MibTableColumn
cettf100CacheClean = _Cettf100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 3, 1, 18),
    _Cettf100CacheClean_Type()
)
cettf100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cettf100CacheClean.setStatus("mandatory")
_Cfetf100Table_Object = MibTable
cfetf100Table = _Cfetf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cfetf100Table.setStatus("mandatory")
_Cfetf100Entry_Object = MibTableRow
cfetf100Entry = _Cfetf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1)
)
cfetf100Entry.setIndexNames(
    (0, "MCC16-MIB", "cfetf100BiaIndex"),
    (0, "MCC16-MIB", "cfetf100SlotIndex"),
)
if mibBuilder.loadTexts:
    cfetf100Entry.setStatus("mandatory")
_Cfetf100BiaIndex_Type = Integer32
_Cfetf100BiaIndex_Object = MibTableColumn
cfetf100BiaIndex = _Cfetf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 1),
    _Cfetf100BiaIndex_Type()
)
cfetf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100BiaIndex.setStatus("mandatory")
_Cfetf100SlotIndex_Type = Integer32
_Cfetf100SlotIndex_Object = MibTableColumn
cfetf100SlotIndex = _Cfetf100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 2),
    _Cfetf100SlotIndex_Type()
)
cfetf100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100SlotIndex.setStatus("mandatory")
_Cfetf100Groups_Type = DisplayString
_Cfetf100Groups_Object = MibTableColumn
cfetf100Groups = _Cfetf100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 3),
    _Cfetf100Groups_Type()
)
cfetf100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf100Groups.setStatus("mandatory")
_Cfetf100MRevision_Type = Integer32
_Cfetf100MRevision_Object = MibTableColumn
cfetf100MRevision = _Cfetf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 4),
    _Cfetf100MRevision_Type()
)
cfetf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100MRevision.setStatus("mandatory")


class _Cfetf100CfgMatch_Type(Integer32):
    """Custom type cfetf100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cfetf100CfgMatch_Type.__name__ = "Integer32"
_Cfetf100CfgMatch_Object = MibTableColumn
cfetf100CfgMatch = _Cfetf100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 5),
    _Cfetf100CfgMatch_Type()
)
cfetf100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100CfgMatch.setStatus("mandatory")
_Cfetf100SerialNumber_Type = Integer32
_Cfetf100SerialNumber_Object = MibTableColumn
cfetf100SerialNumber = _Cfetf100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 6),
    _Cfetf100SerialNumber_Type()
)
cfetf100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100SerialNumber.setStatus("mandatory")
_Cfetf100ConnA_Type = CpsConnector
_Cfetf100ConnA_Object = MibTableColumn
cfetf100ConnA = _Cfetf100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 7),
    _Cfetf100ConnA_Type()
)
cfetf100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100ConnA.setStatus("mandatory")
_Cfetf100ConnB_Type = CpsConnector
_Cfetf100ConnB_Object = MibTableColumn
cfetf100ConnB = _Cfetf100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 8),
    _Cfetf100ConnB_Type()
)
cfetf100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100ConnB.setStatus("mandatory")


class _Cfetf100TPLink_Type(Integer32):
    """Custom type cfetf100TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cfetf100TPLink_Type.__name__ = "Integer32"
_Cfetf100TPLink_Object = MibTableColumn
cfetf100TPLink = _Cfetf100TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 9),
    _Cfetf100TPLink_Type()
)
cfetf100TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100TPLink.setStatus("mandatory")


class _Cfetf100FiberLink_Type(Integer32):
    """Custom type cfetf100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cfetf100FiberLink_Type.__name__ = "Integer32"
_Cfetf100FiberLink_Object = MibTableColumn
cfetf100FiberLink = _Cfetf100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 10),
    _Cfetf100FiberLink_Type()
)
cfetf100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100FiberLink.setStatus("mandatory")


class _Cfetf100Fault_Type(Integer32):
    """Custom type cfetf100Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cfetf100Fault_Type.__name__ = "Integer32"
_Cfetf100Fault_Object = MibTableColumn
cfetf100Fault = _Cfetf100Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 11),
    _Cfetf100Fault_Type()
)
cfetf100Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100Fault.setStatus("mandatory")


class _Cfetf100FastLinkPulse_Type(Integer32):
    """Custom type cfetf100FastLinkPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autonegotiate", 1),
          ("hdx100Btx", 2))
    )


_Cfetf100FastLinkPulse_Type.__name__ = "Integer32"
_Cfetf100FastLinkPulse_Object = MibTableColumn
cfetf100FastLinkPulse = _Cfetf100FastLinkPulse_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 12),
    _Cfetf100FastLinkPulse_Type()
)
cfetf100FastLinkPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf100FastLinkPulse.setStatus("mandatory")


class _Cfetf100Enabled_Type(Integer32):
    """Custom type cfetf100Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cfetf100Enabled_Type.__name__ = "Integer32"
_Cfetf100Enabled_Object = MibTableColumn
cfetf100Enabled = _Cfetf100Enabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 13),
    _Cfetf100Enabled_Type()
)
cfetf100Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf100Enabled.setStatus("mandatory")


class _Cfetf100Pause_Type(Integer32):
    """Custom type cfetf100Pause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cfetf100Pause_Type.__name__ = "Integer32"
_Cfetf100Pause_Object = MibTableColumn
cfetf100Pause = _Cfetf100Pause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 14),
    _Cfetf100Pause_Type()
)
cfetf100Pause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf100Pause.setStatus("mandatory")


class _Cfetf100LinkPassThrough_Type(Integer32):
    """Custom type cfetf100LinkPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cfetf100LinkPassThrough_Type.__name__ = "Integer32"
_Cfetf100LinkPassThrough_Object = MibTableColumn
cfetf100LinkPassThrough = _Cfetf100LinkPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 15),
    _Cfetf100LinkPassThrough_Type()
)
cfetf100LinkPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf100LinkPassThrough.setStatus("mandatory")


class _Cfetf100AutoCross_Type(Integer32):
    """Custom type cfetf100AutoCross based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cfetf100AutoCross_Type.__name__ = "Integer32"
_Cfetf100AutoCross_Object = MibTableColumn
cfetf100AutoCross = _Cfetf100AutoCross_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 16),
    _Cfetf100AutoCross_Type()
)
cfetf100AutoCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf100AutoCross.setStatus("mandatory")


class _Cfetf100TPActivity_Type(Integer32):
    """Custom type cfetf100TPActivity based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Cfetf100TPActivity_Type.__name__ = "Integer32"
_Cfetf100TPActivity_Object = MibTableColumn
cfetf100TPActivity = _Cfetf100TPActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 17),
    _Cfetf100TPActivity_Type()
)
cfetf100TPActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100TPActivity.setStatus("mandatory")


class _Cfetf100FiberActivity_Type(Integer32):
    """Custom type cfetf100FiberActivity based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Cfetf100FiberActivity_Type.__name__ = "Integer32"
_Cfetf100FiberActivity_Object = MibTableColumn
cfetf100FiberActivity = _Cfetf100FiberActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 18),
    _Cfetf100FiberActivity_Type()
)
cfetf100FiberActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100FiberActivity.setStatus("mandatory")


class _Cfetf100ConfigMode_Type(Integer32):
    """Custom type cfetf100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cfetf100ConfigMode_Type.__name__ = "Integer32"
_Cfetf100ConfigMode_Object = MibTableColumn
cfetf100ConfigMode = _Cfetf100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 19),
    _Cfetf100ConfigMode_Type()
)
cfetf100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100ConfigMode.setStatus("mandatory")


class _Cfetf100FarEndFault_Type(Integer32):
    """Custom type cfetf100FarEndFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cfetf100FarEndFault_Type.__name__ = "Integer32"
_Cfetf100FarEndFault_Object = MibTableColumn
cfetf100FarEndFault = _Cfetf100FarEndFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 20),
    _Cfetf100FarEndFault_Type()
)
cfetf100FarEndFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf100FarEndFault.setStatus("mandatory")


class _Cfetf100CacheClean_Type(Integer32):
    """Custom type cfetf100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cfetf100CacheClean_Type.__name__ = "Integer32"
_Cfetf100CacheClean_Object = MibTableColumn
cfetf100CacheClean = _Cfetf100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 4, 1, 21),
    _Cfetf100CacheClean_Type()
)
cfetf100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf100CacheClean.setStatus("mandatory")
_Cfmff100Table_Object = MibTable
cfmff100Table = _Cfmff100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cfmff100Table.setStatus("mandatory")
_Cfmff100Entry_Object = MibTableRow
cfmff100Entry = _Cfmff100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1)
)
cfmff100Entry.setIndexNames(
    (0, "MCC16-MIB", "cfmff100BiaIndex"),
    (0, "MCC16-MIB", "cfmff100SlotIndex"),
)
if mibBuilder.loadTexts:
    cfmff100Entry.setStatus("mandatory")
_Cfmff100BiaIndex_Type = Integer32
_Cfmff100BiaIndex_Object = MibTableColumn
cfmff100BiaIndex = _Cfmff100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 1),
    _Cfmff100BiaIndex_Type()
)
cfmff100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100BiaIndex.setStatus("mandatory")
_Cfmff100SlotIndex_Type = Integer32
_Cfmff100SlotIndex_Object = MibTableColumn
cfmff100SlotIndex = _Cfmff100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 2),
    _Cfmff100SlotIndex_Type()
)
cfmff100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100SlotIndex.setStatus("mandatory")
_Cfmff100Groups_Type = DisplayString
_Cfmff100Groups_Object = MibTableColumn
cfmff100Groups = _Cfmff100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 3),
    _Cfmff100Groups_Type()
)
cfmff100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmff100Groups.setStatus("mandatory")
_Cfmff100MRevision_Type = Integer32
_Cfmff100MRevision_Object = MibTableColumn
cfmff100MRevision = _Cfmff100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 4),
    _Cfmff100MRevision_Type()
)
cfmff100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100MRevision.setStatus("mandatory")


class _Cfmff100CfgMatch_Type(Integer32):
    """Custom type cfmff100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cfmff100CfgMatch_Type.__name__ = "Integer32"
_Cfmff100CfgMatch_Object = MibTableColumn
cfmff100CfgMatch = _Cfmff100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 5),
    _Cfmff100CfgMatch_Type()
)
cfmff100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100CfgMatch.setStatus("mandatory")
_Cfmff100ConnA_Type = CpsConnector
_Cfmff100ConnA_Object = MibTableColumn
cfmff100ConnA = _Cfmff100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 6),
    _Cfmff100ConnA_Type()
)
cfmff100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100ConnA.setStatus("mandatory")
_Cfmff100ConnB_Type = CpsConnector
_Cfmff100ConnB_Object = MibTableColumn
cfmff100ConnB = _Cfmff100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 7),
    _Cfmff100ConnB_Type()
)
cfmff100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100ConnB.setStatus("mandatory")
_Cfmff100SerialNumber_Type = Integer32
_Cfmff100SerialNumber_Object = MibTableColumn
cfmff100SerialNumber = _Cfmff100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 8),
    _Cfmff100SerialNumber_Type()
)
cfmff100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100SerialNumber.setStatus("mandatory")


class _Cfmff100SMSignal_Type(Integer32):
    """Custom type cfmff100SMSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signalDown", 2),
          ("signalUp", 1))
    )


_Cfmff100SMSignal_Type.__name__ = "Integer32"
_Cfmff100SMSignal_Object = MibTableColumn
cfmff100SMSignal = _Cfmff100SMSignal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 9),
    _Cfmff100SMSignal_Type()
)
cfmff100SMSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100SMSignal.setStatus("mandatory")


class _Cfmff100MMSignal_Type(Integer32):
    """Custom type cfmff100MMSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signalDown", 2),
          ("signalUp", 1))
    )


_Cfmff100MMSignal_Type.__name__ = "Integer32"
_Cfmff100MMSignal_Object = MibTableColumn
cfmff100MMSignal = _Cfmff100MMSignal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 10),
    _Cfmff100MMSignal_Type()
)
cfmff100MMSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100MMSignal.setStatus("mandatory")


class _Cfmff100Enabled_Type(Integer32):
    """Custom type cfmff100Enabled based on Integer32"""
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
        *(("no", 4),
          ("noP1", 2),
          ("noP2", 3),
          ("yes", 1))
    )


_Cfmff100Enabled_Type.__name__ = "Integer32"
_Cfmff100Enabled_Object = MibTableColumn
cfmff100Enabled = _Cfmff100Enabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 11),
    _Cfmff100Enabled_Type()
)
cfmff100Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmff100Enabled.setStatus("mandatory")


class _Cfmff100PortShutOff_Type(Integer32):
    """Custom type cfmff100PortShutOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cfmff100PortShutOff_Type.__name__ = "Integer32"
_Cfmff100PortShutOff_Object = MibTableColumn
cfmff100PortShutOff = _Cfmff100PortShutOff_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 12),
    _Cfmff100PortShutOff_Type()
)
cfmff100PortShutOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100PortShutOff.setStatus("mandatory")


class _Cfmff100ConfigMode_Type(Integer32):
    """Custom type cfmff100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cfmff100ConfigMode_Type.__name__ = "Integer32"
_Cfmff100ConfigMode_Object = MibTableColumn
cfmff100ConfigMode = _Cfmff100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 13),
    _Cfmff100ConfigMode_Type()
)
cfmff100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100ConfigMode.setStatus("mandatory")


class _Cfmff100CacheClean_Type(Integer32):
    """Custom type cfmff100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cfmff100CacheClean_Type.__name__ = "Integer32"
_Cfmff100CacheClean_Object = MibTableColumn
cfmff100CacheClean = _Cfmff100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 5, 1, 14),
    _Cfmff100CacheClean_Type()
)
cfmff100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmff100CacheClean.setStatus("mandatory")
_Cpsmp100Table_Object = MibTable
cpsmp100Table = _Cpsmp100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    cpsmp100Table.setStatus("mandatory")
_Cpsmp100Entry_Object = MibTableRow
cpsmp100Entry = _Cpsmp100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1)
)
cpsmp100Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsmp100BiaIndex"),
    (0, "MCC16-MIB", "cpsmp100SlotIndex"),
)
if mibBuilder.loadTexts:
    cpsmp100Entry.setStatus("mandatory")
_Cpsmp100BiaIndex_Type = Integer32
_Cpsmp100BiaIndex_Object = MibTableColumn
cpsmp100BiaIndex = _Cpsmp100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 1),
    _Cpsmp100BiaIndex_Type()
)
cpsmp100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100BiaIndex.setStatus("mandatory")
_Cpsmp100SlotIndex_Type = Integer32
_Cpsmp100SlotIndex_Object = MibTableColumn
cpsmp100SlotIndex = _Cpsmp100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 2),
    _Cpsmp100SlotIndex_Type()
)
cpsmp100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100SlotIndex.setStatus("mandatory")
_Cpsmp100Groups_Type = DisplayString
_Cpsmp100Groups_Object = MibTableColumn
cpsmp100Groups = _Cpsmp100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 3),
    _Cpsmp100Groups_Type()
)
cpsmp100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmp100Groups.setStatus("mandatory")
_Cpsmp100MRevision_Type = Integer32
_Cpsmp100MRevision_Object = MibTableColumn
cpsmp100MRevision = _Cpsmp100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 4),
    _Cpsmp100MRevision_Type()
)
cpsmp100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100MRevision.setStatus("mandatory")


class _Cpsmp100CfgMatch_Type(Integer32):
    """Custom type cpsmp100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cpsmp100CfgMatch_Type.__name__ = "Integer32"
_Cpsmp100CfgMatch_Object = MibTableColumn
cpsmp100CfgMatch = _Cpsmp100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 5),
    _Cpsmp100CfgMatch_Type()
)
cpsmp100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100CfgMatch.setStatus("mandatory")
_Cpsmp100SerialNumber_Type = Integer32
_Cpsmp100SerialNumber_Object = MibTableColumn
cpsmp100SerialNumber = _Cpsmp100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 6),
    _Cpsmp100SerialNumber_Type()
)
cpsmp100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100SerialNumber.setStatus("mandatory")


class _Cpsmp100Mode_Type(Integer32):
    """Custom type cpsmp100Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_Cpsmp100Mode_Type.__name__ = "Integer32"
_Cpsmp100Mode_Object = MibTableColumn
cpsmp100Mode = _Cpsmp100Mode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 7),
    _Cpsmp100Mode_Type()
)
cpsmp100Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmp100Mode.setStatus("mandatory")


class _Cpsmp100ConfigMode_Type(Integer32):
    """Custom type cpsmp100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cpsmp100ConfigMode_Type.__name__ = "Integer32"
_Cpsmp100ConfigMode_Object = MibTableColumn
cpsmp100ConfigMode = _Cpsmp100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 8),
    _Cpsmp100ConfigMode_Type()
)
cpsmp100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100ConfigMode.setStatus("mandatory")


class _Cpsmp100RemoteFan_Type(Integer32):
    """Custom type cpsmp100RemoteFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Cpsmp100RemoteFan_Type.__name__ = "Integer32"
_Cpsmp100RemoteFan_Object = MibTableColumn
cpsmp100RemoteFan = _Cpsmp100RemoteFan_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 9),
    _Cpsmp100RemoteFan_Type()
)
cpsmp100RemoteFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100RemoteFan.setStatus("mandatory")


class _Cpsmp100PowerOK_Type(Integer32):
    """Custom type cpsmp100PowerOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp100PowerOK_Type.__name__ = "Integer32"
_Cpsmp100PowerOK_Object = MibTableColumn
cpsmp100PowerOK = _Cpsmp100PowerOK_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 10),
    _Cpsmp100PowerOK_Type()
)
cpsmp100PowerOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100PowerOK.setStatus("mandatory")


class _Cpsmp100InUse_Type(Integer32):
    """Custom type cpsmp100InUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp100InUse_Type.__name__ = "Integer32"
_Cpsmp100InUse_Object = MibTableColumn
cpsmp100InUse = _Cpsmp100InUse_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 11),
    _Cpsmp100InUse_Type()
)
cpsmp100InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100InUse.setStatus("mandatory")
_Cpsmp100ChassisPower_Type = Integer32
_Cpsmp100ChassisPower_Object = MibTableColumn
cpsmp100ChassisPower = _Cpsmp100ChassisPower_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 12),
    _Cpsmp100ChassisPower_Type()
)
cpsmp100ChassisPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100ChassisPower.setStatus("mandatory")
_Cpsmp100ChassisTemp_Type = Integer32
_Cpsmp100ChassisTemp_Object = MibTableColumn
cpsmp100ChassisTemp = _Cpsmp100ChassisTemp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 13),
    _Cpsmp100ChassisTemp_Type()
)
cpsmp100ChassisTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100ChassisTemp.setStatus("mandatory")


class _Cpsmp100RFanFault_Type(Integer32):
    """Custom type cpsmp100RFanFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp100RFanFault_Type.__name__ = "Integer32"
_Cpsmp100RFanFault_Object = MibTableColumn
cpsmp100RFanFault = _Cpsmp100RFanFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 14),
    _Cpsmp100RFanFault_Type()
)
cpsmp100RFanFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100RFanFault.setStatus("mandatory")


class _Cpsmp100LFanFault_Type(Integer32):
    """Custom type cpsmp100LFanFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp100LFanFault_Type.__name__ = "Integer32"
_Cpsmp100LFanFault_Object = MibTableColumn
cpsmp100LFanFault = _Cpsmp100LFanFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 15),
    _Cpsmp100LFanFault_Type()
)
cpsmp100LFanFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100LFanFault.setStatus("mandatory")


class _Cpsmp100SupplyType_Type(Integer32):
    """Custom type cpsmp100SupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc48", 2))
    )


_Cpsmp100SupplyType_Type.__name__ = "Integer32"
_Cpsmp100SupplyType_Object = MibTableColumn
cpsmp100SupplyType = _Cpsmp100SupplyType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 16),
    _Cpsmp100SupplyType_Type()
)
cpsmp100SupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100SupplyType.setStatus("mandatory")


class _Cpsmp100CacheClean_Type(Integer32):
    """Custom type cpsmp100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cpsmp100CacheClean_Type.__name__ = "Integer32"
_Cpsmp100CacheClean_Object = MibTableColumn
cpsmp100CacheClean = _Cpsmp100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 6, 1, 17),
    _Cpsmp100CacheClean_Type()
)
cpsmp100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp100CacheClean.setStatus("mandatory")
_Csetf100Table_Object = MibTable
csetf100Table = _Csetf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    csetf100Table.setStatus("mandatory")
_Csetf100Entry_Object = MibTableRow
csetf100Entry = _Csetf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1)
)
csetf100Entry.setIndexNames(
    (0, "MCC16-MIB", "csetf100BiaIndex"),
    (0, "MCC16-MIB", "csetf100SlotIndex"),
)
if mibBuilder.loadTexts:
    csetf100Entry.setStatus("mandatory")
_Csetf100BiaIndex_Type = Integer32
_Csetf100BiaIndex_Object = MibTableColumn
csetf100BiaIndex = _Csetf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 1),
    _Csetf100BiaIndex_Type()
)
csetf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100BiaIndex.setStatus("mandatory")
_Csetf100SlotIndex_Type = Integer32
_Csetf100SlotIndex_Object = MibTableColumn
csetf100SlotIndex = _Csetf100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 2),
    _Csetf100SlotIndex_Type()
)
csetf100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100SlotIndex.setStatus("mandatory")
_Csetf100Groups_Type = DisplayString
_Csetf100Groups_Object = MibTableColumn
csetf100Groups = _Csetf100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 3),
    _Csetf100Groups_Type()
)
csetf100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csetf100Groups.setStatus("mandatory")
_Csetf100MRevision_Type = Integer32
_Csetf100MRevision_Object = MibTableColumn
csetf100MRevision = _Csetf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 4),
    _Csetf100MRevision_Type()
)
csetf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100MRevision.setStatus("mandatory")


class _Csetf100CfgMatch_Type(Integer32):
    """Custom type csetf100CfgMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 3),
          ("no", 2),
          ("yes", 1))
    )


_Csetf100CfgMatch_Type.__name__ = "Integer32"
_Csetf100CfgMatch_Object = MibTableColumn
csetf100CfgMatch = _Csetf100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 5),
    _Csetf100CfgMatch_Type()
)
csetf100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100CfgMatch.setStatus("mandatory")
_Csetf100SerialNumber_Type = Integer32
_Csetf100SerialNumber_Object = MibTableColumn
csetf100SerialNumber = _Csetf100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 6),
    _Csetf100SerialNumber_Type()
)
csetf100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100SerialNumber.setStatus("mandatory")
_Csetf100ConnA_Type = CpsConnector
_Csetf100ConnA_Object = MibTableColumn
csetf100ConnA = _Csetf100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 7),
    _Csetf100ConnA_Type()
)
csetf100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100ConnA.setStatus("mandatory")
_Csetf100ConnB_Type = CpsConnector
_Csetf100ConnB_Object = MibTableColumn
csetf100ConnB = _Csetf100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 8),
    _Csetf100ConnB_Type()
)
csetf100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100ConnB.setStatus("mandatory")


class _Csetf100TPLink_Type(Integer32):
    """Custom type csetf100TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Csetf100TPLink_Type.__name__ = "Integer32"
_Csetf100TPLink_Object = MibTableColumn
csetf100TPLink = _Csetf100TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 9),
    _Csetf100TPLink_Type()
)
csetf100TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100TPLink.setStatus("mandatory")


class _Csetf100FiberLink_Type(Integer32):
    """Custom type csetf100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Csetf100FiberLink_Type.__name__ = "Integer32"
_Csetf100FiberLink_Object = MibTableColumn
csetf100FiberLink = _Csetf100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 10),
    _Csetf100FiberLink_Type()
)
csetf100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100FiberLink.setStatus("mandatory")


class _Csetf100AutoCross_Type(Integer32):
    """Custom type csetf100AutoCross based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Csetf100AutoCross_Type.__name__ = "Integer32"
_Csetf100AutoCross_Object = MibTableColumn
csetf100AutoCross = _Csetf100AutoCross_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 11),
    _Csetf100AutoCross_Type()
)
csetf100AutoCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csetf100AutoCross.setStatus("mandatory")


class _Csetf100SpeedConfig_Type(Integer32):
    """Custom type csetf100SpeedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mbps10", 2),
          ("mbps100", 3))
    )


_Csetf100SpeedConfig_Type.__name__ = "Integer32"
_Csetf100SpeedConfig_Object = MibTableColumn
csetf100SpeedConfig = _Csetf100SpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 12),
    _Csetf100SpeedConfig_Type()
)
csetf100SpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csetf100SpeedConfig.setStatus("mandatory")


class _Csetf100Speed100Mbps_Type(Integer32):
    """Custom type csetf100Speed100Mbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Csetf100Speed100Mbps_Type.__name__ = "Integer32"
_Csetf100Speed100Mbps_Object = MibTableColumn
csetf100Speed100Mbps = _Csetf100Speed100Mbps_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 13),
    _Csetf100Speed100Mbps_Type()
)
csetf100Speed100Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100Speed100Mbps.setStatus("mandatory")


class _Csetf100TPActivity_Type(Integer32):
    """Custom type csetf100TPActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activity", 1),
          ("noActivity", 2))
    )


_Csetf100TPActivity_Type.__name__ = "Integer32"
_Csetf100TPActivity_Object = MibTableColumn
csetf100TPActivity = _Csetf100TPActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 14),
    _Csetf100TPActivity_Type()
)
csetf100TPActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100TPActivity.setStatus("mandatory")


class _Csetf100FiberActivity_Type(Integer32):
    """Custom type csetf100FiberActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activity", 1),
          ("noActivity", 2))
    )


_Csetf100FiberActivity_Type.__name__ = "Integer32"
_Csetf100FiberActivity_Object = MibTableColumn
csetf100FiberActivity = _Csetf100FiberActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 15),
    _Csetf100FiberActivity_Type()
)
csetf100FiberActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100FiberActivity.setStatus("mandatory")


class _Csetf100ConfigMode_Type(Integer32):
    """Custom type csetf100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Csetf100ConfigMode_Type.__name__ = "Integer32"
_Csetf100ConfigMode_Object = MibTableColumn
csetf100ConfigMode = _Csetf100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 16),
    _Csetf100ConfigMode_Type()
)
csetf100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100ConfigMode.setStatus("mandatory")


class _Csetf100CacheClean_Type(Integer32):
    """Custom type csetf100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Csetf100CacheClean_Type.__name__ = "Integer32"
_Csetf100CacheClean_Object = MibTableColumn
csetf100CacheClean = _Csetf100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 7, 1, 17),
    _Csetf100CacheClean_Type()
)
csetf100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csetf100CacheClean.setStatus("mandatory")
_Cgetf100Table_Object = MibTable
cgetf100Table = _Cgetf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    cgetf100Table.setStatus("mandatory")
_Cgetf100Entry_Object = MibTableRow
cgetf100Entry = _Cgetf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1)
)
cgetf100Entry.setIndexNames(
    (0, "MCC16-MIB", "cgetf100BiaIndex"),
    (0, "MCC16-MIB", "cgetf100SlotIndex"),
)
if mibBuilder.loadTexts:
    cgetf100Entry.setStatus("mandatory")
_Cgetf100BiaIndex_Type = Integer32
_Cgetf100BiaIndex_Object = MibTableColumn
cgetf100BiaIndex = _Cgetf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 1),
    _Cgetf100BiaIndex_Type()
)
cgetf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100BiaIndex.setStatus("mandatory")
_Cgetf100SlotIndex_Type = Integer32
_Cgetf100SlotIndex_Object = MibTableColumn
cgetf100SlotIndex = _Cgetf100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 2),
    _Cgetf100SlotIndex_Type()
)
cgetf100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100SlotIndex.setStatus("mandatory")
_Cgetf100Groups_Type = DisplayString
_Cgetf100Groups_Object = MibTableColumn
cgetf100Groups = _Cgetf100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 3),
    _Cgetf100Groups_Type()
)
cgetf100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgetf100Groups.setStatus("mandatory")
_Cgetf100MRevision_Type = Integer32
_Cgetf100MRevision_Object = MibTableColumn
cgetf100MRevision = _Cgetf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 4),
    _Cgetf100MRevision_Type()
)
cgetf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100MRevision.setStatus("mandatory")


class _Cgetf100CfgMatch_Type(Integer32):
    """Custom type cgetf100CfgMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 3),
          ("no", 2),
          ("yes", 1))
    )


_Cgetf100CfgMatch_Type.__name__ = "Integer32"
_Cgetf100CfgMatch_Object = MibTableColumn
cgetf100CfgMatch = _Cgetf100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 5),
    _Cgetf100CfgMatch_Type()
)
cgetf100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100CfgMatch.setStatus("mandatory")
_Cgetf100SerialNumber_Type = Integer32
_Cgetf100SerialNumber_Object = MibTableColumn
cgetf100SerialNumber = _Cgetf100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 6),
    _Cgetf100SerialNumber_Type()
)
cgetf100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100SerialNumber.setStatus("mandatory")
_Cgetf100ConnA_Type = CpsConnector
_Cgetf100ConnA_Object = MibTableColumn
cgetf100ConnA = _Cgetf100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 7),
    _Cgetf100ConnA_Type()
)
cgetf100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100ConnA.setStatus("mandatory")
_Cgetf100ConnB_Type = CpsConnector
_Cgetf100ConnB_Object = MibTableColumn
cgetf100ConnB = _Cgetf100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 8),
    _Cgetf100ConnB_Type()
)
cgetf100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100ConnB.setStatus("mandatory")


class _Cgetf100TPLink_Type(Integer32):
    """Custom type cgetf100TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cgetf100TPLink_Type.__name__ = "Integer32"
_Cgetf100TPLink_Object = MibTableColumn
cgetf100TPLink = _Cgetf100TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 9),
    _Cgetf100TPLink_Type()
)
cgetf100TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100TPLink.setStatus("mandatory")


class _Cgetf100FiberLink_Type(Integer32):
    """Custom type cgetf100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cgetf100FiberLink_Type.__name__ = "Integer32"
_Cgetf100FiberLink_Object = MibTableColumn
cgetf100FiberLink = _Cgetf100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 10),
    _Cgetf100FiberLink_Type()
)
cgetf100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100FiberLink.setStatus("mandatory")


class _Cgetf100Fault_Type(Integer32):
    """Custom type cgetf100Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cgetf100Fault_Type.__name__ = "Integer32"
_Cgetf100Fault_Object = MibTableColumn
cgetf100Fault = _Cgetf100Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 11),
    _Cgetf100Fault_Type()
)
cgetf100Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100Fault.setStatus("mandatory")


class _Cgetf100Enabled_Type(Integer32):
    """Custom type cgetf100Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cgetf100Enabled_Type.__name__ = "Integer32"
_Cgetf100Enabled_Object = MibTableColumn
cgetf100Enabled = _Cgetf100Enabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 12),
    _Cgetf100Enabled_Type()
)
cgetf100Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgetf100Enabled.setStatus("mandatory")


class _Cgetf100Pause_Type(Integer32):
    """Custom type cgetf100Pause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cgetf100Pause_Type.__name__ = "Integer32"
_Cgetf100Pause_Object = MibTableColumn
cgetf100Pause = _Cgetf100Pause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 13),
    _Cgetf100Pause_Type()
)
cgetf100Pause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgetf100Pause.setStatus("mandatory")


class _Cgetf100LinkPassThrough_Type(Integer32):
    """Custom type cgetf100LinkPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cgetf100LinkPassThrough_Type.__name__ = "Integer32"
_Cgetf100LinkPassThrough_Object = MibTableColumn
cgetf100LinkPassThrough = _Cgetf100LinkPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 14),
    _Cgetf100LinkPassThrough_Type()
)
cgetf100LinkPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgetf100LinkPassThrough.setStatus("mandatory")


class _Cgetf100FullDuplex_Type(Integer32):
    """Custom type cgetf100FullDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_Cgetf100FullDuplex_Type.__name__ = "Integer32"
_Cgetf100FullDuplex_Object = MibTableColumn
cgetf100FullDuplex = _Cgetf100FullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 15),
    _Cgetf100FullDuplex_Type()
)
cgetf100FullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgetf100FullDuplex.setStatus("mandatory")


class _Cgetf100ClockMaster_Type(Integer32):
    """Custom type cgetf100ClockMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cgetf100ClockMaster_Type.__name__ = "Integer32"
_Cgetf100ClockMaster_Object = MibTableColumn
cgetf100ClockMaster = _Cgetf100ClockMaster_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 16),
    _Cgetf100ClockMaster_Type()
)
cgetf100ClockMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100ClockMaster.setStatus("mandatory")


class _Cgetf100ConfigMode_Type(Integer32):
    """Custom type cgetf100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cgetf100ConfigMode_Type.__name__ = "Integer32"
_Cgetf100ConfigMode_Object = MibTableColumn
cgetf100ConfigMode = _Cgetf100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 17),
    _Cgetf100ConfigMode_Type()
)
cgetf100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100ConfigMode.setStatus("mandatory")


class _Cgetf100TPLength_Type(Integer32):
    """Custom type cgetf100TPLength based on Integer32"""
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
        *(("ln-110-140", 4),
          ("ln-50-80", 2),
          ("ln-80-110", 3),
          ("ln-gt140", 5),
          ("ln-lt50", 1))
    )


_Cgetf100TPLength_Type.__name__ = "Integer32"
_Cgetf100TPLength_Object = MibTableColumn
cgetf100TPLength = _Cgetf100TPLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 18),
    _Cgetf100TPLength_Type()
)
cgetf100TPLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100TPLength.setStatus("mandatory")


class _Cgetf100FiberAutoNegot_Type(Integer32):
    """Custom type cgetf100FiberAutoNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cgetf100FiberAutoNegot_Type.__name__ = "Integer32"
_Cgetf100FiberAutoNegot_Object = MibTableColumn
cgetf100FiberAutoNegot = _Cgetf100FiberAutoNegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 19),
    _Cgetf100FiberAutoNegot_Type()
)
cgetf100FiberAutoNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgetf100FiberAutoNegot.setStatus("mandatory")


class _Cgetf100CacheClean_Type(Integer32):
    """Custom type cgetf100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cgetf100CacheClean_Type.__name__ = "Integer32"
_Cgetf100CacheClean_Object = MibTableColumn
cgetf100CacheClean = _Cgetf100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 20),
    _Cgetf100CacheClean_Type()
)
cgetf100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgetf100CacheClean.setStatus("mandatory")


class _Cgetf100PauseType_Type(Integer32):
    """Custom type cgetf100PauseType based on Integer32"""
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
        *(("all", 10),
          ("asymRX", 2),
          ("asymRXRO", 7),
          ("asymTX", 3),
          ("asymTXRO", 8),
          ("disabled", 4),
          ("disabledRO", 9),
          ("notApplicable", 5),
          ("symmetric", 1),
          ("symmetricRO", 6))
    )


_Cgetf100PauseType_Type.__name__ = "Integer32"
_Cgetf100PauseType_Object = MibTableColumn
cgetf100PauseType = _Cgetf100PauseType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 8, 1, 21),
    _Cgetf100PauseType_Type()
)
cgetf100PauseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgetf100PauseType.setStatus("mandatory")
_Csdtf100Table_Object = MibTable
csdtf100Table = _Csdtf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    csdtf100Table.setStatus("mandatory")
_Csdtf100Entry_Object = MibTableRow
csdtf100Entry = _Csdtf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1)
)
csdtf100Entry.setIndexNames(
    (0, "MCC16-MIB", "csdtf100BiaIndex"),
    (0, "MCC16-MIB", "csdtf100SlotIndex"),
)
if mibBuilder.loadTexts:
    csdtf100Entry.setStatus("mandatory")
_Csdtf100BiaIndex_Type = Integer32
_Csdtf100BiaIndex_Object = MibTableColumn
csdtf100BiaIndex = _Csdtf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 1),
    _Csdtf100BiaIndex_Type()
)
csdtf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100BiaIndex.setStatus("mandatory")
_Csdtf100SlotIndex_Type = Integer32
_Csdtf100SlotIndex_Object = MibTableColumn
csdtf100SlotIndex = _Csdtf100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 2),
    _Csdtf100SlotIndex_Type()
)
csdtf100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100SlotIndex.setStatus("mandatory")
_Csdtf100Groups_Type = DisplayString
_Csdtf100Groups_Object = MibTableColumn
csdtf100Groups = _Csdtf100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 3),
    _Csdtf100Groups_Type()
)
csdtf100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csdtf100Groups.setStatus("mandatory")
_Csdtf100MRevision_Type = Integer32
_Csdtf100MRevision_Object = MibTableColumn
csdtf100MRevision = _Csdtf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 4),
    _Csdtf100MRevision_Type()
)
csdtf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100MRevision.setStatus("mandatory")


class _Csdtf100CfgMatch_Type(Integer32):
    """Custom type csdtf100CfgMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 3),
          ("no", 2),
          ("yes", 1))
    )


_Csdtf100CfgMatch_Type.__name__ = "Integer32"
_Csdtf100CfgMatch_Object = MibTableColumn
csdtf100CfgMatch = _Csdtf100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 5),
    _Csdtf100CfgMatch_Type()
)
csdtf100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100CfgMatch.setStatus("mandatory")
_Csdtf100SerialNumber_Type = Integer32
_Csdtf100SerialNumber_Object = MibTableColumn
csdtf100SerialNumber = _Csdtf100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 6),
    _Csdtf100SerialNumber_Type()
)
csdtf100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100SerialNumber.setStatus("mandatory")
_Csdtf100ConnA_Type = CpsConnector
_Csdtf100ConnA_Object = MibTableColumn
csdtf100ConnA = _Csdtf100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 7),
    _Csdtf100ConnA_Type()
)
csdtf100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100ConnA.setStatus("mandatory")
_Csdtf100ConnB_Type = CpsConnector
_Csdtf100ConnB_Object = MibTableColumn
csdtf100ConnB = _Csdtf100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 8),
    _Csdtf100ConnB_Type()
)
csdtf100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100ConnB.setStatus("mandatory")


class _Csdtf100CopperLink_Type(Integer32):
    """Custom type csdtf100CopperLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Csdtf100CopperLink_Type.__name__ = "Integer32"
_Csdtf100CopperLink_Object = MibTableColumn
csdtf100CopperLink = _Csdtf100CopperLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 9),
    _Csdtf100CopperLink_Type()
)
csdtf100CopperLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100CopperLink.setStatus("mandatory")


class _Csdtf100FiberLink_Type(Integer32):
    """Custom type csdtf100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Csdtf100FiberLink_Type.__name__ = "Integer32"
_Csdtf100FiberLink_Object = MibTableColumn
csdtf100FiberLink = _Csdtf100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 10),
    _Csdtf100FiberLink_Type()
)
csdtf100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100FiberLink.setStatus("mandatory")


class _Csdtf100Fault_Type(Integer32):
    """Custom type csdtf100Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Csdtf100Fault_Type.__name__ = "Integer32"
_Csdtf100Fault_Object = MibTableColumn
csdtf100Fault = _Csdtf100Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 11),
    _Csdtf100Fault_Type()
)
csdtf100Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100Fault.setStatus("mandatory")


class _Csdtf100TAOSFiber_Type(Integer32):
    """Custom type csdtf100TAOSFiber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Csdtf100TAOSFiber_Type.__name__ = "Integer32"
_Csdtf100TAOSFiber_Object = MibTableColumn
csdtf100TAOSFiber = _Csdtf100TAOSFiber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 12),
    _Csdtf100TAOSFiber_Type()
)
csdtf100TAOSFiber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csdtf100TAOSFiber.setStatus("mandatory")


class _Csdtf100TAOSCopper_Type(Integer32):
    """Custom type csdtf100TAOSCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Csdtf100TAOSCopper_Type.__name__ = "Integer32"
_Csdtf100TAOSCopper_Object = MibTableColumn
csdtf100TAOSCopper = _Csdtf100TAOSCopper_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 13),
    _Csdtf100TAOSCopper_Type()
)
csdtf100TAOSCopper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csdtf100TAOSCopper.setStatus("mandatory")


class _Csdtf100AISFiber_Type(Integer32):
    """Custom type csdtf100AISFiber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_Csdtf100AISFiber_Type.__name__ = "Integer32"
_Csdtf100AISFiber_Object = MibTableColumn
csdtf100AISFiber = _Csdtf100AISFiber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 14),
    _Csdtf100AISFiber_Type()
)
csdtf100AISFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100AISFiber.setStatus("mandatory")


class _Csdtf100AISCopper_Type(Integer32):
    """Custom type csdtf100AISCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_Csdtf100AISCopper_Type.__name__ = "Integer32"
_Csdtf100AISCopper_Object = MibTableColumn
csdtf100AISCopper = _Csdtf100AISCopper_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 15),
    _Csdtf100AISCopper_Type()
)
csdtf100AISCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100AISCopper.setStatus("mandatory")


class _Csdtf100CopperLoopback_Type(Integer32):
    """Custom type csdtf100CopperLoopback based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Csdtf100CopperLoopback_Type.__name__ = "Integer32"
_Csdtf100CopperLoopback_Object = MibTableColumn
csdtf100CopperLoopback = _Csdtf100CopperLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 16),
    _Csdtf100CopperLoopback_Type()
)
csdtf100CopperLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csdtf100CopperLoopback.setStatus("mandatory")


class _Csdtf100CopperLongHaul_Type(Integer32):
    """Custom type csdtf100CopperLongHaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Csdtf100CopperLongHaul_Type.__name__ = "Integer32"
_Csdtf100CopperLongHaul_Object = MibTableColumn
csdtf100CopperLongHaul = _Csdtf100CopperLongHaul_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 17),
    _Csdtf100CopperLongHaul_Type()
)
csdtf100CopperLongHaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100CopperLongHaul.setStatus("mandatory")


class _Csdtf100T1E1_Type(Integer32):
    """Custom type csdtf100T1E1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_Csdtf100T1E1_Type.__name__ = "Integer32"
_Csdtf100T1E1_Object = MibTableColumn
csdtf100T1E1 = _Csdtf100T1E1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 18),
    _Csdtf100T1E1_Type()
)
csdtf100T1E1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100T1E1.setStatus("mandatory")


class _Csdtf100ConfigMode_Type(Integer32):
    """Custom type csdtf100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Csdtf100ConfigMode_Type.__name__ = "Integer32"
_Csdtf100ConfigMode_Object = MibTableColumn
csdtf100ConfigMode = _Csdtf100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 19),
    _Csdtf100ConfigMode_Type()
)
csdtf100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100ConfigMode.setStatus("mandatory")


class _Csdtf100TPCoax_Type(Integer32):
    """Custom type csdtf100TPCoax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coax", 2),
          ("tp", 1))
    )


_Csdtf100TPCoax_Type.__name__ = "Integer32"
_Csdtf100TPCoax_Object = MibTableColumn
csdtf100TPCoax = _Csdtf100TPCoax_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 20),
    _Csdtf100TPCoax_Type()
)
csdtf100TPCoax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100TPCoax.setStatus("mandatory")


class _Csdtf100CopperLineBuildout_Type(Integer32):
    """Custom type csdtf100CopperLineBuildout based on Integer32"""
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
        *(("e12-37V75ohm", 2),
          ("e13-0V120ohm", 1),
          ("t1LH-0dB", 9),
          ("t1LH-m15dB", 11),
          ("t1LH-m22-5dB", 12),
          ("t1LH-m7-5dB", 10),
          ("t1SH-DSX-0-133ANSIT1403", 3),
          ("t1SH-DSX-133-266", 4),
          ("t1SH-DSX-266-399", 5),
          ("t1SH-DSX-399-533", 6),
          ("t1SH-DSX-533-655", 7),
          ("t1SH-DSX-6V", 8))
    )


_Csdtf100CopperLineBuildout_Type.__name__ = "Integer32"
_Csdtf100CopperLineBuildout_Object = MibTableColumn
csdtf100CopperLineBuildout = _Csdtf100CopperLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 21),
    _Csdtf100CopperLineBuildout_Type()
)
csdtf100CopperLineBuildout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100CopperLineBuildout.setStatus("mandatory")


class _Csdtf100FiberLoopback_Type(Integer32):
    """Custom type csdtf100FiberLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Csdtf100FiberLoopback_Type.__name__ = "Integer32"
_Csdtf100FiberLoopback_Object = MibTableColumn
csdtf100FiberLoopback = _Csdtf100FiberLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 22),
    _Csdtf100FiberLoopback_Type()
)
csdtf100FiberLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csdtf100FiberLoopback.setStatus("mandatory")


class _Csdtf100RmtSupported_Type(Integer32):
    """Custom type csdtf100RmtSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Csdtf100RmtSupported_Type.__name__ = "Integer32"
_Csdtf100RmtSupported_Object = MibTableColumn
csdtf100RmtSupported = _Csdtf100RmtSupported_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 23),
    _Csdtf100RmtSupported_Type()
)
csdtf100RmtSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtSupported.setStatus("mandatory")


class _Csdtf100RmtDetected_Type(Integer32):
    """Custom type csdtf100RmtDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Csdtf100RmtDetected_Type.__name__ = "Integer32"
_Csdtf100RmtDetected_Object = MibTableColumn
csdtf100RmtDetected = _Csdtf100RmtDetected_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 24),
    _Csdtf100RmtDetected_Type()
)
csdtf100RmtDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtDetected.setStatus("mandatory")
_Csdtf100RmtMRevision_Type = Integer32
_Csdtf100RmtMRevision_Object = MibTableColumn
csdtf100RmtMRevision = _Csdtf100RmtMRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 25),
    _Csdtf100RmtMRevision_Type()
)
csdtf100RmtMRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtMRevision.setStatus("mandatory")
_Csdtf100RmtSerialNumber_Type = Integer32
_Csdtf100RmtSerialNumber_Object = MibTableColumn
csdtf100RmtSerialNumber = _Csdtf100RmtSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 26),
    _Csdtf100RmtSerialNumber_Type()
)
csdtf100RmtSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtSerialNumber.setStatus("mandatory")
_Csdtf100RmtConnA_Type = CpsConnector
_Csdtf100RmtConnA_Object = MibTableColumn
csdtf100RmtConnA = _Csdtf100RmtConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 27),
    _Csdtf100RmtConnA_Type()
)
csdtf100RmtConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtConnA.setStatus("mandatory")
_Csdtf100RmtConnB_Type = CpsConnector
_Csdtf100RmtConnB_Object = MibTableColumn
csdtf100RmtConnB = _Csdtf100RmtConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 28),
    _Csdtf100RmtConnB_Type()
)
csdtf100RmtConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtConnB.setStatus("mandatory")


class _Csdtf100RmtCopperLink_Type(Integer32):
    """Custom type csdtf100RmtCopperLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Csdtf100RmtCopperLink_Type.__name__ = "Integer32"
_Csdtf100RmtCopperLink_Object = MibTableColumn
csdtf100RmtCopperLink = _Csdtf100RmtCopperLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 29),
    _Csdtf100RmtCopperLink_Type()
)
csdtf100RmtCopperLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtCopperLink.setStatus("mandatory")


class _Csdtf100RmtFiberLink_Type(Integer32):
    """Custom type csdtf100RmtFiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Csdtf100RmtFiberLink_Type.__name__ = "Integer32"
_Csdtf100RmtFiberLink_Object = MibTableColumn
csdtf100RmtFiberLink = _Csdtf100RmtFiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 30),
    _Csdtf100RmtFiberLink_Type()
)
csdtf100RmtFiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtFiberLink.setStatus("mandatory")


class _Csdtf100RmtFault_Type(Integer32):
    """Custom type csdtf100RmtFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Csdtf100RmtFault_Type.__name__ = "Integer32"
_Csdtf100RmtFault_Object = MibTableColumn
csdtf100RmtFault = _Csdtf100RmtFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 31),
    _Csdtf100RmtFault_Type()
)
csdtf100RmtFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtFault.setStatus("mandatory")


class _Csdtf100RmtTAOSFiber_Type(Integer32):
    """Custom type csdtf100RmtTAOSFiber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Csdtf100RmtTAOSFiber_Type.__name__ = "Integer32"
_Csdtf100RmtTAOSFiber_Object = MibTableColumn
csdtf100RmtTAOSFiber = _Csdtf100RmtTAOSFiber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 32),
    _Csdtf100RmtTAOSFiber_Type()
)
csdtf100RmtTAOSFiber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csdtf100RmtTAOSFiber.setStatus("mandatory")


class _Csdtf100RmtTAOSCopper_Type(Integer32):
    """Custom type csdtf100RmtTAOSCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Csdtf100RmtTAOSCopper_Type.__name__ = "Integer32"
_Csdtf100RmtTAOSCopper_Object = MibTableColumn
csdtf100RmtTAOSCopper = _Csdtf100RmtTAOSCopper_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 33),
    _Csdtf100RmtTAOSCopper_Type()
)
csdtf100RmtTAOSCopper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csdtf100RmtTAOSCopper.setStatus("mandatory")


class _Csdtf100RmtAISFiber_Type(Integer32):
    """Custom type csdtf100RmtAISFiber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_Csdtf100RmtAISFiber_Type.__name__ = "Integer32"
_Csdtf100RmtAISFiber_Object = MibTableColumn
csdtf100RmtAISFiber = _Csdtf100RmtAISFiber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 34),
    _Csdtf100RmtAISFiber_Type()
)
csdtf100RmtAISFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtAISFiber.setStatus("mandatory")


class _Csdtf100RmtAISCopper_Type(Integer32):
    """Custom type csdtf100RmtAISCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_Csdtf100RmtAISCopper_Type.__name__ = "Integer32"
_Csdtf100RmtAISCopper_Object = MibTableColumn
csdtf100RmtAISCopper = _Csdtf100RmtAISCopper_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 35),
    _Csdtf100RmtAISCopper_Type()
)
csdtf100RmtAISCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtAISCopper.setStatus("mandatory")


class _Csdtf100RmtCopperLoopback_Type(Integer32):
    """Custom type csdtf100RmtCopperLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Csdtf100RmtCopperLoopback_Type.__name__ = "Integer32"
_Csdtf100RmtCopperLoopback_Object = MibTableColumn
csdtf100RmtCopperLoopback = _Csdtf100RmtCopperLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 36),
    _Csdtf100RmtCopperLoopback_Type()
)
csdtf100RmtCopperLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csdtf100RmtCopperLoopback.setStatus("mandatory")


class _Csdtf100RmtCopperLongHaul_Type(Integer32):
    """Custom type csdtf100RmtCopperLongHaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Csdtf100RmtCopperLongHaul_Type.__name__ = "Integer32"
_Csdtf100RmtCopperLongHaul_Object = MibTableColumn
csdtf100RmtCopperLongHaul = _Csdtf100RmtCopperLongHaul_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 37),
    _Csdtf100RmtCopperLongHaul_Type()
)
csdtf100RmtCopperLongHaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtCopperLongHaul.setStatus("mandatory")


class _Csdtf100RmtConfigMode_Type(Integer32):
    """Custom type csdtf100RmtConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Csdtf100RmtConfigMode_Type.__name__ = "Integer32"
_Csdtf100RmtConfigMode_Object = MibTableColumn
csdtf100RmtConfigMode = _Csdtf100RmtConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 38),
    _Csdtf100RmtConfigMode_Type()
)
csdtf100RmtConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtConfigMode.setStatus("mandatory")


class _Csdtf100RmtTPCoax_Type(Integer32):
    """Custom type csdtf100RmtTPCoax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coax", 2),
          ("tp", 1))
    )


_Csdtf100RmtTPCoax_Type.__name__ = "Integer32"
_Csdtf100RmtTPCoax_Object = MibTableColumn
csdtf100RmtTPCoax = _Csdtf100RmtTPCoax_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 39),
    _Csdtf100RmtTPCoax_Type()
)
csdtf100RmtTPCoax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtTPCoax.setStatus("mandatory")


class _Csdtf100RmtCopperLineBuildout_Type(Integer32):
    """Custom type csdtf100RmtCopperLineBuildout based on Integer32"""
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
        *(("e12-37V75ohm", 2),
          ("e13-0V120ohm", 1),
          ("t1LH-0dB", 9),
          ("t1LH-m15dB", 11),
          ("t1LH-m22-5dB", 12),
          ("t1LH-m7-5dB", 10),
          ("t1SH-DSX-0-133ANSIT1403", 3),
          ("t1SH-DSX-133-266", 4),
          ("t1SH-DSX-266-399", 5),
          ("t1SH-DSX-399-533", 6),
          ("t1SH-DSX-533-655", 7),
          ("t1SH-DSX-6V", 8))
    )


_Csdtf100RmtCopperLineBuildout_Type.__name__ = "Integer32"
_Csdtf100RmtCopperLineBuildout_Object = MibTableColumn
csdtf100RmtCopperLineBuildout = _Csdtf100RmtCopperLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 40),
    _Csdtf100RmtCopperLineBuildout_Type()
)
csdtf100RmtCopperLineBuildout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100RmtCopperLineBuildout.setStatus("mandatory")


class _Csdtf100RmtFiberLoopback_Type(Integer32):
    """Custom type csdtf100RmtFiberLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Csdtf100RmtFiberLoopback_Type.__name__ = "Integer32"
_Csdtf100RmtFiberLoopback_Object = MibTableColumn
csdtf100RmtFiberLoopback = _Csdtf100RmtFiberLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 41),
    _Csdtf100RmtFiberLoopback_Type()
)
csdtf100RmtFiberLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csdtf100RmtFiberLoopback.setStatus("mandatory")


class _Csdtf100CacheClean_Type(Integer32):
    """Custom type csdtf100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Csdtf100CacheClean_Type.__name__ = "Integer32"
_Csdtf100CacheClean_Object = MibTableColumn
csdtf100CacheClean = _Csdtf100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 9, 1, 42),
    _Csdtf100CacheClean_Type()
)
csdtf100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csdtf100CacheClean.setStatus("mandatory")
_Cpsmp110Table_Object = MibTable
cpsmp110Table = _Cpsmp110Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10)
)
if mibBuilder.loadTexts:
    cpsmp110Table.setStatus("mandatory")
_Cpsmp110Entry_Object = MibTableRow
cpsmp110Entry = _Cpsmp110Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1)
)
cpsmp110Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsmp110SubDeviceIndex"),
    (0, "MCC16-MIB", "cpsmp110BiaIndex"),
    (0, "MCC16-MIB", "cpsmp110SlotIndex"),
)
if mibBuilder.loadTexts:
    cpsmp110Entry.setStatus("mandatory")
_Cpsmp110SubDeviceIndex_Type = Integer32
_Cpsmp110SubDeviceIndex_Object = MibTableColumn
cpsmp110SubDeviceIndex = _Cpsmp110SubDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 1),
    _Cpsmp110SubDeviceIndex_Type()
)
cpsmp110SubDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110SubDeviceIndex.setStatus("mandatory")
_Cpsmp110BiaIndex_Type = Integer32
_Cpsmp110BiaIndex_Object = MibTableColumn
cpsmp110BiaIndex = _Cpsmp110BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 2),
    _Cpsmp110BiaIndex_Type()
)
cpsmp110BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110BiaIndex.setStatus("mandatory")
_Cpsmp110SlotIndex_Type = Integer32
_Cpsmp110SlotIndex_Object = MibTableColumn
cpsmp110SlotIndex = _Cpsmp110SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 3),
    _Cpsmp110SlotIndex_Type()
)
cpsmp110SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110SlotIndex.setStatus("mandatory")
_Cpsmp110Groups_Type = DisplayString
_Cpsmp110Groups_Object = MibTableColumn
cpsmp110Groups = _Cpsmp110Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 4),
    _Cpsmp110Groups_Type()
)
cpsmp110Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmp110Groups.setStatus("mandatory")
_Cpsmp110MRevision_Type = Integer32
_Cpsmp110MRevision_Object = MibTableColumn
cpsmp110MRevision = _Cpsmp110MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 5),
    _Cpsmp110MRevision_Type()
)
cpsmp110MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110MRevision.setStatus("mandatory")


class _Cpsmp110CfgMatch_Type(Integer32):
    """Custom type cpsmp110CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cpsmp110CfgMatch_Type.__name__ = "Integer32"
_Cpsmp110CfgMatch_Object = MibTableColumn
cpsmp110CfgMatch = _Cpsmp110CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 6),
    _Cpsmp110CfgMatch_Type()
)
cpsmp110CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110CfgMatch.setStatus("mandatory")
_Cpsmp110SerialNumber_Type = Integer32
_Cpsmp110SerialNumber_Object = MibTableColumn
cpsmp110SerialNumber = _Cpsmp110SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 7),
    _Cpsmp110SerialNumber_Type()
)
cpsmp110SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110SerialNumber.setStatus("mandatory")


class _Cpsmp110ConfigMode_Type(Integer32):
    """Custom type cpsmp110ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cpsmp110ConfigMode_Type.__name__ = "Integer32"
_Cpsmp110ConfigMode_Object = MibTableColumn
cpsmp110ConfigMode = _Cpsmp110ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 8),
    _Cpsmp110ConfigMode_Type()
)
cpsmp110ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110ConfigMode.setStatus("mandatory")


class _Cpsmp110MasterTempFault_Type(Integer32):
    """Custom type cpsmp110MasterTempFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp110MasterTempFault_Type.__name__ = "Integer32"
_Cpsmp110MasterTempFault_Object = MibTableColumn
cpsmp110MasterTempFault = _Cpsmp110MasterTempFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 9),
    _Cpsmp110MasterTempFault_Type()
)
cpsmp110MasterTempFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110MasterTempFault.setStatus("mandatory")


class _Cpsmp110MasterCurrentFault_Type(Integer32):
    """Custom type cpsmp110MasterCurrentFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp110MasterCurrentFault_Type.__name__ = "Integer32"
_Cpsmp110MasterCurrentFault_Object = MibTableColumn
cpsmp110MasterCurrentFault = _Cpsmp110MasterCurrentFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 10),
    _Cpsmp110MasterCurrentFault_Type()
)
cpsmp110MasterCurrentFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110MasterCurrentFault.setStatus("mandatory")


class _Cpsmp110MasterFanFault_Type(Integer32):
    """Custom type cpsmp110MasterFanFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp110MasterFanFault_Type.__name__ = "Integer32"
_Cpsmp110MasterFanFault_Object = MibTableColumn
cpsmp110MasterFanFault = _Cpsmp110MasterFanFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 11),
    _Cpsmp110MasterFanFault_Type()
)
cpsmp110MasterFanFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110MasterFanFault.setStatus("mandatory")
_Cpsmp110FirmwareRevision_Type = Integer32
_Cpsmp110FirmwareRevision_Object = MibTableColumn
cpsmp110FirmwareRevision = _Cpsmp110FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 12),
    _Cpsmp110FirmwareRevision_Type()
)
cpsmp110FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110FirmwareRevision.setStatus("mandatory")


class _Cpsmp110PSSupplyTbl_Type(Integer32):
    """Custom type cpsmp110PSSupplyTbl based on Integer32"""
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
        *(("ac", 1),
          ("dc", 2),
          ("notInstalled", 5),
          ("reserved3", 3),
          ("reserved4", 4))
    )


_Cpsmp110PSSupplyTbl_Type.__name__ = "Integer32"
_Cpsmp110PSSupplyTbl_Object = MibTableColumn
cpsmp110PSSupplyTbl = _Cpsmp110PSSupplyTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 13),
    _Cpsmp110PSSupplyTbl_Type()
)
cpsmp110PSSupplyTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110PSSupplyTbl.setStatus("mandatory")


class _Cpsmp110PSRoleTbl_Type(Integer32):
    """Custom type cpsmp110PSRoleTbl based on Integer32"""
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
        *(("master", 1),
          ("notInstalled", 4),
          ("shared", 3),
          ("slave", 2))
    )


_Cpsmp110PSRoleTbl_Type.__name__ = "Integer32"
_Cpsmp110PSRoleTbl_Object = MibTableColumn
cpsmp110PSRoleTbl = _Cpsmp110PSRoleTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 14),
    _Cpsmp110PSRoleTbl_Type()
)
cpsmp110PSRoleTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsmp110PSRoleTbl.setStatus("mandatory")


class _Cpsmp110PSReadyTbl_Type(Integer32):
    """Custom type cpsmp110PSReadyTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp110PSReadyTbl_Type.__name__ = "Integer32"
_Cpsmp110PSReadyTbl_Object = MibTableColumn
cpsmp110PSReadyTbl = _Cpsmp110PSReadyTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 15),
    _Cpsmp110PSReadyTbl_Type()
)
cpsmp110PSReadyTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110PSReadyTbl.setStatus("mandatory")


class _Cpsmp110PSInUseTbl_Type(Integer32):
    """Custom type cpsmp110PSInUseTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp110PSInUseTbl_Type.__name__ = "Integer32"
_Cpsmp110PSInUseTbl_Object = MibTableColumn
cpsmp110PSInUseTbl = _Cpsmp110PSInUseTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 16),
    _Cpsmp110PSInUseTbl_Type()
)
cpsmp110PSInUseTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110PSInUseTbl.setStatus("mandatory")
_Cpsmp110TemperatureTbl_Type = Integer32
_Cpsmp110TemperatureTbl_Object = MibTableColumn
cpsmp110TemperatureTbl = _Cpsmp110TemperatureTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 17),
    _Cpsmp110TemperatureTbl_Type()
)
cpsmp110TemperatureTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110TemperatureTbl.setStatus("mandatory")
_Cpsmp110CurrentTbl_Type = Integer32
_Cpsmp110CurrentTbl_Object = MibTableColumn
cpsmp110CurrentTbl = _Cpsmp110CurrentTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 18),
    _Cpsmp110CurrentTbl_Type()
)
cpsmp110CurrentTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110CurrentTbl.setStatus("mandatory")


class _Cpsmp110FanStatusTbl_Type(Integer32):
    """Custom type cpsmp110FanStatusTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("notInstalled", 3),
          ("ok", 1))
    )


_Cpsmp110FanStatusTbl_Type.__name__ = "Integer32"
_Cpsmp110FanStatusTbl_Object = MibTableColumn
cpsmp110FanStatusTbl = _Cpsmp110FanStatusTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 19),
    _Cpsmp110FanStatusTbl_Type()
)
cpsmp110FanStatusTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110FanStatusTbl.setStatus("mandatory")


class _Cpsmp110TempFaultTbl_Type(Integer32):
    """Custom type cpsmp110TempFaultTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp110TempFaultTbl_Type.__name__ = "Integer32"
_Cpsmp110TempFaultTbl_Object = MibTableColumn
cpsmp110TempFaultTbl = _Cpsmp110TempFaultTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 20),
    _Cpsmp110TempFaultTbl_Type()
)
cpsmp110TempFaultTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110TempFaultTbl.setStatus("mandatory")


class _Cpsmp110CurrFaultTbl_Type(Integer32):
    """Custom type cpsmp110CurrFaultTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsmp110CurrFaultTbl_Type.__name__ = "Integer32"
_Cpsmp110CurrFaultTbl_Object = MibTableColumn
cpsmp110CurrFaultTbl = _Cpsmp110CurrFaultTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 21),
    _Cpsmp110CurrFaultTbl_Type()
)
cpsmp110CurrFaultTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110CurrFaultTbl.setStatus("mandatory")
_Cpsmp110PSCount_Type = Integer32
_Cpsmp110PSCount_Object = MibTableColumn
cpsmp110PSCount = _Cpsmp110PSCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 22),
    _Cpsmp110PSCount_Type()
)
cpsmp110PSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110PSCount.setStatus("mandatory")
_Cpsmp110TempSensorCount_Type = Integer32
_Cpsmp110TempSensorCount_Object = MibTableColumn
cpsmp110TempSensorCount = _Cpsmp110TempSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 23),
    _Cpsmp110TempSensorCount_Type()
)
cpsmp110TempSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110TempSensorCount.setStatus("mandatory")
_Cpsmp110CurrSensorCount_Type = Integer32
_Cpsmp110CurrSensorCount_Object = MibTableColumn
cpsmp110CurrSensorCount = _Cpsmp110CurrSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 24),
    _Cpsmp110CurrSensorCount_Type()
)
cpsmp110CurrSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110CurrSensorCount.setStatus("mandatory")
_Cpsmp110FanCount_Type = Integer32
_Cpsmp110FanCount_Object = MibTableColumn
cpsmp110FanCount = _Cpsmp110FanCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 25),
    _Cpsmp110FanCount_Type()
)
cpsmp110FanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110FanCount.setStatus("mandatory")


class _Cpsmp110CacheClean_Type(Integer32):
    """Custom type cpsmp110CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cpsmp110CacheClean_Type.__name__ = "Integer32"
_Cpsmp110CacheClean_Object = MibTableColumn
cpsmp110CacheClean = _Cpsmp110CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 10, 1, 26),
    _Cpsmp110CacheClean_Type()
)
cpsmp110CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsmp110CacheClean.setStatus("mandatory")
_Cbftf100Table_Object = MibTable
cbftf100Table = _Cbftf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11)
)
if mibBuilder.loadTexts:
    cbftf100Table.setStatus("mandatory")
_Cbftf100Entry_Object = MibTableRow
cbftf100Entry = _Cbftf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1)
)
cbftf100Entry.setIndexNames(
    (0, "MCC16-MIB", "cbftf100SubDeviceIndex"),
    (0, "MCC16-MIB", "cbftf100BiaIndex"),
    (0, "MCC16-MIB", "cbftf100SlotIndex"),
)
if mibBuilder.loadTexts:
    cbftf100Entry.setStatus("mandatory")
_Cbftf100SubDeviceIndex_Type = Integer32
_Cbftf100SubDeviceIndex_Object = MibTableColumn
cbftf100SubDeviceIndex = _Cbftf100SubDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 1),
    _Cbftf100SubDeviceIndex_Type()
)
cbftf100SubDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100SubDeviceIndex.setStatus("mandatory")
_Cbftf100BiaIndex_Type = Integer32
_Cbftf100BiaIndex_Object = MibTableColumn
cbftf100BiaIndex = _Cbftf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 2),
    _Cbftf100BiaIndex_Type()
)
cbftf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100BiaIndex.setStatus("mandatory")
_Cbftf100SlotIndex_Type = Integer32
_Cbftf100SlotIndex_Object = MibTableColumn
cbftf100SlotIndex = _Cbftf100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 3),
    _Cbftf100SlotIndex_Type()
)
cbftf100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100SlotIndex.setStatus("mandatory")
_Cbftf100Groups_Type = DisplayString
_Cbftf100Groups_Object = MibTableColumn
cbftf100Groups = _Cbftf100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 4),
    _Cbftf100Groups_Type()
)
cbftf100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100Groups.setStatus("mandatory")
_Cbftf100MRevision_Type = Integer32
_Cbftf100MRevision_Object = MibTableColumn
cbftf100MRevision = _Cbftf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 5),
    _Cbftf100MRevision_Type()
)
cbftf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100MRevision.setStatus("mandatory")


class _Cbftf100CfgMatch_Type(Integer32):
    """Custom type cbftf100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cbftf100CfgMatch_Type.__name__ = "Integer32"
_Cbftf100CfgMatch_Object = MibTableColumn
cbftf100CfgMatch = _Cbftf100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 6),
    _Cbftf100CfgMatch_Type()
)
cbftf100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100CfgMatch.setStatus("mandatory")
_Cbftf100SerialNumber_Type = Integer32
_Cbftf100SerialNumber_Object = MibTableColumn
cbftf100SerialNumber = _Cbftf100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 7),
    _Cbftf100SerialNumber_Type()
)
cbftf100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100SerialNumber.setStatus("mandatory")


class _Cbftf100ConfigMode_Type(Integer32):
    """Custom type cbftf100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cbftf100ConfigMode_Type.__name__ = "Integer32"
_Cbftf100ConfigMode_Object = MibTableColumn
cbftf100ConfigMode = _Cbftf100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 8),
    _Cbftf100ConfigMode_Type()
)
cbftf100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100ConfigMode.setStatus("mandatory")
_Cbftf100FirmwareRevision_Type = Integer32
_Cbftf100FirmwareRevision_Object = MibTableColumn
cbftf100FirmwareRevision = _Cbftf100FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 9),
    _Cbftf100FirmwareRevision_Type()
)
cbftf100FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100FirmwareRevision.setStatus("mandatory")


class _Cbftf100SelfTestFailed_Type(Integer32):
    """Custom type cbftf100SelfTestFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cbftf100SelfTestFailed_Type.__name__ = "Integer32"
_Cbftf100SelfTestFailed_Object = MibTableColumn
cbftf100SelfTestFailed = _Cbftf100SelfTestFailed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 10),
    _Cbftf100SelfTestFailed_Type()
)
cbftf100SelfTestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100SelfTestFailed.setStatus("mandatory")


class _Cbftf100SpanningTree_Type(Integer32):
    """Custom type cbftf100SpanningTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cbftf100SpanningTree_Type.__name__ = "Integer32"
_Cbftf100SpanningTree_Object = MibTableColumn
cbftf100SpanningTree = _Cbftf100SpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 11),
    _Cbftf100SpanningTree_Type()
)
cbftf100SpanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100SpanningTree.setStatus("mandatory")


class _Cbftf100MirrorCfg_Type(Integer32):
    """Custom type cbftf100MirrorCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cbftf100MirrorCfg_Type.__name__ = "Integer32"
_Cbftf100MirrorCfg_Object = MibTableColumn
cbftf100MirrorCfg = _Cbftf100MirrorCfg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 12),
    _Cbftf100MirrorCfg_Type()
)
cbftf100MirrorCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100MirrorCfg.setStatus("mandatory")


class _Cbftf100SACMasterCfg_Type(Integer32):
    """Custom type cbftf100SACMasterCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cbftf100SACMasterCfg_Type.__name__ = "Integer32"
_Cbftf100SACMasterCfg_Object = MibTableColumn
cbftf100SACMasterCfg = _Cbftf100SACMasterCfg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 13),
    _Cbftf100SACMasterCfg_Type()
)
cbftf100SACMasterCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100SACMasterCfg.setStatus("mandatory")


class _Cbftf100FormFactor_Type(Integer32):
    """Custom type cbftf100FormFactor based on Integer32"""
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
        *(("s1W1N1a", 3),
          ("s1W1N2a", 2),
          ("s1W2a", 1),
          ("s2W1N5a", 5),
          ("s2W2N4a", 4))
    )


_Cbftf100FormFactor_Type.__name__ = "Integer32"
_Cbftf100FormFactor_Object = MibTableColumn
cbftf100FormFactor = _Cbftf100FormFactor_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 14),
    _Cbftf100FormFactor_Type()
)
cbftf100FormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100FormFactor.setStatus("mandatory")


class _Cbftf100AutoNegotTbl_Type(Integer32):
    """Custom type cbftf100AutoNegotTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cbftf100AutoNegotTbl_Type.__name__ = "Integer32"
_Cbftf100AutoNegotTbl_Object = MibTableColumn
cbftf100AutoNegotTbl = _Cbftf100AutoNegotTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 15),
    _Cbftf100AutoNegotTbl_Type()
)
cbftf100AutoNegotTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100AutoNegotTbl.setStatus("mandatory")


class _Cbftf100FullDuplexTbl_Type(Integer32):
    """Custom type cbftf100FullDuplexTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("negotiating", 3))
    )


_Cbftf100FullDuplexTbl_Type.__name__ = "Integer32"
_Cbftf100FullDuplexTbl_Object = MibTableColumn
cbftf100FullDuplexTbl = _Cbftf100FullDuplexTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 16),
    _Cbftf100FullDuplexTbl_Type()
)
cbftf100FullDuplexTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100FullDuplexTbl.setStatus("mandatory")


class _Cbftf100100MbpsTbl_Type(Integer32):
    """Custom type cbftf100100MbpsTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mbps10", 2),
          ("mbps100", 1),
          ("negotiating", 3))
    )


_Cbftf100100MbpsTbl_Type.__name__ = "Integer32"
_Cbftf100100MbpsTbl_Object = MibTableColumn
cbftf100100MbpsTbl = _Cbftf100100MbpsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 17),
    _Cbftf100100MbpsTbl_Type()
)
cbftf100100MbpsTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100100MbpsTbl.setStatus("mandatory")


class _Cbftf100Adv10HDXTbl_Type(Integer32):
    """Custom type cbftf100Adv10HDXTbl based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Cbftf100Adv10HDXTbl_Type.__name__ = "Integer32"
_Cbftf100Adv10HDXTbl_Object = MibTableColumn
cbftf100Adv10HDXTbl = _Cbftf100Adv10HDXTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 18),
    _Cbftf100Adv10HDXTbl_Type()
)
cbftf100Adv10HDXTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100Adv10HDXTbl.setStatus("mandatory")


class _Cbftf100Adv10FDXTbl_Type(Integer32):
    """Custom type cbftf100Adv10FDXTbl based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Cbftf100Adv10FDXTbl_Type.__name__ = "Integer32"
_Cbftf100Adv10FDXTbl_Object = MibTableColumn
cbftf100Adv10FDXTbl = _Cbftf100Adv10FDXTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 19),
    _Cbftf100Adv10FDXTbl_Type()
)
cbftf100Adv10FDXTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100Adv10FDXTbl.setStatus("mandatory")


class _Cbftf100Adv100HDXTbl_Type(Integer32):
    """Custom type cbftf100Adv100HDXTbl based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Cbftf100Adv100HDXTbl_Type.__name__ = "Integer32"
_Cbftf100Adv100HDXTbl_Object = MibTableColumn
cbftf100Adv100HDXTbl = _Cbftf100Adv100HDXTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 20),
    _Cbftf100Adv100HDXTbl_Type()
)
cbftf100Adv100HDXTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100Adv100HDXTbl.setStatus("mandatory")


class _Cbftf100Adv100FDXTbl_Type(Integer32):
    """Custom type cbftf100Adv100FDXTbl based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Cbftf100Adv100FDXTbl_Type.__name__ = "Integer32"
_Cbftf100Adv100FDXTbl_Object = MibTableColumn
cbftf100Adv100FDXTbl = _Cbftf100Adv100FDXTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 21),
    _Cbftf100Adv100FDXTbl_Type()
)
cbftf100Adv100FDXTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100Adv100FDXTbl.setStatus("mandatory")


class _Cbftf100CrossTbl_Type(Integer32):
    """Custom type cbftf100CrossTbl based on Integer32"""
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
        *(("auto", 1),
          ("mdi", 2),
          ("mdix", 3),
          ("notSupported", 4))
    )


_Cbftf100CrossTbl_Type.__name__ = "Integer32"
_Cbftf100CrossTbl_Object = MibTableColumn
cbftf100CrossTbl = _Cbftf100CrossTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 22),
    _Cbftf100CrossTbl_Type()
)
cbftf100CrossTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100CrossTbl.setStatus("mandatory")


class _Cbftf100PauseCfgTbl_Type(Integer32):
    """Custom type cbftf100PauseCfgTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cbftf100PauseCfgTbl_Type.__name__ = "Integer32"
_Cbftf100PauseCfgTbl_Object = MibTableColumn
cbftf100PauseCfgTbl = _Cbftf100PauseCfgTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 23),
    _Cbftf100PauseCfgTbl_Type()
)
cbftf100PauseCfgTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100PauseCfgTbl.setStatus("mandatory")


class _Cbftf100PauseStatTbl_Type(Integer32):
    """Custom type cbftf100PauseStatTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("paused", 1))
    )


_Cbftf100PauseStatTbl_Type.__name__ = "Integer32"
_Cbftf100PauseStatTbl_Object = MibTableColumn
cbftf100PauseStatTbl = _Cbftf100PauseStatTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 24),
    _Cbftf100PauseStatTbl_Type()
)
cbftf100PauseStatTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100PauseStatTbl.setStatus("mandatory")


class _Cbftf100FarEndFaultTbl_Type(Integer32):
    """Custom type cbftf100FarEndFaultTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cbftf100FarEndFaultTbl_Type.__name__ = "Integer32"
_Cbftf100FarEndFaultTbl_Object = MibTableColumn
cbftf100FarEndFaultTbl = _Cbftf100FarEndFaultTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 25),
    _Cbftf100FarEndFaultTbl_Type()
)
cbftf100FarEndFaultTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100FarEndFaultTbl.setStatus("mandatory")
_Cbftf100ConnectorTbl_Type = CpsConnector
_Cbftf100ConnectorTbl_Object = MibTableColumn
cbftf100ConnectorTbl = _Cbftf100ConnectorTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 26),
    _Cbftf100ConnectorTbl_Type()
)
cbftf100ConnectorTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100ConnectorTbl.setStatus("mandatory")


class _Cbftf100SACCfgTbl_Type(Integer32):
    """Custom type cbftf100SACCfgTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cbftf100SACCfgTbl_Type.__name__ = "Integer32"
_Cbftf100SACCfgTbl_Object = MibTableColumn
cbftf100SACCfgTbl = _Cbftf100SACCfgTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 27),
    _Cbftf100SACCfgTbl_Type()
)
cbftf100SACCfgTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100SACCfgTbl.setStatus("mandatory")


class _Cbftf100SACStatTbl_Type(Integer32):
    """Custom type cbftf100SACStatTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changed", 1),
          ("same", 2))
    )


_Cbftf100SACStatTbl_Type.__name__ = "Integer32"
_Cbftf100SACStatTbl_Object = MibTableColumn
cbftf100SACStatTbl = _Cbftf100SACStatTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 28),
    _Cbftf100SACStatTbl_Type()
)
cbftf100SACStatTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100SACStatTbl.setStatus("mandatory")


class _Cbftf100MirrorSelTbl_Type(Integer32):
    """Custom type cbftf100MirrorSelTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mirror", 1),
          ("normal", 2))
    )


_Cbftf100MirrorSelTbl_Type.__name__ = "Integer32"
_Cbftf100MirrorSelTbl_Object = MibTableColumn
cbftf100MirrorSelTbl = _Cbftf100MirrorSelTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 29),
    _Cbftf100MirrorSelTbl_Type()
)
cbftf100MirrorSelTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100MirrorSelTbl.setStatus("mandatory")


class _Cbftf100MirrorInTbl_Type(Integer32):
    """Custom type cbftf100MirrorInTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mirrorIn", 1),
          ("normal", 2))
    )


_Cbftf100MirrorInTbl_Type.__name__ = "Integer32"
_Cbftf100MirrorInTbl_Object = MibTableColumn
cbftf100MirrorInTbl = _Cbftf100MirrorInTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 30),
    _Cbftf100MirrorInTbl_Type()
)
cbftf100MirrorInTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100MirrorInTbl.setStatus("mandatory")


class _Cbftf100MirrorOutTbl_Type(Integer32):
    """Custom type cbftf100MirrorOutTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mirrorOut", 1),
          ("normal", 2))
    )


_Cbftf100MirrorOutTbl_Type.__name__ = "Integer32"
_Cbftf100MirrorOutTbl_Object = MibTableColumn
cbftf100MirrorOutTbl = _Cbftf100MirrorOutTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 31),
    _Cbftf100MirrorOutTbl_Type()
)
cbftf100MirrorOutTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100MirrorOutTbl.setStatus("mandatory")


class _Cbftf100LinkTbl_Type(Integer32):
    """Custom type cbftf100LinkTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cbftf100LinkTbl_Type.__name__ = "Integer32"
_Cbftf100LinkTbl_Object = MibTableColumn
cbftf100LinkTbl = _Cbftf100LinkTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 32),
    _Cbftf100LinkTbl_Type()
)
cbftf100LinkTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100LinkTbl.setStatus("mandatory")
_Cbftf100PortCount_Type = Integer32
_Cbftf100PortCount_Object = MibTableColumn
cbftf100PortCount = _Cbftf100PortCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 33),
    _Cbftf100PortCount_Type()
)
cbftf100PortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100PortCount.setStatus("mandatory")


class _Cbftf100LinkPassThrough_Type(Integer32):
    """Custom type cbftf100LinkPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cbftf100LinkPassThrough_Type.__name__ = "Integer32"
_Cbftf100LinkPassThrough_Object = MibTableColumn
cbftf100LinkPassThrough = _Cbftf100LinkPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 34),
    _Cbftf100LinkPassThrough_Type()
)
cbftf100LinkPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf100LinkPassThrough.setStatus("mandatory")


class _Cbftf100CacheClean_Type(Integer32):
    """Custom type cbftf100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cbftf100CacheClean_Type.__name__ = "Integer32"
_Cbftf100CacheClean_Object = MibTableColumn
cbftf100CacheClean = _Cbftf100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 35),
    _Cbftf100CacheClean_Type()
)
cbftf100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100CacheClean.setStatus("mandatory")


class _Cbftf100RedundantPath_Type(Integer32):
    """Custom type cbftf100RedundantPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cbftf100RedundantPath_Type.__name__ = "Integer32"
_Cbftf100RedundantPath_Object = MibTableColumn
cbftf100RedundantPath = _Cbftf100RedundantPath_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 11, 1, 36),
    _Cbftf100RedundantPath_Type()
)
cbftf100RedundantPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf100RedundantPath.setStatus("mandatory")
_Cetct100Table_Object = MibTable
cetct100Table = _Cetct100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12)
)
if mibBuilder.loadTexts:
    cetct100Table.setStatus("mandatory")
_Cetct100Entry_Object = MibTableRow
cetct100Entry = _Cetct100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1)
)
cetct100Entry.setIndexNames(
    (0, "MCC16-MIB", "cetct100BiaIndex"),
    (0, "MCC16-MIB", "cetct100SlotIndex"),
)
if mibBuilder.loadTexts:
    cetct100Entry.setStatus("mandatory")
_Cetct100BiaIndex_Type = Integer32
_Cetct100BiaIndex_Object = MibTableColumn
cetct100BiaIndex = _Cetct100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 1),
    _Cetct100BiaIndex_Type()
)
cetct100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100BiaIndex.setStatus("mandatory")
_Cetct100SlotIndex_Type = Integer32
_Cetct100SlotIndex_Object = MibTableColumn
cetct100SlotIndex = _Cetct100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 2),
    _Cetct100SlotIndex_Type()
)
cetct100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100SlotIndex.setStatus("mandatory")
_Cetct100Groups_Type = DisplayString
_Cetct100Groups_Object = MibTableColumn
cetct100Groups = _Cetct100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 3),
    _Cetct100Groups_Type()
)
cetct100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cetct100Groups.setStatus("mandatory")
_Cetct100MRevision_Type = Integer32
_Cetct100MRevision_Object = MibTableColumn
cetct100MRevision = _Cetct100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 4),
    _Cetct100MRevision_Type()
)
cetct100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100MRevision.setStatus("mandatory")


class _Cetct100CfgMatch_Type(Integer32):
    """Custom type cetct100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cetct100CfgMatch_Type.__name__ = "Integer32"
_Cetct100CfgMatch_Object = MibTableColumn
cetct100CfgMatch = _Cetct100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 5),
    _Cetct100CfgMatch_Type()
)
cetct100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100CfgMatch.setStatus("mandatory")
_Cetct100SerialNumber_Type = Integer32
_Cetct100SerialNumber_Object = MibTableColumn
cetct100SerialNumber = _Cetct100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 6),
    _Cetct100SerialNumber_Type()
)
cetct100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100SerialNumber.setStatus("mandatory")


class _Cetct100ConfigMode_Type(Integer32):
    """Custom type cetct100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cetct100ConfigMode_Type.__name__ = "Integer32"
_Cetct100ConfigMode_Object = MibTableColumn
cetct100ConfigMode = _Cetct100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 7),
    _Cetct100ConfigMode_Type()
)
cetct100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100ConfigMode.setStatus("mandatory")
_Cetct100FirmwareRevision_Type = Integer32
_Cetct100FirmwareRevision_Object = MibTableColumn
cetct100FirmwareRevision = _Cetct100FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 8),
    _Cetct100FirmwareRevision_Type()
)
cetct100FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100FirmwareRevision.setStatus("mandatory")


class _Cetct100TPLink_Type(Integer32):
    """Custom type cetct100TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cetct100TPLink_Type.__name__ = "Integer32"
_Cetct100TPLink_Object = MibTableColumn
cetct100TPLink = _Cetct100TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 9),
    _Cetct100TPLink_Type()
)
cetct100TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100TPLink.setStatus("mandatory")


class _Cetct100Collision_Type(Integer32):
    """Custom type cetct100Collision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cetct100Collision_Type.__name__ = "Integer32"
_Cetct100Collision_Object = MibTableColumn
cetct100Collision = _Cetct100Collision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 10),
    _Cetct100Collision_Type()
)
cetct100Collision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100Collision.setStatus("mandatory")


class _Cetct100CoaxActivity_Type(Integer32):
    """Custom type cetct100CoaxActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cetct100CoaxActivity_Type.__name__ = "Integer32"
_Cetct100CoaxActivity_Object = MibTableColumn
cetct100CoaxActivity = _Cetct100CoaxActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 11),
    _Cetct100CoaxActivity_Type()
)
cetct100CoaxActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100CoaxActivity.setStatus("mandatory")


class _Cetct100TPActivity_Type(Integer32):
    """Custom type cetct100TPActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cetct100TPActivity_Type.__name__ = "Integer32"
_Cetct100TPActivity_Object = MibTableColumn
cetct100TPActivity = _Cetct100TPActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 12),
    _Cetct100TPActivity_Type()
)
cetct100TPActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100TPActivity.setStatus("mandatory")
_Cetct100CollisionsPerMinute_Type = Integer32
_Cetct100CollisionsPerMinute_Object = MibTableColumn
cetct100CollisionsPerMinute = _Cetct100CollisionsPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 13),
    _Cetct100CollisionsPerMinute_Type()
)
cetct100CollisionsPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100CollisionsPerMinute.setStatus("mandatory")
_Cetct100CollisionsPerHour_Type = Integer32
_Cetct100CollisionsPerHour_Object = MibTableColumn
cetct100CollisionsPerHour = _Cetct100CollisionsPerHour_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 14),
    _Cetct100CollisionsPerHour_Type()
)
cetct100CollisionsPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100CollisionsPerHour.setStatus("mandatory")
_Cetct100ConnA_Type = CpsConnector
_Cetct100ConnA_Object = MibTableColumn
cetct100ConnA = _Cetct100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 15),
    _Cetct100ConnA_Type()
)
cetct100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100ConnA.setStatus("mandatory")
_Cetct100ConnB_Type = CpsConnector
_Cetct100ConnB_Object = MibTableColumn
cetct100ConnB = _Cetct100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 16),
    _Cetct100ConnB_Type()
)
cetct100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100ConnB.setStatus("mandatory")


class _Cetct100CacheClean_Type(Integer32):
    """Custom type cetct100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cetct100CacheClean_Type.__name__ = "Integer32"
_Cetct100CacheClean_Object = MibTableColumn
cetct100CacheClean = _Cetct100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 12, 1, 17),
    _Cetct100CacheClean_Type()
)
cetct100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cetct100CacheClean.setStatus("mandatory")
_Ccscf100Table_Object = MibTable
ccscf100Table = _Ccscf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13)
)
if mibBuilder.loadTexts:
    ccscf100Table.setStatus("mandatory")
_Ccscf100Entry_Object = MibTableRow
ccscf100Entry = _Ccscf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1)
)
ccscf100Entry.setIndexNames(
    (0, "MCC16-MIB", "ccscf100BiaIndex"),
    (0, "MCC16-MIB", "ccscf100SlotIndex"),
)
if mibBuilder.loadTexts:
    ccscf100Entry.setStatus("mandatory")
_Ccscf100BiaIndex_Type = Integer32
_Ccscf100BiaIndex_Object = MibTableColumn
ccscf100BiaIndex = _Ccscf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 1),
    _Ccscf100BiaIndex_Type()
)
ccscf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100BiaIndex.setStatus("mandatory")
_Ccscf100SlotIndex_Type = Integer32
_Ccscf100SlotIndex_Object = MibTableColumn
ccscf100SlotIndex = _Ccscf100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 2),
    _Ccscf100SlotIndex_Type()
)
ccscf100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100SlotIndex.setStatus("mandatory")
_Ccscf100Groups_Type = DisplayString
_Ccscf100Groups_Object = MibTableColumn
ccscf100Groups = _Ccscf100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 3),
    _Ccscf100Groups_Type()
)
ccscf100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccscf100Groups.setStatus("mandatory")
_Ccscf100MRevision_Type = Integer32
_Ccscf100MRevision_Object = MibTableColumn
ccscf100MRevision = _Ccscf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 4),
    _Ccscf100MRevision_Type()
)
ccscf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100MRevision.setStatus("mandatory")


class _Ccscf100CfgMatch_Type(Integer32):
    """Custom type ccscf100CfgMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 3),
          ("no", 2),
          ("yes", 1))
    )


_Ccscf100CfgMatch_Type.__name__ = "Integer32"
_Ccscf100CfgMatch_Object = MibTableColumn
ccscf100CfgMatch = _Ccscf100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 5),
    _Ccscf100CfgMatch_Type()
)
ccscf100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100CfgMatch.setStatus("mandatory")
_Ccscf100SerialNumber_Type = Integer32
_Ccscf100SerialNumber_Object = MibTableColumn
ccscf100SerialNumber = _Ccscf100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 6),
    _Ccscf100SerialNumber_Type()
)
ccscf100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100SerialNumber.setStatus("mandatory")


class _Ccscf100ConfigMode_Type(Integer32):
    """Custom type ccscf100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Ccscf100ConfigMode_Type.__name__ = "Integer32"
_Ccscf100ConfigMode_Object = MibTableColumn
ccscf100ConfigMode = _Ccscf100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 7),
    _Ccscf100ConfigMode_Type()
)
ccscf100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100ConfigMode.setStatus("mandatory")


class _Ccscf100FiberLink_Type(Integer32):
    """Custom type ccscf100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Ccscf100FiberLink_Type.__name__ = "Integer32"
_Ccscf100FiberLink_Object = MibTableColumn
ccscf100FiberLink = _Ccscf100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 8),
    _Ccscf100FiberLink_Type()
)
ccscf100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100FiberLink.setStatus("mandatory")


class _Ccscf100CopperLink_Type(Integer32):
    """Custom type ccscf100CopperLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Ccscf100CopperLink_Type.__name__ = "Integer32"
_Ccscf100CopperLink_Object = MibTableColumn
ccscf100CopperLink = _Ccscf100CopperLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 9),
    _Ccscf100CopperLink_Type()
)
ccscf100CopperLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100CopperLink.setStatus("mandatory")


class _Ccscf100AISFiber_Type(Integer32):
    """Custom type ccscf100AISFiber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_Ccscf100AISFiber_Type.__name__ = "Integer32"
_Ccscf100AISFiber_Object = MibTableColumn
ccscf100AISFiber = _Ccscf100AISFiber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 10),
    _Ccscf100AISFiber_Type()
)
ccscf100AISFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100AISFiber.setStatus("mandatory")


class _Ccscf100AISCopper_Type(Integer32):
    """Custom type ccscf100AISCopper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 2))
    )


_Ccscf100AISCopper_Type.__name__ = "Integer32"
_Ccscf100AISCopper_Object = MibTableColumn
ccscf100AISCopper = _Ccscf100AISCopper_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 11),
    _Ccscf100AISCopper_Type()
)
ccscf100AISCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100AISCopper.setStatus("mandatory")


class _Ccscf100DS3LineBuildout_Type(Integer32):
    """Custom type ccscf100DS3LineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boost", 1),
          ("normal", 2),
          ("notSupported", 3))
    )


_Ccscf100DS3LineBuildout_Type.__name__ = "Integer32"
_Ccscf100DS3LineBuildout_Object = MibTableColumn
ccscf100DS3LineBuildout = _Ccscf100DS3LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 12),
    _Ccscf100DS3LineBuildout_Type()
)
ccscf100DS3LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccscf100DS3LineBuildout.setStatus("mandatory")


class _Ccscf100E3DS3_Type(Integer32):
    """Custom type ccscf100E3DS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 2),
          ("e3", 1))
    )


_Ccscf100E3DS3_Type.__name__ = "Integer32"
_Ccscf100E3DS3_Object = MibTableColumn
ccscf100E3DS3 = _Ccscf100E3DS3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 13),
    _Ccscf100E3DS3_Type()
)
ccscf100E3DS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100E3DS3.setStatus("mandatory")


class _Ccscf100CopperLoopback_Type(Integer32):
    """Custom type ccscf100CopperLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Ccscf100CopperLoopback_Type.__name__ = "Integer32"
_Ccscf100CopperLoopback_Object = MibTableColumn
ccscf100CopperLoopback = _Ccscf100CopperLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 14),
    _Ccscf100CopperLoopback_Type()
)
ccscf100CopperLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccscf100CopperLoopback.setStatus("mandatory")


class _Ccscf100FiberLoopback_Type(Integer32):
    """Custom type ccscf100FiberLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Ccscf100FiberLoopback_Type.__name__ = "Integer32"
_Ccscf100FiberLoopback_Object = MibTableColumn
ccscf100FiberLoopback = _Ccscf100FiberLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 15),
    _Ccscf100FiberLoopback_Type()
)
ccscf100FiberLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccscf100FiberLoopback.setStatus("mandatory")
_Ccscf100ConnA_Type = CpsConnector
_Ccscf100ConnA_Object = MibTableColumn
ccscf100ConnA = _Ccscf100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 16),
    _Ccscf100ConnA_Type()
)
ccscf100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100ConnA.setStatus("mandatory")
_Ccscf100ConnB_Type = CpsConnector
_Ccscf100ConnB_Object = MibTableColumn
ccscf100ConnB = _Ccscf100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 17),
    _Ccscf100ConnB_Type()
)
ccscf100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100ConnB.setStatus("mandatory")


class _Ccscf100CacheClean_Type(Integer32):
    """Custom type ccscf100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Ccscf100CacheClean_Type.__name__ = "Integer32"
_Ccscf100CacheClean_Object = MibTableColumn
ccscf100CacheClean = _Ccscf100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 13, 1, 18),
    _Ccscf100CacheClean_Type()
)
ccscf100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccscf100CacheClean.setStatus("mandatory")
_Cfetf105Table_Object = MibTable
cfetf105Table = _Cfetf105Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14)
)
if mibBuilder.loadTexts:
    cfetf105Table.setStatus("mandatory")
_Cfetf105Entry_Object = MibTableRow
cfetf105Entry = _Cfetf105Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1)
)
cfetf105Entry.setIndexNames(
    (0, "MCC16-MIB", "cfetf105BiaIndex"),
    (0, "MCC16-MIB", "cfetf105SlotIndex"),
)
if mibBuilder.loadTexts:
    cfetf105Entry.setStatus("mandatory")
_Cfetf105BiaIndex_Type = Integer32
_Cfetf105BiaIndex_Object = MibTableColumn
cfetf105BiaIndex = _Cfetf105BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 1),
    _Cfetf105BiaIndex_Type()
)
cfetf105BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105BiaIndex.setStatus("mandatory")
_Cfetf105SlotIndex_Type = Integer32
_Cfetf105SlotIndex_Object = MibTableColumn
cfetf105SlotIndex = _Cfetf105SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 2),
    _Cfetf105SlotIndex_Type()
)
cfetf105SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105SlotIndex.setStatus("mandatory")
_Cfetf105Groups_Type = DisplayString
_Cfetf105Groups_Object = MibTableColumn
cfetf105Groups = _Cfetf105Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 3),
    _Cfetf105Groups_Type()
)
cfetf105Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf105Groups.setStatus("mandatory")
_Cfetf105MRevision_Type = Integer32
_Cfetf105MRevision_Object = MibTableColumn
cfetf105MRevision = _Cfetf105MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 4),
    _Cfetf105MRevision_Type()
)
cfetf105MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105MRevision.setStatus("mandatory")


class _Cfetf105CfgMatch_Type(Integer32):
    """Custom type cfetf105CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cfetf105CfgMatch_Type.__name__ = "Integer32"
_Cfetf105CfgMatch_Object = MibTableColumn
cfetf105CfgMatch = _Cfetf105CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 5),
    _Cfetf105CfgMatch_Type()
)
cfetf105CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105CfgMatch.setStatus("mandatory")
_Cfetf105SerialNumber_Type = Integer32
_Cfetf105SerialNumber_Object = MibTableColumn
cfetf105SerialNumber = _Cfetf105SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 6),
    _Cfetf105SerialNumber_Type()
)
cfetf105SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105SerialNumber.setStatus("mandatory")
_Cfetf105ConnA_Type = CpsConnector
_Cfetf105ConnA_Object = MibTableColumn
cfetf105ConnA = _Cfetf105ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 7),
    _Cfetf105ConnA_Type()
)
cfetf105ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105ConnA.setStatus("mandatory")
_Cfetf105ConnB_Type = CpsConnector
_Cfetf105ConnB_Object = MibTableColumn
cfetf105ConnB = _Cfetf105ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 8),
    _Cfetf105ConnB_Type()
)
cfetf105ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105ConnB.setStatus("mandatory")


class _Cfetf105TPLink_Type(Integer32):
    """Custom type cfetf105TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cfetf105TPLink_Type.__name__ = "Integer32"
_Cfetf105TPLink_Object = MibTableColumn
cfetf105TPLink = _Cfetf105TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 9),
    _Cfetf105TPLink_Type()
)
cfetf105TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105TPLink.setStatus("mandatory")


class _Cfetf105FiberLink_Type(Integer32):
    """Custom type cfetf105FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cfetf105FiberLink_Type.__name__ = "Integer32"
_Cfetf105FiberLink_Object = MibTableColumn
cfetf105FiberLink = _Cfetf105FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 10),
    _Cfetf105FiberLink_Type()
)
cfetf105FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105FiberLink.setStatus("mandatory")


class _Cfetf105AutoNegot_Type(Integer32):
    """Custom type cfetf105AutoNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cfetf105AutoNegot_Type.__name__ = "Integer32"
_Cfetf105AutoNegot_Object = MibTableColumn
cfetf105AutoNegot = _Cfetf105AutoNegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 11),
    _Cfetf105AutoNegot_Type()
)
cfetf105AutoNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf105AutoNegot.setStatus("mandatory")


class _Cfetf105LinkPassThrough_Type(Integer32):
    """Custom type cfetf105LinkPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cfetf105LinkPassThrough_Type.__name__ = "Integer32"
_Cfetf105LinkPassThrough_Object = MibTableColumn
cfetf105LinkPassThrough = _Cfetf105LinkPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 12),
    _Cfetf105LinkPassThrough_Type()
)
cfetf105LinkPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf105LinkPassThrough.setStatus("mandatory")


class _Cfetf105AutoCross_Type(Integer32):
    """Custom type cfetf105AutoCross based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cfetf105AutoCross_Type.__name__ = "Integer32"
_Cfetf105AutoCross_Object = MibTableColumn
cfetf105AutoCross = _Cfetf105AutoCross_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 13),
    _Cfetf105AutoCross_Type()
)
cfetf105AutoCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf105AutoCross.setStatus("mandatory")


class _Cfetf105TPActivity_Type(Integer32):
    """Custom type cfetf105TPActivity based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Cfetf105TPActivity_Type.__name__ = "Integer32"
_Cfetf105TPActivity_Object = MibTableColumn
cfetf105TPActivity = _Cfetf105TPActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 14),
    _Cfetf105TPActivity_Type()
)
cfetf105TPActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105TPActivity.setStatus("mandatory")


class _Cfetf105FiberActivity_Type(Integer32):
    """Custom type cfetf105FiberActivity based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Cfetf105FiberActivity_Type.__name__ = "Integer32"
_Cfetf105FiberActivity_Object = MibTableColumn
cfetf105FiberActivity = _Cfetf105FiberActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 15),
    _Cfetf105FiberActivity_Type()
)
cfetf105FiberActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105FiberActivity.setStatus("mandatory")


class _Cfetf105ConfigMode_Type(Integer32):
    """Custom type cfetf105ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cfetf105ConfigMode_Type.__name__ = "Integer32"
_Cfetf105ConfigMode_Object = MibTableColumn
cfetf105ConfigMode = _Cfetf105ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 16),
    _Cfetf105ConfigMode_Type()
)
cfetf105ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105ConfigMode.setStatus("mandatory")


class _Cfetf105CacheClean_Type(Integer32):
    """Custom type cfetf105CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cfetf105CacheClean_Type.__name__ = "Integer32"
_Cfetf105CacheClean_Object = MibTableColumn
cfetf105CacheClean = _Cfetf105CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 14, 1, 17),
    _Cfetf105CacheClean_Type()
)
cfetf105CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf105CacheClean.setStatus("mandatory")
_Smacf100PTable_Object = MibTable
smacf100PTable = _Smacf100PTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15)
)
if mibBuilder.loadTexts:
    smacf100PTable.setStatus("mandatory")
_Smacf100PEntry_Object = MibTableRow
smacf100PEntry = _Smacf100PEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1)
)
smacf100PEntry.setIndexNames(
    (0, "MCC16-MIB", "smacf100PSubDeviceIndex"),
    (0, "MCC16-MIB", "smacf100PBiaIndex"),
    (0, "MCC16-MIB", "smacf100PSlotIndex"),
)
if mibBuilder.loadTexts:
    smacf100PEntry.setStatus("mandatory")
_Smacf100PSubDeviceIndex_Type = Integer32
_Smacf100PSubDeviceIndex_Object = MibTableColumn
smacf100PSubDeviceIndex = _Smacf100PSubDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 1),
    _Smacf100PSubDeviceIndex_Type()
)
smacf100PSubDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PSubDeviceIndex.setStatus("mandatory")
_Smacf100PBiaIndex_Type = Integer32
_Smacf100PBiaIndex_Object = MibTableColumn
smacf100PBiaIndex = _Smacf100PBiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 2),
    _Smacf100PBiaIndex_Type()
)
smacf100PBiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PBiaIndex.setStatus("mandatory")
_Smacf100PSlotIndex_Type = Integer32
_Smacf100PSlotIndex_Object = MibTableColumn
smacf100PSlotIndex = _Smacf100PSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 3),
    _Smacf100PSlotIndex_Type()
)
smacf100PSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PSlotIndex.setStatus("mandatory")
_Smacf100PGroups_Type = DisplayString
_Smacf100PGroups_Object = MibTableColumn
smacf100PGroups = _Smacf100PGroups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 4),
    _Smacf100PGroups_Type()
)
smacf100PGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PGroups.setStatus("mandatory")


class _Smacf100PCfgMatch_Type(Integer32):
    """Custom type smacf100PCfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Smacf100PCfgMatch_Type.__name__ = "Integer32"
_Smacf100PCfgMatch_Object = MibTableColumn
smacf100PCfgMatch = _Smacf100PCfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 5),
    _Smacf100PCfgMatch_Type()
)
smacf100PCfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PCfgMatch.setStatus("mandatory")
_Smacf100PConnA_Type = CpsConnector
_Smacf100PConnA_Object = MibTableColumn
smacf100PConnA = _Smacf100PConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 6),
    _Smacf100PConnA_Type()
)
smacf100PConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PConnA.setStatus("mandatory")


class _Smacf100PLink_Type(Integer32):
    """Custom type smacf100PLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Smacf100PLink_Type.__name__ = "Integer32"
_Smacf100PLink_Object = MibTableColumn
smacf100PLink = _Smacf100PLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 7),
    _Smacf100PLink_Type()
)
smacf100PLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PLink.setStatus("mandatory")


class _Smacf100P100Mbps_Type(Integer32):
    """Custom type smacf100P100Mbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mbps10", 2),
          ("mbps100", 1))
    )


_Smacf100P100Mbps_Type.__name__ = "Integer32"
_Smacf100P100Mbps_Object = MibTableColumn
smacf100P100Mbps = _Smacf100P100Mbps_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 8),
    _Smacf100P100Mbps_Type()
)
smacf100P100Mbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100P100Mbps.setStatus("mandatory")


class _Smacf100PFullDuplex_Type(Integer32):
    """Custom type smacf100PFullDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("negotiating", 3))
    )


_Smacf100PFullDuplex_Type.__name__ = "Integer32"
_Smacf100PFullDuplex_Object = MibTableColumn
smacf100PFullDuplex = _Smacf100PFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 9),
    _Smacf100PFullDuplex_Type()
)
smacf100PFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PFullDuplex.setStatus("mandatory")


class _Smacf100PSACStat_Type(Integer32):
    """Custom type smacf100PSACStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changed", 1),
          ("same", 2))
    )


_Smacf100PSACStat_Type.__name__ = "Integer32"
_Smacf100PSACStat_Object = MibTableColumn
smacf100PSACStat = _Smacf100PSACStat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 10),
    _Smacf100PSACStat_Type()
)
smacf100PSACStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PSACStat.setStatus("mandatory")


class _Smacf100PEnabled_Type(Integer32):
    """Custom type smacf100PEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Smacf100PEnabled_Type.__name__ = "Integer32"
_Smacf100PEnabled_Object = MibTableColumn
smacf100PEnabled = _Smacf100PEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 11),
    _Smacf100PEnabled_Type()
)
smacf100PEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PEnabled.setStatus("mandatory")


class _Smacf100PAutoNegot_Type(Integer32):
    """Custom type smacf100PAutoNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Smacf100PAutoNegot_Type.__name__ = "Integer32"
_Smacf100PAutoNegot_Object = MibTableColumn
smacf100PAutoNegot = _Smacf100PAutoNegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 12),
    _Smacf100PAutoNegot_Type()
)
smacf100PAutoNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PAutoNegot.setStatus("mandatory")


class _Smacf100PAdv10HDX_Type(Integer32):
    """Custom type smacf100PAdv10HDX based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Smacf100PAdv10HDX_Type.__name__ = "Integer32"
_Smacf100PAdv10HDX_Object = MibTableColumn
smacf100PAdv10HDX = _Smacf100PAdv10HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 13),
    _Smacf100PAdv10HDX_Type()
)
smacf100PAdv10HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PAdv10HDX.setStatus("mandatory")


class _Smacf100PAdv10FDX_Type(Integer32):
    """Custom type smacf100PAdv10FDX based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Smacf100PAdv10FDX_Type.__name__ = "Integer32"
_Smacf100PAdv10FDX_Object = MibTableColumn
smacf100PAdv10FDX = _Smacf100PAdv10FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 14),
    _Smacf100PAdv10FDX_Type()
)
smacf100PAdv10FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PAdv10FDX.setStatus("mandatory")


class _Smacf100PAdv100HDX_Type(Integer32):
    """Custom type smacf100PAdv100HDX based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Smacf100PAdv100HDX_Type.__name__ = "Integer32"
_Smacf100PAdv100HDX_Object = MibTableColumn
smacf100PAdv100HDX = _Smacf100PAdv100HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 15),
    _Smacf100PAdv100HDX_Type()
)
smacf100PAdv100HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PAdv100HDX.setStatus("mandatory")


class _Smacf100PAdv100FDX_Type(Integer32):
    """Custom type smacf100PAdv100FDX based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Smacf100PAdv100FDX_Type.__name__ = "Integer32"
_Smacf100PAdv100FDX_Object = MibTableColumn
smacf100PAdv100FDX = _Smacf100PAdv100FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 16),
    _Smacf100PAdv100FDX_Type()
)
smacf100PAdv100FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PAdv100FDX.setStatus("mandatory")


class _Smacf100PSTPState_Type(Integer32):
    """Custom type smacf100PSTPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("disabled", 2),
          ("forwarding", 6),
          ("learning", 5),
          ("listening", 4),
          ("notSupported", 1))
    )


_Smacf100PSTPState_Type.__name__ = "Integer32"
_Smacf100PSTPState_Object = MibTableColumn
smacf100PSTPState = _Smacf100PSTPState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 17),
    _Smacf100PSTPState_Type()
)
smacf100PSTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PSTPState.setStatus("mandatory")
_Smacf100PLastMAC_Type = MacAddress
_Smacf100PLastMAC_Object = MibTableColumn
smacf100PLastMAC = _Smacf100PLastMAC_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 18),
    _Smacf100PLastMAC_Type()
)
smacf100PLastMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PLastMAC.setStatus("mandatory")


class _Smacf100PFarEndFaultCfg_Type(Integer32):
    """Custom type smacf100PFarEndFaultCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Smacf100PFarEndFaultCfg_Type.__name__ = "Integer32"
_Smacf100PFarEndFaultCfg_Object = MibTableColumn
smacf100PFarEndFaultCfg = _Smacf100PFarEndFaultCfg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 19),
    _Smacf100PFarEndFaultCfg_Type()
)
smacf100PFarEndFaultCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PFarEndFaultCfg.setStatus("mandatory")


class _Smacf100PFarEndFaultStat_Type(Integer32):
    """Custom type smacf100PFarEndFaultStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Smacf100PFarEndFaultStat_Type.__name__ = "Integer32"
_Smacf100PFarEndFaultStat_Object = MibTableColumn
smacf100PFarEndFaultStat = _Smacf100PFarEndFaultStat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 20),
    _Smacf100PFarEndFaultStat_Type()
)
smacf100PFarEndFaultStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PFarEndFaultStat.setStatus("mandatory")
_Smacf100PTxOctets_Type = Integer32
_Smacf100PTxOctets_Object = MibTableColumn
smacf100PTxOctets = _Smacf100PTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 21),
    _Smacf100PTxOctets_Type()
)
smacf100PTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxOctets.setStatus("mandatory")
_Smacf100PWrapTxOctets_Type = Integer32
_Smacf100PWrapTxOctets_Object = MibTableColumn
smacf100PWrapTxOctets = _Smacf100PWrapTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 22),
    _Smacf100PWrapTxOctets_Type()
)
smacf100PWrapTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PWrapTxOctets.setStatus("mandatory")
_Smacf100PRxOctets_Type = Integer32
_Smacf100PRxOctets_Object = MibTableColumn
smacf100PRxOctets = _Smacf100PRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 23),
    _Smacf100PRxOctets_Type()
)
smacf100PRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxOctets.setStatus("mandatory")
_Smacf100PWrapRxOctets_Type = Integer32
_Smacf100PWrapRxOctets_Object = MibTableColumn
smacf100PWrapRxOctets = _Smacf100PWrapRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 24),
    _Smacf100PWrapRxOctets_Type()
)
smacf100PWrapRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PWrapRxOctets.setStatus("mandatory")


class _Smacf100PSACCfg_Type(Integer32):
    """Custom type smacf100PSACCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Smacf100PSACCfg_Type.__name__ = "Integer32"
_Smacf100PSACCfg_Object = MibTableColumn
smacf100PSACCfg = _Smacf100PSACCfg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 25),
    _Smacf100PSACCfg_Type()
)
smacf100PSACCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PSACCfg.setStatus("mandatory")


class _Smacf100PBlockMgmt_Type(Integer32):
    """Custom type smacf100PBlockMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_Smacf100PBlockMgmt_Type.__name__ = "Integer32"
_Smacf100PBlockMgmt_Object = MibTableColumn
smacf100PBlockMgmt = _Smacf100PBlockMgmt_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 26),
    _Smacf100PBlockMgmt_Type()
)
smacf100PBlockMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PBlockMgmt.setStatus("mandatory")


class _Smacf100PBlockPort_Type(Integer32):
    """Custom type smacf100PBlockPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_Smacf100PBlockPort_Type.__name__ = "Integer32"
_Smacf100PBlockPort_Object = MibTableColumn
smacf100PBlockPort = _Smacf100PBlockPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 27),
    _Smacf100PBlockPort_Type()
)
smacf100PBlockPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PBlockPort.setStatus("mandatory")
_Smacf100PTxDropPkts_Type = Integer32
_Smacf100PTxDropPkts_Object = MibTableColumn
smacf100PTxDropPkts = _Smacf100PTxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 28),
    _Smacf100PTxDropPkts_Type()
)
smacf100PTxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxDropPkts.setStatus("mandatory")
_Smacf100PTxBroadcastPkts_Type = Integer32
_Smacf100PTxBroadcastPkts_Object = MibTableColumn
smacf100PTxBroadcastPkts = _Smacf100PTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 29),
    _Smacf100PTxBroadcastPkts_Type()
)
smacf100PTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxBroadcastPkts.setStatus("mandatory")
_Smacf100PTxMulticastPkts_Type = Integer32
_Smacf100PTxMulticastPkts_Object = MibTableColumn
smacf100PTxMulticastPkts = _Smacf100PTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 30),
    _Smacf100PTxMulticastPkts_Type()
)
smacf100PTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxMulticastPkts.setStatus("mandatory")
_Smacf100PTxUnicastPkts_Type = Integer32
_Smacf100PTxUnicastPkts_Object = MibTableColumn
smacf100PTxUnicastPkts = _Smacf100PTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 31),
    _Smacf100PTxUnicastPkts_Type()
)
smacf100PTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxUnicastPkts.setStatus("mandatory")
_Smacf100PTxCollisions_Type = Integer32
_Smacf100PTxCollisions_Object = MibTableColumn
smacf100PTxCollisions = _Smacf100PTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 32),
    _Smacf100PTxCollisions_Type()
)
smacf100PTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxCollisions.setStatus("mandatory")
_Smacf100PTxSingleCollision_Type = Integer32
_Smacf100PTxSingleCollision_Object = MibTableColumn
smacf100PTxSingleCollision = _Smacf100PTxSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 33),
    _Smacf100PTxSingleCollision_Type()
)
smacf100PTxSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxSingleCollision.setStatus("mandatory")
_Smacf100PTxMultipleCollision_Type = Integer32
_Smacf100PTxMultipleCollision_Object = MibTableColumn
smacf100PTxMultipleCollision = _Smacf100PTxMultipleCollision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 34),
    _Smacf100PTxMultipleCollision_Type()
)
smacf100PTxMultipleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxMultipleCollision.setStatus("mandatory")
_Smacf100PTxDeferredTransmit_Type = Integer32
_Smacf100PTxDeferredTransmit_Object = MibTableColumn
smacf100PTxDeferredTransmit = _Smacf100PTxDeferredTransmit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 35),
    _Smacf100PTxDeferredTransmit_Type()
)
smacf100PTxDeferredTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxDeferredTransmit.setStatus("mandatory")
_Smacf100PTxLateCollision_Type = Integer32
_Smacf100PTxLateCollision_Object = MibTableColumn
smacf100PTxLateCollision = _Smacf100PTxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 36),
    _Smacf100PTxLateCollision_Type()
)
smacf100PTxLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxLateCollision.setStatus("mandatory")
_Smacf100PTxExcessiveCollision_Type = Integer32
_Smacf100PTxExcessiveCollision_Object = MibTableColumn
smacf100PTxExcessiveCollision = _Smacf100PTxExcessiveCollision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 37),
    _Smacf100PTxExcessiveCollision_Type()
)
smacf100PTxExcessiveCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxExcessiveCollision.setStatus("mandatory")
_Smacf100PTxFrameInDisc_Type = Integer32
_Smacf100PTxFrameInDisc_Object = MibTableColumn
smacf100PTxFrameInDisc = _Smacf100PTxFrameInDisc_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 38),
    _Smacf100PTxFrameInDisc_Type()
)
smacf100PTxFrameInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PTxFrameInDisc.setStatus("mandatory")


class _Smacf100PTxPausePkts_Type(Integer32):
    """Custom type smacf100PTxPausePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Smacf100PTxPausePkts_Type.__name__ = "Integer32"
_Smacf100PTxPausePkts_Object = MibTableColumn
smacf100PTxPausePkts = _Smacf100PTxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 39),
    _Smacf100PTxPausePkts_Type()
)
smacf100PTxPausePkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PTxPausePkts.setStatus("mandatory")
_Smacf100PRxUndersizePkts_Type = Integer32
_Smacf100PRxUndersizePkts_Object = MibTableColumn
smacf100PRxUndersizePkts = _Smacf100PRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 40),
    _Smacf100PRxUndersizePkts_Type()
)
smacf100PRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxUndersizePkts.setStatus("mandatory")


class _Smacf100PRxPausePkts_Type(Integer32):
    """Custom type smacf100PRxPausePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Smacf100PRxPausePkts_Type.__name__ = "Integer32"
_Smacf100PRxPausePkts_Object = MibTableColumn
smacf100PRxPausePkts = _Smacf100PRxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 41),
    _Smacf100PRxPausePkts_Type()
)
smacf100PRxPausePkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PRxPausePkts.setStatus("mandatory")
_Smacf100PPkts64Octets_Type = Integer32
_Smacf100PPkts64Octets_Object = MibTableColumn
smacf100PPkts64Octets = _Smacf100PPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 42),
    _Smacf100PPkts64Octets_Type()
)
smacf100PPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PPkts64Octets.setStatus("mandatory")
_Smacf100PPkts65to127Octets_Type = Integer32
_Smacf100PPkts65to127Octets_Object = MibTableColumn
smacf100PPkts65to127Octets = _Smacf100PPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 43),
    _Smacf100PPkts65to127Octets_Type()
)
smacf100PPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PPkts65to127Octets.setStatus("mandatory")
_Smacf100PPkts128to255Octets_Type = Integer32
_Smacf100PPkts128to255Octets_Object = MibTableColumn
smacf100PPkts128to255Octets = _Smacf100PPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 44),
    _Smacf100PPkts128to255Octets_Type()
)
smacf100PPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PPkts128to255Octets.setStatus("mandatory")
_Smacf100PPkts256to511Octets_Type = Integer32
_Smacf100PPkts256to511Octets_Object = MibTableColumn
smacf100PPkts256to511Octets = _Smacf100PPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 45),
    _Smacf100PPkts256to511Octets_Type()
)
smacf100PPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PPkts256to511Octets.setStatus("mandatory")
_Smacf100PPkts512to1023Octets_Type = Integer32
_Smacf100PPkts512to1023Octets_Object = MibTableColumn
smacf100PPkts512to1023Octets = _Smacf100PPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 46),
    _Smacf100PPkts512to1023Octets_Type()
)
smacf100PPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PPkts512to1023Octets.setStatus("mandatory")
_Smacf100PPkts1024to1522Octets_Type = Integer32
_Smacf100PPkts1024to1522Octets_Object = MibTableColumn
smacf100PPkts1024to1522Octets = _Smacf100PPkts1024to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 47),
    _Smacf100PPkts1024to1522Octets_Type()
)
smacf100PPkts1024to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PPkts1024to1522Octets.setStatus("mandatory")


class _Smacf100PRxOversizePkts_Type(Integer32):
    """Custom type smacf100PRxOversizePkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Smacf100PRxOversizePkts_Type.__name__ = "Integer32"
_Smacf100PRxOversizePkts_Object = MibTableColumn
smacf100PRxOversizePkts = _Smacf100PRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 48),
    _Smacf100PRxOversizePkts_Type()
)
smacf100PRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxOversizePkts.setStatus("mandatory")
_Smacf100PRxJabbers_Type = Integer32
_Smacf100PRxJabbers_Object = MibTableColumn
smacf100PRxJabbers = _Smacf100PRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 49),
    _Smacf100PRxJabbers_Type()
)
smacf100PRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxJabbers.setStatus("mandatory")
_Smacf100PRxAlignmentErrors_Type = Integer32
_Smacf100PRxAlignmentErrors_Object = MibTableColumn
smacf100PRxAlignmentErrors = _Smacf100PRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 50),
    _Smacf100PRxAlignmentErrors_Type()
)
smacf100PRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxAlignmentErrors.setStatus("mandatory")
_Smacf100PRxFCSErrors_Type = Integer32
_Smacf100PRxFCSErrors_Object = MibTableColumn
smacf100PRxFCSErrors = _Smacf100PRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 51),
    _Smacf100PRxFCSErrors_Type()
)
smacf100PRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxFCSErrors.setStatus("mandatory")
_Smacf100PRxGoodOctets_Type = Integer32
_Smacf100PRxGoodOctets_Object = MibTableColumn
smacf100PRxGoodOctets = _Smacf100PRxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 52),
    _Smacf100PRxGoodOctets_Type()
)
smacf100PRxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxGoodOctets.setStatus("mandatory")
_Smacf100PWrapRxGoodOctets_Type = Integer32
_Smacf100PWrapRxGoodOctets_Object = MibTableColumn
smacf100PWrapRxGoodOctets = _Smacf100PWrapRxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 53),
    _Smacf100PWrapRxGoodOctets_Type()
)
smacf100PWrapRxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PWrapRxGoodOctets.setStatus("mandatory")
_Smacf100PRxDropPkts_Type = Integer32
_Smacf100PRxDropPkts_Object = MibTableColumn
smacf100PRxDropPkts = _Smacf100PRxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 54),
    _Smacf100PRxDropPkts_Type()
)
smacf100PRxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxDropPkts.setStatus("mandatory")
_Smacf100PRxUnicastPkts_Type = Integer32
_Smacf100PRxUnicastPkts_Object = MibTableColumn
smacf100PRxUnicastPkts = _Smacf100PRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 55),
    _Smacf100PRxUnicastPkts_Type()
)
smacf100PRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxUnicastPkts.setStatus("mandatory")
_Smacf100PRxMulticastPkts_Type = Integer32
_Smacf100PRxMulticastPkts_Object = MibTableColumn
smacf100PRxMulticastPkts = _Smacf100PRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 56),
    _Smacf100PRxMulticastPkts_Type()
)
smacf100PRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxMulticastPkts.setStatus("mandatory")
_Smacf100PRxBroadcastPkts_Type = Integer32
_Smacf100PRxBroadcastPkts_Object = MibTableColumn
smacf100PRxBroadcastPkts = _Smacf100PRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 57),
    _Smacf100PRxBroadcastPkts_Type()
)
smacf100PRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxBroadcastPkts.setStatus("mandatory")
_Smacf100PRxSAChanges_Type = Integer32
_Smacf100PRxSAChanges_Object = MibTableColumn
smacf100PRxSAChanges = _Smacf100PRxSAChanges_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 58),
    _Smacf100PRxSAChanges_Type()
)
smacf100PRxSAChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxSAChanges.setStatus("mandatory")
_Smacf100PRxFragments_Type = Integer32
_Smacf100PRxFragments_Object = MibTableColumn
smacf100PRxFragments = _Smacf100PRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 59),
    _Smacf100PRxFragments_Type()
)
smacf100PRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxFragments.setStatus("mandatory")
_Smacf100PRxExcessSizeDisc_Type = Integer32
_Smacf100PRxExcessSizeDisc_Object = MibTableColumn
smacf100PRxExcessSizeDisc = _Smacf100PRxExcessSizeDisc_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 60),
    _Smacf100PRxExcessSizeDisc_Type()
)
smacf100PRxExcessSizeDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxExcessSizeDisc.setStatus("mandatory")
_Smacf100PRxSymbolError_Type = Integer32
_Smacf100PRxSymbolError_Object = MibTableColumn
smacf100PRxSymbolError = _Smacf100PRxSymbolError_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 61),
    _Smacf100PRxSymbolError_Type()
)
smacf100PRxSymbolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PRxSymbolError.setStatus("mandatory")
_Smacf100PQosPriority_Type = Integer32
_Smacf100PQosPriority_Object = MibTableColumn
smacf100PQosPriority = _Smacf100PQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 62),
    _Smacf100PQosPriority_Type()
)
smacf100PQosPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PQosPriority.setStatus("mandatory")
_Smacf100PQosPause_Type = Integer32
_Smacf100PQosPause_Object = MibTableColumn
smacf100PQosPause = _Smacf100PQosPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 63),
    _Smacf100PQosPause_Type()
)
smacf100PQosPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PQosPause.setStatus("mandatory")
_Smacf100PAdvPause_Type = Integer32
_Smacf100PAdvPause_Object = MibTableColumn
smacf100PAdvPause = _Smacf100PAdvPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 64),
    _Smacf100PAdvPause_Type()
)
smacf100PAdvPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100PAdvPause.setStatus("mandatory")


class _Smacf100PCacheClean_Type(Integer32):
    """Custom type smacf100PCacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Smacf100PCacheClean_Type.__name__ = "Integer32"
_Smacf100PCacheClean_Object = MibTableColumn
smacf100PCacheClean = _Smacf100PCacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 15, 1, 65),
    _Smacf100PCacheClean_Type()
)
smacf100PCacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100PCacheClean.setStatus("mandatory")
_Cpsld100Table_Object = MibTable
cpsld100Table = _Cpsld100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 16)
)
if mibBuilder.loadTexts:
    cpsld100Table.setStatus("mandatory")
_Cpsld100Entry_Object = MibTableRow
cpsld100Entry = _Cpsld100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 16, 1)
)
cpsld100Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsld100BiaIndex"),
    (0, "MCC16-MIB", "cpsld100SlotIndex"),
)
if mibBuilder.loadTexts:
    cpsld100Entry.setStatus("mandatory")
_Cpsld100BiaIndex_Type = Integer32
_Cpsld100BiaIndex_Object = MibTableColumn
cpsld100BiaIndex = _Cpsld100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 16, 1, 1),
    _Cpsld100BiaIndex_Type()
)
cpsld100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsld100BiaIndex.setStatus("mandatory")
_Cpsld100SlotIndex_Type = Integer32
_Cpsld100SlotIndex_Object = MibTableColumn
cpsld100SlotIndex = _Cpsld100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 16, 1, 2),
    _Cpsld100SlotIndex_Type()
)
cpsld100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsld100SlotIndex.setStatus("mandatory")
_Cpsld100SerialNumber_Type = Integer32
_Cpsld100SerialNumber_Object = MibTableColumn
cpsld100SerialNumber = _Cpsld100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 16, 1, 3),
    _Cpsld100SerialNumber_Type()
)
cpsld100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsld100SerialNumber.setStatus("mandatory")
_Cpsld100MRevision_Type = Integer32
_Cpsld100MRevision_Object = MibTableColumn
cpsld100MRevision = _Cpsld100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 16, 1, 4),
    _Cpsld100MRevision_Type()
)
cpsld100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsld100MRevision.setStatus("mandatory")


class _Cpsld100Ps1Power_Type(Integer32):
    """Custom type cpsld100Ps1Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 3),
          ("off", 2),
          ("on", 1))
    )


_Cpsld100Ps1Power_Type.__name__ = "Integer32"
_Cpsld100Ps1Power_Object = MibTableColumn
cpsld100Ps1Power = _Cpsld100Ps1Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 16, 1, 5),
    _Cpsld100Ps1Power_Type()
)
cpsld100Ps1Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsld100Ps1Power.setStatus("mandatory")


class _Cpsld100Ps1InUse_Type(Integer32):
    """Custom type cpsld100Ps1InUse based on Integer32"""
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
          ("notInstalled", 3),
          ("yes", 1))
    )


_Cpsld100Ps1InUse_Type.__name__ = "Integer32"
_Cpsld100Ps1InUse_Object = MibTableColumn
cpsld100Ps1InUse = _Cpsld100Ps1InUse_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 16, 1, 6),
    _Cpsld100Ps1InUse_Type()
)
cpsld100Ps1InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsld100Ps1InUse.setStatus("mandatory")


class _Cpsld100Ps2Power_Type(Integer32):
    """Custom type cpsld100Ps2Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 3),
          ("off", 2),
          ("on", 1))
    )


_Cpsld100Ps2Power_Type.__name__ = "Integer32"
_Cpsld100Ps2Power_Object = MibTableColumn
cpsld100Ps2Power = _Cpsld100Ps2Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 16, 1, 7),
    _Cpsld100Ps2Power_Type()
)
cpsld100Ps2Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsld100Ps2Power.setStatus("mandatory")


class _Cpsld100Ps2InUse_Type(Integer32):
    """Custom type cpsld100Ps2InUse based on Integer32"""
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
          ("notInstalled", 3),
          ("yes", 1))
    )


_Cpsld100Ps2InUse_Type.__name__ = "Integer32"
_Cpsld100Ps2InUse_Object = MibTableColumn
cpsld100Ps2InUse = _Cpsld100Ps2InUse_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 16, 1, 8),
    _Cpsld100Ps2InUse_Type()
)
cpsld100Ps2InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsld100Ps2InUse.setStatus("mandatory")
_Cdftf100Table_Object = MibTable
cdftf100Table = _Cdftf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17)
)
if mibBuilder.loadTexts:
    cdftf100Table.setStatus("mandatory")
_Cdftf100Entry_Object = MibTableRow
cdftf100Entry = _Cdftf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1)
)
cdftf100Entry.setIndexNames(
    (0, "MCC16-MIB", "cdftf100SubDeviceIndex"),
    (0, "MCC16-MIB", "cdftf100BiaIndex"),
    (0, "MCC16-MIB", "cdftf100SlotIndex"),
)
if mibBuilder.loadTexts:
    cdftf100Entry.setStatus("mandatory")
_Cdftf100SubDeviceIndex_Type = Integer32
_Cdftf100SubDeviceIndex_Object = MibTableColumn
cdftf100SubDeviceIndex = _Cdftf100SubDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 1),
    _Cdftf100SubDeviceIndex_Type()
)
cdftf100SubDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100SubDeviceIndex.setStatus("mandatory")
_Cdftf100BiaIndex_Type = Integer32
_Cdftf100BiaIndex_Object = MibTableColumn
cdftf100BiaIndex = _Cdftf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 2),
    _Cdftf100BiaIndex_Type()
)
cdftf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100BiaIndex.setStatus("mandatory")
_Cdftf100SlotIndex_Type = Integer32
_Cdftf100SlotIndex_Object = MibTableColumn
cdftf100SlotIndex = _Cdftf100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 3),
    _Cdftf100SlotIndex_Type()
)
cdftf100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100SlotIndex.setStatus("mandatory")
_Cdftf100Groups_Type = DisplayString
_Cdftf100Groups_Object = MibTableColumn
cdftf100Groups = _Cdftf100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 4),
    _Cdftf100Groups_Type()
)
cdftf100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdftf100Groups.setStatus("mandatory")


class _Cdftf100CfgMatch_Type(Integer32):
    """Custom type cdftf100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cdftf100CfgMatch_Type.__name__ = "Integer32"
_Cdftf100CfgMatch_Object = MibTableColumn
cdftf100CfgMatch = _Cdftf100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 5),
    _Cdftf100CfgMatch_Type()
)
cdftf100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100CfgMatch.setStatus("mandatory")
_Cdftf100SerialNumber_Type = Integer32
_Cdftf100SerialNumber_Object = MibTableColumn
cdftf100SerialNumber = _Cdftf100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 6),
    _Cdftf100SerialNumber_Type()
)
cdftf100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100SerialNumber.setStatus("mandatory")
_Cdftf100MRevision_Type = Integer32
_Cdftf100MRevision_Object = MibTableColumn
cdftf100MRevision = _Cdftf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 7),
    _Cdftf100MRevision_Type()
)
cdftf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100MRevision.setStatus("mandatory")


class _Cdftf100TPLinkTbl_Type(Integer32):
    """Custom type cdftf100TPLinkTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cdftf100TPLinkTbl_Type.__name__ = "Integer32"
_Cdftf100TPLinkTbl_Object = MibTableColumn
cdftf100TPLinkTbl = _Cdftf100TPLinkTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 8),
    _Cdftf100TPLinkTbl_Type()
)
cdftf100TPLinkTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100TPLinkTbl.setStatus("mandatory")


class _Cdftf100FiberLinkTbl_Type(Integer32):
    """Custom type cdftf100FiberLinkTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cdftf100FiberLinkTbl_Type.__name__ = "Integer32"
_Cdftf100FiberLinkTbl_Object = MibTableColumn
cdftf100FiberLinkTbl = _Cdftf100FiberLinkTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 9),
    _Cdftf100FiberLinkTbl_Type()
)
cdftf100FiberLinkTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100FiberLinkTbl.setStatus("mandatory")


class _Cdftf100TPActivityTbl_Type(Integer32):
    """Custom type cdftf100TPActivityTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cdftf100TPActivityTbl_Type.__name__ = "Integer32"
_Cdftf100TPActivityTbl_Object = MibTableColumn
cdftf100TPActivityTbl = _Cdftf100TPActivityTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 10),
    _Cdftf100TPActivityTbl_Type()
)
cdftf100TPActivityTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100TPActivityTbl.setStatus("mandatory")


class _Cdftf100FiberActivityTbl_Type(Integer32):
    """Custom type cdftf100FiberActivityTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cdftf100FiberActivityTbl_Type.__name__ = "Integer32"
_Cdftf100FiberActivityTbl_Object = MibTableColumn
cdftf100FiberActivityTbl = _Cdftf100FiberActivityTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 11),
    _Cdftf100FiberActivityTbl_Type()
)
cdftf100FiberActivityTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100FiberActivityTbl.setStatus("mandatory")


class _Cdftf100ConnectorTbl_Type(Integer32):
    """Custom type cdftf100ConnectorTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cdftf100ConnectorTbl_Type.__name__ = "Integer32"
_Cdftf100ConnectorTbl_Object = MibTableColumn
cdftf100ConnectorTbl = _Cdftf100ConnectorTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 12),
    _Cdftf100ConnectorTbl_Type()
)
cdftf100ConnectorTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100ConnectorTbl.setStatus("mandatory")
_Cdftf100FirmwareRevision_Type = CpsConnector
_Cdftf100FirmwareRevision_Object = MibTableColumn
cdftf100FirmwareRevision = _Cdftf100FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 13),
    _Cdftf100FirmwareRevision_Type()
)
cdftf100FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100FirmwareRevision.setStatus("mandatory")


class _Cdftf100CacheClean_Type(Integer32):
    """Custom type cdftf100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cdftf100CacheClean_Type.__name__ = "Integer32"
_Cdftf100CacheClean_Object = MibTableColumn
cdftf100CacheClean = _Cdftf100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 17, 1, 14),
    _Cdftf100CacheClean_Type()
)
cdftf100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdftf100CacheClean.setStatus("mandatory")
_Cpsvt100Table_Object = MibTable
cpsvt100Table = _Cpsvt100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18)
)
if mibBuilder.loadTexts:
    cpsvt100Table.setStatus("mandatory")
_Cpsvt100Entry_Object = MibTableRow
cpsvt100Entry = _Cpsvt100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1)
)
cpsvt100Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsvt100BiaIndex"),
    (0, "MCC16-MIB", "cpsvt100SlotIndex"),
)
if mibBuilder.loadTexts:
    cpsvt100Entry.setStatus("mandatory")
_Cpsvt100BiaIndex_Type = Integer32
_Cpsvt100BiaIndex_Object = MibTableColumn
cpsvt100BiaIndex = _Cpsvt100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 1),
    _Cpsvt100BiaIndex_Type()
)
cpsvt100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100BiaIndex.setStatus("mandatory")
_Cpsvt100SlotIndex_Type = Integer32
_Cpsvt100SlotIndex_Object = MibTableColumn
cpsvt100SlotIndex = _Cpsvt100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 2),
    _Cpsvt100SlotIndex_Type()
)
cpsvt100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100SlotIndex.setStatus("mandatory")
_Cpsvt100Groups_Type = DisplayString
_Cpsvt100Groups_Object = MibTableColumn
cpsvt100Groups = _Cpsvt100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 3),
    _Cpsvt100Groups_Type()
)
cpsvt100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsvt100Groups.setStatus("mandatory")
_Cpsvt100MRevision_Type = Integer32
_Cpsvt100MRevision_Object = MibTableColumn
cpsvt100MRevision = _Cpsvt100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 4),
    _Cpsvt100MRevision_Type()
)
cpsvt100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100MRevision.setStatus("mandatory")


class _Cpsvt100CfgMatch_Type(Integer32):
    """Custom type cpsvt100CfgMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 3),
          ("no", 2),
          ("yes", 1))
    )


_Cpsvt100CfgMatch_Type.__name__ = "Integer32"
_Cpsvt100CfgMatch_Object = MibTableColumn
cpsvt100CfgMatch = _Cpsvt100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 5),
    _Cpsvt100CfgMatch_Type()
)
cpsvt100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100CfgMatch.setStatus("mandatory")
_Cpsvt100SerialNumber_Type = Integer32
_Cpsvt100SerialNumber_Object = MibTableColumn
cpsvt100SerialNumber = _Cpsvt100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 6),
    _Cpsvt100SerialNumber_Type()
)
cpsvt100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100SerialNumber.setStatus("mandatory")


class _Cpsvt100FiberLink_Type(Integer32):
    """Custom type cpsvt100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cpsvt100FiberLink_Type.__name__ = "Integer32"
_Cpsvt100FiberLink_Object = MibTableColumn
cpsvt100FiberLink = _Cpsvt100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 7),
    _Cpsvt100FiberLink_Type()
)
cpsvt100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100FiberLink.setStatus("mandatory")


class _Cpsvt100CopperLink_Type(Integer32):
    """Custom type cpsvt100CopperLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cpsvt100CopperLink_Type.__name__ = "Integer32"
_Cpsvt100CopperLink_Object = MibTableColumn
cpsvt100CopperLink = _Cpsvt100CopperLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 8),
    _Cpsvt100CopperLink_Type()
)
cpsvt100CopperLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100CopperLink.setStatus("mandatory")


class _Cpsvt100Fault_Type(Integer32):
    """Custom type cpsvt100Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsvt100Fault_Type.__name__ = "Integer32"
_Cpsvt100Fault_Object = MibTableColumn
cpsvt100Fault = _Cpsvt100Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 9),
    _Cpsvt100Fault_Type()
)
cpsvt100Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100Fault.setStatus("mandatory")
_Cpsvt100ConnA_Type = CpsConnector
_Cpsvt100ConnA_Object = MibTableColumn
cpsvt100ConnA = _Cpsvt100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 10),
    _Cpsvt100ConnA_Type()
)
cpsvt100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100ConnA.setStatus("mandatory")
_Cpsvt100ConnB_Type = CpsConnector
_Cpsvt100ConnB_Object = MibTableColumn
cpsvt100ConnB = _Cpsvt100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 11),
    _Cpsvt100ConnB_Type()
)
cpsvt100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100ConnB.setStatus("mandatory")


class _Cpsvt100TermTiming_Type(Integer32):
    """Custom type cpsvt100TermTiming based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 16),
          ("kbps1024", 10),
          ("kbps112", 4),
          ("kbps128", 5),
          ("kbps1554", 11),
          ("kbps2048", 12),
          ("kbps256", 6),
          ("kbps3072", 13),
          ("kbps384", 7),
          ("kbps4096", 14),
          ("kbps512", 8),
          ("kbps56", 2),
          ("kbps6144", 15),
          ("kbps64", 3),
          ("kbps768", 9),
          ("rxc", 1))
    )


_Cpsvt100TermTiming_Type.__name__ = "Integer32"
_Cpsvt100TermTiming_Object = MibTableColumn
cpsvt100TermTiming = _Cpsvt100TermTiming_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 12),
    _Cpsvt100TermTiming_Type()
)
cpsvt100TermTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsvt100TermTiming.setStatus("mandatory")


class _Cpsvt100LoopBack_Type(Integer32):
    """Custom type cpsvt100LoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cpsvt100LoopBack_Type.__name__ = "Integer32"
_Cpsvt100LoopBack_Object = MibTableColumn
cpsvt100LoopBack = _Cpsvt100LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 13),
    _Cpsvt100LoopBack_Type()
)
cpsvt100LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsvt100LoopBack.setStatus("mandatory")


class _Cpsvt100CableMode_Type(Integer32):
    """Custom type cpsvt100CableMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 8),
          ("notValid", 1),
          ("rs-232", 7),
          ("rs-449", 6),
          ("rs-530", 3),
          ("rs-530A", 2),
          ("v-35", 5),
          ("x-21", 4))
    )


_Cpsvt100CableMode_Type.__name__ = "Integer32"
_Cpsvt100CableMode_Object = MibTableColumn
cpsvt100CableMode = _Cpsvt100CableMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 14),
    _Cpsvt100CableMode_Type()
)
cpsvt100CableMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100CableMode.setStatus("mandatory")


class _Cpsvt100DCE_Type(Integer32):
    """Custom type cpsvt100DCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_Cpsvt100DCE_Type.__name__ = "Integer32"
_Cpsvt100DCE_Object = MibTableColumn
cpsvt100DCE = _Cpsvt100DCE_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 15),
    _Cpsvt100DCE_Type()
)
cpsvt100DCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100DCE.setStatus("mandatory")


class _Cpsvt100InvertTX_Type(Integer32):
    """Custom type cpsvt100InvertTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("falling", 2),
          ("rising", 1))
    )


_Cpsvt100InvertTX_Type.__name__ = "Integer32"
_Cpsvt100InvertTX_Object = MibTableColumn
cpsvt100InvertTX = _Cpsvt100InvertTX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 16),
    _Cpsvt100InvertTX_Type()
)
cpsvt100InvertTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100InvertTX.setStatus("mandatory")


class _Cpsvt100InvertRX_Type(Integer32):
    """Custom type cpsvt100InvertRX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("falling", 2),
          ("rising", 1))
    )


_Cpsvt100InvertRX_Type.__name__ = "Integer32"
_Cpsvt100InvertRX_Object = MibTableColumn
cpsvt100InvertRX = _Cpsvt100InvertRX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 17),
    _Cpsvt100InvertRX_Type()
)
cpsvt100InvertRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100InvertRX.setStatus("mandatory")


class _Cpsvt100ConfigMode_Type(Integer32):
    """Custom type cpsvt100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cpsvt100ConfigMode_Type.__name__ = "Integer32"
_Cpsvt100ConfigMode_Object = MibTableColumn
cpsvt100ConfigMode = _Cpsvt100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 18),
    _Cpsvt100ConfigMode_Type()
)
cpsvt100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100ConfigMode.setStatus("mandatory")
_Cpsvt100FirmwareRev_Type = Integer32
_Cpsvt100FirmwareRev_Object = MibTableColumn
cpsvt100FirmwareRev = _Cpsvt100FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 19),
    _Cpsvt100FirmwareRev_Type()
)
cpsvt100FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100FirmwareRev.setStatus("mandatory")


class _Cpsvt100RmtDetected_Type(Integer32):
    """Custom type cpsvt100RmtDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cpsvt100RmtDetected_Type.__name__ = "Integer32"
_Cpsvt100RmtDetected_Object = MibTableColumn
cpsvt100RmtDetected = _Cpsvt100RmtDetected_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 20),
    _Cpsvt100RmtDetected_Type()
)
cpsvt100RmtDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100RmtDetected.setStatus("mandatory")


class _Cpsvt100RmtTermTiming_Type(Integer32):
    """Custom type cpsvt100RmtTermTiming based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 16),
          ("kbps1024", 10),
          ("kbps112", 4),
          ("kbps128", 5),
          ("kbps1554", 11),
          ("kbps2048", 12),
          ("kbps256", 6),
          ("kbps3072", 13),
          ("kbps384", 7),
          ("kbps4096", 14),
          ("kbps512", 8),
          ("kbps56", 2),
          ("kbps6144", 15),
          ("kbps64", 3),
          ("kbps768", 9),
          ("rxc", 1))
    )


_Cpsvt100RmtTermTiming_Type.__name__ = "Integer32"
_Cpsvt100RmtTermTiming_Object = MibTableColumn
cpsvt100RmtTermTiming = _Cpsvt100RmtTermTiming_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 21),
    _Cpsvt100RmtTermTiming_Type()
)
cpsvt100RmtTermTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsvt100RmtTermTiming.setStatus("mandatory")


class _Cpsvt100RmtLoopBack_Type(Integer32):
    """Custom type cpsvt100RmtLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cpsvt100RmtLoopBack_Type.__name__ = "Integer32"
_Cpsvt100RmtLoopBack_Object = MibTableColumn
cpsvt100RmtLoopBack = _Cpsvt100RmtLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 22),
    _Cpsvt100RmtLoopBack_Type()
)
cpsvt100RmtLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsvt100RmtLoopBack.setStatus("mandatory")
_Cpsvt100RmtCableMode_Type = Integer32
_Cpsvt100RmtCableMode_Object = MibTableColumn
cpsvt100RmtCableMode = _Cpsvt100RmtCableMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 23),
    _Cpsvt100RmtCableMode_Type()
)
cpsvt100RmtCableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsvt100RmtCableMode.setStatus("mandatory")
_Cpsvt100RmtDCE_Type = Integer32
_Cpsvt100RmtDCE_Object = MibTableColumn
cpsvt100RmtDCE = _Cpsvt100RmtDCE_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 24),
    _Cpsvt100RmtDCE_Type()
)
cpsvt100RmtDCE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsvt100RmtDCE.setStatus("mandatory")
_Cpsvt100RmtInvertTX_Type = Integer32
_Cpsvt100RmtInvertTX_Object = MibTableColumn
cpsvt100RmtInvertTX = _Cpsvt100RmtInvertTX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 25),
    _Cpsvt100RmtInvertTX_Type()
)
cpsvt100RmtInvertTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsvt100RmtInvertTX.setStatus("mandatory")
_Cpsvt100RmtInvertRX_Type = Integer32
_Cpsvt100RmtInvertRX_Object = MibTableColumn
cpsvt100RmtInvertRX = _Cpsvt100RmtInvertRX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 26),
    _Cpsvt100RmtInvertRX_Type()
)
cpsvt100RmtInvertRX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsvt100RmtInvertRX.setStatus("mandatory")


class _Cpsvt100RmtConfigMode_Type(Integer32):
    """Custom type cpsvt100RmtConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cpsvt100RmtConfigMode_Type.__name__ = "Integer32"
_Cpsvt100RmtConfigMode_Object = MibTableColumn
cpsvt100RmtConfigMode = _Cpsvt100RmtConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 27),
    _Cpsvt100RmtConfigMode_Type()
)
cpsvt100RmtConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100RmtConfigMode.setStatus("mandatory")
_Cpsvt100RmtFirmwareRev_Type = Integer32
_Cpsvt100RmtFirmwareRev_Object = MibTableColumn
cpsvt100RmtFirmwareRev = _Cpsvt100RmtFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 28),
    _Cpsvt100RmtFirmwareRev_Type()
)
cpsvt100RmtFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100RmtFirmwareRev.setStatus("mandatory")


class _Cpsvt100RmtCopperLink_Type(Integer32):
    """Custom type cpsvt100RmtCopperLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cpsvt100RmtCopperLink_Type.__name__ = "Integer32"
_Cpsvt100RmtCopperLink_Object = MibTableColumn
cpsvt100RmtCopperLink = _Cpsvt100RmtCopperLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 29),
    _Cpsvt100RmtCopperLink_Type()
)
cpsvt100RmtCopperLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100RmtCopperLink.setStatus("mandatory")


class _Cpsvt100RmtFiberLink_Type(Integer32):
    """Custom type cpsvt100RmtFiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cpsvt100RmtFiberLink_Type.__name__ = "Integer32"
_Cpsvt100RmtFiberLink_Object = MibTableColumn
cpsvt100RmtFiberLink = _Cpsvt100RmtFiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 30),
    _Cpsvt100RmtFiberLink_Type()
)
cpsvt100RmtFiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100RmtFiberLink.setStatus("mandatory")


class _Cpsvt100CacheClean_Type(Integer32):
    """Custom type cpsvt100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cpsvt100CacheClean_Type.__name__ = "Integer32"
_Cpsvt100CacheClean_Object = MibTableColumn
cpsvt100CacheClean = _Cpsvt100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 18, 1, 31),
    _Cpsvt100CacheClean_Type()
)
cpsvt100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsvt100CacheClean.setStatus("mandatory")
_Cemtf100Table_Object = MibTable
cemtf100Table = _Cemtf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19)
)
if mibBuilder.loadTexts:
    cemtf100Table.setStatus("mandatory")
_Cemtf100Entry_Object = MibTableRow
cemtf100Entry = _Cemtf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1)
)
cemtf100Entry.setIndexNames(
    (0, "MCC16-MIB", "cemtf100BiaIndex"),
    (0, "MCC16-MIB", "cemtf100SlotIndex"),
)
if mibBuilder.loadTexts:
    cemtf100Entry.setStatus("mandatory")
_Cemtf100BiaIndex_Type = Integer32
_Cemtf100BiaIndex_Object = MibTableColumn
cemtf100BiaIndex = _Cemtf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 1),
    _Cemtf100BiaIndex_Type()
)
cemtf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100BiaIndex.setStatus("mandatory")
_Cemtf100SlotIndex_Type = Integer32
_Cemtf100SlotIndex_Object = MibTableColumn
cemtf100SlotIndex = _Cemtf100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 2),
    _Cemtf100SlotIndex_Type()
)
cemtf100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100SlotIndex.setStatus("mandatory")
_Cemtf100Groups_Type = DisplayString
_Cemtf100Groups_Object = MibTableColumn
cemtf100Groups = _Cemtf100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 3),
    _Cemtf100Groups_Type()
)
cemtf100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cemtf100Groups.setStatus("mandatory")
_Cemtf100MRevision_Type = Integer32
_Cemtf100MRevision_Object = MibTableColumn
cemtf100MRevision = _Cemtf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 4),
    _Cemtf100MRevision_Type()
)
cemtf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100MRevision.setStatus("mandatory")


class _Cemtf100CfgMatch_Type(Integer32):
    """Custom type cemtf100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cemtf100CfgMatch_Type.__name__ = "Integer32"
_Cemtf100CfgMatch_Object = MibTableColumn
cemtf100CfgMatch = _Cemtf100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 5),
    _Cemtf100CfgMatch_Type()
)
cemtf100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100CfgMatch.setStatus("mandatory")
_Cemtf100SerialNumber_Type = Integer32
_Cemtf100SerialNumber_Object = MibTableColumn
cemtf100SerialNumber = _Cemtf100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 6),
    _Cemtf100SerialNumber_Type()
)
cemtf100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100SerialNumber.setStatus("mandatory")


class _Cemtf100FiberLink_Type(Integer32):
    """Custom type cemtf100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cemtf100FiberLink_Type.__name__ = "Integer32"
_Cemtf100FiberLink_Object = MibTableColumn
cemtf100FiberLink = _Cemtf100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 7),
    _Cemtf100FiberLink_Type()
)
cemtf100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100FiberLink.setStatus("mandatory")


class _Cemtf100OffHook_Type(Integer32):
    """Custom type cemtf100OffHook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cemtf100OffHook_Type.__name__ = "Integer32"
_Cemtf100OffHook_Object = MibTableColumn
cemtf100OffHook = _Cemtf100OffHook_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 8),
    _Cemtf100OffHook_Type()
)
cemtf100OffHook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100OffHook.setStatus("mandatory")


class _Cemtf100Fault_Type(Integer32):
    """Custom type cemtf100Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cemtf100Fault_Type.__name__ = "Integer32"
_Cemtf100Fault_Object = MibTableColumn
cemtf100Fault = _Cemtf100Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 9),
    _Cemtf100Fault_Type()
)
cemtf100Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100Fault.setStatus("mandatory")
_Cemtf100ConnA_Type = CpsConnector
_Cemtf100ConnA_Object = MibTableColumn
cemtf100ConnA = _Cemtf100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 10),
    _Cemtf100ConnA_Type()
)
cemtf100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100ConnA.setStatus("mandatory")
_Cemtf100ConnB_Type = CpsConnector
_Cemtf100ConnB_Object = MibTableColumn
cemtf100ConnB = _Cemtf100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 11),
    _Cemtf100ConnB_Type()
)
cemtf100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100ConnB.setStatus("mandatory")


class _Cemtf100CacheClean_Type(Integer32):
    """Custom type cemtf100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cemtf100CacheClean_Type.__name__ = "Integer32"
_Cemtf100CacheClean_Object = MibTableColumn
cemtf100CacheClean = _Cemtf100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 19, 1, 12),
    _Cemtf100CacheClean_Type()
)
cemtf100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemtf100CacheClean.setStatus("mandatory")
_Captf100Table_Object = MibTable
captf100Table = _Captf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20)
)
if mibBuilder.loadTexts:
    captf100Table.setStatus("mandatory")
_Captf100Entry_Object = MibTableRow
captf100Entry = _Captf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1)
)
captf100Entry.setIndexNames(
    (0, "MCC16-MIB", "captf100BiaIndex"),
    (0, "MCC16-MIB", "captf100SlotIndex"),
)
if mibBuilder.loadTexts:
    captf100Entry.setStatus("mandatory")
_Captf100BiaIndex_Type = Integer32
_Captf100BiaIndex_Object = MibTableColumn
captf100BiaIndex = _Captf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 1),
    _Captf100BiaIndex_Type()
)
captf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100BiaIndex.setStatus("mandatory")
_Captf100SlotIndex_Type = Integer32
_Captf100SlotIndex_Object = MibTableColumn
captf100SlotIndex = _Captf100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 2),
    _Captf100SlotIndex_Type()
)
captf100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100SlotIndex.setStatus("mandatory")
_Captf100Groups_Type = DisplayString
_Captf100Groups_Object = MibTableColumn
captf100Groups = _Captf100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 3),
    _Captf100Groups_Type()
)
captf100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captf100Groups.setStatus("mandatory")
_Captf100MRevision_Type = Integer32
_Captf100MRevision_Object = MibTableColumn
captf100MRevision = _Captf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 4),
    _Captf100MRevision_Type()
)
captf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100MRevision.setStatus("mandatory")


class _Captf100CfgMatch_Type(Integer32):
    """Custom type captf100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Captf100CfgMatch_Type.__name__ = "Integer32"
_Captf100CfgMatch_Object = MibTableColumn
captf100CfgMatch = _Captf100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 5),
    _Captf100CfgMatch_Type()
)
captf100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100CfgMatch.setStatus("mandatory")
_Captf100SerialNumber_Type = Integer32
_Captf100SerialNumber_Object = MibTableColumn
captf100SerialNumber = _Captf100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 6),
    _Captf100SerialNumber_Type()
)
captf100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100SerialNumber.setStatus("mandatory")


class _Captf100FiberLink_Type(Integer32):
    """Custom type captf100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Captf100FiberLink_Type.__name__ = "Integer32"
_Captf100FiberLink_Object = MibTableColumn
captf100FiberLink = _Captf100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 7),
    _Captf100FiberLink_Type()
)
captf100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100FiberLink.setStatus("mandatory")


class _Captf100InUse_Type(Integer32):
    """Custom type captf100InUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Captf100InUse_Type.__name__ = "Integer32"
_Captf100InUse_Object = MibTableColumn
captf100InUse = _Captf100InUse_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 8),
    _Captf100InUse_Type()
)
captf100InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100InUse.setStatus("mandatory")


class _Captf100Fault_Type(Integer32):
    """Custom type captf100Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Captf100Fault_Type.__name__ = "Integer32"
_Captf100Fault_Object = MibTableColumn
captf100Fault = _Captf100Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 9),
    _Captf100Fault_Type()
)
captf100Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100Fault.setStatus("mandatory")
_Captf100ConnA_Type = CpsConnector
_Captf100ConnA_Object = MibTableColumn
captf100ConnA = _Captf100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 10),
    _Captf100ConnA_Type()
)
captf100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100ConnA.setStatus("mandatory")
_Captf100ConnB_Type = CpsConnector
_Captf100ConnB_Object = MibTableColumn
captf100ConnB = _Captf100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 11),
    _Captf100ConnB_Type()
)
captf100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100ConnB.setStatus("mandatory")
_Captf100FirmwareRev_Type = Integer32
_Captf100FirmwareRev_Object = MibTableColumn
captf100FirmwareRev = _Captf100FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 12),
    _Captf100FirmwareRev_Type()
)
captf100FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100FirmwareRev.setStatus("mandatory")


class _Captf100CacheClean_Type(Integer32):
    """Custom type captf100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Captf100CacheClean_Type.__name__ = "Integer32"
_Captf100CacheClean_Object = MibTableColumn
captf100CacheClean = _Captf100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 13),
    _Captf100CacheClean_Type()
)
captf100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100CacheClean.setStatus("mandatory")


class _Captf100Emulates_Type(Integer32):
    """Custom type captf100Emulates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coAutoRingDown", 3),
          ("coStandard", 2),
          ("phone", 1))
    )


_Captf100Emulates_Type.__name__ = "Integer32"
_Captf100Emulates_Object = MibTableColumn
captf100Emulates = _Captf100Emulates_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 20, 1, 14),
    _Captf100Emulates_Type()
)
captf100Emulates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    captf100Emulates.setStatus("mandatory")
_Cfetf205Table_Object = MibTable
cfetf205Table = _Cfetf205Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21)
)
if mibBuilder.loadTexts:
    cfetf205Table.setStatus("mandatory")
_Cfetf205Entry_Object = MibTableRow
cfetf205Entry = _Cfetf205Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1)
)
cfetf205Entry.setIndexNames(
    (0, "MCC16-MIB", "cfetf205BiaIndex"),
    (0, "MCC16-MIB", "cfetf205SlotIndex"),
)
if mibBuilder.loadTexts:
    cfetf205Entry.setStatus("mandatory")
_Cfetf205BiaIndex_Type = Integer32
_Cfetf205BiaIndex_Object = MibTableColumn
cfetf205BiaIndex = _Cfetf205BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 1),
    _Cfetf205BiaIndex_Type()
)
cfetf205BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205BiaIndex.setStatus("mandatory")
_Cfetf205SlotIndex_Type = Integer32
_Cfetf205SlotIndex_Object = MibTableColumn
cfetf205SlotIndex = _Cfetf205SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 2),
    _Cfetf205SlotIndex_Type()
)
cfetf205SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205SlotIndex.setStatus("mandatory")
_Cfetf205Groups_Type = DisplayString
_Cfetf205Groups_Object = MibTableColumn
cfetf205Groups = _Cfetf205Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 3),
    _Cfetf205Groups_Type()
)
cfetf205Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf205Groups.setStatus("mandatory")
_Cfetf205MRevision_Type = Integer32
_Cfetf205MRevision_Object = MibTableColumn
cfetf205MRevision = _Cfetf205MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 4),
    _Cfetf205MRevision_Type()
)
cfetf205MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205MRevision.setStatus("mandatory")


class _Cfetf205CfgMatch_Type(Integer32):
    """Custom type cfetf205CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cfetf205CfgMatch_Type.__name__ = "Integer32"
_Cfetf205CfgMatch_Object = MibTableColumn
cfetf205CfgMatch = _Cfetf205CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 5),
    _Cfetf205CfgMatch_Type()
)
cfetf205CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205CfgMatch.setStatus("mandatory")
_Cfetf205SerialNumber_Type = Integer32
_Cfetf205SerialNumber_Object = MibTableColumn
cfetf205SerialNumber = _Cfetf205SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 6),
    _Cfetf205SerialNumber_Type()
)
cfetf205SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205SerialNumber.setStatus("mandatory")
_Cfetf205ConnA_Type = CpsConnector
_Cfetf205ConnA_Object = MibTableColumn
cfetf205ConnA = _Cfetf205ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 7),
    _Cfetf205ConnA_Type()
)
cfetf205ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205ConnA.setStatus("mandatory")
_Cfetf205ConnB_Type = CpsConnector
_Cfetf205ConnB_Object = MibTableColumn
cfetf205ConnB = _Cfetf205ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 8),
    _Cfetf205ConnB_Type()
)
cfetf205ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205ConnB.setStatus("mandatory")


class _Cfetf205TPLink_Type(Integer32):
    """Custom type cfetf205TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cfetf205TPLink_Type.__name__ = "Integer32"
_Cfetf205TPLink_Object = MibTableColumn
cfetf205TPLink = _Cfetf205TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 9),
    _Cfetf205TPLink_Type()
)
cfetf205TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205TPLink.setStatus("mandatory")


class _Cfetf205FiberLink_Type(Integer32):
    """Custom type cfetf205FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Cfetf205FiberLink_Type.__name__ = "Integer32"
_Cfetf205FiberLink_Object = MibTableColumn
cfetf205FiberLink = _Cfetf205FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 10),
    _Cfetf205FiberLink_Type()
)
cfetf205FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205FiberLink.setStatus("mandatory")


class _Cfetf205Fault_Type(Integer32):
    """Custom type cfetf205Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cfetf205Fault_Type.__name__ = "Integer32"
_Cfetf205Fault_Object = MibTableColumn
cfetf205Fault = _Cfetf205Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 11),
    _Cfetf205Fault_Type()
)
cfetf205Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205Fault.setStatus("mandatory")


class _Cfetf205FastLinkPulse_Type(Integer32):
    """Custom type cfetf205FastLinkPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autonegotiate", 1),
          ("hdx100Btx", 2))
    )


_Cfetf205FastLinkPulse_Type.__name__ = "Integer32"
_Cfetf205FastLinkPulse_Object = MibTableColumn
cfetf205FastLinkPulse = _Cfetf205FastLinkPulse_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 12),
    _Cfetf205FastLinkPulse_Type()
)
cfetf205FastLinkPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf205FastLinkPulse.setStatus("mandatory")


class _Cfetf205Enabled_Type(Integer32):
    """Custom type cfetf205Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cfetf205Enabled_Type.__name__ = "Integer32"
_Cfetf205Enabled_Object = MibTableColumn
cfetf205Enabled = _Cfetf205Enabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 13),
    _Cfetf205Enabled_Type()
)
cfetf205Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf205Enabled.setStatus("mandatory")


class _Cfetf205Pause_Type(Integer32):
    """Custom type cfetf205Pause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cfetf205Pause_Type.__name__ = "Integer32"
_Cfetf205Pause_Object = MibTableColumn
cfetf205Pause = _Cfetf205Pause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 14),
    _Cfetf205Pause_Type()
)
cfetf205Pause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf205Pause.setStatus("mandatory")


class _Cfetf205LinkPassThrough_Type(Integer32):
    """Custom type cfetf205LinkPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cfetf205LinkPassThrough_Type.__name__ = "Integer32"
_Cfetf205LinkPassThrough_Object = MibTableColumn
cfetf205LinkPassThrough = _Cfetf205LinkPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 15),
    _Cfetf205LinkPassThrough_Type()
)
cfetf205LinkPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf205LinkPassThrough.setStatus("mandatory")


class _Cfetf205AutoCross_Type(Integer32):
    """Custom type cfetf205AutoCross based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cfetf205AutoCross_Type.__name__ = "Integer32"
_Cfetf205AutoCross_Object = MibTableColumn
cfetf205AutoCross = _Cfetf205AutoCross_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 16),
    _Cfetf205AutoCross_Type()
)
cfetf205AutoCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf205AutoCross.setStatus("mandatory")


class _Cfetf205TPActivity_Type(Integer32):
    """Custom type cfetf205TPActivity based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Cfetf205TPActivity_Type.__name__ = "Integer32"
_Cfetf205TPActivity_Object = MibTableColumn
cfetf205TPActivity = _Cfetf205TPActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 17),
    _Cfetf205TPActivity_Type()
)
cfetf205TPActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205TPActivity.setStatus("mandatory")


class _Cfetf205FiberActivity_Type(Integer32):
    """Custom type cfetf205FiberActivity based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Cfetf205FiberActivity_Type.__name__ = "Integer32"
_Cfetf205FiberActivity_Object = MibTableColumn
cfetf205FiberActivity = _Cfetf205FiberActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 18),
    _Cfetf205FiberActivity_Type()
)
cfetf205FiberActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205FiberActivity.setStatus("mandatory")


class _Cfetf205ConfigMode_Type(Integer32):
    """Custom type cfetf205ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cfetf205ConfigMode_Type.__name__ = "Integer32"
_Cfetf205ConfigMode_Object = MibTableColumn
cfetf205ConfigMode = _Cfetf205ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 19),
    _Cfetf205ConfigMode_Type()
)
cfetf205ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205ConfigMode.setStatus("mandatory")


class _Cfetf205FarEndFault_Type(Integer32):
    """Custom type cfetf205FarEndFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cfetf205FarEndFault_Type.__name__ = "Integer32"
_Cfetf205FarEndFault_Object = MibTableColumn
cfetf205FarEndFault = _Cfetf205FarEndFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 20),
    _Cfetf205FarEndFault_Type()
)
cfetf205FarEndFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfetf205FarEndFault.setStatus("mandatory")


class _Cfetf205CacheClean_Type(Integer32):
    """Custom type cfetf205CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cfetf205CacheClean_Type.__name__ = "Integer32"
_Cfetf205CacheClean_Object = MibTableColumn
cfetf205CacheClean = _Cfetf205CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 21, 1, 21),
    _Cfetf205CacheClean_Type()
)
cfetf205CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfetf205CacheClean.setStatus("mandatory")
_Cbftf150Table_Object = MibTable
cbftf150Table = _Cbftf150Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22)
)
if mibBuilder.loadTexts:
    cbftf150Table.setStatus("mandatory")
_Cbftf150Entry_Object = MibTableRow
cbftf150Entry = _Cbftf150Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1)
)
cbftf150Entry.setIndexNames(
    (0, "MCC16-MIB", "cbftf150SubDeviceIndex"),
    (0, "MCC16-MIB", "cbftf150BiaIndex"),
    (0, "MCC16-MIB", "cbftf150SlotIndex"),
)
if mibBuilder.loadTexts:
    cbftf150Entry.setStatus("mandatory")
_Cbftf150SubDeviceIndex_Type = Integer32
_Cbftf150SubDeviceIndex_Object = MibTableColumn
cbftf150SubDeviceIndex = _Cbftf150SubDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 1),
    _Cbftf150SubDeviceIndex_Type()
)
cbftf150SubDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150SubDeviceIndex.setStatus("mandatory")
_Cbftf150BiaIndex_Type = Integer32
_Cbftf150BiaIndex_Object = MibTableColumn
cbftf150BiaIndex = _Cbftf150BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 2),
    _Cbftf150BiaIndex_Type()
)
cbftf150BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150BiaIndex.setStatus("mandatory")
_Cbftf150SlotIndex_Type = Integer32
_Cbftf150SlotIndex_Object = MibTableColumn
cbftf150SlotIndex = _Cbftf150SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 3),
    _Cbftf150SlotIndex_Type()
)
cbftf150SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150SlotIndex.setStatus("mandatory")
_Cbftf150Groups_Type = DisplayString
_Cbftf150Groups_Object = MibTableColumn
cbftf150Groups = _Cbftf150Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 4),
    _Cbftf150Groups_Type()
)
cbftf150Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf150Groups.setStatus("mandatory")
_Cbftf150MRevision_Type = Integer32
_Cbftf150MRevision_Object = MibTableColumn
cbftf150MRevision = _Cbftf150MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 5),
    _Cbftf150MRevision_Type()
)
cbftf150MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150MRevision.setStatus("mandatory")


class _Cbftf150CfgMatch_Type(Integer32):
    """Custom type cbftf150CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cbftf150CfgMatch_Type.__name__ = "Integer32"
_Cbftf150CfgMatch_Object = MibTableColumn
cbftf150CfgMatch = _Cbftf150CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 6),
    _Cbftf150CfgMatch_Type()
)
cbftf150CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150CfgMatch.setStatus("mandatory")
_Cbftf150SerialNumber_Type = Integer32
_Cbftf150SerialNumber_Object = MibTableColumn
cbftf150SerialNumber = _Cbftf150SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 7),
    _Cbftf150SerialNumber_Type()
)
cbftf150SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150SerialNumber.setStatus("mandatory")


class _Cbftf150ConfigMode_Type(Integer32):
    """Custom type cbftf150ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cbftf150ConfigMode_Type.__name__ = "Integer32"
_Cbftf150ConfigMode_Object = MibTableColumn
cbftf150ConfigMode = _Cbftf150ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 8),
    _Cbftf150ConfigMode_Type()
)
cbftf150ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150ConfigMode.setStatus("mandatory")
_Cbftf150FirmwareRevision_Type = Integer32
_Cbftf150FirmwareRevision_Object = MibTableColumn
cbftf150FirmwareRevision = _Cbftf150FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 9),
    _Cbftf150FirmwareRevision_Type()
)
cbftf150FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150FirmwareRevision.setStatus("mandatory")


class _Cbftf150FormFactor_Type(Integer32):
    """Custom type cbftf150FormFactor based on Integer32"""
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
        *(("s1W1N1a", 3),
          ("s1W1N2a", 2),
          ("s1W2a", 1),
          ("s2W1N5a", 5),
          ("s2W2N4a", 4))
    )


_Cbftf150FormFactor_Type.__name__ = "Integer32"
_Cbftf150FormFactor_Object = MibTableColumn
cbftf150FormFactor = _Cbftf150FormFactor_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 10),
    _Cbftf150FormFactor_Type()
)
cbftf150FormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150FormFactor.setStatus("mandatory")


class _Cbftf150AutoNegotTbl_Type(Integer32):
    """Custom type cbftf150AutoNegotTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cbftf150AutoNegotTbl_Type.__name__ = "Integer32"
_Cbftf150AutoNegotTbl_Object = MibTableColumn
cbftf150AutoNegotTbl = _Cbftf150AutoNegotTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 11),
    _Cbftf150AutoNegotTbl_Type()
)
cbftf150AutoNegotTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf150AutoNegotTbl.setStatus("mandatory")


class _Cbftf150FullDuplexTbl_Type(Integer32):
    """Custom type cbftf150FullDuplexTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2),
          ("negotiating", 3))
    )


_Cbftf150FullDuplexTbl_Type.__name__ = "Integer32"
_Cbftf150FullDuplexTbl_Object = MibTableColumn
cbftf150FullDuplexTbl = _Cbftf150FullDuplexTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 12),
    _Cbftf150FullDuplexTbl_Type()
)
cbftf150FullDuplexTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf150FullDuplexTbl.setStatus("mandatory")


class _Cbftf150100MbpsTbl_Type(Integer32):
    """Custom type cbftf150100MbpsTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mbps10", 2),
          ("mbps100", 1),
          ("negotiating", 3))
    )


_Cbftf150100MbpsTbl_Type.__name__ = "Integer32"
_Cbftf150100MbpsTbl_Object = MibTableColumn
cbftf150100MbpsTbl = _Cbftf150100MbpsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 13),
    _Cbftf150100MbpsTbl_Type()
)
cbftf150100MbpsTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf150100MbpsTbl.setStatus("mandatory")


class _Cbftf150CrossTbl_Type(Integer32):
    """Custom type cbftf150CrossTbl based on Integer32"""
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
        *(("auto", 1),
          ("mdi", 2),
          ("mdix", 3),
          ("notSupported", 4))
    )


_Cbftf150CrossTbl_Type.__name__ = "Integer32"
_Cbftf150CrossTbl_Object = MibTableColumn
cbftf150CrossTbl = _Cbftf150CrossTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 14),
    _Cbftf150CrossTbl_Type()
)
cbftf150CrossTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf150CrossTbl.setStatus("mandatory")


class _Cbftf150FarEndFaultTbl_Type(Integer32):
    """Custom type cbftf150FarEndFaultTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cbftf150FarEndFaultTbl_Type.__name__ = "Integer32"
_Cbftf150FarEndFaultTbl_Object = MibTableColumn
cbftf150FarEndFaultTbl = _Cbftf150FarEndFaultTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 15),
    _Cbftf150FarEndFaultTbl_Type()
)
cbftf150FarEndFaultTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cbftf150FarEndFaultTbl.setStatus("mandatory")
_Cbftf150ConnectorTbl_Type = CpsConnector
_Cbftf150ConnectorTbl_Object = MibTableColumn
cbftf150ConnectorTbl = _Cbftf150ConnectorTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 16),
    _Cbftf150ConnectorTbl_Type()
)
cbftf150ConnectorTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150ConnectorTbl.setStatus("mandatory")


class _Cbftf150LinkTbl_Type(Integer32):
    """Custom type cbftf150LinkTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cbftf150LinkTbl_Type.__name__ = "Integer32"
_Cbftf150LinkTbl_Object = MibTableColumn
cbftf150LinkTbl = _Cbftf150LinkTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 17),
    _Cbftf150LinkTbl_Type()
)
cbftf150LinkTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150LinkTbl.setStatus("mandatory")
_Cbftf150PortCount_Type = Integer32
_Cbftf150PortCount_Object = MibTableColumn
cbftf150PortCount = _Cbftf150PortCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 18),
    _Cbftf150PortCount_Type()
)
cbftf150PortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150PortCount.setStatus("mandatory")


class _Cbftf150CacheClean_Type(Integer32):
    """Custom type cbftf150CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cbftf150CacheClean_Type.__name__ = "Integer32"
_Cbftf150CacheClean_Object = MibTableColumn
cbftf150CacheClean = _Cbftf150CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 22, 1, 19),
    _Cbftf150CacheClean_Type()
)
cbftf150CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbftf150CacheClean.setStatus("mandatory")
_Cgfeb100Table_Object = MibTable
cgfeb100Table = _Cgfeb100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23)
)
if mibBuilder.loadTexts:
    cgfeb100Table.setStatus("mandatory")
_Cgfeb100Entry_Object = MibTableRow
cgfeb100Entry = _Cgfeb100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1)
)
cgfeb100Entry.setIndexNames(
    (0, "MCC16-MIB", "cgfeb100BiaIndex"),
    (0, "MCC16-MIB", "cgfeb100SlotIndex"),
)
if mibBuilder.loadTexts:
    cgfeb100Entry.setStatus("mandatory")
_Cgfeb100BiaIndex_Type = Integer32
_Cgfeb100BiaIndex_Object = MibTableColumn
cgfeb100BiaIndex = _Cgfeb100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 1),
    _Cgfeb100BiaIndex_Type()
)
cgfeb100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100BiaIndex.setStatus("mandatory")
_Cgfeb100SlotIndex_Type = Integer32
_Cgfeb100SlotIndex_Object = MibTableColumn
cgfeb100SlotIndex = _Cgfeb100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 2),
    _Cgfeb100SlotIndex_Type()
)
cgfeb100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100SlotIndex.setStatus("mandatory")
_Cgfeb100Groups_Type = DisplayString
_Cgfeb100Groups_Object = MibTableColumn
cgfeb100Groups = _Cgfeb100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 3),
    _Cgfeb100Groups_Type()
)
cgfeb100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100Groups.setStatus("mandatory")
_Cgfeb100MRevision_Type = Integer32
_Cgfeb100MRevision_Object = MibTableColumn
cgfeb100MRevision = _Cgfeb100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 4),
    _Cgfeb100MRevision_Type()
)
cgfeb100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100MRevision.setStatus("mandatory")


class _Cgfeb100CfgMatch_Type(Integer32):
    """Custom type cgfeb100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100CfgMatch_Type.__name__ = "Integer32"
_Cgfeb100CfgMatch_Object = MibTableColumn
cgfeb100CfgMatch = _Cgfeb100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 5),
    _Cgfeb100CfgMatch_Type()
)
cgfeb100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100CfgMatch.setStatus("mandatory")
_Cgfeb100SerialNumber_Type = Integer32
_Cgfeb100SerialNumber_Object = MibTableColumn
cgfeb100SerialNumber = _Cgfeb100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 6),
    _Cgfeb100SerialNumber_Type()
)
cgfeb100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100SerialNumber.setStatus("mandatory")


class _Cgfeb100ConfigMode_Type(Integer32):
    """Custom type cgfeb100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Cgfeb100ConfigMode_Type.__name__ = "Integer32"
_Cgfeb100ConfigMode_Object = MibTableColumn
cgfeb100ConfigMode = _Cgfeb100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 7),
    _Cgfeb100ConfigMode_Type()
)
cgfeb100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100ConfigMode.setStatus("mandatory")
_Cgfeb100FirmwareRevision_Type = Integer32
_Cgfeb100FirmwareRevision_Object = MibTableColumn
cgfeb100FirmwareRevision = _Cgfeb100FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 8),
    _Cgfeb100FirmwareRevision_Type()
)
cgfeb100FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100FirmwareRevision.setStatus("mandatory")


class _Cgfeb100SelfTestFailed_Type(Integer32):
    """Custom type cgfeb100SelfTestFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cgfeb100SelfTestFailed_Type.__name__ = "Integer32"
_Cgfeb100SelfTestFailed_Object = MibTableColumn
cgfeb100SelfTestFailed = _Cgfeb100SelfTestFailed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 9),
    _Cgfeb100SelfTestFailed_Type()
)
cgfeb100SelfTestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100SelfTestFailed.setStatus("mandatory")


class _Cgfeb100MonitorType_Type(Integer32):
    """Custom type cgfeb100MonitorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 1),
          ("notInstalled", 3),
          ("twistedPair", 2))
    )


_Cgfeb100MonitorType_Type.__name__ = "Integer32"
_Cgfeb100MonitorType_Object = MibTableColumn
cgfeb100MonitorType = _Cgfeb100MonitorType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 10),
    _Cgfeb100MonitorType_Type()
)
cgfeb100MonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100MonitorType.setStatus("mandatory")


class _Cgfeb100LinkPassThrough_Type(Integer32):
    """Custom type cgfeb100LinkPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cgfeb100LinkPassThrough_Type.__name__ = "Integer32"
_Cgfeb100LinkPassThrough_Object = MibTableColumn
cgfeb100LinkPassThrough = _Cgfeb100LinkPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 11),
    _Cgfeb100LinkPassThrough_Type()
)
cgfeb100LinkPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100LinkPassThrough.setStatus("mandatory")


class _Cgfeb100QosEnabled_Type(Integer32):
    """Custom type cgfeb100QosEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cgfeb100QosEnabled_Type.__name__ = "Integer32"
_Cgfeb100QosEnabled_Object = MibTableColumn
cgfeb100QosEnabled = _Cgfeb100QosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 12),
    _Cgfeb100QosEnabled_Type()
)
cgfeb100QosEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100QosEnabled.setStatus("mandatory")
_Cgfeb100QosHPThreshold_Type = Integer32
_Cgfeb100QosHPThreshold_Object = MibTableColumn
cgfeb100QosHPThreshold = _Cgfeb100QosHPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 13),
    _Cgfeb100QosHPThreshold_Type()
)
cgfeb100QosHPThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100QosHPThreshold.setStatus("mandatory")
_Cgfeb100QosLqWeight_Type = Integer32
_Cgfeb100QosLqWeight_Object = MibTableColumn
cgfeb100QosLqWeight = _Cgfeb100QosLqWeight_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 14),
    _Cgfeb100QosLqWeight_Type()
)
cgfeb100QosLqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100QosLqWeight.setStatus("mandatory")
_Cgfeb100QosHqWeight_Type = Integer32
_Cgfeb100QosHqWeight_Object = MibTableColumn
cgfeb100QosHqWeight = _Cgfeb100QosHqWeight_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 15),
    _Cgfeb100QosHqWeight_Type()
)
cgfeb100QosHqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100QosHqWeight.setStatus("mandatory")
_Cgfeb100ConnA_Type = CpsConnector
_Cgfeb100ConnA_Object = MibTableColumn
cgfeb100ConnA = _Cgfeb100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 16),
    _Cgfeb100ConnA_Type()
)
cgfeb100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100ConnA.setStatus("mandatory")


class _Cgfeb100TPLink_Type(Integer32):
    """Custom type cgfeb100TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cgfeb100TPLink_Type.__name__ = "Integer32"
_Cgfeb100TPLink_Object = MibTableColumn
cgfeb100TPLink = _Cgfeb100TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 17),
    _Cgfeb100TPLink_Type()
)
cgfeb100TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPLink.setStatus("mandatory")


class _Cgfeb100TPSpeedCfg_Type(Integer32):
    """Custom type cgfeb100TPSpeedCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("mbps10", 1),
          ("mbps100", 2))
    )


_Cgfeb100TPSpeedCfg_Type.__name__ = "Integer32"
_Cgfeb100TPSpeedCfg_Object = MibTableColumn
cgfeb100TPSpeedCfg = _Cgfeb100TPSpeedCfg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 18),
    _Cgfeb100TPSpeedCfg_Type()
)
cgfeb100TPSpeedCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPSpeedCfg.setStatus("mandatory")


class _Cgfeb100TPSpeedStat_Type(Integer32):
    """Custom type cgfeb100TPSpeedStat based on Integer32"""
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
        *(("mbps10", 1),
          ("mbps100", 2),
          ("mbps1000", 3),
          ("notApplicable", 4))
    )


_Cgfeb100TPSpeedStat_Type.__name__ = "Integer32"
_Cgfeb100TPSpeedStat_Object = MibTableColumn
cgfeb100TPSpeedStat = _Cgfeb100TPSpeedStat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 19),
    _Cgfeb100TPSpeedStat_Type()
)
cgfeb100TPSpeedStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPSpeedStat.setStatus("mandatory")


class _Cgfeb100TPFullDuplexCfg_Type(Integer32):
    """Custom type cgfeb100TPFullDuplexCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("fdx", 1),
          ("hdx", 2))
    )


_Cgfeb100TPFullDuplexCfg_Type.__name__ = "Integer32"
_Cgfeb100TPFullDuplexCfg_Object = MibTableColumn
cgfeb100TPFullDuplexCfg = _Cgfeb100TPFullDuplexCfg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 20),
    _Cgfeb100TPFullDuplexCfg_Type()
)
cgfeb100TPFullDuplexCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPFullDuplexCfg.setStatus("mandatory")


class _Cgfeb100TPFullDuplexStat_Type(Integer32):
    """Custom type cgfeb100TPFullDuplexStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fdx", 1),
          ("hdx", 2),
          ("notApplicable", 3))
    )


_Cgfeb100TPFullDuplexStat_Type.__name__ = "Integer32"
_Cgfeb100TPFullDuplexStat_Object = MibTableColumn
cgfeb100TPFullDuplexStat = _Cgfeb100TPFullDuplexStat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 21),
    _Cgfeb100TPFullDuplexStat_Type()
)
cgfeb100TPFullDuplexStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPFullDuplexStat.setStatus("mandatory")


class _Cgfeb100TPCrossCfg_Type(Integer32):
    """Custom type cgfeb100TPCrossCfg based on Integer32"""
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
        *(("auto", 3),
          ("mdi", 1),
          ("mdix", 2),
          ("notApplicable", 4))
    )


_Cgfeb100TPCrossCfg_Type.__name__ = "Integer32"
_Cgfeb100TPCrossCfg_Object = MibTableColumn
cgfeb100TPCrossCfg = _Cgfeb100TPCrossCfg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 22),
    _Cgfeb100TPCrossCfg_Type()
)
cgfeb100TPCrossCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPCrossCfg.setStatus("mandatory")


class _Cgfeb100TPCrossStat_Type(Integer32):
    """Custom type cgfeb100TPCrossStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("mdi", 1),
          ("mdix", 2))
    )


_Cgfeb100TPCrossStat_Type.__name__ = "Integer32"
_Cgfeb100TPCrossStat_Object = MibTableColumn
cgfeb100TPCrossStat = _Cgfeb100TPCrossStat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 23),
    _Cgfeb100TPCrossStat_Type()
)
cgfeb100TPCrossStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPCrossStat.setStatus("mandatory")


class _Cgfeb100TPAutoNegot_Type(Integer32):
    """Custom type cgfeb100TPAutoNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Cgfeb100TPAutoNegot_Type.__name__ = "Integer32"
_Cgfeb100TPAutoNegot_Object = MibTableColumn
cgfeb100TPAutoNegot = _Cgfeb100TPAutoNegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 24),
    _Cgfeb100TPAutoNegot_Type()
)
cgfeb100TPAutoNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPAutoNegot.setStatus("mandatory")


class _Cgfeb100TPAdv10HDX_Type(Integer32):
    """Custom type cgfeb100TPAdv10HDX based on Integer32"""
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
        *(("disabled", 2),
          ("disabledRO", 5),
          ("enabled", 1),
          ("enabledRO", 4),
          ("notApplicable", 3))
    )


_Cgfeb100TPAdv10HDX_Type.__name__ = "Integer32"
_Cgfeb100TPAdv10HDX_Object = MibTableColumn
cgfeb100TPAdv10HDX = _Cgfeb100TPAdv10HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 25),
    _Cgfeb100TPAdv10HDX_Type()
)
cgfeb100TPAdv10HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPAdv10HDX.setStatus("mandatory")


class _Cgfeb100TPAdv10FDX_Type(Integer32):
    """Custom type cgfeb100TPAdv10FDX based on Integer32"""
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
        *(("disabled", 2),
          ("disabledRO", 5),
          ("enabled", 1),
          ("enabledRO", 4),
          ("notApplicable", 3))
    )


_Cgfeb100TPAdv10FDX_Type.__name__ = "Integer32"
_Cgfeb100TPAdv10FDX_Object = MibTableColumn
cgfeb100TPAdv10FDX = _Cgfeb100TPAdv10FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 26),
    _Cgfeb100TPAdv10FDX_Type()
)
cgfeb100TPAdv10FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPAdv10FDX.setStatus("mandatory")


class _Cgfeb100TPAdv100HDX_Type(Integer32):
    """Custom type cgfeb100TPAdv100HDX based on Integer32"""
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
        *(("disabled", 2),
          ("disabledRO", 5),
          ("enabled", 1),
          ("enabledRO", 4),
          ("notApplicable", 3))
    )


_Cgfeb100TPAdv100HDX_Type.__name__ = "Integer32"
_Cgfeb100TPAdv100HDX_Object = MibTableColumn
cgfeb100TPAdv100HDX = _Cgfeb100TPAdv100HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 27),
    _Cgfeb100TPAdv100HDX_Type()
)
cgfeb100TPAdv100HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPAdv100HDX.setStatus("mandatory")


class _Cgfeb100TPAdv100FDX_Type(Integer32):
    """Custom type cgfeb100TPAdv100FDX based on Integer32"""
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
        *(("disabled", 2),
          ("disabledRO", 5),
          ("enabled", 1),
          ("enabledRO", 4),
          ("notApplicable", 3))
    )


_Cgfeb100TPAdv100FDX_Type.__name__ = "Integer32"
_Cgfeb100TPAdv100FDX_Object = MibTableColumn
cgfeb100TPAdv100FDX = _Cgfeb100TPAdv100FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 28),
    _Cgfeb100TPAdv100FDX_Type()
)
cgfeb100TPAdv100FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPAdv100FDX.setStatus("mandatory")


class _Cgfeb100TPAdv1000HDX_Type(Integer32):
    """Custom type cgfeb100TPAdv1000HDX based on Integer32"""
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
        *(("disabled", 2),
          ("disabledRO", 5),
          ("enabled", 1),
          ("enabledRO", 4),
          ("notApplicable", 3))
    )


_Cgfeb100TPAdv1000HDX_Type.__name__ = "Integer32"
_Cgfeb100TPAdv1000HDX_Object = MibTableColumn
cgfeb100TPAdv1000HDX = _Cgfeb100TPAdv1000HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 29),
    _Cgfeb100TPAdv1000HDX_Type()
)
cgfeb100TPAdv1000HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPAdv1000HDX.setStatus("mandatory")


class _Cgfeb100TPAdv1000FDX_Type(Integer32):
    """Custom type cgfeb100TPAdv1000FDX based on Integer32"""
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
        *(("disabled", 2),
          ("disabledRO", 5),
          ("enabled", 1),
          ("enabledRO", 4),
          ("notApplicable", 3))
    )


_Cgfeb100TPAdv1000FDX_Type.__name__ = "Integer32"
_Cgfeb100TPAdv1000FDX_Object = MibTableColumn
cgfeb100TPAdv1000FDX = _Cgfeb100TPAdv1000FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 30),
    _Cgfeb100TPAdv1000FDX_Type()
)
cgfeb100TPAdv1000FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPAdv1000FDX.setStatus("mandatory")


class _Cgfeb100TPLpAdvPause_Type(Integer32):
    """Custom type cgfeb100TPLpAdvPause based on Integer32"""
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
        *(("asymRX", 2),
          ("asymTX", 3),
          ("disabled", 4),
          ("notApplicable", 5),
          ("symetric", 1))
    )


_Cgfeb100TPLpAdvPause_Type.__name__ = "Integer32"
_Cgfeb100TPLpAdvPause_Object = MibTableColumn
cgfeb100TPLpAdvPause = _Cgfeb100TPLpAdvPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 31),
    _Cgfeb100TPLpAdvPause_Type()
)
cgfeb100TPLpAdvPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPLpAdvPause.setStatus("mandatory")


class _Cgfeb100TPLpAdv10HDX_Type(Integer32):
    """Custom type cgfeb100TPLpAdv10HDX based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100TPLpAdv10HDX_Type.__name__ = "Integer32"
_Cgfeb100TPLpAdv10HDX_Object = MibTableColumn
cgfeb100TPLpAdv10HDX = _Cgfeb100TPLpAdv10HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 32),
    _Cgfeb100TPLpAdv10HDX_Type()
)
cgfeb100TPLpAdv10HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPLpAdv10HDX.setStatus("mandatory")


class _Cgfeb100TPLpAdv10FDX_Type(Integer32):
    """Custom type cgfeb100TPLpAdv10FDX based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100TPLpAdv10FDX_Type.__name__ = "Integer32"
_Cgfeb100TPLpAdv10FDX_Object = MibTableColumn
cgfeb100TPLpAdv10FDX = _Cgfeb100TPLpAdv10FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 33),
    _Cgfeb100TPLpAdv10FDX_Type()
)
cgfeb100TPLpAdv10FDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPLpAdv10FDX.setStatus("mandatory")


class _Cgfeb100TPLpAdv100HDX_Type(Integer32):
    """Custom type cgfeb100TPLpAdv100HDX based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100TPLpAdv100HDX_Type.__name__ = "Integer32"
_Cgfeb100TPLpAdv100HDX_Object = MibTableColumn
cgfeb100TPLpAdv100HDX = _Cgfeb100TPLpAdv100HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 34),
    _Cgfeb100TPLpAdv100HDX_Type()
)
cgfeb100TPLpAdv100HDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPLpAdv100HDX.setStatus("mandatory")


class _Cgfeb100TPLpAdv100FDX_Type(Integer32):
    """Custom type cgfeb100TPLpAdv100FDX based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100TPLpAdv100FDX_Type.__name__ = "Integer32"
_Cgfeb100TPLpAdv100FDX_Object = MibTableColumn
cgfeb100TPLpAdv100FDX = _Cgfeb100TPLpAdv100FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 35),
    _Cgfeb100TPLpAdv100FDX_Type()
)
cgfeb100TPLpAdv100FDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPLpAdv100FDX.setStatus("mandatory")


class _Cgfeb100TPLpAdv1000HDX_Type(Integer32):
    """Custom type cgfeb100TPLpAdv1000HDX based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100TPLpAdv1000HDX_Type.__name__ = "Integer32"
_Cgfeb100TPLpAdv1000HDX_Object = MibTableColumn
cgfeb100TPLpAdv1000HDX = _Cgfeb100TPLpAdv1000HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 36),
    _Cgfeb100TPLpAdv1000HDX_Type()
)
cgfeb100TPLpAdv1000HDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPLpAdv1000HDX.setStatus("mandatory")


class _Cgfeb100TPLpAdv1000FDX_Type(Integer32):
    """Custom type cgfeb100TPLpAdv1000FDX based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100TPLpAdv1000FDX_Type.__name__ = "Integer32"
_Cgfeb100TPLpAdv1000FDX_Object = MibTableColumn
cgfeb100TPLpAdv1000FDX = _Cgfeb100TPLpAdv1000FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 37),
    _Cgfeb100TPLpAdv1000FDX_Type()
)
cgfeb100TPLpAdv1000FDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPLpAdv1000FDX.setStatus("mandatory")


class _Cgfeb100TPAdvPause_Type(Integer32):
    """Custom type cgfeb100TPAdvPause based on Integer32"""
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
        *(("asymRX", 2),
          ("asymRXRO", 7),
          ("asymTX", 3),
          ("asymTXRO", 8),
          ("disabled", 4),
          ("disabledRO", 9),
          ("notApplicable", 5),
          ("symetric", 1),
          ("symmetricRO", 6))
    )


_Cgfeb100TPAdvPause_Type.__name__ = "Integer32"
_Cgfeb100TPAdvPause_Object = MibTableColumn
cgfeb100TPAdvPause = _Cgfeb100TPAdvPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 38),
    _Cgfeb100TPAdvPause_Type()
)
cgfeb100TPAdvPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPAdvPause.setStatus("mandatory")


class _Cgfeb100TPQosPause_Type(Integer32):
    """Custom type cgfeb100TPQosPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cgfeb100TPQosPause_Type.__name__ = "Integer32"
_Cgfeb100TPQosPause_Object = MibTableColumn
cgfeb100TPQosPause = _Cgfeb100TPQosPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 39),
    _Cgfeb100TPQosPause_Type()
)
cgfeb100TPQosPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPQosPause.setStatus("mandatory")


class _Cgfeb100TPSacCfg_Type(Integer32):
    """Custom type cgfeb100TPSacCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cgfeb100TPSacCfg_Type.__name__ = "Integer32"
_Cgfeb100TPSacCfg_Object = MibTableColumn
cgfeb100TPSacCfg = _Cgfeb100TPSacCfg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 40),
    _Cgfeb100TPSacCfg_Type()
)
cgfeb100TPSacCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100TPSacCfg.setStatus("mandatory")


class _Cgfeb100TPSacStat_Type(Integer32):
    """Custom type cgfeb100TPSacStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changed", 1),
          ("constant", 2))
    )


_Cgfeb100TPSacStat_Type.__name__ = "Integer32"
_Cgfeb100TPSacStat_Object = MibTableColumn
cgfeb100TPSacStat = _Cgfeb100TPSacStat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 41),
    _Cgfeb100TPSacStat_Type()
)
cgfeb100TPSacStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100TPSacStat.setStatus("mandatory")
_Cgfeb100ConnB_Type = CpsConnector
_Cgfeb100ConnB_Object = MibTableColumn
cgfeb100ConnB = _Cgfeb100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 42),
    _Cgfeb100ConnB_Type()
)
cgfeb100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100ConnB.setStatus("mandatory")


class _Cgfeb100FiberLink_Type(Integer32):
    """Custom type cgfeb100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cgfeb100FiberLink_Type.__name__ = "Integer32"
_Cgfeb100FiberLink_Object = MibTableColumn
cgfeb100FiberLink = _Cgfeb100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 43),
    _Cgfeb100FiberLink_Type()
)
cgfeb100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100FiberLink.setStatus("mandatory")


class _Cgfeb100FiberFullDuplexCfg_Type(Integer32):
    """Custom type cgfeb100FiberFullDuplexCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("fdx", 1),
          ("hdx", 2))
    )


_Cgfeb100FiberFullDuplexCfg_Type.__name__ = "Integer32"
_Cgfeb100FiberFullDuplexCfg_Object = MibTableColumn
cgfeb100FiberFullDuplexCfg = _Cgfeb100FiberFullDuplexCfg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 44),
    _Cgfeb100FiberFullDuplexCfg_Type()
)
cgfeb100FiberFullDuplexCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100FiberFullDuplexCfg.setStatus("mandatory")


class _Cgfeb100FiberFullDuplexStat_Type(Integer32):
    """Custom type cgfeb100FiberFullDuplexStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fdx", 1),
          ("hdx", 2),
          ("notApplicable", 3))
    )


_Cgfeb100FiberFullDuplexStat_Type.__name__ = "Integer32"
_Cgfeb100FiberFullDuplexStat_Object = MibTableColumn
cgfeb100FiberFullDuplexStat = _Cgfeb100FiberFullDuplexStat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 45),
    _Cgfeb100FiberFullDuplexStat_Type()
)
cgfeb100FiberFullDuplexStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100FiberFullDuplexStat.setStatus("mandatory")


class _Cgfeb100FiberAutoNegot_Type(Integer32):
    """Custom type cgfeb100FiberAutoNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cgfeb100FiberAutoNegot_Type.__name__ = "Integer32"
_Cgfeb100FiberAutoNegot_Object = MibTableColumn
cgfeb100FiberAutoNegot = _Cgfeb100FiberAutoNegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 46),
    _Cgfeb100FiberAutoNegot_Type()
)
cgfeb100FiberAutoNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100FiberAutoNegot.setStatus("mandatory")


class _Cgfeb100FiberAdv1000HDX_Type(Integer32):
    """Custom type cgfeb100FiberAdv1000HDX based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100FiberAdv1000HDX_Type.__name__ = "Integer32"
_Cgfeb100FiberAdv1000HDX_Object = MibTableColumn
cgfeb100FiberAdv1000HDX = _Cgfeb100FiberAdv1000HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 47),
    _Cgfeb100FiberAdv1000HDX_Type()
)
cgfeb100FiberAdv1000HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100FiberAdv1000HDX.setStatus("mandatory")


class _Cgfeb100FiberAdv1000FDX_Type(Integer32):
    """Custom type cgfeb100FiberAdv1000FDX based on Integer32"""
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
        *(("disabledRO", 5),
          ("enabledRO", 4),
          ("no", 2),
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100FiberAdv1000FDX_Type.__name__ = "Integer32"
_Cgfeb100FiberAdv1000FDX_Object = MibTableColumn
cgfeb100FiberAdv1000FDX = _Cgfeb100FiberAdv1000FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 48),
    _Cgfeb100FiberAdv1000FDX_Type()
)
cgfeb100FiberAdv1000FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100FiberAdv1000FDX.setStatus("mandatory")


class _Cgfeb100FiberLpAdv1000HDX_Type(Integer32):
    """Custom type cgfeb100FiberLpAdv1000HDX based on Integer32"""
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
        *(("disabledRO", 5),
          ("enabledRO", 4),
          ("no", 2),
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100FiberLpAdv1000HDX_Type.__name__ = "Integer32"
_Cgfeb100FiberLpAdv1000HDX_Object = MibTableColumn
cgfeb100FiberLpAdv1000HDX = _Cgfeb100FiberLpAdv1000HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 49),
    _Cgfeb100FiberLpAdv1000HDX_Type()
)
cgfeb100FiberLpAdv1000HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100FiberLpAdv1000HDX.setStatus("mandatory")


class _Cgfeb100FiberLpAdv1000FDX_Type(Integer32):
    """Custom type cgfeb100FiberLpAdv1000FDX based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Cgfeb100FiberLpAdv1000FDX_Type.__name__ = "Integer32"
_Cgfeb100FiberLpAdv1000FDX_Object = MibTableColumn
cgfeb100FiberLpAdv1000FDX = _Cgfeb100FiberLpAdv1000FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 50),
    _Cgfeb100FiberLpAdv1000FDX_Type()
)
cgfeb100FiberLpAdv1000FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100FiberLpAdv1000FDX.setStatus("mandatory")


class _Cgfeb100FiberLpAdvPause_Type(Integer32):
    """Custom type cgfeb100FiberLpAdvPause based on Integer32"""
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
        *(("asymRX", 2),
          ("asymTX", 3),
          ("disabled", 4),
          ("notApplicable", 5),
          ("symetric", 1))
    )


_Cgfeb100FiberLpAdvPause_Type.__name__ = "Integer32"
_Cgfeb100FiberLpAdvPause_Object = MibTableColumn
cgfeb100FiberLpAdvPause = _Cgfeb100FiberLpAdvPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 51),
    _Cgfeb100FiberLpAdvPause_Type()
)
cgfeb100FiberLpAdvPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100FiberLpAdvPause.setStatus("mandatory")


class _Cgfeb100FiberAdvPause_Type(Integer32):
    """Custom type cgfeb100FiberAdvPause based on Integer32"""
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
        *(("asymRX", 2),
          ("asymRXRO", 7),
          ("asymTX", 3),
          ("asymTXRO", 8),
          ("disabled", 4),
          ("disabledRO", 9),
          ("notApplicable", 5),
          ("symetric", 1),
          ("symetricRO", 6))
    )


_Cgfeb100FiberAdvPause_Type.__name__ = "Integer32"
_Cgfeb100FiberAdvPause_Object = MibTableColumn
cgfeb100FiberAdvPause = _Cgfeb100FiberAdvPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 52),
    _Cgfeb100FiberAdvPause_Type()
)
cgfeb100FiberAdvPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100FiberAdvPause.setStatus("mandatory")


class _Cgfeb100FiberQosPause_Type(Integer32):
    """Custom type cgfeb100FiberQosPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cgfeb100FiberQosPause_Type.__name__ = "Integer32"
_Cgfeb100FiberQosPause_Object = MibTableColumn
cgfeb100FiberQosPause = _Cgfeb100FiberQosPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 53),
    _Cgfeb100FiberQosPause_Type()
)
cgfeb100FiberQosPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100FiberQosPause.setStatus("mandatory")


class _Cgfeb100FiberSacCfg_Type(Integer32):
    """Custom type cgfeb100FiberSacCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cgfeb100FiberSacCfg_Type.__name__ = "Integer32"
_Cgfeb100FiberSacCfg_Object = MibTableColumn
cgfeb100FiberSacCfg = _Cgfeb100FiberSacCfg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 54),
    _Cgfeb100FiberSacCfg_Type()
)
cgfeb100FiberSacCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100FiberSacCfg.setStatus("mandatory")


class _Cgfeb100FiberSacStat_Type(Integer32):
    """Custom type cgfeb100FiberSacStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changed", 1),
          ("constant", 2))
    )


_Cgfeb100FiberSacStat_Type.__name__ = "Integer32"
_Cgfeb100FiberSacStat_Object = MibTableColumn
cgfeb100FiberSacStat = _Cgfeb100FiberSacStat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 55),
    _Cgfeb100FiberSacStat_Type()
)
cgfeb100FiberSacStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100FiberSacStat.setStatus("mandatory")


class _Cgfeb100MonitorTap_Type(Integer32):
    """Custom type cgfeb100MonitorTap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 3),
          ("receive", 2),
          ("transmit", 1))
    )


_Cgfeb100MonitorTap_Type.__name__ = "Integer32"
_Cgfeb100MonitorTap_Object = MibTableColumn
cgfeb100MonitorTap = _Cgfeb100MonitorTap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 56),
    _Cgfeb100MonitorTap_Type()
)
cgfeb100MonitorTap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgfeb100MonitorTap.setStatus("mandatory")


class _Cgfeb100CacheClean_Type(Integer32):
    """Custom type cgfeb100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Cgfeb100CacheClean_Type.__name__ = "Integer32"
_Cgfeb100CacheClean_Object = MibTableColumn
cgfeb100CacheClean = _Cgfeb100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 23, 1, 57),
    _Cgfeb100CacheClean_Type()
)
cgfeb100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgfeb100CacheClean.setStatus("mandatory")
_Crmfe100Table_Object = MibTable
crmfe100Table = _Crmfe100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24)
)
if mibBuilder.loadTexts:
    crmfe100Table.setStatus("mandatory")
_Crmfe100Entry_Object = MibTableRow
crmfe100Entry = _Crmfe100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1)
)
crmfe100Entry.setIndexNames(
    (0, "MCC16-MIB", "crmfe100BiaIndex"),
    (0, "MCC16-MIB", "crmfe100SlotIndex"),
)
if mibBuilder.loadTexts:
    crmfe100Entry.setStatus("mandatory")
_Crmfe100BiaIndex_Type = Integer32
_Crmfe100BiaIndex_Object = MibTableColumn
crmfe100BiaIndex = _Crmfe100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 1),
    _Crmfe100BiaIndex_Type()
)
crmfe100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100BiaIndex.setStatus("mandatory")
_Crmfe100SlotIndex_Type = Integer32
_Crmfe100SlotIndex_Object = MibTableColumn
crmfe100SlotIndex = _Crmfe100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 2),
    _Crmfe100SlotIndex_Type()
)
crmfe100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100SlotIndex.setStatus("mandatory")
_Crmfe100Groups_Type = DisplayString
_Crmfe100Groups_Object = MibTableColumn
crmfe100Groups = _Crmfe100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 3),
    _Crmfe100Groups_Type()
)
crmfe100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100Groups.setStatus("mandatory")
_Crmfe100MRevision_Type = Integer32
_Crmfe100MRevision_Object = MibTableColumn
crmfe100MRevision = _Crmfe100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 4),
    _Crmfe100MRevision_Type()
)
crmfe100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100MRevision.setStatus("mandatory")


class _Crmfe100CfgMatch_Type(Integer32):
    """Custom type crmfe100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Crmfe100CfgMatch_Type.__name__ = "Integer32"
_Crmfe100CfgMatch_Object = MibTableColumn
crmfe100CfgMatch = _Crmfe100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 5),
    _Crmfe100CfgMatch_Type()
)
crmfe100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100CfgMatch.setStatus("mandatory")
_Crmfe100SerialNumber_Type = Integer32
_Crmfe100SerialNumber_Object = MibTableColumn
crmfe100SerialNumber = _Crmfe100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 6),
    _Crmfe100SerialNumber_Type()
)
crmfe100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100SerialNumber.setStatus("mandatory")
_Crmfe100ConnA_Type = CpsConnector
_Crmfe100ConnA_Object = MibTableColumn
crmfe100ConnA = _Crmfe100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 7),
    _Crmfe100ConnA_Type()
)
crmfe100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100ConnA.setStatus("mandatory")
_Crmfe100ConnB_Type = CpsConnector
_Crmfe100ConnB_Object = MibTableColumn
crmfe100ConnB = _Crmfe100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 8),
    _Crmfe100ConnB_Type()
)
crmfe100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100ConnB.setStatus("mandatory")


class _Crmfe100TPLink_Type(Integer32):
    """Custom type crmfe100TPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Crmfe100TPLink_Type.__name__ = "Integer32"
_Crmfe100TPLink_Object = MibTableColumn
crmfe100TPLink = _Crmfe100TPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 9),
    _Crmfe100TPLink_Type()
)
crmfe100TPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100TPLink.setStatus("mandatory")


class _Crmfe100FiberLink_Type(Integer32):
    """Custom type crmfe100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Crmfe100FiberLink_Type.__name__ = "Integer32"
_Crmfe100FiberLink_Object = MibTableColumn
crmfe100FiberLink = _Crmfe100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 10),
    _Crmfe100FiberLink_Type()
)
crmfe100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100FiberLink.setStatus("mandatory")


class _Crmfe100Fault_Type(Integer32):
    """Custom type crmfe100Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Crmfe100Fault_Type.__name__ = "Integer32"
_Crmfe100Fault_Object = MibTableColumn
crmfe100Fault = _Crmfe100Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 11),
    _Crmfe100Fault_Type()
)
crmfe100Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100Fault.setStatus("mandatory")


class _Crmfe100Autonegot_Type(Integer32):
    """Custom type crmfe100Autonegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Crmfe100Autonegot_Type.__name__ = "Integer32"
_Crmfe100Autonegot_Object = MibTableColumn
crmfe100Autonegot = _Crmfe100Autonegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 12),
    _Crmfe100Autonegot_Type()
)
crmfe100Autonegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100Autonegot.setStatus("mandatory")


class _Crmfe100Enabled_Type(Integer32):
    """Custom type crmfe100Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Crmfe100Enabled_Type.__name__ = "Integer32"
_Crmfe100Enabled_Object = MibTableColumn
crmfe100Enabled = _Crmfe100Enabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 13),
    _Crmfe100Enabled_Type()
)
crmfe100Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100Enabled.setStatus("mandatory")


class _Crmfe100Pause_Type(Integer32):
    """Custom type crmfe100Pause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Crmfe100Pause_Type.__name__ = "Integer32"
_Crmfe100Pause_Object = MibTableColumn
crmfe100Pause = _Crmfe100Pause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 14),
    _Crmfe100Pause_Type()
)
crmfe100Pause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100Pause.setStatus("mandatory")


class _Crmfe100LinkPassThrough_Type(Integer32):
    """Custom type crmfe100LinkPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Crmfe100LinkPassThrough_Type.__name__ = "Integer32"
_Crmfe100LinkPassThrough_Object = MibTableColumn
crmfe100LinkPassThrough = _Crmfe100LinkPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 15),
    _Crmfe100LinkPassThrough_Type()
)
crmfe100LinkPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100LinkPassThrough.setStatus("mandatory")


class _Crmfe100AutoCross_Type(Integer32):
    """Custom type crmfe100AutoCross based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Crmfe100AutoCross_Type.__name__ = "Integer32"
_Crmfe100AutoCross_Object = MibTableColumn
crmfe100AutoCross = _Crmfe100AutoCross_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 16),
    _Crmfe100AutoCross_Type()
)
crmfe100AutoCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100AutoCross.setStatus("mandatory")


class _Crmfe100TPActivity_Type(Integer32):
    """Custom type crmfe100TPActivity based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Crmfe100TPActivity_Type.__name__ = "Integer32"
_Crmfe100TPActivity_Object = MibTableColumn
crmfe100TPActivity = _Crmfe100TPActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 17),
    _Crmfe100TPActivity_Type()
)
crmfe100TPActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100TPActivity.setStatus("mandatory")


class _Crmfe100FiberActivity_Type(Integer32):
    """Custom type crmfe100FiberActivity based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Crmfe100FiberActivity_Type.__name__ = "Integer32"
_Crmfe100FiberActivity_Object = MibTableColumn
crmfe100FiberActivity = _Crmfe100FiberActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 18),
    _Crmfe100FiberActivity_Type()
)
crmfe100FiberActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100FiberActivity.setStatus("mandatory")


class _Crmfe100ConfigMode_Type(Integer32):
    """Custom type crmfe100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Crmfe100ConfigMode_Type.__name__ = "Integer32"
_Crmfe100ConfigMode_Object = MibTableColumn
crmfe100ConfigMode = _Crmfe100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 19),
    _Crmfe100ConfigMode_Type()
)
crmfe100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100ConfigMode.setStatus("mandatory")


class _Crmfe100FarEndFault_Type(Integer32):
    """Custom type crmfe100FarEndFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Crmfe100FarEndFault_Type.__name__ = "Integer32"
_Crmfe100FarEndFault_Object = MibTableColumn
crmfe100FarEndFault = _Crmfe100FarEndFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 20),
    _Crmfe100FarEndFault_Type()
)
crmfe100FarEndFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100FarEndFault.setStatus("mandatory")


class _Crmfe100NetworkMode_Type(Integer32):
    """Custom type crmfe100NetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("tokenRing", 1))
    )


_Crmfe100NetworkMode_Type.__name__ = "Integer32"
_Crmfe100NetworkMode_Object = MibTableColumn
crmfe100NetworkMode = _Crmfe100NetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 21),
    _Crmfe100NetworkMode_Type()
)
crmfe100NetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100NetworkMode.setStatus("mandatory")
_Crmfe100UpTime_Type = TimeTicks
_Crmfe100UpTime_Object = MibTableColumn
crmfe100UpTime = _Crmfe100UpTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 22),
    _Crmfe100UpTime_Type()
)
crmfe100UpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100UpTime.setStatus("mandatory")
_Crmfe100FirmwareRevision_Type = Integer32
_Crmfe100FirmwareRevision_Object = MibTableColumn
crmfe100FirmwareRevision = _Crmfe100FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 23),
    _Crmfe100FirmwareRevision_Type()
)
crmfe100FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100FirmwareRevision.setStatus("mandatory")


class _Crmfe100RmtDetected_Type(Integer32):
    """Custom type crmfe100RmtDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("notDetected", 2))
    )


_Crmfe100RmtDetected_Type.__name__ = "Integer32"
_Crmfe100RmtDetected_Object = MibTableColumn
crmfe100RmtDetected = _Crmfe100RmtDetected_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 24),
    _Crmfe100RmtDetected_Type()
)
crmfe100RmtDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100RmtDetected.setStatus("mandatory")


class _Crmfe100RmtTPLink_Type(Integer32):
    """Custom type crmfe100RmtTPLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1),
          ("notApplicable", 3))
    )


_Crmfe100RmtTPLink_Type.__name__ = "Integer32"
_Crmfe100RmtTPLink_Object = MibTableColumn
crmfe100RmtTPLink = _Crmfe100RmtTPLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 25),
    _Crmfe100RmtTPLink_Type()
)
crmfe100RmtTPLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100RmtTPLink.setStatus("mandatory")


class _Crmfe100RmtFiberLink_Type(Integer32):
    """Custom type crmfe100RmtFiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1),
          ("notApplicable", 3))
    )


_Crmfe100RmtFiberLink_Type.__name__ = "Integer32"
_Crmfe100RmtFiberLink_Object = MibTableColumn
crmfe100RmtFiberLink = _Crmfe100RmtFiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 26),
    _Crmfe100RmtFiberLink_Type()
)
crmfe100RmtFiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100RmtFiberLink.setStatus("mandatory")


class _Crmfe100RmtFault_Type(Integer32):
    """Custom type crmfe100RmtFault based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Crmfe100RmtFault_Type.__name__ = "Integer32"
_Crmfe100RmtFault_Object = MibTableColumn
crmfe100RmtFault = _Crmfe100RmtFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 27),
    _Crmfe100RmtFault_Type()
)
crmfe100RmtFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100RmtFault.setStatus("mandatory")


class _Crmfe100RmtAutonegot_Type(Integer32):
    """Custom type crmfe100RmtAutonegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Crmfe100RmtAutonegot_Type.__name__ = "Integer32"
_Crmfe100RmtAutonegot_Object = MibTableColumn
crmfe100RmtAutonegot = _Crmfe100RmtAutonegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 28),
    _Crmfe100RmtAutonegot_Type()
)
crmfe100RmtAutonegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100RmtAutonegot.setStatus("mandatory")


class _Crmfe100RmtPause_Type(Integer32):
    """Custom type crmfe100RmtPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Crmfe100RmtPause_Type.__name__ = "Integer32"
_Crmfe100RmtPause_Object = MibTableColumn
crmfe100RmtPause = _Crmfe100RmtPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 29),
    _Crmfe100RmtPause_Type()
)
crmfe100RmtPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100RmtPause.setStatus("mandatory")


class _Crmfe100RmtLinkPassThrough_Type(Integer32):
    """Custom type crmfe100RmtLinkPassThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Crmfe100RmtLinkPassThrough_Type.__name__ = "Integer32"
_Crmfe100RmtLinkPassThrough_Object = MibTableColumn
crmfe100RmtLinkPassThrough = _Crmfe100RmtLinkPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 30),
    _Crmfe100RmtLinkPassThrough_Type()
)
crmfe100RmtLinkPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100RmtLinkPassThrough.setStatus("mandatory")


class _Crmfe100RmtAutoCross_Type(Integer32):
    """Custom type crmfe100RmtAutoCross based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Crmfe100RmtAutoCross_Type.__name__ = "Integer32"
_Crmfe100RmtAutoCross_Object = MibTableColumn
crmfe100RmtAutoCross = _Crmfe100RmtAutoCross_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 31),
    _Crmfe100RmtAutoCross_Type()
)
crmfe100RmtAutoCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100RmtAutoCross.setStatus("mandatory")


class _Crmfe100RmtTPActivity_Type(Integer32):
    """Custom type crmfe100RmtTPActivity based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Crmfe100RmtTPActivity_Type.__name__ = "Integer32"
_Crmfe100RmtTPActivity_Object = MibTableColumn
crmfe100RmtTPActivity = _Crmfe100RmtTPActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 32),
    _Crmfe100RmtTPActivity_Type()
)
crmfe100RmtTPActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100RmtTPActivity.setStatus("mandatory")


class _Crmfe100RmtFiberActivity_Type(Integer32):
    """Custom type crmfe100RmtFiberActivity based on Integer32"""
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
          ("notSupported", 3),
          ("yes", 1))
    )


_Crmfe100RmtFiberActivity_Type.__name__ = "Integer32"
_Crmfe100RmtFiberActivity_Object = MibTableColumn
crmfe100RmtFiberActivity = _Crmfe100RmtFiberActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 33),
    _Crmfe100RmtFiberActivity_Type()
)
crmfe100RmtFiberActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100RmtFiberActivity.setStatus("mandatory")


class _Crmfe100RmtConfigMode_Type(Integer32):
    """Custom type crmfe100RmtConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("notApplicable", 3),
          ("software", 1))
    )


_Crmfe100RmtConfigMode_Type.__name__ = "Integer32"
_Crmfe100RmtConfigMode_Object = MibTableColumn
crmfe100RmtConfigMode = _Crmfe100RmtConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 34),
    _Crmfe100RmtConfigMode_Type()
)
crmfe100RmtConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100RmtConfigMode.setStatus("mandatory")


class _Crmfe100RmtFarEndFault_Type(Integer32):
    """Custom type crmfe100RmtFarEndFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Crmfe100RmtFarEndFault_Type.__name__ = "Integer32"
_Crmfe100RmtFarEndFault_Object = MibTableColumn
crmfe100RmtFarEndFault = _Crmfe100RmtFarEndFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 35),
    _Crmfe100RmtFarEndFault_Type()
)
crmfe100RmtFarEndFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100RmtFarEndFault.setStatus("mandatory")


class _Crmfe100RmtLoopback_Type(Integer32):
    """Custom type crmfe100RmtLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Crmfe100RmtLoopback_Type.__name__ = "Integer32"
_Crmfe100RmtLoopback_Object = MibTableColumn
crmfe100RmtLoopback = _Crmfe100RmtLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 36),
    _Crmfe100RmtLoopback_Type()
)
crmfe100RmtLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100RmtLoopback.setStatus("mandatory")


class _Crmfe100RmtNetworkMode_Type(Integer32):
    """Custom type crmfe100RmtNetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("notApplicable", 3),
          ("tokenRing", 1))
    )


_Crmfe100RmtNetworkMode_Type.__name__ = "Integer32"
_Crmfe100RmtNetworkMode_Object = MibTableColumn
crmfe100RmtNetworkMode = _Crmfe100RmtNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 37),
    _Crmfe100RmtNetworkMode_Type()
)
crmfe100RmtNetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100RmtNetworkMode.setStatus("mandatory")
_Crmfe100RmtUpTime_Type = TimeTicks
_Crmfe100RmtUpTime_Object = MibTableColumn
crmfe100RmtUpTime = _Crmfe100RmtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 38),
    _Crmfe100RmtUpTime_Type()
)
crmfe100RmtUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100RmtUpTime.setStatus("mandatory")
_Crmfe100TxFxBwa_Type = Integer32
_Crmfe100TxFxBwa_Object = MibTableColumn
crmfe100TxFxBwa = _Crmfe100TxFxBwa_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 39),
    _Crmfe100TxFxBwa_Type()
)
crmfe100TxFxBwa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100TxFxBwa.setStatus("mandatory")
_Crmfe100FxTxBwa_Type = Integer32
_Crmfe100FxTxBwa_Object = MibTableColumn
crmfe100FxTxBwa = _Crmfe100FxTxBwa_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 40),
    _Crmfe100FxTxBwa_Type()
)
crmfe100FxTxBwa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100FxTxBwa.setStatus("mandatory")
_Crmfe100TxBytesH_Type = Integer32
_Crmfe100TxBytesH_Object = MibTableColumn
crmfe100TxBytesH = _Crmfe100TxBytesH_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 41),
    _Crmfe100TxBytesH_Type()
)
crmfe100TxBytesH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100TxBytesH.setStatus("mandatory")
_Crmfe100TxBytesL_Type = Integer32
_Crmfe100TxBytesL_Object = MibTableColumn
crmfe100TxBytesL = _Crmfe100TxBytesL_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 42),
    _Crmfe100TxBytesL_Type()
)
crmfe100TxBytesL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100TxBytesL.setStatus("mandatory")
_Crmfe100FxBytesH_Type = Integer32
_Crmfe100FxBytesH_Object = MibTableColumn
crmfe100FxBytesH = _Crmfe100FxBytesH_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 43),
    _Crmfe100FxBytesH_Type()
)
crmfe100FxBytesH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100FxBytesH.setStatus("mandatory")
_Crmfe100FxBytesL_Type = Integer32
_Crmfe100FxBytesL_Object = MibTableColumn
crmfe100FxBytesL = _Crmfe100FxBytesL_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 44),
    _Crmfe100FxBytesL_Type()
)
crmfe100FxBytesL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100FxBytesL.setStatus("mandatory")
_Crmfe100MscRxBytes_Type = Integer32
_Crmfe100MscRxBytes_Object = MibTableColumn
crmfe100MscRxBytes = _Crmfe100MscRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 45),
    _Crmfe100MscRxBytes_Type()
)
crmfe100MscRxBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100MscRxBytes.setStatus("mandatory")
_Crmfe100MscTxBytes_Type = Integer32
_Crmfe100MscTxBytes_Object = MibTableColumn
crmfe100MscTxBytes = _Crmfe100MscTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 46),
    _Crmfe100MscTxBytes_Type()
)
crmfe100MscTxBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100MscTxBytes.setStatus("mandatory")


class _Crmfe100CacheClean_Type(Integer32):
    """Custom type crmfe100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Crmfe100CacheClean_Type.__name__ = "Integer32"
_Crmfe100CacheClean_Object = MibTableColumn
crmfe100CacheClean = _Crmfe100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 47),
    _Crmfe100CacheClean_Type()
)
crmfe100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmfe100CacheClean.setStatus("mandatory")
_Crmfe100MbTxFxBwa_Type = Integer32
_Crmfe100MbTxFxBwa_Object = MibTableColumn
crmfe100MbTxFxBwa = _Crmfe100MbTxFxBwa_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 48),
    _Crmfe100MbTxFxBwa_Type()
)
crmfe100MbTxFxBwa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100MbTxFxBwa.setStatus("mandatory")
_Crmfe100MbFxTxBwa_Type = Integer32
_Crmfe100MbFxTxBwa_Object = MibTableColumn
crmfe100MbFxTxBwa = _Crmfe100MbFxTxBwa_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 24, 1, 49),
    _Crmfe100MbFxTxBwa_Type()
)
crmfe100MbFxTxBwa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmfe100MbFxTxBwa.setStatus("mandatory")
_Crs2f100Table_Object = MibTable
crs2f100Table = _Crs2f100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25)
)
if mibBuilder.loadTexts:
    crs2f100Table.setStatus("mandatory")
_Crs2f100Entry_Object = MibTableRow
crs2f100Entry = _Crs2f100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1)
)
crs2f100Entry.setIndexNames(
    (0, "MCC16-MIB", "crs2f100BiaIndex"),
    (0, "MCC16-MIB", "crs2f100SlotIndex"),
)
if mibBuilder.loadTexts:
    crs2f100Entry.setStatus("mandatory")
_Crs2f100BiaIndex_Type = Integer32
_Crs2f100BiaIndex_Object = MibTableColumn
crs2f100BiaIndex = _Crs2f100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 1),
    _Crs2f100BiaIndex_Type()
)
crs2f100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100BiaIndex.setStatus("mandatory")
_Crs2f100SlotIndex_Type = Integer32
_Crs2f100SlotIndex_Object = MibTableColumn
crs2f100SlotIndex = _Crs2f100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 2),
    _Crs2f100SlotIndex_Type()
)
crs2f100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100SlotIndex.setStatus("mandatory")
_Crs2f100Groups_Type = DisplayString
_Crs2f100Groups_Object = MibTableColumn
crs2f100Groups = _Crs2f100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 3),
    _Crs2f100Groups_Type()
)
crs2f100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crs2f100Groups.setStatus("mandatory")
_Crs2f100MRevision_Type = Integer32
_Crs2f100MRevision_Object = MibTableColumn
crs2f100MRevision = _Crs2f100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 4),
    _Crs2f100MRevision_Type()
)
crs2f100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100MRevision.setStatus("mandatory")


class _Crs2f100CfgMatch_Type(Integer32):
    """Custom type crs2f100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Crs2f100CfgMatch_Type.__name__ = "Integer32"
_Crs2f100CfgMatch_Object = MibTableColumn
crs2f100CfgMatch = _Crs2f100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 5),
    _Crs2f100CfgMatch_Type()
)
crs2f100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100CfgMatch.setStatus("mandatory")
_Crs2f100SerialNumber_Type = Integer32
_Crs2f100SerialNumber_Object = MibTableColumn
crs2f100SerialNumber = _Crs2f100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 6),
    _Crs2f100SerialNumber_Type()
)
crs2f100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100SerialNumber.setStatus("mandatory")
_Crs2f100ConnA_Type = CpsConnector
_Crs2f100ConnA_Object = MibTableColumn
crs2f100ConnA = _Crs2f100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 7),
    _Crs2f100ConnA_Type()
)
crs2f100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100ConnA.setStatus("mandatory")
_Crs2f100ConnB_Type = CpsConnector
_Crs2f100ConnB_Object = MibTableColumn
crs2f100ConnB = _Crs2f100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 8),
    _Crs2f100ConnB_Type()
)
crs2f100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100ConnB.setStatus("mandatory")


class _Crs2f100FiberLink_Type(Integer32):
    """Custom type crs2f100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Crs2f100FiberLink_Type.__name__ = "Integer32"
_Crs2f100FiberLink_Object = MibTableColumn
crs2f100FiberLink = _Crs2f100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 9),
    _Crs2f100FiberLink_Type()
)
crs2f100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100FiberLink.setStatus("mandatory")


class _Crs2f100Fault_Type(Integer32):
    """Custom type crs2f100Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Crs2f100Fault_Type.__name__ = "Integer32"
_Crs2f100Fault_Object = MibTableColumn
crs2f100Fault = _Crs2f100Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 10),
    _Crs2f100Fault_Type()
)
crs2f100Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100Fault.setStatus("mandatory")
_Crs2f100FirmwareRevision_Type = Integer32
_Crs2f100FirmwareRevision_Object = MibTableColumn
crs2f100FirmwareRevision = _Crs2f100FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 11),
    _Crs2f100FirmwareRevision_Type()
)
crs2f100FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100FirmwareRevision.setStatus("mandatory")


class _Crs2f100Loopback_Type(Integer32):
    """Custom type crs2f100Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Crs2f100Loopback_Type.__name__ = "Integer32"
_Crs2f100Loopback_Object = MibTableColumn
crs2f100Loopback = _Crs2f100Loopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 12),
    _Crs2f100Loopback_Type()
)
crs2f100Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crs2f100Loopback.setStatus("mandatory")


class _Crs2f100DCE_Type(Integer32):
    """Custom type crs2f100DCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dCE", 1),
          ("dTE", 2))
    )


_Crs2f100DCE_Type.__name__ = "Integer32"
_Crs2f100DCE_Object = MibTableColumn
crs2f100DCE = _Crs2f100DCE_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 13),
    _Crs2f100DCE_Type()
)
crs2f100DCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100DCE.setStatus("mandatory")


class _Crs2f100CopperActivity_Type(Integer32):
    """Custom type crs2f100CopperActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Crs2f100CopperActivity_Type.__name__ = "Integer32"
_Crs2f100CopperActivity_Object = MibTableColumn
crs2f100CopperActivity = _Crs2f100CopperActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 14),
    _Crs2f100CopperActivity_Type()
)
crs2f100CopperActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100CopperActivity.setStatus("mandatory")


class _Crs2f100ConfigMode_Type(Integer32):
    """Custom type crs2f100ConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_Crs2f100ConfigMode_Type.__name__ = "Integer32"
_Crs2f100ConfigMode_Object = MibTableColumn
crs2f100ConfigMode = _Crs2f100ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 15),
    _Crs2f100ConfigMode_Type()
)
crs2f100ConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100ConfigMode.setStatus("mandatory")


class _Crs2f100RmtDetected_Type(Integer32):
    """Custom type crs2f100RmtDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Crs2f100RmtDetected_Type.__name__ = "Integer32"
_Crs2f100RmtDetected_Object = MibTableColumn
crs2f100RmtDetected = _Crs2f100RmtDetected_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 16),
    _Crs2f100RmtDetected_Type()
)
crs2f100RmtDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100RmtDetected.setStatus("mandatory")


class _Crs2f100RmtLoopback_Type(Integer32):
    """Custom type crs2f100RmtLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Crs2f100RmtLoopback_Type.__name__ = "Integer32"
_Crs2f100RmtLoopback_Object = MibTableColumn
crs2f100RmtLoopback = _Crs2f100RmtLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 17),
    _Crs2f100RmtLoopback_Type()
)
crs2f100RmtLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crs2f100RmtLoopback.setStatus("mandatory")


class _Crs2f100RmtDCE_Type(Integer32):
    """Custom type crs2f100RmtDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dCE", 1),
          ("dTE", 2),
          ("notApplicable", 3))
    )


_Crs2f100RmtDCE_Type.__name__ = "Integer32"
_Crs2f100RmtDCE_Object = MibTableColumn
crs2f100RmtDCE = _Crs2f100RmtDCE_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 18),
    _Crs2f100RmtDCE_Type()
)
crs2f100RmtDCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100RmtDCE.setStatus("mandatory")


class _Crs2f100RmtCopperActivity_Type(Integer32):
    """Custom type crs2f100RmtCopperActivity based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Crs2f100RmtCopperActivity_Type.__name__ = "Integer32"
_Crs2f100RmtCopperActivity_Object = MibTableColumn
crs2f100RmtCopperActivity = _Crs2f100RmtCopperActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 19),
    _Crs2f100RmtCopperActivity_Type()
)
crs2f100RmtCopperActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100RmtCopperActivity.setStatus("mandatory")


class _Crs2f100RmtConfigMode_Type(Integer32):
    """Custom type crs2f100RmtConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("notApplicable", 3),
          ("software", 1))
    )


_Crs2f100RmtConfigMode_Type.__name__ = "Integer32"
_Crs2f100RmtConfigMode_Object = MibTableColumn
crs2f100RmtConfigMode = _Crs2f100RmtConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 20),
    _Crs2f100RmtConfigMode_Type()
)
crs2f100RmtConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100RmtConfigMode.setStatus("mandatory")


class _Crs2f100CacheClean_Type(Integer32):
    """Custom type crs2f100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Crs2f100CacheClean_Type.__name__ = "Integer32"
_Crs2f100CacheClean_Object = MibTableColumn
crs2f100CacheClean = _Crs2f100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 25, 1, 21),
    _Crs2f100CacheClean_Type()
)
crs2f100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs2f100CacheClean.setStatus("mandatory")
_Crs4f100Table_Object = MibTable
crs4f100Table = _Crs4f100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26)
)
if mibBuilder.loadTexts:
    crs4f100Table.setStatus("mandatory")
_Crs4f100Entry_Object = MibTableRow
crs4f100Entry = _Crs4f100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1)
)
crs4f100Entry.setIndexNames(
    (0, "MCC16-MIB", "crs4f100BiaIndex"),
    (0, "MCC16-MIB", "crs4f100SlotIndex"),
)
if mibBuilder.loadTexts:
    crs4f100Entry.setStatus("mandatory")
_Crs4f100BiaIndex_Type = Integer32
_Crs4f100BiaIndex_Object = MibTableColumn
crs4f100BiaIndex = _Crs4f100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 1),
    _Crs4f100BiaIndex_Type()
)
crs4f100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100BiaIndex.setStatus("mandatory")
_Crs4f100SlotIndex_Type = Integer32
_Crs4f100SlotIndex_Object = MibTableColumn
crs4f100SlotIndex = _Crs4f100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 2),
    _Crs4f100SlotIndex_Type()
)
crs4f100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100SlotIndex.setStatus("mandatory")
_Crs4f100Groups_Type = DisplayString
_Crs4f100Groups_Object = MibTableColumn
crs4f100Groups = _Crs4f100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 3),
    _Crs4f100Groups_Type()
)
crs4f100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crs4f100Groups.setStatus("mandatory")
_Crs4f100MRevision_Type = Integer32
_Crs4f100MRevision_Object = MibTableColumn
crs4f100MRevision = _Crs4f100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 4),
    _Crs4f100MRevision_Type()
)
crs4f100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100MRevision.setStatus("mandatory")


class _Crs4f100CfgMatch_Type(Integer32):
    """Custom type crs4f100CfgMatch based on Integer32"""
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
          ("notApplicable", 3),
          ("yes", 1))
    )


_Crs4f100CfgMatch_Type.__name__ = "Integer32"
_Crs4f100CfgMatch_Object = MibTableColumn
crs4f100CfgMatch = _Crs4f100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 5),
    _Crs4f100CfgMatch_Type()
)
crs4f100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100CfgMatch.setStatus("mandatory")
_Crs4f100SerialNumber_Type = Integer32
_Crs4f100SerialNumber_Object = MibTableColumn
crs4f100SerialNumber = _Crs4f100SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 6),
    _Crs4f100SerialNumber_Type()
)
crs4f100SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100SerialNumber.setStatus("mandatory")
_Crs4f100ConnA_Type = CpsConnector
_Crs4f100ConnA_Object = MibTableColumn
crs4f100ConnA = _Crs4f100ConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 7),
    _Crs4f100ConnA_Type()
)
crs4f100ConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100ConnA.setStatus("mandatory")
_Crs4f100ConnB_Type = CpsConnector
_Crs4f100ConnB_Object = MibTableColumn
crs4f100ConnB = _Crs4f100ConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 8),
    _Crs4f100ConnB_Type()
)
crs4f100ConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100ConnB.setStatus("mandatory")


class _Crs4f100FiberLink_Type(Integer32):
    """Custom type crs4f100FiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_Crs4f100FiberLink_Type.__name__ = "Integer32"
_Crs4f100FiberLink_Object = MibTableColumn
crs4f100FiberLink = _Crs4f100FiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 9),
    _Crs4f100FiberLink_Type()
)
crs4f100FiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100FiberLink.setStatus("mandatory")


class _Crs4f100Fault_Type(Integer32):
    """Custom type crs4f100Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Crs4f100Fault_Type.__name__ = "Integer32"
_Crs4f100Fault_Object = MibTableColumn
crs4f100Fault = _Crs4f100Fault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 10),
    _Crs4f100Fault_Type()
)
crs4f100Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100Fault.setStatus("mandatory")
_Crs4f100FirmwareRevision_Type = Integer32
_Crs4f100FirmwareRevision_Object = MibTableColumn
crs4f100FirmwareRevision = _Crs4f100FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 11),
    _Crs4f100FirmwareRevision_Type()
)
crs4f100FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100FirmwareRevision.setStatus("mandatory")


class _Crs4f100CopperActivity_Type(Integer32):
    """Custom type crs4f100CopperActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Crs4f100CopperActivity_Type.__name__ = "Integer32"
_Crs4f100CopperActivity_Object = MibTableColumn
crs4f100CopperActivity = _Crs4f100CopperActivity_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 12),
    _Crs4f100CopperActivity_Type()
)
crs4f100CopperActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100CopperActivity.setStatus("mandatory")


class _Crs4f100CacheClean_Type(Integer32):
    """Custom type crs4f100CacheClean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean", 1),
          ("dirty", 2))
    )


_Crs4f100CacheClean_Type.__name__ = "Integer32"
_Crs4f100CacheClean_Object = MibTableColumn
crs4f100CacheClean = _Crs4f100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 26, 1, 13),
    _Crs4f100CacheClean_Type()
)
crs4f100CacheClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crs4f100CacheClean.setStatus("mandatory")
_Cmefg100Table_Object = MibTable
cmefg100Table = _Cmefg100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27)
)
if mibBuilder.loadTexts:
    cmefg100Table.setStatus("mandatory")
_Cmefg100Entry_Object = MibTableRow
cmefg100Entry = _Cmefg100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1)
)
cmefg100Entry.setIndexNames(
    (0, "MCC16-MIB", "cmefg100SubDeviceIndex"),
    (0, "MCC16-MIB", "cmefg100BiaIndex"),
    (0, "MCC16-MIB", "cmefg100SlotIndex"),
)
if mibBuilder.loadTexts:
    cmefg100Entry.setStatus("mandatory")
_Cmefg100SubDeviceIndex_Type = Integer32
_Cmefg100SubDeviceIndex_Object = MibTableColumn
cmefg100SubDeviceIndex = _Cmefg100SubDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 1),
    _Cmefg100SubDeviceIndex_Type()
)
cmefg100SubDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100SubDeviceIndex.setStatus("mandatory")
_Cmefg100BiaIndex_Type = Integer32
_Cmefg100BiaIndex_Object = MibTableColumn
cmefg100BiaIndex = _Cmefg100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 2),
    _Cmefg100BiaIndex_Type()
)
cmefg100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100BiaIndex.setStatus("mandatory")
_Cmefg100SlotIndex_Type = Integer32
_Cmefg100SlotIndex_Object = MibTableColumn
cmefg100SlotIndex = _Cmefg100SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 3),
    _Cmefg100SlotIndex_Type()
)
cmefg100SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100SlotIndex.setStatus("mandatory")
_Cmefg100Groups_Type = DisplayString
_Cmefg100Groups_Object = MibTableColumn
cmefg100Groups = _Cmefg100Groups_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 4),
    _Cmefg100Groups_Type()
)
cmefg100Groups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100Groups.setStatus("mandatory")
_Cmefg100MRevision_Type = Integer32
_Cmefg100MRevision_Object = MibTableColumn
cmefg100MRevision = _Cmefg100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 5),
    _Cmefg100MRevision_Type()
)
cmefg100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100MRevision.setStatus("mandatory")


class _Cmefg100CfgMatch_Type(Integer32):
    """Custom type cmefg100CfgMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cmefg100CfgMatch_Type.__name__ = "Integer32"
_Cmefg100CfgMatch_Object = MibTableColumn
cmefg100CfgMatch = _Cmefg100CfgMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 6),
    _Cmefg100CfgMatch_Type()
)
cmefg100CfgMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100CfgMatch.setStatus("mandatory")


class _Cmefg100ImcLocEnable_Type(Integer32):
    """Custom type cmefg100ImcLocEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100ImcLocEnable_Type.__name__ = "Integer32"
_Cmefg100ImcLocEnable_Object = MibTableColumn
cmefg100ImcLocEnable = _Cmefg100ImcLocEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 7),
    _Cmefg100ImcLocEnable_Type()
)
cmefg100ImcLocEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100ImcLocEnable.setStatus("mandatory")


class _Cmefg100ImcLocReset_Type(Integer32):
    """Custom type cmefg100ImcLocReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 2),
          ("reset", 1))
    )


_Cmefg100ImcLocReset_Type.__name__ = "Integer32"
_Cmefg100ImcLocReset_Object = MibTableColumn
cmefg100ImcLocReset = _Cmefg100ImcLocReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 8),
    _Cmefg100ImcLocReset_Type()
)
cmefg100ImcLocReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100ImcLocReset.setStatus("mandatory")


class _Cmefg100ImcRmtEnable_Type(Integer32):
    """Custom type cmefg100ImcRmtEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100ImcRmtEnable_Type.__name__ = "Integer32"
_Cmefg100ImcRmtEnable_Object = MibTableColumn
cmefg100ImcRmtEnable = _Cmefg100ImcRmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 9),
    _Cmefg100ImcRmtEnable_Type()
)
cmefg100ImcRmtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100ImcRmtEnable.setStatus("mandatory")


class _Cmefg100ImcRmtReset_Type(Integer32):
    """Custom type cmefg100ImcRmtReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 2),
          ("reset", 1))
    )


_Cmefg100ImcRmtReset_Type.__name__ = "Integer32"
_Cmefg100ImcRmtReset_Object = MibTableColumn
cmefg100ImcRmtReset = _Cmefg100ImcRmtReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 10),
    _Cmefg100ImcRmtReset_Type()
)
cmefg100ImcRmtReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100ImcRmtReset.setStatus("mandatory")
_Cmefg100ImcRxAlignmentErrorsTbl_Type = Integer32
_Cmefg100ImcRxAlignmentErrorsTbl_Object = MibTableColumn
cmefg100ImcRxAlignmentErrorsTbl = _Cmefg100ImcRxAlignmentErrorsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 11),
    _Cmefg100ImcRxAlignmentErrorsTbl_Type()
)
cmefg100ImcRxAlignmentErrorsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxAlignmentErrorsTbl.setStatus("mandatory")
_Cmefg100ImcRxBroadcastPktsTbl_Type = Integer32
_Cmefg100ImcRxBroadcastPktsTbl_Object = MibTableColumn
cmefg100ImcRxBroadcastPktsTbl = _Cmefg100ImcRxBroadcastPktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 12),
    _Cmefg100ImcRxBroadcastPktsTbl_Type()
)
cmefg100ImcRxBroadcastPktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxBroadcastPktsTbl.setStatus("mandatory")
_Cmefg100ImcRxDropPktsTbl_Type = Integer32
_Cmefg100ImcRxDropPktsTbl_Object = MibTableColumn
cmefg100ImcRxDropPktsTbl = _Cmefg100ImcRxDropPktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 13),
    _Cmefg100ImcRxDropPktsTbl_Type()
)
cmefg100ImcRxDropPktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxDropPktsTbl.setStatus("mandatory")
_Cmefg100ImcRxExcessSizeDiscTbl_Type = Integer32
_Cmefg100ImcRxExcessSizeDiscTbl_Object = MibTableColumn
cmefg100ImcRxExcessSizeDiscTbl = _Cmefg100ImcRxExcessSizeDiscTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 14),
    _Cmefg100ImcRxExcessSizeDiscTbl_Type()
)
cmefg100ImcRxExcessSizeDiscTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxExcessSizeDiscTbl.setStatus("mandatory")
_Cmefg100ImcRxFCSErrorsTbl_Type = Integer32
_Cmefg100ImcRxFCSErrorsTbl_Object = MibTableColumn
cmefg100ImcRxFCSErrorsTbl = _Cmefg100ImcRxFCSErrorsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 15),
    _Cmefg100ImcRxFCSErrorsTbl_Type()
)
cmefg100ImcRxFCSErrorsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxFCSErrorsTbl.setStatus("mandatory")
_Cmefg100ImcRxFragmentsTbl_Type = Integer32
_Cmefg100ImcRxFragmentsTbl_Object = MibTableColumn
cmefg100ImcRxFragmentsTbl = _Cmefg100ImcRxFragmentsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 16),
    _Cmefg100ImcRxFragmentsTbl_Type()
)
cmefg100ImcRxFragmentsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxFragmentsTbl.setStatus("mandatory")
_Cmefg100ImcRxGoodOctetsTbl_Type = Integer32
_Cmefg100ImcRxGoodOctetsTbl_Object = MibTableColumn
cmefg100ImcRxGoodOctetsTbl = _Cmefg100ImcRxGoodOctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 17),
    _Cmefg100ImcRxGoodOctetsTbl_Type()
)
cmefg100ImcRxGoodOctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxGoodOctetsTbl.setStatus("mandatory")
_Cmefg100ImcRxGoodOctetsWrapTbl_Type = Integer32
_Cmefg100ImcRxGoodOctetsWrapTbl_Object = MibTableColumn
cmefg100ImcRxGoodOctetsWrapTbl = _Cmefg100ImcRxGoodOctetsWrapTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 18),
    _Cmefg100ImcRxGoodOctetsWrapTbl_Type()
)
cmefg100ImcRxGoodOctetsWrapTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxGoodOctetsWrapTbl.setStatus("mandatory")
_Cmefg100ImcRxJabbersTbl_Type = Integer32
_Cmefg100ImcRxJabbersTbl_Object = MibTableColumn
cmefg100ImcRxJabbersTbl = _Cmefg100ImcRxJabbersTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 19),
    _Cmefg100ImcRxJabbersTbl_Type()
)
cmefg100ImcRxJabbersTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxJabbersTbl.setStatus("mandatory")
_Cmefg100ImcRxMulticastPktsTbl_Type = Integer32
_Cmefg100ImcRxMulticastPktsTbl_Object = MibTableColumn
cmefg100ImcRxMulticastPktsTbl = _Cmefg100ImcRxMulticastPktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 20),
    _Cmefg100ImcRxMulticastPktsTbl_Type()
)
cmefg100ImcRxMulticastPktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxMulticastPktsTbl.setStatus("mandatory")
_Cmefg100ImcRxOctetsTbl_Type = Integer32
_Cmefg100ImcRxOctetsTbl_Object = MibTableColumn
cmefg100ImcRxOctetsTbl = _Cmefg100ImcRxOctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 21),
    _Cmefg100ImcRxOctetsTbl_Type()
)
cmefg100ImcRxOctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxOctetsTbl.setStatus("mandatory")
_Cmefg100ImcRxOctetsWrapTbl_Type = Integer32
_Cmefg100ImcRxOctetsWrapTbl_Object = MibTableColumn
cmefg100ImcRxOctetsWrapTbl = _Cmefg100ImcRxOctetsWrapTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 22),
    _Cmefg100ImcRxOctetsWrapTbl_Type()
)
cmefg100ImcRxOctetsWrapTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxOctetsWrapTbl.setStatus("mandatory")
_Cmefg100ImcRxOversizePktsTbl_Type = Integer32
_Cmefg100ImcRxOversizePktsTbl_Object = MibTableColumn
cmefg100ImcRxOversizePktsTbl = _Cmefg100ImcRxOversizePktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 23),
    _Cmefg100ImcRxOversizePktsTbl_Type()
)
cmefg100ImcRxOversizePktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxOversizePktsTbl.setStatus("mandatory")
_Cmefg100ImcRxPausePktsTbl_Type = Integer32
_Cmefg100ImcRxPausePktsTbl_Object = MibTableColumn
cmefg100ImcRxPausePktsTbl = _Cmefg100ImcRxPausePktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 24),
    _Cmefg100ImcRxPausePktsTbl_Type()
)
cmefg100ImcRxPausePktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxPausePktsTbl.setStatus("mandatory")
_Cmefg100ImcRxPkts1024to1522OctetsTbl_Type = Integer32
_Cmefg100ImcRxPkts1024to1522OctetsTbl_Object = MibTableColumn
cmefg100ImcRxPkts1024to1522OctetsTbl = _Cmefg100ImcRxPkts1024to1522OctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 25),
    _Cmefg100ImcRxPkts1024to1522OctetsTbl_Type()
)
cmefg100ImcRxPkts1024to1522OctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxPkts1024to1522OctetsTbl.setStatus("mandatory")
_Cmefg100ImcRxPkts128to255OctetsTbl_Type = Integer32
_Cmefg100ImcRxPkts128to255OctetsTbl_Object = MibTableColumn
cmefg100ImcRxPkts128to255OctetsTbl = _Cmefg100ImcRxPkts128to255OctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 26),
    _Cmefg100ImcRxPkts128to255OctetsTbl_Type()
)
cmefg100ImcRxPkts128to255OctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxPkts128to255OctetsTbl.setStatus("mandatory")
_Cmefg100ImcRxPkts256to511OctetsTbl_Type = Integer32
_Cmefg100ImcRxPkts256to511OctetsTbl_Object = MibTableColumn
cmefg100ImcRxPkts256to511OctetsTbl = _Cmefg100ImcRxPkts256to511OctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 27),
    _Cmefg100ImcRxPkts256to511OctetsTbl_Type()
)
cmefg100ImcRxPkts256to511OctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxPkts256to511OctetsTbl.setStatus("mandatory")
_Cmefg100ImcRxPkts512to1023OctetsTbl_Type = Integer32
_Cmefg100ImcRxPkts512to1023OctetsTbl_Object = MibTableColumn
cmefg100ImcRxPkts512to1023OctetsTbl = _Cmefg100ImcRxPkts512to1023OctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 28),
    _Cmefg100ImcRxPkts512to1023OctetsTbl_Type()
)
cmefg100ImcRxPkts512to1023OctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxPkts512to1023OctetsTbl.setStatus("mandatory")
_Cmefg100ImcRxPkts64OctetsTbl_Type = Integer32
_Cmefg100ImcRxPkts64OctetsTbl_Object = MibTableColumn
cmefg100ImcRxPkts64OctetsTbl = _Cmefg100ImcRxPkts64OctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 29),
    _Cmefg100ImcRxPkts64OctetsTbl_Type()
)
cmefg100ImcRxPkts64OctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxPkts64OctetsTbl.setStatus("mandatory")
_Cmefg100ImcRxPkts65to127OctetsTbl_Type = Integer32
_Cmefg100ImcRxPkts65to127OctetsTbl_Object = MibTableColumn
cmefg100ImcRxPkts65to127OctetsTbl = _Cmefg100ImcRxPkts65to127OctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 30),
    _Cmefg100ImcRxPkts65to127OctetsTbl_Type()
)
cmefg100ImcRxPkts65to127OctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxPkts65to127OctetsTbl.setStatus("mandatory")
_Cmefg100ImcRxQosOctetsTbl_Type = Integer32
_Cmefg100ImcRxQosOctetsTbl_Object = MibTableColumn
cmefg100ImcRxQosOctetsTbl = _Cmefg100ImcRxQosOctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 31),
    _Cmefg100ImcRxQosOctetsTbl_Type()
)
cmefg100ImcRxQosOctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxQosOctetsTbl.setStatus("mandatory")
_Cmefg100ImcRxQosOctetsWrapTbl_Type = Integer32
_Cmefg100ImcRxQosOctetsWrapTbl_Object = MibTableColumn
cmefg100ImcRxQosOctetsWrapTbl = _Cmefg100ImcRxQosOctetsWrapTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 32),
    _Cmefg100ImcRxQosOctetsWrapTbl_Type()
)
cmefg100ImcRxQosOctetsWrapTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxQosOctetsWrapTbl.setStatus("mandatory")
_Cmefg100ImcRxQosPktsTbl_Type = Integer32
_Cmefg100ImcRxQosPktsTbl_Object = MibTableColumn
cmefg100ImcRxQosPktsTbl = _Cmefg100ImcRxQosPktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 33),
    _Cmefg100ImcRxQosPktsTbl_Type()
)
cmefg100ImcRxQosPktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxQosPktsTbl.setStatus("mandatory")
_Cmefg100ImcRxSAChangesTbl_Type = Integer32
_Cmefg100ImcRxSAChangesTbl_Object = MibTableColumn
cmefg100ImcRxSAChangesTbl = _Cmefg100ImcRxSAChangesTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 34),
    _Cmefg100ImcRxSAChangesTbl_Type()
)
cmefg100ImcRxSAChangesTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxSAChangesTbl.setStatus("mandatory")
_Cmefg100ImcRxSymbolErrorTbl_Type = Integer32
_Cmefg100ImcRxSymbolErrorTbl_Object = MibTableColumn
cmefg100ImcRxSymbolErrorTbl = _Cmefg100ImcRxSymbolErrorTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 35),
    _Cmefg100ImcRxSymbolErrorTbl_Type()
)
cmefg100ImcRxSymbolErrorTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxSymbolErrorTbl.setStatus("mandatory")
_Cmefg100ImcRxUndersizePktsTbl_Type = Integer32
_Cmefg100ImcRxUndersizePktsTbl_Object = MibTableColumn
cmefg100ImcRxUndersizePktsTbl = _Cmefg100ImcRxUndersizePktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 36),
    _Cmefg100ImcRxUndersizePktsTbl_Type()
)
cmefg100ImcRxUndersizePktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxUndersizePktsTbl.setStatus("mandatory")
_Cmefg100ImcRxUnicastPktsTbl_Type = Integer32
_Cmefg100ImcRxUnicastPktsTbl_Object = MibTableColumn
cmefg100ImcRxUnicastPktsTbl = _Cmefg100ImcRxUnicastPktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 37),
    _Cmefg100ImcRxUnicastPktsTbl_Type()
)
cmefg100ImcRxUnicastPktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcRxUnicastPktsTbl.setStatus("mandatory")
_Cmefg100ImcTxBroadcastPktsTbl_Type = Integer32
_Cmefg100ImcTxBroadcastPktsTbl_Object = MibTableColumn
cmefg100ImcTxBroadcastPktsTbl = _Cmefg100ImcTxBroadcastPktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 38),
    _Cmefg100ImcTxBroadcastPktsTbl_Type()
)
cmefg100ImcTxBroadcastPktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxBroadcastPktsTbl.setStatus("mandatory")
_Cmefg100ImcTxCollisionsTbl_Type = Integer32
_Cmefg100ImcTxCollisionsTbl_Object = MibTableColumn
cmefg100ImcTxCollisionsTbl = _Cmefg100ImcTxCollisionsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 39),
    _Cmefg100ImcTxCollisionsTbl_Type()
)
cmefg100ImcTxCollisionsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxCollisionsTbl.setStatus("mandatory")
_Cmefg100ImcTxDeferredTransmitTbl_Type = Integer32
_Cmefg100ImcTxDeferredTransmitTbl_Object = MibTableColumn
cmefg100ImcTxDeferredTransmitTbl = _Cmefg100ImcTxDeferredTransmitTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 40),
    _Cmefg100ImcTxDeferredTransmitTbl_Type()
)
cmefg100ImcTxDeferredTransmitTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxDeferredTransmitTbl.setStatus("mandatory")
_Cmefg100ImcTxDropPktsTbl_Type = Integer32
_Cmefg100ImcTxDropPktsTbl_Object = MibTableColumn
cmefg100ImcTxDropPktsTbl = _Cmefg100ImcTxDropPktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 41),
    _Cmefg100ImcTxDropPktsTbl_Type()
)
cmefg100ImcTxDropPktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxDropPktsTbl.setStatus("mandatory")
_Cmefg100ImcTxExcessiveCollisionTbl_Type = Integer32
_Cmefg100ImcTxExcessiveCollisionTbl_Object = MibTableColumn
cmefg100ImcTxExcessiveCollisionTbl = _Cmefg100ImcTxExcessiveCollisionTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 42),
    _Cmefg100ImcTxExcessiveCollisionTbl_Type()
)
cmefg100ImcTxExcessiveCollisionTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxExcessiveCollisionTbl.setStatus("mandatory")
_Cmefg100ImcTxFrameInDiscTbl_Type = Integer32
_Cmefg100ImcTxFrameInDiscTbl_Object = MibTableColumn
cmefg100ImcTxFrameInDiscTbl = _Cmefg100ImcTxFrameInDiscTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 43),
    _Cmefg100ImcTxFrameInDiscTbl_Type()
)
cmefg100ImcTxFrameInDiscTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxFrameInDiscTbl.setStatus("mandatory")
_Cmefg100ImcTxLateCollisionTbl_Type = Integer32
_Cmefg100ImcTxLateCollisionTbl_Object = MibTableColumn
cmefg100ImcTxLateCollisionTbl = _Cmefg100ImcTxLateCollisionTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 44),
    _Cmefg100ImcTxLateCollisionTbl_Type()
)
cmefg100ImcTxLateCollisionTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxLateCollisionTbl.setStatus("mandatory")
_Cmefg100ImcTxMulticastPktsTbl_Type = Integer32
_Cmefg100ImcTxMulticastPktsTbl_Object = MibTableColumn
cmefg100ImcTxMulticastPktsTbl = _Cmefg100ImcTxMulticastPktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 45),
    _Cmefg100ImcTxMulticastPktsTbl_Type()
)
cmefg100ImcTxMulticastPktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxMulticastPktsTbl.setStatus("mandatory")
_Cmefg100ImcTxMultipleCollisionTbl_Type = Integer32
_Cmefg100ImcTxMultipleCollisionTbl_Object = MibTableColumn
cmefg100ImcTxMultipleCollisionTbl = _Cmefg100ImcTxMultipleCollisionTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 46),
    _Cmefg100ImcTxMultipleCollisionTbl_Type()
)
cmefg100ImcTxMultipleCollisionTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxMultipleCollisionTbl.setStatus("mandatory")
_Cmefg100ImcTxOctetsTbl_Type = Integer32
_Cmefg100ImcTxOctetsTbl_Object = MibTableColumn
cmefg100ImcTxOctetsTbl = _Cmefg100ImcTxOctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 47),
    _Cmefg100ImcTxOctetsTbl_Type()
)
cmefg100ImcTxOctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxOctetsTbl.setStatus("mandatory")
_Cmefg100ImcTxOctetsWrapTbl_Type = Integer32
_Cmefg100ImcTxOctetsWrapTbl_Object = MibTableColumn
cmefg100ImcTxOctetsWrapTbl = _Cmefg100ImcTxOctetsWrapTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 48),
    _Cmefg100ImcTxOctetsWrapTbl_Type()
)
cmefg100ImcTxOctetsWrapTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxOctetsWrapTbl.setStatus("mandatory")
_Cmefg100ImcTxPausePktsTbl_Type = Integer32
_Cmefg100ImcTxPausePktsTbl_Object = MibTableColumn
cmefg100ImcTxPausePktsTbl = _Cmefg100ImcTxPausePktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 49),
    _Cmefg100ImcTxPausePktsTbl_Type()
)
cmefg100ImcTxPausePktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxPausePktsTbl.setStatus("mandatory")
_Cmefg100ImcTxQosOctetsTbl_Type = Integer32
_Cmefg100ImcTxQosOctetsTbl_Object = MibTableColumn
cmefg100ImcTxQosOctetsTbl = _Cmefg100ImcTxQosOctetsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 50),
    _Cmefg100ImcTxQosOctetsTbl_Type()
)
cmefg100ImcTxQosOctetsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxQosOctetsTbl.setStatus("mandatory")
_Cmefg100ImcTxQosOctetsWrapTbl_Type = Integer32
_Cmefg100ImcTxQosOctetsWrapTbl_Object = MibTableColumn
cmefg100ImcTxQosOctetsWrapTbl = _Cmefg100ImcTxQosOctetsWrapTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 51),
    _Cmefg100ImcTxQosOctetsWrapTbl_Type()
)
cmefg100ImcTxQosOctetsWrapTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxQosOctetsWrapTbl.setStatus("mandatory")
_Cmefg100ImcTxQosPktsTbl_Type = Integer32
_Cmefg100ImcTxQosPktsTbl_Object = MibTableColumn
cmefg100ImcTxQosPktsTbl = _Cmefg100ImcTxQosPktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 52),
    _Cmefg100ImcTxQosPktsTbl_Type()
)
cmefg100ImcTxQosPktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxQosPktsTbl.setStatus("mandatory")
_Cmefg100ImcTxSingleCollisionTbl_Type = Integer32
_Cmefg100ImcTxSingleCollisionTbl_Object = MibTableColumn
cmefg100ImcTxSingleCollisionTbl = _Cmefg100ImcTxSingleCollisionTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 53),
    _Cmefg100ImcTxSingleCollisionTbl_Type()
)
cmefg100ImcTxSingleCollisionTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxSingleCollisionTbl.setStatus("mandatory")
_Cmefg100ImcTxUnicastPktsTbl_Type = Integer32
_Cmefg100ImcTxUnicastPktsTbl_Object = MibTableColumn
cmefg100ImcTxUnicastPktsTbl = _Cmefg100ImcTxUnicastPktsTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 54),
    _Cmefg100ImcTxUnicastPktsTbl_Type()
)
cmefg100ImcTxUnicastPktsTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100ImcTxUnicastPktsTbl.setStatus("mandatory")


class _Cmefg100LadCacheCmd_Type(Integer32):
    """Custom type cmefg100LadCacheCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 2),
          ("loadCache", 1),
          ("release", 3))
    )


_Cmefg100LadCacheCmd_Type.__name__ = "Integer32"
_Cmefg100LadCacheCmd_Object = MibTableColumn
cmefg100LadCacheCmd = _Cmefg100LadCacheCmd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 55),
    _Cmefg100LadCacheCmd_Type()
)
cmefg100LadCacheCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LadCacheCmd.setStatus("mandatory")


class _Cmefg100LadCacheState_Type(Integer32):
    """Custom type cmefg100LadCacheState based on Integer32"""
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
        *(("bufferBusy", 4),
          ("empty", 2),
          ("ready", 1),
          ("stale", 5),
          ("transferring", 3))
    )


_Cmefg100LadCacheState_Type.__name__ = "Integer32"
_Cmefg100LadCacheState_Object = MibTableColumn
cmefg100LadCacheState = _Cmefg100LadCacheState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 56),
    _Cmefg100LadCacheState_Type()
)
cmefg100LadCacheState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LadCacheState.setStatus("mandatory")


class _Cmefg100LadEditCmd_Type(Integer32):
    """Custom type cmefg100LadEditCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("doNothing", 3),
          ("write", 1))
    )


_Cmefg100LadEditCmd_Type.__name__ = "Integer32"
_Cmefg100LadEditCmd_Object = MibTableColumn
cmefg100LadEditCmd = _Cmefg100LadEditCmd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 57),
    _Cmefg100LadEditCmd_Type()
)
cmefg100LadEditCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LadEditCmd.setStatus("mandatory")
_Cmefg100LadEditMac_Type = OctetString
_Cmefg100LadEditMac_Object = MibTableColumn
cmefg100LadEditMac = _Cmefg100LadEditMac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 58),
    _Cmefg100LadEditMac_Type()
)
cmefg100LadEditMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LadEditMac.setStatus("mandatory")


class _Cmefg100LadEditPort_Type(Integer32):
    """Custom type cmefg100LadEditPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("fiber", 2),
          ("twistedPair", 1))
    )


_Cmefg100LadEditPort_Type.__name__ = "Integer32"
_Cmefg100LadEditPort_Object = MibTableColumn
cmefg100LadEditPort = _Cmefg100LadEditPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 59),
    _Cmefg100LadEditPort_Type()
)
cmefg100LadEditPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LadEditPort.setStatus("mandatory")
_Cmefg100LadEditVid_Type = Integer32
_Cmefg100LadEditVid_Object = MibTableColumn
cmefg100LadEditVid = _Cmefg100LadEditVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 60),
    _Cmefg100LadEditVid_Type()
)
cmefg100LadEditVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LadEditVid.setStatus("mandatory")
_Cmefg100LadEntries_Type = Integer32
_Cmefg100LadEntries_Object = MibTableColumn
cmefg100LadEntries = _Cmefg100LadEntries_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 61),
    _Cmefg100LadEntries_Type()
)
cmefg100LadEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LadEntries.setStatus("mandatory")
_Cmefg100LadMacTbl_Type = MacAddress
_Cmefg100LadMacTbl_Object = MibTableColumn
cmefg100LadMacTbl = _Cmefg100LadMacTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 62),
    _Cmefg100LadMacTbl_Type()
)
cmefg100LadMacTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LadMacTbl.setStatus("mandatory")


class _Cmefg100LadPortTbl_Type(Integer32):
    """Custom type cmefg100LadPortTbl based on Integer32"""
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
        *(("drop", 3),
          ("fiber", 2),
          ("notApplicable", 4),
          ("twistedPair", 1))
    )


_Cmefg100LadPortTbl_Type.__name__ = "Integer32"
_Cmefg100LadPortTbl_Object = MibTableColumn
cmefg100LadPortTbl = _Cmefg100LadPortTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 63),
    _Cmefg100LadPortTbl_Type()
)
cmefg100LadPortTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LadPortTbl.setStatus("mandatory")


class _Cmefg100LadStaticTbl_Type(Integer32):
    """Custom type cmefg100LadStaticTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("notApplicable", 3),
          ("static", 1))
    )


_Cmefg100LadStaticTbl_Type.__name__ = "Integer32"
_Cmefg100LadStaticTbl_Object = MibTableColumn
cmefg100LadStaticTbl = _Cmefg100LadStaticTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 64),
    _Cmefg100LadStaticTbl_Type()
)
cmefg100LadStaticTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LadStaticTbl.setStatus("mandatory")
_Cmefg100LadVidTbl_Type = Integer32
_Cmefg100LadVidTbl_Object = MibTableColumn
cmefg100LadVidTbl = _Cmefg100LadVidTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 65),
    _Cmefg100LadVidTbl_Type()
)
cmefg100LadVidTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LadVidTbl.setStatus("mandatory")


class _Cmefg100LocColdstart_Type(Integer32):
    """Custom type cmefg100LocColdstart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cmefg100LocColdstart_Type.__name__ = "Integer32"
_Cmefg100LocColdstart_Object = MibTableColumn
cmefg100LocColdstart = _Cmefg100LocColdstart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 66),
    _Cmefg100LocColdstart_Type()
)
cmefg100LocColdstart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocColdstart.setStatus("mandatory")
_Cmefg100LocDmiRxPower_Type = Integer32
_Cmefg100LocDmiRxPower_Object = MibTableColumn
cmefg100LocDmiRxPower = _Cmefg100LocDmiRxPower_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 67),
    _Cmefg100LocDmiRxPower_Type()
)
cmefg100LocDmiRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocDmiRxPower.setStatus("mandatory")


class _Cmefg100LocDmiRxPowerAlarm_Type(Integer32):
    """Custom type cmefg100LocDmiRxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 6),
          ("highWarn", 4),
          ("lowAlarm", 5),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Cmefg100LocDmiRxPowerAlarm_Type.__name__ = "Integer32"
_Cmefg100LocDmiRxPowerAlarm_Object = MibTableColumn
cmefg100LocDmiRxPowerAlarm = _Cmefg100LocDmiRxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 68),
    _Cmefg100LocDmiRxPowerAlarm_Type()
)
cmefg100LocDmiRxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocDmiRxPowerAlarm.setStatus("mandatory")
_Cmefg100LocDmiTemp_Type = Integer32
_Cmefg100LocDmiTemp_Object = MibTableColumn
cmefg100LocDmiTemp = _Cmefg100LocDmiTemp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 69),
    _Cmefg100LocDmiTemp_Type()
)
cmefg100LocDmiTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocDmiTemp.setStatus("mandatory")


class _Cmefg100LocDmiTempAlarm_Type(Integer32):
    """Custom type cmefg100LocDmiTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 6),
          ("highWarn", 4),
          ("lowAlarm", 5),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Cmefg100LocDmiTempAlarm_Type.__name__ = "Integer32"
_Cmefg100LocDmiTempAlarm_Object = MibTableColumn
cmefg100LocDmiTempAlarm = _Cmefg100LocDmiTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 70),
    _Cmefg100LocDmiTempAlarm_Type()
)
cmefg100LocDmiTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocDmiTempAlarm.setStatus("mandatory")


class _Cmefg100LocDmiTxBiasAlarm_Type(Integer32):
    """Custom type cmefg100LocDmiTxBiasAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 6),
          ("highWarn", 4),
          ("lowAlarm", 5),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Cmefg100LocDmiTxBiasAlarm_Type.__name__ = "Integer32"
_Cmefg100LocDmiTxBiasAlarm_Object = MibTableColumn
cmefg100LocDmiTxBiasAlarm = _Cmefg100LocDmiTxBiasAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 71),
    _Cmefg100LocDmiTxBiasAlarm_Type()
)
cmefg100LocDmiTxBiasAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocDmiTxBiasAlarm.setStatus("mandatory")
_Cmefg100LocDmiTxBiasCurrent_Type = Integer32
_Cmefg100LocDmiTxBiasCurrent_Object = MibTableColumn
cmefg100LocDmiTxBiasCurrent = _Cmefg100LocDmiTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 72),
    _Cmefg100LocDmiTxBiasCurrent_Type()
)
cmefg100LocDmiTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocDmiTxBiasCurrent.setStatus("mandatory")
_Cmefg100LocDmiTxPower_Type = Integer32
_Cmefg100LocDmiTxPower_Object = MibTableColumn
cmefg100LocDmiTxPower = _Cmefg100LocDmiTxPower_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 73),
    _Cmefg100LocDmiTxPower_Type()
)
cmefg100LocDmiTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocDmiTxPower.setStatus("mandatory")


class _Cmefg100LocDmiTxPowerAlarm_Type(Integer32):
    """Custom type cmefg100LocDmiTxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 6),
          ("highWarn", 4),
          ("lowAlarm", 5),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Cmefg100LocDmiTxPowerAlarm_Type.__name__ = "Integer32"
_Cmefg100LocDmiTxPowerAlarm_Object = MibTableColumn
cmefg100LocDmiTxPowerAlarm = _Cmefg100LocDmiTxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 74),
    _Cmefg100LocDmiTxPowerAlarm_Type()
)
cmefg100LocDmiTxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocDmiTxPowerAlarm.setStatus("mandatory")


class _Cmefg100LocFiberAdv1000FDX_Type(Integer32):
    """Custom type cmefg100LocFiberAdv1000FDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100LocFiberAdv1000FDX_Type.__name__ = "Integer32"
_Cmefg100LocFiberAdv1000FDX_Object = MibTableColumn
cmefg100LocFiberAdv1000FDX = _Cmefg100LocFiberAdv1000FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 75),
    _Cmefg100LocFiberAdv1000FDX_Type()
)
cmefg100LocFiberAdv1000FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocFiberAdv1000FDX.setStatus("mandatory")


class _Cmefg100LocFiberAdv1000HDX_Type(Integer32):
    """Custom type cmefg100LocFiberAdv1000HDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100LocFiberAdv1000HDX_Type.__name__ = "Integer32"
_Cmefg100LocFiberAdv1000HDX_Object = MibTableColumn
cmefg100LocFiberAdv1000HDX = _Cmefg100LocFiberAdv1000HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 76),
    _Cmefg100LocFiberAdv1000HDX_Type()
)
cmefg100LocFiberAdv1000HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocFiberAdv1000HDX.setStatus("mandatory")


class _Cmefg100LocFiberAutoNegot_Type(Integer32):
    """Custom type cmefg100LocFiberAutoNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100LocFiberAutoNegot_Type.__name__ = "Integer32"
_Cmefg100LocFiberAutoNegot_Object = MibTableColumn
cmefg100LocFiberAutoNegot = _Cmefg100LocFiberAutoNegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 77),
    _Cmefg100LocFiberAutoNegot_Type()
)
cmefg100LocFiberAutoNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocFiberAutoNegot.setStatus("mandatory")
_Cmefg100LocFiberConnA_Type = CpsConnector
_Cmefg100LocFiberConnA_Object = MibTableColumn
cmefg100LocFiberConnA = _Cmefg100LocFiberConnA_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 78),
    _Cmefg100LocFiberConnA_Type()
)
cmefg100LocFiberConnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocFiberConnA.setStatus("mandatory")


class _Cmefg100LocFiberDuplex_Type(Integer32):
    """Custom type cmefg100LocFiberDuplex based on Integer32"""
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
        *(("autoFDX", 3),
          ("autoHDX", 4),
          ("forceFDX", 1),
          ("forceHDX", 2),
          ("negotiating", 5))
    )


_Cmefg100LocFiberDuplex_Type.__name__ = "Integer32"
_Cmefg100LocFiberDuplex_Object = MibTableColumn
cmefg100LocFiberDuplex = _Cmefg100LocFiberDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 79),
    _Cmefg100LocFiberDuplex_Type()
)
cmefg100LocFiberDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocFiberDuplex.setStatus("mandatory")


class _Cmefg100LocFiberLink_Type(Integer32):
    """Custom type cmefg100LocFiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cmefg100LocFiberLink_Type.__name__ = "Integer32"
_Cmefg100LocFiberLink_Object = MibTableColumn
cmefg100LocFiberLink = _Cmefg100LocFiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 80),
    _Cmefg100LocFiberLink_Type()
)
cmefg100LocFiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocFiberLink.setStatus("mandatory")


class _Cmefg100LocFiberPause_Type(Integer32):
    """Custom type cmefg100LocFiberPause based on Integer32"""
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
        *(("asymmetricRx", 1),
          ("asymmetricTx", 2),
          ("disabled", 4),
          ("symmetric", 3))
    )


_Cmefg100LocFiberPause_Type.__name__ = "Integer32"
_Cmefg100LocFiberPause_Object = MibTableColumn
cmefg100LocFiberPause = _Cmefg100LocFiberPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 81),
    _Cmefg100LocFiberPause_Type()
)
cmefg100LocFiberPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocFiberPause.setStatus("mandatory")


class _Cmefg100LocFiberQosPause_Type(Integer32):
    """Custom type cmefg100LocFiberQosPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100LocFiberQosPause_Type.__name__ = "Integer32"
_Cmefg100LocFiberQosPause_Object = MibTableColumn
cmefg100LocFiberQosPause = _Cmefg100LocFiberQosPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 82),
    _Cmefg100LocFiberQosPause_Type()
)
cmefg100LocFiberQosPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocFiberQosPause.setStatus("mandatory")


class _Cmefg100LocFiberSacEnable_Type(Integer32):
    """Custom type cmefg100LocFiberSacEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100LocFiberSacEnable_Type.__name__ = "Integer32"
_Cmefg100LocFiberSacEnable_Object = MibTableColumn
cmefg100LocFiberSacEnable = _Cmefg100LocFiberSacEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 83),
    _Cmefg100LocFiberSacEnable_Type()
)
cmefg100LocFiberSacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocFiberSacEnable.setStatus("mandatory")


class _Cmefg100LocFiberSacStatus_Type(Integer32):
    """Custom type cmefg100LocFiberSacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changed", 1),
          ("constant", 2))
    )


_Cmefg100LocFiberSacStatus_Type.__name__ = "Integer32"
_Cmefg100LocFiberSacStatus_Object = MibTableColumn
cmefg100LocFiberSacStatus = _Cmefg100LocFiberSacStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 84),
    _Cmefg100LocFiberSacStatus_Type()
)
cmefg100LocFiberSacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocFiberSacStatus.setStatus("mandatory")
_Cmefg100LocFirmwareRevision_Type = Integer32
_Cmefg100LocFirmwareRevision_Object = MibTableColumn
cmefg100LocFirmwareRevision = _Cmefg100LocFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 85),
    _Cmefg100LocFirmwareRevision_Type()
)
cmefg100LocFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocFirmwareRevision.setStatus("mandatory")
_Cmefg100LocFpgaRev_Type = Integer32
_Cmefg100LocFpgaRev_Object = MibTableColumn
cmefg100LocFpgaRev = _Cmefg100LocFpgaRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 86),
    _Cmefg100LocFpgaRev_Type()
)
cmefg100LocFpgaRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocFpgaRev.setStatus("mandatory")


class _Cmefg100LocFxTxBwaKb_Type(Integer32):
    """Custom type cmefg100LocFxTxBwaKb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 122112),
    )


_Cmefg100LocFxTxBwaKb_Type.__name__ = "Integer32"
_Cmefg100LocFxTxBwaKb_Object = MibTableColumn
cmefg100LocFxTxBwaKb = _Cmefg100LocFxTxBwaKb_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 87),
    _Cmefg100LocFxTxBwaKb_Type()
)
cmefg100LocFxTxBwaKb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocFxTxBwaKb.setStatus("mandatory")


class _Cmefg100LocFxTxBwaMb_Type(Integer32):
    """Custom type cmefg100LocFxTxBwaMb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Cmefg100LocFxTxBwaMb_Type.__name__ = "Integer32"
_Cmefg100LocFxTxBwaMb_Object = MibTableColumn
cmefg100LocFxTxBwaMb = _Cmefg100LocFxTxBwaMb_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 88),
    _Cmefg100LocFxTxBwaMb_Type()
)
cmefg100LocFxTxBwaMb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocFxTxBwaMb.setStatus("mandatory")


class _Cmefg100LocOamActiveMode_Type(Integer32):
    """Custom type cmefg100LocOamActiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_Cmefg100LocOamActiveMode_Type.__name__ = "Integer32"
_Cmefg100LocOamActiveMode_Object = MibTableColumn
cmefg100LocOamActiveMode = _Cmefg100LocOamActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 89),
    _Cmefg100LocOamActiveMode_Type()
)
cmefg100LocOamActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamActiveMode.setStatus("mandatory")


class _Cmefg100LocOamAdminControl_Type(Integer32):
    """Custom type cmefg100LocOamAdminControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100LocOamAdminControl_Type.__name__ = "Integer32"
_Cmefg100LocOamAdminControl_Object = MibTableColumn
cmefg100LocOamAdminControl = _Cmefg100LocOamAdminControl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 90),
    _Cmefg100LocOamAdminControl_Type()
)
cmefg100LocOamAdminControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocOamAdminControl.setStatus("mandatory")
_Cmefg100LocOamConfigRevision_Type = Integer32
_Cmefg100LocOamConfigRevision_Object = MibTableColumn
cmefg100LocOamConfigRevision = _Cmefg100LocOamConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 91),
    _Cmefg100LocOamConfigRevision_Type()
)
cmefg100LocOamConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamConfigRevision.setStatus("mandatory")
_Cmefg100LocOamControlInUnknownOpcodes_Type = Integer32
_Cmefg100LocOamControlInUnknownOpcodes_Object = MibTableColumn
cmefg100LocOamControlInUnknownOpcodes = _Cmefg100LocOamControlInUnknownOpcodes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 92),
    _Cmefg100LocOamControlInUnknownOpcodes_Type()
)
cmefg100LocOamControlInUnknownOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamControlInUnknownOpcodes.setStatus("mandatory")


class _Cmefg100LocOamCriticalEvent_Type(Integer32):
    """Custom type cmefg100LocOamCriticalEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("normal", 2))
    )


_Cmefg100LocOamCriticalEvent_Type.__name__ = "Integer32"
_Cmefg100LocOamCriticalEvent_Object = MibTableColumn
cmefg100LocOamCriticalEvent = _Cmefg100LocOamCriticalEvent_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 93),
    _Cmefg100LocOamCriticalEvent_Type()
)
cmefg100LocOamCriticalEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamCriticalEvent.setStatus("mandatory")
_Cmefg100LocOamDuplicateEventNotificationRx_Type = Integer32
_Cmefg100LocOamDuplicateEventNotificationRx_Object = MibTableColumn
cmefg100LocOamDuplicateEventNotificationRx = _Cmefg100LocOamDuplicateEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 94),
    _Cmefg100LocOamDuplicateEventNotificationRx_Type()
)
cmefg100LocOamDuplicateEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamDuplicateEventNotificationRx.setStatus("mandatory")
_Cmefg100LocOamFramesLostDueToOamError_Type = Integer32
_Cmefg100LocOamFramesLostDueToOamError_Object = MibTableColumn
cmefg100LocOamFramesLostDueToOamError = _Cmefg100LocOamFramesLostDueToOamError_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 95),
    _Cmefg100LocOamFramesLostDueToOamError_Type()
)
cmefg100LocOamFramesLostDueToOamError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamFramesLostDueToOamError.setStatus("mandatory")
_Cmefg100LocOamInformationRx_Type = Integer32
_Cmefg100LocOamInformationRx_Object = MibTableColumn
cmefg100LocOamInformationRx = _Cmefg100LocOamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 96),
    _Cmefg100LocOamInformationRx_Type()
)
cmefg100LocOamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamInformationRx.setStatus("mandatory")
_Cmefg100LocOamInformationTx_Type = Integer32
_Cmefg100LocOamInformationTx_Object = MibTableColumn
cmefg100LocOamInformationTx = _Cmefg100LocOamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 97),
    _Cmefg100LocOamInformationTx_Type()
)
cmefg100LocOamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamInformationTx.setStatus("mandatory")


class _Cmefg100LocOamLastGasp_Type(Integer32):
    """Custom type cmefg100LocOamLastGasp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("normal", 2))
    )


_Cmefg100LocOamLastGasp_Type.__name__ = "Integer32"
_Cmefg100LocOamLastGasp_Object = MibTableColumn
cmefg100LocOamLastGasp = _Cmefg100LocOamLastGasp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 98),
    _Cmefg100LocOamLastGasp_Type()
)
cmefg100LocOamLastGasp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamLastGasp.setStatus("mandatory")


class _Cmefg100LocOamLinkEvents_Type(Integer32):
    """Custom type cmefg100LocOamLinkEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_Cmefg100LocOamLinkEvents_Type.__name__ = "Integer32"
_Cmefg100LocOamLinkEvents_Object = MibTableColumn
cmefg100LocOamLinkEvents = _Cmefg100LocOamLinkEvents_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 99),
    _Cmefg100LocOamLinkEvents_Type()
)
cmefg100LocOamLinkEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamLinkEvents.setStatus("mandatory")


class _Cmefg100LocOamLinkFault_Type(Integer32):
    """Custom type cmefg100LocOamLinkFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("normal", 2))
    )


_Cmefg100LocOamLinkFault_Type.__name__ = "Integer32"
_Cmefg100LocOamLinkFault_Object = MibTableColumn
cmefg100LocOamLinkFault = _Cmefg100LocOamLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 100),
    _Cmefg100LocOamLinkFault_Type()
)
cmefg100LocOamLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamLinkFault.setStatus("mandatory")


class _Cmefg100LocOamLocDteDisc_Type(Integer32):
    """Custom type cmefg100LocOamLocDteDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("notCompleted", 2),
          ("unsatisfied", 3))
    )


_Cmefg100LocOamLocDteDisc_Type.__name__ = "Integer32"
_Cmefg100LocOamLocDteDisc_Object = MibTableColumn
cmefg100LocOamLocDteDisc = _Cmefg100LocOamLocDteDisc_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 101),
    _Cmefg100LocOamLocDteDisc_Type()
)
cmefg100LocOamLocDteDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamLocDteDisc.setStatus("mandatory")
_Cmefg100LocOamLoopbackControlRx_Type = Integer32
_Cmefg100LocOamLoopbackControlRx_Object = MibTableColumn
cmefg100LocOamLoopbackControlRx = _Cmefg100LocOamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 102),
    _Cmefg100LocOamLoopbackControlRx_Type()
)
cmefg100LocOamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamLoopbackControlRx.setStatus("mandatory")
_Cmefg100LocOamLoopbackControlTx_Type = Integer32
_Cmefg100LocOamLoopbackControlTx_Object = MibTableColumn
cmefg100LocOamLoopbackControlTx = _Cmefg100LocOamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 103),
    _Cmefg100LocOamLoopbackControlTx_Type()
)
cmefg100LocOamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamLoopbackControlTx.setStatus("mandatory")
_Cmefg100LocOamMacAddress_Type = MacAddress
_Cmefg100LocOamMacAddress_Object = MibTableColumn
cmefg100LocOamMacAddress = _Cmefg100LocOamMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 104),
    _Cmefg100LocOamMacAddress_Type()
)
cmefg100LocOamMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamMacAddress.setStatus("mandatory")
_Cmefg100LocOamMaxOamPduSize_Type = Integer32
_Cmefg100LocOamMaxOamPduSize_Object = MibTableColumn
cmefg100LocOamMaxOamPduSize = _Cmefg100LocOamMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 105),
    _Cmefg100LocOamMaxOamPduSize_Type()
)
cmefg100LocOamMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamMaxOamPduSize.setStatus("mandatory")


class _Cmefg100LocOamMultiplexorState_Type(Integer32):
    """Custom type cmefg100LocOamMultiplexorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 2),
          ("forwarding", 1))
    )


_Cmefg100LocOamMultiplexorState_Type.__name__ = "Integer32"
_Cmefg100LocOamMultiplexorState_Object = MibTableColumn
cmefg100LocOamMultiplexorState = _Cmefg100LocOamMultiplexorState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 106),
    _Cmefg100LocOamMultiplexorState_Type()
)
cmefg100LocOamMultiplexorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamMultiplexorState.setStatus("mandatory")


class _Cmefg100LocOamOperStatus_Type(Integer32):
    """Custom type cmefg100LocOamOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("activeSendLocal", 2),
          ("linkFault", 1),
          ("passiveWait", 3),
          ("sendAny", 6),
          ("sendLocalRemote", 4),
          ("sendLocalRemoteOk", 5))
    )


_Cmefg100LocOamOperStatus_Type.__name__ = "Integer32"
_Cmefg100LocOamOperStatus_Object = MibTableColumn
cmefg100LocOamOperStatus = _Cmefg100LocOamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 107),
    _Cmefg100LocOamOperStatus_Type()
)
cmefg100LocOamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamOperStatus.setStatus("mandatory")
_Cmefg100LocOamOrgSpecificRx_Type = Integer32
_Cmefg100LocOamOrgSpecificRx_Object = MibTableColumn
cmefg100LocOamOrgSpecificRx = _Cmefg100LocOamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 108),
    _Cmefg100LocOamOrgSpecificRx_Type()
)
cmefg100LocOamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamOrgSpecificRx.setStatus("mandatory")
_Cmefg100LocOamOrgSpecificTx_Type = Integer32
_Cmefg100LocOamOrgSpecificTx_Object = MibTableColumn
cmefg100LocOamOrgSpecificTx = _Cmefg100LocOamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 109),
    _Cmefg100LocOamOrgSpecificTx_Type()
)
cmefg100LocOamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamOrgSpecificTx.setStatus("mandatory")


class _Cmefg100LocOamParserState_Type(Integer32):
    """Custom type cmefg100LocOamParserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 2),
          ("forwarding", 1),
          ("looping", 3))
    )


_Cmefg100LocOamParserState_Type.__name__ = "Integer32"
_Cmefg100LocOamParserState_Object = MibTableColumn
cmefg100LocOamParserState = _Cmefg100LocOamParserState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 110),
    _Cmefg100LocOamParserState_Type()
)
cmefg100LocOamParserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamParserState.setStatus("mandatory")


class _Cmefg100LocOamRmtDteDisc_Type(Integer32):
    """Custom type cmefg100LocOamRmtDteDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("notCompleted", 2),
          ("unsatisfied", 3))
    )


_Cmefg100LocOamRmtDteDisc_Type.__name__ = "Integer32"
_Cmefg100LocOamRmtDteDisc_Object = MibTableColumn
cmefg100LocOamRmtDteDisc = _Cmefg100LocOamRmtDteDisc_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 111),
    _Cmefg100LocOamRmtDteDisc_Type()
)
cmefg100LocOamRmtDteDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamRmtDteDisc.setStatus("mandatory")


class _Cmefg100LocOamRmtLoopback_Type(Integer32):
    """Custom type cmefg100LocOamRmtLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_Cmefg100LocOamRmtLoopback_Type.__name__ = "Integer32"
_Cmefg100LocOamRmtLoopback_Object = MibTableColumn
cmefg100LocOamRmtLoopback = _Cmefg100LocOamRmtLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 112),
    _Cmefg100LocOamRmtLoopback_Type()
)
cmefg100LocOamRmtLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamRmtLoopback.setStatus("mandatory")


class _Cmefg100LocOamUnidirectional_Type(Integer32):
    """Custom type cmefg100LocOamUnidirectional based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_Cmefg100LocOamUnidirectional_Type.__name__ = "Integer32"
_Cmefg100LocOamUnidirectional_Object = MibTableColumn
cmefg100LocOamUnidirectional = _Cmefg100LocOamUnidirectional_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 113),
    _Cmefg100LocOamUnidirectional_Type()
)
cmefg100LocOamUnidirectional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamUnidirectional.setStatus("mandatory")


class _Cmefg100LocOamVarRetrieval_Type(Integer32):
    """Custom type cmefg100LocOamVarRetrieval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_Cmefg100LocOamVarRetrieval_Type.__name__ = "Integer32"
_Cmefg100LocOamVarRetrieval_Object = MibTableColumn
cmefg100LocOamVarRetrieval = _Cmefg100LocOamVarRetrieval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 114),
    _Cmefg100LocOamVarRetrieval_Type()
)
cmefg100LocOamVarRetrieval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocOamVarRetrieval.setStatus("mandatory")


class _Cmefg100LocSelfTestFailed_Type(Integer32):
    """Custom type cmefg100LocSelfTestFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cmefg100LocSelfTestFailed_Type.__name__ = "Integer32"
_Cmefg100LocSelfTestFailed_Object = MibTableColumn
cmefg100LocSelfTestFailed = _Cmefg100LocSelfTestFailed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 115),
    _Cmefg100LocSelfTestFailed_Type()
)
cmefg100LocSelfTestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocSelfTestFailed.setStatus("mandatory")
_Cmefg100LocSerialNumber_Type = Integer32
_Cmefg100LocSerialNumber_Object = MibTableColumn
cmefg100LocSerialNumber = _Cmefg100LocSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 116),
    _Cmefg100LocSerialNumber_Type()
)
cmefg100LocSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocSerialNumber.setStatus("mandatory")


class _Cmefg100LocTpAdv1000FDX_Type(Integer32):
    """Custom type cmefg100LocTpAdv1000FDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100LocTpAdv1000FDX_Type.__name__ = "Integer32"
_Cmefg100LocTpAdv1000FDX_Object = MibTableColumn
cmefg100LocTpAdv1000FDX = _Cmefg100LocTpAdv1000FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 117),
    _Cmefg100LocTpAdv1000FDX_Type()
)
cmefg100LocTpAdv1000FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpAdv1000FDX.setStatus("mandatory")


class _Cmefg100LocTpAdv1000HDX_Type(Integer32):
    """Custom type cmefg100LocTpAdv1000HDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100LocTpAdv1000HDX_Type.__name__ = "Integer32"
_Cmefg100LocTpAdv1000HDX_Object = MibTableColumn
cmefg100LocTpAdv1000HDX = _Cmefg100LocTpAdv1000HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 118),
    _Cmefg100LocTpAdv1000HDX_Type()
)
cmefg100LocTpAdv1000HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpAdv1000HDX.setStatus("mandatory")


class _Cmefg100LocTpAdv100FDX_Type(Integer32):
    """Custom type cmefg100LocTpAdv100FDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100LocTpAdv100FDX_Type.__name__ = "Integer32"
_Cmefg100LocTpAdv100FDX_Object = MibTableColumn
cmefg100LocTpAdv100FDX = _Cmefg100LocTpAdv100FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 119),
    _Cmefg100LocTpAdv100FDX_Type()
)
cmefg100LocTpAdv100FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpAdv100FDX.setStatus("mandatory")


class _Cmefg100LocTpAdv100HDX_Type(Integer32):
    """Custom type cmefg100LocTpAdv100HDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100LocTpAdv100HDX_Type.__name__ = "Integer32"
_Cmefg100LocTpAdv100HDX_Object = MibTableColumn
cmefg100LocTpAdv100HDX = _Cmefg100LocTpAdv100HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 120),
    _Cmefg100LocTpAdv100HDX_Type()
)
cmefg100LocTpAdv100HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpAdv100HDX.setStatus("mandatory")


class _Cmefg100LocTpAdv10FDX_Type(Integer32):
    """Custom type cmefg100LocTpAdv10FDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100LocTpAdv10FDX_Type.__name__ = "Integer32"
_Cmefg100LocTpAdv10FDX_Object = MibTableColumn
cmefg100LocTpAdv10FDX = _Cmefg100LocTpAdv10FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 121),
    _Cmefg100LocTpAdv10FDX_Type()
)
cmefg100LocTpAdv10FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpAdv10FDX.setStatus("mandatory")


class _Cmefg100LocTpAdv10HDX_Type(Integer32):
    """Custom type cmefg100LocTpAdv10HDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100LocTpAdv10HDX_Type.__name__ = "Integer32"
_Cmefg100LocTpAdv10HDX_Object = MibTableColumn
cmefg100LocTpAdv10HDX = _Cmefg100LocTpAdv10HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 122),
    _Cmefg100LocTpAdv10HDX_Type()
)
cmefg100LocTpAdv10HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpAdv10HDX.setStatus("mandatory")


class _Cmefg100LocTpAutoNegot_Type(Integer32):
    """Custom type cmefg100LocTpAutoNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100LocTpAutoNegot_Type.__name__ = "Integer32"
_Cmefg100LocTpAutoNegot_Object = MibTableColumn
cmefg100LocTpAutoNegot = _Cmefg100LocTpAutoNegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 123),
    _Cmefg100LocTpAutoNegot_Type()
)
cmefg100LocTpAutoNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpAutoNegot.setStatus("mandatory")
_Cmefg100LocTpConnB_Type = CpsConnector
_Cmefg100LocTpConnB_Object = MibTableColumn
cmefg100LocTpConnB = _Cmefg100LocTpConnB_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 124),
    _Cmefg100LocTpConnB_Type()
)
cmefg100LocTpConnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocTpConnB.setStatus("mandatory")


class _Cmefg100LocTpCross_Type(Integer32):
    """Custom type cmefg100LocTpCross based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("forceMDI", 1),
          ("forceMDI-X", 2))
    )


_Cmefg100LocTpCross_Type.__name__ = "Integer32"
_Cmefg100LocTpCross_Object = MibTableColumn
cmefg100LocTpCross = _Cmefg100LocTpCross_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 125),
    _Cmefg100LocTpCross_Type()
)
cmefg100LocTpCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpCross.setStatus("mandatory")


class _Cmefg100LocTpDuplex_Type(Integer32):
    """Custom type cmefg100LocTpDuplex based on Integer32"""
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
        *(("autoFDX", 3),
          ("autoHDX", 4),
          ("forceFDX", 1),
          ("forceHDX", 2),
          ("negotiating", 5))
    )


_Cmefg100LocTpDuplex_Type.__name__ = "Integer32"
_Cmefg100LocTpDuplex_Object = MibTableColumn
cmefg100LocTpDuplex = _Cmefg100LocTpDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 126),
    _Cmefg100LocTpDuplex_Type()
)
cmefg100LocTpDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpDuplex.setStatus("mandatory")


class _Cmefg100LocTpLink_Type(Integer32):
    """Custom type cmefg100LocTpLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cmefg100LocTpLink_Type.__name__ = "Integer32"
_Cmefg100LocTpLink_Object = MibTableColumn
cmefg100LocTpLink = _Cmefg100LocTpLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 127),
    _Cmefg100LocTpLink_Type()
)
cmefg100LocTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocTpLink.setStatus("mandatory")


class _Cmefg100LocTpPause_Type(Integer32):
    """Custom type cmefg100LocTpPause based on Integer32"""
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
        *(("asymmetricRx", 1),
          ("asymmetricTx", 2),
          ("disabled", 4),
          ("symmetric", 3))
    )


_Cmefg100LocTpPause_Type.__name__ = "Integer32"
_Cmefg100LocTpPause_Object = MibTableColumn
cmefg100LocTpPause = _Cmefg100LocTpPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 128),
    _Cmefg100LocTpPause_Type()
)
cmefg100LocTpPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpPause.setStatus("mandatory")


class _Cmefg100LocTpQosPause_Type(Integer32):
    """Custom type cmefg100LocTpQosPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100LocTpQosPause_Type.__name__ = "Integer32"
_Cmefg100LocTpQosPause_Object = MibTableColumn
cmefg100LocTpQosPause = _Cmefg100LocTpQosPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 129),
    _Cmefg100LocTpQosPause_Type()
)
cmefg100LocTpQosPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpQosPause.setStatus("mandatory")


class _Cmefg100LocTpSacEnable_Type(Integer32):
    """Custom type cmefg100LocTpSacEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100LocTpSacEnable_Type.__name__ = "Integer32"
_Cmefg100LocTpSacEnable_Object = MibTableColumn
cmefg100LocTpSacEnable = _Cmefg100LocTpSacEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 130),
    _Cmefg100LocTpSacEnable_Type()
)
cmefg100LocTpSacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpSacEnable.setStatus("mandatory")


class _Cmefg100LocTpSacStatus_Type(Integer32):
    """Custom type cmefg100LocTpSacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changed", 1),
          ("constant", 2))
    )


_Cmefg100LocTpSacStatus_Type.__name__ = "Integer32"
_Cmefg100LocTpSacStatus_Object = MibTableColumn
cmefg100LocTpSacStatus = _Cmefg100LocTpSacStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 131),
    _Cmefg100LocTpSacStatus_Type()
)
cmefg100LocTpSacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100LocTpSacStatus.setStatus("mandatory")


class _Cmefg100LocTpSpeed_Type(Integer32):
    """Custom type cmefg100LocTpSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto1000Mbps", 5),
          ("auto100Mbps", 4),
          ("auto10Mbps", 3),
          ("force100Mbps", 2),
          ("force10Mbps", 1),
          ("negotiating", 6))
    )


_Cmefg100LocTpSpeed_Type.__name__ = "Integer32"
_Cmefg100LocTpSpeed_Object = MibTableColumn
cmefg100LocTpSpeed = _Cmefg100LocTpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 132),
    _Cmefg100LocTpSpeed_Type()
)
cmefg100LocTpSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTpSpeed.setStatus("mandatory")


class _Cmefg100LocTxFxBwaKb_Type(Integer32):
    """Custom type cmefg100LocTxFxBwaKb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 122112),
    )


_Cmefg100LocTxFxBwaKb_Type.__name__ = "Integer32"
_Cmefg100LocTxFxBwaKb_Object = MibTableColumn
cmefg100LocTxFxBwaKb = _Cmefg100LocTxFxBwaKb_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 133),
    _Cmefg100LocTxFxBwaKb_Type()
)
cmefg100LocTxFxBwaKb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTxFxBwaKb.setStatus("mandatory")


class _Cmefg100LocTxFxBwaMb_Type(Integer32):
    """Custom type cmefg100LocTxFxBwaMb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Cmefg100LocTxFxBwaMb_Type.__name__ = "Integer32"
_Cmefg100LocTxFxBwaMb_Object = MibTableColumn
cmefg100LocTxFxBwaMb = _Cmefg100LocTxFxBwaMb_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 134),
    _Cmefg100LocTxFxBwaMb_Type()
)
cmefg100LocTxFxBwaMb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocTxFxBwaMb.setStatus("mandatory")
_Cmefg100LocUptime_Type = TimeTicks
_Cmefg100LocUptime_Object = MibTableColumn
cmefg100LocUptime = _Cmefg100LocUptime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 135),
    _Cmefg100LocUptime_Type()
)
cmefg100LocUptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100LocUptime.setStatus("mandatory")


class _Cmefg100QosHqWeight_Type(Integer32):
    """Custom type cmefg100QosHqWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cmefg100QosHqWeight_Type.__name__ = "Integer32"
_Cmefg100QosHqWeight_Object = MibTableColumn
cmefg100QosHqWeight = _Cmefg100QosHqWeight_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 136),
    _Cmefg100QosHqWeight_Type()
)
cmefg100QosHqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100QosHqWeight.setStatus("mandatory")


class _Cmefg100QosLqWeight_Type(Integer32):
    """Custom type cmefg100QosLqWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cmefg100QosLqWeight_Type.__name__ = "Integer32"
_Cmefg100QosLqWeight_Object = MibTableColumn
cmefg100QosLqWeight = _Cmefg100QosLqWeight_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 137),
    _Cmefg100QosLqWeight_Type()
)
cmefg100QosLqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100QosLqWeight.setStatus("mandatory")


class _Cmefg100QosPriority_Type(Integer32):
    """Custom type cmefg100QosPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cmefg100QosPriority_Type.__name__ = "Integer32"
_Cmefg100QosPriority_Object = MibTableColumn
cmefg100QosPriority = _Cmefg100QosPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 138),
    _Cmefg100QosPriority_Type()
)
cmefg100QosPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100QosPriority.setStatus("mandatory")


class _Cmefg100RmtColdStart_Type(Integer32):
    """Custom type cmefg100RmtColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cmefg100RmtColdStart_Type.__name__ = "Integer32"
_Cmefg100RmtColdStart_Object = MibTableColumn
cmefg100RmtColdStart = _Cmefg100RmtColdStart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 139),
    _Cmefg100RmtColdStart_Type()
)
cmefg100RmtColdStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtColdStart.setStatus("mandatory")


class _Cmefg100RmtDetected_Type(Integer32):
    """Custom type cmefg100RmtDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cmefg100RmtDetected_Type.__name__ = "Integer32"
_Cmefg100RmtDetected_Object = MibTableColumn
cmefg100RmtDetected = _Cmefg100RmtDetected_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 140),
    _Cmefg100RmtDetected_Type()
)
cmefg100RmtDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtDetected.setStatus("mandatory")
_Cmefg100RmtDmiRxPower_Type = Integer32
_Cmefg100RmtDmiRxPower_Object = MibTableColumn
cmefg100RmtDmiRxPower = _Cmefg100RmtDmiRxPower_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 141),
    _Cmefg100RmtDmiRxPower_Type()
)
cmefg100RmtDmiRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtDmiRxPower.setStatus("mandatory")


class _Cmefg100RmtDmiRxPowerAlarm_Type(Integer32):
    """Custom type cmefg100RmtDmiRxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 6),
          ("highWarn", 4),
          ("lowAlarm", 5),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Cmefg100RmtDmiRxPowerAlarm_Type.__name__ = "Integer32"
_Cmefg100RmtDmiRxPowerAlarm_Object = MibTableColumn
cmefg100RmtDmiRxPowerAlarm = _Cmefg100RmtDmiRxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 142),
    _Cmefg100RmtDmiRxPowerAlarm_Type()
)
cmefg100RmtDmiRxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtDmiRxPowerAlarm.setStatus("mandatory")
_Cmefg100RmtDmiTemp_Type = Integer32
_Cmefg100RmtDmiTemp_Object = MibTableColumn
cmefg100RmtDmiTemp = _Cmefg100RmtDmiTemp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 143),
    _Cmefg100RmtDmiTemp_Type()
)
cmefg100RmtDmiTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtDmiTemp.setStatus("mandatory")


class _Cmefg100RmtDmiTempAlarm_Type(Integer32):
    """Custom type cmefg100RmtDmiTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 6),
          ("highWarn", 4),
          ("lowAlarm", 5),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Cmefg100RmtDmiTempAlarm_Type.__name__ = "Integer32"
_Cmefg100RmtDmiTempAlarm_Object = MibTableColumn
cmefg100RmtDmiTempAlarm = _Cmefg100RmtDmiTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 144),
    _Cmefg100RmtDmiTempAlarm_Type()
)
cmefg100RmtDmiTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtDmiTempAlarm.setStatus("mandatory")


class _Cmefg100RmtDmiTxBiasAlarm_Type(Integer32):
    """Custom type cmefg100RmtDmiTxBiasAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 6),
          ("highWarn", 4),
          ("lowAlarm", 5),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Cmefg100RmtDmiTxBiasAlarm_Type.__name__ = "Integer32"
_Cmefg100RmtDmiTxBiasAlarm_Object = MibTableColumn
cmefg100RmtDmiTxBiasAlarm = _Cmefg100RmtDmiTxBiasAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 145),
    _Cmefg100RmtDmiTxBiasAlarm_Type()
)
cmefg100RmtDmiTxBiasAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtDmiTxBiasAlarm.setStatus("mandatory")
_Cmefg100RmtDmiTxBiasCurrent_Type = Integer32
_Cmefg100RmtDmiTxBiasCurrent_Object = MibTableColumn
cmefg100RmtDmiTxBiasCurrent = _Cmefg100RmtDmiTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 146),
    _Cmefg100RmtDmiTxBiasCurrent_Type()
)
cmefg100RmtDmiTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtDmiTxBiasCurrent.setStatus("mandatory")
_Cmefg100RmtDmiTxPower_Type = Integer32
_Cmefg100RmtDmiTxPower_Object = MibTableColumn
cmefg100RmtDmiTxPower = _Cmefg100RmtDmiTxPower_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 147),
    _Cmefg100RmtDmiTxPower_Type()
)
cmefg100RmtDmiTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtDmiTxPower.setStatus("mandatory")


class _Cmefg100RmtDmiTxPowerAlarm_Type(Integer32):
    """Custom type cmefg100RmtDmiTxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("highAlarm", 6),
          ("highWarn", 4),
          ("lowAlarm", 5),
          ("lowWarn", 3),
          ("normal", 1),
          ("notSupported", 2))
    )


_Cmefg100RmtDmiTxPowerAlarm_Type.__name__ = "Integer32"
_Cmefg100RmtDmiTxPowerAlarm_Object = MibTableColumn
cmefg100RmtDmiTxPowerAlarm = _Cmefg100RmtDmiTxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 148),
    _Cmefg100RmtDmiTxPowerAlarm_Type()
)
cmefg100RmtDmiTxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtDmiTxPowerAlarm.setStatus("mandatory")


class _Cmefg100RmtFactoryReset_Type(Integer32):
    """Custom type cmefg100RmtFactoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 2),
          ("reset", 1))
    )


_Cmefg100RmtFactoryReset_Type.__name__ = "Integer32"
_Cmefg100RmtFactoryReset_Object = MibTableColumn
cmefg100RmtFactoryReset = _Cmefg100RmtFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 149),
    _Cmefg100RmtFactoryReset_Type()
)
cmefg100RmtFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtFactoryReset.setStatus("mandatory")


class _Cmefg100RmtFiberAutoNegot_Type(Integer32):
    """Custom type cmefg100RmtFiberAutoNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100RmtFiberAutoNegot_Type.__name__ = "Integer32"
_Cmefg100RmtFiberAutoNegot_Object = MibTableColumn
cmefg100RmtFiberAutoNegot = _Cmefg100RmtFiberAutoNegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 150),
    _Cmefg100RmtFiberAutoNegot_Type()
)
cmefg100RmtFiberAutoNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtFiberAutoNegot.setStatus("mandatory")


class _Cmefg100RmtFiberLink_Type(Integer32):
    """Custom type cmefg100RmtFiberLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cmefg100RmtFiberLink_Type.__name__ = "Integer32"
_Cmefg100RmtFiberLink_Object = MibTableColumn
cmefg100RmtFiberLink = _Cmefg100RmtFiberLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 151),
    _Cmefg100RmtFiberLink_Type()
)
cmefg100RmtFiberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtFiberLink.setStatus("mandatory")


class _Cmefg100RmtFiberPause_Type(Integer32):
    """Custom type cmefg100RmtFiberPause based on Integer32"""
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
        *(("asymmetricRx", 1),
          ("asymmetricTx", 2),
          ("notSupported", 4),
          ("symmetric", 3))
    )


_Cmefg100RmtFiberPause_Type.__name__ = "Integer32"
_Cmefg100RmtFiberPause_Object = MibTableColumn
cmefg100RmtFiberPause = _Cmefg100RmtFiberPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 152),
    _Cmefg100RmtFiberPause_Type()
)
cmefg100RmtFiberPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtFiberPause.setStatus("mandatory")


class _Cmefg100RmtFiberQosPause_Type(Integer32):
    """Custom type cmefg100RmtFiberQosPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100RmtFiberQosPause_Type.__name__ = "Integer32"
_Cmefg100RmtFiberQosPause_Object = MibTableColumn
cmefg100RmtFiberQosPause = _Cmefg100RmtFiberQosPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 153),
    _Cmefg100RmtFiberQosPause_Type()
)
cmefg100RmtFiberQosPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtFiberQosPause.setStatus("mandatory")
_Cmefg100RmtFirmwareRevision_Type = Integer32
_Cmefg100RmtFirmwareRevision_Object = MibTableColumn
cmefg100RmtFirmwareRevision = _Cmefg100RmtFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 154),
    _Cmefg100RmtFirmwareRevision_Type()
)
cmefg100RmtFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtFirmwareRevision.setStatus("mandatory")
_Cmefg100RmtFpgaRev_Type = Integer32
_Cmefg100RmtFpgaRev_Object = MibTableColumn
cmefg100RmtFpgaRev = _Cmefg100RmtFpgaRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 155),
    _Cmefg100RmtFpgaRev_Type()
)
cmefg100RmtFpgaRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtFpgaRev.setStatus("mandatory")


class _Cmefg100RmtOamActiveMode_Type(Integer32):
    """Custom type cmefg100RmtOamActiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_Cmefg100RmtOamActiveMode_Type.__name__ = "Integer32"
_Cmefg100RmtOamActiveMode_Object = MibTableColumn
cmefg100RmtOamActiveMode = _Cmefg100RmtOamActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 156),
    _Cmefg100RmtOamActiveMode_Type()
)
cmefg100RmtOamActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamActiveMode.setStatus("mandatory")


class _Cmefg100RmtOamCriticalEvent_Type(Integer32):
    """Custom type cmefg100RmtOamCriticalEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("normal", 2))
    )


_Cmefg100RmtOamCriticalEvent_Type.__name__ = "Integer32"
_Cmefg100RmtOamCriticalEvent_Object = MibTableColumn
cmefg100RmtOamCriticalEvent = _Cmefg100RmtOamCriticalEvent_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 157),
    _Cmefg100RmtOamCriticalEvent_Type()
)
cmefg100RmtOamCriticalEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamCriticalEvent.setStatus("mandatory")


class _Cmefg100RmtOamLastGasp_Type(Integer32):
    """Custom type cmefg100RmtOamLastGasp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("normal", 2))
    )


_Cmefg100RmtOamLastGasp_Type.__name__ = "Integer32"
_Cmefg100RmtOamLastGasp_Object = MibTableColumn
cmefg100RmtOamLastGasp = _Cmefg100RmtOamLastGasp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 158),
    _Cmefg100RmtOamLastGasp_Type()
)
cmefg100RmtOamLastGasp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamLastGasp.setStatus("mandatory")


class _Cmefg100RmtOamLinkEvents_Type(Integer32):
    """Custom type cmefg100RmtOamLinkEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_Cmefg100RmtOamLinkEvents_Type.__name__ = "Integer32"
_Cmefg100RmtOamLinkEvents_Object = MibTableColumn
cmefg100RmtOamLinkEvents = _Cmefg100RmtOamLinkEvents_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 159),
    _Cmefg100RmtOamLinkEvents_Type()
)
cmefg100RmtOamLinkEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamLinkEvents.setStatus("mandatory")


class _Cmefg100RmtOamLinkFault_Type(Integer32):
    """Custom type cmefg100RmtOamLinkFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("normal", 2))
    )


_Cmefg100RmtOamLinkFault_Type.__name__ = "Integer32"
_Cmefg100RmtOamLinkFault_Object = MibTableColumn
cmefg100RmtOamLinkFault = _Cmefg100RmtOamLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 160),
    _Cmefg100RmtOamLinkFault_Type()
)
cmefg100RmtOamLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamLinkFault.setStatus("mandatory")


class _Cmefg100RmtOamLocDteDisc_Type(Integer32):
    """Custom type cmefg100RmtOamLocDteDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("notCompleted", 2),
          ("unsatisfied", 3))
    )


_Cmefg100RmtOamLocDteDisc_Type.__name__ = "Integer32"
_Cmefg100RmtOamLocDteDisc_Object = MibTableColumn
cmefg100RmtOamLocDteDisc = _Cmefg100RmtOamLocDteDisc_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 161),
    _Cmefg100RmtOamLocDteDisc_Type()
)
cmefg100RmtOamLocDteDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamLocDteDisc.setStatus("mandatory")
_Cmefg100RmtOamPeerConfigRevision_Type = Integer32
_Cmefg100RmtOamPeerConfigRevision_Object = MibTableColumn
cmefg100RmtOamPeerConfigRevision = _Cmefg100RmtOamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 162),
    _Cmefg100RmtOamPeerConfigRevision_Type()
)
cmefg100RmtOamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamPeerConfigRevision.setStatus("mandatory")
_Cmefg100RmtOamPeerMacAddress_Type = MacAddress
_Cmefg100RmtOamPeerMacAddress_Object = MibTableColumn
cmefg100RmtOamPeerMacAddress = _Cmefg100RmtOamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 163),
    _Cmefg100RmtOamPeerMacAddress_Type()
)
cmefg100RmtOamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamPeerMacAddress.setStatus("mandatory")
_Cmefg100RmtOamPeerMaxOamPduSize_Type = Integer32
_Cmefg100RmtOamPeerMaxOamPduSize_Object = MibTableColumn
cmefg100RmtOamPeerMaxOamPduSize = _Cmefg100RmtOamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 164),
    _Cmefg100RmtOamPeerMaxOamPduSize_Type()
)
cmefg100RmtOamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamPeerMaxOamPduSize.setStatus("mandatory")


class _Cmefg100RmtOamPeerMultiplexorState_Type(Integer32):
    """Custom type cmefg100RmtOamPeerMultiplexorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 2),
          ("forwarding", 1))
    )


_Cmefg100RmtOamPeerMultiplexorState_Type.__name__ = "Integer32"
_Cmefg100RmtOamPeerMultiplexorState_Object = MibTableColumn
cmefg100RmtOamPeerMultiplexorState = _Cmefg100RmtOamPeerMultiplexorState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 165),
    _Cmefg100RmtOamPeerMultiplexorState_Type()
)
cmefg100RmtOamPeerMultiplexorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamPeerMultiplexorState.setStatus("mandatory")


class _Cmefg100RmtOamPeerParserState_Type(Integer32):
    """Custom type cmefg100RmtOamPeerParserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 2),
          ("forwarding", 1),
          ("looping", 3))
    )


_Cmefg100RmtOamPeerParserState_Type.__name__ = "Integer32"
_Cmefg100RmtOamPeerParserState_Object = MibTableColumn
cmefg100RmtOamPeerParserState = _Cmefg100RmtOamPeerParserState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 166),
    _Cmefg100RmtOamPeerParserState_Type()
)
cmefg100RmtOamPeerParserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamPeerParserState.setStatus("mandatory")


class _Cmefg100RmtOamPeerVendorInfo_Type(OctetString):
    """Custom type cmefg100RmtOamPeerVendorInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cmefg100RmtOamPeerVendorInfo_Type.__name__ = "OctetString"
_Cmefg100RmtOamPeerVendorInfo_Object = MibTableColumn
cmefg100RmtOamPeerVendorInfo = _Cmefg100RmtOamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 167),
    _Cmefg100RmtOamPeerVendorInfo_Type()
)
cmefg100RmtOamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamPeerVendorInfo.setStatus("mandatory")


class _Cmefg100RmtOamPeerVendorOui_Type(OctetString):
    """Custom type cmefg100RmtOamPeerVendorOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Cmefg100RmtOamPeerVendorOui_Type.__name__ = "OctetString"
_Cmefg100RmtOamPeerVendorOui_Object = MibTableColumn
cmefg100RmtOamPeerVendorOui = _Cmefg100RmtOamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 168),
    _Cmefg100RmtOamPeerVendorOui_Type()
)
cmefg100RmtOamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamPeerVendorOui.setStatus("mandatory")


class _Cmefg100RmtOamRmtDteDisc_Type(Integer32):
    """Custom type cmefg100RmtOamRmtDteDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("notCompleted", 2),
          ("unsatisfied", 3))
    )


_Cmefg100RmtOamRmtDteDisc_Type.__name__ = "Integer32"
_Cmefg100RmtOamRmtDteDisc_Object = MibTableColumn
cmefg100RmtOamRmtDteDisc = _Cmefg100RmtOamRmtDteDisc_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 169),
    _Cmefg100RmtOamRmtDteDisc_Type()
)
cmefg100RmtOamRmtDteDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamRmtDteDisc.setStatus("mandatory")


class _Cmefg100RmtOamRmtLoopback_Type(Integer32):
    """Custom type cmefg100RmtOamRmtLoopback based on Integer32"""
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
        *(("disabled", 3),
          ("enabledAlternate", 2),
          ("enabledOam", 1),
          ("notSupported", 4))
    )


_Cmefg100RmtOamRmtLoopback_Type.__name__ = "Integer32"
_Cmefg100RmtOamRmtLoopback_Object = MibTableColumn
cmefg100RmtOamRmtLoopback = _Cmefg100RmtOamRmtLoopback_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 170),
    _Cmefg100RmtOamRmtLoopback_Type()
)
cmefg100RmtOamRmtLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtOamRmtLoopback.setStatus("mandatory")


class _Cmefg100RmtOamUnidirectional_Type(Integer32):
    """Custom type cmefg100RmtOamUnidirectional based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_Cmefg100RmtOamUnidirectional_Type.__name__ = "Integer32"
_Cmefg100RmtOamUnidirectional_Object = MibTableColumn
cmefg100RmtOamUnidirectional = _Cmefg100RmtOamUnidirectional_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 171),
    _Cmefg100RmtOamUnidirectional_Type()
)
cmefg100RmtOamUnidirectional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamUnidirectional.setStatus("mandatory")


class _Cmefg100RmtOamVarRetrieval_Type(Integer32):
    """Custom type cmefg100RmtOamVarRetrieval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_Cmefg100RmtOamVarRetrieval_Type.__name__ = "Integer32"
_Cmefg100RmtOamVarRetrieval_Object = MibTableColumn
cmefg100RmtOamVarRetrieval = _Cmefg100RmtOamVarRetrieval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 172),
    _Cmefg100RmtOamVarRetrieval_Type()
)
cmefg100RmtOamVarRetrieval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtOamVarRetrieval.setStatus("mandatory")


class _Cmefg100RmtSelfTestFailed_Type(Integer32):
    """Custom type cmefg100RmtSelfTestFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cmefg100RmtSelfTestFailed_Type.__name__ = "Integer32"
_Cmefg100RmtSelfTestFailed_Object = MibTableColumn
cmefg100RmtSelfTestFailed = _Cmefg100RmtSelfTestFailed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 173),
    _Cmefg100RmtSelfTestFailed_Type()
)
cmefg100RmtSelfTestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtSelfTestFailed.setStatus("mandatory")
_Cmefg100RmtSerialNumber_Type = Integer32
_Cmefg100RmtSerialNumber_Object = MibTableColumn
cmefg100RmtSerialNumber = _Cmefg100RmtSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 174),
    _Cmefg100RmtSerialNumber_Type()
)
cmefg100RmtSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtSerialNumber.setStatus("mandatory")


class _Cmefg100RmtTpAdv1000FDX_Type(Integer32):
    """Custom type cmefg100RmtTpAdv1000FDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100RmtTpAdv1000FDX_Type.__name__ = "Integer32"
_Cmefg100RmtTpAdv1000FDX_Object = MibTableColumn
cmefg100RmtTpAdv1000FDX = _Cmefg100RmtTpAdv1000FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 175),
    _Cmefg100RmtTpAdv1000FDX_Type()
)
cmefg100RmtTpAdv1000FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpAdv1000FDX.setStatus("mandatory")


class _Cmefg100RmtTpAdv1000HDX_Type(Integer32):
    """Custom type cmefg100RmtTpAdv1000HDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100RmtTpAdv1000HDX_Type.__name__ = "Integer32"
_Cmefg100RmtTpAdv1000HDX_Object = MibTableColumn
cmefg100RmtTpAdv1000HDX = _Cmefg100RmtTpAdv1000HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 176),
    _Cmefg100RmtTpAdv1000HDX_Type()
)
cmefg100RmtTpAdv1000HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpAdv1000HDX.setStatus("mandatory")


class _Cmefg100RmtTpAdv100FDX_Type(Integer32):
    """Custom type cmefg100RmtTpAdv100FDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100RmtTpAdv100FDX_Type.__name__ = "Integer32"
_Cmefg100RmtTpAdv100FDX_Object = MibTableColumn
cmefg100RmtTpAdv100FDX = _Cmefg100RmtTpAdv100FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 177),
    _Cmefg100RmtTpAdv100FDX_Type()
)
cmefg100RmtTpAdv100FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpAdv100FDX.setStatus("mandatory")


class _Cmefg100RmtTpAdv100HDX_Type(Integer32):
    """Custom type cmefg100RmtTpAdv100HDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100RmtTpAdv100HDX_Type.__name__ = "Integer32"
_Cmefg100RmtTpAdv100HDX_Object = MibTableColumn
cmefg100RmtTpAdv100HDX = _Cmefg100RmtTpAdv100HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 178),
    _Cmefg100RmtTpAdv100HDX_Type()
)
cmefg100RmtTpAdv100HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpAdv100HDX.setStatus("mandatory")


class _Cmefg100RmtTpAdv10FDX_Type(Integer32):
    """Custom type cmefg100RmtTpAdv10FDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100RmtTpAdv10FDX_Type.__name__ = "Integer32"
_Cmefg100RmtTpAdv10FDX_Object = MibTableColumn
cmefg100RmtTpAdv10FDX = _Cmefg100RmtTpAdv10FDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 179),
    _Cmefg100RmtTpAdv10FDX_Type()
)
cmefg100RmtTpAdv10FDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpAdv10FDX.setStatus("mandatory")


class _Cmefg100RmtTpAdv10HDX_Type(Integer32):
    """Custom type cmefg100RmtTpAdv10HDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Cmefg100RmtTpAdv10HDX_Type.__name__ = "Integer32"
_Cmefg100RmtTpAdv10HDX_Object = MibTableColumn
cmefg100RmtTpAdv10HDX = _Cmefg100RmtTpAdv10HDX_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 180),
    _Cmefg100RmtTpAdv10HDX_Type()
)
cmefg100RmtTpAdv10HDX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpAdv10HDX.setStatus("mandatory")


class _Cmefg100RmtTpAutoNegot_Type(Integer32):
    """Custom type cmefg100RmtTpAutoNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100RmtTpAutoNegot_Type.__name__ = "Integer32"
_Cmefg100RmtTpAutoNegot_Object = MibTableColumn
cmefg100RmtTpAutoNegot = _Cmefg100RmtTpAutoNegot_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 181),
    _Cmefg100RmtTpAutoNegot_Type()
)
cmefg100RmtTpAutoNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpAutoNegot.setStatus("mandatory")


class _Cmefg100RmtTpCross_Type(Integer32):
    """Custom type cmefg100RmtTpCross based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("forceMDI", 1),
          ("forceMDI-X", 2))
    )


_Cmefg100RmtTpCross_Type.__name__ = "Integer32"
_Cmefg100RmtTpCross_Object = MibTableColumn
cmefg100RmtTpCross = _Cmefg100RmtTpCross_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 182),
    _Cmefg100RmtTpCross_Type()
)
cmefg100RmtTpCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpCross.setStatus("mandatory")


class _Cmefg100RmtTpDuplex_Type(Integer32):
    """Custom type cmefg100RmtTpDuplex based on Integer32"""
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
        *(("autoFDX", 3),
          ("autoHDX", 4),
          ("forceFDX", 1),
          ("forceHDX", 2),
          ("negotiating", 5))
    )


_Cmefg100RmtTpDuplex_Type.__name__ = "Integer32"
_Cmefg100RmtTpDuplex_Object = MibTableColumn
cmefg100RmtTpDuplex = _Cmefg100RmtTpDuplex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 183),
    _Cmefg100RmtTpDuplex_Type()
)
cmefg100RmtTpDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpDuplex.setStatus("mandatory")


class _Cmefg100RmtTpLink_Type(Integer32):
    """Custom type cmefg100RmtTpLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cmefg100RmtTpLink_Type.__name__ = "Integer32"
_Cmefg100RmtTpLink_Object = MibTableColumn
cmefg100RmtTpLink = _Cmefg100RmtTpLink_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 184),
    _Cmefg100RmtTpLink_Type()
)
cmefg100RmtTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100RmtTpLink.setStatus("mandatory")


class _Cmefg100RmtTpPause_Type(Integer32):
    """Custom type cmefg100RmtTpPause based on Integer32"""
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
        *(("asymmetricRx", 1),
          ("asymmetricTx", 2),
          ("notSupported", 4),
          ("symmetric", 3))
    )


_Cmefg100RmtTpPause_Type.__name__ = "Integer32"
_Cmefg100RmtTpPause_Object = MibTableColumn
cmefg100RmtTpPause = _Cmefg100RmtTpPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 185),
    _Cmefg100RmtTpPause_Type()
)
cmefg100RmtTpPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpPause.setStatus("mandatory")


class _Cmefg100RmtTpQosPause_Type(Integer32):
    """Custom type cmefg100RmtTpQosPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100RmtTpQosPause_Type.__name__ = "Integer32"
_Cmefg100RmtTpQosPause_Object = MibTableColumn
cmefg100RmtTpQosPause = _Cmefg100RmtTpQosPause_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 186),
    _Cmefg100RmtTpQosPause_Type()
)
cmefg100RmtTpQosPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpQosPause.setStatus("mandatory")


class _Cmefg100RmtTpSpeed_Type(Integer32):
    """Custom type cmefg100RmtTpSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto1000Mbps", 5),
          ("auto100Mbps", 4),
          ("auto10Mbps", 3),
          ("force100Mbps", 2),
          ("force10Mbps", 1),
          ("negotiating", 6))
    )


_Cmefg100RmtTpSpeed_Type.__name__ = "Integer32"
_Cmefg100RmtTpSpeed_Object = MibTableColumn
cmefg100RmtTpSpeed = _Cmefg100RmtTpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 187),
    _Cmefg100RmtTpSpeed_Type()
)
cmefg100RmtTpSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtTpSpeed.setStatus("mandatory")
_Cmefg100RmtUptime_Type = TimeTicks
_Cmefg100RmtUptime_Object = MibTableColumn
cmefg100RmtUptime = _Cmefg100RmtUptime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 188),
    _Cmefg100RmtUptime_Type()
)
cmefg100RmtUptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100RmtUptime.setStatus("mandatory")


class _Cmefg100VlanCacheCmd_Type(Integer32):
    """Custom type cmefg100VlanCacheCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 2),
          ("loadCache", 1),
          ("release", 3))
    )


_Cmefg100VlanCacheCmd_Type.__name__ = "Integer32"
_Cmefg100VlanCacheCmd_Object = MibTableColumn
cmefg100VlanCacheCmd = _Cmefg100VlanCacheCmd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 189),
    _Cmefg100VlanCacheCmd_Type()
)
cmefg100VlanCacheCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanCacheCmd.setStatus("mandatory")


class _Cmefg100VlanCacheState_Type(Integer32):
    """Custom type cmefg100VlanCacheState based on Integer32"""
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
        *(("bufferBusy", 4),
          ("empty", 2),
          ("ready", 1),
          ("transferring", 3))
    )


_Cmefg100VlanCacheState_Type.__name__ = "Integer32"
_Cmefg100VlanCacheState_Object = MibTableColumn
cmefg100VlanCacheState = _Cmefg100VlanCacheState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 190),
    _Cmefg100VlanCacheState_Type()
)
cmefg100VlanCacheState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanCacheState.setStatus("mandatory")


class _Cmefg100VlanEditCmd_Type(Integer32):
    """Custom type cmefg100VlanEditCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("doNothing", 3),
          ("write", 1))
    )


_Cmefg100VlanEditCmd_Type.__name__ = "Integer32"
_Cmefg100VlanEditCmd_Object = MibTableColumn
cmefg100VlanEditCmd = _Cmefg100VlanEditCmd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 191),
    _Cmefg100VlanEditCmd_Type()
)
cmefg100VlanEditCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanEditCmd.setStatus("mandatory")


class _Cmefg100VlanEditFwdFiber_Type(Integer32):
    """Custom type cmefg100VlanEditFwdFiber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2))
    )


_Cmefg100VlanEditFwdFiber_Type.__name__ = "Integer32"
_Cmefg100VlanEditFwdFiber_Object = MibTableColumn
cmefg100VlanEditFwdFiber = _Cmefg100VlanEditFwdFiber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 192),
    _Cmefg100VlanEditFwdFiber_Type()
)
cmefg100VlanEditFwdFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanEditFwdFiber.setStatus("mandatory")


class _Cmefg100VlanEditFwdTp_Type(Integer32):
    """Custom type cmefg100VlanEditFwdTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2))
    )


_Cmefg100VlanEditFwdTp_Type.__name__ = "Integer32"
_Cmefg100VlanEditFwdTp_Object = MibTableColumn
cmefg100VlanEditFwdTp = _Cmefg100VlanEditFwdTp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 193),
    _Cmefg100VlanEditFwdTp_Type()
)
cmefg100VlanEditFwdTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanEditFwdTp.setStatus("mandatory")


class _Cmefg100VlanEditUntagFiber_Type(Integer32):
    """Custom type cmefg100VlanEditUntagFiber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asIs", 2),
          ("untag", 1))
    )


_Cmefg100VlanEditUntagFiber_Type.__name__ = "Integer32"
_Cmefg100VlanEditUntagFiber_Object = MibTableColumn
cmefg100VlanEditUntagFiber = _Cmefg100VlanEditUntagFiber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 194),
    _Cmefg100VlanEditUntagFiber_Type()
)
cmefg100VlanEditUntagFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanEditUntagFiber.setStatus("mandatory")


class _Cmefg100VlanEditUntagTp_Type(Integer32):
    """Custom type cmefg100VlanEditUntagTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asIs", 2),
          ("untag", 1))
    )


_Cmefg100VlanEditUntagTp_Type.__name__ = "Integer32"
_Cmefg100VlanEditUntagTp_Object = MibTableColumn
cmefg100VlanEditUntagTp = _Cmefg100VlanEditUntagTp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 195),
    _Cmefg100VlanEditUntagTp_Type()
)
cmefg100VlanEditUntagTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanEditUntagTp.setStatus("mandatory")
_Cmefg100VlanEditVid_Type = Integer32
_Cmefg100VlanEditVid_Object = MibTableColumn
cmefg100VlanEditVid = _Cmefg100VlanEditVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 196),
    _Cmefg100VlanEditVid_Type()
)
cmefg100VlanEditVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanEditVid.setStatus("mandatory")


class _Cmefg100VlanEnable_Type(Integer32):
    """Custom type cmefg100VlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cmefg100VlanEnable_Type.__name__ = "Integer32"
_Cmefg100VlanEnable_Object = MibTableColumn
cmefg100VlanEnable = _Cmefg100VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 197),
    _Cmefg100VlanEnable_Type()
)
cmefg100VlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanEnable.setStatus("mandatory")
_Cmefg100VlanEntries_Type = Integer32
_Cmefg100VlanEntries_Object = MibTableColumn
cmefg100VlanEntries = _Cmefg100VlanEntries_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 198),
    _Cmefg100VlanEntries_Type()
)
cmefg100VlanEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanEntries.setStatus("mandatory")


class _Cmefg100VlanFiberDefaultPri_Type(Integer32):
    """Custom type cmefg100VlanFiberDefaultPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cmefg100VlanFiberDefaultPri_Type.__name__ = "Integer32"
_Cmefg100VlanFiberDefaultPri_Object = MibTableColumn
cmefg100VlanFiberDefaultPri = _Cmefg100VlanFiberDefaultPri_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 199),
    _Cmefg100VlanFiberDefaultPri_Type()
)
cmefg100VlanFiberDefaultPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanFiberDefaultPri.setStatus("mandatory")


class _Cmefg100VlanFiberDefaultVid_Type(Integer32):
    """Custom type cmefg100VlanFiberDefaultVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cmefg100VlanFiberDefaultVid_Type.__name__ = "Integer32"
_Cmefg100VlanFiberDefaultVid_Object = MibTableColumn
cmefg100VlanFiberDefaultVid = _Cmefg100VlanFiberDefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 200),
    _Cmefg100VlanFiberDefaultVid_Type()
)
cmefg100VlanFiberDefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanFiberDefaultVid.setStatus("mandatory")


class _Cmefg100VlanFiberInUntaggedDrop_Type(Integer32):
    """Custom type cmefg100VlanFiberInUntaggedDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2),
          ("notApplicable", 3))
    )


_Cmefg100VlanFiberInUntaggedDrop_Type.__name__ = "Integer32"
_Cmefg100VlanFiberInUntaggedDrop_Object = MibTableColumn
cmefg100VlanFiberInUntaggedDrop = _Cmefg100VlanFiberInUntaggedDrop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 201),
    _Cmefg100VlanFiberInUntaggedDrop_Type()
)
cmefg100VlanFiberInUntaggedDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanFiberInUntaggedDrop.setStatus("mandatory")


class _Cmefg100VlanFwdFiberTbl_Type(Integer32):
    """Custom type cmefg100VlanFwdFiberTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2))
    )


_Cmefg100VlanFwdFiberTbl_Type.__name__ = "Integer32"
_Cmefg100VlanFwdFiberTbl_Object = MibTableColumn
cmefg100VlanFwdFiberTbl = _Cmefg100VlanFwdFiberTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 202),
    _Cmefg100VlanFwdFiberTbl_Type()
)
cmefg100VlanFwdFiberTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanFwdFiberTbl.setStatus("mandatory")


class _Cmefg100VlanFwdTpTbl_Type(Integer32):
    """Custom type cmefg100VlanFwdTpTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2))
    )


_Cmefg100VlanFwdTpTbl_Type.__name__ = "Integer32"
_Cmefg100VlanFwdTpTbl_Object = MibTableColumn
cmefg100VlanFwdTpTbl = _Cmefg100VlanFwdTpTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 203),
    _Cmefg100VlanFwdTpTbl_Type()
)
cmefg100VlanFwdTpTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanFwdTpTbl.setStatus("mandatory")


class _Cmefg100VlanIngressVidHitNoMem_Type(Integer32):
    """Custom type cmefg100VlanIngressVidHitNoMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("forward", 1),
          ("learn", 3))
    )


_Cmefg100VlanIngressVidHitNoMem_Type.__name__ = "Integer32"
_Cmefg100VlanIngressVidHitNoMem_Object = MibTableColumn
cmefg100VlanIngressVidHitNoMem = _Cmefg100VlanIngressVidHitNoMem_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 204),
    _Cmefg100VlanIngressVidHitNoMem_Type()
)
cmefg100VlanIngressVidHitNoMem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanIngressVidHitNoMem.setStatus("mandatory")


class _Cmefg100VlanIngressVidMiss_Type(Integer32):
    """Custom type cmefg100VlanIngressVidMiss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("flood", 1))
    )


_Cmefg100VlanIngressVidMiss_Type.__name__ = "Integer32"
_Cmefg100VlanIngressVidMiss_Object = MibTableColumn
cmefg100VlanIngressVidMiss = _Cmefg100VlanIngressVidMiss_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 205),
    _Cmefg100VlanIngressVidMiss_Type()
)
cmefg100VlanIngressVidMiss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanIngressVidMiss.setStatus("mandatory")


class _Cmefg100VlanPriMapTbl_Type(Integer32):
    """Custom type cmefg100VlanPriMapTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cmefg100VlanPriMapTbl_Type.__name__ = "Integer32"
_Cmefg100VlanPriMapTbl_Object = MibTableColumn
cmefg100VlanPriMapTbl = _Cmefg100VlanPriMapTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 206),
    _Cmefg100VlanPriMapTbl_Type()
)
cmefg100VlanPriMapTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanPriMapTbl.setStatus("mandatory")


class _Cmefg100VlanPriTagCtrl_Type(Integer32):
    """Custom type cmefg100VlanPriTagCtrl based on Integer32"""
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
        *(("asIs", 1),
          ("notApplicable", 5),
          ("remapBoth", 4),
          ("remapPriority", 2),
          ("remapVid", 3))
    )


_Cmefg100VlanPriTagCtrl_Type.__name__ = "Integer32"
_Cmefg100VlanPriTagCtrl_Object = MibTableColumn
cmefg100VlanPriTagCtrl = _Cmefg100VlanPriTagCtrl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 207),
    _Cmefg100VlanPriTagCtrl_Type()
)
cmefg100VlanPriTagCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanPriTagCtrl.setStatus("mandatory")


class _Cmefg100VlanSetFailed_Type(Integer32):
    """Custom type cmefg100VlanSetFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Cmefg100VlanSetFailed_Type.__name__ = "Integer32"
_Cmefg100VlanSetFailed_Object = MibTableColumn
cmefg100VlanSetFailed = _Cmefg100VlanSetFailed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 208),
    _Cmefg100VlanSetFailed_Type()
)
cmefg100VlanSetFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanSetFailed.setStatus("mandatory")


class _Cmefg100VlanTagIn_Type(Integer32):
    """Custom type cmefg100VlanTagIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTag", 2),
          ("notApplicable", 3),
          ("tag", 1))
    )


_Cmefg100VlanTagIn_Type.__name__ = "Integer32"
_Cmefg100VlanTagIn_Object = MibTableColumn
cmefg100VlanTagIn = _Cmefg100VlanTagIn_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 209),
    _Cmefg100VlanTagIn_Type()
)
cmefg100VlanTagIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanTagIn.setStatus("mandatory")


class _Cmefg100VlanTpDefaultPri_Type(Integer32):
    """Custom type cmefg100VlanTpDefaultPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cmefg100VlanTpDefaultPri_Type.__name__ = "Integer32"
_Cmefg100VlanTpDefaultPri_Object = MibTableColumn
cmefg100VlanTpDefaultPri = _Cmefg100VlanTpDefaultPri_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 210),
    _Cmefg100VlanTpDefaultPri_Type()
)
cmefg100VlanTpDefaultPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanTpDefaultPri.setStatus("mandatory")


class _Cmefg100VlanTpDefaultVid_Type(Integer32):
    """Custom type cmefg100VlanTpDefaultVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cmefg100VlanTpDefaultVid_Type.__name__ = "Integer32"
_Cmefg100VlanTpDefaultVid_Object = MibTableColumn
cmefg100VlanTpDefaultVid = _Cmefg100VlanTpDefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 211),
    _Cmefg100VlanTpDefaultVid_Type()
)
cmefg100VlanTpDefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanTpDefaultVid.setStatus("mandatory")


class _Cmefg100VlanTpInUntaggedDrop_Type(Integer32):
    """Custom type cmefg100VlanTpInUntaggedDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2))
    )


_Cmefg100VlanTpInUntaggedDrop_Type.__name__ = "Integer32"
_Cmefg100VlanTpInUntaggedDrop_Object = MibTableColumn
cmefg100VlanTpInUntaggedDrop = _Cmefg100VlanTpInUntaggedDrop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 212),
    _Cmefg100VlanTpInUntaggedDrop_Type()
)
cmefg100VlanTpInUntaggedDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanTpInUntaggedDrop.setStatus("mandatory")


class _Cmefg100VlanUntagFiberTbl_Type(Integer32):
    """Custom type cmefg100VlanUntagFiberTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asIs", 2),
          ("untag", 1))
    )


_Cmefg100VlanUntagFiberTbl_Type.__name__ = "Integer32"
_Cmefg100VlanUntagFiberTbl_Object = MibTableColumn
cmefg100VlanUntagFiberTbl = _Cmefg100VlanUntagFiberTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 213),
    _Cmefg100VlanUntagFiberTbl_Type()
)
cmefg100VlanUntagFiberTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanUntagFiberTbl.setStatus("mandatory")


class _Cmefg100VlanUntagTpTbl_Type(Integer32):
    """Custom type cmefg100VlanUntagTpTbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asIs", 2),
          ("untag", 1))
    )


_Cmefg100VlanUntagTpTbl_Type.__name__ = "Integer32"
_Cmefg100VlanUntagTpTbl_Object = MibTableColumn
cmefg100VlanUntagTpTbl = _Cmefg100VlanUntagTpTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 214),
    _Cmefg100VlanUntagTpTbl_Type()
)
cmefg100VlanUntagTpTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanUntagTpTbl.setStatus("mandatory")


class _Cmefg100VlanVidTagCtrl_Type(Integer32):
    """Custom type cmefg100VlanVidTagCtrl based on Integer32"""
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
        *(("asIs", 1),
          ("notApplicable", 5),
          ("remapBoth", 4),
          ("remapPriority", 2),
          ("remapVid", 3))
    )


_Cmefg100VlanVidTagCtrl_Type.__name__ = "Integer32"
_Cmefg100VlanVidTagCtrl_Object = MibTableColumn
cmefg100VlanVidTagCtrl = _Cmefg100VlanVidTagCtrl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 215),
    _Cmefg100VlanVidTagCtrl_Type()
)
cmefg100VlanVidTagCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100VlanVidTagCtrl.setStatus("mandatory")
_Cmefg100VlanVidTbl_Type = Integer32
_Cmefg100VlanVidTbl_Object = MibTableColumn
cmefg100VlanVidTbl = _Cmefg100VlanVidTbl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 216),
    _Cmefg100VlanVidTbl_Type()
)
cmefg100VlanVidTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmefg100VlanVidTbl.setStatus("mandatory")
_Cmefg100CacheClean_Type = Integer32
_Cmefg100CacheClean_Object = MibTableColumn
cmefg100CacheClean = _Cmefg100CacheClean_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 1, 2, 2, 27, 1, 217),
    _Cmefg100CacheClean_Type()
)
cmefg100CacheClean.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmefg100CacheClean.setStatus("mandatory")
_Backplane_ObjectIdentity = ObjectIdentity
backplane = _Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2)
)
_Mcc16_ObjectIdentity = ObjectIdentity
mcc16 = _Mcc16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1)
)
_Mcc16Common_ObjectIdentity = ObjectIdentity
mcc16Common = _Mcc16Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1)
)


class _Mcc16ComHwReset_Type(Integer32):
    """Custom type mcc16ComHwReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_Mcc16ComHwReset_Type.__name__ = "Integer32"
_Mcc16ComHwReset_Object = MibScalar
mcc16ComHwReset = _Mcc16ComHwReset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 1),
    _Mcc16ComHwReset_Type()
)
mcc16ComHwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcc16ComHwReset.setStatus("mandatory")


class _Mcc16ComMgmtHwRev_Type(DisplayString):
    """Custom type mcc16ComMgmtHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mcc16ComMgmtHwRev_Type.__name__ = "DisplayString"
_Mcc16ComMgmtHwRev_Object = MibScalar
mcc16ComMgmtHwRev = _Mcc16ComMgmtHwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 2),
    _Mcc16ComMgmtHwRev_Type()
)
mcc16ComMgmtHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcc16ComMgmtHwRev.setStatus("mandatory")


class _Mcc16ComMgmtSwRev_Type(DisplayString):
    """Custom type mcc16ComMgmtSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mcc16ComMgmtSwRev_Type.__name__ = "DisplayString"
_Mcc16ComMgmtSwRev_Object = MibScalar
mcc16ComMgmtSwRev = _Mcc16ComMgmtSwRev_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 3),
    _Mcc16ComMgmtSwRev_Type()
)
mcc16ComMgmtSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcc16ComMgmtSwRev.setStatus("mandatory")
_Mcc16ComIpAddr_Type = IpAddress
_Mcc16ComIpAddr_Object = MibScalar
mcc16ComIpAddr = _Mcc16ComIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 4),
    _Mcc16ComIpAddr_Type()
)
mcc16ComIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcc16ComIpAddr.setStatus("mandatory")
_Mcc16ComNetMask_Type = IpAddress
_Mcc16ComNetMask_Object = MibScalar
mcc16ComNetMask = _Mcc16ComNetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 5),
    _Mcc16ComNetMask_Type()
)
mcc16ComNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcc16ComNetMask.setStatus("mandatory")
_Mcc16ComGateway_Type = IpAddress
_Mcc16ComGateway_Object = MibScalar
mcc16ComGateway = _Mcc16ComGateway_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 6),
    _Mcc16ComGateway_Type()
)
mcc16ComGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcc16ComGateway.setStatus("mandatory")


class _Mcc16ComPS1Power_Type(Integer32):
    """Custom type mcc16ComPS1Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Mcc16ComPS1Power_Type.__name__ = "Integer32"
_Mcc16ComPS1Power_Object = MibScalar
mcc16ComPS1Power = _Mcc16ComPS1Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 7),
    _Mcc16ComPS1Power_Type()
)
mcc16ComPS1Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcc16ComPS1Power.setStatus("mandatory")


class _Mcc16ComPS1InUse_Type(Integer32):
    """Custom type mcc16ComPS1InUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Mcc16ComPS1InUse_Type.__name__ = "Integer32"
_Mcc16ComPS1InUse_Object = MibScalar
mcc16ComPS1InUse = _Mcc16ComPS1InUse_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 8),
    _Mcc16ComPS1InUse_Type()
)
mcc16ComPS1InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcc16ComPS1InUse.setStatus("mandatory")


class _Mcc16ComPS2Power_Type(Integer32):
    """Custom type mcc16ComPS2Power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Mcc16ComPS2Power_Type.__name__ = "Integer32"
_Mcc16ComPS2Power_Object = MibScalar
mcc16ComPS2Power = _Mcc16ComPS2Power_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 9),
    _Mcc16ComPS2Power_Type()
)
mcc16ComPS2Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcc16ComPS2Power.setStatus("mandatory")


class _Mcc16ComPS2InUse_Type(Integer32):
    """Custom type mcc16ComPS2InUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Mcc16ComPS2InUse_Type.__name__ = "Integer32"
_Mcc16ComPS2InUse_Object = MibScalar
mcc16ComPS2InUse = _Mcc16ComPS2InUse_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 10),
    _Mcc16ComPS2InUse_Type()
)
mcc16ComPS2InUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcc16ComPS2InUse.setStatus("mandatory")


class _Mcc16ComNotes_Type(DisplayString):
    """Custom type mcc16ComNotes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_Mcc16ComNotes_Type.__name__ = "DisplayString"
_Mcc16ComNotes_Object = MibScalar
mcc16ComNotes = _Mcc16ComNotes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 1, 11),
    _Mcc16ComNotes_Type()
)
mcc16ComNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcc16ComNotes.setStatus("mandatory")
_Mcc16Ver1_ObjectIdentity = ObjectIdentity
mcc16Ver1 = _Mcc16Ver1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 2)
)
_Mcc16SlotTable_Object = MibTable
mcc16SlotTable = _Mcc16SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mcc16SlotTable.setStatus("mandatory")
_Mcc16SlotEntry_Object = MibTableRow
mcc16SlotEntry = _Mcc16SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 2, 1, 1)
)
mcc16SlotEntry.setIndexNames(
    (0, "MCC16-MIB", "mcc16Index"),
)
if mibBuilder.loadTexts:
    mcc16SlotEntry.setStatus("mandatory")


class _Mcc16Index_Type(Integer32):
    """Custom type mcc16Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Mcc16Index_Type.__name__ = "Integer32"
_Mcc16Index_Object = MibTableColumn
mcc16Index = _Mcc16Index_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 2, 1, 1, 1),
    _Mcc16Index_Type()
)
mcc16Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcc16Index.setStatus("mandatory")
_Mcc16DeviceType_Type = ObjectIdentifier
_Mcc16DeviceType_Object = MibTableColumn
mcc16DeviceType = _Mcc16DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 1, 2, 1, 1, 2),
    _Mcc16DeviceType_Type()
)
mcc16DeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcc16DeviceType.setStatus("mandatory")
_Cps_ObjectIdentity = ObjectIdentity
cps = _Cps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2)
)
_CpsCabSummary_ObjectIdentity = ObjectIdentity
cpsCabSummary = _CpsCabSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 1)
)
_CpsCabinetTable_Object = MibTable
cpsCabinetTable = _CpsCabinetTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpsCabinetTable.setStatus("mandatory")
_CpsCabinetEntry_Object = MibTableRow
cpsCabinetEntry = _CpsCabinetEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 1, 1, 1)
)
cpsCabinetEntry.setIndexNames(
    (0, "MCC16-MIB", "cpsCabinetBiaIndex"),
)
if mibBuilder.loadTexts:
    cpsCabinetEntry.setStatus("mandatory")
_CpsCabinetBiaIndex_Type = Integer32
_CpsCabinetBiaIndex_Object = MibTableColumn
cpsCabinetBiaIndex = _CpsCabinetBiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 1, 1, 1, 1),
    _CpsCabinetBiaIndex_Type()
)
cpsCabinetBiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsCabinetBiaIndex.setStatus("mandatory")
_CpsCabinetModel_Type = ObjectIdentifier
_CpsCabinetModel_Object = MibTableColumn
cpsCabinetModel = _CpsCabinetModel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 1, 1, 1, 2),
    _CpsCabinetModel_Type()
)
cpsCabinetModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsCabinetModel.setStatus("mandatory")
_CpsCabinetDescription_Type = DisplayString
_CpsCabinetDescription_Object = MibTableColumn
cpsCabinetDescription = _CpsCabinetDescription_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 1, 1, 1, 3),
    _CpsCabinetDescription_Type()
)
cpsCabinetDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsCabinetDescription.setStatus("mandatory")
_CpsCabinetSequence_Type = Integer32
_CpsCabinetSequence_Object = MibTableColumn
cpsCabinetSequence = _CpsCabinetSequence_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 1, 1, 1, 4),
    _CpsCabinetSequence_Type()
)
cpsCabinetSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsCabinetSequence.setStatus("mandatory")
_CpsCabDetail_ObjectIdentity = ObjectIdentity
cpsCabDetail = _CpsCabDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2)
)
_CpsMc1800Table_Object = MibTable
cpsMc1800Table = _CpsMc1800Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpsMc1800Table.setStatus("mandatory")
_CpsMc1800Entry_Object = MibTableRow
cpsMc1800Entry = _CpsMc1800Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 1, 1)
)
cpsMc1800Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsMc1800BiaIndex"),
)
if mibBuilder.loadTexts:
    cpsMc1800Entry.setStatus("mandatory")
_CpsMc1800BiaIndex_Type = Integer32
_CpsMc1800BiaIndex_Object = MibTableColumn
cpsMc1800BiaIndex = _CpsMc1800BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 1, 1, 1),
    _CpsMc1800BiaIndex_Type()
)
cpsMc1800BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1800BiaIndex.setStatus("mandatory")
_CpsMc1800Description_Type = DisplayString
_CpsMc1800Description_Object = MibTableColumn
cpsMc1800Description = _CpsMc1800Description_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 1, 1, 2),
    _CpsMc1800Description_Type()
)
cpsMc1800Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1800Description.setStatus("mandatory")


class _CpsMc1800PSPower1_Type(Integer32):
    """Custom type cpsMc1800PSPower1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CpsMc1800PSPower1_Type.__name__ = "Integer32"
_CpsMc1800PSPower1_Object = MibTableColumn
cpsMc1800PSPower1 = _CpsMc1800PSPower1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 1, 1, 3),
    _CpsMc1800PSPower1_Type()
)
cpsMc1800PSPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1800PSPower1.setStatus("mandatory")


class _CpsMc1800PSInUse1_Type(Integer32):
    """Custom type cpsMc1800PSInUse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CpsMc1800PSInUse1_Type.__name__ = "Integer32"
_CpsMc1800PSInUse1_Object = MibTableColumn
cpsMc1800PSInUse1 = _CpsMc1800PSInUse1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 1, 1, 4),
    _CpsMc1800PSInUse1_Type()
)
cpsMc1800PSInUse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1800PSInUse1.setStatus("mandatory")


class _CpsMc1800PSPower2_Type(Integer32):
    """Custom type cpsMc1800PSPower2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CpsMc1800PSPower2_Type.__name__ = "Integer32"
_CpsMc1800PSPower2_Object = MibTableColumn
cpsMc1800PSPower2 = _CpsMc1800PSPower2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 1, 1, 5),
    _CpsMc1800PSPower2_Type()
)
cpsMc1800PSPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1800PSPower2.setStatus("mandatory")


class _CpsMc1800PSInUse2_Type(Integer32):
    """Custom type cpsMc1800PSInUse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CpsMc1800PSInUse2_Type.__name__ = "Integer32"
_CpsMc1800PSInUse2_Object = MibTableColumn
cpsMc1800PSInUse2 = _CpsMc1800PSInUse2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 1, 1, 6),
    _CpsMc1800PSInUse2_Type()
)
cpsMc1800PSInUse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1800PSInUse2.setStatus("mandatory")
_CpsMc1800MRevision_Type = Integer32
_CpsMc1800MRevision_Object = MibTableColumn
cpsMc1800MRevision = _CpsMc1800MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 1, 1, 7),
    _CpsMc1800MRevision_Type()
)
cpsMc1800MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1800MRevision.setStatus("mandatory")
_CpsMc1300Table_Object = MibTable
cpsMc1300Table = _CpsMc1300Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cpsMc1300Table.setStatus("mandatory")
_CpsMc1300Entry_Object = MibTableRow
cpsMc1300Entry = _CpsMc1300Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 2, 1)
)
cpsMc1300Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsMc1300BiaIndex"),
)
if mibBuilder.loadTexts:
    cpsMc1300Entry.setStatus("mandatory")
_CpsMc1300BiaIndex_Type = Integer32
_CpsMc1300BiaIndex_Object = MibTableColumn
cpsMc1300BiaIndex = _CpsMc1300BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 2, 1, 1),
    _CpsMc1300BiaIndex_Type()
)
cpsMc1300BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1300BiaIndex.setStatus("mandatory")
_CpsMc1300Description_Type = DisplayString
_CpsMc1300Description_Object = MibTableColumn
cpsMc1300Description = _CpsMc1300Description_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 2, 1, 2),
    _CpsMc1300Description_Type()
)
cpsMc1300Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1300Description.setStatus("mandatory")


class _CpsMc1300PSPower1_Type(Integer32):
    """Custom type cpsMc1300PSPower1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CpsMc1300PSPower1_Type.__name__ = "Integer32"
_CpsMc1300PSPower1_Object = MibTableColumn
cpsMc1300PSPower1 = _CpsMc1300PSPower1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 2, 1, 3),
    _CpsMc1300PSPower1_Type()
)
cpsMc1300PSPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1300PSPower1.setStatus("mandatory")


class _CpsMc1300PSInUse1_Type(Integer32):
    """Custom type cpsMc1300PSInUse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CpsMc1300PSInUse1_Type.__name__ = "Integer32"
_CpsMc1300PSInUse1_Object = MibTableColumn
cpsMc1300PSInUse1 = _CpsMc1300PSInUse1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 2, 1, 4),
    _CpsMc1300PSInUse1_Type()
)
cpsMc1300PSInUse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1300PSInUse1.setStatus("mandatory")


class _CpsMc1300PSPower2_Type(Integer32):
    """Custom type cpsMc1300PSPower2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CpsMc1300PSPower2_Type.__name__ = "Integer32"
_CpsMc1300PSPower2_Object = MibTableColumn
cpsMc1300PSPower2 = _CpsMc1300PSPower2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 2, 1, 5),
    _CpsMc1300PSPower2_Type()
)
cpsMc1300PSPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1300PSPower2.setStatus("mandatory")


class _CpsMc1300PSInUse2_Type(Integer32):
    """Custom type cpsMc1300PSInUse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CpsMc1300PSInUse2_Type.__name__ = "Integer32"
_CpsMc1300PSInUse2_Object = MibTableColumn
cpsMc1300PSInUse2 = _CpsMc1300PSInUse2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 2, 1, 6),
    _CpsMc1300PSInUse2_Type()
)
cpsMc1300PSInUse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1300PSInUse2.setStatus("mandatory")
_CpsMc1300MRevision_Type = Integer32
_CpsMc1300MRevision_Object = MibTableColumn
cpsMc1300MRevision = _CpsMc1300MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 2, 1, 7),
    _CpsMc1300MRevision_Type()
)
cpsMc1300MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1300MRevision.setStatus("mandatory")
_CpsMc0200Table_Object = MibTable
cpsMc0200Table = _CpsMc0200Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cpsMc0200Table.setStatus("mandatory")
_CpsMc0200Entry_Object = MibTableRow
cpsMc0200Entry = _CpsMc0200Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 3, 1)
)
cpsMc0200Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsMc0200BiaIndex"),
)
if mibBuilder.loadTexts:
    cpsMc0200Entry.setStatus("mandatory")
_CpsMc0200BiaIndex_Type = Integer32
_CpsMc0200BiaIndex_Object = MibTableColumn
cpsMc0200BiaIndex = _CpsMc0200BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 3, 1, 1),
    _CpsMc0200BiaIndex_Type()
)
cpsMc0200BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc0200BiaIndex.setStatus("mandatory")
_CpsMc0200Description_Type = DisplayString
_CpsMc0200Description_Object = MibTableColumn
cpsMc0200Description = _CpsMc0200Description_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 3, 1, 2),
    _CpsMc0200Description_Type()
)
cpsMc0200Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc0200Description.setStatus("mandatory")
_CpsMc0200MRevision_Type = Integer32
_CpsMc0200MRevision_Object = MibTableColumn
cpsMc0200MRevision = _CpsMc0200MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 3, 1, 3),
    _CpsMc0200MRevision_Type()
)
cpsMc0200MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc0200MRevision.setStatus("mandatory")
_CpsMc1900Table_Object = MibTable
cpsMc1900Table = _CpsMc1900Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cpsMc1900Table.setStatus("mandatory")
_CpsMc1900Entry_Object = MibTableRow
cpsMc1900Entry = _CpsMc1900Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 4, 1)
)
cpsMc1900Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsMc1900BiaIndex"),
)
if mibBuilder.loadTexts:
    cpsMc1900Entry.setStatus("mandatory")
_CpsMc1900BiaIndex_Type = Integer32
_CpsMc1900BiaIndex_Object = MibTableColumn
cpsMc1900BiaIndex = _CpsMc1900BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 4, 1, 1),
    _CpsMc1900BiaIndex_Type()
)
cpsMc1900BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1900BiaIndex.setStatus("mandatory")
_CpsMc1900Description_Type = DisplayString
_CpsMc1900Description_Object = MibTableColumn
cpsMc1900Description = _CpsMc1900Description_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 4, 1, 2),
    _CpsMc1900Description_Type()
)
cpsMc1900Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1900Description.setStatus("mandatory")
_CpsMc1900MRevision_Type = Integer32
_CpsMc1900MRevision_Object = MibTableColumn
cpsMc1900MRevision = _CpsMc1900MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 4, 1, 3),
    _CpsMc1900MRevision_Type()
)
cpsMc1900MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc1900MRevision.setStatus("mandatory")
_Smacf100Table_Object = MibTable
smacf100Table = _Smacf100Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5)
)
if mibBuilder.loadTexts:
    smacf100Table.setStatus("mandatory")
_Smacf100Entry_Object = MibTableRow
smacf100Entry = _Smacf100Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1)
)
smacf100Entry.setIndexNames(
    (0, "MCC16-MIB", "smacf100BiaIndex"),
)
if mibBuilder.loadTexts:
    smacf100Entry.setStatus("mandatory")
_Smacf100BiaIndex_Type = Integer32
_Smacf100BiaIndex_Object = MibTableColumn
smacf100BiaIndex = _Smacf100BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 1),
    _Smacf100BiaIndex_Type()
)
smacf100BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100BiaIndex.setStatus("mandatory")
_Smacf100Description_Type = DisplayString
_Smacf100Description_Object = MibTableColumn
smacf100Description = _Smacf100Description_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 2),
    _Smacf100Description_Type()
)
smacf100Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100Description.setStatus("mandatory")
_Smacf100MRevision_Type = Integer32
_Smacf100MRevision_Object = MibTableColumn
smacf100MRevision = _Smacf100MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 3),
    _Smacf100MRevision_Type()
)
smacf100MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100MRevision.setStatus("mandatory")


class _Smacf100SpanningTree_Type(Integer32):
    """Custom type smacf100SpanningTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Smacf100SpanningTree_Type.__name__ = "Integer32"
_Smacf100SpanningTree_Object = MibTableColumn
smacf100SpanningTree = _Smacf100SpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 4),
    _Smacf100SpanningTree_Type()
)
smacf100SpanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100SpanningTree.setStatus("mandatory")


class _Smacf100ResetCounters_Type(Integer32):
    """Custom type smacf100ResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 2),
          ("reset", 1))
    )


_Smacf100ResetCounters_Type.__name__ = "Integer32"
_Smacf100ResetCounters_Object = MibTableColumn
smacf100ResetCounters = _Smacf100ResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 5),
    _Smacf100ResetCounters_Type()
)
smacf100ResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100ResetCounters.setStatus("mandatory")


class _Smacf100SelfTest_Type(Integer32):
    """Custom type smacf100SelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 2),
          ("selfTest", 1))
    )


_Smacf100SelfTest_Type.__name__ = "Integer32"
_Smacf100SelfTest_Object = MibTableColumn
smacf100SelfTest = _Smacf100SelfTest_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 6),
    _Smacf100SelfTest_Type()
)
smacf100SelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100SelfTest.setStatus("mandatory")


class _Smacf100QosEnable_Type(Integer32):
    """Custom type smacf100QosEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_Smacf100QosEnable_Type.__name__ = "Integer32"
_Smacf100QosEnable_Object = MibTableColumn
smacf100QosEnable = _Smacf100QosEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 7),
    _Smacf100QosEnable_Type()
)
smacf100QosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100QosEnable.setStatus("mandatory")
_Smacf100QosHPThreshold_Type = Integer32
_Smacf100QosHPThreshold_Object = MibTableColumn
smacf100QosHPThreshold = _Smacf100QosHPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 8),
    _Smacf100QosHPThreshold_Type()
)
smacf100QosHPThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100QosHPThreshold.setStatus("mandatory")
_Smacf100QosLqWeight_Type = Integer32
_Smacf100QosLqWeight_Object = MibTableColumn
smacf100QosLqWeight = _Smacf100QosLqWeight_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 9),
    _Smacf100QosLqWeight_Type()
)
smacf100QosLqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100QosLqWeight.setStatus("mandatory")
_Smacf100QosHqWeight_Type = Integer32
_Smacf100QosHqWeight_Object = MibTableColumn
smacf100QosHqWeight = _Smacf100QosHqWeight_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 10),
    _Smacf100QosHqWeight_Type()
)
smacf100QosHqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100QosHqWeight.setStatus("mandatory")


class _Smacf100SNMPModuleInstalled_Type(Integer32):
    """Custom type smacf100SNMPModuleInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Smacf100SNMPModuleInstalled_Type.__name__ = "Integer32"
_Smacf100SNMPModuleInstalled_Object = MibTableColumn
smacf100SNMPModuleInstalled = _Smacf100SNMPModuleInstalled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 11),
    _Smacf100SNMPModuleInstalled_Type()
)
smacf100SNMPModuleInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smacf100SNMPModuleInstalled.setStatus("mandatory")
_Smacf100AgingTimer_Type = Integer32
_Smacf100AgingTimer_Object = MibTableColumn
smacf100AgingTimer = _Smacf100AgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 5, 1, 12),
    _Smacf100AgingTimer_Type()
)
smacf100AgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smacf100AgingTimer.setStatus("mandatory")
_CpsMc0800Table_Object = MibTable
cpsMc0800Table = _CpsMc0800Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    cpsMc0800Table.setStatus("mandatory")
_CpsMc0800Entry_Object = MibTableRow
cpsMc0800Entry = _CpsMc0800Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 6, 1)
)
cpsMc0800Entry.setIndexNames(
    (0, "MCC16-MIB", "cpsMc0800BiaIndex"),
)
if mibBuilder.loadTexts:
    cpsMc0800Entry.setStatus("mandatory")
_CpsMc0800BiaIndex_Type = Integer32
_CpsMc0800BiaIndex_Object = MibTableColumn
cpsMc0800BiaIndex = _CpsMc0800BiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 6, 1, 1),
    _CpsMc0800BiaIndex_Type()
)
cpsMc0800BiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc0800BiaIndex.setStatus("mandatory")
_CpsMc0800Description_Type = DisplayString
_CpsMc0800Description_Object = MibTableColumn
cpsMc0800Description = _CpsMc0800Description_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 6, 1, 2),
    _CpsMc0800Description_Type()
)
cpsMc0800Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc0800Description.setStatus("mandatory")
_CpsMc0800MRevision_Type = Integer32
_CpsMc0800MRevision_Object = MibTableColumn
cpsMc0800MRevision = _CpsMc0800MRevision_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 2, 6, 1, 3),
    _CpsMc0800MRevision_Type()
)
cpsMc0800MRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsMc0800MRevision.setStatus("mandatory")
_CpsAgent_ObjectIdentity = ObjectIdentity
cpsAgent = _CpsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 3)
)


class _CpsGroupCtrl_Type(DisplayString):
    """Custom type cpsGroupCtrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CpsGroupCtrl_Type.__name__ = "DisplayString"
_CpsGroupCtrl_Object = MibScalar
cpsGroupCtrl = _CpsGroupCtrl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 3, 1),
    _CpsGroupCtrl_Type()
)
cpsGroupCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsGroupCtrl.setStatus("mandatory")
_CpsSlotPwrTable_Object = MibTable
cpsSlotPwrTable = _CpsSlotPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cpsSlotPwrTable.setStatus("mandatory")
_CpsSlotPwrEntry_Object = MibTableRow
cpsSlotPwrEntry = _CpsSlotPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 3, 2, 1)
)
cpsSlotPwrEntry.setIndexNames(
    (0, "MCC16-MIB", "cpsSlotPwrBiaIndex"),
    (0, "MCC16-MIB", "cpsSlotPwrSlotIndex"),
)
if mibBuilder.loadTexts:
    cpsSlotPwrEntry.setStatus("mandatory")
_CpsSlotPwrBiaIndex_Type = Integer32
_CpsSlotPwrBiaIndex_Object = MibTableColumn
cpsSlotPwrBiaIndex = _CpsSlotPwrBiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 3, 2, 1, 1),
    _CpsSlotPwrBiaIndex_Type()
)
cpsSlotPwrBiaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsSlotPwrBiaIndex.setStatus("mandatory")
_CpsSlotPwrSlotIndex_Type = Integer32
_CpsSlotPwrSlotIndex_Object = MibTableColumn
cpsSlotPwrSlotIndex = _CpsSlotPwrSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 3, 2, 1, 2),
    _CpsSlotPwrSlotIndex_Type()
)
cpsSlotPwrSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsSlotPwrSlotIndex.setStatus("mandatory")


class _CpsSlotPwrState_Type(Integer32):
    """Custom type cpsSlotPwrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CpsSlotPwrState_Type.__name__ = "Integer32"
_CpsSlotPwrState_Object = MibTableColumn
cpsSlotPwrState = _CpsSlotPwrState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 3, 2, 1, 3),
    _CpsSlotPwrState_Type()
)
cpsSlotPwrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsSlotPwrState.setStatus("mandatory")


class _CpsIsPrimary_Type(Integer32):
    """Custom type cpsIsPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CpsIsPrimary_Type.__name__ = "Integer32"
_CpsIsPrimary_Object = MibScalar
cpsIsPrimary = _CpsIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 4, 2, 2, 3, 3),
    _CpsIsPrimary_Type()
)
cpsIsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsIsPrimary.setStatus("mandatory")

# Managed Objects groups


# Notification objects

pSError = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1, 0, 111)
)
if mibBuilder.loadTexts:
    pSError.setStatus(
        ""
    )

pSErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1, 0, 112)
)
if mibBuilder.loadTexts:
    pSErrorClear.setStatus(
        ""
    )

pSDeviceInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1, 0, 113)
)
if mibBuilder.loadTexts:
    pSDeviceInserted.setStatus(
        ""
    )

pSDeviceRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1, 0, 114)
)
if mibBuilder.loadTexts:
    pSDeviceRemoved.setStatus(
        ""
    )

pSDeviceColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1, 0, 115)
)
if mibBuilder.loadTexts:
    pSDeviceColdStart.setStatus(
        ""
    )

pSPowerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1, 0, 116)
)
if mibBuilder.loadTexts:
    pSPowerLost.setStatus(
        ""
    )

pSCabinetAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1, 0, 117)
)
if mibBuilder.loadTexts:
    pSCabinetAdded.setStatus(
        ""
    )

pSCabinetRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 1, 2, 1, 0, 118)
)
if mibBuilder.loadTexts:
    pSCabinetRemoved.setStatus(
        ""
    )

mcc16Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 2, 0, 101)
)
if mibBuilder.loadTexts:
    mcc16Error.setStatus(
        ""
    )

mcc16ErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 2, 0, 102)
)
if mibBuilder.loadTexts:
    mcc16ErrorClear.setStatus(
        ""
    )

mcc16PSState = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 1, 4, 2, 0, 103)
)
if mibBuilder.loadTexts:
    mcc16PSState.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MCC16-MIB",
    **{"MacAddress": MacAddress,
       "CpsConnector": CpsConnector,
       "transition": transition,
       "productId": productId,
       "chassisProdsId": chassisProdsId,
       "chassisSlotTypes": chassisSlotTypes,
       "chSlMc20p": chSlMc20p,
       "ceTbtFrl03Id": ceTbtFrl03Id,
       "ceCxTbt04Id": ceCxTbt04Id,
       "ceCxFrl04Id": ceCxFrl04Id,
       "cfSmMm02Id": cfSmMm02Id,
       "cfSmMm05Id": cfSmMm05Id,
       "caCf02Id": caCf02Id,
       "cfSmMm06Id": cfSmMm06Id,
       "ct1e1Cf01Id": ct1e1Cf01Id,
       "ceRTxFx01Id": ceRTxFx01Id,
       "ce100BtxFx04Id": ce100BtxFx04Id,
       "cpsCf01Id": cpsCf01Id,
       "cbCf01Id": cbCf01Id,
       "carCf01Id": carCf01Id,
       "carCf02Id": carCf02Id,
       "cePswFx03Id": cePswFx03Id,
       "cePswSx01Id": cePswSx01Id,
       "cRs232Cf01Id": cRs232Cf01Id,
       "cfSmMm04Id": cfSmMm04Id,
       "ce100BtxSx01Id": ce100BtxSx01Id,
       "ce100BtxFx04MtId": ce100BtxFx04MtId,
       "cfdCd01Id": cfdCd01Id,
       "ctrCf01Id": ctrCf01Id,
       "ce100BtxFrl03Id": ce100BtxFrl03Id,
       "mc20pEmptyId": mc20pEmptyId,
       "mc20pErrorId": mc20pErrorId,
       "mc20pDblWideId": mc20pDblWideId,
       "chstrCf01Id": chstrCf01Id,
       "ceTxSx02Id": ceTxSx02Id,
       "ceTbtFrl04Id": ceTbtFrl04Id,
       "chSlcps": chSlcps,
       "cpsmM100Id": cpsmM100Id,
       "pSError": pSError,
       "pSErrorClear": pSErrorClear,
       "pSDeviceInserted": pSDeviceInserted,
       "pSDeviceRemoved": pSDeviceRemoved,
       "pSDeviceColdStart": pSDeviceColdStart,
       "pSPowerLost": pSPowerLost,
       "pSCabinetAdded": pSCabinetAdded,
       "pSCabinetRemoved": pSCabinetRemoved,
       "cpsmM200Id": cpsmM200Id,
       "cettf100Id": cettf100Id,
       "cfetf100Id": cfetf100Id,
       "cfmff100Id": cfmff100Id,
       "cpsmp100Id": cpsmp100Id,
       "csetf100Id": csetf100Id,
       "cgetf100Id": cgetf100Id,
       "csdtf100Id": csdtf100Id,
       "cpsmp110Id": cpsmp110Id,
       "cbftf100Id": cbftf100Id,
       "cetct100Id": cetct100Id,
       "ccscf100Id": ccscf100Id,
       "cfetf105Id": cfetf105Id,
       "smacf100PId": smacf100PId,
       "cpsld100Id": cpsld100Id,
       "cdftf100Id": cdftf100Id,
       "cpsvt100Id": cpsvt100Id,
       "cemtf100Id": cemtf100Id,
       "captf100Id": captf100Id,
       "cfetf205Id": cfetf205Id,
       "cbftf150Id": cbftf150Id,
       "cgfeb100Id": cgfeb100Id,
       "crmfe100Id": crmfe100Id,
       "crs2f100Id": crs2f100Id,
       "crs4f100Id": crs4f100Id,
       "cmefg100Id": cmefg100Id,
       "cpsEmptyId": cpsEmptyId,
       "cpsDblWideId": cpsDblWideId,
       "cpsUnknownDeviceId": cpsUnknownDeviceId,
       "chassisMcc16Id": chassisMcc16Id,
       "mcc16Error": mcc16Error,
       "mcc16ErrorClear": mcc16ErrorClear,
       "mcc16PSState": mcc16PSState,
       "chassisCpsmc1800Id": chassisCpsmc1800Id,
       "chassisCpsmc1850Id": chassisCpsmc1850Id,
       "chassisCpsmc0800Id": chassisCpsmc0800Id,
       "chassisCpsmc1300Id": chassisCpsmc1300Id,
       "chassisCpsmc0200Id": chassisCpsmc0200Id,
       "chassisSmacf100LCId": chassisSmacf100LCId,
       "chassisCpsmc1900Id": chassisCpsmc1900Id,
       "chassisSmacf100Id": chassisSmacf100Id,
       "products": products,
       "chassis": chassis,
       "card": card,
       "slotMc20p": slotMc20p,
       "ceTbtFrl03Table": ceTbtFrl03Table,
       "ceTbtFrl03Entry": ceTbtFrl03Entry,
       "ceTbtFrl03Index": ceTbtFrl03Index,
       "ceTbtFrl03FiberRecv": ceTbtFrl03FiberRecv,
       "ceTbtFrl03FiberLink": ceTbtFrl03FiberLink,
       "ceTbtFrl03TPRecv": ceTbtFrl03TPRecv,
       "ceTbtFrl03TPLink": ceTbtFrl03TPLink,
       "ceTbtFrl03Power": ceTbtFrl03Power,
       "ceCxTbt04Table": ceCxTbt04Table,
       "ceCxTbt04Entry": ceCxTbt04Entry,
       "ceCxTbt04Index": ceCxTbt04Index,
       "ceCxTbt04Jabber": ceCxTbt04Jabber,
       "ceCxTbt04CoaxRecv": ceCxTbt04CoaxRecv,
       "ceCxTbt04TPRecv": ceCxTbt04TPRecv,
       "ceCxTbt04TPLink": ceCxTbt04TPLink,
       "ceCxTbt04Power": ceCxTbt04Power,
       "ceCxFrl04Table": ceCxFrl04Table,
       "ceCxFrl04Entry": ceCxFrl04Entry,
       "ceCxFrl04Index": ceCxFrl04Index,
       "ceCxFrl04Jabber": ceCxFrl04Jabber,
       "ceCxFrl04CoaxRecv": ceCxFrl04CoaxRecv,
       "ceCxFrl04FLRecv": ceCxFrl04FLRecv,
       "ceCxFrl04FLLink": ceCxFrl04FLLink,
       "ceCxFrl04Power": ceCxFrl04Power,
       "cfSmMm02Table": cfSmMm02Table,
       "cfSmMm02Entry": cfSmMm02Entry,
       "cfSmMm02Index": cfSmMm02Index,
       "cfSmMm02MMSignalDetect": cfSmMm02MMSignalDetect,
       "cfSmMm02SMSignalDetect": cfSmMm02SMSignalDetect,
       "cfSmMm02Power": cfSmMm02Power,
       "cfSmMm05Table": cfSmMm05Table,
       "cfSmMm05Entry": cfSmMm05Entry,
       "cfSmMm05Index": cfSmMm05Index,
       "cfSmMm05SMSignalDetect": cfSmMm05SMSignalDetect,
       "cfSmMm05MMSignalDetect": cfSmMm05MMSignalDetect,
       "cfSmMm05Power": cfSmMm05Power,
       "caCf02Table": caCf02Table,
       "caCf02Entry": caCf02Entry,
       "caCf02Index": caCf02Index,
       "caCf02CopperSignalDetect": caCf02CopperSignalDetect,
       "caCf02FiberSignalDetect": caCf02FiberSignalDetect,
       "caCf02Power": caCf02Power,
       "cfSmMm06Table": cfSmMm06Table,
       "cfSmMm06Entry": cfSmMm06Entry,
       "cfSmMm06Index": cfSmMm06Index,
       "cfSmMm06MMSignalDetect": cfSmMm06MMSignalDetect,
       "cfSmMm06SMSignalDetect": cfSmMm06SMSignalDetect,
       "cfSmMm06Power": cfSmMm06Power,
       "ct1e1Cf01Table": ct1e1Cf01Table,
       "ct1e1Cf01Entry": ct1e1Cf01Entry,
       "ct1e1Cf01Index": ct1e1Cf01Index,
       "ct1e1Cf01CopperSignalDetect": ct1e1Cf01CopperSignalDetect,
       "ct1e1Cf01FiberSignalDetect": ct1e1Cf01FiberSignalDetect,
       "ct1e1Cf01CoaxActive": ct1e1Cf01CoaxActive,
       "ceRTxFx01Table": ceRTxFx01Table,
       "ceRTxFx01Entry": ceRTxFx01Entry,
       "ceRTxFx01Index": ceRTxFx01Index,
       "ceRTxFx01TPPrimary": ceRTxFx01TPPrimary,
       "ceRTxFx01FiberPrimary": ceRTxFx01FiberPrimary,
       "ceRTxFx01TPSignalDetect": ceRTxFx01TPSignalDetect,
       "ceRTxFx01FiberSignalDetect": ceRTxFx01FiberSignalDetect,
       "ce100BtxFx04Table": ce100BtxFx04Table,
       "ce100BtxFx04Entry": ce100BtxFx04Entry,
       "ce100BtxFx04Index": ce100BtxFx04Index,
       "ce100BtxFx04TPRecv": ce100BtxFx04TPRecv,
       "ce100BtxFx04FiberRecv": ce100BtxFx04FiberRecv,
       "ce100BtxFx04TPSignalDetect": ce100BtxFx04TPSignalDetect,
       "ce100BtxFx04FiberSignalDetect": ce100BtxFx04FiberSignalDetect,
       "ce100BtxFx04Power": ce100BtxFx04Power,
       "cpsCf01Table": cpsCf01Table,
       "cpsCf01Entry": cpsCf01Entry,
       "cpsCf01Index": cpsCf01Index,
       "cpsCf01FiberRecv": cpsCf01FiberRecv,
       "cpsCf01TPRecv": cpsCf01TPRecv,
       "cpsCf01Power": cpsCf01Power,
       "cbCf01Table": cbCf01Table,
       "cbCf01Entry": cbCf01Entry,
       "cbCf01Index": cbCf01Index,
       "cbCf01FiberRecv": cbCf01FiberRecv,
       "cbCf01TPCoaxRecv": cbCf01TPCoaxRecv,
       "cbCf01Power": cbCf01Power,
       "carCf01Table": carCf01Table,
       "carCf01Entry": carCf01Entry,
       "carCf01Index": carCf01Index,
       "carCf01FiberRecv": carCf01FiberRecv,
       "carCf01TPRecv": carCf01TPRecv,
       "carCf01Power": carCf01Power,
       "carCf02Table": carCf02Table,
       "carCf02Entry": carCf02Entry,
       "carCf02Index": carCf02Index,
       "carCf02FiberRecv": carCf02FiberRecv,
       "carCf02CoaxRecv": carCf02CoaxRecv,
       "carCf02Power": carCf02Power,
       "cePswFx03Table": cePswFx03Table,
       "cePswFx03Entry": cePswFx03Entry,
       "cePswFx03Index": cePswFx03Index,
       "cePswFx03TPFullDuplex": cePswFx03TPFullDuplex,
       "cePswFx03FiberFullDuplex": cePswFx03FiberFullDuplex,
       "cePswFx03TPLink": cePswFx03TPLink,
       "cePswFx03FiberLink": cePswFx03FiberLink,
       "cePswFx03TP100Mbps": cePswFx03TP100Mbps,
       "cePswSx01Table": cePswSx01Table,
       "cePswSx01Entry": cePswSx01Entry,
       "cePswSx01Index": cePswSx01Index,
       "cePswSx01TPFullDuplex": cePswSx01TPFullDuplex,
       "cePswSx01FiberFullDuplex": cePswSx01FiberFullDuplex,
       "cePswSx01TPLink": cePswSx01TPLink,
       "cePswSx01FiberLink": cePswSx01FiberLink,
       "cePswSx01TP100Mbps": cePswSx01TP100Mbps,
       "cRs232Cf01Table": cRs232Cf01Table,
       "cRs232Cf01Entry": cRs232Cf01Entry,
       "cRs232Cf01Index": cRs232Cf01Index,
       "cRs232Cf01FiberLock": cRs232Cf01FiberLock,
       "cfSmMm04Table": cfSmMm04Table,
       "cfSmMm04Entry": cfSmMm04Entry,
       "cfSmMm04Index": cfSmMm04Index,
       "cfSmMm04MMSignalDetect": cfSmMm04MMSignalDetect,
       "cfSmMm04SMSignalDetect": cfSmMm04SMSignalDetect,
       "cfSmMm04Power": cfSmMm04Power,
       "ce100BtxSx01Table": ce100BtxSx01Table,
       "ce100BtxSx01Entry": ce100BtxSx01Entry,
       "ce100BtxSx01Index": ce100BtxSx01Index,
       "ce100BtxSx01TPRecv": ce100BtxSx01TPRecv,
       "ce100BtxSx01FiberRecv": ce100BtxSx01FiberRecv,
       "ce100BtxSx01TPSignalDetect": ce100BtxSx01TPSignalDetect,
       "ce100BtxSx01FiberSignalDetect": ce100BtxSx01FiberSignalDetect,
       "ce100BtxSx01Power": ce100BtxSx01Power,
       "ce100BtxFx04MtTable": ce100BtxFx04MtTable,
       "ce100BtxFx04MtEntry": ce100BtxFx04MtEntry,
       "ce100BtxFx04MtIndex": ce100BtxFx04MtIndex,
       "ce100BtxFx04MtTPRecv": ce100BtxFx04MtTPRecv,
       "ce100BtxFx04MtFiberRecv": ce100BtxFx04MtFiberRecv,
       "ce100BtxFx04MtTPSignalDetect": ce100BtxFx04MtTPSignalDetect,
       "ce100BtxFx04MtFiberSignalDetect": ce100BtxFx04MtFiberSignalDetect,
       "ce100BtxFx04MtPower": ce100BtxFx04MtPower,
       "cfdCd01Table": cfdCd01Table,
       "cfdCd01Entry": cfdCd01Entry,
       "cfdCd01Index": cfdCd01Index,
       "cfdCd01Lock": cfdCd01Lock,
       "cfdCd01TPRecv": cfdCd01TPRecv,
       "cfdCd01FiberRecv": cfdCd01FiberRecv,
       "cfdCd01TPSignalDetect": cfdCd01TPSignalDetect,
       "cfdCd01FiberSignalDetect": cfdCd01FiberSignalDetect,
       "ctrCf01Table": ctrCf01Table,
       "ctrCf01Entry": ctrCf01Entry,
       "ctrCf01Index": ctrCf01Index,
       "ctrCf01FiberinOK": ctrCf01FiberinOK,
       "ctrCf01TPinOK": ctrCf01TPinOK,
       "ctrCf01Inserted": ctrCf01Inserted,
       "ce100BtxFrl03Table": ce100BtxFrl03Table,
       "ce100BtxFrl03Entry": ce100BtxFrl03Entry,
       "ce100BtxFrl03Index": ce100BtxFrl03Index,
       "ce100BtxFrl03Lock": ce100BtxFrl03Lock,
       "ce100BtxFrl03TPRecv": ce100BtxFrl03TPRecv,
       "ce100BtxFrl03FiberRecv": ce100BtxFrl03FiberRecv,
       "ce100BtxFrl03TPSignalDetect": ce100BtxFrl03TPSignalDetect,
       "ce100BtxFrl03FiberSignalDetect": ce100BtxFrl03FiberSignalDetect,
       "chstrCf01Table": chstrCf01Table,
       "chstrCf01Entry": chstrCf01Entry,
       "chstrCf01Index": chstrCf01Index,
       "chstrCf01TPRecv": chstrCf01TPRecv,
       "chstrCf01FiberRecv": chstrCf01FiberRecv,
       "chstrCf01TPSignalDetect": chstrCf01TPSignalDetect,
       "chstrCf01FiberSignalDetect": chstrCf01FiberSignalDetect,
       "ceTxSx02Table": ceTxSx02Table,
       "ceTxSx02Entry": ceTxSx02Entry,
       "ceTxSx02Index": ceTxSx02Index,
       "ceTxSx02TPLink": ceTxSx02TPLink,
       "ceTxSx02FiberLink": ceTxSx02FiberLink,
       "ceTxSx02100Mbps": ceTxSx02100Mbps,
       "ceTbtFrl04Table": ceTbtFrl04Table,
       "ceTbtFrl04Entry": ceTbtFrl04Entry,
       "ceTbtFrl04Index": ceTbtFrl04Index,
       "ceTbtFrl04FiberRecv": ceTbtFrl04FiberRecv,
       "ceTbtFrl04FiberLink": ceTbtFrl04FiberLink,
       "ceTbtFrl04TPRecv": ceTbtFrl04TPRecv,
       "ceTbtFrl04TPLink": ceTbtFrl04TPLink,
       "slotCps": slotCps,
       "cpsSlotSummary": cpsSlotSummary,
       "cpsModuleTable": cpsModuleTable,
       "cpsModuleEntry": cpsModuleEntry,
       "cpsModuleBiaIndex": cpsModuleBiaIndex,
       "cpsModuleSlotIndex": cpsModuleSlotIndex,
       "cpsModuleModel": cpsModuleModel,
       "cpsSlotDetail": cpsSlotDetail,
       "cpsmm100Table": cpsmm100Table,
       "cpsmm100Entry": cpsmm100Entry,
       "cpsmm100BiaIndex": cpsmm100BiaIndex,
       "cpsmm100SlotIndex": cpsmm100SlotIndex,
       "cpsmm100Groups": cpsmm100Groups,
       "cpsmm100Reset": cpsmm100Reset,
       "cpsmm100SaveConfig": cpsmm100SaveConfig,
       "cpsmm100HwRevision": cpsmm100HwRevision,
       "cpsmm100SwRevision": cpsmm100SwRevision,
       "cpsmm100IPAddress": cpsmm100IPAddress,
       "cpsmm100SubnetMask": cpsmm100SubnetMask,
       "cpsmm100Gateway": cpsmm100Gateway,
       "cpsmm100IsPrimary": cpsmm100IsPrimary,
       "cpsmm100WantPrimary": cpsmm100WantPrimary,
       "cpsmm100CanPrimary": cpsmm100CanPrimary,
       "cpsmm100EthernetLink": cpsmm100EthernetLink,
       "cpsmm100TntRIP": cpsmm100TntRIP,
       "cpsmm100TntRIPMask": cpsmm100TntRIPMask,
       "cpsmm100SNMPTrapMgr": cpsmm100SNMPTrapMgr,
       "cpsmm100SNMPTrapInterval": cpsmm100SNMPTrapInterval,
       "cpsmm100SysUpTime": cpsmm100SysUpTime,
       "cpsmm100SysContact": cpsmm100SysContact,
       "cpsmm100SysName": cpsmm100SysName,
       "cpsmm100SysLocation": cpsmm100SysLocation,
       "cpsmm100CfgMatch": cpsmm100CfgMatch,
       "cpsmm100SerialNumber": cpsmm100SerialNumber,
       "cpsmm100ICIF": cpsmm100ICIF,
       "cpsmm100MRevision": cpsmm100MRevision,
       "cpsmm100LastGasp": cpsmm100LastGasp,
       "cpsmm100SNMPTrapMgr2": cpsmm100SNMPTrapMgr2,
       "cpsmm100SNMPTrapMgr3": cpsmm100SNMPTrapMgr3,
       "cpsmm100SNMPTrapMgr4": cpsmm100SNMPTrapMgr4,
       "cpsmm100CacheClean": cpsmm100CacheClean,
       "cpsmm200Table": cpsmm200Table,
       "cpsmm200Entry": cpsmm200Entry,
       "cpsmm200BiaIndex": cpsmm200BiaIndex,
       "cpsmm200SlotIndex": cpsmm200SlotIndex,
       "cpsmm200SerialNumber": cpsmm200SerialNumber,
       "cpsmm200ICIF": cpsmm200ICIF,
       "cpsmm200MRevision": cpsmm200MRevision,
       "cettf100Table": cettf100Table,
       "cettf100Entry": cettf100Entry,
       "cettf100BiaIndex": cettf100BiaIndex,
       "cettf100SlotIndex": cettf100SlotIndex,
       "cettf100Groups": cettf100Groups,
       "cettf100MRevision": cettf100MRevision,
       "cettf100CfgMatch": cettf100CfgMatch,
       "cettf100SerialNumber": cettf100SerialNumber,
       "cettf100ConnA": cettf100ConnA,
       "cettf100ConnB": cettf100ConnB,
       "cettf100TPLink": cettf100TPLink,
       "cettf100FiberLink": cettf100FiberLink,
       "cettf100Fault": cettf100Fault,
       "cettf100TPActivity": cettf100TPActivity,
       "cettf100FiberActivity": cettf100FiberActivity,
       "cettf100AutoCross": cettf100AutoCross,
       "cettf100LinkPassThrough": cettf100LinkPassThrough,
       "cettf100ConfigMode": cettf100ConfigMode,
       "cettf100Enabled": cettf100Enabled,
       "cettf100CacheClean": cettf100CacheClean,
       "cfetf100Table": cfetf100Table,
       "cfetf100Entry": cfetf100Entry,
       "cfetf100BiaIndex": cfetf100BiaIndex,
       "cfetf100SlotIndex": cfetf100SlotIndex,
       "cfetf100Groups": cfetf100Groups,
       "cfetf100MRevision": cfetf100MRevision,
       "cfetf100CfgMatch": cfetf100CfgMatch,
       "cfetf100SerialNumber": cfetf100SerialNumber,
       "cfetf100ConnA": cfetf100ConnA,
       "cfetf100ConnB": cfetf100ConnB,
       "cfetf100TPLink": cfetf100TPLink,
       "cfetf100FiberLink": cfetf100FiberLink,
       "cfetf100Fault": cfetf100Fault,
       "cfetf100FastLinkPulse": cfetf100FastLinkPulse,
       "cfetf100Enabled": cfetf100Enabled,
       "cfetf100Pause": cfetf100Pause,
       "cfetf100LinkPassThrough": cfetf100LinkPassThrough,
       "cfetf100AutoCross": cfetf100AutoCross,
       "cfetf100TPActivity": cfetf100TPActivity,
       "cfetf100FiberActivity": cfetf100FiberActivity,
       "cfetf100ConfigMode": cfetf100ConfigMode,
       "cfetf100FarEndFault": cfetf100FarEndFault,
       "cfetf100CacheClean": cfetf100CacheClean,
       "cfmff100Table": cfmff100Table,
       "cfmff100Entry": cfmff100Entry,
       "cfmff100BiaIndex": cfmff100BiaIndex,
       "cfmff100SlotIndex": cfmff100SlotIndex,
       "cfmff100Groups": cfmff100Groups,
       "cfmff100MRevision": cfmff100MRevision,
       "cfmff100CfgMatch": cfmff100CfgMatch,
       "cfmff100ConnA": cfmff100ConnA,
       "cfmff100ConnB": cfmff100ConnB,
       "cfmff100SerialNumber": cfmff100SerialNumber,
       "cfmff100SMSignal": cfmff100SMSignal,
       "cfmff100MMSignal": cfmff100MMSignal,
       "cfmff100Enabled": cfmff100Enabled,
       "cfmff100PortShutOff": cfmff100PortShutOff,
       "cfmff100ConfigMode": cfmff100ConfigMode,
       "cfmff100CacheClean": cfmff100CacheClean,
       "cpsmp100Table": cpsmp100Table,
       "cpsmp100Entry": cpsmp100Entry,
       "cpsmp100BiaIndex": cpsmp100BiaIndex,
       "cpsmp100SlotIndex": cpsmp100SlotIndex,
       "cpsmp100Groups": cpsmp100Groups,
       "cpsmp100MRevision": cpsmp100MRevision,
       "cpsmp100CfgMatch": cpsmp100CfgMatch,
       "cpsmp100SerialNumber": cpsmp100SerialNumber,
       "cpsmp100Mode": cpsmp100Mode,
       "cpsmp100ConfigMode": cpsmp100ConfigMode,
       "cpsmp100RemoteFan": cpsmp100RemoteFan,
       "cpsmp100PowerOK": cpsmp100PowerOK,
       "cpsmp100InUse": cpsmp100InUse,
       "cpsmp100ChassisPower": cpsmp100ChassisPower,
       "cpsmp100ChassisTemp": cpsmp100ChassisTemp,
       "cpsmp100RFanFault": cpsmp100RFanFault,
       "cpsmp100LFanFault": cpsmp100LFanFault,
       "cpsmp100SupplyType": cpsmp100SupplyType,
       "cpsmp100CacheClean": cpsmp100CacheClean,
       "csetf100Table": csetf100Table,
       "csetf100Entry": csetf100Entry,
       "csetf100BiaIndex": csetf100BiaIndex,
       "csetf100SlotIndex": csetf100SlotIndex,
       "csetf100Groups": csetf100Groups,
       "csetf100MRevision": csetf100MRevision,
       "csetf100CfgMatch": csetf100CfgMatch,
       "csetf100SerialNumber": csetf100SerialNumber,
       "csetf100ConnA": csetf100ConnA,
       "csetf100ConnB": csetf100ConnB,
       "csetf100TPLink": csetf100TPLink,
       "csetf100FiberLink": csetf100FiberLink,
       "csetf100AutoCross": csetf100AutoCross,
       "csetf100SpeedConfig": csetf100SpeedConfig,
       "csetf100Speed100Mbps": csetf100Speed100Mbps,
       "csetf100TPActivity": csetf100TPActivity,
       "csetf100FiberActivity": csetf100FiberActivity,
       "csetf100ConfigMode": csetf100ConfigMode,
       "csetf100CacheClean": csetf100CacheClean,
       "cgetf100Table": cgetf100Table,
       "cgetf100Entry": cgetf100Entry,
       "cgetf100BiaIndex": cgetf100BiaIndex,
       "cgetf100SlotIndex": cgetf100SlotIndex,
       "cgetf100Groups": cgetf100Groups,
       "cgetf100MRevision": cgetf100MRevision,
       "cgetf100CfgMatch": cgetf100CfgMatch,
       "cgetf100SerialNumber": cgetf100SerialNumber,
       "cgetf100ConnA": cgetf100ConnA,
       "cgetf100ConnB": cgetf100ConnB,
       "cgetf100TPLink": cgetf100TPLink,
       "cgetf100FiberLink": cgetf100FiberLink,
       "cgetf100Fault": cgetf100Fault,
       "cgetf100Enabled": cgetf100Enabled,
       "cgetf100Pause": cgetf100Pause,
       "cgetf100LinkPassThrough": cgetf100LinkPassThrough,
       "cgetf100FullDuplex": cgetf100FullDuplex,
       "cgetf100ClockMaster": cgetf100ClockMaster,
       "cgetf100ConfigMode": cgetf100ConfigMode,
       "cgetf100TPLength": cgetf100TPLength,
       "cgetf100FiberAutoNegot": cgetf100FiberAutoNegot,
       "cgetf100CacheClean": cgetf100CacheClean,
       "cgetf100PauseType": cgetf100PauseType,
       "csdtf100Table": csdtf100Table,
       "csdtf100Entry": csdtf100Entry,
       "csdtf100BiaIndex": csdtf100BiaIndex,
       "csdtf100SlotIndex": csdtf100SlotIndex,
       "csdtf100Groups": csdtf100Groups,
       "csdtf100MRevision": csdtf100MRevision,
       "csdtf100CfgMatch": csdtf100CfgMatch,
       "csdtf100SerialNumber": csdtf100SerialNumber,
       "csdtf100ConnA": csdtf100ConnA,
       "csdtf100ConnB": csdtf100ConnB,
       "csdtf100CopperLink": csdtf100CopperLink,
       "csdtf100FiberLink": csdtf100FiberLink,
       "csdtf100Fault": csdtf100Fault,
       "csdtf100TAOSFiber": csdtf100TAOSFiber,
       "csdtf100TAOSCopper": csdtf100TAOSCopper,
       "csdtf100AISFiber": csdtf100AISFiber,
       "csdtf100AISCopper": csdtf100AISCopper,
       "csdtf100CopperLoopback": csdtf100CopperLoopback,
       "csdtf100CopperLongHaul": csdtf100CopperLongHaul,
       "csdtf100T1E1": csdtf100T1E1,
       "csdtf100ConfigMode": csdtf100ConfigMode,
       "csdtf100TPCoax": csdtf100TPCoax,
       "csdtf100CopperLineBuildout": csdtf100CopperLineBuildout,
       "csdtf100FiberLoopback": csdtf100FiberLoopback,
       "csdtf100RmtSupported": csdtf100RmtSupported,
       "csdtf100RmtDetected": csdtf100RmtDetected,
       "csdtf100RmtMRevision": csdtf100RmtMRevision,
       "csdtf100RmtSerialNumber": csdtf100RmtSerialNumber,
       "csdtf100RmtConnA": csdtf100RmtConnA,
       "csdtf100RmtConnB": csdtf100RmtConnB,
       "csdtf100RmtCopperLink": csdtf100RmtCopperLink,
       "csdtf100RmtFiberLink": csdtf100RmtFiberLink,
       "csdtf100RmtFault": csdtf100RmtFault,
       "csdtf100RmtTAOSFiber": csdtf100RmtTAOSFiber,
       "csdtf100RmtTAOSCopper": csdtf100RmtTAOSCopper,
       "csdtf100RmtAISFiber": csdtf100RmtAISFiber,
       "csdtf100RmtAISCopper": csdtf100RmtAISCopper,
       "csdtf100RmtCopperLoopback": csdtf100RmtCopperLoopback,
       "csdtf100RmtCopperLongHaul": csdtf100RmtCopperLongHaul,
       "csdtf100RmtConfigMode": csdtf100RmtConfigMode,
       "csdtf100RmtTPCoax": csdtf100RmtTPCoax,
       "csdtf100RmtCopperLineBuildout": csdtf100RmtCopperLineBuildout,
       "csdtf100RmtFiberLoopback": csdtf100RmtFiberLoopback,
       "csdtf100CacheClean": csdtf100CacheClean,
       "cpsmp110Table": cpsmp110Table,
       "cpsmp110Entry": cpsmp110Entry,
       "cpsmp110SubDeviceIndex": cpsmp110SubDeviceIndex,
       "cpsmp110BiaIndex": cpsmp110BiaIndex,
       "cpsmp110SlotIndex": cpsmp110SlotIndex,
       "cpsmp110Groups": cpsmp110Groups,
       "cpsmp110MRevision": cpsmp110MRevision,
       "cpsmp110CfgMatch": cpsmp110CfgMatch,
       "cpsmp110SerialNumber": cpsmp110SerialNumber,
       "cpsmp110ConfigMode": cpsmp110ConfigMode,
       "cpsmp110MasterTempFault": cpsmp110MasterTempFault,
       "cpsmp110MasterCurrentFault": cpsmp110MasterCurrentFault,
       "cpsmp110MasterFanFault": cpsmp110MasterFanFault,
       "cpsmp110FirmwareRevision": cpsmp110FirmwareRevision,
       "cpsmp110PSSupplyTbl": cpsmp110PSSupplyTbl,
       "cpsmp110PSRoleTbl": cpsmp110PSRoleTbl,
       "cpsmp110PSReadyTbl": cpsmp110PSReadyTbl,
       "cpsmp110PSInUseTbl": cpsmp110PSInUseTbl,
       "cpsmp110TemperatureTbl": cpsmp110TemperatureTbl,
       "cpsmp110CurrentTbl": cpsmp110CurrentTbl,
       "cpsmp110FanStatusTbl": cpsmp110FanStatusTbl,
       "cpsmp110TempFaultTbl": cpsmp110TempFaultTbl,
       "cpsmp110CurrFaultTbl": cpsmp110CurrFaultTbl,
       "cpsmp110PSCount": cpsmp110PSCount,
       "cpsmp110TempSensorCount": cpsmp110TempSensorCount,
       "cpsmp110CurrSensorCount": cpsmp110CurrSensorCount,
       "cpsmp110FanCount": cpsmp110FanCount,
       "cpsmp110CacheClean": cpsmp110CacheClean,
       "cbftf100Table": cbftf100Table,
       "cbftf100Entry": cbftf100Entry,
       "cbftf100SubDeviceIndex": cbftf100SubDeviceIndex,
       "cbftf100BiaIndex": cbftf100BiaIndex,
       "cbftf100SlotIndex": cbftf100SlotIndex,
       "cbftf100Groups": cbftf100Groups,
       "cbftf100MRevision": cbftf100MRevision,
       "cbftf100CfgMatch": cbftf100CfgMatch,
       "cbftf100SerialNumber": cbftf100SerialNumber,
       "cbftf100ConfigMode": cbftf100ConfigMode,
       "cbftf100FirmwareRevision": cbftf100FirmwareRevision,
       "cbftf100SelfTestFailed": cbftf100SelfTestFailed,
       "cbftf100SpanningTree": cbftf100SpanningTree,
       "cbftf100MirrorCfg": cbftf100MirrorCfg,
       "cbftf100SACMasterCfg": cbftf100SACMasterCfg,
       "cbftf100FormFactor": cbftf100FormFactor,
       "cbftf100AutoNegotTbl": cbftf100AutoNegotTbl,
       "cbftf100FullDuplexTbl": cbftf100FullDuplexTbl,
       "cbftf100100MbpsTbl": cbftf100100MbpsTbl,
       "cbftf100Adv10HDXTbl": cbftf100Adv10HDXTbl,
       "cbftf100Adv10FDXTbl": cbftf100Adv10FDXTbl,
       "cbftf100Adv100HDXTbl": cbftf100Adv100HDXTbl,
       "cbftf100Adv100FDXTbl": cbftf100Adv100FDXTbl,
       "cbftf100CrossTbl": cbftf100CrossTbl,
       "cbftf100PauseCfgTbl": cbftf100PauseCfgTbl,
       "cbftf100PauseStatTbl": cbftf100PauseStatTbl,
       "cbftf100FarEndFaultTbl": cbftf100FarEndFaultTbl,
       "cbftf100ConnectorTbl": cbftf100ConnectorTbl,
       "cbftf100SACCfgTbl": cbftf100SACCfgTbl,
       "cbftf100SACStatTbl": cbftf100SACStatTbl,
       "cbftf100MirrorSelTbl": cbftf100MirrorSelTbl,
       "cbftf100MirrorInTbl": cbftf100MirrorInTbl,
       "cbftf100MirrorOutTbl": cbftf100MirrorOutTbl,
       "cbftf100LinkTbl": cbftf100LinkTbl,
       "cbftf100PortCount": cbftf100PortCount,
       "cbftf100LinkPassThrough": cbftf100LinkPassThrough,
       "cbftf100CacheClean": cbftf100CacheClean,
       "cbftf100RedundantPath": cbftf100RedundantPath,
       "cetct100Table": cetct100Table,
       "cetct100Entry": cetct100Entry,
       "cetct100BiaIndex": cetct100BiaIndex,
       "cetct100SlotIndex": cetct100SlotIndex,
       "cetct100Groups": cetct100Groups,
       "cetct100MRevision": cetct100MRevision,
       "cetct100CfgMatch": cetct100CfgMatch,
       "cetct100SerialNumber": cetct100SerialNumber,
       "cetct100ConfigMode": cetct100ConfigMode,
       "cetct100FirmwareRevision": cetct100FirmwareRevision,
       "cetct100TPLink": cetct100TPLink,
       "cetct100Collision": cetct100Collision,
       "cetct100CoaxActivity": cetct100CoaxActivity,
       "cetct100TPActivity": cetct100TPActivity,
       "cetct100CollisionsPerMinute": cetct100CollisionsPerMinute,
       "cetct100CollisionsPerHour": cetct100CollisionsPerHour,
       "cetct100ConnA": cetct100ConnA,
       "cetct100ConnB": cetct100ConnB,
       "cetct100CacheClean": cetct100CacheClean,
       "ccscf100Table": ccscf100Table,
       "ccscf100Entry": ccscf100Entry,
       "ccscf100BiaIndex": ccscf100BiaIndex,
       "ccscf100SlotIndex": ccscf100SlotIndex,
       "ccscf100Groups": ccscf100Groups,
       "ccscf100MRevision": ccscf100MRevision,
       "ccscf100CfgMatch": ccscf100CfgMatch,
       "ccscf100SerialNumber": ccscf100SerialNumber,
       "ccscf100ConfigMode": ccscf100ConfigMode,
       "ccscf100FiberLink": ccscf100FiberLink,
       "ccscf100CopperLink": ccscf100CopperLink,
       "ccscf100AISFiber": ccscf100AISFiber,
       "ccscf100AISCopper": ccscf100AISCopper,
       "ccscf100DS3LineBuildout": ccscf100DS3LineBuildout,
       "ccscf100E3DS3": ccscf100E3DS3,
       "ccscf100CopperLoopback": ccscf100CopperLoopback,
       "ccscf100FiberLoopback": ccscf100FiberLoopback,
       "ccscf100ConnA": ccscf100ConnA,
       "ccscf100ConnB": ccscf100ConnB,
       "ccscf100CacheClean": ccscf100CacheClean,
       "cfetf105Table": cfetf105Table,
       "cfetf105Entry": cfetf105Entry,
       "cfetf105BiaIndex": cfetf105BiaIndex,
       "cfetf105SlotIndex": cfetf105SlotIndex,
       "cfetf105Groups": cfetf105Groups,
       "cfetf105MRevision": cfetf105MRevision,
       "cfetf105CfgMatch": cfetf105CfgMatch,
       "cfetf105SerialNumber": cfetf105SerialNumber,
       "cfetf105ConnA": cfetf105ConnA,
       "cfetf105ConnB": cfetf105ConnB,
       "cfetf105TPLink": cfetf105TPLink,
       "cfetf105FiberLink": cfetf105FiberLink,
       "cfetf105AutoNegot": cfetf105AutoNegot,
       "cfetf105LinkPassThrough": cfetf105LinkPassThrough,
       "cfetf105AutoCross": cfetf105AutoCross,
       "cfetf105TPActivity": cfetf105TPActivity,
       "cfetf105FiberActivity": cfetf105FiberActivity,
       "cfetf105ConfigMode": cfetf105ConfigMode,
       "cfetf105CacheClean": cfetf105CacheClean,
       "smacf100PTable": smacf100PTable,
       "smacf100PEntry": smacf100PEntry,
       "smacf100PSubDeviceIndex": smacf100PSubDeviceIndex,
       "smacf100PBiaIndex": smacf100PBiaIndex,
       "smacf100PSlotIndex": smacf100PSlotIndex,
       "smacf100PGroups": smacf100PGroups,
       "smacf100PCfgMatch": smacf100PCfgMatch,
       "smacf100PConnA": smacf100PConnA,
       "smacf100PLink": smacf100PLink,
       "smacf100P100Mbps": smacf100P100Mbps,
       "smacf100PFullDuplex": smacf100PFullDuplex,
       "smacf100PSACStat": smacf100PSACStat,
       "smacf100PEnabled": smacf100PEnabled,
       "smacf100PAutoNegot": smacf100PAutoNegot,
       "smacf100PAdv10HDX": smacf100PAdv10HDX,
       "smacf100PAdv10FDX": smacf100PAdv10FDX,
       "smacf100PAdv100HDX": smacf100PAdv100HDX,
       "smacf100PAdv100FDX": smacf100PAdv100FDX,
       "smacf100PSTPState": smacf100PSTPState,
       "smacf100PLastMAC": smacf100PLastMAC,
       "smacf100PFarEndFaultCfg": smacf100PFarEndFaultCfg,
       "smacf100PFarEndFaultStat": smacf100PFarEndFaultStat,
       "smacf100PTxOctets": smacf100PTxOctets,
       "smacf100PWrapTxOctets": smacf100PWrapTxOctets,
       "smacf100PRxOctets": smacf100PRxOctets,
       "smacf100PWrapRxOctets": smacf100PWrapRxOctets,
       "smacf100PSACCfg": smacf100PSACCfg,
       "smacf100PBlockMgmt": smacf100PBlockMgmt,
       "smacf100PBlockPort": smacf100PBlockPort,
       "smacf100PTxDropPkts": smacf100PTxDropPkts,
       "smacf100PTxBroadcastPkts": smacf100PTxBroadcastPkts,
       "smacf100PTxMulticastPkts": smacf100PTxMulticastPkts,
       "smacf100PTxUnicastPkts": smacf100PTxUnicastPkts,
       "smacf100PTxCollisions": smacf100PTxCollisions,
       "smacf100PTxSingleCollision": smacf100PTxSingleCollision,
       "smacf100PTxMultipleCollision": smacf100PTxMultipleCollision,
       "smacf100PTxDeferredTransmit": smacf100PTxDeferredTransmit,
       "smacf100PTxLateCollision": smacf100PTxLateCollision,
       "smacf100PTxExcessiveCollision": smacf100PTxExcessiveCollision,
       "smacf100PTxFrameInDisc": smacf100PTxFrameInDisc,
       "smacf100PTxPausePkts": smacf100PTxPausePkts,
       "smacf100PRxUndersizePkts": smacf100PRxUndersizePkts,
       "smacf100PRxPausePkts": smacf100PRxPausePkts,
       "smacf100PPkts64Octets": smacf100PPkts64Octets,
       "smacf100PPkts65to127Octets": smacf100PPkts65to127Octets,
       "smacf100PPkts128to255Octets": smacf100PPkts128to255Octets,
       "smacf100PPkts256to511Octets": smacf100PPkts256to511Octets,
       "smacf100PPkts512to1023Octets": smacf100PPkts512to1023Octets,
       "smacf100PPkts1024to1522Octets": smacf100PPkts1024to1522Octets,
       "smacf100PRxOversizePkts": smacf100PRxOversizePkts,
       "smacf100PRxJabbers": smacf100PRxJabbers,
       "smacf100PRxAlignmentErrors": smacf100PRxAlignmentErrors,
       "smacf100PRxFCSErrors": smacf100PRxFCSErrors,
       "smacf100PRxGoodOctets": smacf100PRxGoodOctets,
       "smacf100PWrapRxGoodOctets": smacf100PWrapRxGoodOctets,
       "smacf100PRxDropPkts": smacf100PRxDropPkts,
       "smacf100PRxUnicastPkts": smacf100PRxUnicastPkts,
       "smacf100PRxMulticastPkts": smacf100PRxMulticastPkts,
       "smacf100PRxBroadcastPkts": smacf100PRxBroadcastPkts,
       "smacf100PRxSAChanges": smacf100PRxSAChanges,
       "smacf100PRxFragments": smacf100PRxFragments,
       "smacf100PRxExcessSizeDisc": smacf100PRxExcessSizeDisc,
       "smacf100PRxSymbolError": smacf100PRxSymbolError,
       "smacf100PQosPriority": smacf100PQosPriority,
       "smacf100PQosPause": smacf100PQosPause,
       "smacf100PAdvPause": smacf100PAdvPause,
       "smacf100PCacheClean": smacf100PCacheClean,
       "cpsld100Table": cpsld100Table,
       "cpsld100Entry": cpsld100Entry,
       "cpsld100BiaIndex": cpsld100BiaIndex,
       "cpsld100SlotIndex": cpsld100SlotIndex,
       "cpsld100SerialNumber": cpsld100SerialNumber,
       "cpsld100MRevision": cpsld100MRevision,
       "cpsld100Ps1Power": cpsld100Ps1Power,
       "cpsld100Ps1InUse": cpsld100Ps1InUse,
       "cpsld100Ps2Power": cpsld100Ps2Power,
       "cpsld100Ps2InUse": cpsld100Ps2InUse,
       "cdftf100Table": cdftf100Table,
       "cdftf100Entry": cdftf100Entry,
       "cdftf100SubDeviceIndex": cdftf100SubDeviceIndex,
       "cdftf100BiaIndex": cdftf100BiaIndex,
       "cdftf100SlotIndex": cdftf100SlotIndex,
       "cdftf100Groups": cdftf100Groups,
       "cdftf100CfgMatch": cdftf100CfgMatch,
       "cdftf100SerialNumber": cdftf100SerialNumber,
       "cdftf100MRevision": cdftf100MRevision,
       "cdftf100TPLinkTbl": cdftf100TPLinkTbl,
       "cdftf100FiberLinkTbl": cdftf100FiberLinkTbl,
       "cdftf100TPActivityTbl": cdftf100TPActivityTbl,
       "cdftf100FiberActivityTbl": cdftf100FiberActivityTbl,
       "cdftf100ConnectorTbl": cdftf100ConnectorTbl,
       "cdftf100FirmwareRevision": cdftf100FirmwareRevision,
       "cdftf100CacheClean": cdftf100CacheClean,
       "cpsvt100Table": cpsvt100Table,
       "cpsvt100Entry": cpsvt100Entry,
       "cpsvt100BiaIndex": cpsvt100BiaIndex,
       "cpsvt100SlotIndex": cpsvt100SlotIndex,
       "cpsvt100Groups": cpsvt100Groups,
       "cpsvt100MRevision": cpsvt100MRevision,
       "cpsvt100CfgMatch": cpsvt100CfgMatch,
       "cpsvt100SerialNumber": cpsvt100SerialNumber,
       "cpsvt100FiberLink": cpsvt100FiberLink,
       "cpsvt100CopperLink": cpsvt100CopperLink,
       "cpsvt100Fault": cpsvt100Fault,
       "cpsvt100ConnA": cpsvt100ConnA,
       "cpsvt100ConnB": cpsvt100ConnB,
       "cpsvt100TermTiming": cpsvt100TermTiming,
       "cpsvt100LoopBack": cpsvt100LoopBack,
       "cpsvt100CableMode": cpsvt100CableMode,
       "cpsvt100DCE": cpsvt100DCE,
       "cpsvt100InvertTX": cpsvt100InvertTX,
       "cpsvt100InvertRX": cpsvt100InvertRX,
       "cpsvt100ConfigMode": cpsvt100ConfigMode,
       "cpsvt100FirmwareRev": cpsvt100FirmwareRev,
       "cpsvt100RmtDetected": cpsvt100RmtDetected,
       "cpsvt100RmtTermTiming": cpsvt100RmtTermTiming,
       "cpsvt100RmtLoopBack": cpsvt100RmtLoopBack,
       "cpsvt100RmtCableMode": cpsvt100RmtCableMode,
       "cpsvt100RmtDCE": cpsvt100RmtDCE,
       "cpsvt100RmtInvertTX": cpsvt100RmtInvertTX,
       "cpsvt100RmtInvertRX": cpsvt100RmtInvertRX,
       "cpsvt100RmtConfigMode": cpsvt100RmtConfigMode,
       "cpsvt100RmtFirmwareRev": cpsvt100RmtFirmwareRev,
       "cpsvt100RmtCopperLink": cpsvt100RmtCopperLink,
       "cpsvt100RmtFiberLink": cpsvt100RmtFiberLink,
       "cpsvt100CacheClean": cpsvt100CacheClean,
       "cemtf100Table": cemtf100Table,
       "cemtf100Entry": cemtf100Entry,
       "cemtf100BiaIndex": cemtf100BiaIndex,
       "cemtf100SlotIndex": cemtf100SlotIndex,
       "cemtf100Groups": cemtf100Groups,
       "cemtf100MRevision": cemtf100MRevision,
       "cemtf100CfgMatch": cemtf100CfgMatch,
       "cemtf100SerialNumber": cemtf100SerialNumber,
       "cemtf100FiberLink": cemtf100FiberLink,
       "cemtf100OffHook": cemtf100OffHook,
       "cemtf100Fault": cemtf100Fault,
       "cemtf100ConnA": cemtf100ConnA,
       "cemtf100ConnB": cemtf100ConnB,
       "cemtf100CacheClean": cemtf100CacheClean,
       "captf100Table": captf100Table,
       "captf100Entry": captf100Entry,
       "captf100BiaIndex": captf100BiaIndex,
       "captf100SlotIndex": captf100SlotIndex,
       "captf100Groups": captf100Groups,
       "captf100MRevision": captf100MRevision,
       "captf100CfgMatch": captf100CfgMatch,
       "captf100SerialNumber": captf100SerialNumber,
       "captf100FiberLink": captf100FiberLink,
       "captf100InUse": captf100InUse,
       "captf100Fault": captf100Fault,
       "captf100ConnA": captf100ConnA,
       "captf100ConnB": captf100ConnB,
       "captf100FirmwareRev": captf100FirmwareRev,
       "captf100CacheClean": captf100CacheClean,
       "captf100Emulates": captf100Emulates,
       "cfetf205Table": cfetf205Table,
       "cfetf205Entry": cfetf205Entry,
       "cfetf205BiaIndex": cfetf205BiaIndex,
       "cfetf205SlotIndex": cfetf205SlotIndex,
       "cfetf205Groups": cfetf205Groups,
       "cfetf205MRevision": cfetf205MRevision,
       "cfetf205CfgMatch": cfetf205CfgMatch,
       "cfetf205SerialNumber": cfetf205SerialNumber,
       "cfetf205ConnA": cfetf205ConnA,
       "cfetf205ConnB": cfetf205ConnB,
       "cfetf205TPLink": cfetf205TPLink,
       "cfetf205FiberLink": cfetf205FiberLink,
       "cfetf205Fault": cfetf205Fault,
       "cfetf205FastLinkPulse": cfetf205FastLinkPulse,
       "cfetf205Enabled": cfetf205Enabled,
       "cfetf205Pause": cfetf205Pause,
       "cfetf205LinkPassThrough": cfetf205LinkPassThrough,
       "cfetf205AutoCross": cfetf205AutoCross,
       "cfetf205TPActivity": cfetf205TPActivity,
       "cfetf205FiberActivity": cfetf205FiberActivity,
       "cfetf205ConfigMode": cfetf205ConfigMode,
       "cfetf205FarEndFault": cfetf205FarEndFault,
       "cfetf205CacheClean": cfetf205CacheClean,
       "cbftf150Table": cbftf150Table,
       "cbftf150Entry": cbftf150Entry,
       "cbftf150SubDeviceIndex": cbftf150SubDeviceIndex,
       "cbftf150BiaIndex": cbftf150BiaIndex,
       "cbftf150SlotIndex": cbftf150SlotIndex,
       "cbftf150Groups": cbftf150Groups,
       "cbftf150MRevision": cbftf150MRevision,
       "cbftf150CfgMatch": cbftf150CfgMatch,
       "cbftf150SerialNumber": cbftf150SerialNumber,
       "cbftf150ConfigMode": cbftf150ConfigMode,
       "cbftf150FirmwareRevision": cbftf150FirmwareRevision,
       "cbftf150FormFactor": cbftf150FormFactor,
       "cbftf150AutoNegotTbl": cbftf150AutoNegotTbl,
       "cbftf150FullDuplexTbl": cbftf150FullDuplexTbl,
       "cbftf150100MbpsTbl": cbftf150100MbpsTbl,
       "cbftf150CrossTbl": cbftf150CrossTbl,
       "cbftf150FarEndFaultTbl": cbftf150FarEndFaultTbl,
       "cbftf150ConnectorTbl": cbftf150ConnectorTbl,
       "cbftf150LinkTbl": cbftf150LinkTbl,
       "cbftf150PortCount": cbftf150PortCount,
       "cbftf150CacheClean": cbftf150CacheClean,
       "cgfeb100Table": cgfeb100Table,
       "cgfeb100Entry": cgfeb100Entry,
       "cgfeb100BiaIndex": cgfeb100BiaIndex,
       "cgfeb100SlotIndex": cgfeb100SlotIndex,
       "cgfeb100Groups": cgfeb100Groups,
       "cgfeb100MRevision": cgfeb100MRevision,
       "cgfeb100CfgMatch": cgfeb100CfgMatch,
       "cgfeb100SerialNumber": cgfeb100SerialNumber,
       "cgfeb100ConfigMode": cgfeb100ConfigMode,
       "cgfeb100FirmwareRevision": cgfeb100FirmwareRevision,
       "cgfeb100SelfTestFailed": cgfeb100SelfTestFailed,
       "cgfeb100MonitorType": cgfeb100MonitorType,
       "cgfeb100LinkPassThrough": cgfeb100LinkPassThrough,
       "cgfeb100QosEnabled": cgfeb100QosEnabled,
       "cgfeb100QosHPThreshold": cgfeb100QosHPThreshold,
       "cgfeb100QosLqWeight": cgfeb100QosLqWeight,
       "cgfeb100QosHqWeight": cgfeb100QosHqWeight,
       "cgfeb100ConnA": cgfeb100ConnA,
       "cgfeb100TPLink": cgfeb100TPLink,
       "cgfeb100TPSpeedCfg": cgfeb100TPSpeedCfg,
       "cgfeb100TPSpeedStat": cgfeb100TPSpeedStat,
       "cgfeb100TPFullDuplexCfg": cgfeb100TPFullDuplexCfg,
       "cgfeb100TPFullDuplexStat": cgfeb100TPFullDuplexStat,
       "cgfeb100TPCrossCfg": cgfeb100TPCrossCfg,
       "cgfeb100TPCrossStat": cgfeb100TPCrossStat,
       "cgfeb100TPAutoNegot": cgfeb100TPAutoNegot,
       "cgfeb100TPAdv10HDX": cgfeb100TPAdv10HDX,
       "cgfeb100TPAdv10FDX": cgfeb100TPAdv10FDX,
       "cgfeb100TPAdv100HDX": cgfeb100TPAdv100HDX,
       "cgfeb100TPAdv100FDX": cgfeb100TPAdv100FDX,
       "cgfeb100TPAdv1000HDX": cgfeb100TPAdv1000HDX,
       "cgfeb100TPAdv1000FDX": cgfeb100TPAdv1000FDX,
       "cgfeb100TPLpAdvPause": cgfeb100TPLpAdvPause,
       "cgfeb100TPLpAdv10HDX": cgfeb100TPLpAdv10HDX,
       "cgfeb100TPLpAdv10FDX": cgfeb100TPLpAdv10FDX,
       "cgfeb100TPLpAdv100HDX": cgfeb100TPLpAdv100HDX,
       "cgfeb100TPLpAdv100FDX": cgfeb100TPLpAdv100FDX,
       "cgfeb100TPLpAdv1000HDX": cgfeb100TPLpAdv1000HDX,
       "cgfeb100TPLpAdv1000FDX": cgfeb100TPLpAdv1000FDX,
       "cgfeb100TPAdvPause": cgfeb100TPAdvPause,
       "cgfeb100TPQosPause": cgfeb100TPQosPause,
       "cgfeb100TPSacCfg": cgfeb100TPSacCfg,
       "cgfeb100TPSacStat": cgfeb100TPSacStat,
       "cgfeb100ConnB": cgfeb100ConnB,
       "cgfeb100FiberLink": cgfeb100FiberLink,
       "cgfeb100FiberFullDuplexCfg": cgfeb100FiberFullDuplexCfg,
       "cgfeb100FiberFullDuplexStat": cgfeb100FiberFullDuplexStat,
       "cgfeb100FiberAutoNegot": cgfeb100FiberAutoNegot,
       "cgfeb100FiberAdv1000HDX": cgfeb100FiberAdv1000HDX,
       "cgfeb100FiberAdv1000FDX": cgfeb100FiberAdv1000FDX,
       "cgfeb100FiberLpAdv1000HDX": cgfeb100FiberLpAdv1000HDX,
       "cgfeb100FiberLpAdv1000FDX": cgfeb100FiberLpAdv1000FDX,
       "cgfeb100FiberLpAdvPause": cgfeb100FiberLpAdvPause,
       "cgfeb100FiberAdvPause": cgfeb100FiberAdvPause,
       "cgfeb100FiberQosPause": cgfeb100FiberQosPause,
       "cgfeb100FiberSacCfg": cgfeb100FiberSacCfg,
       "cgfeb100FiberSacStat": cgfeb100FiberSacStat,
       "cgfeb100MonitorTap": cgfeb100MonitorTap,
       "cgfeb100CacheClean": cgfeb100CacheClean,
       "crmfe100Table": crmfe100Table,
       "crmfe100Entry": crmfe100Entry,
       "crmfe100BiaIndex": crmfe100BiaIndex,
       "crmfe100SlotIndex": crmfe100SlotIndex,
       "crmfe100Groups": crmfe100Groups,
       "crmfe100MRevision": crmfe100MRevision,
       "crmfe100CfgMatch": crmfe100CfgMatch,
       "crmfe100SerialNumber": crmfe100SerialNumber,
       "crmfe100ConnA": crmfe100ConnA,
       "crmfe100ConnB": crmfe100ConnB,
       "crmfe100TPLink": crmfe100TPLink,
       "crmfe100FiberLink": crmfe100FiberLink,
       "crmfe100Fault": crmfe100Fault,
       "crmfe100Autonegot": crmfe100Autonegot,
       "crmfe100Enabled": crmfe100Enabled,
       "crmfe100Pause": crmfe100Pause,
       "crmfe100LinkPassThrough": crmfe100LinkPassThrough,
       "crmfe100AutoCross": crmfe100AutoCross,
       "crmfe100TPActivity": crmfe100TPActivity,
       "crmfe100FiberActivity": crmfe100FiberActivity,
       "crmfe100ConfigMode": crmfe100ConfigMode,
       "crmfe100FarEndFault": crmfe100FarEndFault,
       "crmfe100NetworkMode": crmfe100NetworkMode,
       "crmfe100UpTime": crmfe100UpTime,
       "crmfe100FirmwareRevision": crmfe100FirmwareRevision,
       "crmfe100RmtDetected": crmfe100RmtDetected,
       "crmfe100RmtTPLink": crmfe100RmtTPLink,
       "crmfe100RmtFiberLink": crmfe100RmtFiberLink,
       "crmfe100RmtFault": crmfe100RmtFault,
       "crmfe100RmtAutonegot": crmfe100RmtAutonegot,
       "crmfe100RmtPause": crmfe100RmtPause,
       "crmfe100RmtLinkPassThrough": crmfe100RmtLinkPassThrough,
       "crmfe100RmtAutoCross": crmfe100RmtAutoCross,
       "crmfe100RmtTPActivity": crmfe100RmtTPActivity,
       "crmfe100RmtFiberActivity": crmfe100RmtFiberActivity,
       "crmfe100RmtConfigMode": crmfe100RmtConfigMode,
       "crmfe100RmtFarEndFault": crmfe100RmtFarEndFault,
       "crmfe100RmtLoopback": crmfe100RmtLoopback,
       "crmfe100RmtNetworkMode": crmfe100RmtNetworkMode,
       "crmfe100RmtUpTime": crmfe100RmtUpTime,
       "crmfe100TxFxBwa": crmfe100TxFxBwa,
       "crmfe100FxTxBwa": crmfe100FxTxBwa,
       "crmfe100TxBytesH": crmfe100TxBytesH,
       "crmfe100TxBytesL": crmfe100TxBytesL,
       "crmfe100FxBytesH": crmfe100FxBytesH,
       "crmfe100FxBytesL": crmfe100FxBytesL,
       "crmfe100MscRxBytes": crmfe100MscRxBytes,
       "crmfe100MscTxBytes": crmfe100MscTxBytes,
       "crmfe100CacheClean": crmfe100CacheClean,
       "crmfe100MbTxFxBwa": crmfe100MbTxFxBwa,
       "crmfe100MbFxTxBwa": crmfe100MbFxTxBwa,
       "crs2f100Table": crs2f100Table,
       "crs2f100Entry": crs2f100Entry,
       "crs2f100BiaIndex": crs2f100BiaIndex,
       "crs2f100SlotIndex": crs2f100SlotIndex,
       "crs2f100Groups": crs2f100Groups,
       "crs2f100MRevision": crs2f100MRevision,
       "crs2f100CfgMatch": crs2f100CfgMatch,
       "crs2f100SerialNumber": crs2f100SerialNumber,
       "crs2f100ConnA": crs2f100ConnA,
       "crs2f100ConnB": crs2f100ConnB,
       "crs2f100FiberLink": crs2f100FiberLink,
       "crs2f100Fault": crs2f100Fault,
       "crs2f100FirmwareRevision": crs2f100FirmwareRevision,
       "crs2f100Loopback": crs2f100Loopback,
       "crs2f100DCE": crs2f100DCE,
       "crs2f100CopperActivity": crs2f100CopperActivity,
       "crs2f100ConfigMode": crs2f100ConfigMode,
       "crs2f100RmtDetected": crs2f100RmtDetected,
       "crs2f100RmtLoopback": crs2f100RmtLoopback,
       "crs2f100RmtDCE": crs2f100RmtDCE,
       "crs2f100RmtCopperActivity": crs2f100RmtCopperActivity,
       "crs2f100RmtConfigMode": crs2f100RmtConfigMode,
       "crs2f100CacheClean": crs2f100CacheClean,
       "crs4f100Table": crs4f100Table,
       "crs4f100Entry": crs4f100Entry,
       "crs4f100BiaIndex": crs4f100BiaIndex,
       "crs4f100SlotIndex": crs4f100SlotIndex,
       "crs4f100Groups": crs4f100Groups,
       "crs4f100MRevision": crs4f100MRevision,
       "crs4f100CfgMatch": crs4f100CfgMatch,
       "crs4f100SerialNumber": crs4f100SerialNumber,
       "crs4f100ConnA": crs4f100ConnA,
       "crs4f100ConnB": crs4f100ConnB,
       "crs4f100FiberLink": crs4f100FiberLink,
       "crs4f100Fault": crs4f100Fault,
       "crs4f100FirmwareRevision": crs4f100FirmwareRevision,
       "crs4f100CopperActivity": crs4f100CopperActivity,
       "crs4f100CacheClean": crs4f100CacheClean,
       "cmefg100Table": cmefg100Table,
       "cmefg100Entry": cmefg100Entry,
       "cmefg100SubDeviceIndex": cmefg100SubDeviceIndex,
       "cmefg100BiaIndex": cmefg100BiaIndex,
       "cmefg100SlotIndex": cmefg100SlotIndex,
       "cmefg100Groups": cmefg100Groups,
       "cmefg100MRevision": cmefg100MRevision,
       "cmefg100CfgMatch": cmefg100CfgMatch,
       "cmefg100ImcLocEnable": cmefg100ImcLocEnable,
       "cmefg100ImcLocReset": cmefg100ImcLocReset,
       "cmefg100ImcRmtEnable": cmefg100ImcRmtEnable,
       "cmefg100ImcRmtReset": cmefg100ImcRmtReset,
       "cmefg100ImcRxAlignmentErrorsTbl": cmefg100ImcRxAlignmentErrorsTbl,
       "cmefg100ImcRxBroadcastPktsTbl": cmefg100ImcRxBroadcastPktsTbl,
       "cmefg100ImcRxDropPktsTbl": cmefg100ImcRxDropPktsTbl,
       "cmefg100ImcRxExcessSizeDiscTbl": cmefg100ImcRxExcessSizeDiscTbl,
       "cmefg100ImcRxFCSErrorsTbl": cmefg100ImcRxFCSErrorsTbl,
       "cmefg100ImcRxFragmentsTbl": cmefg100ImcRxFragmentsTbl,
       "cmefg100ImcRxGoodOctetsTbl": cmefg100ImcRxGoodOctetsTbl,
       "cmefg100ImcRxGoodOctetsWrapTbl": cmefg100ImcRxGoodOctetsWrapTbl,
       "cmefg100ImcRxJabbersTbl": cmefg100ImcRxJabbersTbl,
       "cmefg100ImcRxMulticastPktsTbl": cmefg100ImcRxMulticastPktsTbl,
       "cmefg100ImcRxOctetsTbl": cmefg100ImcRxOctetsTbl,
       "cmefg100ImcRxOctetsWrapTbl": cmefg100ImcRxOctetsWrapTbl,
       "cmefg100ImcRxOversizePktsTbl": cmefg100ImcRxOversizePktsTbl,
       "cmefg100ImcRxPausePktsTbl": cmefg100ImcRxPausePktsTbl,
       "cmefg100ImcRxPkts1024to1522OctetsTbl": cmefg100ImcRxPkts1024to1522OctetsTbl,
       "cmefg100ImcRxPkts128to255OctetsTbl": cmefg100ImcRxPkts128to255OctetsTbl,
       "cmefg100ImcRxPkts256to511OctetsTbl": cmefg100ImcRxPkts256to511OctetsTbl,
       "cmefg100ImcRxPkts512to1023OctetsTbl": cmefg100ImcRxPkts512to1023OctetsTbl,
       "cmefg100ImcRxPkts64OctetsTbl": cmefg100ImcRxPkts64OctetsTbl,
       "cmefg100ImcRxPkts65to127OctetsTbl": cmefg100ImcRxPkts65to127OctetsTbl,
       "cmefg100ImcRxQosOctetsTbl": cmefg100ImcRxQosOctetsTbl,
       "cmefg100ImcRxQosOctetsWrapTbl": cmefg100ImcRxQosOctetsWrapTbl,
       "cmefg100ImcRxQosPktsTbl": cmefg100ImcRxQosPktsTbl,
       "cmefg100ImcRxSAChangesTbl": cmefg100ImcRxSAChangesTbl,
       "cmefg100ImcRxSymbolErrorTbl": cmefg100ImcRxSymbolErrorTbl,
       "cmefg100ImcRxUndersizePktsTbl": cmefg100ImcRxUndersizePktsTbl,
       "cmefg100ImcRxUnicastPktsTbl": cmefg100ImcRxUnicastPktsTbl,
       "cmefg100ImcTxBroadcastPktsTbl": cmefg100ImcTxBroadcastPktsTbl,
       "cmefg100ImcTxCollisionsTbl": cmefg100ImcTxCollisionsTbl,
       "cmefg100ImcTxDeferredTransmitTbl": cmefg100ImcTxDeferredTransmitTbl,
       "cmefg100ImcTxDropPktsTbl": cmefg100ImcTxDropPktsTbl,
       "cmefg100ImcTxExcessiveCollisionTbl": cmefg100ImcTxExcessiveCollisionTbl,
       "cmefg100ImcTxFrameInDiscTbl": cmefg100ImcTxFrameInDiscTbl,
       "cmefg100ImcTxLateCollisionTbl": cmefg100ImcTxLateCollisionTbl,
       "cmefg100ImcTxMulticastPktsTbl": cmefg100ImcTxMulticastPktsTbl,
       "cmefg100ImcTxMultipleCollisionTbl": cmefg100ImcTxMultipleCollisionTbl,
       "cmefg100ImcTxOctetsTbl": cmefg100ImcTxOctetsTbl,
       "cmefg100ImcTxOctetsWrapTbl": cmefg100ImcTxOctetsWrapTbl,
       "cmefg100ImcTxPausePktsTbl": cmefg100ImcTxPausePktsTbl,
       "cmefg100ImcTxQosOctetsTbl": cmefg100ImcTxQosOctetsTbl,
       "cmefg100ImcTxQosOctetsWrapTbl": cmefg100ImcTxQosOctetsWrapTbl,
       "cmefg100ImcTxQosPktsTbl": cmefg100ImcTxQosPktsTbl,
       "cmefg100ImcTxSingleCollisionTbl": cmefg100ImcTxSingleCollisionTbl,
       "cmefg100ImcTxUnicastPktsTbl": cmefg100ImcTxUnicastPktsTbl,
       "cmefg100LadCacheCmd": cmefg100LadCacheCmd,
       "cmefg100LadCacheState": cmefg100LadCacheState,
       "cmefg100LadEditCmd": cmefg100LadEditCmd,
       "cmefg100LadEditMac": cmefg100LadEditMac,
       "cmefg100LadEditPort": cmefg100LadEditPort,
       "cmefg100LadEditVid": cmefg100LadEditVid,
       "cmefg100LadEntries": cmefg100LadEntries,
       "cmefg100LadMacTbl": cmefg100LadMacTbl,
       "cmefg100LadPortTbl": cmefg100LadPortTbl,
       "cmefg100LadStaticTbl": cmefg100LadStaticTbl,
       "cmefg100LadVidTbl": cmefg100LadVidTbl,
       "cmefg100LocColdstart": cmefg100LocColdstart,
       "cmefg100LocDmiRxPower": cmefg100LocDmiRxPower,
       "cmefg100LocDmiRxPowerAlarm": cmefg100LocDmiRxPowerAlarm,
       "cmefg100LocDmiTemp": cmefg100LocDmiTemp,
       "cmefg100LocDmiTempAlarm": cmefg100LocDmiTempAlarm,
       "cmefg100LocDmiTxBiasAlarm": cmefg100LocDmiTxBiasAlarm,
       "cmefg100LocDmiTxBiasCurrent": cmefg100LocDmiTxBiasCurrent,
       "cmefg100LocDmiTxPower": cmefg100LocDmiTxPower,
       "cmefg100LocDmiTxPowerAlarm": cmefg100LocDmiTxPowerAlarm,
       "cmefg100LocFiberAdv1000FDX": cmefg100LocFiberAdv1000FDX,
       "cmefg100LocFiberAdv1000HDX": cmefg100LocFiberAdv1000HDX,
       "cmefg100LocFiberAutoNegot": cmefg100LocFiberAutoNegot,
       "cmefg100LocFiberConnA": cmefg100LocFiberConnA,
       "cmefg100LocFiberDuplex": cmefg100LocFiberDuplex,
       "cmefg100LocFiberLink": cmefg100LocFiberLink,
       "cmefg100LocFiberPause": cmefg100LocFiberPause,
       "cmefg100LocFiberQosPause": cmefg100LocFiberQosPause,
       "cmefg100LocFiberSacEnable": cmefg100LocFiberSacEnable,
       "cmefg100LocFiberSacStatus": cmefg100LocFiberSacStatus,
       "cmefg100LocFirmwareRevision": cmefg100LocFirmwareRevision,
       "cmefg100LocFpgaRev": cmefg100LocFpgaRev,
       "cmefg100LocFxTxBwaKb": cmefg100LocFxTxBwaKb,
       "cmefg100LocFxTxBwaMb": cmefg100LocFxTxBwaMb,
       "cmefg100LocOamActiveMode": cmefg100LocOamActiveMode,
       "cmefg100LocOamAdminControl": cmefg100LocOamAdminControl,
       "cmefg100LocOamConfigRevision": cmefg100LocOamConfigRevision,
       "cmefg100LocOamControlInUnknownOpcodes": cmefg100LocOamControlInUnknownOpcodes,
       "cmefg100LocOamCriticalEvent": cmefg100LocOamCriticalEvent,
       "cmefg100LocOamDuplicateEventNotificationRx": cmefg100LocOamDuplicateEventNotificationRx,
       "cmefg100LocOamFramesLostDueToOamError": cmefg100LocOamFramesLostDueToOamError,
       "cmefg100LocOamInformationRx": cmefg100LocOamInformationRx,
       "cmefg100LocOamInformationTx": cmefg100LocOamInformationTx,
       "cmefg100LocOamLastGasp": cmefg100LocOamLastGasp,
       "cmefg100LocOamLinkEvents": cmefg100LocOamLinkEvents,
       "cmefg100LocOamLinkFault": cmefg100LocOamLinkFault,
       "cmefg100LocOamLocDteDisc": cmefg100LocOamLocDteDisc,
       "cmefg100LocOamLoopbackControlRx": cmefg100LocOamLoopbackControlRx,
       "cmefg100LocOamLoopbackControlTx": cmefg100LocOamLoopbackControlTx,
       "cmefg100LocOamMacAddress": cmefg100LocOamMacAddress,
       "cmefg100LocOamMaxOamPduSize": cmefg100LocOamMaxOamPduSize,
       "cmefg100LocOamMultiplexorState": cmefg100LocOamMultiplexorState,
       "cmefg100LocOamOperStatus": cmefg100LocOamOperStatus,
       "cmefg100LocOamOrgSpecificRx": cmefg100LocOamOrgSpecificRx,
       "cmefg100LocOamOrgSpecificTx": cmefg100LocOamOrgSpecificTx,
       "cmefg100LocOamParserState": cmefg100LocOamParserState,
       "cmefg100LocOamRmtDteDisc": cmefg100LocOamRmtDteDisc,
       "cmefg100LocOamRmtLoopback": cmefg100LocOamRmtLoopback,
       "cmefg100LocOamUnidirectional": cmefg100LocOamUnidirectional,
       "cmefg100LocOamVarRetrieval": cmefg100LocOamVarRetrieval,
       "cmefg100LocSelfTestFailed": cmefg100LocSelfTestFailed,
       "cmefg100LocSerialNumber": cmefg100LocSerialNumber,
       "cmefg100LocTpAdv1000FDX": cmefg100LocTpAdv1000FDX,
       "cmefg100LocTpAdv1000HDX": cmefg100LocTpAdv1000HDX,
       "cmefg100LocTpAdv100FDX": cmefg100LocTpAdv100FDX,
       "cmefg100LocTpAdv100HDX": cmefg100LocTpAdv100HDX,
       "cmefg100LocTpAdv10FDX": cmefg100LocTpAdv10FDX,
       "cmefg100LocTpAdv10HDX": cmefg100LocTpAdv10HDX,
       "cmefg100LocTpAutoNegot": cmefg100LocTpAutoNegot,
       "cmefg100LocTpConnB": cmefg100LocTpConnB,
       "cmefg100LocTpCross": cmefg100LocTpCross,
       "cmefg100LocTpDuplex": cmefg100LocTpDuplex,
       "cmefg100LocTpLink": cmefg100LocTpLink,
       "cmefg100LocTpPause": cmefg100LocTpPause,
       "cmefg100LocTpQosPause": cmefg100LocTpQosPause,
       "cmefg100LocTpSacEnable": cmefg100LocTpSacEnable,
       "cmefg100LocTpSacStatus": cmefg100LocTpSacStatus,
       "cmefg100LocTpSpeed": cmefg100LocTpSpeed,
       "cmefg100LocTxFxBwaKb": cmefg100LocTxFxBwaKb,
       "cmefg100LocTxFxBwaMb": cmefg100LocTxFxBwaMb,
       "cmefg100LocUptime": cmefg100LocUptime,
       "cmefg100QosHqWeight": cmefg100QosHqWeight,
       "cmefg100QosLqWeight": cmefg100QosLqWeight,
       "cmefg100QosPriority": cmefg100QosPriority,
       "cmefg100RmtColdStart": cmefg100RmtColdStart,
       "cmefg100RmtDetected": cmefg100RmtDetected,
       "cmefg100RmtDmiRxPower": cmefg100RmtDmiRxPower,
       "cmefg100RmtDmiRxPowerAlarm": cmefg100RmtDmiRxPowerAlarm,
       "cmefg100RmtDmiTemp": cmefg100RmtDmiTemp,
       "cmefg100RmtDmiTempAlarm": cmefg100RmtDmiTempAlarm,
       "cmefg100RmtDmiTxBiasAlarm": cmefg100RmtDmiTxBiasAlarm,
       "cmefg100RmtDmiTxBiasCurrent": cmefg100RmtDmiTxBiasCurrent,
       "cmefg100RmtDmiTxPower": cmefg100RmtDmiTxPower,
       "cmefg100RmtDmiTxPowerAlarm": cmefg100RmtDmiTxPowerAlarm,
       "cmefg100RmtFactoryReset": cmefg100RmtFactoryReset,
       "cmefg100RmtFiberAutoNegot": cmefg100RmtFiberAutoNegot,
       "cmefg100RmtFiberLink": cmefg100RmtFiberLink,
       "cmefg100RmtFiberPause": cmefg100RmtFiberPause,
       "cmefg100RmtFiberQosPause": cmefg100RmtFiberQosPause,
       "cmefg100RmtFirmwareRevision": cmefg100RmtFirmwareRevision,
       "cmefg100RmtFpgaRev": cmefg100RmtFpgaRev,
       "cmefg100RmtOamActiveMode": cmefg100RmtOamActiveMode,
       "cmefg100RmtOamCriticalEvent": cmefg100RmtOamCriticalEvent,
       "cmefg100RmtOamLastGasp": cmefg100RmtOamLastGasp,
       "cmefg100RmtOamLinkEvents": cmefg100RmtOamLinkEvents,
       "cmefg100RmtOamLinkFault": cmefg100RmtOamLinkFault,
       "cmefg100RmtOamLocDteDisc": cmefg100RmtOamLocDteDisc,
       "cmefg100RmtOamPeerConfigRevision": cmefg100RmtOamPeerConfigRevision,
       "cmefg100RmtOamPeerMacAddress": cmefg100RmtOamPeerMacAddress,
       "cmefg100RmtOamPeerMaxOamPduSize": cmefg100RmtOamPeerMaxOamPduSize,
       "cmefg100RmtOamPeerMultiplexorState": cmefg100RmtOamPeerMultiplexorState,
       "cmefg100RmtOamPeerParserState": cmefg100RmtOamPeerParserState,
       "cmefg100RmtOamPeerVendorInfo": cmefg100RmtOamPeerVendorInfo,
       "cmefg100RmtOamPeerVendorOui": cmefg100RmtOamPeerVendorOui,
       "cmefg100RmtOamRmtDteDisc": cmefg100RmtOamRmtDteDisc,
       "cmefg100RmtOamRmtLoopback": cmefg100RmtOamRmtLoopback,
       "cmefg100RmtOamUnidirectional": cmefg100RmtOamUnidirectional,
       "cmefg100RmtOamVarRetrieval": cmefg100RmtOamVarRetrieval,
       "cmefg100RmtSelfTestFailed": cmefg100RmtSelfTestFailed,
       "cmefg100RmtSerialNumber": cmefg100RmtSerialNumber,
       "cmefg100RmtTpAdv1000FDX": cmefg100RmtTpAdv1000FDX,
       "cmefg100RmtTpAdv1000HDX": cmefg100RmtTpAdv1000HDX,
       "cmefg100RmtTpAdv100FDX": cmefg100RmtTpAdv100FDX,
       "cmefg100RmtTpAdv100HDX": cmefg100RmtTpAdv100HDX,
       "cmefg100RmtTpAdv10FDX": cmefg100RmtTpAdv10FDX,
       "cmefg100RmtTpAdv10HDX": cmefg100RmtTpAdv10HDX,
       "cmefg100RmtTpAutoNegot": cmefg100RmtTpAutoNegot,
       "cmefg100RmtTpCross": cmefg100RmtTpCross,
       "cmefg100RmtTpDuplex": cmefg100RmtTpDuplex,
       "cmefg100RmtTpLink": cmefg100RmtTpLink,
       "cmefg100RmtTpPause": cmefg100RmtTpPause,
       "cmefg100RmtTpQosPause": cmefg100RmtTpQosPause,
       "cmefg100RmtTpSpeed": cmefg100RmtTpSpeed,
       "cmefg100RmtUptime": cmefg100RmtUptime,
       "cmefg100VlanCacheCmd": cmefg100VlanCacheCmd,
       "cmefg100VlanCacheState": cmefg100VlanCacheState,
       "cmefg100VlanEditCmd": cmefg100VlanEditCmd,
       "cmefg100VlanEditFwdFiber": cmefg100VlanEditFwdFiber,
       "cmefg100VlanEditFwdTp": cmefg100VlanEditFwdTp,
       "cmefg100VlanEditUntagFiber": cmefg100VlanEditUntagFiber,
       "cmefg100VlanEditUntagTp": cmefg100VlanEditUntagTp,
       "cmefg100VlanEditVid": cmefg100VlanEditVid,
       "cmefg100VlanEnable": cmefg100VlanEnable,
       "cmefg100VlanEntries": cmefg100VlanEntries,
       "cmefg100VlanFiberDefaultPri": cmefg100VlanFiberDefaultPri,
       "cmefg100VlanFiberDefaultVid": cmefg100VlanFiberDefaultVid,
       "cmefg100VlanFiberInUntaggedDrop": cmefg100VlanFiberInUntaggedDrop,
       "cmefg100VlanFwdFiberTbl": cmefg100VlanFwdFiberTbl,
       "cmefg100VlanFwdTpTbl": cmefg100VlanFwdTpTbl,
       "cmefg100VlanIngressVidHitNoMem": cmefg100VlanIngressVidHitNoMem,
       "cmefg100VlanIngressVidMiss": cmefg100VlanIngressVidMiss,
       "cmefg100VlanPriMapTbl": cmefg100VlanPriMapTbl,
       "cmefg100VlanPriTagCtrl": cmefg100VlanPriTagCtrl,
       "cmefg100VlanSetFailed": cmefg100VlanSetFailed,
       "cmefg100VlanTagIn": cmefg100VlanTagIn,
       "cmefg100VlanTpDefaultPri": cmefg100VlanTpDefaultPri,
       "cmefg100VlanTpDefaultVid": cmefg100VlanTpDefaultVid,
       "cmefg100VlanTpInUntaggedDrop": cmefg100VlanTpInUntaggedDrop,
       "cmefg100VlanUntagFiberTbl": cmefg100VlanUntagFiberTbl,
       "cmefg100VlanUntagTpTbl": cmefg100VlanUntagTpTbl,
       "cmefg100VlanVidTagCtrl": cmefg100VlanVidTagCtrl,
       "cmefg100VlanVidTbl": cmefg100VlanVidTbl,
       "cmefg100CacheClean": cmefg100CacheClean,
       "backplane": backplane,
       "mcc16": mcc16,
       "mcc16Common": mcc16Common,
       "mcc16ComHwReset": mcc16ComHwReset,
       "mcc16ComMgmtHwRev": mcc16ComMgmtHwRev,
       "mcc16ComMgmtSwRev": mcc16ComMgmtSwRev,
       "mcc16ComIpAddr": mcc16ComIpAddr,
       "mcc16ComNetMask": mcc16ComNetMask,
       "mcc16ComGateway": mcc16ComGateway,
       "mcc16ComPS1Power": mcc16ComPS1Power,
       "mcc16ComPS1InUse": mcc16ComPS1InUse,
       "mcc16ComPS2Power": mcc16ComPS2Power,
       "mcc16ComPS2InUse": mcc16ComPS2InUse,
       "mcc16ComNotes": mcc16ComNotes,
       "mcc16Ver1": mcc16Ver1,
       "mcc16SlotTable": mcc16SlotTable,
       "mcc16SlotEntry": mcc16SlotEntry,
       "mcc16Index": mcc16Index,
       "mcc16DeviceType": mcc16DeviceType,
       "cps": cps,
       "cpsCabSummary": cpsCabSummary,
       "cpsCabinetTable": cpsCabinetTable,
       "cpsCabinetEntry": cpsCabinetEntry,
       "cpsCabinetBiaIndex": cpsCabinetBiaIndex,
       "cpsCabinetModel": cpsCabinetModel,
       "cpsCabinetDescription": cpsCabinetDescription,
       "cpsCabinetSequence": cpsCabinetSequence,
       "cpsCabDetail": cpsCabDetail,
       "cpsMc1800Table": cpsMc1800Table,
       "cpsMc1800Entry": cpsMc1800Entry,
       "cpsMc1800BiaIndex": cpsMc1800BiaIndex,
       "cpsMc1800Description": cpsMc1800Description,
       "cpsMc1800PSPower1": cpsMc1800PSPower1,
       "cpsMc1800PSInUse1": cpsMc1800PSInUse1,
       "cpsMc1800PSPower2": cpsMc1800PSPower2,
       "cpsMc1800PSInUse2": cpsMc1800PSInUse2,
       "cpsMc1800MRevision": cpsMc1800MRevision,
       "cpsMc1300Table": cpsMc1300Table,
       "cpsMc1300Entry": cpsMc1300Entry,
       "cpsMc1300BiaIndex": cpsMc1300BiaIndex,
       "cpsMc1300Description": cpsMc1300Description,
       "cpsMc1300PSPower1": cpsMc1300PSPower1,
       "cpsMc1300PSInUse1": cpsMc1300PSInUse1,
       "cpsMc1300PSPower2": cpsMc1300PSPower2,
       "cpsMc1300PSInUse2": cpsMc1300PSInUse2,
       "cpsMc1300MRevision": cpsMc1300MRevision,
       "cpsMc0200Table": cpsMc0200Table,
       "cpsMc0200Entry": cpsMc0200Entry,
       "cpsMc0200BiaIndex": cpsMc0200BiaIndex,
       "cpsMc0200Description": cpsMc0200Description,
       "cpsMc0200MRevision": cpsMc0200MRevision,
       "cpsMc1900Table": cpsMc1900Table,
       "cpsMc1900Entry": cpsMc1900Entry,
       "cpsMc1900BiaIndex": cpsMc1900BiaIndex,
       "cpsMc1900Description": cpsMc1900Description,
       "cpsMc1900MRevision": cpsMc1900MRevision,
       "smacf100Table": smacf100Table,
       "smacf100Entry": smacf100Entry,
       "smacf100BiaIndex": smacf100BiaIndex,
       "smacf100Description": smacf100Description,
       "smacf100MRevision": smacf100MRevision,
       "smacf100SpanningTree": smacf100SpanningTree,
       "smacf100ResetCounters": smacf100ResetCounters,
       "smacf100SelfTest": smacf100SelfTest,
       "smacf100QosEnable": smacf100QosEnable,
       "smacf100QosHPThreshold": smacf100QosHPThreshold,
       "smacf100QosLqWeight": smacf100QosLqWeight,
       "smacf100QosHqWeight": smacf100QosHqWeight,
       "smacf100SNMPModuleInstalled": smacf100SNMPModuleInstalled,
       "smacf100AgingTimer": smacf100AgingTimer,
       "cpsMc0800Table": cpsMc0800Table,
       "cpsMc0800Entry": cpsMc0800Entry,
       "cpsMc0800BiaIndex": cpsMc0800BiaIndex,
       "cpsMc0800Description": cpsMc0800Description,
       "cpsMc0800MRevision": cpsMc0800MRevision,
       "cpsAgent": cpsAgent,
       "cpsGroupCtrl": cpsGroupCtrl,
       "cpsSlotPwrTable": cpsSlotPwrTable,
       "cpsSlotPwrEntry": cpsSlotPwrEntry,
       "cpsSlotPwrBiaIndex": cpsSlotPwrBiaIndex,
       "cpsSlotPwrSlotIndex": cpsSlotPwrSlotIndex,
       "cpsSlotPwrState": cpsSlotPwrState,
       "cpsIsPrimary": cpsIsPrimary}
)
