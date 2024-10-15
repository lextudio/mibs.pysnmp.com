# SNMP MIB module (ENTERASYS-8021X-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-8021X-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:39 2024
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

(PaeControlledDirections,
 PaeControlledPortControl,
 PaeControlledPortStatus) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "PaeControlledDirections",
    "PaeControlledPortControl",
    "PaeControlledPortStatus")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsys8021xExtensionsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18)
)
etsys8021xExtensionsMIB.setRevisions(
        ("2003-11-21 16:23",
         "2002-03-07 20:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysDot1xExtensionsObjects_ObjectIdentity = ObjectIdentity
etsysDot1xExtensionsObjects = _EtsysDot1xExtensionsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1)
)
_EtsysDot1xSystemBranch_ObjectIdentity = ObjectIdentity
etsysDot1xSystemBranch = _EtsysDot1xSystemBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 1)
)
_EtsysDot1xAuthenticatorBranch_ObjectIdentity = ObjectIdentity
etsysDot1xAuthenticatorBranch = _EtsysDot1xAuthenticatorBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2)
)
_EtsysDot1xAuthStationBranch_ObjectIdentity = ObjectIdentity
etsysDot1xAuthStationBranch = _EtsysDot1xAuthStationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1)
)
_EtsysDot1xAuthStationTable_Object = MibTable
etsysDot1xAuthStationTable = _EtsysDot1xAuthStationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysDot1xAuthStationTable.setStatus("current")
_EtsysDot1xAuthStationEntry_Object = MibTableRow
etsysDot1xAuthStationEntry = _EtsysDot1xAuthStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 1, 1)
)
etsysDot1xAuthStationEntry.setIndexNames(
    (0, "ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthStationAddress"),
)
if mibBuilder.loadTexts:
    etsysDot1xAuthStationEntry.setStatus("current")
_EtsysDot1xAuthStationAddress_Type = MacAddress
_EtsysDot1xAuthStationAddress_Object = MibTableColumn
etsysDot1xAuthStationAddress = _EtsysDot1xAuthStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 1, 1, 1),
    _EtsysDot1xAuthStationAddress_Type()
)
etsysDot1xAuthStationAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysDot1xAuthStationAddress.setStatus("current")
_EtsysDot1xAuthStationPaePort_Type = InterfaceIndex
_EtsysDot1xAuthStationPaePort_Object = MibTableColumn
etsysDot1xAuthStationPaePort = _EtsysDot1xAuthStationPaePort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 1, 1, 2),
    _EtsysDot1xAuthStationPaePort_Type()
)
etsysDot1xAuthStationPaePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthStationPaePort.setStatus("current")


class _EtsysDot1xAuthStationPaeState_Type(Integer32):
    """Custom type etsysDot1xAuthStationPaeState based on Integer32"""
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


_EtsysDot1xAuthStationPaeState_Type.__name__ = "Integer32"
_EtsysDot1xAuthStationPaeState_Object = MibTableColumn
etsysDot1xAuthStationPaeState = _EtsysDot1xAuthStationPaeState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 1, 1, 3),
    _EtsysDot1xAuthStationPaeState_Type()
)
etsysDot1xAuthStationPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthStationPaeState.setStatus("current")


class _EtsysDot1xAuthStationBackendAuthState_Type(Integer32):
    """Custom type etsysDot1xAuthStationBackendAuthState based on Integer32"""
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


_EtsysDot1xAuthStationBackendAuthState_Type.__name__ = "Integer32"
_EtsysDot1xAuthStationBackendAuthState_Object = MibTableColumn
etsysDot1xAuthStationBackendAuthState = _EtsysDot1xAuthStationBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 1, 1, 4),
    _EtsysDot1xAuthStationBackendAuthState_Type()
)
etsysDot1xAuthStationBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthStationBackendAuthState.setStatus("current")
_EtsysDot1xAuthStationUserName_Type = SnmpAdminString
_EtsysDot1xAuthStationUserName_Object = MibTableColumn
etsysDot1xAuthStationUserName = _EtsysDot1xAuthStationUserName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 1, 1, 5),
    _EtsysDot1xAuthStationUserName_Type()
)
etsysDot1xAuthStationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthStationUserName.setStatus("current")
_EtsysDot1xAuthConfigTable_Object = MibTable
etsysDot1xAuthConfigTable = _EtsysDot1xAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    etsysDot1xAuthConfigTable.setStatus("current")
_EtsysDot1xAuthConfigEntry_Object = MibTableRow
etsysDot1xAuthConfigEntry = _EtsysDot1xAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1)
)
etsysDot1xAuthConfigEntry.setIndexNames(
    (0, "ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthStationAddress"),
)
if mibBuilder.loadTexts:
    etsysDot1xAuthConfigEntry.setStatus("current")
