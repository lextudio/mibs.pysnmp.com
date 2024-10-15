# SNMP MIB module (CISCO-FASTHUB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FASTHUB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:11 2024
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class VisualLEDMap(OctetString):
    """Custom type VisualLEDMap based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFastHubMIB_ObjectIdentity = ObjectIdentity
ciscoFastHubMIB = _CiscoFastHubMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 11)
)
_CiscoFastHubMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFastHubMIBObjects = _CiscoFastHubMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1)
)
_MrStack_ObjectIdentity = ObjectIdentity
mrStack = _MrStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1)
)
_MrStackUnitCapacity_Type = Integer32
_MrStackUnitCapacity_Object = MibScalar
mrStackUnitCapacity = _MrStackUnitCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 1),
    _MrStackUnitCapacity_Type()
)
mrStackUnitCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitCapacity.setStatus("mandatory")
_MrStackNumberOfUnitsPresent_Type = Integer32
_MrStackNumberOfUnitsPresent_Object = MibScalar
mrStackNumberOfUnitsPresent = _MrStackNumberOfUnitsPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 2),
    _MrStackNumberOfUnitsPresent_Type()
)
mrStackNumberOfUnitsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackNumberOfUnitsPresent.setStatus("mandatory")
_MrStackSelectPrimarySupervisorUnit_Type = Integer32
_MrStackSelectPrimarySupervisorUnit_Object = MibScalar
mrStackSelectPrimarySupervisorUnit = _MrStackSelectPrimarySupervisorUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 3),
    _MrStackSelectPrimarySupervisorUnit_Type()
)
mrStackSelectPrimarySupervisorUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrStackSelectPrimarySupervisorUnit.setStatus("mandatory")


class _MrStackPOSTSelect_Type(Integer32):
    """Custom type mrStackPOSTSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 2),
          ("normal", 1))
    )


_MrStackPOSTSelect_Type.__name__ = "Integer32"
_MrStackPOSTSelect_Object = MibScalar
mrStackPOSTSelect = _MrStackPOSTSelect_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 4),
    _MrStackPOSTSelect_Type()
)
mrStackPOSTSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrStackPOSTSelect.setStatus("mandatory")


class _MrStackReset_Type(Integer32):
    """Custom type mrStackReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_MrStackReset_Type.__name__ = "Integer32"
_MrStackReset_Object = MibScalar
mrStackReset = _MrStackReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 5),
    _MrStackReset_Type()
)
mrStackReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrStackReset.setStatus("mandatory")


class _MrStackDefaultReset_Type(Integer32):
    """Custom type mrStackDefaultReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_MrStackDefaultReset_Type.__name__ = "Integer32"
_MrStackDefaultReset_Object = MibScalar
mrStackDefaultReset = _MrStackDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 6),
    _MrStackDefaultReset_Type()
)
mrStackDefaultReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrStackDefaultReset.setStatus("mandatory")


class _MrStackClearStatistics_Type(Integer32):
    """Custom type mrStackClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noClear", 2))
    )


_MrStackClearStatistics_Type.__name__ = "Integer32"
_MrStackClearStatistics_Object = MibScalar
mrStackClearStatistics = _MrStackClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 7),
    _MrStackClearStatistics_Type()
)
mrStackClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrStackClearStatistics.setStatus("obsolete")
_MrStackShortJabberLoopCorrections_Type = Counter32
_MrStackShortJabberLoopCorrections_Object = MibScalar
mrStackShortJabberLoopCorrections = _MrStackShortJabberLoopCorrections_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 1, 8),
    _MrStackShortJabberLoopCorrections_Type()
)
mrStackShortJabberLoopCorrections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackShortJabberLoopCorrections.setStatus("mandatory")
_MrSupervisorLog_ObjectIdentity = ObjectIdentity
mrSupervisorLog = _MrSupervisorLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2)
)


class _MrSupervisorLogTableClear_Type(Integer32):
    """Custom type mrSupervisorLogTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noClear", 2))
    )


_MrSupervisorLogTableClear_Type.__name__ = "Integer32"
_MrSupervisorLogTableClear_Object = MibScalar
mrSupervisorLogTableClear = _MrSupervisorLogTableClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 1),
    _MrSupervisorLogTableClear_Type()
)
mrSupervisorLogTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrSupervisorLogTableClear.setStatus("mandatory")
_MrSupervisorLogTable_Object = MibTable
mrSupervisorLogTable = _MrSupervisorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mrSupervisorLogTable.setStatus("mandatory")
_MrSupervisorLogEntry_Object = MibTableRow
mrSupervisorLogEntry = _MrSupervisorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2, 1)
)
mrSupervisorLogEntry.setIndexNames(
    (0, "CISCO-FASTHUB-MIB", "mrSupervisorLogIndex"),
)
if mibBuilder.loadTexts:
    mrSupervisorLogEntry.setStatus("mandatory")
