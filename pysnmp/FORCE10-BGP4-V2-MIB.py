# SNMP MIB module (FORCE10-BGP4-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORCE10-BGP4-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:22 2024
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

(f10Experiment,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Experiment")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber",
    "InetPortNumber")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

f10BgpM2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1)
)
f10BgpM2.setRevisions(
        ("2007-04-27 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class F10BgpM2Identifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class F10BgpM2Afi(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class F10BgpM2Safi(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class F10BgpM2Community(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class F10BgpM2ExtendedCommunity(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_F10BgpM2BaseScalars_ObjectIdentity = ObjectIdentity
f10BgpM2BaseScalars = _F10BgpM2BaseScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1)
)
_F10BgpM2BaseNotifications_ObjectIdentity = ObjectIdentity
f10BgpM2BaseNotifications = _F10BgpM2BaseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 0)
)
_F10BgpM2Version_ObjectIdentity = ObjectIdentity
f10BgpM2Version = _F10BgpM2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 1)
)
_F10BgpM2VersionTable_Object = MibTable
f10BgpM2VersionTable = _F10BgpM2VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2VersionTable.setStatus("current")
_F10BgpM2VersionEntry_Object = MibTableRow
f10BgpM2VersionEntry = _F10BgpM2VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 1, 1, 1)
)
f10BgpM2VersionEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2VersionIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2VersionEntry.setStatus("current")


class _F10BgpM2VersionIndex_Type(Unsigned32):
    """Custom type f10BgpM2VersionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F10BgpM2VersionIndex_Type.__name__ = "Unsigned32"
_F10BgpM2VersionIndex_Object = MibTableColumn
f10BgpM2VersionIndex = _F10BgpM2VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 1, 1, 1, 1),
    _F10BgpM2VersionIndex_Type()
)
f10BgpM2VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2VersionIndex.setStatus("current")
_F10BgpM2VersionSupported_Type = TruthValue
_F10BgpM2VersionSupported_Object = MibTableColumn
f10BgpM2VersionSupported = _F10BgpM2VersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 1, 1, 1, 2),
    _F10BgpM2VersionSupported_Type()
)
f10BgpM2VersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2VersionSupported.setStatus("current")
_F10BgpM2SupportedCapabilities_ObjectIdentity = ObjectIdentity
f10BgpM2SupportedCapabilities = _F10BgpM2SupportedCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2)
)
_F10BgpM2CapabilitySupportAvailable_Type = TruthValue
_F10BgpM2CapabilitySupportAvailable_Object = MibScalar
f10BgpM2CapabilitySupportAvailable = _F10BgpM2CapabilitySupportAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2, 1),
    _F10BgpM2CapabilitySupportAvailable_Type()
)
f10BgpM2CapabilitySupportAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2CapabilitySupportAvailable.setStatus("current")
_F10BgpM2SupportedCapabilitiesTable_Object = MibTable
f10BgpM2SupportedCapabilitiesTable = _F10BgpM2SupportedCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    f10BgpM2SupportedCapabilitiesTable.setStatus("current")
_F10BgpM2SupportedCapabilitiesEntry_Object = MibTableRow
f10BgpM2SupportedCapabilitiesEntry = _F10BgpM2SupportedCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2, 2, 1)
)
f10BgpM2SupportedCapabilitiesEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2SupportedCapabilityCode"),
)
if mibBuilder.loadTexts:
    f10BgpM2SupportedCapabilitiesEntry.setStatus("current")


class _F10BgpM2SupportedCapabilityCode_Type(Unsigned32):
    """Custom type f10BgpM2SupportedCapabilityCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F10BgpM2SupportedCapabilityCode_Type.__name__ = "Unsigned32"
_F10BgpM2SupportedCapabilityCode_Object = MibTableColumn
f10BgpM2SupportedCapabilityCode = _F10BgpM2SupportedCapabilityCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2, 2, 1, 1),
    _F10BgpM2SupportedCapabilityCode_Type()
)
f10BgpM2SupportedCapabilityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2SupportedCapabilityCode.setStatus("current")
_F10BgpM2SupportedCapability_Type = TruthValue
_F10BgpM2SupportedCapability_Object = MibTableColumn
f10BgpM2SupportedCapability = _F10BgpM2SupportedCapability_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2, 2, 1, 2),
    _F10BgpM2SupportedCapability_Type()
)
f10BgpM2SupportedCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2SupportedCapability.setStatus("current")


class _F10BgpM2AsSize_Type(Integer32):
    """Custom type f10BgpM2AsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourOctet", 2),
          ("twoOctet", 1))
    )


_F10BgpM2AsSize_Type.__name__ = "Integer32"
_F10BgpM2AsSize_Object = MibScalar
f10BgpM2AsSize = _F10BgpM2AsSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 4),
    _F10BgpM2AsSize_Type()
)
f10BgpM2AsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsSize.setStatus("current")
_F10BgpM2LocalAs_Type = InetAutonomousSystemNumber
_F10BgpM2LocalAs_Object = MibScalar
f10BgpM2LocalAs = _F10BgpM2LocalAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 5),
    _F10BgpM2LocalAs_Type()
)
f10BgpM2LocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2LocalAs.setStatus("current")
_F10BgpM2LocalIdentifier_Type = F10BgpM2Identifier
_F10BgpM2LocalIdentifier_Object = MibScalar
f10BgpM2LocalIdentifier = _F10BgpM2LocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 6),
    _F10BgpM2LocalIdentifier_Type()
)
f10BgpM2LocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2LocalIdentifier.setStatus("current")
_F10BgpM2BaseScalarExtensions_ObjectIdentity = ObjectIdentity
f10BgpM2BaseScalarExtensions = _F10BgpM2BaseScalarExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7)
)
_F10BgpM2BaseScalarNonCapExts_ObjectIdentity = ObjectIdentity
f10BgpM2BaseScalarNonCapExts = _F10BgpM2BaseScalarNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1)
)
_F10BgpM2BaseScalarRouteReflectExts_ObjectIdentity = ObjectIdentity
f10BgpM2BaseScalarRouteReflectExts = _F10BgpM2BaseScalarRouteReflectExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 2796)
)
_F10BgpM2RouteReflector_Type = TruthValue
_F10BgpM2RouteReflector_Object = MibScalar
f10BgpM2RouteReflector = _F10BgpM2RouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 2796, 1),
    _F10BgpM2RouteReflector_Type()
)
f10BgpM2RouteReflector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2RouteReflector.setStatus("current")
_F10BgpM2ClusterId_Type = F10BgpM2Identifier
_F10BgpM2ClusterId_Object = MibScalar
f10BgpM2ClusterId = _F10BgpM2ClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 2796, 2),
    _F10BgpM2ClusterId_Type()
)
f10BgpM2ClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2ClusterId.setStatus("current")
_F10BgpM2BaseScalarASConfedExts_ObjectIdentity = ObjectIdentity
f10BgpM2BaseScalarASConfedExts = _F10BgpM2BaseScalarASConfedExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 3065)
)
_F10BgpM2ConfederationRouter_Type = TruthValue
_F10BgpM2ConfederationRouter_Object = MibScalar
f10BgpM2ConfederationRouter = _F10BgpM2ConfederationRouter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 3065, 1),
    _F10BgpM2ConfederationRouter_Type()
)
f10BgpM2ConfederationRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2ConfederationRouter.setStatus("current")
_F10BgpM2ConfederationId_Type = InetAutonomousSystemNumber
_F10BgpM2ConfederationId_Object = MibScalar
f10BgpM2ConfederationId = _F10BgpM2ConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 3065, 2),
    _F10BgpM2ConfederationId_Type()
)
f10BgpM2ConfederationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2ConfederationId.setStatus("current")
_F10BgpM2BaseScalarCapExts_ObjectIdentity = ObjectIdentity
f10BgpM2BaseScalarCapExts = _F10BgpM2BaseScalarCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 2)
)
_F10BgpM2BaseScalarConfiguration_ObjectIdentity = ObjectIdentity
f10BgpM2BaseScalarConfiguration = _F10BgpM2BaseScalarConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8)
)
_F10BgpM2CfgBaseScalarStorageType_Type = StorageType
_F10BgpM2CfgBaseScalarStorageType_Object = MibScalar
f10BgpM2CfgBaseScalarStorageType = _F10BgpM2CfgBaseScalarStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 1),
    _F10BgpM2CfgBaseScalarStorageType_Type()
)
f10BgpM2CfgBaseScalarStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10BgpM2CfgBaseScalarStorageType.setStatus("current")
_F10BgpM2CfgLocalAs_Type = InetAutonomousSystemNumber
_F10BgpM2CfgLocalAs_Object = MibScalar
f10BgpM2CfgLocalAs = _F10BgpM2CfgLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 2),
    _F10BgpM2CfgLocalAs_Type()
)
f10BgpM2CfgLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10BgpM2CfgLocalAs.setStatus("current")
_F10BgpM2CfgLocalIdentifier_Type = F10BgpM2Identifier
_F10BgpM2CfgLocalIdentifier_Object = MibScalar
f10BgpM2CfgLocalIdentifier = _F10BgpM2CfgLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 3),
    _F10BgpM2CfgLocalIdentifier_Type()
)
f10BgpM2CfgLocalIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10BgpM2CfgLocalIdentifier.setStatus("current")
_F10BgpM2CfgBaseScalarExtensions_ObjectIdentity = ObjectIdentity
f10BgpM2CfgBaseScalarExtensions = _F10BgpM2CfgBaseScalarExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4)
)
_F10BgpM2CfgBaseScalarNonCapExts_ObjectIdentity = ObjectIdentity
f10BgpM2CfgBaseScalarNonCapExts = _F10BgpM2CfgBaseScalarNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1)
)
_F10BgpM2CfgBaseScalarReflectorExts_ObjectIdentity = ObjectIdentity
f10BgpM2CfgBaseScalarReflectorExts = _F10BgpM2CfgBaseScalarReflectorExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 2796)
)
_F10BgpM2CfgRouteReflector_Type = TruthValue
_F10BgpM2CfgRouteReflector_Object = MibScalar
f10BgpM2CfgRouteReflector = _F10BgpM2CfgRouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 2796, 1),
    _F10BgpM2CfgRouteReflector_Type()
)
f10BgpM2CfgRouteReflector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10BgpM2CfgRouteReflector.setStatus("current")
_F10BgpM2CfgClusterId_Type = F10BgpM2Identifier
_F10BgpM2CfgClusterId_Object = MibScalar
f10BgpM2CfgClusterId = _F10BgpM2CfgClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 2796, 2),
    _F10BgpM2CfgClusterId_Type()
)
f10BgpM2CfgClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10BgpM2CfgClusterId.setStatus("current")
_F10BgpM2CfgBaseScalarASConfedExts_ObjectIdentity = ObjectIdentity
f10BgpM2CfgBaseScalarASConfedExts = _F10BgpM2CfgBaseScalarASConfedExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 3065)
)
_F10BgpM2CfgConfederationRouter_Type = TruthValue
_F10BgpM2CfgConfederationRouter_Object = MibScalar
f10BgpM2CfgConfederationRouter = _F10BgpM2CfgConfederationRouter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 3065, 1),
    _F10BgpM2CfgConfederationRouter_Type()
)
f10BgpM2CfgConfederationRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10BgpM2CfgConfederationRouter.setStatus("current")
_F10BgpM2CfgConfederationId_Type = InetAutonomousSystemNumber
_F10BgpM2CfgConfederationId_Object = MibScalar
f10BgpM2CfgConfederationId = _F10BgpM2CfgConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 3065, 2),
    _F10BgpM2CfgConfederationId_Type()
)
f10BgpM2CfgConfederationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10BgpM2CfgConfederationId.setStatus("current")
_F10BgpM2CfgBaseScalarCapExts_ObjectIdentity = ObjectIdentity
f10BgpM2CfgBaseScalarCapExts = _F10BgpM2CfgBaseScalarCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 2)
)
_F10BgpM2Peer_ObjectIdentity = ObjectIdentity
f10BgpM2Peer = _F10BgpM2Peer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2)
)
_F10BgpM2PeerData_ObjectIdentity = ObjectIdentity
f10BgpM2PeerData = _F10BgpM2PeerData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1)
)
_F10BgpM2PeerTable_Object = MibTable
f10BgpM2PeerTable = _F10BgpM2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerTable.setStatus("current")
_F10BgpM2PeerEntry_Object = MibTableRow
f10BgpM2PeerEntry = _F10BgpM2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1)
)
f10BgpM2PeerEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerInstance"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLocalAddrType"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLocalAddr"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerRemoteAddrType"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    f10BgpM2PeerEntry.setStatus("current")
_F10BgpM2PeerInstance_Type = Unsigned32
_F10BgpM2PeerInstance_Object = MibTableColumn
f10BgpM2PeerInstance = _F10BgpM2PeerInstance_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 1),
    _F10BgpM2PeerInstance_Type()
)
f10BgpM2PeerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerInstance.setStatus("current")
_F10BgpM2PeerIdentifier_Type = F10BgpM2Identifier
_F10BgpM2PeerIdentifier_Object = MibTableColumn
f10BgpM2PeerIdentifier = _F10BgpM2PeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 2),
    _F10BgpM2PeerIdentifier_Type()
)
f10BgpM2PeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerIdentifier.setStatus("current")


class _F10BgpM2PeerState_Type(Integer32):
    """Custom type f10BgpM2PeerState based on Integer32"""
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
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openconfirm", 5),
          ("opensent", 4))
    )


_F10BgpM2PeerState_Type.__name__ = "Integer32"
_F10BgpM2PeerState_Object = MibTableColumn
f10BgpM2PeerState = _F10BgpM2PeerState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 3),
    _F10BgpM2PeerState_Type()
)
f10BgpM2PeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerState.setStatus("current")


class _F10BgpM2PeerStatus_Type(Integer32):
    """Custom type f10BgpM2PeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halted", 1),
          ("running", 2))
    )


_F10BgpM2PeerStatus_Type.__name__ = "Integer32"
_F10BgpM2PeerStatus_Object = MibTableColumn
f10BgpM2PeerStatus = _F10BgpM2PeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 4),
    _F10BgpM2PeerStatus_Type()
)
f10BgpM2PeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerStatus.setStatus("current")


class _F10BgpM2PeerConfiguredVersion_Type(Unsigned32):
    """Custom type f10BgpM2PeerConfiguredVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F10BgpM2PeerConfiguredVersion_Type.__name__ = "Unsigned32"
_F10BgpM2PeerConfiguredVersion_Object = MibTableColumn
f10BgpM2PeerConfiguredVersion = _F10BgpM2PeerConfiguredVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 5),
    _F10BgpM2PeerConfiguredVersion_Type()
)
f10BgpM2PeerConfiguredVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerConfiguredVersion.setStatus("current")


class _F10BgpM2PeerNegotiatedVersion_Type(Unsigned32):
    """Custom type f10BgpM2PeerNegotiatedVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F10BgpM2PeerNegotiatedVersion_Type.__name__ = "Unsigned32"
_F10BgpM2PeerNegotiatedVersion_Object = MibTableColumn
f10BgpM2PeerNegotiatedVersion = _F10BgpM2PeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 6),
    _F10BgpM2PeerNegotiatedVersion_Type()
)
f10BgpM2PeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerNegotiatedVersion.setStatus("current")
_F10BgpM2PeerLocalAddrType_Type = InetAddressType
_F10BgpM2PeerLocalAddrType_Object = MibTableColumn
f10BgpM2PeerLocalAddrType = _F10BgpM2PeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 7),
    _F10BgpM2PeerLocalAddrType_Type()
)
f10BgpM2PeerLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLocalAddrType.setStatus("current")


