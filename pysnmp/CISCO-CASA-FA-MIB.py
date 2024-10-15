# SNMP MIB module (CISCO-CASA-FA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CASA-FA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:58 2024
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

(CiscoIpProtocol,
 CiscoPort) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoIpProtocol",
    "CiscoPort")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCasaFaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115)
)
ciscoCasaFaMIB.setRevisions(
        ("2002-09-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CasaWildcardAffIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )



class CasaInterestPacketSpecification(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCasaFaMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCasaFaMIBObjects = _CiscoCasaFaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1)
)
_CcfaGlobal_ObjectIdentity = ObjectIdentity
ccfaGlobal = _CcfaGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 1)
)
_CcfaStats_ObjectIdentity = ObjectIdentity
ccfaStats = _CcfaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 2)
)
_CcfaWildcardAff_ObjectIdentity = ObjectIdentity
ccfaWildcardAff = _CcfaWildcardAff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3)
)
_CcfaWildcardAffTotalBytes_Type = Counter32
_CcfaWildcardAffTotalBytes_Object = MibScalar
ccfaWildcardAffTotalBytes = _CcfaWildcardAffTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 1),
    _CcfaWildcardAffTotalBytes_Type()
)
ccfaWildcardAffTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffTotalBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffTotalBytes.setUnits("bytes")
_CcfaWildcardAffHCTotalBytes_Type = Counter64
_CcfaWildcardAffHCTotalBytes_Object = MibScalar
ccfaWildcardAffHCTotalBytes = _CcfaWildcardAffHCTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 2),
    _CcfaWildcardAffHCTotalBytes_Type()
)
ccfaWildcardAffHCTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffHCTotalBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffHCTotalBytes.setUnits("bytes")
_CcfaWildcardAffTotalPackets_Type = Counter32
_CcfaWildcardAffTotalPackets_Object = MibScalar
ccfaWildcardAffTotalPackets = _CcfaWildcardAffTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 3),
    _CcfaWildcardAffTotalPackets_Type()
)
ccfaWildcardAffTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffTotalPackets.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffTotalPackets.setUnits("packets")
_CcfaWildcardAffNumOf_Type = Gauge32
_CcfaWildcardAffNumOf_Object = MibScalar
ccfaWildcardAffNumOf = _CcfaWildcardAffNumOf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 4),
    _CcfaWildcardAffNumOf_Type()
)
ccfaWildcardAffNumOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffNumOf.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffNumOf.setUnits("affinities")


class _CcfaWildcardAffNotifEnabled_Type(TruthValue):
    """Custom type ccfaWildcardAffNotifEnabled based on TruthValue"""


_CcfaWildcardAffNotifEnabled_Object = MibScalar
ccfaWildcardAffNotifEnabled = _CcfaWildcardAffNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 5),
    _CcfaWildcardAffNotifEnabled_Type()
)
ccfaWildcardAffNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccfaWildcardAffNotifEnabled.setStatus("current")
_CcfaWildcardAffTable_Object = MibTable
ccfaWildcardAffTable = _CcfaWildcardAffTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6)
)
if mibBuilder.loadTexts:
    ccfaWildcardAffTable.setStatus("current")
_CcfaWildcardAffEntry_Object = MibTableRow
ccfaWildcardAffEntry = _CcfaWildcardAffEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1)
)
ccfaWildcardAffEntry.setIndexNames(
    (0, "CISCO-CASA-FA-MIB", "ccfaWildcardAffIndex"),
)
if mibBuilder.loadTexts:
    ccfaWildcardAffEntry.setStatus("current")
