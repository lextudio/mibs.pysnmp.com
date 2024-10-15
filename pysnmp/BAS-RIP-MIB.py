# SNMP MIB module (BAS-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-RIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:32 2024
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

(basRip,) = mibBuilder.importSymbols(
    "BAS-MIB",
    "basRip")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

basRIP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RipIfStatsCurGroup_ObjectIdentity = ObjectIdentity
ripIfStatsCurGroup = _RipIfStatsCurGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1)
)
_RipIfResetTime_Type = TimeTicks
_RipIfResetTime_Object = MibScalar
ripIfResetTime = _RipIfResetTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 1),
    _RipIfResetTime_Type()
)
ripIfResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfResetTime.setStatus("current")
_RipIfStatsIntfCnt_Type = Counter32
_RipIfStatsIntfCnt_Object = MibScalar
ripIfStatsIntfCnt = _RipIfStatsIntfCnt_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 2),
    _RipIfStatsIntfCnt_Type()
)
ripIfStatsIntfCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsIntfCnt.setStatus("current")
_RipIfStatsNbrCnt_Type = Counter32
_RipIfStatsNbrCnt_Object = MibScalar
ripIfStatsNbrCnt = _RipIfStatsNbrCnt_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 3),
    _RipIfStatsNbrCnt_Type()
)
ripIfStatsNbrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsNbrCnt.setStatus("current")
_RipIfStatsPktsRcvd_Type = Counter32
_RipIfStatsPktsRcvd_Object = MibScalar
ripIfStatsPktsRcvd = _RipIfStatsPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 4),
    _RipIfStatsPktsRcvd_Type()
)
ripIfStatsPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsPktsRcvd.setStatus("current")
_RipIfStatsPktsSent_Type = Counter32
_RipIfStatsPktsSent_Object = MibScalar
ripIfStatsPktsSent = _RipIfStatsPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 5),
    _RipIfStatsPktsSent_Type()
)
ripIfStatsPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsPktsSent.setStatus("current")
_RipIfStatsReqsRcvd_Type = Counter32
_RipIfStatsReqsRcvd_Object = MibScalar
ripIfStatsReqsRcvd = _RipIfStatsReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 6),
    _RipIfStatsReqsRcvd_Type()
)
ripIfStatsReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsReqsRcvd.setStatus("current")
_RipIfStatsReqsSent_Type = Counter32
_RipIfStatsReqsSent_Object = MibScalar
ripIfStatsReqsSent = _RipIfStatsReqsSent_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 7),
    _RipIfStatsReqsSent_Type()
)
ripIfStatsReqsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsReqsSent.setStatus("current")
_RipIfStatsRspsRcvd_Type = Counter32
_RipIfStatsRspsRcvd_Object = MibScalar
ripIfStatsRspsRcvd = _RipIfStatsRspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 8),
    _RipIfStatsRspsRcvd_Type()
)
ripIfStatsRspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsRspsRcvd.setStatus("current")
_RipIfStatsRspsSent_Type = Counter32
_RipIfStatsRspsSent_Object = MibScalar
ripIfStatsRspsSent = _RipIfStatsRspsSent_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 9),
    _RipIfStatsRspsSent_Type()
)
ripIfStatsRspsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsRspsSent.setStatus("current")
_RipIfStatsRteTimouts_Type = Counter32
_RipIfStatsRteTimouts_Object = MibScalar
ripIfStatsRteTimouts = _RipIfStatsRteTimouts_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 10),
    _RipIfStatsRteTimouts_Type()
)
ripIfStatsRteTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsRteTimouts.setStatus("current")
_RipIfStatsShrtPktsRcvd_Type = Counter32
_RipIfStatsShrtPktsRcvd_Object = MibScalar
ripIfStatsShrtPktsRcvd = _RipIfStatsShrtPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 11),
    _RipIfStatsShrtPktsRcvd_Type()
)
ripIfStatsShrtPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsShrtPktsRcvd.setStatus("current")
_RipIfStatsBadVerRcvd_Type = Counter32
_RipIfStatsBadVerRcvd_Object = MibScalar
ripIfStatsBadVerRcvd = _RipIfStatsBadVerRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 12),
    _RipIfStatsBadVerRcvd_Type()
)
ripIfStatsBadVerRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsBadVerRcvd.setStatus("current")
_RipIfStatsBadZeroRcvd_Type = Counter32
_RipIfStatsBadZeroRcvd_Object = MibScalar
ripIfStatsBadZeroRcvd = _RipIfStatsBadZeroRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 13),
    _RipIfStatsBadZeroRcvd_Type()
)
ripIfStatsBadZeroRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsBadZeroRcvd.setStatus("current")
_RipIfStatsBadSrcPortRcvd_Type = Counter32
_RipIfStatsBadSrcPortRcvd_Object = MibScalar
ripIfStatsBadSrcPortRcvd = _RipIfStatsBadSrcPortRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 14),
    _RipIfStatsBadSrcPortRcvd_Type()
)
ripIfStatsBadSrcPortRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsBadSrcPortRcvd.setStatus("current")
_RipIfStatsBadSrcIpRcvd_Type = Counter32
_RipIfStatsBadSrcIpRcvd_Object = MibScalar
ripIfStatsBadSrcIpRcvd = _RipIfStatsBadSrcIpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 15),
    _RipIfStatsBadSrcIpRcvd_Type()
)
ripIfStatsBadSrcIpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsBadSrcIpRcvd.setStatus("current")
_RipIfStatsPktsFrmSelfRcvd_Type = Counter32
_RipIfStatsPktsFrmSelfRcvd_Object = MibScalar
ripIfStatsPktsFrmSelfRcvd = _RipIfStatsPktsFrmSelfRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 16),
    _RipIfStatsPktsFrmSelfRcvd_Type()
)
ripIfStatsPktsFrmSelfRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfStatsPktsFrmSelfRcvd.setStatus("current")
_RipIfStatsReset_Type = TruthValue
_RipIfStatsReset_Object = MibScalar
ripIfStatsReset = _RipIfStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 1, 17),
    _RipIfStatsReset_Type()
)
ripIfStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfStatsReset.setStatus("current")
_RipIfStatsAllGroup_ObjectIdentity = ObjectIdentity
ripIfStatsAllGroup = _RipIfStatsAllGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2)
)
_RipIfAllResetTime_Type = TimeTicks
_RipIfAllResetTime_Object = MibScalar
ripIfAllResetTime = _RipIfAllResetTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 1),
    _RipIfAllResetTime_Type()
)
ripIfAllResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllResetTime.setStatus("current")
_RipIfAllStatsIntfCnt_Type = Counter32
_RipIfAllStatsIntfCnt_Object = MibScalar
ripIfAllStatsIntfCnt = _RipIfAllStatsIntfCnt_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 2),
    _RipIfAllStatsIntfCnt_Type()
)
ripIfAllStatsIntfCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsIntfCnt.setStatus("current")
_RipIfAllStatsNbrCnt_Type = Counter32
_RipIfAllStatsNbrCnt_Object = MibScalar
ripIfAllStatsNbrCnt = _RipIfAllStatsNbrCnt_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 3),
    _RipIfAllStatsNbrCnt_Type()
)
ripIfAllStatsNbrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsNbrCnt.setStatus("current")
_RipIfAllStatsPktsRcvd_Type = Counter32
_RipIfAllStatsPktsRcvd_Object = MibScalar
ripIfAllStatsPktsRcvd = _RipIfAllStatsPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 4),
    _RipIfAllStatsPktsRcvd_Type()
)
ripIfAllStatsPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsPktsRcvd.setStatus("current")
_RipIfAllStatsPktsSent_Type = Counter32
_RipIfAllStatsPktsSent_Object = MibScalar
ripIfAllStatsPktsSent = _RipIfAllStatsPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 5),
    _RipIfAllStatsPktsSent_Type()
)
ripIfAllStatsPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsPktsSent.setStatus("current")
_RipIfAllStatsReqsRcvd_Type = Counter32
_RipIfAllStatsReqsRcvd_Object = MibScalar
ripIfAllStatsReqsRcvd = _RipIfAllStatsReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 6),
    _RipIfAllStatsReqsRcvd_Type()
)
ripIfAllStatsReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsReqsRcvd.setStatus("current")
_RipIfAllStatsReqsSent_Type = Counter32
_RipIfAllStatsReqsSent_Object = MibScalar
ripIfAllStatsReqsSent = _RipIfAllStatsReqsSent_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 7),
    _RipIfAllStatsReqsSent_Type()
)
ripIfAllStatsReqsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsReqsSent.setStatus("current")
_RipIfAllStatsRspsRcvd_Type = Counter32
_RipIfAllStatsRspsRcvd_Object = MibScalar
ripIfAllStatsRspsRcvd = _RipIfAllStatsRspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 8),
    _RipIfAllStatsRspsRcvd_Type()
)
ripIfAllStatsRspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsRspsRcvd.setStatus("current")
_RipIfAllStatsRspsSent_Type = Counter32
_RipIfAllStatsRspsSent_Object = MibScalar
ripIfAllStatsRspsSent = _RipIfAllStatsRspsSent_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 9),
    _RipIfAllStatsRspsSent_Type()
)
ripIfAllStatsRspsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsRspsSent.setStatus("current")
_RipIfAllStatsRteTimouts_Type = Counter32
_RipIfAllStatsRteTimouts_Object = MibScalar
ripIfAllStatsRteTimouts = _RipIfAllStatsRteTimouts_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 10),
    _RipIfAllStatsRteTimouts_Type()
)
ripIfAllStatsRteTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsRteTimouts.setStatus("current")
_RipIfAllStatsShrtPktsRcvd_Type = Counter32
_RipIfAllStatsShrtPktsRcvd_Object = MibScalar
ripIfAllStatsShrtPktsRcvd = _RipIfAllStatsShrtPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 11),
    _RipIfAllStatsShrtPktsRcvd_Type()
)
ripIfAllStatsShrtPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsShrtPktsRcvd.setStatus("current")
_RipIfAllStatsBadVerRcvd_Type = Counter32
_RipIfAllStatsBadVerRcvd_Object = MibScalar
ripIfAllStatsBadVerRcvd = _RipIfAllStatsBadVerRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 12),
    _RipIfAllStatsBadVerRcvd_Type()
)
ripIfAllStatsBadVerRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsBadVerRcvd.setStatus("current")
_RipIfAllStatsBadZeroRcvd_Type = Counter32
_RipIfAllStatsBadZeroRcvd_Object = MibScalar
ripIfAllStatsBadZeroRcvd = _RipIfAllStatsBadZeroRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 13),
    _RipIfAllStatsBadZeroRcvd_Type()
)
ripIfAllStatsBadZeroRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsBadZeroRcvd.setStatus("current")
_RipIfAllStatsBadSrcPortRcvd_Type = Counter32
_RipIfAllStatsBadSrcPortRcvd_Object = MibScalar
ripIfAllStatsBadSrcPortRcvd = _RipIfAllStatsBadSrcPortRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 14),
    _RipIfAllStatsBadSrcPortRcvd_Type()
)
ripIfAllStatsBadSrcPortRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsBadSrcPortRcvd.setStatus("current")
_RipIfAllStatsBadSrcIpRcvd_Type = Counter32
_RipIfAllStatsBadSrcIpRcvd_Object = MibScalar
ripIfAllStatsBadSrcIpRcvd = _RipIfAllStatsBadSrcIpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 15),
    _RipIfAllStatsBadSrcIpRcvd_Type()
)
ripIfAllStatsBadSrcIpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsBadSrcIpRcvd.setStatus("current")
_RipIfAllStatsPktsFrmSelfRcvd_Type = Counter32
_RipIfAllStatsPktsFrmSelfRcvd_Object = MibScalar
ripIfAllStatsPktsFrmSelfRcvd = _RipIfAllStatsPktsFrmSelfRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 2, 16),
    _RipIfAllStatsPktsFrmSelfRcvd_Type()
)
ripIfAllStatsPktsFrmSelfRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfAllStatsPktsFrmSelfRcvd.setStatus("current")
_BasRipNbrTable_Object = MibTable
basRipNbrTable = _BasRipNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 3)
)
if mibBuilder.loadTexts:
    basRipNbrTable.setStatus("current")