class _F10BgpM2PeerLocalAddr_Type(InetAddress):
    """Custom type f10BgpM2PeerLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_F10BgpM2PeerLocalAddr_Type.__name__ = "InetAddress"
_F10BgpM2PeerLocalAddr_Object = MibTableColumn
f10BgpM2PeerLocalAddr = _F10BgpM2PeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 8),
    _F10BgpM2PeerLocalAddr_Type()
)
f10BgpM2PeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLocalAddr.setStatus("current")
_F10BgpM2PeerLocalPort_Type = InetPortNumber
_F10BgpM2PeerLocalPort_Object = MibTableColumn
f10BgpM2PeerLocalPort = _F10BgpM2PeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 9),
    _F10BgpM2PeerLocalPort_Type()
)
f10BgpM2PeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLocalPort.setStatus("current")
_F10BgpM2PeerLocalAs_Type = InetAutonomousSystemNumber
_F10BgpM2PeerLocalAs_Object = MibTableColumn
f10BgpM2PeerLocalAs = _F10BgpM2PeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 10),
    _F10BgpM2PeerLocalAs_Type()
)
f10BgpM2PeerLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLocalAs.setStatus("current")
_F10BgpM2PeerRemoteAddrType_Type = InetAddressType
_F10BgpM2PeerRemoteAddrType_Object = MibTableColumn
f10BgpM2PeerRemoteAddrType = _F10BgpM2PeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 11),
    _F10BgpM2PeerRemoteAddrType_Type()
)
f10BgpM2PeerRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerRemoteAddrType.setStatus("current")


class _F10BgpM2PeerRemoteAddr_Type(InetAddress):
    """Custom type f10BgpM2PeerRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_F10BgpM2PeerRemoteAddr_Type.__name__ = "InetAddress"
_F10BgpM2PeerRemoteAddr_Object = MibTableColumn
f10BgpM2PeerRemoteAddr = _F10BgpM2PeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 12),
    _F10BgpM2PeerRemoteAddr_Type()
)
f10BgpM2PeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerRemoteAddr.setStatus("current")
_F10BgpM2PeerRemotePort_Type = InetPortNumber
_F10BgpM2PeerRemotePort_Object = MibTableColumn
f10BgpM2PeerRemotePort = _F10BgpM2PeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 13),
    _F10BgpM2PeerRemotePort_Type()
)
f10BgpM2PeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerRemotePort.setStatus("current")
_F10BgpM2PeerRemoteAs_Type = InetAutonomousSystemNumber
_F10BgpM2PeerRemoteAs_Object = MibTableColumn
f10BgpM2PeerRemoteAs = _F10BgpM2PeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 14),
    _F10BgpM2PeerRemoteAs_Type()
)
f10BgpM2PeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerRemoteAs.setStatus("current")
_F10BgpM2PeerIndex_Type = Unsigned32
_F10BgpM2PeerIndex_Object = MibTableColumn
f10BgpM2PeerIndex = _F10BgpM2PeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 15),
    _F10BgpM2PeerIndex_Type()
)
f10BgpM2PeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerIndex.setStatus("current")
_F10BgpM2PeerErrors_ObjectIdentity = ObjectIdentity
f10BgpM2PeerErrors = _F10BgpM2PeerErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2)
)
_F10BgpM2PeerErrorsTable_Object = MibTable
f10BgpM2PeerErrorsTable = _F10BgpM2PeerErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerErrorsTable.setStatus("current")
_F10BgpM2PeerErrorsEntry_Object = MibTableRow
f10BgpM2PeerErrorsEntry = _F10BgpM2PeerErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerErrorsEntry.setStatus("current")


class _F10BgpM2PeerLastErrorReceived_Type(OctetString):
    """Custom type f10BgpM2PeerLastErrorReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_F10BgpM2PeerLastErrorReceived_Type.__name__ = "OctetString"
_F10BgpM2PeerLastErrorReceived_Object = MibTableColumn
f10BgpM2PeerLastErrorReceived = _F10BgpM2PeerLastErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 1),
    _F10BgpM2PeerLastErrorReceived_Type()
)
f10BgpM2PeerLastErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLastErrorReceived.setStatus("current")


class _F10BgpM2PeerLastErrorSent_Type(OctetString):
    """Custom type f10BgpM2PeerLastErrorSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_F10BgpM2PeerLastErrorSent_Type.__name__ = "OctetString"
_F10BgpM2PeerLastErrorSent_Object = MibTableColumn
f10BgpM2PeerLastErrorSent = _F10BgpM2PeerLastErrorSent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 2),
    _F10BgpM2PeerLastErrorSent_Type()
)
f10BgpM2PeerLastErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLastErrorSent.setStatus("current")
_F10BgpM2PeerLastErrorReceivedTime_Type = TimeTicks
_F10BgpM2PeerLastErrorReceivedTime_Object = MibTableColumn
f10BgpM2PeerLastErrorReceivedTime = _F10BgpM2PeerLastErrorReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 3),
    _F10BgpM2PeerLastErrorReceivedTime_Type()
)
f10BgpM2PeerLastErrorReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLastErrorReceivedTime.setStatus("current")
_F10BgpM2PeerLastErrorSentTime_Type = TimeTicks
_F10BgpM2PeerLastErrorSentTime_Object = MibTableColumn
f10BgpM2PeerLastErrorSentTime = _F10BgpM2PeerLastErrorSentTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 4),
    _F10BgpM2PeerLastErrorSentTime_Type()
)
f10BgpM2PeerLastErrorSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLastErrorSentTime.setStatus("current")
_F10BgpM2PeerLastErrorReceivedText_Type = SnmpAdminString
_F10BgpM2PeerLastErrorReceivedText_Object = MibTableColumn
f10BgpM2PeerLastErrorReceivedText = _F10BgpM2PeerLastErrorReceivedText_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 5),
    _F10BgpM2PeerLastErrorReceivedText_Type()
)
f10BgpM2PeerLastErrorReceivedText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLastErrorReceivedText.setStatus("current")
_F10BgpM2PeerLastErrorSentText_Type = SnmpAdminString
_F10BgpM2PeerLastErrorSentText_Object = MibTableColumn
f10BgpM2PeerLastErrorSentText = _F10BgpM2PeerLastErrorSentText_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 6),
    _F10BgpM2PeerLastErrorSentText_Type()
)
f10BgpM2PeerLastErrorSentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLastErrorSentText.setStatus("current")


class _F10BgpM2PeerLastErrorReceivedData_Type(OctetString):
    """Custom type f10BgpM2PeerLastErrorReceivedData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_F10BgpM2PeerLastErrorReceivedData_Type.__name__ = "OctetString"
_F10BgpM2PeerLastErrorReceivedData_Object = MibTableColumn
f10BgpM2PeerLastErrorReceivedData = _F10BgpM2PeerLastErrorReceivedData_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 7),
    _F10BgpM2PeerLastErrorReceivedData_Type()
)
f10BgpM2PeerLastErrorReceivedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLastErrorReceivedData.setStatus("current")


class _F10BgpM2PeerLastErrorSentData_Type(OctetString):
    """Custom type f10BgpM2PeerLastErrorSentData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_F10BgpM2PeerLastErrorSentData_Type.__name__ = "OctetString"
_F10BgpM2PeerLastErrorSentData_Object = MibTableColumn
f10BgpM2PeerLastErrorSentData = _F10BgpM2PeerLastErrorSentData_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 8),
    _F10BgpM2PeerLastErrorSentData_Type()
)
f10BgpM2PeerLastErrorSentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerLastErrorSentData.setStatus("current")
_F10BgpM2PeerTimers_ObjectIdentity = ObjectIdentity
f10BgpM2PeerTimers = _F10BgpM2PeerTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3)
)
_F10BgpM2PeerEventTimesTable_Object = MibTable
f10BgpM2PeerEventTimesTable = _F10BgpM2PeerEventTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerEventTimesTable.setStatus("current")
_F10BgpM2PeerEventTimesEntry_Object = MibTableRow
f10BgpM2PeerEventTimesEntry = _F10BgpM2PeerEventTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerEventTimesEntry.setStatus("current")
_F10BgpM2PeerFsmEstablishedTime_Type = Gauge32
_F10BgpM2PeerFsmEstablishedTime_Object = MibTableColumn
f10BgpM2PeerFsmEstablishedTime = _F10BgpM2PeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 1, 1, 1),
    _F10BgpM2PeerFsmEstablishedTime_Type()
)
f10BgpM2PeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerFsmEstablishedTime.setStatus("current")
_F10BgpM2PeerInUpdatesElapsedTime_Type = Gauge32
_F10BgpM2PeerInUpdatesElapsedTime_Object = MibTableColumn
f10BgpM2PeerInUpdatesElapsedTime = _F10BgpM2PeerInUpdatesElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 1, 1, 2),
    _F10BgpM2PeerInUpdatesElapsedTime_Type()
)
f10BgpM2PeerInUpdatesElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerInUpdatesElapsedTime.setStatus("current")
_F10BgpM2PeerConfiguredTimersTable_Object = MibTable
f10BgpM2PeerConfiguredTimersTable = _F10BgpM2PeerConfiguredTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerConfiguredTimersTable.setStatus("current")
_F10BgpM2PeerConfiguredTimersEntry_Object = MibTableRow
f10BgpM2PeerConfiguredTimersEntry = _F10BgpM2PeerConfiguredTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerConfiguredTimersEntry.setStatus("current")


class _F10BgpM2PeerConnectRetryInterval_Type(Unsigned32):
    """Custom type f10BgpM2PeerConnectRetryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F10BgpM2PeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_F10BgpM2PeerConnectRetryInterval_Object = MibTableColumn
f10BgpM2PeerConnectRetryInterval = _F10BgpM2PeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1, 1),
    _F10BgpM2PeerConnectRetryInterval_Type()
)
f10BgpM2PeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerConnectRetryInterval.setStatus("current")


class _F10BgpM2PeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type f10BgpM2PeerHoldTimeConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_F10BgpM2PeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_F10BgpM2PeerHoldTimeConfigured_Object = MibTableColumn
f10BgpM2PeerHoldTimeConfigured = _F10BgpM2PeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1, 2),
    _F10BgpM2PeerHoldTimeConfigured_Type()
)
f10BgpM2PeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerHoldTimeConfigured.setStatus("current")


class _F10BgpM2PeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type f10BgpM2PeerKeepAliveConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_F10BgpM2PeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_F10BgpM2PeerKeepAliveConfigured_Object = MibTableColumn
f10BgpM2PeerKeepAliveConfigured = _F10BgpM2PeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1, 3),
    _F10BgpM2PeerKeepAliveConfigured_Type()
)
f10BgpM2PeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerKeepAliveConfigured.setStatus("current")


class _F10BgpM2PeerMinASOrigInterval_Type(Unsigned32):
    """Custom type f10BgpM2PeerMinASOrigInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_F10BgpM2PeerMinASOrigInterval_Type.__name__ = "Unsigned32"
_F10BgpM2PeerMinASOrigInterval_Object = MibTableColumn
f10BgpM2PeerMinASOrigInterval = _F10BgpM2PeerMinASOrigInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1, 4),
    _F10BgpM2PeerMinASOrigInterval_Type()
)
f10BgpM2PeerMinASOrigInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerMinASOrigInterval.setStatus("current")


class _F10BgpM2PeerMinRouteAdverInterval_Type(Unsigned32):
    """Custom type f10BgpM2PeerMinRouteAdverInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_F10BgpM2PeerMinRouteAdverInterval_Type.__name__ = "Unsigned32"
_F10BgpM2PeerMinRouteAdverInterval_Object = MibTableColumn
f10BgpM2PeerMinRouteAdverInterval = _F10BgpM2PeerMinRouteAdverInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1, 5),
    _F10BgpM2PeerMinRouteAdverInterval_Type()
)
f10BgpM2PeerMinRouteAdverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerMinRouteAdverInterval.setStatus("current")
_F10BgpM2PeerNegotiatedTimersTable_Object = MibTable
f10BgpM2PeerNegotiatedTimersTable = _F10BgpM2PeerNegotiatedTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerNegotiatedTimersTable.setStatus("current")
_F10BgpM2PeerNegotiatedTimersEntry_Object = MibTableRow
f10BgpM2PeerNegotiatedTimersEntry = _F10BgpM2PeerNegotiatedTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerNegotiatedTimersEntry.setStatus("current")


class _F10BgpM2PeerHoldTime_Type(Unsigned32):
    """Custom type f10BgpM2PeerHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_F10BgpM2PeerHoldTime_Type.__name__ = "Unsigned32"
_F10BgpM2PeerHoldTime_Object = MibTableColumn
f10BgpM2PeerHoldTime = _F10BgpM2PeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 3, 1, 1),
    _F10BgpM2PeerHoldTime_Type()
)
f10BgpM2PeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerHoldTime.setStatus("current")


class _F10BgpM2PeerKeepAlive_Type(Unsigned32):
    """Custom type f10BgpM2PeerKeepAlive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_F10BgpM2PeerKeepAlive_Type.__name__ = "Unsigned32"
_F10BgpM2PeerKeepAlive_Object = MibTableColumn
f10BgpM2PeerKeepAlive = _F10BgpM2PeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 3, 1, 2),
    _F10BgpM2PeerKeepAlive_Type()
)
f10BgpM2PeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerKeepAlive.setStatus("current")
_F10BgpM2PeerCapabilities_ObjectIdentity = ObjectIdentity
f10BgpM2PeerCapabilities = _F10BgpM2PeerCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4)
)
_F10BgpM2PeerCapsAnnouncedTable_Object = MibTable
f10BgpM2PeerCapsAnnouncedTable = _F10BgpM2PeerCapsAnnouncedTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerCapsAnnouncedTable.setStatus("current")
_F10BgpM2PeerCapsAnnouncedEntry_Object = MibTableRow
f10BgpM2PeerCapsAnnouncedEntry = _F10BgpM2PeerCapsAnnouncedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 1, 1)
)
f10BgpM2PeerCapsAnnouncedEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerCapAnnouncedCode"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerCapAnnouncedIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2PeerCapsAnnouncedEntry.setStatus("current")


class _F10BgpM2PeerCapAnnouncedCode_Type(Unsigned32):
    """Custom type f10BgpM2PeerCapAnnouncedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F10BgpM2PeerCapAnnouncedCode_Type.__name__ = "Unsigned32"
_F10BgpM2PeerCapAnnouncedCode_Object = MibTableColumn
f10BgpM2PeerCapAnnouncedCode = _F10BgpM2PeerCapAnnouncedCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 1, 1, 1),
    _F10BgpM2PeerCapAnnouncedCode_Type()
)
f10BgpM2PeerCapAnnouncedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerCapAnnouncedCode.setStatus("current")


class _F10BgpM2PeerCapAnnouncedIndex_Type(Unsigned32):
    """Custom type f10BgpM2PeerCapAnnouncedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_F10BgpM2PeerCapAnnouncedIndex_Type.__name__ = "Unsigned32"
_F10BgpM2PeerCapAnnouncedIndex_Object = MibTableColumn
f10BgpM2PeerCapAnnouncedIndex = _F10BgpM2PeerCapAnnouncedIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 1, 1, 2),
    _F10BgpM2PeerCapAnnouncedIndex_Type()
)
f10BgpM2PeerCapAnnouncedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerCapAnnouncedIndex.setStatus("current")


class _F10BgpM2PeerCapAnnouncedValue_Type(OctetString):
    """Custom type f10BgpM2PeerCapAnnouncedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F10BgpM2PeerCapAnnouncedValue_Type.__name__ = "OctetString"
