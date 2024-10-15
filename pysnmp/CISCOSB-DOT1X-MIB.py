# SNMP MIB module (CISCOSB-DOT1X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-DOT1X-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:14 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(PaeControlledPortStatus,
 dot1xAuthSessionStatsEntry,
 dot1xPaePortNumber) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "PaeControlledPortStatus",
    "dot1xAuthSessionStatsEntry",
    "dot1xPaePortNumber")

(PortList,
 VlanIndex,
 dot1qFdbId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qFdbId")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

rldot1x = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95)
)
rldot1x.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rldot1xMibVersion_Type = Integer32
_Rldot1xMibVersion_Object = MibScalar
rldot1xMibVersion = _Rldot1xMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 1),
    _Rldot1xMibVersion_Type()
)
rldot1xMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xMibVersion.setStatus("current")
_Rldot1xExtAuthSessionStatsTable_Object = MibTable
rldot1xExtAuthSessionStatsTable = _Rldot1xExtAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 2)
)
if mibBuilder.loadTexts:
    rldot1xExtAuthSessionStatsTable.setStatus("current")
_Rldot1xExtAuthSessionStatsEntry_Object = MibTableRow
rldot1xExtAuthSessionStatsEntry = _Rldot1xExtAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 2, 1)
)
if mibBuilder.loadTexts:
    rldot1xExtAuthSessionStatsEntry.setStatus("current")


class _RlDot1xAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type rlDot1xAuthSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localAuthServer", 2),
          ("none", 3),
          ("remoteAuthServer", 1))
    )


_RlDot1xAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_RlDot1xAuthSessionAuthenticMethod_Object = MibTableColumn
rlDot1xAuthSessionAuthenticMethod = _RlDot1xAuthSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 2, 1, 1),
    _RlDot1xAuthSessionAuthenticMethod_Type()
)
rlDot1xAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot1xAuthSessionAuthenticMethod.setStatus("current")
_Rldot1xGuestVlanSupported_Type = TruthValue
_Rldot1xGuestVlanSupported_Object = MibScalar
rldot1xGuestVlanSupported = _Rldot1xGuestVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 3),
    _Rldot1xGuestVlanSupported_Type()
)
rldot1xGuestVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xGuestVlanSupported.setStatus("current")
_Rldot1xGuestVlanVID_Type = VlanIndex
_Rldot1xGuestVlanVID_Object = MibScalar
rldot1xGuestVlanVID = _Rldot1xGuestVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 4),
    _Rldot1xGuestVlanVID_Type()
)
rldot1xGuestVlanVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xGuestVlanVID.setStatus("current")
_Rldot1xGuestVlanPorts_Type = PortList
_Rldot1xGuestVlanPorts_Object = MibScalar
rldot1xGuestVlanPorts = _Rldot1xGuestVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 5),
    _Rldot1xGuestVlanPorts_Type()
)
rldot1xGuestVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xGuestVlanPorts.setStatus("current")
_Rldot1xUnAuthenticatedVlanSupported_Type = TruthValue
_Rldot1xUnAuthenticatedVlanSupported_Object = MibScalar
rldot1xUnAuthenticatedVlanSupported = _Rldot1xUnAuthenticatedVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 6),
    _Rldot1xUnAuthenticatedVlanSupported_Type()
)
rldot1xUnAuthenticatedVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xUnAuthenticatedVlanSupported.setStatus("current")
_Rldot1xUnAuthenticatedVlanTable_Object = MibTable
rldot1xUnAuthenticatedVlanTable = _Rldot1xUnAuthenticatedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 7)
)
if mibBuilder.loadTexts:
    rldot1xUnAuthenticatedVlanTable.setStatus("current")
_Rldot1xUnAuthenticatedVlanEntry_Object = MibTableRow
rldot1xUnAuthenticatedVlanEntry = _Rldot1xUnAuthenticatedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 7, 1)
)
rldot1xUnAuthenticatedVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
)
if mibBuilder.loadTexts:
    rldot1xUnAuthenticatedVlanEntry.setStatus("current")
_Rldot1xUnAuthenticatedVlanStatus_Type = RowStatus
_Rldot1xUnAuthenticatedVlanStatus_Object = MibTableColumn
rldot1xUnAuthenticatedVlanStatus = _Rldot1xUnAuthenticatedVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 7, 1, 1),
    _Rldot1xUnAuthenticatedVlanStatus_Type()
)
rldot1xUnAuthenticatedVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rldot1xUnAuthenticatedVlanStatus.setStatus("current")
_Rldot1xUserBasedVlanSupported_Type = TruthValue
_Rldot1xUserBasedVlanSupported_Object = MibScalar
rldot1xUserBasedVlanSupported = _Rldot1xUserBasedVlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 8),
    _Rldot1xUserBasedVlanSupported_Type()
)
rldot1xUserBasedVlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xUserBasedVlanSupported.setStatus("current")
_Rldot1xUserBasedVlanPorts_Type = PortList
_Rldot1xUserBasedVlanPorts_Object = MibScalar
rldot1xUserBasedVlanPorts = _Rldot1xUserBasedVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 9),
    _Rldot1xUserBasedVlanPorts_Type()
)
rldot1xUserBasedVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xUserBasedVlanPorts.setStatus("current")
_Rldot1xAuthenticationPortTable_Object = MibTable
rldot1xAuthenticationPortTable = _Rldot1xAuthenticationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10)
)
if mibBuilder.loadTexts:
    rldot1xAuthenticationPortTable.setStatus("current")
_Rldot1xAuthenticationPortEntry_Object = MibTableRow
rldot1xAuthenticationPortEntry = _Rldot1xAuthenticationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1)
)
rldot1xAuthenticationPortEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    rldot1xAuthenticationPortEntry.setStatus("current")


class _Rldot1xAuthenticationPortMethod_Type(Integer32):
    """Custom type rldot1xAuthenticationPortMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eapolOnly", 1),
          ("macAndEapol", 2),
          ("macOnly", 3),
          ("webAndEapol", 5),
          ("webAndMac", 6),
          ("webAndMacAndEapol", 7),
          ("webOnly", 4))
    )


_Rldot1xAuthenticationPortMethod_Type.__name__ = "Integer32"
_Rldot1xAuthenticationPortMethod_Object = MibTableColumn
rldot1xAuthenticationPortMethod = _Rldot1xAuthenticationPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1, 1),
    _Rldot1xAuthenticationPortMethod_Type()
)
rldot1xAuthenticationPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xAuthenticationPortMethod.setStatus("current")
_Rldot1xRadiusAttrVlanIdEnabled_Type = TruthValue
_Rldot1xRadiusAttrVlanIdEnabled_Object = MibTableColumn
rldot1xRadiusAttrVlanIdEnabled = _Rldot1xRadiusAttrVlanIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1, 2),
    _Rldot1xRadiusAttrVlanIdEnabled_Type()
)
rldot1xRadiusAttrVlanIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xRadiusAttrVlanIdEnabled.setStatus("current")
_Rldot1xRadiusAttAclNameEnabled_Type = TruthValue
_Rldot1xRadiusAttAclNameEnabled_Object = MibTableColumn
rldot1xRadiusAttAclNameEnabled = _Rldot1xRadiusAttAclNameEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1, 3),
    _Rldot1xRadiusAttAclNameEnabled_Type()
)
rldot1xRadiusAttAclNameEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xRadiusAttAclNameEnabled.setStatus("current")


class _Rldot1xTimeBasedName_Type(SnmpAdminString):
    """Custom type rldot1xTimeBasedName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Rldot1xTimeBasedName_Type.__name__ = "SnmpAdminString"
