# SNMP MIB module (ENTERASYS-TWCB-MIB-2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-TWCB-MIB-2
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:40 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InetAddress,
 InetAddressType,
 InetPortNumber,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber",
    "InetVersion")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysTWCBMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76)
)
etsysTWCBMIB.setRevisions(
        ("2010-08-17 12:15",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysTwcbGlobal_ObjectIdentity = ObjectIdentity
etsysTwcbGlobal = _EtsysTwcbGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1)
)
_EtsysTwcbGlobalStats_ObjectIdentity = ObjectIdentity
etsysTwcbGlobalStats = _EtsysTwcbGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1)
)
_EtsysTwcbStatsCachesUsed_Type = Gauge32
_EtsysTwcbStatsCachesUsed_Object = MibScalar
etsysTwcbStatsCachesUsed = _EtsysTwcbStatsCachesUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 1),
    _EtsysTwcbStatsCachesUsed_Type()
)
etsysTwcbStatsCachesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsCachesUsed.setStatus("current")
_EtsysTwcbStatsWcServerfarmsUsed_Type = Gauge32
_EtsysTwcbStatsWcServerfarmsUsed_Object = MibScalar
etsysTwcbStatsWcServerfarmsUsed = _EtsysTwcbStatsWcServerfarmsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 2),
    _EtsysTwcbStatsWcServerfarmsUsed_Type()
)
etsysTwcbStatsWcServerfarmsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsWcServerfarmsUsed.setStatus("current")
_EtsysTwcbStatsWebcacheUsed_Type = Gauge32
_EtsysTwcbStatsWebcacheUsed_Object = MibScalar
etsysTwcbStatsWebcacheUsed = _EtsysTwcbStatsWebcacheUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 3),
    _EtsysTwcbStatsWebcacheUsed_Type()
)
etsysTwcbStatsWebcacheUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsWebcacheUsed.setStatus("current")
_EtsysTwcbStatsBindingsCurrent_Type = Gauge32
_EtsysTwcbStatsBindingsCurrent_Object = MibScalar
etsysTwcbStatsBindingsCurrent = _EtsysTwcbStatsBindingsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 4),
    _EtsysTwcbStatsBindingsCurrent_Type()
)
etsysTwcbStatsBindingsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsBindingsCurrent.setStatus("current")
_EtsysTwcbStatsBindingsHigh_Type = Gauge32
_EtsysTwcbStatsBindingsHigh_Object = MibScalar
etsysTwcbStatsBindingsHigh = _EtsysTwcbStatsBindingsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 5),
    _EtsysTwcbStatsBindingsHigh_Type()
)
etsysTwcbStatsBindingsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsBindingsHigh.setStatus("current")
_EtsysTwcbStatsBindingsDeleted_Type = Counter32
_EtsysTwcbStatsBindingsDeleted_Object = MibScalar
etsysTwcbStatsBindingsDeleted = _EtsysTwcbStatsBindingsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 6),
    _EtsysTwcbStatsBindingsDeleted_Type()
)
etsysTwcbStatsBindingsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsBindingsDeleted.setStatus("current")
_EtsysTwcbStatsBindingsTotal_Type = Counter32
_EtsysTwcbStatsBindingsTotal_Object = MibScalar
etsysTwcbStatsBindingsTotal = _EtsysTwcbStatsBindingsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 7),
    _EtsysTwcbStatsBindingsTotal_Type()
)
etsysTwcbStatsBindingsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsBindingsTotal.setStatus("current")
_EtsysTwcbStatsBindingsExhausted_Type = Counter32
_EtsysTwcbStatsBindingsExhausted_Object = MibScalar
etsysTwcbStatsBindingsExhausted = _EtsysTwcbStatsBindingsExhausted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 8),
    _EtsysTwcbStatsBindingsExhausted_Type()
)
etsysTwcbStatsBindingsExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsBindingsExhausted.setStatus("current")
_EtsysTwcbStatsBindingsNoCaches_Type = Counter32
_EtsysTwcbStatsBindingsNoCaches_Object = MibScalar
etsysTwcbStatsBindingsNoCaches = _EtsysTwcbStatsBindingsNoCaches_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 9),
    _EtsysTwcbStatsBindingsNoCaches_Type()
)
etsysTwcbStatsBindingsNoCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsBindingsNoCaches.setStatus("current")
_EtsysTwcbStatsBindingsPerSecond_Type = Gauge32
_EtsysTwcbStatsBindingsPerSecond_Object = MibScalar
etsysTwcbStatsBindingsPerSecond = _EtsysTwcbStatsBindingsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 10),
    _EtsysTwcbStatsBindingsPerSecond_Type()
)
etsysTwcbStatsBindingsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsBindingsPerSecond.setStatus("current")
_EtsysTwcbStatsWebcacheActive_Type = Gauge32
_EtsysTwcbStatsWebcacheActive_Object = MibScalar
etsysTwcbStatsWebcacheActive = _EtsysTwcbStatsWebcacheActive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 11),
    _EtsysTwcbStatsWebcacheActive_Type()
)
etsysTwcbStatsWebcacheActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsWebcacheActive.setStatus("current")
_EtsysTwcbStatsWebcacheHigh_Type = Gauge32
_EtsysTwcbStatsWebcacheHigh_Object = MibScalar
etsysTwcbStatsWebcacheHigh = _EtsysTwcbStatsWebcacheHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 12),
    _EtsysTwcbStatsWebcacheHigh_Type()
)
etsysTwcbStatsWebcacheHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsWebcacheHigh.setStatus("current")
_EtsysTwcbStatsWcServerfarmActive_Type = Gauge32
_EtsysTwcbStatsWcServerfarmActive_Object = MibScalar
etsysTwcbStatsWcServerfarmActive = _EtsysTwcbStatsWcServerfarmActive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 13),
    _EtsysTwcbStatsWcServerfarmActive_Type()
)
etsysTwcbStatsWcServerfarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsWcServerfarmActive.setStatus("current")
_EtsysTwcbStatsWcServerfarmHigh_Type = Gauge32
_EtsysTwcbStatsWcServerfarmHigh_Object = MibScalar
etsysTwcbStatsWcServerfarmHigh = _EtsysTwcbStatsWcServerfarmHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 14),
    _EtsysTwcbStatsWcServerfarmHigh_Type()
)
etsysTwcbStatsWcServerfarmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsWcServerfarmHigh.setStatus("current")
_EtsysTwcbStatsCacheActive_Type = Gauge32
_EtsysTwcbStatsCacheActive_Object = MibScalar
etsysTwcbStatsCacheActive = _EtsysTwcbStatsCacheActive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 15),
    _EtsysTwcbStatsCacheActive_Type()
)
etsysTwcbStatsCacheActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsCacheActive.setStatus("current")
_EtsysTwcbStatsCacheHigh_Type = Gauge32
_EtsysTwcbStatsCacheHigh_Object = MibScalar
etsysTwcbStatsCacheHigh = _EtsysTwcbStatsCacheHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 16),
    _EtsysTwcbStatsCacheHigh_Type()
)
etsysTwcbStatsCacheHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsCacheHigh.setStatus("current")


class _EtsysTwcbStatsClear_Type(TruthValue):
    """Custom type etsysTwcbStatsClear based on TruthValue"""


_EtsysTwcbStatsClear_Object = MibScalar
etsysTwcbStatsClear = _EtsysTwcbStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 17),
    _EtsysTwcbStatsClear_Type()
)
etsysTwcbStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTwcbStatsClear.setStatus("current")
_EtsysTwcbStatsClearDateAndTime_Type = DateAndTime
_EtsysTwcbStatsClearDateAndTime_Object = MibScalar
etsysTwcbStatsClearDateAndTime = _EtsysTwcbStatsClearDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 18),
    _EtsysTwcbStatsClearDateAndTime_Type()
)
etsysTwcbStatsClearDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsClearDateAndTime.setStatus("current")
_EtsysTwcbStatsMinTimeoutValue_Type = Unsigned32
_EtsysTwcbStatsMinTimeoutValue_Object = MibScalar
etsysTwcbStatsMinTimeoutValue = _EtsysTwcbStatsMinTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 19),
    _EtsysTwcbStatsMinTimeoutValue_Type()
)
etsysTwcbStatsMinTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsMinTimeoutValue.setStatus("current")
if mibBuilder.loadTexts:
    etsysTwcbStatsMinTimeoutValue.setUnits("seconds")
_EtsysTwcbStatsMaxTimeoutValue_Type = Unsigned32
_EtsysTwcbStatsMaxTimeoutValue_Object = MibScalar
etsysTwcbStatsMaxTimeoutValue = _EtsysTwcbStatsMaxTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 1, 1, 20),
    _EtsysTwcbStatsMaxTimeoutValue_Type()
)
etsysTwcbStatsMaxTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbStatsMaxTimeoutValue.setStatus("current")
if mibBuilder.loadTexts:
    etsysTwcbStatsMaxTimeoutValue.setUnits("seconds")