_F10BgpM2PeerCapAnnouncedValue_Object = MibTableColumn
f10BgpM2PeerCapAnnouncedValue = _F10BgpM2PeerCapAnnouncedValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 1, 1, 3),
    _F10BgpM2PeerCapAnnouncedValue_Type()
)
f10BgpM2PeerCapAnnouncedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerCapAnnouncedValue.setStatus("current")
_F10BgpM2PeerCapsReceivedTable_Object = MibTable
f10BgpM2PeerCapsReceivedTable = _F10BgpM2PeerCapsReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerCapsReceivedTable.setStatus("current")
_F10BgpM2PeerCapsReceivedEntry_Object = MibTableRow
f10BgpM2PeerCapsReceivedEntry = _F10BgpM2PeerCapsReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 2, 1)
)
f10BgpM2PeerCapsReceivedEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerCapReceivedCode"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerCapReceivedIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2PeerCapsReceivedEntry.setStatus("current")


class _F10BgpM2PeerCapReceivedCode_Type(Unsigned32):
    """Custom type f10BgpM2PeerCapReceivedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F10BgpM2PeerCapReceivedCode_Type.__name__ = "Unsigned32"
_F10BgpM2PeerCapReceivedCode_Object = MibTableColumn
f10BgpM2PeerCapReceivedCode = _F10BgpM2PeerCapReceivedCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 2, 1, 1),
    _F10BgpM2PeerCapReceivedCode_Type()
)
f10BgpM2PeerCapReceivedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerCapReceivedCode.setStatus("current")


class _F10BgpM2PeerCapReceivedIndex_Type(Unsigned32):
    """Custom type f10BgpM2PeerCapReceivedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_F10BgpM2PeerCapReceivedIndex_Type.__name__ = "Unsigned32"
_F10BgpM2PeerCapReceivedIndex_Object = MibTableColumn
f10BgpM2PeerCapReceivedIndex = _F10BgpM2PeerCapReceivedIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 2, 1, 2),
    _F10BgpM2PeerCapReceivedIndex_Type()
)
f10BgpM2PeerCapReceivedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerCapReceivedIndex.setStatus("current")


class _F10BgpM2PeerCapReceivedValue_Type(OctetString):
    """Custom type f10BgpM2PeerCapReceivedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F10BgpM2PeerCapReceivedValue_Type.__name__ = "OctetString"
_F10BgpM2PeerCapReceivedValue_Object = MibTableColumn
f10BgpM2PeerCapReceivedValue = _F10BgpM2PeerCapReceivedValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 2, 1, 3),
    _F10BgpM2PeerCapReceivedValue_Type()
)
f10BgpM2PeerCapReceivedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerCapReceivedValue.setStatus("current")
_F10BgpM2PeerCounters_ObjectIdentity = ObjectIdentity
f10BgpM2PeerCounters = _F10BgpM2PeerCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6)
)
_F10BgpM2PeerCountersTable_Object = MibTable
f10BgpM2PeerCountersTable = _F10BgpM2PeerCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerCountersTable.setStatus("current")
_F10BgpM2PeerCountersEntry_Object = MibTableRow
f10BgpM2PeerCountersEntry = _F10BgpM2PeerCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerCountersEntry.setStatus("current")
_F10BgpM2PeerInUpdates_Type = Counter32
_F10BgpM2PeerInUpdates_Object = MibTableColumn
f10BgpM2PeerInUpdates = _F10BgpM2PeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 1),
    _F10BgpM2PeerInUpdates_Type()
)
f10BgpM2PeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerInUpdates.setStatus("current")
_F10BgpM2PeerOutUpdates_Type = Counter32
_F10BgpM2PeerOutUpdates_Object = MibTableColumn
f10BgpM2PeerOutUpdates = _F10BgpM2PeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 2),
    _F10BgpM2PeerOutUpdates_Type()
)
f10BgpM2PeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerOutUpdates.setStatus("current")
_F10BgpM2PeerInTotalMessages_Type = Counter32
_F10BgpM2PeerInTotalMessages_Object = MibTableColumn
f10BgpM2PeerInTotalMessages = _F10BgpM2PeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 3),
    _F10BgpM2PeerInTotalMessages_Type()
)
f10BgpM2PeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerInTotalMessages.setStatus("current")
_F10BgpM2PeerOutTotalMessages_Type = Counter32
_F10BgpM2PeerOutTotalMessages_Object = MibTableColumn
f10BgpM2PeerOutTotalMessages = _F10BgpM2PeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 4),
    _F10BgpM2PeerOutTotalMessages_Type()
)
f10BgpM2PeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerOutTotalMessages.setStatus("current")
_F10BgpM2PeerFsmEstablishedTrans_Type = Counter32
_F10BgpM2PeerFsmEstablishedTrans_Object = MibTableColumn
f10BgpM2PeerFsmEstablishedTrans = _F10BgpM2PeerFsmEstablishedTrans_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 5),
    _F10BgpM2PeerFsmEstablishedTrans_Type()
)
f10BgpM2PeerFsmEstablishedTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerFsmEstablishedTrans.setStatus("current")
_F10BgpM2PeerInKeepalives_Type = Counter32
_F10BgpM2PeerInKeepalives_Object = MibTableColumn
f10BgpM2PeerInKeepalives = _F10BgpM2PeerInKeepalives_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 6),
    _F10BgpM2PeerInKeepalives_Type()
)
f10BgpM2PeerInKeepalives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerInKeepalives.setStatus("current")
_F10BgpM2PeerOutKeepalives_Type = Counter32
_F10BgpM2PeerOutKeepalives_Object = MibTableColumn
f10BgpM2PeerOutKeepalives = _F10BgpM2PeerOutKeepalives_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 7),
    _F10BgpM2PeerOutKeepalives_Type()
)
f10BgpM2PeerOutKeepalives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerOutKeepalives.setStatus("current")
_F10BgpM2PeerInOpen_Type = Counter32
_F10BgpM2PeerInOpen_Object = MibTableColumn
f10BgpM2PeerInOpen = _F10BgpM2PeerInOpen_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 8),
    _F10BgpM2PeerInOpen_Type()
)
f10BgpM2PeerInOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerInOpen.setStatus("current")
_F10BgpM2PeerOutOpen_Type = Counter32
_F10BgpM2PeerOutOpen_Object = MibTableColumn
f10BgpM2PeerOutOpen = _F10BgpM2PeerOutOpen_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 9),
    _F10BgpM2PeerOutOpen_Type()
)
f10BgpM2PeerOutOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerOutOpen.setStatus("current")
_F10BgpM2PeerInRteRefresh_Type = Counter32
_F10BgpM2PeerInRteRefresh_Object = MibTableColumn
f10BgpM2PeerInRteRefresh = _F10BgpM2PeerInRteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 10),
    _F10BgpM2PeerInRteRefresh_Type()
)
f10BgpM2PeerInRteRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerInRteRefresh.setStatus("current")
_F10BgpM2PeerOutRteRefresh_Type = Counter32
_F10BgpM2PeerOutRteRefresh_Object = MibTableColumn
f10BgpM2PeerOutRteRefresh = _F10BgpM2PeerOutRteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 11),
    _F10BgpM2PeerOutRteRefresh_Type()
)
f10BgpM2PeerOutRteRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerOutRteRefresh.setStatus("current")
_F10BgpM2PrefixCountersTable_Object = MibTable
f10BgpM2PrefixCountersTable = _F10BgpM2PrefixCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    f10BgpM2PrefixCountersTable.setStatus("current")
_F10BgpM2PrefixCountersEntry_Object = MibTableRow
f10BgpM2PrefixCountersEntry = _F10BgpM2PrefixCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1)
)
f10BgpM2PrefixCountersEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PrefixCountersAfi"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PrefixCountersSafi"),
)
if mibBuilder.loadTexts:
    f10BgpM2PrefixCountersEntry.setStatus("current")
_F10BgpM2PrefixCountersAfi_Type = F10BgpM2Afi
_F10BgpM2PrefixCountersAfi_Object = MibTableColumn
f10BgpM2PrefixCountersAfi = _F10BgpM2PrefixCountersAfi_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 1),
    _F10BgpM2PrefixCountersAfi_Type()
)
f10BgpM2PrefixCountersAfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PrefixCountersAfi.setStatus("current")
_F10BgpM2PrefixCountersSafi_Type = F10BgpM2Safi
_F10BgpM2PrefixCountersSafi_Object = MibTableColumn
f10BgpM2PrefixCountersSafi = _F10BgpM2PrefixCountersSafi_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 2),
    _F10BgpM2PrefixCountersSafi_Type()
)
f10BgpM2PrefixCountersSafi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PrefixCountersSafi.setStatus("current")
_F10BgpM2PrefixInPrefixes_Type = Gauge32
_F10BgpM2PrefixInPrefixes_Object = MibTableColumn
f10BgpM2PrefixInPrefixes = _F10BgpM2PrefixInPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 7),
    _F10BgpM2PrefixInPrefixes_Type()
)
f10BgpM2PrefixInPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PrefixInPrefixes.setStatus("current")
_F10BgpM2PrefixInPrefixesAccepted_Type = Gauge32
_F10BgpM2PrefixInPrefixesAccepted_Object = MibTableColumn
f10BgpM2PrefixInPrefixesAccepted = _F10BgpM2PrefixInPrefixesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 8),
    _F10BgpM2PrefixInPrefixesAccepted_Type()
)
f10BgpM2PrefixInPrefixesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PrefixInPrefixesAccepted.setStatus("current")
_F10BgpM2PrefixInPrefixesRejected_Type = Gauge32
_F10BgpM2PrefixInPrefixesRejected_Object = MibTableColumn
f10BgpM2PrefixInPrefixesRejected = _F10BgpM2PrefixInPrefixesRejected_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 9),
    _F10BgpM2PrefixInPrefixesRejected_Type()
)
f10BgpM2PrefixInPrefixesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PrefixInPrefixesRejected.setStatus("current")
_F10BgpM2PrefixOutPrefixes_Type = Gauge32
_F10BgpM2PrefixOutPrefixes_Object = MibTableColumn
f10BgpM2PrefixOutPrefixes = _F10BgpM2PrefixOutPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 10),
    _F10BgpM2PrefixOutPrefixes_Type()
)
f10BgpM2PrefixOutPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PrefixOutPrefixes.setStatus("current")
_F10BgpM2PrefixWdrawnByPeer_Type = Gauge32
_F10BgpM2PrefixWdrawnByPeer_Object = MibTableColumn
f10BgpM2PrefixWdrawnByPeer = _F10BgpM2PrefixWdrawnByPeer_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 11),
    _F10BgpM2PrefixWdrawnByPeer_Type()
)
f10BgpM2PrefixWdrawnByPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PrefixWdrawnByPeer.setStatus("current")
_F10BgpM2PrefixWdrawnFromPeer_Type = Gauge32
_F10BgpM2PrefixWdrawnFromPeer_Object = MibTableColumn
f10BgpM2PrefixWdrawnFromPeer = _F10BgpM2PrefixWdrawnFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 12),
    _F10BgpM2PrefixWdrawnFromPeer_Type()
)
f10BgpM2PrefixWdrawnFromPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PrefixWdrawnFromPeer.setStatus("current")
_F10BgpM2PeerExtensions_ObjectIdentity = ObjectIdentity
f10BgpM2PeerExtensions = _F10BgpM2PeerExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7)
)
_F10BgpM2PeerNonCapExts_ObjectIdentity = ObjectIdentity
f10BgpM2PeerNonCapExts = _F10BgpM2PeerNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1)
)
_F10BgpM2PeerRouteReflectionExts_ObjectIdentity = ObjectIdentity
f10BgpM2PeerRouteReflectionExts = _F10BgpM2PeerRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 2796)
)
_F10BgpM2PeerReflectorClientTable_Object = MibTable
f10BgpM2PeerReflectorClientTable = _F10BgpM2PeerReflectorClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 2796, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerReflectorClientTable.setStatus("current")
_F10BgpM2PeerReflectorClientEntry_Object = MibTableRow
f10BgpM2PeerReflectorClientEntry = _F10BgpM2PeerReflectorClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 2796, 1, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerReflectorClientEntry.setStatus("current")


class _F10BgpM2PeerReflectorClient_Type(Integer32):
    """Custom type f10BgpM2PeerReflectorClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("meshedClient", 2),
          ("nonClient", 0))
    )


_F10BgpM2PeerReflectorClient_Type.__name__ = "Integer32"
_F10BgpM2PeerReflectorClient_Object = MibTableColumn
f10BgpM2PeerReflectorClient = _F10BgpM2PeerReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 2796, 1, 1, 1),
    _F10BgpM2PeerReflectorClient_Type()
)
f10BgpM2PeerReflectorClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerReflectorClient.setStatus("current")
_F10BgpM2PeerASConfederationExts_ObjectIdentity = ObjectIdentity
f10BgpM2PeerASConfederationExts = _F10BgpM2PeerASConfederationExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 3065)
)
_F10BgpM2PeerConfedMemberTable_Object = MibTable
f10BgpM2PeerConfedMemberTable = _F10BgpM2PeerConfedMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 3065, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerConfedMemberTable.setStatus("current")
_F10BgpM2PeerConfedMemberEntry_Object = MibTableRow
f10BgpM2PeerConfedMemberEntry = _F10BgpM2PeerConfedMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 3065, 1, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PeerConfedMemberEntry.setStatus("current")
_F10BgpM2PeerConfedMember_Type = TruthValue
_F10BgpM2PeerConfedMember_Object = MibTableColumn
f10BgpM2PeerConfedMember = _F10BgpM2PeerConfedMember_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 3065, 1, 1, 1),
    _F10BgpM2PeerConfedMember_Type()
)
f10BgpM2PeerConfedMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PeerConfedMember.setStatus("current")
_F10BgpM2PeerCapExts_ObjectIdentity = ObjectIdentity
f10BgpM2PeerCapExts = _F10BgpM2PeerCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 2)
)
_F10BgpM2PeerConfiguration_ObjectIdentity = ObjectIdentity
f10BgpM2PeerConfiguration = _F10BgpM2PeerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8)
)
_F10BgpM2CfgPeerAdminStatusTable_Object = MibTable
f10BgpM2CfgPeerAdminStatusTable = _F10BgpM2CfgPeerAdminStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerAdminStatusTable.setStatus("current")
_F10BgpM2CfgPeerAdminStatusEntry_Object = MibTableRow
f10BgpM2CfgPeerAdminStatusEntry = _F10BgpM2CfgPeerAdminStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 1, 1)
)
f10BgpM2CfgPeerAdminStatusEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerAdminStatusEntry.setStatus("current")


class _F10BgpM2CfgPeerAdminStatus_Type(Integer32):
    """Custom type f10BgpM2CfgPeerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 2),
          ("stop", 1))
    )


_F10BgpM2CfgPeerAdminStatus_Type.__name__ = "Integer32"
_F10BgpM2CfgPeerAdminStatus_Object = MibTableColumn
f10BgpM2CfgPeerAdminStatus = _F10BgpM2CfgPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 1, 1, 1),
    _F10BgpM2CfgPeerAdminStatus_Type()
)
f10BgpM2CfgPeerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerAdminStatus.setStatus("current")


class _F10BgpM2CfgPeerNextIndex_Type(Integer32):
    """Custom type f10BgpM2CfgPeerNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_F10BgpM2CfgPeerNextIndex_Type.__name__ = "Integer32"
