# SNMP MIB module (ELTEX-MES-AAA-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-AAA-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:21 2024
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

(eltMesAAAStatMIB,) = mibBuilder.importSymbols(
    "ELTEX-MES-MNG-MIB",
    "eltMesAAAStatMIB")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltRadiusAuthServTotalAccessRequests_Type = Counter32
_EltRadiusAuthServTotalAccessRequests_Object = MibScalar
eltRadiusAuthServTotalAccessRequests = _EltRadiusAuthServTotalAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 1),
    _EltRadiusAuthServTotalAccessRequests_Type()
)
eltRadiusAuthServTotalAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAuthServTotalAccessRequests.setStatus("current")
_EltRadiusAuthServTotalAccessAccepts_Type = Counter32
_EltRadiusAuthServTotalAccessAccepts_Object = MibScalar
eltRadiusAuthServTotalAccessAccepts = _EltRadiusAuthServTotalAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 2),
    _EltRadiusAuthServTotalAccessAccepts_Type()
)
eltRadiusAuthServTotalAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAuthServTotalAccessAccepts.setStatus("current")
_EltRadiusAuthServAccessRejects_Type = Counter32
_EltRadiusAuthServAccessRejects_Object = MibScalar
eltRadiusAuthServAccessRejects = _EltRadiusAuthServAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 3),
    _EltRadiusAuthServAccessRejects_Type()
)
eltRadiusAuthServAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAuthServAccessRejects.setStatus("current")
_EltRadiusAuthServAccessChallenges_Type = Counter32
_EltRadiusAuthServAccessChallenges_Object = MibScalar
eltRadiusAuthServAccessChallenges = _EltRadiusAuthServAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 4),
    _EltRadiusAuthServAccessChallenges_Type()
)
eltRadiusAuthServAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAuthServAccessChallenges.setStatus("current")
_EltRadiusAuthServAverageResponseDelay_Type = Counter32
_EltRadiusAuthServAverageResponseDelay_Object = MibScalar
eltRadiusAuthServAverageResponseDelay = _EltRadiusAuthServAverageResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 5),
    _EltRadiusAuthServAverageResponseDelay_Type()
)
eltRadiusAuthServAverageResponseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAuthServAverageResponseDelay.setStatus("current")
_EltRadiusAuthServMaximumResponseDelay_Type = Counter32
_EltRadiusAuthServMaximumResponseDelay_Object = MibScalar
eltRadiusAuthServMaximumResponseDelay = _EltRadiusAuthServMaximumResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 6),
    _EltRadiusAuthServMaximumResponseDelay_Type()
)
eltRadiusAuthServMaximumResponseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAuthServMaximumResponseDelay.setStatus("current")
_EltRadiusAuthServTotalTimeouts_Type = Unsigned32
_EltRadiusAuthServTotalTimeouts_Object = MibScalar
eltRadiusAuthServTotalTimeouts = _EltRadiusAuthServTotalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 7),
    _EltRadiusAuthServTotalTimeouts_Type()
)
eltRadiusAuthServTotalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAuthServTotalTimeouts.setStatus("current")
_EltRadiusAuthServTotalMalformedAccessRequests_Type = Counter32
_EltRadiusAuthServTotalMalformedAccessRequests_Object = MibScalar
eltRadiusAuthServTotalMalformedAccessRequests = _EltRadiusAuthServTotalMalformedAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 8),
    _EltRadiusAuthServTotalMalformedAccessRequests_Type()
)
eltRadiusAuthServTotalMalformedAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAuthServTotalMalformedAccessRequests.setStatus("current")
_EltRadiusAuthServMaximumBufferSize_Type = Counter32
_EltRadiusAuthServMaximumBufferSize_Object = MibScalar
eltRadiusAuthServMaximumBufferSize = _EltRadiusAuthServMaximumBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 9),
    _EltRadiusAuthServMaximumBufferSize_Type()
)
eltRadiusAuthServMaximumBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAuthServMaximumBufferSize.setStatus("current")
_EltRadiusAuthServTotalPacketsDropped_Type = Counter32
_EltRadiusAuthServTotalPacketsDropped_Object = MibScalar
eltRadiusAuthServTotalPacketsDropped = _EltRadiusAuthServTotalPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 10),
    _EltRadiusAuthServTotalPacketsDropped_Type()
)
eltRadiusAuthServTotalPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAuthServTotalPacketsDropped.setStatus("current")
_EltRadiusAccServTotalRequests_Type = Counter32
_EltRadiusAccServTotalRequests_Object = MibScalar
eltRadiusAccServTotalRequests = _EltRadiusAccServTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 11),
    _EltRadiusAccServTotalRequests_Type()
)
eltRadiusAccServTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAccServTotalRequests.setStatus("current")
_EltRadiusAccServTotalDupRequests_Type = Counter32
_EltRadiusAccServTotalDupRequests_Object = MibScalar
eltRadiusAccServTotalDupRequests = _EltRadiusAccServTotalDupRequests_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 12),
    _EltRadiusAccServTotalDupRequests_Type()
)
eltRadiusAccServTotalDupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAccServTotalDupRequests.setStatus("current")
_EltRadiusAccServTotalResponses_Type = Counter32
_EltRadiusAccServTotalResponses_Object = MibScalar
eltRadiusAccServTotalResponses = _EltRadiusAccServTotalResponses_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 13),
    _EltRadiusAccServTotalResponses_Type()
)
eltRadiusAccServTotalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAccServTotalResponses.setStatus("current")
_EltRadiusAccServAverageResponseDelay_Type = Counter32
_EltRadiusAccServAverageResponseDelay_Object = MibScalar
eltRadiusAccServAverageResponseDelay = _EltRadiusAccServAverageResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 14),
    _EltRadiusAccServAverageResponseDelay_Type()
)
eltRadiusAccServAverageResponseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAccServAverageResponseDelay.setStatus("current")
_EltRadiusAccServMaximumResponseDelay_Type = Counter32
_EltRadiusAccServMaximumResponseDelay_Object = MibScalar
eltRadiusAccServMaximumResponseDelay = _EltRadiusAccServMaximumResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 15),
    _EltRadiusAccServMaximumResponseDelay_Type()
)
eltRadiusAccServMaximumResponseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAccServMaximumResponseDelay.setStatus("current")
_EltRadiusAccServTotalTimeouts_Type = Unsigned32
_EltRadiusAccServTotalTimeouts_Object = MibScalar
eltRadiusAccServTotalTimeouts = _EltRadiusAccServTotalTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 16),
    _EltRadiusAccServTotalTimeouts_Type()
)
eltRadiusAccServTotalTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAccServTotalTimeouts.setStatus("current")
_EltRadiusAccServTotalMalformedAccessRequests_Type = Counter32
_EltRadiusAccServTotalMalformedAccessRequests_Object = MibScalar
eltRadiusAccServTotalMalformedAccessRequests = _EltRadiusAccServTotalMalformedAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 17),
    _EltRadiusAccServTotalMalformedAccessRequests_Type()
)
eltRadiusAccServTotalMalformedAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAccServTotalMalformedAccessRequests.setStatus("current")
_EltRadiusAccServMaximumBufferSize_Type = Counter32
_EltRadiusAccServMaximumBufferSize_Object = MibScalar
eltRadiusAccServMaximumBufferSize = _EltRadiusAccServMaximumBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 18),
    _EltRadiusAccServMaximumBufferSize_Type()
)
eltRadiusAccServMaximumBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAccServMaximumBufferSize.setStatus("current")
_EltRadiusAccServTotalPacketsDropped_Type = Counter32
_EltRadiusAccServTotalPacketsDropped_Object = MibScalar
eltRadiusAccServTotalPacketsDropped = _EltRadiusAccServTotalPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 19),
    _EltRadiusAccServTotalPacketsDropped_Type()
)
eltRadiusAccServTotalPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusAccServTotalPacketsDropped.setStatus("current")
_EltTacacsStatsTable_Object = MibTable
eltTacacsStatsTable = _EltTacacsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20)
)
if mibBuilder.loadTexts:
    eltTacacsStatsTable.setStatus("current")
