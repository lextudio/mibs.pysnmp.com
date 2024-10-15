# SNMP MIB module (A3COM-PORTPATH-R6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-PORTPATH-R6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:39 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComPath_ObjectIdentity = ObjectIdentity
a3ComPath = _A3ComPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 16)
)
_A3ComPathNumber_Type = Integer32
_A3ComPathNumber_Object = MibScalar
a3ComPathNumber = _A3ComPathNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 1),
    _A3ComPathNumber_Type()
)
a3ComPathNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathNumber.setStatus("mandatory")
_A3ComPathTable_Object = MibTable
a3ComPathTable = _A3ComPathTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2)
)
if mibBuilder.loadTexts:
    a3ComPathTable.setStatus("mandatory")
_A3ComPathEntry_Object = MibTableRow
a3ComPathEntry = _A3ComPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1)
)
a3ComPathEntry.setIndexNames(
    (0, "A3COM-PORTPATH-R6-MIB", "a3ComPathIndex"),
)
if mibBuilder.loadTexts:
    a3ComPathEntry.setStatus("mandatory")
_A3ComPathIndex_Type = Integer32
_A3ComPathIndex_Object = MibTableColumn
a3ComPathIndex = _A3ComPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 1),
    _A3ComPathIndex_Type()
)
a3ComPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathIndex.setStatus("mandatory")


class _A3ComPathName_Type(DisplayString):
    """Custom type a3ComPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_A3ComPathName_Type.__name__ = "DisplayString"
_A3ComPathName_Object = MibTableColumn
a3ComPathName = _A3ComPathName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 2),
    _A3ComPathName_Type()
)
a3ComPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathName.setStatus("mandatory")
_A3ComPathPort_Type = Integer32
_A3ComPathPort_Object = MibTableColumn
a3ComPathPort = _A3ComPathPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 3),
    _A3ComPathPort_Type()
)
a3ComPathPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathPort.setStatus("mandatory")


class _A3ComPathItcmOption_Type(Integer32):
    """Custom type a3ComPathItcmOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 1),
          ("incompatible", 2))
    )


_A3ComPathItcmOption_Type.__name__ = "Integer32"
_A3ComPathItcmOption_Object = MibTableColumn
a3ComPathItcmOption = _A3ComPathItcmOption_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 4),
    _A3ComPathItcmOption_Type()
)
a3ComPathItcmOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathItcmOption.setStatus("mandatory")


class _A3ComPathT1Mode_Type(Integer32):
    """Custom type a3ComPathT1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ComPathT1Mode_Type.__name__ = "Integer32"
_A3ComPathT1Mode_Object = MibTableColumn
a3ComPathT1Mode = _A3ComPathT1Mode_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 5),
    _A3ComPathT1Mode_Type()
)
a3ComPathT1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathT1Mode.setStatus("mandatory")


class _A3ComPathCryptoResync_Type(Integer32):
    """Custom type a3ComPathCryptoResync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ComPathCryptoResync_Type.__name__ = "Integer32"
_A3ComPathCryptoResync_Object = MibTableColumn
a3ComPathCryptoResync = _A3ComPathCryptoResync_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 6),
    _A3ComPathCryptoResync_Type()
)
a3ComPathCryptoResync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathCryptoResync.setStatus("mandatory")


class _A3ComPathCRC_Type(Integer32):
    """Custom type a3ComPathCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 16),
          ("crc32", 32))
    )


_A3ComPathCRC_Type.__name__ = "Integer32"
_A3ComPathCRC_Object = MibTableColumn
a3ComPathCRC = _A3ComPathCRC_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 7),
    _A3ComPathCRC_Type()
)
a3ComPathCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathCRC.setStatus("mandatory")


class _A3ComPathAdminStatus_Type(Integer32):
    """Custom type a3ComPathAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ComPathAdminStatus_Type.__name__ = "Integer32"
_A3ComPathAdminStatus_Object = MibTableColumn
a3ComPathAdminStatus = _A3ComPathAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 8),
    _A3ComPathAdminStatus_Type()
)
a3ComPathAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathAdminStatus.setStatus("mandatory")


class _A3ComPathOperStatus_Type(Integer32):
    """Custom type a3ComPathOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("down", 2),
          ("notAvailable", 4),
          ("other", 5),
          ("up", 1))
    )


_A3ComPathOperStatus_Type.__name__ = "Integer32"
_A3ComPathOperStatus_Object = MibTableColumn
a3ComPathOperStatus = _A3ComPathOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 9),
    _A3ComPathOperStatus_Type()
)
a3ComPathOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathOperStatus.setStatus("mandatory")


class _A3ComPathBaud_Type(Integer32):
    """Custom type a3ComPathBaud based on Integer32"""
    defaultValue = 9

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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("baud1200", 2),
          ("baud128k", 10),
          ("baud1536k", 13),
          ("baud16000k", 21),
          ("baud19200", 6),
          ("baud2048k", 14),
          ("baud2400", 3),
          ("baud256k", 11),
          ("baud3072k", 15),
          ("baud38400", 7),
          ("baud4000k", 16),
          ("baud448k", 12),
          ("baud4608k", 17),
          ("baud4800", 4),
          ("baud56k", 8),
          ("baud6144k", 18),
          ("baud64k", 9),
          ("baud7680k", 19),
          ("baud9216k", 20),
          ("baud9600", 5),
          ("notApplicable", 1),
          ("other", 22))
    )


_A3ComPathBaud_Type.__name__ = "Integer32"
_A3ComPathBaud_Object = MibTableColumn
a3ComPathBaud = _A3ComPathBaud_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 10),
    _A3ComPathBaud_Type()
)
a3ComPathBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathBaud.setStatus("deprecated")


class _A3ComPathConn_Type(Integer32):
    """Custom type a3ComPathConn based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("auto", 9),
          ("g703", 5),
          ("isdnBri", 7),
          ("isdnPri", 8),
          ("notApplicable", 1),
          ("other", 10),
          ("rs232", 3),
          ("rs449", 4),
          ("t3", 6),
          ("v35", 2),
          ("x21", 11))
    )


_A3ComPathConn_Type.__name__ = "Integer32"
_A3ComPathConn_Object = MibTableColumn
a3ComPathConn = _A3ComPathConn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 11),
    _A3ComPathConn_Type()
)
a3ComPathConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathConn.setStatus("mandatory")


