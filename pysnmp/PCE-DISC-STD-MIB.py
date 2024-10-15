# SNMP MIB module (PCE-DISC-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PCE-DISC-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:05 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pceDiscStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 10000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PceRoutingDomainID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



# MIB Managed Objects in the order of their OIDs

_PceDiscNotifications_ObjectIdentity = ObjectIdentity
pceDiscNotifications = _PceDiscNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 0)
)
_PceDiscMIBObjects_ObjectIdentity = ObjectIdentity
pceDiscMIBObjects = _PceDiscMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1)
)
_PceDiscoveryObjects_ObjectIdentity = ObjectIdentity
pceDiscoveryObjects = _PceDiscoveryObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1, 1)
)


class _PceDiscoveryAdminStatus_Type(Integer32):
    """Custom type pceDiscoveryAdminStatus based on Integer32"""
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


_PceDiscoveryAdminStatus_Type.__name__ = "Integer32"
_PceDiscoveryAdminStatus_Object = MibScalar
pceDiscoveryAdminStatus = _PceDiscoveryAdminStatus_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 1),
    _PceDiscoveryAdminStatus_Type()
)
pceDiscoveryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pceDiscoveryAdminStatus.setStatus("current")
_PceDiscoveryKnowPCEs_Type = Counter32
_PceDiscoveryKnowPCEs_Object = MibScalar
pceDiscoveryKnowPCEs = _PceDiscoveryKnowPCEs_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 2),
    _PceDiscoveryKnowPCEs_Type()
)
pceDiscoveryKnowPCEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscoveryKnowPCEs.setStatus("current")
_PceDiscoveryActivePCEs_Type = Counter32
_PceDiscoveryActivePCEs_Object = MibScalar
pceDiscoveryActivePCEs = _PceDiscoveryActivePCEs_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 3),
    _PceDiscoveryActivePCEs_Type()
)
pceDiscoveryActivePCEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscoveryActivePCEs.setStatus("current")
_PceDiscoveryTable_Object = MibTable
pceDiscoveryTable = _PceDiscoveryTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pceDiscoveryTable.setStatus("current")
_PceDiscoveryEntry_Object = MibTableRow
pceDiscoveryEntry = _PceDiscoveryEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1)
)
pceDiscoveryEntry.setIndexNames(
    (0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"),
)
if mibBuilder.loadTexts:
    pceDiscoveryEntry.setStatus("current")


class _PceDiscoveryIndex_Type(Integer32):
    """Custom type pceDiscoveryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PceDiscoveryIndex_Type.__name__ = "Integer32"
_PceDiscoveryIndex_Object = MibTableColumn
pceDiscoveryIndex = _PceDiscoveryIndex_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 1),
    _PceDiscoveryIndex_Type()
)
pceDiscoveryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pceDiscoveryIndex.setStatus("current")
_PceDiscoveryMechanism_Type = IANAipRouteProtocol
_PceDiscoveryMechanism_Object = MibTableColumn
pceDiscoveryMechanism = _PceDiscoveryMechanism_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 2),
    _PceDiscoveryMechanism_Type()
)
pceDiscoveryMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscoveryMechanism.setStatus("current")
_PceDiscoveryIPv4Address_Type = IpAddress
_PceDiscoveryIPv4Address_Object = MibTableColumn
pceDiscoveryIPv4Address = _PceDiscoveryIPv4Address_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 3),
    _PceDiscoveryIPv4Address_Type()
)
pceDiscoveryIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscoveryIPv4Address.setStatus("current")
_PceDiscoveryIPv6Address_Type = Ipv6Address
_PceDiscoveryIPv6Address_Object = MibTableColumn
pceDiscoveryIPv6Address = _PceDiscoveryIPv6Address_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 4),
    _PceDiscoveryIPv6Address_Type()
)
pceDiscoveryIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscoveryIPv6Address.setStatus("current")
_PceDiscoveryTime_Type = TimeStamp
_PceDiscoveryTime_Object = MibTableColumn
pceDiscoveryTime = _PceDiscoveryTime_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 5),
    _PceDiscoveryTime_Type()
)
pceDiscoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscoveryTime.setStatus("current")
_PceDiscoveryLastUpdated_Type = TimeStamp
_PceDiscoveryLastUpdated_Object = MibTableColumn
pceDiscoveryLastUpdated = _PceDiscoveryLastUpdated_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 6),
    _PceDiscoveryLastUpdated_Type()
)
pceDiscoveryLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscoveryLastUpdated.setStatus("current")
_PceDiscoveryCongestion_Type = TruthValue
_PceDiscoveryCongestion_Object = MibTableColumn
pceDiscoveryCongestion = _PceDiscoveryCongestion_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 7),
    _PceDiscoveryCongestion_Type()
)
pceDiscoveryCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscoveryCongestion.setStatus("current")
_PceDiscoveryCongestionDuration_Type = Unsigned32
_PceDiscoveryCongestionDuration_Object = MibTableColumn
pceDiscoveryCongestionDuration = _PceDiscoveryCongestionDuration_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 8),
    _PceDiscoveryCongestionDuration_Type()
)
pceDiscoveryCongestionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscoveryCongestionDuration.setStatus("current")
_PceDiscCapabilityObjects_ObjectIdentity = ObjectIdentity
pceDiscCapabilityObjects = _PceDiscCapabilityObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1, 2)
)
_PceDiscCapPathScopeTable_Object = MibTable
pceDiscCapPathScopeTable = _PceDiscCapPathScopeTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pceDiscCapPathScopeTable.setStatus("current")
_PceDiscCapPathScopeEntry_Object = MibTableRow
pceDiscCapPathScopeEntry = _PceDiscCapPathScopeEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1)
)
pceDiscCapPathScopeEntry.setIndexNames(
    (0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"),
)
if mibBuilder.loadTexts:
    pceDiscCapPathScopeEntry.setStatus("current")
_PceDiscCapPathScopeIntraArea_Type = TruthValue
_PceDiscCapPathScopeIntraArea_Object = MibTableColumn
pceDiscCapPathScopeIntraArea = _PceDiscCapPathScopeIntraArea_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 1),
    _PceDiscCapPathScopeIntraArea_Type()
)
pceDiscCapPathScopeIntraArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapPathScopeIntraArea.setStatus("current")
_PceDiscCapPathScopeInterArea_Type = TruthValue
_PceDiscCapPathScopeInterArea_Object = MibTableColumn
pceDiscCapPathScopeInterArea = _PceDiscCapPathScopeInterArea_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 2),
    _PceDiscCapPathScopeInterArea_Type()
)
pceDiscCapPathScopeInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapPathScopeInterArea.setStatus("current")
_PceDiscCapPathScopeDefInterArea_Type = TruthValue
_PceDiscCapPathScopeDefInterArea_Object = MibTableColumn
pceDiscCapPathScopeDefInterArea = _PceDiscCapPathScopeDefInterArea_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 3),
    _PceDiscCapPathScopeDefInterArea_Type()
)
pceDiscCapPathScopeDefInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapPathScopeDefInterArea.setStatus("current")
_PceDiscCapPathScopeInterAS_Type = TruthValue
_PceDiscCapPathScopeInterAS_Object = MibTableColumn
pceDiscCapPathScopeInterAS = _PceDiscCapPathScopeInterAS_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 4),
    _PceDiscCapPathScopeInterAS_Type()
)
pceDiscCapPathScopeInterAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapPathScopeInterAS.setStatus("current")
_PceDiscCapPathScopeDefInterAS_Type = TruthValue
_PceDiscCapPathScopeDefInterAS_Object = MibTableColumn
pceDiscCapPathScopeDefInterAS = _PceDiscCapPathScopeDefInterAS_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 5),
    _PceDiscCapPathScopeDefInterAS_Type()
)
pceDiscCapPathScopeDefInterAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapPathScopeDefInterAS.setStatus("current")
_PceDiscCapPathScopeInterLayer_Type = TruthValue
_PceDiscCapPathScopeInterLayer_Object = MibTableColumn
pceDiscCapPathScopeInterLayer = _PceDiscCapPathScopeInterLayer_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 6),
    _PceDiscCapPathScopeInterLayer_Type()
)
pceDiscCapPathScopeInterLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapPathScopeInterLayer.setStatus("current")


class _PceDiscCapPathScopePrefIntraArea_Type(Integer32):
    """Custom type pceDiscCapPathScopePrefIntraArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PceDiscCapPathScopePrefIntraArea_Type.__name__ = "Integer32"
_PceDiscCapPathScopePrefIntraArea_Object = MibTableColumn
pceDiscCapPathScopePrefIntraArea = _PceDiscCapPathScopePrefIntraArea_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 7),
    _PceDiscCapPathScopePrefIntraArea_Type()
)
pceDiscCapPathScopePrefIntraArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapPathScopePrefIntraArea.setStatus("current")


