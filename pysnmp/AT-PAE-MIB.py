# SNMP MIB module (AT-PAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-PAE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:26 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

portAuth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118)
)
portAuth.setRevisions(
        ("2007-01-15 11:00",
         "2004-12-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtrPaeControlledDirections(Integer32, TextualConvention):
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



class AtrPaeControlledPortStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorised", 1),
          ("unauthorised", 2))
    )



class AtrPaeControlledPortControl(Integer32, TextualConvention):
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
          ("forceAuthorised", 3),
          ("forceUnauthorised", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AtrPaeMib_ObjectIdentity = ObjectIdentity
atrPaeMib = _AtrPaeMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1)
)
_AtrPaeMIBObjects_ObjectIdentity = ObjectIdentity
atrPaeMIBObjects = _AtrPaeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1)
)
_AtrDot1xPaeSystem_ObjectIdentity = ObjectIdentity
atrDot1xPaeSystem = _AtrDot1xPaeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 1)
)
_AtrDot1xPaePortTable_Object = MibTable
atrDot1xPaePortTable = _AtrDot1xPaePortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    atrDot1xPaePortTable.setStatus("current")
_AtrDot1xPaePortEntry_Object = MibTableRow
atrDot1xPaePortEntry = _AtrDot1xPaePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 1, 2, 1)
)
atrDot1xPaePortEntry.setIndexNames(
    (0, "AT-PAE-MIB", "atrDot1xPaePortNumber"),
    (0, "AT-PAE-MIB", "atrDot1xPaePortSuppMacAddress"),
)
if mibBuilder.loadTexts:
    atrDot1xPaePortEntry.setStatus("current")
_AtrDot1xPaePortNumber_Type = InterfaceIndex
_AtrDot1xPaePortNumber_Object = MibTableColumn
atrDot1xPaePortNumber = _AtrDot1xPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 1, 2, 1, 1),
    _AtrDot1xPaePortNumber_Type()
)
atrDot1xPaePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xPaePortNumber.setStatus("current")
_AtrDot1xPaePortProtocolVersion_Type = Unsigned32
_AtrDot1xPaePortProtocolVersion_Object = MibTableColumn
atrDot1xPaePortProtocolVersion = _AtrDot1xPaePortProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 1, 2, 1, 2),
    _AtrDot1xPaePortProtocolVersion_Type()
)
atrDot1xPaePortProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xPaePortProtocolVersion.setStatus("current")


