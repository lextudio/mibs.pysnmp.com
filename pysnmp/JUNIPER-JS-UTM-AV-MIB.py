# SNMP MIB module (JUNIPER-JS-UTM-AV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JS-UTM-AV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:22 2024
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

(jnxJsUTMRoot,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsUTMRoot")

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

jnxJsAntiVirus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1)
)
jnxJsAntiVirus.setRevisions(
        ("2011-02-08 08:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsAntiVirusTrapsPrefix_ObjectIdentity = ObjectIdentity
jnxJsAntiVirusTrapsPrefix = _JnxJsAntiVirusTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 0)
)
_JnxJsAntiVirusObjects_ObjectIdentity = ObjectIdentity
jnxJsAntiVirusObjects = _JnxJsAntiVirusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1)
)
_JnxJsAntiVirusEngine_ObjectIdentity = ObjectIdentity
jnxJsAntiVirusEngine = _JnxJsAntiVirusEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 1)
)


class _JnxJsAVEngineType_Type(Integer32):
    """Custom type jnxJsAVEngineType based on Integer32"""
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
        *(("juniper-express-engine", 3),
          ("kaspersky-lab-engine", 2),
          ("sophos-engine", 4),
          ("unknown-engine", 1))
    )


_JnxJsAVEngineType_Type.__name__ = "Integer32"
_JnxJsAVEngineType_Object = MibScalar
jnxJsAVEngineType = _JnxJsAVEngineType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 1, 1),
    _JnxJsAVEngineType_Type()
)
jnxJsAVEngineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVEngineType.setStatus("deprecated")