_EtsysDot1xAuthInitialize_Type = TruthValue
_EtsysDot1xAuthInitialize_Object = MibTableColumn
etsysDot1xAuthInitialize = _EtsysDot1xAuthInitialize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 1),
    _EtsysDot1xAuthInitialize_Type()
)
etsysDot1xAuthInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot1xAuthInitialize.setStatus("current")
_EtsysDot1xAuthReauthenticate_Type = TruthValue
_EtsysDot1xAuthReauthenticate_Object = MibTableColumn
etsysDot1xAuthReauthenticate = _EtsysDot1xAuthReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 2),
    _EtsysDot1xAuthReauthenticate_Type()
)
etsysDot1xAuthReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot1xAuthReauthenticate.setStatus("current")
_EtsysDot1xAuthAdminControlledDirections_Type = PaeControlledDirections
_EtsysDot1xAuthAdminControlledDirections_Object = MibTableColumn
etsysDot1xAuthAdminControlledDirections = _EtsysDot1xAuthAdminControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 3),
    _EtsysDot1xAuthAdminControlledDirections_Type()
)
etsysDot1xAuthAdminControlledDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAdminControlledDirections.setStatus("current")
_EtsysDot1xAuthOperControlledDirections_Type = PaeControlledDirections
_EtsysDot1xAuthOperControlledDirections_Object = MibTableColumn
etsysDot1xAuthOperControlledDirections = _EtsysDot1xAuthOperControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 4),
    _EtsysDot1xAuthOperControlledDirections_Type()
)
etsysDot1xAuthOperControlledDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthOperControlledDirections.setStatus("current")
_EtsysDot1xAuthAuthControlledPortStatus_Type = PaeControlledPortStatus
_EtsysDot1xAuthAuthControlledPortStatus_Object = MibTableColumn
etsysDot1xAuthAuthControlledPortStatus = _EtsysDot1xAuthAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 5),
    _EtsysDot1xAuthAuthControlledPortStatus_Type()
)
etsysDot1xAuthAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthControlledPortStatus.setStatus("current")
_EtsysDot1xAuthAuthControlledPortControl_Type = PaeControlledPortControl
_EtsysDot1xAuthAuthControlledPortControl_Object = MibTableColumn
etsysDot1xAuthAuthControlledPortControl = _EtsysDot1xAuthAuthControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 6),
    _EtsysDot1xAuthAuthControlledPortControl_Type()
)
etsysDot1xAuthAuthControlledPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthControlledPortControl.setStatus("current")
_EtsysDot1xAuthQuietPeriod_Type = Unsigned32
_EtsysDot1xAuthQuietPeriod_Object = MibTableColumn
etsysDot1xAuthQuietPeriod = _EtsysDot1xAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 7),
    _EtsysDot1xAuthQuietPeriod_Type()
)
etsysDot1xAuthQuietPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthQuietPeriod.setStatus("current")
_EtsysDot1xAuthTxPeriod_Type = Unsigned32
_EtsysDot1xAuthTxPeriod_Object = MibTableColumn
etsysDot1xAuthTxPeriod = _EtsysDot1xAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 8),
    _EtsysDot1xAuthTxPeriod_Type()
)
etsysDot1xAuthTxPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthTxPeriod.setStatus("current")
_EtsysDot1xAuthSuppTimeout_Type = Unsigned32
_EtsysDot1xAuthSuppTimeout_Object = MibTableColumn
etsysDot1xAuthSuppTimeout = _EtsysDot1xAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 9),
    _EtsysDot1xAuthSuppTimeout_Type()
)
etsysDot1xAuthSuppTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthSuppTimeout.setStatus("current")
_EtsysDot1xAuthServerTimeout_Type = Unsigned32
_EtsysDot1xAuthServerTimeout_Object = MibTableColumn
etsysDot1xAuthServerTimeout = _EtsysDot1xAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 10),
    _EtsysDot1xAuthServerTimeout_Type()
)
etsysDot1xAuthServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthServerTimeout.setStatus("current")
_EtsysDot1xAuthMaxReq_Type = Unsigned32
_EtsysDot1xAuthMaxReq_Object = MibTableColumn
etsysDot1xAuthMaxReq = _EtsysDot1xAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 11),
    _EtsysDot1xAuthMaxReq_Type()
)
etsysDot1xAuthMaxReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthMaxReq.setStatus("current")
_EtsysDot1xAuthReAuthPeriod_Type = Unsigned32
_EtsysDot1xAuthReAuthPeriod_Object = MibTableColumn
etsysDot1xAuthReAuthPeriod = _EtsysDot1xAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 12),
    _EtsysDot1xAuthReAuthPeriod_Type()
)
etsysDot1xAuthReAuthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthReAuthPeriod.setStatus("current")


class _EtsysDot1xAuthReAuthEnabled_Type(TruthValue):
    """Custom type etsysDot1xAuthReAuthEnabled based on TruthValue"""


_EtsysDot1xAuthReAuthEnabled_Object = MibTableColumn
etsysDot1xAuthReAuthEnabled = _EtsysDot1xAuthReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 13),
    _EtsysDot1xAuthReAuthEnabled_Type()
)
etsysDot1xAuthReAuthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthReAuthEnabled.setStatus("current")
_EtsysDot1xAuthKeyTxEnabled_Type = TruthValue
_EtsysDot1xAuthKeyTxEnabled_Object = MibTableColumn
etsysDot1xAuthKeyTxEnabled = _EtsysDot1xAuthKeyTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 2, 1, 14),
    _EtsysDot1xAuthKeyTxEnabled_Type()
)
etsysDot1xAuthKeyTxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthKeyTxEnabled.setStatus("current")
_EtsysDot1xAuthStatsTable_Object = MibTable
etsysDot1xAuthStatsTable = _EtsysDot1xAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    etsysDot1xAuthStatsTable.setStatus("current")
_EtsysDot1xAuthStatsEntry_Object = MibTableRow
etsysDot1xAuthStatsEntry = _EtsysDot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1)
)
etsysDot1xAuthStatsEntry.setIndexNames(
    (0, "ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthStationAddress"),
)
if mibBuilder.loadTexts:
    etsysDot1xAuthStatsEntry.setStatus("current")
