# SNMP MIB module (NIMBLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NIMBLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:30 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

nimble = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37447)
)
nimble.setRevisions(
        ("2012-08-31 00:00",
         "2012-06-12 00:00",
         "2011-02-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Variables_ObjectIdentity = ObjectIdentity
variables = _Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 1)
)
_VolNumberOfVolumes_Type = Unsigned32
_VolNumberOfVolumes_Object = MibScalar
volNumberOfVolumes = _VolNumberOfVolumes_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 1),
    _VolNumberOfVolumes_Type()
)
volNumberOfVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volNumberOfVolumes.setStatus("obsolete")
_VolTable_Object = MibTable
volTable = _VolTable_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2)
)
if mibBuilder.loadTexts:
    volTable.setStatus("current")
_VolEntry_Object = MibTableRow
volEntry = _VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1)
)
volEntry.setIndexNames(
    (0, "NIMBLE-MIB", "volIndex"),
)
if mibBuilder.loadTexts:
    volEntry.setStatus("current")
_VolIndex_Type = Unsigned32
_VolIndex_Object = MibTableColumn
volIndex = _VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 1),
    _VolIndex_Type()
)
volIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    volIndex.setStatus("current")
_VolID_Type = Unsigned32
_VolID_Object = MibTableColumn
volID = _VolID_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 2),
    _VolID_Type()
)
volID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volID.setStatus("current")
_VolName_Type = DisplayString
_VolName_Object = MibTableColumn
volName = _VolName_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 3),
    _VolName_Type()
)
volName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volName.setStatus("current")
_VolSizeLow_Type = Unsigned32
_VolSizeLow_Object = MibTableColumn
volSizeLow = _VolSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 4),
    _VolSizeLow_Type()
)
volSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volSizeLow.setStatus("current")
_VolSizeHigh_Type = Unsigned32
_VolSizeHigh_Object = MibTableColumn
volSizeHigh = _VolSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 5),
    _VolSizeHigh_Type()
)
volSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volSizeHigh.setStatus("current")
_VolUsageLow_Type = Unsigned32
_VolUsageLow_Object = MibTableColumn
volUsageLow = _VolUsageLow_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 6),
    _VolUsageLow_Type()
)
volUsageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volUsageLow.setStatus("current")
_VolUsageHigh_Type = Unsigned32
_VolUsageHigh_Object = MibTableColumn
volUsageHigh = _VolUsageHigh_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 7),
    _VolUsageHigh_Type()
)
volUsageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volUsageHigh.setStatus("current")
_VolReserveLow_Type = Unsigned32
_VolReserveLow_Object = MibTableColumn
volReserveLow = _VolReserveLow_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 8),
    _VolReserveLow_Type()
)
volReserveLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volReserveLow.setStatus("current")
_VolReserveHigh_Type = Unsigned32
_VolReserveHigh_Object = MibTableColumn
volReserveHigh = _VolReserveHigh_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 9),
    _VolReserveHigh_Type()
)
volReserveHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volReserveHigh.setStatus("current")
_VolOnline_Type = TruthValue
_VolOnline_Object = MibTableColumn
volOnline = _VolOnline_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 10),
    _VolOnline_Type()
)
volOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volOnline.setStatus("current")
_VolNumConnections_Type = Unsigned32
_VolNumConnections_Object = MibTableColumn
volNumConnections = _VolNumConnections_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 11),
    _VolNumConnections_Type()
)
volNumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volNumConnections.setStatus("current")
_VolStatTimeEpochSeconds_Type = Counter64
_VolStatTimeEpochSeconds_Object = MibTableColumn
volStatTimeEpochSeconds = _VolStatTimeEpochSeconds_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 12),
    _VolStatTimeEpochSeconds_Type()
)
volStatTimeEpochSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volStatTimeEpochSeconds.setStatus("current")
_VolIoReads_Type = Counter64
_VolIoReads_Object = MibTableColumn
volIoReads = _VolIoReads_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 13),
    _VolIoReads_Type()
)
volIoReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReads.setStatus("current")
_VolIoReadTimeMicrosec_Type = Counter64
_VolIoReadTimeMicrosec_Object = MibTableColumn
volIoReadTimeMicrosec = _VolIoReadTimeMicrosec_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 14),
    _VolIoReadTimeMicrosec_Type()
)
volIoReadTimeMicrosec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadTimeMicrosec.setStatus("current")
_VolIoReadBytes_Type = Counter64
_VolIoReadBytes_Object = MibTableColumn
volIoReadBytes = _VolIoReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 15),
    _VolIoReadBytes_Type()
)
volIoReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadBytes.setStatus("current")
_VolIoSeqReads_Type = Counter64
_VolIoSeqReads_Object = MibTableColumn
volIoSeqReads = _VolIoSeqReads_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 16),
    _VolIoSeqReads_Type()
)
volIoSeqReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoSeqReads.setStatus("current")
_VolIoSeqReadBytes_Type = Counter64
_VolIoSeqReadBytes_Object = MibTableColumn
volIoSeqReadBytes = _VolIoSeqReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 17),
    _VolIoSeqReadBytes_Type()
)
volIoSeqReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoSeqReadBytes.setStatus("current")
_VolIoNonseqReadTotalHits_Type = Counter64
_VolIoNonseqReadTotalHits_Object = MibTableColumn
volIoNonseqReadTotalHits = _VolIoNonseqReadTotalHits_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 18),
    _VolIoNonseqReadTotalHits_Type()
)
volIoNonseqReadTotalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoNonseqReadTotalHits.setStatus("current")
_VolIoNonseqReadMemHits_Type = Counter64
_VolIoNonseqReadMemHits_Object = MibTableColumn
volIoNonseqReadMemHits = _VolIoNonseqReadMemHits_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 19),
    _VolIoNonseqReadMemHits_Type()
)
volIoNonseqReadMemHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoNonseqReadMemHits.setStatus("current")
_VolIoNonseqReadSSDHits_Type = Counter64
_VolIoNonseqReadSSDHits_Object = MibTableColumn
volIoNonseqReadSSDHits = _VolIoNonseqReadSSDHits_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 20),
    _VolIoNonseqReadSSDHits_Type()
)
volIoNonseqReadSSDHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoNonseqReadSSDHits.setStatus("current")
_VolIoReadLatency0uTo100u_Type = Counter64
_VolIoReadLatency0uTo100u_Object = MibTableColumn
volIoReadLatency0uTo100u = _VolIoReadLatency0uTo100u_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 21),
    _VolIoReadLatency0uTo100u_Type()
)
volIoReadLatency0uTo100u.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency0uTo100u.setStatus("current")
_VolIoReadLatency100uTo200u_Type = Counter64
_VolIoReadLatency100uTo200u_Object = MibTableColumn
volIoReadLatency100uTo200u = _VolIoReadLatency100uTo200u_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 22),
    _VolIoReadLatency100uTo200u_Type()
)
volIoReadLatency100uTo200u.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency100uTo200u.setStatus("current")
_VolIoReadLatency200uTo500u_Type = Counter64
_VolIoReadLatency200uTo500u_Object = MibTableColumn
volIoReadLatency200uTo500u = _VolIoReadLatency200uTo500u_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 23),
    _VolIoReadLatency200uTo500u_Type()
)
volIoReadLatency200uTo500u.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency200uTo500u.setStatus("current")
_VolIoReadLatency500uTo1m_Type = Counter64
_VolIoReadLatency500uTo1m_Object = MibTableColumn
volIoReadLatency500uTo1m = _VolIoReadLatency500uTo1m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 24),
    _VolIoReadLatency500uTo1m_Type()
)
volIoReadLatency500uTo1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency500uTo1m.setStatus("current")
_VolIoReadLatency1mTo2m_Type = Counter64
_VolIoReadLatency1mTo2m_Object = MibTableColumn
volIoReadLatency1mTo2m = _VolIoReadLatency1mTo2m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 25),
    _VolIoReadLatency1mTo2m_Type()
)
volIoReadLatency1mTo2m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency1mTo2m.setStatus("current")
_VolIoReadLatency2mTo5m_Type = Counter64
_VolIoReadLatency2mTo5m_Object = MibTableColumn
volIoReadLatency2mTo5m = _VolIoReadLatency2mTo5m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 26),
    _VolIoReadLatency2mTo5m_Type()
)
volIoReadLatency2mTo5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency2mTo5m.setStatus("current")
_VolIoReadLatency5mTo10m_Type = Counter64
_VolIoReadLatency5mTo10m_Object = MibTableColumn
volIoReadLatency5mTo10m = _VolIoReadLatency5mTo10m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 27),
    _VolIoReadLatency5mTo10m_Type()
)
volIoReadLatency5mTo10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency5mTo10m.setStatus("current")
_VolIoReadLatency10mTo20m_Type = Counter64
_VolIoReadLatency10mTo20m_Object = MibTableColumn
volIoReadLatency10mTo20m = _VolIoReadLatency10mTo20m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 28),
    _VolIoReadLatency10mTo20m_Type()
)
volIoReadLatency10mTo20m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency10mTo20m.setStatus("current")
_VolIoReadLatency20mTo50m_Type = Counter64
_VolIoReadLatency20mTo50m_Object = MibTableColumn
volIoReadLatency20mTo50m = _VolIoReadLatency20mTo50m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 29),
    _VolIoReadLatency20mTo50m_Type()
)
volIoReadLatency20mTo50m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency20mTo50m.setStatus("current")
_VolIoReadLatency50mTo100m_Type = Counter64
_VolIoReadLatency50mTo100m_Object = MibTableColumn
volIoReadLatency50mTo100m = _VolIoReadLatency50mTo100m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 30),
    _VolIoReadLatency50mTo100m_Type()
)
volIoReadLatency50mTo100m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency50mTo100m.setStatus("current")
_VolIoReadLatency100mTo200m_Type = Counter64
_VolIoReadLatency100mTo200m_Object = MibTableColumn
volIoReadLatency100mTo200m = _VolIoReadLatency100mTo200m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 31),
    _VolIoReadLatency100mTo200m_Type()
)
volIoReadLatency100mTo200m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency100mTo200m.setStatus("current")
_VolIoReadLatency200mTo500m_Type = Counter64
_VolIoReadLatency200mTo500m_Object = MibTableColumn
volIoReadLatency200mTo500m = _VolIoReadLatency200mTo500m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 32),
    _VolIoReadLatency200mTo500m_Type()
)
volIoReadLatency200mTo500m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency200mTo500m.setStatus("current")
_VolIoReadLatency500mTomax_Type = Counter64
_VolIoReadLatency500mTomax_Object = MibTableColumn
volIoReadLatency500mTomax = _VolIoReadLatency500mTomax_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 33),
    _VolIoReadLatency500mTomax_Type()
)
volIoReadLatency500mTomax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoReadLatency500mTomax.setStatus("current")
_VolIoWrites_Type = Counter64
_VolIoWrites_Object = MibTableColumn
volIoWrites = _VolIoWrites_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 34),
    _VolIoWrites_Type()
)
volIoWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWrites.setStatus("current")
_VolIoWriteTimeMicrosec_Type = Counter64
_VolIoWriteTimeMicrosec_Object = MibTableColumn
volIoWriteTimeMicrosec = _VolIoWriteTimeMicrosec_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 35),
    _VolIoWriteTimeMicrosec_Type()
)
volIoWriteTimeMicrosec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteTimeMicrosec.setStatus("current")
_VolIoWriteBytes_Type = Counter64
_VolIoWriteBytes_Object = MibTableColumn
volIoWriteBytes = _VolIoWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 36),
    _VolIoWriteBytes_Type()
)
volIoWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteBytes.setStatus("current")
_VolIoSeqWrites_Type = Counter64
_VolIoSeqWrites_Object = MibTableColumn
volIoSeqWrites = _VolIoSeqWrites_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 37),
    _VolIoSeqWrites_Type()
)
volIoSeqWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoSeqWrites.setStatus("current")
_VolIoSeqWriteBytes_Type = Counter64
_VolIoSeqWriteBytes_Object = MibTableColumn
volIoSeqWriteBytes = _VolIoSeqWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 38),
    _VolIoSeqWriteBytes_Type()
)
volIoSeqWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoSeqWriteBytes.setStatus("current")
_VolIoWriteLatency0uTo100u_Type = Counter64
_VolIoWriteLatency0uTo100u_Object = MibTableColumn
volIoWriteLatency0uTo100u = _VolIoWriteLatency0uTo100u_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 39),
    _VolIoWriteLatency0uTo100u_Type()
)
volIoWriteLatency0uTo100u.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency0uTo100u.setStatus("current")
_VolIoWriteLatency100uTo200u_Type = Counter64
_VolIoWriteLatency100uTo200u_Object = MibTableColumn
volIoWriteLatency100uTo200u = _VolIoWriteLatency100uTo200u_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 40),
    _VolIoWriteLatency100uTo200u_Type()
)
volIoWriteLatency100uTo200u.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency100uTo200u.setStatus("current")
_VolIoWriteLatency200uTo500u_Type = Counter64
_VolIoWriteLatency200uTo500u_Object = MibTableColumn
volIoWriteLatency200uTo500u = _VolIoWriteLatency200uTo500u_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 41),
    _VolIoWriteLatency200uTo500u_Type()
)
volIoWriteLatency200uTo500u.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency200uTo500u.setStatus("current")
_VolIoWriteLatency500uTo1m_Type = Counter64
_VolIoWriteLatency500uTo1m_Object = MibTableColumn
volIoWriteLatency500uTo1m = _VolIoWriteLatency500uTo1m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 42),
    _VolIoWriteLatency500uTo1m_Type()
)
volIoWriteLatency500uTo1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency500uTo1m.setStatus("current")
_VolIoWriteLatency1mTo2m_Type = Counter64
_VolIoWriteLatency1mTo2m_Object = MibTableColumn
volIoWriteLatency1mTo2m = _VolIoWriteLatency1mTo2m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 43),
    _VolIoWriteLatency1mTo2m_Type()
)
volIoWriteLatency1mTo2m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency1mTo2m.setStatus("current")
_VolIoWriteLatency2mTo5m_Type = Counter64
_VolIoWriteLatency2mTo5m_Object = MibTableColumn
volIoWriteLatency2mTo5m = _VolIoWriteLatency2mTo5m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 44),
    _VolIoWriteLatency2mTo5m_Type()
)
volIoWriteLatency2mTo5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency2mTo5m.setStatus("current")
_VolIoWriteLatency5mTo10m_Type = Counter64
_VolIoWriteLatency5mTo10m_Object = MibTableColumn
volIoWriteLatency5mTo10m = _VolIoWriteLatency5mTo10m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 45),
    _VolIoWriteLatency5mTo10m_Type()
)
volIoWriteLatency5mTo10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency5mTo10m.setStatus("current")
_VolIoWriteLatency10mTo20m_Type = Counter64
_VolIoWriteLatency10mTo20m_Object = MibTableColumn
volIoWriteLatency10mTo20m = _VolIoWriteLatency10mTo20m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 46),
    _VolIoWriteLatency10mTo20m_Type()
)
volIoWriteLatency10mTo20m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency10mTo20m.setStatus("current")
_VolIoWriteLatency20mTo50m_Type = Counter64
_VolIoWriteLatency20mTo50m_Object = MibTableColumn
volIoWriteLatency20mTo50m = _VolIoWriteLatency20mTo50m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 47),
    _VolIoWriteLatency20mTo50m_Type()
)
volIoWriteLatency20mTo50m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency20mTo50m.setStatus("current")
_VolIoWriteLatency50mTo100m_Type = Counter64
_VolIoWriteLatency50mTo100m_Object = MibTableColumn
volIoWriteLatency50mTo100m = _VolIoWriteLatency50mTo100m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 48),
    _VolIoWriteLatency50mTo100m_Type()
)
volIoWriteLatency50mTo100m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency50mTo100m.setStatus("current")
_VolIoWriteLatency100mTo200m_Type = Counter64
_VolIoWriteLatency100mTo200m_Object = MibTableColumn
volIoWriteLatency100mTo200m = _VolIoWriteLatency100mTo200m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 49),
    _VolIoWriteLatency100mTo200m_Type()
)
volIoWriteLatency100mTo200m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency100mTo200m.setStatus("current")
_VolIoWriteLatency200mTo500m_Type = Counter64
_VolIoWriteLatency200mTo500m_Object = MibTableColumn
volIoWriteLatency200mTo500m = _VolIoWriteLatency200mTo500m_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 50),
    _VolIoWriteLatency200mTo500m_Type()
)
volIoWriteLatency200mTo500m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency200mTo500m.setStatus("current")
_VolIoWriteLatency500mTomax_Type = Counter64
_VolIoWriteLatency500mTomax_Object = MibTableColumn
volIoWriteLatency500mTomax = _VolIoWriteLatency500mTomax_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 51),
    _VolIoWriteLatency500mTomax_Type()
)
volIoWriteLatency500mTomax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIoWriteLatency500mTomax.setStatus("current")
_VolDiskVolBytesUsedLow_Type = Unsigned32
_VolDiskVolBytesUsedLow_Object = MibTableColumn
volDiskVolBytesUsedLow = _VolDiskVolBytesUsedLow_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 52),
    _VolDiskVolBytesUsedLow_Type()
)
volDiskVolBytesUsedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDiskVolBytesUsedLow.setStatus("current")
_VolDiskVolBytesUsedHigh_Type = Unsigned32
_VolDiskVolBytesUsedHigh_Object = MibTableColumn
volDiskVolBytesUsedHigh = _VolDiskVolBytesUsedHigh_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 53),
    _VolDiskVolBytesUsedHigh_Type()
)
volDiskVolBytesUsedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDiskVolBytesUsedHigh.setStatus("current")
_VolDiskSnapBytesUsedLow_Type = Unsigned32
_VolDiskSnapBytesUsedLow_Object = MibTableColumn
volDiskSnapBytesUsedLow = _VolDiskSnapBytesUsedLow_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 54),
    _VolDiskSnapBytesUsedLow_Type()
)
volDiskSnapBytesUsedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDiskSnapBytesUsedLow.setStatus("current")
_VolDiskSnapBytesUsedHigh_Type = Unsigned32
_VolDiskSnapBytesUsedHigh_Object = MibTableColumn
volDiskSnapBytesUsedHigh = _VolDiskSnapBytesUsedHigh_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 2, 1, 55),
    _VolDiskSnapBytesUsedHigh_Type()
)
volDiskSnapBytesUsedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDiskSnapBytesUsedHigh.setStatus("current")
_GlobalStats_ObjectIdentity = ObjectIdentity
globalStats = _GlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3)
)
_StatTimeEpochSeconds_Type = Counter64
_StatTimeEpochSeconds_Object = MibScalar
statTimeEpochSeconds = _StatTimeEpochSeconds_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 1),
    _StatTimeEpochSeconds_Type()
)
statTimeEpochSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeEpochSeconds.setStatus("current")
_IoReads_Type = Counter64
_IoReads_Object = MibScalar
ioReads = _IoReads_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 2),
    _IoReads_Type()
)
ioReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioReads.setStatus("current")
_IoSeqReads_Type = Counter64
_IoSeqReads_Object = MibScalar
ioSeqReads = _IoSeqReads_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 3),
    _IoSeqReads_Type()
)
ioSeqReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioSeqReads.setStatus("current")
_IoWrites_Type = Counter64
_IoWrites_Object = MibScalar
ioWrites = _IoWrites_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 4),
    _IoWrites_Type()
)
ioWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioWrites.setStatus("current")
_IoSeqWrites_Type = Counter64
_IoSeqWrites_Object = MibScalar
ioSeqWrites = _IoSeqWrites_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 5),
    _IoSeqWrites_Type()
)
ioSeqWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioSeqWrites.setStatus("current")
_IoReadTimeMicrosec_Type = Counter64
_IoReadTimeMicrosec_Object = MibScalar
ioReadTimeMicrosec = _IoReadTimeMicrosec_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 6),
    _IoReadTimeMicrosec_Type()
)
ioReadTimeMicrosec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioReadTimeMicrosec.setStatus("current")
_IoWriteTimeMicrosec_Type = Counter64
_IoWriteTimeMicrosec_Object = MibScalar
ioWriteTimeMicrosec = _IoWriteTimeMicrosec_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 7),
    _IoWriteTimeMicrosec_Type()
)
ioWriteTimeMicrosec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioWriteTimeMicrosec.setStatus("current")
_IoReadBytes_Type = Counter64
_IoReadBytes_Object = MibScalar
ioReadBytes = _IoReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 8),
    _IoReadBytes_Type()
)
ioReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioReadBytes.setStatus("current")
_IoSeqReadBytes_Type = Counter64
_IoSeqReadBytes_Object = MibScalar
ioSeqReadBytes = _IoSeqReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 9),
    _IoSeqReadBytes_Type()
)
ioSeqReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioSeqReadBytes.setStatus("current")
_IoWriteBytes_Type = Counter64
_IoWriteBytes_Object = MibScalar
ioWriteBytes = _IoWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 10),
    _IoWriteBytes_Type()
)
ioWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioWriteBytes.setStatus("current")
_IoSeqWriteBytes_Type = Counter64
_IoSeqWriteBytes_Object = MibScalar
ioSeqWriteBytes = _IoSeqWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 11),
    _IoSeqWriteBytes_Type()
)
ioSeqWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioSeqWriteBytes.setStatus("current")
_DiskVolBytesUsedLow_Type = Unsigned32
_DiskVolBytesUsedLow_Object = MibScalar
diskVolBytesUsedLow = _DiskVolBytesUsedLow_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 12),
    _DiskVolBytesUsedLow_Type()
)
diskVolBytesUsedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVolBytesUsedLow.setStatus("current")
_DiskVolBytesUsedHigh_Type = Unsigned32
_DiskVolBytesUsedHigh_Object = MibScalar
diskVolBytesUsedHigh = _DiskVolBytesUsedHigh_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 13),
    _DiskVolBytesUsedHigh_Type()
)
diskVolBytesUsedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVolBytesUsedHigh.setStatus("current")
_DiskSnapBytesUsedLow_Type = Unsigned32
_DiskSnapBytesUsedLow_Object = MibScalar
diskSnapBytesUsedLow = _DiskSnapBytesUsedLow_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 14),
    _DiskSnapBytesUsedLow_Type()
)
diskSnapBytesUsedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSnapBytesUsedLow.setStatus("current")
_DiskSnapBytesUsedHigh_Type = Unsigned32
_DiskSnapBytesUsedHigh_Object = MibScalar
diskSnapBytesUsedHigh = _DiskSnapBytesUsedHigh_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 15),
    _DiskSnapBytesUsedHigh_Type()
)
diskSnapBytesUsedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSnapBytesUsedHigh.setStatus("current")
_IoNonseqReadHits_Type = Counter64
_IoNonseqReadHits_Object = MibScalar
ioNonseqReadHits = _IoNonseqReadHits_Object(
    (1, 3, 6, 1, 4, 1, 37447, 1, 3, 16),
    _IoNonseqReadHits_Type()
)
ioNonseqReadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioNonseqReadHits.setStatus("current")
_Arrays_ObjectIdentity = ObjectIdentity
arrays = _Arrays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37447, 3)
)
_ArrayEntry_Type = DisplayString
_ArrayEntry_Object = MibScalar
arrayEntry = _ArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 37447, 3, 1),
    _ArrayEntry_Type()
)
arrayEntry.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrayEntry.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NIMBLE-MIB",
    **{"nimble": nimble,
       "variables": variables,
       "volNumberOfVolumes": volNumberOfVolumes,
       "volTable": volTable,
       "volEntry": volEntry,
       "volIndex": volIndex,
       "volID": volID,
       "volName": volName,
       "volSizeLow": volSizeLow,
       "volSizeHigh": volSizeHigh,
       "volUsageLow": volUsageLow,
       "volUsageHigh": volUsageHigh,
       "volReserveLow": volReserveLow,
       "volReserveHigh": volReserveHigh,
       "volOnline": volOnline,
       "volNumConnections": volNumConnections,
       "volStatTimeEpochSeconds": volStatTimeEpochSeconds,
       "volIoReads": volIoReads,
       "volIoReadTimeMicrosec": volIoReadTimeMicrosec,
       "volIoReadBytes": volIoReadBytes,
       "volIoSeqReads": volIoSeqReads,
       "volIoSeqReadBytes": volIoSeqReadBytes,
       "volIoNonseqReadTotalHits": volIoNonseqReadTotalHits,
       "volIoNonseqReadMemHits": volIoNonseqReadMemHits,
       "volIoNonseqReadSSDHits": volIoNonseqReadSSDHits,
       "volIoReadLatency0uTo100u": volIoReadLatency0uTo100u,
       "volIoReadLatency100uTo200u": volIoReadLatency100uTo200u,
       "volIoReadLatency200uTo500u": volIoReadLatency200uTo500u,
       "volIoReadLatency500uTo1m": volIoReadLatency500uTo1m,
       "volIoReadLatency1mTo2m": volIoReadLatency1mTo2m,
       "volIoReadLatency2mTo5m": volIoReadLatency2mTo5m,
       "volIoReadLatency5mTo10m": volIoReadLatency5mTo10m,
       "volIoReadLatency10mTo20m": volIoReadLatency10mTo20m,
       "volIoReadLatency20mTo50m": volIoReadLatency20mTo50m,
       "volIoReadLatency50mTo100m": volIoReadLatency50mTo100m,
       "volIoReadLatency100mTo200m": volIoReadLatency100mTo200m,
       "volIoReadLatency200mTo500m": volIoReadLatency200mTo500m,
       "volIoReadLatency500mTomax": volIoReadLatency500mTomax,
       "volIoWrites": volIoWrites,
       "volIoWriteTimeMicrosec": volIoWriteTimeMicrosec,
       "volIoWriteBytes": volIoWriteBytes,
       "volIoSeqWrites": volIoSeqWrites,
       "volIoSeqWriteBytes": volIoSeqWriteBytes,
       "volIoWriteLatency0uTo100u": volIoWriteLatency0uTo100u,
       "volIoWriteLatency100uTo200u": volIoWriteLatency100uTo200u,
       "volIoWriteLatency200uTo500u": volIoWriteLatency200uTo500u,
       "volIoWriteLatency500uTo1m": volIoWriteLatency500uTo1m,
       "volIoWriteLatency1mTo2m": volIoWriteLatency1mTo2m,
       "volIoWriteLatency2mTo5m": volIoWriteLatency2mTo5m,
       "volIoWriteLatency5mTo10m": volIoWriteLatency5mTo10m,
       "volIoWriteLatency10mTo20m": volIoWriteLatency10mTo20m,
       "volIoWriteLatency20mTo50m": volIoWriteLatency20mTo50m,
       "volIoWriteLatency50mTo100m": volIoWriteLatency50mTo100m,
       "volIoWriteLatency100mTo200m": volIoWriteLatency100mTo200m,
       "volIoWriteLatency200mTo500m": volIoWriteLatency200mTo500m,
       "volIoWriteLatency500mTomax": volIoWriteLatency500mTomax,
       "volDiskVolBytesUsedLow": volDiskVolBytesUsedLow,
       "volDiskVolBytesUsedHigh": volDiskVolBytesUsedHigh,
       "volDiskSnapBytesUsedLow": volDiskSnapBytesUsedLow,
       "volDiskSnapBytesUsedHigh": volDiskSnapBytesUsedHigh,
       "globalStats": globalStats,
       "statTimeEpochSeconds": statTimeEpochSeconds,
       "ioReads": ioReads,
       "ioSeqReads": ioSeqReads,
       "ioWrites": ioWrites,
       "ioSeqWrites": ioSeqWrites,
       "ioReadTimeMicrosec": ioReadTimeMicrosec,
       "ioWriteTimeMicrosec": ioWriteTimeMicrosec,
       "ioReadBytes": ioReadBytes,
       "ioSeqReadBytes": ioSeqReadBytes,
       "ioWriteBytes": ioWriteBytes,
       "ioSeqWriteBytes": ioSeqWriteBytes,
       "diskVolBytesUsedLow": diskVolBytesUsedLow,
       "diskVolBytesUsedHigh": diskVolBytesUsedHigh,
       "diskSnapBytesUsedLow": diskSnapBytesUsedLow,
       "diskSnapBytesUsedHigh": diskSnapBytesUsedHigh,
       "ioNonseqReadHits": ioNonseqReadHits,
       "arrays": arrays,
       "arrayEntry": arrayEntry}
)
