# SNMP MIB module (ISNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:57 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(FcAddressIdOrZero,
 FcNameIdOrZero) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcAddressIdOrZero",
    "FcNameIdOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

isnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 163)
)
isnsMIB.setRevisions(
        ("2007-07-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IsnsDiscoveryDomainSetId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IsnsDdsStatusType(Bits, TextualConvention):
    status = "current"


class IsnsDiscoveryDomainId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IsnsDdFeatureType(Bits, TextualConvention):
    status = "current"


class IsnsDdDdsModificationType(Bits, TextualConvention):
    status = "current"


class IsnsEntityIndexIdOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class IsnsPortalGroupIndexId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IsnsPortalIndexId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IsnsPortalPortTypeId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1))
    )



class IsnsPortalGroupTagIdOrNull(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )



class IsnsPortalSecurityType(Bits, TextualConvention):
    status = "current"


class IsnsNodeIndexId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class IsnsIscsiNodeType(Bits, TextualConvention):
    status = "current"


class IsnsFcClassOfServiceType(Bits, TextualConvention):
    status = "current"


class IsnsIscsiScnType(Bits, TextualConvention):
    status = "current"


class IsnsIfcpScnType(Bits, TextualConvention):
    status = "current"


class IsnsFcPortRoleType(Bits, TextualConvention):
    status = "current"


class IsnsSrvrDiscoveryMethodsType(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_IsnsNotifications_ObjectIdentity = ObjectIdentity
isnsNotifications = _IsnsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 0)
)
_IsnsObjects_ObjectIdentity = ObjectIdentity
isnsObjects = _IsnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1)
)
_IsnsServerInfo_ObjectIdentity = ObjectIdentity
isnsServerInfo = _IsnsServerInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 1)
)
_IsnsServerTable_Object = MibTable
isnsServerTable = _IsnsServerTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1)
)
if mibBuilder.loadTexts:
    isnsServerTable.setStatus("current")
_IsnsServerEntry_Object = MibTableRow
isnsServerEntry = _IsnsServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1)
)
isnsServerEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
)
if mibBuilder.loadTexts:
    isnsServerEntry.setStatus("current")


class _IsnsServerIndex_Type(Unsigned32):
    """Custom type isnsServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IsnsServerIndex_Type.__name__ = "Unsigned32"
_IsnsServerIndex_Object = MibTableColumn
isnsServerIndex = _IsnsServerIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 1),
    _IsnsServerIndex_Type()
)
isnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsServerIndex.setStatus("current")
_IsnsServerName_Type = SnmpAdminString
_IsnsServerName_Object = MibTableColumn
isnsServerName = _IsnsServerName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 2),
    _IsnsServerName_Type()
)
isnsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerName.setStatus("current")


class _IsnsServerIsnsVersion_Type(Unsigned32):
    """Custom type isnsServerIsnsVersion based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsnsServerIsnsVersion_Type.__name__ = "Unsigned32"
_IsnsServerIsnsVersion_Object = MibTableColumn
isnsServerIsnsVersion = _IsnsServerIsnsVersion_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 3),
    _IsnsServerIsnsVersion_Type()
)
isnsServerIsnsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerIsnsVersion.setStatus("current")
_IsnsServerVendorInfo_Type = SnmpAdminString
_IsnsServerVendorInfo_Object = MibTableColumn
isnsServerVendorInfo = _IsnsServerVendorInfo_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 4),
    _IsnsServerVendorInfo_Type()
)
isnsServerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerVendorInfo.setStatus("current")
_IsnsServerPhysicalIndex_Type = PhysicalIndex
_IsnsServerPhysicalIndex_Object = MibTableColumn
isnsServerPhysicalIndex = _IsnsServerPhysicalIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 5),
    _IsnsServerPhysicalIndex_Type()
)
isnsServerPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerPhysicalIndex.setStatus("current")
_IsnsServerTcpPort_Type = InetPortNumber
_IsnsServerTcpPort_Object = MibTableColumn
isnsServerTcpPort = _IsnsServerTcpPort_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 6),
    _IsnsServerTcpPort_Type()
)
isnsServerTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerTcpPort.setStatus("current")
_IsnsServerUdpPort_Type = InetPortNumber
_IsnsServerUdpPort_Object = MibTableColumn
isnsServerUdpPort = _IsnsServerUdpPort_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 7),
    _IsnsServerUdpPort_Type()
)
isnsServerUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerUdpPort.setStatus("current")
_IsnsServerDiscontinuityTime_Type = TimeStamp
_IsnsServerDiscontinuityTime_Object = MibTableColumn
isnsServerDiscontinuityTime = _IsnsServerDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 8),
    _IsnsServerDiscontinuityTime_Type()
)
isnsServerDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerDiscontinuityTime.setStatus("current")


class _IsnsServerRole_Type(Integer32):
    """Custom type isnsServerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupServer", 3),
          ("notSet", 1),
          ("server", 2))
    )


_IsnsServerRole_Type.__name__ = "Integer32"
_IsnsServerRole_Object = MibTableColumn
isnsServerRole = _IsnsServerRole_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 9),
    _IsnsServerRole_Type()
)
isnsServerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerRole.setStatus("current")
_IsnsServerDiscoveryMethodsEnabled_Type = IsnsSrvrDiscoveryMethodsType
_IsnsServerDiscoveryMethodsEnabled_Object = MibTableColumn
isnsServerDiscoveryMethodsEnabled = _IsnsServerDiscoveryMethodsEnabled_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 10),
    _IsnsServerDiscoveryMethodsEnabled_Type()
)
isnsServerDiscoveryMethodsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerDiscoveryMethodsEnabled.setStatus("current")
_IsnsServerDiscoveryMcGroupType_Type = InetAddressType
_IsnsServerDiscoveryMcGroupType_Object = MibTableColumn
isnsServerDiscoveryMcGroupType = _IsnsServerDiscoveryMcGroupType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 11),
    _IsnsServerDiscoveryMcGroupType_Type()
)
isnsServerDiscoveryMcGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerDiscoveryMcGroupType.setStatus("current")
_IsnsServerDiscoveryMcGroupAddress_Type = InetAddress
_IsnsServerDiscoveryMcGroupAddress_Object = MibTableColumn
isnsServerDiscoveryMcGroupAddress = _IsnsServerDiscoveryMcGroupAddress_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 12),
    _IsnsServerDiscoveryMcGroupAddress_Type()
)
isnsServerDiscoveryMcGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerDiscoveryMcGroupAddress.setStatus("current")


class _IsnsServerEsiNonResponseThreshold_Type(Unsigned32):
    """Custom type isnsServerEsiNonResponseThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsnsServerEsiNonResponseThreshold_Type.__name__ = "Unsigned32"
_IsnsServerEsiNonResponseThreshold_Object = MibTableColumn
isnsServerEsiNonResponseThreshold = _IsnsServerEsiNonResponseThreshold_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 13),
    _IsnsServerEsiNonResponseThreshold_Type()
)
isnsServerEsiNonResponseThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerEsiNonResponseThreshold.setStatus("current")


class _IsnsServerEnableControlNodeMgtScn_Type(TruthValue):
    """Custom type isnsServerEnableControlNodeMgtScn based on TruthValue"""


_IsnsServerEnableControlNodeMgtScn_Object = MibTableColumn
isnsServerEnableControlNodeMgtScn = _IsnsServerEnableControlNodeMgtScn_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 14),
    _IsnsServerEnableControlNodeMgtScn_Type()
)
isnsServerEnableControlNodeMgtScn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerEnableControlNodeMgtScn.setStatus("current")


class _IsnsServerDefaultDdDdsStatus_Type(Integer32):
    """Custom type isnsServerDefaultDdDdsStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inDefaultDdAndDds", 2),
          ("inNoDomain", 1))
    )


_IsnsServerDefaultDdDdsStatus_Type.__name__ = "Integer32"
_IsnsServerDefaultDdDdsStatus_Object = MibTableColumn
isnsServerDefaultDdDdsStatus = _IsnsServerDefaultDdDdsStatus_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 15),
    _IsnsServerDefaultDdDdsStatus_Type()
)
isnsServerDefaultDdDdsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerDefaultDdDdsStatus.setStatus("current")
_IsnsServerUpdateDdDdsSupported_Type = IsnsDdDdsModificationType
_IsnsServerUpdateDdDdsSupported_Object = MibTableColumn
isnsServerUpdateDdDdsSupported = _IsnsServerUpdateDdDdsSupported_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 16),
    _IsnsServerUpdateDdDdsSupported_Type()
)
isnsServerUpdateDdDdsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerUpdateDdDdsSupported.setStatus("current")
_IsnsServerUpdateDdDdsEnabled_Type = IsnsDdDdsModificationType
_IsnsServerUpdateDdDdsEnabled_Object = MibTableColumn
isnsServerUpdateDdDdsEnabled = _IsnsServerUpdateDdDdsEnabled_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 1, 1, 17),
    _IsnsServerUpdateDdDdsEnabled_Type()
)
isnsServerUpdateDdDdsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsServerUpdateDdDdsEnabled.setStatus("current")
_IsnsNumObjectsTable_Object = MibTable
isnsNumObjectsTable = _IsnsNumObjectsTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 2)
)
if mibBuilder.loadTexts:
    isnsNumObjectsTable.setStatus("current")
_IsnsNumObjectsEntry_Object = MibTableRow
isnsNumObjectsEntry = _IsnsNumObjectsEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    isnsNumObjectsEntry.setStatus("current")


class _IsnsNumDds_Type(Gauge32):
    """Custom type isnsNumDds based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsNumDds_Type.__name__ = "Gauge32"
_IsnsNumDds_Object = MibTableColumn
isnsNumDds = _IsnsNumDds_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 1),
    _IsnsNumDds_Type()
)
isnsNumDds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsNumDds.setStatus("current")


class _IsnsNumDd_Type(Gauge32):
    """Custom type isnsNumDd based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsNumDd_Type.__name__ = "Gauge32"
_IsnsNumDd_Object = MibTableColumn
isnsNumDd = _IsnsNumDd_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 2),
    _IsnsNumDd_Type()
)
isnsNumDd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsNumDd.setStatus("current")


class _IsnsNumEntities_Type(Gauge32):
    """Custom type isnsNumEntities based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsNumEntities_Type.__name__ = "Gauge32"
_IsnsNumEntities_Object = MibTableColumn
isnsNumEntities = _IsnsNumEntities_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 3),
    _IsnsNumEntities_Type()
)
isnsNumEntities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsNumEntities.setStatus("current")


class _IsnsNumPortals_Type(Gauge32):
    """Custom type isnsNumPortals based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsNumPortals_Type.__name__ = "Gauge32"
_IsnsNumPortals_Object = MibTableColumn
isnsNumPortals = _IsnsNumPortals_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 4),
    _IsnsNumPortals_Type()
)
isnsNumPortals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsNumPortals.setStatus("current")


class _IsnsNumPortalGroups_Type(Gauge32):
    """Custom type isnsNumPortalGroups based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsNumPortalGroups_Type.__name__ = "Gauge32"
_IsnsNumPortalGroups_Object = MibTableColumn
isnsNumPortalGroups = _IsnsNumPortalGroups_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 5),
    _IsnsNumPortalGroups_Type()
)
isnsNumPortalGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsNumPortalGroups.setStatus("current")


class _IsnsNumIscsiNodes_Type(Gauge32):
    """Custom type isnsNumIscsiNodes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsNumIscsiNodes_Type.__name__ = "Gauge32"
_IsnsNumIscsiNodes_Object = MibTableColumn
isnsNumIscsiNodes = _IsnsNumIscsiNodes_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 6),
    _IsnsNumIscsiNodes_Type()
)
isnsNumIscsiNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsNumIscsiNodes.setStatus("current")


class _IsnsNumFcPorts_Type(Gauge32):
    """Custom type isnsNumFcPorts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsNumFcPorts_Type.__name__ = "Gauge32"