_EltTacacsStatsEntry_Object = MibTableRow
eltTacacsStatsEntry = _EltTacacsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20, 1)
)
eltTacacsStatsEntry.setIndexNames(
    (0, "ELTEX-MES-AAA-STATISTICS-MIB", "eltTacacsServerAddress"),
)
if mibBuilder.loadTexts:
    eltTacacsStatsEntry.setStatus("current")
_EltTacacsServerAddress_Type = IpAddress
_EltTacacsServerAddress_Object = MibTableColumn
eltTacacsServerAddress = _EltTacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20, 1, 1),
    _EltTacacsServerAddress_Type()
)
eltTacacsServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltTacacsServerAddress.setStatus("current")
_EltTacacsSocketOpens_Type = Unsigned32
_EltTacacsSocketOpens_Object = MibTableColumn
eltTacacsSocketOpens = _EltTacacsSocketOpens_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20, 1, 2),
    _EltTacacsSocketOpens_Type()
)
eltTacacsSocketOpens.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltTacacsSocketOpens.setStatus("current")
_EltTacacsSocketCloses_Type = Unsigned32
_EltTacacsSocketCloses_Object = MibTableColumn
eltTacacsSocketCloses = _EltTacacsSocketCloses_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20, 1, 3),
    _EltTacacsSocketCloses_Type()
)
eltTacacsSocketCloses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltTacacsSocketCloses.setStatus("current")
_EltTacacsSocketAborts_Type = Unsigned32
_EltTacacsSocketAborts_Object = MibTableColumn
eltTacacsSocketAborts = _EltTacacsSocketAborts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20, 1, 4),
    _EltTacacsSocketAborts_Type()
)
eltTacacsSocketAborts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltTacacsSocketAborts.setStatus("current")
_EltTacacsSocketErrors_Type = Unsigned32
_EltTacacsSocketErrors_Object = MibTableColumn
eltTacacsSocketErrors = _EltTacacsSocketErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20, 1, 5),
    _EltTacacsSocketErrors_Type()
)
eltTacacsSocketErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltTacacsSocketErrors.setStatus("current")
_EltTacacsSocketTimeouts_Type = Unsigned32
_EltTacacsSocketTimeouts_Object = MibTableColumn
eltTacacsSocketTimeouts = _EltTacacsSocketTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20, 1, 6),
    _EltTacacsSocketTimeouts_Type()
)
eltTacacsSocketTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltTacacsSocketTimeouts.setStatus("current")
_EltTacacsFailesConnAttemps_Type = Unsigned32
_EltTacacsFailesConnAttemps_Object = MibTableColumn
eltTacacsFailesConnAttemps = _EltTacacsFailesConnAttemps_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20, 1, 7),
    _EltTacacsFailesConnAttemps_Type()
)
eltTacacsFailesConnAttemps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltTacacsFailesConnAttemps.setStatus("current")
_EltTacacsTotalPackageSent_Type = Unsigned32
_EltTacacsTotalPackageSent_Object = MibTableColumn
eltTacacsTotalPackageSent = _EltTacacsTotalPackageSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20, 1, 8),
    _EltTacacsTotalPackageSent_Type()
)
eltTacacsTotalPackageSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltTacacsTotalPackageSent.setStatus("current")
_EltTacacsTotalPackageRecv_Type = Unsigned32
_EltTacacsTotalPackageRecv_Object = MibTableColumn
eltTacacsTotalPackageRecv = _EltTacacsTotalPackageRecv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 20, 1, 9),
    _EltTacacsTotalPackageRecv_Type()
)
eltTacacsTotalPackageRecv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltTacacsTotalPackageRecv.setStatus("current")
_EltRadiusServerStatusTable_Object = MibTable
eltRadiusServerStatusTable = _EltRadiusServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21)
)
if mibBuilder.loadTexts:
    eltRadiusServerStatusTable.setStatus("current")
