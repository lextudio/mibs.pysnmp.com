# SNMP MIB module (ACC-PPP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-PPP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:45 2024
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

(ifOperStatus,) = mibBuilder.importSymbols(
    "ACC-FAKE",
    "ifOperStatus")

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accMlPppIndex,
 accMultilink) = mibBuilder.importSymbols(
    "ACC-MULTILINK",
    "accMlPppIndex",
    "accMultilink")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
 NotificationType,
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
    "NotificationType",
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



class CallAddress(OctetString):
    """Custom type CallAddress based on OctetString"""




class BackupPort(Integer32):
    """Custom type BackupPort based on Integer32"""




class PhysicalPort(Integer32):
    """Custom type PhysicalPort based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccMlPppCompressTable_Object = MibTable
accMlPppCompressTable = _AccMlPppCompressTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 7)
)
if mibBuilder.loadTexts:
    accMlPppCompressTable.setStatus("mandatory")
_AccMlPppCompressEntry_Object = MibTableRow
accMlPppCompressEntry = _AccMlPppCompressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 7, 1)
)
accMlPppCompressEntry.setIndexNames(
    (0, "ACC-PPP", "accMlPppCompressIndex"),
)
if mibBuilder.loadTexts:
    accMlPppCompressEntry.setStatus("mandatory")
_AccMlPppCompressIndex_Type = Integer32
_AccMlPppCompressIndex_Object = MibTableColumn
accMlPppCompressIndex = _AccMlPppCompressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 7, 1, 1),
    _AccMlPppCompressIndex_Type()
)
accMlPppCompressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressIndex.setStatus("mandatory")
_AccMlPppCompressMsgLevel_Type = Integer32
_AccMlPppCompressMsgLevel_Object = MibTableColumn
accMlPppCompressMsgLevel = _AccMlPppCompressMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 7, 1, 2),
    _AccMlPppCompressMsgLevel_Type()
)
accMlPppCompressMsgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressMsgLevel.setStatus("mandatory")


class _AccMlPppCompressMethod_Type(Integer32):
    """Custom type accMlPppCompressMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("mppc", 7),
          ("nego", 2),
          ("none", 1),
          ("stac-extd", 5),
          ("stac-none", 6),
          ("stac-seqn", 4),
          ("vendor", 3))
    )


_AccMlPppCompressMethod_Type.__name__ = "Integer32"
_AccMlPppCompressMethod_Object = MibTableColumn
accMlPppCompressMethod = _AccMlPppCompressMethod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 7, 1, 3),
    _AccMlPppCompressMethod_Type()
)
accMlPppCompressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMlPppCompressMethod.setStatus("mandatory")


class _AccMlPppCompressStream_Type(Integer32):
    """Custom type accMlPppCompressStream based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("stream", 2))
    )


_AccMlPppCompressStream_Type.__name__ = "Integer32"
_AccMlPppCompressStream_Object = MibTableColumn
accMlPppCompressStream = _AccMlPppCompressStream_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 7, 1, 4),
    _AccMlPppCompressStream_Type()
)
accMlPppCompressStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMlPppCompressStream.setStatus("mandatory")


class _AccMlPppCompressNegoMethodIn_Type(Integer32):
    """Custom type accMlPppCompressNegoMethodIn based on Integer32"""
    defaultValue = 1

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
        *(("mppc", 6),
          ("none", 1),
          ("stac-extd", 4),
          ("stac-none", 5),
          ("stac-seqn", 3),
          ("vendor", 2))
    )


_AccMlPppCompressNegoMethodIn_Type.__name__ = "Integer32"
_AccMlPppCompressNegoMethodIn_Object = MibTableColumn
accMlPppCompressNegoMethodIn = _AccMlPppCompressNegoMethodIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 7, 1, 5),
    _AccMlPppCompressNegoMethodIn_Type()
)
accMlPppCompressNegoMethodIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMlPppCompressNegoMethodIn.setStatus("mandatory")


class _AccMlPppCompressNegoMethodOut_Type(Integer32):
    """Custom type accMlPppCompressNegoMethodOut based on Integer32"""
    defaultValue = 1

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
        *(("mppc", 6),
          ("none", 1),
          ("stac-extd", 4),
          ("stac-none", 5),
          ("stac-seqn", 3),
          ("vendor", 2))
    )


_AccMlPppCompressNegoMethodOut_Type.__name__ = "Integer32"
_AccMlPppCompressNegoMethodOut_Object = MibTableColumn
accMlPppCompressNegoMethodOut = _AccMlPppCompressNegoMethodOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 7, 1, 6),
    _AccMlPppCompressNegoMethodOut_Type()
)
accMlPppCompressNegoMethodOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMlPppCompressNegoMethodOut.setStatus("mandatory")


class _AccMlPppCompressNegoStreamIn_Type(Integer32):
    """Custom type accMlPppCompressNegoStreamIn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("stream", 2))
    )


_AccMlPppCompressNegoStreamIn_Type.__name__ = "Integer32"
_AccMlPppCompressNegoStreamIn_Object = MibTableColumn
accMlPppCompressNegoStreamIn = _AccMlPppCompressNegoStreamIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 7, 1, 7),
    _AccMlPppCompressNegoStreamIn_Type()
)
accMlPppCompressNegoStreamIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMlPppCompressNegoStreamIn.setStatus("mandatory")


class _AccMlPppCompressNegoStreamOut_Type(Integer32):
    """Custom type accMlPppCompressNegoStreamOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("stream", 2))
    )


_AccMlPppCompressNegoStreamOut_Type.__name__ = "Integer32"
_AccMlPppCompressNegoStreamOut_Object = MibTableColumn
accMlPppCompressNegoStreamOut = _AccMlPppCompressNegoStreamOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 7, 1, 8),
    _AccMlPppCompressNegoStreamOut_Type()
)
accMlPppCompressNegoStreamOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMlPppCompressNegoStreamOut.setStatus("mandatory")
_AccMlPppCompressStatTable_Object = MibTable
accMlPppCompressStatTable = _AccMlPppCompressStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8)
)
if mibBuilder.loadTexts:
    accMlPppCompressStatTable.setStatus("mandatory")
_AccMlPppCompressStatEntry_Object = MibTableRow
accMlPppCompressStatEntry = _AccMlPppCompressStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1)
)
accMlPppCompressStatEntry.setIndexNames(
    (0, "ACC-PPP", "accMlPppCompressStatIndex"),
)
if mibBuilder.loadTexts:
    accMlPppCompressStatEntry.setStatus("mandatory")
_AccMlPppCompressStatIndex_Type = Integer32
_AccMlPppCompressStatIndex_Object = MibTableColumn
accMlPppCompressStatIndex = _AccMlPppCompressStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 1),
    _AccMlPppCompressStatIndex_Type()
)
accMlPppCompressStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatIndex.setStatus("mandatory")


class _AccMlPppCompressStatStatus_Type(Integer32):
    """Custom type accMlPppCompressStatStatus based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccMlPppCompressStatStatus_Type.__name__ = "Integer32"
_AccMlPppCompressStatStatus_Object = MibTableColumn
accMlPppCompressStatStatus = _AccMlPppCompressStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 2),
    _AccMlPppCompressStatStatus_Type()
)
accMlPppCompressStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatStatus.setStatus("mandatory")
_AccMlPppCompressStatAvgCompIn_Type = Gauge32
_AccMlPppCompressStatAvgCompIn_Object = MibTableColumn
accMlPppCompressStatAvgCompIn = _AccMlPppCompressStatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 3),
    _AccMlPppCompressStatAvgCompIn_Type()
)
accMlPppCompressStatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatAvgCompIn.setStatus("mandatory")
_AccMlPppCompressStatAvgCompOut_Type = Gauge32
_AccMlPppCompressStatAvgCompOut_Object = MibTableColumn
accMlPppCompressStatAvgCompOut = _AccMlPppCompressStatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 4),
    _AccMlPppCompressStatAvgCompOut_Type()
)
accMlPppCompressStatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatAvgCompOut.setStatus("mandatory")
_AccMlPppCompressStatInOctets_Type = Counter32
_AccMlPppCompressStatInOctets_Object = MibTableColumn
accMlPppCompressStatInOctets = _AccMlPppCompressStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 5),
    _AccMlPppCompressStatInOctets_Type()
)
accMlPppCompressStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatInOctets.setStatus("mandatory")
_AccMlPppCompressStatOutOctets_Type = Counter32
_AccMlPppCompressStatOutOctets_Object = MibTableColumn
accMlPppCompressStatOutOctets = _AccMlPppCompressStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 6),
    _AccMlPppCompressStatOutOctets_Type()
)
accMlPppCompressStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatOutOctets.setStatus("mandatory")
_AccMlPppCompressStatInPackets_Type = Counter32
_AccMlPppCompressStatInPackets_Object = MibTableColumn
accMlPppCompressStatInPackets = _AccMlPppCompressStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 7),
    _AccMlPppCompressStatInPackets_Type()
)
accMlPppCompressStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatInPackets.setStatus("mandatory")
_AccMlPppCompressStatOutPackets_Type = Counter32
_AccMlPppCompressStatOutPackets_Object = MibTableColumn
accMlPppCompressStatOutPackets = _AccMlPppCompressStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 8),
    _AccMlPppCompressStatOutPackets_Type()
)
accMlPppCompressStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatOutPackets.setStatus("mandatory")
_AccMlPppCompressUnCompInStats_Type = Counter32
_AccMlPppCompressUnCompInStats_Object = MibTableColumn
accMlPppCompressUnCompInStats = _AccMlPppCompressUnCompInStats_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 9),
    _AccMlPppCompressUnCompInStats_Type()
)
accMlPppCompressUnCompInStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressUnCompInStats.setStatus("mandatory")
_AccMlPppCompressUnCompOutStats_Type = Counter32
_AccMlPppCompressUnCompOutStats_Object = MibTableColumn
accMlPppCompressUnCompOutStats = _AccMlPppCompressUnCompOutStats_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 10),
    _AccMlPppCompressUnCompOutStats_Type()
)
accMlPppCompressUnCompOutStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressUnCompOutStats.setStatus("mandatory")
_AccMlPppCompressStatHdrErrors_Type = Counter32
_AccMlPppCompressStatHdrErrors_Object = MibTableColumn
accMlPppCompressStatHdrErrors = _AccMlPppCompressStatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 11),
    _AccMlPppCompressStatHdrErrors_Type()
)
accMlPppCompressStatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatHdrErrors.setStatus("mandatory")
_AccMlPppCompressStatResyncs_Type = Counter32
_AccMlPppCompressStatResyncs_Object = MibTableColumn
accMlPppCompressStatResyncs = _AccMlPppCompressStatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 12),
    _AccMlPppCompressStatResyncs_Type()
)
accMlPppCompressStatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatResyncs.setStatus("mandatory")
_AccMlPppCompressStatNoEndMarks_Type = Counter32
_AccMlPppCompressStatNoEndMarks_Object = MibTableColumn
accMlPppCompressStatNoEndMarks = _AccMlPppCompressStatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 13),
    _AccMlPppCompressStatNoEndMarks_Type()
)
accMlPppCompressStatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatNoEndMarks.setStatus("mandatory")
_AccMlPppCompressStatNoAvailBufs_Type = Counter32
_AccMlPppCompressStatNoAvailBufs_Object = MibTableColumn
accMlPppCompressStatNoAvailBufs = _AccMlPppCompressStatNoAvailBufs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 14),
    _AccMlPppCompressStatNoAvailBufs_Type()
)
accMlPppCompressStatNoAvailBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatNoAvailBufs.setStatus("mandatory")
_AccMlPppCompressStatRcvResetReqs_Type = Counter32
_AccMlPppCompressStatRcvResetReqs_Object = MibTableColumn
accMlPppCompressStatRcvResetReqs = _AccMlPppCompressStatRcvResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 15),
    _AccMlPppCompressStatRcvResetReqs_Type()
)
accMlPppCompressStatRcvResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatRcvResetReqs.setStatus("mandatory")
_AccMlPppCompressStatRcvResetAcks_Type = Counter32
_AccMlPppCompressStatRcvResetAcks_Object = MibTableColumn
accMlPppCompressStatRcvResetAcks = _AccMlPppCompressStatRcvResetAcks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 16),
    _AccMlPppCompressStatRcvResetAcks_Type()
)
accMlPppCompressStatRcvResetAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatRcvResetAcks.setStatus("mandatory")
_AccMlPppCompressStatSndResetReqs_Type = Counter32
_AccMlPppCompressStatSndResetReqs_Object = MibTableColumn
accMlPppCompressStatSndResetReqs = _AccMlPppCompressStatSndResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 17),
    _AccMlPppCompressStatSndResetReqs_Type()
)
accMlPppCompressStatSndResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatSndResetReqs.setStatus("mandatory")
_AccMlPppCompressStatSndResetAcks_Type = Counter32
_AccMlPppCompressStatSndResetAcks_Object = MibTableColumn
accMlPppCompressStatSndResetAcks = _AccMlPppCompressStatSndResetAcks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 8, 1, 18),
    _AccMlPppCompressStatSndResetAcks_Type()
)
accMlPppCompressStatSndResetAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppCompressStatSndResetAcks.setStatus("mandatory")
_AccDial_ObjectIdentity = ObjectIdentity
accDial = _AccDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31)
)
_AccDialBackupTable_Object = MibTable
accDialBackupTable = _AccDialBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1)
)
if mibBuilder.loadTexts:
    accDialBackupTable.setStatus("mandatory")
_AccDialBackupEntry_Object = MibTableRow
accDialBackupEntry = _AccDialBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1)
)
accDialBackupEntry.setIndexNames(
    (0, "ACC-PPP", "accDialBackupPrimary"),
)
if mibBuilder.loadTexts:
    accDialBackupEntry.setStatus("mandatory")
_AccDialBackupPort_Type = BackupPort
_AccDialBackupPort_Object = MibTableColumn
accDialBackupPort = _AccDialBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 1),
    _AccDialBackupPort_Type()
)
accDialBackupPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupPort.setStatus("mandatory")
_AccDialBackupPrimary_Type = PhysicalPort
_AccDialBackupPrimary_Object = MibTableColumn
accDialBackupPrimary = _AccDialBackupPrimary_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 2),
    _AccDialBackupPrimary_Type()
)
accDialBackupPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialBackupPrimary.setStatus("mandatory")


class _AccDialBackupControl_Type(Integer32):
    """Custom type accDialBackupControl based on Integer32"""
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
        *(("demand", 3),
          ("master", 1),
          ("slave", 2))
    )


_AccDialBackupControl_Type.__name__ = "Integer32"
_AccDialBackupControl_Object = MibTableColumn
accDialBackupControl = _AccDialBackupControl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 3),
    _AccDialBackupControl_Type()
)
accDialBackupControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupControl.setStatus("mandatory")


class _AccDialBackupRetry_Type(Integer32):
    """Custom type accDialBackupRetry based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccDialBackupRetry_Type.__name__ = "Integer32"
_AccDialBackupRetry_Object = MibTableColumn
accDialBackupRetry = _AccDialBackupRetry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 4),
    _AccDialBackupRetry_Type()
)
accDialBackupRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupRetry.setStatus("mandatory")


class _AccDialBackupDamp_Type(Integer32):
    """Custom type accDialBackupDamp based on Integer32"""
    defaultValue = 3


_AccDialBackupDamp_Object = MibTableColumn
accDialBackupDamp = _AccDialBackupDamp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 5),
    _AccDialBackupDamp_Type()
)
accDialBackupDamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupDamp.setStatus("mandatory")


class _AccDialBackupCallCongestion_Type(Integer32):
    """Custom type accDialBackupCallCongestion based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_AccDialBackupCallCongestion_Type.__name__ = "Integer32"
_AccDialBackupCallCongestion_Object = MibTableColumn
accDialBackupCallCongestion = _AccDialBackupCallCongestion_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 6),
    _AccDialBackupCallCongestion_Type()
)
accDialBackupCallCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupCallCongestion.setStatus("mandatory")


class _AccDialBackupClearCongestion_Type(Integer32):
    """Custom type accDialBackupClearCongestion based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_AccDialBackupClearCongestion_Type.__name__ = "Integer32"
_AccDialBackupClearCongestion_Object = MibTableColumn
accDialBackupClearCongestion = _AccDialBackupClearCongestion_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 7),
    _AccDialBackupClearCongestion_Type()
)
accDialBackupClearCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupClearCongestion.setStatus("mandatory")


class _AccDialBackupCallError_Type(Integer32):
    """Custom type accDialBackupCallError based on Integer32"""
    defaultValue = 5


_AccDialBackupCallError_Object = MibTableColumn
accDialBackupCallError = _AccDialBackupCallError_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 8),
    _AccDialBackupCallError_Type()
)
accDialBackupCallError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupCallError.setStatus("mandatory")
_AccDialBackupCallAddress_Type = CallAddress
_AccDialBackupCallAddress_Object = MibTableColumn
accDialBackupCallAddress = _AccDialBackupCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 9),
    _AccDialBackupCallAddress_Type()
)
accDialBackupCallAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupCallAddress.setStatus("mandatory")


class _AccDialBackupStatus_Type(Integer32):
    """Custom type accDialBackupStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccDialBackupStatus_Type.__name__ = "Integer32"
_AccDialBackupStatus_Object = MibTableColumn
accDialBackupStatus = _AccDialBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 10),
    _AccDialBackupStatus_Type()
)
accDialBackupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupStatus.setStatus("mandatory")


class _AccDialBackupState_Type(Integer32):
    """Custom type accDialBackupState based on Integer32"""
    defaultValue = 6

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
        *(("backup", 4),
          ("clear", 6),
          ("congestIn", 2),
          ("congestOut", 1),
          ("errors", 3),
          ("manual", 5))
    )


_AccDialBackupState_Type.__name__ = "Integer32"
_AccDialBackupState_Object = MibTableColumn
accDialBackupState = _AccDialBackupState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 11),
    _AccDialBackupState_Type()
)
accDialBackupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupState.setStatus("mandatory")
_AccDialPortTable_Object = MibTable
accDialPortTable = _AccDialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2)
)
if mibBuilder.loadTexts:
    accDialPortTable.setStatus("mandatory")
_AccDialPortEntry_Object = MibTableRow
accDialPortEntry = _AccDialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1)
)
accDialPortEntry.setIndexNames(
    (0, "ACC-PPP", "accDialPortIndex"),
)
if mibBuilder.loadTexts:
    accDialPortEntry.setStatus("mandatory")
_AccDialPortIndex_Type = Integer32
_AccDialPortIndex_Object = MibTableColumn
accDialPortIndex = _AccDialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 1),
    _AccDialPortIndex_Type()
)
accDialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortIndex.setStatus("mandatory")


class _AccDialPortContents_Type(Integer32):
    """Custom type accDialPortContents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialPortContents_Type.__name__ = "Integer32"
_AccDialPortContents_Object = MibTableColumn
accDialPortContents = _AccDialPortContents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 2),
    _AccDialPortContents_Type()
)
accDialPortContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortContents.setStatus("mandatory")


class _AccDialPortStationType_Type(Integer32):
    """Custom type accDialPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demand", 3),
          ("master", 1),
          ("slave", 2))
    )


_AccDialPortStationType_Type.__name__ = "Integer32"
_AccDialPortStationType_Object = MibTableColumn
accDialPortStationType = _AccDialPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 3),
    _AccDialPortStationType_Type()
)
accDialPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortStationType.setStatus("mandatory")


class _AccDialPortAdminState_Type(Integer32):
    """Custom type accDialPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_AccDialPortAdminState_Type.__name__ = "Integer32"
_AccDialPortAdminState_Object = MibTableColumn
accDialPortAdminState = _AccDialPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 4),
    _AccDialPortAdminState_Type()
)
accDialPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortAdminState.setStatus("mandatory")


class _AccDialPortCallState_Type(Integer32):
    """Custom type accDialPortCallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("call", 2),
          ("clear", 1))
    )


