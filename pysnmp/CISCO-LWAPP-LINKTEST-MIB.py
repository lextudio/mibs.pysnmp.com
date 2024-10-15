# SNMP MIB module (CISCO-LWAPP-LINKTEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-LINKTEST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:38 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappLinkTestMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 516)
)
ciscoLwappLinkTestMIB.setRevisions(
        ("2006-04-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappLinkTestMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappLinkTestMIBNotifs = _CiscoLwappLinkTestMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 0)
)
_CiscoLwappLinkTestMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappLinkTestMIBObjects = _CiscoLwappLinkTestMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1)
)
_CiscoLwappLinkTestConfig_ObjectIdentity = ObjectIdentity
ciscoLwappLinkTestConfig = _CiscoLwappLinkTestConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 1)
)


class _CLLtResponder_Type(TruthValue):
    """Custom type cLLtResponder based on TruthValue"""


_CLLtResponder_Object = MibScalar
cLLtResponder = _CLLtResponder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 1, 1),
    _CLLtResponder_Type()
)
cLLtResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLLtResponder.setStatus("current")


class _CLLtPacketSize_Type(Unsigned32):
    """Custom type cLLtPacketSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_CLLtPacketSize_Type.__name__ = "Unsigned32"
_CLLtPacketSize_Object = MibScalar
cLLtPacketSize = _CLLtPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 1, 2),
    _CLLtPacketSize_Type()
)
cLLtPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLLtPacketSize.setStatus("current")


class _CLLtNumberOfPackets_Type(Unsigned32):
    """Custom type cLLtNumberOfPackets based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLLtNumberOfPackets_Type.__name__ = "Unsigned32"
_CLLtNumberOfPackets_Object = MibScalar
cLLtNumberOfPackets = _CLLtNumberOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 1, 3),
    _CLLtNumberOfPackets_Type()
)
cLLtNumberOfPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLLtNumberOfPackets.setStatus("current")


class _CLLtTestPurgeTime_Type(Unsigned32):
    """Custom type cLLtTestPurgeTime based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1800),
    )


_CLLtTestPurgeTime_Type.__name__ = "Unsigned32"
_CLLtTestPurgeTime_Object = MibScalar
cLLtTestPurgeTime = _CLLtTestPurgeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 1, 4),
    _CLLtTestPurgeTime_Type()
)
cLLtTestPurgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLLtTestPurgeTime.setStatus("current")
if mibBuilder.loadTexts:
    cLLtTestPurgeTime.setUnits("seconds")
_CiscoLwappLinkTestRun_ObjectIdentity = ObjectIdentity
ciscoLwappLinkTestRun = _CiscoLwappLinkTestRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2)
)
_CLLtClientLinkTestTable_Object = MibTable
cLLtClientLinkTestTable = _CLLtClientLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLLtClientLinkTestTable.setStatus("current")
_CLLtClientLinkTestEntry_Object = MibTableRow
cLLtClientLinkTestEntry = _CLLtClientLinkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 1, 1)
)
cLLtClientLinkTestEntry.setIndexNames(
    (0, "CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtIndex"),
)
if mibBuilder.loadTexts:
    cLLtClientLinkTestEntry.setStatus("current")


class _CLLtClientLtIndex_Type(Unsigned32):
    """Custom type cLLtClientLtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CLLtClientLtIndex_Type.__name__ = "Unsigned32"
_CLLtClientLtIndex_Object = MibTableColumn
cLLtClientLtIndex = _CLLtClientLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 1, 1, 1),
    _CLLtClientLtIndex_Type()
)
cLLtClientLtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLLtClientLtIndex.setStatus("current")
_CLLtClientLtMacAddress_Type = MacAddress
_CLLtClientLtMacAddress_Object = MibTableColumn
cLLtClientLtMacAddress = _CLLtClientLtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 1, 1, 2),
    _CLLtClientLtMacAddress_Type()
)
cLLtClientLtMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLLtClientLtMacAddress.setStatus("current")
_CLLtClientLtRowStatus_Type = RowStatus
_CLLtClientLtRowStatus_Object = MibTableColumn
cLLtClientLtRowStatus = _CLLtClientLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 1, 1, 3),
    _CLLtClientLtRowStatus_Type()
)
cLLtClientLtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLLtClientLtRowStatus.setStatus("current")
_CLLtClientLTResultsTable_Object = MibTable
cLLtClientLTResultsTable = _CLLtClientLTResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cLLtClientLTResultsTable.setStatus("current")
_CLLtClientLTResultsEntry_Object = MibTableRow
cLLtClientLTResultsEntry = _CLLtClientLTResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1)
)
cLLtClientLTResultsEntry.setIndexNames(
    (0, "CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtIndex"),
)
if mibBuilder.loadTexts:
    cLLtClientLTResultsEntry.setStatus("current")