_F10BgpM2CfgPeerNextIndex_Object = MibScalar
f10BgpM2CfgPeerNextIndex = _F10BgpM2CfgPeerNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 2),
    _F10BgpM2CfgPeerNextIndex_Type()
)
f10BgpM2CfgPeerNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerNextIndex.setStatus("current")
_F10BgpM2CfgPeerTable_Object = MibTable
f10BgpM2CfgPeerTable = _F10BgpM2CfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerTable.setStatus("current")
_F10BgpM2CfgPeerEntry_Object = MibTableRow
f10BgpM2CfgPeerEntry = _F10BgpM2CfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1)
)
f10BgpM2CfgPeerEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerEntry.setStatus("current")


class _F10BgpM2CfgPeerConfiguredVersion_Type(Unsigned32):
    """Custom type f10BgpM2CfgPeerConfiguredVersion based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F10BgpM2CfgPeerConfiguredVersion_Type.__name__ = "Unsigned32"
_F10BgpM2CfgPeerConfiguredVersion_Object = MibTableColumn
f10BgpM2CfgPeerConfiguredVersion = _F10BgpM2CfgPeerConfiguredVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 1),
    _F10BgpM2CfgPeerConfiguredVersion_Type()
)
f10BgpM2CfgPeerConfiguredVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerConfiguredVersion.setStatus("current")


class _F10BgpM2CfgAllowVersionNegotiation_Type(TruthValue):
    """Custom type f10BgpM2CfgAllowVersionNegotiation based on TruthValue"""


_F10BgpM2CfgAllowVersionNegotiation_Object = MibTableColumn
f10BgpM2CfgAllowVersionNegotiation = _F10BgpM2CfgAllowVersionNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 2),
    _F10BgpM2CfgAllowVersionNegotiation_Type()
)
f10BgpM2CfgAllowVersionNegotiation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgAllowVersionNegotiation.setStatus("current")
_F10BgpM2CfgPeerLocalAddrType_Type = InetAddressType
_F10BgpM2CfgPeerLocalAddrType_Object = MibTableColumn
f10BgpM2CfgPeerLocalAddrType = _F10BgpM2CfgPeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 3),
    _F10BgpM2CfgPeerLocalAddrType_Type()
)
f10BgpM2CfgPeerLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerLocalAddrType.setStatus("current")


class _F10BgpM2CfgPeerLocalAddr_Type(InetAddress):
    """Custom type f10BgpM2CfgPeerLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_F10BgpM2CfgPeerLocalAddr_Type.__name__ = "InetAddress"
_F10BgpM2CfgPeerLocalAddr_Object = MibTableColumn
f10BgpM2CfgPeerLocalAddr = _F10BgpM2CfgPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 4),
    _F10BgpM2CfgPeerLocalAddr_Type()
)
f10BgpM2CfgPeerLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerLocalAddr.setStatus("current")


class _F10BgpM2CfgPeerLocalAs_Type(InetAutonomousSystemNumber):
    """Custom type f10BgpM2CfgPeerLocalAs based on InetAutonomousSystemNumber"""
    defaultValue = 0


_F10BgpM2CfgPeerLocalAs_Object = MibTableColumn
f10BgpM2CfgPeerLocalAs = _F10BgpM2CfgPeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 5),
    _F10BgpM2CfgPeerLocalAs_Type()
)
f10BgpM2CfgPeerLocalAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerLocalAs.setStatus("current")
_F10BgpM2CfgPeerRemoteAddrType_Type = InetAddressType
_F10BgpM2CfgPeerRemoteAddrType_Object = MibTableColumn
f10BgpM2CfgPeerRemoteAddrType = _F10BgpM2CfgPeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 6),
    _F10BgpM2CfgPeerRemoteAddrType_Type()
)
f10BgpM2CfgPeerRemoteAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerRemoteAddrType.setStatus("current")


class _F10BgpM2CfgPeerRemoteAddr_Type(InetAddress):
    """Custom type f10BgpM2CfgPeerRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_F10BgpM2CfgPeerRemoteAddr_Type.__name__ = "InetAddress"
_F10BgpM2CfgPeerRemoteAddr_Object = MibTableColumn
f10BgpM2CfgPeerRemoteAddr = _F10BgpM2CfgPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 7),
    _F10BgpM2CfgPeerRemoteAddr_Type()
)
f10BgpM2CfgPeerRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerRemoteAddr.setStatus("current")
_F10BgpM2CfgPeerRemoteAs_Type = InetAutonomousSystemNumber
_F10BgpM2CfgPeerRemoteAs_Object = MibTableColumn
f10BgpM2CfgPeerRemoteAs = _F10BgpM2CfgPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 8),
    _F10BgpM2CfgPeerRemoteAs_Type()
)
f10BgpM2CfgPeerRemoteAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerRemoteAs.setStatus("current")
_F10BgpM2CfgPeerEntryStorageType_Type = StorageType
_F10BgpM2CfgPeerEntryStorageType_Object = MibTableColumn
f10BgpM2CfgPeerEntryStorageType = _F10BgpM2CfgPeerEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 9),
    _F10BgpM2CfgPeerEntryStorageType_Type()
)
f10BgpM2CfgPeerEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerEntryStorageType.setStatus("current")


class _F10BgpM2CfgPeerError_Type(Integer32):
    """Custom type f10BgpM2CfgPeerError based on Integer32"""
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
        *(("activated", 3),
          ("errDuplicatePeeringSession", 2),
          ("notActivated", 1),
          ("unknown", 0))
    )


_F10BgpM2CfgPeerError_Type.__name__ = "Integer32"
_F10BgpM2CfgPeerError_Object = MibTableColumn
f10BgpM2CfgPeerError = _F10BgpM2CfgPeerError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 10),
    _F10BgpM2CfgPeerError_Type()
)
f10BgpM2CfgPeerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerError.setStatus("current")
_F10BgpM2CfgPeerBgpPeerEntry_Type = RowPointer
_F10BgpM2CfgPeerBgpPeerEntry_Object = MibTableColumn
f10BgpM2CfgPeerBgpPeerEntry = _F10BgpM2CfgPeerBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 11),
    _F10BgpM2CfgPeerBgpPeerEntry_Type()
)
f10BgpM2CfgPeerBgpPeerEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerBgpPeerEntry.setStatus("current")
_F10BgpM2CfgPeerRowEntryStatus_Type = RowStatus
_F10BgpM2CfgPeerRowEntryStatus_Object = MibTableColumn
f10BgpM2CfgPeerRowEntryStatus = _F10BgpM2CfgPeerRowEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 12),
    _F10BgpM2CfgPeerRowEntryStatus_Type()
)
f10BgpM2CfgPeerRowEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerRowEntryStatus.setStatus("current")


class _F10BgpM2CfgPeerIndex_Type(Integer32):
    """Custom type f10BgpM2CfgPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F10BgpM2CfgPeerIndex_Type.__name__ = "Integer32"
_F10BgpM2CfgPeerIndex_Object = MibTableColumn
f10BgpM2CfgPeerIndex = _F10BgpM2CfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 13),
    _F10BgpM2CfgPeerIndex_Type()
)
f10BgpM2CfgPeerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerIndex.setStatus("current")


class _F10BgpM2CfgPeerStatus_Type(Integer32):
    """Custom type f10BgpM2CfgPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halted", 1),
          ("running", 2))
    )


_F10BgpM2CfgPeerStatus_Type.__name__ = "Integer32"
_F10BgpM2CfgPeerStatus_Object = MibTableColumn
f10BgpM2CfgPeerStatus = _F10BgpM2CfgPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 14),
    _F10BgpM2CfgPeerStatus_Type()
)
f10BgpM2CfgPeerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerStatus.setStatus("current")
_F10BgpM2CfgPeerTimersTable_Object = MibTable
f10BgpM2CfgPeerTimersTable = _F10BgpM2CfgPeerTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerTimersTable.setStatus("current")
_F10BgpM2CfgPeerTimersEntry_Object = MibTableRow
f10BgpM2CfgPeerTimersEntry = _F10BgpM2CfgPeerTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerTimersEntry.setStatus("current")


class _F10BgpM2CfgPeerConnectRetryInterval_Type(Unsigned32):
    """Custom type f10BgpM2CfgPeerConnectRetryInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F10BgpM2CfgPeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_F10BgpM2CfgPeerConnectRetryInterval_Object = MibTableColumn
f10BgpM2CfgPeerConnectRetryInterval = _F10BgpM2CfgPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1, 1),
    _F10BgpM2CfgPeerConnectRetryInterval_Type()
)
f10BgpM2CfgPeerConnectRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerConnectRetryInterval.setStatus("current")


class _F10BgpM2CfgPeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type f10BgpM2CfgPeerHoldTimeConfigured based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_F10BgpM2CfgPeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_F10BgpM2CfgPeerHoldTimeConfigured_Object = MibTableColumn
f10BgpM2CfgPeerHoldTimeConfigured = _F10BgpM2CfgPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1, 2),
    _F10BgpM2CfgPeerHoldTimeConfigured_Type()
)
f10BgpM2CfgPeerHoldTimeConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerHoldTimeConfigured.setStatus("current")


class _F10BgpM2CfgPeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type f10BgpM2CfgPeerKeepAliveConfigured based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_F10BgpM2CfgPeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_F10BgpM2CfgPeerKeepAliveConfigured_Object = MibTableColumn
f10BgpM2CfgPeerKeepAliveConfigured = _F10BgpM2CfgPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1, 3),
    _F10BgpM2CfgPeerKeepAliveConfigured_Type()
)
f10BgpM2CfgPeerKeepAliveConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerKeepAliveConfigured.setStatus("current")


class _F10BgpM2CfgPeerMinASOrigInterval_Type(Unsigned32):
    """Custom type f10BgpM2CfgPeerMinASOrigInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_F10BgpM2CfgPeerMinASOrigInterval_Type.__name__ = "Unsigned32"
_F10BgpM2CfgPeerMinASOrigInterval_Object = MibTableColumn
f10BgpM2CfgPeerMinASOrigInterval = _F10BgpM2CfgPeerMinASOrigInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1, 4),
    _F10BgpM2CfgPeerMinASOrigInterval_Type()
)
f10BgpM2CfgPeerMinASOrigInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerMinASOrigInterval.setStatus("current")


class _F10BgpM2CfgPeerMinRouteAdverInter_Type(Unsigned32):
    """Custom type f10BgpM2CfgPeerMinRouteAdverInter based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_F10BgpM2CfgPeerMinRouteAdverInter_Type.__name__ = "Unsigned32"
_F10BgpM2CfgPeerMinRouteAdverInter_Object = MibTableColumn
f10BgpM2CfgPeerMinRouteAdverInter = _F10BgpM2CfgPeerMinRouteAdverInter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1, 5),
    _F10BgpM2CfgPeerMinRouteAdverInter_Type()
)
f10BgpM2CfgPeerMinRouteAdverInter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerMinRouteAdverInter.setStatus("current")
_F10BgpM2CfgPeerExtensions_ObjectIdentity = ObjectIdentity
f10BgpM2CfgPeerExtensions = _F10BgpM2CfgPeerExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5)
)
_F10BgpM2CfgPeerNonCapExts_ObjectIdentity = ObjectIdentity
f10BgpM2CfgPeerNonCapExts = _F10BgpM2CfgPeerNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1)
)
_F10BgpM2CfgPeerRouteReflectionExts_ObjectIdentity = ObjectIdentity
f10BgpM2CfgPeerRouteReflectionExts = _F10BgpM2CfgPeerRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 2796)
)
_F10BgpM2CfgPeerReflectorClientTable_Object = MibTable
f10BgpM2CfgPeerReflectorClientTable = _F10BgpM2CfgPeerReflectorClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 2796, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerReflectorClientTable.setStatus("current")
_F10BgpM2CfgPeerReflectorClientEntry_Object = MibTableRow
f10BgpM2CfgPeerReflectorClientEntry = _F10BgpM2CfgPeerReflectorClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 2796, 1, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerReflectorClientEntry.setStatus("current")


class _F10BgpM2CfgPeerReflectorClient_Type(Integer32):
    """Custom type f10BgpM2CfgPeerReflectorClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("meshedClient", 2),
          ("nonClient", 0))
    )


_F10BgpM2CfgPeerReflectorClient_Type.__name__ = "Integer32"
_F10BgpM2CfgPeerReflectorClient_Object = MibTableColumn
f10BgpM2CfgPeerReflectorClient = _F10BgpM2CfgPeerReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 2796, 1, 1, 1),
    _F10BgpM2CfgPeerReflectorClient_Type()
)
f10BgpM2CfgPeerReflectorClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerReflectorClient.setStatus("current")
_F10BgpM2CfgPeerASConfederationExts_ObjectIdentity = ObjectIdentity
f10BgpM2CfgPeerASConfederationExts = _F10BgpM2CfgPeerASConfederationExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 3065)
)
_F10BgpM2CfgPeerConfedMemberTable_Object = MibTable
f10BgpM2CfgPeerConfedMemberTable = _F10BgpM2CfgPeerConfedMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 3065, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerConfedMemberTable.setStatus("current")
_F10BgpM2CfgPeerConfedMemberEntry_Object = MibTableRow
f10BgpM2CfgPeerConfedMemberEntry = _F10BgpM2CfgPeerConfedMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 3065, 1, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerConfedMemberEntry.setStatus("current")
_F10BgpM2CfgPeerConfedMember_Type = TruthValue
_F10BgpM2CfgPeerConfedMember_Object = MibTableColumn
f10BgpM2CfgPeerConfedMember = _F10BgpM2CfgPeerConfedMember_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 3065, 1, 1, 1),
    _F10BgpM2CfgPeerConfedMember_Type()
)
f10BgpM2CfgPeerConfedMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f10BgpM2CfgPeerConfedMember.setStatus("current")
_F10BgpM2CfgPeerCapExts_ObjectIdentity = ObjectIdentity
f10BgpM2CfgPeerCapExts = _F10BgpM2CfgPeerCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 2)
)
_F10BgpM2Rib_ObjectIdentity = ObjectIdentity
f10BgpM2Rib = _F10BgpM2Rib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3)
)
_F10BgpM2NlriTable_Object = MibTable
f10BgpM2NlriTable = _F10BgpM2NlriTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2NlriTable.setStatus("current")
_F10BgpM2NlriEntry_Object = MibTableRow
f10BgpM2NlriEntry = _F10BgpM2NlriEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1)
)
f10BgpM2NlriEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2NlriAfi"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2NlriSafi"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2NlriPrefix"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2NlriPrefixLen"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2NlriIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2NlriEntry.setStatus("current")
_F10BgpM2NlriIndex_Type = Unsigned32
_F10BgpM2NlriIndex_Object = MibTableColumn
f10BgpM2NlriIndex = _F10BgpM2NlriIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 1),
    _F10BgpM2NlriIndex_Type()
)
f10BgpM2NlriIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2NlriIndex.setStatus("current")
_F10BgpM2NlriAfi_Type = F10BgpM2Afi
_F10BgpM2NlriAfi_Object = MibTableColumn
f10BgpM2NlriAfi = _F10BgpM2NlriAfi_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 2),
    _F10BgpM2NlriAfi_Type()
)
f10BgpM2NlriAfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2NlriAfi.setStatus("current")
_F10BgpM2NlriSafi_Type = F10BgpM2Safi
_F10BgpM2NlriSafi_Object = MibTableColumn
f10BgpM2NlriSafi = _F10BgpM2NlriSafi_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 3),
    _F10BgpM2NlriSafi_Type()
)
f10BgpM2NlriSafi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2NlriSafi.setStatus("current")
_F10BgpM2NlriPrefixType_Type = InetAddressType
_F10BgpM2NlriPrefixType_Object = MibTableColumn
f10BgpM2NlriPrefixType = _F10BgpM2NlriPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 4),
    _F10BgpM2NlriPrefixType_Type()
)
f10BgpM2NlriPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2NlriPrefixType.setStatus("current")


class _F10BgpM2NlriPrefix_Type(InetAddress):
    """Custom type f10BgpM2NlriPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_F10BgpM2NlriPrefix_Type.__name__ = "InetAddress"
