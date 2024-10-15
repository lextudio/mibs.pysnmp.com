# SNMP MIB module (UTILIZATION-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UTILIZATION-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:10 2024
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

(avayaSystemStats,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "avayaSystemStats")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

genStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1)
)
genStats.setRevisions(
        ("2003-05-18 16:16",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MBytes(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_GenCpuUtilization_ObjectIdentity = ObjectIdentity
genCpuUtilization = _GenCpuUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1)
)
_GenCpuUtilizationTable_Object = MibTable
genCpuUtilizationTable = _GenCpuUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    genCpuUtilizationTable.setStatus("current")
_GenCpuUtilizationEntry_Object = MibTableRow
genCpuUtilizationEntry = _GenCpuUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 1, 1)
)
genCpuUtilizationEntry.setIndexNames(
    (0, "UTILIZATION-MANAGEMENT-MIB", "genCpuIndex"),
)
if mibBuilder.loadTexts:
    genCpuUtilizationEntry.setStatus("current")
_GenCpuIndex_Type = Integer32
_GenCpuIndex_Object = MibTableColumn
genCpuIndex = _GenCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 1, 1, 1),
    _GenCpuIndex_Type()
)
genCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCpuIndex.setStatus("current")


class _GenCpuUtilizationEnableMonitoring_Type(Integer32):
    """Custom type genCpuUtilizationEnableMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_GenCpuUtilizationEnableMonitoring_Type.__name__ = "Integer32"
_GenCpuUtilizationEnableMonitoring_Object = MibTableColumn
genCpuUtilizationEnableMonitoring = _GenCpuUtilizationEnableMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 1, 1, 2),
    _GenCpuUtilizationEnableMonitoring_Type()
)
genCpuUtilizationEnableMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genCpuUtilizationEnableMonitoring.setStatus("current")


class _GenCpuUtilizationEnableEventGeneration_Type(Integer32):
    """Custom type genCpuUtilizationEnableEventGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_GenCpuUtilizationEnableEventGeneration_Type.__name__ = "Integer32"
_GenCpuUtilizationEnableEventGeneration_Object = MibTableColumn
genCpuUtilizationEnableEventGeneration = _GenCpuUtilizationEnableEventGeneration_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 1, 1, 3),
    _GenCpuUtilizationEnableEventGeneration_Type()
)
genCpuUtilizationEnableEventGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genCpuUtilizationEnableEventGeneration.setStatus("current")


class _GenCpuUtilizationHighThreshold_Type(Integer32):
    """Custom type genCpuUtilizationHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 99),
    )


_GenCpuUtilizationHighThreshold_Type.__name__ = "Integer32"
_GenCpuUtilizationHighThreshold_Object = MibTableColumn
genCpuUtilizationHighThreshold = _GenCpuUtilizationHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 1, 1, 4),
    _GenCpuUtilizationHighThreshold_Type()
)
genCpuUtilizationHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genCpuUtilizationHighThreshold.setStatus("current")


class _GenCpuAverageUtilization_Type(Integer32):
    """Custom type genCpuAverageUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GenCpuAverageUtilization_Type.__name__ = "Integer32"
_GenCpuAverageUtilization_Object = MibTableColumn
genCpuAverageUtilization = _GenCpuAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 1, 1, 5),
    _GenCpuAverageUtilization_Type()
)
genCpuAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCpuAverageUtilization.setStatus("current")