_EtsysTwcbTables_ObjectIdentity = ObjectIdentity
etsysTwcbTables = _EtsysTwcbTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2)
)
_EtsysTwcbWcServerfarmTable_Object = MibTable
etsysTwcbWcServerfarmTable = _EtsysTwcbWcServerfarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1)
)
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmTable.setStatus("current")
_EtsysTwcbWcServerfarmEntry_Object = MibTableRow
etsysTwcbWcServerfarmEntry = _EtsysTwcbWcServerfarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1)
)
etsysTwcbWcServerfarmEntry.setIndexNames(
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmInetVersion"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmName"),
)
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmEntry.setStatus("current")
_EtsysTwcbWcServerfarmInetVersion_Type = InetVersion
_EtsysTwcbWcServerfarmInetVersion_Object = MibTableColumn
etsysTwcbWcServerfarmInetVersion = _EtsysTwcbWcServerfarmInetVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 1),
    _EtsysTwcbWcServerfarmInetVersion_Type()
)
etsysTwcbWcServerfarmInetVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmInetVersion.setStatus("current")


class _EtsysTwcbWcServerfarmName_Type(SnmpAdminString):
    """Custom type etsysTwcbWcServerfarmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysTwcbWcServerfarmName_Type.__name__ = "SnmpAdminString"
_EtsysTwcbWcServerfarmName_Object = MibTableColumn
etsysTwcbWcServerfarmName = _EtsysTwcbWcServerfarmName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 2),
    _EtsysTwcbWcServerfarmName_Type()
)
etsysTwcbWcServerfarmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmName.setStatus("current")


class _EtsysTwcbWcServerfarmPredictor_Type(Integer32):
    """Custom type etsysTwcbWcServerfarmPredictor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destIpHash", 1),
          ("roundrobin", 2))
    )


_EtsysTwcbWcServerfarmPredictor_Type.__name__ = "Integer32"
_EtsysTwcbWcServerfarmPredictor_Object = MibTableColumn
etsysTwcbWcServerfarmPredictor = _EtsysTwcbWcServerfarmPredictor_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 3),
    _EtsysTwcbWcServerfarmPredictor_Type()
)
etsysTwcbWcServerfarmPredictor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmPredictor.setStatus("current")


class _EtsysTwcbWcServerfarmAdminStatus_Type(Integer32):
    """Custom type etsysTwcbWcServerfarmAdminStatus based on Integer32"""
    defaultValue = 2

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


_EtsysTwcbWcServerfarmAdminStatus_Type.__name__ = "Integer32"
_EtsysTwcbWcServerfarmAdminStatus_Object = MibTableColumn
etsysTwcbWcServerfarmAdminStatus = _EtsysTwcbWcServerfarmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 4),
    _EtsysTwcbWcServerfarmAdminStatus_Type()
)
etsysTwcbWcServerfarmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmAdminStatus.setStatus("current")


class _EtsysTwcbWcServerfarmOperStatus_Type(Integer32):
    """Custom type etsysTwcbWcServerfarmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EtsysTwcbWcServerfarmOperStatus_Type.__name__ = "Integer32"
_EtsysTwcbWcServerfarmOperStatus_Object = MibTableColumn
etsysTwcbWcServerfarmOperStatus = _EtsysTwcbWcServerfarmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 5),
    _EtsysTwcbWcServerfarmOperStatus_Type()
)
etsysTwcbWcServerfarmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmOperStatus.setStatus("current")
_EtsysTwcbWcServerfarmConns_Type = Gauge32
_EtsysTwcbWcServerfarmConns_Object = MibTableColumn
etsysTwcbWcServerfarmConns = _EtsysTwcbWcServerfarmConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 6),
    _EtsysTwcbWcServerfarmConns_Type()
)
etsysTwcbWcServerfarmConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmConns.setStatus("current")
_EtsysTwcbWcServerfarmHits_Type = Counter32
_EtsysTwcbWcServerfarmHits_Object = MibTableColumn
etsysTwcbWcServerfarmHits = _EtsysTwcbWcServerfarmHits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 7),
    _EtsysTwcbWcServerfarmHits_Type()
)
etsysTwcbWcServerfarmHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmHits.setStatus("current")
_EtsysTwcbWcServerfarmStateChanges_Type = Counter32
_EtsysTwcbWcServerfarmStateChanges_Object = MibTableColumn
etsysTwcbWcServerfarmStateChanges = _EtsysTwcbWcServerfarmStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 8),
    _EtsysTwcbWcServerfarmStateChanges_Type()
)
etsysTwcbWcServerfarmStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmStateChanges.setStatus("current")
_EtsysTwcbWcServerfarmLastStateChangeDateAndTime_Type = DateAndTime
_EtsysTwcbWcServerfarmLastStateChangeDateAndTime_Object = MibTableColumn
etsysTwcbWcServerfarmLastStateChangeDateAndTime = _EtsysTwcbWcServerfarmLastStateChangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 9),
    _EtsysTwcbWcServerfarmLastStateChangeDateAndTime_Type()
)
etsysTwcbWcServerfarmLastStateChangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmLastStateChangeDateAndTime.setStatus("current")
_EtsysTwcbWcServerfarmCachesCfg_Type = Gauge32
_EtsysTwcbWcServerfarmCachesCfg_Object = MibTableColumn
etsysTwcbWcServerfarmCachesCfg = _EtsysTwcbWcServerfarmCachesCfg_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 10),
    _EtsysTwcbWcServerfarmCachesCfg_Type()
)
etsysTwcbWcServerfarmCachesCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmCachesCfg.setStatus("current")
_EtsysTwcbWcServerfarmCachesUp_Type = Gauge32
_EtsysTwcbWcServerfarmCachesUp_Object = MibTableColumn
etsysTwcbWcServerfarmCachesUp = _EtsysTwcbWcServerfarmCachesUp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 11),
    _EtsysTwcbWcServerfarmCachesUp_Type()
)
etsysTwcbWcServerfarmCachesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmCachesUp.setStatus("current")
_EtsysTwcbWcServerfarmWebcacheCfg_Type = Gauge32
_EtsysTwcbWcServerfarmWebcacheCfg_Object = MibTableColumn
etsysTwcbWcServerfarmWebcacheCfg = _EtsysTwcbWcServerfarmWebcacheCfg_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 12),
    _EtsysTwcbWcServerfarmWebcacheCfg_Type()
)
etsysTwcbWcServerfarmWebcacheCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmWebcacheCfg.setStatus("current")
_EtsysTwcbWcServerfarmRoundRobinCount_Type = Counter32
_EtsysTwcbWcServerfarmRoundRobinCount_Object = MibTableColumn
etsysTwcbWcServerfarmRoundRobinCount = _EtsysTwcbWcServerfarmRoundRobinCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 13),
    _EtsysTwcbWcServerfarmRoundRobinCount_Type()
)
etsysTwcbWcServerfarmRoundRobinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmRoundRobinCount.setStatus("current")
_EtsysTwcbWcServerfarmRowStatus_Type = RowStatus
_EtsysTwcbWcServerfarmRowStatus_Object = MibTableColumn
etsysTwcbWcServerfarmRowStatus = _EtsysTwcbWcServerfarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 14),
    _EtsysTwcbWcServerfarmRowStatus_Type()
)
etsysTwcbWcServerfarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmRowStatus.setStatus("current")
_EtsysTwcbWcServerfarmId_Type = Unsigned32
_EtsysTwcbWcServerfarmId_Object = MibTableColumn
etsysTwcbWcServerfarmId = _EtsysTwcbWcServerfarmId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 1, 1, 15),
    _EtsysTwcbWcServerfarmId_Type()
)
etsysTwcbWcServerfarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWcServerfarmId.setStatus("current")
_EtsysTwcbWcSfarmRoundRobinTable_Object = MibTable
etsysTwcbWcSfarmRoundRobinTable = _EtsysTwcbWcSfarmRoundRobinTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 2)
)
if mibBuilder.loadTexts:
    etsysTwcbWcSfarmRoundRobinTable.setStatus("current")
_EtsysTwcbWcSfarmRoundRobinEntry_Object = MibTableRow
etsysTwcbWcSfarmRoundRobinEntry = _EtsysTwcbWcSfarmRoundRobinEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 2, 1)
)
etsysTwcbWcSfarmRoundRobinEntry.setIndexNames(
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWcSfarmRoundRobinAddressType"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmName"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWcSfarmRoundRobinStartIp"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWcSfarmRoundRobinEndIp"),
)
if mibBuilder.loadTexts:
    etsysTwcbWcSfarmRoundRobinEntry.setStatus("current")
_EtsysTwcbWcSfarmRoundRobinAddressType_Type = InetAddressType
_EtsysTwcbWcSfarmRoundRobinAddressType_Object = MibTableColumn
etsysTwcbWcSfarmRoundRobinAddressType = _EtsysTwcbWcSfarmRoundRobinAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 2, 1, 1),
    _EtsysTwcbWcSfarmRoundRobinAddressType_Type()
)
etsysTwcbWcSfarmRoundRobinAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWcSfarmRoundRobinAddressType.setStatus("current")
_EtsysTwcbWcSfarmRoundRobinStartIp_Type = InetAddress
_EtsysTwcbWcSfarmRoundRobinStartIp_Object = MibTableColumn
etsysTwcbWcSfarmRoundRobinStartIp = _EtsysTwcbWcSfarmRoundRobinStartIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 2, 1, 2),
    _EtsysTwcbWcSfarmRoundRobinStartIp_Type()
)
etsysTwcbWcSfarmRoundRobinStartIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWcSfarmRoundRobinStartIp.setStatus("current")
_EtsysTwcbWcSfarmRoundRobinEndIp_Type = InetAddress
_EtsysTwcbWcSfarmRoundRobinEndIp_Object = MibTableColumn
etsysTwcbWcSfarmRoundRobinEndIp = _EtsysTwcbWcSfarmRoundRobinEndIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 2, 1, 3),
    _EtsysTwcbWcSfarmRoundRobinEndIp_Type()
)
etsysTwcbWcSfarmRoundRobinEndIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWcSfarmRoundRobinEndIp.setStatus("current")
_EtsysTwcbWcSfarmRoundRobinRowStatus_Type = RowStatus
_EtsysTwcbWcSfarmRoundRobinRowStatus_Object = MibTableColumn
etsysTwcbWcSfarmRoundRobinRowStatus = _EtsysTwcbWcSfarmRoundRobinRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 2, 1, 4),
    _EtsysTwcbWcSfarmRoundRobinRowStatus_Type()
)
etsysTwcbWcSfarmRoundRobinRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWcSfarmRoundRobinRowStatus.setStatus("current")
_EtsysTwcbCacheServerTable_Object = MibTable
etsysTwcbCacheServerTable = _EtsysTwcbCacheServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3)
)
if mibBuilder.loadTexts:
    etsysTwcbCacheServerTable.setStatus("current")
_EtsysTwcbCacheServerEntry_Object = MibTableRow
etsysTwcbCacheServerEntry = _EtsysTwcbCacheServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1)
)
etsysTwcbCacheServerEntry.setIndexNames(
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerAddressType"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmName"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerIp"),
)
if mibBuilder.loadTexts:
    etsysTwcbCacheServerEntry.setStatus("current")
_EtsysTwcbCacheServerAddressType_Type = InetAddressType
_EtsysTwcbCacheServerAddressType_Object = MibTableColumn
etsysTwcbCacheServerAddressType = _EtsysTwcbCacheServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 1),
    _EtsysTwcbCacheServerAddressType_Type()
)
etsysTwcbCacheServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerAddressType.setStatus("current")
_EtsysTwcbCacheServerIp_Type = InetAddress
_EtsysTwcbCacheServerIp_Object = MibTableColumn
etsysTwcbCacheServerIp = _EtsysTwcbCacheServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 2),
    _EtsysTwcbCacheServerIp_Type()
)
etsysTwcbCacheServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerIp.setStatus("current")


class _EtsysTwcbCacheServerWeight_Type(Unsigned32):
    """Custom type etsysTwcbCacheServerWeight based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155),
    )