class _JnxJsAVCurrentPatternVersionString_Type(DisplayString):
    """Custom type jnxJsAVCurrentPatternVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxJsAVCurrentPatternVersionString_Type.__name__ = "DisplayString"
_JnxJsAVCurrentPatternVersionString_Object = MibScalar
jnxJsAVCurrentPatternVersionString = _JnxJsAVCurrentPatternVersionString_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 1, 2),
    _JnxJsAVCurrentPatternVersionString_Type()
)
jnxJsAVCurrentPatternVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVCurrentPatternVersionString.setStatus("deprecated")


class _JnxJsAVDatabaseType_Type(Integer32):
    """Custom type jnxJsAVDatabaseType based on Integer32"""
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
        *(("express", 2),
          ("full", 1),
          ("sophos", 4),
          ("unknown", 3))
    )


_JnxJsAVDatabaseType_Type.__name__ = "Integer32"
_JnxJsAVDatabaseType_Object = MibScalar
jnxJsAVDatabaseType = _JnxJsAVDatabaseType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 1, 3),
    _JnxJsAVDatabaseType_Type()
)
jnxJsAVDatabaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVDatabaseType.setStatus("deprecated")
_JnxJsAntiVirusStats_ObjectIdentity = ObjectIdentity
jnxJsAntiVirusStats = _JnxJsAntiVirusStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2)
)
_JnxJsAVScanCodeClean_Type = Integer32
_JnxJsAVScanCodeClean_Object = MibScalar
jnxJsAVScanCodeClean = _JnxJsAVScanCodeClean_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 1),
    _JnxJsAVScanCodeClean_Type()
)
jnxJsAVScanCodeClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeClean.setStatus("deprecated")
_JnxJsAVScanCodeInfected_Type = Integer32
_JnxJsAVScanCodeInfected_Object = MibScalar
jnxJsAVScanCodeInfected = _JnxJsAVScanCodeInfected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 2),
    _JnxJsAVScanCodeInfected_Type()
)
jnxJsAVScanCodeInfected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeInfected.setStatus("deprecated")
_JnxJsAVScanCodeProtected_Type = Integer32
_JnxJsAVScanCodeProtected_Object = MibScalar
jnxJsAVScanCodeProtected = _JnxJsAVScanCodeProtected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 3),
    _JnxJsAVScanCodeProtected_Type()
)
jnxJsAVScanCodeProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeProtected.setStatus("deprecated")
_JnxJsAVScanCodeDecompress_Type = Integer32
_JnxJsAVScanCodeDecompress_Object = MibScalar
jnxJsAVScanCodeDecompress = _JnxJsAVScanCodeDecompress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 4),
    _JnxJsAVScanCodeDecompress_Type()
)
jnxJsAVScanCodeDecompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeDecompress.setStatus("deprecated")
_JnxJsAVScanCodeCorrupted_Type = Integer32
_JnxJsAVScanCodeCorrupted_Object = MibScalar
jnxJsAVScanCodeCorrupted = _JnxJsAVScanCodeCorrupted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 5),
    _JnxJsAVScanCodeCorrupted_Type()
)
jnxJsAVScanCodeCorrupted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeCorrupted.setStatus("deprecated")
_JnxJsAVScanCodeNoResource_Type = Integer32
_JnxJsAVScanCodeNoResource_Object = MibScalar
jnxJsAVScanCodeNoResource = _JnxJsAVScanCodeNoResource_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 6),
    _JnxJsAVScanCodeNoResource_Type()
)
jnxJsAVScanCodeNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeNoResource.setStatus("deprecated")
_JnxJsAVScanCodeInternalError_Type = Integer32
_JnxJsAVScanCodeInternalError_Object = MibScalar
jnxJsAVScanCodeInternalError = _JnxJsAVScanCodeInternalError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 7),
    _JnxJsAVScanCodeInternalError_Type()
)
jnxJsAVScanCodeInternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeInternalError.setStatus("deprecated")
_JnxJsAVScanCodeMaxContentSize_Type = Integer32
_JnxJsAVScanCodeMaxContentSize_Object = MibScalar
jnxJsAVScanCodeMaxContentSize = _JnxJsAVScanCodeMaxContentSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 8),
    _JnxJsAVScanCodeMaxContentSize_Type()
)
jnxJsAVScanCodeMaxContentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeMaxContentSize.setStatus("deprecated")
_JnxJsAVScanCodeTooManyReq_Type = Integer32
_JnxJsAVScanCodeTooManyReq_Object = MibScalar
jnxJsAVScanCodeTooManyReq = _JnxJsAVScanCodeTooManyReq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 9),
    _JnxJsAVScanCodeTooManyReq_Type()
)
jnxJsAVScanCodeTooManyReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeTooManyReq.setStatus("deprecated")
_JnxJsAVScanCodeTimeout_Type = Integer32
_JnxJsAVScanCodeTimeout_Object = MibScalar
jnxJsAVScanCodeTimeout = _JnxJsAVScanCodeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 10),
    _JnxJsAVScanCodeTimeout_Type()
)
jnxJsAVScanCodeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeTimeout.setStatus("deprecated")
_JnxJsAVScanCodeEngineNotReady_Type = Integer32
_JnxJsAVScanCodeEngineNotReady_Object = MibScalar
jnxJsAVScanCodeEngineNotReady = _JnxJsAVScanCodeEngineNotReady_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 2, 11),
    _JnxJsAVScanCodeEngineNotReady_Type()
)
jnxJsAVScanCodeEngineNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsAVScanCodeEngineNotReady.setStatus("deprecated")
_JnxJsUTMAntiVirusEngine_Object = MibTable
jnxJsUTMAntiVirusEngine = _JnxJsUTMAntiVirusEngine_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxJsUTMAntiVirusEngine.setStatus("current")
_JnxJsUTMAntiVirusEngineEntry_Object = MibTableRow
jnxJsUTMAntiVirusEngineEntry = _JnxJsUTMAntiVirusEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 3, 1)
)
jnxJsUTMAntiVirusEngineEntry.setIndexNames(
    (0, "JUNIPER-JS-UTM-AV-MIB", "jnxJsUTMAVEngineIndex"),
)
if mibBuilder.loadTexts:
    jnxJsUTMAntiVirusEngineEntry.setStatus("current")


class _JnxJsUTMAVEngineIndex_Type(Integer32):
    """Custom type jnxJsUTMAVEngineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxJsUTMAVEngineIndex_Type.__name__ = "Integer32"
_JnxJsUTMAVEngineIndex_Object = MibTableColumn
jnxJsUTMAVEngineIndex = _JnxJsUTMAVEngineIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 3, 1, 1),
    _JnxJsUTMAVEngineIndex_Type()
)
jnxJsUTMAVEngineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsUTMAVEngineIndex.setStatus("current")


class _JnxJsUTMAVEngineType_Type(Integer32):
    """Custom type jnxJsUTMAVEngineType based on Integer32"""
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
        *(("juniper-express-engine", 3),
          ("kaspersky-lab-engine", 2),
          ("sophos-engine", 4),
          ("unknown-engine", 1))
    )