_AccDialPortCallState_Type.__name__ = "Integer32"
_AccDialPortCallState_Object = MibTableColumn
accDialPortCallState = _AccDialPortCallState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 5),
    _AccDialPortCallState_Type()
)
accDialPortCallState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortCallState.setStatus("mandatory")
_AccDialPortRetryInterval_Type = TimeTicks
_AccDialPortRetryInterval_Object = MibTableColumn
accDialPortRetryInterval = _AccDialPortRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 6),
    _AccDialPortRetryInterval_Type()
)
accDialPortRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortRetryInterval.setStatus("mandatory")
_AccDialPortRetryCount_Type = Integer32
_AccDialPortRetryCount_Object = MibTableColumn
accDialPortRetryCount = _AccDialPortRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 7),
    _AccDialPortRetryCount_Type()
)
accDialPortRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortRetryCount.setStatus("mandatory")
_AccDialPortClearingInterv_Type = TimeTicks
_AccDialPortClearingInterv_Object = MibTableColumn
accDialPortClearingInterv = _AccDialPortClearingInterv_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 8),
    _AccDialPortClearingInterv_Type()
)
accDialPortClearingInterv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortClearingInterv.setStatus("mandatory")
_AccDialPortMessageLevel_Type = Integer32
_AccDialPortMessageLevel_Object = MibTableColumn
accDialPortMessageLevel = _AccDialPortMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 9),
    _AccDialPortMessageLevel_Type()
)
accDialPortMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortMessageLevel.setStatus("mandatory")
_AccDialPortPhysicalPort_Type = Integer32
_AccDialPortPhysicalPort_Object = MibTableColumn
accDialPortPhysicalPort = _AccDialPortPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 10),
    _AccDialPortPhysicalPort_Type()
)
accDialPortPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortPhysicalPort.setStatus("mandatory")
_AccDialPortCallAddress_Type = OctetString
_AccDialPortCallAddress_Object = MibTableColumn
accDialPortCallAddress = _AccDialPortCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 11),
    _AccDialPortCallAddress_Type()
)
accDialPortCallAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortCallAddress.setStatus("mandatory")
_AccDialPortPhysicalPortStr_Type = OctetString
_AccDialPortPhysicalPortStr_Object = MibTableColumn
accDialPortPhysicalPortStr = _AccDialPortPhysicalPortStr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 12),
    _AccDialPortPhysicalPortStr_Type()
)
accDialPortPhysicalPortStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortPhysicalPortStr.setStatus("mandatory")
_AccDialPortCallAddressStr_Type = OctetString
_AccDialPortCallAddressStr_Object = MibTableColumn
accDialPortCallAddressStr = _AccDialPortCallAddressStr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 13),
    _AccDialPortCallAddressStr_Type()
)
accDialPortCallAddressStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortCallAddressStr.setStatus("mandatory")
_AccDialPortPassword_Type = OctetString
_AccDialPortPassword_Object = MibTableColumn
accDialPortPassword = _AccDialPortPassword_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 14),
    _AccDialPortPassword_Type()
)
accDialPortPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortPassword.setStatus("mandatory")
_AccDialPortName_Type = OctetString
_AccDialPortName_Object = MibTableColumn
accDialPortName = _AccDialPortName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 15),
    _AccDialPortName_Type()
)
accDialPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortName.setStatus("mandatory")


class _AccDialPortAuthType_Type(Integer32):
    """Custom type accDialPortAuthType based on Integer32"""
    defaultValue = 2

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
        *(("chap", 2),
          ("chappap", 3),
          ("none", 4),
          ("pap", 1),
          ("token-chap", 5))
    )


_AccDialPortAuthType_Type.__name__ = "Integer32"
_AccDialPortAuthType_Object = MibTableColumn
accDialPortAuthType = _AccDialPortAuthType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 16),
    _AccDialPortAuthType_Type()
)
accDialPortAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortAuthType.setStatus("mandatory")


class _AccDialPortSessionTimeout_Type(Integer32):
    """Custom type accDialPortSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AccDialPortSessionTimeout_Type.__name__ = "Integer32"
_AccDialPortSessionTimeout_Object = MibTableColumn
accDialPortSessionTimeout = _AccDialPortSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 17),
    _AccDialPortSessionTimeout_Type()
)
accDialPortSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortSessionTimeout.setStatus("mandatory")


class _AccDialPortPriority_Type(Integer32):
    """Custom type accDialPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AccDialPortPriority_Type.__name__ = "Integer32"
_AccDialPortPriority_Object = MibTableColumn
accDialPortPriority = _AccDialPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 18),
    _AccDialPortPriority_Type()
)
accDialPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortPriority.setStatus("mandatory")


class _AccDialPortCallBack_Type(Integer32):
    """Custom type accDialPortCallBack based on Integer32"""
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


_AccDialPortCallBack_Type.__name__ = "Integer32"
_AccDialPortCallBack_Object = MibTableColumn
accDialPortCallBack = _AccDialPortCallBack_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 19),
    _AccDialPortCallBack_Type()
)
accDialPortCallBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortCallBack.setStatus("mandatory")


class _AccDialPortProtocol_Type(Integer32):
    """Custom type accDialPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 1),
          ("x25", 2))
    )


_AccDialPortProtocol_Type.__name__ = "Integer32"
_AccDialPortProtocol_Object = MibTableColumn
accDialPortProtocol = _AccDialPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 20),
    _AccDialPortProtocol_Type()
)
accDialPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortProtocol.setStatus("mandatory")


class _AccDialPortAuthPeer_Type(Integer32):
    """Custom type accDialPortAuthPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 2),
          ("none", 1))
    )


_AccDialPortAuthPeer_Type.__name__ = "Integer32"
_AccDialPortAuthPeer_Object = MibTableColumn
accDialPortAuthPeer = _AccDialPortAuthPeer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 21),
    _AccDialPortAuthPeer_Type()
)
accDialPortAuthPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortAuthPeer.setStatus("mandatory")


class _AccDialPortPromptState_Type(Integer32):
    """Custom type accDialPortPromptState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 7),
          ("idle", 6),
          ("inprocess", 5),
          ("login", 1),
          ("newpin", 3),
          ("nexttoken", 4),
          ("reenter", 2))
    )


_AccDialPortPromptState_Type.__name__ = "Integer32"
_AccDialPortPromptState_Object = MibTableColumn
accDialPortPromptState = _AccDialPortPromptState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 22),
    _AccDialPortPromptState_Type()
)
accDialPortPromptState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortPromptState.setStatus("mandatory")
_AccDialPortLogin_Type = OctetString
_AccDialPortLogin_Object = MibTableColumn
accDialPortLogin = _AccDialPortLogin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 23),
    _AccDialPortLogin_Type()
)
accDialPortLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortLogin.setStatus("mandatory")
_AccDialPortStatTable_Object = MibTable
accDialPortStatTable = _AccDialPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3)
)
if mibBuilder.loadTexts:
    accDialPortStatTable.setStatus("mandatory")
_AccDialPortStatEntry_Object = MibTableRow
accDialPortStatEntry = _AccDialPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1)
)
accDialPortStatEntry.setIndexNames(
    (0, "ACC-PPP", "accDialPortStatIndex"),
)
if mibBuilder.loadTexts:
    accDialPortStatEntry.setStatus("mandatory")
_AccDialPortStatIndex_Type = Integer32
_AccDialPortStatIndex_Object = MibTableColumn
accDialPortStatIndex = _AccDialPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 1),
    _AccDialPortStatIndex_Type()
)
accDialPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatIndex.setStatus("mandatory")
_AccDialPortStatActPhysPort_Type = OctetString
_AccDialPortStatActPhysPort_Object = MibTableColumn
accDialPortStatActPhysPort = _AccDialPortStatActPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 2),
    _AccDialPortStatActPhysPort_Type()
)
accDialPortStatActPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatActPhysPort.setStatus("mandatory")
_AccDialPortStatState_Type = Integer32
_AccDialPortStatState_Object = MibTableColumn
accDialPortStatState = _AccDialPortStatState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 3),
    _AccDialPortStatState_Type()
)
accDialPortStatState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortStatState.setStatus("mandatory")
_AccDialPortStatTrigFwdr_Type = OctetString
_AccDialPortStatTrigFwdr_Object = MibTableColumn
accDialPortStatTrigFwdr = _AccDialPortStatTrigFwdr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 4),
    _AccDialPortStatTrigFwdr_Type()
)
accDialPortStatTrigFwdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatTrigFwdr.setStatus("mandatory")
_AccDialPortStatElapsedTime_Type = TimeTicks
_AccDialPortStatElapsedTime_Object = MibTableColumn
accDialPortStatElapsedTime = _AccDialPortStatElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 5),
    _AccDialPortStatElapsedTime_Type()
)
accDialPortStatElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatElapsedTime.setStatus("mandatory")
_AccDialPortStatTrigSrcAddr_Type = OctetString
_AccDialPortStatTrigSrcAddr_Object = MibTableColumn
accDialPortStatTrigSrcAddr = _AccDialPortStatTrigSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 6),
    _AccDialPortStatTrigSrcAddr_Type()
)
accDialPortStatTrigSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatTrigSrcAddr.setStatus("mandatory")
_AccDialPortStatTrigCallAddr_Type = OctetString
_AccDialPortStatTrigCallAddr_Object = MibTableColumn
accDialPortStatTrigCallAddr = _AccDialPortStatTrigCallAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 7),
    _AccDialPortStatTrigCallAddr_Type()
)
accDialPortStatTrigCallAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatTrigCallAddr.setStatus("mandatory")
_AccDialPortStatSuccessOuts_Type = Counter32
_AccDialPortStatSuccessOuts_Object = MibTableColumn
accDialPortStatSuccessOuts = _AccDialPortStatSuccessOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 8),
    _AccDialPortStatSuccessOuts_Type()
)
accDialPortStatSuccessOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatSuccessOuts.setStatus("mandatory")
_AccDialPortStatUnsuccessOuts_Type = Counter32
_AccDialPortStatUnsuccessOuts_Object = MibTableColumn
accDialPortStatUnsuccessOuts = _AccDialPortStatUnsuccessOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 9),
    _AccDialPortStatUnsuccessOuts_Type()
)
accDialPortStatUnsuccessOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatUnsuccessOuts.setStatus("mandatory")
_AccDialPortStatSuccessIns_Type = Counter32
_AccDialPortStatSuccessIns_Object = MibTableColumn
accDialPortStatSuccessIns = _AccDialPortStatSuccessIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 10),
    _AccDialPortStatSuccessIns_Type()
)
accDialPortStatSuccessIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatSuccessIns.setStatus("mandatory")
_AccDialPortStatUnsuccessIns_Type = Counter32
_AccDialPortStatUnsuccessIns_Object = MibTableColumn
accDialPortStatUnsuccessIns = _AccDialPortStatUnsuccessIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 11),
    _AccDialPortStatUnsuccessIns_Type()
)
accDialPortStatUnsuccessIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatUnsuccessIns.setStatus("mandatory")
_AccDialPortStatAuthTypeClashes_Type = Counter32
_AccDialPortStatAuthTypeClashes_Object = MibTableColumn
accDialPortStatAuthTypeClashes = _AccDialPortStatAuthTypeClashes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 12),
    _AccDialPortStatAuthTypeClashes_Type()
)
accDialPortStatAuthTypeClashes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatAuthTypeClashes.setStatus("mandatory")


class _AccDialPortStatDisconnReasons_Type(Integer32):
    """Custom type accDialPortStatDisconnReasons based on Integer32"""
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
        *(("idletimeout", 4),
          ("locfail", 3),
          ("mgmtreq", 1),
          ("netfail", 2),
          ("sessiontimeout", 5))
    )


_AccDialPortStatDisconnReasons_Type.__name__ = "Integer32"
_AccDialPortStatDisconnReasons_Object = MibTableColumn
accDialPortStatDisconnReasons = _AccDialPortStatDisconnReasons_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 13),
    _AccDialPortStatDisconnReasons_Type()
)
accDialPortStatDisconnReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatDisconnReasons.setStatus("mandatory")
_AccDialOrigAtTable_Object = MibTable
accDialOrigAtTable = _AccDialOrigAtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4)
)
if mibBuilder.loadTexts:
    accDialOrigAtTable.setStatus("mandatory")
_AccDialOrigAtEntry_Object = MibTableRow
accDialOrigAtEntry = _AccDialOrigAtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1)
)
accDialOrigAtEntry.setIndexNames(
    (0, "ACC-PPP", "accDialOrigAtDestStart"),
    (0, "ACC-PPP", "accDialOrigAtDestEnd"),
    (0, "ACC-PPP", "accDialOrigAtSourceStart"),
    (0, "ACC-PPP", "accDialOrigAtSourceEnd"),
)
if mibBuilder.loadTexts:
    accDialOrigAtEntry.setStatus("mandatory")


class _AccDialOrigAtStatus_Type(Integer32):
    """Custom type accDialOrigAtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigAtStatus_Type.__name__ = "Integer32"
_AccDialOrigAtStatus_Object = MibTableColumn
accDialOrigAtStatus = _AccDialOrigAtStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 1),
    _AccDialOrigAtStatus_Type()
)
accDialOrigAtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtStatus.setStatus("mandatory")
_AccDialOrigAtDestStart_Type = OctetString
_AccDialOrigAtDestStart_Object = MibTableColumn
accDialOrigAtDestStart = _AccDialOrigAtDestStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 2),
    _AccDialOrigAtDestStart_Type()
)
accDialOrigAtDestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtDestStart.setStatus("mandatory")
_AccDialOrigAtDestEnd_Type = OctetString
_AccDialOrigAtDestEnd_Object = MibTableColumn
accDialOrigAtDestEnd = _AccDialOrigAtDestEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 3),
    _AccDialOrigAtDestEnd_Type()
)
accDialOrigAtDestEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtDestEnd.setStatus("mandatory")
_AccDialOrigAtSourceStart_Type = OctetString
_AccDialOrigAtSourceStart_Object = MibTableColumn
accDialOrigAtSourceStart = _AccDialOrigAtSourceStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 4),
    _AccDialOrigAtSourceStart_Type()
)
accDialOrigAtSourceStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtSourceStart.setStatus("mandatory")
_AccDialOrigAtSourceEnd_Type = OctetString
_AccDialOrigAtSourceEnd_Object = MibTableColumn
accDialOrigAtSourceEnd = _AccDialOrigAtSourceEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 5),
    _AccDialOrigAtSourceEnd_Type()
)
accDialOrigAtSourceEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtSourceEnd.setStatus("mandatory")


class _AccDialOrigAtTraffic_Type(Integer32):
    """Custom type accDialOrigAtTraffic based on Integer32"""
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
        *(("adsp", 7),
          ("aep", 4),
          ("any", 1),
          ("atp", 3),
          ("nbp", 2),
          ("nbpbroadcast", 8),
          ("nbpforwardreq", 11),
          ("nbplookup", 9),
          ("nbpreply", 10),
          ("rtmp", 5),
          ("zip", 6))
    )


_AccDialOrigAtTraffic_Type.__name__ = "Integer32"
_AccDialOrigAtTraffic_Object = MibTableColumn
accDialOrigAtTraffic = _AccDialOrigAtTraffic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 6),
    _AccDialOrigAtTraffic_Type()
)
accDialOrigAtTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtTraffic.setStatus("mandatory")


class _AccDialOrigAtAction_Type(Integer32):
    """Custom type accDialOrigAtAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigAtAction_Type.__name__ = "Integer32"
_AccDialOrigAtAction_Object = MibTableColumn
accDialOrigAtAction = _AccDialOrigAtAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 7),
    _AccDialOrigAtAction_Type()
)
accDialOrigAtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtAction.setStatus("mandatory")
_AccDialOrigDnTable_Object = MibTable
accDialOrigDnTable = _AccDialOrigDnTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5)
)
if mibBuilder.loadTexts:
    accDialOrigDnTable.setStatus("mandatory")
_AccDialOrigDnEntry_Object = MibTableRow
accDialOrigDnEntry = _AccDialOrigDnEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5, 1)
)
accDialOrigDnEntry.setIndexNames(
    (0, "ACC-PPP", "accDialOrigDnDestAddr"),
    (0, "ACC-PPP", "accDialOrigDnSourceAddr"),
)
if mibBuilder.loadTexts:
    accDialOrigDnEntry.setStatus("mandatory")


class _AccDialOrigDnStatus_Type(Integer32):
    """Custom type accDialOrigDnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigDnStatus_Type.__name__ = "Integer32"
_AccDialOrigDnStatus_Object = MibTableColumn
accDialOrigDnStatus = _AccDialOrigDnStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5, 1, 1),
    _AccDialOrigDnStatus_Type()
)
accDialOrigDnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigDnStatus.setStatus("mandatory")


class _AccDialOrigDnDestAddr_Type(Integer32):
    """Custom type accDialOrigDnDestAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDialOrigDnDestAddr_Type.__name__ = "Integer32"
_AccDialOrigDnDestAddr_Object = MibTableColumn
accDialOrigDnDestAddr = _AccDialOrigDnDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5, 1, 2),
    _AccDialOrigDnDestAddr_Type()
)
accDialOrigDnDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigDnDestAddr.setStatus("mandatory")


class _AccDialOrigDnSourceAddr_Type(Integer32):
    """Custom type accDialOrigDnSourceAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDialOrigDnSourceAddr_Type.__name__ = "Integer32"
_AccDialOrigDnSourceAddr_Object = MibTableColumn
accDialOrigDnSourceAddr = _AccDialOrigDnSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5, 1, 3),
    _AccDialOrigDnSourceAddr_Type()
)
accDialOrigDnSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigDnSourceAddr.setStatus("mandatory")


class _AccDialOrigDnAction_Type(Integer32):
    """Custom type accDialOrigDnAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigDnAction_Type.__name__ = "Integer32"
_AccDialOrigDnAction_Object = MibTableColumn
accDialOrigDnAction = _AccDialOrigDnAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5, 1, 4),
    _AccDialOrigDnAction_Type()
)
accDialOrigDnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigDnAction.setStatus("mandatory")
_AccDialOrigBrTable_Object = MibTable
accDialOrigBrTable = _AccDialOrigBrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6)
)
if mibBuilder.loadTexts:
    accDialOrigBrTable.setStatus("mandatory")
_AccDialOrigBrEntry_Object = MibTableRow
accDialOrigBrEntry = _AccDialOrigBrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6, 1)
)
accDialOrigBrEntry.setIndexNames(
    (0, "ACC-PPP", "accDialOrigBrDestMacAddr"),
    (0, "ACC-PPP", "accDialOrigBrSourceMacAddr"),
)
if mibBuilder.loadTexts:
    accDialOrigBrEntry.setStatus("mandatory")


class _AccDialOrigBrStatus_Type(Integer32):
    """Custom type accDialOrigBrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigBrStatus_Type.__name__ = "Integer32"
_AccDialOrigBrStatus_Object = MibTableColumn
accDialOrigBrStatus = _AccDialOrigBrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6, 1, 1),
    _AccDialOrigBrStatus_Type()
)
accDialOrigBrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigBrStatus.setStatus("mandatory")
_AccDialOrigBrDestMacAddr_Type = OctetString
_AccDialOrigBrDestMacAddr_Object = MibTableColumn
accDialOrigBrDestMacAddr = _AccDialOrigBrDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6, 1, 2),
    _AccDialOrigBrDestMacAddr_Type()
)
accDialOrigBrDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigBrDestMacAddr.setStatus("mandatory")
_AccDialOrigBrSourceMacAddr_Type = OctetString
_AccDialOrigBrSourceMacAddr_Object = MibTableColumn
accDialOrigBrSourceMacAddr = _AccDialOrigBrSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6, 1, 3),
    _AccDialOrigBrSourceMacAddr_Type()
)
accDialOrigBrSourceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigBrSourceMacAddr.setStatus("mandatory")


class _AccDialOrigBrAction_Type(Integer32):
    """Custom type accDialOrigBrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigBrAction_Type.__name__ = "Integer32"
_AccDialOrigBrAction_Object = MibTableColumn
accDialOrigBrAction = _AccDialOrigBrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6, 1, 4),
    _AccDialOrigBrAction_Type()
)
accDialOrigBrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigBrAction.setStatus("mandatory")
_AccDialOrigIdpTable_Object = MibTable
accDialOrigIdpTable = _AccDialOrigIdpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7)
)
if mibBuilder.loadTexts:
    accDialOrigIdpTable.setStatus("mandatory")
_AccDialOrigIdpEntry_Object = MibTableRow
accDialOrigIdpEntry = _AccDialOrigIdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7, 1)
)
accDialOrigIdpEntry.setIndexNames(
    (0, "ACC-PPP", "accDialOrigIdpDestNet"),
    (0, "ACC-PPP", "accDialOrigIdpSourceNet"),
)
if mibBuilder.loadTexts:
    accDialOrigIdpEntry.setStatus("mandatory")


class _AccDialOrigIdpStatus_Type(Integer32):
    """Custom type accDialOrigIdpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigIdpStatus_Type.__name__ = "Integer32"
_AccDialOrigIdpStatus_Object = MibTableColumn
accDialOrigIdpStatus = _AccDialOrigIdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7, 1, 1),
    _AccDialOrigIdpStatus_Type()
)
accDialOrigIdpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIdpStatus.setStatus("mandatory")
_AccDialOrigIdpDestNet_Type = OctetString
_AccDialOrigIdpDestNet_Object = MibTableColumn
accDialOrigIdpDestNet = _AccDialOrigIdpDestNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7, 1, 2),
    _AccDialOrigIdpDestNet_Type()
)
accDialOrigIdpDestNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIdpDestNet.setStatus("mandatory")
_AccDialOrigIdpSourceNet_Type = OctetString
_AccDialOrigIdpSourceNet_Object = MibTableColumn
accDialOrigIdpSourceNet = _AccDialOrigIdpSourceNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7, 1, 3),
    _AccDialOrigIdpSourceNet_Type()
)
accDialOrigIdpSourceNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIdpSourceNet.setStatus("mandatory")


