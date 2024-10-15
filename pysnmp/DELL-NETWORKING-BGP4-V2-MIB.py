# SNMP MIB module (DELL-NETWORKING-BGP4-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-BGP4-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:47 2024
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

(dellNetExperiment,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetExperiment")

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

dellNetBgpM2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1)
)
dellNetBgpM2.setRevisions(
        ("2007-04-27 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DellNetBgpM2Identifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class DellNetBgpM2Afi(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class DellNetBgpM2Safi(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class DellNetBgpM2Community(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class DellNetBgpM2ExtendedCommunity(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_DellNetBgpM2BaseScalars_ObjectIdentity = ObjectIdentity
dellNetBgpM2BaseScalars = _DellNetBgpM2BaseScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1)
)
_DellNetBgpM2BaseNotifications_ObjectIdentity = ObjectIdentity
dellNetBgpM2BaseNotifications = _DellNetBgpM2BaseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 0)
)
_DellNetBgpM2Version_ObjectIdentity = ObjectIdentity
dellNetBgpM2Version = _DellNetBgpM2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 1)
)
_DellNetBgpM2VersionTable_Object = MibTable
dellNetBgpM2VersionTable = _DellNetBgpM2VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2VersionTable.setStatus("current")
_DellNetBgpM2VersionEntry_Object = MibTableRow
dellNetBgpM2VersionEntry = _DellNetBgpM2VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 1, 1, 1)
)
dellNetBgpM2VersionEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2VersionIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2VersionEntry.setStatus("current")


class _DellNetBgpM2VersionIndex_Type(Unsigned32):
    """Custom type dellNetBgpM2VersionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DellNetBgpM2VersionIndex_Type.__name__ = "Unsigned32"
_DellNetBgpM2VersionIndex_Object = MibTableColumn
dellNetBgpM2VersionIndex = _DellNetBgpM2VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 1, 1, 1, 1),
    _DellNetBgpM2VersionIndex_Type()
)
dellNetBgpM2VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2VersionIndex.setStatus("current")
_DellNetBgpM2VersionSupported_Type = TruthValue
_DellNetBgpM2VersionSupported_Object = MibTableColumn
dellNetBgpM2VersionSupported = _DellNetBgpM2VersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 1, 1, 1, 2),
    _DellNetBgpM2VersionSupported_Type()
)
dellNetBgpM2VersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2VersionSupported.setStatus("current")
_DellNetBgpM2SupportedCapabilities_ObjectIdentity = ObjectIdentity
dellNetBgpM2SupportedCapabilities = _DellNetBgpM2SupportedCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2)
)
_DellNetBgpM2CapabilitySupportAvailable_Type = TruthValue
_DellNetBgpM2CapabilitySupportAvailable_Object = MibScalar
dellNetBgpM2CapabilitySupportAvailable = _DellNetBgpM2CapabilitySupportAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2, 1),
    _DellNetBgpM2CapabilitySupportAvailable_Type()
)
dellNetBgpM2CapabilitySupportAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2CapabilitySupportAvailable.setStatus("current")
_DellNetBgpM2SupportedCapabilitiesTable_Object = MibTable
dellNetBgpM2SupportedCapabilitiesTable = _DellNetBgpM2SupportedCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dellNetBgpM2SupportedCapabilitiesTable.setStatus("current")
_DellNetBgpM2SupportedCapabilitiesEntry_Object = MibTableRow
dellNetBgpM2SupportedCapabilitiesEntry = _DellNetBgpM2SupportedCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2, 2, 1)
)
dellNetBgpM2SupportedCapabilitiesEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2SupportedCapabilityCode"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2SupportedCapabilitiesEntry.setStatus("current")


class _DellNetBgpM2SupportedCapabilityCode_Type(Unsigned32):
    """Custom type dellNetBgpM2SupportedCapabilityCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DellNetBgpM2SupportedCapabilityCode_Type.__name__ = "Unsigned32"
_DellNetBgpM2SupportedCapabilityCode_Object = MibTableColumn
dellNetBgpM2SupportedCapabilityCode = _DellNetBgpM2SupportedCapabilityCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2, 2, 1, 1),
    _DellNetBgpM2SupportedCapabilityCode_Type()
)
dellNetBgpM2SupportedCapabilityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2SupportedCapabilityCode.setStatus("current")
_DellNetBgpM2SupportedCapability_Type = TruthValue
_DellNetBgpM2SupportedCapability_Object = MibTableColumn
dellNetBgpM2SupportedCapability = _DellNetBgpM2SupportedCapability_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 2, 2, 1, 2),
    _DellNetBgpM2SupportedCapability_Type()
)
dellNetBgpM2SupportedCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2SupportedCapability.setStatus("current")


class _DellNetBgpM2AsSize_Type(Integer32):
    """Custom type dellNetBgpM2AsSize based on Integer32"""
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


_DellNetBgpM2AsSize_Type.__name__ = "Integer32"
_DellNetBgpM2AsSize_Object = MibScalar
dellNetBgpM2AsSize = _DellNetBgpM2AsSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 4),
    _DellNetBgpM2AsSize_Type()
)
dellNetBgpM2AsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsSize.setStatus("current")
_DellNetBgpM2LocalAs_Type = InetAutonomousSystemNumber
_DellNetBgpM2LocalAs_Object = MibScalar
dellNetBgpM2LocalAs = _DellNetBgpM2LocalAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 5),
    _DellNetBgpM2LocalAs_Type()
)
dellNetBgpM2LocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2LocalAs.setStatus("current")
_DellNetBgpM2LocalIdentifier_Type = DellNetBgpM2Identifier
_DellNetBgpM2LocalIdentifier_Object = MibScalar
dellNetBgpM2LocalIdentifier = _DellNetBgpM2LocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 6),
    _DellNetBgpM2LocalIdentifier_Type()
)
dellNetBgpM2LocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2LocalIdentifier.setStatus("current")
_DellNetBgpM2BaseScalarExtensions_ObjectIdentity = ObjectIdentity
dellNetBgpM2BaseScalarExtensions = _DellNetBgpM2BaseScalarExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7)
)
_DellNetBgpM2BaseScalarNonCapExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2BaseScalarNonCapExts = _DellNetBgpM2BaseScalarNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1)
)
_DellNetBgpM2BaseScalarRouteReflectExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2BaseScalarRouteReflectExts = _DellNetBgpM2BaseScalarRouteReflectExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 2796)
)
_DellNetBgpM2RouteReflector_Type = TruthValue
_DellNetBgpM2RouteReflector_Object = MibScalar
dellNetBgpM2RouteReflector = _DellNetBgpM2RouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 2796, 1),
    _DellNetBgpM2RouteReflector_Type()
)
dellNetBgpM2RouteReflector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2RouteReflector.setStatus("current")
_DellNetBgpM2ClusterId_Type = DellNetBgpM2Identifier
_DellNetBgpM2ClusterId_Object = MibScalar
dellNetBgpM2ClusterId = _DellNetBgpM2ClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 2796, 2),
    _DellNetBgpM2ClusterId_Type()
)
dellNetBgpM2ClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2ClusterId.setStatus("current")
_DellNetBgpM2BaseScalarASConfedExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2BaseScalarASConfedExts = _DellNetBgpM2BaseScalarASConfedExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 3065)
)
_DellNetBgpM2ConfederationRouter_Type = TruthValue
_DellNetBgpM2ConfederationRouter_Object = MibScalar
dellNetBgpM2ConfederationRouter = _DellNetBgpM2ConfederationRouter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 3065, 1),
    _DellNetBgpM2ConfederationRouter_Type()
)
dellNetBgpM2ConfederationRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2ConfederationRouter.setStatus("current")
_DellNetBgpM2ConfederationId_Type = InetAutonomousSystemNumber
_DellNetBgpM2ConfederationId_Object = MibScalar
dellNetBgpM2ConfederationId = _DellNetBgpM2ConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 1, 3065, 2),
    _DellNetBgpM2ConfederationId_Type()
)
dellNetBgpM2ConfederationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2ConfederationId.setStatus("current")
_DellNetBgpM2BaseScalarCapExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2BaseScalarCapExts = _DellNetBgpM2BaseScalarCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 7, 2)
)
_DellNetBgpM2BaseScalarConfiguration_ObjectIdentity = ObjectIdentity
dellNetBgpM2BaseScalarConfiguration = _DellNetBgpM2BaseScalarConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8)
)
_DellNetBgpM2CfgBaseScalarStorageType_Type = StorageType
_DellNetBgpM2CfgBaseScalarStorageType_Object = MibScalar
dellNetBgpM2CfgBaseScalarStorageType = _DellNetBgpM2CfgBaseScalarStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 1),
    _DellNetBgpM2CfgBaseScalarStorageType_Type()
)
dellNetBgpM2CfgBaseScalarStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgBaseScalarStorageType.setStatus("current")
_DellNetBgpM2CfgLocalAs_Type = InetAutonomousSystemNumber
_DellNetBgpM2CfgLocalAs_Object = MibScalar
dellNetBgpM2CfgLocalAs = _DellNetBgpM2CfgLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 2),
    _DellNetBgpM2CfgLocalAs_Type()
)
dellNetBgpM2CfgLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgLocalAs.setStatus("current")
_DellNetBgpM2CfgLocalIdentifier_Type = DellNetBgpM2Identifier
_DellNetBgpM2CfgLocalIdentifier_Object = MibScalar
dellNetBgpM2CfgLocalIdentifier = _DellNetBgpM2CfgLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 3),
    _DellNetBgpM2CfgLocalIdentifier_Type()
)
dellNetBgpM2CfgLocalIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgLocalIdentifier.setStatus("current")
_DellNetBgpM2CfgBaseScalarExtensions_ObjectIdentity = ObjectIdentity
dellNetBgpM2CfgBaseScalarExtensions = _DellNetBgpM2CfgBaseScalarExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4)
)
_DellNetBgpM2CfgBaseScalarNonCapExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2CfgBaseScalarNonCapExts = _DellNetBgpM2CfgBaseScalarNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1)
)
_DellNetBgpM2CfgBaseScalarReflectorExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2CfgBaseScalarReflectorExts = _DellNetBgpM2CfgBaseScalarReflectorExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 2796)
)
_DellNetBgpM2CfgRouteReflector_Type = TruthValue
_DellNetBgpM2CfgRouteReflector_Object = MibScalar
dellNetBgpM2CfgRouteReflector = _DellNetBgpM2CfgRouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 2796, 1),
    _DellNetBgpM2CfgRouteReflector_Type()
)
dellNetBgpM2CfgRouteReflector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgRouteReflector.setStatus("current")
_DellNetBgpM2CfgClusterId_Type = DellNetBgpM2Identifier
_DellNetBgpM2CfgClusterId_Object = MibScalar
dellNetBgpM2CfgClusterId = _DellNetBgpM2CfgClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 2796, 2),
    _DellNetBgpM2CfgClusterId_Type()
)
dellNetBgpM2CfgClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgClusterId.setStatus("current")
_DellNetBgpM2CfgBaseScalarASConfedExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2CfgBaseScalarASConfedExts = _DellNetBgpM2CfgBaseScalarASConfedExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 3065)
)
_DellNetBgpM2CfgConfederationRouter_Type = TruthValue
_DellNetBgpM2CfgConfederationRouter_Object = MibScalar
dellNetBgpM2CfgConfederationRouter = _DellNetBgpM2CfgConfederationRouter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 3065, 1),
    _DellNetBgpM2CfgConfederationRouter_Type()
)
dellNetBgpM2CfgConfederationRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgConfederationRouter.setStatus("current")
_DellNetBgpM2CfgConfederationId_Type = InetAutonomousSystemNumber
_DellNetBgpM2CfgConfederationId_Object = MibScalar
dellNetBgpM2CfgConfederationId = _DellNetBgpM2CfgConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 1, 3065, 2),
    _DellNetBgpM2CfgConfederationId_Type()
)
dellNetBgpM2CfgConfederationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgConfederationId.setStatus("current")
_DellNetBgpM2CfgBaseScalarCapExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2CfgBaseScalarCapExts = _DellNetBgpM2CfgBaseScalarCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 8, 4, 2)
)
_DellNetBgpM2Peer_ObjectIdentity = ObjectIdentity
dellNetBgpM2Peer = _DellNetBgpM2Peer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2)
)
_DellNetBgpM2PeerData_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerData = _DellNetBgpM2PeerData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1)
)
_DellNetBgpM2PeerTable_Object = MibTable
dellNetBgpM2PeerTable = _DellNetBgpM2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerTable.setStatus("current")
_DellNetBgpM2PeerEntry_Object = MibTableRow
dellNetBgpM2PeerEntry = _DellNetBgpM2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1)
)
dellNetBgpM2PeerEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerInstance"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLocalAddrType"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLocalAddr"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerRemoteAddrType"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerEntry.setStatus("current")
_DellNetBgpM2PeerInstance_Type = Unsigned32
_DellNetBgpM2PeerInstance_Object = MibTableColumn
dellNetBgpM2PeerInstance = _DellNetBgpM2PeerInstance_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 1),
    _DellNetBgpM2PeerInstance_Type()
)
dellNetBgpM2PeerInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerInstance.setStatus("current")
_DellNetBgpM2PeerIdentifier_Type = DellNetBgpM2Identifier
_DellNetBgpM2PeerIdentifier_Object = MibTableColumn
dellNetBgpM2PeerIdentifier = _DellNetBgpM2PeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 2),
    _DellNetBgpM2PeerIdentifier_Type()
)
dellNetBgpM2PeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerIdentifier.setStatus("current")


class _DellNetBgpM2PeerState_Type(Integer32):
    """Custom type dellNetBgpM2PeerState based on Integer32"""
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


_DellNetBgpM2PeerState_Type.__name__ = "Integer32"
_DellNetBgpM2PeerState_Object = MibTableColumn
dellNetBgpM2PeerState = _DellNetBgpM2PeerState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 3),
    _DellNetBgpM2PeerState_Type()
)
dellNetBgpM2PeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerState.setStatus("current")


class _DellNetBgpM2PeerStatus_Type(Integer32):
    """Custom type dellNetBgpM2PeerStatus based on Integer32"""
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


_DellNetBgpM2PeerStatus_Type.__name__ = "Integer32"
_DellNetBgpM2PeerStatus_Object = MibTableColumn
dellNetBgpM2PeerStatus = _DellNetBgpM2PeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 4),
    _DellNetBgpM2PeerStatus_Type()
)
dellNetBgpM2PeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerStatus.setStatus("current")


class _DellNetBgpM2PeerConfiguredVersion_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerConfiguredVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DellNetBgpM2PeerConfiguredVersion_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerConfiguredVersion_Object = MibTableColumn
dellNetBgpM2PeerConfiguredVersion = _DellNetBgpM2PeerConfiguredVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 5),
    _DellNetBgpM2PeerConfiguredVersion_Type()
)
dellNetBgpM2PeerConfiguredVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerConfiguredVersion.setStatus("current")


class _DellNetBgpM2PeerNegotiatedVersion_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerNegotiatedVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DellNetBgpM2PeerNegotiatedVersion_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerNegotiatedVersion_Object = MibTableColumn
dellNetBgpM2PeerNegotiatedVersion = _DellNetBgpM2PeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 6),
    _DellNetBgpM2PeerNegotiatedVersion_Type()
)
dellNetBgpM2PeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerNegotiatedVersion.setStatus("current")
_DellNetBgpM2PeerLocalAddrType_Type = InetAddressType
_DellNetBgpM2PeerLocalAddrType_Object = MibTableColumn
dellNetBgpM2PeerLocalAddrType = _DellNetBgpM2PeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 7),
    _DellNetBgpM2PeerLocalAddrType_Type()
)
dellNetBgpM2PeerLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLocalAddrType.setStatus("current")


