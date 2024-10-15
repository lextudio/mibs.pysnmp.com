# SNMP MIB module (NMS-INTERFACES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-INTERFACES
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:57 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

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

_Nmslinterfaces_ObjectIdentity = ObjectIdentity
nmslinterfaces = _Nmslinterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2)
)
_NmslifTable_Object = MibTable
nmslifTable = _NmslifTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nmslifTable.setStatus("mandatory")
_NmslifEntry_Object = MibTableRow
nmslifEntry = _NmslifEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1)
)
nmslifEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nmslifEntry.setStatus("mandatory")
_NmslocIfHardType_Type = DisplayString
_NmslocIfHardType_Object = MibTableColumn
nmslocIfHardType = _NmslocIfHardType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 1),
    _NmslocIfHardType_Type()
)
nmslocIfHardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfHardType.setStatus("mandatory")
_NmslocIfLineProt_Type = Integer32
_NmslocIfLineProt_Object = MibTableColumn
nmslocIfLineProt = _NmslocIfLineProt_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 2),
    _NmslocIfLineProt_Type()
)
nmslocIfLineProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfLineProt.setStatus("mandatory")
_NmslocIfLastIn_Type = Integer32
_NmslocIfLastIn_Object = MibTableColumn
nmslocIfLastIn = _NmslocIfLastIn_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 3),
    _NmslocIfLastIn_Type()
)
nmslocIfLastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfLastIn.setStatus("mandatory")
_NmslocIfLastOut_Type = Integer32
_NmslocIfLastOut_Object = MibTableColumn
nmslocIfLastOut = _NmslocIfLastOut_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 4),
    _NmslocIfLastOut_Type()
)
nmslocIfLastOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfLastOut.setStatus("mandatory")
_NmslocIfLastOutHang_Type = Integer32
_NmslocIfLastOutHang_Object = MibTableColumn
nmslocIfLastOutHang = _NmslocIfLastOutHang_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 5),
    _NmslocIfLastOutHang_Type()
)
nmslocIfLastOutHang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfLastOutHang.setStatus("mandatory")
_NmslocIfInBitsSec_Type = Integer32
_NmslocIfInBitsSec_Object = MibTableColumn
nmslocIfInBitsSec = _NmslocIfInBitsSec_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 6),
    _NmslocIfInBitsSec_Type()
)
nmslocIfInBitsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfInBitsSec.setStatus("mandatory")
_NmslocIfInPktsSec_Type = Integer32
_NmslocIfInPktsSec_Object = MibTableColumn
nmslocIfInPktsSec = _NmslocIfInPktsSec_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 7),
    _NmslocIfInPktsSec_Type()
)
nmslocIfInPktsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfInPktsSec.setStatus("mandatory")
_NmslocIfOutBitsSec_Type = Integer32
_NmslocIfOutBitsSec_Object = MibTableColumn
nmslocIfOutBitsSec = _NmslocIfOutBitsSec_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 8),
    _NmslocIfOutBitsSec_Type()
)
nmslocIfOutBitsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfOutBitsSec.setStatus("mandatory")
_NmslocIfOutPktsSec_Type = Integer32
_NmslocIfOutPktsSec_Object = MibTableColumn
nmslocIfOutPktsSec = _NmslocIfOutPktsSec_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 9),
    _NmslocIfOutPktsSec_Type()
)
nmslocIfOutPktsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfOutPktsSec.setStatus("mandatory")
_NmslocIfInRunts_Type = Integer32
_NmslocIfInRunts_Object = MibTableColumn
nmslocIfInRunts = _NmslocIfInRunts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 10),
    _NmslocIfInRunts_Type()
)
nmslocIfInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfInRunts.setStatus("mandatory")
_NmslocIfInGiants_Type = Integer32
_NmslocIfInGiants_Object = MibTableColumn
nmslocIfInGiants = _NmslocIfInGiants_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 11),
    _NmslocIfInGiants_Type()
)
nmslocIfInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfInGiants.setStatus("mandatory")
_NmslocIfInCRC_Type = Integer32
_NmslocIfInCRC_Object = MibTableColumn
nmslocIfInCRC = _NmslocIfInCRC_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 12),
    _NmslocIfInCRC_Type()
)
nmslocIfInCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfInCRC.setStatus("mandatory")
_NmslocIfInFrame_Type = Integer32
_NmslocIfInFrame_Object = MibTableColumn
nmslocIfInFrame = _NmslocIfInFrame_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 13),
    _NmslocIfInFrame_Type()
)
nmslocIfInFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfInFrame.setStatus("mandatory")
_NmslocIfInOverrun_Type = Integer32
_NmslocIfInOverrun_Object = MibTableColumn
nmslocIfInOverrun = _NmslocIfInOverrun_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 14),
    _NmslocIfInOverrun_Type()
)
nmslocIfInOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfInOverrun.setStatus("mandatory")
_NmslocIfInIgnored_Type = Integer32
_NmslocIfInIgnored_Object = MibTableColumn
nmslocIfInIgnored = _NmslocIfInIgnored_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 15),
    _NmslocIfInIgnored_Type()
)
nmslocIfInIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfInIgnored.setStatus("mandatory")
_NmslocIfInAbort_Type = Integer32
_NmslocIfInAbort_Object = MibTableColumn
nmslocIfInAbort = _NmslocIfInAbort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 16),
    _NmslocIfInAbort_Type()
)
nmslocIfInAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfInAbort.setStatus("mandatory")
_NmslocIfResets_Type = Integer32
_NmslocIfResets_Object = MibTableColumn
nmslocIfResets = _NmslocIfResets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 17),
    _NmslocIfResets_Type()
)
nmslocIfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfResets.setStatus("mandatory")
_NmslocIfRestarts_Type = Integer32
_NmslocIfRestarts_Object = MibTableColumn
nmslocIfRestarts = _NmslocIfRestarts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 18),
    _NmslocIfRestarts_Type()
)
nmslocIfRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfRestarts.setStatus("mandatory")
_NmslocIfKeep_Type = Integer32
_NmslocIfKeep_Object = MibTableColumn
nmslocIfKeep = _NmslocIfKeep_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 19),
    _NmslocIfKeep_Type()
)
nmslocIfKeep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfKeep.setStatus("mandatory")
_NmslocIfReason_Type = DisplayString
_NmslocIfReason_Object = MibTableColumn
nmslocIfReason = _NmslocIfReason_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 20),
    _NmslocIfReason_Type()
)
nmslocIfReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfReason.setStatus("mandatory")
_NmslocIfCarTrans_Type = Integer32
_NmslocIfCarTrans_Object = MibTableColumn
nmslocIfCarTrans = _NmslocIfCarTrans_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 21),
    _NmslocIfCarTrans_Type()
)
nmslocIfCarTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfCarTrans.setStatus("mandatory")
_NmslocIfReliab_Type = Integer32
_NmslocIfReliab_Object = MibTableColumn
nmslocIfReliab = _NmslocIfReliab_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 22),
    _NmslocIfReliab_Type()
)
nmslocIfReliab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfReliab.setStatus("mandatory")
_NmslocIfDelay_Type = Integer32
_NmslocIfDelay_Object = MibTableColumn
nmslocIfDelay = _NmslocIfDelay_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 23),
    _NmslocIfDelay_Type()
)
nmslocIfDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfDelay.setStatus("mandatory")
_NmslocIfLoad_Type = Integer32
_NmslocIfLoad_Object = MibTableColumn
nmslocIfLoad = _NmslocIfLoad_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 24),
    _NmslocIfLoad_Type()
)
nmslocIfLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfLoad.setStatus("mandatory")
_NmslocIfCollisions_Type = Integer32
_NmslocIfCollisions_Object = MibTableColumn
nmslocIfCollisions = _NmslocIfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 25),
    _NmslocIfCollisions_Type()
)
nmslocIfCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfCollisions.setStatus("mandatory")
_NmslocIfInputQueueDrops_Type = Integer32
_NmslocIfInputQueueDrops_Object = MibTableColumn
nmslocIfInputQueueDrops = _NmslocIfInputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 26),
    _NmslocIfInputQueueDrops_Type()
)
nmslocIfInputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfInputQueueDrops.setStatus("mandatory")
_NmslocIfOutputQueueDrops_Type = Integer32
_NmslocIfOutputQueueDrops_Object = MibTableColumn
nmslocIfOutputQueueDrops = _NmslocIfOutputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 27),
    _NmslocIfOutputQueueDrops_Type()
)
nmslocIfOutputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfOutputQueueDrops.setStatus("mandatory")
_NmslocIfDescr_Type = DisplayString
_NmslocIfDescr_Object = MibTableColumn
nmslocIfDescr = _NmslocIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 28),
    _NmslocIfDescr_Type()
)
nmslocIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmslocIfDescr.setStatus("mandatory")
_NmslocIfSlowInPkts_Type = Counter32
_NmslocIfSlowInPkts_Object = MibTableColumn
nmslocIfSlowInPkts = _NmslocIfSlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 30),
    _NmslocIfSlowInPkts_Type()
)
nmslocIfSlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfSlowInPkts.setStatus("mandatory")
_NmslocIfSlowOutPkts_Type = Counter32
_NmslocIfSlowOutPkts_Object = MibTableColumn
nmslocIfSlowOutPkts = _NmslocIfSlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 31),
    _NmslocIfSlowOutPkts_Type()
)
nmslocIfSlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfSlowOutPkts.setStatus("mandatory")
_NmslocIfSlowInOctets_Type = Counter32
_NmslocIfSlowInOctets_Object = MibTableColumn
nmslocIfSlowInOctets = _NmslocIfSlowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 32),
    _NmslocIfSlowInOctets_Type()
)
nmslocIfSlowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfSlowInOctets.setStatus("mandatory")
_NmslocIfSlowOutOctets_Type = Counter32
_NmslocIfSlowOutOctets_Object = MibTableColumn
nmslocIfSlowOutOctets = _NmslocIfSlowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 33),
    _NmslocIfSlowOutOctets_Type()
)
nmslocIfSlowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfSlowOutOctets.setStatus("mandatory")
_NmslocIfFastInPkts_Type = Counter32
_NmslocIfFastInPkts_Object = MibTableColumn
nmslocIfFastInPkts = _NmslocIfFastInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 34),
    _NmslocIfFastInPkts_Type()
)
nmslocIfFastInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFastInPkts.setStatus("mandatory")
_NmslocIfFastOutPkts_Type = Counter32
_NmslocIfFastOutPkts_Object = MibTableColumn
nmslocIfFastOutPkts = _NmslocIfFastOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 35),
    _NmslocIfFastOutPkts_Type()
)
nmslocIfFastOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFastOutPkts.setStatus("mandatory")
_NmslocIfFastInOctets_Type = Counter32
_NmslocIfFastInOctets_Object = MibTableColumn
nmslocIfFastInOctets = _NmslocIfFastInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 36),
    _NmslocIfFastInOctets_Type()
)
nmslocIfFastInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFastInOctets.setStatus("mandatory")
_NmslocIfFastOutOctets_Type = Counter32
_NmslocIfFastOutOctets_Object = MibTableColumn
nmslocIfFastOutOctets = _NmslocIfFastOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 37),
    _NmslocIfFastOutOctets_Type()
)
nmslocIfFastOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFastOutOctets.setStatus("mandatory")
_NmslocIfotherInPkts_Type = Counter32
_NmslocIfotherInPkts_Object = MibTableColumn
nmslocIfotherInPkts = _NmslocIfotherInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 38),
    _NmslocIfotherInPkts_Type()
)
nmslocIfotherInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfotherInPkts.setStatus("mandatory")
_NmslocIfotherOutPkts_Type = Counter32
_NmslocIfotherOutPkts_Object = MibTableColumn
nmslocIfotherOutPkts = _NmslocIfotherOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 39),
    _NmslocIfotherOutPkts_Type()
)
nmslocIfotherOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfotherOutPkts.setStatus("mandatory")
_NmslocIfotherInOctets_Type = Counter32
_NmslocIfotherInOctets_Object = MibTableColumn
nmslocIfotherInOctets = _NmslocIfotherInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 40),
    _NmslocIfotherInOctets_Type()
)
nmslocIfotherInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfotherInOctets.setStatus("mandatory")
_NmslocIfotherOutOctets_Type = Counter32
_NmslocIfotherOutOctets_Object = MibTableColumn
nmslocIfotherOutOctets = _NmslocIfotherOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 41),
    _NmslocIfotherOutOctets_Type()
)
nmslocIfotherOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfotherOutOctets.setStatus("mandatory")
_NmslocIfipInPkts_Type = Counter32
_NmslocIfipInPkts_Object = MibTableColumn
nmslocIfipInPkts = _NmslocIfipInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 42),
    _NmslocIfipInPkts_Type()
)
nmslocIfipInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfipInPkts.setStatus("mandatory")
_NmslocIfipOutPkts_Type = Counter32
_NmslocIfipOutPkts_Object = MibTableColumn
nmslocIfipOutPkts = _NmslocIfipOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 43),
    _NmslocIfipOutPkts_Type()
)
nmslocIfipOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfipOutPkts.setStatus("mandatory")
_NmslocIfipInOctets_Type = Counter32
_NmslocIfipInOctets_Object = MibTableColumn
nmslocIfipInOctets = _NmslocIfipInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 44),
    _NmslocIfipInOctets_Type()
)
nmslocIfipInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfipInOctets.setStatus("mandatory")
_NmslocIfipOutOctets_Type = Counter32
_NmslocIfipOutOctets_Object = MibTableColumn
nmslocIfipOutOctets = _NmslocIfipOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 45),
    _NmslocIfipOutOctets_Type()
)
nmslocIfipOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfipOutOctets.setStatus("mandatory")
_NmslocIfdecnetInPkts_Type = Counter32
_NmslocIfdecnetInPkts_Object = MibTableColumn
nmslocIfdecnetInPkts = _NmslocIfdecnetInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 46),
    _NmslocIfdecnetInPkts_Type()
)
nmslocIfdecnetInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfdecnetInPkts.setStatus("mandatory")
_NmslocIfdecnetOutPkts_Type = Counter32
_NmslocIfdecnetOutPkts_Object = MibTableColumn
nmslocIfdecnetOutPkts = _NmslocIfdecnetOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 47),
    _NmslocIfdecnetOutPkts_Type()
)
nmslocIfdecnetOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfdecnetOutPkts.setStatus("mandatory")
_NmslocIfdecnetInOctets_Type = Counter32
_NmslocIfdecnetInOctets_Object = MibTableColumn
nmslocIfdecnetInOctets = _NmslocIfdecnetInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 48),
    _NmslocIfdecnetInOctets_Type()
)
nmslocIfdecnetInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfdecnetInOctets.setStatus("mandatory")
_NmslocIfdecnetOutOctets_Type = Counter32
_NmslocIfdecnetOutOctets_Object = MibTableColumn
nmslocIfdecnetOutOctets = _NmslocIfdecnetOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 49),
    _NmslocIfdecnetOutOctets_Type()
)
nmslocIfdecnetOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfdecnetOutOctets.setStatus("mandatory")
_NmslocIfxnsInPkts_Type = Counter32
_NmslocIfxnsInPkts_Object = MibTableColumn
nmslocIfxnsInPkts = _NmslocIfxnsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 50),
    _NmslocIfxnsInPkts_Type()
)
nmslocIfxnsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfxnsInPkts.setStatus("mandatory")
_NmslocIfxnsOutPkts_Type = Counter32
_NmslocIfxnsOutPkts_Object = MibTableColumn
nmslocIfxnsOutPkts = _NmslocIfxnsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 51),
    _NmslocIfxnsOutPkts_Type()
)
nmslocIfxnsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfxnsOutPkts.setStatus("mandatory")
_NmslocIfxnsInOctets_Type = Counter32
_NmslocIfxnsInOctets_Object = MibTableColumn
nmslocIfxnsInOctets = _NmslocIfxnsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 52),
    _NmslocIfxnsInOctets_Type()
)
nmslocIfxnsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfxnsInOctets.setStatus("mandatory")
_NmslocIfxnsOutOctets_Type = Counter32
_NmslocIfxnsOutOctets_Object = MibTableColumn
nmslocIfxnsOutOctets = _NmslocIfxnsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 53),
    _NmslocIfxnsOutOctets_Type()
)
nmslocIfxnsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfxnsOutOctets.setStatus("mandatory")
_NmslocIfclnsInPkts_Type = Counter32
_NmslocIfclnsInPkts_Object = MibTableColumn
nmslocIfclnsInPkts = _NmslocIfclnsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 54),
    _NmslocIfclnsInPkts_Type()
)
nmslocIfclnsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfclnsInPkts.setStatus("mandatory")
_NmslocIfclnsOutPkts_Type = Counter32
_NmslocIfclnsOutPkts_Object = MibTableColumn
nmslocIfclnsOutPkts = _NmslocIfclnsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 55),
    _NmslocIfclnsOutPkts_Type()
)
nmslocIfclnsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfclnsOutPkts.setStatus("mandatory")
_NmslocIfclnsInOctets_Type = Counter32
_NmslocIfclnsInOctets_Object = MibTableColumn
nmslocIfclnsInOctets = _NmslocIfclnsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 56),
    _NmslocIfclnsInOctets_Type()
)
nmslocIfclnsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfclnsInOctets.setStatus("mandatory")
_NmslocIfclnsOutOctets_Type = Counter32
_NmslocIfclnsOutOctets_Object = MibTableColumn
nmslocIfclnsOutOctets = _NmslocIfclnsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 57),
    _NmslocIfclnsOutOctets_Type()
)
nmslocIfclnsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfclnsOutOctets.setStatus("mandatory")
_NmslocIfappletalkInPkts_Type = Counter32
_NmslocIfappletalkInPkts_Object = MibTableColumn
nmslocIfappletalkInPkts = _NmslocIfappletalkInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 58),
    _NmslocIfappletalkInPkts_Type()
)
nmslocIfappletalkInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfappletalkInPkts.setStatus("mandatory")
_NmslocIfappletalkOutPkts_Type = Counter32
_NmslocIfappletalkOutPkts_Object = MibTableColumn
nmslocIfappletalkOutPkts = _NmslocIfappletalkOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 59),
    _NmslocIfappletalkOutPkts_Type()
)
nmslocIfappletalkOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfappletalkOutPkts.setStatus("mandatory")
_NmslocIfappletalkInOctets_Type = Counter32
_NmslocIfappletalkInOctets_Object = MibTableColumn
nmslocIfappletalkInOctets = _NmslocIfappletalkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 60),
    _NmslocIfappletalkInOctets_Type()
)
nmslocIfappletalkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfappletalkInOctets.setStatus("mandatory")
_NmslocIfappletalkOutOctets_Type = Counter32
_NmslocIfappletalkOutOctets_Object = MibTableColumn
nmslocIfappletalkOutOctets = _NmslocIfappletalkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 61),
    _NmslocIfappletalkOutOctets_Type()
)
nmslocIfappletalkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfappletalkOutOctets.setStatus("mandatory")
_NmslocIfnovellInPkts_Type = Counter32
_NmslocIfnovellInPkts_Object = MibTableColumn
nmslocIfnovellInPkts = _NmslocIfnovellInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 62),
    _NmslocIfnovellInPkts_Type()
)
nmslocIfnovellInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfnovellInPkts.setStatus("mandatory")
_NmslocIfnovellOutPkts_Type = Counter32
_NmslocIfnovellOutPkts_Object = MibTableColumn
nmslocIfnovellOutPkts = _NmslocIfnovellOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 63),
    _NmslocIfnovellOutPkts_Type()
)
nmslocIfnovellOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfnovellOutPkts.setStatus("mandatory")
_NmslocIfnovellInOctets_Type = Counter32
_NmslocIfnovellInOctets_Object = MibTableColumn
nmslocIfnovellInOctets = _NmslocIfnovellInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 64),
    _NmslocIfnovellInOctets_Type()
)
nmslocIfnovellInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfnovellInOctets.setStatus("mandatory")
_NmslocIfnovellOutOctets_Type = Counter32
_NmslocIfnovellOutOctets_Object = MibTableColumn
nmslocIfnovellOutOctets = _NmslocIfnovellOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 65),
    _NmslocIfnovellOutOctets_Type()
)
nmslocIfnovellOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfnovellOutOctets.setStatus("mandatory")
_NmslocIfapolloInPkts_Type = Counter32
_NmslocIfapolloInPkts_Object = MibTableColumn
nmslocIfapolloInPkts = _NmslocIfapolloInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 66),
    _NmslocIfapolloInPkts_Type()
)
nmslocIfapolloInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfapolloInPkts.setStatus("mandatory")
_NmslocIfapolloOutPkts_Type = Counter32
_NmslocIfapolloOutPkts_Object = MibTableColumn
nmslocIfapolloOutPkts = _NmslocIfapolloOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 67),
    _NmslocIfapolloOutPkts_Type()
)
nmslocIfapolloOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfapolloOutPkts.setStatus("mandatory")
_NmslocIfapolloInOctets_Type = Counter32
_NmslocIfapolloInOctets_Object = MibTableColumn
nmslocIfapolloInOctets = _NmslocIfapolloInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 68),
    _NmslocIfapolloInOctets_Type()
)
nmslocIfapolloInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfapolloInOctets.setStatus("mandatory")
_NmslocIfapolloOutOctets_Type = Counter32
_NmslocIfapolloOutOctets_Object = MibTableColumn
nmslocIfapolloOutOctets = _NmslocIfapolloOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 69),
    _NmslocIfapolloOutOctets_Type()
)
nmslocIfapolloOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfapolloOutOctets.setStatus("mandatory")
_NmslocIfvinesInPkts_Type = Counter32
_NmslocIfvinesInPkts_Object = MibTableColumn
nmslocIfvinesInPkts = _NmslocIfvinesInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 70),
    _NmslocIfvinesInPkts_Type()
)
nmslocIfvinesInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfvinesInPkts.setStatus("mandatory")
_NmslocIfvinesOutPkts_Type = Counter32
_NmslocIfvinesOutPkts_Object = MibTableColumn
nmslocIfvinesOutPkts = _NmslocIfvinesOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 71),
    _NmslocIfvinesOutPkts_Type()
)
nmslocIfvinesOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfvinesOutPkts.setStatus("mandatory")
_NmslocIfvinesInOctets_Type = Counter32
_NmslocIfvinesInOctets_Object = MibTableColumn
nmslocIfvinesInOctets = _NmslocIfvinesInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 72),
    _NmslocIfvinesInOctets_Type()
)
nmslocIfvinesInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfvinesInOctets.setStatus("mandatory")
_NmslocIfvinesOutOctets_Type = Counter32
_NmslocIfvinesOutOctets_Object = MibTableColumn
nmslocIfvinesOutOctets = _NmslocIfvinesOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 73),
    _NmslocIfvinesOutOctets_Type()
)
nmslocIfvinesOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfvinesOutOctets.setStatus("mandatory")
_NmslocIfbridgedInPkts_Type = Counter32
_NmslocIfbridgedInPkts_Object = MibTableColumn
nmslocIfbridgedInPkts = _NmslocIfbridgedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 74),
    _NmslocIfbridgedInPkts_Type()
)
nmslocIfbridgedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfbridgedInPkts.setStatus("mandatory")
_NmslocIfbridgedOutPkts_Type = Counter32
_NmslocIfbridgedOutPkts_Object = MibTableColumn
nmslocIfbridgedOutPkts = _NmslocIfbridgedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 75),
    _NmslocIfbridgedOutPkts_Type()
)
nmslocIfbridgedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfbridgedOutPkts.setStatus("mandatory")
_NmslocIfbridgedInOctets_Type = Counter32
_NmslocIfbridgedInOctets_Object = MibTableColumn
nmslocIfbridgedInOctets = _NmslocIfbridgedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 76),
    _NmslocIfbridgedInOctets_Type()
)
nmslocIfbridgedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfbridgedInOctets.setStatus("mandatory")
_NmslocIfbridgedOutOctets_Type = Counter32
_NmslocIfbridgedOutOctets_Object = MibTableColumn
nmslocIfbridgedOutOctets = _NmslocIfbridgedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 77),
    _NmslocIfbridgedOutOctets_Type()
)
nmslocIfbridgedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfbridgedOutOctets.setStatus("mandatory")
_NmslocIfsrbInPkts_Type = Counter32
_NmslocIfsrbInPkts_Object = MibTableColumn
nmslocIfsrbInPkts = _NmslocIfsrbInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 78),
    _NmslocIfsrbInPkts_Type()
)
nmslocIfsrbInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfsrbInPkts.setStatus("mandatory")
_NmslocIfsrbOutPkts_Type = Counter32
_NmslocIfsrbOutPkts_Object = MibTableColumn
nmslocIfsrbOutPkts = _NmslocIfsrbOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 79),
    _NmslocIfsrbOutPkts_Type()
)
nmslocIfsrbOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfsrbOutPkts.setStatus("mandatory")
_NmslocIfsrbInOctets_Type = Counter32
_NmslocIfsrbInOctets_Object = MibTableColumn
nmslocIfsrbInOctets = _NmslocIfsrbInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 80),
    _NmslocIfsrbInOctets_Type()
)
nmslocIfsrbInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfsrbInOctets.setStatus("mandatory")
_NmslocIfsrbOutOctets_Type = Counter32
_NmslocIfsrbOutOctets_Object = MibTableColumn
nmslocIfsrbOutOctets = _NmslocIfsrbOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 81),
    _NmslocIfsrbOutOctets_Type()
)
nmslocIfsrbOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfsrbOutOctets.setStatus("mandatory")
_NmslocIfchaosInPkts_Type = Counter32
_NmslocIfchaosInPkts_Object = MibTableColumn
nmslocIfchaosInPkts = _NmslocIfchaosInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 82),
    _NmslocIfchaosInPkts_Type()
)
nmslocIfchaosInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfchaosInPkts.setStatus("mandatory")
_NmslocIfchaosOutPkts_Type = Counter32
_NmslocIfchaosOutPkts_Object = MibTableColumn
nmslocIfchaosOutPkts = _NmslocIfchaosOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 83),
    _NmslocIfchaosOutPkts_Type()
)
nmslocIfchaosOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfchaosOutPkts.setStatus("mandatory")
_NmslocIfchaosInOctets_Type = Counter32
_NmslocIfchaosInOctets_Object = MibTableColumn
nmslocIfchaosInOctets = _NmslocIfchaosInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 84),
    _NmslocIfchaosInOctets_Type()
)
nmslocIfchaosInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfchaosInOctets.setStatus("mandatory")
_NmslocIfchaosOutOctets_Type = Counter32
_NmslocIfchaosOutOctets_Object = MibTableColumn
nmslocIfchaosOutOctets = _NmslocIfchaosOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 85),
    _NmslocIfchaosOutOctets_Type()
)
nmslocIfchaosOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfchaosOutOctets.setStatus("mandatory")
_NmslocIfpupInPkts_Type = Counter32
_NmslocIfpupInPkts_Object = MibTableColumn
nmslocIfpupInPkts = _NmslocIfpupInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 86),
    _NmslocIfpupInPkts_Type()
)
nmslocIfpupInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfpupInPkts.setStatus("mandatory")
_NmslocIfpupOutPkts_Type = Counter32
_NmslocIfpupOutPkts_Object = MibTableColumn
nmslocIfpupOutPkts = _NmslocIfpupOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 87),
    _NmslocIfpupOutPkts_Type()
)
nmslocIfpupOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfpupOutPkts.setStatus("mandatory")
_NmslocIfpupInOctets_Type = Counter32
_NmslocIfpupInOctets_Object = MibTableColumn
nmslocIfpupInOctets = _NmslocIfpupInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 88),
    _NmslocIfpupInOctets_Type()
)
nmslocIfpupInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfpupInOctets.setStatus("mandatory")
_NmslocIfpupOutOctets_Type = Counter32
_NmslocIfpupOutOctets_Object = MibTableColumn
nmslocIfpupOutOctets = _NmslocIfpupOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 89),
    _NmslocIfpupOutOctets_Type()
)
nmslocIfpupOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfpupOutOctets.setStatus("mandatory")
_NmslocIfmopInPkts_Type = Counter32
_NmslocIfmopInPkts_Object = MibTableColumn
nmslocIfmopInPkts = _NmslocIfmopInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 90),
    _NmslocIfmopInPkts_Type()
)
nmslocIfmopInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfmopInPkts.setStatus("mandatory")
_NmslocIfmopOutPkts_Type = Counter32
_NmslocIfmopOutPkts_Object = MibTableColumn
nmslocIfmopOutPkts = _NmslocIfmopOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 91),
    _NmslocIfmopOutPkts_Type()
)
nmslocIfmopOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfmopOutPkts.setStatus("mandatory")
_NmslocIfmopInOctets_Type = Counter32
_NmslocIfmopInOctets_Object = MibTableColumn
nmslocIfmopInOctets = _NmslocIfmopInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 92),
    _NmslocIfmopInOctets_Type()
)
nmslocIfmopInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfmopInOctets.setStatus("mandatory")
_NmslocIfmopOutOctets_Type = Counter32
_NmslocIfmopOutOctets_Object = MibTableColumn
nmslocIfmopOutOctets = _NmslocIfmopOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 93),
    _NmslocIfmopOutOctets_Type()
)
nmslocIfmopOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfmopOutOctets.setStatus("mandatory")
_NmslocIflanmanInPkts_Type = Counter32
_NmslocIflanmanInPkts_Object = MibTableColumn
nmslocIflanmanInPkts = _NmslocIflanmanInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 94),
    _NmslocIflanmanInPkts_Type()
)
nmslocIflanmanInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIflanmanInPkts.setStatus("mandatory")
_NmslocIflanmanOutPkts_Type = Counter32
_NmslocIflanmanOutPkts_Object = MibTableColumn
nmslocIflanmanOutPkts = _NmslocIflanmanOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 95),
    _NmslocIflanmanOutPkts_Type()
)
nmslocIflanmanOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIflanmanOutPkts.setStatus("mandatory")
_NmslocIflanmanInOctets_Type = Counter32
_NmslocIflanmanInOctets_Object = MibTableColumn
nmslocIflanmanInOctets = _NmslocIflanmanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 96),
    _NmslocIflanmanInOctets_Type()
)
nmslocIflanmanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIflanmanInOctets.setStatus("mandatory")
_NmslocIflanmanOutOctets_Type = Counter32
_NmslocIflanmanOutOctets_Object = MibTableColumn
nmslocIflanmanOutOctets = _NmslocIflanmanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 97),
    _NmslocIflanmanOutOctets_Type()
)
nmslocIflanmanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIflanmanOutOctets.setStatus("mandatory")
_NmslocIfstunInPkts_Type = Counter32
_NmslocIfstunInPkts_Object = MibTableColumn
nmslocIfstunInPkts = _NmslocIfstunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 98),
    _NmslocIfstunInPkts_Type()
)
nmslocIfstunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfstunInPkts.setStatus("mandatory")
_NmslocIfstunOutPkts_Type = Counter32
_NmslocIfstunOutPkts_Object = MibTableColumn
nmslocIfstunOutPkts = _NmslocIfstunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 99),
    _NmslocIfstunOutPkts_Type()
)
nmslocIfstunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfstunOutPkts.setStatus("mandatory")
_NmslocIfstunInOctets_Type = Counter32
_NmslocIfstunInOctets_Object = MibTableColumn
nmslocIfstunInOctets = _NmslocIfstunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 100),
    _NmslocIfstunInOctets_Type()
)
nmslocIfstunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfstunInOctets.setStatus("mandatory")
_NmslocIfstunOutOctets_Type = Counter32
_NmslocIfstunOutOctets_Object = MibTableColumn
nmslocIfstunOutOctets = _NmslocIfstunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 101),
    _NmslocIfstunOutOctets_Type()
)
nmslocIfstunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfstunOutOctets.setStatus("mandatory")
_NmslocIfspanInPkts_Type = Counter32
_NmslocIfspanInPkts_Object = MibTableColumn
nmslocIfspanInPkts = _NmslocIfspanInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 102),
    _NmslocIfspanInPkts_Type()
)
nmslocIfspanInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfspanInPkts.setStatus("mandatory")
_NmslocIfspanOutPkts_Type = Counter32
_NmslocIfspanOutPkts_Object = MibTableColumn
nmslocIfspanOutPkts = _NmslocIfspanOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 103),
    _NmslocIfspanOutPkts_Type()
)
nmslocIfspanOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfspanOutPkts.setStatus("mandatory")
_NmslocIfspanInOctets_Type = Counter32
_NmslocIfspanInOctets_Object = MibTableColumn
nmslocIfspanInOctets = _NmslocIfspanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 104),
    _NmslocIfspanInOctets_Type()
)
nmslocIfspanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfspanInOctets.setStatus("mandatory")
_NmslocIfspanOutOctets_Type = Counter32
_NmslocIfspanOutOctets_Object = MibTableColumn
nmslocIfspanOutOctets = _NmslocIfspanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 105),
    _NmslocIfspanOutOctets_Type()
)
nmslocIfspanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfspanOutOctets.setStatus("mandatory")
_NmslocIfarpInPkts_Type = Counter32
_NmslocIfarpInPkts_Object = MibTableColumn
nmslocIfarpInPkts = _NmslocIfarpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 106),
    _NmslocIfarpInPkts_Type()
)
nmslocIfarpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfarpInPkts.setStatus("mandatory")
_NmslocIfarpOutPkts_Type = Counter32
_NmslocIfarpOutPkts_Object = MibTableColumn
nmslocIfarpOutPkts = _NmslocIfarpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 107),
    _NmslocIfarpOutPkts_Type()
)
nmslocIfarpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfarpOutPkts.setStatus("mandatory")
_NmslocIfarpInOctets_Type = Counter32
_NmslocIfarpInOctets_Object = MibTableColumn
nmslocIfarpInOctets = _NmslocIfarpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 108),
    _NmslocIfarpInOctets_Type()
)
nmslocIfarpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfarpInOctets.setStatus("mandatory")
_NmslocIfarpOutOctets_Type = Counter32
_NmslocIfarpOutOctets_Object = MibTableColumn
nmslocIfarpOutOctets = _NmslocIfarpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 109),
    _NmslocIfarpOutOctets_Type()
)
nmslocIfarpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfarpOutOctets.setStatus("mandatory")
_NmslocIfprobeInPkts_Type = Counter32
_NmslocIfprobeInPkts_Object = MibTableColumn
nmslocIfprobeInPkts = _NmslocIfprobeInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 110),
    _NmslocIfprobeInPkts_Type()
)
nmslocIfprobeInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfprobeInPkts.setStatus("mandatory")
_NmslocIfprobeOutPkts_Type = Counter32
_NmslocIfprobeOutPkts_Object = MibTableColumn
nmslocIfprobeOutPkts = _NmslocIfprobeOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 111),
    _NmslocIfprobeOutPkts_Type()
)
nmslocIfprobeOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfprobeOutPkts.setStatus("mandatory")
_NmslocIfprobeInOctets_Type = Counter32
_NmslocIfprobeInOctets_Object = MibTableColumn
nmslocIfprobeInOctets = _NmslocIfprobeInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 112),
    _NmslocIfprobeInOctets_Type()
)
nmslocIfprobeInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfprobeInOctets.setStatus("mandatory")
_NmslocIfprobeOutOctets_Type = Counter32
_NmslocIfprobeOutOctets_Object = MibTableColumn
nmslocIfprobeOutOctets = _NmslocIfprobeOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 113),
    _NmslocIfprobeOutOctets_Type()
)
nmslocIfprobeOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfprobeOutOctets.setStatus("mandatory")
_NmslocIfDribbleInputs_Type = Counter32
_NmslocIfDribbleInputs_Object = MibTableColumn
nmslocIfDribbleInputs = _NmslocIfDribbleInputs_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 1, 1, 114),
    _NmslocIfDribbleInputs_Type()
)
nmslocIfDribbleInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfDribbleInputs.setStatus("mandatory")
_NmslFSIPTable_Object = MibTable
nmslFSIPTable = _NmslFSIPTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2)
)
if mibBuilder.loadTexts:
    nmslFSIPTable.setStatus("mandatory")