class _GenCpuCurrentUtilization_Type(Integer32):
    """Custom type genCpuCurrentUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GenCpuCurrentUtilization_Type.__name__ = "Integer32"
_GenCpuCurrentUtilization_Object = MibTableColumn
genCpuCurrentUtilization = _GenCpuCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 1, 1, 6),
    _GenCpuCurrentUtilization_Type()
)
genCpuCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCpuCurrentUtilization.setStatus("obsolete")
_GenCpuUtilizationHistoryTable_Object = MibTable
genCpuUtilizationHistoryTable = _GenCpuUtilizationHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    genCpuUtilizationHistoryTable.setStatus("current")
_GenCpuUtilizationHistoryEntry_Object = MibTableRow
genCpuUtilizationHistoryEntry = _GenCpuUtilizationHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 2, 1)
)
genCpuUtilizationHistoryEntry.setIndexNames(
    (0, "UTILIZATION-MANAGEMENT-MIB", "genCpuIndex"),
    (0, "UTILIZATION-MANAGEMENT-MIB", "genCpuUtilizationHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    genCpuUtilizationHistoryEntry.setStatus("current")
_GenCpuUtilizationHistorySampleIndex_Type = Integer32
_GenCpuUtilizationHistorySampleIndex_Object = MibTableColumn
genCpuUtilizationHistorySampleIndex = _GenCpuUtilizationHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 2, 1, 1),
    _GenCpuUtilizationHistorySampleIndex_Type()
)
genCpuUtilizationHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCpuUtilizationHistorySampleIndex.setStatus("current")
_GenCpuHistoryUtilization_Type = Integer32
_GenCpuHistoryUtilization_Object = MibTableColumn
genCpuHistoryUtilization = _GenCpuHistoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 1, 2, 1, 2),
    _GenCpuHistoryUtilization_Type()
)
genCpuHistoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCpuHistoryUtilization.setStatus("current")
_GenMemUtilization_ObjectIdentity = ObjectIdentity
genMemUtilization = _GenMemUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2)
)
_GenMemUtilizationTotalRAM_Type = MBytes
_GenMemUtilizationTotalRAM_Object = MibScalar
genMemUtilizationTotalRAM = _GenMemUtilizationTotalRAM_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 1),
    _GenMemUtilizationTotalRAM_Type()
)
genMemUtilizationTotalRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMemUtilizationTotalRAM.setStatus("current")
_GenMemUtilizationOperationalImage_Type = MBytes
_GenMemUtilizationOperationalImage_Object = MibScalar
genMemUtilizationOperationalImage = _GenMemUtilizationOperationalImage_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 2),
    _GenMemUtilizationOperationalImage_Type()
)
genMemUtilizationOperationalImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMemUtilizationOperationalImage.setStatus("current")
_GenMemUtilizationDynAllocMem_ObjectIdentity = ObjectIdentity
genMemUtilizationDynAllocMem = _GenMemUtilizationDynAllocMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 3)
)
_GenMemUtilizationDynAllocMemUsed_Type = MBytes
_GenMemUtilizationDynAllocMemUsed_Object = MibScalar
genMemUtilizationDynAllocMemUsed = _GenMemUtilizationDynAllocMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 3, 1),
    _GenMemUtilizationDynAllocMemUsed_Type()
)
genMemUtilizationDynAllocMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMemUtilizationDynAllocMemUsed.setStatus("current")
_GenMemUtilizationDynAllocMemMaxUsed_Type = MBytes
_GenMemUtilizationDynAllocMemMaxUsed_Object = MibScalar
genMemUtilizationDynAllocMemMaxUsed = _GenMemUtilizationDynAllocMemMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 3, 2),
    _GenMemUtilizationDynAllocMemMaxUsed_Type()
)
genMemUtilizationDynAllocMemMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMemUtilizationDynAllocMemMaxUsed.setStatus("current")
_GenMemUtilizationDynAllocMemAvailable_Type = MBytes
_GenMemUtilizationDynAllocMemAvailable_Object = MibScalar
genMemUtilizationDynAllocMemAvailable = _GenMemUtilizationDynAllocMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 3, 3),
    _GenMemUtilizationDynAllocMemAvailable_Type()
)
genMemUtilizationDynAllocMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMemUtilizationDynAllocMemAvailable.setStatus("current")
_GenMemUtilizationAllocationFailures_Type = MBytes
_GenMemUtilizationAllocationFailures_Object = MibScalar
genMemUtilizationAllocationFailures = _GenMemUtilizationAllocationFailures_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 4),
    _GenMemUtilizationAllocationFailures_Type()
)
genMemUtilizationAllocationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMemUtilizationAllocationFailures.setStatus("current")
_GenMemUtilizationSysRAMTrap_ObjectIdentity = ObjectIdentity
genMemUtilizationSysRAMTrap = _GenMemUtilizationSysRAMTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 5)
)
_GenMemUtilizationSysRAMNotificationHighWaterMark_Type = MBytes
_GenMemUtilizationSysRAMNotificationHighWaterMark_Object = MibScalar
genMemUtilizationSysRAMNotificationHighWaterMark = _GenMemUtilizationSysRAMNotificationHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 5, 1),
    _GenMemUtilizationSysRAMNotificationHighWaterMark_Type()
)
genMemUtilizationSysRAMNotificationHighWaterMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genMemUtilizationSysRAMNotificationHighWaterMark.setStatus("current")
_GenMemUtilizationTable_Object = MibTable
genMemUtilizationTable = _GenMemUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 6)
)
if mibBuilder.loadTexts:
    genMemUtilizationTable.setStatus("current")
_GenMemUtilizationEntry_Object = MibTableRow
genMemUtilizationEntry = _GenMemUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 6, 1)
)
genMemUtilizationEntry.setIndexNames(
    (0, "UTILIZATION-MANAGEMENT-MIB", "genMemUtilizationID"),
)
if mibBuilder.loadTexts:
    genMemUtilizationEntry.setStatus("current")


class _GenMemUtilizationID_Type(Integer32):
    """Custom type genMemUtilizationID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_GenMemUtilizationID_Type.__name__ = "Integer32"