_CcfaWildcardAffIndex_Type = CasaWildcardAffIndex
_CcfaWildcardAffIndex_Object = MibTableColumn
ccfaWildcardAffIndex = _CcfaWildcardAffIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 1),
    _CcfaWildcardAffIndex_Type()
)
ccfaWildcardAffIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccfaWildcardAffIndex.setStatus("current")
_CcfaWildcardAffSourceAddr_Type = IpAddress
_CcfaWildcardAffSourceAddr_Object = MibTableColumn
ccfaWildcardAffSourceAddr = _CcfaWildcardAffSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 2),
    _CcfaWildcardAffSourceAddr_Type()
)
ccfaWildcardAffSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffSourceAddr.setStatus("current")
_CcfaWildcardAffDestinationAddr_Type = IpAddress
_CcfaWildcardAffDestinationAddr_Object = MibTableColumn
ccfaWildcardAffDestinationAddr = _CcfaWildcardAffDestinationAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 3),
    _CcfaWildcardAffDestinationAddr_Type()
)
ccfaWildcardAffDestinationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffDestinationAddr.setStatus("current")
_CcfaWildcardAffSourcePort_Type = CiscoPort
_CcfaWildcardAffSourcePort_Object = MibTableColumn
ccfaWildcardAffSourcePort = _CcfaWildcardAffSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 4),
    _CcfaWildcardAffSourcePort_Type()
)
ccfaWildcardAffSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffSourcePort.setStatus("current")
_CcfaWildcardAffDestinationPort_Type = CiscoPort
_CcfaWildcardAffDestinationPort_Object = MibTableColumn
ccfaWildcardAffDestinationPort = _CcfaWildcardAffDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 5),
    _CcfaWildcardAffDestinationPort_Type()
)
ccfaWildcardAffDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffDestinationPort.setStatus("current")
_CcfaWildcardAffProtocol_Type = CiscoIpProtocol
_CcfaWildcardAffProtocol_Object = MibTableColumn
ccfaWildcardAffProtocol = _CcfaWildcardAffProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 6),
    _CcfaWildcardAffProtocol_Type()
)
ccfaWildcardAffProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffProtocol.setStatus("current")
_CcfaWildcardAffFragment_Type = TruthValue
_CcfaWildcardAffFragment_Object = MibTableColumn
ccfaWildcardAffFragment = _CcfaWildcardAffFragment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 7),
    _CcfaWildcardAffFragment_Type()
)
ccfaWildcardAffFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffFragment.setStatus("current")
_CcfaWildcardAffSourceMask_Type = IpAddress
_CcfaWildcardAffSourceMask_Object = MibTableColumn
ccfaWildcardAffSourceMask = _CcfaWildcardAffSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 8),
    _CcfaWildcardAffSourceMask_Type()
)
ccfaWildcardAffSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffSourceMask.setStatus("current")
_CcfaWildcardAffDestinationMask_Type = IpAddress
_CcfaWildcardAffDestinationMask_Object = MibTableColumn
ccfaWildcardAffDestinationMask = _CcfaWildcardAffDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 9),
    _CcfaWildcardAffDestinationMask_Type()
)
ccfaWildcardAffDestinationMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffDestinationMask.setStatus("current")
_CcfaWildcardAffSvcManagerAddr_Type = IpAddress
_CcfaWildcardAffSvcManagerAddr_Object = MibTableColumn
ccfaWildcardAffSvcManagerAddr = _CcfaWildcardAffSvcManagerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 10),
    _CcfaWildcardAffSvcManagerAddr_Type()
)
ccfaWildcardAffSvcManagerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffSvcManagerAddr.setStatus("current")
_CcfaWildcardAffSvcManagerPort_Type = CiscoPort
_CcfaWildcardAffSvcManagerPort_Object = MibTableColumn
ccfaWildcardAffSvcManagerPort = _CcfaWildcardAffSvcManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 11),
    _CcfaWildcardAffSvcManagerPort_Type()
)
ccfaWildcardAffSvcManagerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffSvcManagerPort.setStatus("current")
_CcfaWildcardAffBytes_Type = Counter32
_CcfaWildcardAffBytes_Object = MibTableColumn
ccfaWildcardAffBytes = _CcfaWildcardAffBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 12),
    _CcfaWildcardAffBytes_Type()
)
ccfaWildcardAffBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffBytes.setUnits("bytes")
_CcfaWildcardAffHCBytes_Type = Counter64
_CcfaWildcardAffHCBytes_Object = MibTableColumn
ccfaWildcardAffHCBytes = _CcfaWildcardAffHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 13),
    _CcfaWildcardAffHCBytes_Type()
)
ccfaWildcardAffHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffHCBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffHCBytes.setUnits("bytes")
_CcfaWildcardAffPackets_Type = Counter32
_CcfaWildcardAffPackets_Object = MibTableColumn
ccfaWildcardAffPackets = _CcfaWildcardAffPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 14),
    _CcfaWildcardAffPackets_Type()
)
ccfaWildcardAffPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffPackets.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffPackets.setUnits("packets")
_CcfaWildcardAffHCPackets_Type = Counter64
_CcfaWildcardAffHCPackets_Object = MibTableColumn
ccfaWildcardAffHCPackets = _CcfaWildcardAffHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 15),
    _CcfaWildcardAffHCPackets_Type()
)
ccfaWildcardAffHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffHCPackets.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffHCPackets.setUnits("packets")
_CcfaWildcardAffFlows_Type = Gauge32
_CcfaWildcardAffFlows_Object = MibTableColumn
ccfaWildcardAffFlows = _CcfaWildcardAffFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 16),
    _CcfaWildcardAffFlows_Type()
)
ccfaWildcardAffFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffFlows.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffFlows.setUnits("affinities")
_CcfaWildcardAffInsertTime_Type = DateAndTime
_CcfaWildcardAffInsertTime_Object = MibTableColumn
ccfaWildcardAffInsertTime = _CcfaWildcardAffInsertTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 17),
    _CcfaWildcardAffInsertTime_Type()
)
ccfaWildcardAffInsertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffInsertTime.setStatus("current")
_CcfaWildcardAffInterestTimeouts_Type = Counter32
_CcfaWildcardAffInterestTimeouts_Object = MibTableColumn
ccfaWildcardAffInterestTimeouts = _CcfaWildcardAffInterestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 18),
    _CcfaWildcardAffInterestTimeouts_Type()
)
ccfaWildcardAffInterestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffInterestTimeouts.setStatus("current")
_CcfaWildcardAffAdvertiseDestAddr_Type = TruthValue
_CcfaWildcardAffAdvertiseDestAddr_Object = MibTableColumn
ccfaWildcardAffAdvertiseDestAddr = _CcfaWildcardAffAdvertiseDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 19),
    _CcfaWildcardAffAdvertiseDestAddr_Type()
)
ccfaWildcardAffAdvertiseDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffAdvertiseDestAddr.setStatus("current")
_CcfaWildcardAffInterestAddr_Type = IpAddress
_CcfaWildcardAffInterestAddr_Object = MibTableColumn
ccfaWildcardAffInterestAddr = _CcfaWildcardAffInterestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 20),
    _CcfaWildcardAffInterestAddr_Type()
)
ccfaWildcardAffInterestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffInterestAddr.setStatus("current")
_CcfaWildcardAffInterestPort_Type = CiscoPort
_CcfaWildcardAffInterestPort_Object = MibTableColumn
ccfaWildcardAffInterestPort = _CcfaWildcardAffInterestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 21),
    _CcfaWildcardAffInterestPort_Type()
)
ccfaWildcardAffInterestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffInterestPort.setStatus("current")
_CcfaWildAffInterestPacketSpec_Type = CasaInterestPacketSpecification
_CcfaWildAffInterestPacketSpec_Object = MibTableColumn
ccfaWildAffInterestPacketSpec = _CcfaWildAffInterestPacketSpec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 22),
    _CcfaWildAffInterestPacketSpec_Type()
)
ccfaWildAffInterestPacketSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildAffInterestPacketSpec.setStatus("current")
_CcfaWildAffInterestTickelSpec_Type = CasaInterestPacketSpecification
_CcfaWildAffInterestTickelSpec_Object = MibTableColumn
ccfaWildAffInterestTickelSpec = _CcfaWildAffInterestTickelSpec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 23),
    _CcfaWildAffInterestTickelSpec_Type()
)
ccfaWildAffInterestTickelSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildAffInterestTickelSpec.setStatus("current")
_CcfaWildcardAffDispatch_Type = TruthValue
_CcfaWildcardAffDispatch_Object = MibTableColumn
ccfaWildcardAffDispatch = _CcfaWildcardAffDispatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 24),
    _CcfaWildcardAffDispatch_Type()
)
ccfaWildcardAffDispatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffDispatch.setStatus("current")
_CcfaWildcardAffDispatchAddr_Type = IpAddress
_CcfaWildcardAffDispatchAddr_Object = MibTableColumn
ccfaWildcardAffDispatchAddr = _CcfaWildcardAffDispatchAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 6, 1, 25),
    _CcfaWildcardAffDispatchAddr_Type()
)
ccfaWildcardAffDispatchAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffDispatchAddr.setStatus("current")
_CcfaWildcardAffHiWtrMark_Type = Unsigned32
_CcfaWildcardAffHiWtrMark_Object = MibScalar
ccfaWildcardAffHiWtrMark = _CcfaWildcardAffHiWtrMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 7),
    _CcfaWildcardAffHiWtrMark_Type()
)
ccfaWildcardAffHiWtrMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccfaWildcardAffHiWtrMark.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffHiWtrMark.setUnits("affinities")
_CcfaWildAffCacheHiWtrMarkReset_Type = TimeStamp
_CcfaWildAffCacheHiWtrMarkReset_Object = MibScalar
ccfaWildAffCacheHiWtrMarkReset = _CcfaWildAffCacheHiWtrMarkReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 8),
    _CcfaWildAffCacheHiWtrMarkReset_Type()
)
ccfaWildAffCacheHiWtrMarkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildAffCacheHiWtrMarkReset.setStatus("current")
_CcfaWildcardAffDenies_Type = Counter32
_CcfaWildcardAffDenies_Object = MibScalar
ccfaWildcardAffDenies = _CcfaWildcardAffDenies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 9),
    _CcfaWildcardAffDenies_Type()
)
ccfaWildcardAffDenies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffDenies.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffDenies.setUnits("affinities")
_CcfaWildcardAffDrops_Type = Counter32
_CcfaWildcardAffDrops_Object = MibScalar
ccfaWildcardAffDrops = _CcfaWildcardAffDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 3, 10),
    _CcfaWildcardAffDrops_Type()
)
ccfaWildcardAffDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaWildcardAffDrops.setStatus("current")
if mibBuilder.loadTexts:
    ccfaWildcardAffDrops.setUnits("affinities")
