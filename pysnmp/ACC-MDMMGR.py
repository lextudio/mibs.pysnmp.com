# SNMP MIB module (ACC-MDMMGR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-MDMMGR
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:33 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccMdmMgr_ObjectIdentity = ObjectIdentity
accMdmMgr = _AccMdmMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54)
)
_AccMdmMgrParms_ObjectIdentity = ObjectIdentity
accMdmMgrParms = _AccMdmMgrParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1)
)


class _AccMdmMgrMessageLevel_Type(Integer32):
    """Custom type accMdmMgrMessageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccMdmMgrMessageLevel_Type.__name__ = "Integer32"
_AccMdmMgrMessageLevel_Object = MibScalar
accMdmMgrMessageLevel = _AccMdmMgrMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 1),
    _AccMdmMgrMessageLevel_Type()
)
accMdmMgrMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrMessageLevel.setStatus("mandatory")


class _AccMdmMgrConnFails4Bad_Type(Integer32):
    """Custom type accMdmMgrConnFails4Bad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AccMdmMgrConnFails4Bad_Type.__name__ = "Integer32"
_AccMdmMgrConnFails4Bad_Object = MibScalar
accMdmMgrConnFails4Bad = _AccMdmMgrConnFails4Bad_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 2),
    _AccMdmMgrConnFails4Bad_Type()
)
accMdmMgrConnFails4Bad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrConnFails4Bad.setStatus("mandatory")
_AccMdmMgrTotAssigns_Type = Counter32
_AccMdmMgrTotAssigns_Object = MibScalar
accMdmMgrTotAssigns = _AccMdmMgrTotAssigns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 3),
    _AccMdmMgrTotAssigns_Type()
)
accMdmMgrTotAssigns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrTotAssigns.setStatus("mandatory")
_AccMdmMgrTotConns_Type = Counter32
_AccMdmMgrTotConns_Object = MibScalar
accMdmMgrTotConns = _AccMdmMgrTotConns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 4),
    _AccMdmMgrTotConns_Type()
)
accMdmMgrTotConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrTotConns.setStatus("mandatory")
_AccMdmMgrLicInstTotal56ks_Type = Counter32
_AccMdmMgrLicInstTotal56ks_Object = MibScalar
accMdmMgrLicInstTotal56ks = _AccMdmMgrLicInstTotal56ks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 5),
    _AccMdmMgrLicInstTotal56ks_Type()
)
accMdmMgrLicInstTotal56ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrLicInstTotal56ks.setStatus("mandatory")
_AccMdmMgrLicInstCurrent56ks_Type = Counter32
_AccMdmMgrLicInstCurrent56ks_Object = MibScalar
accMdmMgrLicInstCurrent56ks = _AccMdmMgrLicInstCurrent56ks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 6),
    _AccMdmMgrLicInstCurrent56ks_Type()
)
accMdmMgrLicInstCurrent56ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrLicInstCurrent56ks.setStatus("mandatory")
_AccMdmMgrLicInstPeak56ks_Type = Counter32
_AccMdmMgrLicInstPeak56ks_Object = MibScalar
accMdmMgrLicInstPeak56ks = _AccMdmMgrLicInstPeak56ks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 7),
    _AccMdmMgrLicInstPeak56ks_Type()
)
accMdmMgrLicInstPeak56ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrLicInstPeak56ks.setStatus("mandatory")
_AccMdmMgrLicInstDenial56ks_Type = Counter32
_AccMdmMgrLicInstDenial56ks_Object = MibScalar
accMdmMgrLicInstDenial56ks = _AccMdmMgrLicInstDenial56ks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 8),
    _AccMdmMgrLicInstDenial56ks_Type()
)
accMdmMgrLicInstDenial56ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrLicInstDenial56ks.setStatus("mandatory")
_AccMdmMgrLicInstTotalVoIPs_Type = Counter32
_AccMdmMgrLicInstTotalVoIPs_Object = MibScalar
accMdmMgrLicInstTotalVoIPs = _AccMdmMgrLicInstTotalVoIPs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 9),
    _AccMdmMgrLicInstTotalVoIPs_Type()
)
accMdmMgrLicInstTotalVoIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrLicInstTotalVoIPs.setStatus("mandatory")
_AccMdmMgrLicInstCurrentVoIPs_Type = Counter32
_AccMdmMgrLicInstCurrentVoIPs_Object = MibScalar
accMdmMgrLicInstCurrentVoIPs = _AccMdmMgrLicInstCurrentVoIPs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 10),
    _AccMdmMgrLicInstCurrentVoIPs_Type()
)
accMdmMgrLicInstCurrentVoIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrLicInstCurrentVoIPs.setStatus("mandatory")
_AccMdmMgrLicInstPeakVoIPs_Type = Counter32
_AccMdmMgrLicInstPeakVoIPs_Object = MibScalar
accMdmMgrLicInstPeakVoIPs = _AccMdmMgrLicInstPeakVoIPs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 11),
    _AccMdmMgrLicInstPeakVoIPs_Type()
)
accMdmMgrLicInstPeakVoIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrLicInstPeakVoIPs.setStatus("mandatory")
_AccMdmMgrLicInstDenialVoIPs_Type = Counter32
_AccMdmMgrLicInstDenialVoIPs_Object = MibScalar
accMdmMgrLicInstDenialVoIPs = _AccMdmMgrLicInstDenialVoIPs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 1, 12),
    _AccMdmMgrLicInstDenialVoIPs_Type()
)
accMdmMgrLicInstDenialVoIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrLicInstDenialVoIPs.setStatus("mandatory")
_AccMdmMgrPoolTable_Object = MibTable
accMdmMgrPoolTable = _AccMdmMgrPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2)
)
if mibBuilder.loadTexts:
    accMdmMgrPoolTable.setStatus("mandatory")
_AccMdmMgrPoolEntry_Object = MibTableRow
accMdmMgrPoolEntry = _AccMdmMgrPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1)
)
accMdmMgrPoolEntry.setIndexNames(
    (0, "ACC-MDMMGR", "accMdmMgrPoolName"),
)
if mibBuilder.loadTexts:
    accMdmMgrPoolEntry.setStatus("mandatory")


class _AccMdmMgrPoolAction_Type(Integer32):
    """Custom type accMdmMgrPoolAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2))
    )


_AccMdmMgrPoolAction_Type.__name__ = "Integer32"
_AccMdmMgrPoolAction_Object = MibTableColumn
accMdmMgrPoolAction = _AccMdmMgrPoolAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 1),
    _AccMdmMgrPoolAction_Type()
)
accMdmMgrPoolAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolAction.setStatus("mandatory")
_AccMdmMgrPoolSize_Type = Integer32
_AccMdmMgrPoolSize_Object = MibTableColumn
accMdmMgrPoolSize = _AccMdmMgrPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 2),
    _AccMdmMgrPoolSize_Type()
)
accMdmMgrPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolSize.setStatus("mandatory")
_AccMdmMgrPoolMaxTx_Type = Integer32
_AccMdmMgrPoolMaxTx_Object = MibTableColumn
accMdmMgrPoolMaxTx = _AccMdmMgrPoolMaxTx_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 3),
    _AccMdmMgrPoolMaxTx_Type()
)
accMdmMgrPoolMaxTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolMaxTx.setStatus("mandatory")
_AccMdmMgrPoolCarrDtct_Type = Integer32
_AccMdmMgrPoolCarrDtct_Object = MibTableColumn
accMdmMgrPoolCarrDtct = _AccMdmMgrPoolCarrDtct_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 4),
    _AccMdmMgrPoolCarrDtct_Type()
)
accMdmMgrPoolCarrDtct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolCarrDtct.setStatus("mandatory")
_AccMdmMgrPoolCarrLoss_Type = Integer32
_AccMdmMgrPoolCarrLoss_Object = MibTableColumn
accMdmMgrPoolCarrLoss = _AccMdmMgrPoolCarrLoss_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 5),
    _AccMdmMgrPoolCarrLoss_Type()
)
accMdmMgrPoolCarrLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolCarrLoss.setStatus("mandatory")


class _AccMdmMgrPoolModType_Type(Integer32):
    """Custom type accMdmMgrPoolModType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              14,
              16,
              22,
              32,
              34,
              56,
              90)
        )
    )
    namedValues = NamedValues(
        *(("automode", 1),
          ("isdn", 16),
          ("k56", 56),
          ("v110", 14),
          ("v22b", 22),
          ("v32b", 32),
          ("v34", 34),
          ("v90", 90))
    )


