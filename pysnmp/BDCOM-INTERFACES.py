# SNMP MIB module (BDCOM-INTERFACES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-INTERFACES
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:34 2024
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

(bdlocal,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdlocal")

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

_Bdlinterfaces_ObjectIdentity = ObjectIdentity
bdlinterfaces = _Bdlinterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2)
)
_BdlifTable_Object = MibTable
bdlifTable = _BdlifTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1)
)
if mibBuilder.loadTexts:
    bdlifTable.setStatus("mandatory")
_BdlifEntry_Object = MibTableRow
bdlifEntry = _BdlifEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1)
)
bdlifEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bdlifEntry.setStatus("mandatory")
_BdlocIfHardType_Type = DisplayString
_BdlocIfHardType_Object = MibTableColumn
bdlocIfHardType = _BdlocIfHardType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 1),
    _BdlocIfHardType_Type()
)
bdlocIfHardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfHardType.setStatus("mandatory")
_BdlocIfLineProt_Type = Integer32
_BdlocIfLineProt_Object = MibTableColumn
bdlocIfLineProt = _BdlocIfLineProt_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 2),
    _BdlocIfLineProt_Type()
)
bdlocIfLineProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfLineProt.setStatus("mandatory")
_BdlocIfLastIn_Type = Integer32
_BdlocIfLastIn_Object = MibTableColumn
bdlocIfLastIn = _BdlocIfLastIn_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 3),
    _BdlocIfLastIn_Type()
)
bdlocIfLastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfLastIn.setStatus("mandatory")
_BdlocIfLastOut_Type = Integer32
_BdlocIfLastOut_Object = MibTableColumn
bdlocIfLastOut = _BdlocIfLastOut_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 4),
    _BdlocIfLastOut_Type()
)
bdlocIfLastOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfLastOut.setStatus("mandatory")
_BdlocIfLastOutHang_Type = Integer32
_BdlocIfLastOutHang_Object = MibTableColumn
bdlocIfLastOutHang = _BdlocIfLastOutHang_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 5),
    _BdlocIfLastOutHang_Type()
)
bdlocIfLastOutHang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfLastOutHang.setStatus("mandatory")
_BdlocIfInBitsSec_Type = Integer32
_BdlocIfInBitsSec_Object = MibTableColumn
bdlocIfInBitsSec = _BdlocIfInBitsSec_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 6),
    _BdlocIfInBitsSec_Type()
)
bdlocIfInBitsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfInBitsSec.setStatus("mandatory")
_BdlocIfInPktsSec_Type = Integer32
_BdlocIfInPktsSec_Object = MibTableColumn
bdlocIfInPktsSec = _BdlocIfInPktsSec_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 7),
    _BdlocIfInPktsSec_Type()
)
bdlocIfInPktsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfInPktsSec.setStatus("mandatory")
_BdlocIfOutBitsSec_Type = Integer32
_BdlocIfOutBitsSec_Object = MibTableColumn
bdlocIfOutBitsSec = _BdlocIfOutBitsSec_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 8),
    _BdlocIfOutBitsSec_Type()
)
bdlocIfOutBitsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfOutBitsSec.setStatus("mandatory")
_BdlocIfOutPktsSec_Type = Integer32
_BdlocIfOutPktsSec_Object = MibTableColumn
bdlocIfOutPktsSec = _BdlocIfOutPktsSec_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 9),
    _BdlocIfOutPktsSec_Type()
)
bdlocIfOutPktsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfOutPktsSec.setStatus("mandatory")
_BdlocIfInRunts_Type = Integer32
_BdlocIfInRunts_Object = MibTableColumn
bdlocIfInRunts = _BdlocIfInRunts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 10),
    _BdlocIfInRunts_Type()
)
bdlocIfInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfInRunts.setStatus("mandatory")
_BdlocIfInGiants_Type = Integer32
_BdlocIfInGiants_Object = MibTableColumn
bdlocIfInGiants = _BdlocIfInGiants_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 11),
    _BdlocIfInGiants_Type()
)
bdlocIfInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfInGiants.setStatus("mandatory")
_BdlocIfInCRC_Type = Integer32
_BdlocIfInCRC_Object = MibTableColumn
bdlocIfInCRC = _BdlocIfInCRC_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 12),
    _BdlocIfInCRC_Type()
)
bdlocIfInCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfInCRC.setStatus("mandatory")
_BdlocIfInFrame_Type = Integer32
_BdlocIfInFrame_Object = MibTableColumn
bdlocIfInFrame = _BdlocIfInFrame_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 13),
    _BdlocIfInFrame_Type()
)
bdlocIfInFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfInFrame.setStatus("mandatory")
_BdlocIfInOverrun_Type = Integer32
_BdlocIfInOverrun_Object = MibTableColumn
bdlocIfInOverrun = _BdlocIfInOverrun_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 14),
    _BdlocIfInOverrun_Type()
)
bdlocIfInOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfInOverrun.setStatus("mandatory")
_BdlocIfInIgnored_Type = Integer32
_BdlocIfInIgnored_Object = MibTableColumn
bdlocIfInIgnored = _BdlocIfInIgnored_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 15),
    _BdlocIfInIgnored_Type()
)
bdlocIfInIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfInIgnored.setStatus("mandatory")
_BdlocIfInAbort_Type = Integer32
_BdlocIfInAbort_Object = MibTableColumn
bdlocIfInAbort = _BdlocIfInAbort_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 16),
    _BdlocIfInAbort_Type()
)
bdlocIfInAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfInAbort.setStatus("mandatory")
_BdlocIfResets_Type = Integer32
_BdlocIfResets_Object = MibTableColumn
bdlocIfResets = _BdlocIfResets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 17),
    _BdlocIfResets_Type()
)
bdlocIfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfResets.setStatus("mandatory")
_BdlocIfRestarts_Type = Integer32
_BdlocIfRestarts_Object = MibTableColumn
bdlocIfRestarts = _BdlocIfRestarts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 18),
    _BdlocIfRestarts_Type()
)
bdlocIfRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfRestarts.setStatus("mandatory")
_BdlocIfKeep_Type = Integer32
_BdlocIfKeep_Object = MibTableColumn
bdlocIfKeep = _BdlocIfKeep_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 19),
    _BdlocIfKeep_Type()
)
bdlocIfKeep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfKeep.setStatus("mandatory")
_BdlocIfReason_Type = DisplayString
_BdlocIfReason_Object = MibTableColumn
bdlocIfReason = _BdlocIfReason_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 20),
    _BdlocIfReason_Type()
)
bdlocIfReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfReason.setStatus("mandatory")
_BdlocIfCarTrans_Type = Integer32
_BdlocIfCarTrans_Object = MibTableColumn
bdlocIfCarTrans = _BdlocIfCarTrans_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 21),
    _BdlocIfCarTrans_Type()
)
bdlocIfCarTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfCarTrans.setStatus("mandatory")
_BdlocIfReliab_Type = Integer32
_BdlocIfReliab_Object = MibTableColumn
bdlocIfReliab = _BdlocIfReliab_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 22),
    _BdlocIfReliab_Type()
)
bdlocIfReliab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfReliab.setStatus("mandatory")
_BdlocIfDelay_Type = Integer32
_BdlocIfDelay_Object = MibTableColumn
bdlocIfDelay = _BdlocIfDelay_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 23),
    _BdlocIfDelay_Type()
)
bdlocIfDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfDelay.setStatus("mandatory")
_BdlocIfLoad_Type = Integer32
_BdlocIfLoad_Object = MibTableColumn
bdlocIfLoad = _BdlocIfLoad_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 24),
    _BdlocIfLoad_Type()
)
bdlocIfLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfLoad.setStatus("mandatory")
_BdlocIfCollisions_Type = Integer32
_BdlocIfCollisions_Object = MibTableColumn
bdlocIfCollisions = _BdlocIfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 25),
    _BdlocIfCollisions_Type()
)
bdlocIfCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfCollisions.setStatus("mandatory")
_BdlocIfInputQueueDrops_Type = Integer32
_BdlocIfInputQueueDrops_Object = MibTableColumn
bdlocIfInputQueueDrops = _BdlocIfInputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 26),
    _BdlocIfInputQueueDrops_Type()
)
bdlocIfInputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfInputQueueDrops.setStatus("mandatory")
_BdlocIfOutputQueueDrops_Type = Integer32
_BdlocIfOutputQueueDrops_Object = MibTableColumn
bdlocIfOutputQueueDrops = _BdlocIfOutputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 27),
    _BdlocIfOutputQueueDrops_Type()
)
bdlocIfOutputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfOutputQueueDrops.setStatus("mandatory")
_BdlocIfDescr_Type = DisplayString
_BdlocIfDescr_Object = MibTableColumn
bdlocIfDescr = _BdlocIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 28),
    _BdlocIfDescr_Type()
)
bdlocIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdlocIfDescr.setStatus("mandatory")
_BdlocIfSlowInPkts_Type = Counter32
_BdlocIfSlowInPkts_Object = MibTableColumn
bdlocIfSlowInPkts = _BdlocIfSlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 30),
    _BdlocIfSlowInPkts_Type()
)
bdlocIfSlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfSlowInPkts.setStatus("mandatory")
_BdlocIfSlowOutPkts_Type = Counter32
_BdlocIfSlowOutPkts_Object = MibTableColumn
bdlocIfSlowOutPkts = _BdlocIfSlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 31),
    _BdlocIfSlowOutPkts_Type()
)
bdlocIfSlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfSlowOutPkts.setStatus("mandatory")
_BdlocIfSlowInOctets_Type = Counter32
_BdlocIfSlowInOctets_Object = MibTableColumn
bdlocIfSlowInOctets = _BdlocIfSlowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 32),
    _BdlocIfSlowInOctets_Type()
)
bdlocIfSlowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfSlowInOctets.setStatus("mandatory")
_BdlocIfSlowOutOctets_Type = Counter32
_BdlocIfSlowOutOctets_Object = MibTableColumn
bdlocIfSlowOutOctets = _BdlocIfSlowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 33),
    _BdlocIfSlowOutOctets_Type()
)
bdlocIfSlowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfSlowOutOctets.setStatus("mandatory")
_BdlocIfFastInPkts_Type = Counter32
_BdlocIfFastInPkts_Object = MibTableColumn
bdlocIfFastInPkts = _BdlocIfFastInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 34),
    _BdlocIfFastInPkts_Type()
)
bdlocIfFastInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFastInPkts.setStatus("mandatory")
_BdlocIfFastOutPkts_Type = Counter32
_BdlocIfFastOutPkts_Object = MibTableColumn
bdlocIfFastOutPkts = _BdlocIfFastOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 35),
    _BdlocIfFastOutPkts_Type()
)
bdlocIfFastOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFastOutPkts.setStatus("mandatory")
_BdlocIfFastInOctets_Type = Counter32
_BdlocIfFastInOctets_Object = MibTableColumn
bdlocIfFastInOctets = _BdlocIfFastInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 36),
    _BdlocIfFastInOctets_Type()
)
bdlocIfFastInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFastInOctets.setStatus("mandatory")
_BdlocIfFastOutOctets_Type = Counter32
_BdlocIfFastOutOctets_Object = MibTableColumn
bdlocIfFastOutOctets = _BdlocIfFastOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 37),
    _BdlocIfFastOutOctets_Type()
)
bdlocIfFastOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFastOutOctets.setStatus("mandatory")
_BdlocIfotherInPkts_Type = Counter32
_BdlocIfotherInPkts_Object = MibTableColumn
bdlocIfotherInPkts = _BdlocIfotherInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 38),
    _BdlocIfotherInPkts_Type()
)
bdlocIfotherInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfotherInPkts.setStatus("mandatory")
_BdlocIfotherOutPkts_Type = Counter32
_BdlocIfotherOutPkts_Object = MibTableColumn
bdlocIfotherOutPkts = _BdlocIfotherOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 39),
    _BdlocIfotherOutPkts_Type()
)
bdlocIfotherOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfotherOutPkts.setStatus("mandatory")
_BdlocIfotherInOctets_Type = Counter32
_BdlocIfotherInOctets_Object = MibTableColumn
bdlocIfotherInOctets = _BdlocIfotherInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 40),
    _BdlocIfotherInOctets_Type()
)
bdlocIfotherInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfotherInOctets.setStatus("mandatory")
_BdlocIfotherOutOctets_Type = Counter32
_BdlocIfotherOutOctets_Object = MibTableColumn
bdlocIfotherOutOctets = _BdlocIfotherOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 41),
    _BdlocIfotherOutOctets_Type()
)
bdlocIfotherOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfotherOutOctets.setStatus("mandatory")
_BdlocIfipInPkts_Type = Counter32
_BdlocIfipInPkts_Object = MibTableColumn
bdlocIfipInPkts = _BdlocIfipInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 42),
    _BdlocIfipInPkts_Type()
)
bdlocIfipInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfipInPkts.setStatus("mandatory")
_BdlocIfipOutPkts_Type = Counter32
_BdlocIfipOutPkts_Object = MibTableColumn
bdlocIfipOutPkts = _BdlocIfipOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 43),
    _BdlocIfipOutPkts_Type()
)
bdlocIfipOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfipOutPkts.setStatus("mandatory")
_BdlocIfipInOctets_Type = Counter32
_BdlocIfipInOctets_Object = MibTableColumn
bdlocIfipInOctets = _BdlocIfipInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 44),
    _BdlocIfipInOctets_Type()
)
bdlocIfipInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfipInOctets.setStatus("mandatory")
_BdlocIfipOutOctets_Type = Counter32
_BdlocIfipOutOctets_Object = MibTableColumn
bdlocIfipOutOctets = _BdlocIfipOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 45),
    _BdlocIfipOutOctets_Type()
)
bdlocIfipOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfipOutOctets.setStatus("mandatory")
_BdlocIfdecnetInPkts_Type = Counter32
_BdlocIfdecnetInPkts_Object = MibTableColumn
bdlocIfdecnetInPkts = _BdlocIfdecnetInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 46),
    _BdlocIfdecnetInPkts_Type()
)
bdlocIfdecnetInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfdecnetInPkts.setStatus("mandatory")
_BdlocIfdecnetOutPkts_Type = Counter32
_BdlocIfdecnetOutPkts_Object = MibTableColumn
bdlocIfdecnetOutPkts = _BdlocIfdecnetOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 47),
    _BdlocIfdecnetOutPkts_Type()
)
bdlocIfdecnetOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfdecnetOutPkts.setStatus("mandatory")
_BdlocIfdecnetInOctets_Type = Counter32
_BdlocIfdecnetInOctets_Object = MibTableColumn
bdlocIfdecnetInOctets = _BdlocIfdecnetInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 48),
    _BdlocIfdecnetInOctets_Type()
)
bdlocIfdecnetInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfdecnetInOctets.setStatus("mandatory")
_BdlocIfdecnetOutOctets_Type = Counter32
_BdlocIfdecnetOutOctets_Object = MibTableColumn
bdlocIfdecnetOutOctets = _BdlocIfdecnetOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 49),
    _BdlocIfdecnetOutOctets_Type()
)
bdlocIfdecnetOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfdecnetOutOctets.setStatus("mandatory")
_BdlocIfxnsInPkts_Type = Counter32
_BdlocIfxnsInPkts_Object = MibTableColumn
bdlocIfxnsInPkts = _BdlocIfxnsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 50),
    _BdlocIfxnsInPkts_Type()
)
bdlocIfxnsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfxnsInPkts.setStatus("mandatory")
_BdlocIfxnsOutPkts_Type = Counter32
_BdlocIfxnsOutPkts_Object = MibTableColumn
bdlocIfxnsOutPkts = _BdlocIfxnsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 51),
    _BdlocIfxnsOutPkts_Type()
)
bdlocIfxnsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfxnsOutPkts.setStatus("mandatory")
_BdlocIfxnsInOctets_Type = Counter32
_BdlocIfxnsInOctets_Object = MibTableColumn
bdlocIfxnsInOctets = _BdlocIfxnsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 52),
    _BdlocIfxnsInOctets_Type()
)
bdlocIfxnsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfxnsInOctets.setStatus("mandatory")
_BdlocIfxnsOutOctets_Type = Counter32
_BdlocIfxnsOutOctets_Object = MibTableColumn
bdlocIfxnsOutOctets = _BdlocIfxnsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 53),
    _BdlocIfxnsOutOctets_Type()
)
bdlocIfxnsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfxnsOutOctets.setStatus("mandatory")
_BdlocIfclnsInPkts_Type = Counter32
_BdlocIfclnsInPkts_Object = MibTableColumn
bdlocIfclnsInPkts = _BdlocIfclnsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 54),
    _BdlocIfclnsInPkts_Type()
)
bdlocIfclnsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfclnsInPkts.setStatus("mandatory")
_BdlocIfclnsOutPkts_Type = Counter32
_BdlocIfclnsOutPkts_Object = MibTableColumn
bdlocIfclnsOutPkts = _BdlocIfclnsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 55),
    _BdlocIfclnsOutPkts_Type()
)
bdlocIfclnsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfclnsOutPkts.setStatus("mandatory")
_BdlocIfclnsInOctets_Type = Counter32
_BdlocIfclnsInOctets_Object = MibTableColumn
bdlocIfclnsInOctets = _BdlocIfclnsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 56),
    _BdlocIfclnsInOctets_Type()
)
bdlocIfclnsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfclnsInOctets.setStatus("mandatory")
_BdlocIfclnsOutOctets_Type = Counter32
_BdlocIfclnsOutOctets_Object = MibTableColumn
bdlocIfclnsOutOctets = _BdlocIfclnsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 57),
    _BdlocIfclnsOutOctets_Type()
)
bdlocIfclnsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfclnsOutOctets.setStatus("mandatory")
_BdlocIfappletalkInPkts_Type = Counter32
_BdlocIfappletalkInPkts_Object = MibTableColumn
bdlocIfappletalkInPkts = _BdlocIfappletalkInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 58),
    _BdlocIfappletalkInPkts_Type()
)
bdlocIfappletalkInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfappletalkInPkts.setStatus("mandatory")
_BdlocIfappletalkOutPkts_Type = Counter32
_BdlocIfappletalkOutPkts_Object = MibTableColumn
bdlocIfappletalkOutPkts = _BdlocIfappletalkOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 59),
    _BdlocIfappletalkOutPkts_Type()
)
bdlocIfappletalkOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfappletalkOutPkts.setStatus("mandatory")
_BdlocIfappletalkInOctets_Type = Counter32
_BdlocIfappletalkInOctets_Object = MibTableColumn
bdlocIfappletalkInOctets = _BdlocIfappletalkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 60),
    _BdlocIfappletalkInOctets_Type()
)
bdlocIfappletalkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfappletalkInOctets.setStatus("mandatory")
_BdlocIfappletalkOutOctets_Type = Counter32
_BdlocIfappletalkOutOctets_Object = MibTableColumn
bdlocIfappletalkOutOctets = _BdlocIfappletalkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 61),
    _BdlocIfappletalkOutOctets_Type()
)
bdlocIfappletalkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfappletalkOutOctets.setStatus("mandatory")
_BdlocIfnovellInPkts_Type = Counter32
_BdlocIfnovellInPkts_Object = MibTableColumn
bdlocIfnovellInPkts = _BdlocIfnovellInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 62),
    _BdlocIfnovellInPkts_Type()
)
bdlocIfnovellInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfnovellInPkts.setStatus("mandatory")
_BdlocIfnovellOutPkts_Type = Counter32
_BdlocIfnovellOutPkts_Object = MibTableColumn
bdlocIfnovellOutPkts = _BdlocIfnovellOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 63),
    _BdlocIfnovellOutPkts_Type()
)
bdlocIfnovellOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfnovellOutPkts.setStatus("mandatory")
_BdlocIfnovellInOctets_Type = Counter32
_BdlocIfnovellInOctets_Object = MibTableColumn
bdlocIfnovellInOctets = _BdlocIfnovellInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 64),
    _BdlocIfnovellInOctets_Type()
)
bdlocIfnovellInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfnovellInOctets.setStatus("mandatory")
_BdlocIfnovellOutOctets_Type = Counter32
_BdlocIfnovellOutOctets_Object = MibTableColumn
bdlocIfnovellOutOctets = _BdlocIfnovellOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 65),
    _BdlocIfnovellOutOctets_Type()
)
bdlocIfnovellOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfnovellOutOctets.setStatus("mandatory")
_BdlocIfapolloInPkts_Type = Counter32
_BdlocIfapolloInPkts_Object = MibTableColumn
bdlocIfapolloInPkts = _BdlocIfapolloInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 66),
    _BdlocIfapolloInPkts_Type()
)
bdlocIfapolloInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfapolloInPkts.setStatus("mandatory")
_BdlocIfapolloOutPkts_Type = Counter32
_BdlocIfapolloOutPkts_Object = MibTableColumn
bdlocIfapolloOutPkts = _BdlocIfapolloOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 67),
    _BdlocIfapolloOutPkts_Type()
)
bdlocIfapolloOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfapolloOutPkts.setStatus("mandatory")
_BdlocIfapolloInOctets_Type = Counter32
_BdlocIfapolloInOctets_Object = MibTableColumn
bdlocIfapolloInOctets = _BdlocIfapolloInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 68),
    _BdlocIfapolloInOctets_Type()
)
bdlocIfapolloInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfapolloInOctets.setStatus("mandatory")
_BdlocIfapolloOutOctets_Type = Counter32
_BdlocIfapolloOutOctets_Object = MibTableColumn
bdlocIfapolloOutOctets = _BdlocIfapolloOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 69),
    _BdlocIfapolloOutOctets_Type()
)
bdlocIfapolloOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfapolloOutOctets.setStatus("mandatory")
_BdlocIfvinesInPkts_Type = Counter32
_BdlocIfvinesInPkts_Object = MibTableColumn
bdlocIfvinesInPkts = _BdlocIfvinesInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 70),
    _BdlocIfvinesInPkts_Type()
)
bdlocIfvinesInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfvinesInPkts.setStatus("mandatory")
_BdlocIfvinesOutPkts_Type = Counter32
_BdlocIfvinesOutPkts_Object = MibTableColumn
bdlocIfvinesOutPkts = _BdlocIfvinesOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 71),
    _BdlocIfvinesOutPkts_Type()
)
bdlocIfvinesOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfvinesOutPkts.setStatus("mandatory")
_BdlocIfvinesInOctets_Type = Counter32
_BdlocIfvinesInOctets_Object = MibTableColumn
bdlocIfvinesInOctets = _BdlocIfvinesInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 72),
    _BdlocIfvinesInOctets_Type()
)
bdlocIfvinesInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfvinesInOctets.setStatus("mandatory")
_BdlocIfvinesOutOctets_Type = Counter32
_BdlocIfvinesOutOctets_Object = MibTableColumn
bdlocIfvinesOutOctets = _BdlocIfvinesOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 73),
    _BdlocIfvinesOutOctets_Type()
)
bdlocIfvinesOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfvinesOutOctets.setStatus("mandatory")
_BdlocIfbridgedInPkts_Type = Counter32
_BdlocIfbridgedInPkts_Object = MibTableColumn
bdlocIfbridgedInPkts = _BdlocIfbridgedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 74),
    _BdlocIfbridgedInPkts_Type()
)
bdlocIfbridgedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfbridgedInPkts.setStatus("mandatory")
_BdlocIfbridgedOutPkts_Type = Counter32
_BdlocIfbridgedOutPkts_Object = MibTableColumn
bdlocIfbridgedOutPkts = _BdlocIfbridgedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 75),
    _BdlocIfbridgedOutPkts_Type()
)
bdlocIfbridgedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfbridgedOutPkts.setStatus("mandatory")
_BdlocIfbridgedInOctets_Type = Counter32
_BdlocIfbridgedInOctets_Object = MibTableColumn
bdlocIfbridgedInOctets = _BdlocIfbridgedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 76),
    _BdlocIfbridgedInOctets_Type()
)
bdlocIfbridgedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfbridgedInOctets.setStatus("mandatory")
_BdlocIfbridgedOutOctets_Type = Counter32
_BdlocIfbridgedOutOctets_Object = MibTableColumn
bdlocIfbridgedOutOctets = _BdlocIfbridgedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 77),
    _BdlocIfbridgedOutOctets_Type()
)
bdlocIfbridgedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfbridgedOutOctets.setStatus("mandatory")
_BdlocIfsrbInPkts_Type = Counter32
_BdlocIfsrbInPkts_Object = MibTableColumn
bdlocIfsrbInPkts = _BdlocIfsrbInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 78),
    _BdlocIfsrbInPkts_Type()
)
bdlocIfsrbInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfsrbInPkts.setStatus("mandatory")
_BdlocIfsrbOutPkts_Type = Counter32
_BdlocIfsrbOutPkts_Object = MibTableColumn
bdlocIfsrbOutPkts = _BdlocIfsrbOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 79),
    _BdlocIfsrbOutPkts_Type()
)
bdlocIfsrbOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfsrbOutPkts.setStatus("mandatory")
_BdlocIfsrbInOctets_Type = Counter32
_BdlocIfsrbInOctets_Object = MibTableColumn
bdlocIfsrbInOctets = _BdlocIfsrbInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 80),
    _BdlocIfsrbInOctets_Type()
)
bdlocIfsrbInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfsrbInOctets.setStatus("mandatory")
_BdlocIfsrbOutOctets_Type = Counter32
_BdlocIfsrbOutOctets_Object = MibTableColumn
bdlocIfsrbOutOctets = _BdlocIfsrbOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 81),
    _BdlocIfsrbOutOctets_Type()
)
bdlocIfsrbOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfsrbOutOctets.setStatus("mandatory")
_BdlocIfchaosInPkts_Type = Counter32
_BdlocIfchaosInPkts_Object = MibTableColumn
bdlocIfchaosInPkts = _BdlocIfchaosInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 82),
    _BdlocIfchaosInPkts_Type()
)
bdlocIfchaosInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfchaosInPkts.setStatus("mandatory")
_BdlocIfchaosOutPkts_Type = Counter32
_BdlocIfchaosOutPkts_Object = MibTableColumn
bdlocIfchaosOutPkts = _BdlocIfchaosOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 83),
    _BdlocIfchaosOutPkts_Type()
)
bdlocIfchaosOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfchaosOutPkts.setStatus("mandatory")
_BdlocIfchaosInOctets_Type = Counter32
_BdlocIfchaosInOctets_Object = MibTableColumn
bdlocIfchaosInOctets = _BdlocIfchaosInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 84),
    _BdlocIfchaosInOctets_Type()
)
bdlocIfchaosInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfchaosInOctets.setStatus("mandatory")
_BdlocIfchaosOutOctets_Type = Counter32
_BdlocIfchaosOutOctets_Object = MibTableColumn
bdlocIfchaosOutOctets = _BdlocIfchaosOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 85),
    _BdlocIfchaosOutOctets_Type()
)
bdlocIfchaosOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfchaosOutOctets.setStatus("mandatory")
_BdlocIfpupInPkts_Type = Counter32
_BdlocIfpupInPkts_Object = MibTableColumn
bdlocIfpupInPkts = _BdlocIfpupInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 86),
    _BdlocIfpupInPkts_Type()
)
bdlocIfpupInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfpupInPkts.setStatus("mandatory")
_BdlocIfpupOutPkts_Type = Counter32
_BdlocIfpupOutPkts_Object = MibTableColumn
bdlocIfpupOutPkts = _BdlocIfpupOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 87),
    _BdlocIfpupOutPkts_Type()
)
bdlocIfpupOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfpupOutPkts.setStatus("mandatory")
_BdlocIfpupInOctets_Type = Counter32
_BdlocIfpupInOctets_Object = MibTableColumn
bdlocIfpupInOctets = _BdlocIfpupInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 88),
    _BdlocIfpupInOctets_Type()
)
bdlocIfpupInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfpupInOctets.setStatus("mandatory")
_BdlocIfpupOutOctets_Type = Counter32
_BdlocIfpupOutOctets_Object = MibTableColumn
bdlocIfpupOutOctets = _BdlocIfpupOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 89),
    _BdlocIfpupOutOctets_Type()
)
bdlocIfpupOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfpupOutOctets.setStatus("mandatory")
_BdlocIfmopInPkts_Type = Counter32
_BdlocIfmopInPkts_Object = MibTableColumn
bdlocIfmopInPkts = _BdlocIfmopInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 90),
    _BdlocIfmopInPkts_Type()
)
bdlocIfmopInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfmopInPkts.setStatus("mandatory")
_BdlocIfmopOutPkts_Type = Counter32
_BdlocIfmopOutPkts_Object = MibTableColumn
bdlocIfmopOutPkts = _BdlocIfmopOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 91),
    _BdlocIfmopOutPkts_Type()
)
bdlocIfmopOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfmopOutPkts.setStatus("mandatory")
_BdlocIfmopInOctets_Type = Counter32
_BdlocIfmopInOctets_Object = MibTableColumn
bdlocIfmopInOctets = _BdlocIfmopInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 92),
    _BdlocIfmopInOctets_Type()
)
bdlocIfmopInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfmopInOctets.setStatus("mandatory")
_BdlocIfmopOutOctets_Type = Counter32
_BdlocIfmopOutOctets_Object = MibTableColumn
bdlocIfmopOutOctets = _BdlocIfmopOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 93),
    _BdlocIfmopOutOctets_Type()
)
bdlocIfmopOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfmopOutOctets.setStatus("mandatory")
_BdlocIflanmanInPkts_Type = Counter32
_BdlocIflanmanInPkts_Object = MibTableColumn
bdlocIflanmanInPkts = _BdlocIflanmanInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 94),
    _BdlocIflanmanInPkts_Type()
)
bdlocIflanmanInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIflanmanInPkts.setStatus("mandatory")
_BdlocIflanmanOutPkts_Type = Counter32
_BdlocIflanmanOutPkts_Object = MibTableColumn
bdlocIflanmanOutPkts = _BdlocIflanmanOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 95),
    _BdlocIflanmanOutPkts_Type()
)
bdlocIflanmanOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIflanmanOutPkts.setStatus("mandatory")
_BdlocIflanmanInOctets_Type = Counter32
_BdlocIflanmanInOctets_Object = MibTableColumn
bdlocIflanmanInOctets = _BdlocIflanmanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 96),
    _BdlocIflanmanInOctets_Type()
)
bdlocIflanmanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIflanmanInOctets.setStatus("mandatory")
_BdlocIflanmanOutOctets_Type = Counter32
_BdlocIflanmanOutOctets_Object = MibTableColumn
bdlocIflanmanOutOctets = _BdlocIflanmanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 97),
    _BdlocIflanmanOutOctets_Type()
)
bdlocIflanmanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIflanmanOutOctets.setStatus("mandatory")
_BdlocIfstunInPkts_Type = Counter32
_BdlocIfstunInPkts_Object = MibTableColumn
bdlocIfstunInPkts = _BdlocIfstunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 98),
    _BdlocIfstunInPkts_Type()
)
bdlocIfstunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfstunInPkts.setStatus("mandatory")
_BdlocIfstunOutPkts_Type = Counter32
_BdlocIfstunOutPkts_Object = MibTableColumn
bdlocIfstunOutPkts = _BdlocIfstunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 99),
    _BdlocIfstunOutPkts_Type()
)
bdlocIfstunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfstunOutPkts.setStatus("mandatory")
_BdlocIfstunInOctets_Type = Counter32
_BdlocIfstunInOctets_Object = MibTableColumn
bdlocIfstunInOctets = _BdlocIfstunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 100),
    _BdlocIfstunInOctets_Type()
)
bdlocIfstunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfstunInOctets.setStatus("mandatory")
_BdlocIfstunOutOctets_Type = Counter32
_BdlocIfstunOutOctets_Object = MibTableColumn
bdlocIfstunOutOctets = _BdlocIfstunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 101),
    _BdlocIfstunOutOctets_Type()
)
bdlocIfstunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfstunOutOctets.setStatus("mandatory")
_BdlocIfspanInPkts_Type = Counter32
_BdlocIfspanInPkts_Object = MibTableColumn
bdlocIfspanInPkts = _BdlocIfspanInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 102),
    _BdlocIfspanInPkts_Type()
)
bdlocIfspanInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfspanInPkts.setStatus("mandatory")
_BdlocIfspanOutPkts_Type = Counter32
_BdlocIfspanOutPkts_Object = MibTableColumn
bdlocIfspanOutPkts = _BdlocIfspanOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 103),
    _BdlocIfspanOutPkts_Type()
)
bdlocIfspanOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfspanOutPkts.setStatus("mandatory")
_BdlocIfspanInOctets_Type = Counter32
_BdlocIfspanInOctets_Object = MibTableColumn
bdlocIfspanInOctets = _BdlocIfspanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 104),
    _BdlocIfspanInOctets_Type()
)
bdlocIfspanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfspanInOctets.setStatus("mandatory")
_BdlocIfspanOutOctets_Type = Counter32
_BdlocIfspanOutOctets_Object = MibTableColumn
bdlocIfspanOutOctets = _BdlocIfspanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 105),
    _BdlocIfspanOutOctets_Type()
)
bdlocIfspanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfspanOutOctets.setStatus("mandatory")
_BdlocIfarpInPkts_Type = Counter32
_BdlocIfarpInPkts_Object = MibTableColumn
bdlocIfarpInPkts = _BdlocIfarpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 106),
    _BdlocIfarpInPkts_Type()
)
bdlocIfarpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfarpInPkts.setStatus("mandatory")
_BdlocIfarpOutPkts_Type = Counter32
_BdlocIfarpOutPkts_Object = MibTableColumn
bdlocIfarpOutPkts = _BdlocIfarpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 107),
    _BdlocIfarpOutPkts_Type()
)
bdlocIfarpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfarpOutPkts.setStatus("mandatory")
_BdlocIfarpInOctets_Type = Counter32
_BdlocIfarpInOctets_Object = MibTableColumn
bdlocIfarpInOctets = _BdlocIfarpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 108),
    _BdlocIfarpInOctets_Type()
)
bdlocIfarpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfarpInOctets.setStatus("mandatory")
_BdlocIfarpOutOctets_Type = Counter32
_BdlocIfarpOutOctets_Object = MibTableColumn
bdlocIfarpOutOctets = _BdlocIfarpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 109),
    _BdlocIfarpOutOctets_Type()
)
bdlocIfarpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfarpOutOctets.setStatus("mandatory")
_BdlocIfprobeInPkts_Type = Counter32
_BdlocIfprobeInPkts_Object = MibTableColumn
bdlocIfprobeInPkts = _BdlocIfprobeInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 110),
    _BdlocIfprobeInPkts_Type()
)
bdlocIfprobeInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfprobeInPkts.setStatus("mandatory")
_BdlocIfprobeOutPkts_Type = Counter32
_BdlocIfprobeOutPkts_Object = MibTableColumn
bdlocIfprobeOutPkts = _BdlocIfprobeOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 111),
    _BdlocIfprobeOutPkts_Type()
)
bdlocIfprobeOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfprobeOutPkts.setStatus("mandatory")
_BdlocIfprobeInOctets_Type = Counter32
_BdlocIfprobeInOctets_Object = MibTableColumn
bdlocIfprobeInOctets = _BdlocIfprobeInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 112),
    _BdlocIfprobeInOctets_Type()
)
bdlocIfprobeInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfprobeInOctets.setStatus("mandatory")
_BdlocIfprobeOutOctets_Type = Counter32
_BdlocIfprobeOutOctets_Object = MibTableColumn
bdlocIfprobeOutOctets = _BdlocIfprobeOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 113),
    _BdlocIfprobeOutOctets_Type()
)
bdlocIfprobeOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfprobeOutOctets.setStatus("mandatory")
_BdlocIfDribbleInputs_Type = Counter32
_BdlocIfDribbleInputs_Object = MibTableColumn
bdlocIfDribbleInputs = _BdlocIfDribbleInputs_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 1, 1, 114),
    _BdlocIfDribbleInputs_Type()
)
bdlocIfDribbleInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfDribbleInputs.setStatus("mandatory")
_BdlFSIPTable_Object = MibTable
bdlFSIPTable = _BdlFSIPTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2)
)
if mibBuilder.loadTexts:
    bdlFSIPTable.setStatus("mandatory")