_CcfaDispatchStats_ObjectIdentity = ObjectIdentity
ccfaDispatchStats = _CcfaDispatchStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4)
)
_CcfaDispatchStatsTable_Object = MibTable
ccfaDispatchStatsTable = _CcfaDispatchStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ccfaDispatchStatsTable.setStatus("current")
_CcfaDispatchStatsEntry_Object = MibTableRow
ccfaDispatchStatsEntry = _CcfaDispatchStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1)
)
ccfaDispatchStatsEntry.setIndexNames(
    (0, "CISCO-CASA-FA-MIB", "ccfaDispatchAddress"),
)
if mibBuilder.loadTexts:
    ccfaDispatchStatsEntry.setStatus("current")
_CcfaDispatchAddress_Type = IpAddress
_CcfaDispatchAddress_Object = MibTableColumn
ccfaDispatchAddress = _CcfaDispatchAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1, 1),
    _CcfaDispatchAddress_Type()
)
ccfaDispatchAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccfaDispatchAddress.setStatus("current")
_CcfaDispatchBytesIn_Type = Counter32
_CcfaDispatchBytesIn_Object = MibTableColumn
ccfaDispatchBytesIn = _CcfaDispatchBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1, 2),
    _CcfaDispatchBytesIn_Type()
)
ccfaDispatchBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaDispatchBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    ccfaDispatchBytesIn.setUnits("bytes")
_CcfaDispatchHCBytesIn_Type = Counter64
_CcfaDispatchHCBytesIn_Object = MibTableColumn
ccfaDispatchHCBytesIn = _CcfaDispatchHCBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1, 3),
    _CcfaDispatchHCBytesIn_Type()
)
ccfaDispatchHCBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaDispatchHCBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    ccfaDispatchHCBytesIn.setUnits("bytes")
_CcfaDispatchBytesOut_Type = Counter32
_CcfaDispatchBytesOut_Object = MibTableColumn
ccfaDispatchBytesOut = _CcfaDispatchBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1, 4),
    _CcfaDispatchBytesOut_Type()
)
ccfaDispatchBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaDispatchBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    ccfaDispatchBytesOut.setUnits("bytes")
_CcfaDispatchHCBytesOut_Type = Counter64
_CcfaDispatchHCBytesOut_Object = MibTableColumn
ccfaDispatchHCBytesOut = _CcfaDispatchHCBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1, 5),
    _CcfaDispatchHCBytesOut_Type()
)
ccfaDispatchHCBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaDispatchHCBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    ccfaDispatchHCBytesOut.setUnits("bytes")
_CcfaDispatchPacketsIn_Type = Counter32
_CcfaDispatchPacketsIn_Object = MibTableColumn
ccfaDispatchPacketsIn = _CcfaDispatchPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1, 6),
    _CcfaDispatchPacketsIn_Type()
)
ccfaDispatchPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaDispatchPacketsIn.setStatus("current")
if mibBuilder.loadTexts:
    ccfaDispatchPacketsIn.setUnits("packets")
