# SNMP MIB module (PMCAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PMCAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:04 2024
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

(rmon,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "rmon")

(protocolDirLocalIndex,
 protocolDirectoryGroup) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "protocolDirLocalIndex",
    "protocolDirectoryGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pmCapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25)
)
pmCapsMIB.setRevisions(
        ("2000-07-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PmCapsMIBObjects_ObjectIdentity = ObjectIdentity
pmCapsMIBObjects = _PmCapsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 1)
)
_PmCaps_ObjectIdentity = ObjectIdentity
pmCaps = _PmCaps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1)
)
_PmMetricTable_Object = MibTable
pmMetricTable = _PmMetricTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pmMetricTable.setStatus("current")
_PmMetricEntry_Object = MibTableRow
pmMetricEntry = _PmMetricEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1)
)
pmMetricEntry.setIndexNames(
    (0, "PMCAPS-MIB", "pmMetricID"),
)
if mibBuilder.loadTexts:
    pmMetricEntry.setStatus("current")
_PmMetricID_Type = ObjectIdentifier
_PmMetricID_Object = MibTableColumn
pmMetricID = _PmMetricID_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 1),
    _PmMetricID_Type()
)
pmMetricID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmMetricID.setStatus("current")


class _PmMetricType_Type(Integer32):
    """Custom type pmMetricType based on Integer32"""
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
        *(("connectMetric", 2),
          ("delayMetric", 3),
          ("lossMetric", 4),
          ("other", 1))
    )


_PmMetricType_Type.__name__ = "Integer32"
_PmMetricType_Object = MibTableColumn
pmMetricType = _PmMetricType_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 2),
    _PmMetricType_Type()
)
pmMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMetricType.setStatus("current")


class _PmMetricDirType_Type(Integer32):
    """Custom type pmMetricDirType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiWay", 3),
          ("oneWay", 1),
          ("twoWay", 2))
    )


_PmMetricDirType_Type.__name__ = "Integer32"
_PmMetricDirType_Object = MibTableColumn
pmMetricDirType = _PmMetricDirType_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 3),
    _PmMetricDirType_Type()
)
pmMetricDirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMetricDirType.setStatus("current")
_PmMetricName_Type = SnmpAdminString
_PmMetricName_Object = MibTableColumn
pmMetricName = _PmMetricName_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 4),
    _PmMetricName_Type()
)
pmMetricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMetricName.setStatus("current")
_PmMetricReference_Type = SnmpAdminString
_PmMetricReference_Object = MibTableColumn
pmMetricReference = _PmMetricReference_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 5),
    _PmMetricReference_Type()
)
pmMetricReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMetricReference.setStatus("current")
_PmStudyClassTable_Object = MibTable
pmStudyClassTable = _PmStudyClassTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pmStudyClassTable.setStatus("current")
_PmStudyClassEntry_Object = MibTableRow
pmStudyClassEntry = _PmStudyClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1)
)
pmStudyClassEntry.setIndexNames(
    (0, "PMCAPS-MIB", "pmStudyClassID"),
)
if mibBuilder.loadTexts:
    pmStudyClassEntry.setStatus("current")
_PmStudyClassID_Type = ObjectIdentifier
_PmStudyClassID_Object = MibTableColumn
pmStudyClassID = _PmStudyClassID_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 1),
    _PmStudyClassID_Type()
)
pmStudyClassID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmStudyClassID.setStatus("current")


class _PmStudyClassMeasLoc_Type(Bits):
    """Custom type pmStudyClassMeasLoc based on Bits"""
    namedValues = NamedValues(
        *(("pmClient", 0),
          ("pmNetwork", 1),
          ("pmServer", 2))
    )

_PmStudyClassMeasLoc_Type.__name__ = "Bits"
_PmStudyClassMeasLoc_Object = MibTableColumn
pmStudyClassMeasLoc = _PmStudyClassMeasLoc_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 2),
    _PmStudyClassMeasLoc_Type()
)
pmStudyClassMeasLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmStudyClassMeasLoc.setStatus("current")


class _PmStudyClassMeasType_Type(Bits):
    """Custom type pmStudyClassMeasType based on Bits"""
    namedValues = NamedValues(
        *(("pmActive", 1),
          ("pmBuiltin", 2),
          ("pmPassive", 0))
    )

_PmStudyClassMeasType_Type.__name__ = "Bits"
_PmStudyClassMeasType_Object = MibTableColumn
pmStudyClassMeasType = _PmStudyClassMeasType_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 3),
    _PmStudyClassMeasType_Type()
)
pmStudyClassMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmStudyClassMeasType.setStatus("current")


class _PmStudyClassCollectPts_Type(Integer32):
    """Custom type pmStudyClassCollectPts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmStudyClassCollectPts_Type.__name__ = "Integer32"
