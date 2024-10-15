# SNMP MIB module (OLD-CISCO-INTERFACES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-INTERFACES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:26 2024
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_Linterfaces_ObjectIdentity = ObjectIdentity
linterfaces = _Linterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 2)
)
_LifTable_Object = MibTable
lifTable = _LifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lifTable.setStatus("mandatory")
_LifEntry_Object = MibTableRow
lifEntry = _LifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1)
)
lifEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lifEntry.setStatus("mandatory")
_LocIfHardType_Type = DisplayString
_LocIfHardType_Object = MibTableColumn
locIfHardType = _LocIfHardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 1),
    _LocIfHardType_Type()
)
locIfHardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfHardType.setStatus("mandatory")
_LocIfLineProt_Type = Integer32
_LocIfLineProt_Object = MibTableColumn
locIfLineProt = _LocIfLineProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 2),
    _LocIfLineProt_Type()
)
locIfLineProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfLineProt.setStatus("mandatory")
_LocIfLastIn_Type = Integer32
_LocIfLastIn_Object = MibTableColumn
locIfLastIn = _LocIfLastIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 3),
    _LocIfLastIn_Type()
)
locIfLastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfLastIn.setStatus("mandatory")
_LocIfLastOut_Type = Integer32
_LocIfLastOut_Object = MibTableColumn
locIfLastOut = _LocIfLastOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 4),
    _LocIfLastOut_Type()
)
locIfLastOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfLastOut.setStatus("mandatory")
_LocIfLastOutHang_Type = Integer32
_LocIfLastOutHang_Object = MibTableColumn
locIfLastOutHang = _LocIfLastOutHang_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 5),
    _LocIfLastOutHang_Type()
)
locIfLastOutHang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfLastOutHang.setStatus("mandatory")
_LocIfInBitsSec_Type = Integer32
_LocIfInBitsSec_Object = MibTableColumn
locIfInBitsSec = _LocIfInBitsSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 6),
    _LocIfInBitsSec_Type()
)
locIfInBitsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInBitsSec.setStatus("mandatory")
_LocIfInPktsSec_Type = Integer32
_LocIfInPktsSec_Object = MibTableColumn
locIfInPktsSec = _LocIfInPktsSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 7),
    _LocIfInPktsSec_Type()
)
locIfInPktsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInPktsSec.setStatus("mandatory")
_LocIfOutBitsSec_Type = Integer32
_LocIfOutBitsSec_Object = MibTableColumn
locIfOutBitsSec = _LocIfOutBitsSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 8),
    _LocIfOutBitsSec_Type()
)
locIfOutBitsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfOutBitsSec.setStatus("mandatory")
_LocIfOutPktsSec_Type = Integer32
_LocIfOutPktsSec_Object = MibTableColumn
locIfOutPktsSec = _LocIfOutPktsSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 9),
    _LocIfOutPktsSec_Type()
)
locIfOutPktsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfOutPktsSec.setStatus("mandatory")
_LocIfInRunts_Type = Integer32
_LocIfInRunts_Object = MibTableColumn
locIfInRunts = _LocIfInRunts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 10),
    _LocIfInRunts_Type()
)
locIfInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInRunts.setStatus("mandatory")
_LocIfInGiants_Type = Integer32
_LocIfInGiants_Object = MibTableColumn
locIfInGiants = _LocIfInGiants_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 11),
    _LocIfInGiants_Type()
)
locIfInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInGiants.setStatus("mandatory")
_LocIfInCRC_Type = Integer32
_LocIfInCRC_Object = MibTableColumn
locIfInCRC = _LocIfInCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 12),
    _LocIfInCRC_Type()
)
locIfInCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInCRC.setStatus("mandatory")
_LocIfInFrame_Type = Integer32
_LocIfInFrame_Object = MibTableColumn
locIfInFrame = _LocIfInFrame_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 13),
    _LocIfInFrame_Type()
)
locIfInFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInFrame.setStatus("mandatory")
_LocIfInOverrun_Type = Integer32
_LocIfInOverrun_Object = MibTableColumn
locIfInOverrun = _LocIfInOverrun_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 14),
    _LocIfInOverrun_Type()
)
locIfInOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInOverrun.setStatus("mandatory")
_LocIfInIgnored_Type = Integer32
_LocIfInIgnored_Object = MibTableColumn
locIfInIgnored = _LocIfInIgnored_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 15),
    _LocIfInIgnored_Type()
)
locIfInIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInIgnored.setStatus("mandatory")
_LocIfInAbort_Type = Integer32
_LocIfInAbort_Object = MibTableColumn
locIfInAbort = _LocIfInAbort_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 16),
    _LocIfInAbort_Type()
)
locIfInAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInAbort.setStatus("mandatory")
_LocIfResets_Type = Integer32
_LocIfResets_Object = MibTableColumn
locIfResets = _LocIfResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 17),
    _LocIfResets_Type()
)
locIfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfResets.setStatus("mandatory")
_LocIfRestarts_Type = Integer32
_LocIfRestarts_Object = MibTableColumn
locIfRestarts = _LocIfRestarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 18),
    _LocIfRestarts_Type()
)
locIfRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfRestarts.setStatus("mandatory")
_LocIfKeep_Type = Integer32
_LocIfKeep_Object = MibTableColumn
locIfKeep = _LocIfKeep_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 19),
    _LocIfKeep_Type()
)
locIfKeep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfKeep.setStatus("mandatory")
_LocIfReason_Type = DisplayString
_LocIfReason_Object = MibTableColumn
locIfReason = _LocIfReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 20),
    _LocIfReason_Type()
)
locIfReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfReason.setStatus("mandatory")
_LocIfCarTrans_Type = Integer32
_LocIfCarTrans_Object = MibTableColumn
locIfCarTrans = _LocIfCarTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 21),
    _LocIfCarTrans_Type()
)
locIfCarTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfCarTrans.setStatus("mandatory")
_LocIfReliab_Type = Integer32
_LocIfReliab_Object = MibTableColumn
locIfReliab = _LocIfReliab_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 22),
    _LocIfReliab_Type()
)
locIfReliab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfReliab.setStatus("mandatory")
_LocIfDelay_Type = Integer32
_LocIfDelay_Object = MibTableColumn
locIfDelay = _LocIfDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 23),
    _LocIfDelay_Type()
)
locIfDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfDelay.setStatus("mandatory")
_LocIfLoad_Type = Integer32
_LocIfLoad_Object = MibTableColumn
locIfLoad = _LocIfLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 24),
    _LocIfLoad_Type()
)
locIfLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfLoad.setStatus("mandatory")
_LocIfCollisions_Type = Integer32
_LocIfCollisions_Object = MibTableColumn
locIfCollisions = _LocIfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 25),
    _LocIfCollisions_Type()
)
locIfCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfCollisions.setStatus("mandatory")
_LocIfInputQueueDrops_Type = Integer32
_LocIfInputQueueDrops_Object = MibTableColumn
locIfInputQueueDrops = _LocIfInputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 26),
    _LocIfInputQueueDrops_Type()
)
locIfInputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInputQueueDrops.setStatus("mandatory")
_LocIfOutputQueueDrops_Type = Integer32
_LocIfOutputQueueDrops_Object = MibTableColumn
locIfOutputQueueDrops = _LocIfOutputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 27),
    _LocIfOutputQueueDrops_Type()
)
locIfOutputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfOutputQueueDrops.setStatus("mandatory")
_LocIfDescr_Type = DisplayString
_LocIfDescr_Object = MibTableColumn
locIfDescr = _LocIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 28),
    _LocIfDescr_Type()
)
locIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locIfDescr.setStatus("mandatory")
_LocIfSlowInPkts_Type = Counter32
_LocIfSlowInPkts_Object = MibTableColumn
locIfSlowInPkts = _LocIfSlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 30),
    _LocIfSlowInPkts_Type()
)
locIfSlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfSlowInPkts.setStatus("mandatory")
_LocIfSlowOutPkts_Type = Counter32
_LocIfSlowOutPkts_Object = MibTableColumn
locIfSlowOutPkts = _LocIfSlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 31),
    _LocIfSlowOutPkts_Type()
)
locIfSlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfSlowOutPkts.setStatus("mandatory")
_LocIfSlowInOctets_Type = Counter32
_LocIfSlowInOctets_Object = MibTableColumn
locIfSlowInOctets = _LocIfSlowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 32),
    _LocIfSlowInOctets_Type()
)
locIfSlowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfSlowInOctets.setStatus("mandatory")
_LocIfSlowOutOctets_Type = Counter32
_LocIfSlowOutOctets_Object = MibTableColumn
locIfSlowOutOctets = _LocIfSlowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 33),
    _LocIfSlowOutOctets_Type()
)
locIfSlowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfSlowOutOctets.setStatus("mandatory")
_LocIfFastInPkts_Type = Counter32
_LocIfFastInPkts_Object = MibTableColumn
locIfFastInPkts = _LocIfFastInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 34),
    _LocIfFastInPkts_Type()
)
locIfFastInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFastInPkts.setStatus("mandatory")
_LocIfFastOutPkts_Type = Counter32
_LocIfFastOutPkts_Object = MibTableColumn
locIfFastOutPkts = _LocIfFastOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 35),
    _LocIfFastOutPkts_Type()
)
locIfFastOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFastOutPkts.setStatus("mandatory")
_LocIfFastInOctets_Type = Counter32
_LocIfFastInOctets_Object = MibTableColumn
locIfFastInOctets = _LocIfFastInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 36),
    _LocIfFastInOctets_Type()
)
locIfFastInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFastInOctets.setStatus("mandatory")
_LocIfFastOutOctets_Type = Counter32
_LocIfFastOutOctets_Object = MibTableColumn
locIfFastOutOctets = _LocIfFastOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 37),
    _LocIfFastOutOctets_Type()
)
locIfFastOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFastOutOctets.setStatus("mandatory")
_LocIfotherInPkts_Type = Counter32
_LocIfotherInPkts_Object = MibTableColumn
locIfotherInPkts = _LocIfotherInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 38),
    _LocIfotherInPkts_Type()
)
locIfotherInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfotherInPkts.setStatus("mandatory")
_LocIfotherOutPkts_Type = Counter32
_LocIfotherOutPkts_Object = MibTableColumn
locIfotherOutPkts = _LocIfotherOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 39),
    _LocIfotherOutPkts_Type()
)
locIfotherOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfotherOutPkts.setStatus("mandatory")
_LocIfotherInOctets_Type = Counter32
_LocIfotherInOctets_Object = MibTableColumn
locIfotherInOctets = _LocIfotherInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 40),
    _LocIfotherInOctets_Type()
)
locIfotherInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfotherInOctets.setStatus("mandatory")
_LocIfotherOutOctets_Type = Counter32
_LocIfotherOutOctets_Object = MibTableColumn
locIfotherOutOctets = _LocIfotherOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 41),
    _LocIfotherOutOctets_Type()
)
locIfotherOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfotherOutOctets.setStatus("mandatory")
_LocIfipInPkts_Type = Counter32
_LocIfipInPkts_Object = MibTableColumn
locIfipInPkts = _LocIfipInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 42),
    _LocIfipInPkts_Type()
)
locIfipInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfipInPkts.setStatus("mandatory")
_LocIfipOutPkts_Type = Counter32
_LocIfipOutPkts_Object = MibTableColumn
locIfipOutPkts = _LocIfipOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 43),
    _LocIfipOutPkts_Type()
)
locIfipOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfipOutPkts.setStatus("mandatory")
_LocIfipInOctets_Type = Counter32
_LocIfipInOctets_Object = MibTableColumn
locIfipInOctets = _LocIfipInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 44),
    _LocIfipInOctets_Type()
)
locIfipInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfipInOctets.setStatus("mandatory")
_LocIfipOutOctets_Type = Counter32
_LocIfipOutOctets_Object = MibTableColumn
locIfipOutOctets = _LocIfipOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 45),
    _LocIfipOutOctets_Type()
)
locIfipOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfipOutOctets.setStatus("mandatory")
_LocIfdecnetInPkts_Type = Counter32
_LocIfdecnetInPkts_Object = MibTableColumn
locIfdecnetInPkts = _LocIfdecnetInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 46),
    _LocIfdecnetInPkts_Type()
)
locIfdecnetInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfdecnetInPkts.setStatus("mandatory")
_LocIfdecnetOutPkts_Type = Counter32
_LocIfdecnetOutPkts_Object = MibTableColumn
locIfdecnetOutPkts = _LocIfdecnetOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 47),
    _LocIfdecnetOutPkts_Type()
)
locIfdecnetOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfdecnetOutPkts.setStatus("mandatory")
_LocIfdecnetInOctets_Type = Counter32
_LocIfdecnetInOctets_Object = MibTableColumn
locIfdecnetInOctets = _LocIfdecnetInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 48),
    _LocIfdecnetInOctets_Type()
)
locIfdecnetInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfdecnetInOctets.setStatus("mandatory")
_LocIfdecnetOutOctets_Type = Counter32
_LocIfdecnetOutOctets_Object = MibTableColumn
locIfdecnetOutOctets = _LocIfdecnetOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 49),
    _LocIfdecnetOutOctets_Type()
)
locIfdecnetOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfdecnetOutOctets.setStatus("mandatory")
_LocIfxnsInPkts_Type = Counter32
_LocIfxnsInPkts_Object = MibTableColumn
locIfxnsInPkts = _LocIfxnsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 50),
    _LocIfxnsInPkts_Type()
)
locIfxnsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfxnsInPkts.setStatus("mandatory")
_LocIfxnsOutPkts_Type = Counter32
_LocIfxnsOutPkts_Object = MibTableColumn
locIfxnsOutPkts = _LocIfxnsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 51),
    _LocIfxnsOutPkts_Type()
)
locIfxnsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfxnsOutPkts.setStatus("mandatory")
_LocIfxnsInOctets_Type = Counter32
_LocIfxnsInOctets_Object = MibTableColumn
locIfxnsInOctets = _LocIfxnsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 52),
    _LocIfxnsInOctets_Type()
)
locIfxnsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfxnsInOctets.setStatus("mandatory")
_LocIfxnsOutOctets_Type = Counter32
_LocIfxnsOutOctets_Object = MibTableColumn
locIfxnsOutOctets = _LocIfxnsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 53),
    _LocIfxnsOutOctets_Type()
)
locIfxnsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfxnsOutOctets.setStatus("mandatory")
_LocIfclnsInPkts_Type = Counter32
_LocIfclnsInPkts_Object = MibTableColumn
locIfclnsInPkts = _LocIfclnsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 54),
    _LocIfclnsInPkts_Type()
)
locIfclnsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfclnsInPkts.setStatus("mandatory")
_LocIfclnsOutPkts_Type = Counter32
_LocIfclnsOutPkts_Object = MibTableColumn
locIfclnsOutPkts = _LocIfclnsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 55),
    _LocIfclnsOutPkts_Type()
)
locIfclnsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfclnsOutPkts.setStatus("mandatory")
_LocIfclnsInOctets_Type = Counter32
_LocIfclnsInOctets_Object = MibTableColumn
locIfclnsInOctets = _LocIfclnsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 56),
    _LocIfclnsInOctets_Type()
)
locIfclnsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfclnsInOctets.setStatus("mandatory")
_LocIfclnsOutOctets_Type = Counter32
_LocIfclnsOutOctets_Object = MibTableColumn
locIfclnsOutOctets = _LocIfclnsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 57),
    _LocIfclnsOutOctets_Type()
)
locIfclnsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfclnsOutOctets.setStatus("mandatory")
_LocIfappletalkInPkts_Type = Counter32
_LocIfappletalkInPkts_Object = MibTableColumn
locIfappletalkInPkts = _LocIfappletalkInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 58),
    _LocIfappletalkInPkts_Type()
)
locIfappletalkInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfappletalkInPkts.setStatus("mandatory")
_LocIfappletalkOutPkts_Type = Counter32
_LocIfappletalkOutPkts_Object = MibTableColumn
locIfappletalkOutPkts = _LocIfappletalkOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 59),
    _LocIfappletalkOutPkts_Type()
)
locIfappletalkOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfappletalkOutPkts.setStatus("mandatory")
_LocIfappletalkInOctets_Type = Counter32
_LocIfappletalkInOctets_Object = MibTableColumn
locIfappletalkInOctets = _LocIfappletalkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 60),
    _LocIfappletalkInOctets_Type()
)
locIfappletalkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfappletalkInOctets.setStatus("mandatory")
_LocIfappletalkOutOctets_Type = Counter32
_LocIfappletalkOutOctets_Object = MibTableColumn
locIfappletalkOutOctets = _LocIfappletalkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 61),
    _LocIfappletalkOutOctets_Type()
)
locIfappletalkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfappletalkOutOctets.setStatus("mandatory")
_LocIfnovellInPkts_Type = Counter32
_LocIfnovellInPkts_Object = MibTableColumn
locIfnovellInPkts = _LocIfnovellInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 62),
    _LocIfnovellInPkts_Type()
)
locIfnovellInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfnovellInPkts.setStatus("mandatory")
_LocIfnovellOutPkts_Type = Counter32
_LocIfnovellOutPkts_Object = MibTableColumn
locIfnovellOutPkts = _LocIfnovellOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 63),
    _LocIfnovellOutPkts_Type()
)
locIfnovellOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfnovellOutPkts.setStatus("mandatory")
_LocIfnovellInOctets_Type = Counter32
_LocIfnovellInOctets_Object = MibTableColumn
locIfnovellInOctets = _LocIfnovellInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 64),
    _LocIfnovellInOctets_Type()
)
locIfnovellInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfnovellInOctets.setStatus("mandatory")
_LocIfnovellOutOctets_Type = Counter32
_LocIfnovellOutOctets_Object = MibTableColumn
locIfnovellOutOctets = _LocIfnovellOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 65),
    _LocIfnovellOutOctets_Type()
)
locIfnovellOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfnovellOutOctets.setStatus("mandatory")
_LocIfapolloInPkts_Type = Counter32
_LocIfapolloInPkts_Object = MibTableColumn
locIfapolloInPkts = _LocIfapolloInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 66),
    _LocIfapolloInPkts_Type()
)
locIfapolloInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfapolloInPkts.setStatus("mandatory")
_LocIfapolloOutPkts_Type = Counter32
_LocIfapolloOutPkts_Object = MibTableColumn
locIfapolloOutPkts = _LocIfapolloOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 67),
    _LocIfapolloOutPkts_Type()
)
locIfapolloOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfapolloOutPkts.setStatus("mandatory")
_LocIfapolloInOctets_Type = Counter32
_LocIfapolloInOctets_Object = MibTableColumn
locIfapolloInOctets = _LocIfapolloInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 68),
    _LocIfapolloInOctets_Type()
)
locIfapolloInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfapolloInOctets.setStatus("mandatory")
_LocIfapolloOutOctets_Type = Counter32
_LocIfapolloOutOctets_Object = MibTableColumn
locIfapolloOutOctets = _LocIfapolloOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 69),
    _LocIfapolloOutOctets_Type()
)
locIfapolloOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfapolloOutOctets.setStatus("mandatory")
_LocIfvinesInPkts_Type = Counter32
_LocIfvinesInPkts_Object = MibTableColumn
locIfvinesInPkts = _LocIfvinesInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 70),
    _LocIfvinesInPkts_Type()
)
locIfvinesInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfvinesInPkts.setStatus("mandatory")
_LocIfvinesOutPkts_Type = Counter32
_LocIfvinesOutPkts_Object = MibTableColumn
locIfvinesOutPkts = _LocIfvinesOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 71),
    _LocIfvinesOutPkts_Type()
)
locIfvinesOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfvinesOutPkts.setStatus("mandatory")
_LocIfvinesInOctets_Type = Counter32
_LocIfvinesInOctets_Object = MibTableColumn
locIfvinesInOctets = _LocIfvinesInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 72),
    _LocIfvinesInOctets_Type()
)
locIfvinesInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfvinesInOctets.setStatus("mandatory")
_LocIfvinesOutOctets_Type = Counter32
_LocIfvinesOutOctets_Object = MibTableColumn
locIfvinesOutOctets = _LocIfvinesOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 73),
    _LocIfvinesOutOctets_Type()
)
locIfvinesOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfvinesOutOctets.setStatus("mandatory")
_LocIfbridgedInPkts_Type = Counter32
_LocIfbridgedInPkts_Object = MibTableColumn
locIfbridgedInPkts = _LocIfbridgedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 74),
    _LocIfbridgedInPkts_Type()
)
locIfbridgedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfbridgedInPkts.setStatus("mandatory")
_LocIfbridgedOutPkts_Type = Counter32
_LocIfbridgedOutPkts_Object = MibTableColumn
locIfbridgedOutPkts = _LocIfbridgedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 75),
    _LocIfbridgedOutPkts_Type()
)
locIfbridgedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfbridgedOutPkts.setStatus("mandatory")
_LocIfbridgedInOctets_Type = Counter32
_LocIfbridgedInOctets_Object = MibTableColumn
locIfbridgedInOctets = _LocIfbridgedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 76),
    _LocIfbridgedInOctets_Type()
)
locIfbridgedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfbridgedInOctets.setStatus("mandatory")
_LocIfbridgedOutOctets_Type = Counter32
_LocIfbridgedOutOctets_Object = MibTableColumn
locIfbridgedOutOctets = _LocIfbridgedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 77),
    _LocIfbridgedOutOctets_Type()
)
locIfbridgedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfbridgedOutOctets.setStatus("mandatory")
_LocIfsrbInPkts_Type = Counter32
_LocIfsrbInPkts_Object = MibTableColumn
locIfsrbInPkts = _LocIfsrbInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 78),
    _LocIfsrbInPkts_Type()
)
locIfsrbInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfsrbInPkts.setStatus("mandatory")
_LocIfsrbOutPkts_Type = Counter32
_LocIfsrbOutPkts_Object = MibTableColumn
locIfsrbOutPkts = _LocIfsrbOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 79),
    _LocIfsrbOutPkts_Type()
)
locIfsrbOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfsrbOutPkts.setStatus("mandatory")
_LocIfsrbInOctets_Type = Counter32
_LocIfsrbInOctets_Object = MibTableColumn
locIfsrbInOctets = _LocIfsrbInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 80),
    _LocIfsrbInOctets_Type()
)
locIfsrbInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfsrbInOctets.setStatus("mandatory")
_LocIfsrbOutOctets_Type = Counter32
_LocIfsrbOutOctets_Object = MibTableColumn
locIfsrbOutOctets = _LocIfsrbOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 81),
    _LocIfsrbOutOctets_Type()
)
locIfsrbOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfsrbOutOctets.setStatus("mandatory")
_LocIfchaosInPkts_Type = Counter32
_LocIfchaosInPkts_Object = MibTableColumn
locIfchaosInPkts = _LocIfchaosInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 82),
    _LocIfchaosInPkts_Type()
)
locIfchaosInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfchaosInPkts.setStatus("mandatory")
_LocIfchaosOutPkts_Type = Counter32
_LocIfchaosOutPkts_Object = MibTableColumn
locIfchaosOutPkts = _LocIfchaosOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 83),
    _LocIfchaosOutPkts_Type()
)
locIfchaosOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfchaosOutPkts.setStatus("mandatory")
_LocIfchaosInOctets_Type = Counter32
_LocIfchaosInOctets_Object = MibTableColumn
locIfchaosInOctets = _LocIfchaosInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 84),
    _LocIfchaosInOctets_Type()
)
locIfchaosInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfchaosInOctets.setStatus("mandatory")
_LocIfchaosOutOctets_Type = Counter32
_LocIfchaosOutOctets_Object = MibTableColumn
locIfchaosOutOctets = _LocIfchaosOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 85),
    _LocIfchaosOutOctets_Type()
)
locIfchaosOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfchaosOutOctets.setStatus("mandatory")
_LocIfpupInPkts_Type = Counter32
_LocIfpupInPkts_Object = MibTableColumn
locIfpupInPkts = _LocIfpupInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 86),
    _LocIfpupInPkts_Type()
)
locIfpupInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfpupInPkts.setStatus("mandatory")
_LocIfpupOutPkts_Type = Counter32
_LocIfpupOutPkts_Object = MibTableColumn
locIfpupOutPkts = _LocIfpupOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 87),
    _LocIfpupOutPkts_Type()
)
locIfpupOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfpupOutPkts.setStatus("mandatory")
_LocIfpupInOctets_Type = Counter32
_LocIfpupInOctets_Object = MibTableColumn
locIfpupInOctets = _LocIfpupInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 88),
    _LocIfpupInOctets_Type()
)
locIfpupInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfpupInOctets.setStatus("mandatory")
_LocIfpupOutOctets_Type = Counter32
_LocIfpupOutOctets_Object = MibTableColumn
locIfpupOutOctets = _LocIfpupOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 89),
    _LocIfpupOutOctets_Type()
)
locIfpupOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfpupOutOctets.setStatus("mandatory")
_LocIfmopInPkts_Type = Counter32
_LocIfmopInPkts_Object = MibTableColumn
locIfmopInPkts = _LocIfmopInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 90),
    _LocIfmopInPkts_Type()
)
locIfmopInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfmopInPkts.setStatus("mandatory")
_LocIfmopOutPkts_Type = Counter32
_LocIfmopOutPkts_Object = MibTableColumn
locIfmopOutPkts = _LocIfmopOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 91),
    _LocIfmopOutPkts_Type()
)
locIfmopOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfmopOutPkts.setStatus("mandatory")
_LocIfmopInOctets_Type = Counter32
_LocIfmopInOctets_Object = MibTableColumn
locIfmopInOctets = _LocIfmopInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 92),
    _LocIfmopInOctets_Type()
)
locIfmopInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfmopInOctets.setStatus("mandatory")
_LocIfmopOutOctets_Type = Counter32
_LocIfmopOutOctets_Object = MibTableColumn
locIfmopOutOctets = _LocIfmopOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 93),
    _LocIfmopOutOctets_Type()
)
locIfmopOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfmopOutOctets.setStatus("mandatory")
_LocIflanmanInPkts_Type = Counter32
_LocIflanmanInPkts_Object = MibTableColumn
locIflanmanInPkts = _LocIflanmanInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 94),
    _LocIflanmanInPkts_Type()
)
locIflanmanInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIflanmanInPkts.setStatus("mandatory")
_LocIflanmanOutPkts_Type = Counter32
_LocIflanmanOutPkts_Object = MibTableColumn
locIflanmanOutPkts = _LocIflanmanOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 95),
    _LocIflanmanOutPkts_Type()
)
locIflanmanOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIflanmanOutPkts.setStatus("mandatory")
_LocIflanmanInOctets_Type = Counter32
_LocIflanmanInOctets_Object = MibTableColumn
locIflanmanInOctets = _LocIflanmanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 96),
    _LocIflanmanInOctets_Type()
)
locIflanmanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIflanmanInOctets.setStatus("mandatory")
_LocIflanmanOutOctets_Type = Counter32
_LocIflanmanOutOctets_Object = MibTableColumn
locIflanmanOutOctets = _LocIflanmanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 97),
    _LocIflanmanOutOctets_Type()
)
locIflanmanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIflanmanOutOctets.setStatus("mandatory")
_LocIfstunInPkts_Type = Counter32
_LocIfstunInPkts_Object = MibTableColumn
locIfstunInPkts = _LocIfstunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 98),
    _LocIfstunInPkts_Type()
)
locIfstunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfstunInPkts.setStatus("mandatory")
_LocIfstunOutPkts_Type = Counter32
_LocIfstunOutPkts_Object = MibTableColumn
locIfstunOutPkts = _LocIfstunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 99),
    _LocIfstunOutPkts_Type()
)
locIfstunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfstunOutPkts.setStatus("mandatory")
_LocIfstunInOctets_Type = Counter32
_LocIfstunInOctets_Object = MibTableColumn
locIfstunInOctets = _LocIfstunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 100),
    _LocIfstunInOctets_Type()
)
locIfstunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfstunInOctets.setStatus("mandatory")
_LocIfstunOutOctets_Type = Counter32
_LocIfstunOutOctets_Object = MibTableColumn
locIfstunOutOctets = _LocIfstunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 101),
    _LocIfstunOutOctets_Type()
)
locIfstunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfstunOutOctets.setStatus("mandatory")
_LocIfspanInPkts_Type = Counter32
_LocIfspanInPkts_Object = MibTableColumn
locIfspanInPkts = _LocIfspanInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 102),
    _LocIfspanInPkts_Type()
)
locIfspanInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfspanInPkts.setStatus("mandatory")
_LocIfspanOutPkts_Type = Counter32
_LocIfspanOutPkts_Object = MibTableColumn
locIfspanOutPkts = _LocIfspanOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 103),
    _LocIfspanOutPkts_Type()
)
locIfspanOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfspanOutPkts.setStatus("mandatory")
_LocIfspanInOctets_Type = Counter32
_LocIfspanInOctets_Object = MibTableColumn
locIfspanInOctets = _LocIfspanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 104),
    _LocIfspanInOctets_Type()
)
locIfspanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfspanInOctets.setStatus("mandatory")
_LocIfspanOutOctets_Type = Counter32
_LocIfspanOutOctets_Object = MibTableColumn
locIfspanOutOctets = _LocIfspanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 105),
    _LocIfspanOutOctets_Type()
)
locIfspanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfspanOutOctets.setStatus("mandatory")
_LocIfarpInPkts_Type = Counter32
_LocIfarpInPkts_Object = MibTableColumn
locIfarpInPkts = _LocIfarpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 106),
    _LocIfarpInPkts_Type()
)
locIfarpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfarpInPkts.setStatus("mandatory")
_LocIfarpOutPkts_Type = Counter32
_LocIfarpOutPkts_Object = MibTableColumn
locIfarpOutPkts = _LocIfarpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 107),
    _LocIfarpOutPkts_Type()
)
locIfarpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfarpOutPkts.setStatus("mandatory")
_LocIfarpInOctets_Type = Counter32
_LocIfarpInOctets_Object = MibTableColumn
locIfarpInOctets = _LocIfarpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 108),
    _LocIfarpInOctets_Type()
)
locIfarpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfarpInOctets.setStatus("mandatory")
_LocIfarpOutOctets_Type = Counter32
_LocIfarpOutOctets_Object = MibTableColumn
locIfarpOutOctets = _LocIfarpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 109),
    _LocIfarpOutOctets_Type()
)
locIfarpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfarpOutOctets.setStatus("mandatory")
_LocIfprobeInPkts_Type = Counter32
_LocIfprobeInPkts_Object = MibTableColumn
locIfprobeInPkts = _LocIfprobeInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 110),
    _LocIfprobeInPkts_Type()
)
locIfprobeInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfprobeInPkts.setStatus("mandatory")
_LocIfprobeOutPkts_Type = Counter32
_LocIfprobeOutPkts_Object = MibTableColumn
locIfprobeOutPkts = _LocIfprobeOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 111),
    _LocIfprobeOutPkts_Type()
)
locIfprobeOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfprobeOutPkts.setStatus("mandatory")
_LocIfprobeInOctets_Type = Counter32
_LocIfprobeInOctets_Object = MibTableColumn
locIfprobeInOctets = _LocIfprobeInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 112),
    _LocIfprobeInOctets_Type()
)
locIfprobeInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfprobeInOctets.setStatus("mandatory")
_LocIfprobeOutOctets_Type = Counter32
_LocIfprobeOutOctets_Object = MibTableColumn
locIfprobeOutOctets = _LocIfprobeOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 113),
    _LocIfprobeOutOctets_Type()
)
locIfprobeOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfprobeOutOctets.setStatus("mandatory")
_LocIfDribbleInputs_Type = Counter32
_LocIfDribbleInputs_Object = MibTableColumn
locIfDribbleInputs = _LocIfDribbleInputs_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 114),
    _LocIfDribbleInputs_Type()
)
locIfDribbleInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfDribbleInputs.setStatus("mandatory")
_LFSIPTable_Object = MibTable
lFSIPTable = _LFSIPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2)
)
if mibBuilder.loadTexts:
    lFSIPTable.setStatus("mandatory")
