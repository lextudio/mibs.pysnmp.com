# SNMP MIB module (AT-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:34 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

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

swi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87)
)
swi.setRevisions(
        ("2006-06-12 12:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwiTrap_ObjectIdentity = ObjectIdentity
swiTrap = _SwiTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 0)
)
_SwiPortTable_Object = MibTable
swiPortTable = _SwiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1)
)
if mibBuilder.loadTexts:
    swiPortTable.setStatus("current")
_SwiPortEntry_Object = MibTableRow
swiPortEntry = _SwiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1)
)
swiPortEntry.setIndexNames(
    (0, "AT-SWITCH-MIB", "swiPortNumber"),
)
if mibBuilder.loadTexts:
    swiPortEntry.setStatus("current")
_SwiPortNumber_Type = Integer32
_SwiPortNumber_Object = MibTableColumn
swiPortNumber = _SwiPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 1),
    _SwiPortNumber_Type()
)
swiPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swiPortNumber.setStatus("current")
_SwiPortIngressLimit_Type = Integer32
_SwiPortIngressLimit_Object = MibTableColumn
swiPortIngressLimit = _SwiPortIngressLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 20),
    _SwiPortIngressLimit_Type()
)
swiPortIngressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swiPortIngressLimit.setStatus("current")
_SwiPortEgressLimit_Type = Integer32
_SwiPortEgressLimit_Object = MibTableColumn
swiPortEgressLimit = _SwiPortEgressLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 21),
    _SwiPortEgressLimit_Type()
)
swiPortEgressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swiPortEgressLimit.setStatus("current")
_Swi56xxPortCounterTable_Object = MibTable
swi56xxPortCounterTable = _Swi56xxPortCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2)
)
if mibBuilder.loadTexts:
    swi56xxPortCounterTable.setStatus("current")
_Swi56xxPortCounterEntry_Object = MibTableRow
swi56xxPortCounterEntry = _Swi56xxPortCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1)
)
swi56xxPortCounterEntry.setIndexNames(
    (0, "AT-SWITCH-MIB", "swi56xxPortNumber"),
)
if mibBuilder.loadTexts:
    swi56xxPortCounterEntry.setStatus("current")