class _DellNetBgpM2PeerLocalAddr_Type(InetAddress):
    """Custom type dellNetBgpM2PeerLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_DellNetBgpM2PeerLocalAddr_Type.__name__ = "InetAddress"
_DellNetBgpM2PeerLocalAddr_Object = MibTableColumn
dellNetBgpM2PeerLocalAddr = _DellNetBgpM2PeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 8),
    _DellNetBgpM2PeerLocalAddr_Type()
)
dellNetBgpM2PeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLocalAddr.setStatus("current")
_DellNetBgpM2PeerLocalPort_Type = InetPortNumber
_DellNetBgpM2PeerLocalPort_Object = MibTableColumn
dellNetBgpM2PeerLocalPort = _DellNetBgpM2PeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 9),
    _DellNetBgpM2PeerLocalPort_Type()
)
dellNetBgpM2PeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLocalPort.setStatus("current")
_DellNetBgpM2PeerLocalAs_Type = InetAutonomousSystemNumber
_DellNetBgpM2PeerLocalAs_Object = MibTableColumn
dellNetBgpM2PeerLocalAs = _DellNetBgpM2PeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 10),
    _DellNetBgpM2PeerLocalAs_Type()
)
dellNetBgpM2PeerLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLocalAs.setStatus("current")
_DellNetBgpM2PeerRemoteAddrType_Type = InetAddressType
_DellNetBgpM2PeerRemoteAddrType_Object = MibTableColumn
dellNetBgpM2PeerRemoteAddrType = _DellNetBgpM2PeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 11),
    _DellNetBgpM2PeerRemoteAddrType_Type()
)
dellNetBgpM2PeerRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerRemoteAddrType.setStatus("current")


class _DellNetBgpM2PeerRemoteAddr_Type(InetAddress):
    """Custom type dellNetBgpM2PeerRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_DellNetBgpM2PeerRemoteAddr_Type.__name__ = "InetAddress"
_DellNetBgpM2PeerRemoteAddr_Object = MibTableColumn
dellNetBgpM2PeerRemoteAddr = _DellNetBgpM2PeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 12),
    _DellNetBgpM2PeerRemoteAddr_Type()
)
dellNetBgpM2PeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerRemoteAddr.setStatus("current")
_DellNetBgpM2PeerRemotePort_Type = InetPortNumber
_DellNetBgpM2PeerRemotePort_Object = MibTableColumn
dellNetBgpM2PeerRemotePort = _DellNetBgpM2PeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 13),
    _DellNetBgpM2PeerRemotePort_Type()
)
dellNetBgpM2PeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerRemotePort.setStatus("current")
_DellNetBgpM2PeerRemoteAs_Type = InetAutonomousSystemNumber
_DellNetBgpM2PeerRemoteAs_Object = MibTableColumn
dellNetBgpM2PeerRemoteAs = _DellNetBgpM2PeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 14),
    _DellNetBgpM2PeerRemoteAs_Type()
)
dellNetBgpM2PeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerRemoteAs.setStatus("current")
_DellNetBgpM2PeerIndex_Type = Unsigned32
_DellNetBgpM2PeerIndex_Object = MibTableColumn
dellNetBgpM2PeerIndex = _DellNetBgpM2PeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 1, 1, 1, 15),
    _DellNetBgpM2PeerIndex_Type()
)
dellNetBgpM2PeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerIndex.setStatus("current")
_DellNetBgpM2PeerErrors_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerErrors = _DellNetBgpM2PeerErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2)
)
_DellNetBgpM2PeerErrorsTable_Object = MibTable
dellNetBgpM2PeerErrorsTable = _DellNetBgpM2PeerErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerErrorsTable.setStatus("current")
_DellNetBgpM2PeerErrorsEntry_Object = MibTableRow
dellNetBgpM2PeerErrorsEntry = _DellNetBgpM2PeerErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerErrorsEntry.setStatus("current")


class _DellNetBgpM2PeerLastErrorReceived_Type(OctetString):
    """Custom type dellNetBgpM2PeerLastErrorReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DellNetBgpM2PeerLastErrorReceived_Type.__name__ = "OctetString"
_DellNetBgpM2PeerLastErrorReceived_Object = MibTableColumn
dellNetBgpM2PeerLastErrorReceived = _DellNetBgpM2PeerLastErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 1),
    _DellNetBgpM2PeerLastErrorReceived_Type()
)
dellNetBgpM2PeerLastErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLastErrorReceived.setStatus("current")


class _DellNetBgpM2PeerLastErrorSent_Type(OctetString):
    """Custom type dellNetBgpM2PeerLastErrorSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DellNetBgpM2PeerLastErrorSent_Type.__name__ = "OctetString"
_DellNetBgpM2PeerLastErrorSent_Object = MibTableColumn
dellNetBgpM2PeerLastErrorSent = _DellNetBgpM2PeerLastErrorSent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 2),
    _DellNetBgpM2PeerLastErrorSent_Type()
)
dellNetBgpM2PeerLastErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLastErrorSent.setStatus("current")
_DellNetBgpM2PeerLastErrorReceivedTime_Type = TimeTicks
_DellNetBgpM2PeerLastErrorReceivedTime_Object = MibTableColumn
dellNetBgpM2PeerLastErrorReceivedTime = _DellNetBgpM2PeerLastErrorReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 3),
    _DellNetBgpM2PeerLastErrorReceivedTime_Type()
)
dellNetBgpM2PeerLastErrorReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLastErrorReceivedTime.setStatus("current")
_DellNetBgpM2PeerLastErrorSentTime_Type = TimeTicks
_DellNetBgpM2PeerLastErrorSentTime_Object = MibTableColumn
dellNetBgpM2PeerLastErrorSentTime = _DellNetBgpM2PeerLastErrorSentTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 4),
    _DellNetBgpM2PeerLastErrorSentTime_Type()
)
dellNetBgpM2PeerLastErrorSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLastErrorSentTime.setStatus("current")
_DellNetBgpM2PeerLastErrorReceivedText_Type = SnmpAdminString
_DellNetBgpM2PeerLastErrorReceivedText_Object = MibTableColumn
dellNetBgpM2PeerLastErrorReceivedText = _DellNetBgpM2PeerLastErrorReceivedText_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 5),
    _DellNetBgpM2PeerLastErrorReceivedText_Type()
)
dellNetBgpM2PeerLastErrorReceivedText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLastErrorReceivedText.setStatus("current")
_DellNetBgpM2PeerLastErrorSentText_Type = SnmpAdminString
_DellNetBgpM2PeerLastErrorSentText_Object = MibTableColumn
dellNetBgpM2PeerLastErrorSentText = _DellNetBgpM2PeerLastErrorSentText_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 6),
    _DellNetBgpM2PeerLastErrorSentText_Type()
)
dellNetBgpM2PeerLastErrorSentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLastErrorSentText.setStatus("current")


class _DellNetBgpM2PeerLastErrorReceivedData_Type(OctetString):
    """Custom type dellNetBgpM2PeerLastErrorReceivedData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_DellNetBgpM2PeerLastErrorReceivedData_Type.__name__ = "OctetString"
_DellNetBgpM2PeerLastErrorReceivedData_Object = MibTableColumn
dellNetBgpM2PeerLastErrorReceivedData = _DellNetBgpM2PeerLastErrorReceivedData_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 7),
    _DellNetBgpM2PeerLastErrorReceivedData_Type()
)
dellNetBgpM2PeerLastErrorReceivedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLastErrorReceivedData.setStatus("current")


class _DellNetBgpM2PeerLastErrorSentData_Type(OctetString):
    """Custom type dellNetBgpM2PeerLastErrorSentData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_DellNetBgpM2PeerLastErrorSentData_Type.__name__ = "OctetString"
_DellNetBgpM2PeerLastErrorSentData_Object = MibTableColumn
dellNetBgpM2PeerLastErrorSentData = _DellNetBgpM2PeerLastErrorSentData_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 2, 1, 1, 8),
    _DellNetBgpM2PeerLastErrorSentData_Type()
)
dellNetBgpM2PeerLastErrorSentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerLastErrorSentData.setStatus("current")
_DellNetBgpM2PeerTimers_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerTimers = _DellNetBgpM2PeerTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3)
)
_DellNetBgpM2PeerEventTimesTable_Object = MibTable
dellNetBgpM2PeerEventTimesTable = _DellNetBgpM2PeerEventTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerEventTimesTable.setStatus("current")
_DellNetBgpM2PeerEventTimesEntry_Object = MibTableRow
dellNetBgpM2PeerEventTimesEntry = _DellNetBgpM2PeerEventTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerEventTimesEntry.setStatus("current")
_DellNetBgpM2PeerFsmEstablishedTime_Type = Gauge32
_DellNetBgpM2PeerFsmEstablishedTime_Object = MibTableColumn
dellNetBgpM2PeerFsmEstablishedTime = _DellNetBgpM2PeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 1, 1, 1),
    _DellNetBgpM2PeerFsmEstablishedTime_Type()
)
dellNetBgpM2PeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerFsmEstablishedTime.setStatus("current")
_DellNetBgpM2PeerInUpdatesElapsedTime_Type = Gauge32
_DellNetBgpM2PeerInUpdatesElapsedTime_Object = MibTableColumn
dellNetBgpM2PeerInUpdatesElapsedTime = _DellNetBgpM2PeerInUpdatesElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 1, 1, 2),
    _DellNetBgpM2PeerInUpdatesElapsedTime_Type()
)
dellNetBgpM2PeerInUpdatesElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerInUpdatesElapsedTime.setStatus("current")
_DellNetBgpM2PeerConfiguredTimersTable_Object = MibTable
dellNetBgpM2PeerConfiguredTimersTable = _DellNetBgpM2PeerConfiguredTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerConfiguredTimersTable.setStatus("current")
_DellNetBgpM2PeerConfiguredTimersEntry_Object = MibTableRow
dellNetBgpM2PeerConfiguredTimersEntry = _DellNetBgpM2PeerConfiguredTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerConfiguredTimersEntry.setStatus("current")


class _DellNetBgpM2PeerConnectRetryInterval_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerConnectRetryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DellNetBgpM2PeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerConnectRetryInterval_Object = MibTableColumn
dellNetBgpM2PeerConnectRetryInterval = _DellNetBgpM2PeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1, 1),
    _DellNetBgpM2PeerConnectRetryInterval_Type()
)
dellNetBgpM2PeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerConnectRetryInterval.setStatus("current")


class _DellNetBgpM2PeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerHoldTimeConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_DellNetBgpM2PeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerHoldTimeConfigured_Object = MibTableColumn
dellNetBgpM2PeerHoldTimeConfigured = _DellNetBgpM2PeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1, 2),
    _DellNetBgpM2PeerHoldTimeConfigured_Type()
)
dellNetBgpM2PeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerHoldTimeConfigured.setStatus("current")


class _DellNetBgpM2PeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerKeepAliveConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_DellNetBgpM2PeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerKeepAliveConfigured_Object = MibTableColumn
dellNetBgpM2PeerKeepAliveConfigured = _DellNetBgpM2PeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1, 3),
    _DellNetBgpM2PeerKeepAliveConfigured_Type()
)
dellNetBgpM2PeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerKeepAliveConfigured.setStatus("current")


class _DellNetBgpM2PeerMinASOrigInterval_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerMinASOrigInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DellNetBgpM2PeerMinASOrigInterval_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerMinASOrigInterval_Object = MibTableColumn
dellNetBgpM2PeerMinASOrigInterval = _DellNetBgpM2PeerMinASOrigInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1, 4),
    _DellNetBgpM2PeerMinASOrigInterval_Type()
)
dellNetBgpM2PeerMinASOrigInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerMinASOrigInterval.setStatus("current")


class _DellNetBgpM2PeerMinRouteAdverInterval_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerMinRouteAdverInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DellNetBgpM2PeerMinRouteAdverInterval_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerMinRouteAdverInterval_Object = MibTableColumn
dellNetBgpM2PeerMinRouteAdverInterval = _DellNetBgpM2PeerMinRouteAdverInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 2, 1, 5),
    _DellNetBgpM2PeerMinRouteAdverInterval_Type()
)
dellNetBgpM2PeerMinRouteAdverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerMinRouteAdverInterval.setStatus("current")
_DellNetBgpM2PeerNegotiatedTimersTable_Object = MibTable
dellNetBgpM2PeerNegotiatedTimersTable = _DellNetBgpM2PeerNegotiatedTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerNegotiatedTimersTable.setStatus("current")
_DellNetBgpM2PeerNegotiatedTimersEntry_Object = MibTableRow
dellNetBgpM2PeerNegotiatedTimersEntry = _DellNetBgpM2PeerNegotiatedTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerNegotiatedTimersEntry.setStatus("current")


class _DellNetBgpM2PeerHoldTime_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_DellNetBgpM2PeerHoldTime_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerHoldTime_Object = MibTableColumn
dellNetBgpM2PeerHoldTime = _DellNetBgpM2PeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 3, 1, 1),
    _DellNetBgpM2PeerHoldTime_Type()
)
dellNetBgpM2PeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerHoldTime.setStatus("current")


class _DellNetBgpM2PeerKeepAlive_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerKeepAlive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_DellNetBgpM2PeerKeepAlive_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerKeepAlive_Object = MibTableColumn
dellNetBgpM2PeerKeepAlive = _DellNetBgpM2PeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 3, 3, 1, 2),
    _DellNetBgpM2PeerKeepAlive_Type()
)
dellNetBgpM2PeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerKeepAlive.setStatus("current")
_DellNetBgpM2PeerCapabilities_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerCapabilities = _DellNetBgpM2PeerCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4)
)
_DellNetBgpM2PeerCapsAnnouncedTable_Object = MibTable
dellNetBgpM2PeerCapsAnnouncedTable = _DellNetBgpM2PeerCapsAnnouncedTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCapsAnnouncedTable.setStatus("current")
_DellNetBgpM2PeerCapsAnnouncedEntry_Object = MibTableRow
dellNetBgpM2PeerCapsAnnouncedEntry = _DellNetBgpM2PeerCapsAnnouncedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 1, 1)
)
dellNetBgpM2PeerCapsAnnouncedEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerCapAnnouncedCode"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerCapAnnouncedIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCapsAnnouncedEntry.setStatus("current")


class _DellNetBgpM2PeerCapAnnouncedCode_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerCapAnnouncedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DellNetBgpM2PeerCapAnnouncedCode_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerCapAnnouncedCode_Object = MibTableColumn
dellNetBgpM2PeerCapAnnouncedCode = _DellNetBgpM2PeerCapAnnouncedCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 1, 1, 1),
    _DellNetBgpM2PeerCapAnnouncedCode_Type()
)
dellNetBgpM2PeerCapAnnouncedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCapAnnouncedCode.setStatus("current")


class _DellNetBgpM2PeerCapAnnouncedIndex_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerCapAnnouncedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_DellNetBgpM2PeerCapAnnouncedIndex_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerCapAnnouncedIndex_Object = MibTableColumn
dellNetBgpM2PeerCapAnnouncedIndex = _DellNetBgpM2PeerCapAnnouncedIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 1, 1, 2),
    _DellNetBgpM2PeerCapAnnouncedIndex_Type()
)
dellNetBgpM2PeerCapAnnouncedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCapAnnouncedIndex.setStatus("current")