_Rldot1xTimeBasedName_Object = MibTableColumn
rldot1xTimeBasedName = _Rldot1xTimeBasedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1, 4),
    _Rldot1xTimeBasedName_Type()
)
rldot1xTimeBasedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xTimeBasedName.setStatus("current")
_Rldot1xTimeBasedActive_Type = TruthValue
_Rldot1xTimeBasedActive_Object = MibTableColumn
rldot1xTimeBasedActive = _Rldot1xTimeBasedActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1, 5),
    _Rldot1xTimeBasedActive_Type()
)
rldot1xTimeBasedActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xTimeBasedActive.setStatus("current")


class _Rldot1xRadiusAttrVlanIdentifier_Type(VlanIndex):
    """Custom type rldot1xRadiusAttrVlanIdentifier based on VlanIndex"""
    defaultValue = 0


_Rldot1xRadiusAttrVlanIdentifier_Object = MibTableColumn
rldot1xRadiusAttrVlanIdentifier = _Rldot1xRadiusAttrVlanIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1, 6),
    _Rldot1xRadiusAttrVlanIdentifier_Type()
)
rldot1xRadiusAttrVlanIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xRadiusAttrVlanIdentifier.setStatus("current")


class _Rldot1xMaxHosts_Type(Unsigned32):
    """Custom type rldot1xMaxHosts based on Unsigned32"""
    defaultValue = 0


_Rldot1xMaxHosts_Object = MibTableColumn
rldot1xMaxHosts = _Rldot1xMaxHosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1, 7),
    _Rldot1xMaxHosts_Type()
)
rldot1xMaxHosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xMaxHosts.setStatus("current")


class _Rldot1xMaxLoginAttempts_Type(Integer32):
    """Custom type rldot1xMaxLoginAttempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Rldot1xMaxLoginAttempts_Type.__name__ = "Integer32"
_Rldot1xMaxLoginAttempts_Object = MibTableColumn
rldot1xMaxLoginAttempts = _Rldot1xMaxLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1, 8),
    _Rldot1xMaxLoginAttempts_Type()
)
rldot1xMaxLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xMaxLoginAttempts.setStatus("current")


class _Rldot1xTimeoutSilencePeriod_Type(Integer32):
    """Custom type rldot1xTimeoutSilencePeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Rldot1xTimeoutSilencePeriod_Type.__name__ = "Integer32"