_Swi56xxPortNumber_Type = Integer32
_Swi56xxPortNumber_Object = MibTableColumn
swi56xxPortNumber = _Swi56xxPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 1),
    _Swi56xxPortNumber_Type()
)
swi56xxPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortNumber.setStatus("current")
_Swi56xxRxTx64kPkts_Type = Counter32
_Swi56xxRxTx64kPkts_Object = MibTableColumn
swi56xxRxTx64kPkts = _Swi56xxRxTx64kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 2),
    _Swi56xxRxTx64kPkts_Type()
)
swi56xxRxTx64kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx64kPkts.setStatus("current")
_Swi56xxRxTx65To127kPkts_Type = Counter32
_Swi56xxRxTx65To127kPkts_Object = MibTableColumn
swi56xxRxTx65To127kPkts = _Swi56xxRxTx65To127kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 3),
    _Swi56xxRxTx65To127kPkts_Type()
)
swi56xxRxTx65To127kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx65To127kPkts.setStatus("current")
_Swi56xxRxTx128To255kPkts_Type = Counter32
_Swi56xxRxTx128To255kPkts_Object = MibTableColumn
swi56xxRxTx128To255kPkts = _Swi56xxRxTx128To255kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 4),
    _Swi56xxRxTx128To255kPkts_Type()
)
swi56xxRxTx128To255kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx128To255kPkts.setStatus("current")
_Swi56xxRxTx256To511kPkts_Type = Counter32
_Swi56xxRxTx256To511kPkts_Object = MibTableColumn
swi56xxRxTx256To511kPkts = _Swi56xxRxTx256To511kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 5),
    _Swi56xxRxTx256To511kPkts_Type()
)
swi56xxRxTx256To511kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx256To511kPkts.setStatus("current")
_Swi56xxRxTx512To1023kPkts_Type = Counter32
_Swi56xxRxTx512To1023kPkts_Object = MibTableColumn
swi56xxRxTx512To1023kPkts = _Swi56xxRxTx512To1023kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 6),
    _Swi56xxRxTx512To1023kPkts_Type()
)
swi56xxRxTx512To1023kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx512To1023kPkts.setStatus("current")
_Swi56xxRxTx1024ToMaxPktSzPkts_Type = Counter32
_Swi56xxRxTx1024ToMaxPktSzPkts_Object = MibTableColumn
swi56xxRxTx1024ToMaxPktSzPkts = _Swi56xxRxTx1024ToMaxPktSzPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 7),
    _Swi56xxRxTx1024ToMaxPktSzPkts_Type()
)
swi56xxRxTx1024ToMaxPktSzPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx1024ToMaxPktSzPkts.setStatus("current")
_Swi56xxRxTx519To1522kPkts_Type = Counter32
_Swi56xxRxTx519To1522kPkts_Object = MibTableColumn
swi56xxRxTx519To1522kPkts = _Swi56xxRxTx519To1522kPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 8),
    _Swi56xxRxTx519To1522kPkts_Type()
)
swi56xxRxTx519To1522kPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxRxTx519To1522kPkts.setStatus("current")
_Swi56xxPortRxOctets_Type = Counter32
_Swi56xxPortRxOctets_Object = MibTableColumn
swi56xxPortRxOctets = _Swi56xxPortRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 9),
    _Swi56xxPortRxOctets_Type()
)
swi56xxPortRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxOctets.setStatus("current")
_Swi56xxPortRxPkts_Type = Counter32
_Swi56xxPortRxPkts_Object = MibTableColumn
swi56xxPortRxPkts = _Swi56xxPortRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 10),
    _Swi56xxPortRxPkts_Type()
)
swi56xxPortRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxPkts.setStatus("current")
_Swi56xxPortRxFCSErrors_Type = Counter32
_Swi56xxPortRxFCSErrors_Object = MibTableColumn
swi56xxPortRxFCSErrors = _Swi56xxPortRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 11),
    _Swi56xxPortRxFCSErrors_Type()
)
swi56xxPortRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxFCSErrors.setStatus("current")
_Swi56xxPortRxMulticastPkts_Type = Counter32
_Swi56xxPortRxMulticastPkts_Object = MibTableColumn
swi56xxPortRxMulticastPkts = _Swi56xxPortRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 12),
    _Swi56xxPortRxMulticastPkts_Type()
)
swi56xxPortRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxMulticastPkts.setStatus("current")
_Swi56xxPortRxBroadcastPkts_Type = Counter32
_Swi56xxPortRxBroadcastPkts_Object = MibTableColumn
swi56xxPortRxBroadcastPkts = _Swi56xxPortRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 13),
    _Swi56xxPortRxBroadcastPkts_Type()
)
swi56xxPortRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxBroadcastPkts.setStatus("current")
_Swi56xxPortRxPauseMACCtlFrms_Type = Counter32
_Swi56xxPortRxPauseMACCtlFrms_Object = MibTableColumn
swi56xxPortRxPauseMACCtlFrms = _Swi56xxPortRxPauseMACCtlFrms_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 14),
    _Swi56xxPortRxPauseMACCtlFrms_Type()
)
swi56xxPortRxPauseMACCtlFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxPauseMACCtlFrms.setStatus("current")
_Swi56xxPortRxOversizePkts_Type = Counter32
_Swi56xxPortRxOversizePkts_Object = MibTableColumn
swi56xxPortRxOversizePkts = _Swi56xxPortRxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 15),
    _Swi56xxPortRxOversizePkts_Type()
)
swi56xxPortRxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxOversizePkts.setStatus("current")
_Swi56xxPortRxFragments_Type = Counter32
_Swi56xxPortRxFragments_Object = MibTableColumn
swi56xxPortRxFragments = _Swi56xxPortRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 16),
    _Swi56xxPortRxFragments_Type()
)
swi56xxPortRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxFragments.setStatus("current")
_Swi56xxPortRxJabbers_Type = Counter32
_Swi56xxPortRxJabbers_Object = MibTableColumn
swi56xxPortRxJabbers = _Swi56xxPortRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 17),
    _Swi56xxPortRxJabbers_Type()
)
swi56xxPortRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxJabbers.setStatus("current")
_Swi56xxPortRxMACControlFrms_Type = Counter32
_Swi56xxPortRxMACControlFrms_Object = MibTableColumn
swi56xxPortRxMACControlFrms = _Swi56xxPortRxMACControlFrms_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 18),
    _Swi56xxPortRxMACControlFrms_Type()
)
swi56xxPortRxMACControlFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxMACControlFrms.setStatus("current")
_Swi56xxPortRxUnsupportOpcode_Type = Counter32
_Swi56xxPortRxUnsupportOpcode_Object = MibTableColumn
swi56xxPortRxUnsupportOpcode = _Swi56xxPortRxUnsupportOpcode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 19),
    _Swi56xxPortRxUnsupportOpcode_Type()
)
swi56xxPortRxUnsupportOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxUnsupportOpcode.setStatus("current")
_Swi56xxPortRxAlignmentErrors_Type = Counter32
_Swi56xxPortRxAlignmentErrors_Object = MibTableColumn
swi56xxPortRxAlignmentErrors = _Swi56xxPortRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 20),
    _Swi56xxPortRxAlignmentErrors_Type()
)
swi56xxPortRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxAlignmentErrors.setStatus("current")
_Swi56xxPortRxOutOfRngeLenFld_Type = Counter32
_Swi56xxPortRxOutOfRngeLenFld_Object = MibTableColumn
swi56xxPortRxOutOfRngeLenFld = _Swi56xxPortRxOutOfRngeLenFld_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 21),
    _Swi56xxPortRxOutOfRngeLenFld_Type()
)
swi56xxPortRxOutOfRngeLenFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxOutOfRngeLenFld.setStatus("current")
_Swi56xxPortRxSymErDurCarrier_Type = Counter32
_Swi56xxPortRxSymErDurCarrier_Object = MibTableColumn
swi56xxPortRxSymErDurCarrier = _Swi56xxPortRxSymErDurCarrier_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 22),
    _Swi56xxPortRxSymErDurCarrier_Type()
)
swi56xxPortRxSymErDurCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxSymErDurCarrier.setStatus("current")
_Swi56xxPortRxCarrierSenseErr_Type = Counter32
_Swi56xxPortRxCarrierSenseErr_Object = MibTableColumn
swi56xxPortRxCarrierSenseErr = _Swi56xxPortRxCarrierSenseErr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 23),
    _Swi56xxPortRxCarrierSenseErr_Type()
)
swi56xxPortRxCarrierSenseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxCarrierSenseErr.setStatus("current")
_Swi56xxPortRxUndersizePkts_Type = Counter32
_Swi56xxPortRxUndersizePkts_Object = MibTableColumn
swi56xxPortRxUndersizePkts = _Swi56xxPortRxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 24),
    _Swi56xxPortRxUndersizePkts_Type()
)
swi56xxPortRxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxUndersizePkts.setStatus("current")
_Swi56xxPortRxIpInHdrErrors_Type = Counter32
_Swi56xxPortRxIpInHdrErrors_Object = MibTableColumn
swi56xxPortRxIpInHdrErrors = _Swi56xxPortRxIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 25),
    _Swi56xxPortRxIpInHdrErrors_Type()
)
swi56xxPortRxIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortRxIpInHdrErrors.setStatus("current")
_Swi56xxPortTxOctets_Type = Counter32
_Swi56xxPortTxOctets_Object = MibTableColumn
swi56xxPortTxOctets = _Swi56xxPortTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 26),
    _Swi56xxPortTxOctets_Type()
)
swi56xxPortTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxOctets.setStatus("current")
_Swi56xxPortTxPkts_Type = Counter32
_Swi56xxPortTxPkts_Object = MibTableColumn
swi56xxPortTxPkts = _Swi56xxPortTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 27),
    _Swi56xxPortTxPkts_Type()
)
swi56xxPortTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxPkts.setStatus("current")
_Swi56xxPortTxFCSErrors_Type = Counter32
_Swi56xxPortTxFCSErrors_Object = MibTableColumn
swi56xxPortTxFCSErrors = _Swi56xxPortTxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 28),
    _Swi56xxPortTxFCSErrors_Type()
)
swi56xxPortTxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxFCSErrors.setStatus("current")
_Swi56xxPortTxMulticastPkts_Type = Counter32
_Swi56xxPortTxMulticastPkts_Object = MibTableColumn
swi56xxPortTxMulticastPkts = _Swi56xxPortTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 29),
    _Swi56xxPortTxMulticastPkts_Type()
)
swi56xxPortTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxMulticastPkts.setStatus("current")
_Swi56xxPortTxBroadcastPkts_Type = Counter32
_Swi56xxPortTxBroadcastPkts_Object = MibTableColumn
swi56xxPortTxBroadcastPkts = _Swi56xxPortTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 30),
    _Swi56xxPortTxBroadcastPkts_Type()
)
swi56xxPortTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxBroadcastPkts.setStatus("current")
_Swi56xxPortTxPauseMACCtlFrms_Type = Counter32
_Swi56xxPortTxPauseMACCtlFrms_Object = MibTableColumn
swi56xxPortTxPauseMACCtlFrms = _Swi56xxPortTxPauseMACCtlFrms_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 31),
    _Swi56xxPortTxPauseMACCtlFrms_Type()
)
swi56xxPortTxPauseMACCtlFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxPauseMACCtlFrms.setStatus("current")
_Swi56xxPortTxOversizePkts_Type = Counter32
_Swi56xxPortTxOversizePkts_Object = MibTableColumn
swi56xxPortTxOversizePkts = _Swi56xxPortTxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 32),
    _Swi56xxPortTxOversizePkts_Type()
)
swi56xxPortTxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxOversizePkts.setStatus("current")
_Swi56xxPortTxFragments_Type = Counter32
_Swi56xxPortTxFragments_Object = MibTableColumn
swi56xxPortTxFragments = _Swi56xxPortTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 33),
    _Swi56xxPortTxFragments_Type()
)
swi56xxPortTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxFragments.setStatus("current")
_Swi56xxPortTxJabbers_Type = Counter32
_Swi56xxPortTxJabbers_Object = MibTableColumn
swi56xxPortTxJabbers = _Swi56xxPortTxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 34),
    _Swi56xxPortTxJabbers_Type()
)
swi56xxPortTxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxJabbers.setStatus("current")
_Swi56xxPortTxPauseCtrlFrms_Type = Counter32
_Swi56xxPortTxPauseCtrlFrms_Object = MibTableColumn
swi56xxPortTxPauseCtrlFrms = _Swi56xxPortTxPauseCtrlFrms_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 35),
    _Swi56xxPortTxPauseCtrlFrms_Type()
)
swi56xxPortTxPauseCtrlFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxPauseCtrlFrms.setStatus("current")
_Swi56xxPortTxFrameWDeferrdTx_Type = Counter32
_Swi56xxPortTxFrameWDeferrdTx_Object = MibTableColumn
swi56xxPortTxFrameWDeferrdTx = _Swi56xxPortTxFrameWDeferrdTx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 36),
    _Swi56xxPortTxFrameWDeferrdTx_Type()
)
swi56xxPortTxFrameWDeferrdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxFrameWDeferrdTx.setStatus("current")
_Swi56xxPortTxFrmWExcesDefer_Type = Counter32
_Swi56xxPortTxFrmWExcesDefer_Object = MibTableColumn
swi56xxPortTxFrmWExcesDefer = _Swi56xxPortTxFrmWExcesDefer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 37),
    _Swi56xxPortTxFrmWExcesDefer_Type()
)
swi56xxPortTxFrmWExcesDefer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxFrmWExcesDefer.setStatus("current")
_Swi56xxPortTxSingleCollsnFrm_Type = Counter32
_Swi56xxPortTxSingleCollsnFrm_Object = MibTableColumn
swi56xxPortTxSingleCollsnFrm = _Swi56xxPortTxSingleCollsnFrm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 38),
    _Swi56xxPortTxSingleCollsnFrm_Type()
)
swi56xxPortTxSingleCollsnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxSingleCollsnFrm.setStatus("current")
_Swi56xxPortTxMultCollsnFrm_Type = Counter32
_Swi56xxPortTxMultCollsnFrm_Object = MibTableColumn
swi56xxPortTxMultCollsnFrm = _Swi56xxPortTxMultCollsnFrm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 39),
    _Swi56xxPortTxMultCollsnFrm_Type()
)
swi56xxPortTxMultCollsnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxMultCollsnFrm.setStatus("current")
_Swi56xxPortTxLateCollsns_Type = Counter32
_Swi56xxPortTxLateCollsns_Object = MibTableColumn
swi56xxPortTxLateCollsns = _Swi56xxPortTxLateCollsns_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 40),
    _Swi56xxPortTxLateCollsns_Type()
)
swi56xxPortTxLateCollsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxLateCollsns.setStatus("current")
_Swi56xxPortTxExcessivCollsns_Type = Counter32
_Swi56xxPortTxExcessivCollsns_Object = MibTableColumn
swi56xxPortTxExcessivCollsns = _Swi56xxPortTxExcessivCollsns_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 41),
    _Swi56xxPortTxExcessivCollsns_Type()
)
swi56xxPortTxExcessivCollsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxExcessivCollsns.setStatus("current")
_Swi56xxPortTxCollisionFrames_Type = Counter32
_Swi56xxPortTxCollisionFrames_Object = MibTableColumn
swi56xxPortTxCollisionFrames = _Swi56xxPortTxCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 42),
    _Swi56xxPortTxCollisionFrames_Type()
)
swi56xxPortTxCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortTxCollisionFrames.setStatus("current")
_Swi56xxPortMiscDropEvents_Type = Counter32
_Swi56xxPortMiscDropEvents_Object = MibTableColumn
swi56xxPortMiscDropEvents = _Swi56xxPortMiscDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 43),
    _Swi56xxPortMiscDropEvents_Type()
)
swi56xxPortMiscDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortMiscDropEvents.setStatus("current")
_Swi56xxPortMiscTaggedPktTx_Type = Counter32
_Swi56xxPortMiscTaggedPktTx_Object = MibTableColumn
swi56xxPortMiscTaggedPktTx = _Swi56xxPortMiscTaggedPktTx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 44),
    _Swi56xxPortMiscTaggedPktTx_Type()
)
swi56xxPortMiscTaggedPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortMiscTaggedPktTx.setStatus("current")
_Swi56xxPortMiscTotalPktTxAbort_Type = Counter32
_Swi56xxPortMiscTotalPktTxAbort_Object = MibTableColumn
swi56xxPortMiscTotalPktTxAbort = _Swi56xxPortMiscTotalPktTxAbort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 45),
    _Swi56xxPortMiscTotalPktTxAbort_Type()
)
swi56xxPortMiscTotalPktTxAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortMiscTotalPktTxAbort.setStatus("current")
_Swi56xxPortHWMultiTTLexpired_Type = Counter32
_Swi56xxPortHWMultiTTLexpired_Object = MibTableColumn
swi56xxPortHWMultiTTLexpired = _Swi56xxPortHWMultiTTLexpired_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 46),
    _Swi56xxPortHWMultiTTLexpired_Type()
)
swi56xxPortHWMultiTTLexpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortHWMultiTTLexpired.setStatus("current")
_Swi56xxPortHWMultiBridgedFrames_Type = Counter32
_Swi56xxPortHWMultiBridgedFrames_Object = MibTableColumn
swi56xxPortHWMultiBridgedFrames = _Swi56xxPortHWMultiBridgedFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 47),
    _Swi56xxPortHWMultiBridgedFrames_Type()
)
swi56xxPortHWMultiBridgedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortHWMultiBridgedFrames.setStatus("current")
_Swi56xxPortHWMultiRxDrops_Type = Counter32
_Swi56xxPortHWMultiRxDrops_Object = MibTableColumn
swi56xxPortHWMultiRxDrops = _Swi56xxPortHWMultiRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 48),
    _Swi56xxPortHWMultiRxDrops_Type()
)
swi56xxPortHWMultiRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortHWMultiRxDrops.setStatus("current")
_Swi56xxPortHWMultiTxDrops_Type = Counter32
_Swi56xxPortHWMultiTxDrops_Object = MibTableColumn
swi56xxPortHWMultiTxDrops = _Swi56xxPortHWMultiTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 49),
    _Swi56xxPortHWMultiTxDrops_Type()
)
swi56xxPortHWMultiTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swi56xxPortHWMultiTxDrops.setStatus("current")
_SwiDebugVariables_ObjectIdentity = ObjectIdentity
swiDebugVariables = _SwiDebugVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 3)
)
_SwiDebugMemoryParityErrors_Type = Counter32
_SwiDebugMemoryParityErrors_Object = MibScalar
swiDebugMemoryParityErrors = _SwiDebugMemoryParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 3, 1),
    _SwiDebugMemoryParityErrors_Type()
)
swiDebugMemoryParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swiDebugMemoryParityErrors.setStatus("current")
_SwiPortVlanTable_Object = MibTable
swiPortVlanTable = _SwiPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4)
)
if mibBuilder.loadTexts:
    swiPortVlanTable.setStatus("current")