_EltRadiusServerStatusEntry_Object = MibTableRow
eltRadiusServerStatusEntry = _EltRadiusServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1)
)
eltRadiusServerStatusEntry.setIndexNames(
    (0, "ELTEX-MES-AAA-STATISTICS-MIB", "eltRadiusServerAddressType"),
    (0, "ELTEX-MES-AAA-STATISTICS-MIB", "eltRadiusServerAddress"),
    (0, "ELTEX-MES-AAA-STATISTICS-MIB", "eltRadiusServerAuthPortNumber"),
    (0, "ELTEX-MES-AAA-STATISTICS-MIB", "eltRadiusServerAcctPortNumber"),
)
if mibBuilder.loadTexts:
    eltRadiusServerStatusEntry.setStatus("current")
_EltRadiusServerAddressType_Type = InetAddressType
_EltRadiusServerAddressType_Object = MibTableColumn
eltRadiusServerAddressType = _EltRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 1),
    _EltRadiusServerAddressType_Type()
)
eltRadiusServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltRadiusServerAddressType.setStatus("current")
_EltRadiusServerAddress_Type = InetAddress
_EltRadiusServerAddress_Object = MibTableColumn
eltRadiusServerAddress = _EltRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 2),
    _EltRadiusServerAddress_Type()
)
eltRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltRadiusServerAddress.setStatus("current")


