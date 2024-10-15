# SNMP MIB module (UCD-DISKIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UCD-DISKIO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:20 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(ucdExperimental,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdExperimental")


# MODULE-IDENTITY

ucdDiskIOMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15)
)
ucdDiskIOMIB.setRevisions(
        ("2016-04-04 00:00",
         "2005-04-20 00:00",
         "2002-02-13 00:00",
         "2000-01-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DiskIOTable_Object = MibTable
diskIOTable = _DiskIOTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1)
)
if mibBuilder.loadTexts:
    diskIOTable.setStatus("current")
_DiskIOEntry_Object = MibTableRow
diskIOEntry = _DiskIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1)
)
diskIOEntry.setIndexNames(
    (0, "UCD-DISKIO-MIB", "diskIOIndex"),
)
if mibBuilder.loadTexts:
    diskIOEntry.setStatus("current")


class _DiskIOIndex_Type(Integer32):
    """Custom type diskIOIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiskIOIndex_Type.__name__ = "Integer32"
_DiskIOIndex_Object = MibTableColumn
diskIOIndex = _DiskIOIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 1),
    _DiskIOIndex_Type()
)
diskIOIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIOIndex.setStatus("current")
_DiskIODevice_Type = DisplayString
_DiskIODevice_Object = MibTableColumn
diskIODevice = _DiskIODevice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 2),
    _DiskIODevice_Type()
)
diskIODevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIODevice.setStatus("current")
_DiskIONRead_Type = Counter32
_DiskIONRead_Object = MibTableColumn
diskIONRead = _DiskIONRead_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 3),
    _DiskIONRead_Type()
)
diskIONRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIONRead.setStatus("current")
_DiskIONWritten_Type = Counter32
_DiskIONWritten_Object = MibTableColumn
diskIONWritten = _DiskIONWritten_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 4),
    _DiskIONWritten_Type()
)
diskIONWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIONWritten.setStatus("current")
_DiskIOReads_Type = Counter32
_DiskIOReads_Object = MibTableColumn
diskIOReads = _DiskIOReads_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 5),
    _DiskIOReads_Type()
)
diskIOReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIOReads.setStatus("current")
_DiskIOWrites_Type = Counter32
_DiskIOWrites_Object = MibTableColumn
diskIOWrites = _DiskIOWrites_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 6),
    _DiskIOWrites_Type()
)
diskIOWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIOWrites.setStatus("current")


class _DiskIOLA1_Type(Integer32):
    """Custom type diskIOLA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskIOLA1_Type.__name__ = "Integer32"
_DiskIOLA1_Object = MibTableColumn
diskIOLA1 = _DiskIOLA1_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 9),
    _DiskIOLA1_Type()
)
diskIOLA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIOLA1.setStatus("current")


class _DiskIOLA5_Type(Integer32):
    """Custom type diskIOLA5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskIOLA5_Type.__name__ = "Integer32"
_DiskIOLA5_Object = MibTableColumn
diskIOLA5 = _DiskIOLA5_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 10),
    _DiskIOLA5_Type()
)
diskIOLA5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIOLA5.setStatus("current")


class _DiskIOLA15_Type(Integer32):
    """Custom type diskIOLA15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskIOLA15_Type.__name__ = "Integer32"
_DiskIOLA15_Object = MibTableColumn
diskIOLA15 = _DiskIOLA15_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 11),
    _DiskIOLA15_Type()
)
diskIOLA15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIOLA15.setStatus("current")
_DiskIONReadX_Type = Counter64
_DiskIONReadX_Object = MibTableColumn
diskIONReadX = _DiskIONReadX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 12),
    _DiskIONReadX_Type()
)
diskIONReadX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIONReadX.setStatus("current")
_DiskIONWrittenX_Type = Counter64
_DiskIONWrittenX_Object = MibTableColumn
diskIONWrittenX = _DiskIONWrittenX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 13),
    _DiskIONWrittenX_Type()
)
diskIONWrittenX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIONWrittenX.setStatus("current")
_DiskIOBusyTime_Type = Counter64
_DiskIOBusyTime_Object = MibTableColumn
diskIOBusyTime = _DiskIOBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 14),
    _DiskIOBusyTime_Type()
)
diskIOBusyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIOBusyTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UCD-DISKIO-MIB",
    **{"ucdDiskIOMIB": ucdDiskIOMIB,
       "diskIOTable": diskIOTable,
       "diskIOEntry": diskIOEntry,
       "diskIOIndex": diskIOIndex,
       "diskIODevice": diskIODevice,
       "diskIONRead": diskIONRead,
       "diskIONWritten": diskIONWritten,
       "diskIOReads": diskIOReads,
       "diskIOWrites": diskIOWrites,
       "diskIOLA1": diskIOLA1,
       "diskIOLA5": diskIOLA5,
       "diskIOLA15": diskIOLA15,
       "diskIONReadX": diskIONReadX,
       "diskIONWrittenX": diskIONWrittenX,
       "diskIOBusyTime": diskIOBusyTime}
)