_EtsysDot1xAuthEapolFramesRx_Type = Counter32
_EtsysDot1xAuthEapolFramesRx_Object = MibTableColumn
etsysDot1xAuthEapolFramesRx = _EtsysDot1xAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 1),
    _EtsysDot1xAuthEapolFramesRx_Type()
)
etsysDot1xAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEapolFramesRx.setStatus("current")
_EtsysDot1xAuthEapolFramesTx_Type = Counter32
_EtsysDot1xAuthEapolFramesTx_Object = MibTableColumn
etsysDot1xAuthEapolFramesTx = _EtsysDot1xAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 2),
    _EtsysDot1xAuthEapolFramesTx_Type()
)
etsysDot1xAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEapolFramesTx.setStatus("current")
_EtsysDot1xAuthEapolStartFramesRx_Type = Counter32
_EtsysDot1xAuthEapolStartFramesRx_Object = MibTableColumn
etsysDot1xAuthEapolStartFramesRx = _EtsysDot1xAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 3),
    _EtsysDot1xAuthEapolStartFramesRx_Type()
)
etsysDot1xAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEapolStartFramesRx.setStatus("current")
_EtsysDot1xAuthEapolLogoffFramesRx_Type = Counter32
_EtsysDot1xAuthEapolLogoffFramesRx_Object = MibTableColumn
etsysDot1xAuthEapolLogoffFramesRx = _EtsysDot1xAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 4),
    _EtsysDot1xAuthEapolLogoffFramesRx_Type()
)
etsysDot1xAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEapolLogoffFramesRx.setStatus("current")
_EtsysDot1xAuthEapolRespIdFramesRx_Type = Counter32
_EtsysDot1xAuthEapolRespIdFramesRx_Object = MibTableColumn
etsysDot1xAuthEapolRespIdFramesRx = _EtsysDot1xAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 5),
    _EtsysDot1xAuthEapolRespIdFramesRx_Type()
)
etsysDot1xAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEapolRespIdFramesRx.setStatus("current")
_EtsysDot1xAuthEapolRespFramesRx_Type = Counter32
_EtsysDot1xAuthEapolRespFramesRx_Object = MibTableColumn
etsysDot1xAuthEapolRespFramesRx = _EtsysDot1xAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 6),
    _EtsysDot1xAuthEapolRespFramesRx_Type()
)
etsysDot1xAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEapolRespFramesRx.setStatus("current")
_EtsysDot1xAuthEapolReqIdFramesTx_Type = Counter32
_EtsysDot1xAuthEapolReqIdFramesTx_Object = MibTableColumn
etsysDot1xAuthEapolReqIdFramesTx = _EtsysDot1xAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 7),
    _EtsysDot1xAuthEapolReqIdFramesTx_Type()
)
etsysDot1xAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEapolReqIdFramesTx.setStatus("current")
_EtsysDot1xAuthEapolReqFramesTx_Type = Counter32
_EtsysDot1xAuthEapolReqFramesTx_Object = MibTableColumn
etsysDot1xAuthEapolReqFramesTx = _EtsysDot1xAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 8),
    _EtsysDot1xAuthEapolReqFramesTx_Type()
)
etsysDot1xAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEapolReqFramesTx.setStatus("current")
_EtsysDot1xAuthInvalidEapolFramesRx_Type = Counter32
_EtsysDot1xAuthInvalidEapolFramesRx_Object = MibTableColumn
etsysDot1xAuthInvalidEapolFramesRx = _EtsysDot1xAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 9),
    _EtsysDot1xAuthInvalidEapolFramesRx_Type()
)
etsysDot1xAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthInvalidEapolFramesRx.setStatus("current")
_EtsysDot1xAuthEapLengthErrorFramesRx_Type = Counter32
_EtsysDot1xAuthEapLengthErrorFramesRx_Object = MibTableColumn
etsysDot1xAuthEapLengthErrorFramesRx = _EtsysDot1xAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 10),
    _EtsysDot1xAuthEapLengthErrorFramesRx_Type()
)
etsysDot1xAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEapLengthErrorFramesRx.setStatus("current")
_EtsysDot1xAuthLastEapolFrameVersion_Type = Unsigned32
_EtsysDot1xAuthLastEapolFrameVersion_Object = MibTableColumn
etsysDot1xAuthLastEapolFrameVersion = _EtsysDot1xAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 11),
    _EtsysDot1xAuthLastEapolFrameVersion_Type()
)
etsysDot1xAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthLastEapolFrameVersion.setStatus("current")
_EtsysDot1xAuthLastEapolFrameSource_Type = MacAddress
_EtsysDot1xAuthLastEapolFrameSource_Object = MibTableColumn
etsysDot1xAuthLastEapolFrameSource = _EtsysDot1xAuthLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 3, 1, 12),
    _EtsysDot1xAuthLastEapolFrameSource_Type()
)
etsysDot1xAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthLastEapolFrameSource.setStatus("deprecated")
_EtsysDot1xAuthDiagTable_Object = MibTable
etsysDot1xAuthDiagTable = _EtsysDot1xAuthDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    etsysDot1xAuthDiagTable.setStatus("current")
_EtsysDot1xAuthDiagEntry_Object = MibTableRow
etsysDot1xAuthDiagEntry = _EtsysDot1xAuthDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1)
)
etsysDot1xAuthDiagEntry.setIndexNames(
    (0, "ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthStationAddress"),
)
if mibBuilder.loadTexts:
    etsysDot1xAuthDiagEntry.setStatus("current")