_F10BgpM2NlriPrefix_Object = MibTableColumn
f10BgpM2NlriPrefix = _F10BgpM2NlriPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 5),
    _F10BgpM2NlriPrefix_Type()
)
f10BgpM2NlriPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2NlriPrefix.setStatus("current")
_F10BgpM2NlriPrefixLen_Type = InetAddressPrefixLength
_F10BgpM2NlriPrefixLen_Object = MibTableColumn
f10BgpM2NlriPrefixLen = _F10BgpM2NlriPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 6),
    _F10BgpM2NlriPrefixLen_Type()
)
f10BgpM2NlriPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2NlriPrefixLen.setStatus("current")
_F10BgpM2NlriBest_Type = TruthValue
_F10BgpM2NlriBest_Object = MibTableColumn
f10BgpM2NlriBest = _F10BgpM2NlriBest_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 7),
    _F10BgpM2NlriBest_Type()
)
f10BgpM2NlriBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2NlriBest.setStatus("current")
_F10BgpM2NlriCalcLocalPref_Type = Unsigned32
_F10BgpM2NlriCalcLocalPref_Object = MibTableColumn
f10BgpM2NlriCalcLocalPref = _F10BgpM2NlriCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 8),
    _F10BgpM2NlriCalcLocalPref_Type()
)
f10BgpM2NlriCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2NlriCalcLocalPref.setStatus("current")
_F10BgpM2PathAttrIndex_Type = Unsigned32
_F10BgpM2PathAttrIndex_Object = MibTableColumn
f10BgpM2PathAttrIndex = _F10BgpM2PathAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 9),
    _F10BgpM2PathAttrIndex_Type()
)
f10BgpM2PathAttrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrIndex.setStatus("current")


class _F10BgpM2NlriOpaqueType_Type(Integer32):
    """Custom type f10BgpM2NlriOpaqueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bgpMplsLabelStack", 1),
          ("none", 0))
    )


_F10BgpM2NlriOpaqueType_Type.__name__ = "Integer32"
_F10BgpM2NlriOpaqueType_Object = MibTableColumn
f10BgpM2NlriOpaqueType = _F10BgpM2NlriOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 10),
    _F10BgpM2NlriOpaqueType_Type()
)
f10BgpM2NlriOpaqueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2NlriOpaqueType.setStatus("current")
_F10BgpM2NlriOpaquePointer_Type = RowPointer
_F10BgpM2NlriOpaquePointer_Object = MibTableColumn
f10BgpM2NlriOpaquePointer = _F10BgpM2NlriOpaquePointer_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 11),
    _F10BgpM2NlriOpaquePointer_Type()
)
f10BgpM2NlriOpaquePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2NlriOpaquePointer.setStatus("current")
_F10BgpM2AdjRibsOutTable_Object = MibTable
f10BgpM2AdjRibsOutTable = _F10BgpM2AdjRibsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 2)
)
if mibBuilder.loadTexts:
    f10BgpM2AdjRibsOutTable.setStatus("current")
_F10BgpM2AdjRibsOutEntry_Object = MibTableRow
f10BgpM2AdjRibsOutEntry = _F10BgpM2AdjRibsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 2, 1)
)
f10BgpM2AdjRibsOutEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PeerIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2NlriAfi"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2NlriSafi"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2NlriPrefix"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2NlriPrefixLen"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2AdjRibsOutIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2AdjRibsOutEntry.setStatus("current")
_F10BgpM2AdjRibsOutIndex_Type = Unsigned32
_F10BgpM2AdjRibsOutIndex_Object = MibTableColumn
f10BgpM2AdjRibsOutIndex = _F10BgpM2AdjRibsOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 2, 1, 1),
    _F10BgpM2AdjRibsOutIndex_Type()
)
f10BgpM2AdjRibsOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AdjRibsOutIndex.setStatus("current")
_F10BgpM2AdjRibsOutRoute_Type = RowPointer
_F10BgpM2AdjRibsOutRoute_Object = MibTableColumn
f10BgpM2AdjRibsOutRoute = _F10BgpM2AdjRibsOutRoute_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 2, 1, 2),
    _F10BgpM2AdjRibsOutRoute_Type()
)
f10BgpM2AdjRibsOutRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AdjRibsOutRoute.setStatus("current")
_F10BgpM2PathAttrCount_Type = Counter32
_F10BgpM2PathAttrCount_Object = MibScalar
f10BgpM2PathAttrCount = _F10BgpM2PathAttrCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 3),
    _F10BgpM2PathAttrCount_Type()
)
f10BgpM2PathAttrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrCount.setStatus("current")
_F10BgpM2PathAttrTable_Object = MibTable
f10BgpM2PathAttrTable = _F10BgpM2PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4)
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrTable.setStatus("current")
_F10BgpM2PathAttrEntry_Object = MibTableRow
f10BgpM2PathAttrEntry = _F10BgpM2PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1)
)
f10BgpM2PathAttrEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrEntry.setStatus("current")


class _F10BgpM2PathAttrOrigin_Type(Integer32):
    """Custom type f10BgpM2PathAttrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_F10BgpM2PathAttrOrigin_Type.__name__ = "Integer32"
_F10BgpM2PathAttrOrigin_Object = MibTableColumn
f10BgpM2PathAttrOrigin = _F10BgpM2PathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 1),
    _F10BgpM2PathAttrOrigin_Type()
)
f10BgpM2PathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrOrigin.setStatus("current")
_F10BgpM2PathAttrNextHopAddrType_Type = InetAddressType
_F10BgpM2PathAttrNextHopAddrType_Object = MibTableColumn
f10BgpM2PathAttrNextHopAddrType = _F10BgpM2PathAttrNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 2),
    _F10BgpM2PathAttrNextHopAddrType_Type()
)
f10BgpM2PathAttrNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrNextHopAddrType.setStatus("current")


class _F10BgpM2PathAttrNextHop_Type(InetAddress):
    """Custom type f10BgpM2PathAttrNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_F10BgpM2PathAttrNextHop_Type.__name__ = "InetAddress"
_F10BgpM2PathAttrNextHop_Object = MibTableColumn
f10BgpM2PathAttrNextHop = _F10BgpM2PathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 3),
    _F10BgpM2PathAttrNextHop_Type()
)
f10BgpM2PathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrNextHop.setStatus("current")
_F10BgpM2PathAttrMedPresent_Type = TruthValue
_F10BgpM2PathAttrMedPresent_Object = MibTableColumn
f10BgpM2PathAttrMedPresent = _F10BgpM2PathAttrMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 4),
    _F10BgpM2PathAttrMedPresent_Type()
)
f10BgpM2PathAttrMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrMedPresent.setStatus("current")
_F10BgpM2PathAttrMed_Type = Unsigned32
_F10BgpM2PathAttrMed_Object = MibTableColumn
f10BgpM2PathAttrMed = _F10BgpM2PathAttrMed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 5),
    _F10BgpM2PathAttrMed_Type()
)
f10BgpM2PathAttrMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrMed.setStatus("current")
_F10BgpM2PathAttrLocalPrefPresent_Type = TruthValue
_F10BgpM2PathAttrLocalPrefPresent_Object = MibTableColumn
f10BgpM2PathAttrLocalPrefPresent = _F10BgpM2PathAttrLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 6),
    _F10BgpM2PathAttrLocalPrefPresent_Type()
)
f10BgpM2PathAttrLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrLocalPrefPresent.setStatus("current")
_F10BgpM2PathAttrLocalPref_Type = Unsigned32
_F10BgpM2PathAttrLocalPref_Object = MibTableColumn
f10BgpM2PathAttrLocalPref = _F10BgpM2PathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 7),
    _F10BgpM2PathAttrLocalPref_Type()
)
f10BgpM2PathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrLocalPref.setStatus("current")


class _F10BgpM2PathAttrAtomicAggregate_Type(Integer32):
    """Custom type f10BgpM2PathAttrAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atomicAggregateMissing", 2),
          ("atomicAggregatePresent", 1))
    )


_F10BgpM2PathAttrAtomicAggregate_Type.__name__ = "Integer32"
_F10BgpM2PathAttrAtomicAggregate_Object = MibTableColumn
f10BgpM2PathAttrAtomicAggregate = _F10BgpM2PathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 8),
    _F10BgpM2PathAttrAtomicAggregate_Type()
)
f10BgpM2PathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrAtomicAggregate.setStatus("current")
_F10BgpM2PathAttrAggregatorAS_Type = InetAutonomousSystemNumber
_F10BgpM2PathAttrAggregatorAS_Object = MibTableColumn
f10BgpM2PathAttrAggregatorAS = _F10BgpM2PathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 9),
    _F10BgpM2PathAttrAggregatorAS_Type()
)
f10BgpM2PathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrAggregatorAS.setStatus("current")
_F10BgpM2PathAttrAggregatorAddr_Type = F10BgpM2Identifier
_F10BgpM2PathAttrAggregatorAddr_Object = MibTableColumn
f10BgpM2PathAttrAggregatorAddr = _F10BgpM2PathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 10),
    _F10BgpM2PathAttrAggregatorAddr_Type()
)
f10BgpM2PathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrAggregatorAddr.setStatus("current")
_F10BgpM2AsPathCalcLength_Type = Unsigned32
_F10BgpM2AsPathCalcLength_Object = MibTableColumn
f10BgpM2AsPathCalcLength = _F10BgpM2AsPathCalcLength_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 11),
    _F10BgpM2AsPathCalcLength_Type()
)
f10BgpM2AsPathCalcLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPathCalcLength.setStatus("current")
_F10BgpM2AsPathString_Type = SnmpAdminString
_F10BgpM2AsPathString_Object = MibTableColumn
f10BgpM2AsPathString = _F10BgpM2AsPathString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 12),
    _F10BgpM2AsPathString_Type()
)
f10BgpM2AsPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPathString.setStatus("current")
_F10BgpM2AsPathIndex_Type = Unsigned32
_F10BgpM2AsPathIndex_Object = MibTableColumn
f10BgpM2AsPathIndex = _F10BgpM2AsPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 13),
    _F10BgpM2AsPathIndex_Type()
)
f10BgpM2AsPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPathIndex.setStatus("current")
_F10BgpM2AsPath4byteTable_Object = MibTable
f10BgpM2AsPath4byteTable = _F10BgpM2AsPath4byteTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5)
)
if mibBuilder.loadTexts:
    f10BgpM2AsPath4byteTable.setStatus("current")
_F10BgpM2AsPath4byteEntry_Object = MibTableRow
f10BgpM2AsPath4byteEntry = _F10BgpM2AsPath4byteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2AsPath4byteEntry.setStatus("current")
_F10BgpM2AsPath4bytePathPresent_Type = TruthValue
_F10BgpM2AsPath4bytePathPresent_Object = MibTableColumn
f10BgpM2AsPath4bytePathPresent = _F10BgpM2AsPath4bytePathPresent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1, 1),
    _F10BgpM2AsPath4bytePathPresent_Type()
)
f10BgpM2AsPath4bytePathPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPath4bytePathPresent.setStatus("current")
_F10BgpM2AsPath4byteAggregatorAS_Type = InetAutonomousSystemNumber
_F10BgpM2AsPath4byteAggregatorAS_Object = MibTableColumn
f10BgpM2AsPath4byteAggregatorAS = _F10BgpM2AsPath4byteAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1, 2),
    _F10BgpM2AsPath4byteAggregatorAS_Type()
)
f10BgpM2AsPath4byteAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPath4byteAggregatorAS.setStatus("current")
_F10BgpM2AsPath4byteCalcLength_Type = Unsigned32
_F10BgpM2AsPath4byteCalcLength_Object = MibTableColumn
f10BgpM2AsPath4byteCalcLength = _F10BgpM2AsPath4byteCalcLength_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1, 3),
    _F10BgpM2AsPath4byteCalcLength_Type()
)
f10BgpM2AsPath4byteCalcLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPath4byteCalcLength.setStatus("current")
_F10BgpM2AsPath4byteString_Type = SnmpAdminString
_F10BgpM2AsPath4byteString_Object = MibTableColumn
f10BgpM2AsPath4byteString = _F10BgpM2AsPath4byteString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1, 4),
    _F10BgpM2AsPath4byteString_Type()
)
f10BgpM2AsPath4byteString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPath4byteString.setStatus("current")
_F10BgpM2AsPath4byteIndex_Type = Unsigned32
_F10BgpM2AsPath4byteIndex_Object = MibTableColumn
f10BgpM2AsPath4byteIndex = _F10BgpM2AsPath4byteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1, 5),
    _F10BgpM2AsPath4byteIndex_Type()
)
f10BgpM2AsPath4byteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPath4byteIndex.setStatus("current")
_F10BgpM2AsPathTable_Object = MibTable
f10BgpM2AsPathTable = _F10BgpM2AsPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6)
)
if mibBuilder.loadTexts:
    f10BgpM2AsPathTable.setStatus("current")
_F10BgpM2AsPathTableEntry_Object = MibTableRow
f10BgpM2AsPathTableEntry = _F10BgpM2AsPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6, 1)
)
f10BgpM2AsPathTableEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathSegmentIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathElementIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2AsPathTableEntry.setStatus("current")
_F10BgpM2AsPathSegmentIndex_Type = Unsigned32
_F10BgpM2AsPathSegmentIndex_Object = MibTableColumn
f10BgpM2AsPathSegmentIndex = _F10BgpM2AsPathSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6, 1, 1),
    _F10BgpM2AsPathSegmentIndex_Type()
)
f10BgpM2AsPathSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPathSegmentIndex.setStatus("current")
_F10BgpM2AsPathElementIndex_Type = Unsigned32
_F10BgpM2AsPathElementIndex_Object = MibTableColumn
f10BgpM2AsPathElementIndex = _F10BgpM2AsPathElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6, 1, 2),
    _F10BgpM2AsPathElementIndex_Type()
)
f10BgpM2AsPathElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPathElementIndex.setStatus("current")


class _F10BgpM2AsPathType_Type(Integer32):
    """Custom type f10BgpM2AsPathType based on Integer32"""
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
        *(("asSequence", 2),
          ("asSet", 1),
          ("confedSequence", 3),
          ("confedSet", 4))
    )


