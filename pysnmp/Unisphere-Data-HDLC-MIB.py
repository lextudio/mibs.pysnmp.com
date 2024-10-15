# SNMP MIB module (Unisphere-Data-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:48 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdHdlcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9)
)
usdHdlcMIB.setRevisions(
        ("2001-11-28 13:43",
         "2001-03-22 14:30",
         "2000-01-26 00:00",
         "1999-07-28 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdHdlcObjects_ObjectIdentity = ObjectIdentity
usdHdlcObjects = _UsdHdlcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1)
)
_UsdHdlcNextIfIndex_Type = UsdNextIfIndex
_UsdHdlcNextIfIndex_Object = MibScalar
usdHdlcNextIfIndex = _UsdHdlcNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 1),
    _UsdHdlcNextIfIndex_Type()
)
usdHdlcNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdHdlcNextIfIndex.setStatus("current")
_UsdHdlcIfTable_Object = MibTable
usdHdlcIfTable = _UsdHdlcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    usdHdlcIfTable.setStatus("current")
_UsdHdlcIfEntry_Object = MibTableRow
usdHdlcIfEntry = _UsdHdlcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1)
)
usdHdlcIfEntry.setIndexNames(
    (0, "Unisphere-Data-HDLC-MIB", "usdHdlcIfIndex"),
)
if mibBuilder.loadTexts:
    usdHdlcIfEntry.setStatus("current")
_UsdHdlcIfIndex_Type = InterfaceIndex
_UsdHdlcIfIndex_Object = MibTableColumn
usdHdlcIfIndex = _UsdHdlcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 1),
    _UsdHdlcIfIndex_Type()
)
usdHdlcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdHdlcIfIndex.setStatus("current")
_UsdHdlcIfRowStatus_Type = RowStatus
_UsdHdlcIfRowStatus_Object = MibTableColumn
usdHdlcIfRowStatus = _UsdHdlcIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 2),
    _UsdHdlcIfRowStatus_Type()
)
usdHdlcIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdHdlcIfRowStatus.setStatus("current")
_UsdHdlcIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdHdlcIfLowerIfIndex_Object = MibTableColumn
usdHdlcIfLowerIfIndex = _UsdHdlcIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 3),
    _UsdHdlcIfLowerIfIndex_Type()
)
usdHdlcIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdHdlcIfLowerIfIndex.setStatus("current")


class _UsdHdlcIfMtu_Type(Integer32):
    """Custom type usdHdlcIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32763),
    )


_UsdHdlcIfMtu_Type.__name__ = "Integer32"
_UsdHdlcIfMtu_Object = MibTableColumn
usdHdlcIfMtu = _UsdHdlcIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 4),
    _UsdHdlcIfMtu_Type()
)
usdHdlcIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdHdlcIfMtu.setStatus("current")
if mibBuilder.loadTexts:
    usdHdlcIfMtu.setUnits("octets")


class _UsdHdlcIfMru_Type(Integer32):
    """Custom type usdHdlcIfMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32763),
    )


_UsdHdlcIfMru_Type.__name__ = "Integer32"
_UsdHdlcIfMru_Object = MibTableColumn
usdHdlcIfMru = _UsdHdlcIfMru_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 5),
    _UsdHdlcIfMru_Type()
)
usdHdlcIfMru.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdHdlcIfMru.setStatus("current")
if mibBuilder.loadTexts:
    usdHdlcIfMru.setUnits("octets")


class _UsdHdlcIfCrcSize_Type(Integer32):
    """Custom type usdHdlcIfCrcSize based on Integer32"""
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


_UsdHdlcIfCrcSize_Type.__name__ = "Integer32"
_UsdHdlcIfCrcSize_Object = MibTableColumn
usdHdlcIfCrcSize = _UsdHdlcIfCrcSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 6),
    _UsdHdlcIfCrcSize_Type()
)
usdHdlcIfCrcSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdHdlcIfCrcSize.setStatus("current")


class _UsdHdlcIfDataPolarity_Type(Integer32):
    """Custom type usdHdlcIfDataPolarity based on Integer32"""
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


_UsdHdlcIfDataPolarity_Type.__name__ = "Integer32"
_UsdHdlcIfDataPolarity_Object = MibTableColumn
usdHdlcIfDataPolarity = _UsdHdlcIfDataPolarity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 7),
    _UsdHdlcIfDataPolarity_Type()
)
usdHdlcIfDataPolarity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdHdlcIfDataPolarity.setStatus("current")


class _UsdHdlcIfClockMode_Type(Integer32):
    """Custom type usdHdlcIfClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlcClockInternal", 1),
          ("hdlcClockLine", 2),
          ("hdlcClockUnsupported", 0))
    )


_UsdHdlcIfClockMode_Type.__name__ = "Integer32"
_UsdHdlcIfClockMode_Object = MibTableColumn
usdHdlcIfClockMode = _UsdHdlcIfClockMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 8),
    _UsdHdlcIfClockMode_Type()
)
usdHdlcIfClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdHdlcIfClockMode.setStatus("current")


class _UsdHdlcIfClockRate_Type(Integer32):
    """Custom type usdHdlcIfClockRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlcClockRate34-368Mhz", 1),
          ("hdlcClockRate44-736Mhz", 2),
          ("hdlcClockRateUnsupported", 0))
    )


