# SNMP MIB module (RAQMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAQMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:44 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(rmon,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "rmon")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

raqmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 31)
)
raqmonMIB.setRevisions(
        ("2006-10-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaqmonNotifications_ObjectIdentity = ObjectIdentity
raqmonNotifications = _RaqmonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 31, 0)
)
_RaqmonMIBObjects_ObjectIdentity = ObjectIdentity
raqmonMIBObjects = _RaqmonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 31, 1)
)
_RaqmonSession_ObjectIdentity = ObjectIdentity
raqmonSession = _RaqmonSession_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1)
)
_RaqmonParticipantTable_Object = MibTable
raqmonParticipantTable = _RaqmonParticipantTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    raqmonParticipantTable.setStatus("current")
_RaqmonParticipantEntry_Object = MibTableRow
raqmonParticipantEntry = _RaqmonParticipantEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1)
)
raqmonParticipantEntry.setIndexNames(
    (0, "RAQMON-MIB", "raqmonParticipantStartDate"),
    (0, "RAQMON-MIB", "raqmonParticipantIndex"),
)
if mibBuilder.loadTexts:
    raqmonParticipantEntry.setStatus("current")
_RaqmonParticipantStartDate_Type = DateAndTime
_RaqmonParticipantStartDate_Object = MibTableColumn
raqmonParticipantStartDate = _RaqmonParticipantStartDate_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 1),
    _RaqmonParticipantStartDate_Type()
)
raqmonParticipantStartDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raqmonParticipantStartDate.setStatus("current")


class _RaqmonParticipantIndex_Type(Unsigned32):
    """Custom type raqmonParticipantIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaqmonParticipantIndex_Type.__name__ = "Unsigned32"
_RaqmonParticipantIndex_Object = MibTableColumn
raqmonParticipantIndex = _RaqmonParticipantIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 2),
    _RaqmonParticipantIndex_Type()
)
raqmonParticipantIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raqmonParticipantIndex.setStatus("current")


class _RaqmonParticipantReportCaps_Type(Bits):
    """Custom type raqmonParticipantReportCaps based on Bits"""
    namedValues = NamedValues(
        *(("raqmonPartApplicationDelay", 10),
          ("raqmonPartRepAppName", 29),
          ("raqmonPartRepCPU", 27),
          ("raqmonPartRepCumDiscards", 19),
          ("raqmonPartRepCumPacketsLoss", 17),
          ("raqmonPartRepDestLayer2Priority", 25),
          ("raqmonPartRepDestPayloadType", 22),
          ("raqmonPartRepDestTosDscp", 26),
          ("raqmonPartRepDsrcName", 0),
          ("raqmonPartRepDsrcPort", 2),
          ("raqmonPartRepFractionDiscards", 20),
          ("raqmonPartRepFractionPacketsLoss", 18),
          ("raqmonPartRepIAJitter", 11),
          ("raqmonPartRepIPDV", 12),
          ("raqmonPartRepMemory", 28),
          ("raqmonPartRepOWEnd2EndNetDelay", 9),
          ("raqmonPartRepRTEnd2EndNetDelay", 8),
          ("raqmonPartRepRcvdOctets", 14),
          ("raqmonPartRepRcvdPackets", 13),
          ("raqmonPartRepRecvName", 1),
          ("raqmonPartRepRecvPort", 3),
          ("raqmonPartRepSentOctets", 16),
          ("raqmonPartRepSentPackets", 15),
          ("raqmonPartRepSessionDuration", 6),
          ("raqmonPartRepSetupDelay", 5),
          ("raqmonPartRepSetupStatus", 7),
          ("raqmonPartRepSetupTime", 4),
          ("raqmonPartRepSrcLayer2Priority", 23),
          ("raqmonPartRepSrcPayloadType", 21),
          ("raqmonPartRepSrcTosDscp", 24))
    )

_RaqmonParticipantReportCaps_Type.__name__ = "Bits"
_RaqmonParticipantReportCaps_Object = MibTableColumn
raqmonParticipantReportCaps = _RaqmonParticipantReportCaps_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 3),
    _RaqmonParticipantReportCaps_Type()
)
raqmonParticipantReportCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantReportCaps.setStatus("current")
_RaqmonParticipantAddrType_Type = InetAddressType
_RaqmonParticipantAddrType_Object = MibTableColumn
raqmonParticipantAddrType = _RaqmonParticipantAddrType_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 4),
    _RaqmonParticipantAddrType_Type()
)
raqmonParticipantAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantAddrType.setStatus("current")
_RaqmonParticipantAddr_Type = InetAddress
_RaqmonParticipantAddr_Object = MibTableColumn
raqmonParticipantAddr = _RaqmonParticipantAddr_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 5),
    _RaqmonParticipantAddr_Type()
)
raqmonParticipantAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantAddr.setStatus("current")
_RaqmonParticipantSendPort_Type = InetPortNumber
_RaqmonParticipantSendPort_Object = MibTableColumn
raqmonParticipantSendPort = _RaqmonParticipantSendPort_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 6),
    _RaqmonParticipantSendPort_Type()
)
raqmonParticipantSendPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantSendPort.setStatus("current")
_RaqmonParticipantRecvPort_Type = InetPortNumber
_RaqmonParticipantRecvPort_Object = MibTableColumn
raqmonParticipantRecvPort = _RaqmonParticipantRecvPort_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 7),
    _RaqmonParticipantRecvPort_Type()
)
raqmonParticipantRecvPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantRecvPort.setStatus("current")


class _RaqmonParticipantSetupDelay_Type(Integer32):
    """Custom type raqmonParticipantSetupDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantSetupDelay_Type.__name__ = "Integer32"
_RaqmonParticipantSetupDelay_Object = MibTableColumn
raqmonParticipantSetupDelay = _RaqmonParticipantSetupDelay_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 8),
    _RaqmonParticipantSetupDelay_Type()
)
raqmonParticipantSetupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantSetupDelay.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantSetupDelay.setUnits("milliseconds")
_RaqmonParticipantName_Type = SnmpAdminString
_RaqmonParticipantName_Object = MibTableColumn
raqmonParticipantName = _RaqmonParticipantName_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 9),
    _RaqmonParticipantName_Type()
)
raqmonParticipantName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantName.setStatus("current")
_RaqmonParticipantAppName_Type = SnmpAdminString
_RaqmonParticipantAppName_Object = MibTableColumn
raqmonParticipantAppName = _RaqmonParticipantAppName_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 10),
    _RaqmonParticipantAppName_Type()
)
raqmonParticipantAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantAppName.setStatus("current")
_RaqmonParticipantQosCount_Type = Gauge32
_RaqmonParticipantQosCount_Object = MibTableColumn
raqmonParticipantQosCount = _RaqmonParticipantQosCount_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 11),
    _RaqmonParticipantQosCount_Type()
)
raqmonParticipantQosCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantQosCount.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantQosCount.setUnits("entries")
_RaqmonParticipantEndDate_Type = DateAndTime
_RaqmonParticipantEndDate_Object = MibTableColumn
raqmonParticipantEndDate = _RaqmonParticipantEndDate_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 12),
    _RaqmonParticipantEndDate_Type()
)
raqmonParticipantEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantEndDate.setStatus("current")