class _A3ComPathClock_Type(Integer32):
    """Custom type a3ComPathClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("notApplicable", 1))
    )


_A3ComPathClock_Type.__name__ = "Integer32"
_A3ComPathClock_Object = MibTableColumn
a3ComPathClock = _A3ComPathClock_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 12),
    _A3ComPathClock_Type()
)
a3ComPathClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathClock.setStatus("mandatory")
_A3ComPathLastChange_Type = TimeTicks
_A3ComPathLastChange_Object = MibTableColumn
a3ComPathLastChange = _A3ComPathLastChange_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 13),
    _A3ComPathLastChange_Type()
)
a3ComPathLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathLastChange.setStatus("mandatory")
_A3ComPathSlotIndex_Type = Integer32
_A3ComPathSlotIndex_Object = MibTableColumn
a3ComPathSlotIndex = _A3ComPathSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 14),
    _A3ComPathSlotIndex_Type()
)
a3ComPathSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathSlotIndex.setStatus("mandatory")
_A3ComPathConnPos_Type = Integer32
_A3ComPathConnPos_Object = MibTableColumn
a3ComPathConnPos = _A3ComPathConnPos_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 15),
    _A3ComPathConnPos_Type()
)
a3ComPathConnPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathConnPos.setStatus("mandatory")
_A3ComPathInOctets_Type = Counter32
_A3ComPathInOctets_Object = MibTableColumn
a3ComPathInOctets = _A3ComPathInOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 16),
    _A3ComPathInOctets_Type()
)
a3ComPathInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathInOctets.setStatus("mandatory")
_A3ComPathInUcastPkts_Type = Counter32
_A3ComPathInUcastPkts_Object = MibTableColumn
a3ComPathInUcastPkts = _A3ComPathInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 17),
    _A3ComPathInUcastPkts_Type()
)
a3ComPathInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathInUcastPkts.setStatus("mandatory")
_A3ComPathInNUcastPkts_Type = Counter32
_A3ComPathInNUcastPkts_Object = MibTableColumn
a3ComPathInNUcastPkts = _A3ComPathInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 18),
    _A3ComPathInNUcastPkts_Type()
)
a3ComPathInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathInNUcastPkts.setStatus("mandatory")
_A3ComPathInDiscards_Type = Counter32
_A3ComPathInDiscards_Object = MibTableColumn
a3ComPathInDiscards = _A3ComPathInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 19),
    _A3ComPathInDiscards_Type()
)
a3ComPathInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathInDiscards.setStatus("mandatory")
_A3ComPathInErrors_Type = Counter32
_A3ComPathInErrors_Object = MibTableColumn
a3ComPathInErrors = _A3ComPathInErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 20),
    _A3ComPathInErrors_Type()
)
a3ComPathInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathInErrors.setStatus("mandatory")
_A3ComPathInUnknownProtos_Type = Counter32
_A3ComPathInUnknownProtos_Object = MibTableColumn
a3ComPathInUnknownProtos = _A3ComPathInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 21),
    _A3ComPathInUnknownProtos_Type()
)
a3ComPathInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathInUnknownProtos.setStatus("mandatory")
_A3ComPathOutOctets_Type = Counter32
_A3ComPathOutOctets_Object = MibTableColumn
a3ComPathOutOctets = _A3ComPathOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 22),
    _A3ComPathOutOctets_Type()
)
a3ComPathOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathOutOctets.setStatus("mandatory")
_A3ComPathOutUcastPkts_Type = Counter32
_A3ComPathOutUcastPkts_Object = MibTableColumn
a3ComPathOutUcastPkts = _A3ComPathOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 23),
    _A3ComPathOutUcastPkts_Type()
)
a3ComPathOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathOutUcastPkts.setStatus("mandatory")
_A3ComPathOutNUcastPkts_Type = Counter32
_A3ComPathOutNUcastPkts_Object = MibTableColumn
a3ComPathOutNUcastPkts = _A3ComPathOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 24),
    _A3ComPathOutNUcastPkts_Type()
)
a3ComPathOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathOutNUcastPkts.setStatus("mandatory")
_A3ComPathOutDiscards_Type = Counter32
_A3ComPathOutDiscards_Object = MibTableColumn
a3ComPathOutDiscards = _A3ComPathOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 25),
    _A3ComPathOutDiscards_Type()
)
a3ComPathOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathOutDiscards.setStatus("mandatory")
_A3ComPathOutErrors_Type = Counter32
_A3ComPathOutErrors_Object = MibTableColumn
a3ComPathOutErrors = _A3ComPathOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 26),
    _A3ComPathOutErrors_Type()
)
a3ComPathOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathOutErrors.setStatus("mandatory")


class _A3ComPathBaudRate_Type(Integer32):
    """Custom type a3ComPathBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_A3ComPathBaudRate_Type.__name__ = "Integer32"
_A3ComPathBaudRate_Object = MibTableColumn
a3ComPathBaudRate = _A3ComPathBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 27),
    _A3ComPathBaudRate_Type()
)
a3ComPathBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathBaudRate.setStatus("mandatory")


class _A3ComPathDuplex_Type(Integer32):
    """Custom type a3ComPathDuplex based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("full", 1),
          ("half", 2))
    )


_A3ComPathDuplex_Type.__name__ = "Integer32"
_A3ComPathDuplex_Object = MibTableColumn
a3ComPathDuplex = _A3ComPathDuplex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 28),
    _A3ComPathDuplex_Type()
)
a3ComPathDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDuplex.setStatus("mandatory")
_A3ComPort_ObjectIdentity = ObjectIdentity
a3ComPort = _A3ComPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 17)
)
_A3ComPortNumber_Type = Integer32
_A3ComPortNumber_Object = MibScalar
a3ComPortNumber = _A3ComPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 1),
    _A3ComPortNumber_Type()
)
a3ComPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortNumber.setStatus("mandatory")
_A3ComPortTable_Object = MibTable
a3ComPortTable = _A3ComPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2)
)
if mibBuilder.loadTexts:
    a3ComPortTable.setStatus("mandatory")
_A3ComPortEntry_Object = MibTableRow
a3ComPortEntry = _A3ComPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1)
)
a3ComPortEntry.setIndexNames(
    (0, "A3COM-PORTPATH-R6-MIB", "a3ComPortIndex"),
)
if mibBuilder.loadTexts:
    a3ComPortEntry.setStatus("mandatory")
_A3ComPortIndex_Type = Integer32
_A3ComPortIndex_Object = MibTableColumn
a3ComPortIndex = _A3ComPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 1),
    _A3ComPortIndex_Type()
)
a3ComPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortIndex.setStatus("mandatory")


class _A3ComPortOwner_Type(Integer32):
    """Custom type a3ComPortOwner based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("auto", 9),
          ("autoFr", 11),
          ("autoPpp", 10),
          ("ethernet", 1),
          ("fddi", 3),
          ("frameRelay", 7),
          ("plg", 5),
          ("ppp", 4),
          ("smds", 8),
          ("tokenRing", 2),
          ("x25", 6))
    )


_A3ComPortOwner_Type.__name__ = "Integer32"
_A3ComPortOwner_Object = MibTableColumn
a3ComPortOwner = _A3ComPortOwner_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 2),
    _A3ComPortOwner_Type()
)
a3ComPortOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortOwner.setStatus("mandatory")