_Rldot1xTimeoutSilencePeriod_Object = MibTableColumn
rldot1xTimeoutSilencePeriod = _Rldot1xTimeoutSilencePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1, 9),
    _Rldot1xTimeoutSilencePeriod_Type()
)
rldot1xTimeoutSilencePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xTimeoutSilencePeriod.setStatus("current")
_Rldot1xNumOfAuthorizedHosts_Type = Integer32
_Rldot1xNumOfAuthorizedHosts_Object = MibTableColumn
rldot1xNumOfAuthorizedHosts = _Rldot1xNumOfAuthorizedHosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 10, 1, 10),
    _Rldot1xNumOfAuthorizedHosts_Type()
)
rldot1xNumOfAuthorizedHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xNumOfAuthorizedHosts.setStatus("current")
_Rldot1xAuthMultiStatsTable_Object = MibTable
rldot1xAuthMultiStatsTable = _Rldot1xAuthMultiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11)
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiStatsTable.setStatus("current")
_Rldot1xAuthMultiStatsEntry_Object = MibTableRow
rldot1xAuthMultiStatsEntry = _Rldot1xAuthMultiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1)
)
rldot1xAuthMultiStatsEntry.setIndexNames(
    (0, "CISCOSB-DOT1X-MIB", "rldot1xAuthMultiStatsPortNumber"),
    (0, "CISCOSB-DOT1X-MIB", "rldot1xAuthMultiStatsSourceMac"),
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiStatsEntry.setStatus("current")
_Rldot1xAuthMultiStatsPortNumber_Type = Integer32
_Rldot1xAuthMultiStatsPortNumber_Object = MibTableColumn
rldot1xAuthMultiStatsPortNumber = _Rldot1xAuthMultiStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 1),
    _Rldot1xAuthMultiStatsPortNumber_Type()
)
rldot1xAuthMultiStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiStatsPortNumber.setStatus("current")
_Rldot1xAuthMultiStatsSourceMac_Type = MacAddress
_Rldot1xAuthMultiStatsSourceMac_Object = MibTableColumn
rldot1xAuthMultiStatsSourceMac = _Rldot1xAuthMultiStatsSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 2),
    _Rldot1xAuthMultiStatsSourceMac_Type()
)
rldot1xAuthMultiStatsSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiStatsSourceMac.setStatus("current")
_Rldot1xAuthMultiEapolFramesRx_Type = Counter32
_Rldot1xAuthMultiEapolFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapolFramesRx = _Rldot1xAuthMultiEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 3),
    _Rldot1xAuthMultiEapolFramesRx_Type()
)
rldot1xAuthMultiEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolFramesRx.setStatus("current")
_Rldot1xAuthMultiEapolFramesTx_Type = Counter32
_Rldot1xAuthMultiEapolFramesTx_Object = MibTableColumn
rldot1xAuthMultiEapolFramesTx = _Rldot1xAuthMultiEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 4),
    _Rldot1xAuthMultiEapolFramesTx_Type()
)
rldot1xAuthMultiEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolFramesTx.setStatus("current")
_Rldot1xAuthMultiEapolStartFramesRx_Type = Counter32
_Rldot1xAuthMultiEapolStartFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapolStartFramesRx = _Rldot1xAuthMultiEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 5),
    _Rldot1xAuthMultiEapolStartFramesRx_Type()
)
rldot1xAuthMultiEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolStartFramesRx.setStatus("current")
_Rldot1xAuthMultiEapolLogoffFramesRx_Type = Counter32
_Rldot1xAuthMultiEapolLogoffFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapolLogoffFramesRx = _Rldot1xAuthMultiEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 6),
    _Rldot1xAuthMultiEapolLogoffFramesRx_Type()
)
rldot1xAuthMultiEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolLogoffFramesRx.setStatus("current")
_Rldot1xAuthMultiEapolRespIdFramesRx_Type = Counter32
_Rldot1xAuthMultiEapolRespIdFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapolRespIdFramesRx = _Rldot1xAuthMultiEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 7),
    _Rldot1xAuthMultiEapolRespIdFramesRx_Type()
)
rldot1xAuthMultiEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolRespIdFramesRx.setStatus("current")
_Rldot1xAuthMultiEapolRespFramesRx_Type = Counter32
_Rldot1xAuthMultiEapolRespFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapolRespFramesRx = _Rldot1xAuthMultiEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 8),
    _Rldot1xAuthMultiEapolRespFramesRx_Type()
)
rldot1xAuthMultiEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolRespFramesRx.setStatus("current")
_Rldot1xAuthMultiEapolReqIdFramesTx_Type = Counter32
_Rldot1xAuthMultiEapolReqIdFramesTx_Object = MibTableColumn
rldot1xAuthMultiEapolReqIdFramesTx = _Rldot1xAuthMultiEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 9),
    _Rldot1xAuthMultiEapolReqIdFramesTx_Type()
)
rldot1xAuthMultiEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolReqIdFramesTx.setStatus("current")
_Rldot1xAuthMultiEapolReqFramesTx_Type = Counter32
_Rldot1xAuthMultiEapolReqFramesTx_Object = MibTableColumn
rldot1xAuthMultiEapolReqFramesTx = _Rldot1xAuthMultiEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 10),
    _Rldot1xAuthMultiEapolReqFramesTx_Type()
)
rldot1xAuthMultiEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapolReqFramesTx.setStatus("current")
_Rldot1xAuthMultiInvalidEapolFramesRx_Type = Counter32
_Rldot1xAuthMultiInvalidEapolFramesRx_Object = MibTableColumn
rldot1xAuthMultiInvalidEapolFramesRx = _Rldot1xAuthMultiInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 11),
    _Rldot1xAuthMultiInvalidEapolFramesRx_Type()
)
rldot1xAuthMultiInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiInvalidEapolFramesRx.setStatus("current")
_Rldot1xAuthMultiEapLengthErrorFramesRx_Type = Counter32
_Rldot1xAuthMultiEapLengthErrorFramesRx_Object = MibTableColumn
rldot1xAuthMultiEapLengthErrorFramesRx = _Rldot1xAuthMultiEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 11, 1, 12),
    _Rldot1xAuthMultiEapLengthErrorFramesRx_Type()
)
rldot1xAuthMultiEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEapLengthErrorFramesRx.setStatus("current")
_Rldot1xAuthMultiDiagTable_Object = MibTable
rldot1xAuthMultiDiagTable = _Rldot1xAuthMultiDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12)
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiDiagTable.setStatus("current")
_Rldot1xAuthMultiDiagEntry_Object = MibTableRow
rldot1xAuthMultiDiagEntry = _Rldot1xAuthMultiDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1)
)
rldot1xAuthMultiDiagEntry.setIndexNames(
    (0, "CISCOSB-DOT1X-MIB", "rldot1xAuthMultiDiagPortNumber"),
    (0, "CISCOSB-DOT1X-MIB", "rldot1xAuthMultiDiagSourceMac"),
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiDiagEntry.setStatus("current")
_Rldot1xAuthMultiDiagPortNumber_Type = Integer32
_Rldot1xAuthMultiDiagPortNumber_Object = MibTableColumn
rldot1xAuthMultiDiagPortNumber = _Rldot1xAuthMultiDiagPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 1),
    _Rldot1xAuthMultiDiagPortNumber_Type()
)
rldot1xAuthMultiDiagPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiDiagPortNumber.setStatus("current")
_Rldot1xAuthMultiDiagSourceMac_Type = MacAddress
_Rldot1xAuthMultiDiagSourceMac_Object = MibTableColumn
rldot1xAuthMultiDiagSourceMac = _Rldot1xAuthMultiDiagSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 2),
    _Rldot1xAuthMultiDiagSourceMac_Type()
)
rldot1xAuthMultiDiagSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiDiagSourceMac.setStatus("current")
_Rldot1xAuthMultiEntersConnecting_Type = Counter32
_Rldot1xAuthMultiEntersConnecting_Object = MibTableColumn
rldot1xAuthMultiEntersConnecting = _Rldot1xAuthMultiEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 3),
    _Rldot1xAuthMultiEntersConnecting_Type()
)
rldot1xAuthMultiEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEntersConnecting.setStatus("current")
_Rldot1xAuthMultiEntersAuthenticating_Type = Counter32
_Rldot1xAuthMultiEntersAuthenticating_Object = MibTableColumn
rldot1xAuthMultiEntersAuthenticating = _Rldot1xAuthMultiEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 4),
    _Rldot1xAuthMultiEntersAuthenticating_Type()
)
rldot1xAuthMultiEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiEntersAuthenticating.setStatus("current")
_Rldot1xAuthMultiAuthSuccessWhileAuthenticating_Type = Counter32
_Rldot1xAuthMultiAuthSuccessWhileAuthenticating_Object = MibTableColumn
rldot1xAuthMultiAuthSuccessWhileAuthenticating = _Rldot1xAuthMultiAuthSuccessWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 5),
    _Rldot1xAuthMultiAuthSuccessWhileAuthenticating_Type()
)
rldot1xAuthMultiAuthSuccessWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthSuccessWhileAuthenticating.setStatus("current")
_Rldot1xAuthMultiAuthFailWhileAuthenticating_Type = Counter32
_Rldot1xAuthMultiAuthFailWhileAuthenticating_Object = MibTableColumn
rldot1xAuthMultiAuthFailWhileAuthenticating = _Rldot1xAuthMultiAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 6),
    _Rldot1xAuthMultiAuthFailWhileAuthenticating_Type()
)
rldot1xAuthMultiAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthFailWhileAuthenticating.setStatus("current")
_Rldot1xAuthMultiAuthReauthsWhileAuthenticating_Type = Counter32
_Rldot1xAuthMultiAuthReauthsWhileAuthenticating_Object = MibTableColumn
rldot1xAuthMultiAuthReauthsWhileAuthenticating = _Rldot1xAuthMultiAuthReauthsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 7),
    _Rldot1xAuthMultiAuthReauthsWhileAuthenticating_Type()
)
rldot1xAuthMultiAuthReauthsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthReauthsWhileAuthenticating.setStatus("current")
_Rldot1xAuthMultiAuthEapStartsWhileAuthenticating_Type = Counter32
_Rldot1xAuthMultiAuthEapStartsWhileAuthenticating_Object = MibTableColumn
rldot1xAuthMultiAuthEapStartsWhileAuthenticating = _Rldot1xAuthMultiAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 8),
    _Rldot1xAuthMultiAuthEapStartsWhileAuthenticating_Type()
)
rldot1xAuthMultiAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthEapStartsWhileAuthenticating.setStatus("current")
_Rldot1xAuthMultiAuthReauthsWhileAuthenticated_Type = Counter32
_Rldot1xAuthMultiAuthReauthsWhileAuthenticated_Object = MibTableColumn
rldot1xAuthMultiAuthReauthsWhileAuthenticated = _Rldot1xAuthMultiAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 9),
    _Rldot1xAuthMultiAuthReauthsWhileAuthenticated_Type()
)
rldot1xAuthMultiAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthReauthsWhileAuthenticated.setStatus("current")
_Rldot1xAuthMultiAuthEapStartsWhileAuthenticated_Type = Counter32
_Rldot1xAuthMultiAuthEapStartsWhileAuthenticated_Object = MibTableColumn
rldot1xAuthMultiAuthEapStartsWhileAuthenticated = _Rldot1xAuthMultiAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 10),
    _Rldot1xAuthMultiAuthEapStartsWhileAuthenticated_Type()
)
rldot1xAuthMultiAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiAuthEapStartsWhileAuthenticated.setStatus("current")
_Rldot1xAuthMultiBackendResponses_Type = Counter32
_Rldot1xAuthMultiBackendResponses_Object = MibTableColumn
rldot1xAuthMultiBackendResponses = _Rldot1xAuthMultiBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 11),
    _Rldot1xAuthMultiBackendResponses_Type()
)
rldot1xAuthMultiBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendResponses.setStatus("current")
_Rldot1xAuthMultiBackendAccessChallenges_Type = Counter32
_Rldot1xAuthMultiBackendAccessChallenges_Object = MibTableColumn
rldot1xAuthMultiBackendAccessChallenges = _Rldot1xAuthMultiBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 12),
    _Rldot1xAuthMultiBackendAccessChallenges_Type()
)
rldot1xAuthMultiBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendAccessChallenges.setStatus("current")
_Rldot1xAuthMultiBackendOtherRequestsToSupplicant_Type = Counter32
_Rldot1xAuthMultiBackendOtherRequestsToSupplicant_Object = MibTableColumn
rldot1xAuthMultiBackendOtherRequestsToSupplicant = _Rldot1xAuthMultiBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 13),
    _Rldot1xAuthMultiBackendOtherRequestsToSupplicant_Type()
)
rldot1xAuthMultiBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendOtherRequestsToSupplicant.setStatus("current")
_Rldot1xAuthMultiBackendNonNakResponsesFromSupplicant_Type = Counter32
_Rldot1xAuthMultiBackendNonNakResponsesFromSupplicant_Object = MibTableColumn
rldot1xAuthMultiBackendNonNakResponsesFromSupplicant = _Rldot1xAuthMultiBackendNonNakResponsesFromSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 14),
    _Rldot1xAuthMultiBackendNonNakResponsesFromSupplicant_Type()
)
rldot1xAuthMultiBackendNonNakResponsesFromSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendNonNakResponsesFromSupplicant.setStatus("current")
_Rldot1xAuthMultiBackendAuthSuccesses_Type = Counter32
_Rldot1xAuthMultiBackendAuthSuccesses_Object = MibTableColumn
rldot1xAuthMultiBackendAuthSuccesses = _Rldot1xAuthMultiBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 12, 1, 15),
    _Rldot1xAuthMultiBackendAuthSuccesses_Type()
)
rldot1xAuthMultiBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendAuthSuccesses.setStatus("current")
_Rldot1xAuthMultiSessionStatsTable_Object = MibTable
rldot1xAuthMultiSessionStatsTable = _Rldot1xAuthMultiSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13)
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionStatsTable.setStatus("current")
_Rldot1xAuthMultiSessionStatsEntry_Object = MibTableRow
rldot1xAuthMultiSessionStatsEntry = _Rldot1xAuthMultiSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1)
)
rldot1xAuthMultiSessionStatsEntry.setIndexNames(
    (0, "CISCOSB-DOT1X-MIB", "rldot1xAuthMultiSessionStatsPortNumber"),
    (0, "CISCOSB-DOT1X-MIB", "rldot1xAuthMultiSessionStatsSourceMac"),
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionStatsEntry.setStatus("current")
_Rldot1xAuthMultiSessionStatsPortNumber_Type = Integer32
_Rldot1xAuthMultiSessionStatsPortNumber_Object = MibTableColumn
rldot1xAuthMultiSessionStatsPortNumber = _Rldot1xAuthMultiSessionStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 1),
    _Rldot1xAuthMultiSessionStatsPortNumber_Type()
)
rldot1xAuthMultiSessionStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionStatsPortNumber.setStatus("current")
_Rldot1xAuthMultiSessionStatsSourceMac_Type = MacAddress
_Rldot1xAuthMultiSessionStatsSourceMac_Object = MibTableColumn
rldot1xAuthMultiSessionStatsSourceMac = _Rldot1xAuthMultiSessionStatsSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 2),
    _Rldot1xAuthMultiSessionStatsSourceMac_Type()
)
rldot1xAuthMultiSessionStatsSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionStatsSourceMac.setStatus("current")
_Rldot1xAuthMultiSessionOctetsRx_Type = Counter64
_Rldot1xAuthMultiSessionOctetsRx_Object = MibTableColumn
rldot1xAuthMultiSessionOctetsRx = _Rldot1xAuthMultiSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 3),
    _Rldot1xAuthMultiSessionOctetsRx_Type()
)
rldot1xAuthMultiSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionOctetsRx.setStatus("current")
_Rldot1xAuthMultiSessionOctetsTx_Type = Counter64
_Rldot1xAuthMultiSessionOctetsTx_Object = MibTableColumn
rldot1xAuthMultiSessionOctetsTx = _Rldot1xAuthMultiSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 4),
    _Rldot1xAuthMultiSessionOctetsTx_Type()
)
rldot1xAuthMultiSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionOctetsTx.setStatus("current")
_Rldot1xAuthMultiSessionFramesRx_Type = Counter32
_Rldot1xAuthMultiSessionFramesRx_Object = MibTableColumn
rldot1xAuthMultiSessionFramesRx = _Rldot1xAuthMultiSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 5),
    _Rldot1xAuthMultiSessionFramesRx_Type()
)
rldot1xAuthMultiSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionFramesRx.setStatus("current")
_Rldot1xAuthMultiSessionFramesTx_Type = Counter32
_Rldot1xAuthMultiSessionFramesTx_Object = MibTableColumn
rldot1xAuthMultiSessionFramesTx = _Rldot1xAuthMultiSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 6),
    _Rldot1xAuthMultiSessionFramesTx_Type()
)
rldot1xAuthMultiSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionFramesTx.setStatus("current")
_Rldot1xAuthMultiSessionId_Type = SnmpAdminString
_Rldot1xAuthMultiSessionId_Object = MibTableColumn
rldot1xAuthMultiSessionId = _Rldot1xAuthMultiSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 7),
    _Rldot1xAuthMultiSessionId_Type()
)
rldot1xAuthMultiSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionId.setStatus("current")
_Rldot1xAuthMultiSessionTime_Type = TimeTicks
_Rldot1xAuthMultiSessionTime_Object = MibTableColumn
rldot1xAuthMultiSessionTime = _Rldot1xAuthMultiSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 8),
    _Rldot1xAuthMultiSessionTime_Type()
)
rldot1xAuthMultiSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionTime.setStatus("current")
_Rldot1xAuthMultiSessionUserName_Type = SnmpAdminString
_Rldot1xAuthMultiSessionUserName_Object = MibTableColumn
rldot1xAuthMultiSessionUserName = _Rldot1xAuthMultiSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 9),
    _Rldot1xAuthMultiSessionUserName_Type()
)
rldot1xAuthMultiSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionUserName.setStatus("current")
_Rldot1xAuthMultiSessionRadiusAttrVlan_Type = Integer32
_Rldot1xAuthMultiSessionRadiusAttrVlan_Object = MibTableColumn
rldot1xAuthMultiSessionRadiusAttrVlan = _Rldot1xAuthMultiSessionRadiusAttrVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 10),
    _Rldot1xAuthMultiSessionRadiusAttrVlan_Type()
)
rldot1xAuthMultiSessionRadiusAttrVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionRadiusAttrVlan.setStatus("current")
_Rldot1xAuthMultiSessionRadiusAttrFilterId_Type = SnmpAdminString
_Rldot1xAuthMultiSessionRadiusAttrFilterId_Object = MibTableColumn
rldot1xAuthMultiSessionRadiusAttrFilterId = _Rldot1xAuthMultiSessionRadiusAttrFilterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 11),
    _Rldot1xAuthMultiSessionRadiusAttrFilterId_Type()
)
rldot1xAuthMultiSessionRadiusAttrFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionRadiusAttrFilterId.setStatus("current")
_Rldot1xAuthMultiSessionRadiusAttrSecondFilterId_Type = SnmpAdminString
_Rldot1xAuthMultiSessionRadiusAttrSecondFilterId_Object = MibTableColumn
rldot1xAuthMultiSessionRadiusAttrSecondFilterId = _Rldot1xAuthMultiSessionRadiusAttrSecondFilterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 12),
    _Rldot1xAuthMultiSessionRadiusAttrSecondFilterId_Type()
)
rldot1xAuthMultiSessionRadiusAttrSecondFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSessionRadiusAttrSecondFilterId.setStatus("current")


