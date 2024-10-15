# SNMP MIB module (CISCO-SCAS-BB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SCAS-BB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:57 2024
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

(linkIndex,
 linkModuleIndex,
 pmoduleIndex,
 spvIndex) = mibBuilder.importSymbols(
    "PCUBE-SE-MIB",
    "linkIndex",
    "linkModuleIndex",
    "pmoduleIndex",
    "spvIndex")

(pcubeModules,
 pcubeWorkgroup) = mibBuilder.importSymbols(
    "PCUBE-SMI",
    "pcubeModules",
    "pcubeWorkgroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pcubeEngageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4)
)
pcubeEngageMIB.setRevisions(
        ("2006-05-10 00:00",
         "2004-12-21 00:00",
         "2004-07-01 00:00",
         "2002-07-03 20:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PcubeEngageConformance_ObjectIdentity = ObjectIdentity
pcubeEngageConformance = _PcubeEngageConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3)
)
_PcubeEngageGroups_ObjectIdentity = ObjectIdentity
pcubeEngageGroups = _PcubeEngageGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1)
)
_PcubeEngageCompliances_ObjectIdentity = ObjectIdentity
pcubeEngageCompliances = _PcubeEngageCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 2)
)
_PcubeEngageObjs_ObjectIdentity = ObjectIdentity
pcubeEngageObjs = _PcubeEngageObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2)
)
_ServiceGrp_ObjectIdentity = ObjectIdentity
serviceGrp = _ServiceGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 1)
)
_ServiceTable_ObjectIdentity = ObjectIdentity
serviceTable = _ServiceTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 1, 1)
)
_LinkGrp_ObjectIdentity = ObjectIdentity
linkGrp = _LinkGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2)
)
_LinkServiceUsageTable_Object = MibTable
linkServiceUsageTable = _LinkServiceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    linkServiceUsageTable.setStatus("current")
_LinkServiceUsageEntry_Object = MibTableRow
linkServiceUsageEntry = _LinkServiceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1)
)
linkServiceUsageEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "linkModuleIndex"),
    (0, "PCUBE-SE-MIB", "linkIndex"),
    (0, "CISCO-SCAS-BB-MIB", "globalScopeServiceCounterIndex"),
)
if mibBuilder.loadTexts:
    linkServiceUsageEntry.setStatus("current")
_LinkServiceUsageUpVolume_Type = Counter32
_LinkServiceUsageUpVolume_Object = MibTableColumn
linkServiceUsageUpVolume = _LinkServiceUsageUpVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 1),
    _LinkServiceUsageUpVolume_Type()
)
linkServiceUsageUpVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageUpVolume.setStatus("current")
if mibBuilder.loadTexts:
    linkServiceUsageUpVolume.setUnits("KBytes")
_LinkServiceUsageDownVolume_Type = Counter32
_LinkServiceUsageDownVolume_Object = MibTableColumn
linkServiceUsageDownVolume = _LinkServiceUsageDownVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 2),
    _LinkServiceUsageDownVolume_Type()
)
linkServiceUsageDownVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageDownVolume.setStatus("current")
if mibBuilder.loadTexts:
    linkServiceUsageDownVolume.setUnits("KBytes")
_LinkServiceUsageNumSessions_Type = Counter32
_LinkServiceUsageNumSessions_Object = MibTableColumn
linkServiceUsageNumSessions = _LinkServiceUsageNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 3),
    _LinkServiceUsageNumSessions_Type()
)
linkServiceUsageNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageNumSessions.setStatus("current")
if mibBuilder.loadTexts:
    linkServiceUsageNumSessions.setUnits("sessions")
_LinkServiceUsageDuration_Type = Counter32
_LinkServiceUsageDuration_Object = MibTableColumn
linkServiceUsageDuration = _LinkServiceUsageDuration_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 4),
    _LinkServiceUsageDuration_Type()
)
linkServiceUsageDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageDuration.setStatus("current")
if mibBuilder.loadTexts:
    linkServiceUsageDuration.setUnits("seconds")
