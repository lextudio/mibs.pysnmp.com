# SNMP MIB module (PCC-PCEDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PCC-PCEDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:04 2024
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

pccPcedpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 10000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PccPceDpRoutingDomainID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



# MIB Managed Objects in the order of their OIDs

_PccPcedpNotifications_ObjectIdentity = ObjectIdentity
pccPcedpNotifications = _PccPcedpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 0)
)
_PccPcedpMIBObjects_ObjectIdentity = ObjectIdentity
pccPcedpMIBObjects = _PccPcedpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1)
)
_PccPcedpDiscoveryObjects_ObjectIdentity = ObjectIdentity
pccPcedpDiscoveryObjects = _PccPcedpDiscoveryObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1, 1)
)


class _PccPcedpDiscAdminStatus_Type(Integer32):
    """Custom type pccPcedpDiscAdminStatus based on Integer32"""
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


_PccPcedpDiscAdminStatus_Type.__name__ = "Integer32"
_PccPcedpDiscAdminStatus_Object = MibScalar
pccPcedpDiscAdminStatus = _PccPcedpDiscAdminStatus_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 1),
    _PccPcedpDiscAdminStatus_Type()
)
pccPcedpDiscAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pccPcedpDiscAdminStatus.setStatus("current")
_PccPcedpDiscKnowPCEs_Type = Counter32
_PccPcedpDiscKnowPCEs_Object = MibScalar
pccPcedpDiscKnowPCEs = _PccPcedpDiscKnowPCEs_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 2),
    _PccPcedpDiscKnowPCEs_Type()
)
pccPcedpDiscKnowPCEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpDiscKnowPCEs.setStatus("current")
_PccPcedpDiscActivePCEs_Type = Counter32
_PccPcedpDiscActivePCEs_Object = MibScalar
pccPcedpDiscActivePCEs = _PccPcedpDiscActivePCEs_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 3),
    _PccPcedpDiscActivePCEs_Type()
)
pccPcedpDiscActivePCEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpDiscActivePCEs.setStatus("current")
_PccPcedpDiscPceTable_Object = MibTable
pccPcedpDiscPceTable = _PccPcedpDiscPceTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pccPcedpDiscPceTable.setStatus("current")
_PccPcedpDiscPceEntry_Object = MibTableRow
pccPcedpDiscPceEntry = _PccPcedpDiscPceEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1)
)
pccPcedpDiscPceEntry.setIndexNames(
    (0, "PCC-PCEDP-MIB", "pccPcedpDiscPceIndex"),
)
if mibBuilder.loadTexts:
    pccPcedpDiscPceEntry.setStatus("current")