class _AtrDot1xPaePortCapabilities_Type(Bits):
    """Custom type atrDot1xPaePortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("atrDot1xPaePortAuthCapable", 0),
          ("atrDot1xPaePortSuppCapable", 1))
    )

_AtrDot1xPaePortCapabilities_Type.__name__ = "Bits"
_AtrDot1xPaePortCapabilities_Object = MibTableColumn
atrDot1xPaePortCapabilities = _AtrDot1xPaePortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 1, 2, 1, 3),
    _AtrDot1xPaePortCapabilities_Type()
)
atrDot1xPaePortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xPaePortCapabilities.setStatus("current")
_AtrDot1xPaePortInitialise_Type = TruthValue
_AtrDot1xPaePortInitialise_Object = MibTableColumn
atrDot1xPaePortInitialise = _AtrDot1xPaePortInitialise_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 1, 2, 1, 4),
    _AtrDot1xPaePortInitialise_Type()
)
atrDot1xPaePortInitialise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xPaePortInitialise.setStatus("current")
_AtrDot1xPaePortReauthenticate_Type = TruthValue
_AtrDot1xPaePortReauthenticate_Object = MibTableColumn
atrDot1xPaePortReauthenticate = _AtrDot1xPaePortReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 1, 2, 1, 5),
    _AtrDot1xPaePortReauthenticate_Type()
)
atrDot1xPaePortReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xPaePortReauthenticate.setStatus("current")
_AtrDot1xPaePortSuppMacAddress_Type = MacAddress
_AtrDot1xPaePortSuppMacAddress_Object = MibTableColumn
atrDot1xPaePortSuppMacAddress = _AtrDot1xPaePortSuppMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 1, 2, 1, 6),
    _AtrDot1xPaePortSuppMacAddress_Type()
)
atrDot1xPaePortSuppMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xPaePortSuppMacAddress.setStatus("current")
_AtrDot1xPaeAuthenticator_ObjectIdentity = ObjectIdentity
atrDot1xPaeAuthenticator = _AtrDot1xPaeAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2)
)
_AtrDot1xAuthConfigTable_Object = MibTable
atrDot1xAuthConfigTable = _AtrDot1xAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    atrDot1xAuthConfigTable.setStatus("current")
_AtrDot1xAuthConfigEntry_Object = MibTableRow
atrDot1xAuthConfigEntry = _AtrDot1xAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1)
)
atrDot1xAuthConfigEntry.setIndexNames(
    (0, "AT-PAE-MIB", "atrDot1xPaePortNumber"),
    (0, "AT-PAE-MIB", "atrDot1xPaePortSuppMacAddress"),
)
if mibBuilder.loadTexts:
    atrDot1xAuthConfigEntry.setStatus("current")


class _AtrDot1xAuthPaeState_Type(Integer32):
    """Custom type atrDot1xAuthPaeState based on Integer32"""
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
          ("initialise", 1))
    )


_AtrDot1xAuthPaeState_Type.__name__ = "Integer32"
_AtrDot1xAuthPaeState_Object = MibTableColumn
atrDot1xAuthPaeState = _AtrDot1xAuthPaeState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 1),
    _AtrDot1xAuthPaeState_Type()
)
atrDot1xAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthPaeState.setStatus("current")


class _AtrDot1xAuthBackendAuthState_Type(Integer32):
    """Custom type atrDot1xAuthBackendAuthState based on Integer32"""
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
          ("initialise", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_AtrDot1xAuthBackendAuthState_Type.__name__ = "Integer32"
_AtrDot1xAuthBackendAuthState_Object = MibTableColumn
atrDot1xAuthBackendAuthState = _AtrDot1xAuthBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 2),
    _AtrDot1xAuthBackendAuthState_Type()
)
atrDot1xAuthBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthBackendAuthState.setStatus("current")
_AtrDot1xAuthAdminControlledDirections_Type = AtrPaeControlledDirections
_AtrDot1xAuthAdminControlledDirections_Object = MibTableColumn
atrDot1xAuthAdminControlledDirections = _AtrDot1xAuthAdminControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 3),
    _AtrDot1xAuthAdminControlledDirections_Type()
)
atrDot1xAuthAdminControlledDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthAdminControlledDirections.setStatus("current")
_AtrDot1xAuthOperControlledDirections_Type = AtrPaeControlledDirections
_AtrDot1xAuthOperControlledDirections_Object = MibTableColumn
atrDot1xAuthOperControlledDirections = _AtrDot1xAuthOperControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 4),
    _AtrDot1xAuthOperControlledDirections_Type()
)
atrDot1xAuthOperControlledDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthOperControlledDirections.setStatus("current")
_AtrDot1xAuthAuthControlledPortStatus_Type = AtrPaeControlledPortStatus
_AtrDot1xAuthAuthControlledPortStatus_Object = MibTableColumn
atrDot1xAuthAuthControlledPortStatus = _AtrDot1xAuthAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 5),
    _AtrDot1xAuthAuthControlledPortStatus_Type()
)
atrDot1xAuthAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthAuthControlledPortStatus.setStatus("current")
_AtrDot1xAuthAuthControlledPortControl_Type = AtrPaeControlledPortControl
_AtrDot1xAuthAuthControlledPortControl_Object = MibTableColumn
atrDot1xAuthAuthControlledPortControl = _AtrDot1xAuthAuthControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 6),
    _AtrDot1xAuthAuthControlledPortControl_Type()
)
atrDot1xAuthAuthControlledPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xAuthAuthControlledPortControl.setStatus("current")


class _AtrDot1xAuthQuietPeriod_Type(Unsigned32):
    """Custom type atrDot1xAuthQuietPeriod based on Unsigned32"""
    defaultValue = 60


_AtrDot1xAuthQuietPeriod_Object = MibTableColumn
atrDot1xAuthQuietPeriod = _AtrDot1xAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 7),
    _AtrDot1xAuthQuietPeriod_Type()
)
atrDot1xAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xAuthQuietPeriod.setStatus("current")


class _AtrDot1xAuthTxPeriod_Type(Unsigned32):
    """Custom type atrDot1xAuthTxPeriod based on Unsigned32"""
    defaultValue = 30


_AtrDot1xAuthTxPeriod_Object = MibTableColumn
atrDot1xAuthTxPeriod = _AtrDot1xAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 8),
    _AtrDot1xAuthTxPeriod_Type()
)
atrDot1xAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xAuthTxPeriod.setStatus("current")


class _AtrDot1xAuthSuppTimeout_Type(Unsigned32):
    """Custom type atrDot1xAuthSuppTimeout based on Unsigned32"""
    defaultValue = 30


_AtrDot1xAuthSuppTimeout_Object = MibTableColumn
atrDot1xAuthSuppTimeout = _AtrDot1xAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 9),
    _AtrDot1xAuthSuppTimeout_Type()
)
atrDot1xAuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xAuthSuppTimeout.setStatus("current")


class _AtrDot1xAuthServerTimeout_Type(Unsigned32):
    """Custom type atrDot1xAuthServerTimeout based on Unsigned32"""
    defaultValue = 30


_AtrDot1xAuthServerTimeout_Object = MibTableColumn
atrDot1xAuthServerTimeout = _AtrDot1xAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 10),
    _AtrDot1xAuthServerTimeout_Type()
)
atrDot1xAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xAuthServerTimeout.setStatus("current")


class _AtrDot1xAuthMaxReq_Type(Unsigned32):
    """Custom type atrDot1xAuthMaxReq based on Unsigned32"""
    defaultValue = 2


_AtrDot1xAuthMaxReq_Object = MibTableColumn
atrDot1xAuthMaxReq = _AtrDot1xAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 11),
    _AtrDot1xAuthMaxReq_Type()
)
atrDot1xAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xAuthMaxReq.setStatus("current")


class _AtrDot1xAuthReAuthPeriod_Type(Unsigned32):
    """Custom type atrDot1xAuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_AtrDot1xAuthReAuthPeriod_Object = MibTableColumn
atrDot1xAuthReAuthPeriod = _AtrDot1xAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 12),
    _AtrDot1xAuthReAuthPeriod_Type()
)
atrDot1xAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xAuthReAuthPeriod.setStatus("current")


class _AtrDot1xAuthReAuthEnabled_Type(TruthValue):
    """Custom type atrDot1xAuthReAuthEnabled based on TruthValue"""


