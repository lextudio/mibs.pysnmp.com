# SNMP MIB module (NETSWITCH-DRIVERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSWITCH-DRIVERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:14 2024
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Icf_ObjectIdentity = ObjectIdentity
icf = _Icf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14)
)
_HpicfObjects_ObjectIdentity = ObjectIdentity
hpicfObjects = _HpicfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11)
)
_HpicfSwitch_ObjectIdentity = ObjectIdentity
hpicfSwitch = _HpicfSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5)
)
_HpSwitch_ObjectIdentity = ObjectIdentity
hpSwitch = _HpSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1)
)
_HpOpSystem_ObjectIdentity = ObjectIdentity
hpOpSystem = _HpOpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1)
)
_HpHwSystem_ObjectIdentity = ObjectIdentity
hpHwSystem = _HpHwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2)
)
_HpDriverStats_ObjectIdentity = ObjectIdentity
hpDriverStats = _HpDriverStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3)
)
_HpDriverStatsTable_Object = MibTable
hpDriverStatsTable = _HpDriverStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hpDriverStatsTable.setStatus("mandatory")
_HpDriverStatsEntry_Object = MibTableRow
hpDriverStatsEntry = _HpDriverStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1)
)
hpDriverStatsEntry.setIndexNames(
    (0, "NETSWITCH-DRIVERS-MIB", "hpDriverStatsIndex"),
)
if mibBuilder.loadTexts:
    hpDriverStatsEntry.setStatus("mandatory")


class _HpDriverStatsIndex_Type(Integer32):
    """Custom type hpDriverStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpDriverStatsIndex_Type.__name__ = "Integer32"
_HpDriverStatsIndex_Object = MibTableColumn
hpDriverStatsIndex = _HpDriverStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 1),
    _HpDriverStatsIndex_Type()
)
hpDriverStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsIndex.setStatus("mandatory")


class _HpDriverStatsType_Type(OctetString):
    """Custom type hpDriverStatsType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HpDriverStatsType_Type.__name__ = "OctetString"