_IsnsNumFcPorts_Object = MibTableColumn
isnsNumFcPorts = _IsnsNumFcPorts_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 7),
    _IsnsNumFcPorts_Type()
)
isnsNumFcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsNumFcPorts.setStatus("current")


class _IsnsNumFcNodes_Type(Gauge32):
    """Custom type isnsNumFcNodes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsNumFcNodes_Type.__name__ = "Gauge32"
_IsnsNumFcNodes_Object = MibTableColumn
isnsNumFcNodes = _IsnsNumFcNodes_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 2, 1, 8),
    _IsnsNumFcNodes_Type()
)
isnsNumFcNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsNumFcNodes.setStatus("current")
_IsnsControlNodeInfo_ObjectIdentity = ObjectIdentity
isnsControlNodeInfo = _IsnsControlNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3)
)
_IsnsControlNodeIscsiTable_Object = MibTable
isnsControlNodeIscsiTable = _IsnsControlNodeIscsiTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    isnsControlNodeIscsiTable.setStatus("current")
_IsnsControlNodeIscsiEntry_Object = MibTableRow
isnsControlNodeIscsiEntry = _IsnsControlNodeIscsiEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1, 1)
)
isnsControlNodeIscsiEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsControlNodeIscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    isnsControlNodeIscsiEntry.setStatus("current")
_IsnsControlNodeIscsiNodeIndex_Type = IsnsNodeIndexId
_IsnsControlNodeIscsiNodeIndex_Object = MibTableColumn
isnsControlNodeIscsiNodeIndex = _IsnsControlNodeIscsiNodeIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1, 1, 1),
    _IsnsControlNodeIscsiNodeIndex_Type()
)
isnsControlNodeIscsiNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsControlNodeIscsiNodeIndex.setStatus("current")
_IsnsControlNodeIscsiNodeName_Type = SnmpAdminString
_IsnsControlNodeIscsiNodeName_Object = MibTableColumn
isnsControlNodeIscsiNodeName = _IsnsControlNodeIscsiNodeName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1, 1, 2),
    _IsnsControlNodeIscsiNodeName_Type()
)
isnsControlNodeIscsiNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsControlNodeIscsiNodeName.setStatus("current")
_IsnsControlNodeIscsiIsRegistered_Type = TruthValue
_IsnsControlNodeIscsiIsRegistered_Object = MibTableColumn
isnsControlNodeIscsiIsRegistered = _IsnsControlNodeIscsiIsRegistered_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1, 1, 3),
    _IsnsControlNodeIscsiIsRegistered_Type()
)
isnsControlNodeIscsiIsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsControlNodeIscsiIsRegistered.setStatus("current")
_IsnsControlNodeIscsiRcvMgtSCN_Type = TruthValue
_IsnsControlNodeIscsiRcvMgtSCN_Object = MibTableColumn
isnsControlNodeIscsiRcvMgtSCN = _IsnsControlNodeIscsiRcvMgtSCN_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 1, 1, 4),
    _IsnsControlNodeIscsiRcvMgtSCN_Type()
)
isnsControlNodeIscsiRcvMgtSCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsControlNodeIscsiRcvMgtSCN.setStatus("current")
_IsnsControlNodeFcPortTable_Object = MibTable
isnsControlNodeFcPortTable = _IsnsControlNodeFcPortTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    isnsControlNodeFcPortTable.setStatus("current")
_IsnsControlNodeFcPortEntry_Object = MibTableRow
isnsControlNodeFcPortEntry = _IsnsControlNodeFcPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 2, 1)
)
isnsControlNodeFcPortEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsControlNodeFcPortWwpn"),
)
if mibBuilder.loadTexts:
    isnsControlNodeFcPortEntry.setStatus("current")


class _IsnsControlNodeFcPortWwpn_Type(FcNameIdOrZero):
    """Custom type isnsControlNodeFcPortWwpn based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IsnsControlNodeFcPortWwpn_Type.__name__ = "FcNameIdOrZero"
_IsnsControlNodeFcPortWwpn_Object = MibTableColumn
isnsControlNodeFcPortWwpn = _IsnsControlNodeFcPortWwpn_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 2, 1, 1),
    _IsnsControlNodeFcPortWwpn_Type()
)
isnsControlNodeFcPortWwpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsControlNodeFcPortWwpn.setStatus("current")
_IsnsControlNodeFcPortIsRegistered_Type = TruthValue
_IsnsControlNodeFcPortIsRegistered_Object = MibTableColumn
isnsControlNodeFcPortIsRegistered = _IsnsControlNodeFcPortIsRegistered_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 2, 1, 2),
    _IsnsControlNodeFcPortIsRegistered_Type()
)
isnsControlNodeFcPortIsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsControlNodeFcPortIsRegistered.setStatus("current")
_IsnsControlNodeFcPortRcvMgtSCN_Type = TruthValue
_IsnsControlNodeFcPortRcvMgtSCN_Object = MibTableColumn
isnsControlNodeFcPortRcvMgtSCN = _IsnsControlNodeFcPortRcvMgtSCN_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 3, 2, 1, 3),
    _IsnsControlNodeFcPortRcvMgtSCN_Type()
)
isnsControlNodeFcPortRcvMgtSCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsControlNodeFcPortRcvMgtSCN.setStatus("current")
_IsnsDdsInfo_ObjectIdentity = ObjectIdentity
isnsDdsInfo = _IsnsDdsInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 4)
)
_IsnsDdsTable_Object = MibTable
isnsDdsTable = _IsnsDdsTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    isnsDdsTable.setStatus("current")
_IsnsDdsEntry_Object = MibTableRow
isnsDdsEntry = _IsnsDdsEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 1, 1)
)
isnsDdsEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsDdsId"),
)
if mibBuilder.loadTexts:
    isnsDdsEntry.setStatus("current")
_IsnsDdsId_Type = IsnsDiscoveryDomainSetId
_IsnsDdsId_Object = MibTableColumn
isnsDdsId = _IsnsDdsId_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 1, 1, 1),
    _IsnsDdsId_Type()
)
isnsDdsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsDdsId.setStatus("current")
_IsnsDdsSymbolicName_Type = SnmpAdminString
_IsnsDdsSymbolicName_Object = MibTableColumn
isnsDdsSymbolicName = _IsnsDdsSymbolicName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 1, 1, 2),
    _IsnsDdsSymbolicName_Type()
)
isnsDdsSymbolicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdsSymbolicName.setStatus("current")
_IsnsDdsStatus_Type = IsnsDdsStatusType
_IsnsDdsStatus_Object = MibTableColumn
isnsDdsStatus = _IsnsDdsStatus_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 1, 1, 3),
    _IsnsDdsStatus_Type()
)
isnsDdsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdsStatus.setStatus("current")
_IsnsDdsMemberTable_Object = MibTable
isnsDdsMemberTable = _IsnsDdsMemberTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    isnsDdsMemberTable.setStatus("current")
_IsnsDdsMemberEntry_Object = MibTableRow
isnsDdsMemberEntry = _IsnsDdsMemberEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 2, 1)
)
isnsDdsMemberEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsDdsId"),
    (0, "ISNS-MIB", "isnsDdsMemberDdId"),
)
if mibBuilder.loadTexts:
    isnsDdsMemberEntry.setStatus("current")
_IsnsDdsMemberDdId_Type = IsnsDiscoveryDomainId
_IsnsDdsMemberDdId_Object = MibTableColumn
isnsDdsMemberDdId = _IsnsDdsMemberDdId_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 2, 1, 1),
    _IsnsDdsMemberDdId_Type()
)
isnsDdsMemberDdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsDdsMemberDdId.setStatus("current")
_IsnsDdsMemberSymbolicName_Type = SnmpAdminString
_IsnsDdsMemberSymbolicName_Object = MibTableColumn
isnsDdsMemberSymbolicName = _IsnsDdsMemberSymbolicName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 4, 2, 1, 2),
    _IsnsDdsMemberSymbolicName_Type()
)
isnsDdsMemberSymbolicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdsMemberSymbolicName.setStatus("current")
_IsnsDdInfo_ObjectIdentity = ObjectIdentity
isnsDdInfo = _IsnsDdInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5)
)
_IsnsDdTable_Object = MibTable
isnsDdTable = _IsnsDdTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    isnsDdTable.setStatus("current")
_IsnsDdEntry_Object = MibTableRow
isnsDdEntry = _IsnsDdEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 1, 1)
)
isnsDdEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsDdId"),
)
if mibBuilder.loadTexts:
    isnsDdEntry.setStatus("current")
_IsnsDdId_Type = IsnsDiscoveryDomainId
_IsnsDdId_Object = MibTableColumn
isnsDdId = _IsnsDdId_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 1, 1, 1),
    _IsnsDdId_Type()
)
isnsDdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsDdId.setStatus("current")
_IsnsDdSymbolicName_Type = SnmpAdminString
_IsnsDdSymbolicName_Object = MibTableColumn
isnsDdSymbolicName = _IsnsDdSymbolicName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 1, 1, 2),
    _IsnsDdSymbolicName_Type()
)
isnsDdSymbolicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdSymbolicName.setStatus("current")
_IsnsDdFeatures_Type = IsnsDdFeatureType
_IsnsDdFeatures_Object = MibTableColumn
isnsDdFeatures = _IsnsDdFeatures_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 1, 1, 3),
    _IsnsDdFeatures_Type()
)
isnsDdFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdFeatures.setStatus("current")
_IsnsDdIscsiMemberTable_Object = MibTable
isnsDdIscsiMemberTable = _IsnsDdIscsiMemberTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    isnsDdIscsiMemberTable.setStatus("current")
_IsnsDdIscsiMemberEntry_Object = MibTableRow
isnsDdIscsiMemberEntry = _IsnsDdIscsiMemberEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 2, 1)
)
isnsDdIscsiMemberEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsDdId"),
    (0, "ISNS-MIB", "isnsDdIscsiMemberIndex"),
)
if mibBuilder.loadTexts:
    isnsDdIscsiMemberEntry.setStatus("current")
_IsnsDdIscsiMemberIndex_Type = IsnsNodeIndexId
_IsnsDdIscsiMemberIndex_Object = MibTableColumn
isnsDdIscsiMemberIndex = _IsnsDdIscsiMemberIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 2, 1, 1),
    _IsnsDdIscsiMemberIndex_Type()
)
isnsDdIscsiMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsDdIscsiMemberIndex.setStatus("current")


