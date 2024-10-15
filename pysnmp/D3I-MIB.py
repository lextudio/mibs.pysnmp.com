# SNMP MIB module (D3I-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/D3I-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:51 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_D3i_ObjectIdentity = ObjectIdentity
d3i = _D3i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 43)
)
_D3iID_ObjectIdentity = ObjectIdentity
d3iID = _D3iID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 1)
)
_D3iIDTable_Object = MibTable
d3iIDTable = _D3iIDTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1)
)
if mibBuilder.loadTexts:
    d3iIDTable.setStatus("mandatory")
_D3iIDEntry_Object = MibTableRow
d3iIDEntry = _D3iIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1)
)
d3iIDEntry.setIndexNames(
    (0, "D3I-MIB", "d3iIDIndex"),
)
if mibBuilder.loadTexts:
    d3iIDEntry.setStatus("mandatory")
_D3iIDIndex_Type = Integer32
_D3iIDIndex_Object = MibTableColumn
d3iIDIndex = _D3iIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 1),
    _D3iIDIndex_Type()
)
d3iIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iIDIndex.setStatus("mandatory")


class _D3iIDNACHardwareSerNum_Type(DisplayString):
    """Custom type d3iIDNACHardwareSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_D3iIDNACHardwareSerNum_Type.__name__ = "DisplayString"
_D3iIDNACHardwareSerNum_Object = MibTableColumn
d3iIDNACHardwareSerNum = _D3iIDNACHardwareSerNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 2),
    _D3iIDNACHardwareSerNum_Type()
)
d3iIDNACHardwareSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iIDNACHardwareSerNum.setStatus("mandatory")


class _D3iIDNICHardwareSerNum_Type(DisplayString):
    """Custom type d3iIDNICHardwareSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_D3iIDNICHardwareSerNum_Type.__name__ = "DisplayString"
_D3iIDNICHardwareSerNum_Object = MibTableColumn
d3iIDNICHardwareSerNum = _D3iIDNICHardwareSerNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 3),
    _D3iIDNICHardwareSerNum_Type()
)
d3iIDNICHardwareSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iIDNICHardwareSerNum.setStatus("mandatory")


class _D3iIDNACHardwareRev_Type(DisplayString):
    """Custom type d3iIDNACHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_D3iIDNACHardwareRev_Type.__name__ = "DisplayString"
_D3iIDNACHardwareRev_Object = MibTableColumn
d3iIDNACHardwareRev = _D3iIDNACHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 4),
    _D3iIDNACHardwareRev_Type()
)
d3iIDNACHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iIDNACHardwareRev.setStatus("mandatory")


class _D3iIDNICHardwareRev_Type(DisplayString):
    """Custom type d3iIDNICHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_D3iIDNICHardwareRev_Type.__name__ = "DisplayString"
_D3iIDNICHardwareRev_Object = MibTableColumn
d3iIDNICHardwareRev = _D3iIDNICHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 5),
    _D3iIDNICHardwareRev_Type()
)
d3iIDNICHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iIDNICHardwareRev.setStatus("mandatory")


class _D3iIDBoardManagerSwRev_Type(DisplayString):
    """Custom type d3iIDBoardManagerSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_D3iIDBoardManagerSwRev_Type.__name__ = "DisplayString"
_D3iIDBoardManagerSwRev_Object = MibTableColumn
d3iIDBoardManagerSwRev = _D3iIDBoardManagerSwRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 6),
    _D3iIDBoardManagerSwRev_Type()
)
d3iIDBoardManagerSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iIDBoardManagerSwRev.setStatus("mandatory")


class _D3iIDBoardManagerDate_Type(DisplayString):
    """Custom type d3iIDBoardManagerDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_D3iIDBoardManagerDate_Type.__name__ = "DisplayString"
_D3iIDBoardManagerDate_Object = MibTableColumn
d3iIDBoardManagerDate = _D3iIDBoardManagerDate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 1, 1, 1, 7),
    _D3iIDBoardManagerDate_Type()
)
d3iIDBoardManagerDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iIDBoardManagerDate.setStatus("mandatory")
_D3iCfg_ObjectIdentity = ObjectIdentity
d3iCfg = _D3iCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 2)
)
_D3iCfgTable_Object = MibTable
d3iCfgTable = _D3iCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1)
)
if mibBuilder.loadTexts:
    d3iCfgTable.setStatus("mandatory")