_LinkServiceUsageConcurrentSessions_Type = Counter32
_LinkServiceUsageConcurrentSessions_Object = MibTableColumn
linkServiceUsageConcurrentSessions = _LinkServiceUsageConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 5),
    _LinkServiceUsageConcurrentSessions_Type()
)
linkServiceUsageConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageConcurrentSessions.setStatus("current")
if mibBuilder.loadTexts:
    linkServiceUsageConcurrentSessions.setUnits("sessions")
_LinkServiceUsageActiveSubscribers_Type = Counter32
_LinkServiceUsageActiveSubscribers_Object = MibTableColumn
linkServiceUsageActiveSubscribers = _LinkServiceUsageActiveSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 6),
    _LinkServiceUsageActiveSubscribers_Type()
)
linkServiceUsageActiveSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUsageActiveSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    linkServiceUsageActiveSubscribers.setUnits("subscribers")
_LinkServiceUpDroppedPackets_Type = Counter32
_LinkServiceUpDroppedPackets_Object = MibTableColumn
linkServiceUpDroppedPackets = _LinkServiceUpDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 7),
    _LinkServiceUpDroppedPackets_Type()
)
linkServiceUpDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUpDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    linkServiceUpDroppedPackets.setUnits("packets")
_LinkServiceDownDroppedPackets_Type = Counter32
_LinkServiceDownDroppedPackets_Object = MibTableColumn
linkServiceDownDroppedPackets = _LinkServiceDownDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 8),
    _LinkServiceDownDroppedPackets_Type()
)
linkServiceDownDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceDownDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    linkServiceDownDroppedPackets.setUnits("packets")
_LinkServiceUpDroppedBytes_Type = Counter32
_LinkServiceUpDroppedBytes_Object = MibTableColumn
linkServiceUpDroppedBytes = _LinkServiceUpDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 9),
    _LinkServiceUpDroppedBytes_Type()
)
linkServiceUpDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceUpDroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    linkServiceUpDroppedBytes.setUnits("bytes")
_LinkServiceDownDroppedBytes_Type = Counter32
_LinkServiceDownDroppedBytes_Object = MibTableColumn
linkServiceDownDroppedBytes = _LinkServiceDownDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 2, 1, 1, 10),
    _LinkServiceDownDroppedBytes_Type()
)
linkServiceDownDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkServiceDownDroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    linkServiceDownDroppedBytes.setUnits("bytes")
_PackageGrp_ObjectIdentity = ObjectIdentity
packageGrp = _PackageGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3)
)
_PackageCounterTable_Object = MibTable
packageCounterTable = _PackageCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    packageCounterTable.setStatus("current")
_PackageCounterEntry_Object = MibTableRow
packageCounterEntry = _PackageCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1)
)
packageCounterEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "CISCO-SCAS-BB-MIB", "packageCounterIndex"),
)
if mibBuilder.loadTexts:
    packageCounterEntry.setStatus("current")


class _PackageCounterIndex_Type(Integer32):
    """Custom type packageCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PackageCounterIndex_Type.__name__ = "Integer32"
_PackageCounterIndex_Object = MibTableColumn
packageCounterIndex = _PackageCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 1),
    _PackageCounterIndex_Type()
)
packageCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    packageCounterIndex.setStatus("current")


class _PackageCounterStatus_Type(Integer32):
    """Custom type packageCounterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PackageCounterStatus_Type.__name__ = "Integer32"
_PackageCounterStatus_Object = MibTableColumn
packageCounterStatus = _PackageCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 2),
    _PackageCounterStatus_Type()
)
packageCounterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageCounterStatus.setStatus("current")
_PackageCounterName_Type = SnmpAdminString
_PackageCounterName_Object = MibTableColumn
packageCounterName = _PackageCounterName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 3),
    _PackageCounterName_Type()
)
packageCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageCounterName.setStatus("current")
_PackageCounterActiveSubscribers_Type = Counter32
_PackageCounterActiveSubscribers_Object = MibTableColumn
packageCounterActiveSubscribers = _PackageCounterActiveSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 1, 1, 4),
    _PackageCounterActiveSubscribers_Type()
)
packageCounterActiveSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageCounterActiveSubscribers.setStatus("current")
_PackageServiceUsageTable_Object = MibTable
packageServiceUsageTable = _PackageServiceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    packageServiceUsageTable.setStatus("current")
_PackageServiceUsageEntry_Object = MibTableRow
packageServiceUsageEntry = _PackageServiceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1)
)
packageServiceUsageEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "CISCO-SCAS-BB-MIB", "packageCounterIndex"),
    (0, "CISCO-SCAS-BB-MIB", "globalScopeServiceCounterIndex"),
)
if mibBuilder.loadTexts:
    packageServiceUsageEntry.setStatus("current")
