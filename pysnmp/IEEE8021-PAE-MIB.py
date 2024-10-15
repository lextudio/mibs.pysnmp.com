# SNMP MIB module (IEEE8021-PAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-PAE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:14 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021paeMIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PaeControlledDirections(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("in", 1))
    )



class PaeControlledPortStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2))
    )



class PaeControlledPortControl(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceAuthorized", 3),
          ("forceUnauthorized", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PaeMIBObjects_ObjectIdentity = ObjectIdentity
paeMIBObjects = _PaeMIBObjects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 1, 1)
)
_Dot1xPaeSystem_ObjectIdentity = ObjectIdentity
dot1xPaeSystem = _Dot1xPaeSystem_ObjectIdentity(
    (1, 0, 8802, 1, 1, 1, 1, 1)
)


class _Dot1xPaeSystemAuthControl_Type(Integer32):
    """Custom type dot1xPaeSystemAuthControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Dot1xPaeSystemAuthControl_Type.__name__ = "Integer32"
_Dot1xPaeSystemAuthControl_Object = MibScalar
dot1xPaeSystemAuthControl = _Dot1xPaeSystemAuthControl_Object(
    (1, 0, 8802, 1, 1, 1, 1, 1, 1),
    _Dot1xPaeSystemAuthControl_Type()
)
dot1xPaeSystemAuthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPaeSystemAuthControl.setStatus("current")
_Dot1xPaePortTable_Object = MibTable
dot1xPaePortTable = _Dot1xPaePortTable_Object(
    (1, 0, 8802, 1, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot1xPaePortTable.setStatus("current")
_Dot1xPaePortEntry_Object = MibTableRow
dot1xPaePortEntry = _Dot1xPaePortEntry_Object(
    (1, 0, 8802, 1, 1, 1, 1, 1, 2, 1)
)
dot1xPaePortEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xPaePortEntry.setStatus("current")
_Dot1xPaePortNumber_Type = InterfaceIndex
_Dot1xPaePortNumber_Object = MibTableColumn
dot1xPaePortNumber = _Dot1xPaePortNumber_Object(
    (1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 1),
    _Dot1xPaePortNumber_Type()
)
dot1xPaePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1xPaePortNumber.setStatus("current")
_Dot1xPaePortProtocolVersion_Type = Unsigned32
_Dot1xPaePortProtocolVersion_Object = MibTableColumn
dot1xPaePortProtocolVersion = _Dot1xPaePortProtocolVersion_Object(
    (1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 2),
    _Dot1xPaePortProtocolVersion_Type()
)
dot1xPaePortProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xPaePortProtocolVersion.setStatus("current")


class _Dot1xPaePortCapabilities_Type(Bits):
    """Custom type dot1xPaePortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot1xPaePortAuthCapable", 0),
          ("dot1xPaePortSuppCapable", 1))
    )

_Dot1xPaePortCapabilities_Type.__name__ = "Bits"
_Dot1xPaePortCapabilities_Object = MibTableColumn
dot1xPaePortCapabilities = _Dot1xPaePortCapabilities_Object(
    (1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 3),
    _Dot1xPaePortCapabilities_Type()
)
dot1xPaePortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xPaePortCapabilities.setStatus("current")
_Dot1xPaePortInitialize_Type = TruthValue
_Dot1xPaePortInitialize_Object = MibTableColumn
dot1xPaePortInitialize = _Dot1xPaePortInitialize_Object(
    (1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 4),
    _Dot1xPaePortInitialize_Type()
)
dot1xPaePortInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPaePortInitialize.setStatus("current")
_Dot1xPaePortReauthenticate_Type = TruthValue
_Dot1xPaePortReauthenticate_Object = MibTableColumn
dot1xPaePortReauthenticate = _Dot1xPaePortReauthenticate_Object(
    (1, 0, 8802, 1, 1, 1, 1, 1, 2, 1, 5),
    _Dot1xPaePortReauthenticate_Type()
)
dot1xPaePortReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPaePortReauthenticate.setStatus("current")
_Dot1xPaeAuthenticator_ObjectIdentity = ObjectIdentity
dot1xPaeAuthenticator = _Dot1xPaeAuthenticator_ObjectIdentity(
    (1, 0, 8802, 1, 1, 1, 1, 2)
)
_Dot1xAuthConfigTable_Object = MibTable
dot1xAuthConfigTable = _Dot1xAuthConfigTable_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigTable.setStatus("current")
_Dot1xAuthConfigEntry_Object = MibTableRow
dot1xAuthConfigEntry = _Dot1xAuthConfigEntry_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1)
)
dot1xAuthConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xAuthConfigEntry.setStatus("current")


class _Dot1xAuthPaeState_Type(Integer32):
    """Custom type dot1xAuthPaeState based on Integer32"""
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


_Dot1xAuthPaeState_Type.__name__ = "Integer32"
_Dot1xAuthPaeState_Object = MibTableColumn
dot1xAuthPaeState = _Dot1xAuthPaeState_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 1),
    _Dot1xAuthPaeState_Type()
)
dot1xAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthPaeState.setStatus("current")


class _Dot1xAuthBackendAuthState_Type(Integer32):
    """Custom type dot1xAuthBackendAuthState based on Integer32"""
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


_Dot1xAuthBackendAuthState_Type.__name__ = "Integer32"
_Dot1xAuthBackendAuthState_Object = MibTableColumn
dot1xAuthBackendAuthState = _Dot1xAuthBackendAuthState_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 2),
    _Dot1xAuthBackendAuthState_Type()
)
dot1xAuthBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendAuthState.setStatus("current")
_Dot1xAuthAdminControlledDirections_Type = PaeControlledDirections
_Dot1xAuthAdminControlledDirections_Object = MibTableColumn
dot1xAuthAdminControlledDirections = _Dot1xAuthAdminControlledDirections_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 3),
    _Dot1xAuthAdminControlledDirections_Type()
)
dot1xAuthAdminControlledDirections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthAdminControlledDirections.setStatus("current")
_Dot1xAuthOperControlledDirections_Type = PaeControlledDirections
_Dot1xAuthOperControlledDirections_Object = MibTableColumn
dot1xAuthOperControlledDirections = _Dot1xAuthOperControlledDirections_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 4),
    _Dot1xAuthOperControlledDirections_Type()
)
dot1xAuthOperControlledDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthOperControlledDirections.setStatus("current")
_Dot1xAuthAuthControlledPortStatus_Type = PaeControlledPortStatus
_Dot1xAuthAuthControlledPortStatus_Object = MibTableColumn
dot1xAuthAuthControlledPortStatus = _Dot1xAuthAuthControlledPortStatus_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 5),
    _Dot1xAuthAuthControlledPortStatus_Type()
)
dot1xAuthAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthControlledPortStatus.setStatus("current")
_Dot1xAuthAuthControlledPortControl_Type = PaeControlledPortControl
_Dot1xAuthAuthControlledPortControl_Object = MibTableColumn
dot1xAuthAuthControlledPortControl = _Dot1xAuthAuthControlledPortControl_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 6),
    _Dot1xAuthAuthControlledPortControl_Type()
)
dot1xAuthAuthControlledPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthAuthControlledPortControl.setStatus("current")