_EtsysDot1xAuthEntersConnecting_Type = Counter32
_EtsysDot1xAuthEntersConnecting_Object = MibTableColumn
etsysDot1xAuthEntersConnecting = _EtsysDot1xAuthEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 1),
    _EtsysDot1xAuthEntersConnecting_Type()
)
etsysDot1xAuthEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEntersConnecting.setStatus("current")
_EtsysDot1xAuthEapLogoffsWhileConnecting_Type = Counter32
_EtsysDot1xAuthEapLogoffsWhileConnecting_Object = MibTableColumn
etsysDot1xAuthEapLogoffsWhileConnecting = _EtsysDot1xAuthEapLogoffsWhileConnecting_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 2),
    _EtsysDot1xAuthEapLogoffsWhileConnecting_Type()
)
etsysDot1xAuthEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEapLogoffsWhileConnecting.setStatus("current")
_EtsysDot1xAuthEntersAuthenticating_Type = Counter32
_EtsysDot1xAuthEntersAuthenticating_Object = MibTableColumn
etsysDot1xAuthEntersAuthenticating = _EtsysDot1xAuthEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 3),
    _EtsysDot1xAuthEntersAuthenticating_Type()
)
etsysDot1xAuthEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthEntersAuthenticating.setStatus("current")
_EtsysDot1xAuthAuthSuccessWhileAuthenticating_Type = Counter32
_EtsysDot1xAuthAuthSuccessWhileAuthenticating_Object = MibTableColumn
etsysDot1xAuthAuthSuccessWhileAuthenticating = _EtsysDot1xAuthAuthSuccessWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 4),
    _EtsysDot1xAuthAuthSuccessWhileAuthenticating_Type()
)
etsysDot1xAuthAuthSuccessWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthSuccessWhileAuthenticating.setStatus("current")
_EtsysDot1xAuthAuthTimeoutsWhileAuthenticating_Type = Counter32
_EtsysDot1xAuthAuthTimeoutsWhileAuthenticating_Object = MibTableColumn
etsysDot1xAuthAuthTimeoutsWhileAuthenticating = _EtsysDot1xAuthAuthTimeoutsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 5),
    _EtsysDot1xAuthAuthTimeoutsWhileAuthenticating_Type()
)
etsysDot1xAuthAuthTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthTimeoutsWhileAuthenticating.setStatus("current")
_EtsysDot1xAuthAuthFailWhileAuthenticating_Type = Counter32
_EtsysDot1xAuthAuthFailWhileAuthenticating_Object = MibTableColumn
etsysDot1xAuthAuthFailWhileAuthenticating = _EtsysDot1xAuthAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 6),
    _EtsysDot1xAuthAuthFailWhileAuthenticating_Type()
)
etsysDot1xAuthAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthFailWhileAuthenticating.setStatus("current")
_EtsysDot1xAuthAuthReauthsWhileAuthenticating_Type = Counter32
_EtsysDot1xAuthAuthReauthsWhileAuthenticating_Object = MibTableColumn
etsysDot1xAuthAuthReauthsWhileAuthenticating = _EtsysDot1xAuthAuthReauthsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 7),
    _EtsysDot1xAuthAuthReauthsWhileAuthenticating_Type()
)
etsysDot1xAuthAuthReauthsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthReauthsWhileAuthenticating.setStatus("current")
_EtsysDot1xAuthAuthEapStartsWhileAuthenticating_Type = Counter32
_EtsysDot1xAuthAuthEapStartsWhileAuthenticating_Object = MibTableColumn
etsysDot1xAuthAuthEapStartsWhileAuthenticating = _EtsysDot1xAuthAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 8),
    _EtsysDot1xAuthAuthEapStartsWhileAuthenticating_Type()
)
etsysDot1xAuthAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthEapStartsWhileAuthenticating.setStatus("current")
_EtsysDot1xAuthAuthEapLogoffWhileAuthenticating_Type = Counter32
_EtsysDot1xAuthAuthEapLogoffWhileAuthenticating_Object = MibTableColumn
etsysDot1xAuthAuthEapLogoffWhileAuthenticating = _EtsysDot1xAuthAuthEapLogoffWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 9),
    _EtsysDot1xAuthAuthEapLogoffWhileAuthenticating_Type()
)
etsysDot1xAuthAuthEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthEapLogoffWhileAuthenticating.setStatus("current")
_EtsysDot1xAuthAuthReauthsWhileAuthenticated_Type = Counter32
_EtsysDot1xAuthAuthReauthsWhileAuthenticated_Object = MibTableColumn
etsysDot1xAuthAuthReauthsWhileAuthenticated = _EtsysDot1xAuthAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 10),
    _EtsysDot1xAuthAuthReauthsWhileAuthenticated_Type()
)
etsysDot1xAuthAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthReauthsWhileAuthenticated.setStatus("current")
_EtsysDot1xAuthAuthEapStartsWhileAuthenticated_Type = Counter32
_EtsysDot1xAuthAuthEapStartsWhileAuthenticated_Object = MibTableColumn
etsysDot1xAuthAuthEapStartsWhileAuthenticated = _EtsysDot1xAuthAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 11),
    _EtsysDot1xAuthAuthEapStartsWhileAuthenticated_Type()
)
etsysDot1xAuthAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthEapStartsWhileAuthenticated.setStatus("current")
_EtsysDot1xAuthAuthEapLogoffWhileAuthenticated_Type = Counter32
_EtsysDot1xAuthAuthEapLogoffWhileAuthenticated_Object = MibTableColumn
etsysDot1xAuthAuthEapLogoffWhileAuthenticated = _EtsysDot1xAuthAuthEapLogoffWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 12),
    _EtsysDot1xAuthAuthEapLogoffWhileAuthenticated_Type()
)
etsysDot1xAuthAuthEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthAuthEapLogoffWhileAuthenticated.setStatus("current")
_EtsysDot1xAuthBackendResponses_Type = Counter32
_EtsysDot1xAuthBackendResponses_Object = MibTableColumn
etsysDot1xAuthBackendResponses = _EtsysDot1xAuthBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 13),
    _EtsysDot1xAuthBackendResponses_Type()
)
etsysDot1xAuthBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthBackendResponses.setStatus("current")
_EtsysDot1xAuthBackendAccessChallenges_Type = Counter32
_EtsysDot1xAuthBackendAccessChallenges_Object = MibTableColumn
etsysDot1xAuthBackendAccessChallenges = _EtsysDot1xAuthBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 14),
    _EtsysDot1xAuthBackendAccessChallenges_Type()
)
etsysDot1xAuthBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthBackendAccessChallenges.setStatus("current")
_EtsysDot1xAuthBackendOtherRequestsToSupplicant_Type = Counter32
_EtsysDot1xAuthBackendOtherRequestsToSupplicant_Object = MibTableColumn
etsysDot1xAuthBackendOtherRequestsToSupplicant = _EtsysDot1xAuthBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 15),
    _EtsysDot1xAuthBackendOtherRequestsToSupplicant_Type()
)
etsysDot1xAuthBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthBackendOtherRequestsToSupplicant.setStatus("current")
_EtsysDot1xAuthBackendNonNakResponsesFromSupplicant_Type = Counter32
_EtsysDot1xAuthBackendNonNakResponsesFromSupplicant_Object = MibTableColumn
etsysDot1xAuthBackendNonNakResponsesFromSupplicant = _EtsysDot1xAuthBackendNonNakResponsesFromSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 16),
    _EtsysDot1xAuthBackendNonNakResponsesFromSupplicant_Type()
)
etsysDot1xAuthBackendNonNakResponsesFromSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthBackendNonNakResponsesFromSupplicant.setStatus("current")
_EtsysDot1xAuthBackendAuthSuccesses_Type = Counter32
_EtsysDot1xAuthBackendAuthSuccesses_Object = MibTableColumn
etsysDot1xAuthBackendAuthSuccesses = _EtsysDot1xAuthBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 17),
    _EtsysDot1xAuthBackendAuthSuccesses_Type()
)
etsysDot1xAuthBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthBackendAuthSuccesses.setStatus("current")
_EtsysDot1xAuthBackendAuthFails_Type = Counter32
_EtsysDot1xAuthBackendAuthFails_Object = MibTableColumn
etsysDot1xAuthBackendAuthFails = _EtsysDot1xAuthBackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 4, 1, 18),
    _EtsysDot1xAuthBackendAuthFails_Type()
)
etsysDot1xAuthBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthBackendAuthFails.setStatus("current")
_EtsysDot1xAuthSessionStatsTable_Object = MibTable
etsysDot1xAuthSessionStatsTable = _EtsysDot1xAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionStatsTable.setStatus("current")
_EtsysDot1xAuthSessionStatsEntry_Object = MibTableRow
etsysDot1xAuthSessionStatsEntry = _EtsysDot1xAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 5, 1)
)
etsysDot1xAuthSessionStatsEntry.setIndexNames(
    (0, "ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthStationAddress"),
)
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionStatsEntry.setStatus("current")
_EtsysDot1xAuthSessionOctetsRx_Type = Counter64
_EtsysDot1xAuthSessionOctetsRx_Object = MibTableColumn
etsysDot1xAuthSessionOctetsRx = _EtsysDot1xAuthSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 5, 1, 1),
    _EtsysDot1xAuthSessionOctetsRx_Type()
)
etsysDot1xAuthSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionOctetsRx.setStatus("current")
_EtsysDot1xAuthSessionOctetsTx_Type = Counter64
_EtsysDot1xAuthSessionOctetsTx_Object = MibTableColumn
etsysDot1xAuthSessionOctetsTx = _EtsysDot1xAuthSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 5, 1, 2),
    _EtsysDot1xAuthSessionOctetsTx_Type()
)
etsysDot1xAuthSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionOctetsTx.setStatus("current")
_EtsysDot1xAuthSessionFramesRx_Type = Counter32
_EtsysDot1xAuthSessionFramesRx_Object = MibTableColumn
etsysDot1xAuthSessionFramesRx = _EtsysDot1xAuthSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 5, 1, 3),
    _EtsysDot1xAuthSessionFramesRx_Type()
)
etsysDot1xAuthSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionFramesRx.setStatus("current")
_EtsysDot1xAuthSessionFramesTx_Type = Counter32
_EtsysDot1xAuthSessionFramesTx_Object = MibTableColumn
etsysDot1xAuthSessionFramesTx = _EtsysDot1xAuthSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 5, 1, 4),
    _EtsysDot1xAuthSessionFramesTx_Type()
)
etsysDot1xAuthSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionFramesTx.setStatus("current")
_EtsysDot1xAuthSessionId_Type = SnmpAdminString
_EtsysDot1xAuthSessionId_Object = MibTableColumn
etsysDot1xAuthSessionId = _EtsysDot1xAuthSessionId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 5, 1, 5),
    _EtsysDot1xAuthSessionId_Type()
)
etsysDot1xAuthSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionId.setStatus("current")