_PackageServiceUsageUpVolume_Type = Counter32
_PackageServiceUsageUpVolume_Object = MibTableColumn
packageServiceUsageUpVolume = _PackageServiceUsageUpVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 1),
    _PackageServiceUsageUpVolume_Type()
)
packageServiceUsageUpVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageUpVolume.setStatus("current")
if mibBuilder.loadTexts:
    packageServiceUsageUpVolume.setUnits("KBytes")
_PackageServiceUsageDownVolume_Type = Counter32
_PackageServiceUsageDownVolume_Object = MibTableColumn
packageServiceUsageDownVolume = _PackageServiceUsageDownVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 2),
    _PackageServiceUsageDownVolume_Type()
)
packageServiceUsageDownVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageDownVolume.setStatus("current")
if mibBuilder.loadTexts:
    packageServiceUsageDownVolume.setUnits("KBytes")
_PackageServiceUsageNumSessions_Type = Counter32
_PackageServiceUsageNumSessions_Object = MibTableColumn
packageServiceUsageNumSessions = _PackageServiceUsageNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 3),
    _PackageServiceUsageNumSessions_Type()
)
packageServiceUsageNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageNumSessions.setStatus("current")
if mibBuilder.loadTexts:
    packageServiceUsageNumSessions.setUnits("sessions")
_PackageServiceUsageDuration_Type = Counter32
_PackageServiceUsageDuration_Object = MibTableColumn
packageServiceUsageDuration = _PackageServiceUsageDuration_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 4),
    _PackageServiceUsageDuration_Type()
)
packageServiceUsageDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageDuration.setStatus("current")
if mibBuilder.loadTexts:
    packageServiceUsageDuration.setUnits("seconds")
_PackageServiceUsageConcurrentSessions_Type = Counter32
_PackageServiceUsageConcurrentSessions_Object = MibTableColumn
packageServiceUsageConcurrentSessions = _PackageServiceUsageConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 5),
    _PackageServiceUsageConcurrentSessions_Type()
)
packageServiceUsageConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageConcurrentSessions.setStatus("current")
if mibBuilder.loadTexts:
    packageServiceUsageConcurrentSessions.setUnits("sessions")
_PackageServiceUsageActiveSubscribers_Type = Counter32
_PackageServiceUsageActiveSubscribers_Object = MibTableColumn
packageServiceUsageActiveSubscribers = _PackageServiceUsageActiveSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 6),
    _PackageServiceUsageActiveSubscribers_Type()
)
packageServiceUsageActiveSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUsageActiveSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    packageServiceUsageActiveSubscribers.setUnits("subscribers")
_PackageServiceUpDroppedPackets_Type = Counter32
_PackageServiceUpDroppedPackets_Object = MibTableColumn
packageServiceUpDroppedPackets = _PackageServiceUpDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 7),
    _PackageServiceUpDroppedPackets_Type()
)
packageServiceUpDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUpDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    packageServiceUpDroppedPackets.setUnits("packets")
_PackageServiceDownDroppedPackets_Type = Counter32
_PackageServiceDownDroppedPackets_Object = MibTableColumn
packageServiceDownDroppedPackets = _PackageServiceDownDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 8),
    _PackageServiceDownDroppedPackets_Type()
)
packageServiceDownDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceDownDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    packageServiceDownDroppedPackets.setUnits("packets")
_PackageServiceUpDroppedBytes_Type = Counter32
_PackageServiceUpDroppedBytes_Object = MibTableColumn
packageServiceUpDroppedBytes = _PackageServiceUpDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 9),
    _PackageServiceUpDroppedBytes_Type()
)
packageServiceUpDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceUpDroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    packageServiceUpDroppedBytes.setUnits("bytes")
_PackageServiceDownDroppedBytes_Type = Counter32
_PackageServiceDownDroppedBytes_Object = MibTableColumn
packageServiceDownDroppedBytes = _PackageServiceDownDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 3, 2, 1, 10),
    _PackageServiceDownDroppedBytes_Type()
)
packageServiceDownDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageServiceDownDroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    packageServiceDownDroppedBytes.setUnits("bytes")
_SubscriberGrp_ObjectIdentity = ObjectIdentity
subscriberGrp = _SubscriberGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4)
)
_SubscribersTable_Object = MibTable
subscribersTable = _SubscribersTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    subscribersTable.setStatus("current")
_SubscribersEntry_Object = MibTableRow
subscribersEntry = _SubscribersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 1, 1)
)
subscribersEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "spvIndex"),
)
if mibBuilder.loadTexts:
    subscribersEntry.setStatus("current")