class _PccPcedpDiscPceIndex_Type(Integer32):
    """Custom type pccPcedpDiscPceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PccPcedpDiscPceIndex_Type.__name__ = "Integer32"
_PccPcedpDiscPceIndex_Object = MibTableColumn
pccPcedpDiscPceIndex = _PccPcedpDiscPceIndex_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 1),
    _PccPcedpDiscPceIndex_Type()
)
pccPcedpDiscPceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pccPcedpDiscPceIndex.setStatus("current")
_PccPcedpDiscMechanism_Type = IANAipRouteProtocol
_PccPcedpDiscMechanism_Object = MibTableColumn
pccPcedpDiscMechanism = _PccPcedpDiscMechanism_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 2),
    _PccPcedpDiscMechanism_Type()
)
pccPcedpDiscMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpDiscMechanism.setStatus("current")
_PccPcedpDiscPceIPv4Address_Type = IpAddress
_PccPcedpDiscPceIPv4Address_Object = MibTableColumn
pccPcedpDiscPceIPv4Address = _PccPcedpDiscPceIPv4Address_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 3),
    _PccPcedpDiscPceIPv4Address_Type()
)
pccPcedpDiscPceIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpDiscPceIPv4Address.setStatus("current")
_PccPcedpDiscPceIPv6Address_Type = Ipv6Address
_PccPcedpDiscPceIPv6Address_Object = MibTableColumn
pccPcedpDiscPceIPv6Address = _PccPcedpDiscPceIPv6Address_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 4),
    _PccPcedpDiscPceIPv6Address_Type()
)
pccPcedpDiscPceIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpDiscPceIPv6Address.setStatus("current")
_PccPcedpDiscPceTime_Type = TimeStamp
_PccPcedpDiscPceTime_Object = MibTableColumn
pccPcedpDiscPceTime = _PccPcedpDiscPceTime_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 5),
    _PccPcedpDiscPceTime_Type()
)
pccPcedpDiscPceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpDiscPceTime.setStatus("current")
_PccPcedpDiscPceLastUpdated_Type = TimeStamp
_PccPcedpDiscPceLastUpdated_Object = MibTableColumn
pccPcedpDiscPceLastUpdated = _PccPcedpDiscPceLastUpdated_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 4, 1, 6),
    _PccPcedpDiscPceLastUpdated_Type()
)
pccPcedpDiscPceLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpDiscPceLastUpdated.setStatus("current")
_PccPcedpDiscActTable_Object = MibTable
pccPcedpDiscActTable = _PccPcedpDiscActTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pccPcedpDiscActTable.setStatus("current")
_PccPcedpDiscActEntry_Object = MibTableRow
pccPcedpDiscActEntry = _PccPcedpDiscActEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 5, 1)
)
pccPcedpDiscActEntry.setIndexNames(
    (0, "PCC-PCEDP-MIB", "pccPcedpDiscPceIndex"),
)
if mibBuilder.loadTexts:
    pccPcedpDiscActEntry.setStatus("current")
_PccPcedpDiscActCongestion_Type = TruthValue
_PccPcedpDiscActCongestion_Object = MibTableColumn
pccPcedpDiscActCongestion = _PccPcedpDiscActCongestion_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 5, 1, 1),
    _PccPcedpDiscActCongestion_Type()
)
pccPcedpDiscActCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpDiscActCongestion.setStatus("current")
_PccPcedpDiscActCongestionDuration_Type = Unsigned32
_PccPcedpDiscActCongestionDuration_Object = MibTableColumn
pccPcedpDiscActCongestionDuration = _PccPcedpDiscActCongestionDuration_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 5, 1, 2),
    _PccPcedpDiscActCongestionDuration_Type()
)
pccPcedpDiscActCongestionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpDiscActCongestionDuration.setStatus("current")
_PccPcedpCapabilityObjects_ObjectIdentity = ObjectIdentity
pccPcedpCapabilityObjects = _PccPcedpCapabilityObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1, 2)
)
_PccPcedpCapPathScopeTable_Object = MibTable
pccPcedpCapPathScopeTable = _PccPcedpCapPathScopeTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pccPcedpCapPathScopeTable.setStatus("current")
_PccPcedpCapPathScopeEntry_Object = MibTableRow
pccPcedpCapPathScopeEntry = _PccPcedpCapPathScopeEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1)
)
pccPcedpCapPathScopeEntry.setIndexNames(
    (0, "PCC-PCEDP-MIB", "pccPcedpDiscPceIndex"),
)
if mibBuilder.loadTexts:
    pccPcedpCapPathScopeEntry.setStatus("current")
_PccPcedpCapPathScopeIntraArea_Type = TruthValue
_PccPcedpCapPathScopeIntraArea_Object = MibTableColumn
pccPcedpCapPathScopeIntraArea = _PccPcedpCapPathScopeIntraArea_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 1),
    _PccPcedpCapPathScopeIntraArea_Type()
)
pccPcedpCapPathScopeIntraArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapPathScopeIntraArea.setStatus("current")
_PccPcedpCapPathScopeInterArea_Type = TruthValue
_PccPcedpCapPathScopeInterArea_Object = MibTableColumn
pccPcedpCapPathScopeInterArea = _PccPcedpCapPathScopeInterArea_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 2),
    _PccPcedpCapPathScopeInterArea_Type()
)
pccPcedpCapPathScopeInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapPathScopeInterArea.setStatus("current")
_PccPcedpCapPathScopeDefaultInterArea_Type = TruthValue
_PccPcedpCapPathScopeDefaultInterArea_Object = MibTableColumn
pccPcedpCapPathScopeDefaultInterArea = _PccPcedpCapPathScopeDefaultInterArea_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 3),
    _PccPcedpCapPathScopeDefaultInterArea_Type()
)
pccPcedpCapPathScopeDefaultInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapPathScopeDefaultInterArea.setStatus("current")
_PccPcedpCapPathScopeInterAS_Type = TruthValue
_PccPcedpCapPathScopeInterAS_Object = MibTableColumn
pccPcedpCapPathScopeInterAS = _PccPcedpCapPathScopeInterAS_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 4),
    _PccPcedpCapPathScopeInterAS_Type()
)
pccPcedpCapPathScopeInterAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapPathScopeInterAS.setStatus("current")
_PccPcedpCapPathScopeDefaultInterAS_Type = TruthValue
_PccPcedpCapPathScopeDefaultInterAS_Object = MibTableColumn
pccPcedpCapPathScopeDefaultInterAS = _PccPcedpCapPathScopeDefaultInterAS_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 5),
    _PccPcedpCapPathScopeDefaultInterAS_Type()
)
pccPcedpCapPathScopeDefaultInterAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapPathScopeDefaultInterAS.setStatus("current")
_PccPcedpCapPathScopeInterLayer_Type = TruthValue
_PccPcedpCapPathScopeInterLayer_Object = MibTableColumn
pccPcedpCapPathScopeInterLayer = _PccPcedpCapPathScopeInterLayer_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 6),
    _PccPcedpCapPathScopeInterLayer_Type()
)
pccPcedpCapPathScopeInterLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapPathScopeInterLayer.setStatus("current")


class _PccPcedpCapPathScopePrefIntraArea_Type(Integer32):
    """Custom type pccPcedpCapPathScopePrefIntraArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PccPcedpCapPathScopePrefIntraArea_Type.__name__ = "Integer32"