class _Dot1xAuthQuietPeriod_Type(Unsigned32):
    """Custom type dot1xAuthQuietPeriod based on Unsigned32"""
    defaultValue = 60


_Dot1xAuthQuietPeriod_Object = MibTableColumn
dot1xAuthQuietPeriod = _Dot1xAuthQuietPeriod_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 7),
    _Dot1xAuthQuietPeriod_Type()
)
dot1xAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthQuietPeriod.setStatus("current")


class _Dot1xAuthTxPeriod_Type(Unsigned32):
    """Custom type dot1xAuthTxPeriod based on Unsigned32"""
    defaultValue = 30


_Dot1xAuthTxPeriod_Object = MibTableColumn
dot1xAuthTxPeriod = _Dot1xAuthTxPeriod_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 8),
    _Dot1xAuthTxPeriod_Type()
)
dot1xAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthTxPeriod.setStatus("current")


class _Dot1xAuthSuppTimeout_Type(Unsigned32):
    """Custom type dot1xAuthSuppTimeout based on Unsigned32"""
    defaultValue = 30


_Dot1xAuthSuppTimeout_Object = MibTableColumn
dot1xAuthSuppTimeout = _Dot1xAuthSuppTimeout_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 9),
    _Dot1xAuthSuppTimeout_Type()
)
dot1xAuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthSuppTimeout.setStatus("current")


class _Dot1xAuthServerTimeout_Type(Unsigned32):
    """Custom type dot1xAuthServerTimeout based on Unsigned32"""
    defaultValue = 30


_Dot1xAuthServerTimeout_Object = MibTableColumn
dot1xAuthServerTimeout = _Dot1xAuthServerTimeout_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 10),
    _Dot1xAuthServerTimeout_Type()
)
dot1xAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthServerTimeout.setStatus("current")


class _Dot1xAuthMaxReq_Type(Unsigned32):
    """Custom type dot1xAuthMaxReq based on Unsigned32"""
    defaultValue = 2


_Dot1xAuthMaxReq_Object = MibTableColumn
dot1xAuthMaxReq = _Dot1xAuthMaxReq_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 11),
    _Dot1xAuthMaxReq_Type()
)
dot1xAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthMaxReq.setStatus("current")


