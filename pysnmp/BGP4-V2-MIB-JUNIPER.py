# SNMP MIB module (BGP4-V2-MIB-JUNIPER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BGP4-V2-MIB-JUNIPER
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:17 2024
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

(jnxBgpM2Experiment,) = mibBuilder.importSymbols(
    "JUNIPER-EXPERIMENT-MIB",
    "jnxBgpM2Experiment")

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

jnxBgpM2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1)
)
jnxBgpM2.setRevisions(
        ("2012-12-17 00:00",
         "2003-09-09 15:08",
         "2002-11-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxBgpM2Identifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class JnxBgpM2Safi(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class JnxBgpM2Community(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class JnxBgpM2ExtendedCommunity(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_JnxBgpM2BaseScalars_ObjectIdentity = ObjectIdentity
jnxBgpM2BaseScalars = _JnxBgpM2BaseScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1)
)
_JnxBgpM2BaseNotifications_ObjectIdentity = ObjectIdentity
jnxBgpM2BaseNotifications = _JnxBgpM2BaseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 0)
)
_JnxBgpM2Version_ObjectIdentity = ObjectIdentity
jnxBgpM2Version = _JnxBgpM2Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 1)
)
_JnxBgpM2VersionTable_Object = MibTable
jnxBgpM2VersionTable = _JnxBgpM2VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2VersionTable.setStatus("current")
_JnxBgpM2VersionEntry_Object = MibTableRow
jnxBgpM2VersionEntry = _JnxBgpM2VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 1, 1, 1)
)
jnxBgpM2VersionEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2VersionIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2VersionEntry.setStatus("current")


class _JnxBgpM2VersionIndex_Type(Unsigned32):
    """Custom type jnxBgpM2VersionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxBgpM2VersionIndex_Type.__name__ = "Unsigned32"
_JnxBgpM2VersionIndex_Object = MibTableColumn
jnxBgpM2VersionIndex = _JnxBgpM2VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 1, 1, 1, 1),
    _JnxBgpM2VersionIndex_Type()
)
jnxBgpM2VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2VersionIndex.setStatus("current")
_JnxBgpM2VersionSupported_Type = TruthValue
_JnxBgpM2VersionSupported_Object = MibTableColumn
jnxBgpM2VersionSupported = _JnxBgpM2VersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 1, 1, 1, 2),
    _JnxBgpM2VersionSupported_Type()
)
jnxBgpM2VersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2VersionSupported.setStatus("current")
_JnxBgpM2SupportedAuthentication_ObjectIdentity = ObjectIdentity
jnxBgpM2SupportedAuthentication = _JnxBgpM2SupportedAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 2)
)
_JnxBgpM2SupportedAuthTable_Object = MibTable
jnxBgpM2SupportedAuthTable = _JnxBgpM2SupportedAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2SupportedAuthTable.setStatus("current")
_JnxBgpM2SupportedAuthEntry_Object = MibTableRow
jnxBgpM2SupportedAuthEntry = _JnxBgpM2SupportedAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 2, 1, 1)
)
jnxBgpM2SupportedAuthEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2SupportedAuthCode"),
)
if mibBuilder.loadTexts:
    jnxBgpM2SupportedAuthEntry.setStatus("current")


class _JnxBgpM2SupportedAuthCode_Type(Unsigned32):
    """Custom type jnxBgpM2SupportedAuthCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxBgpM2SupportedAuthCode_Type.__name__ = "Unsigned32"
_JnxBgpM2SupportedAuthCode_Object = MibTableColumn
jnxBgpM2SupportedAuthCode = _JnxBgpM2SupportedAuthCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 2, 1, 1, 1),
    _JnxBgpM2SupportedAuthCode_Type()
)
jnxBgpM2SupportedAuthCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2SupportedAuthCode.setStatus("current")
_JnxBgpM2SupportedAuthValue_Type = TruthValue
_JnxBgpM2SupportedAuthValue_Object = MibTableColumn
jnxBgpM2SupportedAuthValue = _JnxBgpM2SupportedAuthValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 2, 1, 1, 2),
    _JnxBgpM2SupportedAuthValue_Type()
)
jnxBgpM2SupportedAuthValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2SupportedAuthValue.setStatus("current")
_JnxBgpM2SupportedCapabilities_ObjectIdentity = ObjectIdentity
jnxBgpM2SupportedCapabilities = _JnxBgpM2SupportedCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 3)
)
_JnxBgpM2CapabilitySupportAvailable_Type = TruthValue
_JnxBgpM2CapabilitySupportAvailable_Object = MibScalar
jnxBgpM2CapabilitySupportAvailable = _JnxBgpM2CapabilitySupportAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 3, 1),
    _JnxBgpM2CapabilitySupportAvailable_Type()
)
jnxBgpM2CapabilitySupportAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2CapabilitySupportAvailable.setStatus("current")
_JnxBgpM2SupportedCapabilitiesTable_Object = MibTable
jnxBgpM2SupportedCapabilitiesTable = _JnxBgpM2SupportedCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxBgpM2SupportedCapabilitiesTable.setStatus("current")
_JnxBgpM2SupportedCapabilitiesEntry_Object = MibTableRow
jnxBgpM2SupportedCapabilitiesEntry = _JnxBgpM2SupportedCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 3, 2, 1)
)
jnxBgpM2SupportedCapabilitiesEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2SupportedCapabilityCode"),
)
if mibBuilder.loadTexts:
    jnxBgpM2SupportedCapabilitiesEntry.setStatus("current")


class _JnxBgpM2SupportedCapabilityCode_Type(Unsigned32):
    """Custom type jnxBgpM2SupportedCapabilityCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxBgpM2SupportedCapabilityCode_Type.__name__ = "Unsigned32"
_JnxBgpM2SupportedCapabilityCode_Object = MibTableColumn
jnxBgpM2SupportedCapabilityCode = _JnxBgpM2SupportedCapabilityCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 3, 2, 1, 1),
    _JnxBgpM2SupportedCapabilityCode_Type()
)
jnxBgpM2SupportedCapabilityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2SupportedCapabilityCode.setStatus("current")
_JnxBgpM2SupportedCapability_Type = TruthValue
_JnxBgpM2SupportedCapability_Object = MibTableColumn
jnxBgpM2SupportedCapability = _JnxBgpM2SupportedCapability_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 3, 2, 1, 2),
    _JnxBgpM2SupportedCapability_Type()
)
jnxBgpM2SupportedCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2SupportedCapability.setStatus("current")


class _JnxBgpM2AsSize_Type(Integer32):
    """Custom type jnxBgpM2AsSize based on Integer32"""
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


_JnxBgpM2AsSize_Type.__name__ = "Integer32"
_JnxBgpM2AsSize_Object = MibScalar
jnxBgpM2AsSize = _JnxBgpM2AsSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 4),
    _JnxBgpM2AsSize_Type()
)
jnxBgpM2AsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsSize.setStatus("current")
_JnxBgpM2LocalAs_Type = InetAutonomousSystemNumber
_JnxBgpM2LocalAs_Object = MibScalar
jnxBgpM2LocalAs = _JnxBgpM2LocalAs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 5),
    _JnxBgpM2LocalAs_Type()
)
jnxBgpM2LocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2LocalAs.setStatus("current")
_JnxBgpM2LocalIdentifier_Type = JnxBgpM2Identifier
_JnxBgpM2LocalIdentifier_Object = MibScalar
jnxBgpM2LocalIdentifier = _JnxBgpM2LocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 6),
    _JnxBgpM2LocalIdentifier_Type()
)
jnxBgpM2LocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2LocalIdentifier.setStatus("current")
_JnxBgpM2BaseScalarExtensions_ObjectIdentity = ObjectIdentity
jnxBgpM2BaseScalarExtensions = _JnxBgpM2BaseScalarExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 7)
)
_JnxBgpM2BaseScalarNonCapExts_ObjectIdentity = ObjectIdentity
jnxBgpM2BaseScalarNonCapExts = _JnxBgpM2BaseScalarNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 7, 1)
)
_JnxBgpM2BaseScalarRouteReflectExts_ObjectIdentity = ObjectIdentity
jnxBgpM2BaseScalarRouteReflectExts = _JnxBgpM2BaseScalarRouteReflectExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 7, 1, 2796)
)
_JnxBgpM2RouteReflector_Type = TruthValue
_JnxBgpM2RouteReflector_Object = MibScalar
jnxBgpM2RouteReflector = _JnxBgpM2RouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 7, 1, 2796, 1),
    _JnxBgpM2RouteReflector_Type()
)
jnxBgpM2RouteReflector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2RouteReflector.setStatus("current")
_JnxBgpM2ClusterId_Type = JnxBgpM2Identifier
_JnxBgpM2ClusterId_Object = MibScalar
jnxBgpM2ClusterId = _JnxBgpM2ClusterId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 7, 1, 2796, 2),
    _JnxBgpM2ClusterId_Type()
)
jnxBgpM2ClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2ClusterId.setStatus("current")
_JnxBgpM2BaseScalarASConfedExts_ObjectIdentity = ObjectIdentity
jnxBgpM2BaseScalarASConfedExts = _JnxBgpM2BaseScalarASConfedExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 7, 1, 3065)
)
_JnxBgpM2ConfederationRouter_Type = TruthValue
_JnxBgpM2ConfederationRouter_Object = MibScalar
jnxBgpM2ConfederationRouter = _JnxBgpM2ConfederationRouter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 7, 1, 3065, 1),
    _JnxBgpM2ConfederationRouter_Type()
)
jnxBgpM2ConfederationRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2ConfederationRouter.setStatus("current")
_JnxBgpM2ConfederationId_Type = InetAutonomousSystemNumber
_JnxBgpM2ConfederationId_Object = MibScalar
jnxBgpM2ConfederationId = _JnxBgpM2ConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 7, 1, 3065, 2),
    _JnxBgpM2ConfederationId_Type()
)
jnxBgpM2ConfederationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2ConfederationId.setStatus("current")
_JnxBgpM2BaseScalarCapExts_ObjectIdentity = ObjectIdentity
jnxBgpM2BaseScalarCapExts = _JnxBgpM2BaseScalarCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 7, 2)
)
_JnxBgpM2BaseScalarConfiguration_ObjectIdentity = ObjectIdentity
jnxBgpM2BaseScalarConfiguration = _JnxBgpM2BaseScalarConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8)
)
_JnxBgpM2CfgBaseScalarStorageType_Type = StorageType
_JnxBgpM2CfgBaseScalarStorageType_Object = MibScalar
jnxBgpM2CfgBaseScalarStorageType = _JnxBgpM2CfgBaseScalarStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 1),
    _JnxBgpM2CfgBaseScalarStorageType_Type()
)
jnxBgpM2CfgBaseScalarStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxBgpM2CfgBaseScalarStorageType.setStatus("current")
_JnxBgpM2CfgLocalAs_Type = InetAutonomousSystemNumber
_JnxBgpM2CfgLocalAs_Object = MibScalar
jnxBgpM2CfgLocalAs = _JnxBgpM2CfgLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 2),
    _JnxBgpM2CfgLocalAs_Type()
)
jnxBgpM2CfgLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxBgpM2CfgLocalAs.setStatus("current")
_JnxBgpM2CfgLocalIdentifier_Type = JnxBgpM2Identifier
_JnxBgpM2CfgLocalIdentifier_Object = MibScalar
jnxBgpM2CfgLocalIdentifier = _JnxBgpM2CfgLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 3),
    _JnxBgpM2CfgLocalIdentifier_Type()
)
jnxBgpM2CfgLocalIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxBgpM2CfgLocalIdentifier.setStatus("current")
_JnxBgpM2CfgBaseScalarExtensions_ObjectIdentity = ObjectIdentity
jnxBgpM2CfgBaseScalarExtensions = _JnxBgpM2CfgBaseScalarExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 4)
)
_JnxBgpM2CfgBaseScalarNonCapExts_ObjectIdentity = ObjectIdentity
jnxBgpM2CfgBaseScalarNonCapExts = _JnxBgpM2CfgBaseScalarNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 4, 1)
)
_JnxBgpM2CfgBaseScalarReflectorExts_ObjectIdentity = ObjectIdentity
jnxBgpM2CfgBaseScalarReflectorExts = _JnxBgpM2CfgBaseScalarReflectorExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 4, 1, 2796)
)
_JnxBgpM2CfgRouteReflector_Type = TruthValue
_JnxBgpM2CfgRouteReflector_Object = MibScalar
jnxBgpM2CfgRouteReflector = _JnxBgpM2CfgRouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 4, 1, 2796, 1),
    _JnxBgpM2CfgRouteReflector_Type()
)
jnxBgpM2CfgRouteReflector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxBgpM2CfgRouteReflector.setStatus("current")
_JnxBgpM2CfgClusterId_Type = JnxBgpM2Identifier
_JnxBgpM2CfgClusterId_Object = MibScalar
jnxBgpM2CfgClusterId = _JnxBgpM2CfgClusterId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 4, 1, 2796, 2),
    _JnxBgpM2CfgClusterId_Type()
)
jnxBgpM2CfgClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxBgpM2CfgClusterId.setStatus("current")
_JnxBgpM2CfgBaseScalarASConfedExts_ObjectIdentity = ObjectIdentity
jnxBgpM2CfgBaseScalarASConfedExts = _JnxBgpM2CfgBaseScalarASConfedExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 4, 1, 3065)
)
_JnxBgpM2CfgConfederationRouter_Type = TruthValue
_JnxBgpM2CfgConfederationRouter_Object = MibScalar
jnxBgpM2CfgConfederationRouter = _JnxBgpM2CfgConfederationRouter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 4, 1, 3065, 1),
    _JnxBgpM2CfgConfederationRouter_Type()
)
jnxBgpM2CfgConfederationRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxBgpM2CfgConfederationRouter.setStatus("current")
_JnxBgpM2CfgConfederationId_Type = InetAutonomousSystemNumber
_JnxBgpM2CfgConfederationId_Object = MibScalar
jnxBgpM2CfgConfederationId = _JnxBgpM2CfgConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 4, 1, 3065, 2),
    _JnxBgpM2CfgConfederationId_Type()
)
jnxBgpM2CfgConfederationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxBgpM2CfgConfederationId.setStatus("current")
_JnxBgpM2CfgBaseScalarCapExts_ObjectIdentity = ObjectIdentity
jnxBgpM2CfgBaseScalarCapExts = _JnxBgpM2CfgBaseScalarCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 8, 4, 2)
)
_JnxBgpM2Peer_ObjectIdentity = ObjectIdentity
jnxBgpM2Peer = _JnxBgpM2Peer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2)
)
_JnxBgpM2PeerData_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerData = _JnxBgpM2PeerData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1)
)
_JnxBgpM2PeerTable_Object = MibTable
jnxBgpM2PeerTable = _JnxBgpM2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerTable.setStatus("current")
_JnxBgpM2PeerEntry_Object = MibTableRow
jnxBgpM2PeerEntry = _JnxBgpM2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1)
)
jnxBgpM2PeerEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRoutingInstance"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLocalAddrType"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLocalAddr"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRemoteAddrType"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerEntry.setStatus("current")
_JnxBgpM2PeerIdentifier_Type = JnxBgpM2Identifier
_JnxBgpM2PeerIdentifier_Object = MibTableColumn
jnxBgpM2PeerIdentifier = _JnxBgpM2PeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 1),
    _JnxBgpM2PeerIdentifier_Type()
)
jnxBgpM2PeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerIdentifier.setStatus("current")


class _JnxBgpM2PeerState_Type(Integer32):
    """Custom type jnxBgpM2PeerState based on Integer32"""
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


_JnxBgpM2PeerState_Type.__name__ = "Integer32"
_JnxBgpM2PeerState_Object = MibTableColumn
jnxBgpM2PeerState = _JnxBgpM2PeerState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 2),
    _JnxBgpM2PeerState_Type()
)
jnxBgpM2PeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerState.setStatus("current")


class _JnxBgpM2PeerStatus_Type(Integer32):
    """Custom type jnxBgpM2PeerStatus based on Integer32"""
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


_JnxBgpM2PeerStatus_Type.__name__ = "Integer32"
_JnxBgpM2PeerStatus_Object = MibTableColumn
jnxBgpM2PeerStatus = _JnxBgpM2PeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 3),
    _JnxBgpM2PeerStatus_Type()
)
jnxBgpM2PeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerStatus.setStatus("current")


class _JnxBgpM2PeerConfiguredVersion_Type(Unsigned32):
    """Custom type jnxBgpM2PeerConfiguredVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JnxBgpM2PeerConfiguredVersion_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerConfiguredVersion_Object = MibTableColumn
jnxBgpM2PeerConfiguredVersion = _JnxBgpM2PeerConfiguredVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 4),
    _JnxBgpM2PeerConfiguredVersion_Type()
)
jnxBgpM2PeerConfiguredVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerConfiguredVersion.setStatus("current")


