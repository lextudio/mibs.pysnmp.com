# SNMP MIB module (CISCO-SECY-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SECY-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:04 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(secyIfInterfaceIndex,) = mibBuilder.importSymbols(
    "IEEE8021-SECY-MIB",
    "secyIfInterfaceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoSecyExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 835)
)
ciscoSecyExtMIB.setRevisions(
        ("2016-12-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSecyExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSecyExtMIBNotifs = _CiscoSecyExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 0)
)
_CiscoSecyExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSecyExtMIBObjects = _CiscoSecyExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1)
)
_CiscoSecyExtMIBStatsObjects_ObjectIdentity = ObjectIdentity
ciscoSecyExtMIBStatsObjects = _CiscoSecyExtMIBStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1)
)
_CseSecyStatsExtTable_Object = MibTable
cseSecyStatsExtTable = _CseSecyStatsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cseSecyStatsExtTable.setStatus("current")
_CseSecyStatsExtEntry_Object = MibTableRow
cseSecyStatsExtEntry = _CseSecyStatsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1)
)
cseSecyStatsExtEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cseSecyStatsExtEntry.setStatus("current")
_CseSecyStatsRxTransformErrPkts_Type = Counter64
_CseSecyStatsRxTransformErrPkts_Object = MibTableColumn
cseSecyStatsRxTransformErrPkts = _CseSecyStatsRxTransformErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1, 1),
    _CseSecyStatsRxTransformErrPkts_Type()
)
cseSecyStatsRxTransformErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyStatsRxTransformErrPkts.setStatus("current")
_CseSecyStatsRxControlPkts_Type = Counter64
_CseSecyStatsRxControlPkts_Object = MibTableColumn
cseSecyStatsRxControlPkts = _CseSecyStatsRxControlPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1, 2),
    _CseSecyStatsRxControlPkts_Type()
)
cseSecyStatsRxControlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyStatsRxControlPkts.setStatus("current")
_CseSecyStatsRxTaggedCtrlPkts_Type = Counter64
_CseSecyStatsRxTaggedCtrlPkts_Object = MibTableColumn
cseSecyStatsRxTaggedCtrlPkts = _CseSecyStatsRxTaggedCtrlPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1, 3),
    _CseSecyStatsRxTaggedCtrlPkts_Type()
)
cseSecyStatsRxTaggedCtrlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyStatsRxTaggedCtrlPkts.setStatus("current")
_CseSecyStatsTxTransformErrPkts_Type = Counter64
_CseSecyStatsTxTransformErrPkts_Object = MibTableColumn
cseSecyStatsTxTransformErrPkts = _CseSecyStatsTxTransformErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1, 4),
    _CseSecyStatsTxTransformErrPkts_Type()
)
cseSecyStatsTxTransformErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyStatsTxTransformErrPkts.setStatus("current")
_CseSecyStatsTxControlPkts_Type = Counter64
_CseSecyStatsTxControlPkts_Object = MibTableColumn
cseSecyStatsTxControlPkts = _CseSecyStatsTxControlPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 1, 1, 5),
    _CseSecyStatsTxControlPkts_Type()
)
cseSecyStatsTxControlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyStatsTxControlPkts.setStatus("current")
_CseSecyTxSCStatsExtTable_Object = MibTable
cseSecyTxSCStatsExtTable = _CseSecyTxSCStatsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cseSecyTxSCStatsExtTable.setStatus("current")
_CseSecyTxSCStatsExtEntry_Object = MibTableRow
cseSecyTxSCStatsExtEntry = _CseSecyTxSCStatsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 2, 1)
)
cseSecyTxSCStatsExtEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cseSecyTxSCStatsExtEntry.setStatus("current")
_CseSecyTxSCStatsSANotInUse_Type = Counter64
_CseSecyTxSCStatsSANotInUse_Object = MibTableColumn
cseSecyTxSCStatsSANotInUse = _CseSecyTxSCStatsSANotInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 2, 1, 1),
    _CseSecyTxSCStatsSANotInUse_Type()
)
cseSecyTxSCStatsSANotInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyTxSCStatsSANotInUse.setStatus("current")
_CseSecyIfRxStatsTable_Object = MibTable
cseSecyIfRxStatsTable = _CseSecyIfRxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cseSecyIfRxStatsTable.setStatus("current")
_CseSecyIfRxStatsEntry_Object = MibTableRow
cseSecyIfRxStatsEntry = _CseSecyIfRxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1)
)
cseSecyIfRxStatsEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cseSecyIfRxStatsEntry.setStatus("current")
_CseSecyIfRxUnicastUncontrolledPkts_Type = Counter64
_CseSecyIfRxUnicastUncontrolledPkts_Object = MibTableColumn
cseSecyIfRxUnicastUncontrolledPkts = _CseSecyIfRxUnicastUncontrolledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 1),
    _CseSecyIfRxUnicastUncontrolledPkts_Type()
)
cseSecyIfRxUnicastUncontrolledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxUnicastUncontrolledPkts.setStatus("current")
_CseSecyIfRxMulticastUncontrolledPkts_Type = Counter64
_CseSecyIfRxMulticastUncontrolledPkts_Object = MibTableColumn
cseSecyIfRxMulticastUncontrolledPkts = _CseSecyIfRxMulticastUncontrolledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 2),
    _CseSecyIfRxMulticastUncontrolledPkts_Type()
)
cseSecyIfRxMulticastUncontrolledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxMulticastUncontrolledPkts.setStatus("current")
_CseSecyIfRxBroadcastUncontrolledPkts_Type = Counter64
_CseSecyIfRxBroadcastUncontrolledPkts_Object = MibTableColumn
cseSecyIfRxBroadcastUncontrolledPkts = _CseSecyIfRxBroadcastUncontrolledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 3),
    _CseSecyIfRxBroadcastUncontrolledPkts_Type()
)
cseSecyIfRxBroadcastUncontrolledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxBroadcastUncontrolledPkts.setStatus("current")
_CseSecyIfRxUncontrolledPktsDrop_Type = Counter64
_CseSecyIfRxUncontrolledPktsDrop_Object = MibTableColumn
cseSecyIfRxUncontrolledPktsDrop = _CseSecyIfRxUncontrolledPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 4),
    _CseSecyIfRxUncontrolledPktsDrop_Type()
)
cseSecyIfRxUncontrolledPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxUncontrolledPktsDrop.setStatus("current")
_CseSecyIfRxUncontrolledPktsError_Type = Counter64
_CseSecyIfRxUncontrolledPktsError_Object = MibTableColumn
cseSecyIfRxUncontrolledPktsError = _CseSecyIfRxUncontrolledPktsError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 5),
    _CseSecyIfRxUncontrolledPktsError_Type()
)
cseSecyIfRxUncontrolledPktsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxUncontrolledPktsError.setStatus("current")
_CseSecyIfRxUnicastControlledPkts_Type = Counter64
_CseSecyIfRxUnicastControlledPkts_Object = MibTableColumn
cseSecyIfRxUnicastControlledPkts = _CseSecyIfRxUnicastControlledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 6),
    _CseSecyIfRxUnicastControlledPkts_Type()
)
cseSecyIfRxUnicastControlledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxUnicastControlledPkts.setStatus("current")
_CseSecyIfRxMulticastControlledPkts_Type = Counter64
_CseSecyIfRxMulticastControlledPkts_Object = MibTableColumn
cseSecyIfRxMulticastControlledPkts = _CseSecyIfRxMulticastControlledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 7),
    _CseSecyIfRxMulticastControlledPkts_Type()
)
cseSecyIfRxMulticastControlledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxMulticastControlledPkts.setStatus("current")
_CseSecyIfRxBroadcastControlledPkts_Type = Counter64
_CseSecyIfRxBroadcastControlledPkts_Object = MibTableColumn
cseSecyIfRxBroadcastControlledPkts = _CseSecyIfRxBroadcastControlledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 8),
    _CseSecyIfRxBroadcastControlledPkts_Type()
)
cseSecyIfRxBroadcastControlledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxBroadcastControlledPkts.setStatus("current")
_CseSecyIfRxControlledPktsDrop_Type = Counter64
_CseSecyIfRxControlledPktsDrop_Object = MibTableColumn
cseSecyIfRxControlledPktsDrop = _CseSecyIfRxControlledPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 9),
    _CseSecyIfRxControlledPktsDrop_Type()
)
cseSecyIfRxControlledPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxControlledPktsDrop.setStatus("current")
_CseSecyIfRxControlledPktsError_Type = Counter64
_CseSecyIfRxControlledPktsError_Object = MibTableColumn
cseSecyIfRxControlledPktsError = _CseSecyIfRxControlledPktsError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 10),
    _CseSecyIfRxControlledPktsError_Type()
)
cseSecyIfRxControlledPktsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxControlledPktsError.setStatus("current")
_CseSecyIfRxUncontrolledOctets_Type = Counter64
_CseSecyIfRxUncontrolledOctets_Object = MibTableColumn
cseSecyIfRxUncontrolledOctets = _CseSecyIfRxUncontrolledOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 11),
    _CseSecyIfRxUncontrolledOctets_Type()
)
cseSecyIfRxUncontrolledOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxUncontrolledOctets.setStatus("current")
_CseSecyIfRxControlledOctets_Type = Counter64
_CseSecyIfRxControlledOctets_Object = MibTableColumn
cseSecyIfRxControlledOctets = _CseSecyIfRxControlledOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 12),
    _CseSecyIfRxControlledOctets_Type()
)
cseSecyIfRxControlledOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxControlledOctets.setStatus("current")
_CseSecyIfRxUncontrolledPktRate_Type = CounterBasedGauge64
_CseSecyIfRxUncontrolledPktRate_Object = MibTableColumn
cseSecyIfRxUncontrolledPktRate = _CseSecyIfRxUncontrolledPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 13),
    _CseSecyIfRxUncontrolledPktRate_Type()
)
cseSecyIfRxUncontrolledPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxUncontrolledPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cseSecyIfRxUncontrolledPktRate.setUnits("Packets per second")
_CseSecyIfRxUncontrolledOctetRate_Type = CounterBasedGauge64
_CseSecyIfRxUncontrolledOctetRate_Object = MibTableColumn
cseSecyIfRxUncontrolledOctetRate = _CseSecyIfRxUncontrolledOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 14),
    _CseSecyIfRxUncontrolledOctetRate_Type()
)
cseSecyIfRxUncontrolledOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxUncontrolledOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    cseSecyIfRxUncontrolledOctetRate.setUnits("Bytes per second")
_CseSecyIfRxControlledPktRate_Type = CounterBasedGauge64
_CseSecyIfRxControlledPktRate_Object = MibTableColumn
cseSecyIfRxControlledPktRate = _CseSecyIfRxControlledPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 15),
    _CseSecyIfRxControlledPktRate_Type()
)
cseSecyIfRxControlledPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxControlledPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cseSecyIfRxControlledPktRate.setUnits("Packets per second")
_CseSecyIfRxControlledOctetRate_Type = CounterBasedGauge64
_CseSecyIfRxControlledOctetRate_Object = MibTableColumn
cseSecyIfRxControlledOctetRate = _CseSecyIfRxControlledOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 3, 1, 16),
    _CseSecyIfRxControlledOctetRate_Type()
)
cseSecyIfRxControlledOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfRxControlledOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    cseSecyIfRxControlledOctetRate.setUnits("Bytes per second")
_CseSecyIfTxStatsTable_Object = MibTable
cseSecyIfTxStatsTable = _CseSecyIfTxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cseSecyIfTxStatsTable.setStatus("current")
_CseSecyIfTxStatsEntry_Object = MibTableRow
cseSecyIfTxStatsEntry = _CseSecyIfTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1)
)
cseSecyIfTxStatsEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cseSecyIfTxStatsEntry.setStatus("current")
_CseSecyIfTxUnicastUncontrolledPkts_Type = Counter64
_CseSecyIfTxUnicastUncontrolledPkts_Object = MibTableColumn
cseSecyIfTxUnicastUncontrolledPkts = _CseSecyIfTxUnicastUncontrolledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 1),
    _CseSecyIfTxUnicastUncontrolledPkts_Type()
)
cseSecyIfTxUnicastUncontrolledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxUnicastUncontrolledPkts.setStatus("current")
_CseSecyIfTxMulticastUncontrolledPkts_Type = Counter64
_CseSecyIfTxMulticastUncontrolledPkts_Object = MibTableColumn
cseSecyIfTxMulticastUncontrolledPkts = _CseSecyIfTxMulticastUncontrolledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 2),
    _CseSecyIfTxMulticastUncontrolledPkts_Type()
)
cseSecyIfTxMulticastUncontrolledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxMulticastUncontrolledPkts.setStatus("current")
_CseSecyIfTxBroadcastUncontrolledPkts_Type = Counter64
_CseSecyIfTxBroadcastUncontrolledPkts_Object = MibTableColumn
cseSecyIfTxBroadcastUncontrolledPkts = _CseSecyIfTxBroadcastUncontrolledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 3),
    _CseSecyIfTxBroadcastUncontrolledPkts_Type()
)
cseSecyIfTxBroadcastUncontrolledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxBroadcastUncontrolledPkts.setStatus("current")
_CseSecyIfTxUncontrolledPktsDrop_Type = Counter64
_CseSecyIfTxUncontrolledPktsDrop_Object = MibTableColumn
cseSecyIfTxUncontrolledPktsDrop = _CseSecyIfTxUncontrolledPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 4),
    _CseSecyIfTxUncontrolledPktsDrop_Type()
)
cseSecyIfTxUncontrolledPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxUncontrolledPktsDrop.setStatus("current")
_CseSecyIfTxUncontrolledPktsError_Type = Counter64
_CseSecyIfTxUncontrolledPktsError_Object = MibTableColumn
cseSecyIfTxUncontrolledPktsError = _CseSecyIfTxUncontrolledPktsError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 5),
    _CseSecyIfTxUncontrolledPktsError_Type()
)
cseSecyIfTxUncontrolledPktsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxUncontrolledPktsError.setStatus("current")
_CseSecyIfTxUnicastControlledPkts_Type = Counter64
_CseSecyIfTxUnicastControlledPkts_Object = MibTableColumn
cseSecyIfTxUnicastControlledPkts = _CseSecyIfTxUnicastControlledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 6),
    _CseSecyIfTxUnicastControlledPkts_Type()
)
cseSecyIfTxUnicastControlledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxUnicastControlledPkts.setStatus("current")
_CseSecyIfTxMulticastControlledPkts_Type = Counter64
_CseSecyIfTxMulticastControlledPkts_Object = MibTableColumn
cseSecyIfTxMulticastControlledPkts = _CseSecyIfTxMulticastControlledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 7),
    _CseSecyIfTxMulticastControlledPkts_Type()
)
cseSecyIfTxMulticastControlledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxMulticastControlledPkts.setStatus("current")
_CseSecyIfTxBroadcastControlledPkts_Type = Counter64
_CseSecyIfTxBroadcastControlledPkts_Object = MibTableColumn
cseSecyIfTxBroadcastControlledPkts = _CseSecyIfTxBroadcastControlledPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 8),
    _CseSecyIfTxBroadcastControlledPkts_Type()
)
cseSecyIfTxBroadcastControlledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxBroadcastControlledPkts.setStatus("current")
_CseSecyIfTxControlledPktsDrop_Type = Counter64
_CseSecyIfTxControlledPktsDrop_Object = MibTableColumn
cseSecyIfTxControlledPktsDrop = _CseSecyIfTxControlledPktsDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 9),
    _CseSecyIfTxControlledPktsDrop_Type()
)
cseSecyIfTxControlledPktsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxControlledPktsDrop.setStatus("current")
_CseSecyIfTxControlledPktsError_Type = Counter64
_CseSecyIfTxControlledPktsError_Object = MibTableColumn
cseSecyIfTxControlledPktsError = _CseSecyIfTxControlledPktsError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 10),
    _CseSecyIfTxControlledPktsError_Type()
)
cseSecyIfTxControlledPktsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxControlledPktsError.setStatus("current")
_CseSecyIfTxUncontrolledOctets_Type = Counter64
_CseSecyIfTxUncontrolledOctets_Object = MibTableColumn
cseSecyIfTxUncontrolledOctets = _CseSecyIfTxUncontrolledOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 11),
    _CseSecyIfTxUncontrolledOctets_Type()
)
cseSecyIfTxUncontrolledOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxUncontrolledOctets.setStatus("current")
_CseSecyIfTxControlledOctets_Type = Counter64
_CseSecyIfTxControlledOctets_Object = MibTableColumn
cseSecyIfTxControlledOctets = _CseSecyIfTxControlledOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 12),
    _CseSecyIfTxControlledOctets_Type()
)
cseSecyIfTxControlledOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxControlledOctets.setStatus("current")
_CseSecyIfTxCommonOctets_Type = Counter64
_CseSecyIfTxCommonOctets_Object = MibTableColumn
cseSecyIfTxCommonOctets = _CseSecyIfTxCommonOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 13),
    _CseSecyIfTxCommonOctets_Type()
)
cseSecyIfTxCommonOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxCommonOctets.setStatus("current")
_CseSecyIfTxUncontrolledPktRate_Type = CounterBasedGauge64
_CseSecyIfTxUncontrolledPktRate_Object = MibTableColumn
cseSecyIfTxUncontrolledPktRate = _CseSecyIfTxUncontrolledPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 14),
    _CseSecyIfTxUncontrolledPktRate_Type()
)
cseSecyIfTxUncontrolledPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxUncontrolledPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cseSecyIfTxUncontrolledPktRate.setUnits("Packets per second")
_CseSecyIfTxUncontrolledOctetRate_Type = CounterBasedGauge64
_CseSecyIfTxUncontrolledOctetRate_Object = MibTableColumn
cseSecyIfTxUncontrolledOctetRate = _CseSecyIfTxUncontrolledOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 15),
    _CseSecyIfTxUncontrolledOctetRate_Type()
)
cseSecyIfTxUncontrolledOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxUncontrolledOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    cseSecyIfTxUncontrolledOctetRate.setUnits("Bytes per second")
_CseSecyIfTxControlledPktRate_Type = CounterBasedGauge64
_CseSecyIfTxControlledPktRate_Object = MibTableColumn
cseSecyIfTxControlledPktRate = _CseSecyIfTxControlledPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 16),
    _CseSecyIfTxControlledPktRate_Type()
)
cseSecyIfTxControlledPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxControlledPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cseSecyIfTxControlledPktRate.setUnits("Packets per second")
_CseSecyIfTxControlledOctetRate_Type = CounterBasedGauge64
_CseSecyIfTxControlledOctetRate_Object = MibTableColumn
cseSecyIfTxControlledOctetRate = _CseSecyIfTxControlledOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 1, 1, 4, 1, 17),
    _CseSecyIfTxControlledOctetRate_Type()
)
cseSecyIfTxControlledOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSecyIfTxControlledOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    cseSecyIfTxControlledOctetRate.setUnits("Bytes per second")
_CiscoSecyExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoSecyExtMIBConform = _CiscoSecyExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 2)
)
_CiscoSecyExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSecyExtMIBCompliances = _CiscoSecyExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 1)
)
_CiscoSecyExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSecyExtMIBGroups = _CiscoSecyExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 2)
)

