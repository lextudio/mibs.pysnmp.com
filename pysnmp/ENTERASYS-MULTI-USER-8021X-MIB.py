# SNMP MIB module (ENTERASYS-MULTI-USER-8021X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-MULTI-USER-8021X-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:16 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

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

(DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysMultiUser8021xMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53)
)
etsysMultiUser8021xMIB.setRevisions(
        ("2004-11-11 15:31",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysMultiUser8021xObjects_ObjectIdentity = ObjectIdentity
etsysMultiUser8021xObjects = _EtsysMultiUser8021xObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1)
)
_EtsysMultiUser8021xSystem_ObjectIdentity = ObjectIdentity
etsysMultiUser8021xSystem = _EtsysMultiUser8021xSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 1)
)
_EtsysMultiUser8021xAccessEntity_ObjectIdentity = ObjectIdentity
etsysMultiUser8021xAccessEntity = _EtsysMultiUser8021xAccessEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2)
)
_EtsysMulti1xAccessEntityTable_Object = MibTable
etsysMulti1xAccessEntityTable = _EtsysMulti1xAccessEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMulti1xAccessEntityTable.setStatus("current")
_EtsysMulti1xAccessEntityEntry_Object = MibTableRow
etsysMulti1xAccessEntityEntry = _EtsysMulti1xAccessEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1, 1)
)
etsysMulti1xAccessEntityEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
    (0, "ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeIndex"),
)
if mibBuilder.loadTexts:
    etsysMulti1xAccessEntityEntry.setStatus("current")
_EtsysMulti1xAeIndex_Type = Unsigned32
_EtsysMulti1xAeIndex_Object = MibTableColumn
etsysMulti1xAeIndex = _EtsysMulti1xAeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1, 1, 1),
    _EtsysMulti1xAeIndex_Type()
)
etsysMulti1xAeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMulti1xAeIndex.setStatus("current")
_EtsysMulti1xAeActive_Type = TruthValue
_EtsysMulti1xAeActive_Object = MibTableColumn
etsysMulti1xAeActive = _EtsysMulti1xAeActive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1, 1, 2),
    _EtsysMulti1xAeActive_Type()
)
etsysMulti1xAeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeActive.setStatus("current")


class _EtsysMulti1xAeState_Type(Integer32):
    """Custom type etsysMulti1xAeState based on Integer32"""
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


_EtsysMulti1xAeState_Type.__name__ = "Integer32"
_EtsysMulti1xAeState_Object = MibTableColumn
etsysMulti1xAeState = _EtsysMulti1xAeState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1, 1, 3),
    _EtsysMulti1xAeState_Type()
)
etsysMulti1xAeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeState.setStatus("current")


class _EtsysMulti1xAeBackendAuthState_Type(Integer32):
    """Custom type etsysMulti1xAeBackendAuthState based on Integer32"""
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


_EtsysMulti1xAeBackendAuthState_Type.__name__ = "Integer32"
_EtsysMulti1xAeBackendAuthState_Object = MibTableColumn
etsysMulti1xAeBackendAuthState = _EtsysMulti1xAeBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1, 1, 4),
    _EtsysMulti1xAeBackendAuthState_Type()
)
etsysMulti1xAeBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeBackendAuthState.setStatus("current")
_EtsysMulti1xAeInitialize_Type = TruthValue
_EtsysMulti1xAeInitialize_Object = MibTableColumn
etsysMulti1xAeInitialize = _EtsysMulti1xAeInitialize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1, 1, 5),
    _EtsysMulti1xAeInitialize_Type()
)
etsysMulti1xAeInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMulti1xAeInitialize.setStatus("current")
_EtsysMulti1xAeReauthenticate_Type = TruthValue
_EtsysMulti1xAeReauthenticate_Object = MibTableColumn
etsysMulti1xAeReauthenticate = _EtsysMulti1xAeReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1, 1, 6),
    _EtsysMulti1xAeReauthenticate_Type()
)
etsysMulti1xAeReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMulti1xAeReauthenticate.setStatus("current")