class _A3ComPortBoundaryRoute_Type(Integer32):
    """Custom type a3ComPortBoundaryRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("notApplicable", 1))
    )


_A3ComPortBoundaryRoute_Type.__name__ = "Integer32"
_A3ComPortBoundaryRoute_Object = MibTableColumn
a3ComPortBoundaryRoute = _A3ComPortBoundaryRoute_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 3),
    _A3ComPortBoundaryRoute_Type()
)
a3ComPortBoundaryRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortBoundaryRoute.setStatus("mandatory")


class _A3ComPortBoundaryEncap_Type(Integer32):
    """Custom type a3ComPortBoundaryEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("fddi", 4),
          ("none", 5),
          ("notApplicable", 1),
          ("tokenring", 3))
    )


_A3ComPortBoundaryEncap_Type.__name__ = "Integer32"
_A3ComPortBoundaryEncap_Object = MibTableColumn
a3ComPortBoundaryEncap = _A3ComPortBoundaryEncap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 4),
    _A3ComPortBoundaryEncap_Type()
)
a3ComPortBoundaryEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortBoundaryEncap.setStatus("mandatory")
_A3ComPortCosInterleave_Type = Integer32
_A3ComPortCosInterleave_Object = MibTableColumn
a3ComPortCosInterleave = _A3ComPortCosInterleave_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 5),
    _A3ComPortCosInterleave_Type()
)
a3ComPortCosInterleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortCosInterleave.setStatus("deprecated")


class _A3ComPortMacAddrFmtARP_Type(Integer32):
    """Custom type a3ComPortMacAddrFmtARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 1),
          ("nonCanonical", 2))
    )


_A3ComPortMacAddrFmtARP_Type.__name__ = "Integer32"
_A3ComPortMacAddrFmtARP_Object = MibTableColumn
a3ComPortMacAddrFmtARP = _A3ComPortMacAddrFmtARP_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 6),
    _A3ComPortMacAddrFmtARP_Type()
)
a3ComPortMacAddrFmtARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortMacAddrFmtARP.setStatus("mandatory")


class _A3ComPortMacAddrFmtIPX_Type(Integer32):
    """Custom type a3ComPortMacAddrFmtIPX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 1),
          ("nonCanonical", 2))
    )


_A3ComPortMacAddrFmtIPX_Type.__name__ = "Integer32"
_A3ComPortMacAddrFmtIPX_Object = MibTableColumn
a3ComPortMacAddrFmtIPX = _A3ComPortMacAddrFmtIPX_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 7),
    _A3ComPortMacAddrFmtIPX_Type()
)
a3ComPortMacAddrFmtIPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortMacAddrFmtIPX.setStatus("mandatory")


class _A3ComPortMacAddrFmtXNS_Type(Integer32):
    """Custom type a3ComPortMacAddrFmtXNS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("canonical", 1),
          ("nonCanonical", 2))
    )


_A3ComPortMacAddrFmtXNS_Type.__name__ = "Integer32"
_A3ComPortMacAddrFmtXNS_Object = MibTableColumn
a3ComPortMacAddrFmtXNS = _A3ComPortMacAddrFmtXNS_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 8),
    _A3ComPortMacAddrFmtXNS_Type()
)
a3ComPortMacAddrFmtXNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortMacAddrFmtXNS.setStatus("mandatory")
_A3ComPortPath_Type = Integer32
_A3ComPortPath_Object = MibTableColumn
a3ComPortPath = _A3ComPortPath_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 9),
    _A3ComPortPath_Type()
)
a3ComPortPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortPath.setStatus("mandatory")


class _A3ComQueueInterleave1_Type(Integer32):
    """Custom type a3ComQueueInterleave1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_A3ComQueueInterleave1_Type.__name__ = "Integer32"
_A3ComQueueInterleave1_Object = MibTableColumn
a3ComQueueInterleave1 = _A3ComQueueInterleave1_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 10),
    _A3ComQueueInterleave1_Type()
)
a3ComQueueInterleave1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQueueInterleave1.setStatus("mandatory")


class _A3ComQueueInterleave2_Type(Integer32):
    """Custom type a3ComQueueInterleave2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_A3ComQueueInterleave2_Type.__name__ = "Integer32"
_A3ComQueueInterleave2_Object = MibTableColumn
a3ComQueueInterleave2 = _A3ComQueueInterleave2_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 11),
    _A3ComQueueInterleave2_Type()
)
a3ComQueueInterleave2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQueueInterleave2.setStatus("mandatory")


class _A3ComQueuePattern_Type(Integer32):
    """Custom type a3ComQueuePattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 6),
          ("ratio3to3to2", 1),
          ("ratio4to2to2", 2),
          ("ratio4to3to1", 3),
          ("ratio5to2to1", 4),
          ("ratio6to1to1", 5))
    )


_A3ComQueuePattern_Type.__name__ = "Integer32"
_A3ComQueuePattern_Object = MibTableColumn
a3ComQueuePattern = _A3ComQueuePattern_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 13),
    _A3ComQueuePattern_Type()
)
a3ComQueuePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComQueuePattern.setStatus("mandatory")
_A3ComPortAsOwnerTimer_Type = Integer32
_A3ComPortAsOwnerTimer_Object = MibTableColumn
a3ComPortAsOwnerTimer = _A3ComPortAsOwnerTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 15),
    _A3ComPortAsOwnerTimer_Type()
)
a3ComPortAsOwnerTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortAsOwnerTimer.setStatus("mandatory")


class _A3ComSmartFilteringCtl_Type(Integer32):
    """Custom type a3ComSmartFilteringCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSmartFilter", 2),
          ("smartFilter", 1))
    )


_A3ComSmartFilteringCtl_Type.__name__ = "Integer32"
_A3ComSmartFilteringCtl_Object = MibTableColumn
a3ComSmartFilteringCtl = _A3ComSmartFilteringCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 16),
    _A3ComSmartFilteringCtl_Type()
)
a3ComSmartFilteringCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSmartFilteringCtl.setStatus("mandatory")


class _A3ComBrCentralMacCtl_Type(Integer32):
    """Custom type a3ComBrCentralMacCtl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("centralMac", 1),
          ("noCentralMac", 2))
    )


_A3ComBrCentralMacCtl_Type.__name__ = "Integer32"
_A3ComBrCentralMacCtl_Object = MibTableColumn
a3ComBrCentralMacCtl = _A3ComBrCentralMacCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 17),
    _A3ComBrCentralMacCtl_Type()
)
a3ComBrCentralMacCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBrCentralMacCtl.setStatus("mandatory")
_A3ComPortLabel_Type = DisplayString
_A3ComPortLabel_Object = MibTableColumn
a3ComPortLabel = _A3ComPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 18),
    _A3ComPortLabel_Type()
)
a3ComPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortLabel.setStatus("mandatory")
_A3ComPortCircuitID_Type = OctetString
_A3ComPortCircuitID_Object = MibTableColumn
a3ComPortCircuitID = _A3ComPortCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 19),
    _A3ComPortCircuitID_Type()
)
a3ComPortCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortCircuitID.setStatus("mandatory")
_A3ComPortStatus_Type = RowStatus
_A3ComPortStatus_Object = MibTableColumn
a3ComPortStatus = _A3ComPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 20),
    _A3ComPortStatus_Type()
)
a3ComPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortStatus.setStatus("mandatory")
_A3ComPortName_Type = DisplayString
_A3ComPortName_Object = MibTableColumn
a3ComPortName = _A3ComPortName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 21),
    _A3ComPortName_Type()
)
a3ComPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortName.setStatus("mandatory")