_AccMdmMgrPoolModType_Type.__name__ = "Integer32"
_AccMdmMgrPoolModType_Object = MibTableColumn
accMdmMgrPoolModType = _AccMdmMgrPoolModType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 6),
    _AccMdmMgrPoolModType_Type()
)
accMdmMgrPoolModType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolModType.setStatus("mandatory")


class _AccMdmMgrPoolCompProt_Type(Integer32):
    """Custom type accMdmMgrPoolCompProt based on Integer32"""
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


_AccMdmMgrPoolCompProt_Type.__name__ = "Integer32"
_AccMdmMgrPoolCompProt_Object = MibTableColumn
accMdmMgrPoolCompProt = _AccMdmMgrPoolCompProt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 7),
    _AccMdmMgrPoolCompProt_Type()
)
accMdmMgrPoolCompProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolCompProt.setStatus("mandatory")


class _AccMdmMgrPoolErrProt_Type(Integer32):
    """Custom type accMdmMgrPoolErrProt based on Integer32"""
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
        *(("auto", 1),
          ("buffered", 4),
          ("direct", 5),
          ("lapm", 2),
          ("mnp", 3))
    )


_AccMdmMgrPoolErrProt_Type.__name__ = "Integer32"
_AccMdmMgrPoolErrProt_Object = MibTableColumn
accMdmMgrPoolErrProt = _AccMdmMgrPoolErrProt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 8),
    _AccMdmMgrPoolErrProt_Type()
)
accMdmMgrPoolErrProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolErrProt.setStatus("mandatory")
_AccMdmMgrPoolPrefStart_Type = Integer32
_AccMdmMgrPoolPrefStart_Object = MibTableColumn
accMdmMgrPoolPrefStart = _AccMdmMgrPoolPrefStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 9),
    _AccMdmMgrPoolPrefStart_Type()
)
accMdmMgrPoolPrefStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolPrefStart.setStatus("mandatory")
_AccMdmMgrPoolPrefEnd_Type = Integer32
_AccMdmMgrPoolPrefEnd_Object = MibTableColumn
accMdmMgrPoolPrefEnd = _AccMdmMgrPoolPrefEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 10),
    _AccMdmMgrPoolPrefEnd_Type()
)
accMdmMgrPoolPrefEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolPrefEnd.setStatus("mandatory")
_AccMdmMgrPoolOutStart_Type = Integer32
_AccMdmMgrPoolOutStart_Object = MibTableColumn
accMdmMgrPoolOutStart = _AccMdmMgrPoolOutStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 11),
    _AccMdmMgrPoolOutStart_Type()
)
accMdmMgrPoolOutStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolOutStart.setStatus("mandatory")
_AccMdmMgrPoolOutEnd_Type = Integer32
_AccMdmMgrPoolOutEnd_Object = MibTableColumn
accMdmMgrPoolOutEnd = _AccMdmMgrPoolOutEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 12),
    _AccMdmMgrPoolOutEnd_Type()
)
accMdmMgrPoolOutEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolOutEnd.setStatus("mandatory")
_AccMdmMgrPoolAuxCfg_Type = OctetString
_AccMdmMgrPoolAuxCfg_Object = MibTableColumn
accMdmMgrPoolAuxCfg = _AccMdmMgrPoolAuxCfg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 13),
    _AccMdmMgrPoolAuxCfg_Type()
)
accMdmMgrPoolAuxCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolAuxCfg.setStatus("mandatory")
_AccMdmMgrPoolCurrConns_Type = Integer32
_AccMdmMgrPoolCurrConns_Object = MibTableColumn
accMdmMgrPoolCurrConns = _AccMdmMgrPoolCurrConns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 14),
    _AccMdmMgrPoolCurrConns_Type()
)
accMdmMgrPoolCurrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolCurrConns.setStatus("mandatory")
_AccMdmMgrPoolCurrAssigns_Type = Integer32
_AccMdmMgrPoolCurrAssigns_Object = MibTableColumn
accMdmMgrPoolCurrAssigns = _AccMdmMgrPoolCurrAssigns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 15),
    _AccMdmMgrPoolCurrAssigns_Type()
)
accMdmMgrPoolCurrAssigns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolCurrAssigns.setStatus("mandatory")
_AccMdmMgrPoolTotConns_Type = Counter32
_AccMdmMgrPoolTotConns_Object = MibTableColumn
accMdmMgrPoolTotConns = _AccMdmMgrPoolTotConns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 16),
    _AccMdmMgrPoolTotConns_Type()
)
accMdmMgrPoolTotConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolTotConns.setStatus("mandatory")
_AccMdmMgrPoolTotAssigns_Type = Counter32
_AccMdmMgrPoolTotAssigns_Object = MibTableColumn
accMdmMgrPoolTotAssigns = _AccMdmMgrPoolTotAssigns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 17),
    _AccMdmMgrPoolTotAssigns_Type()
)
accMdmMgrPoolTotAssigns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolTotAssigns.setStatus("mandatory")
_AccMdmMgrPoolRsrcFails_Type = Counter32
_AccMdmMgrPoolRsrcFails_Object = MibTableColumn
accMdmMgrPoolRsrcFails = _AccMdmMgrPoolRsrcFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 18),
    _AccMdmMgrPoolRsrcFails_Type()
)
accMdmMgrPoolRsrcFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolRsrcFails.setStatus("mandatory")
_AccMdmMgrPoolConnFails_Type = Counter32
_AccMdmMgrPoolConnFails_Object = MibTableColumn
accMdmMgrPoolConnFails = _AccMdmMgrPoolConnFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 19),
    _AccMdmMgrPoolConnFails_Type()
)
accMdmMgrPoolConnFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolConnFails.setStatus("mandatory")
_AccMdmMgrPoolName_Type = OctetString
_AccMdmMgrPoolName_Object = MibTableColumn
accMdmMgrPoolName = _AccMdmMgrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 20),
    _AccMdmMgrPoolName_Type()
)
accMdmMgrPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolName.setStatus("mandatory")
_AccMdmMgrPoolErrProtMask_Type = OctetString
_AccMdmMgrPoolErrProtMask_Object = MibTableColumn
accMdmMgrPoolErrProtMask = _AccMdmMgrPoolErrProtMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 21),
    _AccMdmMgrPoolErrProtMask_Type()
)
accMdmMgrPoolErrProtMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolErrProtMask.setStatus("mandatory")
_AccMdmMgrPoolBadDiscs_Type = Counter32
_AccMdmMgrPoolBadDiscs_Object = MibTableColumn
accMdmMgrPoolBadDiscs = _AccMdmMgrPoolBadDiscs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 22),
    _AccMdmMgrPoolBadDiscs_Type()
)
accMdmMgrPoolBadDiscs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolBadDiscs.setStatus("obsolete")


