# SNMP MIB module (WWP-LEOS-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:52 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosFilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15)
)
wwpLeosFilterMIB.setRevisions(
        ("2006-02-17 18:45",
         "2003-01-15 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosFilterMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosFilterMIBObjects = _WwpLeosFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1)
)
_WwpLeosFilter_ObjectIdentity = ObjectIdentity
wwpLeosFilter = _WwpLeosFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1)
)
_WwpLeosFilterResources_ObjectIdentity = ObjectIdentity
wwpLeosFilterResources = _WwpLeosFilterResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 1)
)
_WwpLeosFilterMaxHardwareResources_Type = Unsigned32
_WwpLeosFilterMaxHardwareResources_Object = MibScalar
wwpLeosFilterMaxHardwareResources = _WwpLeosFilterMaxHardwareResources_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 1, 1),
    _WwpLeosFilterMaxHardwareResources_Type()
)
wwpLeosFilterMaxHardwareResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterMaxHardwareResources.setStatus("current")
_WwpLeosFilterUsedHardwareResources_Type = Unsigned32
_WwpLeosFilterUsedHardwareResources_Object = MibScalar
wwpLeosFilterUsedHardwareResources = _WwpLeosFilterUsedHardwareResources_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 1, 2),
    _WwpLeosFilterUsedHardwareResources_Type()
)
wwpLeosFilterUsedHardwareResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterUsedHardwareResources.setStatus("current")
_WwpLeosFilterCreated_Type = Unsigned32
_WwpLeosFilterCreated_Object = MibScalar
wwpLeosFilterCreated = _WwpLeosFilterCreated_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 1, 3),
    _WwpLeosFilterCreated_Type()
)
wwpLeosFilterCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterCreated.setStatus("current")
_WwpLeosFilterCountersMax_Type = Unsigned32
_WwpLeosFilterCountersMax_Object = MibScalar
wwpLeosFilterCountersMax = _WwpLeosFilterCountersMax_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 1, 4),
    _WwpLeosFilterCountersMax_Type()
)
wwpLeosFilterCountersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterCountersMax.setStatus("current")
_WwpLeosFilterCountersUsed_Type = Unsigned32
_WwpLeosFilterCountersUsed_Object = MibScalar
wwpLeosFilterCountersUsed = _WwpLeosFilterCountersUsed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 1, 5),
    _WwpLeosFilterCountersUsed_Type()
)
wwpLeosFilterCountersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterCountersUsed.setStatus("current")
_WwpLeosFilterTable_Object = MibTable
wwpLeosFilterTable = _WwpLeosFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosFilterTable.setStatus("current")
_WwpLeosFilterEntry_Object = MibTableRow
wwpLeosFilterEntry = _WwpLeosFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 2, 1)
)
wwpLeosFilterEntry.setIndexNames(
    (0, "WWP-LEOS-FILTER-MIB", "wwpLeosFilterIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosFilterEntry.setStatus("current")


class _WwpLeosFilterIndex_Type(Integer32):
    """Custom type wwpLeosFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WwpLeosFilterIndex_Type.__name__ = "Integer32"
_WwpLeosFilterIndex_Object = MibTableColumn
wwpLeosFilterIndex = _WwpLeosFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 2, 1, 1),
    _WwpLeosFilterIndex_Type()
)
wwpLeosFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterIndex.setStatus("current")


class _WwpLeosFilterName_Type(OctetString):
    """Custom type wwpLeosFilterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_WwpLeosFilterName_Type.__name__ = "OctetString"
_WwpLeosFilterName_Object = MibTableColumn
wwpLeosFilterName = _WwpLeosFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 2, 1, 2),
    _WwpLeosFilterName_Type()
)
wwpLeosFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterName.setStatus("current")


class _WwpLeosFilterAdminState_Type(Integer32):
    """Custom type wwpLeosFilterAdminState based on Integer32"""
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


_WwpLeosFilterAdminState_Type.__name__ = "Integer32"
_WwpLeosFilterAdminState_Object = MibTableColumn
wwpLeosFilterAdminState = _WwpLeosFilterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 2, 1, 3),
    _WwpLeosFilterAdminState_Type()
)
wwpLeosFilterAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterAdminState.setStatus("current")


class _WwpLeosFilterOperState_Type(Integer32):
    """Custom type wwpLeosFilterOperState based on Integer32"""
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