_D3iCfgEntry_Object = MibTableRow
d3iCfgEntry = _D3iCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1)
)
d3iCfgEntry.setIndexNames(
    (0, "D3I-MIB", "d3iCfgIndex"),
)
if mibBuilder.loadTexts:
    d3iCfgEntry.setStatus("mandatory")
_D3iCfgIndex_Type = Integer32
_D3iCfgIndex_Object = MibTableColumn
d3iCfgIndex = _D3iCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1, 1),
    _D3iCfgIndex_Type()
)
d3iCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iCfgIndex.setStatus("mandatory")


class _D3iCfgPrimaryTimeSource_Type(Integer32):
    """Custom type d3iCfgPrimaryTimeSource based on Integer32"""
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
              128,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("internal", 129),
          ("span1", 1),
          ("span10", 10),
          ("span11", 11),
          ("span12", 12),
          ("span13", 13),
          ("span14", 14),
          ("span15", 15),
          ("span16", 16),
          ("span17", 17),
          ("span18", 18),
          ("span19", 19),
          ("span2", 2),
          ("span20", 20),
          ("span21", 21),
          ("span22", 22),
          ("span23", 23),
          ("span24", 24),
          ("span25", 25),
          ("span26", 26),
          ("span27", 27),
          ("span28", 28),
          ("span3", 3),
          ("span4", 4),
          ("span5", 5),
          ("span6", 6),
          ("span7", 7),
          ("span8", 8),
          ("span9", 9),
          ("spanBITS", 128),
          ("throughTDM", 130))
    )


_D3iCfgPrimaryTimeSource_Type.__name__ = "Integer32"
_D3iCfgPrimaryTimeSource_Object = MibTableColumn
d3iCfgPrimaryTimeSource = _D3iCfgPrimaryTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1, 2),
    _D3iCfgPrimaryTimeSource_Type()
)
d3iCfgPrimaryTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iCfgPrimaryTimeSource.setStatus("mandatory")


class _D3iCfgSecondaryTimeSource_Type(Integer32):
    """Custom type d3iCfgSecondaryTimeSource based on Integer32"""
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
              128,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("internal", 129),
          ("span1", 1),
          ("span10", 10),
          ("span11", 11),
          ("span12", 12),
          ("span13", 13),
          ("span14", 14),
          ("span15", 15),
          ("span16", 16),
          ("span17", 17),
          ("span18", 18),
          ("span19", 19),
          ("span2", 2),
          ("span20", 20),
          ("span21", 21),
          ("span22", 22),
          ("span23", 23),
          ("span24", 24),
          ("span25", 25),
          ("span26", 26),
          ("span27", 27),
          ("span28", 28),
          ("span3", 3),
          ("span4", 4),
          ("span5", 5),
          ("span6", 6),
          ("span7", 7),
          ("span8", 8),
          ("span9", 9),
          ("spanBITS", 128),
          ("throughTDM", 130))
    )


_D3iCfgSecondaryTimeSource_Type.__name__ = "Integer32"
_D3iCfgSecondaryTimeSource_Object = MibTableColumn
d3iCfgSecondaryTimeSource = _D3iCfgSecondaryTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1, 3),
    _D3iCfgSecondaryTimeSource_Type()
)
d3iCfgSecondaryTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iCfgSecondaryTimeSource.setStatus("mandatory")


class _D3iCfgTimeSourceSwitchMode_Type(Integer32):
    """Custom type d3iCfgTimeSourceSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_D3iCfgTimeSourceSwitchMode_Type.__name__ = "Integer32"
_D3iCfgTimeSourceSwitchMode_Object = MibTableColumn
d3iCfgTimeSourceSwitchMode = _D3iCfgTimeSourceSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1, 4),
    _D3iCfgTimeSourceSwitchMode_Type()
)
d3iCfgTimeSourceSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iCfgTimeSourceSwitchMode.setStatus("mandatory")


class _D3iCfgCLIPromptName_Type(DisplayString):
    """Custom type d3iCfgCLIPromptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_D3iCfgCLIPromptName_Type.__name__ = "DisplayString"
_D3iCfgCLIPromptName_Object = MibTableColumn
d3iCfgCLIPromptName = _D3iCfgCLIPromptName_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 2, 1, 1, 5),
    _D3iCfgCLIPromptName_Type()
)
d3iCfgCLIPromptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iCfgCLIPromptName.setStatus("mandatory")
_D3iStat_ObjectIdentity = ObjectIdentity
d3iStat = _D3iStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3)
)
_D3iStatTable_Object = MibTable
d3iStatTable = _D3iStatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1)
)
if mibBuilder.loadTexts:
    d3iStatTable.setStatus("mandatory")