class _JnxBgpM2PeerNegotiatedVersion_Type(Unsigned32):
    """Custom type jnxBgpM2PeerNegotiatedVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JnxBgpM2PeerNegotiatedVersion_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerNegotiatedVersion_Object = MibTableColumn
jnxBgpM2PeerNegotiatedVersion = _JnxBgpM2PeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 5),
    _JnxBgpM2PeerNegotiatedVersion_Type()
)
jnxBgpM2PeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerNegotiatedVersion.setStatus("current")
_JnxBgpM2PeerLocalAddrType_Type = InetAddressType
_JnxBgpM2PeerLocalAddrType_Object = MibTableColumn
jnxBgpM2PeerLocalAddrType = _JnxBgpM2PeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 6),
    _JnxBgpM2PeerLocalAddrType_Type()
)
jnxBgpM2PeerLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLocalAddrType.setStatus("current")


class _JnxBgpM2PeerLocalAddr_Type(InetAddress):
    """Custom type jnxBgpM2PeerLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_JnxBgpM2PeerLocalAddr_Type.__name__ = "InetAddress"
_JnxBgpM2PeerLocalAddr_Object = MibTableColumn
jnxBgpM2PeerLocalAddr = _JnxBgpM2PeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 7),
    _JnxBgpM2PeerLocalAddr_Type()
)
jnxBgpM2PeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLocalAddr.setStatus("current")
_JnxBgpM2PeerLocalPort_Type = InetPortNumber
_JnxBgpM2PeerLocalPort_Object = MibTableColumn
jnxBgpM2PeerLocalPort = _JnxBgpM2PeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 8),
    _JnxBgpM2PeerLocalPort_Type()
)
jnxBgpM2PeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLocalPort.setStatus("current")
_JnxBgpM2PeerLocalAs_Type = InetAutonomousSystemNumber
_JnxBgpM2PeerLocalAs_Object = MibTableColumn
jnxBgpM2PeerLocalAs = _JnxBgpM2PeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 9),
    _JnxBgpM2PeerLocalAs_Type()
)
jnxBgpM2PeerLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLocalAs.setStatus("current")
_JnxBgpM2PeerRemoteAddrType_Type = InetAddressType
_JnxBgpM2PeerRemoteAddrType_Object = MibTableColumn
jnxBgpM2PeerRemoteAddrType = _JnxBgpM2PeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 10),
    _JnxBgpM2PeerRemoteAddrType_Type()
)
jnxBgpM2PeerRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerRemoteAddrType.setStatus("current")


class _JnxBgpM2PeerRemoteAddr_Type(InetAddress):
    """Custom type jnxBgpM2PeerRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_JnxBgpM2PeerRemoteAddr_Type.__name__ = "InetAddress"
_JnxBgpM2PeerRemoteAddr_Object = MibTableColumn
jnxBgpM2PeerRemoteAddr = _JnxBgpM2PeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 11),
    _JnxBgpM2PeerRemoteAddr_Type()
)
jnxBgpM2PeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerRemoteAddr.setStatus("current")
_JnxBgpM2PeerRemotePort_Type = InetPortNumber
_JnxBgpM2PeerRemotePort_Object = MibTableColumn
jnxBgpM2PeerRemotePort = _JnxBgpM2PeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 12),
    _JnxBgpM2PeerRemotePort_Type()
)
jnxBgpM2PeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerRemotePort.setStatus("current")
_JnxBgpM2PeerRemoteAs_Type = InetAutonomousSystemNumber
_JnxBgpM2PeerRemoteAs_Object = MibTableColumn
jnxBgpM2PeerRemoteAs = _JnxBgpM2PeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 13),
    _JnxBgpM2PeerRemoteAs_Type()
)
jnxBgpM2PeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerRemoteAs.setStatus("current")
_JnxBgpM2PeerIndex_Type = Unsigned32
_JnxBgpM2PeerIndex_Object = MibTableColumn
jnxBgpM2PeerIndex = _JnxBgpM2PeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 14),
    _JnxBgpM2PeerIndex_Type()
)
jnxBgpM2PeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerIndex.setStatus("current")
_JnxBgpM2PeerRoutingInstance_Type = Unsigned32
_JnxBgpM2PeerRoutingInstance_Object = MibTableColumn
jnxBgpM2PeerRoutingInstance = _JnxBgpM2PeerRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 1, 1, 1, 15),
    _JnxBgpM2PeerRoutingInstance_Type()
)
jnxBgpM2PeerRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerRoutingInstance.setStatus("current")
_JnxBgpM2PeerErrors_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerErrors = _JnxBgpM2PeerErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2)
)
_JnxBgpM2PeerErrorsTable_Object = MibTable
jnxBgpM2PeerErrorsTable = _JnxBgpM2PeerErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerErrorsTable.setStatus("current")
_JnxBgpM2PeerErrorsEntry_Object = MibTableRow
jnxBgpM2PeerErrorsEntry = _JnxBgpM2PeerErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerErrorsEntry.setStatus("current")


class _JnxBgpM2PeerLastErrorReceived_Type(OctetString):
    """Custom type jnxBgpM2PeerLastErrorReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_JnxBgpM2PeerLastErrorReceived_Type.__name__ = "OctetString"
_JnxBgpM2PeerLastErrorReceived_Object = MibTableColumn
jnxBgpM2PeerLastErrorReceived = _JnxBgpM2PeerLastErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2, 1, 1, 1),
    _JnxBgpM2PeerLastErrorReceived_Type()
)
jnxBgpM2PeerLastErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLastErrorReceived.setStatus("current")


class _JnxBgpM2PeerLastErrorSent_Type(OctetString):
    """Custom type jnxBgpM2PeerLastErrorSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_JnxBgpM2PeerLastErrorSent_Type.__name__ = "OctetString"
_JnxBgpM2PeerLastErrorSent_Object = MibTableColumn
jnxBgpM2PeerLastErrorSent = _JnxBgpM2PeerLastErrorSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2, 1, 1, 2),
    _JnxBgpM2PeerLastErrorSent_Type()
)
jnxBgpM2PeerLastErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLastErrorSent.setStatus("current")
_JnxBgpM2PeerLastErrorReceivedTime_Type = TimeTicks
_JnxBgpM2PeerLastErrorReceivedTime_Object = MibTableColumn
jnxBgpM2PeerLastErrorReceivedTime = _JnxBgpM2PeerLastErrorReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2, 1, 1, 3),
    _JnxBgpM2PeerLastErrorReceivedTime_Type()
)
jnxBgpM2PeerLastErrorReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLastErrorReceivedTime.setStatus("current")
_JnxBgpM2PeerLastErrorSentTime_Type = TimeTicks
_JnxBgpM2PeerLastErrorSentTime_Object = MibTableColumn
jnxBgpM2PeerLastErrorSentTime = _JnxBgpM2PeerLastErrorSentTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2, 1, 1, 4),
    _JnxBgpM2PeerLastErrorSentTime_Type()
)
jnxBgpM2PeerLastErrorSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLastErrorSentTime.setStatus("current")
_JnxBgpM2PeerLastErrorReceivedText_Type = SnmpAdminString
_JnxBgpM2PeerLastErrorReceivedText_Object = MibTableColumn
jnxBgpM2PeerLastErrorReceivedText = _JnxBgpM2PeerLastErrorReceivedText_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2, 1, 1, 5),
    _JnxBgpM2PeerLastErrorReceivedText_Type()
)
jnxBgpM2PeerLastErrorReceivedText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLastErrorReceivedText.setStatus("current")
_JnxBgpM2PeerLastErrorSentText_Type = SnmpAdminString
_JnxBgpM2PeerLastErrorSentText_Object = MibTableColumn
jnxBgpM2PeerLastErrorSentText = _JnxBgpM2PeerLastErrorSentText_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2, 1, 1, 6),
    _JnxBgpM2PeerLastErrorSentText_Type()
)
jnxBgpM2PeerLastErrorSentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLastErrorSentText.setStatus("current")


class _JnxBgpM2PeerLastErrorReceivedData_Type(OctetString):
    """Custom type jnxBgpM2PeerLastErrorReceivedData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_JnxBgpM2PeerLastErrorReceivedData_Type.__name__ = "OctetString"
_JnxBgpM2PeerLastErrorReceivedData_Object = MibTableColumn
jnxBgpM2PeerLastErrorReceivedData = _JnxBgpM2PeerLastErrorReceivedData_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2, 1, 1, 7),
    _JnxBgpM2PeerLastErrorReceivedData_Type()
)
jnxBgpM2PeerLastErrorReceivedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLastErrorReceivedData.setStatus("current")


class _JnxBgpM2PeerLastErrorSentData_Type(OctetString):
    """Custom type jnxBgpM2PeerLastErrorSentData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_JnxBgpM2PeerLastErrorSentData_Type.__name__ = "OctetString"
_JnxBgpM2PeerLastErrorSentData_Object = MibTableColumn
jnxBgpM2PeerLastErrorSentData = _JnxBgpM2PeerLastErrorSentData_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 2, 1, 1, 8),
    _JnxBgpM2PeerLastErrorSentData_Type()
)
jnxBgpM2PeerLastErrorSentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerLastErrorSentData.setStatus("current")
_JnxBgpM2PeerAuthentication_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerAuthentication = _JnxBgpM2PeerAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 3)
)
_JnxBgpM2PeerAuthTable_Object = MibTable
jnxBgpM2PeerAuthTable = _JnxBgpM2PeerAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerAuthTable.setStatus("current")
_JnxBgpM2PeerAuthEntry_Object = MibTableRow
jnxBgpM2PeerAuthEntry = _JnxBgpM2PeerAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerAuthEntry.setStatus("current")
_JnxBgpM2PeerAuthSent_Type = TruthValue
_JnxBgpM2PeerAuthSent_Object = MibTableColumn
jnxBgpM2PeerAuthSent = _JnxBgpM2PeerAuthSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 3, 1, 1, 1),
    _JnxBgpM2PeerAuthSent_Type()
)
jnxBgpM2PeerAuthSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerAuthSent.setStatus("current")


class _JnxBgpM2PeerAuthSentCode_Type(Unsigned32):
    """Custom type jnxBgpM2PeerAuthSentCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxBgpM2PeerAuthSentCode_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerAuthSentCode_Object = MibTableColumn
jnxBgpM2PeerAuthSentCode = _JnxBgpM2PeerAuthSentCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 3, 1, 1, 2),
    _JnxBgpM2PeerAuthSentCode_Type()
)
jnxBgpM2PeerAuthSentCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerAuthSentCode.setStatus("current")


class _JnxBgpM2PeerAuthSentValue_Type(OctetString):
    """Custom type jnxBgpM2PeerAuthSentValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_JnxBgpM2PeerAuthSentValue_Type.__name__ = "OctetString"
_JnxBgpM2PeerAuthSentValue_Object = MibTableColumn
jnxBgpM2PeerAuthSentValue = _JnxBgpM2PeerAuthSentValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 3, 1, 1, 3),
    _JnxBgpM2PeerAuthSentValue_Type()
)
jnxBgpM2PeerAuthSentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerAuthSentValue.setStatus("current")
_JnxBgpM2PeerAuthRcvd_Type = TruthValue
_JnxBgpM2PeerAuthRcvd_Object = MibTableColumn
jnxBgpM2PeerAuthRcvd = _JnxBgpM2PeerAuthRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 3, 1, 1, 4),
    _JnxBgpM2PeerAuthRcvd_Type()
)
jnxBgpM2PeerAuthRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerAuthRcvd.setStatus("current")


class _JnxBgpM2PeerAuthRcvdCode_Type(Unsigned32):
    """Custom type jnxBgpM2PeerAuthRcvdCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxBgpM2PeerAuthRcvdCode_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerAuthRcvdCode_Object = MibTableColumn
jnxBgpM2PeerAuthRcvdCode = _JnxBgpM2PeerAuthRcvdCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 3, 1, 1, 5),
    _JnxBgpM2PeerAuthRcvdCode_Type()
)
jnxBgpM2PeerAuthRcvdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerAuthRcvdCode.setStatus("current")


class _JnxBgpM2PeerAuthRcvdValue_Type(OctetString):
    """Custom type jnxBgpM2PeerAuthRcvdValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_JnxBgpM2PeerAuthRcvdValue_Type.__name__ = "OctetString"
_JnxBgpM2PeerAuthRcvdValue_Object = MibTableColumn
jnxBgpM2PeerAuthRcvdValue = _JnxBgpM2PeerAuthRcvdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 3, 1, 1, 6),
    _JnxBgpM2PeerAuthRcvdValue_Type()
)
jnxBgpM2PeerAuthRcvdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerAuthRcvdValue.setStatus("current")
_JnxBgpM2PeerTimers_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerTimers = _JnxBgpM2PeerTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4)
)
_JnxBgpM2PeerEventTimesTable_Object = MibTable
jnxBgpM2PeerEventTimesTable = _JnxBgpM2PeerEventTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerEventTimesTable.setStatus("current")
_JnxBgpM2PeerEventTimesEntry_Object = MibTableRow
jnxBgpM2PeerEventTimesEntry = _JnxBgpM2PeerEventTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerEventTimesEntry.setStatus("current")
_JnxBgpM2PeerFsmEstablishedTime_Type = Gauge32
_JnxBgpM2PeerFsmEstablishedTime_Object = MibTableColumn
jnxBgpM2PeerFsmEstablishedTime = _JnxBgpM2PeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 1, 1, 1),
    _JnxBgpM2PeerFsmEstablishedTime_Type()
)
jnxBgpM2PeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerFsmEstablishedTime.setStatus("current")
_JnxBgpM2PeerInUpdatesElapsedTime_Type = Gauge32
_JnxBgpM2PeerInUpdatesElapsedTime_Object = MibTableColumn
jnxBgpM2PeerInUpdatesElapsedTime = _JnxBgpM2PeerInUpdatesElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 1, 1, 2),
    _JnxBgpM2PeerInUpdatesElapsedTime_Type()
)
jnxBgpM2PeerInUpdatesElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerInUpdatesElapsedTime.setStatus("current")
_JnxBgpM2PeerConfiguredTimersTable_Object = MibTable
jnxBgpM2PeerConfiguredTimersTable = _JnxBgpM2PeerConfiguredTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerConfiguredTimersTable.setStatus("current")
_JnxBgpM2PeerConfiguredTimersEntry_Object = MibTableRow
jnxBgpM2PeerConfiguredTimersEntry = _JnxBgpM2PeerConfiguredTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerConfiguredTimersEntry.setStatus("current")


class _JnxBgpM2PeerConnectRetryInterval_Type(Unsigned32):
    """Custom type jnxBgpM2PeerConnectRetryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxBgpM2PeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerConnectRetryInterval_Object = MibTableColumn
jnxBgpM2PeerConnectRetryInterval = _JnxBgpM2PeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 2, 1, 1),
    _JnxBgpM2PeerConnectRetryInterval_Type()
)
jnxBgpM2PeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerConnectRetryInterval.setStatus("current")


class _JnxBgpM2PeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type jnxBgpM2PeerHoldTimeConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_JnxBgpM2PeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerHoldTimeConfigured_Object = MibTableColumn
jnxBgpM2PeerHoldTimeConfigured = _JnxBgpM2PeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 2, 1, 2),
    _JnxBgpM2PeerHoldTimeConfigured_Type()
)
jnxBgpM2PeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerHoldTimeConfigured.setStatus("current")


class _JnxBgpM2PeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type jnxBgpM2PeerKeepAliveConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_JnxBgpM2PeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerKeepAliveConfigured_Object = MibTableColumn
jnxBgpM2PeerKeepAliveConfigured = _JnxBgpM2PeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 2, 1, 3),
    _JnxBgpM2PeerKeepAliveConfigured_Type()
)
jnxBgpM2PeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerKeepAliveConfigured.setStatus("current")


class _JnxBgpM2PeerMinASOrigInterval_Type(Unsigned32):
    """Custom type jnxBgpM2PeerMinASOrigInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxBgpM2PeerMinASOrigInterval_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerMinASOrigInterval_Object = MibTableColumn
jnxBgpM2PeerMinASOrigInterval = _JnxBgpM2PeerMinASOrigInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 2, 1, 4),
    _JnxBgpM2PeerMinASOrigInterval_Type()
)
jnxBgpM2PeerMinASOrigInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerMinASOrigInterval.setStatus("current")


class _JnxBgpM2PeerMinRouteAdverInterval_Type(Unsigned32):
    """Custom type jnxBgpM2PeerMinRouteAdverInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxBgpM2PeerMinRouteAdverInterval_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerMinRouteAdverInterval_Object = MibTableColumn