_CcfaDispatchHCPacketsIn_Type = Counter64
_CcfaDispatchHCPacketsIn_Object = MibTableColumn
ccfaDispatchHCPacketsIn = _CcfaDispatchHCPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1, 7),
    _CcfaDispatchHCPacketsIn_Type()
)
ccfaDispatchHCPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaDispatchHCPacketsIn.setStatus("current")
if mibBuilder.loadTexts:
    ccfaDispatchHCPacketsIn.setUnits("packets")
_CcfaDispatchPacketsOut_Type = Counter32
_CcfaDispatchPacketsOut_Object = MibTableColumn
ccfaDispatchPacketsOut = _CcfaDispatchPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1, 8),
    _CcfaDispatchPacketsOut_Type()
)
ccfaDispatchPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaDispatchPacketsOut.setStatus("current")
if mibBuilder.loadTexts:
    ccfaDispatchPacketsOut.setUnits("packets")
_CcfaDispatchHCPacketsOut_Type = Counter64
_CcfaDispatchHCPacketsOut_Object = MibTableColumn
ccfaDispatchHCPacketsOut = _CcfaDispatchHCPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1, 9),
    _CcfaDispatchHCPacketsOut_Type()
)
ccfaDispatchHCPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaDispatchHCPacketsOut.setStatus("current")
if mibBuilder.loadTexts:
    ccfaDispatchHCPacketsOut.setUnits("packets")