class _Dot1xAuthReAuthPeriod_Type(Unsigned32):
    """Custom type dot1xAuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_Dot1xAuthReAuthPeriod_Object = MibTableColumn
dot1xAuthReAuthPeriod = _Dot1xAuthReAuthPeriod_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 12),
    _Dot1xAuthReAuthPeriod_Type()
)
dot1xAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthReAuthPeriod.setStatus("current")


class _Dot1xAuthReAuthEnabled_Type(TruthValue):
    """Custom type dot1xAuthReAuthEnabled based on TruthValue"""


_Dot1xAuthReAuthEnabled_Object = MibTableColumn
dot1xAuthReAuthEnabled = _Dot1xAuthReAuthEnabled_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 13),
    _Dot1xAuthReAuthEnabled_Type()
)
dot1xAuthReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthReAuthEnabled.setStatus("current")
_Dot1xAuthKeyTxEnabled_Type = TruthValue
_Dot1xAuthKeyTxEnabled_Object = MibTableColumn
dot1xAuthKeyTxEnabled = _Dot1xAuthKeyTxEnabled_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 1, 1, 14),
    _Dot1xAuthKeyTxEnabled_Type()
)
dot1xAuthKeyTxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthKeyTxEnabled.setStatus("current")
_Dot1xAuthStatsTable_Object = MibTable
dot1xAuthStatsTable = _Dot1xAuthStatsTable_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot1xAuthStatsTable.setStatus("current")
_Dot1xAuthStatsEntry_Object = MibTableRow
dot1xAuthStatsEntry = _Dot1xAuthStatsEntry_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1)
)
dot1xAuthStatsEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xAuthStatsEntry.setStatus("current")
_Dot1xAuthEapolFramesRx_Type = Counter32
_Dot1xAuthEapolFramesRx_Object = MibTableColumn
dot1xAuthEapolFramesRx = _Dot1xAuthEapolFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 1),
    _Dot1xAuthEapolFramesRx_Type()
)
dot1xAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolFramesRx.setStatus("current")
_Dot1xAuthEapolFramesTx_Type = Counter32
_Dot1xAuthEapolFramesTx_Object = MibTableColumn
dot1xAuthEapolFramesTx = _Dot1xAuthEapolFramesTx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 2),
    _Dot1xAuthEapolFramesTx_Type()
)
dot1xAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolFramesTx.setStatus("current")
_Dot1xAuthEapolStartFramesRx_Type = Counter32
_Dot1xAuthEapolStartFramesRx_Object = MibTableColumn
dot1xAuthEapolStartFramesRx = _Dot1xAuthEapolStartFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 3),
    _Dot1xAuthEapolStartFramesRx_Type()
)
dot1xAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolStartFramesRx.setStatus("current")
_Dot1xAuthEapolLogoffFramesRx_Type = Counter32
_Dot1xAuthEapolLogoffFramesRx_Object = MibTableColumn
dot1xAuthEapolLogoffFramesRx = _Dot1xAuthEapolLogoffFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 4),
    _Dot1xAuthEapolLogoffFramesRx_Type()
)
dot1xAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolLogoffFramesRx.setStatus("current")
_Dot1xAuthEapolRespIdFramesRx_Type = Counter32
_Dot1xAuthEapolRespIdFramesRx_Object = MibTableColumn
dot1xAuthEapolRespIdFramesRx = _Dot1xAuthEapolRespIdFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 5),
    _Dot1xAuthEapolRespIdFramesRx_Type()
)
dot1xAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolRespIdFramesRx.setStatus("current")
_Dot1xAuthEapolRespFramesRx_Type = Counter32
_Dot1xAuthEapolRespFramesRx_Object = MibTableColumn
dot1xAuthEapolRespFramesRx = _Dot1xAuthEapolRespFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 6),
    _Dot1xAuthEapolRespFramesRx_Type()
)
dot1xAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolRespFramesRx.setStatus("current")
_Dot1xAuthEapolReqIdFramesTx_Type = Counter32
_Dot1xAuthEapolReqIdFramesTx_Object = MibTableColumn
dot1xAuthEapolReqIdFramesTx = _Dot1xAuthEapolReqIdFramesTx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 7),
    _Dot1xAuthEapolReqIdFramesTx_Type()
)
dot1xAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolReqIdFramesTx.setStatus("current")
_Dot1xAuthEapolReqFramesTx_Type = Counter32
_Dot1xAuthEapolReqFramesTx_Object = MibTableColumn
dot1xAuthEapolReqFramesTx = _Dot1xAuthEapolReqFramesTx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 8),
    _Dot1xAuthEapolReqFramesTx_Type()
)
dot1xAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapolReqFramesTx.setStatus("current")
_Dot1xAuthInvalidEapolFramesRx_Type = Counter32
_Dot1xAuthInvalidEapolFramesRx_Object = MibTableColumn
dot1xAuthInvalidEapolFramesRx = _Dot1xAuthInvalidEapolFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 9),
    _Dot1xAuthInvalidEapolFramesRx_Type()
)
dot1xAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthInvalidEapolFramesRx.setStatus("current")
_Dot1xAuthEapLengthErrorFramesRx_Type = Counter32
_Dot1xAuthEapLengthErrorFramesRx_Object = MibTableColumn
dot1xAuthEapLengthErrorFramesRx = _Dot1xAuthEapLengthErrorFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 10),
    _Dot1xAuthEapLengthErrorFramesRx_Type()
)
dot1xAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapLengthErrorFramesRx.setStatus("current")
_Dot1xAuthLastEapolFrameVersion_Type = Unsigned32
_Dot1xAuthLastEapolFrameVersion_Object = MibTableColumn
dot1xAuthLastEapolFrameVersion = _Dot1xAuthLastEapolFrameVersion_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 11),
    _Dot1xAuthLastEapolFrameVersion_Type()
)
dot1xAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthLastEapolFrameVersion.setStatus("current")
_Dot1xAuthLastEapolFrameSource_Type = MacAddress
_Dot1xAuthLastEapolFrameSource_Object = MibTableColumn
dot1xAuthLastEapolFrameSource = _Dot1xAuthLastEapolFrameSource_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 2, 1, 12),
    _Dot1xAuthLastEapolFrameSource_Type()
)
dot1xAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthLastEapolFrameSource.setStatus("current")
_Dot1xAuthDiagTable_Object = MibTable
dot1xAuthDiagTable = _Dot1xAuthDiagTable_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dot1xAuthDiagTable.setStatus("current")
_Dot1xAuthDiagEntry_Object = MibTableRow
dot1xAuthDiagEntry = _Dot1xAuthDiagEntry_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1)
)
dot1xAuthDiagEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xAuthDiagEntry.setStatus("current")
_Dot1xAuthEntersConnecting_Type = Counter32
_Dot1xAuthEntersConnecting_Object = MibTableColumn
dot1xAuthEntersConnecting = _Dot1xAuthEntersConnecting_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 1),
    _Dot1xAuthEntersConnecting_Type()
)
dot1xAuthEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEntersConnecting.setStatus("current")
_Dot1xAuthEapLogoffsWhileConnecting_Type = Counter32
_Dot1xAuthEapLogoffsWhileConnecting_Object = MibTableColumn
dot1xAuthEapLogoffsWhileConnecting = _Dot1xAuthEapLogoffsWhileConnecting_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 2),
    _Dot1xAuthEapLogoffsWhileConnecting_Type()
)
dot1xAuthEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEapLogoffsWhileConnecting.setStatus("current")
_Dot1xAuthEntersAuthenticating_Type = Counter32
_Dot1xAuthEntersAuthenticating_Object = MibTableColumn
dot1xAuthEntersAuthenticating = _Dot1xAuthEntersAuthenticating_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 3),
    _Dot1xAuthEntersAuthenticating_Type()
)
dot1xAuthEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthEntersAuthenticating.setStatus("current")
_Dot1xAuthAuthSuccessWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthSuccessWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthSuccessWhileAuthenticating = _Dot1xAuthAuthSuccessWhileAuthenticating_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 4),
    _Dot1xAuthAuthSuccessWhileAuthenticating_Type()
)
dot1xAuthAuthSuccessWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthSuccessWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthTimeoutsWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthTimeoutsWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthTimeoutsWhileAuthenticating = _Dot1xAuthAuthTimeoutsWhileAuthenticating_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 5),
    _Dot1xAuthAuthTimeoutsWhileAuthenticating_Type()
)
dot1xAuthAuthTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthTimeoutsWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthFailWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthFailWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthFailWhileAuthenticating = _Dot1xAuthAuthFailWhileAuthenticating_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 6),
    _Dot1xAuthAuthFailWhileAuthenticating_Type()
)
dot1xAuthAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthFailWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthReauthsWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthReauthsWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthReauthsWhileAuthenticating = _Dot1xAuthAuthReauthsWhileAuthenticating_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 7),
    _Dot1xAuthAuthReauthsWhileAuthenticating_Type()
)
dot1xAuthAuthReauthsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthReauthsWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthEapStartsWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthEapStartsWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthEapStartsWhileAuthenticating = _Dot1xAuthAuthEapStartsWhileAuthenticating_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 8),
    _Dot1xAuthAuthEapStartsWhileAuthenticating_Type()
)
dot1xAuthAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthEapStartsWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthEapLogoffWhileAuthenticating_Type = Counter32
_Dot1xAuthAuthEapLogoffWhileAuthenticating_Object = MibTableColumn
dot1xAuthAuthEapLogoffWhileAuthenticating = _Dot1xAuthAuthEapLogoffWhileAuthenticating_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 9),
    _Dot1xAuthAuthEapLogoffWhileAuthenticating_Type()
)
dot1xAuthAuthEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthEapLogoffWhileAuthenticating.setStatus("current")
_Dot1xAuthAuthReauthsWhileAuthenticated_Type = Counter32
_Dot1xAuthAuthReauthsWhileAuthenticated_Object = MibTableColumn
dot1xAuthAuthReauthsWhileAuthenticated = _Dot1xAuthAuthReauthsWhileAuthenticated_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 10),
    _Dot1xAuthAuthReauthsWhileAuthenticated_Type()
)
dot1xAuthAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthReauthsWhileAuthenticated.setStatus("current")
_Dot1xAuthAuthEapStartsWhileAuthenticated_Type = Counter32
_Dot1xAuthAuthEapStartsWhileAuthenticated_Object = MibTableColumn
dot1xAuthAuthEapStartsWhileAuthenticated = _Dot1xAuthAuthEapStartsWhileAuthenticated_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 11),
    _Dot1xAuthAuthEapStartsWhileAuthenticated_Type()
)
dot1xAuthAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthEapStartsWhileAuthenticated.setStatus("current")
_Dot1xAuthAuthEapLogoffWhileAuthenticated_Type = Counter32
_Dot1xAuthAuthEapLogoffWhileAuthenticated_Object = MibTableColumn
dot1xAuthAuthEapLogoffWhileAuthenticated = _Dot1xAuthAuthEapLogoffWhileAuthenticated_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 12),
    _Dot1xAuthAuthEapLogoffWhileAuthenticated_Type()
)
dot1xAuthAuthEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthAuthEapLogoffWhileAuthenticated.setStatus("current")
_Dot1xAuthBackendResponses_Type = Counter32
_Dot1xAuthBackendResponses_Object = MibTableColumn
dot1xAuthBackendResponses = _Dot1xAuthBackendResponses_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 13),
    _Dot1xAuthBackendResponses_Type()
)
dot1xAuthBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendResponses.setStatus("current")
_Dot1xAuthBackendAccessChallenges_Type = Counter32
_Dot1xAuthBackendAccessChallenges_Object = MibTableColumn
dot1xAuthBackendAccessChallenges = _Dot1xAuthBackendAccessChallenges_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 14),
    _Dot1xAuthBackendAccessChallenges_Type()
)
dot1xAuthBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendAccessChallenges.setStatus("current")
_Dot1xAuthBackendOtherRequestsToSupplicant_Type = Counter32
_Dot1xAuthBackendOtherRequestsToSupplicant_Object = MibTableColumn
dot1xAuthBackendOtherRequestsToSupplicant = _Dot1xAuthBackendOtherRequestsToSupplicant_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 15),
    _Dot1xAuthBackendOtherRequestsToSupplicant_Type()
)
dot1xAuthBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendOtherRequestsToSupplicant.setStatus("current")
_Dot1xAuthBackendNonNakResponsesFromSupplicant_Type = Counter32
_Dot1xAuthBackendNonNakResponsesFromSupplicant_Object = MibTableColumn
dot1xAuthBackendNonNakResponsesFromSupplicant = _Dot1xAuthBackendNonNakResponsesFromSupplicant_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 16),
    _Dot1xAuthBackendNonNakResponsesFromSupplicant_Type()
)
dot1xAuthBackendNonNakResponsesFromSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendNonNakResponsesFromSupplicant.setStatus("current")
_Dot1xAuthBackendAuthSuccesses_Type = Counter32
_Dot1xAuthBackendAuthSuccesses_Object = MibTableColumn
dot1xAuthBackendAuthSuccesses = _Dot1xAuthBackendAuthSuccesses_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 17),
    _Dot1xAuthBackendAuthSuccesses_Type()
)
dot1xAuthBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendAuthSuccesses.setStatus("current")
_Dot1xAuthBackendAuthFails_Type = Counter32
_Dot1xAuthBackendAuthFails_Object = MibTableColumn
dot1xAuthBackendAuthFails = _Dot1xAuthBackendAuthFails_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 3, 1, 18),
    _Dot1xAuthBackendAuthFails_Type()
)
dot1xAuthBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthBackendAuthFails.setStatus("current")
_Dot1xAuthSessionStatsTable_Object = MibTable
dot1xAuthSessionStatsTable = _Dot1xAuthSessionStatsTable_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dot1xAuthSessionStatsTable.setStatus("current")
_Dot1xAuthSessionStatsEntry_Object = MibTableRow
dot1xAuthSessionStatsEntry = _Dot1xAuthSessionStatsEntry_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4, 1)
)
dot1xAuthSessionStatsEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xAuthSessionStatsEntry.setStatus("current")
_Dot1xAuthSessionOctetsRx_Type = Counter64
_Dot1xAuthSessionOctetsRx_Object = MibTableColumn
dot1xAuthSessionOctetsRx = _Dot1xAuthSessionOctetsRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 1),
    _Dot1xAuthSessionOctetsRx_Type()
)
dot1xAuthSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionOctetsRx.setStatus("current")
_Dot1xAuthSessionOctetsTx_Type = Counter64
_Dot1xAuthSessionOctetsTx_Object = MibTableColumn
dot1xAuthSessionOctetsTx = _Dot1xAuthSessionOctetsTx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 2),
    _Dot1xAuthSessionOctetsTx_Type()
)
dot1xAuthSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionOctetsTx.setStatus("current")
_Dot1xAuthSessionFramesRx_Type = Counter32
_Dot1xAuthSessionFramesRx_Object = MibTableColumn
dot1xAuthSessionFramesRx = _Dot1xAuthSessionFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 3),
    _Dot1xAuthSessionFramesRx_Type()
)
dot1xAuthSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionFramesRx.setStatus("current")
_Dot1xAuthSessionFramesTx_Type = Counter32
_Dot1xAuthSessionFramesTx_Object = MibTableColumn
dot1xAuthSessionFramesTx = _Dot1xAuthSessionFramesTx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 4),
    _Dot1xAuthSessionFramesTx_Type()
)
dot1xAuthSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionFramesTx.setStatus("current")
_Dot1xAuthSessionId_Type = SnmpAdminString
_Dot1xAuthSessionId_Object = MibTableColumn
dot1xAuthSessionId = _Dot1xAuthSessionId_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 5),
    _Dot1xAuthSessionId_Type()
)
dot1xAuthSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionId.setStatus("current")


class _Dot1xAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type dot1xAuthSessionAuthenticMethod based on Integer32"""
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