class _AccDialOrigIdpAction_Type(Integer32):
    """Custom type accDialOrigIdpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigIdpAction_Type.__name__ = "Integer32"
_AccDialOrigIdpAction_Object = MibTableColumn
accDialOrigIdpAction = _AccDialOrigIdpAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7, 1, 4),
    _AccDialOrigIdpAction_Type()
)
accDialOrigIdpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIdpAction.setStatus("mandatory")
_AccDialOrigIpTable_Object = MibTable
accDialOrigIpTable = _AccDialOrigIpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8)
)
if mibBuilder.loadTexts:
    accDialOrigIpTable.setStatus("mandatory")
_AccDialOrigIpEntry_Object = MibTableRow
accDialOrigIpEntry = _AccDialOrigIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1)
)
accDialOrigIpEntry.setIndexNames(
    (0, "ACC-PPP", "accDialOrigIpDestAddr"),
    (0, "ACC-PPP", "accDialOrigIpDestMask"),
    (0, "ACC-PPP", "accDialOrigIpSourceAddr"),
    (0, "ACC-PPP", "accDialOrigIpSourceMask"),
    (0, "ACC-PPP", "accDialOrigIpParm"),
)
if mibBuilder.loadTexts:
    accDialOrigIpEntry.setStatus("mandatory")


class _AccDialOrigIpStatus_Type(Integer32):
    """Custom type accDialOrigIpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigIpStatus_Type.__name__ = "Integer32"
_AccDialOrigIpStatus_Object = MibTableColumn
accDialOrigIpStatus = _AccDialOrigIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 1),
    _AccDialOrigIpStatus_Type()
)
accDialOrigIpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpStatus.setStatus("mandatory")
_AccDialOrigIpDestAddr_Type = IpAddress
_AccDialOrigIpDestAddr_Object = MibTableColumn
accDialOrigIpDestAddr = _AccDialOrigIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 2),
    _AccDialOrigIpDestAddr_Type()
)
accDialOrigIpDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpDestAddr.setStatus("mandatory")
_AccDialOrigIpDestMask_Type = IpAddress
_AccDialOrigIpDestMask_Object = MibTableColumn
accDialOrigIpDestMask = _AccDialOrigIpDestMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 3),
    _AccDialOrigIpDestMask_Type()
)
accDialOrigIpDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpDestMask.setStatus("mandatory")
_AccDialOrigIpSourceAddr_Type = IpAddress
_AccDialOrigIpSourceAddr_Object = MibTableColumn
accDialOrigIpSourceAddr = _AccDialOrigIpSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 4),
    _AccDialOrigIpSourceAddr_Type()
)
accDialOrigIpSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpSourceAddr.setStatus("mandatory")
_AccDialOrigIpSourceMask_Type = IpAddress
_AccDialOrigIpSourceMask_Object = MibTableColumn
accDialOrigIpSourceMask = _AccDialOrigIpSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 5),
    _AccDialOrigIpSourceMask_Type()
)
accDialOrigIpSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpSourceMask.setStatus("mandatory")
_AccDialOrigIpParm_Type = OctetString
_AccDialOrigIpParm_Object = MibTableColumn
accDialOrigIpParm = _AccDialOrigIpParm_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 6),
    _AccDialOrigIpParm_Type()
)
accDialOrigIpParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpParm.setStatus("mandatory")


class _AccDialOrigIpAction_Type(Integer32):
    """Custom type accDialOrigIpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigIpAction_Type.__name__ = "Integer32"
_AccDialOrigIpAction_Object = MibTableColumn
accDialOrigIpAction = _AccDialOrigIpAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 7),
    _AccDialOrigIpAction_Type()
)
accDialOrigIpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpAction.setStatus("mandatory")
_AccDialOrigIpxTable_Object = MibTable
accDialOrigIpxTable = _AccDialOrigIpxTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9)
)
if mibBuilder.loadTexts:
    accDialOrigIpxTable.setStatus("mandatory")
_AccDialOrigIpxEntry_Object = MibTableRow
accDialOrigIpxEntry = _AccDialOrigIpxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9, 1)
)
accDialOrigIpxEntry.setIndexNames(
    (0, "ACC-PPP", "accDialOrigIpxDestNet"),
    (0, "ACC-PPP", "accDialOrigIpxSourceNet"),
)
if mibBuilder.loadTexts:
    accDialOrigIpxEntry.setStatus("mandatory")


class _AccDialOrigIpxStatus_Type(Integer32):
    """Custom type accDialOrigIpxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigIpxStatus_Type.__name__ = "Integer32"
_AccDialOrigIpxStatus_Object = MibTableColumn
accDialOrigIpxStatus = _AccDialOrigIpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9, 1, 1),
    _AccDialOrigIpxStatus_Type()
)
accDialOrigIpxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpxStatus.setStatus("mandatory")
_AccDialOrigIpxDestNet_Type = OctetString
_AccDialOrigIpxDestNet_Object = MibTableColumn
accDialOrigIpxDestNet = _AccDialOrigIpxDestNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9, 1, 2),
    _AccDialOrigIpxDestNet_Type()
)
accDialOrigIpxDestNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpxDestNet.setStatus("mandatory")
_AccDialOrigIpxSourceNet_Type = OctetString
_AccDialOrigIpxSourceNet_Object = MibTableColumn
accDialOrigIpxSourceNet = _AccDialOrigIpxSourceNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9, 1, 3),
    _AccDialOrigIpxSourceNet_Type()
)
accDialOrigIpxSourceNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpxSourceNet.setStatus("mandatory")


class _AccDialOrigIpxAction_Type(Integer32):
    """Custom type accDialOrigIpxAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigIpxAction_Type.__name__ = "Integer32"
_AccDialOrigIpxAction_Object = MibTableColumn
accDialOrigIpxAction = _AccDialOrigIpxAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9, 1, 4),
    _AccDialOrigIpxAction_Type()
)
accDialOrigIpxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpxAction.setStatus("mandatory")
_AccDialOrigSrTable_Object = MibTable
accDialOrigSrTable = _AccDialOrigSrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10)
)
if mibBuilder.loadTexts:
    accDialOrigSrTable.setStatus("mandatory")
_AccDialOrigSrEntry_Object = MibTableRow
accDialOrigSrEntry = _AccDialOrigSrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10, 1)
)
accDialOrigSrEntry.setIndexNames(
    (0, "ACC-PPP", "accDialOrigSrDestMacAddr"),
    (0, "ACC-PPP", "accDialOrigSrSourceMacAddr"),
)
if mibBuilder.loadTexts:
    accDialOrigSrEntry.setStatus("mandatory")


class _AccDialOrigSrStatus_Type(Integer32):
    """Custom type accDialOrigSrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigSrStatus_Type.__name__ = "Integer32"
_AccDialOrigSrStatus_Object = MibTableColumn
accDialOrigSrStatus = _AccDialOrigSrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10, 1, 1),
    _AccDialOrigSrStatus_Type()
)
accDialOrigSrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigSrStatus.setStatus("mandatory")
_AccDialOrigSrDestMacAddr_Type = OctetString
_AccDialOrigSrDestMacAddr_Object = MibTableColumn
accDialOrigSrDestMacAddr = _AccDialOrigSrDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10, 1, 2),
    _AccDialOrigSrDestMacAddr_Type()
)
accDialOrigSrDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigSrDestMacAddr.setStatus("mandatory")
_AccDialOrigSrSourceMacAddr_Type = OctetString
_AccDialOrigSrSourceMacAddr_Object = MibTableColumn
accDialOrigSrSourceMacAddr = _AccDialOrigSrSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10, 1, 3),
    _AccDialOrigSrSourceMacAddr_Type()
)
accDialOrigSrSourceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigSrSourceMacAddr.setStatus("mandatory")


class _AccDialOrigSrAction_Type(Integer32):
    """Custom type accDialOrigSrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigSrAction_Type.__name__ = "Integer32"
_AccDialOrigSrAction_Object = MibTableColumn
accDialOrigSrAction = _AccDialOrigSrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10, 1, 4),
    _AccDialOrigSrAction_Type()
)
accDialOrigSrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigSrAction.setStatus("mandatory")
_AccDialPortRange_ObjectIdentity = ObjectIdentity
accDialPortRange = _AccDialPortRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 11)
)


class _AccDialPortMaxCount_Type(Integer32):
    """Custom type accDialPortMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AccDialPortMaxCount_Type.__name__ = "Integer32"
_AccDialPortMaxCount_Object = MibScalar
accDialPortMaxCount = _AccDialPortMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 11, 1),
    _AccDialPortMaxCount_Type()
)
accDialPortMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortMaxCount.setStatus("mandatory")
_AccDialPortRangeStart_Type = Integer32
_AccDialPortRangeStart_Object = MibScalar
accDialPortRangeStart = _AccDialPortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 11, 2),
    _AccDialPortRangeStart_Type()
)
accDialPortRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortRangeStart.setStatus("mandatory")
_AccDialPortRangeEnd_Type = Integer32
_AccDialPortRangeEnd_Object = MibScalar
accDialPortRangeEnd = _AccDialPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 11, 3),
    _AccDialPortRangeEnd_Type()
)
accDialPortRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortRangeEnd.setStatus("mandatory")
_AccDialPortConnTable_Object = MibTable
accDialPortConnTable = _AccDialPortConnTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12)
)
if mibBuilder.loadTexts:
    accDialPortConnTable.setStatus("mandatory")
_AccDialPortConnEntry_Object = MibTableRow
accDialPortConnEntry = _AccDialPortConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1)
)
accDialPortConnEntry.setIndexNames(
    (0, "ACC-PPP", "accDialPortConnIndex"),
)
if mibBuilder.loadTexts:
    accDialPortConnEntry.setStatus("mandatory")
_AccDialPortConnIndex_Type = Integer32
_AccDialPortConnIndex_Object = MibTableColumn
accDialPortConnIndex = _AccDialPortConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 1),
    _AccDialPortConnIndex_Type()
)
accDialPortConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortConnIndex.setStatus("mandatory")
_AccDialPortConnUser_Type = OctetString
_AccDialPortConnUser_Object = MibTableColumn
accDialPortConnUser = _AccDialPortConnUser_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 2),
    _AccDialPortConnUser_Type()
)
accDialPortConnUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortConnUser.setStatus("mandatory")
_AccDialPortConnPhyPort_Type = Integer32
_AccDialPortConnPhyPort_Object = MibTableColumn
accDialPortConnPhyPort = _AccDialPortConnPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 3),
    _AccDialPortConnPhyPort_Type()
)
accDialPortConnPhyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortConnPhyPort.setStatus("mandatory")
_AccDialPortConnLogPort_Type = Integer32
_AccDialPortConnLogPort_Object = MibTableColumn
accDialPortConnLogPort = _AccDialPortConnLogPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 4),
    _AccDialPortConnLogPort_Type()
)
accDialPortConnLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortConnLogPort.setStatus("mandatory")


class _AccDialPortConnDir_Type(Integer32):
    """Custom type accDialPortConnDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_AccDialPortConnDir_Type.__name__ = "Integer32"
_AccDialPortConnDir_Object = MibTableColumn
accDialPortConnDir = _AccDialPortConnDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 5),
    _AccDialPortConnDir_Type()
)
accDialPortConnDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortConnDir.setStatus("mandatory")
_AccDialPortConnAuth_Type = IpAddress
_AccDialPortConnAuth_Object = MibTableColumn
accDialPortConnAuth = _AccDialPortConnAuth_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 6),
    _AccDialPortConnAuth_Type()
)
accDialPortConnAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortConnAuth.setStatus("mandatory")
_AccDialPortConnStart_Type = TimeTicks
_AccDialPortConnStart_Object = MibTableColumn
accDialPortConnStart = _AccDialPortConnStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 7),
    _AccDialPortConnStart_Type()
)
accDialPortConnStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortConnStart.setStatus("mandatory")
_AccDialPortConnProf_Type = OctetString
_AccDialPortConnProf_Object = MibTableColumn
accDialPortConnProf = _AccDialPortConnProf_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 8),
    _AccDialPortConnProf_Type()
)
accDialPortConnProf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortConnProf.setStatus("mandatory")
_AccDialPortConnStack_Type = OctetString
_AccDialPortConnStack_Object = MibTableColumn
accDialPortConnStack = _AccDialPortConnStack_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 9),
    _AccDialPortConnStack_Type()
)
accDialPortConnStack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortConnStack.setStatus("mandatory")
_AccDialPortConnAddr_Type = IpAddress
_AccDialPortConnAddr_Object = MibTableColumn
accDialPortConnAddr = _AccDialPortConnAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 10),
    _AccDialPortConnAddr_Type()
)
accDialPortConnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortConnAddr.setStatus("mandatory")


class _AccDialPortConnState_Type(Integer32):
    """Custom type accDialPortConnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disconnect", 1)
    )


_AccDialPortConnState_Type.__name__ = "Integer32"
_AccDialPortConnState_Object = MibTableColumn
accDialPortConnState = _AccDialPortConnState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 12, 1, 11),
    _AccDialPortConnState_Type()
)
accDialPortConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortConnState.setStatus("mandatory")
_AccDialPortCompressTable_Object = MibTable
accDialPortCompressTable = _AccDialPortCompressTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 13)
)
if mibBuilder.loadTexts:
    accDialPortCompressTable.setStatus("mandatory")
_AccDialPortCompressEntry_Object = MibTableRow
accDialPortCompressEntry = _AccDialPortCompressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 13, 1)
)
accDialPortCompressEntry.setIndexNames(
    (0, "ACC-PPP", "accDialPortCompressIndex"),
)
if mibBuilder.loadTexts:
    accDialPortCompressEntry.setStatus("mandatory")
_AccDialPortCompressIndex_Type = Integer32
_AccDialPortCompressIndex_Object = MibTableColumn
accDialPortCompressIndex = _AccDialPortCompressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 13, 1, 1),
    _AccDialPortCompressIndex_Type()
)
accDialPortCompressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortCompressIndex.setStatus("mandatory")
_AccDialPortCompressMsgLevel_Type = Integer32
_AccDialPortCompressMsgLevel_Object = MibTableColumn
accDialPortCompressMsgLevel = _AccDialPortCompressMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 13, 1, 2),
    _AccDialPortCompressMsgLevel_Type()
)
accDialPortCompressMsgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortCompressMsgLevel.setStatus("mandatory")


class _AccDialPortCompressMethod_Type(Integer32):
    """Custom type accDialPortCompressMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("mppc", 7),
          ("nego", 2),
          ("none", 1),
          ("stac-extd", 5),
          ("stac-none", 6),
          ("stac-seqn", 4),
          ("vendor", 3))
    )


_AccDialPortCompressMethod_Type.__name__ = "Integer32"
_AccDialPortCompressMethod_Object = MibTableColumn
accDialPortCompressMethod = _AccDialPortCompressMethod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 13, 1, 3),
    _AccDialPortCompressMethod_Type()
)
accDialPortCompressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortCompressMethod.setStatus("mandatory")


class _AccDialPortCompressStream_Type(Integer32):
    """Custom type accDialPortCompressStream based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("stream", 2))
    )


_AccDialPortCompressStream_Type.__name__ = "Integer32"
_AccDialPortCompressStream_Object = MibTableColumn
accDialPortCompressStream = _AccDialPortCompressStream_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 13, 1, 4),
    _AccDialPortCompressStream_Type()
)
accDialPortCompressStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortCompressStream.setStatus("mandatory")


class _AccDialPortCompressNegoMethodIn_Type(Integer32):
    """Custom type accDialPortCompressNegoMethodIn based on Integer32"""
    defaultValue = 1

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
        *(("mppc", 6),
          ("none", 1),
          ("stac-extd", 4),
          ("stac-none", 5),
          ("stac-seqn", 3),
          ("vendor", 2))
    )


_AccDialPortCompressNegoMethodIn_Type.__name__ = "Integer32"
_AccDialPortCompressNegoMethodIn_Object = MibTableColumn
accDialPortCompressNegoMethodIn = _AccDialPortCompressNegoMethodIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 13, 1, 5),
    _AccDialPortCompressNegoMethodIn_Type()
)
accDialPortCompressNegoMethodIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortCompressNegoMethodIn.setStatus("mandatory")


class _AccDialPortCompressNegoMethodOut_Type(Integer32):
    """Custom type accDialPortCompressNegoMethodOut based on Integer32"""
    defaultValue = 1

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
        *(("mppc", 6),
          ("none", 1),
          ("stac-extd", 4),
          ("stac-none", 5),
          ("stac-seqn", 3),
          ("vendor", 2))
    )


_AccDialPortCompressNegoMethodOut_Type.__name__ = "Integer32"
_AccDialPortCompressNegoMethodOut_Object = MibTableColumn
accDialPortCompressNegoMethodOut = _AccDialPortCompressNegoMethodOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 13, 1, 6),
    _AccDialPortCompressNegoMethodOut_Type()
)
accDialPortCompressNegoMethodOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortCompressNegoMethodOut.setStatus("mandatory")


class _AccDialPortCompressNegoStreamIn_Type(Integer32):
    """Custom type accDialPortCompressNegoStreamIn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("stream", 2))
    )


_AccDialPortCompressNegoStreamIn_Type.__name__ = "Integer32"
_AccDialPortCompressNegoStreamIn_Object = MibTableColumn
accDialPortCompressNegoStreamIn = _AccDialPortCompressNegoStreamIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 13, 1, 7),
    _AccDialPortCompressNegoStreamIn_Type()
)
accDialPortCompressNegoStreamIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortCompressNegoStreamIn.setStatus("mandatory")


class _AccDialPortCompressNegoStreamOut_Type(Integer32):
    """Custom type accDialPortCompressNegoStreamOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("stream", 2))
    )


_AccDialPortCompressNegoStreamOut_Type.__name__ = "Integer32"
_AccDialPortCompressNegoStreamOut_Object = MibTableColumn
accDialPortCompressNegoStreamOut = _AccDialPortCompressNegoStreamOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 13, 1, 8),
    _AccDialPortCompressNegoStreamOut_Type()
)
accDialPortCompressNegoStreamOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortCompressNegoStreamOut.setStatus("mandatory")
_AccAccessParameter_ObjectIdentity = ObjectIdentity
accAccessParameter = _AccAccessParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 14)
)


class _AccAccessTimer_Type(Integer32):
    """Custom type accAccessTimer based on Integer32"""
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


_AccAccessTimer_Type.__name__ = "Integer32"
_AccAccessTimer_Object = MibScalar
accAccessTimer = _AccAccessTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 14, 1),
    _AccAccessTimer_Type()
)
accAccessTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessTimer.setStatus("mandatory")
_AccAccessCreditDay_Type = Integer32
_AccAccessCreditDay_Object = MibScalar
accAccessCreditDay = _AccAccessCreditDay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 14, 2),
    _AccAccessCreditDay_Type()
)
accAccessCreditDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessCreditDay.setStatus("mandatory")
_AccAccessCreditYear_Type = Integer32
_AccAccessCreditYear_Object = MibScalar
accAccessCreditYear = _AccAccessCreditYear_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 14, 3),
    _AccAccessCreditYear_Type()
)
accAccessCreditYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessCreditYear.setStatus("mandatory")
_AccAccessTime_Type = OctetString
_AccAccessTime_Object = MibScalar
accAccessTime = _AccAccessTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 14, 4),
    _AccAccessTime_Type()
)
accAccessTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessTime.setStatus("mandatory")
_AccAccessLimitDate_Type = OctetString
_AccAccessLimitDate_Object = MibScalar
accAccessLimitDate = _AccAccessLimitDate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 14, 5),
    _AccAccessLimitDate_Type()
)
accAccessLimitDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessLimitDate.setStatus("mandatory")
_AccAccessDay_Type = OctetString
_AccAccessDay_Object = MibScalar
accAccessDay = _AccAccessDay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 14, 6),
    _AccAccessDay_Type()
)
accAccessDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessDay.setStatus("mandatory")
_AccAccessDayCreditLeft_Type = Integer32
_AccAccessDayCreditLeft_Object = MibScalar
accAccessDayCreditLeft = _AccAccessDayCreditLeft_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 14, 7),
    _AccAccessDayCreditLeft_Type()
)
accAccessDayCreditLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessDayCreditLeft.setStatus("mandatory")
_AccAccessYearCreditLeft_Type = Integer32
_AccAccessYearCreditLeft_Object = MibScalar
accAccessYearCreditLeft = _AccAccessYearCreditLeft_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 14, 8),
    _AccAccessYearCreditLeft_Type()
)
accAccessYearCreditLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAccessYearCreditLeft.setStatus("mandatory")
_AccDodTraps_ObjectIdentity = ObjectIdentity
accDodTraps = _AccDodTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15)
)
_AccDodTrapMsg_Type = DisplayString
_AccDodTrapMsg_Object = MibScalar
accDodTrapMsg = _AccDodTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 1),
    _AccDodTrapMsg_Type()
)
accDodTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDodTrapMsg.setStatus("mandatory")
_AccPpp_ObjectIdentity = ObjectIdentity
accPpp = _AccPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32)
)
_AccPppLinkTable_Object = MibTable
accPppLinkTable = _AccPppLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1)
)
if mibBuilder.loadTexts:
    accPppLinkTable.setStatus("mandatory")
_AccPppLinkEntry_Object = MibTableRow
accPppLinkEntry = _AccPppLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1)
)
accPppLinkEntry.setIndexNames(
    (0, "ACC-PPP", "accPppLinkIndex"),
)
if mibBuilder.loadTexts:
    accPppLinkEntry.setStatus("mandatory")
