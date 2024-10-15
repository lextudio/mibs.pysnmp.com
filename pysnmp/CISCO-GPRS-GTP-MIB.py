# SNMP MIB module (CISCO-GPRS-GTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GPRS-GTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:56 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoGprsGtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48)
)
ciscoGprsGtpMIB.setRevisions(
        ("2005-09-19 00:00",
         "2001-07-30 00:00",
         "2001-03-08 00:00",
         "1999-07-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoGprsGtpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGprsGtpMIBObjects = _CiscoGprsGtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1)
)
_CiscoGprsGtpConfig_ObjectIdentity = ObjectIdentity
ciscoGprsGtpConfig = _CiscoGprsGtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1)
)
_CgprsGtpGeneralConfig_ObjectIdentity = ObjectIdentity
cgprsGtpGeneralConfig = _CgprsGtpGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1)
)


class _CgprsGtpT3TunnelTimer_Type(Integer32):
    """Custom type cgprsGtpT3TunnelTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_CgprsGtpT3TunnelTimer_Type.__name__ = "Integer32"
_CgprsGtpT3TunnelTimer_Object = MibScalar
cgprsGtpT3TunnelTimer = _CgprsGtpT3TunnelTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1, 1),
    _CgprsGtpT3TunnelTimer_Type()
)
cgprsGtpT3TunnelTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpT3TunnelTimer.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpT3TunnelTimer.setUnits("seconds")


class _CgprsGtpT3ResponseTimer_Type(Integer32):
    """Custom type cgprsGtpT3ResponseTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CgprsGtpT3ResponseTimer_Type.__name__ = "Integer32"
_CgprsGtpT3ResponseTimer_Object = MibScalar
cgprsGtpT3ResponseTimer = _CgprsGtpT3ResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1, 2),
    _CgprsGtpT3ResponseTimer_Type()
)
cgprsGtpT3ResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpT3ResponseTimer.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpT3ResponseTimer.setUnits("seconds")


class _CgprsGtpN3Request_Type(Integer32):
    """Custom type cgprsGtpN3Request based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CgprsGtpN3Request_Type.__name__ = "Integer32"
_CgprsGtpN3Request_Object = MibScalar
cgprsGtpN3Request = _CgprsGtpN3Request_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1, 3),
    _CgprsGtpN3Request_Type()
)
cgprsGtpN3Request.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpN3Request.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpN3Request.setUnits("messages")


class _CgprsGtpN3BufferSize_Type(Integer32):
    """Custom type cgprsGtpN3BufferSize based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgprsGtpN3BufferSize_Type.__name__ = "Integer32"
_CgprsGtpN3BufferSize_Object = MibScalar
cgprsGtpN3BufferSize = _CgprsGtpN3BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1, 4),
    _CgprsGtpN3BufferSize_Type()
)
cgprsGtpN3BufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpN3BufferSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpN3BufferSize.setUnits("bytes")


class _CgprsGtpEchoRequestTimer_Type(Integer32):
    """Custom type cgprsGtpEchoRequestTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_CgprsGtpEchoRequestTimer_Type.__name__ = "Integer32"
_CgprsGtpEchoRequestTimer_Object = MibScalar
cgprsGtpEchoRequestTimer = _CgprsGtpEchoRequestTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1, 5),
    _CgprsGtpEchoRequestTimer_Type()
)
cgprsGtpEchoRequestTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpEchoRequestTimer.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpEchoRequestTimer.setUnits("seconds")


class _CgprsGtpGSNTotalBandwidthResrc_Type(Integer32):
    """Custom type cgprsGtpGSNTotalBandwidthResrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3000),
    )


_CgprsGtpGSNTotalBandwidthResrc_Type.__name__ = "Integer32"
_CgprsGtpGSNTotalBandwidthResrc_Object = MibScalar
cgprsGtpGSNTotalBandwidthResrc = _CgprsGtpGSNTotalBandwidthResrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1, 6),
    _CgprsGtpGSNTotalBandwidthResrc_Type()
)
cgprsGtpGSNTotalBandwidthResrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpGSNTotalBandwidthResrc.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpGSNTotalBandwidthResrc.setUnits("bits/sec")


class _CgprsGtpMaxNumPDPCxts_Type(Integer32):
    """Custom type cgprsGtpMaxNumPDPCxts based on Integer32"""
    defaultValue = 45000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_CgprsGtpMaxNumPDPCxts_Type.__name__ = "Integer32"
_CgprsGtpMaxNumPDPCxts_Object = MibScalar
cgprsGtpMaxNumPDPCxts = _CgprsGtpMaxNumPDPCxts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1, 7),
    _CgprsGtpMaxNumPDPCxts_Type()
)
cgprsGtpMaxNumPDPCxts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpMaxNumPDPCxts.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpMaxNumPDPCxts.setUnits("PDP contexts")