_CLLtClientLtPacketsSent_Type = Counter32
_CLLtClientLtPacketsSent_Object = MibTableColumn
cLLtClientLtPacketsSent = _CLLtClientLtPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 1),
    _CLLtClientLtPacketsSent_Type()
)
cLLtClientLtPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtPacketsSent.setUnits("packets")
_CLLtClientLtPacketsRx_Type = Counter32
_CLLtClientLtPacketsRx_Object = MibTableColumn
cLLtClientLtPacketsRx = _CLLtClientLtPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 2),
    _CLLtClientLtPacketsRx_Type()
)
cLLtClientLtPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtPacketsRx.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtPacketsRx.setUnits("packets")
_CLLtClientLtTotalPacketsLost_Type = Counter32
_CLLtClientLtTotalPacketsLost_Object = MibTableColumn
cLLtClientLtTotalPacketsLost = _CLLtClientLtTotalPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 3),
    _CLLtClientLtTotalPacketsLost_Type()
)
cLLtClientLtTotalPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtTotalPacketsLost.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtTotalPacketsLost.setUnits("packets")
_CLLtClientLtApToClientPktsLost_Type = Counter32
_CLLtClientLtApToClientPktsLost_Object = MibTableColumn
cLLtClientLtApToClientPktsLost = _CLLtClientLtApToClientPktsLost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 4),
    _CLLtClientLtApToClientPktsLost_Type()
)
cLLtClientLtApToClientPktsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtApToClientPktsLost.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtApToClientPktsLost.setUnits("packets")
_CLLtClientLtClientToApPktsLost_Type = Counter32
_CLLtClientLtClientToApPktsLost_Object = MibTableColumn
cLLtClientLtClientToApPktsLost = _CLLtClientLtClientToApPktsLost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 5),
    _CLLtClientLtClientToApPktsLost_Type()
)
cLLtClientLtClientToApPktsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtClientToApPktsLost.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtClientToApPktsLost.setUnits("packets")
_CLLtClientLtMinRoundTripTime_Type = TimeInterval
_CLLtClientLtMinRoundTripTime_Object = MibTableColumn
cLLtClientLtMinRoundTripTime = _CLLtClientLtMinRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 6),
    _CLLtClientLtMinRoundTripTime_Type()
)
cLLtClientLtMinRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtMinRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtMinRoundTripTime.setUnits("hundredths-seconds")
_CLLtClientLtMaxRoundTripTime_Type = TimeInterval
_CLLtClientLtMaxRoundTripTime_Object = MibTableColumn
cLLtClientLtMaxRoundTripTime = _CLLtClientLtMaxRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 7),
    _CLLtClientLtMaxRoundTripTime_Type()
)
cLLtClientLtMaxRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtMaxRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtMaxRoundTripTime.setUnits("hundredths-seconds")
_CLLtClientLtAvgRoundTripTime_Type = TimeInterval
_CLLtClientLtAvgRoundTripTime_Object = MibTableColumn
cLLtClientLtAvgRoundTripTime = _CLLtClientLtAvgRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 8),
    _CLLtClientLtAvgRoundTripTime_Type()
)
cLLtClientLtAvgRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtAvgRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtAvgRoundTripTime.setUnits("hundredths-seconds")
_CLLtClientLtUplinkMinRSSI_Type = Integer32
_CLLtClientLtUplinkMinRSSI_Object = MibTableColumn
cLLtClientLtUplinkMinRSSI = _CLLtClientLtUplinkMinRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 9),
    _CLLtClientLtUplinkMinRSSI_Type()
)
cLLtClientLtUplinkMinRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkMinRSSI.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkMinRSSI.setUnits("dBm")
_CLLtClientLtUplinkMaxRSSI_Type = Integer32
_CLLtClientLtUplinkMaxRSSI_Object = MibTableColumn
cLLtClientLtUplinkMaxRSSI = _CLLtClientLtUplinkMaxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 10),
    _CLLtClientLtUplinkMaxRSSI_Type()
)
cLLtClientLtUplinkMaxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkMaxRSSI.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkMaxRSSI.setUnits("dBm")
_CLLtClientLtUplinkAvgRSSI_Type = Integer32
_CLLtClientLtUplinkAvgRSSI_Object = MibTableColumn
cLLtClientLtUplinkAvgRSSI = _CLLtClientLtUplinkAvgRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 11),
    _CLLtClientLtUplinkAvgRSSI_Type()
)
cLLtClientLtUplinkAvgRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkAvgRSSI.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkAvgRSSI.setUnits("dBm")
_CLLtClientLtDownlinkMinRSSI_Type = Integer32
_CLLtClientLtDownlinkMinRSSI_Object = MibTableColumn
cLLtClientLtDownlinkMinRSSI = _CLLtClientLtDownlinkMinRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 12),
    _CLLtClientLtDownlinkMinRSSI_Type()
)
cLLtClientLtDownlinkMinRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkMinRSSI.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkMinRSSI.setUnits("dBm")
_CLLtClientLtDownlinkMaxRSSI_Type = Integer32
_CLLtClientLtDownlinkMaxRSSI_Object = MibTableColumn
cLLtClientLtDownlinkMaxRSSI = _CLLtClientLtDownlinkMaxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 13),
    _CLLtClientLtDownlinkMaxRSSI_Type()
)
cLLtClientLtDownlinkMaxRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkMaxRSSI.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkMaxRSSI.setUnits("dBm")
_CLLtClientLtDownlinkAvgRSSI_Type = Integer32
_CLLtClientLtDownlinkAvgRSSI_Object = MibTableColumn
cLLtClientLtDownlinkAvgRSSI = _CLLtClientLtDownlinkAvgRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 14),
    _CLLtClientLtDownlinkAvgRSSI_Type()
)
cLLtClientLtDownlinkAvgRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkAvgRSSI.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkAvgRSSI.setUnits("dBm")
_CLLtClientLtUplinkMinSNR_Type = Integer32
_CLLtClientLtUplinkMinSNR_Object = MibTableColumn
cLLtClientLtUplinkMinSNR = _CLLtClientLtUplinkMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 15),
    _CLLtClientLtUplinkMinSNR_Type()
)
cLLtClientLtUplinkMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkMinSNR.setUnits("dB")
_CLLtClientLtUplinkMaxSNR_Type = Integer32
_CLLtClientLtUplinkMaxSNR_Object = MibTableColumn
cLLtClientLtUplinkMaxSNR = _CLLtClientLtUplinkMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 16),
    _CLLtClientLtUplinkMaxSNR_Type()
)
cLLtClientLtUplinkMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkMaxSNR.setUnits("dB")
_CLLtClientLtUplinkAvgSNR_Type = Integer32
_CLLtClientLtUplinkAvgSNR_Object = MibTableColumn
cLLtClientLtUplinkAvgSNR = _CLLtClientLtUplinkAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 17),
    _CLLtClientLtUplinkAvgSNR_Type()
)
cLLtClientLtUplinkAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtUplinkAvgSNR.setUnits("dB")
_CLLtClientLtDownlinkMinSNR_Type = Integer32
_CLLtClientLtDownlinkMinSNR_Object = MibTableColumn
cLLtClientLtDownlinkMinSNR = _CLLtClientLtDownlinkMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 18),
    _CLLtClientLtDownlinkMinSNR_Type()
)
cLLtClientLtDownlinkMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkMinSNR.setUnits("dB")
_CLLtClientLtDownlinkMaxSNR_Type = Integer32
_CLLtClientLtDownlinkMaxSNR_Object = MibTableColumn
cLLtClientLtDownlinkMaxSNR = _CLLtClientLtDownlinkMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 19),
    _CLLtClientLtDownlinkMaxSNR_Type()
)
cLLtClientLtDownlinkMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkMaxSNR.setUnits("dB")
_CLLtClientLtDownlinkAvgSNR_Type = Integer32
_CLLtClientLtDownlinkAvgSNR_Object = MibTableColumn
cLLtClientLtDownlinkAvgSNR = _CLLtClientLtDownlinkAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 20),
    _CLLtClientLtDownlinkAvgSNR_Type()
)
cLLtClientLtDownlinkAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtDownlinkAvgSNR.setUnits("dB")
_CLLtClientLtTotalTxRetriesAP_Type = Counter32
_CLLtClientLtTotalTxRetriesAP_Object = MibTableColumn
cLLtClientLtTotalTxRetriesAP = _CLLtClientLtTotalTxRetriesAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 21),
    _CLLtClientLtTotalTxRetriesAP_Type()
)
cLLtClientLtTotalTxRetriesAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtTotalTxRetriesAP.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtTotalTxRetriesAP.setUnits("retries")
_CLLtClientLtMaxTxRetriesAP_Type = Counter32
_CLLtClientLtMaxTxRetriesAP_Object = MibTableColumn
cLLtClientLtMaxTxRetriesAP = _CLLtClientLtMaxTxRetriesAP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 22),
    _CLLtClientLtMaxTxRetriesAP_Type()
)
cLLtClientLtMaxTxRetriesAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtMaxTxRetriesAP.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtMaxTxRetriesAP.setUnits("retries")
_CLLtClientLtTotalTxRetriesClient_Type = Counter32
_CLLtClientLtTotalTxRetriesClient_Object = MibTableColumn
cLLtClientLtTotalTxRetriesClient = _CLLtClientLtTotalTxRetriesClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 23),
    _CLLtClientLtTotalTxRetriesClient_Type()
)
cLLtClientLtTotalTxRetriesClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtTotalTxRetriesClient.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtTotalTxRetriesClient.setUnits("retries")
_CLLtClientLtMaxTxRetriesClient_Type = Counter32
_CLLtClientLtMaxTxRetriesClient_Object = MibTableColumn
cLLtClientLtMaxTxRetriesClient = _CLLtClientLtMaxTxRetriesClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 24),
    _CLLtClientLtMaxTxRetriesClient_Type()
)
cLLtClientLtMaxTxRetriesClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtMaxTxRetriesClient.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtMaxTxRetriesClient.setUnits("retries")