# Managed Objects groups

cseSecyStatsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 2, 1)
)
cseSecyStatsExtGroup.setObjects(
      *(("CISCO-SECY-EXT-MIB", "cseSecyStatsRxTransformErrPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyStatsRxControlPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyStatsRxTaggedCtrlPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyStatsTxTransformErrPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyStatsTxControlPkts"))
)
if mibBuilder.loadTexts:
    cseSecyStatsExtGroup.setStatus("current")

cseSecyTxSCStatsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 2, 2)
)
cseSecyTxSCStatsExtGroup.setObjects(
    ("CISCO-SECY-EXT-MIB", "cseSecyTxSCStatsSANotInUse")
)
if mibBuilder.loadTexts:
    cseSecyTxSCStatsExtGroup.setStatus("current")

cseSecyIfRxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 2, 3)
)
cseSecyIfRxStatsGroup.setObjects(
      *(("CISCO-SECY-EXT-MIB", "cseSecyIfRxUnicastUncontrolledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxMulticastUncontrolledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxBroadcastUncontrolledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUncontrolledPktsDrop"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUncontrolledPktsError"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUnicastControlledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxMulticastControlledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxBroadcastControlledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxControlledPktsDrop"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxControlledPktsError"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUncontrolledOctets"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxControlledOctets"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUncontrolledPktRate"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxUncontrolledOctetRate"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxControlledPktRate"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfRxControlledOctetRate"))
)
if mibBuilder.loadTexts:
    cseSecyIfRxStatsGroup.setStatus("current")

cseSecyIfTxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 2, 4)
)
cseSecyIfTxStatsGroup.setObjects(
      *(("CISCO-SECY-EXT-MIB", "cseSecyIfTxUnicastUncontrolledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxMulticastUncontrolledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxBroadcastUncontrolledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUncontrolledPktsDrop"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUncontrolledPktsError"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUnicastControlledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxMulticastControlledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxBroadcastControlledPkts"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxControlledPktsDrop"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxControlledPktsError"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUncontrolledOctets"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxControlledOctets"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxCommonOctets"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUncontrolledPktRate"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxUncontrolledOctetRate"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxControlledPktRate"),
        ("CISCO-SECY-EXT-MIB", "cseSecyIfTxControlledOctetRate"))
)
if mibBuilder.loadTexts:
    cseSecyIfTxStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cseSecyExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 835, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cseSecyExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SECY-EXT-MIB",
    **{"ciscoSecyExtMIB": ciscoSecyExtMIB,
       "ciscoSecyExtMIBNotifs": ciscoSecyExtMIBNotifs,
       "ciscoSecyExtMIBObjects": ciscoSecyExtMIBObjects,
       "ciscoSecyExtMIBStatsObjects": ciscoSecyExtMIBStatsObjects,
       "cseSecyStatsExtTable": cseSecyStatsExtTable,
       "cseSecyStatsExtEntry": cseSecyStatsExtEntry,
       "cseSecyStatsRxTransformErrPkts": cseSecyStatsRxTransformErrPkts,
       "cseSecyStatsRxControlPkts": cseSecyStatsRxControlPkts,
       "cseSecyStatsRxTaggedCtrlPkts": cseSecyStatsRxTaggedCtrlPkts,
       "cseSecyStatsTxTransformErrPkts": cseSecyStatsTxTransformErrPkts,
       "cseSecyStatsTxControlPkts": cseSecyStatsTxControlPkts,
       "cseSecyTxSCStatsExtTable": cseSecyTxSCStatsExtTable,
       "cseSecyTxSCStatsExtEntry": cseSecyTxSCStatsExtEntry,
       "cseSecyTxSCStatsSANotInUse": cseSecyTxSCStatsSANotInUse,
       "cseSecyIfRxStatsTable": cseSecyIfRxStatsTable,
       "cseSecyIfRxStatsEntry": cseSecyIfRxStatsEntry,
       "cseSecyIfRxUnicastUncontrolledPkts": cseSecyIfRxUnicastUncontrolledPkts,
       "cseSecyIfRxMulticastUncontrolledPkts": cseSecyIfRxMulticastUncontrolledPkts,
       "cseSecyIfRxBroadcastUncontrolledPkts": cseSecyIfRxBroadcastUncontrolledPkts,
       "cseSecyIfRxUncontrolledPktsDrop": cseSecyIfRxUncontrolledPktsDrop,
       "cseSecyIfRxUncontrolledPktsError": cseSecyIfRxUncontrolledPktsError,
       "cseSecyIfRxUnicastControlledPkts": cseSecyIfRxUnicastControlledPkts,
       "cseSecyIfRxMulticastControlledPkts": cseSecyIfRxMulticastControlledPkts,
       "cseSecyIfRxBroadcastControlledPkts": cseSecyIfRxBroadcastControlledPkts,
       "cseSecyIfRxControlledPktsDrop": cseSecyIfRxControlledPktsDrop,
       "cseSecyIfRxControlledPktsError": cseSecyIfRxControlledPktsError,
       "cseSecyIfRxUncontrolledOctets": cseSecyIfRxUncontrolledOctets,
       "cseSecyIfRxControlledOctets": cseSecyIfRxControlledOctets,
       "cseSecyIfRxUncontrolledPktRate": cseSecyIfRxUncontrolledPktRate,
       "cseSecyIfRxUncontrolledOctetRate": cseSecyIfRxUncontrolledOctetRate,
       "cseSecyIfRxControlledPktRate": cseSecyIfRxControlledPktRate,
       "cseSecyIfRxControlledOctetRate": cseSecyIfRxControlledOctetRate,
       "cseSecyIfTxStatsTable": cseSecyIfTxStatsTable,
       "cseSecyIfTxStatsEntry": cseSecyIfTxStatsEntry,
       "cseSecyIfTxUnicastUncontrolledPkts": cseSecyIfTxUnicastUncontrolledPkts,
       "cseSecyIfTxMulticastUncontrolledPkts": cseSecyIfTxMulticastUncontrolledPkts,
       "cseSecyIfTxBroadcastUncontrolledPkts": cseSecyIfTxBroadcastUncontrolledPkts,
       "cseSecyIfTxUncontrolledPktsDrop": cseSecyIfTxUncontrolledPktsDrop,
       "cseSecyIfTxUncontrolledPktsError": cseSecyIfTxUncontrolledPktsError,
       "cseSecyIfTxUnicastControlledPkts": cseSecyIfTxUnicastControlledPkts,
       "cseSecyIfTxMulticastControlledPkts": cseSecyIfTxMulticastControlledPkts,
       "cseSecyIfTxBroadcastControlledPkts": cseSecyIfTxBroadcastControlledPkts,
       "cseSecyIfTxControlledPktsDrop": cseSecyIfTxControlledPktsDrop,
       "cseSecyIfTxControlledPktsError": cseSecyIfTxControlledPktsError,
       "cseSecyIfTxUncontrolledOctets": cseSecyIfTxUncontrolledOctets,
       "cseSecyIfTxControlledOctets": cseSecyIfTxControlledOctets,
       "cseSecyIfTxCommonOctets": cseSecyIfTxCommonOctets,
       "cseSecyIfTxUncontrolledPktRate": cseSecyIfTxUncontrolledPktRate,
       "cseSecyIfTxUncontrolledOctetRate": cseSecyIfTxUncontrolledOctetRate,
       "cseSecyIfTxControlledPktRate": cseSecyIfTxControlledPktRate,
       "cseSecyIfTxControlledOctetRate": cseSecyIfTxControlledOctetRate,
       "ciscoSecyExtMIBConform": ciscoSecyExtMIBConform,
       "ciscoSecyExtMIBCompliances": ciscoSecyExtMIBCompliances,
       "cseSecyExtMIBCompliance": cseSecyExtMIBCompliance,
       "ciscoSecyExtMIBGroups": ciscoSecyExtMIBGroups,
       "cseSecyStatsExtGroup": cseSecyStatsExtGroup,
       "cseSecyTxSCStatsExtGroup": cseSecyTxSCStatsExtGroup,
       "cseSecyIfRxStatsGroup": cseSecyIfRxStatsGroup,
       "cseSecyIfTxStatsGroup": cseSecyIfTxStatsGroup}
)
