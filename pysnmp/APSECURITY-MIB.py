# SNMP MIB module (APSECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APSECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:58 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apSecurityModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9)
)
apSecurityModule.setRevisions(
        ("2012-07-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApSecurityMIBObjects_ObjectIdentity = ObjectIdentity
apSecurityMIBObjects = _ApSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1)
)
_ApSecurityIPsecTunCount_Type = Unsigned32
_ApSecurityIPsecTunCount_Object = MibScalar
apSecurityIPsecTunCount = _ApSecurityIPsecTunCount_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 1),
    _ApSecurityIPsecTunCount_Type()
)
apSecurityIPsecTunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIPsecTunCount.setStatus("current")
if mibBuilder.loadTexts:
    apSecurityIPsecTunCount.setUnits("tunnels")


class _ApSecurityIPsecTunCapPct_Type(Unsigned32):
    """Custom type apSecurityIPsecTunCapPct based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApSecurityIPsecTunCapPct_Type.__name__ = "Unsigned32"
_ApSecurityIPsecTunCapPct_Object = MibScalar
apSecurityIPsecTunCapPct = _ApSecurityIPsecTunCapPct_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 2),
    _ApSecurityIPsecTunCapPct_Type()
)
apSecurityIPsecTunCapPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIPsecTunCapPct.setStatus("current")
if mibBuilder.loadTexts:
    apSecurityIPsecTunCapPct.setUnits("%")
_ApSecurityIkeInterfaceStatsTable_Object = MibTable
apSecurityIkeInterfaceStatsTable = _ApSecurityIkeInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3)
)
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceStatsTable.setStatus("current")
_ApSecurityIkeInterfaceStatsEntry_Object = MibTableRow
apSecurityIkeInterfaceStatsEntry = _ApSecurityIkeInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1)
)
apSecurityIkeInterfaceStatsEntry.setIndexNames(
    (0, "APSECURITY-MIB", "apSecurityIkeInterfaceType"),
    (0, "APSECURITY-MIB", "apSecurityIkeInterfaceAddress"),
)
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceStatsEntry.setStatus("current")
_ApSecurityIkeInterfaceType_Type = InetAddressType
_ApSecurityIkeInterfaceType_Object = MibTableColumn
apSecurityIkeInterfaceType = _ApSecurityIkeInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 1),
    _ApSecurityIkeInterfaceType_Type()
)
apSecurityIkeInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceType.setStatus("current")
_ApSecurityIkeInterfaceAddress_Type = InetAddress
_ApSecurityIkeInterfaceAddress_Object = MibTableColumn
apSecurityIkeInterfaceAddress = _ApSecurityIkeInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 2),
    _ApSecurityIkeInterfaceAddress_Type()
)
apSecurityIkeInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceAddress.setStatus("current")
_ApSecurityIkeInterfaceCpuOverloadErrors_Type = Unsigned32
_ApSecurityIkeInterfaceCpuOverloadErrors_Object = MibTableColumn
apSecurityIkeInterfaceCpuOverloadErrors = _ApSecurityIkeInterfaceCpuOverloadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 3),
    _ApSecurityIkeInterfaceCpuOverloadErrors_Type()
)
apSecurityIkeInterfaceCpuOverloadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceCpuOverloadErrors.setStatus("current")
_ApSecurityIkeInterfaceInitCookieErrors_Type = Unsigned32
_ApSecurityIkeInterfaceInitCookieErrors_Object = MibTableColumn
apSecurityIkeInterfaceInitCookieErrors = _ApSecurityIkeInterfaceInitCookieErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 4),
    _ApSecurityIkeInterfaceInitCookieErrors_Type()
)
apSecurityIkeInterfaceInitCookieErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceInitCookieErrors.setStatus("current")
_ApSecurityIkeInterfaceAuthErrors_Type = Unsigned32
_ApSecurityIkeInterfaceAuthErrors_Object = MibTableColumn
apSecurityIkeInterfaceAuthErrors = _ApSecurityIkeInterfaceAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 5),
    _ApSecurityIkeInterfaceAuthErrors_Type()
)
apSecurityIkeInterfaceAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceAuthErrors.setStatus("current")
_ApSecurityIkeInterfaceEapAccessRequestErrors_Type = Unsigned32
_ApSecurityIkeInterfaceEapAccessRequestErrors_Object = MibTableColumn
apSecurityIkeInterfaceEapAccessRequestErrors = _ApSecurityIkeInterfaceEapAccessRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 6),
    _ApSecurityIkeInterfaceEapAccessRequestErrors_Type()
)
apSecurityIkeInterfaceEapAccessRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceEapAccessRequestErrors.setStatus("current")
_ApSecurityIkeInterfaceEapAccessChallengeErrors_Type = Unsigned32
_ApSecurityIkeInterfaceEapAccessChallengeErrors_Object = MibTableColumn
apSecurityIkeInterfaceEapAccessChallengeErrors = _ApSecurityIkeInterfaceEapAccessChallengeErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 7),
    _ApSecurityIkeInterfaceEapAccessChallengeErrors_Type()
)
apSecurityIkeInterfaceEapAccessChallengeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceEapAccessChallengeErrors.setStatus("current")
_ApSecurityIkeInterfaceTsErrors_Type = Unsigned32
_ApSecurityIkeInterfaceTsErrors_Object = MibTableColumn
apSecurityIkeInterfaceTsErrors = _ApSecurityIkeInterfaceTsErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 8),
    _ApSecurityIkeInterfaceTsErrors_Type()
)
apSecurityIkeInterfaceTsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceTsErrors.setStatus("current")
_ApSecurityIkeInterfaceCpErrors_Type = Unsigned32
_ApSecurityIkeInterfaceCpErrors_Object = MibTableColumn
apSecurityIkeInterfaceCpErrors = _ApSecurityIkeInterfaceCpErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 9),
    _ApSecurityIkeInterfaceCpErrors_Type()
)
apSecurityIkeInterfaceCpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceCpErrors.setStatus("current")
_ApSecurityIkeInterfaceKeErrors_Type = Unsigned32
_ApSecurityIkeInterfaceKeErrors_Object = MibTableColumn
apSecurityIkeInterfaceKeErrors = _ApSecurityIkeInterfaceKeErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 10),
    _ApSecurityIkeInterfaceKeErrors_Type()
)
apSecurityIkeInterfaceKeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceKeErrors.setStatus("current")
_ApSecurityIkeInterfaceProposalErrors_Type = Unsigned32
_ApSecurityIkeInterfaceProposalErrors_Object = MibTableColumn
apSecurityIkeInterfaceProposalErrors = _ApSecurityIkeInterfaceProposalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 11),
    _ApSecurityIkeInterfaceProposalErrors_Type()
)
apSecurityIkeInterfaceProposalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceProposalErrors.setStatus("current")
_ApSecurityIkeInterfaceSyntaxErrors_Type = Unsigned32
_ApSecurityIkeInterfaceSyntaxErrors_Object = MibTableColumn
apSecurityIkeInterfaceSyntaxErrors = _ApSecurityIkeInterfaceSyntaxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 12),
    _ApSecurityIkeInterfaceSyntaxErrors_Type()
)
apSecurityIkeInterfaceSyntaxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceSyntaxErrors.setStatus("current")
_ApSecurityIkeInterfaceCriticalPayloadErrors_Type = Unsigned32
_ApSecurityIkeInterfaceCriticalPayloadErrors_Object = MibTableColumn
apSecurityIkeInterfaceCriticalPayloadErrors = _ApSecurityIkeInterfaceCriticalPayloadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 13),
    _ApSecurityIkeInterfaceCriticalPayloadErrors_Type()
)
apSecurityIkeInterfaceCriticalPayloadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceCriticalPayloadErrors.setStatus("current")
_ApSecurityIkeInterfaceAuthFailureTca_Type = Unsigned32
_ApSecurityIkeInterfaceAuthFailureTca_Object = MibTableColumn
apSecurityIkeInterfaceAuthFailureTca = _ApSecurityIkeInterfaceAuthFailureTca_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 14),
    _ApSecurityIkeInterfaceAuthFailureTca_Type()
)
apSecurityIkeInterfaceAuthFailureTca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceAuthFailureTca.setStatus("current")
_ApSecurityIkeInterfaceTunnelRemovalsTca_Type = Unsigned32
_ApSecurityIkeInterfaceTunnelRemovalsTca_Object = MibTableColumn
apSecurityIkeInterfaceTunnelRemovalsTca = _ApSecurityIkeInterfaceTunnelRemovalsTca_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 15),
    _ApSecurityIkeInterfaceTunnelRemovalsTca_Type()
)
apSecurityIkeInterfaceTunnelRemovalsTca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceTunnelRemovalsTca.setStatus("current")
_ApSecurityIkeInterfaceDpdTca_Type = Unsigned32
_ApSecurityIkeInterfaceDpdTca_Object = MibTableColumn
apSecurityIkeInterfaceDpdTca = _ApSecurityIkeInterfaceDpdTca_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 3, 1, 16),
    _ApSecurityIkeInterfaceDpdTca_Type()
)
apSecurityIkeInterfaceDpdTca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceDpdTca.setStatus("current")
_ApSecurityTacacsTable_Object = MibTable
apSecurityTacacsTable = _ApSecurityTacacsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 4)
)
if mibBuilder.loadTexts:
    apSecurityTacacsTable.setStatus("current")
_ApSecurityTacacsEntry_Object = MibTableRow
apSecurityTacacsEntry = _ApSecurityTacacsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 4, 1)
)
apSecurityTacacsEntry.setIndexNames(
    (0, "APSECURITY-MIB", "apSecurityTacacsIndex"),
)
if mibBuilder.loadTexts:
    apSecurityTacacsEntry.setStatus("current")


class _ApSecurityTacacsIndex_Type(Integer32):
    """Custom type apSecurityTacacsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApSecurityTacacsIndex_Type.__name__ = "Integer32"