class _AccMdmMgrPoolModTypeCtrl_Type(Integer32):
    """Custom type accMdmMgrPoolModTypeCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restr", 2),
          ("unrestr", 1))
    )


_AccMdmMgrPoolModTypeCtrl_Type.__name__ = "Integer32"
_AccMdmMgrPoolModTypeCtrl_Object = MibTableColumn
accMdmMgrPoolModTypeCtrl = _AccMdmMgrPoolModTypeCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 23),
    _AccMdmMgrPoolModTypeCtrl_Type()
)
accMdmMgrPoolModTypeCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolModTypeCtrl.setStatus("mandatory")
_AccMdmMgrPoolDroppedConns_Type = Counter32
_AccMdmMgrPoolDroppedConns_Object = MibTableColumn
accMdmMgrPoolDroppedConns = _AccMdmMgrPoolDroppedConns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 24),
    _AccMdmMgrPoolDroppedConns_Type()
)
accMdmMgrPoolDroppedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolDroppedConns.setStatus("mandatory")
_AccMdmMgrPoolHangUps_Type = Counter32
_AccMdmMgrPoolHangUps_Object = MibTableColumn
accMdmMgrPoolHangUps = _AccMdmMgrPoolHangUps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 25),
    _AccMdmMgrPoolHangUps_Type()
)
accMdmMgrPoolHangUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolHangUps.setStatus("mandatory")
_AccMdmMgrPoolConnTimeout_Type = Integer32
_AccMdmMgrPoolConnTimeout_Object = MibTableColumn
accMdmMgrPoolConnTimeout = _AccMdmMgrPoolConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 26),
    _AccMdmMgrPoolConnTimeout_Type()
)
accMdmMgrPoolConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolConnTimeout.setStatus("mandatory")
_AccMdmMgrPoolDiscReasonCount_Type = Integer32
_AccMdmMgrPoolDiscReasonCount_Object = MibTableColumn
accMdmMgrPoolDiscReasonCount = _AccMdmMgrPoolDiscReasonCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 27),
    _AccMdmMgrPoolDiscReasonCount_Type()
)
accMdmMgrPoolDiscReasonCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolDiscReasonCount.setStatus("mandatory")
_AccMdmMgrPoolStartDelay_Type = Integer32
_AccMdmMgrPoolStartDelay_Object = MibTableColumn
accMdmMgrPoolStartDelay = _AccMdmMgrPoolStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 28),
    _AccMdmMgrPoolStartDelay_Type()
)
accMdmMgrPoolStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolStartDelay.setStatus("mandatory")


class _AccMdmMgrPoolLicType_Type(Integer32):
    """Custom type accMdmMgrPoolLicType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(53,
              78,
              86)
        )
    )
    namedValues = NamedValues(
        *(("k56", 53),
          ("none", 78),
          ("voip", 86))
    )


_AccMdmMgrPoolLicType_Type.__name__ = "Integer32"
_AccMdmMgrPoolLicType_Object = MibTableColumn
accMdmMgrPoolLicType = _AccMdmMgrPoolLicType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 29),
    _AccMdmMgrPoolLicType_Type()
)
accMdmMgrPoolLicType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolLicType.setStatus("mandatory")
_AccMdmMgrPoolLicNumInst_Type = Integer32
_AccMdmMgrPoolLicNumInst_Object = MibTableColumn
accMdmMgrPoolLicNumInst = _AccMdmMgrPoolLicNumInst_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 30),
    _AccMdmMgrPoolLicNumInst_Type()
)
accMdmMgrPoolLicNumInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolLicNumInst.setStatus("mandatory")


class _AccMdmMgrPoolLicStatus_Type(Integer32):
    """Custom type accMdmMgrPoolLicStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2))
    )


_AccMdmMgrPoolLicStatus_Type.__name__ = "Integer32"
_AccMdmMgrPoolLicStatus_Object = MibTableColumn
accMdmMgrPoolLicStatus = _AccMdmMgrPoolLicStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 31),
    _AccMdmMgrPoolLicStatus_Type()
)
accMdmMgrPoolLicStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolLicStatus.setStatus("mandatory")
_AccMdmMgrPoolLicInstCurrent56ks_Type = Counter32
_AccMdmMgrPoolLicInstCurrent56ks_Object = MibTableColumn
accMdmMgrPoolLicInstCurrent56ks = _AccMdmMgrPoolLicInstCurrent56ks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 32),
    _AccMdmMgrPoolLicInstCurrent56ks_Type()
)
accMdmMgrPoolLicInstCurrent56ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolLicInstCurrent56ks.setStatus("mandatory")
_AccMdmMgrPoolLicInstPeak56ks_Type = Counter32
_AccMdmMgrPoolLicInstPeak56ks_Object = MibTableColumn
accMdmMgrPoolLicInstPeak56ks = _AccMdmMgrPoolLicInstPeak56ks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 33),
    _AccMdmMgrPoolLicInstPeak56ks_Type()
)
accMdmMgrPoolLicInstPeak56ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolLicInstPeak56ks.setStatus("mandatory")
_AccMdmMgrPoolLicInstDenial56ks_Type = Counter32
_AccMdmMgrPoolLicInstDenial56ks_Object = MibTableColumn
accMdmMgrPoolLicInstDenial56ks = _AccMdmMgrPoolLicInstDenial56ks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 34),
    _AccMdmMgrPoolLicInstDenial56ks_Type()
)
accMdmMgrPoolLicInstDenial56ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolLicInstDenial56ks.setStatus("mandatory")
_AccMdmMgrPoolLicInstCurrentVoIPs_Type = Counter32
_AccMdmMgrPoolLicInstCurrentVoIPs_Object = MibTableColumn
accMdmMgrPoolLicInstCurrentVoIPs = _AccMdmMgrPoolLicInstCurrentVoIPs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 35),
    _AccMdmMgrPoolLicInstCurrentVoIPs_Type()
)
accMdmMgrPoolLicInstCurrentVoIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolLicInstCurrentVoIPs.setStatus("mandatory")
_AccMdmMgrPoolLicInstPeakVoIPs_Type = Counter32
_AccMdmMgrPoolLicInstPeakVoIPs_Object = MibTableColumn
accMdmMgrPoolLicInstPeakVoIPs = _AccMdmMgrPoolLicInstPeakVoIPs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 36),
    _AccMdmMgrPoolLicInstPeakVoIPs_Type()
)
accMdmMgrPoolLicInstPeakVoIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolLicInstPeakVoIPs.setStatus("mandatory")
_AccMdmMgrPoolLicInstDenialVoIPs_Type = Counter32
_AccMdmMgrPoolLicInstDenialVoIPs_Object = MibTableColumn
accMdmMgrPoolLicInstDenialVoIPs = _AccMdmMgrPoolLicInstDenialVoIPs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 37),
    _AccMdmMgrPoolLicInstDenialVoIPs_Type()
)
accMdmMgrPoolLicInstDenialVoIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrPoolLicInstDenialVoIPs.setStatus("mandatory")
_AccMdmMgrPoolMaxPwrV90_Type = Integer32
_AccMdmMgrPoolMaxPwrV90_Object = MibTableColumn
accMdmMgrPoolMaxPwrV90 = _AccMdmMgrPoolMaxPwrV90_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 38),
    _AccMdmMgrPoolMaxPwrV90_Type()
)
accMdmMgrPoolMaxPwrV90.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolMaxPwrV90.setStatus("mandatory")
_AccMdmMgrPoolMaxPwrV34_Type = Integer32
_AccMdmMgrPoolMaxPwrV34_Object = MibTableColumn
accMdmMgrPoolMaxPwrV34 = _AccMdmMgrPoolMaxPwrV34_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 39),
    _AccMdmMgrPoolMaxPwrV34_Type()
)
accMdmMgrPoolMaxPwrV34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolMaxPwrV34.setStatus("mandatory")
_AccMdmMgrPoolMaxPwrV32_Type = Integer32
_AccMdmMgrPoolMaxPwrV32_Object = MibTableColumn
accMdmMgrPoolMaxPwrV32 = _AccMdmMgrPoolMaxPwrV32_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 2, 1, 40),
    _AccMdmMgrPoolMaxPwrV32_Type()
)
accMdmMgrPoolMaxPwrV32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrPoolMaxPwrV32.setStatus("mandatory")
_AccMdmMgrModemTable_Object = MibTable
accMdmMgrModemTable = _AccMdmMgrModemTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3)
)
if mibBuilder.loadTexts:
    accMdmMgrModemTable.setStatus("mandatory")
_AccMdmMgrModemEntry_Object = MibTableRow
accMdmMgrModemEntry = _AccMdmMgrModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1)
)
accMdmMgrModemEntry.setIndexNames(
    (0, "ACC-MDMMGR", "accMdmMgrModemName"),
)
if mibBuilder.loadTexts:
    accMdmMgrModemEntry.setStatus("mandatory")


class _AccMdmMgrModemState_Type(Integer32):
    """Custom type accMdmMgrModemState based on Integer32"""
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
        *(("connected", 1),
          ("disconnected", 2),
          ("eightFailures", 10),
          ("fiveFailures", 7),
          ("fourFailures", 6),
          ("nineFailures", 11),
          ("oneFailure", 3),
          ("sevenFailures", 9),
          ("sixFailures", 8),
          ("tenFailures", 12),
          ("threeFailures", 5),
          ("twoFailures", 4))
    )


_AccMdmMgrModemState_Type.__name__ = "Integer32"
_AccMdmMgrModemState_Object = MibTableColumn
accMdmMgrModemState = _AccMdmMgrModemState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 1),
    _AccMdmMgrModemState_Type()
)
accMdmMgrModemState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrModemState.setStatus("mandatory")
_AccMdmMgrModemConns_Type = Counter32
_AccMdmMgrModemConns_Object = MibTableColumn
accMdmMgrModemConns = _AccMdmMgrModemConns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 2),
    _AccMdmMgrModemConns_Type()
)
accMdmMgrModemConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemConns.setStatus("mandatory")
_AccMdmMgrModemFails_Type = Counter32
_AccMdmMgrModemFails_Object = MibTableColumn
accMdmMgrModemFails = _AccMdmMgrModemFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 3),
    _AccMdmMgrModemFails_Type()
)
accMdmMgrModemFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemFails.setStatus("mandatory")
_AccMdmMgrModemRetrains_Type = Counter32
_AccMdmMgrModemRetrains_Object = MibTableColumn
accMdmMgrModemRetrains = _AccMdmMgrModemRetrains_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 4),
    _AccMdmMgrModemRetrains_Type()
)
accMdmMgrModemRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemRetrains.setStatus("mandatory")
_AccMdmMgrModemRxErrs_Type = Counter32
_AccMdmMgrModemRxErrs_Object = MibTableColumn
accMdmMgrModemRxErrs = _AccMdmMgrModemRxErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 5),
    _AccMdmMgrModemRxErrs_Type()
)
accMdmMgrModemRxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemRxErrs.setStatus("mandatory")
_AccMdmMgrModemRetransmits_Type = Counter32
_AccMdmMgrModemRetransmits_Object = MibTableColumn
accMdmMgrModemRetransmits = _AccMdmMgrModemRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 6),
    _AccMdmMgrModemRetransmits_Type()
)
accMdmMgrModemRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemRetransmits.setStatus("mandatory")


class _AccMdmMgrModemDiscReason_Type(Integer32):
    """Custom type accMdmMgrModemDiscReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("badRespToFeatNeg", 11),
          ("farEnd", 13),
          ("farEndNoErrorCorrect", 6),
          ("farEndSync", 8),
          ("lossOfCarrier", 5),
          ("nearEnd", 1),
          ("noCommonFraming", 9),
          ("noCommonProtocol", 10),
          ("noRespToFeatNeg", 7),
          ("noResponse", 14),
          ("noSyncInfo", 12),
          ("protocolViolation", 15))
    )