class _EtsysMulti1xAeReAuthPeriod_Type(Unsigned32):
    """Custom type etsysMulti1xAeReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_EtsysMulti1xAeReAuthPeriod_Object = MibTableColumn
etsysMulti1xAeReAuthPeriod = _EtsysMulti1xAeReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1, 1, 7),
    _EtsysMulti1xAeReAuthPeriod_Type()
)
etsysMulti1xAeReAuthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeReAuthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    etsysMulti1xAeReAuthPeriod.setUnits("seconds")
_EtsysMulti1xAeSupplicantAddress_Type = MacAddress
_EtsysMulti1xAeSupplicantAddress_Object = MibTableColumn
etsysMulti1xAeSupplicantAddress = _EtsysMulti1xAeSupplicantAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1, 1, 8),
    _EtsysMulti1xAeSupplicantAddress_Type()
)
etsysMulti1xAeSupplicantAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeSupplicantAddress.setStatus("current")
_EtsysMulti1xAeUserName_Type = SnmpAdminString
_EtsysMulti1xAeUserName_Object = MibTableColumn
etsysMulti1xAeUserName = _EtsysMulti1xAeUserName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 1, 1, 9),
    _EtsysMulti1xAeUserName_Type()
)
etsysMulti1xAeUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeUserName.setStatus("current")
_EtsysMulti1xAccessEntityStatsTable_Object = MibTable
etsysMulti1xAccessEntityStatsTable = _EtsysMulti1xAccessEntityStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysMulti1xAccessEntityStatsTable.setStatus("current")
_EtsysMulti1xAccessEntityStatsEntry_Object = MibTableRow
etsysMulti1xAccessEntityStatsEntry = _EtsysMulti1xAccessEntityStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMulti1xAccessEntityStatsEntry.setStatus("current")
_EtsysMulti1xAeEapolFramesRx_Type = Counter32
_EtsysMulti1xAeEapolFramesRx_Object = MibTableColumn
etsysMulti1xAeEapolFramesRx = _EtsysMulti1xAeEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 1),
    _EtsysMulti1xAeEapolFramesRx_Type()
)
etsysMulti1xAeEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapolFramesRx.setStatus("current")
_EtsysMulti1xAeEapolFramesTx_Type = Counter32
_EtsysMulti1xAeEapolFramesTx_Object = MibTableColumn
etsysMulti1xAeEapolFramesTx = _EtsysMulti1xAeEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 2),
    _EtsysMulti1xAeEapolFramesTx_Type()
)
etsysMulti1xAeEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapolFramesTx.setStatus("current")
_EtsysMulti1xAeEapolStartFramesRx_Type = Counter32
_EtsysMulti1xAeEapolStartFramesRx_Object = MibTableColumn
etsysMulti1xAeEapolStartFramesRx = _EtsysMulti1xAeEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 3),
    _EtsysMulti1xAeEapolStartFramesRx_Type()
)
etsysMulti1xAeEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapolStartFramesRx.setStatus("current")
_EtsysMulti1xAeEapolLogoffFramesRx_Type = Counter32
_EtsysMulti1xAeEapolLogoffFramesRx_Object = MibTableColumn
etsysMulti1xAeEapolLogoffFramesRx = _EtsysMulti1xAeEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 4),
    _EtsysMulti1xAeEapolLogoffFramesRx_Type()
)
etsysMulti1xAeEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapolLogoffFramesRx.setStatus("current")
_EtsysMulti1xAeEapolRespIdFramesRx_Type = Counter32
_EtsysMulti1xAeEapolRespIdFramesRx_Object = MibTableColumn
etsysMulti1xAeEapolRespIdFramesRx = _EtsysMulti1xAeEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 5),
    _EtsysMulti1xAeEapolRespIdFramesRx_Type()
)
etsysMulti1xAeEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapolRespIdFramesRx.setStatus("current")
_EtsysMulti1xAeEapolRespFramesRx_Type = Counter32
_EtsysMulti1xAeEapolRespFramesRx_Object = MibTableColumn
etsysMulti1xAeEapolRespFramesRx = _EtsysMulti1xAeEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 6),
    _EtsysMulti1xAeEapolRespFramesRx_Type()
)
etsysMulti1xAeEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapolRespFramesRx.setStatus("current")
_EtsysMulti1xAeEapolReqIdFramesTx_Type = Counter32
_EtsysMulti1xAeEapolReqIdFramesTx_Object = MibTableColumn
etsysMulti1xAeEapolReqIdFramesTx = _EtsysMulti1xAeEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 7),
    _EtsysMulti1xAeEapolReqIdFramesTx_Type()
)
etsysMulti1xAeEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapolReqIdFramesTx.setStatus("current")
_EtsysMulti1xAeEapolReqFramesTx_Type = Counter32
_EtsysMulti1xAeEapolReqFramesTx_Object = MibTableColumn
etsysMulti1xAeEapolReqFramesTx = _EtsysMulti1xAeEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 8),
    _EtsysMulti1xAeEapolReqFramesTx_Type()
)
etsysMulti1xAeEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapolReqFramesTx.setStatus("current")
_EtsysMulti1xAeInvalidEapolFramesRx_Type = Counter32
_EtsysMulti1xAeInvalidEapolFramesRx_Object = MibTableColumn
etsysMulti1xAeInvalidEapolFramesRx = _EtsysMulti1xAeInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 9),
    _EtsysMulti1xAeInvalidEapolFramesRx_Type()
)
etsysMulti1xAeInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeInvalidEapolFramesRx.setStatus("current")
_EtsysMulti1xAeEapLengthErrorFramesRx_Type = Counter32
_EtsysMulti1xAeEapLengthErrorFramesRx_Object = MibTableColumn
etsysMulti1xAeEapLengthErrorFramesRx = _EtsysMulti1xAeEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 10),
    _EtsysMulti1xAeEapLengthErrorFramesRx_Type()
)
etsysMulti1xAeEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapLengthErrorFramesRx.setStatus("current")
_EtsysMulti1xAeEapolFrameVersion_Type = Unsigned32
_EtsysMulti1xAeEapolFrameVersion_Object = MibTableColumn
etsysMulti1xAeEapolFrameVersion = _EtsysMulti1xAeEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 11),
    _EtsysMulti1xAeEapolFrameVersion_Type()
)
etsysMulti1xAeEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapolFrameVersion.setStatus("current")
_EtsysMulti1xAeEapolFrameSource_Type = MacAddress
_EtsysMulti1xAeEapolFrameSource_Object = MibTableColumn
etsysMulti1xAeEapolFrameSource = _EtsysMulti1xAeEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 2, 1, 12),
    _EtsysMulti1xAeEapolFrameSource_Type()
)
etsysMulti1xAeEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapolFrameSource.setStatus("current")
_EtsysMulti1xAeDiagTable_Object = MibTable
etsysMulti1xAeDiagTable = _EtsysMulti1xAeDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3)
)
if mibBuilder.loadTexts:
    etsysMulti1xAeDiagTable.setStatus("current")
_EtsysMulti1xAeDiagEntry_Object = MibTableRow
etsysMulti1xAeDiagEntry = _EtsysMulti1xAeDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    etsysMulti1xAeDiagEntry.setStatus("current")
_EtsysMulti1xAeEntersConnecting_Type = Counter32
_EtsysMulti1xAeEntersConnecting_Object = MibTableColumn
etsysMulti1xAeEntersConnecting = _EtsysMulti1xAeEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 1),
    _EtsysMulti1xAeEntersConnecting_Type()
)
etsysMulti1xAeEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEntersConnecting.setStatus("current")
_EtsysMulti1xAeEapLogoffsWhileConnecting_Type = Counter32
_EtsysMulti1xAeEapLogoffsWhileConnecting_Object = MibTableColumn
etsysMulti1xAeEapLogoffsWhileConnecting = _EtsysMulti1xAeEapLogoffsWhileConnecting_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 2),
    _EtsysMulti1xAeEapLogoffsWhileConnecting_Type()
)
etsysMulti1xAeEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEapLogoffsWhileConnecting.setStatus("current")
_EtsysMulti1xAeEntersAuthenticating_Type = Counter32
_EtsysMulti1xAeEntersAuthenticating_Object = MibTableColumn
etsysMulti1xAeEntersAuthenticating = _EtsysMulti1xAeEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 3),
    _EtsysMulti1xAeEntersAuthenticating_Type()
)
etsysMulti1xAeEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeEntersAuthenticating.setStatus("current")
_EtsysMulti1xAeAuthSuccessWhileAuthenticating_Type = Counter32
_EtsysMulti1xAeAuthSuccessWhileAuthenticating_Object = MibTableColumn
etsysMulti1xAeAuthSuccessWhileAuthenticating = _EtsysMulti1xAeAuthSuccessWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 4),
    _EtsysMulti1xAeAuthSuccessWhileAuthenticating_Type()
)
etsysMulti1xAeAuthSuccessWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeAuthSuccessWhileAuthenticating.setStatus("current")
_EtsysMulti1xAeAuthTimeoutsWhileAuthenticating_Type = Counter32
_EtsysMulti1xAeAuthTimeoutsWhileAuthenticating_Object = MibTableColumn
etsysMulti1xAeAuthTimeoutsWhileAuthenticating = _EtsysMulti1xAeAuthTimeoutsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 5),
    _EtsysMulti1xAeAuthTimeoutsWhileAuthenticating_Type()
)
etsysMulti1xAeAuthTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeAuthTimeoutsWhileAuthenticating.setStatus("current")
_EtsysMulti1xAeAuthFailWhileAuthenticating_Type = Counter32
_EtsysMulti1xAeAuthFailWhileAuthenticating_Object = MibTableColumn
etsysMulti1xAeAuthFailWhileAuthenticating = _EtsysMulti1xAeAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 6),
    _EtsysMulti1xAeAuthFailWhileAuthenticating_Type()
)
etsysMulti1xAeAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeAuthFailWhileAuthenticating.setStatus("current")
_EtsysMulti1xAeAuthReauthsWhileAuthenticating_Type = Counter32
_EtsysMulti1xAeAuthReauthsWhileAuthenticating_Object = MibTableColumn
etsysMulti1xAeAuthReauthsWhileAuthenticating = _EtsysMulti1xAeAuthReauthsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 7),
    _EtsysMulti1xAeAuthReauthsWhileAuthenticating_Type()
)
etsysMulti1xAeAuthReauthsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeAuthReauthsWhileAuthenticating.setStatus("current")
_EtsysMulti1xAeAuthEapStartsWhileAuthenticating_Type = Counter32
_EtsysMulti1xAeAuthEapStartsWhileAuthenticating_Object = MibTableColumn
etsysMulti1xAeAuthEapStartsWhileAuthenticating = _EtsysMulti1xAeAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 8),
    _EtsysMulti1xAeAuthEapStartsWhileAuthenticating_Type()
)
etsysMulti1xAeAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeAuthEapStartsWhileAuthenticating.setStatus("current")
_EtsysMulti1xAeAuthEapLogoffWhileAuthenticating_Type = Counter32
_EtsysMulti1xAeAuthEapLogoffWhileAuthenticating_Object = MibTableColumn
etsysMulti1xAeAuthEapLogoffWhileAuthenticating = _EtsysMulti1xAeAuthEapLogoffWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 9),
    _EtsysMulti1xAeAuthEapLogoffWhileAuthenticating_Type()
)
etsysMulti1xAeAuthEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeAuthEapLogoffWhileAuthenticating.setStatus("current")
_EtsysMulti1xAeAuthReauthsWhileAuthenticated_Type = Counter32
_EtsysMulti1xAeAuthReauthsWhileAuthenticated_Object = MibTableColumn
etsysMulti1xAeAuthReauthsWhileAuthenticated = _EtsysMulti1xAeAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 10),
    _EtsysMulti1xAeAuthReauthsWhileAuthenticated_Type()
)
etsysMulti1xAeAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeAuthReauthsWhileAuthenticated.setStatus("current")
_EtsysMulti1xAeAuthEapStartsWhileAuthenticated_Type = Counter32
_EtsysMulti1xAeAuthEapStartsWhileAuthenticated_Object = MibTableColumn
etsysMulti1xAeAuthEapStartsWhileAuthenticated = _EtsysMulti1xAeAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 11),
    _EtsysMulti1xAeAuthEapStartsWhileAuthenticated_Type()
)
etsysMulti1xAeAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeAuthEapStartsWhileAuthenticated.setStatus("current")
_EtsysMulti1xAeAuthEapLogoffWhileAuthenticated_Type = Counter32
_EtsysMulti1xAeAuthEapLogoffWhileAuthenticated_Object = MibTableColumn
etsysMulti1xAeAuthEapLogoffWhileAuthenticated = _EtsysMulti1xAeAuthEapLogoffWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 12),
    _EtsysMulti1xAeAuthEapLogoffWhileAuthenticated_Type()
)
etsysMulti1xAeAuthEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeAuthEapLogoffWhileAuthenticated.setStatus("current")
_EtsysMulti1xAeBackendResponses_Type = Counter32
_EtsysMulti1xAeBackendResponses_Object = MibTableColumn
etsysMulti1xAeBackendResponses = _EtsysMulti1xAeBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 13),
    _EtsysMulti1xAeBackendResponses_Type()
)
etsysMulti1xAeBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeBackendResponses.setStatus("current")
_EtsysMulti1xAeBackendAccessChallenges_Type = Counter32
_EtsysMulti1xAeBackendAccessChallenges_Object = MibTableColumn
etsysMulti1xAeBackendAccessChallenges = _EtsysMulti1xAeBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 14),
    _EtsysMulti1xAeBackendAccessChallenges_Type()
)
etsysMulti1xAeBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeBackendAccessChallenges.setStatus("current")
_EtsysMulti1xAeBackendOtherRequestsToSupplicant_Type = Counter32
_EtsysMulti1xAeBackendOtherRequestsToSupplicant_Object = MibTableColumn
etsysMulti1xAeBackendOtherRequestsToSupplicant = _EtsysMulti1xAeBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 15),
    _EtsysMulti1xAeBackendOtherRequestsToSupplicant_Type()
)
etsysMulti1xAeBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeBackendOtherRequestsToSupplicant.setStatus("current")
_EtsysMulti1xAeBackendNonNakResponsesFromSupplicant_Type = Counter32
_EtsysMulti1xAeBackendNonNakResponsesFromSupplicant_Object = MibTableColumn
etsysMulti1xAeBackendNonNakResponsesFromSupplicant = _EtsysMulti1xAeBackendNonNakResponsesFromSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 16),
    _EtsysMulti1xAeBackendNonNakResponsesFromSupplicant_Type()
)
etsysMulti1xAeBackendNonNakResponsesFromSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeBackendNonNakResponsesFromSupplicant.setStatus("current")
_EtsysMulti1xAeBackendAuthSuccesses_Type = Counter32
_EtsysMulti1xAeBackendAuthSuccesses_Object = MibTableColumn
etsysMulti1xAeBackendAuthSuccesses = _EtsysMulti1xAeBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 17),
    _EtsysMulti1xAeBackendAuthSuccesses_Type()
)
etsysMulti1xAeBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeBackendAuthSuccesses.setStatus("current")
_EtsysMulti1xAeBackendAuthFails_Type = Counter32
_EtsysMulti1xAeBackendAuthFails_Object = MibTableColumn
etsysMulti1xAeBackendAuthFails = _EtsysMulti1xAeBackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 3, 1, 18),
    _EtsysMulti1xAeBackendAuthFails_Type()
)
etsysMulti1xAeBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xAeBackendAuthFails.setStatus("current")
_EtsysMulti1xSessionStatsTable_Object = MibTable
etsysMulti1xSessionStatsTable = _EtsysMulti1xSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4)
)
if mibBuilder.loadTexts:
    etsysMulti1xSessionStatsTable.setStatus("current")
_EtsysMulti1xSessionStatsEntry_Object = MibTableRow
etsysMulti1xSessionStatsEntry = _EtsysMulti1xSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    etsysMulti1xSessionStatsEntry.setStatus("current")
_EtsysMulti1xSessionOctetsRx_Type = Counter64
_EtsysMulti1xSessionOctetsRx_Object = MibTableColumn
etsysMulti1xSessionOctetsRx = _EtsysMulti1xSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1, 1),
    _EtsysMulti1xSessionOctetsRx_Type()
)
etsysMulti1xSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSessionOctetsRx.setStatus("current")
_EtsysMulti1xSessionOctetsTx_Type = Counter64
_EtsysMulti1xSessionOctetsTx_Object = MibTableColumn
etsysMulti1xSessionOctetsTx = _EtsysMulti1xSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1, 2),
    _EtsysMulti1xSessionOctetsTx_Type()
)
etsysMulti1xSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSessionOctetsTx.setStatus("current")
_EtsysMulti1xSessionFramesRx_Type = Counter32
_EtsysMulti1xSessionFramesRx_Object = MibTableColumn
etsysMulti1xSessionFramesRx = _EtsysMulti1xSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1, 3),
    _EtsysMulti1xSessionFramesRx_Type()
)
etsysMulti1xSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSessionFramesRx.setStatus("current")
_EtsysMulti1xSessionFramesTx_Type = Counter32
_EtsysMulti1xSessionFramesTx_Object = MibTableColumn
etsysMulti1xSessionFramesTx = _EtsysMulti1xSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1, 4),
    _EtsysMulti1xSessionFramesTx_Type()
)
etsysMulti1xSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSessionFramesTx.setStatus("current")
_EtsysMulti1xSessionId_Type = SnmpAdminString
_EtsysMulti1xSessionId_Object = MibTableColumn
etsysMulti1xSessionId = _EtsysMulti1xSessionId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1, 5),
    _EtsysMulti1xSessionId_Type()
)
etsysMulti1xSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSessionId.setStatus("current")


class _EtsysMulti1xSessionAuthenticMethod_Type(Integer32):
    """Custom type etsysMulti1xSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localAuthServer", 2),
          ("remoteAuthServer", 1))
    )