_AccPppLinkIndex_Type = Integer32
_AccPppLinkIndex_Object = MibTableColumn
accPppLinkIndex = _AccPppLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 1),
    _AccPppLinkIndex_Type()
)
accPppLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkIndex.setStatus("mandatory")
_AccPppLinkPhysicalIndex_Type = Integer32
_AccPppLinkPhysicalIndex_Object = MibTableColumn
accPppLinkPhysicalIndex = _AccPppLinkPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 2),
    _AccPppLinkPhysicalIndex_Type()
)
accPppLinkPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPhysicalIndex.setStatus("mandatory")
_AccPppLinkBadAddresses_Type = Counter32
_AccPppLinkBadAddresses_Object = MibTableColumn
accPppLinkBadAddresses = _AccPppLinkBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 3),
    _AccPppLinkBadAddresses_Type()
)
accPppLinkBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkBadAddresses.setStatus("mandatory")
_AccPppLinkBadControls_Type = Counter32
_AccPppLinkBadControls_Object = MibTableColumn
accPppLinkBadControls = _AccPppLinkBadControls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 4),
    _AccPppLinkBadControls_Type()
)
accPppLinkBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkBadControls.setStatus("mandatory")
_AccPppLinkPacketTooLongs_Type = Counter32
_AccPppLinkPacketTooLongs_Object = MibTableColumn
accPppLinkPacketTooLongs = _AccPppLinkPacketTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 5),
    _AccPppLinkPacketTooLongs_Type()
)
accPppLinkPacketTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPacketTooLongs.setStatus("mandatory")
_AccPppLinkBadFCSs_Type = Counter32
_AccPppLinkBadFCSs_Object = MibTableColumn
accPppLinkBadFCSs = _AccPppLinkBadFCSs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 6),
    _AccPppLinkBadFCSs_Type()
)
accPppLinkBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkBadFCSs.setStatus("mandatory")
_AccPppLinkLocalMRU_Type = Integer32
_AccPppLinkLocalMRU_Object = MibTableColumn
accPppLinkLocalMRU = _AccPppLinkLocalMRU_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 7),
    _AccPppLinkLocalMRU_Type()
)
accPppLinkLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkLocalMRU.setStatus("mandatory")
_AccPppLinkRemoteMRU_Type = Integer32
_AccPppLinkRemoteMRU_Object = MibTableColumn
accPppLinkRemoteMRU = _AccPppLinkRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 8),
    _AccPppLinkRemoteMRU_Type()
)
accPppLinkRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkRemoteMRU.setStatus("mandatory")
_AccPppLinkLocalToPeerACCMap_Type = OctetString
_AccPppLinkLocalToPeerACCMap_Object = MibTableColumn
accPppLinkLocalToPeerACCMap = _AccPppLinkLocalToPeerACCMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 9),
    _AccPppLinkLocalToPeerACCMap_Type()
)
accPppLinkLocalToPeerACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkLocalToPeerACCMap.setStatus("mandatory")
_AccPppLinkPeerToLocalACCMap_Type = OctetString
_AccPppLinkPeerToLocalACCMap_Object = MibTableColumn
accPppLinkPeerToLocalACCMap = _AccPppLinkPeerToLocalACCMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 10),
    _AccPppLinkPeerToLocalACCMap_Type()
)
accPppLinkPeerToLocalACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPeerToLocalACCMap.setStatus("mandatory")
_AccPppLinkLocalToRemotePC_Type = Integer32
_AccPppLinkLocalToRemotePC_Object = MibTableColumn
accPppLinkLocalToRemotePC = _AccPppLinkLocalToRemotePC_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 11),
    _AccPppLinkLocalToRemotePC_Type()
)
accPppLinkLocalToRemotePC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkLocalToRemotePC.setStatus("mandatory")
_AccPppLinkRemoteToLocalPC_Type = Integer32
_AccPppLinkRemoteToLocalPC_Object = MibTableColumn
accPppLinkRemoteToLocalPC = _AccPppLinkRemoteToLocalPC_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 12),
    _AccPppLinkRemoteToLocalPC_Type()
)
accPppLinkRemoteToLocalPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkRemoteToLocalPC.setStatus("mandatory")
_AccPppLinkLocalToRemoteAC_Type = Integer32
_AccPppLinkLocalToRemoteAC_Object = MibTableColumn
accPppLinkLocalToRemoteAC = _AccPppLinkLocalToRemoteAC_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 13),
    _AccPppLinkLocalToRemoteAC_Type()
)
accPppLinkLocalToRemoteAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkLocalToRemoteAC.setStatus("mandatory")
_AccPppLinkRemoteToLocalAC_Type = Integer32
_AccPppLinkRemoteToLocalAC_Object = MibTableColumn
accPppLinkRemoteToLocalAC = _AccPppLinkRemoteToLocalAC_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 14),
    _AccPppLinkRemoteToLocalAC_Type()
)
accPppLinkRemoteToLocalAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkRemoteToLocalAC.setStatus("mandatory")
_AccPppLinkTransmit32BitFcs_Type = Integer32
_AccPppLinkTransmit32BitFcs_Object = MibTableColumn
accPppLinkTransmit32BitFcs = _AccPppLinkTransmit32BitFcs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 15),
    _AccPppLinkTransmit32BitFcs_Type()
)
accPppLinkTransmit32BitFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkTransmit32BitFcs.setStatus("mandatory")
_AccPppLinkReceive32BitFcs_Type = Integer32
_AccPppLinkReceive32BitFcs_Object = MibTableColumn
accPppLinkReceive32BitFcs = _AccPppLinkReceive32BitFcs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 16),
    _AccPppLinkReceive32BitFcs_Type()
)
accPppLinkReceive32BitFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkReceive32BitFcs.setStatus("mandatory")


class _AccPppLinkOperStatus_Type(Integer32):
    """Custom type accPppLinkOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppLinkOperStatus_Type.__name__ = "Integer32"
_AccPppLinkOperStatus_Object = MibTableColumn
accPppLinkOperStatus = _AccPppLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 17),
    _AccPppLinkOperStatus_Type()
)
accPppLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkOperStatus.setStatus("mandatory")
_AccPppLinkPacketTooShorts_Type = Counter32
_AccPppLinkPacketTooShorts_Object = MibTableColumn
accPppLinkPacketTooShorts = _AccPppLinkPacketTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 18),
    _AccPppLinkPacketTooShorts_Type()
)
accPppLinkPacketTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPacketTooShorts.setStatus("mandatory")
_AccPppLinkUnknownProtocols_Type = Counter32
_AccPppLinkUnknownProtocols_Object = MibTableColumn
accPppLinkUnknownProtocols = _AccPppLinkUnknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 19),
    _AccPppLinkUnknownProtocols_Type()
)
accPppLinkUnknownProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkUnknownProtocols.setStatus("mandatory")
_AccPppLinkPacketInDiscards_Type = Counter32
_AccPppLinkPacketInDiscards_Object = MibTableColumn
accPppLinkPacketInDiscards = _AccPppLinkPacketInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 20),
    _AccPppLinkPacketInDiscards_Type()
)
accPppLinkPacketInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPacketInDiscards.setStatus("mandatory")
_AccPppLinkPacketOutDiscards_Type = Counter32
_AccPppLinkPacketOutDiscards_Object = MibTableColumn
accPppLinkPacketOutDiscards = _AccPppLinkPacketOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 21),
    _AccPppLinkPacketOutDiscards_Type()
)
accPppLinkPacketOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPacketOutDiscards.setStatus("mandatory")
_AccPppLcpConfigTable_Object = MibTable
accPppLcpConfigTable = _AccPppLcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2)
)
if mibBuilder.loadTexts:
    accPppLcpConfigTable.setStatus("mandatory")
_AccPppLcpConfigEntry_Object = MibTableRow
accPppLcpConfigEntry = _AccPppLcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1)
)
accPppLcpConfigEntry.setIndexNames(
    (0, "ACC-PPP", "accPppLcpConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppLcpConfigEntry.setStatus("mandatory")
_AccPppLcpConfigIndex_Type = Integer32
_AccPppLcpConfigIndex_Object = MibTableColumn
accPppLcpConfigIndex = _AccPppLcpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 1),
    _AccPppLcpConfigIndex_Type()
)
accPppLcpConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLcpConfigIndex.setStatus("mandatory")


class _AccPppLcpConfigInitialMRU_Type(Integer32):
    """Custom type accPppLcpConfigInitialMRU based on Integer32"""
    defaultValue = 1500


_AccPppLcpConfigInitialMRU_Object = MibTableColumn
accPppLcpConfigInitialMRU = _AccPppLcpConfigInitialMRU_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 2),
    _AccPppLcpConfigInitialMRU_Type()
)
accPppLcpConfigInitialMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLcpConfigInitialMRU.setStatus("mandatory")
_AccPppLcpConfigReceiveACCMap_Type = OctetString
_AccPppLcpConfigReceiveACCMap_Object = MibTableColumn
accPppLcpConfigReceiveACCMap = _AccPppLcpConfigReceiveACCMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 3),
    _AccPppLcpConfigReceiveACCMap_Type()
)
accPppLcpConfigReceiveACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLcpConfigReceiveACCMap.setStatus("mandatory")
_AccPppLinkConfigXmitACCMap_Type = OctetString
_AccPppLinkConfigXmitACCMap_Object = MibTableColumn
accPppLinkConfigXmitACCMap = _AccPppLinkConfigXmitACCMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 4),
    _AccPppLinkConfigXmitACCMap_Type()
)
accPppLinkConfigXmitACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkConfigXmitACCMap.setStatus("mandatory")


class _AccPppLcpConfigMagicNumber_Type(Integer32):
    """Custom type accPppLcpConfigMagicNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AccPppLcpConfigMagicNumber_Type.__name__ = "Integer32"
_AccPppLcpConfigMagicNumber_Object = MibTableColumn
accPppLcpConfigMagicNumber = _AccPppLcpConfigMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 5),
    _AccPppLcpConfigMagicNumber_Type()
)
accPppLcpConfigMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLcpConfigMagicNumber.setStatus("mandatory")
_AccPppLcpConfig32BitFCS_Type = Integer32
_AccPppLcpConfig32BitFCS_Object = MibTableColumn
accPppLcpConfig32BitFCS = _AccPppLcpConfig32BitFCS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 6),
    _AccPppLcpConfig32BitFCS_Type()
)
accPppLcpConfig32BitFCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLcpConfig32BitFCS.setStatus("mandatory")


class _AccPppLcpRestartTimer_Type(Integer32):
    """Custom type accPppLcpRestartTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AccPppLcpRestartTimer_Type.__name__ = "Integer32"
_AccPppLcpRestartTimer_Object = MibTableColumn
accPppLcpRestartTimer = _AccPppLcpRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 7),
    _AccPppLcpRestartTimer_Type()
)
accPppLcpRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpRestartTimer.setStatus("mandatory")


class _AccPppLcpMaxTerminate_Type(Integer32):
    """Custom type accPppLcpMaxTerminate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccPppLcpMaxTerminate_Type.__name__ = "Integer32"
_AccPppLcpMaxTerminate_Object = MibTableColumn
accPppLcpMaxTerminate = _AccPppLcpMaxTerminate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 8),
    _AccPppLcpMaxTerminate_Type()
)
accPppLcpMaxTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMaxTerminate.setStatus("mandatory")


class _AccPppLcpMaxConfigure_Type(Integer32):
    """Custom type accPppLcpMaxConfigure based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccPppLcpMaxConfigure_Type.__name__ = "Integer32"
_AccPppLcpMaxConfigure_Object = MibTableColumn
accPppLcpMaxConfigure = _AccPppLcpMaxConfigure_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 9),
    _AccPppLcpMaxConfigure_Type()
)
accPppLcpMaxConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMaxConfigure.setStatus("mandatory")


class _AccPppLcpMaxFailure_Type(Integer32):
    """Custom type accPppLcpMaxFailure based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccPppLcpMaxFailure_Type.__name__ = "Integer32"
_AccPppLcpMaxFailure_Object = MibTableColumn
accPppLcpMaxFailure = _AccPppLcpMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 10),
    _AccPppLcpMaxFailure_Type()
)
accPppLcpMaxFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMaxFailure.setStatus("mandatory")


class _AccPppLcpMonInterval_Type(Integer32):
    """Custom type accPppLcpMonInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccPppLcpMonInterval_Type.__name__ = "Integer32"
_AccPppLcpMonInterval_Object = MibTableColumn
accPppLcpMonInterval = _AccPppLcpMonInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 11),
    _AccPppLcpMonInterval_Type()
)
accPppLcpMonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMonInterval.setStatus("mandatory")


class _AccPppLcpMonEvents_Type(Integer32):
    """Custom type accPppLcpMonEvents based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AccPppLcpMonEvents_Type.__name__ = "Integer32"
_AccPppLcpMonEvents_Object = MibTableColumn
accPppLcpMonEvents = _AccPppLcpMonEvents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 12),
    _AccPppLcpMonEvents_Type()
)
accPppLcpMonEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMonEvents.setStatus("mandatory")


class _AccPppLcpMonThreshold_Type(Integer32):
    """Custom type accPppLcpMonThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AccPppLcpMonThreshold_Type.__name__ = "Integer32"
_AccPppLcpMonThreshold_Object = MibTableColumn
accPppLcpMonThreshold = _AccPppLcpMonThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 13),
    _AccPppLcpMonThreshold_Type()
)
accPppLcpMonThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMonThreshold.setStatus("mandatory")


class _AccPppLcpAdminStatus_Type(Integer32):
    """Custom type accPppLcpAdminStatus based on Integer32"""
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


_AccPppLcpAdminStatus_Type.__name__ = "Integer32"
_AccPppLcpAdminStatus_Object = MibTableColumn
accPppLcpAdminStatus = _AccPppLcpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 14),
    _AccPppLcpAdminStatus_Type()
)
accPppLcpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpAdminStatus.setStatus("mandatory")


class _AccPppLinkMsgLevel_Type(Integer32):
    """Custom type accPppLinkMsgLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccPppLinkMsgLevel_Type.__name__ = "Integer32"
_AccPppLinkMsgLevel_Object = MibTableColumn
accPppLinkMsgLevel = _AccPppLinkMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 15),
    _AccPppLinkMsgLevel_Type()
)
accPppLinkMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLinkMsgLevel.setStatus("mandatory")
_AccPppLqrTable_Object = MibTable
accPppLqrTable = _AccPppLqrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3)
)
if mibBuilder.loadTexts:
    accPppLqrTable.setStatus("mandatory")
_AccPppLqrEntry_Object = MibTableRow
accPppLqrEntry = _AccPppLqrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1)
)
accPppLqrEntry.setIndexNames(
    (0, "ACC-PPP", "accPppLqrIndex"),
)
if mibBuilder.loadTexts:
    accPppLqrEntry.setStatus("mandatory")
_AccPppLqrIndex_Type = Integer32
_AccPppLqrIndex_Object = MibTableColumn
accPppLqrIndex = _AccPppLqrIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 1),
    _AccPppLqrIndex_Type()
)
accPppLqrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrIndex.setStatus("mandatory")


class _AccPppLqrQuality_Type(Integer32):
    """Custom type accPppLqrQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_AccPppLqrQuality_Type.__name__ = "Integer32"
_AccPppLqrQuality_Object = MibTableColumn
accPppLqrQuality = _AccPppLqrQuality_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 2),
    _AccPppLqrQuality_Type()
)
accPppLqrQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrQuality.setStatus("mandatory")
_AccPppLqrInGoodOctets_Type = Counter32
_AccPppLqrInGoodOctets_Object = MibTableColumn
accPppLqrInGoodOctets = _AccPppLqrInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 3),
    _AccPppLqrInGoodOctets_Type()
)
accPppLqrInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrInGoodOctets.setStatus("mandatory")
_AccPppLqrLocalPeriod_Type = Integer32
_AccPppLqrLocalPeriod_Object = MibTableColumn
accPppLqrLocalPeriod = _AccPppLqrLocalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 4),
    _AccPppLqrLocalPeriod_Type()
)
accPppLqrLocalPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrLocalPeriod.setStatus("mandatory")
_AccPppLqrRemotePeriod_Type = Integer32
_AccPppLqrRemotePeriod_Object = MibTableColumn
accPppLqrRemotePeriod = _AccPppLqrRemotePeriod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 5),
    _AccPppLqrRemotePeriod_Type()
)
accPppLqrRemotePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrRemotePeriod.setStatus("mandatory")
_AccPppLqrOutLQRs_Type = Counter32
_AccPppLqrOutLQRs_Object = MibTableColumn
accPppLqrOutLQRs = _AccPppLqrOutLQRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 6),
    _AccPppLqrOutLQRs_Type()
)
accPppLqrOutLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrOutLQRs.setStatus("mandatory")
_AccPppLqrInLQRs_Type = Counter32
_AccPppLqrInLQRs_Object = MibTableColumn
accPppLqrInLQRs = _AccPppLqrInLQRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 7),
    _AccPppLqrInLQRs_Type()
)
accPppLqrInLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrInLQRs.setStatus("mandatory")
_AccPppLqrConfigTable_Object = MibTable
accPppLqrConfigTable = _AccPppLqrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 4)
)
if mibBuilder.loadTexts:
    accPppLqrConfigTable.setStatus("mandatory")
_AccPppLqrConfigEntry_Object = MibTableRow
accPppLqrConfigEntry = _AccPppLqrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 4, 1)
)
accPppLqrConfigEntry.setIndexNames(
    (0, "ACC-PPP", "accPppLqrConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppLqrConfigEntry.setStatus("mandatory")
_AccPppLqrConfigIndex_Type = Integer32
_AccPppLqrConfigIndex_Object = MibTableColumn
accPppLqrConfigIndex = _AccPppLqrConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 4, 1, 1),
    _AccPppLqrConfigIndex_Type()
)
accPppLqrConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrConfigIndex.setStatus("mandatory")


class _AccPppLqrConfigPeriod_Type(Integer32):
    """Custom type accPppLqrConfigPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483648),
    )


_AccPppLqrConfigPeriod_Type.__name__ = "Integer32"
_AccPppLqrConfigPeriod_Object = MibTableColumn
accPppLqrConfigPeriod = _AccPppLqrConfigPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 4, 1, 2),
    _AccPppLqrConfigPeriod_Type()
)
accPppLqrConfigPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLqrConfigPeriod.setStatus("mandatory")


class _AccPppLqrConfigStatus_Type(Integer32):
    """Custom type accPppLqrConfigStatus based on Integer32"""
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


_AccPppLqrConfigStatus_Type.__name__ = "Integer32"
_AccPppLqrConfigStatus_Object = MibTableColumn
accPppLqrConfigStatus = _AccPppLqrConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 4, 1, 3),
    _AccPppLqrConfigStatus_Type()
)
accPppLqrConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLqrConfigStatus.setStatus("mandatory")
_AccPppIpcpTable_Object = MibTable
accPppIpcpTable = _AccPppIpcpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5)
)
if mibBuilder.loadTexts:
    accPppIpcpTable.setStatus("mandatory")
_AccPppIpcpEntry_Object = MibTableRow
accPppIpcpEntry = _AccPppIpcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1)
)
accPppIpcpEntry.setIndexNames(
    (0, "ACC-PPP", "accPppIpcpIndex"),
)
if mibBuilder.loadTexts:
    accPppIpcpEntry.setStatus("mandatory")
_AccPppIpcpIndex_Type = Integer32
_AccPppIpcpIndex_Object = MibTableColumn
accPppIpcpIndex = _AccPppIpcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 1),
    _AccPppIpcpIndex_Type()
)
accPppIpcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpIndex.setStatus("mandatory")


class _AccPppIpcpLocalToRemoteCompressionProtocol_Type(Integer32):
    """Custom type accPppIpcpLocalToRemoteCompressionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_AccPppIpcpLocalToRemoteCompressionProtocol_Type.__name__ = "Integer32"
_AccPppIpcpLocalToRemoteCompressionProtocol_Object = MibTableColumn
accPppIpcpLocalToRemoteCompressionProtocol = _AccPppIpcpLocalToRemoteCompressionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 2),
    _AccPppIpcpLocalToRemoteCompressionProtocol_Type()
)
accPppIpcpLocalToRemoteCompressionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpLocalToRemoteCompressionProtocol.setStatus("mandatory")


class _AccPppIpcpRemoteToLocalCompressionProtocol_Type(Integer32):
    """Custom type accPppIpcpRemoteToLocalCompressionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_AccPppIpcpRemoteToLocalCompressionProtocol_Type.__name__ = "Integer32"
_AccPppIpcpRemoteToLocalCompressionProtocol_Object = MibTableColumn
accPppIpcpRemoteToLocalCompressionProtocol = _AccPppIpcpRemoteToLocalCompressionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 3),
    _AccPppIpcpRemoteToLocalCompressionProtocol_Type()
)
accPppIpcpRemoteToLocalCompressionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpRemoteToLocalCompressionProtocol.setStatus("mandatory")


class _AccPppIpcpRemoteMaxSlotId_Type(Integer32):
    """Custom type accPppIpcpRemoteMaxSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccPppIpcpRemoteMaxSlotId_Type.__name__ = "Integer32"
_AccPppIpcpRemoteMaxSlotId_Object = MibTableColumn
accPppIpcpRemoteMaxSlotId = _AccPppIpcpRemoteMaxSlotId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 4),
    _AccPppIpcpRemoteMaxSlotId_Type()
)
accPppIpcpRemoteMaxSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpRemoteMaxSlotId.setStatus("mandatory")


class _AccPppIpcpLocalMaxSlotId_Type(Integer32):
    """Custom type accPppIpcpLocalMaxSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccPppIpcpLocalMaxSlotId_Type.__name__ = "Integer32"