class _SubscriberPackageIndex_Type(Integer32):
    """Custom type subscriberPackageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SubscriberPackageIndex_Type.__name__ = "Integer32"
_SubscriberPackageIndex_Object = MibTableColumn
subscriberPackageIndex = _SubscriberPackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 1, 1, 1),
    _SubscriberPackageIndex_Type()
)
subscriberPackageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberPackageIndex.setStatus("current")
_SubscriberServiceUsageTable_Object = MibTable
subscriberServiceUsageTable = _SubscriberServiceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2)
)
if mibBuilder.loadTexts:
    subscriberServiceUsageTable.setStatus("current")
_SubscriberServiceUsageEntry_Object = MibTableRow
subscriberServiceUsageEntry = _SubscriberServiceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1)
)
subscriberServiceUsageEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "PCUBE-SE-MIB", "spvIndex"),
    (0, "CISCO-SCAS-BB-MIB", "subscriberScopeServiceCounterIndex"),
)
if mibBuilder.loadTexts:
    subscriberServiceUsageEntry.setStatus("current")
_SubscriberServiceUsageUpVolume_Type = Counter32
_SubscriberServiceUsageUpVolume_Object = MibTableColumn
subscriberServiceUsageUpVolume = _SubscriberServiceUsageUpVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 1),
    _SubscriberServiceUsageUpVolume_Type()
)
subscriberServiceUsageUpVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServiceUsageUpVolume.setStatus("current")
if mibBuilder.loadTexts:
    subscriberServiceUsageUpVolume.setUnits("KBytes")
_SubscriberServiceUsageDownVolume_Type = Counter32
_SubscriberServiceUsageDownVolume_Object = MibTableColumn
subscriberServiceUsageDownVolume = _SubscriberServiceUsageDownVolume_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 2),
    _SubscriberServiceUsageDownVolume_Type()
)
subscriberServiceUsageDownVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServiceUsageDownVolume.setStatus("current")
if mibBuilder.loadTexts:
    subscriberServiceUsageDownVolume.setUnits("KBytes")


class _SubscriberServiceUsageNumSessions_Type(Integer32):
    """Custom type subscriberServiceUsageNumSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SubscriberServiceUsageNumSessions_Type.__name__ = "Integer32"
_SubscriberServiceUsageNumSessions_Object = MibTableColumn
subscriberServiceUsageNumSessions = _SubscriberServiceUsageNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 3),
    _SubscriberServiceUsageNumSessions_Type()
)
subscriberServiceUsageNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServiceUsageNumSessions.setStatus("current")
if mibBuilder.loadTexts:
    subscriberServiceUsageNumSessions.setUnits("sessions")


class _SubscriberServiceUsageDuration_Type(Integer32):
    """Custom type subscriberServiceUsageDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SubscriberServiceUsageDuration_Type.__name__ = "Integer32"
_SubscriberServiceUsageDuration_Object = MibTableColumn
subscriberServiceUsageDuration = _SubscriberServiceUsageDuration_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 4, 2, 1, 4),
    _SubscriberServiceUsageDuration_Type()
)
subscriberServiceUsageDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServiceUsageDuration.setStatus("current")
if mibBuilder.loadTexts:
    subscriberServiceUsageDuration.setUnits("seconds")
_ServiceCounterGrp_ObjectIdentity = ObjectIdentity
serviceCounterGrp = _ServiceCounterGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5)
)
_GlobalScopeServiceCounterTable_Object = MibTable
globalScopeServiceCounterTable = _GlobalScopeServiceCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    globalScopeServiceCounterTable.setStatus("current")
_GlobalScopeServiceCounterEntry_Object = MibTableRow
globalScopeServiceCounterEntry = _GlobalScopeServiceCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1)
)
globalScopeServiceCounterEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "CISCO-SCAS-BB-MIB", "globalScopeServiceCounterIndex"),
)
if mibBuilder.loadTexts:
    globalScopeServiceCounterEntry.setStatus("current")


class _GlobalScopeServiceCounterIndex_Type(Integer32):
    """Custom type globalScopeServiceCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GlobalScopeServiceCounterIndex_Type.__name__ = "Integer32"
