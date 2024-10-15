# SNMP MIB module (CISCO-RTTMON-RTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RTTMON-RTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:53 2024
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

(rttMonCtrlAdminIndex,
 rttMonLatestOper,
 rttMonStats) = mibBuilder.importSymbols(
    "CISCO-RTTMON-MIB",
    "rttMonCtrlAdminIndex",
    "rttMonLatestOper",
    "rttMonStats")

(RttResponseSense,) = mibBuilder.importSymbols(
    "CISCO-RTTMON-TC-MIB",
    "RttResponseSense")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoRttMonRtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 487)
)
ciscoRttMonRtpMIB.setRevisions(
        ("2005-08-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RttMonRtpStatsTable_Object = MibTable
rttMonRtpStatsTable = _RttMonRtpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6)
)
if mibBuilder.loadTexts:
    rttMonRtpStatsTable.setStatus("current")
_RttMonRtpStatsEntry_Object = MibTableRow
rttMonRtpStatsEntry = _RttMonRtpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1)
)
rttMonRtpStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsStartTimeIndex"),
)
if mibBuilder.loadTexts:
    rttMonRtpStatsEntry.setStatus("current")
_RttMonRtpStatsStartTimeIndex_Type = TimeStamp
_RttMonRtpStatsStartTimeIndex_Object = MibTableColumn
rttMonRtpStatsStartTimeIndex = _RttMonRtpStatsStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 1),
    _RttMonRtpStatsStartTimeIndex_Type()
)
rttMonRtpStatsStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonRtpStatsStartTimeIndex.setStatus("current")
_RttMonRtpStatsRTTAvg_Type = Gauge32
_RttMonRtpStatsRTTAvg_Object = MibTableColumn
rttMonRtpStatsRTTAvg = _RttMonRtpStatsRTTAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 2),
    _RttMonRtpStatsRTTAvg_Type()
)
rttMonRtpStatsRTTAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsRTTAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsRTTAvg.setUnits("milliseconds")
_RttMonRtpStatsRTTMin_Type = Gauge32
_RttMonRtpStatsRTTMin_Object = MibTableColumn
rttMonRtpStatsRTTMin = _RttMonRtpStatsRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 3),
    _RttMonRtpStatsRTTMin_Type()
)
rttMonRtpStatsRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsRTTMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsRTTMin.setUnits("milliseconds")
_RttMonRtpStatsRTTMax_Type = Gauge32
_RttMonRtpStatsRTTMax_Object = MibTableColumn
rttMonRtpStatsRTTMax = _RttMonRtpStatsRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 4),
    _RttMonRtpStatsRTTMax_Type()
)
rttMonRtpStatsRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsRTTMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsRTTMax.setUnits("milliseconds")
_RttMonRtpStatsIAJitterDSAvg_Type = Gauge32
_RttMonRtpStatsIAJitterDSAvg_Object = MibTableColumn
rttMonRtpStatsIAJitterDSAvg = _RttMonRtpStatsIAJitterDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 5),
    _RttMonRtpStatsIAJitterDSAvg_Type()
)
rttMonRtpStatsIAJitterDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterDSAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterDSAvg.setUnits("milliseconds")
_RttMonRtpStatsIAJitterDSMin_Type = Gauge32
_RttMonRtpStatsIAJitterDSMin_Object = MibTableColumn
rttMonRtpStatsIAJitterDSMin = _RttMonRtpStatsIAJitterDSMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 6),
    _RttMonRtpStatsIAJitterDSMin_Type()
)
rttMonRtpStatsIAJitterDSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterDSMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterDSMin.setUnits("milliseconds")
_RttMonRtpStatsIAJitterDSMax_Type = Gauge32
_RttMonRtpStatsIAJitterDSMax_Object = MibTableColumn
rttMonRtpStatsIAJitterDSMax = _RttMonRtpStatsIAJitterDSMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 7),
    _RttMonRtpStatsIAJitterDSMax_Type()
)
rttMonRtpStatsIAJitterDSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterDSMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterDSMax.setUnits("milliseconds")
_RttMonRtpStatsPacketLossDSAvg_Type = Gauge32
_RttMonRtpStatsPacketLossDSAvg_Object = MibTableColumn
rttMonRtpStatsPacketLossDSAvg = _RttMonRtpStatsPacketLossDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 8),
    _RttMonRtpStatsPacketLossDSAvg_Type()
)
rttMonRtpStatsPacketLossDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossDSAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossDSAvg.setUnits("packets")
_RttMonRtpStatsPacketLossDSMin_Type = Gauge32
_RttMonRtpStatsPacketLossDSMin_Object = MibTableColumn
rttMonRtpStatsPacketLossDSMin = _RttMonRtpStatsPacketLossDSMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 9),
    _RttMonRtpStatsPacketLossDSMin_Type()
)
rttMonRtpStatsPacketLossDSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossDSMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossDSMin.setUnits("packets")
_RttMonRtpStatsPacketLossDSMax_Type = Gauge32
_RttMonRtpStatsPacketLossDSMax_Object = MibTableColumn
rttMonRtpStatsPacketLossDSMax = _RttMonRtpStatsPacketLossDSMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 10),
    _RttMonRtpStatsPacketLossDSMax_Type()
)
rttMonRtpStatsPacketLossDSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossDSMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossDSMax.setUnits("packets")
_RttMonRtpStatsPacketLateDSAvg_Type = Gauge32
_RttMonRtpStatsPacketLateDSAvg_Object = MibTableColumn
rttMonRtpStatsPacketLateDSAvg = _RttMonRtpStatsPacketLateDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 11),
    _RttMonRtpStatsPacketLateDSAvg_Type()
)
rttMonRtpStatsPacketLateDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLateDSAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLateDSAvg.setUnits("packets")
_RttMonRtpStatsPacketEarlyDSAvg_Type = Gauge32
_RttMonRtpStatsPacketEarlyDSAvg_Object = MibTableColumn
rttMonRtpStatsPacketEarlyDSAvg = _RttMonRtpStatsPacketEarlyDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 12),
    _RttMonRtpStatsPacketEarlyDSAvg_Type()
)
rttMonRtpStatsPacketEarlyDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketEarlyDSAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketEarlyDSAvg.setUnits("packets")
_RttMonRtpStatsPacketOOSDSAvg_Type = Gauge32
_RttMonRtpStatsPacketOOSDSAvg_Object = MibTableColumn
rttMonRtpStatsPacketOOSDSAvg = _RttMonRtpStatsPacketOOSDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 13),
    _RttMonRtpStatsPacketOOSDSAvg_Type()
)
rttMonRtpStatsPacketOOSDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketOOSDSAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketOOSDSAvg.setUnits("packets")
_RttMonRtpStatsFrameLossDSAvg_Type = Gauge32
_RttMonRtpStatsFrameLossDSAvg_Object = MibTableColumn
rttMonRtpStatsFrameLossDSAvg = _RttMonRtpStatsFrameLossDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 14),
    _RttMonRtpStatsFrameLossDSAvg_Type()
)
rttMonRtpStatsFrameLossDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsFrameLossDSAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsFrameLossDSAvg.setUnits("frames")
_RttMonRtpStatsFrameLossDSMin_Type = Gauge32
_RttMonRtpStatsFrameLossDSMin_Object = MibTableColumn
rttMonRtpStatsFrameLossDSMin = _RttMonRtpStatsFrameLossDSMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 15),
    _RttMonRtpStatsFrameLossDSMin_Type()
)
rttMonRtpStatsFrameLossDSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsFrameLossDSMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsFrameLossDSMin.setUnits("frames")
_RttMonRtpStatsFrameLossDSMax_Type = Gauge32
_RttMonRtpStatsFrameLossDSMax_Object = MibTableColumn
rttMonRtpStatsFrameLossDSMax = _RttMonRtpStatsFrameLossDSMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 16),
    _RttMonRtpStatsFrameLossDSMax_Type()
)
rttMonRtpStatsFrameLossDSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsFrameLossDSMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsFrameLossDSMax.setUnits("frames")
_RttMonRtpStatsRFactorDSAvg_Type = Gauge32
_RttMonRtpStatsRFactorDSAvg_Object = MibTableColumn
rttMonRtpStatsRFactorDSAvg = _RttMonRtpStatsRFactorDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 17),
    _RttMonRtpStatsRFactorDSAvg_Type()
)
rttMonRtpStatsRFactorDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorDSAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorDSAvg.setUnits("voice quality")
_RttMonRtpStatsRFactorDSMin_Type = Gauge32
_RttMonRtpStatsRFactorDSMin_Object = MibTableColumn
rttMonRtpStatsRFactorDSMin = _RttMonRtpStatsRFactorDSMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 18),
    _RttMonRtpStatsRFactorDSMin_Type()
)
rttMonRtpStatsRFactorDSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorDSMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorDSMin.setUnits("voice quality")
_RttMonRtpStatsRFactorDSMax_Type = Gauge32
_RttMonRtpStatsRFactorDSMax_Object = MibTableColumn
rttMonRtpStatsRFactorDSMax = _RttMonRtpStatsRFactorDSMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 19),
    _RttMonRtpStatsRFactorDSMax_Type()
)
rttMonRtpStatsRFactorDSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorDSMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorDSMax.setUnits("voice quality")
_RttMonRtpStatsMOSCQDSAvg_Type = Gauge32
_RttMonRtpStatsMOSCQDSAvg_Object = MibTableColumn
rttMonRtpStatsMOSCQDSAvg = _RttMonRtpStatsMOSCQDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 20),
    _RttMonRtpStatsMOSCQDSAvg_Type()
)
rttMonRtpStatsMOSCQDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQDSAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQDSAvg.setUnits("voice quality")
_RttMonRtpStatsMOSCQDSMin_Type = Gauge32
_RttMonRtpStatsMOSCQDSMin_Object = MibTableColumn
rttMonRtpStatsMOSCQDSMin = _RttMonRtpStatsMOSCQDSMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 21),
    _RttMonRtpStatsMOSCQDSMin_Type()
)
rttMonRtpStatsMOSCQDSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQDSMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQDSMin.setUnits("voice quality")
_RttMonRtpStatsMOSCQDSMax_Type = Gauge32
_RttMonRtpStatsMOSCQDSMax_Object = MibTableColumn
rttMonRtpStatsMOSCQDSMax = _RttMonRtpStatsMOSCQDSMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 22),
    _RttMonRtpStatsMOSCQDSMax_Type()
)
rttMonRtpStatsMOSCQDSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQDSMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQDSMax.setUnits("voice quality")
_RttMonRtpStatsMOSLQDSAvg_Type = Gauge32
_RttMonRtpStatsMOSLQDSAvg_Object = MibTableColumn
rttMonRtpStatsMOSLQDSAvg = _RttMonRtpStatsMOSLQDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 23),
    _RttMonRtpStatsMOSLQDSAvg_Type()
)
rttMonRtpStatsMOSLQDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSLQDSAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSLQDSAvg.setUnits("voice quality")
_RttMonRtpStatsMOSLQDSMin_Type = Gauge32
_RttMonRtpStatsMOSLQDSMin_Object = MibTableColumn
rttMonRtpStatsMOSLQDSMin = _RttMonRtpStatsMOSLQDSMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 24),
    _RttMonRtpStatsMOSLQDSMin_Type()
)
rttMonRtpStatsMOSLQDSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSLQDSMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSLQDSMin.setUnits("voice quality")
_RttMonRtpStatsMOSLQDSMax_Type = Gauge32
_RttMonRtpStatsMOSLQDSMax_Object = MibTableColumn
rttMonRtpStatsMOSLQDSMax = _RttMonRtpStatsMOSLQDSMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 25),
    _RttMonRtpStatsMOSLQDSMax_Type()
)
rttMonRtpStatsMOSLQDSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSLQDSMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSLQDSMax.setUnits("voice quality")
_RttMonRtpStatsIAJitterSDAvg_Type = Gauge32
_RttMonRtpStatsIAJitterSDAvg_Object = MibTableColumn
rttMonRtpStatsIAJitterSDAvg = _RttMonRtpStatsIAJitterSDAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 26),
    _RttMonRtpStatsIAJitterSDAvg_Type()
)
rttMonRtpStatsIAJitterSDAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterSDAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterSDAvg.setUnits("milliseconds")
_RttMonRtpStatsIAJitterSDMin_Type = Gauge32
_RttMonRtpStatsIAJitterSDMin_Object = MibTableColumn
rttMonRtpStatsIAJitterSDMin = _RttMonRtpStatsIAJitterSDMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 27),
    _RttMonRtpStatsIAJitterSDMin_Type()
)
rttMonRtpStatsIAJitterSDMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterSDMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterSDMin.setUnits("milliseconds")
_RttMonRtpStatsIAJitterSDMax_Type = Gauge32
_RttMonRtpStatsIAJitterSDMax_Object = MibTableColumn
rttMonRtpStatsIAJitterSDMax = _RttMonRtpStatsIAJitterSDMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 28),
    _RttMonRtpStatsIAJitterSDMax_Type()
)
rttMonRtpStatsIAJitterSDMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterSDMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsIAJitterSDMax.setUnits("milliseconds")
_RttMonRtpStatsPacketLossSDAvg_Type = Gauge32
_RttMonRtpStatsPacketLossSDAvg_Object = MibTableColumn
rttMonRtpStatsPacketLossSDAvg = _RttMonRtpStatsPacketLossSDAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 29),
    _RttMonRtpStatsPacketLossSDAvg_Type()
)
rttMonRtpStatsPacketLossSDAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossSDAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossSDAvg.setUnits("packets")
_RttMonRtpStatsPacketLossSDMin_Type = Gauge32
_RttMonRtpStatsPacketLossSDMin_Object = MibTableColumn
rttMonRtpStatsPacketLossSDMin = _RttMonRtpStatsPacketLossSDMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 30),
    _RttMonRtpStatsPacketLossSDMin_Type()
)
rttMonRtpStatsPacketLossSDMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossSDMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossSDMin.setUnits("packets")
_RttMonRtpStatsPacketLossSDMax_Type = Gauge32
_RttMonRtpStatsPacketLossSDMax_Object = MibTableColumn
rttMonRtpStatsPacketLossSDMax = _RttMonRtpStatsPacketLossSDMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 31),
    _RttMonRtpStatsPacketLossSDMax_Type()
)
rttMonRtpStatsPacketLossSDMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossSDMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketLossSDMax.setUnits("packets")
_RttMonRtpStatsPacketsMIAAvg_Type = Gauge32
_RttMonRtpStatsPacketsMIAAvg_Object = MibTableColumn
rttMonRtpStatsPacketsMIAAvg = _RttMonRtpStatsPacketsMIAAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 32),
    _RttMonRtpStatsPacketsMIAAvg_Type()
)
rttMonRtpStatsPacketsMIAAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketsMIAAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsPacketsMIAAvg.setUnits("packets")
_RttMonRtpStatsRFactorSDAvg_Type = Gauge32
_RttMonRtpStatsRFactorSDAvg_Object = MibTableColumn
rttMonRtpStatsRFactorSDAvg = _RttMonRtpStatsRFactorSDAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 33),
    _RttMonRtpStatsRFactorSDAvg_Type()
)
rttMonRtpStatsRFactorSDAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorSDAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorSDAvg.setUnits("voice quality")
_RttMonRtpStatsRFactorSDMin_Type = Gauge32
_RttMonRtpStatsRFactorSDMin_Object = MibTableColumn
rttMonRtpStatsRFactorSDMin = _RttMonRtpStatsRFactorSDMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 34),
    _RttMonRtpStatsRFactorSDMin_Type()
)
rttMonRtpStatsRFactorSDMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorSDMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorSDMin.setUnits("voice quality")
_RttMonRtpStatsRFactorSDMax_Type = Gauge32
_RttMonRtpStatsRFactorSDMax_Object = MibTableColumn
rttMonRtpStatsRFactorSDMax = _RttMonRtpStatsRFactorSDMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 35),
    _RttMonRtpStatsRFactorSDMax_Type()
)
rttMonRtpStatsRFactorSDMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorSDMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsRFactorSDMax.setUnits("voice quality")
_RttMonRtpStatsMOSCQSDAvg_Type = Gauge32
_RttMonRtpStatsMOSCQSDAvg_Object = MibTableColumn
rttMonRtpStatsMOSCQSDAvg = _RttMonRtpStatsMOSCQSDAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 36),
    _RttMonRtpStatsMOSCQSDAvg_Type()
)
rttMonRtpStatsMOSCQSDAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQSDAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQSDAvg.setUnits("voice quality")
_RttMonRtpStatsMOSCQSDMin_Type = Gauge32
_RttMonRtpStatsMOSCQSDMin_Object = MibTableColumn
rttMonRtpStatsMOSCQSDMin = _RttMonRtpStatsMOSCQSDMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 37),
    _RttMonRtpStatsMOSCQSDMin_Type()
)
rttMonRtpStatsMOSCQSDMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQSDMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQSDMin.setUnits("voice quality")
_RttMonRtpStatsMOSCQSDMax_Type = Gauge32
_RttMonRtpStatsMOSCQSDMax_Object = MibTableColumn
rttMonRtpStatsMOSCQSDMax = _RttMonRtpStatsMOSCQSDMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 39),
    _RttMonRtpStatsMOSCQSDMax_Type()
)
rttMonRtpStatsMOSCQSDMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQSDMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsMOSCQSDMax.setUnits("voice quality")
_RttMonRtpStatsOperAvgOWSD_Type = Gauge32
_RttMonRtpStatsOperAvgOWSD_Object = MibTableColumn
rttMonRtpStatsOperAvgOWSD = _RttMonRtpStatsOperAvgOWSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 40),
    _RttMonRtpStatsOperAvgOWSD_Type()
)
rttMonRtpStatsOperAvgOWSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperAvgOWSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperAvgOWSD.setUnits("milliseconds")
_RttMonRtpStatsOperMinOWSD_Type = Gauge32
_RttMonRtpStatsOperMinOWSD_Object = MibTableColumn
rttMonRtpStatsOperMinOWSD = _RttMonRtpStatsOperMinOWSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 41),
    _RttMonRtpStatsOperMinOWSD_Type()
)
rttMonRtpStatsOperMinOWSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperMinOWSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperMinOWSD.setUnits("milliseconds")
_RttMonRtpStatsOperMaxOWSD_Type = Gauge32
_RttMonRtpStatsOperMaxOWSD_Object = MibTableColumn
rttMonRtpStatsOperMaxOWSD = _RttMonRtpStatsOperMaxOWSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 42),
    _RttMonRtpStatsOperMaxOWSD_Type()
)
rttMonRtpStatsOperMaxOWSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperMaxOWSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperMaxOWSD.setUnits("milliseconds")
_RttMonRtpStatsOperAvgOWDS_Type = Gauge32
_RttMonRtpStatsOperAvgOWDS_Object = MibTableColumn
rttMonRtpStatsOperAvgOWDS = _RttMonRtpStatsOperAvgOWDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 43),
    _RttMonRtpStatsOperAvgOWDS_Type()
)
rttMonRtpStatsOperAvgOWDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperAvgOWDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperAvgOWDS.setUnits("milliseconds")
_RttMonRtpStatsOperMinOWDS_Type = Gauge32
_RttMonRtpStatsOperMinOWDS_Object = MibTableColumn
rttMonRtpStatsOperMinOWDS = _RttMonRtpStatsOperMinOWDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 44),
    _RttMonRtpStatsOperMinOWDS_Type()
)
rttMonRtpStatsOperMinOWDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperMinOWDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperMinOWDS.setUnits("milliseconds")
_RttMonRtpStatsOperMaxOWDS_Type = Gauge32
_RttMonRtpStatsOperMaxOWDS_Object = MibTableColumn
rttMonRtpStatsOperMaxOWDS = _RttMonRtpStatsOperMaxOWDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 45),
    _RttMonRtpStatsOperMaxOWDS_Type()
)
rttMonRtpStatsOperMaxOWDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperMaxOWDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsOperMaxOWDS.setUnits("milliseconds")
_RttMonRtpStatsTotalPacketsSDAvg_Type = Gauge32
_RttMonRtpStatsTotalPacketsSDAvg_Object = MibTableColumn
rttMonRtpStatsTotalPacketsSDAvg = _RttMonRtpStatsTotalPacketsSDAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 46),
    _RttMonRtpStatsTotalPacketsSDAvg_Type()
)
rttMonRtpStatsTotalPacketsSDAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsSDAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsSDAvg.setUnits("packets")
_RttMonRtpStatsTotalPacketsSDMin_Type = Gauge32
_RttMonRtpStatsTotalPacketsSDMin_Object = MibTableColumn
rttMonRtpStatsTotalPacketsSDMin = _RttMonRtpStatsTotalPacketsSDMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 47),
    _RttMonRtpStatsTotalPacketsSDMin_Type()
)
rttMonRtpStatsTotalPacketsSDMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsSDMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsSDMin.setUnits("packets")
_RttMonRtpStatsTotalPacketsSDMax_Type = Gauge32
_RttMonRtpStatsTotalPacketsSDMax_Object = MibTableColumn
rttMonRtpStatsTotalPacketsSDMax = _RttMonRtpStatsTotalPacketsSDMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 48),
    _RttMonRtpStatsTotalPacketsSDMax_Type()
)
rttMonRtpStatsTotalPacketsSDMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsSDMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsSDMax.setUnits("packets")
_RttMonRtpStatsTotalPacketsDSAvg_Type = Gauge32
_RttMonRtpStatsTotalPacketsDSAvg_Object = MibTableColumn
rttMonRtpStatsTotalPacketsDSAvg = _RttMonRtpStatsTotalPacketsDSAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 49),
    _RttMonRtpStatsTotalPacketsDSAvg_Type()
)
rttMonRtpStatsTotalPacketsDSAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsDSAvg.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsDSAvg.setUnits("packets")
_RttMonRtpStatsTotalPacketsDSMax_Type = Gauge32
_RttMonRtpStatsTotalPacketsDSMax_Object = MibTableColumn
rttMonRtpStatsTotalPacketsDSMax = _RttMonRtpStatsTotalPacketsDSMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 50),
    _RttMonRtpStatsTotalPacketsDSMax_Type()
)
rttMonRtpStatsTotalPacketsDSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsDSMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsDSMax.setUnits("packets")
_RttMonRtpStatsTotalPacketsDSMin_Type = Gauge32
_RttMonRtpStatsTotalPacketsDSMin_Object = MibTableColumn
rttMonRtpStatsTotalPacketsDSMin = _RttMonRtpStatsTotalPacketsDSMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 6, 1, 51),
    _RttMonRtpStatsTotalPacketsDSMin_Type()
)
rttMonRtpStatsTotalPacketsDSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsDSMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonRtpStatsTotalPacketsDSMin.setUnits("packets")
_RttMonLatestRtpOperTable_Object = MibTable
rttMonLatestRtpOperTable = _RttMonLatestRtpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3)
)
if mibBuilder.loadTexts:
    rttMonLatestRtpOperTable.setStatus("current")