_MrSupervisorLogIndex_Type = Integer32
_MrSupervisorLogIndex_Object = MibTableColumn
mrSupervisorLogIndex = _MrSupervisorLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2, 1, 1),
    _MrSupervisorLogIndex_Type()
)
mrSupervisorLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrSupervisorLogIndex.setStatus("mandatory")
_MrSupervisorLogTime_Type = DisplayString
_MrSupervisorLogTime_Object = MibTableColumn
mrSupervisorLogTime = _MrSupervisorLogTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2, 1, 2),
    _MrSupervisorLogTime_Type()
)
mrSupervisorLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrSupervisorLogTime.setStatus("obsolete")
_MrSupervisorLogInfo_Type = DisplayString
_MrSupervisorLogInfo_Object = MibTableColumn
mrSupervisorLogInfo = _MrSupervisorLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2, 1, 3),
    _MrSupervisorLogInfo_Type()
)
mrSupervisorLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrSupervisorLogInfo.setStatus("mandatory")
_MrSupervisorLogRelativeTime_Type = TimeTicks
_MrSupervisorLogRelativeTime_Object = MibTableColumn
mrSupervisorLogRelativeTime = _MrSupervisorLogRelativeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 2, 2, 1, 4),
    _MrSupervisorLogRelativeTime_Type()
)
mrSupervisorLogRelativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrSupervisorLogRelativeTime.setStatus("mandatory")
_MrStackUnit_ObjectIdentity = ObjectIdentity
mrStackUnit = _MrStackUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3)
)
_MrStackUnitTable_Object = MibTable
mrStackUnitTable = _MrStackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mrStackUnitTable.setStatus("mandatory")
_MrStackUnitEntry_Object = MibTableRow
mrStackUnitEntry = _MrStackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1)
)
mrStackUnitEntry.setIndexNames(
    (0, "CISCO-FASTHUB-MIB", "mrStackUnitIndex"),
)
if mibBuilder.loadTexts:
    mrStackUnitEntry.setStatus("mandatory")
_MrStackUnitIndex_Type = Integer32
_MrStackUnitIndex_Object = MibTableColumn
mrStackUnitIndex = _MrStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 1),
    _MrStackUnitIndex_Type()
)
mrStackUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitIndex.setStatus("mandatory")


class _MrStackUnitPresent_Type(Integer32):
    """Custom type mrStackUnitPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MrStackUnitPresent_Type.__name__ = "Integer32"
_MrStackUnitPresent_Object = MibTableColumn
mrStackUnitPresent = _MrStackUnitPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 2),
    _MrStackUnitPresent_Type()
)
mrStackUnitPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitPresent.setStatus("mandatory")
_MrStackUnitFirstGroupIndex_Type = Integer32
_MrStackUnitFirstGroupIndex_Object = MibTableColumn
mrStackUnitFirstGroupIndex = _MrStackUnitFirstGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 3),
    _MrStackUnitFirstGroupIndex_Type()
)
mrStackUnitFirstGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitFirstGroupIndex.setStatus("mandatory")
_MrStackUnitLastGroupIndex_Type = Integer32
_MrStackUnitLastGroupIndex_Object = MibTableColumn
mrStackUnitLastGroupIndex = _MrStackUnitLastGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 4),
    _MrStackUnitLastGroupIndex_Type()
)
mrStackUnitLastGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitLastGroupIndex.setStatus("mandatory")


class _MrStackUnitSupervisorPresent_Type(Integer32):
    """Custom type mrStackUnitSupervisorPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MrStackUnitSupervisorPresent_Type.__name__ = "Integer32"
_MrStackUnitSupervisorPresent_Object = MibTableColumn
mrStackUnitSupervisorPresent = _MrStackUnitSupervisorPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 5),
    _MrStackUnitSupervisorPresent_Type()
)
mrStackUnitSupervisorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitSupervisorPresent.setStatus("mandatory")
_MrStackUnitSupervisorMajorVersion_Type = Integer32
_MrStackUnitSupervisorMajorVersion_Object = MibTableColumn
mrStackUnitSupervisorMajorVersion = _MrStackUnitSupervisorMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 6),
    _MrStackUnitSupervisorMajorVersion_Type()
)
mrStackUnitSupervisorMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitSupervisorMajorVersion.setStatus("mandatory")
_MrStackUnitSupervisorMinorVersion_Type = Integer32
_MrStackUnitSupervisorMinorVersion_Object = MibTableColumn
mrStackUnitSupervisorMinorVersion = _MrStackUnitSupervisorMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 7),
    _MrStackUnitSupervisorMinorVersion_Type()
)
mrStackUnitSupervisorMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitSupervisorMinorVersion.setStatus("mandatory")
_MrStackUnitSupervisorBootstrapMajorVersion_Type = Integer32
_MrStackUnitSupervisorBootstrapMajorVersion_Object = MibTableColumn
mrStackUnitSupervisorBootstrapMajorVersion = _MrStackUnitSupervisorBootstrapMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 8),
    _MrStackUnitSupervisorBootstrapMajorVersion_Type()
)
mrStackUnitSupervisorBootstrapMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitSupervisorBootstrapMajorVersion.setStatus("mandatory")
_MrStackUnitSupervisorBootstrapMinorVersion_Type = Integer32
_MrStackUnitSupervisorBootstrapMinorVersion_Object = MibTableColumn
mrStackUnitSupervisorBootstrapMinorVersion = _MrStackUnitSupervisorBootstrapMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 9),
    _MrStackUnitSupervisorBootstrapMinorVersion_Type()
)
mrStackUnitSupervisorBootstrapMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitSupervisorBootstrapMinorVersion.setStatus("mandatory")
_MrStackUnitPOSTResult_Type = OctetString
_MrStackUnitPOSTResult_Object = MibTableColumn
mrStackUnitPOSTResult = _MrStackUnitPOSTResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 10),
    _MrStackUnitPOSTResult_Type()
)
mrStackUnitPOSTResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitPOSTResult.setStatus("mandatory")


