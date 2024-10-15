# SNMP MIB module (NTNTECH-INTERFACE-MODULE-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTNTECH-INTERFACE-MODULE-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:44 2024
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

(NtnCounter32,
 NtnDisplayString,
 NtnGauge32,
 NtnMacAddress,
 NtnTimeTicks,
 ntntechInterfaceModule) = mibBuilder.importSymbols(
    "NTNTECH-ROOT-MIB",
    "NtnCounter32",
    "NtnDisplayString",
    "NtnGauge32",
    "NtnMacAddress",
    "NtnTimeTicks",
    "ntntechInterfaceModule")

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

ntntechInterfaceModuleStatusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2)
)
ntntechInterfaceModuleStatusMIB.setRevisions(
        ("1902-06-17 03:05",
         "1902-08-13 11:03",
         "1902-08-28 10:48",
         "1902-09-27 08:11",
         "1902-10-22 02:00",
         "1903-09-30 10:43",
         "1904-03-15 10:00",
         "1904-04-27 10:48",
         "1904-10-11 09:39",
         "1904-11-17 10:04")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfModStaMIBObjects_ObjectIdentity = ObjectIdentity
ifModStaMIBObjects = _IfModStaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1)
)
_IfModStaValues_ObjectIdentity = ObjectIdentity
ifModStaValues = _IfModStaValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1)
)
_ValInterface_ObjectIdentity = ObjectIdentity
valInterface = _ValInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1)
)


class _IfStaCount_Type(Integer32):
    """Custom type ifStaCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_IfStaCount_Type.__name__ = "Integer32"
_IfStaCount_Object = MibScalar
ifStaCount = _IfStaCount_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 1),
    _IfStaCount_Type()
)
ifStaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaCount.setStatus("current")
_IfStaTable_Object = MibTable
ifStaTable = _IfStaTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ifStaTable.setStatus("current")
_IfStaEntry_Object = MibTableRow
ifStaEntry = _IfStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 2, 1)
)
ifStaEntry.setIndexNames(
    (0, "NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"),
)
if mibBuilder.loadTexts:
    ifStaEntry.setStatus("current")


class _IfStaSlotIndex_Type(Integer32):
    """Custom type ifStaSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_IfStaSlotIndex_Type.__name__ = "Integer32"
_IfStaSlotIndex_Object = MibTableColumn
ifStaSlotIndex = _IfStaSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 2, 1, 1),
    _IfStaSlotIndex_Type()
)
ifStaSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaSlotIndex.setStatus("current")


class _IfStaType_Type(Integer32):
    """Custom type ifStaType based on Integer32"""
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
              130,
              131,
              135)
        )
    )
    namedValues = NamedValues(
        *(("aam8000p12", 10),
          ("aam8000p24", 30),
          ("aim24000p48", 35),
          ("amD8000p12", 11),
          ("ane8420", 135),
          ("auD8000p12", 131),
          ("eam2000p12", 5),
          ("eim2000p12", 32),
          ("eim2000p24", 34),
          ("iam144p12", 1),
          ("sam1000p12", 2),
          ("sam2000DQp12", 13),
          ("sam2000Dp12", 12),
          ("sam2000GVp12", 17),
          ("sam2000Gp12", 14),
          ("sam2000QVp12", 16),
          ("sam2000Qp12", 9),
          ("sam2000Vp12", 15),
          ("sam2000p12", 4),
          ("sim2000Vp12", 21),
          ("sim2000Vp24", 20),
          ("sim2000p12", 18),
          ("sim2000p24", 6),
          ("smD2000Gp12", 19),
          ("smD2000Qp12", 8),
          ("smD2000p12", 7),
          ("smD2000p24", 130),
          ("sne2040", 14),
          ("suD2002p6E", 29),
          ("suD2002p6T", 28),
          ("suD2003p12E", 25),
          ("suD2003p12T", 24),
          ("suD2011p12E", 23),
          ("suD2011p12T", 22),
          ("suD2011p6E", 27),
          ("suD2011p6T", 26),
          ("tam1500p12", 3),
          ("tim1500p12", 31),
          ("tim1500p24", 33))
    )