_GlobalScopeServiceCounterIndex_Object = MibTableColumn
globalScopeServiceCounterIndex = _GlobalScopeServiceCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1, 1),
    _GlobalScopeServiceCounterIndex_Type()
)
globalScopeServiceCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    globalScopeServiceCounterIndex.setStatus("current")


class _GlobalScopeServiceCounterStatus_Type(Integer32):
    """Custom type globalScopeServiceCounterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GlobalScopeServiceCounterStatus_Type.__name__ = "Integer32"
_GlobalScopeServiceCounterStatus_Object = MibTableColumn
globalScopeServiceCounterStatus = _GlobalScopeServiceCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1, 2),
    _GlobalScopeServiceCounterStatus_Type()
)
globalScopeServiceCounterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalScopeServiceCounterStatus.setStatus("current")
_GlobalScopeServiceCounterName_Type = SnmpAdminString
_GlobalScopeServiceCounterName_Object = MibTableColumn
globalScopeServiceCounterName = _GlobalScopeServiceCounterName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 1, 1, 3),
    _GlobalScopeServiceCounterName_Type()
)
globalScopeServiceCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalScopeServiceCounterName.setStatus("current")
_SubscriberScopeServiceCounterTable_Object = MibTable
subscriberScopeServiceCounterTable = _SubscriberScopeServiceCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2)
)
if mibBuilder.loadTexts:
    subscriberScopeServiceCounterTable.setStatus("current")
_SubscriberScopeServiceCounterEntry_Object = MibTableRow
subscriberScopeServiceCounterEntry = _SubscriberScopeServiceCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1)
)
subscriberScopeServiceCounterEntry.setIndexNames(
    (0, "PCUBE-SE-MIB", "pmoduleIndex"),
    (0, "CISCO-SCAS-BB-MIB", "subscriberScopeServiceCounterIndex"),
)
if mibBuilder.loadTexts:
    subscriberScopeServiceCounterEntry.setStatus("current")


class _SubscriberScopeServiceCounterIndex_Type(Integer32):
    """Custom type subscriberScopeServiceCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SubscriberScopeServiceCounterIndex_Type.__name__ = "Integer32"
_SubscriberScopeServiceCounterIndex_Object = MibTableColumn
subscriberScopeServiceCounterIndex = _SubscriberScopeServiceCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1, 1),
    _SubscriberScopeServiceCounterIndex_Type()
)
subscriberScopeServiceCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subscriberScopeServiceCounterIndex.setStatus("current")