class _MrStackUnitSupervisorIsPrimary_Type(Integer32):
    """Custom type mrStackUnitSupervisorIsPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MrStackUnitSupervisorIsPrimary_Type.__name__ = "Integer32"
_MrStackUnitSupervisorIsPrimary_Object = MibTableColumn
mrStackUnitSupervisorIsPrimary = _MrStackUnitSupervisorIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 11),
    _MrStackUnitSupervisorIsPrimary_Type()
)
mrStackUnitSupervisorIsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitSupervisorIsPrimary.setStatus("mandatory")


class _MrStackUnitExpansionModulePresent_Type(Integer32):
    """Custom type mrStackUnitExpansionModulePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MrStackUnitExpansionModulePresent_Type.__name__ = "Integer32"
_MrStackUnitExpansionModulePresent_Object = MibTableColumn
mrStackUnitExpansionModulePresent = _MrStackUnitExpansionModulePresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 12),
    _MrStackUnitExpansionModulePresent_Type()
)
mrStackUnitExpansionModulePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitExpansionModulePresent.setStatus("mandatory")


class _MrStackUnitPortVisualIndicatorSelect_Type(Integer32):
    """Custom type mrStackUnitPortVisualIndicatorSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portStatus", 1),
          ("unitNumber", 2),
          ("utilization", 3))
    )


_MrStackUnitPortVisualIndicatorSelect_Type.__name__ = "Integer32"
_MrStackUnitPortVisualIndicatorSelect_Object = MibTableColumn
mrStackUnitPortVisualIndicatorSelect = _MrStackUnitPortVisualIndicatorSelect_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 13),
    _MrStackUnitPortVisualIndicatorSelect_Type()
)
mrStackUnitPortVisualIndicatorSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitPortVisualIndicatorSelect.setStatus("mandatory")
_MrStackUnitBasePortVisualIndicatorGreenMap_Type = VisualLEDMap
_MrStackUnitBasePortVisualIndicatorGreenMap_Object = MibTableColumn
mrStackUnitBasePortVisualIndicatorGreenMap = _MrStackUnitBasePortVisualIndicatorGreenMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 14),
    _MrStackUnitBasePortVisualIndicatorGreenMap_Type()
)
mrStackUnitBasePortVisualIndicatorGreenMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitBasePortVisualIndicatorGreenMap.setStatus("mandatory")
_MrStackUnitBasePortVisualIndicatorAmberMap_Type = VisualLEDMap
_MrStackUnitBasePortVisualIndicatorAmberMap_Object = MibTableColumn
mrStackUnitBasePortVisualIndicatorAmberMap = _MrStackUnitBasePortVisualIndicatorAmberMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 15),
    _MrStackUnitBasePortVisualIndicatorAmberMap_Type()
)
mrStackUnitBasePortVisualIndicatorAmberMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitBasePortVisualIndicatorAmberMap.setStatus("mandatory")
_MrStackUnitExpansionPortVisualIndicatorGreenMap_Type = VisualLEDMap
_MrStackUnitExpansionPortVisualIndicatorGreenMap_Object = MibTableColumn
mrStackUnitExpansionPortVisualIndicatorGreenMap = _MrStackUnitExpansionPortVisualIndicatorGreenMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 16),
    _MrStackUnitExpansionPortVisualIndicatorGreenMap_Type()
)
mrStackUnitExpansionPortVisualIndicatorGreenMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitExpansionPortVisualIndicatorGreenMap.setStatus("mandatory")
_MrStackUnitExpansionPortVisualIndicatorAmberMap_Type = VisualLEDMap
_MrStackUnitExpansionPortVisualIndicatorAmberMap_Object = MibTableColumn
mrStackUnitExpansionPortVisualIndicatorAmberMap = _MrStackUnitExpansionPortVisualIndicatorAmberMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 17),
    _MrStackUnitExpansionPortVisualIndicatorAmberMap_Type()
)
mrStackUnitExpansionPortVisualIndicatorAmberMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitExpansionPortVisualIndicatorAmberMap.setStatus("mandatory")


class _MrStackUnitActivityVisualIndicator_Type(Integer32):
    """Custom type mrStackUnitActivityVisualIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MrStackUnitActivityVisualIndicator_Type.__name__ = "Integer32"
_MrStackUnitActivityVisualIndicator_Object = MibTableColumn
mrStackUnitActivityVisualIndicator = _MrStackUnitActivityVisualIndicator_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 18),
    _MrStackUnitActivityVisualIndicator_Type()
)
mrStackUnitActivityVisualIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitActivityVisualIndicator.setStatus("mandatory")