_AccPppIpcpLocalMaxSlotId_Object = MibTableColumn
accPppIpcpLocalMaxSlotId = _AccPppIpcpLocalMaxSlotId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 5),
    _AccPppIpcpLocalMaxSlotId_Type()
)
accPppIpcpLocalMaxSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpLocalMaxSlotId.setStatus("mandatory")


class _AccPppIpOperStatus_Type(Integer32):
    """Custom type accPppIpOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppIpOperStatus_Type.__name__ = "Integer32"
_AccPppIpOperStatus_Object = MibTableColumn
accPppIpOperStatus = _AccPppIpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 6),
    _AccPppIpOperStatus_Type()
)
accPppIpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpOperStatus.setStatus("mandatory")
_AccPppIpcpConfigTable_Object = MibTable
accPppIpcpConfigTable = _AccPppIpcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 6)
)
if mibBuilder.loadTexts:
    accPppIpcpConfigTable.setStatus("mandatory")
_AccPppIpcpConfigEntry_Object = MibTableRow
accPppIpcpConfigEntry = _AccPppIpcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 6, 1)
)
accPppIpcpConfigEntry.setIndexNames(
    (0, "ACC-PPP", "accPppIpcpConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppIpcpConfigEntry.setStatus("mandatory")
_AccPppIpcpConfigIndex_Type = Integer32
_AccPppIpcpConfigIndex_Object = MibTableColumn
accPppIpcpConfigIndex = _AccPppIpcpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 6, 1, 1),
    _AccPppIpcpConfigIndex_Type()
)
accPppIpcpConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpConfigIndex.setStatus("mandatory")


class _AccPppIpcpConfigCompression_Type(Integer32):
    """Custom type accPppIpcpConfigCompression based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_AccPppIpcpConfigCompression_Type.__name__ = "Integer32"
_AccPppIpcpConfigCompression_Object = MibTableColumn
accPppIpcpConfigCompression = _AccPppIpcpConfigCompression_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 6, 1, 2),
    _AccPppIpcpConfigCompression_Type()
)
accPppIpcpConfigCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppIpcpConfigCompression.setStatus("mandatory")


class _AccPppIpcpConfigStatus_Type(Integer32):
    """Custom type accPppIpcpConfigStatus based on Integer32"""
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


_AccPppIpcpConfigStatus_Type.__name__ = "Integer32"
_AccPppIpcpConfigStatus_Object = MibTableColumn
accPppIpcpConfigStatus = _AccPppIpcpConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 6, 1, 3),
    _AccPppIpcpConfigStatus_Type()
)
accPppIpcpConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppIpcpConfigStatus.setStatus("mandatory")
_AccPppBncpTable_Object = MibTable
accPppBncpTable = _AccPppBncpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7)
)
if mibBuilder.loadTexts:
    accPppBncpTable.setStatus("mandatory")
_AccPppBncpEntry_Object = MibTableRow
accPppBncpEntry = _AccPppBncpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1)
)
accPppBncpEntry.setIndexNames(
    (0, "ACC-PPP", "accPppBncpIndex"),
)
if mibBuilder.loadTexts:
    accPppBncpEntry.setStatus("mandatory")
_AccPppBncpIndex_Type = Integer32
_AccPppBncpIndex_Object = MibTableColumn
accPppBncpIndex = _AccPppBncpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 1),
    _AccPppBncpIndex_Type()
)
accPppBncpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpIndex.setStatus("mandatory")


class _AccPppBncpLocalToRemoteTinygramCompression_Type(Integer32):
    """Custom type accPppBncpLocalToRemoteTinygramCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AccPppBncpLocalToRemoteTinygramCompression_Type.__name__ = "Integer32"
_AccPppBncpLocalToRemoteTinygramCompression_Object = MibTableColumn
accPppBncpLocalToRemoteTinygramCompression = _AccPppBncpLocalToRemoteTinygramCompression_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 2),
    _AccPppBncpLocalToRemoteTinygramCompression_Type()
)
accPppBncpLocalToRemoteTinygramCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpLocalToRemoteTinygramCompression.setStatus("mandatory")


class _AccPppBncpRemoteToLocalTinygramCompression_Type(Integer32):
    """Custom type accPppBncpRemoteToLocalTinygramCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AccPppBncpRemoteToLocalTinygramCompression_Type.__name__ = "Integer32"
_AccPppBncpRemoteToLocalTinygramCompression_Object = MibTableColumn
accPppBncpRemoteToLocalTinygramCompression = _AccPppBncpRemoteToLocalTinygramCompression_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 3),
    _AccPppBncpRemoteToLocalTinygramCompression_Type()
)
accPppBncpRemoteToLocalTinygramCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpRemoteToLocalTinygramCompression.setStatus("mandatory")


class _AccPppBncpLocalToRemoteLanId_Type(Integer32):
    """Custom type accPppBncpLocalToRemoteLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AccPppBncpLocalToRemoteLanId_Type.__name__ = "Integer32"
_AccPppBncpLocalToRemoteLanId_Object = MibTableColumn
accPppBncpLocalToRemoteLanId = _AccPppBncpLocalToRemoteLanId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 4),
    _AccPppBncpLocalToRemoteLanId_Type()
)
accPppBncpLocalToRemoteLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpLocalToRemoteLanId.setStatus("mandatory")


class _AccPppBncpRemoteToLocalLanId_Type(Integer32):
    """Custom type accPppBncpRemoteToLocalLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AccPppBncpRemoteToLocalLanId_Type.__name__ = "Integer32"
_AccPppBncpRemoteToLocalLanId_Object = MibTableColumn
accPppBncpRemoteToLocalLanId = _AccPppBncpRemoteToLocalLanId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 5),
    _AccPppBncpRemoteToLocalLanId_Type()
)
accPppBncpRemoteToLocalLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpRemoteToLocalLanId.setStatus("mandatory")


class _AccPppBncpOperStatus_Type(Integer32):
    """Custom type accPppBncpOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppBncpOperStatus_Type.__name__ = "Integer32"
_AccPppBncpOperStatus_Object = MibTableColumn
accPppBncpOperStatus = _AccPppBncpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 6),
    _AccPppBncpOperStatus_Type()
)
accPppBncpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpOperStatus.setStatus("mandatory")
_AccPppBncpConfigTable_Object = MibTable
accPppBncpConfigTable = _AccPppBncpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8)
)
if mibBuilder.loadTexts:
    accPppBncpConfigTable.setStatus("mandatory")
_AccPppBncpConfigEntry_Object = MibTableRow
accPppBncpConfigEntry = _AccPppBncpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1)
)
accPppBncpConfigEntry.setIndexNames(
    (0, "ACC-PPP", "accPppBncpConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppBncpConfigEntry.setStatus("mandatory")
_AccPppBncpConfigIndex_Type = Integer32
_AccPppBncpConfigIndex_Object = MibTableColumn
accPppBncpConfigIndex = _AccPppBncpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 1),
    _AccPppBncpConfigIndex_Type()
)
accPppBncpConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpConfigIndex.setStatus("mandatory")


class _AccPppBncpConfigTinygram_Type(Integer32):
    """Custom type accPppBncpConfigTinygram based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AccPppBncpConfigTinygram_Type.__name__ = "Integer32"
_AccPppBncpConfigTinygram_Object = MibTableColumn
accPppBncpConfigTinygram = _AccPppBncpConfigTinygram_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 2),
    _AccPppBncpConfigTinygram_Type()
)
accPppBncpConfigTinygram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppBncpConfigTinygram.setStatus("mandatory")


class _AccPppBncpConfigRingId_Type(Integer32):
    """Custom type accPppBncpConfigRingId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AccPppBncpConfigRingId_Type.__name__ = "Integer32"
_AccPppBncpConfigRingId_Object = MibTableColumn
accPppBncpConfigRingId = _AccPppBncpConfigRingId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 3),
    _AccPppBncpConfigRingId_Type()
)
accPppBncpConfigRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppBncpConfigRingId.setStatus("mandatory")


class _AccPppBncpConfigLineId_Type(Integer32):
    """Custom type accPppBncpConfigLineId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AccPppBncpConfigLineId_Type.__name__ = "Integer32"
_AccPppBncpConfigLineId_Object = MibTableColumn
accPppBncpConfigLineId = _AccPppBncpConfigLineId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 4),
    _AccPppBncpConfigLineId_Type()
)
accPppBncpConfigLineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppBncpConfigLineId.setStatus("mandatory")


class _AccPppBncpConfigLanId_Type(Integer32):
    """Custom type accPppBncpConfigLanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_AccPppBncpConfigLanId_Type.__name__ = "Integer32"
_AccPppBncpConfigLanId_Object = MibTableColumn
accPppBncpConfigLanId = _AccPppBncpConfigLanId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 5),
    _AccPppBncpConfigLanId_Type()
)
accPppBncpConfigLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppBncpConfigLanId.setStatus("mandatory")


class _AccPppBncpConfigAdminStatus_Type(Integer32):
    """Custom type accPppBncpConfigAdminStatus based on Integer32"""
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


_AccPppBncpConfigAdminStatus_Type.__name__ = "Integer32"
_AccPppBncpConfigAdminStatus_Object = MibTableColumn
accPppBncpConfigAdminStatus = _AccPppBncpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 6),
    _AccPppBncpConfigAdminStatus_Type()
)
accPppBncpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppBncpConfigAdminStatus.setStatus("mandatory")
_AccPppXnsTable_Object = MibTable
accPppXnsTable = _AccPppXnsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 9)
)
if mibBuilder.loadTexts:
    accPppXnsTable.setStatus("mandatory")
_AccPppXnsEntry_Object = MibTableRow
accPppXnsEntry = _AccPppXnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 9, 1)
)
accPppXnsEntry.setIndexNames(
    (0, "ACC-PPP", "accPppXnsIndex"),
)
if mibBuilder.loadTexts:
    accPppXnsEntry.setStatus("mandatory")
_AccPppXnsIndex_Type = Integer32
_AccPppXnsIndex_Object = MibTableColumn
accPppXnsIndex = _AccPppXnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 9, 1, 1),
    _AccPppXnsIndex_Type()
)
accPppXnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppXnsIndex.setStatus("mandatory")


class _AccPppXnsOperStatus_Type(Integer32):
    """Custom type accPppXnsOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppXnsOperStatus_Type.__name__ = "Integer32"
_AccPppXnsOperStatus_Object = MibTableColumn
accPppXnsOperStatus = _AccPppXnsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 9, 1, 2),
    _AccPppXnsOperStatus_Type()
)
accPppXnsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppXnsOperStatus.setStatus("mandatory")
_AccPppXnsConfigTable_Object = MibTable
accPppXnsConfigTable = _AccPppXnsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 10)
)
if mibBuilder.loadTexts:
    accPppXnsConfigTable.setStatus("mandatory")
_AccPppXnsConfigEntry_Object = MibTableRow
accPppXnsConfigEntry = _AccPppXnsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 10, 1)
)
accPppXnsConfigEntry.setIndexNames(
    (0, "ACC-PPP", "accPppXnsConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppXnsConfigEntry.setStatus("mandatory")
_AccPppXnsConfigIndex_Type = Integer32
_AccPppXnsConfigIndex_Object = MibTableColumn
accPppXnsConfigIndex = _AccPppXnsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 10, 1, 1),
    _AccPppXnsConfigIndex_Type()
)
accPppXnsConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppXnsConfigIndex.setStatus("mandatory")


class _AccPppXnsConfigAdminStatus_Type(Integer32):
    """Custom type accPppXnsConfigAdminStatus based on Integer32"""
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


_AccPppXnsConfigAdminStatus_Type.__name__ = "Integer32"
_AccPppXnsConfigAdminStatus_Object = MibTableColumn
accPppXnsConfigAdminStatus = _AccPppXnsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 10, 1, 3),
    _AccPppXnsConfigAdminStatus_Type()
)
accPppXnsConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppXnsConfigAdminStatus.setStatus("mandatory")
_AccPppIpxTable_Object = MibTable
accPppIpxTable = _AccPppIpxTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 11)
)
if mibBuilder.loadTexts:
    accPppIpxTable.setStatus("mandatory")
_AccPppIpxEntry_Object = MibTableRow
accPppIpxEntry = _AccPppIpxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 11, 1)
)
accPppIpxEntry.setIndexNames(
    (0, "ACC-PPP", "accPppIpxIndex"),
)
if mibBuilder.loadTexts:
    accPppIpxEntry.setStatus("mandatory")
_AccPppIpxIndex_Type = Integer32
_AccPppIpxIndex_Object = MibTableColumn
accPppIpxIndex = _AccPppIpxIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 11, 1, 1),
    _AccPppIpxIndex_Type()
)
accPppIpxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpxIndex.setStatus("mandatory")


class _AccPppIpxOperStatus_Type(Integer32):
    """Custom type accPppIpxOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppIpxOperStatus_Type.__name__ = "Integer32"
_AccPppIpxOperStatus_Object = MibTableColumn
accPppIpxOperStatus = _AccPppIpxOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 11, 1, 2),
    _AccPppIpxOperStatus_Type()
)
accPppIpxOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpxOperStatus.setStatus("mandatory")
_AccPppIpxConfigTable_Object = MibTable
accPppIpxConfigTable = _AccPppIpxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 12)
)
if mibBuilder.loadTexts:
    accPppIpxConfigTable.setStatus("mandatory")
_AccPppIpxConfigEntry_Object = MibTableRow
accPppIpxConfigEntry = _AccPppIpxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 12, 1)
)
accPppIpxConfigEntry.setIndexNames(
    (0, "ACC-PPP", "accPppIpxConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppIpxConfigEntry.setStatus("mandatory")
_AccPppIpxConfigIndex_Type = Integer32
_AccPppIpxConfigIndex_Object = MibTableColumn
accPppIpxConfigIndex = _AccPppIpxConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 12, 1, 1),
    _AccPppIpxConfigIndex_Type()
)
accPppIpxConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpxConfigIndex.setStatus("mandatory")


class _AccPppIpxConfigAdminStatus_Type(Integer32):
    """Custom type accPppIpxConfigAdminStatus based on Integer32"""
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


_AccPppIpxConfigAdminStatus_Type.__name__ = "Integer32"
_AccPppIpxConfigAdminStatus_Object = MibTableColumn
accPppIpxConfigAdminStatus = _AccPppIpxConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 12, 1, 3),
    _AccPppIpxConfigAdminStatus_Type()
)
accPppIpxConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppIpxConfigAdminStatus.setStatus("mandatory")
_AccPppAppleTable_Object = MibTable
accPppAppleTable = _AccPppAppleTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 13)
)
if mibBuilder.loadTexts:
    accPppAppleTable.setStatus("mandatory")
_AccPppAppleEntry_Object = MibTableRow
accPppAppleEntry = _AccPppAppleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 13, 1)
)
accPppAppleEntry.setIndexNames(
    (0, "ACC-PPP", "accPppAppleIndex"),
)
if mibBuilder.loadTexts:
    accPppAppleEntry.setStatus("mandatory")
_AccPppAppleIndex_Type = Integer32
_AccPppAppleIndex_Object = MibTableColumn
accPppAppleIndex = _AccPppAppleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 13, 1, 1),
    _AccPppAppleIndex_Type()
)
accPppAppleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAppleIndex.setStatus("mandatory")


class _AccPppAppleOperStatus_Type(Integer32):
    """Custom type accPppAppleOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppAppleOperStatus_Type.__name__ = "Integer32"
_AccPppAppleOperStatus_Object = MibTableColumn
accPppAppleOperStatus = _AccPppAppleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 13, 1, 2),
    _AccPppAppleOperStatus_Type()
)
accPppAppleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAppleOperStatus.setStatus("mandatory")
_AccPppAppleConfigTable_Object = MibTable
accPppAppleConfigTable = _AccPppAppleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 14)
)
if mibBuilder.loadTexts:
    accPppAppleConfigTable.setStatus("mandatory")
_AccPppAppleConfigEntry_Object = MibTableRow
accPppAppleConfigEntry = _AccPppAppleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 14, 1)
)
accPppAppleConfigEntry.setIndexNames(
    (0, "ACC-PPP", "accPppAppleConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppAppleConfigEntry.setStatus("mandatory")
_AccPppAppleConfigIndex_Type = Integer32
_AccPppAppleConfigIndex_Object = MibTableColumn
accPppAppleConfigIndex = _AccPppAppleConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 14, 1, 1),
    _AccPppAppleConfigIndex_Type()
)
accPppAppleConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAppleConfigIndex.setStatus("mandatory")


class _AccPppAppleConfigAdminStatus_Type(Integer32):
    """Custom type accPppAppleConfigAdminStatus based on Integer32"""
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


_AccPppAppleConfigAdminStatus_Type.__name__ = "Integer32"
_AccPppAppleConfigAdminStatus_Object = MibTableColumn
accPppAppleConfigAdminStatus = _AccPppAppleConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 14, 1, 3),
    _AccPppAppleConfigAdminStatus_Type()
)
accPppAppleConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAppleConfigAdminStatus.setStatus("mandatory")
_AccPppDecTable_Object = MibTable
accPppDecTable = _AccPppDecTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 15)
)
if mibBuilder.loadTexts:
    accPppDecTable.setStatus("mandatory")
_AccPppDecEntry_Object = MibTableRow
accPppDecEntry = _AccPppDecEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 15, 1)
)
accPppDecEntry.setIndexNames(
    (0, "ACC-PPP", "accPppDecIndex"),
)
if mibBuilder.loadTexts:
    accPppDecEntry.setStatus("mandatory")
_AccPppDecIndex_Type = Integer32
_AccPppDecIndex_Object = MibTableColumn
accPppDecIndex = _AccPppDecIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 15, 1, 1),
    _AccPppDecIndex_Type()
)
accPppDecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppDecIndex.setStatus("mandatory")


class _AccPppDecOperStatus_Type(Integer32):
    """Custom type accPppDecOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppDecOperStatus_Type.__name__ = "Integer32"
_AccPppDecOperStatus_Object = MibTableColumn
accPppDecOperStatus = _AccPppDecOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 15, 1, 2),
    _AccPppDecOperStatus_Type()
)
accPppDecOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppDecOperStatus.setStatus("mandatory")
_AccPppDecConfigTable_Object = MibTable
accPppDecConfigTable = _AccPppDecConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 16)
)
if mibBuilder.loadTexts:
    accPppDecConfigTable.setStatus("mandatory")
_AccPppDecConfigEntry_Object = MibTableRow
accPppDecConfigEntry = _AccPppDecConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 16, 1)
)
accPppDecConfigEntry.setIndexNames(
    (0, "ACC-PPP", "accPppDecConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppDecConfigEntry.setStatus("mandatory")
_AccPppDecConfigIndex_Type = Integer32
_AccPppDecConfigIndex_Object = MibTableColumn
accPppDecConfigIndex = _AccPppDecConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 16, 1, 1),
    _AccPppDecConfigIndex_Type()
)
accPppDecConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppDecConfigIndex.setStatus("mandatory")


class _AccPppDecConfigAdminStatus_Type(Integer32):
    """Custom type accPppDecConfigAdminStatus based on Integer32"""
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


_AccPppDecConfigAdminStatus_Type.__name__ = "Integer32"
_AccPppDecConfigAdminStatus_Object = MibTableColumn
accPppDecConfigAdminStatus = _AccPppDecConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 16, 1, 3),
    _AccPppDecConfigAdminStatus_Type()
)
accPppDecConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppDecConfigAdminStatus.setStatus("mandatory")
_AccPppProtocolTable_Object = MibTable
accPppProtocolTable = _AccPppProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17)
)
if mibBuilder.loadTexts:
    accPppProtocolTable.setStatus("mandatory")
_AccPppProtocolEntry_Object = MibTableRow
accPppProtocolEntry = _AccPppProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17, 1)
)
accPppProtocolEntry.setIndexNames(
    (0, "ACC-PPP", "accPppProtocolIndex"),
)
if mibBuilder.loadTexts:
    accPppProtocolEntry.setStatus("mandatory")
_AccPppProtocolIndex_Type = Integer32
_AccPppProtocolIndex_Object = MibTableColumn
accPppProtocolIndex = _AccPppProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17, 1, 1),
    _AccPppProtocolIndex_Type()
)
accPppProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppProtocolIndex.setStatus("mandatory")


class _AccPppProtocolProtocol_Type(Integer32):
    """Custom type accPppProtocolProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(33,
              35,
              37,
              39,
              41,
              43,
              49,
              53,
              61,
              251,
              253)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 41),
          ("bridge", 49),
          ("ccp", 253),
          ("decnet", 39),
          ("idp", 37),
          ("illcp", 251),
          ("ip", 33),
          ("ipx", 43),
          ("multilink", 61),
          ("osi", 35),
          ("vines", 53))
    )