class _A3ComPortVirtual_Type(Integer32):
    """Custom type a3ComPortVirtual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("virtual", 2))
    )


_A3ComPortVirtual_Type.__name__ = "Integer32"
_A3ComPortVirtual_Object = MibTableColumn
a3ComPortVirtual = _A3ComPortVirtual_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 22),
    _A3ComPortVirtual_Type()
)
a3ComPortVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortVirtual.setStatus("mandatory")


class _A3ComQueueThrottle_Type(Integer32):
    """Custom type a3ComQueueThrottle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_A3ComQueueThrottle_Type.__name__ = "Integer32"
_A3ComQueueThrottle_Object = MibTableColumn
a3ComQueueThrottle = _A3ComQueueThrottle_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 23),
    _A3ComQueueThrottle_Type()
)
a3ComQueueThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComQueueThrottle.setStatus("mandatory")


class _A3ComPortInCallerId_Type(DisplayString):
    """Custom type a3ComPortInCallerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComPortInCallerId_Type.__name__ = "DisplayString"
_A3ComPortInCallerId_Object = MibTableColumn
a3ComPortInCallerId = _A3ComPortInCallerId_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 24),
    _A3ComPortInCallerId_Type()
)
a3ComPortInCallerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortInCallerId.setStatus("mandatory")


class _A3ComPortCompType_Type(Integer32):
    """Custom type a3ComPortCompType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("history", 2),
          ("none", 1),
          ("perPacket", 3))
    )


_A3ComPortCompType_Type.__name__ = "Integer32"
_A3ComPortCompType_Object = MibTableColumn
a3ComPortCompType = _A3ComPortCompType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 25),
    _A3ComPortCompType_Type()
)
a3ComPortCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortCompType.setStatus("mandatory")


class _A3ComPortX25ProtID_Type(Integer32):
    """Custom type a3ComPortX25ProtID based on Integer32"""
    defaultValue = 221

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A3ComPortX25ProtID_Type.__name__ = "Integer32"
_A3ComPortX25ProtID_Object = MibTableColumn
a3ComPortX25ProtID = _A3ComPortX25ProtID_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 26),
    _A3ComPortX25ProtID_Type()
)
a3ComPortX25ProtID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortX25ProtID.setStatus("mandatory")


class _A3ComPortIbmTraffic_Type(Integer32):
    """Custom type a3ComPortIbmTraffic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ibmTraffic", 1),
          ("noibmTraffic", 2))
    )


_A3ComPortIbmTraffic_Type.__name__ = "Integer32"
_A3ComPortIbmTraffic_Object = MibTableColumn
a3ComPortIbmTraffic = _A3ComPortIbmTraffic_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 27),
    _A3ComPortIbmTraffic_Type()
)
a3ComPortIbmTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortIbmTraffic.setStatus("mandatory")


class _A3ComDefaultPriority_Type(Integer32):
    """Custom type a3ComDefaultPriority based on Integer32"""
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
        *(("high", 1),
          ("low", 3),
          ("med", 2),
          ("unknown", 4))
    )


_A3ComDefaultPriority_Type.__name__ = "Integer32"
_A3ComDefaultPriority_Object = MibScalar
a3ComDefaultPriority = _A3ComDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 17, 3),
    _A3ComDefaultPriority_Type()
)
a3ComDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDefaultPriority.setStatus("mandatory")
_A3ComPathDial_ObjectIdentity = ObjectIdentity
a3ComPathDial = _A3ComPathDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 18)
)
_A3ComPathDialNumber_Type = Integer32
_A3ComPathDialNumber_Object = MibScalar
a3ComPathDialNumber = _A3ComPathDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 1),
    _A3ComPathDialNumber_Type()
)
a3ComPathDialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathDialNumber.setStatus("mandatory")
_A3ComPathDialTable_Object = MibTable
a3ComPathDialTable = _A3ComPathDialTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2)
)
if mibBuilder.loadTexts:
    a3ComPathDialTable.setStatus("mandatory")
_A3ComPathDialEntry_Object = MibTableRow
a3ComPathDialEntry = _A3ComPathDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1)
)
a3ComPathDialEntry.setIndexNames(
    (0, "A3COM-PORTPATH-R6-MIB", "a3ComPathDialIndex"),
)
if mibBuilder.loadTexts:
    a3ComPathDialEntry.setStatus("mandatory")
_A3ComPathDialIndex_Type = Integer32
_A3ComPathDialIndex_Object = MibTableColumn
a3ComPathDialIndex = _A3ComPathDialIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 1),
    _A3ComPathDialIndex_Type()
)
a3ComPathDialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPathDialIndex.setStatus("mandatory")


class _A3ComPathDialType_Type(Integer32):
    """Custom type a3ComPathDialType based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 4),
          ("primaryAuto", 5),
          ("primaryAutoDial", 9),
          ("primaryAutoLeased", 8),
          ("primaryDial", 2),
          ("primaryLeased", 1),
          ("secondaryAuto", 6),
          ("secondaryAutoDial", 11),
          ("secondaryAutoLeased", 10),
          ("secondaryDial", 3),
          ("secondaryLeased", 7))
    )


_A3ComPathDialType_Type.__name__ = "Integer32"
_A3ComPathDialType_Object = MibTableColumn
a3ComPathDialType = _A3ComPathDialType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 2),
    _A3ComPathDialType_Type()
)
a3ComPathDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialType.setStatus("mandatory")


class _A3ComPathDialCtl_Type(Integer32):
    """Custom type a3ComPathDialCtl based on Integer32"""
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
        *(("answerNoOriginate", 2),
          ("answerOriginate", 1),
          ("noAnswerNoOriginate", 4),
          ("noAnswerOriginate", 3))
    )


_A3ComPathDialCtl_Type.__name__ = "Integer32"
_A3ComPathDialCtl_Object = MibTableColumn
a3ComPathDialCtl = _A3ComPathDialCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 3),
    _A3ComPathDialCtl_Type()
)
a3ComPathDialCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialCtl.setStatus("mandatory")


class _A3ComPathDialAction_Type(Integer32):
    """Custom type a3ComPathDialAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dial", 1),
          ("hangUp", 2),
          ("other", 3))
    )


_A3ComPathDialAction_Type.__name__ = "Integer32"
_A3ComPathDialAction_Object = MibTableColumn
a3ComPathDialAction = _A3ComPathDialAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 4),
    _A3ComPathDialAction_Type()
)
a3ComPathDialAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialAction.setStatus("mandatory")


class _A3ComPathDialNum_Type(DisplayString):
    """Custom type a3ComPathDialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_A3ComPathDialNum_Type.__name__ = "DisplayString"