_EtsysTwcbCacheServerWeight_Type.__name__ = "Unsigned32"
_EtsysTwcbCacheServerWeight_Object = MibTableColumn
etsysTwcbCacheServerWeight = _EtsysTwcbCacheServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 3),
    _EtsysTwcbCacheServerWeight_Type()
)
etsysTwcbCacheServerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerWeight.setStatus("current")


class _EtsysTwcbCacheServerMaxConns_Type(Unsigned32):
    """Custom type etsysTwcbCacheServerMaxConns based on Unsigned32"""
    defaultValue = 0


_EtsysTwcbCacheServerMaxConns_Object = MibTableColumn
etsysTwcbCacheServerMaxConns = _EtsysTwcbCacheServerMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 4),
    _EtsysTwcbCacheServerMaxConns_Type()
)
etsysTwcbCacheServerMaxConns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerMaxConns.setStatus("current")


class _EtsysTwcbCacheServerFailDetectType_Type(Integer32):
    """Custom type etsysTwcbCacheServerFailDetectType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("probe", 2))
    )


_EtsysTwcbCacheServerFailDetectType_Type.__name__ = "Integer32"
_EtsysTwcbCacheServerFailDetectType_Object = MibTableColumn
etsysTwcbCacheServerFailDetectType = _EtsysTwcbCacheServerFailDetectType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 5),
    _EtsysTwcbCacheServerFailDetectType_Type()
)
etsysTwcbCacheServerFailDetectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerFailDetectType.setStatus("current")


class _EtsysTwcbCacheServerFailDetectProbeOne_Type(SnmpAdminString):
    """Custom type etsysTwcbCacheServerFailDetectProbeOne based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EtsysTwcbCacheServerFailDetectProbeOne_Type.__name__ = "SnmpAdminString"
_EtsysTwcbCacheServerFailDetectProbeOne_Object = MibTableColumn
etsysTwcbCacheServerFailDetectProbeOne = _EtsysTwcbCacheServerFailDetectProbeOne_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 6),
    _EtsysTwcbCacheServerFailDetectProbeOne_Type()
)
etsysTwcbCacheServerFailDetectProbeOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerFailDetectProbeOne.setStatus("current")


class _EtsysTwcbCacheServerFailDetectProbeTwo_Type(SnmpAdminString):
    """Custom type etsysTwcbCacheServerFailDetectProbeTwo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EtsysTwcbCacheServerFailDetectProbeTwo_Type.__name__ = "SnmpAdminString"
_EtsysTwcbCacheServerFailDetectProbeTwo_Object = MibTableColumn
etsysTwcbCacheServerFailDetectProbeTwo = _EtsysTwcbCacheServerFailDetectProbeTwo_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 7),
    _EtsysTwcbCacheServerFailDetectProbeTwo_Type()
)
etsysTwcbCacheServerFailDetectProbeTwo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerFailDetectProbeTwo.setStatus("current")


class _EtsysTwcbCacheServerFailDetectAppPort_Type(InetPortNumber):
    """Custom type etsysTwcbCacheServerFailDetectAppPort based on InetPortNumber"""
    defaultValue = 80

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTwcbCacheServerFailDetectAppPort_Type.__name__ = "InetPortNumber"
_EtsysTwcbCacheServerFailDetectAppPort_Object = MibTableColumn
etsysTwcbCacheServerFailDetectAppPort = _EtsysTwcbCacheServerFailDetectAppPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 8),
    _EtsysTwcbCacheServerFailDetectAppPort_Type()
)
etsysTwcbCacheServerFailDetectAppPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerFailDetectAppPort.setStatus("current")


class _EtsysTwcbCacheServerAdminStatus_Type(Integer32):
    """Custom type etsysTwcbCacheServerAdminStatus based on Integer32"""
    defaultValue = 1

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


_EtsysTwcbCacheServerAdminStatus_Type.__name__ = "Integer32"
_EtsysTwcbCacheServerAdminStatus_Object = MibTableColumn
etsysTwcbCacheServerAdminStatus = _EtsysTwcbCacheServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 9),
    _EtsysTwcbCacheServerAdminStatus_Type()
)
etsysTwcbCacheServerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerAdminStatus.setStatus("current")


class _EtsysTwcbCacheServerOperStatus_Type(Integer32):
    """Custom type etsysTwcbCacheServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EtsysTwcbCacheServerOperStatus_Type.__name__ = "Integer32"
