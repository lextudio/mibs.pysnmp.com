# SNMP MIB module (CISCO-OBMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OBMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:20 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoObmiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 698)
)
ciscoObmiMIB.setRevisions(
        ("2009-05-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoObmiMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoObmiMIBNotifs = _CiscoObmiMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 0)
)
_CiscoObmiMIBObjects_ObjectIdentity = ObjectIdentity
ciscoObmiMIBObjects = _CiscoObmiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1)
)
_CObmiTransportTable_Object = MibTable
cObmiTransportTable = _CObmiTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2)
)
if mibBuilder.loadTexts:
    cObmiTransportTable.setStatus("current")
_CObmiTransportEntry_Object = MibTableRow
cObmiTransportEntry = _CObmiTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1)
)
cObmiTransportEntry.setIndexNames(
    (0, "CISCO-OBMI-MIB", "cObmiBusID"),
)
if mibBuilder.loadTexts:
    cObmiTransportEntry.setStatus("current")


class _CObmiBusID_Type(Unsigned32):
    """Custom type cObmiBusID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CObmiBusID_Type.__name__ = "Unsigned32"
_CObmiBusID_Object = MibTableColumn
cObmiBusID = _CObmiBusID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 1),
    _CObmiBusID_Type()
)
cObmiBusID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cObmiBusID.setStatus("current")
_CObmiBusName_Type = DisplayString
_CObmiBusName_Object = MibTableColumn
cObmiBusName = _CObmiBusName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 2),
    _CObmiBusName_Type()
)
cObmiBusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiBusName.setStatus("current")
_CObmiCommandRx_Type = Counter32
_CObmiCommandRx_Object = MibTableColumn
cObmiCommandRx = _CObmiCommandRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 3),
    _CObmiCommandRx_Type()
)
cObmiCommandRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiCommandRx.setStatus("current")
if mibBuilder.loadTexts:
    cObmiCommandRx.setUnits("Messages")
_CObmiCommandProcessedTotal_Type = Counter32
_CObmiCommandProcessedTotal_Object = MibTableColumn
cObmiCommandProcessedTotal = _CObmiCommandProcessedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 4),
    _CObmiCommandProcessedTotal_Type()
)
cObmiCommandProcessedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiCommandProcessedTotal.setStatus("current")
if mibBuilder.loadTexts:
    cObmiCommandProcessedTotal.setUnits("Messages")
_CObmiCommandGets_Type = Counter32
_CObmiCommandGets_Object = MibTableColumn
cObmiCommandGets = _CObmiCommandGets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 5),
    _CObmiCommandGets_Type()
)
cObmiCommandGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiCommandGets.setStatus("current")
if mibBuilder.loadTexts:
    cObmiCommandGets.setUnits("Messages")
_CObmiCommandSets_Type = Counter32
_CObmiCommandSets_Object = MibTableColumn
cObmiCommandSets = _CObmiCommandSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 6),
    _CObmiCommandSets_Type()
)
cObmiCommandSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiCommandSets.setStatus("current")
if mibBuilder.loadTexts:
    cObmiCommandSets.setUnits("Messages")
_CObmiCommandProcessedInvalid_Type = Counter32
_CObmiCommandProcessedInvalid_Object = MibTableColumn
cObmiCommandProcessedInvalid = _CObmiCommandProcessedInvalid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 7),
    _CObmiCommandProcessedInvalid_Type()
)
cObmiCommandProcessedInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiCommandProcessedInvalid.setStatus("current")
if mibBuilder.loadTexts:
    cObmiCommandProcessedInvalid.setUnits("Messages")
_CObmiCommandPending_Type = Gauge32
_CObmiCommandPending_Object = MibTableColumn
cObmiCommandPending = _CObmiCommandPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 8),
    _CObmiCommandPending_Type()
)
cObmiCommandPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiCommandPending.setStatus("current")
if mibBuilder.loadTexts:
    cObmiCommandPending.setUnits("Messages")
_CObmiCommandDropped_Type = Counter32
_CObmiCommandDropped_Object = MibTableColumn
cObmiCommandDropped = _CObmiCommandDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 9),
    _CObmiCommandDropped_Type()
)
cObmiCommandDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiCommandDropped.setStatus("current")
if mibBuilder.loadTexts:
    cObmiCommandDropped.setUnits("Messages")
_CObmiTelemetrySent_Type = Counter32
_CObmiTelemetrySent_Object = MibTableColumn
cObmiTelemetrySent = _CObmiTelemetrySent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 10),
    _CObmiTelemetrySent_Type()
)
cObmiTelemetrySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiTelemetrySent.setStatus("current")
if mibBuilder.loadTexts:
    cObmiTelemetrySent.setUnits("Messages")
_CObmiTelemetryDemandSent_Type = Counter32
_CObmiTelemetryDemandSent_Object = MibTableColumn
cObmiTelemetryDemandSent = _CObmiTelemetryDemandSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 11),
    _CObmiTelemetryDemandSent_Type()
)
cObmiTelemetryDemandSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiTelemetryDemandSent.setStatus("current")
if mibBuilder.loadTexts:
    cObmiTelemetryDemandSent.setUnits("Messages")
_CObmiTelemetryPending_Type = Gauge32
_CObmiTelemetryPending_Object = MibTableColumn
cObmiTelemetryPending = _CObmiTelemetryPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 12),
    _CObmiTelemetryPending_Type()
)
cObmiTelemetryPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiTelemetryPending.setStatus("current")
if mibBuilder.loadTexts:
    cObmiTelemetryPending.setUnits("Messages")
_CObmiTransportHeartBeatTable_Object = MibTable
cObmiTransportHeartBeatTable = _CObmiTransportHeartBeatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3)
)
if mibBuilder.loadTexts:
    cObmiTransportHeartBeatTable.setStatus("current")
_CObmiTransportHeartBeatEntry_Object = MibTableRow
cObmiTransportHeartBeatEntry = _CObmiTransportHeartBeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1)
)
cObmiTransportHeartBeatEntry.setIndexNames(
    (0, "CISCO-OBMI-MIB", "cObmiBusID"),
    (0, "CISCO-OBMI-MIB", "cObmiHeartBeatPort"),
)
if mibBuilder.loadTexts:
    cObmiTransportHeartBeatEntry.setStatus("current")


class _CObmiHeartBeatPort_Type(Unsigned32):
    """Custom type cObmiHeartBeatPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CObmiHeartBeatPort_Type.__name__ = "Unsigned32"
