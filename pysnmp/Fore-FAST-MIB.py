# SNMP MIB module (Fore-FAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-FAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:59 2024
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

(asx,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ForeFastGroup_ObjectIdentity = ObjectIdentity
foreFastGroup = _ForeFastGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21)
)
_ForeFastIfTable_Object = MibTable
foreFastIfTable = _ForeFastIfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 1)
)
if mibBuilder.loadTexts:
    foreFastIfTable.setStatus("current")
_ForeFastIfEntry_Object = MibTableRow
foreFastIfEntry = _ForeFastIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 1, 1)
)
foreFastIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreFastIfEntry.setStatus("current")


class _ForeFastIfFramingMode_Type(Integer32):
    """Custom type foreFastIfFramingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mode0", 1)
    )


_ForeFastIfFramingMode_Type.__name__ = "Integer32"
_ForeFastIfFramingMode_Object = MibTableColumn
foreFastIfFramingMode = _ForeFastIfFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 1, 1, 1),
    _ForeFastIfFramingMode_Type()
)
foreFastIfFramingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIfFramingMode.setStatus("current")


class _ForeFastIfAdminStatus_Type(Integer32):
    """Custom type foreFastIfAdminStatus based on Integer32"""
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


_ForeFastIfAdminStatus_Type.__name__ = "Integer32"
_ForeFastIfAdminStatus_Object = MibTableColumn
foreFastIfAdminStatus = _ForeFastIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 1, 1, 2),
    _ForeFastIfAdminStatus_Type()
)
foreFastIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreFastIfAdminStatus.setStatus("current")
_ForeFastIwfStatsTable_Object = MibTable
foreFastIwfStatsTable = _ForeFastIwfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2)
)
if mibBuilder.loadTexts:
    foreFastIwfStatsTable.setStatus("current")
_ForeFastIwfStatsEntry_Object = MibTableRow
foreFastIwfStatsEntry = _ForeFastIwfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1)
)
foreFastIwfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreFastIwfStatsEntry.setStatus("current")
_ForeFastIwfTxCells_Type = Counter32
_ForeFastIwfTxCells_Object = MibTableColumn
foreFastIwfTxCells = _ForeFastIwfTxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 1),
    _ForeFastIwfTxCells_Type()
)
foreFastIwfTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIwfTxCells.setStatus("current")
_ForeFastIwfTxOctets_Type = Counter32
_ForeFastIwfTxOctets_Object = MibTableColumn
foreFastIwfTxOctets = _ForeFastIwfTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 2),
    _ForeFastIwfTxOctets_Type()
)
foreFastIwfTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIwfTxOctets.setStatus("current")
_ForeFastIwfTxPackets_Type = Counter32
_ForeFastIwfTxPackets_Object = MibTableColumn
foreFastIwfTxPackets = _ForeFastIwfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 3),
    _ForeFastIwfTxPackets_Type()
)
foreFastIwfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIwfTxPackets.setStatus("current")
_ForeFastIwfTxHdrLookupErr_Type = Counter32
_ForeFastIwfTxHdrLookupErr_Object = MibTableColumn
foreFastIwfTxHdrLookupErr = _ForeFastIwfTxHdrLookupErr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 4),
    _ForeFastIwfTxHdrLookupErr_Type()
)
foreFastIwfTxHdrLookupErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIwfTxHdrLookupErr.setStatus("current")
_ForeFastIwfTxResourceFail_Type = Counter32
_ForeFastIwfTxResourceFail_Object = MibTableColumn
foreFastIwfTxResourceFail = _ForeFastIwfTxResourceFail_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 5),
    _ForeFastIwfTxResourceFail_Type()
)
foreFastIwfTxResourceFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIwfTxResourceFail.setStatus("current")
_ForeFastIwfRxCells_Type = Counter32
_ForeFastIwfRxCells_Object = MibTableColumn
foreFastIwfRxCells = _ForeFastIwfRxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 6),
    _ForeFastIwfRxCells_Type()
)
foreFastIwfRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIwfRxCells.setStatus("current")
_ForeFastIwfRxOctets_Type = Counter32
_ForeFastIwfRxOctets_Object = MibTableColumn
foreFastIwfRxOctets = _ForeFastIwfRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 7),
    _ForeFastIwfRxOctets_Type()
)
foreFastIwfRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIwfRxOctets.setStatus("current")
_ForeFastIwfRxPackets_Type = Counter32
_ForeFastIwfRxPackets_Object = MibTableColumn
foreFastIwfRxPackets = _ForeFastIwfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 8),
    _ForeFastIwfRxPackets_Type()
)
foreFastIwfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIwfRxPackets.setStatus("current")
_ForeFastIwfRxHdrLookupErr_Type = Counter32
_ForeFastIwfRxHdrLookupErr_Object = MibTableColumn
foreFastIwfRxHdrLookupErr = _ForeFastIwfRxHdrLookupErr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 9),
    _ForeFastIwfRxHdrLookupErr_Type()
)
foreFastIwfRxHdrLookupErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIwfRxHdrLookupErr.setStatus("current")
_ForeFastIwfRxResourceFail_Type = Counter32
_ForeFastIwfRxResourceFail_Object = MibTableColumn
foreFastIwfRxResourceFail = _ForeFastIwfRxResourceFail_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 10),
    _ForeFastIwfRxResourceFail_Type()
)
foreFastIwfRxResourceFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreFastIwfRxResourceFail.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-FAST-MIB",
    **{"foreFastGroup": foreFastGroup,
       "foreFastIfTable": foreFastIfTable,
       "foreFastIfEntry": foreFastIfEntry,
       "foreFastIfFramingMode": foreFastIfFramingMode,
       "foreFastIfAdminStatus": foreFastIfAdminStatus,
       "foreFastIwfStatsTable": foreFastIwfStatsTable,
       "foreFastIwfStatsEntry": foreFastIwfStatsEntry,
       "foreFastIwfTxCells": foreFastIwfTxCells,
       "foreFastIwfTxOctets": foreFastIwfTxOctets,
       "foreFastIwfTxPackets": foreFastIwfTxPackets,
       "foreFastIwfTxHdrLookupErr": foreFastIwfTxHdrLookupErr,
       "foreFastIwfTxResourceFail": foreFastIwfTxResourceFail,
       "foreFastIwfRxCells": foreFastIwfRxCells,
       "foreFastIwfRxOctets": foreFastIwfRxOctets,
       "foreFastIwfRxPackets": foreFastIwfRxPackets,
       "foreFastIwfRxHdrLookupErr": foreFastIwfRxHdrLookupErr,
       "foreFastIwfRxResourceFail": foreFastIwfRxResourceFail}
)