class _IsnsDdIscsiMemberName_Type(SnmpAdminString):
    """Custom type isnsDdIscsiMemberName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_IsnsDdIscsiMemberName_Type.__name__ = "SnmpAdminString"
_IsnsDdIscsiMemberName_Object = MibTableColumn
isnsDdIscsiMemberName = _IsnsDdIscsiMemberName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 2, 1, 2),
    _IsnsDdIscsiMemberName_Type()
)
isnsDdIscsiMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdIscsiMemberName.setStatus("current")
_IsnsDdIscsiMemberIsRegistered_Type = TruthValue
_IsnsDdIscsiMemberIsRegistered_Object = MibTableColumn
isnsDdIscsiMemberIsRegistered = _IsnsDdIscsiMemberIsRegistered_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 2, 1, 3),
    _IsnsDdIscsiMemberIsRegistered_Type()
)
isnsDdIscsiMemberIsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdIscsiMemberIsRegistered.setStatus("current")
_IsnsDdPortalMemberTable_Object = MibTable
isnsDdPortalMemberTable = _IsnsDdPortalMemberTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    isnsDdPortalMemberTable.setStatus("current")
_IsnsDdPortalMemberEntry_Object = MibTableRow
isnsDdPortalMemberEntry = _IsnsDdPortalMemberEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1)
)
isnsDdPortalMemberEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsDdId"),
    (0, "ISNS-MIB", "isnsDdPortalMemberIndex"),
)
if mibBuilder.loadTexts:
    isnsDdPortalMemberEntry.setStatus("current")
_IsnsDdPortalMemberIndex_Type = IsnsPortalIndexId
_IsnsDdPortalMemberIndex_Object = MibTableColumn
isnsDdPortalMemberIndex = _IsnsDdPortalMemberIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 1),
    _IsnsDdPortalMemberIndex_Type()
)
isnsDdPortalMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsDdPortalMemberIndex.setStatus("current")
_IsnsDdPortalMemberAddressType_Type = InetAddressType
_IsnsDdPortalMemberAddressType_Object = MibTableColumn
isnsDdPortalMemberAddressType = _IsnsDdPortalMemberAddressType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 2),
    _IsnsDdPortalMemberAddressType_Type()
)
isnsDdPortalMemberAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdPortalMemberAddressType.setStatus("current")
_IsnsDdPortalMemberAddress_Type = InetAddress
_IsnsDdPortalMemberAddress_Object = MibTableColumn
isnsDdPortalMemberAddress = _IsnsDdPortalMemberAddress_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 3),
    _IsnsDdPortalMemberAddress_Type()
)
isnsDdPortalMemberAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdPortalMemberAddress.setStatus("current")
_IsnsDdPortalMemberPortType_Type = IsnsPortalPortTypeId
_IsnsDdPortalMemberPortType_Object = MibTableColumn
isnsDdPortalMemberPortType = _IsnsDdPortalMemberPortType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 4),
    _IsnsDdPortalMemberPortType_Type()
)
isnsDdPortalMemberPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdPortalMemberPortType.setStatus("current")


class _IsnsDdPortalMemberPort_Type(InetPortNumber):
    """Custom type isnsDdPortalMemberPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsnsDdPortalMemberPort_Type.__name__ = "InetPortNumber"
_IsnsDdPortalMemberPort_Object = MibTableColumn
isnsDdPortalMemberPort = _IsnsDdPortalMemberPort_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 5),
    _IsnsDdPortalMemberPort_Type()
)
isnsDdPortalMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdPortalMemberPort.setStatus("current")
_IsnsDdPortalMemberIsRegistered_Type = TruthValue
_IsnsDdPortalMemberIsRegistered_Object = MibTableColumn
isnsDdPortalMemberIsRegistered = _IsnsDdPortalMemberIsRegistered_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 3, 1, 6),
    _IsnsDdPortalMemberIsRegistered_Type()
)
isnsDdPortalMemberIsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdPortalMemberIsRegistered.setStatus("current")
_IsnsDdFcPortMemberTable_Object = MibTable
isnsDdFcPortMemberTable = _IsnsDdFcPortMemberTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    isnsDdFcPortMemberTable.setStatus("current")
_IsnsDdFcPortMemberEntry_Object = MibTableRow
isnsDdFcPortMemberEntry = _IsnsDdFcPortMemberEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 4, 1)
)
isnsDdFcPortMemberEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsDdId"),
    (0, "ISNS-MIB", "isnsDdFcPortMemberPortName"),
)
if mibBuilder.loadTexts:
    isnsDdFcPortMemberEntry.setStatus("current")


class _IsnsDdFcPortMemberPortName_Type(FcNameIdOrZero):
    """Custom type isnsDdFcPortMemberPortName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IsnsDdFcPortMemberPortName_Type.__name__ = "FcNameIdOrZero"
_IsnsDdFcPortMemberPortName_Object = MibTableColumn
isnsDdFcPortMemberPortName = _IsnsDdFcPortMemberPortName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 4, 1, 1),
    _IsnsDdFcPortMemberPortName_Type()
)
isnsDdFcPortMemberPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsDdFcPortMemberPortName.setStatus("current")
_IsnsDdFcPortMemberIsRegistered_Type = TruthValue
_IsnsDdFcPortMemberIsRegistered_Object = MibTableColumn
isnsDdFcPortMemberIsRegistered = _IsnsDdFcPortMemberIsRegistered_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 5, 4, 1, 2),
    _IsnsDdFcPortMemberIsRegistered_Type()
)
isnsDdFcPortMemberIsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsDdFcPortMemberIsRegistered.setStatus("current")
_IsnsReg_ObjectIdentity = ObjectIdentity
isnsReg = _IsnsReg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6)
)
_IsnsRegEntityInfo_ObjectIdentity = ObjectIdentity
isnsRegEntityInfo = _IsnsRegEntityInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1)
)
_IsnsRegEntityTable_Object = MibTable
isnsRegEntityTable = _IsnsRegEntityTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    isnsRegEntityTable.setStatus("current")
_IsnsRegEntityEntry_Object = MibTableRow
isnsRegEntityEntry = _IsnsRegEntityEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1)
)
isnsRegEntityEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsRegEntityIndex"),
)
if mibBuilder.loadTexts:
    isnsRegEntityEntry.setStatus("current")


class _IsnsRegEntityIndex_Type(IsnsEntityIndexIdOrZero):
    """Custom type isnsRegEntityIndex based on IsnsEntityIndexIdOrZero"""
    subtypeSpec = IsnsEntityIndexIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IsnsRegEntityIndex_Type.__name__ = "IsnsEntityIndexIdOrZero"
_IsnsRegEntityIndex_Object = MibTableColumn
isnsRegEntityIndex = _IsnsRegEntityIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 1),
    _IsnsRegEntityIndex_Type()
)
isnsRegEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsRegEntityIndex.setStatus("current")
_IsnsRegEntityEID_Type = SnmpAdminString
_IsnsRegEntityEID_Object = MibTableColumn
isnsRegEntityEID = _IsnsRegEntityEID_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 2),
    _IsnsRegEntityEID_Type()
)
isnsRegEntityEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityEID.setStatus("current")


class _IsnsRegEntityProtocol_Type(Unsigned32):
    """Custom type isnsRegEntityProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IsnsRegEntityProtocol_Type.__name__ = "Unsigned32"
_IsnsRegEntityProtocol_Object = MibTableColumn
isnsRegEntityProtocol = _IsnsRegEntityProtocol_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 3),
    _IsnsRegEntityProtocol_Type()
)
isnsRegEntityProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityProtocol.setStatus("current")
_IsnsRegEntityManagementAddressType_Type = InetAddressType
_IsnsRegEntityManagementAddressType_Object = MibTableColumn
isnsRegEntityManagementAddressType = _IsnsRegEntityManagementAddressType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 4),
    _IsnsRegEntityManagementAddressType_Type()
)
isnsRegEntityManagementAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityManagementAddressType.setStatus("current")
_IsnsRegEntityManagementAddress_Type = InetAddress
_IsnsRegEntityManagementAddress_Object = MibTableColumn
isnsRegEntityManagementAddress = _IsnsRegEntityManagementAddress_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 5),
    _IsnsRegEntityManagementAddress_Type()
)
isnsRegEntityManagementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityManagementAddress.setStatus("current")
_IsnsRegEntityTimestamp_Type = TimeStamp
_IsnsRegEntityTimestamp_Object = MibTableColumn
isnsRegEntityTimestamp = _IsnsRegEntityTimestamp_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 6),
    _IsnsRegEntityTimestamp_Type()
)
isnsRegEntityTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityTimestamp.setStatus("current")


class _IsnsRegEntityVersionMin_Type(Unsigned32):
    """Custom type isnsRegEntityVersionMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
        ValueRangeConstraint(255, 255),
    )


_IsnsRegEntityVersionMin_Type.__name__ = "Unsigned32"
_IsnsRegEntityVersionMin_Object = MibTableColumn
isnsRegEntityVersionMin = _IsnsRegEntityVersionMin_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 7),
    _IsnsRegEntityVersionMin_Type()
)
isnsRegEntityVersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityVersionMin.setStatus("current")


class _IsnsRegEntityVersionMax_Type(Unsigned32):
    """Custom type isnsRegEntityVersionMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
        ValueRangeConstraint(255, 255),
    )


_IsnsRegEntityVersionMax_Type.__name__ = "Unsigned32"
_IsnsRegEntityVersionMax_Object = MibTableColumn
isnsRegEntityVersionMax = _IsnsRegEntityVersionMax_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 8),
    _IsnsRegEntityVersionMax_Type()
)
isnsRegEntityVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityVersionMax.setStatus("current")


class _IsnsRegEntityRegistrationPeriod_Type(Unsigned32):
    """Custom type isnsRegEntityRegistrationPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsRegEntityRegistrationPeriod_Type.__name__ = "Unsigned32"
_IsnsRegEntityRegistrationPeriod_Object = MibTableColumn
isnsRegEntityRegistrationPeriod = _IsnsRegEntityRegistrationPeriod_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 1, 1, 9),
    _IsnsRegEntityRegistrationPeriod_Type()
)
isnsRegEntityRegistrationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityRegistrationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    isnsRegEntityRegistrationPeriod.setUnits("seconds")
_IsnsRegEntityNumObjectsTable_Object = MibTable
isnsRegEntityNumObjectsTable = _IsnsRegEntityNumObjectsTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    isnsRegEntityNumObjectsTable.setStatus("current")
_IsnsRegEntityNumObjectsEntry_Object = MibTableRow
isnsRegEntityNumObjectsEntry = _IsnsRegEntityNumObjectsEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1)
)
isnsRegEntityNumObjectsEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsRegEntityIndex"),
)
if mibBuilder.loadTexts:
    isnsRegEntityNumObjectsEntry.setStatus("current")


class _IsnsRegEntityInfoNumPortals_Type(Gauge32):
    """Custom type isnsRegEntityInfoNumPortals based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsRegEntityInfoNumPortals_Type.__name__ = "Gauge32"
_IsnsRegEntityInfoNumPortals_Object = MibTableColumn
isnsRegEntityInfoNumPortals = _IsnsRegEntityInfoNumPortals_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1, 1),
    _IsnsRegEntityInfoNumPortals_Type()
)
isnsRegEntityInfoNumPortals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityInfoNumPortals.setStatus("current")


class _IsnsRegEntityInfoNumPortalGroups_Type(Gauge32):
    """Custom type isnsRegEntityInfoNumPortalGroups based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsRegEntityInfoNumPortalGroups_Type.__name__ = "Gauge32"
_IsnsRegEntityInfoNumPortalGroups_Object = MibTableColumn
isnsRegEntityInfoNumPortalGroups = _IsnsRegEntityInfoNumPortalGroups_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1, 2),
    _IsnsRegEntityInfoNumPortalGroups_Type()
)
isnsRegEntityInfoNumPortalGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityInfoNumPortalGroups.setStatus("current")


class _IsnsRegEntityInfoNumIscsiNodes_Type(Gauge32):
    """Custom type isnsRegEntityInfoNumIscsiNodes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsRegEntityInfoNumIscsiNodes_Type.__name__ = "Gauge32"
_IsnsRegEntityInfoNumIscsiNodes_Object = MibTableColumn
isnsRegEntityInfoNumIscsiNodes = _IsnsRegEntityInfoNumIscsiNodes_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1, 3),
    _IsnsRegEntityInfoNumIscsiNodes_Type()
)
isnsRegEntityInfoNumIscsiNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityInfoNumIscsiNodes.setStatus("current")


