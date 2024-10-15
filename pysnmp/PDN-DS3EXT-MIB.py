# SNMP MIB module (PDN-DS3EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-DS3EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:34 2024
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

(dsx3CurrentEntry,
 dsx3IntervalEntry,
 dsx3TotalEntry) = mibBuilder.importSymbols(
    "DS3-MIB",
    "dsx3CurrentEntry",
    "dsx3IntervalEntry",
    "dsx3TotalEntry")

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pdnDs3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14)
)
pdnDs3MIB.setRevisions(
        ("1902-07-10 00:00",
         "1902-07-05 00:00",
         "1900-05-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DevDs3Objects_ObjectIdentity = ObjectIdentity
devDs3Objects = _DevDs3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1)
)
_DevDs3ConfigTable_Object = MibTable
devDs3ConfigTable = _DevDs3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1)
)
if mibBuilder.loadTexts:
    devDs3ConfigTable.setStatus("current")
_DevDs3ConfigEntry_Object = MibTableRow
devDs3ConfigEntry = _DevDs3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1, 1)
)
devDs3ConfigEntry.setIndexNames(
    (0, "PDN-DS3EXT-MIB", "devDs3ConfigIfIndex"),
)
if mibBuilder.loadTexts:
    devDs3ConfigEntry.setStatus("current")
_DevDs3ConfigIfIndex_Type = Integer32
_DevDs3ConfigIfIndex_Object = MibTableColumn
devDs3ConfigIfIndex = _DevDs3ConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1, 1, 1),
    _DevDs3ConfigIfIndex_Type()
)
devDs3ConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3ConfigIfIndex.setStatus("current")


class _DevDs3ConfigFramingType_Type(Integer32):
    """Custom type devDs3ConfigFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("plcp", 2))
    )


_DevDs3ConfigFramingType_Type.__name__ = "Integer32"
_DevDs3ConfigFramingType_Object = MibTableColumn
devDs3ConfigFramingType = _DevDs3ConfigFramingType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1, 1, 2),
    _DevDs3ConfigFramingType_Type()
)
devDs3ConfigFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDs3ConfigFramingType.setStatus("current")


class _DevDs3ConfigIgnoreCbit_Type(Integer32):
    """Custom type devDs3ConfigIgnoreCbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DevDs3ConfigIgnoreCbit_Type.__name__ = "Integer32"
_DevDs3ConfigIgnoreCbit_Object = MibTableColumn
devDs3ConfigIgnoreCbit = _DevDs3ConfigIgnoreCbit_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1, 1, 3),
    _DevDs3ConfigIgnoreCbit_Type()
)
devDs3ConfigIgnoreCbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDs3ConfigIgnoreCbit.setStatus("current")