_ApSecurityTacacsIndex_Object = MibTableColumn
apSecurityTacacsIndex = _ApSecurityTacacsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 4, 1, 1),
    _ApSecurityTacacsIndex_Type()
)
apSecurityTacacsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSecurityTacacsIndex.setStatus("current")


class _ApSecurityTacacsServer_Type(DisplayString):
    """Custom type apSecurityTacacsServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSecurityTacacsServer_Type.__name__ = "DisplayString"
_ApSecurityTacacsServer_Object = MibTableColumn
apSecurityTacacsServer = _ApSecurityTacacsServer_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 4, 1, 2),
    _ApSecurityTacacsServer_Type()
)
apSecurityTacacsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityTacacsServer.setStatus("current")
_ApSecurityTacacsCliCommands_Type = Unsigned32
_ApSecurityTacacsCliCommands_Object = MibTableColumn
apSecurityTacacsCliCommands = _ApSecurityTacacsCliCommands_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 4, 1, 3),
    _ApSecurityTacacsCliCommands_Type()
)
apSecurityTacacsCliCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityTacacsCliCommands.setStatus("current")
_ApSecurityTacacsSuccessAuthentication_Type = Unsigned32
_ApSecurityTacacsSuccessAuthentication_Object = MibTableColumn
apSecurityTacacsSuccessAuthentication = _ApSecurityTacacsSuccessAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 4, 1, 4),
    _ApSecurityTacacsSuccessAuthentication_Type()
)
apSecurityTacacsSuccessAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityTacacsSuccessAuthentication.setStatus("current")
_ApSecurityTacacsFailureAuthentication_Type = Unsigned32
_ApSecurityTacacsFailureAuthentication_Object = MibTableColumn
apSecurityTacacsFailureAuthentication = _ApSecurityTacacsFailureAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 4, 1, 5),
    _ApSecurityTacacsFailureAuthentication_Type()
)
apSecurityTacacsFailureAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityTacacsFailureAuthentication.setStatus("current")
_ApSecurityTacacsSuccessAuthorization_Type = Unsigned32
_ApSecurityTacacsSuccessAuthorization_Object = MibTableColumn
apSecurityTacacsSuccessAuthorization = _ApSecurityTacacsSuccessAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 4, 1, 6),
    _ApSecurityTacacsSuccessAuthorization_Type()
)
apSecurityTacacsSuccessAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityTacacsSuccessAuthorization.setStatus("current")
_ApSecurityTacacsFailureAuthorization_Type = Unsigned32
_ApSecurityTacacsFailureAuthorization_Object = MibTableColumn
apSecurityTacacsFailureAuthorization = _ApSecurityTacacsFailureAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 4, 1, 7),
    _ApSecurityTacacsFailureAuthorization_Type()
)
apSecurityTacacsFailureAuthorization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityTacacsFailureAuthorization.setStatus("current")
_ApSecurityOCSRIpAddress_Type = IpAddress
_ApSecurityOCSRIpAddress_Object = MibScalar
apSecurityOCSRIpAddress = _ApSecurityOCSRIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 5),
    _ApSecurityOCSRIpAddress_Type()
)
apSecurityOCSRIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityOCSRIpAddress.setStatus("current")
_ApSecurityOCSRHostname_Type = DisplayString
_ApSecurityOCSRHostname_Object = MibScalar
apSecurityOCSRHostname = _ApSecurityOCSRHostname_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 6),
    _ApSecurityOCSRHostname_Type()
)
apSecurityOCSRHostname.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityOCSRHostname.setStatus("current")
_ApSecurityCrlIssuer_Type = DisplayString
_ApSecurityCrlIssuer_Object = MibScalar
apSecurityCrlIssuer = _ApSecurityCrlIssuer_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 7),
    _ApSecurityCrlIssuer_Type()
)
apSecurityCrlIssuer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityCrlIssuer.setStatus("current")
_ApSecurityCspName_Type = DisplayString
_ApSecurityCspName_Object = MibScalar
apSecurityCspName = _ApSecurityCspName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 8),
    _ApSecurityCspName_Type()
)
apSecurityCspName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityCspName.setStatus("current")
_ApSecurityIkeInterfaceInfoTable_Object = MibTable
apSecurityIkeInterfaceInfoTable = _ApSecurityIkeInterfaceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9)
)
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceInfoTable.setStatus("current")
_ApSecurityIkeInterfaceInfoEntry_Object = MibTableRow
apSecurityIkeInterfaceInfoEntry = _ApSecurityIkeInterfaceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1)
)
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceInfoEntry.setStatus("current")
_ApSecurityIkeInterfaceChildSaRequest_Type = Unsigned32
_ApSecurityIkeInterfaceChildSaRequest_Object = MibTableColumn
apSecurityIkeInterfaceChildSaRequest = _ApSecurityIkeInterfaceChildSaRequest_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 1),
    _ApSecurityIkeInterfaceChildSaRequest_Type()
)
apSecurityIkeInterfaceChildSaRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceChildSaRequest.setStatus("current")
_ApSecurityIkeInterfaceChildSaSuccess_Type = Unsigned32
_ApSecurityIkeInterfaceChildSaSuccess_Object = MibTableColumn
apSecurityIkeInterfaceChildSaSuccess = _ApSecurityIkeInterfaceChildSaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 2),
    _ApSecurityIkeInterfaceChildSaSuccess_Type()
)
apSecurityIkeInterfaceChildSaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceChildSaSuccess.setStatus("current")
_ApSecurityIkeInterfaceChildSaFail_Type = Unsigned32
_ApSecurityIkeInterfaceChildSaFail_Object = MibTableColumn
apSecurityIkeInterfaceChildSaFail = _ApSecurityIkeInterfaceChildSaFail_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 3),
    _ApSecurityIkeInterfaceChildSaFail_Type()
)
apSecurityIkeInterfaceChildSaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceChildSaFail.setStatus("current")
_ApSecurityIkeInterfaceChildSaDelRequest_Type = Unsigned32
_ApSecurityIkeInterfaceChildSaDelRequest_Object = MibTableColumn
apSecurityIkeInterfaceChildSaDelRequest = _ApSecurityIkeInterfaceChildSaDelRequest_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 4),
    _ApSecurityIkeInterfaceChildSaDelRequest_Type()
)
apSecurityIkeInterfaceChildSaDelRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceChildSaDelRequest.setStatus("current")
_ApSecurityIkeInterfaceChildSaDelSuccess_Type = Unsigned32
_ApSecurityIkeInterfaceChildSaDelSuccess_Object = MibTableColumn
apSecurityIkeInterfaceChildSaDelSuccess = _ApSecurityIkeInterfaceChildSaDelSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 5),
    _ApSecurityIkeInterfaceChildSaDelSuccess_Type()
)
apSecurityIkeInterfaceChildSaDelSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceChildSaDelSuccess.setStatus("current")
_ApSecurityIkeInterfaceChildSaDelFail_Type = Unsigned32
_ApSecurityIkeInterfaceChildSaDelFail_Object = MibTableColumn
apSecurityIkeInterfaceChildSaDelFail = _ApSecurityIkeInterfaceChildSaDelFail_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 6),
    _ApSecurityIkeInterfaceChildSaDelFail_Type()
)
apSecurityIkeInterfaceChildSaDelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceChildSaDelFail.setStatus("current")
_ApSecurityIkeInterfaceChildSaRekey_Type = Unsigned32
_ApSecurityIkeInterfaceChildSaRekey_Object = MibTableColumn
apSecurityIkeInterfaceChildSaRekey = _ApSecurityIkeInterfaceChildSaRekey_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 7),
    _ApSecurityIkeInterfaceChildSaRekey_Type()
)
apSecurityIkeInterfaceChildSaRekey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceChildSaRekey.setStatus("current")
_ApSecurityIkeInterfaceInitialChildSa_Type = Unsigned32
_ApSecurityIkeInterfaceInitialChildSa_Object = MibTableColumn
apSecurityIkeInterfaceInitialChildSa = _ApSecurityIkeInterfaceInitialChildSa_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 8),
    _ApSecurityIkeInterfaceInitialChildSa_Type()
)
apSecurityIkeInterfaceInitialChildSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceInitialChildSa.setStatus("current")
_ApSecurityIkeInterfaceDPDRecvPortChange_Type = Unsigned32
_ApSecurityIkeInterfaceDPDRecvPortChange_Object = MibTableColumn
apSecurityIkeInterfaceDPDRecvPortChange = _ApSecurityIkeInterfaceDPDRecvPortChange_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 9),
    _ApSecurityIkeInterfaceDPDRecvPortChange_Type()
)
apSecurityIkeInterfaceDPDRecvPortChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceDPDRecvPortChange.setStatus("current")
_ApSecurityIkeInterfaceDPDRecvIPChange_Type = Unsigned32
_ApSecurityIkeInterfaceDPDRecvIPChange_Object = MibTableColumn
apSecurityIkeInterfaceDPDRecvIPChange = _ApSecurityIkeInterfaceDPDRecvIPChange_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 10),
    _ApSecurityIkeInterfaceDPDRecvIPChange_Type()
)
apSecurityIkeInterfaceDPDRecvIPChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceDPDRecvIPChange.setStatus("current")
_ApSecurityIkeInterfaceDPDRespRecv_Type = Unsigned32
_ApSecurityIkeInterfaceDPDRespRecv_Object = MibTableColumn
apSecurityIkeInterfaceDPDRespRecv = _ApSecurityIkeInterfaceDPDRespRecv_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 11),
    _ApSecurityIkeInterfaceDPDRespRecv_Type()
)
apSecurityIkeInterfaceDPDRespRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceDPDRespRecv.setStatus("current")
_ApSecurityIkeInterfaceDPDRespNotRecv_Type = Unsigned32
_ApSecurityIkeInterfaceDPDRespNotRecv_Object = MibTableColumn
apSecurityIkeInterfaceDPDRespNotRecv = _ApSecurityIkeInterfaceDPDRespNotRecv_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 12),
    _ApSecurityIkeInterfaceDPDRespNotRecv_Type()
)
apSecurityIkeInterfaceDPDRespNotRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceDPDRespNotRecv.setStatus("current")
_ApSecurityIkeInterfaceDPDRecv_Type = Unsigned32
_ApSecurityIkeInterfaceDPDRecv_Object = MibTableColumn
apSecurityIkeInterfaceDPDRecv = _ApSecurityIkeInterfaceDPDRecv_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 13),
    _ApSecurityIkeInterfaceDPDRecv_Type()
)
apSecurityIkeInterfaceDPDRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceDPDRecv.setStatus("current")
_ApSecurityIkeInterfaceDPDRetran_Type = Unsigned32
_ApSecurityIkeInterfaceDPDRetran_Object = MibTableColumn
apSecurityIkeInterfaceDPDRetran = _ApSecurityIkeInterfaceDPDRetran_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 14),
    _ApSecurityIkeInterfaceDPDRetran_Type()
)
apSecurityIkeInterfaceDPDRetran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceDPDRetran.setStatus("current")
_ApSecurityIkeInterfaceDPDSent_Type = Unsigned32
_ApSecurityIkeInterfaceDPDSent_Object = MibTableColumn
apSecurityIkeInterfaceDPDSent = _ApSecurityIkeInterfaceDPDSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 15),
    _ApSecurityIkeInterfaceDPDSent_Type()
)
apSecurityIkeInterfaceDPDSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceDPDSent.setStatus("current")
_ApSecurityIkeInterfaceIKESAPacketSent_Type = Unsigned32
_ApSecurityIkeInterfaceIKESAPacketSent_Object = MibTableColumn
apSecurityIkeInterfaceIKESAPacketSent = _ApSecurityIkeInterfaceIKESAPacketSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 16),
    _ApSecurityIkeInterfaceIKESAPacketSent_Type()
)
apSecurityIkeInterfaceIKESAPacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceIKESAPacketSent.setStatus("current")
_ApSecurityIkeInterfaceIKESAPacketRcv_Type = Unsigned32
_ApSecurityIkeInterfaceIKESAPacketRcv_Object = MibTableColumn
apSecurityIkeInterfaceIKESAPacketRcv = _ApSecurityIkeInterfaceIKESAPacketRcv_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 17),
    _ApSecurityIkeInterfaceIKESAPacketRcv_Type()
)
apSecurityIkeInterfaceIKESAPacketRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceIKESAPacketRcv.setStatus("current")
_ApSecurityIkeInterfaceIKESAPacketDropped_Type = Unsigned32
_ApSecurityIkeInterfaceIKESAPacketDropped_Object = MibTableColumn
apSecurityIkeInterfaceIKESAPacketDropped = _ApSecurityIkeInterfaceIKESAPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 18),
    _ApSecurityIkeInterfaceIKESAPacketDropped_Type()
)
apSecurityIkeInterfaceIKESAPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceIKESAPacketDropped.setStatus("current")
_ApSecurityIkeInterfaceAuthFailure_Type = Unsigned32
_ApSecurityIkeInterfaceAuthFailure_Object = MibTableColumn
apSecurityIkeInterfaceAuthFailure = _ApSecurityIkeInterfaceAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 19),
    _ApSecurityIkeInterfaceAuthFailure_Type()
)
apSecurityIkeInterfaceAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceAuthFailure.setStatus("current")
_ApSecurityIkeInterfaceMsgError_Type = Unsigned32
_ApSecurityIkeInterfaceMsgError_Object = MibTableColumn
apSecurityIkeInterfaceMsgError = _ApSecurityIkeInterfaceMsgError_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 20),
    _ApSecurityIkeInterfaceMsgError_Type()
)
apSecurityIkeInterfaceMsgError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceMsgError.setStatus("current")
_ApSecurityIkeInterfaceAuthIDError_Type = Unsigned32
_ApSecurityIkeInterfaceAuthIDError_Object = MibTableColumn
apSecurityIkeInterfaceAuthIDError = _ApSecurityIkeInterfaceAuthIDError_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 21),
    _ApSecurityIkeInterfaceAuthIDError_Type()
)
apSecurityIkeInterfaceAuthIDError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceAuthIDError.setStatus("current")
_ApSecurityIkeInterfaceAuthCertCheckRequest_Type = Unsigned32
_ApSecurityIkeInterfaceAuthCertCheckRequest_Object = MibTableColumn
apSecurityIkeInterfaceAuthCertCheckRequest = _ApSecurityIkeInterfaceAuthCertCheckRequest_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 22),
    _ApSecurityIkeInterfaceAuthCertCheckRequest_Type()
)
apSecurityIkeInterfaceAuthCertCheckRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceAuthCertCheckRequest.setStatus("current")
_ApSecurityIkeInterfaceAuthCertCheckSuccess_Type = Unsigned32
_ApSecurityIkeInterfaceAuthCertCheckSuccess_Object = MibTableColumn
apSecurityIkeInterfaceAuthCertCheckSuccess = _ApSecurityIkeInterfaceAuthCertCheckSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 23),
    _ApSecurityIkeInterfaceAuthCertCheckSuccess_Type()
)
apSecurityIkeInterfaceAuthCertCheckSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceAuthCertCheckSuccess.setStatus("current")
_ApSecurityIkeInterfaceAuthCertCheckFailure_Type = Unsigned32
_ApSecurityIkeInterfaceAuthCertCheckFailure_Object = MibTableColumn
apSecurityIkeInterfaceAuthCertCheckFailure = _ApSecurityIkeInterfaceAuthCertCheckFailure_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 24),
    _ApSecurityIkeInterfaceAuthCertCheckFailure_Type()
)
apSecurityIkeInterfaceAuthCertCheckFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceAuthCertCheckFailure.setStatus("current")
_ApSecurityIkeInterfaceDDosSent_Type = Unsigned32
_ApSecurityIkeInterfaceDDosSent_Object = MibTableColumn
apSecurityIkeInterfaceDDosSent = _ApSecurityIkeInterfaceDDosSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 25),
    _ApSecurityIkeInterfaceDDosSent_Type()
)
apSecurityIkeInterfaceDDosSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceDDosSent.setStatus("current")
_ApSecurityIkeInterfaceDDosRecv_Type = Unsigned32
_ApSecurityIkeInterfaceDDosRecv_Object = MibTableColumn
apSecurityIkeInterfaceDDosRecv = _ApSecurityIkeInterfaceDDosRecv_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 26),
    _ApSecurityIkeInterfaceDDosRecv_Type()
)
apSecurityIkeInterfaceDDosRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceDDosRecv.setStatus("current")
_ApSecurityIkeInterfaceMessageRetrans_Type = Unsigned32
_ApSecurityIkeInterfaceMessageRetrans_Object = MibTableColumn
apSecurityIkeInterfaceMessageRetrans = _ApSecurityIkeInterfaceMessageRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 27),
    _ApSecurityIkeInterfaceMessageRetrans_Type()
)
apSecurityIkeInterfaceMessageRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceMessageRetrans.setStatus("current")
_ApSecurityIkeInterfaceSAInitMsgRecv_Type = Unsigned32
_ApSecurityIkeInterfaceSAInitMsgRecv_Object = MibTableColumn
apSecurityIkeInterfaceSAInitMsgRecv = _ApSecurityIkeInterfaceSAInitMsgRecv_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 28),
    _ApSecurityIkeInterfaceSAInitMsgRecv_Type()
)
apSecurityIkeInterfaceSAInitMsgRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceSAInitMsgRecv.setStatus("current")
_ApSecurityIkeInterfaceSAInitMsgSent_Type = Unsigned32
_ApSecurityIkeInterfaceSAInitMsgSent_Object = MibTableColumn
apSecurityIkeInterfaceSAInitMsgSent = _ApSecurityIkeInterfaceSAInitMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 29),
    _ApSecurityIkeInterfaceSAInitMsgSent_Type()
)
apSecurityIkeInterfaceSAInitMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceSAInitMsgSent.setStatus("current")
_ApSecurityIkeInterfaceSAEstablishmentAttempts_Type = Unsigned32
_ApSecurityIkeInterfaceSAEstablishmentAttempts_Object = MibTableColumn
apSecurityIkeInterfaceSAEstablishmentAttempts = _ApSecurityIkeInterfaceSAEstablishmentAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 30),
    _ApSecurityIkeInterfaceSAEstablishmentAttempts_Type()
)
apSecurityIkeInterfaceSAEstablishmentAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceSAEstablishmentAttempts.setStatus("current")
_ApSecurityIkeInterfaceSAEstablishmentSuccess_Type = Unsigned32
_ApSecurityIkeInterfaceSAEstablishmentSuccess_Object = MibTableColumn
apSecurityIkeInterfaceSAEstablishmentSuccess = _ApSecurityIkeInterfaceSAEstablishmentSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 31),
    _ApSecurityIkeInterfaceSAEstablishmentSuccess_Type()
)
apSecurityIkeInterfaceSAEstablishmentSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceSAEstablishmentSuccess.setStatus("current")
_ApSecurityIkeInterfaceTunnelRate_Type = Unsigned32
_ApSecurityIkeInterfaceTunnelRate_Object = MibTableColumn
apSecurityIkeInterfaceTunnelRate = _ApSecurityIkeInterfaceTunnelRate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 32),
    _ApSecurityIkeInterfaceTunnelRate_Type()
)
apSecurityIkeInterfaceTunnelRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceTunnelRate.setStatus("current")
_ApSecurityIkeInterfaceCurrentChildSaPair_Type = Unsigned32
_ApSecurityIkeInterfaceCurrentChildSaPair_Object = MibTableColumn
apSecurityIkeInterfaceCurrentChildSaPair = _ApSecurityIkeInterfaceCurrentChildSaPair_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 9, 1, 33),
    _ApSecurityIkeInterfaceCurrentChildSaPair_Type()
)
apSecurityIkeInterfaceCurrentChildSaPair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceCurrentChildSaPair.setStatus("current")
_ApSecurityCertificateTable_Object = MibTable
apSecurityCertificateTable = _ApSecurityCertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 10)
)
if mibBuilder.loadTexts:
    apSecurityCertificateTable.setStatus("current")
_ApSecurityCertificateEntry_Object = MibTableRow
apSecurityCertificateEntry = _ApSecurityCertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 10, 1)
)
apSecurityCertificateEntry.setIndexNames(
    (0, "APSECURITY-MIB", "apSecurityCertificateConfigId"),
    (0, "APSECURITY-MIB", "apSecurityCertificateIndex"),
)
if mibBuilder.loadTexts:
    apSecurityCertificateEntry.setStatus("current")
_ApSecurityCertificateConfigId_Type = Unsigned32
_ApSecurityCertificateConfigId_Object = MibTableColumn
apSecurityCertificateConfigId = _ApSecurityCertificateConfigId_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 10, 1, 1),
    _ApSecurityCertificateConfigId_Type()
)
apSecurityCertificateConfigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSecurityCertificateConfigId.setStatus("current")
_ApSecurityCertificateIndex_Type = Unsigned32
_ApSecurityCertificateIndex_Object = MibTableColumn
apSecurityCertificateIndex = _ApSecurityCertificateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 10, 1, 2),
    _ApSecurityCertificateIndex_Type()
)
apSecurityCertificateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSecurityCertificateIndex.setStatus("current")


class _ApSecurityCertificateRecordName_Type(DisplayString):
    """Custom type apSecurityCertificateRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSecurityCertificateRecordName_Type.__name__ = "DisplayString"