_D3iStatEntry_Object = MibTableRow
d3iStatEntry = _D3iStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1)
)
d3iStatEntry.setIndexNames(
    (0, "D3I-MIB", "d3iStatIndex"),
)
if mibBuilder.loadTexts:
    d3iStatEntry.setStatus("mandatory")
_D3iStatIndex_Type = Integer32
_D3iStatIndex_Object = MibTableColumn
d3iStatIndex = _D3iStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 1),
    _D3iStatIndex_Type()
)
d3iStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iStatIndex.setStatus("mandatory")
_D3iStatSigPBusTxPktOkCnt_Type = Counter32
_D3iStatSigPBusTxPktOkCnt_Object = MibTableColumn
d3iStatSigPBusTxPktOkCnt = _D3iStatSigPBusTxPktOkCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 2),
    _D3iStatSigPBusTxPktOkCnt_Type()
)
d3iStatSigPBusTxPktOkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iStatSigPBusTxPktOkCnt.setStatus("mandatory")
_D3iStatSigPBusTxPktFldCnt_Type = Counter32
_D3iStatSigPBusTxPktFldCnt_Object = MibTableColumn
d3iStatSigPBusTxPktFldCnt = _D3iStatSigPBusTxPktFldCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 3),
    _D3iStatSigPBusTxPktFldCnt_Type()
)
d3iStatSigPBusTxPktFldCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iStatSigPBusTxPktFldCnt.setStatus("mandatory")
_D3iStatSigPBusRxPktOkCnt_Type = Counter32
_D3iStatSigPBusRxPktOkCnt_Object = MibTableColumn
d3iStatSigPBusRxPktOkCnt = _D3iStatSigPBusRxPktOkCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 4),
    _D3iStatSigPBusRxPktOkCnt_Type()
)
d3iStatSigPBusRxPktOkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iStatSigPBusRxPktOkCnt.setStatus("mandatory")
_D3iStatSigPBusRxPktRjtCnt_Type = Counter32
_D3iStatSigPBusRxPktRjtCnt_Object = MibTableColumn
d3iStatSigPBusRxPktRjtCnt = _D3iStatSigPBusRxPktRjtCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 5),
    _D3iStatSigPBusRxPktRjtCnt_Type()
)
d3iStatSigPBusRxPktRjtCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iStatSigPBusRxPktRjtCnt.setStatus("mandatory")


class _D3iStatSigPBusConnState_Type(Integer32):
    """Custom type d3iStatSigPBusConnState based on Integer32"""
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
        *(("closed", 1),
          ("closing", 6),
          ("configuring", 4),
          ("loopback", 7),
          ("opened", 3),
          ("opening", 2),
          ("ready", 5))
    )


_D3iStatSigPBusConnState_Type.__name__ = "Integer32"
_D3iStatSigPBusConnState_Object = MibTableColumn
d3iStatSigPBusConnState = _D3iStatSigPBusConnState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 6),
    _D3iStatSigPBusConnState_Type()
)
d3iStatSigPBusConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iStatSigPBusConnState.setStatus("mandatory")