jnxBgpM2PeerMinRouteAdverInterval = _JnxBgpM2PeerMinRouteAdverInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 2, 1, 5),
    _JnxBgpM2PeerMinRouteAdverInterval_Type()
)
jnxBgpM2PeerMinRouteAdverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerMinRouteAdverInterval.setStatus("current")
_JnxBgpM2PeerNegotiatedTimersTable_Object = MibTable
jnxBgpM2PeerNegotiatedTimersTable = _JnxBgpM2PeerNegotiatedTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerNegotiatedTimersTable.setStatus("current")
_JnxBgpM2PeerNegotiatedTimersEntry_Object = MibTableRow
jnxBgpM2PeerNegotiatedTimersEntry = _JnxBgpM2PeerNegotiatedTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerNegotiatedTimersEntry.setStatus("current")


class _JnxBgpM2PeerHoldTime_Type(Unsigned32):
    """Custom type jnxBgpM2PeerHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_JnxBgpM2PeerHoldTime_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerHoldTime_Object = MibTableColumn
jnxBgpM2PeerHoldTime = _JnxBgpM2PeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 3, 1, 1),
    _JnxBgpM2PeerHoldTime_Type()
)
jnxBgpM2PeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerHoldTime.setStatus("current")


class _JnxBgpM2PeerKeepAlive_Type(Unsigned32):
    """Custom type jnxBgpM2PeerKeepAlive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_JnxBgpM2PeerKeepAlive_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerKeepAlive_Object = MibTableColumn
jnxBgpM2PeerKeepAlive = _JnxBgpM2PeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 4, 3, 1, 2),
    _JnxBgpM2PeerKeepAlive_Type()
)
jnxBgpM2PeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerKeepAlive.setStatus("current")
_JnxBgpM2PeerCapabilities_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerCapabilities = _JnxBgpM2PeerCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5)
)
_JnxBgpM2PeerCapsAnnouncedTable_Object = MibTable
jnxBgpM2PeerCapsAnnouncedTable = _JnxBgpM2PeerCapsAnnouncedTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerCapsAnnouncedTable.setStatus("current")
_JnxBgpM2PeerCapsAnnouncedEntry_Object = MibTableRow
jnxBgpM2PeerCapsAnnouncedEntry = _JnxBgpM2PeerCapsAnnouncedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5, 1, 1)
)
jnxBgpM2PeerCapsAnnouncedEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerCapAnnouncedCode"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerCapAnnouncedIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerCapsAnnouncedEntry.setStatus("current")


class _JnxBgpM2PeerCapAnnouncedCode_Type(Unsigned32):
    """Custom type jnxBgpM2PeerCapAnnouncedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxBgpM2PeerCapAnnouncedCode_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerCapAnnouncedCode_Object = MibTableColumn
jnxBgpM2PeerCapAnnouncedCode = _JnxBgpM2PeerCapAnnouncedCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5, 1, 1, 1),
    _JnxBgpM2PeerCapAnnouncedCode_Type()
)
jnxBgpM2PeerCapAnnouncedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerCapAnnouncedCode.setStatus("current")


class _JnxBgpM2PeerCapAnnouncedIndex_Type(Unsigned32):
    """Custom type jnxBgpM2PeerCapAnnouncedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_JnxBgpM2PeerCapAnnouncedIndex_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerCapAnnouncedIndex_Object = MibTableColumn
jnxBgpM2PeerCapAnnouncedIndex = _JnxBgpM2PeerCapAnnouncedIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5, 1, 1, 2),
    _JnxBgpM2PeerCapAnnouncedIndex_Type()
)
jnxBgpM2PeerCapAnnouncedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerCapAnnouncedIndex.setStatus("current")


class _JnxBgpM2PeerCapAnnouncedValue_Type(OctetString):
    """Custom type jnxBgpM2PeerCapAnnouncedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxBgpM2PeerCapAnnouncedValue_Type.__name__ = "OctetString"
_JnxBgpM2PeerCapAnnouncedValue_Object = MibTableColumn
jnxBgpM2PeerCapAnnouncedValue = _JnxBgpM2PeerCapAnnouncedValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5, 1, 1, 3),
    _JnxBgpM2PeerCapAnnouncedValue_Type()
)
jnxBgpM2PeerCapAnnouncedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerCapAnnouncedValue.setStatus("current")
_JnxBgpM2PeerCapsReceivedTable_Object = MibTable
jnxBgpM2PeerCapsReceivedTable = _JnxBgpM2PeerCapsReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerCapsReceivedTable.setStatus("current")
_JnxBgpM2PeerCapsReceivedEntry_Object = MibTableRow
jnxBgpM2PeerCapsReceivedEntry = _JnxBgpM2PeerCapsReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5, 2, 1)
)
jnxBgpM2PeerCapsReceivedEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerCapReceivedCode"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerCapReceivedIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerCapsReceivedEntry.setStatus("current")


class _JnxBgpM2PeerCapReceivedCode_Type(Unsigned32):
    """Custom type jnxBgpM2PeerCapReceivedCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxBgpM2PeerCapReceivedCode_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerCapReceivedCode_Object = MibTableColumn
jnxBgpM2PeerCapReceivedCode = _JnxBgpM2PeerCapReceivedCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5, 2, 1, 1),
    _JnxBgpM2PeerCapReceivedCode_Type()
)
jnxBgpM2PeerCapReceivedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerCapReceivedCode.setStatus("current")


class _JnxBgpM2PeerCapReceivedIndex_Type(Unsigned32):
    """Custom type jnxBgpM2PeerCapReceivedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_JnxBgpM2PeerCapReceivedIndex_Type.__name__ = "Unsigned32"
_JnxBgpM2PeerCapReceivedIndex_Object = MibTableColumn
jnxBgpM2PeerCapReceivedIndex = _JnxBgpM2PeerCapReceivedIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5, 2, 1, 2),
    _JnxBgpM2PeerCapReceivedIndex_Type()
)
jnxBgpM2PeerCapReceivedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerCapReceivedIndex.setStatus("current")


class _JnxBgpM2PeerCapReceivedValue_Type(OctetString):
    """Custom type jnxBgpM2PeerCapReceivedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxBgpM2PeerCapReceivedValue_Type.__name__ = "OctetString"
_JnxBgpM2PeerCapReceivedValue_Object = MibTableColumn
jnxBgpM2PeerCapReceivedValue = _JnxBgpM2PeerCapReceivedValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 5, 2, 1, 3),
    _JnxBgpM2PeerCapReceivedValue_Type()
)
jnxBgpM2PeerCapReceivedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerCapReceivedValue.setStatus("current")
_JnxBgpM2PeerCounters_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerCounters = _JnxBgpM2PeerCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6)
)
_JnxBgpM2PeerCountersTable_Object = MibTable
jnxBgpM2PeerCountersTable = _JnxBgpM2PeerCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerCountersTable.setStatus("current")
_JnxBgpM2PeerCountersEntry_Object = MibTableRow
jnxBgpM2PeerCountersEntry = _JnxBgpM2PeerCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerCountersEntry.setStatus("current")
_JnxBgpM2PeerInUpdates_Type = Counter32
_JnxBgpM2PeerInUpdates_Object = MibTableColumn
jnxBgpM2PeerInUpdates = _JnxBgpM2PeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 1, 1, 1),
    _JnxBgpM2PeerInUpdates_Type()
)
jnxBgpM2PeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerInUpdates.setStatus("current")
_JnxBgpM2PeerOutUpdates_Type = Counter32
_JnxBgpM2PeerOutUpdates_Object = MibTableColumn
jnxBgpM2PeerOutUpdates = _JnxBgpM2PeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 1, 1, 2),
    _JnxBgpM2PeerOutUpdates_Type()
)
jnxBgpM2PeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerOutUpdates.setStatus("current")
_JnxBgpM2PeerInTotalMessages_Type = Counter32
_JnxBgpM2PeerInTotalMessages_Object = MibTableColumn
jnxBgpM2PeerInTotalMessages = _JnxBgpM2PeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 1, 1, 3),
    _JnxBgpM2PeerInTotalMessages_Type()
)
jnxBgpM2PeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerInTotalMessages.setStatus("current")
_JnxBgpM2PeerOutTotalMessages_Type = Counter32
_JnxBgpM2PeerOutTotalMessages_Object = MibTableColumn
jnxBgpM2PeerOutTotalMessages = _JnxBgpM2PeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 1, 1, 4),
    _JnxBgpM2PeerOutTotalMessages_Type()
)
jnxBgpM2PeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerOutTotalMessages.setStatus("current")
_JnxBgpM2PeerFsmEstablishedTrans_Type = Counter32
_JnxBgpM2PeerFsmEstablishedTrans_Object = MibTableColumn
jnxBgpM2PeerFsmEstablishedTrans = _JnxBgpM2PeerFsmEstablishedTrans_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 1, 1, 5),
    _JnxBgpM2PeerFsmEstablishedTrans_Type()
)
jnxBgpM2PeerFsmEstablishedTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerFsmEstablishedTrans.setStatus("current")
_JnxBgpM2PrefixCountersTable_Object = MibTable
jnxBgpM2PrefixCountersTable = _JnxBgpM2PrefixCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    jnxBgpM2PrefixCountersTable.setStatus("current")
_JnxBgpM2PrefixCountersEntry_Object = MibTableRow
jnxBgpM2PrefixCountersEntry = _JnxBgpM2PrefixCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 2, 1)
)
jnxBgpM2PrefixCountersEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PrefixCountersAfi"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PrefixCountersSafi"),
)
if mibBuilder.loadTexts:
    jnxBgpM2PrefixCountersEntry.setStatus("current")
_JnxBgpM2PrefixCountersAfi_Type = InetAddressType
_JnxBgpM2PrefixCountersAfi_Object = MibTableColumn
jnxBgpM2PrefixCountersAfi = _JnxBgpM2PrefixCountersAfi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 2, 1, 1),
    _JnxBgpM2PrefixCountersAfi_Type()
)
jnxBgpM2PrefixCountersAfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PrefixCountersAfi.setStatus("current")
_JnxBgpM2PrefixCountersSafi_Type = JnxBgpM2Safi
_JnxBgpM2PrefixCountersSafi_Object = MibTableColumn
jnxBgpM2PrefixCountersSafi = _JnxBgpM2PrefixCountersSafi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 2, 1, 2),
    _JnxBgpM2PrefixCountersSafi_Type()
)
jnxBgpM2PrefixCountersSafi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PrefixCountersSafi.setStatus("current")
_JnxBgpM2PrefixInPrefixes_Type = Gauge32
_JnxBgpM2PrefixInPrefixes_Object = MibTableColumn
jnxBgpM2PrefixInPrefixes = _JnxBgpM2PrefixInPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 2, 1, 7),
    _JnxBgpM2PrefixInPrefixes_Type()
)
jnxBgpM2PrefixInPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PrefixInPrefixes.setStatus("current")
_JnxBgpM2PrefixInPrefixesAccepted_Type = Gauge32
_JnxBgpM2PrefixInPrefixesAccepted_Object = MibTableColumn
jnxBgpM2PrefixInPrefixesAccepted = _JnxBgpM2PrefixInPrefixesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 2, 1, 8),
    _JnxBgpM2PrefixInPrefixesAccepted_Type()
)
jnxBgpM2PrefixInPrefixesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PrefixInPrefixesAccepted.setStatus("current")
_JnxBgpM2PrefixInPrefixesRejected_Type = Gauge32
_JnxBgpM2PrefixInPrefixesRejected_Object = MibTableColumn
jnxBgpM2PrefixInPrefixesRejected = _JnxBgpM2PrefixInPrefixesRejected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 2, 1, 9),
    _JnxBgpM2PrefixInPrefixesRejected_Type()
)
jnxBgpM2PrefixInPrefixesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PrefixInPrefixesRejected.setStatus("current")
_JnxBgpM2PrefixOutPrefixes_Type = Gauge32
_JnxBgpM2PrefixOutPrefixes_Object = MibTableColumn
jnxBgpM2PrefixOutPrefixes = _JnxBgpM2PrefixOutPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 2, 1, 10),
    _JnxBgpM2PrefixOutPrefixes_Type()
)
jnxBgpM2PrefixOutPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PrefixOutPrefixes.setStatus("current")
_JnxBgpM2PrefixInPrefixesActive_Type = Gauge32
_JnxBgpM2PrefixInPrefixesActive_Object = MibTableColumn
jnxBgpM2PrefixInPrefixesActive = _JnxBgpM2PrefixInPrefixesActive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 6, 2, 1, 11),
    _JnxBgpM2PrefixInPrefixesActive_Type()
)
jnxBgpM2PrefixInPrefixesActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PrefixInPrefixesActive.setStatus("current")
_JnxBgpM2PeerExtensions_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerExtensions = _JnxBgpM2PeerExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7)
)
_JnxBgpM2PeerNonCapExts_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerNonCapExts = _JnxBgpM2PeerNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7, 1)
)
_JnxBgpM2PeerRouteReflectionExts_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerRouteReflectionExts = _JnxBgpM2PeerRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7, 1, 2796)
)
_JnxBgpM2PeerReflectorClientTable_Object = MibTable
jnxBgpM2PeerReflectorClientTable = _JnxBgpM2PeerReflectorClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7, 1, 2796, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerReflectorClientTable.setStatus("current")
_JnxBgpM2PeerReflectorClientEntry_Object = MibTableRow
jnxBgpM2PeerReflectorClientEntry = _JnxBgpM2PeerReflectorClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7, 1, 2796, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerReflectorClientEntry.setStatus("current")


class _JnxBgpM2PeerReflectorClient_Type(Integer32):
    """Custom type jnxBgpM2PeerReflectorClient based on Integer32"""
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


_JnxBgpM2PeerReflectorClient_Type.__name__ = "Integer32"
_JnxBgpM2PeerReflectorClient_Object = MibTableColumn
jnxBgpM2PeerReflectorClient = _JnxBgpM2PeerReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7, 1, 2796, 1, 1, 1),
    _JnxBgpM2PeerReflectorClient_Type()
)
jnxBgpM2PeerReflectorClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerReflectorClient.setStatus("current")
_JnxBgpM2PeerASConfederationExts_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerASConfederationExts = _JnxBgpM2PeerASConfederationExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7, 1, 3065)
)
_JnxBgpM2PeerConfedMemberTable_Object = MibTable
jnxBgpM2PeerConfedMemberTable = _JnxBgpM2PeerConfedMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7, 1, 3065, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerConfedMemberTable.setStatus("current")
_JnxBgpM2PeerConfedMemberEntry_Object = MibTableRow
jnxBgpM2PeerConfedMemberEntry = _JnxBgpM2PeerConfedMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7, 1, 3065, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerConfedMemberEntry.setStatus("current")
_JnxBgpM2PeerConfedMember_Type = TruthValue
_JnxBgpM2PeerConfedMember_Object = MibTableColumn
jnxBgpM2PeerConfedMember = _JnxBgpM2PeerConfedMember_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7, 1, 3065, 1, 1, 1),
    _JnxBgpM2PeerConfedMember_Type()
)
jnxBgpM2PeerConfedMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PeerConfedMember.setStatus("current")
_JnxBgpM2PeerCapExts_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerCapExts = _JnxBgpM2PeerCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 7, 2)
)
_JnxBgpM2PeerConfiguration_ObjectIdentity = ObjectIdentity
jnxBgpM2PeerConfiguration = _JnxBgpM2PeerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8)
)
_JnxBgpM2CfgPeerAdminStatusTable_Object = MibTable
jnxBgpM2CfgPeerAdminStatusTable = _JnxBgpM2CfgPeerAdminStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerAdminStatusTable.setStatus("current")
_JnxBgpM2CfgPeerAdminStatusEntry_Object = MibTableRow
jnxBgpM2CfgPeerAdminStatusEntry = _JnxBgpM2CfgPeerAdminStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 1, 1)
)
jnxBgpM2CfgPeerAdminStatusEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerAdminStatusEntry.setStatus("current")


class _JnxBgpM2CfgPeerAdminStatus_Type(Integer32):
    """Custom type jnxBgpM2CfgPeerAdminStatus based on Integer32"""
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


_JnxBgpM2CfgPeerAdminStatus_Type.__name__ = "Integer32"
_JnxBgpM2CfgPeerAdminStatus_Object = MibTableColumn
jnxBgpM2CfgPeerAdminStatus = _JnxBgpM2CfgPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 1, 1, 1),
    _JnxBgpM2CfgPeerAdminStatus_Type()
)
jnxBgpM2CfgPeerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerAdminStatus.setStatus("current")