_ApSecurityCertificateRecordName_Object = MibTableColumn
apSecurityCertificateRecordName = _ApSecurityCertificateRecordName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 10, 1, 3),
    _ApSecurityCertificateRecordName_Type()
)
apSecurityCertificateRecordName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityCertificateRecordName.setStatus("current")


class _ApSecurityCertificateCertSubject_Type(DisplayString):
    """Custom type apSecurityCertificateCertSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSecurityCertificateCertSubject_Type.__name__ = "DisplayString"
_ApSecurityCertificateCertSubject_Object = MibTableColumn
apSecurityCertificateCertSubject = _ApSecurityCertificateCertSubject_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 10, 1, 4),
    _ApSecurityCertificateCertSubject_Type()
)
apSecurityCertificateCertSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityCertificateCertSubject.setStatus("current")


class _ApSecurityCertificateCertStart_Type(DisplayString):
    """Custom type apSecurityCertificateCertStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSecurityCertificateCertStart_Type.__name__ = "DisplayString"
_ApSecurityCertificateCertStart_Object = MibTableColumn
apSecurityCertificateCertStart = _ApSecurityCertificateCertStart_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 10, 1, 5),
    _ApSecurityCertificateCertStart_Type()
)
apSecurityCertificateCertStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityCertificateCertStart.setStatus("current")


