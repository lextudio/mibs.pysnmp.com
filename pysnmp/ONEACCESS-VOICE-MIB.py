# SNMP MIB module (ONEACCESS-VOICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-VOICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:07 2024
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

(oacExpIMVoice,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMVoice",
    "oacMIBModules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

oacVoiceMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 801)
)
oacVoiceMIBModule.setRevisions(
        ("2013-05-03 00:00",
         "2011-10-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VoiceFxsPortStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2),
          ("undefined", 0))
    )



class VoiceFxsPathStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("established", 1),
          ("idle", 0))
    )



class VoicePriPhPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e1", 3),
          ("t1", 4))
    )



class VoicePriProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e1Cas", 4),
          ("e1Pri", 3),
          ("none", 255),
          ("t1Cas", 6),
          ("t1Pri", 5))
    )



class VoiceBriProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("briNt", 1),
          ("briTe", 2))
    )



class VoiceFxsProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("offHook", 4),
          ("onHook", 3),
          ("ringing", 5))
    )



class VoiceAcDeacState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )



class VoiceUpDnState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class VoiceBriPortStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("activated", 3),
          ("blocked", 1),
          ("deactivated", 4),
          ("unblocked", 2),
          ("undefined", 0))
    )



class VoiceIOCoder(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ces", 5),
          ("fax", 6),
          ("g711-64", 1),
          ("g726-32", 2),
          ("g726-40", 3),
          ("none", 0),
          ("sid", 4))
    )



class VoiceBearerCap(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unrestricted", 2),
          ("voice", 0),
          ("voice-band", 1))
    )



class VoiceChnType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("signalling", 0),
          ("voice", 1))
    )



class VoipPortType(Integer32, TextualConvention):
    status = "current"
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
        *(("bri", 3),
          ("fxo", 1),
          ("fxs", 2),
          ("pri", 4))
    )



class IsdnProtocolDescriptor(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("briNt", 1),
          ("briTe", 2),
          ("e1Cas", 4),
          ("e1Pri", 3),
          ("none", 255),
          ("t1Cas", 6),
          ("t1Pri", 5))
    )



class PortVoipCurrentState(Integer32, TextualConvention):
    status = "current"
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
        *(("activated", 1),
          ("deactivated", 2),
          ("offhook", 4),
          ("onhook", 3),
          ("ringing", 5),
          ("undefined", 0))
    )



class ConfigState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class IsdnLayerStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2),
          ("undefined", 0))
    )



class OacVoipGatewayState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )



class OacVoipPriPhysicalType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("ptE1", 0),
          ("ptT1", 1))
    )



class OacVoipGatewayStateReason(Integer32, TextualConvention):
    status = "current"
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
        *(("autoconfigDown", 2),
          ("interfaceDown", 3),
          ("invalidIpAddress", 4),
          ("shutdown", 1),
          ("unknown", 0))
    )



class OacVoipGatewayRegistrationState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("registered", 1),
          ("unregistered", 0))
    )



class OacH323GwRasBwControl(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )



class OacH323GwPortabilityStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("done", 3),
          ("enable", 1),
          ("inProgress", 2),
          ("undefined", 0))
    )



class OacVoipMgcpGatewayConnectionState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 0))
    )



class OacVoiceSipGwPhoneState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("registered", 1),
          ("registering", 0))
    )



# MIB Managed Objects in the order of their OIDs

_OacExpIMVoiceStatistics_ObjectIdentity = ObjectIdentity
oacExpIMVoiceStatistics = _OacExpIMVoiceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2)
)
_OacVoiceStatObjects_ObjectIdentity = ObjectIdentity
oacVoiceStatObjects = _OacVoiceStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1)
)
_OacVoiceStatGlobal_ObjectIdentity = ObjectIdentity
oacVoiceStatGlobal = _OacVoiceStatGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 1)
)
_OacVoiceFxsPorts_Type = Integer32
_OacVoiceFxsPorts_Object = MibScalar
oacVoiceFxsPorts = _OacVoiceFxsPorts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 1, 1),
    _OacVoiceFxsPorts_Type()
)
oacVoiceFxsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceFxsPorts.setStatus("current")
_OacVoiceBriPorts_Type = Integer32
_OacVoiceBriPorts_Object = MibScalar
oacVoiceBriPorts = _OacVoiceBriPorts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 1, 2),
    _OacVoiceBriPorts_Type()
)
oacVoiceBriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceBriPorts.setStatus("current")
_OacVoicePriPorts_Type = Integer32
_OacVoicePriPorts_Object = MibScalar
oacVoicePriPorts = _OacVoicePriPorts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 1, 3),
    _OacVoicePriPorts_Type()
)
oacVoicePriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePriPorts.setStatus("current")
_OacVoiceVmoaConnections_Type = Integer32
_OacVoiceVmoaConnections_Object = MibScalar
oacVoiceVmoaConnections = _OacVoiceVmoaConnections_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 1, 4),
    _OacVoiceVmoaConnections_Type()
)
oacVoiceVmoaConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnections.setStatus("current")
_OacVoiceVtoaConnections_Type = Integer32
_OacVoiceVtoaConnections_Object = MibScalar
oacVoiceVtoaConnections = _OacVoiceVtoaConnections_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 1, 5),
    _OacVoiceVtoaConnections_Type()
)
oacVoiceVtoaConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnections.setStatus("current")
_OacVoiceFxsDialPeers_Type = Integer32
_OacVoiceFxsDialPeers_Object = MibScalar
oacVoiceFxsDialPeers = _OacVoiceFxsDialPeers_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 1, 6),
    _OacVoiceFxsDialPeers_Type()
)
oacVoiceFxsDialPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceFxsDialPeers.setStatus("current")
_OacVoiceBriDialPeers_Type = Integer32
_OacVoiceBriDialPeers_Object = MibScalar
oacVoiceBriDialPeers = _OacVoiceBriDialPeers_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 1, 7),
    _OacVoiceBriDialPeers_Type()
)
oacVoiceBriDialPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceBriDialPeers.setStatus("current")
_OacVoicePriDialPeers_Type = Integer32
_OacVoicePriDialPeers_Object = MibScalar
oacVoicePriDialPeers = _OacVoicePriDialPeers_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 1, 8),
    _OacVoicePriDialPeers_Type()
)
oacVoicePriDialPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePriDialPeers.setStatus("current")
_OacVoiceStatBles_ObjectIdentity = ObjectIdentity
oacVoiceStatBles = _OacVoiceStatBles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2)
)
_OacVoicePortBles_ObjectIdentity = ObjectIdentity
oacVoicePortBles = _OacVoicePortBles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1)
)
_OacVoiceVoicePortFxsTable_Object = MibTable
oacVoiceVoicePortFxsTable = _OacVoiceVoicePortFxsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    oacVoiceVoicePortFxsTable.setStatus("current")
_OacVoiceVoicePortFxsEntry_Object = MibTableRow
oacVoiceVoicePortFxsEntry = _OacVoiceVoicePortFxsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 1, 1)
)
oacVoiceVoicePortFxsEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceVoicePortFxsIfIndex"),
)
if mibBuilder.loadTexts:
    oacVoiceVoicePortFxsEntry.setStatus("current")


class _OacVoiceVoicePortFxsIfIndex_Type(Integer32):
    """Custom type oacVoiceVoicePortFxsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVoiceVoicePortFxsIfIndex_Type.__name__ = "Integer32"
_OacVoiceVoicePortFxsIfIndex_Object = MibTableColumn
oacVoiceVoicePortFxsIfIndex = _OacVoiceVoicePortFxsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 1, 1, 1),
    _OacVoiceVoicePortFxsIfIndex_Type()
)
oacVoiceVoicePortFxsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortFxsIfIndex.setStatus("current")


class _OacVoiceVoicePortVoicePortFxs_Type(DisplayString):
    """Custom type oacVoiceVoicePortVoicePortFxs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_OacVoiceVoicePortVoicePortFxs_Type.__name__ = "DisplayString"
_OacVoiceVoicePortVoicePortFxs_Object = MibTableColumn
oacVoiceVoicePortVoicePortFxs = _OacVoiceVoicePortVoicePortFxs_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 1, 1, 2),
    _OacVoiceVoicePortVoicePortFxs_Type()
)
oacVoiceVoicePortVoicePortFxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortVoicePortFxs.setStatus("current")
_OacVoiceVoicePortFxsProtocolState_Type = VoiceFxsProtocol
_OacVoiceVoicePortFxsProtocolState_Object = MibTableColumn
oacVoiceVoicePortFxsProtocolState = _OacVoiceVoicePortFxsProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 1, 1, 3),
    _OacVoiceVoicePortFxsProtocolState_Type()
)
oacVoiceVoicePortFxsProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortFxsProtocolState.setStatus("current")
_OacVoiceVoicePortFxsOperState_Type = VoiceAcDeacState
_OacVoiceVoicePortFxsOperState_Object = MibTableColumn
oacVoiceVoicePortFxsOperState = _OacVoiceVoicePortFxsOperState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 1, 1, 4),
    _OacVoiceVoicePortFxsOperState_Type()
)
oacVoiceVoicePortFxsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortFxsOperState.setStatus("current")
_OacVoiceVoicePortFxsAdminState_Type = VoiceAcDeacState
_OacVoiceVoicePortFxsAdminState_Object = MibTableColumn
oacVoiceVoicePortFxsAdminState = _OacVoiceVoicePortFxsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 1, 1, 5),
    _OacVoiceVoicePortFxsAdminState_Type()
)
oacVoiceVoicePortFxsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortFxsAdminState.setStatus("current")
_OacVoiceVoicePortFxsConfigState_Type = VoiceUpDnState
_OacVoiceVoicePortFxsConfigState_Object = MibTableColumn
oacVoiceVoicePortFxsConfigState = _OacVoiceVoicePortFxsConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 1, 1, 6),
    _OacVoiceVoicePortFxsConfigState_Type()
)
oacVoiceVoicePortFxsConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortFxsConfigState.setStatus("current")
_OacVoiceVoicePortFxsAttachedDialPeer_Type = Integer32
_OacVoiceVoicePortFxsAttachedDialPeer_Object = MibTableColumn
oacVoiceVoicePortFxsAttachedDialPeer = _OacVoiceVoicePortFxsAttachedDialPeer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 1, 1, 7),
    _OacVoiceVoicePortFxsAttachedDialPeer_Type()
)
oacVoiceVoicePortFxsAttachedDialPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortFxsAttachedDialPeer.setStatus("current")
_OacVoiceVoicePortFxsVoiceCommNb_Type = Unsigned32
_OacVoiceVoicePortFxsVoiceCommNb_Object = MibTableColumn
oacVoiceVoicePortFxsVoiceCommNb = _OacVoiceVoicePortFxsVoiceCommNb_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 1, 1, 8),
    _OacVoiceVoicePortFxsVoiceCommNb_Type()
)
oacVoiceVoicePortFxsVoiceCommNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortFxsVoiceCommNb.setStatus("current")
_OacVoiceVoicePortBriTable_Object = MibTable
oacVoiceVoicePortBriTable = _OacVoiceVoicePortBriTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriTable.setStatus("current")
_OacVoiceVoicePortBriEntry_Object = MibTableRow
oacVoiceVoicePortBriEntry = _OacVoiceVoicePortBriEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1)
)
oacVoiceVoicePortBriEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceVoicePortBriIfIndex"),
)
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriEntry.setStatus("current")


class _OacVoiceVoicePortBriIfIndex_Type(Integer32):
    """Custom type oacVoiceVoicePortBriIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVoiceVoicePortBriIfIndex_Type.__name__ = "Integer32"
_OacVoiceVoicePortBriIfIndex_Object = MibTableColumn
oacVoiceVoicePortBriIfIndex = _OacVoiceVoicePortBriIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1, 1),
    _OacVoiceVoicePortBriIfIndex_Type()
)
oacVoiceVoicePortBriIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriIfIndex.setStatus("current")


class _OacVoiceVoicePortVoicePortBri_Type(DisplayString):
    """Custom type oacVoiceVoicePortVoicePortBri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_OacVoiceVoicePortVoicePortBri_Type.__name__ = "DisplayString"
_OacVoiceVoicePortVoicePortBri_Object = MibTableColumn
oacVoiceVoicePortVoicePortBri = _OacVoiceVoicePortVoicePortBri_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1, 2),
    _OacVoiceVoicePortVoicePortBri_Type()
)
oacVoiceVoicePortVoicePortBri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortVoicePortBri.setStatus("current")
_OacVoiceVoicePortBriProtocolDescriptor_Type = VoiceBriProtocol
_OacVoiceVoicePortBriProtocolDescriptor_Object = MibTableColumn
oacVoiceVoicePortBriProtocolDescriptor = _OacVoiceVoicePortBriProtocolDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1, 3),
    _OacVoiceVoicePortBriProtocolDescriptor_Type()
)
oacVoiceVoicePortBriProtocolDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriProtocolDescriptor.setStatus("current")
_OacVoiceVoicePortBriProtocolState_Type = VoiceAcDeacState
_OacVoiceVoicePortBriProtocolState_Object = MibTableColumn
oacVoiceVoicePortBriProtocolState = _OacVoiceVoicePortBriProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1, 4),
    _OacVoiceVoicePortBriProtocolState_Type()
)
oacVoiceVoicePortBriProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriProtocolState.setStatus("current")
_OacVoiceVoicePortBriOperState_Type = VoiceAcDeacState
_OacVoiceVoicePortBriOperState_Object = MibTableColumn
oacVoiceVoicePortBriOperState = _OacVoiceVoicePortBriOperState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1, 5),
    _OacVoiceVoicePortBriOperState_Type()
)
oacVoiceVoicePortBriOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriOperState.setStatus("current")
_OacVoiceVoicePortBriAdminState_Type = VoiceAcDeacState
_OacVoiceVoicePortBriAdminState_Object = MibTableColumn
oacVoiceVoicePortBriAdminState = _OacVoiceVoicePortBriAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1, 6),
    _OacVoiceVoicePortBriAdminState_Type()
)
oacVoiceVoicePortBriAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriAdminState.setStatus("current")
_OacVoiceVoicePortBriConfigState_Type = VoiceUpDnState
_OacVoiceVoicePortBriConfigState_Object = MibTableColumn
oacVoiceVoicePortBriConfigState = _OacVoiceVoicePortBriConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1, 7),
    _OacVoiceVoicePortBriConfigState_Type()
)
oacVoiceVoicePortBriConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriConfigState.setStatus("current")
_OacVoiceVoicePortBriLayer1_Type = VoiceAcDeacState
_OacVoiceVoicePortBriLayer1_Object = MibTableColumn
oacVoiceVoicePortBriLayer1 = _OacVoiceVoicePortBriLayer1_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1, 8),
    _OacVoiceVoicePortBriLayer1_Type()
)
oacVoiceVoicePortBriLayer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriLayer1.setStatus("current")
_OacVoiceVoicePortBriAttachedDialPeer_Type = Integer32
_OacVoiceVoicePortBriAttachedDialPeer_Object = MibTableColumn
oacVoiceVoicePortBriAttachedDialPeer = _OacVoiceVoicePortBriAttachedDialPeer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1, 9),
    _OacVoiceVoicePortBriAttachedDialPeer_Type()
)
oacVoiceVoicePortBriAttachedDialPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriAttachedDialPeer.setStatus("current")
_OacVoiceVoicePortBriVoiceCommNb_Type = Unsigned32
_OacVoiceVoicePortBriVoiceCommNb_Object = MibTableColumn
oacVoiceVoicePortBriVoiceCommNb = _OacVoiceVoicePortBriVoiceCommNb_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 2, 1, 10),
    _OacVoiceVoicePortBriVoiceCommNb_Type()
)
oacVoiceVoicePortBriVoiceCommNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortBriVoiceCommNb.setStatus("current")
_OacVoiceVoicePortPriTable_Object = MibTable
oacVoiceVoicePortPriTable = _OacVoiceVoicePortPriTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriTable.setStatus("current")
_OacVoiceVoicePortPriEntry_Object = MibTableRow
oacVoiceVoicePortPriEntry = _OacVoiceVoicePortPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1)
)
oacVoiceVoicePortPriEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriIfIndex"),
)
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriEntry.setStatus("current")


class _OacVoiceVoicePortPriIfIndex_Type(Integer32):
    """Custom type oacVoiceVoicePortPriIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVoiceVoicePortPriIfIndex_Type.__name__ = "Integer32"
_OacVoiceVoicePortPriIfIndex_Object = MibTableColumn
oacVoiceVoicePortPriIfIndex = _OacVoiceVoicePortPriIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 1),
    _OacVoiceVoicePortPriIfIndex_Type()
)
oacVoiceVoicePortPriIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriIfIndex.setStatus("current")


class _OacVoiceVoicePortVoicePortPri_Type(DisplayString):
    """Custom type oacVoiceVoicePortVoicePortPri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_OacVoiceVoicePortVoicePortPri_Type.__name__ = "DisplayString"
_OacVoiceVoicePortVoicePortPri_Object = MibTableColumn
oacVoiceVoicePortVoicePortPri = _OacVoiceVoicePortVoicePortPri_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 2),
    _OacVoiceVoicePortVoicePortPri_Type()
)
oacVoiceVoicePortVoicePortPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortVoicePortPri.setStatus("current")
_OacVoiceVoicePortPriPhysicalType_Type = VoicePriPhPortType
_OacVoiceVoicePortPriPhysicalType_Object = MibTableColumn
oacVoiceVoicePortPriPhysicalType = _OacVoiceVoicePortPriPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 3),
    _OacVoiceVoicePortPriPhysicalType_Type()
)
oacVoiceVoicePortPriPhysicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriPhysicalType.setStatus("current")
_OacVoiceVoicePortPriProtocolDescriptor_Type = VoicePriProtocol
_OacVoiceVoicePortPriProtocolDescriptor_Object = MibTableColumn
oacVoiceVoicePortPriProtocolDescriptor = _OacVoiceVoicePortPriProtocolDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 4),
    _OacVoiceVoicePortPriProtocolDescriptor_Type()
)
oacVoiceVoicePortPriProtocolDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriProtocolDescriptor.setStatus("current")
_OacVoiceVoicePortPriProtocolState_Type = VoiceAcDeacState
_OacVoiceVoicePortPriProtocolState_Object = MibTableColumn
oacVoiceVoicePortPriProtocolState = _OacVoiceVoicePortPriProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 5),
    _OacVoiceVoicePortPriProtocolState_Type()
)
oacVoiceVoicePortPriProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriProtocolState.setStatus("current")
_OacVoiceVoicePortPriOperState_Type = VoiceAcDeacState
_OacVoiceVoicePortPriOperState_Object = MibTableColumn
oacVoiceVoicePortPriOperState = _OacVoiceVoicePortPriOperState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 6),
    _OacVoiceVoicePortPriOperState_Type()
)
oacVoiceVoicePortPriOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriOperState.setStatus("current")
_OacVoiceVoicePortPriAdminState_Type = VoiceAcDeacState
_OacVoiceVoicePortPriAdminState_Object = MibTableColumn
oacVoiceVoicePortPriAdminState = _OacVoiceVoicePortPriAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 7),
    _OacVoiceVoicePortPriAdminState_Type()
)
oacVoiceVoicePortPriAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriAdminState.setStatus("current")
_OacVoiceVoicePortPriConfigState_Type = VoiceUpDnState
_OacVoiceVoicePortPriConfigState_Object = MibTableColumn
oacVoiceVoicePortPriConfigState = _OacVoiceVoicePortPriConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 8),
    _OacVoiceVoicePortPriConfigState_Type()
)
oacVoiceVoicePortPriConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriConfigState.setStatus("current")
_OacVoiceVoicePortPriLayer1_Type = VoiceAcDeacState
_OacVoiceVoicePortPriLayer1_Object = MibTableColumn
oacVoiceVoicePortPriLayer1 = _OacVoiceVoicePortPriLayer1_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 9),
    _OacVoiceVoicePortPriLayer1_Type()
)
oacVoiceVoicePortPriLayer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriLayer1.setStatus("current")
_OacVoiceVoicePortPriAttachedDialPeer_Type = Integer32
_OacVoiceVoicePortPriAttachedDialPeer_Object = MibTableColumn
oacVoiceVoicePortPriAttachedDialPeer = _OacVoiceVoicePortPriAttachedDialPeer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 10),
    _OacVoiceVoicePortPriAttachedDialPeer_Type()
)
oacVoiceVoicePortPriAttachedDialPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriAttachedDialPeer.setStatus("current")
_OacVoiceVoicePortPriVoiceCommNb_Type = Unsigned32
_OacVoiceVoicePortPriVoiceCommNb_Object = MibTableColumn
oacVoiceVoicePortPriVoiceCommNb = _OacVoiceVoicePortPriVoiceCommNb_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 11),
    _OacVoiceVoicePortPriVoiceCommNb_Type()
)
oacVoiceVoicePortPriVoiceCommNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriVoiceCommNb.setStatus("current")
_OacVoiceVoicePortPriAisOccur_Type = Unsigned32
_OacVoiceVoicePortPriAisOccur_Object = MibTableColumn
oacVoiceVoicePortPriAisOccur = _OacVoiceVoicePortPriAisOccur_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 12),
    _OacVoiceVoicePortPriAisOccur_Type()
)
oacVoiceVoicePortPriAisOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriAisOccur.setStatus("current")
_OacVoiceVoicePortPriRdiOccur_Type = Unsigned32
_OacVoiceVoicePortPriRdiOccur_Object = MibTableColumn
oacVoiceVoicePortPriRdiOccur = _OacVoiceVoicePortPriRdiOccur_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 1, 3, 1, 13),
    _OacVoiceVoicePortPriRdiOccur_Type()
)
oacVoiceVoicePortPriRdiOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVoicePortPriRdiOccur.setStatus("current")
_OacVoiceDialPeerBles_ObjectIdentity = ObjectIdentity
oacVoiceDialPeerBles = _OacVoiceDialPeerBles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2)
)
_OacVoiceDialPeerVoiceVmoafxsTable_Object = MibTable
oacVoiceDialPeerVoiceVmoafxsTable = _OacVoiceDialPeerVoiceVmoafxsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsTable.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsEntry_Object = MibTableRow
oacVoiceDialPeerVoiceVmoafxsEntry = _OacVoiceDialPeerVoiceVmoafxsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1)
)
oacVoiceDialPeerVoiceVmoafxsEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsDialPeer"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsEntry.setStatus("current")


class _OacVoiceDialPeerVoiceVmoafxsDialPeer_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVmoafxsDialPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVoiceDialPeerVoiceVmoafxsDialPeer_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVmoafxsDialPeer_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsDialPeer = _OacVoiceDialPeerVoiceVmoafxsDialPeer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 1),
    _OacVoiceDialPeerVoiceVmoafxsDialPeer_Type()
)
oacVoiceDialPeerVoiceVmoafxsDialPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsDialPeer.setStatus("current")


class _OacVoiceDialPeerVoiceVmoafxsLinkedPort_Type(DisplayString):
    """Custom type oacVoiceDialPeerVoiceVmoafxsLinkedPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_OacVoiceDialPeerVoiceVmoafxsLinkedPort_Type.__name__ = "DisplayString"
_OacVoiceDialPeerVoiceVmoafxsLinkedPort_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsLinkedPort = _OacVoiceDialPeerVoiceVmoafxsLinkedPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 2),
    _OacVoiceDialPeerVoiceVmoafxsLinkedPort_Type()
)
oacVoiceDialPeerVoiceVmoafxsLinkedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsLinkedPort.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsCurrentState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVmoafxsCurrentState_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsCurrentState = _OacVoiceDialPeerVoiceVmoafxsCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 3),
    _OacVoiceDialPeerVoiceVmoafxsCurrentState_Type()
)
oacVoiceDialPeerVoiceVmoafxsCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsCurrentState.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsPortStatus_Type = VoiceFxsPortStatus
_OacVoiceDialPeerVoiceVmoafxsPortStatus_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsPortStatus = _OacVoiceDialPeerVoiceVmoafxsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 4),
    _OacVoiceDialPeerVoiceVmoafxsPortStatus_Type()
)
oacVoiceDialPeerVoiceVmoafxsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsPortStatus.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsPathStatus_Type = VoiceFxsPathStatus
_OacVoiceDialPeerVoiceVmoafxsPathStatus_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsPathStatus = _OacVoiceDialPeerVoiceVmoafxsPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 5),
    _OacVoiceDialPeerVoiceVmoafxsPathStatus_Type()
)
oacVoiceDialPeerVoiceVmoafxsPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsPathStatus.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsCurrentTxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVmoafxsCurrentTxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsCurrentTxCoder = _OacVoiceDialPeerVoiceVmoafxsCurrentTxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 6),
    _OacVoiceDialPeerVoiceVmoafxsCurrentTxCoder_Type()
)
oacVoiceDialPeerVoiceVmoafxsCurrentTxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsCurrentTxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsCurrentRxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVmoafxsCurrentRxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsCurrentRxCoder = _OacVoiceDialPeerVoiceVmoafxsCurrentRxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 7),
    _OacVoiceDialPeerVoiceVmoafxsCurrentRxCoder_Type()
)
oacVoiceDialPeerVoiceVmoafxsCurrentRxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsCurrentRxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVmofxsCurrentBc_Type = VoiceBearerCap
_OacVoiceDialPeerVoiceVmofxsCurrentBc_Object = MibTableColumn
oacVoiceDialPeerVoiceVmofxsCurrentBc = _OacVoiceDialPeerVoiceVmofxsCurrentBc_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 8),
    _OacVoiceDialPeerVoiceVmofxsCurrentBc_Type()
)
oacVoiceDialPeerVoiceVmofxsCurrentBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmofxsCurrentBc.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsCurrentCid_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoafxsCurrentCid_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsCurrentCid = _OacVoiceDialPeerVoiceVmoafxsCurrentCid_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 9),
    _OacVoiceDialPeerVoiceVmoafxsCurrentCid_Type()
)
oacVoiceDialPeerVoiceVmoafxsCurrentCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsCurrentCid.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsBlockingOccurence_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoafxsBlockingOccurence_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsBlockingOccurence = _OacVoiceDialPeerVoiceVmoafxsBlockingOccurence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 10),
    _OacVoiceDialPeerVoiceVmoafxsBlockingOccurence_Type()
)
oacVoiceDialPeerVoiceVmoafxsBlockingOccurence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsBlockingOccurence.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsTotalBlockingDuration_Type = TimeTicks
_OacVoiceDialPeerVoiceVmoafxsTotalBlockingDuration_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsTotalBlockingDuration = _OacVoiceDialPeerVoiceVmoafxsTotalBlockingDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 11),
    _OacVoiceDialPeerVoiceVmoafxsTotalBlockingDuration_Type()
)
oacVoiceDialPeerVoiceVmoafxsTotalBlockingDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsTotalBlockingDuration.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsVoicePacketSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoafxsVoicePacketSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsVoicePacketSent = _OacVoiceDialPeerVoiceVmoafxsVoicePacketSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 12),
    _OacVoiceDialPeerVoiceVmoafxsVoicePacketSent_Type()
)
oacVoiceDialPeerVoiceVmoafxsVoicePacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsVoicePacketSent.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsVoicePacketReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoafxsVoicePacketReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsVoicePacketReceived = _OacVoiceDialPeerVoiceVmoafxsVoicePacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 13),
    _OacVoiceDialPeerVoiceVmoafxsVoicePacketReceived_Type()
)
oacVoiceDialPeerVoiceVmoafxsVoicePacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsVoicePacketReceived.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsPathEstablished_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoafxsPathEstablished_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsPathEstablished = _OacVoiceDialPeerVoiceVmoafxsPathEstablished_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 14),
    _OacVoiceDialPeerVoiceVmoafxsPathEstablished_Type()
)
oacVoiceDialPeerVoiceVmoafxsPathEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsPathEstablished.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsPathRqFailed_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoafxsPathRqFailed_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsPathRqFailed = _OacVoiceDialPeerVoiceVmoafxsPathRqFailed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 15),
    _OacVoiceDialPeerVoiceVmoafxsPathRqFailed_Type()
)
oacVoiceDialPeerVoiceVmoafxsPathRqFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsPathRqFailed.setStatus("current")
_OacVoiceDialPeerVoiceVmoafxsPathDuration_Type = TimeTicks
_OacVoiceDialPeerVoiceVmoafxsPathDuration_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoafxsPathDuration = _OacVoiceDialPeerVoiceVmoafxsPathDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 1, 1, 16),
    _OacVoiceDialPeerVoiceVmoafxsPathDuration_Type()
)
oacVoiceDialPeerVoiceVmoafxsPathDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoafxsPathDuration.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriTable_Object = MibTable
oacVoiceDialPeerVoiceVmoabriTable = _OacVoiceDialPeerVoiceVmoabriTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriTable.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriEntry_Object = MibTableRow
oacVoiceDialPeerVoiceVmoabriEntry = _OacVoiceDialPeerVoiceVmoabriEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 2, 1)
)
oacVoiceDialPeerVoiceVmoabriEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriDialPeer"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriEntry.setStatus("current")


class _OacVoiceDialPeerVoiceVmoabriDialPeer_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVmoabriDialPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVoiceDialPeerVoiceVmoabriDialPeer_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVmoabriDialPeer_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriDialPeer = _OacVoiceDialPeerVoiceVmoabriDialPeer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 2, 1, 1),
    _OacVoiceDialPeerVoiceVmoabriDialPeer_Type()
)
oacVoiceDialPeerVoiceVmoabriDialPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriDialPeer.setStatus("current")


class _OacVoiceDialPeerVoiceVmoabriPort_Type(DisplayString):
    """Custom type oacVoiceDialPeerVoiceVmoabriPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_OacVoiceDialPeerVoiceVmoabriPort_Type.__name__ = "DisplayString"