class _SubscriberScopeServiceCounterStatus_Type(Integer32):
    """Custom type subscriberScopeServiceCounterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SubscriberScopeServiceCounterStatus_Type.__name__ = "Integer32"
_SubscriberScopeServiceCounterStatus_Object = MibTableColumn
subscriberScopeServiceCounterStatus = _SubscriberScopeServiceCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1, 2),
    _SubscriberScopeServiceCounterStatus_Type()
)
subscriberScopeServiceCounterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberScopeServiceCounterStatus.setStatus("current")
_SubscriberScopeServiceCounterName_Type = SnmpAdminString
_SubscriberScopeServiceCounterName_Object = MibTableColumn
subscriberScopeServiceCounterName = _SubscriberScopeServiceCounterName_Object(
    (1, 3, 6, 1, 4, 1, 5655, 4, 2, 5, 2, 1, 3),
    _SubscriberScopeServiceCounterName_Type()
)
subscriberScopeServiceCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberScopeServiceCounterName.setStatus("current")

# Managed Objects groups

pcubeLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 2)
)
pcubeLinkGroup.setObjects(
      *(("CISCO-SCAS-BB-MIB", "linkServiceUsageUpVolume"),
        ("CISCO-SCAS-BB-MIB", "linkServiceUsageDownVolume"),
        ("CISCO-SCAS-BB-MIB", "linkServiceUsageNumSessions"),
        ("CISCO-SCAS-BB-MIB", "linkServiceUsageDuration"),
        ("CISCO-SCAS-BB-MIB", "linkServiceUsageConcurrentSessions"),
        ("CISCO-SCAS-BB-MIB", "linkServiceUsageActiveSubscribers"),
        ("CISCO-SCAS-BB-MIB", "linkServiceUpDroppedPackets"),
        ("CISCO-SCAS-BB-MIB", "linkServiceDownDroppedPackets"),
        ("CISCO-SCAS-BB-MIB", "linkServiceUpDroppedBytes"),
        ("CISCO-SCAS-BB-MIB", "linkServiceDownDroppedBytes"))
)
if mibBuilder.loadTexts:
    pcubeLinkGroup.setStatus("current")

pcubePackageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 3)
)
pcubePackageGroup.setObjects(
      *(("CISCO-SCAS-BB-MIB", "packageCounterStatus"),
        ("CISCO-SCAS-BB-MIB", "packageCounterName"),
        ("CISCO-SCAS-BB-MIB", "packageCounterActiveSubscribers"),
        ("CISCO-SCAS-BB-MIB", "packageServiceUsageUpVolume"),
        ("CISCO-SCAS-BB-MIB", "packageServiceUsageDownVolume"),
        ("CISCO-SCAS-BB-MIB", "packageServiceUsageNumSessions"),
        ("CISCO-SCAS-BB-MIB", "packageServiceUsageDuration"),
        ("CISCO-SCAS-BB-MIB", "packageServiceUsageConcurrentSessions"),
        ("CISCO-SCAS-BB-MIB", "packageServiceUsageActiveSubscribers"),
        ("CISCO-SCAS-BB-MIB", "packageServiceUpDroppedPackets"),
        ("CISCO-SCAS-BB-MIB", "packageServiceDownDroppedPackets"),
        ("CISCO-SCAS-BB-MIB", "packageServiceUpDroppedBytes"),
        ("CISCO-SCAS-BB-MIB", "packageServiceDownDroppedBytes"))
)
if mibBuilder.loadTexts:
    pcubePackageGroup.setStatus("current")

pcubeSubscriberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 4)
)
pcubeSubscriberGroup.setObjects(
      *(("CISCO-SCAS-BB-MIB", "subscriberPackageIndex"),
        ("CISCO-SCAS-BB-MIB", "subscriberServiceUsageUpVolume"),
        ("CISCO-SCAS-BB-MIB", "subscriberServiceUsageDownVolume"),
        ("CISCO-SCAS-BB-MIB", "subscriberServiceUsageNumSessions"),
        ("CISCO-SCAS-BB-MIB", "subscriberServiceUsageDuration"))
)
if mibBuilder.loadTexts:
    pcubeSubscriberGroup.setStatus("current")

pcubeServiceCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 1, 5)
)
pcubeServiceCounterGroup.setObjects(
      *(("CISCO-SCAS-BB-MIB", "globalScopeServiceCounterStatus"),
        ("CISCO-SCAS-BB-MIB", "globalScopeServiceCounterName"),
        ("CISCO-SCAS-BB-MIB", "subscriberScopeServiceCounterStatus"),
        ("CISCO-SCAS-BB-MIB", "subscriberScopeServiceCounterName"))
)
if mibBuilder.loadTexts:
    pcubeServiceCounterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pcubeEngageCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5655, 2, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    pcubeEngageCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SCAS-BB-MIB",
    **{"pcubeEngageMIB": pcubeEngageMIB,
       "pcubeEngageConformance": pcubeEngageConformance,
       "pcubeEngageGroups": pcubeEngageGroups,
       "pcubeLinkGroup": pcubeLinkGroup,
       "pcubePackageGroup": pcubePackageGroup,
       "pcubeSubscriberGroup": pcubeSubscriberGroup,
       "pcubeServiceCounterGroup": pcubeServiceCounterGroup,
       "pcubeEngageCompliances": pcubeEngageCompliances,
       "pcubeEngageCompliance": pcubeEngageCompliance,
       "pcubeEngageObjs": pcubeEngageObjs,
       "serviceGrp": serviceGrp,
       "serviceTable": serviceTable,
       "linkGrp": linkGrp,
       "linkServiceUsageTable": linkServiceUsageTable,
       "linkServiceUsageEntry": linkServiceUsageEntry,
       "linkServiceUsageUpVolume": linkServiceUsageUpVolume,
       "linkServiceUsageDownVolume": linkServiceUsageDownVolume,
       "linkServiceUsageNumSessions": linkServiceUsageNumSessions,
       "linkServiceUsageDuration": linkServiceUsageDuration,
       "linkServiceUsageConcurrentSessions": linkServiceUsageConcurrentSessions,
       "linkServiceUsageActiveSubscribers": linkServiceUsageActiveSubscribers,
       "linkServiceUpDroppedPackets": linkServiceUpDroppedPackets,
       "linkServiceDownDroppedPackets": linkServiceDownDroppedPackets,
       "linkServiceUpDroppedBytes": linkServiceUpDroppedBytes,
       "linkServiceDownDroppedBytes": linkServiceDownDroppedBytes,
       "packageGrp": packageGrp,
       "packageCounterTable": packageCounterTable,
       "packageCounterEntry": packageCounterEntry,
       "packageCounterIndex": packageCounterIndex,
       "packageCounterStatus": packageCounterStatus,
       "packageCounterName": packageCounterName,
       "packageCounterActiveSubscribers": packageCounterActiveSubscribers,
       "packageServiceUsageTable": packageServiceUsageTable,
       "packageServiceUsageEntry": packageServiceUsageEntry,
       "packageServiceUsageUpVolume": packageServiceUsageUpVolume,
       "packageServiceUsageDownVolume": packageServiceUsageDownVolume,
       "packageServiceUsageNumSessions": packageServiceUsageNumSessions,
       "packageServiceUsageDuration": packageServiceUsageDuration,
       "packageServiceUsageConcurrentSessions": packageServiceUsageConcurrentSessions,
       "packageServiceUsageActiveSubscribers": packageServiceUsageActiveSubscribers,
       "packageServiceUpDroppedPackets": packageServiceUpDroppedPackets,
       "packageServiceDownDroppedPackets": packageServiceDownDroppedPackets,
       "packageServiceUpDroppedBytes": packageServiceUpDroppedBytes,
       "packageServiceDownDroppedBytes": packageServiceDownDroppedBytes,
       "subscriberGrp": subscriberGrp,
       "subscribersTable": subscribersTable,
       "subscribersEntry": subscribersEntry,
       "subscriberPackageIndex": subscriberPackageIndex,
       "subscriberServiceUsageTable": subscriberServiceUsageTable,
       "subscriberServiceUsageEntry": subscriberServiceUsageEntry,
       "subscriberServiceUsageUpVolume": subscriberServiceUsageUpVolume,
       "subscriberServiceUsageDownVolume": subscriberServiceUsageDownVolume,
       "subscriberServiceUsageNumSessions": subscriberServiceUsageNumSessions,
       "subscriberServiceUsageDuration": subscriberServiceUsageDuration,
       "serviceCounterGrp": serviceCounterGrp,
       "globalScopeServiceCounterTable": globalScopeServiceCounterTable,
       "globalScopeServiceCounterEntry": globalScopeServiceCounterEntry,
       "globalScopeServiceCounterIndex": globalScopeServiceCounterIndex,
       "globalScopeServiceCounterStatus": globalScopeServiceCounterStatus,
       "globalScopeServiceCounterName": globalScopeServiceCounterName,
       "subscriberScopeServiceCounterTable": subscriberScopeServiceCounterTable,
       "subscriberScopeServiceCounterEntry": subscriberScopeServiceCounterEntry,
       "subscriberScopeServiceCounterIndex": subscriberScopeServiceCounterIndex,
       "subscriberScopeServiceCounterStatus": subscriberScopeServiceCounterStatus,
       "subscriberScopeServiceCounterName": subscriberScopeServiceCounterName}
)