_JnxJsUTMAVEngineType_Type.__name__ = "Integer32"
_JnxJsUTMAVEngineType_Object = MibTableColumn
jnxJsUTMAVEngineType = _JnxJsUTMAVEngineType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 3, 1, 2),
    _JnxJsUTMAVEngineType_Type()
)
jnxJsUTMAVEngineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVEngineType.setStatus("current")


class _JnxJsUTMAVPatternVersionString_Type(DisplayString):
    """Custom type jnxJsUTMAVPatternVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxJsUTMAVPatternVersionString_Type.__name__ = "DisplayString"
_JnxJsUTMAVPatternVersionString_Object = MibTableColumn
jnxJsUTMAVPatternVersionString = _JnxJsUTMAVPatternVersionString_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 3, 1, 3),
    _JnxJsUTMAVPatternVersionString_Type()
)
jnxJsUTMAVPatternVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVPatternVersionString.setStatus("current")


class _JnxJsUTMAVDatabaseType_Type(Integer32):
    """Custom type jnxJsUTMAVDatabaseType based on Integer32"""
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
        *(("express", 2),
          ("full", 1),
          ("sophos", 4),
          ("unknown", 3))
    )


_JnxJsUTMAVDatabaseType_Type.__name__ = "Integer32"
_JnxJsUTMAVDatabaseType_Object = MibTableColumn
jnxJsUTMAVDatabaseType = _JnxJsUTMAVDatabaseType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 3, 1, 4),
    _JnxJsUTMAVDatabaseType_Type()
)
jnxJsUTMAVDatabaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVDatabaseType.setStatus("current")
_JnxJsUTMAntiVirusStats_Object = MibTable
jnxJsUTMAntiVirusStats = _JnxJsUTMAntiVirusStats_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxJsUTMAntiVirusStats.setStatus("current")
_JnxJsUTMAntiVirusStatsEntry_Object = MibTableRow
jnxJsUTMAntiVirusStatsEntry = _JnxJsUTMAntiVirusStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1)
)
jnxJsUTMAntiVirusStatsEntry.setIndexNames(
    (0, "JUNIPER-JS-UTM-AV-MIB", "jnxJsUTMAVStatsIndex"),
)
if mibBuilder.loadTexts:
    jnxJsUTMAntiVirusStatsEntry.setStatus("current")


class _JnxJsUTMAVStatsIndex_Type(Integer32):
    """Custom type jnxJsUTMAVStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxJsUTMAVStatsIndex_Type.__name__ = "Integer32"