class _EtsysDot1xAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type etsysDot1xAuthSessionAuthenticMethod based on Integer32"""
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


_EtsysDot1xAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_EtsysDot1xAuthSessionAuthenticMethod_Object = MibTableColumn
etsysDot1xAuthSessionAuthenticMethod = _EtsysDot1xAuthSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 5, 1, 6),
    _EtsysDot1xAuthSessionAuthenticMethod_Type()
)
etsysDot1xAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionAuthenticMethod.setStatus("current")
_EtsysDot1xAuthSessionTime_Type = TimeTicks
_EtsysDot1xAuthSessionTime_Object = MibTableColumn
etsysDot1xAuthSessionTime = _EtsysDot1xAuthSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 5, 1, 7),
    _EtsysDot1xAuthSessionTime_Type()
)
etsysDot1xAuthSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionTime.setStatus("current")


class _EtsysDot1xAuthSessionTerminateCause_Type(Integer32):
    """Custom type etsysDot1xAuthSessionTerminateCause based on Integer32"""
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


_EtsysDot1xAuthSessionTerminateCause_Type.__name__ = "Integer32"
_EtsysDot1xAuthSessionTerminateCause_Object = MibTableColumn
etsysDot1xAuthSessionTerminateCause = _EtsysDot1xAuthSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 5, 1, 8),
    _EtsysDot1xAuthSessionTerminateCause_Type()
)
etsysDot1xAuthSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionTerminateCause.setStatus("current")


class _EtsysDot1xAuthStatsSupported_Type(Bits):
    """Custom type etsysDot1xAuthStatsSupported based on Bits"""
    namedValues = NamedValues(
        *(("etsysDot1xAuthEapLengthErrorFramesRxSupported", 9),
          ("etsysDot1xAuthEapolFramesRxSupported", 0),
          ("etsysDot1xAuthEapolFramesTxSupported", 1),
          ("etsysDot1xAuthEapolLogoffFramesRxSupported", 3),
          ("etsysDot1xAuthEapolReqFramesTxSupported", 7),
          ("etsysDot1xAuthEapolReqIdFramesTxSupported", 6),
          ("etsysDot1xAuthEapolRespFramesRxSupported", 5),
          ("etsysDot1xAuthEapolRespIdFramesRxSupported", 4),
          ("etsysDot1xAuthEapolStartFramesRxSupported", 2),
          ("etsysDot1xAuthInvalidEapolFramesRxSupported", 8),
          ("etsysDot1xAuthLastEapolFrameVersionSupported", 10))
    )

_EtsysDot1xAuthStatsSupported_Type.__name__ = "Bits"
_EtsysDot1xAuthStatsSupported_Object = MibScalar
etsysDot1xAuthStatsSupported = _EtsysDot1xAuthStatsSupported_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 6),
    _EtsysDot1xAuthStatsSupported_Type()
)
etsysDot1xAuthStatsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthStatsSupported.setStatus("current")


class _EtsysDot1xAuthDiagSupported_Type(Bits):
    """Custom type etsysDot1xAuthDiagSupported based on Bits"""
    namedValues = NamedValues(
        *(("etsysDot1xAuthAuthEapLogoffWhileAuthenticatedSupported", 11),
          ("etsysDot1xAuthAuthEapLogoffWhileAuthenticatingSupported", 8),
          ("etsysDot1xAuthAuthEapStartsWhileAuthenticatedSupported", 10),
          ("etsysDot1xAuthAuthEapStartsWhileAuthenticatingSupported", 7),
          ("etsysDot1xAuthAuthFailWhileAuthenticatingSupported", 5),
          ("etsysDot1xAuthAuthReauthsWhileAuthenticatedSupported", 9),
          ("etsysDot1xAuthAuthReauthsWhileAuthenticatingSupported", 6),
          ("etsysDot1xAuthAuthSuccessWhileAuthenticatingSupported", 3),
          ("etsysDot1xAuthAuthTimeoutsWhileAuthenticatingSupported", 4),
          ("etsysDot1xAuthBackendAccessChallengesSupported", 13),
          ("etsysDot1xAuthBackendAuthFailsSupported", 17),
          ("etsysDot1xAuthBackendAuthSuccessesSupported", 16),
          ("etsysDot1xAuthBackendNonNakResponsesFromSupplicantSupported", 15),
          ("etsysDot1xAuthBackendOtherRequestsToSupplicantSupported", 14),
          ("etsysDot1xAuthBackendResponsesSupported", 12),
          ("etsysDot1xAuthEapLogoffsWhileConnectingSupported", 1),
          ("etsysDot1xAuthEntersAuthenticatingSupported", 2),
          ("etsysDot1xAuthEntersConnectingSupported", 0))
    )

_EtsysDot1xAuthDiagSupported_Type.__name__ = "Bits"
_EtsysDot1xAuthDiagSupported_Object = MibScalar
etsysDot1xAuthDiagSupported = _EtsysDot1xAuthDiagSupported_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 7),
    _EtsysDot1xAuthDiagSupported_Type()
)
etsysDot1xAuthDiagSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthDiagSupported.setStatus("current")


class _EtsysDot1xAuthSessionSuppportedObjs_Type(Bits):
    """Custom type etsysDot1xAuthSessionSuppportedObjs based on Bits"""
    namedValues = NamedValues(
        *(("etsysDot1xAuthSessionAuthenticMethodSupported", 5),
          ("etsysDot1xAuthSessionFramesRxSupported", 2),
          ("etsysDot1xAuthSessionFramesTxSupported", 3),
          ("etsysDot1xAuthSessionIdSupported", 4),
          ("etsysDot1xAuthSessionOctetsRxSupported", 0),
          ("etsysDot1xAuthSessionOctetsTxSupported", 1),
          ("etsysDot1xAuthSessionTerminateCauseSupported", 7),
          ("etsysDot1xAuthSessionTimeSupported", 6))
    )

_EtsysDot1xAuthSessionSuppportedObjs_Type.__name__ = "Bits"
_EtsysDot1xAuthSessionSuppportedObjs_Object = MibScalar
etsysDot1xAuthSessionSuppportedObjs = _EtsysDot1xAuthSessionSuppportedObjs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 8),
    _EtsysDot1xAuthSessionSuppportedObjs_Type()
)
etsysDot1xAuthSessionSuppportedObjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionSuppportedObjs.setStatus("current")


class _EtsysDot1xMaxCapableAuthStations_Type(Unsigned32):
    """Custom type etsysDot1xMaxCapableAuthStations based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysDot1xMaxCapableAuthStations_Type.__name__ = "Unsigned32"