_HpDriverStatsType_Object = MibTableColumn
hpDriverStatsType = _HpDriverStatsType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 2),
    _HpDriverStatsType_Type()
)
hpDriverStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsType.setStatus("mandatory")
_HpDriverStatsOctetsRxOk_Type = Integer32
_HpDriverStatsOctetsRxOk_Object = MibTableColumn
hpDriverStatsOctetsRxOk = _HpDriverStatsOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 3),
    _HpDriverStatsOctetsRxOk_Type()
)
hpDriverStatsOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsOctetsRxOk.setStatus("mandatory")
_HpDriverStatsFrameRxOk_Type = Integer32
_HpDriverStatsFrameRxOk_Object = MibTableColumn
hpDriverStatsFrameRxOk = _HpDriverStatsFrameRxOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 4),
    _HpDriverStatsFrameRxOk_Type()
)
hpDriverStatsFrameRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsFrameRxOk.setStatus("mandatory")
_HpDriverStatsTotalRxError_Type = Integer32
_HpDriverStatsTotalRxError_Object = MibTableColumn
hpDriverStatsTotalRxError = _HpDriverStatsTotalRxError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 5),
    _HpDriverStatsTotalRxError_Type()
)
hpDriverStatsTotalRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsTotalRxError.setStatus("mandatory")
_HpDriverStatsOctetTxOk_Type = Integer32
_HpDriverStatsOctetTxOk_Object = MibTableColumn
hpDriverStatsOctetTxOk = _HpDriverStatsOctetTxOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 6),
    _HpDriverStatsOctetTxOk_Type()
)
hpDriverStatsOctetTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsOctetTxOk.setStatus("mandatory")
_HpDriverStatsFrameTxOk_Type = Integer32
_HpDriverStatsFrameTxOk_Object = MibTableColumn
hpDriverStatsFrameTxOk = _HpDriverStatsFrameTxOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 7),
    _HpDriverStatsFrameTxOk_Type()
)
hpDriverStatsFrameTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsFrameTxOk.setStatus("mandatory")
_HpDriverStatsTotalTxError_Type = Integer32
_HpDriverStatsTotalTxError_Object = MibTableColumn
hpDriverStatsTotalTxError = _HpDriverStatsTotalTxError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 8),
    _HpDriverStatsTotalTxError_Type()
)
hpDriverStatsTotalTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsTotalTxError.setStatus("mandatory")
_HpDriverStatsOctetsRxPerSec_Type = Integer32
_HpDriverStatsOctetsRxPerSec_Object = MibTableColumn
hpDriverStatsOctetsRxPerSec = _HpDriverStatsOctetsRxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 9),
    _HpDriverStatsOctetsRxPerSec_Type()
)
hpDriverStatsOctetsRxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsOctetsRxPerSec.setStatus("mandatory")
_HpDriverStatsPeakOctetsRx_Type = Integer32
_HpDriverStatsPeakOctetsRx_Object = MibTableColumn
hpDriverStatsPeakOctetsRx = _HpDriverStatsPeakOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 10),
    _HpDriverStatsPeakOctetsRx_Type()
)
hpDriverStatsPeakOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsPeakOctetsRx.setStatus("mandatory")
_HpDriverStatsFramesRxPerSec_Type = Integer32
_HpDriverStatsFramesRxPerSec_Object = MibTableColumn
hpDriverStatsFramesRxPerSec = _HpDriverStatsFramesRxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 11),
    _HpDriverStatsFramesRxPerSec_Type()
)
hpDriverStatsFramesRxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsFramesRxPerSec.setStatus("mandatory")
_HpDriverStatsPeakFramesRx_Type = Integer32
_HpDriverStatsPeakFramesRx_Object = MibTableColumn
hpDriverStatsPeakFramesRx = _HpDriverStatsPeakFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 12),
    _HpDriverStatsPeakFramesRx_Type()
)
hpDriverStatsPeakFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsPeakFramesRx.setStatus("mandatory")
_HpDriverStatsOctetsTxPerSec_Type = Integer32
_HpDriverStatsOctetsTxPerSec_Object = MibTableColumn
hpDriverStatsOctetsTxPerSec = _HpDriverStatsOctetsTxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 13),
    _HpDriverStatsOctetsTxPerSec_Type()
)
hpDriverStatsOctetsTxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsOctetsTxPerSec.setStatus("mandatory")
_HpDriverStatsPeakOctetsTx_Type = Integer32
_HpDriverStatsPeakOctetsTx_Object = MibTableColumn
hpDriverStatsPeakOctetsTx = _HpDriverStatsPeakOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 14),
    _HpDriverStatsPeakOctetsTx_Type()
)
hpDriverStatsPeakOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsPeakOctetsTx.setStatus("mandatory")
_HpDriverStatsFramesTxPerSec_Type = Integer32
_HpDriverStatsFramesTxPerSec_Object = MibTableColumn
hpDriverStatsFramesTxPerSec = _HpDriverStatsFramesTxPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 15),
    _HpDriverStatsFramesTxPerSec_Type()
)
hpDriverStatsFramesTxPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsFramesTxPerSec.setStatus("mandatory")
_HpDriverStatsPeakFramesTx_Type = Integer32
_HpDriverStatsPeakFramesTx_Object = MibTableColumn
hpDriverStatsPeakFramesTx = _HpDriverStatsPeakFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 1, 1, 16),
    _HpDriverStatsPeakFramesTx_Type()
)
hpDriverStatsPeakFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDriverStatsPeakFramesTx.setStatus("mandatory")
_HpFddiDriverStatsTable_Object = MibTable
hpFddiDriverStatsTable = _HpFddiDriverStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hpFddiDriverStatsTable.setStatus("mandatory")
_HpFddiDriverStatsEntry_Object = MibTableRow
hpFddiDriverStatsEntry = _HpFddiDriverStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1)
)
hpFddiDriverStatsEntry.setIndexNames(
    (0, "NETSWITCH-DRIVERS-MIB", "hpFddiDriverStatsIndex"),
)
if mibBuilder.loadTexts:
    hpFddiDriverStatsEntry.setStatus("mandatory")