_JnxJsUTMAVStatsIndex_Object = MibTableColumn
jnxJsUTMAVStatsIndex = _JnxJsUTMAVStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 1),
    _JnxJsUTMAVStatsIndex_Type()
)
jnxJsUTMAVStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsUTMAVStatsIndex.setStatus("current")
_JnxJsUTMAVScanCodeClean_Type = Integer32
_JnxJsUTMAVScanCodeClean_Object = MibTableColumn
jnxJsUTMAVScanCodeClean = _JnxJsUTMAVScanCodeClean_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 2),
    _JnxJsUTMAVScanCodeClean_Type()
)
jnxJsUTMAVScanCodeClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeClean.setStatus("current")
_JnxJsUTMAVScanCodeInfected_Type = Integer32
_JnxJsUTMAVScanCodeInfected_Object = MibTableColumn
jnxJsUTMAVScanCodeInfected = _JnxJsUTMAVScanCodeInfected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 3),
    _JnxJsUTMAVScanCodeInfected_Type()
)
jnxJsUTMAVScanCodeInfected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeInfected.setStatus("current")
_JnxJsUTMAVScanCodeProtected_Type = Integer32
_JnxJsUTMAVScanCodeProtected_Object = MibTableColumn
jnxJsUTMAVScanCodeProtected = _JnxJsUTMAVScanCodeProtected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 4),
    _JnxJsUTMAVScanCodeProtected_Type()
)
jnxJsUTMAVScanCodeProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeProtected.setStatus("current")
_JnxJsUTMAVScanCodeDecompress_Type = Integer32
_JnxJsUTMAVScanCodeDecompress_Object = MibTableColumn
jnxJsUTMAVScanCodeDecompress = _JnxJsUTMAVScanCodeDecompress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 5),
    _JnxJsUTMAVScanCodeDecompress_Type()
)
jnxJsUTMAVScanCodeDecompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeDecompress.setStatus("current")
_JnxJsUTMAVScanCodeCorrupted_Type = Integer32
_JnxJsUTMAVScanCodeCorrupted_Object = MibTableColumn
jnxJsUTMAVScanCodeCorrupted = _JnxJsUTMAVScanCodeCorrupted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 6),
    _JnxJsUTMAVScanCodeCorrupted_Type()
)
jnxJsUTMAVScanCodeCorrupted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeCorrupted.setStatus("current")
_JnxJsUTMAVScanCodeNoResource_Type = Integer32
_JnxJsUTMAVScanCodeNoResource_Object = MibTableColumn
jnxJsUTMAVScanCodeNoResource = _JnxJsUTMAVScanCodeNoResource_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 7),
    _JnxJsUTMAVScanCodeNoResource_Type()
)
jnxJsUTMAVScanCodeNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeNoResource.setStatus("current")
_JnxJsUTMAVScanCodeInternalError_Type = Integer32
_JnxJsUTMAVScanCodeInternalError_Object = MibTableColumn
jnxJsUTMAVScanCodeInternalError = _JnxJsUTMAVScanCodeInternalError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 8),
    _JnxJsUTMAVScanCodeInternalError_Type()
)
jnxJsUTMAVScanCodeInternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeInternalError.setStatus("current")
_JnxJsUTMAVScanCodeMaxContentSize_Type = Integer32
_JnxJsUTMAVScanCodeMaxContentSize_Object = MibTableColumn
jnxJsUTMAVScanCodeMaxContentSize = _JnxJsUTMAVScanCodeMaxContentSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 9),
    _JnxJsUTMAVScanCodeMaxContentSize_Type()
)
jnxJsUTMAVScanCodeMaxContentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeMaxContentSize.setStatus("current")
_JnxJsUTMAVScanCodeTooManyReq_Type = Integer32
_JnxJsUTMAVScanCodeTooManyReq_Object = MibTableColumn
jnxJsUTMAVScanCodeTooManyReq = _JnxJsUTMAVScanCodeTooManyReq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 10),
    _JnxJsUTMAVScanCodeTooManyReq_Type()
)
jnxJsUTMAVScanCodeTooManyReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeTooManyReq.setStatus("current")
_JnxJsUTMAVScanCodeTimeout_Type = Integer32
_JnxJsUTMAVScanCodeTimeout_Object = MibTableColumn
jnxJsUTMAVScanCodeTimeout = _JnxJsUTMAVScanCodeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 11),
    _JnxJsUTMAVScanCodeTimeout_Type()
)
jnxJsUTMAVScanCodeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeTimeout.setStatus("current")
_JnxJsUTMAVScanCodeEngineNotReady_Type = Integer32
_JnxJsUTMAVScanCodeEngineNotReady_Object = MibTableColumn
jnxJsUTMAVScanCodeEngineNotReady = _JnxJsUTMAVScanCodeEngineNotReady_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 1, 4, 1, 12),
    _JnxJsUTMAVScanCodeEngineNotReady_Type()
)
jnxJsUTMAVScanCodeEngineNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsUTMAVScanCodeEngineNotReady.setStatus("current")
_JnxJsAntiVirusTraps_ObjectIdentity = ObjectIdentity
jnxJsAntiVirusTraps = _JnxJsAntiVirusTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 2)
)
_JnxJsAntiVirusTrapVars_ObjectIdentity = ObjectIdentity
jnxJsAntiVirusTrapVars = _JnxJsAntiVirusTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 3)
)


class _JnxAVPatternVersionString_Type(DisplayString):
    """Custom type jnxAVPatternVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxAVPatternVersionString_Type.__name__ = "DisplayString"
_JnxAVPatternVersionString_Object = MibScalar
jnxAVPatternVersionString = _JnxAVPatternVersionString_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 3, 1),
    _JnxAVPatternVersionString_Type()
)
jnxAVPatternVersionString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxAVPatternVersionString.setStatus("current")


class _JnxAVPatternTimestamp_Type(DisplayString):
    """Custom type jnxAVPatternTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxAVPatternTimestamp_Type.__name__ = "DisplayString"
