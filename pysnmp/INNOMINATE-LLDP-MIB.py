# SNMP MIB module (INNOMINATE-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INNOMINATE-LLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:25 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

innominateLldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7)
)
innominateLldpMIB.setRevisions(
        ("2005-08-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TimeFilter(TimeTicks, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_InnominateLLDPConfig_ObjectIdentity = ObjectIdentity
innominateLLDPConfig = _InnominateLLDPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 1)
)


class _InnominateLLDPAdminStatus_Type(Integer32):
    """Custom type innominateLLDPAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_InnominateLLDPAdminStatus_Type.__name__ = "Integer32"
_InnominateLLDPAdminStatus_Object = MibScalar
innominateLLDPAdminStatus = _InnominateLLDPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 1),
    _InnominateLLDPAdminStatus_Type()
)
innominateLLDPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    innominateLLDPAdminStatus.setStatus("current")
_InnominateLLDPInterfaceTable_Object = MibTable
innominateLLDPInterfaceTable = _InnominateLLDPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    innominateLLDPInterfaceTable.setStatus("current")
_InnominateLLDPIfEntry_Object = MibTableRow
innominateLLDPIfEntry = _InnominateLLDPIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1)
)
innominateLLDPIfEntry.setIndexNames(
    (0, "INNOMINATE-LLDP-MIB", "innominateLLDPIfaceGroupID"),
    (0, "INNOMINATE-LLDP-MIB", "innominateLLDPIfaceID"),
)
if mibBuilder.loadTexts:
    innominateLLDPIfEntry.setStatus("current")


class _InnominateLLDPIfaceGroupID_Type(Integer32):
    """Custom type innominateLLDPIfaceGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_InnominateLLDPIfaceGroupID_Type.__name__ = "Integer32"
_InnominateLLDPIfaceGroupID_Object = MibTableColumn
innominateLLDPIfaceGroupID = _InnominateLLDPIfaceGroupID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1, 1),
    _InnominateLLDPIfaceGroupID_Type()
)
innominateLLDPIfaceGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innominateLLDPIfaceGroupID.setStatus("current")


class _InnominateLLDPIfaceID_Type(Integer32):
    """Custom type innominateLLDPIfaceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_InnominateLLDPIfaceID_Type.__name__ = "Integer32"
_InnominateLLDPIfaceID_Object = MibTableColumn
innominateLLDPIfaceID = _InnominateLLDPIfaceID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1, 2),
    _InnominateLLDPIfaceID_Type()
)
innominateLLDPIfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innominateLLDPIfaceID.setStatus("current")


class _InnominateLLDPIfaceHirmaMode_Type(Integer32):
    """Custom type innominateLLDPIfaceHirmaMode based on Integer32"""
    defaultValue = 3

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
        *(("disabled", 4),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("txOnly", 1))
    )


_InnominateLLDPIfaceHirmaMode_Type.__name__ = "Integer32"
_InnominateLLDPIfaceHirmaMode_Object = MibTableColumn
innominateLLDPIfaceHirmaMode = _InnominateLLDPIfaceHirmaMode_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1, 3),
    _InnominateLLDPIfaceHirmaMode_Type()
)
innominateLLDPIfaceHirmaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    innominateLLDPIfaceHirmaMode.setStatus("current")


class _InnominateLLDPIfaceFDBMode_Type(Integer32):
    """Custom type innominateLLDPIfaceFDBMode based on Integer32"""
    defaultValue = 1

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
        *(("autoDetect", 4),
          ("both", 3),
          ("lldpOnly", 1),
          ("macOnly", 2))
    )


_InnominateLLDPIfaceFDBMode_Type.__name__ = "Integer32"
_InnominateLLDPIfaceFDBMode_Object = MibTableColumn
innominateLLDPIfaceFDBMode = _InnominateLLDPIfaceFDBMode_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1, 4),
    _InnominateLLDPIfaceFDBMode_Type()
)
innominateLLDPIfaceFDBMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    innominateLLDPIfaceFDBMode.setStatus("current")


class _InnominateLLDPIfaceMaxNeighbors_Type(Integer32):
    """Custom type innominateLLDPIfaceMaxNeighbors based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_InnominateLLDPIfaceMaxNeighbors_Type.__name__ = "Integer32"
_InnominateLLDPIfaceMaxNeighbors_Object = MibTableColumn
innominateLLDPIfaceMaxNeighbors = _InnominateLLDPIfaceMaxNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 1, 2, 1, 5),
    _InnominateLLDPIfaceMaxNeighbors_Type()
)
innominateLLDPIfaceMaxNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    innominateLLDPIfaceMaxNeighbors.setStatus("current")
_InnominateLLDPStatistics_ObjectIdentity = ObjectIdentity
innominateLLDPStatistics = _InnominateLLDPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 2)
)
_InnominateLLDPStatsIfTable_Object = MibTable
innominateLLDPStatsIfTable = _InnominateLLDPStatsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1)
)
if mibBuilder.loadTexts:
    innominateLLDPStatsIfTable.setStatus("current")
_InnominateLLDPStatsIfEntry_Object = MibTableRow
innominateLLDPStatsIfEntry = _InnominateLLDPStatsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1)
)
innominateLLDPStatsIfEntry.setIndexNames(
    (0, "INNOMINATE-LLDP-MIB", "innominateLLDPStatsIfaceGroupID"),
    (0, "INNOMINATE-LLDP-MIB", "innominateLLDPStatsIfaceID"),
)
if mibBuilder.loadTexts:
    innominateLLDPStatsIfEntry.setStatus("current")