_AccPppProtocolProtocol_Type.__name__ = "Integer32"
_AccPppProtocolProtocol_Object = MibTableColumn
accPppProtocolProtocol = _AccPppProtocolProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17, 1, 2),
    _AccPppProtocolProtocol_Type()
)
accPppProtocolProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppProtocolProtocol.setStatus("mandatory")


class _AccPppProtocolAdminStatus_Type(Integer32):
    """Custom type accPppProtocolAdminStatus based on Integer32"""
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


_AccPppProtocolAdminStatus_Type.__name__ = "Integer32"
_AccPppProtocolAdminStatus_Object = MibTableColumn
accPppProtocolAdminStatus = _AccPppProtocolAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17, 1, 3),
    _AccPppProtocolAdminStatus_Type()
)
accPppProtocolAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppProtocolAdminStatus.setStatus("mandatory")


class _AccPppProtocolOperStatus_Type(Integer32):
    """Custom type accPppProtocolOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppProtocolOperStatus_Type.__name__ = "Integer32"
_AccPppProtocolOperStatus_Object = MibTableColumn
accPppProtocolOperStatus = _AccPppProtocolOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17, 1, 4),
    _AccPppProtocolOperStatus_Type()
)
accPppProtocolOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppProtocolOperStatus.setStatus("mandatory")
_AccPppMsg_ObjectIdentity = ObjectIdentity
accPppMsg = _AccPppMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 18)
)


class _AccPppMsgLevel_Type(Integer32):
    """Custom type accPppMsgLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccPppMsgLevel_Type.__name__ = "Integer32"
_AccPppMsgLevel_Object = MibScalar
accPppMsgLevel = _AccPppMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 18, 1),
    _AccPppMsgLevel_Type()
)
accPppMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppMsgLevel.setStatus("mandatory")
_AccPppAuthStatTable_Object = MibTable
accPppAuthStatTable = _AccPppAuthStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19)
)
if mibBuilder.loadTexts:
    accPppAuthStatTable.setStatus("mandatory")
_AccPppAuthStatEntry_Object = MibTableRow
accPppAuthStatEntry = _AccPppAuthStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1)
)
accPppAuthStatEntry.setIndexNames(
    (0, "ACC-PPP", "accPppAuthStatIndex"),
)
if mibBuilder.loadTexts:
    accPppAuthStatEntry.setStatus("mandatory")
_AccPppAuthStatIndex_Type = Integer32
_AccPppAuthStatIndex_Object = MibTableColumn
accPppAuthStatIndex = _AccPppAuthStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 1),
    _AccPppAuthStatIndex_Type()
)
accPppAuthStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatIndex.setStatus("mandatory")
_AccPppAuthStatPapReqSents_Type = Counter32
_AccPppAuthStatPapReqSents_Object = MibTableColumn
accPppAuthStatPapReqSents = _AccPppAuthStatPapReqSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 2),
    _AccPppAuthStatPapReqSents_Type()
)
accPppAuthStatPapReqSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatPapReqSents.setStatus("mandatory")
_AccPppAuthStatPapReqRcvs_Type = Counter32
_AccPppAuthStatPapReqRcvs_Object = MibTableColumn
accPppAuthStatPapReqRcvs = _AccPppAuthStatPapReqRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 3),
    _AccPppAuthStatPapReqRcvs_Type()
)
accPppAuthStatPapReqRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatPapReqRcvs.setStatus("mandatory")
_AccPppAuthStatPapAckSents_Type = Counter32
_AccPppAuthStatPapAckSents_Object = MibTableColumn
accPppAuthStatPapAckSents = _AccPppAuthStatPapAckSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 4),
    _AccPppAuthStatPapAckSents_Type()
)
accPppAuthStatPapAckSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatPapAckSents.setStatus("mandatory")
_AccPppAuthStatPapAckRcvs_Type = Counter32
_AccPppAuthStatPapAckRcvs_Object = MibTableColumn
accPppAuthStatPapAckRcvs = _AccPppAuthStatPapAckRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 5),
    _AccPppAuthStatPapAckRcvs_Type()
)
accPppAuthStatPapAckRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatPapAckRcvs.setStatus("mandatory")
_AccPppAuthStatPapNakSents_Type = Counter32
_AccPppAuthStatPapNakSents_Object = MibTableColumn
accPppAuthStatPapNakSents = _AccPppAuthStatPapNakSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 6),
    _AccPppAuthStatPapNakSents_Type()
)
accPppAuthStatPapNakSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatPapNakSents.setStatus("mandatory")
_AccPppAuthStatPapNakRcvs_Type = Counter32
_AccPppAuthStatPapNakRcvs_Object = MibTableColumn
accPppAuthStatPapNakRcvs = _AccPppAuthStatPapNakRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 7),
    _AccPppAuthStatPapNakRcvs_Type()
)
accPppAuthStatPapNakRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatPapNakRcvs.setStatus("mandatory")
_AccPppAuthStatPapRetryTimeouts_Type = Counter32
_AccPppAuthStatPapRetryTimeouts_Object = MibTableColumn
accPppAuthStatPapRetryTimeouts = _AccPppAuthStatPapRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 8),
    _AccPppAuthStatPapRetryTimeouts_Type()
)
accPppAuthStatPapRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatPapRetryTimeouts.setStatus("mandatory")
_AccPppAuthStatChapChallengeSents_Type = Counter32
_AccPppAuthStatChapChallengeSents_Object = MibTableColumn
accPppAuthStatChapChallengeSents = _AccPppAuthStatChapChallengeSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 9),
    _AccPppAuthStatChapChallengeSents_Type()
)
accPppAuthStatChapChallengeSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapChallengeSents.setStatus("mandatory")
_AccPppAuthStatChapChallengeRcvs_Type = Counter32
_AccPppAuthStatChapChallengeRcvs_Object = MibTableColumn
accPppAuthStatChapChallengeRcvs = _AccPppAuthStatChapChallengeRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 10),
    _AccPppAuthStatChapChallengeRcvs_Type()
)
accPppAuthStatChapChallengeRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapChallengeRcvs.setStatus("mandatory")
_AccPppAuthStatChapResponseSents_Type = Counter32
_AccPppAuthStatChapResponseSents_Object = MibTableColumn
accPppAuthStatChapResponseSents = _AccPppAuthStatChapResponseSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 11),
    _AccPppAuthStatChapResponseSents_Type()
)
accPppAuthStatChapResponseSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapResponseSents.setStatus("mandatory")
_AccPppAuthStatChapResponseRcvs_Type = Counter32
_AccPppAuthStatChapResponseRcvs_Object = MibTableColumn
accPppAuthStatChapResponseRcvs = _AccPppAuthStatChapResponseRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 12),
    _AccPppAuthStatChapResponseRcvs_Type()
)
accPppAuthStatChapResponseRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapResponseRcvs.setStatus("mandatory")
_AccPppAuthStatChapAckSents_Type = Counter32
_AccPppAuthStatChapAckSents_Object = MibTableColumn
accPppAuthStatChapAckSents = _AccPppAuthStatChapAckSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 13),
    _AccPppAuthStatChapAckSents_Type()
)
accPppAuthStatChapAckSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapAckSents.setStatus("mandatory")
_AccPppAuthStatChapAckRcvs_Type = Counter32
_AccPppAuthStatChapAckRcvs_Object = MibTableColumn
accPppAuthStatChapAckRcvs = _AccPppAuthStatChapAckRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 14),
    _AccPppAuthStatChapAckRcvs_Type()
)
accPppAuthStatChapAckRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapAckRcvs.setStatus("mandatory")
_AccPppAuthStatChapNakSents_Type = Counter32
_AccPppAuthStatChapNakSents_Object = MibTableColumn
accPppAuthStatChapNakSents = _AccPppAuthStatChapNakSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 15),
    _AccPppAuthStatChapNakSents_Type()
)
accPppAuthStatChapNakSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapNakSents.setStatus("mandatory")
_AccPppAuthStatChapNakRcvs_Type = Counter32
_AccPppAuthStatChapNakRcvs_Object = MibTableColumn
accPppAuthStatChapNakRcvs = _AccPppAuthStatChapNakRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 16),
    _AccPppAuthStatChapNakRcvs_Type()
)
accPppAuthStatChapNakRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapNakRcvs.setStatus("mandatory")
_AccPppAuthStatChapResponseTimeouts_Type = Counter32
_AccPppAuthStatChapResponseTimeouts_Object = MibTableColumn
accPppAuthStatChapResponseTimeouts = _AccPppAuthStatChapResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 17),
    _AccPppAuthStatChapResponseTimeouts_Type()
)
accPppAuthStatChapResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapResponseTimeouts.setStatus("mandatory")
_AccPppAuthStatChapChallengeTimeouts_Type = Counter32
_AccPppAuthStatChapChallengeTimeouts_Object = MibTableColumn
accPppAuthStatChapChallengeTimeouts = _AccPppAuthStatChapChallengeTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 18),
    _AccPppAuthStatChapChallengeTimeouts_Type()
)
accPppAuthStatChapChallengeTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapChallengeTimeouts.setStatus("mandatory")
_AccPppAuthStatChapAckNakTimeouts_Type = Counter32
_AccPppAuthStatChapAckNakTimeouts_Object = MibTableColumn
accPppAuthStatChapAckNakTimeouts = _AccPppAuthStatChapAckNakTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 19),
    _AccPppAuthStatChapAckNakTimeouts_Type()
)
accPppAuthStatChapAckNakTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatChapAckNakTimeouts.setStatus("mandatory")
_AccPppAuthStatLastNegoOptions_Type = Integer32
_AccPppAuthStatLastNegoOptions_Object = MibTableColumn
accPppAuthStatLastNegoOptions = _AccPppAuthStatLastNegoOptions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 20),
    _AccPppAuthStatLastNegoOptions_Type()
)
accPppAuthStatLastNegoOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatLastNegoOptions.setStatus("mandatory")
_AccPppAuthStatOutgoingCallMisMatchs_Type = Counter32
_AccPppAuthStatOutgoingCallMisMatchs_Object = MibTableColumn
accPppAuthStatOutgoingCallMisMatchs = _AccPppAuthStatOutgoingCallMisMatchs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 19, 1, 21),
    _AccPppAuthStatOutgoingCallMisMatchs_Type()
)
accPppAuthStatOutgoingCallMisMatchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthStatOutgoingCallMisMatchs.setStatus("mandatory")
_AccPppAuthParmTable_Object = MibTable
accPppAuthParmTable = _AccPppAuthParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20)
)
if mibBuilder.loadTexts:
    accPppAuthParmTable.setStatus("mandatory")
_AccPppAuthParmEntry_Object = MibTableRow
accPppAuthParmEntry = _AccPppAuthParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1)
)
accPppAuthParmEntry.setIndexNames(
    (0, "ACC-MULTILINK", "accMlPppIndex"),
)
if mibBuilder.loadTexts:
    accPppAuthParmEntry.setStatus("mandatory")
_AccPppAuthParmIndex_Type = Integer32
_AccPppAuthParmIndex_Object = MibTableColumn
accPppAuthParmIndex = _AccPppAuthParmIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1, 1),
    _AccPppAuthParmIndex_Type()
)
accPppAuthParmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAuthParmIndex.setStatus("mandatory")
_AccPppAuthParmUserNameIn_Type = DisplayString
_AccPppAuthParmUserNameIn_Object = MibTableColumn
accPppAuthParmUserNameIn = _AccPppAuthParmUserNameIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1, 2),
    _AccPppAuthParmUserNameIn_Type()
)
accPppAuthParmUserNameIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAuthParmUserNameIn.setStatus("mandatory")
_AccPppAuthParmPasswordIn_Type = DisplayString
_AccPppAuthParmPasswordIn_Object = MibTableColumn
accPppAuthParmPasswordIn = _AccPppAuthParmPasswordIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1, 3),
    _AccPppAuthParmPasswordIn_Type()
)
accPppAuthParmPasswordIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAuthParmPasswordIn.setStatus("mandatory")


class _AccPppAuthParmMethodIn_Type(Integer32):
    """Custom type accPppAuthParmMethodIn based on Integer32"""
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
        *(("chap", 3),
          ("chap-or-pap", 4),
          ("none", 1),
          ("pap", 2))
    )


_AccPppAuthParmMethodIn_Type.__name__ = "Integer32"
_AccPppAuthParmMethodIn_Object = MibTableColumn
accPppAuthParmMethodIn = _AccPppAuthParmMethodIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1, 4),
    _AccPppAuthParmMethodIn_Type()
)
accPppAuthParmMethodIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAuthParmMethodIn.setStatus("mandatory")
_AccPppAuthParmUserNameOut_Type = DisplayString
_AccPppAuthParmUserNameOut_Object = MibTableColumn
accPppAuthParmUserNameOut = _AccPppAuthParmUserNameOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1, 5),
    _AccPppAuthParmUserNameOut_Type()
)
accPppAuthParmUserNameOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAuthParmUserNameOut.setStatus("mandatory")
_AccPppAuthParmPasswordOut_Type = DisplayString
_AccPppAuthParmPasswordOut_Object = MibTableColumn
accPppAuthParmPasswordOut = _AccPppAuthParmPasswordOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1, 6),
    _AccPppAuthParmPasswordOut_Type()
)
accPppAuthParmPasswordOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAuthParmPasswordOut.setStatus("mandatory")


class _AccPppAuthParmMethodOut_Type(Integer32):
    """Custom type accPppAuthParmMethodOut based on Integer32"""
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
        *(("chap", 3),
          ("chap-or-pap", 4),
          ("none", 1),
          ("pap", 2))
    )


_AccPppAuthParmMethodOut_Type.__name__ = "Integer32"
_AccPppAuthParmMethodOut_Object = MibTableColumn
accPppAuthParmMethodOut = _AccPppAuthParmMethodOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1, 7),
    _AccPppAuthParmMethodOut_Type()
)
accPppAuthParmMethodOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAuthParmMethodOut.setStatus("mandatory")
_AccPppAuthParmRetryInterval_Type = TimeTicks
_AccPppAuthParmRetryInterval_Object = MibTableColumn
accPppAuthParmRetryInterval = _AccPppAuthParmRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1, 8),
    _AccPppAuthParmRetryInterval_Type()
)
accPppAuthParmRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAuthParmRetryInterval.setStatus("mandatory")


class _AccPppAuthParmRetryCount_Type(Integer32):
    """Custom type accPppAuthParmRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AccPppAuthParmRetryCount_Type.__name__ = "Integer32"
_AccPppAuthParmRetryCount_Object = MibTableColumn
accPppAuthParmRetryCount = _AccPppAuthParmRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1, 9),
    _AccPppAuthParmRetryCount_Type()
)
accPppAuthParmRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAuthParmRetryCount.setStatus("mandatory")


class _AccPppAuthParmAcctOption_Type(Integer32):
    """Custom type accPppAuthParmAcctOption based on Integer32"""
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


_AccPppAuthParmAcctOption_Type.__name__ = "Integer32"
_AccPppAuthParmAcctOption_Object = MibTableColumn
accPppAuthParmAcctOption = _AccPppAuthParmAcctOption_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 20, 1, 10),
    _AccPppAuthParmAcctOption_Type()
)
accPppAuthParmAcctOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAuthParmAcctOption.setStatus("mandatory")
_AccPppCompressTable_Object = MibTable
accPppCompressTable = _AccPppCompressTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 21)
)
if mibBuilder.loadTexts:
    accPppCompressTable.setStatus("mandatory")
_AccPppCompressEntry_Object = MibTableRow
accPppCompressEntry = _AccPppCompressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 21, 1)
)
accPppCompressEntry.setIndexNames(
    (0, "ACC-PPP", "accPppCompressIndex"),
)
if mibBuilder.loadTexts:
    accPppCompressEntry.setStatus("mandatory")
_AccPppCompressIndex_Type = Integer32
_AccPppCompressIndex_Object = MibTableColumn
accPppCompressIndex = _AccPppCompressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 21, 1, 1),
    _AccPppCompressIndex_Type()
)
accPppCompressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressIndex.setStatus("mandatory")
_AccPppCompressMsgLevel_Type = Integer32
_AccPppCompressMsgLevel_Object = MibTableColumn
accPppCompressMsgLevel = _AccPppCompressMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 21, 1, 2),
    _AccPppCompressMsgLevel_Type()
)
accPppCompressMsgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressMsgLevel.setStatus("mandatory")


class _AccPppCompressMethod_Type(Integer32):
    """Custom type accPppCompressMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("mppc", 7),
          ("nego", 2),
          ("none", 1),
          ("stac-extd", 5),
          ("stac-none", 6),
          ("stac-seqn", 4),
          ("vendor", 3))
    )


_AccPppCompressMethod_Type.__name__ = "Integer32"
_AccPppCompressMethod_Object = MibTableColumn
accPppCompressMethod = _AccPppCompressMethod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 21, 1, 3),
    _AccPppCompressMethod_Type()
)
accPppCompressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppCompressMethod.setStatus("mandatory")


class _AccPppCompressStream_Type(Integer32):
    """Custom type accPppCompressStream based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("stream", 2))
    )


_AccPppCompressStream_Type.__name__ = "Integer32"
_AccPppCompressStream_Object = MibTableColumn
accPppCompressStream = _AccPppCompressStream_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 21, 1, 4),
    _AccPppCompressStream_Type()
)
accPppCompressStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppCompressStream.setStatus("mandatory")


class _AccPppCompressNegoMethodIn_Type(Integer32):
    """Custom type accPppCompressNegoMethodIn based on Integer32"""
    defaultValue = 1

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
        *(("mppc", 6),
          ("none", 1),
          ("stac-extd", 4),
          ("stac-none", 5),
          ("stac-seqn", 3),
          ("vendor", 2))
    )


_AccPppCompressNegoMethodIn_Type.__name__ = "Integer32"
_AccPppCompressNegoMethodIn_Object = MibTableColumn
accPppCompressNegoMethodIn = _AccPppCompressNegoMethodIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 21, 1, 5),
    _AccPppCompressNegoMethodIn_Type()
)
accPppCompressNegoMethodIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppCompressNegoMethodIn.setStatus("mandatory")


class _AccPppCompressNegoMethodOut_Type(Integer32):
    """Custom type accPppCompressNegoMethodOut based on Integer32"""
    defaultValue = 1

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
        *(("mppc", 6),
          ("none", 1),
          ("stac-extd", 4),
          ("stac-none", 5),
          ("stac-seqn", 3),
          ("vendor", 2))
    )


_AccPppCompressNegoMethodOut_Type.__name__ = "Integer32"
_AccPppCompressNegoMethodOut_Object = MibTableColumn
accPppCompressNegoMethodOut = _AccPppCompressNegoMethodOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 21, 1, 6),
    _AccPppCompressNegoMethodOut_Type()
)
accPppCompressNegoMethodOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppCompressNegoMethodOut.setStatus("mandatory")


class _AccPppCompressNegoStreamIn_Type(Integer32):
    """Custom type accPppCompressNegoStreamIn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("stream", 2))
    )


_AccPppCompressNegoStreamIn_Type.__name__ = "Integer32"
_AccPppCompressNegoStreamIn_Object = MibTableColumn
accPppCompressNegoStreamIn = _AccPppCompressNegoStreamIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 21, 1, 7),
    _AccPppCompressNegoStreamIn_Type()
)
accPppCompressNegoStreamIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppCompressNegoStreamIn.setStatus("mandatory")


class _AccPppCompressNegoStreamOut_Type(Integer32):
    """Custom type accPppCompressNegoStreamOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("stream", 2))
    )


_AccPppCompressNegoStreamOut_Type.__name__ = "Integer32"
_AccPppCompressNegoStreamOut_Object = MibTableColumn
accPppCompressNegoStreamOut = _AccPppCompressNegoStreamOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 21, 1, 8),
    _AccPppCompressNegoStreamOut_Type()
)
accPppCompressNegoStreamOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppCompressNegoStreamOut.setStatus("mandatory")
_AccPppCompressStatTable_Object = MibTable
accPppCompressStatTable = _AccPppCompressStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22)
)
if mibBuilder.loadTexts:
    accPppCompressStatTable.setStatus("mandatory")
_AccPppCompressStatEntry_Object = MibTableRow
accPppCompressStatEntry = _AccPppCompressStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1)
)
accPppCompressStatEntry.setIndexNames(
    (0, "ACC-PPP", "accPppCompressStatIndex"),
)
if mibBuilder.loadTexts:
    accPppCompressStatEntry.setStatus("mandatory")
_AccPppCompressStatIndex_Type = Integer32
_AccPppCompressStatIndex_Object = MibTableColumn
accPppCompressStatIndex = _AccPppCompressStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 1),
    _AccPppCompressStatIndex_Type()
)
accPppCompressStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatIndex.setStatus("mandatory")


class _AccPppCompressStatStatusIn_Type(Integer32):
    """Custom type accPppCompressStatStatusIn based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccPppCompressStatStatusIn_Type.__name__ = "Integer32"
_AccPppCompressStatStatusIn_Object = MibTableColumn
accPppCompressStatStatusIn = _AccPppCompressStatStatusIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 2),
    _AccPppCompressStatStatusIn_Type()
)
accPppCompressStatStatusIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatStatusIn.setStatus("mandatory")