class _IsnsRegEntityInfoNumFcPorts_Type(Gauge32):
    """Custom type isnsRegEntityInfoNumFcPorts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsRegEntityInfoNumFcPorts_Type.__name__ = "Gauge32"
_IsnsRegEntityInfoNumFcPorts_Object = MibTableColumn
isnsRegEntityInfoNumFcPorts = _IsnsRegEntityInfoNumFcPorts_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1, 4),
    _IsnsRegEntityInfoNumFcPorts_Type()
)
isnsRegEntityInfoNumFcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityInfoNumFcPorts.setStatus("current")


class _IsnsRegEntityInfoNumFcNodes_Type(Gauge32):
    """Custom type isnsRegEntityInfoNumFcNodes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsRegEntityInfoNumFcNodes_Type.__name__ = "Gauge32"
_IsnsRegEntityInfoNumFcNodes_Object = MibTableColumn
isnsRegEntityInfoNumFcNodes = _IsnsRegEntityInfoNumFcNodes_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 1, 2, 1, 5),
    _IsnsRegEntityInfoNumFcNodes_Type()
)
isnsRegEntityInfoNumFcNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegEntityInfoNumFcNodes.setStatus("current")
_IsnsRegPortalInfo_ObjectIdentity = ObjectIdentity
isnsRegPortalInfo = _IsnsRegPortalInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2)
)
_IsnsRegPortalTable_Object = MibTable
isnsRegPortalTable = _IsnsRegPortalTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    isnsRegPortalTable.setStatus("current")
_IsnsRegPortalEntry_Object = MibTableRow
isnsRegPortalEntry = _IsnsRegPortalEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1)
)
isnsRegPortalEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsRegEntityIndex"),
    (0, "ISNS-MIB", "isnsRegPortalPortalIndex"),
)
if mibBuilder.loadTexts:
    isnsRegPortalEntry.setStatus("current")
_IsnsRegPortalPortalIndex_Type = IsnsPortalIndexId
_IsnsRegPortalPortalIndex_Object = MibTableColumn
isnsRegPortalPortalIndex = _IsnsRegPortalPortalIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 1),
    _IsnsRegPortalPortalIndex_Type()
)
isnsRegPortalPortalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsRegPortalPortalIndex.setStatus("current")
_IsnsRegPortalAddressType_Type = InetAddressType
_IsnsRegPortalAddressType_Object = MibTableColumn
isnsRegPortalAddressType = _IsnsRegPortalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 2),
    _IsnsRegPortalAddressType_Type()
)
isnsRegPortalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalAddressType.setStatus("current")
_IsnsRegPortalAddress_Type = InetAddress
_IsnsRegPortalAddress_Object = MibTableColumn
isnsRegPortalAddress = _IsnsRegPortalAddress_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 3),
    _IsnsRegPortalAddress_Type()
)
isnsRegPortalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalAddress.setStatus("current")
_IsnsRegPortalPortType_Type = IsnsPortalPortTypeId
_IsnsRegPortalPortType_Object = MibTableColumn
isnsRegPortalPortType = _IsnsRegPortalPortType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 4),
    _IsnsRegPortalPortType_Type()
)
isnsRegPortalPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalPortType.setStatus("current")


class _IsnsRegPortalPort_Type(InetPortNumber):
    """Custom type isnsRegPortalPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsnsRegPortalPort_Type.__name__ = "InetPortNumber"
_IsnsRegPortalPort_Object = MibTableColumn
isnsRegPortalPort = _IsnsRegPortalPort_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 5),
    _IsnsRegPortalPort_Type()
)
isnsRegPortalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalPort.setStatus("current")
_IsnsRegPortalSymbolicName_Type = SnmpAdminString
_IsnsRegPortalSymbolicName_Object = MibTableColumn
isnsRegPortalSymbolicName = _IsnsRegPortalSymbolicName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 6),
    _IsnsRegPortalSymbolicName_Type()
)
isnsRegPortalSymbolicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalSymbolicName.setStatus("current")


class _IsnsRegPortalEsiInterval_Type(Unsigned32):
    """Custom type isnsRegPortalEsiInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsnsRegPortalEsiInterval_Type.__name__ = "Unsigned32"
_IsnsRegPortalEsiInterval_Object = MibTableColumn
isnsRegPortalEsiInterval = _IsnsRegPortalEsiInterval_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 7),
    _IsnsRegPortalEsiInterval_Type()
)
isnsRegPortalEsiInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalEsiInterval.setStatus("current")
if mibBuilder.loadTexts:
    isnsRegPortalEsiInterval.setUnits("seconds")
_IsnsRegPortalEsiPortType_Type = IsnsPortalPortTypeId
_IsnsRegPortalEsiPortType_Object = MibTableColumn
isnsRegPortalEsiPortType = _IsnsRegPortalEsiPortType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 8),
    _IsnsRegPortalEsiPortType_Type()
)
isnsRegPortalEsiPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalEsiPortType.setStatus("current")
_IsnsRegPortalEsiPort_Type = InetPortNumber
_IsnsRegPortalEsiPort_Object = MibTableColumn
isnsRegPortalEsiPort = _IsnsRegPortalEsiPort_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 9),
    _IsnsRegPortalEsiPort_Type()
)
isnsRegPortalEsiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalEsiPort.setStatus("current")
_IsnsRegPortalScnPortType_Type = IsnsPortalPortTypeId
_IsnsRegPortalScnPortType_Object = MibTableColumn
isnsRegPortalScnPortType = _IsnsRegPortalScnPortType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 10),
    _IsnsRegPortalScnPortType_Type()
)
isnsRegPortalScnPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalScnPortType.setStatus("current")
_IsnsRegPortalScnPort_Type = InetPortNumber
_IsnsRegPortalScnPort_Object = MibTableColumn
isnsRegPortalScnPort = _IsnsRegPortalScnPort_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 11),
    _IsnsRegPortalScnPort_Type()
)
isnsRegPortalScnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalScnPort.setStatus("current")
_IsnsRegPortalSecurityInfo_Type = IsnsPortalSecurityType
_IsnsRegPortalSecurityInfo_Object = MibTableColumn
isnsRegPortalSecurityInfo = _IsnsRegPortalSecurityInfo_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 2, 1, 1, 12),
    _IsnsRegPortalSecurityInfo_Type()
)
isnsRegPortalSecurityInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPortalSecurityInfo.setStatus("current")
_IsnsRegPortalGroupInfo_ObjectIdentity = ObjectIdentity
isnsRegPortalGroupInfo = _IsnsRegPortalGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3)
)
_IsnsRegPgTable_Object = MibTable
isnsRegPgTable = _IsnsRegPgTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    isnsRegPgTable.setStatus("current")
_IsnsRegPgEntry_Object = MibTableRow
isnsRegPgEntry = _IsnsRegPgEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1)
)
isnsRegPgEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsRegEntityIndex"),
    (0, "ISNS-MIB", "isnsRegPgIndex"),
)
if mibBuilder.loadTexts:
    isnsRegPgEntry.setStatus("current")
_IsnsRegPgIndex_Type = IsnsPortalGroupIndexId
_IsnsRegPgIndex_Object = MibTableColumn
isnsRegPgIndex = _IsnsRegPgIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 1),
    _IsnsRegPgIndex_Type()
)
isnsRegPgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsRegPgIndex.setStatus("current")
_IsnsRegPgIscsiNodeIndex_Type = IsnsNodeIndexId
_IsnsRegPgIscsiNodeIndex_Object = MibTableColumn
isnsRegPgIscsiNodeIndex = _IsnsRegPgIscsiNodeIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 2),
    _IsnsRegPgIscsiNodeIndex_Type()
)
isnsRegPgIscsiNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPgIscsiNodeIndex.setStatus("current")


class _IsnsRegPgIscsiName_Type(SnmpAdminString):
    """Custom type isnsRegPgIscsiName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_IsnsRegPgIscsiName_Type.__name__ = "SnmpAdminString"
_IsnsRegPgIscsiName_Object = MibTableColumn
isnsRegPgIscsiName = _IsnsRegPgIscsiName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 3),
    _IsnsRegPgIscsiName_Type()
)
isnsRegPgIscsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPgIscsiName.setStatus("current")
_IsnsRegPgPortalPortalIndex_Type = IsnsPortalIndexId
_IsnsRegPgPortalPortalIndex_Object = MibTableColumn
isnsRegPgPortalPortalIndex = _IsnsRegPgPortalPortalIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 4),
    _IsnsRegPgPortalPortalIndex_Type()
)
isnsRegPgPortalPortalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPgPortalPortalIndex.setStatus("current")
_IsnsRegPgPortalAddressType_Type = InetAddressType
_IsnsRegPgPortalAddressType_Object = MibTableColumn
isnsRegPgPortalAddressType = _IsnsRegPgPortalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 5),
    _IsnsRegPgPortalAddressType_Type()
)
isnsRegPgPortalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPgPortalAddressType.setStatus("current")
_IsnsRegPgPortalAddress_Type = InetAddress
_IsnsRegPgPortalAddress_Object = MibTableColumn
isnsRegPgPortalAddress = _IsnsRegPgPortalAddress_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 6),
    _IsnsRegPgPortalAddress_Type()
)
isnsRegPgPortalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPgPortalAddress.setStatus("current")
_IsnsRegPgPortalPortType_Type = IsnsPortalPortTypeId
_IsnsRegPgPortalPortType_Object = MibTableColumn
isnsRegPgPortalPortType = _IsnsRegPgPortalPortType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 7),
    _IsnsRegPgPortalPortType_Type()
)
isnsRegPgPortalPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPgPortalPortType.setStatus("current")


class _IsnsRegPgPortalPort_Type(InetPortNumber):
    """Custom type isnsRegPgPortalPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsnsRegPgPortalPort_Type.__name__ = "InetPortNumber"
_IsnsRegPgPortalPort_Object = MibTableColumn
isnsRegPgPortalPort = _IsnsRegPgPortalPort_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 8),
    _IsnsRegPgPortalPort_Type()
)
isnsRegPgPortalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPgPortalPort.setStatus("current")
_IsnsRegPgPGT_Type = IsnsPortalGroupTagIdOrNull
_IsnsRegPgPGT_Object = MibTableColumn
isnsRegPgPGT = _IsnsRegPgPGT_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 3, 1, 1, 9),
    _IsnsRegPgPGT_Type()
)
isnsRegPgPGT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegPgPGT.setStatus("current")
_IsnsRegIscsiNodeInfo_ObjectIdentity = ObjectIdentity
isnsRegIscsiNodeInfo = _IsnsRegIscsiNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4)
)
_IsnsRegIscsiNodeTable_Object = MibTable
isnsRegIscsiNodeTable = _IsnsRegIscsiNodeTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    isnsRegIscsiNodeTable.setStatus("current")
_IsnsRegIscsiNodeEntry_Object = MibTableRow
isnsRegIscsiNodeEntry = _IsnsRegIscsiNodeEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1)
)
isnsRegIscsiNodeEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsRegEntityIndex"),
    (0, "ISNS-MIB", "isnsRegIscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    isnsRegIscsiNodeEntry.setStatus("current")
_IsnsRegIscsiNodeIndex_Type = IsnsNodeIndexId
_IsnsRegIscsiNodeIndex_Object = MibTableColumn
isnsRegIscsiNodeIndex = _IsnsRegIscsiNodeIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 1),
    _IsnsRegIscsiNodeIndex_Type()
)
isnsRegIscsiNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsRegIscsiNodeIndex.setStatus("current")