_PccPcedpCapPathScopePrefIntraArea_Object = MibTableColumn
pccPcedpCapPathScopePrefIntraArea = _PccPcedpCapPathScopePrefIntraArea_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 7),
    _PccPcedpCapPathScopePrefIntraArea_Type()
)
pccPcedpCapPathScopePrefIntraArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapPathScopePrefIntraArea.setStatus("current")


class _PccPcedpCapPathScopePrefInterArea_Type(Integer32):
    """Custom type pccPcedpCapPathScopePrefInterArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PccPcedpCapPathScopePrefInterArea_Type.__name__ = "Integer32"
_PccPcedpCapPathScopePrefInterArea_Object = MibTableColumn
pccPcedpCapPathScopePrefInterArea = _PccPcedpCapPathScopePrefInterArea_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 8),
    _PccPcedpCapPathScopePrefInterArea_Type()
)
pccPcedpCapPathScopePrefInterArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapPathScopePrefInterArea.setStatus("current")


class _PccPcedpCapPathScopePrefInterAS_Type(Integer32):
    """Custom type pccPcedpCapPathScopePrefInterAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PccPcedpCapPathScopePrefInterAS_Type.__name__ = "Integer32"
_PccPcedpCapPathScopePrefInterAS_Object = MibTableColumn
pccPcedpCapPathScopePrefInterAS = _PccPcedpCapPathScopePrefInterAS_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 9),
    _PccPcedpCapPathScopePrefInterAS_Type()
)
pccPcedpCapPathScopePrefInterAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapPathScopePrefInterAS.setStatus("current")


class _PccPcedpCapPathScopePrefInterLayer_Type(Integer32):
    """Custom type pccPcedpCapPathScopePrefInterLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PccPcedpCapPathScopePrefInterLayer_Type.__name__ = "Integer32"
_PccPcedpCapPathScopePrefInterLayer_Object = MibTableColumn
pccPcedpCapPathScopePrefInterLayer = _PccPcedpCapPathScopePrefInterLayer_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 1, 1, 10),
    _PccPcedpCapPathScopePrefInterLayer_Type()
)
pccPcedpCapPathScopePrefInterLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapPathScopePrefInterLayer.setStatus("current")
_PccPcedpCapDomainTable_Object = MibTable
pccPcedpCapDomainTable = _PccPcedpCapDomainTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pccPcedpCapDomainTable.setStatus("current")
_PccPcedpCapDomainEntry_Object = MibTableRow
pccPcedpCapDomainEntry = _PccPcedpCapDomainEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 2, 1)
)
pccPcedpCapDomainEntry.setIndexNames(
    (0, "PCC-PCEDP-MIB", "pccPcedpDiscPceIndex"),
    (0, "PCC-PCEDP-MIB", "pccPcedpCapDomainIndex"),
)
if mibBuilder.loadTexts:
    pccPcedpCapDomainEntry.setStatus("current")


class _PccPcedpCapDomainIndex_Type(Integer32):
    """Custom type pccPcedpCapDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PccPcedpCapDomainIndex_Type.__name__ = "Integer32"