_RttMonLatestRtpOperEntry_Object = MibTableRow
rttMonLatestRtpOperEntry = _RttMonLatestRtpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1)
)
rttMonLatestRtpOperEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonLatestRtpOperEntry.setStatus("current")
_RttMonLatestRtpOperRTT_Type = Gauge32
_RttMonLatestRtpOperRTT_Object = MibTableColumn
rttMonLatestRtpOperRTT = _RttMonLatestRtpOperRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 1),
    _RttMonLatestRtpOperRTT_Type()
)
rttMonLatestRtpOperRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperRTT.setStatus("current")
_RttMonLatestRtpOperIAJitterDS_Type = Gauge32
_RttMonLatestRtpOperIAJitterDS_Object = MibTableColumn
rttMonLatestRtpOperIAJitterDS = _RttMonLatestRtpOperIAJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 2),
    _RttMonLatestRtpOperIAJitterDS_Type()
)
rttMonLatestRtpOperIAJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperIAJitterDS.setStatus("current")
_RttMonLatestRtpOperPacketLossDS_Type = Gauge32
_RttMonLatestRtpOperPacketLossDS_Object = MibTableColumn
rttMonLatestRtpOperPacketLossDS = _RttMonLatestRtpOperPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 3),
    _RttMonLatestRtpOperPacketLossDS_Type()
)
rttMonLatestRtpOperPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperPacketLossDS.setStatus("current")
_RttMonLatestRtpOperPacketLateDS_Type = Gauge32
_RttMonLatestRtpOperPacketLateDS_Object = MibTableColumn
rttMonLatestRtpOperPacketLateDS = _RttMonLatestRtpOperPacketLateDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 4),
    _RttMonLatestRtpOperPacketLateDS_Type()
)
rttMonLatestRtpOperPacketLateDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperPacketLateDS.setStatus("current")
_RttMonLatestRtpOperPacketEarlyDS_Type = Gauge32
_RttMonLatestRtpOperPacketEarlyDS_Object = MibTableColumn
rttMonLatestRtpOperPacketEarlyDS = _RttMonLatestRtpOperPacketEarlyDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 5),
    _RttMonLatestRtpOperPacketEarlyDS_Type()
)
rttMonLatestRtpOperPacketEarlyDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperPacketEarlyDS.setStatus("current")
_RttMonLatestRtpOperPacketOOSDS_Type = Gauge32
_RttMonLatestRtpOperPacketOOSDS_Object = MibTableColumn
rttMonLatestRtpOperPacketOOSDS = _RttMonLatestRtpOperPacketOOSDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 6),
    _RttMonLatestRtpOperPacketOOSDS_Type()
)
rttMonLatestRtpOperPacketOOSDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperPacketOOSDS.setStatus("current")
_RttMonLatestRtpOperFrameLossDS_Type = Gauge32
_RttMonLatestRtpOperFrameLossDS_Object = MibTableColumn
rttMonLatestRtpOperFrameLossDS = _RttMonLatestRtpOperFrameLossDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 7),
    _RttMonLatestRtpOperFrameLossDS_Type()
)
rttMonLatestRtpOperFrameLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperFrameLossDS.setStatus("current")
_RttMonLatestRtpOperRFactorDS_Type = Gauge32
_RttMonLatestRtpOperRFactorDS_Object = MibTableColumn
rttMonLatestRtpOperRFactorDS = _RttMonLatestRtpOperRFactorDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 8),
    _RttMonLatestRtpOperRFactorDS_Type()
)
rttMonLatestRtpOperRFactorDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperRFactorDS.setStatus("current")
_RttMonLatestRtpOperMOSCQDS_Type = Gauge32
_RttMonLatestRtpOperMOSCQDS_Object = MibTableColumn
rttMonLatestRtpOperMOSCQDS = _RttMonLatestRtpOperMOSCQDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 9),
    _RttMonLatestRtpOperMOSCQDS_Type()
)
rttMonLatestRtpOperMOSCQDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMOSCQDS.setStatus("current")
_RttMonLatestRtpOperMOSLQDS_Type = Gauge32
_RttMonLatestRtpOperMOSLQDS_Object = MibTableColumn
rttMonLatestRtpOperMOSLQDS = _RttMonLatestRtpOperMOSLQDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 10),
    _RttMonLatestRtpOperMOSLQDS_Type()
)
rttMonLatestRtpOperMOSLQDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMOSLQDS.setStatus("current")
_RttMonLatestRtpOperSense_Type = RttResponseSense
_RttMonLatestRtpOperSense_Object = MibTableColumn
rttMonLatestRtpOperSense = _RttMonLatestRtpOperSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 11),
    _RttMonLatestRtpOperSense_Type()
)
rttMonLatestRtpOperSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperSense.setStatus("current")
_RttMonLatestRtpErrorSenseDescription_Type = DisplayString
_RttMonLatestRtpErrorSenseDescription_Object = MibTableColumn
rttMonLatestRtpErrorSenseDescription = _RttMonLatestRtpErrorSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 12),
    _RttMonLatestRtpErrorSenseDescription_Type()
)
rttMonLatestRtpErrorSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpErrorSenseDescription.setStatus("current")
_RttMonLatestRtpOperIAJitterSD_Type = Gauge32
_RttMonLatestRtpOperIAJitterSD_Object = MibTableColumn
rttMonLatestRtpOperIAJitterSD = _RttMonLatestRtpOperIAJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 13),
    _RttMonLatestRtpOperIAJitterSD_Type()
)
rttMonLatestRtpOperIAJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperIAJitterSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperIAJitterSD.setUnits("milliseconds")
_RttMonLatestRtpOperPacketLossSD_Type = Gauge32
_RttMonLatestRtpOperPacketLossSD_Object = MibTableColumn
rttMonLatestRtpOperPacketLossSD = _RttMonLatestRtpOperPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 14),
    _RttMonLatestRtpOperPacketLossSD_Type()
)
rttMonLatestRtpOperPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperPacketLossSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperPacketLossSD.setUnits("packets")
_RttMonLatestRtpOperPacketsMIA_Type = Gauge32
_RttMonLatestRtpOperPacketsMIA_Object = MibTableColumn
rttMonLatestRtpOperPacketsMIA = _RttMonLatestRtpOperPacketsMIA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 15),
    _RttMonLatestRtpOperPacketsMIA_Type()
)
rttMonLatestRtpOperPacketsMIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperPacketsMIA.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperPacketsMIA.setUnits("packets")
_RttMonLatestRtpOperRFactorSD_Type = Gauge32
_RttMonLatestRtpOperRFactorSD_Object = MibTableColumn
rttMonLatestRtpOperRFactorSD = _RttMonLatestRtpOperRFactorSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 16),
    _RttMonLatestRtpOperRFactorSD_Type()
)
rttMonLatestRtpOperRFactorSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperRFactorSD.setStatus("current")
_RttMonLatestRtpOperMOSCQSD_Type = Gauge32
_RttMonLatestRtpOperMOSCQSD_Object = MibTableColumn
rttMonLatestRtpOperMOSCQSD = _RttMonLatestRtpOperMOSCQSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 17),
    _RttMonLatestRtpOperMOSCQSD_Type()
)
rttMonLatestRtpOperMOSCQSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMOSCQSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMOSCQSD.setUnits("voice quality")
_RttMonLatestRtpOperMinOWSD_Type = Gauge32
_RttMonLatestRtpOperMinOWSD_Object = MibTableColumn
rttMonLatestRtpOperMinOWSD = _RttMonLatestRtpOperMinOWSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 18),
    _RttMonLatestRtpOperMinOWSD_Type()
)
rttMonLatestRtpOperMinOWSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMinOWSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMinOWSD.setUnits("milliseconds")
_RttMonLatestRtpOperMaxOWSD_Type = Gauge32
_RttMonLatestRtpOperMaxOWSD_Object = MibTableColumn
rttMonLatestRtpOperMaxOWSD = _RttMonLatestRtpOperMaxOWSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 19),
    _RttMonLatestRtpOperMaxOWSD_Type()
)
rttMonLatestRtpOperMaxOWSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMaxOWSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMaxOWSD.setUnits("milliseconds")
_RttMonLatestRtpOperAvgOWSD_Type = Gauge32
_RttMonLatestRtpOperAvgOWSD_Object = MibTableColumn
rttMonLatestRtpOperAvgOWSD = _RttMonLatestRtpOperAvgOWSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 20),
    _RttMonLatestRtpOperAvgOWSD_Type()
)
rttMonLatestRtpOperAvgOWSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperAvgOWSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperAvgOWSD.setUnits("milliseconds")
_RttMonLatestRtpOperMinOWDS_Type = Gauge32
_RttMonLatestRtpOperMinOWDS_Object = MibTableColumn
rttMonLatestRtpOperMinOWDS = _RttMonLatestRtpOperMinOWDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 21),
    _RttMonLatestRtpOperMinOWDS_Type()
)
rttMonLatestRtpOperMinOWDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMinOWDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMinOWDS.setUnits("milliseconds")
_RttMonLatestRtpOperMaxOWDS_Type = Gauge32
_RttMonLatestRtpOperMaxOWDS_Object = MibTableColumn
rttMonLatestRtpOperMaxOWDS = _RttMonLatestRtpOperMaxOWDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 22),
    _RttMonLatestRtpOperMaxOWDS_Type()
)
rttMonLatestRtpOperMaxOWDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMaxOWDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperMaxOWDS.setUnits("milliseconds")
_RttMonLatestRtpOperAvgOWDS_Type = Gauge32
_RttMonLatestRtpOperAvgOWDS_Object = MibTableColumn
rttMonLatestRtpOperAvgOWDS = _RttMonLatestRtpOperAvgOWDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 23),
    _RttMonLatestRtpOperAvgOWDS_Type()
)
rttMonLatestRtpOperAvgOWDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperAvgOWDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperAvgOWDS.setUnits("milliseconds")
_RttMonLatestRtpOperTotalPaksSD_Type = Gauge32
_RttMonLatestRtpOperTotalPaksSD_Object = MibTableColumn
rttMonLatestRtpOperTotalPaksSD = _RttMonLatestRtpOperTotalPaksSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 24),
    _RttMonLatestRtpOperTotalPaksSD_Type()
)
rttMonLatestRtpOperTotalPaksSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperTotalPaksSD.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperTotalPaksSD.setUnits("packets")
_RttMonLatestRtpOperTotalPaksDS_Type = Gauge32
_RttMonLatestRtpOperTotalPaksDS_Object = MibTableColumn
rttMonLatestRtpOperTotalPaksDS = _RttMonLatestRtpOperTotalPaksDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 3, 1, 25),
    _RttMonLatestRtpOperTotalPaksDS_Type()
)
rttMonLatestRtpOperTotalPaksDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperTotalPaksDS.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRtpOperTotalPaksDS.setUnits("packets")
_CiscoRttMonRtpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoRttMonRtpMIBNotifs = _CiscoRttMonRtpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 487, 0)
)
_CiscoRttMonRtpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRttMonRtpMIBObjects = _CiscoRttMonRtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 487, 1)
)
_CiscoRttMonRtpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoRttMonRtpMIBConformance = _CiscoRttMonRtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 487, 2)
)
_CiscoRttMonRtpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoRttMonRtpMIBCompliances = _CiscoRttMonRtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 1)
)
_CiscoRttMonRtpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoRttMonRtpMIBGroups = _CiscoRttMonRtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 2)
)