_OacVoiceDialPeerVoiceVmoabriPort_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriPort = _OacVoiceDialPeerVoiceVmoabriPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 2, 1, 2),
    _OacVoiceDialPeerVoiceVmoabriPort_Type()
)
oacVoiceDialPeerVoiceVmoabriPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriPort.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriCurrentState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVmoabriCurrentState_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriCurrentState = _OacVoiceDialPeerVoiceVmoabriCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 2, 1, 3),
    _OacVoiceDialPeerVoiceVmoabriCurrentState_Type()
)
oacVoiceDialPeerVoiceVmoabriCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriCurrentState.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriConfigState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVmoabriConfigState_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriConfigState = _OacVoiceDialPeerVoiceVmoabriConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 2, 1, 4),
    _OacVoiceDialPeerVoiceVmoabriConfigState_Type()
)
oacVoiceDialPeerVoiceVmoabriConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriConfigState.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriPortStatus_Type = VoiceBriPortStatus
_OacVoiceDialPeerVoiceVmoabriPortStatus_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriPortStatus = _OacVoiceDialPeerVoiceVmoabriPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 2, 1, 5),
    _OacVoiceDialPeerVoiceVmoabriPortStatus_Type()
)
oacVoiceDialPeerVoiceVmoabriPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriPortStatus.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriBlockingOccurence_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriBlockingOccurence_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriBlockingOccurence = _OacVoiceDialPeerVoiceVmoabriBlockingOccurence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 2, 1, 6),
    _OacVoiceDialPeerVoiceVmoabriBlockingOccurence_Type()
)
oacVoiceDialPeerVoiceVmoabriBlockingOccurence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriBlockingOccurence.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriTotalBlockingDuration_Type = TimeTicks
_OacVoiceDialPeerVoiceVmoabriTotalBlockingDuration_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriTotalBlockingDuration = _OacVoiceDialPeerVoiceVmoabriTotalBlockingDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 2, 1, 7),
    _OacVoiceDialPeerVoiceVmoabriTotalBlockingDuration_Type()
)
oacVoiceDialPeerVoiceVmoabriTotalBlockingDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriTotalBlockingDuration.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriBxAllocNum_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriBxAllocNum_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriBxAllocNum = _OacVoiceDialPeerVoiceVmoabriBxAllocNum_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 2, 1, 8),
    _OacVoiceDialPeerVoiceVmoabriBxAllocNum_Type()
)
oacVoiceDialPeerVoiceVmoabriBxAllocNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriBxAllocNum.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1Table_Object = MibTable
oacVoiceDialPeerVoiceVmoabriB1Table = _OacVoiceDialPeerVoiceVmoabriB1Table_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1Table.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1Entry_Object = MibTableRow
oacVoiceDialPeerVoiceVmoabriB1Entry = _OacVoiceDialPeerVoiceVmoabriB1Entry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1)
)
oacVoiceDialPeerVoiceVmoabriB1Entry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriDialPeer"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1Entry.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1CurrentTxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVmoabriB1CurrentTxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1CurrentTxCoder = _OacVoiceDialPeerVoiceVmoabriB1CurrentTxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 1),
    _OacVoiceDialPeerVoiceVmoabriB1CurrentTxCoder_Type()
)
oacVoiceDialPeerVoiceVmoabriB1CurrentTxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1CurrentTxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1CurrentRxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVmoabriB1CurrentRxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1CurrentRxCoder = _OacVoiceDialPeerVoiceVmoabriB1CurrentRxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 2),
    _OacVoiceDialPeerVoiceVmoabriB1CurrentRxCoder_Type()
)
oacVoiceDialPeerVoiceVmoabriB1CurrentRxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1CurrentRxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1CurrentBc_Type = VoiceBearerCap
_OacVoiceDialPeerVoiceVmoabriB1CurrentBc_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1CurrentBc = _OacVoiceDialPeerVoiceVmoabriB1CurrentBc_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 3),
    _OacVoiceDialPeerVoiceVmoabriB1CurrentBc_Type()
)
oacVoiceDialPeerVoiceVmoabriB1CurrentBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1CurrentBc.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1CurrentCid_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB1CurrentCid_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1CurrentCid = _OacVoiceDialPeerVoiceVmoabriB1CurrentCid_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 4),
    _OacVoiceDialPeerVoiceVmoabriB1CurrentCid_Type()
)
oacVoiceDialPeerVoiceVmoabriB1CurrentCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1CurrentCid.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1VoicePacketSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB1VoicePacketSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1VoicePacketSent = _OacVoiceDialPeerVoiceVmoabriB1VoicePacketSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 5),
    _OacVoiceDialPeerVoiceVmoabriB1VoicePacketSent_Type()
)
oacVoiceDialPeerVoiceVmoabriB1VoicePacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1VoicePacketSent.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1VoicePacketReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB1VoicePacketReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1VoicePacketReceived = _OacVoiceDialPeerVoiceVmoabriB1VoicePacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 6),
    _OacVoiceDialPeerVoiceVmoabriB1VoicePacketReceived_Type()
)
oacVoiceDialPeerVoiceVmoabriB1VoicePacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1VoicePacketReceived.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1BytesSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB1BytesSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1BytesSent = _OacVoiceDialPeerVoiceVmoabriB1BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 7),
    _OacVoiceDialPeerVoiceVmoabriB1BytesSent_Type()
)
oacVoiceDialPeerVoiceVmoabriB1BytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1BytesSent.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1BytesReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB1BytesReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1BytesReceived = _OacVoiceDialPeerVoiceVmoabriB1BytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 8),
    _OacVoiceDialPeerVoiceVmoabriB1BytesReceived_Type()
)
oacVoiceDialPeerVoiceVmoabriB1BytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1BytesReceived.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1PathEstablished_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB1PathEstablished_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1PathEstablished = _OacVoiceDialPeerVoiceVmoabriB1PathEstablished_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 9),
    _OacVoiceDialPeerVoiceVmoabriB1PathEstablished_Type()
)
oacVoiceDialPeerVoiceVmoabriB1PathEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1PathEstablished.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB1PathDuration_Type = TimeTicks
_OacVoiceDialPeerVoiceVmoabriB1PathDuration_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1PathDuration = _OacVoiceDialPeerVoiceVmoabriB1PathDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 10),
    _OacVoiceDialPeerVoiceVmoabriB1PathDuration_Type()
)
oacVoiceDialPeerVoiceVmoabriB1PathDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1PathDuration.setStatus("current")


class _OacVoiceDialPeerVoiceVmoabriB1Bundle_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVmoabriB1Bundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OacVoiceDialPeerVoiceVmoabriB1Bundle_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVmoabriB1Bundle_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB1Bundle = _OacVoiceDialPeerVoiceVmoabriB1Bundle_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 3, 1, 11),
    _OacVoiceDialPeerVoiceVmoabriB1Bundle_Type()
)
oacVoiceDialPeerVoiceVmoabriB1Bundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB1Bundle.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2Table_Object = MibTable
oacVoiceDialPeerVoiceVmoabriB2Table = _OacVoiceDialPeerVoiceVmoabriB2Table_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2Table.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2Entry_Object = MibTableRow
oacVoiceDialPeerVoiceVmoabriB2Entry = _OacVoiceDialPeerVoiceVmoabriB2Entry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1)
)
oacVoiceDialPeerVoiceVmoabriB2Entry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriDialPeer"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2Entry.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2CurrentTxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVmoabriB2CurrentTxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2CurrentTxCoder = _OacVoiceDialPeerVoiceVmoabriB2CurrentTxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 1),
    _OacVoiceDialPeerVoiceVmoabriB2CurrentTxCoder_Type()
)
oacVoiceDialPeerVoiceVmoabriB2CurrentTxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2CurrentTxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2CurrentRxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVmoabriB2CurrentRxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2CurrentRxCoder = _OacVoiceDialPeerVoiceVmoabriB2CurrentRxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 2),
    _OacVoiceDialPeerVoiceVmoabriB2CurrentRxCoder_Type()
)
oacVoiceDialPeerVoiceVmoabriB2CurrentRxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2CurrentRxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2CurrentBc_Type = VoiceBearerCap
_OacVoiceDialPeerVoiceVmoabriB2CurrentBc_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2CurrentBc = _OacVoiceDialPeerVoiceVmoabriB2CurrentBc_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 3),
    _OacVoiceDialPeerVoiceVmoabriB2CurrentBc_Type()
)
oacVoiceDialPeerVoiceVmoabriB2CurrentBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2CurrentBc.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2CurrentCid_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB2CurrentCid_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2CurrentCid = _OacVoiceDialPeerVoiceVmoabriB2CurrentCid_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 4),
    _OacVoiceDialPeerVoiceVmoabriB2CurrentCid_Type()
)
oacVoiceDialPeerVoiceVmoabriB2CurrentCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2CurrentCid.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2VoicePacketSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB2VoicePacketSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2VoicePacketSent = _OacVoiceDialPeerVoiceVmoabriB2VoicePacketSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 5),
    _OacVoiceDialPeerVoiceVmoabriB2VoicePacketSent_Type()
)
oacVoiceDialPeerVoiceVmoabriB2VoicePacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2VoicePacketSent.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2VoicePacketReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB2VoicePacketReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2VoicePacketReceived = _OacVoiceDialPeerVoiceVmoabriB2VoicePacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 6),
    _OacVoiceDialPeerVoiceVmoabriB2VoicePacketReceived_Type()
)
oacVoiceDialPeerVoiceVmoabriB2VoicePacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2VoicePacketReceived.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2BytesSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB2BytesSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2BytesSent = _OacVoiceDialPeerVoiceVmoabriB2BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 7),
    _OacVoiceDialPeerVoiceVmoabriB2BytesSent_Type()
)
oacVoiceDialPeerVoiceVmoabriB2BytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2BytesSent.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2BytesReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB2BytesReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2BytesReceived = _OacVoiceDialPeerVoiceVmoabriB2BytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 8),
    _OacVoiceDialPeerVoiceVmoabriB2BytesReceived_Type()
)
oacVoiceDialPeerVoiceVmoabriB2BytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2BytesReceived.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2PathEstablished_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriB2PathEstablished_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2PathEstablished = _OacVoiceDialPeerVoiceVmoabriB2PathEstablished_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 9),
    _OacVoiceDialPeerVoiceVmoabriB2PathEstablished_Type()
)
oacVoiceDialPeerVoiceVmoabriB2PathEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2PathEstablished.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriB2PathDuration_Type = TimeTicks
_OacVoiceDialPeerVoiceVmoabriB2PathDuration_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2PathDuration = _OacVoiceDialPeerVoiceVmoabriB2PathDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 10),
    _OacVoiceDialPeerVoiceVmoabriB2PathDuration_Type()
)
oacVoiceDialPeerVoiceVmoabriB2PathDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2PathDuration.setStatus("current")


class _OacVoiceDialPeerVoiceVmoabriB2Bundle_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVmoabriB2Bundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OacVoiceDialPeerVoiceVmoabriB2Bundle_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVmoabriB2Bundle_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriB2Bundle = _OacVoiceDialPeerVoiceVmoabriB2Bundle_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 4, 1, 11),
    _OacVoiceDialPeerVoiceVmoabriB2Bundle_Type()
)
oacVoiceDialPeerVoiceVmoabriB2Bundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriB2Bundle.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriDTable_Object = MibTable
oacVoiceDialPeerVoiceVmoabriDTable = _OacVoiceDialPeerVoiceVmoabriDTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriDTable.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriDEntry_Object = MibTableRow
oacVoiceDialPeerVoiceVmoabriDEntry = _OacVoiceDialPeerVoiceVmoabriDEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 5, 1)
)
oacVoiceDialPeerVoiceVmoabriDEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriDialPeer"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriDEntry.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriDCurrentCid_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriDCurrentCid_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriDCurrentCid = _OacVoiceDialPeerVoiceVmoabriDCurrentCid_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 5, 1, 1),
    _OacVoiceDialPeerVoiceVmoabriDCurrentCid_Type()
)
oacVoiceDialPeerVoiceVmoabriDCurrentCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriDCurrentCid.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriDFramesSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriDFramesSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriDFramesSent = _OacVoiceDialPeerVoiceVmoabriDFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 5, 1, 2),
    _OacVoiceDialPeerVoiceVmoabriDFramesSent_Type()
)
oacVoiceDialPeerVoiceVmoabriDFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriDFramesSent.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriDFramesReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriDFramesReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriDFramesReceived = _OacVoiceDialPeerVoiceVmoabriDFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 5, 1, 3),
    _OacVoiceDialPeerVoiceVmoabriDFramesReceived_Type()
)
oacVoiceDialPeerVoiceVmoabriDFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriDFramesReceived.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriDBytesSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriDBytesSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriDBytesSent = _OacVoiceDialPeerVoiceVmoabriDBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 5, 1, 4),
    _OacVoiceDialPeerVoiceVmoabriDBytesSent_Type()
)
oacVoiceDialPeerVoiceVmoabriDBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriDBytesSent.setStatus("current")
_OacVoiceDialPeerVoiceVmoabriDBytesReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoabriDBytesReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoabriDBytesReceived = _OacVoiceDialPeerVoiceVmoabriDBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 5, 1, 5),
    _OacVoiceDialPeerVoiceVmoabriDBytesReceived_Type()
)
oacVoiceDialPeerVoiceVmoabriDBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoabriDBytesReceived.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTable_Object = MibTable
oacVoiceDialPeerVoiceVmoapriTable = _OacVoiceDialPeerVoiceVmoapriTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTable.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriEntry_Object = MibTableRow
oacVoiceDialPeerVoiceVmoapriEntry = _OacVoiceDialPeerVoiceVmoapriEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 6, 1)
)
oacVoiceDialPeerVoiceVmoapriEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriDialPeer"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriEntry.setStatus("current")


class _OacVoiceDialPeerVoiceVmoapriDialPeer_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVmoapriDialPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVoiceDialPeerVoiceVmoapriDialPeer_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVmoapriDialPeer_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriDialPeer = _OacVoiceDialPeerVoiceVmoapriDialPeer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 6, 1, 1),
    _OacVoiceDialPeerVoiceVmoapriDialPeer_Type()
)
oacVoiceDialPeerVoiceVmoapriDialPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriDialPeer.setStatus("current")


class _OacVoiceDialPeerVoiceVmoapriLinkedPort_Type(DisplayString):
    """Custom type oacVoiceDialPeerVoiceVmoapriLinkedPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OacVoiceDialPeerVoiceVmoapriLinkedPort_Type.__name__ = "DisplayString"
_OacVoiceDialPeerVoiceVmoapriLinkedPort_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriLinkedPort = _OacVoiceDialPeerVoiceVmoapriLinkedPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 6, 1, 2),
    _OacVoiceDialPeerVoiceVmoapriLinkedPort_Type()
)
oacVoiceDialPeerVoiceVmoapriLinkedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriLinkedPort.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriPortStatus_Type = VoiceBriPortStatus
_OacVoiceDialPeerVoiceVmoapriPortStatus_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriPortStatus = _OacVoiceDialPeerVoiceVmoapriPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 6, 1, 3),
    _OacVoiceDialPeerVoiceVmoapriPortStatus_Type()
)
oacVoiceDialPeerVoiceVmoapriPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriPortStatus.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriCurrentState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVmoapriCurrentState_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriCurrentState = _OacVoiceDialPeerVoiceVmoapriCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 6, 1, 4),
    _OacVoiceDialPeerVoiceVmoapriCurrentState_Type()
)
oacVoiceDialPeerVoiceVmoapriCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriCurrentState.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriConfigState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVmoapriConfigState_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriConfigState = _OacVoiceDialPeerVoiceVmoapriConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 6, 1, 5),
    _OacVoiceDialPeerVoiceVmoapriConfigState_Type()
)
oacVoiceDialPeerVoiceVmoapriConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriConfigState.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriBlockingOccurence_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoapriBlockingOccurence_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriBlockingOccurence = _OacVoiceDialPeerVoiceVmoapriBlockingOccurence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 6, 1, 6),
    _OacVoiceDialPeerVoiceVmoapriBlockingOccurence_Type()
)
oacVoiceDialPeerVoiceVmoapriBlockingOccurence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriBlockingOccurence.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTotalBlockingDuration_Type = TimeTicks
_OacVoiceDialPeerVoiceVmoapriTotalBlockingDuration_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriTotalBlockingDuration = _OacVoiceDialPeerVoiceVmoapriTotalBlockingDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 6, 1, 7),
    _OacVoiceDialPeerVoiceVmoapriTotalBlockingDuration_Type()
)
oacVoiceDialPeerVoiceVmoapriTotalBlockingDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTotalBlockingDuration.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriBxAllocNum_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoapriBxAllocNum_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriBxAllocNum = _OacVoiceDialPeerVoiceVmoapriBxAllocNum_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 6, 1, 8),
    _OacVoiceDialPeerVoiceVmoapriBxAllocNum_Type()
)
oacVoiceDialPeerVoiceVmoapriBxAllocNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriBxAllocNum.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTsxTable_Object = MibTable
oacVoiceDialPeerVoiceVmoapriTsxTable = _OacVoiceDialPeerVoiceVmoapriTsxTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTsxTable.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTsxEntry_Object = MibTableRow
oacVoiceDialPeerVoiceVmoapriTsxEntry = _OacVoiceDialPeerVoiceVmoapriTsxEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 7, 1)
)
oacVoiceDialPeerVoiceVmoapriTsxEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriDialPeer"),
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriTsxIndex"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTsxEntry.setStatus("current")


class _OacVoiceDialPeerVoiceVmoapriTsxIndex_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVmoapriTsxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_OacVoiceDialPeerVoiceVmoapriTsxIndex_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVmoapriTsxIndex_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriTsxIndex = _OacVoiceDialPeerVoiceVmoapriTsxIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 7, 1, 1),
    _OacVoiceDialPeerVoiceVmoapriTsxIndex_Type()
)
oacVoiceDialPeerVoiceVmoapriTsxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTsxIndex.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTsxChannelType_Type = VoiceChnType
_OacVoiceDialPeerVoiceVmoapriTsxChannelType_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriTsxChannelType = _OacVoiceDialPeerVoiceVmoapriTsxChannelType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 7, 1, 2),
    _OacVoiceDialPeerVoiceVmoapriTsxChannelType_Type()
)
oacVoiceDialPeerVoiceVmoapriTsxChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTsxChannelType.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTsxCurrentTxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVmoapriTsxCurrentTxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriTsxCurrentTxCoder = _OacVoiceDialPeerVoiceVmoapriTsxCurrentTxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 7, 1, 3),
    _OacVoiceDialPeerVoiceVmoapriTsxCurrentTxCoder_Type()
)
oacVoiceDialPeerVoiceVmoapriTsxCurrentTxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTsxCurrentTxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTsxCurrentRxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVmoapriTsxCurrentRxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriTsxCurrentRxCoder = _OacVoiceDialPeerVoiceVmoapriTsxCurrentRxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 7, 1, 4),
    _OacVoiceDialPeerVoiceVmoapriTsxCurrentRxCoder_Type()
)
oacVoiceDialPeerVoiceVmoapriTsxCurrentRxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTsxCurrentRxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTsxCurrentBC_Type = VoiceBearerCap
_OacVoiceDialPeerVoiceVmoapriTsxCurrentBC_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriTsxCurrentBC = _OacVoiceDialPeerVoiceVmoapriTsxCurrentBC_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 7, 1, 5),
    _OacVoiceDialPeerVoiceVmoapriTsxCurrentBC_Type()
)
oacVoiceDialPeerVoiceVmoapriTsxCurrentBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTsxCurrentBC.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTsxCurrentCID_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoapriTsxCurrentCID_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriTsxCurrentCID = _OacVoiceDialPeerVoiceVmoapriTsxCurrentCID_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 7, 1, 6),
    _OacVoiceDialPeerVoiceVmoapriTsxCurrentCID_Type()
)
oacVoiceDialPeerVoiceVmoapriTsxCurrentCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTsxCurrentCID.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTsxVoicePacketSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoapriTsxVoicePacketSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriTsxVoicePacketSent = _OacVoiceDialPeerVoiceVmoapriTsxVoicePacketSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 7, 1, 7),
    _OacVoiceDialPeerVoiceVmoapriTsxVoicePacketSent_Type()
)
oacVoiceDialPeerVoiceVmoapriTsxVoicePacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTsxVoicePacketSent.setStatus("current")
_OacVoiceDialPeerVoiceVmoapriTsxVoicePacketReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVmoapriTsxVoicePacketReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVmoapriTsxVoicePacketReceived = _OacVoiceDialPeerVoiceVmoapriTsxVoicePacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 7, 1, 8),
    _OacVoiceDialPeerVoiceVmoapriTsxVoicePacketReceived_Type()
)
oacVoiceDialPeerVoiceVmoapriTsxVoicePacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVmoapriTsxVoicePacketReceived.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTable_Object = MibTable
oacVoiceDialPeerVoiceVtoaccsTable = _OacVoiceDialPeerVoiceVtoaccsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTable.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsEntry_Object = MibTableRow
oacVoiceDialPeerVoiceVtoaccsEntry = _OacVoiceDialPeerVoiceVtoaccsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 8, 1)
)
oacVoiceDialPeerVoiceVtoaccsEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsDialPeer"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsEntry.setStatus("current")


class _OacVoiceDialPeerVoiceVtoaccsDialPeer_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVtoaccsDialPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVoiceDialPeerVoiceVtoaccsDialPeer_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVtoaccsDialPeer_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsDialPeer = _OacVoiceDialPeerVoiceVtoaccsDialPeer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 8, 1, 1),
    _OacVoiceDialPeerVoiceVtoaccsDialPeer_Type()
)
oacVoiceDialPeerVoiceVtoaccsDialPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsDialPeer.setStatus("current")


class _OacVoiceDialPeerVoiceVtoaccsLinkedPort_Type(DisplayString):
    """Custom type oacVoiceDialPeerVoiceVtoaccsLinkedPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OacVoiceDialPeerVoiceVtoaccsLinkedPort_Type.__name__ = "DisplayString"
_OacVoiceDialPeerVoiceVtoaccsLinkedPort_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsLinkedPort = _OacVoiceDialPeerVoiceVtoaccsLinkedPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 8, 1, 2),
    _OacVoiceDialPeerVoiceVtoaccsLinkedPort_Type()
)
oacVoiceDialPeerVoiceVtoaccsLinkedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsLinkedPort.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsPortStatus_Type = VoiceBriPortStatus
_OacVoiceDialPeerVoiceVtoaccsPortStatus_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsPortStatus = _OacVoiceDialPeerVoiceVtoaccsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 8, 1, 3),
    _OacVoiceDialPeerVoiceVtoaccsPortStatus_Type()
)
oacVoiceDialPeerVoiceVtoaccsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsPortStatus.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsCurrentState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVtoaccsCurrentState_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsCurrentState = _OacVoiceDialPeerVoiceVtoaccsCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 8, 1, 4),
    _OacVoiceDialPeerVoiceVtoaccsCurrentState_Type()
)
oacVoiceDialPeerVoiceVtoaccsCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsCurrentState.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsConfigState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVtoaccsConfigState_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsConfigState = _OacVoiceDialPeerVoiceVtoaccsConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 8, 1, 5),
    _OacVoiceDialPeerVoiceVtoaccsConfigState_Type()
)
oacVoiceDialPeerVoiceVtoaccsConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsConfigState.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsBlockingOccurence_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoaccsBlockingOccurence_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsBlockingOccurence = _OacVoiceDialPeerVoiceVtoaccsBlockingOccurence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 8, 1, 6),
    _OacVoiceDialPeerVoiceVtoaccsBlockingOccurence_Type()
)
oacVoiceDialPeerVoiceVtoaccsBlockingOccurence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsBlockingOccurence.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTotalBlockingDuration_Type = TimeTicks
_OacVoiceDialPeerVoiceVtoaccsTotalBlockingDuration_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsTotalBlockingDuration = _OacVoiceDialPeerVoiceVtoaccsTotalBlockingDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 8, 1, 7),
    _OacVoiceDialPeerVoiceVtoaccsTotalBlockingDuration_Type()
)
oacVoiceDialPeerVoiceVtoaccsTotalBlockingDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTotalBlockingDuration.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsBxAllocNum_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoaccsBxAllocNum_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsBxAllocNum = _OacVoiceDialPeerVoiceVtoaccsBxAllocNum_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 8, 1, 8),
    _OacVoiceDialPeerVoiceVtoaccsBxAllocNum_Type()
)
oacVoiceDialPeerVoiceVtoaccsBxAllocNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsBxAllocNum.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTsxTable_Object = MibTable
oacVoiceDialPeerVoiceVtoaccsTsxTable = _OacVoiceDialPeerVoiceVtoaccsTsxTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxTable.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTsxEntry_Object = MibTableRow
oacVoiceDialPeerVoiceVtoaccsTsxEntry = _OacVoiceDialPeerVoiceVtoaccsTsxEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9, 1)
)
oacVoiceDialPeerVoiceVtoaccsTsxEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsDialPeer"),
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTsxIndex"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxEntry.setStatus("current")


class _OacVoiceDialPeerVoiceVtoaccsTsxIndex_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVtoaccsTsxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_OacVoiceDialPeerVoiceVtoaccsTsxIndex_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVtoaccsTsxIndex_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsTsxIndex = _OacVoiceDialPeerVoiceVtoaccsTsxIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9, 1, 1),
    _OacVoiceDialPeerVoiceVtoaccsTsxIndex_Type()
)
oacVoiceDialPeerVoiceVtoaccsTsxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxIndex.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTsxChannelType_Type = VoiceChnType
_OacVoiceDialPeerVoiceVtoaccsTsxChannelType_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsTsxChannelType = _OacVoiceDialPeerVoiceVtoaccsTsxChannelType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9, 1, 2),
    _OacVoiceDialPeerVoiceVtoaccsTsxChannelType_Type()
)
oacVoiceDialPeerVoiceVtoaccsTsxChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxChannelType.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTsxCurrentTxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVtoaccsTsxCurrentTxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsTsxCurrentTxCoder = _OacVoiceDialPeerVoiceVtoaccsTsxCurrentTxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9, 1, 3),
    _OacVoiceDialPeerVoiceVtoaccsTsxCurrentTxCoder_Type()
)
oacVoiceDialPeerVoiceVtoaccsTsxCurrentTxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxCurrentTxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTsxCurrentRxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVtoaccsTsxCurrentRxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsTsxCurrentRxCoder = _OacVoiceDialPeerVoiceVtoaccsTsxCurrentRxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9, 1, 4),
    _OacVoiceDialPeerVoiceVtoaccsTsxCurrentRxCoder_Type()
)
oacVoiceDialPeerVoiceVtoaccsTsxCurrentRxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxCurrentRxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTsxCurrentBC_Type = VoiceBearerCap
_OacVoiceDialPeerVoiceVtoaccsTsxCurrentBC_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsTsxCurrentBC = _OacVoiceDialPeerVoiceVtoaccsTsxCurrentBC_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9, 1, 5),
    _OacVoiceDialPeerVoiceVtoaccsTsxCurrentBC_Type()
)
oacVoiceDialPeerVoiceVtoaccsTsxCurrentBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxCurrentBC.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTsxCurrentCID_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoaccsTsxCurrentCID_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsTsxCurrentCID = _OacVoiceDialPeerVoiceVtoaccsTsxCurrentCID_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9, 1, 6),
    _OacVoiceDialPeerVoiceVtoaccsTsxCurrentCID_Type()
)
oacVoiceDialPeerVoiceVtoaccsTsxCurrentCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxCurrentCID.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTsxVoicePacketSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoaccsTsxVoicePacketSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketSent = _OacVoiceDialPeerVoiceVtoaccsTsxVoicePacketSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9, 1, 7),
    _OacVoiceDialPeerVoiceVtoaccsTsxVoicePacketSent_Type()
)
oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketSent.setStatus("current")
_OacVoiceDialPeerVoiceVtoaccsTsxVoicePacketReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoaccsTsxVoicePacketReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketReceived = _OacVoiceDialPeerVoiceVtoaccsTsxVoicePacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9, 1, 8),
    _OacVoiceDialPeerVoiceVtoaccsTsxVoicePacketReceived_Type()
)
oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketReceived.setStatus("current")


class _OacVoiceDialPeerVoiceVtoaccsTsxBundle_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVtoaccsTsxBundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_OacVoiceDialPeerVoiceVtoaccsTsxBundle_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVtoaccsTsxBundle_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoaccsTsxBundle = _OacVoiceDialPeerVoiceVtoaccsTsxBundle_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 9, 1, 9),
    _OacVoiceDialPeerVoiceVtoaccsTsxBundle_Type()
)
oacVoiceDialPeerVoiceVtoaccsTsxBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoaccsTsxBundle.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTable_Object = MibTable
oacVoiceDialPeerVoiceVtoacasTable = _OacVoiceDialPeerVoiceVtoacasTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 10)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTable.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasEntry_Object = MibTableRow
oacVoiceDialPeerVoiceVtoacasEntry = _OacVoiceDialPeerVoiceVtoacasEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 10, 1)
)
oacVoiceDialPeerVoiceVtoacasEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasDialPeer"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasEntry.setStatus("current")


class _OacVoiceDialPeerVoiceVtoacasDialPeer_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVtoacasDialPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVoiceDialPeerVoiceVtoacasDialPeer_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVtoacasDialPeer_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasDialPeer = _OacVoiceDialPeerVoiceVtoacasDialPeer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 10, 1, 1),
    _OacVoiceDialPeerVoiceVtoacasDialPeer_Type()
)
oacVoiceDialPeerVoiceVtoacasDialPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasDialPeer.setStatus("current")


class _OacVoiceDialPeerVoiceVtoacasLinkedPort_Type(DisplayString):
    """Custom type oacVoiceDialPeerVoiceVtoacasLinkedPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OacVoiceDialPeerVoiceVtoacasLinkedPort_Type.__name__ = "DisplayString"
_OacVoiceDialPeerVoiceVtoacasLinkedPort_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasLinkedPort = _OacVoiceDialPeerVoiceVtoacasLinkedPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 10, 1, 2),
    _OacVoiceDialPeerVoiceVtoacasLinkedPort_Type()
)
oacVoiceDialPeerVoiceVtoacasLinkedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasLinkedPort.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasPortStatus_Type = VoiceBriPortStatus
_OacVoiceDialPeerVoiceVtoacasPortStatus_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasPortStatus = _OacVoiceDialPeerVoiceVtoacasPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 10, 1, 3),
    _OacVoiceDialPeerVoiceVtoacasPortStatus_Type()
)
oacVoiceDialPeerVoiceVtoacasPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasPortStatus.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasCurrentState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVtoacasCurrentState_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasCurrentState = _OacVoiceDialPeerVoiceVtoacasCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 10, 1, 4),
    _OacVoiceDialPeerVoiceVtoacasCurrentState_Type()
)
oacVoiceDialPeerVoiceVtoacasCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasCurrentState.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasConfigState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVtoacasConfigState_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasConfigState = _OacVoiceDialPeerVoiceVtoacasConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 10, 1, 5),
    _OacVoiceDialPeerVoiceVtoacasConfigState_Type()
)
oacVoiceDialPeerVoiceVtoacasConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasConfigState.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasBlockingOccurence_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacasBlockingOccurence_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasBlockingOccurence = _OacVoiceDialPeerVoiceVtoacasBlockingOccurence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 10, 1, 6),
    _OacVoiceDialPeerVoiceVtoacasBlockingOccurence_Type()
)
oacVoiceDialPeerVoiceVtoacasBlockingOccurence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasBlockingOccurence.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTotalBlockingDuration_Type = TimeTicks
_OacVoiceDialPeerVoiceVtoacasTotalBlockingDuration_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTotalBlockingDuration = _OacVoiceDialPeerVoiceVtoacasTotalBlockingDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 10, 1, 7),
    _OacVoiceDialPeerVoiceVtoacasTotalBlockingDuration_Type()
)
oacVoiceDialPeerVoiceVtoacasTotalBlockingDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTotalBlockingDuration.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasBxAllocNum_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacasBxAllocNum_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasBxAllocNum = _OacVoiceDialPeerVoiceVtoacasBxAllocNum_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 10, 1, 8),
    _OacVoiceDialPeerVoiceVtoacasBxAllocNum_Type()
)
oacVoiceDialPeerVoiceVtoacasBxAllocNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasBxAllocNum.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxTable_Object = MibTable
oacVoiceDialPeerVoiceVtoacasTsxTable = _OacVoiceDialPeerVoiceVtoacasTsxTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxTable.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxEntry_Object = MibTableRow
oacVoiceDialPeerVoiceVtoacasTsxEntry = _OacVoiceDialPeerVoiceVtoacasTsxEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1)
)
oacVoiceDialPeerVoiceVtoacasTsxEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasDialPeer"),
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxIndex"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxEntry.setStatus("current")


class _OacVoiceDialPeerVoiceVtoacasTsxIndex_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVtoacasTsxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_OacVoiceDialPeerVoiceVtoacasTsxIndex_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVtoacasTsxIndex_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxIndex = _OacVoiceDialPeerVoiceVtoacasTsxIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 1),
    _OacVoiceDialPeerVoiceVtoacasTsxIndex_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxIndex.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxChannelType_Type = VoiceChnType
_OacVoiceDialPeerVoiceVtoacasTsxChannelType_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxChannelType = _OacVoiceDialPeerVoiceVtoacasTsxChannelType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 2),
    _OacVoiceDialPeerVoiceVtoacasTsxChannelType_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxChannelType.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxCurrentTxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVtoacasTsxCurrentTxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxCurrentTxCoder = _OacVoiceDialPeerVoiceVtoacasTsxCurrentTxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 3),
    _OacVoiceDialPeerVoiceVtoacasTsxCurrentTxCoder_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxCurrentTxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxCurrentTxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxCurrentRxCoder_Type = VoiceIOCoder
_OacVoiceDialPeerVoiceVtoacasTsxCurrentRxCoder_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxCurrentRxCoder = _OacVoiceDialPeerVoiceVtoacasTsxCurrentRxCoder_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 4),
    _OacVoiceDialPeerVoiceVtoacasTsxCurrentRxCoder_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxCurrentRxCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxCurrentRxCoder.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxCurrentBC_Type = VoiceBearerCap
_OacVoiceDialPeerVoiceVtoacasTsxCurrentBC_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxCurrentBC = _OacVoiceDialPeerVoiceVtoacasTsxCurrentBC_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 5),
    _OacVoiceDialPeerVoiceVtoacasTsxCurrentBC_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxCurrentBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxCurrentBC.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxCurrentCID_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacasTsxCurrentCID_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxCurrentCID = _OacVoiceDialPeerVoiceVtoacasTsxCurrentCID_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 6),
    _OacVoiceDialPeerVoiceVtoacasTsxCurrentCID_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxCurrentCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxCurrentCID.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxVoicePacketSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacasTsxVoicePacketSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxVoicePacketSent = _OacVoiceDialPeerVoiceVtoacasTsxVoicePacketSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 7),
    _OacVoiceDialPeerVoiceVtoacasTsxVoicePacketSent_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxVoicePacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxVoicePacketSent.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxVoicePacketReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacasTsxVoicePacketReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxVoicePacketReceived = _OacVoiceDialPeerVoiceVtoacasTsxVoicePacketReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 8),
    _OacVoiceDialPeerVoiceVtoacasTsxVoicePacketReceived_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxVoicePacketReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxVoicePacketReceived.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesSent_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesSent_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesSent = _OacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 9),
    _OacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesSent_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesSent.setStatus("current")
_OacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesReceived_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesReceived_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesReceived = _OacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 10),
    _OacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesReceived_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesReceived.setStatus("current")


class _OacVoiceDialPeerVoiceVtoacasTsxBundle_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVtoacasTsxBundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bundle1", 1),
          ("bundle2", 2),
          ("none", 0))
    )


_OacVoiceDialPeerVoiceVtoacasTsxBundle_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVtoacasTsxBundle_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacasTsxBundle = _OacVoiceDialPeerVoiceVtoacasTsxBundle_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 11, 1, 11),
    _OacVoiceDialPeerVoiceVtoacasTsxBundle_Type()
)
oacVoiceDialPeerVoiceVtoacasTsxBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacasTsxBundle.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesTable_Object = MibTable
oacVoiceDialPeerVoiceVtoacesTable = _OacVoiceDialPeerVoiceVtoacesTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesTable.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesEntry_Object = MibTableRow
oacVoiceDialPeerVoiceVtoacesEntry = _OacVoiceDialPeerVoiceVtoacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1)
)
oacVoiceDialPeerVoiceVtoacesEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesDialPeer"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesEntry.setStatus("current")


class _OacVoiceDialPeerVoiceVtoacesDialPeer_Type(Integer32):
    """Custom type oacVoiceDialPeerVoiceVtoacesDialPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVoiceDialPeerVoiceVtoacesDialPeer_Type.__name__ = "Integer32"