class _PceDiscCapPathScopePrefInterArea_Type(Integer32):
    """Custom type pceDiscCapPathScopePrefInterArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PceDiscCapPathScopePrefInterArea_Type.__name__ = "Integer32"
_PceDiscCapPathScopePrefInterArea_Object = MibTableColumn
pceDiscCapPathScopePrefInterArea = _PceDiscCapPathScopePrefInterArea_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 8),
    _PceDiscCapPathScopePrefInterArea_Type()
)
pceDiscCapPathScopePrefInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapPathScopePrefInterArea.setStatus("current")


class _PceDiscCapPathScopePrefInterAS_Type(Integer32):
    """Custom type pceDiscCapPathScopePrefInterAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PceDiscCapPathScopePrefInterAS_Type.__name__ = "Integer32"
_PceDiscCapPathScopePrefInterAS_Object = MibTableColumn
pceDiscCapPathScopePrefInterAS = _PceDiscCapPathScopePrefInterAS_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 9),
    _PceDiscCapPathScopePrefInterAS_Type()
)
pceDiscCapPathScopePrefInterAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapPathScopePrefInterAS.setStatus("current")


class _PceDiscCapPathScopePrefIntLayer_Type(Integer32):
    """Custom type pceDiscCapPathScopePrefIntLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PceDiscCapPathScopePrefIntLayer_Type.__name__ = "Integer32"
_PceDiscCapPathScopePrefIntLayer_Object = MibTableColumn
pceDiscCapPathScopePrefIntLayer = _PceDiscCapPathScopePrefIntLayer_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 10),
    _PceDiscCapPathScopePrefIntLayer_Type()
)
pceDiscCapPathScopePrefIntLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapPathScopePrefIntLayer.setStatus("current")
_PceDiscCapDomainTable_Object = MibTable
pceDiscCapDomainTable = _PceDiscCapDomainTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pceDiscCapDomainTable.setStatus("current")
_PceDiscCapDomainEntry_Object = MibTableRow
pceDiscCapDomainEntry = _PceDiscCapDomainEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 2, 1)
)
pceDiscCapDomainEntry.setIndexNames(
    (0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"),
    (0, "PCE-DISC-STD-MIB", "pceDiscCapDomainIndex"),
)
if mibBuilder.loadTexts:
    pceDiscCapDomainEntry.setStatus("current")


class _PceDiscCapDomainIndex_Type(Integer32):
    """Custom type pceDiscCapDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PceDiscCapDomainIndex_Type.__name__ = "Integer32"