class _JnxBgpM2CfgPeerNextIndex_Type(Integer32):
    """Custom type jnxBgpM2CfgPeerNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxBgpM2CfgPeerNextIndex_Type.__name__ = "Integer32"
_JnxBgpM2CfgPeerNextIndex_Object = MibScalar
jnxBgpM2CfgPeerNextIndex = _JnxBgpM2CfgPeerNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 2),
    _JnxBgpM2CfgPeerNextIndex_Type()
)
jnxBgpM2CfgPeerNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerNextIndex.setStatus("current")
_JnxBgpM2CfgPeerTable_Object = MibTable
jnxBgpM2CfgPeerTable = _JnxBgpM2CfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerTable.setStatus("current")
_JnxBgpM2CfgPeerEntry_Object = MibTableRow
jnxBgpM2CfgPeerEntry = _JnxBgpM2CfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1)
)
jnxBgpM2CfgPeerEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerEntry.setStatus("current")


class _JnxBgpM2CfgPeerConfiguredVersion_Type(Unsigned32):
    """Custom type jnxBgpM2CfgPeerConfiguredVersion based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JnxBgpM2CfgPeerConfiguredVersion_Type.__name__ = "Unsigned32"
_JnxBgpM2CfgPeerConfiguredVersion_Object = MibTableColumn
jnxBgpM2CfgPeerConfiguredVersion = _JnxBgpM2CfgPeerConfiguredVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 1),
    _JnxBgpM2CfgPeerConfiguredVersion_Type()
)
jnxBgpM2CfgPeerConfiguredVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerConfiguredVersion.setStatus("current")


class _JnxBgpM2CfgAllowVersionNegotiation_Type(TruthValue):
    """Custom type jnxBgpM2CfgAllowVersionNegotiation based on TruthValue"""


_JnxBgpM2CfgAllowVersionNegotiation_Object = MibTableColumn
jnxBgpM2CfgAllowVersionNegotiation = _JnxBgpM2CfgAllowVersionNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 2),
    _JnxBgpM2CfgAllowVersionNegotiation_Type()
)
jnxBgpM2CfgAllowVersionNegotiation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgAllowVersionNegotiation.setStatus("current")
_JnxBgpM2CfgPeerLocalAddrType_Type = InetAddressType
_JnxBgpM2CfgPeerLocalAddrType_Object = MibTableColumn
jnxBgpM2CfgPeerLocalAddrType = _JnxBgpM2CfgPeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 3),
    _JnxBgpM2CfgPeerLocalAddrType_Type()
)
jnxBgpM2CfgPeerLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerLocalAddrType.setStatus("current")


class _JnxBgpM2CfgPeerLocalAddr_Type(InetAddress):
    """Custom type jnxBgpM2CfgPeerLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_JnxBgpM2CfgPeerLocalAddr_Type.__name__ = "InetAddress"
_JnxBgpM2CfgPeerLocalAddr_Object = MibTableColumn
jnxBgpM2CfgPeerLocalAddr = _JnxBgpM2CfgPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 4),
    _JnxBgpM2CfgPeerLocalAddr_Type()
)
jnxBgpM2CfgPeerLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerLocalAddr.setStatus("current")


class _JnxBgpM2CfgPeerLocalAs_Type(InetAutonomousSystemNumber):
    """Custom type jnxBgpM2CfgPeerLocalAs based on InetAutonomousSystemNumber"""
    defaultValue = 0


_JnxBgpM2CfgPeerLocalAs_Object = MibTableColumn
jnxBgpM2CfgPeerLocalAs = _JnxBgpM2CfgPeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 5),
    _JnxBgpM2CfgPeerLocalAs_Type()
)
jnxBgpM2CfgPeerLocalAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerLocalAs.setStatus("current")
_JnxBgpM2CfgPeerRemoteAddrType_Type = InetAddressType
_JnxBgpM2CfgPeerRemoteAddrType_Object = MibTableColumn
jnxBgpM2CfgPeerRemoteAddrType = _JnxBgpM2CfgPeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 6),
    _JnxBgpM2CfgPeerRemoteAddrType_Type()
)
jnxBgpM2CfgPeerRemoteAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerRemoteAddrType.setStatus("current")


class _JnxBgpM2CfgPeerRemoteAddr_Type(InetAddress):
    """Custom type jnxBgpM2CfgPeerRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_JnxBgpM2CfgPeerRemoteAddr_Type.__name__ = "InetAddress"
_JnxBgpM2CfgPeerRemoteAddr_Object = MibTableColumn
jnxBgpM2CfgPeerRemoteAddr = _JnxBgpM2CfgPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 7),
    _JnxBgpM2CfgPeerRemoteAddr_Type()
)
jnxBgpM2CfgPeerRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerRemoteAddr.setStatus("current")


class _JnxBgpM2CfgPeerRemotePort_Type(Integer32):
    """Custom type jnxBgpM2CfgPeerRemotePort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_JnxBgpM2CfgPeerRemotePort_Type.__name__ = "Integer32"
_JnxBgpM2CfgPeerRemotePort_Object = MibTableColumn
jnxBgpM2CfgPeerRemotePort = _JnxBgpM2CfgPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 8),
    _JnxBgpM2CfgPeerRemotePort_Type()
)
jnxBgpM2CfgPeerRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerRemotePort.setStatus("current")
_JnxBgpM2CfgPeerRemoteAs_Type = InetAutonomousSystemNumber
_JnxBgpM2CfgPeerRemoteAs_Object = MibTableColumn
jnxBgpM2CfgPeerRemoteAs = _JnxBgpM2CfgPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 9),
    _JnxBgpM2CfgPeerRemoteAs_Type()
)
jnxBgpM2CfgPeerRemoteAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerRemoteAs.setStatus("current")
_JnxBgpM2CfgPeerEntryStorageType_Type = StorageType
_JnxBgpM2CfgPeerEntryStorageType_Object = MibTableColumn
jnxBgpM2CfgPeerEntryStorageType = _JnxBgpM2CfgPeerEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 10),
    _JnxBgpM2CfgPeerEntryStorageType_Type()
)
jnxBgpM2CfgPeerEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerEntryStorageType.setStatus("current")


class _JnxBgpM2CfgPeerError_Type(Integer32):
    """Custom type jnxBgpM2CfgPeerError based on Integer32"""
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


_JnxBgpM2CfgPeerError_Type.__name__ = "Integer32"
_JnxBgpM2CfgPeerError_Object = MibTableColumn
jnxBgpM2CfgPeerError = _JnxBgpM2CfgPeerError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 11),
    _JnxBgpM2CfgPeerError_Type()
)
jnxBgpM2CfgPeerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerError.setStatus("current")
_JnxBgpM2CfgPeerBgpPeerEntry_Type = RowPointer
_JnxBgpM2CfgPeerBgpPeerEntry_Object = MibTableColumn
jnxBgpM2CfgPeerBgpPeerEntry = _JnxBgpM2CfgPeerBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 12),
    _JnxBgpM2CfgPeerBgpPeerEntry_Type()
)
jnxBgpM2CfgPeerBgpPeerEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerBgpPeerEntry.setStatus("current")
_JnxBgpM2CfgPeerRowEntryStatus_Type = RowStatus
_JnxBgpM2CfgPeerRowEntryStatus_Object = MibTableColumn
jnxBgpM2CfgPeerRowEntryStatus = _JnxBgpM2CfgPeerRowEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 13),
    _JnxBgpM2CfgPeerRowEntryStatus_Type()
)
jnxBgpM2CfgPeerRowEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerRowEntryStatus.setStatus("current")


class _JnxBgpM2CfgPeerIndex_Type(Integer32):
    """Custom type jnxBgpM2CfgPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxBgpM2CfgPeerIndex_Type.__name__ = "Integer32"
_JnxBgpM2CfgPeerIndex_Object = MibTableColumn
jnxBgpM2CfgPeerIndex = _JnxBgpM2CfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 14),
    _JnxBgpM2CfgPeerIndex_Type()
)
jnxBgpM2CfgPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerIndex.setStatus("current")


class _JnxBgpM2CfgPeerStatus_Type(Integer32):
    """Custom type jnxBgpM2CfgPeerStatus based on Integer32"""
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


_JnxBgpM2CfgPeerStatus_Type.__name__ = "Integer32"
_JnxBgpM2CfgPeerStatus_Object = MibTableColumn
jnxBgpM2CfgPeerStatus = _JnxBgpM2CfgPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 15),
    _JnxBgpM2CfgPeerStatus_Type()
)
jnxBgpM2CfgPeerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerStatus.setStatus("current")
_JnxBgpM2CfgPeerRoutingInstance_Type = Unsigned32
_JnxBgpM2CfgPeerRoutingInstance_Object = MibTableColumn
jnxBgpM2CfgPeerRoutingInstance = _JnxBgpM2CfgPeerRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 3, 1, 16),
    _JnxBgpM2CfgPeerRoutingInstance_Type()
)
jnxBgpM2CfgPeerRoutingInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerRoutingInstance.setStatus("current")
_JnxBgpM2CfgPeerAuthTable_Object = MibTable
jnxBgpM2CfgPeerAuthTable = _JnxBgpM2CfgPeerAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerAuthTable.setStatus("current")
_JnxBgpM2CfgPeerAuthEntry_Object = MibTableRow
jnxBgpM2CfgPeerAuthEntry = _JnxBgpM2CfgPeerAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerAuthEntry.setStatus("current")


class _JnxBgpM2CfgPeerAuthEnabled_Type(TruthValue):
    """Custom type jnxBgpM2CfgPeerAuthEnabled based on TruthValue"""


_JnxBgpM2CfgPeerAuthEnabled_Object = MibTableColumn
jnxBgpM2CfgPeerAuthEnabled = _JnxBgpM2CfgPeerAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 4, 1, 1),
    _JnxBgpM2CfgPeerAuthEnabled_Type()
)
jnxBgpM2CfgPeerAuthEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerAuthEnabled.setStatus("current")


class _JnxBgpM2CfgPeerAuthCode_Type(Unsigned32):
    """Custom type jnxBgpM2CfgPeerAuthCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxBgpM2CfgPeerAuthCode_Type.__name__ = "Unsigned32"
_JnxBgpM2CfgPeerAuthCode_Object = MibTableColumn
jnxBgpM2CfgPeerAuthCode = _JnxBgpM2CfgPeerAuthCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 4, 1, 2),
    _JnxBgpM2CfgPeerAuthCode_Type()
)
jnxBgpM2CfgPeerAuthCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerAuthCode.setStatus("current")


class _JnxBgpM2CfgPeerAuthValue_Type(OctetString):
    """Custom type jnxBgpM2CfgPeerAuthValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_JnxBgpM2CfgPeerAuthValue_Type.__name__ = "OctetString"
_JnxBgpM2CfgPeerAuthValue_Object = MibTableColumn
jnxBgpM2CfgPeerAuthValue = _JnxBgpM2CfgPeerAuthValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 4, 1, 3),
    _JnxBgpM2CfgPeerAuthValue_Type()
)
jnxBgpM2CfgPeerAuthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerAuthValue.setStatus("current")
_JnxBgpM2CfgPeerTimersTable_Object = MibTable
jnxBgpM2CfgPeerTimersTable = _JnxBgpM2CfgPeerTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 5)
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerTimersTable.setStatus("current")
_JnxBgpM2CfgPeerTimersEntry_Object = MibTableRow
jnxBgpM2CfgPeerTimersEntry = _JnxBgpM2CfgPeerTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 5, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerTimersEntry.setStatus("current")


class _JnxBgpM2CfgPeerConnectRetryInterval_Type(Unsigned32):
    """Custom type jnxBgpM2CfgPeerConnectRetryInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxBgpM2CfgPeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_JnxBgpM2CfgPeerConnectRetryInterval_Object = MibTableColumn
jnxBgpM2CfgPeerConnectRetryInterval = _JnxBgpM2CfgPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 5, 1, 1),
    _JnxBgpM2CfgPeerConnectRetryInterval_Type()
)
jnxBgpM2CfgPeerConnectRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerConnectRetryInterval.setStatus("current")


class _JnxBgpM2CfgPeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type jnxBgpM2CfgPeerHoldTimeConfigured based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_JnxBgpM2CfgPeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_JnxBgpM2CfgPeerHoldTimeConfigured_Object = MibTableColumn
jnxBgpM2CfgPeerHoldTimeConfigured = _JnxBgpM2CfgPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 5, 1, 2),
    _JnxBgpM2CfgPeerHoldTimeConfigured_Type()
)
jnxBgpM2CfgPeerHoldTimeConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerHoldTimeConfigured.setStatus("current")


class _JnxBgpM2CfgPeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type jnxBgpM2CfgPeerKeepAliveConfigured based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_JnxBgpM2CfgPeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_JnxBgpM2CfgPeerKeepAliveConfigured_Object = MibTableColumn
jnxBgpM2CfgPeerKeepAliveConfigured = _JnxBgpM2CfgPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 5, 1, 3),
    _JnxBgpM2CfgPeerKeepAliveConfigured_Type()
)
jnxBgpM2CfgPeerKeepAliveConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerKeepAliveConfigured.setStatus("current")


class _JnxBgpM2CfgPeerMinASOrigInterval_Type(Unsigned32):
    """Custom type jnxBgpM2CfgPeerMinASOrigInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxBgpM2CfgPeerMinASOrigInterval_Type.__name__ = "Unsigned32"
_JnxBgpM2CfgPeerMinASOrigInterval_Object = MibTableColumn
jnxBgpM2CfgPeerMinASOrigInterval = _JnxBgpM2CfgPeerMinASOrigInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 5, 1, 4),
    _JnxBgpM2CfgPeerMinASOrigInterval_Type()
)
jnxBgpM2CfgPeerMinASOrigInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerMinASOrigInterval.setStatus("current")


class _JnxBgpM2CfgPeerMinRouteAdverInter_Type(Unsigned32):
    """Custom type jnxBgpM2CfgPeerMinRouteAdverInter based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxBgpM2CfgPeerMinRouteAdverInter_Type.__name__ = "Unsigned32"
_JnxBgpM2CfgPeerMinRouteAdverInter_Object = MibTableColumn
jnxBgpM2CfgPeerMinRouteAdverInter = _JnxBgpM2CfgPeerMinRouteAdverInter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 5, 1, 5),
    _JnxBgpM2CfgPeerMinRouteAdverInter_Type()
)
jnxBgpM2CfgPeerMinRouteAdverInter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerMinRouteAdverInter.setStatus("current")
_JnxBgpM2CfgPeerExtensions_ObjectIdentity = ObjectIdentity
jnxBgpM2CfgPeerExtensions = _JnxBgpM2CfgPeerExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6)
)
_JnxBgpM2CfgPeerNonCapExts_ObjectIdentity = ObjectIdentity
jnxBgpM2CfgPeerNonCapExts = _JnxBgpM2CfgPeerNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6, 1)
)
_JnxBgpM2CfgPeerRouteReflectionExts_ObjectIdentity = ObjectIdentity
jnxBgpM2CfgPeerRouteReflectionExts = _JnxBgpM2CfgPeerRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6, 1, 2796)
)
_JnxBgpM2CfgPeerReflectorClientTable_Object = MibTable
jnxBgpM2CfgPeerReflectorClientTable = _JnxBgpM2CfgPeerReflectorClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6, 1, 2796, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerReflectorClientTable.setStatus("current")
_JnxBgpM2CfgPeerReflectorClientEntry_Object = MibTableRow
jnxBgpM2CfgPeerReflectorClientEntry = _JnxBgpM2CfgPeerReflectorClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6, 1, 2796, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerReflectorClientEntry.setStatus("current")


class _JnxBgpM2CfgPeerReflectorClient_Type(Integer32):
    """Custom type jnxBgpM2CfgPeerReflectorClient based on Integer32"""
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


_JnxBgpM2CfgPeerReflectorClient_Type.__name__ = "Integer32"
_JnxBgpM2CfgPeerReflectorClient_Object = MibTableColumn
jnxBgpM2CfgPeerReflectorClient = _JnxBgpM2CfgPeerReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6, 1, 2796, 1, 1, 1),
    _JnxBgpM2CfgPeerReflectorClient_Type()
)
jnxBgpM2CfgPeerReflectorClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerReflectorClient.setStatus("current")
_JnxBgpM2CfgPeerASConfederationExts_ObjectIdentity = ObjectIdentity
jnxBgpM2CfgPeerASConfederationExts = _JnxBgpM2CfgPeerASConfederationExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6, 1, 3065)
)
_JnxBgpM2CfgPeerConfedMemberTable_Object = MibTable
jnxBgpM2CfgPeerConfedMemberTable = _JnxBgpM2CfgPeerConfedMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6, 1, 3065, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerConfedMemberTable.setStatus("current")
_JnxBgpM2CfgPeerConfedMemberEntry_Object = MibTableRow
jnxBgpM2CfgPeerConfedMemberEntry = _JnxBgpM2CfgPeerConfedMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6, 1, 3065, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerConfedMemberEntry.setStatus("current")
_JnxBgpM2CfgPeerConfedMember_Type = TruthValue
_JnxBgpM2CfgPeerConfedMember_Object = MibTableColumn
jnxBgpM2CfgPeerConfedMember = _JnxBgpM2CfgPeerConfedMember_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6, 1, 3065, 1, 1, 1),
    _JnxBgpM2CfgPeerConfedMember_Type()
)
jnxBgpM2CfgPeerConfedMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxBgpM2CfgPeerConfedMember.setStatus("current")
_JnxBgpM2CfgPeerCapExts_ObjectIdentity = ObjectIdentity
jnxBgpM2CfgPeerCapExts = _JnxBgpM2CfgPeerCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 2, 8, 6, 2)
)
_JnxBgpM2Rib_ObjectIdentity = ObjectIdentity
jnxBgpM2Rib = _JnxBgpM2Rib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3)
)
_JnxBgpM2NlriTable_Object = MibTable
jnxBgpM2NlriTable = _JnxBgpM2NlriTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2NlriTable.setStatus("current")
_JnxBgpM2NlriEntry_Object = MibTableRow
jnxBgpM2NlriEntry = _JnxBgpM2NlriEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1)
)
jnxBgpM2NlriEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriAfi"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriSafi"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriPrefix"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriPrefixLen"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2NlriEntry.setStatus("current")
_JnxBgpM2NlriIndex_Type = Unsigned32
_JnxBgpM2NlriIndex_Object = MibTableColumn
jnxBgpM2NlriIndex = _JnxBgpM2NlriIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1, 1),
    _JnxBgpM2NlriIndex_Type()
)
jnxBgpM2NlriIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2NlriIndex.setStatus("current")
_JnxBgpM2NlriAfi_Type = InetAddressType
_JnxBgpM2NlriAfi_Object = MibTableColumn
jnxBgpM2NlriAfi = _JnxBgpM2NlriAfi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1, 2),
    _JnxBgpM2NlriAfi_Type()
)
jnxBgpM2NlriAfi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2NlriAfi.setStatus("current")
_JnxBgpM2NlriSafi_Type = JnxBgpM2Safi
_JnxBgpM2NlriSafi_Object = MibTableColumn
jnxBgpM2NlriSafi = _JnxBgpM2NlriSafi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1, 3),
    _JnxBgpM2NlriSafi_Type()
)
jnxBgpM2NlriSafi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2NlriSafi.setStatus("current")


class _JnxBgpM2NlriPrefix_Type(InetAddress):
    """Custom type jnxBgpM2NlriPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_JnxBgpM2NlriPrefix_Type.__name__ = "InetAddress"
