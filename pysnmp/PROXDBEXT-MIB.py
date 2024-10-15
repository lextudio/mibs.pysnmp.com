# SNMP MIB module (PROXDBEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PROXDBEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:53 2024
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

(proxDbExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "proxDbExt")

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

apProxDbExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApProxDbTTLProbed_Type(Integer32):
    """Custom type apProxDbTTLProbed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApProxDbTTLProbed_Type.__name__ = "Integer32"
_ApProxDbTTLProbed_Object = MibScalar
apProxDbTTLProbed = _ApProxDbTTLProbed_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 2),
    _ApProxDbTTLProbed_Type()
)
apProxDbTTLProbed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProxDbTTLProbed.setStatus("current")


class _ApProxDbTTLAssigned_Type(Integer32):
    """Custom type apProxDbTTLAssigned based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApProxDbTTLAssigned_Type.__name__ = "Integer32"
_ApProxDbTTLAssigned_Object = MibScalar
apProxDbTTLAssigned = _ApProxDbTTLAssigned_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 3),
    _ApProxDbTTLAssigned_Type()
)
apProxDbTTLAssigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProxDbTTLAssigned.setStatus("current")
_ApProxDb8StatTable_Object = MibTable
apProxDb8StatTable = _ApProxDb8StatTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 6)
)
if mibBuilder.loadTexts:
    apProxDb8StatTable.setStatus("current")
_ApProxDb8StatEntry_Object = MibTableRow
apProxDb8StatEntry = _ApProxDb8StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 6, 1)
)
apProxDb8StatEntry.setIndexNames(
    (0, "PROXDBEXT-MIB", "apProx8StatIpAddress"),
)
if mibBuilder.loadTexts:
    apProxDb8StatEntry.setStatus("current")
_ApProx8StatIpAddress_Type = IpAddress
_ApProx8StatIpAddress_Object = MibTableColumn
apProx8StatIpAddress = _ApProx8StatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 6, 1, 1),
    _ApProx8StatIpAddress_Type()
)
apProx8StatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx8StatIpAddress.setStatus("current")
_ApProx8StatHitCount_Type = Counter64
_ApProx8StatHitCount_Object = MibTableColumn
apProx8StatHitCount = _ApProx8StatHitCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 6, 1, 2),
    _ApProx8StatHitCount_Type()
)
apProx8StatHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx8StatHitCount.setStatus("current")
_ApProx8StatAdvMask_Type = Integer32
_ApProx8StatAdvMask_Object = MibTableColumn
apProx8StatAdvMask = _ApProx8StatAdvMask_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 6, 1, 3),
    _ApProx8StatAdvMask_Type()
)
apProx8StatAdvMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx8StatAdvMask.setStatus("current")
_ApProxDb16StatTable_Object = MibTable
apProxDb16StatTable = _ApProxDb16StatTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 7)
)
if mibBuilder.loadTexts:
    apProxDb16StatTable.setStatus("current")
_ApProxDb16StatEntry_Object = MibTableRow
apProxDb16StatEntry = _ApProxDb16StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 7, 1)
)
apProxDb16StatEntry.setIndexNames(
    (0, "PROXDBEXT-MIB", "apProx16StatIpAddress"),
)
if mibBuilder.loadTexts:
    apProxDb16StatEntry.setStatus("current")
_ApProx16StatIpAddress_Type = IpAddress
_ApProx16StatIpAddress_Object = MibTableColumn
apProx16StatIpAddress = _ApProx16StatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 7, 1, 1),
    _ApProx16StatIpAddress_Type()
)
apProx16StatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx16StatIpAddress.setStatus("current")
_ApProx16StatHitCount_Type = Integer32
_ApProx16StatHitCount_Object = MibTableColumn
apProx16StatHitCount = _ApProx16StatHitCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 7, 1, 2),
    _ApProx16StatHitCount_Type()
)
apProx16StatHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx16StatHitCount.setStatus("current")
_ApProx16StatAdvMask_Type = Integer32
_ApProx16StatAdvMask_Object = MibTableColumn
apProx16StatAdvMask = _ApProx16StatAdvMask_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 7, 1, 3),
    _ApProx16StatAdvMask_Type()
)
apProx16StatAdvMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx16StatAdvMask.setStatus("current")
_ApProxDb24StatTable_Object = MibTable
apProxDb24StatTable = _ApProxDb24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 8)
)
if mibBuilder.loadTexts:
    apProxDb24StatTable.setStatus("current")
_ApProxDb24StatEntry_Object = MibTableRow
apProxDb24StatEntry = _ApProxDb24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 8, 1)
)
apProxDb24StatEntry.setIndexNames(
    (0, "PROXDBEXT-MIB", "apProx24StatIpAddress"),
)
if mibBuilder.loadTexts:
    apProxDb24StatEntry.setStatus("current")