class _MrStackUnitCollisionVisualIndicator_Type(Integer32):
    """Custom type mrStackUnitCollisionVisualIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MrStackUnitCollisionVisualIndicator_Type.__name__ = "Integer32"
_MrStackUnitCollisionVisualIndicator_Object = MibTableColumn
mrStackUnitCollisionVisualIndicator = _MrStackUnitCollisionVisualIndicator_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 19),
    _MrStackUnitCollisionVisualIndicator_Type()
)
mrStackUnitCollisionVisualIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitCollisionVisualIndicator.setStatus("mandatory")


class _MrStackUnitRPSStatus_Type(Integer32):
    """Custom type mrStackUnitRPSStatus based on Integer32"""
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
        *(("connectedFunctional", 2),
          ("connectedNotFunctional", 3),
          ("functionalPrimaryFailed", 4),
          ("notPresent", 1))
    )


_MrStackUnitRPSStatus_Type.__name__ = "Integer32"
_MrStackUnitRPSStatus_Object = MibTableColumn
mrStackUnitRPSStatus = _MrStackUnitRPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 20),
    _MrStackUnitRPSStatus_Type()
)
mrStackUnitRPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitRPSStatus.setStatus("mandatory")


class _MrStackUnitRPSVisualIndicator_Type(Integer32):
    """Custom type mrStackUnitRPSVisualIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("amber", 3),
          ("green", 2),
          ("off", 1))
    )


_MrStackUnitRPSVisualIndicator_Type.__name__ = "Integer32"
_MrStackUnitRPSVisualIndicator_Object = MibTableColumn
mrStackUnitRPSVisualIndicator = _MrStackUnitRPSVisualIndicator_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 21),
    _MrStackUnitRPSVisualIndicator_Type()
)
mrStackUnitRPSVisualIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitRPSVisualIndicator.setStatus("mandatory")
_MrStackUnitSerialNumber_Type = DisplayString
_MrStackUnitSerialNumber_Object = MibTableColumn
mrStackUnitSerialNumber = _MrStackUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 3, 1, 1, 22),
    _MrStackUnitSerialNumber_Type()
)
mrStackUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrStackUnitSerialNumber.setStatus("mandatory")
_MrNetMgmt_ObjectIdentity = ObjectIdentity
mrNetMgmt = _MrNetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4)
)
_MrNetMgmtIpAddress_Type = IpAddress
_MrNetMgmtIpAddress_Object = MibScalar
mrNetMgmtIpAddress = _MrNetMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 1),
    _MrNetMgmtIpAddress_Type()
)
mrNetMgmtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtIpAddress.setStatus("mandatory")
_MrNetMgmtIpSubnetMask_Type = IpAddress
_MrNetMgmtIpSubnetMask_Object = MibScalar
mrNetMgmtIpSubnetMask = _MrNetMgmtIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 2),
    _MrNetMgmtIpSubnetMask_Type()
)
mrNetMgmtIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtIpSubnetMask.setStatus("mandatory")
_MrNetMgmtDefaultGateway_Type = IpAddress
_MrNetMgmtDefaultGateway_Object = MibScalar
mrNetMgmtDefaultGateway = _MrNetMgmtDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 3),
    _MrNetMgmtDefaultGateway_Type()
)
mrNetMgmtDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtDefaultGateway.setStatus("mandatory")


class _MrNetMgmtEnableAuthenTraps_Type(Integer32):
    """Custom type mrNetMgmtEnableAuthenTraps based on Integer32"""
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


_MrNetMgmtEnableAuthenTraps_Type.__name__ = "Integer32"
_MrNetMgmtEnableAuthenTraps_Object = MibScalar
mrNetMgmtEnableAuthenTraps = _MrNetMgmtEnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 4),
    _MrNetMgmtEnableAuthenTraps_Type()
)
mrNetMgmtEnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtEnableAuthenTraps.setStatus("mandatory")


class _MrNetMgmtEnableRIP_Type(Integer32):
    """Custom type mrNetMgmtEnableRIP based on Integer32"""
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


_MrNetMgmtEnableRIP_Type.__name__ = "Integer32"
_MrNetMgmtEnableRIP_Object = MibScalar
mrNetMgmtEnableRIP = _MrNetMgmtEnableRIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 6),
    _MrNetMgmtEnableRIP_Type()
)
mrNetMgmtEnableRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtEnableRIP.setStatus("mandatory")


class _MrNetMgmtConsoleInactTime_Type(Integer32):
    """Custom type mrNetMgmtConsoleInactTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_MrNetMgmtConsoleInactTime_Type.__name__ = "Integer32"
_MrNetMgmtConsoleInactTime_Object = MibScalar
mrNetMgmtConsoleInactTime = _MrNetMgmtConsoleInactTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 7),
    _MrNetMgmtConsoleInactTime_Type()
)
mrNetMgmtConsoleInactTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtConsoleInactTime.setStatus("mandatory")


class _MrNetMgmtConsolePasswordThreshold_Type(Integer32):
    """Custom type mrNetMgmtConsolePasswordThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_MrNetMgmtConsolePasswordThreshold_Type.__name__ = "Integer32"