_F10BgpM2AsPathType_Type.__name__ = "Integer32"
_F10BgpM2AsPathType_Object = MibTableColumn
f10BgpM2AsPathType = _F10BgpM2AsPathType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6, 1, 3),
    _F10BgpM2AsPathType_Type()
)
f10BgpM2AsPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPathType.setStatus("current")
_F10BgpM2AsPathElementValue_Type = InetAutonomousSystemNumber
_F10BgpM2AsPathElementValue_Object = MibTableColumn
f10BgpM2AsPathElementValue = _F10BgpM2AsPathElementValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6, 1, 4),
    _F10BgpM2AsPathElementValue_Type()
)
f10BgpM2AsPathElementValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2AsPathElementValue.setStatus("current")
_F10BgpM2PathAttrUnknownTable_Object = MibTable
f10BgpM2PathAttrUnknownTable = _F10BgpM2PathAttrUnknownTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 7)
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrUnknownTable.setStatus("current")
_F10BgpM2PathAttrUnknownEntry_Object = MibTableRow
f10BgpM2PathAttrUnknownEntry = _F10BgpM2PathAttrUnknownEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 7, 1)
)
f10BgpM2PathAttrUnknownEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrUnknownIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrUnknownEntry.setStatus("current")
_F10BgpM2PathAttrUnknownIndex_Type = Unsigned32
_F10BgpM2PathAttrUnknownIndex_Object = MibTableColumn
f10BgpM2PathAttrUnknownIndex = _F10BgpM2PathAttrUnknownIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 7, 1, 1),
    _F10BgpM2PathAttrUnknownIndex_Type()
)
f10BgpM2PathAttrUnknownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrUnknownIndex.setStatus("current")
_F10BgpM2PathAttrUnknownType_Type = Unsigned32
_F10BgpM2PathAttrUnknownType_Object = MibTableColumn
f10BgpM2PathAttrUnknownType = _F10BgpM2PathAttrUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 7, 1, 2),
    _F10BgpM2PathAttrUnknownType_Type()
)
f10BgpM2PathAttrUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrUnknownType.setStatus("current")


class _F10BgpM2PathAttrUnknownValue_Type(OctetString):
    """Custom type f10BgpM2PathAttrUnknownValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4070),
    )


_F10BgpM2PathAttrUnknownValue_Type.__name__ = "OctetString"
_F10BgpM2PathAttrUnknownValue_Object = MibTableColumn
f10BgpM2PathAttrUnknownValue = _F10BgpM2PathAttrUnknownValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 7, 1, 3),
    _F10BgpM2PathAttrUnknownValue_Type()
)
f10BgpM2PathAttrUnknownValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrUnknownValue.setStatus("current")
_F10BgpM2PathAttrExtensions_ObjectIdentity = ObjectIdentity
f10BgpM2PathAttrExtensions = _F10BgpM2PathAttrExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8)
)
_F10BgpM2PathAttrNonCapExts_ObjectIdentity = ObjectIdentity
f10BgpM2PathAttrNonCapExts = _F10BgpM2PathAttrNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1)
)
_F10BgpM2PathAttrCommunityExts_ObjectIdentity = ObjectIdentity
f10BgpM2PathAttrCommunityExts = _F10BgpM2PathAttrCommunityExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 1997)
)
_F10BgpM2PathAttrCommTable_Object = MibTable
f10BgpM2PathAttrCommTable = _F10BgpM2PathAttrCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 1997, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrCommTable.setStatus("current")
_F10BgpM2PathAttrCommEntry_Object = MibTableRow
f10BgpM2PathAttrCommEntry = _F10BgpM2PathAttrCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 1997, 1, 1)
)
f10BgpM2PathAttrCommEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrCommIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrCommEntry.setStatus("current")
_F10BgpM2PathAttrCommIndex_Type = Unsigned32
_F10BgpM2PathAttrCommIndex_Object = MibTableColumn
f10BgpM2PathAttrCommIndex = _F10BgpM2PathAttrCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 1997, 1, 1, 1),
    _F10BgpM2PathAttrCommIndex_Type()
)
f10BgpM2PathAttrCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrCommIndex.setStatus("current")
_F10BgpM2PathAttrCommValue_Type = F10BgpM2Community
_F10BgpM2PathAttrCommValue_Object = MibTableColumn
f10BgpM2PathAttrCommValue = _F10BgpM2PathAttrCommValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 1997, 1, 1, 2),
    _F10BgpM2PathAttrCommValue_Type()
)
f10BgpM2PathAttrCommValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrCommValue.setStatus("current")
_F10BgpM2LinkLocalNextHopTable_Object = MibTable
f10BgpM2LinkLocalNextHopTable = _F10BgpM2LinkLocalNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2545)
)
if mibBuilder.loadTexts:
    f10BgpM2LinkLocalNextHopTable.setStatus("current")
_F10BgpM2LinkLocalNextHopEntry_Object = MibTableRow
f10BgpM2LinkLocalNextHopEntry = _F10BgpM2LinkLocalNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2545, 1)
)
f10BgpM2LinkLocalNextHopEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2LinkLocalNextHopEntry.setStatus("current")
_F10BgpM2LinkLocalNextHopPresent_Type = TruthValue
_F10BgpM2LinkLocalNextHopPresent_Object = MibTableColumn
f10BgpM2LinkLocalNextHopPresent = _F10BgpM2LinkLocalNextHopPresent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2545, 1, 1),
    _F10BgpM2LinkLocalNextHopPresent_Type()
)
f10BgpM2LinkLocalNextHopPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2LinkLocalNextHopPresent.setStatus("current")


class _F10BgpM2LinkLocalNextHop_Type(InetAddress):
    """Custom type f10BgpM2LinkLocalNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_F10BgpM2LinkLocalNextHop_Type.__name__ = "InetAddress"
_F10BgpM2LinkLocalNextHop_Object = MibTableColumn
f10BgpM2LinkLocalNextHop = _F10BgpM2LinkLocalNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2545, 1, 2),
    _F10BgpM2LinkLocalNextHop_Type()
)
f10BgpM2LinkLocalNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2LinkLocalNextHop.setStatus("current")
_F10BgpM2PathAttrRouteReflectionExts_ObjectIdentity = ObjectIdentity
f10BgpM2PathAttrRouteReflectionExts = _F10BgpM2PathAttrRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796)
)
_F10BgpM2PathAttrOriginatorIdTable_Object = MibTable
f10BgpM2PathAttrOriginatorIdTable = _F10BgpM2PathAttrOriginatorIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrOriginatorIdTable.setStatus("current")
_F10BgpM2PathAttrOriginatorIdEntry_Object = MibTableRow
f10BgpM2PathAttrOriginatorIdEntry = _F10BgpM2PathAttrOriginatorIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 1, 1)
)
f10BgpM2PathAttrOriginatorIdEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrOriginatorIdEntry.setStatus("current")
_F10BgpM2PathAttrOriginatorId_Type = F10BgpM2Identifier
_F10BgpM2PathAttrOriginatorId_Object = MibTableColumn
f10BgpM2PathAttrOriginatorId = _F10BgpM2PathAttrOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 1, 1, 1),
    _F10BgpM2PathAttrOriginatorId_Type()
)
f10BgpM2PathAttrOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrOriginatorId.setStatus("current")
_F10BgpM2PathAttrClusterTable_Object = MibTable
f10BgpM2PathAttrClusterTable = _F10BgpM2PathAttrClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 2)
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrClusterTable.setStatus("current")
_F10BgpM2PathAttrClusterEntry_Object = MibTableRow
f10BgpM2PathAttrClusterEntry = _F10BgpM2PathAttrClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 2, 1)
)
f10BgpM2PathAttrClusterEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrClusterIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrClusterEntry.setStatus("current")
_F10BgpM2PathAttrClusterIndex_Type = Unsigned32
_F10BgpM2PathAttrClusterIndex_Object = MibTableColumn
f10BgpM2PathAttrClusterIndex = _F10BgpM2PathAttrClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 2, 1, 1),
    _F10BgpM2PathAttrClusterIndex_Type()
)
f10BgpM2PathAttrClusterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrClusterIndex.setStatus("current")
_F10BgpM2PathAttrClusterValue_Type = F10BgpM2Identifier
_F10BgpM2PathAttrClusterValue_Object = MibTableColumn
f10BgpM2PathAttrClusterValue = _F10BgpM2PathAttrClusterValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 2, 1, 2),
    _F10BgpM2PathAttrClusterValue_Type()
)
f10BgpM2PathAttrClusterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrClusterValue.setStatus("current")
_F10BgpM2PathAttrExtCommTable_Object = MibTable
f10BgpM2PathAttrExtCommTable = _F10BgpM2PathAttrExtCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 3501)
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrExtCommTable.setStatus("current")
_F10BgpM2PathAttrExtCommEntry_Object = MibTableRow
f10BgpM2PathAttrExtCommEntry = _F10BgpM2PathAttrExtCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 3501, 1)
)
f10BgpM2PathAttrExtCommEntry.setIndexNames(
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrIndex"),
    (0, "FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrExtCommIndex"),
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttrExtCommEntry.setStatus("current")
_F10BgpM2PathAttrExtCommIndex_Type = Unsigned32
_F10BgpM2PathAttrExtCommIndex_Object = MibTableColumn
f10BgpM2PathAttrExtCommIndex = _F10BgpM2PathAttrExtCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 3501, 1, 1),
    _F10BgpM2PathAttrExtCommIndex_Type()
)
f10BgpM2PathAttrExtCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrExtCommIndex.setStatus("current")
_F10BgpM2PathAttrExtCommValue_Type = F10BgpM2ExtendedCommunity
_F10BgpM2PathAttrExtCommValue_Object = MibTableColumn
f10BgpM2PathAttrExtCommValue = _F10BgpM2PathAttrExtCommValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 3501, 1, 2),
    _F10BgpM2PathAttrExtCommValue_Type()
)
f10BgpM2PathAttrExtCommValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10BgpM2PathAttrExtCommValue.setStatus("current")
_F10BgpM2PathAttrCapExts_ObjectIdentity = ObjectIdentity
f10BgpM2PathAttrCapExts = _F10BgpM2PathAttrCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 2)
)
_F10BgpM2Conformance_ObjectIdentity = ObjectIdentity
f10BgpM2Conformance = _F10BgpM2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4)
)
_F10BgpM2MIBCompliances_ObjectIdentity = ObjectIdentity
f10BgpM2MIBCompliances = _F10BgpM2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 1)
)
_F10BgpM2MIBGroups_ObjectIdentity = ObjectIdentity
f10BgpM2MIBGroups = _F10BgpM2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2)
)
f10BgpM2PeerEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2PeerErrorsEntry")
)
f10BgpM2PeerErrorsEntry.setIndexNames(*f10BgpM2PeerEntry.getIndexNames())
f10BgpM2PeerEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2PeerEventTimesEntry")
)
f10BgpM2PeerEventTimesEntry.setIndexNames(*f10BgpM2PeerEntry.getIndexNames())
f10BgpM2PeerEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2PeerConfiguredTimersEntry")
)
f10BgpM2PeerConfiguredTimersEntry.setIndexNames(*f10BgpM2PeerEntry.getIndexNames())
f10BgpM2PeerEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2PeerNegotiatedTimersEntry")
)
f10BgpM2PeerNegotiatedTimersEntry.setIndexNames(*f10BgpM2PeerEntry.getIndexNames())
f10BgpM2PeerEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2PeerCountersEntry")
)
f10BgpM2PeerCountersEntry.setIndexNames(*f10BgpM2PeerEntry.getIndexNames())
f10BgpM2PeerEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2PeerReflectorClientEntry")
)
f10BgpM2PeerReflectorClientEntry.setIndexNames(*f10BgpM2PeerEntry.getIndexNames())
f10BgpM2PeerEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2PeerConfedMemberEntry")
)
f10BgpM2PeerConfedMemberEntry.setIndexNames(*f10BgpM2PeerEntry.getIndexNames())
f10BgpM2CfgPeerEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2CfgPeerTimersEntry")
)
f10BgpM2CfgPeerTimersEntry.setIndexNames(*f10BgpM2CfgPeerEntry.getIndexNames())
f10BgpM2CfgPeerEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2CfgPeerReflectorClientEntry")
)
f10BgpM2CfgPeerReflectorClientEntry.setIndexNames(*f10BgpM2CfgPeerEntry.getIndexNames())
f10BgpM2PeerEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2CfgPeerConfedMemberEntry")
)
f10BgpM2CfgPeerConfedMemberEntry.setIndexNames(*f10BgpM2PeerEntry.getIndexNames())
f10BgpM2PathAttrEntry.registerAugmentions(
    ("FORCE10-BGP4-V2-MIB",
     "f10BgpM2AsPath4byteEntry")
)
f10BgpM2AsPath4byteEntry.setIndexNames(*f10BgpM2PathAttrEntry.getIndexNames())

# Managed Objects groups

f10BgpM2CommunitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 1)
)
f10BgpM2CommunitiesGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrCommIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrCommValue"))
)
if mibBuilder.loadTexts:
    f10BgpM2CommunitiesGroup.setStatus("current")

f10BgpM2ExtCommunitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 2)
)
f10BgpM2ExtCommunitiesGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrExtCommIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrExtCommValue"))
)
if mibBuilder.loadTexts:
    f10BgpM2ExtCommunitiesGroup.setStatus("current")

f10BgpM2RouteReflectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 3)
)
f10BgpM2RouteReflectionGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2RouteReflector"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2ClusterId"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerReflectorClient"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrOriginatorId"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrClusterIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrClusterValue"))
)
if mibBuilder.loadTexts:
    f10BgpM2RouteReflectionGroup.setStatus("current")

f10BgpM2AsConfederationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 4)
)
f10BgpM2AsConfederationGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2ConfederationRouter"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2ConfederationId"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerConfedMember"))
)
if mibBuilder.loadTexts:
    f10BgpM2AsConfederationGroup.setStatus("current")

f10BgpM2TimersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 5)
)
f10BgpM2TimersGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerFsmEstablishedTime"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerInUpdatesElapsedTime"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerConnectRetryInterval"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerHoldTimeConfigured"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerKeepAliveConfigured"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerMinASOrigInterval"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerMinRouteAdverInterval"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerHoldTime"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerKeepAlive"))
)
if mibBuilder.loadTexts:
    f10BgpM2TimersGroup.setStatus("current")

f10BgpM2CountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 6)
)
f10BgpM2CountersGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerInUpdates"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerOutUpdates"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerInTotalMessages"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerOutTotalMessages"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerFsmEstablishedTrans"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerInKeepalives"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerOutKeepalives"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerInOpen"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerOutOpen"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerInRteRefresh"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerOutRteRefresh"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PrefixCountersAfi"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PrefixCountersSafi"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PrefixInPrefixes"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PrefixInPrefixesAccepted"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PrefixInPrefixesRejected"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PrefixOutPrefixes"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PrefixWdrawnByPeer"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PrefixWdrawnFromPeer"))
)
if mibBuilder.loadTexts:
    f10BgpM2CountersGroup.setStatus("current")

f10BgpM2CapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 7)
)
f10BgpM2CapabilitiesGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2CapabilitySupportAvailable"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2SupportedCapabilityCode"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2SupportedCapability"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerCapAnnouncedCode"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerCapAnnouncedIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerCapAnnouncedValue"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerCapReceivedCode"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerCapReceivedIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerCapReceivedValue"))
)
if mibBuilder.loadTexts:
    f10BgpM2CapabilitiesGroup.setStatus("current")

f10BgpM2AsPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 8)
)
f10BgpM2AsPathGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathSegmentIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathElementIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathElementValue"))
)
if mibBuilder.loadTexts:
    f10BgpM2AsPathGroup.setStatus("current")

f10BgpM2As4byteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 9)
)
f10BgpM2As4byteGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2AsSize"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPath4bytePathPresent"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPath4byteAggregatorAS"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPath4byteCalcLength"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPath4byteString"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPath4byteIndex"))
)
if mibBuilder.loadTexts:
    f10BgpM2As4byteGroup.setStatus("current")