_CObmiHeartBeatPort_Object = MibTableColumn
cObmiHeartBeatPort = _CObmiHeartBeatPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1, 1),
    _CObmiHeartBeatPort_Type()
)
cObmiHeartBeatPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cObmiHeartBeatPort.setStatus("current")
_CObmiHeartBeatSent_Type = Counter32
_CObmiHeartBeatSent_Object = MibTableColumn
cObmiHeartBeatSent = _CObmiHeartBeatSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1, 2),
    _CObmiHeartBeatSent_Type()
)
cObmiHeartBeatSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiHeartBeatSent.setStatus("current")
if mibBuilder.loadTexts:
    cObmiHeartBeatSent.setUnits("Messages")
_CObmiHeartBeatPending_Type = Gauge32
_CObmiHeartBeatPending_Object = MibTableColumn
cObmiHeartBeatPending = _CObmiHeartBeatPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1, 3),
    _CObmiHeartBeatPending_Type()
)
cObmiHeartBeatPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiHeartBeatPending.setStatus("current")
if mibBuilder.loadTexts:
    cObmiHeartBeatPending.setUnits("Messages")
_CObmiM500FramingTable_Object = MibTable
cObmiM500FramingTable = _CObmiM500FramingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4)
)
if mibBuilder.loadTexts:
    cObmiM500FramingTable.setStatus("current")
_CObmiM500FramingEntry_Object = MibTableRow
cObmiM500FramingEntry = _CObmiM500FramingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1)
)
cObmiM500FramingEntry.setIndexNames(
    (0, "CISCO-OBMI-MIB", "cObmiBusID"),
)
if mibBuilder.loadTexts:
    cObmiM500FramingEntry.setStatus("current")