_AccMdmMgrModemDiscReason_Type.__name__ = "Integer32"
_AccMdmMgrModemDiscReason_Object = MibTableColumn
accMdmMgrModemDiscReason = _AccMdmMgrModemDiscReason_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 7),
    _AccMdmMgrModemDiscReason_Type()
)
accMdmMgrModemDiscReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemDiscReason.setStatus("mandatory")
_AccMdmMgrModemTxRate_Type = Integer32
_AccMdmMgrModemTxRate_Object = MibTableColumn
accMdmMgrModemTxRate = _AccMdmMgrModemTxRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 8),
    _AccMdmMgrModemTxRate_Type()
)
accMdmMgrModemTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemTxRate.setStatus("mandatory")
_AccMdmMgrModemRxRate_Type = Integer32
_AccMdmMgrModemRxRate_Object = MibTableColumn
accMdmMgrModemRxRate = _AccMdmMgrModemRxRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 9),
    _AccMdmMgrModemRxRate_Type()
)
accMdmMgrModemRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemRxRate.setStatus("mandatory")


class _AccMdmMgrModemCompProt_Type(Integer32):
    """Custom type accMdmMgrModemCompProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              42,
              255)
        )
    )
    namedValues = NamedValues(
        *(("mnp5", 5),
          ("none", 255),
          ("v42bis", 42))
    )


_AccMdmMgrModemCompProt_Type.__name__ = "Integer32"
_AccMdmMgrModemCompProt_Object = MibTableColumn
accMdmMgrModemCompProt = _AccMdmMgrModemCompProt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 10),
    _AccMdmMgrModemCompProt_Type()
)
accMdmMgrModemCompProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemCompProt.setStatus("mandatory")
_AccMdmMgrModemCompPerc_Type = Integer32
_AccMdmMgrModemCompPerc_Object = MibTableColumn
accMdmMgrModemCompPerc = _AccMdmMgrModemCompPerc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 11),
    _AccMdmMgrModemCompPerc_Type()
)
accMdmMgrModemCompPerc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemCompPerc.setStatus("mandatory")


class _AccMdmMgrModemModType_Type(Integer32):
    """Custom type accMdmMgrModemModType based on Integer32"""
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
        *(("bell", 13),
          ("isdn", 16),
          ("k56", 6),
          ("v110", 14),
          ("v17", 1),
          ("v21", 2),
          ("v22", 3),
          ("v22b", 4),
          ("v23", 5),
          ("v26t", 7),
          ("v27t", 8),
          ("v29", 9),
          ("v32", 10),
          ("v32b", 11),
          ("v34", 12),
          ("v90", 15))
    )


_AccMdmMgrModemModType_Type.__name__ = "Integer32"
_AccMdmMgrModemModType_Object = MibTableColumn
accMdmMgrModemModType = _AccMdmMgrModemModType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 12),
    _AccMdmMgrModemModType_Type()
)
accMdmMgrModemModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemModType.setStatus("mandatory")


class _AccMdmMgrModemErrProt_Type(Integer32):
    """Custom type accMdmMgrModemErrProt based on Integer32"""
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
        *(("alt", 3),
          ("cell", 4),
          ("direct", 5),
          ("lapm", 2),
          ("mnp", 6),
          ("none", 1))
    )


_AccMdmMgrModemErrProt_Type.__name__ = "Integer32"
_AccMdmMgrModemErrProt_Object = MibTableColumn
accMdmMgrModemErrProt = _AccMdmMgrModemErrProt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 13),
    _AccMdmMgrModemErrProt_Type()
)
accMdmMgrModemErrProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemErrProt.setStatus("mandatory")
_AccMdmMgrModemAuxCfg_Type = OctetString
_AccMdmMgrModemAuxCfg_Object = MibTableColumn
accMdmMgrModemAuxCfg = _AccMdmMgrModemAuxCfg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 14),
    _AccMdmMgrModemAuxCfg_Type()
)
accMdmMgrModemAuxCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrModemAuxCfg.setStatus("mandatory")
_AccMdmMgrModemName_Type = Integer32
_AccMdmMgrModemName_Object = MibTableColumn
accMdmMgrModemName = _AccMdmMgrModemName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 15),
    _AccMdmMgrModemName_Type()
)
accMdmMgrModemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemName.setStatus("mandatory")
_AccMdmMgrModemPool_Type = OctetString
_AccMdmMgrModemPool_Object = MibTableColumn
accMdmMgrModemPool = _AccMdmMgrModemPool_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 16),
    _AccMdmMgrModemPool_Type()
)
accMdmMgrModemPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemPool.setStatus("mandatory")
_AccMdmMgrModemConnName_Type = Integer32
_AccMdmMgrModemConnName_Object = MibTableColumn
accMdmMgrModemConnName = _AccMdmMgrModemConnName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 17),
    _AccMdmMgrModemConnName_Type()
)
accMdmMgrModemConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemConnName.setStatus("mandatory")
_AccMdmMgrModemConnTxRate_Type = Integer32
_AccMdmMgrModemConnTxRate_Object = MibTableColumn
accMdmMgrModemConnTxRate = _AccMdmMgrModemConnTxRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 18),
    _AccMdmMgrModemConnTxRate_Type()
)
accMdmMgrModemConnTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemConnTxRate.setStatus("mandatory")
_AccMdmMgrModemConnRxRate_Type = Integer32
_AccMdmMgrModemConnRxRate_Object = MibTableColumn
accMdmMgrModemConnRxRate = _AccMdmMgrModemConnRxRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 19),
    _AccMdmMgrModemConnRxRate_Type()
)
accMdmMgrModemConnRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemConnRxRate.setStatus("mandatory")


class _AccMdmMgrModemConnErrProt_Type(Integer32):
    """Custom type accMdmMgrModemConnErrProt based on Integer32"""
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
        *(("alt", 3),
          ("cell", 4),
          ("direct", 5),
          ("lapm", 2),
          ("mnp", 6),
          ("none", 1))
    )


_AccMdmMgrModemConnErrProt_Type.__name__ = "Integer32"
_AccMdmMgrModemConnErrProt_Object = MibTableColumn
accMdmMgrModemConnErrProt = _AccMdmMgrModemConnErrProt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 20),
    _AccMdmMgrModemConnErrProt_Type()
)
accMdmMgrModemConnErrProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemConnErrProt.setStatus("mandatory")


class _AccMdmMgrModemConnCompProt_Type(Integer32):
    """Custom type accMdmMgrModemConnCompProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              42,
              255)
        )
    )
    namedValues = NamedValues(
        *(("mnp5", 5),
          ("none", 255),
          ("v42bis", 42))
    )