class _CgprsGtpDroppedPktsMonTime_Type(Integer32):
    """Custom type cgprsGtpDroppedPktsMonTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgprsGtpDroppedPktsMonTime_Type.__name__ = "Integer32"
_CgprsGtpDroppedPktsMonTime_Object = MibScalar
cgprsGtpDroppedPktsMonTime = _CgprsGtpDroppedPktsMonTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1, 8),
    _CgprsGtpDroppedPktsMonTime_Type()
)
cgprsGtpDroppedPktsMonTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpDroppedPktsMonTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpDroppedPktsMonTime.setUnits("seconds")


class _CgprsGtpNoRespToEchoNotifEnable_Type(TruthValue):
    """Custom type cgprsGtpNoRespToEchoNotifEnable based on TruthValue"""


_CgprsGtpNoRespToEchoNotifEnable_Object = MibScalar
cgprsGtpNoRespToEchoNotifEnable = _CgprsGtpNoRespToEchoNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1, 9),
    _CgprsGtpNoRespToEchoNotifEnable_Type()
)
cgprsGtpNoRespToEchoNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpNoRespToEchoNotifEnable.setStatus("obsolete")


class _CgprsGtpPDPCxtActRejNotifEnable_Type(TruthValue):
    """Custom type cgprsGtpPDPCxtActRejNotifEnable based on TruthValue"""


_CgprsGtpPDPCxtActRejNotifEnable_Object = MibScalar
cgprsGtpPDPCxtActRejNotifEnable = _CgprsGtpPDPCxtActRejNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 1, 10),
    _CgprsGtpPDPCxtActRejNotifEnable_Type()
)
cgprsGtpPDPCxtActRejNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpPDPCxtActRejNotifEnable.setStatus("obsolete")
_CgprsGtpGgsnConfig_ObjectIdentity = ObjectIdentity
cgprsGtpGgsnConfig = _CgprsGtpGgsnConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2)
)


class _CgprsGtpAPNAddrAllocMethodGlobDef_Type(Integer32):
    """Custom type cgprsGtpAPNAddrAllocMethodGlobDef based on Integer32"""
    defaultValue = 3

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
        *(("dhcp", 2),
          ("disable", 3),
          ("notconfig", 4),
          ("radius", 1))
    )


_CgprsGtpAPNAddrAllocMethodGlobDef_Type.__name__ = "Integer32"
_CgprsGtpAPNAddrAllocMethodGlobDef_Object = MibScalar
cgprsGtpAPNAddrAllocMethodGlobDef = _CgprsGtpAPNAddrAllocMethodGlobDef_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 1),
    _CgprsGtpAPNAddrAllocMethodGlobDef_Type()
)
cgprsGtpAPNAddrAllocMethodGlobDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsGtpAPNAddrAllocMethodGlobDef.setStatus("obsolete")
_CgprsGtpChargingGWTable_Object = MibTable
cgprsGtpChargingGWTable = _CgprsGtpChargingGWTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cgprsGtpChargingGWTable.setStatus("obsolete")
_CgprsGtpChargingGWEntry_Object = MibTableRow
cgprsGtpChargingGWEntry = _CgprsGtpChargingGWEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 2, 1)
)
cgprsGtpChargingGWEntry.setIndexNames(
    (0, "CISCO-GPRS-GTP-MIB", "cgprsGtpChargingGWid"),
)
if mibBuilder.loadTexts:
    cgprsGtpChargingGWEntry.setStatus("obsolete")
_CgprsGtpChargingGWid_Type = IpAddress
_CgprsGtpChargingGWid_Object = MibTableColumn
cgprsGtpChargingGWid = _CgprsGtpChargingGWid_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 2, 1, 1),
    _CgprsGtpChargingGWid_Type()
)
cgprsGtpChargingGWid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsGtpChargingGWid.setStatus("obsolete")
_CgprsGtpChargingGWName_Type = DisplayString
_CgprsGtpChargingGWName_Object = MibTableColumn
cgprsGtpChargingGWName = _CgprsGtpChargingGWName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 2, 1, 2),
    _CgprsGtpChargingGWName_Type()
)
cgprsGtpChargingGWName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsGtpChargingGWName.setStatus("obsolete")


class _CgprsGtpChargingGWType_Type(Integer32):
    """Custom type cgprsGtpChargingGWType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_CgprsGtpChargingGWType_Type.__name__ = "Integer32"
_CgprsGtpChargingGWType_Object = MibTableColumn
cgprsGtpChargingGWType = _CgprsGtpChargingGWType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 2, 1, 3),
    _CgprsGtpChargingGWType_Type()
)
cgprsGtpChargingGWType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsGtpChargingGWType.setStatus("obsolete")