_GenMemUtilizationID_Object = MibTableColumn
genMemUtilizationID = _GenMemUtilizationID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 6, 1, 1),
    _GenMemUtilizationID_Type()
)
genMemUtilizationID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    genMemUtilizationID.setStatus("current")
_GenMemUtilizationPhyRam_Type = MBytes
_GenMemUtilizationPhyRam_Object = MibTableColumn
genMemUtilizationPhyRam = _GenMemUtilizationPhyRam_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 6, 1, 2),
    _GenMemUtilizationPhyRam_Type()
)
genMemUtilizationPhyRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMemUtilizationPhyRam.setStatus("current")


class _GenMemUtilizationPercentUsed_Type(Integer32):
    """Custom type genMemUtilizationPercentUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GenMemUtilizationPercentUsed_Type.__name__ = "Integer32"
_GenMemUtilizationPercentUsed_Object = MibTableColumn
genMemUtilizationPercentUsed = _GenMemUtilizationPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11, 1, 2, 6, 1, 3),
    _GenMemUtilizationPercentUsed_Type()
)
genMemUtilizationPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMemUtilizationPercentUsed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UTILIZATION-MANAGEMENT-MIB",
    **{"MBytes": MBytes,
       "genStats": genStats,
       "genCpuUtilization": genCpuUtilization,
       "genCpuUtilizationTable": genCpuUtilizationTable,
       "genCpuUtilizationEntry": genCpuUtilizationEntry,
       "genCpuIndex": genCpuIndex,
       "genCpuUtilizationEnableMonitoring": genCpuUtilizationEnableMonitoring,
       "genCpuUtilizationEnableEventGeneration": genCpuUtilizationEnableEventGeneration,
       "genCpuUtilizationHighThreshold": genCpuUtilizationHighThreshold,
       "genCpuAverageUtilization": genCpuAverageUtilization,
       "genCpuCurrentUtilization": genCpuCurrentUtilization,
       "genCpuUtilizationHistoryTable": genCpuUtilizationHistoryTable,
       "genCpuUtilizationHistoryEntry": genCpuUtilizationHistoryEntry,
       "genCpuUtilizationHistorySampleIndex": genCpuUtilizationHistorySampleIndex,
       "genCpuHistoryUtilization": genCpuHistoryUtilization,
       "genMemUtilization": genMemUtilization,
       "genMemUtilizationTotalRAM": genMemUtilizationTotalRAM,
       "genMemUtilizationOperationalImage": genMemUtilizationOperationalImage,
       "genMemUtilizationDynAllocMem": genMemUtilizationDynAllocMem,
       "genMemUtilizationDynAllocMemUsed": genMemUtilizationDynAllocMemUsed,
       "genMemUtilizationDynAllocMemMaxUsed": genMemUtilizationDynAllocMemMaxUsed,
       "genMemUtilizationDynAllocMemAvailable": genMemUtilizationDynAllocMemAvailable,
       "genMemUtilizationAllocationFailures": genMemUtilizationAllocationFailures,
       "genMemUtilizationSysRAMTrap": genMemUtilizationSysRAMTrap,
       "genMemUtilizationSysRAMNotificationHighWaterMark": genMemUtilizationSysRAMNotificationHighWaterMark,
       "genMemUtilizationTable": genMemUtilizationTable,
       "genMemUtilizationEntry": genMemUtilizationEntry,
       "genMemUtilizationID": genMemUtilizationID,
       "genMemUtilizationPhyRam": genMemUtilizationPhyRam,
       "genMemUtilizationPercentUsed": genMemUtilizationPercentUsed}
)