class _DellNetBgpM2PeerCapAnnouncedValue_Type(OctetString):
    """Custom type dellNetBgpM2PeerCapAnnouncedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DellNetBgpM2PeerCapAnnouncedValue_Type.__name__ = "OctetString"
_DellNetBgpM2PeerCapAnnouncedValue_Object = MibTableColumn
dellNetBgpM2PeerCapAnnouncedValue = _DellNetBgpM2PeerCapAnnouncedValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 1, 1, 3),
    _DellNetBgpM2PeerCapAnnouncedValue_Type()
)
dellNetBgpM2PeerCapAnnouncedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCapAnnouncedValue.setStatus("current")
_DellNetBgpM2PeerCapsReceivedTable_Object = MibTable
dellNetBgpM2PeerCapsReceivedTable = _DellNetBgpM2PeerCapsReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCapsReceivedTable.setStatus("current")
_DellNetBgpM2PeerCapsReceivedEntry_Object = MibTableRow
dellNetBgpM2PeerCapsReceivedEntry = _DellNetBgpM2PeerCapsReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 2, 1)
)
dellNetBgpM2PeerCapsReceivedEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerCapReceivedCode"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerCapReceivedIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCapsReceivedEntry.setStatus("current")


class _DellNetBgpM2PeerCapReceivedCode_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerCapReceivedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DellNetBgpM2PeerCapReceivedCode_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerCapReceivedCode_Object = MibTableColumn
dellNetBgpM2PeerCapReceivedCode = _DellNetBgpM2PeerCapReceivedCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 2, 1, 1),
    _DellNetBgpM2PeerCapReceivedCode_Type()
)
dellNetBgpM2PeerCapReceivedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCapReceivedCode.setStatus("current")


class _DellNetBgpM2PeerCapReceivedIndex_Type(Unsigned32):
    """Custom type dellNetBgpM2PeerCapReceivedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_DellNetBgpM2PeerCapReceivedIndex_Type.__name__ = "Unsigned32"
_DellNetBgpM2PeerCapReceivedIndex_Object = MibTableColumn
dellNetBgpM2PeerCapReceivedIndex = _DellNetBgpM2PeerCapReceivedIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 2, 1, 2),
    _DellNetBgpM2PeerCapReceivedIndex_Type()
)
dellNetBgpM2PeerCapReceivedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCapReceivedIndex.setStatus("current")


class _DellNetBgpM2PeerCapReceivedValue_Type(OctetString):
    """Custom type dellNetBgpM2PeerCapReceivedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DellNetBgpM2PeerCapReceivedValue_Type.__name__ = "OctetString"
_DellNetBgpM2PeerCapReceivedValue_Object = MibTableColumn
dellNetBgpM2PeerCapReceivedValue = _DellNetBgpM2PeerCapReceivedValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 4, 2, 1, 3),
    _DellNetBgpM2PeerCapReceivedValue_Type()
)
dellNetBgpM2PeerCapReceivedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCapReceivedValue.setStatus("current")
_DellNetBgpM2PeerCounters_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerCounters = _DellNetBgpM2PeerCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6)
)
_DellNetBgpM2PeerCountersTable_Object = MibTable
dellNetBgpM2PeerCountersTable = _DellNetBgpM2PeerCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCountersTable.setStatus("current")
_DellNetBgpM2PeerCountersEntry_Object = MibTableRow
dellNetBgpM2PeerCountersEntry = _DellNetBgpM2PeerCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerCountersEntry.setStatus("current")
_DellNetBgpM2PeerInUpdates_Type = Counter32
_DellNetBgpM2PeerInUpdates_Object = MibTableColumn
dellNetBgpM2PeerInUpdates = _DellNetBgpM2PeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 1),
    _DellNetBgpM2PeerInUpdates_Type()
)
dellNetBgpM2PeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerInUpdates.setStatus("current")
_DellNetBgpM2PeerOutUpdates_Type = Counter32
_DellNetBgpM2PeerOutUpdates_Object = MibTableColumn
dellNetBgpM2PeerOutUpdates = _DellNetBgpM2PeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 2),
    _DellNetBgpM2PeerOutUpdates_Type()
)
dellNetBgpM2PeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerOutUpdates.setStatus("current")
_DellNetBgpM2PeerInTotalMessages_Type = Counter32
_DellNetBgpM2PeerInTotalMessages_Object = MibTableColumn
dellNetBgpM2PeerInTotalMessages = _DellNetBgpM2PeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 3),
    _DellNetBgpM2PeerInTotalMessages_Type()
)
dellNetBgpM2PeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerInTotalMessages.setStatus("current")
_DellNetBgpM2PeerOutTotalMessages_Type = Counter32
_DellNetBgpM2PeerOutTotalMessages_Object = MibTableColumn
dellNetBgpM2PeerOutTotalMessages = _DellNetBgpM2PeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 4),
    _DellNetBgpM2PeerOutTotalMessages_Type()
)
dellNetBgpM2PeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerOutTotalMessages.setStatus("current")
_DellNetBgpM2PeerFsmEstablishedTrans_Type = Counter32
_DellNetBgpM2PeerFsmEstablishedTrans_Object = MibTableColumn
dellNetBgpM2PeerFsmEstablishedTrans = _DellNetBgpM2PeerFsmEstablishedTrans_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 5),
    _DellNetBgpM2PeerFsmEstablishedTrans_Type()
)
dellNetBgpM2PeerFsmEstablishedTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerFsmEstablishedTrans.setStatus("current")
_DellNetBgpM2PeerInKeepalives_Type = Counter32
_DellNetBgpM2PeerInKeepalives_Object = MibTableColumn
dellNetBgpM2PeerInKeepalives = _DellNetBgpM2PeerInKeepalives_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 6),
    _DellNetBgpM2PeerInKeepalives_Type()
)
dellNetBgpM2PeerInKeepalives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerInKeepalives.setStatus("current")
_DellNetBgpM2PeerOutKeepalives_Type = Counter32
_DellNetBgpM2PeerOutKeepalives_Object = MibTableColumn
dellNetBgpM2PeerOutKeepalives = _DellNetBgpM2PeerOutKeepalives_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 7),
    _DellNetBgpM2PeerOutKeepalives_Type()
)
dellNetBgpM2PeerOutKeepalives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerOutKeepalives.setStatus("current")
_DellNetBgpM2PeerInOpen_Type = Counter32
_DellNetBgpM2PeerInOpen_Object = MibTableColumn
dellNetBgpM2PeerInOpen = _DellNetBgpM2PeerInOpen_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 8),
    _DellNetBgpM2PeerInOpen_Type()
)
dellNetBgpM2PeerInOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerInOpen.setStatus("current")
_DellNetBgpM2PeerOutOpen_Type = Counter32
_DellNetBgpM2PeerOutOpen_Object = MibTableColumn
dellNetBgpM2PeerOutOpen = _DellNetBgpM2PeerOutOpen_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 9),
    _DellNetBgpM2PeerOutOpen_Type()
)
dellNetBgpM2PeerOutOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerOutOpen.setStatus("current")
_DellNetBgpM2PeerInRteRefresh_Type = Counter32
_DellNetBgpM2PeerInRteRefresh_Object = MibTableColumn
dellNetBgpM2PeerInRteRefresh = _DellNetBgpM2PeerInRteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 10),
    _DellNetBgpM2PeerInRteRefresh_Type()
)
dellNetBgpM2PeerInRteRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerInRteRefresh.setStatus("current")
_DellNetBgpM2PeerOutRteRefresh_Type = Counter32
_DellNetBgpM2PeerOutRteRefresh_Object = MibTableColumn
dellNetBgpM2PeerOutRteRefresh = _DellNetBgpM2PeerOutRteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 1, 1, 11),
    _DellNetBgpM2PeerOutRteRefresh_Type()
)
dellNetBgpM2PeerOutRteRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerOutRteRefresh.setStatus("current")
_DellNetBgpM2PrefixCountersTable_Object = MibTable
dellNetBgpM2PrefixCountersTable = _DellNetBgpM2PrefixCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PrefixCountersTable.setStatus("current")
_DellNetBgpM2PrefixCountersEntry_Object = MibTableRow
dellNetBgpM2PrefixCountersEntry = _DellNetBgpM2PrefixCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1)
)
dellNetBgpM2PrefixCountersEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PrefixCountersAfi"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PrefixCountersSafi"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2PrefixCountersEntry.setStatus("current")
_DellNetBgpM2PrefixCountersAfi_Type = DellNetBgpM2Afi
_DellNetBgpM2PrefixCountersAfi_Object = MibTableColumn
dellNetBgpM2PrefixCountersAfi = _DellNetBgpM2PrefixCountersAfi_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 1),
    _DellNetBgpM2PrefixCountersAfi_Type()
)
dellNetBgpM2PrefixCountersAfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PrefixCountersAfi.setStatus("current")
_DellNetBgpM2PrefixCountersSafi_Type = DellNetBgpM2Safi
_DellNetBgpM2PrefixCountersSafi_Object = MibTableColumn
dellNetBgpM2PrefixCountersSafi = _DellNetBgpM2PrefixCountersSafi_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 2),
    _DellNetBgpM2PrefixCountersSafi_Type()
)
dellNetBgpM2PrefixCountersSafi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PrefixCountersSafi.setStatus("current")
_DellNetBgpM2PrefixInPrefixes_Type = Gauge32
_DellNetBgpM2PrefixInPrefixes_Object = MibTableColumn
dellNetBgpM2PrefixInPrefixes = _DellNetBgpM2PrefixInPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 7),
    _DellNetBgpM2PrefixInPrefixes_Type()
)
dellNetBgpM2PrefixInPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PrefixInPrefixes.setStatus("current")
_DellNetBgpM2PrefixInPrefixesAccepted_Type = Gauge32
_DellNetBgpM2PrefixInPrefixesAccepted_Object = MibTableColumn
dellNetBgpM2PrefixInPrefixesAccepted = _DellNetBgpM2PrefixInPrefixesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 8),
    _DellNetBgpM2PrefixInPrefixesAccepted_Type()
)
dellNetBgpM2PrefixInPrefixesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PrefixInPrefixesAccepted.setStatus("current")
_DellNetBgpM2PrefixInPrefixesRejected_Type = Gauge32
_DellNetBgpM2PrefixInPrefixesRejected_Object = MibTableColumn
dellNetBgpM2PrefixInPrefixesRejected = _DellNetBgpM2PrefixInPrefixesRejected_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 9),
    _DellNetBgpM2PrefixInPrefixesRejected_Type()
)
dellNetBgpM2PrefixInPrefixesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PrefixInPrefixesRejected.setStatus("current")
_DellNetBgpM2PrefixOutPrefixes_Type = Gauge32
_DellNetBgpM2PrefixOutPrefixes_Object = MibTableColumn
dellNetBgpM2PrefixOutPrefixes = _DellNetBgpM2PrefixOutPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 10),
    _DellNetBgpM2PrefixOutPrefixes_Type()
)
dellNetBgpM2PrefixOutPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PrefixOutPrefixes.setStatus("current")
_DellNetBgpM2PrefixWdrawnByPeer_Type = Gauge32
_DellNetBgpM2PrefixWdrawnByPeer_Object = MibTableColumn
dellNetBgpM2PrefixWdrawnByPeer = _DellNetBgpM2PrefixWdrawnByPeer_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 11),
    _DellNetBgpM2PrefixWdrawnByPeer_Type()
)
dellNetBgpM2PrefixWdrawnByPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PrefixWdrawnByPeer.setStatus("current")
_DellNetBgpM2PrefixWdrawnFromPeer_Type = Gauge32
_DellNetBgpM2PrefixWdrawnFromPeer_Object = MibTableColumn
dellNetBgpM2PrefixWdrawnFromPeer = _DellNetBgpM2PrefixWdrawnFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 6, 2, 1, 12),
    _DellNetBgpM2PrefixWdrawnFromPeer_Type()
)
dellNetBgpM2PrefixWdrawnFromPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PrefixWdrawnFromPeer.setStatus("current")
_DellNetBgpM2PeerExtensions_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerExtensions = _DellNetBgpM2PeerExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7)
)
_DellNetBgpM2PeerNonCapExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerNonCapExts = _DellNetBgpM2PeerNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1)
)
_DellNetBgpM2PeerRouteReflectionExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerRouteReflectionExts = _DellNetBgpM2PeerRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 2796)
)
_DellNetBgpM2PeerReflectorClientTable_Object = MibTable
dellNetBgpM2PeerReflectorClientTable = _DellNetBgpM2PeerReflectorClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 2796, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerReflectorClientTable.setStatus("current")
_DellNetBgpM2PeerReflectorClientEntry_Object = MibTableRow
dellNetBgpM2PeerReflectorClientEntry = _DellNetBgpM2PeerReflectorClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 2796, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerReflectorClientEntry.setStatus("current")


class _DellNetBgpM2PeerReflectorClient_Type(Integer32):
    """Custom type dellNetBgpM2PeerReflectorClient based on Integer32"""
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


_DellNetBgpM2PeerReflectorClient_Type.__name__ = "Integer32"
_DellNetBgpM2PeerReflectorClient_Object = MibTableColumn
dellNetBgpM2PeerReflectorClient = _DellNetBgpM2PeerReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 2796, 1, 1, 1),
    _DellNetBgpM2PeerReflectorClient_Type()
)
dellNetBgpM2PeerReflectorClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerReflectorClient.setStatus("current")
_DellNetBgpM2PeerASConfederationExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerASConfederationExts = _DellNetBgpM2PeerASConfederationExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 3065)
)
_DellNetBgpM2PeerConfedMemberTable_Object = MibTable
dellNetBgpM2PeerConfedMemberTable = _DellNetBgpM2PeerConfedMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 3065, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerConfedMemberTable.setStatus("current")
_DellNetBgpM2PeerConfedMemberEntry_Object = MibTableRow
dellNetBgpM2PeerConfedMemberEntry = _DellNetBgpM2PeerConfedMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 3065, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerConfedMemberEntry.setStatus("current")
_DellNetBgpM2PeerConfedMember_Type = TruthValue
_DellNetBgpM2PeerConfedMember_Object = MibTableColumn
dellNetBgpM2PeerConfedMember = _DellNetBgpM2PeerConfedMember_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 1, 3065, 1, 1, 1),
    _DellNetBgpM2PeerConfedMember_Type()
)
dellNetBgpM2PeerConfedMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PeerConfedMember.setStatus("current")
_DellNetBgpM2PeerCapExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerCapExts = _DellNetBgpM2PeerCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 7, 2)
)
_DellNetBgpM2PeerConfiguration_ObjectIdentity = ObjectIdentity
dellNetBgpM2PeerConfiguration = _DellNetBgpM2PeerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8)
)
_DellNetBgpM2CfgPeerAdminStatusTable_Object = MibTable
dellNetBgpM2CfgPeerAdminStatusTable = _DellNetBgpM2CfgPeerAdminStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerAdminStatusTable.setStatus("current")
_DellNetBgpM2CfgPeerAdminStatusEntry_Object = MibTableRow
dellNetBgpM2CfgPeerAdminStatusEntry = _DellNetBgpM2CfgPeerAdminStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 1, 1)
)
dellNetBgpM2CfgPeerAdminStatusEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerAdminStatusEntry.setStatus("current")


class _DellNetBgpM2CfgPeerAdminStatus_Type(Integer32):
    """Custom type dellNetBgpM2CfgPeerAdminStatus based on Integer32"""
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


_DellNetBgpM2CfgPeerAdminStatus_Type.__name__ = "Integer32"
_DellNetBgpM2CfgPeerAdminStatus_Object = MibTableColumn
dellNetBgpM2CfgPeerAdminStatus = _DellNetBgpM2CfgPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 1, 1, 1),
    _DellNetBgpM2CfgPeerAdminStatus_Type()
)
dellNetBgpM2CfgPeerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerAdminStatus.setStatus("current")


class _DellNetBgpM2CfgPeerNextIndex_Type(Integer32):
    """Custom type dellNetBgpM2CfgPeerNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DellNetBgpM2CfgPeerNextIndex_Type.__name__ = "Integer32"
_DellNetBgpM2CfgPeerNextIndex_Object = MibScalar
dellNetBgpM2CfgPeerNextIndex = _DellNetBgpM2CfgPeerNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 2),
    _DellNetBgpM2CfgPeerNextIndex_Type()
)
dellNetBgpM2CfgPeerNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerNextIndex.setStatus("current")
_DellNetBgpM2CfgPeerTable_Object = MibTable
dellNetBgpM2CfgPeerTable = _DellNetBgpM2CfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerTable.setStatus("current")
_DellNetBgpM2CfgPeerEntry_Object = MibTableRow
dellNetBgpM2CfgPeerEntry = _DellNetBgpM2CfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1)
)
dellNetBgpM2CfgPeerEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerEntry.setStatus("current")


