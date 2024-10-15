# SNMP MIB module (CISCO-RADIUS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RADIUS-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:27 2024
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

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

ciscoRadiusExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736)
)
ciscoRadiusExtMIB.setRevisions(
        ("2010-05-25 00:00",
         "2010-05-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RadiusSourceIdentifier(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CRadiusExtMIBObjects_ObjectIdentity = ObjectIdentity
cRadiusExtMIBObjects = _CRadiusExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1)
)
_CreClientGlobal_ObjectIdentity = ObjectIdentity
creClientGlobal = _CreClientGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1)
)
_CreClientTotalMaxInQLength_Type = Gauge32
_CreClientTotalMaxInQLength_Object = MibScalar
creClientTotalMaxInQLength = _CreClientTotalMaxInQLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 1),
    _CreClientTotalMaxInQLength_Type()
)
creClientTotalMaxInQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creClientTotalMaxInQLength.setStatus("current")
if mibBuilder.loadTexts:
    creClientTotalMaxInQLength.setUnits("RADIUS packets")
_CreClientTotalMaxWaitQLength_Type = Gauge32
_CreClientTotalMaxWaitQLength_Object = MibScalar
creClientTotalMaxWaitQLength = _CreClientTotalMaxWaitQLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 2),
    _CreClientTotalMaxWaitQLength_Type()
)
creClientTotalMaxWaitQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creClientTotalMaxWaitQLength.setStatus("current")
if mibBuilder.loadTexts:
    creClientTotalMaxWaitQLength.setUnits("RADIUS packets")
_CreClientTotalMaxDoneQLength_Type = Gauge32
_CreClientTotalMaxDoneQLength_Object = MibScalar
creClientTotalMaxDoneQLength = _CreClientTotalMaxDoneQLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 3),
    _CreClientTotalMaxDoneQLength_Type()
)
creClientTotalMaxDoneQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creClientTotalMaxDoneQLength.setStatus("current")
if mibBuilder.loadTexts:
    creClientTotalMaxDoneQLength.setUnits("RADIUS packets")
_CreClientTotalAccessRejects_Type = Counter32
_CreClientTotalAccessRejects_Object = MibScalar
creClientTotalAccessRejects = _CreClientTotalAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 4),
    _CreClientTotalAccessRejects_Type()
)
creClientTotalAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creClientTotalAccessRejects.setStatus("current")
if mibBuilder.loadTexts:
    creClientTotalAccessRejects.setUnits("RADIUS packets")
_CreClientTotalAverageResponseDelay_Type = TimeInterval
_CreClientTotalAverageResponseDelay_Object = MibScalar
creClientTotalAverageResponseDelay = _CreClientTotalAverageResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 5),
    _CreClientTotalAverageResponseDelay_Type()
)
creClientTotalAverageResponseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creClientTotalAverageResponseDelay.setStatus("current")
_CreClientSourcePortRangeStart_Type = InetPortNumber
_CreClientSourcePortRangeStart_Object = MibScalar
creClientSourcePortRangeStart = _CreClientSourcePortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 6),
    _CreClientSourcePortRangeStart_Type()
)
creClientSourcePortRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creClientSourcePortRangeStart.setStatus("current")
_CreClientSourcePortRangeEnd_Type = InetPortNumber
_CreClientSourcePortRangeEnd_Object = MibScalar
creClientSourcePortRangeEnd = _CreClientSourcePortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 7),
    _CreClientSourcePortRangeEnd_Type()
)
creClientSourcePortRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creClientSourcePortRangeEnd.setStatus("current")
_CreClientLastUsedSourcePort_Type = InetPortNumber
_CreClientLastUsedSourcePort_Object = MibScalar
creClientLastUsedSourcePort = _CreClientLastUsedSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 8),
    _CreClientLastUsedSourcePort_Type()
)
creClientLastUsedSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creClientLastUsedSourcePort.setStatus("current")
_CreClientLastUsedSourceId_Type = RadiusSourceIdentifier
_CreClientLastUsedSourceId_Object = MibScalar
creClientLastUsedSourceId = _CreClientLastUsedSourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 1, 9),
    _CreClientLastUsedSourceId_Type()
)
creClientLastUsedSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creClientLastUsedSourceId.setStatus("current")
_CreClientAuthentication_ObjectIdentity = ObjectIdentity
creClientAuthentication = _CreClientAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2)
)
_CreAuthClientBadAuthenticators_Type = Counter32
_CreAuthClientBadAuthenticators_Object = MibScalar
creAuthClientBadAuthenticators = _CreAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 1),
    _CreAuthClientBadAuthenticators_Type()
)
creAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    creAuthClientBadAuthenticators.setUnits("RADIUS packets")
_CreAuthClientUnknownResponses_Type = Counter32
_CreAuthClientUnknownResponses_Object = MibScalar
creAuthClientUnknownResponses = _CreAuthClientUnknownResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 2),
    _CreAuthClientUnknownResponses_Type()
)
creAuthClientUnknownResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientUnknownResponses.setStatus("current")
if mibBuilder.loadTexts:
    creAuthClientUnknownResponses.setUnits("RADIUS packets")