_EtsysMulti1xSessionAuthenticMethod_Type.__name__ = "Integer32"
_EtsysMulti1xSessionAuthenticMethod_Object = MibTableColumn
etsysMulti1xSessionAuthenticMethod = _EtsysMulti1xSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1, 6),
    _EtsysMulti1xSessionAuthenticMethod_Type()
)
etsysMulti1xSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSessionAuthenticMethod.setStatus("current")
_EtsysMulti1xSessionTime_Type = TimeTicks
_EtsysMulti1xSessionTime_Object = MibTableColumn
etsysMulti1xSessionTime = _EtsysMulti1xSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1, 7),
    _EtsysMulti1xSessionTime_Type()
)
etsysMulti1xSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSessionTime.setStatus("current")


class _EtsysMulti1xSessionTerminateCause_Type(Integer32):
    """Custom type etsysMulti1xSessionTerminateCause based on Integer32"""
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
              999)
        )
    )
    namedValues = NamedValues(
        *(("authControlForceUnauth", 5),
          ("notTerminatedYet", 999),
          ("portAdminDisabled", 7),
          ("portFailure", 2),
          ("portReInit", 6),
          ("reauthFailed", 4),
          ("supplicantLogoff", 1),
          ("supplicantRestart", 3))
    )


_EtsysMulti1xSessionTerminateCause_Type.__name__ = "Integer32"
_EtsysMulti1xSessionTerminateCause_Object = MibTableColumn
etsysMulti1xSessionTerminateCause = _EtsysMulti1xSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1, 8),
    _EtsysMulti1xSessionTerminateCause_Type()
)
etsysMulti1xSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSessionTerminateCause.setStatus("current")
_EtsysMulti1xSessionUserName_Type = SnmpAdminString
_EtsysMulti1xSessionUserName_Object = MibTableColumn
etsysMulti1xSessionUserName = _EtsysMulti1xSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1, 9),
    _EtsysMulti1xSessionUserName_Type()
)
etsysMulti1xSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSessionUserName.setStatus("current")
_EtsysMulti1xSessionActive_Type = TruthValue
_EtsysMulti1xSessionActive_Object = MibTableColumn
etsysMulti1xSessionActive = _EtsysMulti1xSessionActive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 4, 1, 10),
    _EtsysMulti1xSessionActive_Type()
)
etsysMulti1xSessionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSessionActive.setStatus("current")
_EtsysMulti1xSupplicantAddressTable_Object = MibTable
etsysMulti1xSupplicantAddressTable = _EtsysMulti1xSupplicantAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 5)
)
if mibBuilder.loadTexts:
    etsysMulti1xSupplicantAddressTable.setStatus("current")