_Dot1xAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_Dot1xAuthSessionAuthenticMethod_Object = MibTableColumn
dot1xAuthSessionAuthenticMethod = _Dot1xAuthSessionAuthenticMethod_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 6),
    _Dot1xAuthSessionAuthenticMethod_Type()
)
dot1xAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionAuthenticMethod.setStatus("current")
_Dot1xAuthSessionTime_Type = TimeTicks
_Dot1xAuthSessionTime_Object = MibTableColumn
dot1xAuthSessionTime = _Dot1xAuthSessionTime_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 7),
    _Dot1xAuthSessionTime_Type()
)
dot1xAuthSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionTime.setStatus("current")


class _Dot1xAuthSessionTerminateCause_Type(Integer32):
    """Custom type dot1xAuthSessionTerminateCause based on Integer32"""
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


_Dot1xAuthSessionTerminateCause_Type.__name__ = "Integer32"
_Dot1xAuthSessionTerminateCause_Object = MibTableColumn
dot1xAuthSessionTerminateCause = _Dot1xAuthSessionTerminateCause_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 8),
    _Dot1xAuthSessionTerminateCause_Type()
)
dot1xAuthSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionTerminateCause.setStatus("current")
_Dot1xAuthSessionUserName_Type = SnmpAdminString
_Dot1xAuthSessionUserName_Object = MibTableColumn
dot1xAuthSessionUserName = _Dot1xAuthSessionUserName_Object(
    (1, 0, 8802, 1, 1, 1, 1, 2, 4, 1, 9),
    _Dot1xAuthSessionUserName_Type()
)
dot1xAuthSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthSessionUserName.setStatus("current")
_Dot1xPaeSupplicant_ObjectIdentity = ObjectIdentity
dot1xPaeSupplicant = _Dot1xPaeSupplicant_ObjectIdentity(
    (1, 0, 8802, 1, 1, 1, 1, 3)
)
_Dot1xSuppConfigTable_Object = MibTable
dot1xSuppConfigTable = _Dot1xSuppConfigTable_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot1xSuppConfigTable.setStatus("current")
_Dot1xSuppConfigEntry_Object = MibTableRow
dot1xSuppConfigEntry = _Dot1xSuppConfigEntry_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 1, 1)
)
dot1xSuppConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xSuppConfigEntry.setStatus("current")


