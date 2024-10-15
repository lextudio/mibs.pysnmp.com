# SNMP MIB module (CISCO-WAN-BBIF-ATM-CONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-BBIF-ATM-CONN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:53 2024
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

(bbChanCnfGrp,
 bbChanStateGrp) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "bbChanCnfGrp",
    "bbChanStateGrp")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoWanBbifAtmConnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 35)
)
ciscoWanBbifAtmConnMIB.setRevisions(
        ("2002-09-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IfNsapAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )



# MIB Managed Objects in the order of their OIDs

_BbChanCnfGrpTable_Object = MibTable
bbChanCnfGrpTable = _BbChanCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    bbChanCnfGrpTable.setStatus("current")
_BbChanCnfGrpEntry_Object = MibTableRow
bbChanCnfGrpEntry = _BbChanCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1)
)
bbChanCnfGrpEntry.setIndexNames(
    (0, "CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanCnfNum"),
)
if mibBuilder.loadTexts:
    bbChanCnfGrpEntry.setStatus("current")


class _BbChanCnfNum_Type(Integer32):
    """Custom type bbChanCnfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4111),
    )


_BbChanCnfNum_Type.__name__ = "Integer32"
_BbChanCnfNum_Object = MibTableColumn
bbChanCnfNum = _BbChanCnfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 1),
    _BbChanCnfNum_Type()
)
bbChanCnfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanCnfNum.setStatus("current")


class _BbChanRowStatus_Type(Integer32):
    """Custom type bbChanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2),
          ("modify", 3))
    )


_BbChanRowStatus_Type.__name__ = "Integer32"
_BbChanRowStatus_Object = MibTableColumn
bbChanRowStatus = _BbChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 2),
    _BbChanRowStatus_Type()
)
bbChanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanRowStatus.setStatus("current")


class _BbChanConnType_Type(Integer32):
    """Custom type bbChanConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcc", 2),
          ("vpc", 1))
    )


_BbChanConnType_Type.__name__ = "Integer32"
_BbChanConnType_Object = MibTableColumn
bbChanConnType = _BbChanConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 3),
    _BbChanConnType_Type()
)
bbChanConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanConnType.setStatus("current")


class _BbChanServiceType_Type(Integer32):
    """Custom type bbChanServiceType based on Integer32"""
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
        *(("abr", 3),
          ("cbr", 1),
          ("ubr", 4),
          ("vbr", 2),
          ("vbr-rt", 5))
    )


_BbChanServiceType_Type.__name__ = "Integer32"
_BbChanServiceType_Object = MibTableColumn
bbChanServiceType = _BbChanServiceType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 4),
    _BbChanServiceType_Type()
)
bbChanServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanServiceType.setStatus("current")


class _BbChanConnDesc_Type(DisplayString):
    """Custom type bbChanConnDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BbChanConnDesc_Type.__name__ = "DisplayString"
_BbChanConnDesc_Object = MibTableColumn
bbChanConnDesc = _BbChanConnDesc_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 5),
    _BbChanConnDesc_Type()
)
bbChanConnDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanConnDesc.setStatus("current")


class _BbChanSvcFlag_Type(Integer32):
    """Custom type bbChanSvcFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 2),
          ("spvc", 3),
          ("svc", 1))
    )


_BbChanSvcFlag_Type.__name__ = "Integer32"
_BbChanSvcFlag_Object = MibTableColumn
bbChanSvcFlag = _BbChanSvcFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 6),
    _BbChanSvcFlag_Type()
)
bbChanSvcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanSvcFlag.setStatus("current")
_BbChanSvcConnId_Type = Integer32
_BbChanSvcConnId_Object = MibTableColumn
bbChanSvcConnId = _BbChanSvcConnId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 7),
    _BbChanSvcConnId_Type()
)
bbChanSvcConnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanSvcConnId.setStatus("current")


class _BbChanIfNum_Type(Integer32):
    """Custom type bbChanIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BbChanIfNum_Type.__name__ = "Integer32"
_BbChanIfNum_Object = MibTableColumn
bbChanIfNum = _BbChanIfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 8),
    _BbChanIfNum_Type()
)
bbChanIfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanIfNum.setStatus("current")