class _DellNetBgpM2CfgPeerConfiguredVersion_Type(Unsigned32):
    """Custom type dellNetBgpM2CfgPeerConfiguredVersion based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DellNetBgpM2CfgPeerConfiguredVersion_Type.__name__ = "Unsigned32"
_DellNetBgpM2CfgPeerConfiguredVersion_Object = MibTableColumn
dellNetBgpM2CfgPeerConfiguredVersion = _DellNetBgpM2CfgPeerConfiguredVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 1),
    _DellNetBgpM2CfgPeerConfiguredVersion_Type()
)
dellNetBgpM2CfgPeerConfiguredVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerConfiguredVersion.setStatus("current")


class _DellNetBgpM2CfgAllowVersionNegotiation_Type(TruthValue):
    """Custom type dellNetBgpM2CfgAllowVersionNegotiation based on TruthValue"""


_DellNetBgpM2CfgAllowVersionNegotiation_Object = MibTableColumn
dellNetBgpM2CfgAllowVersionNegotiation = _DellNetBgpM2CfgAllowVersionNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 2),
    _DellNetBgpM2CfgAllowVersionNegotiation_Type()
)
dellNetBgpM2CfgAllowVersionNegotiation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgAllowVersionNegotiation.setStatus("current")
_DellNetBgpM2CfgPeerLocalAddrType_Type = InetAddressType
_DellNetBgpM2CfgPeerLocalAddrType_Object = MibTableColumn
dellNetBgpM2CfgPeerLocalAddrType = _DellNetBgpM2CfgPeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 3),
    _DellNetBgpM2CfgPeerLocalAddrType_Type()
)
dellNetBgpM2CfgPeerLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerLocalAddrType.setStatus("current")


class _DellNetBgpM2CfgPeerLocalAddr_Type(InetAddress):
    """Custom type dellNetBgpM2CfgPeerLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_DellNetBgpM2CfgPeerLocalAddr_Type.__name__ = "InetAddress"
_DellNetBgpM2CfgPeerLocalAddr_Object = MibTableColumn
dellNetBgpM2CfgPeerLocalAddr = _DellNetBgpM2CfgPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 4),
    _DellNetBgpM2CfgPeerLocalAddr_Type()
)
dellNetBgpM2CfgPeerLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerLocalAddr.setStatus("current")


class _DellNetBgpM2CfgPeerLocalAs_Type(InetAutonomousSystemNumber):
    """Custom type dellNetBgpM2CfgPeerLocalAs based on InetAutonomousSystemNumber"""
    defaultValue = 0


_DellNetBgpM2CfgPeerLocalAs_Object = MibTableColumn
dellNetBgpM2CfgPeerLocalAs = _DellNetBgpM2CfgPeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 5),
    _DellNetBgpM2CfgPeerLocalAs_Type()
)
dellNetBgpM2CfgPeerLocalAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerLocalAs.setStatus("current")
_DellNetBgpM2CfgPeerRemoteAddrType_Type = InetAddressType
_DellNetBgpM2CfgPeerRemoteAddrType_Object = MibTableColumn
dellNetBgpM2CfgPeerRemoteAddrType = _DellNetBgpM2CfgPeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 6),
    _DellNetBgpM2CfgPeerRemoteAddrType_Type()
)
dellNetBgpM2CfgPeerRemoteAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerRemoteAddrType.setStatus("current")


class _DellNetBgpM2CfgPeerRemoteAddr_Type(InetAddress):
    """Custom type dellNetBgpM2CfgPeerRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_DellNetBgpM2CfgPeerRemoteAddr_Type.__name__ = "InetAddress"
_DellNetBgpM2CfgPeerRemoteAddr_Object = MibTableColumn
dellNetBgpM2CfgPeerRemoteAddr = _DellNetBgpM2CfgPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 7),
    _DellNetBgpM2CfgPeerRemoteAddr_Type()
)
dellNetBgpM2CfgPeerRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerRemoteAddr.setStatus("current")
_DellNetBgpM2CfgPeerRemoteAs_Type = InetAutonomousSystemNumber
_DellNetBgpM2CfgPeerRemoteAs_Object = MibTableColumn
dellNetBgpM2CfgPeerRemoteAs = _DellNetBgpM2CfgPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 8),
    _DellNetBgpM2CfgPeerRemoteAs_Type()
)
dellNetBgpM2CfgPeerRemoteAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerRemoteAs.setStatus("current")
_DellNetBgpM2CfgPeerEntryStorageType_Type = StorageType
_DellNetBgpM2CfgPeerEntryStorageType_Object = MibTableColumn
dellNetBgpM2CfgPeerEntryStorageType = _DellNetBgpM2CfgPeerEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 9),
    _DellNetBgpM2CfgPeerEntryStorageType_Type()
)
dellNetBgpM2CfgPeerEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerEntryStorageType.setStatus("current")


class _DellNetBgpM2CfgPeerError_Type(Integer32):
    """Custom type dellNetBgpM2CfgPeerError based on Integer32"""
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


_DellNetBgpM2CfgPeerError_Type.__name__ = "Integer32"
_DellNetBgpM2CfgPeerError_Object = MibTableColumn
dellNetBgpM2CfgPeerError = _DellNetBgpM2CfgPeerError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 10),
    _DellNetBgpM2CfgPeerError_Type()
)
dellNetBgpM2CfgPeerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerError.setStatus("current")
_DellNetBgpM2CfgPeerBgpPeerEntry_Type = RowPointer
_DellNetBgpM2CfgPeerBgpPeerEntry_Object = MibTableColumn
dellNetBgpM2CfgPeerBgpPeerEntry = _DellNetBgpM2CfgPeerBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 11),
    _DellNetBgpM2CfgPeerBgpPeerEntry_Type()
)
dellNetBgpM2CfgPeerBgpPeerEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerBgpPeerEntry.setStatus("current")
_DellNetBgpM2CfgPeerRowEntryStatus_Type = RowStatus
_DellNetBgpM2CfgPeerRowEntryStatus_Object = MibTableColumn
dellNetBgpM2CfgPeerRowEntryStatus = _DellNetBgpM2CfgPeerRowEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 12),
    _DellNetBgpM2CfgPeerRowEntryStatus_Type()
)
dellNetBgpM2CfgPeerRowEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerRowEntryStatus.setStatus("current")


class _DellNetBgpM2CfgPeerIndex_Type(Integer32):
    """Custom type dellNetBgpM2CfgPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DellNetBgpM2CfgPeerIndex_Type.__name__ = "Integer32"
_DellNetBgpM2CfgPeerIndex_Object = MibTableColumn
dellNetBgpM2CfgPeerIndex = _DellNetBgpM2CfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 13),
    _DellNetBgpM2CfgPeerIndex_Type()
)
dellNetBgpM2CfgPeerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerIndex.setStatus("current")


class _DellNetBgpM2CfgPeerStatus_Type(Integer32):
    """Custom type dellNetBgpM2CfgPeerStatus based on Integer32"""
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


_DellNetBgpM2CfgPeerStatus_Type.__name__ = "Integer32"
_DellNetBgpM2CfgPeerStatus_Object = MibTableColumn
dellNetBgpM2CfgPeerStatus = _DellNetBgpM2CfgPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 3, 1, 14),
    _DellNetBgpM2CfgPeerStatus_Type()
)
dellNetBgpM2CfgPeerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerStatus.setStatus("current")
_DellNetBgpM2CfgPeerTimersTable_Object = MibTable
dellNetBgpM2CfgPeerTimersTable = _DellNetBgpM2CfgPeerTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerTimersTable.setStatus("current")
_DellNetBgpM2CfgPeerTimersEntry_Object = MibTableRow
dellNetBgpM2CfgPeerTimersEntry = _DellNetBgpM2CfgPeerTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerTimersEntry.setStatus("current")


class _DellNetBgpM2CfgPeerConnectRetryInterval_Type(Unsigned32):
    """Custom type dellNetBgpM2CfgPeerConnectRetryInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DellNetBgpM2CfgPeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_DellNetBgpM2CfgPeerConnectRetryInterval_Object = MibTableColumn
dellNetBgpM2CfgPeerConnectRetryInterval = _DellNetBgpM2CfgPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1, 1),
    _DellNetBgpM2CfgPeerConnectRetryInterval_Type()
)
dellNetBgpM2CfgPeerConnectRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerConnectRetryInterval.setStatus("current")


class _DellNetBgpM2CfgPeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type dellNetBgpM2CfgPeerHoldTimeConfigured based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_DellNetBgpM2CfgPeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_DellNetBgpM2CfgPeerHoldTimeConfigured_Object = MibTableColumn
dellNetBgpM2CfgPeerHoldTimeConfigured = _DellNetBgpM2CfgPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1, 2),
    _DellNetBgpM2CfgPeerHoldTimeConfigured_Type()
)
dellNetBgpM2CfgPeerHoldTimeConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerHoldTimeConfigured.setStatus("current")


class _DellNetBgpM2CfgPeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type dellNetBgpM2CfgPeerKeepAliveConfigured based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_DellNetBgpM2CfgPeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_DellNetBgpM2CfgPeerKeepAliveConfigured_Object = MibTableColumn
dellNetBgpM2CfgPeerKeepAliveConfigured = _DellNetBgpM2CfgPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1, 3),
    _DellNetBgpM2CfgPeerKeepAliveConfigured_Type()
)
dellNetBgpM2CfgPeerKeepAliveConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerKeepAliveConfigured.setStatus("current")


class _DellNetBgpM2CfgPeerMinASOrigInterval_Type(Unsigned32):
    """Custom type dellNetBgpM2CfgPeerMinASOrigInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DellNetBgpM2CfgPeerMinASOrigInterval_Type.__name__ = "Unsigned32"
_DellNetBgpM2CfgPeerMinASOrigInterval_Object = MibTableColumn
dellNetBgpM2CfgPeerMinASOrigInterval = _DellNetBgpM2CfgPeerMinASOrigInterval_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1, 4),
    _DellNetBgpM2CfgPeerMinASOrigInterval_Type()
)
dellNetBgpM2CfgPeerMinASOrigInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerMinASOrigInterval.setStatus("current")


class _DellNetBgpM2CfgPeerMinRouteAdverInter_Type(Unsigned32):
    """Custom type dellNetBgpM2CfgPeerMinRouteAdverInter based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DellNetBgpM2CfgPeerMinRouteAdverInter_Type.__name__ = "Unsigned32"
_DellNetBgpM2CfgPeerMinRouteAdverInter_Object = MibTableColumn
dellNetBgpM2CfgPeerMinRouteAdverInter = _DellNetBgpM2CfgPeerMinRouteAdverInter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 4, 1, 5),
    _DellNetBgpM2CfgPeerMinRouteAdverInter_Type()
)
dellNetBgpM2CfgPeerMinRouteAdverInter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerMinRouteAdverInter.setStatus("current")
_DellNetBgpM2CfgPeerExtensions_ObjectIdentity = ObjectIdentity
dellNetBgpM2CfgPeerExtensions = _DellNetBgpM2CfgPeerExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5)
)
_DellNetBgpM2CfgPeerNonCapExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2CfgPeerNonCapExts = _DellNetBgpM2CfgPeerNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1)
)
_DellNetBgpM2CfgPeerRouteReflectionExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2CfgPeerRouteReflectionExts = _DellNetBgpM2CfgPeerRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 2796)
)
_DellNetBgpM2CfgPeerReflectorClientTable_Object = MibTable
dellNetBgpM2CfgPeerReflectorClientTable = _DellNetBgpM2CfgPeerReflectorClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 2796, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerReflectorClientTable.setStatus("current")
_DellNetBgpM2CfgPeerReflectorClientEntry_Object = MibTableRow
dellNetBgpM2CfgPeerReflectorClientEntry = _DellNetBgpM2CfgPeerReflectorClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 2796, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerReflectorClientEntry.setStatus("current")


class _DellNetBgpM2CfgPeerReflectorClient_Type(Integer32):
    """Custom type dellNetBgpM2CfgPeerReflectorClient based on Integer32"""
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


_DellNetBgpM2CfgPeerReflectorClient_Type.__name__ = "Integer32"
_DellNetBgpM2CfgPeerReflectorClient_Object = MibTableColumn
dellNetBgpM2CfgPeerReflectorClient = _DellNetBgpM2CfgPeerReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 2796, 1, 1, 1),
    _DellNetBgpM2CfgPeerReflectorClient_Type()
)
dellNetBgpM2CfgPeerReflectorClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerReflectorClient.setStatus("current")
_DellNetBgpM2CfgPeerASConfederationExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2CfgPeerASConfederationExts = _DellNetBgpM2CfgPeerASConfederationExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 3065)
)
_DellNetBgpM2CfgPeerConfedMemberTable_Object = MibTable
dellNetBgpM2CfgPeerConfedMemberTable = _DellNetBgpM2CfgPeerConfedMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 3065, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerConfedMemberTable.setStatus("current")
_DellNetBgpM2CfgPeerConfedMemberEntry_Object = MibTableRow
dellNetBgpM2CfgPeerConfedMemberEntry = _DellNetBgpM2CfgPeerConfedMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 3065, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerConfedMemberEntry.setStatus("current")
_DellNetBgpM2CfgPeerConfedMember_Type = TruthValue
_DellNetBgpM2CfgPeerConfedMember_Object = MibTableColumn
dellNetBgpM2CfgPeerConfedMember = _DellNetBgpM2CfgPeerConfedMember_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 1, 3065, 1, 1, 1),
    _DellNetBgpM2CfgPeerConfedMember_Type()
)
dellNetBgpM2CfgPeerConfedMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dellNetBgpM2CfgPeerConfedMember.setStatus("current")
_DellNetBgpM2CfgPeerCapExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2CfgPeerCapExts = _DellNetBgpM2CfgPeerCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 2, 8, 5, 2)
)
_DellNetBgpM2Rib_ObjectIdentity = ObjectIdentity
dellNetBgpM2Rib = _DellNetBgpM2Rib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3)
)
_DellNetBgpM2NlriTable_Object = MibTable
dellNetBgpM2NlriTable = _DellNetBgpM2NlriTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2NlriTable.setStatus("current")
_DellNetBgpM2NlriEntry_Object = MibTableRow
dellNetBgpM2NlriEntry = _DellNetBgpM2NlriEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1)
)
dellNetBgpM2NlriEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriAfi"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriSafi"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriPrefix"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriPrefixLen"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2NlriEntry.setStatus("current")
_DellNetBgpM2NlriIndex_Type = Unsigned32
_DellNetBgpM2NlriIndex_Object = MibTableColumn
dellNetBgpM2NlriIndex = _DellNetBgpM2NlriIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 1),
    _DellNetBgpM2NlriIndex_Type()
)
dellNetBgpM2NlriIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2NlriIndex.setStatus("current")
_DellNetBgpM2NlriAfi_Type = DellNetBgpM2Afi
_DellNetBgpM2NlriAfi_Object = MibTableColumn
dellNetBgpM2NlriAfi = _DellNetBgpM2NlriAfi_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 2),
    _DellNetBgpM2NlriAfi_Type()
)
dellNetBgpM2NlriAfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2NlriAfi.setStatus("current")
_DellNetBgpM2NlriSafi_Type = DellNetBgpM2Safi
_DellNetBgpM2NlriSafi_Object = MibTableColumn
dellNetBgpM2NlriSafi = _DellNetBgpM2NlriSafi_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 3),
    _DellNetBgpM2NlriSafi_Type()
)
dellNetBgpM2NlriSafi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2NlriSafi.setStatus("current")
_DellNetBgpM2NlriPrefixType_Type = InetAddressType
_DellNetBgpM2NlriPrefixType_Object = MibTableColumn
dellNetBgpM2NlriPrefixType = _DellNetBgpM2NlriPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 4),
    _DellNetBgpM2NlriPrefixType_Type()
)
dellNetBgpM2NlriPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2NlriPrefixType.setStatus("current")


class _DellNetBgpM2NlriPrefix_Type(InetAddress):
    """Custom type dellNetBgpM2NlriPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_DellNetBgpM2NlriPrefix_Type.__name__ = "InetAddress"