class _HpFddiDriverStatsIndex_Type(Integer32):
    """Custom type hpFddiDriverStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpFddiDriverStatsIndex_Type.__name__ = "Integer32"
_HpFddiDriverStatsIndex_Object = MibTableColumn
hpFddiDriverStatsIndex = _HpFddiDriverStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 1),
    _HpFddiDriverStatsIndex_Type()
)
hpFddiDriverStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsIndex.setStatus("mandatory")
_HpFddiDriverStatsSMTOctetsRxOk_Type = Integer32
_HpFddiDriverStatsSMTOctetsRxOk_Object = MibTableColumn
hpFddiDriverStatsSMTOctetsRxOk = _HpFddiDriverStatsSMTOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 2),
    _HpFddiDriverStatsSMTOctetsRxOk_Type()
)
hpFddiDriverStatsSMTOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsSMTOctetsRxOk.setStatus("mandatory")
_HpFddiDriverStatsSMTFrameRxOk_Type = Integer32
_HpFddiDriverStatsSMTFrameRxOk_Object = MibTableColumn
hpFddiDriverStatsSMTFrameRxOk = _HpFddiDriverStatsSMTFrameRxOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 3),
    _HpFddiDriverStatsSMTFrameRxOk_Type()
)
hpFddiDriverStatsSMTFrameRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsSMTFrameRxOk.setStatus("mandatory")
_HpFddiDriverStatsSMTOctetsTxOk_Type = Integer32
_HpFddiDriverStatsSMTOctetsTxOk_Object = MibTableColumn
hpFddiDriverStatsSMTOctetsTxOk = _HpFddiDriverStatsSMTOctetsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 4),
    _HpFddiDriverStatsSMTOctetsTxOk_Type()
)
hpFddiDriverStatsSMTOctetsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsSMTOctetsTxOk.setStatus("mandatory")
_HpFddiDriverStatsSMTFrameTxOk_Type = Integer32
_HpFddiDriverStatsSMTFrameTxOk_Object = MibTableColumn
hpFddiDriverStatsSMTFrameTxOk = _HpFddiDriverStatsSMTFrameTxOk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 5),
    _HpFddiDriverStatsSMTFrameTxOk_Type()
)
hpFddiDriverStatsSMTFrameTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsSMTFrameTxOk.setStatus("mandatory")
_HpFddiDriverStatsErrRxCRC_Type = Integer32
_HpFddiDriverStatsErrRxCRC_Object = MibTableColumn
hpFddiDriverStatsErrRxCRC = _HpFddiDriverStatsErrRxCRC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 6),
    _HpFddiDriverStatsErrRxCRC_Type()
)
hpFddiDriverStatsErrRxCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrRxCRC.setStatus("mandatory")
_HpFddiDriverStatsErrRxOverrun_Type = Integer32
_HpFddiDriverStatsErrRxOverrun_Object = MibTableColumn
hpFddiDriverStatsErrRxOverrun = _HpFddiDriverStatsErrRxOverrun_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 7),
    _HpFddiDriverStatsErrRxOverrun_Type()
)
hpFddiDriverStatsErrRxOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrRxOverrun.setStatus("mandatory")
_HpFddiDriverStatsErrRxParity_Type = Integer32
_HpFddiDriverStatsErrRxParity_Object = MibTableColumn
hpFddiDriverStatsErrRxParity = _HpFddiDriverStatsErrRxParity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 8),
    _HpFddiDriverStatsErrRxParity_Type()
)
hpFddiDriverStatsErrRxParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrRxParity.setStatus("mandatory")
_HpFddiDriverStatsErrRxMACStatus_Type = Integer32
_HpFddiDriverStatsErrRxMACStatus_Object = MibTableColumn
hpFddiDriverStatsErrRxMACStatus = _HpFddiDriverStatsErrRxMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 9),
    _HpFddiDriverStatsErrRxMACStatus_Type()
)
hpFddiDriverStatsErrRxMACStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrRxMACStatus.setStatus("mandatory")
_HpFddiDriverStatsErrTxAbort_Type = Integer32
_HpFddiDriverStatsErrTxAbort_Object = MibTableColumn
hpFddiDriverStatsErrTxAbort = _HpFddiDriverStatsErrTxAbort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 10),
    _HpFddiDriverStatsErrTxAbort_Type()
)
hpFddiDriverStatsErrTxAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrTxAbort.setStatus("mandatory")
_HpFddiDriverStatsErrTxUnderrun_Type = Integer32
_HpFddiDriverStatsErrTxUnderrun_Object = MibTableColumn
hpFddiDriverStatsErrTxUnderrun = _HpFddiDriverStatsErrTxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 11),
    _HpFddiDriverStatsErrTxUnderrun_Type()
)
hpFddiDriverStatsErrTxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrTxUnderrun.setStatus("mandatory")
_HpFddiDriverStatsErrTxParity_Type = Integer32
_HpFddiDriverStatsErrTxParity_Object = MibTableColumn
hpFddiDriverStatsErrTxParity = _HpFddiDriverStatsErrTxParity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 12),
    _HpFddiDriverStatsErrTxParity_Type()
)
hpFddiDriverStatsErrTxParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrTxParity.setStatus("mandatory")
_HpFddiDriverStatsErrGsrLlcTxRer_Type = Integer32
_HpFddiDriverStatsErrGsrLlcTxRer_Object = MibTableColumn
hpFddiDriverStatsErrGsrLlcTxRer = _HpFddiDriverStatsErrGsrLlcTxRer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 13),
    _HpFddiDriverStatsErrGsrLlcTxRer_Type()
)
hpFddiDriverStatsErrGsrLlcTxRer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrGsrLlcTxRer.setStatus("mandatory")
_HpFddiDriverStatsErrGsrLlcRxRer_Type = Integer32
_HpFddiDriverStatsErrGsrLlcRxRer_Object = MibTableColumn
hpFddiDriverStatsErrGsrLlcRxRer = _HpFddiDriverStatsErrGsrLlcRxRer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 14),
    _HpFddiDriverStatsErrGsrLlcRxRer_Type()
)
hpFddiDriverStatsErrGsrLlcRxRer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrGsrLlcRxRer.setStatus("mandatory")
_HpFddiDriverStatsErrGsrSMTTxRer_Type = Integer32
_HpFddiDriverStatsErrGsrSMTTxRer_Object = MibTableColumn
hpFddiDriverStatsErrGsrSMTTxRer = _HpFddiDriverStatsErrGsrSMTTxRer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 15),
    _HpFddiDriverStatsErrGsrSMTTxRer_Type()
)
hpFddiDriverStatsErrGsrSMTTxRer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrGsrSMTTxRer.setStatus("mandatory")
_HpFddiDriverStatsErrGsrSMTRxRer_Type = Integer32
_HpFddiDriverStatsErrGsrSMTRxRer_Object = MibTableColumn
hpFddiDriverStatsErrGsrSMTRxRer = _HpFddiDriverStatsErrGsrSMTRxRer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 16),
    _HpFddiDriverStatsErrGsrSMTRxRer_Type()
)
hpFddiDriverStatsErrGsrSMTRxRer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrGsrSMTRxRer.setStatus("mandatory")
_HpFddiDriverStatsErrGsrPortOp_Type = Integer32
_HpFddiDriverStatsErrGsrPortOp_Object = MibTableColumn
hpFddiDriverStatsErrGsrPortOp = _HpFddiDriverStatsErrGsrPortOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 17),
    _HpFddiDriverStatsErrGsrPortOp_Type()
)
hpFddiDriverStatsErrGsrPortOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrGsrPortOp.setStatus("mandatory")
_HpFddiDriverStatsErrGsrLlcRxRov_Type = Integer32
_HpFddiDriverStatsErrGsrLlcRxRov_Object = MibTableColumn
hpFddiDriverStatsErrGsrLlcRxRov = _HpFddiDriverStatsErrGsrLlcRxRov_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 18),
    _HpFddiDriverStatsErrGsrLlcRxRov_Type()
)
hpFddiDriverStatsErrGsrLlcRxRov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrGsrLlcRxRov.setStatus("mandatory")
_HpFddiDriverStatsErrGsrSMTRxRov_Type = Integer32
_HpFddiDriverStatsErrGsrSMTRxRov_Object = MibTableColumn
hpFddiDriverStatsErrGsrSMTRxRov = _HpFddiDriverStatsErrGsrSMTRxRov_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 19),
    _HpFddiDriverStatsErrGsrSMTRxRov_Type()
)
hpFddiDriverStatsErrGsrSMTRxRov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrGsrSMTRxRov.setStatus("mandatory")
_HpFddiDriverStatsErrGsrInternalOp_Type = Integer32
_HpFddiDriverStatsErrGsrInternalOp_Object = MibTableColumn
hpFddiDriverStatsErrGsrInternalOp = _HpFddiDriverStatsErrGsrInternalOp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 20),
    _HpFddiDriverStatsErrGsrInternalOp_Type()
)
hpFddiDriverStatsErrGsrInternalOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrGsrInternalOp.setStatus("mandatory")
_HpFddiDriverStatsIoeMov_Type = Integer32
_HpFddiDriverStatsIoeMov_Object = MibTableColumn
hpFddiDriverStatsIoeMov = _HpFddiDriverStatsIoeMov_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 21),
    _HpFddiDriverStatsIoeMov_Type()
)
hpFddiDriverStatsIoeMov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsIoeMov.setStatus("mandatory")
_HpFddiDriverStatsErrGsrHost_Type = Integer32
_HpFddiDriverStatsErrGsrHost_Object = MibTableColumn
hpFddiDriverStatsErrGsrHost = _HpFddiDriverStatsErrGsrHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 22),
    _HpFddiDriverStatsErrGsrHost_Type()
)
hpFddiDriverStatsErrGsrHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsErrGsrHost.setStatus("mandatory")
_HpFddiDriverStatsTxCongestion_Type = Integer32
_HpFddiDriverStatsTxCongestion_Object = MibTableColumn
hpFddiDriverStatsTxCongestion = _HpFddiDriverStatsTxCongestion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 23),
    _HpFddiDriverStatsTxCongestion_Type()
)
hpFddiDriverStatsTxCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsTxCongestion.setStatus("mandatory")
_HpFddiDriverStatsMissedCmd_Type = Integer32
_HpFddiDriverStatsMissedCmd_Object = MibTableColumn
hpFddiDriverStatsMissedCmd = _HpFddiDriverStatsMissedCmd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 24),
    _HpFddiDriverStatsMissedCmd_Type()
)
hpFddiDriverStatsMissedCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsMissedCmd.setStatus("mandatory")
_HpFddiDriverStatsMissedCRF_Type = Integer32
_HpFddiDriverStatsMissedCRF_Object = MibTableColumn
hpFddiDriverStatsMissedCRF = _HpFddiDriverStatsMissedCRF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 3, 2, 1, 25),
    _HpFddiDriverStatsMissedCRF_Type()
)
hpFddiDriverStatsMissedCRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFddiDriverStatsMissedCRF.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSWITCH-DRIVERS-MIB",
    **{"hp": hp,
       "nm": nm,
       "icf": icf,
       "hpicfObjects": hpicfObjects,
       "hpicfSwitch": hpicfSwitch,
       "hpSwitch": hpSwitch,
       "hpOpSystem": hpOpSystem,
       "hpHwSystem": hpHwSystem,
       "hpDriverStats": hpDriverStats,
       "hpDriverStatsTable": hpDriverStatsTable,
       "hpDriverStatsEntry": hpDriverStatsEntry,
       "hpDriverStatsIndex": hpDriverStatsIndex,
       "hpDriverStatsType": hpDriverStatsType,
       "hpDriverStatsOctetsRxOk": hpDriverStatsOctetsRxOk,
       "hpDriverStatsFrameRxOk": hpDriverStatsFrameRxOk,
       "hpDriverStatsTotalRxError": hpDriverStatsTotalRxError,
       "hpDriverStatsOctetTxOk": hpDriverStatsOctetTxOk,
       "hpDriverStatsFrameTxOk": hpDriverStatsFrameTxOk,
       "hpDriverStatsTotalTxError": hpDriverStatsTotalTxError,
       "hpDriverStatsOctetsRxPerSec": hpDriverStatsOctetsRxPerSec,
       "hpDriverStatsPeakOctetsRx": hpDriverStatsPeakOctetsRx,
       "hpDriverStatsFramesRxPerSec": hpDriverStatsFramesRxPerSec,
       "hpDriverStatsPeakFramesRx": hpDriverStatsPeakFramesRx,
       "hpDriverStatsOctetsTxPerSec": hpDriverStatsOctetsTxPerSec,
       "hpDriverStatsPeakOctetsTx": hpDriverStatsPeakOctetsTx,
       "hpDriverStatsFramesTxPerSec": hpDriverStatsFramesTxPerSec,
       "hpDriverStatsPeakFramesTx": hpDriverStatsPeakFramesTx,
       "hpFddiDriverStatsTable": hpFddiDriverStatsTable,
       "hpFddiDriverStatsEntry": hpFddiDriverStatsEntry,
       "hpFddiDriverStatsIndex": hpFddiDriverStatsIndex,
       "hpFddiDriverStatsSMTOctetsRxOk": hpFddiDriverStatsSMTOctetsRxOk,
       "hpFddiDriverStatsSMTFrameRxOk": hpFddiDriverStatsSMTFrameRxOk,
       "hpFddiDriverStatsSMTOctetsTxOk": hpFddiDriverStatsSMTOctetsTxOk,
       "hpFddiDriverStatsSMTFrameTxOk": hpFddiDriverStatsSMTFrameTxOk,
       "hpFddiDriverStatsErrRxCRC": hpFddiDriverStatsErrRxCRC,
       "hpFddiDriverStatsErrRxOverrun": hpFddiDriverStatsErrRxOverrun,
       "hpFddiDriverStatsErrRxParity": hpFddiDriverStatsErrRxParity,
       "hpFddiDriverStatsErrRxMACStatus": hpFddiDriverStatsErrRxMACStatus,
       "hpFddiDriverStatsErrTxAbort": hpFddiDriverStatsErrTxAbort,
       "hpFddiDriverStatsErrTxUnderrun": hpFddiDriverStatsErrTxUnderrun,
       "hpFddiDriverStatsErrTxParity": hpFddiDriverStatsErrTxParity,
       "hpFddiDriverStatsErrGsrLlcTxRer": hpFddiDriverStatsErrGsrLlcTxRer,
       "hpFddiDriverStatsErrGsrLlcRxRer": hpFddiDriverStatsErrGsrLlcRxRer,
       "hpFddiDriverStatsErrGsrSMTTxRer": hpFddiDriverStatsErrGsrSMTTxRer,
       "hpFddiDriverStatsErrGsrSMTRxRer": hpFddiDriverStatsErrGsrSMTRxRer,
       "hpFddiDriverStatsErrGsrPortOp": hpFddiDriverStatsErrGsrPortOp,
       "hpFddiDriverStatsErrGsrLlcRxRov": hpFddiDriverStatsErrGsrLlcRxRov,
       "hpFddiDriverStatsErrGsrSMTRxRov": hpFddiDriverStatsErrGsrSMTRxRov,
       "hpFddiDriverStatsErrGsrInternalOp": hpFddiDriverStatsErrGsrInternalOp,
       "hpFddiDriverStatsIoeMov": hpFddiDriverStatsIoeMov,
       "hpFddiDriverStatsErrGsrHost": hpFddiDriverStatsErrGsrHost,
       "hpFddiDriverStatsTxCongestion": hpFddiDriverStatsTxCongestion,
       "hpFddiDriverStatsMissedCmd": hpFddiDriverStatsMissedCmd,
       "hpFddiDriverStatsMissedCRF": hpFddiDriverStatsMissedCRF}
)