class _IsnsRegIscsiNodeName_Type(SnmpAdminString):
    """Custom type isnsRegIscsiNodeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_IsnsRegIscsiNodeName_Type.__name__ = "SnmpAdminString"
_IsnsRegIscsiNodeName_Object = MibTableColumn
isnsRegIscsiNodeName = _IsnsRegIscsiNodeName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 2),
    _IsnsRegIscsiNodeName_Type()
)
isnsRegIscsiNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegIscsiNodeName.setStatus("current")
_IsnsRegIscsiNodeType_Type = IsnsIscsiNodeType
_IsnsRegIscsiNodeType_Object = MibTableColumn
isnsRegIscsiNodeType = _IsnsRegIscsiNodeType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 3),
    _IsnsRegIscsiNodeType_Type()
)
isnsRegIscsiNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegIscsiNodeType.setStatus("current")
_IsnsRegIscsiNodeAlias_Type = SnmpAdminString
_IsnsRegIscsiNodeAlias_Object = MibTableColumn
isnsRegIscsiNodeAlias = _IsnsRegIscsiNodeAlias_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 4),
    _IsnsRegIscsiNodeAlias_Type()
)
isnsRegIscsiNodeAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegIscsiNodeAlias.setStatus("current")
_IsnsRegIscsiNodeScnTypes_Type = IsnsIscsiScnType
_IsnsRegIscsiNodeScnTypes_Object = MibTableColumn
isnsRegIscsiNodeScnTypes = _IsnsRegIscsiNodeScnTypes_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 5),
    _IsnsRegIscsiNodeScnTypes_Type()
)
isnsRegIscsiNodeScnTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegIscsiNodeScnTypes.setStatus("current")
_IsnsRegIscsiNodeWwnToken_Type = FcNameIdOrZero
_IsnsRegIscsiNodeWwnToken_Object = MibTableColumn
isnsRegIscsiNodeWwnToken = _IsnsRegIscsiNodeWwnToken_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 6),
    _IsnsRegIscsiNodeWwnToken_Type()
)
isnsRegIscsiNodeWwnToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegIscsiNodeWwnToken.setStatus("current")
_IsnsRegIscsiNodeAuthMethod_Type = SnmpAdminString
_IsnsRegIscsiNodeAuthMethod_Object = MibTableColumn
isnsRegIscsiNodeAuthMethod = _IsnsRegIscsiNodeAuthMethod_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 4, 1, 1, 7),
    _IsnsRegIscsiNodeAuthMethod_Type()
)
isnsRegIscsiNodeAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegIscsiNodeAuthMethod.setStatus("current")
_IsnsRegFcNodeInfo_ObjectIdentity = ObjectIdentity
isnsRegFcNodeInfo = _IsnsRegFcNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5)
)
_IsnsRegFcNodeTable_Object = MibTable
isnsRegFcNodeTable = _IsnsRegFcNodeTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    isnsRegFcNodeTable.setStatus("current")
_IsnsRegFcNodeEntry_Object = MibTableRow
isnsRegFcNodeEntry = _IsnsRegFcNodeEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1)
)
isnsRegFcNodeEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsRegFcNodeWwnn"),
)
if mibBuilder.loadTexts:
    isnsRegFcNodeEntry.setStatus("current")


class _IsnsRegFcNodeWwnn_Type(FcNameIdOrZero):
    """Custom type isnsRegFcNodeWwnn based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IsnsRegFcNodeWwnn_Type.__name__ = "FcNameIdOrZero"
_IsnsRegFcNodeWwnn_Object = MibTableColumn
isnsRegFcNodeWwnn = _IsnsRegFcNodeWwnn_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 1),
    _IsnsRegFcNodeWwnn_Type()
)
isnsRegFcNodeWwnn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsRegFcNodeWwnn.setStatus("current")
_IsnsRegFcNodeSymbolicName_Type = SnmpAdminString
_IsnsRegFcNodeSymbolicName_Object = MibTableColumn
isnsRegFcNodeSymbolicName = _IsnsRegFcNodeSymbolicName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 2),
    _IsnsRegFcNodeSymbolicName_Type()
)
isnsRegFcNodeSymbolicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcNodeSymbolicName.setStatus("current")
_IsnsRegFcNodeAddressType_Type = InetAddressType
_IsnsRegFcNodeAddressType_Object = MibTableColumn
isnsRegFcNodeAddressType = _IsnsRegFcNodeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 3),
    _IsnsRegFcNodeAddressType_Type()
)
isnsRegFcNodeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcNodeAddressType.setStatus("current")
_IsnsRegFcNodeAddress_Type = InetAddress
_IsnsRegFcNodeAddress_Object = MibTableColumn
isnsRegFcNodeAddress = _IsnsRegFcNodeAddress_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 4),
    _IsnsRegFcNodeAddress_Type()
)
isnsRegFcNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcNodeAddress.setStatus("current")


class _IsnsRegFcNodeIPA_Type(OctetString):
    """Custom type isnsRegFcNodeIPA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IsnsRegFcNodeIPA_Type.__name__ = "OctetString"
_IsnsRegFcNodeIPA_Object = MibTableColumn
isnsRegFcNodeIPA = _IsnsRegFcNodeIPA_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 5),
    _IsnsRegFcNodeIPA_Type()
)
isnsRegFcNodeIPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcNodeIPA.setStatus("current")


class _IsnsRegFcNodeProxyIscsiName_Type(SnmpAdminString):
    """Custom type isnsRegFcNodeProxyIscsiName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_IsnsRegFcNodeProxyIscsiName_Type.__name__ = "SnmpAdminString"
_IsnsRegFcNodeProxyIscsiName_Object = MibTableColumn
isnsRegFcNodeProxyIscsiName = _IsnsRegFcNodeProxyIscsiName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 6),
    _IsnsRegFcNodeProxyIscsiName_Type()
)
isnsRegFcNodeProxyIscsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcNodeProxyIscsiName.setStatus("current")


class _IsnsRegFcNodeNumFcPorts_Type(Gauge32):
    """Custom type isnsRegFcNodeNumFcPorts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IsnsRegFcNodeNumFcPorts_Type.__name__ = "Gauge32"
_IsnsRegFcNodeNumFcPorts_Object = MibTableColumn
isnsRegFcNodeNumFcPorts = _IsnsRegFcNodeNumFcPorts_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 1, 1, 7),
    _IsnsRegFcNodeNumFcPorts_Type()
)
isnsRegFcNodeNumFcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcNodeNumFcPorts.setStatus("current")
_IsnsRegFcPortTable_Object = MibTable
isnsRegFcPortTable = _IsnsRegFcPortTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    isnsRegFcPortTable.setStatus("current")
_IsnsRegFcPortEntry_Object = MibTableRow
isnsRegFcPortEntry = _IsnsRegFcPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1)
)
isnsRegFcPortEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsRegEntityIndex"),
    (0, "ISNS-MIB", "isnsRegFcPortWwpn"),
)
if mibBuilder.loadTexts:
    isnsRegFcPortEntry.setStatus("current")


class _IsnsRegFcPortWwpn_Type(FcNameIdOrZero):
    """Custom type isnsRegFcPortWwpn based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IsnsRegFcPortWwpn_Type.__name__ = "FcNameIdOrZero"
_IsnsRegFcPortWwpn_Object = MibTableColumn
isnsRegFcPortWwpn = _IsnsRegFcPortWwpn_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 1),
    _IsnsRegFcPortWwpn_Type()
)
isnsRegFcPortWwpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isnsRegFcPortWwpn.setStatus("current")
_IsnsRegFcPortID_Type = FcAddressIdOrZero
_IsnsRegFcPortID_Object = MibTableColumn
isnsRegFcPortID = _IsnsRegFcPortID_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 2),
    _IsnsRegFcPortID_Type()
)
isnsRegFcPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortID.setStatus("current")


class _IsnsRegFcPortType_Type(Unsigned32):
    """Custom type isnsRegFcPortType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsnsRegFcPortType_Type.__name__ = "Unsigned32"
_IsnsRegFcPortType_Object = MibTableColumn
isnsRegFcPortType = _IsnsRegFcPortType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 3),
    _IsnsRegFcPortType_Type()
)
isnsRegFcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortType.setStatus("current")
_IsnsRegFcPortSymbolicName_Type = SnmpAdminString
_IsnsRegFcPortSymbolicName_Object = MibTableColumn
isnsRegFcPortSymbolicName = _IsnsRegFcPortSymbolicName_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 4),
    _IsnsRegFcPortSymbolicName_Type()
)
isnsRegFcPortSymbolicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortSymbolicName.setStatus("current")
_IsnsRegFcPortFabricPortWwn_Type = FcNameIdOrZero
_IsnsRegFcPortFabricPortWwn_Object = MibTableColumn
isnsRegFcPortFabricPortWwn = _IsnsRegFcPortFabricPortWwn_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 5),
    _IsnsRegFcPortFabricPortWwn_Type()
)
isnsRegFcPortFabricPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortFabricPortWwn.setStatus("current")
_IsnsRegFcPortHA_Type = FcAddressIdOrZero
_IsnsRegFcPortHA_Object = MibTableColumn
isnsRegFcPortHA = _IsnsRegFcPortHA_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 6),
    _IsnsRegFcPortHA_Type()
)
isnsRegFcPortHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortHA.setStatus("current")
_IsnsRegFcPortAddressType_Type = InetAddressType
_IsnsRegFcPortAddressType_Object = MibTableColumn
isnsRegFcPortAddressType = _IsnsRegFcPortAddressType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 7),
    _IsnsRegFcPortAddressType_Type()
)
isnsRegFcPortAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortAddressType.setStatus("current")
_IsnsRegFcPortAddress_Type = InetAddress
_IsnsRegFcPortAddress_Object = MibTableColumn
isnsRegFcPortAddress = _IsnsRegFcPortAddress_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 8),
    _IsnsRegFcPortAddress_Type()
)
isnsRegFcPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortAddress.setStatus("current")
_IsnsRegFcPortFcCos_Type = IsnsFcClassOfServiceType
_IsnsRegFcPortFcCos_Object = MibTableColumn
isnsRegFcPortFcCos = _IsnsRegFcPortFcCos_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 9),
    _IsnsRegFcPortFcCos_Type()
)
isnsRegFcPortFcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortFcCos.setStatus("current")


class _IsnsRegFcPortFc4Types_Type(OctetString):
    """Custom type isnsRegFcPortFc4Types based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_IsnsRegFcPortFc4Types_Type.__name__ = "OctetString"
_IsnsRegFcPortFc4Types_Object = MibTableColumn
isnsRegFcPortFc4Types = _IsnsRegFcPortFc4Types_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 10),
    _IsnsRegFcPortFc4Types_Type()
)
isnsRegFcPortFc4Types.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortFc4Types.setStatus("current")


class _IsnsRegFcPortFc4Descr_Type(SnmpAdminString):
    """Custom type isnsRegFcPortFc4Descr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 255),
    )


_IsnsRegFcPortFc4Descr_Type.__name__ = "SnmpAdminString"
_IsnsRegFcPortFc4Descr_Object = MibTableColumn
isnsRegFcPortFc4Descr = _IsnsRegFcPortFc4Descr_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 11),
    _IsnsRegFcPortFc4Descr_Type()
)
isnsRegFcPortFc4Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortFc4Descr.setStatus("current")


class _IsnsRegFcPortFc4Features_Type(OctetString):
    """Custom type isnsRegFcPortFc4Features based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_IsnsRegFcPortFc4Features_Type.__name__ = "OctetString"