_SwiPortVlanEntry_Object = MibTableRow
swiPortVlanEntry = _SwiPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1)
)
swiPortVlanEntry.setIndexNames(
    (0, "AT-SWITCH-MIB", "swiPortVlanPortNumber"),
    (0, "AT-SWITCH-MIB", "swiPortVlanVlanId"),
)
if mibBuilder.loadTexts:
    swiPortVlanEntry.setStatus("current")
_SwiPortVlanPortNumber_Type = Integer32
_SwiPortVlanPortNumber_Object = MibTableColumn
swiPortVlanPortNumber = _SwiPortVlanPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1, 1),
    _SwiPortVlanPortNumber_Type()
)
swiPortVlanPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swiPortVlanPortNumber.setStatus("current")
_SwiPortVlanVlanId_Type = Integer32
_SwiPortVlanVlanId_Object = MibTableColumn
swiPortVlanVlanId = _SwiPortVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1, 2),
    _SwiPortVlanVlanId_Type()
)
swiPortVlanVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swiPortVlanVlanId.setStatus("current")


class _SwiPortVlanControl_Type(Integer32):
    """Custom type swiPortVlanControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SwiPortVlanControl_Type.__name__ = "Integer32"
_SwiPortVlanControl_Object = MibTableColumn
swiPortVlanControl = _SwiPortVlanControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1, 3),
    _SwiPortVlanControl_Type()
)
swiPortVlanControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swiPortVlanControl.setStatus("current")

# Managed Objects groups


# Notification objects

swiIntrusionDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 0, 6)
)
swiIntrusionDetectionTrap.setObjects(
    ("AT-SWITCH-MIB", "swiPortNumber")
)
if mibBuilder.loadTexts:
    swiIntrusionDetectionTrap.setStatus(
        "current"
    )

swiPortVlanStateNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 9)
)
swiPortVlanStateNotify.setObjects(
      *(("AT-SWITCH-MIB", "swiPortVlanPortNumber"),
        ("AT-SWITCH-MIB", "swiPortVlanVlanId"),
        ("AT-SWITCH-MIB", "swiPortVlanControl"))
)
if mibBuilder.loadTexts:
    swiPortVlanStateNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-SWITCH-MIB",
    **{"swi": swi,
       "swiTrap": swiTrap,
       "swiIntrusionDetectionTrap": swiIntrusionDetectionTrap,
       "swiPortTable": swiPortTable,
       "swiPortEntry": swiPortEntry,
       "swiPortNumber": swiPortNumber,
       "swiPortIngressLimit": swiPortIngressLimit,
       "swiPortEgressLimit": swiPortEgressLimit,
       "swi56xxPortCounterTable": swi56xxPortCounterTable,
       "swi56xxPortCounterEntry": swi56xxPortCounterEntry,
       "swi56xxPortNumber": swi56xxPortNumber,
       "swi56xxRxTx64kPkts": swi56xxRxTx64kPkts,
       "swi56xxRxTx65To127kPkts": swi56xxRxTx65To127kPkts,
       "swi56xxRxTx128To255kPkts": swi56xxRxTx128To255kPkts,
       "swi56xxRxTx256To511kPkts": swi56xxRxTx256To511kPkts,
       "swi56xxRxTx512To1023kPkts": swi56xxRxTx512To1023kPkts,
       "swi56xxRxTx1024ToMaxPktSzPkts": swi56xxRxTx1024ToMaxPktSzPkts,
       "swi56xxRxTx519To1522kPkts": swi56xxRxTx519To1522kPkts,
       "swi56xxPortRxOctets": swi56xxPortRxOctets,
       "swi56xxPortRxPkts": swi56xxPortRxPkts,
       "swi56xxPortRxFCSErrors": swi56xxPortRxFCSErrors,
       "swi56xxPortRxMulticastPkts": swi56xxPortRxMulticastPkts,
       "swi56xxPortRxBroadcastPkts": swi56xxPortRxBroadcastPkts,
       "swi56xxPortRxPauseMACCtlFrms": swi56xxPortRxPauseMACCtlFrms,
       "swi56xxPortRxOversizePkts": swi56xxPortRxOversizePkts,
       "swi56xxPortRxFragments": swi56xxPortRxFragments,
       "swi56xxPortRxJabbers": swi56xxPortRxJabbers,
       "swi56xxPortRxMACControlFrms": swi56xxPortRxMACControlFrms,
       "swi56xxPortRxUnsupportOpcode": swi56xxPortRxUnsupportOpcode,
       "swi56xxPortRxAlignmentErrors": swi56xxPortRxAlignmentErrors,
       "swi56xxPortRxOutOfRngeLenFld": swi56xxPortRxOutOfRngeLenFld,
       "swi56xxPortRxSymErDurCarrier": swi56xxPortRxSymErDurCarrier,
       "swi56xxPortRxCarrierSenseErr": swi56xxPortRxCarrierSenseErr,
       "swi56xxPortRxUndersizePkts": swi56xxPortRxUndersizePkts,
       "swi56xxPortRxIpInHdrErrors": swi56xxPortRxIpInHdrErrors,
       "swi56xxPortTxOctets": swi56xxPortTxOctets,
       "swi56xxPortTxPkts": swi56xxPortTxPkts,
       "swi56xxPortTxFCSErrors": swi56xxPortTxFCSErrors,
       "swi56xxPortTxMulticastPkts": swi56xxPortTxMulticastPkts,
       "swi56xxPortTxBroadcastPkts": swi56xxPortTxBroadcastPkts,
       "swi56xxPortTxPauseMACCtlFrms": swi56xxPortTxPauseMACCtlFrms,
       "swi56xxPortTxOversizePkts": swi56xxPortTxOversizePkts,
       "swi56xxPortTxFragments": swi56xxPortTxFragments,
       "swi56xxPortTxJabbers": swi56xxPortTxJabbers,
       "swi56xxPortTxPauseCtrlFrms": swi56xxPortTxPauseCtrlFrms,
       "swi56xxPortTxFrameWDeferrdTx": swi56xxPortTxFrameWDeferrdTx,
       "swi56xxPortTxFrmWExcesDefer": swi56xxPortTxFrmWExcesDefer,
       "swi56xxPortTxSingleCollsnFrm": swi56xxPortTxSingleCollsnFrm,
       "swi56xxPortTxMultCollsnFrm": swi56xxPortTxMultCollsnFrm,
       "swi56xxPortTxLateCollsns": swi56xxPortTxLateCollsns,
       "swi56xxPortTxExcessivCollsns": swi56xxPortTxExcessivCollsns,
       "swi56xxPortTxCollisionFrames": swi56xxPortTxCollisionFrames,
       "swi56xxPortMiscDropEvents": swi56xxPortMiscDropEvents,
       "swi56xxPortMiscTaggedPktTx": swi56xxPortMiscTaggedPktTx,
       "swi56xxPortMiscTotalPktTxAbort": swi56xxPortMiscTotalPktTxAbort,
       "swi56xxPortHWMultiTTLexpired": swi56xxPortHWMultiTTLexpired,
       "swi56xxPortHWMultiBridgedFrames": swi56xxPortHWMultiBridgedFrames,
       "swi56xxPortHWMultiRxDrops": swi56xxPortHWMultiRxDrops,
       "swi56xxPortHWMultiTxDrops": swi56xxPortHWMultiTxDrops,
       "swiDebugVariables": swiDebugVariables,
       "swiDebugMemoryParityErrors": swiDebugMemoryParityErrors,
       "swiPortVlanTable": swiPortVlanTable,
       "swiPortVlanEntry": swiPortVlanEntry,
       "swiPortVlanPortNumber": swiPortVlanPortNumber,
       "swiPortVlanVlanId": swiPortVlanVlanId,
       "swiPortVlanControl": swiPortVlanControl,
       "swiPortVlanStateNotify": swiPortVlanStateNotify}
)