_WwpLeosFilterOperState_Type.__name__ = "Integer32"
_WwpLeosFilterOperState_Object = MibTableColumn
wwpLeosFilterOperState = _WwpLeosFilterOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 2, 1, 4),
    _WwpLeosFilterOperState_Type()
)
wwpLeosFilterOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterOperState.setStatus("current")


class _WwpLeosFilterCounter_Type(Integer32):
    """Custom type wwpLeosFilterCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosFilterCounter_Type.__name__ = "Integer32"
_WwpLeosFilterCounter_Object = MibTableColumn
wwpLeosFilterCounter = _WwpLeosFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 2, 1, 5),
    _WwpLeosFilterCounter_Type()
)
wwpLeosFilterCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterCounter.setStatus("current")
_WwpLeosFilterStatus_Type = RowStatus
_WwpLeosFilterStatus_Object = MibTableColumn
wwpLeosFilterStatus = _WwpLeosFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 2, 1, 6),
    _WwpLeosFilterStatus_Type()
)
wwpLeosFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterStatus.setStatus("current")
_WwpLeosFilterProtocolTable_Object = MibTable
wwpLeosFilterProtocolTable = _WwpLeosFilterProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolTable.setStatus("current")
_WwpLeosFilterProtocolEntry_Object = MibTableRow
wwpLeosFilterProtocolEntry = _WwpLeosFilterProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 3, 1)
)
wwpLeosFilterProtocolEntry.setIndexNames(
    (0, "WWP-LEOS-FILTER-MIB", "wwpLeosFilterProtocolIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolEntry.setStatus("current")


class _WwpLeosFilterProtocolIndex_Type(Integer32):
    """Custom type wwpLeosFilterProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 41),
    )


_WwpLeosFilterProtocolIndex_Type.__name__ = "Integer32"
_WwpLeosFilterProtocolIndex_Object = MibTableColumn
wwpLeosFilterProtocolIndex = _WwpLeosFilterProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 3, 1, 1),
    _WwpLeosFilterProtocolIndex_Type()
)
wwpLeosFilterProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolIndex.setStatus("current")


class _WwpLeosFilterProtocolName_Type(OctetString):
    """Custom type wwpLeosFilterProtocolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_WwpLeosFilterProtocolName_Type.__name__ = "OctetString"
_WwpLeosFilterProtocolName_Object = MibTableColumn
wwpLeosFilterProtocolName = _WwpLeosFilterProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 3, 1, 2),
    _WwpLeosFilterProtocolName_Type()
)
wwpLeosFilterProtocolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolName.setStatus("current")


class _WwpLeosFilterProtocolType_Type(Integer32):
    """Custom type wwpLeosFilterProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WwpLeosFilterProtocolType_Type.__name__ = "Integer32"
_WwpLeosFilterProtocolType_Object = MibTableColumn
wwpLeosFilterProtocolType = _WwpLeosFilterProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 3, 1, 3),
    _WwpLeosFilterProtocolType_Type()
)
wwpLeosFilterProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolType.setStatus("current")


class _WwpLeosFilterProtocolSrcPort_Type(Integer32):
    """Custom type wwpLeosFilterProtocolSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFilterProtocolSrcPort_Type.__name__ = "Integer32"
_WwpLeosFilterProtocolSrcPort_Object = MibTableColumn
wwpLeosFilterProtocolSrcPort = _WwpLeosFilterProtocolSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 3, 1, 4),
    _WwpLeosFilterProtocolSrcPort_Type()
)
wwpLeosFilterProtocolSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolSrcPort.setStatus("current")


class _WwpLeosFilterProtocolDstPort_Type(Integer32):
    """Custom type wwpLeosFilterProtocolDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFilterProtocolDstPort_Type.__name__ = "Integer32"