_IsnsRegFcPortFc4Features_Object = MibTableColumn
isnsRegFcPortFc4Features = _IsnsRegFcPortFc4Features_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 12),
    _IsnsRegFcPortFc4Features_Type()
)
isnsRegFcPortFc4Features.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortFc4Features.setStatus("current")
_IsnsRegFcPortScnTypes_Type = IsnsIfcpScnType
_IsnsRegFcPortScnTypes_Object = MibTableColumn
isnsRegFcPortScnTypes = _IsnsRegFcPortScnTypes_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 13),
    _IsnsRegFcPortScnTypes_Type()
)
isnsRegFcPortScnTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortScnTypes.setStatus("current")
_IsnsRegFcPortRole_Type = IsnsFcPortRoleType
_IsnsRegFcPortRole_Object = MibTableColumn
isnsRegFcPortRole = _IsnsRegFcPortRole_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 14),
    _IsnsRegFcPortRole_Type()
)
isnsRegFcPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortRole.setStatus("current")
_IsnsRegFcPortFcNodeWwnn_Type = FcNameIdOrZero
_IsnsRegFcPortFcNodeWwnn_Object = MibTableColumn
isnsRegFcPortFcNodeWwnn = _IsnsRegFcPortFcNodeWwnn_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 15),
    _IsnsRegFcPortFcNodeWwnn_Type()
)
isnsRegFcPortFcNodeWwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortFcNodeWwnn.setStatus("current")
_IsnsRegFcPortPpnWwn_Type = FcNameIdOrZero
_IsnsRegFcPortPpnWwn_Object = MibTableColumn
isnsRegFcPortPpnWwn = _IsnsRegFcPortPpnWwn_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 2, 1, 16),
    _IsnsRegFcPortPpnWwn_Type()
)
isnsRegFcPortPpnWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcPortPpnWwn.setStatus("current")
_IsnsRegFcNodePortTable_Object = MibTable
isnsRegFcNodePortTable = _IsnsRegFcNodePortTable_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 3)
)
if mibBuilder.loadTexts:
    isnsRegFcNodePortTable.setStatus("current")
_IsnsRegFcNodePortEntry_Object = MibTableRow
isnsRegFcNodePortEntry = _IsnsRegFcNodePortEntry_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 3, 1)
)
isnsRegFcNodePortEntry.setIndexNames(
    (0, "ISNS-MIB", "isnsServerIndex"),
    (0, "ISNS-MIB", "isnsRegFcNodeWwnn"),
    (0, "ISNS-MIB", "isnsRegFcPortWwpn"),
)
if mibBuilder.loadTexts:
    isnsRegFcNodePortEntry.setStatus("current")
_IsnsRegFcNodePortEntityIndex_Type = IsnsEntityIndexIdOrZero
_IsnsRegFcNodePortEntityIndex_Object = MibTableColumn
isnsRegFcNodePortEntityIndex = _IsnsRegFcNodePortEntityIndex_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 1, 6, 5, 3, 1, 1),
    _IsnsRegFcNodePortEntityIndex_Type()
)
isnsRegFcNodePortEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isnsRegFcNodePortEntityIndex.setStatus("current")
_IsnsNotificationsInfo_ObjectIdentity = ObjectIdentity
isnsNotificationsInfo = _IsnsNotificationsInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 1, 2)
)
_IsnsInstanceInfo_Type = SnmpAdminString
_IsnsInstanceInfo_Object = MibScalar
isnsInstanceInfo = _IsnsInstanceInfo_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 2, 1),
    _IsnsInstanceInfo_Type()
)
isnsInstanceInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isnsInstanceInfo.setStatus("current")
_IsnsAddressNotificationType_Type = InetAddressType
_IsnsAddressNotificationType_Object = MibScalar
isnsAddressNotificationType = _IsnsAddressNotificationType_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 2, 2),
    _IsnsAddressNotificationType_Type()
)
isnsAddressNotificationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isnsAddressNotificationType.setStatus("current")
_IsnsAddressNotification_Type = InetAddress
_IsnsAddressNotification_Object = MibScalar
isnsAddressNotification = _IsnsAddressNotification_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 2, 3),
    _IsnsAddressNotification_Type()
)
isnsAddressNotification.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isnsAddressNotification.setStatus("current")
_IsnsTcpPortNotification_Type = InetPortNumber
_IsnsTcpPortNotification_Object = MibScalar
isnsTcpPortNotification = _IsnsTcpPortNotification_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 2, 4),
    _IsnsTcpPortNotification_Type()
)
isnsTcpPortNotification.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isnsTcpPortNotification.setStatus("current")
_IsnsUdpPortNotification_Type = InetPortNumber
_IsnsUdpPortNotification_Object = MibScalar
isnsUdpPortNotification = _IsnsUdpPortNotification_Object(
    (1, 3, 6, 1, 2, 1, 163, 1, 2, 5),
    _IsnsUdpPortNotification_Type()
)
isnsUdpPortNotification.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isnsUdpPortNotification.setStatus("current")
_IsnsConformance_ObjectIdentity = ObjectIdentity
isnsConformance = _IsnsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 2)
)
_IsnsCompliances_ObjectIdentity = ObjectIdentity
isnsCompliances = _IsnsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 2, 1)
)
_IsnsGroups_ObjectIdentity = ObjectIdentity
isnsGroups = _IsnsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 163, 2, 2)
)
isnsServerEntry.registerAugmentions(
    ("ISNS-MIB",
     "isnsNumObjectsEntry")
)
isnsNumObjectsEntry.setIndexNames(*isnsServerEntry.getIndexNames())

# Managed Objects groups

isnsServerAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 163, 2, 2, 1)
)
isnsServerAttributesGroup.setObjects(
      *(("ISNS-MIB", "isnsServerName"),
        ("ISNS-MIB", "isnsServerIsnsVersion"),
        ("ISNS-MIB", "isnsServerVendorInfo"),
        ("ISNS-MIB", "isnsServerPhysicalIndex"),
        ("ISNS-MIB", "isnsServerTcpPort"),
        ("ISNS-MIB", "isnsServerUdpPort"),
        ("ISNS-MIB", "isnsServerDiscontinuityTime"),
        ("ISNS-MIB", "isnsServerRole"),
        ("ISNS-MIB", "isnsServerDiscoveryMethodsEnabled"),
        ("ISNS-MIB", "isnsServerDiscoveryMcGroupType"),
        ("ISNS-MIB", "isnsServerDiscoveryMcGroupAddress"),
        ("ISNS-MIB", "isnsServerEsiNonResponseThreshold"),
        ("ISNS-MIB", "isnsServerEnableControlNodeMgtScn"),
        ("ISNS-MIB", "isnsServerDefaultDdDdsStatus"),
        ("ISNS-MIB", "isnsServerUpdateDdDdsSupported"),
        ("ISNS-MIB", "isnsServerUpdateDdDdsEnabled"))
)
if mibBuilder.loadTexts:
    isnsServerAttributesGroup.setStatus("current")

isnsServerNumObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 163, 2, 2, 2)
)
isnsServerNumObjectsGroup.setObjects(
      *(("ISNS-MIB", "isnsNumDds"),
        ("ISNS-MIB", "isnsNumDd"),
        ("ISNS-MIB", "isnsNumEntities"),
        ("ISNS-MIB", "isnsNumPortals"),
        ("ISNS-MIB", "isnsNumPortalGroups"),
        ("ISNS-MIB", "isnsNumIscsiNodes"),
        ("ISNS-MIB", "isnsNumFcPorts"),
        ("ISNS-MIB", "isnsNumFcNodes"),
        ("ISNS-MIB", "isnsRegEntityInfoNumPortals"),
        ("ISNS-MIB", "isnsRegEntityInfoNumPortalGroups"),
        ("ISNS-MIB", "isnsRegEntityInfoNumIscsiNodes"),
        ("ISNS-MIB", "isnsRegEntityInfoNumFcPorts"),
        ("ISNS-MIB", "isnsRegEntityInfoNumFcNodes"))
)
if mibBuilder.loadTexts:
    isnsServerNumObjectsGroup.setStatus("current")

isnsServerIscsiControlNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 163, 2, 2, 3)
)
isnsServerIscsiControlNodeGroup.setObjects(
      *(("ISNS-MIB", "isnsControlNodeIscsiNodeName"),
        ("ISNS-MIB", "isnsControlNodeIscsiIsRegistered"),
        ("ISNS-MIB", "isnsControlNodeIscsiRcvMgtSCN"))
)
if mibBuilder.loadTexts:
    isnsServerIscsiControlNodeGroup.setStatus("current")

isnsServerIfcpPortControlNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 163, 2, 2, 4)
)
isnsServerIfcpPortControlNodeGroup.setObjects(
      *(("ISNS-MIB", "isnsControlNodeFcPortIsRegistered"),
        ("ISNS-MIB", "isnsControlNodeFcPortRcvMgtSCN"))
)
if mibBuilder.loadTexts:
    isnsServerIfcpPortControlNodeGroup.setStatus("current")

isnsServerIscsiDdsDdObjGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 163, 2, 2, 5)
)
isnsServerIscsiDdsDdObjGroup.setObjects(
      *(("ISNS-MIB", "isnsDdsSymbolicName"),
        ("ISNS-MIB", "isnsDdsStatus"),
        ("ISNS-MIB", "isnsDdsMemberSymbolicName"),
        ("ISNS-MIB", "isnsDdSymbolicName"),
        ("ISNS-MIB", "isnsDdFeatures"),
        ("ISNS-MIB", "isnsDdIscsiMemberName"),
        ("ISNS-MIB", "isnsDdIscsiMemberIsRegistered"),
        ("ISNS-MIB", "isnsDdPortalMemberAddressType"),
        ("ISNS-MIB", "isnsDdPortalMemberAddress"),
        ("ISNS-MIB", "isnsDdPortalMemberPortType"),
        ("ISNS-MIB", "isnsDdPortalMemberPort"),
        ("ISNS-MIB", "isnsDdPortalMemberIsRegistered"))
)
if mibBuilder.loadTexts:
    isnsServerIscsiDdsDdObjGroup.setStatus("current")

isnsServerIfcpDdsDdObjGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 163, 2, 2, 6)
)
isnsServerIfcpDdsDdObjGroup.setObjects(
      *(("ISNS-MIB", "isnsDdsSymbolicName"),
        ("ISNS-MIB", "isnsDdsStatus"),
        ("ISNS-MIB", "isnsDdSymbolicName"),
        ("ISNS-MIB", "isnsDdFeatures"),
        ("ISNS-MIB", "isnsDdPortalMemberAddressType"),
        ("ISNS-MIB", "isnsDdPortalMemberAddress"),
        ("ISNS-MIB", "isnsDdPortalMemberPortType"),
        ("ISNS-MIB", "isnsDdPortalMemberPort"),
        ("ISNS-MIB", "isnsDdPortalMemberIsRegistered"),
        ("ISNS-MIB", "isnsDdFcPortMemberIsRegistered"))
)
if mibBuilder.loadTexts:
    isnsServerIfcpDdsDdObjGroup.setStatus("current")

isnsServerRegIscsiObjGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 163, 2, 2, 7)
)
isnsServerRegIscsiObjGroup.setObjects(
      *(("ISNS-MIB", "isnsRegEntityEID"),
        ("ISNS-MIB", "isnsRegEntityProtocol"),
        ("ISNS-MIB", "isnsRegEntityManagementAddressType"),
        ("ISNS-MIB", "isnsRegEntityManagementAddress"),
        ("ISNS-MIB", "isnsRegEntityTimestamp"),
        ("ISNS-MIB", "isnsRegEntityVersionMin"),
        ("ISNS-MIB", "isnsRegEntityVersionMax"),
        ("ISNS-MIB", "isnsRegEntityRegistrationPeriod"),
        ("ISNS-MIB", "isnsRegEntityInfoNumPortals"),
        ("ISNS-MIB", "isnsRegEntityInfoNumPortalGroups"),
        ("ISNS-MIB", "isnsRegEntityInfoNumIscsiNodes"),
        ("ISNS-MIB", "isnsRegEntityInfoNumFcPorts"),
        ("ISNS-MIB", "isnsRegEntityInfoNumFcNodes"),
        ("ISNS-MIB", "isnsRegPortalAddressType"),
        ("ISNS-MIB", "isnsRegPortalAddress"),
        ("ISNS-MIB", "isnsRegPortalPortType"),
        ("ISNS-MIB", "isnsRegPortalPort"),
        ("ISNS-MIB", "isnsRegPortalSymbolicName"),
        ("ISNS-MIB", "isnsRegPortalEsiInterval"),
        ("ISNS-MIB", "isnsRegPortalEsiPortType"),
        ("ISNS-MIB", "isnsRegPortalEsiPort"),
        ("ISNS-MIB", "isnsRegPortalScnPortType"),
        ("ISNS-MIB", "isnsRegPortalScnPort"),
        ("ISNS-MIB", "isnsRegPortalSecurityInfo"),
        ("ISNS-MIB", "isnsRegPgIscsiNodeIndex"),
        ("ISNS-MIB", "isnsRegPgIscsiName"),
        ("ISNS-MIB", "isnsRegPgPortalPortalIndex"),
        ("ISNS-MIB", "isnsRegPgPortalAddressType"),
        ("ISNS-MIB", "isnsRegPgPortalAddress"),
        ("ISNS-MIB", "isnsRegPgPortalPortType"),
        ("ISNS-MIB", "isnsRegPgPortalPort"),
        ("ISNS-MIB", "isnsRegPgPGT"),
        ("ISNS-MIB", "isnsRegIscsiNodeName"),
        ("ISNS-MIB", "isnsRegIscsiNodeType"),
        ("ISNS-MIB", "isnsRegIscsiNodeAlias"),
        ("ISNS-MIB", "isnsRegIscsiNodeScnTypes"),
        ("ISNS-MIB", "isnsRegIscsiNodeWwnToken"),
        ("ISNS-MIB", "isnsRegIscsiNodeAuthMethod"))
)
if mibBuilder.loadTexts:
    isnsServerRegIscsiObjGroup.setStatus("current")

isnsServerRegIfcpObjGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 163, 2, 2, 8)
)
isnsServerRegIfcpObjGroup.setObjects(
      *(("ISNS-MIB", "isnsRegEntityEID"),
        ("ISNS-MIB", "isnsRegEntityProtocol"),
        ("ISNS-MIB", "isnsRegEntityManagementAddressType"),
        ("ISNS-MIB", "isnsRegEntityManagementAddress"),
        ("ISNS-MIB", "isnsRegEntityTimestamp"),
        ("ISNS-MIB", "isnsRegEntityVersionMin"),
        ("ISNS-MIB", "isnsRegEntityVersionMax"),
        ("ISNS-MIB", "isnsRegEntityRegistrationPeriod"),
        ("ISNS-MIB", "isnsRegEntityInfoNumPortals"),
        ("ISNS-MIB", "isnsRegEntityInfoNumPortalGroups"),
        ("ISNS-MIB", "isnsRegEntityInfoNumIscsiNodes"),
        ("ISNS-MIB", "isnsRegEntityInfoNumFcPorts"),
        ("ISNS-MIB", "isnsRegEntityInfoNumFcNodes"),
        ("ISNS-MIB", "isnsRegPortalAddressType"),
        ("ISNS-MIB", "isnsRegPortalAddress"),
        ("ISNS-MIB", "isnsRegPortalPortType"),
        ("ISNS-MIB", "isnsRegPortalPort"),
        ("ISNS-MIB", "isnsRegPortalSymbolicName"),
        ("ISNS-MIB", "isnsRegPortalEsiInterval"),
        ("ISNS-MIB", "isnsRegPortalEsiPortType"),
        ("ISNS-MIB", "isnsRegPortalEsiPort"),
        ("ISNS-MIB", "isnsRegPortalScnPortType"),
        ("ISNS-MIB", "isnsRegPortalScnPort"),
        ("ISNS-MIB", "isnsRegPortalSecurityInfo"),
        ("ISNS-MIB", "isnsRegFcPortID"),
        ("ISNS-MIB", "isnsRegFcPortType"),
        ("ISNS-MIB", "isnsRegFcPortSymbolicName"),
        ("ISNS-MIB", "isnsRegFcPortFabricPortWwn"),
        ("ISNS-MIB", "isnsRegFcPortHA"),
        ("ISNS-MIB", "isnsRegFcPortAddressType"),
        ("ISNS-MIB", "isnsRegFcPortAddress"),
        ("ISNS-MIB", "isnsRegFcPortFcCos"),
        ("ISNS-MIB", "isnsRegFcPortFc4Types"),
        ("ISNS-MIB", "isnsRegFcPortFc4Descr"),
        ("ISNS-MIB", "isnsRegFcPortFc4Features"),
        ("ISNS-MIB", "isnsRegFcPortScnTypes"),
        ("ISNS-MIB", "isnsRegFcPortRole"),
        ("ISNS-MIB", "isnsRegFcPortFcNodeWwnn"),
        ("ISNS-MIB", "isnsRegFcPortPpnWwn"),
        ("ISNS-MIB", "isnsRegFcNodeSymbolicName"),
        ("ISNS-MIB", "isnsRegFcNodeAddressType"),
        ("ISNS-MIB", "isnsRegFcNodeAddress"),
        ("ISNS-MIB", "isnsRegFcNodeIPA"),
        ("ISNS-MIB", "isnsRegFcNodeProxyIscsiName"),
        ("ISNS-MIB", "isnsRegFcNodeNumFcPorts"),
        ("ISNS-MIB", "isnsRegFcNodePortEntityIndex"))
)
if mibBuilder.loadTexts:
    isnsServerRegIfcpObjGroup.setStatus("current")

isnsNotificationsObjGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 163, 2, 2, 9)
)
isnsNotificationsObjGroup.setObjects(
      *(("ISNS-MIB", "isnsInstanceInfo"),
        ("ISNS-MIB", "isnsAddressNotificationType"),
        ("ISNS-MIB", "isnsAddressNotification"),
        ("ISNS-MIB", "isnsTcpPortNotification"),
        ("ISNS-MIB", "isnsUdpPortNotification"))
)
if mibBuilder.loadTexts:
    isnsNotificationsObjGroup.setStatus("current")


# Notification objects

isnsServerStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 163, 0, 1)
)
isnsServerStart.setObjects(
      *(("ISNS-MIB", "isnsInstanceInfo"),
        ("ISNS-MIB", "isnsAddressNotificationType"),
        ("ISNS-MIB", "isnsAddressNotification"),
        ("ISNS-MIB", "isnsTcpPortNotification"),
        ("ISNS-MIB", "isnsUdpPortNotification"))
)
if mibBuilder.loadTexts:
    isnsServerStart.setStatus(
        "current"
    )

isnsServerShutdown = NotificationType(
    (1, 3, 6, 1, 2, 1, 163, 0, 2)
)
isnsServerShutdown.setObjects(
      *(("ISNS-MIB", "isnsInstanceInfo"),
        ("ISNS-MIB", "isnsAddressNotificationType"),
        ("ISNS-MIB", "isnsAddressNotification"),
        ("ISNS-MIB", "isnsTcpPortNotification"),
        ("ISNS-MIB", "isnsUdpPortNotification"))
)
if mibBuilder.loadTexts:
    isnsServerShutdown.setStatus(
        "current"
    )


# Notifications groups

isnsServerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 163, 2, 2, 10)
)
isnsServerNotificationGroup.setObjects(
      *(("ISNS-MIB", "isnsServerStart"),
        ("ISNS-MIB", "isnsServerShutdown"))
)
if mibBuilder.loadTexts:
    isnsServerNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

isnsIscsiServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 163, 2, 1, 1)
)
if mibBuilder.loadTexts:
    isnsIscsiServerCompliance.setStatus(
        "current"
    )

isnsIfcpServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 163, 2, 1, 2)
)
if mibBuilder.loadTexts:
    isnsIfcpServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISNS-MIB",
    **{"IsnsDiscoveryDomainSetId": IsnsDiscoveryDomainSetId,
       "IsnsDdsStatusType": IsnsDdsStatusType,
       "IsnsDiscoveryDomainId": IsnsDiscoveryDomainId,
       "IsnsDdFeatureType": IsnsDdFeatureType,
       "IsnsDdDdsModificationType": IsnsDdDdsModificationType,
       "IsnsEntityIndexIdOrZero": IsnsEntityIndexIdOrZero,
       "IsnsPortalGroupIndexId": IsnsPortalGroupIndexId,
       "IsnsPortalIndexId": IsnsPortalIndexId,
       "IsnsPortalPortTypeId": IsnsPortalPortTypeId,
       "IsnsPortalGroupTagIdOrNull": IsnsPortalGroupTagIdOrNull,
       "IsnsPortalSecurityType": IsnsPortalSecurityType,
       "IsnsNodeIndexId": IsnsNodeIndexId,
       "IsnsIscsiNodeType": IsnsIscsiNodeType,
       "IsnsFcClassOfServiceType": IsnsFcClassOfServiceType,
       "IsnsIscsiScnType": IsnsIscsiScnType,
       "IsnsIfcpScnType": IsnsIfcpScnType,
       "IsnsFcPortRoleType": IsnsFcPortRoleType,
       "IsnsSrvrDiscoveryMethodsType": IsnsSrvrDiscoveryMethodsType,
       "isnsMIB": isnsMIB,
       "isnsNotifications": isnsNotifications,
       "isnsServerStart": isnsServerStart,
       "isnsServerShutdown": isnsServerShutdown,
       "isnsObjects": isnsObjects,
       "isnsServerInfo": isnsServerInfo,
       "isnsServerTable": isnsServerTable,
       "isnsServerEntry": isnsServerEntry,
       "isnsServerIndex": isnsServerIndex,
       "isnsServerName": isnsServerName,
       "isnsServerIsnsVersion": isnsServerIsnsVersion,
       "isnsServerVendorInfo": isnsServerVendorInfo,
       "isnsServerPhysicalIndex": isnsServerPhysicalIndex,
       "isnsServerTcpPort": isnsServerTcpPort,
       "isnsServerUdpPort": isnsServerUdpPort,
       "isnsServerDiscontinuityTime": isnsServerDiscontinuityTime,
       "isnsServerRole": isnsServerRole,
       "isnsServerDiscoveryMethodsEnabled": isnsServerDiscoveryMethodsEnabled,
       "isnsServerDiscoveryMcGroupType": isnsServerDiscoveryMcGroupType,
       "isnsServerDiscoveryMcGroupAddress": isnsServerDiscoveryMcGroupAddress,
       "isnsServerEsiNonResponseThreshold": isnsServerEsiNonResponseThreshold,
       "isnsServerEnableControlNodeMgtScn": isnsServerEnableControlNodeMgtScn,
       "isnsServerDefaultDdDdsStatus": isnsServerDefaultDdDdsStatus,
       "isnsServerUpdateDdDdsSupported": isnsServerUpdateDdDdsSupported,
       "isnsServerUpdateDdDdsEnabled": isnsServerUpdateDdDdsEnabled,
       "isnsNumObjectsTable": isnsNumObjectsTable,
       "isnsNumObjectsEntry": isnsNumObjectsEntry,
       "isnsNumDds": isnsNumDds,
       "isnsNumDd": isnsNumDd,
       "isnsNumEntities": isnsNumEntities,
       "isnsNumPortals": isnsNumPortals,
       "isnsNumPortalGroups": isnsNumPortalGroups,
       "isnsNumIscsiNodes": isnsNumIscsiNodes,
       "isnsNumFcPorts": isnsNumFcPorts,
       "isnsNumFcNodes": isnsNumFcNodes,
       "isnsControlNodeInfo": isnsControlNodeInfo,
       "isnsControlNodeIscsiTable": isnsControlNodeIscsiTable,
       "isnsControlNodeIscsiEntry": isnsControlNodeIscsiEntry,
       "isnsControlNodeIscsiNodeIndex": isnsControlNodeIscsiNodeIndex,
       "isnsControlNodeIscsiNodeName": isnsControlNodeIscsiNodeName,
       "isnsControlNodeIscsiIsRegistered": isnsControlNodeIscsiIsRegistered,
       "isnsControlNodeIscsiRcvMgtSCN": isnsControlNodeIscsiRcvMgtSCN,
       "isnsControlNodeFcPortTable": isnsControlNodeFcPortTable,
       "isnsControlNodeFcPortEntry": isnsControlNodeFcPortEntry,
       "isnsControlNodeFcPortWwpn": isnsControlNodeFcPortWwpn,
       "isnsControlNodeFcPortIsRegistered": isnsControlNodeFcPortIsRegistered,
       "isnsControlNodeFcPortRcvMgtSCN": isnsControlNodeFcPortRcvMgtSCN,
       "isnsDdsInfo": isnsDdsInfo,
       "isnsDdsTable": isnsDdsTable,
       "isnsDdsEntry": isnsDdsEntry,
       "isnsDdsId": isnsDdsId,
       "isnsDdsSymbolicName": isnsDdsSymbolicName,
       "isnsDdsStatus": isnsDdsStatus,
       "isnsDdsMemberTable": isnsDdsMemberTable,
       "isnsDdsMemberEntry": isnsDdsMemberEntry,
       "isnsDdsMemberDdId": isnsDdsMemberDdId,
       "isnsDdsMemberSymbolicName": isnsDdsMemberSymbolicName,
       "isnsDdInfo": isnsDdInfo,
       "isnsDdTable": isnsDdTable,
       "isnsDdEntry": isnsDdEntry,
       "isnsDdId": isnsDdId,
       "isnsDdSymbolicName": isnsDdSymbolicName,
       "isnsDdFeatures": isnsDdFeatures,
       "isnsDdIscsiMemberTable": isnsDdIscsiMemberTable,
       "isnsDdIscsiMemberEntry": isnsDdIscsiMemberEntry,
       "isnsDdIscsiMemberIndex": isnsDdIscsiMemberIndex,
       "isnsDdIscsiMemberName": isnsDdIscsiMemberName,
       "isnsDdIscsiMemberIsRegistered": isnsDdIscsiMemberIsRegistered,
       "isnsDdPortalMemberTable": isnsDdPortalMemberTable,
       "isnsDdPortalMemberEntry": isnsDdPortalMemberEntry,
       "isnsDdPortalMemberIndex": isnsDdPortalMemberIndex,
       "isnsDdPortalMemberAddressType": isnsDdPortalMemberAddressType,
       "isnsDdPortalMemberAddress": isnsDdPortalMemberAddress,
       "isnsDdPortalMemberPortType": isnsDdPortalMemberPortType,
       "isnsDdPortalMemberPort": isnsDdPortalMemberPort,
       "isnsDdPortalMemberIsRegistered": isnsDdPortalMemberIsRegistered,
       "isnsDdFcPortMemberTable": isnsDdFcPortMemberTable,
       "isnsDdFcPortMemberEntry": isnsDdFcPortMemberEntry,
       "isnsDdFcPortMemberPortName": isnsDdFcPortMemberPortName,
       "isnsDdFcPortMemberIsRegistered": isnsDdFcPortMemberIsRegistered,
       "isnsReg": isnsReg,
       "isnsRegEntityInfo": isnsRegEntityInfo,
       "isnsRegEntityTable": isnsRegEntityTable,
       "isnsRegEntityEntry": isnsRegEntityEntry,
       "isnsRegEntityIndex": isnsRegEntityIndex,
       "isnsRegEntityEID": isnsRegEntityEID,
       "isnsRegEntityProtocol": isnsRegEntityProtocol,
       "isnsRegEntityManagementAddressType": isnsRegEntityManagementAddressType,
       "isnsRegEntityManagementAddress": isnsRegEntityManagementAddress,
       "isnsRegEntityTimestamp": isnsRegEntityTimestamp,
       "isnsRegEntityVersionMin": isnsRegEntityVersionMin,
       "isnsRegEntityVersionMax": isnsRegEntityVersionMax,
       "isnsRegEntityRegistrationPeriod": isnsRegEntityRegistrationPeriod,
       "isnsRegEntityNumObjectsTable": isnsRegEntityNumObjectsTable,
       "isnsRegEntityNumObjectsEntry": isnsRegEntityNumObjectsEntry,
       "isnsRegEntityInfoNumPortals": isnsRegEntityInfoNumPortals,
       "isnsRegEntityInfoNumPortalGroups": isnsRegEntityInfoNumPortalGroups,
       "isnsRegEntityInfoNumIscsiNodes": isnsRegEntityInfoNumIscsiNodes,
       "isnsRegEntityInfoNumFcPorts": isnsRegEntityInfoNumFcPorts,
       "isnsRegEntityInfoNumFcNodes": isnsRegEntityInfoNumFcNodes,
       "isnsRegPortalInfo": isnsRegPortalInfo,
       "isnsRegPortalTable": isnsRegPortalTable,
       "isnsRegPortalEntry": isnsRegPortalEntry,
       "isnsRegPortalPortalIndex": isnsRegPortalPortalIndex,
       "isnsRegPortalAddressType": isnsRegPortalAddressType,
       "isnsRegPortalAddress": isnsRegPortalAddress,
       "isnsRegPortalPortType": isnsRegPortalPortType,
       "isnsRegPortalPort": isnsRegPortalPort,
       "isnsRegPortalSymbolicName": isnsRegPortalSymbolicName,
       "isnsRegPortalEsiInterval": isnsRegPortalEsiInterval,
       "isnsRegPortalEsiPortType": isnsRegPortalEsiPortType,
       "isnsRegPortalEsiPort": isnsRegPortalEsiPort,
       "isnsRegPortalScnPortType": isnsRegPortalScnPortType,
       "isnsRegPortalScnPort": isnsRegPortalScnPort,
       "isnsRegPortalSecurityInfo": isnsRegPortalSecurityInfo,
       "isnsRegPortalGroupInfo": isnsRegPortalGroupInfo,
       "isnsRegPgTable": isnsRegPgTable,
       "isnsRegPgEntry": isnsRegPgEntry,
       "isnsRegPgIndex": isnsRegPgIndex,
       "isnsRegPgIscsiNodeIndex": isnsRegPgIscsiNodeIndex,
       "isnsRegPgIscsiName": isnsRegPgIscsiName,
       "isnsRegPgPortalPortalIndex": isnsRegPgPortalPortalIndex,
       "isnsRegPgPortalAddressType": isnsRegPgPortalAddressType,
       "isnsRegPgPortalAddress": isnsRegPgPortalAddress,
       "isnsRegPgPortalPortType": isnsRegPgPortalPortType,
       "isnsRegPgPortalPort": isnsRegPgPortalPort,
       "isnsRegPgPGT": isnsRegPgPGT,
       "isnsRegIscsiNodeInfo": isnsRegIscsiNodeInfo,
       "isnsRegIscsiNodeTable": isnsRegIscsiNodeTable,
       "isnsRegIscsiNodeEntry": isnsRegIscsiNodeEntry,
       "isnsRegIscsiNodeIndex": isnsRegIscsiNodeIndex,
       "isnsRegIscsiNodeName": isnsRegIscsiNodeName,
       "isnsRegIscsiNodeType": isnsRegIscsiNodeType,
       "isnsRegIscsiNodeAlias": isnsRegIscsiNodeAlias,
       "isnsRegIscsiNodeScnTypes": isnsRegIscsiNodeScnTypes,
       "isnsRegIscsiNodeWwnToken": isnsRegIscsiNodeWwnToken,
       "isnsRegIscsiNodeAuthMethod": isnsRegIscsiNodeAuthMethod,
       "isnsRegFcNodeInfo": isnsRegFcNodeInfo,
       "isnsRegFcNodeTable": isnsRegFcNodeTable,
       "isnsRegFcNodeEntry": isnsRegFcNodeEntry,
       "isnsRegFcNodeWwnn": isnsRegFcNodeWwnn,
       "isnsRegFcNodeSymbolicName": isnsRegFcNodeSymbolicName,
       "isnsRegFcNodeAddressType": isnsRegFcNodeAddressType,
       "isnsRegFcNodeAddress": isnsRegFcNodeAddress,
       "isnsRegFcNodeIPA": isnsRegFcNodeIPA,
       "isnsRegFcNodeProxyIscsiName": isnsRegFcNodeProxyIscsiName,
       "isnsRegFcNodeNumFcPorts": isnsRegFcNodeNumFcPorts,
       "isnsRegFcPortTable": isnsRegFcPortTable,
       "isnsRegFcPortEntry": isnsRegFcPortEntry,
       "isnsRegFcPortWwpn": isnsRegFcPortWwpn,
       "isnsRegFcPortID": isnsRegFcPortID,
       "isnsRegFcPortType": isnsRegFcPortType,
       "isnsRegFcPortSymbolicName": isnsRegFcPortSymbolicName,
       "isnsRegFcPortFabricPortWwn": isnsRegFcPortFabricPortWwn,
       "isnsRegFcPortHA": isnsRegFcPortHA,
       "isnsRegFcPortAddressType": isnsRegFcPortAddressType,
       "isnsRegFcPortAddress": isnsRegFcPortAddress,
       "isnsRegFcPortFcCos": isnsRegFcPortFcCos,
       "isnsRegFcPortFc4Types": isnsRegFcPortFc4Types,
       "isnsRegFcPortFc4Descr": isnsRegFcPortFc4Descr,
       "isnsRegFcPortFc4Features": isnsRegFcPortFc4Features,
       "isnsRegFcPortScnTypes": isnsRegFcPortScnTypes,
       "isnsRegFcPortRole": isnsRegFcPortRole,
       "isnsRegFcPortFcNodeWwnn": isnsRegFcPortFcNodeWwnn,
       "isnsRegFcPortPpnWwn": isnsRegFcPortPpnWwn,
       "isnsRegFcNodePortTable": isnsRegFcNodePortTable,
       "isnsRegFcNodePortEntry": isnsRegFcNodePortEntry,
       "isnsRegFcNodePortEntityIndex": isnsRegFcNodePortEntityIndex,
       "isnsNotificationsInfo": isnsNotificationsInfo,
       "isnsInstanceInfo": isnsInstanceInfo,
       "isnsAddressNotificationType": isnsAddressNotificationType,
       "isnsAddressNotification": isnsAddressNotification,
       "isnsTcpPortNotification": isnsTcpPortNotification,
       "isnsUdpPortNotification": isnsUdpPortNotification,
       "isnsConformance": isnsConformance,
       "isnsCompliances": isnsCompliances,
       "isnsIscsiServerCompliance": isnsIscsiServerCompliance,
       "isnsIfcpServerCompliance": isnsIfcpServerCompliance,
       "isnsGroups": isnsGroups,
       "isnsServerAttributesGroup": isnsServerAttributesGroup,
       "isnsServerNumObjectsGroup": isnsServerNumObjectsGroup,
       "isnsServerIscsiControlNodeGroup": isnsServerIscsiControlNodeGroup,
       "isnsServerIfcpPortControlNodeGroup": isnsServerIfcpPortControlNodeGroup,
       "isnsServerIscsiDdsDdObjGroup": isnsServerIscsiDdsDdObjGroup,
       "isnsServerIfcpDdsDdObjGroup": isnsServerIfcpDdsDdObjGroup,
       "isnsServerRegIscsiObjGroup": isnsServerRegIscsiObjGroup,
       "isnsServerRegIfcpObjGroup": isnsServerRegIfcpObjGroup,
       "isnsNotificationsObjGroup": isnsNotificationsObjGroup,
       "isnsServerNotificationGroup": isnsServerNotificationGroup}
)