_PmStudyClassCollectPts_Object = MibTableColumn
pmStudyClassCollectPts = _PmStudyClassCollectPts_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 4),
    _PmStudyClassCollectPts_Type()
)
pmStudyClassCollectPts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmStudyClassCollectPts.setStatus("current")


class _PmStudyClassCollectCaps_Type(Bits):
    """Custom type pmStudyClassCollectCaps based on Bits"""
    namedValues = NamedValues(
        *(("pmCollectApp", 1),
          ("pmCollectFlow", 2),
          ("pmCollectNonNet", 3),
          ("pmCollectTrans", 0))
    )

_PmStudyClassCollectCaps_Type.__name__ = "Bits"
_PmStudyClassCollectCaps_Object = MibTableColumn
pmStudyClassCollectCaps = _PmStudyClassCollectCaps_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 5),
    _PmStudyClassCollectCaps_Type()
)
pmStudyClassCollectCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmStudyClassCollectCaps.setStatus("current")


class _PmStudyClassOutputCaps_Type(Bits):
    """Custom type pmStudyClassOutputCaps based on Bits"""
    namedValues = NamedValues(
        *(("pmOutputApmDist", 1),
          ("pmOutputApmExcept", 5),
          ("pmOutputApmFlow", 4),
          ("pmOutputApmHist", 3),
          ("pmOutputApmProp", 6),
          ("pmOutputApmStat", 2),
          ("pmOutputOther", 0),
          ("pmOutputTpmDist", 7),
          ("pmOutputTpmExcept", 10),
          ("pmOutputTpmHist", 9),
          ("pmOutputTpmProp", 11),
          ("pmOutputTpmStat", 8))
    )

_PmStudyClassOutputCaps_Type.__name__ = "Bits"
_PmStudyClassOutputCaps_Object = MibTableColumn
pmStudyClassOutputCaps = _PmStudyClassOutputCaps_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 6),
    _PmStudyClassOutputCaps_Type()
)
pmStudyClassOutputCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmStudyClassOutputCaps.setStatus("current")
_PmStudyClassCtlTablePtr_Type = RowPointer
_PmStudyClassCtlTablePtr_Object = MibTableColumn
pmStudyClassCtlTablePtr = _PmStudyClassCtlTablePtr_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 7),
    _PmStudyClassCtlTablePtr_Type()
)
pmStudyClassCtlTablePtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmStudyClassCtlTablePtr.setStatus("current")
_PmStudyMetricTable_Object = MibTable
pmStudyMetricTable = _PmStudyMetricTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pmStudyMetricTable.setStatus("current")
_PmStudyMetricEntry_Object = MibTableRow
pmStudyMetricEntry = _PmStudyMetricEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 3, 1)
)
pmStudyMetricEntry.setIndexNames(
    (0, "PMCAPS-MIB", "pmStudyClassID"),
)
if mibBuilder.loadTexts:
    pmStudyMetricEntry.setStatus("current")
_PmStudyMetricID_Type = ObjectIdentifier
_PmStudyMetricID_Object = MibTableColumn
pmStudyMetricID = _PmStudyMetricID_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 3, 1, 1),
    _PmStudyMetricID_Type()
)
pmStudyMetricID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmStudyMetricID.setStatus("current")
_PmStudyProtocolTable_Object = MibTable
pmStudyProtocolTable = _PmStudyProtocolTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pmStudyProtocolTable.setStatus("current")
_PmStudyProtocolEntry_Object = MibTableRow
pmStudyProtocolEntry = _PmStudyProtocolEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 4, 1)
)
pmStudyProtocolEntry.setIndexNames(
    (0, "PMCAPS-MIB", "pmStudyClassID"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
)
if mibBuilder.loadTexts:
    pmStudyProtocolEntry.setStatus("current")
_PmStudyProtocolIsSubtree_Type = TruthValue
_PmStudyProtocolIsSubtree_Object = MibTableColumn
pmStudyProtocolIsSubtree = _PmStudyProtocolIsSubtree_Object(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 4, 1, 1),
    _PmStudyProtocolIsSubtree_Type()
)
pmStudyProtocolIsSubtree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmStudyProtocolIsSubtree.setStatus("current")
_PmMetrics_ObjectIdentity = ObjectIdentity
pmMetrics = _PmMetrics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 2)
)
_PmAppAvailMetric_ObjectIdentity = ObjectIdentity
pmAppAvailMetric = _PmAppAvailMetric_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pmAppAvailMetric.setStatus("current")
_PmAppTransRespMetric_ObjectIdentity = ObjectIdentity
pmAppTransRespMetric = _PmAppTransRespMetric_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pmAppTransRespMetric.setStatus("current")
_PmAppTputRespMetric_ObjectIdentity = ObjectIdentity
pmAppTputRespMetric = _PmAppTputRespMetric_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pmAppTputRespMetric.setStatus("current")
_PmAppStreamRespMetric_ObjectIdentity = ObjectIdentity
pmAppStreamRespMetric = _PmAppStreamRespMetric_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 4)
)
if mibBuilder.loadTexts:
    pmAppStreamRespMetric.setStatus("current")