_LFSIPEntry_Object = MibTableRow
lFSIPEntry = _LFSIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1)
)
lFSIPEntry.setIndexNames(
    (0, "OLD-CISCO-INTERFACES-MIB", "locIfFSIPIndex"),
)
if mibBuilder.loadTexts:
    lFSIPEntry.setStatus("mandatory")
_LocIfFSIPIndex_Type = Integer32
_LocIfFSIPIndex_Object = MibTableColumn
locIfFSIPIndex = _LocIfFSIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 1),
    _LocIfFSIPIndex_Type()
)
locIfFSIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPIndex.setStatus("mandatory")


class _LocIfFSIPtype_Type(Integer32):
    """Custom type locIfFSIPtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 3),
          ("dte", 2),
          ("notAvailable", 1))
    )


_LocIfFSIPtype_Type.__name__ = "Integer32"
_LocIfFSIPtype_Object = MibTableColumn
locIfFSIPtype = _LocIfFSIPtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 2),
    _LocIfFSIPtype_Type()
)
locIfFSIPtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPtype.setStatus("mandatory")


class _LocIfFSIPrts_Type(Integer32):
    """Custom type locIfFSIPrts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notAvailable", 1),
          ("up", 2))
    )


_LocIfFSIPrts_Type.__name__ = "Integer32"
_LocIfFSIPrts_Object = MibTableColumn
locIfFSIPrts = _LocIfFSIPrts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 3),
    _LocIfFSIPrts_Type()
)
locIfFSIPrts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPrts.setStatus("mandatory")