_BdlFSIPEntry_Object = MibTableRow
bdlFSIPEntry = _BdlFSIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1)
)
bdlFSIPEntry.setIndexNames(
    (0, "BDCOM-INTERFACES", "bdlocIfFSIPIndex"),
)
if mibBuilder.loadTexts:
    bdlFSIPEntry.setStatus("mandatory")
_BdlocIfFSIPIndex_Type = Integer32
_BdlocIfFSIPIndex_Object = MibTableColumn
bdlocIfFSIPIndex = _BdlocIfFSIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1, 1),
    _BdlocIfFSIPIndex_Type()
)
bdlocIfFSIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFSIPIndex.setStatus("mandatory")


class _BdlocIfFSIPtype_Type(Integer32):
    """Custom type bdlocIfFSIPtype based on Integer32"""
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


_BdlocIfFSIPtype_Type.__name__ = "Integer32"
_BdlocIfFSIPtype_Object = MibTableColumn
bdlocIfFSIPtype = _BdlocIfFSIPtype_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1, 2),
    _BdlocIfFSIPtype_Type()
)
bdlocIfFSIPtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFSIPtype.setStatus("mandatory")


class _BdlocIfFSIPrts_Type(Integer32):
    """Custom type bdlocIfFSIPrts based on Integer32"""
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


