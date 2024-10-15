# SNMP MIB module (DCP-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DCP-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:25 2024
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



class Counter8(Integer32):
    """Custom type Counter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_Cdx6500OSTDCPTable_Object = MibTable
cdx6500OSTDCPTable = _Cdx6500OSTDCPTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cdx6500OSTDCPTable.setStatus("mandatory")
_Cdx6500DCPStatEntry_Object = MibTableRow
cdx6500DCPStatEntry = _Cdx6500DCPStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1)
)
cdx6500DCPStatEntry.setIndexNames(
    (0, "DCP-OPT-MIB", "cdx6500DCPPortNumber"),
    (0, "DCP-OPT-MIB", "cdx6500DCPChanNumber"),
)
if mibBuilder.loadTexts:
    cdx6500DCPStatEntry.setStatus("mandatory")


class _Cdx6500DCPPortNumber_Type(Integer32):
    """Custom type cdx6500DCPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500DCPPortNumber_Type.__name__ = "Integer32"
_Cdx6500DCPPortNumber_Object = MibTableColumn
cdx6500DCPPortNumber = _Cdx6500DCPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 1),
    _Cdx6500DCPPortNumber_Type()
)
cdx6500DCPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPPortNumber.setStatus("mandatory")


class _Cdx6500DCPChanNumber_Type(Integer32):
    """Custom type cdx6500DCPChanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Cdx6500DCPChanNumber_Type.__name__ = "Integer32"
_Cdx6500DCPChanNumber_Object = MibTableColumn
cdx6500DCPChanNumber = _Cdx6500DCPChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 2),
    _Cdx6500DCPChanNumber_Type()
)
cdx6500DCPChanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPChanNumber.setStatus("mandatory")
_Cdx6500DCPNegProtLevel_Type = DisplayString
_Cdx6500DCPNegProtLevel_Object = MibTableColumn
cdx6500DCPNegProtLevel = _Cdx6500DCPNegProtLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 3),
    _Cdx6500DCPNegProtLevel_Type()
)
cdx6500DCPNegProtLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPNegProtLevel.setStatus("mandatory")
_Cdx6500DCPCurrConnState_Type = DisplayString
_Cdx6500DCPCurrConnState_Object = MibTableColumn
cdx6500DCPCurrConnState = _Cdx6500DCPCurrConnState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 4),
    _Cdx6500DCPCurrConnState_Type()
)
cdx6500DCPCurrConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPCurrConnState.setStatus("mandatory")
_Cdx6500DCPUnackDataTpdu_Type = Counter8
_Cdx6500DCPUnackDataTpdu_Object = MibTableColumn
cdx6500DCPUnackDataTpdu = _Cdx6500DCPUnackDataTpdu_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 5),
    _Cdx6500DCPUnackDataTpdu_Type()
)
cdx6500DCPUnackDataTpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPUnackDataTpdu.setStatus("mandatory")
_Cdx6500DCPDataTpduQueued_Type = Counter8
_Cdx6500DCPDataTpduQueued_Object = MibTableColumn
cdx6500DCPDataTpduQueued = _Cdx6500DCPDataTpduQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 6),
    _Cdx6500DCPDataTpduQueued_Type()
)
cdx6500DCPDataTpduQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPDataTpduQueued.setStatus("mandatory")


class _Cdx6500DCPInboundFlowSt_Type(Integer32):
    """Custom type cdx6500DCPInboundFlowSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500DCPInboundFlowSt_Type.__name__ = "Integer32"
_Cdx6500DCPInboundFlowSt_Object = MibTableColumn
cdx6500DCPInboundFlowSt = _Cdx6500DCPInboundFlowSt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 7),
    _Cdx6500DCPInboundFlowSt_Type()
)
cdx6500DCPInboundFlowSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPInboundFlowSt.setStatus("mandatory")