_OacVoiceDialPeerVoiceVtoacesDialPeer_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesDialPeer = _OacVoiceDialPeerVoiceVtoacesDialPeer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 1),
    _OacVoiceDialPeerVoiceVtoacesDialPeer_Type()
)
oacVoiceDialPeerVoiceVtoacesDialPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesDialPeer.setStatus("current")


class _OacVoiceDialPeerVoiceVtoacesLinkedPort_Type(DisplayString):
    """Custom type oacVoiceDialPeerVoiceVtoacesLinkedPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OacVoiceDialPeerVoiceVtoacesLinkedPort_Type.__name__ = "DisplayString"
_OacVoiceDialPeerVoiceVtoacesLinkedPort_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesLinkedPort = _OacVoiceDialPeerVoiceVtoacesLinkedPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 2),
    _OacVoiceDialPeerVoiceVtoacesLinkedPort_Type()
)
oacVoiceDialPeerVoiceVtoacesLinkedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesLinkedPort.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesCurrentState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVtoacesCurrentState_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesCurrentState = _OacVoiceDialPeerVoiceVtoacesCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 3),
    _OacVoiceDialPeerVoiceVtoacesCurrentState_Type()
)
oacVoiceDialPeerVoiceVtoacesCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesCurrentState.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesConfigState_Type = VoiceUpDnState
_OacVoiceDialPeerVoiceVtoacesConfigState_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesConfigState = _OacVoiceDialPeerVoiceVtoacesConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 4),
    _OacVoiceDialPeerVoiceVtoacesConfigState_Type()
)
oacVoiceDialPeerVoiceVtoacesConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesConfigState.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesCellLossIntegrationPeriod_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacesCellLossIntegrationPeriod_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesCellLossIntegrationPeriod = _OacVoiceDialPeerVoiceVtoacesCellLossIntegrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 5),
    _OacVoiceDialPeerVoiceVtoacesCellLossIntegrationPeriod_Type()
)
oacVoiceDialPeerVoiceVtoacesCellLossIntegrationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesCellLossIntegrationPeriod.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesOutOfSyncOccurences_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacesOutOfSyncOccurences_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesOutOfSyncOccurences = _OacVoiceDialPeerVoiceVtoacesOutOfSyncOccurences_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 6),
    _OacVoiceDialPeerVoiceVtoacesOutOfSyncOccurences_Type()
)
oacVoiceDialPeerVoiceVtoacesOutOfSyncOccurences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesOutOfSyncOccurences.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesTxCells_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacesTxCells_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesTxCells = _OacVoiceDialPeerVoiceVtoacesTxCells_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 7),
    _OacVoiceDialPeerVoiceVtoacesTxCells_Type()
)
oacVoiceDialPeerVoiceVtoacesTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesTxCells.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesReassCells_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacesReassCells_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesReassCells = _OacVoiceDialPeerVoiceVtoacesReassCells_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 8),
    _OacVoiceDialPeerVoiceVtoacesReassCells_Type()
)
oacVoiceDialPeerVoiceVtoacesReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesReassCells.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesBufOverflows_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacesBufOverflows_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesBufOverflows = _OacVoiceDialPeerVoiceVtoacesBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 9),
    _OacVoiceDialPeerVoiceVtoacesBufOverflows_Type()
)
oacVoiceDialPeerVoiceVtoacesBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesBufOverflows.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesBufUnderflows_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacesBufUnderflows_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesBufUnderflows = _OacVoiceDialPeerVoiceVtoacesBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 10),
    _OacVoiceDialPeerVoiceVtoacesBufUnderflows_Type()
)
oacVoiceDialPeerVoiceVtoacesBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesBufUnderflows.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesPointerReframes_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacesPointerReframes_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesPointerReframes = _OacVoiceDialPeerVoiceVtoacesPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 11),
    _OacVoiceDialPeerVoiceVtoacesPointerReframes_Type()
)
oacVoiceDialPeerVoiceVtoacesPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesPointerReframes.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesHdrErrors_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacesHdrErrors_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesHdrErrors = _OacVoiceDialPeerVoiceVtoacesHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 12),
    _OacVoiceDialPeerVoiceVtoacesHdrErrors_Type()
)
oacVoiceDialPeerVoiceVtoacesHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesHdrErrors.setStatus("current")
_OacVoiceDialPeerVoiceVtoacesLossCells_Type = Unsigned32
_OacVoiceDialPeerVoiceVtoacesLossCells_Object = MibTableColumn
oacVoiceDialPeerVoiceVtoacesLossCells = _OacVoiceDialPeerVoiceVtoacesLossCells_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 2, 12, 1, 13),
    _OacVoiceDialPeerVoiceVtoacesLossCells_Type()
)
oacVoiceDialPeerVoiceVtoacesLossCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoiceVtoacesLossCells.setStatus("current")
_OacVoiceConnectionBles_ObjectIdentity = ObjectIdentity
oacVoiceConnectionBles = _OacVoiceConnectionBles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3)
)
_OacVoiceVmoaConnTable_Object = MibTable
oacVoiceVmoaConnTable = _OacVoiceVmoaConnTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    oacVoiceVmoaConnTable.setStatus("current")
_OacVoiceVmoaConnEntry_Object = MibTableRow
oacVoiceVmoaConnEntry = _OacVoiceVmoaConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 1, 1)
)
oacVoiceVmoaConnEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnConnection"),
)
if mibBuilder.loadTexts:
    oacVoiceVmoaConnEntry.setStatus("current")


class _OacVoiceVmoaConnConnection_Type(Integer32):
    """Custom type oacVoiceVmoaConnConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_OacVoiceVmoaConnConnection_Type.__name__ = "Integer32"
_OacVoiceVmoaConnConnection_Object = MibTableColumn
oacVoiceVmoaConnConnection = _OacVoiceVmoaConnConnection_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 1, 1, 1),
    _OacVoiceVmoaConnConnection_Type()
)
oacVoiceVmoaConnConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnConnection.setStatus("current")


class _OacVoiceVmoaConnVpVc_Type(DisplayString):
    """Custom type oacVoiceVmoaConnVpVc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OacVoiceVmoaConnVpVc_Type.__name__ = "DisplayString"
_OacVoiceVmoaConnVpVc_Object = MibTableColumn
oacVoiceVmoaConnVpVc = _OacVoiceVmoaConnVpVc_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 1, 1, 2),
    _OacVoiceVmoaConnVpVc_Type()
)
oacVoiceVmoaConnVpVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnVpVc.setStatus("current")
_OacVoiceVmoaConnCurrentState_Type = VoiceUpDnState
_OacVoiceVmoaConnCurrentState_Object = MibTableColumn
oacVoiceVmoaConnCurrentState = _OacVoiceVmoaConnCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 1, 1, 3),
    _OacVoiceVmoaConnCurrentState_Type()
)
oacVoiceVmoaConnCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnCurrentState.setStatus("current")
_OacVoiceVmoaConnConfigState_Type = VoiceUpDnState
_OacVoiceVmoaConnConfigState_Object = MibTableColumn
oacVoiceVmoaConnConfigState = _OacVoiceVmoaConnConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 1, 1, 4),
    _OacVoiceVmoaConnConfigState_Type()
)
oacVoiceVmoaConnConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnConfigState.setStatus("current")
_OacVoiceVmoaConnAtmVcFailureOccurence_Type = Unsigned32
_OacVoiceVmoaConnAtmVcFailureOccurence_Object = MibTableColumn
oacVoiceVmoaConnAtmVcFailureOccurence = _OacVoiceVmoaConnAtmVcFailureOccurence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 1, 1, 5),
    _OacVoiceVmoaConnAtmVcFailureOccurence_Type()
)
oacVoiceVmoaConnAtmVcFailureOccurence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAtmVcFailureOccurence.setStatus("current")
_OacVoiceVmoaConnAtmVcTotalFailureDuration_Type = TimeTicks
_OacVoiceVmoaConnAtmVcTotalFailureDuration_Object = MibTableColumn
oacVoiceVmoaConnAtmVcTotalFailureDuration = _OacVoiceVmoaConnAtmVcTotalFailureDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 1, 1, 6),
    _OacVoiceVmoaConnAtmVcTotalFailureDuration_Type()
)
oacVoiceVmoaConnAtmVcTotalFailureDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAtmVcTotalFailureDuration.setStatus("current")
_OacVoiceVmoaConnLesTable_Object = MibTable
oacVoiceVmoaConnLesTable = _OacVoiceVmoaConnLesTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLesTable.setStatus("current")
_OacVoiceVmoaConnLesEntry_Object = MibTableRow
oacVoiceVmoaConnLesEntry = _OacVoiceVmoaConnLesEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 2, 1)
)
oacVoiceVmoaConnLesEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnConnection"),
)
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLesEntry.setStatus("current")
_OacVoiceVmoaConnLesVoicePathNum_Type = Unsigned32
_OacVoiceVmoaConnLesVoicePathNum_Object = MibTableColumn
oacVoiceVmoaConnLesVoicePathNum = _OacVoiceVmoaConnLesVoicePathNum_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 2, 1, 1),
    _OacVoiceVmoaConnLesVoicePathNum_Type()
)
oacVoiceVmoaConnLesVoicePathNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLesVoicePathNum.setStatus("current")
_OacVoiceVmoaConnLesTotalCpIwfOriginated_Type = Unsigned32
_OacVoiceVmoaConnLesTotalCpIwfOriginated_Object = MibTableColumn
oacVoiceVmoaConnLesTotalCpIwfOriginated = _OacVoiceVmoaConnLesTotalCpIwfOriginated_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 2, 1, 2),
    _OacVoiceVmoaConnLesTotalCpIwfOriginated_Type()
)
oacVoiceVmoaConnLesTotalCpIwfOriginated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLesTotalCpIwfOriginated.setStatus("current")
_OacVoiceVmoaConnLesTotalCoIwfOriginated_Type = Unsigned32
_OacVoiceVmoaConnLesTotalCoIwfOriginated_Object = MibTableColumn
oacVoiceVmoaConnLesTotalCoIwfOriginated = _OacVoiceVmoaConnLesTotalCoIwfOriginated_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 2, 1, 3),
    _OacVoiceVmoaConnLesTotalCoIwfOriginated_Type()
)
oacVoiceVmoaConnLesTotalCoIwfOriginated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLesTotalCoIwfOriginated.setStatus("current")
_OacVoiceVmoaConnLesCpIwfRestartNum_Type = Unsigned32
_OacVoiceVmoaConnLesCpIwfRestartNum_Object = MibTableColumn
oacVoiceVmoaConnLesCpIwfRestartNum = _OacVoiceVmoaConnLesCpIwfRestartNum_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 2, 1, 4),
    _OacVoiceVmoaConnLesCpIwfRestartNum_Type()
)
oacVoiceVmoaConnLesCpIwfRestartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLesCpIwfRestartNum.setStatus("current")
_OacVoiceVmoaConnLesCoIwfRestartNum_Type = Unsigned32
_OacVoiceVmoaConnLesCoIwfRestartNum_Object = MibTableColumn
oacVoiceVmoaConnLesCoIwfRestartNum = _OacVoiceVmoaConnLesCoIwfRestartNum_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 2, 1, 5),
    _OacVoiceVmoaConnLesCoIwfRestartNum_Type()
)
oacVoiceVmoaConnLesCoIwfRestartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLesCoIwfRestartNum.setStatus("current")
_OacVoiceVmoaConnElcpTable_Object = MibTable
oacVoiceVmoaConnElcpTable = _OacVoiceVmoaConnElcpTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    oacVoiceVmoaConnElcpTable.setStatus("current")
_OacVoiceVmoaConnElcpEntry_Object = MibTableRow
oacVoiceVmoaConnElcpEntry = _OacVoiceVmoaConnElcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 3, 1)
)
oacVoiceVmoaConnElcpEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnConnection"),
)
if mibBuilder.loadTexts:
    oacVoiceVmoaConnElcpEntry.setStatus("current")
_OacVoiceVmoaConnElcpTotalSuccessfulAllocation_Type = Unsigned32
_OacVoiceVmoaConnElcpTotalSuccessfulAllocation_Object = MibTableColumn
oacVoiceVmoaConnElcpTotalSuccessfulAllocation = _OacVoiceVmoaConnElcpTotalSuccessfulAllocation_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 3, 1, 1),
    _OacVoiceVmoaConnElcpTotalSuccessfulAllocation_Type()
)
oacVoiceVmoaConnElcpTotalSuccessfulAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnElcpTotalSuccessfulAllocation.setStatus("current")
_OacVoiceVmoaConnElcpTotalUnsuccessfulAllocation_Type = Unsigned32
_OacVoiceVmoaConnElcpTotalUnsuccessfulAllocation_Object = MibTableColumn
oacVoiceVmoaConnElcpTotalUnsuccessfulAllocation = _OacVoiceVmoaConnElcpTotalUnsuccessfulAllocation_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 3, 1, 2),
    _OacVoiceVmoaConnElcpTotalUnsuccessfulAllocation_Type()
)
oacVoiceVmoaConnElcpTotalUnsuccessfulAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnElcpTotalUnsuccessfulAllocation.setStatus("current")
_OacVoiceVmoaConnElcpTotalAllocationDuration_Type = TimeTicks
_OacVoiceVmoaConnElcpTotalAllocationDuration_Object = MibTableColumn
oacVoiceVmoaConnElcpTotalAllocationDuration = _OacVoiceVmoaConnElcpTotalAllocationDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 3, 1, 3),
    _OacVoiceVmoaConnElcpTotalAllocationDuration_Type()
)
oacVoiceVmoaConnElcpTotalAllocationDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnElcpTotalAllocationDuration.setStatus("current")
_OacVoiceVmoaConnLapv5Table_Object = MibTable
oacVoiceVmoaConnLapv5Table = _OacVoiceVmoaConnLapv5Table_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5Table.setStatus("current")
_OacVoiceVmoaConnLapv5Entry_Object = MibTableRow
oacVoiceVmoaConnLapv5Entry = _OacVoiceVmoaConnLapv5Entry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4, 1)
)
oacVoiceVmoaConnLapv5Entry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnConnection"),
)
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5Entry.setStatus("current")
_OacVoiceVmoaConnLapv5NbrRxFrame_Type = Unsigned32
_OacVoiceVmoaConnLapv5NbrRxFrame_Object = MibTableColumn
oacVoiceVmoaConnLapv5NbrRxFrame = _OacVoiceVmoaConnLapv5NbrRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4, 1, 1),
    _OacVoiceVmoaConnLapv5NbrRxFrame_Type()
)
oacVoiceVmoaConnLapv5NbrRxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5NbrRxFrame.setStatus("current")
_OacVoiceVmoaConnLapv5NbrTxFrame_Type = Unsigned32
_OacVoiceVmoaConnLapv5NbrTxFrame_Object = MibTableColumn
oacVoiceVmoaConnLapv5NbrTxFrame = _OacVoiceVmoaConnLapv5NbrTxFrame_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4, 1, 2),
    _OacVoiceVmoaConnLapv5NbrTxFrame_Type()
)
oacVoiceVmoaConnLapv5NbrTxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5NbrTxFrame.setStatus("current")
_OacVoiceVmoaConnLapv5NbrRxIFrame_Type = Unsigned32
_OacVoiceVmoaConnLapv5NbrRxIFrame_Object = MibTableColumn
oacVoiceVmoaConnLapv5NbrRxIFrame = _OacVoiceVmoaConnLapv5NbrRxIFrame_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4, 1, 3),
    _OacVoiceVmoaConnLapv5NbrRxIFrame_Type()
)
oacVoiceVmoaConnLapv5NbrRxIFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5NbrRxIFrame.setStatus("current")
_OacVoiceVmoaConnLapv5NbrTxIFrame_Type = Unsigned32
_OacVoiceVmoaConnLapv5NbrTxIFrame_Object = MibTableColumn
oacVoiceVmoaConnLapv5NbrTxIFrame = _OacVoiceVmoaConnLapv5NbrTxIFrame_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4, 1, 4),
    _OacVoiceVmoaConnLapv5NbrTxIFrame_Type()
)
oacVoiceVmoaConnLapv5NbrTxIFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5NbrTxIFrame.setStatus("current")
_OacVoiceVmoaConnLapv5NbrRxRejFrame_Type = Unsigned32
_OacVoiceVmoaConnLapv5NbrRxRejFrame_Object = MibTableColumn
oacVoiceVmoaConnLapv5NbrRxRejFrame = _OacVoiceVmoaConnLapv5NbrRxRejFrame_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4, 1, 5),
    _OacVoiceVmoaConnLapv5NbrRxRejFrame_Type()
)
oacVoiceVmoaConnLapv5NbrRxRejFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5NbrRxRejFrame.setStatus("current")
_OacVoiceVmoaConnLapv5NbrTxRejFrame_Type = Unsigned32
_OacVoiceVmoaConnLapv5NbrTxRejFrame_Object = MibTableColumn
oacVoiceVmoaConnLapv5NbrTxRejFrame = _OacVoiceVmoaConnLapv5NbrTxRejFrame_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4, 1, 6),
    _OacVoiceVmoaConnLapv5NbrTxRejFrame_Type()
)
oacVoiceVmoaConnLapv5NbrTxRejFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5NbrTxRejFrame.setStatus("current")
_OacVoiceVmoaConnLapv5NbrRxRnrFrame_Type = Unsigned32
_OacVoiceVmoaConnLapv5NbrRxRnrFrame_Object = MibTableColumn
oacVoiceVmoaConnLapv5NbrRxRnrFrame = _OacVoiceVmoaConnLapv5NbrRxRnrFrame_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4, 1, 7),
    _OacVoiceVmoaConnLapv5NbrRxRnrFrame_Type()
)
oacVoiceVmoaConnLapv5NbrRxRnrFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5NbrRxRnrFrame.setStatus("current")
_OacVoiceVmoaConnLapv5NbrTxRnrFrame_Type = Unsigned32
_OacVoiceVmoaConnLapv5NbrTxRnrFrame_Object = MibTableColumn
oacVoiceVmoaConnLapv5NbrTxRnrFrame = _OacVoiceVmoaConnLapv5NbrTxRnrFrame_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4, 1, 8),
    _OacVoiceVmoaConnLapv5NbrTxRnrFrame_Type()
)
oacVoiceVmoaConnLapv5NbrTxRnrFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5NbrTxRnrFrame.setStatus("current")
_OacVoiceVmoaConnLapv5NbrT200Expiration_Type = Unsigned32
_OacVoiceVmoaConnLapv5NbrT200Expiration_Object = MibTableColumn
oacVoiceVmoaConnLapv5NbrT200Expiration = _OacVoiceVmoaConnLapv5NbrT200Expiration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 4, 1, 9),
    _OacVoiceVmoaConnLapv5NbrT200Expiration_Type()
)
oacVoiceVmoaConnLapv5NbrT200Expiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnLapv5NbrT200Expiration.setStatus("current")
_OacVoiceVmoaConnAal2Table_Object = MibTable
oacVoiceVmoaConnAal2Table = _OacVoiceVmoaConnAal2Table_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAal2Table.setStatus("current")
_OacVoiceVmoaConnAal2Entry_Object = MibTableRow
oacVoiceVmoaConnAal2Entry = _OacVoiceVmoaConnAal2Entry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 5, 1)
)
oacVoiceVmoaConnAal2Entry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnConnection"),
)
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAal2Entry.setStatus("current")
_OacVoiceVmoaConnAal2TotalFramesReceived_Type = Unsigned32
_OacVoiceVmoaConnAal2TotalFramesReceived_Object = MibTableColumn
oacVoiceVmoaConnAal2TotalFramesReceived = _OacVoiceVmoaConnAal2TotalFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 5, 1, 1),
    _OacVoiceVmoaConnAal2TotalFramesReceived_Type()
)
oacVoiceVmoaConnAal2TotalFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAal2TotalFramesReceived.setStatus("current")
_OacVoiceVmoaConnAal2TotalBytesReceived_Type = Unsigned32
_OacVoiceVmoaConnAal2TotalBytesReceived_Object = MibTableColumn
oacVoiceVmoaConnAal2TotalBytesReceived = _OacVoiceVmoaConnAal2TotalBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 5, 1, 2),
    _OacVoiceVmoaConnAal2TotalBytesReceived_Type()
)
oacVoiceVmoaConnAal2TotalBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAal2TotalBytesReceived.setStatus("current")
_OacVoiceVmoaConnAal2TotalFramesDiscardedReceived_Type = Unsigned32
_OacVoiceVmoaConnAal2TotalFramesDiscardedReceived_Object = MibTableColumn
oacVoiceVmoaConnAal2TotalFramesDiscardedReceived = _OacVoiceVmoaConnAal2TotalFramesDiscardedReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 5, 1, 3),
    _OacVoiceVmoaConnAal2TotalFramesDiscardedReceived_Type()
)
oacVoiceVmoaConnAal2TotalFramesDiscardedReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAal2TotalFramesDiscardedReceived.setStatus("current")
_OacVoiceVmoaConnAal2TotalFramesErrorsReceived_Type = Unsigned32
_OacVoiceVmoaConnAal2TotalFramesErrorsReceived_Object = MibTableColumn
oacVoiceVmoaConnAal2TotalFramesErrorsReceived = _OacVoiceVmoaConnAal2TotalFramesErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 5, 1, 4),
    _OacVoiceVmoaConnAal2TotalFramesErrorsReceived_Type()
)
oacVoiceVmoaConnAal2TotalFramesErrorsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAal2TotalFramesErrorsReceived.setStatus("current")
_OacVoiceVmoaConnAal2TotalFramesSent_Type = Unsigned32
_OacVoiceVmoaConnAal2TotalFramesSent_Object = MibTableColumn
oacVoiceVmoaConnAal2TotalFramesSent = _OacVoiceVmoaConnAal2TotalFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 5, 1, 5),
    _OacVoiceVmoaConnAal2TotalFramesSent_Type()
)
oacVoiceVmoaConnAal2TotalFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAal2TotalFramesSent.setStatus("current")
_OacVoiceVmoaConnAal2TotalBytesSent_Type = Unsigned32
_OacVoiceVmoaConnAal2TotalBytesSent_Object = MibTableColumn
oacVoiceVmoaConnAal2TotalBytesSent = _OacVoiceVmoaConnAal2TotalBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 5, 1, 6),
    _OacVoiceVmoaConnAal2TotalBytesSent_Type()
)
oacVoiceVmoaConnAal2TotalBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAal2TotalBytesSent.setStatus("current")
_OacVoiceVmoaConnAal2TotalFramesDiscardedSent_Type = Unsigned32
_OacVoiceVmoaConnAal2TotalFramesDiscardedSent_Object = MibTableColumn
oacVoiceVmoaConnAal2TotalFramesDiscardedSent = _OacVoiceVmoaConnAal2TotalFramesDiscardedSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 5, 1, 7),
    _OacVoiceVmoaConnAal2TotalFramesDiscardedSent_Type()
)
oacVoiceVmoaConnAal2TotalFramesDiscardedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVmoaConnAal2TotalFramesDiscardedSent.setStatus("current")
_OacVoiceVtoaConnTable_Object = MibTable
oacVoiceVtoaConnTable = _OacVoiceVtoaConnTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    oacVoiceVtoaConnTable.setStatus("current")
_OacVoiceVtoaConnEntry_Object = MibTableRow
oacVoiceVtoaConnEntry = _OacVoiceVtoaConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 6, 1)
)
oacVoiceVtoaConnEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnConnection"),
)
if mibBuilder.loadTexts:
    oacVoiceVtoaConnEntry.setStatus("current")


class _OacVoiceVtoaConnConnection_Type(Integer32):
    """Custom type oacVoiceVtoaConnConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_OacVoiceVtoaConnConnection_Type.__name__ = "Integer32"
_OacVoiceVtoaConnConnection_Object = MibTableColumn
oacVoiceVtoaConnConnection = _OacVoiceVtoaConnConnection_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 6, 1, 1),
    _OacVoiceVtoaConnConnection_Type()
)
oacVoiceVtoaConnConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnConnection.setStatus("current")


class _OacVoiceVtoaConnVpVc_Type(DisplayString):
    """Custom type oacVoiceVtoaConnVpVc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OacVoiceVtoaConnVpVc_Type.__name__ = "DisplayString"
_OacVoiceVtoaConnVpVc_Object = MibTableColumn
oacVoiceVtoaConnVpVc = _OacVoiceVtoaConnVpVc_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 6, 1, 2),
    _OacVoiceVtoaConnVpVc_Type()
)
oacVoiceVtoaConnVpVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnVpVc.setStatus("current")
_OacVoiceVtoaConnCurrentState_Type = VoiceUpDnState
_OacVoiceVtoaConnCurrentState_Object = MibTableColumn
oacVoiceVtoaConnCurrentState = _OacVoiceVtoaConnCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 6, 1, 3),
    _OacVoiceVtoaConnCurrentState_Type()
)
oacVoiceVtoaConnCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnCurrentState.setStatus("current")
_OacVoiceVtoaConnConfigState_Type = VoiceUpDnState
_OacVoiceVtoaConnConfigState_Object = MibTableColumn
oacVoiceVtoaConnConfigState = _OacVoiceVtoaConnConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 6, 1, 4),
    _OacVoiceVtoaConnConfigState_Type()
)
oacVoiceVtoaConnConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnConfigState.setStatus("current")
_OacVoiceVtoaConnAtmVcFailureOccurence_Type = Unsigned32
_OacVoiceVtoaConnAtmVcFailureOccurence_Object = MibTableColumn
oacVoiceVtoaConnAtmVcFailureOccurence = _OacVoiceVtoaConnAtmVcFailureOccurence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 6, 1, 5),
    _OacVoiceVtoaConnAtmVcFailureOccurence_Type()
)
oacVoiceVtoaConnAtmVcFailureOccurence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAtmVcFailureOccurence.setStatus("current")
_OacVoiceVtoaConnAtmVcTotalFailureDuration_Type = TimeTicks
_OacVoiceVtoaConnAtmVcTotalFailureDuration_Object = MibTableColumn
oacVoiceVtoaConnAtmVcTotalFailureDuration = _OacVoiceVtoaConnAtmVcTotalFailureDuration_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 6, 1, 6),
    _OacVoiceVtoaConnAtmVcTotalFailureDuration_Type()
)
oacVoiceVtoaConnAtmVcTotalFailureDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAtmVcTotalFailureDuration.setStatus("current")
_OacVoiceVtoaConnAal2Table_Object = MibTable
oacVoiceVtoaConnAal2Table = _OacVoiceVtoaConnAal2Table_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAal2Table.setStatus("current")
_OacVoiceVtoaConnAal2Entry_Object = MibTableRow
oacVoiceVtoaConnAal2Entry = _OacVoiceVtoaConnAal2Entry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 7, 1)
)
oacVoiceVtoaConnAal2Entry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnConnection"),
)
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAal2Entry.setStatus("current")
_OacVoiceVtoaConnAal2TotalFramesReceived_Type = Unsigned32
_OacVoiceVtoaConnAal2TotalFramesReceived_Object = MibTableColumn
oacVoiceVtoaConnAal2TotalFramesReceived = _OacVoiceVtoaConnAal2TotalFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 7, 1, 1),
    _OacVoiceVtoaConnAal2TotalFramesReceived_Type()
)
oacVoiceVtoaConnAal2TotalFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAal2TotalFramesReceived.setStatus("current")
_OacVoiceVtoaConnAal2TotalBytesReceived_Type = Unsigned32
_OacVoiceVtoaConnAal2TotalBytesReceived_Object = MibTableColumn
oacVoiceVtoaConnAal2TotalBytesReceived = _OacVoiceVtoaConnAal2TotalBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 7, 1, 2),
    _OacVoiceVtoaConnAal2TotalBytesReceived_Type()
)
oacVoiceVtoaConnAal2TotalBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAal2TotalBytesReceived.setStatus("current")
_OacVoiceVtoaConnAal2TotalFramesDiscardedReceived_Type = Unsigned32
_OacVoiceVtoaConnAal2TotalFramesDiscardedReceived_Object = MibTableColumn
oacVoiceVtoaConnAal2TotalFramesDiscardedReceived = _OacVoiceVtoaConnAal2TotalFramesDiscardedReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 7, 1, 3),
    _OacVoiceVtoaConnAal2TotalFramesDiscardedReceived_Type()
)
oacVoiceVtoaConnAal2TotalFramesDiscardedReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAal2TotalFramesDiscardedReceived.setStatus("current")
_OacVoiceVtoaConnAal2TotalFramesErrorsReceived_Type = Unsigned32
_OacVoiceVtoaConnAal2TotalFramesErrorsReceived_Object = MibTableColumn
oacVoiceVtoaConnAal2TotalFramesErrorsReceived = _OacVoiceVtoaConnAal2TotalFramesErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 7, 1, 4),
    _OacVoiceVtoaConnAal2TotalFramesErrorsReceived_Type()
)
oacVoiceVtoaConnAal2TotalFramesErrorsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAal2TotalFramesErrorsReceived.setStatus("current")
_OacVoiceVtoaConnAal2TotalFramesSent_Type = Unsigned32
_OacVoiceVtoaConnAal2TotalFramesSent_Object = MibTableColumn
oacVoiceVtoaConnAal2TotalFramesSent = _OacVoiceVtoaConnAal2TotalFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 7, 1, 5),
    _OacVoiceVtoaConnAal2TotalFramesSent_Type()
)
oacVoiceVtoaConnAal2TotalFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAal2TotalFramesSent.setStatus("current")
_OacVoiceVtoaConnAal2TotalBytesSent_Type = Unsigned32
_OacVoiceVtoaConnAal2TotalBytesSent_Object = MibTableColumn
oacVoiceVtoaConnAal2TotalBytesSent = _OacVoiceVtoaConnAal2TotalBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 7, 1, 6),
    _OacVoiceVtoaConnAal2TotalBytesSent_Type()
)
oacVoiceVtoaConnAal2TotalBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAal2TotalBytesSent.setStatus("current")
_OacVoiceVtoaConnAal2TotalFramesDiscardedSent_Type = Unsigned32
_OacVoiceVtoaConnAal2TotalFramesDiscardedSent_Object = MibTableColumn
oacVoiceVtoaConnAal2TotalFramesDiscardedSent = _OacVoiceVtoaConnAal2TotalFramesDiscardedSent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 2, 3, 7, 1, 7),
    _OacVoiceVtoaConnAal2TotalFramesDiscardedSent_Type()
)
oacVoiceVtoaConnAal2TotalFramesDiscardedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceVtoaConnAal2TotalFramesDiscardedSent.setStatus("current")
_OacVoiceStatVoip_ObjectIdentity = ObjectIdentity
oacVoiceStatVoip = _OacVoiceStatVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3)
)
_OacVoicePortVoipTable_Object = MibTable
oacVoicePortVoipTable = _OacVoicePortVoipTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    oacVoicePortVoipTable.setStatus("current")
_OacVoicePortVoipEntry_Object = MibTableRow
oacVoicePortVoipEntry = _OacVoicePortVoipEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1)
)
oacVoicePortVoipEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoicePortIfIndex"),
)
if mibBuilder.loadTexts:
    oacVoicePortVoipEntry.setStatus("current")


class _OacVoicePortIfIndex_Type(Integer32):
    """Custom type oacVoicePortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacVoicePortIfIndex_Type.__name__ = "Integer32"