_CcfaDispatchFlows_Type = Gauge32
_CcfaDispatchFlows_Object = MibTableColumn
ccfaDispatchFlows = _CcfaDispatchFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 1, 1, 10),
    _CcfaDispatchFlows_Type()
)
ccfaDispatchFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaDispatchFlows.setStatus("current")
if mibBuilder.loadTexts:
    ccfaDispatchFlows.setUnits("affinities")
_CcfaAdvertisedDispatchTable_Object = MibTable
ccfaAdvertisedDispatchTable = _CcfaAdvertisedDispatchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ccfaAdvertisedDispatchTable.setStatus("current")
_CcfaAdvertisedDispatchEntry_Object = MibTableRow
ccfaAdvertisedDispatchEntry = _CcfaAdvertisedDispatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 2, 1)
)
ccfaAdvertisedDispatchEntry.setIndexNames(
    (0, "CISCO-CASA-FA-MIB", "ccfaAdvertisedAddress"),
)
if mibBuilder.loadTexts:
    ccfaAdvertisedDispatchEntry.setStatus("current")
_CcfaAdvertisedAddress_Type = IpAddress
_CcfaAdvertisedAddress_Object = MibTableColumn
ccfaAdvertisedAddress = _CcfaAdvertisedAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 2, 1, 1),
    _CcfaAdvertisedAddress_Type()
)
ccfaAdvertisedAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccfaAdvertisedAddress.setStatus("current")
_CcfaAdvertisedDispatchAddress_Type = IpAddress
_CcfaAdvertisedDispatchAddress_Object = MibTableColumn
ccfaAdvertisedDispatchAddress = _CcfaAdvertisedDispatchAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 4, 2, 1, 2),
    _CcfaAdvertisedDispatchAddress_Type()
)
ccfaAdvertisedDispatchAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaAdvertisedDispatchAddress.setStatus("current")
_CiscoCasaFaMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoCasaFaMIBNotificationPrefix = _CiscoCasaFaMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 2)
)
_CiscoCasaFaMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoCasaFaMIBNotifications = _CiscoCasaFaMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 2, 0)
)
_CiscoCasaFaMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCasaFaMIBConformance = _CiscoCasaFaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 3)
)
_CiscoCasaFaMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCasaFaMIBCompliances = _CiscoCasaFaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 3, 1)
)
_CiscoCasaFaMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCasaFaMIBGroups = _CiscoCasaFaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 3, 2)
)