class _EltRadiusServerAuthPortNumber_Type(Integer32):
    """Custom type eltRadiusServerAuthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltRadiusServerAuthPortNumber_Type.__name__ = "Integer32"
_EltRadiusServerAuthPortNumber_Object = MibTableColumn
eltRadiusServerAuthPortNumber = _EltRadiusServerAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 3),
    _EltRadiusServerAuthPortNumber_Type()
)
eltRadiusServerAuthPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltRadiusServerAuthPortNumber.setStatus("current")


class _EltRadiusServerAcctPortNumber_Type(Integer32):
    """Custom type eltRadiusServerAcctPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltRadiusServerAcctPortNumber_Type.__name__ = "Integer32"
_EltRadiusServerAcctPortNumber_Object = MibTableColumn
eltRadiusServerAcctPortNumber = _EltRadiusServerAcctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 4),
    _EltRadiusServerAcctPortNumber_Type()
)
eltRadiusServerAcctPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltRadiusServerAcctPortNumber.setStatus("current")
_EltRadiusServerAuthClientTimeouts_Type = Unsigned32
_EltRadiusServerAuthClientTimeouts_Object = MibTableColumn
eltRadiusServerAuthClientTimeouts = _EltRadiusServerAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 5),
    _EltRadiusServerAuthClientTimeouts_Type()
)
eltRadiusServerAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusServerAuthClientTimeouts.setStatus("current")
_EltRadiusServerDeadStatus_Type = TruthValue
_EltRadiusServerDeadStatus_Object = MibTableColumn
eltRadiusServerDeadStatus = _EltRadiusServerDeadStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 6),
    _EltRadiusServerDeadStatus_Type()
)
eltRadiusServerDeadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusServerDeadStatus.setStatus("current")
_EltRadiusServerRemainDeadTime_Type = Unsigned32
_EltRadiusServerRemainDeadTime_Object = MibTableColumn
eltRadiusServerRemainDeadTime = _EltRadiusServerRemainDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 21, 1, 7),
    _EltRadiusServerRemainDeadTime_Type()
)
eltRadiusServerRemainDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltRadiusServerRemainDeadTime.setStatus("current")