_IfStaType_Type.__name__ = "Integer32"
_IfStaType_Object = MibTableColumn
ifStaType = _IfStaType_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 2, 1, 2),
    _IfStaType_Type()
)
ifStaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaType.setStatus("current")
_IfStaFirmwareRev_Type = NtnDisplayString
_IfStaFirmwareRev_Object = MibTableColumn
ifStaFirmwareRev = _IfStaFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 2, 1, 3),
    _IfStaFirmwareRev_Type()
)
ifStaFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaFirmwareRev.setStatus("current")
_IfStaPortTable_Object = MibTable
ifStaPortTable = _IfStaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ifStaPortTable.setStatus("current")
_IfStaPortEntry_Object = MibTableRow
ifStaPortEntry = _IfStaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1)
)
ifStaPortEntry.setIndexNames(
    (0, "NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaPortSlotIndex"),
    (0, "NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaPortPortIndex"),
)
if mibBuilder.loadTexts:
    ifStaPortEntry.setStatus("current")


class _IfStaPortSlotIndex_Type(Integer32):
    """Custom type ifStaPortSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_IfStaPortSlotIndex_Type.__name__ = "Integer32"
_IfStaPortSlotIndex_Object = MibTableColumn
ifStaPortSlotIndex = _IfStaPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 1),
    _IfStaPortSlotIndex_Type()
)
ifStaPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortSlotIndex.setStatus("current")


class _IfStaPortPortIndex_Type(Integer32):
    """Custom type ifStaPortPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IfStaPortPortIndex_Type.__name__ = "Integer32"
_IfStaPortPortIndex_Object = MibTableColumn
ifStaPortPortIndex = _IfStaPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 2),
    _IfStaPortPortIndex_Type()
)
ifStaPortPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortPortIndex.setStatus("current")
_IfStaPortFirmwareRev_Type = NtnDisplayString
_IfStaPortFirmwareRev_Object = MibTableColumn
ifStaPortFirmwareRev = _IfStaPortFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 3),
    _IfStaPortFirmwareRev_Type()
)
ifStaPortFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortFirmwareRev.setStatus("current")


class _IfStaPortLinkState_Type(Integer32):
    """Custom type ifStaPortLinkState based on Integer32"""
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
        *(("linkdefect", 4),
          ("linkdisabled", 5),
          ("linkdown", 2),
          ("linkloopback", 3),
          ("linkup", 1))
    )