class _ApSecurityCertificateCertExpire_Type(DisplayString):
    """Custom type apSecurityCertificateCertExpire based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSecurityCertificateCertExpire_Type.__name__ = "DisplayString"
_ApSecurityCertificateCertExpire_Object = MibTableColumn
apSecurityCertificateCertExpire = _ApSecurityCertificateCertExpire_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 10, 1, 6),
    _ApSecurityCertificateCertExpire_Type()
)
apSecurityCertificateCertExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityCertificateCertExpire.setStatus("current")


class _ApSecurityCertificateCertIssuer_Type(DisplayString):
    """Custom type apSecurityCertificateCertIssuer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSecurityCertificateCertIssuer_Type.__name__ = "DisplayString"
_ApSecurityCertificateCertIssuer_Object = MibTableColumn
apSecurityCertificateCertIssuer = _ApSecurityCertificateCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 10, 1, 7),
    _ApSecurityCertificateCertIssuer_Type()
)
apSecurityCertificateCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityCertificateCertIssuer.setStatus("current")
_ApSecurityCertificateCertIsCA_Type = TruthValue
_ApSecurityCertificateCertIsCA_Object = MibTableColumn
apSecurityCertificateCertIsCA = _ApSecurityCertificateCertIsCA_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 1, 10, 1, 8),
    _ApSecurityCertificateCertIsCA_Type()
)
apSecurityCertificateCertIsCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSecurityCertificateCertIsCA.setStatus("current")
_ApSecurityNotificationObjects_ObjectIdentity = ObjectIdentity
apSecurityNotificationObjects = _ApSecurityNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2)
)
_ApSecuritySpi_Type = Unsigned32
_ApSecuritySpi_Object = MibScalar
apSecuritySpi = _ApSecuritySpi_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 1),
    _ApSecuritySpi_Type()
)
apSecuritySpi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecuritySpi.setStatus("current")
_ApSecuritySrcIpAddress_Type = IpAddress
_ApSecuritySrcIpAddress_Object = MibScalar
apSecuritySrcIpAddress = _ApSecuritySrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 2),
    _ApSecuritySrcIpAddress_Type()
)
apSecuritySrcIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecuritySrcIpAddress.setStatus("current")
_ApSecurityDstIpAddress_Type = IpAddress
_ApSecurityDstIpAddress_Object = MibScalar
apSecurityDstIpAddress = _ApSecurityDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 3),
    _ApSecurityDstIpAddress_Type()
)
apSecurityDstIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityDstIpAddress.setStatus("current")


class _ApSecurityIPSECMode_Type(Integer32):
    """Custom type apSecurityIPSECMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("transport", 1),
          ("tunnel", 0))
    )


_ApSecurityIPSECMode_Type.__name__ = "Integer32"
_ApSecurityIPSECMode_Object = MibScalar
apSecurityIPSECMode = _ApSecurityIPSECMode_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 4),
    _ApSecurityIPSECMode_Type()
)
apSecurityIPSECMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityIPSECMode.setStatus("current")


class _ApSecurityEncryptionAlg_Type(Integer32):
    """Custom type apSecurityEncryptionAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alg-3des", 2),
          ("alg-aes", 4),
          ("alg-blowfish", 3),
          ("alg-des", 1),
          ("any", 0),
          ("null", 5))
    )


_ApSecurityEncryptionAlg_Type.__name__ = "Integer32"
_ApSecurityEncryptionAlg_Object = MibScalar
apSecurityEncryptionAlg = _ApSecurityEncryptionAlg_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 5),
    _ApSecurityEncryptionAlg_Type()
)
apSecurityEncryptionAlg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityEncryptionAlg.setStatus("current")


class _ApSecurityAuthAlg_Type(Integer32):
    """Custom type apSecurityAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("md5", 1),
          ("sha1", 2))
    )


_ApSecurityAuthAlg_Type.__name__ = "Integer32"
_ApSecurityAuthAlg_Object = MibScalar
apSecurityAuthAlg = _ApSecurityAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 6),
    _ApSecurityAuthAlg_Type()
)
apSecurityAuthAlg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityAuthAlg.setStatus("current")


class _ApSecuritySecProtocol_Type(Integer32):
    """Custom type apSecuritySecProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ah", 0),
          ("esp", 1),
          ("esp-auth", 2),
          ("esp-null", 3))
    )


_ApSecuritySecProtocol_Type.__name__ = "Integer32"
_ApSecuritySecProtocol_Object = MibScalar
apSecuritySecProtocol = _ApSecuritySecProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 7),
    _ApSecuritySecProtocol_Type()
)
apSecuritySecProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecuritySecProtocol.setStatus("current")


class _ApSecurityFailureCause_Type(Integer32):
    """Custom type apSecurityFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("access-reject", 10),
          ("accounting-failure", 15),
          ("authentication-failure", 13),
          ("authorization-failure", 14),
          ("incorrect-auth-alg", 5),
          ("incorrect-dh-group", 3),
          ("incorrect-encryption-alg", 4),
          ("incorrect-hash", 7),
          ("incorrect-id", 0),
          ("incorrect-mode", 8),
          ("incorrect-sec-protocol", 6),
          ("incorrect-shared-secret", 2),
          ("incorrect-user-passwd", 1),
          ("initiator-timeout", 11),
          ("invalid-certificate", 12),
          ("service-unavailable", 9))
    )


_ApSecurityFailureCause_Type.__name__ = "Integer32"
_ApSecurityFailureCause_Object = MibScalar
apSecurityFailureCause = _ApSecurityFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 8),
    _ApSecurityFailureCause_Type()
)
apSecurityFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityFailureCause.setStatus("current")


class _ApSecurityFailureArea_Type(Integer32):
    """Custom type apSecurityFailureArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ike", 0),
          ("ipsec", 1),
          ("radius", 2),
          ("tacacs", 3))
    )


_ApSecurityFailureArea_Type.__name__ = "Integer32"
_ApSecurityFailureArea_Object = MibScalar
apSecurityFailureArea = _ApSecurityFailureArea_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 9),
    _ApSecurityFailureArea_Type()
)
apSecurityFailureArea.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityFailureArea.setStatus("current")


class _ApSecurityStatus_Type(Integer32):
    """Custom type apSecurityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_ApSecurityStatus_Type.__name__ = "Integer32"
_ApSecurityStatus_Object = MibScalar
apSecurityStatus = _ApSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 10),
    _ApSecurityStatus_Type()
)
apSecurityStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityStatus.setStatus("current")
_ApSecurityDateTime_Type = DisplayString
_ApSecurityDateTime_Object = MibScalar
apSecurityDateTime = _ApSecurityDateTime_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 11),
    _ApSecurityDateTime_Type()
)
apSecurityDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityDateTime.setStatus("current")


class _ApSecurityUser_Type(DisplayString):
    """Custom type apSecurityUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSecurityUser_Type.__name__ = "DisplayString"