class _RlDot1xAuthMultiSessionMonitorResultsReason_Type(Integer32):
    """Custom type rlDot1xAuthMultiSessionMonitorResultsReason based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("aclDel", 8),
          ("aclEgress", 22),
          ("aclNotExst", 1),
          ("aclOvrfl", 2),
          ("authErr", 3),
          ("fltrErr", 4),
          ("frsMthDeny", 18),
          ("ipv6WithMac", 5),
          ("ipv6WithNotIp", 6),
          ("maxHosts", 23),
          ("noActivity", 24),
          ("notRejected", 0),
          ("polBasicMode", 7),
          ("polDel", 9),
          ("radApierr", 19),
          ("radInvlres", 20),
          ("radNoresp", 21),
          ("vlanDfly", 10),
          ("vlanDynam", 11),
          ("vlanGuest", 12),
          ("vlanNoInMsg", 13),
          ("vlanNotExst", 14),
          ("vlanOvfl", 15),
          ("vlanUnauth", 17),
          ("vlanVoice", 16))
    )


_RlDot1xAuthMultiSessionMonitorResultsReason_Type.__name__ = "Integer32"
_RlDot1xAuthMultiSessionMonitorResultsReason_Object = MibTableColumn
rlDot1xAuthMultiSessionMonitorResultsReason = _RlDot1xAuthMultiSessionMonitorResultsReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 13),
    _RlDot1xAuthMultiSessionMonitorResultsReason_Type()
)
rlDot1xAuthMultiSessionMonitorResultsReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot1xAuthMultiSessionMonitorResultsReason.setStatus("current")


class _RlDot1xAuthMultiSessionMethodType_Type(Integer32):
    """Custom type rlDot1xAuthMultiSessionMethodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eapol", 1),
          ("mac", 2),
          ("web", 3))
    )