_AtrDot1xAuthReAuthEnabled_Object = MibTableColumn
atrDot1xAuthReAuthEnabled = _AtrDot1xAuthReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 13),
    _AtrDot1xAuthReAuthEnabled_Type()
)
atrDot1xAuthReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xAuthReAuthEnabled.setStatus("current")
_AtrDot1xAuthKeyTxEnabled_Type = TruthValue
_AtrDot1xAuthKeyTxEnabled_Object = MibTableColumn
atrDot1xAuthKeyTxEnabled = _AtrDot1xAuthKeyTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 14),
    _AtrDot1xAuthKeyTxEnabled_Type()
)
atrDot1xAuthKeyTxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthKeyTxEnabled.setStatus("current")
_AtrDot1xAuthPreAuthVlan_Type = DisplayString
_AtrDot1xAuthPreAuthVlan_Object = MibTableColumn
atrDot1xAuthPreAuthVlan = _AtrDot1xAuthPreAuthVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 15),
    _AtrDot1xAuthPreAuthVlan_Type()
)
atrDot1xAuthPreAuthVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthPreAuthVlan.setStatus("current")
_AtrDot1xAuthPostAuthVlan_Type = DisplayString
_AtrDot1xAuthPostAuthVlan_Object = MibTableColumn
atrDot1xAuthPostAuthVlan = _AtrDot1xAuthPostAuthVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 16),
    _AtrDot1xAuthPostAuthVlan_Type()
)
atrDot1xAuthPostAuthVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthPostAuthVlan.setStatus("current")


class _AtrDot1xAuthLastAuthReason_Type(Integer32):
    """Custom type atrDot1xAuthLastAuthReason based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("adminReset", 2),
          ("authTimeout", 4),
          ("conflictingVlan", 9),
          ("forcedAuthed", 12),
          ("forcedUnauth", 10),
          ("invalidVlan", 8),
          ("logoff", 3),
          ("never", 1),
          ("noActiveServers", 7),
          ("serverAuthed", 11),
          ("serverReject", 5),
          ("serverTimeout", 6))
    )


_AtrDot1xAuthLastAuthReason_Type.__name__ = "Integer32"
_AtrDot1xAuthLastAuthReason_Object = MibTableColumn
atrDot1xAuthLastAuthReason = _AtrDot1xAuthLastAuthReason_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 17),
    _AtrDot1xAuthLastAuthReason_Type()
)
atrDot1xAuthLastAuthReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthLastAuthReason.setStatus("current")
_AtrDot1XAuthVlanAssignment_Type = TruthValue
_AtrDot1XAuthVlanAssignment_Object = MibTableColumn
atrDot1XAuthVlanAssignment = _AtrDot1XAuthVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 18),
    _AtrDot1XAuthVlanAssignment_Type()
)
atrDot1XAuthVlanAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1XAuthVlanAssignment.setStatus("current")
_AtrDot1XAuthSecureVlan_Type = TruthValue
_AtrDot1XAuthSecureVlan_Object = MibTableColumn
atrDot1XAuthSecureVlan = _AtrDot1XAuthSecureVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 19),
    _AtrDot1XAuthSecureVlan_Type()
)
atrDot1XAuthSecureVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1XAuthSecureVlan.setStatus("current")
_AtrDot1xAuthGuestVlan_Type = DisplayString
_AtrDot1xAuthGuestVlan_Object = MibTableColumn
atrDot1xAuthGuestVlan = _AtrDot1xAuthGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 20),
    _AtrDot1xAuthGuestVlan_Type()
)
atrDot1xAuthGuestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xAuthGuestVlan.setStatus("current")
_AtrDot1XAuthMibReset_Type = TruthValue
_AtrDot1XAuthMibReset_Object = MibTableColumn
atrDot1XAuthMibReset = _AtrDot1XAuthMibReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 21),
    _AtrDot1XAuthMibReset_Type()
)
atrDot1XAuthMibReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1XAuthMibReset.setStatus("current")


class _AtrDot1xAuthTrap_Type(Integer32):
    """Custom type atrDot1xAuthTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("failure", 2),
          ("none", 4),
          ("success", 1))
    )


_AtrDot1xAuthTrap_Type.__name__ = "Integer32"
_AtrDot1xAuthTrap_Object = MibTableColumn
atrDot1xAuthTrap = _AtrDot1xAuthTrap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 1, 1, 22),
    _AtrDot1xAuthTrap_Type()
)
atrDot1xAuthTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrDot1xAuthTrap.setStatus("current")
_AtrDot1xAuthStatsTable_Object = MibTable
atrDot1xAuthStatsTable = _AtrDot1xAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    atrDot1xAuthStatsTable.setStatus("current")
_AtrDot1xAuthStatsEntry_Object = MibTableRow
atrDot1xAuthStatsEntry = _AtrDot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1)
)
atrDot1xAuthStatsEntry.setIndexNames(
    (0, "AT-PAE-MIB", "atrDot1xPaePortNumber"),
    (0, "AT-PAE-MIB", "atrDot1xPaePortSuppMacAddress"),
)
if mibBuilder.loadTexts:
    atrDot1xAuthStatsEntry.setStatus("current")