class _RaqmonParticipantDestPayloadType_Type(Integer32):
    """Custom type raqmonParticipantDestPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 127),
    )


_RaqmonParticipantDestPayloadType_Type.__name__ = "Integer32"
_RaqmonParticipantDestPayloadType_Object = MibTableColumn
raqmonParticipantDestPayloadType = _RaqmonParticipantDestPayloadType_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 13),
    _RaqmonParticipantDestPayloadType_Type()
)
raqmonParticipantDestPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantDestPayloadType.setStatus("current")


class _RaqmonParticipantSrcPayloadType_Type(Integer32):
    """Custom type raqmonParticipantSrcPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 127),
    )


_RaqmonParticipantSrcPayloadType_Type.__name__ = "Integer32"
_RaqmonParticipantSrcPayloadType_Object = MibTableColumn
raqmonParticipantSrcPayloadType = _RaqmonParticipantSrcPayloadType_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 14),
    _RaqmonParticipantSrcPayloadType_Type()
)
raqmonParticipantSrcPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantSrcPayloadType.setStatus("current")
_RaqmonParticipantActive_Type = TruthValue
_RaqmonParticipantActive_Object = MibTableColumn
raqmonParticipantActive = _RaqmonParticipantActive_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 15),
    _RaqmonParticipantActive_Type()
)
raqmonParticipantActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantActive.setStatus("current")
_RaqmonParticipantPeer_Type = RowPointer
_RaqmonParticipantPeer_Object = MibTableColumn
raqmonParticipantPeer = _RaqmonParticipantPeer_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 16),
    _RaqmonParticipantPeer_Type()
)
raqmonParticipantPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantPeer.setStatus("current")
_RaqmonParticipantPeerAddrType_Type = InetAddressType
_RaqmonParticipantPeerAddrType_Object = MibTableColumn
raqmonParticipantPeerAddrType = _RaqmonParticipantPeerAddrType_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 17),
    _RaqmonParticipantPeerAddrType_Type()
)
raqmonParticipantPeerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantPeerAddrType.setStatus("current")
_RaqmonParticipantPeerAddr_Type = InetAddress
_RaqmonParticipantPeerAddr_Object = MibTableColumn
raqmonParticipantPeerAddr = _RaqmonParticipantPeerAddr_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 18),
    _RaqmonParticipantPeerAddr_Type()
)
raqmonParticipantPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantPeerAddr.setStatus("current")


class _RaqmonParticipantSrcL2Priority_Type(Integer32):
    """Custom type raqmonParticipantSrcL2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_RaqmonParticipantSrcL2Priority_Type.__name__ = "Integer32"
_RaqmonParticipantSrcL2Priority_Object = MibTableColumn
raqmonParticipantSrcL2Priority = _RaqmonParticipantSrcL2Priority_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 19),
    _RaqmonParticipantSrcL2Priority_Type()
)
raqmonParticipantSrcL2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantSrcL2Priority.setStatus("current")


class _RaqmonParticipantDestL2Priority_Type(Integer32):
    """Custom type raqmonParticipantDestL2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_RaqmonParticipantDestL2Priority_Type.__name__ = "Integer32"
_RaqmonParticipantDestL2Priority_Object = MibTableColumn
raqmonParticipantDestL2Priority = _RaqmonParticipantDestL2Priority_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 20),
    _RaqmonParticipantDestL2Priority_Type()
)
raqmonParticipantDestL2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantDestL2Priority.setStatus("current")


class _RaqmonParticipantSrcDSCP_Type(Integer32):
    """Custom type raqmonParticipantSrcDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RaqmonParticipantSrcDSCP_Type.__name__ = "Integer32"
_RaqmonParticipantSrcDSCP_Object = MibTableColumn
raqmonParticipantSrcDSCP = _RaqmonParticipantSrcDSCP_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 21),
    _RaqmonParticipantSrcDSCP_Type()
)
raqmonParticipantSrcDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantSrcDSCP.setStatus("current")


class _RaqmonParticipantDestDSCP_Type(Integer32):
    """Custom type raqmonParticipantDestDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RaqmonParticipantDestDSCP_Type.__name__ = "Integer32"
_RaqmonParticipantDestDSCP_Object = MibTableColumn
raqmonParticipantDestDSCP = _RaqmonParticipantDestDSCP_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 22),
    _RaqmonParticipantDestDSCP_Type()
)
raqmonParticipantDestDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantDestDSCP.setStatus("current")


class _RaqmonParticipantCpuMean_Type(Integer32):
    """Custom type raqmonParticipantCpuMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_RaqmonParticipantCpuMean_Type.__name__ = "Integer32"
_RaqmonParticipantCpuMean_Object = MibTableColumn
raqmonParticipantCpuMean = _RaqmonParticipantCpuMean_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 23),
    _RaqmonParticipantCpuMean_Type()
)
raqmonParticipantCpuMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantCpuMean.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantCpuMean.setUnits("percents")


class _RaqmonParticipantCpuMin_Type(Integer32):
    """Custom type raqmonParticipantCpuMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_RaqmonParticipantCpuMin_Type.__name__ = "Integer32"
_RaqmonParticipantCpuMin_Object = MibTableColumn
raqmonParticipantCpuMin = _RaqmonParticipantCpuMin_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 24),
    _RaqmonParticipantCpuMin_Type()
)
raqmonParticipantCpuMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantCpuMin.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantCpuMin.setUnits("percents")


class _RaqmonParticipantCpuMax_Type(Integer32):
    """Custom type raqmonParticipantCpuMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_RaqmonParticipantCpuMax_Type.__name__ = "Integer32"
_RaqmonParticipantCpuMax_Object = MibTableColumn
raqmonParticipantCpuMax = _RaqmonParticipantCpuMax_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 25),
    _RaqmonParticipantCpuMax_Type()
)
raqmonParticipantCpuMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantCpuMax.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantCpuMax.setUnits("percents")


class _RaqmonParticipantMemoryMean_Type(Integer32):
    """Custom type raqmonParticipantMemoryMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_RaqmonParticipantMemoryMean_Type.__name__ = "Integer32"