f10BgpM2BaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 10)
)
f10BgpM2BaseGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2LocalAs"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2LocalIdentifier"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2VersionIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2VersionSupported"))
)
if mibBuilder.loadTexts:
    f10BgpM2BaseGroup.setStatus("current")

f10BgpM2ErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 11)
)
f10BgpM2ErrorsGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorReceived"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorReceivedData"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorReceivedTime"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorReceivedText"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorSent"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorSentData"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorSentTime"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorSentText"))
)
if mibBuilder.loadTexts:
    f10BgpM2ErrorsGroup.setStatus("current")

f10BgpM2PeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 12)
)
f10BgpM2PeerGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerInstance"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerIdentifier"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerState"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerStatus"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerConfiguredVersion"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerNegotiatedVersion"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLocalAddrType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLocalAddr"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLocalPort"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLocalAs"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerRemoteAddrType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerRemoteAddr"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerRemotePort"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerRemoteAs"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerIndex"))
)
if mibBuilder.loadTexts:
    f10BgpM2PeerGroup.setStatus("current")

f10BgpM2PathAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 13)
)
f10BgpM2PathAttributesGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrCount"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathCalcLength"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathElementValue"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathString"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AsPathType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2NlriAfi"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2NlriBest"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2NlriPrefixType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2NlriPrefix"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2NlriPrefixLen"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2NlriSafi"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2NlriOpaqueType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2NlriOpaquePointer"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2NlriIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2NlriCalcLocalPref"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AdjRibsOutIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2AdjRibsOutRoute"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrAggregatorAS"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrAggregatorAddr"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrAtomicAggregate"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrLocalPref"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrLocalPrefPresent"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrMed"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrMedPresent"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrNextHop"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrNextHopAddrType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrOrigin"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrUnknownIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrUnknownType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PathAttrUnknownValue"))
)
if mibBuilder.loadTexts:
    f10BgpM2PathAttributesGroup.setStatus("current")

f10BgpM2PeerConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 14)
)
f10BgpM2PeerConfigurationGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgBaseScalarStorageType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgLocalAs"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgLocalIdentifier"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerAdminStatus"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerNextIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerConfiguredVersion"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgAllowVersionNegotiation"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerLocalAddrType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerLocalAddr"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerLocalAs"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerRemoteAddrType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerRemoteAddr"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerRemoteAs"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerEntryStorageType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerError"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerBgpPeerEntry"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerRowEntryStatus"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerIndex"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerStatus"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerConnectRetryInterval"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerHoldTimeConfigured"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerKeepAliveConfigured"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerMinASOrigInterval"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerMinRouteAdverInter"))
)
if mibBuilder.loadTexts:
    f10BgpM2PeerConfigurationGroup.setStatus("current")

f10BgpM2PeerRouteReflectorCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 15)
)
f10BgpM2PeerRouteReflectorCfgGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgRouteReflector"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgClusterId"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerReflectorClient"))
)
if mibBuilder.loadTexts:
    f10BgpM2PeerRouteReflectorCfgGroup.setStatus("current")

f10BgpM2PeerAsConfederationCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 16)
)
f10BgpM2PeerAsConfederationCfgGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgConfederationRouter"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgConfederationId"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2CfgPeerConfedMember"))
)
if mibBuilder.loadTexts:
    f10BgpM2PeerAsConfederationCfgGroup.setStatus("current")

f10BgpM2Rfc2545Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 18)
)
f10BgpM2Rfc2545Group.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2LinkLocalNextHopPresent"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2LinkLocalNextHop"))
)
if mibBuilder.loadTexts:
    f10BgpM2Rfc2545Group.setStatus("current")


# Notification objects

f10BgpM2Established = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 0, 1)
)
f10BgpM2Established.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLocalAddrType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLocalAddr"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerRemoteAddrType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerRemoteAddr"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorReceived"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerState"))
)
if mibBuilder.loadTexts:
    f10BgpM2Established.setStatus(
        "current"
    )

f10BgpM2BackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 0, 2)
)
f10BgpM2BackwardTransition.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLocalAddrType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLocalAddr"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerRemoteAddrType"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerRemoteAddr"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorReceived"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerLastErrorReceivedText"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2PeerState"))
)
if mibBuilder.loadTexts:
    f10BgpM2BackwardTransition.setStatus(
        "current"
    )


# Notifications groups