class _LocIfFSIPcts_Type(Integer32):
    """Custom type locIfFSIPcts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notAvailable", 1),
          ("up", 2))
    )


_LocIfFSIPcts_Type.__name__ = "Integer32"
_LocIfFSIPcts_Object = MibTableColumn
locIfFSIPcts = _LocIfFSIPcts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 4),
    _LocIfFSIPcts_Type()
)
locIfFSIPcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPcts.setStatus("mandatory")


class _LocIfFSIPdtr_Type(Integer32):
    """Custom type locIfFSIPdtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notAvailable", 1),
          ("up", 2))
    )


_LocIfFSIPdtr_Type.__name__ = "Integer32"
_LocIfFSIPdtr_Object = MibTableColumn
locIfFSIPdtr = _LocIfFSIPdtr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 5),
    _LocIfFSIPdtr_Type()
)
locIfFSIPdtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPdtr.setStatus("mandatory")


class _LocIfFSIPdcd_Type(Integer32):
    """Custom type locIfFSIPdcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notAvailable", 1),
          ("up", 2))
    )


_LocIfFSIPdcd_Type.__name__ = "Integer32"
_LocIfFSIPdcd_Object = MibTableColumn
locIfFSIPdcd = _LocIfFSIPdcd_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 6),
    _LocIfFSIPdcd_Type()
)
locIfFSIPdcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPdcd.setStatus("mandatory")


class _LocIfFSIPdsr_Type(Integer32):
    """Custom type locIfFSIPdsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notAvailable", 1),
          ("up", 2))
    )