_EtsysDot1xMaxCapableAuthStations_Object = MibScalar
etsysDot1xMaxCapableAuthStations = _EtsysDot1xMaxCapableAuthStations_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 9),
    _EtsysDot1xMaxCapableAuthStations_Type()
)
etsysDot1xMaxCapableAuthStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xMaxCapableAuthStations.setStatus("current")


class _EtsysDot1xMaximumStationsStatsGathered_Type(Unsigned32):
    """Custom type etsysDot1xMaximumStationsStatsGathered based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysDot1xMaximumStationsStatsGathered_Type.__name__ = "Unsigned32"
_EtsysDot1xMaximumStationsStatsGathered_Object = MibScalar
etsysDot1xMaximumStationsStatsGathered = _EtsysDot1xMaximumStationsStatsGathered_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 10),
    _EtsysDot1xMaximumStationsStatsGathered_Type()
)
etsysDot1xMaximumStationsStatsGathered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xMaximumStationsStatsGathered.setStatus("current")


class _EtsysDot1xCurrentStationsStatsGathered_Type(Unsigned32):
    """Custom type etsysDot1xCurrentStationsStatsGathered based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysDot1xCurrentStationsStatsGathered_Type.__name__ = "Unsigned32"
_EtsysDot1xCurrentStationsStatsGathered_Object = MibScalar
etsysDot1xCurrentStationsStatsGathered = _EtsysDot1xCurrentStationsStatsGathered_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 11),
    _EtsysDot1xCurrentStationsStatsGathered_Type()
)
etsysDot1xCurrentStationsStatsGathered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot1xCurrentStationsStatsGathered.setStatus("current")
_EtsysDot1xAuthStationWatchTable_Object = MibTable
etsysDot1xAuthStationWatchTable = _EtsysDot1xAuthStationWatchTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 12)
)
if mibBuilder.loadTexts:
    etsysDot1xAuthStationWatchTable.setStatus("current")
_EtsysDot1xAuthStationWatchEntry_Object = MibTableRow
etsysDot1xAuthStationWatchEntry = _EtsysDot1xAuthStationWatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 12, 1)
)
etsysDot1xAuthStationWatchEntry.setIndexNames(
    (0, "ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthInfoStationAddress"),
)
if mibBuilder.loadTexts:
    etsysDot1xAuthStationWatchEntry.setStatus("current")
_EtsysDot1xAuthInfoStationAddress_Type = MacAddress
_EtsysDot1xAuthInfoStationAddress_Object = MibTableColumn
etsysDot1xAuthInfoStationAddress = _EtsysDot1xAuthInfoStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 12, 1, 1),
    _EtsysDot1xAuthInfoStationAddress_Type()
)
etsysDot1xAuthInfoStationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysDot1xAuthInfoStationAddress.setStatus("current")
_EtsysDot1xAuthInfoStationRowStatus_Type = RowStatus
_EtsysDot1xAuthInfoStationRowStatus_Object = MibTableColumn
etsysDot1xAuthInfoStationRowStatus = _EtsysDot1xAuthInfoStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 2, 1, 12, 1, 2),
    _EtsysDot1xAuthInfoStationRowStatus_Type()
)
etsysDot1xAuthInfoStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysDot1xAuthInfoStationRowStatus.setStatus("current")
_EtsysDot1xSupplicantBranch_ObjectIdentity = ObjectIdentity
etsysDot1xSupplicantBranch = _EtsysDot1xSupplicantBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 1, 3)
)
_EtsysDot1xConformance_ObjectIdentity = ObjectIdentity
etsysDot1xConformance = _EtsysDot1xConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 2)
)
_EtsysDot1xGroups_ObjectIdentity = ObjectIdentity
etsysDot1xGroups = _EtsysDot1xGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 2, 1)
)
_EtsysDot1xCompliances_ObjectIdentity = ObjectIdentity
etsysDot1xCompliances = _EtsysDot1xCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 2, 2)
)

# Managed Objects groups

