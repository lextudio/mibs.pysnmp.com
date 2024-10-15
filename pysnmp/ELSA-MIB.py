# SNMP MIB module (ELSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:55 2024
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

_Elsa_ObjectIdentity = ObjectIdentity
elsa = _Elsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356)
)
_Isdn_Systems_ObjectIdentity = ObjectIdentity
isdn_Systems = _Isdn_Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400)
)
_Isdn_Router_ObjectIdentity = ObjectIdentity
isdn_Router = _Isdn_Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1)
)
_Lancom_2000_ObjectIdentity = ObjectIdentity
lancom_2000 = _Lancom_2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000)
)
_Sta_ObjectIdentity = ObjectIdentity
sta = _Sta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1)
)
_StaConne_Type = DisplayString
_StaConne_Object = MibScalar
staConne = _StaConne_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 1),
    _StaConne_Type()
)
staConne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConne.setStatus("mandatory")
_StaOpera_Type = DisplayString
_StaOpera_Object = MibScalar
staOpera = _StaOpera_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 2),
    _StaOpera_Type()
)
staOpera.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOpera.setStatus("mandatory")
_StaWanst_ObjectIdentity = ObjectIdentity
staWanst = _StaWanst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4)
)
_StaWanstBytetrans_Object = MibTable
staWanstBytetrans = _StaWanstBytetrans_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 1)
)
if mibBuilder.loadTexts:
    staWanstBytetrans.setStatus("mandatory")
_StaWanstBytetransCols_Object = MibTableRow
staWanstBytetransCols = _StaWanstBytetransCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 1, 1)
)
staWanstBytetransCols.setIndexNames(
    (0, "ELSA-MIB", "staWanstBytetransIfc"),
)
if mibBuilder.loadTexts:
    staWanstBytetransCols.setStatus("mandatory")


class _StaWanstBytetransIfc_Type(Integer32):
    """Custom type staWanstBytetransIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaWanstBytetransIfc_Type.__name__ = "Integer32"
_StaWanstBytetransIfc_Object = MibTableColumn
staWanstBytetransIfc = _StaWanstBytetransIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 1, 1, 1),
    _StaWanstBytetransIfc_Type()
)
staWanstBytetransIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstBytetransIfc.setStatus("mandatory")
_StaWanstBytetransCrx_Type = Integer32
_StaWanstBytetransCrx_Object = MibTableColumn
staWanstBytetransCrx = _StaWanstBytetransCrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 1, 1, 2),
    _StaWanstBytetransCrx_Type()
)
staWanstBytetransCrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstBytetransCrx.setStatus("mandatory")
_StaWanstBytetransRxb_Type = Integer32
_StaWanstBytetransRxb_Object = MibTableColumn
staWanstBytetransRxb = _StaWanstBytetransRxb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 1, 1, 3),
    _StaWanstBytetransRxb_Type()
)
staWanstBytetransRxb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstBytetransRxb.setStatus("mandatory")
_StaWanstBytetransTxb_Type = Integer32
_StaWanstBytetransTxb_Object = MibTableColumn
staWanstBytetransTxb = _StaWanstBytetransTxb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 1, 1, 4),
    _StaWanstBytetransTxb_Type()
)
staWanstBytetransTxb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstBytetransTxb.setStatus("mandatory")
_StaWanstBytetransCtx_Type = Integer32
_StaWanstBytetransCtx_Object = MibTableColumn
staWanstBytetransCtx = _StaWanstBytetransCtx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 1, 1, 5),
    _StaWanstBytetransCtx_Type()
)
staWanstBytetransCtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstBytetransCtx.setStatus("mandatory")
_StaWanstPackettra_Object = MibTable
staWanstPackettra = _StaWanstPackettra_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 2)
)
if mibBuilder.loadTexts:
    staWanstPackettra.setStatus("mandatory")
_StaWanstPackettraCols_Object = MibTableRow
staWanstPackettraCols = _StaWanstPackettraCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 2, 1)
)
staWanstPackettraCols.setIndexNames(
    (0, "ELSA-MIB", "staWanstPackettraIfc"),
)
if mibBuilder.loadTexts:
    staWanstPackettraCols.setStatus("mandatory")


class _StaWanstPackettraIfc_Type(Integer32):
    """Custom type staWanstPackettraIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaWanstPackettraIfc_Type.__name__ = "Integer32"
_StaWanstPackettraIfc_Object = MibTableColumn
staWanstPackettraIfc = _StaWanstPackettraIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 2, 1, 1),
    _StaWanstPackettraIfc_Type()
)
staWanstPackettraIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstPackettraIfc.setStatus("mandatory")
_StaWanstPackettraRx_Type = Integer32
_StaWanstPackettraRx_Object = MibTableColumn
staWanstPackettraRx = _StaWanstPackettraRx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 2, 1, 2),
    _StaWanstPackettraRx_Type()
)
staWanstPackettraRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstPackettraRx.setStatus("mandatory")
_StaWanstPackettraTxt_Type = Integer32
_StaWanstPackettraTxt_Object = MibTableColumn
staWanstPackettraTxt = _StaWanstPackettraTxt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 2, 1, 3),
    _StaWanstPackettraTxt_Type()
)
staWanstPackettraTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstPackettraTxt.setStatus("mandatory")
_StaWanstPackettraTxn_Type = Integer32
_StaWanstPackettraTxn_Object = MibTableColumn
staWanstPackettraTxn = _StaWanstPackettraTxn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 2, 1, 4),
    _StaWanstPackettraTxn_Type()
)
staWanstPackettraTxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstPackettraTxn.setStatus("mandatory")
_StaWanstPackettraTxr_Type = Integer32
_StaWanstPackettraTxr_Object = MibTableColumn
staWanstPackettraTxr = _StaWanstPackettraTxr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 2, 1, 5),
    _StaWanstPackettraTxr_Type()
)
staWanstPackettraTxr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstPackettraTxr.setStatus("mandatory")
_StaWanstPackettraTxu_Type = Integer32
_StaWanstPackettraTxu_Object = MibTableColumn
staWanstPackettraTxu = _StaWanstPackettraTxu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 2, 1, 6),
    _StaWanstPackettraTxu_Type()
)
staWanstPackettraTxu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstPackettraTxu.setStatus("mandatory")
_StaWanstErrorstat_Object = MibTable
staWanstErrorstat = _StaWanstErrorstat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 3)
)
if mibBuilder.loadTexts:
    staWanstErrorstat.setStatus("mandatory")
_StaWanstErrorstatCols_Object = MibTableRow
staWanstErrorstatCols = _StaWanstErrorstatCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 3, 1)
)
staWanstErrorstatCols.setIndexNames(
    (0, "ELSA-MIB", "staWanstErrorstatIfc"),
)
if mibBuilder.loadTexts:
    staWanstErrorstatCols.setStatus("mandatory")


class _StaWanstErrorstatIfc_Type(Integer32):
    """Custom type staWanstErrorstatIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaWanstErrorstatIfc_Type.__name__ = "Integer32"
_StaWanstErrorstatIfc_Object = MibTableColumn
staWanstErrorstatIfc = _StaWanstErrorstatIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 3, 1, 1),
    _StaWanstErrorstatIfc_Type()
)
staWanstErrorstatIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstErrorstatIfc.setStatus("mandatory")
_StaWanstErrorstatRxl1_Type = Integer32
_StaWanstErrorstatRxl1_Object = MibTableColumn
staWanstErrorstatRxl1 = _StaWanstErrorstatRxl1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 3, 1, 2),
    _StaWanstErrorstatRxl1_Type()
)
staWanstErrorstatRxl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstErrorstatRxl1.setStatus("mandatory")
_StaWanstErrorstatRxl2_Type = Integer32
_StaWanstErrorstatRxl2_Object = MibTableColumn
staWanstErrorstatRxl2 = _StaWanstErrorstatRxl2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 3, 1, 3),
    _StaWanstErrorstatRxl2_Type()
)
staWanstErrorstatRxl2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstErrorstatRxl2.setStatus("mandatory")
_StaWanstErrorstatRxl3_Type = Integer32
_StaWanstErrorstatRxl3_Object = MibTableColumn
staWanstErrorstatRxl3 = _StaWanstErrorstatRxl3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 3, 1, 4),
    _StaWanstErrorstatRxl3_Type()
)
staWanstErrorstatRxl3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstErrorstatRxl3.setStatus("mandatory")
_StaWanstErrorstatStac_Type = Integer32
_StaWanstErrorstatStac_Object = MibTableColumn
staWanstErrorstatStac = _StaWanstErrorstatStac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 3, 1, 5),
    _StaWanstErrorstatStac_Type()
)
staWanstErrorstatStac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstErrorstatStac.setStatus("mandatory")
_StaWanstErrorstatTxer_Type = Integer32
_StaWanstErrorstatTxer_Object = MibTableColumn
staWanstErrorstatTxer = _StaWanstErrorstatTxer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 3, 1, 6),
    _StaWanstErrorstatTxer_Type()
)
staWanstErrorstatTxer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstErrorstatTxer.setStatus("mandatory")
_StaWanstWantxdisc_Type = Integer32
_StaWanstWantxdisc_Object = MibScalar
staWanstWantxdisc = _StaWanstWantxdisc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 4),
    _StaWanstWantxdisc_Type()
)
staWanstWantxdisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstWantxdisc.setStatus("mandatory")
_StaWanstWanheappa_Type = Integer32
_StaWanstWanheappa_Object = MibScalar
staWanstWanheappa = _StaWanstWanheappa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 5),
    _StaWanstWanheappa_Type()
)
staWanstWanheappa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstWanheappa.setStatus("mandatory")
_StaWanstWanqueuep_Type = Integer32
_StaWanstWanqueuep_Object = MibScalar
staWanstWanqueuep = _StaWanstWanqueuep_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 6),
    _StaWanstWanqueuep_Type()
)
staWanstWanqueuep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstWanqueuep.setStatus("mandatory")
_StaWanstWanqueuee_Type = Integer32
_StaWanstWanqueuee_Object = MibScalar
staWanstWanqueuee = _StaWanstWanqueuee_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 7),
    _StaWanstWanqueuee_Type()
)
staWanstWanqueuee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstWanqueuee.setStatus("mandatory")
_StaWanstThroughpu_Object = MibTable
staWanstThroughpu = _StaWanstThroughpu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 8)
)
if mibBuilder.loadTexts:
    staWanstThroughpu.setStatus("mandatory")
_StaWanstThroughpuCols_Object = MibTableRow
staWanstThroughpuCols = _StaWanstThroughpuCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 8, 1)
)
staWanstThroughpuCols.setIndexNames(
    (0, "ELSA-MIB", "staWanstThroughpuIfc"),
)
if mibBuilder.loadTexts:
    staWanstThroughpuCols.setStatus("mandatory")


class _StaWanstThroughpuIfc_Type(Integer32):
    """Custom type staWanstThroughpuIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaWanstThroughpuIfc_Type.__name__ = "Integer32"
_StaWanstThroughpuIfc_Object = MibTableColumn
staWanstThroughpuIfc = _StaWanstThroughpuIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 8, 1, 1),
    _StaWanstThroughpuIfc_Type()
)
staWanstThroughpuIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstThroughpuIfc.setStatus("mandatory")
_StaWanstThroughpuRxsc_Type = Integer32
_StaWanstThroughpuRxsc_Object = MibTableColumn
staWanstThroughpuRxsc = _StaWanstThroughpuRxsc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 8, 1, 2),
    _StaWanstThroughpuRxsc_Type()
)
staWanstThroughpuRxsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstThroughpuRxsc.setStatus("mandatory")
_StaWanstThroughpuTxsc_Type = Integer32
_StaWanstThroughpuTxsc_Object = MibTableColumn
staWanstThroughpuTxsc = _StaWanstThroughpuTxsc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 8, 1, 3),
    _StaWanstThroughpuTxsc_Type()
)
staWanstThroughpuTxsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstThroughpuTxsc.setStatus("mandatory")
_StaWanstThroughpuRxsa_Type = Integer32
_StaWanstThroughpuRxsa_Object = MibTableColumn
staWanstThroughpuRxsa = _StaWanstThroughpuRxsa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 8, 1, 4),
    _StaWanstThroughpuRxsa_Type()
)
staWanstThroughpuRxsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstThroughpuRxsa.setStatus("mandatory")
_StaWanstThroughpuTxsa_Type = Integer32
_StaWanstThroughpuTxsa_Object = MibTableColumn
staWanstThroughpuTxsa = _StaWanstThroughpuTxsa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 8, 1, 5),
    _StaWanstThroughpuTxsa_Type()
)
staWanstThroughpuTxsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staWanstThroughpuTxsa.setStatus("mandatory")
_StaWanstDeleteval_Type = Integer32
_StaWanstDeleteval_Object = MibScalar
staWanstDeleteval = _StaWanstDeleteval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 4, 9),
    _StaWanstDeleteval_Type()
)
staWanstDeleteval.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staWanstDeleteval.setStatus("mandatory")
_StaLanst_ObjectIdentity = ObjectIdentity
staLanst = _StaLanst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5)
)
_StaLanstLanrxpack_Type = Integer32
_StaLanstLanrxpack_Object = MibScalar
staLanstLanrxpack = _StaLanstLanrxpack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 1),
    _StaLanstLanrxpack_Type()
)
staLanstLanrxpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanrxpack.setStatus("mandatory")
_StaLanstLantxpack_Type = Integer32
_StaLanstLantxpack_Object = MibScalar
staLanstLantxpack = _StaLanstLantxpack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 2),
    _StaLanstLantxpack_Type()
)
staLanstLantxpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLantxpack.setStatus("mandatory")
_StaLanstLanrxerro_Type = Integer32
_StaLanstLanrxerro_Object = MibScalar
staLanstLanrxerro = _StaLanstLanrxerro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 3),
    _StaLanstLanrxerro_Type()
)
staLanstLanrxerro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanrxerro.setStatus("mandatory")
_StaLanstLantxerro_Type = Integer32
_StaLanstLantxerro_Object = MibScalar
staLanstLantxerro = _StaLanstLantxerro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 4),
    _StaLanstLantxerro_Type()
)
staLanstLantxerro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLantxerro.setStatus("mandatory")
_StaLanstLanstacke_Type = Integer32
_StaLanstLanstacke_Object = MibScalar
staLanstLanstacke = _StaLanstLanstacke_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 5),
    _StaLanstLanstacke_Type()
)
staLanstLanstacke.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanstacke.setStatus("mandatory")
_StaLanstLannicerr_Type = Integer32
_StaLanstLannicerr_Object = MibScalar
staLanstLannicerr = _StaLanstLannicerr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 6),
    _StaLanstLannicerr_Type()
)
staLanstLannicerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLannicerr.setStatus("mandatory")
_StaLanstLanheappa_Type = Integer32
_StaLanstLanheappa_Object = MibScalar
staLanstLanheappa = _StaLanstLanheappa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 7),
    _StaLanstLanheappa_Type()
)
staLanstLanheappa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanheappa.setStatus("mandatory")
_StaLanstLanqueuep_Type = Integer32
_StaLanstLanqueuep_Object = MibScalar
staLanstLanqueuep = _StaLanstLanqueuep_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 8),
    _StaLanstLanqueuep_Type()
)
staLanstLanqueuep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanqueuep.setStatus("mandatory")
_StaLanstLanqueuee_Type = Integer32
_StaLanstLanqueuee_Object = MibScalar
staLanstLanqueuee = _StaLanstLanqueuee_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 9),
    _StaLanstLanqueuee_Type()
)
staLanstLanqueuee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanqueuee.setStatus("mandatory")
_StaLanstLancollis_Type = Integer32
_StaLanstLancollis_Object = MibScalar
staLanstLancollis = _StaLanstLancollis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 10),
    _StaLanstLancollis_Type()
)
staLanstLancollis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLancollis.setStatus("mandatory")
_StaLanstDeleteval_Type = Integer32
_StaLanstDeleteval_Object = MibScalar
staLanstDeleteval = _StaLanstDeleteval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 11),
    _StaLanstDeleteval_Type()
)
staLanstDeleteval.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staLanstDeleteval.setStatus("mandatory")
_StaLanstLanrxbyte_Type = Integer32
_StaLanstLanrxbyte_Object = MibScalar
staLanstLanrxbyte = _StaLanstLanrxbyte_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 18),
    _StaLanstLanrxbyte_Type()
)
staLanstLanrxbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanrxbyte.setStatus("mandatory")
_StaLanstLantxbyte_Type = Integer32
_StaLanstLantxbyte_Object = MibScalar
staLanstLantxbyte = _StaLanstLantxbyte_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 19),
    _StaLanstLantxbyte_Type()
)
staLanstLantxbyte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLantxbyte.setStatus("mandatory")
_StaLanstLanrxbroa_Type = Integer32
_StaLanstLanrxbroa_Object = MibScalar
staLanstLanrxbroa = _StaLanstLanrxbroa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 20),
    _StaLanstLanrxbroa_Type()
)
staLanstLanrxbroa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanrxbroa.setStatus("mandatory")
_StaLanstLanrxmult_Type = Integer32
_StaLanstLanrxmult_Object = MibScalar
staLanstLanrxmult = _StaLanstLanrxmult_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 21),
    _StaLanstLanrxmult_Type()
)
staLanstLanrxmult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanrxmult.setStatus("mandatory")
_StaLanstLanrxunic_Type = Integer32
_StaLanstLanrxunic_Object = MibScalar
staLanstLanrxunic = _StaLanstLanrxunic_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 22),
    _StaLanstLanrxunic_Type()
)
staLanstLanrxunic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanrxunic.setStatus("mandatory")
_StaLanstLantxbroa_Type = Integer32
_StaLanstLantxbroa_Object = MibScalar
staLanstLantxbroa = _StaLanstLantxbroa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 23),
    _StaLanstLantxbroa_Type()
)
staLanstLantxbroa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLantxbroa.setStatus("mandatory")
_StaLanstLantxmult_Type = Integer32
_StaLanstLantxmult_Object = MibScalar
staLanstLantxmult = _StaLanstLantxmult_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 24),
    _StaLanstLantxmult_Type()
)
staLanstLantxmult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLantxmult.setStatus("mandatory")
_StaLanstLantxunic_Type = Integer32
_StaLanstLantxunic_Object = MibScalar
staLanstLantxunic = _StaLanstLantxunic_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 25),
    _StaLanstLantxunic_Type()
)
staLanstLantxunic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLantxunic.setStatus("mandatory")
_StaLanstLanrxcrce_Type = Integer32
_StaLanstLanrxcrce_Object = MibScalar
staLanstLanrxcrce = _StaLanstLanrxcrce_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 26),
    _StaLanstLanrxcrce_Type()
)
staLanstLanrxcrce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanrxcrce.setStatus("mandatory")
_StaLanstLanrxalig_Type = Integer32
_StaLanstLanrxalig_Object = MibScalar
staLanstLanrxalig = _StaLanstLanrxalig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 5, 27),
    _StaLanstLanrxalig_Type()
)
staLanstLanrxalig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLanstLanrxalig.setStatus("mandatory")
_StaPppst_ObjectIdentity = ObjectIdentity
staPppst = _StaPppst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6)
)
_StaPppstPpp_Object = MibTable
staPppstPpp = _StaPppstPpp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 1)
)
if mibBuilder.loadTexts:
    staPppstPpp.setStatus("mandatory")
_StaPppstPppCols_Object = MibTableRow
staPppstPppCols = _StaPppstPppCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 1, 1)
)
staPppstPppCols.setIndexNames(
    (0, "ELSA-MIB", "staPppstPppIfc"),
)
if mibBuilder.loadTexts:
    staPppstPppCols.setStatus("mandatory")


class _StaPppstPppIfc_Type(Integer32):
    """Custom type staPppstPppIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaPppstPppIfc_Type.__name__ = "Integer32"
_StaPppstPppIfc_Object = MibTableColumn
staPppstPppIfc = _StaPppstPppIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 1, 1, 1),
    _StaPppstPppIfc_Type()
)
staPppstPppIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPppIfc.setStatus("mandatory")


class _StaPppstPppPha_Type(Integer32):
    """Custom type staPppstPppPha based on Integer32"""
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
        *(("authenticate", 4),
          ("callback", 5),
          ("dead", 1),
          ("establish", 2),
          ("network", 6),
          ("terminate", 3))
    )


_StaPppstPppPha_Type.__name__ = "Integer32"
_StaPppstPppPha_Object = MibTableColumn
staPppstPppPha = _StaPppstPppPha_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 1, 1, 2),
    _StaPppstPppPha_Type()
)
staPppstPppPha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPppPha.setStatus("mandatory")


class _StaPppstPppLcp_Type(Integer32):
    """Custom type staPppstPppLcp based on Integer32"""
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
        *(("ackrcvd", 8),
          ("acksent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("reqsent", 7),
          ("startng", 2),
          ("stopped", 4),
          ("stoppng", 6))
    )


_StaPppstPppLcp_Type.__name__ = "Integer32"
_StaPppstPppLcp_Object = MibTableColumn
staPppstPppLcp = _StaPppstPppLcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 1, 1, 3),
    _StaPppstPppLcp_Type()
)
staPppstPppLcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPppLcp.setStatus("mandatory")


class _StaPppstPppIpc_Type(Integer32):
    """Custom type staPppstPppIpc based on Integer32"""
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
        *(("ackrcvd", 8),
          ("acksent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("reqsent", 7),
          ("startng", 2),
          ("stopped", 4),
          ("stoppng", 6))
    )


_StaPppstPppIpc_Type.__name__ = "Integer32"
_StaPppstPppIpc_Object = MibTableColumn
staPppstPppIpc = _StaPppstPppIpc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 1, 1, 4),
    _StaPppstPppIpc_Type()
)
staPppstPppIpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPppIpc.setStatus("mandatory")


class _StaPppstPppIpx_Type(Integer32):
    """Custom type staPppstPppIpx based on Integer32"""
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
        *(("ackrcvd", 8),
          ("acksent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("reqsent", 7),
          ("startng", 2),
          ("stopped", 4),
          ("stoppng", 6))
    )


_StaPppstPppIpx_Type.__name__ = "Integer32"
_StaPppstPppIpx_Object = MibTableColumn
staPppstPppIpx = _StaPppstPppIpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 1, 1, 5),
    _StaPppstPppIpx_Type()
)
staPppstPppIpx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPppIpx.setStatus("mandatory")


class _StaPppstPppCcp_Type(Integer32):
    """Custom type staPppstPppCcp based on Integer32"""
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
        *(("ackrcvd", 8),
          ("acksent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("reqsent", 7),
          ("startng", 2),
          ("stopped", 4),
          ("stoppng", 6))
    )


_StaPppstPppCcp_Type.__name__ = "Integer32"
_StaPppstPppCcp_Object = MibTableColumn
staPppstPppCcp = _StaPppstPppCcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 1, 1, 6),
    _StaPppstPppCcp_Type()
)
staPppstPppCcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPppCcp.setStatus("mandatory")


class _StaPppstPppBac_Type(Integer32):
    """Custom type staPppstPppBac based on Integer32"""
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
        *(("ackrcvd", 8),
          ("acksent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("reqsent", 7),
          ("startng", 2),
          ("stopped", 4),
          ("stoppng", 6))
    )


_StaPppstPppBac_Type.__name__ = "Integer32"
_StaPppstPppBac_Object = MibTableColumn
staPppstPppBac = _StaPppstPppBac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 1, 1, 7),
    _StaPppstPppBac_Type()
)
staPppstPppBac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPppBac.setStatus("mandatory")
_StaPppstLcp_ObjectIdentity = ObjectIdentity
staPppstLcp = _StaPppstLcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2)
)
_StaPppstLcpRxerrors_Type = Integer32
_StaPppstLcpRxerrors_Object = MibScalar
staPppstLcpRxerrors = _StaPppstLcpRxerrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 1),
    _StaPppstLcpRxerrors_Type()
)
staPppstLcpRxerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxerrors.setStatus("mandatory")
_StaPppstLcpRxdiscarded_Type = Integer32
_StaPppstLcpRxdiscarded_Object = MibScalar
staPppstLcpRxdiscarded = _StaPppstLcpRxdiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 2),
    _StaPppstLcpRxdiscarded_Type()
)
staPppstLcpRxdiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxdiscarded.setStatus("mandatory")
_StaPppstLcpRxconfigrequ_Type = Integer32
_StaPppstLcpRxconfigrequ_Object = MibScalar
staPppstLcpRxconfigrequ = _StaPppstLcpRxconfigrequ_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 3),
    _StaPppstLcpRxconfigrequ_Type()
)
staPppstLcpRxconfigrequ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxconfigrequ.setStatus("mandatory")
_StaPppstLcpRxconfigack_Type = Integer32
_StaPppstLcpRxconfigack_Object = MibScalar
staPppstLcpRxconfigack = _StaPppstLcpRxconfigack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 4),
    _StaPppstLcpRxconfigack_Type()
)
staPppstLcpRxconfigack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxconfigack.setStatus("mandatory")
_StaPppstLcpRxconfignak_Type = Integer32
_StaPppstLcpRxconfignak_Object = MibScalar
staPppstLcpRxconfignak = _StaPppstLcpRxconfignak_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 5),
    _StaPppstLcpRxconfignak_Type()
)
staPppstLcpRxconfignak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxconfignak.setStatus("mandatory")
_StaPppstLcpRxconfigreje_Type = Integer32
_StaPppstLcpRxconfigreje_Object = MibScalar
staPppstLcpRxconfigreje = _StaPppstLcpRxconfigreje_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 6),
    _StaPppstLcpRxconfigreje_Type()
)
staPppstLcpRxconfigreje.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxconfigreje.setStatus("mandatory")
_StaPppstLcpRxterminater_Type = Integer32
_StaPppstLcpRxterminater_Object = MibScalar
staPppstLcpRxterminater = _StaPppstLcpRxterminater_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 7),
    _StaPppstLcpRxterminater_Type()
)
staPppstLcpRxterminater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxterminater.setStatus("mandatory")
_StaPppstLcpRxterminatea_Type = Integer32
_StaPppstLcpRxterminatea_Object = MibScalar
staPppstLcpRxterminatea = _StaPppstLcpRxterminatea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 8),
    _StaPppstLcpRxterminatea_Type()
)
staPppstLcpRxterminatea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxterminatea.setStatus("mandatory")
_StaPppstLcpRxcodereject_Type = Integer32
_StaPppstLcpRxcodereject_Object = MibScalar
staPppstLcpRxcodereject = _StaPppstLcpRxcodereject_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 9),
    _StaPppstLcpRxcodereject_Type()
)
staPppstLcpRxcodereject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxcodereject.setStatus("mandatory")
_StaPppstLcpRxprotocolre_Type = Integer32
_StaPppstLcpRxprotocolre_Object = MibScalar
staPppstLcpRxprotocolre = _StaPppstLcpRxprotocolre_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 10),
    _StaPppstLcpRxprotocolre_Type()
)
staPppstLcpRxprotocolre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxprotocolre.setStatus("mandatory")
_StaPppstLcpRxechoreques_Type = Integer32
_StaPppstLcpRxechoreques_Object = MibScalar
staPppstLcpRxechoreques = _StaPppstLcpRxechoreques_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 11),
    _StaPppstLcpRxechoreques_Type()
)
staPppstLcpRxechoreques.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxechoreques.setStatus("mandatory")
_StaPppstLcpRxechoreply_Type = Integer32
_StaPppstLcpRxechoreply_Object = MibScalar
staPppstLcpRxechoreply = _StaPppstLcpRxechoreply_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 12),
    _StaPppstLcpRxechoreply_Type()
)
staPppstLcpRxechoreply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxechoreply.setStatus("mandatory")
_StaPppstLcpRxdiscardreq_Type = Integer32
_StaPppstLcpRxdiscardreq_Object = MibScalar
staPppstLcpRxdiscardreq = _StaPppstLcpRxdiscardreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 13),
    _StaPppstLcpRxdiscardreq_Type()
)
staPppstLcpRxdiscardreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpRxdiscardreq.setStatus("mandatory")
_StaPppstLcpTxconfigrequ_Type = Integer32
_StaPppstLcpTxconfigrequ_Object = MibScalar
staPppstLcpTxconfigrequ = _StaPppstLcpTxconfigrequ_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 14),
    _StaPppstLcpTxconfigrequ_Type()
)
staPppstLcpTxconfigrequ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxconfigrequ.setStatus("mandatory")
_StaPppstLcpTxconfigack_Type = Integer32
_StaPppstLcpTxconfigack_Object = MibScalar
staPppstLcpTxconfigack = _StaPppstLcpTxconfigack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 15),
    _StaPppstLcpTxconfigack_Type()
)
staPppstLcpTxconfigack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxconfigack.setStatus("mandatory")
_StaPppstLcpTxconfignak_Type = Integer32
_StaPppstLcpTxconfignak_Object = MibScalar
staPppstLcpTxconfignak = _StaPppstLcpTxconfignak_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 16),
    _StaPppstLcpTxconfignak_Type()
)
staPppstLcpTxconfignak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxconfignak.setStatus("mandatory")
_StaPppstLcpTxconfigreje_Type = Integer32
_StaPppstLcpTxconfigreje_Object = MibScalar
staPppstLcpTxconfigreje = _StaPppstLcpTxconfigreje_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 17),
    _StaPppstLcpTxconfigreje_Type()
)
staPppstLcpTxconfigreje.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxconfigreje.setStatus("mandatory")
_StaPppstLcpTxterminater_Type = Integer32
_StaPppstLcpTxterminater_Object = MibScalar
staPppstLcpTxterminater = _StaPppstLcpTxterminater_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 18),
    _StaPppstLcpTxterminater_Type()
)
staPppstLcpTxterminater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxterminater.setStatus("mandatory")
_StaPppstLcpTxterminatea_Type = Integer32
_StaPppstLcpTxterminatea_Object = MibScalar
staPppstLcpTxterminatea = _StaPppstLcpTxterminatea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 19),
    _StaPppstLcpTxterminatea_Type()
)
staPppstLcpTxterminatea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxterminatea.setStatus("mandatory")
_StaPppstLcpTxcodereject_Type = Integer32
_StaPppstLcpTxcodereject_Object = MibScalar
staPppstLcpTxcodereject = _StaPppstLcpTxcodereject_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 20),
    _StaPppstLcpTxcodereject_Type()
)
staPppstLcpTxcodereject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxcodereject.setStatus("mandatory")
_StaPppstLcpTxprotocolre_Type = Integer32
_StaPppstLcpTxprotocolre_Object = MibScalar
staPppstLcpTxprotocolre = _StaPppstLcpTxprotocolre_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 21),
    _StaPppstLcpTxprotocolre_Type()
)
staPppstLcpTxprotocolre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxprotocolre.setStatus("mandatory")
_StaPppstLcpTxechoreques_Type = Integer32
_StaPppstLcpTxechoreques_Object = MibScalar
staPppstLcpTxechoreques = _StaPppstLcpTxechoreques_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 22),
    _StaPppstLcpTxechoreques_Type()
)
staPppstLcpTxechoreques.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxechoreques.setStatus("mandatory")
_StaPppstLcpTxechoreply_Type = Integer32
_StaPppstLcpTxechoreply_Object = MibScalar
staPppstLcpTxechoreply = _StaPppstLcpTxechoreply_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 23),
    _StaPppstLcpTxechoreply_Type()
)
staPppstLcpTxechoreply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxechoreply.setStatus("mandatory")
_StaPppstLcpTxdiscardreq_Type = Integer32
_StaPppstLcpTxdiscardreq_Object = MibScalar
staPppstLcpTxdiscardreq = _StaPppstLcpTxdiscardreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 24),
    _StaPppstLcpTxdiscardreq_Type()
)
staPppstLcpTxdiscardreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstLcpTxdiscardreq.setStatus("mandatory")
_StaPppstLcpDeletevalues_Type = Integer32
_StaPppstLcpDeletevalues_Object = MibScalar
staPppstLcpDeletevalues = _StaPppstLcpDeletevalues_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 2, 25),
    _StaPppstLcpDeletevalues_Type()
)
staPppstLcpDeletevalues.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staPppstLcpDeletevalues.setStatus("mandatory")
_StaPppstPap_ObjectIdentity = ObjectIdentity
staPppstPap = _StaPppstPap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 3)
)
_StaPppstPapRxdis_Type = Integer32
_StaPppstPapRxdis_Object = MibScalar
staPppstPapRxdis = _StaPppstPapRxdis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 3, 1),
    _StaPppstPapRxdis_Type()
)
staPppstPapRxdis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPapRxdis.setStatus("mandatory")
_StaPppstPapRxreq_Type = Integer32
_StaPppstPapRxreq_Object = MibScalar
staPppstPapRxreq = _StaPppstPapRxreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 3, 2),
    _StaPppstPapRxreq_Type()
)
staPppstPapRxreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPapRxreq.setStatus("mandatory")
_StaPppstPapRxsuc_Type = Integer32
_StaPppstPapRxsuc_Object = MibScalar
staPppstPapRxsuc = _StaPppstPapRxsuc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 3, 3),
    _StaPppstPapRxsuc_Type()
)
staPppstPapRxsuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPapRxsuc.setStatus("mandatory")
_StaPppstPapRxfai_Type = Integer32
_StaPppstPapRxfai_Object = MibScalar
staPppstPapRxfai = _StaPppstPapRxfai_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 3, 4),
    _StaPppstPapRxfai_Type()
)
staPppstPapRxfai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPapRxfai.setStatus("mandatory")
_StaPppstPapTxret_Type = Integer32
_StaPppstPapTxret_Object = MibScalar
staPppstPapTxret = _StaPppstPapTxret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 3, 5),
    _StaPppstPapTxret_Type()
)
staPppstPapTxret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPapTxret.setStatus("mandatory")
_StaPppstPapTxreq_Type = Integer32
_StaPppstPapTxreq_Object = MibScalar
staPppstPapTxreq = _StaPppstPapTxreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 3, 6),
    _StaPppstPapTxreq_Type()
)
staPppstPapTxreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPapTxreq.setStatus("mandatory")
_StaPppstPapTxsuc_Type = Integer32
_StaPppstPapTxsuc_Object = MibScalar
staPppstPapTxsuc = _StaPppstPapTxsuc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 3, 7),
    _StaPppstPapTxsuc_Type()
)
staPppstPapTxsuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPapTxsuc.setStatus("mandatory")
_StaPppstPapTxfai_Type = Integer32
_StaPppstPapTxfai_Object = MibScalar
staPppstPapTxfai = _StaPppstPapTxfai_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 3, 8),
    _StaPppstPapTxfai_Type()
)
staPppstPapTxfai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstPapTxfai.setStatus("mandatory")
_StaPppstPapDelet_Type = Integer32
_StaPppstPapDelet_Object = MibScalar
staPppstPapDelet = _StaPppstPapDelet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 3, 9),
    _StaPppstPapDelet_Type()
)
staPppstPapDelet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staPppstPapDelet.setStatus("mandatory")
_StaPppstCha_ObjectIdentity = ObjectIdentity
staPppstCha = _StaPppstCha_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4)
)
_StaPppstChaRxdis_Type = Integer32
_StaPppstChaRxdis_Object = MibScalar
staPppstChaRxdis = _StaPppstChaRxdis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 1),
    _StaPppstChaRxdis_Type()
)
staPppstChaRxdis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstChaRxdis.setStatus("mandatory")
_StaPppstChaRxcha_Type = Integer32
_StaPppstChaRxcha_Object = MibScalar
staPppstChaRxcha = _StaPppstChaRxcha_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 2),
    _StaPppstChaRxcha_Type()
)
staPppstChaRxcha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstChaRxcha.setStatus("mandatory")
_StaPppstChaRxres_Type = Integer32
_StaPppstChaRxres_Object = MibScalar
staPppstChaRxres = _StaPppstChaRxres_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 3),
    _StaPppstChaRxres_Type()
)
staPppstChaRxres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstChaRxres.setStatus("mandatory")
_StaPppstChaRxsuc_Type = Integer32
_StaPppstChaRxsuc_Object = MibScalar
staPppstChaRxsuc = _StaPppstChaRxsuc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 4),
    _StaPppstChaRxsuc_Type()
)
staPppstChaRxsuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstChaRxsuc.setStatus("mandatory")
_StaPppstChaRxfai_Type = Integer32
_StaPppstChaRxfai_Object = MibScalar
staPppstChaRxfai = _StaPppstChaRxfai_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 5),
    _StaPppstChaRxfai_Type()
)
staPppstChaRxfai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstChaRxfai.setStatus("mandatory")
_StaPppstChaTxret_Type = Integer32
_StaPppstChaTxret_Object = MibScalar
staPppstChaTxret = _StaPppstChaTxret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 6),
    _StaPppstChaTxret_Type()
)
staPppstChaTxret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstChaTxret.setStatus("mandatory")
_StaPppstChaTxcha_Type = Integer32
_StaPppstChaTxcha_Object = MibScalar
staPppstChaTxcha = _StaPppstChaTxcha_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 7),
    _StaPppstChaTxcha_Type()
)
staPppstChaTxcha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstChaTxcha.setStatus("mandatory")
_StaPppstChaTxres_Type = Integer32
_StaPppstChaTxres_Object = MibScalar
staPppstChaTxres = _StaPppstChaTxres_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 8),
    _StaPppstChaTxres_Type()
)
staPppstChaTxres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstChaTxres.setStatus("mandatory")
_StaPppstChaTxsuc_Type = Integer32
_StaPppstChaTxsuc_Object = MibScalar
staPppstChaTxsuc = _StaPppstChaTxsuc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 9),
    _StaPppstChaTxsuc_Type()
)
staPppstChaTxsuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstChaTxsuc.setStatus("mandatory")
_StaPppstChaTxfai_Type = Integer32
_StaPppstChaTxfai_Object = MibScalar
staPppstChaTxfai = _StaPppstChaTxfai_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 10),
    _StaPppstChaTxfai_Type()
)
staPppstChaTxfai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstChaTxfai.setStatus("mandatory")
_StaPppstChaDelet_Type = Integer32
_StaPppstChaDelet_Object = MibScalar
staPppstChaDelet = _StaPppstChaDelet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 4, 11),
    _StaPppstChaDelet_Type()
)
staPppstChaDelet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staPppstChaDelet.setStatus("mandatory")
_StaPppstIpx_ObjectIdentity = ObjectIdentity
staPppstIpx = _StaPppstIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5)
)
_StaPppstIpxRxdiscarded_Type = Integer32
_StaPppstIpxRxdiscarded_Object = MibScalar
staPppstIpxRxdiscarded = _StaPppstIpxRxdiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 1),
    _StaPppstIpxRxdiscarded_Type()
)
staPppstIpxRxdiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxRxdiscarded.setStatus("mandatory")
_StaPppstIpxRxconfigrequ_Type = Integer32
_StaPppstIpxRxconfigrequ_Object = MibScalar
staPppstIpxRxconfigrequ = _StaPppstIpxRxconfigrequ_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 2),
    _StaPppstIpxRxconfigrequ_Type()
)
staPppstIpxRxconfigrequ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxRxconfigrequ.setStatus("mandatory")
_StaPppstIpxRxconfigack_Type = Integer32
_StaPppstIpxRxconfigack_Object = MibScalar
staPppstIpxRxconfigack = _StaPppstIpxRxconfigack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 3),
    _StaPppstIpxRxconfigack_Type()
)
staPppstIpxRxconfigack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxRxconfigack.setStatus("mandatory")
_StaPppstIpxRxconfignak_Type = Integer32
_StaPppstIpxRxconfignak_Object = MibScalar
staPppstIpxRxconfignak = _StaPppstIpxRxconfignak_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 4),
    _StaPppstIpxRxconfignak_Type()
)
staPppstIpxRxconfignak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxRxconfignak.setStatus("mandatory")
_StaPppstIpxRxconfigreje_Type = Integer32
_StaPppstIpxRxconfigreje_Object = MibScalar
staPppstIpxRxconfigreje = _StaPppstIpxRxconfigreje_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 5),
    _StaPppstIpxRxconfigreje_Type()
)
staPppstIpxRxconfigreje.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxRxconfigreje.setStatus("mandatory")
_StaPppstIpxRxterminater_Type = Integer32
_StaPppstIpxRxterminater_Object = MibScalar
staPppstIpxRxterminater = _StaPppstIpxRxterminater_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 6),
    _StaPppstIpxRxterminater_Type()
)
staPppstIpxRxterminater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxRxterminater.setStatus("mandatory")
_StaPppstIpxRxterminatea_Type = Integer32
_StaPppstIpxRxterminatea_Object = MibScalar
staPppstIpxRxterminatea = _StaPppstIpxRxterminatea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 7),
    _StaPppstIpxRxterminatea_Type()
)
staPppstIpxRxterminatea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxRxterminatea.setStatus("mandatory")
_StaPppstIpxRxcodereject_Type = Integer32
_StaPppstIpxRxcodereject_Object = MibScalar
staPppstIpxRxcodereject = _StaPppstIpxRxcodereject_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 8),
    _StaPppstIpxRxcodereject_Type()
)
staPppstIpxRxcodereject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxRxcodereject.setStatus("mandatory")
_StaPppstIpxTxconfigrequ_Type = Integer32
_StaPppstIpxTxconfigrequ_Object = MibScalar
staPppstIpxTxconfigrequ = _StaPppstIpxTxconfigrequ_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 9),
    _StaPppstIpxTxconfigrequ_Type()
)
staPppstIpxTxconfigrequ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxTxconfigrequ.setStatus("mandatory")
_StaPppstIpxTxconfigack_Type = Integer32
_StaPppstIpxTxconfigack_Object = MibScalar
staPppstIpxTxconfigack = _StaPppstIpxTxconfigack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 10),
    _StaPppstIpxTxconfigack_Type()
)
staPppstIpxTxconfigack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxTxconfigack.setStatus("mandatory")
_StaPppstIpxTxconfignak_Type = Integer32
_StaPppstIpxTxconfignak_Object = MibScalar
staPppstIpxTxconfignak = _StaPppstIpxTxconfignak_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 11),
    _StaPppstIpxTxconfignak_Type()
)
staPppstIpxTxconfignak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxTxconfignak.setStatus("mandatory")
_StaPppstIpxTxconfigreje_Type = Integer32
_StaPppstIpxTxconfigreje_Object = MibScalar
staPppstIpxTxconfigreje = _StaPppstIpxTxconfigreje_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 12),
    _StaPppstIpxTxconfigreje_Type()
)
staPppstIpxTxconfigreje.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxTxconfigreje.setStatus("mandatory")
_StaPppstIpxTxterminater_Type = Integer32
_StaPppstIpxTxterminater_Object = MibScalar
staPppstIpxTxterminater = _StaPppstIpxTxterminater_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 13),
    _StaPppstIpxTxterminater_Type()
)
staPppstIpxTxterminater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxTxterminater.setStatus("mandatory")
_StaPppstIpxTxterminatea_Type = Integer32
_StaPppstIpxTxterminatea_Object = MibScalar
staPppstIpxTxterminatea = _StaPppstIpxTxterminatea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 14),
    _StaPppstIpxTxterminatea_Type()
)
staPppstIpxTxterminatea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxTxterminatea.setStatus("mandatory")
_StaPppstIpxTxcodereject_Type = Integer32
_StaPppstIpxTxcodereject_Object = MibScalar
staPppstIpxTxcodereject = _StaPppstIpxTxcodereject_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 15),
    _StaPppstIpxTxcodereject_Type()
)
staPppstIpxTxcodereject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpxTxcodereject.setStatus("mandatory")
_StaPppstIpxDeletevalues_Type = Integer32
_StaPppstIpxDeletevalues_Object = MibScalar
staPppstIpxDeletevalues = _StaPppstIpxDeletevalues_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 5, 16),
    _StaPppstIpxDeletevalues_Type()
)
staPppstIpxDeletevalues.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staPppstIpxDeletevalues.setStatus("mandatory")
_StaPppstIpc_ObjectIdentity = ObjectIdentity
staPppstIpc = _StaPppstIpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6)
)
_StaPppstIpcRxdiscarded_Type = Integer32
_StaPppstIpcRxdiscarded_Object = MibScalar
staPppstIpcRxdiscarded = _StaPppstIpcRxdiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 1),
    _StaPppstIpcRxdiscarded_Type()
)
staPppstIpcRxdiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcRxdiscarded.setStatus("mandatory")
_StaPppstIpcRxconfigrequ_Type = Integer32
_StaPppstIpcRxconfigrequ_Object = MibScalar
staPppstIpcRxconfigrequ = _StaPppstIpcRxconfigrequ_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 2),
    _StaPppstIpcRxconfigrequ_Type()
)
staPppstIpcRxconfigrequ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcRxconfigrequ.setStatus("mandatory")
_StaPppstIpcRxconfigack_Type = Integer32
_StaPppstIpcRxconfigack_Object = MibScalar
staPppstIpcRxconfigack = _StaPppstIpcRxconfigack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 3),
    _StaPppstIpcRxconfigack_Type()
)
staPppstIpcRxconfigack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcRxconfigack.setStatus("mandatory")
_StaPppstIpcRxconfignak_Type = Integer32
_StaPppstIpcRxconfignak_Object = MibScalar
staPppstIpcRxconfignak = _StaPppstIpcRxconfignak_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 4),
    _StaPppstIpcRxconfignak_Type()
)
staPppstIpcRxconfignak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcRxconfignak.setStatus("mandatory")
_StaPppstIpcRxconfigreje_Type = Integer32
_StaPppstIpcRxconfigreje_Object = MibScalar
staPppstIpcRxconfigreje = _StaPppstIpcRxconfigreje_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 5),
    _StaPppstIpcRxconfigreje_Type()
)
staPppstIpcRxconfigreje.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcRxconfigreje.setStatus("mandatory")
_StaPppstIpcRxterminater_Type = Integer32
_StaPppstIpcRxterminater_Object = MibScalar
staPppstIpcRxterminater = _StaPppstIpcRxterminater_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 6),
    _StaPppstIpcRxterminater_Type()
)
staPppstIpcRxterminater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcRxterminater.setStatus("mandatory")
_StaPppstIpcRxterminatea_Type = Integer32
_StaPppstIpcRxterminatea_Object = MibScalar
staPppstIpcRxterminatea = _StaPppstIpcRxterminatea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 7),
    _StaPppstIpcRxterminatea_Type()
)
staPppstIpcRxterminatea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcRxterminatea.setStatus("mandatory")
_StaPppstIpcRxcodereject_Type = Integer32
_StaPppstIpcRxcodereject_Object = MibScalar
staPppstIpcRxcodereject = _StaPppstIpcRxcodereject_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 8),
    _StaPppstIpcRxcodereject_Type()
)
staPppstIpcRxcodereject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcRxcodereject.setStatus("mandatory")
_StaPppstIpcTxconfigrequ_Type = Integer32
_StaPppstIpcTxconfigrequ_Object = MibScalar
staPppstIpcTxconfigrequ = _StaPppstIpcTxconfigrequ_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 9),
    _StaPppstIpcTxconfigrequ_Type()
)
staPppstIpcTxconfigrequ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcTxconfigrequ.setStatus("mandatory")
_StaPppstIpcTxconfigack_Type = Integer32
_StaPppstIpcTxconfigack_Object = MibScalar
staPppstIpcTxconfigack = _StaPppstIpcTxconfigack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 10),
    _StaPppstIpcTxconfigack_Type()
)
staPppstIpcTxconfigack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcTxconfigack.setStatus("mandatory")
_StaPppstIpcTxconfignak_Type = Integer32
_StaPppstIpcTxconfignak_Object = MibScalar
staPppstIpcTxconfignak = _StaPppstIpcTxconfignak_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 11),
    _StaPppstIpcTxconfignak_Type()
)
staPppstIpcTxconfignak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcTxconfignak.setStatus("mandatory")
_StaPppstIpcTxconfigreje_Type = Integer32
_StaPppstIpcTxconfigreje_Object = MibScalar
staPppstIpcTxconfigreje = _StaPppstIpcTxconfigreje_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 12),
    _StaPppstIpcTxconfigreje_Type()
)
staPppstIpcTxconfigreje.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcTxconfigreje.setStatus("mandatory")
_StaPppstIpcTxterminater_Type = Integer32
_StaPppstIpcTxterminater_Object = MibScalar
staPppstIpcTxterminater = _StaPppstIpcTxterminater_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 13),
    _StaPppstIpcTxterminater_Type()
)
staPppstIpcTxterminater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcTxterminater.setStatus("mandatory")
_StaPppstIpcTxterminatea_Type = Integer32
_StaPppstIpcTxterminatea_Object = MibScalar
staPppstIpcTxterminatea = _StaPppstIpcTxterminatea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 14),
    _StaPppstIpcTxterminatea_Type()
)
staPppstIpcTxterminatea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcTxterminatea.setStatus("mandatory")
_StaPppstIpcTxcodereject_Type = Integer32
_StaPppstIpcTxcodereject_Object = MibScalar
staPppstIpcTxcodereject = _StaPppstIpcTxcodereject_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 15),
    _StaPppstIpcTxcodereject_Type()
)
staPppstIpcTxcodereject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstIpcTxcodereject.setStatus("mandatory")
_StaPppstIpcDeletevalues_Type = Integer32
_StaPppstIpcDeletevalues_Object = MibScalar
staPppstIpcDeletevalues = _StaPppstIpcDeletevalues_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 6, 16),
    _StaPppstIpcDeletevalues_Type()
)
staPppstIpcDeletevalues.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staPppstIpcDeletevalues.setStatus("mandatory")
_StaPppstCbc_ObjectIdentity = ObjectIdentity
staPppstCbc = _StaPppstCbc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 7)
)
_StaPppstCbcRxdis_Type = Integer32
_StaPppstCbcRxdis_Object = MibScalar
staPppstCbcRxdis = _StaPppstCbcRxdis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 7, 1),
    _StaPppstCbcRxdis_Type()
)
staPppstCbcRxdis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCbcRxdis.setStatus("mandatory")
_StaPppstCbcRxreq_Type = Integer32
_StaPppstCbcRxreq_Object = MibScalar
staPppstCbcRxreq = _StaPppstCbcRxreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 7, 2),
    _StaPppstCbcRxreq_Type()
)
staPppstCbcRxreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCbcRxreq.setStatus("mandatory")
_StaPppstCbcRxres_Type = Integer32
_StaPppstCbcRxres_Object = MibScalar
staPppstCbcRxres = _StaPppstCbcRxres_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 7, 3),
    _StaPppstCbcRxres_Type()
)
staPppstCbcRxres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCbcRxres.setStatus("mandatory")
_StaPppstCbcRxack_Type = Integer32
_StaPppstCbcRxack_Object = MibScalar
staPppstCbcRxack = _StaPppstCbcRxack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 7, 4),
    _StaPppstCbcRxack_Type()
)
staPppstCbcRxack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCbcRxack.setStatus("mandatory")
_StaPppstCbcTxreq_Type = Integer32
_StaPppstCbcTxreq_Object = MibScalar
staPppstCbcTxreq = _StaPppstCbcTxreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 7, 5),
    _StaPppstCbcTxreq_Type()
)
staPppstCbcTxreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCbcTxreq.setStatus("mandatory")
_StaPppstCbcTxres_Type = Integer32
_StaPppstCbcTxres_Object = MibScalar
staPppstCbcTxres = _StaPppstCbcTxres_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 7, 6),
    _StaPppstCbcTxres_Type()
)
staPppstCbcTxres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCbcTxres.setStatus("mandatory")
_StaPppstCbcTxack_Type = Integer32
_StaPppstCbcTxack_Object = MibScalar
staPppstCbcTxack = _StaPppstCbcTxack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 7, 7),
    _StaPppstCbcTxack_Type()
)
staPppstCbcTxack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCbcTxack.setStatus("mandatory")
_StaPppstCbcDelet_Type = Integer32
_StaPppstCbcDelet_Object = MibScalar
staPppstCbcDelet = _StaPppstCbcDelet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 7, 8),
    _StaPppstCbcDelet_Type()
)
staPppstCbcDelet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staPppstCbcDelet.setStatus("mandatory")
_StaPppstRxo_ObjectIdentity = ObjectIdentity
staPppstRxo = _StaPppstRxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8)
)
_StaPppstRxoLcp_Object = MibTable
staPppstRxoLcp = _StaPppstRxoLcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 1)
)
if mibBuilder.loadTexts:
    staPppstRxoLcp.setStatus("mandatory")
_StaPppstRxoLcpCols_Object = MibTableRow
staPppstRxoLcpCols = _StaPppstRxoLcpCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 1, 1)
)
staPppstRxoLcpCols.setIndexNames(
    (0, "ELSA-MIB", "staPppstRxoLcpIfc"),
)
if mibBuilder.loadTexts:
    staPppstRxoLcpCols.setStatus("mandatory")


class _StaPppstRxoLcpIfc_Type(Integer32):
    """Custom type staPppstRxoLcpIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaPppstRxoLcpIfc_Type.__name__ = "Integer32"
_StaPppstRxoLcpIfc_Object = MibTableColumn
staPppstRxoLcpIfc = _StaPppstRxoLcpIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 1, 1, 1),
    _StaPppstRxoLcpIfc_Type()
)
staPppstRxoLcpIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoLcpIfc.setStatus("mandatory")
_StaPppstRxoLcpMru_Type = Integer32
_StaPppstRxoLcpMru_Object = MibTableColumn
staPppstRxoLcpMru = _StaPppstRxoLcpMru_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 1, 1, 2),
    _StaPppstRxoLcpMru_Type()
)
staPppstRxoLcpMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoLcpMru.setStatus("mandatory")
_StaPppstRxoLcpAcc_Type = DisplayString
_StaPppstRxoLcpAcc_Object = MibTableColumn
staPppstRxoLcpAcc = _StaPppstRxoLcpAcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 1, 1, 3),
    _StaPppstRxoLcpAcc_Type()
)
staPppstRxoLcpAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoLcpAcc.setStatus("mandatory")


class _StaPppstRxoLcpAut_Type(Integer32):
    """Custom type staPppstRxoLcpAut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("chap", 8),
          ("none", 0),
          ("pap", 4))
    )


_StaPppstRxoLcpAut_Type.__name__ = "Integer32"
_StaPppstRxoLcpAut_Object = MibTableColumn
staPppstRxoLcpAut = _StaPppstRxoLcpAut_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 1, 1, 4),
    _StaPppstRxoLcpAut_Type()
)
staPppstRxoLcpAut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoLcpAut.setStatus("mandatory")


class _StaPppstRxoLcpCal_Type(Integer32):
    """Custom type staPppstRxoLcpCal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cbcp", 6),
          ("lcp", 5),
          ("none", 255))
    )


_StaPppstRxoLcpCal_Type.__name__ = "Integer32"
_StaPppstRxoLcpCal_Object = MibTableColumn
staPppstRxoLcpCal = _StaPppstRxoLcpCal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 1, 1, 5),
    _StaPppstRxoLcpCal_Type()
)
staPppstRxoLcpCal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoLcpCal.setStatus("mandatory")
_StaPppstRxoLcpMag_Type = DisplayString
_StaPppstRxoLcpMag_Object = MibTableColumn
staPppstRxoLcpMag = _StaPppstRxoLcpMag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 1, 1, 6),
    _StaPppstRxoLcpMag_Type()
)
staPppstRxoLcpMag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoLcpMag.setStatus("mandatory")


class _StaPppstRxoLcpPfc_Type(Integer32):
    """Custom type staPppstRxoLcpPfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_StaPppstRxoLcpPfc_Type.__name__ = "Integer32"
_StaPppstRxoLcpPfc_Object = MibTableColumn
staPppstRxoLcpPfc = _StaPppstRxoLcpPfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 1, 1, 7),
    _StaPppstRxoLcpPfc_Type()
)
staPppstRxoLcpPfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoLcpPfc.setStatus("mandatory")


class _StaPppstRxoLcpAcf_Type(Integer32):
    """Custom type staPppstRxoLcpAcf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_StaPppstRxoLcpAcf_Type.__name__ = "Integer32"
_StaPppstRxoLcpAcf_Object = MibTableColumn
staPppstRxoLcpAcf = _StaPppstRxoLcpAcf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 1, 1, 8),
    _StaPppstRxoLcpAcf_Type()
)
staPppstRxoLcpAcf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoLcpAcf.setStatus("mandatory")
_StaPppstRxoIpx_Object = MibTable
staPppstRxoIpx = _StaPppstRxoIpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 2)
)
if mibBuilder.loadTexts:
    staPppstRxoIpx.setStatus("mandatory")
_StaPppstRxoIpxCols_Object = MibTableRow
staPppstRxoIpxCols = _StaPppstRxoIpxCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 2, 1)
)
staPppstRxoIpxCols.setIndexNames(
    (0, "ELSA-MIB", "staPppstRxoIpxIfc"),
)
if mibBuilder.loadTexts:
    staPppstRxoIpxCols.setStatus("mandatory")


class _StaPppstRxoIpxIfc_Type(Integer32):
    """Custom type staPppstRxoIpxIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaPppstRxoIpxIfc_Type.__name__ = "Integer32"
_StaPppstRxoIpxIfc_Object = MibTableColumn
staPppstRxoIpxIfc = _StaPppstRxoIpxIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 2, 1, 1),
    _StaPppstRxoIpxIfc_Type()
)
staPppstRxoIpxIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoIpxIfc.setStatus("mandatory")
_StaPppstRxoIpxNet_Type = DisplayString
_StaPppstRxoIpxNet_Object = MibTableColumn
staPppstRxoIpxNet = _StaPppstRxoIpxNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 2, 1, 2),
    _StaPppstRxoIpxNet_Type()
)
staPppstRxoIpxNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoIpxNet.setStatus("mandatory")
_StaPppstRxoIpxNod_Type = DisplayString
_StaPppstRxoIpxNod_Object = MibTableColumn
staPppstRxoIpxNod = _StaPppstRxoIpxNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 2, 1, 3),
    _StaPppstRxoIpxNod_Type()
)
staPppstRxoIpxNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoIpxNod.setStatus("mandatory")


class _StaPppstRxoIpxRou_Type(Integer32):
    """Custom type staPppstRxoIpxRou based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nlsp", 4),
          ("none", 0),
          ("rip-sap", 2))
    )


_StaPppstRxoIpxRou_Type.__name__ = "Integer32"
_StaPppstRxoIpxRou_Object = MibTableColumn
staPppstRxoIpxRou = _StaPppstRxoIpxRou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 2, 1, 4),
    _StaPppstRxoIpxRou_Type()
)
staPppstRxoIpxRou.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoIpxRou.setStatus("mandatory")
_StaPppstRxoIpc_Object = MibTable
staPppstRxoIpc = _StaPppstRxoIpc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 3)
)
if mibBuilder.loadTexts:
    staPppstRxoIpc.setStatus("mandatory")
_StaPppstRxoIpcCols_Object = MibTableRow
staPppstRxoIpcCols = _StaPppstRxoIpcCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 3, 1)
)
staPppstRxoIpcCols.setIndexNames(
    (0, "ELSA-MIB", "staPppstRxoIpcIfc"),
)
if mibBuilder.loadTexts:
    staPppstRxoIpcCols.setStatus("mandatory")


class _StaPppstRxoIpcIfc_Type(Integer32):
    """Custom type staPppstRxoIpcIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaPppstRxoIpcIfc_Type.__name__ = "Integer32"
_StaPppstRxoIpcIfc_Object = MibTableColumn
staPppstRxoIpcIfc = _StaPppstRxoIpcIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 3, 1, 1),
    _StaPppstRxoIpcIfc_Type()
)
staPppstRxoIpcIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoIpcIfc.setStatus("mandatory")
_StaPppstRxoIpcIpa_Type = IpAddress
_StaPppstRxoIpcIpa_Object = MibTableColumn
staPppstRxoIpcIpa = _StaPppstRxoIpcIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 3, 1, 2),
    _StaPppstRxoIpcIpa_Type()
)
staPppstRxoIpcIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoIpcIpa.setStatus("mandatory")
_StaPppstRxoIpcDns_Type = IpAddress
_StaPppstRxoIpcDns_Object = MibTableColumn
staPppstRxoIpcDns = _StaPppstRxoIpcDns_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 3, 1, 3),
    _StaPppstRxoIpcDns_Type()
)
staPppstRxoIpcDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoIpcDns.setStatus("mandatory")
_StaPppstRxoIpcNbn_Type = IpAddress
_StaPppstRxoIpcNbn_Object = MibTableColumn
staPppstRxoIpcNbn = _StaPppstRxoIpcNbn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 8, 3, 1, 4),
    _StaPppstRxoIpcNbn_Type()
)
staPppstRxoIpcNbn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstRxoIpcNbn.setStatus("mandatory")
_StaPppstTxo_ObjectIdentity = ObjectIdentity
staPppstTxo = _StaPppstTxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9)
)
_StaPppstTxoLcp_Object = MibTable
staPppstTxoLcp = _StaPppstTxoLcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 1)
)
if mibBuilder.loadTexts:
    staPppstTxoLcp.setStatus("mandatory")
_StaPppstTxoLcpCols_Object = MibTableRow
staPppstTxoLcpCols = _StaPppstTxoLcpCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 1, 1)
)
staPppstTxoLcpCols.setIndexNames(
    (0, "ELSA-MIB", "staPppstTxoLcpIfc"),
)
if mibBuilder.loadTexts:
    staPppstTxoLcpCols.setStatus("mandatory")


class _StaPppstTxoLcpIfc_Type(Integer32):
    """Custom type staPppstTxoLcpIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaPppstTxoLcpIfc_Type.__name__ = "Integer32"
_StaPppstTxoLcpIfc_Object = MibTableColumn
staPppstTxoLcpIfc = _StaPppstTxoLcpIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 1, 1, 1),
    _StaPppstTxoLcpIfc_Type()
)
staPppstTxoLcpIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoLcpIfc.setStatus("mandatory")
_StaPppstTxoLcpMru_Type = Integer32
_StaPppstTxoLcpMru_Object = MibTableColumn
staPppstTxoLcpMru = _StaPppstTxoLcpMru_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 1, 1, 2),
    _StaPppstTxoLcpMru_Type()
)
staPppstTxoLcpMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoLcpMru.setStatus("mandatory")
_StaPppstTxoLcpAcc_Type = DisplayString
_StaPppstTxoLcpAcc_Object = MibTableColumn
staPppstTxoLcpAcc = _StaPppstTxoLcpAcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 1, 1, 3),
    _StaPppstTxoLcpAcc_Type()
)
staPppstTxoLcpAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoLcpAcc.setStatus("mandatory")


class _StaPppstTxoLcpAut_Type(Integer32):
    """Custom type staPppstTxoLcpAut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("chap", 8),
          ("none", 0),
          ("pap", 4))
    )


_StaPppstTxoLcpAut_Type.__name__ = "Integer32"
_StaPppstTxoLcpAut_Object = MibTableColumn
staPppstTxoLcpAut = _StaPppstTxoLcpAut_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 1, 1, 4),
    _StaPppstTxoLcpAut_Type()
)
staPppstTxoLcpAut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoLcpAut.setStatus("mandatory")


class _StaPppstTxoLcpCal_Type(Integer32):
    """Custom type staPppstTxoLcpCal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cbcp", 6),
          ("lcp", 5),
          ("none", 255))
    )


_StaPppstTxoLcpCal_Type.__name__ = "Integer32"
_StaPppstTxoLcpCal_Object = MibTableColumn
staPppstTxoLcpCal = _StaPppstTxoLcpCal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 1, 1, 5),
    _StaPppstTxoLcpCal_Type()
)
staPppstTxoLcpCal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoLcpCal.setStatus("mandatory")
_StaPppstTxoLcpMag_Type = DisplayString
_StaPppstTxoLcpMag_Object = MibTableColumn
staPppstTxoLcpMag = _StaPppstTxoLcpMag_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 1, 1, 6),
    _StaPppstTxoLcpMag_Type()
)
staPppstTxoLcpMag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoLcpMag.setStatus("mandatory")


class _StaPppstTxoLcpPfc_Type(Integer32):
    """Custom type staPppstTxoLcpPfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_StaPppstTxoLcpPfc_Type.__name__ = "Integer32"
_StaPppstTxoLcpPfc_Object = MibTableColumn
staPppstTxoLcpPfc = _StaPppstTxoLcpPfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 1, 1, 7),
    _StaPppstTxoLcpPfc_Type()
)
staPppstTxoLcpPfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoLcpPfc.setStatus("mandatory")


class _StaPppstTxoLcpAcf_Type(Integer32):
    """Custom type staPppstTxoLcpAcf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_StaPppstTxoLcpAcf_Type.__name__ = "Integer32"
_StaPppstTxoLcpAcf_Object = MibTableColumn
staPppstTxoLcpAcf = _StaPppstTxoLcpAcf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 1, 1, 8),
    _StaPppstTxoLcpAcf_Type()
)
staPppstTxoLcpAcf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoLcpAcf.setStatus("mandatory")
_StaPppstTxoIpx_Object = MibTable
staPppstTxoIpx = _StaPppstTxoIpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 2)
)
if mibBuilder.loadTexts:
    staPppstTxoIpx.setStatus("mandatory")
_StaPppstTxoIpxCols_Object = MibTableRow
staPppstTxoIpxCols = _StaPppstTxoIpxCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 2, 1)
)
staPppstTxoIpxCols.setIndexNames(
    (0, "ELSA-MIB", "staPppstTxoIpxIfc"),
)
if mibBuilder.loadTexts:
    staPppstTxoIpxCols.setStatus("mandatory")


class _StaPppstTxoIpxIfc_Type(Integer32):
    """Custom type staPppstTxoIpxIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaPppstTxoIpxIfc_Type.__name__ = "Integer32"
_StaPppstTxoIpxIfc_Object = MibTableColumn
staPppstTxoIpxIfc = _StaPppstTxoIpxIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 2, 1, 1),
    _StaPppstTxoIpxIfc_Type()
)
staPppstTxoIpxIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoIpxIfc.setStatus("mandatory")
_StaPppstTxoIpxNet_Type = DisplayString
_StaPppstTxoIpxNet_Object = MibTableColumn
staPppstTxoIpxNet = _StaPppstTxoIpxNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 2, 1, 2),
    _StaPppstTxoIpxNet_Type()
)
staPppstTxoIpxNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoIpxNet.setStatus("mandatory")
_StaPppstTxoIpxNod_Type = DisplayString
_StaPppstTxoIpxNod_Object = MibTableColumn
staPppstTxoIpxNod = _StaPppstTxoIpxNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 2, 1, 3),
    _StaPppstTxoIpxNod_Type()
)
staPppstTxoIpxNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoIpxNod.setStatus("mandatory")


class _StaPppstTxoIpxRou_Type(Integer32):
    """Custom type staPppstTxoIpxRou based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nlsp", 4),
          ("none", 0),
          ("rip-sap", 2))
    )


_StaPppstTxoIpxRou_Type.__name__ = "Integer32"
_StaPppstTxoIpxRou_Object = MibTableColumn
staPppstTxoIpxRou = _StaPppstTxoIpxRou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 2, 1, 4),
    _StaPppstTxoIpxRou_Type()
)
staPppstTxoIpxRou.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoIpxRou.setStatus("mandatory")
_StaPppstTxoIpc_Object = MibTable
staPppstTxoIpc = _StaPppstTxoIpc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 3)
)
if mibBuilder.loadTexts:
    staPppstTxoIpc.setStatus("mandatory")
_StaPppstTxoIpcCols_Object = MibTableRow
staPppstTxoIpcCols = _StaPppstTxoIpcCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 3, 1)
)
staPppstTxoIpcCols.setIndexNames(
    (0, "ELSA-MIB", "staPppstTxoIpcIfc"),
)
if mibBuilder.loadTexts:
    staPppstTxoIpcCols.setStatus("mandatory")


class _StaPppstTxoIpcIfc_Type(Integer32):
    """Custom type staPppstTxoIpcIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaPppstTxoIpcIfc_Type.__name__ = "Integer32"
_StaPppstTxoIpcIfc_Object = MibTableColumn
staPppstTxoIpcIfc = _StaPppstTxoIpcIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 3, 1, 1),
    _StaPppstTxoIpcIfc_Type()
)
staPppstTxoIpcIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoIpcIfc.setStatus("mandatory")
_StaPppstTxoIpcIpa_Type = IpAddress
_StaPppstTxoIpcIpa_Object = MibTableColumn
staPppstTxoIpcIpa = _StaPppstTxoIpcIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 3, 1, 2),
    _StaPppstTxoIpcIpa_Type()
)
staPppstTxoIpcIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoIpcIpa.setStatus("mandatory")
_StaPppstTxoIpcDns_Type = IpAddress
_StaPppstTxoIpcDns_Object = MibTableColumn
staPppstTxoIpcDns = _StaPppstTxoIpcDns_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 3, 1, 3),
    _StaPppstTxoIpcDns_Type()
)
staPppstTxoIpcDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoIpcDns.setStatus("mandatory")
_StaPppstTxoIpcNbn_Type = IpAddress
_StaPppstTxoIpcNbn_Object = MibTableColumn
staPppstTxoIpcNbn = _StaPppstTxoIpcNbn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 9, 3, 1, 4),
    _StaPppstTxoIpcNbn_Type()
)
staPppstTxoIpcNbn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstTxoIpcNbn.setStatus("mandatory")
_StaPppstCcp_ObjectIdentity = ObjectIdentity
staPppstCcp = _StaPppstCcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10)
)
_StaPppstCcpRxdiscarded_Type = Integer32
_StaPppstCcpRxdiscarded_Object = MibScalar
staPppstCcpRxdiscarded = _StaPppstCcpRxdiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 1),
    _StaPppstCcpRxdiscarded_Type()
)
staPppstCcpRxdiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpRxdiscarded.setStatus("mandatory")
_StaPppstCcpRxconfigrequ_Type = Integer32
_StaPppstCcpRxconfigrequ_Object = MibScalar
staPppstCcpRxconfigrequ = _StaPppstCcpRxconfigrequ_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 2),
    _StaPppstCcpRxconfigrequ_Type()
)
staPppstCcpRxconfigrequ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpRxconfigrequ.setStatus("mandatory")
_StaPppstCcpRxconfigack_Type = Integer32
_StaPppstCcpRxconfigack_Object = MibScalar
staPppstCcpRxconfigack = _StaPppstCcpRxconfigack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 3),
    _StaPppstCcpRxconfigack_Type()
)
staPppstCcpRxconfigack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpRxconfigack.setStatus("mandatory")
_StaPppstCcpRxconfignak_Type = Integer32
_StaPppstCcpRxconfignak_Object = MibScalar
staPppstCcpRxconfignak = _StaPppstCcpRxconfignak_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 4),
    _StaPppstCcpRxconfignak_Type()
)
staPppstCcpRxconfignak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpRxconfignak.setStatus("mandatory")
_StaPppstCcpRxconfigreje_Type = Integer32
_StaPppstCcpRxconfigreje_Object = MibScalar
staPppstCcpRxconfigreje = _StaPppstCcpRxconfigreje_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 5),
    _StaPppstCcpRxconfigreje_Type()
)
staPppstCcpRxconfigreje.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpRxconfigreje.setStatus("mandatory")
_StaPppstCcpRxterminater_Type = Integer32
_StaPppstCcpRxterminater_Object = MibScalar
staPppstCcpRxterminater = _StaPppstCcpRxterminater_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 6),
    _StaPppstCcpRxterminater_Type()
)
staPppstCcpRxterminater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpRxterminater.setStatus("mandatory")
_StaPppstCcpRxterminatea_Type = Integer32
_StaPppstCcpRxterminatea_Object = MibScalar
staPppstCcpRxterminatea = _StaPppstCcpRxterminatea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 7),
    _StaPppstCcpRxterminatea_Type()
)
staPppstCcpRxterminatea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpRxterminatea.setStatus("mandatory")
_StaPppstCcpRxcodereject_Type = Integer32
_StaPppstCcpRxcodereject_Object = MibScalar
staPppstCcpRxcodereject = _StaPppstCcpRxcodereject_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 8),
    _StaPppstCcpRxcodereject_Type()
)
staPppstCcpRxcodereject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpRxcodereject.setStatus("mandatory")
_StaPppstCcpRxresetreque_Type = Integer32
_StaPppstCcpRxresetreque_Object = MibScalar
staPppstCcpRxresetreque = _StaPppstCcpRxresetreque_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 9),
    _StaPppstCcpRxresetreque_Type()
)
staPppstCcpRxresetreque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpRxresetreque.setStatus("mandatory")
_StaPppstCcpRxresetack_Type = Integer32
_StaPppstCcpRxresetack_Object = MibScalar
staPppstCcpRxresetack = _StaPppstCcpRxresetack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 10),
    _StaPppstCcpRxresetack_Type()
)
staPppstCcpRxresetack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpRxresetack.setStatus("mandatory")
_StaPppstCcpTxconfigrequ_Type = Integer32
_StaPppstCcpTxconfigrequ_Object = MibScalar
staPppstCcpTxconfigrequ = _StaPppstCcpTxconfigrequ_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 11),
    _StaPppstCcpTxconfigrequ_Type()
)
staPppstCcpTxconfigrequ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpTxconfigrequ.setStatus("mandatory")
_StaPppstCcpTxconfigack_Type = Integer32
_StaPppstCcpTxconfigack_Object = MibScalar
staPppstCcpTxconfigack = _StaPppstCcpTxconfigack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 12),
    _StaPppstCcpTxconfigack_Type()
)
staPppstCcpTxconfigack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpTxconfigack.setStatus("mandatory")
_StaPppstCcpTxconfignak_Type = Integer32
_StaPppstCcpTxconfignak_Object = MibScalar
staPppstCcpTxconfignak = _StaPppstCcpTxconfignak_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 13),
    _StaPppstCcpTxconfignak_Type()
)
staPppstCcpTxconfignak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpTxconfignak.setStatus("mandatory")
_StaPppstCcpTxconfigreje_Type = Integer32
_StaPppstCcpTxconfigreje_Object = MibScalar
staPppstCcpTxconfigreje = _StaPppstCcpTxconfigreje_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 14),
    _StaPppstCcpTxconfigreje_Type()
)
staPppstCcpTxconfigreje.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpTxconfigreje.setStatus("mandatory")
_StaPppstCcpTxterminater_Type = Integer32
_StaPppstCcpTxterminater_Object = MibScalar
staPppstCcpTxterminater = _StaPppstCcpTxterminater_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 15),
    _StaPppstCcpTxterminater_Type()
)
staPppstCcpTxterminater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpTxterminater.setStatus("mandatory")
_StaPppstCcpTxterminatea_Type = Integer32
_StaPppstCcpTxterminatea_Object = MibScalar
staPppstCcpTxterminatea = _StaPppstCcpTxterminatea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 16),
    _StaPppstCcpTxterminatea_Type()
)
staPppstCcpTxterminatea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpTxterminatea.setStatus("mandatory")
_StaPppstCcpTxcodereject_Type = Integer32
_StaPppstCcpTxcodereject_Object = MibScalar
staPppstCcpTxcodereject = _StaPppstCcpTxcodereject_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 17),
    _StaPppstCcpTxcodereject_Type()
)
staPppstCcpTxcodereject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpTxcodereject.setStatus("mandatory")
_StaPppstCcpTxresetreque_Type = Integer32
_StaPppstCcpTxresetreque_Object = MibScalar
staPppstCcpTxresetreque = _StaPppstCcpTxresetreque_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 19),
    _StaPppstCcpTxresetreque_Type()
)
staPppstCcpTxresetreque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpTxresetreque.setStatus("mandatory")
_StaPppstCcpTxresetack_Type = Integer32
_StaPppstCcpTxresetack_Object = MibScalar
staPppstCcpTxresetack = _StaPppstCcpTxresetack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 20),
    _StaPppstCcpTxresetack_Type()
)
staPppstCcpTxresetack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpTxresetack.setStatus("mandatory")
_StaPppstCcpDeletevalues_Type = Integer32
_StaPppstCcpDeletevalues_Object = MibScalar
staPppstCcpDeletevalues = _StaPppstCcpDeletevalues_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 21),
    _StaPppstCcpDeletevalues_Type()
)
staPppstCcpDeletevalues.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staPppstCcpDeletevalues.setStatus("mandatory")
_StaPppstCcpCompressione_Type = Integer32
_StaPppstCcpCompressione_Object = MibScalar
staPppstCcpCompressione = _StaPppstCcpCompressione_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 10, 22),
    _StaPppstCcpCompressione_Type()
)
staPppstCcpCompressione.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstCcpCompressione.setStatus("mandatory")
_StaPppstMls_ObjectIdentity = ObjectIdentity
staPppstMls = _StaPppstMls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11)
)
_StaPppstMlsBundlec_Type = Integer32
_StaPppstMlsBundlec_Object = MibScalar
staPppstMlsBundlec = _StaPppstMlsBundlec_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 1),
    _StaPppstMlsBundlec_Type()
)
staPppstMlsBundlec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstMlsBundlec.setStatus("mandatory")
_StaPppstMlsRxseqlo_Type = Integer32
_StaPppstMlsRxseqlo_Object = MibScalar
staPppstMlsRxseqlo = _StaPppstMlsRxseqlo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 2),
    _StaPppstMlsRxseqlo_Type()
)
staPppstMlsRxseqlo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstMlsRxseqlo.setStatus("mandatory")
_StaPppstMlsRxseqre_Type = Integer32
_StaPppstMlsRxseqre_Object = MibScalar
staPppstMlsRxseqre = _StaPppstMlsRxseqre_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 3),
    _StaPppstMlsRxseqre_Type()
)
staPppstMlsRxseqre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstMlsRxseqre.setStatus("mandatory")
_StaPppstMlsRxmrrue_Type = Integer32
_StaPppstMlsRxmrrue_Object = MibScalar
staPppstMlsRxmrrue = _StaPppstMlsRxmrrue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 4),
    _StaPppstMlsRxmrrue_Type()
)
staPppstMlsRxmrrue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstMlsRxmrrue.setStatus("mandatory")
_StaPppstMlsRxheade_Type = Integer32
_StaPppstMlsRxheade_Object = MibScalar
staPppstMlsRxheade = _StaPppstMlsRxheade_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 5),
    _StaPppstMlsRxheade_Type()
)
staPppstMlsRxheade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstMlsRxheade.setStatus("mandatory")
_StaPppstMlsRxdisca_Type = Integer32
_StaPppstMlsRxdisca_Object = MibScalar
staPppstMlsRxdisca = _StaPppstMlsRxdisca_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 6),
    _StaPppstMlsRxdisca_Type()
)
staPppstMlsRxdisca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstMlsRxdisca.setStatus("mandatory")
_StaPppstMlsRxfrags_Type = Integer32
_StaPppstMlsRxfrags_Object = MibScalar
staPppstMlsRxfrags = _StaPppstMlsRxfrags_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 7),
    _StaPppstMlsRxfrags_Type()
)
staPppstMlsRxfrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstMlsRxfrags.setStatus("mandatory")
_StaPppstMlsRxfragm_Type = Integer32
_StaPppstMlsRxfragm_Object = MibScalar
staPppstMlsRxfragm = _StaPppstMlsRxfragm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 8),
    _StaPppstMlsRxfragm_Type()
)
staPppstMlsRxfragm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstMlsRxfragm.setStatus("mandatory")
_StaPppstMlsRxfrage_Type = Integer32
_StaPppstMlsRxfrage_Object = MibScalar
staPppstMlsRxfrage = _StaPppstMlsRxfrage_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 9),
    _StaPppstMlsRxfrage_Type()
)
staPppstMlsRxfrage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstMlsRxfrage.setStatus("mandatory")
_StaPppstMlsRxnotfr_Type = Integer32
_StaPppstMlsRxnotfr_Object = MibScalar
staPppstMlsRxnotfr = _StaPppstMlsRxnotfr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 10),
    _StaPppstMlsRxnotfr_Type()
)
staPppstMlsRxnotfr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstMlsRxnotfr.setStatus("mandatory")
_StaPppstMlsDeletev_Type = Integer32
_StaPppstMlsDeletev_Object = MibScalar
staPppstMlsDeletev = _StaPppstMlsDeletev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 11, 11),
    _StaPppstMlsDeletev_Type()
)
staPppstMlsDeletev.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staPppstMlsDeletev.setStatus("mandatory")
_StaPppstBac_ObjectIdentity = ObjectIdentity
staPppstBac = _StaPppstBac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12)
)
_StaPppstBacRxerrors_Type = Integer32
_StaPppstBacRxerrors_Object = MibScalar
staPppstBacRxerrors = _StaPppstBacRxerrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 1),
    _StaPppstBacRxerrors_Type()
)
staPppstBacRxerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacRxerrors.setStatus("mandatory")
_StaPppstBacRxdiscarded_Type = Integer32
_StaPppstBacRxdiscarded_Object = MibScalar
staPppstBacRxdiscarded = _StaPppstBacRxdiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 2),
    _StaPppstBacRxdiscarded_Type()
)
staPppstBacRxdiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacRxdiscarded.setStatus("mandatory")
_StaPppstBacRxcallrequest_Type = Integer32
_StaPppstBacRxcallrequest_Object = MibScalar
staPppstBacRxcallrequest = _StaPppstBacRxcallrequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 3),
    _StaPppstBacRxcallrequest_Type()
)
staPppstBacRxcallrequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacRxcallrequest.setStatus("mandatory")
_StaPppstBacRxcallrespons_Type = Integer32
_StaPppstBacRxcallrespons_Object = MibScalar
staPppstBacRxcallrespons = _StaPppstBacRxcallrespons_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 4),
    _StaPppstBacRxcallrespons_Type()
)
staPppstBacRxcallrespons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacRxcallrespons.setStatus("mandatory")
_StaPppstBacRxcallbackreq_Type = Integer32
_StaPppstBacRxcallbackreq_Object = MibScalar
staPppstBacRxcallbackreq = _StaPppstBacRxcallbackreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 5),
    _StaPppstBacRxcallbackreq_Type()
)
staPppstBacRxcallbackreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacRxcallbackreq.setStatus("mandatory")
_StaPppstBacRxcallbackres_Type = Integer32
_StaPppstBacRxcallbackres_Object = MibScalar
staPppstBacRxcallbackres = _StaPppstBacRxcallbackres_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 6),
    _StaPppstBacRxcallbackres_Type()
)
staPppstBacRxcallbackres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacRxcallbackres.setStatus("mandatory")
_StaPppstBacRxlinkdropreq_Type = Integer32
_StaPppstBacRxlinkdropreq_Object = MibScalar
staPppstBacRxlinkdropreq = _StaPppstBacRxlinkdropreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 7),
    _StaPppstBacRxlinkdropreq_Type()
)
staPppstBacRxlinkdropreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacRxlinkdropreq.setStatus("mandatory")
_StaPppstBacRxlinkdropres_Type = Integer32
_StaPppstBacRxlinkdropres_Object = MibScalar
staPppstBacRxlinkdropres = _StaPppstBacRxlinkdropres_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 8),
    _StaPppstBacRxlinkdropres_Type()
)
staPppstBacRxlinkdropres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacRxlinkdropres.setStatus("mandatory")
_StaPppstBacRxstatusindic_Type = Integer32
_StaPppstBacRxstatusindic_Object = MibScalar
staPppstBacRxstatusindic = _StaPppstBacRxstatusindic_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 9),
    _StaPppstBacRxstatusindic_Type()
)
staPppstBacRxstatusindic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacRxstatusindic.setStatus("mandatory")
_StaPppstBacRxstatusreson_Type = Integer32
_StaPppstBacRxstatusreson_Object = MibScalar
staPppstBacRxstatusreson = _StaPppstBacRxstatusreson_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 10),
    _StaPppstBacRxstatusreson_Type()
)
staPppstBacRxstatusreson.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacRxstatusreson.setStatus("mandatory")
_StaPppstBacTxcallrequest_Type = Integer32
_StaPppstBacTxcallrequest_Object = MibScalar
staPppstBacTxcallrequest = _StaPppstBacTxcallrequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 11),
    _StaPppstBacTxcallrequest_Type()
)
staPppstBacTxcallrequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacTxcallrequest.setStatus("mandatory")
_StaPppstBacTxcallrespons_Type = Integer32
_StaPppstBacTxcallrespons_Object = MibScalar
staPppstBacTxcallrespons = _StaPppstBacTxcallrespons_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 12),
    _StaPppstBacTxcallrespons_Type()
)
staPppstBacTxcallrespons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacTxcallrespons.setStatus("mandatory")
_StaPppstBacTxcallbackreq_Type = Integer32
_StaPppstBacTxcallbackreq_Object = MibScalar
staPppstBacTxcallbackreq = _StaPppstBacTxcallbackreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 13),
    _StaPppstBacTxcallbackreq_Type()
)
staPppstBacTxcallbackreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacTxcallbackreq.setStatus("mandatory")
_StaPppstBacTxcallbackres_Type = Integer32
_StaPppstBacTxcallbackres_Object = MibScalar
staPppstBacTxcallbackres = _StaPppstBacTxcallbackres_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 14),
    _StaPppstBacTxcallbackres_Type()
)
staPppstBacTxcallbackres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacTxcallbackres.setStatus("mandatory")
_StaPppstBacTxlinkdropreq_Type = Integer32
_StaPppstBacTxlinkdropreq_Object = MibScalar
staPppstBacTxlinkdropreq = _StaPppstBacTxlinkdropreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 15),
    _StaPppstBacTxlinkdropreq_Type()
)
staPppstBacTxlinkdropreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacTxlinkdropreq.setStatus("mandatory")
_StaPppstBacTxlinkdropres_Type = Integer32
_StaPppstBacTxlinkdropres_Object = MibScalar
staPppstBacTxlinkdropres = _StaPppstBacTxlinkdropres_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 16),
    _StaPppstBacTxlinkdropres_Type()
)
staPppstBacTxlinkdropres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacTxlinkdropres.setStatus("mandatory")
_StaPppstBacTxstatusindic_Type = Integer32
_StaPppstBacTxstatusindic_Object = MibScalar
staPppstBacTxstatusindic = _StaPppstBacTxstatusindic_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 17),
    _StaPppstBacTxstatusindic_Type()
)
staPppstBacTxstatusindic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacTxstatusindic.setStatus("mandatory")
_StaPppstBacTxstatusreson_Type = Integer32
_StaPppstBacTxstatusreson_Object = MibScalar
staPppstBacTxstatusreson = _StaPppstBacTxstatusreson_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 18),
    _StaPppstBacTxstatusreson_Type()
)
staPppstBacTxstatusreson.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPppstBacTxstatusreson.setStatus("mandatory")
_StaPppstBacDeletevalues_Type = Integer32
_StaPppstBacDeletevalues_Object = MibScalar
staPppstBacDeletevalues = _StaPppstBacDeletevalues_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 12, 19),
    _StaPppstBacDeletevalues_Type()
)
staPppstBacDeletevalues.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staPppstBacDeletevalues.setStatus("mandatory")
_StaPppstDel_Type = Integer32
_StaPppstDel_Object = MibScalar
staPppstDel = _StaPppstDel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 6, 13),
    _StaPppstDel_Type()
)
staPppstDel.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staPppstDel.setStatus("mandatory")
_StaBridg_ObjectIdentity = ObjectIdentity
staBridg = _StaBridg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7)
)
_StaBridgBrglanr_Type = Integer32
_StaBridgBrglanr_Object = MibScalar
staBridgBrglanr = _StaBridgBrglanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 1),
    _StaBridgBrglanr_Type()
)
staBridgBrglanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrglanr.setStatus("mandatory")
_StaBridgBrglant_Type = Integer32
_StaBridgBrglant_Object = MibScalar
staBridgBrglant = _StaBridgBrglant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 2),
    _StaBridgBrglant_Type()
)
staBridgBrglant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrglant.setStatus("mandatory")
_StaBridgBrglanf_Type = Integer32
_StaBridgBrglanf_Object = MibScalar
staBridgBrglanf = _StaBridgBrglanf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 3),
    _StaBridgBrglanf_Type()
)
staBridgBrglanf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrglanf.setStatus("mandatory")
_StaBridgBrglanb_Type = Integer32
_StaBridgBrglanb_Object = MibScalar
staBridgBrglanb = _StaBridgBrglanb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 4),
    _StaBridgBrglanb_Type()
)
staBridgBrglanb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrglanb.setStatus("mandatory")
_StaBridgBrglanm_Type = Integer32
_StaBridgBrglanm_Object = MibScalar
staBridgBrglanm = _StaBridgBrglanm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 5),
    _StaBridgBrglanm_Type()
)
staBridgBrglanm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrglanm.setStatus("mandatory")
_StaBridgBrgwanr_Type = Integer32
_StaBridgBrgwanr_Object = MibScalar
staBridgBrgwanr = _StaBridgBrgwanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 6),
    _StaBridgBrgwanr_Type()
)
staBridgBrgwanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrgwanr.setStatus("mandatory")
_StaBridgBrgwant_Type = Integer32
_StaBridgBrgwant_Object = MibScalar
staBridgBrgwant = _StaBridgBrgwant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 7),
    _StaBridgBrgwant_Type()
)
staBridgBrgwant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrgwant.setStatus("mandatory")
_StaBridgBrgwanf_Type = Integer32
_StaBridgBrgwanf_Object = MibScalar
staBridgBrgwanf = _StaBridgBrgwanf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 8),
    _StaBridgBrgwanf_Type()
)
staBridgBrgwanf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrgwanf.setStatus("mandatory")
_StaBridgBrgwanb_Type = Integer32
_StaBridgBrgwanb_Object = MibScalar
staBridgBrgwanb = _StaBridgBrgwanb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 9),
    _StaBridgBrgwanb_Type()
)
staBridgBrgwanb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrgwanb.setStatus("mandatory")
_StaBridgBrgwanm_Type = Integer32
_StaBridgBrgwanm_Object = MibScalar
staBridgBrgwanm = _StaBridgBrgwanm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 10),
    _StaBridgBrgwanm_Type()
)
staBridgBrgwanm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrgwanm.setStatus("mandatory")
_StaBridgBrgaddr_Type = Integer32
_StaBridgBrgaddr_Object = MibScalar
staBridgBrgaddr = _StaBridgBrgaddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 11),
    _StaBridgBrgaddr_Type()
)
staBridgBrgaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgBrgaddr.setStatus("mandatory")
_StaBridgTablebr_Object = MibTable
staBridgTablebr = _StaBridgTablebr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 12)
)
if mibBuilder.loadTexts:
    staBridgTablebr.setStatus("mandatory")
_StaBridgTablebrCols_Object = MibTableRow
staBridgTablebrCols = _StaBridgTablebrCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 12, 1)
)
staBridgTablebrCols.setIndexNames(
    (0, "ELSA-MIB", "staBridgTablebrNod"),
)
if mibBuilder.loadTexts:
    staBridgTablebrCols.setStatus("mandatory")
_StaBridgTablebrNod_Type = DisplayString
_StaBridgTablebrNod_Object = MibTableColumn
staBridgTablebrNod = _StaBridgTablebrNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 12, 1, 1),
    _StaBridgTablebrNod_Type()
)
staBridgTablebrNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgTablebrNod.setStatus("mandatory")
_StaBridgTablebrLas_Type = Integer32
_StaBridgTablebrLas_Object = MibTableColumn
staBridgTablebrLas = _StaBridgTablebrLas_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 12, 1, 2),
    _StaBridgTablebrLas_Type()
)
staBridgTablebrLas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgTablebrLas.setStatus("mandatory")
_StaBridgTablebrFor_Type = DisplayString
_StaBridgTablebrFor_Object = MibTableColumn
staBridgTablebrFor = _StaBridgTablebrFor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 12, 1, 3),
    _StaBridgTablebrFor_Type()
)
staBridgTablebrFor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgTablebrFor.setStatus("mandatory")
_StaBridgEstabli_Object = MibTable
staBridgEstabli = _StaBridgEstabli_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 13)
)
if mibBuilder.loadTexts:
    staBridgEstabli.setStatus("mandatory")
_StaBridgEstabliCols_Object = MibTableRow
staBridgEstabliCols = _StaBridgEstabliCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 13, 1)
)
staBridgEstabliCols.setIndexNames(
    (0, "ELSA-MIB", "staBridgEstabliTim"),
)
if mibBuilder.loadTexts:
    staBridgEstabliCols.setStatus("mandatory")
_StaBridgEstabliTim_Type = DisplayString
_StaBridgEstabliTim_Object = MibTableColumn
staBridgEstabliTim = _StaBridgEstabliTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 13, 1, 1),
    _StaBridgEstabliTim_Type()
)
staBridgEstabliTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgEstabliTim.setStatus("mandatory")
_StaBridgEstabliDes_Type = DisplayString
_StaBridgEstabliDes_Object = MibTableColumn
staBridgEstabliDes = _StaBridgEstabliDes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 13, 1, 2),
    _StaBridgEstabliDes_Type()
)
staBridgEstabliDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgEstabliDes.setStatus("mandatory")
_StaBridgEstabliSou_Type = DisplayString
_StaBridgEstabliSou_Object = MibTableColumn
staBridgEstabliSou = _StaBridgEstabliSou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 13, 1, 3),
    _StaBridgEstabliSou_Type()
)
staBridgEstabliSou.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBridgEstabliSou.setStatus("mandatory")
_StaBridgDeletev_Type = Integer32
_StaBridgDeletev_Object = MibScalar
staBridgDeletev = _StaBridgDeletev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 7, 14),
    _StaBridgDeletev_Type()
)
staBridgDeletev.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staBridgDeletev.setStatus("mandatory")
_StaIpxst_ObjectIdentity = ObjectIdentity
staIpxst = _StaIpxst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8)
)
_StaIpxstMac_ObjectIdentity = ObjectIdentity
staIpxstMac = _StaIpxstMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1)
)
_StaIpxstMacIpxlanrx_Type = Integer32
_StaIpxstMacIpxlanrx_Object = MibScalar
staIpxstMacIpxlanrx = _StaIpxstMacIpxlanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 1),
    _StaIpxstMacIpxlanrx_Type()
)
staIpxstMacIpxlanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstMacIpxlanrx.setStatus("mandatory")
_StaIpxstMacIpxlanrxb_Type = Integer32
_StaIpxstMacIpxlanrxb_Object = MibScalar
staIpxstMacIpxlanrxb = _StaIpxstMacIpxlanrxb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 2),
    _StaIpxstMacIpxlanrxb_Type()
)
staIpxstMacIpxlanrxb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstMacIpxlanrxb.setStatus("mandatory")
_StaIpxstMacIpxlanrxm_Type = Integer32
_StaIpxstMacIpxlanrxm_Object = MibScalar
staIpxstMacIpxlanrxm = _StaIpxstMacIpxlanrxm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 3),
    _StaIpxstMacIpxlanrxm_Type()
)
staIpxstMacIpxlanrxm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstMacIpxlanrxm.setStatus("mandatory")
_StaIpxstMacIpxlanrxu_Type = Integer32
_StaIpxstMacIpxlanrxu_Object = MibScalar
staIpxstMacIpxlanrxu = _StaIpxstMacIpxlanrxu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 4),
    _StaIpxstMacIpxlanrxu_Type()
)
staIpxstMacIpxlanrxu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstMacIpxlanrxu.setStatus("mandatory")
_StaIpxstMacIpxlantx_Type = Integer32
_StaIpxstMacIpxlantx_Object = MibScalar
staIpxstMacIpxlantx = _StaIpxstMacIpxlantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 5),
    _StaIpxstMacIpxlantx_Type()
)
staIpxstMacIpxlantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstMacIpxlantx.setStatus("mandatory")
_StaIpxstMacIpxwanrx_Type = Integer32
_StaIpxstMacIpxwanrx_Object = MibScalar
staIpxstMacIpxwanrx = _StaIpxstMacIpxwanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 6),
    _StaIpxstMacIpxwanrx_Type()
)
staIpxstMacIpxwanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstMacIpxwanrx.setStatus("mandatory")
_StaIpxstMacIpxwanrxb_Type = Integer32
_StaIpxstMacIpxwanrxb_Object = MibScalar
staIpxstMacIpxwanrxb = _StaIpxstMacIpxwanrxb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 7),
    _StaIpxstMacIpxwanrxb_Type()
)
staIpxstMacIpxwanrxb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstMacIpxwanrxb.setStatus("mandatory")
_StaIpxstMacIpxwanrxm_Type = Integer32
_StaIpxstMacIpxwanrxm_Object = MibScalar
staIpxstMacIpxwanrxm = _StaIpxstMacIpxwanrxm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 8),
    _StaIpxstMacIpxwanrxm_Type()
)
staIpxstMacIpxwanrxm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstMacIpxwanrxm.setStatus("mandatory")
_StaIpxstMacIpxwanrxu_Type = Integer32
_StaIpxstMacIpxwanrxu_Object = MibScalar
staIpxstMacIpxwanrxu = _StaIpxstMacIpxwanrxu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 9),
    _StaIpxstMacIpxwanrxu_Type()
)
staIpxstMacIpxwanrxu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstMacIpxwanrxu.setStatus("mandatory")
_StaIpxstMacIpxwantx_Type = Integer32
_StaIpxstMacIpxwantx_Object = MibScalar
staIpxstMacIpxwantx = _StaIpxstMacIpxwantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 10),
    _StaIpxstMacIpxwantx_Type()
)
staIpxstMacIpxwantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstMacIpxwantx.setStatus("mandatory")
_StaIpxstMacDeleteval_Type = Integer32
_StaIpxstMacDeleteval_Object = MibScalar
staIpxstMacDeleteval = _StaIpxstMacDeleteval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 1, 11),
    _StaIpxstMacDeleteval_Type()
)
staIpxstMacDeleteval.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staIpxstMacDeleteval.setStatus("mandatory")
_StaIpxstWat_ObjectIdentity = ObjectIdentity
staIpxstWat = _StaIpxstWat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 2)
)
_StaIpxstWatIpxwatchdoglanr_Type = Integer32
_StaIpxstWatIpxwatchdoglanr_Object = MibScalar
staIpxstWatIpxwatchdoglanr = _StaIpxstWatIpxwatchdoglanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 2, 1),
    _StaIpxstWatIpxwatchdoglanr_Type()
)
staIpxstWatIpxwatchdoglanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstWatIpxwatchdoglanr.setStatus("mandatory")
_StaIpxstWatIpxwatchdoglant_Type = Integer32
_StaIpxstWatIpxwatchdoglant_Object = MibScalar
staIpxstWatIpxwatchdoglant = _StaIpxstWatIpxwatchdoglant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 2, 2),
    _StaIpxstWatIpxwatchdoglant_Type()
)
staIpxstWatIpxwatchdoglant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstWatIpxwatchdoglant.setStatus("mandatory")
_StaIpxstWatIpxwatchdogwanr_Type = Integer32
_StaIpxstWatIpxwatchdogwanr_Object = MibScalar
staIpxstWatIpxwatchdogwanr = _StaIpxstWatIpxwatchdogwanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 2, 3),
    _StaIpxstWatIpxwatchdogwanr_Type()
)
staIpxstWatIpxwatchdogwanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstWatIpxwatchdogwanr.setStatus("mandatory")
_StaIpxstWatIpxwatchdogwant_Type = Integer32
_StaIpxstWatIpxwatchdogwant_Object = MibScalar
staIpxstWatIpxwatchdogwant = _StaIpxstWatIpxwatchdogwant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 2, 4),
    _StaIpxstWatIpxwatchdogwant_Type()
)
staIpxstWatIpxwatchdogwant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstWatIpxwatchdogwant.setStatus("mandatory")
_StaIpxstWatSpxwatchdoglanr_Type = Integer32
_StaIpxstWatSpxwatchdoglanr_Object = MibScalar
staIpxstWatSpxwatchdoglanr = _StaIpxstWatSpxwatchdoglanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 2, 5),
    _StaIpxstWatSpxwatchdoglanr_Type()
)
staIpxstWatSpxwatchdoglanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstWatSpxwatchdoglanr.setStatus("mandatory")
_StaIpxstWatSpxwatchdoglant_Type = Integer32
_StaIpxstWatSpxwatchdoglant_Object = MibScalar
staIpxstWatSpxwatchdoglant = _StaIpxstWatSpxwatchdoglant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 2, 6),
    _StaIpxstWatSpxwatchdoglant_Type()
)
staIpxstWatSpxwatchdoglant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstWatSpxwatchdoglant.setStatus("mandatory")
_StaIpxstWatSpxwatchdogwanr_Type = Integer32
_StaIpxstWatSpxwatchdogwanr_Object = MibScalar
staIpxstWatSpxwatchdogwanr = _StaIpxstWatSpxwatchdogwanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 2, 7),
    _StaIpxstWatSpxwatchdogwanr_Type()
)
staIpxstWatSpxwatchdogwanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstWatSpxwatchdogwanr.setStatus("mandatory")
_StaIpxstWatSpxwatchdogwant_Type = Integer32
_StaIpxstWatSpxwatchdogwant_Object = MibScalar
staIpxstWatSpxwatchdogwant = _StaIpxstWatSpxwatchdogwant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 2, 8),
    _StaIpxstWatSpxwatchdogwant_Type()
)
staIpxstWatSpxwatchdogwant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstWatSpxwatchdogwant.setStatus("mandatory")
_StaIpxstWatDeletevalues_Type = Integer32
_StaIpxstWatDeletevalues_Object = MibScalar
staIpxstWatDeletevalues = _StaIpxstWatDeletevalues_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 2, 9),
    _StaIpxstWatDeletevalues_Type()
)
staIpxstWatDeletevalues.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staIpxstWatDeletevalues.setStatus("mandatory")
_StaIpxstPro_ObjectIdentity = ObjectIdentity
staIpxstPro = _StaIpxstPro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3)
)
_StaIpxstProPropagatelanr_Type = Integer32
_StaIpxstProPropagatelanr_Object = MibScalar
staIpxstProPropagatelanr = _StaIpxstProPropagatelanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 1),
    _StaIpxstProPropagatelanr_Type()
)
staIpxstProPropagatelanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatelanr.setStatus("mandatory")
_StaIpxstProPropagatelanf_Type = Integer32
_StaIpxstProPropagatelanf_Object = MibScalar
staIpxstProPropagatelanf = _StaIpxstProPropagatelanf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 2),
    _StaIpxstProPropagatelanf_Type()
)
staIpxstProPropagatelanf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatelanf.setStatus("mandatory")
_StaIpxstProPropagatelant_Type = Integer32
_StaIpxstProPropagatelant_Object = MibScalar
staIpxstProPropagatelant = _StaIpxstProPropagatelant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 3),
    _StaIpxstProPropagatelant_Type()
)
staIpxstProPropagatelant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatelant.setStatus("mandatory")
_StaIpxstProPropagatelans_Type = Integer32
_StaIpxstProPropagatelans_Object = MibScalar
staIpxstProPropagatelans = _StaIpxstProPropagatelans_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 4),
    _StaIpxstProPropagatelans_Type()
)
staIpxstProPropagatelans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatelans.setStatus("mandatory")
_StaIpxstProPropagatelanh_Type = Integer32
_StaIpxstProPropagatelanh_Object = MibScalar
staIpxstProPropagatelanh = _StaIpxstProPropagatelanh_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 5),
    _StaIpxstProPropagatelanh_Type()
)
staIpxstProPropagatelanh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatelanh.setStatus("mandatory")
_StaIpxstProPropagatelanb_Type = Integer32
_StaIpxstProPropagatelanb_Object = MibScalar
staIpxstProPropagatelanb = _StaIpxstProPropagatelanb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 6),
    _StaIpxstProPropagatelanb_Type()
)
staIpxstProPropagatelanb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatelanb.setStatus("mandatory")
_StaIpxstProPropagatelanc_Type = Integer32
_StaIpxstProPropagatelanc_Object = MibScalar
staIpxstProPropagatelanc = _StaIpxstProPropagatelanc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 7),
    _StaIpxstProPropagatelanc_Type()
)
staIpxstProPropagatelanc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatelanc.setStatus("mandatory")
_StaIpxstProPropagatewanr_Type = Integer32
_StaIpxstProPropagatewanr_Object = MibScalar
staIpxstProPropagatewanr = _StaIpxstProPropagatewanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 8),
    _StaIpxstProPropagatewanr_Type()
)
staIpxstProPropagatewanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatewanr.setStatus("mandatory")
_StaIpxstProPropagatewanf_Type = Integer32
_StaIpxstProPropagatewanf_Object = MibScalar
staIpxstProPropagatewanf = _StaIpxstProPropagatewanf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 9),
    _StaIpxstProPropagatewanf_Type()
)
staIpxstProPropagatewanf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatewanf.setStatus("mandatory")
_StaIpxstProPropagatewant_Type = Integer32
_StaIpxstProPropagatewant_Object = MibScalar
staIpxstProPropagatewant = _StaIpxstProPropagatewant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 10),
    _StaIpxstProPropagatewant_Type()
)
staIpxstProPropagatewant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatewant.setStatus("mandatory")
_StaIpxstProPropagatewans_Type = Integer32
_StaIpxstProPropagatewans_Object = MibScalar
staIpxstProPropagatewans = _StaIpxstProPropagatewans_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 11),
    _StaIpxstProPropagatewans_Type()
)
staIpxstProPropagatewans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstProPropagatewans.setStatus("mandatory")
_StaIpxstProDeletevalues_Type = Integer32
_StaIpxstProDeletevalues_Object = MibScalar
staIpxstProDeletevalues = _StaIpxstProDeletevalues_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 3, 12),
    _StaIpxstProDeletevalues_Type()
)
staIpxstProDeletevalues.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staIpxstProDeletevalues.setStatus("mandatory")
_StaIpxstRip_ObjectIdentity = ObjectIdentity
staIpxstRip = _StaIpxstRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4)
)
_StaIpxstRipRiplanr_Type = Integer32
_StaIpxstRipRiplanr_Object = MibScalar
staIpxstRipRiplanr = _StaIpxstRipRiplanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 1),
    _StaIpxstRipRiplanr_Type()
)
staIpxstRipRiplanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipRiplanr.setStatus("mandatory")
_StaIpxstRipRiplane_Type = Integer32
_StaIpxstRipRiplane_Object = MibScalar
staIpxstRipRiplane = _StaIpxstRipRiplane_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 2),
    _StaIpxstRipRiplane_Type()
)
staIpxstRipRiplane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipRiplane.setStatus("mandatory")
_StaIpxstRipRiplant_Type = Integer32
_StaIpxstRipRiplant_Object = MibScalar
staIpxstRipRiplant = _StaIpxstRipRiplant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 3),
    _StaIpxstRipRiplant_Type()
)
staIpxstRipRiplant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipRiplant.setStatus("mandatory")
_StaIpxstRipRipwanr_Type = Integer32
_StaIpxstRipRipwanr_Object = MibScalar
staIpxstRipRipwanr = _StaIpxstRipRipwanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 4),
    _StaIpxstRipRipwanr_Type()
)
staIpxstRipRipwanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipRipwanr.setStatus("mandatory")
_StaIpxstRipRipwane_Type = Integer32
_StaIpxstRipRipwane_Object = MibScalar
staIpxstRipRipwane = _StaIpxstRipRipwane_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 5),
    _StaIpxstRipRipwane_Type()
)
staIpxstRipRipwane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipRipwane.setStatus("mandatory")
_StaIpxstRipRipwant_Type = Integer32
_StaIpxstRipRipwant_Object = MibScalar
staIpxstRipRipwant = _StaIpxstRipRipwant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 6),
    _StaIpxstRipRipwant_Type()
)
staIpxstRipRipwant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipRipwant.setStatus("mandatory")
_StaIpxstRipTableri_Object = MibTable
staIpxstRipTableri = _StaIpxstRipTableri_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 7)
)
if mibBuilder.loadTexts:
    staIpxstRipTableri.setStatus("mandatory")
_StaIpxstRipTableriCols_Object = MibTableRow
staIpxstRipTableriCols = _StaIpxstRipTableriCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 7, 1)
)
staIpxstRipTableriCols.setIndexNames(
    (0, "ELSA-MIB", "staIpxstRipTableriNet"),
)
if mibBuilder.loadTexts:
    staIpxstRipTableriCols.setStatus("mandatory")
_StaIpxstRipTableriNet_Type = DisplayString
_StaIpxstRipTableriNet_Object = MibTableColumn
staIpxstRipTableriNet = _StaIpxstRipTableriNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 7, 1, 1),
    _StaIpxstRipTableriNet_Type()
)
staIpxstRipTableriNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipTableriNet.setStatus("mandatory")
_StaIpxstRipTableriHop_Type = Integer32
_StaIpxstRipTableriHop_Object = MibTableColumn
staIpxstRipTableriHop = _StaIpxstRipTableriHop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 7, 1, 2),
    _StaIpxstRipTableriHop_Type()
)
staIpxstRipTableriHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipTableriHop.setStatus("mandatory")
_StaIpxstRipTableriTic_Type = Integer32
_StaIpxstRipTableriTic_Object = MibTableColumn
staIpxstRipTableriTic = _StaIpxstRipTableriTic_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 7, 1, 3),
    _StaIpxstRipTableriTic_Type()
)
staIpxstRipTableriTic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipTableriTic.setStatus("mandatory")
_StaIpxstRipTableriNod_Type = DisplayString
_StaIpxstRipTableriNod_Object = MibTableColumn
staIpxstRipTableriNod = _StaIpxstRipTableriNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 7, 1, 4),
    _StaIpxstRipTableriNod_Type()
)
staIpxstRipTableriNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipTableriNod.setStatus("mandatory")
_StaIpxstRipTableriTim_Type = Integer32
_StaIpxstRipTableriTim_Object = MibTableColumn
staIpxstRipTableriTim = _StaIpxstRipTableriTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 7, 1, 5),
    _StaIpxstRipTableriTim_Type()
)
staIpxstRipTableriTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipTableriTim.setStatus("mandatory")


class _StaIpxstRipTableriFla_Type(Integer32):
    """Custom type staIpxstRipTableriFla based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("direct", 128),
          ("down", 32),
          ("local", 2),
          ("loop", 16),
          ("new", 64),
          ("remote", 1),
          ("spare", 8))
    )


_StaIpxstRipTableriFla_Type.__name__ = "Integer32"
_StaIpxstRipTableriFla_Object = MibTableColumn
staIpxstRipTableriFla = _StaIpxstRipTableriFla_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 7, 1, 6),
    _StaIpxstRipTableriFla_Type()
)
staIpxstRipTableriFla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstRipTableriFla.setStatus("mandatory")
_StaIpxstRipDeletev_Type = Integer32
_StaIpxstRipDeletev_Object = MibScalar
staIpxstRipDeletev = _StaIpxstRipDeletev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 4, 8),
    _StaIpxstRipDeletev_Type()
)
staIpxstRipDeletev.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staIpxstRipDeletev.setStatus("mandatory")
_StaIpxstSap_ObjectIdentity = ObjectIdentity
staIpxstSap = _StaIpxstSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5)
)
_StaIpxstSapSaplanr_Type = Integer32
_StaIpxstSapSaplanr_Object = MibScalar
staIpxstSapSaplanr = _StaIpxstSapSaplanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 1),
    _StaIpxstSapSaplanr_Type()
)
staIpxstSapSaplanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapSaplanr.setStatus("mandatory")
_StaIpxstSapSaplane_Type = Integer32
_StaIpxstSapSaplane_Object = MibScalar
staIpxstSapSaplane = _StaIpxstSapSaplane_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 2),
    _StaIpxstSapSaplane_Type()
)
staIpxstSapSaplane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapSaplane.setStatus("mandatory")
_StaIpxstSapSaplant_Type = Integer32
_StaIpxstSapSaplant_Object = MibScalar
staIpxstSapSaplant = _StaIpxstSapSaplant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 3),
    _StaIpxstSapSaplant_Type()
)
staIpxstSapSaplant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapSaplant.setStatus("mandatory")
_StaIpxstSapSapwanr_Type = Integer32
_StaIpxstSapSapwanr_Object = MibScalar
staIpxstSapSapwanr = _StaIpxstSapSapwanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 4),
    _StaIpxstSapSapwanr_Type()
)
staIpxstSapSapwanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapSapwanr.setStatus("mandatory")
_StaIpxstSapSapwane_Type = Integer32
_StaIpxstSapSapwane_Object = MibScalar
staIpxstSapSapwane = _StaIpxstSapSapwane_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 5),
    _StaIpxstSapSapwane_Type()
)
staIpxstSapSapwane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapSapwane.setStatus("mandatory")
_StaIpxstSapSapwant_Type = Integer32
_StaIpxstSapSapwant_Object = MibScalar
staIpxstSapSapwant = _StaIpxstSapSapwant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 6),
    _StaIpxstSapSapwant_Type()
)
staIpxstSapSapwant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapSapwant.setStatus("mandatory")
_StaIpxstSapTablesa_Object = MibTable
staIpxstSapTablesa = _StaIpxstSapTablesa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 7)
)
if mibBuilder.loadTexts:
    staIpxstSapTablesa.setStatus("mandatory")
_StaIpxstSapTablesaCols_Object = MibTableRow
staIpxstSapTablesaCols = _StaIpxstSapTablesaCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 7, 1)
)
staIpxstSapTablesaCols.setIndexNames(
    (0, "ELSA-MIB", "staIpxstSapTablesaTyp"),
)
if mibBuilder.loadTexts:
    staIpxstSapTablesaCols.setStatus("mandatory")
_StaIpxstSapTablesaTyp_Type = DisplayString
_StaIpxstSapTablesaTyp_Object = MibTableColumn
staIpxstSapTablesaTyp = _StaIpxstSapTablesaTyp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 7, 1, 1),
    _StaIpxstSapTablesaTyp_Type()
)
staIpxstSapTablesaTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapTablesaTyp.setStatus("mandatory")
_StaIpxstSapTablesaSer_Type = DisplayString
_StaIpxstSapTablesaSer_Object = MibTableColumn
staIpxstSapTablesaSer = _StaIpxstSapTablesaSer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 7, 1, 2),
    _StaIpxstSapTablesaSer_Type()
)
staIpxstSapTablesaSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapTablesaSer.setStatus("mandatory")
_StaIpxstSapTablesaNet_Type = DisplayString
_StaIpxstSapTablesaNet_Object = MibTableColumn
staIpxstSapTablesaNet = _StaIpxstSapTablesaNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 7, 1, 3),
    _StaIpxstSapTablesaNet_Type()
)
staIpxstSapTablesaNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapTablesaNet.setStatus("mandatory")
_StaIpxstSapTablesaNod_Type = DisplayString
_StaIpxstSapTablesaNod_Object = MibTableColumn
staIpxstSapTablesaNod = _StaIpxstSapTablesaNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 7, 1, 4),
    _StaIpxstSapTablesaNod_Type()
)
staIpxstSapTablesaNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapTablesaNod.setStatus("mandatory")
_StaIpxstSapTablesaSoc_Type = DisplayString
_StaIpxstSapTablesaSoc_Object = MibTableColumn
staIpxstSapTablesaSoc = _StaIpxstSapTablesaSoc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 7, 1, 5),
    _StaIpxstSapTablesaSoc_Type()
)
staIpxstSapTablesaSoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapTablesaSoc.setStatus("mandatory")
_StaIpxstSapTablesaHop_Type = Integer32
_StaIpxstSapTablesaHop_Object = MibTableColumn
staIpxstSapTablesaHop = _StaIpxstSapTablesaHop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 7, 1, 6),
    _StaIpxstSapTablesaHop_Type()
)
staIpxstSapTablesaHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapTablesaHop.setStatus("mandatory")
_StaIpxstSapTablesaTim_Type = Integer32
_StaIpxstSapTablesaTim_Object = MibTableColumn
staIpxstSapTablesaTim = _StaIpxstSapTablesaTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 7, 1, 7),
    _StaIpxstSapTablesaTim_Type()
)
staIpxstSapTablesaTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapTablesaTim.setStatus("mandatory")


class _StaIpxstSapTablesaFla_Type(Integer32):
    """Custom type staIpxstSapTablesaFla based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("direct", 128),
          ("down", 32),
          ("local", 2),
          ("loop", 16),
          ("new", 64),
          ("remote", 1),
          ("spare", 8))
    )


_StaIpxstSapTablesaFla_Type.__name__ = "Integer32"
_StaIpxstSapTablesaFla_Object = MibTableColumn
staIpxstSapTablesaFla = _StaIpxstSapTablesaFla_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 7, 1, 8),
    _StaIpxstSapTablesaFla_Type()
)
staIpxstSapTablesaFla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstSapTablesaFla.setStatus("mandatory")
_StaIpxstSapDeletev_Type = Integer32
_StaIpxstSapDeletev_Object = MibScalar
staIpxstSapDeletev = _StaIpxstSapDeletev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 5, 8),
    _StaIpxstSapDeletev_Type()
)
staIpxstSapDeletev.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staIpxstSapDeletev.setStatus("mandatory")
_StaIpxstIpx_ObjectIdentity = ObjectIdentity
staIpxstIpx = _StaIpxstIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6)
)
_StaIpxstIpxIpxrlanr_Type = Integer32
_StaIpxstIpxIpxrlanr_Object = MibScalar
staIpxstIpxIpxrlanr = _StaIpxstIpxIpxrlanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 1),
    _StaIpxstIpxIpxrlanr_Type()
)
staIpxstIpxIpxrlanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrlanr.setStatus("mandatory")
_StaIpxstIpxIpxrlant_Type = Integer32
_StaIpxstIpxIpxrlant_Object = MibScalar
staIpxstIpxIpxrlant = _StaIpxstIpxIpxrlant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 2),
    _StaIpxstIpxIpxrlant_Type()
)
staIpxstIpxIpxrlant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrlant.setStatus("mandatory")
_StaIpxstIpxIpxrlanh_Type = Integer32
_StaIpxstIpxIpxrlanh_Object = MibScalar
staIpxstIpxIpxrlanh = _StaIpxstIpxIpxrlanh_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 3),
    _StaIpxstIpxIpxrlanh_Type()
)
staIpxstIpxIpxrlanh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrlanh.setStatus("mandatory")
_StaIpxstIpxIpxrlans_Type = Integer32
_StaIpxstIpxIpxrlans_Object = MibScalar
staIpxstIpxIpxrlans = _StaIpxstIpxIpxrlans_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 4),
    _StaIpxstIpxIpxrlans_Type()
)
staIpxstIpxIpxrlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrlans.setStatus("mandatory")
_StaIpxstIpxIpxrlann_Type = Integer32
_StaIpxstIpxIpxrlann_Object = MibScalar
staIpxstIpxIpxrlann = _StaIpxstIpxIpxrlann_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 5),
    _StaIpxstIpxIpxrlann_Type()
)
staIpxstIpxIpxrlann.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrlann.setStatus("mandatory")
_StaIpxstIpxIpxrlanb_Type = Integer32
_StaIpxstIpxIpxrlanb_Object = MibScalar
staIpxstIpxIpxrlanb = _StaIpxstIpxIpxrlanb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 6),
    _StaIpxstIpxIpxrlanb_Type()
)
staIpxstIpxIpxrlanb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrlanb.setStatus("mandatory")
_StaIpxstIpxIpxrlanc_Type = Integer32
_StaIpxstIpxIpxrlanc_Object = MibScalar
staIpxstIpxIpxrlanc = _StaIpxstIpxIpxrlanc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 7),
    _StaIpxstIpxIpxrlanc_Type()
)
staIpxstIpxIpxrlanc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrlanc.setStatus("mandatory")
_StaIpxstIpxIpxrland_Type = Integer32
_StaIpxstIpxIpxrland_Object = MibScalar
staIpxstIpxIpxrland = _StaIpxstIpxIpxrland_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 8),
    _StaIpxstIpxIpxrland_Type()
)
staIpxstIpxIpxrland.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrland.setStatus("mandatory")
_StaIpxstIpxIpxrwanr_Type = Integer32
_StaIpxstIpxIpxrwanr_Object = MibScalar
staIpxstIpxIpxrwanr = _StaIpxstIpxIpxrwanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 9),
    _StaIpxstIpxIpxrwanr_Type()
)
staIpxstIpxIpxrwanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrwanr.setStatus("mandatory")
_StaIpxstIpxIpxrwant_Type = Integer32
_StaIpxstIpxIpxrwant_Object = MibScalar
staIpxstIpxIpxrwant = _StaIpxstIpxIpxrwant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 10),
    _StaIpxstIpxIpxrwant_Type()
)
staIpxstIpxIpxrwant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrwant.setStatus("mandatory")
_StaIpxstIpxIpxrwanh_Type = Integer32
_StaIpxstIpxIpxrwanh_Object = MibScalar
staIpxstIpxIpxrwanh = _StaIpxstIpxIpxrwanh_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 11),
    _StaIpxstIpxIpxrwanh_Type()
)
staIpxstIpxIpxrwanh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrwanh.setStatus("mandatory")
_StaIpxstIpxIpxrwans_Type = Integer32
_StaIpxstIpxIpxrwans_Object = MibScalar
staIpxstIpxIpxrwans = _StaIpxstIpxIpxrwans_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 12),
    _StaIpxstIpxIpxrwans_Type()
)
staIpxstIpxIpxrwans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrwans.setStatus("mandatory")
_StaIpxstIpxIpxrwann_Type = Integer32
_StaIpxstIpxIpxrwann_Object = MibScalar
staIpxstIpxIpxrwann = _StaIpxstIpxIpxrwann_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 13),
    _StaIpxstIpxIpxrwann_Type()
)
staIpxstIpxIpxrwann.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrwann.setStatus("mandatory")
_StaIpxstIpxIpxrwanb_Type = Integer32
_StaIpxstIpxIpxrwanb_Object = MibScalar
staIpxstIpxIpxrwanb = _StaIpxstIpxIpxrwanb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 14),
    _StaIpxstIpxIpxrwanb_Type()
)
staIpxstIpxIpxrwanb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrwanb.setStatus("mandatory")
_StaIpxstIpxIpxrwand_Type = Integer32
_StaIpxstIpxIpxrwand_Object = MibScalar
staIpxstIpxIpxrwand = _StaIpxstIpxIpxrwand_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 15),
    _StaIpxstIpxIpxrwand_Type()
)
staIpxstIpxIpxrwand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrwand.setStatus("mandatory")
_StaIpxstIpxIpxrinte_Type = Integer32
_StaIpxstIpxIpxrinte_Object = MibScalar
staIpxstIpxIpxrinte = _StaIpxstIpxIpxrinte_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 16),
    _StaIpxstIpxIpxrinte_Type()
)
staIpxstIpxIpxrinte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxIpxrinte.setStatus("mandatory")
_StaIpxstIpxNetworks_Object = MibTable
staIpxstIpxNetworks = _StaIpxstIpxNetworks_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 17)
)
if mibBuilder.loadTexts:
    staIpxstIpxNetworks.setStatus("mandatory")
_StaIpxstIpxNetworksCols_Object = MibTableRow
staIpxstIpxNetworksCols = _StaIpxstIpxNetworksCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 17, 1)
)
staIpxstIpxNetworksCols.setIndexNames(
    (0, "ELSA-MIB", "staIpxstIpxNetworksRem"),
)
if mibBuilder.loadTexts:
    staIpxstIpxNetworksCols.setStatus("mandatory")
_StaIpxstIpxNetworksRem_Type = DisplayString
_StaIpxstIpxNetworksRem_Object = MibTableColumn
staIpxstIpxNetworksRem = _StaIpxstIpxNetworksRem_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 17, 1, 1),
    _StaIpxstIpxNetworksRem_Type()
)
staIpxstIpxNetworksRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxNetworksRem.setStatus("mandatory")
_StaIpxstIpxNetworksNet_Type = DisplayString
_StaIpxstIpxNetworksNet_Object = MibTableColumn
staIpxstIpxNetworksNet = _StaIpxstIpxNetworksNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 17, 1, 2),
    _StaIpxstIpxNetworksNet_Type()
)
staIpxstIpxNetworksNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxNetworksNet.setStatus("mandatory")


class _StaIpxstIpxNetworksBin_Type(Integer32):
    """Custom type staIpxstIpxNetworksBin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("dot802-2", 4),
          ("dot802-3", 2),
          ("ii", 1),
          ("snap", 8))
    )


_StaIpxstIpxNetworksBin_Type.__name__ = "Integer32"
_StaIpxstIpxNetworksBin_Object = MibTableColumn
staIpxstIpxNetworksBin = _StaIpxstIpxNetworksBin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 17, 1, 3),
    _StaIpxstIpxNetworksBin_Type()
)
staIpxstIpxNetworksBin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxNetworksBin.setStatus("mandatory")


class _StaIpxstIpxNetworksPro_Type(Integer32):
    """Custom type staIpxstIpxNetworksPro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("route", 3))
    )


_StaIpxstIpxNetworksPro_Type.__name__ = "Integer32"
_StaIpxstIpxNetworksPro_Object = MibTableColumn
staIpxstIpxNetworksPro = _StaIpxstIpxNetworksPro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 17, 1, 4),
    _StaIpxstIpxNetworksPro_Type()
)
staIpxstIpxNetworksPro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxNetworksPro.setStatus("mandatory")
_StaIpxstIpxNetworksBac_Type = Integer32
_StaIpxstIpxNetworksBac_Object = MibTableColumn
staIpxstIpxNetworksBac = _StaIpxstIpxNetworksBac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 17, 1, 5),
    _StaIpxstIpxNetworksBac_Type()
)
staIpxstIpxNetworksBac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxNetworksBac.setStatus("mandatory")
_StaIpxstIpxNetworksTim_Type = Integer32
_StaIpxstIpxNetworksTim_Object = MibTableColumn
staIpxstIpxNetworksTim = _StaIpxstIpxNetworksTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 17, 1, 6),
    _StaIpxstIpxNetworksTim_Type()
)
staIpxstIpxNetworksTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxNetworksTim.setStatus("mandatory")
_StaIpxstIpxNetworksNod_Type = DisplayString
_StaIpxstIpxNetworksNod_Object = MibTableColumn
staIpxstIpxNetworksNod = _StaIpxstIpxNetworksNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 17, 1, 7),
    _StaIpxstIpxNetworksNod_Type()
)
staIpxstIpxNetworksNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxNetworksNod.setStatus("mandatory")
_StaIpxstIpxEstablis_Object = MibTable
staIpxstIpxEstablis = _StaIpxstIpxEstablis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 18)
)
if mibBuilder.loadTexts:
    staIpxstIpxEstablis.setStatus("mandatory")
_StaIpxstIpxEstablisCols_Object = MibTableRow
staIpxstIpxEstablisCols = _StaIpxstIpxEstablisCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 18, 1)
)
staIpxstIpxEstablisCols.setIndexNames(
    (0, "ELSA-MIB", "staIpxstIpxEstablisTime"),
)
if mibBuilder.loadTexts:
    staIpxstIpxEstablisCols.setStatus("mandatory")
_StaIpxstIpxEstablisTime_Type = DisplayString
_StaIpxstIpxEstablisTime_Object = MibTableColumn
staIpxstIpxEstablisTime = _StaIpxstIpxEstablisTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 18, 1, 1),
    _StaIpxstIpxEstablisTime_Type()
)
staIpxstIpxEstablisTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxEstablisTime.setStatus("mandatory")
_StaIpxstIpxEstablisDestnet_Type = DisplayString
_StaIpxstIpxEstablisDestnet_Object = MibTableColumn
staIpxstIpxEstablisDestnet = _StaIpxstIpxEstablisDestnet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 18, 1, 2),
    _StaIpxstIpxEstablisDestnet_Type()
)
staIpxstIpxEstablisDestnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxEstablisDestnet.setStatus("mandatory")
_StaIpxstIpxEstablisDestnode_Type = DisplayString
_StaIpxstIpxEstablisDestnode_Object = MibTableColumn
staIpxstIpxEstablisDestnode = _StaIpxstIpxEstablisDestnode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 18, 1, 3),
    _StaIpxstIpxEstablisDestnode_Type()
)
staIpxstIpxEstablisDestnode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxEstablisDestnode.setStatus("mandatory")
_StaIpxstIpxEstablisDestsock_Type = DisplayString
_StaIpxstIpxEstablisDestsock_Object = MibTableColumn
staIpxstIpxEstablisDestsock = _StaIpxstIpxEstablisDestsock_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 18, 1, 4),
    _StaIpxstIpxEstablisDestsock_Type()
)
staIpxstIpxEstablisDestsock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxEstablisDestsock.setStatus("mandatory")
_StaIpxstIpxEstablisSourcene_Type = DisplayString
_StaIpxstIpxEstablisSourcene_Object = MibTableColumn
staIpxstIpxEstablisSourcene = _StaIpxstIpxEstablisSourcene_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 18, 1, 5),
    _StaIpxstIpxEstablisSourcene_Type()
)
staIpxstIpxEstablisSourcene.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxEstablisSourcene.setStatus("mandatory")
_StaIpxstIpxEstablisSourceno_Type = DisplayString
_StaIpxstIpxEstablisSourceno_Object = MibTableColumn
staIpxstIpxEstablisSourceno = _StaIpxstIpxEstablisSourceno_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 18, 1, 6),
    _StaIpxstIpxEstablisSourceno_Type()
)
staIpxstIpxEstablisSourceno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxEstablisSourceno.setStatus("mandatory")
_StaIpxstIpxEstablisSourceso_Type = DisplayString
_StaIpxstIpxEstablisSourceso_Object = MibTableColumn
staIpxstIpxEstablisSourceso = _StaIpxstIpxEstablisSourceso_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 18, 1, 7),
    _StaIpxstIpxEstablisSourceso_Type()
)
staIpxstIpxEstablisSourceso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIpxstIpxEstablisSourceso.setStatus("mandatory")
_StaIpxstIpxDeleteva_Type = Integer32
_StaIpxstIpxDeleteva_Object = MibScalar
staIpxstIpxDeleteva = _StaIpxstIpxDeleteva_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 6, 19),
    _StaIpxstIpxDeleteva_Type()
)
staIpxstIpxDeleteva.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staIpxstIpxDeleteva.setStatus("mandatory")
_StaIpxstDel_Type = Integer32
_StaIpxstDel_Object = MibScalar
staIpxstDel = _StaIpxstDel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 8, 7),
    _StaIpxstDel_Type()
)
staIpxstDel.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staIpxstDel.setStatus("mandatory")
_StaTcpip_ObjectIdentity = ObjectIdentity
staTcpip = _StaTcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9)
)
_StaTcpipArp_ObjectIdentity = ObjectIdentity
staTcpipArp = _StaTcpipArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1)
)
_StaTcpipArpArplanr_Type = Integer32
_StaTcpipArpArplanr_Object = MibScalar
staTcpipArpArplanr = _StaTcpipArpArplanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 1),
    _StaTcpipArpArplanr_Type()
)
staTcpipArpArplanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipArpArplanr.setStatus("mandatory")
_StaTcpipArpArplant_Type = Integer32
_StaTcpipArpArplant_Object = MibScalar
staTcpipArpArplant = _StaTcpipArpArplant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 2),
    _StaTcpipArpArplant_Type()
)
staTcpipArpArplant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipArpArplant.setStatus("mandatory")
_StaTcpipArpArplane_Type = Integer32
_StaTcpipArpArplane_Object = MibScalar
staTcpipArpArplane = _StaTcpipArpArplane_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 3),
    _StaTcpipArpArplane_Type()
)
staTcpipArpArplane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipArpArplane.setStatus("mandatory")
_StaTcpipArpArpwanr_Type = Integer32
_StaTcpipArpArpwanr_Object = MibScalar
staTcpipArpArpwanr = _StaTcpipArpArpwanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 4),
    _StaTcpipArpArpwanr_Type()
)
staTcpipArpArpwanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipArpArpwanr.setStatus("mandatory")
_StaTcpipArpArpwant_Type = Integer32
_StaTcpipArpArpwant_Object = MibScalar
staTcpipArpArpwant = _StaTcpipArpArpwant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 5),
    _StaTcpipArpArpwant_Type()
)
staTcpipArpArpwant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipArpArpwant.setStatus("mandatory")
_StaTcpipArpArpwane_Type = Integer32
_StaTcpipArpArpwane_Object = MibScalar
staTcpipArpArpwane = _StaTcpipArpArpwane_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 6),
    _StaTcpipArpArpwane_Type()
)
staTcpipArpArpwane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipArpArpwane.setStatus("mandatory")
_StaTcpipArpTablear_Object = MibTable
staTcpipArpTablear = _StaTcpipArpTablear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 7)
)
if mibBuilder.loadTexts:
    staTcpipArpTablear.setStatus("mandatory")
_StaTcpipArpTablearCols_Object = MibTableRow
staTcpipArpTablearCols = _StaTcpipArpTablearCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 7, 1)
)
staTcpipArpTablearCols.setIndexNames(
    (0, "ELSA-MIB", "staTcpipArpTablearIpa"),
)
if mibBuilder.loadTexts:
    staTcpipArpTablearCols.setStatus("mandatory")
_StaTcpipArpTablearIpa_Type = IpAddress
_StaTcpipArpTablearIpa_Object = MibTableColumn
staTcpipArpTablearIpa = _StaTcpipArpTablearIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 7, 1, 1),
    _StaTcpipArpTablearIpa_Type()
)
staTcpipArpTablearIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipArpTablearIpa.setStatus("mandatory")
_StaTcpipArpTablearNod_Type = DisplayString
_StaTcpipArpTablearNod_Object = MibTableColumn
staTcpipArpTablearNod = _StaTcpipArpTablearNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 7, 1, 2),
    _StaTcpipArpTablearNod_Type()
)
staTcpipArpTablearNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipArpTablearNod.setStatus("mandatory")
_StaTcpipArpTablearLas_Type = Integer32
_StaTcpipArpTablearLas_Object = MibTableColumn
staTcpipArpTablearLas = _StaTcpipArpTablearLas_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 7, 1, 3),
    _StaTcpipArpTablearLas_Type()
)
staTcpipArpTablearLas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipArpTablearLas.setStatus("mandatory")


class _StaTcpipArpTablearCon_Type(Integer32):
    """Custom type staTcpipArpTablearCon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("remote", 1))
    )


_StaTcpipArpTablearCon_Type.__name__ = "Integer32"
_StaTcpipArpTablearCon_Object = MibTableColumn
staTcpipArpTablearCon = _StaTcpipArpTablearCon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 7, 1, 4),
    _StaTcpipArpTablearCon_Type()
)
staTcpipArpTablearCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipArpTablearCon.setStatus("mandatory")
_StaTcpipArpDeletev_Type = Integer32
_StaTcpipArpDeletev_Object = MibScalar
staTcpipArpDeletev = _StaTcpipArpDeletev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 1, 8),
    _StaTcpipArpDeletev_Type()
)
staTcpipArpDeletev.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staTcpipArpDeletev.setStatus("mandatory")
_StaTcpipIps_ObjectIdentity = ObjectIdentity
staTcpipIps = _StaTcpipIps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2)
)
_StaTcpipIpsIplanrx_Type = Integer32
_StaTcpipIpsIplanrx_Object = MibScalar
staTcpipIpsIplanrx = _StaTcpipIpsIplanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 1),
    _StaTcpipIpsIplanrx_Type()
)
staTcpipIpsIplanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIplanrx.setStatus("mandatory")
_StaTcpipIpsIplantx_Type = Integer32
_StaTcpipIpsIplantx_Object = MibScalar
staTcpipIpsIplantx = _StaTcpipIpsIplantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 2),
    _StaTcpipIpsIplantx_Type()
)
staTcpipIpsIplantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIplantx.setStatus("mandatory")
_StaTcpipIpsIplanchecksumerrors_Type = Integer32
_StaTcpipIpsIplanchecksumerrors_Object = MibScalar
staTcpipIpsIplanchecksumerrors = _StaTcpipIpsIplanchecksumerrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 3),
    _StaTcpipIpsIplanchecksumerrors_Type()
)
staTcpipIpsIplanchecksumerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIplanchecksumerrors.setStatus("mandatory")
_StaTcpipIpsIplanserviceerrors_Type = Integer32
_StaTcpipIpsIplanserviceerrors_Object = MibScalar
staTcpipIpsIplanserviceerrors = _StaTcpipIpsIplanserviceerrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 4),
    _StaTcpipIpsIplanserviceerrors_Type()
)
staTcpipIpsIplanserviceerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIplanserviceerrors.setStatus("mandatory")
_StaTcpipIpsIpwanrx_Type = Integer32
_StaTcpipIpsIpwanrx_Object = MibScalar
staTcpipIpsIpwanrx = _StaTcpipIpsIpwanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 5),
    _StaTcpipIpsIpwanrx_Type()
)
staTcpipIpsIpwanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIpwanrx.setStatus("mandatory")
_StaTcpipIpsIpwantx_Type = Integer32
_StaTcpipIpsIpwantx_Object = MibScalar
staTcpipIpsIpwantx = _StaTcpipIpsIpwantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 6),
    _StaTcpipIpsIpwantx_Type()
)
staTcpipIpsIpwantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIpwantx.setStatus("mandatory")
_StaTcpipIpsIpwanchecksumerrors_Type = Integer32
_StaTcpipIpsIpwanchecksumerrors_Object = MibScalar
staTcpipIpsIpwanchecksumerrors = _StaTcpipIpsIpwanchecksumerrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 7),
    _StaTcpipIpsIpwanchecksumerrors_Type()
)
staTcpipIpsIpwanchecksumerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIpwanchecksumerrors.setStatus("mandatory")
_StaTcpipIpsIpwanserviceerrors_Type = Integer32
_StaTcpipIpsIpwanserviceerrors_Object = MibScalar
staTcpipIpsIpwanserviceerrors = _StaTcpipIpsIpwanserviceerrors_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 8),
    _StaTcpipIpsIpwanserviceerrors_Type()
)
staTcpipIpsIpwanserviceerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIpwanserviceerrors.setStatus("mandatory")
_StaTcpipIpsIpwanrxdisconnect_Type = Integer32
_StaTcpipIpsIpwanrxdisconnect_Object = MibScalar
staTcpipIpsIpwanrxdisconnect = _StaTcpipIpsIpwanrxdisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 9),
    _StaTcpipIpsIpwanrxdisconnect_Type()
)
staTcpipIpsIpwanrxdisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIpwanrxdisconnect.setStatus("mandatory")
_StaTcpipIpsIplanfragmentationer_Type = Integer32
_StaTcpipIpsIplanfragmentationer_Object = MibScalar
staTcpipIpsIplanfragmentationer = _StaTcpipIpsIplanfragmentationer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 10),
    _StaTcpipIpsIplanfragmentationer_Type()
)
staTcpipIpsIplanfragmentationer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIplanfragmentationer.setStatus("mandatory")
_StaTcpipIpsIpwanfragmentationer_Type = Integer32
_StaTcpipIpsIpwanfragmentationer_Object = MibScalar
staTcpipIpsIpwanfragmentationer = _StaTcpipIpsIpwanfragmentationer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 11),
    _StaTcpipIpsIpwanfragmentationer_Type()
)
staTcpipIpsIpwanfragmentationer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIpwanfragmentationer.setStatus("mandatory")
_StaTcpipIpsDeletevalues_Type = Integer32
_StaTcpipIpsDeletevalues_Object = MibScalar
staTcpipIpsDeletevalues = _StaTcpipIpsDeletevalues_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 12),
    _StaTcpipIpsDeletevalues_Type()
)
staTcpipIpsDeletevalues.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staTcpipIpsDeletevalues.setStatus("mandatory")
_StaTcpipIpsIplanfragmentations_Type = Integer32
_StaTcpipIpsIplanfragmentations_Object = MibScalar
staTcpipIpsIplanfragmentations = _StaTcpipIpsIplanfragmentations_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 13),
    _StaTcpipIpsIplanfragmentations_Type()
)
staTcpipIpsIplanfragmentations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIplanfragmentations.setStatus("mandatory")
_StaTcpipIpsIplanfragmentationsf_Type = Integer32
_StaTcpipIpsIplanfragmentationsf_Object = MibScalar
staTcpipIpsIplanfragmentationsf = _StaTcpipIpsIplanfragmentationsf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 14),
    _StaTcpipIpsIplanfragmentationsf_Type()
)
staTcpipIpsIplanfragmentationsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIplanfragmentationsf.setStatus("mandatory")
_StaTcpipIpsIpwanfragmentations_Type = Integer32
_StaTcpipIpsIpwanfragmentations_Object = MibScalar
staTcpipIpsIpwanfragmentations = _StaTcpipIpsIpwanfragmentations_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 15),
    _StaTcpipIpsIpwanfragmentations_Type()
)
staTcpipIpsIpwanfragmentations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIpwanfragmentations.setStatus("mandatory")
_StaTcpipIpsIpwanfragmentationsf_Type = Integer32
_StaTcpipIpsIpwanfragmentationsf_Object = MibScalar
staTcpipIpsIpwanfragmentationsf = _StaTcpipIpsIpwanfragmentationsf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 2, 16),
    _StaTcpipIpsIpwanfragmentationsf_Type()
)
staTcpipIpsIpwanfragmentationsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIpsIpwanfragmentationsf.setStatus("mandatory")
_StaTcpipIcm_ObjectIdentity = ObjectIdentity
staTcpipIcm = _StaTcpipIcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 3)
)
_StaTcpipIcmIcmplanr_Type = Integer32
_StaTcpipIcmIcmplanr_Object = MibScalar
staTcpipIcmIcmplanr = _StaTcpipIcmIcmplanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 3, 1),
    _StaTcpipIcmIcmplanr_Type()
)
staTcpipIcmIcmplanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIcmIcmplanr.setStatus("mandatory")
_StaTcpipIcmIcmplant_Type = Integer32
_StaTcpipIcmIcmplant_Object = MibScalar
staTcpipIcmIcmplant = _StaTcpipIcmIcmplant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 3, 2),
    _StaTcpipIcmIcmplant_Type()
)
staTcpipIcmIcmplant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIcmIcmplant.setStatus("mandatory")
_StaTcpipIcmIcmplanc_Type = Integer32
_StaTcpipIcmIcmplanc_Object = MibScalar
staTcpipIcmIcmplanc = _StaTcpipIcmIcmplanc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 3, 3),
    _StaTcpipIcmIcmplanc_Type()
)
staTcpipIcmIcmplanc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIcmIcmplanc.setStatus("mandatory")
_StaTcpipIcmIcmplans_Type = Integer32
_StaTcpipIcmIcmplans_Object = MibScalar
staTcpipIcmIcmplans = _StaTcpipIcmIcmplans_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 3, 4),
    _StaTcpipIcmIcmplans_Type()
)
staTcpipIcmIcmplans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIcmIcmplans.setStatus("mandatory")
_StaTcpipIcmIcmpwanr_Type = Integer32
_StaTcpipIcmIcmpwanr_Object = MibScalar
staTcpipIcmIcmpwanr = _StaTcpipIcmIcmpwanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 3, 5),
    _StaTcpipIcmIcmpwanr_Type()
)
staTcpipIcmIcmpwanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIcmIcmpwanr.setStatus("mandatory")
_StaTcpipIcmIcmpwant_Type = Integer32
_StaTcpipIcmIcmpwant_Object = MibScalar
staTcpipIcmIcmpwant = _StaTcpipIcmIcmpwant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 3, 6),
    _StaTcpipIcmIcmpwant_Type()
)
staTcpipIcmIcmpwant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIcmIcmpwant.setStatus("mandatory")
_StaTcpipIcmIcmpwanc_Type = Integer32
_StaTcpipIcmIcmpwanc_Object = MibScalar
staTcpipIcmIcmpwanc = _StaTcpipIcmIcmpwanc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 3, 7),
    _StaTcpipIcmIcmpwanc_Type()
)
staTcpipIcmIcmpwanc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIcmIcmpwanc.setStatus("mandatory")
_StaTcpipIcmIcmpwans_Type = Integer32
_StaTcpipIcmIcmpwans_Object = MibScalar
staTcpipIcmIcmpwans = _StaTcpipIcmIcmpwans_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 3, 8),
    _StaTcpipIcmIcmpwans_Type()
)
staTcpipIcmIcmpwans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipIcmIcmpwans.setStatus("mandatory")
_StaTcpipIcmDeleteva_Type = Integer32
_StaTcpipIcmDeleteva_Object = MibScalar
staTcpipIcmDeleteva = _StaTcpipIcmDeleteva_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 3, 9),
    _StaTcpipIcmDeleteva_Type()
)
staTcpipIcmDeleteva.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staTcpipIcmDeleteva.setStatus("mandatory")
_StaTcpipTft_ObjectIdentity = ObjectIdentity
staTcpipTft = _StaTcpipTft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4)
)
_StaTcpipTftTftplanrx_Type = Integer32
_StaTcpipTftTftplanrx_Object = MibScalar
staTcpipTftTftplanrx = _StaTcpipTftTftplanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 1),
    _StaTcpipTftTftplanrx_Type()
)
staTcpipTftTftplanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplanrx.setStatus("mandatory")
_StaTcpipTftTftplanrxr_Type = Integer32
_StaTcpipTftTftplanrxr_Object = MibScalar
staTcpipTftTftplanrxr = _StaTcpipTftTftplanrxr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 2),
    _StaTcpipTftTftplanrxr_Type()
)
staTcpipTftTftplanrxr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplanrxr.setStatus("mandatory")
_StaTcpipTftTftplanrxw_Type = Integer32
_StaTcpipTftTftplanrxw_Object = MibScalar
staTcpipTftTftplanrxw = _StaTcpipTftTftplanrxw_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 3),
    _StaTcpipTftTftplanrxw_Type()
)
staTcpipTftTftplanrxw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplanrxw.setStatus("mandatory")
_StaTcpipTftTftplanrxd_Type = Integer32
_StaTcpipTftTftplanrxd_Object = MibScalar
staTcpipTftTftplanrxd = _StaTcpipTftTftplanrxd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 4),
    _StaTcpipTftTftplanrxd_Type()
)
staTcpipTftTftplanrxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplanrxd.setStatus("mandatory")
_StaTcpipTftTftplanrxa_Type = Integer32
_StaTcpipTftTftplanrxa_Object = MibScalar
staTcpipTftTftplanrxa = _StaTcpipTftTftplanrxa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 5),
    _StaTcpipTftTftplanrxa_Type()
)
staTcpipTftTftplanrxa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplanrxa.setStatus("mandatory")
_StaTcpipTftTftplanrxo_Type = Integer32
_StaTcpipTftTftplanrxo_Object = MibScalar
staTcpipTftTftplanrxo = _StaTcpipTftTftplanrxo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 6),
    _StaTcpipTftTftplanrxo_Type()
)
staTcpipTftTftplanrxo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplanrxo.setStatus("mandatory")
_StaTcpipTftTftplanrxe_Type = Integer32
_StaTcpipTftTftplanrxe_Object = MibScalar
staTcpipTftTftplanrxe = _StaTcpipTftTftplanrxe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 7),
    _StaTcpipTftTftplanrxe_Type()
)
staTcpipTftTftplanrxe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplanrxe.setStatus("mandatory")
_StaTcpipTftTftplanrxb_Type = Integer32
_StaTcpipTftTftplanrxb_Object = MibScalar
staTcpipTftTftplanrxb = _StaTcpipTftTftplanrxb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 8),
    _StaTcpipTftTftplanrxb_Type()
)
staTcpipTftTftplanrxb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplanrxb.setStatus("mandatory")
_StaTcpipTftTftplantx_Type = Integer32
_StaTcpipTftTftplantx_Object = MibScalar
staTcpipTftTftplantx = _StaTcpipTftTftplantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 9),
    _StaTcpipTftTftplantx_Type()
)
staTcpipTftTftplantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplantx.setStatus("mandatory")
_StaTcpipTftTftplantxd_Type = Integer32
_StaTcpipTftTftplantxd_Object = MibScalar
staTcpipTftTftplantxd = _StaTcpipTftTftplantxd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 10),
    _StaTcpipTftTftplantxd_Type()
)
staTcpipTftTftplantxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplantxd.setStatus("mandatory")
_StaTcpipTftTftplantxa_Type = Integer32
_StaTcpipTftTftplantxa_Object = MibScalar
staTcpipTftTftplantxa = _StaTcpipTftTftplantxa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 11),
    _StaTcpipTftTftplantxa_Type()
)
staTcpipTftTftplantxa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplantxa.setStatus("mandatory")
_StaTcpipTftTftplantxo_Type = Integer32
_StaTcpipTftTftplantxo_Object = MibScalar
staTcpipTftTftplantxo = _StaTcpipTftTftplantxo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 12),
    _StaTcpipTftTftplantxo_Type()
)
staTcpipTftTftplantxo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplantxo.setStatus("mandatory")
_StaTcpipTftTftplantxe_Type = Integer32
_StaTcpipTftTftplantxe_Object = MibScalar
staTcpipTftTftplantxe = _StaTcpipTftTftplantxe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 13),
    _StaTcpipTftTftplantxe_Type()
)
staTcpipTftTftplantxe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplantxe.setStatus("mandatory")
_StaTcpipTftTftplantxr_Type = Integer32
_StaTcpipTftTftplantxr_Object = MibScalar
staTcpipTftTftplantxr = _StaTcpipTftTftplantxr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 14),
    _StaTcpipTftTftplantxr_Type()
)
staTcpipTftTftplantxr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplantxr.setStatus("mandatory")
_StaTcpipTftTftplancon_Type = Integer32
_StaTcpipTftTftplancon_Object = MibScalar
staTcpipTftTftplancon = _StaTcpipTftTftplancon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 15),
    _StaTcpipTftTftplancon_Type()
)
staTcpipTftTftplancon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftplancon.setStatus("mandatory")
_StaTcpipTftTftpwanrx_Type = Integer32
_StaTcpipTftTftpwanrx_Object = MibScalar
staTcpipTftTftpwanrx = _StaTcpipTftTftpwanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 16),
    _StaTcpipTftTftpwanrx_Type()
)
staTcpipTftTftpwanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwanrx.setStatus("mandatory")
_StaTcpipTftTftpwanrxr_Type = Integer32
_StaTcpipTftTftpwanrxr_Object = MibScalar
staTcpipTftTftpwanrxr = _StaTcpipTftTftpwanrxr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 17),
    _StaTcpipTftTftpwanrxr_Type()
)
staTcpipTftTftpwanrxr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwanrxr.setStatus("mandatory")
_StaTcpipTftTftpwanrxw_Type = Integer32
_StaTcpipTftTftpwanrxw_Object = MibScalar
staTcpipTftTftpwanrxw = _StaTcpipTftTftpwanrxw_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 18),
    _StaTcpipTftTftpwanrxw_Type()
)
staTcpipTftTftpwanrxw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwanrxw.setStatus("mandatory")
_StaTcpipTftTftpwanrxd_Type = Integer32
_StaTcpipTftTftpwanrxd_Object = MibScalar
staTcpipTftTftpwanrxd = _StaTcpipTftTftpwanrxd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 19),
    _StaTcpipTftTftpwanrxd_Type()
)
staTcpipTftTftpwanrxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwanrxd.setStatus("mandatory")
_StaTcpipTftTftpwanrxa_Type = Integer32
_StaTcpipTftTftpwanrxa_Object = MibScalar
staTcpipTftTftpwanrxa = _StaTcpipTftTftpwanrxa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 20),
    _StaTcpipTftTftpwanrxa_Type()
)
staTcpipTftTftpwanrxa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwanrxa.setStatus("mandatory")
_StaTcpipTftTftpwanrxo_Type = Integer32
_StaTcpipTftTftpwanrxo_Object = MibScalar
staTcpipTftTftpwanrxo = _StaTcpipTftTftpwanrxo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 21),
    _StaTcpipTftTftpwanrxo_Type()
)
staTcpipTftTftpwanrxo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwanrxo.setStatus("mandatory")
_StaTcpipTftTftpwanrxe_Type = Integer32
_StaTcpipTftTftpwanrxe_Object = MibScalar
staTcpipTftTftpwanrxe = _StaTcpipTftTftpwanrxe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 22),
    _StaTcpipTftTftpwanrxe_Type()
)
staTcpipTftTftpwanrxe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwanrxe.setStatus("mandatory")
_StaTcpipTftTftpwanrxb_Type = Integer32
_StaTcpipTftTftpwanrxb_Object = MibScalar
staTcpipTftTftpwanrxb = _StaTcpipTftTftpwanrxb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 23),
    _StaTcpipTftTftpwanrxb_Type()
)
staTcpipTftTftpwanrxb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwanrxb.setStatus("mandatory")
_StaTcpipTftTftpwantx_Type = Integer32
_StaTcpipTftTftpwantx_Object = MibScalar
staTcpipTftTftpwantx = _StaTcpipTftTftpwantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 24),
    _StaTcpipTftTftpwantx_Type()
)
staTcpipTftTftpwantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwantx.setStatus("mandatory")
_StaTcpipTftTftpwantxd_Type = Integer32
_StaTcpipTftTftpwantxd_Object = MibScalar
staTcpipTftTftpwantxd = _StaTcpipTftTftpwantxd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 25),
    _StaTcpipTftTftpwantxd_Type()
)
staTcpipTftTftpwantxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwantxd.setStatus("mandatory")
_StaTcpipTftTftpwantxa_Type = Integer32
_StaTcpipTftTftpwantxa_Object = MibScalar
staTcpipTftTftpwantxa = _StaTcpipTftTftpwantxa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 26),
    _StaTcpipTftTftpwantxa_Type()
)
staTcpipTftTftpwantxa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwantxa.setStatus("mandatory")
_StaTcpipTftTftpwantxo_Type = Integer32
_StaTcpipTftTftpwantxo_Object = MibScalar
staTcpipTftTftpwantxo = _StaTcpipTftTftpwantxo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 27),
    _StaTcpipTftTftpwantxo_Type()
)
staTcpipTftTftpwantxo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwantxo.setStatus("mandatory")
_StaTcpipTftTftpwantxe_Type = Integer32
_StaTcpipTftTftpwantxe_Object = MibScalar
staTcpipTftTftpwantxe = _StaTcpipTftTftpwantxe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 28),
    _StaTcpipTftTftpwantxe_Type()
)
staTcpipTftTftpwantxe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwantxe.setStatus("mandatory")
_StaTcpipTftTftpwantxr_Type = Integer32
_StaTcpipTftTftpwantxr_Object = MibScalar
staTcpipTftTftpwantxr = _StaTcpipTftTftpwantxr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 29),
    _StaTcpipTftTftpwantxr_Type()
)
staTcpipTftTftpwantxr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwantxr.setStatus("mandatory")
_StaTcpipTftTftpwancon_Type = Integer32
_StaTcpipTftTftpwancon_Object = MibScalar
staTcpipTftTftpwancon = _StaTcpipTftTftpwancon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 30),
    _StaTcpipTftTftpwancon_Type()
)
staTcpipTftTftpwancon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTftTftpwancon.setStatus("mandatory")
_StaTcpipTftDeletevalu_Type = Integer32
_StaTcpipTftDeletevalu_Object = MibScalar
staTcpipTftDeletevalu = _StaTcpipTftDeletevalu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 4, 31),
    _StaTcpipTftDeletevalu_Type()
)
staTcpipTftDeletevalu.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staTcpipTftDeletevalu.setStatus("mandatory")
_StaTcpipTcp_ObjectIdentity = ObjectIdentity
staTcpipTcp = _StaTcpipTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5)
)
_StaTcpipTcpTcplanrx_Type = Integer32
_StaTcpipTcpTcplanrx_Object = MibScalar
staTcpipTcpTcplanrx = _StaTcpipTcpTcplanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 1),
    _StaTcpipTcpTcplanrx_Type()
)
staTcpipTcpTcplanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcplanrx.setStatus("mandatory")
_StaTcpipTcpTcplantx_Type = Integer32
_StaTcpipTcpTcplantx_Object = MibScalar
staTcpipTcpTcplantx = _StaTcpipTcpTcplantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 2),
    _StaTcpipTcpTcplantx_Type()
)
staTcpipTcpTcplantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcplantx.setStatus("mandatory")
_StaTcpipTcpTcplantxr_Type = Integer32
_StaTcpipTcpTcplantxr_Object = MibScalar
staTcpipTcpTcplantxr = _StaTcpipTcpTcplantxr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 3),
    _StaTcpipTcpTcplantxr_Type()
)
staTcpipTcpTcplantxr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcplantxr.setStatus("mandatory")
_StaTcpipTcpTcplanche_Type = Integer32
_StaTcpipTcpTcplanche_Object = MibScalar
staTcpipTcpTcplanche = _StaTcpipTcpTcplanche_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 4),
    _StaTcpipTcpTcplanche_Type()
)
staTcpipTcpTcplanche.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcplanche.setStatus("mandatory")
_StaTcpipTcpTcplanser_Type = Integer32
_StaTcpipTcpTcplanser_Object = MibScalar
staTcpipTcpTcplanser = _StaTcpipTcpTcplanser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 5),
    _StaTcpipTcpTcplanser_Type()
)
staTcpipTcpTcplanser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcplanser.setStatus("mandatory")
_StaTcpipTcpTcplancon_Type = Integer32
_StaTcpipTcpTcplancon_Object = MibScalar
staTcpipTcpTcplancon = _StaTcpipTcpTcplancon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 6),
    _StaTcpipTcpTcplancon_Type()
)
staTcpipTcpTcplancon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcplancon.setStatus("mandatory")
_StaTcpipTcpTcpwanrx_Type = Integer32
_StaTcpipTcpTcpwanrx_Object = MibScalar
staTcpipTcpTcpwanrx = _StaTcpipTcpTcpwanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 7),
    _StaTcpipTcpTcpwanrx_Type()
)
staTcpipTcpTcpwanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcpwanrx.setStatus("mandatory")
_StaTcpipTcpTcpwantx_Type = Integer32
_StaTcpipTcpTcpwantx_Object = MibScalar
staTcpipTcpTcpwantx = _StaTcpipTcpTcpwantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 8),
    _StaTcpipTcpTcpwantx_Type()
)
staTcpipTcpTcpwantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcpwantx.setStatus("mandatory")
_StaTcpipTcpTcpwantxr_Type = Integer32
_StaTcpipTcpTcpwantxr_Object = MibScalar
staTcpipTcpTcpwantxr = _StaTcpipTcpTcpwantxr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 9),
    _StaTcpipTcpTcpwantxr_Type()
)
staTcpipTcpTcpwantxr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcpwantxr.setStatus("mandatory")
_StaTcpipTcpTcpwanche_Type = Integer32
_StaTcpipTcpTcpwanche_Object = MibScalar
staTcpipTcpTcpwanche = _StaTcpipTcpTcpwanche_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 10),
    _StaTcpipTcpTcpwanche_Type()
)
staTcpipTcpTcpwanche.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcpwanche.setStatus("mandatory")
_StaTcpipTcpTcpwanser_Type = Integer32
_StaTcpipTcpTcpwanser_Object = MibScalar
staTcpipTcpTcpwanser = _StaTcpipTcpTcpwanser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 11),
    _StaTcpipTcpTcpwanser_Type()
)
staTcpipTcpTcpwanser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcpwanser.setStatus("mandatory")
_StaTcpipTcpTcpwancon_Type = Integer32
_StaTcpipTcpTcpwancon_Object = MibScalar
staTcpipTcpTcpwancon = _StaTcpipTcpTcpwancon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 12),
    _StaTcpipTcpTcpwancon_Type()
)
staTcpipTcpTcpwancon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipTcpTcpwancon.setStatus("mandatory")
_StaTcpipTcpDeleteval_Type = Integer32
_StaTcpipTcpDeleteval_Object = MibScalar
staTcpipTcpDeleteval = _StaTcpipTcpDeleteval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 5, 13),
    _StaTcpipTcpDeleteval_Type()
)
staTcpipTcpDeleteval.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staTcpipTcpDeleteval.setStatus("mandatory")
_StaTcpipDhc_ObjectIdentity = ObjectIdentity
staTcpipDhc = _StaTcpipDhc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6)
)
_StaTcpipDhcDhcplanrx_Type = Integer32
_StaTcpipDhcDhcplanrx_Object = MibScalar
staTcpipDhcDhcplanrx = _StaTcpipDhcDhcplanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 1),
    _StaTcpipDhcDhcplanrx_Type()
)
staTcpipDhcDhcplanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcplanrx.setStatus("mandatory")
_StaTcpipDhcDhcplantx_Type = Integer32
_StaTcpipDhcDhcplantx_Object = MibScalar
staTcpipDhcDhcplantx = _StaTcpipDhcDhcplantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 2),
    _StaTcpipDhcDhcplantx_Type()
)
staTcpipDhcDhcplantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcplantx.setStatus("mandatory")
_StaTcpipDhcDhcpwanrx_Type = Integer32
_StaTcpipDhcDhcpwanrx_Object = MibScalar
staTcpipDhcDhcpwanrx = _StaTcpipDhcDhcpwanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 3),
    _StaTcpipDhcDhcpwanrx_Type()
)
staTcpipDhcDhcpwanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcpwanrx.setStatus("mandatory")
_StaTcpipDhcDhcpdisca_Type = Integer32
_StaTcpipDhcDhcpdisca_Object = MibScalar
staTcpipDhcDhcpdisca = _StaTcpipDhcDhcpdisca_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 4),
    _StaTcpipDhcDhcpdisca_Type()
)
staTcpipDhcDhcpdisca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcpdisca.setStatus("mandatory")
_StaTcpipDhcDhcprxdis_Type = Integer32
_StaTcpipDhcDhcprxdis_Object = MibScalar
staTcpipDhcDhcprxdis = _StaTcpipDhcDhcprxdis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 5),
    _StaTcpipDhcDhcprxdis_Type()
)
staTcpipDhcDhcprxdis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcprxdis.setStatus("mandatory")
_StaTcpipDhcDhcprxreq_Type = Integer32
_StaTcpipDhcDhcprxreq_Object = MibScalar
staTcpipDhcDhcprxreq = _StaTcpipDhcDhcprxreq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 6),
    _StaTcpipDhcDhcprxreq_Type()
)
staTcpipDhcDhcprxreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcprxreq.setStatus("mandatory")
_StaTcpipDhcDhcprxdec_Type = Integer32
_StaTcpipDhcDhcprxdec_Object = MibScalar
staTcpipDhcDhcprxdec = _StaTcpipDhcDhcprxdec_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 7),
    _StaTcpipDhcDhcprxdec_Type()
)
staTcpipDhcDhcprxdec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcprxdec.setStatus("mandatory")
_StaTcpipDhcDhcprxinf_Type = Integer32
_StaTcpipDhcDhcprxinf_Object = MibScalar
staTcpipDhcDhcprxinf = _StaTcpipDhcDhcprxinf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 8),
    _StaTcpipDhcDhcprxinf_Type()
)
staTcpipDhcDhcprxinf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcprxinf.setStatus("mandatory")
_StaTcpipDhcDhcprxrel_Type = Integer32
_StaTcpipDhcDhcprxrel_Object = MibScalar
staTcpipDhcDhcprxrel = _StaTcpipDhcDhcprxrel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 9),
    _StaTcpipDhcDhcprxrel_Type()
)
staTcpipDhcDhcprxrel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcprxrel.setStatus("mandatory")
_StaTcpipDhcDhcptxoff_Type = Integer32
_StaTcpipDhcDhcptxoff_Object = MibScalar
staTcpipDhcDhcptxoff = _StaTcpipDhcDhcptxoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 10),
    _StaTcpipDhcDhcptxoff_Type()
)
staTcpipDhcDhcptxoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcptxoff.setStatus("mandatory")
_StaTcpipDhcDhcptxack_Type = Integer32
_StaTcpipDhcDhcptxack_Object = MibScalar
staTcpipDhcDhcptxack = _StaTcpipDhcDhcptxack_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 11),
    _StaTcpipDhcDhcptxack_Type()
)
staTcpipDhcDhcptxack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcptxack.setStatus("mandatory")
_StaTcpipDhcDhcptxnak_Type = Integer32
_StaTcpipDhcDhcptxnak_Object = MibScalar
staTcpipDhcDhcptxnak = _StaTcpipDhcDhcptxnak_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 12),
    _StaTcpipDhcDhcptxnak_Type()
)
staTcpipDhcDhcptxnak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcptxnak.setStatus("mandatory")
_StaTcpipDhcDchpserve_Type = Integer32
_StaTcpipDhcDchpserve_Object = MibScalar
staTcpipDhcDchpserve = _StaTcpipDhcDchpserve_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 13),
    _StaTcpipDhcDchpserve_Type()
)
staTcpipDhcDchpserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDchpserve.setStatus("mandatory")
_StaTcpipDhcDhcpassig_Type = Integer32
_StaTcpipDhcDhcpassig_Object = MibScalar
staTcpipDhcDhcpassig = _StaTcpipDhcDhcpassig_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 14),
    _StaTcpipDhcDhcpassig_Type()
)
staTcpipDhcDhcpassig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcpassig.setStatus("mandatory")
_StaTcpipDhcDhcpmacco_Type = Integer32
_StaTcpipDhcDhcpmacco_Object = MibScalar
staTcpipDhcDhcpmacco = _StaTcpipDhcDhcpmacco_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 15),
    _StaTcpipDhcDhcpmacco_Type()
)
staTcpipDhcDhcpmacco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcDhcpmacco.setStatus("mandatory")
_StaTcpipDhcTabledhcp_Object = MibTable
staTcpipDhcTabledhcp = _StaTcpipDhcTabledhcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 16)
)
if mibBuilder.loadTexts:
    staTcpipDhcTabledhcp.setStatus("mandatory")
_StaTcpipDhcTabledhcpCols_Object = MibTableRow
staTcpipDhcTabledhcpCols = _StaTcpipDhcTabledhcpCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 16, 1)
)
staTcpipDhcTabledhcpCols.setIndexNames(
    (0, "ELSA-MIB", "staTcpipDhcTabledhcpIpa"),
)
if mibBuilder.loadTexts:
    staTcpipDhcTabledhcpCols.setStatus("mandatory")
_StaTcpipDhcTabledhcpIpa_Type = IpAddress
_StaTcpipDhcTabledhcpIpa_Object = MibTableColumn
staTcpipDhcTabledhcpIpa = _StaTcpipDhcTabledhcpIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 16, 1, 1),
    _StaTcpipDhcTabledhcpIpa_Type()
)
staTcpipDhcTabledhcpIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcTabledhcpIpa.setStatus("mandatory")
_StaTcpipDhcTabledhcpNod_Type = DisplayString
_StaTcpipDhcTabledhcpNod_Object = MibTableColumn
staTcpipDhcTabledhcpNod = _StaTcpipDhcTabledhcpNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 16, 1, 2),
    _StaTcpipDhcTabledhcpNod_Type()
)
staTcpipDhcTabledhcpNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcTabledhcpNod.setStatus("mandatory")
_StaTcpipDhcTabledhcpTim_Type = Integer32
_StaTcpipDhcTabledhcpTim_Object = MibTableColumn
staTcpipDhcTabledhcpTim = _StaTcpipDhcTabledhcpTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 16, 1, 3),
    _StaTcpipDhcTabledhcpTim_Type()
)
staTcpipDhcTabledhcpTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcTabledhcpTim.setStatus("mandatory")
_StaTcpipDhcTabledhcpHos_Type = DisplayString
_StaTcpipDhcTabledhcpHos_Object = MibTableColumn
staTcpipDhcTabledhcpHos = _StaTcpipDhcTabledhcpHos_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 16, 1, 4),
    _StaTcpipDhcTabledhcpHos_Type()
)
staTcpipDhcTabledhcpHos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcTabledhcpHos.setStatus("mandatory")


class _StaTcpipDhcTabledhcpTyp_Type(Integer32):
    """Custom type staTcpipDhcTabledhcpTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8,
              16,
              32,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 32),
          ("dyn", 16),
          ("new", 2),
          ("relay", 2048),
          ("stat", 8),
          ("unkn", 4))
    )


_StaTcpipDhcTabledhcpTyp_Type.__name__ = "Integer32"
_StaTcpipDhcTabledhcpTyp_Object = MibTableColumn
staTcpipDhcTabledhcpTyp = _StaTcpipDhcTabledhcpTyp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 16, 1, 5),
    _StaTcpipDhcTabledhcpTyp_Type()
)
staTcpipDhcTabledhcpTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcTabledhcpTyp.setStatus("mandatory")
_StaTcpipDhcServerfla_Type = DisplayString
_StaTcpipDhcServerfla_Object = MibScalar
staTcpipDhcServerfla = _StaTcpipDhcServerfla_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 17),
    _StaTcpipDhcServerfla_Type()
)
staTcpipDhcServerfla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDhcServerfla.setStatus("mandatory")
_StaTcpipDhcDeleteval_Type = Integer32
_StaTcpipDhcDeleteval_Object = MibScalar
staTcpipDhcDeleteval = _StaTcpipDhcDeleteval_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 6, 18),
    _StaTcpipDhcDeleteval_Type()
)
staTcpipDhcDeleteval.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staTcpipDhcDeleteval.setStatus("mandatory")
_StaTcpipDel_Type = Integer32
_StaTcpipDel_Object = MibScalar
staTcpipDel = _StaTcpipDel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 7),
    _StaTcpipDel_Type()
)
staTcpipDel.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staTcpipDel.setStatus("mandatory")
_StaTcpipNet_ObjectIdentity = ObjectIdentity
staTcpipNet = _StaTcpipNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8)
)
_StaTcpipNetLanr_Type = Integer32
_StaTcpipNetLanr_Object = MibScalar
staTcpipNetLanr = _StaTcpipNetLanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 1),
    _StaTcpipNetLanr_Type()
)
staTcpipNetLanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetLanr.setStatus("mandatory")
_StaTcpipNetLant_Type = Integer32
_StaTcpipNetLant_Object = MibScalar
staTcpipNetLant = _StaTcpipNetLant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 2),
    _StaTcpipNetLant_Type()
)
staTcpipNetLant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetLant.setStatus("mandatory")
_StaTcpipNetWanr_Type = Integer32
_StaTcpipNetWanr_Object = MibScalar
staTcpipNetWanr = _StaTcpipNetWanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 3),
    _StaTcpipNetWanr_Type()
)
staTcpipNetWanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetWanr.setStatus("mandatory")
_StaTcpipNetWant_Type = Integer32
_StaTcpipNetWant_Object = MibScalar
staTcpipNetWant = _StaTcpipNetWant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 4),
    _StaTcpipNetWant_Type()
)
staTcpipNetWant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetWant.setStatus("mandatory")
_StaTcpipNetRegi_Type = Integer32
_StaTcpipNetRegi_Object = MibScalar
staTcpipNetRegi = _StaTcpipNetRegi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 5),
    _StaTcpipNetRegi_Type()
)
staTcpipNetRegi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetRegi.setStatus("mandatory")
_StaTcpipNetConf_Type = Integer32
_StaTcpipNetConf_Object = MibScalar
staTcpipNetConf = _StaTcpipNetConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 6),
    _StaTcpipNetConf_Type()
)
staTcpipNetConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetConf.setStatus("mandatory")
_StaTcpipNetRele_Type = Integer32
_StaTcpipNetRele_Object = MibScalar
staTcpipNetRele = _StaTcpipNetRele_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 7),
    _StaTcpipNetRele_Type()
)
staTcpipNetRele.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetRele.setStatus("mandatory")
_StaTcpipNetRefr_Type = Integer32
_StaTcpipNetRefr_Object = MibScalar
staTcpipNetRefr = _StaTcpipNetRefr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 8),
    _StaTcpipNetRefr_Type()
)
staTcpipNetRefr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetRefr.setStatus("mandatory")
_StaTcpipNetTime_Type = Integer32
_StaTcpipNetTime_Object = MibScalar
staTcpipNetTime = _StaTcpipNetTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 9),
    _StaTcpipNetTime_Type()
)
staTcpipNetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetTime.setStatus("mandatory")
_StaTcpipNetHost_Type = Integer32
_StaTcpipNetHost_Object = MibScalar
staTcpipNetHost = _StaTcpipNetHost_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 10),
    _StaTcpipNetHost_Type()
)
staTcpipNetHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetHost.setStatus("mandatory")
_StaTcpipNetGrou_Type = Integer32
_StaTcpipNetGrou_Object = MibScalar
staTcpipNetGrou = _StaTcpipNetGrou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 11),
    _StaTcpipNetGrou_Type()
)
staTcpipNetGrou.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetGrou.setStatus("mandatory")
_StaTcpipNetBnod_Type = Integer32
_StaTcpipNetBnod_Object = MibScalar
staTcpipNetBnod = _StaTcpipNetBnod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 12),
    _StaTcpipNetBnod_Type()
)
staTcpipNetBnod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetBnod.setStatus("mandatory")
_StaTcpipNetPnod_Type = Integer32
_StaTcpipNetPnod_Object = MibScalar
staTcpipNetPnod = _StaTcpipNetPnod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 13),
    _StaTcpipNetPnod_Type()
)
staTcpipNetPnod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetPnod.setStatus("mandatory")
_StaTcpipNetMnod_Type = Integer32
_StaTcpipNetMnod_Object = MibScalar
staTcpipNetMnod = _StaTcpipNetMnod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 14),
    _StaTcpipNetMnod_Type()
)
staTcpipNetMnod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetMnod.setStatus("mandatory")
_StaTcpipNetWnod_Type = Integer32
_StaTcpipNetWnod_Object = MibScalar
staTcpipNetWnod = _StaTcpipNetWnod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 15),
    _StaTcpipNetWnod_Type()
)
staTcpipNetWnod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetWnod.setStatus("mandatory")
_StaTcpipNetRemo_Object = MibTable
staTcpipNetRemo = _StaTcpipNetRemo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 16)
)
if mibBuilder.loadTexts:
    staTcpipNetRemo.setStatus("mandatory")
_StaTcpipNetRemoCols_Object = MibTableRow
staTcpipNetRemoCols = _StaTcpipNetRemoCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 16, 1)
)
staTcpipNetRemoCols.setIndexNames(
    (0, "ELSA-MIB", "staTcpipNetRemoNam"),
)
if mibBuilder.loadTexts:
    staTcpipNetRemoCols.setStatus("mandatory")
_StaTcpipNetRemoNam_Type = DisplayString
_StaTcpipNetRemoNam_Object = MibTableColumn
staTcpipNetRemoNam = _StaTcpipNetRemoNam_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 16, 1, 1),
    _StaTcpipNetRemoNam_Type()
)
staTcpipNetRemoNam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetRemoNam.setStatus("mandatory")


class _StaTcpipNetRemoTyp_Type(Integer32):
    """Custom type staTcpipNetRemoTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("router", 0),
          ("workstation", 1))
    )


_StaTcpipNetRemoTyp_Type.__name__ = "Integer32"
_StaTcpipNetRemoTyp_Object = MibTableColumn
staTcpipNetRemoTyp = _StaTcpipNetRemoTyp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 16, 1, 2),
    _StaTcpipNetRemoTyp_Type()
)
staTcpipNetRemoTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetRemoTyp.setStatus("mandatory")
_StaTcpipNetRemoBac_Type = Integer32
_StaTcpipNetRemoBac_Object = MibTableColumn
staTcpipNetRemoBac = _StaTcpipNetRemoBac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 16, 1, 3),
    _StaTcpipNetRemoBac_Type()
)
staTcpipNetRemoBac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetRemoBac.setStatus("mandatory")
_StaTcpipNetRemoTim_Type = Integer32
_StaTcpipNetRemoTim_Object = MibTableColumn
staTcpipNetRemoTim = _StaTcpipNetRemoTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 16, 1, 4),
    _StaTcpipNetRemoTim_Type()
)
staTcpipNetRemoTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipNetRemoTim.setStatus("mandatory")
_StaTcpipNetDele_Type = Integer32
_StaTcpipNetDele_Object = MibScalar
staTcpipNetDele = _StaTcpipNetDele_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 8, 17),
    _StaTcpipNetDele_Type()
)
staTcpipNetDele.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staTcpipNetDele.setStatus("mandatory")
_StaTcpipDns_ObjectIdentity = ObjectIdentity
staTcpipDns = _StaTcpipDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9)
)
_StaTcpipDnsLanr_Type = Integer32
_StaTcpipDnsLanr_Object = MibScalar
staTcpipDnsLanr = _StaTcpipDnsLanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 1),
    _StaTcpipDnsLanr_Type()
)
staTcpipDnsLanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsLanr.setStatus("mandatory")
_StaTcpipDnsLant_Type = Integer32
_StaTcpipDnsLant_Object = MibScalar
staTcpipDnsLant = _StaTcpipDnsLant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 2),
    _StaTcpipDnsLant_Type()
)
staTcpipDnsLant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsLant.setStatus("mandatory")
_StaTcpipDnsWanr_Type = Integer32
_StaTcpipDnsWanr_Object = MibScalar
staTcpipDnsWanr = _StaTcpipDnsWanr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 3),
    _StaTcpipDnsWanr_Type()
)
staTcpipDnsWanr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsWanr.setStatus("mandatory")
_StaTcpipDnsWant_Type = Integer32
_StaTcpipDnsWant_Object = MibScalar
staTcpipDnsWant = _StaTcpipDnsWant_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 4),
    _StaTcpipDnsWant_Type()
)
staTcpipDnsWant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsWant.setStatus("mandatory")
_StaTcpipDnsForw_Type = Integer32
_StaTcpipDnsForw_Object = MibScalar
staTcpipDnsForw = _StaTcpipDnsForw_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 5),
    _StaTcpipDnsForw_Type()
)
staTcpipDnsForw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsForw.setStatus("mandatory")
_StaTcpipDnsErro_Type = Integer32
_StaTcpipDnsErro_Object = MibScalar
staTcpipDnsErro = _StaTcpipDnsErro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 6),
    _StaTcpipDnsErro_Type()
)
staTcpipDnsErro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsErro.setStatus("mandatory")
_StaTcpipDnsDnsa_Type = Integer32
_StaTcpipDnsDnsa_Object = MibScalar
staTcpipDnsDnsa = _StaTcpipDnsDnsa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 7),
    _StaTcpipDnsDnsa_Type()
)
staTcpipDnsDnsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsDnsa.setStatus("mandatory")
_StaTcpipDnsDhcp_Type = Integer32
_StaTcpipDnsDhcp_Object = MibScalar
staTcpipDnsDhcp = _StaTcpipDnsDhcp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 8),
    _StaTcpipDnsDhcp_Type()
)
staTcpipDnsDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsDhcp.setStatus("mandatory")
_StaTcpipDnsNetb_Type = Integer32
_StaTcpipDnsNetb_Object = MibScalar
staTcpipDnsNetb = _StaTcpipDnsNetb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 9),
    _StaTcpipDnsNetb_Type()
)
staTcpipDnsNetb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsNetb.setStatus("mandatory")
_StaTcpipDnsFilt_Type = Integer32
_StaTcpipDnsFilt_Object = MibScalar
staTcpipDnsFilt = _StaTcpipDnsFilt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 10),
    _StaTcpipDnsFilt_Type()
)
staTcpipDnsFilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsFilt.setStatus("mandatory")
_StaTcpipDnsHitl_Object = MibTable
staTcpipDnsHitl = _StaTcpipDnsHitl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 11)
)
if mibBuilder.loadTexts:
    staTcpipDnsHitl.setStatus("mandatory")
_StaTcpipDnsHitlCols_Object = MibTableRow
staTcpipDnsHitlCols = _StaTcpipDnsHitlCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 11, 1)
)
staTcpipDnsHitlCols.setIndexNames(
    (0, "ELSA-MIB", "staTcpipDnsHitlDom"),
)
if mibBuilder.loadTexts:
    staTcpipDnsHitlCols.setStatus("mandatory")
_StaTcpipDnsHitlDom_Type = DisplayString
_StaTcpipDnsHitlDom_Object = MibTableColumn
staTcpipDnsHitlDom = _StaTcpipDnsHitlDom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 11, 1, 1),
    _StaTcpipDnsHitlDom_Type()
)
staTcpipDnsHitlDom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsHitlDom.setStatus("mandatory")
_StaTcpipDnsHitlReq_Type = Integer32
_StaTcpipDnsHitlReq_Object = MibTableColumn
staTcpipDnsHitlReq = _StaTcpipDnsHitlReq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 11, 1, 2),
    _StaTcpipDnsHitlReq_Type()
)
staTcpipDnsHitlReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsHitlReq.setStatus("mandatory")
_StaTcpipDnsHitlTim_Type = DisplayString
_StaTcpipDnsHitlTim_Object = MibTableColumn
staTcpipDnsHitlTim = _StaTcpipDnsHitlTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 11, 1, 3),
    _StaTcpipDnsHitlTim_Type()
)
staTcpipDnsHitlTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsHitlTim.setStatus("mandatory")
_StaTcpipDnsHitlIpa_Type = IpAddress
_StaTcpipDnsHitlIpa_Object = MibTableColumn
staTcpipDnsHitlIpa = _StaTcpipDnsHitlIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 11, 1, 4),
    _StaTcpipDnsHitlIpa_Type()
)
staTcpipDnsHitlIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipDnsHitlIpa.setStatus("mandatory")
_StaTcpipDnsDele_Type = Integer32
_StaTcpipDnsDele_Object = MibScalar
staTcpipDnsDele = _StaTcpipDnsDele_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 9, 12),
    _StaTcpipDnsDele_Type()
)
staTcpipDnsDele.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staTcpipDnsDele.setStatus("mandatory")
_StaTcpipHtt_ObjectIdentity = ObjectIdentity
staTcpipHtt = _StaTcpipHtt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 10)
)
_StaTcpipHttHttpac_Type = Integer32
_StaTcpipHttHttpac_Object = MibScalar
staTcpipHttHttpac = _StaTcpipHttHttpac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 10, 1),
    _StaTcpipHttHttpac_Type()
)
staTcpipHttHttpac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipHttHttpac.setStatus("mandatory")
_StaTcpipHttHttpno_Type = Integer32
_StaTcpipHttHttpno_Object = MibScalar
staTcpipHttHttpno = _StaTcpipHttHttpno_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 10, 2),
    _StaTcpipHttHttpno_Type()
)
staTcpipHttHttpno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipHttHttpno.setStatus("mandatory")
_StaTcpipHttHttpau_Type = Integer32
_StaTcpipHttHttpau_Object = MibScalar
staTcpipHttHttpau = _StaTcpipHttHttpau_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 10, 3),
    _StaTcpipHttHttpau_Type()
)
staTcpipHttHttpau.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipHttHttpau.setStatus("mandatory")
_StaTcpipHttHttppr_Type = Integer32
_StaTcpipHttHttppr_Object = MibScalar
staTcpipHttHttppr = _StaTcpipHttHttppr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 10, 4),
    _StaTcpipHttHttppr_Type()
)
staTcpipHttHttppr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTcpipHttHttppr.setStatus("mandatory")
_StaTcpipHttDelete_Type = Integer32
_StaTcpipHttDelete_Object = MibScalar
staTcpipHttDelete = _StaTcpipHttDelete_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 9, 10, 5),
    _StaTcpipHttDelete_Type()
)
staTcpipHttDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staTcpipHttDelete.setStatus("mandatory")
_StaIprou_ObjectIdentity = ObjectIdentity
staIprou = _StaIprou_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10)
)
_StaIprouIprlanrx_Type = Integer32
_StaIprouIprlanrx_Object = MibScalar
staIprouIprlanrx = _StaIprouIprlanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 1),
    _StaIprouIprlanrx_Type()
)
staIprouIprlanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprlanrx.setStatus("mandatory")
_StaIprouIprlantx_Type = Integer32
_StaIprouIprlantx_Object = MibScalar
staIprouIprlantx = _StaIprouIprlantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 2),
    _StaIprouIprlantx_Type()
)
staIprouIprlantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprlantx.setStatus("mandatory")
_StaIprouIprlanlo_Type = Integer32
_StaIprouIprlanlo_Object = MibScalar
staIprouIprlanlo = _StaIprouIprlanlo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 3),
    _StaIprouIprlanlo_Type()
)
staIprouIprlanlo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprlanlo.setStatus("mandatory")
_StaIprouIprlanne_Type = Integer32
_StaIprouIprlanne_Object = MibScalar
staIprouIprlanne = _StaIprouIprlanne_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 4),
    _StaIprouIprlanne_Type()
)
staIprouIprlanne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprlanne.setStatus("mandatory")
_StaIprouIprlanro_Type = Integer32
_StaIprouIprlanro_Object = MibScalar
staIprouIprlanro = _StaIprouIprlanro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 5),
    _StaIprouIprlanro_Type()
)
staIprouIprlanro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprlanro.setStatus("mandatory")
_StaIprouIprlantt_Type = Integer32
_StaIprouIprlantt_Object = MibScalar
staIprouIprlantt = _StaIprouIprlantt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 6),
    _StaIprouIprlantt_Type()
)
staIprouIprlantt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprlantt.setStatus("mandatory")
_StaIprouIprlanfi_Type = Integer32
_StaIprouIprlanfi_Object = MibScalar
staIprouIprlanfi = _StaIprouIprlanfi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 7),
    _StaIprouIprlanfi_Type()
)
staIprouIprlanfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprlanfi.setStatus("mandatory")
_StaIprouIprlandi_Type = Integer32
_StaIprouIprlandi_Object = MibScalar
staIprouIprlandi = _StaIprouIprlandi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 8),
    _StaIprouIprlandi_Type()
)
staIprouIprlandi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprlandi.setStatus("mandatory")
_StaIprouIprwanrx_Type = Integer32
_StaIprouIprwanrx_Object = MibScalar
staIprouIprwanrx = _StaIprouIprwanrx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 9),
    _StaIprouIprwanrx_Type()
)
staIprouIprwanrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprwanrx.setStatus("mandatory")
_StaIprouIprwantx_Type = Integer32
_StaIprouIprwantx_Object = MibScalar
staIprouIprwantx = _StaIprouIprwantx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 10),
    _StaIprouIprwantx_Type()
)
staIprouIprwantx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprwantx.setStatus("mandatory")
_StaIprouIprwanne_Type = Integer32
_StaIprouIprwanne_Object = MibScalar
staIprouIprwanne = _StaIprouIprwanne_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 11),
    _StaIprouIprwanne_Type()
)
staIprouIprwanne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprwanne.setStatus("mandatory")
_StaIprouIprwantt_Type = Integer32
_StaIprouIprwantt_Object = MibScalar
staIprouIprwantt = _StaIprouIprwantt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 12),
    _StaIprouIprwantt_Type()
)
staIprouIprwantt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprwantt.setStatus("mandatory")
_StaIprouIprwanfi_Type = Integer32
_StaIprouIprwanfi_Object = MibScalar
staIprouIprwanfi = _StaIprouIprwanfi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 13),
    _StaIprouIprwanfi_Type()
)
staIprouIprwanfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprwanfi.setStatus("mandatory")
_StaIprouIprwandi_Type = Integer32
_StaIprouIprwandi_Object = MibScalar
staIprouIprwandi = _StaIprouIprwandi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 14),
    _StaIprouIprwandi_Type()
)
staIprouIprwandi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprwandi.setStatus("mandatory")
_StaIprouIprwanty_Type = Integer32
_StaIprouIprwanty_Object = MibScalar
staIprouIprwanty = _StaIprouIprwanty_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 15),
    _StaIprouIprwanty_Type()
)
staIprouIprwanty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprwanty.setStatus("mandatory")
_StaIprouIprarper_Type = Integer32
_StaIprouIprarper_Object = MibScalar
staIprouIprarper = _StaIprouIprarper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 16),
    _StaIprouIprarper_Type()
)
staIprouIprarper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouIprarper.setStatus("mandatory")
_StaIprouEstablis_Object = MibTable
staIprouEstablis = _StaIprouEstablis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 17)
)
if mibBuilder.loadTexts:
    staIprouEstablis.setStatus("mandatory")
_StaIprouEstablisCols_Object = MibTableRow
staIprouEstablisCols = _StaIprouEstablisCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 17, 1)
)
staIprouEstablisCols.setIndexNames(
    (0, "ELSA-MIB", "staIprouEstablisTim"),
)
if mibBuilder.loadTexts:
    staIprouEstablisCols.setStatus("mandatory")
_StaIprouEstablisTim_Type = DisplayString
_StaIprouEstablisTim_Object = MibTableColumn
staIprouEstablisTim = _StaIprouEstablisTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 17, 1, 1),
    _StaIprouEstablisTim_Type()
)
staIprouEstablisTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouEstablisTim.setStatus("mandatory")
_StaIprouEstablisDes_Type = IpAddress
_StaIprouEstablisDes_Object = MibTableColumn
staIprouEstablisDes = _StaIprouEstablisDes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 17, 1, 2),
    _StaIprouEstablisDes_Type()
)
staIprouEstablisDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouEstablisDes.setStatus("mandatory")
_StaIprouEstablisSrc_Type = IpAddress
_StaIprouEstablisSrc_Object = MibTableColumn
staIprouEstablisSrc = _StaIprouEstablisSrc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 17, 1, 3),
    _StaIprouEstablisSrc_Type()
)
staIprouEstablisSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouEstablisSrc.setStatus("mandatory")


class _StaIprouEstablisPro_Type(Integer32):
    """Custom type staIprouEstablisPro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              8,
              17,
              62)
        )
    )
    namedValues = NamedValues(
        *(("cftp", 62),
          ("egp", 8),
          ("ggt", 3),
          ("icmp", 1),
          ("igmp", 2),
          ("tcp", 6),
          ("udp", 17))
    )


_StaIprouEstablisPro_Type.__name__ = "Integer32"
_StaIprouEstablisPro_Object = MibTableColumn
staIprouEstablisPro = _StaIprouEstablisPro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 17, 1, 4),
    _StaIprouEstablisPro_Type()
)
staIprouEstablisPro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouEstablisPro.setStatus("mandatory")
_StaIprouEstablisDpo_Type = Integer32
_StaIprouEstablisDpo_Object = MibTableColumn
staIprouEstablisDpo = _StaIprouEstablisDpo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 17, 1, 5),
    _StaIprouEstablisDpo_Type()
)
staIprouEstablisDpo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouEstablisDpo.setStatus("mandatory")
_StaIprouEstablisSpo_Type = Integer32
_StaIprouEstablisSpo_Object = MibTableColumn
staIprouEstablisSpo = _StaIprouEstablisSpo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 10, 17, 1, 6),
    _StaIprouEstablisSpo_Type()
)
staIprouEstablisSpo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staIprouEstablisSpo.setStatus("mandatory")
_StaConfi_ObjectIdentity = ObjectIdentity
staConfi = _StaConfi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11)
)
_StaConfiLanactiv_Type = Integer32
_StaConfiLanactiv_Object = MibScalar
staConfiLanactiv = _StaConfiLanactiv_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 1),
    _StaConfiLanactiv_Type()
)
staConfiLanactiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConfiLanactiv.setStatus("mandatory")
_StaConfiLantotal_Type = Integer32
_StaConfiLantotal_Object = MibScalar
staConfiLantotal = _StaConfiLantotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 2),
    _StaConfiLantotal_Type()
)
staConfiLantotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConfiLantotal.setStatus("mandatory")
_StaConfiWanactiv_Type = Integer32
_StaConfiWanactiv_Object = MibScalar
staConfiWanactiv = _StaConfiWanactiv_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 3),
    _StaConfiWanactiv_Type()
)
staConfiWanactiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConfiWanactiv.setStatus("mandatory")
_StaConfiWantotal_Type = Integer32
_StaConfiWantotal_Object = MibScalar
staConfiWantotal = _StaConfiWantotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 4),
    _StaConfiWantotal_Type()
)
staConfiWantotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConfiWantotal.setStatus("mandatory")
_StaConfiOutbanda_Type = Integer32
_StaConfiOutbanda_Object = MibScalar
staConfiOutbanda = _StaConfiOutbanda_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 5),
    _StaConfiOutbanda_Type()
)
staConfiOutbanda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConfiOutbanda.setStatus("mandatory")
_StaConfiOutbandt_Type = Integer32
_StaConfiOutbandt_Object = MibScalar
staConfiOutbandt = _StaConfiOutbandt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 6),
    _StaConfiOutbandt_Type()
)
staConfiOutbandt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConfiOutbandt.setStatus("mandatory")
_StaConfiOutbandb_Type = Integer32
_StaConfiOutbandb_Object = MibScalar
staConfiOutbandb = _StaConfiOutbandb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 7),
    _StaConfiOutbandb_Type()
)
staConfiOutbandb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConfiOutbandb.setStatus("mandatory")
_StaConfiLoginerr_Type = Integer32
_StaConfiLoginerr_Object = MibScalar
staConfiLoginerr = _StaConfiLoginerr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 8),
    _StaConfiLoginerr_Type()
)
staConfiLoginerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConfiLoginerr.setStatus("mandatory")
_StaConfiLoginloc_Type = Integer32
_StaConfiLoginloc_Object = MibScalar
staConfiLoginloc = _StaConfiLoginloc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 9),
    _StaConfiLoginloc_Type()
)
staConfiLoginloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConfiLoginloc.setStatus("mandatory")
_StaConfiLoginrej_Type = Integer32
_StaConfiLoginrej_Object = MibScalar
staConfiLoginrej = _StaConfiLoginrej_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 10),
    _StaConfiLoginrej_Type()
)
staConfiLoginrej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConfiLoginrej.setStatus("mandatory")
_StaConfiDeleteva_Type = Integer32
_StaConfiDeleteva_Object = MibScalar
staConfiDeleteva = _StaConfiDeleteva_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 11, 11),
    _StaConfiDeleteva_Type()
)
staConfiDeleteva.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staConfiDeleteva.setStatus("mandatory")
_StaQueue_ObjectIdentity = ObjectIdentity
staQueue = _StaQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12)
)
_StaQueueLanheap_Type = Integer32
_StaQueueLanheap_Object = MibScalar
staQueueLanheap = _StaQueueLanheap_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 1),
    _StaQueueLanheap_Type()
)
staQueueLanheap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueLanheap.setStatus("mandatory")
_StaQueueLanqueu_Type = Integer32
_StaQueueLanqueu_Object = MibScalar
staQueueLanqueu = _StaQueueLanqueu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 2),
    _StaQueueLanqueu_Type()
)
staQueueLanqueu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueLanqueu.setStatus("mandatory")
_StaQueueWanheap_Type = Integer32
_StaQueueWanheap_Object = MibScalar
staQueueWanheap = _StaQueueWanheap_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 3),
    _StaQueueWanheap_Type()
)
staQueueWanheap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueWanheap.setStatus("mandatory")
_StaQueueWanqueu_Type = Integer32
_StaQueueWanqueu_Object = MibScalar
staQueueWanqueu = _StaQueueWanqueu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 4),
    _StaQueueWanqueu_Type()
)
staQueueWanqueu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueWanqueu.setStatus("mandatory")
_StaQueueBridgei_Type = Integer32
_StaQueueBridgei_Object = MibScalar
staQueueBridgei = _StaQueueBridgei_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 5),
    _StaQueueBridgei_Type()
)
staQueueBridgei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueBridgei.setStatus("mandatory")
_StaQueueBridgee_Type = Integer32
_StaQueueBridgee_Object = MibScalar
staQueueBridgee = _StaQueueBridgee_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 6),
    _StaQueueBridgee_Type()
)
staQueueBridgee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueBridgee.setStatus("mandatory")
_StaQueueArpquer_Type = Integer32
_StaQueueArpquer_Object = MibScalar
staQueueArpquer = _StaQueueArpquer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 7),
    _StaQueueArpquer_Type()
)
staQueueArpquer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueArpquer.setStatus("mandatory")
_StaQueueArpqueu_Type = Integer32
_StaQueueArpqueu_Object = MibScalar
staQueueArpqueu = _StaQueueArpqueu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 8),
    _StaQueueArpqueu_Type()
)
staQueueArpqueu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueArpqueu.setStatus("mandatory")
_StaQueueIpqueue_Type = Integer32
_StaQueueIpqueue_Object = MibScalar
staQueueIpqueue = _StaQueueIpqueue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 9),
    _StaQueueIpqueue_Type()
)
staQueueIpqueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueIpqueue.setStatus("mandatory")
_StaQueueIpurgen_Type = Integer32
_StaQueueIpurgen_Object = MibScalar
staQueueIpurgen = _StaQueueIpurgen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 10),
    _StaQueueIpurgen_Type()
)
staQueueIpurgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueIpurgen.setStatus("mandatory")
_StaQueueIcmpque_Type = Integer32
_StaQueueIcmpque_Object = MibScalar
staQueueIcmpque = _StaQueueIcmpque_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 11),
    _StaQueueIcmpque_Type()
)
staQueueIcmpque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueIcmpque.setStatus("mandatory")
_StaQueueTcpqueu_Type = Integer32
_StaQueueTcpqueu_Object = MibScalar
staQueueTcpqueu = _StaQueueTcpqueu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 12),
    _StaQueueTcpqueu_Type()
)
staQueueTcpqueu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueTcpqueu.setStatus("mandatory")
_StaQueueTftpser_Type = Integer32
_StaQueueTftpser_Object = MibScalar
staQueueTftpser = _StaQueueTftpser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 13),
    _StaQueueTftpser_Type()
)
staQueueTftpser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueTftpser.setStatus("mandatory")
_StaQueueSnmpque_Type = Integer32
_StaQueueSnmpque_Object = MibScalar
staQueueSnmpque = _StaQueueSnmpque_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 14),
    _StaQueueSnmpque_Type()
)
staQueueSnmpque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueSnmpque.setStatus("mandatory")
_StaQueueIpxqueu_Type = Integer32
_StaQueueIpxqueu_Object = MibScalar
staQueueIpxqueu = _StaQueueIpxqueu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 15),
    _StaQueueIpxqueu_Type()
)
staQueueIpxqueu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueIpxqueu.setStatus("mandatory")
_StaQueueRipquer_Type = Integer32
_StaQueueRipquer_Object = MibScalar
staQueueRipquer = _StaQueueRipquer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 16),
    _StaQueueRipquer_Type()
)
staQueueRipquer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueRipquer.setStatus("mandatory")
_StaQueueSapqueu_Type = Integer32
_StaQueueSapqueu_Object = MibScalar
staQueueSapqueu = _StaQueueSapqueu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 17),
    _StaQueueSapqueu_Type()
)
staQueueSapqueu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueSapqueu.setStatus("mandatory")
_StaQueueIpxwatc_Type = Integer32
_StaQueueIpxwatc_Object = MibScalar
staQueueIpxwatc = _StaQueueIpxwatc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 18),
    _StaQueueIpxwatc_Type()
)
staQueueIpxwatc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueIpxwatc.setStatus("mandatory")
_StaQueueSpxwatc_Type = Integer32
_StaQueueSpxwatc_Object = MibScalar
staQueueSpxwatc = _StaQueueSpxwatc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 19),
    _StaQueueSpxwatc_Type()
)
staQueueSpxwatc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueSpxwatc.setStatus("mandatory")
_StaQueueIpxrout_Type = Integer32
_StaQueueIpxrout_Object = MibScalar
staQueueIpxrout = _StaQueueIpxrout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 21),
    _StaQueueIpxrout_Type()
)
staQueueIpxrout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueIpxrout.setStatus("mandatory")
_StaQueueProthea_Type = Integer32
_StaQueueProthea_Object = MibScalar
staQueueProthea = _StaQueueProthea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 22),
    _StaQueueProthea_Type()
)
staQueueProthea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueProthea.setStatus("mandatory")
_StaQueueIprqueu_Type = Integer32
_StaQueueIprqueu_Object = MibScalar
staQueueIprqueu = _StaQueueIprqueu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 24),
    _StaQueueIprqueu_Type()
)
staQueueIprqueu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueIprqueu.setStatus("mandatory")
_StaQueueDhcpser_Type = Integer32
_StaQueueDhcpser_Object = MibScalar
staQueueDhcpser = _StaQueueDhcpser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 27),
    _StaQueueDhcpser_Type()
)
staQueueDhcpser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueDhcpser.setStatus("mandatory")
_StaQueueDhcpcli_Type = Integer32
_StaQueueDhcpcli_Object = MibScalar
staQueueDhcpcli = _StaQueueDhcpcli_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 28),
    _StaQueueDhcpcli_Type()
)
staQueueDhcpcli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueDhcpcli.setStatus("mandatory")
_StaQueueIprripq_Type = Integer32
_StaQueueIprripq_Object = MibScalar
staQueueIprripq = _StaQueueIprripq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 29),
    _StaQueueIprripq_Type()
)
staQueueIprripq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueIprripq.setStatus("mandatory")
_StaQueueDnstxqu_Type = Integer32
_StaQueueDnstxqu_Object = MibScalar
staQueueDnstxqu = _StaQueueDnstxqu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 30),
    _StaQueueDnstxqu_Type()
)
staQueueDnstxqu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueDnstxqu.setStatus("mandatory")
_StaQueueDnsrxqu_Type = Integer32
_StaQueueDnsrxqu_Object = MibScalar
staQueueDnsrxqu = _StaQueueDnsrxqu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 31),
    _StaQueueDnsrxqu_Type()
)
staQueueDnsrxqu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueDnsrxqu.setStatus("mandatory")
_StaQueueIpmasqt_Type = Integer32
_StaQueueIpmasqt_Object = MibScalar
staQueueIpmasqt = _StaQueueIpmasqt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 32),
    _StaQueueIpmasqt_Type()
)
staQueueIpmasqt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueIpmasqt.setStatus("mandatory")
_StaQueueIpmasqr_Type = Integer32
_StaQueueIpmasqr_Object = MibScalar
staQueueIpmasqr = _StaQueueIpmasqr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 12, 33),
    _StaQueueIpmasqr_Type()
)
staQueueIpmasqr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staQueueIpmasqr.setStatus("mandatory")
_StaConns_Object = MibTable
staConns = _StaConns_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 13)
)
if mibBuilder.loadTexts:
    staConns.setStatus("mandatory")
_StaConnsCols_Object = MibTableRow
staConnsCols = _StaConnsCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 13, 1)
)
staConnsCols.setIndexNames(
    (0, "ELSA-MIB", "staConnsIfc"),
)
if mibBuilder.loadTexts:
    staConnsCols.setStatus("mandatory")


class _StaConnsIfc_Type(Integer32):
    """Custom type staConnsIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaConnsIfc_Type.__name__ = "Integer32"
_StaConnsIfc_Object = MibTableColumn
staConnsIfc = _StaConnsIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 13, 1, 1),
    _StaConnsIfc_Type()
)
staConnsIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConnsIfc.setStatus("mandatory")
_StaConnsConn_Type = Integer32
_StaConnsConn_Object = MibTableColumn
staConnsConn = _StaConnsConn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 13, 1, 2),
    _StaConnsConn_Type()
)
staConnsConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConnsConn.setStatus("mandatory")
_StaConnsActi_Type = Integer32
_StaConnsActi_Object = MibTableColumn
staConnsActi = _StaConnsActi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 13, 1, 3),
    _StaConnsActi_Type()
)
staConnsActi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConnsActi.setStatus("mandatory")
_StaConnsPass_Type = Integer32
_StaConnsPass_Object = MibTableColumn
staConnsPass = _StaConnsPass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 13, 1, 4),
    _StaConnsPass_Type()
)
staConnsPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConnsPass.setStatus("mandatory")
_StaConnsErro_Type = Integer32
_StaConnsErro_Object = MibTableColumn
staConnsErro = _StaConnsErro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 13, 1, 5),
    _StaConnsErro_Type()
)
staConnsErro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConnsErro.setStatus("mandatory")
_StaConnsCont_Type = DisplayString
_StaConnsCont_Object = MibTableColumn
staConnsCont = _StaConnsCont_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 13, 1, 6),
    _StaConnsCont_Type()
)
staConnsCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConnsCont.setStatus("mandatory")
_StaConnsChar_Type = Integer32
_StaConnsChar_Object = MibTableColumn
staConnsChar = _StaConnsChar_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 13, 1, 7),
    _StaConnsChar_Type()
)
staConnsChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staConnsChar.setStatus("mandatory")
_StaInfoc_Object = MibTable
staInfoc = _StaInfoc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 14)
)
if mibBuilder.loadTexts:
    staInfoc.setStatus("mandatory")
_StaInfocCols_Object = MibTableRow
staInfocCols = _StaInfocCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 14, 1)
)
staInfocCols.setIndexNames(
    (0, "ELSA-MIB", "staInfocIfc"),
)
if mibBuilder.loadTexts:
    staInfocCols.setStatus("mandatory")


class _StaInfocIfc_Type(Integer32):
    """Custom type staInfocIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaInfocIfc_Type.__name__ = "Integer32"
_StaInfocIfc_Object = MibTableColumn
staInfocIfc = _StaInfocIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 14, 1, 1),
    _StaInfocIfc_Type()
)
staInfocIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staInfocIfc.setStatus("mandatory")
_StaInfocSta_Type = DisplayString
_StaInfocSta_Object = MibTableColumn
staInfocSta = _StaInfocSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 14, 1, 2),
    _StaInfocSta_Type()
)
staInfocSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staInfocSta.setStatus("mandatory")


class _StaInfocMod_Type(Integer32):
    """Custom type staInfocMod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("callback", 9),
          ("passive", 5),
          ("unknown", 0))
    )


_StaInfocMod_Type.__name__ = "Integer32"
_StaInfocMod_Object = MibTableColumn
staInfocMod = _StaInfocMod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 14, 1, 3),
    _StaInfocMod_Type()
)
staInfocMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staInfocMod.setStatus("mandatory")
_StaInfocDia_Type = DisplayString
_StaInfocDia_Object = MibTableColumn
staInfocDia = _StaInfocDia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 14, 1, 4),
    _StaInfocDia_Type()
)
staInfocDia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staInfocDia.setStatus("mandatory")
_StaInfocDev_Type = DisplayString
_StaInfocDev_Object = MibTableColumn
staInfocDev = _StaInfocDev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 14, 1, 5),
    _StaInfocDev_Type()
)
staInfocDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staInfocDev.setStatus("mandatory")
_StaInfocB1d_Type = Integer32
_StaInfocB1d_Object = MibTableColumn
staInfocB1d = _StaInfocB1d_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 14, 1, 6),
    _StaInfocB1d_Type()
)
staInfocB1d.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staInfocB1d.setStatus("mandatory")
_StaInfocB2d_Type = Integer32
_StaInfocB2d_Object = MibTableColumn
staInfocB2d = _StaInfocB2d_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 14, 1, 7),
    _StaInfocB2d_Type()
)
staInfocB2d.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staInfocB2d.setStatus("mandatory")
_StaLayer_Object = MibTable
staLayer = _StaLayer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 15)
)
if mibBuilder.loadTexts:
    staLayer.setStatus("mandatory")
_StaLayerCols_Object = MibTableRow
staLayerCols = _StaLayerCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 15, 1)
)
staLayerCols.setIndexNames(
    (0, "ELSA-MIB", "staLayerIfc"),
)
if mibBuilder.loadTexts:
    staLayerCols.setStatus("mandatory")


class _StaLayerIfc_Type(Integer32):
    """Custom type staLayerIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaLayerIfc_Type.__name__ = "Integer32"
_StaLayerIfc_Object = MibTableColumn
staLayerIfc = _StaLayerIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 15, 1, 1),
    _StaLayerIfc_Type()
)
staLayerIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLayerIfc.setStatus("mandatory")
_StaLayerWanl_Type = DisplayString
_StaLayerWanl_Object = MibTableColumn
staLayerWanl = _StaLayerWanl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 15, 1, 2),
    _StaLayerWanl_Type()
)
staLayerWanl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLayerWanl.setStatus("mandatory")


class _StaLayerEnca_Type(Integer32):
    """Custom type staLayerEnca based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ether", 0),
          ("trans", 255))
    )


_StaLayerEnca_Type.__name__ = "Integer32"
_StaLayerEnca_Object = MibTableColumn
staLayerEnca = _StaLayerEnca_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 15, 1, 3),
    _StaLayerEnca_Type()
)
staLayerEnca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLayerEnca.setStatus("mandatory")


class _StaLayerLay3_Type(Integer32):
    """Custom type staLayerLay3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("appp", 5),
          ("elsa", 0),
          ("ppp", 4),
          ("scappp", 7),
          ("scppp", 6),
          ("sctrans", 8),
          ("trans", 255))
    )


_StaLayerLay3_Type.__name__ = "Integer32"
_StaLayerLay3_Object = MibTableColumn
staLayerLay3 = _StaLayerLay3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 15, 1, 4),
    _StaLayerLay3_Type()
)
staLayerLay3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLayerLay3.setStatus("mandatory")


class _StaLayerLay2_Type(Integer32):
    """Custom type staLayerLay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pppoe", 5),
          ("sscop", 6),
          ("trans", 1),
          ("x75lapb", 0))
    )


_StaLayerLay2_Type.__name__ = "Integer32"
_StaLayerLay2_Object = MibTableColumn
staLayerLay2 = _StaLayerLay2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 15, 1, 5),
    _StaLayerLay2_Type()
)
staLayerLay2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLayerLay2.setStatus("mandatory")


class _StaLayerL2op_Type(Integer32):
    """Custom type staLayerL2op based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bnd-and-cmpr", 2),
          ("bundle", 1),
          ("compr", 0),
          ("none", 255))
    )


_StaLayerL2op_Type.__name__ = "Integer32"
_StaLayerL2op_Object = MibTableColumn
staLayerL2op = _StaLayerL2op_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 15, 1, 6),
    _StaLayerL2op_Type()
)
staLayerL2op.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLayerL2op.setStatus("mandatory")


class _StaLayerLay1_Type(Integer32):
    """Custom type staLayerLay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              67,
              131)
        )
    )
    namedValues = NamedValues(
        *(("aal-5", 2),
          ("eth-10", 4),
          ("hdlc56k", 1),
          ("hdlc64k", 0),
          ("modem", 5),
          ("v110-19k2", 67),
          ("v110-38k4", 131),
          ("v110-9k6", 3))
    )


_StaLayerLay1_Type.__name__ = "Integer32"
_StaLayerLay1_Object = MibTableColumn
staLayerLay1 = _StaLayerLay1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 15, 1, 7),
    _StaLayerLay1_Type()
)
staLayerLay1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLayerLay1.setStatus("mandatory")


class _StaLayerL1pa_Type(Integer32):
    """Custom type staLayerL1pa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              43,
              44,
              45,
              46,
              47)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("v21-300", 1),
          ("v22-1200", 4),
          ("v22bis-2400", 5),
          ("v23-1200", 3),
          ("v23-600", 2),
          ("v32bis-12000", 10),
          ("v32bis-14400", 11),
          ("v32bis-7200", 8),
          ("v32qam-4800", 6),
          ("v32qam-9600", 7),
          ("v32tcm-9600", 9),
          ("v34-12000", 16),
          ("v34-14400", 17),
          ("v34-16800", 18),
          ("v34-19200", 19),
          ("v34-21600", 20),
          ("v34-2400", 12),
          ("v34-24000", 21),
          ("v34-26400", 22),
          ("v34-28800", 23),
          ("v34-31200", 24),
          ("v34-33600", 25),
          ("v34-4800", 13),
          ("v34-7200", 14),
          ("v34-9600", 15),
          ("v90-28000", 26),
          ("v90-29333", 27),
          ("v90-30667", 28),
          ("v90-32000", 29),
          ("v90-33333", 30),
          ("v90-34667", 31),
          ("v90-36000", 32),
          ("v90-37333", 33),
          ("v90-38667", 34),
          ("v90-40000", 35),
          ("v90-41333", 36),
          ("v90-42667", 37),
          ("v90-44000", 38),
          ("v90-45333", 39),
          ("v90-46667", 40),
          ("v90-48000", 41),
          ("v90-49333", 42),
          ("v90-50667", 43),
          ("v90-52000", 44),
          ("v90-53333", 45),
          ("v90-54667", 46),
          ("v90-56000", 47))
    )


_StaLayerL1pa_Type.__name__ = "Integer32"
_StaLayerL1pa_Object = MibTableColumn
staLayerL1pa = _StaLayerL1pa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 15, 1, 8),
    _StaLayerL1pa_Type()
)
staLayerL1pa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLayerL1pa.setStatus("mandatory")
_StaCalli_Object = MibTable
staCalli = _StaCalli_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 16)
)
if mibBuilder.loadTexts:
    staCalli.setStatus("mandatory")
_StaCalliCols_Object = MibTableRow
staCalliCols = _StaCalliCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 16, 1)
)
staCalliCols.setIndexNames(
    (0, "ELSA-MIB", "staCalliSys"),
)
if mibBuilder.loadTexts:
    staCalliCols.setStatus("mandatory")
_StaCalliSys_Type = DisplayString
_StaCalliSys_Object = MibTableColumn
staCalliSys = _StaCalliSys_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 16, 1, 1),
    _StaCalliSys_Type()
)
staCalliSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCalliSys.setStatus("mandatory")


class _StaCalliIfc_Type(Integer32):
    """Custom type staCalliIfc based on Integer32"""
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
        *(("s0-1", 1),
          ("s0-2", 2),
          ("s0-3", 3),
          ("s0-4", 4))
    )


_StaCalliIfc_Type.__name__ = "Integer32"
_StaCalliIfc_Object = MibTableColumn
staCalliIfc = _StaCalliIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 16, 1, 2),
    _StaCalliIfc_Type()
)
staCalliIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCalliIfc.setStatus("mandatory")
_StaCalliCli_Type = DisplayString
_StaCalliCli_Object = MibTableColumn
staCalliCli = _StaCalliCli_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 16, 1, 3),
    _StaCalliCli_Type()
)
staCalliCli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCalliCli.setStatus("mandatory")
_StaCalliDia_Type = DisplayString
_StaCalliDia_Object = MibTableColumn
staCalliDia = _StaCalliDia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 16, 1, 4),
    _StaCalliDia_Type()
)
staCalliDia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCalliDia.setStatus("mandatory")


class _StaCalliCap_Type(Integer32):
    """Custom type staCalliCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              13,
              14,
              15,
              67,
              131,
              255)
        )
    )
    namedValues = NamedValues(
        *(("a-3-1khz", 13),
          ("fax-g2-3", 15),
          ("hdlc56k", 1),
          ("hdlc64k", 0),
          ("modem", 5),
          ("speech", 14),
          ("unknown", 255),
          ("v110-19k2", 67),
          ("v110-38k4", 131),
          ("v110-9k6", 3))
    )


_StaCalliCap_Type.__name__ = "Integer32"
_StaCalliCap_Object = MibTableColumn
staCalliCap = _StaCalliCap_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 16, 1, 5),
    _StaCalliCap_Type()
)
staCalliCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCalliCap.setStatus("mandatory")
_StaCalliBch_Type = Integer32
_StaCalliBch_Object = MibTableColumn
staCalliBch = _StaCalliBch_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 16, 1, 6),
    _StaCalliBch_Type()
)
staCalliBch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCalliBch.setStatus("mandatory")
_StaRemot_Object = MibTable
staRemot = _StaRemot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 17)
)
if mibBuilder.loadTexts:
    staRemot.setStatus("mandatory")
_StaRemotCols_Object = MibTableRow
staRemotCols = _StaRemotCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 17, 1)
)
staRemotCols.setIndexNames(
    (0, "ELSA-MIB", "staRemotConns"),
)
if mibBuilder.loadTexts:
    staRemotCols.setStatus("mandatory")
_StaRemotConns_Type = DisplayString
_StaRemotConns_Object = MibTableColumn
staRemotConns = _StaRemotConns_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 17, 1, 1),
    _StaRemotConns_Type()
)
staRemotConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRemotConns.setStatus("mandatory")
_StaRemotRemot_Type = DisplayString
_StaRemotRemot_Object = MibTableColumn
staRemotRemot = _StaRemotRemot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 17, 1, 2),
    _StaRemotRemot_Type()
)
staRemotRemot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRemotRemot.setStatus("mandatory")


class _StaRemotMode_Type(Integer32):
    """Custom type staRemotMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("callback", 9),
          ("passive", 5),
          ("unknown", 0))
    )


_StaRemotMode_Type.__name__ = "Integer32"
_StaRemotMode_Object = MibTableColumn
staRemotMode = _StaRemotMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 17, 1, 3),
    _StaRemotMode_Type()
)
staRemotMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRemotMode.setStatus("mandatory")


class _StaRemotIfc_Type(Integer32):
    """Custom type staRemotIfc based on Integer32"""
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
        *(("ch01", 1),
          ("ch02", 2),
          ("ch03", 3),
          ("ch04", 4),
          ("ch05", 5),
          ("ch06", 6),
          ("ch07", 7),
          ("ch08", 8),
          ("ch09", 9),
          ("ch10", 10),
          ("ch11", 11),
          ("ch12", 12))
    )


_StaRemotIfc_Type.__name__ = "Integer32"
_StaRemotIfc_Object = MibTableColumn
staRemotIfc = _StaRemotIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 17, 1, 4),
    _StaRemotIfc_Type()
)
staRemotIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRemotIfc.setStatus("mandatory")
_StaRemotConnt_Type = DisplayString
_StaRemotConnt_Object = MibTableColumn
staRemotConnt = _StaRemotConnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 17, 1, 5),
    _StaRemotConnt_Type()
)
staRemotConnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRemotConnt.setStatus("mandatory")
_StaRemotCharg_Type = Integer32
_StaRemotCharg_Object = MibTableColumn
staRemotCharg = _StaRemotCharg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 17, 1, 6),
    _StaRemotCharg_Type()
)
staRemotCharg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staRemotCharg.setStatus("mandatory")
_StaCurre_Type = DisplayString
_StaCurre_Object = MibScalar
staCurre = _StaCurre_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 18),
    _StaCurre_Type()
)
staCurre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCurre.setStatus("mandatory")
_StaChann_Object = MibTable
staChann = _StaChann_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19)
)
if mibBuilder.loadTexts:
    staChann.setStatus("mandatory")
_StaChannCols_Object = MibTableRow
staChannCols = _StaChannCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1)
)
staChannCols.setIndexNames(
    (0, "ELSA-MIB", "staChannChan"),
)
if mibBuilder.loadTexts:
    staChannCols.setStatus("mandatory")


class _StaChannChan_Type(Integer32):
    """Custom type staChannChan based on Integer32"""
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
        *(("ab-1", 5),
          ("ab-2", 6),
          ("ab-3", 7),
          ("ab-4", 8),
          ("ab-err", 4),
          ("s0-1-b1", 2),
          ("s0-1-b2", 3),
          ("s0-1-err", 1))
    )


_StaChannChan_Type.__name__ = "Integer32"
_StaChannChan_Object = MibTableColumn
staChannChan = _StaChannChan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 1),
    _StaChannChan_Type()
)
staChannChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannChan.setStatus("mandatory")
_StaChannPlci_Type = Integer32
_StaChannPlci_Object = MibTableColumn
staChannPlci = _StaChannPlci_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 2),
    _StaChannPlci_Type()
)
staChannPlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannPlci.setStatus("mandatory")
_StaChannBus_Type = Integer32
_StaChannBus_Object = MibTableColumn
staChannBus = _StaChannBus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 3),
    _StaChannBus_Type()
)
staChannBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannBus.setStatus("mandatory")
_StaChannState_Type = Integer32
_StaChannState_Object = MibTableColumn
staChannState = _StaChannState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 4),
    _StaChannState_Type()
)
staChannState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannState.setStatus("mandatory")


class _StaChannApp_Type(Integer32):
    """Custom type staChannApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("a-b", 3),
          ("capi", 2),
          ("none", 0),
          ("router", 1),
          ("time-module", 255))
    )


_StaChannApp_Type.__name__ = "Integer32"
_StaChannApp_Object = MibTableColumn
staChannApp = _StaChannApp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 5),
    _StaChannApp_Type()
)
staChannApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannApp.setStatus("mandatory")


class _StaChannMode_Type(Integer32):
    """Custom type staChannMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("act", 1),
          ("pas", 2),
          ("perm", 3),
          ("unk", 0))
    )


_StaChannMode_Type.__name__ = "Integer32"
_StaChannMode_Object = MibTableColumn
staChannMode = _StaChannMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 6),
    _StaChannMode_Type()
)
staChannMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannMode.setStatus("mandatory")
_StaChannCause_Type = Integer32
_StaChannCause_Object = MibTableColumn
staChannCause = _StaChannCause_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 7),
    _StaChannCause_Type()
)
staChannCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staChannCause.setStatus("mandatory")
_StaChannNumbe_Type = DisplayString
_StaChannNumbe_Object = MibTableColumn
staChannNumbe = _StaChannNumbe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 8),
    _StaChannNumbe_Type()
)
staChannNumbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannNumbe.setStatus("mandatory")
_StaChannSubad_Type = Integer32
_StaChannSubad_Object = MibTableColumn
staChannSubad = _StaChannSubad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 9),
    _StaChannSubad_Type()
)
staChannSubad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannSubad.setStatus("mandatory")
_StaChannCharg_Type = Integer32
_StaChannCharg_Object = MibTableColumn
staChannCharg = _StaChannCharg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 10),
    _StaChannCharg_Type()
)
staChannCharg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannCharg.setStatus("mandatory")
_StaChannExtra_Type = DisplayString
_StaChannExtra_Object = MibTableColumn
staChannExtra = _StaChannExtra_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 11),
    _StaChannExtra_Type()
)
staChannExtra.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannExtra.setStatus("mandatory")
_StaChannConnt_Type = Integer32
_StaChannConnt_Object = MibTableColumn
staChannConnt = _StaChannConnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 12),
    _StaChannConnt_Type()
)
staChannConnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannConnt.setStatus("mandatory")
_StaChannConns_Type = Integer32
_StaChannConns_Object = MibTableColumn
staChannConns = _StaChannConns_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 13),
    _StaChannConns_Type()
)
staChannConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannConns.setStatus("mandatory")
_StaChannIsdnd_Type = DisplayString
_StaChannIsdnd_Object = MibTableColumn
staChannIsdnd = _StaChannIsdnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 19, 1, 14),
    _StaChannIsdnd_Type()
)
staChannIsdnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChannIsdnd.setStatus("mandatory")
_StaDelet_Type = Integer32
_StaDelet_Object = MibScalar
staDelet = _StaDelet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 20),
    _StaDelet_Type()
)
staDelet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staDelet.setStatus("mandatory")
_StaTimes_ObjectIdentity = ObjectIdentity
staTimes = _StaTimes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 21)
)
_StaTimesCur_Type = DisplayString
_StaTimesCur_Object = MibScalar
staTimesCur = _StaTimesCur_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 21, 1),
    _StaTimesCur_Type()
)
staTimesCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTimesCur.setStatus("mandatory")


class _StaTimesSou_Type(Integer32):
    """Custom type staTimesSou based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 2),
          ("lan", 3),
          ("lanconfig", 8),
          ("manual", 1),
          ("no", 0),
          ("ram", 4))
    )


_StaTimesSou_Type.__name__ = "Integer32"
_StaTimesSou_Object = MibScalar
staTimesSou = _StaTimesSou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 21, 2),
    _StaTimesSou_Type()
)
staTimesSou.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTimesSou.setStatus("mandatory")
_StaTimesSet_Type = Integer32
_StaTimesSet_Object = MibScalar
staTimesSet = _StaTimesSet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 21, 3),
    _StaTimesSet_Type()
)
staTimesSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTimesSet.setStatus("mandatory")
_StaTimesIsd_ObjectIdentity = ObjectIdentity
staTimesIsd = _StaTimesIsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 21, 4)
)
_StaTimesIsdConne_Type = Integer32
_StaTimesIsdConne_Object = MibScalar
staTimesIsdConne = _StaTimesIsdConne_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 21, 4, 1),
    _StaTimesIsdConne_Type()
)
staTimesIsdConne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTimesIsdConne.setStatus("mandatory")
_StaTimesIsdInfor_Type = Integer32
_StaTimesIsdInfor_Object = MibScalar
staTimesIsdInfor = _StaTimesIsdInfor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 21, 4, 2),
    _StaTimesIsdInfor_Type()
)
staTimesIsdInfor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTimesIsdInfor.setStatus("mandatory")
_StaTimesIsdInfoe_Type = Integer32
_StaTimesIsdInfoe_Object = MibScalar
staTimesIsdInfoe = _StaTimesIsdInfoe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 21, 4, 3),
    _StaTimesIsdInfoe_Type()
)
staTimesIsdInfoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTimesIsdInfoe.setStatus("mandatory")
_StaTimesIsdUnits_Type = Integer32
_StaTimesIsdUnits_Object = MibScalar
staTimesIsdUnits = _StaTimesIsdUnits_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 21, 4, 4),
    _StaTimesIsdUnits_Type()
)
staTimesIsdUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTimesIsdUnits.setStatus("mandatory")
_StaTimesIsdDelet_Type = Integer32
_StaTimesIsdDelet_Object = MibScalar
staTimesIsdDelet = _StaTimesIsdDelet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 21, 4, 5),
    _StaTimesIsdDelet_Type()
)
staTimesIsdDelet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staTimesIsdDelet.setStatus("mandatory")
_StaLcrst_ObjectIdentity = ObjectIdentity
staLcrst = _StaLcrst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22)
)
_StaLcrstTot_Type = Integer32
_StaLcrstTot_Object = MibScalar
staLcrstTot = _StaLcrstTot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22, 1),
    _StaLcrstTot_Type()
)
staLcrstTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLcrstTot.setStatus("mandatory")
_StaLcrstFou_Type = Integer32
_StaLcrstFou_Object = MibScalar
staLcrstFou = _StaLcrstFou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22, 2),
    _StaLcrstFou_Type()
)
staLcrstFou.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLcrstFou.setStatus("mandatory")
_StaLcrstNot_Type = Integer32
_StaLcrstNot_Object = MibScalar
staLcrstNot = _StaLcrstNot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22, 3),
    _StaLcrstNot_Type()
)
staLcrstNot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLcrstNot.setStatus("mandatory")
_StaLcrstMis_Type = Integer32
_StaLcrstMis_Object = MibScalar
staLcrstMis = _StaLcrstMis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22, 4),
    _StaLcrstMis_Type()
)
staLcrstMis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLcrstMis.setStatus("mandatory")
_StaLcrstPro_Object = MibTable
staLcrstPro = _StaLcrstPro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22, 6)
)
if mibBuilder.loadTexts:
    staLcrstPro.setStatus("mandatory")
_StaLcrstProCols_Object = MibTableRow
staLcrstProCols = _StaLcrstProCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22, 6, 1)
)
staLcrstProCols.setIndexNames(
    (0, "ELSA-MIB", "staLcrstProPro"),
)
if mibBuilder.loadTexts:
    staLcrstProCols.setStatus("mandatory")
_StaLcrstProPro_Type = DisplayString
_StaLcrstProPro_Object = MibTableColumn
staLcrstProPro = _StaLcrstProPro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22, 6, 1, 1),
    _StaLcrstProPro_Type()
)
staLcrstProPro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLcrstProPro.setStatus("mandatory")
_StaLcrstProFai_Type = Integer32
_StaLcrstProFai_Object = MibTableColumn
staLcrstProFai = _StaLcrstProFai_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22, 6, 1, 2),
    _StaLcrstProFai_Type()
)
staLcrstProFai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLcrstProFai.setStatus("mandatory")
_StaLcrstProSuc_Type = Integer32
_StaLcrstProSuc_Object = MibTableColumn
staLcrstProSuc = _StaLcrstProSuc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22, 6, 1, 3),
    _StaLcrstProSuc_Type()
)
staLcrstProSuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLcrstProSuc.setStatus("mandatory")
_StaLcrstDel_Type = Integer32
_StaLcrstDel_Object = MibScalar
staLcrstDel = _StaLcrstDel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 22, 7),
    _StaLcrstDel_Type()
)
staLcrstDel.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staLcrstDel.setStatus("mandatory")
_StaS0bus_ObjectIdentity = ObjectIdentity
staS0bus = _StaS0bus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23)
)
_StaS0busDin_Object = MibTable
staS0busDin = _StaS0busDin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 1)
)
if mibBuilder.loadTexts:
    staS0busDin.setStatus("mandatory")
_StaS0busDinCols_Object = MibTableRow
staS0busDinCols = _StaS0busDinCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 1, 1)
)
staS0busDinCols.setIndexNames(
    (0, "ELSA-MIB", "staS0busDinCha"),
)
if mibBuilder.loadTexts:
    staS0busDinCols.setStatus("mandatory")


class _StaS0busDinCha_Type(Integer32):
    """Custom type staS0busDinCha based on Integer32"""
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
        *(("s0-1", 1),
          ("s0-2", 2),
          ("s0-3", 3),
          ("s0-4", 4))
    )


_StaS0busDinCha_Type.__name__ = "Integer32"
_StaS0busDinCha_Object = MibTableColumn
staS0busDinCha = _StaS0busDinCha_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 1, 1, 1),
    _StaS0busDinCha_Type()
)
staS0busDinCha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staS0busDinCha.setStatus("mandatory")


class _StaS0busDinPro_Type(Integer32):
    """Custom type staS0busDinPro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 255),
          ("dss1", 1),
          ("p2p-dss1", 4),
          ("tr1-6", 2))
    )


_StaS0busDinPro_Type.__name__ = "Integer32"
_StaS0busDinPro_Object = MibTableColumn
staS0busDinPro = _StaS0busDinPro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 1, 1, 2),
    _StaS0busDinPro_Type()
)
staS0busDinPro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staS0busDinPro.setStatus("mandatory")


class _StaS0busDinLay_Type(Integer32):
    """Custom type staS0busDinLay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_StaS0busDinLay_Type.__name__ = "Integer32"
_StaS0busDinLay_Object = MibTableColumn
staS0busDinLay = _StaS0busDinLay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 1, 1, 3),
    _StaS0busDinLay_Type()
)
staS0busDinLay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staS0busDinLay.setStatus("mandatory")


class _StaS0busDinTei_Type(Integer32):
    """Custom type staS0busDinTei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_StaS0busDinTei_Type.__name__ = "Integer32"
_StaS0busDinTei_Object = MibTableColumn
staS0busDinTei = _StaS0busDinTei_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 1, 1, 4),
    _StaS0busDinTei_Type()
)
staS0busDinTei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staS0busDinTei.setStatus("mandatory")


class _StaS0busDinS0a_Type(Integer32):
    """Custom type staS0busDinS0a based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_StaS0busDinS0a_Type.__name__ = "Integer32"
_StaS0busDinS0a_Object = MibTableColumn
staS0busDinS0a = _StaS0busDinS0a_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 1, 1, 5),
    _StaS0busDinS0a_Type()
)
staS0busDinS0a.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staS0busDinS0a.setStatus("mandatory")
_StaS0busD2s_Object = MibTable
staS0busD2s = _StaS0busD2s_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 3)
)
if mibBuilder.loadTexts:
    staS0busD2s.setStatus("mandatory")
_StaS0busD2sCols_Object = MibTableRow
staS0busD2sCols = _StaS0busD2sCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 3, 1)
)
staS0busD2sCols.setIndexNames(
    (0, "ELSA-MIB", "staS0busD2sCha"),
)
if mibBuilder.loadTexts:
    staS0busD2sCols.setStatus("mandatory")


class _StaS0busD2sCha_Type(Integer32):
    """Custom type staS0busD2sCha based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("s0-1", 2),
          ("s0-2", 4),
          ("s0-3", 6),
          ("s0-4", 8))
    )


_StaS0busD2sCha_Type.__name__ = "Integer32"
_StaS0busD2sCha_Object = MibTableColumn
staS0busD2sCha = _StaS0busD2sCha_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 3, 1, 1),
    _StaS0busD2sCha_Type()
)
staS0busD2sCha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staS0busD2sCha.setStatus("mandatory")


class _StaS0busD2sTei_Type(Integer32):
    """Custom type staS0busD2sTei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            128
        )
    )
    namedValues = NamedValues(
        ("none", 128)
    )


_StaS0busD2sTei_Type.__name__ = "Integer32"
_StaS0busD2sTei_Object = MibTableColumn
staS0busD2sTei = _StaS0busD2sTei_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 3, 1, 2),
    _StaS0busD2sTei_Type()
)
staS0busD2sTei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staS0busD2sTei.setStatus("mandatory")


class _StaS0busD2sL2a_Type(Integer32):
    """Custom type staS0busD2sL2a based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_StaS0busD2sL2a_Type.__name__ = "Integer32"
_StaS0busD2sL2a_Object = MibTableColumn
staS0busD2sL2a = _StaS0busD2sL2a_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 3, 1, 3),
    _StaS0busD2sL2a_Type()
)
staS0busD2sL2a.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staS0busD2sL2a.setStatus("mandatory")
_StaS0busD2sCon_Type = Integer32
_StaS0busD2sCon_Object = MibTableColumn
staS0busD2sCon = _StaS0busD2sCon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 23, 3, 1, 4),
    _StaS0busD2sCon_Type()
)
staS0busD2sCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staS0busD2sCon.setStatus("mandatory")
_StaCharg_ObjectIdentity = ObjectIdentity
staCharg = _StaCharg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24)
)
_StaChargSparemi_Type = Integer32
_StaChargSparemi_Object = MibScalar
staChargSparemi = _StaChargSparemi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 1),
    _StaChargSparemi_Type()
)
staChargSparemi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargSparemi.setStatus("mandatory")
_StaChargTimetab_Object = MibTable
staChargTimetab = _StaChargTimetab_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 2)
)
if mibBuilder.loadTexts:
    staChargTimetab.setStatus("mandatory")
_StaChargTimetabCols_Object = MibTableRow
staChargTimetabCols = _StaChargTimetabCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 2, 1)
)
staChargTimetabCols.setIndexNames(
    (0, "ELSA-MIB", "staChargTimetabIfc"),
)
if mibBuilder.loadTexts:
    staChargTimetabCols.setStatus("mandatory")


class _StaChargTimetabIfc_Type(Integer32):
    """Custom type staChargTimetabIfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ab-1", 3),
          ("ab-2", 4),
          ("ab-3", 5),
          ("ab-4", 6),
          ("lancapi", 2),
          ("router", 1),
          ("time-Modul", 255))
    )


_StaChargTimetabIfc_Type.__name__ = "Integer32"
_StaChargTimetabIfc_Object = MibTableColumn
staChargTimetabIfc = _StaChargTimetabIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 2, 1, 1),
    _StaChargTimetabIfc_Type()
)
staChargTimetabIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargTimetabIfc.setStatus("mandatory")
_StaChargTimetabBudgetmi_Type = Integer32
_StaChargTimetabBudgetmi_Object = MibTableColumn
staChargTimetabBudgetmi = _StaChargTimetabBudgetmi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 2, 1, 2),
    _StaChargTimetabBudgetmi_Type()
)
staChargTimetabBudgetmi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargTimetabBudgetmi.setStatus("mandatory")
_StaChargTimetabSparemin_Type = Integer32
_StaChargTimetabSparemin_Object = MibTableColumn
staChargTimetabSparemin = _StaChargTimetabSparemin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 2, 1, 3),
    _StaChargTimetabSparemin_Type()
)
staChargTimetabSparemin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargTimetabSparemin.setStatus("mandatory")
_StaChargTimetabMinutesa_Type = Integer32
_StaChargTimetabMinutesa_Object = MibTableColumn
staChargTimetabMinutesa = _StaChargTimetabMinutesa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 2, 1, 4),
    _StaChargTimetabMinutesa_Type()
)
staChargTimetabMinutesa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargTimetabMinutesa.setStatus("mandatory")
_StaChargTimetabMinutesp_Type = Integer32
_StaChargTimetabMinutesp_Object = MibTableColumn
staChargTimetabMinutesp = _StaChargTimetabMinutesp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 2, 1, 5),
    _StaChargTimetabMinutesp_Type()
)
staChargTimetabMinutesp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargTimetabMinutesp.setStatus("mandatory")
_StaChargDeletev_Type = Integer32
_StaChargDeletev_Object = MibScalar
staChargDeletev = _StaChargDeletev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 3),
    _StaChargDeletev_Type()
)
staChargDeletev.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    staChargDeletev.setStatus("mandatory")
_StaChargSpareun_Type = Integer32
_StaChargSpareun_Object = MibScalar
staChargSpareun = _StaChargSpareun_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 4),
    _StaChargSpareun_Type()
)
staChargSpareun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargSpareun.setStatus("mandatory")
_StaChargTablebu_Object = MibTable
staChargTablebu = _StaChargTablebu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 5)
)
if mibBuilder.loadTexts:
    staChargTablebu.setStatus("mandatory")
_StaChargTablebuCols_Object = MibTableRow
staChargTablebuCols = _StaChargTablebuCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 5, 1)
)
staChargTablebuCols.setIndexNames(
    (0, "ELSA-MIB", "staChargTablebuIfc"),
)
if mibBuilder.loadTexts:
    staChargTablebuCols.setStatus("mandatory")


class _StaChargTablebuIfc_Type(Integer32):
    """Custom type staChargTablebuIfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ab-1", 3),
          ("ab-2", 4),
          ("ab-3", 5),
          ("ab-4", 6),
          ("lancapi", 2),
          ("router", 1),
          ("time-modul", 255))
    )


_StaChargTablebuIfc_Type.__name__ = "Integer32"
_StaChargTablebuIfc_Object = MibTableColumn
staChargTablebuIfc = _StaChargTablebuIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 5, 1, 1),
    _StaChargTablebuIfc_Type()
)
staChargTablebuIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargTablebuIfc.setStatus("mandatory")
_StaChargTablebuBud_Type = Integer32
_StaChargTablebuBud_Object = MibTableColumn
staChargTablebuBud = _StaChargTablebuBud_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 5, 1, 2),
    _StaChargTablebuBud_Type()
)
staChargTablebuBud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargTablebuBud.setStatus("mandatory")
_StaChargTablebuSpa_Type = Integer32
_StaChargTablebuSpa_Object = MibTableColumn
staChargTablebuSpa = _StaChargTablebuSpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 5, 1, 3),
    _StaChargTablebuSpa_Type()
)
staChargTablebuSpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargTablebuSpa.setStatus("mandatory")
_StaChargTablebuTot_Type = Integer32
_StaChargTablebuTot_Object = MibTableColumn
staChargTablebuTot = _StaChargTablebuTot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 5, 1, 4),
    _StaChargTablebuTot_Type()
)
staChargTablebuTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargTablebuTot.setStatus("mandatory")
_StaChargSpareda_Type = Integer32
_StaChargSpareda_Object = MibScalar
staChargSpareda = _StaChargSpareda_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 6),
    _StaChargSpareda_Type()
)
staChargSpareda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargSpareda.setStatus("mandatory")
_StaChargRouteru_Type = Integer32
_StaChargRouteru_Object = MibScalar
staChargRouteru = _StaChargRouteru_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 7),
    _StaChargRouteru_Type()
)
staChargRouteru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargRouteru.setStatus("mandatory")
_StaChargTotalun_Type = Integer32
_StaChargTotalun_Object = MibScalar
staChargTotalun = _StaChargTotalun_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 8),
    _StaChargTotalun_Type()
)
staChargTotalun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargTotalun.setStatus("mandatory")
_StaChargRouterm_Type = Integer32
_StaChargRouterm_Object = MibScalar
staChargRouterm = _StaChargRouterm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 24, 9),
    _StaChargRouterm_Type()
)
staChargRouterm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staChargRouterm.setStatus("mandatory")
_StaDhcpc_ObjectIdentity = ObjectIdentity
staDhcpc = _StaDhcpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32)
)


class _StaDhcpcState_Type(Integer32):
    """Custom type staDhcpcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("bound", 7),
          ("idle", 0),
          ("init", 3),
          ("init-reboot", 1),
          ("rebinding", 9),
          ("rebooting", 2),
          ("renewing", 8),
          ("request", 5),
          ("selecting", 4),
          ("wait-arp-request", 6))
    )


_StaDhcpcState_Type.__name__ = "Integer32"
_StaDhcpcState_Object = MibScalar
staDhcpcState = _StaDhcpcState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 1),
    _StaDhcpcState_Type()
)
staDhcpcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcState.setStatus("mandatory")
_StaDhcpcLeaseti_Type = Integer32
_StaDhcpcLeaseti_Object = MibScalar
staDhcpcLeaseti = _StaDhcpcLeaseti_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 2),
    _StaDhcpcLeaseti_Type()
)
staDhcpcLeaseti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcLeaseti.setStatus("mandatory")
_StaDhcpcYouripa_Type = IpAddress
_StaDhcpcYouripa_Object = MibScalar
staDhcpcYouripa = _StaDhcpcYouripa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 3),
    _StaDhcpcYouripa_Type()
)
staDhcpcYouripa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcYouripa.setStatus("mandatory")
_StaDhcpcYouripn_Type = IpAddress
_StaDhcpcYouripn_Object = MibScalar
staDhcpcYouripn = _StaDhcpcYouripn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 4),
    _StaDhcpcYouripn_Type()
)
staDhcpcYouripn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcYouripn.setStatus("mandatory")
_StaDhcpcGateway_Type = IpAddress
_StaDhcpcGateway_Object = MibScalar
staDhcpcGateway = _StaDhcpcGateway_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 5),
    _StaDhcpcGateway_Type()
)
staDhcpcGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcGateway.setStatus("mandatory")
_StaDhcpcServeri_Type = IpAddress
_StaDhcpcServeri_Object = MibScalar
staDhcpcServeri = _StaDhcpcServeri_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 6),
    _StaDhcpcServeri_Type()
)
staDhcpcServeri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcServeri.setStatus("mandatory")
_StaDhcpcSecurit_Type = IpAddress
_StaDhcpcSecurit_Object = MibScalar
staDhcpcSecurit = _StaDhcpcSecurit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 7),
    _StaDhcpcSecurit_Type()
)
staDhcpcSecurit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcSecurit.setStatus("mandatory")
_StaDhcpcTimeoff_Type = Integer32
_StaDhcpcTimeoff_Object = MibScalar
staDhcpcTimeoff = _StaDhcpcTimeoff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 8),
    _StaDhcpcTimeoff_Type()
)
staDhcpcTimeoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcTimeoff.setStatus("mandatory")
_StaDhcpcTimeser_Type = IpAddress
_StaDhcpcTimeser_Object = MibScalar
staDhcpcTimeser = _StaDhcpcTimeser_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 9),
    _StaDhcpcTimeser_Type()
)
staDhcpcTimeser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcTimeser.setStatus("mandatory")
_StaDhcpcTableti_Object = MibTable
staDhcpcTableti = _StaDhcpcTableti_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 10)
)
if mibBuilder.loadTexts:
    staDhcpcTableti.setStatus("mandatory")
_StaDhcpcTabletiCols_Object = MibTableRow
staDhcpcTabletiCols = _StaDhcpcTabletiCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 10, 1)
)
staDhcpcTabletiCols.setIndexNames(
    (0, "ELSA-MIB", "staDhcpcTabletiIpa"),
)
if mibBuilder.loadTexts:
    staDhcpcTabletiCols.setStatus("mandatory")
_StaDhcpcTabletiIpa_Type = IpAddress
_StaDhcpcTabletiIpa_Object = MibTableColumn
staDhcpcTabletiIpa = _StaDhcpcTabletiIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 10, 1, 1),
    _StaDhcpcTabletiIpa_Type()
)
staDhcpcTabletiIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcTabletiIpa.setStatus("mandatory")
_StaDhcpcTablero_Object = MibTable
staDhcpcTablero = _StaDhcpcTablero_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 11)
)
if mibBuilder.loadTexts:
    staDhcpcTablero.setStatus("mandatory")
_StaDhcpcTableroCols_Object = MibTableRow
staDhcpcTableroCols = _StaDhcpcTableroCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 11, 1)
)
staDhcpcTableroCols.setIndexNames(
    (0, "ELSA-MIB", "staDhcpcTableroIpa"),
)
if mibBuilder.loadTexts:
    staDhcpcTableroCols.setStatus("mandatory")
_StaDhcpcTableroIpa_Type = IpAddress
_StaDhcpcTableroIpa_Object = MibTableColumn
staDhcpcTableroIpa = _StaDhcpcTableroIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 11, 1, 1),
    _StaDhcpcTableroIpa_Type()
)
staDhcpcTableroIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcTableroIpa.setStatus("mandatory")
_StaDhcpcTablena_Object = MibTable
staDhcpcTablena = _StaDhcpcTablena_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 12)
)
if mibBuilder.loadTexts:
    staDhcpcTablena.setStatus("mandatory")
_StaDhcpcTablenaCols_Object = MibTableRow
staDhcpcTablenaCols = _StaDhcpcTablenaCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 12, 1)
)
staDhcpcTablenaCols.setIndexNames(
    (0, "ELSA-MIB", "staDhcpcTablenaIpa"),
)
if mibBuilder.loadTexts:
    staDhcpcTablenaCols.setStatus("mandatory")
_StaDhcpcTablenaIpa_Type = IpAddress
_StaDhcpcTablenaIpa_Object = MibTableColumn
staDhcpcTablenaIpa = _StaDhcpcTablenaIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 12, 1, 1),
    _StaDhcpcTablenaIpa_Type()
)
staDhcpcTablenaIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcTablenaIpa.setStatus("mandatory")
_StaDhcpcTabledo_Object = MibTable
staDhcpcTabledo = _StaDhcpcTabledo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 13)
)
if mibBuilder.loadTexts:
    staDhcpcTabledo.setStatus("mandatory")
_StaDhcpcTabledoCols_Object = MibTableRow
staDhcpcTabledoCols = _StaDhcpcTabledoCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 13, 1)
)
staDhcpcTabledoCols.setIndexNames(
    (0, "ELSA-MIB", "staDhcpcTabledoIpa"),
)
if mibBuilder.loadTexts:
    staDhcpcTabledoCols.setStatus("mandatory")
_StaDhcpcTabledoIpa_Type = IpAddress
_StaDhcpcTabledoIpa_Object = MibTableColumn
staDhcpcTabledoIpa = _StaDhcpcTabledoIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 13, 1, 1),
    _StaDhcpcTabledoIpa_Type()
)
staDhcpcTabledoIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcTabledoIpa.setStatus("mandatory")
_StaDhcpcTablelo_Object = MibTable
staDhcpcTablelo = _StaDhcpcTablelo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 14)
)
if mibBuilder.loadTexts:
    staDhcpcTablelo.setStatus("mandatory")
_StaDhcpcTableloCols_Object = MibTableRow
staDhcpcTableloCols = _StaDhcpcTableloCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 14, 1)
)
staDhcpcTableloCols.setIndexNames(
    (0, "ELSA-MIB", "staDhcpcTableloIpa"),
)
if mibBuilder.loadTexts:
    staDhcpcTableloCols.setStatus("mandatory")
_StaDhcpcTableloIpa_Type = IpAddress
_StaDhcpcTableloIpa_Object = MibTableColumn
staDhcpcTableloIpa = _StaDhcpcTableloIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 14, 1, 1),
    _StaDhcpcTableloIpa_Type()
)
staDhcpcTableloIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcTableloIpa.setStatus("mandatory")
_StaDhcpcConfigu_Type = DisplayString
_StaDhcpcConfigu_Object = MibScalar
staDhcpcConfigu = _StaDhcpcConfigu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 1, 32, 15),
    _StaDhcpcConfigu_Type()
)
staDhcpcConfigu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDhcpcConfigu.setStatus("mandatory")
_Set_ObjectIdentity = ObjectIdentity
set = _Set_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2)
)


class _SetName_Type(DisplayString):
    """Custom type setName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SetName_Type.__name__ = "DisplayString"
_SetName_Object = MibScalar
setName = _SetName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 1),
    _SetName_Type()
)
setName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setName.setStatus("mandatory")
_SetWanm_ObjectIdentity = ObjectIdentity
setWanm = _SetWanm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2)
)
_SetWanmName_Object = MibTable
setWanmName = _SetWanmName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 2)
)
if mibBuilder.loadTexts:
    setWanmName.setStatus("mandatory")
_SetWanmNameCols_Object = MibTableRow
setWanmNameCols = _SetWanmNameCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 2, 1)
)
setWanmNameCols.setIndexNames(
    (0, "ELSA-MIB", "setWanmNameDev"),
)
if mibBuilder.loadTexts:
    setWanmNameCols.setStatus("mandatory")
_SetWanmNameDev_Type = DisplayString
_SetWanmNameDev_Object = MibTableColumn
setWanmNameDev = _SetWanmNameDev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 2, 1, 1),
    _SetWanmNameDev_Type()
)
setWanmNameDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmNameDev.setStatus("mandatory")
_SetWanmNameDia_Type = DisplayString
_SetWanmNameDia_Object = MibTableColumn
setWanmNameDia = _SetWanmNameDia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 2, 1, 2),
    _SetWanmNameDia_Type()
)
setWanmNameDia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmNameDia.setStatus("mandatory")
_SetWanmNameB1d_Type = Integer32
_SetWanmNameB1d_Object = MibTableColumn
setWanmNameB1d = _SetWanmNameB1d_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 2, 1, 3),
    _SetWanmNameB1d_Type()
)
setWanmNameB1d.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmNameB1d.setStatus("mandatory")
_SetWanmNameB2d_Type = Integer32
_SetWanmNameB2d_Object = MibTableColumn
setWanmNameB2d = _SetWanmNameB2d_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 2, 1, 4),
    _SetWanmNameB2d_Type()
)
setWanmNameB2d.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmNameB2d.setStatus("mandatory")
_SetWanmNameWan_Type = DisplayString
_SetWanmNameWan_Object = MibTableColumn
setWanmNameWan = _SetWanmNameWan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 2, 1, 5),
    _SetWanmNameWan_Type()
)
setWanmNameWan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmNameWan.setStatus("mandatory")


class _SetWanmNameCal_Type(Integer32):
    """Custom type setWanmNameCal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("elsa", 9),
          ("looser", 2),
          ("name", 5),
          ("off", 0))
    )


_SetWanmNameCal_Type.__name__ = "Integer32"
_SetWanmNameCal_Object = MibTableColumn
setWanmNameCal = _SetWanmNameCal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 2, 1, 6),
    _SetWanmNameCal_Type()
)
setWanmNameCal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmNameCal.setStatus("mandatory")
_SetWanmRoun_Object = MibTable
setWanmRoun = _SetWanmRoun_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 3)
)
if mibBuilder.loadTexts:
    setWanmRoun.setStatus("mandatory")
_SetWanmRounCols_Object = MibTableRow
setWanmRounCols = _SetWanmRounCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 3, 1)
)
setWanmRounCols.setIndexNames(
    (0, "ELSA-MIB", "setWanmRounDev"),
)
if mibBuilder.loadTexts:
    setWanmRounCols.setStatus("mandatory")
_SetWanmRounDev_Type = DisplayString
_SetWanmRounDev_Object = MibTableColumn
setWanmRounDev = _SetWanmRounDev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 3, 1, 1),
    _SetWanmRounDev_Type()
)
setWanmRounDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmRounDev.setStatus("mandatory")
_SetWanmRounRou_Type = DisplayString
_SetWanmRounRou_Object = MibTableColumn
setWanmRounRou = _SetWanmRounRou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 3, 1, 2),
    _SetWanmRounRou_Type()
)
setWanmRounRou.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmRounRou.setStatus("mandatory")


class _SetWanmRounHea_Type(Integer32):
    """Custom type setWanmRounHea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("last", 0))
    )


_SetWanmRounHea_Type.__name__ = "Integer32"
_SetWanmRounHea_Object = MibTableColumn
setWanmRounHea = _SetWanmRounHea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 3, 1, 3),
    _SetWanmRounHea_Type()
)
setWanmRounHea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmRounHea.setStatus("mandatory")
_SetWanmLaye_Object = MibTable
setWanmLaye = _SetWanmLaye_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 4)
)
if mibBuilder.loadTexts:
    setWanmLaye.setStatus("mandatory")
_SetWanmLayeCols_Object = MibTableRow
setWanmLayeCols = _SetWanmLayeCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 4, 1)
)
setWanmLayeCols.setIndexNames(
    (0, "ELSA-MIB", "setWanmLayeWanl"),
)
if mibBuilder.loadTexts:
    setWanmLayeCols.setStatus("mandatory")
_SetWanmLayeWanl_Type = DisplayString
_SetWanmLayeWanl_Object = MibTableColumn
setWanmLayeWanl = _SetWanmLayeWanl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 4, 1, 1),
    _SetWanmLayeWanl_Type()
)
setWanmLayeWanl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmLayeWanl.setStatus("mandatory")


class _SetWanmLayeEnca_Type(Integer32):
    """Custom type setWanmLayeEnca based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ether", 0),
          ("trans", 255))
    )


_SetWanmLayeEnca_Type.__name__ = "Integer32"
_SetWanmLayeEnca_Object = MibTableColumn
setWanmLayeEnca = _SetWanmLayeEnca_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 4, 1, 2),
    _SetWanmLayeEnca_Type()
)
setWanmLayeEnca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmLayeEnca.setStatus("mandatory")


class _SetWanmLayeLay3_Type(Integer32):
    """Custom type setWanmLayeLay3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("appp", 5),
          ("elsa", 0),
          ("ppp", 4),
          ("scappp", 7),
          ("scppp", 6),
          ("sctrans", 8),
          ("trans", 255))
    )


_SetWanmLayeLay3_Type.__name__ = "Integer32"
_SetWanmLayeLay3_Object = MibTableColumn
setWanmLayeLay3 = _SetWanmLayeLay3_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 4, 1, 3),
    _SetWanmLayeLay3_Type()
)
setWanmLayeLay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmLayeLay3.setStatus("mandatory")


class _SetWanmLayeLay2_Type(Integer32):
    """Custom type setWanmLayeLay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trans", 1),
          ("x75lapb", 0))
    )


_SetWanmLayeLay2_Type.__name__ = "Integer32"
_SetWanmLayeLay2_Object = MibTableColumn
setWanmLayeLay2 = _SetWanmLayeLay2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 4, 1, 4),
    _SetWanmLayeLay2_Type()
)
setWanmLayeLay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmLayeLay2.setStatus("mandatory")


class _SetWanmLayeL2op_Type(Integer32):
    """Custom type setWanmLayeL2op based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bnd-and-cmpr", 2),
          ("bundle", 1),
          ("compr", 0),
          ("none", 255))
    )


_SetWanmLayeL2op_Type.__name__ = "Integer32"
_SetWanmLayeL2op_Object = MibTableColumn
setWanmLayeL2op = _SetWanmLayeL2op_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 4, 1, 5),
    _SetWanmLayeL2op_Type()
)
setWanmLayeL2op.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmLayeL2op.setStatus("mandatory")


class _SetWanmLayeLay1_Type(Integer32):
    """Custom type setWanmLayeLay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              67,
              131)
        )
    )
    namedValues = NamedValues(
        *(("hdlc56k", 1),
          ("hdlc64k", 0),
          ("v110-19k2", 67),
          ("v110-38k4", 131),
          ("v110-9k6", 3))
    )


_SetWanmLayeLay1_Type.__name__ = "Integer32"
_SetWanmLayeLay1_Object = MibTableColumn
setWanmLayeLay1 = _SetWanmLayeLay1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 4, 1, 6),
    _SetWanmLayeLay1_Type()
)
setWanmLayeLay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmLayeLay1.setStatus("mandatory")
_SetWanmPppl_Object = MibTable
setWanmPppl = _SetWanmPppl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5)
)
if mibBuilder.loadTexts:
    setWanmPppl.setStatus("mandatory")
_SetWanmPpplCols_Object = MibTableRow
setWanmPpplCols = _SetWanmPpplCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5, 1)
)
setWanmPpplCols.setIndexNames(
    (0, "ELSA-MIB", "setWanmPpplDev"),
)
if mibBuilder.loadTexts:
    setWanmPpplCols.setStatus("mandatory")
_SetWanmPpplDev_Type = DisplayString
_SetWanmPpplDev_Object = MibTableColumn
setWanmPpplDev = _SetWanmPpplDev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5, 1, 1),
    _SetWanmPpplDev_Type()
)
setWanmPpplDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmPpplDev.setStatus("mandatory")


class _SetWanmPpplAut_Type(Integer32):
    """Custom type setWanmPpplAut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("chap", 8),
          ("none", 0),
          ("pap", 4))
    )


_SetWanmPpplAut_Type.__name__ = "Integer32"
_SetWanmPpplAut_Object = MibTableColumn
setWanmPpplAut = _SetWanmPpplAut_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5, 1, 2),
    _SetWanmPpplAut_Type()
)
setWanmPpplAut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmPpplAut.setStatus("mandatory")
_SetWanmPpplKey_Type = DisplayString
_SetWanmPpplKey_Object = MibTableColumn
setWanmPpplKey = _SetWanmPpplKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5, 1, 3),
    _SetWanmPpplKey_Type()
)
setWanmPpplKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmPpplKey.setStatus("mandatory")
_SetWanmPpplTim_Type = Integer32
_SetWanmPpplTim_Object = MibTableColumn
setWanmPpplTim = _SetWanmPpplTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5, 1, 4),
    _SetWanmPpplTim_Type()
)
setWanmPpplTim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmPpplTim.setStatus("mandatory")
_SetWanmPpplTry_Type = Integer32
_SetWanmPpplTry_Object = MibTableColumn
setWanmPpplTry = _SetWanmPpplTry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5, 1, 5),
    _SetWanmPpplTry_Type()
)
setWanmPpplTry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmPpplTry.setStatus("mandatory")
_SetWanmPpplUse_Type = DisplayString
_SetWanmPpplUse_Object = MibTableColumn
setWanmPpplUse = _SetWanmPpplUse_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5, 1, 6),
    _SetWanmPpplUse_Type()
)
setWanmPpplUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmPpplUse.setStatus("mandatory")
_SetWanmPpplCon_Type = Integer32
_SetWanmPpplCon_Object = MibTableColumn
setWanmPpplCon = _SetWanmPpplCon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5, 1, 7),
    _SetWanmPpplCon_Type()
)
setWanmPpplCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmPpplCon.setStatus("mandatory")
_SetWanmPpplFai_Type = Integer32
_SetWanmPpplFai_Object = MibTableColumn
setWanmPpplFai = _SetWanmPpplFai_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5, 1, 8),
    _SetWanmPpplFai_Type()
)
setWanmPpplFai.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmPpplFai.setStatus("mandatory")
_SetWanmPpplTer_Type = Integer32
_SetWanmPpplTer_Object = MibTableColumn
setWanmPpplTer = _SetWanmPpplTer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 5, 1, 9),
    _SetWanmPpplTer_Type()
)
setWanmPpplTer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmPpplTer.setStatus("mandatory")
_SetWanmNumb_Object = MibTable
setWanmNumb = _SetWanmNumb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 6)
)
if mibBuilder.loadTexts:
    setWanmNumb.setStatus("mandatory")
_SetWanmNumbCols_Object = MibTableRow
setWanmNumbCols = _SetWanmNumbCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 6, 1)
)
setWanmNumbCols.setIndexNames(
    (0, "ELSA-MIB", "setWanmNumbDia"),
)
if mibBuilder.loadTexts:
    setWanmNumbCols.setStatus("mandatory")
_SetWanmNumbDia_Type = DisplayString
_SetWanmNumbDia_Object = MibTableColumn
setWanmNumbDia = _SetWanmNumbDia_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 6, 1, 1),
    _SetWanmNumbDia_Type()
)
setWanmNumbDia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmNumbDia.setStatus("mandatory")
_SetWanmNumbDev_Type = DisplayString
_SetWanmNumbDev_Object = MibTableColumn
setWanmNumbDev = _SetWanmNumbDev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 6, 1, 2),
    _SetWanmNumbDev_Type()
)
setWanmNumbDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmNumbDev.setStatus("mandatory")


class _SetWanmDial_Type(DisplayString):
    """Custom type setWanmDial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SetWanmDial_Type.__name__ = "DisplayString"
_SetWanmDial_Object = MibScalar
setWanmDial = _SetWanmDial_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 7),
    _SetWanmDial_Type()
)
setWanmDial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setWanmDial.setStatus("mandatory")
_SetWanmScri_Object = MibTable
setWanmScri = _SetWanmScri_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 8)
)
if mibBuilder.loadTexts:
    setWanmScri.setStatus("mandatory")
_SetWanmScriCols_Object = MibTableRow
setWanmScriCols = _SetWanmScriCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 8, 1)
)
setWanmScriCols.setIndexNames(
    (0, "ELSA-MIB", "setWanmScriDev"),
)
if mibBuilder.loadTexts:
    setWanmScriCols.setStatus("mandatory")
_SetWanmScriDev_Type = DisplayString
_SetWanmScriDev_Object = MibTableColumn
setWanmScriDev = _SetWanmScriDev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 8, 1, 1),
    _SetWanmScriDev_Type()
)
setWanmScriDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmScriDev.setStatus("mandatory")
_SetWanmScriScr_Type = DisplayString
_SetWanmScriScr_Object = MibTableColumn
setWanmScriScr = _SetWanmScriScr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 8, 1, 2),
    _SetWanmScriScr_Type()
)
setWanmScriScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmScriScr.setStatus("mandatory")


class _SetWanmProt_Type(Integer32):
    """Custom type setWanmProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("name", 1),
          ("noname", 3),
          ("none", 0),
          ("number", 2))
    )


_SetWanmProt_Type.__name__ = "Integer32"
_SetWanmProt_Object = MibScalar
setWanmProt = _SetWanmProt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 9),
    _SetWanmProt_Type()
)
setWanmProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmProt.setStatus("mandatory")
_SetWanmCbat_Type = Integer32
_SetWanmCbat_Object = MibScalar
setWanmCbat = _SetWanmCbat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 10),
    _SetWanmCbat_Type()
)
setWanmCbat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmCbat.setStatus("mandatory")
_SetWanmRout_Object = MibTable
setWanmRout = _SetWanmRout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 11)
)
if mibBuilder.loadTexts:
    setWanmRout.setStatus("mandatory")
_SetWanmRoutCols_Object = MibTableRow
setWanmRoutCols = _SetWanmRoutCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 11, 1)
)
setWanmRoutCols.setIndexNames(
    (0, "ELSA-MIB", "setWanmRoutIfc"),
)
if mibBuilder.loadTexts:
    setWanmRoutCols.setStatus("mandatory")


class _SetWanmRoutIfc_Type(Integer32):
    """Custom type setWanmRoutIfc based on Integer32"""
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
        *(("s0-1", 1),
          ("s0-2", 2),
          ("s0-3", 3),
          ("s0-4", 4))
    )


_SetWanmRoutIfc_Type.__name__ = "Integer32"
_SetWanmRoutIfc_Object = MibTableColumn
setWanmRoutIfc = _SetWanmRoutIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 11, 1, 1),
    _SetWanmRoutIfc_Type()
)
setWanmRoutIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setWanmRoutIfc.setStatus("mandatory")
_SetWanmRoutMsn_Type = DisplayString
_SetWanmRoutMsn_Object = MibTableColumn
setWanmRoutMsn = _SetWanmRoutMsn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 11, 1, 2),
    _SetWanmRoutMsn_Type()
)
setWanmRoutMsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmRoutMsn.setStatus("mandatory")


class _SetWanmRoutCli_Type(Integer32):
    """Custom type setWanmRoutCli based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_SetWanmRoutCli_Type.__name__ = "Integer32"
_SetWanmRoutCli_Object = MibTableColumn
setWanmRoutCli = _SetWanmRoutCli_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 11, 1, 3),
    _SetWanmRoutCli_Type()
)
setWanmRoutCli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmRoutCli.setStatus("mandatory")


class _SetWanmRoutYc_Type(Integer32):
    """Custom type setWanmRoutYc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_SetWanmRoutYc_Type.__name__ = "Integer32"
_SetWanmRoutYc_Object = MibTableColumn
setWanmRoutYc = _SetWanmRoutYc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 11, 1, 8),
    _SetWanmRoutYc_Type()
)
setWanmRoutYc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmRoutYc.setStatus("mandatory")
_SetWanmManu_ObjectIdentity = ObjectIdentity
setWanmManu = _SetWanmManu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 13)
)
_SetWanmManuCon_Type = Integer32
_SetWanmManuCon_Object = MibScalar
setWanmManuCon = _SetWanmManuCon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 13, 1),
    _SetWanmManuCon_Type()
)
setWanmManuCon.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    setWanmManuCon.setStatus("mandatory")
_SetWanmManuDis_Type = Integer32
_SetWanmManuDis_Object = MibScalar
setWanmManuDis = _SetWanmManuDis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 13, 2),
    _SetWanmManuDis_Type()
)
setWanmManuDis.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    setWanmManuDis.setStatus("mandatory")
_SetWanmInte_Object = MibTable
setWanmInte = _SetWanmInte_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 14)
)
if mibBuilder.loadTexts:
    setWanmInte.setStatus("mandatory")
_SetWanmInteCols_Object = MibTableRow
setWanmInteCols = _SetWanmInteCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 14, 1)
)
setWanmInteCols.setIndexNames(
    (0, "ELSA-MIB", "setWanmInteIfc"),
)
if mibBuilder.loadTexts:
    setWanmInteCols.setStatus("mandatory")


class _SetWanmInteIfc_Type(Integer32):
    """Custom type setWanmInteIfc based on Integer32"""
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
        *(("s0-1", 1),
          ("s0-2", 2),
          ("s0-3", 3),
          ("s0-4", 4))
    )


_SetWanmInteIfc_Type.__name__ = "Integer32"
_SetWanmInteIfc_Object = MibTableColumn
setWanmInteIfc = _SetWanmInteIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 14, 1, 1),
    _SetWanmInteIfc_Type()
)
setWanmInteIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setWanmInteIfc.setStatus("mandatory")


class _SetWanmInteProt_Type(Integer32):
    """Custom type setWanmInteProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 255),
          ("dss1", 1),
          ("ltr6", 2),
          ("p2p-dss1", 4))
    )


_SetWanmInteProt_Type.__name__ = "Integer32"
_SetWanmInteProt_Object = MibTableColumn
setWanmInteProt = _SetWanmInteProt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 14, 1, 2),
    _SetWanmInteProt_Type()
)
setWanmInteProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmInteProt.setStatus("mandatory")


class _SetWanmInteLlmo_Type(Integer32):
    """Custom type setWanmInteLlmo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_SetWanmInteLlmo_Type.__name__ = "Integer32"
_SetWanmInteLlmo_Object = MibTableColumn
setWanmInteLlmo = _SetWanmInteLlmo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 14, 1, 6),
    _SetWanmInteLlmo_Type()
)
setWanmInteLlmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmInteLlmo.setStatus("mandatory")


class _SetWanmInteLlbc_Type(Integer32):
    """Custom type setWanmInteLlbc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b1", 1),
          ("b2", 2),
          ("none", 0))
    )


_SetWanmInteLlbc_Type.__name__ = "Integer32"
_SetWanmInteLlbc_Object = MibTableColumn
setWanmInteLlbc = _SetWanmInteLlbc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 14, 1, 7),
    _SetWanmInteLlbc_Type()
)
setWanmInteLlbc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmInteLlbc.setStatus("mandatory")
_SetWanmInteDial_Type = DisplayString
_SetWanmInteDial_Object = MibTableColumn
setWanmInteDial = _SetWanmInteDial_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 14, 1, 9),
    _SetWanmInteDial_Type()
)
setWanmInteDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmInteDial.setStatus("mandatory")


class _SetWanmInteMaxi_Type(Integer32):
    """Custom type setWanmInteMaxi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 0),
          ("zero", 2))
    )


_SetWanmInteMaxi_Type.__name__ = "Integer32"
_SetWanmInteMaxi_Object = MibTableColumn
setWanmInteMaxi = _SetWanmInteMaxi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 14, 1, 13),
    _SetWanmInteMaxi_Type()
)
setWanmInteMaxi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmInteMaxi.setStatus("mandatory")


class _SetWanmInteMaxo_Type(Integer32):
    """Custom type setWanmInteMaxo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 0),
          ("zero", 2))
    )


_SetWanmInteMaxo_Type.__name__ = "Integer32"
_SetWanmInteMaxo_Object = MibTableColumn
setWanmInteMaxo = _SetWanmInteMaxo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 2, 14, 1, 14),
    _SetWanmInteMaxo_Type()
)
setWanmInteMaxo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setWanmInteMaxo.setStatus("mandatory")
_SetChar_ObjectIdentity = ObjectIdentity
setChar = _SetChar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3)
)
_SetCharBudgetu_Type = Integer32
_SetCharBudgetu_Object = MibScalar
setCharBudgetu = _SetCharBudgetu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 1),
    _SetCharBudgetu_Type()
)
setCharBudgetu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCharBudgetu.setStatus("mandatory")
_SetCharDaysper_Type = Integer32
_SetCharDaysper_Object = MibScalar
setCharDaysper = _SetCharDaysper_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 2),
    _SetCharDaysper_Type()
)
setCharDaysper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCharDaysper.setStatus("mandatory")
_SetCharSpareun_Type = Integer32
_SetCharSpareun_Object = MibScalar
setCharSpareun = _SetCharSpareun_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 3),
    _SetCharSpareun_Type()
)
setCharSpareun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharSpareun.setStatus("mandatory")
_SetCharRouteru_Type = Integer32
_SetCharRouteru_Object = MibScalar
setCharRouteru = _SetCharRouteru_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 4),
    _SetCharRouteru_Type()
)
setCharRouteru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharRouteru.setStatus("mandatory")
_SetCharTablebu_Object = MibTable
setCharTablebu = _SetCharTablebu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 5)
)
if mibBuilder.loadTexts:
    setCharTablebu.setStatus("mandatory")
_SetCharTablebuCols_Object = MibTableRow
setCharTablebuCols = _SetCharTablebuCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 5, 1)
)
setCharTablebuCols.setIndexNames(
    (0, "ELSA-MIB", "setCharTablebuIfc"),
)
if mibBuilder.loadTexts:
    setCharTablebuCols.setStatus("mandatory")


class _SetCharTablebuIfc_Type(Integer32):
    """Custom type setCharTablebuIfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ab-1", 3),
          ("ab-2", 4),
          ("ab-3", 5),
          ("ab-4", 6),
          ("lancapi", 2),
          ("router", 1),
          ("time-Modul", 255))
    )


_SetCharTablebuIfc_Type.__name__ = "Integer32"
_SetCharTablebuIfc_Object = MibTableColumn
setCharTablebuIfc = _SetCharTablebuIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 5, 1, 1),
    _SetCharTablebuIfc_Type()
)
setCharTablebuIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharTablebuIfc.setStatus("mandatory")
_SetCharTablebuBud_Type = Integer32
_SetCharTablebuBud_Object = MibTableColumn
setCharTablebuBud = _SetCharTablebuBud_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 5, 1, 2),
    _SetCharTablebuBud_Type()
)
setCharTablebuBud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharTablebuBud.setStatus("mandatory")
_SetCharTablebuSpa_Type = Integer32
_SetCharTablebuSpa_Object = MibTableColumn
setCharTablebuSpa = _SetCharTablebuSpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 5, 1, 3),
    _SetCharTablebuSpa_Type()
)
setCharTablebuSpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharTablebuSpa.setStatus("mandatory")
_SetCharTablebuTot_Type = Integer32
_SetCharTablebuTot_Object = MibTableColumn
setCharTablebuTot = _SetCharTablebuTot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 5, 1, 4),
    _SetCharTablebuTot_Type()
)
setCharTablebuTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharTablebuTot.setStatus("mandatory")
_SetCharTotalun_Type = Integer32
_SetCharTotalun_Object = MibScalar
setCharTotalun = _SetCharTotalun_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 6),
    _SetCharTotalun_Type()
)
setCharTotalun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharTotalun.setStatus("mandatory")
_SetCharTimetab_Object = MibTable
setCharTimetab = _SetCharTimetab_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 7)
)
if mibBuilder.loadTexts:
    setCharTimetab.setStatus("mandatory")
_SetCharTimetabCols_Object = MibTableRow
setCharTimetabCols = _SetCharTimetabCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 7, 1)
)
setCharTimetabCols.setIndexNames(
    (0, "ELSA-MIB", "setCharTimetabIfc"),
)
if mibBuilder.loadTexts:
    setCharTimetabCols.setStatus("mandatory")


class _SetCharTimetabIfc_Type(Integer32):
    """Custom type setCharTimetabIfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ab-1", 3),
          ("ab-2", 4),
          ("ab-3", 5),
          ("ab-4", 6),
          ("lancapi", 2),
          ("router", 1),
          ("time-Modul", 255))
    )


_SetCharTimetabIfc_Type.__name__ = "Integer32"
_SetCharTimetabIfc_Object = MibTableColumn
setCharTimetabIfc = _SetCharTimetabIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 7, 1, 1),
    _SetCharTimetabIfc_Type()
)
setCharTimetabIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharTimetabIfc.setStatus("mandatory")
_SetCharTimetabBudgetmi_Type = Integer32
_SetCharTimetabBudgetmi_Object = MibTableColumn
setCharTimetabBudgetmi = _SetCharTimetabBudgetmi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 7, 1, 2),
    _SetCharTimetabBudgetmi_Type()
)
setCharTimetabBudgetmi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharTimetabBudgetmi.setStatus("mandatory")
_SetCharTimetabSparemin_Type = Integer32
_SetCharTimetabSparemin_Object = MibTableColumn
setCharTimetabSparemin = _SetCharTimetabSparemin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 7, 1, 3),
    _SetCharTimetabSparemin_Type()
)
setCharTimetabSparemin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharTimetabSparemin.setStatus("mandatory")
_SetCharTimetabMinutesa_Type = Integer32
_SetCharTimetabMinutesa_Object = MibTableColumn
setCharTimetabMinutesa = _SetCharTimetabMinutesa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 7, 1, 4),
    _SetCharTimetabMinutesa_Type()
)
setCharTimetabMinutesa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharTimetabMinutesa.setStatus("mandatory")
_SetCharTimetabMinutesp_Type = Integer32
_SetCharTimetabMinutesp_Object = MibTableColumn
setCharTimetabMinutesp = _SetCharTimetabMinutesp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 7, 1, 5),
    _SetCharTimetabMinutesp_Type()
)
setCharTimetabMinutesp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharTimetabMinutesp.setStatus("mandatory")
_SetCharMinutes_Type = Integer32
_SetCharMinutes_Object = MibScalar
setCharMinutes = _SetCharMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 8),
    _SetCharMinutes_Type()
)
setCharMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCharMinutes.setStatus("mandatory")
_SetCharSparemi_Type = Integer32
_SetCharSparemi_Object = MibScalar
setCharSparemi = _SetCharSparemi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 9),
    _SetCharSparemi_Type()
)
setCharSparemi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharSparemi.setStatus("mandatory")
_SetCharRouterm_Type = Integer32
_SetCharRouterm_Object = MibScalar
setCharRouterm = _SetCharRouterm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 3, 10),
    _SetCharRouterm_Type()
)
setCharRouterm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCharRouterm.setStatus("mandatory")
_SetLanm_ObjectIdentity = ObjectIdentity
setLanm = _SetLanm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 4)
)


class _SetLanmCon_Type(Integer32):
    """Custom type setLanmCon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33,
              35)
        )
    )
    namedValues = NamedValues(
        *(("auto", 35),
          ("ten-b2", 33),
          ("ten-bt", 32))
    )


_SetLanmCon_Type.__name__ = "Integer32"
_SetLanmCon_Object = MibScalar
setLanmCon = _SetLanmCon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 4, 1),
    _SetLanmCon_Type()
)
setLanmCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLanmCon.setStatus("mandatory")


class _SetLanmNod_Type(DisplayString):
    """Custom type setLanmNod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SetLanmNod_Type.__name__ = "DisplayString"
_SetLanmNod_Object = MibScalar
setLanmNod = _SetLanmNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 4, 2),
    _SetLanmNod_Type()
)
setLanmNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setLanmNod.setStatus("mandatory")
_SetLanmSpa_Type = Integer32
_SetLanmSpa_Object = MibScalar
setLanmSpa = _SetLanmSpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 4, 3),
    _SetLanmSpa_Type()
)
setLanmSpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLanmSpa.setStatus("mandatory")
_SetBrid_ObjectIdentity = ObjectIdentity
setBrid = _SetBrid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5)
)


class _SetBridOpe_Type(Integer32):
    """Custom type setBridOpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetBridOpe_Type.__name__ = "Integer32"
_SetBridOpe_Object = MibScalar
setBridOpe = _SetBridOpe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 1),
    _SetBridOpe_Type()
)
setBridOpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridOpe.setStatus("mandatory")


class _SetBridRem_Type(DisplayString):
    """Custom type setBridRem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SetBridRem_Type.__name__ = "DisplayString"
_SetBridRem_Object = MibScalar
setBridRem = _SetBridRem_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 2),
    _SetBridRem_Type()
)
setBridRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridRem.setStatus("mandatory")
_SetBridTab_Object = MibTable
setBridTab = _SetBridTab_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 3)
)
if mibBuilder.loadTexts:
    setBridTab.setStatus("mandatory")
_SetBridTabCols_Object = MibTableRow
setBridTabCols = _SetBridTabCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 3, 1)
)
setBridTabCols.setIndexNames(
    (0, "ELSA-MIB", "setBridTabNod"),
)
if mibBuilder.loadTexts:
    setBridTabCols.setStatus("mandatory")
_SetBridTabNod_Type = DisplayString
_SetBridTabNod_Object = MibTableColumn
setBridTabNod = _SetBridTabNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 3, 1, 1),
    _SetBridTabNod_Type()
)
setBridTabNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setBridTabNod.setStatus("mandatory")
_SetBridTabLas_Type = Integer32
_SetBridTabLas_Object = MibTableColumn
setBridTabLas = _SetBridTabLas_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 3, 1, 2),
    _SetBridTabLas_Type()
)
setBridTabLas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setBridTabLas.setStatus("mandatory")
_SetBridTabFor_Type = DisplayString
_SetBridTabFor_Object = MibTableColumn
setBridTabFor = _SetBridTabFor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 3, 1, 3),
    _SetBridTabFor_Type()
)
setBridTabFor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setBridTabFor.setStatus("mandatory")
_SetBridAgi_Type = Integer32
_SetBridAgi_Object = MibScalar
setBridAgi = _SetBridAgi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 4),
    _SetBridAgi_Type()
)
setBridAgi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridAgi.setStatus("mandatory")
_SetBridLan_ObjectIdentity = ObjectIdentity
setBridLan = _SetBridLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5)
)


class _SetBridLanBro_Type(Integer32):
    """Custom type setBridLanBro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 1),
          ("semi", 2))
    )


_SetBridLanBro_Type.__name__ = "Integer32"
_SetBridLanBro_Object = MibScalar
setBridLanBro = _SetBridLanBro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 1),
    _SetBridLanBro_Type()
)
setBridLanBro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridLanBro.setStatus("mandatory")


class _SetBridLanMul_Type(Integer32):
    """Custom type setBridLanMul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 1),
          ("semi", 2))
    )


_SetBridLanMul_Type.__name__ = "Integer32"
_SetBridLanMul_Object = MibScalar
setBridLanMul = _SetBridLanMul_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 2),
    _SetBridLanMul_Type()
)
setBridLanMul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridLanMul.setStatus("mandatory")
_SetBridLanDes_ObjectIdentity = ObjectIdentity
setBridLanDes = _SetBridLanDes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 3)
)


class _SetBridLanDesFilterty_Type(Integer32):
    """Custom type setBridLanDesFilterty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 4))
    )


_SetBridLanDesFilterty_Type.__name__ = "Integer32"
_SetBridLanDesFilterty_Object = MibScalar
setBridLanDesFilterty = _SetBridLanDesFilterty_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 3, 1),
    _SetBridLanDesFilterty_Type()
)
setBridLanDesFilterty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridLanDesFilterty.setStatus("mandatory")
_SetBridLanDesFilterta_Object = MibTable
setBridLanDesFilterta = _SetBridLanDesFilterta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 3, 2)
)
if mibBuilder.loadTexts:
    setBridLanDesFilterta.setStatus("mandatory")
_SetBridLanDesFiltertaCols_Object = MibTableRow
setBridLanDesFiltertaCols = _SetBridLanDesFiltertaCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 3, 2, 1)
)
setBridLanDesFiltertaCols.setIndexNames(
    (0, "ELSA-MIB", "setBridLanDesFiltertaDes"),
)
if mibBuilder.loadTexts:
    setBridLanDesFiltertaCols.setStatus("mandatory")
_SetBridLanDesFiltertaDes_Type = DisplayString
_SetBridLanDesFiltertaDes_Object = MibTableColumn
setBridLanDesFiltertaDes = _SetBridLanDesFiltertaDes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 3, 2, 1, 1),
    _SetBridLanDesFiltertaDes_Type()
)
setBridLanDesFiltertaDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridLanDesFiltertaDes.setStatus("mandatory")
_SetBridLanSrc_ObjectIdentity = ObjectIdentity
setBridLanSrc = _SetBridLanSrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 4)
)


class _SetBridLanSrcFilterty_Type(Integer32):
    """Custom type setBridLanSrcFilterty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 8))
    )


_SetBridLanSrcFilterty_Type.__name__ = "Integer32"
_SetBridLanSrcFilterty_Object = MibScalar
setBridLanSrcFilterty = _SetBridLanSrcFilterty_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 4, 1),
    _SetBridLanSrcFilterty_Type()
)
setBridLanSrcFilterty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridLanSrcFilterty.setStatus("mandatory")
_SetBridLanSrcFilterta_Object = MibTable
setBridLanSrcFilterta = _SetBridLanSrcFilterta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 4, 2)
)
if mibBuilder.loadTexts:
    setBridLanSrcFilterta.setStatus("mandatory")
_SetBridLanSrcFiltertaCols_Object = MibTableRow
setBridLanSrcFiltertaCols = _SetBridLanSrcFiltertaCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 4, 2, 1)
)
setBridLanSrcFiltertaCols.setIndexNames(
    (0, "ELSA-MIB", "setBridLanSrcFiltertaSrc"),
)
if mibBuilder.loadTexts:
    setBridLanSrcFiltertaCols.setStatus("mandatory")
_SetBridLanSrcFiltertaSrc_Type = DisplayString
_SetBridLanSrcFiltertaSrc_Object = MibTableColumn
setBridLanSrcFiltertaSrc = _SetBridLanSrcFiltertaSrc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 5, 4, 2, 1, 1),
    _SetBridLanSrcFiltertaSrc_Type()
)
setBridLanSrcFiltertaSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridLanSrcFiltertaSrc.setStatus("mandatory")
_SetBridWan_ObjectIdentity = ObjectIdentity
setBridWan = _SetBridWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6)
)


class _SetBridWanBro_Type(Integer32):
    """Custom type setBridWanBro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 1),
          ("semi", 2))
    )


_SetBridWanBro_Type.__name__ = "Integer32"
_SetBridWanBro_Object = MibScalar
setBridWanBro = _SetBridWanBro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 1),
    _SetBridWanBro_Type()
)
setBridWanBro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridWanBro.setStatus("mandatory")


class _SetBridWanMul_Type(Integer32):
    """Custom type setBridWanMul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 1),
          ("semi", 2))
    )


_SetBridWanMul_Type.__name__ = "Integer32"
_SetBridWanMul_Object = MibScalar
setBridWanMul = _SetBridWanMul_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 2),
    _SetBridWanMul_Type()
)
setBridWanMul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridWanMul.setStatus("mandatory")
_SetBridWanDes_ObjectIdentity = ObjectIdentity
setBridWanDes = _SetBridWanDes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 3)
)


class _SetBridWanDesFilterty_Type(Integer32):
    """Custom type setBridWanDesFilterty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 1))
    )


_SetBridWanDesFilterty_Type.__name__ = "Integer32"
_SetBridWanDesFilterty_Object = MibScalar
setBridWanDesFilterty = _SetBridWanDesFilterty_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 3, 1),
    _SetBridWanDesFilterty_Type()
)
setBridWanDesFilterty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridWanDesFilterty.setStatus("mandatory")
_SetBridWanDesFilterta_Object = MibTable
setBridWanDesFilterta = _SetBridWanDesFilterta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 3, 2)
)
if mibBuilder.loadTexts:
    setBridWanDesFilterta.setStatus("mandatory")
_SetBridWanDesFiltertaCols_Object = MibTableRow
setBridWanDesFiltertaCols = _SetBridWanDesFiltertaCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 3, 2, 1)
)
setBridWanDesFiltertaCols.setIndexNames(
    (0, "ELSA-MIB", "setBridWanDesFiltertaDes"),
)
if mibBuilder.loadTexts:
    setBridWanDesFiltertaCols.setStatus("mandatory")
_SetBridWanDesFiltertaDes_Type = DisplayString
_SetBridWanDesFiltertaDes_Object = MibTableColumn
setBridWanDesFiltertaDes = _SetBridWanDesFiltertaDes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 3, 2, 1, 1),
    _SetBridWanDesFiltertaDes_Type()
)
setBridWanDesFiltertaDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridWanDesFiltertaDes.setStatus("mandatory")
_SetBridWanSrc_ObjectIdentity = ObjectIdentity
setBridWanSrc = _SetBridWanSrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 4)
)


class _SetBridWanSrcFilterty_Type(Integer32):
    """Custom type setBridWanSrcFilterty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 0),
          ("positive", 2))
    )


_SetBridWanSrcFilterty_Type.__name__ = "Integer32"
_SetBridWanSrcFilterty_Object = MibScalar
setBridWanSrcFilterty = _SetBridWanSrcFilterty_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 4, 1),
    _SetBridWanSrcFilterty_Type()
)
setBridWanSrcFilterty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridWanSrcFilterty.setStatus("mandatory")
_SetBridWanSrcFilterta_Object = MibTable
setBridWanSrcFilterta = _SetBridWanSrcFilterta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 4, 2)
)
if mibBuilder.loadTexts:
    setBridWanSrcFilterta.setStatus("mandatory")
_SetBridWanSrcFiltertaCols_Object = MibTableRow
setBridWanSrcFiltertaCols = _SetBridWanSrcFiltertaCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 4, 2, 1)
)
setBridWanSrcFiltertaCols.setIndexNames(
    (0, "ELSA-MIB", "setBridWanSrcFiltertaDes"),
)
if mibBuilder.loadTexts:
    setBridWanSrcFiltertaCols.setStatus("mandatory")
_SetBridWanSrcFiltertaDes_Type = DisplayString
_SetBridWanSrcFiltertaDes_Object = MibTableColumn
setBridWanSrcFiltertaDes = _SetBridWanSrcFiltertaDes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 5, 6, 4, 2, 1, 1),
    _SetBridWanSrcFiltertaDes_Type()
)
setBridWanSrcFiltertaDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setBridWanSrcFiltertaDes.setStatus("mandatory")
_SetIpxm_ObjectIdentity = ObjectIdentity
setIpxm = _SetIpxm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6)
)


class _SetIpxmOpe_Type(Integer32):
    """Custom type setIpxmOpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetIpxmOpe_Type.__name__ = "Integer32"
_SetIpxmOpe_Object = MibScalar
setIpxmOpe = _SetIpxmOpe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 1),
    _SetIpxmOpe_Type()
)
setIpxmOpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmOpe.setStatus("mandatory")


class _SetIpxmIpx_Type(Integer32):
    """Custom type setIpxmIpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetIpxmIpx_Type.__name__ = "Integer32"
_SetIpxmIpx_Object = MibScalar
setIpxmIpx = _SetIpxmIpx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 2),
    _SetIpxmIpx_Type()
)
setIpxmIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmIpx.setStatus("mandatory")
_SetIpxmLan_ObjectIdentity = ObjectIdentity
setIpxmLan = _SetIpxmLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3)
)


class _SetIpxmLanNetw_Type(DisplayString):
    """Custom type setIpxmLanNetw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SetIpxmLanNetw_Type.__name__ = "DisplayString"
_SetIpxmLanNetw_Object = MibScalar
setIpxmLanNetw = _SetIpxmLanNetw_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 1),
    _SetIpxmLanNetw_Type()
)
setIpxmLanNetw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmLanNetw.setStatus("mandatory")


class _SetIpxmLanBind_Type(Integer32):
    """Custom type setIpxmLanBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("dot802-2", 4),
          ("dot802-3", 2),
          ("ii", 1),
          ("snap", 8))
    )


_SetIpxmLanBind_Type.__name__ = "Integer32"
_SetIpxmLanBind_Object = MibScalar
setIpxmLanBind = _SetIpxmLanBind_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 2),
    _SetIpxmLanBind_Type()
)
setIpxmLanBind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmLanBind.setStatus("mandatory")


class _SetIpxmLanSpxw_Type(Integer32):
    """Custom type setIpxmLanSpxw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 3),
          ("route", 1),
          ("spoof", 0))
    )


_SetIpxmLanSpxw_Type.__name__ = "Integer32"
_SetIpxmLanSpxw_Object = MibScalar
setIpxmLanSpxw = _SetIpxmLanSpxw_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 3),
    _SetIpxmLanSpxw_Type()
)
setIpxmLanSpxw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmLanSpxw.setStatus("mandatory")


class _SetIpxmLanIpxw_Type(Integer32):
    """Custom type setIpxmLanIpxw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("route", 1),
          ("spoof", 0))
    )


_SetIpxmLanIpxw_Type.__name__ = "Integer32"
_SetIpxmLanIpxw_Object = MibScalar
setIpxmLanIpxw = _SetIpxmLanIpxw_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 4),
    _SetIpxmLanIpxw_Type()
)
setIpxmLanIpxw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmLanIpxw.setStatus("mandatory")


class _SetIpxmLanNetb_Type(Integer32):
    """Custom type setIpxmLanNetb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("route", 3),
          ("spoof", 0))
    )


_SetIpxmLanNetb_Type.__name__ = "Integer32"
_SetIpxmLanNetb_Object = MibScalar
setIpxmLanNetb = _SetIpxmLanNetb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 5),
    _SetIpxmLanNetb_Type()
)
setIpxmLanNetb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmLanNetb.setStatus("mandatory")
_SetIpxmLanSock_Object = MibTable
setIpxmLanSock = _SetIpxmLanSock_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 6)
)
if mibBuilder.loadTexts:
    setIpxmLanSock.setStatus("mandatory")
_SetIpxmLanSockCols_Object = MibTableRow
setIpxmLanSockCols = _SetIpxmLanSockCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 6, 1)
)
setIpxmLanSockCols.setIndexNames(
    (0, "ELSA-MIB", "setIpxmLanSockSta"),
)
if mibBuilder.loadTexts:
    setIpxmLanSockCols.setStatus("mandatory")
_SetIpxmLanSockSta_Type = DisplayString
_SetIpxmLanSockSta_Object = MibTableColumn
setIpxmLanSockSta = _SetIpxmLanSockSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 6, 1, 1),
    _SetIpxmLanSockSta_Type()
)
setIpxmLanSockSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmLanSockSta.setStatus("mandatory")
_SetIpxmLanSockEnd_Type = DisplayString
_SetIpxmLanSockEnd_Object = MibTableColumn
setIpxmLanSockEnd = _SetIpxmLanSockEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 6, 1, 2),
    _SetIpxmLanSockEnd_Type()
)
setIpxmLanSockEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmLanSockEnd.setStatus("mandatory")


class _SetIpxmLanLocr_Type(Integer32):
    """Custom type setIpxmLanLocr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetIpxmLanLocr_Type.__name__ = "Integer32"
_SetIpxmLanLocr_Object = MibScalar
setIpxmLanLocr = _SetIpxmLanLocr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 7),
    _SetIpxmLanLocr_Type()
)
setIpxmLanLocr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmLanLocr.setStatus("mandatory")


class _SetIpxmLanRips_Type(Integer32):
    """Custom type setIpxmLanRips based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetIpxmLanRips_Type.__name__ = "Integer32"
_SetIpxmLanRips_Object = MibScalar
setIpxmLanRips = _SetIpxmLanRips_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 8),
    _SetIpxmLanRips_Type()
)
setIpxmLanRips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmLanRips.setStatus("mandatory")


class _SetIpxmLanLoop_Type(Integer32):
    """Custom type setIpxmLanLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetIpxmLanLoop_Type.__name__ = "Integer32"
_SetIpxmLanLoop_Object = MibScalar
setIpxmLanLoop = _SetIpxmLanLoop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 3, 9),
    _SetIpxmLanLoop_Type()
)
setIpxmLanLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmLanLoop.setStatus("mandatory")
_SetIpxmWan_ObjectIdentity = ObjectIdentity
setIpxmWan = _SetIpxmWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4)
)
_SetIpxmWanRou_Object = MibTable
setIpxmWanRou = _SetIpxmWanRou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 1)
)
if mibBuilder.loadTexts:
    setIpxmWanRou.setStatus("mandatory")
_SetIpxmWanRouCols_Object = MibTableRow
setIpxmWanRouCols = _SetIpxmWanRouCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 1, 1)
)
setIpxmWanRouCols.setIndexNames(
    (0, "ELSA-MIB", "setIpxmWanRouRem"),
)
if mibBuilder.loadTexts:
    setIpxmWanRouCols.setStatus("mandatory")
_SetIpxmWanRouRem_Type = DisplayString
_SetIpxmWanRouRem_Object = MibTableColumn
setIpxmWanRouRem = _SetIpxmWanRouRem_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 1, 1, 1),
    _SetIpxmWanRouRem_Type()
)
setIpxmWanRouRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmWanRouRem.setStatus("mandatory")
_SetIpxmWanRouNet_Type = DisplayString
_SetIpxmWanRouNet_Object = MibTableColumn
setIpxmWanRouNet = _SetIpxmWanRouNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 1, 1, 2),
    _SetIpxmWanRouNet_Type()
)
setIpxmWanRouNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmWanRouNet.setStatus("mandatory")


class _SetIpxmWanRouBin_Type(Integer32):
    """Custom type setIpxmWanRouBin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dot802-2", 4),
          ("dot802-3", 2),
          ("ii", 1),
          ("snap", 8))
    )


_SetIpxmWanRouBin_Type.__name__ = "Integer32"
_SetIpxmWanRouBin_Object = MibTableColumn
setIpxmWanRouBin = _SetIpxmWanRouBin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 1, 1, 3),
    _SetIpxmWanRouBin_Type()
)
setIpxmWanRouBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmWanRouBin.setStatus("mandatory")


class _SetIpxmWanRouPro_Type(Integer32):
    """Custom type setIpxmWanRouPro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("route", 3))
    )


_SetIpxmWanRouPro_Type.__name__ = "Integer32"
_SetIpxmWanRouPro_Object = MibTableColumn
setIpxmWanRouPro = _SetIpxmWanRouPro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 1, 1, 4),
    _SetIpxmWanRouPro_Type()
)
setIpxmWanRouPro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmWanRouPro.setStatus("mandatory")


class _SetIpxmWanRouBac_Type(Integer32):
    """Custom type setIpxmWanRouBac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetIpxmWanRouBac_Type.__name__ = "Integer32"
_SetIpxmWanRouBac_Object = MibTableColumn
setIpxmWanRouBac = _SetIpxmWanRouBac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 1, 1, 5),
    _SetIpxmWanRouBac_Type()
)
setIpxmWanRouBac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmWanRouBac.setStatus("mandatory")
_SetIpxmWanSoc_Object = MibTable
setIpxmWanSoc = _SetIpxmWanSoc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 2)
)
if mibBuilder.loadTexts:
    setIpxmWanSoc.setStatus("mandatory")
_SetIpxmWanSocCols_Object = MibTableRow
setIpxmWanSocCols = _SetIpxmWanSocCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 2, 1)
)
setIpxmWanSocCols.setIndexNames(
    (0, "ELSA-MIB", "setIpxmWanSocSta"),
)
if mibBuilder.loadTexts:
    setIpxmWanSocCols.setStatus("mandatory")
_SetIpxmWanSocSta_Type = DisplayString
_SetIpxmWanSocSta_Object = MibTableColumn
setIpxmWanSocSta = _SetIpxmWanSocSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 2, 1, 1),
    _SetIpxmWanSocSta_Type()
)
setIpxmWanSocSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmWanSocSta.setStatus("mandatory")
_SetIpxmWanSocEnd_Type = DisplayString
_SetIpxmWanSocEnd_Object = MibTableColumn
setIpxmWanSocEnd = _SetIpxmWanSocEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 4, 2, 1, 2),
    _SetIpxmWanSocEnd_Type()
)
setIpxmWanSocEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmWanSocEnd.setStatus("mandatory")
_SetIpxmRip_ObjectIdentity = ObjectIdentity
setIpxmRip = _SetIpxmRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5)
)
_SetIpxmRipTabl_Object = MibTable
setIpxmRipTabl = _SetIpxmRipTabl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 1)
)
if mibBuilder.loadTexts:
    setIpxmRipTabl.setStatus("mandatory")
_SetIpxmRipTablCols_Object = MibTableRow
setIpxmRipTablCols = _SetIpxmRipTablCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 1, 1)
)
setIpxmRipTablCols.setIndexNames(
    (0, "ELSA-MIB", "setIpxmRipTablNet"),
)
if mibBuilder.loadTexts:
    setIpxmRipTablCols.setStatus("mandatory")
_SetIpxmRipTablNet_Type = DisplayString
_SetIpxmRipTablNet_Object = MibTableColumn
setIpxmRipTablNet = _SetIpxmRipTablNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 1, 1, 1),
    _SetIpxmRipTablNet_Type()
)
setIpxmRipTablNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmRipTablNet.setStatus("mandatory")
_SetIpxmRipTablHop_Type = Integer32
_SetIpxmRipTablHop_Object = MibTableColumn
setIpxmRipTablHop = _SetIpxmRipTablHop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 1, 1, 2),
    _SetIpxmRipTablHop_Type()
)
setIpxmRipTablHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmRipTablHop.setStatus("mandatory")
_SetIpxmRipTablTic_Type = Integer32
_SetIpxmRipTablTic_Object = MibTableColumn
setIpxmRipTablTic = _SetIpxmRipTablTic_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 1, 1, 3),
    _SetIpxmRipTablTic_Type()
)
setIpxmRipTablTic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmRipTablTic.setStatus("mandatory")
_SetIpxmRipTablNod_Type = DisplayString
_SetIpxmRipTablNod_Object = MibTableColumn
setIpxmRipTablNod = _SetIpxmRipTablNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 1, 1, 4),
    _SetIpxmRipTablNod_Type()
)
setIpxmRipTablNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmRipTablNod.setStatus("mandatory")
_SetIpxmRipTablTim_Type = Integer32
_SetIpxmRipTablTim_Object = MibTableColumn
setIpxmRipTablTim = _SetIpxmRipTablTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 1, 1, 5),
    _SetIpxmRipTablTim_Type()
)
setIpxmRipTablTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmRipTablTim.setStatus("mandatory")


class _SetIpxmRipTablFla_Type(Integer32):
    """Custom type setIpxmRipTablFla based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("direct", 128),
          ("down", 32),
          ("local", 2),
          ("loop", 16),
          ("new", 64),
          ("remote", 1),
          ("spare", 8))
    )


_SetIpxmRipTablFla_Type.__name__ = "Integer32"
_SetIpxmRipTablFla_Object = MibTableColumn
setIpxmRipTablFla = _SetIpxmRipTablFla_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 1, 1, 6),
    _SetIpxmRipTablFla_Type()
)
setIpxmRipTablFla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmRipTablFla.setStatus("mandatory")
_SetIpxmRipLanf_Object = MibTable
setIpxmRipLanf = _SetIpxmRipLanf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 2)
)
if mibBuilder.loadTexts:
    setIpxmRipLanf.setStatus("mandatory")
_SetIpxmRipLanfCols_Object = MibTableRow
setIpxmRipLanfCols = _SetIpxmRipLanfCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 2, 1)
)
setIpxmRipLanfCols.setIndexNames(
    (0, "ELSA-MIB", "setIpxmRipLanfSta"),
)
if mibBuilder.loadTexts:
    setIpxmRipLanfCols.setStatus("mandatory")
_SetIpxmRipLanfSta_Type = DisplayString
_SetIpxmRipLanfSta_Object = MibTableColumn
setIpxmRipLanfSta = _SetIpxmRipLanfSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 2, 1, 1),
    _SetIpxmRipLanfSta_Type()
)
setIpxmRipLanfSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmRipLanfSta.setStatus("mandatory")
_SetIpxmRipLanfEnd_Type = DisplayString
_SetIpxmRipLanfEnd_Object = MibTableColumn
setIpxmRipLanfEnd = _SetIpxmRipLanfEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 2, 1, 2),
    _SetIpxmRipLanfEnd_Type()
)
setIpxmRipLanfEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmRipLanfEnd.setStatus("mandatory")
_SetIpxmRipWanf_Object = MibTable
setIpxmRipWanf = _SetIpxmRipWanf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 3)
)
if mibBuilder.loadTexts:
    setIpxmRipWanf.setStatus("mandatory")
_SetIpxmRipWanfCols_Object = MibTableRow
setIpxmRipWanfCols = _SetIpxmRipWanfCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 3, 1)
)
setIpxmRipWanfCols.setIndexNames(
    (0, "ELSA-MIB", "setIpxmRipWanfSta"),
)
if mibBuilder.loadTexts:
    setIpxmRipWanfCols.setStatus("mandatory")
_SetIpxmRipWanfSta_Type = DisplayString
_SetIpxmRipWanfSta_Object = MibTableColumn
setIpxmRipWanfSta = _SetIpxmRipWanfSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 3, 1, 1),
    _SetIpxmRipWanfSta_Type()
)
setIpxmRipWanfSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmRipWanfSta.setStatus("mandatory")
_SetIpxmRipWanfEnd_Type = DisplayString
_SetIpxmRipWanfEnd_Object = MibTableColumn
setIpxmRipWanfEnd = _SetIpxmRipWanfEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 3, 1, 2),
    _SetIpxmRipWanfEnd_Type()
)
setIpxmRipWanfEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmRipWanfEnd.setStatus("mandatory")
_SetIpxmRipRout_Type = Integer32
_SetIpxmRipRout_Object = MibScalar
setIpxmRipRout = _SetIpxmRipRout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 4),
    _SetIpxmRipRout_Type()
)
setIpxmRipRout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmRipRout.setStatus("mandatory")
_SetIpxmRipAgin_Type = Integer32
_SetIpxmRipAgin_Object = MibScalar
setIpxmRipAgin = _SetIpxmRipAgin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 5),
    _SetIpxmRipAgin_Type()
)
setIpxmRipAgin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmRipAgin.setStatus("mandatory")


class _SetIpxmRipSpoo_Type(Integer32):
    """Custom type setIpxmRipSpoo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("pback", 3),
          ("time", 2),
          ("trig", 1))
    )


_SetIpxmRipSpoo_Type.__name__ = "Integer32"
_SetIpxmRipSpoo_Object = MibScalar
setIpxmRipSpoo = _SetIpxmRipSpoo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 6),
    _SetIpxmRipSpoo_Type()
)
setIpxmRipSpoo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmRipSpoo.setStatus("mandatory")
_SetIpxmRipWanu_Type = Integer32
_SetIpxmRipWanu_Object = MibScalar
setIpxmRipWanu = _SetIpxmRipWanu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 5, 7),
    _SetIpxmRipWanu_Type()
)
setIpxmRipWanu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmRipWanu.setStatus("mandatory")
_SetIpxmSap_ObjectIdentity = ObjectIdentity
setIpxmSap = _SetIpxmSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6)
)
_SetIpxmSapTabl_Object = MibTable
setIpxmSapTabl = _SetIpxmSapTabl_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 1)
)
if mibBuilder.loadTexts:
    setIpxmSapTabl.setStatus("mandatory")
_SetIpxmSapTablCols_Object = MibTableRow
setIpxmSapTablCols = _SetIpxmSapTablCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 1, 1)
)
setIpxmSapTablCols.setIndexNames(
    (0, "ELSA-MIB", "setIpxmSapTablTyp"),
)
if mibBuilder.loadTexts:
    setIpxmSapTablCols.setStatus("mandatory")
_SetIpxmSapTablTyp_Type = DisplayString
_SetIpxmSapTablTyp_Object = MibTableColumn
setIpxmSapTablTyp = _SetIpxmSapTablTyp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 1, 1, 1),
    _SetIpxmSapTablTyp_Type()
)
setIpxmSapTablTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmSapTablTyp.setStatus("mandatory")
_SetIpxmSapTablSer_Type = DisplayString
_SetIpxmSapTablSer_Object = MibTableColumn
setIpxmSapTablSer = _SetIpxmSapTablSer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 1, 1, 2),
    _SetIpxmSapTablSer_Type()
)
setIpxmSapTablSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmSapTablSer.setStatus("mandatory")
_SetIpxmSapTablNet_Type = DisplayString
_SetIpxmSapTablNet_Object = MibTableColumn
setIpxmSapTablNet = _SetIpxmSapTablNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 1, 1, 3),
    _SetIpxmSapTablNet_Type()
)
setIpxmSapTablNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmSapTablNet.setStatus("mandatory")
_SetIpxmSapTablNod_Type = DisplayString
_SetIpxmSapTablNod_Object = MibTableColumn
setIpxmSapTablNod = _SetIpxmSapTablNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 1, 1, 4),
    _SetIpxmSapTablNod_Type()
)
setIpxmSapTablNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmSapTablNod.setStatus("mandatory")
_SetIpxmSapTablSoc_Type = DisplayString
_SetIpxmSapTablSoc_Object = MibTableColumn
setIpxmSapTablSoc = _SetIpxmSapTablSoc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 1, 1, 5),
    _SetIpxmSapTablSoc_Type()
)
setIpxmSapTablSoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmSapTablSoc.setStatus("mandatory")
_SetIpxmSapTablHop_Type = Integer32
_SetIpxmSapTablHop_Object = MibTableColumn
setIpxmSapTablHop = _SetIpxmSapTablHop_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 1, 1, 6),
    _SetIpxmSapTablHop_Type()
)
setIpxmSapTablHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmSapTablHop.setStatus("mandatory")
_SetIpxmSapTablTim_Type = Integer32
_SetIpxmSapTablTim_Object = MibTableColumn
setIpxmSapTablTim = _SetIpxmSapTablTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 1, 1, 7),
    _SetIpxmSapTablTim_Type()
)
setIpxmSapTablTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmSapTablTim.setStatus("mandatory")


class _SetIpxmSapTablFla_Type(Integer32):
    """Custom type setIpxmSapTablFla based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("direct", 128),
          ("down", 32),
          ("local", 2),
          ("loop", 16),
          ("new", 64),
          ("remote", 1),
          ("spare", 8))
    )


_SetIpxmSapTablFla_Type.__name__ = "Integer32"
_SetIpxmSapTablFla_Object = MibTableColumn
setIpxmSapTablFla = _SetIpxmSapTablFla_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 1, 1, 8),
    _SetIpxmSapTablFla_Type()
)
setIpxmSapTablFla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpxmSapTablFla.setStatus("mandatory")
_SetIpxmSapLanf_Object = MibTable
setIpxmSapLanf = _SetIpxmSapLanf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 2)
)
if mibBuilder.loadTexts:
    setIpxmSapLanf.setStatus("mandatory")
_SetIpxmSapLanfCols_Object = MibTableRow
setIpxmSapLanfCols = _SetIpxmSapLanfCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 2, 1)
)
setIpxmSapLanfCols.setIndexNames(
    (0, "ELSA-MIB", "setIpxmSapLanfSta"),
)
if mibBuilder.loadTexts:
    setIpxmSapLanfCols.setStatus("mandatory")
_SetIpxmSapLanfSta_Type = DisplayString
_SetIpxmSapLanfSta_Object = MibTableColumn
setIpxmSapLanfSta = _SetIpxmSapLanfSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 2, 1, 1),
    _SetIpxmSapLanfSta_Type()
)
setIpxmSapLanfSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmSapLanfSta.setStatus("mandatory")
_SetIpxmSapLanfEnd_Type = DisplayString
_SetIpxmSapLanfEnd_Object = MibTableColumn
setIpxmSapLanfEnd = _SetIpxmSapLanfEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 2, 1, 2),
    _SetIpxmSapLanfEnd_Type()
)
setIpxmSapLanfEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmSapLanfEnd.setStatus("mandatory")
_SetIpxmSapWanf_Object = MibTable
setIpxmSapWanf = _SetIpxmSapWanf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 3)
)
if mibBuilder.loadTexts:
    setIpxmSapWanf.setStatus("mandatory")
_SetIpxmSapWanfCols_Object = MibTableRow
setIpxmSapWanfCols = _SetIpxmSapWanfCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 3, 1)
)
setIpxmSapWanfCols.setIndexNames(
    (0, "ELSA-MIB", "setIpxmSapWanfSta"),
)
if mibBuilder.loadTexts:
    setIpxmSapWanfCols.setStatus("mandatory")
_SetIpxmSapWanfSta_Type = DisplayString
_SetIpxmSapWanfSta_Object = MibTableColumn
setIpxmSapWanfSta = _SetIpxmSapWanfSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 3, 1, 1),
    _SetIpxmSapWanfSta_Type()
)
setIpxmSapWanfSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmSapWanfSta.setStatus("mandatory")
_SetIpxmSapWanfEnd_Type = DisplayString
_SetIpxmSapWanfEnd_Object = MibTableColumn
setIpxmSapWanfEnd = _SetIpxmSapWanfEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 3, 1, 2),
    _SetIpxmSapWanfEnd_Type()
)
setIpxmSapWanfEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmSapWanfEnd.setStatus("mandatory")
_SetIpxmSapServ_Type = Integer32
_SetIpxmSapServ_Object = MibScalar
setIpxmSapServ = _SetIpxmSapServ_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 4),
    _SetIpxmSapServ_Type()
)
setIpxmSapServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmSapServ.setStatus("mandatory")
_SetIpxmSapAgin_Type = Integer32
_SetIpxmSapAgin_Object = MibScalar
setIpxmSapAgin = _SetIpxmSapAgin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 5),
    _SetIpxmSapAgin_Type()
)
setIpxmSapAgin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmSapAgin.setStatus("mandatory")


class _SetIpxmSapSpoo_Type(Integer32):
    """Custom type setIpxmSapSpoo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("pback", 3),
          ("time", 2),
          ("trig", 1))
    )


_SetIpxmSapSpoo_Type.__name__ = "Integer32"
_SetIpxmSapSpoo_Object = MibScalar
setIpxmSapSpoo = _SetIpxmSapSpoo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 6),
    _SetIpxmSapSpoo_Type()
)
setIpxmSapSpoo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmSapSpoo.setStatus("mandatory")
_SetIpxmSapWanu_Type = Integer32
_SetIpxmSapWanu_Object = MibScalar
setIpxmSapWanu = _SetIpxmSapWanu_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 6, 6, 7),
    _SetIpxmSapWanu_Type()
)
setIpxmSapWanu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpxmSapWanu.setStatus("mandatory")
_SetTcpi_ObjectIdentity = ObjectIdentity
setTcpi = _SetTcpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7)
)


class _SetTcpiOperating_Type(Integer32):
    """Custom type setTcpiOperating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetTcpiOperating_Type.__name__ = "Integer32"
_SetTcpiOperating_Object = MibScalar
setTcpiOperating = _SetTcpiOperating_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 1),
    _SetTcpiOperating_Type()
)
setTcpiOperating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiOperating.setStatus("mandatory")
_SetTcpiIpaddress_Type = IpAddress
_SetTcpiIpaddress_Object = MibScalar
setTcpiIpaddress = _SetTcpiIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 2),
    _SetTcpiIpaddress_Type()
)
setTcpiIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiIpaddress.setStatus("mandatory")
_SetTcpiIpnetmask_Type = IpAddress
_SetTcpiIpnetmask_Object = MibScalar
setTcpiIpnetmask = _SetTcpiIpnetmask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 3),
    _SetTcpiIpnetmask_Type()
)
setTcpiIpnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiIpnetmask.setStatus("mandatory")
_SetTcpiIntraneta_Type = IpAddress
_SetTcpiIntraneta_Object = MibScalar
setTcpiIntraneta = _SetTcpiIntraneta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 4),
    _SetTcpiIntraneta_Type()
)
setTcpiIntraneta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiIntraneta.setStatus("mandatory")
_SetTcpiIntranetm_Type = IpAddress
_SetTcpiIntranetm_Object = MibScalar
setTcpiIntranetm = _SetTcpiIntranetm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 5),
    _SetTcpiIntranetm_Type()
)
setTcpiIntranetm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiIntranetm.setStatus("mandatory")
_SetTcpiAccesslis_Object = MibTable
setTcpiAccesslis = _SetTcpiAccesslis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 6)
)
if mibBuilder.loadTexts:
    setTcpiAccesslis.setStatus("mandatory")
_SetTcpiAccesslisCols_Object = MibTableRow
setTcpiAccesslisCols = _SetTcpiAccesslisCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 6, 1)
)
setTcpiAccesslisCols.setIndexNames(
    (0, "ELSA-MIB", "setTcpiAccesslisIpa"),
)
if mibBuilder.loadTexts:
    setTcpiAccesslisCols.setStatus("mandatory")
_SetTcpiAccesslisIpa_Type = IpAddress
_SetTcpiAccesslisIpa_Object = MibTableColumn
setTcpiAccesslisIpa = _SetTcpiAccesslisIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 6, 1, 1),
    _SetTcpiAccesslisIpa_Type()
)
setTcpiAccesslisIpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiAccesslisIpa.setStatus("mandatory")
_SetTcpiAccesslisIpn_Type = IpAddress
_SetTcpiAccesslisIpn_Object = MibTableColumn
setTcpiAccesslisIpn = _SetTcpiAccesslisIpn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 6, 1, 2),
    _SetTcpiAccesslisIpn_Type()
)
setTcpiAccesslisIpn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiAccesslisIpn.setStatus("mandatory")
_SetTcpiDnsdefaul_Type = IpAddress
_SetTcpiDnsdefaul_Object = MibScalar
setTcpiDnsdefaul = _SetTcpiDnsdefaul_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 7),
    _SetTcpiDnsdefaul_Type()
)
setTcpiDnsdefaul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiDnsdefaul.setStatus("mandatory")
_SetTcpiDnsbackup_Type = IpAddress
_SetTcpiDnsbackup_Object = MibScalar
setTcpiDnsbackup = _SetTcpiDnsbackup_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 8),
    _SetTcpiDnsbackup_Type()
)
setTcpiDnsbackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiDnsbackup.setStatus("mandatory")
_SetTcpiNbnsdefau_Type = IpAddress
_SetTcpiNbnsdefau_Object = MibScalar
setTcpiNbnsdefau = _SetTcpiNbnsdefau_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 9),
    _SetTcpiNbnsdefau_Type()
)
setTcpiNbnsdefau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiNbnsdefau.setStatus("mandatory")
_SetTcpiNbnsbacku_Type = IpAddress
_SetTcpiNbnsbacku_Object = MibScalar
setTcpiNbnsbacku = _SetTcpiNbnsbacku_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 10),
    _SetTcpiNbnsbacku_Type()
)
setTcpiNbnsbacku.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiNbnsbacku.setStatus("mandatory")
_SetTcpiArpagingm_Type = Integer32
_SetTcpiArpagingm_Object = MibScalar
setTcpiArpagingm = _SetTcpiArpagingm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 11),
    _SetTcpiArpagingm_Type()
)
setTcpiArpagingm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiArpagingm.setStatus("mandatory")
_SetTcpiTcpagingm_Type = Integer32
_SetTcpiTcpagingm_Object = MibScalar
setTcpiTcpagingm = _SetTcpiTcpagingm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 12),
    _SetTcpiTcpagingm_Type()
)
setTcpiTcpagingm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiTcpagingm.setStatus("mandatory")
_SetTcpiTcpmaxcon_Type = Integer32
_SetTcpiTcpmaxcon_Object = MibScalar
setTcpiTcpmaxcon = _SetTcpiTcpmaxcon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 13),
    _SetTcpiTcpmaxcon_Type()
)
setTcpiTcpmaxcon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTcpiTcpmaxcon.setStatus("mandatory")
_SetTcpiTablearp_Object = MibTable
setTcpiTablearp = _SetTcpiTablearp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 16)
)
if mibBuilder.loadTexts:
    setTcpiTablearp.setStatus("mandatory")
_SetTcpiTablearpCols_Object = MibTableRow
setTcpiTablearpCols = _SetTcpiTablearpCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 16, 1)
)
setTcpiTablearpCols.setIndexNames(
    (0, "ELSA-MIB", "setTcpiTablearpIpa"),
)
if mibBuilder.loadTexts:
    setTcpiTablearpCols.setStatus("mandatory")
_SetTcpiTablearpIpa_Type = IpAddress
_SetTcpiTablearpIpa_Object = MibTableColumn
setTcpiTablearpIpa = _SetTcpiTablearpIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 16, 1, 1),
    _SetTcpiTablearpIpa_Type()
)
setTcpiTablearpIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setTcpiTablearpIpa.setStatus("mandatory")
_SetTcpiTablearpNod_Type = DisplayString
_SetTcpiTablearpNod_Object = MibTableColumn
setTcpiTablearpNod = _SetTcpiTablearpNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 16, 1, 2),
    _SetTcpiTablearpNod_Type()
)
setTcpiTablearpNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setTcpiTablearpNod.setStatus("mandatory")
_SetTcpiTablearpLas_Type = Integer32
_SetTcpiTablearpLas_Object = MibTableColumn
setTcpiTablearpLas = _SetTcpiTablearpLas_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 16, 1, 3),
    _SetTcpiTablearpLas_Type()
)
setTcpiTablearpLas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setTcpiTablearpLas.setStatus("mandatory")


class _SetTcpiTablearpCon_Type(Integer32):
    """Custom type setTcpiTablearpCon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("remote", 1))
    )


_SetTcpiTablearpCon_Type.__name__ = "Integer32"
_SetTcpiTablearpCon_Object = MibTableColumn
setTcpiTablearpCon = _SetTcpiTablearpCon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 7, 16, 1, 4),
    _SetTcpiTablearpCon_Type()
)
setTcpiTablearpCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setTcpiTablearpCon.setStatus("mandatory")
_SetIpro_ObjectIdentity = ObjectIdentity
setIpro = _SetIpro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8)
)


class _SetIproOpe_Type(Integer32):
    """Custom type setIproOpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetIproOpe_Type.__name__ = "Integer32"
_SetIproOpe_Object = MibScalar
setIproOpe = _SetIproOpe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 1),
    _SetIproOpe_Type()
)
setIproOpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproOpe.setStatus("mandatory")
_SetIproIpr_Object = MibTable
setIproIpr = _SetIproIpr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 2)
)
if mibBuilder.loadTexts:
    setIproIpr.setStatus("mandatory")
_SetIproIprCols_Object = MibTableRow
setIproIprCols = _SetIproIprCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 2, 1)
)
setIproIprCols.setIndexNames(
    (0, "ELSA-MIB", "setIproIprIpa"),
)
if mibBuilder.loadTexts:
    setIproIprCols.setStatus("mandatory")
_SetIproIprIpa_Type = IpAddress
_SetIproIprIpa_Object = MibTableColumn
setIproIprIpa = _SetIproIprIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 2, 1, 1),
    _SetIproIprIpa_Type()
)
setIproIprIpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproIprIpa.setStatus("mandatory")
_SetIproIprIpn_Type = IpAddress
_SetIproIprIpn_Object = MibTableColumn
setIproIprIpn = _SetIproIprIpn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 2, 1, 2),
    _SetIproIprIpn_Type()
)
setIproIprIpn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproIprIpn.setStatus("mandatory")
_SetIproIprRou_Type = DisplayString
_SetIproIprRou_Object = MibTableColumn
setIproIprRou = _SetIproIprRou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 2, 1, 3),
    _SetIproIprRou_Type()
)
setIproIprRou.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproIprRou.setStatus("mandatory")
_SetIproIprDis_Type = Integer32
_SetIproIprDis_Object = MibTableColumn
setIproIprDis = _SetIproIprDis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 2, 1, 4),
    _SetIproIprDis_Type()
)
setIproIprDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproIprDis.setStatus("mandatory")


class _SetIproIprMas_Type(Integer32):
    """Custom type setIproIprMas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("static", 2))
    )


_SetIproIprMas_Type.__name__ = "Integer32"
_SetIproIprMas_Object = MibTableColumn
setIproIprMas = _SetIproIprMas_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 2, 1, 5),
    _SetIproIprMas_Type()
)
setIproIprMas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproIprMas.setStatus("mandatory")


class _SetIproPro_Type(Integer32):
    """Custom type setIproPro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetIproPro_Type.__name__ = "Integer32"
_SetIproPro_Object = MibScalar
setIproPro = _SetIproPro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 5),
    _SetIproPro_Type()
)
setIproPro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproPro.setStatus("mandatory")


class _SetIproLoc_Type(Integer32):
    """Custom type setIproLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetIproLoc_Type.__name__ = "Integer32"
_SetIproLoc_Object = MibScalar
setIproLoc = _SetIproLoc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 6),
    _SetIproLoc_Type()
)
setIproLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproLoc.setStatus("mandatory")
_SetIproRou_ObjectIdentity = ObjectIdentity
setIproRou = _SetIproRou_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 7)
)


class _SetIproRouRou_Type(Integer32):
    """Custom type setIproRouRou based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("type-of-service", 1))
    )


_SetIproRouRou_Type.__name__ = "Integer32"
_SetIproRouRou_Object = MibScalar
setIproRouRou = _SetIproRouRou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 7, 1),
    _SetIproRouRou_Type()
)
setIproRouRou.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproRouRou.setStatus("mandatory")


class _SetIproRouIcm_Type(Integer32):
    """Custom type setIproRouIcm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reliable", 1))
    )


_SetIproRouIcm_Type.__name__ = "Integer32"
_SetIproRouIcm_Object = MibScalar
setIproRouIcm = _SetIproRouIcm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 7, 2),
    _SetIproRouIcm_Type()
)
setIproRouIcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproRouIcm.setStatus("mandatory")
_SetIproRip_ObjectIdentity = ObjectIdentity
setIproRip = _SetIproRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 8)
)


class _SetIproRipRip_Type(Integer32):
    """Custom type setIproRipRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("r1-comp", 2),
          ("rip-1", 1),
          ("rip-2", 3))
    )


_SetIproRipRip_Type.__name__ = "Integer32"
_SetIproRipRip_Object = MibScalar
setIproRipRip = _SetIproRipRip_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 8, 1),
    _SetIproRipRip_Type()
)
setIproRipRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproRipRip.setStatus("mandatory")


class _SetIproRipR1m_Type(Integer32):
    """Custom type setIproRipR1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("address", 1),
          ("cl-and-addr", 2),
          ("class", 0))
    )


_SetIproRipR1m_Type.__name__ = "Integer32"
_SetIproRipR1m_Object = MibScalar
setIproRipR1m = _SetIproRipR1m_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 8, 2),
    _SetIproRipR1m_Type()
)
setIproRipR1m.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproRipR1m.setStatus("mandatory")
_SetIproRipTab_Object = MibTable
setIproRipTab = _SetIproRipTab_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 8, 3)
)
if mibBuilder.loadTexts:
    setIproRipTab.setStatus("mandatory")
_SetIproRipTabCols_Object = MibTableRow
setIproRipTabCols = _SetIproRipTabCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 8, 3, 1)
)
setIproRipTabCols.setIndexNames(
    (0, "ELSA-MIB", "setIproRipTabIpa"),
)
if mibBuilder.loadTexts:
    setIproRipTabCols.setStatus("mandatory")
_SetIproRipTabIpa_Type = IpAddress
_SetIproRipTabIpa_Object = MibTableColumn
setIproRipTabIpa = _SetIproRipTabIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 8, 3, 1, 1),
    _SetIproRipTabIpa_Type()
)
setIproRipTabIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproRipTabIpa.setStatus("mandatory")
_SetIproRipTabIpn_Type = IpAddress
_SetIproRipTabIpn_Object = MibTableColumn
setIproRipTabIpn = _SetIproRipTabIpn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 8, 3, 1, 2),
    _SetIproRipTabIpn_Type()
)
setIproRipTabIpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproRipTabIpn.setStatus("mandatory")
_SetIproRipTabTim_Type = Integer32
_SetIproRipTabTim_Object = MibTableColumn
setIproRipTabTim = _SetIproRipTabTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 8, 3, 1, 3),
    _SetIproRipTabTim_Type()
)
setIproRipTabTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproRipTabTim.setStatus("mandatory")
_SetIproRipTabDis_Type = Integer32
_SetIproRipTabDis_Object = MibTableColumn
setIproRipTabDis = _SetIproRipTabDis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 8, 3, 1, 4),
    _SetIproRipTabDis_Type()
)
setIproRipTabDis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproRipTabDis.setStatus("mandatory")
_SetIproRipTabRou_Type = DisplayString
_SetIproRipTabRou_Object = MibTableColumn
setIproRipTabRou = _SetIproRipTabRou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 8, 3, 1, 5),
    _SetIproRipTabRou_Type()
)
setIproRipTabRou.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproRipTabRou.setStatus("mandatory")
_SetIproMas_ObjectIdentity = ObjectIdentity
setIproMas = _SetIproMas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9)
)
_SetIproMasTcpagings_Type = Integer32
_SetIproMasTcpagings_Object = MibScalar
setIproMasTcpagings = _SetIproMasTcpagings_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 1),
    _SetIproMasTcpagings_Type()
)
setIproMasTcpagings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproMasTcpagings.setStatus("mandatory")
_SetIproMasUdpagings_Type = Integer32
_SetIproMasUdpagings_Object = MibScalar
setIproMasUdpagings = _SetIproMasUdpagings_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 2),
    _SetIproMasUdpagings_Type()
)
setIproMasUdpagings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproMasUdpagings.setStatus("mandatory")
_SetIproMasIcmpaging_Type = Integer32
_SetIproMasIcmpaging_Object = MibScalar
setIproMasIcmpaging = _SetIproMasIcmpaging_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 3),
    _SetIproMasIcmpaging_Type()
)
setIproMasIcmpaging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproMasIcmpaging.setStatus("mandatory")
_SetIproMasServiceta_Object = MibTable
setIproMasServiceta = _SetIproMasServiceta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 4)
)
if mibBuilder.loadTexts:
    setIproMasServiceta.setStatus("mandatory")
_SetIproMasServicetaCols_Object = MibTableRow
setIproMasServicetaCols = _SetIproMasServicetaCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 4, 1)
)
setIproMasServicetaCols.setIndexNames(
    (0, "ELSA-MIB", "setIproMasServicetaDpo"),
)
if mibBuilder.loadTexts:
    setIproMasServicetaCols.setStatus("mandatory")
_SetIproMasServicetaDpo_Type = Integer32
_SetIproMasServicetaDpo_Object = MibTableColumn
setIproMasServicetaDpo = _SetIproMasServicetaDpo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 4, 1, 1),
    _SetIproMasServicetaDpo_Type()
)
setIproMasServicetaDpo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproMasServicetaDpo.setStatus("mandatory")
_SetIproMasServicetaInt_Type = IpAddress
_SetIproMasServicetaInt_Object = MibTableColumn
setIproMasServicetaInt = _SetIproMasServicetaInt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 4, 1, 2),
    _SetIproMasServicetaInt_Type()
)
setIproMasServicetaInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproMasServicetaInt.setStatus("mandatory")
_SetIproMasTablemasq_Object = MibTable
setIproMasTablemasq = _SetIproMasTablemasq_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 5)
)
if mibBuilder.loadTexts:
    setIproMasTablemasq.setStatus("mandatory")
_SetIproMasTablemasqCols_Object = MibTableRow
setIproMasTablemasqCols = _SetIproMasTablemasqCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 5, 1)
)
setIproMasTablemasqCols.setIndexNames(
    (0, "ELSA-MIB", "setIproMasTablemasqInt"),
)
if mibBuilder.loadTexts:
    setIproMasTablemasqCols.setStatus("mandatory")
_SetIproMasTablemasqInt_Type = IpAddress
_SetIproMasTablemasqInt_Object = MibTableColumn
setIproMasTablemasqInt = _SetIproMasTablemasqInt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 5, 1, 1),
    _SetIproMasTablemasqInt_Type()
)
setIproMasTablemasqInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproMasTablemasqInt.setStatus("mandatory")
_SetIproMasTablemasqSpo_Type = Integer32
_SetIproMasTablemasqSpo_Object = MibTableColumn
setIproMasTablemasqSpo = _SetIproMasTablemasqSpo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 5, 1, 2),
    _SetIproMasTablemasqSpo_Type()
)
setIproMasTablemasqSpo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproMasTablemasqSpo.setStatus("mandatory")


class _SetIproMasTablemasqPro_Type(Integer32):
    """Custom type setIproMasTablemasqPro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 4),
          ("tcp", 1),
          ("udp", 2))
    )


_SetIproMasTablemasqPro_Type.__name__ = "Integer32"
_SetIproMasTablemasqPro_Object = MibTableColumn
setIproMasTablemasqPro = _SetIproMasTablemasqPro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 5, 1, 3),
    _SetIproMasTablemasqPro_Type()
)
setIproMasTablemasqPro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproMasTablemasqPro.setStatus("mandatory")
_SetIproMasTablemasqTim_Type = Integer32
_SetIproMasTablemasqTim_Object = MibTableColumn
setIproMasTablemasqTim = _SetIproMasTablemasqTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 5, 1, 4),
    _SetIproMasTablemasqTim_Type()
)
setIproMasTablemasqTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproMasTablemasqTim.setStatus("mandatory")


class _SetIproMasFragments_Type(Integer32):
    """Custom type setIproMasFragments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("reassemble", 2),
          ("route", 1))
    )


_SetIproMasFragments_Type.__name__ = "Integer32"
_SetIproMasFragments_Object = MibScalar
setIproMasFragments = _SetIproMasFragments_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 6),
    _SetIproMasFragments_Type()
)
setIproMasFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproMasFragments.setStatus("mandatory")
_SetIproMasFragmenta_Type = Integer32
_SetIproMasFragmenta_Object = MibScalar
setIproMasFragmenta = _SetIproMasFragmenta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 9, 7),
    _SetIproMasFragmenta_Type()
)
setIproMasFragmenta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproMasFragmenta.setStatus("mandatory")
_SetIproFir_ObjectIdentity = ObjectIdentity
setIproFir = _SetIproFir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10)
)
_SetIproFirObj_Object = MibTable
setIproFirObj = _SetIproFirObj_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 1)
)
if mibBuilder.loadTexts:
    setIproFirObj.setStatus("mandatory")
_SetIproFirObjCols_Object = MibTableRow
setIproFirObjCols = _SetIproFirObjCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 1, 1)
)
setIproFirObjCols.setIndexNames(
    (0, "ELSA-MIB", "setIproFirObjNam"),
)
if mibBuilder.loadTexts:
    setIproFirObjCols.setStatus("mandatory")
_SetIproFirObjNam_Type = DisplayString
_SetIproFirObjNam_Object = MibTableColumn
setIproFirObjNam = _SetIproFirObjNam_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 1, 1, 1),
    _SetIproFirObjNam_Type()
)
setIproFirObjNam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproFirObjNam.setStatus("mandatory")
_SetIproFirObjDes_Type = DisplayString
_SetIproFirObjDes_Object = MibTableColumn
setIproFirObjDes = _SetIproFirObjDes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 1, 1, 2),
    _SetIproFirObjDes_Type()
)
setIproFirObjDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproFirObjDes.setStatus("mandatory")
_SetIproFirRul_Object = MibTable
setIproFirRul = _SetIproFirRul_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 2)
)
if mibBuilder.loadTexts:
    setIproFirRul.setStatus("mandatory")
_SetIproFirRulCols_Object = MibTableRow
setIproFirRulCols = _SetIproFirRulCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 2, 1)
)
setIproFirRulCols.setIndexNames(
    (0, "ELSA-MIB", "setIproFirRulNam"),
)
if mibBuilder.loadTexts:
    setIproFirRulCols.setStatus("mandatory")
_SetIproFirRulNam_Type = DisplayString
_SetIproFirRulNam_Object = MibTableColumn
setIproFirRulNam = _SetIproFirRulNam_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 2, 1, 1),
    _SetIproFirRulNam_Type()
)
setIproFirRulNam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproFirRulNam.setStatus("mandatory")
_SetIproFirRulPro_Type = DisplayString
_SetIproFirRulPro_Object = MibTableColumn
setIproFirRulPro = _SetIproFirRulPro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 2, 1, 2),
    _SetIproFirRulPro_Type()
)
setIproFirRulPro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproFirRulPro.setStatus("mandatory")
_SetIproFirRulSou_Type = DisplayString
_SetIproFirRulSou_Object = MibTableColumn
setIproFirRulSou = _SetIproFirRulSou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 2, 1, 3),
    _SetIproFirRulSou_Type()
)
setIproFirRulSou.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproFirRulSou.setStatus("mandatory")
_SetIproFirRulDes_Type = DisplayString
_SetIproFirRulDes_Object = MibTableColumn
setIproFirRulDes = _SetIproFirRulDes_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 2, 1, 4),
    _SetIproFirRulDes_Type()
)
setIproFirRulDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproFirRulDes.setStatus("mandatory")


class _SetIproFirRulAct_Type(Integer32):
    """Custom type setIproFirRulAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("always-filt", 256),
          ("connect-filt", 512),
          ("internet-filt", 1024))
    )


_SetIproFirRulAct_Type.__name__ = "Integer32"
_SetIproFirRulAct_Object = MibTableColumn
setIproFirRulAct = _SetIproFirRulAct_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 2, 1, 5),
    _SetIproFirRulAct_Type()
)
setIproFirRulAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproFirRulAct.setStatus("mandatory")
_SetIproFirFil_Object = MibTable
setIproFirFil = _SetIproFirFil_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3)
)
if mibBuilder.loadTexts:
    setIproFirFil.setStatus("mandatory")
_SetIproFirFilCols_Object = MibTableRow
setIproFirFilCols = _SetIproFirFilCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1)
)
setIproFirFilCols.setIndexNames(
    (0, "ELSA-MIB", "setIproFirFilIdx"),
)
if mibBuilder.loadTexts:
    setIproFirFilCols.setStatus("mandatory")
_SetIproFirFilIdx_Type = Integer32
_SetIproFirFilIdx_Object = MibTableColumn
setIproFirFilIdx = _SetIproFirFilIdx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 1),
    _SetIproFirFilIdx_Type()
)
setIproFirFilIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilIdx.setStatus("mandatory")
_SetIproFirFilProt_Type = Integer32
_SetIproFirFilProt_Object = MibTableColumn
setIproFirFilProt = _SetIproFirFilProt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 2),
    _SetIproFirFilProt_Type()
)
setIproFirFilProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilProt.setStatus("mandatory")
_SetIproFirFilSrca_Type = IpAddress
_SetIproFirFilSrca_Object = MibTableColumn
setIproFirFilSrca = _SetIproFirFilSrca_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 3),
    _SetIproFirFilSrca_Type()
)
setIproFirFilSrca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilSrca.setStatus("mandatory")
_SetIproFirFilSrcn_Type = IpAddress
_SetIproFirFilSrcn_Object = MibTableColumn
setIproFirFilSrcn = _SetIproFirFilSrcn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 4),
    _SetIproFirFilSrcn_Type()
)
setIproFirFilSrcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilSrcn.setStatus("mandatory")
_SetIproFirFilSst_Type = Integer32
_SetIproFirFilSst_Object = MibTableColumn
setIproFirFilSst = _SetIproFirFilSst_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 5),
    _SetIproFirFilSst_Type()
)
setIproFirFilSst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilSst.setStatus("mandatory")
_SetIproFirFilSend_Type = Integer32
_SetIproFirFilSend_Object = MibTableColumn
setIproFirFilSend = _SetIproFirFilSend_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 6),
    _SetIproFirFilSend_Type()
)
setIproFirFilSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilSend.setStatus("mandatory")
_SetIproFirFilDsta_Type = IpAddress
_SetIproFirFilDsta_Object = MibTableColumn
setIproFirFilDsta = _SetIproFirFilDsta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 7),
    _SetIproFirFilDsta_Type()
)
setIproFirFilDsta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilDsta.setStatus("mandatory")
_SetIproFirFilDstn_Type = IpAddress
_SetIproFirFilDstn_Object = MibTableColumn
setIproFirFilDstn = _SetIproFirFilDstn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 8),
    _SetIproFirFilDstn_Type()
)
setIproFirFilDstn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilDstn.setStatus("mandatory")
_SetIproFirFilDst_Type = Integer32
_SetIproFirFilDst_Object = MibTableColumn
setIproFirFilDst = _SetIproFirFilDst_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 9),
    _SetIproFirFilDst_Type()
)
setIproFirFilDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilDst.setStatus("mandatory")
_SetIproFirFilDend_Type = Integer32
_SetIproFirFilDend_Object = MibTableColumn
setIproFirFilDend = _SetIproFirFilDend_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 10),
    _SetIproFirFilDend_Type()
)
setIproFirFilDend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilDend.setStatus("mandatory")


class _SetIproFirFilActi_Type(Integer32):
    """Custom type setIproFirFilActi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("always-filt", 256),
          ("connect-filt", 512),
          ("internet-filt", 1024))
    )


_SetIproFirFilActi_Type.__name__ = "Integer32"
_SetIproFirFilActi_Object = MibTableColumn
setIproFirFilActi = _SetIproFirFilActi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 10, 3, 1, 11),
    _SetIproFirFilActi_Type()
)
setIproFirFilActi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIproFirFilActi.setStatus("mandatory")
_SetIproDef_Object = MibTable
setIproDef = _SetIproDef_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 13)
)
if mibBuilder.loadTexts:
    setIproDef.setStatus("mandatory")
_SetIproDefCols_Object = MibTableRow
setIproDefCols = _SetIproDefCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 13, 1)
)
setIproDefCols.setIndexNames(
    (0, "ELSA-MIB", "setIproDefInd"),
)
if mibBuilder.loadTexts:
    setIproDefCols.setStatus("mandatory")
_SetIproDefInd_Type = Integer32
_SetIproDefInd_Object = MibTableColumn
setIproDefInd = _SetIproDefInd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 13, 1, 1),
    _SetIproDefInd_Type()
)
setIproDefInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproDefInd.setStatus("mandatory")
_SetIproDefDay_Type = Integer32
_SetIproDefDay_Object = MibTableColumn
setIproDefDay = _SetIproDefDay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 13, 1, 2),
    _SetIproDefDay_Type()
)
setIproDefDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproDefDay.setStatus("mandatory")
_SetIproDefSta_Type = DisplayString
_SetIproDefSta_Object = MibTableColumn
setIproDefSta = _SetIproDefSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 13, 1, 3),
    _SetIproDefSta_Type()
)
setIproDefSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproDefSta.setStatus("mandatory")
_SetIproDefSto_Type = DisplayString
_SetIproDefSto_Object = MibTableColumn
setIproDefSto = _SetIproDefSto_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 13, 1, 4),
    _SetIproDefSto_Type()
)
setIproDefSto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproDefSto.setStatus("mandatory")
_SetIproDefDev_Type = DisplayString
_SetIproDefDev_Object = MibTableColumn
setIproDefDev = _SetIproDefDev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 13, 1, 5),
    _SetIproDefDev_Type()
)
setIproDefDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproDefDev.setStatus("mandatory")


class _SetIproUsa_Type(Integer32):
    """Custom type setIproUsa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetIproUsa_Type.__name__ = "Integer32"
_SetIproUsa_Object = MibScalar
setIproUsa = _SetIproUsa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 8, 14),
    _SetIproUsa_Type()
)
setIproUsa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIproUsa.setStatus("mandatory")
_SetSnmp_ObjectIdentity = ObjectIdentity
setSnmp = _SetSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9)
)


class _SetSnmpSen_Type(Integer32):
    """Custom type setSnmpSen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SetSnmpSen_Type.__name__ = "Integer32"
_SetSnmpSen_Object = MibScalar
setSnmpSen = _SetSnmpSen_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 1),
    _SetSnmpSen_Type()
)
setSnmpSen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSnmpSen.setStatus("mandatory")
_SetSnmpIpt_Object = MibTable
setSnmpIpt = _SetSnmpIpt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 2)
)
if mibBuilder.loadTexts:
    setSnmpIpt.setStatus("mandatory")
_SetSnmpIptCols_Object = MibTableRow
setSnmpIptCols = _SetSnmpIptCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 2, 1)
)
setSnmpIptCols.setIndexNames(
    (0, "ELSA-MIB", "setSnmpIptTra"),
)
if mibBuilder.loadTexts:
    setSnmpIptCols.setStatus("mandatory")
_SetSnmpIptTra_Type = IpAddress
_SetSnmpIptTra_Object = MibTableColumn
setSnmpIptTra = _SetSnmpIptTra_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 2, 1, 1),
    _SetSnmpIptTra_Type()
)
setSnmpIptTra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSnmpIptTra.setStatus("mandatory")


class _SetSnmpAdm_Type(DisplayString):
    """Custom type setSnmpAdm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SetSnmpAdm_Type.__name__ = "DisplayString"
_SetSnmpAdm_Object = MibScalar
setSnmpAdm = _SetSnmpAdm_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 3),
    _SetSnmpAdm_Type()
)
setSnmpAdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSnmpAdm.setStatus("mandatory")


class _SetSnmpLoc_Type(DisplayString):
    """Custom type setSnmpLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SetSnmpLoc_Type.__name__ = "DisplayString"
_SetSnmpLoc_Object = MibScalar
setSnmpLoc = _SetSnmpLoc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 4),
    _SetSnmpLoc_Type()
)
setSnmpLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSnmpLoc.setStatus("mandatory")
_SetSnmpReg_Type = Integer32
_SetSnmpReg_Object = MibScalar
setSnmpReg = _SetSnmpReg_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 5),
    _SetSnmpReg_Type()
)
setSnmpReg.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    setSnmpReg.setStatus("mandatory")
_SetSnmpDel_Type = Integer32
_SetSnmpDel_Object = MibScalar
setSnmpDel = _SetSnmpDel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 6),
    _SetSnmpDel_Type()
)
setSnmpDel.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    setSnmpDel.setStatus("mandatory")
_SetSnmpMon_Object = MibTable
setSnmpMon = _SetSnmpMon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 7)
)
if mibBuilder.loadTexts:
    setSnmpMon.setStatus("mandatory")
_SetSnmpMonCols_Object = MibTableRow
setSnmpMonCols = _SetSnmpMonCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 7, 1)
)
setSnmpMonCols.setIndexNames(
    (0, "ELSA-MIB", "setSnmpMonIpa"),
)
if mibBuilder.loadTexts:
    setSnmpMonCols.setStatus("mandatory")
_SetSnmpMonIpa_Type = IpAddress
_SetSnmpMonIpa_Object = MibTableColumn
setSnmpMonIpa = _SetSnmpMonIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 7, 1, 1),
    _SetSnmpMonIpa_Type()
)
setSnmpMonIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setSnmpMonIpa.setStatus("mandatory")
_SetSnmpMonPor_Type = Integer32
_SetSnmpMonPor_Object = MibTableColumn
setSnmpMonPor = _SetSnmpMonPor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 7, 1, 2),
    _SetSnmpMonPor_Type()
)
setSnmpMonPor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setSnmpMonPor.setStatus("mandatory")
_SetSnmpMonTim_Type = Integer32
_SetSnmpMonTim_Object = MibTableColumn
setSnmpMonTim = _SetSnmpMonTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 7, 1, 3),
    _SetSnmpMonTim_Type()
)
setSnmpMonTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setSnmpMonTim.setStatus("mandatory")
_SetSnmpMonMac_Type = DisplayString
_SetSnmpMonMac_Object = MibTableColumn
setSnmpMonMac = _SetSnmpMonMac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 7, 1, 4),
    _SetSnmpMonMac_Type()
)
setSnmpMonMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setSnmpMonMac.setStatus("mandatory")
_SetSnmpMonDev_Type = DisplayString
_SetSnmpMonDev_Object = MibTableColumn
setSnmpMonDev = _SetSnmpMonDev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 7, 1, 5),
    _SetSnmpMonDev_Type()
)
setSnmpMonDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setSnmpMonDev.setStatus("mandatory")


class _SetSnmpPas_Type(Integer32):
    """Custom type setSnmpPas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetSnmpPas_Type.__name__ = "Integer32"
_SetSnmpPas_Object = MibScalar
setSnmpPas = _SetSnmpPas_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 9, 10),
    _SetSnmpPas_Type()
)
setSnmpPas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSnmpPas.setStatus("mandatory")
_SetDhcp_ObjectIdentity = ObjectIdentity
setDhcp = _SetDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10)
)


class _SetDhcpOpe_Type(Integer32):
    """Custom type setDhcpOpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("off", 0),
          ("on", 1),
          ("relay", 16))
    )


_SetDhcpOpe_Type.__name__ = "Integer32"
_SetDhcpOpe_Object = MibScalar
setDhcpOpe = _SetDhcpOpe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 1),
    _SetDhcpOpe_Type()
)
setDhcpOpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpOpe.setStatus("mandatory")
_SetDhcpSta_Type = IpAddress
_SetDhcpSta_Object = MibScalar
setDhcpSta = _SetDhcpSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 2),
    _SetDhcpSta_Type()
)
setDhcpSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpSta.setStatus("mandatory")
_SetDhcpEnd_Type = IpAddress
_SetDhcpEnd_Object = MibScalar
setDhcpEnd = _SetDhcpEnd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 3),
    _SetDhcpEnd_Type()
)
setDhcpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpEnd.setStatus("mandatory")
_SetDhcpNet_Type = IpAddress
_SetDhcpNet_Object = MibScalar
setDhcpNet = _SetDhcpNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 4),
    _SetDhcpNet_Type()
)
setDhcpNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpNet.setStatus("mandatory")
_SetDhcpBro_Type = IpAddress
_SetDhcpBro_Object = MibScalar
setDhcpBro = _SetDhcpBro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 5),
    _SetDhcpBro_Type()
)
setDhcpBro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpBro.setStatus("mandatory")
_SetDhcpMax_Type = Integer32
_SetDhcpMax_Object = MibScalar
setDhcpMax = _SetDhcpMax_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 6),
    _SetDhcpMax_Type()
)
setDhcpMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpMax.setStatus("mandatory")
_SetDhcpDef_Type = Integer32
_SetDhcpDef_Object = MibScalar
setDhcpDef = _SetDhcpDef_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 7),
    _SetDhcpDef_Type()
)
setDhcpDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpDef.setStatus("mandatory")
_SetDhcpTab_Object = MibTable
setDhcpTab = _SetDhcpTab_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 8)
)
if mibBuilder.loadTexts:
    setDhcpTab.setStatus("mandatory")
_SetDhcpTabCols_Object = MibTableRow
setDhcpTabCols = _SetDhcpTabCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 8, 1)
)
setDhcpTabCols.setIndexNames(
    (0, "ELSA-MIB", "setDhcpTabIpa"),
)
if mibBuilder.loadTexts:
    setDhcpTabCols.setStatus("mandatory")
_SetDhcpTabIpa_Type = IpAddress
_SetDhcpTabIpa_Object = MibTableColumn
setDhcpTabIpa = _SetDhcpTabIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 8, 1, 1),
    _SetDhcpTabIpa_Type()
)
setDhcpTabIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDhcpTabIpa.setStatus("mandatory")
_SetDhcpTabNod_Type = DisplayString
_SetDhcpTabNod_Object = MibTableColumn
setDhcpTabNod = _SetDhcpTabNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 8, 1, 2),
    _SetDhcpTabNod_Type()
)
setDhcpTabNod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDhcpTabNod.setStatus("mandatory")
_SetDhcpTabTim_Type = Integer32
_SetDhcpTabTim_Object = MibTableColumn
setDhcpTabTim = _SetDhcpTabTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 8, 1, 3),
    _SetDhcpTabTim_Type()
)
setDhcpTabTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDhcpTabTim.setStatus("mandatory")
_SetDhcpTabHos_Type = DisplayString
_SetDhcpTabHos_Object = MibTableColumn
setDhcpTabHos = _SetDhcpTabHos_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 8, 1, 4),
    _SetDhcpTabHos_Type()
)
setDhcpTabHos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDhcpTabHos.setStatus("mandatory")


class _SetDhcpTabTyp_Type(Integer32):
    """Custom type setDhcpTabTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8,
              16,
              32,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 32),
          ("dyn", 16),
          ("new", 2),
          ("relay", 2048),
          ("stat", 8),
          ("unkn", 4))
    )


_SetDhcpTabTyp_Type.__name__ = "Integer32"
_SetDhcpTabTyp_Object = MibTableColumn
setDhcpTabTyp = _SetDhcpTabTyp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 8, 1, 5),
    _SetDhcpTabTyp_Type()
)
setDhcpTabTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDhcpTabTyp.setStatus("mandatory")
_SetDhcpHos_Object = MibTable
setDhcpHos = _SetDhcpHos_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 9)
)
if mibBuilder.loadTexts:
    setDhcpHos.setStatus("mandatory")
_SetDhcpHosCols_Object = MibTableRow
setDhcpHosCols = _SetDhcpHosCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 9, 1)
)
setDhcpHosCols.setIndexNames(
    (0, "ELSA-MIB", "setDhcpHosNod"),
)
if mibBuilder.loadTexts:
    setDhcpHosCols.setStatus("mandatory")
_SetDhcpHosNod_Type = DisplayString
_SetDhcpHosNod_Object = MibTableColumn
setDhcpHosNod = _SetDhcpHosNod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 9, 1, 1),
    _SetDhcpHosNod_Type()
)
setDhcpHosNod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpHosNod.setStatus("mandatory")
_SetDhcpHosIpa_Type = IpAddress
_SetDhcpHosIpa_Object = MibTableColumn
setDhcpHosIpa = _SetDhcpHosIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 9, 1, 2),
    _SetDhcpHosIpa_Type()
)
setDhcpHosIpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpHosIpa.setStatus("mandatory")
_SetDhcpHosHos_Type = DisplayString
_SetDhcpHosHos_Object = MibTableColumn
setDhcpHosHos = _SetDhcpHosHos_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 9, 1, 3),
    _SetDhcpHosHos_Type()
)
setDhcpHosHos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpHosHos.setStatus("mandatory")
_SetDhcpHosIma_Type = DisplayString
_SetDhcpHosIma_Object = MibTableColumn
setDhcpHosIma = _SetDhcpHosIma_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 9, 1, 4),
    _SetDhcpHosIma_Type()
)
setDhcpHosIma.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpHosIma.setStatus("mandatory")
_SetDhcpAli_Object = MibTable
setDhcpAli = _SetDhcpAli_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 10)
)
if mibBuilder.loadTexts:
    setDhcpAli.setStatus("mandatory")
_SetDhcpAliCols_Object = MibTableRow
setDhcpAliCols = _SetDhcpAliCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 10, 1)
)
setDhcpAliCols.setIndexNames(
    (0, "ELSA-MIB", "setDhcpAliImagea"),
)
if mibBuilder.loadTexts:
    setDhcpAliCols.setStatus("mandatory")
_SetDhcpAliImagea_Type = DisplayString
_SetDhcpAliImagea_Object = MibTableColumn
setDhcpAliImagea = _SetDhcpAliImagea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 10, 1, 1),
    _SetDhcpAliImagea_Type()
)
setDhcpAliImagea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpAliImagea.setStatus("mandatory")
_SetDhcpAliImagef_Type = DisplayString
_SetDhcpAliImagef_Object = MibTableColumn
setDhcpAliImagef = _SetDhcpAliImagef_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 10, 1, 2),
    _SetDhcpAliImagef_Type()
)
setDhcpAliImagef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpAliImagef.setStatus("mandatory")
_SetDhcpAliImages_Type = IpAddress
_SetDhcpAliImages_Object = MibTableColumn
setDhcpAliImages = _SetDhcpAliImages_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 10, 1, 3),
    _SetDhcpAliImages_Type()
)
setDhcpAliImages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpAliImages.setStatus("mandatory")
_SetDhcpMas_Type = IpAddress
_SetDhcpMas_Object = MibScalar
setDhcpMas = _SetDhcpMas_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 12),
    _SetDhcpMas_Type()
)
setDhcpMas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpMas.setStatus("mandatory")


class _SetDhcpRep_Type(Integer32):
    """Custom type setDhcpRep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SetDhcpRep_Type.__name__ = "Integer32"
_SetDhcpRep_Object = MibScalar
setDhcpRep = _SetDhcpRep_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 13),
    _SetDhcpRep_Type()
)
setDhcpRep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpRep.setStatus("mandatory")
_SetDhcpGat_Type = IpAddress
_SetDhcpGat_Object = MibScalar
setDhcpGat = _SetDhcpGat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 14),
    _SetDhcpGat_Type()
)
setDhcpGat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpGat.setStatus("mandatory")


class _SetDhcpRel_Type(Integer32):
    """Custom type setDhcpRel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SetDhcpRel_Type.__name__ = "Integer32"
_SetDhcpRel_Object = MibScalar
setDhcpRel = _SetDhcpRel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 10, 15),
    _SetDhcpRel_Type()
)
setDhcpRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDhcpRel.setStatus("mandatory")
_SetConf_ObjectIdentity = ObjectIdentity
setConf = _SetConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 11)
)


class _SetConfLanc_Type(Integer32):
    """Custom type setConfLanc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("read", 4))
    )


_SetConfLanc_Type.__name__ = "Integer32"
_SetConfLanc_Object = MibScalar
setConfLanc = _SetConfLanc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 11, 1),
    _SetConfLanc_Type()
)
setConfLanc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setConfLanc.setStatus("mandatory")


class _SetConfWanc_Type(Integer32):
    """Custom type setConfWanc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 2),
          ("read", 8))
    )


_SetConfWanc_Type.__name__ = "Integer32"
_SetConfWanc_Object = MibScalar
setConfWanc = _SetConfWanc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 11, 2),
    _SetConfWanc_Type()
)
setConfWanc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setConfWanc.setStatus("mandatory")


class _SetConfPass_Type(Integer32):
    """Custom type setConfPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetConfPass_Type.__name__ = "Integer32"
_SetConfPass_Object = MibScalar
setConfPass = _SetConfPass_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 11, 3),
    _SetConfPass_Type()
)
setConfPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setConfPass.setStatus("mandatory")
_SetConfMaxi_Type = Integer32
_SetConfMaxi_Object = MibScalar
setConfMaxi = _SetConfMaxi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 11, 4),
    _SetConfMaxi_Type()
)
setConfMaxi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setConfMaxi.setStatus("mandatory")
_SetConfConf_Type = Integer32
_SetConfConf_Object = MibScalar
setConfConf = _SetConfConf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 11, 5),
    _SetConfConf_Type()
)
setConfConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setConfConf.setStatus("mandatory")


class _SetConfLang_Type(Integer32):
    """Custom type setConfLang based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deutsch", 2),
          ("english", 1))
    )


_SetConfLang_Type.__name__ = "Integer32"
_SetConfLang_Object = MibScalar
setConfLang = _SetConfLang_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 11, 6),
    _SetConfLang_Type()
)
setConfLang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setConfLang.setStatus("mandatory")
_SetConfLogi_Type = Integer32
_SetConfLogi_Object = MibScalar
setConfLogi = _SetConfLogi_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 11, 7),
    _SetConfLogi_Type()
)
setConfLogi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setConfLogi.setStatus("mandatory")
_SetConfLock_Type = Integer32
_SetConfLock_Object = MibScalar
setConfLock = _SetConfLock_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 11, 8),
    _SetConfLock_Type()
)
setConfLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setConfLock.setStatus("mandatory")


class _SetConfFarc_Type(DisplayString):
    """Custom type setConfFarc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SetConfFarc_Type.__name__ = "DisplayString"
_SetConfFarc_Object = MibScalar
setConfFarc = _SetConfFarc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 11, 9),
    _SetConfFarc_Type()
)
setConfFarc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setConfFarc.setStatus("mandatory")
_SetAbmo_ObjectIdentity = ObjectIdentity
setAbmo = _SetAbmo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12)
)
_SetAbmoPor_Object = MibTable
setAbmoPor = _SetAbmoPor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 1)
)
if mibBuilder.loadTexts:
    setAbmoPor.setStatus("mandatory")
_SetAbmoPorCols_Object = MibTableRow
setAbmoPorCols = _SetAbmoPorCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 1, 1)
)
setAbmoPorCols.setIndexNames(
    (0, "ELSA-MIB", "setAbmoPorPort"),
)
if mibBuilder.loadTexts:
    setAbmoPorCols.setStatus("mandatory")


class _SetAbmoPorPort_Type(Integer32):
    """Custom type setAbmoPorPort based on Integer32"""
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
        *(("ab-1", 1),
          ("ab-2", 2),
          ("ab-3", 3),
          ("ab-4", 4))
    )


_SetAbmoPorPort_Type.__name__ = "Integer32"
_SetAbmoPorPort_Object = MibTableColumn
setAbmoPorPort = _SetAbmoPorPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 1, 1, 1),
    _SetAbmoPorPort_Type()
)
setAbmoPorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAbmoPorPort.setStatus("mandatory")
_SetAbmoPorEazmsns_Type = DisplayString
_SetAbmoPorEazmsns_Object = MibTableColumn
setAbmoPorEazmsns = _SetAbmoPorEazmsns_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 1, 1, 3),
    _SetAbmoPorEazmsns_Type()
)
setAbmoPorEazmsns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPorEazmsns.setStatus("mandatory")


class _SetAbmoPorCapab_Type(Integer32):
    """Custom type setAbmoPorCapab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("a-3-1khz", 8),
          ("fax-g2-3", 4),
          ("modem", 2),
          ("speech", 1))
    )


_SetAbmoPorCapab_Type.__name__ = "Integer32"
_SetAbmoPorCapab_Object = MibTableColumn
setAbmoPorCapab = _SetAbmoPorCapab_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 1, 1, 5),
    _SetAbmoPorCapab_Type()
)
setAbmoPorCapab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPorCapab.setStatus("mandatory")
_SetAbmoPorMode_Type = Integer32
_SetAbmoPorMode_Object = MibTableColumn
setAbmoPorMode = _SetAbmoPorMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 1, 1, 6),
    _SetAbmoPorMode_Type()
)
setAbmoPorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPorMode.setStatus("mandatory")


class _SetAbmoPorClip_Type(Integer32):
    """Custom type setAbmoPorClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SetAbmoPorClip_Type.__name__ = "Integer32"
_SetAbmoPorClip_Object = MibTableColumn
setAbmoPorClip = _SetAbmoPorClip_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 1, 1, 7),
    _SetAbmoPorClip_Type()
)
setAbmoPorClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPorClip.setStatus("mandatory")
_SetAbmoPorAutodialf_Type = Integer32
_SetAbmoPorAutodialf_Object = MibTableColumn
setAbmoPorAutodialf = _SetAbmoPorAutodialf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 1, 1, 8),
    _SetAbmoPorAutodialf_Type()
)
setAbmoPorAutodialf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPorAutodialf.setStatus("mandatory")
_SetAbmoPorAutodialn_Type = DisplayString
_SetAbmoPorAutodialn_Object = MibTableColumn
setAbmoPorAutodialn = _SetAbmoPorAutodialn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 1, 1, 9),
    _SetAbmoPorAutodialn_Type()
)
setAbmoPorAutodialn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPorAutodialn.setStatus("mandatory")


class _SetAbmoPorDevice_Type(Integer32):
    """Custom type setAbmoPorDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("answ-mach", 4),
          ("combi", 5),
          ("fax", 2),
          ("modem", 3),
          ("none", 0),
          ("phone", 1))
    )


_SetAbmoPorDevice_Type.__name__ = "Integer32"
_SetAbmoPorDevice_Object = MibTableColumn
setAbmoPorDevice = _SetAbmoPorDevice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 1, 1, 10),
    _SetAbmoPorDevice_Type()
)
setAbmoPorDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPorDevice.setStatus("mandatory")


class _SetAbmoRin_Type(Integer32):
    """Custom type setAbmoRin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 4),
          ("paired", 2),
          ("single", 1))
    )


_SetAbmoRin_Type.__name__ = "Integer32"
_SetAbmoRin_Object = MibScalar
setAbmoRin = _SetAbmoRin_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 3),
    _SetAbmoRin_Type()
)
setAbmoRin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoRin.setStatus("mandatory")


class _SetAbmoCou_Type(Integer32):
    """Custom type setAbmoCou based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              30,
              31,
              32,
              33,
              34,
              39,
              41,
              43,
              44,
              45,
              46,
              47,
              49,
              81,
              90,
              351,
              352,
              353,
              357,
              358)
        )
    )
    namedValues = NamedValues(
        *(("austria", 43),
          ("belgium", 32),
          ("cyprus", 357),
          ("denmark", 45),
          ("finland", 358),
          ("france", 33),
          ("germany", 49),
          ("great-britain", 44),
          ("greece", 30),
          ("ireland", 353),
          ("italy", 39),
          ("japan", 81),
          ("luxembourg", 352),
          ("netherlands", 31),
          ("norway", 47),
          ("portugal", 351),
          ("spain", 34),
          ("sweden", 46),
          ("switzerland", 41),
          ("turkey", 90),
          ("united-states-of-america", 1))
    )


_SetAbmoCou_Type.__name__ = "Integer32"
_SetAbmoCou_Object = MibScalar
setAbmoCou = _SetAbmoCou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 5),
    _SetAbmoCou_Type()
)
setAbmoCou.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoCou.setStatus("mandatory")
_SetAbmoPub_Object = MibTable
setAbmoPub = _SetAbmoPub_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 6)
)
if mibBuilder.loadTexts:
    setAbmoPub.setStatus("mandatory")
_SetAbmoPubCols_Object = MibTableRow
setAbmoPubCols = _SetAbmoPubCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 6, 1)
)
setAbmoPubCols.setIndexNames(
    (0, "ELSA-MIB", "setAbmoPubPor"),
)
if mibBuilder.loadTexts:
    setAbmoPubCols.setStatus("mandatory")


class _SetAbmoPubPor_Type(Integer32):
    """Custom type setAbmoPubPor based on Integer32"""
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
        *(("ab-1", 1),
          ("ab-2", 2),
          ("ab-3", 3),
          ("ab-4", 4))
    )


_SetAbmoPubPor_Type.__name__ = "Integer32"
_SetAbmoPubPor_Object = MibTableColumn
setAbmoPubPor = _SetAbmoPubPor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 6, 1, 1),
    _SetAbmoPubPor_Type()
)
setAbmoPubPor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAbmoPubPor.setStatus("mandatory")


class _SetAbmoPubOff_Type(Integer32):
    """Custom type setAbmoPubOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("private", 1),
          ("public", 2))
    )


_SetAbmoPubOff_Type.__name__ = "Integer32"
_SetAbmoPubOff_Object = MibTableColumn
setAbmoPubOff = _SetAbmoPubOff_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 6, 1, 4),
    _SetAbmoPubOff_Type()
)
setAbmoPubOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPubOff.setStatus("mandatory")


class _SetAbmoPubFla_Type(Integer32):
    """Custom type setAbmoPubFla based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("private", 1),
          ("public", 2))
    )


_SetAbmoPubFla_Type.__name__ = "Integer32"
_SetAbmoPubFla_Object = MibTableColumn
setAbmoPubFla = _SetAbmoPubFla_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 6, 1, 5),
    _SetAbmoPubFla_Type()
)
setAbmoPubFla.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPubFla.setStatus("mandatory")
_SetAbmoPubExc_Type = DisplayString
_SetAbmoPubExc_Object = MibTableColumn
setAbmoPubExc = _SetAbmoPubExc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 6, 1, 6),
    _SetAbmoPubExc_Type()
)
setAbmoPubExc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPubExc.setStatus("mandatory")
_SetAbmoCla_Object = MibTable
setAbmoCla = _SetAbmoCla_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 7)
)
if mibBuilder.loadTexts:
    setAbmoCla.setStatus("mandatory")
_SetAbmoClaCols_Object = MibTableRow
setAbmoClaCols = _SetAbmoClaCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 7, 1)
)
setAbmoClaCols.setIndexNames(
    (0, "ELSA-MIB", "setAbmoClaPort"),
)
if mibBuilder.loadTexts:
    setAbmoClaCols.setStatus("mandatory")


class _SetAbmoClaPort_Type(Integer32):
    """Custom type setAbmoClaPort based on Integer32"""
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
        *(("ab-1", 1),
          ("ab-2", 2),
          ("ab-3", 3),
          ("ab-4", 4))
    )


_SetAbmoClaPort_Type.__name__ = "Integer32"
_SetAbmoClaPort_Object = MibTableColumn
setAbmoClaPort = _SetAbmoClaPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 7, 1, 1),
    _SetAbmoClaPort_Type()
)
setAbmoClaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAbmoClaPort.setStatus("mandatory")
_SetAbmoClaClassofservice_Type = Integer32
_SetAbmoClaClassofservice_Object = MibTableColumn
setAbmoClaClassofservice = _SetAbmoClaClassofservice_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 7, 1, 2),
    _SetAbmoClaClassofservice_Type()
)
setAbmoClaClassofservice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoClaClassofservice.setStatus("mandatory")
_SetAbmoClaBlockednumber1_Type = DisplayString
_SetAbmoClaBlockednumber1_Object = MibTableColumn
setAbmoClaBlockednumber1 = _SetAbmoClaBlockednumber1_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 7, 1, 3),
    _SetAbmoClaBlockednumber1_Type()
)
setAbmoClaBlockednumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoClaBlockednumber1.setStatus("mandatory")
_SetAbmoClaBlockednumber2_Type = DisplayString
_SetAbmoClaBlockednumber2_Object = MibTableColumn
setAbmoClaBlockednumber2 = _SetAbmoClaBlockednumber2_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 7, 1, 4),
    _SetAbmoClaBlockednumber2_Type()
)
setAbmoClaBlockednumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoClaBlockednumber2.setStatus("mandatory")
_SetAbmoPri_Object = MibTable
setAbmoPri = _SetAbmoPri_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 8)
)
if mibBuilder.loadTexts:
    setAbmoPri.setStatus("mandatory")
_SetAbmoPriCols_Object = MibTableRow
setAbmoPriCols = _SetAbmoPriCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 8, 1)
)
setAbmoPriCols.setIndexNames(
    (0, "ELSA-MIB", "setAbmoPriPor"),
)
if mibBuilder.loadTexts:
    setAbmoPriCols.setStatus("mandatory")


class _SetAbmoPriPor_Type(Integer32):
    """Custom type setAbmoPriPor based on Integer32"""
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
        *(("ab-1", 1),
          ("ab-2", 2),
          ("ab-3", 3),
          ("ab-4", 4))
    )


_SetAbmoPriPor_Type.__name__ = "Integer32"
_SetAbmoPriPor_Object = MibTableColumn
setAbmoPriPor = _SetAbmoPriPor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 8, 1, 1),
    _SetAbmoPriPor_Type()
)
setAbmoPriPor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAbmoPriPor.setStatus("mandatory")


class _SetAbmoPriPri_Type(Integer32):
    """Custom type setAbmoPriPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p1", 0),
          ("p2", 1),
          ("p3", 2))
    )


_SetAbmoPriPri_Type.__name__ = "Integer32"
_SetAbmoPriPri_Object = MibTableColumn
setAbmoPriPri = _SetAbmoPriPri_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 12, 8, 1, 3),
    _SetAbmoPriPri_Type()
)
setAbmoPriPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAbmoPriPri.setStatus("mandatory")
_SetLanc_ObjectIdentity = ObjectIdentity
setLanc = _SetLanc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13)
)
_SetLancAcces_Object = MibTable
setLancAcces = _SetLancAcces_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 1)
)
if mibBuilder.loadTexts:
    setLancAcces.setStatus("mandatory")
_SetLancAccesCols_Object = MibTableRow
setLancAccesCols = _SetLancAccesCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 1, 1)
)
setLancAccesCols.setIndexNames(
    (0, "ELSA-MIB", "setLancAccesIpa"),
)
if mibBuilder.loadTexts:
    setLancAccesCols.setStatus("mandatory")
_SetLancAccesIpa_Type = IpAddress
_SetLancAccesIpa_Object = MibTableColumn
setLancAccesIpa = _SetLancAccesIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 1, 1, 1),
    _SetLancAccesIpa_Type()
)
setLancAccesIpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLancAccesIpa.setStatus("mandatory")
_SetLancAccesIpn_Type = IpAddress
_SetLancAccesIpn_Object = MibTableColumn
setLancAccesIpn = _SetLancAccesIpn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 1, 1, 2),
    _SetLancAccesIpn_Type()
)
setLancAccesIpn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLancAccesIpn.setStatus("mandatory")


class _SetLancOpera_Type(Integer32):
    """Custom type setLancOpera based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dial-only", 2),
          ("off", 0),
          ("on", 1))
    )


_SetLancOpera_Type.__name__ = "Integer32"
_SetLancOpera_Object = MibScalar
setLancOpera = _SetLancOpera_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 2),
    _SetLancOpera_Type()
)
setLancOpera.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLancOpera.setStatus("mandatory")
_SetLancUdppo_Type = Integer32
_SetLancUdppo_Object = MibScalar
setLancUdppo = _SetLancUdppo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 3),
    _SetLancUdppo_Type()
)
setLancUdppo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLancUdppo.setStatus("mandatory")


class _SetLancEazms_Type(DisplayString):
    """Custom type setLancEazms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SetLancEazms_Type.__name__ = "DisplayString"
_SetLancEazms_Object = MibScalar
setLancEazms = _SetLancEazms_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 4),
    _SetLancEazms_Type()
)
setLancEazms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLancEazms.setStatus("mandatory")


class _SetLancPrioo_Type(Integer32):
    """Custom type setLancPrioo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p1", 0),
          ("p2", 1),
          ("p3", 2))
    )


_SetLancPrioo_Type.__name__ = "Integer32"
_SetLancPrioo_Object = MibScalar
setLancPrioo = _SetLancPrioo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 5),
    _SetLancPrioo_Type()
)
setLancPrioo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLancPrioo.setStatus("mandatory")
_SetLancInter_Object = MibTable
setLancInter = _SetLancInter_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 6)
)
if mibBuilder.loadTexts:
    setLancInter.setStatus("mandatory")
_SetLancInterCols_Object = MibTableRow
setLancInterCols = _SetLancInterCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 6, 1)
)
setLancInterCols.setIndexNames(
    (0, "ELSA-MIB", "setLancInterIfc"),
)
if mibBuilder.loadTexts:
    setLancInterCols.setStatus("mandatory")


class _SetLancInterIfc_Type(Integer32):
    """Custom type setLancInterIfc based on Integer32"""
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
        *(("s0-1", 1),
          ("s0-2", 2),
          ("s0-3", 3),
          ("s0-4", 4))
    )


_SetLancInterIfc_Type.__name__ = "Integer32"
_SetLancInterIfc_Object = MibTableColumn
setLancInterIfc = _SetLancInterIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 6, 1, 1),
    _SetLancInterIfc_Type()
)
setLancInterIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setLancInterIfc.setStatus("mandatory")


class _SetLancInterOpe_Type(Integer32):
    """Custom type setLancInterOpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dial-only", 2),
          ("off", 0),
          ("on", 1))
    )


_SetLancInterOpe_Type.__name__ = "Integer32"
_SetLancInterOpe_Object = MibTableColumn
setLancInterOpe = _SetLancInterOpe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 6, 1, 2),
    _SetLancInterOpe_Type()
)
setLancInterOpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLancInterOpe.setStatus("mandatory")
_SetLancInterEaz_Type = DisplayString
_SetLancInterEaz_Object = MibTableColumn
setLancInterEaz = _SetLancInterEaz_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 6, 1, 3),
    _SetLancInterEaz_Type()
)
setLancInterEaz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLancInterEaz.setStatus("mandatory")


class _SetLancInterFor_Type(Integer32):
    """Custom type setLancInterFor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SetLancInterFor_Type.__name__ = "Integer32"
_SetLancInterFor_Object = MibTableColumn
setLancInterFor = _SetLancInterFor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 6, 1, 5),
    _SetLancInterFor_Type()
)
setLancInterFor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLancInterFor.setStatus("mandatory")
_SetLancPrior_Object = MibTable
setLancPrior = _SetLancPrior_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 7)
)
if mibBuilder.loadTexts:
    setLancPrior.setStatus("mandatory")
_SetLancPriorCols_Object = MibTableRow
setLancPriorCols = _SetLancPriorCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 7, 1)
)
setLancPriorCols.setIndexNames(
    (0, "ELSA-MIB", "setLancPriorIfc"),
)
if mibBuilder.loadTexts:
    setLancPriorCols.setStatus("mandatory")


class _SetLancPriorIfc_Type(Integer32):
    """Custom type setLancPriorIfc based on Integer32"""
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
        *(("s0-1", 1),
          ("s0-2", 2),
          ("s0-3", 3),
          ("s0-4", 4))
    )


_SetLancPriorIfc_Type.__name__ = "Integer32"
_SetLancPriorIfc_Object = MibTableColumn
setLancPriorIfc = _SetLancPriorIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 7, 1, 1),
    _SetLancPriorIfc_Type()
)
setLancPriorIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setLancPriorIfc.setStatus("mandatory")


class _SetLancPriorPri_Type(Integer32):
    """Custom type setLancPriorPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p1", 0),
          ("p2", 1),
          ("p3", 2))
    )


_SetLancPriorPri_Type.__name__ = "Integer32"
_SetLancPriorPri_Object = MibTableColumn
setLancPriorPri = _SetLancPriorPri_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 13, 7, 1, 2),
    _SetLancPriorPri_Type()
)
setLancPriorPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLancPriorPri.setStatus("mandatory")
_SetTime_ObjectIdentity = ObjectIdentity
setTime = _SetTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 14)
)


class _SetTimeOpe_Type(Integer32):
    """Custom type setTimeOpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetTimeOpe_Type.__name__ = "Integer32"
_SetTimeOpe_Object = MibScalar
setTimeOpe = _SetTimeOpe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 14, 1),
    _SetTimeOpe_Type()
)
setTimeOpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTimeOpe.setStatus("mandatory")
_SetTimeCur_Type = DisplayString
_SetTimeCur_Object = MibScalar
setTimeCur = _SetTimeCur_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 14, 2),
    _SetTimeCur_Type()
)
setTimeCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setTimeCur.setStatus("mandatory")


class _SetTimeTim_Type(DisplayString):
    """Custom type setTimeTim based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_SetTimeTim_Type.__name__ = "DisplayString"
_SetTimeTim_Object = MibScalar
setTimeTim = _SetTimeTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 14, 3),
    _SetTimeTim_Type()
)
setTimeTim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTimeTim.setStatus("mandatory")
_SetTimeCal_Type = Integer32
_SetTimeCal_Object = MibScalar
setTimeCal = _SetTimeCal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 14, 5),
    _SetTimeCal_Type()
)
setTimeCal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setTimeCal.setStatus("mandatory")
_SetTimeUtc_Type = Integer32
_SetTimeUtc_Object = MibScalar
setTimeUtc = _SetTimeUtc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 14, 7),
    _SetTimeUtc_Type()
)
setTimeUtc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setTimeUtc.setStatus("mandatory")
_SetLcrm_ObjectIdentity = ObjectIdentity
setLcrm = _SetLcrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15)
)


class _SetLcrmRou_Type(Integer32):
    """Custom type setLcrmRou based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetLcrmRou_Type.__name__ = "Integer32"
_SetLcrmRou_Object = MibScalar
setLcrmRou = _SetLcrmRou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 1),
    _SetLcrmRou_Type()
)
setLcrmRou.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmRou.setStatus("mandatory")


class _SetLcrmLan_Type(Integer32):
    """Custom type setLcrmLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetLcrmLan_Type.__name__ = "Integer32"
_SetLcrmLan_Object = MibScalar
setLcrmLan = _SetLcrmLan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 2),
    _SetLcrmLan_Type()
)
setLcrmLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmLan.setStatus("mandatory")


class _SetLcrmAbp_Type(Integer32):
    """Custom type setLcrmAbp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetLcrmAbp_Type.__name__ = "Integer32"
_SetLcrmAbp_Object = MibScalar
setLcrmAbp = _SetLcrmAbp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 3),
    _SetLcrmAbp_Type()
)
setLcrmAbp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmAbp.setStatus("mandatory")
_SetLcrmTim_Object = MibTable
setLcrmTim = _SetLcrmTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 4)
)
if mibBuilder.loadTexts:
    setLcrmTim.setStatus("mandatory")
_SetLcrmTimCols_Object = MibTableRow
setLcrmTimCols = _SetLcrmTimCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 4, 1)
)
setLcrmTimCols.setIndexNames(
    (0, "ELSA-MIB", "setLcrmTimInd"),
)
if mibBuilder.loadTexts:
    setLcrmTimCols.setStatus("mandatory")
_SetLcrmTimInd_Type = Integer32
_SetLcrmTimInd_Object = MibTableColumn
setLcrmTimInd = _SetLcrmTimInd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 4, 1, 1),
    _SetLcrmTimInd_Type()
)
setLcrmTimInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmTimInd.setStatus("mandatory")
_SetLcrmTimPre_Type = DisplayString
_SetLcrmTimPre_Object = MibTableColumn
setLcrmTimPre = _SetLcrmTimPre_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 4, 1, 2),
    _SetLcrmTimPre_Type()
)
setLcrmTimPre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmTimPre.setStatus("mandatory")
_SetLcrmTimDay_Type = Integer32
_SetLcrmTimDay_Object = MibTableColumn
setLcrmTimDay = _SetLcrmTimDay_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 4, 1, 3),
    _SetLcrmTimDay_Type()
)
setLcrmTimDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmTimDay.setStatus("mandatory")
_SetLcrmTimSta_Type = DisplayString
_SetLcrmTimSta_Object = MibTableColumn
setLcrmTimSta = _SetLcrmTimSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 4, 1, 4),
    _SetLcrmTimSta_Type()
)
setLcrmTimSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmTimSta.setStatus("mandatory")
_SetLcrmTimSto_Type = DisplayString
_SetLcrmTimSto_Object = MibTableColumn
setLcrmTimSto = _SetLcrmTimSto_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 4, 1, 5),
    _SetLcrmTimSto_Type()
)
setLcrmTimSto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmTimSto.setStatus("mandatory")
_SetLcrmTimNum_Type = DisplayString
_SetLcrmTimNum_Object = MibTableColumn
setLcrmTimNum = _SetLcrmTimNum_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 4, 1, 6),
    _SetLcrmTimNum_Type()
)
setLcrmTimNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmTimNum.setStatus("mandatory")


class _SetLcrmTimFal_Type(Integer32):
    """Custom type setLcrmTimFal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetLcrmTimFal_Type.__name__ = "Integer32"
_SetLcrmTimFal_Object = MibTableColumn
setLcrmTimFal = _SetLcrmTimFal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 4, 1, 7),
    _SetLcrmTimFal_Type()
)
setLcrmTimFal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmTimFal.setStatus("mandatory")
_SetLcrmCel_Object = MibTable
setLcrmCel = _SetLcrmCel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 5)
)
if mibBuilder.loadTexts:
    setLcrmCel.setStatus("mandatory")
_SetLcrmCelCols_Object = MibTableRow
setLcrmCelCols = _SetLcrmCelCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 5, 1)
)
setLcrmCelCols.setIndexNames(
    (0, "ELSA-MIB", "setLcrmCelInd"),
)
if mibBuilder.loadTexts:
    setLcrmCelCols.setStatus("mandatory")
_SetLcrmCelInd_Type = Integer32
_SetLcrmCelInd_Object = MibTableColumn
setLcrmCelInd = _SetLcrmCelInd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 5, 1, 1),
    _SetLcrmCelInd_Type()
)
setLcrmCelInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setLcrmCelInd.setStatus("mandatory")
_SetLcrmCelDat_Type = DisplayString
_SetLcrmCelDat_Object = MibTableColumn
setLcrmCelDat = _SetLcrmCelDat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 15, 5, 1, 2),
    _SetLcrmCelDat_Type()
)
setLcrmCelDat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLcrmCelDat.setStatus("mandatory")
_SetNetb_ObjectIdentity = ObjectIdentity
setNetb = _SetNetb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16)
)


class _SetNetbOpe_Type(Integer32):
    """Custom type setNetbOpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetNetbOpe_Type.__name__ = "Integer32"
_SetNetbOpe_Object = MibScalar
setNetbOpe = _SetNetbOpe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 1),
    _SetNetbOpe_Type()
)
setNetbOpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setNetbOpe.setStatus("mandatory")


class _SetNetbSco_Type(DisplayString):
    """Custom type setNetbSco based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SetNetbSco_Type.__name__ = "DisplayString"
_SetNetbSco_Object = MibScalar
setNetbSco = _SetNetbSco_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 2),
    _SetNetbSco_Type()
)
setNetbSco.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setNetbSco.setStatus("mandatory")


class _SetNetbNtd_Type(DisplayString):
    """Custom type setNetbNtd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SetNetbNtd_Type.__name__ = "DisplayString"
_SetNetbNtd_Object = MibScalar
setNetbNtd = _SetNetbNtd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 3),
    _SetNetbNtd_Type()
)
setNetbNtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setNetbNtd.setStatus("mandatory")
_SetNetbRem_Object = MibTable
setNetbRem = _SetNetbRem_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 4)
)
if mibBuilder.loadTexts:
    setNetbRem.setStatus("mandatory")
_SetNetbRemCols_Object = MibTableRow
setNetbRemCols = _SetNetbRemCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 4, 1)
)
setNetbRemCols.setIndexNames(
    (0, "ELSA-MIB", "setNetbRemNam"),
)
if mibBuilder.loadTexts:
    setNetbRemCols.setStatus("mandatory")
_SetNetbRemNam_Type = DisplayString
_SetNetbRemNam_Object = MibTableColumn
setNetbRemNam = _SetNetbRemNam_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 4, 1, 1),
    _SetNetbRemNam_Type()
)
setNetbRemNam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setNetbRemNam.setStatus("mandatory")


class _SetNetbRemTyp_Type(Integer32):
    """Custom type setNetbRemTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("router", 0),
          ("workstation", 1))
    )


_SetNetbRemTyp_Type.__name__ = "Integer32"
_SetNetbRemTyp_Object = MibTableColumn
setNetbRemTyp = _SetNetbRemTyp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 4, 1, 3),
    _SetNetbRemTyp_Type()
)
setNetbRemTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setNetbRemTyp.setStatus("mandatory")
_SetNetbGro_Object = MibTable
setNetbGro = _SetNetbGro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 5)
)
if mibBuilder.loadTexts:
    setNetbGro.setStatus("mandatory")
_SetNetbGroCols_Object = MibTableRow
setNetbGroCols = _SetNetbGroCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 5, 1)
)
setNetbGroCols.setIndexNames(
    (0, "ELSA-MIB", "setNetbGroGro"),
)
if mibBuilder.loadTexts:
    setNetbGroCols.setStatus("mandatory")
_SetNetbGroGro_Type = DisplayString
_SetNetbGroGro_Object = MibTableColumn
setNetbGroGro = _SetNetbGroGro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 5, 1, 1),
    _SetNetbGroGro_Type()
)
setNetbGroGro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbGroGro.setStatus("mandatory")
_SetNetbGroTyp_Type = DisplayString
_SetNetbGroTyp_Object = MibTableColumn
setNetbGroTyp = _SetNetbGroTyp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 5, 1, 2),
    _SetNetbGroTyp_Type()
)
setNetbGroTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbGroTyp.setStatus("mandatory")
_SetNetbGroIpa_Type = IpAddress
_SetNetbGroIpa_Object = MibTableColumn
setNetbGroIpa = _SetNetbGroIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 5, 1, 3),
    _SetNetbGroIpa_Type()
)
setNetbGroIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbGroIpa.setStatus("mandatory")
_SetNetbGroRem_Type = DisplayString
_SetNetbGroRem_Object = MibTableColumn
setNetbGroRem = _SetNetbGroRem_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 5, 1, 4),
    _SetNetbGroRem_Type()
)
setNetbGroRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbGroRem.setStatus("mandatory")
_SetNetbGroTim_Type = Integer32
_SetNetbGroTim_Object = MibTableColumn
setNetbGroTim = _SetNetbGroTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 5, 1, 5),
    _SetNetbGroTim_Type()
)
setNetbGroTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbGroTim.setStatus("mandatory")
_SetNetbGroFla_Type = DisplayString
_SetNetbGroFla_Object = MibTableColumn
setNetbGroFla = _SetNetbGroFla_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 5, 1, 6),
    _SetNetbGroFla_Type()
)
setNetbGroFla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbGroFla.setStatus("mandatory")
_SetNetbHos_Object = MibTable
setNetbHos = _SetNetbHos_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 6)
)
if mibBuilder.loadTexts:
    setNetbHos.setStatus("mandatory")
_SetNetbHosCols_Object = MibTableRow
setNetbHosCols = _SetNetbHosCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 6, 1)
)
setNetbHosCols.setIndexNames(
    (0, "ELSA-MIB", "setNetbHosNam"),
)
if mibBuilder.loadTexts:
    setNetbHosCols.setStatus("mandatory")
_SetNetbHosNam_Type = DisplayString
_SetNetbHosNam_Object = MibTableColumn
setNetbHosNam = _SetNetbHosNam_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 6, 1, 1),
    _SetNetbHosNam_Type()
)
setNetbHosNam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbHosNam.setStatus("mandatory")
_SetNetbHosTyp_Type = DisplayString
_SetNetbHosTyp_Object = MibTableColumn
setNetbHosTyp = _SetNetbHosTyp_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 6, 1, 2),
    _SetNetbHosTyp_Type()
)
setNetbHosTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbHosTyp.setStatus("mandatory")
_SetNetbHosIpa_Type = IpAddress
_SetNetbHosIpa_Object = MibTableColumn
setNetbHosIpa = _SetNetbHosIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 6, 1, 3),
    _SetNetbHosIpa_Type()
)
setNetbHosIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbHosIpa.setStatus("mandatory")
_SetNetbHosRem_Type = DisplayString
_SetNetbHosRem_Object = MibTableColumn
setNetbHosRem = _SetNetbHosRem_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 6, 1, 4),
    _SetNetbHosRem_Type()
)
setNetbHosRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbHosRem.setStatus("mandatory")
_SetNetbHosTim_Type = Integer32
_SetNetbHosTim_Object = MibTableColumn
setNetbHosTim = _SetNetbHosTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 6, 1, 5),
    _SetNetbHosTim_Type()
)
setNetbHosTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbHosTim.setStatus("mandatory")
_SetNetbHosFla_Type = DisplayString
_SetNetbHosFla_Object = MibTableColumn
setNetbHosFla = _SetNetbHosFla_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 6, 1, 6),
    _SetNetbHosFla_Type()
)
setNetbHosFla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbHosFla.setStatus("mandatory")
_SetNetbSer_Object = MibTable
setNetbSer = _SetNetbSer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7)
)
if mibBuilder.loadTexts:
    setNetbSer.setStatus("mandatory")
_SetNetbSerCols_Object = MibTableRow
setNetbSerCols = _SetNetbSerCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1)
)
setNetbSerCols.setIndexNames(
    (0, "ELSA-MIB", "setNetbSerHos"),
)
if mibBuilder.loadTexts:
    setNetbSerCols.setStatus("mandatory")
_SetNetbSerHos_Type = DisplayString
_SetNetbSerHos_Object = MibTableColumn
setNetbSerHos = _SetNetbSerHos_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1, 1),
    _SetNetbSerHos_Type()
)
setNetbSerHos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbSerHos.setStatus("mandatory")
_SetNetbSerGro_Type = DisplayString
_SetNetbSerGro_Object = MibTableColumn
setNetbSerGro = _SetNetbSerGro_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1, 2),
    _SetNetbSerGro_Type()
)
setNetbSerGro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbSerGro.setStatus("mandatory")
_SetNetbSerUpd_Type = DisplayString
_SetNetbSerUpd_Object = MibTableColumn
setNetbSerUpd = _SetNetbSerUpd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1, 3),
    _SetNetbSerUpd_Type()
)
setNetbSerUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbSerUpd.setStatus("mandatory")
_SetNetbSerIpa_Type = DisplayString
_SetNetbSerIpa_Object = MibTableColumn
setNetbSerIpa = _SetNetbSerIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1, 4),
    _SetNetbSerIpa_Type()
)
setNetbSerIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbSerIpa.setStatus("mandatory")
_SetNetbSerOsv_Type = DisplayString
_SetNetbSerOsv_Object = MibTableColumn
setNetbSerOsv = _SetNetbSerOsv_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1, 5),
    _SetNetbSerOsv_Type()
)
setNetbSerOsv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbSerOsv.setStatus("mandatory")
_SetNetbSerSmb_Type = DisplayString
_SetNetbSerSmb_Object = MibTableColumn
setNetbSerSmb = _SetNetbSerSmb_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1, 6),
    _SetNetbSerSmb_Type()
)
setNetbSerSmb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbSerSmb.setStatus("mandatory")
_SetNetbSerSer_Type = DisplayString
_SetNetbSerSer_Object = MibTableColumn
setNetbSerSer = _SetNetbSerSer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1, 7),
    _SetNetbSerSer_Type()
)
setNetbSerSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbSerSer.setStatus("mandatory")
_SetNetbSerRem_Type = DisplayString
_SetNetbSerRem_Object = MibTableColumn
setNetbSerRem = _SetNetbSerRem_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1, 8),
    _SetNetbSerRem_Type()
)
setNetbSerRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbSerRem.setStatus("mandatory")
_SetNetbSerTim_Type = Integer32
_SetNetbSerTim_Object = MibTableColumn
setNetbSerTim = _SetNetbSerTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1, 9),
    _SetNetbSerTim_Type()
)
setNetbSerTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbSerTim.setStatus("mandatory")
_SetNetbSerFla_Type = DisplayString
_SetNetbSerFla_Object = MibTableColumn
setNetbSerFla = _SetNetbSerFla_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 7, 1, 10),
    _SetNetbSerFla_Type()
)
setNetbSerFla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNetbSerFla.setStatus("mandatory")


class _SetNetbWat_Type(Integer32):
    """Custom type setNetbWat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("route", 0),
          ("spoof", 1))
    )


_SetNetbWat_Type.__name__ = "Integer32"
_SetNetbWat_Object = MibScalar
setNetbWat = _SetNetbWat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 8),
    _SetNetbWat_Type()
)
setNetbWat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setNetbWat.setStatus("mandatory")


class _SetNetbUpd_Type(Integer32):
    """Custom type setNetbUpd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pback", 0),
          ("time", 2),
          ("trig", 1))
    )


_SetNetbUpd_Type.__name__ = "Integer32"
_SetNetbUpd_Object = MibScalar
setNetbUpd = _SetNetbUpd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 9),
    _SetNetbUpd_Type()
)
setNetbUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setNetbUpd.setStatus("mandatory")
_SetNetbWan_Type = Integer32
_SetNetbWan_Object = MibScalar
setNetbWan = _SetNetbWan_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 16, 10),
    _SetNetbWan_Type()
)
setNetbWan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setNetbWan.setStatus("mandatory")
_SetDnsm_ObjectIdentity = ObjectIdentity
setDnsm = _SetDnsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17)
)


class _SetDnsmOpe_Type(Integer32):
    """Custom type setDnsmOpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetDnsmOpe_Type.__name__ = "Integer32"
_SetDnsmOpe_Object = MibScalar
setDnsmOpe = _SetDnsmOpe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 1),
    _SetDnsmOpe_Type()
)
setDnsmOpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmOpe.setStatus("mandatory")


class _SetDnsmDom_Type(DisplayString):
    """Custom type setDnsmDom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SetDnsmDom_Type.__name__ = "DisplayString"
_SetDnsmDom_Object = MibScalar
setDnsmDom = _SetDnsmDom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 2),
    _SetDnsmDom_Type()
)
setDnsmDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmDom.setStatus("mandatory")


class _SetDnsmDhc_Type(Integer32):
    """Custom type setDnsmDhc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SetDnsmDhc_Type.__name__ = "Integer32"
_SetDnsmDhc_Object = MibScalar
setDnsmDhc = _SetDnsmDhc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 3),
    _SetDnsmDhc_Type()
)
setDnsmDhc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmDhc.setStatus("mandatory")


class _SetDnsmNet_Type(Integer32):
    """Custom type setDnsmNet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SetDnsmNet_Type.__name__ = "Integer32"
_SetDnsmNet_Object = MibScalar
setDnsmNet = _SetDnsmNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 4),
    _SetDnsmNet_Type()
)
setDnsmNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmNet.setStatus("mandatory")
_SetDnsmDns_Object = MibTable
setDnsmDns = _SetDnsmDns_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 5)
)
if mibBuilder.loadTexts:
    setDnsmDns.setStatus("mandatory")
_SetDnsmDnsCols_Object = MibTableRow
setDnsmDnsCols = _SetDnsmDnsCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 5, 1)
)
setDnsmDnsCols.setIndexNames(
    (0, "ELSA-MIB", "setDnsmDnsHos"),
)
if mibBuilder.loadTexts:
    setDnsmDnsCols.setStatus("mandatory")
_SetDnsmDnsHos_Type = DisplayString
_SetDnsmDnsHos_Object = MibTableColumn
setDnsmDnsHos = _SetDnsmDnsHos_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 5, 1, 1),
    _SetDnsmDnsHos_Type()
)
setDnsmDnsHos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmDnsHos.setStatus("mandatory")
_SetDnsmDnsIpa_Type = IpAddress
_SetDnsmDnsIpa_Object = MibTableColumn
setDnsmDnsIpa = _SetDnsmDnsIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 5, 1, 2),
    _SetDnsmDnsIpa_Type()
)
setDnsmDnsIpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmDnsIpa.setStatus("mandatory")
_SetDnsmFil_Object = MibTable
setDnsmFil = _SetDnsmFil_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 6)
)
if mibBuilder.loadTexts:
    setDnsmFil.setStatus("mandatory")
_SetDnsmFilCols_Object = MibTableRow
setDnsmFilCols = _SetDnsmFilCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 6, 1)
)
setDnsmFilCols.setIndexNames(
    (0, "ELSA-MIB", "setDnsmFilIdx"),
)
if mibBuilder.loadTexts:
    setDnsmFilCols.setStatus("mandatory")
_SetDnsmFilIdx_Type = DisplayString
_SetDnsmFilIdx_Object = MibTableColumn
setDnsmFilIdx = _SetDnsmFilIdx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 6, 1, 1),
    _SetDnsmFilIdx_Type()
)
setDnsmFilIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmFilIdx.setStatus("mandatory")
_SetDnsmFilDom_Type = DisplayString
_SetDnsmFilDom_Object = MibTableColumn
setDnsmFilDom = _SetDnsmFilDom_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 6, 1, 2),
    _SetDnsmFilDom_Type()
)
setDnsmFilDom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmFilDom.setStatus("mandatory")
_SetDnsmFilIpa_Type = IpAddress
_SetDnsmFilIpa_Object = MibTableColumn
setDnsmFilIpa = _SetDnsmFilIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 6, 1, 3),
    _SetDnsmFilIpa_Type()
)
setDnsmFilIpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmFilIpa.setStatus("mandatory")
_SetDnsmFilNet_Type = IpAddress
_SetDnsmFilNet_Object = MibTableColumn
setDnsmFilNet = _SetDnsmFilNet_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 6, 1, 4),
    _SetDnsmFilNet_Type()
)
setDnsmFilNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmFilNet.setStatus("mandatory")
_SetDnsmLea_Type = Integer32
_SetDnsmLea_Object = MibScalar
setDnsmLea = _SetDnsmLea_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 7),
    _SetDnsmLea_Type()
)
setDnsmLea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDnsmLea.setStatus("mandatory")
_SetDnsmDyn_Object = MibTable
setDnsmDyn = _SetDnsmDyn_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 8)
)
if mibBuilder.loadTexts:
    setDnsmDyn.setStatus("mandatory")
_SetDnsmDynCols_Object = MibTableRow
setDnsmDynCols = _SetDnsmDynCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 8, 1)
)
setDnsmDynCols.setIndexNames(
    (0, "ELSA-MIB", "setDnsmDynHos"),
)
if mibBuilder.loadTexts:
    setDnsmDynCols.setStatus("mandatory")
_SetDnsmDynHos_Type = DisplayString
_SetDnsmDynHos_Object = MibTableColumn
setDnsmDynHos = _SetDnsmDynHos_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 8, 1, 1),
    _SetDnsmDynHos_Type()
)
setDnsmDynHos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDnsmDynHos.setStatus("mandatory")
_SetDnsmDynIpa_Type = IpAddress
_SetDnsmDynIpa_Object = MibTableColumn
setDnsmDynIpa = _SetDnsmDynIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 8, 1, 2),
    _SetDnsmDynIpa_Type()
)
setDnsmDynIpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDnsmDynIpa.setStatus("mandatory")
_SetDnsmDynTim_Type = Integer32
_SetDnsmDynTim_Object = MibTableColumn
setDnsmDynTim = _SetDnsmDynTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 17, 8, 1, 3),
    _SetDnsmDynTim_Type()
)
setDnsmDynTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDnsmDynTim.setStatus("mandatory")
_SetAcco_ObjectIdentity = ObjectIdentity
setAcco = _SetAcco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18)
)


class _SetAccoOpe_Type(Integer32):
    """Custom type setAccoOpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetAccoOpe_Type.__name__ = "Integer32"
_SetAccoOpe_Object = MibScalar
setAccoOpe = _SetAccoOpe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 1),
    _SetAccoOpe_Type()
)
setAccoOpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAccoOpe.setStatus("mandatory")


class _SetAccoSav_Type(Integer32):
    """Custom type setAccoSav based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SetAccoSav_Type.__name__ = "Integer32"
_SetAccoSav_Object = MibScalar
setAccoSav = _SetAccoSav_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 2),
    _SetAccoSav_Type()
)
setAccoSav.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAccoSav.setStatus("mandatory")


class _SetAccoSor_Type(Integer32):
    """Custom type setAccoSor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("time", 0))
    )


_SetAccoSor_Type.__name__ = "Integer32"
_SetAccoSor_Object = MibScalar
setAccoSor = _SetAccoSor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 3),
    _SetAccoSor_Type()
)
setAccoSor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAccoSor.setStatus("mandatory")
_SetAccoCur_Object = MibTable
setAccoCur = _SetAccoCur_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 4)
)
if mibBuilder.loadTexts:
    setAccoCur.setStatus("mandatory")
_SetAccoCurCols_Object = MibTableRow
setAccoCurCols = _SetAccoCurCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 4, 1)
)
setAccoCurCols.setIndexNames(
    (0, "ELSA-MIB", "setAccoCurUsern"),
)
if mibBuilder.loadTexts:
    setAccoCurCols.setStatus("mandatory")
_SetAccoCurUsern_Type = DisplayString
_SetAccoCurUsern_Object = MibTableColumn
setAccoCurUsern = _SetAccoCurUsern_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 4, 1, 1),
    _SetAccoCurUsern_Type()
)
setAccoCurUsern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoCurUsern.setStatus("mandatory")
_SetAccoCurMacad_Type = DisplayString
_SetAccoCurMacad_Object = MibTableColumn
setAccoCurMacad = _SetAccoCurMacad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 4, 1, 2),
    _SetAccoCurMacad_Type()
)
setAccoCurMacad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoCurMacad.setStatus("mandatory")
_SetAccoCurRemot_Type = DisplayString
_SetAccoCurRemot_Object = MibTableColumn
setAccoCurRemot = _SetAccoCurRemot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 4, 1, 3),
    _SetAccoCurRemot_Type()
)
setAccoCurRemot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoCurRemot.setStatus("mandatory")


class _SetAccoCurConnt_Type(Integer32):
    """Custom type setAccoCurConnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ab-ports", 6),
          ("dial-up", 1),
          ("dsl-line", 4),
          ("lancapi", 5),
          ("leased-line", 2),
          ("unknown", 0))
    )


_SetAccoCurConnt_Type.__name__ = "Integer32"
_SetAccoCurConnt_Object = MibTableColumn
setAccoCurConnt = _SetAccoCurConnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 4, 1, 4),
    _SetAccoCurConnt_Type()
)
setAccoCurConnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoCurConnt.setStatus("mandatory")
_SetAccoCurRxkby_Type = Integer32
_SetAccoCurRxkby_Object = MibTableColumn
setAccoCurRxkby = _SetAccoCurRxkby_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 4, 1, 5),
    _SetAccoCurRxkby_Type()
)
setAccoCurRxkby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoCurRxkby.setStatus("mandatory")
_SetAccoCurTxkby_Type = Integer32
_SetAccoCurTxkby_Object = MibTableColumn
setAccoCurTxkby = _SetAccoCurTxkby_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 4, 1, 6),
    _SetAccoCurTxkby_Type()
)
setAccoCurTxkby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoCurTxkby.setStatus("mandatory")
_SetAccoCurTotal_Type = Integer32
_SetAccoCurTotal_Object = MibTableColumn
setAccoCurTotal = _SetAccoCurTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 4, 1, 8),
    _SetAccoCurTotal_Type()
)
setAccoCurTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoCurTotal.setStatus("mandatory")
_SetAccoCurConne_Type = Integer32
_SetAccoCurConne_Object = MibTableColumn
setAccoCurConne = _SetAccoCurConne_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 4, 1, 9),
    _SetAccoCurConne_Type()
)
setAccoCurConne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoCurConne.setStatus("mandatory")
_SetAccoAcc_Object = MibTable
setAccoAcc = _SetAccoAcc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 5)
)
if mibBuilder.loadTexts:
    setAccoAcc.setStatus("mandatory")
_SetAccoAccCols_Object = MibTableRow
setAccoAccCols = _SetAccoAccCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 5, 1)
)
setAccoAccCols.setIndexNames(
    (0, "ELSA-MIB", "setAccoAccUsern"),
)
if mibBuilder.loadTexts:
    setAccoAccCols.setStatus("mandatory")
_SetAccoAccUsern_Type = DisplayString
_SetAccoAccUsern_Object = MibTableColumn
setAccoAccUsern = _SetAccoAccUsern_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 5, 1, 1),
    _SetAccoAccUsern_Type()
)
setAccoAccUsern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoAccUsern.setStatus("mandatory")
_SetAccoAccMacad_Type = DisplayString
_SetAccoAccMacad_Object = MibTableColumn
setAccoAccMacad = _SetAccoAccMacad_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 5, 1, 2),
    _SetAccoAccMacad_Type()
)
setAccoAccMacad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoAccMacad.setStatus("mandatory")
_SetAccoAccRemot_Type = DisplayString
_SetAccoAccRemot_Object = MibTableColumn
setAccoAccRemot = _SetAccoAccRemot_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 5, 1, 3),
    _SetAccoAccRemot_Type()
)
setAccoAccRemot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoAccRemot.setStatus("mandatory")


class _SetAccoAccConnt_Type(Integer32):
    """Custom type setAccoAccConnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ab-ports", 6),
          ("dial-up", 1),
          ("dsl-line", 4),
          ("lancapi", 5),
          ("leased-line", 2),
          ("unknown", 0))
    )


_SetAccoAccConnt_Type.__name__ = "Integer32"
_SetAccoAccConnt_Object = MibTableColumn
setAccoAccConnt = _SetAccoAccConnt_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 5, 1, 4),
    _SetAccoAccConnt_Type()
)
setAccoAccConnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoAccConnt.setStatus("mandatory")
_SetAccoAccRxkby_Type = Integer32
_SetAccoAccRxkby_Object = MibTableColumn
setAccoAccRxkby = _SetAccoAccRxkby_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 5, 1, 5),
    _SetAccoAccRxkby_Type()
)
setAccoAccRxkby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoAccRxkby.setStatus("mandatory")
_SetAccoAccTxkby_Type = Integer32
_SetAccoAccTxkby_Object = MibTableColumn
setAccoAccTxkby = _SetAccoAccTxkby_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 5, 1, 6),
    _SetAccoAccTxkby_Type()
)
setAccoAccTxkby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoAccTxkby.setStatus("mandatory")
_SetAccoAccTotal_Type = Integer32
_SetAccoAccTotal_Object = MibTableColumn
setAccoAccTotal = _SetAccoAccTotal_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 5, 1, 8),
    _SetAccoAccTotal_Type()
)
setAccoAccTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoAccTotal.setStatus("mandatory")
_SetAccoAccConne_Type = Integer32
_SetAccoAccConne_Object = MibTableColumn
setAccoAccConne = _SetAccoAccConne_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 5, 1, 9),
    _SetAccoAccConne_Type()
)
setAccoAccConne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setAccoAccConne.setStatus("mandatory")
_SetAccoDel_Type = Integer32
_SetAccoDel_Object = MibScalar
setAccoDel = _SetAccoDel_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 18, 6),
    _SetAccoDel_Type()
)
setAccoDel.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    setAccoDel.setStatus("mandatory")
_SetHttp_ObjectIdentity = ObjectIdentity
setHttp = _SetHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 21)
)


class _SetHttpDoc_Type(DisplayString):
    """Custom type setHttpDoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_SetHttpDoc_Type.__name__ = "DisplayString"
_SetHttpDoc_Object = MibScalar
setHttpDoc = _SetHttpDoc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 21, 1),
    _SetHttpDoc_Type()
)
setHttpDoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setHttpDoc.setStatus("mandatory")
_SetSysl_ObjectIdentity = ObjectIdentity
setSysl = _SetSysl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22)
)


class _SetSyslOpe_Type(Integer32):
    """Custom type setSyslOpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SetSyslOpe_Type.__name__ = "Integer32"
_SetSyslOpe_Object = MibScalar
setSyslOpe = _SetSyslOpe_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 1),
    _SetSyslOpe_Type()
)
setSyslOpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSyslOpe.setStatus("mandatory")
_SetSyslTab_Object = MibTable
setSyslTab = _SetSyslTab_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 2)
)
if mibBuilder.loadTexts:
    setSyslTab.setStatus("mandatory")
_SetSyslTabCols_Object = MibTableRow
setSyslTabCols = _SetSyslTabCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 2, 1)
)
setSyslTabCols.setIndexNames(
    (0, "ELSA-MIB", "setSyslTabIdx"),
)
if mibBuilder.loadTexts:
    setSyslTabCols.setStatus("mandatory")
_SetSyslTabIdx_Type = DisplayString
_SetSyslTabIdx_Object = MibTableColumn
setSyslTabIdx = _SetSyslTabIdx_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 2, 1, 1),
    _SetSyslTabIdx_Type()
)
setSyslTabIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSyslTabIdx.setStatus("mandatory")
_SetSyslTabIpa_Type = IpAddress
_SetSyslTabIpa_Object = MibTableColumn
setSyslTabIpa = _SetSyslTabIpa_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 2, 1, 2),
    _SetSyslTabIpa_Type()
)
setSyslTabIpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSyslTabIpa.setStatus("mandatory")
_SetSyslTabSou_Type = Integer32
_SetSyslTabSou_Object = MibTableColumn
setSyslTabSou = _SetSyslTabSou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 2, 1, 3),
    _SetSyslTabSou_Type()
)
setSyslTabSou.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSyslTabSou.setStatus("mandatory")
_SetSyslTabLev_Type = Integer32
_SetSyslTabLev_Object = MibTableColumn
setSyslTabLev = _SetSyslTabLev_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 2, 1, 4),
    _SetSyslTabLev_Type()
)
setSyslTabLev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSyslTabLev.setStatus("mandatory")
_SetSyslFac_Object = MibTable
setSyslFac = _SetSyslFac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 3)
)
if mibBuilder.loadTexts:
    setSyslFac.setStatus("mandatory")
_SetSyslFacCols_Object = MibTableRow
setSyslFacCols = _SetSyslFacCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 3, 1)
)
setSyslFacCols.setIndexNames(
    (0, "ELSA-MIB", "setSyslFacSou"),
)
if mibBuilder.loadTexts:
    setSyslFacCols.setStatus("mandatory")


class _SetSyslFacSou_Type(Integer32):
    """Custom type setSyslFacSou based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 32),
          ("administration", 64),
          ("connections", 16),
          ("console-login", 8),
          ("login", 2),
          ("router", 128),
          ("system", 1),
          ("systemtime", 4))
    )


_SetSyslFacSou_Type.__name__ = "Integer32"
_SetSyslFacSou_Object = MibTableColumn
setSyslFacSou = _SetSyslFacSou_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 3, 1, 1),
    _SetSyslFacSou_Type()
)
setSyslFacSou.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setSyslFacSou.setStatus("mandatory")


class _SetSyslFacFac_Type(Integer32):
    """Custom type setSyslFacFac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("auth", 4),
          ("authpriv", 10),
          ("cron", 9),
          ("daemon", 3),
          ("kern", 0),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("lpr", 6),
          ("mail", 2),
          ("news", 7),
          ("syslog", 5),
          ("user", 1),
          ("uucp", 8))
    )


_SetSyslFacFac_Type.__name__ = "Integer32"
_SetSyslFacFac_Object = MibTableColumn
setSyslFacFac = _SetSyslFacFac_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 3, 1, 2),
    _SetSyslFacFac_Type()
)
setSyslFacFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSyslFacFac.setStatus("mandatory")
_SetSyslPor_Type = Integer32
_SetSyslPor_Object = MibScalar
setSyslPor = _SetSyslPor_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 2, 22, 4),
    _SetSyslPor_Type()
)
setSyslPor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSyslPor.setStatus("mandatory")
_Fir_ObjectIdentity = ObjectIdentity
fir = _Fir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3)
)
_FirVer_Object = MibTable
firVer = _FirVer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 1)
)
if mibBuilder.loadTexts:
    firVer.setStatus("mandatory")
_FirVerCols_Object = MibTableRow
firVerCols = _FirVerCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 1, 1)
)
firVerCols.setIndexNames(
    (0, "ELSA-MIB", "firVerIfc"),
)
if mibBuilder.loadTexts:
    firVerCols.setStatus("mandatory")


class _FirVerIfc_Type(Integer32):
    """Custom type firVerIfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ifc", 1)
    )


_FirVerIfc_Type.__name__ = "Integer32"
_FirVerIfc_Object = MibTableColumn
firVerIfc = _FirVerIfc_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 1, 1, 1),
    _FirVerIfc_Type()
)
firVerIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firVerIfc.setStatus("mandatory")
_FirVerMod_Type = DisplayString
_FirVerMod_Object = MibTableColumn
firVerMod = _FirVerMod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 1, 1, 2),
    _FirVerMod_Type()
)
firVerMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firVerMod.setStatus("mandatory")
_FirVerVer_Type = DisplayString
_FirVerVer_Object = MibTableColumn
firVerVer = _FirVerVer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 1, 1, 3),
    _FirVerVer_Type()
)
firVerVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firVerVer.setStatus("mandatory")
_FirVerSer_Type = DisplayString
_FirVerSer_Object = MibTableColumn
firVerSer = _FirVerSer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 1, 1, 4),
    _FirVerSer_Type()
)
firVerSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firVerSer.setStatus("mandatory")
_FirTab_Object = MibTable
firTab = _FirTab_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 2)
)
if mibBuilder.loadTexts:
    firTab.setStatus("mandatory")
_FirTabCols_Object = MibTableRow
firTabCols = _FirTabCols_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 2, 1)
)
firTabCols.setIndexNames(
    (0, "ELSA-MIB", "firTabPos"),
)
if mibBuilder.loadTexts:
    firTabCols.setStatus("mandatory")
_FirTabPos_Type = Integer32
_FirTabPos_Object = MibTableColumn
firTabPos = _FirTabPos_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 2, 1, 1),
    _FirTabPos_Type()
)
firTabPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firTabPos.setStatus("mandatory")


class _FirTabSta_Type(Integer32):
    """Custom type firTabSta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0),
          ("minimal-active", 5),
          ("minimal-inactive", 4))
    )


_FirTabSta_Type.__name__ = "Integer32"
_FirTabSta_Object = MibTableColumn
firTabSta = _FirTabSta_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 2, 1, 2),
    _FirTabSta_Type()
)
firTabSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firTabSta.setStatus("mandatory")
_FirTabVer_Type = DisplayString
_FirTabVer_Object = MibTableColumn
firTabVer = _FirTabVer_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 2, 1, 3),
    _FirTabVer_Type()
)
firTabVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firTabVer.setStatus("mandatory")
_FirTabDat_Type = DisplayString
_FirTabDat_Object = MibTableColumn
firTabDat = _FirTabDat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 2, 1, 4),
    _FirTabDat_Type()
)
firTabDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firTabDat.setStatus("mandatory")
_FirTabSiz_Type = Integer32
_FirTabSiz_Object = MibTableColumn
firTabSiz = _FirTabSiz_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 2, 1, 5),
    _FirTabSiz_Type()
)
firTabSiz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firTabSiz.setStatus("mandatory")
_FirTabInd_Type = Integer32
_FirTabInd_Object = MibTableColumn
firTabInd = _FirTabInd_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 2, 1, 6),
    _FirTabInd_Type()
)
firTabInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firTabInd.setStatus("mandatory")


class _FirMod_Type(Integer32):
    """Custom type firMod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 0),
          ("login", 1),
          ("manual", 2))
    )


_FirMod_Type.__name__ = "Integer32"
_FirMod_Object = MibScalar
firMod = _FirMod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 3),
    _FirMod_Type()
)
firMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firMod.setStatus("mandatory")
_FirTim_Type = Integer32
_FirTim_Object = MibScalar
firTim = _FirTim_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 3, 4),
    _FirTim_Type()
)
firTim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firTim.setStatus("mandatory")
_Oth_ObjectIdentity = ObjectIdentity
oth = _Oth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 4)
)
_OthMan_ObjectIdentity = ObjectIdentity
othMan = _OthMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 4, 1)
)
_OthManCon_Type = Integer32
_OthManCon_Object = MibScalar
othManCon = _OthManCon_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 4, 1, 1),
    _OthManCon_Type()
)
othManCon.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    othManCon.setStatus("mandatory")
_OthManDis_Type = Integer32
_OthManDis_Object = MibScalar
othManDis = _OthManDis_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 4, 1, 2),
    _OthManDis_Type()
)
othManDis.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    othManDis.setStatus("mandatory")
_OthBoo_Type = Integer32
_OthBoo_Object = MibScalar
othBoo = _OthBoo_Object(
    (1, 3, 6, 1, 4, 1, 2356, 400, 1, 2000, 4, 2),
    _OthBoo_Type()
)
othBoo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    othBoo.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELSA-MIB",
    **{"elsa": elsa,
       "isdn-Systems": isdn_Systems,
       "isdn-Router": isdn_Router,
       "lancom-2000": lancom_2000,
       "sta": sta,
       "staConne": staConne,
       "staOpera": staOpera,
       "staWanst": staWanst,
       "staWanstBytetrans": staWanstBytetrans,
       "staWanstBytetransCols": staWanstBytetransCols,
       "staWanstBytetransIfc": staWanstBytetransIfc,
       "staWanstBytetransCrx": staWanstBytetransCrx,
       "staWanstBytetransRxb": staWanstBytetransRxb,
       "staWanstBytetransTxb": staWanstBytetransTxb,
       "staWanstBytetransCtx": staWanstBytetransCtx,
       "staWanstPackettra": staWanstPackettra,
       "staWanstPackettraCols": staWanstPackettraCols,
       "staWanstPackettraIfc": staWanstPackettraIfc,
       "staWanstPackettraRx": staWanstPackettraRx,
       "staWanstPackettraTxt": staWanstPackettraTxt,
       "staWanstPackettraTxn": staWanstPackettraTxn,
       "staWanstPackettraTxr": staWanstPackettraTxr,
       "staWanstPackettraTxu": staWanstPackettraTxu,
       "staWanstErrorstat": staWanstErrorstat,
       "staWanstErrorstatCols": staWanstErrorstatCols,
       "staWanstErrorstatIfc": staWanstErrorstatIfc,
       "staWanstErrorstatRxl1": staWanstErrorstatRxl1,
       "staWanstErrorstatRxl2": staWanstErrorstatRxl2,
       "staWanstErrorstatRxl3": staWanstErrorstatRxl3,
       "staWanstErrorstatStac": staWanstErrorstatStac,
       "staWanstErrorstatTxer": staWanstErrorstatTxer,
       "staWanstWantxdisc": staWanstWantxdisc,
       "staWanstWanheappa": staWanstWanheappa,
       "staWanstWanqueuep": staWanstWanqueuep,
       "staWanstWanqueuee": staWanstWanqueuee,
       "staWanstThroughpu": staWanstThroughpu,
       "staWanstThroughpuCols": staWanstThroughpuCols,
       "staWanstThroughpuIfc": staWanstThroughpuIfc,
       "staWanstThroughpuRxsc": staWanstThroughpuRxsc,
       "staWanstThroughpuTxsc": staWanstThroughpuTxsc,
       "staWanstThroughpuRxsa": staWanstThroughpuRxsa,
       "staWanstThroughpuTxsa": staWanstThroughpuTxsa,
       "staWanstDeleteval": staWanstDeleteval,
       "staLanst": staLanst,
       "staLanstLanrxpack": staLanstLanrxpack,
       "staLanstLantxpack": staLanstLantxpack,
       "staLanstLanrxerro": staLanstLanrxerro,
       "staLanstLantxerro": staLanstLantxerro,
       "staLanstLanstacke": staLanstLanstacke,
       "staLanstLannicerr": staLanstLannicerr,
       "staLanstLanheappa": staLanstLanheappa,
       "staLanstLanqueuep": staLanstLanqueuep,
       "staLanstLanqueuee": staLanstLanqueuee,
       "staLanstLancollis": staLanstLancollis,
       "staLanstDeleteval": staLanstDeleteval,
       "staLanstLanrxbyte": staLanstLanrxbyte,
       "staLanstLantxbyte": staLanstLantxbyte,
       "staLanstLanrxbroa": staLanstLanrxbroa,
       "staLanstLanrxmult": staLanstLanrxmult,
       "staLanstLanrxunic": staLanstLanrxunic,
       "staLanstLantxbroa": staLanstLantxbroa,
       "staLanstLantxmult": staLanstLantxmult,
       "staLanstLantxunic": staLanstLantxunic,
       "staLanstLanrxcrce": staLanstLanrxcrce,
       "staLanstLanrxalig": staLanstLanrxalig,
       "staPppst": staPppst,
       "staPppstPpp": staPppstPpp,
       "staPppstPppCols": staPppstPppCols,
       "staPppstPppIfc": staPppstPppIfc,
       "staPppstPppPha": staPppstPppPha,
       "staPppstPppLcp": staPppstPppLcp,
       "staPppstPppIpc": staPppstPppIpc,
       "staPppstPppIpx": staPppstPppIpx,
       "staPppstPppCcp": staPppstPppCcp,
       "staPppstPppBac": staPppstPppBac,
       "staPppstLcp": staPppstLcp,
       "staPppstLcpRxerrors": staPppstLcpRxerrors,
       "staPppstLcpRxdiscarded": staPppstLcpRxdiscarded,
       "staPppstLcpRxconfigrequ": staPppstLcpRxconfigrequ,
       "staPppstLcpRxconfigack": staPppstLcpRxconfigack,
       "staPppstLcpRxconfignak": staPppstLcpRxconfignak,
       "staPppstLcpRxconfigreje": staPppstLcpRxconfigreje,
       "staPppstLcpRxterminater": staPppstLcpRxterminater,
       "staPppstLcpRxterminatea": staPppstLcpRxterminatea,
       "staPppstLcpRxcodereject": staPppstLcpRxcodereject,
       "staPppstLcpRxprotocolre": staPppstLcpRxprotocolre,
       "staPppstLcpRxechoreques": staPppstLcpRxechoreques,
       "staPppstLcpRxechoreply": staPppstLcpRxechoreply,
       "staPppstLcpRxdiscardreq": staPppstLcpRxdiscardreq,
       "staPppstLcpTxconfigrequ": staPppstLcpTxconfigrequ,
       "staPppstLcpTxconfigack": staPppstLcpTxconfigack,
       "staPppstLcpTxconfignak": staPppstLcpTxconfignak,
       "staPppstLcpTxconfigreje": staPppstLcpTxconfigreje,
       "staPppstLcpTxterminater": staPppstLcpTxterminater,
       "staPppstLcpTxterminatea": staPppstLcpTxterminatea,
       "staPppstLcpTxcodereject": staPppstLcpTxcodereject,
       "staPppstLcpTxprotocolre": staPppstLcpTxprotocolre,
       "staPppstLcpTxechoreques": staPppstLcpTxechoreques,
       "staPppstLcpTxechoreply": staPppstLcpTxechoreply,
       "staPppstLcpTxdiscardreq": staPppstLcpTxdiscardreq,
       "staPppstLcpDeletevalues": staPppstLcpDeletevalues,
       "staPppstPap": staPppstPap,
       "staPppstPapRxdis": staPppstPapRxdis,
       "staPppstPapRxreq": staPppstPapRxreq,
       "staPppstPapRxsuc": staPppstPapRxsuc,
       "staPppstPapRxfai": staPppstPapRxfai,
       "staPppstPapTxret": staPppstPapTxret,
       "staPppstPapTxreq": staPppstPapTxreq,
       "staPppstPapTxsuc": staPppstPapTxsuc,
       "staPppstPapTxfai": staPppstPapTxfai,
       "staPppstPapDelet": staPppstPapDelet,
       "staPppstCha": staPppstCha,
       "staPppstChaRxdis": staPppstChaRxdis,
       "staPppstChaRxcha": staPppstChaRxcha,
       "staPppstChaRxres": staPppstChaRxres,
       "staPppstChaRxsuc": staPppstChaRxsuc,
       "staPppstChaRxfai": staPppstChaRxfai,
       "staPppstChaTxret": staPppstChaTxret,
       "staPppstChaTxcha": staPppstChaTxcha,
       "staPppstChaTxres": staPppstChaTxres,
       "staPppstChaTxsuc": staPppstChaTxsuc,
       "staPppstChaTxfai": staPppstChaTxfai,
       "staPppstChaDelet": staPppstChaDelet,
       "staPppstIpx": staPppstIpx,
       "staPppstIpxRxdiscarded": staPppstIpxRxdiscarded,
       "staPppstIpxRxconfigrequ": staPppstIpxRxconfigrequ,
       "staPppstIpxRxconfigack": staPppstIpxRxconfigack,
       "staPppstIpxRxconfignak": staPppstIpxRxconfignak,
       "staPppstIpxRxconfigreje": staPppstIpxRxconfigreje,
       "staPppstIpxRxterminater": staPppstIpxRxterminater,
       "staPppstIpxRxterminatea": staPppstIpxRxterminatea,
       "staPppstIpxRxcodereject": staPppstIpxRxcodereject,
       "staPppstIpxTxconfigrequ": staPppstIpxTxconfigrequ,
       "staPppstIpxTxconfigack": staPppstIpxTxconfigack,
       "staPppstIpxTxconfignak": staPppstIpxTxconfignak,
       "staPppstIpxTxconfigreje": staPppstIpxTxconfigreje,
       "staPppstIpxTxterminater": staPppstIpxTxterminater,
       "staPppstIpxTxterminatea": staPppstIpxTxterminatea,
       "staPppstIpxTxcodereject": staPppstIpxTxcodereject,
       "staPppstIpxDeletevalues": staPppstIpxDeletevalues,
       "staPppstIpc": staPppstIpc,
       "staPppstIpcRxdiscarded": staPppstIpcRxdiscarded,
       "staPppstIpcRxconfigrequ": staPppstIpcRxconfigrequ,
       "staPppstIpcRxconfigack": staPppstIpcRxconfigack,
       "staPppstIpcRxconfignak": staPppstIpcRxconfignak,
       "staPppstIpcRxconfigreje": staPppstIpcRxconfigreje,
       "staPppstIpcRxterminater": staPppstIpcRxterminater,
       "staPppstIpcRxterminatea": staPppstIpcRxterminatea,
       "staPppstIpcRxcodereject": staPppstIpcRxcodereject,
       "staPppstIpcTxconfigrequ": staPppstIpcTxconfigrequ,
       "staPppstIpcTxconfigack": staPppstIpcTxconfigack,
       "staPppstIpcTxconfignak": staPppstIpcTxconfignak,
       "staPppstIpcTxconfigreje": staPppstIpcTxconfigreje,
       "staPppstIpcTxterminater": staPppstIpcTxterminater,
       "staPppstIpcTxterminatea": staPppstIpcTxterminatea,
       "staPppstIpcTxcodereject": staPppstIpcTxcodereject,
       "staPppstIpcDeletevalues": staPppstIpcDeletevalues,
       "staPppstCbc": staPppstCbc,
       "staPppstCbcRxdis": staPppstCbcRxdis,
       "staPppstCbcRxreq": staPppstCbcRxreq,
       "staPppstCbcRxres": staPppstCbcRxres,
       "staPppstCbcRxack": staPppstCbcRxack,
       "staPppstCbcTxreq": staPppstCbcTxreq,
       "staPppstCbcTxres": staPppstCbcTxres,
       "staPppstCbcTxack": staPppstCbcTxack,
       "staPppstCbcDelet": staPppstCbcDelet,
       "staPppstRxo": staPppstRxo,
       "staPppstRxoLcp": staPppstRxoLcp,
       "staPppstRxoLcpCols": staPppstRxoLcpCols,
       "staPppstRxoLcpIfc": staPppstRxoLcpIfc,
       "staPppstRxoLcpMru": staPppstRxoLcpMru,
       "staPppstRxoLcpAcc": staPppstRxoLcpAcc,
       "staPppstRxoLcpAut": staPppstRxoLcpAut,
       "staPppstRxoLcpCal": staPppstRxoLcpCal,
       "staPppstRxoLcpMag": staPppstRxoLcpMag,
       "staPppstRxoLcpPfc": staPppstRxoLcpPfc,
       "staPppstRxoLcpAcf": staPppstRxoLcpAcf,
       "staPppstRxoIpx": staPppstRxoIpx,
       "staPppstRxoIpxCols": staPppstRxoIpxCols,
       "staPppstRxoIpxIfc": staPppstRxoIpxIfc,
       "staPppstRxoIpxNet": staPppstRxoIpxNet,
       "staPppstRxoIpxNod": staPppstRxoIpxNod,
       "staPppstRxoIpxRou": staPppstRxoIpxRou,
       "staPppstRxoIpc": staPppstRxoIpc,
       "staPppstRxoIpcCols": staPppstRxoIpcCols,
       "staPppstRxoIpcIfc": staPppstRxoIpcIfc,
       "staPppstRxoIpcIpa": staPppstRxoIpcIpa,
       "staPppstRxoIpcDns": staPppstRxoIpcDns,
       "staPppstRxoIpcNbn": staPppstRxoIpcNbn,
       "staPppstTxo": staPppstTxo,
       "staPppstTxoLcp": staPppstTxoLcp,
       "staPppstTxoLcpCols": staPppstTxoLcpCols,
       "staPppstTxoLcpIfc": staPppstTxoLcpIfc,
       "staPppstTxoLcpMru": staPppstTxoLcpMru,
       "staPppstTxoLcpAcc": staPppstTxoLcpAcc,
       "staPppstTxoLcpAut": staPppstTxoLcpAut,
       "staPppstTxoLcpCal": staPppstTxoLcpCal,
       "staPppstTxoLcpMag": staPppstTxoLcpMag,
       "staPppstTxoLcpPfc": staPppstTxoLcpPfc,
       "staPppstTxoLcpAcf": staPppstTxoLcpAcf,
       "staPppstTxoIpx": staPppstTxoIpx,
       "staPppstTxoIpxCols": staPppstTxoIpxCols,
       "staPppstTxoIpxIfc": staPppstTxoIpxIfc,
       "staPppstTxoIpxNet": staPppstTxoIpxNet,
       "staPppstTxoIpxNod": staPppstTxoIpxNod,
       "staPppstTxoIpxRou": staPppstTxoIpxRou,
       "staPppstTxoIpc": staPppstTxoIpc,
       "staPppstTxoIpcCols": staPppstTxoIpcCols,
       "staPppstTxoIpcIfc": staPppstTxoIpcIfc,
       "staPppstTxoIpcIpa": staPppstTxoIpcIpa,
       "staPppstTxoIpcDns": staPppstTxoIpcDns,
       "staPppstTxoIpcNbn": staPppstTxoIpcNbn,
       "staPppstCcp": staPppstCcp,
       "staPppstCcpRxdiscarded": staPppstCcpRxdiscarded,
       "staPppstCcpRxconfigrequ": staPppstCcpRxconfigrequ,
       "staPppstCcpRxconfigack": staPppstCcpRxconfigack,
       "staPppstCcpRxconfignak": staPppstCcpRxconfignak,
       "staPppstCcpRxconfigreje": staPppstCcpRxconfigreje,
       "staPppstCcpRxterminater": staPppstCcpRxterminater,
       "staPppstCcpRxterminatea": staPppstCcpRxterminatea,
       "staPppstCcpRxcodereject": staPppstCcpRxcodereject,
       "staPppstCcpRxresetreque": staPppstCcpRxresetreque,
       "staPppstCcpRxresetack": staPppstCcpRxresetack,
       "staPppstCcpTxconfigrequ": staPppstCcpTxconfigrequ,
       "staPppstCcpTxconfigack": staPppstCcpTxconfigack,
       "staPppstCcpTxconfignak": staPppstCcpTxconfignak,
       "staPppstCcpTxconfigreje": staPppstCcpTxconfigreje,
       "staPppstCcpTxterminater": staPppstCcpTxterminater,
       "staPppstCcpTxterminatea": staPppstCcpTxterminatea,
       "staPppstCcpTxcodereject": staPppstCcpTxcodereject,
       "staPppstCcpTxresetreque": staPppstCcpTxresetreque,
       "staPppstCcpTxresetack": staPppstCcpTxresetack,
       "staPppstCcpDeletevalues": staPppstCcpDeletevalues,
       "staPppstCcpCompressione": staPppstCcpCompressione,
       "staPppstMls": staPppstMls,
       "staPppstMlsBundlec": staPppstMlsBundlec,
       "staPppstMlsRxseqlo": staPppstMlsRxseqlo,
       "staPppstMlsRxseqre": staPppstMlsRxseqre,
       "staPppstMlsRxmrrue": staPppstMlsRxmrrue,
       "staPppstMlsRxheade": staPppstMlsRxheade,
       "staPppstMlsRxdisca": staPppstMlsRxdisca,
       "staPppstMlsRxfrags": staPppstMlsRxfrags,
       "staPppstMlsRxfragm": staPppstMlsRxfragm,
       "staPppstMlsRxfrage": staPppstMlsRxfrage,
       "staPppstMlsRxnotfr": staPppstMlsRxnotfr,
       "staPppstMlsDeletev": staPppstMlsDeletev,
       "staPppstBac": staPppstBac,
       "staPppstBacRxerrors": staPppstBacRxerrors,
       "staPppstBacRxdiscarded": staPppstBacRxdiscarded,
       "staPppstBacRxcallrequest": staPppstBacRxcallrequest,
       "staPppstBacRxcallrespons": staPppstBacRxcallrespons,
       "staPppstBacRxcallbackreq": staPppstBacRxcallbackreq,
       "staPppstBacRxcallbackres": staPppstBacRxcallbackres,
       "staPppstBacRxlinkdropreq": staPppstBacRxlinkdropreq,
       "staPppstBacRxlinkdropres": staPppstBacRxlinkdropres,
       "staPppstBacRxstatusindic": staPppstBacRxstatusindic,
       "staPppstBacRxstatusreson": staPppstBacRxstatusreson,
       "staPppstBacTxcallrequest": staPppstBacTxcallrequest,
       "staPppstBacTxcallrespons": staPppstBacTxcallrespons,
       "staPppstBacTxcallbackreq": staPppstBacTxcallbackreq,
       "staPppstBacTxcallbackres": staPppstBacTxcallbackres,
       "staPppstBacTxlinkdropreq": staPppstBacTxlinkdropreq,
       "staPppstBacTxlinkdropres": staPppstBacTxlinkdropres,
       "staPppstBacTxstatusindic": staPppstBacTxstatusindic,
       "staPppstBacTxstatusreson": staPppstBacTxstatusreson,
       "staPppstBacDeletevalues": staPppstBacDeletevalues,
       "staPppstDel": staPppstDel,
       "staBridg": staBridg,
       "staBridgBrglanr": staBridgBrglanr,
       "staBridgBrglant": staBridgBrglant,
       "staBridgBrglanf": staBridgBrglanf,
       "staBridgBrglanb": staBridgBrglanb,
       "staBridgBrglanm": staBridgBrglanm,
       "staBridgBrgwanr": staBridgBrgwanr,
       "staBridgBrgwant": staBridgBrgwant,
       "staBridgBrgwanf": staBridgBrgwanf,
       "staBridgBrgwanb": staBridgBrgwanb,
       "staBridgBrgwanm": staBridgBrgwanm,
       "staBridgBrgaddr": staBridgBrgaddr,
       "staBridgTablebr": staBridgTablebr,
       "staBridgTablebrCols": staBridgTablebrCols,
       "staBridgTablebrNod": staBridgTablebrNod,
       "staBridgTablebrLas": staBridgTablebrLas,
       "staBridgTablebrFor": staBridgTablebrFor,
       "staBridgEstabli": staBridgEstabli,
       "staBridgEstabliCols": staBridgEstabliCols,
       "staBridgEstabliTim": staBridgEstabliTim,
       "staBridgEstabliDes": staBridgEstabliDes,
       "staBridgEstabliSou": staBridgEstabliSou,
       "staBridgDeletev": staBridgDeletev,
       "staIpxst": staIpxst,
       "staIpxstMac": staIpxstMac,
       "staIpxstMacIpxlanrx": staIpxstMacIpxlanrx,
       "staIpxstMacIpxlanrxb": staIpxstMacIpxlanrxb,
       "staIpxstMacIpxlanrxm": staIpxstMacIpxlanrxm,
       "staIpxstMacIpxlanrxu": staIpxstMacIpxlanrxu,
       "staIpxstMacIpxlantx": staIpxstMacIpxlantx,
       "staIpxstMacIpxwanrx": staIpxstMacIpxwanrx,
       "staIpxstMacIpxwanrxb": staIpxstMacIpxwanrxb,
       "staIpxstMacIpxwanrxm": staIpxstMacIpxwanrxm,
       "staIpxstMacIpxwanrxu": staIpxstMacIpxwanrxu,
       "staIpxstMacIpxwantx": staIpxstMacIpxwantx,
       "staIpxstMacDeleteval": staIpxstMacDeleteval,
       "staIpxstWat": staIpxstWat,
       "staIpxstWatIpxwatchdoglanr": staIpxstWatIpxwatchdoglanr,
       "staIpxstWatIpxwatchdoglant": staIpxstWatIpxwatchdoglant,
       "staIpxstWatIpxwatchdogwanr": staIpxstWatIpxwatchdogwanr,
       "staIpxstWatIpxwatchdogwant": staIpxstWatIpxwatchdogwant,
       "staIpxstWatSpxwatchdoglanr": staIpxstWatSpxwatchdoglanr,
       "staIpxstWatSpxwatchdoglant": staIpxstWatSpxwatchdoglant,
       "staIpxstWatSpxwatchdogwanr": staIpxstWatSpxwatchdogwanr,
       "staIpxstWatSpxwatchdogwant": staIpxstWatSpxwatchdogwant,
       "staIpxstWatDeletevalues": staIpxstWatDeletevalues,
       "staIpxstPro": staIpxstPro,
       "staIpxstProPropagatelanr": staIpxstProPropagatelanr,
       "staIpxstProPropagatelanf": staIpxstProPropagatelanf,
       "staIpxstProPropagatelant": staIpxstProPropagatelant,
       "staIpxstProPropagatelans": staIpxstProPropagatelans,
       "staIpxstProPropagatelanh": staIpxstProPropagatelanh,
       "staIpxstProPropagatelanb": staIpxstProPropagatelanb,
       "staIpxstProPropagatelanc": staIpxstProPropagatelanc,
       "staIpxstProPropagatewanr": staIpxstProPropagatewanr,
       "staIpxstProPropagatewanf": staIpxstProPropagatewanf,
       "staIpxstProPropagatewant": staIpxstProPropagatewant,
       "staIpxstProPropagatewans": staIpxstProPropagatewans,
       "staIpxstProDeletevalues": staIpxstProDeletevalues,
       "staIpxstRip": staIpxstRip,
       "staIpxstRipRiplanr": staIpxstRipRiplanr,
       "staIpxstRipRiplane": staIpxstRipRiplane,
       "staIpxstRipRiplant": staIpxstRipRiplant,
       "staIpxstRipRipwanr": staIpxstRipRipwanr,
       "staIpxstRipRipwane": staIpxstRipRipwane,
       "staIpxstRipRipwant": staIpxstRipRipwant,
       "staIpxstRipTableri": staIpxstRipTableri,
       "staIpxstRipTableriCols": staIpxstRipTableriCols,
       "staIpxstRipTableriNet": staIpxstRipTableriNet,
       "staIpxstRipTableriHop": staIpxstRipTableriHop,
       "staIpxstRipTableriTic": staIpxstRipTableriTic,
       "staIpxstRipTableriNod": staIpxstRipTableriNod,
       "staIpxstRipTableriTim": staIpxstRipTableriTim,
       "staIpxstRipTableriFla": staIpxstRipTableriFla,
       "staIpxstRipDeletev": staIpxstRipDeletev,
       "staIpxstSap": staIpxstSap,
       "staIpxstSapSaplanr": staIpxstSapSaplanr,
       "staIpxstSapSaplane": staIpxstSapSaplane,
       "staIpxstSapSaplant": staIpxstSapSaplant,
       "staIpxstSapSapwanr": staIpxstSapSapwanr,
       "staIpxstSapSapwane": staIpxstSapSapwane,
       "staIpxstSapSapwant": staIpxstSapSapwant,
       "staIpxstSapTablesa": staIpxstSapTablesa,
       "staIpxstSapTablesaCols": staIpxstSapTablesaCols,
       "staIpxstSapTablesaTyp": staIpxstSapTablesaTyp,
       "staIpxstSapTablesaSer": staIpxstSapTablesaSer,
       "staIpxstSapTablesaNet": staIpxstSapTablesaNet,
       "staIpxstSapTablesaNod": staIpxstSapTablesaNod,
       "staIpxstSapTablesaSoc": staIpxstSapTablesaSoc,
       "staIpxstSapTablesaHop": staIpxstSapTablesaHop,
       "staIpxstSapTablesaTim": staIpxstSapTablesaTim,
       "staIpxstSapTablesaFla": staIpxstSapTablesaFla,
       "staIpxstSapDeletev": staIpxstSapDeletev,
       "staIpxstIpx": staIpxstIpx,
       "staIpxstIpxIpxrlanr": staIpxstIpxIpxrlanr,
       "staIpxstIpxIpxrlant": staIpxstIpxIpxrlant,
       "staIpxstIpxIpxrlanh": staIpxstIpxIpxrlanh,
       "staIpxstIpxIpxrlans": staIpxstIpxIpxrlans,
       "staIpxstIpxIpxrlann": staIpxstIpxIpxrlann,
       "staIpxstIpxIpxrlanb": staIpxstIpxIpxrlanb,
       "staIpxstIpxIpxrlanc": staIpxstIpxIpxrlanc,
       "staIpxstIpxIpxrland": staIpxstIpxIpxrland,
       "staIpxstIpxIpxrwanr": staIpxstIpxIpxrwanr,
       "staIpxstIpxIpxrwant": staIpxstIpxIpxrwant,
       "staIpxstIpxIpxrwanh": staIpxstIpxIpxrwanh,
       "staIpxstIpxIpxrwans": staIpxstIpxIpxrwans,
       "staIpxstIpxIpxrwann": staIpxstIpxIpxrwann,
       "staIpxstIpxIpxrwanb": staIpxstIpxIpxrwanb,
       "staIpxstIpxIpxrwand": staIpxstIpxIpxrwand,
       "staIpxstIpxIpxrinte": staIpxstIpxIpxrinte,
       "staIpxstIpxNetworks": staIpxstIpxNetworks,
       "staIpxstIpxNetworksCols": staIpxstIpxNetworksCols,
       "staIpxstIpxNetworksRem": staIpxstIpxNetworksRem,
       "staIpxstIpxNetworksNet": staIpxstIpxNetworksNet,
       "staIpxstIpxNetworksBin": staIpxstIpxNetworksBin,
       "staIpxstIpxNetworksPro": staIpxstIpxNetworksPro,
       "staIpxstIpxNetworksBac": staIpxstIpxNetworksBac,
       "staIpxstIpxNetworksTim": staIpxstIpxNetworksTim,
       "staIpxstIpxNetworksNod": staIpxstIpxNetworksNod,
       "staIpxstIpxEstablis": staIpxstIpxEstablis,
       "staIpxstIpxEstablisCols": staIpxstIpxEstablisCols,
       "staIpxstIpxEstablisTime": staIpxstIpxEstablisTime,
       "staIpxstIpxEstablisDestnet": staIpxstIpxEstablisDestnet,
       "staIpxstIpxEstablisDestnode": staIpxstIpxEstablisDestnode,
       "staIpxstIpxEstablisDestsock": staIpxstIpxEstablisDestsock,
       "staIpxstIpxEstablisSourcene": staIpxstIpxEstablisSourcene,
       "staIpxstIpxEstablisSourceno": staIpxstIpxEstablisSourceno,
       "staIpxstIpxEstablisSourceso": staIpxstIpxEstablisSourceso,
       "staIpxstIpxDeleteva": staIpxstIpxDeleteva,
       "staIpxstDel": staIpxstDel,
       "staTcpip": staTcpip,
       "staTcpipArp": staTcpipArp,
       "staTcpipArpArplanr": staTcpipArpArplanr,
       "staTcpipArpArplant": staTcpipArpArplant,
       "staTcpipArpArplane": staTcpipArpArplane,
       "staTcpipArpArpwanr": staTcpipArpArpwanr,
       "staTcpipArpArpwant": staTcpipArpArpwant,
       "staTcpipArpArpwane": staTcpipArpArpwane,
       "staTcpipArpTablear": staTcpipArpTablear,
       "staTcpipArpTablearCols": staTcpipArpTablearCols,
       "staTcpipArpTablearIpa": staTcpipArpTablearIpa,
       "staTcpipArpTablearNod": staTcpipArpTablearNod,
       "staTcpipArpTablearLas": staTcpipArpTablearLas,
       "staTcpipArpTablearCon": staTcpipArpTablearCon,
       "staTcpipArpDeletev": staTcpipArpDeletev,
       "staTcpipIps": staTcpipIps,
       "staTcpipIpsIplanrx": staTcpipIpsIplanrx,
       "staTcpipIpsIplantx": staTcpipIpsIplantx,
       "staTcpipIpsIplanchecksumerrors": staTcpipIpsIplanchecksumerrors,
       "staTcpipIpsIplanserviceerrors": staTcpipIpsIplanserviceerrors,
       "staTcpipIpsIpwanrx": staTcpipIpsIpwanrx,
       "staTcpipIpsIpwantx": staTcpipIpsIpwantx,
       "staTcpipIpsIpwanchecksumerrors": staTcpipIpsIpwanchecksumerrors,
       "staTcpipIpsIpwanserviceerrors": staTcpipIpsIpwanserviceerrors,
       "staTcpipIpsIpwanrxdisconnect": staTcpipIpsIpwanrxdisconnect,
       "staTcpipIpsIplanfragmentationer": staTcpipIpsIplanfragmentationer,
       "staTcpipIpsIpwanfragmentationer": staTcpipIpsIpwanfragmentationer,
       "staTcpipIpsDeletevalues": staTcpipIpsDeletevalues,
       "staTcpipIpsIplanfragmentations": staTcpipIpsIplanfragmentations,
       "staTcpipIpsIplanfragmentationsf": staTcpipIpsIplanfragmentationsf,
       "staTcpipIpsIpwanfragmentations": staTcpipIpsIpwanfragmentations,
       "staTcpipIpsIpwanfragmentationsf": staTcpipIpsIpwanfragmentationsf,
       "staTcpipIcm": staTcpipIcm,
       "staTcpipIcmIcmplanr": staTcpipIcmIcmplanr,
       "staTcpipIcmIcmplant": staTcpipIcmIcmplant,
       "staTcpipIcmIcmplanc": staTcpipIcmIcmplanc,
       "staTcpipIcmIcmplans": staTcpipIcmIcmplans,
       "staTcpipIcmIcmpwanr": staTcpipIcmIcmpwanr,
       "staTcpipIcmIcmpwant": staTcpipIcmIcmpwant,
       "staTcpipIcmIcmpwanc": staTcpipIcmIcmpwanc,
       "staTcpipIcmIcmpwans": staTcpipIcmIcmpwans,
       "staTcpipIcmDeleteva": staTcpipIcmDeleteva,
       "staTcpipTft": staTcpipTft,
       "staTcpipTftTftplanrx": staTcpipTftTftplanrx,
       "staTcpipTftTftplanrxr": staTcpipTftTftplanrxr,
       "staTcpipTftTftplanrxw": staTcpipTftTftplanrxw,
       "staTcpipTftTftplanrxd": staTcpipTftTftplanrxd,
       "staTcpipTftTftplanrxa": staTcpipTftTftplanrxa,
       "staTcpipTftTftplanrxo": staTcpipTftTftplanrxo,
       "staTcpipTftTftplanrxe": staTcpipTftTftplanrxe,
       "staTcpipTftTftplanrxb": staTcpipTftTftplanrxb,
       "staTcpipTftTftplantx": staTcpipTftTftplantx,
       "staTcpipTftTftplantxd": staTcpipTftTftplantxd,
       "staTcpipTftTftplantxa": staTcpipTftTftplantxa,
       "staTcpipTftTftplantxo": staTcpipTftTftplantxo,
       "staTcpipTftTftplantxe": staTcpipTftTftplantxe,
       "staTcpipTftTftplantxr": staTcpipTftTftplantxr,
       "staTcpipTftTftplancon": staTcpipTftTftplancon,
       "staTcpipTftTftpwanrx": staTcpipTftTftpwanrx,
       "staTcpipTftTftpwanrxr": staTcpipTftTftpwanrxr,
       "staTcpipTftTftpwanrxw": staTcpipTftTftpwanrxw,
       "staTcpipTftTftpwanrxd": staTcpipTftTftpwanrxd,
       "staTcpipTftTftpwanrxa": staTcpipTftTftpwanrxa,
       "staTcpipTftTftpwanrxo": staTcpipTftTftpwanrxo,
       "staTcpipTftTftpwanrxe": staTcpipTftTftpwanrxe,
       "staTcpipTftTftpwanrxb": staTcpipTftTftpwanrxb,
       "staTcpipTftTftpwantx": staTcpipTftTftpwantx,
       "staTcpipTftTftpwantxd": staTcpipTftTftpwantxd,
       "staTcpipTftTftpwantxa": staTcpipTftTftpwantxa,
       "staTcpipTftTftpwantxo": staTcpipTftTftpwantxo,
       "staTcpipTftTftpwantxe": staTcpipTftTftpwantxe,
       "staTcpipTftTftpwantxr": staTcpipTftTftpwantxr,
       "staTcpipTftTftpwancon": staTcpipTftTftpwancon,
       "staTcpipTftDeletevalu": staTcpipTftDeletevalu,
       "staTcpipTcp": staTcpipTcp,
       "staTcpipTcpTcplanrx": staTcpipTcpTcplanrx,
       "staTcpipTcpTcplantx": staTcpipTcpTcplantx,
       "staTcpipTcpTcplantxr": staTcpipTcpTcplantxr,
       "staTcpipTcpTcplanche": staTcpipTcpTcplanche,
       "staTcpipTcpTcplanser": staTcpipTcpTcplanser,
       "staTcpipTcpTcplancon": staTcpipTcpTcplancon,
       "staTcpipTcpTcpwanrx": staTcpipTcpTcpwanrx,
       "staTcpipTcpTcpwantx": staTcpipTcpTcpwantx,
       "staTcpipTcpTcpwantxr": staTcpipTcpTcpwantxr,
       "staTcpipTcpTcpwanche": staTcpipTcpTcpwanche,
       "staTcpipTcpTcpwanser": staTcpipTcpTcpwanser,
       "staTcpipTcpTcpwancon": staTcpipTcpTcpwancon,
       "staTcpipTcpDeleteval": staTcpipTcpDeleteval,
       "staTcpipDhc": staTcpipDhc,
       "staTcpipDhcDhcplanrx": staTcpipDhcDhcplanrx,
       "staTcpipDhcDhcplantx": staTcpipDhcDhcplantx,
       "staTcpipDhcDhcpwanrx": staTcpipDhcDhcpwanrx,
       "staTcpipDhcDhcpdisca": staTcpipDhcDhcpdisca,
       "staTcpipDhcDhcprxdis": staTcpipDhcDhcprxdis,
       "staTcpipDhcDhcprxreq": staTcpipDhcDhcprxreq,
       "staTcpipDhcDhcprxdec": staTcpipDhcDhcprxdec,
       "staTcpipDhcDhcprxinf": staTcpipDhcDhcprxinf,
       "staTcpipDhcDhcprxrel": staTcpipDhcDhcprxrel,
       "staTcpipDhcDhcptxoff": staTcpipDhcDhcptxoff,
       "staTcpipDhcDhcptxack": staTcpipDhcDhcptxack,
       "staTcpipDhcDhcptxnak": staTcpipDhcDhcptxnak,
       "staTcpipDhcDchpserve": staTcpipDhcDchpserve,
       "staTcpipDhcDhcpassig": staTcpipDhcDhcpassig,
       "staTcpipDhcDhcpmacco": staTcpipDhcDhcpmacco,
       "staTcpipDhcTabledhcp": staTcpipDhcTabledhcp,
       "staTcpipDhcTabledhcpCols": staTcpipDhcTabledhcpCols,
       "staTcpipDhcTabledhcpIpa": staTcpipDhcTabledhcpIpa,
       "staTcpipDhcTabledhcpNod": staTcpipDhcTabledhcpNod,
       "staTcpipDhcTabledhcpTim": staTcpipDhcTabledhcpTim,
       "staTcpipDhcTabledhcpHos": staTcpipDhcTabledhcpHos,
       "staTcpipDhcTabledhcpTyp": staTcpipDhcTabledhcpTyp,
       "staTcpipDhcServerfla": staTcpipDhcServerfla,
       "staTcpipDhcDeleteval": staTcpipDhcDeleteval,
       "staTcpipDel": staTcpipDel,
       "staTcpipNet": staTcpipNet,
       "staTcpipNetLanr": staTcpipNetLanr,
       "staTcpipNetLant": staTcpipNetLant,
       "staTcpipNetWanr": staTcpipNetWanr,
       "staTcpipNetWant": staTcpipNetWant,
       "staTcpipNetRegi": staTcpipNetRegi,
       "staTcpipNetConf": staTcpipNetConf,
       "staTcpipNetRele": staTcpipNetRele,
       "staTcpipNetRefr": staTcpipNetRefr,
       "staTcpipNetTime": staTcpipNetTime,
       "staTcpipNetHost": staTcpipNetHost,
       "staTcpipNetGrou": staTcpipNetGrou,
       "staTcpipNetBnod": staTcpipNetBnod,
       "staTcpipNetPnod": staTcpipNetPnod,
       "staTcpipNetMnod": staTcpipNetMnod,
       "staTcpipNetWnod": staTcpipNetWnod,
       "staTcpipNetRemo": staTcpipNetRemo,
       "staTcpipNetRemoCols": staTcpipNetRemoCols,
       "staTcpipNetRemoNam": staTcpipNetRemoNam,
       "staTcpipNetRemoTyp": staTcpipNetRemoTyp,
       "staTcpipNetRemoBac": staTcpipNetRemoBac,
       "staTcpipNetRemoTim": staTcpipNetRemoTim,
       "staTcpipNetDele": staTcpipNetDele,
       "staTcpipDns": staTcpipDns,
       "staTcpipDnsLanr": staTcpipDnsLanr,
       "staTcpipDnsLant": staTcpipDnsLant,
       "staTcpipDnsWanr": staTcpipDnsWanr,
       "staTcpipDnsWant": staTcpipDnsWant,
       "staTcpipDnsForw": staTcpipDnsForw,
       "staTcpipDnsErro": staTcpipDnsErro,
       "staTcpipDnsDnsa": staTcpipDnsDnsa,
       "staTcpipDnsDhcp": staTcpipDnsDhcp,
       "staTcpipDnsNetb": staTcpipDnsNetb,
       "staTcpipDnsFilt": staTcpipDnsFilt,
       "staTcpipDnsHitl": staTcpipDnsHitl,
       "staTcpipDnsHitlCols": staTcpipDnsHitlCols,
       "staTcpipDnsHitlDom": staTcpipDnsHitlDom,
       "staTcpipDnsHitlReq": staTcpipDnsHitlReq,
       "staTcpipDnsHitlTim": staTcpipDnsHitlTim,
       "staTcpipDnsHitlIpa": staTcpipDnsHitlIpa,
       "staTcpipDnsDele": staTcpipDnsDele,
       "staTcpipHtt": staTcpipHtt,
       "staTcpipHttHttpac": staTcpipHttHttpac,
       "staTcpipHttHttpno": staTcpipHttHttpno,
       "staTcpipHttHttpau": staTcpipHttHttpau,
       "staTcpipHttHttppr": staTcpipHttHttppr,
       "staTcpipHttDelete": staTcpipHttDelete,
       "staIprou": staIprou,
       "staIprouIprlanrx": staIprouIprlanrx,
       "staIprouIprlantx": staIprouIprlantx,
       "staIprouIprlanlo": staIprouIprlanlo,
       "staIprouIprlanne": staIprouIprlanne,
       "staIprouIprlanro": staIprouIprlanro,
       "staIprouIprlantt": staIprouIprlantt,
       "staIprouIprlanfi": staIprouIprlanfi,
       "staIprouIprlandi": staIprouIprlandi,
       "staIprouIprwanrx": staIprouIprwanrx,
       "staIprouIprwantx": staIprouIprwantx,
       "staIprouIprwanne": staIprouIprwanne,
       "staIprouIprwantt": staIprouIprwantt,
       "staIprouIprwanfi": staIprouIprwanfi,
       "staIprouIprwandi": staIprouIprwandi,
       "staIprouIprwanty": staIprouIprwanty,
       "staIprouIprarper": staIprouIprarper,
       "staIprouEstablis": staIprouEstablis,
       "staIprouEstablisCols": staIprouEstablisCols,
       "staIprouEstablisTim": staIprouEstablisTim,
       "staIprouEstablisDes": staIprouEstablisDes,
       "staIprouEstablisSrc": staIprouEstablisSrc,
       "staIprouEstablisPro": staIprouEstablisPro,
       "staIprouEstablisDpo": staIprouEstablisDpo,
       "staIprouEstablisSpo": staIprouEstablisSpo,
       "staConfi": staConfi,
       "staConfiLanactiv": staConfiLanactiv,
       "staConfiLantotal": staConfiLantotal,
       "staConfiWanactiv": staConfiWanactiv,
       "staConfiWantotal": staConfiWantotal,
       "staConfiOutbanda": staConfiOutbanda,
       "staConfiOutbandt": staConfiOutbandt,
       "staConfiOutbandb": staConfiOutbandb,
       "staConfiLoginerr": staConfiLoginerr,
       "staConfiLoginloc": staConfiLoginloc,
       "staConfiLoginrej": staConfiLoginrej,
       "staConfiDeleteva": staConfiDeleteva,
       "staQueue": staQueue,
       "staQueueLanheap": staQueueLanheap,
       "staQueueLanqueu": staQueueLanqueu,
       "staQueueWanheap": staQueueWanheap,
       "staQueueWanqueu": staQueueWanqueu,
       "staQueueBridgei": staQueueBridgei,
       "staQueueBridgee": staQueueBridgee,
       "staQueueArpquer": staQueueArpquer,
       "staQueueArpqueu": staQueueArpqueu,
       "staQueueIpqueue": staQueueIpqueue,
       "staQueueIpurgen": staQueueIpurgen,
       "staQueueIcmpque": staQueueIcmpque,
       "staQueueTcpqueu": staQueueTcpqueu,
       "staQueueTftpser": staQueueTftpser,
       "staQueueSnmpque": staQueueSnmpque,
       "staQueueIpxqueu": staQueueIpxqueu,
       "staQueueRipquer": staQueueRipquer,
       "staQueueSapqueu": staQueueSapqueu,
       "staQueueIpxwatc": staQueueIpxwatc,
       "staQueueSpxwatc": staQueueSpxwatc,
       "staQueueIpxrout": staQueueIpxrout,
       "staQueueProthea": staQueueProthea,
       "staQueueIprqueu": staQueueIprqueu,
       "staQueueDhcpser": staQueueDhcpser,
       "staQueueDhcpcli": staQueueDhcpcli,
       "staQueueIprripq": staQueueIprripq,
       "staQueueDnstxqu": staQueueDnstxqu,
       "staQueueDnsrxqu": staQueueDnsrxqu,
       "staQueueIpmasqt": staQueueIpmasqt,
       "staQueueIpmasqr": staQueueIpmasqr,
       "staConns": staConns,
       "staConnsCols": staConnsCols,
       "staConnsIfc": staConnsIfc,
       "staConnsConn": staConnsConn,
       "staConnsActi": staConnsActi,
       "staConnsPass": staConnsPass,
       "staConnsErro": staConnsErro,
       "staConnsCont": staConnsCont,
       "staConnsChar": staConnsChar,
       "staInfoc": staInfoc,
       "staInfocCols": staInfocCols,
       "staInfocIfc": staInfocIfc,
       "staInfocSta": staInfocSta,
       "staInfocMod": staInfocMod,
       "staInfocDia": staInfocDia,
       "staInfocDev": staInfocDev,
       "staInfocB1d": staInfocB1d,
       "staInfocB2d": staInfocB2d,
       "staLayer": staLayer,
       "staLayerCols": staLayerCols,
       "staLayerIfc": staLayerIfc,
       "staLayerWanl": staLayerWanl,
       "staLayerEnca": staLayerEnca,
       "staLayerLay3": staLayerLay3,
       "staLayerLay2": staLayerLay2,
       "staLayerL2op": staLayerL2op,
       "staLayerLay1": staLayerLay1,
       "staLayerL1pa": staLayerL1pa,
       "staCalli": staCalli,
       "staCalliCols": staCalliCols,
       "staCalliSys": staCalliSys,
       "staCalliIfc": staCalliIfc,
       "staCalliCli": staCalliCli,
       "staCalliDia": staCalliDia,
       "staCalliCap": staCalliCap,
       "staCalliBch": staCalliBch,
       "staRemot": staRemot,
       "staRemotCols": staRemotCols,
       "staRemotConns": staRemotConns,
       "staRemotRemot": staRemotRemot,
       "staRemotMode": staRemotMode,
       "staRemotIfc": staRemotIfc,
       "staRemotConnt": staRemotConnt,
       "staRemotCharg": staRemotCharg,
       "staCurre": staCurre,
       "staChann": staChann,
       "staChannCols": staChannCols,
       "staChannChan": staChannChan,
       "staChannPlci": staChannPlci,
       "staChannBus": staChannBus,
       "staChannState": staChannState,
       "staChannApp": staChannApp,
       "staChannMode": staChannMode,
       "staChannCause": staChannCause,
       "staChannNumbe": staChannNumbe,
       "staChannSubad": staChannSubad,
       "staChannCharg": staChannCharg,
       "staChannExtra": staChannExtra,
       "staChannConnt": staChannConnt,
       "staChannConns": staChannConns,
       "staChannIsdnd": staChannIsdnd,
       "staDelet": staDelet,
       "staTimes": staTimes,
       "staTimesCur": staTimesCur,
       "staTimesSou": staTimesSou,
       "staTimesSet": staTimesSet,
       "staTimesIsd": staTimesIsd,
       "staTimesIsdConne": staTimesIsdConne,
       "staTimesIsdInfor": staTimesIsdInfor,
       "staTimesIsdInfoe": staTimesIsdInfoe,
       "staTimesIsdUnits": staTimesIsdUnits,
       "staTimesIsdDelet": staTimesIsdDelet,
       "staLcrst": staLcrst,
       "staLcrstTot": staLcrstTot,
       "staLcrstFou": staLcrstFou,
       "staLcrstNot": staLcrstNot,
       "staLcrstMis": staLcrstMis,
       "staLcrstPro": staLcrstPro,
       "staLcrstProCols": staLcrstProCols,
       "staLcrstProPro": staLcrstProPro,
       "staLcrstProFai": staLcrstProFai,
       "staLcrstProSuc": staLcrstProSuc,
       "staLcrstDel": staLcrstDel,
       "staS0bus": staS0bus,
       "staS0busDin": staS0busDin,
       "staS0busDinCols": staS0busDinCols,
       "staS0busDinCha": staS0busDinCha,
       "staS0busDinPro": staS0busDinPro,
       "staS0busDinLay": staS0busDinLay,
       "staS0busDinTei": staS0busDinTei,
       "staS0busDinS0a": staS0busDinS0a,
       "staS0busD2s": staS0busD2s,
       "staS0busD2sCols": staS0busD2sCols,
       "staS0busD2sCha": staS0busD2sCha,
       "staS0busD2sTei": staS0busD2sTei,
       "staS0busD2sL2a": staS0busD2sL2a,
       "staS0busD2sCon": staS0busD2sCon,
       "staCharg": staCharg,
       "staChargSparemi": staChargSparemi,
       "staChargTimetab": staChargTimetab,
       "staChargTimetabCols": staChargTimetabCols,
       "staChargTimetabIfc": staChargTimetabIfc,
       "staChargTimetabBudgetmi": staChargTimetabBudgetmi,
       "staChargTimetabSparemin": staChargTimetabSparemin,
       "staChargTimetabMinutesa": staChargTimetabMinutesa,
       "staChargTimetabMinutesp": staChargTimetabMinutesp,
       "staChargDeletev": staChargDeletev,
       "staChargSpareun": staChargSpareun,
       "staChargTablebu": staChargTablebu,
       "staChargTablebuCols": staChargTablebuCols,
       "staChargTablebuIfc": staChargTablebuIfc,
       "staChargTablebuBud": staChargTablebuBud,
       "staChargTablebuSpa": staChargTablebuSpa,
       "staChargTablebuTot": staChargTablebuTot,
       "staChargSpareda": staChargSpareda,
       "staChargRouteru": staChargRouteru,
       "staChargTotalun": staChargTotalun,
       "staChargRouterm": staChargRouterm,
       "staDhcpc": staDhcpc,
       "staDhcpcState": staDhcpcState,
       "staDhcpcLeaseti": staDhcpcLeaseti,
       "staDhcpcYouripa": staDhcpcYouripa,
       "staDhcpcYouripn": staDhcpcYouripn,
       "staDhcpcGateway": staDhcpcGateway,
       "staDhcpcServeri": staDhcpcServeri,
       "staDhcpcSecurit": staDhcpcSecurit,
       "staDhcpcTimeoff": staDhcpcTimeoff,
       "staDhcpcTimeser": staDhcpcTimeser,
       "staDhcpcTableti": staDhcpcTableti,
       "staDhcpcTabletiCols": staDhcpcTabletiCols,
       "staDhcpcTabletiIpa": staDhcpcTabletiIpa,
       "staDhcpcTablero": staDhcpcTablero,
       "staDhcpcTableroCols": staDhcpcTableroCols,
       "staDhcpcTableroIpa": staDhcpcTableroIpa,
       "staDhcpcTablena": staDhcpcTablena,
       "staDhcpcTablenaCols": staDhcpcTablenaCols,
       "staDhcpcTablenaIpa": staDhcpcTablenaIpa,
       "staDhcpcTabledo": staDhcpcTabledo,
       "staDhcpcTabledoCols": staDhcpcTabledoCols,
       "staDhcpcTabledoIpa": staDhcpcTabledoIpa,
       "staDhcpcTablelo": staDhcpcTablelo,
       "staDhcpcTableloCols": staDhcpcTableloCols,
       "staDhcpcTableloIpa": staDhcpcTableloIpa,
       "staDhcpcConfigu": staDhcpcConfigu,
       "set": set,
       "setName": setName,
       "setWanm": setWanm,
       "setWanmName": setWanmName,
       "setWanmNameCols": setWanmNameCols,
       "setWanmNameDev": setWanmNameDev,
       "setWanmNameDia": setWanmNameDia,
       "setWanmNameB1d": setWanmNameB1d,
       "setWanmNameB2d": setWanmNameB2d,
       "setWanmNameWan": setWanmNameWan,
       "setWanmNameCal": setWanmNameCal,
       "setWanmRoun": setWanmRoun,
       "setWanmRounCols": setWanmRounCols,
       "setWanmRounDev": setWanmRounDev,
       "setWanmRounRou": setWanmRounRou,
       "setWanmRounHea": setWanmRounHea,
       "setWanmLaye": setWanmLaye,
       "setWanmLayeCols": setWanmLayeCols,
       "setWanmLayeWanl": setWanmLayeWanl,
       "setWanmLayeEnca": setWanmLayeEnca,
       "setWanmLayeLay3": setWanmLayeLay3,
       "setWanmLayeLay2": setWanmLayeLay2,
       "setWanmLayeL2op": setWanmLayeL2op,
       "setWanmLayeLay1": setWanmLayeLay1,
       "setWanmPppl": setWanmPppl,
       "setWanmPpplCols": setWanmPpplCols,
       "setWanmPpplDev": setWanmPpplDev,
       "setWanmPpplAut": setWanmPpplAut,
       "setWanmPpplKey": setWanmPpplKey,
       "setWanmPpplTim": setWanmPpplTim,
       "setWanmPpplTry": setWanmPpplTry,
       "setWanmPpplUse": setWanmPpplUse,
       "setWanmPpplCon": setWanmPpplCon,
       "setWanmPpplFai": setWanmPpplFai,
       "setWanmPpplTer": setWanmPpplTer,
       "setWanmNumb": setWanmNumb,
       "setWanmNumbCols": setWanmNumbCols,
       "setWanmNumbDia": setWanmNumbDia,
       "setWanmNumbDev": setWanmNumbDev,
       "setWanmDial": setWanmDial,
       "setWanmScri": setWanmScri,
       "setWanmScriCols": setWanmScriCols,
       "setWanmScriDev": setWanmScriDev,
       "setWanmScriScr": setWanmScriScr,
       "setWanmProt": setWanmProt,
       "setWanmCbat": setWanmCbat,
       "setWanmRout": setWanmRout,
       "setWanmRoutCols": setWanmRoutCols,
       "setWanmRoutIfc": setWanmRoutIfc,
       "setWanmRoutMsn": setWanmRoutMsn,
       "setWanmRoutCli": setWanmRoutCli,
       "setWanmRoutYc": setWanmRoutYc,
       "setWanmManu": setWanmManu,
       "setWanmManuCon": setWanmManuCon,
       "setWanmManuDis": setWanmManuDis,
       "setWanmInte": setWanmInte,
       "setWanmInteCols": setWanmInteCols,
       "setWanmInteIfc": setWanmInteIfc,
       "setWanmInteProt": setWanmInteProt,
       "setWanmInteLlmo": setWanmInteLlmo,
       "setWanmInteLlbc": setWanmInteLlbc,
       "setWanmInteDial": setWanmInteDial,
       "setWanmInteMaxi": setWanmInteMaxi,
       "setWanmInteMaxo": setWanmInteMaxo,
       "setChar": setChar,
       "setCharBudgetu": setCharBudgetu,
       "setCharDaysper": setCharDaysper,
       "setCharSpareun": setCharSpareun,
       "setCharRouteru": setCharRouteru,
       "setCharTablebu": setCharTablebu,
       "setCharTablebuCols": setCharTablebuCols,
       "setCharTablebuIfc": setCharTablebuIfc,
       "setCharTablebuBud": setCharTablebuBud,
       "setCharTablebuSpa": setCharTablebuSpa,
       "setCharTablebuTot": setCharTablebuTot,
       "setCharTotalun": setCharTotalun,
       "setCharTimetab": setCharTimetab,
       "setCharTimetabCols": setCharTimetabCols,
       "setCharTimetabIfc": setCharTimetabIfc,
       "setCharTimetabBudgetmi": setCharTimetabBudgetmi,
       "setCharTimetabSparemin": setCharTimetabSparemin,
       "setCharTimetabMinutesa": setCharTimetabMinutesa,
       "setCharTimetabMinutesp": setCharTimetabMinutesp,
       "setCharMinutes": setCharMinutes,
       "setCharSparemi": setCharSparemi,
       "setCharRouterm": setCharRouterm,
       "setLanm": setLanm,
       "setLanmCon": setLanmCon,
       "setLanmNod": setLanmNod,
       "setLanmSpa": setLanmSpa,
       "setBrid": setBrid,
       "setBridOpe": setBridOpe,
       "setBridRem": setBridRem,
       "setBridTab": setBridTab,
       "setBridTabCols": setBridTabCols,
       "setBridTabNod": setBridTabNod,
       "setBridTabLas": setBridTabLas,
       "setBridTabFor": setBridTabFor,
       "setBridAgi": setBridAgi,
       "setBridLan": setBridLan,
       "setBridLanBro": setBridLanBro,
       "setBridLanMul": setBridLanMul,
       "setBridLanDes": setBridLanDes,
       "setBridLanDesFilterty": setBridLanDesFilterty,
       "setBridLanDesFilterta": setBridLanDesFilterta,
       "setBridLanDesFiltertaCols": setBridLanDesFiltertaCols,
       "setBridLanDesFiltertaDes": setBridLanDesFiltertaDes,
       "setBridLanSrc": setBridLanSrc,
       "setBridLanSrcFilterty": setBridLanSrcFilterty,
       "setBridLanSrcFilterta": setBridLanSrcFilterta,
       "setBridLanSrcFiltertaCols": setBridLanSrcFiltertaCols,
       "setBridLanSrcFiltertaSrc": setBridLanSrcFiltertaSrc,
       "setBridWan": setBridWan,
       "setBridWanBro": setBridWanBro,
       "setBridWanMul": setBridWanMul,
       "setBridWanDes": setBridWanDes,
       "setBridWanDesFilterty": setBridWanDesFilterty,
       "setBridWanDesFilterta": setBridWanDesFilterta,
       "setBridWanDesFiltertaCols": setBridWanDesFiltertaCols,
       "setBridWanDesFiltertaDes": setBridWanDesFiltertaDes,
       "setBridWanSrc": setBridWanSrc,
       "setBridWanSrcFilterty": setBridWanSrcFilterty,
       "setBridWanSrcFilterta": setBridWanSrcFilterta,
       "setBridWanSrcFiltertaCols": setBridWanSrcFiltertaCols,
       "setBridWanSrcFiltertaDes": setBridWanSrcFiltertaDes,
       "setIpxm": setIpxm,
       "setIpxmOpe": setIpxmOpe,
       "setIpxmIpx": setIpxmIpx,
       "setIpxmLan": setIpxmLan,
       "setIpxmLanNetw": setIpxmLanNetw,
       "setIpxmLanBind": setIpxmLanBind,
       "setIpxmLanSpxw": setIpxmLanSpxw,
       "setIpxmLanIpxw": setIpxmLanIpxw,
       "setIpxmLanNetb": setIpxmLanNetb,
       "setIpxmLanSock": setIpxmLanSock,
       "setIpxmLanSockCols": setIpxmLanSockCols,
       "setIpxmLanSockSta": setIpxmLanSockSta,
       "setIpxmLanSockEnd": setIpxmLanSockEnd,
       "setIpxmLanLocr": setIpxmLanLocr,
       "setIpxmLanRips": setIpxmLanRips,
       "setIpxmLanLoop": setIpxmLanLoop,
       "setIpxmWan": setIpxmWan,
       "setIpxmWanRou": setIpxmWanRou,
       "setIpxmWanRouCols": setIpxmWanRouCols,
       "setIpxmWanRouRem": setIpxmWanRouRem,
       "setIpxmWanRouNet": setIpxmWanRouNet,
       "setIpxmWanRouBin": setIpxmWanRouBin,
       "setIpxmWanRouPro": setIpxmWanRouPro,
       "setIpxmWanRouBac": setIpxmWanRouBac,
       "setIpxmWanSoc": setIpxmWanSoc,
       "setIpxmWanSocCols": setIpxmWanSocCols,
       "setIpxmWanSocSta": setIpxmWanSocSta,
       "setIpxmWanSocEnd": setIpxmWanSocEnd,
       "setIpxmRip": setIpxmRip,
       "setIpxmRipTabl": setIpxmRipTabl,
       "setIpxmRipTablCols": setIpxmRipTablCols,
       "setIpxmRipTablNet": setIpxmRipTablNet,
       "setIpxmRipTablHop": setIpxmRipTablHop,
       "setIpxmRipTablTic": setIpxmRipTablTic,
       "setIpxmRipTablNod": setIpxmRipTablNod,
       "setIpxmRipTablTim": setIpxmRipTablTim,
       "setIpxmRipTablFla": setIpxmRipTablFla,
       "setIpxmRipLanf": setIpxmRipLanf,
       "setIpxmRipLanfCols": setIpxmRipLanfCols,
       "setIpxmRipLanfSta": setIpxmRipLanfSta,
       "setIpxmRipLanfEnd": setIpxmRipLanfEnd,
       "setIpxmRipWanf": setIpxmRipWanf,
       "setIpxmRipWanfCols": setIpxmRipWanfCols,
       "setIpxmRipWanfSta": setIpxmRipWanfSta,
       "setIpxmRipWanfEnd": setIpxmRipWanfEnd,
       "setIpxmRipRout": setIpxmRipRout,
       "setIpxmRipAgin": setIpxmRipAgin,
       "setIpxmRipSpoo": setIpxmRipSpoo,
       "setIpxmRipWanu": setIpxmRipWanu,
       "setIpxmSap": setIpxmSap,
       "setIpxmSapTabl": setIpxmSapTabl,
       "setIpxmSapTablCols": setIpxmSapTablCols,
       "setIpxmSapTablTyp": setIpxmSapTablTyp,
       "setIpxmSapTablSer": setIpxmSapTablSer,
       "setIpxmSapTablNet": setIpxmSapTablNet,
       "setIpxmSapTablNod": setIpxmSapTablNod,
       "setIpxmSapTablSoc": setIpxmSapTablSoc,
       "setIpxmSapTablHop": setIpxmSapTablHop,
       "setIpxmSapTablTim": setIpxmSapTablTim,
       "setIpxmSapTablFla": setIpxmSapTablFla,
       "setIpxmSapLanf": setIpxmSapLanf,
       "setIpxmSapLanfCols": setIpxmSapLanfCols,
       "setIpxmSapLanfSta": setIpxmSapLanfSta,
       "setIpxmSapLanfEnd": setIpxmSapLanfEnd,
       "setIpxmSapWanf": setIpxmSapWanf,
       "setIpxmSapWanfCols": setIpxmSapWanfCols,
       "setIpxmSapWanfSta": setIpxmSapWanfSta,
       "setIpxmSapWanfEnd": setIpxmSapWanfEnd,
       "setIpxmSapServ": setIpxmSapServ,
       "setIpxmSapAgin": setIpxmSapAgin,
       "setIpxmSapSpoo": setIpxmSapSpoo,
       "setIpxmSapWanu": setIpxmSapWanu,
       "setTcpi": setTcpi,
       "setTcpiOperating": setTcpiOperating,
       "setTcpiIpaddress": setTcpiIpaddress,
       "setTcpiIpnetmask": setTcpiIpnetmask,
       "setTcpiIntraneta": setTcpiIntraneta,
       "setTcpiIntranetm": setTcpiIntranetm,
       "setTcpiAccesslis": setTcpiAccesslis,
       "setTcpiAccesslisCols": setTcpiAccesslisCols,
       "setTcpiAccesslisIpa": setTcpiAccesslisIpa,
       "setTcpiAccesslisIpn": setTcpiAccesslisIpn,
       "setTcpiDnsdefaul": setTcpiDnsdefaul,
       "setTcpiDnsbackup": setTcpiDnsbackup,
       "setTcpiNbnsdefau": setTcpiNbnsdefau,
       "setTcpiNbnsbacku": setTcpiNbnsbacku,
       "setTcpiArpagingm": setTcpiArpagingm,
       "setTcpiTcpagingm": setTcpiTcpagingm,
       "setTcpiTcpmaxcon": setTcpiTcpmaxcon,
       "setTcpiTablearp": setTcpiTablearp,
       "setTcpiTablearpCols": setTcpiTablearpCols,
       "setTcpiTablearpIpa": setTcpiTablearpIpa,
       "setTcpiTablearpNod": setTcpiTablearpNod,
       "setTcpiTablearpLas": setTcpiTablearpLas,
       "setTcpiTablearpCon": setTcpiTablearpCon,
       "setIpro": setIpro,
       "setIproOpe": setIproOpe,
       "setIproIpr": setIproIpr,
       "setIproIprCols": setIproIprCols,
       "setIproIprIpa": setIproIprIpa,
       "setIproIprIpn": setIproIprIpn,
       "setIproIprRou": setIproIprRou,
       "setIproIprDis": setIproIprDis,
       "setIproIprMas": setIproIprMas,
       "setIproPro": setIproPro,
       "setIproLoc": setIproLoc,
       "setIproRou": setIproRou,
       "setIproRouRou": setIproRouRou,
       "setIproRouIcm": setIproRouIcm,
       "setIproRip": setIproRip,
       "setIproRipRip": setIproRipRip,
       "setIproRipR1m": setIproRipR1m,
       "setIproRipTab": setIproRipTab,
       "setIproRipTabCols": setIproRipTabCols,
       "setIproRipTabIpa": setIproRipTabIpa,
       "setIproRipTabIpn": setIproRipTabIpn,
       "setIproRipTabTim": setIproRipTabTim,
       "setIproRipTabDis": setIproRipTabDis,
       "setIproRipTabRou": setIproRipTabRou,
       "setIproMas": setIproMas,
       "setIproMasTcpagings": setIproMasTcpagings,
       "setIproMasUdpagings": setIproMasUdpagings,
       "setIproMasIcmpaging": setIproMasIcmpaging,
       "setIproMasServiceta": setIproMasServiceta,
       "setIproMasServicetaCols": setIproMasServicetaCols,
       "setIproMasServicetaDpo": setIproMasServicetaDpo,
       "setIproMasServicetaInt": setIproMasServicetaInt,
       "setIproMasTablemasq": setIproMasTablemasq,
       "setIproMasTablemasqCols": setIproMasTablemasqCols,
       "setIproMasTablemasqInt": setIproMasTablemasqInt,
       "setIproMasTablemasqSpo": setIproMasTablemasqSpo,
       "setIproMasTablemasqPro": setIproMasTablemasqPro,
       "setIproMasTablemasqTim": setIproMasTablemasqTim,
       "setIproMasFragments": setIproMasFragments,
       "setIproMasFragmenta": setIproMasFragmenta,
       "setIproFir": setIproFir,
       "setIproFirObj": setIproFirObj,
       "setIproFirObjCols": setIproFirObjCols,
       "setIproFirObjNam": setIproFirObjNam,
       "setIproFirObjDes": setIproFirObjDes,
       "setIproFirRul": setIproFirRul,
       "setIproFirRulCols": setIproFirRulCols,
       "setIproFirRulNam": setIproFirRulNam,
       "setIproFirRulPro": setIproFirRulPro,
       "setIproFirRulSou": setIproFirRulSou,
       "setIproFirRulDes": setIproFirRulDes,
       "setIproFirRulAct": setIproFirRulAct,
       "setIproFirFil": setIproFirFil,
       "setIproFirFilCols": setIproFirFilCols,
       "setIproFirFilIdx": setIproFirFilIdx,
       "setIproFirFilProt": setIproFirFilProt,
       "setIproFirFilSrca": setIproFirFilSrca,
       "setIproFirFilSrcn": setIproFirFilSrcn,
       "setIproFirFilSst": setIproFirFilSst,
       "setIproFirFilSend": setIproFirFilSend,
       "setIproFirFilDsta": setIproFirFilDsta,
       "setIproFirFilDstn": setIproFirFilDstn,
       "setIproFirFilDst": setIproFirFilDst,
       "setIproFirFilDend": setIproFirFilDend,
       "setIproFirFilActi": setIproFirFilActi,
       "setIproDef": setIproDef,
       "setIproDefCols": setIproDefCols,
       "setIproDefInd": setIproDefInd,
       "setIproDefDay": setIproDefDay,
       "setIproDefSta": setIproDefSta,
       "setIproDefSto": setIproDefSto,
       "setIproDefDev": setIproDefDev,
       "setIproUsa": setIproUsa,
       "setSnmp": setSnmp,
       "setSnmpSen": setSnmpSen,
       "setSnmpIpt": setSnmpIpt,
       "setSnmpIptCols": setSnmpIptCols,
       "setSnmpIptTra": setSnmpIptTra,
       "setSnmpAdm": setSnmpAdm,
       "setSnmpLoc": setSnmpLoc,
       "setSnmpReg": setSnmpReg,
       "setSnmpDel": setSnmpDel,
       "setSnmpMon": setSnmpMon,
       "setSnmpMonCols": setSnmpMonCols,
       "setSnmpMonIpa": setSnmpMonIpa,
       "setSnmpMonPor": setSnmpMonPor,
       "setSnmpMonTim": setSnmpMonTim,
       "setSnmpMonMac": setSnmpMonMac,
       "setSnmpMonDev": setSnmpMonDev,
       "setSnmpPas": setSnmpPas,
       "setDhcp": setDhcp,
       "setDhcpOpe": setDhcpOpe,
       "setDhcpSta": setDhcpSta,
       "setDhcpEnd": setDhcpEnd,
       "setDhcpNet": setDhcpNet,
       "setDhcpBro": setDhcpBro,
       "setDhcpMax": setDhcpMax,
       "setDhcpDef": setDhcpDef,
       "setDhcpTab": setDhcpTab,
       "setDhcpTabCols": setDhcpTabCols,
       "setDhcpTabIpa": setDhcpTabIpa,
       "setDhcpTabNod": setDhcpTabNod,
       "setDhcpTabTim": setDhcpTabTim,
       "setDhcpTabHos": setDhcpTabHos,
       "setDhcpTabTyp": setDhcpTabTyp,
       "setDhcpHos": setDhcpHos,
       "setDhcpHosCols": setDhcpHosCols,
       "setDhcpHosNod": setDhcpHosNod,
       "setDhcpHosIpa": setDhcpHosIpa,
       "setDhcpHosHos": setDhcpHosHos,
       "setDhcpHosIma": setDhcpHosIma,
       "setDhcpAli": setDhcpAli,
       "setDhcpAliCols": setDhcpAliCols,
       "setDhcpAliImagea": setDhcpAliImagea,
       "setDhcpAliImagef": setDhcpAliImagef,
       "setDhcpAliImages": setDhcpAliImages,
       "setDhcpMas": setDhcpMas,
       "setDhcpRep": setDhcpRep,
       "setDhcpGat": setDhcpGat,
       "setDhcpRel": setDhcpRel,
       "setConf": setConf,
       "setConfLanc": setConfLanc,
       "setConfWanc": setConfWanc,
       "setConfPass": setConfPass,
       "setConfMaxi": setConfMaxi,
       "setConfConf": setConfConf,
       "setConfLang": setConfLang,
       "setConfLogi": setConfLogi,
       "setConfLock": setConfLock,
       "setConfFarc": setConfFarc,
       "setAbmo": setAbmo,
       "setAbmoPor": setAbmoPor,
       "setAbmoPorCols": setAbmoPorCols,
       "setAbmoPorPort": setAbmoPorPort,
       "setAbmoPorEazmsns": setAbmoPorEazmsns,
       "setAbmoPorCapab": setAbmoPorCapab,
       "setAbmoPorMode": setAbmoPorMode,
       "setAbmoPorClip": setAbmoPorClip,
       "setAbmoPorAutodialf": setAbmoPorAutodialf,
       "setAbmoPorAutodialn": setAbmoPorAutodialn,
       "setAbmoPorDevice": setAbmoPorDevice,
       "setAbmoRin": setAbmoRin,
       "setAbmoCou": setAbmoCou,
       "setAbmoPub": setAbmoPub,
       "setAbmoPubCols": setAbmoPubCols,
       "setAbmoPubPor": setAbmoPubPor,
       "setAbmoPubOff": setAbmoPubOff,
       "setAbmoPubFla": setAbmoPubFla,
       "setAbmoPubExc": setAbmoPubExc,
       "setAbmoCla": setAbmoCla,
       "setAbmoClaCols": setAbmoClaCols,
       "setAbmoClaPort": setAbmoClaPort,
       "setAbmoClaClassofservice": setAbmoClaClassofservice,
       "setAbmoClaBlockednumber1": setAbmoClaBlockednumber1,
       "setAbmoClaBlockednumber2": setAbmoClaBlockednumber2,
       "setAbmoPri": setAbmoPri,
       "setAbmoPriCols": setAbmoPriCols,
       "setAbmoPriPor": setAbmoPriPor,
       "setAbmoPriPri": setAbmoPriPri,
       "setLanc": setLanc,
       "setLancAcces": setLancAcces,
       "setLancAccesCols": setLancAccesCols,
       "setLancAccesIpa": setLancAccesIpa,
       "setLancAccesIpn": setLancAccesIpn,
       "setLancOpera": setLancOpera,
       "setLancUdppo": setLancUdppo,
       "setLancEazms": setLancEazms,
       "setLancPrioo": setLancPrioo,
       "setLancInter": setLancInter,
       "setLancInterCols": setLancInterCols,
       "setLancInterIfc": setLancInterIfc,
       "setLancInterOpe": setLancInterOpe,
       "setLancInterEaz": setLancInterEaz,
       "setLancInterFor": setLancInterFor,
       "setLancPrior": setLancPrior,
       "setLancPriorCols": setLancPriorCols,
       "setLancPriorIfc": setLancPriorIfc,
       "setLancPriorPri": setLancPriorPri,
       "setTime": setTime,
       "setTimeOpe": setTimeOpe,
       "setTimeCur": setTimeCur,
       "setTimeTim": setTimeTim,
       "setTimeCal": setTimeCal,
       "setTimeUtc": setTimeUtc,
       "setLcrm": setLcrm,
       "setLcrmRou": setLcrmRou,
       "setLcrmLan": setLcrmLan,
       "setLcrmAbp": setLcrmAbp,
       "setLcrmTim": setLcrmTim,
       "setLcrmTimCols": setLcrmTimCols,
       "setLcrmTimInd": setLcrmTimInd,
       "setLcrmTimPre": setLcrmTimPre,
       "setLcrmTimDay": setLcrmTimDay,
       "setLcrmTimSta": setLcrmTimSta,
       "setLcrmTimSto": setLcrmTimSto,
       "setLcrmTimNum": setLcrmTimNum,
       "setLcrmTimFal": setLcrmTimFal,
       "setLcrmCel": setLcrmCel,
       "setLcrmCelCols": setLcrmCelCols,
       "setLcrmCelInd": setLcrmCelInd,
       "setLcrmCelDat": setLcrmCelDat,
       "setNetb": setNetb,
       "setNetbOpe": setNetbOpe,
       "setNetbSco": setNetbSco,
       "setNetbNtd": setNetbNtd,
       "setNetbRem": setNetbRem,
       "setNetbRemCols": setNetbRemCols,
       "setNetbRemNam": setNetbRemNam,
       "setNetbRemTyp": setNetbRemTyp,
       "setNetbGro": setNetbGro,
       "setNetbGroCols": setNetbGroCols,
       "setNetbGroGro": setNetbGroGro,
       "setNetbGroTyp": setNetbGroTyp,
       "setNetbGroIpa": setNetbGroIpa,
       "setNetbGroRem": setNetbGroRem,
       "setNetbGroTim": setNetbGroTim,
       "setNetbGroFla": setNetbGroFla,
       "setNetbHos": setNetbHos,
       "setNetbHosCols": setNetbHosCols,
       "setNetbHosNam": setNetbHosNam,
       "setNetbHosTyp": setNetbHosTyp,
       "setNetbHosIpa": setNetbHosIpa,
       "setNetbHosRem": setNetbHosRem,
       "setNetbHosTim": setNetbHosTim,
       "setNetbHosFla": setNetbHosFla,
       "setNetbSer": setNetbSer,
       "setNetbSerCols": setNetbSerCols,
       "setNetbSerHos": setNetbSerHos,
       "setNetbSerGro": setNetbSerGro,
       "setNetbSerUpd": setNetbSerUpd,
       "setNetbSerIpa": setNetbSerIpa,
       "setNetbSerOsv": setNetbSerOsv,
       "setNetbSerSmb": setNetbSerSmb,
       "setNetbSerSer": setNetbSerSer,
       "setNetbSerRem": setNetbSerRem,
       "setNetbSerTim": setNetbSerTim,
       "setNetbSerFla": setNetbSerFla,
       "setNetbWat": setNetbWat,
       "setNetbUpd": setNetbUpd,
       "setNetbWan": setNetbWan,
       "setDnsm": setDnsm,
       "setDnsmOpe": setDnsmOpe,
       "setDnsmDom": setDnsmDom,
       "setDnsmDhc": setDnsmDhc,
       "setDnsmNet": setDnsmNet,
       "setDnsmDns": setDnsmDns,
       "setDnsmDnsCols": setDnsmDnsCols,
       "setDnsmDnsHos": setDnsmDnsHos,
       "setDnsmDnsIpa": setDnsmDnsIpa,
       "setDnsmFil": setDnsmFil,
       "setDnsmFilCols": setDnsmFilCols,
       "setDnsmFilIdx": setDnsmFilIdx,
       "setDnsmFilDom": setDnsmFilDom,
       "setDnsmFilIpa": setDnsmFilIpa,
       "setDnsmFilNet": setDnsmFilNet,
       "setDnsmLea": setDnsmLea,
       "setDnsmDyn": setDnsmDyn,
       "setDnsmDynCols": setDnsmDynCols,
       "setDnsmDynHos": setDnsmDynHos,
       "setDnsmDynIpa": setDnsmDynIpa,
       "setDnsmDynTim": setDnsmDynTim,
       "setAcco": setAcco,
       "setAccoOpe": setAccoOpe,
       "setAccoSav": setAccoSav,
       "setAccoSor": setAccoSor,
       "setAccoCur": setAccoCur,
       "setAccoCurCols": setAccoCurCols,
       "setAccoCurUsern": setAccoCurUsern,
       "setAccoCurMacad": setAccoCurMacad,
       "setAccoCurRemot": setAccoCurRemot,
       "setAccoCurConnt": setAccoCurConnt,
       "setAccoCurRxkby": setAccoCurRxkby,
       "setAccoCurTxkby": setAccoCurTxkby,
       "setAccoCurTotal": setAccoCurTotal,
       "setAccoCurConne": setAccoCurConne,
       "setAccoAcc": setAccoAcc,
       "setAccoAccCols": setAccoAccCols,
       "setAccoAccUsern": setAccoAccUsern,
       "setAccoAccMacad": setAccoAccMacad,
       "setAccoAccRemot": setAccoAccRemot,
       "setAccoAccConnt": setAccoAccConnt,
       "setAccoAccRxkby": setAccoAccRxkby,
       "setAccoAccTxkby": setAccoAccTxkby,
       "setAccoAccTotal": setAccoAccTotal,
       "setAccoAccConne": setAccoAccConne,
       "setAccoDel": setAccoDel,
       "setHttp": setHttp,
       "setHttpDoc": setHttpDoc,
       "setSysl": setSysl,
       "setSyslOpe": setSyslOpe,
       "setSyslTab": setSyslTab,
       "setSyslTabCols": setSyslTabCols,
       "setSyslTabIdx": setSyslTabIdx,
       "setSyslTabIpa": setSyslTabIpa,
       "setSyslTabSou": setSyslTabSou,
       "setSyslTabLev": setSyslTabLev,
       "setSyslFac": setSyslFac,
       "setSyslFacCols": setSyslFacCols,
       "setSyslFacSou": setSyslFacSou,
       "setSyslFacFac": setSyslFacFac,
       "setSyslPor": setSyslPor,
       "fir": fir,
       "firVer": firVer,
       "firVerCols": firVerCols,
       "firVerIfc": firVerIfc,
       "firVerMod": firVerMod,
       "firVerVer": firVerVer,
       "firVerSer": firVerSer,
       "firTab": firTab,
       "firTabCols": firTabCols,
       "firTabPos": firTabPos,
       "firTabSta": firTabSta,
       "firTabVer": firTabVer,
       "firTabDat": firTabDat,
       "firTabSiz": firTabSiz,
       "firTabInd": firTabInd,
       "firMod": firMod,
       "firTim": firTim,
       "oth": oth,
       "othMan": othMan,
       "othManCon": othManCon,
       "othManDis": othManDis,
       "othBoo": othBoo}
)