# Managed Objects groups

ciscoCasaFaWildcardAffGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 3, 2, 3)
)
ciscoCasaFaWildcardAffGroup.setObjects(
      *(("CISCO-CASA-FA-MIB", "ccfaWildcardAffTotalBytes"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffHCTotalBytes"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffTotalPackets"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffNumOf"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffNotifEnabled"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffHiWtrMark"),
        ("CISCO-CASA-FA-MIB", "ccfaWildAffCacheHiWtrMarkReset"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDenies"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDrops"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSourceAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDestinationAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSourcePort"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDestinationPort"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffProtocol"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffFragment"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSourceMask"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDestinationMask"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSvcManagerAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSvcManagerPort"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffBytes"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffHCBytes"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffPackets"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffHCPackets"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffFlows"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffInsertTime"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffInterestTimeouts"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffAdvertiseDestAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffInterestAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffInterestPort"),
        ("CISCO-CASA-FA-MIB", "ccfaWildAffInterestPacketSpec"),
        ("CISCO-CASA-FA-MIB", "ccfaWildAffInterestTickelSpec"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDispatch"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDispatchAddr"))
)
if mibBuilder.loadTexts:
    ciscoCasaFaWildcardAffGroup.setStatus("current")

ciscoCasaFaDispatchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 3, 2, 5)
)
ciscoCasaFaDispatchGroup.setObjects(
      *(("CISCO-CASA-FA-MIB", "ccfaDispatchBytesIn"),
        ("CISCO-CASA-FA-MIB", "ccfaDispatchHCBytesIn"),
        ("CISCO-CASA-FA-MIB", "ccfaDispatchBytesOut"),
        ("CISCO-CASA-FA-MIB", "ccfaDispatchHCBytesOut"),
        ("CISCO-CASA-FA-MIB", "ccfaDispatchPacketsIn"),
        ("CISCO-CASA-FA-MIB", "ccfaDispatchHCPacketsIn"),
        ("CISCO-CASA-FA-MIB", "ccfaDispatchPacketsOut"),
        ("CISCO-CASA-FA-MIB", "ccfaDispatchHCPacketsOut"),
        ("CISCO-CASA-FA-MIB", "ccfaDispatchFlows"))
)
if mibBuilder.loadTexts:
    ciscoCasaFaDispatchGroup.setStatus("current")

ciscoCasaFaADGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 3, 2, 6)
)
ciscoCasaFaADGroup.setObjects(
    ("CISCO-CASA-FA-MIB", "ccfaAdvertisedDispatchAddress")
)
if mibBuilder.loadTexts:
    ciscoCasaFaADGroup.setStatus("current")