_OacVoicePortIfIndex_Object = MibTableColumn
oacVoicePortIfIndex = _OacVoicePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 1),
    _OacVoicePortIfIndex_Type()
)
oacVoicePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortIfIndex.setStatus("current")


class _OacVoicePortVoipPortName_Type(DisplayString):
    """Custom type oacVoicePortVoipPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_OacVoicePortVoipPortName_Type.__name__ = "DisplayString"
_OacVoicePortVoipPortName_Object = MibTableColumn
oacVoicePortVoipPortName = _OacVoicePortVoipPortName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 2),
    _OacVoicePortVoipPortName_Type()
)
oacVoicePortVoipPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipPortName.setStatus("current")
_OacVoicePortVoipPortType_Type = VoipPortType
_OacVoicePortVoipPortType_Object = MibTableColumn
oacVoicePortVoipPortType = _OacVoicePortVoipPortType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 3),
    _OacVoicePortVoipPortType_Type()
)
oacVoicePortVoipPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipPortType.setStatus("current")
_OacVoicePortVoipPriPhysicalType_Type = OacVoipPriPhysicalType
_OacVoicePortVoipPriPhysicalType_Object = MibTableColumn
oacVoicePortVoipPriPhysicalType = _OacVoicePortVoipPriPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 4),
    _OacVoicePortVoipPriPhysicalType_Type()
)
oacVoicePortVoipPriPhysicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipPriPhysicalType.setStatus("current")
_OacVoicePortVoipIsdnProtocolDescriptor_Type = IsdnProtocolDescriptor
_OacVoicePortVoipIsdnProtocolDescriptor_Object = MibTableColumn
oacVoicePortVoipIsdnProtocolDescriptor = _OacVoicePortVoipIsdnProtocolDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 5),
    _OacVoicePortVoipIsdnProtocolDescriptor_Type()
)
oacVoicePortVoipIsdnProtocolDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIsdnProtocolDescriptor.setStatus("current")
_OacVoicePortVoipCurrentState_Type = PortVoipCurrentState
_OacVoicePortVoipCurrentState_Object = MibTableColumn
oacVoicePortVoipCurrentState = _OacVoicePortVoipCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 6),
    _OacVoicePortVoipCurrentState_Type()
)
oacVoicePortVoipCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipCurrentState.setStatus("current")
_OacVoicePortVoipConfigState_Type = ConfigState
_OacVoicePortVoipConfigState_Object = MibTableColumn
oacVoicePortVoipConfigState = _OacVoicePortVoipConfigState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 7),
    _OacVoicePortVoipConfigState_Type()
)
oacVoicePortVoipConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipConfigState.setStatus("current")
_OacVoicePortVoipIsdnLayer1Status_Type = IsdnLayerStatus
_OacVoicePortVoipIsdnLayer1Status_Object = MibTableColumn
oacVoicePortVoipIsdnLayer1Status = _OacVoicePortVoipIsdnLayer1Status_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 8),
    _OacVoicePortVoipIsdnLayer1Status_Type()
)
oacVoicePortVoipIsdnLayer1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIsdnLayer1Status.setStatus("current")
_OacVoicePortVoipIsdnLayer2Status_Type = DisplayString
_OacVoicePortVoipIsdnLayer2Status_Object = MibTableColumn
oacVoicePortVoipIsdnLayer2Status = _OacVoicePortVoipIsdnLayer2Status_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 9),
    _OacVoicePortVoipIsdnLayer2Status_Type()
)
oacVoicePortVoipIsdnLayer2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIsdnLayer2Status.setStatus("current")
_OacVoicePortVoipAttachedDialPeer_Type = Integer32
_OacVoicePortVoipAttachedDialPeer_Object = MibTableColumn
oacVoicePortVoipAttachedDialPeer = _OacVoicePortVoipAttachedDialPeer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 10),
    _OacVoicePortVoipAttachedDialPeer_Type()
)
oacVoicePortVoipAttachedDialPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipAttachedDialPeer.setStatus("current")
_OacVoicePortVoipCurrentCalls_Type = Integer32
_OacVoicePortVoipCurrentCalls_Object = MibTableColumn
oacVoicePortVoipCurrentCalls = _OacVoicePortVoipCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 11),
    _OacVoicePortVoipCurrentCalls_Type()
)
oacVoicePortVoipCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipCurrentCalls.setStatus("current")
_OacVoicePortVoipIsdnTxFramesOnDChannel_Type = Integer32
_OacVoicePortVoipIsdnTxFramesOnDChannel_Object = MibTableColumn
oacVoicePortVoipIsdnTxFramesOnDChannel = _OacVoicePortVoipIsdnTxFramesOnDChannel_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 12),
    _OacVoicePortVoipIsdnTxFramesOnDChannel_Type()
)
oacVoicePortVoipIsdnTxFramesOnDChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIsdnTxFramesOnDChannel.setStatus("current")
_OacVoicePortVoipIsdnRxFramesOnDChannel_Type = Integer32
_OacVoicePortVoipIsdnRxFramesOnDChannel_Object = MibTableColumn
oacVoicePortVoipIsdnRxFramesOnDChannel = _OacVoicePortVoipIsdnRxFramesOnDChannel_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 13),
    _OacVoicePortVoipIsdnRxFramesOnDChannel_Type()
)
oacVoicePortVoipIsdnRxFramesOnDChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIsdnRxFramesOnDChannel.setStatus("current")
_OacVoicePortVoipPriNbAisOccurence_Type = Integer32
_OacVoicePortVoipPriNbAisOccurence_Object = MibTableColumn
oacVoicePortVoipPriNbAisOccurence = _OacVoicePortVoipPriNbAisOccurence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 14),
    _OacVoicePortVoipPriNbAisOccurence_Type()
)
oacVoicePortVoipPriNbAisOccurence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipPriNbAisOccurence.setStatus("current")
_OacVoicePortVoipPriNbRdiOccurence_Type = Integer32
_OacVoicePortVoipPriNbRdiOccurence_Object = MibTableColumn
oacVoicePortVoipPriNbRdiOccurence = _OacVoicePortVoipPriNbRdiOccurence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 15),
    _OacVoicePortVoipPriNbRdiOccurence_Type()
)
oacVoicePortVoipPriNbRdiOccurence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipPriNbRdiOccurence.setStatus("current")
_OacVoicePortVoipOutCalls_Type = Integer32
_OacVoicePortVoipOutCalls_Object = MibTableColumn
oacVoicePortVoipOutCalls = _OacVoicePortVoipOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 16),
    _OacVoicePortVoipOutCalls_Type()
)
oacVoicePortVoipOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCalls.setStatus("current")
_OacVoicePortVoipOutCallsFailures_Type = Integer32
_OacVoicePortVoipOutCallsFailures_Object = MibTableColumn
oacVoicePortVoipOutCallsFailures = _OacVoicePortVoipOutCallsFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 17),
    _OacVoicePortVoipOutCallsFailures_Type()
)
oacVoicePortVoipOutCallsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsFailures.setStatus("current")
_OacVoicePortVoipOutCallsUnsufficientPotsGroupResource_Type = Integer32
_OacVoicePortVoipOutCallsUnsufficientPotsGroupResource_Object = MibTableColumn
oacVoicePortVoipOutCallsUnsufficientPotsGroupResource = _OacVoicePortVoipOutCallsUnsufficientPotsGroupResource_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 18),
    _OacVoicePortVoipOutCallsUnsufficientPotsGroupResource_Type()
)
oacVoicePortVoipOutCallsUnsufficientPotsGroupResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsUnsufficientPotsGroupResource.setStatus("current")
_OacVoicePortVoipOutCallsIsdnPhysicalInterfaceDown_Type = Integer32
_OacVoicePortVoipOutCallsIsdnPhysicalInterfaceDown_Object = MibTableColumn
oacVoicePortVoipOutCallsIsdnPhysicalInterfaceDown = _OacVoicePortVoipOutCallsIsdnPhysicalInterfaceDown_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 19),
    _OacVoicePortVoipOutCallsIsdnPhysicalInterfaceDown_Type()
)
oacVoicePortVoipOutCallsIsdnPhysicalInterfaceDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsIsdnPhysicalInterfaceDown.setStatus("current")
_OacVoicePortVoipOutCallsIsdnCauseClass0_Type = Integer32
_OacVoicePortVoipOutCallsIsdnCauseClass0_Object = MibTableColumn
oacVoicePortVoipOutCallsIsdnCauseClass0 = _OacVoicePortVoipOutCallsIsdnCauseClass0_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 20),
    _OacVoicePortVoipOutCallsIsdnCauseClass0_Type()
)
oacVoicePortVoipOutCallsIsdnCauseClass0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsIsdnCauseClass0.setStatus("current")
_OacVoicePortVoipOutCallsIsdnCauseClass1_Type = Integer32
_OacVoicePortVoipOutCallsIsdnCauseClass1_Object = MibTableColumn
oacVoicePortVoipOutCallsIsdnCauseClass1 = _OacVoicePortVoipOutCallsIsdnCauseClass1_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 21),
    _OacVoicePortVoipOutCallsIsdnCauseClass1_Type()
)
oacVoicePortVoipOutCallsIsdnCauseClass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsIsdnCauseClass1.setStatus("current")
_OacVoicePortVoipOutCallsIsdnCC1NormalCause_Type = Integer32
_OacVoicePortVoipOutCallsIsdnCC1NormalCause_Object = MibTableColumn
oacVoicePortVoipOutCallsIsdnCC1NormalCause = _OacVoicePortVoipOutCallsIsdnCC1NormalCause_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 22),
    _OacVoicePortVoipOutCallsIsdnCC1NormalCause_Type()
)
oacVoicePortVoipOutCallsIsdnCC1NormalCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsIsdnCC1NormalCause.setStatus("current")
_OacVoicePortVoipOutCallsCC1UserBusy_Type = Integer32
_OacVoicePortVoipOutCallsCC1UserBusy_Object = MibTableColumn
oacVoicePortVoipOutCallsCC1UserBusy = _OacVoicePortVoipOutCallsCC1UserBusy_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 23),
    _OacVoicePortVoipOutCallsCC1UserBusy_Type()
)
oacVoicePortVoipOutCallsCC1UserBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsCC1UserBusy.setStatus("current")
_OacVoicePortVoipOutCallsCC1NoAnswer_Type = Integer32
_OacVoicePortVoipOutCallsCC1NoAnswer_Object = MibTableColumn
oacVoicePortVoipOutCallsCC1NoAnswer = _OacVoicePortVoipOutCallsCC1NoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 24),
    _OacVoicePortVoipOutCallsCC1NoAnswer_Type()
)
oacVoicePortVoipOutCallsCC1NoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsCC1NoAnswer.setStatus("current")
_OacVoicePortVoipOutCallsIsdnCauseClass2_Type = Integer32
_OacVoicePortVoipOutCallsIsdnCauseClass2_Object = MibTableColumn
oacVoicePortVoipOutCallsIsdnCauseClass2 = _OacVoicePortVoipOutCallsIsdnCauseClass2_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 25),
    _OacVoicePortVoipOutCallsIsdnCauseClass2_Type()
)
oacVoicePortVoipOutCallsIsdnCauseClass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsIsdnCauseClass2.setStatus("current")
_OacVoicePortVoipOutCallsIsdnCauseClass3_Type = Integer32
_OacVoicePortVoipOutCallsIsdnCauseClass3_Object = MibTableColumn
oacVoicePortVoipOutCallsIsdnCauseClass3 = _OacVoicePortVoipOutCallsIsdnCauseClass3_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 26),
    _OacVoicePortVoipOutCallsIsdnCauseClass3_Type()
)
oacVoicePortVoipOutCallsIsdnCauseClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsIsdnCauseClass3.setStatus("current")
_OacVoicePortVoipOutCallsIsdnCauseClass4_Type = Integer32
_OacVoicePortVoipOutCallsIsdnCauseClass4_Object = MibTableColumn
oacVoicePortVoipOutCallsIsdnCauseClass4 = _OacVoicePortVoipOutCallsIsdnCauseClass4_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 27),
    _OacVoicePortVoipOutCallsIsdnCauseClass4_Type()
)
oacVoicePortVoipOutCallsIsdnCauseClass4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsIsdnCauseClass4.setStatus("current")
_OacVoicePortVoipOutCallsIsdnCauseClass5_Type = Integer32
_OacVoicePortVoipOutCallsIsdnCauseClass5_Object = MibTableColumn
oacVoicePortVoipOutCallsIsdnCauseClass5 = _OacVoicePortVoipOutCallsIsdnCauseClass5_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 28),
    _OacVoicePortVoipOutCallsIsdnCauseClass5_Type()
)
oacVoicePortVoipOutCallsIsdnCauseClass5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsIsdnCauseClass5.setStatus("current")
_OacVoicePortVoipOutCallsIsdnCauseClass6_Type = Integer32
_OacVoicePortVoipOutCallsIsdnCauseClass6_Object = MibTableColumn
oacVoicePortVoipOutCallsIsdnCauseClass6 = _OacVoicePortVoipOutCallsIsdnCauseClass6_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 29),
    _OacVoicePortVoipOutCallsIsdnCauseClass6_Type()
)
oacVoicePortVoipOutCallsIsdnCauseClass6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsIsdnCauseClass6.setStatus("current")
_OacVoicePortVoipOutCallsIsdnCauseClass7_Type = Integer32
_OacVoicePortVoipOutCallsIsdnCauseClass7_Object = MibTableColumn
oacVoicePortVoipOutCallsIsdnCauseClass7 = _OacVoicePortVoipOutCallsIsdnCauseClass7_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 30),
    _OacVoicePortVoipOutCallsIsdnCauseClass7_Type()
)
oacVoicePortVoipOutCallsIsdnCauseClass7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipOutCallsIsdnCauseClass7.setStatus("current")
_OacVoicePortVoipIncCalls_Type = Integer32
_OacVoicePortVoipIncCalls_Object = MibTableColumn
oacVoicePortVoipIncCalls = _OacVoicePortVoipIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 31),
    _OacVoicePortVoipIncCalls_Type()
)
oacVoicePortVoipIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIncCalls.setStatus("current")
_OacVoicePortVoipIncCallsBackupInvoked_Type = Integer32
_OacVoicePortVoipIncCallsBackupInvoked_Object = MibTableColumn
oacVoicePortVoipIncCallsBackupInvoked = _OacVoicePortVoipIncCallsBackupInvoked_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 32),
    _OacVoicePortVoipIncCallsBackupInvoked_Type()
)
oacVoicePortVoipIncCallsBackupInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIncCallsBackupInvoked.setStatus("current")
_OacVoicePortVoipIncCallsFailures_Type = Integer32
_OacVoicePortVoipIncCallsFailures_Object = MibTableColumn
oacVoicePortVoipIncCallsFailures = _OacVoicePortVoipIncCallsFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 33),
    _OacVoicePortVoipIncCallsFailures_Type()
)
oacVoicePortVoipIncCallsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIncCallsFailures.setStatus("current")
_OacVoicePortVoipIncCallsRemoteFailure_Type = Integer32
_OacVoicePortVoipIncCallsRemoteFailure_Object = MibTableColumn
oacVoicePortVoipIncCallsRemoteFailure = _OacVoicePortVoipIncCallsRemoteFailure_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 34),
    _OacVoicePortVoipIncCallsRemoteFailure_Type()
)
oacVoicePortVoipIncCallsRemoteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIncCallsRemoteFailure.setStatus("current")
_OacVoicePortVoipIncCallsUnknownNumber_Type = Integer32
_OacVoicePortVoipIncCallsUnknownNumber_Object = MibTableColumn
oacVoicePortVoipIncCallsUnknownNumber = _OacVoicePortVoipIncCallsUnknownNumber_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 35),
    _OacVoicePortVoipIncCallsUnknownNumber_Type()
)
oacVoicePortVoipIncCallsUnknownNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIncCallsUnknownNumber.setStatus("current")
_OacVoicePortVoipIncCallsDspUnavailable_Type = Integer32
_OacVoicePortVoipIncCallsDspUnavailable_Object = MibTableColumn
oacVoicePortVoipIncCallsDspUnavailable = _OacVoicePortVoipIncCallsDspUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 36),
    _OacVoicePortVoipIncCallsDspUnavailable_Type()
)
oacVoicePortVoipIncCallsDspUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIncCallsDspUnavailable.setStatus("current")
_OacVoicePortVoipIncCallsNoVoipRessourceAvailable_Type = Integer32
_OacVoicePortVoipIncCallsNoVoipRessourceAvailable_Object = MibTableColumn
oacVoicePortVoipIncCallsNoVoipRessourceAvailable = _OacVoicePortVoipIncCallsNoVoipRessourceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 37),
    _OacVoicePortVoipIncCallsNoVoipRessourceAvailable_Type()
)
oacVoicePortVoipIncCallsNoVoipRessourceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIncCallsNoVoipRessourceAvailable.setStatus("current")
_OacVoicePortVoipIncCallsNotSpecified_Type = Integer32
_OacVoicePortVoipIncCallsNotSpecified_Object = MibTableColumn
oacVoicePortVoipIncCallsNotSpecified = _OacVoicePortVoipIncCallsNotSpecified_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 38),
    _OacVoicePortVoipIncCallsNotSpecified_Type()
)
oacVoicePortVoipIncCallsNotSpecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipIncCallsNotSpecified.setStatus("current")
_OacVoicePortVoipMgcpOffHookEvents_Type = Integer32
_OacVoicePortVoipMgcpOffHookEvents_Object = MibTableColumn
oacVoicePortVoipMgcpOffHookEvents = _OacVoicePortVoipMgcpOffHookEvents_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 39),
    _OacVoicePortVoipMgcpOffHookEvents_Type()
)
oacVoicePortVoipMgcpOffHookEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipMgcpOffHookEvents.setStatus("current")
_OacVoicePortVoipMgcpOutCallsPathEstablished_Type = Integer32
_OacVoicePortVoipMgcpOutCallsPathEstablished_Object = MibTableColumn
oacVoicePortVoipMgcpOutCallsPathEstablished = _OacVoicePortVoipMgcpOutCallsPathEstablished_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 40),
    _OacVoicePortVoipMgcpOutCallsPathEstablished_Type()
)
oacVoicePortVoipMgcpOutCallsPathEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipMgcpOutCallsPathEstablished.setStatus("current")
_OacVoicePortVoipMgcpRingingEvents_Type = Integer32
_OacVoicePortVoipMgcpRingingEvents_Object = MibTableColumn
oacVoicePortVoipMgcpRingingEvents = _OacVoicePortVoipMgcpRingingEvents_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 41),
    _OacVoicePortVoipMgcpRingingEvents_Type()
)
oacVoicePortVoipMgcpRingingEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipMgcpRingingEvents.setStatus("current")
_OacVoicePortVoipMgcpIncCallsPathEstablished_Type = Integer32
_OacVoicePortVoipMgcpIncCallsPathEstablished_Object = MibTableColumn
oacVoicePortVoipMgcpIncCallsPathEstablished = _OacVoicePortVoipMgcpIncCallsPathEstablished_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 1, 1, 42),
    _OacVoicePortVoipMgcpIncCallsPathEstablished_Type()
)
oacVoicePortVoipMgcpIncCallsPathEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoicePortVoipMgcpIncCallsPathEstablished.setStatus("current")
_OacVoiceDialPeerVoipTable_Object = MibTable
oacVoiceDialPeerVoipTable = _OacVoiceDialPeerVoipTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoipTable.setStatus("current")
_OacVoiceDialPeerVoipEntry_Object = MibTableRow
oacVoiceDialPeerVoipEntry = _OacVoiceDialPeerVoipEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1)
)
oacVoiceDialPeerVoipEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIndex"),
)
if mibBuilder.loadTexts:
    oacVoiceDialPeerVoipEntry.setStatus("current")
_OacVoiceDialPeerIndex_Type = Integer32
_OacVoiceDialPeerIndex_Object = MibTableColumn
oacVoiceDialPeerIndex = _OacVoiceDialPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 1),
    _OacVoiceDialPeerIndex_Type()
)
oacVoiceDialPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIndex.setStatus("current")
_OacVoiceDialPeerCurrentCalls_Type = Integer32
_OacVoiceDialPeerCurrentCalls_Object = MibTableColumn
oacVoiceDialPeerCurrentCalls = _OacVoiceDialPeerCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 2),
    _OacVoiceDialPeerCurrentCalls_Type()
)
oacVoiceDialPeerCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerCurrentCalls.setStatus("current")
_OacVoiceDialPeerOutCalls_Type = Integer32
_OacVoiceDialPeerOutCalls_Object = MibTableColumn
oacVoiceDialPeerOutCalls = _OacVoiceDialPeerOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 3),
    _OacVoiceDialPeerOutCalls_Type()
)
oacVoiceDialPeerOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCalls.setStatus("current")
_OacVoiceDialPeerOutCallsMgcpOffHookEvents_Type = Integer32
_OacVoiceDialPeerOutCallsMgcpOffHookEvents_Object = MibTableColumn
oacVoiceDialPeerOutCallsMgcpOffHookEvents = _OacVoiceDialPeerOutCallsMgcpOffHookEvents_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 4),
    _OacVoiceDialPeerOutCallsMgcpOffHookEvents_Type()
)
oacVoiceDialPeerOutCallsMgcpOffHookEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsMgcpOffHookEvents.setStatus("current")
_OacVoiceDialPeerOutCallsMgcpPathEstablished_Type = Integer32
_OacVoiceDialPeerOutCallsMgcpPathEstablished_Object = MibTableColumn
oacVoiceDialPeerOutCallsMgcpPathEstablished = _OacVoiceDialPeerOutCallsMgcpPathEstablished_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 5),
    _OacVoiceDialPeerOutCallsMgcpPathEstablished_Type()
)
oacVoiceDialPeerOutCallsMgcpPathEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsMgcpPathEstablished.setStatus("current")
_OacVoiceDialPeerOutCallsFailures_Type = Integer32
_OacVoiceDialPeerOutCallsFailures_Object = MibTableColumn
oacVoiceDialPeerOutCallsFailures = _OacVoiceDialPeerOutCallsFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 6),
    _OacVoiceDialPeerOutCallsFailures_Type()
)
oacVoiceDialPeerOutCallsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsFailures.setStatus("current")
_OacVoiceDialPeerOutCallsRasFailures_Type = Integer32
_OacVoiceDialPeerOutCallsRasFailures_Object = MibTableColumn
oacVoiceDialPeerOutCallsRasFailures = _OacVoiceDialPeerOutCallsRasFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 7),
    _OacVoiceDialPeerOutCallsRasFailures_Type()
)
oacVoiceDialPeerOutCallsRasFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsRasFailures.setStatus("current")
_OacVoiceDialPeerOutCallsRasFailGatekeeperUnavailable_Type = Integer32
_OacVoiceDialPeerOutCallsRasFailGatekeeperUnavailable_Object = MibTableColumn
oacVoiceDialPeerOutCallsRasFailGatekeeperUnavailable = _OacVoiceDialPeerOutCallsRasFailGatekeeperUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 8),
    _OacVoiceDialPeerOutCallsRasFailGatekeeperUnavailable_Type()
)
oacVoiceDialPeerOutCallsRasFailGatekeeperUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsRasFailGatekeeperUnavailable.setStatus("current")
_OacVoiceDialPeerOutCallsRasFailAdmissionRejects_Type = Integer32
_OacVoiceDialPeerOutCallsRasFailAdmissionRejects_Object = MibTableColumn
oacVoiceDialPeerOutCallsRasFailAdmissionRejects = _OacVoiceDialPeerOutCallsRasFailAdmissionRejects_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 9),
    _OacVoiceDialPeerOutCallsRasFailAdmissionRejects_Type()
)
oacVoiceDialPeerOutCallsRasFailAdmissionRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsRasFailAdmissionRejects.setStatus("current")
_OacVoiceDialPeerOutCallsH225Q931Failures_Type = Integer32
_OacVoiceDialPeerOutCallsH225Q931Failures_Object = MibTableColumn
oacVoiceDialPeerOutCallsH225Q931Failures = _OacVoiceDialPeerOutCallsH225Q931Failures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 10),
    _OacVoiceDialPeerOutCallsH225Q931Failures_Type()
)
oacVoiceDialPeerOutCallsH225Q931Failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsH225Q931Failures.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCauseClass0_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCauseClass0_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCauseClass0 = _OacVoiceDialPeerOutCallsHQFailCauseClass0_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 11),
    _OacVoiceDialPeerOutCallsHQFailCauseClass0_Type()
)
oacVoiceDialPeerOutCallsHQFailCauseClass0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCauseClass0.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCauseClass1_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCauseClass1_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCauseClass1 = _OacVoiceDialPeerOutCallsHQFailCauseClass1_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 12),
    _OacVoiceDialPeerOutCallsHQFailCauseClass1_Type()
)
oacVoiceDialPeerOutCallsHQFailCauseClass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCauseClass1.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCC1NormalCause_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCC1NormalCause_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCC1NormalCause = _OacVoiceDialPeerOutCallsHQFailCC1NormalCause_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 13),
    _OacVoiceDialPeerOutCallsHQFailCC1NormalCause_Type()
)
oacVoiceDialPeerOutCallsHQFailCC1NormalCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCC1NormalCause.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCC1UserBusy_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCC1UserBusy_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCC1UserBusy = _OacVoiceDialPeerOutCallsHQFailCC1UserBusy_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 14),
    _OacVoiceDialPeerOutCallsHQFailCC1UserBusy_Type()
)
oacVoiceDialPeerOutCallsHQFailCC1UserBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCC1UserBusy.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCC1NoAnswer_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCC1NoAnswer_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCC1NoAnswer = _OacVoiceDialPeerOutCallsHQFailCC1NoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 15),
    _OacVoiceDialPeerOutCallsHQFailCC1NoAnswer_Type()
)
oacVoiceDialPeerOutCallsHQFailCC1NoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCC1NoAnswer.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCauseClass2_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCauseClass2_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCauseClass2 = _OacVoiceDialPeerOutCallsHQFailCauseClass2_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 16),
    _OacVoiceDialPeerOutCallsHQFailCauseClass2_Type()
)
oacVoiceDialPeerOutCallsHQFailCauseClass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCauseClass2.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCauseClass3_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCauseClass3_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCauseClass3 = _OacVoiceDialPeerOutCallsHQFailCauseClass3_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 17),
    _OacVoiceDialPeerOutCallsHQFailCauseClass3_Type()
)
oacVoiceDialPeerOutCallsHQFailCauseClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCauseClass3.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCauseClass4_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCauseClass4_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCauseClass4 = _OacVoiceDialPeerOutCallsHQFailCauseClass4_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 18),
    _OacVoiceDialPeerOutCallsHQFailCauseClass4_Type()
)
oacVoiceDialPeerOutCallsHQFailCauseClass4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCauseClass4.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCauseClass5_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCauseClass5_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCauseClass5 = _OacVoiceDialPeerOutCallsHQFailCauseClass5_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 19),
    _OacVoiceDialPeerOutCallsHQFailCauseClass5_Type()
)
oacVoiceDialPeerOutCallsHQFailCauseClass5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCauseClass5.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCauseClass6_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCauseClass6_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCauseClass6 = _OacVoiceDialPeerOutCallsHQFailCauseClass6_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 20),
    _OacVoiceDialPeerOutCallsHQFailCauseClass6_Type()
)
oacVoiceDialPeerOutCallsHQFailCauseClass6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCauseClass6.setStatus("current")
_OacVoiceDialPeerOutCallsHQFailCauseClass7_Type = Integer32
_OacVoiceDialPeerOutCallsHQFailCauseClass7_Object = MibTableColumn
oacVoiceDialPeerOutCallsHQFailCauseClass7 = _OacVoiceDialPeerOutCallsHQFailCauseClass7_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 21),
    _OacVoiceDialPeerOutCallsHQFailCauseClass7_Type()
)
oacVoiceDialPeerOutCallsHQFailCauseClass7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsHQFailCauseClass7.setStatus("current")
_OacVoiceDialPeerOutCallsH245Failures_Type = Integer32
_OacVoiceDialPeerOutCallsH245Failures_Object = MibTableColumn
oacVoiceDialPeerOutCallsH245Failures = _OacVoiceDialPeerOutCallsH245Failures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 22),
    _OacVoiceDialPeerOutCallsH245Failures_Type()
)
oacVoiceDialPeerOutCallsH245Failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsH245Failures.setStatus("current")
_OacVoiceDialPeerOutCallsH245FailIncompatibleCapabilities_Type = Integer32
_OacVoiceDialPeerOutCallsH245FailIncompatibleCapabilities_Object = MibTableColumn
oacVoiceDialPeerOutCallsH245FailIncompatibleCapabilities = _OacVoiceDialPeerOutCallsH245FailIncompatibleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 23),
    _OacVoiceDialPeerOutCallsH245FailIncompatibleCapabilities_Type()
)
oacVoiceDialPeerOutCallsH245FailIncompatibleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsH245FailIncompatibleCapabilities.setStatus("current")
_OacVoiceDialPeerOutCallsH245FailProtocolErrors_Type = Integer32
_OacVoiceDialPeerOutCallsH245FailProtocolErrors_Object = MibTableColumn
oacVoiceDialPeerOutCallsH245FailProtocolErrors = _OacVoiceDialPeerOutCallsH245FailProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 24),
    _OacVoiceDialPeerOutCallsH245FailProtocolErrors_Type()
)
oacVoiceDialPeerOutCallsH245FailProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsH245FailProtocolErrors.setStatus("current")
_OacVoiceDialPeerOutCallsInternalFailures_Type = Integer32
_OacVoiceDialPeerOutCallsInternalFailures_Object = MibTableColumn
oacVoiceDialPeerOutCallsInternalFailures = _OacVoiceDialPeerOutCallsInternalFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 25),
    _OacVoiceDialPeerOutCallsInternalFailures_Type()
)
oacVoiceDialPeerOutCallsInternalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsInternalFailures.setStatus("current")
_OacVoiceDialPeerOutCallsInternalFailDspUnavailable_Type = Integer32
_OacVoiceDialPeerOutCallsInternalFailDspUnavailable_Object = MibTableColumn
oacVoiceDialPeerOutCallsInternalFailDspUnavailable = _OacVoiceDialPeerOutCallsInternalFailDspUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 26),
    _OacVoiceDialPeerOutCallsInternalFailDspUnavailable_Type()
)
oacVoiceDialPeerOutCallsInternalFailDspUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsInternalFailDspUnavailable.setStatus("current")
_OacVoiceDialPeerOutCallsInternalFailMaxBwExceeded_Type = Integer32
_OacVoiceDialPeerOutCallsInternalFailMaxBwExceeded_Object = MibTableColumn
oacVoiceDialPeerOutCallsInternalFailMaxBwExceeded = _OacVoiceDialPeerOutCallsInternalFailMaxBwExceeded_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 27),
    _OacVoiceDialPeerOutCallsInternalFailMaxBwExceeded_Type()
)
oacVoiceDialPeerOutCallsInternalFailMaxBwExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsInternalFailMaxBwExceeded.setStatus("current")
_OacVoiceDialPeerOutCallsInternalFailMaxConnExceeded_Type = Integer32
_OacVoiceDialPeerOutCallsInternalFailMaxConnExceeded_Object = MibTableColumn
oacVoiceDialPeerOutCallsInternalFailMaxConnExceeded = _OacVoiceDialPeerOutCallsInternalFailMaxConnExceeded_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 28),
    _OacVoiceDialPeerOutCallsInternalFailMaxConnExceeded_Type()
)
oacVoiceDialPeerOutCallsInternalFailMaxConnExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsInternalFailMaxConnExceeded.setStatus("current")
_OacVoiceDialPeerOutCallsInternalFailNotSpecified_Type = Integer32
_OacVoiceDialPeerOutCallsInternalFailNotSpecified_Object = MibTableColumn
oacVoiceDialPeerOutCallsInternalFailNotSpecified = _OacVoiceDialPeerOutCallsInternalFailNotSpecified_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 29),
    _OacVoiceDialPeerOutCallsInternalFailNotSpecified_Type()
)
oacVoiceDialPeerOutCallsInternalFailNotSpecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerOutCallsInternalFailNotSpecified.setStatus("current")
_OacVoiceDialPeerIncCalls_Type = Integer32
_OacVoiceDialPeerIncCalls_Object = MibTableColumn
oacVoiceDialPeerIncCalls = _OacVoiceDialPeerIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 30),
    _OacVoiceDialPeerIncCalls_Type()
)
oacVoiceDialPeerIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCalls.setStatus("current")
_OacVoiceDialPeerIncCallsMgcpRingingEvents_Type = Integer32
_OacVoiceDialPeerIncCallsMgcpRingingEvents_Object = MibTableColumn
oacVoiceDialPeerIncCallsMgcpRingingEvents = _OacVoiceDialPeerIncCallsMgcpRingingEvents_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 31),
    _OacVoiceDialPeerIncCallsMgcpRingingEvents_Type()
)
oacVoiceDialPeerIncCallsMgcpRingingEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsMgcpRingingEvents.setStatus("current")
_OacVoiceDialPeerIncCallsMgcpPathEstablished_Type = Integer32
_OacVoiceDialPeerIncCallsMgcpPathEstablished_Object = MibTableColumn
oacVoiceDialPeerIncCallsMgcpPathEstablished = _OacVoiceDialPeerIncCallsMgcpPathEstablished_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 32),
    _OacVoiceDialPeerIncCallsMgcpPathEstablished_Type()
)
oacVoiceDialPeerIncCallsMgcpPathEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsMgcpPathEstablished.setStatus("current")
_OacVoiceDialPeerIncCallsFailures_Type = Integer32
_OacVoiceDialPeerIncCallsFailures_Object = MibTableColumn
oacVoiceDialPeerIncCallsFailures = _OacVoiceDialPeerIncCallsFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 33),
    _OacVoiceDialPeerIncCallsFailures_Type()
)
oacVoiceDialPeerIncCallsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsFailures.setStatus("current")
_OacVoiceDialPeerIncCallsRasFailures_Type = Integer32
_OacVoiceDialPeerIncCallsRasFailures_Object = MibTableColumn
oacVoiceDialPeerIncCallsRasFailures = _OacVoiceDialPeerIncCallsRasFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 34),
    _OacVoiceDialPeerIncCallsRasFailures_Type()
)
oacVoiceDialPeerIncCallsRasFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsRasFailures.setStatus("current")
_OacVoiceDialPeerIncCallsRasFailGatekeeperUnavailable_Type = Integer32
_OacVoiceDialPeerIncCallsRasFailGatekeeperUnavailable_Object = MibTableColumn
oacVoiceDialPeerIncCallsRasFailGatekeeperUnavailable = _OacVoiceDialPeerIncCallsRasFailGatekeeperUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 35),
    _OacVoiceDialPeerIncCallsRasFailGatekeeperUnavailable_Type()
)
oacVoiceDialPeerIncCallsRasFailGatekeeperUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsRasFailGatekeeperUnavailable.setStatus("current")
_OacVoiceDialPeerIncCallsRasFailAdmissionRejects_Type = Integer32
_OacVoiceDialPeerIncCallsRasFailAdmissionRejects_Object = MibTableColumn
oacVoiceDialPeerIncCallsRasFailAdmissionRejects = _OacVoiceDialPeerIncCallsRasFailAdmissionRejects_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 36),
    _OacVoiceDialPeerIncCallsRasFailAdmissionRejects_Type()
)
oacVoiceDialPeerIncCallsRasFailAdmissionRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsRasFailAdmissionRejects.setStatus("current")
_OacVoiceDialPeerIncCallsLocalPortFailures_Type = Integer32
_OacVoiceDialPeerIncCallsLocalPortFailures_Object = MibTableColumn
oacVoiceDialPeerIncCallsLocalPortFailures = _OacVoiceDialPeerIncCallsLocalPortFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 37),
    _OacVoiceDialPeerIncCallsLocalPortFailures_Type()
)
oacVoiceDialPeerIncCallsLocalPortFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsLocalPortFailures.setStatus("current")
_OacVoiceDialPeerIncCallsH245Failures_Type = Integer32
_OacVoiceDialPeerIncCallsH245Failures_Object = MibTableColumn
oacVoiceDialPeerIncCallsH245Failures = _OacVoiceDialPeerIncCallsH245Failures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 38),
    _OacVoiceDialPeerIncCallsH245Failures_Type()
)
oacVoiceDialPeerIncCallsH245Failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsH245Failures.setStatus("current")
_OacVoiceDialPeerIncCallsH245FailIncompatibleCapabilities_Type = Integer32
_OacVoiceDialPeerIncCallsH245FailIncompatibleCapabilities_Object = MibTableColumn
oacVoiceDialPeerIncCallsH245FailIncompatibleCapabilities = _OacVoiceDialPeerIncCallsH245FailIncompatibleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 39),
    _OacVoiceDialPeerIncCallsH245FailIncompatibleCapabilities_Type()
)
oacVoiceDialPeerIncCallsH245FailIncompatibleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsH245FailIncompatibleCapabilities.setStatus("current")
_OacVoiceDialPeerIncCallsH245FailProtocolErrors_Type = Integer32
_OacVoiceDialPeerIncCallsH245FailProtocolErrors_Object = MibTableColumn
oacVoiceDialPeerIncCallsH245FailProtocolErrors = _OacVoiceDialPeerIncCallsH245FailProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 40),
    _OacVoiceDialPeerIncCallsH245FailProtocolErrors_Type()
)
oacVoiceDialPeerIncCallsH245FailProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsH245FailProtocolErrors.setStatus("current")
_OacVoiceDialPeerIncCallsInternalFailures_Type = Integer32
_OacVoiceDialPeerIncCallsInternalFailures_Object = MibTableColumn
oacVoiceDialPeerIncCallsInternalFailures = _OacVoiceDialPeerIncCallsInternalFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 41),
    _OacVoiceDialPeerIncCallsInternalFailures_Type()
)
oacVoiceDialPeerIncCallsInternalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsInternalFailures.setStatus("current")
_OacVoiceDialPeerIncCallsInternalFailDspUnavailable_Type = Integer32
_OacVoiceDialPeerIncCallsInternalFailDspUnavailable_Object = MibTableColumn
oacVoiceDialPeerIncCallsInternalFailDspUnavailable = _OacVoiceDialPeerIncCallsInternalFailDspUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 42),
    _OacVoiceDialPeerIncCallsInternalFailDspUnavailable_Type()
)
oacVoiceDialPeerIncCallsInternalFailDspUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsInternalFailDspUnavailable.setStatus("current")
_OacVoiceDialPeerIncCallsInternalFailUnknownNumber_Type = Integer32
_OacVoiceDialPeerIncCallsInternalFailUnknownNumber_Object = MibTableColumn
oacVoiceDialPeerIncCallsInternalFailUnknownNumber = _OacVoiceDialPeerIncCallsInternalFailUnknownNumber_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 43),
    _OacVoiceDialPeerIncCallsInternalFailUnknownNumber_Type()
)
oacVoiceDialPeerIncCallsInternalFailUnknownNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsInternalFailUnknownNumber.setStatus("current")
_OacVoiceDialPeerIncCallsInternalFailChannelPortUnavailable_Type = Integer32
_OacVoiceDialPeerIncCallsInternalFailChannelPortUnavailable_Object = MibTableColumn
oacVoiceDialPeerIncCallsInternalFailChannelPortUnavailable = _OacVoiceDialPeerIncCallsInternalFailChannelPortUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 44),
    _OacVoiceDialPeerIncCallsInternalFailChannelPortUnavailable_Type()
)
oacVoiceDialPeerIncCallsInternalFailChannelPortUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsInternalFailChannelPortUnavailable.setStatus("current")
_OacVoiceDialPeerIncCallsInternalFailMaxBwExceeded_Type = Integer32
_OacVoiceDialPeerIncCallsInternalFailMaxBwExceeded_Object = MibTableColumn
oacVoiceDialPeerIncCallsInternalFailMaxBwExceeded = _OacVoiceDialPeerIncCallsInternalFailMaxBwExceeded_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 45),
    _OacVoiceDialPeerIncCallsInternalFailMaxBwExceeded_Type()
)
oacVoiceDialPeerIncCallsInternalFailMaxBwExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsInternalFailMaxBwExceeded.setStatus("current")
_OacVoiceDialPeerIncCallsInternalFailMaxConnExceeded_Type = Integer32
_OacVoiceDialPeerIncCallsInternalFailMaxConnExceeded_Object = MibTableColumn
oacVoiceDialPeerIncCallsInternalFailMaxConnExceeded = _OacVoiceDialPeerIncCallsInternalFailMaxConnExceeded_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 46),
    _OacVoiceDialPeerIncCallsInternalFailMaxConnExceeded_Type()
)
oacVoiceDialPeerIncCallsInternalFailMaxConnExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsInternalFailMaxConnExceeded.setStatus("current")
_OacVoiceDialPeerIncCallsInternalFailNotSpecified_Type = Integer32
_OacVoiceDialPeerIncCallsInternalFailNotSpecified_Object = MibTableColumn
oacVoiceDialPeerIncCallsInternalFailNotSpecified = _OacVoiceDialPeerIncCallsInternalFailNotSpecified_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 47),
    _OacVoiceDialPeerIncCallsInternalFailNotSpecified_Type()
)
oacVoiceDialPeerIncCallsInternalFailNotSpecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsInternalFailNotSpecified.setStatus("current")
_OacVoiceDialPeerIncCallsAdviceofCharge_Type = Integer32
_OacVoiceDialPeerIncCallsAdviceofCharge_Object = MibTableColumn
oacVoiceDialPeerIncCallsAdviceofCharge = _OacVoiceDialPeerIncCallsAdviceofCharge_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 48),
    _OacVoiceDialPeerIncCallsAdviceofCharge_Type()
)
oacVoiceDialPeerIncCallsAdviceofCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerIncCallsAdviceofCharge.setStatus("current")
_OacVoiceDialPeerRtpStatNbTxPackets_Type = Unsigned32
_OacVoiceDialPeerRtpStatNbTxPackets_Object = MibTableColumn
oacVoiceDialPeerRtpStatNbTxPackets = _OacVoiceDialPeerRtpStatNbTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 49),
    _OacVoiceDialPeerRtpStatNbTxPackets_Type()
)
oacVoiceDialPeerRtpStatNbTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerRtpStatNbTxPackets.setStatus("current")
_OacVoiceDialPeerRtpStatNbRxPackets_Type = Unsigned32
_OacVoiceDialPeerRtpStatNbRxPackets_Object = MibTableColumn
oacVoiceDialPeerRtpStatNbRxPackets = _OacVoiceDialPeerRtpStatNbRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 50),
    _OacVoiceDialPeerRtpStatNbRxPackets_Type()
)
oacVoiceDialPeerRtpStatNbRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerRtpStatNbRxPackets.setStatus("current")
_OacVoiceDialPeerRtpStatNbTxBytes_Type = Unsigned32
_OacVoiceDialPeerRtpStatNbTxBytes_Object = MibTableColumn
oacVoiceDialPeerRtpStatNbTxBytes = _OacVoiceDialPeerRtpStatNbTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 51),
    _OacVoiceDialPeerRtpStatNbTxBytes_Type()
)
oacVoiceDialPeerRtpStatNbTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerRtpStatNbTxBytes.setStatus("current")
_OacVoiceDialPeerRtpStatNbRxBytes_Type = Unsigned32
_OacVoiceDialPeerRtpStatNbRxBytes_Object = MibTableColumn
oacVoiceDialPeerRtpStatNbRxBytes = _OacVoiceDialPeerRtpStatNbRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 52),
    _OacVoiceDialPeerRtpStatNbRxBytes_Type()
)
oacVoiceDialPeerRtpStatNbRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerRtpStatNbRxBytes.setStatus("current")
_OacVoiceDialPeerRtpStatNbExcessiveJitterEvents_Type = Unsigned32
_OacVoiceDialPeerRtpStatNbExcessiveJitterEvents_Object = MibTableColumn
oacVoiceDialPeerRtpStatNbExcessiveJitterEvents = _OacVoiceDialPeerRtpStatNbExcessiveJitterEvents_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 53),
    _OacVoiceDialPeerRtpStatNbExcessiveJitterEvents_Type()
)
oacVoiceDialPeerRtpStatNbExcessiveJitterEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerRtpStatNbExcessiveJitterEvents.setStatus("current")
_OacVoiceDialPeerRtpStatNbLostPackets_Type = Unsigned32
_OacVoiceDialPeerRtpStatNbLostPackets_Object = MibTableColumn
oacVoiceDialPeerRtpStatNbLostPackets = _OacVoiceDialPeerRtpStatNbLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 54),
    _OacVoiceDialPeerRtpStatNbLostPackets_Type()
)
oacVoiceDialPeerRtpStatNbLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerRtpStatNbLostPackets.setStatus("current")
_OacVoiceDialPeerRtpStatNbInvalidPackets_Type = Unsigned32
_OacVoiceDialPeerRtpStatNbInvalidPackets_Object = MibTableColumn
oacVoiceDialPeerRtpStatNbInvalidPackets = _OacVoiceDialPeerRtpStatNbInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 55),
    _OacVoiceDialPeerRtpStatNbInvalidPackets_Type()
)
oacVoiceDialPeerRtpStatNbInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerRtpStatNbInvalidPackets.setStatus("current")
_OacVoiceDialPeerModemNbSwitchingToModemMode_Type = Unsigned32
_OacVoiceDialPeerModemNbSwitchingToModemMode_Object = MibTableColumn
oacVoiceDialPeerModemNbSwitchingToModemMode = _OacVoiceDialPeerModemNbSwitchingToModemMode_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 56),
    _OacVoiceDialPeerModemNbSwitchingToModemMode_Type()
)
oacVoiceDialPeerModemNbSwitchingToModemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerModemNbSwitchingToModemMode.setStatus("current")
_OacVoiceDialPeerFaxNbOutgoingFax_Type = Integer32
_OacVoiceDialPeerFaxNbOutgoingFax_Object = MibTableColumn
oacVoiceDialPeerFaxNbOutgoingFax = _OacVoiceDialPeerFaxNbOutgoingFax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 57),
    _OacVoiceDialPeerFaxNbOutgoingFax_Type()
)
oacVoiceDialPeerFaxNbOutgoingFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxNbOutgoingFax.setStatus("current")
_OacVoiceDialPeerFaxNbIncomingFax_Type = Integer32
_OacVoiceDialPeerFaxNbIncomingFax_Object = MibTableColumn
oacVoiceDialPeerFaxNbIncomingFax = _OacVoiceDialPeerFaxNbIncomingFax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 58),
    _OacVoiceDialPeerFaxNbIncomingFax_Type()
)
oacVoiceDialPeerFaxNbIncomingFax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxNbIncomingFax.setStatus("current")
_OacVoiceDialPeerFaxNbFailures_Type = Integer32
_OacVoiceDialPeerFaxNbFailures_Object = MibTableColumn
oacVoiceDialPeerFaxNbFailures = _OacVoiceDialPeerFaxNbFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 59),
    _OacVoiceDialPeerFaxNbFailures_Type()
)
oacVoiceDialPeerFaxNbFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxNbFailures.setStatus("current")
_OacVoiceDialPeerFaxFailureRequestMode_Type = Integer32
_OacVoiceDialPeerFaxFailureRequestMode_Object = MibTableColumn
oacVoiceDialPeerFaxFailureRequestMode = _OacVoiceDialPeerFaxFailureRequestMode_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 60),
    _OacVoiceDialPeerFaxFailureRequestMode_Type()
)
oacVoiceDialPeerFaxFailureRequestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxFailureRequestMode.setStatus("current")
_OacVoiceDialPeerFaxFailurePreMsgProcedure_Type = Integer32
_OacVoiceDialPeerFaxFailurePreMsgProcedure_Object = MibTableColumn
oacVoiceDialPeerFaxFailurePreMsgProcedure = _OacVoiceDialPeerFaxFailurePreMsgProcedure_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 61),
    _OacVoiceDialPeerFaxFailurePreMsgProcedure_Type()
)
oacVoiceDialPeerFaxFailurePreMsgProcedure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxFailurePreMsgProcedure.setStatus("current")
_OacVoiceDialPeerFaxFailurePage_Type = Integer32
_OacVoiceDialPeerFaxFailurePage_Object = MibTableColumn
oacVoiceDialPeerFaxFailurePage = _OacVoiceDialPeerFaxFailurePage_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 62),
    _OacVoiceDialPeerFaxFailurePage_Type()
)
oacVoiceDialPeerFaxFailurePage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxFailurePage.setStatus("current")
_OacVoiceDialPeerFaxNbTxPackets_Type = Unsigned32
_OacVoiceDialPeerFaxNbTxPackets_Object = MibTableColumn
oacVoiceDialPeerFaxNbTxPackets = _OacVoiceDialPeerFaxNbTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 63),
    _OacVoiceDialPeerFaxNbTxPackets_Type()
)
oacVoiceDialPeerFaxNbTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxNbTxPackets.setStatus("current")
_OacVoiceDialPeerFaxNbRxPackets_Type = Unsigned32
_OacVoiceDialPeerFaxNbRxPackets_Object = MibTableColumn
oacVoiceDialPeerFaxNbRxPackets = _OacVoiceDialPeerFaxNbRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 64),
    _OacVoiceDialPeerFaxNbRxPackets_Type()
)
oacVoiceDialPeerFaxNbRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxNbRxPackets.setStatus("current")
_OacVoiceDialPeerFaxNbTxBytes_Type = Unsigned32
_OacVoiceDialPeerFaxNbTxBytes_Object = MibTableColumn
oacVoiceDialPeerFaxNbTxBytes = _OacVoiceDialPeerFaxNbTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 65),
    _OacVoiceDialPeerFaxNbTxBytes_Type()
)
oacVoiceDialPeerFaxNbTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxNbTxBytes.setStatus("current")
_OacVoiceDialPeerFaxNbRxBytes_Type = Unsigned32
_OacVoiceDialPeerFaxNbRxBytes_Object = MibTableColumn
oacVoiceDialPeerFaxNbRxBytes = _OacVoiceDialPeerFaxNbRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 66),
    _OacVoiceDialPeerFaxNbRxBytes_Type()
)
oacVoiceDialPeerFaxNbRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxNbRxBytes.setStatus("current")
_OacVoiceDialPeerFaxNbLostPackets_Type = Unsigned32
_OacVoiceDialPeerFaxNbLostPackets_Object = MibTableColumn
oacVoiceDialPeerFaxNbLostPackets = _OacVoiceDialPeerFaxNbLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 2, 1, 67),
    _OacVoiceDialPeerFaxNbLostPackets_Type()
)
oacVoiceDialPeerFaxNbLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceDialPeerFaxNbLostPackets.setStatus("current")
_OacVoiceH323Gw_ObjectIdentity = ObjectIdentity
oacVoiceH323Gw = _OacVoiceH323Gw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3)
)
_OacVoiceH323GwState_Type = OacVoipGatewayState
_OacVoiceH323GwState_Object = MibScalar
oacVoiceH323GwState = _OacVoiceH323GwState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 1),
    _OacVoiceH323GwState_Type()
)
oacVoiceH323GwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwState.setStatus("current")
_OacVoiceH323GwStateReason_Type = OacVoipGatewayStateReason
_OacVoiceH323GwStateReason_Object = MibScalar
oacVoiceH323GwStateReason = _OacVoiceH323GwStateReason_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 2),
    _OacVoiceH323GwStateReason_Type()
)
oacVoiceH323GwStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwStateReason.setStatus("current")
_OacVoiceH323GwRasBwControl_Type = OacH323GwRasBwControl
_OacVoiceH323GwRasBwControl_Object = MibScalar
oacVoiceH323GwRasBwControl = _OacVoiceH323GwRasBwControl_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 3),
    _OacVoiceH323GwRasBwControl_Type()
)
oacVoiceH323GwRasBwControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRasBwControl.setStatus("current")
_OacVoiceH323GwPortabilityStatus_Type = OacH323GwPortabilityStatus
_OacVoiceH323GwPortabilityStatus_Object = MibScalar
oacVoiceH323GwPortabilityStatus = _OacVoiceH323GwPortabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 4),
    _OacVoiceH323GwPortabilityStatus_Type()
)
oacVoiceH323GwPortabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwPortabilityStatus.setStatus("current")
_OacVoiceH323GwPortabilityStatusTimeout_Type = Integer32
_OacVoiceH323GwPortabilityStatusTimeout_Object = MibScalar
oacVoiceH323GwPortabilityStatusTimeout = _OacVoiceH323GwPortabilityStatusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 5),
    _OacVoiceH323GwPortabilityStatusTimeout_Type()
)
oacVoiceH323GwPortabilityStatusTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwPortabilityStatusTimeout.setStatus("current")
_OacVoiceH323GwDs0Configured_Type = Integer32
_OacVoiceH323GwDs0Configured_Object = MibScalar
oacVoiceH323GwDs0Configured = _OacVoiceH323GwDs0Configured_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 6),
    _OacVoiceH323GwDs0Configured_Type()
)
oacVoiceH323GwDs0Configured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwDs0Configured.setStatus("current")
_OacVoiceH323GwDs0Low_Type = Integer32
_OacVoiceH323GwDs0Low_Object = MibScalar
oacVoiceH323GwDs0Low = _OacVoiceH323GwDs0Low_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 7),
    _OacVoiceH323GwDs0Low_Type()
)
oacVoiceH323GwDs0Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwDs0Low.setStatus("current")
_OacVoiceH323GwDs0High_Type = Integer32
_OacVoiceH323GwDs0High_Object = MibScalar
oacVoiceH323GwDs0High = _OacVoiceH323GwDs0High_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 8),
    _OacVoiceH323GwDs0High_Type()
)
oacVoiceH323GwDs0High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwDs0High.setStatus("current")
_OacVoiceH323GwDs0Current_Type = Integer32
_OacVoiceH323GwDs0Current_Object = MibScalar
oacVoiceH323GwDs0Current = _OacVoiceH323GwDs0Current_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 9),
    _OacVoiceH323GwDs0Current_Type()
)
oacVoiceH323GwDs0Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwDs0Current.setStatus("current")
_OacVoiceH323GwBwConfigured_Type = Integer32
_OacVoiceH323GwBwConfigured_Object = MibScalar
oacVoiceH323GwBwConfigured = _OacVoiceH323GwBwConfigured_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 10),
    _OacVoiceH323GwBwConfigured_Type()
)
oacVoiceH323GwBwConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwBwConfigured.setStatus("current")
_OacVoiceH323GwBwLow_Type = Integer32
_OacVoiceH323GwBwLow_Object = MibScalar
oacVoiceH323GwBwLow = _OacVoiceH323GwBwLow_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 11),
    _OacVoiceH323GwBwLow_Type()
)
oacVoiceH323GwBwLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwBwLow.setStatus("current")
_OacVoiceH323GwBwHigh_Type = Integer32
_OacVoiceH323GwBwHigh_Object = MibScalar
oacVoiceH323GwBwHigh = _OacVoiceH323GwBwHigh_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 12),
    _OacVoiceH323GwBwHigh_Type()
)
oacVoiceH323GwBwHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwBwHigh.setStatus("current")
_OacVoiceH323GwBwCurrent_Type = Integer32
_OacVoiceH323GwBwCurrent_Object = MibScalar
oacVoiceH323GwBwCurrent = _OacVoiceH323GwBwCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 13),
    _OacVoiceH323GwBwCurrent_Type()
)
oacVoiceH323GwBwCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwBwCurrent.setStatus("current")
_OacVoiceH323GwRegistrationState_Type = OacVoipGatewayRegistrationState
_OacVoiceH323GwRegistrationState_Object = MibScalar
oacVoiceH323GwRegistrationState = _OacVoiceH323GwRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 14),
    _OacVoiceH323GwRegistrationState_Type()
)
oacVoiceH323GwRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegistrationState.setStatus("current")


class _OacVoiceH323GwGatekeeperIdentifier_Type(DisplayString):
    """Custom type oacVoiceH323GwGatekeeperIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_OacVoiceH323GwGatekeeperIdentifier_Type.__name__ = "DisplayString"
