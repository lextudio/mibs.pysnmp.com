# SNMP MIB module (Fore-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:02 2024
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

(trapLogIndex,) = mibBuilder.importSymbols(
    "Fore-TrapLog-MIB",
    "trapLogIndex")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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

_ForeHdlcIfGroup_ObjectIdentity = ObjectIdentity
foreHdlcIfGroup = _ForeHdlcIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20)
)
_ForeHdlcIfTable_Object = MibTable
foreHdlcIfTable = _ForeHdlcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    foreHdlcIfTable.setStatus("current")
_ForeHdlcIfEntry_Object = MibTableRow
foreHdlcIfEntry = _ForeHdlcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 1, 1)
)
foreHdlcIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreHdlcIfEntry.setStatus("current")


class _ForeHdlcIfPayloadType_Type(Integer32):
    """Custom type foreHdlcIfPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("ppp", 2))
    )


_ForeHdlcIfPayloadType_Type.__name__ = "Integer32"
_ForeHdlcIfPayloadType_Object = MibTableColumn
foreHdlcIfPayloadType = _ForeHdlcIfPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 1, 1, 1),
    _ForeHdlcIfPayloadType_Type()
)
foreHdlcIfPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreHdlcIfPayloadType.setStatus("current")


class _ForeHdlcIfAdminStatus_Type(Integer32):
    """Custom type foreHdlcIfAdminStatus based on Integer32"""
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


_ForeHdlcIfAdminStatus_Type.__name__ = "Integer32"
_ForeHdlcIfAdminStatus_Object = MibTableColumn
foreHdlcIfAdminStatus = _ForeHdlcIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 1, 1, 2),
    _ForeHdlcIfAdminStatus_Type()
)
foreHdlcIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreHdlcIfAdminStatus.setStatus("current")


class _ForeHdlcIfFcsWidth_Type(Integer32):
    """Custom type foreHdlcIfFcsWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("fcs16", 16),
          ("fcs32", 32))
    )


_ForeHdlcIfFcsWidth_Type.__name__ = "Integer32"
_ForeHdlcIfFcsWidth_Object = MibTableColumn
foreHdlcIfFcsWidth = _ForeHdlcIfFcsWidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 1, 1, 3),
    _ForeHdlcIfFcsWidth_Type()
)
foreHdlcIfFcsWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreHdlcIfFcsWidth.setStatus("current")
_ForeHdlcStatsTable_Object = MibTable
foreHdlcStatsTable = _ForeHdlcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 2)
)
if mibBuilder.loadTexts:
    foreHdlcStatsTable.setStatus("current")
_ForeHdlcStatsEntry_Object = MibTableRow
foreHdlcStatsEntry = _ForeHdlcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 2, 1)
)
foreHdlcStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreHdlcStatsEntry.setStatus("current")
_ForeHdlcIfTxPackets_Type = Counter32
_ForeHdlcIfTxPackets_Object = MibTableColumn
foreHdlcIfTxPackets = _ForeHdlcIfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 2, 1, 1),
    _ForeHdlcIfTxPackets_Type()
)
foreHdlcIfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreHdlcIfTxPackets.setStatus("current")
_ForeHdlcIfTxOctets_Type = Counter32
_ForeHdlcIfTxOctets_Object = MibTableColumn
foreHdlcIfTxOctets = _ForeHdlcIfTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 2, 1, 2),
    _ForeHdlcIfTxOctets_Type()
)
foreHdlcIfTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreHdlcIfTxOctets.setStatus("current")
_ForeHdlcIfRxPackets_Type = Counter32
_ForeHdlcIfRxPackets_Object = MibTableColumn
foreHdlcIfRxPackets = _ForeHdlcIfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 2, 1, 3),
    _ForeHdlcIfRxPackets_Type()
)
foreHdlcIfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreHdlcIfRxPackets.setStatus("current")
_ForeHdlcIfRxOctets_Type = Counter32
_ForeHdlcIfRxOctets_Object = MibTableColumn
foreHdlcIfRxOctets = _ForeHdlcIfRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 2, 1, 4),
    _ForeHdlcIfRxOctets_Type()
)
foreHdlcIfRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreHdlcIfRxOctets.setStatus("current")
_ForeHdlcIfChecksumErrors_Type = Counter32
_ForeHdlcIfChecksumErrors_Object = MibTableColumn
foreHdlcIfChecksumErrors = _ForeHdlcIfChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 2, 1, 5),
    _ForeHdlcIfChecksumErrors_Type()
)
foreHdlcIfChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreHdlcIfChecksumErrors.setStatus("current")


class _ForeHdlcIfLossOfFrame_Type(Integer32):
    """Custom type foreHdlcIfLossOfFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ForeHdlcIfLossOfFrame_Type.__name__ = "Integer32"
_ForeHdlcIfLossOfFrame_Object = MibTableColumn
foreHdlcIfLossOfFrame = _ForeHdlcIfLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 2, 1, 6),
    _ForeHdlcIfLossOfFrame_Type()
)
foreHdlcIfLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreHdlcIfLossOfFrame.setStatus("current")

# Managed Objects groups


# Notification objects

foreHdlcLOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 0, 1)
)
foreHdlcLOFDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreHdlcLOFDetected.setStatus(
        "current"
    )

foreHdlcLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 20, 0, 2)
)
foreHdlcLOFCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreHdlcLOFCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-HDLC-MIB",
    **{"foreHdlcIfGroup": foreHdlcIfGroup,
       "foreHdlcLOFDetected": foreHdlcLOFDetected,
       "foreHdlcLOFCleared": foreHdlcLOFCleared,
       "foreHdlcIfTable": foreHdlcIfTable,
       "foreHdlcIfEntry": foreHdlcIfEntry,
       "foreHdlcIfPayloadType": foreHdlcIfPayloadType,
       "foreHdlcIfAdminStatus": foreHdlcIfAdminStatus,
       "foreHdlcIfFcsWidth": foreHdlcIfFcsWidth,
       "foreHdlcStatsTable": foreHdlcStatsTable,
       "foreHdlcStatsEntry": foreHdlcStatsEntry,
       "foreHdlcIfTxPackets": foreHdlcIfTxPackets,
       "foreHdlcIfTxOctets": foreHdlcIfTxOctets,
       "foreHdlcIfRxPackets": foreHdlcIfRxPackets,
       "foreHdlcIfRxOctets": foreHdlcIfRxOctets,
       "foreHdlcIfChecksumErrors": foreHdlcIfChecksumErrors,
       "foreHdlcIfLossOfFrame": foreHdlcIfLossOfFrame}
)