_EtsysTwcbCacheServerOperStatus_Object = MibTableColumn
etsysTwcbCacheServerOperStatus = _EtsysTwcbCacheServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 10),
    _EtsysTwcbCacheServerOperStatus_Type()
)
etsysTwcbCacheServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerOperStatus.setStatus("current")
_EtsysTwcbCacheServerConns_Type = Gauge32
_EtsysTwcbCacheServerConns_Object = MibTableColumn
etsysTwcbCacheServerConns = _EtsysTwcbCacheServerConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 11),
    _EtsysTwcbCacheServerConns_Type()
)
etsysTwcbCacheServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerConns.setStatus("current")
_EtsysTwcbCacheServerHits_Type = Counter32
_EtsysTwcbCacheServerHits_Object = MibTableColumn
etsysTwcbCacheServerHits = _EtsysTwcbCacheServerHits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 12),
    _EtsysTwcbCacheServerHits_Type()
)
etsysTwcbCacheServerHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerHits.setStatus("current")
_EtsysTwcbCacheServerStateChanges_Type = Counter32
_EtsysTwcbCacheServerStateChanges_Object = MibTableColumn
etsysTwcbCacheServerStateChanges = _EtsysTwcbCacheServerStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 13),
    _EtsysTwcbCacheServerStateChanges_Type()
)
etsysTwcbCacheServerStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerStateChanges.setStatus("current")
_EtsysTwcbCacheServerLastStateChangeDateAndTime_Type = DateAndTime
_EtsysTwcbCacheServerLastStateChangeDateAndTime_Object = MibTableColumn
etsysTwcbCacheServerLastStateChangeDateAndTime = _EtsysTwcbCacheServerLastStateChangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 14),
    _EtsysTwcbCacheServerLastStateChangeDateAndTime_Type()
)
etsysTwcbCacheServerLastStateChangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerLastStateChangeDateAndTime.setStatus("current")
_EtsysTwcbCacheServerRowStatus_Type = RowStatus
_EtsysTwcbCacheServerRowStatus_Object = MibTableColumn
etsysTwcbCacheServerRowStatus = _EtsysTwcbCacheServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 3, 1, 15),
    _EtsysTwcbCacheServerRowStatus_Type()
)
etsysTwcbCacheServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbCacheServerRowStatus.setStatus("current")
_EtsysTwcbWebcacheServerTable_Object = MibTable
etsysTwcbWebcacheServerTable = _EtsysTwcbWebcacheServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4)
)
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerTable.setStatus("current")
_EtsysTwcbWebcacheServerEntry_Object = MibTableRow
etsysTwcbWebcacheServerEntry = _EtsysTwcbWebcacheServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1)
)
etsysTwcbWebcacheServerEntry.setIndexNames(
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerInetVersion"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerName"),
)
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerEntry.setStatus("current")
_EtsysTwcbWebcacheServerInetVersion_Type = InetVersion
_EtsysTwcbWebcacheServerInetVersion_Object = MibTableColumn
etsysTwcbWebcacheServerInetVersion = _EtsysTwcbWebcacheServerInetVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 1),
    _EtsysTwcbWebcacheServerInetVersion_Type()
)
etsysTwcbWebcacheServerInetVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerInetVersion.setStatus("current")


class _EtsysTwcbWebcacheServerName_Type(SnmpAdminString):
    """Custom type etsysTwcbWebcacheServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysTwcbWebcacheServerName_Type.__name__ = "SnmpAdminString"
_EtsysTwcbWebcacheServerName_Object = MibTableColumn
etsysTwcbWebcacheServerName = _EtsysTwcbWebcacheServerName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 2),
    _EtsysTwcbWebcacheServerName_Type()
)
etsysTwcbWebcacheServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerName.setStatus("current")


class _EtsysTwcbWebcacheServerIdleTimeout_Type(Unsigned32):
    """Custom type etsysTwcbWebcacheServerIdleTimeout based on Unsigned32"""
    defaultValue = 41


_EtsysTwcbWebcacheServerIdleTimeout_Object = MibTableColumn
etsysTwcbWebcacheServerIdleTimeout = _EtsysTwcbWebcacheServerIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 3),
    _EtsysTwcbWebcacheServerIdleTimeout_Type()
)
etsysTwcbWebcacheServerIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerIdleTimeout.setUnits("seconds")


class _EtsysTwcbWebcacheServerHttpport_Type(InetPortNumber):
    """Custom type etsysTwcbWebcacheServerHttpport based on InetPortNumber"""
    defaultValue = 80

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTwcbWebcacheServerHttpport_Type.__name__ = "InetPortNumber"
_EtsysTwcbWebcacheServerHttpport_Object = MibTableColumn
etsysTwcbWebcacheServerHttpport = _EtsysTwcbWebcacheServerHttpport_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 4),
    _EtsysTwcbWebcacheServerHttpport_Type()
)
etsysTwcbWebcacheServerHttpport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHttpport.setStatus("current")


class _EtsysTwcbWebcacheServerAdminStatus_Type(Integer32):
    """Custom type etsysTwcbWebcacheServerAdminStatus based on Integer32"""
    defaultValue = 1

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


_EtsysTwcbWebcacheServerAdminStatus_Type.__name__ = "Integer32"
_EtsysTwcbWebcacheServerAdminStatus_Object = MibTableColumn
etsysTwcbWebcacheServerAdminStatus = _EtsysTwcbWebcacheServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 5),
    _EtsysTwcbWebcacheServerAdminStatus_Type()
)
etsysTwcbWebcacheServerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerAdminStatus.setStatus("current")


class _EtsysTwcbWebcacheServerOperStatus_Type(Integer32):
    """Custom type etsysTwcbWebcacheServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EtsysTwcbWebcacheServerOperStatus_Type.__name__ = "Integer32"