_IfStaPortLinkState_Type.__name__ = "Integer32"
_IfStaPortLinkState_Object = MibTableColumn
ifStaPortLinkState = _IfStaPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 4),
    _IfStaPortLinkState_Type()
)
ifStaPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortLinkState.setStatus("current")
_IfStaPortRxWanNUCastUtil_Type = NtnCounter32
_IfStaPortRxWanNUCastUtil_Object = MibTableColumn
ifStaPortRxWanNUCastUtil = _IfStaPortRxWanNUCastUtil_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 5),
    _IfStaPortRxWanNUCastUtil_Type()
)
ifStaPortRxWanNUCastUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortRxWanNUCastUtil.setStatus("current")
_IfStaPortRxWanNUCastRate_Type = NtnGauge32
_IfStaPortRxWanNUCastRate_Object = MibTableColumn
ifStaPortRxWanNUCastRate = _IfStaPortRxWanNUCastRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 6),
    _IfStaPortRxWanNUCastRate_Type()
)
ifStaPortRxWanNUCastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortRxWanNUCastRate.setStatus("current")
_IfStaPortRxWanNUCastMaxRate_Type = NtnGauge32
_IfStaPortRxWanNUCastMaxRate_Object = MibTableColumn
ifStaPortRxWanNUCastMaxRate = _IfStaPortRxWanNUCastMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 7),
    _IfStaPortRxWanNUCastMaxRate_Type()
)
ifStaPortRxWanNUCastMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortRxWanNUCastMaxRate.setStatus("current")
_IfStaPortRxWanNUCastAveRate_Type = NtnGauge32
_IfStaPortRxWanNUCastAveRate_Object = MibTableColumn
ifStaPortRxWanNUCastAveRate = _IfStaPortRxWanNUCastAveRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 8),
    _IfStaPortRxWanNUCastAveRate_Type()
)
ifStaPortRxWanNUCastAveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortRxWanNUCastAveRate.setStatus("current")
_IfStaPortTxWanNUCastUtil_Type = NtnCounter32
_IfStaPortTxWanNUCastUtil_Object = MibTableColumn
ifStaPortTxWanNUCastUtil = _IfStaPortTxWanNUCastUtil_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 9),
    _IfStaPortTxWanNUCastUtil_Type()
)
ifStaPortTxWanNUCastUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTxWanNUCastUtil.setStatus("current")
_IfStaPortTxWanNUCastRate_Type = NtnGauge32
_IfStaPortTxWanNUCastRate_Object = MibTableColumn
ifStaPortTxWanNUCastRate = _IfStaPortTxWanNUCastRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 10),
    _IfStaPortTxWanNUCastRate_Type()
)
ifStaPortTxWanNUCastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTxWanNUCastRate.setStatus("current")
_IfStaPortTxWanNUCastMaxRate_Type = NtnGauge32
_IfStaPortTxWanNUCastMaxRate_Object = MibTableColumn
ifStaPortTxWanNUCastMaxRate = _IfStaPortTxWanNUCastMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 11),
    _IfStaPortTxWanNUCastMaxRate_Type()
)
ifStaPortTxWanNUCastMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTxWanNUCastMaxRate.setStatus("current")
_IfStaPortTxWanNUCastAveRate_Type = NtnGauge32
_IfStaPortTxWanNUCastAveRate_Object = MibTableColumn
ifStaPortTxWanNUCastAveRate = _IfStaPortTxWanNUCastAveRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 12),
    _IfStaPortTxWanNUCastAveRate_Type()
)
ifStaPortTxWanNUCastAveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTxWanNUCastAveRate.setStatus("current")
_IfStaPortRxWanUCastUtil_Type = NtnCounter32
_IfStaPortRxWanUCastUtil_Object = MibTableColumn
ifStaPortRxWanUCastUtil = _IfStaPortRxWanUCastUtil_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 13),
    _IfStaPortRxWanUCastUtil_Type()
)
ifStaPortRxWanUCastUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortRxWanUCastUtil.setStatus("current")
_IfStaPortRxWanUCastRate_Type = NtnGauge32
_IfStaPortRxWanUCastRate_Object = MibTableColumn
ifStaPortRxWanUCastRate = _IfStaPortRxWanUCastRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 14),
    _IfStaPortRxWanUCastRate_Type()
)
ifStaPortRxWanUCastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortRxWanUCastRate.setStatus("current")
_IfStaPortRxWanUCastMaxRate_Type = NtnGauge32
_IfStaPortRxWanUCastMaxRate_Object = MibTableColumn
ifStaPortRxWanUCastMaxRate = _IfStaPortRxWanUCastMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 15),
    _IfStaPortRxWanUCastMaxRate_Type()
)
ifStaPortRxWanUCastMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortRxWanUCastMaxRate.setStatus("current")
_IfStaPortRxWanUCastAveRate_Type = NtnGauge32
_IfStaPortRxWanUCastAveRate_Object = MibTableColumn
ifStaPortRxWanUCastAveRate = _IfStaPortRxWanUCastAveRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 16),
    _IfStaPortRxWanUCastAveRate_Type()
)
ifStaPortRxWanUCastAveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortRxWanUCastAveRate.setStatus("current")
_IfStaPortTxWanUCastUtil_Type = NtnCounter32
_IfStaPortTxWanUCastUtil_Object = MibTableColumn
ifStaPortTxWanUCastUtil = _IfStaPortTxWanUCastUtil_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 17),
    _IfStaPortTxWanUCastUtil_Type()
)
ifStaPortTxWanUCastUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTxWanUCastUtil.setStatus("current")
_IfStaPortTxWanUCastRate_Type = NtnGauge32
_IfStaPortTxWanUCastRate_Object = MibTableColumn
ifStaPortTxWanUCastRate = _IfStaPortTxWanUCastRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 18),
    _IfStaPortTxWanUCastRate_Type()
)
ifStaPortTxWanUCastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTxWanUCastRate.setStatus("current")
_IfStaPortTxWanUCastMaxRate_Type = NtnGauge32
_IfStaPortTxWanUCastMaxRate_Object = MibTableColumn
ifStaPortTxWanUCastMaxRate = _IfStaPortTxWanUCastMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 19),
    _IfStaPortTxWanUCastMaxRate_Type()
)
ifStaPortTxWanUCastMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTxWanUCastMaxRate.setStatus("current")
_IfStaPortTxWanUCastAveRate_Type = NtnGauge32
_IfStaPortTxWanUCastAveRate_Object = MibTableColumn
ifStaPortTxWanUCastAveRate = _IfStaPortTxWanUCastAveRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 20),
    _IfStaPortTxWanUCastAveRate_Type()
)
ifStaPortTxWanUCastAveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTxWanUCastAveRate.setStatus("current")
_IfStaPortTotRxWanPercentUtil_Type = NtnCounter32
_IfStaPortTotRxWanPercentUtil_Object = MibTableColumn
ifStaPortTotRxWanPercentUtil = _IfStaPortTotRxWanPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 21),
    _IfStaPortTotRxWanPercentUtil_Type()
)
ifStaPortTotRxWanPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTotRxWanPercentUtil.setStatus("current")
_IfStaPortTotRxWanRate_Type = NtnGauge32
_IfStaPortTotRxWanRate_Object = MibTableColumn
ifStaPortTotRxWanRate = _IfStaPortTotRxWanRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 22),
    _IfStaPortTotRxWanRate_Type()
)
ifStaPortTotRxWanRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTotRxWanRate.setStatus("current")
_IfStaPortTotTxWanPercentUtil_Type = NtnCounter32
_IfStaPortTotTxWanPercentUtil_Object = MibTableColumn
ifStaPortTotTxWanPercentUtil = _IfStaPortTotTxWanPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 23),
    _IfStaPortTotTxWanPercentUtil_Type()
)
ifStaPortTotTxWanPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTotTxWanPercentUtil.setStatus("current")
_IfStaPortTotTxWanRate_Type = NtnGauge32
_IfStaPortTotTxWanRate_Object = MibTableColumn
ifStaPortTotTxWanRate = _IfStaPortTotTxWanRate_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 24),
    _IfStaPortTotTxWanRate_Type()
)
ifStaPortTotTxWanRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTotTxWanRate.setStatus("current")
_IfStaPortTotUpTime_Type = NtnTimeTicks
_IfStaPortTotUpTime_Object = MibTableColumn
ifStaPortTotUpTime = _IfStaPortTotUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 25),
    _IfStaPortTotUpTime_Type()
)
ifStaPortTotUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTotUpTime.setStatus("current")
_IfStaPortTotDwnTime_Type = NtnTimeTicks
_IfStaPortTotDwnTime_Object = MibTableColumn
ifStaPortTotDwnTime = _IfStaPortTotDwnTime_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 26),
    _IfStaPortTotDwnTime_Type()
)
ifStaPortTotDwnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaPortTotDwnTime.setStatus("current")
_IfStaUCastTxPkt_Type = NtnCounter32
_IfStaUCastTxPkt_Object = MibTableColumn
ifStaUCastTxPkt = _IfStaUCastTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 27),
    _IfStaUCastTxPkt_Type()
)
ifStaUCastTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaUCastTxPkt.setStatus("current")
_IfStaUCastRxPkt_Type = NtnCounter32
_IfStaUCastRxPkt_Object = MibTableColumn
ifStaUCastRxPkt = _IfStaUCastRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 28),
    _IfStaUCastRxPkt_Type()
)
ifStaUCastRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaUCastRxPkt.setStatus("current")
_IfStaNUCastTxPkt_Type = NtnCounter32
_IfStaNUCastTxPkt_Object = MibTableColumn
ifStaNUCastTxPkt = _IfStaNUCastTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 29),
    _IfStaNUCastTxPkt_Type()
)
ifStaNUCastTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaNUCastTxPkt.setStatus("current")
_IfStaNUCastRxPkt_Type = NtnCounter32
_IfStaNUCastRxPkt_Object = MibTableColumn
ifStaNUCastRxPkt = _IfStaNUCastRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 30),
    _IfStaNUCastRxPkt_Type()
)
ifStaNUCastRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaNUCastRxPkt.setStatus("current")