class _D3iStatEnfasLinkDownCause_Type(Integer32):
    """Custom type d3iStatEnfasLinkDownCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discCmd", 2),
          ("nacRemoval", 3),
          ("none", 1))
    )


_D3iStatEnfasLinkDownCause_Type.__name__ = "Integer32"
_D3iStatEnfasLinkDownCause_Object = MibTableColumn
d3iStatEnfasLinkDownCause = _D3iStatEnfasLinkDownCause_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 7),
    _D3iStatEnfasLinkDownCause_Type()
)
d3iStatEnfasLinkDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iStatEnfasLinkDownCause.setStatus("mandatory")


class _D3iStatPbClock_Type(Integer32):
    """Custom type d3iStatPbClock based on Integer32"""
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
        *(("clockMaster", 2),
          ("clockSlave", 3),
          ("noClockPresent", 4),
          ("notSupported", 1))
    )


_D3iStatPbClock_Type.__name__ = "Integer32"
_D3iStatPbClock_Object = MibTableColumn
d3iStatPbClock = _D3iStatPbClock_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 8),
    _D3iStatPbClock_Type()
)
d3iStatPbClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iStatPbClock.setStatus("mandatory")


class _D3iStatTdmClock_Type(Integer32):
    """Custom type d3iStatTdmClock based on Integer32"""
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
        *(("clockMaster", 2),
          ("clockSlave", 3),
          ("noClockPresent", 4),
          ("notSupported", 1))
    )


_D3iStatTdmClock_Type.__name__ = "Integer32"
_D3iStatTdmClock_Object = MibTableColumn
d3iStatTdmClock = _D3iStatTdmClock_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 3, 1, 1, 9),
    _D3iStatTdmClock_Type()
)
d3iStatTdmClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iStatTdmClock.setStatus("mandatory")
_D3iCmd_ObjectIdentity = ObjectIdentity
d3iCmd = _D3iCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4)
)
_D3iCmdTable_Object = MibTable
d3iCmdTable = _D3iCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1)
)
if mibBuilder.loadTexts:
    d3iCmdTable.setStatus("mandatory")
_D3iCmdEntry_Object = MibTableRow
d3iCmdEntry = _D3iCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1)
)
d3iCmdEntry.setIndexNames(
    (0, "D3I-MIB", "d3iCmdIndex"),
)
if mibBuilder.loadTexts:
    d3iCmdEntry.setStatus("mandatory")
_D3iCmdIndex_Type = Integer32
_D3iCmdIndex_Object = MibTableColumn
d3iCmdIndex = _D3iCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 1),
    _D3iCmdIndex_Type()
)
d3iCmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iCmdIndex.setStatus("mandatory")


class _D3iCmdMgtStationId_Type(OctetString):
    """Custom type d3iCmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_D3iCmdMgtStationId_Type.__name__ = "OctetString"
_D3iCmdMgtStationId_Object = MibTableColumn
d3iCmdMgtStationId = _D3iCmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 2),
    _D3iCmdMgtStationId_Type()
)
d3iCmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iCmdMgtStationId.setStatus("mandatory")
_D3iCmdReqId_Type = Integer32
_D3iCmdReqId_Object = MibTableColumn
d3iCmdReqId = _D3iCmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 3),
    _D3iCmdReqId_Type()
)
d3iCmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iCmdReqId.setStatus("mandatory")


class _D3iCmdFunction_Type(Integer32):
    """Custom type d3iCmdFunction based on Integer32"""
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
        *(("d3iNICReset", 7),
          ("d3iNICResetHold", 8),
          ("noCommand", 1),
          ("restoreCfgFromDefaults", 5),
          ("restoreCfgFromNvram", 2),
          ("restoreDefaultUIPassword", 4),
          ("saveCfgtoNvram", 6),
          ("softwareReset", 3))
    )


_D3iCmdFunction_Type.__name__ = "Integer32"
_D3iCmdFunction_Object = MibTableColumn
d3iCmdFunction = _D3iCmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 4),
    _D3iCmdFunction_Type()
)
d3iCmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iCmdFunction.setStatus("mandatory")


class _D3iCmdForce_Type(Integer32):
    """Custom type d3iCmdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("noForce", 2))
    )


_D3iCmdForce_Type.__name__ = "Integer32"
_D3iCmdForce_Object = MibTableColumn
d3iCmdForce = _D3iCmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 5),
    _D3iCmdForce_Type()
)
d3iCmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iCmdForce.setStatus("mandatory")


class _D3iCmdParam_Type(OctetString):
    """Custom type d3iCmdParam based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_D3iCmdParam_Type.__name__ = "OctetString"
_D3iCmdParam_Object = MibTableColumn
d3iCmdParam = _D3iCmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 6),
    _D3iCmdParam_Type()
)
d3iCmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iCmdParam.setStatus("mandatory")


class _D3iCmdResult_Type(Integer32):
    """Custom type d3iCmdResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_D3iCmdResult_Type.__name__ = "Integer32"
_D3iCmdResult_Object = MibTableColumn
d3iCmdResult = _D3iCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 7),
    _D3iCmdResult_Type()
)
d3iCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iCmdResult.setStatus("mandatory")


class _D3iCmdCode_Type(Integer32):
    """Custom type d3iCmdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(58,
              73)
        )
    )
    namedValues = NamedValues(
        *(("pendingSoftwareDownload", 73),
          ("userInterfaceActive", 58))
    )