_A3ComPathDialNum_Object = MibTableColumn
a3ComPathDialNum = _A3ComPathDialNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 5),
    _A3ComPathDialNum_Type()
)
a3ComPathDialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialNum.setStatus("mandatory")


class _A3ComPathDialDodIdleTime_Type(Integer32):
    """Custom type a3ComPathDialDodIdleTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_A3ComPathDialDodIdleTime_Type.__name__ = "Integer32"
_A3ComPathDialDodIdleTime_Object = MibTableColumn
a3ComPathDialDodIdleTime = _A3ComPathDialDodIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 6),
    _A3ComPathDialDodIdleTime_Type()
)
a3ComPathDialDodIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialDodIdleTime.setStatus("deprecated")


class _A3ComPathDialMode_Type(Integer32):
    """Custom type a3ComPathDialMode based on Integer32"""
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
        *(("autoDTR", 4),
          ("autoV25", 3),
          ("dtrDial", 2),
          ("v25Dial", 1))
    )


_A3ComPathDialMode_Type.__name__ = "Integer32"
_A3ComPathDialMode_Object = MibTableColumn
a3ComPathDialMode = _A3ComPathDialMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 7),
    _A3ComPathDialMode_Type()
)
a3ComPathDialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialMode.setStatus("mandatory")


class _A3ComPathDialDynCont_Type(Integer32):
    """Custom type a3ComPathDialDynCont based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("other", 3),
          ("static", 1))
    )


_A3ComPathDialDynCont_Type.__name__ = "Integer32"
_A3ComPathDialDynCont_Object = MibTableColumn
a3ComPathDialDynCont = _A3ComPathDialDynCont_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 8),
    _A3ComPathDialDynCont_Type()
)
a3ComPathDialDynCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialDynCont.setStatus("mandatory")


class _A3ComPathDialLocalDialNumber_Type(DisplayString):
    """Custom type a3ComPathDialLocalDialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_A3ComPathDialLocalDialNumber_Type.__name__ = "DisplayString"
_A3ComPathDialLocalDialNumber_Object = MibTableColumn
a3ComPathDialLocalDialNumber = _A3ComPathDialLocalDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 9),
    _A3ComPathDialLocalDialNumber_Type()
)
a3ComPathDialLocalDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialLocalDialNumber.setStatus("mandatory")


class _A3ComPathDialLocalSubAddress_Type(DisplayString):
    """Custom type a3ComPathDialLocalSubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_A3ComPathDialLocalSubAddress_Type.__name__ = "DisplayString"
_A3ComPathDialLocalSubAddress_Object = MibTableColumn
a3ComPathDialLocalSubAddress = _A3ComPathDialLocalSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 10),
    _A3ComPathDialLocalSubAddress_Type()
)
a3ComPathDialLocalSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialLocalSubAddress.setStatus("mandatory")


class _A3ComPathDialSPIDDN1_Type(DisplayString):
    """Custom type a3ComPathDialSPIDDN1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_A3ComPathDialSPIDDN1_Type.__name__ = "DisplayString"
_A3ComPathDialSPIDDN1_Object = MibTableColumn
a3ComPathDialSPIDDN1 = _A3ComPathDialSPIDDN1_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 11),
    _A3ComPathDialSPIDDN1_Type()
)
a3ComPathDialSPIDDN1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialSPIDDN1.setStatus("mandatory")


class _A3ComPathDialSPIDDN2_Type(DisplayString):
    """Custom type a3ComPathDialSPIDDN2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_A3ComPathDialSPIDDN2_Type.__name__ = "DisplayString"
_A3ComPathDialSPIDDN2_Object = MibTableColumn
a3ComPathDialSPIDDN2 = _A3ComPathDialSPIDDN2_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 12),
    _A3ComPathDialSPIDDN2_Type()
)
a3ComPathDialSPIDDN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialSPIDDN2.setStatus("mandatory")


class _A3ComPathDialRateAdaption_Type(Integer32):
    """Custom type a3ComPathDialRateAdaption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("rate56", 3),
          ("rate64", 2))
    )


_A3ComPathDialRateAdaption_Type.__name__ = "Integer32"
_A3ComPathDialRateAdaption_Object = MibTableColumn
a3ComPathDialRateAdaption = _A3ComPathDialRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 13),
    _A3ComPathDialRateAdaption_Type()
)
a3ComPathDialRateAdaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialRateAdaption.setStatus("mandatory")


class _A3ComPathDialSwitchType_Type(Integer32):
    """Custom type a3ComPathDialSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("att5ess", 4),
          ("dms100", 5),
          ("etsi", 1),
          ("ni1", 3),
          ("ntt", 2))
    )


_A3ComPathDialSwitchType_Type.__name__ = "Integer32"
_A3ComPathDialSwitchType_Object = MibTableColumn
a3ComPathDialSwitchType = _A3ComPathDialSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 14),
    _A3ComPathDialSwitchType_Type()
)
a3ComPathDialSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialSwitchType.setStatus("mandatory")


class _A3ComPathDialExDevType_Type(Integer32):
    """Custom type a3ComPathDialExDevType based on Integer32"""
    defaultValue = 2

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
        *(("bri", 1),
          ("modem", 2),
          ("other", 4),
          ("sw56", 3))
    )


_A3ComPathDialExDevType_Type.__name__ = "Integer32"
_A3ComPathDialExDevType_Object = MibTableColumn
a3ComPathDialExDevType = _A3ComPathDialExDevType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 15),
    _A3ComPathDialExDevType_Type()
)
a3ComPathDialExDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPathDialExDevType.setStatus("mandatory")
_A3ComPortDial_ObjectIdentity = ObjectIdentity
a3ComPortDial = _A3ComPortDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 19)
)
_A3ComPortDIALNumber_Type = Integer32
_A3ComPortDIALNumber_Object = MibScalar
a3ComPortDIALNumber = _A3ComPortDIALNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 1),
    _A3ComPortDIALNumber_Type()
)
a3ComPortDIALNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortDIALNumber.setStatus("mandatory")
_A3ComPortDialTable_Object = MibTable
a3ComPortDialTable = _A3ComPortDialTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2)
)
if mibBuilder.loadTexts:
    a3ComPortDialTable.setStatus("mandatory")
_A3ComPortDialEntry_Object = MibTableRow
a3ComPortDialEntry = _A3ComPortDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1)
)
a3ComPortDialEntry.setIndexNames(
    (0, "A3COM-PORTPATH-R6-MIB", "a3ComPortDialIndex"),
)
if mibBuilder.loadTexts:
    a3ComPortDialEntry.setStatus("mandatory")
_A3ComPortDialIndex_Type = Integer32
_A3ComPortDialIndex_Object = MibTableColumn
a3ComPortDialIndex = _A3ComPortDialIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 1),
    _A3ComPortDialIndex_Type()
)
a3ComPortDialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortDialIndex.setStatus("mandatory")