_PccPcedpCapDomainIndex_Object = MibTableColumn
pccPcedpCapDomainIndex = _PccPcedpCapDomainIndex_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 2, 1, 1),
    _PccPcedpCapDomainIndex_Type()
)
pccPcedpCapDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pccPcedpCapDomainIndex.setStatus("current")
_PccPcedpCapDomainIDType_Type = AddressFamilyNumbers
_PccPcedpCapDomainIDType_Object = MibTableColumn
pccPcedpCapDomainIDType = _PccPcedpCapDomainIDType_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 2, 1, 2),
    _PccPcedpCapDomainIDType_Type()
)
pccPcedpCapDomainIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapDomainIDType.setStatus("current")
_PccPcedpCapDomainID_Type = PccPceDpRoutingDomainID
_PccPcedpCapDomainID_Object = MibTableColumn
pccPcedpCapDomainID = _PccPcedpCapDomainID_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 2, 1, 3),
    _PccPcedpCapDomainID_Type()
)
pccPcedpCapDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapDomainID.setStatus("current")
_PccPcedpCapDestDomainTable_Object = MibTable
pccPcedpCapDestDomainTable = _PccPcedpCapDestDomainTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pccPcedpCapDestDomainTable.setStatus("current")
_PccPcedpCapDestDomainEntry_Object = MibTableRow
pccPcedpCapDestDomainEntry = _PccPcedpCapDestDomainEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 3, 1)
)
pccPcedpCapDestDomainEntry.setIndexNames(
    (0, "PCC-PCEDP-MIB", "pccPcedpDiscPceIndex"),
    (0, "PCC-PCEDP-MIB", "pccPcedpCapDestDomainIndex"),
)
if mibBuilder.loadTexts:
    pccPcedpCapDestDomainEntry.setStatus("current")