class _BbChanVpi_Type(Integer32):
    """Custom type bbChanVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BbChanVpi_Type.__name__ = "Integer32"
_BbChanVpi_Object = MibTableColumn
bbChanVpi = _BbChanVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 9),
    _BbChanVpi_Type()
)
bbChanVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanVpi.setStatus("current")


class _BbChanVci_Type(Integer32):
    """Custom type bbChanVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BbChanVci_Type.__name__ = "Integer32"
_BbChanVci_Object = MibTableColumn
bbChanVci = _BbChanVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 10),
    _BbChanVci_Type()
)
bbChanVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanVci.setStatus("current")


class _BbChanUpcEnable_Type(Integer32):
    """Custom type bbChanUpcEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BbChanUpcEnable_Type.__name__ = "Integer32"
_BbChanUpcEnable_Object = MibTableColumn
bbChanUpcEnable = _BbChanUpcEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 11),
    _BbChanUpcEnable_Type()
)
bbChanUpcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanUpcEnable.setStatus("current")


class _BbChanUpcPCR_Type(Integer32):
    """Custom type bbChanUpcPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1412832),
    )


_BbChanUpcPCR_Type.__name__ = "Integer32"
_BbChanUpcPCR_Object = MibTableColumn
bbChanUpcPCR = _BbChanUpcPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 12),
    _BbChanUpcPCR_Type()
)
bbChanUpcPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanUpcPCR.setStatus("current")


class _BbChanUpcCDVT_Type(Integer32):
    """Custom type bbChanUpcCDVT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000000),
    )


_BbChanUpcCDVT_Type.__name__ = "Integer32"
_BbChanUpcCDVT_Object = MibTableColumn
bbChanUpcCDVT = _BbChanUpcCDVT_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 13),
    _BbChanUpcCDVT_Type()
)
bbChanUpcCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanUpcCDVT.setStatus("current")


class _BbChanUpcSCR_Type(Integer32):
    """Custom type bbChanUpcSCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1412832),
    )


_BbChanUpcSCR_Type.__name__ = "Integer32"
_BbChanUpcSCR_Object = MibTableColumn
bbChanUpcSCR = _BbChanUpcSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 14),
    _BbChanUpcSCR_Type()
)
bbChanUpcSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanUpcSCR.setStatus("current")


class _BbChanUpcMBS_Type(Integer32):
    """Custom type bbChanUpcMBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000000),
    )


_BbChanUpcMBS_Type.__name__ = "Integer32"
_BbChanUpcMBS_Object = MibTableColumn
bbChanUpcMBS = _BbChanUpcMBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 15),
    _BbChanUpcMBS_Type()
)
bbChanUpcMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanUpcMBS.setStatus("current")


class _BbChanGcra1Action_Type(Integer32):
    """Custom type bbChanGcra1Action based on Integer32"""
    defaultValue = 4

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
        *(("discardAllNonComformCells", 4),
          ("noAction", 1),
          ("tagAndDiscard", 3),
          ("tagCells", 2))
    )


_BbChanGcra1Action_Type.__name__ = "Integer32"
_BbChanGcra1Action_Object = MibTableColumn
bbChanGcra1Action = _BbChanGcra1Action_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 16),
    _BbChanGcra1Action_Type()
)
bbChanGcra1Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanGcra1Action.setStatus("current")


class _BbChanGcra2Action_Type(Integer32):
    """Custom type bbChanGcra2Action based on Integer32"""
    defaultValue = 4

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
        *(("discardAllNonComformCells", 4),
          ("noAction", 1),
          ("tagAndDiscard", 3),
          ("tagCells", 2))
    )


_BbChanGcra2Action_Type.__name__ = "Integer32"
_BbChanGcra2Action_Object = MibTableColumn
bbChanGcra2Action = _BbChanGcra2Action_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 17),
    _BbChanGcra2Action_Type()
)
bbChanGcra2Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanGcra2Action.setStatus("current")


class _BbChanUpcSCRPolicing_Type(Integer32):
    """Custom type bbChanUpcSCRPolicing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clp0", 1),
          ("clp0and1", 2),
          ("off", 3))
    )


_BbChanUpcSCRPolicing_Type.__name__ = "Integer32"
_BbChanUpcSCRPolicing_Object = MibTableColumn
bbChanUpcSCRPolicing = _BbChanUpcSCRPolicing_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 18),
    _BbChanUpcSCRPolicing_Type()
)
bbChanUpcSCRPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanUpcSCRPolicing.setStatus("current")