_LocIfFSIPdsr_Type.__name__ = "Integer32"
_LocIfFSIPdsr_Object = MibTableColumn
locIfFSIPdsr = _LocIfFSIPdsr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 7),
    _LocIfFSIPdsr_Type()
)
locIfFSIPdsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPdsr.setStatus("mandatory")
_LocIfFSIPrxClockrate_Type = Integer32
_LocIfFSIPrxClockrate_Object = MibTableColumn
locIfFSIPrxClockrate = _LocIfFSIPrxClockrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 8),
    _LocIfFSIPrxClockrate_Type()
)
locIfFSIPrxClockrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPrxClockrate.setStatus("mandatory")
_LocIfFSIPrxClockrateHi_Type = Integer32
_LocIfFSIPrxClockrateHi_Object = MibTableColumn
locIfFSIPrxClockrateHi = _LocIfFSIPrxClockrateHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 9),
    _LocIfFSIPrxClockrateHi_Type()
)
locIfFSIPrxClockrateHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPrxClockrateHi.setStatus("mandatory")


class _LocIfFSIPportType_Type(Integer32):
    """Custom type locIfFSIPportType based on Integer32"""
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
        *(("hssi", 9),
          ("noCable", 1),
          ("rs232", 2),
          ("rs422", 3),
          ("rs423", 4),
          ("rs449", 7),
          ("rs530", 8),
          ("v35", 5),
          ("x21", 6))
    )