_D3iCmdCode_Type.__name__ = "Integer32"
_D3iCmdCode_Object = MibTableColumn
d3iCmdCode = _D3iCmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 4, 1, 1, 8),
    _D3iCmdCode_Type()
)
d3iCmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iCmdCode.setStatus("mandatory")
_D3iTe_ObjectIdentity = ObjectIdentity
d3iTe = _D3iTe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5)
)
_D3iTeTable_Object = MibTable
d3iTeTable = _D3iTeTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1)
)
if mibBuilder.loadTexts:
    d3iTeTable.setStatus("mandatory")
_D3iTeEntry_Object = MibTableRow
d3iTeEntry = _D3iTeEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1)
)
d3iTeEntry.setIndexNames(
    (0, "D3I-MIB", "d3iTeIndex"),
)
if mibBuilder.loadTexts:
    d3iTeEntry.setStatus("mandatory")
_D3iTeIndex_Type = Integer32
_D3iTeIndex_Object = MibTableColumn
d3iTeIndex = _D3iTeIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 1),
    _D3iTeIndex_Type()
)
d3iTeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3iTeIndex.setStatus("mandatory")


class _D3iTePbActive_Type(Integer32):
    """Custom type d3iTePbActive based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_D3iTePbActive_Type.__name__ = "Integer32"
_D3iTePbActive_Object = MibTableColumn
d3iTePbActive = _D3iTePbActive_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 2),
    _D3iTePbActive_Type()
)
d3iTePbActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iTePbActive.setStatus("mandatory")


class _D3iTePbLost_Type(Integer32):
    """Custom type d3iTePbLost based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_D3iTePbLost_Type.__name__ = "Integer32"
_D3iTePbLost_Object = MibTableColumn
d3iTePbLost = _D3iTePbLost_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 3),
    _D3iTePbLost_Type()
)
d3iTePbLost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iTePbLost.setStatus("mandatory")


class _D3iTePbClockLossEvent_Type(Integer32):
    """Custom type d3iTePbClockLossEvent based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_D3iTePbClockLossEvent_Type.__name__ = "Integer32"
_D3iTePbClockLossEvent_Object = MibTableColumn
d3iTePbClockLossEvent = _D3iTePbClockLossEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 4),
    _D3iTePbClockLossEvent_Type()
)
d3iTePbClockLossEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iTePbClockLossEvent.setStatus("mandatory")


class _D3iTePbClockRestoreEvent_Type(Integer32):
    """Custom type d3iTePbClockRestoreEvent based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_D3iTePbClockRestoreEvent_Type.__name__ = "Integer32"
_D3iTePbClockRestoreEvent_Object = MibTableColumn
d3iTePbClockRestoreEvent = _D3iTePbClockRestoreEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 5),
    _D3iTePbClockRestoreEvent_Type()
)
d3iTePbClockRestoreEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iTePbClockRestoreEvent.setStatus("mandatory")


class _D3iTeTdmClockLost_Type(Integer32):
    """Custom type d3iTeTdmClockLost based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_D3iTeTdmClockLost_Type.__name__ = "Integer32"
_D3iTeTdmClockLost_Object = MibTableColumn
d3iTeTdmClockLost = _D3iTeTdmClockLost_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 6),
    _D3iTeTdmClockLost_Type()
)
d3iTeTdmClockLost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iTeTdmClockLost.setStatus("mandatory")


class _D3iTeTdmClockRestored_Type(Integer32):
    """Custom type d3iTeTdmClockRestored based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_D3iTeTdmClockRestored_Type.__name__ = "Integer32"
_D3iTeTdmClockRestored_Object = MibTableColumn
d3iTeTdmClockRestored = _D3iTeTdmClockRestored_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 7),
    _D3iTeTdmClockRestored_Type()
)
d3iTeTdmClockRestored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iTeTdmClockRestored.setStatus("mandatory")


class _D3iTeEnfasLinkUp_Type(Integer32):
    """Custom type d3iTeEnfasLinkUp based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_D3iTeEnfasLinkUp_Type.__name__ = "Integer32"
_D3iTeEnfasLinkUp_Object = MibTableColumn
d3iTeEnfasLinkUp = _D3iTeEnfasLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 8),
    _D3iTeEnfasLinkUp_Type()
)
d3iTeEnfasLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iTeEnfasLinkUp.setStatus("mandatory")


class _D3iTeEnfasLinkDown_Type(Integer32):
    """Custom type d3iTeEnfasLinkDown based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_D3iTeEnfasLinkDown_Type.__name__ = "Integer32"