etsysDot1xAuthStationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 2, 1, 1)
)
etsysDot1xAuthStationGroup.setObjects(
      *(("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthStationPaePort"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthStationPaeState"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthStationBackendAuthState"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthStationUserName"))
)
if mibBuilder.loadTexts:
    etsysDot1xAuthStationGroup.setStatus("current")

etsysDot1xAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 2, 1, 2)
)
etsysDot1xAuthConfigGroup.setObjects(
      *(("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthInitialize"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthReauthenticate"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAdminControlledDirections"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthOperControlledDirections"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthControlledPortStatus"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthControlledPortControl"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthQuietPeriod"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthTxPeriod"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthSuppTimeout"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthServerTimeout"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthMaxReq"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthReAuthPeriod"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthReAuthEnabled"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthKeyTxEnabled"))
)
if mibBuilder.loadTexts:
    etsysDot1xAuthConfigGroup.setStatus("current")

etsysDot1xAuthStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 2, 1, 3)
)
etsysDot1xAuthStatsGroup.setObjects(
      *(("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEapolFramesRx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEapolFramesTx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEapolStartFramesRx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEapolLogoffFramesRx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEapolRespIdFramesRx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEapolRespFramesRx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEapolReqIdFramesTx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEapolReqFramesTx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthInvalidEapolFramesRx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEapLengthErrorFramesRx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthLastEapolFrameVersion"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthLastEapolFrameSource"))
)
if mibBuilder.loadTexts:
    etsysDot1xAuthStatsGroup.setStatus("current")

etsysDot1xAuthDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 2, 1, 4)
)
etsysDot1xAuthDiagGroup.setObjects(
      *(("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEntersConnecting"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEapLogoffsWhileConnecting"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthEntersAuthenticating"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthSuccessWhileAuthenticating"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthTimeoutsWhileAuthenticating"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthFailWhileAuthenticating"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthReauthsWhileAuthenticating"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthEapStartsWhileAuthenticating"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthEapLogoffWhileAuthenticating"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthReauthsWhileAuthenticated"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthEapStartsWhileAuthenticated"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthAuthEapLogoffWhileAuthenticated"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthBackendResponses"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthBackendAccessChallenges"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthBackendOtherRequestsToSupplicant"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthBackendNonNakResponsesFromSupplicant"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthBackendAuthSuccesses"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthBackendAuthFails"))
)
if mibBuilder.loadTexts:
    etsysDot1xAuthDiagGroup.setStatus("current")

etsysDot1xAuthSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 2, 1, 5)
)
etsysDot1xAuthSessionStatsGroup.setObjects(
      *(("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthSessionOctetsRx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthSessionOctetsTx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthSessionFramesRx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthSessionFramesTx"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthSessionId"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthSessionAuthenticMethod"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthSessionTime"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthSessionTerminateCause"))
)
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionStatsGroup.setStatus("current")