_MrNetMgmtConsolePasswordThreshold_Object = MibScalar
mrNetMgmtConsolePasswordThreshold = _MrNetMgmtConsolePasswordThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 8),
    _MrNetMgmtConsolePasswordThreshold_Type()
)
mrNetMgmtConsolePasswordThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtConsolePasswordThreshold.setStatus("mandatory")


class _MrNetMgmtConsoleSilentTime_Type(Integer32):
    """Custom type mrNetMgmtConsoleSilentTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_MrNetMgmtConsoleSilentTime_Type.__name__ = "Integer32"
_MrNetMgmtConsoleSilentTime_Object = MibScalar
mrNetMgmtConsoleSilentTime = _MrNetMgmtConsoleSilentTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 9),
    _MrNetMgmtConsoleSilentTime_Type()
)
mrNetMgmtConsoleSilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtConsoleSilentTime.setStatus("mandatory")


class _MrNetMgmtModemInitString_Type(DisplayString):
    """Custom type mrNetMgmtModemInitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_MrNetMgmtModemInitString_Type.__name__ = "DisplayString"
_MrNetMgmtModemInitString_Object = MibScalar
mrNetMgmtModemInitString = _MrNetMgmtModemInitString_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 10),
    _MrNetMgmtModemInitString_Type()
)
mrNetMgmtModemInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtModemInitString.setStatus("mandatory")


class _MrNetMgmtModemDialString_Type(DisplayString):
    """Custom type mrNetMgmtModemDialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_MrNetMgmtModemDialString_Type.__name__ = "DisplayString"
_MrNetMgmtModemDialString_Object = MibScalar
mrNetMgmtModemDialString = _MrNetMgmtModemDialString_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 11),
    _MrNetMgmtModemDialString_Type()
)
mrNetMgmtModemDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtModemDialString.setStatus("mandatory")


class _MrNetMgmtModemDialDelay_Type(Integer32):
    """Custom type mrNetMgmtModemDialDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_MrNetMgmtModemDialDelay_Type.__name__ = "Integer32"
_MrNetMgmtModemDialDelay_Object = MibScalar
mrNetMgmtModemDialDelay = _MrNetMgmtModemDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 12),
    _MrNetMgmtModemDialDelay_Type()
)
mrNetMgmtModemDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtModemDialDelay.setStatus("mandatory")


class _MrNetMgmtModemAutoAnswer_Type(Integer32):
    """Custom type mrNetMgmtModemAutoAnswer based on Integer32"""
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


_MrNetMgmtModemAutoAnswer_Type.__name__ = "Integer32"
_MrNetMgmtModemAutoAnswer_Object = MibScalar
mrNetMgmtModemAutoAnswer = _MrNetMgmtModemAutoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 13),
    _MrNetMgmtModemAutoAnswer_Type()
)
mrNetMgmtModemAutoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtModemAutoAnswer.setStatus("mandatory")
_MrNetMgmtDomainServer1IpAddress_Type = IpAddress
_MrNetMgmtDomainServer1IpAddress_Object = MibScalar
mrNetMgmtDomainServer1IpAddress = _MrNetMgmtDomainServer1IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 14),
    _MrNetMgmtDomainServer1IpAddress_Type()
)
mrNetMgmtDomainServer1IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtDomainServer1IpAddress.setStatus("mandatory")
_MrNetMgmtDomainServer2IpAddress_Type = IpAddress
_MrNetMgmtDomainServer2IpAddress_Object = MibScalar
mrNetMgmtDomainServer2IpAddress = _MrNetMgmtDomainServer2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 15),
    _MrNetMgmtDomainServer2IpAddress_Type()
)
mrNetMgmtDomainServer2IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtDomainServer2IpAddress.setStatus("mandatory")


class _MrNetMgmtDefaultSearchDomain_Type(DisplayString):
    """Custom type mrNetMgmtDefaultSearchDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MrNetMgmtDefaultSearchDomain_Type.__name__ = "DisplayString"
_MrNetMgmtDefaultSearchDomain_Object = MibScalar
mrNetMgmtDefaultSearchDomain = _MrNetMgmtDefaultSearchDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 16),
    _MrNetMgmtDefaultSearchDomain_Type()
)
mrNetMgmtDefaultSearchDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtDefaultSearchDomain.setStatus("mandatory")
_MrNetMgmtSetClientTable_Object = MibTable
mrNetMgmtSetClientTable = _MrNetMgmtSetClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 17)
)
if mibBuilder.loadTexts:
    mrNetMgmtSetClientTable.setStatus("mandatory")
_MrNetMgmtSetClientEntry_Object = MibTableRow
mrNetMgmtSetClientEntry = _MrNetMgmtSetClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 17, 1)
)
mrNetMgmtSetClientEntry.setIndexNames(
    (0, "CISCO-FASTHUB-MIB", "mrNetMgmtSetClientIndex"),
)
if mibBuilder.loadTexts:
    mrNetMgmtSetClientEntry.setStatus("mandatory")


class _MrNetMgmtSetClientIndex_Type(Integer32):
    """Custom type mrNetMgmtSetClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MrNetMgmtSetClientIndex_Type.__name__ = "Integer32"