_BdlocIfFSIPrts_Type.__name__ = "Integer32"
_BdlocIfFSIPrts_Object = MibTableColumn
bdlocIfFSIPrts = _BdlocIfFSIPrts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1, 3),
    _BdlocIfFSIPrts_Type()
)
bdlocIfFSIPrts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFSIPrts.setStatus("mandatory")


class _BdlocIfFSIPcts_Type(Integer32):
    """Custom type bdlocIfFSIPcts based on Integer32"""
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


_BdlocIfFSIPcts_Type.__name__ = "Integer32"
_BdlocIfFSIPcts_Object = MibTableColumn
bdlocIfFSIPcts = _BdlocIfFSIPcts_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1, 4),
    _BdlocIfFSIPcts_Type()
)
bdlocIfFSIPcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFSIPcts.setStatus("mandatory")


class _BdlocIfFSIPdtr_Type(Integer32):
    """Custom type bdlocIfFSIPdtr based on Integer32"""
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


_BdlocIfFSIPdtr_Type.__name__ = "Integer32"
_BdlocIfFSIPdtr_Object = MibTableColumn
bdlocIfFSIPdtr = _BdlocIfFSIPdtr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1, 5),
    _BdlocIfFSIPdtr_Type()
)
bdlocIfFSIPdtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFSIPdtr.setStatus("mandatory")