_CObmiM500RxFrames_Type = Counter32
_CObmiM500RxFrames_Object = MibTableColumn
cObmiM500RxFrames = _CObmiM500RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 1),
    _CObmiM500RxFrames_Type()
)
cObmiM500RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500RxFrames.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500RxFrames.setUnits("Frames")
_CObmiM500RxBytes_Type = Counter32
_CObmiM500RxBytes_Object = MibTableColumn
cObmiM500RxBytes = _CObmiM500RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 2),
    _CObmiM500RxBytes_Type()
)
cObmiM500RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500RxBytes.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500RxBytes.setUnits("Bytes")
_CObmiM500RxAbortFrames_Type = Counter32
_CObmiM500RxAbortFrames_Object = MibTableColumn
cObmiM500RxAbortFrames = _CObmiM500RxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 3),
    _CObmiM500RxAbortFrames_Type()
)
cObmiM500RxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500RxAbortFrames.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500RxAbortFrames.setUnits("Frames")
_CObmiM500RxEchoFrames_Type = Counter32
_CObmiM500RxEchoFrames_Object = MibTableColumn
cObmiM500RxEchoFrames = _CObmiM500RxEchoFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 4),
    _CObmiM500RxEchoFrames_Type()
)
cObmiM500RxEchoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500RxEchoFrames.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500RxEchoFrames.setUnits("Frames")
_CObmiM500RxResetFrames_Type = Counter32
_CObmiM500RxResetFrames_Object = MibTableColumn
cObmiM500RxResetFrames = _CObmiM500RxResetFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 5),
    _CObmiM500RxResetFrames_Type()
)
cObmiM500RxResetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500RxResetFrames.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500RxResetFrames.setUnits("Frames")
_CObmiM500RxTransportErrFrames_Type = Counter32
_CObmiM500RxTransportErrFrames_Object = MibTableColumn
cObmiM500RxTransportErrFrames = _CObmiM500RxTransportErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 6),
    _CObmiM500RxTransportErrFrames_Type()
)
cObmiM500RxTransportErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500RxTransportErrFrames.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500RxTransportErrFrames.setUnits("Frames")
_CObmiM500RxUnknownOpFrames_Type = Counter32
_CObmiM500RxUnknownOpFrames_Object = MibTableColumn
cObmiM500RxUnknownOpFrames = _CObmiM500RxUnknownOpFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 7),
    _CObmiM500RxUnknownOpFrames_Type()
)
cObmiM500RxUnknownOpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500RxUnknownOpFrames.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500RxUnknownOpFrames.setUnits("Frames")
_CObmiM500TxFrames_Type = Counter32
_CObmiM500TxFrames_Object = MibTableColumn
cObmiM500TxFrames = _CObmiM500TxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 8),
    _CObmiM500TxFrames_Type()
)
cObmiM500TxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TxFrames.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500TxFrames.setUnits("Frames")
_CObmiM500TxBytes_Type = Counter32
_CObmiM500TxBytes_Object = MibTableColumn
cObmiM500TxBytes = _CObmiM500TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 9),
    _CObmiM500TxBytes_Type()
)
cObmiM500TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TxBytes.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500TxBytes.setUnits("Frames")
_CObmiM500TxAbortFrames_Type = Counter32
_CObmiM500TxAbortFrames_Object = MibTableColumn
cObmiM500TxAbortFrames = _CObmiM500TxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 10),
    _CObmiM500TxAbortFrames_Type()
)
cObmiM500TxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TxAbortFrames.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500TxAbortFrames.setUnits("Frames")
_CObmiM500TxEchoFrames_Type = Counter32
_CObmiM500TxEchoFrames_Object = MibTableColumn
cObmiM500TxEchoFrames = _CObmiM500TxEchoFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 11),
    _CObmiM500TxEchoFrames_Type()
)
cObmiM500TxEchoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TxEchoFrames.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500TxEchoFrames.setUnits("Frames")
_CObmiM500TxTransportErrFrames_Type = Counter32
_CObmiM500TxTransportErrFrames_Object = MibTableColumn
cObmiM500TxTransportErrFrames = _CObmiM500TxTransportErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 12),
    _CObmiM500TxTransportErrFrames_Type()
)
cObmiM500TxTransportErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TxTransportErrFrames.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500TxTransportErrFrames.setUnits("Frames")
_CObmiM500RxQOverRun_Type = Counter32
_CObmiM500RxQOverRun_Object = MibTableColumn
cObmiM500RxQOverRun = _CObmiM500RxQOverRun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 13),
    _CObmiM500RxQOverRun_Type()
)
cObmiM500RxQOverRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500RxQOverRun.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500RxQOverRun.setUnits("Messages")
_CObmiM500TxQ0UnderRun_Type = Counter32
_CObmiM500TxQ0UnderRun_Object = MibTableColumn
cObmiM500TxQ0UnderRun = _CObmiM500TxQ0UnderRun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 14),
    _CObmiM500TxQ0UnderRun_Type()
)
cObmiM500TxQ0UnderRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TxQ0UnderRun.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500TxQ0UnderRun.setUnits("Messages")
_CObmiM500TxQ1UnderRun_Type = Counter32
_CObmiM500TxQ1UnderRun_Object = MibTableColumn
cObmiM500TxQ1UnderRun = _CObmiM500TxQ1UnderRun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 15),
    _CObmiM500TxQ1UnderRun_Type()
)
cObmiM500TxQ1UnderRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TxQ1UnderRun.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500TxQ1UnderRun.setUnits("Messages")
_CObmiM500TxCtlQOverRun_Type = Counter32
_CObmiM500TxCtlQOverRun_Object = MibTableColumn
cObmiM500TxCtlQOverRun = _CObmiM500TxCtlQOverRun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 16),
    _CObmiM500TxCtlQOverRun_Type()
)
cObmiM500TxCtlQOverRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TxCtlQOverRun.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500TxCtlQOverRun.setUnits("Messages")
_CObmiM500PhyTable_Object = MibTable
cObmiM500PhyTable = _CObmiM500PhyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5)
)
if mibBuilder.loadTexts:
    cObmiM500PhyTable.setStatus("current")