_MrNetMgmtSetClientIndex_Object = MibTableColumn
mrNetMgmtSetClientIndex = _MrNetMgmtSetClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 17, 1, 1),
    _MrNetMgmtSetClientIndex_Type()
)
mrNetMgmtSetClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrNetMgmtSetClientIndex.setStatus("mandatory")
_MrNetMgmtSetClientName_Type = DisplayString
_MrNetMgmtSetClientName_Object = MibTableColumn
mrNetMgmtSetClientName = _MrNetMgmtSetClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 17, 1, 2),
    _MrNetMgmtSetClientName_Type()
)
mrNetMgmtSetClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtSetClientName.setStatus("mandatory")


class _MrNetMgmtSetClientStatus_Type(Integer32):
    """Custom type mrNetMgmtSetClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_MrNetMgmtSetClientStatus_Type.__name__ = "Integer32"
_MrNetMgmtSetClientStatus_Object = MibTableColumn
mrNetMgmtSetClientStatus = _MrNetMgmtSetClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 17, 1, 3),
    _MrNetMgmtSetClientStatus_Type()
)
mrNetMgmtSetClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtSetClientStatus.setStatus("mandatory")
_MrNetMgmtTrapClientTable_Object = MibTable
mrNetMgmtTrapClientTable = _MrNetMgmtTrapClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18)
)
if mibBuilder.loadTexts:
    mrNetMgmtTrapClientTable.setStatus("mandatory")
_MrNetMgmtTrapClientEntry_Object = MibTableRow
mrNetMgmtTrapClientEntry = _MrNetMgmtTrapClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18, 1)
)
mrNetMgmtTrapClientEntry.setIndexNames(
    (0, "CISCO-FASTHUB-MIB", "mrNetMgmtTrapClientIndex"),
)
if mibBuilder.loadTexts:
    mrNetMgmtTrapClientEntry.setStatus("mandatory")


class _MrNetMgmtTrapClientIndex_Type(Integer32):
    """Custom type mrNetMgmtTrapClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MrNetMgmtTrapClientIndex_Type.__name__ = "Integer32"
_MrNetMgmtTrapClientIndex_Object = MibTableColumn
mrNetMgmtTrapClientIndex = _MrNetMgmtTrapClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18, 1, 1),
    _MrNetMgmtTrapClientIndex_Type()
)
mrNetMgmtTrapClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrNetMgmtTrapClientIndex.setStatus("mandatory")
_MrNetMgmtTrapClientName_Type = DisplayString
_MrNetMgmtTrapClientName_Object = MibTableColumn
mrNetMgmtTrapClientName = _MrNetMgmtTrapClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18, 1, 2),
    _MrNetMgmtTrapClientName_Type()
)
mrNetMgmtTrapClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtTrapClientName.setStatus("mandatory")


class _MrNetMgmtTrapClientComm_Type(DisplayString):
    """Custom type mrNetMgmtTrapClientComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MrNetMgmtTrapClientComm_Type.__name__ = "DisplayString"
_MrNetMgmtTrapClientComm_Object = MibTableColumn
mrNetMgmtTrapClientComm = _MrNetMgmtTrapClientComm_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18, 1, 3),
    _MrNetMgmtTrapClientComm_Type()
)
mrNetMgmtTrapClientComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtTrapClientComm.setStatus("mandatory")


class _MrNetMgmtTrapClientStatus_Type(Integer32):
    """Custom type mrNetMgmtTrapClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_MrNetMgmtTrapClientStatus_Type.__name__ = "Integer32"
_MrNetMgmtTrapClientStatus_Object = MibTableColumn
mrNetMgmtTrapClientStatus = _MrNetMgmtTrapClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 4, 18, 1, 4),
    _MrNetMgmtTrapClientStatus_Type()
)
mrNetMgmtTrapClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrNetMgmtTrapClientStatus.setStatus("mandatory")
_MrUpgrade_ObjectIdentity = ObjectIdentity
mrUpgrade = _MrUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5)
)
_MrUpgradeFlashSize_Type = Integer32
_MrUpgradeFlashSize_Object = MibScalar
mrUpgradeFlashSize = _MrUpgradeFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 1),
    _MrUpgradeFlashSize_Type()
)
mrUpgradeFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrUpgradeFlashSize.setStatus("mandatory")