_RlDot1xAuthMultiSessionMethodType_Type.__name__ = "Integer32"
_RlDot1xAuthMultiSessionMethodType_Object = MibTableColumn
rlDot1xAuthMultiSessionMethodType = _RlDot1xAuthMultiSessionMethodType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 13, 1, 14),
    _RlDot1xAuthMultiSessionMethodType_Type()
)
rlDot1xAuthMultiSessionMethodType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDot1xAuthMultiSessionMethodType.setStatus("current")
_Rldot1xAuthMultiConfigTable_Object = MibTable
rldot1xAuthMultiConfigTable = _Rldot1xAuthMultiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 14)
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiConfigTable.setStatus("current")
_Rldot1xAuthMultiConfigEntry_Object = MibTableRow
rldot1xAuthMultiConfigEntry = _Rldot1xAuthMultiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 14, 1)
)
rldot1xAuthMultiConfigEntry.setIndexNames(
    (0, "CISCOSB-DOT1X-MIB", "rldot1xAuthMultiPortNumber"),
    (0, "CISCOSB-DOT1X-MIB", "rldot1xAuthMultiSourceMac"),
)
if mibBuilder.loadTexts:
    rldot1xAuthMultiConfigEntry.setStatus("current")
_Rldot1xAuthMultiPortNumber_Type = Integer32
_Rldot1xAuthMultiPortNumber_Object = MibTableColumn
rldot1xAuthMultiPortNumber = _Rldot1xAuthMultiPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 14, 1, 1),
    _Rldot1xAuthMultiPortNumber_Type()
)
rldot1xAuthMultiPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiPortNumber.setStatus("current")
_Rldot1xAuthMultiSourceMac_Type = MacAddress
_Rldot1xAuthMultiSourceMac_Object = MibTableColumn
rldot1xAuthMultiSourceMac = _Rldot1xAuthMultiSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 14, 1, 2),
    _Rldot1xAuthMultiSourceMac_Type()
)
rldot1xAuthMultiSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiSourceMac.setStatus("current")