class _A3ComPortDialDisasterCtl_Type(Integer32):
    """Custom type a3ComPortDialDisasterCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disasterRecovery", 1),
          ("noDisasterRecovery", 2))
    )


_A3ComPortDialDisasterCtl_Type.__name__ = "Integer32"
_A3ComPortDialDisasterCtl_Object = MibTableColumn
a3ComPortDialDisasterCtl = _A3ComPortDialDisasterCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 2),
    _A3ComPortDialDisasterCtl_Type()
)
a3ComPortDialDisasterCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialDisasterCtl.setStatus("mandatory")


class _A3ComPortDialBandOnDmnd_Type(Integer32):
    """Custom type a3ComPortDialBandOnDmnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bandwidthOnDemand", 1),
          ("noBandwidthOnDemand", 2))
    )


_A3ComPortDialBandOnDmnd_Type.__name__ = "Integer32"
_A3ComPortDialBandOnDmnd_Object = MibTableColumn
a3ComPortDialBandOnDmnd = _A3ComPortDialBandOnDmnd_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 3),
    _A3ComPortDialBandOnDmnd_Type()
)
a3ComPortDialBandOnDmnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialBandOnDmnd.setStatus("mandatory")


class _A3ComPortDialDebounceTimeUp_Type(Integer32):
    """Custom type a3ComPortDialDebounceTimeUp based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_A3ComPortDialDebounceTimeUp_Type.__name__ = "Integer32"
_A3ComPortDialDebounceTimeUp_Object = MibTableColumn
a3ComPortDialDebounceTimeUp = _A3ComPortDialDebounceTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 4),
    _A3ComPortDialDebounceTimeUp_Type()
)
a3ComPortDialDebounceTimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialDebounceTimeUp.setStatus("mandatory")


class _A3ComPortDialDebounceTimeDown_Type(Integer32):
    """Custom type a3ComPortDialDebounceTimeDown based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_A3ComPortDialDebounceTimeDown_Type.__name__ = "Integer32"
_A3ComPortDialDebounceTimeDown_Object = MibTableColumn
a3ComPortDialDebounceTimeDown = _A3ComPortDialDebounceTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 5),
    _A3ComPortDialDebounceTimeDown_Type()
)
a3ComPortDialDebounceTimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialDebounceTimeDown.setStatus("mandatory")


class _A3ComPortDialInitState_Type(Integer32):
    """Custom type a3ComPortDialInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dialOnDemand", 3),
          ("manualDial", 2),
          ("noDialOut", 1))
    )


_A3ComPortDialInitState_Type.__name__ = "Integer32"
_A3ComPortDialInitState_Object = MibTableColumn
a3ComPortDialInitState = _A3ComPortDialInitState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 6),
    _A3ComPortDialInitState_Type()
)
a3ComPortDialInitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialInitState.setStatus("mandatory")


class _A3ComPortDialRcvrState_Type(Integer32):
    """Custom type a3ComPortDialRcvrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("noAnswer", 1))
    )


_A3ComPortDialRcvrState_Type.__name__ = "Integer32"
_A3ComPortDialRcvrState_Object = MibTableColumn
a3ComPortDialRcvrState = _A3ComPortDialRcvrState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 7),
    _A3ComPortDialRcvrState_Type()
)
a3ComPortDialRcvrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialRcvrState.setStatus("mandatory")


class _A3ComPortDialAction_Type(Integer32):
    """Custom type a3ComPortDialAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dial", 1),
          ("hangUp", 2),
          ("other", 3))
    )


_A3ComPortDialAction_Type.__name__ = "Integer32"
_A3ComPortDialAction_Object = MibTableColumn
a3ComPortDialAction = _A3ComPortDialAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 8),
    _A3ComPortDialAction_Type()
)
a3ComPortDialAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialAction.setStatus("mandatory")


class _A3ComPortDialDodIdleTime_Type(Integer32):
    """Custom type a3ComPortDialDodIdleTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_A3ComPortDialDodIdleTime_Type.__name__ = "Integer32"
_A3ComPortDialDodIdleTime_Object = MibTableColumn
a3ComPortDialDodIdleTime = _A3ComPortDialDodIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 9),
    _A3ComPortDialDodIdleTime_Type()
)
a3ComPortDialDodIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialDodIdleTime.setStatus("mandatory")


class _A3ComPortDialIdleTime_Type(Integer32):
    """Custom type a3ComPortDialIdleTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_A3ComPortDialIdleTime_Type.__name__ = "Integer32"
_A3ComPortDialIdleTime_Object = MibTableColumn
a3ComPortDialIdleTime = _A3ComPortDialIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 10),
    _A3ComPortDialIdleTime_Type()
)
a3ComPortDialIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialIdleTime.setStatus("mandatory")
_A3ComPortDialDodCallsMade_Type = Counter32
_A3ComPortDialDodCallsMade_Object = MibTableColumn
a3ComPortDialDodCallsMade = _A3ComPortDialDodCallsMade_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 11),
    _A3ComPortDialDodCallsMade_Type()
)
a3ComPortDialDodCallsMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortDialDodCallsMade.setStatus("mandatory")
_A3ComPortDialDodCallsFail_Type = Counter32
_A3ComPortDialDodCallsFail_Object = MibTableColumn
a3ComPortDialDodCallsFail = _A3ComPortDialDodCallsFail_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 12),
    _A3ComPortDialDodCallsFail_Type()
)
a3ComPortDialDodCallsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortDialDodCallsFail.setStatus("mandatory")
_A3ComPortDialDodUpTime_Type = Counter32
_A3ComPortDialDodUpTime_Object = MibTableColumn
a3ComPortDialDodUpTime = _A3ComPortDialDodUpTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 13),
    _A3ComPortDialDodUpTime_Type()
)
a3ComPortDialDodUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortDialDodUpTime.setStatus("mandatory")
_A3ComPortDialDodPktsOut_Type = Counter32
_A3ComPortDialDodPktsOut_Object = MibTableColumn
a3ComPortDialDodPktsOut = _A3ComPortDialDodPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 14),
    _A3ComPortDialDodPktsOut_Type()
)
a3ComPortDialDodPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortDialDodPktsOut.setStatus("mandatory")


class _A3ComPortDialBODTHreshold_Type(Integer32):
    """Custom type a3ComPortDialBODTHreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_A3ComPortDialBODTHreshold_Type.__name__ = "Integer32"
_A3ComPortDialBODTHreshold_Object = MibTableColumn
a3ComPortDialBODTHreshold = _A3ComPortDialBODTHreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 15),
    _A3ComPortDialBODTHreshold_Type()
)
a3ComPortDialBODTHreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialBODTHreshold.setStatus("mandatory")
_A3ComPortDialPoolPrefTable_Object = MibTable
a3ComPortDialPoolPrefTable = _A3ComPortDialPoolPrefTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 3)
)
if mibBuilder.loadTexts:
    a3ComPortDialPoolPrefTable.setStatus("mandatory")