_AtrDot1xAuthEapolFramesRx_Type = Counter32
_AtrDot1xAuthEapolFramesRx_Object = MibTableColumn
atrDot1xAuthEapolFramesRx = _AtrDot1xAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 1),
    _AtrDot1xAuthEapolFramesRx_Type()
)
atrDot1xAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthEapolFramesRx.setStatus("current")
_AtrDot1xAuthEapolFramesTx_Type = Counter32
_AtrDot1xAuthEapolFramesTx_Object = MibTableColumn
atrDot1xAuthEapolFramesTx = _AtrDot1xAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 2),
    _AtrDot1xAuthEapolFramesTx_Type()
)
atrDot1xAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthEapolFramesTx.setStatus("current")
_AtrDot1xAuthEapolStartFramesRx_Type = Counter32
_AtrDot1xAuthEapolStartFramesRx_Object = MibTableColumn
atrDot1xAuthEapolStartFramesRx = _AtrDot1xAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 3),
    _AtrDot1xAuthEapolStartFramesRx_Type()
)
atrDot1xAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthEapolStartFramesRx.setStatus("current")
_AtrDot1xAuthEapolLogoffFramesRx_Type = Counter32
_AtrDot1xAuthEapolLogoffFramesRx_Object = MibTableColumn
atrDot1xAuthEapolLogoffFramesRx = _AtrDot1xAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 4),
    _AtrDot1xAuthEapolLogoffFramesRx_Type()
)
atrDot1xAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthEapolLogoffFramesRx.setStatus("current")
_AtrDot1xAuthEapolRespIdFramesRx_Type = Counter32
_AtrDot1xAuthEapolRespIdFramesRx_Object = MibTableColumn
atrDot1xAuthEapolRespIdFramesRx = _AtrDot1xAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 5),
    _AtrDot1xAuthEapolRespIdFramesRx_Type()
)
atrDot1xAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthEapolRespIdFramesRx.setStatus("current")
_AtrDot1xAuthEapolRespFramesRx_Type = Counter32
_AtrDot1xAuthEapolRespFramesRx_Object = MibTableColumn
atrDot1xAuthEapolRespFramesRx = _AtrDot1xAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 6),
    _AtrDot1xAuthEapolRespFramesRx_Type()
)
atrDot1xAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthEapolRespFramesRx.setStatus("current")
_AtrDot1xAuthEapolReqIdFramesTx_Type = Counter32
_AtrDot1xAuthEapolReqIdFramesTx_Object = MibTableColumn
atrDot1xAuthEapolReqIdFramesTx = _AtrDot1xAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 7),
    _AtrDot1xAuthEapolReqIdFramesTx_Type()
)
atrDot1xAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthEapolReqIdFramesTx.setStatus("current")
_AtrDot1xAuthEapolReqFramesTx_Type = Counter32
_AtrDot1xAuthEapolReqFramesTx_Object = MibTableColumn
atrDot1xAuthEapolReqFramesTx = _AtrDot1xAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 8),
    _AtrDot1xAuthEapolReqFramesTx_Type()
)
atrDot1xAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthEapolReqFramesTx.setStatus("current")
_AtrDot1xAuthInvalidEapolFramesRx_Type = Counter32
_AtrDot1xAuthInvalidEapolFramesRx_Object = MibTableColumn
atrDot1xAuthInvalidEapolFramesRx = _AtrDot1xAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 9),
    _AtrDot1xAuthInvalidEapolFramesRx_Type()
)
atrDot1xAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthInvalidEapolFramesRx.setStatus("current")
_AtrDot1xAuthEapLengthErrorFramesRx_Type = Counter32
_AtrDot1xAuthEapLengthErrorFramesRx_Object = MibTableColumn
atrDot1xAuthEapLengthErrorFramesRx = _AtrDot1xAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 10),
    _AtrDot1xAuthEapLengthErrorFramesRx_Type()
)
atrDot1xAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthEapLengthErrorFramesRx.setStatus("current")
_AtrDot1xAuthLastEapolFrameVersion_Type = Unsigned32
_AtrDot1xAuthLastEapolFrameVersion_Object = MibTableColumn
atrDot1xAuthLastEapolFrameVersion = _AtrDot1xAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 2, 2, 1, 11),
    _AtrDot1xAuthLastEapolFrameVersion_Type()
)
atrDot1xAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrDot1xAuthLastEapolFrameVersion.setStatus("current")
_AtrDot1xTraps_ObjectIdentity = ObjectIdentity
atrDot1xTraps = _AtrDot1xTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 3)
)
_AtrMacBasedAuthPaeSystem_ObjectIdentity = ObjectIdentity
atrMacBasedAuthPaeSystem = _AtrMacBasedAuthPaeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 4)
)
_AtrMacBasedAuthPaePortTable_Object = MibTable
atrMacBasedAuthPaePortTable = _AtrMacBasedAuthPaePortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    atrMacBasedAuthPaePortTable.setStatus("current")
_AtrMacBasedAuthPaePortEntry_Object = MibTableRow
atrMacBasedAuthPaePortEntry = _AtrMacBasedAuthPaePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 4, 1, 1)
)
atrMacBasedAuthPaePortEntry.setIndexNames(
    (0, "AT-PAE-MIB", "atrMacBasedAuthPaePortNumber"),
    (0, "AT-PAE-MIB", "atrMacBasedAuthPaePortSuppMacAddress"),
)
if mibBuilder.loadTexts:
    atrMacBasedAuthPaePortEntry.setStatus("current")