class _MrUpgradeLastUpgradeTime_Type(DisplayString):
    """Custom type mrUpgradeLastUpgradeTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MrUpgradeLastUpgradeTime_Type.__name__ = "DisplayString"
_MrUpgradeLastUpgradeTime_Object = MibScalar
mrUpgradeLastUpgradeTime = _MrUpgradeLastUpgradeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 2),
    _MrUpgradeLastUpgradeTime_Type()
)
mrUpgradeLastUpgradeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrUpgradeLastUpgradeTime.setStatus("obsolete")
_MrUpgradeLastUpgradeSource_Type = DisplayString
_MrUpgradeLastUpgradeSource_Object = MibScalar
mrUpgradeLastUpgradeSource = _MrUpgradeLastUpgradeSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 3),
    _MrUpgradeLastUpgradeSource_Type()
)
mrUpgradeLastUpgradeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrUpgradeLastUpgradeSource.setStatus("mandatory")


class _MrUpgradeLastUpgradeStatus_Type(Integer32):
    """Custom type mrUpgradeLastUpgradeStatus based on Integer32"""
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
        *(("failure", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_MrUpgradeLastUpgradeStatus_Type.__name__ = "Integer32"
_MrUpgradeLastUpgradeStatus_Object = MibScalar
mrUpgradeLastUpgradeStatus = _MrUpgradeLastUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 4),
    _MrUpgradeLastUpgradeStatus_Type()
)
mrUpgradeLastUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrUpgradeLastUpgradeStatus.setStatus("mandatory")
_MrUpgradeTFTPServerAddress_Type = DisplayString
_MrUpgradeTFTPServerAddress_Object = MibScalar
mrUpgradeTFTPServerAddress = _MrUpgradeTFTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 5),
    _MrUpgradeTFTPServerAddress_Type()
)
mrUpgradeTFTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrUpgradeTFTPServerAddress.setStatus("mandatory")


class _MrUpgradeTFTPLoadFilename_Type(DisplayString):
    """Custom type mrUpgradeTFTPLoadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MrUpgradeTFTPLoadFilename_Type.__name__ = "DisplayString"
_MrUpgradeTFTPLoadFilename_Object = MibScalar
mrUpgradeTFTPLoadFilename = _MrUpgradeTFTPLoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 6),
    _MrUpgradeTFTPLoadFilename_Type()
)
mrUpgradeTFTPLoadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrUpgradeTFTPLoadFilename.setStatus("mandatory")