_NmslFSIPEntry_Object = MibTableRow
nmslFSIPEntry = _NmslFSIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1)
)
nmslFSIPEntry.setIndexNames(
    (0, "NMS-INTERFACES", "nmslocIfFSIPIndex"),
)
if mibBuilder.loadTexts:
    nmslFSIPEntry.setStatus("mandatory")
_NmslocIfFSIPIndex_Type = Integer32
_NmslocIfFSIPIndex_Object = MibTableColumn
nmslocIfFSIPIndex = _NmslocIfFSIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1, 1),
    _NmslocIfFSIPIndex_Type()
)
nmslocIfFSIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFSIPIndex.setStatus("mandatory")


class _NmslocIfFSIPtype_Type(Integer32):
    """Custom type nmslocIfFSIPtype based on Integer32"""
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


_NmslocIfFSIPtype_Type.__name__ = "Integer32"
_NmslocIfFSIPtype_Object = MibTableColumn
nmslocIfFSIPtype = _NmslocIfFSIPtype_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1, 2),
    _NmslocIfFSIPtype_Type()
)
nmslocIfFSIPtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFSIPtype.setStatus("mandatory")


class _NmslocIfFSIPrts_Type(Integer32):
    """Custom type nmslocIfFSIPrts based on Integer32"""
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