_AccMdmMgrModemConnCompProt_Type.__name__ = "Integer32"
_AccMdmMgrModemConnCompProt_Object = MibTableColumn
accMdmMgrModemConnCompProt = _AccMdmMgrModemConnCompProt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 21),
    _AccMdmMgrModemConnCompProt_Type()
)
accMdmMgrModemConnCompProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemConnCompProt.setStatus("mandatory")
_AccMdmMgrModemConnUser_Type = OctetString
_AccMdmMgrModemConnUser_Object = MibTableColumn
accMdmMgrModemConnUser = _AccMdmMgrModemConnUser_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 22),
    _AccMdmMgrModemConnUser_Type()
)
accMdmMgrModemConnUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemConnUser.setStatus("mandatory")
_AccMdmMgrModemConnLogPort_Type = OctetString
_AccMdmMgrModemConnLogPort_Object = MibTableColumn
accMdmMgrModemConnLogPort = _AccMdmMgrModemConnLogPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 3, 1, 23),
    _AccMdmMgrModemConnLogPort_Type()
)
accMdmMgrModemConnLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMdmMgrModemConnLogPort.setStatus("mandatory")
_AccMdmMgrDiscStatTable_Object = MibTable
accMdmMgrDiscStatTable = _AccMdmMgrDiscStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5)
)
if mibBuilder.loadTexts:
    accMdmMgrDiscStatTable.setStatus("mandatory")
_AccMdmMgrDiscStatEntry_Object = MibTableRow
accMdmMgrDiscStatEntry = _AccMdmMgrDiscStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1)
)
accMdmMgrDiscStatEntry.setIndexNames(
    (0, "ACC-MDMMGR", "accMdmMgrPoolName"),
)
if mibBuilder.loadTexts:
    accMdmMgrDiscStatEntry.setStatus("mandatory")