class _IfStaNetworkLoopCount_Type(Integer32):
    """Custom type ifStaNetworkLoopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IfStaNetworkLoopCount_Type.__name__ = "Integer32"
_IfStaNetworkLoopCount_Object = MibTableColumn
ifStaNetworkLoopCount = _IfStaNetworkLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 31),
    _IfStaNetworkLoopCount_Type()
)
ifStaNetworkLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaNetworkLoopCount.setStatus("current")
_IfStaLastMacCausingLoop_Type = NtnMacAddress
_IfStaLastMacCausingLoop_Object = MibTableColumn
ifStaLastMacCausingLoop = _IfStaLastMacCausingLoop_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 32),
    _IfStaLastMacCausingLoop_Type()
)
ifStaLastMacCausingLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaLastMacCausingLoop.setStatus("current")


class _IfStaLastMacSrcPort_Type(Integer32):
    """Custom type ifStaLastMacSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfStaLastMacSrcPort_Type.__name__ = "Integer32"
_IfStaLastMacSrcPort_Object = MibTableColumn
ifStaLastMacSrcPort = _IfStaLastMacSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 33),
    _IfStaLastMacSrcPort_Type()
)
ifStaLastMacSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaLastMacSrcPort.setStatus("current")


class _IfStaLoopBondedGroupPortList_Type(Integer32):
    """Custom type ifStaLoopBondedGroupPortList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IfStaLoopBondedGroupPortList_Type.__name__ = "Integer32"
_IfStaLoopBondedGroupPortList_Object = MibTableColumn
ifStaLoopBondedGroupPortList = _IfStaLoopBondedGroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 34),
    _IfStaLoopBondedGroupPortList_Type()
)
ifStaLoopBondedGroupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaLoopBondedGroupPortList.setStatus("current")


class _IfStaLoopBondedGroupID_Type(Integer32):
    """Custom type ifStaLoopBondedGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IfStaLoopBondedGroupID_Type.__name__ = "Integer32"