class _PccPcedpCapDestDomainIndex_Type(Integer32):
    """Custom type pccPcedpCapDestDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PccPcedpCapDestDomainIndex_Type.__name__ = "Integer32"
_PccPcedpCapDestDomainIndex_Object = MibTableColumn
pccPcedpCapDestDomainIndex = _PccPcedpCapDestDomainIndex_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 3, 1, 1),
    _PccPcedpCapDestDomainIndex_Type()
)
pccPcedpCapDestDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pccPcedpCapDestDomainIndex.setStatus("current")
_PccPcedpCapDestDomainIDType_Type = AddressFamilyNumbers
_PccPcedpCapDestDomainIDType_Object = MibTableColumn
pccPcedpCapDestDomainIDType = _PccPcedpCapDestDomainIDType_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 3, 1, 2),
    _PccPcedpCapDestDomainIDType_Type()
)
pccPcedpCapDestDomainIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapDestDomainIDType.setStatus("current")
_PccPcedpCapDestDomainID_Type = PccPceDpRoutingDomainID
_PccPcedpCapDestDomainID_Object = MibTableColumn
pccPcedpCapDestDomainID = _PccPcedpCapDestDomainID_Object(
    (1, 3, 6, 1, 3, 10000, 1, 2, 3, 1, 3),
    _PccPcedpCapDestDomainID_Type()
)
pccPcedpCapDestDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pccPcedpCapDestDomainID.setStatus("current")
_PccPcedpPceActivityGroup_ObjectIdentity = ObjectIdentity
pccPcedpPceActivityGroup = _PccPcedpPceActivityGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1, 3)
)
_PccPcedpConformance_ObjectIdentity = ObjectIdentity
pccPcedpConformance = _PccPcedpConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 2)
)
_PccPcedpGroups_ObjectIdentity = ObjectIdentity
pccPcedpGroups = _PccPcedpGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 2, 1)
)
_PccPcedpCompliances_ObjectIdentity = ObjectIdentity
pccPcedpCompliances = _PccPcedpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pccPcedpGeneralPceInformation = ModuleCompliance(
    (1, 3, 6, 1, 3, 10000, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pccPcedpGeneralPceInformation.setStatus(
        "current"
    )

pccPcedpDetailledPceInformation = ModuleCompliance(
    (1, 3, 6, 1, 3, 10000, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pccPcedpDetailledPceInformation.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCC-PCEDP-MIB",
    **{"PccPceDpRoutingDomainID": PccPceDpRoutingDomainID,
       "pccPcedpMIB": pccPcedpMIB,
       "pccPcedpNotifications": pccPcedpNotifications,
       "pccPcedpMIBObjects": pccPcedpMIBObjects,
       "pccPcedpDiscoveryObjects": pccPcedpDiscoveryObjects,
       "pccPcedpDiscAdminStatus": pccPcedpDiscAdminStatus,
       "pccPcedpDiscKnowPCEs": pccPcedpDiscKnowPCEs,
       "pccPcedpDiscActivePCEs": pccPcedpDiscActivePCEs,
       "pccPcedpDiscPceTable": pccPcedpDiscPceTable,
       "pccPcedpDiscPceEntry": pccPcedpDiscPceEntry,
       "pccPcedpDiscPceIndex": pccPcedpDiscPceIndex,
       "pccPcedpDiscMechanism": pccPcedpDiscMechanism,
       "pccPcedpDiscPceIPv4Address": pccPcedpDiscPceIPv4Address,
       "pccPcedpDiscPceIPv6Address": pccPcedpDiscPceIPv6Address,
       "pccPcedpDiscPceTime": pccPcedpDiscPceTime,
       "pccPcedpDiscPceLastUpdated": pccPcedpDiscPceLastUpdated,
       "pccPcedpDiscActTable": pccPcedpDiscActTable,
       "pccPcedpDiscActEntry": pccPcedpDiscActEntry,
       "pccPcedpDiscActCongestion": pccPcedpDiscActCongestion,
       "pccPcedpDiscActCongestionDuration": pccPcedpDiscActCongestionDuration,
       "pccPcedpCapabilityObjects": pccPcedpCapabilityObjects,
       "pccPcedpCapPathScopeTable": pccPcedpCapPathScopeTable,
       "pccPcedpCapPathScopeEntry": pccPcedpCapPathScopeEntry,
       "pccPcedpCapPathScopeIntraArea": pccPcedpCapPathScopeIntraArea,
       "pccPcedpCapPathScopeInterArea": pccPcedpCapPathScopeInterArea,
       "pccPcedpCapPathScopeDefaultInterArea": pccPcedpCapPathScopeDefaultInterArea,
       "pccPcedpCapPathScopeInterAS": pccPcedpCapPathScopeInterAS,
       "pccPcedpCapPathScopeDefaultInterAS": pccPcedpCapPathScopeDefaultInterAS,
       "pccPcedpCapPathScopeInterLayer": pccPcedpCapPathScopeInterLayer,
       "pccPcedpCapPathScopePrefIntraArea": pccPcedpCapPathScopePrefIntraArea,
       "pccPcedpCapPathScopePrefInterArea": pccPcedpCapPathScopePrefInterArea,
       "pccPcedpCapPathScopePrefInterAS": pccPcedpCapPathScopePrefInterAS,
       "pccPcedpCapPathScopePrefInterLayer": pccPcedpCapPathScopePrefInterLayer,
       "pccPcedpCapDomainTable": pccPcedpCapDomainTable,
       "pccPcedpCapDomainEntry": pccPcedpCapDomainEntry,
       "pccPcedpCapDomainIndex": pccPcedpCapDomainIndex,
       "pccPcedpCapDomainIDType": pccPcedpCapDomainIDType,
       "pccPcedpCapDomainID": pccPcedpCapDomainID,
       "pccPcedpCapDestDomainTable": pccPcedpCapDestDomainTable,
       "pccPcedpCapDestDomainEntry": pccPcedpCapDestDomainEntry,
       "pccPcedpCapDestDomainIndex": pccPcedpCapDestDomainIndex,
       "pccPcedpCapDestDomainIDType": pccPcedpCapDestDomainIDType,
       "pccPcedpCapDestDomainID": pccPcedpCapDestDomainID,
       "pccPcedpPceActivityGroup": pccPcedpPceActivityGroup,
       "pccPcedpConformance": pccPcedpConformance,
       "pccPcedpGroups": pccPcedpGroups,
       "pccPcedpCompliances": pccPcedpCompliances,
       "pccPcedpGeneralPceInformation": pccPcedpGeneralPceInformation,
       "pccPcedpDetailledPceInformation": pccPcedpDetailledPceInformation}
)