class _Dot1xSuppPaeState_Type(Integer32):
    """Custom type dot1xSuppPaeState based on Integer32"""
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
        *(("acquired", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 1),
          ("held", 7),
          ("logoff", 2))
    )


_Dot1xSuppPaeState_Type.__name__ = "Integer32"
_Dot1xSuppPaeState_Object = MibTableColumn
dot1xSuppPaeState = _Dot1xSuppPaeState_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 1),
    _Dot1xSuppPaeState_Type()
)
dot1xSuppPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppPaeState.setStatus("current")


class _Dot1xSuppHeldPeriod_Type(Unsigned32):
    """Custom type dot1xSuppHeldPeriod based on Unsigned32"""
    defaultValue = 60


_Dot1xSuppHeldPeriod_Object = MibTableColumn
dot1xSuppHeldPeriod = _Dot1xSuppHeldPeriod_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 2),
    _Dot1xSuppHeldPeriod_Type()
)
dot1xSuppHeldPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xSuppHeldPeriod.setStatus("current")


class _Dot1xSuppAuthPeriod_Type(Unsigned32):
    """Custom type dot1xSuppAuthPeriod based on Unsigned32"""
    defaultValue = 30


_Dot1xSuppAuthPeriod_Object = MibTableColumn
dot1xSuppAuthPeriod = _Dot1xSuppAuthPeriod_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 3),
    _Dot1xSuppAuthPeriod_Type()
)
dot1xSuppAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xSuppAuthPeriod.setStatus("current")


class _Dot1xSuppStartPeriod_Type(Unsigned32):
    """Custom type dot1xSuppStartPeriod based on Unsigned32"""
    defaultValue = 30


_Dot1xSuppStartPeriod_Object = MibTableColumn
dot1xSuppStartPeriod = _Dot1xSuppStartPeriod_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 4),
    _Dot1xSuppStartPeriod_Type()
)
dot1xSuppStartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xSuppStartPeriod.setStatus("current")


class _Dot1xSuppMaxStart_Type(Unsigned32):
    """Custom type dot1xSuppMaxStart based on Unsigned32"""
    defaultValue = 3


