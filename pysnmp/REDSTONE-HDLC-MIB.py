# SNMP MIB module (REDSTONE-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:39 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsNextIfIndex,) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsNextIfIndex")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rsHdlcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9)
)
rsHdlcMIB.setRevisions(
        ("1999-07-28 00:00",
         "1999-07-14 00:00",
         "1998-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsHdlcObjects_ObjectIdentity = ObjectIdentity
rsHdlcObjects = _RsHdlcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1)
)
_RsHdlcNextIfIndex_Type = RsNextIfIndex
_RsHdlcNextIfIndex_Object = MibScalar
rsHdlcNextIfIndex = _RsHdlcNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 1),
    _RsHdlcNextIfIndex_Type()
)
rsHdlcNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsHdlcNextIfIndex.setStatus("current")
_RsHdlcIfTable_Object = MibTable
rsHdlcIfTable = _RsHdlcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    rsHdlcIfTable.setStatus("current")
_RsHdlcIfEntry_Object = MibTableRow
rsHdlcIfEntry = _RsHdlcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1)
)
rsHdlcIfEntry.setIndexNames(
    (0, "REDSTONE-HDLC-MIB", "rsHdlcIfIndex"),
)
if mibBuilder.loadTexts:
    rsHdlcIfEntry.setStatus("current")
_RsHdlcIfIndex_Type = InterfaceIndex
_RsHdlcIfIndex_Object = MibTableColumn
rsHdlcIfIndex = _RsHdlcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 1),
    _RsHdlcIfIndex_Type()
)
rsHdlcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsHdlcIfIndex.setStatus("current")
_RsHdlcIfRowStatus_Type = RowStatus
_RsHdlcIfRowStatus_Object = MibTableColumn
rsHdlcIfRowStatus = _RsHdlcIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 2),
    _RsHdlcIfRowStatus_Type()
)
rsHdlcIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsHdlcIfRowStatus.setStatus("current")
_RsHdlcIfLowerIfIndex_Type = InterfaceIndexOrZero
_RsHdlcIfLowerIfIndex_Object = MibTableColumn
rsHdlcIfLowerIfIndex = _RsHdlcIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 3),
    _RsHdlcIfLowerIfIndex_Type()
)
rsHdlcIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsHdlcIfLowerIfIndex.setStatus("current")


class _RsHdlcIfMtu_Type(Integer32):
    """Custom type rsHdlcIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65533),
    )


_RsHdlcIfMtu_Type.__name__ = "Integer32"
_RsHdlcIfMtu_Object = MibTableColumn
rsHdlcIfMtu = _RsHdlcIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 4),
    _RsHdlcIfMtu_Type()
)
rsHdlcIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsHdlcIfMtu.setStatus("current")
if mibBuilder.loadTexts:
    rsHdlcIfMtu.setUnits("octets")


class _RsHdlcIfMru_Type(Integer32):
    """Custom type rsHdlcIfMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65533),
    )


_RsHdlcIfMru_Type.__name__ = "Integer32"
_RsHdlcIfMru_Object = MibTableColumn
rsHdlcIfMru = _RsHdlcIfMru_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 5),
    _RsHdlcIfMru_Type()
)
rsHdlcIfMru.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsHdlcIfMru.setStatus("current")
if mibBuilder.loadTexts:
    rsHdlcIfMru.setUnits("octets")


class _RsHdlcIfCrcSize_Type(Integer32):
    """Custom type rsHdlcIfCrcSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2),
          ("none", 0))
    )


_RsHdlcIfCrcSize_Type.__name__ = "Integer32"
_RsHdlcIfCrcSize_Object = MibTableColumn
rsHdlcIfCrcSize = _RsHdlcIfCrcSize_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 6),
    _RsHdlcIfCrcSize_Type()
)
rsHdlcIfCrcSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsHdlcIfCrcSize.setStatus("current")


class _RsHdlcIfDataPolarity_Type(Integer32):
    """Custom type rsHdlcIfDataPolarity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 1),
          ("normal", 0))
    )


_RsHdlcIfDataPolarity_Type.__name__ = "Integer32"
_RsHdlcIfDataPolarity_Object = MibTableColumn
rsHdlcIfDataPolarity = _RsHdlcIfDataPolarity_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 7),
    _RsHdlcIfDataPolarity_Type()
)
rsHdlcIfDataPolarity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsHdlcIfDataPolarity.setStatus("current")
_RsHdlcConformance_ObjectIdentity = ObjectIdentity
rsHdlcConformance = _RsHdlcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 4)
)
_RsHdlcCompliances_ObjectIdentity = ObjectIdentity
rsHdlcCompliances = _RsHdlcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 1)
)
_RsHdlcGroups_ObjectIdentity = ObjectIdentity
rsHdlcGroups = _RsHdlcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 2)
)

# Managed Objects groups

rsHdlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 2, 1)
)
rsHdlcGroup.setObjects(
      *(("REDSTONE-HDLC-MIB", "rsHdlcNextIfIndex"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfRowStatus"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfLowerIfIndex"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfMtu"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfMru"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfCrcSize"))
)
if mibBuilder.loadTexts:
    rsHdlcGroup.setStatus("obsolete")

rsHdlcGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 2, 2)
)
rsHdlcGroup2.setObjects(
      *(("REDSTONE-HDLC-MIB", "rsHdlcNextIfIndex"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfRowStatus"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfLowerIfIndex"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfMtu"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfMru"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfCrcSize"),
        ("REDSTONE-HDLC-MIB", "rsHdlcIfDataPolarity"))
)
if mibBuilder.loadTexts:
    rsHdlcGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsHdlcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsHdlcCompliance.setStatus(
        "obsolete"
    )

rsHdlcCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 1, 2)
)
if mibBuilder.loadTexts:
    rsHdlcCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-HDLC-MIB",
    **{"rsHdlcMIB": rsHdlcMIB,
       "rsHdlcObjects": rsHdlcObjects,
       "rsHdlcNextIfIndex": rsHdlcNextIfIndex,
       "rsHdlcIfTable": rsHdlcIfTable,
       "rsHdlcIfEntry": rsHdlcIfEntry,
       "rsHdlcIfIndex": rsHdlcIfIndex,
       "rsHdlcIfRowStatus": rsHdlcIfRowStatus,
       "rsHdlcIfLowerIfIndex": rsHdlcIfLowerIfIndex,
       "rsHdlcIfMtu": rsHdlcIfMtu,
       "rsHdlcIfMru": rsHdlcIfMru,
       "rsHdlcIfCrcSize": rsHdlcIfCrcSize,
       "rsHdlcIfDataPolarity": rsHdlcIfDataPolarity,
       "rsHdlcConformance": rsHdlcConformance,
       "rsHdlcCompliances": rsHdlcCompliances,
       "rsHdlcCompliance": rsHdlcCompliance,
       "rsHdlcCompliance2": rsHdlcCompliance2,
       "rsHdlcGroups": rsHdlcGroups,
       "rsHdlcGroup": rsHdlcGroup,
       "rsHdlcGroup2": rsHdlcGroup2}
)
