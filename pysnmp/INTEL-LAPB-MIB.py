# SNMP MIB module (INTEL-LAPB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-LAPB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:53 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lapb2_ObjectIdentity = ObjectIdentity
lapb2 = _Lapb2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 31)
)
_LapbFrameType_ObjectIdentity = ObjectIdentity
lapbFrameType = _LapbFrameType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1)
)
_LapbFrameTypeTable_Object = MibTable
lapbFrameTypeTable = _LapbFrameTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1)
)
if mibBuilder.loadTexts:
    lapbFrameTypeTable.setStatus("mandatory")
_LapbFrameTypeEntry_Object = MibTableRow
lapbFrameTypeEntry = _LapbFrameTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1)
)
lapbFrameTypeEntry.setIndexNames(
    (0, "INTEL-LAPB-MIB", "lapbFrameTypeIndex"),
)
if mibBuilder.loadTexts:
    lapbFrameTypeEntry.setStatus("mandatory")
_LapbFrameTypeIndex_Type = Integer32
_LapbFrameTypeIndex_Object = MibTableColumn
lapbFrameTypeIndex = _LapbFrameTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 1),
    _LapbFrameTypeIndex_Type()
)
lapbFrameTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeIndex.setStatus("mandatory")
_LapbFrameTypeRxInfo_Type = Counter32
_LapbFrameTypeRxInfo_Object = MibTableColumn
lapbFrameTypeRxInfo = _LapbFrameTypeRxInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 2),
    _LapbFrameTypeRxInfo_Type()
)
lapbFrameTypeRxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxInfo.setStatus("mandatory")
_LapbFrameTypeTxInfo_Type = Counter32
_LapbFrameTypeTxInfo_Object = MibTableColumn
lapbFrameTypeTxInfo = _LapbFrameTypeTxInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 3),
    _LapbFrameTypeTxInfo_Type()
)
lapbFrameTypeTxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxInfo.setStatus("mandatory")
_LapbFrameTypeRxRR_Type = Counter32
_LapbFrameTypeRxRR_Object = MibTableColumn
lapbFrameTypeRxRR = _LapbFrameTypeRxRR_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 4),
    _LapbFrameTypeRxRR_Type()
)
lapbFrameTypeRxRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxRR.setStatus("mandatory")
_LapbFrameTypeTxRR_Type = Counter32
_LapbFrameTypeTxRR_Object = MibTableColumn
lapbFrameTypeTxRR = _LapbFrameTypeTxRR_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 5),
    _LapbFrameTypeTxRR_Type()
)
lapbFrameTypeTxRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxRR.setStatus("mandatory")
_LapbFrameTypeRxRNR_Type = Counter32
_LapbFrameTypeRxRNR_Object = MibTableColumn
lapbFrameTypeRxRNR = _LapbFrameTypeRxRNR_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 6),
    _LapbFrameTypeRxRNR_Type()
)
lapbFrameTypeRxRNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxRNR.setStatus("mandatory")
_LapbFrameTypeTxRNR_Type = Counter32
_LapbFrameTypeTxRNR_Object = MibTableColumn
lapbFrameTypeTxRNR = _LapbFrameTypeTxRNR_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 7),
    _LapbFrameTypeTxRNR_Type()
)
lapbFrameTypeTxRNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxRNR.setStatus("mandatory")
_LapbFrameTypeRxREJ_Type = Counter32
_LapbFrameTypeRxREJ_Object = MibTableColumn
lapbFrameTypeRxREJ = _LapbFrameTypeRxREJ_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 8),
    _LapbFrameTypeRxREJ_Type()
)
lapbFrameTypeRxREJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxREJ.setStatus("mandatory")
_LapbFrameTypeTxREJ_Type = Counter32
_LapbFrameTypeTxREJ_Object = MibTableColumn
lapbFrameTypeTxREJ = _LapbFrameTypeTxREJ_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 9),
    _LapbFrameTypeTxREJ_Type()
)
lapbFrameTypeTxREJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxREJ.setStatus("mandatory")
_LapbFrameTypeRxFRMR_Type = Counter32
_LapbFrameTypeRxFRMR_Object = MibTableColumn
lapbFrameTypeRxFRMR = _LapbFrameTypeRxFRMR_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 10),
    _LapbFrameTypeRxFRMR_Type()
)
lapbFrameTypeRxFRMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxFRMR.setStatus("mandatory")
_LapbFrameTypeTxFRMR_Type = Counter32
_LapbFrameTypeTxFRMR_Object = MibTableColumn
lapbFrameTypeTxFRMR = _LapbFrameTypeTxFRMR_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 11),
    _LapbFrameTypeTxFRMR_Type()
)
lapbFrameTypeTxFRMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxFRMR.setStatus("mandatory")
_LapbFrameTypeRxSABM_Type = Counter32
_LapbFrameTypeRxSABM_Object = MibTableColumn
lapbFrameTypeRxSABM = _LapbFrameTypeRxSABM_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 12),
    _LapbFrameTypeRxSABM_Type()
)
lapbFrameTypeRxSABM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxSABM.setStatus("mandatory")
_LapbFrameTypeTxSABM_Type = Counter32
_LapbFrameTypeTxSABM_Object = MibTableColumn
lapbFrameTypeTxSABM = _LapbFrameTypeTxSABM_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 13),
    _LapbFrameTypeTxSABM_Type()
)
lapbFrameTypeTxSABM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxSABM.setStatus("mandatory")
_LapbFrameTypeRxUA_Type = Counter32
_LapbFrameTypeRxUA_Object = MibTableColumn
lapbFrameTypeRxUA = _LapbFrameTypeRxUA_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 14),
    _LapbFrameTypeRxUA_Type()
)
lapbFrameTypeRxUA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxUA.setStatus("mandatory")
_LapbFrameTypeTxUA_Type = Counter32
_LapbFrameTypeTxUA_Object = MibTableColumn
lapbFrameTypeTxUA = _LapbFrameTypeTxUA_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 15),
    _LapbFrameTypeTxUA_Type()
)
lapbFrameTypeTxUA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxUA.setStatus("mandatory")
_LapbFrameTypeRxDISC_Type = Counter32
_LapbFrameTypeRxDISC_Object = MibTableColumn
lapbFrameTypeRxDISC = _LapbFrameTypeRxDISC_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 16),
    _LapbFrameTypeRxDISC_Type()
)
lapbFrameTypeRxDISC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxDISC.setStatus("mandatory")
_LapbFrameTypeTxDISC_Type = Counter32
_LapbFrameTypeTxDISC_Object = MibTableColumn
lapbFrameTypeTxDISC = _LapbFrameTypeTxDISC_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 17),
    _LapbFrameTypeTxDISC_Type()
)
lapbFrameTypeTxDISC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxDISC.setStatus("mandatory")
_LapbFrameTypeRxDM_Type = Counter32
_LapbFrameTypeRxDM_Object = MibTableColumn
lapbFrameTypeRxDM = _LapbFrameTypeRxDM_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 18),
    _LapbFrameTypeRxDM_Type()
)
lapbFrameTypeRxDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxDM.setStatus("mandatory")
_LapbFrameTypeTxDM_Type = Counter32
_LapbFrameTypeTxDM_Object = MibTableColumn
lapbFrameTypeTxDM = _LapbFrameTypeTxDM_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 19),
    _LapbFrameTypeTxDM_Type()
)
lapbFrameTypeTxDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxDM.setStatus("mandatory")
_LapbFrameTypeRxPOLL_Type = Counter32
_LapbFrameTypeRxPOLL_Object = MibTableColumn
lapbFrameTypeRxPOLL = _LapbFrameTypeRxPOLL_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 20),
    _LapbFrameTypeRxPOLL_Type()
)
lapbFrameTypeRxPOLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxPOLL.setStatus("mandatory")
_LapbFrameTypeTxPOLL_Type = Counter32
_LapbFrameTypeTxPOLL_Object = MibTableColumn
lapbFrameTypeTxPOLL = _LapbFrameTypeTxPOLL_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 21),
    _LapbFrameTypeTxPOLL_Type()
)
lapbFrameTypeTxPOLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxPOLL.setStatus("mandatory")
_LapbFrameTypeRxFINAL_Type = Counter32
_LapbFrameTypeRxFINAL_Object = MibTableColumn
lapbFrameTypeRxFINAL = _LapbFrameTypeRxFINAL_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 22),
    _LapbFrameTypeRxFINAL_Type()
)
lapbFrameTypeRxFINAL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxFINAL.setStatus("mandatory")
_LapbFrameTypeTxFINAL_Type = Counter32
_LapbFrameTypeTxFINAL_Object = MibTableColumn
lapbFrameTypeTxFINAL = _LapbFrameTypeTxFINAL_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 23),
    _LapbFrameTypeTxFINAL_Type()
)
lapbFrameTypeTxFINAL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxFINAL.setStatus("mandatory")
_LapbFrameTypeRxComUndef_Type = Counter32
_LapbFrameTypeRxComUndef_Object = MibTableColumn
lapbFrameTypeRxComUndef = _LapbFrameTypeRxComUndef_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 24),
    _LapbFrameTypeRxComUndef_Type()
)
lapbFrameTypeRxComUndef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxComUndef.setStatus("mandatory")
_LapbFrameTypeRxIllAddr_Type = Counter32
_LapbFrameTypeRxIllAddr_Object = MibTableColumn
lapbFrameTypeRxIllAddr = _LapbFrameTypeRxIllAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 25),
    _LapbFrameTypeRxIllAddr_Type()
)
lapbFrameTypeRxIllAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxIllAddr.setStatus("mandatory")
_LapbFrameTypeRxLong_Type = Counter32
_LapbFrameTypeRxLong_Object = MibTableColumn
lapbFrameTypeRxLong = _LapbFrameTypeRxLong_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 26),
    _LapbFrameTypeRxLong_Type()
)
lapbFrameTypeRxLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeRxLong.setStatus("mandatory")
_LapbFrameTypeTxRe_Type = Counter32
_LapbFrameTypeTxRe_Object = MibTableColumn
lapbFrameTypeTxRe = _LapbFrameTypeTxRe_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 27),
    _LapbFrameTypeTxRe_Type()
)
lapbFrameTypeTxRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeTxRe.setStatus("mandatory")
_LapbFrameTypeReset_Type = Counter32
_LapbFrameTypeReset_Object = MibTableColumn
lapbFrameTypeReset = _LapbFrameTypeReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 31, 1, 1, 1, 28),
    _LapbFrameTypeReset_Type()
)
lapbFrameTypeReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFrameTypeReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-LAPB-MIB",
    **{"lapb2": lapb2,
       "lapbFrameType": lapbFrameType,
       "lapbFrameTypeTable": lapbFrameTypeTable,
       "lapbFrameTypeEntry": lapbFrameTypeEntry,
       "lapbFrameTypeIndex": lapbFrameTypeIndex,
       "lapbFrameTypeRxInfo": lapbFrameTypeRxInfo,
       "lapbFrameTypeTxInfo": lapbFrameTypeTxInfo,
       "lapbFrameTypeRxRR": lapbFrameTypeRxRR,
       "lapbFrameTypeTxRR": lapbFrameTypeTxRR,
       "lapbFrameTypeRxRNR": lapbFrameTypeRxRNR,
       "lapbFrameTypeTxRNR": lapbFrameTypeTxRNR,
       "lapbFrameTypeRxREJ": lapbFrameTypeRxREJ,
       "lapbFrameTypeTxREJ": lapbFrameTypeTxREJ,
       "lapbFrameTypeRxFRMR": lapbFrameTypeRxFRMR,
       "lapbFrameTypeTxFRMR": lapbFrameTypeTxFRMR,
       "lapbFrameTypeRxSABM": lapbFrameTypeRxSABM,
       "lapbFrameTypeTxSABM": lapbFrameTypeTxSABM,
       "lapbFrameTypeRxUA": lapbFrameTypeRxUA,
       "lapbFrameTypeTxUA": lapbFrameTypeTxUA,
       "lapbFrameTypeRxDISC": lapbFrameTypeRxDISC,
       "lapbFrameTypeTxDISC": lapbFrameTypeTxDISC,
       "lapbFrameTypeRxDM": lapbFrameTypeRxDM,
       "lapbFrameTypeTxDM": lapbFrameTypeTxDM,
       "lapbFrameTypeRxPOLL": lapbFrameTypeRxPOLL,
       "lapbFrameTypeTxPOLL": lapbFrameTypeTxPOLL,
       "lapbFrameTypeRxFINAL": lapbFrameTypeRxFINAL,
       "lapbFrameTypeTxFINAL": lapbFrameTypeTxFINAL,
       "lapbFrameTypeRxComUndef": lapbFrameTypeRxComUndef,
       "lapbFrameTypeRxIllAddr": lapbFrameTypeRxIllAddr,
       "lapbFrameTypeRxLong": lapbFrameTypeRxLong,
       "lapbFrameTypeTxRe": lapbFrameTypeTxRe,
       "lapbFrameTypeReset": lapbFrameTypeReset}
)