_AccMdmMgrDiscStatPoolName_Type = OctetString
_AccMdmMgrDiscStatPoolName_Object = MibTableColumn
accMdmMgrDiscStatPoolName = _AccMdmMgrDiscStatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 1),
    _AccMdmMgrDiscStatPoolName_Type()
)
accMdmMgrDiscStatPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatPoolName.setStatus("mandatory")
_AccMdmMgrDiscStatNormalNears_Type = Counter32
_AccMdmMgrDiscStatNormalNears_Object = MibTableColumn
accMdmMgrDiscStatNormalNears = _AccMdmMgrDiscStatNormalNears_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 2),
    _AccMdmMgrDiscStatNormalNears_Type()
)
accMdmMgrDiscStatNormalNears.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatNormalNears.setStatus("mandatory")
_AccMdmMgrDiscStatNormalFars_Type = Counter32
_AccMdmMgrDiscStatNormalFars_Object = MibTableColumn
accMdmMgrDiscStatNormalFars = _AccMdmMgrDiscStatNormalFars_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 3),
    _AccMdmMgrDiscStatNormalFars_Type()
)
accMdmMgrDiscStatNormalFars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatNormalFars.setStatus("mandatory")
_AccMdmMgrDiscStatInactivities_Type = Counter32
_AccMdmMgrDiscStatInactivities_Object = MibTableColumn
accMdmMgrDiscStatInactivities = _AccMdmMgrDiscStatInactivities_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 4),
    _AccMdmMgrDiscStatInactivities_Type()
)
accMdmMgrDiscStatInactivities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatInactivities.setStatus("mandatory")
_AccMdmMgrDiscStatCircuitLosses_Type = Counter32
_AccMdmMgrDiscStatCircuitLosses_Object = MibTableColumn
accMdmMgrDiscStatCircuitLosses = _AccMdmMgrDiscStatCircuitLosses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 5),
    _AccMdmMgrDiscStatCircuitLosses_Type()
)
accMdmMgrDiscStatCircuitLosses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatCircuitLosses.setStatus("mandatory")
_AccMdmMgrDiscStatHalteds_Type = Counter32
_AccMdmMgrDiscStatHalteds_Object = MibTableColumn
accMdmMgrDiscStatHalteds = _AccMdmMgrDiscStatHalteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 6),
    _AccMdmMgrDiscStatHalteds_Type()
)
accMdmMgrDiscStatHalteds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatHalteds.setStatus("mandatory")
_AccMdmMgrDiscStatModTimeouts_Type = Counter32
_AccMdmMgrDiscStatModTimeouts_Object = MibTableColumn
accMdmMgrDiscStatModTimeouts = _AccMdmMgrDiscStatModTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 7),
    _AccMdmMgrDiscStatModTimeouts_Type()
)
accMdmMgrDiscStatModTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatModTimeouts.setStatus("mandatory")
_AccMdmMgrDiscStatProtTimeouts_Type = Counter32
_AccMdmMgrDiscStatProtTimeouts_Object = MibTableColumn
accMdmMgrDiscStatProtTimeouts = _AccMdmMgrDiscStatProtTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 8),
    _AccMdmMgrDiscStatProtTimeouts_Type()
)
accMdmMgrDiscStatProtTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatProtTimeouts.setStatus("mandatory")
_AccMdmMgrDiscStatBadControls_Type = Counter32
_AccMdmMgrDiscStatBadControls_Object = MibTableColumn
accMdmMgrDiscStatBadControls = _AccMdmMgrDiscStatBadControls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 9),
    _AccMdmMgrDiscStatBadControls_Type()
)
accMdmMgrDiscStatBadControls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatBadControls.setStatus("mandatory")
_AccMdmMgrDiscStatFaxDetecteds_Type = Counter32
_AccMdmMgrDiscStatFaxDetecteds_Object = MibTableColumn
accMdmMgrDiscStatFaxDetecteds = _AccMdmMgrDiscStatFaxDetecteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 10),
    _AccMdmMgrDiscStatFaxDetecteds_Type()
)
accMdmMgrDiscStatFaxDetecteds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatFaxDetecteds.setStatus("mandatory")
_AccMdmMgrDiscStatCleardowns_Type = Counter32
_AccMdmMgrDiscStatCleardowns_Object = MibTableColumn
accMdmMgrDiscStatCleardowns = _AccMdmMgrDiscStatCleardowns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 11),
    _AccMdmMgrDiscStatCleardowns_Type()
)
accMdmMgrDiscStatCleardowns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatCleardowns.setStatus("mandatory")
_AccMdmMgrDiscStatFuncUnsupporteds_Type = Counter32
_AccMdmMgrDiscStatFuncUnsupporteds_Object = MibTableColumn
accMdmMgrDiscStatFuncUnsupporteds = _AccMdmMgrDiscStatFuncUnsupporteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 12),
    _AccMdmMgrDiscStatFuncUnsupporteds_Type()
)
accMdmMgrDiscStatFuncUnsupporteds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatFuncUnsupporteds.setStatus("mandatory")
_AccMdmMgrDiscStatT30Sessions_Type = Counter32
_AccMdmMgrDiscStatT30Sessions_Object = MibTableColumn
accMdmMgrDiscStatT30Sessions = _AccMdmMgrDiscStatT30Sessions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 13),
    _AccMdmMgrDiscStatT30Sessions_Type()
)
accMdmMgrDiscStatT30Sessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatT30Sessions.setStatus("mandatory")
_AccMdmMgrDiscStatFX1Sessions_Type = Counter32
_AccMdmMgrDiscStatFX1Sessions_Object = MibTableColumn
accMdmMgrDiscStatFX1Sessions = _AccMdmMgrDiscStatFX1Sessions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 14),
    _AccMdmMgrDiscStatFX1Sessions_Type()
)
accMdmMgrDiscStatFX1Sessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatFX1Sessions.setStatus("mandatory")
_AccMdmMgrDiscStatDspDisc1s_Type = Counter32
_AccMdmMgrDiscStatDspDisc1s_Object = MibTableColumn
accMdmMgrDiscStatDspDisc1s = _AccMdmMgrDiscStatDspDisc1s_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 15),
    _AccMdmMgrDiscStatDspDisc1s_Type()
)
accMdmMgrDiscStatDspDisc1s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatDspDisc1s.setStatus("mandatory")
_AccMdmMgrDiscStatDspDisc2s_Type = Counter32
_AccMdmMgrDiscStatDspDisc2s_Object = MibTableColumn
accMdmMgrDiscStatDspDisc2s = _AccMdmMgrDiscStatDspDisc2s_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 16),
    _AccMdmMgrDiscStatDspDisc2s_Type()
)
accMdmMgrDiscStatDspDisc2s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatDspDisc2s.setStatus("mandatory")
_AccMdmMgrDiscStatDspDisc3s_Type = Counter32
_AccMdmMgrDiscStatDspDisc3s_Object = MibTableColumn
accMdmMgrDiscStatDspDisc3s = _AccMdmMgrDiscStatDspDisc3s_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 17),
    _AccMdmMgrDiscStatDspDisc3s_Type()
)
accMdmMgrDiscStatDspDisc3s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatDspDisc3s.setStatus("mandatory")
_AccMdmMgrDiscStatDspDisc4s_Type = Counter32
_AccMdmMgrDiscStatDspDisc4s_Object = MibTableColumn
accMdmMgrDiscStatDspDisc4s = _AccMdmMgrDiscStatDspDisc4s_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 18),
    _AccMdmMgrDiscStatDspDisc4s_Type()
)
accMdmMgrDiscStatDspDisc4s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatDspDisc4s.setStatus("mandatory")
_AccMdmMgrDiscStatLossOfCarriers_Type = Counter32
_AccMdmMgrDiscStatLossOfCarriers_Object = MibTableColumn
accMdmMgrDiscStatLossOfCarriers = _AccMdmMgrDiscStatLossOfCarriers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 19),
    _AccMdmMgrDiscStatLossOfCarriers_Type()
)
accMdmMgrDiscStatLossOfCarriers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatLossOfCarriers.setStatus("mandatory")
_AccMdmMgrDiscStatModNegReqFails_Type = Counter32
_AccMdmMgrDiscStatModNegReqFails_Object = MibTableColumn
accMdmMgrDiscStatModNegReqFails = _AccMdmMgrDiscStatModNegReqFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 20),
    _AccMdmMgrDiscStatModNegReqFails_Type()
)
accMdmMgrDiscStatModNegReqFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatModNegReqFails.setStatus("mandatory")
_AccMdmMgrDiscStatModReqFails_Type = Counter32
_AccMdmMgrDiscStatModReqFails_Object = MibTableColumn
accMdmMgrDiscStatModReqFails = _AccMdmMgrDiscStatModReqFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 21),
    _AccMdmMgrDiscStatModReqFails_Type()
)
accMdmMgrDiscStatModReqFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatModReqFails.setStatus("mandatory")
_AccMdmMgrDiscStatModProtViolations_Type = Counter32
_AccMdmMgrDiscStatModProtViolations_Object = MibTableColumn
accMdmMgrDiscStatModProtViolations = _AccMdmMgrDiscStatModProtViolations_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 22),
    _AccMdmMgrDiscStatModProtViolations_Type()
)
accMdmMgrDiscStatModProtViolations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatModProtViolations.setStatus("mandatory")
_AccMdmMgrDiscStatModGeneralFails_Type = Counter32
_AccMdmMgrDiscStatModGeneralFails_Object = MibTableColumn
accMdmMgrDiscStatModGeneralFails = _AccMdmMgrDiscStatModGeneralFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 23),
    _AccMdmMgrDiscStatModGeneralFails_Type()
)
accMdmMgrDiscStatModGeneralFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatModGeneralFails.setStatus("mandatory")
_AccMdmMgrDiscStatProtNegReqFails_Type = Counter32
_AccMdmMgrDiscStatProtNegReqFails_Object = MibTableColumn
accMdmMgrDiscStatProtNegReqFails = _AccMdmMgrDiscStatProtNegReqFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 24),
    _AccMdmMgrDiscStatProtNegReqFails_Type()
)
accMdmMgrDiscStatProtNegReqFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatProtNegReqFails.setStatus("mandatory")
_AccMdmMgrDiscStatProtReqFails_Type = Counter32
_AccMdmMgrDiscStatProtReqFails_Object = MibTableColumn
accMdmMgrDiscStatProtReqFails = _AccMdmMgrDiscStatProtReqFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 25),
    _AccMdmMgrDiscStatProtReqFails_Type()
)
accMdmMgrDiscStatProtReqFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatProtReqFails.setStatus("mandatory")
_AccMdmMgrDiscStatProtViolations_Type = Counter32
_AccMdmMgrDiscStatProtViolations_Object = MibTableColumn
accMdmMgrDiscStatProtViolations = _AccMdmMgrDiscStatProtViolations_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 26),
    _AccMdmMgrDiscStatProtViolations_Type()
)
accMdmMgrDiscStatProtViolations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatProtViolations.setStatus("mandatory")
_AccMdmMgrDiscStatProtCompFails_Type = Counter32
_AccMdmMgrDiscStatProtCompFails_Object = MibTableColumn
accMdmMgrDiscStatProtCompFails = _AccMdmMgrDiscStatProtCompFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 27),
    _AccMdmMgrDiscStatProtCompFails_Type()
)
accMdmMgrDiscStatProtCompFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatProtCompFails.setStatus("mandatory")
_AccMdmMgrDiscStatProtGeneralFails_Type = Counter32
_AccMdmMgrDiscStatProtGeneralFails_Object = MibTableColumn
accMdmMgrDiscStatProtGeneralFails = _AccMdmMgrDiscStatProtGeneralFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 28),
    _AccMdmMgrDiscStatProtGeneralFails_Type()
)
accMdmMgrDiscStatProtGeneralFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatProtGeneralFails.setStatus("mandatory")
_AccMdmMgrDiscStatProtNoResps_Type = Counter32
_AccMdmMgrDiscStatProtNoResps_Object = MibTableColumn
accMdmMgrDiscStatProtNoResps = _AccMdmMgrDiscStatProtNoResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 29),
    _AccMdmMgrDiscStatProtNoResps_Type()
)
accMdmMgrDiscStatProtNoResps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatProtNoResps.setStatus("mandatory")
_AccMdmMgrDiscStatProtStartFails_Type = Counter32
_AccMdmMgrDiscStatProtStartFails_Object = MibTableColumn
accMdmMgrDiscStatProtStartFails = _AccMdmMgrDiscStatProtStartFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 30),
    _AccMdmMgrDiscStatProtStartFails_Type()
)
accMdmMgrDiscStatProtStartFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatProtStartFails.setStatus("mandatory")
_AccMdmMgrDiscStatProtGenTimeouts_Type = Counter32
_AccMdmMgrDiscStatProtGenTimeouts_Object = MibTableColumn
accMdmMgrDiscStatProtGenTimeouts = _AccMdmMgrDiscStatProtGenTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 5, 1, 31),
    _AccMdmMgrDiscStatProtGenTimeouts_Type()
)
accMdmMgrDiscStatProtGenTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrDiscStatProtGenTimeouts.setStatus("mandatory")
_AccMdmMgrAsyncPoolTable_Object = MibTable
accMdmMgrAsyncPoolTable = _AccMdmMgrAsyncPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 6)
)
if mibBuilder.loadTexts:
    accMdmMgrAsyncPoolTable.setStatus("mandatory")