_DellNetBgpM2NlriPrefix_Object = MibTableColumn
dellNetBgpM2NlriPrefix = _DellNetBgpM2NlriPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 5),
    _DellNetBgpM2NlriPrefix_Type()
)
dellNetBgpM2NlriPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2NlriPrefix.setStatus("current")
_DellNetBgpM2NlriPrefixLen_Type = InetAddressPrefixLength
_DellNetBgpM2NlriPrefixLen_Object = MibTableColumn
dellNetBgpM2NlriPrefixLen = _DellNetBgpM2NlriPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 6),
    _DellNetBgpM2NlriPrefixLen_Type()
)
dellNetBgpM2NlriPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2NlriPrefixLen.setStatus("current")
_DellNetBgpM2NlriBest_Type = TruthValue
_DellNetBgpM2NlriBest_Object = MibTableColumn
dellNetBgpM2NlriBest = _DellNetBgpM2NlriBest_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 7),
    _DellNetBgpM2NlriBest_Type()
)
dellNetBgpM2NlriBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2NlriBest.setStatus("current")
_DellNetBgpM2NlriCalcLocalPref_Type = Unsigned32
_DellNetBgpM2NlriCalcLocalPref_Object = MibTableColumn
dellNetBgpM2NlriCalcLocalPref = _DellNetBgpM2NlriCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 8),
    _DellNetBgpM2NlriCalcLocalPref_Type()
)
dellNetBgpM2NlriCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2NlriCalcLocalPref.setStatus("current")
_DellNetBgpM2PathAttrIndex_Type = Unsigned32
_DellNetBgpM2PathAttrIndex_Object = MibTableColumn
dellNetBgpM2PathAttrIndex = _DellNetBgpM2PathAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 9),
    _DellNetBgpM2PathAttrIndex_Type()
)
dellNetBgpM2PathAttrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrIndex.setStatus("current")


class _DellNetBgpM2NlriOpaqueType_Type(Integer32):
    """Custom type dellNetBgpM2NlriOpaqueType based on Integer32"""
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


_DellNetBgpM2NlriOpaqueType_Type.__name__ = "Integer32"
_DellNetBgpM2NlriOpaqueType_Object = MibTableColumn
dellNetBgpM2NlriOpaqueType = _DellNetBgpM2NlriOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 10),
    _DellNetBgpM2NlriOpaqueType_Type()
)
dellNetBgpM2NlriOpaqueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2NlriOpaqueType.setStatus("current")
_DellNetBgpM2NlriOpaquePointer_Type = RowPointer
_DellNetBgpM2NlriOpaquePointer_Object = MibTableColumn
dellNetBgpM2NlriOpaquePointer = _DellNetBgpM2NlriOpaquePointer_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 1, 1, 11),
    _DellNetBgpM2NlriOpaquePointer_Type()
)
dellNetBgpM2NlriOpaquePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2NlriOpaquePointer.setStatus("current")
_DellNetBgpM2AdjRibsOutTable_Object = MibTable
dellNetBgpM2AdjRibsOutTable = _DellNetBgpM2AdjRibsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dellNetBgpM2AdjRibsOutTable.setStatus("current")
_DellNetBgpM2AdjRibsOutEntry_Object = MibTableRow
dellNetBgpM2AdjRibsOutEntry = _DellNetBgpM2AdjRibsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 2, 1)
)
dellNetBgpM2AdjRibsOutEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriAfi"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriSafi"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriPrefix"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriPrefixLen"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AdjRibsOutIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2AdjRibsOutEntry.setStatus("current")
_DellNetBgpM2AdjRibsOutIndex_Type = Unsigned32
_DellNetBgpM2AdjRibsOutIndex_Object = MibTableColumn
dellNetBgpM2AdjRibsOutIndex = _DellNetBgpM2AdjRibsOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 2, 1, 1),
    _DellNetBgpM2AdjRibsOutIndex_Type()
)
dellNetBgpM2AdjRibsOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AdjRibsOutIndex.setStatus("current")
_DellNetBgpM2AdjRibsOutRoute_Type = RowPointer
_DellNetBgpM2AdjRibsOutRoute_Object = MibTableColumn
dellNetBgpM2AdjRibsOutRoute = _DellNetBgpM2AdjRibsOutRoute_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 2, 1, 2),
    _DellNetBgpM2AdjRibsOutRoute_Type()
)
dellNetBgpM2AdjRibsOutRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AdjRibsOutRoute.setStatus("current")
_DellNetBgpM2PathAttrCount_Type = Counter32
_DellNetBgpM2PathAttrCount_Object = MibScalar
dellNetBgpM2PathAttrCount = _DellNetBgpM2PathAttrCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 3),
    _DellNetBgpM2PathAttrCount_Type()
)
dellNetBgpM2PathAttrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrCount.setStatus("current")
_DellNetBgpM2PathAttrTable_Object = MibTable
dellNetBgpM2PathAttrTable = _DellNetBgpM2PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrTable.setStatus("current")
_DellNetBgpM2PathAttrEntry_Object = MibTableRow
dellNetBgpM2PathAttrEntry = _DellNetBgpM2PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1)
)
dellNetBgpM2PathAttrEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrEntry.setStatus("current")


class _DellNetBgpM2PathAttrOrigin_Type(Integer32):
    """Custom type dellNetBgpM2PathAttrOrigin based on Integer32"""
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


_DellNetBgpM2PathAttrOrigin_Type.__name__ = "Integer32"
_DellNetBgpM2PathAttrOrigin_Object = MibTableColumn
dellNetBgpM2PathAttrOrigin = _DellNetBgpM2PathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 1),
    _DellNetBgpM2PathAttrOrigin_Type()
)
dellNetBgpM2PathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrOrigin.setStatus("current")
_DellNetBgpM2PathAttrNextHopAddrType_Type = InetAddressType
_DellNetBgpM2PathAttrNextHopAddrType_Object = MibTableColumn
dellNetBgpM2PathAttrNextHopAddrType = _DellNetBgpM2PathAttrNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 2),
    _DellNetBgpM2PathAttrNextHopAddrType_Type()
)
dellNetBgpM2PathAttrNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrNextHopAddrType.setStatus("current")


class _DellNetBgpM2PathAttrNextHop_Type(InetAddress):
    """Custom type dellNetBgpM2PathAttrNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_DellNetBgpM2PathAttrNextHop_Type.__name__ = "InetAddress"
_DellNetBgpM2PathAttrNextHop_Object = MibTableColumn
dellNetBgpM2PathAttrNextHop = _DellNetBgpM2PathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 3),
    _DellNetBgpM2PathAttrNextHop_Type()
)
dellNetBgpM2PathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrNextHop.setStatus("current")
_DellNetBgpM2PathAttrMedPresent_Type = TruthValue
_DellNetBgpM2PathAttrMedPresent_Object = MibTableColumn
dellNetBgpM2PathAttrMedPresent = _DellNetBgpM2PathAttrMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 4),
    _DellNetBgpM2PathAttrMedPresent_Type()
)
dellNetBgpM2PathAttrMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrMedPresent.setStatus("current")
_DellNetBgpM2PathAttrMed_Type = Unsigned32
_DellNetBgpM2PathAttrMed_Object = MibTableColumn
dellNetBgpM2PathAttrMed = _DellNetBgpM2PathAttrMed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 5),
    _DellNetBgpM2PathAttrMed_Type()
)
dellNetBgpM2PathAttrMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrMed.setStatus("current")
_DellNetBgpM2PathAttrLocalPrefPresent_Type = TruthValue
_DellNetBgpM2PathAttrLocalPrefPresent_Object = MibTableColumn
dellNetBgpM2PathAttrLocalPrefPresent = _DellNetBgpM2PathAttrLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 6),
    _DellNetBgpM2PathAttrLocalPrefPresent_Type()
)
dellNetBgpM2PathAttrLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrLocalPrefPresent.setStatus("current")
_DellNetBgpM2PathAttrLocalPref_Type = Unsigned32
_DellNetBgpM2PathAttrLocalPref_Object = MibTableColumn
dellNetBgpM2PathAttrLocalPref = _DellNetBgpM2PathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 7),
    _DellNetBgpM2PathAttrLocalPref_Type()
)
dellNetBgpM2PathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrLocalPref.setStatus("current")


class _DellNetBgpM2PathAttrAtomicAggregate_Type(Integer32):
    """Custom type dellNetBgpM2PathAttrAtomicAggregate based on Integer32"""
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


_DellNetBgpM2PathAttrAtomicAggregate_Type.__name__ = "Integer32"
_DellNetBgpM2PathAttrAtomicAggregate_Object = MibTableColumn
dellNetBgpM2PathAttrAtomicAggregate = _DellNetBgpM2PathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 8),
    _DellNetBgpM2PathAttrAtomicAggregate_Type()
)
dellNetBgpM2PathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrAtomicAggregate.setStatus("current")
_DellNetBgpM2PathAttrAggregatorAS_Type = InetAutonomousSystemNumber
_DellNetBgpM2PathAttrAggregatorAS_Object = MibTableColumn
dellNetBgpM2PathAttrAggregatorAS = _DellNetBgpM2PathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 9),
    _DellNetBgpM2PathAttrAggregatorAS_Type()
)
dellNetBgpM2PathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrAggregatorAS.setStatus("current")
_DellNetBgpM2PathAttrAggregatorAddr_Type = DellNetBgpM2Identifier
_DellNetBgpM2PathAttrAggregatorAddr_Object = MibTableColumn
dellNetBgpM2PathAttrAggregatorAddr = _DellNetBgpM2PathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 10),
    _DellNetBgpM2PathAttrAggregatorAddr_Type()
)
dellNetBgpM2PathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrAggregatorAddr.setStatus("current")
_DellNetBgpM2AsPathCalcLength_Type = Unsigned32
_DellNetBgpM2AsPathCalcLength_Object = MibTableColumn
dellNetBgpM2AsPathCalcLength = _DellNetBgpM2AsPathCalcLength_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 11),
    _DellNetBgpM2AsPathCalcLength_Type()
)
dellNetBgpM2AsPathCalcLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPathCalcLength.setStatus("current")
_DellNetBgpM2AsPathString_Type = SnmpAdminString
_DellNetBgpM2AsPathString_Object = MibTableColumn
dellNetBgpM2AsPathString = _DellNetBgpM2AsPathString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 12),
    _DellNetBgpM2AsPathString_Type()
)
dellNetBgpM2AsPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPathString.setStatus("current")
_DellNetBgpM2AsPathIndex_Type = Unsigned32
_DellNetBgpM2AsPathIndex_Object = MibTableColumn
dellNetBgpM2AsPathIndex = _DellNetBgpM2AsPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 4, 1, 13),
    _DellNetBgpM2AsPathIndex_Type()
)
dellNetBgpM2AsPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPathIndex.setStatus("current")
_DellNetBgpM2AsPath4byteTable_Object = MibTable
dellNetBgpM2AsPath4byteTable = _DellNetBgpM2AsPath4byteTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5)
)
if mibBuilder.loadTexts:
    dellNetBgpM2AsPath4byteTable.setStatus("current")
_DellNetBgpM2AsPath4byteEntry_Object = MibTableRow
dellNetBgpM2AsPath4byteEntry = _DellNetBgpM2AsPath4byteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2AsPath4byteEntry.setStatus("current")
_DellNetBgpM2AsPath4bytePathPresent_Type = TruthValue
_DellNetBgpM2AsPath4bytePathPresent_Object = MibTableColumn
dellNetBgpM2AsPath4bytePathPresent = _DellNetBgpM2AsPath4bytePathPresent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1, 1),
    _DellNetBgpM2AsPath4bytePathPresent_Type()
)
dellNetBgpM2AsPath4bytePathPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPath4bytePathPresent.setStatus("current")
_DellNetBgpM2AsPath4byteAggregatorAS_Type = InetAutonomousSystemNumber
_DellNetBgpM2AsPath4byteAggregatorAS_Object = MibTableColumn
dellNetBgpM2AsPath4byteAggregatorAS = _DellNetBgpM2AsPath4byteAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1, 2),
    _DellNetBgpM2AsPath4byteAggregatorAS_Type()
)
dellNetBgpM2AsPath4byteAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPath4byteAggregatorAS.setStatus("current")
_DellNetBgpM2AsPath4byteCalcLength_Type = Unsigned32
_DellNetBgpM2AsPath4byteCalcLength_Object = MibTableColumn
dellNetBgpM2AsPath4byteCalcLength = _DellNetBgpM2AsPath4byteCalcLength_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1, 3),
    _DellNetBgpM2AsPath4byteCalcLength_Type()
)
dellNetBgpM2AsPath4byteCalcLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPath4byteCalcLength.setStatus("current")
_DellNetBgpM2AsPath4byteString_Type = SnmpAdminString
_DellNetBgpM2AsPath4byteString_Object = MibTableColumn
dellNetBgpM2AsPath4byteString = _DellNetBgpM2AsPath4byteString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1, 4),
    _DellNetBgpM2AsPath4byteString_Type()
)
dellNetBgpM2AsPath4byteString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPath4byteString.setStatus("current")
_DellNetBgpM2AsPath4byteIndex_Type = Unsigned32
_DellNetBgpM2AsPath4byteIndex_Object = MibTableColumn
dellNetBgpM2AsPath4byteIndex = _DellNetBgpM2AsPath4byteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 5, 1, 5),
    _DellNetBgpM2AsPath4byteIndex_Type()
)
dellNetBgpM2AsPath4byteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPath4byteIndex.setStatus("current")
_DellNetBgpM2AsPathTable_Object = MibTable
dellNetBgpM2AsPathTable = _DellNetBgpM2AsPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6)
)
if mibBuilder.loadTexts:
    dellNetBgpM2AsPathTable.setStatus("current")
_DellNetBgpM2AsPathTableEntry_Object = MibTableRow
dellNetBgpM2AsPathTableEntry = _DellNetBgpM2AsPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6, 1)
)
dellNetBgpM2AsPathTableEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathSegmentIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathElementIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2AsPathTableEntry.setStatus("current")
_DellNetBgpM2AsPathSegmentIndex_Type = Unsigned32
_DellNetBgpM2AsPathSegmentIndex_Object = MibTableColumn
dellNetBgpM2AsPathSegmentIndex = _DellNetBgpM2AsPathSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6, 1, 1),
    _DellNetBgpM2AsPathSegmentIndex_Type()
)
dellNetBgpM2AsPathSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPathSegmentIndex.setStatus("current")
_DellNetBgpM2AsPathElementIndex_Type = Unsigned32
_DellNetBgpM2AsPathElementIndex_Object = MibTableColumn
dellNetBgpM2AsPathElementIndex = _DellNetBgpM2AsPathElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6, 1, 2),
    _DellNetBgpM2AsPathElementIndex_Type()
)
dellNetBgpM2AsPathElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPathElementIndex.setStatus("current")


class _DellNetBgpM2AsPathType_Type(Integer32):
    """Custom type dellNetBgpM2AsPathType based on Integer32"""
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


_DellNetBgpM2AsPathType_Type.__name__ = "Integer32"
_DellNetBgpM2AsPathType_Object = MibTableColumn
dellNetBgpM2AsPathType = _DellNetBgpM2AsPathType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6, 1, 3),
    _DellNetBgpM2AsPathType_Type()
)
dellNetBgpM2AsPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPathType.setStatus("current")
_DellNetBgpM2AsPathElementValue_Type = InetAutonomousSystemNumber
_DellNetBgpM2AsPathElementValue_Object = MibTableColumn
dellNetBgpM2AsPathElementValue = _DellNetBgpM2AsPathElementValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 6, 1, 4),
    _DellNetBgpM2AsPathElementValue_Type()
)
dellNetBgpM2AsPathElementValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2AsPathElementValue.setStatus("current")
_DellNetBgpM2PathAttrUnknownTable_Object = MibTable
dellNetBgpM2PathAttrUnknownTable = _DellNetBgpM2PathAttrUnknownTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 7)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrUnknownTable.setStatus("current")
_DellNetBgpM2PathAttrUnknownEntry_Object = MibTableRow
dellNetBgpM2PathAttrUnknownEntry = _DellNetBgpM2PathAttrUnknownEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 7, 1)
)
dellNetBgpM2PathAttrUnknownEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrUnknownIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrUnknownEntry.setStatus("current")
_DellNetBgpM2PathAttrUnknownIndex_Type = Unsigned32
_DellNetBgpM2PathAttrUnknownIndex_Object = MibTableColumn
dellNetBgpM2PathAttrUnknownIndex = _DellNetBgpM2PathAttrUnknownIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 7, 1, 1),
    _DellNetBgpM2PathAttrUnknownIndex_Type()
)
dellNetBgpM2PathAttrUnknownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrUnknownIndex.setStatus("current")
_DellNetBgpM2PathAttrUnknownType_Type = Unsigned32
_DellNetBgpM2PathAttrUnknownType_Object = MibTableColumn
dellNetBgpM2PathAttrUnknownType = _DellNetBgpM2PathAttrUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 7, 1, 2),
    _DellNetBgpM2PathAttrUnknownType_Type()
)
dellNetBgpM2PathAttrUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrUnknownType.setStatus("current")


class _DellNetBgpM2PathAttrUnknownValue_Type(OctetString):
    """Custom type dellNetBgpM2PathAttrUnknownValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4070),
    )