class _CLLtClientLtStatus_Type(Integer32):
    """Custom type cLLtClientLtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cLLtClientLtStatusCcxInProgress", 1),
          ("cLLtClientLtStatusCcxLtSuccess", 4),
          ("cLLtClientLtStatusFailed", 0),
          ("cLLtClientLtStatusPingSuccess", 3),
          ("cLLtClientLtStatusPngInProgress", 2))
    )


_CLLtClientLtStatus_Type.__name__ = "Integer32"
_CLLtClientLtStatus_Object = MibTableColumn
cLLtClientLtStatus = _CLLtClientLtStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 25),
    _CLLtClientLtStatus_Type()
)
cLLtClientLtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtStatus.setStatus("current")
_CiscoLwappLinkTestStatus_ObjectIdentity = ObjectIdentity
ciscoLwappLinkTestStatus = _CiscoLwappLinkTestStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3)
)
_CLLtClientLtDataRateTable_Object = MibTable
cLLtClientLtDataRateTable = _CLLtClientLtDataRateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLLtClientLtDataRateTable.setStatus("current")
_CLLtClientLtDataRateEntry_Object = MibTableRow
cLLtClientLtDataRateEntry = _CLLtClientLtDataRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3, 1, 1)
)
cLLtClientLtDataRateEntry.setIndexNames(
    (0, "CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtIndex"),
    (0, "CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDataRate"),
)
if mibBuilder.loadTexts:
    cLLtClientLtDataRateEntry.setStatus("current")


class _CLLtClientLtDataRate_Type(OctetString):
    """Custom type cLLtClientLtDataRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLLtClientLtDataRate_Type.__name__ = "OctetString"