class _BdlocIfFSIPdcd_Type(Integer32):
    """Custom type bdlocIfFSIPdcd based on Integer32"""
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


_BdlocIfFSIPdcd_Type.__name__ = "Integer32"
_BdlocIfFSIPdcd_Object = MibTableColumn
bdlocIfFSIPdcd = _BdlocIfFSIPdcd_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1, 6),
    _BdlocIfFSIPdcd_Type()
)
bdlocIfFSIPdcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFSIPdcd.setStatus("mandatory")


class _BdlocIfFSIPdsr_Type(Integer32):
    """Custom type bdlocIfFSIPdsr based on Integer32"""
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


_BdlocIfFSIPdsr_Type.__name__ = "Integer32"
_BdlocIfFSIPdsr_Object = MibTableColumn
bdlocIfFSIPdsr = _BdlocIfFSIPdsr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1, 7),
    _BdlocIfFSIPdsr_Type()
)
bdlocIfFSIPdsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFSIPdsr.setStatus("mandatory")
_BdlocIfFSIPrxClockrate_Type = Integer32
_BdlocIfFSIPrxClockrate_Object = MibTableColumn
bdlocIfFSIPrxClockrate = _BdlocIfFSIPrxClockrate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1, 8),
    _BdlocIfFSIPrxClockrate_Type()
)
bdlocIfFSIPrxClockrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFSIPrxClockrate.setStatus("mandatory")
_BdlocIfFSIPrxClockrateHi_Type = Integer32
_BdlocIfFSIPrxClockrateHi_Object = MibTableColumn
bdlocIfFSIPrxClockrateHi = _BdlocIfFSIPrxClockrateHi_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1, 9),
    _BdlocIfFSIPrxClockrateHi_Type()
)
bdlocIfFSIPrxClockrateHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFSIPrxClockrateHi.setStatus("mandatory")