_Dot1xSuppMaxStart_Object = MibTableColumn
dot1xSuppMaxStart = _Dot1xSuppMaxStart_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 1, 1, 5),
    _Dot1xSuppMaxStart_Type()
)
dot1xSuppMaxStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xSuppMaxStart.setStatus("current")
_Dot1xSuppStatsTable_Object = MibTable
dot1xSuppStatsTable = _Dot1xSuppStatsTable_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dot1xSuppStatsTable.setStatus("current")
_Dot1xSuppStatsEntry_Object = MibTableRow
dot1xSuppStatsEntry = _Dot1xSuppStatsEntry_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1)
)
dot1xSuppStatsEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    dot1xSuppStatsEntry.setStatus("current")
_Dot1xSuppEapolFramesRx_Type = Counter32
_Dot1xSuppEapolFramesRx_Object = MibTableColumn
dot1xSuppEapolFramesRx = _Dot1xSuppEapolFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 1),
    _Dot1xSuppEapolFramesRx_Type()
)
dot1xSuppEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppEapolFramesRx.setStatus("current")
_Dot1xSuppEapolFramesTx_Type = Counter32
_Dot1xSuppEapolFramesTx_Object = MibTableColumn
dot1xSuppEapolFramesTx = _Dot1xSuppEapolFramesTx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 2),
    _Dot1xSuppEapolFramesTx_Type()
)
dot1xSuppEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppEapolFramesTx.setStatus("current")
_Dot1xSuppEapolStartFramesTx_Type = Counter32
_Dot1xSuppEapolStartFramesTx_Object = MibTableColumn
dot1xSuppEapolStartFramesTx = _Dot1xSuppEapolStartFramesTx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 3),
    _Dot1xSuppEapolStartFramesTx_Type()
)
dot1xSuppEapolStartFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppEapolStartFramesTx.setStatus("current")
_Dot1xSuppEapolLogoffFramesTx_Type = Counter32
_Dot1xSuppEapolLogoffFramesTx_Object = MibTableColumn
dot1xSuppEapolLogoffFramesTx = _Dot1xSuppEapolLogoffFramesTx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 4),
    _Dot1xSuppEapolLogoffFramesTx_Type()
)
dot1xSuppEapolLogoffFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppEapolLogoffFramesTx.setStatus("current")
_Dot1xSuppEapolRespIdFramesTx_Type = Counter32
_Dot1xSuppEapolRespIdFramesTx_Object = MibTableColumn
dot1xSuppEapolRespIdFramesTx = _Dot1xSuppEapolRespIdFramesTx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 5),
    _Dot1xSuppEapolRespIdFramesTx_Type()
)
dot1xSuppEapolRespIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppEapolRespIdFramesTx.setStatus("current")
_Dot1xSuppEapolRespFramesTx_Type = Counter32
_Dot1xSuppEapolRespFramesTx_Object = MibTableColumn
dot1xSuppEapolRespFramesTx = _Dot1xSuppEapolRespFramesTx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 6),
    _Dot1xSuppEapolRespFramesTx_Type()
)
dot1xSuppEapolRespFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppEapolRespFramesTx.setStatus("current")
_Dot1xSuppEapolReqIdFramesRx_Type = Counter32
_Dot1xSuppEapolReqIdFramesRx_Object = MibTableColumn
dot1xSuppEapolReqIdFramesRx = _Dot1xSuppEapolReqIdFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 7),
    _Dot1xSuppEapolReqIdFramesRx_Type()
)
dot1xSuppEapolReqIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppEapolReqIdFramesRx.setStatus("current")
_Dot1xSuppEapolReqFramesRx_Type = Counter32
_Dot1xSuppEapolReqFramesRx_Object = MibTableColumn
dot1xSuppEapolReqFramesRx = _Dot1xSuppEapolReqFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 8),
    _Dot1xSuppEapolReqFramesRx_Type()
)
dot1xSuppEapolReqFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppEapolReqFramesRx.setStatus("current")
_Dot1xSuppInvalidEapolFramesRx_Type = Counter32
_Dot1xSuppInvalidEapolFramesRx_Object = MibTableColumn
dot1xSuppInvalidEapolFramesRx = _Dot1xSuppInvalidEapolFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 9),
    _Dot1xSuppInvalidEapolFramesRx_Type()
)
dot1xSuppInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppInvalidEapolFramesRx.setStatus("current")
_Dot1xSuppEapLengthErrorFramesRx_Type = Counter32
_Dot1xSuppEapLengthErrorFramesRx_Object = MibTableColumn
dot1xSuppEapLengthErrorFramesRx = _Dot1xSuppEapLengthErrorFramesRx_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 10),
    _Dot1xSuppEapLengthErrorFramesRx_Type()
)
dot1xSuppEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppEapLengthErrorFramesRx.setStatus("current")
_Dot1xSuppLastEapolFrameVersion_Type = Unsigned32
_Dot1xSuppLastEapolFrameVersion_Object = MibTableColumn
dot1xSuppLastEapolFrameVersion = _Dot1xSuppLastEapolFrameVersion_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 11),
    _Dot1xSuppLastEapolFrameVersion_Type()
)
dot1xSuppLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppLastEapolFrameVersion.setStatus("current")
_Dot1xSuppLastEapolFrameSource_Type = MacAddress
_Dot1xSuppLastEapolFrameSource_Object = MibTableColumn
dot1xSuppLastEapolFrameSource = _Dot1xSuppLastEapolFrameSource_Object(
    (1, 0, 8802, 1, 1, 1, 1, 3, 2, 1, 12),
    _Dot1xSuppLastEapolFrameSource_Type()
)
dot1xSuppLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xSuppLastEapolFrameSource.setStatus("current")
_Dot1xPaeConformance_ObjectIdentity = ObjectIdentity
dot1xPaeConformance = _Dot1xPaeConformance_ObjectIdentity(
    (1, 0, 8802, 1, 1, 1, 2)
)
_Dot1xPaeGroups_ObjectIdentity = ObjectIdentity
dot1xPaeGroups = _Dot1xPaeGroups_ObjectIdentity(
    (1, 0, 8802, 1, 1, 1, 2, 1)
)
_Dot1xPaeCompliances_ObjectIdentity = ObjectIdentity
dot1xPaeCompliances = _Dot1xPaeCompliances_ObjectIdentity(
    (1, 0, 8802, 1, 1, 1, 2, 2)
)

# Managed Objects groups

dot1xPaeSystemGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 1, 2, 1, 1)
)
dot1xPaeSystemGroup.setObjects(
      *(("IEEE8021-PAE-MIB", "dot1xPaeSystemAuthControl"),
        ("IEEE8021-PAE-MIB", "dot1xPaePortProtocolVersion"),
        ("IEEE8021-PAE-MIB", "dot1xPaePortCapabilities"),
        ("IEEE8021-PAE-MIB", "dot1xPaePortInitialize"))
)
if mibBuilder.loadTexts:
    dot1xPaeSystemGroup.setStatus("current")

dot1xPaeAuthConfigGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 1, 2, 1, 2)
)
dot1xPaeAuthConfigGroup.setObjects(
      *(("IEEE8021-PAE-MIB", "dot1xAuthPaeState"),
        ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthState"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAdminControlledDirections"),
        ("IEEE8021-PAE-MIB", "dot1xAuthOperControlledDirections"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthControlledPortStatus"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthControlledPortControl"),
        ("IEEE8021-PAE-MIB", "dot1xAuthQuietPeriod"),
        ("IEEE8021-PAE-MIB", "dot1xAuthTxPeriod"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSuppTimeout"),
        ("IEEE8021-PAE-MIB", "dot1xAuthServerTimeout"),
        ("IEEE8021-PAE-MIB", "dot1xAuthMaxReq"),
        ("IEEE8021-PAE-MIB", "dot1xAuthReAuthPeriod"),
        ("IEEE8021-PAE-MIB", "dot1xAuthReAuthEnabled"),
        ("IEEE8021-PAE-MIB", "dot1xAuthKeyTxEnabled"))
)
if mibBuilder.loadTexts:
    dot1xPaeAuthConfigGroup.setStatus("current")

dot1xPaeAuthStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 1, 2, 1, 3)
)
dot1xPaeAuthStatsGroup.setObjects(
      *(("IEEE8021-PAE-MIB", "dot1xAuthEapolFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthEapolFramesTx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthEapolStartFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthEapolLogoffFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthEapolRespIdFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthEapolRespFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthEapolReqIdFramesTx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthEapolReqFramesTx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthInvalidEapolFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthEapLengthErrorFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthLastEapolFrameVersion"),
        ("IEEE8021-PAE-MIB", "dot1xAuthLastEapolFrameSource"))
)
if mibBuilder.loadTexts:
    dot1xPaeAuthStatsGroup.setStatus("current")