_A3ComPortDialPoolPrefEntry_Object = MibTableRow
a3ComPortDialPoolPrefEntry = _A3ComPortDialPoolPrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 3, 1)
)
a3ComPortDialPoolPrefEntry.setIndexNames(
    (0, "A3COM-PORTPATH-R6-MIB", "a3ComPortDialPoolPrefPort"),
    (0, "A3COM-PORTPATH-R6-MIB", "a3ComPortDialPoolPrefPathPos"),
)
if mibBuilder.loadTexts:
    a3ComPortDialPoolPrefEntry.setStatus("mandatory")
_A3ComPortDialPoolPrefPort_Type = Integer32
_A3ComPortDialPoolPrefPort_Object = MibTableColumn
a3ComPortDialPoolPrefPort = _A3ComPortDialPoolPrefPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 3, 1, 1),
    _A3ComPortDialPoolPrefPort_Type()
)
a3ComPortDialPoolPrefPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortDialPoolPrefPort.setStatus("mandatory")
_A3ComPortDialPoolPrefPathPos_Type = Integer32
_A3ComPortDialPoolPrefPathPos_Object = MibTableColumn
a3ComPortDialPoolPrefPathPos = _A3ComPortDialPoolPrefPathPos_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 3, 1, 2),
    _A3ComPortDialPoolPrefPathPos_Type()
)
a3ComPortDialPoolPrefPathPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortDialPoolPrefPathPos.setStatus("mandatory")
_A3ComPortDialPoolPrefPathNum_Type = Integer32
_A3ComPortDialPoolPrefPathNum_Object = MibTableColumn
a3ComPortDialPoolPrefPathNum = _A3ComPortDialPoolPrefPathNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 3, 1, 3),
    _A3ComPortDialPoolPrefPathNum_Type()
)
a3ComPortDialPoolPrefPathNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialPoolPrefPathNum.setStatus("mandatory")
_A3ComPortDialPoolPrefStatus_Type = RowStatus
_A3ComPortDialPoolPrefStatus_Object = MibTableColumn
a3ComPortDialPoolPrefStatus = _A3ComPortDialPoolPrefStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 3, 1, 4),
    _A3ComPortDialPoolPrefStatus_Type()
)
a3ComPortDialPoolPrefStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialPoolPrefStatus.setStatus("mandatory")
_A3ComPortDialPhoneListTable_Object = MibTable
a3ComPortDialPhoneListTable = _A3ComPortDialPhoneListTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 4)
)
if mibBuilder.loadTexts:
    a3ComPortDialPhoneListTable.setStatus("mandatory")
_A3ComPortDialPhoneListEntry_Object = MibTableRow
a3ComPortDialPhoneListEntry = _A3ComPortDialPhoneListEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1)
)
a3ComPortDialPhoneListEntry.setIndexNames(
    (0, "A3COM-PORTPATH-R6-MIB", "a3ComPortDialPhoneListPort"),
    (0, "A3COM-PORTPATH-R6-MIB", "a3ComPortDialPhoneListPos"),
)
if mibBuilder.loadTexts:
    a3ComPortDialPhoneListEntry.setStatus("mandatory")
_A3ComPortDialPhoneListPort_Type = Integer32
_A3ComPortDialPhoneListPort_Object = MibTableColumn
a3ComPortDialPhoneListPort = _A3ComPortDialPhoneListPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 1),
    _A3ComPortDialPhoneListPort_Type()
)
a3ComPortDialPhoneListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortDialPhoneListPort.setStatus("mandatory")
_A3ComPortDialPhoneListPos_Type = Integer32
_A3ComPortDialPhoneListPos_Object = MibTableColumn
a3ComPortDialPhoneListPos = _A3ComPortDialPhoneListPos_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 2),
    _A3ComPortDialPhoneListPos_Type()
)
a3ComPortDialPhoneListPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortDialPhoneListPos.setStatus("mandatory")


class _A3ComPortDialPhoneListPhoneNo_Type(DisplayString):
    """Custom type a3ComPortDialPhoneListPhoneNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 51),
    )


_A3ComPortDialPhoneListPhoneNo_Type.__name__ = "DisplayString"
_A3ComPortDialPhoneListPhoneNo_Object = MibTableColumn
a3ComPortDialPhoneListPhoneNo = _A3ComPortDialPhoneListPhoneNo_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 3),
    _A3ComPortDialPhoneListPhoneNo_Type()
)
a3ComPortDialPhoneListPhoneNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialPhoneListPhoneNo.setStatus("mandatory")


class _A3ComPortDialPhoneListType_Type(Integer32):
    """Custom type a3ComPortDialPhoneListType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("iSDN", 1),
          ("other", 3))
    )


_A3ComPortDialPhoneListType_Type.__name__ = "Integer32"
_A3ComPortDialPhoneListType_Object = MibTableColumn
a3ComPortDialPhoneListType = _A3ComPortDialPhoneListType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 4),
    _A3ComPortDialPhoneListType_Type()
)
a3ComPortDialPhoneListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialPhoneListType.setStatus("mandatory")