_AtrMacBasedAuthPaePortNumber_Type = InterfaceIndex
_AtrMacBasedAuthPaePortNumber_Object = MibTableColumn
atrMacBasedAuthPaePortNumber = _AtrMacBasedAuthPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 4, 1, 1, 1),
    _AtrMacBasedAuthPaePortNumber_Type()
)
atrMacBasedAuthPaePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrMacBasedAuthPaePortNumber.setStatus("current")
_AtrMacBasedAuthPaePortInitialise_Type = TruthValue
_AtrMacBasedAuthPaePortInitialise_Object = MibTableColumn
atrMacBasedAuthPaePortInitialise = _AtrMacBasedAuthPaePortInitialise_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 4, 1, 1, 2),
    _AtrMacBasedAuthPaePortInitialise_Type()
)
atrMacBasedAuthPaePortInitialise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrMacBasedAuthPaePortInitialise.setStatus("current")
_AtrMacBasedAuthPaePortReauthenticate_Type = TruthValue
_AtrMacBasedAuthPaePortReauthenticate_Object = MibTableColumn
atrMacBasedAuthPaePortReauthenticate = _AtrMacBasedAuthPaePortReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 4, 1, 1, 3),
    _AtrMacBasedAuthPaePortReauthenticate_Type()
)
atrMacBasedAuthPaePortReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrMacBasedAuthPaePortReauthenticate.setStatus("current")
_AtrMacBasedAuthPaePortSuppMacAddress_Type = MacAddress
_AtrMacBasedAuthPaePortSuppMacAddress_Object = MibTableColumn
atrMacBasedAuthPaePortSuppMacAddress = _AtrMacBasedAuthPaePortSuppMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 4, 1, 1, 4),
    _AtrMacBasedAuthPaePortSuppMacAddress_Type()
)
atrMacBasedAuthPaePortSuppMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrMacBasedAuthPaePortSuppMacAddress.setStatus("current")
_AtrMacBasedAuthPaeAuthenticator_ObjectIdentity = ObjectIdentity
atrMacBasedAuthPaeAuthenticator = _AtrMacBasedAuthPaeAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5)
)
_AtrMacBasedAuthConfigTable_Object = MibTable
atrMacBasedAuthConfigTable = _AtrMacBasedAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    atrMacBasedAuthConfigTable.setStatus("current")
_AtrMacBasedAuthConfigEntry_Object = MibTableRow
atrMacBasedAuthConfigEntry = _AtrMacBasedAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1)
)
atrMacBasedAuthConfigEntry.setIndexNames(
    (0, "AT-PAE-MIB", "atrMacBasedAuthPaePortNumber"),
    (0, "AT-PAE-MIB", "atrMacBasedAuthPaePortSuppMacAddress"),
)
if mibBuilder.loadTexts:
    atrMacBasedAuthConfigEntry.setStatus("current")


class _AtrMacBasedAuthPaeState_Type(Integer32):
    """Custom type atrMacBasedAuthPaeState based on Integer32"""
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
          ("initialise", 1))
    )


_AtrMacBasedAuthPaeState_Type.__name__ = "Integer32"
_AtrMacBasedAuthPaeState_Object = MibTableColumn
atrMacBasedAuthPaeState = _AtrMacBasedAuthPaeState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 1),
    _AtrMacBasedAuthPaeState_Type()
)
atrMacBasedAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrMacBasedAuthPaeState.setStatus("current")


class _AtrMacBasedAuthBackendAuthState_Type(Integer32):
    """Custom type atrMacBasedAuthBackendAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("idle", 5),
          ("initialise", 6),
          ("request", 1),
          ("success", 2),
          ("timeout", 4))
    )


_AtrMacBasedAuthBackendAuthState_Type.__name__ = "Integer32"
_AtrMacBasedAuthBackendAuthState_Object = MibTableColumn
atrMacBasedAuthBackendAuthState = _AtrMacBasedAuthBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 2),
    _AtrMacBasedAuthBackendAuthState_Type()
)
atrMacBasedAuthBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrMacBasedAuthBackendAuthState.setStatus("current")
_AtrMacBasedAuthControlledPortStatus_Type = AtrPaeControlledPortStatus
_AtrMacBasedAuthControlledPortStatus_Object = MibTableColumn
atrMacBasedAuthControlledPortStatus = _AtrMacBasedAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 3),
    _AtrMacBasedAuthControlledPortStatus_Type()
)
atrMacBasedAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrMacBasedAuthControlledPortStatus.setStatus("current")
_AtrMacBasedAuthControlledPortControl_Type = AtrPaeControlledPortControl
_AtrMacBasedAuthControlledPortControl_Object = MibTableColumn
atrMacBasedAuthControlledPortControl = _AtrMacBasedAuthControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 4),
    _AtrMacBasedAuthControlledPortControl_Type()
)
atrMacBasedAuthControlledPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrMacBasedAuthControlledPortControl.setStatus("current")


class _AtrMacBasedAuthQuietPeriod_Type(Unsigned32):
    """Custom type atrMacBasedAuthQuietPeriod based on Unsigned32"""
    defaultValue = 60


_AtrMacBasedAuthQuietPeriod_Object = MibTableColumn
atrMacBasedAuthQuietPeriod = _AtrMacBasedAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 5),
    _AtrMacBasedAuthQuietPeriod_Type()
)
atrMacBasedAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrMacBasedAuthQuietPeriod.setStatus("current")


class _AtrMacBasedAuthReAuthPeriod_Type(Unsigned32):
    """Custom type atrMacBasedAuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_AtrMacBasedAuthReAuthPeriod_Object = MibTableColumn