_CObmiM500PhyEntry_Object = MibTableRow
cObmiM500PhyEntry = _CObmiM500PhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1)
)
cObmiM500PhyEntry.setIndexNames(
    (0, "CISCO-OBMI-MIB", "cObmiBusID"),
)
if mibBuilder.loadTexts:
    cObmiM500PhyEntry.setStatus("current")
_CObmiM500BusALOS_Type = TruthValue
_CObmiM500BusALOS_Object = MibTableColumn
cObmiM500BusALOS = _CObmiM500BusALOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 1),
    _CObmiM500BusALOS_Type()
)
cObmiM500BusALOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500BusALOS.setStatus("current")
_CObmiM500BusBLOS_Type = TruthValue
_CObmiM500BusBLOS_Object = MibTableColumn
cObmiM500BusBLOS = _CObmiM500BusBLOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 2),
    _CObmiM500BusBLOS_Type()
)
cObmiM500BusBLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500BusBLOS.setStatus("current")


class _CObmiM500LastActiveBus_Type(Bits):
    """Custom type cObmiM500LastActiveBus based on Bits"""
    namedValues = NamedValues(
        *(("a", 0),
          ("b", 1))
    )

_CObmiM500LastActiveBus_Type.__name__ = "Bits"
_CObmiM500LastActiveBus_Object = MibTableColumn
cObmiM500LastActiveBus = _CObmiM500LastActiveBus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 3),
    _CObmiM500LastActiveBus_Type()
)
cObmiM500LastActiveBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500LastActiveBus.setStatus("current")
_CObmiM500CommandsRcvd_Type = Counter32
_CObmiM500CommandsRcvd_Object = MibTableColumn
cObmiM500CommandsRcvd = _CObmiM500CommandsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 4),
    _CObmiM500CommandsRcvd_Type()
)
cObmiM500CommandsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500CommandsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500CommandsRcvd.setUnits("Words")
_CObmiM500TelemetrySent_Type = Counter32
_CObmiM500TelemetrySent_Object = MibTableColumn
cObmiM500TelemetrySent = _CObmiM500TelemetrySent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 5),
    _CObmiM500TelemetrySent_Type()
)
cObmiM500TelemetrySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TelemetrySent.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500TelemetrySent.setUnits("Words")
_CObmiM500TelemetryErrs_Type = Counter32
_CObmiM500TelemetryErrs_Object = MibTableColumn
cObmiM500TelemetryErrs = _CObmiM500TelemetryErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 6),
    _CObmiM500TelemetryErrs_Type()
)
cObmiM500TelemetryErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TelemetryErrs.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500TelemetryErrs.setUnits("Words")
_CObmiM500CommandErrs_Type = Counter32
_CObmiM500CommandErrs_Object = MibTableColumn
cObmiM500CommandErrs = _CObmiM500CommandErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 7),
    _CObmiM500CommandErrs_Type()
)
cObmiM500CommandErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500CommandErrs.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500CommandErrs.setUnits("Words")
_CObmiM500CommandOverWrts_Type = Counter32
_CObmiM500CommandOverWrts_Object = MibTableColumn
cObmiM500CommandOverWrts = _CObmiM500CommandOverWrts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 8),
    _CObmiM500CommandOverWrts_Type()
)
cObmiM500CommandOverWrts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500CommandOverWrts.setStatus("current")
if mibBuilder.loadTexts:
    cObmiM500CommandOverWrts.setUnits("Words")