_OacVoiceH323GwGatekeeperIdentifier_Object = MibScalar
oacVoiceH323GwGatekeeperIdentifier = _OacVoiceH323GwGatekeeperIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 15),
    _OacVoiceH323GwGatekeeperIdentifier_Type()
)
oacVoiceH323GwGatekeeperIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwGatekeeperIdentifier.setStatus("current")


class _OacVoiceH323GwGatekeeperAddress_Type(DisplayString):
    """Custom type oacVoiceH323GwGatekeeperAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OacVoiceH323GwGatekeeperAddress_Type.__name__ = "DisplayString"
_OacVoiceH323GwGatekeeperAddress_Object = MibScalar
oacVoiceH323GwGatekeeperAddress = _OacVoiceH323GwGatekeeperAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 16),
    _OacVoiceH323GwGatekeeperAddress_Type()
)
oacVoiceH323GwGatekeeperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwGatekeeperAddress.setStatus("current")
_OacVoiceH323GwRegistrationRequest_Type = Integer32
_OacVoiceH323GwRegistrationRequest_Object = MibScalar
oacVoiceH323GwRegistrationRequest = _OacVoiceH323GwRegistrationRequest_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 17),
    _OacVoiceH323GwRegistrationRequest_Type()
)
oacVoiceH323GwRegistrationRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegistrationRequest.setStatus("current")
_OacVoiceH323GwRegistrationFailures_Type = Integer32
_OacVoiceH323GwRegistrationFailures_Object = MibScalar
oacVoiceH323GwRegistrationFailures = _OacVoiceH323GwRegistrationFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 18),
    _OacVoiceH323GwRegistrationFailures_Type()
)
oacVoiceH323GwRegistrationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegistrationFailures.setStatus("current")
_OacVoiceH323GwRegFailNoResponse_Type = Integer32
_OacVoiceH323GwRegFailNoResponse_Object = MibScalar
oacVoiceH323GwRegFailNoResponse = _OacVoiceH323GwRegFailNoResponse_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 19),
    _OacVoiceH323GwRegFailNoResponse_Type()
)
oacVoiceH323GwRegFailNoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegFailNoResponse.setStatus("current")
_OacVoiceH323GwRegFailInvalidIpAddress_Type = Integer32
_OacVoiceH323GwRegFailInvalidIpAddress_Object = MibScalar
oacVoiceH323GwRegFailInvalidIpAddress = _OacVoiceH323GwRegFailInvalidIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 20),
    _OacVoiceH323GwRegFailInvalidIpAddress_Type()
)
oacVoiceH323GwRegFailInvalidIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegFailInvalidIpAddress.setStatus("current")
_OacVoiceH323GwRegFailDuplicateAlias_Type = Integer32
_OacVoiceH323GwRegFailDuplicateAlias_Object = MibScalar
oacVoiceH323GwRegFailDuplicateAlias = _OacVoiceH323GwRegFailDuplicateAlias_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 21),
    _OacVoiceH323GwRegFailDuplicateAlias_Type()
)
oacVoiceH323GwRegFailDuplicateAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegFailDuplicateAlias.setStatus("current")
_OacVoiceH323GwRegFailInvalidTerminalType_Type = Integer32
_OacVoiceH323GwRegFailInvalidTerminalType_Object = MibScalar
oacVoiceH323GwRegFailInvalidTerminalType = _OacVoiceH323GwRegFailInvalidTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 22),
    _OacVoiceH323GwRegFailInvalidTerminalType_Type()
)
oacVoiceH323GwRegFailInvalidTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegFailInvalidTerminalType.setStatus("current")
_OacVoiceH323GwRegFailResourceUnavailable_Type = Integer32
_OacVoiceH323GwRegFailResourceUnavailable_Object = MibScalar
oacVoiceH323GwRegFailResourceUnavailable = _OacVoiceH323GwRegFailResourceUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 23),
    _OacVoiceH323GwRegFailResourceUnavailable_Type()
)
oacVoiceH323GwRegFailResourceUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegFailResourceUnavailable.setStatus("current")
_OacVoiceH323GwRegFailInvalidAlias_Type = Integer32
_OacVoiceH323GwRegFailInvalidAlias_Object = MibScalar
oacVoiceH323GwRegFailInvalidAlias = _OacVoiceH323GwRegFailInvalidAlias_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 24),
    _OacVoiceH323GwRegFailInvalidAlias_Type()
)
oacVoiceH323GwRegFailInvalidAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegFailInvalidAlias.setStatus("current")
_OacVoiceH323GwRegFailSecurityDenial_Type = Integer32
_OacVoiceH323GwRegFailSecurityDenial_Object = MibScalar
oacVoiceH323GwRegFailSecurityDenial = _OacVoiceH323GwRegFailSecurityDenial_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 25),
    _OacVoiceH323GwRegFailSecurityDenial_Type()
)
oacVoiceH323GwRegFailSecurityDenial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegFailSecurityDenial.setStatus("current")
_OacVoiceH323GwRegFailUndefinedReason_Type = Integer32
_OacVoiceH323GwRegFailUndefinedReason_Object = MibScalar
oacVoiceH323GwRegFailUndefinedReason = _OacVoiceH323GwRegFailUndefinedReason_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 26),
    _OacVoiceH323GwRegFailUndefinedReason_Type()
)
oacVoiceH323GwRegFailUndefinedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwRegFailUndefinedReason.setStatus("current")
_OacVoiceH323GwAdmissionRequests_Type = Integer32
_OacVoiceH323GwAdmissionRequests_Object = MibScalar
oacVoiceH323GwAdmissionRequests = _OacVoiceH323GwAdmissionRequests_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 27),
    _OacVoiceH323GwAdmissionRequests_Type()
)
oacVoiceH323GwAdmissionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmissionRequests.setStatus("current")
_OacVoiceH323GwAdmissionRejects_Type = Integer32
_OacVoiceH323GwAdmissionRejects_Object = MibScalar
oacVoiceH323GwAdmissionRejects = _OacVoiceH323GwAdmissionRejects_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 28),
    _OacVoiceH323GwAdmissionRejects_Type()
)
oacVoiceH323GwAdmissionRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmissionRejects.setStatus("current")
_OacVoiceH323GwAdmRejCalledPartyNotRegistered_Type = Integer32
_OacVoiceH323GwAdmRejCalledPartyNotRegistered_Object = MibScalar
oacVoiceH323GwAdmRejCalledPartyNotRegistered = _OacVoiceH323GwAdmRejCalledPartyNotRegistered_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 29),
    _OacVoiceH323GwAdmRejCalledPartyNotRegistered_Type()
)
oacVoiceH323GwAdmRejCalledPartyNotRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmRejCalledPartyNotRegistered.setStatus("current")
_OacVoiceH323GwAdmRejInvalidPermission_Type = Integer32
_OacVoiceH323GwAdmRejInvalidPermission_Object = MibScalar
oacVoiceH323GwAdmRejInvalidPermission = _OacVoiceH323GwAdmRejInvalidPermission_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 30),
    _OacVoiceH323GwAdmRejInvalidPermission_Type()
)
oacVoiceH323GwAdmRejInvalidPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmRejInvalidPermission.setStatus("current")
_OacVoiceH323GwAdmRejRequestDenied_Type = Integer32
_OacVoiceH323GwAdmRejRequestDenied_Object = MibScalar
oacVoiceH323GwAdmRejRequestDenied = _OacVoiceH323GwAdmRejRequestDenied_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 31),
    _OacVoiceH323GwAdmRejRequestDenied_Type()
)
oacVoiceH323GwAdmRejRequestDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmRejRequestDenied.setStatus("current")
_OacVoiceH323GwAdmRejCallerNotRegistered_Type = Integer32
_OacVoiceH323GwAdmRejCallerNotRegistered_Object = MibScalar
oacVoiceH323GwAdmRejCallerNotRegistered = _OacVoiceH323GwAdmRejCallerNotRegistered_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 32),
    _OacVoiceH323GwAdmRejCallerNotRegistered_Type()
)
oacVoiceH323GwAdmRejCallerNotRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmRejCallerNotRegistered.setStatus("current")
_OacVoiceH323GwAdmRejResourceUnavailable_Type = Integer32
_OacVoiceH323GwAdmRejResourceUnavailable_Object = MibScalar
oacVoiceH323GwAdmRejResourceUnavailable = _OacVoiceH323GwAdmRejResourceUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 33),
    _OacVoiceH323GwAdmRejResourceUnavailable_Type()
)
oacVoiceH323GwAdmRejResourceUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmRejResourceUnavailable.setStatus("current")
_OacVoiceH323GwAdmRejSecurityDenial_Type = Integer32
_OacVoiceH323GwAdmRejSecurityDenial_Object = MibScalar
oacVoiceH323GwAdmRejSecurityDenial = _OacVoiceH323GwAdmRejSecurityDenial_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 34),
    _OacVoiceH323GwAdmRejSecurityDenial_Type()
)
oacVoiceH323GwAdmRejSecurityDenial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmRejSecurityDenial.setStatus("current")
_OacVoiceH323GwAdmRejInvalidEndpointIdent_Type = Integer32
_OacVoiceH323GwAdmRejInvalidEndpointIdent_Object = MibScalar
oacVoiceH323GwAdmRejInvalidEndpointIdent = _OacVoiceH323GwAdmRejInvalidEndpointIdent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 35),
    _OacVoiceH323GwAdmRejInvalidEndpointIdent_Type()
)
oacVoiceH323GwAdmRejInvalidEndpointIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmRejInvalidEndpointIdent.setStatus("current")
_OacVoiceH323GwAdmRejIncompleteAddress_Type = Integer32
_OacVoiceH323GwAdmRejIncompleteAddress_Object = MibScalar
oacVoiceH323GwAdmRejIncompleteAddress = _OacVoiceH323GwAdmRejIncompleteAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 36),
    _OacVoiceH323GwAdmRejIncompleteAddress_Type()
)
oacVoiceH323GwAdmRejIncompleteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmRejIncompleteAddress.setStatus("current")
_OacVoiceH323GwAdmRejNotSpecified_Type = Integer32
_OacVoiceH323GwAdmRejNotSpecified_Object = MibScalar
oacVoiceH323GwAdmRejNotSpecified = _OacVoiceH323GwAdmRejNotSpecified_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 37),
    _OacVoiceH323GwAdmRejNotSpecified_Type()
)
oacVoiceH323GwAdmRejNotSpecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmRejNotSpecified.setStatus("current")
_OacVoiceH323GwAdmRejUndefinedReason_Type = Integer32
_OacVoiceH323GwAdmRejUndefinedReason_Object = MibScalar
oacVoiceH323GwAdmRejUndefinedReason = _OacVoiceH323GwAdmRejUndefinedReason_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 3, 38),
    _OacVoiceH323GwAdmRejUndefinedReason_Type()
)
oacVoiceH323GwAdmRejUndefinedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceH323GwAdmRejUndefinedReason.setStatus("current")
_OacVoiceSipGw_ObjectIdentity = ObjectIdentity
oacVoiceSipGw = _OacVoiceSipGw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4)
)
_OacVoiceSipGwState_Type = OacVoipGatewayState
_OacVoiceSipGwState_Object = MibScalar
oacVoiceSipGwState = _OacVoiceSipGwState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 1),
    _OacVoiceSipGwState_Type()
)
oacVoiceSipGwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwState.setStatus("current")
_OacVoiceSipGwRegistrationState_Type = OacVoipGatewayRegistrationState
_OacVoiceSipGwRegistrationState_Object = MibScalar
oacVoiceSipGwRegistrationState = _OacVoiceSipGwRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 2),
    _OacVoiceSipGwRegistrationState_Type()
)
oacVoiceSipGwRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwRegistrationState.setStatus("current")


class _OacVoiceSipGwRegistrarServer_Type(DisplayString):
    """Custom type oacVoiceSipGwRegistrarServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_OacVoiceSipGwRegistrarServer_Type.__name__ = "DisplayString"