_NmslocIfFSIPrts_Type.__name__ = "Integer32"
_NmslocIfFSIPrts_Object = MibTableColumn
nmslocIfFSIPrts = _NmslocIfFSIPrts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1, 3),
    _NmslocIfFSIPrts_Type()
)
nmslocIfFSIPrts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFSIPrts.setStatus("mandatory")


class _NmslocIfFSIPcts_Type(Integer32):
    """Custom type nmslocIfFSIPcts based on Integer32"""
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


_NmslocIfFSIPcts_Type.__name__ = "Integer32"
_NmslocIfFSIPcts_Object = MibTableColumn
nmslocIfFSIPcts = _NmslocIfFSIPcts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1, 4),
    _NmslocIfFSIPcts_Type()
)
nmslocIfFSIPcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFSIPcts.setStatus("mandatory")


class _NmslocIfFSIPdtr_Type(Integer32):
    """Custom type nmslocIfFSIPdtr based on Integer32"""
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


_NmslocIfFSIPdtr_Type.__name__ = "Integer32"
_NmslocIfFSIPdtr_Object = MibTableColumn
nmslocIfFSIPdtr = _NmslocIfFSIPdtr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1, 5),
    _NmslocIfFSIPdtr_Type()
)
nmslocIfFSIPdtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFSIPdtr.setStatus("mandatory")