_EtsysTwcbWebcacheServerOperStatus_Object = MibTableColumn
etsysTwcbWebcacheServerOperStatus = _EtsysTwcbWebcacheServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 6),
    _EtsysTwcbWebcacheServerOperStatus_Type()
)
etsysTwcbWebcacheServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerOperStatus.setStatus("current")
_EtsysTwcbWebcacheServerConns_Type = Gauge32
_EtsysTwcbWebcacheServerConns_Object = MibTableColumn
etsysTwcbWebcacheServerConns = _EtsysTwcbWebcacheServerConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 7),
    _EtsysTwcbWebcacheServerConns_Type()
)
etsysTwcbWebcacheServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerConns.setStatus("current")
_EtsysTwcbWebcacheServerHits_Type = Counter32
_EtsysTwcbWebcacheServerHits_Object = MibTableColumn
etsysTwcbWebcacheServerHits = _EtsysTwcbWebcacheServerHits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 8),
    _EtsysTwcbWebcacheServerHits_Type()
)
etsysTwcbWebcacheServerHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHits.setStatus("current")
_EtsysTwcbWebcacheServerStateChanges_Type = Counter32
_EtsysTwcbWebcacheServerStateChanges_Object = MibTableColumn
etsysTwcbWebcacheServerStateChanges = _EtsysTwcbWebcacheServerStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 9),
    _EtsysTwcbWebcacheServerStateChanges_Type()
)
etsysTwcbWebcacheServerStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerStateChanges.setStatus("current")
_EtsysTwcbWebcacheServerLastStateChangeDateAndTime_Type = DateAndTime
_EtsysTwcbWebcacheServerLastStateChangeDateAndTime_Object = MibTableColumn
etsysTwcbWebcacheServerLastStateChangeDateAndTime = _EtsysTwcbWebcacheServerLastStateChangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 10),
    _EtsysTwcbWebcacheServerLastStateChangeDateAndTime_Type()
)
etsysTwcbWebcacheServerLastStateChangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerLastStateChangeDateAndTime.setStatus("current")
_EtsysTwcbWebcacheServerHostPermitCount_Type = Counter32
_EtsysTwcbWebcacheServerHostPermitCount_Object = MibTableColumn
etsysTwcbWebcacheServerHostPermitCount = _EtsysTwcbWebcacheServerHostPermitCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 11),
    _EtsysTwcbWebcacheServerHostPermitCount_Type()
)
etsysTwcbWebcacheServerHostPermitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostPermitCount.setStatus("current")
_EtsysTwcbWebcacheServerHostDenyCount_Type = Counter32
_EtsysTwcbWebcacheServerHostDenyCount_Object = MibTableColumn
etsysTwcbWebcacheServerHostDenyCount = _EtsysTwcbWebcacheServerHostDenyCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 12),
    _EtsysTwcbWebcacheServerHostDenyCount_Type()
)
etsysTwcbWebcacheServerHostDenyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostDenyCount.setStatus("current")
_EtsysTwcbWebcacheServerBypassListCount_Type = Counter32
_EtsysTwcbWebcacheServerBypassListCount_Object = MibTableColumn
etsysTwcbWebcacheServerBypassListCount = _EtsysTwcbWebcacheServerBypassListCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 13),
    _EtsysTwcbWebcacheServerBypassListCount_Type()
)
etsysTwcbWebcacheServerBypassListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerBypassListCount.setStatus("current")
_EtsysTwcbWebcacheServerServerfarmCount_Type = Counter32
_EtsysTwcbWebcacheServerServerfarmCount_Object = MibTableColumn
etsysTwcbWebcacheServerServerfarmCount = _EtsysTwcbWebcacheServerServerfarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 14),
    _EtsysTwcbWebcacheServerServerfarmCount_Type()
)
etsysTwcbWebcacheServerServerfarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerServerfarmCount.setStatus("current")
_EtsysTwcbWebcacheServerRowStatus_Type = RowStatus
_EtsysTwcbWebcacheServerRowStatus_Object = MibTableColumn
etsysTwcbWebcacheServerRowStatus = _EtsysTwcbWebcacheServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 4, 1, 15),
    _EtsysTwcbWebcacheServerRowStatus_Type()
)
etsysTwcbWebcacheServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerRowStatus.setStatus("current")
_EtsysTwcbWebcacheServerHostPermitTable_Object = MibTable
etsysTwcbWebcacheServerHostPermitTable = _EtsysTwcbWebcacheServerHostPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 5)
)
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostPermitTable.setStatus("current")
_EtsysTwcbWebcacheServerHostPermitEntry_Object = MibTableRow
etsysTwcbWebcacheServerHostPermitEntry = _EtsysTwcbWebcacheServerHostPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 5, 1)
)
etsysTwcbWebcacheServerHostPermitEntry.setIndexNames(
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHostPermitAddressType"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerName"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHostPermitStartIp"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHostPermitEndIp"),
)
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostPermitEntry.setStatus("current")
_EtsysTwcbWebcacheServerHostPermitAddressType_Type = InetAddressType
_EtsysTwcbWebcacheServerHostPermitAddressType_Object = MibTableColumn
etsysTwcbWebcacheServerHostPermitAddressType = _EtsysTwcbWebcacheServerHostPermitAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 5, 1, 1),
    _EtsysTwcbWebcacheServerHostPermitAddressType_Type()
)
etsysTwcbWebcacheServerHostPermitAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostPermitAddressType.setStatus("current")
_EtsysTwcbWebcacheServerHostPermitStartIp_Type = InetAddress
_EtsysTwcbWebcacheServerHostPermitStartIp_Object = MibTableColumn
etsysTwcbWebcacheServerHostPermitStartIp = _EtsysTwcbWebcacheServerHostPermitStartIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 5, 1, 2),
    _EtsysTwcbWebcacheServerHostPermitStartIp_Type()
)
etsysTwcbWebcacheServerHostPermitStartIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostPermitStartIp.setStatus("current")
_EtsysTwcbWebcacheServerHostPermitEndIp_Type = InetAddress
_EtsysTwcbWebcacheServerHostPermitEndIp_Object = MibTableColumn
etsysTwcbWebcacheServerHostPermitEndIp = _EtsysTwcbWebcacheServerHostPermitEndIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 5, 1, 3),
    _EtsysTwcbWebcacheServerHostPermitEndIp_Type()
)
etsysTwcbWebcacheServerHostPermitEndIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostPermitEndIp.setStatus("current")
_EtsysTwcbWebcacheServerHostPermitRowStatus_Type = RowStatus
_EtsysTwcbWebcacheServerHostPermitRowStatus_Object = MibTableColumn
etsysTwcbWebcacheServerHostPermitRowStatus = _EtsysTwcbWebcacheServerHostPermitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 5, 1, 4),
    _EtsysTwcbWebcacheServerHostPermitRowStatus_Type()
)
etsysTwcbWebcacheServerHostPermitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostPermitRowStatus.setStatus("current")
_EtsysTwcbWebcacheServerHostDenyTable_Object = MibTable
etsysTwcbWebcacheServerHostDenyTable = _EtsysTwcbWebcacheServerHostDenyTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 6)
)
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostDenyTable.setStatus("current")
_EtsysTwcbWebcacheServerHostDenyEntry_Object = MibTableRow
etsysTwcbWebcacheServerHostDenyEntry = _EtsysTwcbWebcacheServerHostDenyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 6, 1)
)
etsysTwcbWebcacheServerHostDenyEntry.setIndexNames(
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHostDenyAddressType"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerName"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHostDenyStartIp"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHostDenyEndIp"),
)
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostDenyEntry.setStatus("current")
_EtsysTwcbWebcacheServerHostDenyAddressType_Type = InetAddressType
_EtsysTwcbWebcacheServerHostDenyAddressType_Object = MibTableColumn
etsysTwcbWebcacheServerHostDenyAddressType = _EtsysTwcbWebcacheServerHostDenyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 6, 1, 1),
    _EtsysTwcbWebcacheServerHostDenyAddressType_Type()
)
etsysTwcbWebcacheServerHostDenyAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostDenyAddressType.setStatus("current")
_EtsysTwcbWebcacheServerHostDenyStartIp_Type = InetAddress
_EtsysTwcbWebcacheServerHostDenyStartIp_Object = MibTableColumn
etsysTwcbWebcacheServerHostDenyStartIp = _EtsysTwcbWebcacheServerHostDenyStartIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 6, 1, 2),
    _EtsysTwcbWebcacheServerHostDenyStartIp_Type()
)
etsysTwcbWebcacheServerHostDenyStartIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostDenyStartIp.setStatus("current")
_EtsysTwcbWebcacheServerHostDenyEndIp_Type = InetAddress
_EtsysTwcbWebcacheServerHostDenyEndIp_Object = MibTableColumn
etsysTwcbWebcacheServerHostDenyEndIp = _EtsysTwcbWebcacheServerHostDenyEndIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 6, 1, 3),
    _EtsysTwcbWebcacheServerHostDenyEndIp_Type()
)
etsysTwcbWebcacheServerHostDenyEndIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostDenyEndIp.setStatus("current")
_EtsysTwcbWebcacheServerHostDenyRowStatus_Type = RowStatus
_EtsysTwcbWebcacheServerHostDenyRowStatus_Object = MibTableColumn
etsysTwcbWebcacheServerHostDenyRowStatus = _EtsysTwcbWebcacheServerHostDenyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 6, 1, 4),
    _EtsysTwcbWebcacheServerHostDenyRowStatus_Type()
)
etsysTwcbWebcacheServerHostDenyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerHostDenyRowStatus.setStatus("current")
_EtsysTwcbWebcacheServerBypassTable_Object = MibTable
etsysTwcbWebcacheServerBypassTable = _EtsysTwcbWebcacheServerBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 7)
)
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerBypassTable.setStatus("current")
_EtsysTwcbWebcacheServerBypassEntry_Object = MibTableRow
etsysTwcbWebcacheServerBypassEntry = _EtsysTwcbWebcacheServerBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 7, 1)
)
etsysTwcbWebcacheServerBypassEntry.setIndexNames(
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerBypassAddressType"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerName"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerBypassStartIp"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerBypassEndIp"),
)
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerBypassEntry.setStatus("current")
_EtsysTwcbWebcacheServerBypassAddressType_Type = InetAddressType
_EtsysTwcbWebcacheServerBypassAddressType_Object = MibTableColumn
etsysTwcbWebcacheServerBypassAddressType = _EtsysTwcbWebcacheServerBypassAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 7, 1, 1),
    _EtsysTwcbWebcacheServerBypassAddressType_Type()
)
etsysTwcbWebcacheServerBypassAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerBypassAddressType.setStatus("current")
_EtsysTwcbWebcacheServerBypassStartIp_Type = InetAddress
_EtsysTwcbWebcacheServerBypassStartIp_Object = MibTableColumn
etsysTwcbWebcacheServerBypassStartIp = _EtsysTwcbWebcacheServerBypassStartIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 7, 1, 2),
    _EtsysTwcbWebcacheServerBypassStartIp_Type()
)
etsysTwcbWebcacheServerBypassStartIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerBypassStartIp.setStatus("current")
_EtsysTwcbWebcacheServerBypassEndIp_Type = InetAddress
_EtsysTwcbWebcacheServerBypassEndIp_Object = MibTableColumn
etsysTwcbWebcacheServerBypassEndIp = _EtsysTwcbWebcacheServerBypassEndIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 7, 1, 3),
    _EtsysTwcbWebcacheServerBypassEndIp_Type()
)
etsysTwcbWebcacheServerBypassEndIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerBypassEndIp.setStatus("current")
_EtsysTwcbWebcacheServerBypassRowStatus_Type = RowStatus
_EtsysTwcbWebcacheServerBypassRowStatus_Object = MibTableColumn
etsysTwcbWebcacheServerBypassRowStatus = _EtsysTwcbWebcacheServerBypassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 7, 1, 4),
    _EtsysTwcbWebcacheServerBypassRowStatus_Type()
)
etsysTwcbWebcacheServerBypassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerBypassRowStatus.setStatus("current")
_EtsysTwcbWebcacheServerfarmTable_Object = MibTable
etsysTwcbWebcacheServerfarmTable = _EtsysTwcbWebcacheServerfarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 8)
)
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerfarmTable.setStatus("current")
_EtsysTwcbWebcacheServerfarmEntry_Object = MibTableRow
etsysTwcbWebcacheServerfarmEntry = _EtsysTwcbWebcacheServerfarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 8, 1)
)
etsysTwcbWebcacheServerfarmEntry.setIndexNames(
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerInetVersion"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerName"),
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmId"),
)
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerfarmEntry.setStatus("current")
_EtsysTwcbWebcacheServerfarmRowStatus_Type = RowStatus
_EtsysTwcbWebcacheServerfarmRowStatus_Object = MibTableColumn
etsysTwcbWebcacheServerfarmRowStatus = _EtsysTwcbWebcacheServerfarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 8, 1, 1),
    _EtsysTwcbWebcacheServerfarmRowStatus_Type()
)
etsysTwcbWebcacheServerfarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTwcbWebcacheServerfarmRowStatus.setStatus("current")
_EtsysTwcbBindingTable_Object = MibTable
etsysTwcbBindingTable = _EtsysTwcbBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9)
)
if mibBuilder.loadTexts:
    etsysTwcbBindingTable.setStatus("current")