_CObmiM500HWParityErr_Type = TruthValue
_CObmiM500HWParityErr_Object = MibTableColumn
cObmiM500HWParityErr = _CObmiM500HWParityErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 9),
    _CObmiM500HWParityErr_Type()
)
cObmiM500HWParityErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500HWParityErr.setStatus("current")
_CObmiM500TelemetryReqParityErr_Type = TruthValue
_CObmiM500TelemetryReqParityErr_Object = MibTableColumn
cObmiM500TelemetryReqParityErr = _CObmiM500TelemetryReqParityErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 10),
    _CObmiM500TelemetryReqParityErr_Type()
)
cObmiM500TelemetryReqParityErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500TelemetryReqParityErr.setStatus("current")
_CObmiM500CommandParityErr_Type = TruthValue
_CObmiM500CommandParityErr_Object = MibTableColumn
cObmiM500CommandParityErr = _CObmiM500CommandParityErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 11),
    _CObmiM500CommandParityErr_Type()
)
cObmiM500CommandParityErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500CommandParityErr.setStatus("current")
_CObmiM500CommandTimeout_Type = TruthValue
_CObmiM500CommandTimeout_Object = MibTableColumn
cObmiM500CommandTimeout = _CObmiM500CommandTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 12),
    _CObmiM500CommandTimeout_Type()
)
cObmiM500CommandTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500CommandTimeout.setStatus("current")
_CObmiM500CommandOverWrt_Type = TruthValue
_CObmiM500CommandOverWrt_Object = MibTableColumn
cObmiM500CommandOverWrt = _CObmiM500CommandOverWrt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 13),
    _CObmiM500CommandOverWrt_Type()
)
cObmiM500CommandOverWrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cObmiM500CommandOverWrt.setStatus("current")
_CiscoObmiMIBConform_ObjectIdentity = ObjectIdentity
ciscoObmiMIBConform = _CiscoObmiMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 2)
)
_CiscoObmiMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoObmiMIBCompliances = _CiscoObmiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 1)
)
_CiscoObmiMIBGroups_ObjectIdentity = ObjectIdentity
ciscoObmiMIBGroups = _CiscoObmiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 2)
)

# Managed Objects groups

ciscoObmiMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 2, 1)
)
ciscoObmiMIBMainObjectGroup.setObjects(
      *(("CISCO-OBMI-MIB", "cObmiBusName"),
        ("CISCO-OBMI-MIB", "cObmiCommandRx"),
        ("CISCO-OBMI-MIB", "cObmiCommandProcessedTotal"),
        ("CISCO-OBMI-MIB", "cObmiCommandGets"),
        ("CISCO-OBMI-MIB", "cObmiCommandSets"),
        ("CISCO-OBMI-MIB", "cObmiCommandProcessedInvalid"),
        ("CISCO-OBMI-MIB", "cObmiCommandPending"),
        ("CISCO-OBMI-MIB", "cObmiCommandDropped"),
        ("CISCO-OBMI-MIB", "cObmiTelemetrySent"),
        ("CISCO-OBMI-MIB", "cObmiTelemetryDemandSent"),
        ("CISCO-OBMI-MIB", "cObmiTelemetryPending"),
        ("CISCO-OBMI-MIB", "cObmiHeartBeatSent"),
        ("CISCO-OBMI-MIB", "cObmiHeartBeatPending"))
)
if mibBuilder.loadTexts:
    ciscoObmiMIBMainObjectGroup.setStatus("current")

ciscoObmiMIBM500ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 2, 2)
)
ciscoObmiMIBM500ObjectGroup.setObjects(
      *(("CISCO-OBMI-MIB", "cObmiM500RxFrames"),
        ("CISCO-OBMI-MIB", "cObmiM500RxBytes"),
        ("CISCO-OBMI-MIB", "cObmiM500RxAbortFrames"),
        ("CISCO-OBMI-MIB", "cObmiM500RxEchoFrames"),
        ("CISCO-OBMI-MIB", "cObmiM500RxResetFrames"),
        ("CISCO-OBMI-MIB", "cObmiM500RxTransportErrFrames"),
        ("CISCO-OBMI-MIB", "cObmiM500RxUnknownOpFrames"),
        ("CISCO-OBMI-MIB", "cObmiM500TxFrames"),
        ("CISCO-OBMI-MIB", "cObmiM500TxBytes"),
        ("CISCO-OBMI-MIB", "cObmiM500TxAbortFrames"),
        ("CISCO-OBMI-MIB", "cObmiM500TxEchoFrames"),
        ("CISCO-OBMI-MIB", "cObmiM500TxTransportErrFrames"),
        ("CISCO-OBMI-MIB", "cObmiM500RxQOverRun"),
        ("CISCO-OBMI-MIB", "cObmiM500TxQ0UnderRun"),
        ("CISCO-OBMI-MIB", "cObmiM500TxQ1UnderRun"),
        ("CISCO-OBMI-MIB", "cObmiM500TxCtlQOverRun"),
        ("CISCO-OBMI-MIB", "cObmiM500BusALOS"),
        ("CISCO-OBMI-MIB", "cObmiM500BusBLOS"),
        ("CISCO-OBMI-MIB", "cObmiM500LastActiveBus"),
        ("CISCO-OBMI-MIB", "cObmiM500CommandsRcvd"),
        ("CISCO-OBMI-MIB", "cObmiM500TelemetrySent"),
        ("CISCO-OBMI-MIB", "cObmiM500TelemetryErrs"),
        ("CISCO-OBMI-MIB", "cObmiM500CommandErrs"),
        ("CISCO-OBMI-MIB", "cObmiM500HWParityErr"),
        ("CISCO-OBMI-MIB", "cObmiM500CommandOverWrts"),
        ("CISCO-OBMI-MIB", "cObmiM500TelemetryReqParityErr"),
        ("CISCO-OBMI-MIB", "cObmiM500CommandParityErr"),
        ("CISCO-OBMI-MIB", "cObmiM500CommandTimeout"),
        ("CISCO-OBMI-MIB", "cObmiM500CommandOverWrt"))
)
if mibBuilder.loadTexts:
    ciscoObmiMIBM500ObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoObmiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoObmiMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OBMI-MIB",
    **{"ciscoObmiMIB": ciscoObmiMIB,
       "ciscoObmiMIBNotifs": ciscoObmiMIBNotifs,
       "ciscoObmiMIBObjects": ciscoObmiMIBObjects,
       "cObmiTransportTable": cObmiTransportTable,
       "cObmiTransportEntry": cObmiTransportEntry,
       "cObmiBusID": cObmiBusID,
       "cObmiBusName": cObmiBusName,
       "cObmiCommandRx": cObmiCommandRx,
       "cObmiCommandProcessedTotal": cObmiCommandProcessedTotal,
       "cObmiCommandGets": cObmiCommandGets,
       "cObmiCommandSets": cObmiCommandSets,
       "cObmiCommandProcessedInvalid": cObmiCommandProcessedInvalid,
       "cObmiCommandPending": cObmiCommandPending,
       "cObmiCommandDropped": cObmiCommandDropped,
       "cObmiTelemetrySent": cObmiTelemetrySent,
       "cObmiTelemetryDemandSent": cObmiTelemetryDemandSent,
       "cObmiTelemetryPending": cObmiTelemetryPending,
       "cObmiTransportHeartBeatTable": cObmiTransportHeartBeatTable,
       "cObmiTransportHeartBeatEntry": cObmiTransportHeartBeatEntry,
       "cObmiHeartBeatPort": cObmiHeartBeatPort,
       "cObmiHeartBeatSent": cObmiHeartBeatSent,
       "cObmiHeartBeatPending": cObmiHeartBeatPending,
       "cObmiM500FramingTable": cObmiM500FramingTable,
       "cObmiM500FramingEntry": cObmiM500FramingEntry,
       "cObmiM500RxFrames": cObmiM500RxFrames,
       "cObmiM500RxBytes": cObmiM500RxBytes,
       "cObmiM500RxAbortFrames": cObmiM500RxAbortFrames,
       "cObmiM500RxEchoFrames": cObmiM500RxEchoFrames,
       "cObmiM500RxResetFrames": cObmiM500RxResetFrames,
       "cObmiM500RxTransportErrFrames": cObmiM500RxTransportErrFrames,
       "cObmiM500RxUnknownOpFrames": cObmiM500RxUnknownOpFrames,
       "cObmiM500TxFrames": cObmiM500TxFrames,
       "cObmiM500TxBytes": cObmiM500TxBytes,
       "cObmiM500TxAbortFrames": cObmiM500TxAbortFrames,
       "cObmiM500TxEchoFrames": cObmiM500TxEchoFrames,
       "cObmiM500TxTransportErrFrames": cObmiM500TxTransportErrFrames,
       "cObmiM500RxQOverRun": cObmiM500RxQOverRun,
       "cObmiM500TxQ0UnderRun": cObmiM500TxQ0UnderRun,
       "cObmiM500TxQ1UnderRun": cObmiM500TxQ1UnderRun,
       "cObmiM500TxCtlQOverRun": cObmiM500TxCtlQOverRun,
       "cObmiM500PhyTable": cObmiM500PhyTable,
       "cObmiM500PhyEntry": cObmiM500PhyEntry,
       "cObmiM500BusALOS": cObmiM500BusALOS,
       "cObmiM500BusBLOS": cObmiM500BusBLOS,
       "cObmiM500LastActiveBus": cObmiM500LastActiveBus,
       "cObmiM500CommandsRcvd": cObmiM500CommandsRcvd,
       "cObmiM500TelemetrySent": cObmiM500TelemetrySent,
       "cObmiM500TelemetryErrs": cObmiM500TelemetryErrs,
       "cObmiM500CommandErrs": cObmiM500CommandErrs,
       "cObmiM500CommandOverWrts": cObmiM500CommandOverWrts,
       "cObmiM500HWParityErr": cObmiM500HWParityErr,
       "cObmiM500TelemetryReqParityErr": cObmiM500TelemetryReqParityErr,
       "cObmiM500CommandParityErr": cObmiM500CommandParityErr,
       "cObmiM500CommandTimeout": cObmiM500CommandTimeout,
       "cObmiM500CommandOverWrt": cObmiM500CommandOverWrt,
       "ciscoObmiMIBConform": ciscoObmiMIBConform,
       "ciscoObmiMIBCompliances": ciscoObmiMIBCompliances,
       "ciscoObmiMIBCompliance": ciscoObmiMIBCompliance,
       "ciscoObmiMIBGroups": ciscoObmiMIBGroups,
       "ciscoObmiMIBMainObjectGroup": ciscoObmiMIBMainObjectGroup,
       "ciscoObmiMIBM500ObjectGroup": ciscoObmiMIBM500ObjectGroup}
)