etsysDot1xAuthSessionControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 2, 1, 6)
)
etsysDot1xAuthSessionControlGroup.setObjects(
      *(("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthSessionSuppportedObjs"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xMaxCapableAuthStations"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xCurrentStationsStatsGathered"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xMaximumStationsStatsGathered"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthInfoStationAddress"),
        ("ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthInfoStationRowStatus"))
)
if mibBuilder.loadTexts:
    etsysDot1xAuthSessionControlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysDot1xCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 18, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysDot1xCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-8021X-EXTENSIONS-MIB",
    **{"etsys8021xExtensionsMIB": etsys8021xExtensionsMIB,
       "etsysDot1xExtensionsObjects": etsysDot1xExtensionsObjects,
       "etsysDot1xSystemBranch": etsysDot1xSystemBranch,
       "etsysDot1xAuthenticatorBranch": etsysDot1xAuthenticatorBranch,
       "etsysDot1xAuthStationBranch": etsysDot1xAuthStationBranch,
       "etsysDot1xAuthStationTable": etsysDot1xAuthStationTable,
       "etsysDot1xAuthStationEntry": etsysDot1xAuthStationEntry,
       "etsysDot1xAuthStationAddress": etsysDot1xAuthStationAddress,
       "etsysDot1xAuthStationPaePort": etsysDot1xAuthStationPaePort,
       "etsysDot1xAuthStationPaeState": etsysDot1xAuthStationPaeState,
       "etsysDot1xAuthStationBackendAuthState": etsysDot1xAuthStationBackendAuthState,
       "etsysDot1xAuthStationUserName": etsysDot1xAuthStationUserName,
       "etsysDot1xAuthConfigTable": etsysDot1xAuthConfigTable,
       "etsysDot1xAuthConfigEntry": etsysDot1xAuthConfigEntry,
       "etsysDot1xAuthInitialize": etsysDot1xAuthInitialize,
       "etsysDot1xAuthReauthenticate": etsysDot1xAuthReauthenticate,
       "etsysDot1xAuthAdminControlledDirections": etsysDot1xAuthAdminControlledDirections,
       "etsysDot1xAuthOperControlledDirections": etsysDot1xAuthOperControlledDirections,
       "etsysDot1xAuthAuthControlledPortStatus": etsysDot1xAuthAuthControlledPortStatus,
       "etsysDot1xAuthAuthControlledPortControl": etsysDot1xAuthAuthControlledPortControl,
       "etsysDot1xAuthQuietPeriod": etsysDot1xAuthQuietPeriod,
       "etsysDot1xAuthTxPeriod": etsysDot1xAuthTxPeriod,
       "etsysDot1xAuthSuppTimeout": etsysDot1xAuthSuppTimeout,
       "etsysDot1xAuthServerTimeout": etsysDot1xAuthServerTimeout,
       "etsysDot1xAuthMaxReq": etsysDot1xAuthMaxReq,
       "etsysDot1xAuthReAuthPeriod": etsysDot1xAuthReAuthPeriod,
       "etsysDot1xAuthReAuthEnabled": etsysDot1xAuthReAuthEnabled,
       "etsysDot1xAuthKeyTxEnabled": etsysDot1xAuthKeyTxEnabled,
       "etsysDot1xAuthStatsTable": etsysDot1xAuthStatsTable,
       "etsysDot1xAuthStatsEntry": etsysDot1xAuthStatsEntry,
       "etsysDot1xAuthEapolFramesRx": etsysDot1xAuthEapolFramesRx,
       "etsysDot1xAuthEapolFramesTx": etsysDot1xAuthEapolFramesTx,
       "etsysDot1xAuthEapolStartFramesRx": etsysDot1xAuthEapolStartFramesRx,
       "etsysDot1xAuthEapolLogoffFramesRx": etsysDot1xAuthEapolLogoffFramesRx,
       "etsysDot1xAuthEapolRespIdFramesRx": etsysDot1xAuthEapolRespIdFramesRx,
       "etsysDot1xAuthEapolRespFramesRx": etsysDot1xAuthEapolRespFramesRx,
       "etsysDot1xAuthEapolReqIdFramesTx": etsysDot1xAuthEapolReqIdFramesTx,
       "etsysDot1xAuthEapolReqFramesTx": etsysDot1xAuthEapolReqFramesTx,
       "etsysDot1xAuthInvalidEapolFramesRx": etsysDot1xAuthInvalidEapolFramesRx,
       "etsysDot1xAuthEapLengthErrorFramesRx": etsysDot1xAuthEapLengthErrorFramesRx,
       "etsysDot1xAuthLastEapolFrameVersion": etsysDot1xAuthLastEapolFrameVersion,
       "etsysDot1xAuthLastEapolFrameSource": etsysDot1xAuthLastEapolFrameSource,
       "etsysDot1xAuthDiagTable": etsysDot1xAuthDiagTable,
       "etsysDot1xAuthDiagEntry": etsysDot1xAuthDiagEntry,
       "etsysDot1xAuthEntersConnecting": etsysDot1xAuthEntersConnecting,
       "etsysDot1xAuthEapLogoffsWhileConnecting": etsysDot1xAuthEapLogoffsWhileConnecting,
       "etsysDot1xAuthEntersAuthenticating": etsysDot1xAuthEntersAuthenticating,
       "etsysDot1xAuthAuthSuccessWhileAuthenticating": etsysDot1xAuthAuthSuccessWhileAuthenticating,
       "etsysDot1xAuthAuthTimeoutsWhileAuthenticating": etsysDot1xAuthAuthTimeoutsWhileAuthenticating,
       "etsysDot1xAuthAuthFailWhileAuthenticating": etsysDot1xAuthAuthFailWhileAuthenticating,
       "etsysDot1xAuthAuthReauthsWhileAuthenticating": etsysDot1xAuthAuthReauthsWhileAuthenticating,
       "etsysDot1xAuthAuthEapStartsWhileAuthenticating": etsysDot1xAuthAuthEapStartsWhileAuthenticating,
       "etsysDot1xAuthAuthEapLogoffWhileAuthenticating": etsysDot1xAuthAuthEapLogoffWhileAuthenticating,
       "etsysDot1xAuthAuthReauthsWhileAuthenticated": etsysDot1xAuthAuthReauthsWhileAuthenticated,
       "etsysDot1xAuthAuthEapStartsWhileAuthenticated": etsysDot1xAuthAuthEapStartsWhileAuthenticated,
       "etsysDot1xAuthAuthEapLogoffWhileAuthenticated": etsysDot1xAuthAuthEapLogoffWhileAuthenticated,
       "etsysDot1xAuthBackendResponses": etsysDot1xAuthBackendResponses,
       "etsysDot1xAuthBackendAccessChallenges": etsysDot1xAuthBackendAccessChallenges,
       "etsysDot1xAuthBackendOtherRequestsToSupplicant": etsysDot1xAuthBackendOtherRequestsToSupplicant,
       "etsysDot1xAuthBackendNonNakResponsesFromSupplicant": etsysDot1xAuthBackendNonNakResponsesFromSupplicant,
       "etsysDot1xAuthBackendAuthSuccesses": etsysDot1xAuthBackendAuthSuccesses,
       "etsysDot1xAuthBackendAuthFails": etsysDot1xAuthBackendAuthFails,
       "etsysDot1xAuthSessionStatsTable": etsysDot1xAuthSessionStatsTable,
       "etsysDot1xAuthSessionStatsEntry": etsysDot1xAuthSessionStatsEntry,
       "etsysDot1xAuthSessionOctetsRx": etsysDot1xAuthSessionOctetsRx,
       "etsysDot1xAuthSessionOctetsTx": etsysDot1xAuthSessionOctetsTx,
       "etsysDot1xAuthSessionFramesRx": etsysDot1xAuthSessionFramesRx,
       "etsysDot1xAuthSessionFramesTx": etsysDot1xAuthSessionFramesTx,
       "etsysDot1xAuthSessionId": etsysDot1xAuthSessionId,
       "etsysDot1xAuthSessionAuthenticMethod": etsysDot1xAuthSessionAuthenticMethod,
       "etsysDot1xAuthSessionTime": etsysDot1xAuthSessionTime,
       "etsysDot1xAuthSessionTerminateCause": etsysDot1xAuthSessionTerminateCause,
       "etsysDot1xAuthStatsSupported": etsysDot1xAuthStatsSupported,
       "etsysDot1xAuthDiagSupported": etsysDot1xAuthDiagSupported,
       "etsysDot1xAuthSessionSuppportedObjs": etsysDot1xAuthSessionSuppportedObjs,
       "etsysDot1xMaxCapableAuthStations": etsysDot1xMaxCapableAuthStations,
       "etsysDot1xMaximumStationsStatsGathered": etsysDot1xMaximumStationsStatsGathered,
       "etsysDot1xCurrentStationsStatsGathered": etsysDot1xCurrentStationsStatsGathered,
       "etsysDot1xAuthStationWatchTable": etsysDot1xAuthStationWatchTable,
       "etsysDot1xAuthStationWatchEntry": etsysDot1xAuthStationWatchEntry,
       "etsysDot1xAuthInfoStationAddress": etsysDot1xAuthInfoStationAddress,
       "etsysDot1xAuthInfoStationRowStatus": etsysDot1xAuthInfoStationRowStatus,
       "etsysDot1xSupplicantBranch": etsysDot1xSupplicantBranch,
       "etsysDot1xConformance": etsysDot1xConformance,
       "etsysDot1xGroups": etsysDot1xGroups,
       "etsysDot1xAuthStationGroup": etsysDot1xAuthStationGroup,
       "etsysDot1xAuthConfigGroup": etsysDot1xAuthConfigGroup,
       "etsysDot1xAuthStatsGroup": etsysDot1xAuthStatsGroup,
       "etsysDot1xAuthDiagGroup": etsysDot1xAuthDiagGroup,
       "etsysDot1xAuthSessionStatsGroup": etsysDot1xAuthSessionStatsGroup,
       "etsysDot1xAuthSessionControlGroup": etsysDot1xAuthSessionControlGroup,
       "etsysDot1xCompliances": etsysDot1xCompliances,
       "etsysDot1xCompliance": etsysDot1xCompliance}
)