class _NmslocIfFSIPdcd_Type(Integer32):
    """Custom type nmslocIfFSIPdcd based on Integer32"""
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


_NmslocIfFSIPdcd_Type.__name__ = "Integer32"
_NmslocIfFSIPdcd_Object = MibTableColumn
nmslocIfFSIPdcd = _NmslocIfFSIPdcd_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1, 6),
    _NmslocIfFSIPdcd_Type()
)
nmslocIfFSIPdcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFSIPdcd.setStatus("mandatory")


class _NmslocIfFSIPdsr_Type(Integer32):
    """Custom type nmslocIfFSIPdsr based on Integer32"""
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


_NmslocIfFSIPdsr_Type.__name__ = "Integer32"
_NmslocIfFSIPdsr_Object = MibTableColumn
nmslocIfFSIPdsr = _NmslocIfFSIPdsr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1, 7),
    _NmslocIfFSIPdsr_Type()
)
nmslocIfFSIPdsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFSIPdsr.setStatus("mandatory")
_NmslocIfFSIPrxClockrate_Type = Integer32
_NmslocIfFSIPrxClockrate_Object = MibTableColumn
nmslocIfFSIPrxClockrate = _NmslocIfFSIPrxClockrate_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1, 8),
    _NmslocIfFSIPrxClockrate_Type()
)
nmslocIfFSIPrxClockrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFSIPrxClockrate.setStatus("mandatory")
_NmslocIfFSIPrxClockrateHi_Type = Integer32
_NmslocIfFSIPrxClockrateHi_Object = MibTableColumn
nmslocIfFSIPrxClockrateHi = _NmslocIfFSIPrxClockrateHi_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1, 9),
    _NmslocIfFSIPrxClockrateHi_Type()
)
nmslocIfFSIPrxClockrateHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFSIPrxClockrateHi.setStatus("mandatory")