_OacVoiceSipGwRegistrarServer_Object = MibScalar
oacVoiceSipGwRegistrarServer = _OacVoiceSipGwRegistrarServer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 3),
    _OacVoiceSipGwRegistrarServer_Type()
)
oacVoiceSipGwRegistrarServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwRegistrarServer.setStatus("current")


class _OacVoiceSipGwBandwidth_Type(DisplayString):
    """Custom type oacVoiceSipGwBandwidth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_OacVoiceSipGwBandwidth_Type.__name__ = "DisplayString"
_OacVoiceSipGwBandwidth_Object = MibScalar
oacVoiceSipGwBandwidth = _OacVoiceSipGwBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 4),
    _OacVoiceSipGwBandwidth_Type()
)
oacVoiceSipGwBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwBandwidth.setStatus("current")
_OacVoiceSipGwRegistrationErrors_Type = Integer32
_OacVoiceSipGwRegistrationErrors_Object = MibScalar
oacVoiceSipGwRegistrationErrors = _OacVoiceSipGwRegistrationErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 5),
    _OacVoiceSipGwRegistrationErrors_Type()
)
oacVoiceSipGwRegistrationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwRegistrationErrors.setStatus("current")
_OacVoiceSipGwRegisteredEndpoints_Type = Integer32
_OacVoiceSipGwRegisteredEndpoints_Object = MibScalar
oacVoiceSipGwRegisteredEndpoints = _OacVoiceSipGwRegisteredEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 6),
    _OacVoiceSipGwRegisteredEndpoints_Type()
)
oacVoiceSipGwRegisteredEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwRegisteredEndpoints.setStatus("current")
_OacVoiceSipGwCurrentCalls_Type = Integer32
_OacVoiceSipGwCurrentCalls_Object = MibScalar
oacVoiceSipGwCurrentCalls = _OacVoiceSipGwCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 7),
    _OacVoiceSipGwCurrentCalls_Type()
)
oacVoiceSipGwCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwCurrentCalls.setStatus("current")
_OacVoiceSipGwAuthenticationRejects_Type = Integer32
_OacVoiceSipGwAuthenticationRejects_Object = MibScalar
oacVoiceSipGwAuthenticationRejects = _OacVoiceSipGwAuthenticationRejects_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 8),
    _OacVoiceSipGwAuthenticationRejects_Type()
)
oacVoiceSipGwAuthenticationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwAuthenticationRejects.setStatus("current")
_OacVoiceSipGwEndpointTable_Object = MibTable
oacVoiceSipGwEndpointTable = _OacVoiceSipGwEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 9)
)
if mibBuilder.loadTexts:
    oacVoiceSipGwEndpointTable.setStatus("current")
_OacVoiceSipGwEndpointEntry_Object = MibTableRow
oacVoiceSipGwEndpointEntry = _OacVoiceSipGwEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 9, 1)
)
oacVoiceSipGwEndpointEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceSipGwPhoneIndex"),
)
if mibBuilder.loadTexts:
    oacVoiceSipGwEndpointEntry.setStatus("current")
_OacVoiceSipGwPhoneIndex_Type = Integer32
_OacVoiceSipGwPhoneIndex_Object = MibTableColumn
oacVoiceSipGwPhoneIndex = _OacVoiceSipGwPhoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 9, 1, 1),
    _OacVoiceSipGwPhoneIndex_Type()
)
oacVoiceSipGwPhoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwPhoneIndex.setStatus("current")
_OacVoiceSipGwPhoneState_Type = OacVoiceSipGwPhoneState
_OacVoiceSipGwPhoneState_Object = MibTableColumn
oacVoiceSipGwPhoneState = _OacVoiceSipGwPhoneState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 9, 1, 2),
    _OacVoiceSipGwPhoneState_Type()
)
oacVoiceSipGwPhoneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwPhoneState.setStatus("current")


class _OacVoiceSipGwPhoneNumber_Type(DisplayString):
    """Custom type oacVoiceSipGwPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_OacVoiceSipGwPhoneNumber_Type.__name__ = "DisplayString"
_OacVoiceSipGwPhoneNumber_Object = MibTableColumn
oacVoiceSipGwPhoneNumber = _OacVoiceSipGwPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 9, 1, 3),
    _OacVoiceSipGwPhoneNumber_Type()
)
oacVoiceSipGwPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwPhoneNumber.setStatus("current")


class _OacVoiceSipGwPhoneSipId_Type(DisplayString):
    """Custom type oacVoiceSipGwPhoneSipId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_OacVoiceSipGwPhoneSipId_Type.__name__ = "DisplayString"
_OacVoiceSipGwPhoneSipId_Object = MibTableColumn
oacVoiceSipGwPhoneSipId = _OacVoiceSipGwPhoneSipId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 9, 1, 4),
    _OacVoiceSipGwPhoneSipId_Type()
)
oacVoiceSipGwPhoneSipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwPhoneSipId.setStatus("current")


class _OacVoiceSipGwRegistrationTimeout_Type(DisplayString):
    """Custom type oacVoiceSipGwRegistrationTimeout based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_OacVoiceSipGwRegistrationTimeout_Type.__name__ = "DisplayString"
_OacVoiceSipGwRegistrationTimeout_Object = MibTableColumn
oacVoiceSipGwRegistrationTimeout = _OacVoiceSipGwRegistrationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 9, 1, 5),
    _OacVoiceSipGwRegistrationTimeout_Type()
)
oacVoiceSipGwRegistrationTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwRegistrationTimeout.setStatus("current")
_OacVoiceSipGwMaxToRegisterEndpoints_Type = Integer32
_OacVoiceSipGwMaxToRegisterEndpoints_Object = MibScalar
oacVoiceSipGwMaxToRegisterEndpoints = _OacVoiceSipGwMaxToRegisterEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 4, 10),
    _OacVoiceSipGwMaxToRegisterEndpoints_Type()
)
oacVoiceSipGwMaxToRegisterEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipGwMaxToRegisterEndpoints.setStatus("current")
_OacVoiceSipServer_ObjectIdentity = ObjectIdentity
oacVoiceSipServer = _OacVoiceSipServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5)
)
_OacVoiceSipServerState_Type = OacVoipGatewayState
_OacVoiceSipServerState_Object = MibScalar
oacVoiceSipServerState = _OacVoiceSipServerState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 1),
    _OacVoiceSipServerState_Type()
)
oacVoiceSipServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipServerState.setStatus("current")
_OacVoiceSipServerRegisteredEndpoints_Type = Integer32
_OacVoiceSipServerRegisteredEndpoints_Object = MibScalar
oacVoiceSipServerRegisteredEndpoints = _OacVoiceSipServerRegisteredEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 2),
    _OacVoiceSipServerRegisteredEndpoints_Type()
)
oacVoiceSipServerRegisteredEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipServerRegisteredEndpoints.setStatus("current")


class _OacVoiceSipServerRegistrarServer_Type(DisplayString):
    """Custom type oacVoiceSipServerRegistrarServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_OacVoiceSipServerRegistrarServer_Type.__name__ = "DisplayString"
_OacVoiceSipServerRegistrarServer_Object = MibScalar
oacVoiceSipServerRegistrarServer = _OacVoiceSipServerRegistrarServer_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 3),
    _OacVoiceSipServerRegistrarServer_Type()
)
oacVoiceSipServerRegistrarServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipServerRegistrarServer.setStatus("current")
_OacVoiceSipServerCurrentCalls_Type = Integer32
_OacVoiceSipServerCurrentCalls_Object = MibScalar
oacVoiceSipServerCurrentCalls = _OacVoiceSipServerCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 4),
    _OacVoiceSipServerCurrentCalls_Type()
)
oacVoiceSipServerCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipServerCurrentCalls.setStatus("current")
_OacVoiceSipServerEndpointTable_Object = MibTable
oacVoiceSipServerEndpointTable = _OacVoiceSipServerEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 5)
)
if mibBuilder.loadTexts:
    oacVoiceSipServerEndpointTable.setStatus("current")
_OacVoiceSipServerEndpointEntry_Object = MibTableRow
oacVoiceSipServerEndpointEntry = _OacVoiceSipServerEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 5, 1)
)
oacVoiceSipServerEndpointEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceSipServerPhoneIndex"),
)
if mibBuilder.loadTexts:
    oacVoiceSipServerEndpointEntry.setStatus("current")
_OacVoiceSipServerPhoneIndex_Type = Integer32
_OacVoiceSipServerPhoneIndex_Object = MibTableColumn
oacVoiceSipServerPhoneIndex = _OacVoiceSipServerPhoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 5, 1, 1),
    _OacVoiceSipServerPhoneIndex_Type()
)
oacVoiceSipServerPhoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipServerPhoneIndex.setStatus("current")


class _OacVoiceSipServerPhoneNumber_Type(DisplayString):
    """Custom type oacVoiceSipServerPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_OacVoiceSipServerPhoneNumber_Type.__name__ = "DisplayString"
_OacVoiceSipServerPhoneNumber_Object = MibTableColumn
oacVoiceSipServerPhoneNumber = _OacVoiceSipServerPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 5, 1, 2),
    _OacVoiceSipServerPhoneNumber_Type()
)
oacVoiceSipServerPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipServerPhoneNumber.setStatus("current")


class _OacVoiceSipServerPhoneIpAddress_Type(DisplayString):
    """Custom type oacVoiceSipServerPhoneIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_OacVoiceSipServerPhoneIpAddress_Type.__name__ = "DisplayString"
_OacVoiceSipServerPhoneIpAddress_Object = MibTableColumn
oacVoiceSipServerPhoneIpAddress = _OacVoiceSipServerPhoneIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 5, 1, 3),
    _OacVoiceSipServerPhoneIpAddress_Type()
)
oacVoiceSipServerPhoneIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipServerPhoneIpAddress.setStatus("current")


class _OacVoiceSipServerPhoneSipId_Type(DisplayString):
    """Custom type oacVoiceSipServerPhoneSipId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_OacVoiceSipServerPhoneSipId_Type.__name__ = "DisplayString"
_OacVoiceSipServerPhoneSipId_Object = MibTableColumn
oacVoiceSipServerPhoneSipId = _OacVoiceSipServerPhoneSipId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 5, 1, 4),
    _OacVoiceSipServerPhoneSipId_Type()
)
oacVoiceSipServerPhoneSipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipServerPhoneSipId.setStatus("current")


class _OacVoiceSipServerRegistrationTime_Type(DisplayString):
    """Custom type oacVoiceSipServerRegistrationTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_OacVoiceSipServerRegistrationTime_Type.__name__ = "DisplayString"
_OacVoiceSipServerRegistrationTime_Object = MibTableColumn
oacVoiceSipServerRegistrationTime = _OacVoiceSipServerRegistrationTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 5, 1, 5),
    _OacVoiceSipServerRegistrationTime_Type()
)
oacVoiceSipServerRegistrationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipServerRegistrationTime.setStatus("current")


class _OacVoiceSipServerRegistrationTimeout_Type(DisplayString):
    """Custom type oacVoiceSipServerRegistrationTimeout based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_OacVoiceSipServerRegistrationTimeout_Type.__name__ = "DisplayString"
_OacVoiceSipServerRegistrationTimeout_Object = MibTableColumn
oacVoiceSipServerRegistrationTimeout = _OacVoiceSipServerRegistrationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 5, 5, 1, 6),
    _OacVoiceSipServerRegistrationTimeout_Type()
)
oacVoiceSipServerRegistrationTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceSipServerRegistrationTimeout.setStatus("current")
_OacVoiceMgcpGw_ObjectIdentity = ObjectIdentity
oacVoiceMgcpGw = _OacVoiceMgcpGw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 6)
)
_OacVoiceMgcpGwState_Type = OacVoipGatewayState
_OacVoiceMgcpGwState_Object = MibScalar
oacVoiceMgcpGwState = _OacVoiceMgcpGwState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 6, 1),
    _OacVoiceMgcpGwState_Type()
)
oacVoiceMgcpGwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceMgcpGwState.setStatus("current")


class _OacVoiceMgcpGwCallAgentIpAddress_Type(DisplayString):
    """Custom type oacVoiceMgcpGwCallAgentIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 21),
    )


_OacVoiceMgcpGwCallAgentIpAddress_Type.__name__ = "DisplayString"
_OacVoiceMgcpGwCallAgentIpAddress_Object = MibScalar
oacVoiceMgcpGwCallAgentIpAddress = _OacVoiceMgcpGwCallAgentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 6, 2),
    _OacVoiceMgcpGwCallAgentIpAddress_Type()
)
oacVoiceMgcpGwCallAgentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceMgcpGwCallAgentIpAddress.setStatus("current")
_OacVoiceMgcpGwConnectionState_Type = OacVoipMgcpGatewayConnectionState
_OacVoiceMgcpGwConnectionState_Object = MibScalar
oacVoiceMgcpGwConnectionState = _OacVoiceMgcpGwConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 6, 3),
    _OacVoiceMgcpGwConnectionState_Type()
)
oacVoiceMgcpGwConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceMgcpGwConnectionState.setStatus("current")
_OacVoiceMgcpGwEstablishedPathCurrentNumber_Type = Integer32
_OacVoiceMgcpGwEstablishedPathCurrentNumber_Object = MibScalar
oacVoiceMgcpGwEstablishedPathCurrentNumber = _OacVoiceMgcpGwEstablishedPathCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 6, 4),
    _OacVoiceMgcpGwEstablishedPathCurrentNumber_Type()
)
oacVoiceMgcpGwEstablishedPathCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceMgcpGwEstablishedPathCurrentNumber.setStatus("current")
_OacVoiceMgcpGwOutCallsOffHookEvents_Type = Integer32
_OacVoiceMgcpGwOutCallsOffHookEvents_Object = MibScalar
oacVoiceMgcpGwOutCallsOffHookEvents = _OacVoiceMgcpGwOutCallsOffHookEvents_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 6, 5),
    _OacVoiceMgcpGwOutCallsOffHookEvents_Type()
)
oacVoiceMgcpGwOutCallsOffHookEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceMgcpGwOutCallsOffHookEvents.setStatus("current")
_OacVoiceMgcpGwOutCallsPathEstablished_Type = Integer32
_OacVoiceMgcpGwOutCallsPathEstablished_Object = MibScalar
oacVoiceMgcpGwOutCallsPathEstablished = _OacVoiceMgcpGwOutCallsPathEstablished_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 6, 6),
    _OacVoiceMgcpGwOutCallsPathEstablished_Type()
)
oacVoiceMgcpGwOutCallsPathEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceMgcpGwOutCallsPathEstablished.setStatus("current")
_OacVoiceMgcpGwIncCallsRingingEvents_Type = Integer32
_OacVoiceMgcpGwIncCallsRingingEvents_Object = MibScalar
oacVoiceMgcpGwIncCallsRingingEvents = _OacVoiceMgcpGwIncCallsRingingEvents_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 6, 7),
    _OacVoiceMgcpGwIncCallsRingingEvents_Type()
)
oacVoiceMgcpGwIncCallsRingingEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceMgcpGwIncCallsRingingEvents.setStatus("current")
_OacVoiceMgcpGwIncCallsPath_Type = Integer32
_OacVoiceMgcpGwIncCallsPath_Object = MibScalar
oacVoiceMgcpGwIncCallsPath = _OacVoiceMgcpGwIncCallsPath_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 3, 6, 8),
    _OacVoiceMgcpGwIncCallsPath_Type()
)
oacVoiceMgcpGwIncCallsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceMgcpGwIncCallsPath.setStatus("current")
_OacVoiceStatMos_ObjectIdentity = ObjectIdentity
oacVoiceStatMos = _OacVoiceStatMos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4)
)
_OacVoiceStatMosTable_Object = MibTable
oacVoiceStatMosTable = _OacVoiceStatMosTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    oacVoiceStatMosTable.setStatus("current")
_OacVoiceStatMosEntry_Object = MibTableRow
oacVoiceStatMosEntry = _OacVoiceStatMosEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1)
)
oacVoiceStatMosEntry.setIndexNames(
    (0, "ONEACCESS-VOICE-MIB", "oacVoiceStatMosIndex"),
)
if mibBuilder.loadTexts:
    oacVoiceStatMosEntry.setStatus("current")


class _OacVoiceStatMosIndex_Type(Integer32):
    """Custom type oacVoiceStatMosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_OacVoiceStatMosIndex_Type.__name__ = "Integer32"
_OacVoiceStatMosIndex_Object = MibTableColumn
oacVoiceStatMosIndex = _OacVoiceStatMosIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 1),
    _OacVoiceStatMosIndex_Type()
)
oacVoiceStatMosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosIndex.setStatus("current")
_OacVoiceStatMosEntryNumberOfCalls_Type = Integer32
_OacVoiceStatMosEntryNumberOfCalls_Object = MibTableColumn
oacVoiceStatMosEntryNumberOfCalls = _OacVoiceStatMosEntryNumberOfCalls_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 2),
    _OacVoiceStatMosEntryNumberOfCalls_Type()
)
oacVoiceStatMosEntryNumberOfCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosEntryNumberOfCalls.setStatus("current")


class _OacVoiceStatMosEntryMosAvg_Type(DisplayString):
    """Custom type oacVoiceStatMosEntryMosAvg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_OacVoiceStatMosEntryMosAvg_Type.__name__ = "DisplayString"
_OacVoiceStatMosEntryMosAvg_Object = MibTableColumn
oacVoiceStatMosEntryMosAvg = _OacVoiceStatMosEntryMosAvg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 3),
    _OacVoiceStatMosEntryMosAvg_Type()
)
oacVoiceStatMosEntryMosAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosEntryMosAvg.setStatus("current")


class _OacVoiceStatMosEntryMosMin_Type(DisplayString):
    """Custom type oacVoiceStatMosEntryMosMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_OacVoiceStatMosEntryMosMin_Type.__name__ = "DisplayString"
_OacVoiceStatMosEntryMosMin_Object = MibTableColumn
oacVoiceStatMosEntryMosMin = _OacVoiceStatMosEntryMosMin_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 4),
    _OacVoiceStatMosEntryMosMin_Type()
)
oacVoiceStatMosEntryMosMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosEntryMosMin.setStatus("current")


