# SNMP MIB module (AT-LOADER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-LOADER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:22 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

loader = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48)
)
loader.setRevisions(
        ("2007-02-07 10:10",
         "2006-06-28 12:22")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LoadTable_Object = MibTable
loadTable = _LoadTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1)
)
if mibBuilder.loadTexts:
    loadTable.setStatus("current")
_LoadEntry_Object = MibTableRow
loadEntry = _LoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1)
)
loadEntry.setIndexNames(
    (0, "AT-LOADER-MIB", "loadIndex"),
)
if mibBuilder.loadTexts:
    loadEntry.setStatus("current")


class _LoadIndex_Type(Integer32):
    """Custom type loadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_LoadIndex_Type.__name__ = "Integer32"
_LoadIndex_Object = MibTableColumn
loadIndex = _LoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 1),
    _LoadIndex_Type()
)
loadIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadIndex.setStatus("current")
_LoadServer_Type = IpAddress
_LoadServer_Object = MibTableColumn
loadServer = _LoadServer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 2),
    _LoadServer_Type()
)
loadServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadServer.setStatus("current")


class _LoadDestination_Type(Integer32):
    """Custom type loadDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("nvs", 2),
          ("undefined", 1))
    )


_LoadDestination_Type.__name__ = "Integer32"
_LoadDestination_Object = MibTableColumn
loadDestination = _LoadDestination_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 3),
    _LoadDestination_Type()
)
loadDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadDestination.setStatus("current")
_LoadFilename_Type = DisplayString
_LoadFilename_Object = MibTableColumn
loadFilename = _LoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 4),
    _LoadFilename_Type()
)
loadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFilename.setStatus("current")
_LoadDelay_Type = Integer32
_LoadDelay_Object = MibTableColumn
loadDelay = _LoadDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 1, 1, 5),
    _LoadDelay_Type()
)
loadDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadDelay.setStatus("current")


class _LoadStatus_Type(Integer32):
    """Custom type loadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("actionload", 6),
          ("actionstop", 7),
          ("actionupload", 8),
          ("complete", 4),
          ("idle", 1),
          ("loading", 3),
          ("reset", 5),
          ("wait", 2))
    )


_LoadStatus_Type.__name__ = "Integer32"
_LoadStatus_Object = MibScalar
loadStatus = _LoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 48, 2),
    _LoadStatus_Type()
)
loadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-LOADER-MIB",
    **{"loader": loader,
       "loadTable": loadTable,
       "loadEntry": loadEntry,
       "loadIndex": loadIndex,
       "loadServer": loadServer,
       "loadDestination": loadDestination,
       "loadFilename": loadFilename,
       "loadDelay": loadDelay,
       "loadStatus": loadStatus}
)