_CreAuthClientTotalPacketsWithResponses_Type = Counter32
_CreAuthClientTotalPacketsWithResponses_Object = MibScalar
creAuthClientTotalPacketsWithResponses = _CreAuthClientTotalPacketsWithResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 3),
    _CreAuthClientTotalPacketsWithResponses_Type()
)
creAuthClientTotalPacketsWithResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientTotalPacketsWithResponses.setStatus("current")
if mibBuilder.loadTexts:
    creAuthClientTotalPacketsWithResponses.setUnits("RADIUS packets")
_CreAuthClientBufferAllocFailures_Type = Counter32
_CreAuthClientBufferAllocFailures_Object = MibScalar
creAuthClientBufferAllocFailures = _CreAuthClientBufferAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 4),
    _CreAuthClientBufferAllocFailures_Type()
)
creAuthClientBufferAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientBufferAllocFailures.setStatus("current")
if mibBuilder.loadTexts:
    creAuthClientBufferAllocFailures.setUnits("buffer failures")
_CreAuthClientTotalResponses_Type = Counter32
_CreAuthClientTotalResponses_Object = MibScalar
creAuthClientTotalResponses = _CreAuthClientTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 5),
    _CreAuthClientTotalResponses_Type()
)
creAuthClientTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientTotalResponses.setStatus("current")
if mibBuilder.loadTexts:
    creAuthClientTotalResponses.setUnits("RADIUS packets")
_CreAuthClientTotalPacketsWithoutResponses_Type = Counter32
_CreAuthClientTotalPacketsWithoutResponses_Object = MibScalar
creAuthClientTotalPacketsWithoutResponses = _CreAuthClientTotalPacketsWithoutResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 6),
    _CreAuthClientTotalPacketsWithoutResponses_Type()
)
creAuthClientTotalPacketsWithoutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientTotalPacketsWithoutResponses.setStatus("current")
if mibBuilder.loadTexts:
    creAuthClientTotalPacketsWithoutResponses.setUnits("RADIUS packets")
_CreAuthClientAverageResponseDelay_Type = TimeInterval
_CreAuthClientAverageResponseDelay_Object = MibScalar
creAuthClientAverageResponseDelay = _CreAuthClientAverageResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 7),
    _CreAuthClientAverageResponseDelay_Type()
)
creAuthClientAverageResponseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientAverageResponseDelay.setStatus("current")
_CreAuthClientMaxResponseDelay_Type = TimeInterval
_CreAuthClientMaxResponseDelay_Object = MibScalar
creAuthClientMaxResponseDelay = _CreAuthClientMaxResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 8),
    _CreAuthClientMaxResponseDelay_Type()
)
creAuthClientMaxResponseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientMaxResponseDelay.setStatus("current")