class _DevDs3ConfigTimingMarkerCode_Type(Integer32):
    """Custom type devDs3ConfigTimingMarkerCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notTraceable", 2),
          ("traceable", 1))
    )


_DevDs3ConfigTimingMarkerCode_Type.__name__ = "Integer32"
_DevDs3ConfigTimingMarkerCode_Object = MibTableColumn
devDs3ConfigTimingMarkerCode = _DevDs3ConfigTimingMarkerCode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1, 1, 4),
    _DevDs3ConfigTimingMarkerCode_Type()
)
devDs3ConfigTimingMarkerCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDs3ConfigTimingMarkerCode.setStatus("current")
_DevDs3CurrentTable_Object = MibTable
devDs3CurrentTable = _DevDs3CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2)
)
if mibBuilder.loadTexts:
    devDs3CurrentTable.setStatus("current")
_DevDs3CurrentEntry_Object = MibTableRow
devDs3CurrentEntry = _DevDs3CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    devDs3CurrentEntry.setStatus("current")
_DevDs3CurrentEB_Type = PerfCurrentCount
_DevDs3CurrentEB_Object = MibTableColumn
devDs3CurrentEB = _DevDs3CurrentEB_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2, 1, 1),
    _DevDs3CurrentEB_Type()
)
devDs3CurrentEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3CurrentEB.setStatus("current")
_DevDs3CurrentES_Type = PerfCurrentCount
_DevDs3CurrentES_Object = MibTableColumn
devDs3CurrentES = _DevDs3CurrentES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2, 1, 2),
    _DevDs3CurrentES_Type()
)
devDs3CurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3CurrentES.setStatus("current")
_DevDs3CurrentSES_Type = PerfCurrentCount
_DevDs3CurrentSES_Object = MibTableColumn
devDs3CurrentSES = _DevDs3CurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2, 1, 3),
    _DevDs3CurrentSES_Type()
)
devDs3CurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3CurrentSES.setStatus("current")
_DevDs3CurrentPlcpSEFS_Type = PerfCurrentCount
_DevDs3CurrentPlcpSEFS_Object = MibTableColumn
devDs3CurrentPlcpSEFS = _DevDs3CurrentPlcpSEFS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2, 1, 4),
    _DevDs3CurrentPlcpSEFS_Type()
)
devDs3CurrentPlcpSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3CurrentPlcpSEFS.setStatus("current")
_DevDs3IntervalTable_Object = MibTable
devDs3IntervalTable = _DevDs3IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3)
)
if mibBuilder.loadTexts:
    devDs3IntervalTable.setStatus("current")
_DevDs3IntervalEntry_Object = MibTableRow
devDs3IntervalEntry = _DevDs3IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3, 1)
)
if mibBuilder.loadTexts:
    devDs3IntervalEntry.setStatus("current")
_DevDs3IntervalEB_Type = PerfIntervalCount
_DevDs3IntervalEB_Object = MibTableColumn
devDs3IntervalEB = _DevDs3IntervalEB_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3, 1, 1),
    _DevDs3IntervalEB_Type()
)
devDs3IntervalEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3IntervalEB.setStatus("current")
_DevDs3IntervalES_Type = PerfIntervalCount
_DevDs3IntervalES_Object = MibTableColumn
devDs3IntervalES = _DevDs3IntervalES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3, 1, 2),
    _DevDs3IntervalES_Type()
)
devDs3IntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3IntervalES.setStatus("current")
_DevDs3IntervalSES_Type = PerfIntervalCount
_DevDs3IntervalSES_Object = MibTableColumn
devDs3IntervalSES = _DevDs3IntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3, 1, 3),
    _DevDs3IntervalSES_Type()
)
devDs3IntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3IntervalSES.setStatus("current")
_DevDs3IntervalPlcpSEFS_Type = PerfIntervalCount
_DevDs3IntervalPlcpSEFS_Object = MibTableColumn
devDs3IntervalPlcpSEFS = _DevDs3IntervalPlcpSEFS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3, 1, 4),
    _DevDs3IntervalPlcpSEFS_Type()
)
devDs3IntervalPlcpSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3IntervalPlcpSEFS.setStatus("current")
_DevDs3TotalTable_Object = MibTable
devDs3TotalTable = _DevDs3TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4)
)
if mibBuilder.loadTexts:
    devDs3TotalTable.setStatus("current")
_DevDs3TotalEntry_Object = MibTableRow
devDs3TotalEntry = _DevDs3TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4, 1)
)
if mibBuilder.loadTexts:
    devDs3TotalEntry.setStatus("current")
_DevDs3TotalEB_Type = PerfTotalCount
_DevDs3TotalEB_Object = MibTableColumn
devDs3TotalEB = _DevDs3TotalEB_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4, 1, 1),
    _DevDs3TotalEB_Type()
)
devDs3TotalEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3TotalEB.setStatus("current")
_DevDs3TotalES_Type = PerfTotalCount
_DevDs3TotalES_Object = MibTableColumn
devDs3TotalES = _DevDs3TotalES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4, 1, 2),
    _DevDs3TotalES_Type()
)
devDs3TotalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3TotalES.setStatus("current")
_DevDs3TotalSES_Type = PerfTotalCount
_DevDs3TotalSES_Object = MibTableColumn
devDs3TotalSES = _DevDs3TotalSES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4, 1, 3),
    _DevDs3TotalSES_Type()
)
devDs3TotalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3TotalSES.setStatus("current")
_DevDs3TotalPlcpSEFS_Type = PerfTotalCount
_DevDs3TotalPlcpSEFS_Object = MibTableColumn
devDs3TotalPlcpSEFS = _DevDs3TotalPlcpSEFS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4, 1, 4),
    _DevDs3TotalPlcpSEFS_Type()
)
devDs3TotalPlcpSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3TotalPlcpSEFS.setStatus("current")
_DevDs3FreeRunTable_Object = MibTable
devDs3FreeRunTable = _DevDs3FreeRunTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5)
)
if mibBuilder.loadTexts:
    devDs3FreeRunTable.setStatus("current")
_DevDs3FreeRunEntry_Object = MibTableRow
devDs3FreeRunEntry = _DevDs3FreeRunEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1)
)
if mibBuilder.loadTexts:
    devDs3FreeRunEntry.setStatus("current")
_DevDs3FreeRunPES_Type = PerfTotalCount
_DevDs3FreeRunPES_Object = MibTableColumn
devDs3FreeRunPES = _DevDs3FreeRunPES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 1),
    _DevDs3FreeRunPES_Type()
)
devDs3FreeRunPES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3FreeRunPES.setStatus("current")
_DevDs3FreeRunPSES_Type = PerfTotalCount
_DevDs3FreeRunPSES_Object = MibTableColumn
devDs3FreeRunPSES = _DevDs3FreeRunPSES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 2),
    _DevDs3FreeRunPSES_Type()
)
devDs3FreeRunPSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3FreeRunPSES.setStatus("current")
_DevDs3FreeRunPSEFS_Type = PerfTotalCount
_DevDs3FreeRunPSEFS_Object = MibTableColumn
devDs3FreeRunPSEFS = _DevDs3FreeRunPSEFS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 3),
    _DevDs3FreeRunPSEFS_Type()
)
devDs3FreeRunPSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3FreeRunPSEFS.setStatus("current")
_DevDs3FreeRunUAS_Type = PerfTotalCount
_DevDs3FreeRunUAS_Object = MibTableColumn
devDs3FreeRunUAS = _DevDs3FreeRunUAS_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 4),
    _DevDs3FreeRunUAS_Type()
)
devDs3FreeRunUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3FreeRunUAS.setStatus("current")
_DevDs3FreeRunLCV_Type = PerfTotalCount
_DevDs3FreeRunLCV_Object = MibTableColumn
devDs3FreeRunLCV = _DevDs3FreeRunLCV_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 5),
    _DevDs3FreeRunLCV_Type()
)
devDs3FreeRunLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3FreeRunLCV.setStatus("current")
_DevDs3FreeRunPCV_Type = PerfTotalCount
_DevDs3FreeRunPCV_Object = MibTableColumn
devDs3FreeRunPCV = _DevDs3FreeRunPCV_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 6),
    _DevDs3FreeRunPCV_Type()
)
devDs3FreeRunPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3FreeRunPCV.setStatus("current")
_DevDs3FreeRunLES_Type = PerfTotalCount
_DevDs3FreeRunLES_Object = MibTableColumn
devDs3FreeRunLES = _DevDs3FreeRunLES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 7),
    _DevDs3FreeRunLES_Type()
)
devDs3FreeRunLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3FreeRunLES.setStatus("current")
_DevDs3FreeRunCCV_Type = PerfTotalCount
_DevDs3FreeRunCCV_Object = MibTableColumn
devDs3FreeRunCCV = _DevDs3FreeRunCCV_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 8),
    _DevDs3FreeRunCCV_Type()
)
devDs3FreeRunCCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3FreeRunCCV.setStatus("current")
_DevDs3FreeRunCES_Type = PerfTotalCount
_DevDs3FreeRunCES_Object = MibTableColumn
devDs3FreeRunCES = _DevDs3FreeRunCES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 9),
    _DevDs3FreeRunCES_Type()
)
devDs3FreeRunCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3FreeRunCES.setStatus("current")
_DevDs3FreeRunCSES_Type = PerfTotalCount
_DevDs3FreeRunCSES_Object = MibTableColumn
devDs3FreeRunCSES = _DevDs3FreeRunCSES_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 10),
    _DevDs3FreeRunCSES_Type()
)
devDs3FreeRunCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDs3FreeRunCSES.setStatus("current")
dsx3CurrentEntry.registerAugmentions(
    ("PDN-DS3EXT-MIB",
     "devDs3CurrentEntry")
)
devDs3CurrentEntry.setIndexNames(*dsx3CurrentEntry.getIndexNames())
dsx3IntervalEntry.registerAugmentions(
    ("PDN-DS3EXT-MIB",
     "devDs3IntervalEntry")
)
devDs3IntervalEntry.setIndexNames(*dsx3IntervalEntry.getIndexNames())
dsx3TotalEntry.registerAugmentions(
    ("PDN-DS3EXT-MIB",
     "devDs3TotalEntry")
)
devDs3TotalEntry.setIndexNames(*dsx3TotalEntry.getIndexNames())
dsx3TotalEntry.registerAugmentions(
    ("PDN-DS3EXT-MIB",
     "devDs3FreeRunEntry")
)
devDs3FreeRunEntry.setIndexNames(*dsx3TotalEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DS3EXT-MIB",
    **{"pdnDs3MIB": pdnDs3MIB,
       "devDs3Objects": devDs3Objects,
       "devDs3ConfigTable": devDs3ConfigTable,
       "devDs3ConfigEntry": devDs3ConfigEntry,
       "devDs3ConfigIfIndex": devDs3ConfigIfIndex,
       "devDs3ConfigFramingType": devDs3ConfigFramingType,
       "devDs3ConfigIgnoreCbit": devDs3ConfigIgnoreCbit,
       "devDs3ConfigTimingMarkerCode": devDs3ConfigTimingMarkerCode,
       "devDs3CurrentTable": devDs3CurrentTable,
       "devDs3CurrentEntry": devDs3CurrentEntry,
       "devDs3CurrentEB": devDs3CurrentEB,
       "devDs3CurrentES": devDs3CurrentES,
       "devDs3CurrentSES": devDs3CurrentSES,
       "devDs3CurrentPlcpSEFS": devDs3CurrentPlcpSEFS,
       "devDs3IntervalTable": devDs3IntervalTable,
       "devDs3IntervalEntry": devDs3IntervalEntry,
       "devDs3IntervalEB": devDs3IntervalEB,
       "devDs3IntervalES": devDs3IntervalES,
       "devDs3IntervalSES": devDs3IntervalSES,
       "devDs3IntervalPlcpSEFS": devDs3IntervalPlcpSEFS,
       "devDs3TotalTable": devDs3TotalTable,
       "devDs3TotalEntry": devDs3TotalEntry,
       "devDs3TotalEB": devDs3TotalEB,
       "devDs3TotalES": devDs3TotalES,
       "devDs3TotalSES": devDs3TotalSES,
       "devDs3TotalPlcpSEFS": devDs3TotalPlcpSEFS,
       "devDs3FreeRunTable": devDs3FreeRunTable,
       "devDs3FreeRunEntry": devDs3FreeRunEntry,
       "devDs3FreeRunPES": devDs3FreeRunPES,
       "devDs3FreeRunPSES": devDs3FreeRunPSES,
       "devDs3FreeRunPSEFS": devDs3FreeRunPSEFS,
       "devDs3FreeRunUAS": devDs3FreeRunUAS,
       "devDs3FreeRunLCV": devDs3FreeRunLCV,
       "devDs3FreeRunPCV": devDs3FreeRunPCV,
       "devDs3FreeRunLES": devDs3FreeRunLES,
       "devDs3FreeRunCCV": devDs3FreeRunCCV,
       "devDs3FreeRunCES": devDs3FreeRunCES,
       "devDs3FreeRunCSES": devDs3FreeRunCSES}
)