_DellNetBgpM2PathAttrUnknownValue_Type.__name__ = "OctetString"
_DellNetBgpM2PathAttrUnknownValue_Object = MibTableColumn
dellNetBgpM2PathAttrUnknownValue = _DellNetBgpM2PathAttrUnknownValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 7, 1, 3),
    _DellNetBgpM2PathAttrUnknownValue_Type()
)
dellNetBgpM2PathAttrUnknownValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrUnknownValue.setStatus("current")
_DellNetBgpM2PathAttrExtensions_ObjectIdentity = ObjectIdentity
dellNetBgpM2PathAttrExtensions = _DellNetBgpM2PathAttrExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8)
)
_DellNetBgpM2PathAttrNonCapExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2PathAttrNonCapExts = _DellNetBgpM2PathAttrNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1)
)
_DellNetBgpM2PathAttrCommunityExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2PathAttrCommunityExts = _DellNetBgpM2PathAttrCommunityExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 1997)
)
_DellNetBgpM2PathAttrCommTable_Object = MibTable
dellNetBgpM2PathAttrCommTable = _DellNetBgpM2PathAttrCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 1997, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrCommTable.setStatus("current")
_DellNetBgpM2PathAttrCommEntry_Object = MibTableRow
dellNetBgpM2PathAttrCommEntry = _DellNetBgpM2PathAttrCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 1997, 1, 1)
)
dellNetBgpM2PathAttrCommEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrCommIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrCommEntry.setStatus("current")
_DellNetBgpM2PathAttrCommIndex_Type = Unsigned32
_DellNetBgpM2PathAttrCommIndex_Object = MibTableColumn
dellNetBgpM2PathAttrCommIndex = _DellNetBgpM2PathAttrCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 1997, 1, 1, 1),
    _DellNetBgpM2PathAttrCommIndex_Type()
)
dellNetBgpM2PathAttrCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrCommIndex.setStatus("current")
_DellNetBgpM2PathAttrCommValue_Type = DellNetBgpM2Community
_DellNetBgpM2PathAttrCommValue_Object = MibTableColumn
dellNetBgpM2PathAttrCommValue = _DellNetBgpM2PathAttrCommValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 1997, 1, 1, 2),
    _DellNetBgpM2PathAttrCommValue_Type()
)
dellNetBgpM2PathAttrCommValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrCommValue.setStatus("current")
_DellNetBgpM2LinkLocalNextHopTable_Object = MibTable
dellNetBgpM2LinkLocalNextHopTable = _DellNetBgpM2LinkLocalNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2545)
)
if mibBuilder.loadTexts:
    dellNetBgpM2LinkLocalNextHopTable.setStatus("current")
_DellNetBgpM2LinkLocalNextHopEntry_Object = MibTableRow
dellNetBgpM2LinkLocalNextHopEntry = _DellNetBgpM2LinkLocalNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2545, 1)
)
dellNetBgpM2LinkLocalNextHopEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2LinkLocalNextHopEntry.setStatus("current")
_DellNetBgpM2LinkLocalNextHopPresent_Type = TruthValue
_DellNetBgpM2LinkLocalNextHopPresent_Object = MibTableColumn
dellNetBgpM2LinkLocalNextHopPresent = _DellNetBgpM2LinkLocalNextHopPresent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2545, 1, 1),
    _DellNetBgpM2LinkLocalNextHopPresent_Type()
)
dellNetBgpM2LinkLocalNextHopPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2LinkLocalNextHopPresent.setStatus("current")