_BasRipNbrEntry_Object = MibTableRow
basRipNbrEntry = _BasRipNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 3, 1)
)
basRipNbrEntry.setIndexNames(
    (0, "BAS-RIP-MIB", "ripNbrIfIpAddr"),
    (0, "BAS-RIP-MIB", "ripNbrIpAddr"),
)
if mibBuilder.loadTexts:
    basRipNbrEntry.setStatus("current")
_RipNbrIfIpAddr_Type = IpAddress
_RipNbrIfIpAddr_Object = MibTableColumn
ripNbrIfIpAddr = _RipNbrIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 3, 1, 1),
    _RipNbrIfIpAddr_Type()
)
ripNbrIfIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ripNbrIfIpAddr.setStatus("current")
_RipNbrIpAddr_Type = IpAddress
_RipNbrIpAddr_Object = MibTableColumn
ripNbrIpAddr = _RipNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 3, 1, 2),
    _RipNbrIpAddr_Type()
)
ripNbrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ripNbrIpAddr.setStatus("current")
_RipNbrAddressLessIf_Type = Integer32
_RipNbrAddressLessIf_Object = MibTableColumn
ripNbrAddressLessIf = _RipNbrAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 3, 1, 3),
    _RipNbrAddressLessIf_Type()
)
ripNbrAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNbrAddressLessIf.setStatus("current")