class _OacVoiceStatMosEntryMosMax_Type(DisplayString):
    """Custom type oacVoiceStatMosEntryMosMax based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_OacVoiceStatMosEntryMosMax_Type.__name__ = "DisplayString"
_OacVoiceStatMosEntryMosMax_Object = MibTableColumn
oacVoiceStatMosEntryMosMax = _OacVoiceStatMosEntryMosMax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 5),
    _OacVoiceStatMosEntryMosMax_Type()
)
oacVoiceStatMosEntryMosMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosEntryMosMax.setStatus("current")
_OacVoiceStatMosEntryErlAvg_Type = Integer32
_OacVoiceStatMosEntryErlAvg_Object = MibTableColumn
oacVoiceStatMosEntryErlAvg = _OacVoiceStatMosEntryErlAvg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 6),
    _OacVoiceStatMosEntryErlAvg_Type()
)
oacVoiceStatMosEntryErlAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosEntryErlAvg.setStatus("current")
_OacVoiceStatMosEntryAcomAvg_Type = Integer32
_OacVoiceStatMosEntryAcomAvg_Object = MibTableColumn
oacVoiceStatMosEntryAcomAvg = _OacVoiceStatMosEntryAcomAvg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 7),
    _OacVoiceStatMosEntryAcomAvg_Type()
)
oacVoiceStatMosEntryAcomAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosEntryAcomAvg.setStatus("current")
_OacVoiceStatMosEntryLossRateAvg_Type = Integer32
_OacVoiceStatMosEntryLossRateAvg_Object = MibTableColumn
oacVoiceStatMosEntryLossRateAvg = _OacVoiceStatMosEntryLossRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 8),
    _OacVoiceStatMosEntryLossRateAvg_Type()
)
oacVoiceStatMosEntryLossRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosEntryLossRateAvg.setStatus("current")
_OacVoiceStatMosJitterAvg_Type = Integer32
_OacVoiceStatMosJitterAvg_Object = MibTableColumn
oacVoiceStatMosJitterAvg = _OacVoiceStatMosJitterAvg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 9),
    _OacVoiceStatMosJitterAvg_Type()
)
oacVoiceStatMosJitterAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosJitterAvg.setStatus("current")
_OacVoiceStatMosEntryMaxDelayAvg_Type = Integer32
_OacVoiceStatMosEntryMaxDelayAvg_Object = MibTableColumn
oacVoiceStatMosEntryMaxDelayAvg = _OacVoiceStatMosEntryMaxDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 10),
    _OacVoiceStatMosEntryMaxDelayAvg_Type()
)
oacVoiceStatMosEntryMaxDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosEntryMaxDelayAvg.setStatus("current")
_OacVoiceStatMosEntryPddAvg_Type = Integer32
_OacVoiceStatMosEntryPddAvg_Object = MibTableColumn
oacVoiceStatMosEntryPddAvg = _OacVoiceStatMosEntryPddAvg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 1, 4, 1, 1, 11),
    _OacVoiceStatMosEntryPddAvg_Type()
)
oacVoiceStatMosEntryPddAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacVoiceStatMosEntryPddAvg.setStatus("current")
_OacVoiceStatNotifications_ObjectIdentity = ObjectIdentity
oacVoiceStatNotifications = _OacVoiceStatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 2)
)
_OacVoiceStatConformance_ObjectIdentity = ObjectIdentity
oacVoiceStatConformance = _OacVoiceStatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 3)
)
_OacVoiceStatGroups_ObjectIdentity = ObjectIdentity
oacVoiceStatGroups = _OacVoiceStatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 3, 1)
)
_OacVoiceStatCompliances_ObjectIdentity = ObjectIdentity
oacVoiceStatCompliances = _OacVoiceStatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 3, 2)
)

# Managed Objects groups

oacVoiceStatGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 3, 1, 1)
)
oacVoiceStatGeneralGroup.setObjects(
      *(("ONEACCESS-VOICE-MIB", "oacVoiceFxsPorts"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceBriPorts"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePriPorts"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnections"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnections"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceFxsDialPeers"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceBriDialPeers"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePriDialPeers"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortFxsIfIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortVoicePortFxs"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortFxsProtocolState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortFxsOperState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortFxsAdminState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortFxsConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortFxsAttachedDialPeer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortFxsVoiceCommNb"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortBriIfIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortVoicePortBri"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortBriProtocolDescriptor"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortBriProtocolState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortBriOperState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortBriAdminState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortBriConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortBriLayer1"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortBriAttachedDialPeer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortBriVoiceCommNb"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriIfIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortVoicePortPri"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriPhysicalType"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriProtocolDescriptor"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriProtocolState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriOperState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriAdminState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriLayer1"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriAttachedDialPeer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriVoiceCommNb"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriAisOccur"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVoicePortPriRdiOccur"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnConnection"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnVpVc"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnCurrentState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnAtmVcFailureOccurence"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnAtmVcTotalFailureDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLesVoicePathNum"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLesTotalCpIwfOriginated"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLesTotalCoIwfOriginated"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLesCpIwfRestartNum"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLesCoIwfRestartNum"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnElcpTotalSuccessfulAllocation"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnElcpTotalUnsuccessfulAllocation"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnElcpTotalAllocationDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLapv5NbrRxFrame"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLapv5NbrTxFrame"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLapv5NbrRxIFrame"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLapv5NbrTxIFrame"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLapv5NbrRxRejFrame"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLapv5NbrTxRejFrame"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLapv5NbrRxRnrFrame"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLapv5NbrTxRnrFrame"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnLapv5NbrT200Expiration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnAal2TotalFramesReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnAal2TotalBytesReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnAal2TotalFramesDiscardedReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnAal2TotalFramesErrorsReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnAal2TotalFramesSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnAal2TotalBytesSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVmoaConnAal2TotalFramesDiscardedSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnConnection"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnVpVc"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnCurrentState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnAtmVcFailureOccurence"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnAtmVcTotalFailureDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnAal2TotalFramesReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnAal2TotalBytesReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnAal2TotalFramesDiscardedReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnAal2TotalFramesErrorsReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnAal2TotalFramesSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnAal2TotalBytesSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceVtoaConnAal2TotalFramesDiscardedSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsDialPeer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsLinkedPort"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsCurrentState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsPortStatus"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsPathStatus"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsCurrentTxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsCurrentRxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmofxsCurrentBc"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsCurrentCid"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsBlockingOccurence"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsTotalBlockingDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsVoicePacketSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsVoicePacketReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsPathEstablished"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsPathRqFailed"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoafxsPathDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriDialPeer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriPort"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriCurrentState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriPortStatus"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriBlockingOccurence"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriTotalBlockingDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriBxAllocNum"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1CurrentTxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1CurrentRxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1CurrentBc"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1CurrentCid"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1VoicePacketSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1VoicePacketReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1BytesSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1BytesReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1PathEstablished"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1PathDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB1Bundle"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2CurrentTxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2CurrentRxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2CurrentBc"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2CurrentCid"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2VoicePacketSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2VoicePacketReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2BytesSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2BytesReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2PathEstablished"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2PathDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriB2Bundle"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriDCurrentCid"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriDFramesSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriDFramesReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriDBytesSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoabriDBytesReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsDialPeer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsLinkedPort"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsPortStatus"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsCurrentState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsBlockingOccurence"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTotalBlockingDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsBxAllocNum"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTsxIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTsxChannelType"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTsxCurrentTxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTsxCurrentRxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTsxCurrentBC"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTsxCurrentCID"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoaccsTsxBundle"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasDialPeer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasLinkedPort"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasPortStatus"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasCurrentState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasBlockingOccurence"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTotalBlockingDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasBxAllocNum"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxChannelType"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxCurrentTxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxCurrentRxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxCurrentBC"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxCurrentCID"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxVoicePacketSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxVoicePacketReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacasTsxBundle"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriDialPeer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriLinkedPort"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriPortStatus"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriCurrentState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriBlockingOccurence"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriTotalBlockingDuration"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriBxAllocNum"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriTsxIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriTsxChannelType"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriTsxCurrentTxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriTsxCurrentRxCoder"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriTsxCurrentBC"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriTsxCurrentCID"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriTsxVoicePacketSent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVmoapriTsxVoicePacketReceived"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesDialPeer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesLinkedPort"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesCurrentState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesCellLossIntegrationPeriod"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesOutOfSyncOccurences"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesTxCells"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesReassCells"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesBufOverflows"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesBufUnderflows"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesPointerReframes"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesHdrErrors"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerVoiceVtoacesLossCells"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortIfIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipPortName"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipPortType"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipPriPhysicalType"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIsdnProtocolDescriptor"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipCurrentState"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipConfigState"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIsdnLayer1Status"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIsdnLayer2Status"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipAttachedDialPeer"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipCurrentCalls"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIsdnTxFramesOnDChannel"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIsdnRxFramesOnDChannel"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipPriNbAisOccurence"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipPriNbRdiOccurence"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCalls"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsUnsufficientPotsGroupResource"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsIsdnPhysicalInterfaceDown"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsIsdnCauseClass0"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsIsdnCauseClass1"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsIsdnCC1NormalCause"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsCC1UserBusy"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsCC1NoAnswer"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsIsdnCauseClass2"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsIsdnCauseClass3"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsIsdnCauseClass4"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsIsdnCauseClass5"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsIsdnCauseClass6"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipOutCallsIsdnCauseClass7"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIncCalls"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIncCallsBackupInvoked"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIncCallsFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIncCallsRemoteFailure"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIncCallsUnknownNumber"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIncCallsDspUnavailable"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIncCallsNoVoipRessourceAvailable"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipIncCallsNotSpecified"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipMgcpOffHookEvents"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipMgcpOutCallsPathEstablished"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipMgcpRingingEvents"),
        ("ONEACCESS-VOICE-MIB", "oacVoicePortVoipMgcpIncCallsPathEstablished"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerCurrentCalls"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCalls"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsMgcpOffHookEvents"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsMgcpPathEstablished"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsRasFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsRasFailGatekeeperUnavailable"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsRasFailAdmissionRejects"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsH225Q931Failures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCauseClass0"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCauseClass1"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCC1NormalCause"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCC1UserBusy"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCC1NoAnswer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCauseClass2"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCauseClass3"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCauseClass4"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCauseClass5"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCauseClass6"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsHQFailCauseClass7"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsH245Failures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsH245FailIncompatibleCapabilities"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsH245FailProtocolErrors"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsInternalFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsInternalFailDspUnavailable"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsInternalFailMaxBwExceeded"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsInternalFailMaxConnExceeded"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerOutCallsInternalFailNotSpecified"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCalls"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsMgcpRingingEvents"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsMgcpPathEstablished"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsRasFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsRasFailGatekeeperUnavailable"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsRasFailAdmissionRejects"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsLocalPortFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsH245Failures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsH245FailIncompatibleCapabilities"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsH245FailProtocolErrors"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsInternalFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsInternalFailDspUnavailable"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsInternalFailUnknownNumber"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsInternalFailChannelPortUnavailable"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsInternalFailMaxBwExceeded"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsInternalFailMaxConnExceeded"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsInternalFailNotSpecified"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerIncCallsAdviceofCharge"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerRtpStatNbTxPackets"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerRtpStatNbRxPackets"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerRtpStatNbTxBytes"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerRtpStatNbRxBytes"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerRtpStatNbExcessiveJitterEvents"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerRtpStatNbLostPackets"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerRtpStatNbInvalidPackets"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerModemNbSwitchingToModemMode"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxNbOutgoingFax"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxNbIncomingFax"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxNbFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxFailureRequestMode"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxFailurePreMsgProcedure"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxFailurePage"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxNbTxPackets"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxNbRxPackets"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxNbTxBytes"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxNbRxBytes"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceDialPeerFaxNbLostPackets"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwStateReason"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRasBwControl"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwPortabilityStatus"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwPortabilityStatusTimeout"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwDs0Configured"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwDs0Low"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwDs0High"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwDs0Current"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwBwConfigured"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwBwLow"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwBwHigh"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwBwCurrent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegistrationState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwGatekeeperIdentifier"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwGatekeeperAddress"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegistrationRequest"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegistrationFailures"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegFailNoResponse"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegFailInvalidIpAddress"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegFailDuplicateAlias"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegFailInvalidTerminalType"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegFailResourceUnavailable"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegFailInvalidAlias"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegFailSecurityDenial"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwRegFailUndefinedReason"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmissionRequests"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmissionRejects"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmRejCalledPartyNotRegistered"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmRejInvalidPermission"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmRejRequestDenied"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmRejCallerNotRegistered"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmRejResourceUnavailable"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmRejSecurityDenial"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmRejInvalidEndpointIdent"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmRejIncompleteAddress"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmRejNotSpecified"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceH323GwAdmRejUndefinedReason"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwRegistrationState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwRegistrarServer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwBandwidth"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwRegistrationErrors"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwRegisteredEndpoints"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwCurrentCalls"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwAuthenticationRejects"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwMaxToRegisterEndpoints"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwPhoneIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwPhoneState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwPhoneNumber"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwPhoneSipId"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipGwRegistrationTimeout"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipServerState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipServerRegisteredEndpoints"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipServerRegistrarServer"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipServerCurrentCalls"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipServerPhoneIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipServerPhoneNumber"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipServerPhoneIpAddress"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipServerPhoneSipId"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipServerRegistrationTime"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceSipServerRegistrationTimeout"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceMgcpGwState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceMgcpGwCallAgentIpAddress"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceMgcpGwConnectionState"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceMgcpGwEstablishedPathCurrentNumber"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceMgcpGwOutCallsOffHookEvents"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceMgcpGwOutCallsPathEstablished"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceMgcpGwIncCallsRingingEvents"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceMgcpGwIncCallsPath"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosIndex"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosEntryNumberOfCalls"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosEntryMosAvg"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosEntryMosMin"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosEntryMosMax"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosEntryErlAvg"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosEntryAcomAvg"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosEntryLossRateAvg"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosJitterAvg"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosEntryMaxDelayAvg"),
        ("ONEACCESS-VOICE-MIB", "oacVoiceStatMosEntryPddAvg"))
)
if mibBuilder.loadTexts:
    oacVoiceStatGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oacVoiceStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    oacVoiceStatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-VOICE-MIB",
    **{"VoiceFxsPortStatus": VoiceFxsPortStatus,
       "VoiceFxsPathStatus": VoiceFxsPathStatus,
       "VoicePriPhPortType": VoicePriPhPortType,
       "VoicePriProtocol": VoicePriProtocol,
       "VoiceBriProtocol": VoiceBriProtocol,
       "VoiceFxsProtocol": VoiceFxsProtocol,
       "VoiceAcDeacState": VoiceAcDeacState,
       "VoiceUpDnState": VoiceUpDnState,
       "VoiceBriPortStatus": VoiceBriPortStatus,
       "VoiceIOCoder": VoiceIOCoder,
       "VoiceBearerCap": VoiceBearerCap,
       "VoiceChnType": VoiceChnType,
       "VoipPortType": VoipPortType,
       "IsdnProtocolDescriptor": IsdnProtocolDescriptor,
       "PortVoipCurrentState": PortVoipCurrentState,
       "ConfigState": ConfigState,
       "IsdnLayerStatus": IsdnLayerStatus,
       "OacVoipGatewayState": OacVoipGatewayState,
       "OacVoipPriPhysicalType": OacVoipPriPhysicalType,
       "OacVoipGatewayStateReason": OacVoipGatewayStateReason,
       "OacVoipGatewayRegistrationState": OacVoipGatewayRegistrationState,
       "OacH323GwRasBwControl": OacH323GwRasBwControl,
       "OacH323GwPortabilityStatus": OacH323GwPortabilityStatus,
       "OacVoipMgcpGatewayConnectionState": OacVoipMgcpGatewayConnectionState,
       "OacVoiceSipGwPhoneState": OacVoiceSipGwPhoneState,
       "oacVoiceMIBModule": oacVoiceMIBModule,
       "oacExpIMVoiceStatistics": oacExpIMVoiceStatistics,
       "oacVoiceStatObjects": oacVoiceStatObjects,
       "oacVoiceStatGlobal": oacVoiceStatGlobal,
       "oacVoiceFxsPorts": oacVoiceFxsPorts,
       "oacVoiceBriPorts": oacVoiceBriPorts,
       "oacVoicePriPorts": oacVoicePriPorts,
       "oacVoiceVmoaConnections": oacVoiceVmoaConnections,
       "oacVoiceVtoaConnections": oacVoiceVtoaConnections,
       "oacVoiceFxsDialPeers": oacVoiceFxsDialPeers,
       "oacVoiceBriDialPeers": oacVoiceBriDialPeers,
       "oacVoicePriDialPeers": oacVoicePriDialPeers,
       "oacVoiceStatBles": oacVoiceStatBles,
       "oacVoicePortBles": oacVoicePortBles,
       "oacVoiceVoicePortFxsTable": oacVoiceVoicePortFxsTable,
       "oacVoiceVoicePortFxsEntry": oacVoiceVoicePortFxsEntry,
       "oacVoiceVoicePortFxsIfIndex": oacVoiceVoicePortFxsIfIndex,
       "oacVoiceVoicePortVoicePortFxs": oacVoiceVoicePortVoicePortFxs,
       "oacVoiceVoicePortFxsProtocolState": oacVoiceVoicePortFxsProtocolState,
       "oacVoiceVoicePortFxsOperState": oacVoiceVoicePortFxsOperState,
       "oacVoiceVoicePortFxsAdminState": oacVoiceVoicePortFxsAdminState,
       "oacVoiceVoicePortFxsConfigState": oacVoiceVoicePortFxsConfigState,
       "oacVoiceVoicePortFxsAttachedDialPeer": oacVoiceVoicePortFxsAttachedDialPeer,
       "oacVoiceVoicePortFxsVoiceCommNb": oacVoiceVoicePortFxsVoiceCommNb,
       "oacVoiceVoicePortBriTable": oacVoiceVoicePortBriTable,
       "oacVoiceVoicePortBriEntry": oacVoiceVoicePortBriEntry,
       "oacVoiceVoicePortBriIfIndex": oacVoiceVoicePortBriIfIndex,
       "oacVoiceVoicePortVoicePortBri": oacVoiceVoicePortVoicePortBri,
       "oacVoiceVoicePortBriProtocolDescriptor": oacVoiceVoicePortBriProtocolDescriptor,
       "oacVoiceVoicePortBriProtocolState": oacVoiceVoicePortBriProtocolState,
       "oacVoiceVoicePortBriOperState": oacVoiceVoicePortBriOperState,
       "oacVoiceVoicePortBriAdminState": oacVoiceVoicePortBriAdminState,
       "oacVoiceVoicePortBriConfigState": oacVoiceVoicePortBriConfigState,
       "oacVoiceVoicePortBriLayer1": oacVoiceVoicePortBriLayer1,
       "oacVoiceVoicePortBriAttachedDialPeer": oacVoiceVoicePortBriAttachedDialPeer,
       "oacVoiceVoicePortBriVoiceCommNb": oacVoiceVoicePortBriVoiceCommNb,
       "oacVoiceVoicePortPriTable": oacVoiceVoicePortPriTable,
       "oacVoiceVoicePortPriEntry": oacVoiceVoicePortPriEntry,
       "oacVoiceVoicePortPriIfIndex": oacVoiceVoicePortPriIfIndex,
       "oacVoiceVoicePortVoicePortPri": oacVoiceVoicePortVoicePortPri,
       "oacVoiceVoicePortPriPhysicalType": oacVoiceVoicePortPriPhysicalType,
       "oacVoiceVoicePortPriProtocolDescriptor": oacVoiceVoicePortPriProtocolDescriptor,
       "oacVoiceVoicePortPriProtocolState": oacVoiceVoicePortPriProtocolState,
       "oacVoiceVoicePortPriOperState": oacVoiceVoicePortPriOperState,
       "oacVoiceVoicePortPriAdminState": oacVoiceVoicePortPriAdminState,
       "oacVoiceVoicePortPriConfigState": oacVoiceVoicePortPriConfigState,
       "oacVoiceVoicePortPriLayer1": oacVoiceVoicePortPriLayer1,
       "oacVoiceVoicePortPriAttachedDialPeer": oacVoiceVoicePortPriAttachedDialPeer,
       "oacVoiceVoicePortPriVoiceCommNb": oacVoiceVoicePortPriVoiceCommNb,
       "oacVoiceVoicePortPriAisOccur": oacVoiceVoicePortPriAisOccur,
       "oacVoiceVoicePortPriRdiOccur": oacVoiceVoicePortPriRdiOccur,
       "oacVoiceDialPeerBles": oacVoiceDialPeerBles,
       "oacVoiceDialPeerVoiceVmoafxsTable": oacVoiceDialPeerVoiceVmoafxsTable,
       "oacVoiceDialPeerVoiceVmoafxsEntry": oacVoiceDialPeerVoiceVmoafxsEntry,
       "oacVoiceDialPeerVoiceVmoafxsDialPeer": oacVoiceDialPeerVoiceVmoafxsDialPeer,
       "oacVoiceDialPeerVoiceVmoafxsLinkedPort": oacVoiceDialPeerVoiceVmoafxsLinkedPort,
       "oacVoiceDialPeerVoiceVmoafxsCurrentState": oacVoiceDialPeerVoiceVmoafxsCurrentState,
       "oacVoiceDialPeerVoiceVmoafxsPortStatus": oacVoiceDialPeerVoiceVmoafxsPortStatus,
       "oacVoiceDialPeerVoiceVmoafxsPathStatus": oacVoiceDialPeerVoiceVmoafxsPathStatus,
       "oacVoiceDialPeerVoiceVmoafxsCurrentTxCoder": oacVoiceDialPeerVoiceVmoafxsCurrentTxCoder,
       "oacVoiceDialPeerVoiceVmoafxsCurrentRxCoder": oacVoiceDialPeerVoiceVmoafxsCurrentRxCoder,
       "oacVoiceDialPeerVoiceVmofxsCurrentBc": oacVoiceDialPeerVoiceVmofxsCurrentBc,
       "oacVoiceDialPeerVoiceVmoafxsCurrentCid": oacVoiceDialPeerVoiceVmoafxsCurrentCid,
       "oacVoiceDialPeerVoiceVmoafxsBlockingOccurence": oacVoiceDialPeerVoiceVmoafxsBlockingOccurence,
       "oacVoiceDialPeerVoiceVmoafxsTotalBlockingDuration": oacVoiceDialPeerVoiceVmoafxsTotalBlockingDuration,
       "oacVoiceDialPeerVoiceVmoafxsVoicePacketSent": oacVoiceDialPeerVoiceVmoafxsVoicePacketSent,
       "oacVoiceDialPeerVoiceVmoafxsVoicePacketReceived": oacVoiceDialPeerVoiceVmoafxsVoicePacketReceived,
       "oacVoiceDialPeerVoiceVmoafxsPathEstablished": oacVoiceDialPeerVoiceVmoafxsPathEstablished,
       "oacVoiceDialPeerVoiceVmoafxsPathRqFailed": oacVoiceDialPeerVoiceVmoafxsPathRqFailed,
       "oacVoiceDialPeerVoiceVmoafxsPathDuration": oacVoiceDialPeerVoiceVmoafxsPathDuration,
       "oacVoiceDialPeerVoiceVmoabriTable": oacVoiceDialPeerVoiceVmoabriTable,
       "oacVoiceDialPeerVoiceVmoabriEntry": oacVoiceDialPeerVoiceVmoabriEntry,
       "oacVoiceDialPeerVoiceVmoabriDialPeer": oacVoiceDialPeerVoiceVmoabriDialPeer,
       "oacVoiceDialPeerVoiceVmoabriPort": oacVoiceDialPeerVoiceVmoabriPort,
       "oacVoiceDialPeerVoiceVmoabriCurrentState": oacVoiceDialPeerVoiceVmoabriCurrentState,
       "oacVoiceDialPeerVoiceVmoabriConfigState": oacVoiceDialPeerVoiceVmoabriConfigState,
       "oacVoiceDialPeerVoiceVmoabriPortStatus": oacVoiceDialPeerVoiceVmoabriPortStatus,
       "oacVoiceDialPeerVoiceVmoabriBlockingOccurence": oacVoiceDialPeerVoiceVmoabriBlockingOccurence,
       "oacVoiceDialPeerVoiceVmoabriTotalBlockingDuration": oacVoiceDialPeerVoiceVmoabriTotalBlockingDuration,
       "oacVoiceDialPeerVoiceVmoabriBxAllocNum": oacVoiceDialPeerVoiceVmoabriBxAllocNum,
       "oacVoiceDialPeerVoiceVmoabriB1Table": oacVoiceDialPeerVoiceVmoabriB1Table,
       "oacVoiceDialPeerVoiceVmoabriB1Entry": oacVoiceDialPeerVoiceVmoabriB1Entry,
       "oacVoiceDialPeerVoiceVmoabriB1CurrentTxCoder": oacVoiceDialPeerVoiceVmoabriB1CurrentTxCoder,
       "oacVoiceDialPeerVoiceVmoabriB1CurrentRxCoder": oacVoiceDialPeerVoiceVmoabriB1CurrentRxCoder,
       "oacVoiceDialPeerVoiceVmoabriB1CurrentBc": oacVoiceDialPeerVoiceVmoabriB1CurrentBc,
       "oacVoiceDialPeerVoiceVmoabriB1CurrentCid": oacVoiceDialPeerVoiceVmoabriB1CurrentCid,
       "oacVoiceDialPeerVoiceVmoabriB1VoicePacketSent": oacVoiceDialPeerVoiceVmoabriB1VoicePacketSent,
       "oacVoiceDialPeerVoiceVmoabriB1VoicePacketReceived": oacVoiceDialPeerVoiceVmoabriB1VoicePacketReceived,
       "oacVoiceDialPeerVoiceVmoabriB1BytesSent": oacVoiceDialPeerVoiceVmoabriB1BytesSent,
       "oacVoiceDialPeerVoiceVmoabriB1BytesReceived": oacVoiceDialPeerVoiceVmoabriB1BytesReceived,
       "oacVoiceDialPeerVoiceVmoabriB1PathEstablished": oacVoiceDialPeerVoiceVmoabriB1PathEstablished,
       "oacVoiceDialPeerVoiceVmoabriB1PathDuration": oacVoiceDialPeerVoiceVmoabriB1PathDuration,
       "oacVoiceDialPeerVoiceVmoabriB1Bundle": oacVoiceDialPeerVoiceVmoabriB1Bundle,
       "oacVoiceDialPeerVoiceVmoabriB2Table": oacVoiceDialPeerVoiceVmoabriB2Table,
       "oacVoiceDialPeerVoiceVmoabriB2Entry": oacVoiceDialPeerVoiceVmoabriB2Entry,
       "oacVoiceDialPeerVoiceVmoabriB2CurrentTxCoder": oacVoiceDialPeerVoiceVmoabriB2CurrentTxCoder,
       "oacVoiceDialPeerVoiceVmoabriB2CurrentRxCoder": oacVoiceDialPeerVoiceVmoabriB2CurrentRxCoder,
       "oacVoiceDialPeerVoiceVmoabriB2CurrentBc": oacVoiceDialPeerVoiceVmoabriB2CurrentBc,
       "oacVoiceDialPeerVoiceVmoabriB2CurrentCid": oacVoiceDialPeerVoiceVmoabriB2CurrentCid,
       "oacVoiceDialPeerVoiceVmoabriB2VoicePacketSent": oacVoiceDialPeerVoiceVmoabriB2VoicePacketSent,
       "oacVoiceDialPeerVoiceVmoabriB2VoicePacketReceived": oacVoiceDialPeerVoiceVmoabriB2VoicePacketReceived,
       "oacVoiceDialPeerVoiceVmoabriB2BytesSent": oacVoiceDialPeerVoiceVmoabriB2BytesSent,
       "oacVoiceDialPeerVoiceVmoabriB2BytesReceived": oacVoiceDialPeerVoiceVmoabriB2BytesReceived,
       "oacVoiceDialPeerVoiceVmoabriB2PathEstablished": oacVoiceDialPeerVoiceVmoabriB2PathEstablished,
       "oacVoiceDialPeerVoiceVmoabriB2PathDuration": oacVoiceDialPeerVoiceVmoabriB2PathDuration,
       "oacVoiceDialPeerVoiceVmoabriB2Bundle": oacVoiceDialPeerVoiceVmoabriB2Bundle,
       "oacVoiceDialPeerVoiceVmoabriDTable": oacVoiceDialPeerVoiceVmoabriDTable,
       "oacVoiceDialPeerVoiceVmoabriDEntry": oacVoiceDialPeerVoiceVmoabriDEntry,
       "oacVoiceDialPeerVoiceVmoabriDCurrentCid": oacVoiceDialPeerVoiceVmoabriDCurrentCid,
       "oacVoiceDialPeerVoiceVmoabriDFramesSent": oacVoiceDialPeerVoiceVmoabriDFramesSent,
       "oacVoiceDialPeerVoiceVmoabriDFramesReceived": oacVoiceDialPeerVoiceVmoabriDFramesReceived,
       "oacVoiceDialPeerVoiceVmoabriDBytesSent": oacVoiceDialPeerVoiceVmoabriDBytesSent,
       "oacVoiceDialPeerVoiceVmoabriDBytesReceived": oacVoiceDialPeerVoiceVmoabriDBytesReceived,
       "oacVoiceDialPeerVoiceVmoapriTable": oacVoiceDialPeerVoiceVmoapriTable,
       "oacVoiceDialPeerVoiceVmoapriEntry": oacVoiceDialPeerVoiceVmoapriEntry,
       "oacVoiceDialPeerVoiceVmoapriDialPeer": oacVoiceDialPeerVoiceVmoapriDialPeer,
       "oacVoiceDialPeerVoiceVmoapriLinkedPort": oacVoiceDialPeerVoiceVmoapriLinkedPort,
       "oacVoiceDialPeerVoiceVmoapriPortStatus": oacVoiceDialPeerVoiceVmoapriPortStatus,
       "oacVoiceDialPeerVoiceVmoapriCurrentState": oacVoiceDialPeerVoiceVmoapriCurrentState,
       "oacVoiceDialPeerVoiceVmoapriConfigState": oacVoiceDialPeerVoiceVmoapriConfigState,
       "oacVoiceDialPeerVoiceVmoapriBlockingOccurence": oacVoiceDialPeerVoiceVmoapriBlockingOccurence,
       "oacVoiceDialPeerVoiceVmoapriTotalBlockingDuration": oacVoiceDialPeerVoiceVmoapriTotalBlockingDuration,
       "oacVoiceDialPeerVoiceVmoapriBxAllocNum": oacVoiceDialPeerVoiceVmoapriBxAllocNum,
       "oacVoiceDialPeerVoiceVmoapriTsxTable": oacVoiceDialPeerVoiceVmoapriTsxTable,
       "oacVoiceDialPeerVoiceVmoapriTsxEntry": oacVoiceDialPeerVoiceVmoapriTsxEntry,
       "oacVoiceDialPeerVoiceVmoapriTsxIndex": oacVoiceDialPeerVoiceVmoapriTsxIndex,
       "oacVoiceDialPeerVoiceVmoapriTsxChannelType": oacVoiceDialPeerVoiceVmoapriTsxChannelType,
       "oacVoiceDialPeerVoiceVmoapriTsxCurrentTxCoder": oacVoiceDialPeerVoiceVmoapriTsxCurrentTxCoder,
       "oacVoiceDialPeerVoiceVmoapriTsxCurrentRxCoder": oacVoiceDialPeerVoiceVmoapriTsxCurrentRxCoder,
       "oacVoiceDialPeerVoiceVmoapriTsxCurrentBC": oacVoiceDialPeerVoiceVmoapriTsxCurrentBC,
       "oacVoiceDialPeerVoiceVmoapriTsxCurrentCID": oacVoiceDialPeerVoiceVmoapriTsxCurrentCID,
       "oacVoiceDialPeerVoiceVmoapriTsxVoicePacketSent": oacVoiceDialPeerVoiceVmoapriTsxVoicePacketSent,
       "oacVoiceDialPeerVoiceVmoapriTsxVoicePacketReceived": oacVoiceDialPeerVoiceVmoapriTsxVoicePacketReceived,
       "oacVoiceDialPeerVoiceVtoaccsTable": oacVoiceDialPeerVoiceVtoaccsTable,
       "oacVoiceDialPeerVoiceVtoaccsEntry": oacVoiceDialPeerVoiceVtoaccsEntry,
       "oacVoiceDialPeerVoiceVtoaccsDialPeer": oacVoiceDialPeerVoiceVtoaccsDialPeer,
       "oacVoiceDialPeerVoiceVtoaccsLinkedPort": oacVoiceDialPeerVoiceVtoaccsLinkedPort,
       "oacVoiceDialPeerVoiceVtoaccsPortStatus": oacVoiceDialPeerVoiceVtoaccsPortStatus,
       "oacVoiceDialPeerVoiceVtoaccsCurrentState": oacVoiceDialPeerVoiceVtoaccsCurrentState,
       "oacVoiceDialPeerVoiceVtoaccsConfigState": oacVoiceDialPeerVoiceVtoaccsConfigState,
       "oacVoiceDialPeerVoiceVtoaccsBlockingOccurence": oacVoiceDialPeerVoiceVtoaccsBlockingOccurence,
       "oacVoiceDialPeerVoiceVtoaccsTotalBlockingDuration": oacVoiceDialPeerVoiceVtoaccsTotalBlockingDuration,
       "oacVoiceDialPeerVoiceVtoaccsBxAllocNum": oacVoiceDialPeerVoiceVtoaccsBxAllocNum,
       "oacVoiceDialPeerVoiceVtoaccsTsxTable": oacVoiceDialPeerVoiceVtoaccsTsxTable,
       "oacVoiceDialPeerVoiceVtoaccsTsxEntry": oacVoiceDialPeerVoiceVtoaccsTsxEntry,
       "oacVoiceDialPeerVoiceVtoaccsTsxIndex": oacVoiceDialPeerVoiceVtoaccsTsxIndex,
       "oacVoiceDialPeerVoiceVtoaccsTsxChannelType": oacVoiceDialPeerVoiceVtoaccsTsxChannelType,
       "oacVoiceDialPeerVoiceVtoaccsTsxCurrentTxCoder": oacVoiceDialPeerVoiceVtoaccsTsxCurrentTxCoder,
       "oacVoiceDialPeerVoiceVtoaccsTsxCurrentRxCoder": oacVoiceDialPeerVoiceVtoaccsTsxCurrentRxCoder,
       "oacVoiceDialPeerVoiceVtoaccsTsxCurrentBC": oacVoiceDialPeerVoiceVtoaccsTsxCurrentBC,
       "oacVoiceDialPeerVoiceVtoaccsTsxCurrentCID": oacVoiceDialPeerVoiceVtoaccsTsxCurrentCID,
       "oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketSent": oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketSent,
       "oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketReceived": oacVoiceDialPeerVoiceVtoaccsTsxVoicePacketReceived,
       "oacVoiceDialPeerVoiceVtoaccsTsxBundle": oacVoiceDialPeerVoiceVtoaccsTsxBundle,
       "oacVoiceDialPeerVoiceVtoacasTable": oacVoiceDialPeerVoiceVtoacasTable,
       "oacVoiceDialPeerVoiceVtoacasEntry": oacVoiceDialPeerVoiceVtoacasEntry,
       "oacVoiceDialPeerVoiceVtoacasDialPeer": oacVoiceDialPeerVoiceVtoacasDialPeer,
       "oacVoiceDialPeerVoiceVtoacasLinkedPort": oacVoiceDialPeerVoiceVtoacasLinkedPort,
       "oacVoiceDialPeerVoiceVtoacasPortStatus": oacVoiceDialPeerVoiceVtoacasPortStatus,
       "oacVoiceDialPeerVoiceVtoacasCurrentState": oacVoiceDialPeerVoiceVtoacasCurrentState,
       "oacVoiceDialPeerVoiceVtoacasConfigState": oacVoiceDialPeerVoiceVtoacasConfigState,
       "oacVoiceDialPeerVoiceVtoacasBlockingOccurence": oacVoiceDialPeerVoiceVtoacasBlockingOccurence,
       "oacVoiceDialPeerVoiceVtoacasTotalBlockingDuration": oacVoiceDialPeerVoiceVtoacasTotalBlockingDuration,
       "oacVoiceDialPeerVoiceVtoacasBxAllocNum": oacVoiceDialPeerVoiceVtoacasBxAllocNum,
       "oacVoiceDialPeerVoiceVtoacasTsxTable": oacVoiceDialPeerVoiceVtoacasTsxTable,
       "oacVoiceDialPeerVoiceVtoacasTsxEntry": oacVoiceDialPeerVoiceVtoacasTsxEntry,
       "oacVoiceDialPeerVoiceVtoacasTsxIndex": oacVoiceDialPeerVoiceVtoacasTsxIndex,
       "oacVoiceDialPeerVoiceVtoacasTsxChannelType": oacVoiceDialPeerVoiceVtoacasTsxChannelType,
       "oacVoiceDialPeerVoiceVtoacasTsxCurrentTxCoder": oacVoiceDialPeerVoiceVtoacasTsxCurrentTxCoder,
       "oacVoiceDialPeerVoiceVtoacasTsxCurrentRxCoder": oacVoiceDialPeerVoiceVtoacasTsxCurrentRxCoder,
       "oacVoiceDialPeerVoiceVtoacasTsxCurrentBC": oacVoiceDialPeerVoiceVtoacasTsxCurrentBC,
       "oacVoiceDialPeerVoiceVtoacasTsxCurrentCID": oacVoiceDialPeerVoiceVtoacasTsxCurrentCID,
       "oacVoiceDialPeerVoiceVtoacasTsxVoicePacketSent": oacVoiceDialPeerVoiceVtoacasTsxVoicePacketSent,
       "oacVoiceDialPeerVoiceVtoacasTsxVoicePacketReceived": oacVoiceDialPeerVoiceVtoacasTsxVoicePacketReceived,
       "oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesSent": oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesSent,
       "oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesReceived": oacVoiceDialPeerVoiceVtoacasTsxVoiceCasFramesReceived,
       "oacVoiceDialPeerVoiceVtoacasTsxBundle": oacVoiceDialPeerVoiceVtoacasTsxBundle,
       "oacVoiceDialPeerVoiceVtoacesTable": oacVoiceDialPeerVoiceVtoacesTable,
       "oacVoiceDialPeerVoiceVtoacesEntry": oacVoiceDialPeerVoiceVtoacesEntry,
       "oacVoiceDialPeerVoiceVtoacesDialPeer": oacVoiceDialPeerVoiceVtoacesDialPeer,
       "oacVoiceDialPeerVoiceVtoacesLinkedPort": oacVoiceDialPeerVoiceVtoacesLinkedPort,
       "oacVoiceDialPeerVoiceVtoacesCurrentState": oacVoiceDialPeerVoiceVtoacesCurrentState,
       "oacVoiceDialPeerVoiceVtoacesConfigState": oacVoiceDialPeerVoiceVtoacesConfigState,
       "oacVoiceDialPeerVoiceVtoacesCellLossIntegrationPeriod": oacVoiceDialPeerVoiceVtoacesCellLossIntegrationPeriod,
       "oacVoiceDialPeerVoiceVtoacesOutOfSyncOccurences": oacVoiceDialPeerVoiceVtoacesOutOfSyncOccurences,
       "oacVoiceDialPeerVoiceVtoacesTxCells": oacVoiceDialPeerVoiceVtoacesTxCells,
       "oacVoiceDialPeerVoiceVtoacesReassCells": oacVoiceDialPeerVoiceVtoacesReassCells,
       "oacVoiceDialPeerVoiceVtoacesBufOverflows": oacVoiceDialPeerVoiceVtoacesBufOverflows,
       "oacVoiceDialPeerVoiceVtoacesBufUnderflows": oacVoiceDialPeerVoiceVtoacesBufUnderflows,
       "oacVoiceDialPeerVoiceVtoacesPointerReframes": oacVoiceDialPeerVoiceVtoacesPointerReframes,
       "oacVoiceDialPeerVoiceVtoacesHdrErrors": oacVoiceDialPeerVoiceVtoacesHdrErrors,
       "oacVoiceDialPeerVoiceVtoacesLossCells": oacVoiceDialPeerVoiceVtoacesLossCells,
       "oacVoiceConnectionBles": oacVoiceConnectionBles,
       "oacVoiceVmoaConnTable": oacVoiceVmoaConnTable,
       "oacVoiceVmoaConnEntry": oacVoiceVmoaConnEntry,
       "oacVoiceVmoaConnConnection": oacVoiceVmoaConnConnection,
       "oacVoiceVmoaConnVpVc": oacVoiceVmoaConnVpVc,
       "oacVoiceVmoaConnCurrentState": oacVoiceVmoaConnCurrentState,
       "oacVoiceVmoaConnConfigState": oacVoiceVmoaConnConfigState,
       "oacVoiceVmoaConnAtmVcFailureOccurence": oacVoiceVmoaConnAtmVcFailureOccurence,
       "oacVoiceVmoaConnAtmVcTotalFailureDuration": oacVoiceVmoaConnAtmVcTotalFailureDuration,
       "oacVoiceVmoaConnLesTable": oacVoiceVmoaConnLesTable,
       "oacVoiceVmoaConnLesEntry": oacVoiceVmoaConnLesEntry,
       "oacVoiceVmoaConnLesVoicePathNum": oacVoiceVmoaConnLesVoicePathNum,
       "oacVoiceVmoaConnLesTotalCpIwfOriginated": oacVoiceVmoaConnLesTotalCpIwfOriginated,
       "oacVoiceVmoaConnLesTotalCoIwfOriginated": oacVoiceVmoaConnLesTotalCoIwfOriginated,
       "oacVoiceVmoaConnLesCpIwfRestartNum": oacVoiceVmoaConnLesCpIwfRestartNum,
       "oacVoiceVmoaConnLesCoIwfRestartNum": oacVoiceVmoaConnLesCoIwfRestartNum,
       "oacVoiceVmoaConnElcpTable": oacVoiceVmoaConnElcpTable,
       "oacVoiceVmoaConnElcpEntry": oacVoiceVmoaConnElcpEntry,
       "oacVoiceVmoaConnElcpTotalSuccessfulAllocation": oacVoiceVmoaConnElcpTotalSuccessfulAllocation,
       "oacVoiceVmoaConnElcpTotalUnsuccessfulAllocation": oacVoiceVmoaConnElcpTotalUnsuccessfulAllocation,
       "oacVoiceVmoaConnElcpTotalAllocationDuration": oacVoiceVmoaConnElcpTotalAllocationDuration,
       "oacVoiceVmoaConnLapv5Table": oacVoiceVmoaConnLapv5Table,
       "oacVoiceVmoaConnLapv5Entry": oacVoiceVmoaConnLapv5Entry,
       "oacVoiceVmoaConnLapv5NbrRxFrame": oacVoiceVmoaConnLapv5NbrRxFrame,
       "oacVoiceVmoaConnLapv5NbrTxFrame": oacVoiceVmoaConnLapv5NbrTxFrame,
       "oacVoiceVmoaConnLapv5NbrRxIFrame": oacVoiceVmoaConnLapv5NbrRxIFrame,
       "oacVoiceVmoaConnLapv5NbrTxIFrame": oacVoiceVmoaConnLapv5NbrTxIFrame,
       "oacVoiceVmoaConnLapv5NbrRxRejFrame": oacVoiceVmoaConnLapv5NbrRxRejFrame,
       "oacVoiceVmoaConnLapv5NbrTxRejFrame": oacVoiceVmoaConnLapv5NbrTxRejFrame,
       "oacVoiceVmoaConnLapv5NbrRxRnrFrame": oacVoiceVmoaConnLapv5NbrRxRnrFrame,
       "oacVoiceVmoaConnLapv5NbrTxRnrFrame": oacVoiceVmoaConnLapv5NbrTxRnrFrame,
       "oacVoiceVmoaConnLapv5NbrT200Expiration": oacVoiceVmoaConnLapv5NbrT200Expiration,
       "oacVoiceVmoaConnAal2Table": oacVoiceVmoaConnAal2Table,
       "oacVoiceVmoaConnAal2Entry": oacVoiceVmoaConnAal2Entry,
       "oacVoiceVmoaConnAal2TotalFramesReceived": oacVoiceVmoaConnAal2TotalFramesReceived,
       "oacVoiceVmoaConnAal2TotalBytesReceived": oacVoiceVmoaConnAal2TotalBytesReceived,
       "oacVoiceVmoaConnAal2TotalFramesDiscardedReceived": oacVoiceVmoaConnAal2TotalFramesDiscardedReceived,
       "oacVoiceVmoaConnAal2TotalFramesErrorsReceived": oacVoiceVmoaConnAal2TotalFramesErrorsReceived,
       "oacVoiceVmoaConnAal2TotalFramesSent": oacVoiceVmoaConnAal2TotalFramesSent,
       "oacVoiceVmoaConnAal2TotalBytesSent": oacVoiceVmoaConnAal2TotalBytesSent,
       "oacVoiceVmoaConnAal2TotalFramesDiscardedSent": oacVoiceVmoaConnAal2TotalFramesDiscardedSent,
       "oacVoiceVtoaConnTable": oacVoiceVtoaConnTable,
       "oacVoiceVtoaConnEntry": oacVoiceVtoaConnEntry,
       "oacVoiceVtoaConnConnection": oacVoiceVtoaConnConnection,
       "oacVoiceVtoaConnVpVc": oacVoiceVtoaConnVpVc,
       "oacVoiceVtoaConnCurrentState": oacVoiceVtoaConnCurrentState,
       "oacVoiceVtoaConnConfigState": oacVoiceVtoaConnConfigState,
       "oacVoiceVtoaConnAtmVcFailureOccurence": oacVoiceVtoaConnAtmVcFailureOccurence,
       "oacVoiceVtoaConnAtmVcTotalFailureDuration": oacVoiceVtoaConnAtmVcTotalFailureDuration,
       "oacVoiceVtoaConnAal2Table": oacVoiceVtoaConnAal2Table,
       "oacVoiceVtoaConnAal2Entry": oacVoiceVtoaConnAal2Entry,
       "oacVoiceVtoaConnAal2TotalFramesReceived": oacVoiceVtoaConnAal2TotalFramesReceived,
       "oacVoiceVtoaConnAal2TotalBytesReceived": oacVoiceVtoaConnAal2TotalBytesReceived,
       "oacVoiceVtoaConnAal2TotalFramesDiscardedReceived": oacVoiceVtoaConnAal2TotalFramesDiscardedReceived,
       "oacVoiceVtoaConnAal2TotalFramesErrorsReceived": oacVoiceVtoaConnAal2TotalFramesErrorsReceived,
       "oacVoiceVtoaConnAal2TotalFramesSent": oacVoiceVtoaConnAal2TotalFramesSent,
       "oacVoiceVtoaConnAal2TotalBytesSent": oacVoiceVtoaConnAal2TotalBytesSent,
       "oacVoiceVtoaConnAal2TotalFramesDiscardedSent": oacVoiceVtoaConnAal2TotalFramesDiscardedSent,
       "oacVoiceStatVoip": oacVoiceStatVoip,
       "oacVoicePortVoipTable": oacVoicePortVoipTable,
       "oacVoicePortVoipEntry": oacVoicePortVoipEntry,
       "oacVoicePortIfIndex": oacVoicePortIfIndex,
       "oacVoicePortVoipPortName": oacVoicePortVoipPortName,
       "oacVoicePortVoipPortType": oacVoicePortVoipPortType,
       "oacVoicePortVoipPriPhysicalType": oacVoicePortVoipPriPhysicalType,
       "oacVoicePortVoipIsdnProtocolDescriptor": oacVoicePortVoipIsdnProtocolDescriptor,
       "oacVoicePortVoipCurrentState": oacVoicePortVoipCurrentState,
       "oacVoicePortVoipConfigState": oacVoicePortVoipConfigState,
       "oacVoicePortVoipIsdnLayer1Status": oacVoicePortVoipIsdnLayer1Status,
       "oacVoicePortVoipIsdnLayer2Status": oacVoicePortVoipIsdnLayer2Status,
       "oacVoicePortVoipAttachedDialPeer": oacVoicePortVoipAttachedDialPeer,
       "oacVoicePortVoipCurrentCalls": oacVoicePortVoipCurrentCalls,
       "oacVoicePortVoipIsdnTxFramesOnDChannel": oacVoicePortVoipIsdnTxFramesOnDChannel,
       "oacVoicePortVoipIsdnRxFramesOnDChannel": oacVoicePortVoipIsdnRxFramesOnDChannel,
       "oacVoicePortVoipPriNbAisOccurence": oacVoicePortVoipPriNbAisOccurence,
       "oacVoicePortVoipPriNbRdiOccurence": oacVoicePortVoipPriNbRdiOccurence,
       "oacVoicePortVoipOutCalls": oacVoicePortVoipOutCalls,
       "oacVoicePortVoipOutCallsFailures": oacVoicePortVoipOutCallsFailures,
       "oacVoicePortVoipOutCallsUnsufficientPotsGroupResource": oacVoicePortVoipOutCallsUnsufficientPotsGroupResource,
       "oacVoicePortVoipOutCallsIsdnPhysicalInterfaceDown": oacVoicePortVoipOutCallsIsdnPhysicalInterfaceDown,
       "oacVoicePortVoipOutCallsIsdnCauseClass0": oacVoicePortVoipOutCallsIsdnCauseClass0,
       "oacVoicePortVoipOutCallsIsdnCauseClass1": oacVoicePortVoipOutCallsIsdnCauseClass1,
       "oacVoicePortVoipOutCallsIsdnCC1NormalCause": oacVoicePortVoipOutCallsIsdnCC1NormalCause,
       "oacVoicePortVoipOutCallsCC1UserBusy": oacVoicePortVoipOutCallsCC1UserBusy,
       "oacVoicePortVoipOutCallsCC1NoAnswer": oacVoicePortVoipOutCallsCC1NoAnswer,
       "oacVoicePortVoipOutCallsIsdnCauseClass2": oacVoicePortVoipOutCallsIsdnCauseClass2,
       "oacVoicePortVoipOutCallsIsdnCauseClass3": oacVoicePortVoipOutCallsIsdnCauseClass3,
       "oacVoicePortVoipOutCallsIsdnCauseClass4": oacVoicePortVoipOutCallsIsdnCauseClass4,
       "oacVoicePortVoipOutCallsIsdnCauseClass5": oacVoicePortVoipOutCallsIsdnCauseClass5,
       "oacVoicePortVoipOutCallsIsdnCauseClass6": oacVoicePortVoipOutCallsIsdnCauseClass6,
       "oacVoicePortVoipOutCallsIsdnCauseClass7": oacVoicePortVoipOutCallsIsdnCauseClass7,
       "oacVoicePortVoipIncCalls": oacVoicePortVoipIncCalls,
       "oacVoicePortVoipIncCallsBackupInvoked": oacVoicePortVoipIncCallsBackupInvoked,
       "oacVoicePortVoipIncCallsFailures": oacVoicePortVoipIncCallsFailures,
       "oacVoicePortVoipIncCallsRemoteFailure": oacVoicePortVoipIncCallsRemoteFailure,
       "oacVoicePortVoipIncCallsUnknownNumber": oacVoicePortVoipIncCallsUnknownNumber,
       "oacVoicePortVoipIncCallsDspUnavailable": oacVoicePortVoipIncCallsDspUnavailable,
       "oacVoicePortVoipIncCallsNoVoipRessourceAvailable": oacVoicePortVoipIncCallsNoVoipRessourceAvailable,
       "oacVoicePortVoipIncCallsNotSpecified": oacVoicePortVoipIncCallsNotSpecified,
       "oacVoicePortVoipMgcpOffHookEvents": oacVoicePortVoipMgcpOffHookEvents,
       "oacVoicePortVoipMgcpOutCallsPathEstablished": oacVoicePortVoipMgcpOutCallsPathEstablished,
       "oacVoicePortVoipMgcpRingingEvents": oacVoicePortVoipMgcpRingingEvents,
       "oacVoicePortVoipMgcpIncCallsPathEstablished": oacVoicePortVoipMgcpIncCallsPathEstablished,
       "oacVoiceDialPeerVoipTable": oacVoiceDialPeerVoipTable,
       "oacVoiceDialPeerVoipEntry": oacVoiceDialPeerVoipEntry,
       "oacVoiceDialPeerIndex": oacVoiceDialPeerIndex,
       "oacVoiceDialPeerCurrentCalls": oacVoiceDialPeerCurrentCalls,
       "oacVoiceDialPeerOutCalls": oacVoiceDialPeerOutCalls,
       "oacVoiceDialPeerOutCallsMgcpOffHookEvents": oacVoiceDialPeerOutCallsMgcpOffHookEvents,
       "oacVoiceDialPeerOutCallsMgcpPathEstablished": oacVoiceDialPeerOutCallsMgcpPathEstablished,
       "oacVoiceDialPeerOutCallsFailures": oacVoiceDialPeerOutCallsFailures,
       "oacVoiceDialPeerOutCallsRasFailures": oacVoiceDialPeerOutCallsRasFailures,
       "oacVoiceDialPeerOutCallsRasFailGatekeeperUnavailable": oacVoiceDialPeerOutCallsRasFailGatekeeperUnavailable,
       "oacVoiceDialPeerOutCallsRasFailAdmissionRejects": oacVoiceDialPeerOutCallsRasFailAdmissionRejects,
       "oacVoiceDialPeerOutCallsH225Q931Failures": oacVoiceDialPeerOutCallsH225Q931Failures,
       "oacVoiceDialPeerOutCallsHQFailCauseClass0": oacVoiceDialPeerOutCallsHQFailCauseClass0,
       "oacVoiceDialPeerOutCallsHQFailCauseClass1": oacVoiceDialPeerOutCallsHQFailCauseClass1,
       "oacVoiceDialPeerOutCallsHQFailCC1NormalCause": oacVoiceDialPeerOutCallsHQFailCC1NormalCause,
       "oacVoiceDialPeerOutCallsHQFailCC1UserBusy": oacVoiceDialPeerOutCallsHQFailCC1UserBusy,
       "oacVoiceDialPeerOutCallsHQFailCC1NoAnswer": oacVoiceDialPeerOutCallsHQFailCC1NoAnswer,
       "oacVoiceDialPeerOutCallsHQFailCauseClass2": oacVoiceDialPeerOutCallsHQFailCauseClass2,
       "oacVoiceDialPeerOutCallsHQFailCauseClass3": oacVoiceDialPeerOutCallsHQFailCauseClass3,
       "oacVoiceDialPeerOutCallsHQFailCauseClass4": oacVoiceDialPeerOutCallsHQFailCauseClass4,
       "oacVoiceDialPeerOutCallsHQFailCauseClass5": oacVoiceDialPeerOutCallsHQFailCauseClass5,
       "oacVoiceDialPeerOutCallsHQFailCauseClass6": oacVoiceDialPeerOutCallsHQFailCauseClass6,
       "oacVoiceDialPeerOutCallsHQFailCauseClass7": oacVoiceDialPeerOutCallsHQFailCauseClass7,
       "oacVoiceDialPeerOutCallsH245Failures": oacVoiceDialPeerOutCallsH245Failures,
       "oacVoiceDialPeerOutCallsH245FailIncompatibleCapabilities": oacVoiceDialPeerOutCallsH245FailIncompatibleCapabilities,
       "oacVoiceDialPeerOutCallsH245FailProtocolErrors": oacVoiceDialPeerOutCallsH245FailProtocolErrors,
       "oacVoiceDialPeerOutCallsInternalFailures": oacVoiceDialPeerOutCallsInternalFailures,
       "oacVoiceDialPeerOutCallsInternalFailDspUnavailable": oacVoiceDialPeerOutCallsInternalFailDspUnavailable,
       "oacVoiceDialPeerOutCallsInternalFailMaxBwExceeded": oacVoiceDialPeerOutCallsInternalFailMaxBwExceeded,
       "oacVoiceDialPeerOutCallsInternalFailMaxConnExceeded": oacVoiceDialPeerOutCallsInternalFailMaxConnExceeded,
       "oacVoiceDialPeerOutCallsInternalFailNotSpecified": oacVoiceDialPeerOutCallsInternalFailNotSpecified,
       "oacVoiceDialPeerIncCalls": oacVoiceDialPeerIncCalls,
       "oacVoiceDialPeerIncCallsMgcpRingingEvents": oacVoiceDialPeerIncCallsMgcpRingingEvents,
       "oacVoiceDialPeerIncCallsMgcpPathEstablished": oacVoiceDialPeerIncCallsMgcpPathEstablished,
       "oacVoiceDialPeerIncCallsFailures": oacVoiceDialPeerIncCallsFailures,
       "oacVoiceDialPeerIncCallsRasFailures": oacVoiceDialPeerIncCallsRasFailures,
       "oacVoiceDialPeerIncCallsRasFailGatekeeperUnavailable": oacVoiceDialPeerIncCallsRasFailGatekeeperUnavailable,
       "oacVoiceDialPeerIncCallsRasFailAdmissionRejects": oacVoiceDialPeerIncCallsRasFailAdmissionRejects,
       "oacVoiceDialPeerIncCallsLocalPortFailures": oacVoiceDialPeerIncCallsLocalPortFailures,
       "oacVoiceDialPeerIncCallsH245Failures": oacVoiceDialPeerIncCallsH245Failures,
       "oacVoiceDialPeerIncCallsH245FailIncompatibleCapabilities": oacVoiceDialPeerIncCallsH245FailIncompatibleCapabilities,
       "oacVoiceDialPeerIncCallsH245FailProtocolErrors": oacVoiceDialPeerIncCallsH245FailProtocolErrors,
       "oacVoiceDialPeerIncCallsInternalFailures": oacVoiceDialPeerIncCallsInternalFailures,
       "oacVoiceDialPeerIncCallsInternalFailDspUnavailable": oacVoiceDialPeerIncCallsInternalFailDspUnavailable,
       "oacVoiceDialPeerIncCallsInternalFailUnknownNumber": oacVoiceDialPeerIncCallsInternalFailUnknownNumber,
       "oacVoiceDialPeerIncCallsInternalFailChannelPortUnavailable": oacVoiceDialPeerIncCallsInternalFailChannelPortUnavailable,
       "oacVoiceDialPeerIncCallsInternalFailMaxBwExceeded": oacVoiceDialPeerIncCallsInternalFailMaxBwExceeded,
       "oacVoiceDialPeerIncCallsInternalFailMaxConnExceeded": oacVoiceDialPeerIncCallsInternalFailMaxConnExceeded,
       "oacVoiceDialPeerIncCallsInternalFailNotSpecified": oacVoiceDialPeerIncCallsInternalFailNotSpecified,
       "oacVoiceDialPeerIncCallsAdviceofCharge": oacVoiceDialPeerIncCallsAdviceofCharge,
       "oacVoiceDialPeerRtpStatNbTxPackets": oacVoiceDialPeerRtpStatNbTxPackets,
       "oacVoiceDialPeerRtpStatNbRxPackets": oacVoiceDialPeerRtpStatNbRxPackets,
       "oacVoiceDialPeerRtpStatNbTxBytes": oacVoiceDialPeerRtpStatNbTxBytes,
       "oacVoiceDialPeerRtpStatNbRxBytes": oacVoiceDialPeerRtpStatNbRxBytes,
       "oacVoiceDialPeerRtpStatNbExcessiveJitterEvents": oacVoiceDialPeerRtpStatNbExcessiveJitterEvents,
       "oacVoiceDialPeerRtpStatNbLostPackets": oacVoiceDialPeerRtpStatNbLostPackets,
       "oacVoiceDialPeerRtpStatNbInvalidPackets": oacVoiceDialPeerRtpStatNbInvalidPackets,
       "oacVoiceDialPeerModemNbSwitchingToModemMode": oacVoiceDialPeerModemNbSwitchingToModemMode,
       "oacVoiceDialPeerFaxNbOutgoingFax": oacVoiceDialPeerFaxNbOutgoingFax,
       "oacVoiceDialPeerFaxNbIncomingFax": oacVoiceDialPeerFaxNbIncomingFax,
       "oacVoiceDialPeerFaxNbFailures": oacVoiceDialPeerFaxNbFailures,
       "oacVoiceDialPeerFaxFailureRequestMode": oacVoiceDialPeerFaxFailureRequestMode,
       "oacVoiceDialPeerFaxFailurePreMsgProcedure": oacVoiceDialPeerFaxFailurePreMsgProcedure,
       "oacVoiceDialPeerFaxFailurePage": oacVoiceDialPeerFaxFailurePage,
       "oacVoiceDialPeerFaxNbTxPackets": oacVoiceDialPeerFaxNbTxPackets,
       "oacVoiceDialPeerFaxNbRxPackets": oacVoiceDialPeerFaxNbRxPackets,
       "oacVoiceDialPeerFaxNbTxBytes": oacVoiceDialPeerFaxNbTxBytes,
       "oacVoiceDialPeerFaxNbRxBytes": oacVoiceDialPeerFaxNbRxBytes,
       "oacVoiceDialPeerFaxNbLostPackets": oacVoiceDialPeerFaxNbLostPackets,
       "oacVoiceH323Gw": oacVoiceH323Gw,
       "oacVoiceH323GwState": oacVoiceH323GwState,
       "oacVoiceH323GwStateReason": oacVoiceH323GwStateReason,
       "oacVoiceH323GwRasBwControl": oacVoiceH323GwRasBwControl,
       "oacVoiceH323GwPortabilityStatus": oacVoiceH323GwPortabilityStatus,
       "oacVoiceH323GwPortabilityStatusTimeout": oacVoiceH323GwPortabilityStatusTimeout,
       "oacVoiceH323GwDs0Configured": oacVoiceH323GwDs0Configured,
       "oacVoiceH323GwDs0Low": oacVoiceH323GwDs0Low,
       "oacVoiceH323GwDs0High": oacVoiceH323GwDs0High,
       "oacVoiceH323GwDs0Current": oacVoiceH323GwDs0Current,
       "oacVoiceH323GwBwConfigured": oacVoiceH323GwBwConfigured,
       "oacVoiceH323GwBwLow": oacVoiceH323GwBwLow,
       "oacVoiceH323GwBwHigh": oacVoiceH323GwBwHigh,
       "oacVoiceH323GwBwCurrent": oacVoiceH323GwBwCurrent,
       "oacVoiceH323GwRegistrationState": oacVoiceH323GwRegistrationState,
       "oacVoiceH323GwGatekeeperIdentifier": oacVoiceH323GwGatekeeperIdentifier,
       "oacVoiceH323GwGatekeeperAddress": oacVoiceH323GwGatekeeperAddress,
       "oacVoiceH323GwRegistrationRequest": oacVoiceH323GwRegistrationRequest,
       "oacVoiceH323GwRegistrationFailures": oacVoiceH323GwRegistrationFailures,
       "oacVoiceH323GwRegFailNoResponse": oacVoiceH323GwRegFailNoResponse,
       "oacVoiceH323GwRegFailInvalidIpAddress": oacVoiceH323GwRegFailInvalidIpAddress,
       "oacVoiceH323GwRegFailDuplicateAlias": oacVoiceH323GwRegFailDuplicateAlias,
       "oacVoiceH323GwRegFailInvalidTerminalType": oacVoiceH323GwRegFailInvalidTerminalType,
       "oacVoiceH323GwRegFailResourceUnavailable": oacVoiceH323GwRegFailResourceUnavailable,
       "oacVoiceH323GwRegFailInvalidAlias": oacVoiceH323GwRegFailInvalidAlias,
       "oacVoiceH323GwRegFailSecurityDenial": oacVoiceH323GwRegFailSecurityDenial,
       "oacVoiceH323GwRegFailUndefinedReason": oacVoiceH323GwRegFailUndefinedReason,
       "oacVoiceH323GwAdmissionRequests": oacVoiceH323GwAdmissionRequests,
       "oacVoiceH323GwAdmissionRejects": oacVoiceH323GwAdmissionRejects,
       "oacVoiceH323GwAdmRejCalledPartyNotRegistered": oacVoiceH323GwAdmRejCalledPartyNotRegistered,
       "oacVoiceH323GwAdmRejInvalidPermission": oacVoiceH323GwAdmRejInvalidPermission,
       "oacVoiceH323GwAdmRejRequestDenied": oacVoiceH323GwAdmRejRequestDenied,
       "oacVoiceH323GwAdmRejCallerNotRegistered": oacVoiceH323GwAdmRejCallerNotRegistered,
       "oacVoiceH323GwAdmRejResourceUnavailable": oacVoiceH323GwAdmRejResourceUnavailable,
       "oacVoiceH323GwAdmRejSecurityDenial": oacVoiceH323GwAdmRejSecurityDenial,
       "oacVoiceH323GwAdmRejInvalidEndpointIdent": oacVoiceH323GwAdmRejInvalidEndpointIdent,
       "oacVoiceH323GwAdmRejIncompleteAddress": oacVoiceH323GwAdmRejIncompleteAddress,
       "oacVoiceH323GwAdmRejNotSpecified": oacVoiceH323GwAdmRejNotSpecified,
       "oacVoiceH323GwAdmRejUndefinedReason": oacVoiceH323GwAdmRejUndefinedReason,
       "oacVoiceSipGw": oacVoiceSipGw,
       "oacVoiceSipGwState": oacVoiceSipGwState,
       "oacVoiceSipGwRegistrationState": oacVoiceSipGwRegistrationState,
       "oacVoiceSipGwRegistrarServer": oacVoiceSipGwRegistrarServer,
       "oacVoiceSipGwBandwidth": oacVoiceSipGwBandwidth,
       "oacVoiceSipGwRegistrationErrors": oacVoiceSipGwRegistrationErrors,
       "oacVoiceSipGwRegisteredEndpoints": oacVoiceSipGwRegisteredEndpoints,
       "oacVoiceSipGwCurrentCalls": oacVoiceSipGwCurrentCalls,
       "oacVoiceSipGwAuthenticationRejects": oacVoiceSipGwAuthenticationRejects,
       "oacVoiceSipGwEndpointTable": oacVoiceSipGwEndpointTable,
       "oacVoiceSipGwEndpointEntry": oacVoiceSipGwEndpointEntry,
       "oacVoiceSipGwPhoneIndex": oacVoiceSipGwPhoneIndex,
       "oacVoiceSipGwPhoneState": oacVoiceSipGwPhoneState,
       "oacVoiceSipGwPhoneNumber": oacVoiceSipGwPhoneNumber,
       "oacVoiceSipGwPhoneSipId": oacVoiceSipGwPhoneSipId,
       "oacVoiceSipGwRegistrationTimeout": oacVoiceSipGwRegistrationTimeout,
       "oacVoiceSipGwMaxToRegisterEndpoints": oacVoiceSipGwMaxToRegisterEndpoints,
       "oacVoiceSipServer": oacVoiceSipServer,
       "oacVoiceSipServerState": oacVoiceSipServerState,
       "oacVoiceSipServerRegisteredEndpoints": oacVoiceSipServerRegisteredEndpoints,
       "oacVoiceSipServerRegistrarServer": oacVoiceSipServerRegistrarServer,
       "oacVoiceSipServerCurrentCalls": oacVoiceSipServerCurrentCalls,
       "oacVoiceSipServerEndpointTable": oacVoiceSipServerEndpointTable,
       "oacVoiceSipServerEndpointEntry": oacVoiceSipServerEndpointEntry,
       "oacVoiceSipServerPhoneIndex": oacVoiceSipServerPhoneIndex,
       "oacVoiceSipServerPhoneNumber": oacVoiceSipServerPhoneNumber,
       "oacVoiceSipServerPhoneIpAddress": oacVoiceSipServerPhoneIpAddress,
       "oacVoiceSipServerPhoneSipId": oacVoiceSipServerPhoneSipId,
       "oacVoiceSipServerRegistrationTime": oacVoiceSipServerRegistrationTime,
       "oacVoiceSipServerRegistrationTimeout": oacVoiceSipServerRegistrationTimeout,
       "oacVoiceMgcpGw": oacVoiceMgcpGw,
       "oacVoiceMgcpGwState": oacVoiceMgcpGwState,
       "oacVoiceMgcpGwCallAgentIpAddress": oacVoiceMgcpGwCallAgentIpAddress,
       "oacVoiceMgcpGwConnectionState": oacVoiceMgcpGwConnectionState,
       "oacVoiceMgcpGwEstablishedPathCurrentNumber": oacVoiceMgcpGwEstablishedPathCurrentNumber,
       "oacVoiceMgcpGwOutCallsOffHookEvents": oacVoiceMgcpGwOutCallsOffHookEvents,
       "oacVoiceMgcpGwOutCallsPathEstablished": oacVoiceMgcpGwOutCallsPathEstablished,
       "oacVoiceMgcpGwIncCallsRingingEvents": oacVoiceMgcpGwIncCallsRingingEvents,
       "oacVoiceMgcpGwIncCallsPath": oacVoiceMgcpGwIncCallsPath,
       "oacVoiceStatMos": oacVoiceStatMos,
       "oacVoiceStatMosTable": oacVoiceStatMosTable,
       "oacVoiceStatMosEntry": oacVoiceStatMosEntry,
       "oacVoiceStatMosIndex": oacVoiceStatMosIndex,
       "oacVoiceStatMosEntryNumberOfCalls": oacVoiceStatMosEntryNumberOfCalls,
       "oacVoiceStatMosEntryMosAvg": oacVoiceStatMosEntryMosAvg,
       "oacVoiceStatMosEntryMosMin": oacVoiceStatMosEntryMosMin,
       "oacVoiceStatMosEntryMosMax": oacVoiceStatMosEntryMosMax,
       "oacVoiceStatMosEntryErlAvg": oacVoiceStatMosEntryErlAvg,
       "oacVoiceStatMosEntryAcomAvg": oacVoiceStatMosEntryAcomAvg,
       "oacVoiceStatMosEntryLossRateAvg": oacVoiceStatMosEntryLossRateAvg,
       "oacVoiceStatMosJitterAvg": oacVoiceStatMosJitterAvg,
       "oacVoiceStatMosEntryMaxDelayAvg": oacVoiceStatMosEntryMaxDelayAvg,
       "oacVoiceStatMosEntryPddAvg": oacVoiceStatMosEntryPddAvg,
       "oacVoiceStatNotifications": oacVoiceStatNotifications,
       "oacVoiceStatConformance": oacVoiceStatConformance,
       "oacVoiceStatGroups": oacVoiceStatGroups,
       "oacVoiceStatGeneralGroup": oacVoiceStatGeneralGroup,
       "oacVoiceStatCompliances": oacVoiceStatCompliances,
       "oacVoiceStatCompliance": oacVoiceStatCompliance}
)