f10BgpM2MIBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 17)
)
f10BgpM2MIBNotificationsGroup.setObjects(
      *(("FORCE10-BGP4-V2-MIB", "f10BgpM2Established"),
        ("FORCE10-BGP4-V2-MIB", "f10BgpM2BackwardTransition"))
)
if mibBuilder.loadTexts:
    f10BgpM2MIBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f10BgpM2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    f10BgpM2MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCE10-BGP4-V2-MIB",
    **{"F10BgpM2Identifier": F10BgpM2Identifier,
       "F10BgpM2Afi": F10BgpM2Afi,
       "F10BgpM2Safi": F10BgpM2Safi,
       "F10BgpM2Community": F10BgpM2Community,
       "F10BgpM2ExtendedCommunity": F10BgpM2ExtendedCommunity,
       "f10BgpM2": f10BgpM2,
       "f10BgpM2BaseScalars": f10BgpM2BaseScalars,
       "f10BgpM2BaseNotifications": f10BgpM2BaseNotifications,
       "f10BgpM2Established": f10BgpM2Established,
       "f10BgpM2BackwardTransition": f10BgpM2BackwardTransition,
       "f10BgpM2Version": f10BgpM2Version,
       "f10BgpM2VersionTable": f10BgpM2VersionTable,
       "f10BgpM2VersionEntry": f10BgpM2VersionEntry,
       "f10BgpM2VersionIndex": f10BgpM2VersionIndex,
       "f10BgpM2VersionSupported": f10BgpM2VersionSupported,
       "f10BgpM2SupportedCapabilities": f10BgpM2SupportedCapabilities,
       "f10BgpM2CapabilitySupportAvailable": f10BgpM2CapabilitySupportAvailable,
       "f10BgpM2SupportedCapabilitiesTable": f10BgpM2SupportedCapabilitiesTable,
       "f10BgpM2SupportedCapabilitiesEntry": f10BgpM2SupportedCapabilitiesEntry,
       "f10BgpM2SupportedCapabilityCode": f10BgpM2SupportedCapabilityCode,
       "f10BgpM2SupportedCapability": f10BgpM2SupportedCapability,
       "f10BgpM2AsSize": f10BgpM2AsSize,
       "f10BgpM2LocalAs": f10BgpM2LocalAs,
       "f10BgpM2LocalIdentifier": f10BgpM2LocalIdentifier,
       "f10BgpM2BaseScalarExtensions": f10BgpM2BaseScalarExtensions,
       "f10BgpM2BaseScalarNonCapExts": f10BgpM2BaseScalarNonCapExts,
       "f10BgpM2BaseScalarRouteReflectExts": f10BgpM2BaseScalarRouteReflectExts,
       "f10BgpM2RouteReflector": f10BgpM2RouteReflector,
       "f10BgpM2ClusterId": f10BgpM2ClusterId,
       "f10BgpM2BaseScalarASConfedExts": f10BgpM2BaseScalarASConfedExts,
       "f10BgpM2ConfederationRouter": f10BgpM2ConfederationRouter,
       "f10BgpM2ConfederationId": f10BgpM2ConfederationId,
       "f10BgpM2BaseScalarCapExts": f10BgpM2BaseScalarCapExts,
       "f10BgpM2BaseScalarConfiguration": f10BgpM2BaseScalarConfiguration,
       "f10BgpM2CfgBaseScalarStorageType": f10BgpM2CfgBaseScalarStorageType,
       "f10BgpM2CfgLocalAs": f10BgpM2CfgLocalAs,
       "f10BgpM2CfgLocalIdentifier": f10BgpM2CfgLocalIdentifier,
       "f10BgpM2CfgBaseScalarExtensions": f10BgpM2CfgBaseScalarExtensions,
       "f10BgpM2CfgBaseScalarNonCapExts": f10BgpM2CfgBaseScalarNonCapExts,
       "f10BgpM2CfgBaseScalarReflectorExts": f10BgpM2CfgBaseScalarReflectorExts,
       "f10BgpM2CfgRouteReflector": f10BgpM2CfgRouteReflector,
       "f10BgpM2CfgClusterId": f10BgpM2CfgClusterId,
       "f10BgpM2CfgBaseScalarASConfedExts": f10BgpM2CfgBaseScalarASConfedExts,
       "f10BgpM2CfgConfederationRouter": f10BgpM2CfgConfederationRouter,
       "f10BgpM2CfgConfederationId": f10BgpM2CfgConfederationId,
       "f10BgpM2CfgBaseScalarCapExts": f10BgpM2CfgBaseScalarCapExts,
       "f10BgpM2Peer": f10BgpM2Peer,
       "f10BgpM2PeerData": f10BgpM2PeerData,
       "f10BgpM2PeerTable": f10BgpM2PeerTable,
       "f10BgpM2PeerEntry": f10BgpM2PeerEntry,
       "f10BgpM2PeerInstance": f10BgpM2PeerInstance,
       "f10BgpM2PeerIdentifier": f10BgpM2PeerIdentifier,
       "f10BgpM2PeerState": f10BgpM2PeerState,
       "f10BgpM2PeerStatus": f10BgpM2PeerStatus,
       "f10BgpM2PeerConfiguredVersion": f10BgpM2PeerConfiguredVersion,
       "f10BgpM2PeerNegotiatedVersion": f10BgpM2PeerNegotiatedVersion,
       "f10BgpM2PeerLocalAddrType": f10BgpM2PeerLocalAddrType,
       "f10BgpM2PeerLocalAddr": f10BgpM2PeerLocalAddr,
       "f10BgpM2PeerLocalPort": f10BgpM2PeerLocalPort,
       "f10BgpM2PeerLocalAs": f10BgpM2PeerLocalAs,
       "f10BgpM2PeerRemoteAddrType": f10BgpM2PeerRemoteAddrType,
       "f10BgpM2PeerRemoteAddr": f10BgpM2PeerRemoteAddr,
       "f10BgpM2PeerRemotePort": f10BgpM2PeerRemotePort,
       "f10BgpM2PeerRemoteAs": f10BgpM2PeerRemoteAs,
       "f10BgpM2PeerIndex": f10BgpM2PeerIndex,
       "f10BgpM2PeerErrors": f10BgpM2PeerErrors,
       "f10BgpM2PeerErrorsTable": f10BgpM2PeerErrorsTable,
       "f10BgpM2PeerErrorsEntry": f10BgpM2PeerErrorsEntry,
       "f10BgpM2PeerLastErrorReceived": f10BgpM2PeerLastErrorReceived,
       "f10BgpM2PeerLastErrorSent": f10BgpM2PeerLastErrorSent,
       "f10BgpM2PeerLastErrorReceivedTime": f10BgpM2PeerLastErrorReceivedTime,
       "f10BgpM2PeerLastErrorSentTime": f10BgpM2PeerLastErrorSentTime,
       "f10BgpM2PeerLastErrorReceivedText": f10BgpM2PeerLastErrorReceivedText,
       "f10BgpM2PeerLastErrorSentText": f10BgpM2PeerLastErrorSentText,
       "f10BgpM2PeerLastErrorReceivedData": f10BgpM2PeerLastErrorReceivedData,
       "f10BgpM2PeerLastErrorSentData": f10BgpM2PeerLastErrorSentData,
       "f10BgpM2PeerTimers": f10BgpM2PeerTimers,
       "f10BgpM2PeerEventTimesTable": f10BgpM2PeerEventTimesTable,
       "f10BgpM2PeerEventTimesEntry": f10BgpM2PeerEventTimesEntry,
       "f10BgpM2PeerFsmEstablishedTime": f10BgpM2PeerFsmEstablishedTime,
       "f10BgpM2PeerInUpdatesElapsedTime": f10BgpM2PeerInUpdatesElapsedTime,
       "f10BgpM2PeerConfiguredTimersTable": f10BgpM2PeerConfiguredTimersTable,
       "f10BgpM2PeerConfiguredTimersEntry": f10BgpM2PeerConfiguredTimersEntry,
       "f10BgpM2PeerConnectRetryInterval": f10BgpM2PeerConnectRetryInterval,
       "f10BgpM2PeerHoldTimeConfigured": f10BgpM2PeerHoldTimeConfigured,
       "f10BgpM2PeerKeepAliveConfigured": f10BgpM2PeerKeepAliveConfigured,
       "f10BgpM2PeerMinASOrigInterval": f10BgpM2PeerMinASOrigInterval,
       "f10BgpM2PeerMinRouteAdverInterval": f10BgpM2PeerMinRouteAdverInterval,
       "f10BgpM2PeerNegotiatedTimersTable": f10BgpM2PeerNegotiatedTimersTable,
       "f10BgpM2PeerNegotiatedTimersEntry": f10BgpM2PeerNegotiatedTimersEntry,
       "f10BgpM2PeerHoldTime": f10BgpM2PeerHoldTime,
       "f10BgpM2PeerKeepAlive": f10BgpM2PeerKeepAlive,
       "f10BgpM2PeerCapabilities": f10BgpM2PeerCapabilities,
       "f10BgpM2PeerCapsAnnouncedTable": f10BgpM2PeerCapsAnnouncedTable,
       "f10BgpM2PeerCapsAnnouncedEntry": f10BgpM2PeerCapsAnnouncedEntry,
       "f10BgpM2PeerCapAnnouncedCode": f10BgpM2PeerCapAnnouncedCode,
       "f10BgpM2PeerCapAnnouncedIndex": f10BgpM2PeerCapAnnouncedIndex,
       "f10BgpM2PeerCapAnnouncedValue": f10BgpM2PeerCapAnnouncedValue,
       "f10BgpM2PeerCapsReceivedTable": f10BgpM2PeerCapsReceivedTable,
       "f10BgpM2PeerCapsReceivedEntry": f10BgpM2PeerCapsReceivedEntry,
       "f10BgpM2PeerCapReceivedCode": f10BgpM2PeerCapReceivedCode,
       "f10BgpM2PeerCapReceivedIndex": f10BgpM2PeerCapReceivedIndex,
       "f10BgpM2PeerCapReceivedValue": f10BgpM2PeerCapReceivedValue,
       "f10BgpM2PeerCounters": f10BgpM2PeerCounters,
       "f10BgpM2PeerCountersTable": f10BgpM2PeerCountersTable,
       "f10BgpM2PeerCountersEntry": f10BgpM2PeerCountersEntry,
       "f10BgpM2PeerInUpdates": f10BgpM2PeerInUpdates,
       "f10BgpM2PeerOutUpdates": f10BgpM2PeerOutUpdates,
       "f10BgpM2PeerInTotalMessages": f10BgpM2PeerInTotalMessages,
       "f10BgpM2PeerOutTotalMessages": f10BgpM2PeerOutTotalMessages,
       "f10BgpM2PeerFsmEstablishedTrans": f10BgpM2PeerFsmEstablishedTrans,
       "f10BgpM2PeerInKeepalives": f10BgpM2PeerInKeepalives,
       "f10BgpM2PeerOutKeepalives": f10BgpM2PeerOutKeepalives,
       "f10BgpM2PeerInOpen": f10BgpM2PeerInOpen,
       "f10BgpM2PeerOutOpen": f10BgpM2PeerOutOpen,
       "f10BgpM2PeerInRteRefresh": f10BgpM2PeerInRteRefresh,
       "f10BgpM2PeerOutRteRefresh": f10BgpM2PeerOutRteRefresh,
       "f10BgpM2PrefixCountersTable": f10BgpM2PrefixCountersTable,
       "f10BgpM2PrefixCountersEntry": f10BgpM2PrefixCountersEntry,
       "f10BgpM2PrefixCountersAfi": f10BgpM2PrefixCountersAfi,
       "f10BgpM2PrefixCountersSafi": f10BgpM2PrefixCountersSafi,
       "f10BgpM2PrefixInPrefixes": f10BgpM2PrefixInPrefixes,
       "f10BgpM2PrefixInPrefixesAccepted": f10BgpM2PrefixInPrefixesAccepted,
       "f10BgpM2PrefixInPrefixesRejected": f10BgpM2PrefixInPrefixesRejected,
       "f10BgpM2PrefixOutPrefixes": f10BgpM2PrefixOutPrefixes,
       "f10BgpM2PrefixWdrawnByPeer": f10BgpM2PrefixWdrawnByPeer,
       "f10BgpM2PrefixWdrawnFromPeer": f10BgpM2PrefixWdrawnFromPeer,
       "f10BgpM2PeerExtensions": f10BgpM2PeerExtensions,
       "f10BgpM2PeerNonCapExts": f10BgpM2PeerNonCapExts,
       "f10BgpM2PeerRouteReflectionExts": f10BgpM2PeerRouteReflectionExts,
       "f10BgpM2PeerReflectorClientTable": f10BgpM2PeerReflectorClientTable,
       "f10BgpM2PeerReflectorClientEntry": f10BgpM2PeerReflectorClientEntry,
       "f10BgpM2PeerReflectorClient": f10BgpM2PeerReflectorClient,
       "f10BgpM2PeerASConfederationExts": f10BgpM2PeerASConfederationExts,
       "f10BgpM2PeerConfedMemberTable": f10BgpM2PeerConfedMemberTable,
       "f10BgpM2PeerConfedMemberEntry": f10BgpM2PeerConfedMemberEntry,
       "f10BgpM2PeerConfedMember": f10BgpM2PeerConfedMember,
       "f10BgpM2PeerCapExts": f10BgpM2PeerCapExts,
       "f10BgpM2PeerConfiguration": f10BgpM2PeerConfiguration,
       "f10BgpM2CfgPeerAdminStatusTable": f10BgpM2CfgPeerAdminStatusTable,
       "f10BgpM2CfgPeerAdminStatusEntry": f10BgpM2CfgPeerAdminStatusEntry,
       "f10BgpM2CfgPeerAdminStatus": f10BgpM2CfgPeerAdminStatus,
       "f10BgpM2CfgPeerNextIndex": f10BgpM2CfgPeerNextIndex,
       "f10BgpM2CfgPeerTable": f10BgpM2CfgPeerTable,
       "f10BgpM2CfgPeerEntry": f10BgpM2CfgPeerEntry,
       "f10BgpM2CfgPeerConfiguredVersion": f10BgpM2CfgPeerConfiguredVersion,
       "f10BgpM2CfgAllowVersionNegotiation": f10BgpM2CfgAllowVersionNegotiation,
       "f10BgpM2CfgPeerLocalAddrType": f10BgpM2CfgPeerLocalAddrType,
       "f10BgpM2CfgPeerLocalAddr": f10BgpM2CfgPeerLocalAddr,
       "f10BgpM2CfgPeerLocalAs": f10BgpM2CfgPeerLocalAs,
       "f10BgpM2CfgPeerRemoteAddrType": f10BgpM2CfgPeerRemoteAddrType,
       "f10BgpM2CfgPeerRemoteAddr": f10BgpM2CfgPeerRemoteAddr,
       "f10BgpM2CfgPeerRemoteAs": f10BgpM2CfgPeerRemoteAs,
       "f10BgpM2CfgPeerEntryStorageType": f10BgpM2CfgPeerEntryStorageType,
       "f10BgpM2CfgPeerError": f10BgpM2CfgPeerError,
       "f10BgpM2CfgPeerBgpPeerEntry": f10BgpM2CfgPeerBgpPeerEntry,
       "f10BgpM2CfgPeerRowEntryStatus": f10BgpM2CfgPeerRowEntryStatus,
       "f10BgpM2CfgPeerIndex": f10BgpM2CfgPeerIndex,
       "f10BgpM2CfgPeerStatus": f10BgpM2CfgPeerStatus,
       "f10BgpM2CfgPeerTimersTable": f10BgpM2CfgPeerTimersTable,
       "f10BgpM2CfgPeerTimersEntry": f10BgpM2CfgPeerTimersEntry,
       "f10BgpM2CfgPeerConnectRetryInterval": f10BgpM2CfgPeerConnectRetryInterval,
       "f10BgpM2CfgPeerHoldTimeConfigured": f10BgpM2CfgPeerHoldTimeConfigured,
       "f10BgpM2CfgPeerKeepAliveConfigured": f10BgpM2CfgPeerKeepAliveConfigured,
       "f10BgpM2CfgPeerMinASOrigInterval": f10BgpM2CfgPeerMinASOrigInterval,
       "f10BgpM2CfgPeerMinRouteAdverInter": f10BgpM2CfgPeerMinRouteAdverInter,
       "f10BgpM2CfgPeerExtensions": f10BgpM2CfgPeerExtensions,
       "f10BgpM2CfgPeerNonCapExts": f10BgpM2CfgPeerNonCapExts,
       "f10BgpM2CfgPeerRouteReflectionExts": f10BgpM2CfgPeerRouteReflectionExts,
       "f10BgpM2CfgPeerReflectorClientTable": f10BgpM2CfgPeerReflectorClientTable,
       "f10BgpM2CfgPeerReflectorClientEntry": f10BgpM2CfgPeerReflectorClientEntry,
       "f10BgpM2CfgPeerReflectorClient": f10BgpM2CfgPeerReflectorClient,
       "f10BgpM2CfgPeerASConfederationExts": f10BgpM2CfgPeerASConfederationExts,
       "f10BgpM2CfgPeerConfedMemberTable": f10BgpM2CfgPeerConfedMemberTable,
       "f10BgpM2CfgPeerConfedMemberEntry": f10BgpM2CfgPeerConfedMemberEntry,
       "f10BgpM2CfgPeerConfedMember": f10BgpM2CfgPeerConfedMember,
       "f10BgpM2CfgPeerCapExts": f10BgpM2CfgPeerCapExts,
       "f10BgpM2Rib": f10BgpM2Rib,
       "f10BgpM2NlriTable": f10BgpM2NlriTable,
       "f10BgpM2NlriEntry": f10BgpM2NlriEntry,
       "f10BgpM2NlriIndex": f10BgpM2NlriIndex,
       "f10BgpM2NlriAfi": f10BgpM2NlriAfi,
       "f10BgpM2NlriSafi": f10BgpM2NlriSafi,
       "f10BgpM2NlriPrefixType": f10BgpM2NlriPrefixType,
       "f10BgpM2NlriPrefix": f10BgpM2NlriPrefix,
       "f10BgpM2NlriPrefixLen": f10BgpM2NlriPrefixLen,
       "f10BgpM2NlriBest": f10BgpM2NlriBest,
       "f10BgpM2NlriCalcLocalPref": f10BgpM2NlriCalcLocalPref,
       "f10BgpM2PathAttrIndex": f10BgpM2PathAttrIndex,
       "f10BgpM2NlriOpaqueType": f10BgpM2NlriOpaqueType,
       "f10BgpM2NlriOpaquePointer": f10BgpM2NlriOpaquePointer,
       "f10BgpM2AdjRibsOutTable": f10BgpM2AdjRibsOutTable,
       "f10BgpM2AdjRibsOutEntry": f10BgpM2AdjRibsOutEntry,
       "f10BgpM2AdjRibsOutIndex": f10BgpM2AdjRibsOutIndex,
       "f10BgpM2AdjRibsOutRoute": f10BgpM2AdjRibsOutRoute,
       "f10BgpM2PathAttrCount": f10BgpM2PathAttrCount,
       "f10BgpM2PathAttrTable": f10BgpM2PathAttrTable,
       "f10BgpM2PathAttrEntry": f10BgpM2PathAttrEntry,
       "f10BgpM2PathAttrOrigin": f10BgpM2PathAttrOrigin,
       "f10BgpM2PathAttrNextHopAddrType": f10BgpM2PathAttrNextHopAddrType,
       "f10BgpM2PathAttrNextHop": f10BgpM2PathAttrNextHop,
       "f10BgpM2PathAttrMedPresent": f10BgpM2PathAttrMedPresent,
       "f10BgpM2PathAttrMed": f10BgpM2PathAttrMed,
       "f10BgpM2PathAttrLocalPrefPresent": f10BgpM2PathAttrLocalPrefPresent,
       "f10BgpM2PathAttrLocalPref": f10BgpM2PathAttrLocalPref,
       "f10BgpM2PathAttrAtomicAggregate": f10BgpM2PathAttrAtomicAggregate,
       "f10BgpM2PathAttrAggregatorAS": f10BgpM2PathAttrAggregatorAS,
       "f10BgpM2PathAttrAggregatorAddr": f10BgpM2PathAttrAggregatorAddr,
       "f10BgpM2AsPathCalcLength": f10BgpM2AsPathCalcLength,
       "f10BgpM2AsPathString": f10BgpM2AsPathString,
       "f10BgpM2AsPathIndex": f10BgpM2AsPathIndex,
       "f10BgpM2AsPath4byteTable": f10BgpM2AsPath4byteTable,
       "f10BgpM2AsPath4byteEntry": f10BgpM2AsPath4byteEntry,
       "f10BgpM2AsPath4bytePathPresent": f10BgpM2AsPath4bytePathPresent,
       "f10BgpM2AsPath4byteAggregatorAS": f10BgpM2AsPath4byteAggregatorAS,
       "f10BgpM2AsPath4byteCalcLength": f10BgpM2AsPath4byteCalcLength,
       "f10BgpM2AsPath4byteString": f10BgpM2AsPath4byteString,
       "f10BgpM2AsPath4byteIndex": f10BgpM2AsPath4byteIndex,
       "f10BgpM2AsPathTable": f10BgpM2AsPathTable,
       "f10BgpM2AsPathTableEntry": f10BgpM2AsPathTableEntry,
       "f10BgpM2AsPathSegmentIndex": f10BgpM2AsPathSegmentIndex,
       "f10BgpM2AsPathElementIndex": f10BgpM2AsPathElementIndex,
       "f10BgpM2AsPathType": f10BgpM2AsPathType,
       "f10BgpM2AsPathElementValue": f10BgpM2AsPathElementValue,
       "f10BgpM2PathAttrUnknownTable": f10BgpM2PathAttrUnknownTable,
       "f10BgpM2PathAttrUnknownEntry": f10BgpM2PathAttrUnknownEntry,
       "f10BgpM2PathAttrUnknownIndex": f10BgpM2PathAttrUnknownIndex,
       "f10BgpM2PathAttrUnknownType": f10BgpM2PathAttrUnknownType,
       "f10BgpM2PathAttrUnknownValue": f10BgpM2PathAttrUnknownValue,
       "f10BgpM2PathAttrExtensions": f10BgpM2PathAttrExtensions,
       "f10BgpM2PathAttrNonCapExts": f10BgpM2PathAttrNonCapExts,
       "f10BgpM2PathAttrCommunityExts": f10BgpM2PathAttrCommunityExts,
       "f10BgpM2PathAttrCommTable": f10BgpM2PathAttrCommTable,
       "f10BgpM2PathAttrCommEntry": f10BgpM2PathAttrCommEntry,
       "f10BgpM2PathAttrCommIndex": f10BgpM2PathAttrCommIndex,
       "f10BgpM2PathAttrCommValue": f10BgpM2PathAttrCommValue,
       "f10BgpM2LinkLocalNextHopTable": f10BgpM2LinkLocalNextHopTable,
       "f10BgpM2LinkLocalNextHopEntry": f10BgpM2LinkLocalNextHopEntry,
       "f10BgpM2LinkLocalNextHopPresent": f10BgpM2LinkLocalNextHopPresent,
       "f10BgpM2LinkLocalNextHop": f10BgpM2LinkLocalNextHop,
       "f10BgpM2PathAttrRouteReflectionExts": f10BgpM2PathAttrRouteReflectionExts,
       "f10BgpM2PathAttrOriginatorIdTable": f10BgpM2PathAttrOriginatorIdTable,
       "f10BgpM2PathAttrOriginatorIdEntry": f10BgpM2PathAttrOriginatorIdEntry,
       "f10BgpM2PathAttrOriginatorId": f10BgpM2PathAttrOriginatorId,
       "f10BgpM2PathAttrClusterTable": f10BgpM2PathAttrClusterTable,
       "f10BgpM2PathAttrClusterEntry": f10BgpM2PathAttrClusterEntry,
       "f10BgpM2PathAttrClusterIndex": f10BgpM2PathAttrClusterIndex,
       "f10BgpM2PathAttrClusterValue": f10BgpM2PathAttrClusterValue,
       "f10BgpM2PathAttrExtCommTable": f10BgpM2PathAttrExtCommTable,
       "f10BgpM2PathAttrExtCommEntry": f10BgpM2PathAttrExtCommEntry,
       "f10BgpM2PathAttrExtCommIndex": f10BgpM2PathAttrExtCommIndex,
       "f10BgpM2PathAttrExtCommValue": f10BgpM2PathAttrExtCommValue,
       "f10BgpM2PathAttrCapExts": f10BgpM2PathAttrCapExts,
       "f10BgpM2Conformance": f10BgpM2Conformance,
       "f10BgpM2MIBCompliances": f10BgpM2MIBCompliances,
       "f10BgpM2MIBCompliance": f10BgpM2MIBCompliance,
       "f10BgpM2MIBGroups": f10BgpM2MIBGroups,
       "f10BgpM2CommunitiesGroup": f10BgpM2CommunitiesGroup,
       "f10BgpM2ExtCommunitiesGroup": f10BgpM2ExtCommunitiesGroup,
       "f10BgpM2RouteReflectionGroup": f10BgpM2RouteReflectionGroup,
       "f10BgpM2AsConfederationGroup": f10BgpM2AsConfederationGroup,
       "f10BgpM2TimersGroup": f10BgpM2TimersGroup,
       "f10BgpM2CountersGroup": f10BgpM2CountersGroup,
       "f10BgpM2CapabilitiesGroup": f10BgpM2CapabilitiesGroup,
       "f10BgpM2AsPathGroup": f10BgpM2AsPathGroup,
       "f10BgpM2As4byteGroup": f10BgpM2As4byteGroup,
       "f10BgpM2BaseGroup": f10BgpM2BaseGroup,
       "f10BgpM2ErrorsGroup": f10BgpM2ErrorsGroup,
       "f10BgpM2PeerGroup": f10BgpM2PeerGroup,
       "f10BgpM2PathAttributesGroup": f10BgpM2PathAttributesGroup,
       "f10BgpM2PeerConfigurationGroup": f10BgpM2PeerConfigurationGroup,
       "f10BgpM2PeerRouteReflectorCfgGroup": f10BgpM2PeerRouteReflectorCfgGroup,
       "f10BgpM2PeerAsConfederationCfgGroup": f10BgpM2PeerAsConfederationCfgGroup,
       "f10BgpM2MIBNotificationsGroup": f10BgpM2MIBNotificationsGroup,
       "f10BgpM2Rfc2545Group": f10BgpM2Rfc2545Group}
)