atrMacBasedAuthReAuthPeriod = _AtrMacBasedAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 6),
    _AtrMacBasedAuthReAuthPeriod_Type()
)
atrMacBasedAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrMacBasedAuthReAuthPeriod.setStatus("current")


class _AtrMacBasedAuthReAuthEnabled_Type(TruthValue):
    """Custom type atrMacBasedAuthReAuthEnabled based on TruthValue"""


_AtrMacBasedAuthReAuthEnabled_Object = MibTableColumn
atrMacBasedAuthReAuthEnabled = _AtrMacBasedAuthReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 7),
    _AtrMacBasedAuthReAuthEnabled_Type()
)
atrMacBasedAuthReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrMacBasedAuthReAuthEnabled.setStatus("current")
_AtrMacBasedAuthPreAuthVlan_Type = DisplayString
_AtrMacBasedAuthPreAuthVlan_Object = MibTableColumn
atrMacBasedAuthPreAuthVlan = _AtrMacBasedAuthPreAuthVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 8),
    _AtrMacBasedAuthPreAuthVlan_Type()
)
atrMacBasedAuthPreAuthVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrMacBasedAuthPreAuthVlan.setStatus("current")
_AtrMacBasedAuthPostAuthVlan_Type = DisplayString
_AtrMacBasedAuthPostAuthVlan_Object = MibTableColumn
atrMacBasedAuthPostAuthVlan = _AtrMacBasedAuthPostAuthVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 9),
    _AtrMacBasedAuthPostAuthVlan_Type()
)
atrMacBasedAuthPostAuthVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrMacBasedAuthPostAuthVlan.setStatus("current")


class _AtrMacBasedAuthLastAuthReason_Type(Integer32):
    """Custom type atrMacBasedAuthLastAuthReason based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("adminReset", 2),
          ("authTimeout", 4),
          ("conflictingVlan", 9),
          ("forcedAuthed", 12),
          ("forcedUnauth", 10),
          ("invalidVlan", 8),
          ("logoff", 3),
          ("never", 1),
          ("noActiveServers", 7),
          ("serverAuthed", 11),
          ("serverReject", 5),
          ("serverTimeout", 6))
    )


_AtrMacBasedAuthLastAuthReason_Type.__name__ = "Integer32"
_AtrMacBasedAuthLastAuthReason_Object = MibTableColumn
atrMacBasedAuthLastAuthReason = _AtrMacBasedAuthLastAuthReason_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 10),
    _AtrMacBasedAuthLastAuthReason_Type()
)
atrMacBasedAuthLastAuthReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atrMacBasedAuthLastAuthReason.setStatus("current")
_AtrMacBasedAuthVlanAssignment_Type = TruthValue
_AtrMacBasedAuthVlanAssignment_Object = MibTableColumn
atrMacBasedAuthVlanAssignment = _AtrMacBasedAuthVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 11),
    _AtrMacBasedAuthVlanAssignment_Type()
)
atrMacBasedAuthVlanAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrMacBasedAuthVlanAssignment.setStatus("current")
_AtrMacBasedAuthSecureVlan_Type = TruthValue
_AtrMacBasedAuthSecureVlan_Object = MibTableColumn
atrMacBasedAuthSecureVlan = _AtrMacBasedAuthSecureVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 12),
    _AtrMacBasedAuthSecureVlan_Type()
)
atrMacBasedAuthSecureVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrMacBasedAuthSecureVlan.setStatus("current")
_AtrMacBasedAuthMibReset_Type = TruthValue
_AtrMacBasedAuthMibReset_Object = MibTableColumn
atrMacBasedAuthMibReset = _AtrMacBasedAuthMibReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 13),
    _AtrMacBasedAuthMibReset_Type()
)
atrMacBasedAuthMibReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrMacBasedAuthMibReset.setStatus("current")


class _AtrMacBasedAuthTrap_Type(Integer32):
    """Custom type atrMacBasedAuthTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("failure", 2),
          ("none", 4),
          ("success", 1))
    )


_AtrMacBasedAuthTrap_Type.__name__ = "Integer32"
_AtrMacBasedAuthTrap_Object = MibTableColumn
atrMacBasedAuthTrap = _AtrMacBasedAuthTrap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 5, 1, 1, 14),
    _AtrMacBasedAuthTrap_Type()
)
atrMacBasedAuthTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atrMacBasedAuthTrap.setStatus("current")
_AtrMacBasedAuthTraps_ObjectIdentity = ObjectIdentity
atrMacBasedAuthTraps = _AtrMacBasedAuthTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 6)
)

# Managed Objects groups


# Notification objects

atrDot1xAuthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 3, 1)
)
atrDot1xAuthenticated.setObjects(
      *(("AT-PAE-MIB", "atrDot1xPaePortNumber"),
        ("AT-PAE-MIB", "atrDot1xPaePortSuppMacAddress"),
        ("AT-PAE-MIB", "atrDot1xAuthPreAuthVlan"),
        ("AT-PAE-MIB", "atrDot1xAuthPostAuthVlan"),
        ("AT-PAE-MIB", "atrDot1xAuthLastAuthReason"))
)
if mibBuilder.loadTexts:
    atrDot1xAuthenticated.setStatus(
        "current"
    )

atrDot1xUnauthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 3, 2)
)
atrDot1xUnauthenticated.setObjects(
      *(("AT-PAE-MIB", "atrDot1xPaePortNumber"),
        ("AT-PAE-MIB", "atrDot1xPaePortSuppMacAddress"),
        ("AT-PAE-MIB", "atrDot1xAuthPreAuthVlan"),
        ("AT-PAE-MIB", "atrDot1xAuthPostAuthVlan"),
        ("AT-PAE-MIB", "atrDot1xAuthLastAuthReason"))
)
if mibBuilder.loadTexts:
    atrDot1xUnauthenticated.setStatus(
        "current"
    )