_ApProx24StatIpAddress_Type = IpAddress
_ApProx24StatIpAddress_Object = MibTableColumn
apProx24StatIpAddress = _ApProx24StatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 8, 1, 1),
    _ApProx24StatIpAddress_Type()
)
apProx24StatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx24StatIpAddress.setStatus("current")
_ApProx24StatHitCount_Type = Integer32
_ApProx24StatHitCount_Object = MibTableColumn
apProx24StatHitCount = _ApProx24StatHitCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 8, 1, 2),
    _ApProx24StatHitCount_Type()
)
apProx24StatHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx24StatHitCount.setStatus("current")
_ApProx24StatAdvMask_Type = Integer32
_ApProx24StatAdvMask_Object = MibTableColumn
apProx24StatAdvMask = _ApProx24StatAdvMask_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 8, 1, 3),
    _ApProx24StatAdvMask_Type()
)
apProx24StatAdvMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx24StatAdvMask.setStatus("current")
_ApProxDbVplStatTable_Object = MibTable
apProxDbVplStatTable = _ApProxDbVplStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 9)
)
if mibBuilder.loadTexts:
    apProxDbVplStatTable.setStatus("current")
_ApProxDbVplStatEntry_Object = MibTableRow
apProxDbVplStatEntry = _ApProxDbVplStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 9, 1)
)
apProxDbVplStatEntry.setIndexNames(
    (0, "PROXDBEXT-MIB", "apProxVplStatIpAddress"),
    (0, "PROXDBEXT-MIB", "apProxVplStatIpPrefix"),
)
if mibBuilder.loadTexts:
    apProxDbVplStatEntry.setStatus("current")
_ApProxVplStatIpAddress_Type = IpAddress
_ApProxVplStatIpAddress_Object = MibTableColumn
apProxVplStatIpAddress = _ApProxVplStatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 9, 1, 1),
    _ApProxVplStatIpAddress_Type()
)
apProxVplStatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProxVplStatIpAddress.setStatus("current")
_ApProxVplStatIpPrefix_Type = Integer32
_ApProxVplStatIpPrefix_Object = MibTableColumn
apProxVplStatIpPrefix = _ApProxVplStatIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 9, 1, 2),
    _ApProxVplStatIpPrefix_Type()
)
apProxVplStatIpPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProxVplStatIpPrefix.setStatus("current")
_ApProxVplStatHitCount_Type = Integer32
_ApProxVplStatHitCount_Object = MibTableColumn
apProxVplStatHitCount = _ApProxVplStatHitCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 9, 1, 3),
    _ApProxVplStatHitCount_Type()
)
apProxVplStatHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProxVplStatHitCount.setStatus("current")
_ApProxVplStatAdvMask_Type = Integer32
_ApProxVplStatAdvMask_Object = MibTableColumn
apProxVplStatAdvMask = _ApProxVplStatAdvMask_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 9, 1, 4),
    _ApProxVplStatAdvMask_Type()
)
apProxVplStatAdvMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProxVplStatAdvMask.setStatus("current")
_ApProxDb8MetricTable_Object = MibTable
apProxDb8MetricTable = _ApProxDb8MetricTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 10)
)
if mibBuilder.loadTexts:
    apProxDb8MetricTable.setStatus("current")
_ApProxDb8MetricEntry_Object = MibTableRow
apProxDb8MetricEntry = _ApProxDb8MetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 10, 1)
)
apProxDb8MetricEntry.setIndexNames(
    (0, "PROXDBEXT-MIB", "apProx8MetricIpAddress"),
    (0, "PROXDBEXT-MIB", "apProx8MetricZoneIndex"),
)
if mibBuilder.loadTexts:
    apProxDb8MetricEntry.setStatus("current")
_ApProx8MetricIpAddress_Type = IpAddress
_ApProx8MetricIpAddress_Object = MibTableColumn
apProx8MetricIpAddress = _ApProx8MetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 10, 1, 1),
    _ApProx8MetricIpAddress_Type()
)
apProx8MetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx8MetricIpAddress.setStatus("current")


class _ApProx8MetricZoneIndex_Type(Integer32):
    """Custom type apProx8MetricZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ApProx8MetricZoneIndex_Type.__name__ = "Integer32"
_ApProx8MetricZoneIndex_Object = MibTableColumn
apProx8MetricZoneIndex = _ApProx8MetricZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 10, 1, 2),
    _ApProx8MetricZoneIndex_Type()
)
apProx8MetricZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx8MetricZoneIndex.setStatus("current")


class _ApProx8MetricValue_Type(Integer32):
    """Custom type apProx8MetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ApProx8MetricValue_Type.__name__ = "Integer32"