class _BbChanEfciThreshold_Type(Integer32):
    """Custom type bbChanEfciThreshold based on Integer32"""
    defaultValue = 196608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 491520),
    )


_BbChanEfciThreshold_Type.__name__ = "Integer32"
_BbChanEfciThreshold_Object = MibTableColumn
bbChanEfciThreshold = _BbChanEfciThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 19),
    _BbChanEfciThreshold_Type()
)
bbChanEfciThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanEfciThreshold.setStatus("current")


class _BbChanDiscardOption_Type(Integer32):
    """Custom type bbChanDiscardOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clpHysteresis", 1),
          ("frameDiscard", 2))
    )


_BbChanDiscardOption_Type.__name__ = "Integer32"
_BbChanDiscardOption_Object = MibTableColumn
bbChanDiscardOption = _BbChanDiscardOption_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 20),
    _BbChanDiscardOption_Type()
)
bbChanDiscardOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanDiscardOption.setStatus("current")


class _BbChanFrmDiscardThreshold_Type(Integer32):
    """Custom type bbChanFrmDiscardThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 491520),
    )


_BbChanFrmDiscardThreshold_Type.__name__ = "Integer32"
_BbChanFrmDiscardThreshold_Object = MibTableColumn
bbChanFrmDiscardThreshold = _BbChanFrmDiscardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 21),
    _BbChanFrmDiscardThreshold_Type()
)
bbChanFrmDiscardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanFrmDiscardThreshold.setStatus("current")


class _BbChanClpHiThreshold_Type(Integer32):
    """Custom type bbChanClpHiThreshold based on Integer32"""
    defaultValue = 196608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 491520),
    )


_BbChanClpHiThreshold_Type.__name__ = "Integer32"
_BbChanClpHiThreshold_Object = MibTableColumn
bbChanClpHiThreshold = _BbChanClpHiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 22),
    _BbChanClpHiThreshold_Type()
)
bbChanClpHiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanClpHiThreshold.setStatus("current")


class _BbChanClpLoThreshold_Type(Integer32):
    """Custom type bbChanClpLoThreshold based on Integer32"""
    defaultValue = 131072

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 491520),
    )


_BbChanClpLoThreshold_Type.__name__ = "Integer32"
_BbChanClpLoThreshold_Object = MibTableColumn
bbChanClpLoThreshold = _BbChanClpLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 23),
    _BbChanClpLoThreshold_Type()
)
bbChanClpLoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanClpLoThreshold.setStatus("current")


class _BbChanCongstUpdateCode_Type(Integer32):
    """Custom type bbChanCongstUpdateCode based on Integer32"""
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
        *(("clearEfciBit", 4),
          ("dontUpdate", 1),
          ("setCiBit", 2),
          ("setEfciBit", 3))
    )


_BbChanCongstUpdateCode_Type.__name__ = "Integer32"
_BbChanCongstUpdateCode_Object = MibTableColumn
bbChanCongstUpdateCode = _BbChanCongstUpdateCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 24),
    _BbChanCongstUpdateCode_Type()
)
bbChanCongstUpdateCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanCongstUpdateCode.setStatus("current")


class _BbChanMaxCellMemThreshold_Type(Integer32):
    """Custom type bbChanMaxCellMemThreshold based on Integer32"""
    defaultValue = 262144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512000),
    )


_BbChanMaxCellMemThreshold_Type.__name__ = "Integer32"
_BbChanMaxCellMemThreshold_Object = MibTableColumn
bbChanMaxCellMemThreshold = _BbChanMaxCellMemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 25),
    _BbChanMaxCellMemThreshold_Type()
)
bbChanMaxCellMemThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanMaxCellMemThreshold.setStatus("current")


class _BbChanIngrPercentUtil_Type(Integer32):
    """Custom type bbChanIngrPercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BbChanIngrPercentUtil_Type.__name__ = "Integer32"
_BbChanIngrPercentUtil_Object = MibTableColumn
bbChanIngrPercentUtil = _BbChanIngrPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 26),
    _BbChanIngrPercentUtil_Type()
)
bbChanIngrPercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanIngrPercentUtil.setStatus("current")


class _BbChanEgrPercentUtil_Type(Integer32):
    """Custom type bbChanEgrPercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BbChanEgrPercentUtil_Type.__name__ = "Integer32"