_AccMdmMgrAsyncPoolEntry_Object = MibTableRow
accMdmMgrAsyncPoolEntry = _AccMdmMgrAsyncPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 6, 1)
)
accMdmMgrAsyncPoolEntry.setIndexNames(
    (0, "ACC-MDMMGR", "accMdmMgrAsyncName"),
)
if mibBuilder.loadTexts:
    accMdmMgrAsyncPoolEntry.setStatus("mandatory")
_AccMdmMgrAsyncName_Type = DisplayString
_AccMdmMgrAsyncName_Object = MibTableColumn
accMdmMgrAsyncName = _AccMdmMgrAsyncName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 6, 1, 1),
    _AccMdmMgrAsyncName_Type()
)
accMdmMgrAsyncName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrAsyncName.setStatus("mandatory")


class _AccMdmMgrAsyncFrmType_Type(Integer32):
    """Custom type accMdmMgrAsyncFrmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("transparent", 2))
    )


_AccMdmMgrAsyncFrmType_Type.__name__ = "Integer32"
_AccMdmMgrAsyncFrmType_Object = MibTableColumn
accMdmMgrAsyncFrmType = _AccMdmMgrAsyncFrmType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 6, 1, 2),
    _AccMdmMgrAsyncFrmType_Type()
)
accMdmMgrAsyncFrmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrAsyncFrmType.setStatus("mandatory")


class _AccMdmMgrAsyncMaxRcvFrmInt_Type(Integer32):
    """Custom type accMdmMgrAsyncMaxRcvFrmInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 512),
    )


_AccMdmMgrAsyncMaxRcvFrmInt_Type.__name__ = "Integer32"
_AccMdmMgrAsyncMaxRcvFrmInt_Object = MibTableColumn
accMdmMgrAsyncMaxRcvFrmInt = _AccMdmMgrAsyncMaxRcvFrmInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 6, 1, 3),
    _AccMdmMgrAsyncMaxRcvFrmInt_Type()
)
accMdmMgrAsyncMaxRcvFrmInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrAsyncMaxRcvFrmInt.setStatus("mandatory")


class _AccMdmMgrAsyncMaxRcvIdleInt_Type(Integer32):
    """Custom type accMdmMgrAsyncMaxRcvIdleInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_AccMdmMgrAsyncMaxRcvIdleInt_Type.__name__ = "Integer32"
_AccMdmMgrAsyncMaxRcvIdleInt_Object = MibTableColumn
accMdmMgrAsyncMaxRcvIdleInt = _AccMdmMgrAsyncMaxRcvIdleInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 6, 1, 4),
    _AccMdmMgrAsyncMaxRcvIdleInt_Type()
)
accMdmMgrAsyncMaxRcvIdleInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrAsyncMaxRcvIdleInt.setStatus("mandatory")


class _AccMdmMgrAsyncPoolEntryStatus_Type(Integer32):
    """Custom type accMdmMgrAsyncPoolEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 2),
          ("valid", 1))
    )