_ApProx8MetricValue_Object = MibTableColumn
apProx8MetricValue = _ApProx8MetricValue_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 10, 1, 3),
    _ApProx8MetricValue_Type()
)
apProx8MetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx8MetricValue.setStatus("current")
_ApProxDb16MetricTable_Object = MibTable
apProxDb16MetricTable = _ApProxDb16MetricTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 11)
)
if mibBuilder.loadTexts:
    apProxDb16MetricTable.setStatus("current")
_ApProxDb16MetricEntry_Object = MibTableRow
apProxDb16MetricEntry = _ApProxDb16MetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 11, 1)
)
apProxDb16MetricEntry.setIndexNames(
    (0, "PROXDBEXT-MIB", "apProx16MetricIpAddress"),
    (0, "PROXDBEXT-MIB", "apProx16MetricZoneIndex"),
)
if mibBuilder.loadTexts:
    apProxDb16MetricEntry.setStatus("current")
_ApProx16MetricIpAddress_Type = IpAddress
_ApProx16MetricIpAddress_Object = MibTableColumn
apProx16MetricIpAddress = _ApProx16MetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 11, 1, 1),
    _ApProx16MetricIpAddress_Type()
)
apProx16MetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx16MetricIpAddress.setStatus("current")


class _ApProx16MetricZoneIndex_Type(Integer32):
    """Custom type apProx16MetricZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ApProx16MetricZoneIndex_Type.__name__ = "Integer32"
_ApProx16MetricZoneIndex_Object = MibTableColumn
apProx16MetricZoneIndex = _ApProx16MetricZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 11, 1, 2),
    _ApProx16MetricZoneIndex_Type()
)
apProx16MetricZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx16MetricZoneIndex.setStatus("current")


class _ApProx16MetricValue_Type(Integer32):
    """Custom type apProx16MetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ApProx16MetricValue_Type.__name__ = "Integer32"
_ApProx16MetricValue_Object = MibTableColumn
apProx16MetricValue = _ApProx16MetricValue_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 11, 1, 3),
    _ApProx16MetricValue_Type()
)
apProx16MetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx16MetricValue.setStatus("current")
_ApProxDb24MetricTable_Object = MibTable
apProxDb24MetricTable = _ApProxDb24MetricTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 12)
)
if mibBuilder.loadTexts:
    apProxDb24MetricTable.setStatus("current")
_ApProxDb24MetricEntry_Object = MibTableRow
apProxDb24MetricEntry = _ApProxDb24MetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 12, 1)
)
apProxDb24MetricEntry.setIndexNames(
    (0, "PROXDBEXT-MIB", "apProx24MetricIpAddress"),
    (0, "PROXDBEXT-MIB", "apProx24MetricZoneIndex"),
)
if mibBuilder.loadTexts:
    apProxDb24MetricEntry.setStatus("current")
_ApProx24MetricIpAddress_Type = IpAddress
_ApProx24MetricIpAddress_Object = MibTableColumn
apProx24MetricIpAddress = _ApProx24MetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 12, 1, 1),
    _ApProx24MetricIpAddress_Type()
)
apProx24MetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx24MetricIpAddress.setStatus("current")


class _ApProx24MetricZoneIndex_Type(Integer32):
    """Custom type apProx24MetricZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ApProx24MetricZoneIndex_Type.__name__ = "Integer32"
_ApProx24MetricZoneIndex_Object = MibTableColumn
apProx24MetricZoneIndex = _ApProx24MetricZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 12, 1, 2),
    _ApProx24MetricZoneIndex_Type()
)
apProx24MetricZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx24MetricZoneIndex.setStatus("current")


class _ApProx24MetricValue_Type(Integer32):
    """Custom type apProx24MetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ApProx24MetricValue_Type.__name__ = "Integer32"
_ApProx24MetricValue_Object = MibTableColumn
apProx24MetricValue = _ApProx24MetricValue_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 12, 1, 3),
    _ApProx24MetricValue_Type()
)
apProx24MetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProx24MetricValue.setStatus("current")
_ApProxDbVplMetricTable_Object = MibTable
apProxDbVplMetricTable = _ApProxDbVplMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 13)
)
if mibBuilder.loadTexts:
    apProxDbVplMetricTable.setStatus("current")
_ApProxDbVplMetricEntry_Object = MibTableRow
apProxDbVplMetricEntry = _ApProxDbVplMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 13, 1)
)
apProxDbVplMetricEntry.setIndexNames(
    (0, "PROXDBEXT-MIB", "apProxVplMetricIpAddress"),
    (0, "PROXDBEXT-MIB", "apProxVplMetricIpPrefix"),
    (0, "PROXDBEXT-MIB", "apProxVplMetricZoneIndex"),
)
if mibBuilder.loadTexts:
    apProxDbVplMetricEntry.setStatus("current")