class _CreAuthClientMaxBufferSize_Type(Unsigned32):
    """Custom type creAuthClientMaxBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CreAuthClientMaxBufferSize_Type.__name__ = "Unsigned32"
_CreAuthClientMaxBufferSize_Object = MibScalar
creAuthClientMaxBufferSize = _CreAuthClientMaxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 9),
    _CreAuthClientMaxBufferSize_Type()
)
creAuthClientMaxBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientMaxBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    creAuthClientMaxBufferSize.setUnits("bytes")
_CreAuthClientTimeouts_Type = Counter32
_CreAuthClientTimeouts_Object = MibScalar
creAuthClientTimeouts = _CreAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 10),
    _CreAuthClientTimeouts_Type()
)
creAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    creAuthClientTimeouts.setUnits("timeouts")
_CreAuthClientDupIDs_Type = Counter32
_CreAuthClientDupIDs_Object = MibScalar
creAuthClientDupIDs = _CreAuthClientDupIDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 11),
    _CreAuthClientDupIDs_Type()
)
creAuthClientDupIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientDupIDs.setStatus("current")
if mibBuilder.loadTexts:
    creAuthClientDupIDs.setUnits("RADIUS packets")
_CreAuthClientMalformedResponses_Type = Counter32
_CreAuthClientMalformedResponses_Object = MibScalar
creAuthClientMalformedResponses = _CreAuthClientMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 12),
    _CreAuthClientMalformedResponses_Type()
)
creAuthClientMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientMalformedResponses.setStatus("current")
if mibBuilder.loadTexts:
    creAuthClientMalformedResponses.setUnits("RADIUS packets")
_CreAuthClientLastUsedSourceId_Type = RadiusSourceIdentifier
_CreAuthClientLastUsedSourceId_Object = MibScalar
creAuthClientLastUsedSourceId = _CreAuthClientLastUsedSourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 2, 13),
    _CreAuthClientLastUsedSourceId_Type()
)
creAuthClientLastUsedSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAuthClientLastUsedSourceId.setStatus("current")
_CreClientAccounting_ObjectIdentity = ObjectIdentity
creClientAccounting = _CreClientAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3)
)
_CreAcctClientBadAuthenticators_Type = Counter32
_CreAcctClientBadAuthenticators_Object = MibScalar
creAcctClientBadAuthenticators = _CreAcctClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 1),
    _CreAcctClientBadAuthenticators_Type()
)
creAcctClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    creAcctClientBadAuthenticators.setUnits("RADIUS packets")
_CreAcctClientUnknownResponses_Type = Counter32
_CreAcctClientUnknownResponses_Object = MibScalar
creAcctClientUnknownResponses = _CreAcctClientUnknownResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 2),
    _CreAcctClientUnknownResponses_Type()
)
creAcctClientUnknownResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientUnknownResponses.setStatus("current")
if mibBuilder.loadTexts:
    creAcctClientUnknownResponses.setUnits("RADIUS packets")
_CreAcctClientTotalPacketsWithResponses_Type = Counter32
_CreAcctClientTotalPacketsWithResponses_Object = MibScalar
creAcctClientTotalPacketsWithResponses = _CreAcctClientTotalPacketsWithResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 3),
    _CreAcctClientTotalPacketsWithResponses_Type()
)
creAcctClientTotalPacketsWithResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientTotalPacketsWithResponses.setStatus("current")
if mibBuilder.loadTexts:
    creAcctClientTotalPacketsWithResponses.setUnits("RADIUS packets")
_CreAcctClientBufferAllocFailures_Type = Counter32
_CreAcctClientBufferAllocFailures_Object = MibScalar
creAcctClientBufferAllocFailures = _CreAcctClientBufferAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 4),
    _CreAcctClientBufferAllocFailures_Type()
)
creAcctClientBufferAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientBufferAllocFailures.setStatus("current")
if mibBuilder.loadTexts:
    creAcctClientBufferAllocFailures.setUnits("buffer failures")
_CreAcctClientTotalResponses_Type = Counter32
_CreAcctClientTotalResponses_Object = MibScalar
creAcctClientTotalResponses = _CreAcctClientTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 5),
    _CreAcctClientTotalResponses_Type()
)
creAcctClientTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientTotalResponses.setStatus("current")
if mibBuilder.loadTexts:
    creAcctClientTotalResponses.setUnits("RADIUS packets")
_CreAcctClientTotalPacketsWithoutResponses_Type = Counter32
_CreAcctClientTotalPacketsWithoutResponses_Object = MibScalar
creAcctClientTotalPacketsWithoutResponses = _CreAcctClientTotalPacketsWithoutResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 6),
    _CreAcctClientTotalPacketsWithoutResponses_Type()
)
creAcctClientTotalPacketsWithoutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientTotalPacketsWithoutResponses.setStatus("current")
if mibBuilder.loadTexts:
    creAcctClientTotalPacketsWithoutResponses.setUnits("RADIUS packets")
_CreAcctClientAverageResponseDelay_Type = TimeInterval
_CreAcctClientAverageResponseDelay_Object = MibScalar
creAcctClientAverageResponseDelay = _CreAcctClientAverageResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 7),
    _CreAcctClientAverageResponseDelay_Type()
)
creAcctClientAverageResponseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientAverageResponseDelay.setStatus("current")
_CreAcctClientMaxResponseDelay_Type = TimeInterval
_CreAcctClientMaxResponseDelay_Object = MibScalar
creAcctClientMaxResponseDelay = _CreAcctClientMaxResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 8),
    _CreAcctClientMaxResponseDelay_Type()
)
creAcctClientMaxResponseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientMaxResponseDelay.setStatus("current")


class _CreAcctClientMaxBufferSize_Type(Unsigned32):
    """Custom type creAcctClientMaxBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CreAcctClientMaxBufferSize_Type.__name__ = "Unsigned32"