_RaqmonParticipantMemoryMean_Object = MibTableColumn
raqmonParticipantMemoryMean = _RaqmonParticipantMemoryMean_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 26),
    _RaqmonParticipantMemoryMean_Type()
)
raqmonParticipantMemoryMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantMemoryMean.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantMemoryMean.setUnits("percents")


class _RaqmonParticipantMemoryMin_Type(Integer32):
    """Custom type raqmonParticipantMemoryMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_RaqmonParticipantMemoryMin_Type.__name__ = "Integer32"
_RaqmonParticipantMemoryMin_Object = MibTableColumn
raqmonParticipantMemoryMin = _RaqmonParticipantMemoryMin_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 27),
    _RaqmonParticipantMemoryMin_Type()
)
raqmonParticipantMemoryMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantMemoryMin.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantMemoryMin.setUnits("percents")


class _RaqmonParticipantMemoryMax_Type(Integer32):
    """Custom type raqmonParticipantMemoryMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_RaqmonParticipantMemoryMax_Type.__name__ = "Integer32"
_RaqmonParticipantMemoryMax_Object = MibTableColumn
raqmonParticipantMemoryMax = _RaqmonParticipantMemoryMax_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 28),
    _RaqmonParticipantMemoryMax_Type()
)
raqmonParticipantMemoryMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantMemoryMax.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantMemoryMax.setUnits("percents")


class _RaqmonParticipantNetRTTMean_Type(Integer32):
    """Custom type raqmonParticipantNetRTTMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantNetRTTMean_Type.__name__ = "Integer32"
_RaqmonParticipantNetRTTMean_Object = MibTableColumn
raqmonParticipantNetRTTMean = _RaqmonParticipantNetRTTMean_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 29),
    _RaqmonParticipantNetRTTMean_Type()
)
raqmonParticipantNetRTTMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantNetRTTMean.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantNetRTTMean.setUnits("milliseconds")


class _RaqmonParticipantNetRTTMin_Type(Integer32):
    """Custom type raqmonParticipantNetRTTMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantNetRTTMin_Type.__name__ = "Integer32"
_RaqmonParticipantNetRTTMin_Object = MibTableColumn
raqmonParticipantNetRTTMin = _RaqmonParticipantNetRTTMin_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 30),
    _RaqmonParticipantNetRTTMin_Type()
)
raqmonParticipantNetRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantNetRTTMin.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantNetRTTMin.setUnits("milliseconds")


class _RaqmonParticipantNetRTTMax_Type(Integer32):
    """Custom type raqmonParticipantNetRTTMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantNetRTTMax_Type.__name__ = "Integer32"
_RaqmonParticipantNetRTTMax_Object = MibTableColumn
raqmonParticipantNetRTTMax = _RaqmonParticipantNetRTTMax_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 31),
    _RaqmonParticipantNetRTTMax_Type()
)
raqmonParticipantNetRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantNetRTTMax.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantNetRTTMax.setUnits("milliseconds")


class _RaqmonParticipantIAJitterMean_Type(Integer32):
    """Custom type raqmonParticipantIAJitterMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantIAJitterMean_Type.__name__ = "Integer32"
_RaqmonParticipantIAJitterMean_Object = MibTableColumn
raqmonParticipantIAJitterMean = _RaqmonParticipantIAJitterMean_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 32),
    _RaqmonParticipantIAJitterMean_Type()
)
raqmonParticipantIAJitterMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantIAJitterMean.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantIAJitterMean.setUnits("milliseconds")


class _RaqmonParticipantIAJitterMin_Type(Integer32):
    """Custom type raqmonParticipantIAJitterMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantIAJitterMin_Type.__name__ = "Integer32"
_RaqmonParticipantIAJitterMin_Object = MibTableColumn
raqmonParticipantIAJitterMin = _RaqmonParticipantIAJitterMin_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 33),
    _RaqmonParticipantIAJitterMin_Type()
)
raqmonParticipantIAJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantIAJitterMin.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantIAJitterMin.setUnits("milliseconds")


class _RaqmonParticipantIAJitterMax_Type(Integer32):
    """Custom type raqmonParticipantIAJitterMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantIAJitterMax_Type.__name__ = "Integer32"
_RaqmonParticipantIAJitterMax_Object = MibTableColumn
raqmonParticipantIAJitterMax = _RaqmonParticipantIAJitterMax_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 34),
    _RaqmonParticipantIAJitterMax_Type()
)
raqmonParticipantIAJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantIAJitterMax.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantIAJitterMax.setUnits("milliseconds")


class _RaqmonParticipantIPDVMean_Type(Integer32):
    """Custom type raqmonParticipantIPDVMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantIPDVMean_Type.__name__ = "Integer32"
_RaqmonParticipantIPDVMean_Object = MibTableColumn
raqmonParticipantIPDVMean = _RaqmonParticipantIPDVMean_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 35),
    _RaqmonParticipantIPDVMean_Type()
)
raqmonParticipantIPDVMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantIPDVMean.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantIPDVMean.setUnits("milliseconds")


class _RaqmonParticipantIPDVMin_Type(Integer32):
    """Custom type raqmonParticipantIPDVMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantIPDVMin_Type.__name__ = "Integer32"
_RaqmonParticipantIPDVMin_Object = MibTableColumn
raqmonParticipantIPDVMin = _RaqmonParticipantIPDVMin_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 36),
    _RaqmonParticipantIPDVMin_Type()
)
raqmonParticipantIPDVMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantIPDVMin.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantIPDVMin.setUnits("milliseconds")


class _RaqmonParticipantIPDVMax_Type(Integer32):
    """Custom type raqmonParticipantIPDVMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantIPDVMax_Type.__name__ = "Integer32"
_RaqmonParticipantIPDVMax_Object = MibTableColumn
raqmonParticipantIPDVMax = _RaqmonParticipantIPDVMax_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 37),
    _RaqmonParticipantIPDVMax_Type()
)
raqmonParticipantIPDVMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantIPDVMax.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantIPDVMax.setUnits("milliseconds")


class _RaqmonParticipantNetOwdMean_Type(Integer32):
    """Custom type raqmonParticipantNetOwdMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantNetOwdMean_Type.__name__ = "Integer32"
_RaqmonParticipantNetOwdMean_Object = MibTableColumn
raqmonParticipantNetOwdMean = _RaqmonParticipantNetOwdMean_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 38),
    _RaqmonParticipantNetOwdMean_Type()
)
raqmonParticipantNetOwdMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantNetOwdMean.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantNetOwdMean.setUnits("milliseconds")