_ApProxVplMetricIpAddress_Type = IpAddress
_ApProxVplMetricIpAddress_Object = MibTableColumn
apProxVplMetricIpAddress = _ApProxVplMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 13, 1, 1),
    _ApProxVplMetricIpAddress_Type()
)
apProxVplMetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProxVplMetricIpAddress.setStatus("current")
_ApProxVplMetricIpPrefix_Type = Integer32
_ApProxVplMetricIpPrefix_Object = MibTableColumn
apProxVplMetricIpPrefix = _ApProxVplMetricIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 13, 1, 2),
    _ApProxVplMetricIpPrefix_Type()
)
apProxVplMetricIpPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProxVplMetricIpPrefix.setStatus("current")


class _ApProxVplMetricZoneIndex_Type(Integer32):
    """Custom type apProxVplMetricZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ApProxVplMetricZoneIndex_Type.__name__ = "Integer32"
_ApProxVplMetricZoneIndex_Object = MibTableColumn
apProxVplMetricZoneIndex = _ApProxVplMetricZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 13, 1, 3),
    _ApProxVplMetricZoneIndex_Type()
)
apProxVplMetricZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProxVplMetricZoneIndex.setStatus("current")


class _ApProxVplMetricValue_Type(Integer32):
    """Custom type apProxVplMetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ApProxVplMetricValue_Type.__name__ = "Integer32"
_ApProxVplMetricValue_Object = MibTableColumn
apProxVplMetricValue = _ApProxVplMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 54, 13, 1, 4),
    _ApProxVplMetricValue_Type()
)
apProxVplMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProxVplMetricValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROXDBEXT-MIB",
    **{"apProxDbExtMib": apProxDbExtMib,
       "apProxDbTTLProbed": apProxDbTTLProbed,
       "apProxDbTTLAssigned": apProxDbTTLAssigned,
       "apProxDb8StatTable": apProxDb8StatTable,
       "apProxDb8StatEntry": apProxDb8StatEntry,
       "apProx8StatIpAddress": apProx8StatIpAddress,
       "apProx8StatHitCount": apProx8StatHitCount,
       "apProx8StatAdvMask": apProx8StatAdvMask,
       "apProxDb16StatTable": apProxDb16StatTable,
       "apProxDb16StatEntry": apProxDb16StatEntry,
       "apProx16StatIpAddress": apProx16StatIpAddress,
       "apProx16StatHitCount": apProx16StatHitCount,
       "apProx16StatAdvMask": apProx16StatAdvMask,
       "apProxDb24StatTable": apProxDb24StatTable,
       "apProxDb24StatEntry": apProxDb24StatEntry,
       "apProx24StatIpAddress": apProx24StatIpAddress,
       "apProx24StatHitCount": apProx24StatHitCount,
       "apProx24StatAdvMask": apProx24StatAdvMask,
       "apProxDbVplStatTable": apProxDbVplStatTable,
       "apProxDbVplStatEntry": apProxDbVplStatEntry,
       "apProxVplStatIpAddress": apProxVplStatIpAddress,
       "apProxVplStatIpPrefix": apProxVplStatIpPrefix,
       "apProxVplStatHitCount": apProxVplStatHitCount,
       "apProxVplStatAdvMask": apProxVplStatAdvMask,
       "apProxDb8MetricTable": apProxDb8MetricTable,
       "apProxDb8MetricEntry": apProxDb8MetricEntry,
       "apProx8MetricIpAddress": apProx8MetricIpAddress,
       "apProx8MetricZoneIndex": apProx8MetricZoneIndex,
       "apProx8MetricValue": apProx8MetricValue,
       "apProxDb16MetricTable": apProxDb16MetricTable,
       "apProxDb16MetricEntry": apProxDb16MetricEntry,
       "apProx16MetricIpAddress": apProx16MetricIpAddress,
       "apProx16MetricZoneIndex": apProx16MetricZoneIndex,
       "apProx16MetricValue": apProx16MetricValue,
       "apProxDb24MetricTable": apProxDb24MetricTable,
       "apProxDb24MetricEntry": apProxDb24MetricEntry,
       "apProx24MetricIpAddress": apProx24MetricIpAddress,
       "apProx24MetricZoneIndex": apProx24MetricZoneIndex,
       "apProx24MetricValue": apProx24MetricValue,
       "apProxDbVplMetricTable": apProxDbVplMetricTable,
       "apProxDbVplMetricEntry": apProxDbVplMetricEntry,
       "apProxVplMetricIpAddress": apProxVplMetricIpAddress,
       "apProxVplMetricIpPrefix": apProxVplMetricIpPrefix,
       "apProxVplMetricZoneIndex": apProxVplMetricZoneIndex,
       "apProxVplMetricValue": apProxVplMetricValue}
)