_EtsysTwcbBindingEntry_Object = MibTableRow
etsysTwcbBindingEntry = _EtsysTwcbBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1)
)
etsysTwcbBindingEntry.setIndexNames(
    (0, "ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingId"),
)
if mibBuilder.loadTexts:
    etsysTwcbBindingEntry.setStatus("current")


class _EtsysTwcbBindingId_Type(Unsigned32):
    """Custom type etsysTwcbBindingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTwcbBindingId_Type.__name__ = "Unsigned32"
_EtsysTwcbBindingId_Object = MibTableColumn
etsysTwcbBindingId = _EtsysTwcbBindingId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 1),
    _EtsysTwcbBindingId_Type()
)
etsysTwcbBindingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTwcbBindingId.setStatus("current")


class _EtsysTwcbBindingState_Type(Integer32):
    """Custom type etsysTwcbBindingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("established", 3),
          ("init", 1),
          ("syncing", 2))
    )


_EtsysTwcbBindingState_Type.__name__ = "Integer32"
_EtsysTwcbBindingState_Object = MibTableColumn
etsysTwcbBindingState = _EtsysTwcbBindingState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 2),
    _EtsysTwcbBindingState_Type()
)
etsysTwcbBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingState.setStatus("current")
_EtsysTwcbBindingAddressType_Type = InetAddressType
_EtsysTwcbBindingAddressType_Object = MibTableColumn
etsysTwcbBindingAddressType = _EtsysTwcbBindingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 3),
    _EtsysTwcbBindingAddressType_Type()
)
etsysTwcbBindingAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingAddressType.setStatus("current")
_EtsysTwcbBindingSrcIp_Type = InetAddress
_EtsysTwcbBindingSrcIp_Object = MibTableColumn
etsysTwcbBindingSrcIp = _EtsysTwcbBindingSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 4),
    _EtsysTwcbBindingSrcIp_Type()
)
etsysTwcbBindingSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingSrcIp.setStatus("current")


class _EtsysTwcbBindingSrcPort_Type(InetPortNumber):
    """Custom type etsysTwcbBindingSrcPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTwcbBindingSrcPort_Type.__name__ = "InetPortNumber"
_EtsysTwcbBindingSrcPort_Object = MibTableColumn
etsysTwcbBindingSrcPort = _EtsysTwcbBindingSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 5),
    _EtsysTwcbBindingSrcPort_Type()
)
etsysTwcbBindingSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingSrcPort.setStatus("current")
_EtsysTwcbBindingDstIp_Type = InetAddress
_EtsysTwcbBindingDstIp_Object = MibTableColumn
etsysTwcbBindingDstIp = _EtsysTwcbBindingDstIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 6),
    _EtsysTwcbBindingDstIp_Type()
)
etsysTwcbBindingDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingDstIp.setStatus("current")


class _EtsysTwcbBindingDstPort_Type(InetPortNumber):
    """Custom type etsysTwcbBindingDstPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysTwcbBindingDstPort_Type.__name__ = "InetPortNumber"
_EtsysTwcbBindingDstPort_Object = MibTableColumn
etsysTwcbBindingDstPort = _EtsysTwcbBindingDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 7),
    _EtsysTwcbBindingDstPort_Type()
)
etsysTwcbBindingDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingDstPort.setStatus("current")
_EtsysTwcbBindingHWConns_Type = Gauge32
_EtsysTwcbBindingHWConns_Object = MibTableColumn
etsysTwcbBindingHWConns = _EtsysTwcbBindingHWConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 8),
    _EtsysTwcbBindingHWConns_Type()
)
etsysTwcbBindingHWConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingHWConns.setStatus("current")


class _EtsysTwcbBindingWebcacheName_Type(SnmpAdminString):
    """Custom type etsysTwcbBindingWebcacheName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysTwcbBindingWebcacheName_Type.__name__ = "SnmpAdminString"
_EtsysTwcbBindingWebcacheName_Object = MibTableColumn
etsysTwcbBindingWebcacheName = _EtsysTwcbBindingWebcacheName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 9),
    _EtsysTwcbBindingWebcacheName_Type()
)
etsysTwcbBindingWebcacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingWebcacheName.setStatus("current")


class _EtsysTwcbBindingWcServerfarmName_Type(SnmpAdminString):
    """Custom type etsysTwcbBindingWcServerfarmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysTwcbBindingWcServerfarmName_Type.__name__ = "SnmpAdminString"
_EtsysTwcbBindingWcServerfarmName_Object = MibTableColumn
etsysTwcbBindingWcServerfarmName = _EtsysTwcbBindingWcServerfarmName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 10),
    _EtsysTwcbBindingWcServerfarmName_Type()
)
etsysTwcbBindingWcServerfarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingWcServerfarmName.setStatus("current")
_EtsysTwcbBindingCacheIp_Type = InetAddress
_EtsysTwcbBindingCacheIp_Object = MibTableColumn
etsysTwcbBindingCacheIp = _EtsysTwcbBindingCacheIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 11),
    _EtsysTwcbBindingCacheIp_Type()
)
etsysTwcbBindingCacheIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingCacheIp.setStatus("current")
_EtsysTwcbBindingCreationDate_Type = DateAndTime
_EtsysTwcbBindingCreationDate_Object = MibTableColumn
etsysTwcbBindingCreationDate = _EtsysTwcbBindingCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 12),
    _EtsysTwcbBindingCreationDate_Type()
)
etsysTwcbBindingCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingCreationDate.setStatus("current")
_EtsysTwcbBindingExpirationDate_Type = DateAndTime
_EtsysTwcbBindingExpirationDate_Object = MibTableColumn
etsysTwcbBindingExpirationDate = _EtsysTwcbBindingExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 13),
    _EtsysTwcbBindingExpirationDate_Type()
)
etsysTwcbBindingExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingExpirationDate.setStatus("current")
_EtsysTwcbBindingIdleTime_Type = Unsigned32
_EtsysTwcbBindingIdleTime_Object = MibTableColumn
etsysTwcbBindingIdleTime = _EtsysTwcbBindingIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 14),
    _EtsysTwcbBindingIdleTime_Type()
)
etsysTwcbBindingIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysTwcbBindingIdleTime.setUnits("seconds")
_EtsysTwcbBindingExpireTime_Type = Unsigned32
_EtsysTwcbBindingExpireTime_Object = MibTableColumn
etsysTwcbBindingExpireTime = _EtsysTwcbBindingExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 15),
    _EtsysTwcbBindingExpireTime_Type()
)
etsysTwcbBindingExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTwcbBindingExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysTwcbBindingExpireTime.setUnits("seconds")


class _EtsysTwcbBindingClear_Type(TruthValue):
    """Custom type etsysTwcbBindingClear based on TruthValue"""


_EtsysTwcbBindingClear_Object = MibTableColumn
etsysTwcbBindingClear = _EtsysTwcbBindingClear_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 2, 9, 1, 16),
    _EtsysTwcbBindingClear_Type()
)
etsysTwcbBindingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTwcbBindingClear.setStatus("current")
_EtsysTwcbConformance_ObjectIdentity = ObjectIdentity
etsysTwcbConformance = _EtsysTwcbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3)
)
_EtsysTwcbMIBGroups_ObjectIdentity = ObjectIdentity
etsysTwcbMIBGroups = _EtsysTwcbMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1)
)
_EtsysTwcbMIBCompliances_ObjectIdentity = ObjectIdentity
etsysTwcbMIBCompliances = _EtsysTwcbMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 2)
)

# Managed Objects groups

etsysTwcbMIBGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1, 1)
)
etsysTwcbMIBGlobalStatsGroup.setObjects(
      *(("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsCachesUsed"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsWcServerfarmsUsed"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsWebcacheUsed"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsBindingsCurrent"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsBindingsHigh"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsBindingsDeleted"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsBindingsTotal"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsBindingsExhausted"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsBindingsNoCaches"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsBindingsPerSecond"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsWebcacheActive"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsWebcacheHigh"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsWcServerfarmActive"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsWcServerfarmHigh"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsCacheActive"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsCacheHigh"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsClear"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsClearDateAndTime"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsMinTimeoutValue"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbStatsMaxTimeoutValue"))
)
if mibBuilder.loadTexts:
    etsysTwcbMIBGlobalStatsGroup.setStatus("current")

etsysTwcbMIBWcServerfarmTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1, 2)
)
etsysTwcbMIBWcServerfarmTableGroup.setObjects(
      *(("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmPredictor"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmAdminStatus"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmOperStatus"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmConns"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmHits"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmStateChanges"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmLastStateChangeDateAndTime"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmCachesCfg"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmCachesUp"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmWebcacheCfg"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmRoundRobinCount"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmRowStatus"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcServerfarmId"))
)
if mibBuilder.loadTexts:
    etsysTwcbMIBWcServerfarmTableGroup.setStatus("current")