_EtsysMulti1xSupplicantAddressEntry_Object = MibTableRow
etsysMulti1xSupplicantAddressEntry = _EtsysMulti1xSupplicantAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 5, 1)
)
etsysMulti1xSupplicantAddressEntry.setIndexNames(
    (0, "ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeSupplicantAddress"),
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
    (0, "ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeIndex"),
)
if mibBuilder.loadTexts:
    etsysMulti1xSupplicantAddressEntry.setStatus("current")
_EtsysMulti1xSupplicantActive_Type = TruthValue
_EtsysMulti1xSupplicantActive_Object = MibTableColumn
etsysMulti1xSupplicantActive = _EtsysMulti1xSupplicantActive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 5, 1, 1),
    _EtsysMulti1xSupplicantActive_Type()
)
etsysMulti1xSupplicantActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSupplicantActive.setStatus("current")
_EtsysMulti1xSupplicantUserName_Type = SnmpAdminString
_EtsysMulti1xSupplicantUserName_Object = MibTableColumn
etsysMulti1xSupplicantUserName = _EtsysMulti1xSupplicantUserName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 5, 1, 2),
    _EtsysMulti1xSupplicantUserName_Type()
)
etsysMulti1xSupplicantUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xSupplicantUserName.setStatus("current")
_EtsysMulti1xUserNameTable_Object = MibTable
etsysMulti1xUserNameTable = _EtsysMulti1xUserNameTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 6)
)
if mibBuilder.loadTexts:
    etsysMulti1xUserNameTable.setStatus("current")
