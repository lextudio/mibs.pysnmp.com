# SNMP MIB module (Juniper-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:22 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex")

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

juniHdlcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9)
)
juniHdlcMIB.setRevisions(
        ("2003-10-03 19:25",
         "2002-09-16 21:44",
         "2001-11-28 13:43",
         "2001-03-22 14:30",
         "2000-01-26 00:00",
         "1999-07-28 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniHdlcObjects_ObjectIdentity = ObjectIdentity
juniHdlcObjects = _JuniHdlcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1)
)
_JuniHdlcNextIfIndex_Type = JuniNextIfIndex
_JuniHdlcNextIfIndex_Object = MibScalar
juniHdlcNextIfIndex = _JuniHdlcNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 1),
    _JuniHdlcNextIfIndex_Type()
)
juniHdlcNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniHdlcNextIfIndex.setStatus("current")
_JuniHdlcIfTable_Object = MibTable
juniHdlcIfTable = _JuniHdlcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    juniHdlcIfTable.setStatus("current")
_JuniHdlcIfEntry_Object = MibTableRow
juniHdlcIfEntry = _JuniHdlcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1)
)
juniHdlcIfEntry.setIndexNames(
    (0, "Juniper-HDLC-MIB", "juniHdlcIfIndex"),
)
if mibBuilder.loadTexts:
    juniHdlcIfEntry.setStatus("current")
_JuniHdlcIfIndex_Type = InterfaceIndex
_JuniHdlcIfIndex_Object = MibTableColumn
juniHdlcIfIndex = _JuniHdlcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 1),
    _JuniHdlcIfIndex_Type()
)
juniHdlcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniHdlcIfIndex.setStatus("current")
_JuniHdlcIfRowStatus_Type = RowStatus
_JuniHdlcIfRowStatus_Object = MibTableColumn
juniHdlcIfRowStatus = _JuniHdlcIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 2),
    _JuniHdlcIfRowStatus_Type()
)
juniHdlcIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHdlcIfRowStatus.setStatus("current")
_JuniHdlcIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniHdlcIfLowerIfIndex_Object = MibTableColumn
juniHdlcIfLowerIfIndex = _JuniHdlcIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 3),
    _JuniHdlcIfLowerIfIndex_Type()
)
juniHdlcIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHdlcIfLowerIfIndex.setStatus("current")


class _JuniHdlcIfMtu_Type(Integer32):
    """Custom type juniHdlcIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32763),
    )


_JuniHdlcIfMtu_Type.__name__ = "Integer32"
_JuniHdlcIfMtu_Object = MibTableColumn
juniHdlcIfMtu = _JuniHdlcIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 4),
    _JuniHdlcIfMtu_Type()
)
juniHdlcIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHdlcIfMtu.setStatus("current")
if mibBuilder.loadTexts:
    juniHdlcIfMtu.setUnits("octets")


class _JuniHdlcIfMru_Type(Integer32):
    """Custom type juniHdlcIfMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32763),
    )


_JuniHdlcIfMru_Type.__name__ = "Integer32"
_JuniHdlcIfMru_Object = MibTableColumn
juniHdlcIfMru = _JuniHdlcIfMru_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 5),
    _JuniHdlcIfMru_Type()
)
juniHdlcIfMru.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHdlcIfMru.setStatus("current")
if mibBuilder.loadTexts:
    juniHdlcIfMru.setUnits("octets")


class _JuniHdlcIfCrcSize_Type(Integer32):
    """Custom type juniHdlcIfCrcSize based on Integer32"""
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


_JuniHdlcIfCrcSize_Type.__name__ = "Integer32"
_JuniHdlcIfCrcSize_Object = MibTableColumn
juniHdlcIfCrcSize = _JuniHdlcIfCrcSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 6),
    _JuniHdlcIfCrcSize_Type()
)
juniHdlcIfCrcSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHdlcIfCrcSize.setStatus("current")


class _JuniHdlcIfDataPolarity_Type(Integer32):
    """Custom type juniHdlcIfDataPolarity based on Integer32"""
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


_JuniHdlcIfDataPolarity_Type.__name__ = "Integer32"
_JuniHdlcIfDataPolarity_Object = MibTableColumn
juniHdlcIfDataPolarity = _JuniHdlcIfDataPolarity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 7),
    _JuniHdlcIfDataPolarity_Type()
)
juniHdlcIfDataPolarity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHdlcIfDataPolarity.setStatus("current")