_CLLtClientLtDataRate_Object = MibTableColumn
cLLtClientLtDataRate = _CLLtClientLtDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3, 1, 1, 1),
    _CLLtClientLtDataRate_Type()
)
cLLtClientLtDataRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLLtClientLtDataRate.setStatus("current")
_CLLtClientLtRateDownlinkPktsSent_Type = Counter32
_CLLtClientLtRateDownlinkPktsSent_Object = MibTableColumn
cLLtClientLtRateDownlinkPktsSent = _CLLtClientLtRateDownlinkPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3, 1, 1, 2),
    _CLLtClientLtRateDownlinkPktsSent_Type()
)
cLLtClientLtRateDownlinkPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtRateDownlinkPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtRateDownlinkPktsSent.setUnits("packets")
_CLLtClientLtRateUplinkPktsSent_Type = Counter32
_CLLtClientLtRateUplinkPktsSent_Object = MibTableColumn
cLLtClientLtRateUplinkPktsSent = _CLLtClientLtRateUplinkPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3, 1, 1, 3),
    _CLLtClientLtRateUplinkPktsSent_Type()
)
cLLtClientLtRateUplinkPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLtClientLtRateUplinkPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    cLLtClientLtRateUplinkPktsSent.setUnits("packets")
_CiscoLwappLinkTestMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappLinkTestMIBConform = _CiscoLwappLinkTestMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 2)
)
_CiscoLwappLinkTestMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappLinkTestMIBCompliances = _CiscoLwappLinkTestMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 1)
)
_CiscoLwappLinkTestMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappLinkTestMIBGroups = _CiscoLwappLinkTestMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 2)
)