_PmCapsNotifications_ObjectIdentity = ObjectIdentity
pmCapsNotifications = _PmCapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 2)
)
_PmCapsConformance_ObjectIdentity = ObjectIdentity
pmCapsConformance = _PmCapsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 3)
)
_PmCapsCompliances_ObjectIdentity = ObjectIdentity
pmCapsCompliances = _PmCapsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 3, 1)
)
_PmCapsGroups_ObjectIdentity = ObjectIdentity
pmCapsGroups = _PmCapsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 25, 3, 2)
)

# Managed Objects groups

pmCapsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 25, 3, 2, 1)
)
pmCapsGroup.setObjects(
      *(("PMCAPS-MIB", "pmMetricType"),
        ("PMCAPS-MIB", "pmMetricDirType"),
        ("PMCAPS-MIB", "pmMetricName"),
        ("PMCAPS-MIB", "pmMetricReference"),
        ("PMCAPS-MIB", "pmStudyClassMeasLoc"),
        ("PMCAPS-MIB", "pmStudyClassMeasType"),
        ("PMCAPS-MIB", "pmStudyClassCollectPts"),
        ("PMCAPS-MIB", "pmStudyClassCollectCaps"),
        ("PMCAPS-MIB", "pmStudyClassOutputCaps"),
        ("PMCAPS-MIB", "pmStudyClassCtlTablePtr"),
        ("PMCAPS-MIB", "pmStudyMetricID"),
        ("PMCAPS-MIB", "pmStudyProtocolIsSubtree"))
)
if mibBuilder.loadTexts:
    pmCapsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pmCapsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 25, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pmCapsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PMCAPS-MIB",
    **{"pmCapsMIB": pmCapsMIB,
       "pmCapsMIBObjects": pmCapsMIBObjects,
       "pmCaps": pmCaps,
       "pmMetricTable": pmMetricTable,
       "pmMetricEntry": pmMetricEntry,
       "pmMetricID": pmMetricID,
       "pmMetricType": pmMetricType,
       "pmMetricDirType": pmMetricDirType,
       "pmMetricName": pmMetricName,
       "pmMetricReference": pmMetricReference,
       "pmStudyClassTable": pmStudyClassTable,
       "pmStudyClassEntry": pmStudyClassEntry,
       "pmStudyClassID": pmStudyClassID,
       "pmStudyClassMeasLoc": pmStudyClassMeasLoc,
       "pmStudyClassMeasType": pmStudyClassMeasType,
       "pmStudyClassCollectPts": pmStudyClassCollectPts,
       "pmStudyClassCollectCaps": pmStudyClassCollectCaps,
       "pmStudyClassOutputCaps": pmStudyClassOutputCaps,
       "pmStudyClassCtlTablePtr": pmStudyClassCtlTablePtr,
       "pmStudyMetricTable": pmStudyMetricTable,
       "pmStudyMetricEntry": pmStudyMetricEntry,
       "pmStudyMetricID": pmStudyMetricID,
       "pmStudyProtocolTable": pmStudyProtocolTable,
       "pmStudyProtocolEntry": pmStudyProtocolEntry,
       "pmStudyProtocolIsSubtree": pmStudyProtocolIsSubtree,
       "pmMetrics": pmMetrics,
       "pmAppAvailMetric": pmAppAvailMetric,
       "pmAppTransRespMetric": pmAppTransRespMetric,
       "pmAppTputRespMetric": pmAppTputRespMetric,
       "pmAppStreamRespMetric": pmAppStreamRespMetric,
       "pmCapsNotifications": pmCapsNotifications,
       "pmCapsConformance": pmCapsConformance,
       "pmCapsCompliances": pmCapsCompliances,
       "pmCapsCompliance": pmCapsCompliance,
       "pmCapsGroups": pmCapsGroups,
       "pmCapsGroup": pmCapsGroup}
)