class _EltRadiusServerStatusReset_Type(Integer32):
    """Custom type eltRadiusServerStatusReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EltRadiusServerStatusReset_Type.__name__ = "Integer32"
_EltRadiusServerStatusReset_Object = MibScalar
eltRadiusServerStatusReset = _EltRadiusServerStatusReset_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3, 22),
    _EltRadiusServerStatusReset_Type()
)
eltRadiusServerStatusReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltRadiusServerStatusReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-AAA-STATISTICS-MIB",
    **{"eltRadiusAuthServTotalAccessRequests": eltRadiusAuthServTotalAccessRequests,
       "eltRadiusAuthServTotalAccessAccepts": eltRadiusAuthServTotalAccessAccepts,
       "eltRadiusAuthServAccessRejects": eltRadiusAuthServAccessRejects,
       "eltRadiusAuthServAccessChallenges": eltRadiusAuthServAccessChallenges,
       "eltRadiusAuthServAverageResponseDelay": eltRadiusAuthServAverageResponseDelay,
       "eltRadiusAuthServMaximumResponseDelay": eltRadiusAuthServMaximumResponseDelay,
       "eltRadiusAuthServTotalTimeouts": eltRadiusAuthServTotalTimeouts,
       "eltRadiusAuthServTotalMalformedAccessRequests": eltRadiusAuthServTotalMalformedAccessRequests,
       "eltRadiusAuthServMaximumBufferSize": eltRadiusAuthServMaximumBufferSize,
       "eltRadiusAuthServTotalPacketsDropped": eltRadiusAuthServTotalPacketsDropped,
       "eltRadiusAccServTotalRequests": eltRadiusAccServTotalRequests,
       "eltRadiusAccServTotalDupRequests": eltRadiusAccServTotalDupRequests,
       "eltRadiusAccServTotalResponses": eltRadiusAccServTotalResponses,
       "eltRadiusAccServAverageResponseDelay": eltRadiusAccServAverageResponseDelay,
       "eltRadiusAccServMaximumResponseDelay": eltRadiusAccServMaximumResponseDelay,
       "eltRadiusAccServTotalTimeouts": eltRadiusAccServTotalTimeouts,
       "eltRadiusAccServTotalMalformedAccessRequests": eltRadiusAccServTotalMalformedAccessRequests,
       "eltRadiusAccServMaximumBufferSize": eltRadiusAccServMaximumBufferSize,
       "eltRadiusAccServTotalPacketsDropped": eltRadiusAccServTotalPacketsDropped,
       "eltTacacsStatsTable": eltTacacsStatsTable,
       "eltTacacsStatsEntry": eltTacacsStatsEntry,
       "eltTacacsServerAddress": eltTacacsServerAddress,
       "eltTacacsSocketOpens": eltTacacsSocketOpens,
       "eltTacacsSocketCloses": eltTacacsSocketCloses,
       "eltTacacsSocketAborts": eltTacacsSocketAborts,
       "eltTacacsSocketErrors": eltTacacsSocketErrors,
       "eltTacacsSocketTimeouts": eltTacacsSocketTimeouts,
       "eltTacacsFailesConnAttemps": eltTacacsFailesConnAttemps,
       "eltTacacsTotalPackageSent": eltTacacsTotalPackageSent,
       "eltTacacsTotalPackageRecv": eltTacacsTotalPackageRecv,
       "eltRadiusServerStatusTable": eltRadiusServerStatusTable,
       "eltRadiusServerStatusEntry": eltRadiusServerStatusEntry,
       "eltRadiusServerAddressType": eltRadiusServerAddressType,
       "eltRadiusServerAddress": eltRadiusServerAddress,
       "eltRadiusServerAuthPortNumber": eltRadiusServerAuthPortNumber,
       "eltRadiusServerAcctPortNumber": eltRadiusServerAcctPortNumber,
       "eltRadiusServerAuthClientTimeouts": eltRadiusServerAuthClientTimeouts,
       "eltRadiusServerDeadStatus": eltRadiusServerDeadStatus,
       "eltRadiusServerRemainDeadTime": eltRadiusServerRemainDeadTime,
       "eltRadiusServerStatusReset": eltRadiusServerStatusReset}
)