dot1xPaeAuthDiagGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 1, 2, 1, 4)
)
dot1xPaeAuthDiagGroup.setObjects(
      *(("IEEE8021-PAE-MIB", "dot1xAuthEntersConnecting"),
        ("IEEE8021-PAE-MIB", "dot1xAuthEapLogoffsWhileConnecting"),
        ("IEEE8021-PAE-MIB", "dot1xAuthEntersAuthenticating"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthSuccessWhileAuthenticating"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthTimeoutsWhileAuthenticating"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthFailWhileAuthenticating"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthReauthsWhileAuthenticating"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapStartsWhileAuthenticating"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapLogoffWhileAuthenticating"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthReauthsWhileAuthenticated"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapStartsWhileAuthenticated"),
        ("IEEE8021-PAE-MIB", "dot1xAuthAuthEapLogoffWhileAuthenticated"),
        ("IEEE8021-PAE-MIB", "dot1xAuthBackendResponses"),
        ("IEEE8021-PAE-MIB", "dot1xAuthBackendAccessChallenges"),
        ("IEEE8021-PAE-MIB", "dot1xAuthBackendOtherRequestsToSupplicant"),
        ("IEEE8021-PAE-MIB", "dot1xAuthBackendNonNakResponsesFromSupplicant"),
        ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthSuccesses"),
        ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthFails"))
)
if mibBuilder.loadTexts:
    dot1xPaeAuthDiagGroup.setStatus("current")

dot1xPaeAuthSessionStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 1, 2, 1, 5)
)
dot1xPaeAuthSessionStatsGroup.setObjects(
      *(("IEEE8021-PAE-MIB", "dot1xAuthSessionOctetsRx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionOctetsTx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionFramesTx"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionId"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionAuthenticMethod"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionTime"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionTerminateCause"))
)
if mibBuilder.loadTexts:
    dot1xPaeAuthSessionStatsGroup.setStatus("current")

dot1xPaeSuppConfigGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 1, 2, 1, 6)
)
dot1xPaeSuppConfigGroup.setObjects(
      *(("IEEE8021-PAE-MIB", "dot1xSuppPaeState"),
        ("IEEE8021-PAE-MIB", "dot1xSuppHeldPeriod"),
        ("IEEE8021-PAE-MIB", "dot1xSuppAuthPeriod"),
        ("IEEE8021-PAE-MIB", "dot1xSuppStartPeriod"),
        ("IEEE8021-PAE-MIB", "dot1xSuppMaxStart"))
)
if mibBuilder.loadTexts:
    dot1xPaeSuppConfigGroup.setStatus("current")