class _MrUpgradeTFTPInitiate_Type(Integer32):
    """Custom type mrUpgradeTFTPInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUpgrade", 2),
          ("upgrade", 1))
    )


_MrUpgradeTFTPInitiate_Type.__name__ = "Integer32"
_MrUpgradeTFTPInitiate_Object = MibScalar
mrUpgradeTFTPInitiate = _MrUpgradeTFTPInitiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 7),
    _MrUpgradeTFTPInitiate_Type()
)
mrUpgradeTFTPInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrUpgradeTFTPInitiate.setStatus("mandatory")


class _MrUpgradeTFTPAccept_Type(Integer32):
    """Custom type mrUpgradeTFTPAccept based on Integer32"""
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


_MrUpgradeTFTPAccept_Type.__name__ = "Integer32"
_MrUpgradeTFTPAccept_Object = MibScalar
mrUpgradeTFTPAccept = _MrUpgradeTFTPAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 5, 8),
    _MrUpgradeTFTPAccept_Type()
)
mrUpgradeTFTPAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrUpgradeTFTPAccept.setStatus("mandatory")

# Managed Objects groups


# Notification objects

logonIntruder = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 0, 0)
)
logonIntruder.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    logonIntruder.setStatus(
        ""
    )

hubStackDiagnostic = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 0, 1)
)
hubStackDiagnostic.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    hubStackDiagnostic.setStatus(
        ""
    )

rpsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 0, 2)
)
rpsFailed.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    rpsFailed.setStatus(
        ""
    )

ipAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 2, 11, 1, 0, 3)
)
ipAddressChange.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    ipAddressChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FASTHUB-MIB",
    **{"VisualLEDMap": VisualLEDMap,
       "ciscoFastHubMIB": ciscoFastHubMIB,
       "ciscoFastHubMIBObjects": ciscoFastHubMIBObjects,
       "logonIntruder": logonIntruder,
       "hubStackDiagnostic": hubStackDiagnostic,
       "rpsFailed": rpsFailed,
       "ipAddressChange": ipAddressChange,
       "mrStack": mrStack,
       "mrStackUnitCapacity": mrStackUnitCapacity,
       "mrStackNumberOfUnitsPresent": mrStackNumberOfUnitsPresent,
       "mrStackSelectPrimarySupervisorUnit": mrStackSelectPrimarySupervisorUnit,
       "mrStackPOSTSelect": mrStackPOSTSelect,
       "mrStackReset": mrStackReset,
       "mrStackDefaultReset": mrStackDefaultReset,
       "mrStackClearStatistics": mrStackClearStatistics,
       "mrStackShortJabberLoopCorrections": mrStackShortJabberLoopCorrections,
       "mrSupervisorLog": mrSupervisorLog,
       "mrSupervisorLogTableClear": mrSupervisorLogTableClear,
       "mrSupervisorLogTable": mrSupervisorLogTable,
       "mrSupervisorLogEntry": mrSupervisorLogEntry,
       "mrSupervisorLogIndex": mrSupervisorLogIndex,
       "mrSupervisorLogTime": mrSupervisorLogTime,
       "mrSupervisorLogInfo": mrSupervisorLogInfo,
       "mrSupervisorLogRelativeTime": mrSupervisorLogRelativeTime,
       "mrStackUnit": mrStackUnit,
       "mrStackUnitTable": mrStackUnitTable,
       "mrStackUnitEntry": mrStackUnitEntry,
       "mrStackUnitIndex": mrStackUnitIndex,
       "mrStackUnitPresent": mrStackUnitPresent,
       "mrStackUnitFirstGroupIndex": mrStackUnitFirstGroupIndex,
       "mrStackUnitLastGroupIndex": mrStackUnitLastGroupIndex,
       "mrStackUnitSupervisorPresent": mrStackUnitSupervisorPresent,
       "mrStackUnitSupervisorMajorVersion": mrStackUnitSupervisorMajorVersion,
       "mrStackUnitSupervisorMinorVersion": mrStackUnitSupervisorMinorVersion,
       "mrStackUnitSupervisorBootstrapMajorVersion": mrStackUnitSupervisorBootstrapMajorVersion,
       "mrStackUnitSupervisorBootstrapMinorVersion": mrStackUnitSupervisorBootstrapMinorVersion,
       "mrStackUnitPOSTResult": mrStackUnitPOSTResult,
       "mrStackUnitSupervisorIsPrimary": mrStackUnitSupervisorIsPrimary,
       "mrStackUnitExpansionModulePresent": mrStackUnitExpansionModulePresent,
       "mrStackUnitPortVisualIndicatorSelect": mrStackUnitPortVisualIndicatorSelect,
       "mrStackUnitBasePortVisualIndicatorGreenMap": mrStackUnitBasePortVisualIndicatorGreenMap,
       "mrStackUnitBasePortVisualIndicatorAmberMap": mrStackUnitBasePortVisualIndicatorAmberMap,
       "mrStackUnitExpansionPortVisualIndicatorGreenMap": mrStackUnitExpansionPortVisualIndicatorGreenMap,
       "mrStackUnitExpansionPortVisualIndicatorAmberMap": mrStackUnitExpansionPortVisualIndicatorAmberMap,
       "mrStackUnitActivityVisualIndicator": mrStackUnitActivityVisualIndicator,
       "mrStackUnitCollisionVisualIndicator": mrStackUnitCollisionVisualIndicator,
       "mrStackUnitRPSStatus": mrStackUnitRPSStatus,
       "mrStackUnitRPSVisualIndicator": mrStackUnitRPSVisualIndicator,
       "mrStackUnitSerialNumber": mrStackUnitSerialNumber,
       "mrNetMgmt": mrNetMgmt,
       "mrNetMgmtIpAddress": mrNetMgmtIpAddress,
       "mrNetMgmtIpSubnetMask": mrNetMgmtIpSubnetMask,
       "mrNetMgmtDefaultGateway": mrNetMgmtDefaultGateway,
       "mrNetMgmtEnableAuthenTraps": mrNetMgmtEnableAuthenTraps,
       "mrNetMgmtEnableRIP": mrNetMgmtEnableRIP,
       "mrNetMgmtConsoleInactTime": mrNetMgmtConsoleInactTime,
       "mrNetMgmtConsolePasswordThreshold": mrNetMgmtConsolePasswordThreshold,
       "mrNetMgmtConsoleSilentTime": mrNetMgmtConsoleSilentTime,
       "mrNetMgmtModemInitString": mrNetMgmtModemInitString,
       "mrNetMgmtModemDialString": mrNetMgmtModemDialString,
       "mrNetMgmtModemDialDelay": mrNetMgmtModemDialDelay,
       "mrNetMgmtModemAutoAnswer": mrNetMgmtModemAutoAnswer,
       "mrNetMgmtDomainServer1IpAddress": mrNetMgmtDomainServer1IpAddress,
       "mrNetMgmtDomainServer2IpAddress": mrNetMgmtDomainServer2IpAddress,
       "mrNetMgmtDefaultSearchDomain": mrNetMgmtDefaultSearchDomain,
       "mrNetMgmtSetClientTable": mrNetMgmtSetClientTable,
       "mrNetMgmtSetClientEntry": mrNetMgmtSetClientEntry,
       "mrNetMgmtSetClientIndex": mrNetMgmtSetClientIndex,
       "mrNetMgmtSetClientName": mrNetMgmtSetClientName,
       "mrNetMgmtSetClientStatus": mrNetMgmtSetClientStatus,
       "mrNetMgmtTrapClientTable": mrNetMgmtTrapClientTable,
       "mrNetMgmtTrapClientEntry": mrNetMgmtTrapClientEntry,
       "mrNetMgmtTrapClientIndex": mrNetMgmtTrapClientIndex,
       "mrNetMgmtTrapClientName": mrNetMgmtTrapClientName,
       "mrNetMgmtTrapClientComm": mrNetMgmtTrapClientComm,
       "mrNetMgmtTrapClientStatus": mrNetMgmtTrapClientStatus,
       "mrUpgrade": mrUpgrade,
       "mrUpgradeFlashSize": mrUpgradeFlashSize,
       "mrUpgradeLastUpgradeTime": mrUpgradeLastUpgradeTime,
       "mrUpgradeLastUpgradeSource": mrUpgradeLastUpgradeSource,
       "mrUpgradeLastUpgradeStatus": mrUpgradeLastUpgradeStatus,
       "mrUpgradeTFTPServerAddress": mrUpgradeTFTPServerAddress,
       "mrUpgradeTFTPLoadFilename": mrUpgradeTFTPLoadFilename,
       "mrUpgradeTFTPInitiate": mrUpgradeTFTPInitiate,
       "mrUpgradeTFTPAccept": mrUpgradeTFTPAccept}
)