class _Cdx6500DCPOutboundFlowSt_Type(Integer32):
    """Custom type cdx6500DCPOutboundFlowSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500DCPOutboundFlowSt_Type.__name__ = "Integer32"
_Cdx6500DCPOutboundFlowSt_Object = MibTableColumn
cdx6500DCPOutboundFlowSt = _Cdx6500DCPOutboundFlowSt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 8),
    _Cdx6500DCPOutboundFlowSt_Type()
)
cdx6500DCPOutboundFlowSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPOutboundFlowSt.setStatus("mandatory")
_Cdx6500DCPConnReqTx_Type = Counter8
_Cdx6500DCPConnReqTx_Object = MibTableColumn
cdx6500DCPConnReqTx = _Cdx6500DCPConnReqTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 9),
    _Cdx6500DCPConnReqTx_Type()
)
cdx6500DCPConnReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPConnReqTx.setStatus("mandatory")
_Cdx6500DCPConnConfTx_Type = Counter8
_Cdx6500DCPConnConfTx_Object = MibTableColumn
cdx6500DCPConnConfTx = _Cdx6500DCPConnConfTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 10),
    _Cdx6500DCPConnConfTx_Type()
)
cdx6500DCPConnConfTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPConnConfTx.setStatus("mandatory")
_Cdx6500DCPReconnReqTx_Type = Counter8
_Cdx6500DCPReconnReqTx_Object = MibTableColumn
cdx6500DCPReconnReqTx = _Cdx6500DCPReconnReqTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 11),
    _Cdx6500DCPReconnReqTx_Type()
)
cdx6500DCPReconnReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPReconnReqTx.setStatus("mandatory")
_Cdx6500DCPReconnConfTx_Type = Counter8
_Cdx6500DCPReconnConfTx_Object = MibTableColumn
cdx6500DCPReconnConfTx = _Cdx6500DCPReconnConfTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 12),
    _Cdx6500DCPReconnConfTx_Type()
)
cdx6500DCPReconnConfTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPReconnConfTx.setStatus("mandatory")
_Cdx6500DCPDiscReqTx_Type = Counter8
_Cdx6500DCPDiscReqTx_Object = MibTableColumn
cdx6500DCPDiscReqTx = _Cdx6500DCPDiscReqTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 13),
    _Cdx6500DCPDiscReqTx_Type()
)
cdx6500DCPDiscReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPDiscReqTx.setStatus("mandatory")
_Cdx6500DCPDiscConfTx_Type = Counter8
_Cdx6500DCPDiscConfTx_Object = MibTableColumn
cdx6500DCPDiscConfTx = _Cdx6500DCPDiscConfTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 14),
    _Cdx6500DCPDiscConfTx_Type()
)
cdx6500DCPDiscConfTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPDiscConfTx.setStatus("mandatory")
_Cdx6500DCPDataTx_Type = Counter32
_Cdx6500DCPDataTx_Object = MibTableColumn
cdx6500DCPDataTx = _Cdx6500DCPDataTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 15),
    _Cdx6500DCPDataTx_Type()
)
cdx6500DCPDataTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPDataTx.setStatus("mandatory")
_Cdx6500DCPAckTx_Type = Counter32
_Cdx6500DCPAckTx_Object = MibTableColumn
cdx6500DCPAckTx = _Cdx6500DCPAckTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 16),
    _Cdx6500DCPAckTx_Type()
)
cdx6500DCPAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPAckTx.setStatus("mandatory")
_Cdx6500DCPIntReqTx_Type = Counter8
_Cdx6500DCPIntReqTx_Object = MibTableColumn
cdx6500DCPIntReqTx = _Cdx6500DCPIntReqTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 17),
    _Cdx6500DCPIntReqTx_Type()
)
cdx6500DCPIntReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPIntReqTx.setStatus("mandatory")
_Cdx6500DCPIntConfTx_Type = Counter8
_Cdx6500DCPIntConfTx_Object = MibTableColumn
cdx6500DCPIntConfTx = _Cdx6500DCPIntConfTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 18),
    _Cdx6500DCPIntConfTx_Type()
)
cdx6500DCPIntConfTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPIntConfTx.setStatus("mandatory")
_Cdx6500DCPResetReqTx_Type = Counter8
_Cdx6500DCPResetReqTx_Object = MibTableColumn
cdx6500DCPResetReqTx = _Cdx6500DCPResetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 19),
    _Cdx6500DCPResetReqTx_Type()
)
cdx6500DCPResetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPResetReqTx.setStatus("mandatory")
_Cdx6500DCPResetConfTx_Type = Counter8
_Cdx6500DCPResetConfTx_Object = MibTableColumn
cdx6500DCPResetConfTx = _Cdx6500DCPResetConfTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 20),
    _Cdx6500DCPResetConfTx_Type()
)
cdx6500DCPResetConfTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPResetConfTx.setStatus("mandatory")
_Cdx6500DCPRejTx_Type = Counter8
_Cdx6500DCPRejTx_Object = MibTableColumn
cdx6500DCPRejTx = _Cdx6500DCPRejTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 21),
    _Cdx6500DCPRejTx_Type()
)
cdx6500DCPRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPRejTx.setStatus("mandatory")
_Cdx6500DCPConnReqRcv_Type = Counter8
_Cdx6500DCPConnReqRcv_Object = MibTableColumn
cdx6500DCPConnReqRcv = _Cdx6500DCPConnReqRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 22),
    _Cdx6500DCPConnReqRcv_Type()
)
cdx6500DCPConnReqRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPConnReqRcv.setStatus("mandatory")
_Cdx6500DCPConnConfRcv_Type = Counter8
_Cdx6500DCPConnConfRcv_Object = MibTableColumn
cdx6500DCPConnConfRcv = _Cdx6500DCPConnConfRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 23),
    _Cdx6500DCPConnConfRcv_Type()
)
cdx6500DCPConnConfRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPConnConfRcv.setStatus("mandatory")
_Cdx6500DCPReconnReqRcv_Type = Counter8
_Cdx6500DCPReconnReqRcv_Object = MibTableColumn
cdx6500DCPReconnReqRcv = _Cdx6500DCPReconnReqRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 24),
    _Cdx6500DCPReconnReqRcv_Type()
)
cdx6500DCPReconnReqRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPReconnReqRcv.setStatus("mandatory")
_Cdx6500DCPReconnConfRcv_Type = Counter8
_Cdx6500DCPReconnConfRcv_Object = MibTableColumn
cdx6500DCPReconnConfRcv = _Cdx6500DCPReconnConfRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 25),
    _Cdx6500DCPReconnConfRcv_Type()
)
cdx6500DCPReconnConfRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPReconnConfRcv.setStatus("mandatory")
_Cdx6500DCPDiscReqRcv_Type = Counter8
_Cdx6500DCPDiscReqRcv_Object = MibTableColumn
cdx6500DCPDiscReqRcv = _Cdx6500DCPDiscReqRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 26),
    _Cdx6500DCPDiscReqRcv_Type()
)
cdx6500DCPDiscReqRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPDiscReqRcv.setStatus("mandatory")
_Cdx6500DCPDiscConfRcv_Type = Counter8
_Cdx6500DCPDiscConfRcv_Object = MibTableColumn
cdx6500DCPDiscConfRcv = _Cdx6500DCPDiscConfRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 27),
    _Cdx6500DCPDiscConfRcv_Type()
)
cdx6500DCPDiscConfRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPDiscConfRcv.setStatus("mandatory")
_Cdx6500DCPDataRcv_Type = Counter32
_Cdx6500DCPDataRcv_Object = MibTableColumn
cdx6500DCPDataRcv = _Cdx6500DCPDataRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 28),
    _Cdx6500DCPDataRcv_Type()
)
cdx6500DCPDataRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPDataRcv.setStatus("mandatory")
_Cdx6500DCPAckRcv_Type = Counter32
_Cdx6500DCPAckRcv_Object = MibTableColumn
cdx6500DCPAckRcv = _Cdx6500DCPAckRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 29),
    _Cdx6500DCPAckRcv_Type()
)
cdx6500DCPAckRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPAckRcv.setStatus("mandatory")
_Cdx6500DCPIntReqRcv_Type = Counter8
_Cdx6500DCPIntReqRcv_Object = MibTableColumn
cdx6500DCPIntReqRcv = _Cdx6500DCPIntReqRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 30),
    _Cdx6500DCPIntReqRcv_Type()
)
cdx6500DCPIntReqRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPIntReqRcv.setStatus("mandatory")
_Cdx6500DCPIntConfRcv_Type = Counter8
_Cdx6500DCPIntConfRcv_Object = MibTableColumn
cdx6500DCPIntConfRcv = _Cdx6500DCPIntConfRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 31),
    _Cdx6500DCPIntConfRcv_Type()
)
cdx6500DCPIntConfRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPIntConfRcv.setStatus("mandatory")
_Cdx6500DCPResetReqRcv_Type = Counter8
_Cdx6500DCPResetReqRcv_Object = MibTableColumn
cdx6500DCPResetReqRcv = _Cdx6500DCPResetReqRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 32),
    _Cdx6500DCPResetReqRcv_Type()
)
cdx6500DCPResetReqRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPResetReqRcv.setStatus("mandatory")
_Cdx6500DCPResetConfRcv_Type = Counter8
_Cdx6500DCPResetConfRcv_Object = MibTableColumn
cdx6500DCPResetConfRcv = _Cdx6500DCPResetConfRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 33),
    _Cdx6500DCPResetConfRcv_Type()
)
cdx6500DCPResetConfRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPResetConfRcv.setStatus("mandatory")
_Cdx6500DCPRejRcv_Type = Counter8
_Cdx6500DCPRejRcv_Object = MibTableColumn
cdx6500DCPRejRcv = _Cdx6500DCPRejRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 1, 1, 34),
    _Cdx6500DCPRejRcv_Type()
)
cdx6500DCPRejRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500DCPRejRcv.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCP-OPT-MIB",
    **{"Counter8": Counter8,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "cdx6500OSTDCPTable": cdx6500OSTDCPTable,
       "cdx6500DCPStatEntry": cdx6500DCPStatEntry,
       "cdx6500DCPPortNumber": cdx6500DCPPortNumber,
       "cdx6500DCPChanNumber": cdx6500DCPChanNumber,
       "cdx6500DCPNegProtLevel": cdx6500DCPNegProtLevel,
       "cdx6500DCPCurrConnState": cdx6500DCPCurrConnState,
       "cdx6500DCPUnackDataTpdu": cdx6500DCPUnackDataTpdu,
       "cdx6500DCPDataTpduQueued": cdx6500DCPDataTpduQueued,
       "cdx6500DCPInboundFlowSt": cdx6500DCPInboundFlowSt,
       "cdx6500DCPOutboundFlowSt": cdx6500DCPOutboundFlowSt,
       "cdx6500DCPConnReqTx": cdx6500DCPConnReqTx,
       "cdx6500DCPConnConfTx": cdx6500DCPConnConfTx,
       "cdx6500DCPReconnReqTx": cdx6500DCPReconnReqTx,
       "cdx6500DCPReconnConfTx": cdx6500DCPReconnConfTx,
       "cdx6500DCPDiscReqTx": cdx6500DCPDiscReqTx,
       "cdx6500DCPDiscConfTx": cdx6500DCPDiscConfTx,
       "cdx6500DCPDataTx": cdx6500DCPDataTx,
       "cdx6500DCPAckTx": cdx6500DCPAckTx,
       "cdx6500DCPIntReqTx": cdx6500DCPIntReqTx,
       "cdx6500DCPIntConfTx": cdx6500DCPIntConfTx,
       "cdx6500DCPResetReqTx": cdx6500DCPResetReqTx,
       "cdx6500DCPResetConfTx": cdx6500DCPResetConfTx,
       "cdx6500DCPRejTx": cdx6500DCPRejTx,
       "cdx6500DCPConnReqRcv": cdx6500DCPConnReqRcv,
       "cdx6500DCPConnConfRcv": cdx6500DCPConnConfRcv,
       "cdx6500DCPReconnReqRcv": cdx6500DCPReconnReqRcv,
       "cdx6500DCPReconnConfRcv": cdx6500DCPReconnConfRcv,
       "cdx6500DCPDiscReqRcv": cdx6500DCPDiscReqRcv,
       "cdx6500DCPDiscConfRcv": cdx6500DCPDiscConfRcv,
       "cdx6500DCPDataRcv": cdx6500DCPDataRcv,
       "cdx6500DCPAckRcv": cdx6500DCPAckRcv,
       "cdx6500DCPIntReqRcv": cdx6500DCPIntReqRcv,
       "cdx6500DCPIntConfRcv": cdx6500DCPIntConfRcv,
       "cdx6500DCPResetReqRcv": cdx6500DCPResetReqRcv,
       "cdx6500DCPResetConfRcv": cdx6500DCPResetConfRcv,
       "cdx6500DCPRejRcv": cdx6500DCPRejRcv}
)