class _Rldot1xAuthMultiPaeState_Type(Integer32):
    """Custom type rldot1xAuthMultiPaeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("forceAuth", 8),
          ("forceUnauth", 9),
          ("held", 7),
          ("initialize", 1))
    )


_Rldot1xAuthMultiPaeState_Type.__name__ = "Integer32"
_Rldot1xAuthMultiPaeState_Object = MibTableColumn
rldot1xAuthMultiPaeState = _Rldot1xAuthMultiPaeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 14, 1, 3),
    _Rldot1xAuthMultiPaeState_Type()
)
rldot1xAuthMultiPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiPaeState.setStatus("current")


class _Rldot1xAuthMultiBackendAuthState_Type(Integer32):
    """Custom type rldot1xAuthMultiBackendAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fail", 4),
          ("idle", 6),
          ("initialize", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_Rldot1xAuthMultiBackendAuthState_Type.__name__ = "Integer32"
_Rldot1xAuthMultiBackendAuthState_Object = MibTableColumn
rldot1xAuthMultiBackendAuthState = _Rldot1xAuthMultiBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 14, 1, 4),
    _Rldot1xAuthMultiBackendAuthState_Type()
)
rldot1xAuthMultiBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiBackendAuthState.setStatus("current")
_Rldot1xAuthMultiControlledPortStatus_Type = PaeControlledPortStatus
_Rldot1xAuthMultiControlledPortStatus_Object = MibTableColumn
rldot1xAuthMultiControlledPortStatus = _Rldot1xAuthMultiControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 14, 1, 5),
    _Rldot1xAuthMultiControlledPortStatus_Type()
)
rldot1xAuthMultiControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xAuthMultiControlledPortStatus.setStatus("current")
_Rldot1xBpduFilteringEnabled_Type = TruthValue
_Rldot1xBpduFilteringEnabled_Object = MibScalar
rldot1xBpduFilteringEnabled = _Rldot1xBpduFilteringEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 15),
    _Rldot1xBpduFilteringEnabled_Type()
)
rldot1xBpduFilteringEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xBpduFilteringEnabled.setStatus("current")
_Rldot1xRadiusAttributesErrorsAclReject_Type = TruthValue
_Rldot1xRadiusAttributesErrorsAclReject_Object = MibScalar
rldot1xRadiusAttributesErrorsAclReject = _Rldot1xRadiusAttributesErrorsAclReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 18),
    _Rldot1xRadiusAttributesErrorsAclReject_Type()
)
rldot1xRadiusAttributesErrorsAclReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xRadiusAttributesErrorsAclReject.setStatus("current")


class _Rldot1xGuestVlanTimeInterval_Type(Integer32):
    """Custom type rldot1xGuestVlanTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_Rldot1xGuestVlanTimeInterval_Type.__name__ = "Integer32"
_Rldot1xGuestVlanTimeInterval_Object = MibScalar
rldot1xGuestVlanTimeInterval = _Rldot1xGuestVlanTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 19),
    _Rldot1xGuestVlanTimeInterval_Type()
)
rldot1xGuestVlanTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xGuestVlanTimeInterval.setStatus("current")
_Rldot1xMacAuthSuccessTrapEnabled_Type = TruthValue
_Rldot1xMacAuthSuccessTrapEnabled_Object = MibScalar
rldot1xMacAuthSuccessTrapEnabled = _Rldot1xMacAuthSuccessTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 20),
    _Rldot1xMacAuthSuccessTrapEnabled_Type()
)
rldot1xMacAuthSuccessTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xMacAuthSuccessTrapEnabled.setStatus("current")
_Rldot1xMacAuthFailureTrapEnabled_Type = TruthValue
_Rldot1xMacAuthFailureTrapEnabled_Object = MibScalar
rldot1xMacAuthFailureTrapEnabled = _Rldot1xMacAuthFailureTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 21),
    _Rldot1xMacAuthFailureTrapEnabled_Type()
)
rldot1xMacAuthFailureTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xMacAuthFailureTrapEnabled.setStatus("current")
_Rldot1xLegacyPortTable_Object = MibTable
rldot1xLegacyPortTable = _Rldot1xLegacyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 22)
)
if mibBuilder.loadTexts:
    rldot1xLegacyPortTable.setStatus("current")
_Rldot1xLegacyPortEntry_Object = MibTableRow
rldot1xLegacyPortEntry = _Rldot1xLegacyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 22, 1)
)
rldot1xLegacyPortEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    rldot1xLegacyPortEntry.setStatus("current")
_Rldot1xLegacyPortModeEnabled_Type = TruthValue
_Rldot1xLegacyPortModeEnabled_Object = MibTableColumn
rldot1xLegacyPortModeEnabled = _Rldot1xLegacyPortModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 22, 1, 1),
    _Rldot1xLegacyPortModeEnabled_Type()
)
rldot1xLegacyPortModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xLegacyPortModeEnabled.setStatus("current")


class _Rldot1xSystemAuthControlMonitorVlan_Type(Integer32):
    """Custom type rldot1xSystemAuthControlMonitorVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Rldot1xSystemAuthControlMonitorVlan_Type.__name__ = "Integer32"
_Rldot1xSystemAuthControlMonitorVlan_Object = MibScalar
rldot1xSystemAuthControlMonitorVlan = _Rldot1xSystemAuthControlMonitorVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 23),
    _Rldot1xSystemAuthControlMonitorVlan_Type()
)
rldot1xSystemAuthControlMonitorVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xSystemAuthControlMonitorVlan.setStatus("current")
_Rldot1xClearPortMibCounters_Type = PortList
_Rldot1xClearPortMibCounters_Object = MibScalar
rldot1xClearPortMibCounters = _Rldot1xClearPortMibCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 24),
    _Rldot1xClearPortMibCounters_Type()
)
rldot1xClearPortMibCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xClearPortMibCounters.setStatus("current")
_Rldot1xWebQuietFailureTrapEnabled_Type = TruthValue
_Rldot1xWebQuietFailureTrapEnabled_Object = MibScalar
rldot1xWebQuietFailureTrapEnabled = _Rldot1xWebQuietFailureTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 25),
    _Rldot1xWebQuietFailureTrapEnabled_Type()
)
rldot1xWebQuietFailureTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xWebQuietFailureTrapEnabled.setStatus("current")


class _Rldot1xMacWebAuthSuccessTrapEnabled_Type(Integer32):
    """Custom type rldot1xMacWebAuthSuccessTrapEnabled based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("eapolOnly", 1),
          ("macAndEapol", 2),
          ("macOnly", 3),
          ("none", 0),
          ("webAndEapol", 5),
          ("webAndMac", 6),
          ("webAndMacAndEapol", 7),
          ("webOnly", 4))
    )


_Rldot1xMacWebAuthSuccessTrapEnabled_Type.__name__ = "Integer32"
_Rldot1xMacWebAuthSuccessTrapEnabled_Object = MibScalar
rldot1xMacWebAuthSuccessTrapEnabled = _Rldot1xMacWebAuthSuccessTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 26),
    _Rldot1xMacWebAuthSuccessTrapEnabled_Type()
)
rldot1xMacWebAuthSuccessTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xMacWebAuthSuccessTrapEnabled.setStatus("current")


class _Rldot1xMacWebAuthFailureTrapEnabled_Type(Integer32):
    """Custom type rldot1xMacWebAuthFailureTrapEnabled based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("eapolOnly", 1),
          ("macAndEapol", 2),
          ("macOnly", 3),
          ("none", 0),
          ("webAndEapol", 5),
          ("webAndMac", 6),
          ("webAndMacAndEapol", 7),
          ("webOnly", 4))
    )