_IfStaLoopBondedGroupID_Object = MibTableColumn
ifStaLoopBondedGroupID = _IfStaLoopBondedGroupID_Object(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2, 1, 1, 1, 3, 1, 35),
    _IfStaLoopBondedGroupID_Type()
)
ifStaLoopBondedGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStaLoopBondedGroupID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTNTECH-INTERFACE-MODULE-STATUS-MIB",
    **{"ntntechInterfaceModuleStatusMIB": ntntechInterfaceModuleStatusMIB,
       "ifModStaMIBObjects": ifModStaMIBObjects,
       "ifModStaValues": ifModStaValues,
       "valInterface": valInterface,
       "ifStaCount": ifStaCount,
       "ifStaTable": ifStaTable,
       "ifStaEntry": ifStaEntry,
       "ifStaSlotIndex": ifStaSlotIndex,
       "ifStaType": ifStaType,
       "ifStaFirmwareRev": ifStaFirmwareRev,
       "ifStaPortTable": ifStaPortTable,
       "ifStaPortEntry": ifStaPortEntry,
       "ifStaPortSlotIndex": ifStaPortSlotIndex,
       "ifStaPortPortIndex": ifStaPortPortIndex,
       "ifStaPortFirmwareRev": ifStaPortFirmwareRev,
       "ifStaPortLinkState": ifStaPortLinkState,
       "ifStaPortRxWanNUCastUtil": ifStaPortRxWanNUCastUtil,
       "ifStaPortRxWanNUCastRate": ifStaPortRxWanNUCastRate,
       "ifStaPortRxWanNUCastMaxRate": ifStaPortRxWanNUCastMaxRate,
       "ifStaPortRxWanNUCastAveRate": ifStaPortRxWanNUCastAveRate,
       "ifStaPortTxWanNUCastUtil": ifStaPortTxWanNUCastUtil,
       "ifStaPortTxWanNUCastRate": ifStaPortTxWanNUCastRate,
       "ifStaPortTxWanNUCastMaxRate": ifStaPortTxWanNUCastMaxRate,
       "ifStaPortTxWanNUCastAveRate": ifStaPortTxWanNUCastAveRate,
       "ifStaPortRxWanUCastUtil": ifStaPortRxWanUCastUtil,
       "ifStaPortRxWanUCastRate": ifStaPortRxWanUCastRate,
       "ifStaPortRxWanUCastMaxRate": ifStaPortRxWanUCastMaxRate,
       "ifStaPortRxWanUCastAveRate": ifStaPortRxWanUCastAveRate,
       "ifStaPortTxWanUCastUtil": ifStaPortTxWanUCastUtil,
       "ifStaPortTxWanUCastRate": ifStaPortTxWanUCastRate,
       "ifStaPortTxWanUCastMaxRate": ifStaPortTxWanUCastMaxRate,
       "ifStaPortTxWanUCastAveRate": ifStaPortTxWanUCastAveRate,
       "ifStaPortTotRxWanPercentUtil": ifStaPortTotRxWanPercentUtil,
       "ifStaPortTotRxWanRate": ifStaPortTotRxWanRate,
       "ifStaPortTotTxWanPercentUtil": ifStaPortTotTxWanPercentUtil,
       "ifStaPortTotTxWanRate": ifStaPortTotTxWanRate,
       "ifStaPortTotUpTime": ifStaPortTotUpTime,
       "ifStaPortTotDwnTime": ifStaPortTotDwnTime,
       "ifStaUCastTxPkt": ifStaUCastTxPkt,
       "ifStaUCastRxPkt": ifStaUCastRxPkt,
       "ifStaNUCastTxPkt": ifStaNUCastTxPkt,
       "ifStaNUCastRxPkt": ifStaNUCastRxPkt,
       "ifStaNetworkLoopCount": ifStaNetworkLoopCount,
       "ifStaLastMacCausingLoop": ifStaLastMacCausingLoop,
       "ifStaLastMacSrcPort": ifStaLastMacSrcPort,
       "ifStaLoopBondedGroupPortList": ifStaLoopBondedGroupPortList,
       "ifStaLoopBondedGroupID": ifStaLoopBondedGroupID}
)