_CreAcctClientMaxBufferSize_Object = MibScalar
creAcctClientMaxBufferSize = _CreAcctClientMaxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 9),
    _CreAcctClientMaxBufferSize_Type()
)
creAcctClientMaxBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientMaxBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    creAcctClientMaxBufferSize.setUnits("bytes")
_CreAcctClientTimeouts_Type = Counter32
_CreAcctClientTimeouts_Object = MibScalar
creAcctClientTimeouts = _CreAcctClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 10),
    _CreAcctClientTimeouts_Type()
)
creAcctClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    creAcctClientTimeouts.setUnits("timeouts")
_CreAcctClientDupIDs_Type = Counter32
_CreAcctClientDupIDs_Object = MibScalar
creAcctClientDupIDs = _CreAcctClientDupIDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 11),
    _CreAcctClientDupIDs_Type()
)
creAcctClientDupIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientDupIDs.setStatus("current")
if mibBuilder.loadTexts:
    creAcctClientDupIDs.setUnits("RADIUS packets")
_CreAcctClientMalformedResponses_Type = Counter32
_CreAcctClientMalformedResponses_Object = MibScalar
creAcctClientMalformedResponses = _CreAcctClientMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 12),
    _CreAcctClientMalformedResponses_Type()
)
creAcctClientMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientMalformedResponses.setStatus("current")
if mibBuilder.loadTexts:
    creAcctClientMalformedResponses.setUnits("RADIUS packets")