_JnxBgpM2NlriPrefix_Object = MibTableColumn
jnxBgpM2NlriPrefix = _JnxBgpM2NlriPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1, 4),
    _JnxBgpM2NlriPrefix_Type()
)
jnxBgpM2NlriPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2NlriPrefix.setStatus("current")
_JnxBgpM2NlriPrefixLen_Type = InetAddressPrefixLength
_JnxBgpM2NlriPrefixLen_Object = MibTableColumn
jnxBgpM2NlriPrefixLen = _JnxBgpM2NlriPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1, 5),
    _JnxBgpM2NlriPrefixLen_Type()
)
jnxBgpM2NlriPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2NlriPrefixLen.setStatus("current")
_JnxBgpM2NlriBest_Type = TruthValue
_JnxBgpM2NlriBest_Object = MibTableColumn
jnxBgpM2NlriBest = _JnxBgpM2NlriBest_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1, 6),
    _JnxBgpM2NlriBest_Type()
)
jnxBgpM2NlriBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2NlriBest.setStatus("current")
_JnxBgpM2NlriCalcLocalPref_Type = Unsigned32
_JnxBgpM2NlriCalcLocalPref_Object = MibTableColumn
jnxBgpM2NlriCalcLocalPref = _JnxBgpM2NlriCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1, 7),
    _JnxBgpM2NlriCalcLocalPref_Type()
)
jnxBgpM2NlriCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2NlriCalcLocalPref.setStatus("current")
_JnxBgpM2PathAttrIndex_Type = Unsigned32
_JnxBgpM2PathAttrIndex_Object = MibTableColumn
jnxBgpM2PathAttrIndex = _JnxBgpM2PathAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1, 8),
    _JnxBgpM2PathAttrIndex_Type()
)
jnxBgpM2PathAttrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrIndex.setStatus("current")


class _JnxBgpM2NlriOpaqueType_Type(Integer32):
    """Custom type jnxBgpM2NlriOpaqueType based on Integer32"""
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


_JnxBgpM2NlriOpaqueType_Type.__name__ = "Integer32"
_JnxBgpM2NlriOpaqueType_Object = MibTableColumn
jnxBgpM2NlriOpaqueType = _JnxBgpM2NlriOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1, 9),
    _JnxBgpM2NlriOpaqueType_Type()
)
jnxBgpM2NlriOpaqueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2NlriOpaqueType.setStatus("current")
_JnxBgpM2NlriOpaquePointer_Type = RowPointer
_JnxBgpM2NlriOpaquePointer_Object = MibTableColumn
jnxBgpM2NlriOpaquePointer = _JnxBgpM2NlriOpaquePointer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 1, 1, 10),
    _JnxBgpM2NlriOpaquePointer_Type()
)
jnxBgpM2NlriOpaquePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2NlriOpaquePointer.setStatus("current")
_JnxBgpM2AdjRibsOutTable_Object = MibTable
jnxBgpM2AdjRibsOutTable = _JnxBgpM2AdjRibsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxBgpM2AdjRibsOutTable.setStatus("current")
_JnxBgpM2AdjRibsOutEntry_Object = MibTableRow
jnxBgpM2AdjRibsOutEntry = _JnxBgpM2AdjRibsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 2, 1)
)
jnxBgpM2AdjRibsOutEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriAfi"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriSafi"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriPrefix"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriPrefixLen"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2AdjRibsOutIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2AdjRibsOutEntry.setStatus("current")
_JnxBgpM2AdjRibsOutIndex_Type = Unsigned32
_JnxBgpM2AdjRibsOutIndex_Object = MibTableColumn
jnxBgpM2AdjRibsOutIndex = _JnxBgpM2AdjRibsOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 2, 1, 1),
    _JnxBgpM2AdjRibsOutIndex_Type()
)
jnxBgpM2AdjRibsOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AdjRibsOutIndex.setStatus("current")
_JnxBgpM2AdjRibsOutRoute_Type = RowPointer
_JnxBgpM2AdjRibsOutRoute_Object = MibTableColumn
jnxBgpM2AdjRibsOutRoute = _JnxBgpM2AdjRibsOutRoute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 2, 1, 2),
    _JnxBgpM2AdjRibsOutRoute_Type()
)
jnxBgpM2AdjRibsOutRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AdjRibsOutRoute.setStatus("current")
_JnxBgpM2PathAttrCount_Type = Counter32
_JnxBgpM2PathAttrCount_Object = MibScalar
jnxBgpM2PathAttrCount = _JnxBgpM2PathAttrCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 3),
    _JnxBgpM2PathAttrCount_Type()
)
jnxBgpM2PathAttrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrCount.setStatus("current")
_JnxBgpM2PathAttrTable_Object = MibTable
jnxBgpM2PathAttrTable = _JnxBgpM2PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrTable.setStatus("current")
_JnxBgpM2PathAttrEntry_Object = MibTableRow
jnxBgpM2PathAttrEntry = _JnxBgpM2PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1)
)
jnxBgpM2PathAttrEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrEntry.setStatus("current")


class _JnxBgpM2PathAttrOrigin_Type(Integer32):
    """Custom type jnxBgpM2PathAttrOrigin based on Integer32"""
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


_JnxBgpM2PathAttrOrigin_Type.__name__ = "Integer32"
_JnxBgpM2PathAttrOrigin_Object = MibTableColumn
jnxBgpM2PathAttrOrigin = _JnxBgpM2PathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 1),
    _JnxBgpM2PathAttrOrigin_Type()
)
jnxBgpM2PathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrOrigin.setStatus("current")
_JnxBgpM2PathAttrNextHopAddrType_Type = InetAddressType
_JnxBgpM2PathAttrNextHopAddrType_Object = MibTableColumn
jnxBgpM2PathAttrNextHopAddrType = _JnxBgpM2PathAttrNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 2),
    _JnxBgpM2PathAttrNextHopAddrType_Type()
)
jnxBgpM2PathAttrNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrNextHopAddrType.setStatus("current")


class _JnxBgpM2PathAttrNextHop_Type(InetAddress):
    """Custom type jnxBgpM2PathAttrNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_JnxBgpM2PathAttrNextHop_Type.__name__ = "InetAddress"
_JnxBgpM2PathAttrNextHop_Object = MibTableColumn
jnxBgpM2PathAttrNextHop = _JnxBgpM2PathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 3),
    _JnxBgpM2PathAttrNextHop_Type()
)
jnxBgpM2PathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrNextHop.setStatus("current")
_JnxBgpM2PathAttrMedPresent_Type = TruthValue
_JnxBgpM2PathAttrMedPresent_Object = MibTableColumn
jnxBgpM2PathAttrMedPresent = _JnxBgpM2PathAttrMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 4),
    _JnxBgpM2PathAttrMedPresent_Type()
)
jnxBgpM2PathAttrMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrMedPresent.setStatus("current")
_JnxBgpM2PathAttrMed_Type = Unsigned32
_JnxBgpM2PathAttrMed_Object = MibTableColumn
jnxBgpM2PathAttrMed = _JnxBgpM2PathAttrMed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 5),
    _JnxBgpM2PathAttrMed_Type()
)
jnxBgpM2PathAttrMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrMed.setStatus("current")
_JnxBgpM2PathAttrLocalPrefPresent_Type = TruthValue
_JnxBgpM2PathAttrLocalPrefPresent_Object = MibTableColumn
jnxBgpM2PathAttrLocalPrefPresent = _JnxBgpM2PathAttrLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 6),
    _JnxBgpM2PathAttrLocalPrefPresent_Type()
)
jnxBgpM2PathAttrLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrLocalPrefPresent.setStatus("current")
_JnxBgpM2PathAttrLocalPref_Type = Unsigned32
_JnxBgpM2PathAttrLocalPref_Object = MibTableColumn
jnxBgpM2PathAttrLocalPref = _JnxBgpM2PathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 7),
    _JnxBgpM2PathAttrLocalPref_Type()
)
jnxBgpM2PathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrLocalPref.setStatus("current")


class _JnxBgpM2PathAttrAtomicAggregate_Type(Integer32):
    """Custom type jnxBgpM2PathAttrAtomicAggregate based on Integer32"""
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


_JnxBgpM2PathAttrAtomicAggregate_Type.__name__ = "Integer32"
_JnxBgpM2PathAttrAtomicAggregate_Object = MibTableColumn
jnxBgpM2PathAttrAtomicAggregate = _JnxBgpM2PathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 8),
    _JnxBgpM2PathAttrAtomicAggregate_Type()
)
jnxBgpM2PathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrAtomicAggregate.setStatus("current")
_JnxBgpM2PathAttrAggregatorAS_Type = InetAutonomousSystemNumber
_JnxBgpM2PathAttrAggregatorAS_Object = MibTableColumn
jnxBgpM2PathAttrAggregatorAS = _JnxBgpM2PathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 9),
    _JnxBgpM2PathAttrAggregatorAS_Type()
)
jnxBgpM2PathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrAggregatorAS.setStatus("current")
_JnxBgpM2PathAttrAggregatorAddr_Type = JnxBgpM2Identifier
_JnxBgpM2PathAttrAggregatorAddr_Object = MibTableColumn
jnxBgpM2PathAttrAggregatorAddr = _JnxBgpM2PathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 10),
    _JnxBgpM2PathAttrAggregatorAddr_Type()
)
jnxBgpM2PathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrAggregatorAddr.setStatus("current")
_JnxBgpM2AsPathCalcLength_Type = Unsigned32
_JnxBgpM2AsPathCalcLength_Object = MibTableColumn
jnxBgpM2AsPathCalcLength = _JnxBgpM2AsPathCalcLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 11),
    _JnxBgpM2AsPathCalcLength_Type()
)
jnxBgpM2AsPathCalcLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPathCalcLength.setStatus("current")
_JnxBgpM2AsPathString_Type = SnmpAdminString
_JnxBgpM2AsPathString_Object = MibTableColumn
jnxBgpM2AsPathString = _JnxBgpM2AsPathString_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 12),
    _JnxBgpM2AsPathString_Type()
)
jnxBgpM2AsPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPathString.setStatus("current")
_JnxBgpM2AsPathIndex_Type = Unsigned32
_JnxBgpM2AsPathIndex_Object = MibTableColumn
jnxBgpM2AsPathIndex = _JnxBgpM2AsPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 4, 1, 13),
    _JnxBgpM2AsPathIndex_Type()
)
jnxBgpM2AsPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPathIndex.setStatus("current")
_JnxBgpM2AsPath4byteTable_Object = MibTable
jnxBgpM2AsPath4byteTable = _JnxBgpM2AsPath4byteTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    jnxBgpM2AsPath4byteTable.setStatus("current")
_JnxBgpM2AsPath4byteEntry_Object = MibTableRow
jnxBgpM2AsPath4byteEntry = _JnxBgpM2AsPath4byteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2AsPath4byteEntry.setStatus("current")
_JnxBgpM2AsPath4bytePathPresent_Type = TruthValue
_JnxBgpM2AsPath4bytePathPresent_Object = MibTableColumn
jnxBgpM2AsPath4bytePathPresent = _JnxBgpM2AsPath4bytePathPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 5, 1, 1),
    _JnxBgpM2AsPath4bytePathPresent_Type()
)
jnxBgpM2AsPath4bytePathPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPath4bytePathPresent.setStatus("current")
_JnxBgpM2AsPath4byteAggregatorAS_Type = InetAutonomousSystemNumber
_JnxBgpM2AsPath4byteAggregatorAS_Object = MibTableColumn
jnxBgpM2AsPath4byteAggregatorAS = _JnxBgpM2AsPath4byteAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 5, 1, 2),
    _JnxBgpM2AsPath4byteAggregatorAS_Type()
)
jnxBgpM2AsPath4byteAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPath4byteAggregatorAS.setStatus("current")
_JnxBgpM2AsPath4byteCalcLength_Type = Unsigned32
_JnxBgpM2AsPath4byteCalcLength_Object = MibTableColumn
jnxBgpM2AsPath4byteCalcLength = _JnxBgpM2AsPath4byteCalcLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 5, 1, 3),
    _JnxBgpM2AsPath4byteCalcLength_Type()
)
jnxBgpM2AsPath4byteCalcLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPath4byteCalcLength.setStatus("current")
_JnxBgpM2AsPath4byteString_Type = SnmpAdminString
_JnxBgpM2AsPath4byteString_Object = MibTableColumn
jnxBgpM2AsPath4byteString = _JnxBgpM2AsPath4byteString_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 5, 1, 4),
    _JnxBgpM2AsPath4byteString_Type()
)
jnxBgpM2AsPath4byteString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPath4byteString.setStatus("current")
_JnxBgpM2AsPath4byteIndex_Type = Unsigned32
_JnxBgpM2AsPath4byteIndex_Object = MibTableColumn
jnxBgpM2AsPath4byteIndex = _JnxBgpM2AsPath4byteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 5, 1, 5),
    _JnxBgpM2AsPath4byteIndex_Type()
)
jnxBgpM2AsPath4byteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPath4byteIndex.setStatus("current")
_JnxBgpM2AsPathTable_Object = MibTable
jnxBgpM2AsPathTable = _JnxBgpM2AsPathTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    jnxBgpM2AsPathTable.setStatus("current")
_JnxBgpM2AsPathEntry_Object = MibTableRow
jnxBgpM2AsPathEntry = _JnxBgpM2AsPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 6, 1)
)
jnxBgpM2AsPathEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathSegmentIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathElementIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathElementValue"),
)
if mibBuilder.loadTexts:
    jnxBgpM2AsPathEntry.setStatus("current")
_JnxBgpM2AsPathSegmentIndex_Type = Unsigned32
_JnxBgpM2AsPathSegmentIndex_Object = MibTableColumn
jnxBgpM2AsPathSegmentIndex = _JnxBgpM2AsPathSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 6, 1, 1),
    _JnxBgpM2AsPathSegmentIndex_Type()
)
jnxBgpM2AsPathSegmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPathSegmentIndex.setStatus("current")
_JnxBgpM2AsPathElementIndex_Type = Unsigned32
_JnxBgpM2AsPathElementIndex_Object = MibTableColumn
jnxBgpM2AsPathElementIndex = _JnxBgpM2AsPathElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 6, 1, 2),
    _JnxBgpM2AsPathElementIndex_Type()
)
jnxBgpM2AsPathElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPathElementIndex.setStatus("current")


class _JnxBgpM2AsPathType_Type(Integer32):
    """Custom type jnxBgpM2AsPathType based on Integer32"""
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


_JnxBgpM2AsPathType_Type.__name__ = "Integer32"
_JnxBgpM2AsPathType_Object = MibTableColumn
jnxBgpM2AsPathType = _JnxBgpM2AsPathType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 6, 1, 3),
    _JnxBgpM2AsPathType_Type()
)
jnxBgpM2AsPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPathType.setStatus("current")
_JnxBgpM2AsPathElementValue_Type = InetAutonomousSystemNumber
_JnxBgpM2AsPathElementValue_Object = MibTableColumn
jnxBgpM2AsPathElementValue = _JnxBgpM2AsPathElementValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 6, 1, 4),
    _JnxBgpM2AsPathElementValue_Type()
)
jnxBgpM2AsPathElementValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2AsPathElementValue.setStatus("current")
_JnxBgpM2PathAttrUnknownTable_Object = MibTable
jnxBgpM2PathAttrUnknownTable = _JnxBgpM2PathAttrUnknownTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrUnknownTable.setStatus("current")
_JnxBgpM2PathAttrUnknownEntry_Object = MibTableRow
jnxBgpM2PathAttrUnknownEntry = _JnxBgpM2PathAttrUnknownEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 7, 1)
)
jnxBgpM2PathAttrUnknownEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrUnknownIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrUnknownEntry.setStatus("current")
_JnxBgpM2PathAttrUnknownIndex_Type = Unsigned32
_JnxBgpM2PathAttrUnknownIndex_Object = MibTableColumn
jnxBgpM2PathAttrUnknownIndex = _JnxBgpM2PathAttrUnknownIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 7, 1, 1),
    _JnxBgpM2PathAttrUnknownIndex_Type()
)
jnxBgpM2PathAttrUnknownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrUnknownIndex.setStatus("current")
_JnxBgpM2PathAttrUnknownType_Type = Unsigned32
_JnxBgpM2PathAttrUnknownType_Object = MibTableColumn
jnxBgpM2PathAttrUnknownType = _JnxBgpM2PathAttrUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 7, 1, 2),
    _JnxBgpM2PathAttrUnknownType_Type()
)
jnxBgpM2PathAttrUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrUnknownType.setStatus("current")


class _JnxBgpM2PathAttrUnknownValue_Type(OctetString):
    """Custom type jnxBgpM2PathAttrUnknownValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4070),
    )