_AccMdmMgrAsyncPoolEntryStatus_Type.__name__ = "Integer32"
_AccMdmMgrAsyncPoolEntryStatus_Object = MibTableColumn
accMdmMgrAsyncPoolEntryStatus = _AccMdmMgrAsyncPoolEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 54, 6, 1, 5),
    _AccMdmMgrAsyncPoolEntryStatus_Type()
)
accMdmMgrAsyncPoolEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMdmMgrAsyncPoolEntryStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-MDMMGR",
    **{"accMdmMgr": accMdmMgr,
       "accMdmMgrParms": accMdmMgrParms,
       "accMdmMgrMessageLevel": accMdmMgrMessageLevel,
       "accMdmMgrConnFails4Bad": accMdmMgrConnFails4Bad,
       "accMdmMgrTotAssigns": accMdmMgrTotAssigns,
       "accMdmMgrTotConns": accMdmMgrTotConns,
       "accMdmMgrLicInstTotal56ks": accMdmMgrLicInstTotal56ks,
       "accMdmMgrLicInstCurrent56ks": accMdmMgrLicInstCurrent56ks,
       "accMdmMgrLicInstPeak56ks": accMdmMgrLicInstPeak56ks,
       "accMdmMgrLicInstDenial56ks": accMdmMgrLicInstDenial56ks,
       "accMdmMgrLicInstTotalVoIPs": accMdmMgrLicInstTotalVoIPs,
       "accMdmMgrLicInstCurrentVoIPs": accMdmMgrLicInstCurrentVoIPs,
       "accMdmMgrLicInstPeakVoIPs": accMdmMgrLicInstPeakVoIPs,
       "accMdmMgrLicInstDenialVoIPs": accMdmMgrLicInstDenialVoIPs,
       "accMdmMgrPoolTable": accMdmMgrPoolTable,
       "accMdmMgrPoolEntry": accMdmMgrPoolEntry,
       "accMdmMgrPoolAction": accMdmMgrPoolAction,
       "accMdmMgrPoolSize": accMdmMgrPoolSize,
       "accMdmMgrPoolMaxTx": accMdmMgrPoolMaxTx,
       "accMdmMgrPoolCarrDtct": accMdmMgrPoolCarrDtct,
       "accMdmMgrPoolCarrLoss": accMdmMgrPoolCarrLoss,
       "accMdmMgrPoolModType": accMdmMgrPoolModType,
       "accMdmMgrPoolCompProt": accMdmMgrPoolCompProt,
       "accMdmMgrPoolErrProt": accMdmMgrPoolErrProt,
       "accMdmMgrPoolPrefStart": accMdmMgrPoolPrefStart,
       "accMdmMgrPoolPrefEnd": accMdmMgrPoolPrefEnd,
       "accMdmMgrPoolOutStart": accMdmMgrPoolOutStart,
       "accMdmMgrPoolOutEnd": accMdmMgrPoolOutEnd,
       "accMdmMgrPoolAuxCfg": accMdmMgrPoolAuxCfg,
       "accMdmMgrPoolCurrConns": accMdmMgrPoolCurrConns,
       "accMdmMgrPoolCurrAssigns": accMdmMgrPoolCurrAssigns,
       "accMdmMgrPoolTotConns": accMdmMgrPoolTotConns,
       "accMdmMgrPoolTotAssigns": accMdmMgrPoolTotAssigns,
       "accMdmMgrPoolRsrcFails": accMdmMgrPoolRsrcFails,
       "accMdmMgrPoolConnFails": accMdmMgrPoolConnFails,
       "accMdmMgrPoolName": accMdmMgrPoolName,
       "accMdmMgrPoolErrProtMask": accMdmMgrPoolErrProtMask,
       "accMdmMgrPoolBadDiscs": accMdmMgrPoolBadDiscs,
       "accMdmMgrPoolModTypeCtrl": accMdmMgrPoolModTypeCtrl,
       "accMdmMgrPoolDroppedConns": accMdmMgrPoolDroppedConns,
       "accMdmMgrPoolHangUps": accMdmMgrPoolHangUps,
       "accMdmMgrPoolConnTimeout": accMdmMgrPoolConnTimeout,
       "accMdmMgrPoolDiscReasonCount": accMdmMgrPoolDiscReasonCount,
       "accMdmMgrPoolStartDelay": accMdmMgrPoolStartDelay,
       "accMdmMgrPoolLicType": accMdmMgrPoolLicType,
       "accMdmMgrPoolLicNumInst": accMdmMgrPoolLicNumInst,
       "accMdmMgrPoolLicStatus": accMdmMgrPoolLicStatus,
       "accMdmMgrPoolLicInstCurrent56ks": accMdmMgrPoolLicInstCurrent56ks,
       "accMdmMgrPoolLicInstPeak56ks": accMdmMgrPoolLicInstPeak56ks,
       "accMdmMgrPoolLicInstDenial56ks": accMdmMgrPoolLicInstDenial56ks,
       "accMdmMgrPoolLicInstCurrentVoIPs": accMdmMgrPoolLicInstCurrentVoIPs,
       "accMdmMgrPoolLicInstPeakVoIPs": accMdmMgrPoolLicInstPeakVoIPs,
       "accMdmMgrPoolLicInstDenialVoIPs": accMdmMgrPoolLicInstDenialVoIPs,
       "accMdmMgrPoolMaxPwrV90": accMdmMgrPoolMaxPwrV90,
       "accMdmMgrPoolMaxPwrV34": accMdmMgrPoolMaxPwrV34,
       "accMdmMgrPoolMaxPwrV32": accMdmMgrPoolMaxPwrV32,
       "accMdmMgrModemTable": accMdmMgrModemTable,
       "accMdmMgrModemEntry": accMdmMgrModemEntry,
       "accMdmMgrModemState": accMdmMgrModemState,
       "accMdmMgrModemConns": accMdmMgrModemConns,
       "accMdmMgrModemFails": accMdmMgrModemFails,
       "accMdmMgrModemRetrains": accMdmMgrModemRetrains,
       "accMdmMgrModemRxErrs": accMdmMgrModemRxErrs,
       "accMdmMgrModemRetransmits": accMdmMgrModemRetransmits,
       "accMdmMgrModemDiscReason": accMdmMgrModemDiscReason,
       "accMdmMgrModemTxRate": accMdmMgrModemTxRate,
       "accMdmMgrModemRxRate": accMdmMgrModemRxRate,
       "accMdmMgrModemCompProt": accMdmMgrModemCompProt,
       "accMdmMgrModemCompPerc": accMdmMgrModemCompPerc,
       "accMdmMgrModemModType": accMdmMgrModemModType,
       "accMdmMgrModemErrProt": accMdmMgrModemErrProt,
       "accMdmMgrModemAuxCfg": accMdmMgrModemAuxCfg,
       "accMdmMgrModemName": accMdmMgrModemName,
       "accMdmMgrModemPool": accMdmMgrModemPool,
       "accMdmMgrModemConnName": accMdmMgrModemConnName,
       "accMdmMgrModemConnTxRate": accMdmMgrModemConnTxRate,
       "accMdmMgrModemConnRxRate": accMdmMgrModemConnRxRate,
       "accMdmMgrModemConnErrProt": accMdmMgrModemConnErrProt,
       "accMdmMgrModemConnCompProt": accMdmMgrModemConnCompProt,
       "accMdmMgrModemConnUser": accMdmMgrModemConnUser,
       "accMdmMgrModemConnLogPort": accMdmMgrModemConnLogPort,
       "accMdmMgrDiscStatTable": accMdmMgrDiscStatTable,
       "accMdmMgrDiscStatEntry": accMdmMgrDiscStatEntry,
       "accMdmMgrDiscStatPoolName": accMdmMgrDiscStatPoolName,
       "accMdmMgrDiscStatNormalNears": accMdmMgrDiscStatNormalNears,
       "accMdmMgrDiscStatNormalFars": accMdmMgrDiscStatNormalFars,
       "accMdmMgrDiscStatInactivities": accMdmMgrDiscStatInactivities,
       "accMdmMgrDiscStatCircuitLosses": accMdmMgrDiscStatCircuitLosses,
       "accMdmMgrDiscStatHalteds": accMdmMgrDiscStatHalteds,
       "accMdmMgrDiscStatModTimeouts": accMdmMgrDiscStatModTimeouts,
       "accMdmMgrDiscStatProtTimeouts": accMdmMgrDiscStatProtTimeouts,
       "accMdmMgrDiscStatBadControls": accMdmMgrDiscStatBadControls,
       "accMdmMgrDiscStatFaxDetecteds": accMdmMgrDiscStatFaxDetecteds,
       "accMdmMgrDiscStatCleardowns": accMdmMgrDiscStatCleardowns,
       "accMdmMgrDiscStatFuncUnsupporteds": accMdmMgrDiscStatFuncUnsupporteds,
       "accMdmMgrDiscStatT30Sessions": accMdmMgrDiscStatT30Sessions,
       "accMdmMgrDiscStatFX1Sessions": accMdmMgrDiscStatFX1Sessions,
       "accMdmMgrDiscStatDspDisc1s": accMdmMgrDiscStatDspDisc1s,
       "accMdmMgrDiscStatDspDisc2s": accMdmMgrDiscStatDspDisc2s,
       "accMdmMgrDiscStatDspDisc3s": accMdmMgrDiscStatDspDisc3s,
       "accMdmMgrDiscStatDspDisc4s": accMdmMgrDiscStatDspDisc4s,
       "accMdmMgrDiscStatLossOfCarriers": accMdmMgrDiscStatLossOfCarriers,
       "accMdmMgrDiscStatModNegReqFails": accMdmMgrDiscStatModNegReqFails,
       "accMdmMgrDiscStatModReqFails": accMdmMgrDiscStatModReqFails,
       "accMdmMgrDiscStatModProtViolations": accMdmMgrDiscStatModProtViolations,
       "accMdmMgrDiscStatModGeneralFails": accMdmMgrDiscStatModGeneralFails,
       "accMdmMgrDiscStatProtNegReqFails": accMdmMgrDiscStatProtNegReqFails,
       "accMdmMgrDiscStatProtReqFails": accMdmMgrDiscStatProtReqFails,
       "accMdmMgrDiscStatProtViolations": accMdmMgrDiscStatProtViolations,
       "accMdmMgrDiscStatProtCompFails": accMdmMgrDiscStatProtCompFails,
       "accMdmMgrDiscStatProtGeneralFails": accMdmMgrDiscStatProtGeneralFails,
       "accMdmMgrDiscStatProtNoResps": accMdmMgrDiscStatProtNoResps,
       "accMdmMgrDiscStatProtStartFails": accMdmMgrDiscStatProtStartFails,
       "accMdmMgrDiscStatProtGenTimeouts": accMdmMgrDiscStatProtGenTimeouts,
       "accMdmMgrAsyncPoolTable": accMdmMgrAsyncPoolTable,
       "accMdmMgrAsyncPoolEntry": accMdmMgrAsyncPoolEntry,
       "accMdmMgrAsyncName": accMdmMgrAsyncName,
       "accMdmMgrAsyncFrmType": accMdmMgrAsyncFrmType,
       "accMdmMgrAsyncMaxRcvFrmInt": accMdmMgrAsyncMaxRcvFrmInt,
       "accMdmMgrAsyncMaxRcvIdleInt": accMdmMgrAsyncMaxRcvIdleInt,
       "accMdmMgrAsyncPoolEntryStatus": accMdmMgrAsyncPoolEntryStatus}
)