class _CgprsGtpChargingGWOperState_Type(Integer32):
    """Custom type cgprsGtpChargingGWOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_CgprsGtpChargingGWOperState_Type.__name__ = "Integer32"
_CgprsGtpChargingGWOperState_Object = MibTableColumn
cgprsGtpChargingGWOperState = _CgprsGtpChargingGWOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 2, 1, 4),
    _CgprsGtpChargingGWOperState_Type()
)
cgprsGtpChargingGWOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpChargingGWOperState.setStatus("obsolete")


class _CgprsGtpChargingGWNotifEnable_Type(TruthValue):
    """Custom type cgprsGtpChargingGWNotifEnable based on TruthValue"""


_CgprsGtpChargingGWNotifEnable_Object = MibTableColumn
cgprsGtpChargingGWNotifEnable = _CgprsGtpChargingGWNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 2, 1, 5),
    _CgprsGtpChargingGWNotifEnable_Type()
)
cgprsGtpChargingGWNotifEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsGtpChargingGWNotifEnable.setStatus("obsolete")
_CgprsGtpChargingGWRowStatus_Type = RowStatus
_CgprsGtpChargingGWRowStatus_Object = MibTableColumn
cgprsGtpChargingGWRowStatus = _CgprsGtpChargingGWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 2, 1, 6),
    _CgprsGtpChargingGWRowStatus_Type()
)
cgprsGtpChargingGWRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsGtpChargingGWRowStatus.setStatus("obsolete")
_CgprsGtpAPNTable_Object = MibTable
cgprsGtpAPNTable = _CgprsGtpAPNTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cgprsGtpAPNTable.setStatus("obsolete")
_CgprsGtpAPNEntry_Object = MibTableRow
cgprsGtpAPNEntry = _CgprsGtpAPNEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 3, 1)
)
cgprsGtpAPNEntry.setIndexNames(
    (0, "CISCO-GPRS-GTP-MIB", "cgprsGtpAPNId"),
)
if mibBuilder.loadTexts:
    cgprsGtpAPNEntry.setStatus("obsolete")


class _CgprsGtpAPNId_Type(Integer32):
    """Custom type cgprsGtpAPNId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgprsGtpAPNId_Type.__name__ = "Integer32"
_CgprsGtpAPNId_Object = MibTableColumn
cgprsGtpAPNId = _CgprsGtpAPNId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 3, 1, 1),
    _CgprsGtpAPNId_Type()
)
cgprsGtpAPNId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsGtpAPNId.setStatus("obsolete")
_CgprsGtpAPNName_Type = DisplayString
_CgprsGtpAPNName_Object = MibTableColumn
cgprsGtpAPNName = _CgprsGtpAPNName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 3, 1, 2),
    _CgprsGtpAPNName_Type()
)
cgprsGtpAPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsGtpAPNName.setStatus("obsolete")


class _CgprsGtpAPNAddrAllocMethod_Type(Integer32):
    """Custom type cgprsGtpAPNAddrAllocMethod based on Integer32"""
    defaultValue = 3

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
        *(("dhcp", 2),
          ("disable", 3),
          ("notconfig", 4),
          ("radius", 1))
    )


_CgprsGtpAPNAddrAllocMethod_Type.__name__ = "Integer32"
_CgprsGtpAPNAddrAllocMethod_Object = MibTableColumn
cgprsGtpAPNAddrAllocMethod = _CgprsGtpAPNAddrAllocMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 3, 1, 3),
    _CgprsGtpAPNAddrAllocMethod_Type()
)
cgprsGtpAPNAddrAllocMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsGtpAPNAddrAllocMethod.setStatus("obsolete")
_CgprsGtpAPNRowStatus_Type = RowStatus
_CgprsGtpAPNRowStatus_Object = MibTableColumn
cgprsGtpAPNRowStatus = _CgprsGtpAPNRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 1, 2, 3, 1, 4),
    _CgprsGtpAPNRowStatus_Type()
)
cgprsGtpAPNRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsGtpAPNRowStatus.setStatus("obsolete")
_CiscoGprsGtpStats_ObjectIdentity = ObjectIdentity
ciscoGprsGtpStats = _CiscoGprsGtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2)
)
_CgprsGtpGeneralStats_ObjectIdentity = ObjectIdentity
cgprsGtpGeneralStats = _CgprsGtpGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1)
)
_CgprsGtpCurRxPacketQueueSize_Type = Gauge32
_CgprsGtpCurRxPacketQueueSize_Object = MibScalar
cgprsGtpCurRxPacketQueueSize = _CgprsGtpCurRxPacketQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 1),
    _CgprsGtpCurRxPacketQueueSize_Type()
)
cgprsGtpCurRxPacketQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpCurRxPacketQueueSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpCurRxPacketQueueSize.setUnits("packets")
_CgprsGtpCurActivatedPDPCxtsCnt_Type = Gauge32
_CgprsGtpCurActivatedPDPCxtsCnt_Object = MibScalar
cgprsGtpCurActivatedPDPCxtsCnt = _CgprsGtpCurActivatedPDPCxtsCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 2),
    _CgprsGtpCurActivatedPDPCxtsCnt_Type()
)
cgprsGtpCurActivatedPDPCxtsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpCurActivatedPDPCxtsCnt.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpCurActivatedPDPCxtsCnt.setUnits("PDP contexts")
_CgprsGtpCurUnexpRxGpduCnt_Type = Counter32
_CgprsGtpCurUnexpRxGpduCnt_Object = MibScalar
cgprsGtpCurUnexpRxGpduCnt = _CgprsGtpCurUnexpRxGpduCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 3),
    _CgprsGtpCurUnexpRxGpduCnt_Type()
)
cgprsGtpCurUnexpRxGpduCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpCurUnexpRxGpduCnt.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpCurUnexpRxGpduCnt.setUnits("PDUs")
_CgprsGtpCurRejPDPCxtActivationCnt_Type = Counter32
_CgprsGtpCurRejPDPCxtActivationCnt_Object = MibScalar
cgprsGtpCurRejPDPCxtActivationCnt = _CgprsGtpCurRejPDPCxtActivationCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 4),
    _CgprsGtpCurRejPDPCxtActivationCnt_Type()
)
cgprsGtpCurRejPDPCxtActivationCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpCurRejPDPCxtActivationCnt.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpCurRejPDPCxtActivationCnt.setUnits("PDP contexts")
_CgprsGtpTotalPktsDropped_Type = Counter32
_CgprsGtpTotalPktsDropped_Object = MibScalar
cgprsGtpTotalPktsDropped = _CgprsGtpTotalPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 5),
    _CgprsGtpTotalPktsDropped_Type()
)
cgprsGtpTotalPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpTotalPktsDropped.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpTotalPktsDropped.setUnits("packets")