_BbChanEgrPercentUtil_Object = MibTableColumn
bbChanEgrPercentUtil = _BbChanEgrPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 27),
    _BbChanEgrPercentUtil_Type()
)
bbChanEgrPercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanEgrPercentUtil.setStatus("current")


class _BbChanEgrSrvRate_Type(Integer32):
    """Custom type bbChanEgrSrvRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1412832),
    )


_BbChanEgrSrvRate_Type.__name__ = "Integer32"
_BbChanEgrSrvRate_Object = MibTableColumn
bbChanEgrSrvRate = _BbChanEgrSrvRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 28),
    _BbChanEgrSrvRate_Type()
)
bbChanEgrSrvRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanEgrSrvRate.setStatus("current")


class _BbChanOvrSubOvrRide_Type(Integer32):
    """Custom type bbChanOvrSubOvrRide based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BbChanOvrSubOvrRide_Type.__name__ = "Integer32"
_BbChanOvrSubOvrRide_Object = MibTableColumn
bbChanOvrSubOvrRide = _BbChanOvrSubOvrRide_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 29),
    _BbChanOvrSubOvrRide_Type()
)
bbChanOvrSubOvrRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanOvrSubOvrRide.setStatus("current")


class _BbChanLocalVpi_Type(Integer32):
    """Custom type bbChanLocalVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BbChanLocalVpi_Type.__name__ = "Integer32"
_BbChanLocalVpi_Object = MibTableColumn
bbChanLocalVpi = _BbChanLocalVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 30),
    _BbChanLocalVpi_Type()
)
bbChanLocalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanLocalVpi.setStatus("current")


class _BbChanLocalVci_Type(Integer32):
    """Custom type bbChanLocalVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BbChanLocalVci_Type.__name__ = "Integer32"
_BbChanLocalVci_Object = MibTableColumn
bbChanLocalVci = _BbChanLocalVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 31),
    _BbChanLocalVci_Type()
)
bbChanLocalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanLocalVci.setStatus("current")
_BbChanLocalNsapAddr_Type = IfNsapAddress
_BbChanLocalNsapAddr_Object = MibTableColumn
bbChanLocalNsapAddr = _BbChanLocalNsapAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 32),
    _BbChanLocalNsapAddr_Type()
)
bbChanLocalNsapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanLocalNsapAddr.setStatus("current")


class _BbChanRemoteVpi_Type(Integer32):
    """Custom type bbChanRemoteVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BbChanRemoteVpi_Type.__name__ = "Integer32"
_BbChanRemoteVpi_Object = MibTableColumn
bbChanRemoteVpi = _BbChanRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 33),
    _BbChanRemoteVpi_Type()
)
bbChanRemoteVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanRemoteVpi.setStatus("current")


class _BbChanRemoteVci_Type(Integer32):
    """Custom type bbChanRemoteVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BbChanRemoteVci_Type.__name__ = "Integer32"
_BbChanRemoteVci_Object = MibTableColumn
bbChanRemoteVci = _BbChanRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 34),
    _BbChanRemoteVci_Type()
)
bbChanRemoteVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanRemoteVci.setStatus("current")
_BbChanRemoteNsapAddr_Type = IfNsapAddress
_BbChanRemoteNsapAddr_Object = MibTableColumn
bbChanRemoteNsapAddr = _BbChanRemoteNsapAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 35),
    _BbChanRemoteNsapAddr_Type()
)
bbChanRemoteNsapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanRemoteNsapAddr.setStatus("current")


class _BbChanMaster_Type(Integer32):
    """Custom type bbChanMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("unknown", 3))
    )


_BbChanMaster_Type.__name__ = "Integer32"
_BbChanMaster_Object = MibTableColumn
bbChanMaster = _BbChanMaster_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 36),
    _BbChanMaster_Type()
)
bbChanMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanMaster.setStatus("current")


class _BbChanRtePriority_Type(Integer32):
    """Custom type bbChanRtePriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_BbChanRtePriority_Type.__name__ = "Integer32"
_BbChanRtePriority_Object = MibTableColumn
bbChanRtePriority = _BbChanRtePriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 37),
    _BbChanRtePriority_Type()
)
bbChanRtePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanRtePriority.setStatus("current")