# Managed Objects groups

cLLinkTestConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 2, 1)
)
cLLinkTestConfigGroup.setObjects(
      *(("CISCO-LWAPP-LINKTEST-MIB", "cLLtResponder"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtPacketSize"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtNumberOfPackets"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtTestPurgeTime"))
)
if mibBuilder.loadTexts:
    cLLinkTestConfigGroup.setStatus("current")

cLLinkTestRunsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 2, 2)
)
cLLinkTestRunsGroup.setObjects(
      *(("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtMacAddress"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtPacketsSent"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtPacketsRx"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtTotalPacketsLost"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtApToClientPktsLost"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtClientToApPktsLost"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtMinRoundTripTime"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtMaxRoundTripTime"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtAvgRoundTripTime"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkMinRSSI"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkMaxRSSI"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkAvgRSSI"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkMinRSSI"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkMaxRSSI"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkAvgRSSI"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkMinSNR"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkMaxSNR"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkAvgSNR"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkMinSNR"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkMaxSNR"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkAvgSNR"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtTotalTxRetriesAP"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtMaxTxRetriesAP"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtTotalTxRetriesClient"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtMaxTxRetriesClient"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtStatus"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtRowStatus"))
)
if mibBuilder.loadTexts:
    cLLinkTestRunsGroup.setStatus("current")

cLLinkTestStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 2, 3)
)
cLLinkTestStatusGroup.setObjects(
      *(("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtRateDownlinkPktsSent"),
        ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtRateUplinkPktsSent"))
)
if mibBuilder.loadTexts:
    cLLinkTestStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappLinkTestMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappLinkTestMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-LINKTEST-MIB",
    **{"ciscoLwappLinkTestMIB": ciscoLwappLinkTestMIB,
       "ciscoLwappLinkTestMIBNotifs": ciscoLwappLinkTestMIBNotifs,
       "ciscoLwappLinkTestMIBObjects": ciscoLwappLinkTestMIBObjects,
       "ciscoLwappLinkTestConfig": ciscoLwappLinkTestConfig,
       "cLLtResponder": cLLtResponder,
       "cLLtPacketSize": cLLtPacketSize,
       "cLLtNumberOfPackets": cLLtNumberOfPackets,
       "cLLtTestPurgeTime": cLLtTestPurgeTime,
       "ciscoLwappLinkTestRun": ciscoLwappLinkTestRun,
       "cLLtClientLinkTestTable": cLLtClientLinkTestTable,
       "cLLtClientLinkTestEntry": cLLtClientLinkTestEntry,
       "cLLtClientLtIndex": cLLtClientLtIndex,
       "cLLtClientLtMacAddress": cLLtClientLtMacAddress,
       "cLLtClientLtRowStatus": cLLtClientLtRowStatus,
       "cLLtClientLTResultsTable": cLLtClientLTResultsTable,
       "cLLtClientLTResultsEntry": cLLtClientLTResultsEntry,
       "cLLtClientLtPacketsSent": cLLtClientLtPacketsSent,
       "cLLtClientLtPacketsRx": cLLtClientLtPacketsRx,
       "cLLtClientLtTotalPacketsLost": cLLtClientLtTotalPacketsLost,
       "cLLtClientLtApToClientPktsLost": cLLtClientLtApToClientPktsLost,
       "cLLtClientLtClientToApPktsLost": cLLtClientLtClientToApPktsLost,
       "cLLtClientLtMinRoundTripTime": cLLtClientLtMinRoundTripTime,
       "cLLtClientLtMaxRoundTripTime": cLLtClientLtMaxRoundTripTime,
       "cLLtClientLtAvgRoundTripTime": cLLtClientLtAvgRoundTripTime,
       "cLLtClientLtUplinkMinRSSI": cLLtClientLtUplinkMinRSSI,
       "cLLtClientLtUplinkMaxRSSI": cLLtClientLtUplinkMaxRSSI,
       "cLLtClientLtUplinkAvgRSSI": cLLtClientLtUplinkAvgRSSI,
       "cLLtClientLtDownlinkMinRSSI": cLLtClientLtDownlinkMinRSSI,
       "cLLtClientLtDownlinkMaxRSSI": cLLtClientLtDownlinkMaxRSSI,
       "cLLtClientLtDownlinkAvgRSSI": cLLtClientLtDownlinkAvgRSSI,
       "cLLtClientLtUplinkMinSNR": cLLtClientLtUplinkMinSNR,
       "cLLtClientLtUplinkMaxSNR": cLLtClientLtUplinkMaxSNR,
       "cLLtClientLtUplinkAvgSNR": cLLtClientLtUplinkAvgSNR,
       "cLLtClientLtDownlinkMinSNR": cLLtClientLtDownlinkMinSNR,
       "cLLtClientLtDownlinkMaxSNR": cLLtClientLtDownlinkMaxSNR,
       "cLLtClientLtDownlinkAvgSNR": cLLtClientLtDownlinkAvgSNR,
       "cLLtClientLtTotalTxRetriesAP": cLLtClientLtTotalTxRetriesAP,
       "cLLtClientLtMaxTxRetriesAP": cLLtClientLtMaxTxRetriesAP,
       "cLLtClientLtTotalTxRetriesClient": cLLtClientLtTotalTxRetriesClient,
       "cLLtClientLtMaxTxRetriesClient": cLLtClientLtMaxTxRetriesClient,
       "cLLtClientLtStatus": cLLtClientLtStatus,
       "ciscoLwappLinkTestStatus": ciscoLwappLinkTestStatus,
       "cLLtClientLtDataRateTable": cLLtClientLtDataRateTable,
       "cLLtClientLtDataRateEntry": cLLtClientLtDataRateEntry,
       "cLLtClientLtDataRate": cLLtClientLtDataRate,
       "cLLtClientLtRateDownlinkPktsSent": cLLtClientLtRateDownlinkPktsSent,
       "cLLtClientLtRateUplinkPktsSent": cLLtClientLtRateUplinkPktsSent,
       "ciscoLwappLinkTestMIBConform": ciscoLwappLinkTestMIBConform,
       "ciscoLwappLinkTestMIBCompliances": ciscoLwappLinkTestMIBCompliances,
       "ciscoLwappLinkTestMIBCompliance": ciscoLwappLinkTestMIBCompliance,
       "ciscoLwappLinkTestMIBGroups": ciscoLwappLinkTestMIBGroups,
       "cLLinkTestConfigGroup": cLLinkTestConfigGroup,
       "cLLinkTestRunsGroup": cLLinkTestRunsGroup,
       "cLLinkTestStatusGroup": cLLinkTestStatusGroup}
)