_Rldot1xMacWebAuthFailureTrapEnabled_Type.__name__ = "Integer32"
_Rldot1xMacWebAuthFailureTrapEnabled_Object = MibScalar
rldot1xMacWebAuthFailureTrapEnabled = _Rldot1xMacWebAuthFailureTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 27),
    _Rldot1xMacWebAuthFailureTrapEnabled_Type()
)
rldot1xMacWebAuthFailureTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xMacWebAuthFailureTrapEnabled.setStatus("current")
_Rldot1xLockedCientsTable_Object = MibTable
rldot1xLockedCientsTable = _Rldot1xLockedCientsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 28)
)
if mibBuilder.loadTexts:
    rldot1xLockedCientsTable.setStatus("current")
_Rldot1xLockedCientsEntry_Object = MibTableRow
rldot1xLockedCientsEntry = _Rldot1xLockedCientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 28, 1)
)
rldot1xLockedCientsEntry.setIndexNames(
    (0, "CISCOSB-DOT1X-MIB", "rldot1xLockedCientsPortNumber"),
    (0, "CISCOSB-DOT1X-MIB", "rldot1xLockedCientsSourceMac"),
)
if mibBuilder.loadTexts:
    rldot1xLockedCientsEntry.setStatus("current")
_Rldot1xLockedCientsPortNumber_Type = Integer32
_Rldot1xLockedCientsPortNumber_Object = MibTableColumn
rldot1xLockedCientsPortNumber = _Rldot1xLockedCientsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 28, 1, 1),
    _Rldot1xLockedCientsPortNumber_Type()
)
rldot1xLockedCientsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xLockedCientsPortNumber.setStatus("current")
_Rldot1xLockedCientsSourceMac_Type = MacAddress
_Rldot1xLockedCientsSourceMac_Object = MibTableColumn
rldot1xLockedCientsSourceMac = _Rldot1xLockedCientsSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 28, 1, 2),
    _Rldot1xLockedCientsSourceMac_Type()
)
rldot1xLockedCientsSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xLockedCientsSourceMac.setStatus("current")
_Rldot1xLockedCientsRemainedTime_Type = Integer32
_Rldot1xLockedCientsRemainedTime_Object = MibTableColumn
rldot1xLockedCientsRemainedTime = _Rldot1xLockedCientsRemainedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 28, 1, 3),
    _Rldot1xLockedCientsRemainedTime_Type()
)
rldot1xLockedCientsRemainedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rldot1xLockedCientsRemainedTime.setStatus("current")
_Rldot1xLockedCientsRowStatus_Type = RowStatus
_Rldot1xLockedCientsRowStatus_Object = MibTableColumn
rldot1xLockedCientsRowStatus = _Rldot1xLockedCientsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95, 28, 1, 4),
    _Rldot1xLockedCientsRowStatus_Type()
)
rldot1xLockedCientsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rldot1xLockedCientsRowStatus.setStatus("current")
dot1xAuthSessionStatsEntry.registerAugmentions(
    ("CISCOSB-DOT1X-MIB",
     "rldot1xExtAuthSessionStatsEntry")
)
rldot1xExtAuthSessionStatsEntry.setIndexNames(*dot1xAuthSessionStatsEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-DOT1X-MIB",
    **{"rldot1x": rldot1x,
       "rldot1xMibVersion": rldot1xMibVersion,
       "rldot1xExtAuthSessionStatsTable": rldot1xExtAuthSessionStatsTable,
       "rldot1xExtAuthSessionStatsEntry": rldot1xExtAuthSessionStatsEntry,
       "rlDot1xAuthSessionAuthenticMethod": rlDot1xAuthSessionAuthenticMethod,
       "rldot1xGuestVlanSupported": rldot1xGuestVlanSupported,
       "rldot1xGuestVlanVID": rldot1xGuestVlanVID,
       "rldot1xGuestVlanPorts": rldot1xGuestVlanPorts,
       "rldot1xUnAuthenticatedVlanSupported": rldot1xUnAuthenticatedVlanSupported,
       "rldot1xUnAuthenticatedVlanTable": rldot1xUnAuthenticatedVlanTable,
       "rldot1xUnAuthenticatedVlanEntry": rldot1xUnAuthenticatedVlanEntry,
       "rldot1xUnAuthenticatedVlanStatus": rldot1xUnAuthenticatedVlanStatus,
       "rldot1xUserBasedVlanSupported": rldot1xUserBasedVlanSupported,
       "rldot1xUserBasedVlanPorts": rldot1xUserBasedVlanPorts,
       "rldot1xAuthenticationPortTable": rldot1xAuthenticationPortTable,
       "rldot1xAuthenticationPortEntry": rldot1xAuthenticationPortEntry,
       "rldot1xAuthenticationPortMethod": rldot1xAuthenticationPortMethod,
       "rldot1xRadiusAttrVlanIdEnabled": rldot1xRadiusAttrVlanIdEnabled,
       "rldot1xRadiusAttAclNameEnabled": rldot1xRadiusAttAclNameEnabled,
       "rldot1xTimeBasedName": rldot1xTimeBasedName,
       "rldot1xTimeBasedActive": rldot1xTimeBasedActive,
       "rldot1xRadiusAttrVlanIdentifier": rldot1xRadiusAttrVlanIdentifier,
       "rldot1xMaxHosts": rldot1xMaxHosts,
       "rldot1xMaxLoginAttempts": rldot1xMaxLoginAttempts,
       "rldot1xTimeoutSilencePeriod": rldot1xTimeoutSilencePeriod,
       "rldot1xNumOfAuthorizedHosts": rldot1xNumOfAuthorizedHosts,
       "rldot1xAuthMultiStatsTable": rldot1xAuthMultiStatsTable,
       "rldot1xAuthMultiStatsEntry": rldot1xAuthMultiStatsEntry,
       "rldot1xAuthMultiStatsPortNumber": rldot1xAuthMultiStatsPortNumber,
       "rldot1xAuthMultiStatsSourceMac": rldot1xAuthMultiStatsSourceMac,
       "rldot1xAuthMultiEapolFramesRx": rldot1xAuthMultiEapolFramesRx,
       "rldot1xAuthMultiEapolFramesTx": rldot1xAuthMultiEapolFramesTx,
       "rldot1xAuthMultiEapolStartFramesRx": rldot1xAuthMultiEapolStartFramesRx,
       "rldot1xAuthMultiEapolLogoffFramesRx": rldot1xAuthMultiEapolLogoffFramesRx,
       "rldot1xAuthMultiEapolRespIdFramesRx": rldot1xAuthMultiEapolRespIdFramesRx,
       "rldot1xAuthMultiEapolRespFramesRx": rldot1xAuthMultiEapolRespFramesRx,
       "rldot1xAuthMultiEapolReqIdFramesTx": rldot1xAuthMultiEapolReqIdFramesTx,
       "rldot1xAuthMultiEapolReqFramesTx": rldot1xAuthMultiEapolReqFramesTx,
       "rldot1xAuthMultiInvalidEapolFramesRx": rldot1xAuthMultiInvalidEapolFramesRx,
       "rldot1xAuthMultiEapLengthErrorFramesRx": rldot1xAuthMultiEapLengthErrorFramesRx,
       "rldot1xAuthMultiDiagTable": rldot1xAuthMultiDiagTable,
       "rldot1xAuthMultiDiagEntry": rldot1xAuthMultiDiagEntry,
       "rldot1xAuthMultiDiagPortNumber": rldot1xAuthMultiDiagPortNumber,
       "rldot1xAuthMultiDiagSourceMac": rldot1xAuthMultiDiagSourceMac,
       "rldot1xAuthMultiEntersConnecting": rldot1xAuthMultiEntersConnecting,
       "rldot1xAuthMultiEntersAuthenticating": rldot1xAuthMultiEntersAuthenticating,
       "rldot1xAuthMultiAuthSuccessWhileAuthenticating": rldot1xAuthMultiAuthSuccessWhileAuthenticating,
       "rldot1xAuthMultiAuthFailWhileAuthenticating": rldot1xAuthMultiAuthFailWhileAuthenticating,
       "rldot1xAuthMultiAuthReauthsWhileAuthenticating": rldot1xAuthMultiAuthReauthsWhileAuthenticating,
       "rldot1xAuthMultiAuthEapStartsWhileAuthenticating": rldot1xAuthMultiAuthEapStartsWhileAuthenticating,
       "rldot1xAuthMultiAuthReauthsWhileAuthenticated": rldot1xAuthMultiAuthReauthsWhileAuthenticated,
       "rldot1xAuthMultiAuthEapStartsWhileAuthenticated": rldot1xAuthMultiAuthEapStartsWhileAuthenticated,
       "rldot1xAuthMultiBackendResponses": rldot1xAuthMultiBackendResponses,
       "rldot1xAuthMultiBackendAccessChallenges": rldot1xAuthMultiBackendAccessChallenges,
       "rldot1xAuthMultiBackendOtherRequestsToSupplicant": rldot1xAuthMultiBackendOtherRequestsToSupplicant,
       "rldot1xAuthMultiBackendNonNakResponsesFromSupplicant": rldot1xAuthMultiBackendNonNakResponsesFromSupplicant,
       "rldot1xAuthMultiBackendAuthSuccesses": rldot1xAuthMultiBackendAuthSuccesses,
       "rldot1xAuthMultiSessionStatsTable": rldot1xAuthMultiSessionStatsTable,
       "rldot1xAuthMultiSessionStatsEntry": rldot1xAuthMultiSessionStatsEntry,
       "rldot1xAuthMultiSessionStatsPortNumber": rldot1xAuthMultiSessionStatsPortNumber,
       "rldot1xAuthMultiSessionStatsSourceMac": rldot1xAuthMultiSessionStatsSourceMac,
       "rldot1xAuthMultiSessionOctetsRx": rldot1xAuthMultiSessionOctetsRx,
       "rldot1xAuthMultiSessionOctetsTx": rldot1xAuthMultiSessionOctetsTx,
       "rldot1xAuthMultiSessionFramesRx": rldot1xAuthMultiSessionFramesRx,
       "rldot1xAuthMultiSessionFramesTx": rldot1xAuthMultiSessionFramesTx,
       "rldot1xAuthMultiSessionId": rldot1xAuthMultiSessionId,
       "rldot1xAuthMultiSessionTime": rldot1xAuthMultiSessionTime,
       "rldot1xAuthMultiSessionUserName": rldot1xAuthMultiSessionUserName,
       "rldot1xAuthMultiSessionRadiusAttrVlan": rldot1xAuthMultiSessionRadiusAttrVlan,
       "rldot1xAuthMultiSessionRadiusAttrFilterId": rldot1xAuthMultiSessionRadiusAttrFilterId,
       "rldot1xAuthMultiSessionRadiusAttrSecondFilterId": rldot1xAuthMultiSessionRadiusAttrSecondFilterId,
       "rlDot1xAuthMultiSessionMonitorResultsReason": rlDot1xAuthMultiSessionMonitorResultsReason,
       "rlDot1xAuthMultiSessionMethodType": rlDot1xAuthMultiSessionMethodType,
       "rldot1xAuthMultiConfigTable": rldot1xAuthMultiConfigTable,
       "rldot1xAuthMultiConfigEntry": rldot1xAuthMultiConfigEntry,
       "rldot1xAuthMultiPortNumber": rldot1xAuthMultiPortNumber,
       "rldot1xAuthMultiSourceMac": rldot1xAuthMultiSourceMac,
       "rldot1xAuthMultiPaeState": rldot1xAuthMultiPaeState,
       "rldot1xAuthMultiBackendAuthState": rldot1xAuthMultiBackendAuthState,
       "rldot1xAuthMultiControlledPortStatus": rldot1xAuthMultiControlledPortStatus,
       "rldot1xBpduFilteringEnabled": rldot1xBpduFilteringEnabled,
       "rldot1xRadiusAttributesErrorsAclReject": rldot1xRadiusAttributesErrorsAclReject,
       "rldot1xGuestVlanTimeInterval": rldot1xGuestVlanTimeInterval,
       "rldot1xMacAuthSuccessTrapEnabled": rldot1xMacAuthSuccessTrapEnabled,
       "rldot1xMacAuthFailureTrapEnabled": rldot1xMacAuthFailureTrapEnabled,
       "rldot1xLegacyPortTable": rldot1xLegacyPortTable,
       "rldot1xLegacyPortEntry": rldot1xLegacyPortEntry,
       "rldot1xLegacyPortModeEnabled": rldot1xLegacyPortModeEnabled,
       "rldot1xSystemAuthControlMonitorVlan": rldot1xSystemAuthControlMonitorVlan,
       "rldot1xClearPortMibCounters": rldot1xClearPortMibCounters,
       "rldot1xWebQuietFailureTrapEnabled": rldot1xWebQuietFailureTrapEnabled,
       "rldot1xMacWebAuthSuccessTrapEnabled": rldot1xMacWebAuthSuccessTrapEnabled,
       "rldot1xMacWebAuthFailureTrapEnabled": rldot1xMacWebAuthFailureTrapEnabled,
       "rldot1xLockedCientsTable": rldot1xLockedCientsTable,
       "rldot1xLockedCientsEntry": rldot1xLockedCientsEntry,
       "rldot1xLockedCientsPortNumber": rldot1xLockedCientsPortNumber,
       "rldot1xLockedCientsSourceMac": rldot1xLockedCientsSourceMac,
       "rldot1xLockedCientsRemainedTime": rldot1xLockedCientsRemainedTime,
       "rldot1xLockedCientsRowStatus": rldot1xLockedCientsRowStatus}
)