# Notification objects

ciscoCasaFaWildcardAffCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 2, 1)
)
ciscoCasaFaWildcardAffCreated.setObjects(
      *(("CISCO-CASA-FA-MIB", "ccfaWildcardAffSourceAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDestinationAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSourcePort"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDestinationPort"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffProtocol"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffFragment"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSourceMask"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDestinationMask"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSvcManagerAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSvcManagerPort"))
)
if mibBuilder.loadTexts:
    ciscoCasaFaWildcardAffCreated.setStatus(
        "current"
    )

ciscoCasaFaWildcardAffDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 2, 2)
)
ciscoCasaFaWildcardAffDeleted.setObjects(
      *(("CISCO-CASA-FA-MIB", "ccfaWildcardAffSourceAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDestinationAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSourcePort"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDestinationPort"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffProtocol"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffFragment"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSourceMask"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffDestinationMask"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSvcManagerAddr"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffSvcManagerPort"),
        ("CISCO-CASA-FA-MIB", "ccfaWildcardAffFlows"))
)
if mibBuilder.loadTexts:
    ciscoCasaFaWildcardAffDeleted.setStatus(
        "current"
    )


# Notifications groups

ciscoCasaFaNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 3, 2, 7)
)
ciscoCasaFaNotifGroup.setObjects(
      *(("CISCO-CASA-FA-MIB", "ciscoCasaFaWildcardAffCreated"),
        ("CISCO-CASA-FA-MIB", "ciscoCasaFaWildcardAffDeleted"))
)
if mibBuilder.loadTexts:
    ciscoCasaFaNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCasaFaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCasaFaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CASA-FA-MIB",
    **{"CasaWildcardAffIndex": CasaWildcardAffIndex,
       "CasaInterestPacketSpecification": CasaInterestPacketSpecification,
       "ciscoCasaFaMIB": ciscoCasaFaMIB,
       "ciscoCasaFaMIBObjects": ciscoCasaFaMIBObjects,
       "ccfaGlobal": ccfaGlobal,
       "ccfaStats": ccfaStats,
       "ccfaWildcardAff": ccfaWildcardAff,
       "ccfaWildcardAffTotalBytes": ccfaWildcardAffTotalBytes,
       "ccfaWildcardAffHCTotalBytes": ccfaWildcardAffHCTotalBytes,
       "ccfaWildcardAffTotalPackets": ccfaWildcardAffTotalPackets,
       "ccfaWildcardAffNumOf": ccfaWildcardAffNumOf,
       "ccfaWildcardAffNotifEnabled": ccfaWildcardAffNotifEnabled,
       "ccfaWildcardAffTable": ccfaWildcardAffTable,
       "ccfaWildcardAffEntry": ccfaWildcardAffEntry,
       "ccfaWildcardAffIndex": ccfaWildcardAffIndex,
       "ccfaWildcardAffSourceAddr": ccfaWildcardAffSourceAddr,
       "ccfaWildcardAffDestinationAddr": ccfaWildcardAffDestinationAddr,
       "ccfaWildcardAffSourcePort": ccfaWildcardAffSourcePort,
       "ccfaWildcardAffDestinationPort": ccfaWildcardAffDestinationPort,
       "ccfaWildcardAffProtocol": ccfaWildcardAffProtocol,
       "ccfaWildcardAffFragment": ccfaWildcardAffFragment,
       "ccfaWildcardAffSourceMask": ccfaWildcardAffSourceMask,
       "ccfaWildcardAffDestinationMask": ccfaWildcardAffDestinationMask,
       "ccfaWildcardAffSvcManagerAddr": ccfaWildcardAffSvcManagerAddr,
       "ccfaWildcardAffSvcManagerPort": ccfaWildcardAffSvcManagerPort,
       "ccfaWildcardAffBytes": ccfaWildcardAffBytes,
       "ccfaWildcardAffHCBytes": ccfaWildcardAffHCBytes,
       "ccfaWildcardAffPackets": ccfaWildcardAffPackets,
       "ccfaWildcardAffHCPackets": ccfaWildcardAffHCPackets,
       "ccfaWildcardAffFlows": ccfaWildcardAffFlows,
       "ccfaWildcardAffInsertTime": ccfaWildcardAffInsertTime,
       "ccfaWildcardAffInterestTimeouts": ccfaWildcardAffInterestTimeouts,
       "ccfaWildcardAffAdvertiseDestAddr": ccfaWildcardAffAdvertiseDestAddr,
       "ccfaWildcardAffInterestAddr": ccfaWildcardAffInterestAddr,
       "ccfaWildcardAffInterestPort": ccfaWildcardAffInterestPort,
       "ccfaWildAffInterestPacketSpec": ccfaWildAffInterestPacketSpec,
       "ccfaWildAffInterestTickelSpec": ccfaWildAffInterestTickelSpec,
       "ccfaWildcardAffDispatch": ccfaWildcardAffDispatch,
       "ccfaWildcardAffDispatchAddr": ccfaWildcardAffDispatchAddr,
       "ccfaWildcardAffHiWtrMark": ccfaWildcardAffHiWtrMark,
       "ccfaWildAffCacheHiWtrMarkReset": ccfaWildAffCacheHiWtrMarkReset,
       "ccfaWildcardAffDenies": ccfaWildcardAffDenies,
       "ccfaWildcardAffDrops": ccfaWildcardAffDrops,
       "ccfaDispatchStats": ccfaDispatchStats,
       "ccfaDispatchStatsTable": ccfaDispatchStatsTable,
       "ccfaDispatchStatsEntry": ccfaDispatchStatsEntry,
       "ccfaDispatchAddress": ccfaDispatchAddress,
       "ccfaDispatchBytesIn": ccfaDispatchBytesIn,
       "ccfaDispatchHCBytesIn": ccfaDispatchHCBytesIn,
       "ccfaDispatchBytesOut": ccfaDispatchBytesOut,
       "ccfaDispatchHCBytesOut": ccfaDispatchHCBytesOut,
       "ccfaDispatchPacketsIn": ccfaDispatchPacketsIn,
       "ccfaDispatchHCPacketsIn": ccfaDispatchHCPacketsIn,
       "ccfaDispatchPacketsOut": ccfaDispatchPacketsOut,
       "ccfaDispatchHCPacketsOut": ccfaDispatchHCPacketsOut,
       "ccfaDispatchFlows": ccfaDispatchFlows,
       "ccfaAdvertisedDispatchTable": ccfaAdvertisedDispatchTable,
       "ccfaAdvertisedDispatchEntry": ccfaAdvertisedDispatchEntry,
       "ccfaAdvertisedAddress": ccfaAdvertisedAddress,
       "ccfaAdvertisedDispatchAddress": ccfaAdvertisedDispatchAddress,
       "ciscoCasaFaMIBNotificationPrefix": ciscoCasaFaMIBNotificationPrefix,
       "ciscoCasaFaMIBNotifications": ciscoCasaFaMIBNotifications,
       "ciscoCasaFaWildcardAffCreated": ciscoCasaFaWildcardAffCreated,
       "ciscoCasaFaWildcardAffDeleted": ciscoCasaFaWildcardAffDeleted,
       "ciscoCasaFaMIBConformance": ciscoCasaFaMIBConformance,
       "ciscoCasaFaMIBCompliances": ciscoCasaFaMIBCompliances,
       "ciscoCasaFaMIBCompliance": ciscoCasaFaMIBCompliance,
       "ciscoCasaFaMIBGroups": ciscoCasaFaMIBGroups,
       "ciscoCasaFaWildcardAffGroup": ciscoCasaFaWildcardAffGroup,
       "ciscoCasaFaDispatchGroup": ciscoCasaFaDispatchGroup,
       "ciscoCasaFaADGroup": ciscoCasaFaADGroup,
       "ciscoCasaFaNotifGroup": ciscoCasaFaNotifGroup}
)