# Managed Objects groups

ciscoRttMonRtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 2, 1)
)
ciscoRttMonRtpGroup.setObjects(
      *(("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperRTT"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperIAJitterDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketLossDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketLateDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketEarlyDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketOOSDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperFrameLossDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperRFactorDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMOSCQDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMOSLQDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperSense"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpErrorSenseDescription"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRTTAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRTTMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRTTMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterDSAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterDSMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterDSMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossDSAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossDSMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossDSMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLateDSAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketEarlyDSAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketOOSDSAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsFrameLossDSAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsFrameLossDSMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsFrameLossDSMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorDSAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorDSMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorDSMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQDSAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQDSMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQDSMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSLQDSAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSLQDSMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSLQDSMax"))
)
if mibBuilder.loadTexts:
    ciscoRttMonRtpGroup.setStatus("current")

ciscoRttMonRtpGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 2, 2)
)
ciscoRttMonRtpGroupRev1.setObjects(
      *(("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperIAJitterSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketLossSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperPacketsMIA"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperRFactorSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMOSCQSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMinOWSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMaxOWSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperAvgOWSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMinOWDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperMaxOWDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperAvgOWDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperTotalPaksSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonLatestRtpOperTotalPaksDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterSDAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterSDMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsIAJitterSDMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossSDAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossSDMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketLossSDMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsPacketsMIAAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorSDAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorSDMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsRFactorSDMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQSDAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQSDMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsMOSCQSDMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperAvgOWSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMinOWSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMaxOWSD"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperAvgOWDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMinOWDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsOperMaxOWDS"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsSDAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsSDMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsSDMax"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsDSAvg"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsDSMin"),
        ("CISCO-RTTMON-RTP-MIB", "rttMonRtpStatsTotalPacketsDSMax"))
)
if mibBuilder.loadTexts:
    ciscoRttMonRtpGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoRttMonRtpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 487, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRttMonRtpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RTTMON-RTP-MIB",
    **{"rttMonRtpStatsTable": rttMonRtpStatsTable,
       "rttMonRtpStatsEntry": rttMonRtpStatsEntry,
       "rttMonRtpStatsStartTimeIndex": rttMonRtpStatsStartTimeIndex,
       "rttMonRtpStatsRTTAvg": rttMonRtpStatsRTTAvg,
       "rttMonRtpStatsRTTMin": rttMonRtpStatsRTTMin,
       "rttMonRtpStatsRTTMax": rttMonRtpStatsRTTMax,
       "rttMonRtpStatsIAJitterDSAvg": rttMonRtpStatsIAJitterDSAvg,
       "rttMonRtpStatsIAJitterDSMin": rttMonRtpStatsIAJitterDSMin,
       "rttMonRtpStatsIAJitterDSMax": rttMonRtpStatsIAJitterDSMax,
       "rttMonRtpStatsPacketLossDSAvg": rttMonRtpStatsPacketLossDSAvg,
       "rttMonRtpStatsPacketLossDSMin": rttMonRtpStatsPacketLossDSMin,
       "rttMonRtpStatsPacketLossDSMax": rttMonRtpStatsPacketLossDSMax,
       "rttMonRtpStatsPacketLateDSAvg": rttMonRtpStatsPacketLateDSAvg,
       "rttMonRtpStatsPacketEarlyDSAvg": rttMonRtpStatsPacketEarlyDSAvg,
       "rttMonRtpStatsPacketOOSDSAvg": rttMonRtpStatsPacketOOSDSAvg,
       "rttMonRtpStatsFrameLossDSAvg": rttMonRtpStatsFrameLossDSAvg,
       "rttMonRtpStatsFrameLossDSMin": rttMonRtpStatsFrameLossDSMin,
       "rttMonRtpStatsFrameLossDSMax": rttMonRtpStatsFrameLossDSMax,
       "rttMonRtpStatsRFactorDSAvg": rttMonRtpStatsRFactorDSAvg,
       "rttMonRtpStatsRFactorDSMin": rttMonRtpStatsRFactorDSMin,
       "rttMonRtpStatsRFactorDSMax": rttMonRtpStatsRFactorDSMax,
       "rttMonRtpStatsMOSCQDSAvg": rttMonRtpStatsMOSCQDSAvg,
       "rttMonRtpStatsMOSCQDSMin": rttMonRtpStatsMOSCQDSMin,
       "rttMonRtpStatsMOSCQDSMax": rttMonRtpStatsMOSCQDSMax,
       "rttMonRtpStatsMOSLQDSAvg": rttMonRtpStatsMOSLQDSAvg,
       "rttMonRtpStatsMOSLQDSMin": rttMonRtpStatsMOSLQDSMin,
       "rttMonRtpStatsMOSLQDSMax": rttMonRtpStatsMOSLQDSMax,
       "rttMonRtpStatsIAJitterSDAvg": rttMonRtpStatsIAJitterSDAvg,
       "rttMonRtpStatsIAJitterSDMin": rttMonRtpStatsIAJitterSDMin,
       "rttMonRtpStatsIAJitterSDMax": rttMonRtpStatsIAJitterSDMax,
       "rttMonRtpStatsPacketLossSDAvg": rttMonRtpStatsPacketLossSDAvg,
       "rttMonRtpStatsPacketLossSDMin": rttMonRtpStatsPacketLossSDMin,
       "rttMonRtpStatsPacketLossSDMax": rttMonRtpStatsPacketLossSDMax,
       "rttMonRtpStatsPacketsMIAAvg": rttMonRtpStatsPacketsMIAAvg,
       "rttMonRtpStatsRFactorSDAvg": rttMonRtpStatsRFactorSDAvg,
       "rttMonRtpStatsRFactorSDMin": rttMonRtpStatsRFactorSDMin,
       "rttMonRtpStatsRFactorSDMax": rttMonRtpStatsRFactorSDMax,
       "rttMonRtpStatsMOSCQSDAvg": rttMonRtpStatsMOSCQSDAvg,
       "rttMonRtpStatsMOSCQSDMin": rttMonRtpStatsMOSCQSDMin,
       "rttMonRtpStatsMOSCQSDMax": rttMonRtpStatsMOSCQSDMax,
       "rttMonRtpStatsOperAvgOWSD": rttMonRtpStatsOperAvgOWSD,
       "rttMonRtpStatsOperMinOWSD": rttMonRtpStatsOperMinOWSD,
       "rttMonRtpStatsOperMaxOWSD": rttMonRtpStatsOperMaxOWSD,
       "rttMonRtpStatsOperAvgOWDS": rttMonRtpStatsOperAvgOWDS,
       "rttMonRtpStatsOperMinOWDS": rttMonRtpStatsOperMinOWDS,
       "rttMonRtpStatsOperMaxOWDS": rttMonRtpStatsOperMaxOWDS,
       "rttMonRtpStatsTotalPacketsSDAvg": rttMonRtpStatsTotalPacketsSDAvg,
       "rttMonRtpStatsTotalPacketsSDMin": rttMonRtpStatsTotalPacketsSDMin,
       "rttMonRtpStatsTotalPacketsSDMax": rttMonRtpStatsTotalPacketsSDMax,
       "rttMonRtpStatsTotalPacketsDSAvg": rttMonRtpStatsTotalPacketsDSAvg,
       "rttMonRtpStatsTotalPacketsDSMax": rttMonRtpStatsTotalPacketsDSMax,
       "rttMonRtpStatsTotalPacketsDSMin": rttMonRtpStatsTotalPacketsDSMin,
       "rttMonLatestRtpOperTable": rttMonLatestRtpOperTable,
       "rttMonLatestRtpOperEntry": rttMonLatestRtpOperEntry,
       "rttMonLatestRtpOperRTT": rttMonLatestRtpOperRTT,
       "rttMonLatestRtpOperIAJitterDS": rttMonLatestRtpOperIAJitterDS,
       "rttMonLatestRtpOperPacketLossDS": rttMonLatestRtpOperPacketLossDS,
       "rttMonLatestRtpOperPacketLateDS": rttMonLatestRtpOperPacketLateDS,
       "rttMonLatestRtpOperPacketEarlyDS": rttMonLatestRtpOperPacketEarlyDS,
       "rttMonLatestRtpOperPacketOOSDS": rttMonLatestRtpOperPacketOOSDS,
       "rttMonLatestRtpOperFrameLossDS": rttMonLatestRtpOperFrameLossDS,
       "rttMonLatestRtpOperRFactorDS": rttMonLatestRtpOperRFactorDS,
       "rttMonLatestRtpOperMOSCQDS": rttMonLatestRtpOperMOSCQDS,
       "rttMonLatestRtpOperMOSLQDS": rttMonLatestRtpOperMOSLQDS,
       "rttMonLatestRtpOperSense": rttMonLatestRtpOperSense,
       "rttMonLatestRtpErrorSenseDescription": rttMonLatestRtpErrorSenseDescription,
       "rttMonLatestRtpOperIAJitterSD": rttMonLatestRtpOperIAJitterSD,
       "rttMonLatestRtpOperPacketLossSD": rttMonLatestRtpOperPacketLossSD,
       "rttMonLatestRtpOperPacketsMIA": rttMonLatestRtpOperPacketsMIA,
       "rttMonLatestRtpOperRFactorSD": rttMonLatestRtpOperRFactorSD,
       "rttMonLatestRtpOperMOSCQSD": rttMonLatestRtpOperMOSCQSD,
       "rttMonLatestRtpOperMinOWSD": rttMonLatestRtpOperMinOWSD,
       "rttMonLatestRtpOperMaxOWSD": rttMonLatestRtpOperMaxOWSD,
       "rttMonLatestRtpOperAvgOWSD": rttMonLatestRtpOperAvgOWSD,
       "rttMonLatestRtpOperMinOWDS": rttMonLatestRtpOperMinOWDS,
       "rttMonLatestRtpOperMaxOWDS": rttMonLatestRtpOperMaxOWDS,
       "rttMonLatestRtpOperAvgOWDS": rttMonLatestRtpOperAvgOWDS,
       "rttMonLatestRtpOperTotalPaksSD": rttMonLatestRtpOperTotalPaksSD,
       "rttMonLatestRtpOperTotalPaksDS": rttMonLatestRtpOperTotalPaksDS,
       "ciscoRttMonRtpMIB": ciscoRttMonRtpMIB,
       "ciscoRttMonRtpMIBNotifs": ciscoRttMonRtpMIBNotifs,
       "ciscoRttMonRtpMIBObjects": ciscoRttMonRtpMIBObjects,
       "ciscoRttMonRtpMIBConformance": ciscoRttMonRtpMIBConformance,
       "ciscoRttMonRtpMIBCompliances": ciscoRttMonRtpMIBCompliances,
       "ciscoRttMonRtpMIBCompliance": ciscoRttMonRtpMIBCompliance,
       "ciscoRttMonRtpMIBGroups": ciscoRttMonRtpMIBGroups,
       "ciscoRttMonRtpGroup": ciscoRttMonRtpGroup,
       "ciscoRttMonRtpGroupRev1": ciscoRttMonRtpGroupRev1}
)