class _InnominateLLDPStatsIfaceGroupID_Type(Integer32):
    """Custom type innominateLLDPStatsIfaceGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_InnominateLLDPStatsIfaceGroupID_Type.__name__ = "Integer32"
_InnominateLLDPStatsIfaceGroupID_Object = MibTableColumn
innominateLLDPStatsIfaceGroupID = _InnominateLLDPStatsIfaceGroupID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 1),
    _InnominateLLDPStatsIfaceGroupID_Type()
)
innominateLLDPStatsIfaceGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innominateLLDPStatsIfaceGroupID.setStatus("current")


class _InnominateLLDPStatsIfaceID_Type(Integer32):
    """Custom type innominateLLDPStatsIfaceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_InnominateLLDPStatsIfaceID_Type.__name__ = "Integer32"
_InnominateLLDPStatsIfaceID_Object = MibTableColumn
innominateLLDPStatsIfaceID = _InnominateLLDPStatsIfaceID_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 2),
    _InnominateLLDPStatsIfaceID_Type()
)
innominateLLDPStatsIfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innominateLLDPStatsIfaceID.setStatus("current")
_InnominateLLDPStatsIfaceTotalFDBEntryCount_Type = Counter32
_InnominateLLDPStatsIfaceTotalFDBEntryCount_Object = MibTableColumn
innominateLLDPStatsIfaceTotalFDBEntryCount = _InnominateLLDPStatsIfaceTotalFDBEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 3),
    _InnominateLLDPStatsIfaceTotalFDBEntryCount_Type()
)
innominateLLDPStatsIfaceTotalFDBEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innominateLLDPStatsIfaceTotalFDBEntryCount.setStatus("current")
_InnominateLLDPStatsIfaceTotalEntryCount_Type = Counter32
_InnominateLLDPStatsIfaceTotalEntryCount_Object = MibTableColumn
innominateLLDPStatsIfaceTotalEntryCount = _InnominateLLDPStatsIfaceTotalEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 4),
    _InnominateLLDPStatsIfaceTotalEntryCount_Type()
)
innominateLLDPStatsIfaceTotalEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innominateLLDPStatsIfaceTotalEntryCount.setStatus("current")
_InnominateLLDPStatsIfaceIEEEEntryCount_Type = Counter32
_InnominateLLDPStatsIfaceIEEEEntryCount_Object = MibTableColumn
innominateLLDPStatsIfaceIEEEEntryCount = _InnominateLLDPStatsIfaceIEEEEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 5),
    _InnominateLLDPStatsIfaceIEEEEntryCount_Type()
)
innominateLLDPStatsIfaceIEEEEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innominateLLDPStatsIfaceIEEEEntryCount.setStatus("current")
_InnominateLLDPStatsIfaceHirmaEntryCount_Type = Counter32
_InnominateLLDPStatsIfaceHirmaEntryCount_Object = MibTableColumn
innominateLLDPStatsIfaceHirmaEntryCount = _InnominateLLDPStatsIfaceHirmaEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 6),
    _InnominateLLDPStatsIfaceHirmaEntryCount_Type()
)
innominateLLDPStatsIfaceHirmaEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innominateLLDPStatsIfaceHirmaEntryCount.setStatus("current")
_InnominateLLDPStatsIfaceFDBEntryCount_Type = Counter32
_InnominateLLDPStatsIfaceFDBEntryCount_Object = MibTableColumn
innominateLLDPStatsIfaceFDBEntryCount = _InnominateLLDPStatsIfaceFDBEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 15450, 3, 7, 2, 1, 1, 7),
    _InnominateLLDPStatsIfaceFDBEntryCount_Type()
)
innominateLLDPStatsIfaceFDBEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innominateLLDPStatsIfaceFDBEntryCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INNOMINATE-LLDP-MIB",
    **{"TimeFilter": TimeFilter,
       "innominateLldpMIB": innominateLldpMIB,
       "innominateLLDPConfig": innominateLLDPConfig,
       "innominateLLDPAdminStatus": innominateLLDPAdminStatus,
       "innominateLLDPInterfaceTable": innominateLLDPInterfaceTable,
       "innominateLLDPIfEntry": innominateLLDPIfEntry,
       "innominateLLDPIfaceGroupID": innominateLLDPIfaceGroupID,
       "innominateLLDPIfaceID": innominateLLDPIfaceID,
       "innominateLLDPIfaceHirmaMode": innominateLLDPIfaceHirmaMode,
       "innominateLLDPIfaceFDBMode": innominateLLDPIfaceFDBMode,
       "innominateLLDPIfaceMaxNeighbors": innominateLLDPIfaceMaxNeighbors,
       "innominateLLDPStatistics": innominateLLDPStatistics,
       "innominateLLDPStatsIfTable": innominateLLDPStatsIfTable,
       "innominateLLDPStatsIfEntry": innominateLLDPStatsIfEntry,
       "innominateLLDPStatsIfaceGroupID": innominateLLDPStatsIfaceGroupID,
       "innominateLLDPStatsIfaceID": innominateLLDPStatsIfaceID,
       "innominateLLDPStatsIfaceTotalFDBEntryCount": innominateLLDPStatsIfaceTotalFDBEntryCount,
       "innominateLLDPStatsIfaceTotalEntryCount": innominateLLDPStatsIfaceTotalEntryCount,
       "innominateLLDPStatsIfaceIEEEEntryCount": innominateLLDPStatsIfaceIEEEEntryCount,
       "innominateLLDPStatsIfaceHirmaEntryCount": innominateLLDPStatsIfaceHirmaEntryCount,
       "innominateLLDPStatsIfaceFDBEntryCount": innominateLLDPStatsIfaceFDBEntryCount}
)