class _RipNbrType_Type(Integer32):
    """Custom type ripNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ripNbrTypeConfigured", 1),
          ("ripNbrTypeDiscovered", 2))
    )


_RipNbrType_Type.__name__ = "Integer32"
_RipNbrType_Object = MibTableColumn
ripNbrType = _RipNbrType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 3, 1, 4),
    _RipNbrType_Type()
)
ripNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNbrType.setStatus("current")
_RipNbrLastUpdate_Type = Counter32
_RipNbrLastUpdate_Object = MibTableColumn
ripNbrLastUpdate = _RipNbrLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 3, 1, 5),
    _RipNbrLastUpdate_Type()
)
ripNbrLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNbrLastUpdate.setStatus("current")
_RipNbrTriggerMode_Type = Integer32
_RipNbrTriggerMode_Object = MibTableColumn
ripNbrTriggerMode = _RipNbrTriggerMode_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 3, 1, 6),
    _RipNbrTriggerMode_Type()
)
ripNbrTriggerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripNbrTriggerMode.setStatus("current")
_RipNbrRowStatus_Type = RowStatus
_RipNbrRowStatus_Object = MibTableColumn
ripNbrRowStatus = _RipNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 3, 1, 7),
    _RipNbrRowStatus_Type()
)
ripNbrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripNbrRowStatus.setStatus("current")
_BasRipIfTable_Object = MibTable
basRipIfTable = _BasRipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4)
)
if mibBuilder.loadTexts:
    basRipIfTable.setStatus("current")
_BasRipIfEntry_Object = MibTableRow
basRipIfEntry = _BasRipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1)
)
basRipIfEntry.setIndexNames(
    (0, "BAS-RIP-MIB", "ripIfIpAddress"),
    (0, "BAS-RIP-MIB", "ripIfAddressLessIf"),
)
if mibBuilder.loadTexts:
    basRipIfEntry.setStatus("current")
_RipIfIpAddress_Type = IpAddress
_RipIfIpAddress_Object = MibTableColumn
ripIfIpAddress = _RipIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 1),
    _RipIfIpAddress_Type()
)
ripIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfIpAddress.setStatus("current")
_RipIfAddressLessIf_Type = Integer32
_RipIfAddressLessIf_Object = MibTableColumn
ripIfAddressLessIf = _RipIfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 2),
    _RipIfAddressLessIf_Type()
)
ripIfAddressLessIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfAddressLessIf.setStatus("current")


class _RipIfType_Type(Integer32):
    """Custom type ripIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ripIfTypeBroadcast", 1),
          ("ripIfTypeNBMA", 2),
          ("ripIfTypePointToPoint", 3))
    )