_PceDiscCapDomainIndex_Object = MibTableColumn
pceDiscCapDomainIndex = _PceDiscCapDomainIndex_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 2, 1, 1),
    _PceDiscCapDomainIndex_Type()
)
pceDiscCapDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pceDiscCapDomainIndex.setStatus("current")
_PceDiscCapDomainIDType_Type = AddressFamilyNumbers
_PceDiscCapDomainIDType_Object = MibTableColumn
pceDiscCapDomainIDType = _PceDiscCapDomainIDType_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 2, 1, 2),
    _PceDiscCapDomainIDType_Type()
)
pceDiscCapDomainIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapDomainIDType.setStatus("current")
_PceDiscCapDomainID_Type = PceRoutingDomainID
_PceDiscCapDomainID_Object = MibTableColumn
pceDiscCapDomainID = _PceDiscCapDomainID_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 2, 1, 3),
    _PceDiscCapDomainID_Type()
)
pceDiscCapDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapDomainID.setStatus("current")
_PceDiscCapDestDomainTable_Object = MibTable
pceDiscCapDestDomainTable = _PceDiscCapDestDomainTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pceDiscCapDestDomainTable.setStatus("current")
_PceDiscCapDestDomainEntry_Object = MibTableRow
pceDiscCapDestDomainEntry = _PceDiscCapDestDomainEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 3, 1)
)
pceDiscCapDestDomainEntry.setIndexNames(
    (0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"),
    (0, "PCE-DISC-STD-MIB", "pceDiscCapDestDomainIndex"),
)
if mibBuilder.loadTexts:
    pceDiscCapDestDomainEntry.setStatus("current")


class _PceDiscCapDestDomainIndex_Type(Integer32):
    """Custom type pceDiscCapDestDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PceDiscCapDestDomainIndex_Type.__name__ = "Integer32"
_PceDiscCapDestDomainIndex_Object = MibTableColumn
pceDiscCapDestDomainIndex = _PceDiscCapDestDomainIndex_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 3, 1, 1),
    _PceDiscCapDestDomainIndex_Type()
)
pceDiscCapDestDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pceDiscCapDestDomainIndex.setStatus("current")
_PceDiscCapDestDomainIDType_Type = AddressFamilyNumbers
_PceDiscCapDestDomainIDType_Object = MibTableColumn
pceDiscCapDestDomainIDType = _PceDiscCapDestDomainIDType_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 3, 1, 2),
    _PceDiscCapDestDomainIDType_Type()
)
pceDiscCapDestDomainIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapDestDomainIDType.setStatus("current")
_PceDiscCapDestDomainID_Type = PceRoutingDomainID
_PceDiscCapDestDomainID_Object = MibTableColumn
pceDiscCapDestDomainID = _PceDiscCapDestDomainID_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 3, 1, 3),
    _PceDiscCapDestDomainID_Type()
)
pceDiscCapDestDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCapDestDomainID.setStatus("current")
_PceDiscComputationOptionsObjects_ObjectIdentity = ObjectIdentity
pceDiscComputationOptionsObjects = _PceDiscComputationOptionsObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1, 3)
)
_PceDiscComputationOptionsTable_Object = MibTable
pceDiscComputationOptionsTable = _PceDiscComputationOptionsTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pceDiscComputationOptionsTable.setStatus("current")
_PceDiscComputationOptionsEntry_Object = MibTableRow
pceDiscComputationOptionsEntry = _PceDiscComputationOptionsEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 3, 1, 1)
)
pceDiscComputationOptionsEntry.setIndexNames(
    (0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"),
)
if mibBuilder.loadTexts:
    pceDiscComputationOptionsEntry.setStatus("current")


class _PceDiscCompOptionsRpriority_Type(Integer32):
    """Custom type pceDiscCompOptionsRpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_PceDiscCompOptionsRpriority_Type.__name__ = "Integer32"
_PceDiscCompOptionsRpriority_Object = MibTableColumn
pceDiscCompOptionsRpriority = _PceDiscCompOptionsRpriority_Object(
    (1, 3, 6, 1, 3, 10000, 1, 3, 1, 1, 1),
    _PceDiscCompOptionsRpriority_Type()
)
pceDiscCompOptionsRpriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCompOptionsRpriority.setStatus("current")


class _PceDiscCompOptionsMmessages_Type(Integer32):
    """Custom type pceDiscCompOptionsMmessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_PceDiscCompOptionsMmessages_Type.__name__ = "Integer32"
_PceDiscCompOptionsMmessages_Object = MibTableColumn
pceDiscCompOptionsMmessages = _PceDiscCompOptionsMmessages_Object(
    (1, 3, 6, 1, 3, 10000, 1, 3, 1, 1, 2),
    _PceDiscCompOptionsMmessages_Type()
)
pceDiscCompOptionsMmessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pceDiscCompOptionsMmessages.setStatus("current")
_PceDiscActivityObjects_ObjectIdentity = ObjectIdentity
pceDiscActivityObjects = _PceDiscActivityObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1, 4)
)
_PceDiscActivityTable_Object = MibTable
pceDiscActivityTable = _PceDiscActivityTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pceDiscActivityTable.setStatus("current")
_PceDiscActivityEntry_Object = MibTableRow
pceDiscActivityEntry = _PceDiscActivityEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 4, 1, 1)
)
pceDiscActivityEntry.setIndexNames(
    (0, "PCE-DISC-STD-MIB", "pceDiscoveryIndex"),
)
if mibBuilder.loadTexts:
    pceDiscActivityEntry.setStatus("current")


class _PceDiscActivityTlvsRecv_Type(Integer32):
    """Custom type pceDiscActivityTlvsRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PceDiscActivityTlvsRecv_Type.__name__ = "Integer32"
_PceDiscActivityTlvsRecv_Object = MibTableColumn
pceDiscActivityTlvsRecv = _PceDiscActivityTlvsRecv_Object(
    (1, 3, 6, 1, 3, 10000, 1, 4, 1, 1, 1),
    _PceDiscActivityTlvsRecv_Type()
)
pceDiscActivityTlvsRecv.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pceDiscActivityTlvsRecv.setStatus("current")


class _PceDiscActivityErroredTlvsRecv_Type(Integer32):
    """Custom type pceDiscActivityErroredTlvsRecv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PceDiscActivityErroredTlvsRecv_Type.__name__ = "Integer32"
_PceDiscActivityErroredTlvsRecv_Object = MibTableColumn
pceDiscActivityErroredTlvsRecv = _PceDiscActivityErroredTlvsRecv_Object(
    (1, 3, 6, 1, 3, 10000, 1, 4, 1, 1, 2),
    _PceDiscActivityErroredTlvsRecv_Type()
)
pceDiscActivityErroredTlvsRecv.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pceDiscActivityErroredTlvsRecv.setStatus("current")
_PceDiscConformance_ObjectIdentity = ObjectIdentity
pceDiscConformance = _PceDiscConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 2)
)
_PceDiscGroups_ObjectIdentity = ObjectIdentity
pceDiscGroups = _PceDiscGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 2, 1)
)
_PceDiscCompliances_ObjectIdentity = ObjectIdentity
pceDiscCompliances = _PceDiscCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pceDiscGeneralPceInformation = ModuleCompliance(
    (1, 3, 6, 1, 3, 10000, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pceDiscGeneralPceInformation.setStatus(
        "current"
    )

pceDiscDetailledPceInformation = ModuleCompliance(
    (1, 3, 6, 1, 3, 10000, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pceDiscDetailledPceInformation.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCE-DISC-STD-MIB",
    **{"PceRoutingDomainID": PceRoutingDomainID,
       "pceDiscStdMIB": pceDiscStdMIB,
       "pceDiscNotifications": pceDiscNotifications,
       "pceDiscMIBObjects": pceDiscMIBObjects,
       "pceDiscoveryObjects": pceDiscoveryObjects,
       "pceDiscoveryAdminStatus": pceDiscoveryAdminStatus,
       "pceDiscoveryKnowPCEs": pceDiscoveryKnowPCEs,
       "pceDiscoveryActivePCEs": pceDiscoveryActivePCEs,
       "pceDiscoveryTable": pceDiscoveryTable,
       "pceDiscoveryEntry": pceDiscoveryEntry,
       "pceDiscoveryIndex": pceDiscoveryIndex,
       "pceDiscoveryMechanism": pceDiscoveryMechanism,
       "pceDiscoveryIPv4Address": pceDiscoveryIPv4Address,
       "pceDiscoveryIPv6Address": pceDiscoveryIPv6Address,
       "pceDiscoveryTime": pceDiscoveryTime,
       "pceDiscoveryLastUpdated": pceDiscoveryLastUpdated,
       "pceDiscoveryCongestion": pceDiscoveryCongestion,
       "pceDiscoveryCongestionDuration": pceDiscoveryCongestionDuration,
       "pceDiscCapabilityObjects": pceDiscCapabilityObjects,
       "pceDiscCapPathScopeTable": pceDiscCapPathScopeTable,
       "pceDiscCapPathScopeEntry": pceDiscCapPathScopeEntry,
       "pceDiscCapPathScopeIntraArea": pceDiscCapPathScopeIntraArea,
       "pceDiscCapPathScopeInterArea": pceDiscCapPathScopeInterArea,
       "pceDiscCapPathScopeDefInterArea": pceDiscCapPathScopeDefInterArea,
       "pceDiscCapPathScopeInterAS": pceDiscCapPathScopeInterAS,
       "pceDiscCapPathScopeDefInterAS": pceDiscCapPathScopeDefInterAS,
       "pceDiscCapPathScopeInterLayer": pceDiscCapPathScopeInterLayer,
       "pceDiscCapPathScopePrefIntraArea": pceDiscCapPathScopePrefIntraArea,
       "pceDiscCapPathScopePrefInterArea": pceDiscCapPathScopePrefInterArea,
       "pceDiscCapPathScopePrefInterAS": pceDiscCapPathScopePrefInterAS,
       "pceDiscCapPathScopePrefIntLayer": pceDiscCapPathScopePrefIntLayer,
       "pceDiscCapDomainTable": pceDiscCapDomainTable,
       "pceDiscCapDomainEntry": pceDiscCapDomainEntry,
       "pceDiscCapDomainIndex": pceDiscCapDomainIndex,
       "pceDiscCapDomainIDType": pceDiscCapDomainIDType,
       "pceDiscCapDomainID": pceDiscCapDomainID,
       "pceDiscCapDestDomainTable": pceDiscCapDestDomainTable,
       "pceDiscCapDestDomainEntry": pceDiscCapDestDomainEntry,
       "pceDiscCapDestDomainIndex": pceDiscCapDestDomainIndex,
       "pceDiscCapDestDomainIDType": pceDiscCapDestDomainIDType,
       "pceDiscCapDestDomainID": pceDiscCapDestDomainID,
       "pceDiscComputationOptionsObjects": pceDiscComputationOptionsObjects,
       "pceDiscComputationOptionsTable": pceDiscComputationOptionsTable,
       "pceDiscComputationOptionsEntry": pceDiscComputationOptionsEntry,
       "pceDiscCompOptionsRpriority": pceDiscCompOptionsRpriority,
       "pceDiscCompOptionsMmessages": pceDiscCompOptionsMmessages,
       "pceDiscActivityObjects": pceDiscActivityObjects,
       "pceDiscActivityTable": pceDiscActivityTable,
       "pceDiscActivityEntry": pceDiscActivityEntry,
       "pceDiscActivityTlvsRecv": pceDiscActivityTlvsRecv,
       "pceDiscActivityErroredTlvsRecv": pceDiscActivityErroredTlvsRecv,
       "pceDiscConformance": pceDiscConformance,
       "pceDiscGroups": pceDiscGroups,
       "pceDiscCompliances": pceDiscCompliances,
       "pceDiscGeneralPceInformation": pceDiscGeneralPceInformation,
       "pceDiscDetailledPceInformation": pceDiscDetailledPceInformation}
)