_EtsysMulti1xUserNameEntry_Object = MibTableRow
etsysMulti1xUserNameEntry = _EtsysMulti1xUserNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 6, 1)
)
etsysMulti1xUserNameEntry.setIndexNames(
    (0, "ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xUserNameIndex"),
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
    (0, "ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeIndex"),
)
if mibBuilder.loadTexts:
    etsysMulti1xUserNameEntry.setStatus("current")


class _EtsysMulti1xUserNameIndex_Type(SnmpAdminString):
    """Custom type etsysMulti1xUserNameIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EtsysMulti1xUserNameIndex_Type.__name__ = "SnmpAdminString"
_EtsysMulti1xUserNameIndex_Object = MibTableColumn
etsysMulti1xUserNameIndex = _EtsysMulti1xUserNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 6, 1, 1),
    _EtsysMulti1xUserNameIndex_Type()
)
etsysMulti1xUserNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMulti1xUserNameIndex.setStatus("current")
_EtsysMulti1xUserName_Type = SnmpAdminString
_EtsysMulti1xUserName_Object = MibTableColumn
etsysMulti1xUserName = _EtsysMulti1xUserName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 6, 1, 2),
    _EtsysMulti1xUserName_Type()
)
etsysMulti1xUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xUserName.setStatus("current")
_EtsysMulti1xUserActive_Type = TruthValue
_EtsysMulti1xUserActive_Object = MibTableColumn
etsysMulti1xUserActive = _EtsysMulti1xUserActive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 6, 1, 3),
    _EtsysMulti1xUserActive_Type()
)
etsysMulti1xUserActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xUserActive.setStatus("current")
_EtsysMulti1xUserAddress_Type = MacAddress
_EtsysMulti1xUserAddress_Object = MibTableColumn
etsysMulti1xUserAddress = _EtsysMulti1xUserAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 6, 1, 4),
    _EtsysMulti1xUserAddress_Type()
)
etsysMulti1xUserAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xUserAddress.setStatus("current")
_EtsysMulti1xActiveAccessEntityTable_Object = MibTable
etsysMulti1xActiveAccessEntityTable = _EtsysMulti1xActiveAccessEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 7)
)
if mibBuilder.loadTexts:
    etsysMulti1xActiveAccessEntityTable.setStatus("current")
_EtsysMulti1xActiveAccessEntityEntry_Object = MibTableRow
etsysMulti1xActiveAccessEntityEntry = _EtsysMulti1xActiveAccessEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 7, 1)
)
etsysMulti1xActiveAccessEntityEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
    (0, "ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeIndex"),
)
if mibBuilder.loadTexts:
    etsysMulti1xActiveAccessEntityEntry.setStatus("current")
_EtsysMulti1xActiveSupplicantAddress_Type = MacAddress
_EtsysMulti1xActiveSupplicantAddress_Object = MibTableColumn
etsysMulti1xActiveSupplicantAddress = _EtsysMulti1xActiveSupplicantAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 1, 2, 7, 1, 1),
    _EtsysMulti1xActiveSupplicantAddress_Type()
)
etsysMulti1xActiveSupplicantAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMulti1xActiveSupplicantAddress.setStatus("current")
_EtsysMultiUser8021xConformance_ObjectIdentity = ObjectIdentity
etsysMultiUser8021xConformance = _EtsysMultiUser8021xConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2)
)
_EtsysMultiUser8021xGroups_ObjectIdentity = ObjectIdentity
etsysMultiUser8021xGroups = _EtsysMultiUser8021xGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2, 1)
)
_EtsysMultiUser8021xCompliances_ObjectIdentity = ObjectIdentity
etsysMultiUser8021xCompliances = _EtsysMultiUser8021xCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2, 2)
)
etsysMulti1xAccessEntityEntry.registerAugmentions(
    ("ENTERASYS-MULTI-USER-8021X-MIB",
     "etsysMulti1xAccessEntityStatsEntry")
)
etsysMulti1xAccessEntityStatsEntry.setIndexNames(*etsysMulti1xAccessEntityEntry.getIndexNames())
etsysMulti1xAccessEntityEntry.registerAugmentions(
    ("ENTERASYS-MULTI-USER-8021X-MIB",
     "etsysMulti1xAeDiagEntry")
)
etsysMulti1xAeDiagEntry.setIndexNames(*etsysMulti1xAccessEntityEntry.getIndexNames())
etsysMulti1xAccessEntityEntry.registerAugmentions(
    ("ENTERASYS-MULTI-USER-8021X-MIB",
     "etsysMulti1xSessionStatsEntry")
)
etsysMulti1xSessionStatsEntry.setIndexNames(*etsysMulti1xAccessEntityEntry.getIndexNames())

# Managed Objects groups

etsysMultiUser8021xAccessEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2, 1, 1)
)
etsysMultiUser8021xAccessEntityGroup.setObjects(
      *(("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeActive"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeState"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeBackendAuthState"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeInitialize"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeReauthenticate"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeReAuthPeriod"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeSupplicantAddress"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeUserName"))
)
if mibBuilder.loadTexts:
    etsysMultiUser8021xAccessEntityGroup.setStatus("current")

etsysMultiUser8021xAccessEntityStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2, 1, 2)
)
etsysMultiUser8021xAccessEntityStatsGroup.setObjects(
      *(("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapolFramesRx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapolFramesTx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapolStartFramesRx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapolLogoffFramesRx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapolRespIdFramesRx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapolRespFramesRx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapolReqIdFramesTx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapolReqFramesTx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeInvalidEapolFramesRx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapLengthErrorFramesRx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapolFrameVersion"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapolFrameSource"))
)
if mibBuilder.loadTexts:
    etsysMultiUser8021xAccessEntityStatsGroup.setStatus("current")

etsysMultiUser8021xAccessEntityDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2, 1, 3)
)
etsysMultiUser8021xAccessEntityDiagGroup.setObjects(
      *(("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEntersConnecting"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEapLogoffsWhileConnecting"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeEntersAuthenticating"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeAuthSuccessWhileAuthenticating"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeAuthTimeoutsWhileAuthenticating"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeAuthFailWhileAuthenticating"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeAuthReauthsWhileAuthenticating"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeAuthEapStartsWhileAuthenticating"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeAuthEapLogoffWhileAuthenticating"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeAuthReauthsWhileAuthenticated"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeAuthEapStartsWhileAuthenticated"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeAuthEapLogoffWhileAuthenticated"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeBackendResponses"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeBackendAccessChallenges"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeBackendOtherRequestsToSupplicant"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeBackendNonNakResponsesFromSupplicant"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeBackendAuthSuccesses"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xAeBackendAuthFails"))
)
if mibBuilder.loadTexts:
    etsysMultiUser8021xAccessEntityDiagGroup.setStatus("current")

etsysMultiUser8021xAccessEntitySessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2, 1, 4)
)
etsysMultiUser8021xAccessEntitySessionGroup.setObjects(
      *(("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSessionOctetsRx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSessionOctetsTx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSessionFramesRx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSessionFramesTx"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSessionId"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSessionAuthenticMethod"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSessionTime"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSessionTerminateCause"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSessionUserName"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSessionActive"))
)
if mibBuilder.loadTexts:
    etsysMultiUser8021xAccessEntitySessionGroup.setStatus("current")

etsysMultiUser8021xSupplicantAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2, 1, 5)
)
etsysMultiUser8021xSupplicantAddressGroup.setObjects(
      *(("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSupplicantActive"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xSupplicantUserName"))
)
if mibBuilder.loadTexts:
    etsysMultiUser8021xSupplicantAddressGroup.setStatus("current")

etsysMultiUser8021xUserNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2, 1, 6)
)
etsysMultiUser8021xUserNameGroup.setObjects(
      *(("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xUserName"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xUserActive"),
        ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xUserAddress"))
)
if mibBuilder.loadTexts:
    etsysMultiUser8021xUserNameGroup.setStatus("current")

etsysMultiUser8021xActiveAccessEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2, 1, 7)
)
etsysMultiUser8021xActiveAccessEntityGroup.setObjects(
    ("ENTERASYS-MULTI-USER-8021X-MIB", "etsysMulti1xActiveSupplicantAddress")
)
if mibBuilder.loadTexts:
    etsysMultiUser8021xActiveAccessEntityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysMulti8021xCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 53, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMulti8021xCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MULTI-USER-8021X-MIB",
    **{"etsysMultiUser8021xMIB": etsysMultiUser8021xMIB,
       "etsysMultiUser8021xObjects": etsysMultiUser8021xObjects,
       "etsysMultiUser8021xSystem": etsysMultiUser8021xSystem,
       "etsysMultiUser8021xAccessEntity": etsysMultiUser8021xAccessEntity,
       "etsysMulti1xAccessEntityTable": etsysMulti1xAccessEntityTable,
       "etsysMulti1xAccessEntityEntry": etsysMulti1xAccessEntityEntry,
       "etsysMulti1xAeIndex": etsysMulti1xAeIndex,
       "etsysMulti1xAeActive": etsysMulti1xAeActive,
       "etsysMulti1xAeState": etsysMulti1xAeState,
       "etsysMulti1xAeBackendAuthState": etsysMulti1xAeBackendAuthState,
       "etsysMulti1xAeInitialize": etsysMulti1xAeInitialize,
       "etsysMulti1xAeReauthenticate": etsysMulti1xAeReauthenticate,
       "etsysMulti1xAeReAuthPeriod": etsysMulti1xAeReAuthPeriod,
       "etsysMulti1xAeSupplicantAddress": etsysMulti1xAeSupplicantAddress,
       "etsysMulti1xAeUserName": etsysMulti1xAeUserName,
       "etsysMulti1xAccessEntityStatsTable": etsysMulti1xAccessEntityStatsTable,
       "etsysMulti1xAccessEntityStatsEntry": etsysMulti1xAccessEntityStatsEntry,
       "etsysMulti1xAeEapolFramesRx": etsysMulti1xAeEapolFramesRx,
       "etsysMulti1xAeEapolFramesTx": etsysMulti1xAeEapolFramesTx,
       "etsysMulti1xAeEapolStartFramesRx": etsysMulti1xAeEapolStartFramesRx,
       "etsysMulti1xAeEapolLogoffFramesRx": etsysMulti1xAeEapolLogoffFramesRx,
       "etsysMulti1xAeEapolRespIdFramesRx": etsysMulti1xAeEapolRespIdFramesRx,
       "etsysMulti1xAeEapolRespFramesRx": etsysMulti1xAeEapolRespFramesRx,
       "etsysMulti1xAeEapolReqIdFramesTx": etsysMulti1xAeEapolReqIdFramesTx,
       "etsysMulti1xAeEapolReqFramesTx": etsysMulti1xAeEapolReqFramesTx,
       "etsysMulti1xAeInvalidEapolFramesRx": etsysMulti1xAeInvalidEapolFramesRx,
       "etsysMulti1xAeEapLengthErrorFramesRx": etsysMulti1xAeEapLengthErrorFramesRx,
       "etsysMulti1xAeEapolFrameVersion": etsysMulti1xAeEapolFrameVersion,
       "etsysMulti1xAeEapolFrameSource": etsysMulti1xAeEapolFrameSource,
       "etsysMulti1xAeDiagTable": etsysMulti1xAeDiagTable,
       "etsysMulti1xAeDiagEntry": etsysMulti1xAeDiagEntry,
       "etsysMulti1xAeEntersConnecting": etsysMulti1xAeEntersConnecting,
       "etsysMulti1xAeEapLogoffsWhileConnecting": etsysMulti1xAeEapLogoffsWhileConnecting,
       "etsysMulti1xAeEntersAuthenticating": etsysMulti1xAeEntersAuthenticating,
       "etsysMulti1xAeAuthSuccessWhileAuthenticating": etsysMulti1xAeAuthSuccessWhileAuthenticating,
       "etsysMulti1xAeAuthTimeoutsWhileAuthenticating": etsysMulti1xAeAuthTimeoutsWhileAuthenticating,
       "etsysMulti1xAeAuthFailWhileAuthenticating": etsysMulti1xAeAuthFailWhileAuthenticating,
       "etsysMulti1xAeAuthReauthsWhileAuthenticating": etsysMulti1xAeAuthReauthsWhileAuthenticating,
       "etsysMulti1xAeAuthEapStartsWhileAuthenticating": etsysMulti1xAeAuthEapStartsWhileAuthenticating,
       "etsysMulti1xAeAuthEapLogoffWhileAuthenticating": etsysMulti1xAeAuthEapLogoffWhileAuthenticating,
       "etsysMulti1xAeAuthReauthsWhileAuthenticated": etsysMulti1xAeAuthReauthsWhileAuthenticated,
       "etsysMulti1xAeAuthEapStartsWhileAuthenticated": etsysMulti1xAeAuthEapStartsWhileAuthenticated,
       "etsysMulti1xAeAuthEapLogoffWhileAuthenticated": etsysMulti1xAeAuthEapLogoffWhileAuthenticated,
       "etsysMulti1xAeBackendResponses": etsysMulti1xAeBackendResponses,
       "etsysMulti1xAeBackendAccessChallenges": etsysMulti1xAeBackendAccessChallenges,
       "etsysMulti1xAeBackendOtherRequestsToSupplicant": etsysMulti1xAeBackendOtherRequestsToSupplicant,
       "etsysMulti1xAeBackendNonNakResponsesFromSupplicant": etsysMulti1xAeBackendNonNakResponsesFromSupplicant,
       "etsysMulti1xAeBackendAuthSuccesses": etsysMulti1xAeBackendAuthSuccesses,
       "etsysMulti1xAeBackendAuthFails": etsysMulti1xAeBackendAuthFails,
       "etsysMulti1xSessionStatsTable": etsysMulti1xSessionStatsTable,
       "etsysMulti1xSessionStatsEntry": etsysMulti1xSessionStatsEntry,
       "etsysMulti1xSessionOctetsRx": etsysMulti1xSessionOctetsRx,
       "etsysMulti1xSessionOctetsTx": etsysMulti1xSessionOctetsTx,
       "etsysMulti1xSessionFramesRx": etsysMulti1xSessionFramesRx,
       "etsysMulti1xSessionFramesTx": etsysMulti1xSessionFramesTx,
       "etsysMulti1xSessionId": etsysMulti1xSessionId,
       "etsysMulti1xSessionAuthenticMethod": etsysMulti1xSessionAuthenticMethod,
       "etsysMulti1xSessionTime": etsysMulti1xSessionTime,
       "etsysMulti1xSessionTerminateCause": etsysMulti1xSessionTerminateCause,
       "etsysMulti1xSessionUserName": etsysMulti1xSessionUserName,
       "etsysMulti1xSessionActive": etsysMulti1xSessionActive,
       "etsysMulti1xSupplicantAddressTable": etsysMulti1xSupplicantAddressTable,
       "etsysMulti1xSupplicantAddressEntry": etsysMulti1xSupplicantAddressEntry,
       "etsysMulti1xSupplicantActive": etsysMulti1xSupplicantActive,
       "etsysMulti1xSupplicantUserName": etsysMulti1xSupplicantUserName,
       "etsysMulti1xUserNameTable": etsysMulti1xUserNameTable,
       "etsysMulti1xUserNameEntry": etsysMulti1xUserNameEntry,
       "etsysMulti1xUserNameIndex": etsysMulti1xUserNameIndex,
       "etsysMulti1xUserName": etsysMulti1xUserName,
       "etsysMulti1xUserActive": etsysMulti1xUserActive,
       "etsysMulti1xUserAddress": etsysMulti1xUserAddress,
       "etsysMulti1xActiveAccessEntityTable": etsysMulti1xActiveAccessEntityTable,
       "etsysMulti1xActiveAccessEntityEntry": etsysMulti1xActiveAccessEntityEntry,
       "etsysMulti1xActiveSupplicantAddress": etsysMulti1xActiveSupplicantAddress,
       "etsysMultiUser8021xConformance": etsysMultiUser8021xConformance,
       "etsysMultiUser8021xGroups": etsysMultiUser8021xGroups,
       "etsysMultiUser8021xAccessEntityGroup": etsysMultiUser8021xAccessEntityGroup,
       "etsysMultiUser8021xAccessEntityStatsGroup": etsysMultiUser8021xAccessEntityStatsGroup,
       "etsysMultiUser8021xAccessEntityDiagGroup": etsysMultiUser8021xAccessEntityDiagGroup,
       "etsysMultiUser8021xAccessEntitySessionGroup": etsysMultiUser8021xAccessEntitySessionGroup,
       "etsysMultiUser8021xSupplicantAddressGroup": etsysMultiUser8021xSupplicantAddressGroup,
       "etsysMultiUser8021xUserNameGroup": etsysMultiUser8021xUserNameGroup,
       "etsysMultiUser8021xActiveAccessEntityGroup": etsysMultiUser8021xActiveAccessEntityGroup,
       "etsysMultiUser8021xCompliances": etsysMultiUser8021xCompliances,
       "etsysMulti8021xCompliance": etsysMulti8021xCompliance}
)