_JnxBgpM2PathAttrUnknownValue_Type.__name__ = "OctetString"
_JnxBgpM2PathAttrUnknownValue_Object = MibTableColumn
jnxBgpM2PathAttrUnknownValue = _JnxBgpM2PathAttrUnknownValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 7, 1, 3),
    _JnxBgpM2PathAttrUnknownValue_Type()
)
jnxBgpM2PathAttrUnknownValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrUnknownValue.setStatus("current")
_JnxBgpM2PathAttrExtensions_ObjectIdentity = ObjectIdentity
jnxBgpM2PathAttrExtensions = _JnxBgpM2PathAttrExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8)
)
_JnxBgpM2PathAttrNonCapExts_ObjectIdentity = ObjectIdentity
jnxBgpM2PathAttrNonCapExts = _JnxBgpM2PathAttrNonCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1)
)
_JnxBgpM2PathAttrCommunityExts_ObjectIdentity = ObjectIdentity
jnxBgpM2PathAttrCommunityExts = _JnxBgpM2PathAttrCommunityExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 1997)
)
_JnxBgpM2PathAttrCommTable_Object = MibTable
jnxBgpM2PathAttrCommTable = _JnxBgpM2PathAttrCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 1997, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrCommTable.setStatus("current")
_JnxBgpM2PathAttrCommEntry_Object = MibTableRow
jnxBgpM2PathAttrCommEntry = _JnxBgpM2PathAttrCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 1997, 1, 1)
)
jnxBgpM2PathAttrCommEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrCommIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrCommEntry.setStatus("current")
_JnxBgpM2PathAttrCommIndex_Type = Unsigned32
_JnxBgpM2PathAttrCommIndex_Object = MibTableColumn
jnxBgpM2PathAttrCommIndex = _JnxBgpM2PathAttrCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 1997, 1, 1, 1),
    _JnxBgpM2PathAttrCommIndex_Type()
)
jnxBgpM2PathAttrCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrCommIndex.setStatus("current")
_JnxBgpM2PathAttrCommValue_Type = JnxBgpM2Community
_JnxBgpM2PathAttrCommValue_Object = MibTableColumn
jnxBgpM2PathAttrCommValue = _JnxBgpM2PathAttrCommValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 1997, 1, 1, 2),
    _JnxBgpM2PathAttrCommValue_Type()
)
jnxBgpM2PathAttrCommValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrCommValue.setStatus("current")
_JnxBgpM2LinkLocalNextHopTable_Object = MibTable
jnxBgpM2LinkLocalNextHopTable = _JnxBgpM2LinkLocalNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2545)
)
if mibBuilder.loadTexts:
    jnxBgpM2LinkLocalNextHopTable.setStatus("current")
_JnxBgpM2LinkLocalNextHopEntry_Object = MibTableRow
jnxBgpM2LinkLocalNextHopEntry = _JnxBgpM2LinkLocalNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2545, 1)
)
jnxBgpM2LinkLocalNextHopEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2LinkLocalNextHopEntry.setStatus("current")
_JnxBgpM2LinkLocalNextHopPresent_Type = TruthValue
_JnxBgpM2LinkLocalNextHopPresent_Object = MibTableColumn
jnxBgpM2LinkLocalNextHopPresent = _JnxBgpM2LinkLocalNextHopPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2545, 1, 1),
    _JnxBgpM2LinkLocalNextHopPresent_Type()
)
jnxBgpM2LinkLocalNextHopPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2LinkLocalNextHopPresent.setStatus("current")