_LocIfFSIPportType_Type.__name__ = "Integer32"
_LocIfFSIPportType_Object = MibTableColumn
locIfFSIPportType = _LocIfFSIPportType_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 10),
    _LocIfFSIPportType_Type()
)
locIfFSIPportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPportType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-INTERFACES-MIB",
    **{"linterfaces": linterfaces,
       "lifTable": lifTable,
       "lifEntry": lifEntry,
       "locIfHardType": locIfHardType,
       "locIfLineProt": locIfLineProt,
       "locIfLastIn": locIfLastIn,
       "locIfLastOut": locIfLastOut,
       "locIfLastOutHang": locIfLastOutHang,
       "locIfInBitsSec": locIfInBitsSec,
       "locIfInPktsSec": locIfInPktsSec,
       "locIfOutBitsSec": locIfOutBitsSec,
       "locIfOutPktsSec": locIfOutPktsSec,
       "locIfInRunts": locIfInRunts,
       "locIfInGiants": locIfInGiants,
       "locIfInCRC": locIfInCRC,
       "locIfInFrame": locIfInFrame,
       "locIfInOverrun": locIfInOverrun,
       "locIfInIgnored": locIfInIgnored,
       "locIfInAbort": locIfInAbort,
       "locIfResets": locIfResets,
       "locIfRestarts": locIfRestarts,
       "locIfKeep": locIfKeep,
       "locIfReason": locIfReason,
       "locIfCarTrans": locIfCarTrans,
       "locIfReliab": locIfReliab,
       "locIfDelay": locIfDelay,
       "locIfLoad": locIfLoad,
       "locIfCollisions": locIfCollisions,
       "locIfInputQueueDrops": locIfInputQueueDrops,
       "locIfOutputQueueDrops": locIfOutputQueueDrops,
       "locIfDescr": locIfDescr,
       "locIfSlowInPkts": locIfSlowInPkts,
       "locIfSlowOutPkts": locIfSlowOutPkts,
       "locIfSlowInOctets": locIfSlowInOctets,
       "locIfSlowOutOctets": locIfSlowOutOctets,
       "locIfFastInPkts": locIfFastInPkts,
       "locIfFastOutPkts": locIfFastOutPkts,
       "locIfFastInOctets": locIfFastInOctets,
       "locIfFastOutOctets": locIfFastOutOctets,
       "locIfotherInPkts": locIfotherInPkts,
       "locIfotherOutPkts": locIfotherOutPkts,
       "locIfotherInOctets": locIfotherInOctets,
       "locIfotherOutOctets": locIfotherOutOctets,
       "locIfipInPkts": locIfipInPkts,
       "locIfipOutPkts": locIfipOutPkts,
       "locIfipInOctets": locIfipInOctets,
       "locIfipOutOctets": locIfipOutOctets,
       "locIfdecnetInPkts": locIfdecnetInPkts,
       "locIfdecnetOutPkts": locIfdecnetOutPkts,
       "locIfdecnetInOctets": locIfdecnetInOctets,
       "locIfdecnetOutOctets": locIfdecnetOutOctets,
       "locIfxnsInPkts": locIfxnsInPkts,
       "locIfxnsOutPkts": locIfxnsOutPkts,
       "locIfxnsInOctets": locIfxnsInOctets,
       "locIfxnsOutOctets": locIfxnsOutOctets,
       "locIfclnsInPkts": locIfclnsInPkts,
       "locIfclnsOutPkts": locIfclnsOutPkts,
       "locIfclnsInOctets": locIfclnsInOctets,
       "locIfclnsOutOctets": locIfclnsOutOctets,
       "locIfappletalkInPkts": locIfappletalkInPkts,
       "locIfappletalkOutPkts": locIfappletalkOutPkts,
       "locIfappletalkInOctets": locIfappletalkInOctets,
       "locIfappletalkOutOctets": locIfappletalkOutOctets,
       "locIfnovellInPkts": locIfnovellInPkts,
       "locIfnovellOutPkts": locIfnovellOutPkts,
       "locIfnovellInOctets": locIfnovellInOctets,
       "locIfnovellOutOctets": locIfnovellOutOctets,
       "locIfapolloInPkts": locIfapolloInPkts,
       "locIfapolloOutPkts": locIfapolloOutPkts,
       "locIfapolloInOctets": locIfapolloInOctets,
       "locIfapolloOutOctets": locIfapolloOutOctets,
       "locIfvinesInPkts": locIfvinesInPkts,
       "locIfvinesOutPkts": locIfvinesOutPkts,
       "locIfvinesInOctets": locIfvinesInOctets,
       "locIfvinesOutOctets": locIfvinesOutOctets,
       "locIfbridgedInPkts": locIfbridgedInPkts,
       "locIfbridgedOutPkts": locIfbridgedOutPkts,
       "locIfbridgedInOctets": locIfbridgedInOctets,
       "locIfbridgedOutOctets": locIfbridgedOutOctets,
       "locIfsrbInPkts": locIfsrbInPkts,
       "locIfsrbOutPkts": locIfsrbOutPkts,
       "locIfsrbInOctets": locIfsrbInOctets,
       "locIfsrbOutOctets": locIfsrbOutOctets,
       "locIfchaosInPkts": locIfchaosInPkts,
       "locIfchaosOutPkts": locIfchaosOutPkts,
       "locIfchaosInOctets": locIfchaosInOctets,
       "locIfchaosOutOctets": locIfchaosOutOctets,
       "locIfpupInPkts": locIfpupInPkts,
       "locIfpupOutPkts": locIfpupOutPkts,
       "locIfpupInOctets": locIfpupInOctets,
       "locIfpupOutOctets": locIfpupOutOctets,
       "locIfmopInPkts": locIfmopInPkts,
       "locIfmopOutPkts": locIfmopOutPkts,
       "locIfmopInOctets": locIfmopInOctets,
       "locIfmopOutOctets": locIfmopOutOctets,
       "locIflanmanInPkts": locIflanmanInPkts,
       "locIflanmanOutPkts": locIflanmanOutPkts,
       "locIflanmanInOctets": locIflanmanInOctets,
       "locIflanmanOutOctets": locIflanmanOutOctets,
       "locIfstunInPkts": locIfstunInPkts,
       "locIfstunOutPkts": locIfstunOutPkts,
       "locIfstunInOctets": locIfstunInOctets,
       "locIfstunOutOctets": locIfstunOutOctets,
       "locIfspanInPkts": locIfspanInPkts,
       "locIfspanOutPkts": locIfspanOutPkts,
       "locIfspanInOctets": locIfspanInOctets,
       "locIfspanOutOctets": locIfspanOutOctets,
       "locIfarpInPkts": locIfarpInPkts,
       "locIfarpOutPkts": locIfarpOutPkts,
       "locIfarpInOctets": locIfarpInOctets,
       "locIfarpOutOctets": locIfarpOutOctets,
       "locIfprobeInPkts": locIfprobeInPkts,
       "locIfprobeOutPkts": locIfprobeOutPkts,
       "locIfprobeInOctets": locIfprobeInOctets,
       "locIfprobeOutOctets": locIfprobeOutOctets,
       "locIfDribbleInputs": locIfDribbleInputs,
       "lFSIPTable": lFSIPTable,
       "lFSIPEntry": lFSIPEntry,
       "locIfFSIPIndex": locIfFSIPIndex,
       "locIfFSIPtype": locIfFSIPtype,
       "locIfFSIPrts": locIfFSIPrts,
       "locIfFSIPcts": locIfFSIPcts,
       "locIfFSIPdtr": locIfFSIPdtr,
       "locIfFSIPdcd": locIfFSIPdcd,
       "locIfFSIPdsr": locIfFSIPdsr,
       "locIfFSIPrxClockrate": locIfFSIPrxClockrate,
       "locIfFSIPrxClockrateHi": locIfFSIPrxClockrateHi,
       "locIfFSIPportType": locIfFSIPportType}
)