class _JuniHdlcIfClockMode_Type(Integer32):
    """Custom type juniHdlcIfClockMode based on Integer32"""
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


_JuniHdlcIfClockMode_Type.__name__ = "Integer32"
_JuniHdlcIfClockMode_Object = MibTableColumn
juniHdlcIfClockMode = _JuniHdlcIfClockMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 8),
    _JuniHdlcIfClockMode_Type()
)
juniHdlcIfClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHdlcIfClockMode.setStatus("current")


class _JuniHdlcIfClockRate_Type(Integer32):
    """Custom type juniHdlcIfClockRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlcClockRate34At368Mhz", 1),
          ("hdlcClockRate44At736Mhz", 2),
          ("hdlcClockRateUnsupported", 0))
    )


_JuniHdlcIfClockRate_Type.__name__ = "Integer32"
_JuniHdlcIfClockRate_Object = MibTableColumn
juniHdlcIfClockRate = _JuniHdlcIfClockRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 9),
    _JuniHdlcIfClockRate_Type()
)
juniHdlcIfClockRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHdlcIfClockRate.setStatus("current")


class _JuniHdlcIfForceDteAck_Type(Integer32):
    """Custom type juniHdlcIfForceDteAck based on Integer32"""
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


_JuniHdlcIfForceDteAck_Type.__name__ = "Integer32"
_JuniHdlcIfForceDteAck_Object = MibTableColumn
juniHdlcIfForceDteAck = _JuniHdlcIfForceDteAck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 10),
    _JuniHdlcIfForceDteAck_Type()
)
juniHdlcIfForceDteAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHdlcIfForceDteAck.setStatus("current")


class _JuniHdlcIfIdleCharacter_Type(Integer32):
    """Custom type juniHdlcIfIdleCharacter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idleCharacterFlags", 0),
          ("idleCharacterMarks", 1))
    )


_JuniHdlcIfIdleCharacter_Type.__name__ = "Integer32"
_JuniHdlcIfIdleCharacter_Object = MibTableColumn
juniHdlcIfIdleCharacter = _JuniHdlcIfIdleCharacter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 11),
    _JuniHdlcIfIdleCharacter_Type()
)
juniHdlcIfIdleCharacter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniHdlcIfIdleCharacter.setStatus("current")
_JuniHdlcConformance_ObjectIdentity = ObjectIdentity
juniHdlcConformance = _JuniHdlcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4)
)
_JuniHdlcCompliances_ObjectIdentity = ObjectIdentity
juniHdlcCompliances = _JuniHdlcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1)
)
_JuniHdlcGroups_ObjectIdentity = ObjectIdentity
juniHdlcGroups = _JuniHdlcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2)
)

# Managed Objects groups

juniHdlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 1)
)
juniHdlcGroup.setObjects(
      *(("Juniper-HDLC-MIB", "juniHdlcNextIfIndex"),
        ("Juniper-HDLC-MIB", "juniHdlcIfRowStatus"),
        ("Juniper-HDLC-MIB", "juniHdlcIfLowerIfIndex"),
        ("Juniper-HDLC-MIB", "juniHdlcIfMtu"),
        ("Juniper-HDLC-MIB", "juniHdlcIfMru"),
        ("Juniper-HDLC-MIB", "juniHdlcIfCrcSize"))
)
if mibBuilder.loadTexts:
    juniHdlcGroup.setStatus("obsolete")

juniHdlcGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 2)
)
juniHdlcGroup2.setObjects(
      *(("Juniper-HDLC-MIB", "juniHdlcNextIfIndex"),
        ("Juniper-HDLC-MIB", "juniHdlcIfRowStatus"),
        ("Juniper-HDLC-MIB", "juniHdlcIfLowerIfIndex"),
        ("Juniper-HDLC-MIB", "juniHdlcIfMtu"),
        ("Juniper-HDLC-MIB", "juniHdlcIfMru"),
        ("Juniper-HDLC-MIB", "juniHdlcIfCrcSize"),
        ("Juniper-HDLC-MIB", "juniHdlcIfDataPolarity"))
)
if mibBuilder.loadTexts:
    juniHdlcGroup2.setStatus("obsolete")

juniHdlcGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 3)
)
juniHdlcGroup3.setObjects(
      *(("Juniper-HDLC-MIB", "juniHdlcNextIfIndex"),
        ("Juniper-HDLC-MIB", "juniHdlcIfRowStatus"),
        ("Juniper-HDLC-MIB", "juniHdlcIfLowerIfIndex"),
        ("Juniper-HDLC-MIB", "juniHdlcIfMtu"),
        ("Juniper-HDLC-MIB", "juniHdlcIfMru"),
        ("Juniper-HDLC-MIB", "juniHdlcIfCrcSize"),
        ("Juniper-HDLC-MIB", "juniHdlcIfDataPolarity"),
        ("Juniper-HDLC-MIB", "juniHdlcIfClockMode"),
        ("Juniper-HDLC-MIB", "juniHdlcIfClockRate"),
        ("Juniper-HDLC-MIB", "juniHdlcIfForceDteAck"))
)
if mibBuilder.loadTexts:
    juniHdlcGroup3.setStatus("obsolete")

juniHdlcGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 4)
)
juniHdlcGroup4.setObjects(
      *(("Juniper-HDLC-MIB", "juniHdlcNextIfIndex"),
        ("Juniper-HDLC-MIB", "juniHdlcIfRowStatus"),
        ("Juniper-HDLC-MIB", "juniHdlcIfLowerIfIndex"),
        ("Juniper-HDLC-MIB", "juniHdlcIfMtu"),
        ("Juniper-HDLC-MIB", "juniHdlcIfMru"),
        ("Juniper-HDLC-MIB", "juniHdlcIfCrcSize"),
        ("Juniper-HDLC-MIB", "juniHdlcIfDataPolarity"),
        ("Juniper-HDLC-MIB", "juniHdlcIfClockMode"),
        ("Juniper-HDLC-MIB", "juniHdlcIfClockRate"),
        ("Juniper-HDLC-MIB", "juniHdlcIfForceDteAck"),
        ("Juniper-HDLC-MIB", "juniHdlcIfIdleCharacter"))
)
if mibBuilder.loadTexts:
    juniHdlcGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniHdlcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniHdlcCompliance.setStatus(
        "obsolete"
    )

juniHdlcCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniHdlcCompliance2.setStatus(
        "obsolete"
    )

juniHdlcCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniHdlcCompliance3.setStatus(
        "obsolete"
    )

juniHdlcCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniHdlcCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-HDLC-MIB",
    **{"juniHdlcMIB": juniHdlcMIB,
       "juniHdlcObjects": juniHdlcObjects,
       "juniHdlcNextIfIndex": juniHdlcNextIfIndex,
       "juniHdlcIfTable": juniHdlcIfTable,
       "juniHdlcIfEntry": juniHdlcIfEntry,
       "juniHdlcIfIndex": juniHdlcIfIndex,
       "juniHdlcIfRowStatus": juniHdlcIfRowStatus,
       "juniHdlcIfLowerIfIndex": juniHdlcIfLowerIfIndex,
       "juniHdlcIfMtu": juniHdlcIfMtu,
       "juniHdlcIfMru": juniHdlcIfMru,
       "juniHdlcIfCrcSize": juniHdlcIfCrcSize,
       "juniHdlcIfDataPolarity": juniHdlcIfDataPolarity,
       "juniHdlcIfClockMode": juniHdlcIfClockMode,
       "juniHdlcIfClockRate": juniHdlcIfClockRate,
       "juniHdlcIfForceDteAck": juniHdlcIfForceDteAck,
       "juniHdlcIfIdleCharacter": juniHdlcIfIdleCharacter,
       "juniHdlcConformance": juniHdlcConformance,
       "juniHdlcCompliances": juniHdlcCompliances,
       "juniHdlcCompliance": juniHdlcCompliance,
       "juniHdlcCompliance2": juniHdlcCompliance2,
       "juniHdlcCompliance3": juniHdlcCompliance3,
       "juniHdlcCompliance4": juniHdlcCompliance4,
       "juniHdlcGroups": juniHdlcGroups,
       "juniHdlcGroup": juniHdlcGroup,
       "juniHdlcGroup2": juniHdlcGroup2,
       "juniHdlcGroup3": juniHdlcGroup3,
       "juniHdlcGroup4": juniHdlcGroup4}
)