class _BdlocIfFSIPportType_Type(Integer32):
    """Custom type bdlocIfFSIPportType based on Integer32"""
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


_BdlocIfFSIPportType_Type.__name__ = "Integer32"
_BdlocIfFSIPportType_Object = MibTableColumn
bdlocIfFSIPportType = _BdlocIfFSIPportType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 2, 2, 1, 10),
    _BdlocIfFSIPportType_Type()
)
bdlocIfFSIPportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdlocIfFSIPportType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-INTERFACES",
    **{"bdlinterfaces": bdlinterfaces,
       "bdlifTable": bdlifTable,
       "bdlifEntry": bdlifEntry,
       "bdlocIfHardType": bdlocIfHardType,
       "bdlocIfLineProt": bdlocIfLineProt,
       "bdlocIfLastIn": bdlocIfLastIn,
       "bdlocIfLastOut": bdlocIfLastOut,
       "bdlocIfLastOutHang": bdlocIfLastOutHang,
       "bdlocIfInBitsSec": bdlocIfInBitsSec,
       "bdlocIfInPktsSec": bdlocIfInPktsSec,
       "bdlocIfOutBitsSec": bdlocIfOutBitsSec,
       "bdlocIfOutPktsSec": bdlocIfOutPktsSec,
       "bdlocIfInRunts": bdlocIfInRunts,
       "bdlocIfInGiants": bdlocIfInGiants,
       "bdlocIfInCRC": bdlocIfInCRC,
       "bdlocIfInFrame": bdlocIfInFrame,
       "bdlocIfInOverrun": bdlocIfInOverrun,
       "bdlocIfInIgnored": bdlocIfInIgnored,
       "bdlocIfInAbort": bdlocIfInAbort,
       "bdlocIfResets": bdlocIfResets,
       "bdlocIfRestarts": bdlocIfRestarts,
       "bdlocIfKeep": bdlocIfKeep,
       "bdlocIfReason": bdlocIfReason,
       "bdlocIfCarTrans": bdlocIfCarTrans,
       "bdlocIfReliab": bdlocIfReliab,
       "bdlocIfDelay": bdlocIfDelay,
       "bdlocIfLoad": bdlocIfLoad,
       "bdlocIfCollisions": bdlocIfCollisions,
       "bdlocIfInputQueueDrops": bdlocIfInputQueueDrops,
       "bdlocIfOutputQueueDrops": bdlocIfOutputQueueDrops,
       "bdlocIfDescr": bdlocIfDescr,
       "bdlocIfSlowInPkts": bdlocIfSlowInPkts,
       "bdlocIfSlowOutPkts": bdlocIfSlowOutPkts,
       "bdlocIfSlowInOctets": bdlocIfSlowInOctets,
       "bdlocIfSlowOutOctets": bdlocIfSlowOutOctets,
       "bdlocIfFastInPkts": bdlocIfFastInPkts,
       "bdlocIfFastOutPkts": bdlocIfFastOutPkts,
       "bdlocIfFastInOctets": bdlocIfFastInOctets,
       "bdlocIfFastOutOctets": bdlocIfFastOutOctets,
       "bdlocIfotherInPkts": bdlocIfotherInPkts,
       "bdlocIfotherOutPkts": bdlocIfotherOutPkts,
       "bdlocIfotherInOctets": bdlocIfotherInOctets,
       "bdlocIfotherOutOctets": bdlocIfotherOutOctets,
       "bdlocIfipInPkts": bdlocIfipInPkts,
       "bdlocIfipOutPkts": bdlocIfipOutPkts,
       "bdlocIfipInOctets": bdlocIfipInOctets,
       "bdlocIfipOutOctets": bdlocIfipOutOctets,
       "bdlocIfdecnetInPkts": bdlocIfdecnetInPkts,
       "bdlocIfdecnetOutPkts": bdlocIfdecnetOutPkts,
       "bdlocIfdecnetInOctets": bdlocIfdecnetInOctets,
       "bdlocIfdecnetOutOctets": bdlocIfdecnetOutOctets,
       "bdlocIfxnsInPkts": bdlocIfxnsInPkts,
       "bdlocIfxnsOutPkts": bdlocIfxnsOutPkts,
       "bdlocIfxnsInOctets": bdlocIfxnsInOctets,
       "bdlocIfxnsOutOctets": bdlocIfxnsOutOctets,
       "bdlocIfclnsInPkts": bdlocIfclnsInPkts,
       "bdlocIfclnsOutPkts": bdlocIfclnsOutPkts,
       "bdlocIfclnsInOctets": bdlocIfclnsInOctets,
       "bdlocIfclnsOutOctets": bdlocIfclnsOutOctets,
       "bdlocIfappletalkInPkts": bdlocIfappletalkInPkts,
       "bdlocIfappletalkOutPkts": bdlocIfappletalkOutPkts,
       "bdlocIfappletalkInOctets": bdlocIfappletalkInOctets,
       "bdlocIfappletalkOutOctets": bdlocIfappletalkOutOctets,
       "bdlocIfnovellInPkts": bdlocIfnovellInPkts,
       "bdlocIfnovellOutPkts": bdlocIfnovellOutPkts,
       "bdlocIfnovellInOctets": bdlocIfnovellInOctets,
       "bdlocIfnovellOutOctets": bdlocIfnovellOutOctets,
       "bdlocIfapolloInPkts": bdlocIfapolloInPkts,
       "bdlocIfapolloOutPkts": bdlocIfapolloOutPkts,
       "bdlocIfapolloInOctets": bdlocIfapolloInOctets,
       "bdlocIfapolloOutOctets": bdlocIfapolloOutOctets,
       "bdlocIfvinesInPkts": bdlocIfvinesInPkts,
       "bdlocIfvinesOutPkts": bdlocIfvinesOutPkts,
       "bdlocIfvinesInOctets": bdlocIfvinesInOctets,
       "bdlocIfvinesOutOctets": bdlocIfvinesOutOctets,
       "bdlocIfbridgedInPkts": bdlocIfbridgedInPkts,
       "bdlocIfbridgedOutPkts": bdlocIfbridgedOutPkts,
       "bdlocIfbridgedInOctets": bdlocIfbridgedInOctets,
       "bdlocIfbridgedOutOctets": bdlocIfbridgedOutOctets,
       "bdlocIfsrbInPkts": bdlocIfsrbInPkts,
       "bdlocIfsrbOutPkts": bdlocIfsrbOutPkts,
       "bdlocIfsrbInOctets": bdlocIfsrbInOctets,
       "bdlocIfsrbOutOctets": bdlocIfsrbOutOctets,
       "bdlocIfchaosInPkts": bdlocIfchaosInPkts,
       "bdlocIfchaosOutPkts": bdlocIfchaosOutPkts,
       "bdlocIfchaosInOctets": bdlocIfchaosInOctets,
       "bdlocIfchaosOutOctets": bdlocIfchaosOutOctets,
       "bdlocIfpupInPkts": bdlocIfpupInPkts,
       "bdlocIfpupOutPkts": bdlocIfpupOutPkts,
       "bdlocIfpupInOctets": bdlocIfpupInOctets,
       "bdlocIfpupOutOctets": bdlocIfpupOutOctets,
       "bdlocIfmopInPkts": bdlocIfmopInPkts,
       "bdlocIfmopOutPkts": bdlocIfmopOutPkts,
       "bdlocIfmopInOctets": bdlocIfmopInOctets,
       "bdlocIfmopOutOctets": bdlocIfmopOutOctets,
       "bdlocIflanmanInPkts": bdlocIflanmanInPkts,
       "bdlocIflanmanOutPkts": bdlocIflanmanOutPkts,
       "bdlocIflanmanInOctets": bdlocIflanmanInOctets,
       "bdlocIflanmanOutOctets": bdlocIflanmanOutOctets,
       "bdlocIfstunInPkts": bdlocIfstunInPkts,
       "bdlocIfstunOutPkts": bdlocIfstunOutPkts,
       "bdlocIfstunInOctets": bdlocIfstunInOctets,
       "bdlocIfstunOutOctets": bdlocIfstunOutOctets,
       "bdlocIfspanInPkts": bdlocIfspanInPkts,
       "bdlocIfspanOutPkts": bdlocIfspanOutPkts,
       "bdlocIfspanInOctets": bdlocIfspanInOctets,
       "bdlocIfspanOutOctets": bdlocIfspanOutOctets,
       "bdlocIfarpInPkts": bdlocIfarpInPkts,
       "bdlocIfarpOutPkts": bdlocIfarpOutPkts,
       "bdlocIfarpInOctets": bdlocIfarpInOctets,
       "bdlocIfarpOutOctets": bdlocIfarpOutOctets,
       "bdlocIfprobeInPkts": bdlocIfprobeInPkts,
       "bdlocIfprobeOutPkts": bdlocIfprobeOutPkts,
       "bdlocIfprobeInOctets": bdlocIfprobeInOctets,
       "bdlocIfprobeOutOctets": bdlocIfprobeOutOctets,
       "bdlocIfDribbleInputs": bdlocIfDribbleInputs,
       "bdlFSIPTable": bdlFSIPTable,
       "bdlFSIPEntry": bdlFSIPEntry,
       "bdlocIfFSIPIndex": bdlocIfFSIPIndex,
       "bdlocIfFSIPtype": bdlocIfFSIPtype,
       "bdlocIfFSIPrts": bdlocIfFSIPrts,
       "bdlocIfFSIPcts": bdlocIfFSIPcts,
       "bdlocIfFSIPdtr": bdlocIfFSIPdtr,
       "bdlocIfFSIPdcd": bdlocIfFSIPdcd,
       "bdlocIfFSIPdsr": bdlocIfFSIPdsr,
       "bdlocIfFSIPrxClockrate": bdlocIfFSIPrxClockrate,
       "bdlocIfFSIPrxClockrateHi": bdlocIfFSIPrxClockrateHi,
       "bdlocIfFSIPportType": bdlocIfFSIPportType}
)