dot1xPaeSuppStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 1, 2, 1, 7)
)
dot1xPaeSuppStatsGroup.setObjects(
      *(("IEEE8021-PAE-MIB", "dot1xSuppEapolFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xSuppEapolFramesTx"),
        ("IEEE8021-PAE-MIB", "dot1xSuppEapolStartFramesTx"),
        ("IEEE8021-PAE-MIB", "dot1xSuppEapolLogoffFramesTx"),
        ("IEEE8021-PAE-MIB", "dot1xSuppEapolRespIdFramesTx"),
        ("IEEE8021-PAE-MIB", "dot1xSuppEapolRespFramesTx"),
        ("IEEE8021-PAE-MIB", "dot1xSuppEapolReqIdFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xSuppEapolReqFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xSuppInvalidEapolFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xSuppEapLengthErrorFramesRx"),
        ("IEEE8021-PAE-MIB", "dot1xSuppLastEapolFrameVersion"),
        ("IEEE8021-PAE-MIB", "dot1xSuppLastEapolFrameSource"))
)
if mibBuilder.loadTexts:
    dot1xPaeSuppStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dot1xPaeCompliance = ModuleCompliance(
    (1, 0, 8802, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dot1xPaeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-PAE-MIB",
    **{"PaeControlledDirections": PaeControlledDirections,
       "PaeControlledPortStatus": PaeControlledPortStatus,
       "PaeControlledPortControl": PaeControlledPortControl,
       "ieee8021paeMIB": ieee8021paeMIB,
       "paeMIBObjects": paeMIBObjects,
       "dot1xPaeSystem": dot1xPaeSystem,
       "dot1xPaeSystemAuthControl": dot1xPaeSystemAuthControl,
       "dot1xPaePortTable": dot1xPaePortTable,
       "dot1xPaePortEntry": dot1xPaePortEntry,
       "dot1xPaePortNumber": dot1xPaePortNumber,
       "dot1xPaePortProtocolVersion": dot1xPaePortProtocolVersion,
       "dot1xPaePortCapabilities": dot1xPaePortCapabilities,
       "dot1xPaePortInitialize": dot1xPaePortInitialize,
       "dot1xPaePortReauthenticate": dot1xPaePortReauthenticate,
       "dot1xPaeAuthenticator": dot1xPaeAuthenticator,
       "dot1xAuthConfigTable": dot1xAuthConfigTable,
       "dot1xAuthConfigEntry": dot1xAuthConfigEntry,
       "dot1xAuthPaeState": dot1xAuthPaeState,
       "dot1xAuthBackendAuthState": dot1xAuthBackendAuthState,
       "dot1xAuthAdminControlledDirections": dot1xAuthAdminControlledDirections,
       "dot1xAuthOperControlledDirections": dot1xAuthOperControlledDirections,
       "dot1xAuthAuthControlledPortStatus": dot1xAuthAuthControlledPortStatus,
       "dot1xAuthAuthControlledPortControl": dot1xAuthAuthControlledPortControl,
       "dot1xAuthQuietPeriod": dot1xAuthQuietPeriod,
       "dot1xAuthTxPeriod": dot1xAuthTxPeriod,
       "dot1xAuthSuppTimeout": dot1xAuthSuppTimeout,
       "dot1xAuthServerTimeout": dot1xAuthServerTimeout,
       "dot1xAuthMaxReq": dot1xAuthMaxReq,
       "dot1xAuthReAuthPeriod": dot1xAuthReAuthPeriod,
       "dot1xAuthReAuthEnabled": dot1xAuthReAuthEnabled,
       "dot1xAuthKeyTxEnabled": dot1xAuthKeyTxEnabled,
       "dot1xAuthStatsTable": dot1xAuthStatsTable,
       "dot1xAuthStatsEntry": dot1xAuthStatsEntry,
       "dot1xAuthEapolFramesRx": dot1xAuthEapolFramesRx,
       "dot1xAuthEapolFramesTx": dot1xAuthEapolFramesTx,
       "dot1xAuthEapolStartFramesRx": dot1xAuthEapolStartFramesRx,
       "dot1xAuthEapolLogoffFramesRx": dot1xAuthEapolLogoffFramesRx,
       "dot1xAuthEapolRespIdFramesRx": dot1xAuthEapolRespIdFramesRx,
       "dot1xAuthEapolRespFramesRx": dot1xAuthEapolRespFramesRx,
       "dot1xAuthEapolReqIdFramesTx": dot1xAuthEapolReqIdFramesTx,
       "dot1xAuthEapolReqFramesTx": dot1xAuthEapolReqFramesTx,
       "dot1xAuthInvalidEapolFramesRx": dot1xAuthInvalidEapolFramesRx,
       "dot1xAuthEapLengthErrorFramesRx": dot1xAuthEapLengthErrorFramesRx,
       "dot1xAuthLastEapolFrameVersion": dot1xAuthLastEapolFrameVersion,
       "dot1xAuthLastEapolFrameSource": dot1xAuthLastEapolFrameSource,
       "dot1xAuthDiagTable": dot1xAuthDiagTable,
       "dot1xAuthDiagEntry": dot1xAuthDiagEntry,
       "dot1xAuthEntersConnecting": dot1xAuthEntersConnecting,
       "dot1xAuthEapLogoffsWhileConnecting": dot1xAuthEapLogoffsWhileConnecting,
       "dot1xAuthEntersAuthenticating": dot1xAuthEntersAuthenticating,
       "dot1xAuthAuthSuccessWhileAuthenticating": dot1xAuthAuthSuccessWhileAuthenticating,
       "dot1xAuthAuthTimeoutsWhileAuthenticating": dot1xAuthAuthTimeoutsWhileAuthenticating,
       "dot1xAuthAuthFailWhileAuthenticating": dot1xAuthAuthFailWhileAuthenticating,
       "dot1xAuthAuthReauthsWhileAuthenticating": dot1xAuthAuthReauthsWhileAuthenticating,
       "dot1xAuthAuthEapStartsWhileAuthenticating": dot1xAuthAuthEapStartsWhileAuthenticating,
       "dot1xAuthAuthEapLogoffWhileAuthenticating": dot1xAuthAuthEapLogoffWhileAuthenticating,
       "dot1xAuthAuthReauthsWhileAuthenticated": dot1xAuthAuthReauthsWhileAuthenticated,
       "dot1xAuthAuthEapStartsWhileAuthenticated": dot1xAuthAuthEapStartsWhileAuthenticated,
       "dot1xAuthAuthEapLogoffWhileAuthenticated": dot1xAuthAuthEapLogoffWhileAuthenticated,
       "dot1xAuthBackendResponses": dot1xAuthBackendResponses,
       "dot1xAuthBackendAccessChallenges": dot1xAuthBackendAccessChallenges,
       "dot1xAuthBackendOtherRequestsToSupplicant": dot1xAuthBackendOtherRequestsToSupplicant,
       "dot1xAuthBackendNonNakResponsesFromSupplicant": dot1xAuthBackendNonNakResponsesFromSupplicant,
       "dot1xAuthBackendAuthSuccesses": dot1xAuthBackendAuthSuccesses,
       "dot1xAuthBackendAuthFails": dot1xAuthBackendAuthFails,
       "dot1xAuthSessionStatsTable": dot1xAuthSessionStatsTable,
       "dot1xAuthSessionStatsEntry": dot1xAuthSessionStatsEntry,
       "dot1xAuthSessionOctetsRx": dot1xAuthSessionOctetsRx,
       "dot1xAuthSessionOctetsTx": dot1xAuthSessionOctetsTx,
       "dot1xAuthSessionFramesRx": dot1xAuthSessionFramesRx,
       "dot1xAuthSessionFramesTx": dot1xAuthSessionFramesTx,
       "dot1xAuthSessionId": dot1xAuthSessionId,
       "dot1xAuthSessionAuthenticMethod": dot1xAuthSessionAuthenticMethod,
       "dot1xAuthSessionTime": dot1xAuthSessionTime,
       "dot1xAuthSessionTerminateCause": dot1xAuthSessionTerminateCause,
       "dot1xAuthSessionUserName": dot1xAuthSessionUserName,
       "dot1xPaeSupplicant": dot1xPaeSupplicant,
       "dot1xSuppConfigTable": dot1xSuppConfigTable,
       "dot1xSuppConfigEntry": dot1xSuppConfigEntry,
       "dot1xSuppPaeState": dot1xSuppPaeState,
       "dot1xSuppHeldPeriod": dot1xSuppHeldPeriod,
       "dot1xSuppAuthPeriod": dot1xSuppAuthPeriod,
       "dot1xSuppStartPeriod": dot1xSuppStartPeriod,
       "dot1xSuppMaxStart": dot1xSuppMaxStart,
       "dot1xSuppStatsTable": dot1xSuppStatsTable,
       "dot1xSuppStatsEntry": dot1xSuppStatsEntry,
       "dot1xSuppEapolFramesRx": dot1xSuppEapolFramesRx,
       "dot1xSuppEapolFramesTx": dot1xSuppEapolFramesTx,
       "dot1xSuppEapolStartFramesTx": dot1xSuppEapolStartFramesTx,
       "dot1xSuppEapolLogoffFramesTx": dot1xSuppEapolLogoffFramesTx,
       "dot1xSuppEapolRespIdFramesTx": dot1xSuppEapolRespIdFramesTx,
       "dot1xSuppEapolRespFramesTx": dot1xSuppEapolRespFramesTx,
       "dot1xSuppEapolReqIdFramesRx": dot1xSuppEapolReqIdFramesRx,
       "dot1xSuppEapolReqFramesRx": dot1xSuppEapolReqFramesRx,
       "dot1xSuppInvalidEapolFramesRx": dot1xSuppInvalidEapolFramesRx,
       "dot1xSuppEapLengthErrorFramesRx": dot1xSuppEapLengthErrorFramesRx,
       "dot1xSuppLastEapolFrameVersion": dot1xSuppLastEapolFrameVersion,
       "dot1xSuppLastEapolFrameSource": dot1xSuppLastEapolFrameSource,
       "dot1xPaeConformance": dot1xPaeConformance,
       "dot1xPaeGroups": dot1xPaeGroups,
       "dot1xPaeSystemGroup": dot1xPaeSystemGroup,
       "dot1xPaeAuthConfigGroup": dot1xPaeAuthConfigGroup,
       "dot1xPaeAuthStatsGroup": dot1xPaeAuthStatsGroup,
       "dot1xPaeAuthDiagGroup": dot1xPaeAuthDiagGroup,
       "dot1xPaeAuthSessionStatsGroup": dot1xPaeAuthSessionStatsGroup,
       "dot1xPaeSuppConfigGroup": dot1xPaeSuppConfigGroup,
       "dot1xPaeSuppStatsGroup": dot1xPaeSuppStatsGroup,
       "dot1xPaeCompliances": dot1xPaeCompliances,
       "dot1xPaeCompliance": dot1xPaeCompliance}
)