_WwpLeosFilterProtocolDstPort_Object = MibTableColumn
wwpLeosFilterProtocolDstPort = _WwpLeosFilterProtocolDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 3, 1, 5),
    _WwpLeosFilterProtocolDstPort_Type()
)
wwpLeosFilterProtocolDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolDstPort.setStatus("current")
_WwpLeosFilterProtocolStatus_Type = RowStatus
_WwpLeosFilterProtocolStatus_Object = MibTableColumn
wwpLeosFilterProtocolStatus = _WwpLeosFilterProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 3, 1, 6),
    _WwpLeosFilterProtocolStatus_Type()
)
wwpLeosFilterProtocolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolStatus.setStatus("current")
_WwpLeosFilterMemTable_Object = MibTable
wwpLeosFilterMemTable = _WwpLeosFilterMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosFilterMemTable.setStatus("current")
_WwpLeosFilterMemEntry_Object = MibTableRow
wwpLeosFilterMemEntry = _WwpLeosFilterMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 4, 1)
)
wwpLeosFilterMemEntry.setIndexNames(
    (0, "WWP-LEOS-FILTER-MIB", "wwpLeosFilterIndex"),
    (0, "WWP-LEOS-FILTER-MIB", "wwpLeosFilterVlan"),
    (0, "WWP-LEOS-FILTER-MIB", "wwpLeosFilterPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosFilterMemEntry.setStatus("current")


class _WwpLeosFilterVlan_Type(Integer32):
    """Custom type wwpLeosFilterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_WwpLeosFilterVlan_Type.__name__ = "Integer32"
_WwpLeosFilterVlan_Object = MibTableColumn
wwpLeosFilterVlan = _WwpLeosFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 4, 1, 1),
    _WwpLeosFilterVlan_Type()
)
wwpLeosFilterVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterVlan.setStatus("current")


class _WwpLeosFilterPortId_Type(Integer32):
    """Custom type wwpLeosFilterPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFilterPortId_Type.__name__ = "Integer32"
_WwpLeosFilterPortId_Object = MibTableColumn
wwpLeosFilterPortId = _WwpLeosFilterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 4, 1, 2),
    _WwpLeosFilterPortId_Type()
)
wwpLeosFilterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterPortId.setStatus("current")
_WwpLeosFilterMemStatus_Type = RowStatus
_WwpLeosFilterMemStatus_Object = MibTableColumn
wwpLeosFilterMemStatus = _WwpLeosFilterMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 4, 1, 3),
    _WwpLeosFilterMemStatus_Type()
)
wwpLeosFilterMemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterMemStatus.setStatus("current")