class _NmslocIfFSIPportType_Type(Integer32):
    """Custom type nmslocIfFSIPportType based on Integer32"""
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


_NmslocIfFSIPportType_Type.__name__ = "Integer32"
_NmslocIfFSIPportType_Object = MibTableColumn
nmslocIfFSIPportType = _NmslocIfFSIPportType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 2, 2, 1, 10),
    _NmslocIfFSIPportType_Type()
)
nmslocIfFSIPportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmslocIfFSIPportType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-INTERFACES",
    **{"nmslinterfaces": nmslinterfaces,
       "nmslifTable": nmslifTable,
       "nmslifEntry": nmslifEntry,
       "nmslocIfHardType": nmslocIfHardType,
       "nmslocIfLineProt": nmslocIfLineProt,
       "nmslocIfLastIn": nmslocIfLastIn,
       "nmslocIfLastOut": nmslocIfLastOut,
       "nmslocIfLastOutHang": nmslocIfLastOutHang,
       "nmslocIfInBitsSec": nmslocIfInBitsSec,
       "nmslocIfInPktsSec": nmslocIfInPktsSec,
       "nmslocIfOutBitsSec": nmslocIfOutBitsSec,
       "nmslocIfOutPktsSec": nmslocIfOutPktsSec,
       "nmslocIfInRunts": nmslocIfInRunts,
       "nmslocIfInGiants": nmslocIfInGiants,
       "nmslocIfInCRC": nmslocIfInCRC,
       "nmslocIfInFrame": nmslocIfInFrame,
       "nmslocIfInOverrun": nmslocIfInOverrun,
       "nmslocIfInIgnored": nmslocIfInIgnored,
       "nmslocIfInAbort": nmslocIfInAbort,
       "nmslocIfResets": nmslocIfResets,
       "nmslocIfRestarts": nmslocIfRestarts,
       "nmslocIfKeep": nmslocIfKeep,
       "nmslocIfReason": nmslocIfReason,
       "nmslocIfCarTrans": nmslocIfCarTrans,
       "nmslocIfReliab": nmslocIfReliab,
       "nmslocIfDelay": nmslocIfDelay,
       "nmslocIfLoad": nmslocIfLoad,
       "nmslocIfCollisions": nmslocIfCollisions,
       "nmslocIfInputQueueDrops": nmslocIfInputQueueDrops,
       "nmslocIfOutputQueueDrops": nmslocIfOutputQueueDrops,
       "nmslocIfDescr": nmslocIfDescr,
       "nmslocIfSlowInPkts": nmslocIfSlowInPkts,
       "nmslocIfSlowOutPkts": nmslocIfSlowOutPkts,
       "nmslocIfSlowInOctets": nmslocIfSlowInOctets,
       "nmslocIfSlowOutOctets": nmslocIfSlowOutOctets,
       "nmslocIfFastInPkts": nmslocIfFastInPkts,
       "nmslocIfFastOutPkts": nmslocIfFastOutPkts,
       "nmslocIfFastInOctets": nmslocIfFastInOctets,
       "nmslocIfFastOutOctets": nmslocIfFastOutOctets,
       "nmslocIfotherInPkts": nmslocIfotherInPkts,
       "nmslocIfotherOutPkts": nmslocIfotherOutPkts,
       "nmslocIfotherInOctets": nmslocIfotherInOctets,
       "nmslocIfotherOutOctets": nmslocIfotherOutOctets,
       "nmslocIfipInPkts": nmslocIfipInPkts,
       "nmslocIfipOutPkts": nmslocIfipOutPkts,
       "nmslocIfipInOctets": nmslocIfipInOctets,
       "nmslocIfipOutOctets": nmslocIfipOutOctets,
       "nmslocIfdecnetInPkts": nmslocIfdecnetInPkts,
       "nmslocIfdecnetOutPkts": nmslocIfdecnetOutPkts,
       "nmslocIfdecnetInOctets": nmslocIfdecnetInOctets,
       "nmslocIfdecnetOutOctets": nmslocIfdecnetOutOctets,
       "nmslocIfxnsInPkts": nmslocIfxnsInPkts,
       "nmslocIfxnsOutPkts": nmslocIfxnsOutPkts,
       "nmslocIfxnsInOctets": nmslocIfxnsInOctets,
       "nmslocIfxnsOutOctets": nmslocIfxnsOutOctets,
       "nmslocIfclnsInPkts": nmslocIfclnsInPkts,
       "nmslocIfclnsOutPkts": nmslocIfclnsOutPkts,
       "nmslocIfclnsInOctets": nmslocIfclnsInOctets,
       "nmslocIfclnsOutOctets": nmslocIfclnsOutOctets,
       "nmslocIfappletalkInPkts": nmslocIfappletalkInPkts,
       "nmslocIfappletalkOutPkts": nmslocIfappletalkOutPkts,
       "nmslocIfappletalkInOctets": nmslocIfappletalkInOctets,
       "nmslocIfappletalkOutOctets": nmslocIfappletalkOutOctets,
       "nmslocIfnovellInPkts": nmslocIfnovellInPkts,
       "nmslocIfnovellOutPkts": nmslocIfnovellOutPkts,
       "nmslocIfnovellInOctets": nmslocIfnovellInOctets,
       "nmslocIfnovellOutOctets": nmslocIfnovellOutOctets,
       "nmslocIfapolloInPkts": nmslocIfapolloInPkts,
       "nmslocIfapolloOutPkts": nmslocIfapolloOutPkts,
       "nmslocIfapolloInOctets": nmslocIfapolloInOctets,
       "nmslocIfapolloOutOctets": nmslocIfapolloOutOctets,
       "nmslocIfvinesInPkts": nmslocIfvinesInPkts,
       "nmslocIfvinesOutPkts": nmslocIfvinesOutPkts,
       "nmslocIfvinesInOctets": nmslocIfvinesInOctets,
       "nmslocIfvinesOutOctets": nmslocIfvinesOutOctets,
       "nmslocIfbridgedInPkts": nmslocIfbridgedInPkts,
       "nmslocIfbridgedOutPkts": nmslocIfbridgedOutPkts,
       "nmslocIfbridgedInOctets": nmslocIfbridgedInOctets,
       "nmslocIfbridgedOutOctets": nmslocIfbridgedOutOctets,
       "nmslocIfsrbInPkts": nmslocIfsrbInPkts,
       "nmslocIfsrbOutPkts": nmslocIfsrbOutPkts,
       "nmslocIfsrbInOctets": nmslocIfsrbInOctets,
       "nmslocIfsrbOutOctets": nmslocIfsrbOutOctets,
       "nmslocIfchaosInPkts": nmslocIfchaosInPkts,
       "nmslocIfchaosOutPkts": nmslocIfchaosOutPkts,
       "nmslocIfchaosInOctets": nmslocIfchaosInOctets,
       "nmslocIfchaosOutOctets": nmslocIfchaosOutOctets,
       "nmslocIfpupInPkts": nmslocIfpupInPkts,
       "nmslocIfpupOutPkts": nmslocIfpupOutPkts,
       "nmslocIfpupInOctets": nmslocIfpupInOctets,
       "nmslocIfpupOutOctets": nmslocIfpupOutOctets,
       "nmslocIfmopInPkts": nmslocIfmopInPkts,
       "nmslocIfmopOutPkts": nmslocIfmopOutPkts,
       "nmslocIfmopInOctets": nmslocIfmopInOctets,
       "nmslocIfmopOutOctets": nmslocIfmopOutOctets,
       "nmslocIflanmanInPkts": nmslocIflanmanInPkts,
       "nmslocIflanmanOutPkts": nmslocIflanmanOutPkts,
       "nmslocIflanmanInOctets": nmslocIflanmanInOctets,
       "nmslocIflanmanOutOctets": nmslocIflanmanOutOctets,
       "nmslocIfstunInPkts": nmslocIfstunInPkts,
       "nmslocIfstunOutPkts": nmslocIfstunOutPkts,
       "nmslocIfstunInOctets": nmslocIfstunInOctets,
       "nmslocIfstunOutOctets": nmslocIfstunOutOctets,
       "nmslocIfspanInPkts": nmslocIfspanInPkts,
       "nmslocIfspanOutPkts": nmslocIfspanOutPkts,
       "nmslocIfspanInOctets": nmslocIfspanInOctets,
       "nmslocIfspanOutOctets": nmslocIfspanOutOctets,
       "nmslocIfarpInPkts": nmslocIfarpInPkts,
       "nmslocIfarpOutPkts": nmslocIfarpOutPkts,
       "nmslocIfarpInOctets": nmslocIfarpInOctets,
       "nmslocIfarpOutOctets": nmslocIfarpOutOctets,
       "nmslocIfprobeInPkts": nmslocIfprobeInPkts,
       "nmslocIfprobeOutPkts": nmslocIfprobeOutPkts,
       "nmslocIfprobeInOctets": nmslocIfprobeInOctets,
       "nmslocIfprobeOutOctets": nmslocIfprobeOutOctets,
       "nmslocIfDribbleInputs": nmslocIfDribbleInputs,
       "nmslFSIPTable": nmslFSIPTable,
       "nmslFSIPEntry": nmslFSIPEntry,
       "nmslocIfFSIPIndex": nmslocIfFSIPIndex,
       "nmslocIfFSIPtype": nmslocIfFSIPtype,
       "nmslocIfFSIPrts": nmslocIfFSIPrts,
       "nmslocIfFSIPcts": nmslocIfFSIPcts,
       "nmslocIfFSIPdtr": nmslocIfFSIPdtr,
       "nmslocIfFSIPdcd": nmslocIfFSIPdcd,
       "nmslocIfFSIPdsr": nmslocIfFSIPdsr,
       "nmslocIfFSIPrxClockrate": nmslocIfFSIPrxClockrate,
       "nmslocIfFSIPrxClockrateHi": nmslocIfFSIPrxClockrateHi,
       "nmslocIfFSIPportType": nmslocIfFSIPportType}
)