class _DellNetBgpM2LinkLocalNextHop_Type(InetAddress):
    """Custom type dellNetBgpM2LinkLocalNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_DellNetBgpM2LinkLocalNextHop_Type.__name__ = "InetAddress"
_DellNetBgpM2LinkLocalNextHop_Object = MibTableColumn
dellNetBgpM2LinkLocalNextHop = _DellNetBgpM2LinkLocalNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2545, 1, 2),
    _DellNetBgpM2LinkLocalNextHop_Type()
)
dellNetBgpM2LinkLocalNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2LinkLocalNextHop.setStatus("current")
_DellNetBgpM2PathAttrRouteReflectionExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2PathAttrRouteReflectionExts = _DellNetBgpM2PathAttrRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796)
)
_DellNetBgpM2PathAttrOriginatorIdTable_Object = MibTable
dellNetBgpM2PathAttrOriginatorIdTable = _DellNetBgpM2PathAttrOriginatorIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrOriginatorIdTable.setStatus("current")
_DellNetBgpM2PathAttrOriginatorIdEntry_Object = MibTableRow
dellNetBgpM2PathAttrOriginatorIdEntry = _DellNetBgpM2PathAttrOriginatorIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 1, 1)
)
dellNetBgpM2PathAttrOriginatorIdEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrOriginatorIdEntry.setStatus("current")
_DellNetBgpM2PathAttrOriginatorId_Type = DellNetBgpM2Identifier
_DellNetBgpM2PathAttrOriginatorId_Object = MibTableColumn
dellNetBgpM2PathAttrOriginatorId = _DellNetBgpM2PathAttrOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 1, 1, 1),
    _DellNetBgpM2PathAttrOriginatorId_Type()
)
dellNetBgpM2PathAttrOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrOriginatorId.setStatus("current")
_DellNetBgpM2PathAttrClusterTable_Object = MibTable
dellNetBgpM2PathAttrClusterTable = _DellNetBgpM2PathAttrClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 2)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrClusterTable.setStatus("current")
_DellNetBgpM2PathAttrClusterEntry_Object = MibTableRow
dellNetBgpM2PathAttrClusterEntry = _DellNetBgpM2PathAttrClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 2, 1)
)
dellNetBgpM2PathAttrClusterEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrClusterIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrClusterEntry.setStatus("current")
_DellNetBgpM2PathAttrClusterIndex_Type = Unsigned32
_DellNetBgpM2PathAttrClusterIndex_Object = MibTableColumn
dellNetBgpM2PathAttrClusterIndex = _DellNetBgpM2PathAttrClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 2, 1, 1),
    _DellNetBgpM2PathAttrClusterIndex_Type()
)
dellNetBgpM2PathAttrClusterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrClusterIndex.setStatus("current")
_DellNetBgpM2PathAttrClusterValue_Type = DellNetBgpM2Identifier
_DellNetBgpM2PathAttrClusterValue_Object = MibTableColumn
dellNetBgpM2PathAttrClusterValue = _DellNetBgpM2PathAttrClusterValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 2796, 2, 1, 2),
    _DellNetBgpM2PathAttrClusterValue_Type()
)
dellNetBgpM2PathAttrClusterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrClusterValue.setStatus("current")
_DellNetBgpM2PathAttrExtCommTable_Object = MibTable
dellNetBgpM2PathAttrExtCommTable = _DellNetBgpM2PathAttrExtCommTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 3501)
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrExtCommTable.setStatus("current")
_DellNetBgpM2PathAttrExtCommEntry_Object = MibTableRow
dellNetBgpM2PathAttrExtCommEntry = _DellNetBgpM2PathAttrExtCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 3501, 1)
)
dellNetBgpM2PathAttrExtCommEntry.setIndexNames(
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrIndex"),
    (0, "DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrExtCommIndex"),
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrExtCommEntry.setStatus("current")
_DellNetBgpM2PathAttrExtCommIndex_Type = Unsigned32
_DellNetBgpM2PathAttrExtCommIndex_Object = MibTableColumn
dellNetBgpM2PathAttrExtCommIndex = _DellNetBgpM2PathAttrExtCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 3501, 1, 1),
    _DellNetBgpM2PathAttrExtCommIndex_Type()
)
dellNetBgpM2PathAttrExtCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrExtCommIndex.setStatus("current")
_DellNetBgpM2PathAttrExtCommValue_Type = DellNetBgpM2ExtendedCommunity
_DellNetBgpM2PathAttrExtCommValue_Object = MibTableColumn
dellNetBgpM2PathAttrExtCommValue = _DellNetBgpM2PathAttrExtCommValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 1, 3501, 1, 2),
    _DellNetBgpM2PathAttrExtCommValue_Type()
)
dellNetBgpM2PathAttrExtCommValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttrExtCommValue.setStatus("current")
_DellNetBgpM2PathAttrCapExts_ObjectIdentity = ObjectIdentity
dellNetBgpM2PathAttrCapExts = _DellNetBgpM2PathAttrCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 3, 8, 2)
)
_DellNetBgpM2Conformance_ObjectIdentity = ObjectIdentity
dellNetBgpM2Conformance = _DellNetBgpM2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4)
)
_DellNetBgpM2MIBCompliances_ObjectIdentity = ObjectIdentity
dellNetBgpM2MIBCompliances = _DellNetBgpM2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 1)
)
_DellNetBgpM2MIBGroups_ObjectIdentity = ObjectIdentity
dellNetBgpM2MIBGroups = _DellNetBgpM2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2)
)
dellNetBgpM2PeerEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2PeerErrorsEntry")
)
dellNetBgpM2PeerErrorsEntry.setIndexNames(*dellNetBgpM2PeerEntry.getIndexNames())
dellNetBgpM2PeerEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2PeerEventTimesEntry")
)
dellNetBgpM2PeerEventTimesEntry.setIndexNames(*dellNetBgpM2PeerEntry.getIndexNames())
dellNetBgpM2PeerEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2PeerConfiguredTimersEntry")
)
dellNetBgpM2PeerConfiguredTimersEntry.setIndexNames(*dellNetBgpM2PeerEntry.getIndexNames())
dellNetBgpM2PeerEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2PeerNegotiatedTimersEntry")
)
dellNetBgpM2PeerNegotiatedTimersEntry.setIndexNames(*dellNetBgpM2PeerEntry.getIndexNames())
dellNetBgpM2PeerEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2PeerCountersEntry")
)
dellNetBgpM2PeerCountersEntry.setIndexNames(*dellNetBgpM2PeerEntry.getIndexNames())
dellNetBgpM2PeerEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2PeerReflectorClientEntry")
)
dellNetBgpM2PeerReflectorClientEntry.setIndexNames(*dellNetBgpM2PeerEntry.getIndexNames())
dellNetBgpM2PeerEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2PeerConfedMemberEntry")
)
dellNetBgpM2PeerConfedMemberEntry.setIndexNames(*dellNetBgpM2PeerEntry.getIndexNames())
dellNetBgpM2CfgPeerEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2CfgPeerTimersEntry")
)
dellNetBgpM2CfgPeerTimersEntry.setIndexNames(*dellNetBgpM2CfgPeerEntry.getIndexNames())
dellNetBgpM2CfgPeerEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2CfgPeerReflectorClientEntry")
)
dellNetBgpM2CfgPeerReflectorClientEntry.setIndexNames(*dellNetBgpM2CfgPeerEntry.getIndexNames())
dellNetBgpM2PeerEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2CfgPeerConfedMemberEntry")
)
dellNetBgpM2CfgPeerConfedMemberEntry.setIndexNames(*dellNetBgpM2PeerEntry.getIndexNames())
dellNetBgpM2PathAttrEntry.registerAugmentions(
    ("DELL-NETWORKING-BGP4-V2-MIB",
     "dellNetBgpM2AsPath4byteEntry")
)
dellNetBgpM2AsPath4byteEntry.setIndexNames(*dellNetBgpM2PathAttrEntry.getIndexNames())

# Managed Objects groups

dellNetBgpM2CommunitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 1)
)
dellNetBgpM2CommunitiesGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrCommIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrCommValue"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2CommunitiesGroup.setStatus("current")

dellNetBgpM2ExtCommunitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 2)
)
dellNetBgpM2ExtCommunitiesGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrExtCommIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrExtCommValue"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2ExtCommunitiesGroup.setStatus("current")

dellNetBgpM2RouteReflectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 3)
)
dellNetBgpM2RouteReflectionGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2RouteReflector"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2ClusterId"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerReflectorClient"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrOriginatorId"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrClusterIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrClusterValue"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2RouteReflectionGroup.setStatus("current")

dellNetBgpM2AsConfederationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 4)
)
dellNetBgpM2AsConfederationGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2ConfederationRouter"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2ConfederationId"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerConfedMember"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2AsConfederationGroup.setStatus("current")

dellNetBgpM2TimersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 5)
)
dellNetBgpM2TimersGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerFsmEstablishedTime"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerInUpdatesElapsedTime"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerConnectRetryInterval"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerHoldTimeConfigured"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerKeepAliveConfigured"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerMinASOrigInterval"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerMinRouteAdverInterval"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerHoldTime"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerKeepAlive"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2TimersGroup.setStatus("current")

dellNetBgpM2CountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 6)
)
dellNetBgpM2CountersGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerInUpdates"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerOutUpdates"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerInTotalMessages"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerOutTotalMessages"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerFsmEstablishedTrans"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerInKeepalives"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerOutKeepalives"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerInOpen"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerOutOpen"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerInRteRefresh"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerOutRteRefresh"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PrefixCountersAfi"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PrefixCountersSafi"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PrefixInPrefixes"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PrefixInPrefixesAccepted"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PrefixInPrefixesRejected"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PrefixOutPrefixes"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PrefixWdrawnByPeer"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PrefixWdrawnFromPeer"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2CountersGroup.setStatus("current")

dellNetBgpM2CapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 7)
)
dellNetBgpM2CapabilitiesGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CapabilitySupportAvailable"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2SupportedCapabilityCode"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2SupportedCapability"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerCapAnnouncedCode"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerCapAnnouncedIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerCapAnnouncedValue"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerCapReceivedCode"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerCapReceivedIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerCapReceivedValue"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2CapabilitiesGroup.setStatus("current")

dellNetBgpM2AsPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 8)
)
dellNetBgpM2AsPathGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathSegmentIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathElementIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathElementValue"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2AsPathGroup.setStatus("current")

dellNetBgpM2As4byteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 9)
)
dellNetBgpM2As4byteGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsSize"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPath4bytePathPresent"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPath4byteAggregatorAS"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPath4byteCalcLength"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPath4byteString"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPath4byteIndex"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2As4byteGroup.setStatus("current")

dellNetBgpM2BaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 10)
)
dellNetBgpM2BaseGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2LocalAs"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2LocalIdentifier"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2VersionIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2VersionSupported"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2BaseGroup.setStatus("current")

dellNetBgpM2ErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 11)
)
dellNetBgpM2ErrorsGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorReceived"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorReceivedData"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorReceivedTime"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorReceivedText"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorSent"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorSentData"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorSentTime"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorSentText"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2ErrorsGroup.setStatus("current")

dellNetBgpM2PeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 12)
)
dellNetBgpM2PeerGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerInstance"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerIdentifier"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerState"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerStatus"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerConfiguredVersion"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerNegotiatedVersion"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLocalAddrType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLocalAddr"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLocalPort"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLocalAs"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerRemoteAddrType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerRemoteAddr"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerRemotePort"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerRemoteAs"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerIndex"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerGroup.setStatus("current")

dellNetBgpM2PathAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 13)
)
dellNetBgpM2PathAttributesGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrCount"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathCalcLength"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathElementValue"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathString"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AsPathType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriAfi"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriBest"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriPrefixType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriPrefix"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriPrefixLen"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriSafi"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriOpaqueType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriOpaquePointer"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2NlriCalcLocalPref"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AdjRibsOutIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2AdjRibsOutRoute"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrAggregatorAS"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrAggregatorAddr"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrAtomicAggregate"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrLocalPref"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrLocalPrefPresent"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrMed"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrMedPresent"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrNextHop"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrNextHopAddrType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrOrigin"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrUnknownIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrUnknownType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PathAttrUnknownValue"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2PathAttributesGroup.setStatus("current")

dellNetBgpM2PeerConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 14)
)
dellNetBgpM2PeerConfigurationGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgBaseScalarStorageType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgLocalAs"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgLocalIdentifier"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerAdminStatus"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerNextIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerConfiguredVersion"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgAllowVersionNegotiation"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerLocalAddrType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerLocalAddr"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerLocalAs"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerRemoteAddrType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerRemoteAddr"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerRemoteAs"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerEntryStorageType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerError"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerBgpPeerEntry"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerRowEntryStatus"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerIndex"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerStatus"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerConnectRetryInterval"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerHoldTimeConfigured"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerKeepAliveConfigured"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerMinASOrigInterval"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerMinRouteAdverInter"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerConfigurationGroup.setStatus("current")

dellNetBgpM2PeerRouteReflectorCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 15)
)
dellNetBgpM2PeerRouteReflectorCfgGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgRouteReflector"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgClusterId"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerReflectorClient"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerRouteReflectorCfgGroup.setStatus("current")

dellNetBgpM2PeerAsConfederationCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 16)
)
dellNetBgpM2PeerAsConfederationCfgGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgConfederationRouter"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgConfederationId"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2CfgPeerConfedMember"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2PeerAsConfederationCfgGroup.setStatus("current")

dellNetBgpM2Rfc2545Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 18)
)
dellNetBgpM2Rfc2545Group.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2LinkLocalNextHopPresent"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2LinkLocalNextHop"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2Rfc2545Group.setStatus("current")


# Notification objects

dellNetBgpM2Established = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 0, 1)
)
dellNetBgpM2Established.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLocalAddrType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLocalAddr"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerRemoteAddrType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerRemoteAddr"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorReceived"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerState"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2Established.setStatus(
        "current"
    )

dellNetBgpM2BackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 1, 0, 2)
)
dellNetBgpM2BackwardTransition.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLocalAddrType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLocalAddr"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerRemoteAddrType"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerRemoteAddr"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorReceived"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerLastErrorReceivedText"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2PeerState"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2BackwardTransition.setStatus(
        "current"
    )


# Notifications groups

dellNetBgpM2MIBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 2, 17)
)
dellNetBgpM2MIBNotificationsGroup.setObjects(
      *(("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2Established"),
        ("DELL-NETWORKING-BGP4-V2-MIB", "dellNetBgpM2BackwardTransition"))
)
if mibBuilder.loadTexts:
    dellNetBgpM2MIBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dellNetBgpM2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 20, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetBgpM2MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-BGP4-V2-MIB",
    **{"DellNetBgpM2Identifier": DellNetBgpM2Identifier,
       "DellNetBgpM2Afi": DellNetBgpM2Afi,
       "DellNetBgpM2Safi": DellNetBgpM2Safi,
       "DellNetBgpM2Community": DellNetBgpM2Community,
       "DellNetBgpM2ExtendedCommunity": DellNetBgpM2ExtendedCommunity,
       "dellNetBgpM2": dellNetBgpM2,
       "dellNetBgpM2BaseScalars": dellNetBgpM2BaseScalars,
       "dellNetBgpM2BaseNotifications": dellNetBgpM2BaseNotifications,
       "dellNetBgpM2Established": dellNetBgpM2Established,
       "dellNetBgpM2BackwardTransition": dellNetBgpM2BackwardTransition,
       "dellNetBgpM2Version": dellNetBgpM2Version,
       "dellNetBgpM2VersionTable": dellNetBgpM2VersionTable,
       "dellNetBgpM2VersionEntry": dellNetBgpM2VersionEntry,
       "dellNetBgpM2VersionIndex": dellNetBgpM2VersionIndex,
       "dellNetBgpM2VersionSupported": dellNetBgpM2VersionSupported,
       "dellNetBgpM2SupportedCapabilities": dellNetBgpM2SupportedCapabilities,
       "dellNetBgpM2CapabilitySupportAvailable": dellNetBgpM2CapabilitySupportAvailable,
       "dellNetBgpM2SupportedCapabilitiesTable": dellNetBgpM2SupportedCapabilitiesTable,
       "dellNetBgpM2SupportedCapabilitiesEntry": dellNetBgpM2SupportedCapabilitiesEntry,
       "dellNetBgpM2SupportedCapabilityCode": dellNetBgpM2SupportedCapabilityCode,
       "dellNetBgpM2SupportedCapability": dellNetBgpM2SupportedCapability,
       "dellNetBgpM2AsSize": dellNetBgpM2AsSize,
       "dellNetBgpM2LocalAs": dellNetBgpM2LocalAs,
       "dellNetBgpM2LocalIdentifier": dellNetBgpM2LocalIdentifier,
       "dellNetBgpM2BaseScalarExtensions": dellNetBgpM2BaseScalarExtensions,
       "dellNetBgpM2BaseScalarNonCapExts": dellNetBgpM2BaseScalarNonCapExts,
       "dellNetBgpM2BaseScalarRouteReflectExts": dellNetBgpM2BaseScalarRouteReflectExts,
       "dellNetBgpM2RouteReflector": dellNetBgpM2RouteReflector,
       "dellNetBgpM2ClusterId": dellNetBgpM2ClusterId,
       "dellNetBgpM2BaseScalarASConfedExts": dellNetBgpM2BaseScalarASConfedExts,
       "dellNetBgpM2ConfederationRouter": dellNetBgpM2ConfederationRouter,
       "dellNetBgpM2ConfederationId": dellNetBgpM2ConfederationId,
       "dellNetBgpM2BaseScalarCapExts": dellNetBgpM2BaseScalarCapExts,
       "dellNetBgpM2BaseScalarConfiguration": dellNetBgpM2BaseScalarConfiguration,
       "dellNetBgpM2CfgBaseScalarStorageType": dellNetBgpM2CfgBaseScalarStorageType,
       "dellNetBgpM2CfgLocalAs": dellNetBgpM2CfgLocalAs,
       "dellNetBgpM2CfgLocalIdentifier": dellNetBgpM2CfgLocalIdentifier,
       "dellNetBgpM2CfgBaseScalarExtensions": dellNetBgpM2CfgBaseScalarExtensions,
       "dellNetBgpM2CfgBaseScalarNonCapExts": dellNetBgpM2CfgBaseScalarNonCapExts,
       "dellNetBgpM2CfgBaseScalarReflectorExts": dellNetBgpM2CfgBaseScalarReflectorExts,
       "dellNetBgpM2CfgRouteReflector": dellNetBgpM2CfgRouteReflector,
       "dellNetBgpM2CfgClusterId": dellNetBgpM2CfgClusterId,
       "dellNetBgpM2CfgBaseScalarASConfedExts": dellNetBgpM2CfgBaseScalarASConfedExts,
       "dellNetBgpM2CfgConfederationRouter": dellNetBgpM2CfgConfederationRouter,
       "dellNetBgpM2CfgConfederationId": dellNetBgpM2CfgConfederationId,
       "dellNetBgpM2CfgBaseScalarCapExts": dellNetBgpM2CfgBaseScalarCapExts,
       "dellNetBgpM2Peer": dellNetBgpM2Peer,
       "dellNetBgpM2PeerData": dellNetBgpM2PeerData,
       "dellNetBgpM2PeerTable": dellNetBgpM2PeerTable,
       "dellNetBgpM2PeerEntry": dellNetBgpM2PeerEntry,
       "dellNetBgpM2PeerInstance": dellNetBgpM2PeerInstance,
       "dellNetBgpM2PeerIdentifier": dellNetBgpM2PeerIdentifier,
       "dellNetBgpM2PeerState": dellNetBgpM2PeerState,
       "dellNetBgpM2PeerStatus": dellNetBgpM2PeerStatus,
       "dellNetBgpM2PeerConfiguredVersion": dellNetBgpM2PeerConfiguredVersion,
       "dellNetBgpM2PeerNegotiatedVersion": dellNetBgpM2PeerNegotiatedVersion,
       "dellNetBgpM2PeerLocalAddrType": dellNetBgpM2PeerLocalAddrType,
       "dellNetBgpM2PeerLocalAddr": dellNetBgpM2PeerLocalAddr,
       "dellNetBgpM2PeerLocalPort": dellNetBgpM2PeerLocalPort,
       "dellNetBgpM2PeerLocalAs": dellNetBgpM2PeerLocalAs,
       "dellNetBgpM2PeerRemoteAddrType": dellNetBgpM2PeerRemoteAddrType,
       "dellNetBgpM2PeerRemoteAddr": dellNetBgpM2PeerRemoteAddr,
       "dellNetBgpM2PeerRemotePort": dellNetBgpM2PeerRemotePort,
       "dellNetBgpM2PeerRemoteAs": dellNetBgpM2PeerRemoteAs,
       "dellNetBgpM2PeerIndex": dellNetBgpM2PeerIndex,
       "dellNetBgpM2PeerErrors": dellNetBgpM2PeerErrors,
       "dellNetBgpM2PeerErrorsTable": dellNetBgpM2PeerErrorsTable,
       "dellNetBgpM2PeerErrorsEntry": dellNetBgpM2PeerErrorsEntry,
       "dellNetBgpM2PeerLastErrorReceived": dellNetBgpM2PeerLastErrorReceived,
       "dellNetBgpM2PeerLastErrorSent": dellNetBgpM2PeerLastErrorSent,
       "dellNetBgpM2PeerLastErrorReceivedTime": dellNetBgpM2PeerLastErrorReceivedTime,
       "dellNetBgpM2PeerLastErrorSentTime": dellNetBgpM2PeerLastErrorSentTime,
       "dellNetBgpM2PeerLastErrorReceivedText": dellNetBgpM2PeerLastErrorReceivedText,
       "dellNetBgpM2PeerLastErrorSentText": dellNetBgpM2PeerLastErrorSentText,
       "dellNetBgpM2PeerLastErrorReceivedData": dellNetBgpM2PeerLastErrorReceivedData,
       "dellNetBgpM2PeerLastErrorSentData": dellNetBgpM2PeerLastErrorSentData,
       "dellNetBgpM2PeerTimers": dellNetBgpM2PeerTimers,
       "dellNetBgpM2PeerEventTimesTable": dellNetBgpM2PeerEventTimesTable,
       "dellNetBgpM2PeerEventTimesEntry": dellNetBgpM2PeerEventTimesEntry,
       "dellNetBgpM2PeerFsmEstablishedTime": dellNetBgpM2PeerFsmEstablishedTime,
       "dellNetBgpM2PeerInUpdatesElapsedTime": dellNetBgpM2PeerInUpdatesElapsedTime,
       "dellNetBgpM2PeerConfiguredTimersTable": dellNetBgpM2PeerConfiguredTimersTable,
       "dellNetBgpM2PeerConfiguredTimersEntry": dellNetBgpM2PeerConfiguredTimersEntry,
       "dellNetBgpM2PeerConnectRetryInterval": dellNetBgpM2PeerConnectRetryInterval,
       "dellNetBgpM2PeerHoldTimeConfigured": dellNetBgpM2PeerHoldTimeConfigured,
       "dellNetBgpM2PeerKeepAliveConfigured": dellNetBgpM2PeerKeepAliveConfigured,
       "dellNetBgpM2PeerMinASOrigInterval": dellNetBgpM2PeerMinASOrigInterval,
       "dellNetBgpM2PeerMinRouteAdverInterval": dellNetBgpM2PeerMinRouteAdverInterval,
       "dellNetBgpM2PeerNegotiatedTimersTable": dellNetBgpM2PeerNegotiatedTimersTable,
       "dellNetBgpM2PeerNegotiatedTimersEntry": dellNetBgpM2PeerNegotiatedTimersEntry,
       "dellNetBgpM2PeerHoldTime": dellNetBgpM2PeerHoldTime,
       "dellNetBgpM2PeerKeepAlive": dellNetBgpM2PeerKeepAlive,
       "dellNetBgpM2PeerCapabilities": dellNetBgpM2PeerCapabilities,
       "dellNetBgpM2PeerCapsAnnouncedTable": dellNetBgpM2PeerCapsAnnouncedTable,
       "dellNetBgpM2PeerCapsAnnouncedEntry": dellNetBgpM2PeerCapsAnnouncedEntry,
       "dellNetBgpM2PeerCapAnnouncedCode": dellNetBgpM2PeerCapAnnouncedCode,
       "dellNetBgpM2PeerCapAnnouncedIndex": dellNetBgpM2PeerCapAnnouncedIndex,
       "dellNetBgpM2PeerCapAnnouncedValue": dellNetBgpM2PeerCapAnnouncedValue,
       "dellNetBgpM2PeerCapsReceivedTable": dellNetBgpM2PeerCapsReceivedTable,
       "dellNetBgpM2PeerCapsReceivedEntry": dellNetBgpM2PeerCapsReceivedEntry,
       "dellNetBgpM2PeerCapReceivedCode": dellNetBgpM2PeerCapReceivedCode,
       "dellNetBgpM2PeerCapReceivedIndex": dellNetBgpM2PeerCapReceivedIndex,
       "dellNetBgpM2PeerCapReceivedValue": dellNetBgpM2PeerCapReceivedValue,
       "dellNetBgpM2PeerCounters": dellNetBgpM2PeerCounters,
       "dellNetBgpM2PeerCountersTable": dellNetBgpM2PeerCountersTable,
       "dellNetBgpM2PeerCountersEntry": dellNetBgpM2PeerCountersEntry,
       "dellNetBgpM2PeerInUpdates": dellNetBgpM2PeerInUpdates,
       "dellNetBgpM2PeerOutUpdates": dellNetBgpM2PeerOutUpdates,
       "dellNetBgpM2PeerInTotalMessages": dellNetBgpM2PeerInTotalMessages,
       "dellNetBgpM2PeerOutTotalMessages": dellNetBgpM2PeerOutTotalMessages,
       "dellNetBgpM2PeerFsmEstablishedTrans": dellNetBgpM2PeerFsmEstablishedTrans,
       "dellNetBgpM2PeerInKeepalives": dellNetBgpM2PeerInKeepalives,
       "dellNetBgpM2PeerOutKeepalives": dellNetBgpM2PeerOutKeepalives,
       "dellNetBgpM2PeerInOpen": dellNetBgpM2PeerInOpen,
       "dellNetBgpM2PeerOutOpen": dellNetBgpM2PeerOutOpen,
       "dellNetBgpM2PeerInRteRefresh": dellNetBgpM2PeerInRteRefresh,
       "dellNetBgpM2PeerOutRteRefresh": dellNetBgpM2PeerOutRteRefresh,
       "dellNetBgpM2PrefixCountersTable": dellNetBgpM2PrefixCountersTable,
       "dellNetBgpM2PrefixCountersEntry": dellNetBgpM2PrefixCountersEntry,
       "dellNetBgpM2PrefixCountersAfi": dellNetBgpM2PrefixCountersAfi,
       "dellNetBgpM2PrefixCountersSafi": dellNetBgpM2PrefixCountersSafi,
       "dellNetBgpM2PrefixInPrefixes": dellNetBgpM2PrefixInPrefixes,
       "dellNetBgpM2PrefixInPrefixesAccepted": dellNetBgpM2PrefixInPrefixesAccepted,
       "dellNetBgpM2PrefixInPrefixesRejected": dellNetBgpM2PrefixInPrefixesRejected,
       "dellNetBgpM2PrefixOutPrefixes": dellNetBgpM2PrefixOutPrefixes,
       "dellNetBgpM2PrefixWdrawnByPeer": dellNetBgpM2PrefixWdrawnByPeer,
       "dellNetBgpM2PrefixWdrawnFromPeer": dellNetBgpM2PrefixWdrawnFromPeer,
       "dellNetBgpM2PeerExtensions": dellNetBgpM2PeerExtensions,
       "dellNetBgpM2PeerNonCapExts": dellNetBgpM2PeerNonCapExts,
       "dellNetBgpM2PeerRouteReflectionExts": dellNetBgpM2PeerRouteReflectionExts,
       "dellNetBgpM2PeerReflectorClientTable": dellNetBgpM2PeerReflectorClientTable,
       "dellNetBgpM2PeerReflectorClientEntry": dellNetBgpM2PeerReflectorClientEntry,
       "dellNetBgpM2PeerReflectorClient": dellNetBgpM2PeerReflectorClient,
       "dellNetBgpM2PeerASConfederationExts": dellNetBgpM2PeerASConfederationExts,
       "dellNetBgpM2PeerConfedMemberTable": dellNetBgpM2PeerConfedMemberTable,
       "dellNetBgpM2PeerConfedMemberEntry": dellNetBgpM2PeerConfedMemberEntry,
       "dellNetBgpM2PeerConfedMember": dellNetBgpM2PeerConfedMember,
       "dellNetBgpM2PeerCapExts": dellNetBgpM2PeerCapExts,
       "dellNetBgpM2PeerConfiguration": dellNetBgpM2PeerConfiguration,
       "dellNetBgpM2CfgPeerAdminStatusTable": dellNetBgpM2CfgPeerAdminStatusTable,
       "dellNetBgpM2CfgPeerAdminStatusEntry": dellNetBgpM2CfgPeerAdminStatusEntry,
       "dellNetBgpM2CfgPeerAdminStatus": dellNetBgpM2CfgPeerAdminStatus,
       "dellNetBgpM2CfgPeerNextIndex": dellNetBgpM2CfgPeerNextIndex,
       "dellNetBgpM2CfgPeerTable": dellNetBgpM2CfgPeerTable,
       "dellNetBgpM2CfgPeerEntry": dellNetBgpM2CfgPeerEntry,
       "dellNetBgpM2CfgPeerConfiguredVersion": dellNetBgpM2CfgPeerConfiguredVersion,
       "dellNetBgpM2CfgAllowVersionNegotiation": dellNetBgpM2CfgAllowVersionNegotiation,
       "dellNetBgpM2CfgPeerLocalAddrType": dellNetBgpM2CfgPeerLocalAddrType,
       "dellNetBgpM2CfgPeerLocalAddr": dellNetBgpM2CfgPeerLocalAddr,
       "dellNetBgpM2CfgPeerLocalAs": dellNetBgpM2CfgPeerLocalAs,
       "dellNetBgpM2CfgPeerRemoteAddrType": dellNetBgpM2CfgPeerRemoteAddrType,
       "dellNetBgpM2CfgPeerRemoteAddr": dellNetBgpM2CfgPeerRemoteAddr,
       "dellNetBgpM2CfgPeerRemoteAs": dellNetBgpM2CfgPeerRemoteAs,
       "dellNetBgpM2CfgPeerEntryStorageType": dellNetBgpM2CfgPeerEntryStorageType,
       "dellNetBgpM2CfgPeerError": dellNetBgpM2CfgPeerError,
       "dellNetBgpM2CfgPeerBgpPeerEntry": dellNetBgpM2CfgPeerBgpPeerEntry,
       "dellNetBgpM2CfgPeerRowEntryStatus": dellNetBgpM2CfgPeerRowEntryStatus,
       "dellNetBgpM2CfgPeerIndex": dellNetBgpM2CfgPeerIndex,
       "dellNetBgpM2CfgPeerStatus": dellNetBgpM2CfgPeerStatus,
       "dellNetBgpM2CfgPeerTimersTable": dellNetBgpM2CfgPeerTimersTable,
       "dellNetBgpM2CfgPeerTimersEntry": dellNetBgpM2CfgPeerTimersEntry,
       "dellNetBgpM2CfgPeerConnectRetryInterval": dellNetBgpM2CfgPeerConnectRetryInterval,
       "dellNetBgpM2CfgPeerHoldTimeConfigured": dellNetBgpM2CfgPeerHoldTimeConfigured,
       "dellNetBgpM2CfgPeerKeepAliveConfigured": dellNetBgpM2CfgPeerKeepAliveConfigured,
       "dellNetBgpM2CfgPeerMinASOrigInterval": dellNetBgpM2CfgPeerMinASOrigInterval,
       "dellNetBgpM2CfgPeerMinRouteAdverInter": dellNetBgpM2CfgPeerMinRouteAdverInter,
       "dellNetBgpM2CfgPeerExtensions": dellNetBgpM2CfgPeerExtensions,
       "dellNetBgpM2CfgPeerNonCapExts": dellNetBgpM2CfgPeerNonCapExts,
       "dellNetBgpM2CfgPeerRouteReflectionExts": dellNetBgpM2CfgPeerRouteReflectionExts,
       "dellNetBgpM2CfgPeerReflectorClientTable": dellNetBgpM2CfgPeerReflectorClientTable,
       "dellNetBgpM2CfgPeerReflectorClientEntry": dellNetBgpM2CfgPeerReflectorClientEntry,
       "dellNetBgpM2CfgPeerReflectorClient": dellNetBgpM2CfgPeerReflectorClient,
       "dellNetBgpM2CfgPeerASConfederationExts": dellNetBgpM2CfgPeerASConfederationExts,
       "dellNetBgpM2CfgPeerConfedMemberTable": dellNetBgpM2CfgPeerConfedMemberTable,
       "dellNetBgpM2CfgPeerConfedMemberEntry": dellNetBgpM2CfgPeerConfedMemberEntry,
       "dellNetBgpM2CfgPeerConfedMember": dellNetBgpM2CfgPeerConfedMember,
       "dellNetBgpM2CfgPeerCapExts": dellNetBgpM2CfgPeerCapExts,
       "dellNetBgpM2Rib": dellNetBgpM2Rib,
       "dellNetBgpM2NlriTable": dellNetBgpM2NlriTable,
       "dellNetBgpM2NlriEntry": dellNetBgpM2NlriEntry,
       "dellNetBgpM2NlriIndex": dellNetBgpM2NlriIndex,
       "dellNetBgpM2NlriAfi": dellNetBgpM2NlriAfi,
       "dellNetBgpM2NlriSafi": dellNetBgpM2NlriSafi,
       "dellNetBgpM2NlriPrefixType": dellNetBgpM2NlriPrefixType,
       "dellNetBgpM2NlriPrefix": dellNetBgpM2NlriPrefix,
       "dellNetBgpM2NlriPrefixLen": dellNetBgpM2NlriPrefixLen,
       "dellNetBgpM2NlriBest": dellNetBgpM2NlriBest,
       "dellNetBgpM2NlriCalcLocalPref": dellNetBgpM2NlriCalcLocalPref,
       "dellNetBgpM2PathAttrIndex": dellNetBgpM2PathAttrIndex,
       "dellNetBgpM2NlriOpaqueType": dellNetBgpM2NlriOpaqueType,
       "dellNetBgpM2NlriOpaquePointer": dellNetBgpM2NlriOpaquePointer,
       "dellNetBgpM2AdjRibsOutTable": dellNetBgpM2AdjRibsOutTable,
       "dellNetBgpM2AdjRibsOutEntry": dellNetBgpM2AdjRibsOutEntry,
       "dellNetBgpM2AdjRibsOutIndex": dellNetBgpM2AdjRibsOutIndex,
       "dellNetBgpM2AdjRibsOutRoute": dellNetBgpM2AdjRibsOutRoute,
       "dellNetBgpM2PathAttrCount": dellNetBgpM2PathAttrCount,
       "dellNetBgpM2PathAttrTable": dellNetBgpM2PathAttrTable,
       "dellNetBgpM2PathAttrEntry": dellNetBgpM2PathAttrEntry,
       "dellNetBgpM2PathAttrOrigin": dellNetBgpM2PathAttrOrigin,
       "dellNetBgpM2PathAttrNextHopAddrType": dellNetBgpM2PathAttrNextHopAddrType,
       "dellNetBgpM2PathAttrNextHop": dellNetBgpM2PathAttrNextHop,
       "dellNetBgpM2PathAttrMedPresent": dellNetBgpM2PathAttrMedPresent,
       "dellNetBgpM2PathAttrMed": dellNetBgpM2PathAttrMed,
       "dellNetBgpM2PathAttrLocalPrefPresent": dellNetBgpM2PathAttrLocalPrefPresent,
       "dellNetBgpM2PathAttrLocalPref": dellNetBgpM2PathAttrLocalPref,
       "dellNetBgpM2PathAttrAtomicAggregate": dellNetBgpM2PathAttrAtomicAggregate,
       "dellNetBgpM2PathAttrAggregatorAS": dellNetBgpM2PathAttrAggregatorAS,
       "dellNetBgpM2PathAttrAggregatorAddr": dellNetBgpM2PathAttrAggregatorAddr,
       "dellNetBgpM2AsPathCalcLength": dellNetBgpM2AsPathCalcLength,
       "dellNetBgpM2AsPathString": dellNetBgpM2AsPathString,
       "dellNetBgpM2AsPathIndex": dellNetBgpM2AsPathIndex,
       "dellNetBgpM2AsPath4byteTable": dellNetBgpM2AsPath4byteTable,
       "dellNetBgpM2AsPath4byteEntry": dellNetBgpM2AsPath4byteEntry,
       "dellNetBgpM2AsPath4bytePathPresent": dellNetBgpM2AsPath4bytePathPresent,
       "dellNetBgpM2AsPath4byteAggregatorAS": dellNetBgpM2AsPath4byteAggregatorAS,
       "dellNetBgpM2AsPath4byteCalcLength": dellNetBgpM2AsPath4byteCalcLength,
       "dellNetBgpM2AsPath4byteString": dellNetBgpM2AsPath4byteString,
       "dellNetBgpM2AsPath4byteIndex": dellNetBgpM2AsPath4byteIndex,
       "dellNetBgpM2AsPathTable": dellNetBgpM2AsPathTable,
       "dellNetBgpM2AsPathTableEntry": dellNetBgpM2AsPathTableEntry,
       "dellNetBgpM2AsPathSegmentIndex": dellNetBgpM2AsPathSegmentIndex,
       "dellNetBgpM2AsPathElementIndex": dellNetBgpM2AsPathElementIndex,
       "dellNetBgpM2AsPathType": dellNetBgpM2AsPathType,
       "dellNetBgpM2AsPathElementValue": dellNetBgpM2AsPathElementValue,
       "dellNetBgpM2PathAttrUnknownTable": dellNetBgpM2PathAttrUnknownTable,
       "dellNetBgpM2PathAttrUnknownEntry": dellNetBgpM2PathAttrUnknownEntry,
       "dellNetBgpM2PathAttrUnknownIndex": dellNetBgpM2PathAttrUnknownIndex,
       "dellNetBgpM2PathAttrUnknownType": dellNetBgpM2PathAttrUnknownType,
       "dellNetBgpM2PathAttrUnknownValue": dellNetBgpM2PathAttrUnknownValue,
       "dellNetBgpM2PathAttrExtensions": dellNetBgpM2PathAttrExtensions,
       "dellNetBgpM2PathAttrNonCapExts": dellNetBgpM2PathAttrNonCapExts,
       "dellNetBgpM2PathAttrCommunityExts": dellNetBgpM2PathAttrCommunityExts,
       "dellNetBgpM2PathAttrCommTable": dellNetBgpM2PathAttrCommTable,
       "dellNetBgpM2PathAttrCommEntry": dellNetBgpM2PathAttrCommEntry,
       "dellNetBgpM2PathAttrCommIndex": dellNetBgpM2PathAttrCommIndex,
       "dellNetBgpM2PathAttrCommValue": dellNetBgpM2PathAttrCommValue,
       "dellNetBgpM2LinkLocalNextHopTable": dellNetBgpM2LinkLocalNextHopTable,
       "dellNetBgpM2LinkLocalNextHopEntry": dellNetBgpM2LinkLocalNextHopEntry,
       "dellNetBgpM2LinkLocalNextHopPresent": dellNetBgpM2LinkLocalNextHopPresent,
       "dellNetBgpM2LinkLocalNextHop": dellNetBgpM2LinkLocalNextHop,
       "dellNetBgpM2PathAttrRouteReflectionExts": dellNetBgpM2PathAttrRouteReflectionExts,
       "dellNetBgpM2PathAttrOriginatorIdTable": dellNetBgpM2PathAttrOriginatorIdTable,
       "dellNetBgpM2PathAttrOriginatorIdEntry": dellNetBgpM2PathAttrOriginatorIdEntry,
       "dellNetBgpM2PathAttrOriginatorId": dellNetBgpM2PathAttrOriginatorId,
       "dellNetBgpM2PathAttrClusterTable": dellNetBgpM2PathAttrClusterTable,
       "dellNetBgpM2PathAttrClusterEntry": dellNetBgpM2PathAttrClusterEntry,
       "dellNetBgpM2PathAttrClusterIndex": dellNetBgpM2PathAttrClusterIndex,
       "dellNetBgpM2PathAttrClusterValue": dellNetBgpM2PathAttrClusterValue,
       "dellNetBgpM2PathAttrExtCommTable": dellNetBgpM2PathAttrExtCommTable,
       "dellNetBgpM2PathAttrExtCommEntry": dellNetBgpM2PathAttrExtCommEntry,
       "dellNetBgpM2PathAttrExtCommIndex": dellNetBgpM2PathAttrExtCommIndex,
       "dellNetBgpM2PathAttrExtCommValue": dellNetBgpM2PathAttrExtCommValue,
       "dellNetBgpM2PathAttrCapExts": dellNetBgpM2PathAttrCapExts,
       "dellNetBgpM2Conformance": dellNetBgpM2Conformance,
       "dellNetBgpM2MIBCompliances": dellNetBgpM2MIBCompliances,
       "dellNetBgpM2MIBCompliance": dellNetBgpM2MIBCompliance,
       "dellNetBgpM2MIBGroups": dellNetBgpM2MIBGroups,
       "dellNetBgpM2CommunitiesGroup": dellNetBgpM2CommunitiesGroup,
       "dellNetBgpM2ExtCommunitiesGroup": dellNetBgpM2ExtCommunitiesGroup,
       "dellNetBgpM2RouteReflectionGroup": dellNetBgpM2RouteReflectionGroup,
       "dellNetBgpM2AsConfederationGroup": dellNetBgpM2AsConfederationGroup,
       "dellNetBgpM2TimersGroup": dellNetBgpM2TimersGroup,
       "dellNetBgpM2CountersGroup": dellNetBgpM2CountersGroup,
       "dellNetBgpM2CapabilitiesGroup": dellNetBgpM2CapabilitiesGroup,
       "dellNetBgpM2AsPathGroup": dellNetBgpM2AsPathGroup,
       "dellNetBgpM2As4byteGroup": dellNetBgpM2As4byteGroup,
       "dellNetBgpM2BaseGroup": dellNetBgpM2BaseGroup,
       "dellNetBgpM2ErrorsGroup": dellNetBgpM2ErrorsGroup,
       "dellNetBgpM2PeerGroup": dellNetBgpM2PeerGroup,
       "dellNetBgpM2PathAttributesGroup": dellNetBgpM2PathAttributesGroup,
       "dellNetBgpM2PeerConfigurationGroup": dellNetBgpM2PeerConfigurationGroup,
       "dellNetBgpM2PeerRouteReflectorCfgGroup": dellNetBgpM2PeerRouteReflectorCfgGroup,
       "dellNetBgpM2PeerAsConfederationCfgGroup": dellNetBgpM2PeerAsConfederationCfgGroup,
       "dellNetBgpM2MIBNotificationsGroup": dellNetBgpM2MIBNotificationsGroup,
       "dellNetBgpM2Rfc2545Group": dellNetBgpM2Rfc2545Group}
)