class _WwpLeosFilterMemRule_Type(Integer32):
    """Custom type wwpLeosFilterMemRule based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("block", 1))
    )


_WwpLeosFilterMemRule_Type.__name__ = "Integer32"
_WwpLeosFilterMemRule_Object = MibTableColumn
wwpLeosFilterMemRule = _WwpLeosFilterMemRule_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 4, 1, 4),
    _WwpLeosFilterMemRule_Type()
)
wwpLeosFilterMemRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterMemRule.setStatus("current")
_WwpLeosFilterProtocolMemTable_Object = MibTable
wwpLeosFilterProtocolMemTable = _WwpLeosFilterProtocolMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolMemTable.setStatus("current")
_WwpLeosFilterProtocolMemEntry_Object = MibTableRow
wwpLeosFilterProtocolMemEntry = _WwpLeosFilterProtocolMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 5, 1)
)
wwpLeosFilterProtocolMemEntry.setIndexNames(
    (0, "WWP-LEOS-FILTER-MIB", "wwpLeosFilterIndex"),
    (0, "WWP-LEOS-FILTER-MIB", "wwpLeosFilterProtocolIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolMemEntry.setStatus("current")
_WwpLeosFilterProtocolMemStatus_Type = RowStatus
_WwpLeosFilterProtocolMemStatus_Object = MibTableColumn
wwpLeosFilterProtocolMemStatus = _WwpLeosFilterProtocolMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 5, 1, 1),
    _WwpLeosFilterProtocolMemStatus_Type()
)
wwpLeosFilterProtocolMemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFilterProtocolMemStatus.setStatus("current")
_WwpLeosFilterStatsTable_Object = MibTable
wwpLeosFilterStatsTable = _WwpLeosFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosFilterStatsTable.setStatus("current")
_WwpLeosFilterStatsEntry_Object = MibTableRow
wwpLeosFilterStatsEntry = _WwpLeosFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 6, 1)
)
wwpLeosFilterStatsEntry.setIndexNames(
    (0, "WWP-LEOS-FILTER-MIB", "wwpLeosFilterIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosFilterStatsEntry.setStatus("current")
_WwpLeosFilterDropBytes_Type = Counter32
_WwpLeosFilterDropBytes_Object = MibTableColumn
wwpLeosFilterDropBytes = _WwpLeosFilterDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 1, 1, 6, 1, 1),
    _WwpLeosFilterDropBytes_Type()
)
wwpLeosFilterDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFilterDropBytes.setStatus("current")
_WwpLeosFilterMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosFilterMIBNotificationPrefix = _WwpLeosFilterMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 2)
)
_WwpLeosFilterMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosFilterMIBNotifications = _WwpLeosFilterMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 2, 0)
)
_WwpLeosFilterMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosFilterMIBConformance = _WwpLeosFilterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 3)
)
_WwpLeosFilterMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosFilterMIBCompliances = _WwpLeosFilterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 3, 1)
)
_WwpLeosFilterMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosFilterMIBGroups = _WwpLeosFilterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 15, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-FILTER-MIB",
    **{"wwpLeosFilterMIB": wwpLeosFilterMIB,
       "wwpLeosFilterMIBObjects": wwpLeosFilterMIBObjects,
       "wwpLeosFilter": wwpLeosFilter,
       "wwpLeosFilterResources": wwpLeosFilterResources,
       "wwpLeosFilterMaxHardwareResources": wwpLeosFilterMaxHardwareResources,
       "wwpLeosFilterUsedHardwareResources": wwpLeosFilterUsedHardwareResources,
       "wwpLeosFilterCreated": wwpLeosFilterCreated,
       "wwpLeosFilterCountersMax": wwpLeosFilterCountersMax,
       "wwpLeosFilterCountersUsed": wwpLeosFilterCountersUsed,
       "wwpLeosFilterTable": wwpLeosFilterTable,
       "wwpLeosFilterEntry": wwpLeosFilterEntry,
       "wwpLeosFilterIndex": wwpLeosFilterIndex,
       "wwpLeosFilterName": wwpLeosFilterName,
       "wwpLeosFilterAdminState": wwpLeosFilterAdminState,
       "wwpLeosFilterOperState": wwpLeosFilterOperState,
       "wwpLeosFilterCounter": wwpLeosFilterCounter,
       "wwpLeosFilterStatus": wwpLeosFilterStatus,
       "wwpLeosFilterProtocolTable": wwpLeosFilterProtocolTable,
       "wwpLeosFilterProtocolEntry": wwpLeosFilterProtocolEntry,
       "wwpLeosFilterProtocolIndex": wwpLeosFilterProtocolIndex,
       "wwpLeosFilterProtocolName": wwpLeosFilterProtocolName,
       "wwpLeosFilterProtocolType": wwpLeosFilterProtocolType,
       "wwpLeosFilterProtocolSrcPort": wwpLeosFilterProtocolSrcPort,
       "wwpLeosFilterProtocolDstPort": wwpLeosFilterProtocolDstPort,
       "wwpLeosFilterProtocolStatus": wwpLeosFilterProtocolStatus,
       "wwpLeosFilterMemTable": wwpLeosFilterMemTable,
       "wwpLeosFilterMemEntry": wwpLeosFilterMemEntry,
       "wwpLeosFilterVlan": wwpLeosFilterVlan,
       "wwpLeosFilterPortId": wwpLeosFilterPortId,
       "wwpLeosFilterMemStatus": wwpLeosFilterMemStatus,
       "wwpLeosFilterMemRule": wwpLeosFilterMemRule,
       "wwpLeosFilterProtocolMemTable": wwpLeosFilterProtocolMemTable,
       "wwpLeosFilterProtocolMemEntry": wwpLeosFilterProtocolMemEntry,
       "wwpLeosFilterProtocolMemStatus": wwpLeosFilterProtocolMemStatus,
       "wwpLeosFilterStatsTable": wwpLeosFilterStatsTable,
       "wwpLeosFilterStatsEntry": wwpLeosFilterStatsEntry,
       "wwpLeosFilterDropBytes": wwpLeosFilterDropBytes,
       "wwpLeosFilterMIBNotificationPrefix": wwpLeosFilterMIBNotificationPrefix,
       "wwpLeosFilterMIBNotifications": wwpLeosFilterMIBNotifications,
       "wwpLeosFilterMIBConformance": wwpLeosFilterMIBConformance,
       "wwpLeosFilterMIBCompliances": wwpLeosFilterMIBCompliances,
       "wwpLeosFilterMIBGroups": wwpLeosFilterMIBGroups}
)