_ApSecurityUser_Object = MibScalar
apSecurityUser = _ApSecurityUser_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 12),
    _ApSecurityUser_Type()
)
apSecurityUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityUser.setStatus("current")
_ApSecurityPeerPort_Type = InetPortNumber
_ApSecurityPeerPort_Object = MibScalar
apSecurityPeerPort = _ApSecurityPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 13),
    _ApSecurityPeerPort_Type()
)
apSecurityPeerPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityPeerPort.setStatus("current")
_ApSecurityPeerIpAddress_Type = IpAddress
_ApSecurityPeerIpAddress_Object = MibScalar
apSecurityPeerIpAddress = _ApSecurityPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 14),
    _ApSecurityPeerIpAddress_Type()
)
apSecurityPeerIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityPeerIpAddress.setStatus("current")
_ApSecurityCRLServer_Type = DisplayString
_ApSecurityCRLServer_Object = MibScalar
apSecurityCRLServer = _ApSecurityCRLServer_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 15),
    _ApSecurityCRLServer_Type()
)
apSecurityCRLServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityCRLServer.setStatus("current")


class _ApSecurityCRLRetrievalFailureCause_Type(Integer32):
    """Custom type apSecurityCRLRetrievalFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incorrect-response", 1),
          ("internal", 0),
          ("timeout", 2))
    )


_ApSecurityCRLRetrievalFailureCause_Type.__name__ = "Integer32"
_ApSecurityCRLRetrievalFailureCause_Object = MibScalar
apSecurityCRLRetrievalFailureCause = _ApSecurityCRLRetrievalFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 16),
    _ApSecurityCRLRetrievalFailureCause_Type()
)
apSecurityCRLRetrievalFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityCRLRetrievalFailureCause.setStatus("current")
_ApSecurityLastSuccessfulCRLRetrieval_Type = Integer32
_ApSecurityLastSuccessfulCRLRetrieval_Object = MibScalar
apSecurityLastSuccessfulCRLRetrieval = _ApSecurityLastSuccessfulCRLRetrieval_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 17),
    _ApSecurityLastSuccessfulCRLRetrieval_Type()
)
apSecurityLastSuccessfulCRLRetrieval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityLastSuccessfulCRLRetrieval.setStatus("current")
_ApSecurityCRLServerIPAddress_Type = IpAddress
_ApSecurityCRLServerIPAddress_Object = MibScalar
apSecurityCRLServerIPAddress = _ApSecurityCRLServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 18),
    _ApSecurityCRLServerIPAddress_Type()
)
apSecurityCRLServerIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityCRLServerIPAddress.setStatus("current")
_ApSecurityGTPProfileName_Type = DisplayString
_ApSecurityGTPProfileName_Object = MibScalar
apSecurityGTPProfileName = _ApSecurityGTPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 19),
    _ApSecurityGTPProfileName_Type()
)
apSecurityGTPProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityGTPProfileName.setStatus("current")
_ApSecurityGTPHostName_Type = DisplayString
_ApSecurityGTPHostName_Object = MibScalar
apSecurityGTPHostName = _ApSecurityGTPHostName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 20),
    _ApSecurityGTPHostName_Type()
)
apSecurityGTPHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityGTPHostName.setStatus("current")


class _ApSecurityGTPLinkFailureCause_Type(Integer32):
    """Custom type apSecurityGTPLinkFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("timeout", 1),
          ("versionError", 2))
    )


_ApSecurityGTPLinkFailureCause_Type.__name__ = "Integer32"
_ApSecurityGTPLinkFailureCause_Object = MibScalar
apSecurityGTPLinkFailureCause = _ApSecurityGTPLinkFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 21),
    _ApSecurityGTPLinkFailureCause_Type()
)
apSecurityGTPLinkFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityGTPLinkFailureCause.setStatus("current")
_ApSecurityGTPIPAddress_Type = IpAddress
_ApSecurityGTPIPAddress_Object = MibScalar
apSecurityGTPIPAddress = _ApSecurityGTPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 22),
    _ApSecurityGTPIPAddress_Type()
)
apSecurityGTPIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityGTPIPAddress.setStatus("current")
_ApSecuritySrcAddressFamily_Type = InetAddressType
_ApSecuritySrcAddressFamily_Object = MibScalar
apSecuritySrcAddressFamily = _ApSecuritySrcAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 23),
    _ApSecuritySrcAddressFamily_Type()
)
apSecuritySrcAddressFamily.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecuritySrcAddressFamily.setStatus("current")
_ApSecuritySrcAddress_Type = InetAddress
_ApSecuritySrcAddress_Object = MibScalar
apSecuritySrcAddress = _ApSecuritySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 24),
    _ApSecuritySrcAddress_Type()
)
apSecuritySrcAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecuritySrcAddress.setStatus("current")
_ApSecurityDstAddressFamily_Type = InetAddressType
_ApSecurityDstAddressFamily_Object = MibScalar
apSecurityDstAddressFamily = _ApSecurityDstAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 25),
    _ApSecurityDstAddressFamily_Type()
)
apSecurityDstAddressFamily.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityDstAddressFamily.setStatus("current")
_ApSecurityDstAddress_Type = InetAddress
_ApSecurityDstAddress_Object = MibScalar
apSecurityDstAddress = _ApSecurityDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 26),
    _ApSecurityDstAddress_Type()
)
apSecurityDstAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityDstAddress.setStatus("current")
_ApSecurityPeerAddressFamily_Type = InetAddressType
_ApSecurityPeerAddressFamily_Object = MibScalar
apSecurityPeerAddressFamily = _ApSecurityPeerAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 27),
    _ApSecurityPeerAddressFamily_Type()
)
apSecurityPeerAddressFamily.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityPeerAddressFamily.setStatus("current")
_ApSecurityPeerAddress_Type = InetAddress
_ApSecurityPeerAddress_Object = MibScalar
apSecurityPeerAddress = _ApSecurityPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 2, 28),
    _ApSecurityPeerAddress_Type()
)
apSecurityPeerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSecurityPeerAddress.setStatus("current")
_ApSecurityNotifications_ObjectIdentity = ObjectIdentity
apSecurityNotifications = _ApSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3)
)
_ApSecurityAuthNotificationsPrefix_ObjectIdentity = ObjectIdentity
apSecurityAuthNotificationsPrefix = _ApSecurityAuthNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 1)
)
_ApSecurityAuthNotifications_ObjectIdentity = ObjectIdentity
apSecurityAuthNotifications = _ApSecurityAuthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 1, 0)
)
_ApSecurityGeneralNotificationsPrefix_ObjectIdentity = ObjectIdentity
apSecurityGeneralNotificationsPrefix = _ApSecurityGeneralNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 2)
)
_ApSecurityGeneralNotifications_ObjectIdentity = ObjectIdentity
apSecurityGeneralNotifications = _ApSecurityGeneralNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 2, 0)
)
_ApSecurityOCSRNotificationsPrefix_ObjectIdentity = ObjectIdentity
apSecurityOCSRNotificationsPrefix = _ApSecurityOCSRNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 3)
)
_ApSecurityOCSRNotifications_ObjectIdentity = ObjectIdentity
apSecurityOCSRNotifications = _ApSecurityOCSRNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 3, 0)
)
_ApSecurityCrlNotificationsPrefix_ObjectIdentity = ObjectIdentity
apSecurityCrlNotificationsPrefix = _ApSecurityCrlNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 4)
)
_ApSecurityCrlNotifications_ObjectIdentity = ObjectIdentity
apSecurityCrlNotifications = _ApSecurityCrlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 4, 0)
)
_ApSecurityCRLRetrievalNotificationsPrefix_ObjectIdentity = ObjectIdentity
apSecurityCRLRetrievalNotificationsPrefix = _ApSecurityCRLRetrievalNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 5)
)
_ApSecurityCRLRetrievalNotifications_ObjectIdentity = ObjectIdentity
apSecurityCRLRetrievalNotifications = _ApSecurityCRLRetrievalNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 5, 0)
)
_ApSecurityCertNotificationsPrefix_ObjectIdentity = ObjectIdentity
apSecurityCertNotificationsPrefix = _ApSecurityCertNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 6)
)
_ApSecurityCertNotifications_ObjectIdentity = ObjectIdentity
apSecurityCertNotifications = _ApSecurityCertNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 6, 0)
)
_ApSecurityGTPFailureNotificationsPrefix_ObjectIdentity = ObjectIdentity
apSecurityGTPFailureNotificationsPrefix = _ApSecurityGTPFailureNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 7)
)
_ApSecurityGTPFailureNotifications_ObjectIdentity = ObjectIdentity
apSecurityGTPFailureNotifications = _ApSecurityGTPFailureNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 7, 0)
)
_ApSecurityConformance_ObjectIdentity = ObjectIdentity
apSecurityConformance = _ApSecurityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4)
)
_ApSecurityCompliances_ObjectIdentity = ObjectIdentity
apSecurityCompliances = _ApSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 1)
)
_ApSecurityGroups_ObjectIdentity = ObjectIdentity
apSecurityGroups = _ApSecurityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 2)
)
_ApSecurityNotificationsGroups_ObjectIdentity = ObjectIdentity
apSecurityNotificationsGroups = _ApSecurityNotificationsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3)
)
apSecurityIkeInterfaceStatsEntry.registerAugmentions(
    ("APSECURITY-MIB",
     "apSecurityIkeInterfaceInfoEntry")
)
apSecurityIkeInterfaceInfoEntry.setIndexNames(*apSecurityIkeInterfaceStatsEntry.getIndexNames())

# Managed Objects groups

apSecurityIPsecTunnelsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 2, 1)
)
apSecurityIPsecTunnelsObjectsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityIPsecTunCount"),
        ("APSECURITY-MIB", "apSecurityIPsecTunCapPct"))
)
if mibBuilder.loadTexts:
    apSecurityIPsecTunnelsObjectsGroup.setStatus("current")

apSecurityIkeInterfaceObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 2, 2)
)
apSecurityIkeInterfaceObjectsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityIkeInterfaceInitCookieErrors"),
        ("APSECURITY-MIB", "apSecurityIkeInterfaceAuthErrors"),
        ("APSECURITY-MIB", "apSecurityIkeInterfaceEapAccessRequestErrors"),
        ("APSECURITY-MIB", "apSecurityIkeInterfaceEapAccessChallengeErrors"),
        ("APSECURITY-MIB", "apSecurityIkeInterfaceTsErrors"),
        ("APSECURITY-MIB", "apSecurityIkeInterfaceCpErrors"),
        ("APSECURITY-MIB", "apSecurityIkeInterfaceKeErrors"),
        ("APSECURITY-MIB", "apSecurityIkeInterfaceProposalErrors"),
        ("APSECURITY-MIB", "apSecurityIkeInterfaceSyntaxErrors"),
        ("APSECURITY-MIB", "apSecurityIkeInterfaceCriticalPayloadErrors"))
)
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceObjectsGroup.setStatus("current")

apSecurityTacacsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 2, 3)
)
apSecurityTacacsObjectsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityTacacsServer"),
        ("APSECURITY-MIB", "apSecurityTacacsCliCommands"),
        ("APSECURITY-MIB", "apSecurityTacacsSuccessAuthentication"),
        ("APSECURITY-MIB", "apSecurityTacacsFailureAuthentication"),
        ("APSECURITY-MIB", "apSecurityTacacsSuccessAuthorization"),
        ("APSECURITY-MIB", "apSecurityTacacsFailureAuthorization"))
)
if mibBuilder.loadTexts:
    apSecurityTacacsObjectsGroup.setStatus("current")

apSecurityCertObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 2, 4)
)
apSecurityCertObjectsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityCertificateRecordName"),
        ("APSECURITY-MIB", "apSecurityCertificateCertSubject"),
        ("APSECURITY-MIB", "apSecurityCertificateCertStart"),
        ("APSECURITY-MIB", "apSecurityCertificateCertExpire"),
        ("APSECURITY-MIB", "apSecurityCertificateCertIssuer"),
        ("APSECURITY-MIB", "apSecurityCertificateCertIsCA"))
)
if mibBuilder.loadTexts:
    apSecurityCertObjectsGroup.setStatus("current")

apSecurityIkeInterfaceInfoObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 2, 5)
)
apSecurityIkeInterfaceInfoObjectsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityIkeInterfaceTunnelRate"),
        ("APSECURITY-MIB", "apSecurityIkeInterfaceCurrentChildSaPair"))
)
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceInfoObjectsGroup.setStatus("current")


# Notification objects

apSecurityTunnelFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 1, 0, 1)
)
apSecurityTunnelFailureNotification.setObjects(
      *(("APSECURITY-MIB", "apSecuritySpi"),
        ("APSECURITY-MIB", "apSecuritySrcIpAddress"),
        ("APSECURITY-MIB", "apSecurityDstIpAddress"),
        ("APSECURITY-MIB", "apSecurityFailureCause"),
        ("APSECURITY-MIB", "apSecurityFailureArea"),
        ("APSECURITY-MIB", "apSecurityStatus"))
)
if mibBuilder.loadTexts:
    apSecurityTunnelFailureNotification.setStatus(
        "current"
    )

apSecurityRadiusFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 1, 0, 2)
)
apSecurityRadiusFailureNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityUser"),
        ("APSECURITY-MIB", "apSecurityFailureCause"),
        ("APSECURITY-MIB", "apSecurityFailureArea"),
        ("APSECURITY-MIB", "apSecurityStatus"))
)
if mibBuilder.loadTexts:
    apSecurityRadiusFailureNotification.setStatus(
        "current"
    )

apSecurityAuthFailureThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 1, 0, 3)
)
apSecurityAuthFailureThresholdNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityUser"),
        ("APSECURITY-MIB", "apSecurityPeerIpAddress"),
        ("APSECURITY-MIB", "apSecurityPeerPort"))
)
if mibBuilder.loadTexts:
    apSecurityAuthFailureThresholdNotification.setStatus(
        "current"
    )

apSecurityTacacsFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 1, 0, 4)
)
apSecurityTacacsFailureNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityUser"),
        ("APSECURITY-MIB", "apSecurityFailureCause"),
        ("APSECURITY-MIB", "apSecurityFailureArea"),
        ("APSECURITY-MIB", "apSecurityStatus"))
)
if mibBuilder.loadTexts:
    apSecurityTacacsFailureNotification.setStatus(
        "current"
    )

apSecurityTunnelFailureInetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 1, 0, 5)
)
apSecurityTunnelFailureInetNotification.setObjects(
      *(("APSECURITY-MIB", "apSecuritySpi"),
        ("APSECURITY-MIB", "apSecuritySrcAddressFamily"),
        ("APSECURITY-MIB", "apSecuritySrcAddress"),
        ("APSECURITY-MIB", "apSecurityDstAddressFamily"),
        ("APSECURITY-MIB", "apSecurityDstAddress"),
        ("APSECURITY-MIB", "apSecurityFailureCause"),
        ("APSECURITY-MIB", "apSecurityFailureArea"),
        ("APSECURITY-MIB", "apSecurityStatus"))
)
if mibBuilder.loadTexts:
    apSecurityTunnelFailureInetNotification.setStatus(
        "current"
    )

apSecurityAuthFailureThresholdInetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 1, 0, 6)
)
apSecurityAuthFailureThresholdInetNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityUser"),
        ("APSECURITY-MIB", "apSecurityPeerAddressFamily"),
        ("APSECURITY-MIB", "apSecurityPeerAddress"),
        ("APSECURITY-MIB", "apSecurityPeerPort"))
)
if mibBuilder.loadTexts:
    apSecurityAuthFailureThresholdInetNotification.setStatus(
        "current"
    )

apSecurityTunnelDPDNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 2, 0, 1)
)
apSecurityTunnelDPDNotification.setObjects(
      *(("APSECURITY-MIB", "apSecuritySpi"),
        ("APSECURITY-MIB", "apSecuritySrcIpAddress"),
        ("APSECURITY-MIB", "apSecurityDstIpAddress"),
        ("APSECURITY-MIB", "apSecurityFailureArea"),
        ("APSECURITY-MIB", "apSecurityStatus"))
)
if mibBuilder.loadTexts:
    apSecurityTunnelDPDNotification.setStatus(
        "current"
    )

apSecurityIPsecTunCapNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 2, 0, 2)
)
apSecurityIPsecTunCapNotification.setObjects(
    ("APSECURITY-MIB", "apSecurityIPsecTunCapPct")
)
if mibBuilder.loadTexts:
    apSecurityIPsecTunCapNotification.setStatus(
        "current"
    )

apSecurityIPsecTunCapClearNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 2, 0, 3)
)
apSecurityIPsecTunCapClearNotification.setObjects(
    ("APSECURITY-MIB", "apSecurityIPsecTunCapPct")
)
if mibBuilder.loadTexts:
    apSecurityIPsecTunCapClearNotification.setStatus(
        "current"
    )

apSecurityTunnelDPDInetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 2, 0, 4)
)
apSecurityTunnelDPDInetNotification.setObjects(
      *(("APSECURITY-MIB", "apSecuritySpi"),
        ("APSECURITY-MIB", "apSecuritySrcAddressFamily"),
        ("APSECURITY-MIB", "apSecuritySrcAddress"),
        ("APSECURITY-MIB", "apSecurityDstAddressFamily"),
        ("APSECURITY-MIB", "apSecurityDstAddress"),
        ("APSECURITY-MIB", "apSecurityFailureArea"),
        ("APSECURITY-MIB", "apSecurityStatus"))
)
if mibBuilder.loadTexts:
    apSecurityTunnelDPDInetNotification.setStatus(
        "current"
    )

apSecurityOCSRDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 3, 0, 1)
)
apSecurityOCSRDownNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityOCSRHostname"),
        ("APSECURITY-MIB", "apSecurityOCSRIpAddress"))
)
if mibBuilder.loadTexts:
    apSecurityOCSRDownNotification.setStatus(
        "current"
    )

apSecurityOCSRUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 3, 0, 2)
)
apSecurityOCSRUpNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityOCSRHostname"),
        ("APSECURITY-MIB", "apSecurityOCSRIpAddress"))
)
if mibBuilder.loadTexts:
    apSecurityOCSRUpNotification.setStatus(
        "current"
    )

apSecurityCrlInvalidNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 4, 0, 1)
)
apSecurityCrlInvalidNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityCrlIssuer"),
        ("APSECURITY-MIB", "apSecurityCspName"))
)
if mibBuilder.loadTexts:
    apSecurityCrlInvalidNotification.setStatus(
        "current"
    )

apSecurityCRLRetrievalFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 5, 0, 1)
)
apSecurityCRLRetrievalFailNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityCRLServer"),
        ("APSECURITY-MIB", "apSecurityCRLRetrievalFailureCause"),
        ("APSECURITY-MIB", "apSecurityLastSuccessfulCRLRetrieval"),
        ("APSECURITY-MIB", "apSecurityCRLServerIPAddress"))
)
if mibBuilder.loadTexts:
    apSecurityCRLRetrievalFailNotification.setStatus(
        "current"
    )

apSecurityCRLRetrievalClearNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 5, 0, 2)
)
apSecurityCRLRetrievalClearNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityCRLServer"),
        ("APSECURITY-MIB", "apSecurityCRLServerIPAddress"))
)
if mibBuilder.loadTexts:
    apSecurityCRLRetrievalClearNotification.setStatus(
        "current"
    )

apSecurityCertExpiredNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 6, 0, 1)
)
apSecurityCertExpiredNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityCertificateRecordName"),
        ("APSECURITY-MIB", "apSecurityCertificateCertSubject"),
        ("APSECURITY-MIB", "apSecurityCertificateCertExpire"),
        ("APSECURITY-MIB", "apSecurityCertificateCertIssuer"))
)
if mibBuilder.loadTexts:
    apSecurityCertExpiredNotification.setStatus(
        "current"
    )

apSecurityCertExpireSoonNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 6, 0, 2)
)
apSecurityCertExpireSoonNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityCertificateRecordName"),
        ("APSECURITY-MIB", "apSecurityCertificateCertSubject"),
        ("APSECURITY-MIB", "apSecurityCertificateCertExpire"),
        ("APSECURITY-MIB", "apSecurityCertificateCertIssuer"))
)
if mibBuilder.loadTexts:
    apSecurityCertExpireSoonNotification.setStatus(
        "current"
    )

apSecurityGTPLinkFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 7, 0, 1)
)
apSecurityGTPLinkFailureNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityGTPProfileName"),
        ("APSECURITY-MIB", "apSecurityGTPHostName"),
        ("APSECURITY-MIB", "apSecurityGTPLinkFailureCause"),
        ("APSECURITY-MIB", "apSecurityGTPIPAddress"))
)
if mibBuilder.loadTexts:
    apSecurityGTPLinkFailureNotification.setStatus(
        "current"
    )

apSecurityGTPLinkClearNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 3, 7, 0, 2)
)
apSecurityGTPLinkClearNotification.setObjects(
      *(("APSECURITY-MIB", "apSecurityGTPProfileName"),
        ("APSECURITY-MIB", "apSecurityGTPHostName"),
        ("APSECURITY-MIB", "apSecurityGTPIPAddress"))
)
if mibBuilder.loadTexts:
    apSecurityGTPLinkClearNotification.setStatus(
        "current"
    )


# Notifications groups

apSecurityNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3, 1)
)
apSecurityNotificationsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityTunnelFailureNotification"),
        ("APSECURITY-MIB", "apSecurityRadiusFailureNotification"),
        ("APSECURITY-MIB", "apSecurityTunnelDPDNotification"),
        ("APSECURITY-MIB", "apSecurityTacacsFailureNotification"))
)
if mibBuilder.loadTexts:
    apSecurityNotificationsGroup.setStatus(
        "current"
    )

apSecurityIPsecTunnelsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3, 2)
)
apSecurityIPsecTunnelsNotificationsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityIPsecTunCapNotification"),
        ("APSECURITY-MIB", "apSecurityIPsecTunCapClearNotification"))
)
if mibBuilder.loadTexts:
    apSecurityIPsecTunnelsNotificationsGroup.setStatus(
        "current"
    )

apSecurityDDosNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3, 3)
)
apSecurityDDosNotificationsGroup.setObjects(
    ("APSECURITY-MIB", "apSecurityAuthFailureThresholdNotification")
)
if mibBuilder.loadTexts:
    apSecurityDDosNotificationsGroup.setStatus(
        "current"
    )

apSecurityOCSRNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3, 4)
)
apSecurityOCSRNotificationsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityOCSRDownNotification"),
        ("APSECURITY-MIB", "apSecurityOCSRUpNotification"))
)
if mibBuilder.loadTexts:
    apSecurityOCSRNotificationsGroup.setStatus(
        "current"
    )

apSecurityCrlNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3, 5)
)
apSecurityCrlNotificationsGroup.setObjects(
    ("APSECURITY-MIB", "apSecurityCrlInvalidNotification")
)
if mibBuilder.loadTexts:
    apSecurityCrlNotificationsGroup.setStatus(
        "current"
    )

apSecurityCRLRetrievalNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3, 6)
)
apSecurityCRLRetrievalNotificationsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityCRLRetrievalFailNotification"),
        ("APSECURITY-MIB", "apSecurityCRLRetrievalClearNotification"))
)
if mibBuilder.loadTexts:
    apSecurityCRLRetrievalNotificationsGroup.setStatus(
        "current"
    )

apSecurityCertNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3, 7)
)
apSecurityCertNotificationsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityCertExpiredNotification"),
        ("APSECURITY-MIB", "apSecurityCertExpireSoonNotification"))
)
if mibBuilder.loadTexts:
    apSecurityCertNotificationsGroup.setStatus(
        "current"
    )

apSecurityGTPNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3, 8)
)
apSecurityGTPNotificationsGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityGTPLinkFailureNotification"),
        ("APSECURITY-MIB", "apSecurityGTPLinkClearNotification"))
)
if mibBuilder.loadTexts:
    apSecurityGTPNotificationsGroup.setStatus(
        "current"
    )

apSecurityNotificationsInetGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3, 9)
)
apSecurityNotificationsInetGroup.setObjects(
      *(("APSECURITY-MIB", "apSecurityTunnelFailureInetNotification"),
        ("APSECURITY-MIB", "apSecurityRadiusFailureNotification"),
        ("APSECURITY-MIB", "apSecurityTunnelDPDInetNotification"),
        ("APSECURITY-MIB", "apSecurityTacacsFailureNotification"))
)
if mibBuilder.loadTexts:
    apSecurityNotificationsInetGroup.setStatus(
        "current"
    )

apSecurityDDosNotificationsInetGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 9, 4, 3, 10)
)
apSecurityDDosNotificationsInetGroup.setObjects(
    ("APSECURITY-MIB", "apSecurityAuthFailureThresholdInetNotification")
)
if mibBuilder.loadTexts:
    apSecurityDDosNotificationsInetGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APSECURITY-MIB",
    **{"apSecurityModule": apSecurityModule,
       "apSecurityMIBObjects": apSecurityMIBObjects,
       "apSecurityIPsecTunCount": apSecurityIPsecTunCount,
       "apSecurityIPsecTunCapPct": apSecurityIPsecTunCapPct,
       "apSecurityIkeInterfaceStatsTable": apSecurityIkeInterfaceStatsTable,
       "apSecurityIkeInterfaceStatsEntry": apSecurityIkeInterfaceStatsEntry,
       "apSecurityIkeInterfaceType": apSecurityIkeInterfaceType,
       "apSecurityIkeInterfaceAddress": apSecurityIkeInterfaceAddress,
       "apSecurityIkeInterfaceCpuOverloadErrors": apSecurityIkeInterfaceCpuOverloadErrors,
       "apSecurityIkeInterfaceInitCookieErrors": apSecurityIkeInterfaceInitCookieErrors,
       "apSecurityIkeInterfaceAuthErrors": apSecurityIkeInterfaceAuthErrors,
       "apSecurityIkeInterfaceEapAccessRequestErrors": apSecurityIkeInterfaceEapAccessRequestErrors,
       "apSecurityIkeInterfaceEapAccessChallengeErrors": apSecurityIkeInterfaceEapAccessChallengeErrors,
       "apSecurityIkeInterfaceTsErrors": apSecurityIkeInterfaceTsErrors,
       "apSecurityIkeInterfaceCpErrors": apSecurityIkeInterfaceCpErrors,
       "apSecurityIkeInterfaceKeErrors": apSecurityIkeInterfaceKeErrors,
       "apSecurityIkeInterfaceProposalErrors": apSecurityIkeInterfaceProposalErrors,
       "apSecurityIkeInterfaceSyntaxErrors": apSecurityIkeInterfaceSyntaxErrors,
       "apSecurityIkeInterfaceCriticalPayloadErrors": apSecurityIkeInterfaceCriticalPayloadErrors,
       "apSecurityIkeInterfaceAuthFailureTca": apSecurityIkeInterfaceAuthFailureTca,
       "apSecurityIkeInterfaceTunnelRemovalsTca": apSecurityIkeInterfaceTunnelRemovalsTca,
       "apSecurityIkeInterfaceDpdTca": apSecurityIkeInterfaceDpdTca,
       "apSecurityTacacsTable": apSecurityTacacsTable,
       "apSecurityTacacsEntry": apSecurityTacacsEntry,
       "apSecurityTacacsIndex": apSecurityTacacsIndex,
       "apSecurityTacacsServer": apSecurityTacacsServer,
       "apSecurityTacacsCliCommands": apSecurityTacacsCliCommands,
       "apSecurityTacacsSuccessAuthentication": apSecurityTacacsSuccessAuthentication,
       "apSecurityTacacsFailureAuthentication": apSecurityTacacsFailureAuthentication,
       "apSecurityTacacsSuccessAuthorization": apSecurityTacacsSuccessAuthorization,
       "apSecurityTacacsFailureAuthorization": apSecurityTacacsFailureAuthorization,
       "apSecurityOCSRIpAddress": apSecurityOCSRIpAddress,
       "apSecurityOCSRHostname": apSecurityOCSRHostname,
       "apSecurityCrlIssuer": apSecurityCrlIssuer,
       "apSecurityCspName": apSecurityCspName,
       "apSecurityIkeInterfaceInfoTable": apSecurityIkeInterfaceInfoTable,
       "apSecurityIkeInterfaceInfoEntry": apSecurityIkeInterfaceInfoEntry,
       "apSecurityIkeInterfaceChildSaRequest": apSecurityIkeInterfaceChildSaRequest,
       "apSecurityIkeInterfaceChildSaSuccess": apSecurityIkeInterfaceChildSaSuccess,
       "apSecurityIkeInterfaceChildSaFail": apSecurityIkeInterfaceChildSaFail,
       "apSecurityIkeInterfaceChildSaDelRequest": apSecurityIkeInterfaceChildSaDelRequest,
       "apSecurityIkeInterfaceChildSaDelSuccess": apSecurityIkeInterfaceChildSaDelSuccess,
       "apSecurityIkeInterfaceChildSaDelFail": apSecurityIkeInterfaceChildSaDelFail,
       "apSecurityIkeInterfaceChildSaRekey": apSecurityIkeInterfaceChildSaRekey,
       "apSecurityIkeInterfaceInitialChildSa": apSecurityIkeInterfaceInitialChildSa,
       "apSecurityIkeInterfaceDPDRecvPortChange": apSecurityIkeInterfaceDPDRecvPortChange,
       "apSecurityIkeInterfaceDPDRecvIPChange": apSecurityIkeInterfaceDPDRecvIPChange,
       "apSecurityIkeInterfaceDPDRespRecv": apSecurityIkeInterfaceDPDRespRecv,
       "apSecurityIkeInterfaceDPDRespNotRecv": apSecurityIkeInterfaceDPDRespNotRecv,
       "apSecurityIkeInterfaceDPDRecv": apSecurityIkeInterfaceDPDRecv,
       "apSecurityIkeInterfaceDPDRetran": apSecurityIkeInterfaceDPDRetran,
       "apSecurityIkeInterfaceDPDSent": apSecurityIkeInterfaceDPDSent,
       "apSecurityIkeInterfaceIKESAPacketSent": apSecurityIkeInterfaceIKESAPacketSent,
       "apSecurityIkeInterfaceIKESAPacketRcv": apSecurityIkeInterfaceIKESAPacketRcv,
       "apSecurityIkeInterfaceIKESAPacketDropped": apSecurityIkeInterfaceIKESAPacketDropped,
       "apSecurityIkeInterfaceAuthFailure": apSecurityIkeInterfaceAuthFailure,
       "apSecurityIkeInterfaceMsgError": apSecurityIkeInterfaceMsgError,
       "apSecurityIkeInterfaceAuthIDError": apSecurityIkeInterfaceAuthIDError,
       "apSecurityIkeInterfaceAuthCertCheckRequest": apSecurityIkeInterfaceAuthCertCheckRequest,
       "apSecurityIkeInterfaceAuthCertCheckSuccess": apSecurityIkeInterfaceAuthCertCheckSuccess,
       "apSecurityIkeInterfaceAuthCertCheckFailure": apSecurityIkeInterfaceAuthCertCheckFailure,
       "apSecurityIkeInterfaceDDosSent": apSecurityIkeInterfaceDDosSent,
       "apSecurityIkeInterfaceDDosRecv": apSecurityIkeInterfaceDDosRecv,
       "apSecurityIkeInterfaceMessageRetrans": apSecurityIkeInterfaceMessageRetrans,
       "apSecurityIkeInterfaceSAInitMsgRecv": apSecurityIkeInterfaceSAInitMsgRecv,
       "apSecurityIkeInterfaceSAInitMsgSent": apSecurityIkeInterfaceSAInitMsgSent,
       "apSecurityIkeInterfaceSAEstablishmentAttempts": apSecurityIkeInterfaceSAEstablishmentAttempts,
       "apSecurityIkeInterfaceSAEstablishmentSuccess": apSecurityIkeInterfaceSAEstablishmentSuccess,
       "apSecurityIkeInterfaceTunnelRate": apSecurityIkeInterfaceTunnelRate,
       "apSecurityIkeInterfaceCurrentChildSaPair": apSecurityIkeInterfaceCurrentChildSaPair,
       "apSecurityCertificateTable": apSecurityCertificateTable,
       "apSecurityCertificateEntry": apSecurityCertificateEntry,
       "apSecurityCertificateConfigId": apSecurityCertificateConfigId,
       "apSecurityCertificateIndex": apSecurityCertificateIndex,
       "apSecurityCertificateRecordName": apSecurityCertificateRecordName,
       "apSecurityCertificateCertSubject": apSecurityCertificateCertSubject,
       "apSecurityCertificateCertStart": apSecurityCertificateCertStart,
       "apSecurityCertificateCertExpire": apSecurityCertificateCertExpire,
       "apSecurityCertificateCertIssuer": apSecurityCertificateCertIssuer,
       "apSecurityCertificateCertIsCA": apSecurityCertificateCertIsCA,
       "apSecurityNotificationObjects": apSecurityNotificationObjects,
       "apSecuritySpi": apSecuritySpi,
       "apSecuritySrcIpAddress": apSecuritySrcIpAddress,
       "apSecurityDstIpAddress": apSecurityDstIpAddress,
       "apSecurityIPSECMode": apSecurityIPSECMode,
       "apSecurityEncryptionAlg": apSecurityEncryptionAlg,
       "apSecurityAuthAlg": apSecurityAuthAlg,
       "apSecuritySecProtocol": apSecuritySecProtocol,
       "apSecurityFailureCause": apSecurityFailureCause,
       "apSecurityFailureArea": apSecurityFailureArea,
       "apSecurityStatus": apSecurityStatus,
       "apSecurityDateTime": apSecurityDateTime,
       "apSecurityUser": apSecurityUser,
       "apSecurityPeerPort": apSecurityPeerPort,
       "apSecurityPeerIpAddress": apSecurityPeerIpAddress,
       "apSecurityCRLServer": apSecurityCRLServer,
       "apSecurityCRLRetrievalFailureCause": apSecurityCRLRetrievalFailureCause,
       "apSecurityLastSuccessfulCRLRetrieval": apSecurityLastSuccessfulCRLRetrieval,
       "apSecurityCRLServerIPAddress": apSecurityCRLServerIPAddress,
       "apSecurityGTPProfileName": apSecurityGTPProfileName,
       "apSecurityGTPHostName": apSecurityGTPHostName,
       "apSecurityGTPLinkFailureCause": apSecurityGTPLinkFailureCause,
       "apSecurityGTPIPAddress": apSecurityGTPIPAddress,
       "apSecuritySrcAddressFamily": apSecuritySrcAddressFamily,
       "apSecuritySrcAddress": apSecuritySrcAddress,
       "apSecurityDstAddressFamily": apSecurityDstAddressFamily,
       "apSecurityDstAddress": apSecurityDstAddress,
       "apSecurityPeerAddressFamily": apSecurityPeerAddressFamily,
       "apSecurityPeerAddress": apSecurityPeerAddress,
       "apSecurityNotifications": apSecurityNotifications,
       "apSecurityAuthNotificationsPrefix": apSecurityAuthNotificationsPrefix,
       "apSecurityAuthNotifications": apSecurityAuthNotifications,
       "apSecurityTunnelFailureNotification": apSecurityTunnelFailureNotification,
       "apSecurityRadiusFailureNotification": apSecurityRadiusFailureNotification,
       "apSecurityAuthFailureThresholdNotification": apSecurityAuthFailureThresholdNotification,
       "apSecurityTacacsFailureNotification": apSecurityTacacsFailureNotification,
       "apSecurityTunnelFailureInetNotification": apSecurityTunnelFailureInetNotification,
       "apSecurityAuthFailureThresholdInetNotification": apSecurityAuthFailureThresholdInetNotification,
       "apSecurityGeneralNotificationsPrefix": apSecurityGeneralNotificationsPrefix,
       "apSecurityGeneralNotifications": apSecurityGeneralNotifications,
       "apSecurityTunnelDPDNotification": apSecurityTunnelDPDNotification,
       "apSecurityIPsecTunCapNotification": apSecurityIPsecTunCapNotification,
       "apSecurityIPsecTunCapClearNotification": apSecurityIPsecTunCapClearNotification,
       "apSecurityTunnelDPDInetNotification": apSecurityTunnelDPDInetNotification,
       "apSecurityOCSRNotificationsPrefix": apSecurityOCSRNotificationsPrefix,
       "apSecurityOCSRNotifications": apSecurityOCSRNotifications,
       "apSecurityOCSRDownNotification": apSecurityOCSRDownNotification,
       "apSecurityOCSRUpNotification": apSecurityOCSRUpNotification,
       "apSecurityCrlNotificationsPrefix": apSecurityCrlNotificationsPrefix,
       "apSecurityCrlNotifications": apSecurityCrlNotifications,
       "apSecurityCrlInvalidNotification": apSecurityCrlInvalidNotification,
       "apSecurityCRLRetrievalNotificationsPrefix": apSecurityCRLRetrievalNotificationsPrefix,
       "apSecurityCRLRetrievalNotifications": apSecurityCRLRetrievalNotifications,
       "apSecurityCRLRetrievalFailNotification": apSecurityCRLRetrievalFailNotification,
       "apSecurityCRLRetrievalClearNotification": apSecurityCRLRetrievalClearNotification,
       "apSecurityCertNotificationsPrefix": apSecurityCertNotificationsPrefix,
       "apSecurityCertNotifications": apSecurityCertNotifications,
       "apSecurityCertExpiredNotification": apSecurityCertExpiredNotification,
       "apSecurityCertExpireSoonNotification": apSecurityCertExpireSoonNotification,
       "apSecurityGTPFailureNotificationsPrefix": apSecurityGTPFailureNotificationsPrefix,
       "apSecurityGTPFailureNotifications": apSecurityGTPFailureNotifications,
       "apSecurityGTPLinkFailureNotification": apSecurityGTPLinkFailureNotification,
       "apSecurityGTPLinkClearNotification": apSecurityGTPLinkClearNotification,
       "apSecurityConformance": apSecurityConformance,
       "apSecurityCompliances": apSecurityCompliances,
       "apSecurityGroups": apSecurityGroups,
       "apSecurityIPsecTunnelsObjectsGroup": apSecurityIPsecTunnelsObjectsGroup,
       "apSecurityIkeInterfaceObjectsGroup": apSecurityIkeInterfaceObjectsGroup,
       "apSecurityTacacsObjectsGroup": apSecurityTacacsObjectsGroup,
       "apSecurityCertObjectsGroup": apSecurityCertObjectsGroup,
       "apSecurityIkeInterfaceInfoObjectsGroup": apSecurityIkeInterfaceInfoObjectsGroup,
       "apSecurityNotificationsGroups": apSecurityNotificationsGroups,
       "apSecurityNotificationsGroup": apSecurityNotificationsGroup,
       "apSecurityIPsecTunnelsNotificationsGroup": apSecurityIPsecTunnelsNotificationsGroup,
       "apSecurityDDosNotificationsGroup": apSecurityDDosNotificationsGroup,
       "apSecurityOCSRNotificationsGroup": apSecurityOCSRNotificationsGroup,
       "apSecurityCrlNotificationsGroup": apSecurityCrlNotificationsGroup,
       "apSecurityCRLRetrievalNotificationsGroup": apSecurityCRLRetrievalNotificationsGroup,
       "apSecurityCertNotificationsGroup": apSecurityCertNotificationsGroup,
       "apSecurityGTPNotificationsGroup": apSecurityGTPNotificationsGroup,
       "apSecurityNotificationsInetGroup": apSecurityNotificationsInetGroup,
       "apSecurityDDosNotificationsInetGroup": apSecurityDDosNotificationsInetGroup}
)