class _RaqmonParticipantNetOwdMin_Type(Integer32):
    """Custom type raqmonParticipantNetOwdMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantNetOwdMin_Type.__name__ = "Integer32"
_RaqmonParticipantNetOwdMin_Object = MibTableColumn
raqmonParticipantNetOwdMin = _RaqmonParticipantNetOwdMin_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 39),
    _RaqmonParticipantNetOwdMin_Type()
)
raqmonParticipantNetOwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantNetOwdMin.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantNetOwdMin.setUnits("milliseconds")


class _RaqmonParticipantNetOwdMax_Type(Integer32):
    """Custom type raqmonParticipantNetOwdMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantNetOwdMax_Type.__name__ = "Integer32"
_RaqmonParticipantNetOwdMax_Object = MibTableColumn
raqmonParticipantNetOwdMax = _RaqmonParticipantNetOwdMax_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 40),
    _RaqmonParticipantNetOwdMax_Type()
)
raqmonParticipantNetOwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantNetOwdMax.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantNetOwdMax.setUnits("milliseconds")


class _RaqmonParticipantAppDelayMean_Type(Integer32):
    """Custom type raqmonParticipantAppDelayMean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantAppDelayMean_Type.__name__ = "Integer32"
_RaqmonParticipantAppDelayMean_Object = MibTableColumn
raqmonParticipantAppDelayMean = _RaqmonParticipantAppDelayMean_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 41),
    _RaqmonParticipantAppDelayMean_Type()
)
raqmonParticipantAppDelayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantAppDelayMean.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantAppDelayMean.setUnits("milliseconds")


class _RaqmonParticipantAppDelayMin_Type(Integer32):
    """Custom type raqmonParticipantAppDelayMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantAppDelayMin_Type.__name__ = "Integer32"
_RaqmonParticipantAppDelayMin_Object = MibTableColumn
raqmonParticipantAppDelayMin = _RaqmonParticipantAppDelayMin_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 42),
    _RaqmonParticipantAppDelayMin_Type()
)
raqmonParticipantAppDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantAppDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantAppDelayMin.setUnits("milliseconds")


class _RaqmonParticipantAppDelayMax_Type(Integer32):
    """Custom type raqmonParticipantAppDelayMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantAppDelayMax_Type.__name__ = "Integer32"
_RaqmonParticipantAppDelayMax_Object = MibTableColumn
raqmonParticipantAppDelayMax = _RaqmonParticipantAppDelayMax_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 43),
    _RaqmonParticipantAppDelayMax_Type()
)
raqmonParticipantAppDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantAppDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantAppDelayMax.setUnits("milliseconds")


class _RaqmonParticipantPacketsRcvd_Type(Integer32):
    """Custom type raqmonParticipantPacketsRcvd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantPacketsRcvd_Type.__name__ = "Integer32"
_RaqmonParticipantPacketsRcvd_Object = MibTableColumn
raqmonParticipantPacketsRcvd = _RaqmonParticipantPacketsRcvd_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 44),
    _RaqmonParticipantPacketsRcvd_Type()
)
raqmonParticipantPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantPacketsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantPacketsRcvd.setUnits("packets")


class _RaqmonParticipantPacketsSent_Type(Integer32):
    """Custom type raqmonParticipantPacketsSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantPacketsSent_Type.__name__ = "Integer32"
_RaqmonParticipantPacketsSent_Object = MibTableColumn
raqmonParticipantPacketsSent = _RaqmonParticipantPacketsSent_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 45),
    _RaqmonParticipantPacketsSent_Type()
)
raqmonParticipantPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantPacketsSent.setUnits("packets")


class _RaqmonParticipantOctetsRcvd_Type(Integer32):
    """Custom type raqmonParticipantOctetsRcvd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantOctetsRcvd_Type.__name__ = "Integer32"
_RaqmonParticipantOctetsRcvd_Object = MibTableColumn
raqmonParticipantOctetsRcvd = _RaqmonParticipantOctetsRcvd_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 46),
    _RaqmonParticipantOctetsRcvd_Type()
)
raqmonParticipantOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantOctetsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantOctetsRcvd.setUnits("Octets")


class _RaqmonParticipantOctetsSent_Type(Integer32):
    """Custom type raqmonParticipantOctetsSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantOctetsSent_Type.__name__ = "Integer32"
_RaqmonParticipantOctetsSent_Object = MibTableColumn
raqmonParticipantOctetsSent = _RaqmonParticipantOctetsSent_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 47),
    _RaqmonParticipantOctetsSent_Type()
)
raqmonParticipantOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantOctetsSent.setUnits("Octets")


class _RaqmonParticipantLostPackets_Type(Integer32):
    """Custom type raqmonParticipantLostPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantLostPackets_Type.__name__ = "Integer32"
_RaqmonParticipantLostPackets_Object = MibTableColumn
raqmonParticipantLostPackets = _RaqmonParticipantLostPackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 48),
    _RaqmonParticipantLostPackets_Type()
)
raqmonParticipantLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantLostPackets.setUnits("packets")


class _RaqmonParticipantLostPacketsFrct_Type(Integer32):
    """Custom type raqmonParticipantLostPacketsFrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_RaqmonParticipantLostPacketsFrct_Type.__name__ = "Integer32"
_RaqmonParticipantLostPacketsFrct_Object = MibTableColumn
raqmonParticipantLostPacketsFrct = _RaqmonParticipantLostPacketsFrct_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 49),
    _RaqmonParticipantLostPacketsFrct_Type()
)
raqmonParticipantLostPacketsFrct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantLostPacketsFrct.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantLostPacketsFrct.setUnits("percents")


class _RaqmonParticipantDiscards_Type(Integer32):
    """Custom type raqmonParticipantDiscards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonParticipantDiscards_Type.__name__ = "Integer32"
_RaqmonParticipantDiscards_Object = MibTableColumn
raqmonParticipantDiscards = _RaqmonParticipantDiscards_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 50),
    _RaqmonParticipantDiscards_Type()
)
raqmonParticipantDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantDiscards.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantDiscards.setUnits("packets")