class _BbChanMaxCost_Type(Integer32):
    """Custom type bbChanMaxCost based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BbChanMaxCost_Type.__name__ = "Integer32"
_BbChanMaxCost_Object = MibTableColumn
bbChanMaxCost = _BbChanMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 38),
    _BbChanMaxCost_Type()
)
bbChanMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanMaxCost.setStatus("current")


class _BbChanRestrictTrkType_Type(Integer32):
    """Custom type bbChanRestrictTrkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRestriction", 1),
          ("satelliteTrunk", 3),
          ("terrestrialTrunk", 2))
    )


_BbChanRestrictTrkType_Type.__name__ = "Integer32"
_BbChanRestrictTrkType_Object = MibTableColumn
bbChanRestrictTrkType = _BbChanRestrictTrkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 39),
    _BbChanRestrictTrkType_Type()
)
bbChanRestrictTrkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanRestrictTrkType.setStatus("current")


class _BbChanTestType_Type(Integer32):
    """Custom type bbChanTestType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notest", 3),
          ("testcon", 1),
          ("testdelay", 2))
    )


_BbChanTestType_Type.__name__ = "Integer32"
_BbChanTestType_Object = MibTableColumn
bbChanTestType = _BbChanTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 40),
    _BbChanTestType_Type()
)
bbChanTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanTestType.setStatus("current")


class _BbChanTestState_Type(Integer32):
    """Custom type bbChanTestState based on Integer32"""
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
        *(("failed", 2),
          ("inprogress", 3),
          ("notinprogress", 4),
          ("passed", 1))
    )


_BbChanTestState_Type.__name__ = "Integer32"
_BbChanTestState_Object = MibTableColumn
bbChanTestState = _BbChanTestState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 41),
    _BbChanTestState_Type()
)
bbChanTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanTestState.setStatus("current")


class _BbChanTestResult_Type(Integer32):
    """Custom type bbChanTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BbChanTestResult_Type.__name__ = "Integer32"
_BbChanTestResult_Object = MibTableColumn
bbChanTestResult = _BbChanTestResult_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 42),
    _BbChanTestResult_Type()
)
bbChanTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanTestResult.setStatus("current")
if mibBuilder.loadTexts:
    bbChanTestResult.setUnits("milliseconds")


class _BbChanTestTypeCPESide_Type(Integer32):
    """Custom type bbChanTestTypeCPESide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notest", 2),
          ("testconseg", 1))
    )


_BbChanTestTypeCPESide_Type.__name__ = "Integer32"
_BbChanTestTypeCPESide_Object = MibTableColumn
bbChanTestTypeCPESide = _BbChanTestTypeCPESide_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 43),
    _BbChanTestTypeCPESide_Type()
)
bbChanTestTypeCPESide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanTestTypeCPESide.setStatus("current")


class _BbChanTestStateCPESide_Type(Integer32):
    """Custom type bbChanTestStateCPESide based on Integer32"""
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
        *(("failed", 2),
          ("inprogress", 3),
          ("notinprogress", 4),
          ("passed", 1))
    )


_BbChanTestStateCPESide_Type.__name__ = "Integer32"
_BbChanTestStateCPESide_Object = MibTableColumn
bbChanTestStateCPESide = _BbChanTestStateCPESide_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 44),
    _BbChanTestStateCPESide_Type()
)
bbChanTestStateCPESide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanTestStateCPESide.setStatus("current")


class _BbConnVpcFlag_Type(Integer32):
    """Custom type bbConnVpcFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcc", 2),
          ("vpc", 1))
    )


_BbConnVpcFlag_Type.__name__ = "Integer32"
_BbConnVpcFlag_Object = MibTableColumn
bbConnVpcFlag = _BbConnVpcFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 45),
    _BbConnVpcFlag_Type()
)
bbConnVpcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbConnVpcFlag.setStatus("current")


class _BbConnServiceType_Type(Integer32):
    """Custom type bbConnServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("abrstd", 6),
          ("cbr", 1),
          ("ubr", 4),
          ("vbr", 2),
          ("vbrrt", 8))
    )


_BbConnServiceType_Type.__name__ = "Integer32"
_BbConnServiceType_Object = MibTableColumn
bbConnServiceType = _BbConnServiceType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 46),
    _BbConnServiceType_Type()
)
bbConnServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbConnServiceType.setStatus("current")
_BbConnPCR_Type = Integer32
_BbConnPCR_Object = MibTableColumn
bbConnPCR = _BbConnPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 47),
    _BbConnPCR_Type()
)
bbConnPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbConnPCR.setStatus("current")
_BbConnSCR_Type = Integer32
_BbConnSCR_Object = MibTableColumn
bbConnSCR = _BbConnSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 48),
    _BbConnSCR_Type()
)
bbConnSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbConnSCR.setStatus("current")


class _BbConnPercentUtil_Type(Integer32):
    """Custom type bbConnPercentUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BbConnPercentUtil_Type.__name__ = "Integer32"