_D3iTeEnfasLinkDown_Object = MibTableColumn
d3iTeEnfasLinkDown = _D3iTeEnfasLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 9),
    _D3iTeEnfasLinkDown_Type()
)
d3iTeEnfasLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iTeEnfasLinkDown.setStatus("mandatory")


class _D3iTeSystemReset_Type(Integer32):
    """Custom type d3iTeSystemReset based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_D3iTeSystemReset_Type.__name__ = "Integer32"
_D3iTeSystemReset_Object = MibTableColumn
d3iTeSystemReset = _D3iTeSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 43, 5, 1, 1, 10),
    _D3iTeSystemReset_Type()
)
d3iTeSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d3iTeSystemReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "D3I-MIB",
    **{"usr": usr,
       "nas": nas,
       "d3i": d3i,
       "d3iID": d3iID,
       "d3iIDTable": d3iIDTable,
       "d3iIDEntry": d3iIDEntry,
       "d3iIDIndex": d3iIDIndex,
       "d3iIDNACHardwareSerNum": d3iIDNACHardwareSerNum,
       "d3iIDNICHardwareSerNum": d3iIDNICHardwareSerNum,
       "d3iIDNACHardwareRev": d3iIDNACHardwareRev,
       "d3iIDNICHardwareRev": d3iIDNICHardwareRev,
       "d3iIDBoardManagerSwRev": d3iIDBoardManagerSwRev,
       "d3iIDBoardManagerDate": d3iIDBoardManagerDate,
       "d3iCfg": d3iCfg,
       "d3iCfgTable": d3iCfgTable,
       "d3iCfgEntry": d3iCfgEntry,
       "d3iCfgIndex": d3iCfgIndex,
       "d3iCfgPrimaryTimeSource": d3iCfgPrimaryTimeSource,
       "d3iCfgSecondaryTimeSource": d3iCfgSecondaryTimeSource,
       "d3iCfgTimeSourceSwitchMode": d3iCfgTimeSourceSwitchMode,
       "d3iCfgCLIPromptName": d3iCfgCLIPromptName,
       "d3iStat": d3iStat,
       "d3iStatTable": d3iStatTable,
       "d3iStatEntry": d3iStatEntry,
       "d3iStatIndex": d3iStatIndex,
       "d3iStatSigPBusTxPktOkCnt": d3iStatSigPBusTxPktOkCnt,
       "d3iStatSigPBusTxPktFldCnt": d3iStatSigPBusTxPktFldCnt,
       "d3iStatSigPBusRxPktOkCnt": d3iStatSigPBusRxPktOkCnt,
       "d3iStatSigPBusRxPktRjtCnt": d3iStatSigPBusRxPktRjtCnt,
       "d3iStatSigPBusConnState": d3iStatSigPBusConnState,
       "d3iStatEnfasLinkDownCause": d3iStatEnfasLinkDownCause,
       "d3iStatPbClock": d3iStatPbClock,
       "d3iStatTdmClock": d3iStatTdmClock,
       "d3iCmd": d3iCmd,
       "d3iCmdTable": d3iCmdTable,
       "d3iCmdEntry": d3iCmdEntry,
       "d3iCmdIndex": d3iCmdIndex,
       "d3iCmdMgtStationId": d3iCmdMgtStationId,
       "d3iCmdReqId": d3iCmdReqId,
       "d3iCmdFunction": d3iCmdFunction,
       "d3iCmdForce": d3iCmdForce,
       "d3iCmdParam": d3iCmdParam,
       "d3iCmdResult": d3iCmdResult,
       "d3iCmdCode": d3iCmdCode,
       "d3iTe": d3iTe,
       "d3iTeTable": d3iTeTable,
       "d3iTeEntry": d3iTeEntry,
       "d3iTeIndex": d3iTeIndex,
       "d3iTePbActive": d3iTePbActive,
       "d3iTePbLost": d3iTePbLost,
       "d3iTePbClockLossEvent": d3iTePbClockLossEvent,
       "d3iTePbClockRestoreEvent": d3iTePbClockRestoreEvent,
       "d3iTeTdmClockLost": d3iTeTdmClockLost,
       "d3iTeTdmClockRestored": d3iTeTdmClockRestored,
       "d3iTeEnfasLinkUp": d3iTeEnfasLinkUp,
       "d3iTeEnfasLinkDown": d3iTeEnfasLinkDown,
       "d3iTeSystemReset": d3iTeSystemReset}
)