class _A3ComPortDialPhoneListBaud_Type(Integer32):
    """Custom type a3ComPortDialPhoneListBaud based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_A3ComPortDialPhoneListBaud_Type.__name__ = "Integer32"
_A3ComPortDialPhoneListBaud_Object = MibTableColumn
a3ComPortDialPhoneListBaud = _A3ComPortDialPhoneListBaud_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 5),
    _A3ComPortDialPhoneListBaud_Type()
)
a3ComPortDialPhoneListBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialPhoneListBaud.setStatus("mandatory")
_A3ComPortDialPhoneListStatus_Type = RowStatus
_A3ComPortDialPhoneListStatus_Object = MibTableColumn
a3ComPortDialPhoneListStatus = _A3ComPortDialPhoneListStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 6),
    _A3ComPortDialPhoneListStatus_Type()
)
a3ComPortDialPhoneListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortDialPhoneListStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-PORTPATH-R6-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComPath": a3ComPath,
       "a3ComPathNumber": a3ComPathNumber,
       "a3ComPathTable": a3ComPathTable,
       "a3ComPathEntry": a3ComPathEntry,
       "a3ComPathIndex": a3ComPathIndex,
       "a3ComPathName": a3ComPathName,
       "a3ComPathPort": a3ComPathPort,
       "a3ComPathItcmOption": a3ComPathItcmOption,
       "a3ComPathT1Mode": a3ComPathT1Mode,
       "a3ComPathCryptoResync": a3ComPathCryptoResync,
       "a3ComPathCRC": a3ComPathCRC,
       "a3ComPathAdminStatus": a3ComPathAdminStatus,
       "a3ComPathOperStatus": a3ComPathOperStatus,
       "a3ComPathBaud": a3ComPathBaud,
       "a3ComPathConn": a3ComPathConn,
       "a3ComPathClock": a3ComPathClock,
       "a3ComPathLastChange": a3ComPathLastChange,
       "a3ComPathSlotIndex": a3ComPathSlotIndex,
       "a3ComPathConnPos": a3ComPathConnPos,
       "a3ComPathInOctets": a3ComPathInOctets,
       "a3ComPathInUcastPkts": a3ComPathInUcastPkts,
       "a3ComPathInNUcastPkts": a3ComPathInNUcastPkts,
       "a3ComPathInDiscards": a3ComPathInDiscards,
       "a3ComPathInErrors": a3ComPathInErrors,
       "a3ComPathInUnknownProtos": a3ComPathInUnknownProtos,
       "a3ComPathOutOctets": a3ComPathOutOctets,
       "a3ComPathOutUcastPkts": a3ComPathOutUcastPkts,
       "a3ComPathOutNUcastPkts": a3ComPathOutNUcastPkts,
       "a3ComPathOutDiscards": a3ComPathOutDiscards,
       "a3ComPathOutErrors": a3ComPathOutErrors,
       "a3ComPathBaudRate": a3ComPathBaudRate,
       "a3ComPathDuplex": a3ComPathDuplex,
       "a3ComPort": a3ComPort,
       "a3ComPortNumber": a3ComPortNumber,
       "a3ComPortTable": a3ComPortTable,
       "a3ComPortEntry": a3ComPortEntry,
       "a3ComPortIndex": a3ComPortIndex,
       "a3ComPortOwner": a3ComPortOwner,
       "a3ComPortBoundaryRoute": a3ComPortBoundaryRoute,
       "a3ComPortBoundaryEncap": a3ComPortBoundaryEncap,
       "a3ComPortCosInterleave": a3ComPortCosInterleave,
       "a3ComPortMacAddrFmtARP": a3ComPortMacAddrFmtARP,
       "a3ComPortMacAddrFmtIPX": a3ComPortMacAddrFmtIPX,
       "a3ComPortMacAddrFmtXNS": a3ComPortMacAddrFmtXNS,
       "a3ComPortPath": a3ComPortPath,
       "a3ComQueueInterleave1": a3ComQueueInterleave1,
       "a3ComQueueInterleave2": a3ComQueueInterleave2,
       "a3ComQueuePattern": a3ComQueuePattern,
       "a3ComPortAsOwnerTimer": a3ComPortAsOwnerTimer,
       "a3ComSmartFilteringCtl": a3ComSmartFilteringCtl,
       "a3ComBrCentralMacCtl": a3ComBrCentralMacCtl,
       "a3ComPortLabel": a3ComPortLabel,
       "a3ComPortCircuitID": a3ComPortCircuitID,
       "a3ComPortStatus": a3ComPortStatus,
       "a3ComPortName": a3ComPortName,
       "a3ComPortVirtual": a3ComPortVirtual,
       "a3ComQueueThrottle": a3ComQueueThrottle,
       "a3ComPortInCallerId": a3ComPortInCallerId,
       "a3ComPortCompType": a3ComPortCompType,
       "a3ComPortX25ProtID": a3ComPortX25ProtID,
       "a3ComPortIbmTraffic": a3ComPortIbmTraffic,
       "a3ComDefaultPriority": a3ComDefaultPriority,
       "a3ComPathDial": a3ComPathDial,
       "a3ComPathDialNumber": a3ComPathDialNumber,
       "a3ComPathDialTable": a3ComPathDialTable,
       "a3ComPathDialEntry": a3ComPathDialEntry,
       "a3ComPathDialIndex": a3ComPathDialIndex,
       "a3ComPathDialType": a3ComPathDialType,
       "a3ComPathDialCtl": a3ComPathDialCtl,
       "a3ComPathDialAction": a3ComPathDialAction,
       "a3ComPathDialNum": a3ComPathDialNum,
       "a3ComPathDialDodIdleTime": a3ComPathDialDodIdleTime,
       "a3ComPathDialMode": a3ComPathDialMode,
       "a3ComPathDialDynCont": a3ComPathDialDynCont,
       "a3ComPathDialLocalDialNumber": a3ComPathDialLocalDialNumber,
       "a3ComPathDialLocalSubAddress": a3ComPathDialLocalSubAddress,
       "a3ComPathDialSPIDDN1": a3ComPathDialSPIDDN1,
       "a3ComPathDialSPIDDN2": a3ComPathDialSPIDDN2,
       "a3ComPathDialRateAdaption": a3ComPathDialRateAdaption,
       "a3ComPathDialSwitchType": a3ComPathDialSwitchType,
       "a3ComPathDialExDevType": a3ComPathDialExDevType,
       "a3ComPortDial": a3ComPortDial,
       "a3ComPortDIALNumber": a3ComPortDIALNumber,
       "a3ComPortDialTable": a3ComPortDialTable,
       "a3ComPortDialEntry": a3ComPortDialEntry,
       "a3ComPortDialIndex": a3ComPortDialIndex,
       "a3ComPortDialDisasterCtl": a3ComPortDialDisasterCtl,
       "a3ComPortDialBandOnDmnd": a3ComPortDialBandOnDmnd,
       "a3ComPortDialDebounceTimeUp": a3ComPortDialDebounceTimeUp,
       "a3ComPortDialDebounceTimeDown": a3ComPortDialDebounceTimeDown,
       "a3ComPortDialInitState": a3ComPortDialInitState,
       "a3ComPortDialRcvrState": a3ComPortDialRcvrState,
       "a3ComPortDialAction": a3ComPortDialAction,
       "a3ComPortDialDodIdleTime": a3ComPortDialDodIdleTime,
       "a3ComPortDialIdleTime": a3ComPortDialIdleTime,
       "a3ComPortDialDodCallsMade": a3ComPortDialDodCallsMade,
       "a3ComPortDialDodCallsFail": a3ComPortDialDodCallsFail,
       "a3ComPortDialDodUpTime": a3ComPortDialDodUpTime,
       "a3ComPortDialDodPktsOut": a3ComPortDialDodPktsOut,
       "a3ComPortDialBODTHreshold": a3ComPortDialBODTHreshold,
       "a3ComPortDialPoolPrefTable": a3ComPortDialPoolPrefTable,
       "a3ComPortDialPoolPrefEntry": a3ComPortDialPoolPrefEntry,
       "a3ComPortDialPoolPrefPort": a3ComPortDialPoolPrefPort,
       "a3ComPortDialPoolPrefPathPos": a3ComPortDialPoolPrefPathPos,
       "a3ComPortDialPoolPrefPathNum": a3ComPortDialPoolPrefPathNum,
       "a3ComPortDialPoolPrefStatus": a3ComPortDialPoolPrefStatus,
       "a3ComPortDialPhoneListTable": a3ComPortDialPhoneListTable,
       "a3ComPortDialPhoneListEntry": a3ComPortDialPhoneListEntry,
       "a3ComPortDialPhoneListPort": a3ComPortDialPhoneListPort,
       "a3ComPortDialPhoneListPos": a3ComPortDialPhoneListPos,
       "a3ComPortDialPhoneListPhoneNo": a3ComPortDialPhoneListPhoneNo,
       "a3ComPortDialPhoneListType": a3ComPortDialPhoneListType,
       "a3ComPortDialPhoneListBaud": a3ComPortDialPhoneListBaud,
       "a3ComPortDialPhoneListStatus": a3ComPortDialPhoneListStatus}
)