atrDot1xFailedAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 3, 3)
)
atrDot1xFailedAuth.setObjects(
      *(("AT-PAE-MIB", "atrDot1xPaePortNumber"),
        ("AT-PAE-MIB", "atrDot1xPaePortSuppMacAddress"),
        ("AT-PAE-MIB", "atrDot1xAuthPreAuthVlan"),
        ("AT-PAE-MIB", "atrDot1xAuthPostAuthVlan"),
        ("AT-PAE-MIB", "atrDot1xAuthLastAuthReason"))
)
if mibBuilder.loadTexts:
    atrDot1xFailedAuth.setStatus(
        "current"
    )

atrMacBasedAuthAuthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 6, 1)
)
atrMacBasedAuthAuthenticated.setObjects(
      *(("AT-PAE-MIB", "atrMacBasedAuthPaePortNumber"),
        ("AT-PAE-MIB", "atrMacBasedAuthPaePortSuppMacAddress"),
        ("AT-PAE-MIB", "atrMacBasedAuthPreAuthVlan"),
        ("AT-PAE-MIB", "atrMacBasedAuthPostAuthVlan"),
        ("AT-PAE-MIB", "atrMacBasedAuthLastAuthReason"))
)
if mibBuilder.loadTexts:
    atrMacBasedAuthAuthenticated.setStatus(
        "current"
    )

atrMacBasedAuthUnauthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 6, 2)
)
atrMacBasedAuthUnauthenticated.setObjects(
      *(("AT-PAE-MIB", "atrMacBasedAuthPaePortNumber"),
        ("AT-PAE-MIB", "atrMacBasedAuthPaePortSuppMacAddress"),
        ("AT-PAE-MIB", "atrMacBasedAuthPreAuthVlan"),
        ("AT-PAE-MIB", "atrMacBasedAuthPostAuthVlan"),
        ("AT-PAE-MIB", "atrMacBasedAuthLastAuthReason"))
)
if mibBuilder.loadTexts:
    atrMacBasedAuthUnauthenticated.setStatus(
        "current"
    )

atrMacBasedAuthFailedAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 118, 1, 1, 6, 3)
)
atrMacBasedAuthFailedAuth.setObjects(
      *(("AT-PAE-MIB", "atrMacBasedAuthPaePortNumber"),
        ("AT-PAE-MIB", "atrMacBasedAuthPaePortSuppMacAddress"),
        ("AT-PAE-MIB", "atrMacBasedAuthPreAuthVlan"),
        ("AT-PAE-MIB", "atrMacBasedAuthPostAuthVlan"),
        ("AT-PAE-MIB", "atrMacBasedAuthLastAuthReason"))
)
if mibBuilder.loadTexts:
    atrMacBasedAuthFailedAuth.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-PAE-MIB",
    **{"AtrPaeControlledDirections": AtrPaeControlledDirections,
       "AtrPaeControlledPortStatus": AtrPaeControlledPortStatus,
       "AtrPaeControlledPortControl": AtrPaeControlledPortControl,
       "portAuth": portAuth,
       "atrPaeMib": atrPaeMib,
       "atrPaeMIBObjects": atrPaeMIBObjects,
       "atrDot1xPaeSystem": atrDot1xPaeSystem,
       "atrDot1xPaePortTable": atrDot1xPaePortTable,
       "atrDot1xPaePortEntry": atrDot1xPaePortEntry,
       "atrDot1xPaePortNumber": atrDot1xPaePortNumber,
       "atrDot1xPaePortProtocolVersion": atrDot1xPaePortProtocolVersion,
       "atrDot1xPaePortCapabilities": atrDot1xPaePortCapabilities,
       "atrDot1xPaePortInitialise": atrDot1xPaePortInitialise,
       "atrDot1xPaePortReauthenticate": atrDot1xPaePortReauthenticate,
       "atrDot1xPaePortSuppMacAddress": atrDot1xPaePortSuppMacAddress,
       "atrDot1xPaeAuthenticator": atrDot1xPaeAuthenticator,
       "atrDot1xAuthConfigTable": atrDot1xAuthConfigTable,
       "atrDot1xAuthConfigEntry": atrDot1xAuthConfigEntry,
       "atrDot1xAuthPaeState": atrDot1xAuthPaeState,
       "atrDot1xAuthBackendAuthState": atrDot1xAuthBackendAuthState,
       "atrDot1xAuthAdminControlledDirections": atrDot1xAuthAdminControlledDirections,
       "atrDot1xAuthOperControlledDirections": atrDot1xAuthOperControlledDirections,
       "atrDot1xAuthAuthControlledPortStatus": atrDot1xAuthAuthControlledPortStatus,
       "atrDot1xAuthAuthControlledPortControl": atrDot1xAuthAuthControlledPortControl,
       "atrDot1xAuthQuietPeriod": atrDot1xAuthQuietPeriod,
       "atrDot1xAuthTxPeriod": atrDot1xAuthTxPeriod,
       "atrDot1xAuthSuppTimeout": atrDot1xAuthSuppTimeout,
       "atrDot1xAuthServerTimeout": atrDot1xAuthServerTimeout,
       "atrDot1xAuthMaxReq": atrDot1xAuthMaxReq,
       "atrDot1xAuthReAuthPeriod": atrDot1xAuthReAuthPeriod,
       "atrDot1xAuthReAuthEnabled": atrDot1xAuthReAuthEnabled,
       "atrDot1xAuthKeyTxEnabled": atrDot1xAuthKeyTxEnabled,
       "atrDot1xAuthPreAuthVlan": atrDot1xAuthPreAuthVlan,
       "atrDot1xAuthPostAuthVlan": atrDot1xAuthPostAuthVlan,
       "atrDot1xAuthLastAuthReason": atrDot1xAuthLastAuthReason,
       "atrDot1XAuthVlanAssignment": atrDot1XAuthVlanAssignment,
       "atrDot1XAuthSecureVlan": atrDot1XAuthSecureVlan,
       "atrDot1xAuthGuestVlan": atrDot1xAuthGuestVlan,
       "atrDot1XAuthMibReset": atrDot1XAuthMibReset,
       "atrDot1xAuthTrap": atrDot1xAuthTrap,
       "atrDot1xAuthStatsTable": atrDot1xAuthStatsTable,
       "atrDot1xAuthStatsEntry": atrDot1xAuthStatsEntry,
       "atrDot1xAuthEapolFramesRx": atrDot1xAuthEapolFramesRx,
       "atrDot1xAuthEapolFramesTx": atrDot1xAuthEapolFramesTx,
       "atrDot1xAuthEapolStartFramesRx": atrDot1xAuthEapolStartFramesRx,
       "atrDot1xAuthEapolLogoffFramesRx": atrDot1xAuthEapolLogoffFramesRx,
       "atrDot1xAuthEapolRespIdFramesRx": atrDot1xAuthEapolRespIdFramesRx,
       "atrDot1xAuthEapolRespFramesRx": atrDot1xAuthEapolRespFramesRx,
       "atrDot1xAuthEapolReqIdFramesTx": atrDot1xAuthEapolReqIdFramesTx,
       "atrDot1xAuthEapolReqFramesTx": atrDot1xAuthEapolReqFramesTx,
       "atrDot1xAuthInvalidEapolFramesRx": atrDot1xAuthInvalidEapolFramesRx,
       "atrDot1xAuthEapLengthErrorFramesRx": atrDot1xAuthEapLengthErrorFramesRx,
       "atrDot1xAuthLastEapolFrameVersion": atrDot1xAuthLastEapolFrameVersion,
       "atrDot1xTraps": atrDot1xTraps,
       "atrDot1xAuthenticated": atrDot1xAuthenticated,
       "atrDot1xUnauthenticated": atrDot1xUnauthenticated,
       "atrDot1xFailedAuth": atrDot1xFailedAuth,
       "atrMacBasedAuthPaeSystem": atrMacBasedAuthPaeSystem,
       "atrMacBasedAuthPaePortTable": atrMacBasedAuthPaePortTable,
       "atrMacBasedAuthPaePortEntry": atrMacBasedAuthPaePortEntry,
       "atrMacBasedAuthPaePortNumber": atrMacBasedAuthPaePortNumber,
       "atrMacBasedAuthPaePortInitialise": atrMacBasedAuthPaePortInitialise,
       "atrMacBasedAuthPaePortReauthenticate": atrMacBasedAuthPaePortReauthenticate,
       "atrMacBasedAuthPaePortSuppMacAddress": atrMacBasedAuthPaePortSuppMacAddress,
       "atrMacBasedAuthPaeAuthenticator": atrMacBasedAuthPaeAuthenticator,
       "atrMacBasedAuthConfigTable": atrMacBasedAuthConfigTable,
       "atrMacBasedAuthConfigEntry": atrMacBasedAuthConfigEntry,
       "atrMacBasedAuthPaeState": atrMacBasedAuthPaeState,
       "atrMacBasedAuthBackendAuthState": atrMacBasedAuthBackendAuthState,
       "atrMacBasedAuthControlledPortStatus": atrMacBasedAuthControlledPortStatus,
       "atrMacBasedAuthControlledPortControl": atrMacBasedAuthControlledPortControl,
       "atrMacBasedAuthQuietPeriod": atrMacBasedAuthQuietPeriod,
       "atrMacBasedAuthReAuthPeriod": atrMacBasedAuthReAuthPeriod,
       "atrMacBasedAuthReAuthEnabled": atrMacBasedAuthReAuthEnabled,
       "atrMacBasedAuthPreAuthVlan": atrMacBasedAuthPreAuthVlan,
       "atrMacBasedAuthPostAuthVlan": atrMacBasedAuthPostAuthVlan,
       "atrMacBasedAuthLastAuthReason": atrMacBasedAuthLastAuthReason,
       "atrMacBasedAuthVlanAssignment": atrMacBasedAuthVlanAssignment,
       "atrMacBasedAuthSecureVlan": atrMacBasedAuthSecureVlan,
       "atrMacBasedAuthMibReset": atrMacBasedAuthMibReset,
       "atrMacBasedAuthTrap": atrMacBasedAuthTrap,
       "atrMacBasedAuthTraps": atrMacBasedAuthTraps,
       "atrMacBasedAuthAuthenticated": atrMacBasedAuthAuthenticated,
       "atrMacBasedAuthUnauthenticated": atrMacBasedAuthUnauthenticated,
       "atrMacBasedAuthFailedAuth": atrMacBasedAuthFailedAuth}
)