etsysTwcbMIBWcSfarmRoundRobinTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1, 3)
)
etsysTwcbMIBWcSfarmRoundRobinTableGroup.setObjects(
    ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWcSfarmRoundRobinRowStatus")
)
if mibBuilder.loadTexts:
    etsysTwcbMIBWcSfarmRoundRobinTableGroup.setStatus("current")

etsysTwcbMIBCacheServerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1, 4)
)
etsysTwcbMIBCacheServerTableGroup.setObjects(
      *(("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerWeight"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerMaxConns"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerFailDetectType"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerFailDetectProbeOne"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerFailDetectProbeTwo"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerFailDetectAppPort"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerAdminStatus"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerOperStatus"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerConns"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerHits"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerStateChanges"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerLastStateChangeDateAndTime"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbCacheServerRowStatus"))
)
if mibBuilder.loadTexts:
    etsysTwcbMIBCacheServerTableGroup.setStatus("current")

etsysTwcbMIBWebcacheServerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1, 5)
)
etsysTwcbMIBWebcacheServerTableGroup.setObjects(
      *(("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerIdleTimeout"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHttpport"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerAdminStatus"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerOperStatus"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerConns"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHits"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerStateChanges"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerLastStateChangeDateAndTime"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHostPermitCount"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHostDenyCount"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerBypassListCount"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerServerfarmCount"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerRowStatus"))
)
if mibBuilder.loadTexts:
    etsysTwcbMIBWebcacheServerTableGroup.setStatus("current")

etsysTwcbMIBWebcacheServerHostPermitTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1, 6)
)
etsysTwcbMIBWebcacheServerHostPermitTableGroup.setObjects(
    ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHostPermitRowStatus")
)
if mibBuilder.loadTexts:
    etsysTwcbMIBWebcacheServerHostPermitTableGroup.setStatus("current")

etsysTwcbMIBWebcacheServerHostDenyTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1, 7)
)
etsysTwcbMIBWebcacheServerHostDenyTableGroup.setObjects(
    ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerHostDenyRowStatus")
)
if mibBuilder.loadTexts:
    etsysTwcbMIBWebcacheServerHostDenyTableGroup.setStatus("current")

etsysTwcbMIBWebcacheServerBypassTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1, 8)
)
etsysTwcbMIBWebcacheServerBypassTableGroup.setObjects(
    ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerBypassRowStatus")
)
if mibBuilder.loadTexts:
    etsysTwcbMIBWebcacheServerBypassTableGroup.setStatus("current")

etsysTwcbMIBWebcacheServerfarmTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1, 9)
)
etsysTwcbMIBWebcacheServerfarmTableGroup.setObjects(
    ("ENTERASYS-TWCB-MIB-2", "etsysTwcbWebcacheServerfarmRowStatus")
)
if mibBuilder.loadTexts:
    etsysTwcbMIBWebcacheServerfarmTableGroup.setStatus("current")

etsysTwcbMIBBindingTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 1, 10)
)
etsysTwcbMIBBindingTableGroup.setObjects(
      *(("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingAddressType"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingSrcIp"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingSrcPort"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingDstIp"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingDstPort"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingHWConns"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingWebcacheName"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingWcServerfarmName"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingCacheIp"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingCreationDate"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingExpirationDate"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingIdleTime"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingExpireTime"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingClear"),
        ("ENTERASYS-TWCB-MIB-2", "etsysTwcbBindingState"))
)
if mibBuilder.loadTexts:
    etsysTwcbMIBBindingTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysTwcbMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 76, 3, 2, 1)
)
if mibBuilder.loadTexts:
    etsysTwcbMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-TWCB-MIB-2",
    **{"etsysTWCBMIB": etsysTWCBMIB,
       "etsysTwcbGlobal": etsysTwcbGlobal,
       "etsysTwcbGlobalStats": etsysTwcbGlobalStats,
       "etsysTwcbStatsCachesUsed": etsysTwcbStatsCachesUsed,
       "etsysTwcbStatsWcServerfarmsUsed": etsysTwcbStatsWcServerfarmsUsed,
       "etsysTwcbStatsWebcacheUsed": etsysTwcbStatsWebcacheUsed,
       "etsysTwcbStatsBindingsCurrent": etsysTwcbStatsBindingsCurrent,
       "etsysTwcbStatsBindingsHigh": etsysTwcbStatsBindingsHigh,
       "etsysTwcbStatsBindingsDeleted": etsysTwcbStatsBindingsDeleted,
       "etsysTwcbStatsBindingsTotal": etsysTwcbStatsBindingsTotal,
       "etsysTwcbStatsBindingsExhausted": etsysTwcbStatsBindingsExhausted,
       "etsysTwcbStatsBindingsNoCaches": etsysTwcbStatsBindingsNoCaches,
       "etsysTwcbStatsBindingsPerSecond": etsysTwcbStatsBindingsPerSecond,
       "etsysTwcbStatsWebcacheActive": etsysTwcbStatsWebcacheActive,
       "etsysTwcbStatsWebcacheHigh": etsysTwcbStatsWebcacheHigh,
       "etsysTwcbStatsWcServerfarmActive": etsysTwcbStatsWcServerfarmActive,
       "etsysTwcbStatsWcServerfarmHigh": etsysTwcbStatsWcServerfarmHigh,
       "etsysTwcbStatsCacheActive": etsysTwcbStatsCacheActive,
       "etsysTwcbStatsCacheHigh": etsysTwcbStatsCacheHigh,
       "etsysTwcbStatsClear": etsysTwcbStatsClear,
       "etsysTwcbStatsClearDateAndTime": etsysTwcbStatsClearDateAndTime,
       "etsysTwcbStatsMinTimeoutValue": etsysTwcbStatsMinTimeoutValue,
       "etsysTwcbStatsMaxTimeoutValue": etsysTwcbStatsMaxTimeoutValue,
       "etsysTwcbTables": etsysTwcbTables,
       "etsysTwcbWcServerfarmTable": etsysTwcbWcServerfarmTable,
       "etsysTwcbWcServerfarmEntry": etsysTwcbWcServerfarmEntry,
       "etsysTwcbWcServerfarmInetVersion": etsysTwcbWcServerfarmInetVersion,
       "etsysTwcbWcServerfarmName": etsysTwcbWcServerfarmName,
       "etsysTwcbWcServerfarmPredictor": etsysTwcbWcServerfarmPredictor,
       "etsysTwcbWcServerfarmAdminStatus": etsysTwcbWcServerfarmAdminStatus,
       "etsysTwcbWcServerfarmOperStatus": etsysTwcbWcServerfarmOperStatus,
       "etsysTwcbWcServerfarmConns": etsysTwcbWcServerfarmConns,
       "etsysTwcbWcServerfarmHits": etsysTwcbWcServerfarmHits,
       "etsysTwcbWcServerfarmStateChanges": etsysTwcbWcServerfarmStateChanges,
       "etsysTwcbWcServerfarmLastStateChangeDateAndTime": etsysTwcbWcServerfarmLastStateChangeDateAndTime,
       "etsysTwcbWcServerfarmCachesCfg": etsysTwcbWcServerfarmCachesCfg,
       "etsysTwcbWcServerfarmCachesUp": etsysTwcbWcServerfarmCachesUp,
       "etsysTwcbWcServerfarmWebcacheCfg": etsysTwcbWcServerfarmWebcacheCfg,
       "etsysTwcbWcServerfarmRoundRobinCount": etsysTwcbWcServerfarmRoundRobinCount,
       "etsysTwcbWcServerfarmRowStatus": etsysTwcbWcServerfarmRowStatus,
       "etsysTwcbWcServerfarmId": etsysTwcbWcServerfarmId,
       "etsysTwcbWcSfarmRoundRobinTable": etsysTwcbWcSfarmRoundRobinTable,
       "etsysTwcbWcSfarmRoundRobinEntry": etsysTwcbWcSfarmRoundRobinEntry,
       "etsysTwcbWcSfarmRoundRobinAddressType": etsysTwcbWcSfarmRoundRobinAddressType,
       "etsysTwcbWcSfarmRoundRobinStartIp": etsysTwcbWcSfarmRoundRobinStartIp,
       "etsysTwcbWcSfarmRoundRobinEndIp": etsysTwcbWcSfarmRoundRobinEndIp,
       "etsysTwcbWcSfarmRoundRobinRowStatus": etsysTwcbWcSfarmRoundRobinRowStatus,
       "etsysTwcbCacheServerTable": etsysTwcbCacheServerTable,
       "etsysTwcbCacheServerEntry": etsysTwcbCacheServerEntry,
       "etsysTwcbCacheServerAddressType": etsysTwcbCacheServerAddressType,
       "etsysTwcbCacheServerIp": etsysTwcbCacheServerIp,
       "etsysTwcbCacheServerWeight": etsysTwcbCacheServerWeight,
       "etsysTwcbCacheServerMaxConns": etsysTwcbCacheServerMaxConns,
       "etsysTwcbCacheServerFailDetectType": etsysTwcbCacheServerFailDetectType,
       "etsysTwcbCacheServerFailDetectProbeOne": etsysTwcbCacheServerFailDetectProbeOne,
       "etsysTwcbCacheServerFailDetectProbeTwo": etsysTwcbCacheServerFailDetectProbeTwo,
       "etsysTwcbCacheServerFailDetectAppPort": etsysTwcbCacheServerFailDetectAppPort,
       "etsysTwcbCacheServerAdminStatus": etsysTwcbCacheServerAdminStatus,
       "etsysTwcbCacheServerOperStatus": etsysTwcbCacheServerOperStatus,
       "etsysTwcbCacheServerConns": etsysTwcbCacheServerConns,
       "etsysTwcbCacheServerHits": etsysTwcbCacheServerHits,
       "etsysTwcbCacheServerStateChanges": etsysTwcbCacheServerStateChanges,
       "etsysTwcbCacheServerLastStateChangeDateAndTime": etsysTwcbCacheServerLastStateChangeDateAndTime,
       "etsysTwcbCacheServerRowStatus": etsysTwcbCacheServerRowStatus,
       "etsysTwcbWebcacheServerTable": etsysTwcbWebcacheServerTable,
       "etsysTwcbWebcacheServerEntry": etsysTwcbWebcacheServerEntry,
       "etsysTwcbWebcacheServerInetVersion": etsysTwcbWebcacheServerInetVersion,
       "etsysTwcbWebcacheServerName": etsysTwcbWebcacheServerName,
       "etsysTwcbWebcacheServerIdleTimeout": etsysTwcbWebcacheServerIdleTimeout,
       "etsysTwcbWebcacheServerHttpport": etsysTwcbWebcacheServerHttpport,
       "etsysTwcbWebcacheServerAdminStatus": etsysTwcbWebcacheServerAdminStatus,
       "etsysTwcbWebcacheServerOperStatus": etsysTwcbWebcacheServerOperStatus,
       "etsysTwcbWebcacheServerConns": etsysTwcbWebcacheServerConns,
       "etsysTwcbWebcacheServerHits": etsysTwcbWebcacheServerHits,
       "etsysTwcbWebcacheServerStateChanges": etsysTwcbWebcacheServerStateChanges,
       "etsysTwcbWebcacheServerLastStateChangeDateAndTime": etsysTwcbWebcacheServerLastStateChangeDateAndTime,
       "etsysTwcbWebcacheServerHostPermitCount": etsysTwcbWebcacheServerHostPermitCount,
       "etsysTwcbWebcacheServerHostDenyCount": etsysTwcbWebcacheServerHostDenyCount,
       "etsysTwcbWebcacheServerBypassListCount": etsysTwcbWebcacheServerBypassListCount,
       "etsysTwcbWebcacheServerServerfarmCount": etsysTwcbWebcacheServerServerfarmCount,
       "etsysTwcbWebcacheServerRowStatus": etsysTwcbWebcacheServerRowStatus,
       "etsysTwcbWebcacheServerHostPermitTable": etsysTwcbWebcacheServerHostPermitTable,
       "etsysTwcbWebcacheServerHostPermitEntry": etsysTwcbWebcacheServerHostPermitEntry,
       "etsysTwcbWebcacheServerHostPermitAddressType": etsysTwcbWebcacheServerHostPermitAddressType,
       "etsysTwcbWebcacheServerHostPermitStartIp": etsysTwcbWebcacheServerHostPermitStartIp,
       "etsysTwcbWebcacheServerHostPermitEndIp": etsysTwcbWebcacheServerHostPermitEndIp,
       "etsysTwcbWebcacheServerHostPermitRowStatus": etsysTwcbWebcacheServerHostPermitRowStatus,
       "etsysTwcbWebcacheServerHostDenyTable": etsysTwcbWebcacheServerHostDenyTable,
       "etsysTwcbWebcacheServerHostDenyEntry": etsysTwcbWebcacheServerHostDenyEntry,
       "etsysTwcbWebcacheServerHostDenyAddressType": etsysTwcbWebcacheServerHostDenyAddressType,
       "etsysTwcbWebcacheServerHostDenyStartIp": etsysTwcbWebcacheServerHostDenyStartIp,
       "etsysTwcbWebcacheServerHostDenyEndIp": etsysTwcbWebcacheServerHostDenyEndIp,
       "etsysTwcbWebcacheServerHostDenyRowStatus": etsysTwcbWebcacheServerHostDenyRowStatus,
       "etsysTwcbWebcacheServerBypassTable": etsysTwcbWebcacheServerBypassTable,
       "etsysTwcbWebcacheServerBypassEntry": etsysTwcbWebcacheServerBypassEntry,
       "etsysTwcbWebcacheServerBypassAddressType": etsysTwcbWebcacheServerBypassAddressType,
       "etsysTwcbWebcacheServerBypassStartIp": etsysTwcbWebcacheServerBypassStartIp,
       "etsysTwcbWebcacheServerBypassEndIp": etsysTwcbWebcacheServerBypassEndIp,
       "etsysTwcbWebcacheServerBypassRowStatus": etsysTwcbWebcacheServerBypassRowStatus,
       "etsysTwcbWebcacheServerfarmTable": etsysTwcbWebcacheServerfarmTable,
       "etsysTwcbWebcacheServerfarmEntry": etsysTwcbWebcacheServerfarmEntry,
       "etsysTwcbWebcacheServerfarmRowStatus": etsysTwcbWebcacheServerfarmRowStatus,
       "etsysTwcbBindingTable": etsysTwcbBindingTable,
       "etsysTwcbBindingEntry": etsysTwcbBindingEntry,
       "etsysTwcbBindingId": etsysTwcbBindingId,
       "etsysTwcbBindingState": etsysTwcbBindingState,
       "etsysTwcbBindingAddressType": etsysTwcbBindingAddressType,
       "etsysTwcbBindingSrcIp": etsysTwcbBindingSrcIp,
       "etsysTwcbBindingSrcPort": etsysTwcbBindingSrcPort,
       "etsysTwcbBindingDstIp": etsysTwcbBindingDstIp,
       "etsysTwcbBindingDstPort": etsysTwcbBindingDstPort,
       "etsysTwcbBindingHWConns": etsysTwcbBindingHWConns,
       "etsysTwcbBindingWebcacheName": etsysTwcbBindingWebcacheName,
       "etsysTwcbBindingWcServerfarmName": etsysTwcbBindingWcServerfarmName,
       "etsysTwcbBindingCacheIp": etsysTwcbBindingCacheIp,
       "etsysTwcbBindingCreationDate": etsysTwcbBindingCreationDate,
       "etsysTwcbBindingExpirationDate": etsysTwcbBindingExpirationDate,
       "etsysTwcbBindingIdleTime": etsysTwcbBindingIdleTime,
       "etsysTwcbBindingExpireTime": etsysTwcbBindingExpireTime,
       "etsysTwcbBindingClear": etsysTwcbBindingClear,
       "etsysTwcbConformance": etsysTwcbConformance,
       "etsysTwcbMIBGroups": etsysTwcbMIBGroups,
       "etsysTwcbMIBGlobalStatsGroup": etsysTwcbMIBGlobalStatsGroup,
       "etsysTwcbMIBWcServerfarmTableGroup": etsysTwcbMIBWcServerfarmTableGroup,
       "etsysTwcbMIBWcSfarmRoundRobinTableGroup": etsysTwcbMIBWcSfarmRoundRobinTableGroup,
       "etsysTwcbMIBCacheServerTableGroup": etsysTwcbMIBCacheServerTableGroup,
       "etsysTwcbMIBWebcacheServerTableGroup": etsysTwcbMIBWebcacheServerTableGroup,
       "etsysTwcbMIBWebcacheServerHostPermitTableGroup": etsysTwcbMIBWebcacheServerHostPermitTableGroup,
       "etsysTwcbMIBWebcacheServerHostDenyTableGroup": etsysTwcbMIBWebcacheServerHostDenyTableGroup,
       "etsysTwcbMIBWebcacheServerBypassTableGroup": etsysTwcbMIBWebcacheServerBypassTableGroup,
       "etsysTwcbMIBWebcacheServerfarmTableGroup": etsysTwcbMIBWebcacheServerfarmTableGroup,
       "etsysTwcbMIBBindingTableGroup": etsysTwcbMIBBindingTableGroup,
       "etsysTwcbMIBCompliances": etsysTwcbMIBCompliances,
       "etsysTwcbMIBCompliance": etsysTwcbMIBCompliance}
)