_BbConnPercentUtil_Object = MibTableColumn
bbConnPercentUtil = _BbConnPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 49),
    _BbConnPercentUtil_Type()
)
bbConnPercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbConnPercentUtil.setStatus("current")
_BbRemoteConnPCR_Type = Integer32
_BbRemoteConnPCR_Object = MibTableColumn
bbRemoteConnPCR = _BbRemoteConnPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 50),
    _BbRemoteConnPCR_Type()
)
bbRemoteConnPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbRemoteConnPCR.setStatus("current")
_BbRemoteConnSCR_Type = Integer32
_BbRemoteConnSCR_Object = MibTableColumn
bbRemoteConnSCR = _BbRemoteConnSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 51),
    _BbRemoteConnSCR_Type()
)
bbRemoteConnSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbRemoteConnSCR.setStatus("current")


class _BbRemoteConnPercentUtil_Type(Integer32):
    """Custom type bbRemoteConnPercentUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BbRemoteConnPercentUtil_Type.__name__ = "Integer32"
_BbRemoteConnPercentUtil_Object = MibTableColumn
bbRemoteConnPercentUtil = _BbRemoteConnPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 52),
    _BbRemoteConnPercentUtil_Type()
)
bbRemoteConnPercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbRemoteConnPercentUtil.setStatus("current")


class _BbChanUpcMCR_Type(Integer32):
    """Custom type bbChanUpcMCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1412832),
    )


_BbChanUpcMCR_Type.__name__ = "Integer32"
_BbChanUpcMCR_Object = MibTableColumn
bbChanUpcMCR = _BbChanUpcMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 1, 1, 53),
    _BbChanUpcMCR_Type()
)
bbChanUpcMCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbChanUpcMCR.setStatus("current")


class _BbChanNumNextAvailable_Type(Integer32):
    """Custom type bbChanNumNextAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4111),
    )


_BbChanNumNextAvailable_Type.__name__ = "Integer32"
_BbChanNumNextAvailable_Object = MibScalar
bbChanNumNextAvailable = _BbChanNumNextAvailable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 2),
    _BbChanNumNextAvailable_Type()
)
bbChanNumNextAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanNumNextAvailable.setStatus("current")


class _BbChanVpIdNextAvailable_Type(Integer32):
    """Custom type bbChanVpIdNextAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_BbChanVpIdNextAvailable_Type.__name__ = "Integer32"
_BbChanVpIdNextAvailable_Object = MibScalar
bbChanVpIdNextAvailable = _BbChanVpIdNextAvailable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1, 3),
    _BbChanVpIdNextAvailable_Type()
)
bbChanVpIdNextAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanVpIdNextAvailable.setStatus("current")
_BbChanStateGrpTable_Object = MibTable
bbChanStateGrpTable = _BbChanStateGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    bbChanStateGrpTable.setStatus("current")
_BbChanStateGrpEntry_Object = MibTableRow
bbChanStateGrpEntry = _BbChanStateGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 2, 1, 1)
)
bbChanStateGrpEntry.setIndexNames(
    (0, "CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanStateNum"),
)
if mibBuilder.loadTexts:
    bbChanStateGrpEntry.setStatus("current")


class _BbChanStateNum_Type(Integer32):
    """Custom type bbChanStateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4111),
    )


_BbChanStateNum_Type.__name__ = "Integer32"
_BbChanStateNum_Object = MibTableColumn
bbChanStateNum = _BbChanStateNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 2, 1, 1, 1),
    _BbChanStateNum_Type()
)
bbChanStateNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanStateNum.setStatus("current")


class _BbChanState_Type(Integer32):
    """Custom type bbChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("normal", 2),
          ("notconfigured", 1))
    )


_BbChanState_Type.__name__ = "Integer32"
_BbChanState_Object = MibTableColumn
bbChanState = _BbChanState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 2, 1, 1, 2),
    _BbChanState_Type()
)
bbChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanState.setStatus("current")