class _CgprsGtpDroppedPktsTimeFrame_Type(Integer32):
    """Custom type cgprsGtpDroppedPktsTimeFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgprsGtpDroppedPktsTimeFrame_Type.__name__ = "Integer32"
_CgprsGtpDroppedPktsTimeFrame_Object = MibScalar
cgprsGtpDroppedPktsTimeFrame = _CgprsGtpDroppedPktsTimeFrame_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 6),
    _CgprsGtpDroppedPktsTimeFrame_Type()
)
cgprsGtpDroppedPktsTimeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpDroppedPktsTimeFrame.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpDroppedPktsTimeFrame.setUnits("seconds")
_CgprsGtpDroppedPktsCnt_Type = Counter32
_CgprsGtpDroppedPktsCnt_Object = MibScalar
cgprsGtpDroppedPktsCnt = _CgprsGtpDroppedPktsCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 7),
    _CgprsGtpDroppedPktsCnt_Type()
)
cgprsGtpDroppedPktsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpDroppedPktsCnt.setStatus("obsolete")
_CgprsGtpCurMTForPremiumQos_Type = Gauge32
_CgprsGtpCurMTForPremiumQos_Object = MibScalar
cgprsGtpCurMTForPremiumQos = _CgprsGtpCurMTForPremiumQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 8),
    _CgprsGtpCurMTForPremiumQos_Type()
)
cgprsGtpCurMTForPremiumQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpCurMTForPremiumQos.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpCurMTForPremiumQos.setUnits("bits/sec")
_CgprsGtpCurMTForNormalQos_Type = Gauge32
_CgprsGtpCurMTForNormalQos_Object = MibScalar
cgprsGtpCurMTForNormalQos = _CgprsGtpCurMTForNormalQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 9),
    _CgprsGtpCurMTForNormalQos_Type()
)
cgprsGtpCurMTForNormalQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpCurMTForNormalQos.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpCurMTForNormalQos.setUnits("bits/sec")
_CgprsGtpCurMTForBestEffortQos_Type = Gauge32
_CgprsGtpCurMTForBestEffortQos_Object = MibScalar
cgprsGtpCurMTForBestEffortQos = _CgprsGtpCurMTForBestEffortQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 10),
    _CgprsGtpCurMTForBestEffortQos_Type()
)
cgprsGtpCurMTForBestEffortQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpCurMTForBestEffortQos.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpCurMTForBestEffortQos.setUnits("bits/sec")
_CgprsGtpCurGSNBandwidthResrcUsed_Type = Gauge32
_CgprsGtpCurGSNBandwidthResrcUsed_Object = MibScalar
cgprsGtpCurGSNBandwidthResrcUsed = _CgprsGtpCurGSNBandwidthResrcUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 11),
    _CgprsGtpCurGSNBandwidthResrcUsed_Type()
)
cgprsGtpCurGSNBandwidthResrcUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpCurGSNBandwidthResrcUsed.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpCurGSNBandwidthResrcUsed.setUnits("bits/sec")
_CgprsGtpGSNTable_Object = MibTable
cgprsGtpGSNTable = _CgprsGtpGSNTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 12)
)
if mibBuilder.loadTexts:
    cgprsGtpGSNTable.setStatus("obsolete")
_CgprsGtpGSNEntry_Object = MibTableRow
cgprsGtpGSNEntry = _CgprsGtpGSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 12, 1)
)
cgprsGtpGSNEntry.setIndexNames(
    (0, "CISCO-GPRS-GTP-MIB", "cgprsGtpGSNid"),
)
if mibBuilder.loadTexts:
    cgprsGtpGSNEntry.setStatus("obsolete")
_CgprsGtpGSNid_Type = IpAddress
_CgprsGtpGSNid_Object = MibTableColumn
cgprsGtpGSNid = _CgprsGtpGSNid_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 12, 1, 1),
    _CgprsGtpGSNid_Type()
)
cgprsGtpGSNid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsGtpGSNid.setStatus("obsolete")
_CgprsGtpGSNEchoFailedNotifCnt_Type = Counter32
_CgprsGtpGSNEchoFailedNotifCnt_Object = MibTableColumn
cgprsGtpGSNEchoFailedNotifCnt = _CgprsGtpGSNEchoFailedNotifCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 1, 12, 1, 2),
    _CgprsGtpGSNEchoFailedNotifCnt_Type()
)
cgprsGtpGSNEchoFailedNotifCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpGSNEchoFailedNotifCnt.setStatus("obsolete")
_CgprsGtpGgsnStats_ObjectIdentity = ObjectIdentity
cgprsGtpGgsnStats = _CgprsGtpGgsnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 2)
)
_CgprsGtpTotalNumAllocIpAddr_Type = Gauge32
_CgprsGtpTotalNumAllocIpAddr_Object = MibScalar
cgprsGtpTotalNumAllocIpAddr = _CgprsGtpTotalNumAllocIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 2, 1),
    _CgprsGtpTotalNumAllocIpAddr_Type()
)
cgprsGtpTotalNumAllocIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpTotalNumAllocIpAddr.setStatus("obsolete")
if mibBuilder.loadTexts:
    cgprsGtpTotalNumAllocIpAddr.setUnits("allocated dynamic addreses")
_CgprsGtpChargingMsgCnt_Type = Gauge32
_CgprsGtpChargingMsgCnt_Object = MibScalar
cgprsGtpChargingMsgCnt = _CgprsGtpChargingMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 2, 2),
    _CgprsGtpChargingMsgCnt_Type()
)
cgprsGtpChargingMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpChargingMsgCnt.setStatus("obsolete")
_CgprsGtpNumAllocIpAddrTable_Object = MibTable
cgprsGtpNumAllocIpAddrTable = _CgprsGtpNumAllocIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cgprsGtpNumAllocIpAddrTable.setStatus("obsolete")
_CgprsGtpNumAllocIpAddrEntry_Object = MibTableRow
cgprsGtpNumAllocIpAddrEntry = _CgprsGtpNumAllocIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 2, 3, 1)
)
cgprsGtpNumAllocIpAddrEntry.setIndexNames(
    (0, "CISCO-GPRS-GTP-MIB", "cgprsGtpAPNId"),
)
if mibBuilder.loadTexts:
    cgprsGtpNumAllocIpAddrEntry.setStatus("obsolete")
_CgprsGtpNumAllocIpAddr_Type = Gauge32
_CgprsGtpNumAllocIpAddr_Object = MibTableColumn
cgprsGtpNumAllocIpAddr = _CgprsGtpNumAllocIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 2, 3, 1, 1),
    _CgprsGtpNumAllocIpAddr_Type()
)
cgprsGtpNumAllocIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpNumAllocIpAddr.setStatus("obsolete")
_CgprsGtpGgsnStatus_ObjectIdentity = ObjectIdentity
cgprsGtpGgsnStatus = _CgprsGtpGgsnStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 3)
)
_CgprsGtpVersion_Type = DisplayString
_CgprsGtpVersion_Object = MibScalar
cgprsGtpVersion = _CgprsGtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 3, 1),
    _CgprsGtpVersion_Type()
)
cgprsGtpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpVersion.setStatus("obsolete")
_CgprsGtpLastGSNidNoRespToEcho_Type = DisplayString
_CgprsGtpLastGSNidNoRespToEcho_Object = MibScalar
cgprsGtpLastGSNidNoRespToEcho = _CgprsGtpLastGSNidNoRespToEcho_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 3, 2),
    _CgprsGtpLastGSNidNoRespToEcho_Type()
)
cgprsGtpLastGSNidNoRespToEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpLastGSNidNoRespToEcho.setStatus("obsolete")
_CgprsGtpLastGSNidRecovered_Type = DisplayString
_CgprsGtpLastGSNidRecovered_Object = MibScalar
cgprsGtpLastGSNidRecovered = _CgprsGtpLastGSNidRecovered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 3, 3),
    _CgprsGtpLastGSNidRecovered_Type()
)
cgprsGtpLastGSNidRecovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpLastGSNidRecovered.setStatus("obsolete")
_CgprsGtpGSNidOfLastUnexpPDPCxt_Type = DisplayString
_CgprsGtpGSNidOfLastUnexpPDPCxt_Object = MibScalar
cgprsGtpGSNidOfLastUnexpPDPCxt = _CgprsGtpGSNidOfLastUnexpPDPCxt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 3, 4),
    _CgprsGtpGSNidOfLastUnexpPDPCxt_Type()
)
cgprsGtpGSNidOfLastUnexpPDPCxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpGSNidOfLastUnexpPDPCxt.setStatus("obsolete")
_CgprsGtpTIDOfLastUnexpPDPCxt_Type = DisplayString
_CgprsGtpTIDOfLastUnexpPDPCxt_Object = MibScalar
cgprsGtpTIDOfLastUnexpPDPCxt = _CgprsGtpTIDOfLastUnexpPDPCxt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 3, 5),
    _CgprsGtpTIDOfLastUnexpPDPCxt_Type()
)
cgprsGtpTIDOfLastUnexpPDPCxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpTIDOfLastUnexpPDPCxt.setStatus("obsolete")
_CgprsGtpRejReasonOfLastUnexpPDPCxt_Type = DisplayString
_CgprsGtpRejReasonOfLastUnexpPDPCxt_Object = MibScalar
cgprsGtpRejReasonOfLastUnexpPDPCxt = _CgprsGtpRejReasonOfLastUnexpPDPCxt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 1, 2, 3, 6),
    _CgprsGtpRejReasonOfLastUnexpPDPCxt_Type()
)
cgprsGtpRejReasonOfLastUnexpPDPCxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsGtpRejReasonOfLastUnexpPDPCxt.setStatus("obsolete")
_CiscoGprsGtpNotifPrefix_ObjectIdentity = ObjectIdentity
ciscoGprsGtpNotifPrefix = _CiscoGprsGtpNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 2)
)
_CiscoGprsGtpNotifs_ObjectIdentity = ObjectIdentity
ciscoGprsGtpNotifs = _CiscoGprsGtpNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 2, 0)
)
_CiscoGprsGtpConformances_ObjectIdentity = ObjectIdentity
ciscoGprsGtpConformances = _CiscoGprsGtpConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 3)
)
_CgprsGtpCompliances_ObjectIdentity = ObjectIdentity
cgprsGtpCompliances = _CgprsGtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 3, 1)
)
_CgprsGtpGroups_ObjectIdentity = ObjectIdentity
cgprsGtpGroups = _CgprsGtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 3, 2)
)

# Managed Objects groups

cgprsGtpGeneralConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 3, 2, 1)
)
cgprsGtpGeneralConfigGroup.setObjects(
      *(("CISCO-GPRS-GTP-MIB", "cgprsGtpT3TunnelTimer"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpT3ResponseTimer"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpN3Request"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpN3BufferSize"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpEchoRequestTimer"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpGSNTotalBandwidthResrc"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpMaxNumPDPCxts"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpDroppedPktsMonTime"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpNoRespToEchoNotifEnable"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpPDPCxtActRejNotifEnable"))
)
if mibBuilder.loadTexts:
    cgprsGtpGeneralConfigGroup.setStatus("obsolete")

cgprsGtpGgsnConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 3, 2, 2)
)
cgprsGtpGgsnConfigGroup.setObjects(
      *(("CISCO-GPRS-GTP-MIB", "cgprsGtpAPNAddrAllocMethodGlobDef"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpChargingGWName"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpChargingGWType"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpChargingGWOperState"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpChargingGWNotifEnable"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpChargingGWRowStatus"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpAPNName"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpAPNAddrAllocMethod"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpAPNRowStatus"))
)
if mibBuilder.loadTexts:
    cgprsGtpGgsnConfigGroup.setStatus("obsolete")

cgprsGtpGeneralStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 3, 2, 3)
)
cgprsGtpGeneralStatsGroup.setObjects(
      *(("CISCO-GPRS-GTP-MIB", "cgprsGtpCurRxPacketQueueSize"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpCurActivatedPDPCxtsCnt"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpCurUnexpRxGpduCnt"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpCurRejPDPCxtActivationCnt"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpTotalPktsDropped"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpDroppedPktsTimeFrame"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpDroppedPktsCnt"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpCurMTForPremiumQos"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpCurMTForNormalQos"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpCurMTForBestEffortQos"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpCurGSNBandwidthResrcUsed"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpGSNEchoFailedNotifCnt"))
)
if mibBuilder.loadTexts:
    cgprsGtpGeneralStatsGroup.setStatus("obsolete")

cgprsGtpGgsnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 3, 2, 4)
)
cgprsGtpGgsnStatsGroup.setObjects(
      *(("CISCO-GPRS-GTP-MIB", "cgprsGtpTotalNumAllocIpAddr"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpChargingMsgCnt"))
)
if mibBuilder.loadTexts:
    cgprsGtpGgsnStatsGroup.setStatus("obsolete")

cgprsGtpGgsnStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 3, 2, 5)
)
cgprsGtpGgsnStatusGroup.setObjects(
      *(("CISCO-GPRS-GTP-MIB", "cgprsGtpVersion"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpLastGSNidNoRespToEcho"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpLastGSNidRecovered"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpGSNidOfLastUnexpPDPCxt"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpTIDOfLastUnexpPDPCxt"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpRejReasonOfLastUnexpPDPCxt"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpNumAllocIpAddr"))
)
if mibBuilder.loadTexts:
    cgprsGtpGgsnStatusGroup.setStatus("obsolete")


# Notification objects

cgprsGtpGSNPathFailedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 2, 0, 1)
)
cgprsGtpGSNPathFailedNotif.setObjects(
    ("CISCO-GPRS-GTP-MIB", "cgprsGtpLastGSNidNoRespToEcho")
)
if mibBuilder.loadTexts:
    cgprsGtpGSNPathFailedNotif.setStatus(
        "obsolete"
    )

cgprsGtpGSNPathRecoveredNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 2, 0, 2)
)
cgprsGtpGSNPathRecoveredNotif.setObjects(
    ("CISCO-GPRS-GTP-MIB", "cgprsGtpLastGSNidRecovered")
)
if mibBuilder.loadTexts:
    cgprsGtpGSNPathRecoveredNotif.setStatus(
        "obsolete"
    )

cgprsGtpPDPCxtActivationRejNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 2, 0, 3)
)
cgprsGtpPDPCxtActivationRejNotif.setObjects(
      *(("CISCO-GPRS-GTP-MIB", "cgprsGtpGSNidOfLastUnexpPDPCxt"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpTIDOfLastUnexpPDPCxt"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpRejReasonOfLastUnexpPDPCxt"))
)
if mibBuilder.loadTexts:
    cgprsGtpPDPCxtActivationRejNotif.setStatus(
        "obsolete"
    )

cgprsGtpPrimaryChargingGWUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 2, 0, 4)
)
if mibBuilder.loadTexts:
    cgprsGtpPrimaryChargingGWUpNotif.setStatus(
        "obsolete"
    )

cgprsGtpPrimaryChargingGWDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 2, 0, 5)
)
if mibBuilder.loadTexts:
    cgprsGtpPrimaryChargingGWDownNotif.setStatus(
        "obsolete"
    )

cgprsGtpSecondaryChargingGWUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 2, 0, 6)
)
if mibBuilder.loadTexts:
    cgprsGtpSecondaryChargingGWUpNotif.setStatus(
        "obsolete"
    )

cgprsGtpSecondaryChargingGWDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 2, 0, 7)
)
if mibBuilder.loadTexts:
    cgprsGtpSecondaryChargingGWDownNotif.setStatus(
        "obsolete"
    )


# Notifications groups

cgprsGtpGgsnNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 3, 2, 6)
)
cgprsGtpGgsnNotifGroup.setObjects(
      *(("CISCO-GPRS-GTP-MIB", "cgprsGtpGSNPathFailedNotif"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpGSNPathRecoveredNotif"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpPDPCxtActivationRejNotif"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpPrimaryChargingGWUpNotif"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpPrimaryChargingGWDownNotif"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpSecondaryChargingGWUpNotif"),
        ("CISCO-GPRS-GTP-MIB", "cgprsGtpSecondaryChargingGWDownNotif"))
)
if mibBuilder.loadTexts:
    cgprsGtpGgsnNotifGroup.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

cgprsGtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 48, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsGtpCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GPRS-GTP-MIB",
    **{"ciscoGprsGtpMIB": ciscoGprsGtpMIB,
       "ciscoGprsGtpMIBObjects": ciscoGprsGtpMIBObjects,
       "ciscoGprsGtpConfig": ciscoGprsGtpConfig,
       "cgprsGtpGeneralConfig": cgprsGtpGeneralConfig,
       "cgprsGtpT3TunnelTimer": cgprsGtpT3TunnelTimer,
       "cgprsGtpT3ResponseTimer": cgprsGtpT3ResponseTimer,
       "cgprsGtpN3Request": cgprsGtpN3Request,
       "cgprsGtpN3BufferSize": cgprsGtpN3BufferSize,
       "cgprsGtpEchoRequestTimer": cgprsGtpEchoRequestTimer,
       "cgprsGtpGSNTotalBandwidthResrc": cgprsGtpGSNTotalBandwidthResrc,
       "cgprsGtpMaxNumPDPCxts": cgprsGtpMaxNumPDPCxts,
       "cgprsGtpDroppedPktsMonTime": cgprsGtpDroppedPktsMonTime,
       "cgprsGtpNoRespToEchoNotifEnable": cgprsGtpNoRespToEchoNotifEnable,
       "cgprsGtpPDPCxtActRejNotifEnable": cgprsGtpPDPCxtActRejNotifEnable,
       "cgprsGtpGgsnConfig": cgprsGtpGgsnConfig,
       "cgprsGtpAPNAddrAllocMethodGlobDef": cgprsGtpAPNAddrAllocMethodGlobDef,
       "cgprsGtpChargingGWTable": cgprsGtpChargingGWTable,
       "cgprsGtpChargingGWEntry": cgprsGtpChargingGWEntry,
       "cgprsGtpChargingGWid": cgprsGtpChargingGWid,
       "cgprsGtpChargingGWName": cgprsGtpChargingGWName,
       "cgprsGtpChargingGWType": cgprsGtpChargingGWType,
       "cgprsGtpChargingGWOperState": cgprsGtpChargingGWOperState,
       "cgprsGtpChargingGWNotifEnable": cgprsGtpChargingGWNotifEnable,
       "cgprsGtpChargingGWRowStatus": cgprsGtpChargingGWRowStatus,
       "cgprsGtpAPNTable": cgprsGtpAPNTable,
       "cgprsGtpAPNEntry": cgprsGtpAPNEntry,
       "cgprsGtpAPNId": cgprsGtpAPNId,
       "cgprsGtpAPNName": cgprsGtpAPNName,
       "cgprsGtpAPNAddrAllocMethod": cgprsGtpAPNAddrAllocMethod,
       "cgprsGtpAPNRowStatus": cgprsGtpAPNRowStatus,
       "ciscoGprsGtpStats": ciscoGprsGtpStats,
       "cgprsGtpGeneralStats": cgprsGtpGeneralStats,
       "cgprsGtpCurRxPacketQueueSize": cgprsGtpCurRxPacketQueueSize,
       "cgprsGtpCurActivatedPDPCxtsCnt": cgprsGtpCurActivatedPDPCxtsCnt,
       "cgprsGtpCurUnexpRxGpduCnt": cgprsGtpCurUnexpRxGpduCnt,
       "cgprsGtpCurRejPDPCxtActivationCnt": cgprsGtpCurRejPDPCxtActivationCnt,
       "cgprsGtpTotalPktsDropped": cgprsGtpTotalPktsDropped,
       "cgprsGtpDroppedPktsTimeFrame": cgprsGtpDroppedPktsTimeFrame,
       "cgprsGtpDroppedPktsCnt": cgprsGtpDroppedPktsCnt,
       "cgprsGtpCurMTForPremiumQos": cgprsGtpCurMTForPremiumQos,
       "cgprsGtpCurMTForNormalQos": cgprsGtpCurMTForNormalQos,
       "cgprsGtpCurMTForBestEffortQos": cgprsGtpCurMTForBestEffortQos,
       "cgprsGtpCurGSNBandwidthResrcUsed": cgprsGtpCurGSNBandwidthResrcUsed,
       "cgprsGtpGSNTable": cgprsGtpGSNTable,
       "cgprsGtpGSNEntry": cgprsGtpGSNEntry,
       "cgprsGtpGSNid": cgprsGtpGSNid,
       "cgprsGtpGSNEchoFailedNotifCnt": cgprsGtpGSNEchoFailedNotifCnt,
       "cgprsGtpGgsnStats": cgprsGtpGgsnStats,
       "cgprsGtpTotalNumAllocIpAddr": cgprsGtpTotalNumAllocIpAddr,
       "cgprsGtpChargingMsgCnt": cgprsGtpChargingMsgCnt,
       "cgprsGtpNumAllocIpAddrTable": cgprsGtpNumAllocIpAddrTable,
       "cgprsGtpNumAllocIpAddrEntry": cgprsGtpNumAllocIpAddrEntry,
       "cgprsGtpNumAllocIpAddr": cgprsGtpNumAllocIpAddr,
       "cgprsGtpGgsnStatus": cgprsGtpGgsnStatus,
       "cgprsGtpVersion": cgprsGtpVersion,
       "cgprsGtpLastGSNidNoRespToEcho": cgprsGtpLastGSNidNoRespToEcho,
       "cgprsGtpLastGSNidRecovered": cgprsGtpLastGSNidRecovered,
       "cgprsGtpGSNidOfLastUnexpPDPCxt": cgprsGtpGSNidOfLastUnexpPDPCxt,
       "cgprsGtpTIDOfLastUnexpPDPCxt": cgprsGtpTIDOfLastUnexpPDPCxt,
       "cgprsGtpRejReasonOfLastUnexpPDPCxt": cgprsGtpRejReasonOfLastUnexpPDPCxt,
       "ciscoGprsGtpNotifPrefix": ciscoGprsGtpNotifPrefix,
       "ciscoGprsGtpNotifs": ciscoGprsGtpNotifs,
       "cgprsGtpGSNPathFailedNotif": cgprsGtpGSNPathFailedNotif,
       "cgprsGtpGSNPathRecoveredNotif": cgprsGtpGSNPathRecoveredNotif,
       "cgprsGtpPDPCxtActivationRejNotif": cgprsGtpPDPCxtActivationRejNotif,
       "cgprsGtpPrimaryChargingGWUpNotif": cgprsGtpPrimaryChargingGWUpNotif,
       "cgprsGtpPrimaryChargingGWDownNotif": cgprsGtpPrimaryChargingGWDownNotif,
       "cgprsGtpSecondaryChargingGWUpNotif": cgprsGtpSecondaryChargingGWUpNotif,
       "cgprsGtpSecondaryChargingGWDownNotif": cgprsGtpSecondaryChargingGWDownNotif,
       "ciscoGprsGtpConformances": ciscoGprsGtpConformances,
       "cgprsGtpCompliances": cgprsGtpCompliances,
       "cgprsGtpCompliance": cgprsGtpCompliance,
       "cgprsGtpGroups": cgprsGtpGroups,
       "cgprsGtpGeneralConfigGroup": cgprsGtpGeneralConfigGroup,
       "cgprsGtpGgsnConfigGroup": cgprsGtpGgsnConfigGroup,
       "cgprsGtpGeneralStatsGroup": cgprsGtpGeneralStatsGroup,
       "cgprsGtpGgsnStatsGroup": cgprsGtpGgsnStatsGroup,
       "cgprsGtpGgsnStatusGroup": cgprsGtpGgsnStatusGroup,
       "cgprsGtpGgsnNotifGroup": cgprsGtpGgsnNotifGroup}
)