_UsdHdlcIfClockRate_Type.__name__ = "Integer32"
_UsdHdlcIfClockRate_Object = MibTableColumn
usdHdlcIfClockRate = _UsdHdlcIfClockRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 9),
    _UsdHdlcIfClockRate_Type()
)
usdHdlcIfClockRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdHdlcIfClockRate.setStatus("current")


class _UsdHdlcIfForceDteAck_Type(Integer32):
    """Custom type usdHdlcIfForceDteAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceDteAckForced", 2),
          ("forceDteAckNormal", 1),
          ("forceDteAckUnsupported", 0))
    )


_UsdHdlcIfForceDteAck_Type.__name__ = "Integer32"
_UsdHdlcIfForceDteAck_Object = MibTableColumn
usdHdlcIfForceDteAck = _UsdHdlcIfForceDteAck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 10),
    _UsdHdlcIfForceDteAck_Type()
)
usdHdlcIfForceDteAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdHdlcIfForceDteAck.setStatus("current")
_UsdHdlcConformance_ObjectIdentity = ObjectIdentity
usdHdlcConformance = _UsdHdlcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4)
)
_UsdHdlcCompliances_ObjectIdentity = ObjectIdentity
usdHdlcCompliances = _UsdHdlcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1)
)
_UsdHdlcGroups_ObjectIdentity = ObjectIdentity
usdHdlcGroups = _UsdHdlcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2)
)

# Managed Objects groups

usdHdlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 1)
)
usdHdlcGroup.setObjects(
      *(("Unisphere-Data-HDLC-MIB", "usdHdlcNextIfIndex"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfRowStatus"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfLowerIfIndex"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMtu"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMru"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfCrcSize"))
)
if mibBuilder.loadTexts:
    usdHdlcGroup.setStatus("obsolete")

usdHdlcGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 2)
)
usdHdlcGroup2.setObjects(
      *(("Unisphere-Data-HDLC-MIB", "usdHdlcNextIfIndex"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfRowStatus"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfLowerIfIndex"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMtu"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMru"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfCrcSize"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfDataPolarity"))
)
if mibBuilder.loadTexts:
    usdHdlcGroup2.setStatus("obsolete")

usdHdlcGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 3)
)
usdHdlcGroup3.setObjects(
      *(("Unisphere-Data-HDLC-MIB", "usdHdlcNextIfIndex"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfRowStatus"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfLowerIfIndex"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMtu"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMru"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfCrcSize"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfDataPolarity"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfClockMode"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfClockRate"),
        ("Unisphere-Data-HDLC-MIB", "usdHdlcIfForceDteAck"))
)
if mibBuilder.loadTexts:
    usdHdlcGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdHdlcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdHdlcCompliance.setStatus(
        "obsolete"
    )

usdHdlcCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdHdlcCompliance2.setStatus(
        "obsolete"
    )

usdHdlcCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdHdlcCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-HDLC-MIB",
    **{"usdHdlcMIB": usdHdlcMIB,
       "usdHdlcObjects": usdHdlcObjects,
       "usdHdlcNextIfIndex": usdHdlcNextIfIndex,
       "usdHdlcIfTable": usdHdlcIfTable,
       "usdHdlcIfEntry": usdHdlcIfEntry,
       "usdHdlcIfIndex": usdHdlcIfIndex,
       "usdHdlcIfRowStatus": usdHdlcIfRowStatus,
       "usdHdlcIfLowerIfIndex": usdHdlcIfLowerIfIndex,
       "usdHdlcIfMtu": usdHdlcIfMtu,
       "usdHdlcIfMru": usdHdlcIfMru,
       "usdHdlcIfCrcSize": usdHdlcIfCrcSize,
       "usdHdlcIfDataPolarity": usdHdlcIfDataPolarity,
       "usdHdlcIfClockMode": usdHdlcIfClockMode,
       "usdHdlcIfClockRate": usdHdlcIfClockRate,
       "usdHdlcIfForceDteAck": usdHdlcIfForceDteAck,
       "usdHdlcConformance": usdHdlcConformance,
       "usdHdlcCompliances": usdHdlcCompliances,
       "usdHdlcCompliance": usdHdlcCompliance,
       "usdHdlcCompliance2": usdHdlcCompliance2,
       "usdHdlcCompliance3": usdHdlcCompliance3,
       "usdHdlcGroups": usdHdlcGroups,
       "usdHdlcGroup": usdHdlcGroup,
       "usdHdlcGroup2": usdHdlcGroup2,
       "usdHdlcGroup3": usdHdlcGroup3}
)