class _BbChanEgrXmtState_Type(Integer32):
    """Custom type bbChanEgrXmtState based on Integer32"""
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
        *(("normal", 2),
          ("other", 1),
          ("sendingAis", 3),
          ("sendingFerf", 4))
    )


_BbChanEgrXmtState_Type.__name__ = "Integer32"
_BbChanEgrXmtState_Object = MibTableColumn
bbChanEgrXmtState = _BbChanEgrXmtState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 2, 1, 1, 3),
    _BbChanEgrXmtState_Type()
)
bbChanEgrXmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanEgrXmtState.setStatus("current")


class _BbChanIngrRcvState_Type(Integer32):
    """Custom type bbChanIngrRcvState based on Integer32"""
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
        *(("alarm", 5),
          ("normal", 2),
          ("other", 1),
          ("receivingAis", 3),
          ("receivingFerf", 4))
    )


_BbChanIngrRcvState_Type.__name__ = "Integer32"
_BbChanIngrRcvState_Object = MibTableColumn
bbChanIngrRcvState = _BbChanIngrRcvState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 2, 1, 1, 4),
    _BbChanIngrRcvState_Type()
)
bbChanIngrRcvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbChanIngrRcvState.setStatus("current")
_CwbAtmConnMIBConformance_ObjectIdentity = ObjectIdentity
cwbAtmConnMIBConformance = _CwbAtmConnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 35, 2)
)
_CwbAtmConnMIBGroups_ObjectIdentity = ObjectIdentity
cwbAtmConnMIBGroups = _CwbAtmConnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 35, 2, 1)
)
_CwbAtmConnMIBCompliances_ObjectIdentity = ObjectIdentity
cwbAtmConnMIBCompliances = _CwbAtmConnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 35, 2, 2)
)

# Managed Objects groups

cwbAtmConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 35, 2, 1, 1)
)
cwbAtmConnGroup.setObjects(
      *(("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanCnfNum"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanRowStatus"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanConnType"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanServiceType"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanConnDesc"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanSvcFlag"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanSvcConnId"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanIfNum"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanVpi"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanVci"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanUpcEnable"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanUpcPCR"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanUpcCDVT"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanUpcSCR"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanUpcMBS"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanGcra1Action"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanGcra2Action"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanUpcSCRPolicing"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanEfciThreshold"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanDiscardOption"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanFrmDiscardThreshold"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanClpHiThreshold"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanClpLoThreshold"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanCongstUpdateCode"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanMaxCellMemThreshold"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanIngrPercentUtil"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanEgrPercentUtil"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanEgrSrvRate"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanOvrSubOvrRide"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanLocalVpi"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanLocalVci"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanLocalNsapAddr"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanRemoteVpi"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanRemoteVci"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanRemoteNsapAddr"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanMaster"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanRtePriority"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanMaxCost"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanRestrictTrkType"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanTestType"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanTestState"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanTestResult"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanTestTypeCPESide"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanTestStateCPESide"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbConnVpcFlag"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbConnServiceType"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbConnPCR"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbConnSCR"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbConnPercentUtil"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbRemoteConnPCR"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbRemoteConnSCR"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbRemoteConnPercentUtil"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanUpcMCR"))
)
if mibBuilder.loadTexts:
    cwbAtmConnGroup.setStatus("current")

cwbAtmConnStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 35, 2, 1, 2)
)
cwbAtmConnStateGroup.setObjects(
      *(("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanStateNum"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanState"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanEgrXmtState"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanIngrRcvState"))
)
if mibBuilder.loadTexts:
    cwbAtmConnStateGroup.setStatus("current")

cwbAtmConnGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 35, 2, 1, 3)
)
cwbAtmConnGeneralGroup.setObjects(
      *(("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanNumNextAvailable"),
        ("CISCO-WAN-BBIF-ATM-CONN-MIB", "bbChanVpIdNextAvailable"))
)
if mibBuilder.loadTexts:
    cwbAtmConnGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwbAtmConnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 35, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cwbAtmConnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-BBIF-ATM-CONN-MIB",
    **{"IfNsapAddress": IfNsapAddress,
       "bbChanCnfGrpTable": bbChanCnfGrpTable,
       "bbChanCnfGrpEntry": bbChanCnfGrpEntry,
       "bbChanCnfNum": bbChanCnfNum,
       "bbChanRowStatus": bbChanRowStatus,
       "bbChanConnType": bbChanConnType,
       "bbChanServiceType": bbChanServiceType,
       "bbChanConnDesc": bbChanConnDesc,
       "bbChanSvcFlag": bbChanSvcFlag,
       "bbChanSvcConnId": bbChanSvcConnId,
       "bbChanIfNum": bbChanIfNum,
       "bbChanVpi": bbChanVpi,
       "bbChanVci": bbChanVci,
       "bbChanUpcEnable": bbChanUpcEnable,
       "bbChanUpcPCR": bbChanUpcPCR,
       "bbChanUpcCDVT": bbChanUpcCDVT,
       "bbChanUpcSCR": bbChanUpcSCR,
       "bbChanUpcMBS": bbChanUpcMBS,
       "bbChanGcra1Action": bbChanGcra1Action,
       "bbChanGcra2Action": bbChanGcra2Action,
       "bbChanUpcSCRPolicing": bbChanUpcSCRPolicing,
       "bbChanEfciThreshold": bbChanEfciThreshold,
       "bbChanDiscardOption": bbChanDiscardOption,
       "bbChanFrmDiscardThreshold": bbChanFrmDiscardThreshold,
       "bbChanClpHiThreshold": bbChanClpHiThreshold,
       "bbChanClpLoThreshold": bbChanClpLoThreshold,
       "bbChanCongstUpdateCode": bbChanCongstUpdateCode,
       "bbChanMaxCellMemThreshold": bbChanMaxCellMemThreshold,
       "bbChanIngrPercentUtil": bbChanIngrPercentUtil,
       "bbChanEgrPercentUtil": bbChanEgrPercentUtil,
       "bbChanEgrSrvRate": bbChanEgrSrvRate,
       "bbChanOvrSubOvrRide": bbChanOvrSubOvrRide,
       "bbChanLocalVpi": bbChanLocalVpi,
       "bbChanLocalVci": bbChanLocalVci,
       "bbChanLocalNsapAddr": bbChanLocalNsapAddr,
       "bbChanRemoteVpi": bbChanRemoteVpi,
       "bbChanRemoteVci": bbChanRemoteVci,
       "bbChanRemoteNsapAddr": bbChanRemoteNsapAddr,
       "bbChanMaster": bbChanMaster,
       "bbChanRtePriority": bbChanRtePriority,
       "bbChanMaxCost": bbChanMaxCost,
       "bbChanRestrictTrkType": bbChanRestrictTrkType,
       "bbChanTestType": bbChanTestType,
       "bbChanTestState": bbChanTestState,
       "bbChanTestResult": bbChanTestResult,
       "bbChanTestTypeCPESide": bbChanTestTypeCPESide,
       "bbChanTestStateCPESide": bbChanTestStateCPESide,
       "bbConnVpcFlag": bbConnVpcFlag,
       "bbConnServiceType": bbConnServiceType,
       "bbConnPCR": bbConnPCR,
       "bbConnSCR": bbConnSCR,
       "bbConnPercentUtil": bbConnPercentUtil,
       "bbRemoteConnPCR": bbRemoteConnPCR,
       "bbRemoteConnSCR": bbRemoteConnSCR,
       "bbRemoteConnPercentUtil": bbRemoteConnPercentUtil,
       "bbChanUpcMCR": bbChanUpcMCR,
       "bbChanNumNextAvailable": bbChanNumNextAvailable,
       "bbChanVpIdNextAvailable": bbChanVpIdNextAvailable,
       "bbChanStateGrpTable": bbChanStateGrpTable,
       "bbChanStateGrpEntry": bbChanStateGrpEntry,
       "bbChanStateNum": bbChanStateNum,
       "bbChanState": bbChanState,
       "bbChanEgrXmtState": bbChanEgrXmtState,
       "bbChanIngrRcvState": bbChanIngrRcvState,
       "ciscoWanBbifAtmConnMIB": ciscoWanBbifAtmConnMIB,
       "cwbAtmConnMIBConformance": cwbAtmConnMIBConformance,
       "cwbAtmConnMIBGroups": cwbAtmConnMIBGroups,
       "cwbAtmConnGroup": cwbAtmConnGroup,
       "cwbAtmConnStateGroup": cwbAtmConnStateGroup,
       "cwbAtmConnGeneralGroup": cwbAtmConnGeneralGroup,
       "cwbAtmConnMIBCompliances": cwbAtmConnMIBCompliances,
       "cwbAtmConnCompliance": cwbAtmConnCompliance}
)