class _JnxBgpM2LinkLocalNextHop_Type(InetAddress):
    """Custom type jnxBgpM2LinkLocalNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_JnxBgpM2LinkLocalNextHop_Type.__name__ = "InetAddress"
_JnxBgpM2LinkLocalNextHop_Object = MibTableColumn
jnxBgpM2LinkLocalNextHop = _JnxBgpM2LinkLocalNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2545, 1, 2),
    _JnxBgpM2LinkLocalNextHop_Type()
)
jnxBgpM2LinkLocalNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2LinkLocalNextHop.setStatus("current")
_JnxBgpM2PathAttrRouteReflectionExts_ObjectIdentity = ObjectIdentity
jnxBgpM2PathAttrRouteReflectionExts = _JnxBgpM2PathAttrRouteReflectionExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2796)
)
_JnxBgpM2PathAttrOriginatorIdTable_Object = MibTable
jnxBgpM2PathAttrOriginatorIdTable = _JnxBgpM2PathAttrOriginatorIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2796, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrOriginatorIdTable.setStatus("current")
_JnxBgpM2PathAttrOriginatorIdEntry_Object = MibTableRow
jnxBgpM2PathAttrOriginatorIdEntry = _JnxBgpM2PathAttrOriginatorIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2796, 1, 1)
)
jnxBgpM2PathAttrOriginatorIdEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrOriginatorIdEntry.setStatus("current")
_JnxBgpM2PathAttrOriginatorId_Type = JnxBgpM2Identifier
_JnxBgpM2PathAttrOriginatorId_Object = MibTableColumn
jnxBgpM2PathAttrOriginatorId = _JnxBgpM2PathAttrOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2796, 1, 1, 1),
    _JnxBgpM2PathAttrOriginatorId_Type()
)
jnxBgpM2PathAttrOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrOriginatorId.setStatus("current")
_JnxBgpM2PathAttrClusterTable_Object = MibTable
jnxBgpM2PathAttrClusterTable = _JnxBgpM2PathAttrClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2796, 2)
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrClusterTable.setStatus("current")
_JnxBgpM2PathAttrClusterEntry_Object = MibTableRow
jnxBgpM2PathAttrClusterEntry = _JnxBgpM2PathAttrClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2796, 2, 1)
)
jnxBgpM2PathAttrClusterEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrClusterIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrClusterEntry.setStatus("current")
_JnxBgpM2PathAttrClusterIndex_Type = Unsigned32
_JnxBgpM2PathAttrClusterIndex_Object = MibTableColumn
jnxBgpM2PathAttrClusterIndex = _JnxBgpM2PathAttrClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2796, 2, 1, 1),
    _JnxBgpM2PathAttrClusterIndex_Type()
)
jnxBgpM2PathAttrClusterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrClusterIndex.setStatus("current")
_JnxBgpM2PathAttrClusterValue_Type = JnxBgpM2Identifier
_JnxBgpM2PathAttrClusterValue_Object = MibTableColumn
jnxBgpM2PathAttrClusterValue = _JnxBgpM2PathAttrClusterValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 2796, 2, 1, 2),
    _JnxBgpM2PathAttrClusterValue_Type()
)
jnxBgpM2PathAttrClusterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrClusterValue.setStatus("current")
_JnxBgpM2PathAttrExtCommTable_Object = MibTable
jnxBgpM2PathAttrExtCommTable = _JnxBgpM2PathAttrExtCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 65001)
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrExtCommTable.setStatus("current")
_JnxBgpM2PathAttrExtCommEntry_Object = MibTableRow
jnxBgpM2PathAttrExtCommEntry = _JnxBgpM2PathAttrExtCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 65001, 1)
)
jnxBgpM2PathAttrExtCommEntry.setIndexNames(
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrIndex"),
    (0, "BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrExtCommIndex"),
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrExtCommEntry.setStatus("current")
_JnxBgpM2PathAttrExtCommIndex_Type = Unsigned32
_JnxBgpM2PathAttrExtCommIndex_Object = MibTableColumn
jnxBgpM2PathAttrExtCommIndex = _JnxBgpM2PathAttrExtCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 65001, 1, 1),
    _JnxBgpM2PathAttrExtCommIndex_Type()
)
jnxBgpM2PathAttrExtCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrExtCommIndex.setStatus("current")
_JnxBgpM2PathAttrExtCommValue_Type = JnxBgpM2ExtendedCommunity
_JnxBgpM2PathAttrExtCommValue_Object = MibTableColumn
jnxBgpM2PathAttrExtCommValue = _JnxBgpM2PathAttrExtCommValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 1, 65001, 1, 2),
    _JnxBgpM2PathAttrExtCommValue_Type()
)
jnxBgpM2PathAttrExtCommValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBgpM2PathAttrExtCommValue.setStatus("current")
_JnxBgpM2PathAttrCapExts_ObjectIdentity = ObjectIdentity
jnxBgpM2PathAttrCapExts = _JnxBgpM2PathAttrCapExts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 3, 8, 2)
)
_JnxBgpM2Conformance_ObjectIdentity = ObjectIdentity
jnxBgpM2Conformance = _JnxBgpM2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4)
)
_JnxBgpM2MIBCompliances_ObjectIdentity = ObjectIdentity
jnxBgpM2MIBCompliances = _JnxBgpM2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 1)
)
_JnxBgpM2MIBGroups_ObjectIdentity = ObjectIdentity
jnxBgpM2MIBGroups = _JnxBgpM2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2)
)
jnxBgpM2PeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2PeerErrorsEntry")
)
jnxBgpM2PeerErrorsEntry.setIndexNames(*jnxBgpM2PeerEntry.getIndexNames())
jnxBgpM2PeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2PeerAuthEntry")
)
jnxBgpM2PeerAuthEntry.setIndexNames(*jnxBgpM2PeerEntry.getIndexNames())
jnxBgpM2PeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2PeerEventTimesEntry")
)
jnxBgpM2PeerEventTimesEntry.setIndexNames(*jnxBgpM2PeerEntry.getIndexNames())
jnxBgpM2PeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2PeerConfiguredTimersEntry")
)
jnxBgpM2PeerConfiguredTimersEntry.setIndexNames(*jnxBgpM2PeerEntry.getIndexNames())
jnxBgpM2PeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2PeerNegotiatedTimersEntry")
)
jnxBgpM2PeerNegotiatedTimersEntry.setIndexNames(*jnxBgpM2PeerEntry.getIndexNames())
jnxBgpM2PeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2PeerCountersEntry")
)
jnxBgpM2PeerCountersEntry.setIndexNames(*jnxBgpM2PeerEntry.getIndexNames())
jnxBgpM2PeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2PeerReflectorClientEntry")
)
jnxBgpM2PeerReflectorClientEntry.setIndexNames(*jnxBgpM2PeerEntry.getIndexNames())
jnxBgpM2PeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2PeerConfedMemberEntry")
)
jnxBgpM2PeerConfedMemberEntry.setIndexNames(*jnxBgpM2PeerEntry.getIndexNames())
jnxBgpM2CfgPeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2CfgPeerAuthEntry")
)
jnxBgpM2CfgPeerAuthEntry.setIndexNames(*jnxBgpM2CfgPeerEntry.getIndexNames())
jnxBgpM2CfgPeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2CfgPeerTimersEntry")
)
jnxBgpM2CfgPeerTimersEntry.setIndexNames(*jnxBgpM2CfgPeerEntry.getIndexNames())
jnxBgpM2CfgPeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2CfgPeerReflectorClientEntry")
)
jnxBgpM2CfgPeerReflectorClientEntry.setIndexNames(*jnxBgpM2CfgPeerEntry.getIndexNames())
jnxBgpM2CfgPeerEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2CfgPeerConfedMemberEntry")
)
jnxBgpM2CfgPeerConfedMemberEntry.setIndexNames(*jnxBgpM2CfgPeerEntry.getIndexNames())
jnxBgpM2PathAttrEntry.registerAugmentions(
    ("BGP4-V2-MIB-JUNIPER",
     "jnxBgpM2AsPath4byteEntry")
)
jnxBgpM2AsPath4byteEntry.setIndexNames(*jnxBgpM2PathAttrEntry.getIndexNames())

# Managed Objects groups

jnxBgpM2AuthenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 1)
)
jnxBgpM2AuthenticationGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2SupportedAuthCode"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2SupportedAuthValue"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerAuthSent"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerAuthSentCode"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerAuthSentValue"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerAuthRcvd"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerAuthRcvdCode"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerAuthRcvdValue"))
)
if mibBuilder.loadTexts:
    jnxBgpM2AuthenticationGroup.setStatus("current")

jnxBgpM2CommunitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 2)
)
jnxBgpM2CommunitiesGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrCommIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrCommValue"))
)
if mibBuilder.loadTexts:
    jnxBgpM2CommunitiesGroup.setStatus("current")

jnxBgpM2ExtCommunitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 3)
)
jnxBgpM2ExtCommunitiesGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrExtCommIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrExtCommValue"))
)
if mibBuilder.loadTexts:
    jnxBgpM2ExtCommunitiesGroup.setStatus("current")

jnxBgpM2RouteReflectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 4)
)
jnxBgpM2RouteReflectionGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2RouteReflector"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2ClusterId"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerReflectorClient"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrOriginatorId"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrClusterIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrClusterValue"))
)
if mibBuilder.loadTexts:
    jnxBgpM2RouteReflectionGroup.setStatus("current")

jnxBgpM2AsConfederationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 5)
)
jnxBgpM2AsConfederationGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2ConfederationRouter"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2ConfederationId"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerConfedMember"))
)
if mibBuilder.loadTexts:
    jnxBgpM2AsConfederationGroup.setStatus("current")

jnxBgpM2TimersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 6)
)
jnxBgpM2TimersGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerFsmEstablishedTime"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerInUpdatesElapsedTime"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerConnectRetryInterval"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerHoldTimeConfigured"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerKeepAliveConfigured"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerMinASOrigInterval"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerMinRouteAdverInterval"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerHoldTime"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerKeepAlive"))
)
if mibBuilder.loadTexts:
    jnxBgpM2TimersGroup.setStatus("current")

jnxBgpM2CountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 7)
)
jnxBgpM2CountersGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerInUpdates"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerOutUpdates"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerInTotalMessages"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerOutTotalMessages"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerFsmEstablishedTrans"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PrefixCountersAfi"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PrefixCountersSafi"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PrefixInPrefixes"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PrefixInPrefixesAccepted"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PrefixInPrefixesRejected"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PrefixOutPrefixes"))
)
if mibBuilder.loadTexts:
    jnxBgpM2CountersGroup.setStatus("current")

jnxBgpM2CapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 8)
)
jnxBgpM2CapabilitiesGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CapabilitySupportAvailable"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2SupportedCapabilityCode"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2SupportedCapability"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerCapAnnouncedCode"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerCapAnnouncedIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerCapAnnouncedValue"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerCapReceivedCode"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerCapReceivedIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerCapReceivedValue"))
)
if mibBuilder.loadTexts:
    jnxBgpM2CapabilitiesGroup.setStatus("current")

jnxBgpM2AsPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 9)
)
jnxBgpM2AsPathGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathSegmentIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathElementIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathElementValue"))
)
if mibBuilder.loadTexts:
    jnxBgpM2AsPathGroup.setStatus("current")

jnxBgpM2As4byteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 10)
)
jnxBgpM2As4byteGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsSize"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPath4bytePathPresent"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPath4byteAggregatorAS"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPath4byteCalcLength"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPath4byteString"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPath4byteIndex"))
)
if mibBuilder.loadTexts:
    jnxBgpM2As4byteGroup.setStatus("current")

jnxBgpM2BaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 11)
)
jnxBgpM2BaseGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2LocalAs"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2LocalIdentifier"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2VersionIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2VersionSupported"))
)
if mibBuilder.loadTexts:
    jnxBgpM2BaseGroup.setStatus("current")

jnxBgpM2ErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 12)
)
jnxBgpM2ErrorsGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorReceived"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorReceivedData"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorReceivedTime"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorReceivedText"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorSent"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorSentData"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorSentTime"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorSentText"))
)
if mibBuilder.loadTexts:
    jnxBgpM2ErrorsGroup.setStatus("current")

jnxBgpM2PeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 13)
)
jnxBgpM2PeerGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerIdentifier"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerState"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerStatus"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerConfiguredVersion"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerNegotiatedVersion"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLocalAddrType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLocalAddr"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLocalPort"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLocalAs"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRemoteAddrType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRemoteAddr"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRemotePort"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRemoteAs"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRoutingInstance"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerIndex"))
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerGroup.setStatus("current")

jnxBgpM2PathAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 14)
)
jnxBgpM2PathAttributesGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrCount"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathCalcLength"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathElementValue"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathString"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AsPathType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriAfi"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriBest"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriPrefix"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriPrefixLen"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriSafi"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriOpaqueType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriOpaquePointer"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2NlriCalcLocalPref"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AdjRibsOutIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2AdjRibsOutRoute"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrAggregatorAS"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrAggregatorAddr"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrAtomicAggregate"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrLocalPref"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrLocalPrefPresent"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrMed"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrMedPresent"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrNextHop"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrNextHopAddrType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrOrigin"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrUnknownIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrUnknownType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PathAttrUnknownValue"))
)
if mibBuilder.loadTexts:
    jnxBgpM2PathAttributesGroup.setStatus("current")

jnxBgpM2PeerConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 15)
)
jnxBgpM2PeerConfigurationGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgBaseScalarStorageType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgLocalAs"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgLocalIdentifier"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerAdminStatus"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerNextIndex"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerConfiguredVersion"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgAllowVersionNegotiation"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerLocalAddrType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerLocalAddr"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerLocalAs"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerRemoteAddrType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerRemoteAddr"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerRemotePort"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerRemoteAs"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerEntryStorageType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerError"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerBgpPeerEntry"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerRowEntryStatus"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerStatus"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerConnectRetryInterval"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerHoldTimeConfigured"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerKeepAliveConfigured"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerMinASOrigInterval"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerMinRouteAdverInter"))
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerConfigurationGroup.setStatus("current")

jnxBgpM2PeerAuthConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 16)
)
jnxBgpM2PeerAuthConfigurationGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerAuthEnabled"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerAuthCode"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerAuthValue"))
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerAuthConfigurationGroup.setStatus("current")

jnxBgpM2PeerRouteReflectorCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 17)
)
jnxBgpM2PeerRouteReflectorCfgGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgRouteReflector"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgClusterId"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerReflectorClient"))
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerRouteReflectorCfgGroup.setStatus("current")

jnxBgpM2PeerAsConfederationCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 18)
)
jnxBgpM2PeerAsConfederationCfgGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgConfederationRouter"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgConfederationId"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2CfgPeerConfedMember"))
)
if mibBuilder.loadTexts:
    jnxBgpM2PeerAsConfederationCfgGroup.setStatus("current")

jnxBgpM2Rfc2545Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 20)
)
jnxBgpM2Rfc2545Group.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2LinkLocalNextHopPresent"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2LinkLocalNextHop"))
)
if mibBuilder.loadTexts:
    jnxBgpM2Rfc2545Group.setStatus("current")


# Notification objects

jnxBgpM2Established = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 0, 1)
)
jnxBgpM2Established.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLocalAddrType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLocalAddr"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRemoteAddrType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRemoteAddr"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorReceived"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerState"))
)
if mibBuilder.loadTexts:
    jnxBgpM2Established.setStatus(
        "current"
    )

jnxBgpM2BackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 1, 0, 2)
)
jnxBgpM2BackwardTransition.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLocalAddrType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLocalAddr"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRemoteAddrType"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerRemoteAddr"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorReceived"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerLastErrorReceivedText"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2PeerState"))
)
if mibBuilder.loadTexts:
    jnxBgpM2BackwardTransition.setStatus(
        "current"
    )


# Notifications groups

jnxBgpM2MIBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 2, 19)
)
jnxBgpM2MIBNotificationsGroup.setObjects(
      *(("BGP4-V2-MIB-JUNIPER", "jnxBgpM2Established"),
        ("BGP4-V2-MIB-JUNIPER", "jnxBgpM2BackwardTransition"))
)
if mibBuilder.loadTexts:
    jnxBgpM2MIBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

jnxBgpM2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 5, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBgpM2MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BGP4-V2-MIB-JUNIPER",
    **{"JnxBgpM2Identifier": JnxBgpM2Identifier,
       "JnxBgpM2Safi": JnxBgpM2Safi,
       "JnxBgpM2Community": JnxBgpM2Community,
       "JnxBgpM2ExtendedCommunity": JnxBgpM2ExtendedCommunity,
       "jnxBgpM2": jnxBgpM2,
       "jnxBgpM2BaseScalars": jnxBgpM2BaseScalars,
       "jnxBgpM2BaseNotifications": jnxBgpM2BaseNotifications,
       "jnxBgpM2Established": jnxBgpM2Established,
       "jnxBgpM2BackwardTransition": jnxBgpM2BackwardTransition,
       "jnxBgpM2Version": jnxBgpM2Version,
       "jnxBgpM2VersionTable": jnxBgpM2VersionTable,
       "jnxBgpM2VersionEntry": jnxBgpM2VersionEntry,
       "jnxBgpM2VersionIndex": jnxBgpM2VersionIndex,
       "jnxBgpM2VersionSupported": jnxBgpM2VersionSupported,
       "jnxBgpM2SupportedAuthentication": jnxBgpM2SupportedAuthentication,
       "jnxBgpM2SupportedAuthTable": jnxBgpM2SupportedAuthTable,
       "jnxBgpM2SupportedAuthEntry": jnxBgpM2SupportedAuthEntry,
       "jnxBgpM2SupportedAuthCode": jnxBgpM2SupportedAuthCode,
       "jnxBgpM2SupportedAuthValue": jnxBgpM2SupportedAuthValue,
       "jnxBgpM2SupportedCapabilities": jnxBgpM2SupportedCapabilities,
       "jnxBgpM2CapabilitySupportAvailable": jnxBgpM2CapabilitySupportAvailable,
       "jnxBgpM2SupportedCapabilitiesTable": jnxBgpM2SupportedCapabilitiesTable,
       "jnxBgpM2SupportedCapabilitiesEntry": jnxBgpM2SupportedCapabilitiesEntry,
       "jnxBgpM2SupportedCapabilityCode": jnxBgpM2SupportedCapabilityCode,
       "jnxBgpM2SupportedCapability": jnxBgpM2SupportedCapability,
       "jnxBgpM2AsSize": jnxBgpM2AsSize,
       "jnxBgpM2LocalAs": jnxBgpM2LocalAs,
       "jnxBgpM2LocalIdentifier": jnxBgpM2LocalIdentifier,
       "jnxBgpM2BaseScalarExtensions": jnxBgpM2BaseScalarExtensions,
       "jnxBgpM2BaseScalarNonCapExts": jnxBgpM2BaseScalarNonCapExts,
       "jnxBgpM2BaseScalarRouteReflectExts": jnxBgpM2BaseScalarRouteReflectExts,
       "jnxBgpM2RouteReflector": jnxBgpM2RouteReflector,
       "jnxBgpM2ClusterId": jnxBgpM2ClusterId,
       "jnxBgpM2BaseScalarASConfedExts": jnxBgpM2BaseScalarASConfedExts,
       "jnxBgpM2ConfederationRouter": jnxBgpM2ConfederationRouter,
       "jnxBgpM2ConfederationId": jnxBgpM2ConfederationId,
       "jnxBgpM2BaseScalarCapExts": jnxBgpM2BaseScalarCapExts,
       "jnxBgpM2BaseScalarConfiguration": jnxBgpM2BaseScalarConfiguration,
       "jnxBgpM2CfgBaseScalarStorageType": jnxBgpM2CfgBaseScalarStorageType,
       "jnxBgpM2CfgLocalAs": jnxBgpM2CfgLocalAs,
       "jnxBgpM2CfgLocalIdentifier": jnxBgpM2CfgLocalIdentifier,
       "jnxBgpM2CfgBaseScalarExtensions": jnxBgpM2CfgBaseScalarExtensions,
       "jnxBgpM2CfgBaseScalarNonCapExts": jnxBgpM2CfgBaseScalarNonCapExts,
       "jnxBgpM2CfgBaseScalarReflectorExts": jnxBgpM2CfgBaseScalarReflectorExts,
       "jnxBgpM2CfgRouteReflector": jnxBgpM2CfgRouteReflector,
       "jnxBgpM2CfgClusterId": jnxBgpM2CfgClusterId,
       "jnxBgpM2CfgBaseScalarASConfedExts": jnxBgpM2CfgBaseScalarASConfedExts,
       "jnxBgpM2CfgConfederationRouter": jnxBgpM2CfgConfederationRouter,
       "jnxBgpM2CfgConfederationId": jnxBgpM2CfgConfederationId,
       "jnxBgpM2CfgBaseScalarCapExts": jnxBgpM2CfgBaseScalarCapExts,
       "jnxBgpM2Peer": jnxBgpM2Peer,
       "jnxBgpM2PeerData": jnxBgpM2PeerData,
       "jnxBgpM2PeerTable": jnxBgpM2PeerTable,
       "jnxBgpM2PeerEntry": jnxBgpM2PeerEntry,
       "jnxBgpM2PeerIdentifier": jnxBgpM2PeerIdentifier,
       "jnxBgpM2PeerState": jnxBgpM2PeerState,
       "jnxBgpM2PeerStatus": jnxBgpM2PeerStatus,
       "jnxBgpM2PeerConfiguredVersion": jnxBgpM2PeerConfiguredVersion,
       "jnxBgpM2PeerNegotiatedVersion": jnxBgpM2PeerNegotiatedVersion,
       "jnxBgpM2PeerLocalAddrType": jnxBgpM2PeerLocalAddrType,
       "jnxBgpM2PeerLocalAddr": jnxBgpM2PeerLocalAddr,
       "jnxBgpM2PeerLocalPort": jnxBgpM2PeerLocalPort,
       "jnxBgpM2PeerLocalAs": jnxBgpM2PeerLocalAs,
       "jnxBgpM2PeerRemoteAddrType": jnxBgpM2PeerRemoteAddrType,
       "jnxBgpM2PeerRemoteAddr": jnxBgpM2PeerRemoteAddr,
       "jnxBgpM2PeerRemotePort": jnxBgpM2PeerRemotePort,
       "jnxBgpM2PeerRemoteAs": jnxBgpM2PeerRemoteAs,
       "jnxBgpM2PeerIndex": jnxBgpM2PeerIndex,
       "jnxBgpM2PeerRoutingInstance": jnxBgpM2PeerRoutingInstance,
       "jnxBgpM2PeerErrors": jnxBgpM2PeerErrors,
       "jnxBgpM2PeerErrorsTable": jnxBgpM2PeerErrorsTable,
       "jnxBgpM2PeerErrorsEntry": jnxBgpM2PeerErrorsEntry,
       "jnxBgpM2PeerLastErrorReceived": jnxBgpM2PeerLastErrorReceived,
       "jnxBgpM2PeerLastErrorSent": jnxBgpM2PeerLastErrorSent,
       "jnxBgpM2PeerLastErrorReceivedTime": jnxBgpM2PeerLastErrorReceivedTime,
       "jnxBgpM2PeerLastErrorSentTime": jnxBgpM2PeerLastErrorSentTime,
       "jnxBgpM2PeerLastErrorReceivedText": jnxBgpM2PeerLastErrorReceivedText,
       "jnxBgpM2PeerLastErrorSentText": jnxBgpM2PeerLastErrorSentText,
       "jnxBgpM2PeerLastErrorReceivedData": jnxBgpM2PeerLastErrorReceivedData,
       "jnxBgpM2PeerLastErrorSentData": jnxBgpM2PeerLastErrorSentData,
       "jnxBgpM2PeerAuthentication": jnxBgpM2PeerAuthentication,
       "jnxBgpM2PeerAuthTable": jnxBgpM2PeerAuthTable,
       "jnxBgpM2PeerAuthEntry": jnxBgpM2PeerAuthEntry,
       "jnxBgpM2PeerAuthSent": jnxBgpM2PeerAuthSent,
       "jnxBgpM2PeerAuthSentCode": jnxBgpM2PeerAuthSentCode,
       "jnxBgpM2PeerAuthSentValue": jnxBgpM2PeerAuthSentValue,
       "jnxBgpM2PeerAuthRcvd": jnxBgpM2PeerAuthRcvd,
       "jnxBgpM2PeerAuthRcvdCode": jnxBgpM2PeerAuthRcvdCode,
       "jnxBgpM2PeerAuthRcvdValue": jnxBgpM2PeerAuthRcvdValue,
       "jnxBgpM2PeerTimers": jnxBgpM2PeerTimers,
       "jnxBgpM2PeerEventTimesTable": jnxBgpM2PeerEventTimesTable,
       "jnxBgpM2PeerEventTimesEntry": jnxBgpM2PeerEventTimesEntry,
       "jnxBgpM2PeerFsmEstablishedTime": jnxBgpM2PeerFsmEstablishedTime,
       "jnxBgpM2PeerInUpdatesElapsedTime": jnxBgpM2PeerInUpdatesElapsedTime,
       "jnxBgpM2PeerConfiguredTimersTable": jnxBgpM2PeerConfiguredTimersTable,
       "jnxBgpM2PeerConfiguredTimersEntry": jnxBgpM2PeerConfiguredTimersEntry,
       "jnxBgpM2PeerConnectRetryInterval": jnxBgpM2PeerConnectRetryInterval,
       "jnxBgpM2PeerHoldTimeConfigured": jnxBgpM2PeerHoldTimeConfigured,
       "jnxBgpM2PeerKeepAliveConfigured": jnxBgpM2PeerKeepAliveConfigured,
       "jnxBgpM2PeerMinASOrigInterval": jnxBgpM2PeerMinASOrigInterval,
       "jnxBgpM2PeerMinRouteAdverInterval": jnxBgpM2PeerMinRouteAdverInterval,
       "jnxBgpM2PeerNegotiatedTimersTable": jnxBgpM2PeerNegotiatedTimersTable,
       "jnxBgpM2PeerNegotiatedTimersEntry": jnxBgpM2PeerNegotiatedTimersEntry,
       "jnxBgpM2PeerHoldTime": jnxBgpM2PeerHoldTime,
       "jnxBgpM2PeerKeepAlive": jnxBgpM2PeerKeepAlive,
       "jnxBgpM2PeerCapabilities": jnxBgpM2PeerCapabilities,
       "jnxBgpM2PeerCapsAnnouncedTable": jnxBgpM2PeerCapsAnnouncedTable,
       "jnxBgpM2PeerCapsAnnouncedEntry": jnxBgpM2PeerCapsAnnouncedEntry,
       "jnxBgpM2PeerCapAnnouncedCode": jnxBgpM2PeerCapAnnouncedCode,
       "jnxBgpM2PeerCapAnnouncedIndex": jnxBgpM2PeerCapAnnouncedIndex,
       "jnxBgpM2PeerCapAnnouncedValue": jnxBgpM2PeerCapAnnouncedValue,
       "jnxBgpM2PeerCapsReceivedTable": jnxBgpM2PeerCapsReceivedTable,
       "jnxBgpM2PeerCapsReceivedEntry": jnxBgpM2PeerCapsReceivedEntry,
       "jnxBgpM2PeerCapReceivedCode": jnxBgpM2PeerCapReceivedCode,
       "jnxBgpM2PeerCapReceivedIndex": jnxBgpM2PeerCapReceivedIndex,
       "jnxBgpM2PeerCapReceivedValue": jnxBgpM2PeerCapReceivedValue,
       "jnxBgpM2PeerCounters": jnxBgpM2PeerCounters,
       "jnxBgpM2PeerCountersTable": jnxBgpM2PeerCountersTable,
       "jnxBgpM2PeerCountersEntry": jnxBgpM2PeerCountersEntry,
       "jnxBgpM2PeerInUpdates": jnxBgpM2PeerInUpdates,
       "jnxBgpM2PeerOutUpdates": jnxBgpM2PeerOutUpdates,
       "jnxBgpM2PeerInTotalMessages": jnxBgpM2PeerInTotalMessages,
       "jnxBgpM2PeerOutTotalMessages": jnxBgpM2PeerOutTotalMessages,
       "jnxBgpM2PeerFsmEstablishedTrans": jnxBgpM2PeerFsmEstablishedTrans,
       "jnxBgpM2PrefixCountersTable": jnxBgpM2PrefixCountersTable,
       "jnxBgpM2PrefixCountersEntry": jnxBgpM2PrefixCountersEntry,
       "jnxBgpM2PrefixCountersAfi": jnxBgpM2PrefixCountersAfi,
       "jnxBgpM2PrefixCountersSafi": jnxBgpM2PrefixCountersSafi,
       "jnxBgpM2PrefixInPrefixes": jnxBgpM2PrefixInPrefixes,
       "jnxBgpM2PrefixInPrefixesAccepted": jnxBgpM2PrefixInPrefixesAccepted,
       "jnxBgpM2PrefixInPrefixesRejected": jnxBgpM2PrefixInPrefixesRejected,
       "jnxBgpM2PrefixOutPrefixes": jnxBgpM2PrefixOutPrefixes,
       "jnxBgpM2PrefixInPrefixesActive": jnxBgpM2PrefixInPrefixesActive,
       "jnxBgpM2PeerExtensions": jnxBgpM2PeerExtensions,
       "jnxBgpM2PeerNonCapExts": jnxBgpM2PeerNonCapExts,
       "jnxBgpM2PeerRouteReflectionExts": jnxBgpM2PeerRouteReflectionExts,
       "jnxBgpM2PeerReflectorClientTable": jnxBgpM2PeerReflectorClientTable,
       "jnxBgpM2PeerReflectorClientEntry": jnxBgpM2PeerReflectorClientEntry,
       "jnxBgpM2PeerReflectorClient": jnxBgpM2PeerReflectorClient,
       "jnxBgpM2PeerASConfederationExts": jnxBgpM2PeerASConfederationExts,
       "jnxBgpM2PeerConfedMemberTable": jnxBgpM2PeerConfedMemberTable,
       "jnxBgpM2PeerConfedMemberEntry": jnxBgpM2PeerConfedMemberEntry,
       "jnxBgpM2PeerConfedMember": jnxBgpM2PeerConfedMember,
       "jnxBgpM2PeerCapExts": jnxBgpM2PeerCapExts,
       "jnxBgpM2PeerConfiguration": jnxBgpM2PeerConfiguration,
       "jnxBgpM2CfgPeerAdminStatusTable": jnxBgpM2CfgPeerAdminStatusTable,
       "jnxBgpM2CfgPeerAdminStatusEntry": jnxBgpM2CfgPeerAdminStatusEntry,
       "jnxBgpM2CfgPeerAdminStatus": jnxBgpM2CfgPeerAdminStatus,
       "jnxBgpM2CfgPeerNextIndex": jnxBgpM2CfgPeerNextIndex,
       "jnxBgpM2CfgPeerTable": jnxBgpM2CfgPeerTable,
       "jnxBgpM2CfgPeerEntry": jnxBgpM2CfgPeerEntry,
       "jnxBgpM2CfgPeerConfiguredVersion": jnxBgpM2CfgPeerConfiguredVersion,
       "jnxBgpM2CfgAllowVersionNegotiation": jnxBgpM2CfgAllowVersionNegotiation,
       "jnxBgpM2CfgPeerLocalAddrType": jnxBgpM2CfgPeerLocalAddrType,
       "jnxBgpM2CfgPeerLocalAddr": jnxBgpM2CfgPeerLocalAddr,
       "jnxBgpM2CfgPeerLocalAs": jnxBgpM2CfgPeerLocalAs,
       "jnxBgpM2CfgPeerRemoteAddrType": jnxBgpM2CfgPeerRemoteAddrType,
       "jnxBgpM2CfgPeerRemoteAddr": jnxBgpM2CfgPeerRemoteAddr,
       "jnxBgpM2CfgPeerRemotePort": jnxBgpM2CfgPeerRemotePort,
       "jnxBgpM2CfgPeerRemoteAs": jnxBgpM2CfgPeerRemoteAs,
       "jnxBgpM2CfgPeerEntryStorageType": jnxBgpM2CfgPeerEntryStorageType,
       "jnxBgpM2CfgPeerError": jnxBgpM2CfgPeerError,
       "jnxBgpM2CfgPeerBgpPeerEntry": jnxBgpM2CfgPeerBgpPeerEntry,
       "jnxBgpM2CfgPeerRowEntryStatus": jnxBgpM2CfgPeerRowEntryStatus,
       "jnxBgpM2CfgPeerIndex": jnxBgpM2CfgPeerIndex,
       "jnxBgpM2CfgPeerStatus": jnxBgpM2CfgPeerStatus,
       "jnxBgpM2CfgPeerRoutingInstance": jnxBgpM2CfgPeerRoutingInstance,
       "jnxBgpM2CfgPeerAuthTable": jnxBgpM2CfgPeerAuthTable,
       "jnxBgpM2CfgPeerAuthEntry": jnxBgpM2CfgPeerAuthEntry,
       "jnxBgpM2CfgPeerAuthEnabled": jnxBgpM2CfgPeerAuthEnabled,
       "jnxBgpM2CfgPeerAuthCode": jnxBgpM2CfgPeerAuthCode,
       "jnxBgpM2CfgPeerAuthValue": jnxBgpM2CfgPeerAuthValue,
       "jnxBgpM2CfgPeerTimersTable": jnxBgpM2CfgPeerTimersTable,
       "jnxBgpM2CfgPeerTimersEntry": jnxBgpM2CfgPeerTimersEntry,
       "jnxBgpM2CfgPeerConnectRetryInterval": jnxBgpM2CfgPeerConnectRetryInterval,
       "jnxBgpM2CfgPeerHoldTimeConfigured": jnxBgpM2CfgPeerHoldTimeConfigured,
       "jnxBgpM2CfgPeerKeepAliveConfigured": jnxBgpM2CfgPeerKeepAliveConfigured,
       "jnxBgpM2CfgPeerMinASOrigInterval": jnxBgpM2CfgPeerMinASOrigInterval,
       "jnxBgpM2CfgPeerMinRouteAdverInter": jnxBgpM2CfgPeerMinRouteAdverInter,
       "jnxBgpM2CfgPeerExtensions": jnxBgpM2CfgPeerExtensions,
       "jnxBgpM2CfgPeerNonCapExts": jnxBgpM2CfgPeerNonCapExts,
       "jnxBgpM2CfgPeerRouteReflectionExts": jnxBgpM2CfgPeerRouteReflectionExts,
       "jnxBgpM2CfgPeerReflectorClientTable": jnxBgpM2CfgPeerReflectorClientTable,
       "jnxBgpM2CfgPeerReflectorClientEntry": jnxBgpM2CfgPeerReflectorClientEntry,
       "jnxBgpM2CfgPeerReflectorClient": jnxBgpM2CfgPeerReflectorClient,
       "jnxBgpM2CfgPeerASConfederationExts": jnxBgpM2CfgPeerASConfederationExts,
       "jnxBgpM2CfgPeerConfedMemberTable": jnxBgpM2CfgPeerConfedMemberTable,
       "jnxBgpM2CfgPeerConfedMemberEntry": jnxBgpM2CfgPeerConfedMemberEntry,
       "jnxBgpM2CfgPeerConfedMember": jnxBgpM2CfgPeerConfedMember,
       "jnxBgpM2CfgPeerCapExts": jnxBgpM2CfgPeerCapExts,
       "jnxBgpM2Rib": jnxBgpM2Rib,
       "jnxBgpM2NlriTable": jnxBgpM2NlriTable,
       "jnxBgpM2NlriEntry": jnxBgpM2NlriEntry,
       "jnxBgpM2NlriIndex": jnxBgpM2NlriIndex,
       "jnxBgpM2NlriAfi": jnxBgpM2NlriAfi,
       "jnxBgpM2NlriSafi": jnxBgpM2NlriSafi,
       "jnxBgpM2NlriPrefix": jnxBgpM2NlriPrefix,
       "jnxBgpM2NlriPrefixLen": jnxBgpM2NlriPrefixLen,
       "jnxBgpM2NlriBest": jnxBgpM2NlriBest,
       "jnxBgpM2NlriCalcLocalPref": jnxBgpM2NlriCalcLocalPref,
       "jnxBgpM2PathAttrIndex": jnxBgpM2PathAttrIndex,
       "jnxBgpM2NlriOpaqueType": jnxBgpM2NlriOpaqueType,
       "jnxBgpM2NlriOpaquePointer": jnxBgpM2NlriOpaquePointer,
       "jnxBgpM2AdjRibsOutTable": jnxBgpM2AdjRibsOutTable,
       "jnxBgpM2AdjRibsOutEntry": jnxBgpM2AdjRibsOutEntry,
       "jnxBgpM2AdjRibsOutIndex": jnxBgpM2AdjRibsOutIndex,
       "jnxBgpM2AdjRibsOutRoute": jnxBgpM2AdjRibsOutRoute,
       "jnxBgpM2PathAttrCount": jnxBgpM2PathAttrCount,
       "jnxBgpM2PathAttrTable": jnxBgpM2PathAttrTable,
       "jnxBgpM2PathAttrEntry": jnxBgpM2PathAttrEntry,
       "jnxBgpM2PathAttrOrigin": jnxBgpM2PathAttrOrigin,
       "jnxBgpM2PathAttrNextHopAddrType": jnxBgpM2PathAttrNextHopAddrType,
       "jnxBgpM2PathAttrNextHop": jnxBgpM2PathAttrNextHop,
       "jnxBgpM2PathAttrMedPresent": jnxBgpM2PathAttrMedPresent,
       "jnxBgpM2PathAttrMed": jnxBgpM2PathAttrMed,
       "jnxBgpM2PathAttrLocalPrefPresent": jnxBgpM2PathAttrLocalPrefPresent,
       "jnxBgpM2PathAttrLocalPref": jnxBgpM2PathAttrLocalPref,
       "jnxBgpM2PathAttrAtomicAggregate": jnxBgpM2PathAttrAtomicAggregate,
       "jnxBgpM2PathAttrAggregatorAS": jnxBgpM2PathAttrAggregatorAS,
       "jnxBgpM2PathAttrAggregatorAddr": jnxBgpM2PathAttrAggregatorAddr,
       "jnxBgpM2AsPathCalcLength": jnxBgpM2AsPathCalcLength,
       "jnxBgpM2AsPathString": jnxBgpM2AsPathString,
       "jnxBgpM2AsPathIndex": jnxBgpM2AsPathIndex,
       "jnxBgpM2AsPath4byteTable": jnxBgpM2AsPath4byteTable,
       "jnxBgpM2AsPath4byteEntry": jnxBgpM2AsPath4byteEntry,
       "jnxBgpM2AsPath4bytePathPresent": jnxBgpM2AsPath4bytePathPresent,
       "jnxBgpM2AsPath4byteAggregatorAS": jnxBgpM2AsPath4byteAggregatorAS,
       "jnxBgpM2AsPath4byteCalcLength": jnxBgpM2AsPath4byteCalcLength,
       "jnxBgpM2AsPath4byteString": jnxBgpM2AsPath4byteString,
       "jnxBgpM2AsPath4byteIndex": jnxBgpM2AsPath4byteIndex,
       "jnxBgpM2AsPathTable": jnxBgpM2AsPathTable,
       "jnxBgpM2AsPathEntry": jnxBgpM2AsPathEntry,
       "jnxBgpM2AsPathSegmentIndex": jnxBgpM2AsPathSegmentIndex,
       "jnxBgpM2AsPathElementIndex": jnxBgpM2AsPathElementIndex,
       "jnxBgpM2AsPathType": jnxBgpM2AsPathType,
       "jnxBgpM2AsPathElementValue": jnxBgpM2AsPathElementValue,
       "jnxBgpM2PathAttrUnknownTable": jnxBgpM2PathAttrUnknownTable,
       "jnxBgpM2PathAttrUnknownEntry": jnxBgpM2PathAttrUnknownEntry,
       "jnxBgpM2PathAttrUnknownIndex": jnxBgpM2PathAttrUnknownIndex,
       "jnxBgpM2PathAttrUnknownType": jnxBgpM2PathAttrUnknownType,
       "jnxBgpM2PathAttrUnknownValue": jnxBgpM2PathAttrUnknownValue,
       "jnxBgpM2PathAttrExtensions": jnxBgpM2PathAttrExtensions,
       "jnxBgpM2PathAttrNonCapExts": jnxBgpM2PathAttrNonCapExts,
       "jnxBgpM2PathAttrCommunityExts": jnxBgpM2PathAttrCommunityExts,
       "jnxBgpM2PathAttrCommTable": jnxBgpM2PathAttrCommTable,
       "jnxBgpM2PathAttrCommEntry": jnxBgpM2PathAttrCommEntry,
       "jnxBgpM2PathAttrCommIndex": jnxBgpM2PathAttrCommIndex,
       "jnxBgpM2PathAttrCommValue": jnxBgpM2PathAttrCommValue,
       "jnxBgpM2LinkLocalNextHopTable": jnxBgpM2LinkLocalNextHopTable,
       "jnxBgpM2LinkLocalNextHopEntry": jnxBgpM2LinkLocalNextHopEntry,
       "jnxBgpM2LinkLocalNextHopPresent": jnxBgpM2LinkLocalNextHopPresent,
       "jnxBgpM2LinkLocalNextHop": jnxBgpM2LinkLocalNextHop,
       "jnxBgpM2PathAttrRouteReflectionExts": jnxBgpM2PathAttrRouteReflectionExts,
       "jnxBgpM2PathAttrOriginatorIdTable": jnxBgpM2PathAttrOriginatorIdTable,
       "jnxBgpM2PathAttrOriginatorIdEntry": jnxBgpM2PathAttrOriginatorIdEntry,
       "jnxBgpM2PathAttrOriginatorId": jnxBgpM2PathAttrOriginatorId,
       "jnxBgpM2PathAttrClusterTable": jnxBgpM2PathAttrClusterTable,
       "jnxBgpM2PathAttrClusterEntry": jnxBgpM2PathAttrClusterEntry,
       "jnxBgpM2PathAttrClusterIndex": jnxBgpM2PathAttrClusterIndex,
       "jnxBgpM2PathAttrClusterValue": jnxBgpM2PathAttrClusterValue,
       "jnxBgpM2PathAttrExtCommTable": jnxBgpM2PathAttrExtCommTable,
       "jnxBgpM2PathAttrExtCommEntry": jnxBgpM2PathAttrExtCommEntry,
       "jnxBgpM2PathAttrExtCommIndex": jnxBgpM2PathAttrExtCommIndex,
       "jnxBgpM2PathAttrExtCommValue": jnxBgpM2PathAttrExtCommValue,
       "jnxBgpM2PathAttrCapExts": jnxBgpM2PathAttrCapExts,
       "jnxBgpM2Conformance": jnxBgpM2Conformance,
       "jnxBgpM2MIBCompliances": jnxBgpM2MIBCompliances,
       "jnxBgpM2MIBCompliance": jnxBgpM2MIBCompliance,
       "jnxBgpM2MIBGroups": jnxBgpM2MIBGroups,
       "jnxBgpM2AuthenticationGroup": jnxBgpM2AuthenticationGroup,
       "jnxBgpM2CommunitiesGroup": jnxBgpM2CommunitiesGroup,
       "jnxBgpM2ExtCommunitiesGroup": jnxBgpM2ExtCommunitiesGroup,
       "jnxBgpM2RouteReflectionGroup": jnxBgpM2RouteReflectionGroup,
       "jnxBgpM2AsConfederationGroup": jnxBgpM2AsConfederationGroup,
       "jnxBgpM2TimersGroup": jnxBgpM2TimersGroup,
       "jnxBgpM2CountersGroup": jnxBgpM2CountersGroup,
       "jnxBgpM2CapabilitiesGroup": jnxBgpM2CapabilitiesGroup,
       "jnxBgpM2AsPathGroup": jnxBgpM2AsPathGroup,
       "jnxBgpM2As4byteGroup": jnxBgpM2As4byteGroup,
       "jnxBgpM2BaseGroup": jnxBgpM2BaseGroup,
       "jnxBgpM2ErrorsGroup": jnxBgpM2ErrorsGroup,
       "jnxBgpM2PeerGroup": jnxBgpM2PeerGroup,
       "jnxBgpM2PathAttributesGroup": jnxBgpM2PathAttributesGroup,
       "jnxBgpM2PeerConfigurationGroup": jnxBgpM2PeerConfigurationGroup,
       "jnxBgpM2PeerAuthConfigurationGroup": jnxBgpM2PeerAuthConfigurationGroup,
       "jnxBgpM2PeerRouteReflectorCfgGroup": jnxBgpM2PeerRouteReflectorCfgGroup,
       "jnxBgpM2PeerAsConfederationCfgGroup": jnxBgpM2PeerAsConfederationCfgGroup,
       "jnxBgpM2MIBNotificationsGroup": jnxBgpM2MIBNotificationsGroup,
       "jnxBgpM2Rfc2545Group": jnxBgpM2Rfc2545Group}
)