class _AccPppCompressStatStatusOut_Type(Integer32):
    """Custom type accPppCompressStatStatusOut based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccPppCompressStatStatusOut_Type.__name__ = "Integer32"
_AccPppCompressStatStatusOut_Object = MibTableColumn
accPppCompressStatStatusOut = _AccPppCompressStatStatusOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 3),
    _AccPppCompressStatStatusOut_Type()
)
accPppCompressStatStatusOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatStatusOut.setStatus("mandatory")
_AccPppCompressStatAvgCompIn_Type = Gauge32
_AccPppCompressStatAvgCompIn_Object = MibTableColumn
accPppCompressStatAvgCompIn = _AccPppCompressStatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 4),
    _AccPppCompressStatAvgCompIn_Type()
)
accPppCompressStatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatAvgCompIn.setStatus("mandatory")
_AccPppCompressStatAvgCompOut_Type = Gauge32
_AccPppCompressStatAvgCompOut_Object = MibTableColumn
accPppCompressStatAvgCompOut = _AccPppCompressStatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 5),
    _AccPppCompressStatAvgCompOut_Type()
)
accPppCompressStatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatAvgCompOut.setStatus("mandatory")
_AccPppCompressStatInOctets_Type = Counter32
_AccPppCompressStatInOctets_Object = MibTableColumn
accPppCompressStatInOctets = _AccPppCompressStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 6),
    _AccPppCompressStatInOctets_Type()
)
accPppCompressStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatInOctets.setStatus("mandatory")
_AccPppCompressStatOutOctets_Type = Counter32
_AccPppCompressStatOutOctets_Object = MibTableColumn
accPppCompressStatOutOctets = _AccPppCompressStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 7),
    _AccPppCompressStatOutOctets_Type()
)
accPppCompressStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatOutOctets.setStatus("mandatory")
_AccPppCompressStatInPackets_Type = Counter32
_AccPppCompressStatInPackets_Object = MibTableColumn
accPppCompressStatInPackets = _AccPppCompressStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 8),
    _AccPppCompressStatInPackets_Type()
)
accPppCompressStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatInPackets.setStatus("mandatory")
_AccPppCompressStatOutPackets_Type = Counter32
_AccPppCompressStatOutPackets_Object = MibTableColumn
accPppCompressStatOutPackets = _AccPppCompressStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 9),
    _AccPppCompressStatOutPackets_Type()
)
accPppCompressStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatOutPackets.setStatus("mandatory")
_AccPppCompressUnCompInStats_Type = Counter32
_AccPppCompressUnCompInStats_Object = MibTableColumn
accPppCompressUnCompInStats = _AccPppCompressUnCompInStats_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 10),
    _AccPppCompressUnCompInStats_Type()
)
accPppCompressUnCompInStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressUnCompInStats.setStatus("mandatory")
_AccPppCompressUnCompOutStats_Type = Counter32
_AccPppCompressUnCompOutStats_Object = MibTableColumn
accPppCompressUnCompOutStats = _AccPppCompressUnCompOutStats_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 11),
    _AccPppCompressUnCompOutStats_Type()
)
accPppCompressUnCompOutStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressUnCompOutStats.setStatus("mandatory")
_AccPppCompressStatHdrErrors_Type = Counter32
_AccPppCompressStatHdrErrors_Object = MibTableColumn
accPppCompressStatHdrErrors = _AccPppCompressStatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 12),
    _AccPppCompressStatHdrErrors_Type()
)
accPppCompressStatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatHdrErrors.setStatus("mandatory")
_AccPppCompressStatResyncs_Type = Counter32
_AccPppCompressStatResyncs_Object = MibTableColumn
accPppCompressStatResyncs = _AccPppCompressStatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 13),
    _AccPppCompressStatResyncs_Type()
)
accPppCompressStatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatResyncs.setStatus("mandatory")
_AccPppCompressStatNoEndMarks_Type = Counter32
_AccPppCompressStatNoEndMarks_Object = MibTableColumn
accPppCompressStatNoEndMarks = _AccPppCompressStatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 14),
    _AccPppCompressStatNoEndMarks_Type()
)
accPppCompressStatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatNoEndMarks.setStatus("mandatory")
_AccPppCompressStatNoAvailBufs_Type = Counter32
_AccPppCompressStatNoAvailBufs_Object = MibTableColumn
accPppCompressStatNoAvailBufs = _AccPppCompressStatNoAvailBufs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 15),
    _AccPppCompressStatNoAvailBufs_Type()
)
accPppCompressStatNoAvailBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatNoAvailBufs.setStatus("mandatory")
_AccPppCompressStatRcvResetReqs_Type = Counter32
_AccPppCompressStatRcvResetReqs_Object = MibTableColumn
accPppCompressStatRcvResetReqs = _AccPppCompressStatRcvResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 16),
    _AccPppCompressStatRcvResetReqs_Type()
)
accPppCompressStatRcvResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatRcvResetReqs.setStatus("mandatory")
_AccPppCompressStatRcvResetAcks_Type = Counter32
_AccPppCompressStatRcvResetAcks_Object = MibTableColumn
accPppCompressStatRcvResetAcks = _AccPppCompressStatRcvResetAcks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 17),
    _AccPppCompressStatRcvResetAcks_Type()
)
accPppCompressStatRcvResetAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatRcvResetAcks.setStatus("mandatory")
_AccPppCompressStatSndResetReqs_Type = Counter32
_AccPppCompressStatSndResetReqs_Object = MibTableColumn
accPppCompressStatSndResetReqs = _AccPppCompressStatSndResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 18),
    _AccPppCompressStatSndResetReqs_Type()
)
accPppCompressStatSndResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatSndResetReqs.setStatus("mandatory")
_AccPppCompressStatSndResetAcks_Type = Counter32
_AccPppCompressStatSndResetAcks_Object = MibTableColumn
accPppCompressStatSndResetAcks = _AccPppCompressStatSndResetAcks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 19),
    _AccPppCompressStatSndResetAcks_Type()
)
accPppCompressStatSndResetAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatSndResetAcks.setStatus("mandatory")
_AccPppCompressStatExpandIn_Type = Integer32
_AccPppCompressStatExpandIn_Object = MibTableColumn
accPppCompressStatExpandIn = _AccPppCompressStatExpandIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 20),
    _AccPppCompressStatExpandIn_Type()
)
accPppCompressStatExpandIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatExpandIn.setStatus("mandatory")
_AccPppCompressStatExpandOut_Type = Integer32
_AccPppCompressStatExpandOut_Object = MibTableColumn
accPppCompressStatExpandOut = _AccPppCompressStatExpandOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 21),
    _AccPppCompressStatExpandOut_Type()
)
accPppCompressStatExpandOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatExpandOut.setStatus("mandatory")
_AccPppCompressStatDiscardIn_Type = Integer32
_AccPppCompressStatDiscardIn_Object = MibTableColumn
accPppCompressStatDiscardIn = _AccPppCompressStatDiscardIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 22),
    _AccPppCompressStatDiscardIn_Type()
)
accPppCompressStatDiscardIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatDiscardIn.setStatus("mandatory")
_AccPppCompressStatDiscardOut_Type = Integer32
_AccPppCompressStatDiscardOut_Object = MibTableColumn
accPppCompressStatDiscardOut = _AccPppCompressStatDiscardOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 22, 1, 23),
    _AccPppCompressStatDiscardOut_Type()
)
accPppCompressStatDiscardOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppCompressStatDiscardOut.setStatus("mandatory")
_AccIpHeaderCompStatTable_Object = MibTable
accIpHeaderCompStatTable = _AccIpHeaderCompStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23)
)
if mibBuilder.loadTexts:
    accIpHeaderCompStatTable.setStatus("mandatory")
_AccIpHeaderCompStatEntry_Object = MibTableRow
accIpHeaderCompStatEntry = _AccIpHeaderCompStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23, 1)
)
accIpHeaderCompStatEntry.setIndexNames(
    (0, "ACC-PPP", "accPppLinkVjhcStatIndex"),
)
if mibBuilder.loadTexts:
    accIpHeaderCompStatEntry.setStatus("mandatory")
_AccPppLinkVjhcStatIndex_Type = Integer32
_AccPppLinkVjhcStatIndex_Object = MibTableColumn
accPppLinkVjhcStatIndex = _AccPppLinkVjhcStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23, 1, 1),
    _AccPppLinkVjhcStatIndex_Type()
)
accPppLinkVjhcStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkVjhcStatIndex.setStatus("mandatory")


class _AccPppLinkVjhcOper_Type(Integer32):
    """Custom type accPppLinkVjhcOper based on Integer32"""
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


_AccPppLinkVjhcOper_Type.__name__ = "Integer32"
_AccPppLinkVjhcOper_Object = MibTableColumn
accPppLinkVjhcOper = _AccPppLinkVjhcOper_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23, 1, 2),
    _AccPppLinkVjhcOper_Type()
)
accPppLinkVjhcOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkVjhcOper.setStatus("mandatory")


class _AccPppLinkVjhcNegot_Type(Integer32):
    """Custom type accPppLinkVjhcNegot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("notApp", 1),
          ("success", 3))
    )


_AccPppLinkVjhcNegot_Type.__name__ = "Integer32"
_AccPppLinkVjhcNegot_Object = MibTableColumn
accPppLinkVjhcNegot = _AccPppLinkVjhcNegot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23, 1, 3),
    _AccPppLinkVjhcNegot_Type()
)
accPppLinkVjhcNegot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkVjhcNegot.setStatus("mandatory")
_AccPppLinkVjhcCompIn_Type = Integer32
_AccPppLinkVjhcCompIn_Object = MibTableColumn
accPppLinkVjhcCompIn = _AccPppLinkVjhcCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23, 1, 4),
    _AccPppLinkVjhcCompIn_Type()
)
accPppLinkVjhcCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkVjhcCompIn.setStatus("mandatory")
_AccPppLinkVjhcUnCompIn_Type = Integer32
_AccPppLinkVjhcUnCompIn_Object = MibTableColumn
accPppLinkVjhcUnCompIn = _AccPppLinkVjhcUnCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23, 1, 5),
    _AccPppLinkVjhcUnCompIn_Type()
)
accPppLinkVjhcUnCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkVjhcUnCompIn.setStatus("mandatory")
_AccPppLinkVjhcErrIn_Type = Integer32
_AccPppLinkVjhcErrIn_Object = MibTableColumn
accPppLinkVjhcErrIn = _AccPppLinkVjhcErrIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23, 1, 6),
    _AccPppLinkVjhcErrIn_Type()
)
accPppLinkVjhcErrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkVjhcErrIn.setStatus("mandatory")
_AccPppLinkVjhcCompOut_Type = Integer32
_AccPppLinkVjhcCompOut_Object = MibTableColumn
accPppLinkVjhcCompOut = _AccPppLinkVjhcCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23, 1, 7),
    _AccPppLinkVjhcCompOut_Type()
)
accPppLinkVjhcCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkVjhcCompOut.setStatus("mandatory")
_AccPppLinkVjhcUnCompOut_Type = Integer32
_AccPppLinkVjhcUnCompOut_Object = MibTableColumn
accPppLinkVjhcUnCompOut = _AccPppLinkVjhcUnCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23, 1, 8),
    _AccPppLinkVjhcUnCompOut_Type()
)
accPppLinkVjhcUnCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkVjhcUnCompOut.setStatus("mandatory")
_AccPppLinkVjhcErrOut_Type = Integer32
_AccPppLinkVjhcErrOut_Object = MibTableColumn
accPppLinkVjhcErrOut = _AccPppLinkVjhcErrOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 23, 1, 9),
    _AccPppLinkVjhcErrOut_Type()
)
accPppLinkVjhcErrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkVjhcErrOut.setStatus("mandatory")
_AccPppTraps_ObjectIdentity = ObjectIdentity
accPppTraps = _AccPppTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 24)
)
_AccPppTrapMsg_Type = DisplayString
_AccPppTrapMsg_Object = MibScalar
accPppTrapMsg = _AccPppTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 24, 1),
    _AccPppTrapMsg_Type()
)
accPppTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accDodPasswdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 1)
)
accDodPasswdTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDodPasswdTrap.setStatus(
        ""
    )

accPppAuthDenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 2)
)
accPppAuthDenTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-PPP", "accPppAuthParmMethodIn"),
        ("ACC-PPP", "accPppAuthParmUserNameIn"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accPppAuthDenTrap.setStatus(
        ""
    )

accPppAuthNakTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 3)
)
accPppAuthNakTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-PPP", "accDialPortAuthType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accPppAuthNakTrap.setStatus(
        ""
    )

accDodDialTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 4)
)
accDodDialTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-PPP", "accDialPortIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDodDialTrap.setStatus(
        ""
    )

accDodNoCktTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 5)
)
accDodNoCktTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-MULTILINK", "accMlPppIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDodNoCktTrap.setStatus(
        ""
    )

accDodPrtBumpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 6)
)
accDodPrtBumpTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-PPP", "accDialPortIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDodPrtBumpTrap.setStatus(
        ""
    )

accPhyPrtNotAvailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 7)
)
accPhyPrtNotAvailTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-MULTILINK", "accMlPppIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accPhyPrtNotAvailTrap.setStatus(
        ""
    )

accDodCompressionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 8)
)
accDodCompressionTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-PPP", "accDialPortIndex"),
        ("ACC-PPP", "accDialPortProtocol"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDodCompressionTrap.setStatus(
        ""
    )

accPortInUseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 9)
)
accPortInUseTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-PPP", "accDialPortIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accPortInUseTrap.setStatus(
        ""
    )

accDodMaxPapPasswdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 10)
)
accDodMaxPapPasswdTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDodMaxPapPasswdTrap.setStatus(
        ""
    )

accDodNeedResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 15, 0, 11)
)
accDodNeedResetTrap.setObjects(
      *(("ACC-PPP", "accDodTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accDodNeedResetTrap.setStatus(
        ""
    )

accPppUnIdentifiedSourceTrap1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 24, 0, 1)
)
accPppUnIdentifiedSourceTrap1.setObjects(
      *(("ACC-PPP", "accPppTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accPppUnIdentifiedSourceTrap1.setStatus(
        ""
    )

accPppLoopBackTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 24, 0, 2)
)
accPppLoopBackTrap2.setObjects(
      *(("ACC-PPP", "accPppTrapMsg"),
        ("IF-MIB", "ifIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accPppLoopBackTrap2.setStatus(
        ""
    )

accPppCallBackTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 24, 0, 3)
)
accPppCallBackTrap3.setObjects(
      *(("ACC-PPP", "accPppTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accPppCallBackTrap3.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-PPP",
    **{"CallAddress": CallAddress,
       "BackupPort": BackupPort,
       "PhysicalPort": PhysicalPort,
       "accMlPppCompressTable": accMlPppCompressTable,
       "accMlPppCompressEntry": accMlPppCompressEntry,
       "accMlPppCompressIndex": accMlPppCompressIndex,
       "accMlPppCompressMsgLevel": accMlPppCompressMsgLevel,
       "accMlPppCompressMethod": accMlPppCompressMethod,
       "accMlPppCompressStream": accMlPppCompressStream,
       "accMlPppCompressNegoMethodIn": accMlPppCompressNegoMethodIn,
       "accMlPppCompressNegoMethodOut": accMlPppCompressNegoMethodOut,
       "accMlPppCompressNegoStreamIn": accMlPppCompressNegoStreamIn,
       "accMlPppCompressNegoStreamOut": accMlPppCompressNegoStreamOut,
       "accMlPppCompressStatTable": accMlPppCompressStatTable,
       "accMlPppCompressStatEntry": accMlPppCompressStatEntry,
       "accMlPppCompressStatIndex": accMlPppCompressStatIndex,
       "accMlPppCompressStatStatus": accMlPppCompressStatStatus,
       "accMlPppCompressStatAvgCompIn": accMlPppCompressStatAvgCompIn,
       "accMlPppCompressStatAvgCompOut": accMlPppCompressStatAvgCompOut,
       "accMlPppCompressStatInOctets": accMlPppCompressStatInOctets,
       "accMlPppCompressStatOutOctets": accMlPppCompressStatOutOctets,
       "accMlPppCompressStatInPackets": accMlPppCompressStatInPackets,
       "accMlPppCompressStatOutPackets": accMlPppCompressStatOutPackets,
       "accMlPppCompressUnCompInStats": accMlPppCompressUnCompInStats,
       "accMlPppCompressUnCompOutStats": accMlPppCompressUnCompOutStats,
       "accMlPppCompressStatHdrErrors": accMlPppCompressStatHdrErrors,
       "accMlPppCompressStatResyncs": accMlPppCompressStatResyncs,
       "accMlPppCompressStatNoEndMarks": accMlPppCompressStatNoEndMarks,
       "accMlPppCompressStatNoAvailBufs": accMlPppCompressStatNoAvailBufs,
       "accMlPppCompressStatRcvResetReqs": accMlPppCompressStatRcvResetReqs,
       "accMlPppCompressStatRcvResetAcks": accMlPppCompressStatRcvResetAcks,
       "accMlPppCompressStatSndResetReqs": accMlPppCompressStatSndResetReqs,
       "accMlPppCompressStatSndResetAcks": accMlPppCompressStatSndResetAcks,
       "accDial": accDial,
       "accDialBackupTable": accDialBackupTable,
       "accDialBackupEntry": accDialBackupEntry,
       "accDialBackupPort": accDialBackupPort,
       "accDialBackupPrimary": accDialBackupPrimary,
       "accDialBackupControl": accDialBackupControl,
       "accDialBackupRetry": accDialBackupRetry,
       "accDialBackupDamp": accDialBackupDamp,
       "accDialBackupCallCongestion": accDialBackupCallCongestion,
       "accDialBackupClearCongestion": accDialBackupClearCongestion,
       "accDialBackupCallError": accDialBackupCallError,
       "accDialBackupCallAddress": accDialBackupCallAddress,
       "accDialBackupStatus": accDialBackupStatus,
       "accDialBackupState": accDialBackupState,
       "accDialPortTable": accDialPortTable,
       "accDialPortEntry": accDialPortEntry,
       "accDialPortIndex": accDialPortIndex,
       "accDialPortContents": accDialPortContents,
       "accDialPortStationType": accDialPortStationType,
       "accDialPortAdminState": accDialPortAdminState,
       "accDialPortCallState": accDialPortCallState,
       "accDialPortRetryInterval": accDialPortRetryInterval,
       "accDialPortRetryCount": accDialPortRetryCount,
       "accDialPortClearingInterv": accDialPortClearingInterv,
       "accDialPortMessageLevel": accDialPortMessageLevel,
       "accDialPortPhysicalPort": accDialPortPhysicalPort,
       "accDialPortCallAddress": accDialPortCallAddress,
       "accDialPortPhysicalPortStr": accDialPortPhysicalPortStr,
       "accDialPortCallAddressStr": accDialPortCallAddressStr,
       "accDialPortPassword": accDialPortPassword,
       "accDialPortName": accDialPortName,
       "accDialPortAuthType": accDialPortAuthType,
       "accDialPortSessionTimeout": accDialPortSessionTimeout,
       "accDialPortPriority": accDialPortPriority,
       "accDialPortCallBack": accDialPortCallBack,
       "accDialPortProtocol": accDialPortProtocol,
       "accDialPortAuthPeer": accDialPortAuthPeer,
       "accDialPortPromptState": accDialPortPromptState,
       "accDialPortLogin": accDialPortLogin,
       "accDialPortStatTable": accDialPortStatTable,
       "accDialPortStatEntry": accDialPortStatEntry,
       "accDialPortStatIndex": accDialPortStatIndex,
       "accDialPortStatActPhysPort": accDialPortStatActPhysPort,
       "accDialPortStatState": accDialPortStatState,
       "accDialPortStatTrigFwdr": accDialPortStatTrigFwdr,
       "accDialPortStatElapsedTime": accDialPortStatElapsedTime,
       "accDialPortStatTrigSrcAddr": accDialPortStatTrigSrcAddr,
       "accDialPortStatTrigCallAddr": accDialPortStatTrigCallAddr,
       "accDialPortStatSuccessOuts": accDialPortStatSuccessOuts,
       "accDialPortStatUnsuccessOuts": accDialPortStatUnsuccessOuts,
       "accDialPortStatSuccessIns": accDialPortStatSuccessIns,
       "accDialPortStatUnsuccessIns": accDialPortStatUnsuccessIns,
       "accDialPortStatAuthTypeClashes": accDialPortStatAuthTypeClashes,
       "accDialPortStatDisconnReasons": accDialPortStatDisconnReasons,
       "accDialOrigAtTable": accDialOrigAtTable,
       "accDialOrigAtEntry": accDialOrigAtEntry,
       "accDialOrigAtStatus": accDialOrigAtStatus,
       "accDialOrigAtDestStart": accDialOrigAtDestStart,
       "accDialOrigAtDestEnd": accDialOrigAtDestEnd,
       "accDialOrigAtSourceStart": accDialOrigAtSourceStart,
       "accDialOrigAtSourceEnd": accDialOrigAtSourceEnd,
       "accDialOrigAtTraffic": accDialOrigAtTraffic,
       "accDialOrigAtAction": accDialOrigAtAction,
       "accDialOrigDnTable": accDialOrigDnTable,
       "accDialOrigDnEntry": accDialOrigDnEntry,
       "accDialOrigDnStatus": accDialOrigDnStatus,
       "accDialOrigDnDestAddr": accDialOrigDnDestAddr,
       "accDialOrigDnSourceAddr": accDialOrigDnSourceAddr,
       "accDialOrigDnAction": accDialOrigDnAction,
       "accDialOrigBrTable": accDialOrigBrTable,
       "accDialOrigBrEntry": accDialOrigBrEntry,
       "accDialOrigBrStatus": accDialOrigBrStatus,
       "accDialOrigBrDestMacAddr": accDialOrigBrDestMacAddr,
       "accDialOrigBrSourceMacAddr": accDialOrigBrSourceMacAddr,
       "accDialOrigBrAction": accDialOrigBrAction,
       "accDialOrigIdpTable": accDialOrigIdpTable,
       "accDialOrigIdpEntry": accDialOrigIdpEntry,
       "accDialOrigIdpStatus": accDialOrigIdpStatus,
       "accDialOrigIdpDestNet": accDialOrigIdpDestNet,
       "accDialOrigIdpSourceNet": accDialOrigIdpSourceNet,
       "accDialOrigIdpAction": accDialOrigIdpAction,
       "accDialOrigIpTable": accDialOrigIpTable,
       "accDialOrigIpEntry": accDialOrigIpEntry,
       "accDialOrigIpStatus": accDialOrigIpStatus,
       "accDialOrigIpDestAddr": accDialOrigIpDestAddr,
       "accDialOrigIpDestMask": accDialOrigIpDestMask,
       "accDialOrigIpSourceAddr": accDialOrigIpSourceAddr,
       "accDialOrigIpSourceMask": accDialOrigIpSourceMask,
       "accDialOrigIpParm": accDialOrigIpParm,
       "accDialOrigIpAction": accDialOrigIpAction,
       "accDialOrigIpxTable": accDialOrigIpxTable,
       "accDialOrigIpxEntry": accDialOrigIpxEntry,
       "accDialOrigIpxStatus": accDialOrigIpxStatus,
       "accDialOrigIpxDestNet": accDialOrigIpxDestNet,
       "accDialOrigIpxSourceNet": accDialOrigIpxSourceNet,
       "accDialOrigIpxAction": accDialOrigIpxAction,
       "accDialOrigSrTable": accDialOrigSrTable,
       "accDialOrigSrEntry": accDialOrigSrEntry,
       "accDialOrigSrStatus": accDialOrigSrStatus,
       "accDialOrigSrDestMacAddr": accDialOrigSrDestMacAddr,
       "accDialOrigSrSourceMacAddr": accDialOrigSrSourceMacAddr,
       "accDialOrigSrAction": accDialOrigSrAction,
       "accDialPortRange": accDialPortRange,
       "accDialPortMaxCount": accDialPortMaxCount,
       "accDialPortRangeStart": accDialPortRangeStart,
       "accDialPortRangeEnd": accDialPortRangeEnd,
       "accDialPortConnTable": accDialPortConnTable,
       "accDialPortConnEntry": accDialPortConnEntry,
       "accDialPortConnIndex": accDialPortConnIndex,
       "accDialPortConnUser": accDialPortConnUser,
       "accDialPortConnPhyPort": accDialPortConnPhyPort,
       "accDialPortConnLogPort": accDialPortConnLogPort,
       "accDialPortConnDir": accDialPortConnDir,
       "accDialPortConnAuth": accDialPortConnAuth,
       "accDialPortConnStart": accDialPortConnStart,
       "accDialPortConnProf": accDialPortConnProf,
       "accDialPortConnStack": accDialPortConnStack,
       "accDialPortConnAddr": accDialPortConnAddr,
       "accDialPortConnState": accDialPortConnState,
       "accDialPortCompressTable": accDialPortCompressTable,
       "accDialPortCompressEntry": accDialPortCompressEntry,
       "accDialPortCompressIndex": accDialPortCompressIndex,
       "accDialPortCompressMsgLevel": accDialPortCompressMsgLevel,
       "accDialPortCompressMethod": accDialPortCompressMethod,
       "accDialPortCompressStream": accDialPortCompressStream,
       "accDialPortCompressNegoMethodIn": accDialPortCompressNegoMethodIn,
       "accDialPortCompressNegoMethodOut": accDialPortCompressNegoMethodOut,
       "accDialPortCompressNegoStreamIn": accDialPortCompressNegoStreamIn,
       "accDialPortCompressNegoStreamOut": accDialPortCompressNegoStreamOut,
       "accAccessParameter": accAccessParameter,
       "accAccessTimer": accAccessTimer,
       "accAccessCreditDay": accAccessCreditDay,
       "accAccessCreditYear": accAccessCreditYear,
       "accAccessTime": accAccessTime,
       "accAccessLimitDate": accAccessLimitDate,
       "accAccessDay": accAccessDay,
       "accAccessDayCreditLeft": accAccessDayCreditLeft,
       "accAccessYearCreditLeft": accAccessYearCreditLeft,
       "accDodTraps": accDodTraps,
       "accDodPasswdTrap": accDodPasswdTrap,
       "accPppAuthDenTrap": accPppAuthDenTrap,
       "accPppAuthNakTrap": accPppAuthNakTrap,
       "accDodDialTrap": accDodDialTrap,
       "accDodNoCktTrap": accDodNoCktTrap,
       "accDodPrtBumpTrap": accDodPrtBumpTrap,
       "accPhyPrtNotAvailTrap": accPhyPrtNotAvailTrap,
       "accDodCompressionTrap": accDodCompressionTrap,
       "accPortInUseTrap": accPortInUseTrap,
       "accDodMaxPapPasswdTrap": accDodMaxPapPasswdTrap,
       "accDodNeedResetTrap": accDodNeedResetTrap,
       "accDodTrapMsg": accDodTrapMsg,
       "accPpp": accPpp,
       "accPppLinkTable": accPppLinkTable,
       "accPppLinkEntry": accPppLinkEntry,
       "accPppLinkIndex": accPppLinkIndex,
       "accPppLinkPhysicalIndex": accPppLinkPhysicalIndex,
       "accPppLinkBadAddresses": accPppLinkBadAddresses,
       "accPppLinkBadControls": accPppLinkBadControls,
       "accPppLinkPacketTooLongs": accPppLinkPacketTooLongs,
       "accPppLinkBadFCSs": accPppLinkBadFCSs,
       "accPppLinkLocalMRU": accPppLinkLocalMRU,
       "accPppLinkRemoteMRU": accPppLinkRemoteMRU,
       "accPppLinkLocalToPeerACCMap": accPppLinkLocalToPeerACCMap,
       "accPppLinkPeerToLocalACCMap": accPppLinkPeerToLocalACCMap,
       "accPppLinkLocalToRemotePC": accPppLinkLocalToRemotePC,
       "accPppLinkRemoteToLocalPC": accPppLinkRemoteToLocalPC,
       "accPppLinkLocalToRemoteAC": accPppLinkLocalToRemoteAC,
       "accPppLinkRemoteToLocalAC": accPppLinkRemoteToLocalAC,
       "accPppLinkTransmit32BitFcs": accPppLinkTransmit32BitFcs,
       "accPppLinkReceive32BitFcs": accPppLinkReceive32BitFcs,
       "accPppLinkOperStatus": accPppLinkOperStatus,
       "accPppLinkPacketTooShorts": accPppLinkPacketTooShorts,
       "accPppLinkUnknownProtocols": accPppLinkUnknownProtocols,
       "accPppLinkPacketInDiscards": accPppLinkPacketInDiscards,
       "accPppLinkPacketOutDiscards": accPppLinkPacketOutDiscards,
       "accPppLcpConfigTable": accPppLcpConfigTable,
       "accPppLcpConfigEntry": accPppLcpConfigEntry,
       "accPppLcpConfigIndex": accPppLcpConfigIndex,
       "accPppLcpConfigInitialMRU": accPppLcpConfigInitialMRU,
       "accPppLcpConfigReceiveACCMap": accPppLcpConfigReceiveACCMap,
       "accPppLinkConfigXmitACCMap": accPppLinkConfigXmitACCMap,
       "accPppLcpConfigMagicNumber": accPppLcpConfigMagicNumber,
       "accPppLcpConfig32BitFCS": accPppLcpConfig32BitFCS,
       "accPppLcpRestartTimer": accPppLcpRestartTimer,
       "accPppLcpMaxTerminate": accPppLcpMaxTerminate,
       "accPppLcpMaxConfigure": accPppLcpMaxConfigure,
       "accPppLcpMaxFailure": accPppLcpMaxFailure,
       "accPppLcpMonInterval": accPppLcpMonInterval,
       "accPppLcpMonEvents": accPppLcpMonEvents,
       "accPppLcpMonThreshold": accPppLcpMonThreshold,
       "accPppLcpAdminStatus": accPppLcpAdminStatus,
       "accPppLinkMsgLevel": accPppLinkMsgLevel,
       "accPppLqrTable": accPppLqrTable,
       "accPppLqrEntry": accPppLqrEntry,
       "accPppLqrIndex": accPppLqrIndex,
       "accPppLqrQuality": accPppLqrQuality,
       "accPppLqrInGoodOctets": accPppLqrInGoodOctets,
       "accPppLqrLocalPeriod": accPppLqrLocalPeriod,
       "accPppLqrRemotePeriod": accPppLqrRemotePeriod,
       "accPppLqrOutLQRs": accPppLqrOutLQRs,
       "accPppLqrInLQRs": accPppLqrInLQRs,
       "accPppLqrConfigTable": accPppLqrConfigTable,
       "accPppLqrConfigEntry": accPppLqrConfigEntry,
       "accPppLqrConfigIndex": accPppLqrConfigIndex,
       "accPppLqrConfigPeriod": accPppLqrConfigPeriod,
       "accPppLqrConfigStatus": accPppLqrConfigStatus,
       "accPppIpcpTable": accPppIpcpTable,
       "accPppIpcpEntry": accPppIpcpEntry,
       "accPppIpcpIndex": accPppIpcpIndex,
       "accPppIpcpLocalToRemoteCompressionProtocol": accPppIpcpLocalToRemoteCompressionProtocol,
       "accPppIpcpRemoteToLocalCompressionProtocol": accPppIpcpRemoteToLocalCompressionProtocol,
       "accPppIpcpRemoteMaxSlotId": accPppIpcpRemoteMaxSlotId,
       "accPppIpcpLocalMaxSlotId": accPppIpcpLocalMaxSlotId,
       "accPppIpOperStatus": accPppIpOperStatus,
       "accPppIpcpConfigTable": accPppIpcpConfigTable,
       "accPppIpcpConfigEntry": accPppIpcpConfigEntry,
       "accPppIpcpConfigIndex": accPppIpcpConfigIndex,
       "accPppIpcpConfigCompression": accPppIpcpConfigCompression,
       "accPppIpcpConfigStatus": accPppIpcpConfigStatus,
       "accPppBncpTable": accPppBncpTable,
       "accPppBncpEntry": accPppBncpEntry,
       "accPppBncpIndex": accPppBncpIndex,
       "accPppBncpLocalToRemoteTinygramCompression": accPppBncpLocalToRemoteTinygramCompression,
       "accPppBncpRemoteToLocalTinygramCompression": accPppBncpRemoteToLocalTinygramCompression,
       "accPppBncpLocalToRemoteLanId": accPppBncpLocalToRemoteLanId,
       "accPppBncpRemoteToLocalLanId": accPppBncpRemoteToLocalLanId,
       "accPppBncpOperStatus": accPppBncpOperStatus,
       "accPppBncpConfigTable": accPppBncpConfigTable,
       "accPppBncpConfigEntry": accPppBncpConfigEntry,
       "accPppBncpConfigIndex": accPppBncpConfigIndex,
       "accPppBncpConfigTinygram": accPppBncpConfigTinygram,
       "accPppBncpConfigRingId": accPppBncpConfigRingId,
       "accPppBncpConfigLineId": accPppBncpConfigLineId,
       "accPppBncpConfigLanId": accPppBncpConfigLanId,
       "accPppBncpConfigAdminStatus": accPppBncpConfigAdminStatus,
       "accPppXnsTable": accPppXnsTable,
       "accPppXnsEntry": accPppXnsEntry,
       "accPppXnsIndex": accPppXnsIndex,
       "accPppXnsOperStatus": accPppXnsOperStatus,
       "accPppXnsConfigTable": accPppXnsConfigTable,
       "accPppXnsConfigEntry": accPppXnsConfigEntry,
       "accPppXnsConfigIndex": accPppXnsConfigIndex,
       "accPppXnsConfigAdminStatus": accPppXnsConfigAdminStatus,
       "accPppIpxTable": accPppIpxTable,
       "accPppIpxEntry": accPppIpxEntry,
       "accPppIpxIndex": accPppIpxIndex,
       "accPppIpxOperStatus": accPppIpxOperStatus,
       "accPppIpxConfigTable": accPppIpxConfigTable,
       "accPppIpxConfigEntry": accPppIpxConfigEntry,
       "accPppIpxConfigIndex": accPppIpxConfigIndex,
       "accPppIpxConfigAdminStatus": accPppIpxConfigAdminStatus,
       "accPppAppleTable": accPppAppleTable,
       "accPppAppleEntry": accPppAppleEntry,
       "accPppAppleIndex": accPppAppleIndex,
       "accPppAppleOperStatus": accPppAppleOperStatus,
       "accPppAppleConfigTable": accPppAppleConfigTable,
       "accPppAppleConfigEntry": accPppAppleConfigEntry,
       "accPppAppleConfigIndex": accPppAppleConfigIndex,
       "accPppAppleConfigAdminStatus": accPppAppleConfigAdminStatus,
       "accPppDecTable": accPppDecTable,
       "accPppDecEntry": accPppDecEntry,
       "accPppDecIndex": accPppDecIndex,
       "accPppDecOperStatus": accPppDecOperStatus,
       "accPppDecConfigTable": accPppDecConfigTable,
       "accPppDecConfigEntry": accPppDecConfigEntry,
       "accPppDecConfigIndex": accPppDecConfigIndex,
       "accPppDecConfigAdminStatus": accPppDecConfigAdminStatus,
       "accPppProtocolTable": accPppProtocolTable,
       "accPppProtocolEntry": accPppProtocolEntry,
       "accPppProtocolIndex": accPppProtocolIndex,
       "accPppProtocolProtocol": accPppProtocolProtocol,
       "accPppProtocolAdminStatus": accPppProtocolAdminStatus,
       "accPppProtocolOperStatus": accPppProtocolOperStatus,
       "accPppMsg": accPppMsg,
       "accPppMsgLevel": accPppMsgLevel,
       "accPppAuthStatTable": accPppAuthStatTable,
       "accPppAuthStatEntry": accPppAuthStatEntry,
       "accPppAuthStatIndex": accPppAuthStatIndex,
       "accPppAuthStatPapReqSents": accPppAuthStatPapReqSents,
       "accPppAuthStatPapReqRcvs": accPppAuthStatPapReqRcvs,
       "accPppAuthStatPapAckSents": accPppAuthStatPapAckSents,
       "accPppAuthStatPapAckRcvs": accPppAuthStatPapAckRcvs,
       "accPppAuthStatPapNakSents": accPppAuthStatPapNakSents,
       "accPppAuthStatPapNakRcvs": accPppAuthStatPapNakRcvs,
       "accPppAuthStatPapRetryTimeouts": accPppAuthStatPapRetryTimeouts,
       "accPppAuthStatChapChallengeSents": accPppAuthStatChapChallengeSents,
       "accPppAuthStatChapChallengeRcvs": accPppAuthStatChapChallengeRcvs,
       "accPppAuthStatChapResponseSents": accPppAuthStatChapResponseSents,
       "accPppAuthStatChapResponseRcvs": accPppAuthStatChapResponseRcvs,
       "accPppAuthStatChapAckSents": accPppAuthStatChapAckSents,
       "accPppAuthStatChapAckRcvs": accPppAuthStatChapAckRcvs,
       "accPppAuthStatChapNakSents": accPppAuthStatChapNakSents,
       "accPppAuthStatChapNakRcvs": accPppAuthStatChapNakRcvs,
       "accPppAuthStatChapResponseTimeouts": accPppAuthStatChapResponseTimeouts,
       "accPppAuthStatChapChallengeTimeouts": accPppAuthStatChapChallengeTimeouts,
       "accPppAuthStatChapAckNakTimeouts": accPppAuthStatChapAckNakTimeouts,
       "accPppAuthStatLastNegoOptions": accPppAuthStatLastNegoOptions,
       "accPppAuthStatOutgoingCallMisMatchs": accPppAuthStatOutgoingCallMisMatchs,
       "accPppAuthParmTable": accPppAuthParmTable,
       "accPppAuthParmEntry": accPppAuthParmEntry,
       "accPppAuthParmIndex": accPppAuthParmIndex,
       "accPppAuthParmUserNameIn": accPppAuthParmUserNameIn,
       "accPppAuthParmPasswordIn": accPppAuthParmPasswordIn,
       "accPppAuthParmMethodIn": accPppAuthParmMethodIn,
       "accPppAuthParmUserNameOut": accPppAuthParmUserNameOut,
       "accPppAuthParmPasswordOut": accPppAuthParmPasswordOut,
       "accPppAuthParmMethodOut": accPppAuthParmMethodOut,
       "accPppAuthParmRetryInterval": accPppAuthParmRetryInterval,
       "accPppAuthParmRetryCount": accPppAuthParmRetryCount,
       "accPppAuthParmAcctOption": accPppAuthParmAcctOption,
       "accPppCompressTable": accPppCompressTable,
       "accPppCompressEntry": accPppCompressEntry,
       "accPppCompressIndex": accPppCompressIndex,
       "accPppCompressMsgLevel": accPppCompressMsgLevel,
       "accPppCompressMethod": accPppCompressMethod,
       "accPppCompressStream": accPppCompressStream,
       "accPppCompressNegoMethodIn": accPppCompressNegoMethodIn,
       "accPppCompressNegoMethodOut": accPppCompressNegoMethodOut,
       "accPppCompressNegoStreamIn": accPppCompressNegoStreamIn,
       "accPppCompressNegoStreamOut": accPppCompressNegoStreamOut,
       "accPppCompressStatTable": accPppCompressStatTable,
       "accPppCompressStatEntry": accPppCompressStatEntry,
       "accPppCompressStatIndex": accPppCompressStatIndex,
       "accPppCompressStatStatusIn": accPppCompressStatStatusIn,
       "accPppCompressStatStatusOut": accPppCompressStatStatusOut,
       "accPppCompressStatAvgCompIn": accPppCompressStatAvgCompIn,
       "accPppCompressStatAvgCompOut": accPppCompressStatAvgCompOut,
       "accPppCompressStatInOctets": accPppCompressStatInOctets,
       "accPppCompressStatOutOctets": accPppCompressStatOutOctets,
       "accPppCompressStatInPackets": accPppCompressStatInPackets,
       "accPppCompressStatOutPackets": accPppCompressStatOutPackets,
       "accPppCompressUnCompInStats": accPppCompressUnCompInStats,
       "accPppCompressUnCompOutStats": accPppCompressUnCompOutStats,
       "accPppCompressStatHdrErrors": accPppCompressStatHdrErrors,
       "accPppCompressStatResyncs": accPppCompressStatResyncs,
       "accPppCompressStatNoEndMarks": accPppCompressStatNoEndMarks,
       "accPppCompressStatNoAvailBufs": accPppCompressStatNoAvailBufs,
       "accPppCompressStatRcvResetReqs": accPppCompressStatRcvResetReqs,
       "accPppCompressStatRcvResetAcks": accPppCompressStatRcvResetAcks,
       "accPppCompressStatSndResetReqs": accPppCompressStatSndResetReqs,
       "accPppCompressStatSndResetAcks": accPppCompressStatSndResetAcks,
       "accPppCompressStatExpandIn": accPppCompressStatExpandIn,
       "accPppCompressStatExpandOut": accPppCompressStatExpandOut,
       "accPppCompressStatDiscardIn": accPppCompressStatDiscardIn,
       "accPppCompressStatDiscardOut": accPppCompressStatDiscardOut,
       "accIpHeaderCompStatTable": accIpHeaderCompStatTable,
       "accIpHeaderCompStatEntry": accIpHeaderCompStatEntry,
       "accPppLinkVjhcStatIndex": accPppLinkVjhcStatIndex,
       "accPppLinkVjhcOper": accPppLinkVjhcOper,
       "accPppLinkVjhcNegot": accPppLinkVjhcNegot,
       "accPppLinkVjhcCompIn": accPppLinkVjhcCompIn,
       "accPppLinkVjhcUnCompIn": accPppLinkVjhcUnCompIn,
       "accPppLinkVjhcErrIn": accPppLinkVjhcErrIn,
       "accPppLinkVjhcCompOut": accPppLinkVjhcCompOut,
       "accPppLinkVjhcUnCompOut": accPppLinkVjhcUnCompOut,
       "accPppLinkVjhcErrOut": accPppLinkVjhcErrOut,
       "accPppTraps": accPppTraps,
       "accPppUnIdentifiedSourceTrap1": accPppUnIdentifiedSourceTrap1,
       "accPppLoopBackTrap2": accPppLoopBackTrap2,
       "accPppCallBackTrap3": accPppCallBackTrap3,
       "accPppTrapMsg": accPppTrapMsg}
)