_CreAcctClientLastUsedSourceId_Type = RadiusSourceIdentifier
_CreAcctClientLastUsedSourceId_Object = MibScalar
creAcctClientLastUsedSourceId = _CreAcctClientLastUsedSourceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 3, 13),
    _CreAcctClientLastUsedSourceId_Type()
)
creAcctClientLastUsedSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    creAcctClientLastUsedSourceId.setStatus("current")
_CreClientDynAuth_ObjectIdentity = ObjectIdentity
creClientDynAuth = _CreClientDynAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 4)
)
_CreServerGlobal_ObjectIdentity = ObjectIdentity
creServerGlobal = _CreServerGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 5)
)
_CreServerAuthentication_ObjectIdentity = ObjectIdentity
creServerAuthentication = _CreServerAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 6)
)
_CreServerAccounting_ObjectIdentity = ObjectIdentity
creServerAccounting = _CreServerAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 7)
)
_CreServerDynAuth_ObjectIdentity = ObjectIdentity
creServerDynAuth = _CreServerDynAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 1, 8)
)
_CRadiusExtMIBConformance_ObjectIdentity = ObjectIdentity
cRadiusExtMIBConformance = _CRadiusExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 2)
)
_CreMIBCompliances_ObjectIdentity = ObjectIdentity
creMIBCompliances = _CreMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 1)
)
_CreMIBGroups_ObjectIdentity = ObjectIdentity
creMIBGroups = _CreMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 2)
)

# Managed Objects groups

creClientGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 2, 1)
)
creClientGlobalGroup.setObjects(
      *(("CISCO-RADIUS-EXT-MIB", "creClientTotalMaxInQLength"),
        ("CISCO-RADIUS-EXT-MIB", "creClientTotalMaxWaitQLength"),
        ("CISCO-RADIUS-EXT-MIB", "creClientTotalMaxDoneQLength"),
        ("CISCO-RADIUS-EXT-MIB", "creClientTotalAccessRejects"),
        ("CISCO-RADIUS-EXT-MIB", "creClientSourcePortRangeStart"),
        ("CISCO-RADIUS-EXT-MIB", "creClientSourcePortRangeEnd"),
        ("CISCO-RADIUS-EXT-MIB", "creClientLastUsedSourcePort"),
        ("CISCO-RADIUS-EXT-MIB", "creClientLastUsedSourceId"),
        ("CISCO-RADIUS-EXT-MIB", "creClientTotalAverageResponseDelay"))
)
if mibBuilder.loadTexts:
    creClientGlobalGroup.setStatus("current")

creClientAuthenenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 2, 2)
)
creClientAuthenenticationGroup.setObjects(
      *(("CISCO-RADIUS-EXT-MIB", "creAuthClientTotalResponses"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientTotalPacketsWithResponses"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientTotalPacketsWithoutResponses"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientAverageResponseDelay"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientMaxResponseDelay"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientTimeouts"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientDupIDs"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientBufferAllocFailures"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientMaxBufferSize"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientMalformedResponses"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientBadAuthenticators"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientUnknownResponses"),
        ("CISCO-RADIUS-EXT-MIB", "creAuthClientLastUsedSourceId"))
)
if mibBuilder.loadTexts:
    creClientAuthenenticationGroup.setStatus("current")

creClientAccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 2, 3)
)
creClientAccountingGroup.setObjects(
      *(("CISCO-RADIUS-EXT-MIB", "creAcctClientTotalResponses"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientTotalPacketsWithResponses"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientTotalPacketsWithoutResponses"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientAverageResponseDelay"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientMaxResponseDelay"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientTimeouts"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientBadAuthenticators"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientUnknownResponses"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientLastUsedSourceId"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientDupIDs"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientBufferAllocFailures"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientMaxBufferSize"),
        ("CISCO-RADIUS-EXT-MIB", "creAcctClientMalformedResponses"))
)
if mibBuilder.loadTexts:
    creClientAccountingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

creMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 736, 2, 1, 1)
)
if mibBuilder.loadTexts:
    creMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RADIUS-EXT-MIB",
    **{"RadiusSourceIdentifier": RadiusSourceIdentifier,
       "ciscoRadiusExtMIB": ciscoRadiusExtMIB,
       "cRadiusExtMIBObjects": cRadiusExtMIBObjects,
       "creClientGlobal": creClientGlobal,
       "creClientTotalMaxInQLength": creClientTotalMaxInQLength,
       "creClientTotalMaxWaitQLength": creClientTotalMaxWaitQLength,
       "creClientTotalMaxDoneQLength": creClientTotalMaxDoneQLength,
       "creClientTotalAccessRejects": creClientTotalAccessRejects,
       "creClientTotalAverageResponseDelay": creClientTotalAverageResponseDelay,
       "creClientSourcePortRangeStart": creClientSourcePortRangeStart,
       "creClientSourcePortRangeEnd": creClientSourcePortRangeEnd,
       "creClientLastUsedSourcePort": creClientLastUsedSourcePort,
       "creClientLastUsedSourceId": creClientLastUsedSourceId,
       "creClientAuthentication": creClientAuthentication,
       "creAuthClientBadAuthenticators": creAuthClientBadAuthenticators,
       "creAuthClientUnknownResponses": creAuthClientUnknownResponses,
       "creAuthClientTotalPacketsWithResponses": creAuthClientTotalPacketsWithResponses,
       "creAuthClientBufferAllocFailures": creAuthClientBufferAllocFailures,
       "creAuthClientTotalResponses": creAuthClientTotalResponses,
       "creAuthClientTotalPacketsWithoutResponses": creAuthClientTotalPacketsWithoutResponses,
       "creAuthClientAverageResponseDelay": creAuthClientAverageResponseDelay,
       "creAuthClientMaxResponseDelay": creAuthClientMaxResponseDelay,
       "creAuthClientMaxBufferSize": creAuthClientMaxBufferSize,
       "creAuthClientTimeouts": creAuthClientTimeouts,
       "creAuthClientDupIDs": creAuthClientDupIDs,
       "creAuthClientMalformedResponses": creAuthClientMalformedResponses,
       "creAuthClientLastUsedSourceId": creAuthClientLastUsedSourceId,
       "creClientAccounting": creClientAccounting,
       "creAcctClientBadAuthenticators": creAcctClientBadAuthenticators,
       "creAcctClientUnknownResponses": creAcctClientUnknownResponses,
       "creAcctClientTotalPacketsWithResponses": creAcctClientTotalPacketsWithResponses,
       "creAcctClientBufferAllocFailures": creAcctClientBufferAllocFailures,
       "creAcctClientTotalResponses": creAcctClientTotalResponses,
       "creAcctClientTotalPacketsWithoutResponses": creAcctClientTotalPacketsWithoutResponses,
       "creAcctClientAverageResponseDelay": creAcctClientAverageResponseDelay,
       "creAcctClientMaxResponseDelay": creAcctClientMaxResponseDelay,
       "creAcctClientMaxBufferSize": creAcctClientMaxBufferSize,
       "creAcctClientTimeouts": creAcctClientTimeouts,
       "creAcctClientDupIDs": creAcctClientDupIDs,
       "creAcctClientMalformedResponses": creAcctClientMalformedResponses,
       "creAcctClientLastUsedSourceId": creAcctClientLastUsedSourceId,
       "creClientDynAuth": creClientDynAuth,
       "creServerGlobal": creServerGlobal,
       "creServerAuthentication": creServerAuthentication,
       "creServerAccounting": creServerAccounting,
       "creServerDynAuth": creServerDynAuth,
       "cRadiusExtMIBConformance": cRadiusExtMIBConformance,
       "creMIBCompliances": creMIBCompliances,
       "creMIBCompliance": creMIBCompliance,
       "creMIBGroups": creMIBGroups,
       "creClientGlobalGroup": creClientGlobalGroup,
       "creClientAuthenenticationGroup": creClientAuthenenticationGroup,
       "creClientAccountingGroup": creClientAccountingGroup}
)