_JnxAVPatternTimestamp_Object = MibScalar
jnxAVPatternTimestamp = _JnxAVPatternTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 3, 2),
    _JnxAVPatternTimestamp_Type()
)
jnxAVPatternTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxAVPatternTimestamp.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsAvPatternUpdateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13, 1, 0, 1)
)
jnxJsAvPatternUpdateTrap.setObjects(
      *(("JUNIPER-JS-UTM-AV-MIB", "jnxAVPatternVersionString"),
        ("JUNIPER-JS-UTM-AV-MIB", "jnxAVPatternTimestamp"))
)
if mibBuilder.loadTexts:
    jnxJsAvPatternUpdateTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-UTM-AV-MIB",
    **{"jnxJsAntiVirus": jnxJsAntiVirus,
       "jnxJsAntiVirusTrapsPrefix": jnxJsAntiVirusTrapsPrefix,
       "jnxJsAvPatternUpdateTrap": jnxJsAvPatternUpdateTrap,
       "jnxJsAntiVirusObjects": jnxJsAntiVirusObjects,
       "jnxJsAntiVirusEngine": jnxJsAntiVirusEngine,
       "jnxJsAVEngineType": jnxJsAVEngineType,
       "jnxJsAVCurrentPatternVersionString": jnxJsAVCurrentPatternVersionString,
       "jnxJsAVDatabaseType": jnxJsAVDatabaseType,
       "jnxJsAntiVirusStats": jnxJsAntiVirusStats,
       "jnxJsAVScanCodeClean": jnxJsAVScanCodeClean,
       "jnxJsAVScanCodeInfected": jnxJsAVScanCodeInfected,
       "jnxJsAVScanCodeProtected": jnxJsAVScanCodeProtected,
       "jnxJsAVScanCodeDecompress": jnxJsAVScanCodeDecompress,
       "jnxJsAVScanCodeCorrupted": jnxJsAVScanCodeCorrupted,
       "jnxJsAVScanCodeNoResource": jnxJsAVScanCodeNoResource,
       "jnxJsAVScanCodeInternalError": jnxJsAVScanCodeInternalError,
       "jnxJsAVScanCodeMaxContentSize": jnxJsAVScanCodeMaxContentSize,
       "jnxJsAVScanCodeTooManyReq": jnxJsAVScanCodeTooManyReq,
       "jnxJsAVScanCodeTimeout": jnxJsAVScanCodeTimeout,
       "jnxJsAVScanCodeEngineNotReady": jnxJsAVScanCodeEngineNotReady,
       "jnxJsUTMAntiVirusEngine": jnxJsUTMAntiVirusEngine,
       "jnxJsUTMAntiVirusEngineEntry": jnxJsUTMAntiVirusEngineEntry,
       "jnxJsUTMAVEngineIndex": jnxJsUTMAVEngineIndex,
       "jnxJsUTMAVEngineType": jnxJsUTMAVEngineType,
       "jnxJsUTMAVPatternVersionString": jnxJsUTMAVPatternVersionString,
       "jnxJsUTMAVDatabaseType": jnxJsUTMAVDatabaseType,
       "jnxJsUTMAntiVirusStats": jnxJsUTMAntiVirusStats,
       "jnxJsUTMAntiVirusStatsEntry": jnxJsUTMAntiVirusStatsEntry,
       "jnxJsUTMAVStatsIndex": jnxJsUTMAVStatsIndex,
       "jnxJsUTMAVScanCodeClean": jnxJsUTMAVScanCodeClean,
       "jnxJsUTMAVScanCodeInfected": jnxJsUTMAVScanCodeInfected,
       "jnxJsUTMAVScanCodeProtected": jnxJsUTMAVScanCodeProtected,
       "jnxJsUTMAVScanCodeDecompress": jnxJsUTMAVScanCodeDecompress,
       "jnxJsUTMAVScanCodeCorrupted": jnxJsUTMAVScanCodeCorrupted,
       "jnxJsUTMAVScanCodeNoResource": jnxJsUTMAVScanCodeNoResource,
       "jnxJsUTMAVScanCodeInternalError": jnxJsUTMAVScanCodeInternalError,
       "jnxJsUTMAVScanCodeMaxContentSize": jnxJsUTMAVScanCodeMaxContentSize,
       "jnxJsUTMAVScanCodeTooManyReq": jnxJsUTMAVScanCodeTooManyReq,
       "jnxJsUTMAVScanCodeTimeout": jnxJsUTMAVScanCodeTimeout,
       "jnxJsUTMAVScanCodeEngineNotReady": jnxJsUTMAVScanCodeEngineNotReady,
       "jnxJsAntiVirusTraps": jnxJsAntiVirusTraps,
       "jnxJsAntiVirusTrapVars": jnxJsAntiVirusTrapVars,
       "jnxAVPatternVersionString": jnxAVPatternVersionString,
       "jnxAVPatternTimestamp": jnxAVPatternTimestamp}
)