class _RaqmonParticipantDiscardsFrct_Type(Integer32):
    """Custom type raqmonParticipantDiscardsFrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )


_RaqmonParticipantDiscardsFrct_Type.__name__ = "Integer32"
_RaqmonParticipantDiscardsFrct_Object = MibTableColumn
raqmonParticipantDiscardsFrct = _RaqmonParticipantDiscardsFrct_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 1, 1, 51),
    _RaqmonParticipantDiscardsFrct_Type()
)
raqmonParticipantDiscardsFrct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantDiscardsFrct.setStatus("current")
if mibBuilder.loadTexts:
    raqmonParticipantDiscardsFrct.setUnits("percents")
_RaqmonQosTable_Object = MibTable
raqmonQosTable = _RaqmonQosTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2)
)
if mibBuilder.loadTexts:
    raqmonQosTable.setStatus("current")
_RaqmonQosEntry_Object = MibTableRow
raqmonQosEntry = _RaqmonQosEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2, 1)
)
raqmonQosEntry.setIndexNames(
    (0, "RAQMON-MIB", "raqmonParticipantStartDate"),
    (0, "RAQMON-MIB", "raqmonParticipantIndex"),
    (0, "RAQMON-MIB", "raqmonQosTime"),
)
if mibBuilder.loadTexts:
    raqmonQosEntry.setStatus("current")


class _RaqmonQosTime_Type(Unsigned32):
    """Custom type raqmonQosTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonQosTime_Type.__name__ = "Unsigned32"
_RaqmonQosTime_Object = MibTableColumn
raqmonQosTime = _RaqmonQosTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2, 1, 1),
    _RaqmonQosTime_Type()
)
raqmonQosTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raqmonQosTime.setStatus("current")
if mibBuilder.loadTexts:
    raqmonQosTime.setUnits("seconds")


class _RaqmonQoSEnd2EndNetDelay_Type(Integer32):
    """Custom type raqmonQoSEnd2EndNetDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonQoSEnd2EndNetDelay_Type.__name__ = "Integer32"
_RaqmonQoSEnd2EndNetDelay_Object = MibTableColumn
raqmonQoSEnd2EndNetDelay = _RaqmonQoSEnd2EndNetDelay_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2, 1, 2),
    _RaqmonQoSEnd2EndNetDelay_Type()
)
raqmonQoSEnd2EndNetDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonQoSEnd2EndNetDelay.setStatus("current")
if mibBuilder.loadTexts:
    raqmonQoSEnd2EndNetDelay.setUnits("milliseconds")


class _RaqmonQoSInterArrivalJitter_Type(Integer32):
    """Custom type raqmonQoSInterArrivalJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonQoSInterArrivalJitter_Type.__name__ = "Integer32"
_RaqmonQoSInterArrivalJitter_Object = MibTableColumn
raqmonQoSInterArrivalJitter = _RaqmonQoSInterArrivalJitter_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2, 1, 3),
    _RaqmonQoSInterArrivalJitter_Type()
)
raqmonQoSInterArrivalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonQoSInterArrivalJitter.setStatus("current")
if mibBuilder.loadTexts:
    raqmonQoSInterArrivalJitter.setUnits("milliseconds")


class _RaqmonQosRcvdPackets_Type(Integer32):
    """Custom type raqmonQosRcvdPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonQosRcvdPackets_Type.__name__ = "Integer32"
_RaqmonQosRcvdPackets_Object = MibTableColumn
raqmonQosRcvdPackets = _RaqmonQosRcvdPackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2, 1, 4),
    _RaqmonQosRcvdPackets_Type()
)
raqmonQosRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonQosRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    raqmonQosRcvdPackets.setUnits("packets")


class _RaqmonQosRcvdOctets_Type(Integer32):
    """Custom type raqmonQosRcvdOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonQosRcvdOctets_Type.__name__ = "Integer32"
_RaqmonQosRcvdOctets_Object = MibTableColumn
raqmonQosRcvdOctets = _RaqmonQosRcvdOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2, 1, 5),
    _RaqmonQosRcvdOctets_Type()
)
raqmonQosRcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonQosRcvdOctets.setStatus("current")
if mibBuilder.loadTexts:
    raqmonQosRcvdOctets.setUnits("octets")


class _RaqmonQosSentPackets_Type(Integer32):
    """Custom type raqmonQosSentPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonQosSentPackets_Type.__name__ = "Integer32"
_RaqmonQosSentPackets_Object = MibTableColumn
raqmonQosSentPackets = _RaqmonQosSentPackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2, 1, 6),
    _RaqmonQosSentPackets_Type()
)
raqmonQosSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonQosSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    raqmonQosSentPackets.setUnits("packets")


class _RaqmonQosSentOctets_Type(Integer32):
    """Custom type raqmonQosSentOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonQosSentOctets_Type.__name__ = "Integer32"
_RaqmonQosSentOctets_Object = MibTableColumn
raqmonQosSentOctets = _RaqmonQosSentOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2, 1, 7),
    _RaqmonQosSentOctets_Type()
)
raqmonQosSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonQosSentOctets.setStatus("current")
if mibBuilder.loadTexts:
    raqmonQosSentOctets.setUnits("octets")


class _RaqmonQosLostPackets_Type(Integer32):
    """Custom type raqmonQosLostPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RaqmonQosLostPackets_Type.__name__ = "Integer32"
_RaqmonQosLostPackets_Object = MibTableColumn
raqmonQosLostPackets = _RaqmonQosLostPackets_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2, 1, 8),
    _RaqmonQosLostPackets_Type()
)
raqmonQosLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonQosLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    raqmonQosLostPackets.setUnits("packets")
_RaqmonQosSessionStatus_Type = SnmpAdminString
_RaqmonQosSessionStatus_Object = MibTableColumn
raqmonQosSessionStatus = _RaqmonQosSessionStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 2, 1, 9),
    _RaqmonQosSessionStatus_Type()
)
raqmonQosSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonQosSessionStatus.setStatus("current")
_RaqmonParticipantAddrTable_Object = MibTable
raqmonParticipantAddrTable = _RaqmonParticipantAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 3)
)
if mibBuilder.loadTexts:
    raqmonParticipantAddrTable.setStatus("current")
_RaqmonParticipantAddrEntry_Object = MibTableRow
raqmonParticipantAddrEntry = _RaqmonParticipantAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 3, 1)
)
raqmonParticipantAddrEntry.setIndexNames(
    (0, "RAQMON-MIB", "raqmonParticipantAddrType"),
    (0, "RAQMON-MIB", "raqmonParticipantAddr"),
    (0, "RAQMON-MIB", "raqmonParticipantStartDate"),
    (0, "RAQMON-MIB", "raqmonParticipantIndex"),
)
if mibBuilder.loadTexts:
    raqmonParticipantAddrEntry.setStatus("current")
_RaqmonParticipantAddrEndDate_Type = DateAndTime
_RaqmonParticipantAddrEndDate_Object = MibTableColumn
raqmonParticipantAddrEndDate = _RaqmonParticipantAddrEndDate_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 1, 3, 1, 1),
    _RaqmonParticipantAddrEndDate_Type()
)
raqmonParticipantAddrEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonParticipantAddrEndDate.setStatus("current")
_RaqmonException_ObjectIdentity = ObjectIdentity
raqmonException = _RaqmonException_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 2)
)
_RaqmonSessionExceptionTable_Object = MibTable
raqmonSessionExceptionTable = _RaqmonSessionExceptionTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 2, 2)
)
if mibBuilder.loadTexts:
    raqmonSessionExceptionTable.setStatus("current")
_RaqmonSessionExceptionEntry_Object = MibTableRow
raqmonSessionExceptionEntry = _RaqmonSessionExceptionEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 2, 2, 1)
)
raqmonSessionExceptionEntry.setIndexNames(
    (0, "RAQMON-MIB", "raqmonSessionExceptionIndex"),
)
if mibBuilder.loadTexts:
    raqmonSessionExceptionEntry.setStatus("current")


class _RaqmonSessionExceptionIndex_Type(Unsigned32):
    """Custom type raqmonSessionExceptionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RaqmonSessionExceptionIndex_Type.__name__ = "Unsigned32"