_RipIfType_Type.__name__ = "Integer32"
_RipIfType_Object = MibTableColumn
ripIfType = _RipIfType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 3),
    _RipIfType_Type()
)
ripIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfType.setStatus("current")


class _RipIfVersion_Type(Integer32):
    """Custom type ripIfVersion based on Integer32"""
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
        *(("ripSendCompat", 3),
          ("ripSendNone", 1),
          ("ripSendVer1", 2),
          ("ripSendVer1Demand", 5),
          ("ripSendVer2", 4),
          ("ripSendVer2Demand", 6))
    )


_RipIfVersion_Type.__name__ = "Integer32"
_RipIfVersion_Object = MibTableColumn
ripIfVersion = _RipIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 4),
    _RipIfVersion_Type()
)
ripIfVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfVersion.setStatus("current")


class _RipIfRecvVer_Type(Integer32):
    """Custom type ripIfRecvVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ripRcvNone", 4),
          ("ripRcvVer1", 1),
          ("ripRcvVer1and2", 3),
          ("ripRcvVer2", 2))
    )


_RipIfRecvVer_Type.__name__ = "Integer32"
_RipIfRecvVer_Object = MibTableColumn
ripIfRecvVer = _RipIfRecvVer_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 5),
    _RipIfRecvVer_Type()
)
ripIfRecvVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfRecvVer.setStatus("current")
_RipIfMetric_Type = Integer32
_RipIfMetric_Object = MibTableColumn
ripIfMetric = _RipIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 6),
    _RipIfMetric_Type()
)
ripIfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfMetric.setStatus("current")
_RipIfAcceptDefault_Type = TruthValue
_RipIfAcceptDefault_Object = MibTableColumn
ripIfAcceptDefault = _RipIfAcceptDefault_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 7),
    _RipIfAcceptDefault_Type()
)
ripIfAcceptDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfAcceptDefault.setStatus("current")
_RipIfSilent_Type = TruthValue
_RipIfSilent_Object = MibTableColumn
ripIfSilent = _RipIfSilent_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 8),
    _RipIfSilent_Type()
)
ripIfSilent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfSilent.setStatus("current")
_RipIfRecvRoutes_Type = TruthValue
_RipIfRecvRoutes_Object = MibTableColumn
ripIfRecvRoutes = _RipIfRecvRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 9),
    _RipIfRecvRoutes_Type()
)
ripIfRecvRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfRecvRoutes.setStatus("current")
_RipIfSubnetsOnly_Type = TruthValue
_RipIfSubnetsOnly_Object = MibTableColumn
ripIfSubnetsOnly = _RipIfSubnetsOnly_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 10),
    _RipIfSubnetsOnly_Type()
)
ripIfSubnetsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfSubnetsOnly.setStatus("current")
_RipIfSendDefaultOnly_Type = TruthValue
_RipIfSendDefaultOnly_Object = MibTableColumn
ripIfSendDefaultOnly = _RipIfSendDefaultOnly_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 11),
    _RipIfSendDefaultOnly_Type()
)
ripIfSendDefaultOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfSendDefaultOnly.setStatus("current")
_RipIfSendDefaultAlso_Type = TruthValue
_RipIfSendDefaultAlso_Object = MibTableColumn
ripIfSendDefaultAlso = _RipIfSendDefaultAlso_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 12),
    _RipIfSendDefaultAlso_Type()
)
ripIfSendDefaultAlso.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfSendDefaultAlso.setStatus("current")
_RipIfDfltRouteMetric_Type = Integer32
_RipIfDfltRouteMetric_Object = MibTableColumn
ripIfDfltRouteMetric = _RipIfDfltRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 13),
    _RipIfDfltRouteMetric_Type()
)
ripIfDfltRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfDfltRouteMetric.setStatus("current")
_RipIfSplitHorizon_Type = TruthValue
_RipIfSplitHorizon_Object = MibTableColumn
ripIfSplitHorizon = _RipIfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 14),
    _RipIfSplitHorizon_Type()
)
ripIfSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfSplitHorizon.setStatus("current")
_RipIfPoison_Type = TruthValue
_RipIfPoison_Object = MibTableColumn
ripIfPoison = _RipIfPoison_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 15),
    _RipIfPoison_Type()
)
ripIfPoison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfPoison.setStatus("current")
_RipIfFlash_Type = TruthValue
_RipIfFlash_Object = MibTableColumn
ripIfFlash = _RipIfFlash_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 16),
    _RipIfFlash_Type()
)
ripIfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfFlash.setStatus("current")
_RipAuthOn_Type = TruthValue
_RipAuthOn_Object = MibTableColumn
ripAuthOn = _RipAuthOn_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 17),
    _RipAuthOn_Type()
)
ripAuthOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripAuthOn.setStatus("current")


class _RipIfAuthType_Type(Integer32):
    """Custom type ripIfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("noAuthentication", 1),
          ("simplePassword", 2))
    )