_RaqmonSessionExceptionIndex_Object = MibTableColumn
raqmonSessionExceptionIndex = _RaqmonSessionExceptionIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 2, 2, 1, 2),
    _RaqmonSessionExceptionIndex_Type()
)
raqmonSessionExceptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raqmonSessionExceptionIndex.setStatus("current")
_RaqmonSessionExceptionIAJitterThreshold_Type = Unsigned32
_RaqmonSessionExceptionIAJitterThreshold_Object = MibTableColumn
raqmonSessionExceptionIAJitterThreshold = _RaqmonSessionExceptionIAJitterThreshold_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 2, 2, 1, 3),
    _RaqmonSessionExceptionIAJitterThreshold_Type()
)
raqmonSessionExceptionIAJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raqmonSessionExceptionIAJitterThreshold.setStatus("current")
if mibBuilder.loadTexts:
    raqmonSessionExceptionIAJitterThreshold.setUnits("milliseconds")
_RaqmonSessionExceptionNetRTTThreshold_Type = Unsigned32
_RaqmonSessionExceptionNetRTTThreshold_Object = MibTableColumn
raqmonSessionExceptionNetRTTThreshold = _RaqmonSessionExceptionNetRTTThreshold_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 2, 2, 1, 4),
    _RaqmonSessionExceptionNetRTTThreshold_Type()
)
raqmonSessionExceptionNetRTTThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raqmonSessionExceptionNetRTTThreshold.setStatus("current")
if mibBuilder.loadTexts:
    raqmonSessionExceptionNetRTTThreshold.setUnits("milliseconds")


class _RaqmonSessionExceptionLostPacketsThreshold_Type(Unsigned32):
    """Custom type raqmonSessionExceptionLostPacketsThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RaqmonSessionExceptionLostPacketsThreshold_Type.__name__ = "Unsigned32"
_RaqmonSessionExceptionLostPacketsThreshold_Object = MibTableColumn
raqmonSessionExceptionLostPacketsThreshold = _RaqmonSessionExceptionLostPacketsThreshold_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 2, 2, 1, 5),
    _RaqmonSessionExceptionLostPacketsThreshold_Type()
)
raqmonSessionExceptionLostPacketsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raqmonSessionExceptionLostPacketsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    raqmonSessionExceptionLostPacketsThreshold.setUnits("tenth of a percent")
_RaqmonSessionExceptionRowStatus_Type = RowStatus
_RaqmonSessionExceptionRowStatus_Object = MibTableColumn
raqmonSessionExceptionRowStatus = _RaqmonSessionExceptionRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 2, 2, 1, 7),
    _RaqmonSessionExceptionRowStatus_Type()
)
raqmonSessionExceptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raqmonSessionExceptionRowStatus.setStatus("current")
_RaqmonConfig_ObjectIdentity = ObjectIdentity
raqmonConfig = _RaqmonConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 3)
)
_RaqmonConfigPort_Type = InetPortNumber
_RaqmonConfigPort_Object = MibScalar
raqmonConfigPort = _RaqmonConfigPort_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 3, 1),
    _RaqmonConfigPort_Type()
)
raqmonConfigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raqmonConfigPort.setStatus("current")


class _RaqmonConfigPduTransport_Type(Bits):
    """Custom type raqmonConfigPduTransport based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("snmp", 2),
          ("tcp", 1))
    )

_RaqmonConfigPduTransport_Type.__name__ = "Bits"
_RaqmonConfigPduTransport_Object = MibScalar
raqmonConfigPduTransport = _RaqmonConfigPduTransport_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 3, 2),
    _RaqmonConfigPduTransport_Type()
)
raqmonConfigPduTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonConfigPduTransport.setStatus("current")
_RaqmonConfigRaqmonPdus_Type = Counter32
_RaqmonConfigRaqmonPdus_Object = MibScalar
raqmonConfigRaqmonPdus = _RaqmonConfigRaqmonPdus_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 3, 3),
    _RaqmonConfigRaqmonPdus_Type()
)
raqmonConfigRaqmonPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raqmonConfigRaqmonPdus.setStatus("current")
if mibBuilder.loadTexts:
    raqmonConfigRaqmonPdus.setUnits("PDUs")
_RaqmonConfigRDSTimeout_Type = Unsigned32
_RaqmonConfigRDSTimeout_Object = MibScalar
raqmonConfigRDSTimeout = _RaqmonConfigRDSTimeout_Object(
    (1, 3, 6, 1, 2, 1, 16, 31, 1, 3, 4),
    _RaqmonConfigRDSTimeout_Type()
)
raqmonConfigRDSTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raqmonConfigRDSTimeout.setStatus("current")
_RaqmonConformance_ObjectIdentity = ObjectIdentity
raqmonConformance = _RaqmonConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 31, 2)
)
_RaqmonCompliances_ObjectIdentity = ObjectIdentity
raqmonCompliances = _RaqmonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 31, 2, 1)
)
_RaqmonGroups_ObjectIdentity = ObjectIdentity
raqmonGroups = _RaqmonGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 31, 2, 2)
)

# Managed Objects groups

raqmonCollectorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 31, 2, 2, 1)
)
raqmonCollectorGroup.setObjects(
      *(("RAQMON-MIB", "raqmonParticipantReportCaps"),
        ("RAQMON-MIB", "raqmonParticipantAddrType"),
        ("RAQMON-MIB", "raqmonParticipantAddr"),
        ("RAQMON-MIB", "raqmonParticipantSendPort"),
        ("RAQMON-MIB", "raqmonParticipantRecvPort"),
        ("RAQMON-MIB", "raqmonParticipantSetupDelay"),
        ("RAQMON-MIB", "raqmonParticipantName"),
        ("RAQMON-MIB", "raqmonParticipantAppName"),
        ("RAQMON-MIB", "raqmonParticipantQosCount"),
        ("RAQMON-MIB", "raqmonParticipantEndDate"),
        ("RAQMON-MIB", "raqmonParticipantDestPayloadType"),
        ("RAQMON-MIB", "raqmonParticipantSrcPayloadType"),
        ("RAQMON-MIB", "raqmonParticipantActive"),
        ("RAQMON-MIB", "raqmonParticipantPeer"),
        ("RAQMON-MIB", "raqmonParticipantPeerAddrType"),
        ("RAQMON-MIB", "raqmonParticipantPeerAddr"),
        ("RAQMON-MIB", "raqmonParticipantSrcL2Priority"),
        ("RAQMON-MIB", "raqmonParticipantDestL2Priority"),
        ("RAQMON-MIB", "raqmonParticipantSrcDSCP"),
        ("RAQMON-MIB", "raqmonParticipantDestDSCP"),
        ("RAQMON-MIB", "raqmonParticipantCpuMean"),
        ("RAQMON-MIB", "raqmonParticipantCpuMin"),
        ("RAQMON-MIB", "raqmonParticipantCpuMax"),
        ("RAQMON-MIB", "raqmonParticipantMemoryMean"),
        ("RAQMON-MIB", "raqmonParticipantMemoryMin"),
        ("RAQMON-MIB", "raqmonParticipantMemoryMax"),
        ("RAQMON-MIB", "raqmonParticipantNetRTTMean"),
        ("RAQMON-MIB", "raqmonParticipantNetRTTMin"),
        ("RAQMON-MIB", "raqmonParticipantNetRTTMax"),
        ("RAQMON-MIB", "raqmonParticipantIAJitterMean"),
        ("RAQMON-MIB", "raqmonParticipantIAJitterMin"),
        ("RAQMON-MIB", "raqmonParticipantIAJitterMax"),
        ("RAQMON-MIB", "raqmonParticipantIPDVMean"),
        ("RAQMON-MIB", "raqmonParticipantIPDVMin"),
        ("RAQMON-MIB", "raqmonParticipantIPDVMax"),
        ("RAQMON-MIB", "raqmonParticipantNetOwdMean"),
        ("RAQMON-MIB", "raqmonParticipantNetOwdMin"),
        ("RAQMON-MIB", "raqmonParticipantNetOwdMax"),
        ("RAQMON-MIB", "raqmonParticipantAppDelayMean"),
        ("RAQMON-MIB", "raqmonParticipantAppDelayMin"),
        ("RAQMON-MIB", "raqmonParticipantAppDelayMax"),
        ("RAQMON-MIB", "raqmonParticipantPacketsRcvd"),
        ("RAQMON-MIB", "raqmonParticipantPacketsSent"),
        ("RAQMON-MIB", "raqmonParticipantOctetsRcvd"),
        ("RAQMON-MIB", "raqmonParticipantOctetsSent"),
        ("RAQMON-MIB", "raqmonParticipantLostPackets"),
        ("RAQMON-MIB", "raqmonParticipantLostPacketsFrct"),
        ("RAQMON-MIB", "raqmonParticipantDiscards"),
        ("RAQMON-MIB", "raqmonParticipantDiscardsFrct"),
        ("RAQMON-MIB", "raqmonQoSEnd2EndNetDelay"),
        ("RAQMON-MIB", "raqmonQoSInterArrivalJitter"),
        ("RAQMON-MIB", "raqmonQosRcvdPackets"),
        ("RAQMON-MIB", "raqmonQosRcvdOctets"),
        ("RAQMON-MIB", "raqmonQosSentPackets"),
        ("RAQMON-MIB", "raqmonQosSentOctets"),
        ("RAQMON-MIB", "raqmonQosLostPackets"),
        ("RAQMON-MIB", "raqmonQosSessionStatus"),
        ("RAQMON-MIB", "raqmonParticipantAddrEndDate"),
        ("RAQMON-MIB", "raqmonConfigPort"),
        ("RAQMON-MIB", "raqmonSessionExceptionIAJitterThreshold"),
        ("RAQMON-MIB", "raqmonSessionExceptionNetRTTThreshold"),
        ("RAQMON-MIB", "raqmonSessionExceptionLostPacketsThreshold"),
        ("RAQMON-MIB", "raqmonSessionExceptionRowStatus"),
        ("RAQMON-MIB", "raqmonConfigPduTransport"),
        ("RAQMON-MIB", "raqmonConfigRaqmonPdus"),
        ("RAQMON-MIB", "raqmonConfigRDSTimeout"))
)
if mibBuilder.loadTexts:
    raqmonCollectorGroup.setStatus("current")


# Notification objects

raqmonSessionAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 31, 0, 1)
)
raqmonSessionAlarm.setObjects(
      *(("RAQMON-MIB", "raqmonParticipantAddr"),
        ("RAQMON-MIB", "raqmonParticipantName"),
        ("RAQMON-MIB", "raqmonParticipantPeerAddrType"),
        ("RAQMON-MIB", "raqmonParticipantPeerAddr"),
        ("RAQMON-MIB", "raqmonQoSEnd2EndNetDelay"),
        ("RAQMON-MIB", "raqmonQoSInterArrivalJitter"),
        ("RAQMON-MIB", "raqmonQosLostPackets"),
        ("RAQMON-MIB", "raqmonQosRcvdPackets"))
)
if mibBuilder.loadTexts:
    raqmonSessionAlarm.setStatus(
        "current"
    )


# Notifications groups

raqmonCollectorNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 16, 31, 2, 2, 2)
)
raqmonCollectorNotificationsGroup.setObjects(
    ("RAQMON-MIB", "raqmonSessionAlarm")
)
if mibBuilder.loadTexts:
    raqmonCollectorNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

raqmonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 31, 2, 1, 1)
)
if mibBuilder.loadTexts:
    raqmonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAQMON-MIB",
    **{"raqmonMIB": raqmonMIB,
       "raqmonNotifications": raqmonNotifications,
       "raqmonSessionAlarm": raqmonSessionAlarm,
       "raqmonMIBObjects": raqmonMIBObjects,
       "raqmonSession": raqmonSession,
       "raqmonParticipantTable": raqmonParticipantTable,
       "raqmonParticipantEntry": raqmonParticipantEntry,
       "raqmonParticipantStartDate": raqmonParticipantStartDate,
       "raqmonParticipantIndex": raqmonParticipantIndex,
       "raqmonParticipantReportCaps": raqmonParticipantReportCaps,
       "raqmonParticipantAddrType": raqmonParticipantAddrType,
       "raqmonParticipantAddr": raqmonParticipantAddr,
       "raqmonParticipantSendPort": raqmonParticipantSendPort,
       "raqmonParticipantRecvPort": raqmonParticipantRecvPort,
       "raqmonParticipantSetupDelay": raqmonParticipantSetupDelay,
       "raqmonParticipantName": raqmonParticipantName,
       "raqmonParticipantAppName": raqmonParticipantAppName,
       "raqmonParticipantQosCount": raqmonParticipantQosCount,
       "raqmonParticipantEndDate": raqmonParticipantEndDate,
       "raqmonParticipantDestPayloadType": raqmonParticipantDestPayloadType,
       "raqmonParticipantSrcPayloadType": raqmonParticipantSrcPayloadType,
       "raqmonParticipantActive": raqmonParticipantActive,
       "raqmonParticipantPeer": raqmonParticipantPeer,
       "raqmonParticipantPeerAddrType": raqmonParticipantPeerAddrType,
       "raqmonParticipantPeerAddr": raqmonParticipantPeerAddr,
       "raqmonParticipantSrcL2Priority": raqmonParticipantSrcL2Priority,
       "raqmonParticipantDestL2Priority": raqmonParticipantDestL2Priority,
       "raqmonParticipantSrcDSCP": raqmonParticipantSrcDSCP,
       "raqmonParticipantDestDSCP": raqmonParticipantDestDSCP,
       "raqmonParticipantCpuMean": raqmonParticipantCpuMean,
       "raqmonParticipantCpuMin": raqmonParticipantCpuMin,
       "raqmonParticipantCpuMax": raqmonParticipantCpuMax,
       "raqmonParticipantMemoryMean": raqmonParticipantMemoryMean,
       "raqmonParticipantMemoryMin": raqmonParticipantMemoryMin,
       "raqmonParticipantMemoryMax": raqmonParticipantMemoryMax,
       "raqmonParticipantNetRTTMean": raqmonParticipantNetRTTMean,
       "raqmonParticipantNetRTTMin": raqmonParticipantNetRTTMin,
       "raqmonParticipantNetRTTMax": raqmonParticipantNetRTTMax,
       "raqmonParticipantIAJitterMean": raqmonParticipantIAJitterMean,
       "raqmonParticipantIAJitterMin": raqmonParticipantIAJitterMin,
       "raqmonParticipantIAJitterMax": raqmonParticipantIAJitterMax,
       "raqmonParticipantIPDVMean": raqmonParticipantIPDVMean,
       "raqmonParticipantIPDVMin": raqmonParticipantIPDVMin,
       "raqmonParticipantIPDVMax": raqmonParticipantIPDVMax,
       "raqmonParticipantNetOwdMean": raqmonParticipantNetOwdMean,
       "raqmonParticipantNetOwdMin": raqmonParticipantNetOwdMin,
       "raqmonParticipantNetOwdMax": raqmonParticipantNetOwdMax,
       "raqmonParticipantAppDelayMean": raqmonParticipantAppDelayMean,
       "raqmonParticipantAppDelayMin": raqmonParticipantAppDelayMin,
       "raqmonParticipantAppDelayMax": raqmonParticipantAppDelayMax,
       "raqmonParticipantPacketsRcvd": raqmonParticipantPacketsRcvd,
       "raqmonParticipantPacketsSent": raqmonParticipantPacketsSent,
       "raqmonParticipantOctetsRcvd": raqmonParticipantOctetsRcvd,
       "raqmonParticipantOctetsSent": raqmonParticipantOctetsSent,
       "raqmonParticipantLostPackets": raqmonParticipantLostPackets,
       "raqmonParticipantLostPacketsFrct": raqmonParticipantLostPacketsFrct,
       "raqmonParticipantDiscards": raqmonParticipantDiscards,
       "raqmonParticipantDiscardsFrct": raqmonParticipantDiscardsFrct,
       "raqmonQosTable": raqmonQosTable,
       "raqmonQosEntry": raqmonQosEntry,
       "raqmonQosTime": raqmonQosTime,
       "raqmonQoSEnd2EndNetDelay": raqmonQoSEnd2EndNetDelay,
       "raqmonQoSInterArrivalJitter": raqmonQoSInterArrivalJitter,
       "raqmonQosRcvdPackets": raqmonQosRcvdPackets,
       "raqmonQosRcvdOctets": raqmonQosRcvdOctets,
       "raqmonQosSentPackets": raqmonQosSentPackets,
       "raqmonQosSentOctets": raqmonQosSentOctets,
       "raqmonQosLostPackets": raqmonQosLostPackets,
       "raqmonQosSessionStatus": raqmonQosSessionStatus,
       "raqmonParticipantAddrTable": raqmonParticipantAddrTable,
       "raqmonParticipantAddrEntry": raqmonParticipantAddrEntry,
       "raqmonParticipantAddrEndDate": raqmonParticipantAddrEndDate,
       "raqmonException": raqmonException,
       "raqmonSessionExceptionTable": raqmonSessionExceptionTable,
       "raqmonSessionExceptionEntry": raqmonSessionExceptionEntry,
       "raqmonSessionExceptionIndex": raqmonSessionExceptionIndex,
       "raqmonSessionExceptionIAJitterThreshold": raqmonSessionExceptionIAJitterThreshold,
       "raqmonSessionExceptionNetRTTThreshold": raqmonSessionExceptionNetRTTThreshold,
       "raqmonSessionExceptionLostPacketsThreshold": raqmonSessionExceptionLostPacketsThreshold,
       "raqmonSessionExceptionRowStatus": raqmonSessionExceptionRowStatus,
       "raqmonConfig": raqmonConfig,
       "raqmonConfigPort": raqmonConfigPort,
       "raqmonConfigPduTransport": raqmonConfigPduTransport,
       "raqmonConfigRaqmonPdus": raqmonConfigRaqmonPdus,
       "raqmonConfigRDSTimeout": raqmonConfigRDSTimeout,
       "raqmonConformance": raqmonConformance,
       "raqmonCompliances": raqmonCompliances,
       "raqmonCompliance": raqmonCompliance,
       "raqmonGroups": raqmonGroups,
       "raqmonCollectorGroup": raqmonCollectorGroup,
       "raqmonCollectorNotificationsGroup": raqmonCollectorNotificationsGroup}
)