_RipIfAuthType_Type.__name__ = "Integer32"
_RipIfAuthType_Object = MibTableColumn
ripIfAuthType = _RipIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 18),
    _RipIfAuthType_Type()
)
ripIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfAuthType.setStatus("current")
_RipIfAuthKeyId_Type = Integer32
_RipIfAuthKeyId_Object = MibTableColumn
ripIfAuthKeyId = _RipIfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 19),
    _RipIfAuthKeyId_Type()
)
ripIfAuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfAuthKeyId.setStatus("current")


class _RipIfAuthKey_Type(OctetString):
    """Custom type ripIfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RipIfAuthKey_Type.__name__ = "OctetString"
_RipIfAuthKey_Object = MibTableColumn
ripIfAuthKey = _RipIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 20),
    _RipIfAuthKey_Type()
)
ripIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfAuthKey.setStatus("current")
_RipIfUpdateInterval_Type = Integer32
_RipIfUpdateInterval_Object = MibTableColumn
ripIfUpdateInterval = _RipIfUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 21),
    _RipIfUpdateInterval_Type()
)
ripIfUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfUpdateInterval.setStatus("current")
_RipIfUpdateInterPktGap_Type = Integer32
_RipIfUpdateInterPktGap_Object = MibTableColumn
ripIfUpdateInterPktGap = _RipIfUpdateInterPktGap_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 22),
    _RipIfUpdateInterPktGap_Type()
)
ripIfUpdateInterPktGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfUpdateInterPktGap.setStatus("current")
_RipIfPktsPerUpdate_Type = Integer32
_RipIfPktsPerUpdate_Object = MibTableColumn
ripIfPktsPerUpdate = _RipIfPktsPerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 23),
    _RipIfPktsPerUpdate_Type()
)
ripIfPktsPerUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfPktsPerUpdate.setStatus("current")
_RipIfPortDown_Type = TruthValue
_RipIfPortDown_Object = MibTableColumn
ripIfPortDown = _RipIfPortDown_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 24),
    _RipIfPortDown_Type()
)
ripIfPortDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfPortDown.setStatus("current")
_RipIfRowStat_Type = RowStatus
_RipIfRowStat_Object = MibTableColumn
ripIfRowStat = _RipIfRowStat_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 19, 1, 4, 1, 25),
    _RipIfRowStat_Type()
)
ripIfRowStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripIfRowStat.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-RIP-MIB",
    **{"basRIP": basRIP,
       "ripIfStatsCurGroup": ripIfStatsCurGroup,
       "ripIfResetTime": ripIfResetTime,
       "ripIfStatsIntfCnt": ripIfStatsIntfCnt,
       "ripIfStatsNbrCnt": ripIfStatsNbrCnt,
       "ripIfStatsPktsRcvd": ripIfStatsPktsRcvd,
       "ripIfStatsPktsSent": ripIfStatsPktsSent,
       "ripIfStatsReqsRcvd": ripIfStatsReqsRcvd,
       "ripIfStatsReqsSent": ripIfStatsReqsSent,
       "ripIfStatsRspsRcvd": ripIfStatsRspsRcvd,
       "ripIfStatsRspsSent": ripIfStatsRspsSent,
       "ripIfStatsRteTimouts": ripIfStatsRteTimouts,
       "ripIfStatsShrtPktsRcvd": ripIfStatsShrtPktsRcvd,
       "ripIfStatsBadVerRcvd": ripIfStatsBadVerRcvd,
       "ripIfStatsBadZeroRcvd": ripIfStatsBadZeroRcvd,
       "ripIfStatsBadSrcPortRcvd": ripIfStatsBadSrcPortRcvd,
       "ripIfStatsBadSrcIpRcvd": ripIfStatsBadSrcIpRcvd,
       "ripIfStatsPktsFrmSelfRcvd": ripIfStatsPktsFrmSelfRcvd,
       "ripIfStatsReset": ripIfStatsReset,
       "ripIfStatsAllGroup": ripIfStatsAllGroup,
       "ripIfAllResetTime": ripIfAllResetTime,
       "ripIfAllStatsIntfCnt": ripIfAllStatsIntfCnt,
       "ripIfAllStatsNbrCnt": ripIfAllStatsNbrCnt,
       "ripIfAllStatsPktsRcvd": ripIfAllStatsPktsRcvd,
       "ripIfAllStatsPktsSent": ripIfAllStatsPktsSent,
       "ripIfAllStatsReqsRcvd": ripIfAllStatsReqsRcvd,
       "ripIfAllStatsReqsSent": ripIfAllStatsReqsSent,
       "ripIfAllStatsRspsRcvd": ripIfAllStatsRspsRcvd,
       "ripIfAllStatsRspsSent": ripIfAllStatsRspsSent,
       "ripIfAllStatsRteTimouts": ripIfAllStatsRteTimouts,
       "ripIfAllStatsShrtPktsRcvd": ripIfAllStatsShrtPktsRcvd,
       "ripIfAllStatsBadVerRcvd": ripIfAllStatsBadVerRcvd,
       "ripIfAllStatsBadZeroRcvd": ripIfAllStatsBadZeroRcvd,
       "ripIfAllStatsBadSrcPortRcvd": ripIfAllStatsBadSrcPortRcvd,
       "ripIfAllStatsBadSrcIpRcvd": ripIfAllStatsBadSrcIpRcvd,
       "ripIfAllStatsPktsFrmSelfRcvd": ripIfAllStatsPktsFrmSelfRcvd,
       "basRipNbrTable": basRipNbrTable,
       "basRipNbrEntry": basRipNbrEntry,
       "ripNbrIfIpAddr": ripNbrIfIpAddr,
       "ripNbrIpAddr": ripNbrIpAddr,
       "ripNbrAddressLessIf": ripNbrAddressLessIf,
       "ripNbrType": ripNbrType,
       "ripNbrLastUpdate": ripNbrLastUpdate,
       "ripNbrTriggerMode": ripNbrTriggerMode,
       "ripNbrRowStatus": ripNbrRowStatus,
       "basRipIfTable": basRipIfTable,
       "basRipIfEntry": basRipIfEntry,
       "ripIfIpAddress": ripIfIpAddress,
       "ripIfAddressLessIf": ripIfAddressLessIf,
       "ripIfType": ripIfType,
       "ripIfVersion": ripIfVersion,
       "ripIfRecvVer": ripIfRecvVer,
       "ripIfMetric": ripIfMetric,
       "ripIfAcceptDefault": ripIfAcceptDefault,
       "ripIfSilent": ripIfSilent,
       "ripIfRecvRoutes": ripIfRecvRoutes,
       "ripIfSubnetsOnly": ripIfSubnetsOnly,
       "ripIfSendDefaultOnly": ripIfSendDefaultOnly,
       "ripIfSendDefaultAlso": ripIfSendDefaultAlso,
       "ripIfDfltRouteMetric": ripIfDfltRouteMetric,
       "ripIfSplitHorizon": ripIfSplitHorizon,
       "ripIfPoison": ripIfPoison,
       "ripIfFlash": ripIfFlash,
       "ripAuthOn": ripAuthOn,
       "ripIfAuthType": ripIfAuthType,
       "ripIfAuthKeyId": ripIfAuthKeyId,
       "ripIfAuthKey": ripIfAuthKey,
       "ripIfUpdateInterval": ripIfUpdateInterval,
       "ripIfUpdateInterPktGap": ripIfUpdateInterPktGap,
       "ripIfPktsPerUpdate": ripIfPktsPerUpdate,
       "ripIfPortDown": ripIfPortDown,
       "ripIfRowStat": ripIfRowStat}
)
