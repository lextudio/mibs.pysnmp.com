# SNMP MIB module (BIANCA-BRICK-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:37 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboip_ObjectIdentity = ObjectIdentity
biboip = _Biboip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_Biboping_ObjectIdentity = ObjectIdentity
biboping = _Biboping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27)
)
_BiboPingTable_Object = MibTable
biboPingTable = _BiboPingTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1)
)
if mibBuilder.loadTexts:
    biboPingTable.setStatus("mandatory")
_BiboPingEntry_Object = MibTableRow
biboPingEntry = _BiboPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1)
)
biboPingEntry.setIndexNames(
    (0, "BIANCA-BRICK-PING-MIB", "biboPingIndex"),
)
if mibBuilder.loadTexts:
    biboPingEntry.setStatus("mandatory")


class _BiboPingIndex_Type(Integer32):
    """Custom type biboPingIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BiboPingIndex_Type.__name__ = "Integer32"
_BiboPingIndex_Object = MibTableColumn
biboPingIndex = _BiboPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 1),
    _BiboPingIndex_Type()
)
biboPingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPingIndex.setStatus("mandatory")


class _BiboPingStatus_Type(Integer32):
    """Custom type biboPingStatus based on Integer32"""
    defaultValue = 5

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
          ("createandgo", 4),
          ("createandwait", 5),
          ("delete", 6),
          ("notinservice", 2),
          ("notready", 3))
    )


_BiboPingStatus_Type.__name__ = "Integer32"
_BiboPingStatus_Object = MibTableColumn
biboPingStatus = _BiboPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 2),
    _BiboPingStatus_Type()
)
biboPingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPingStatus.setStatus("mandatory")


class _BiboPingCompleted_Type(Integer32):
    """Custom type biboPingCompleted based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_BiboPingCompleted_Type.__name__ = "Integer32"
_BiboPingCompleted_Object = MibTableColumn
biboPingCompleted = _BiboPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 3),
    _BiboPingCompleted_Type()
)
biboPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPingCompleted.setStatus("mandatory")
_BiboPingSourceAddress_Type = IpAddress
_BiboPingSourceAddress_Object = MibTableColumn
biboPingSourceAddress = _BiboPingSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 4),
    _BiboPingSourceAddress_Type()
)
biboPingSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPingSourceAddress.setStatus("mandatory")
_BiboPingAddress_Type = IpAddress
_BiboPingAddress_Object = MibTableColumn
biboPingAddress = _BiboPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 5),
    _BiboPingAddress_Type()
)
biboPingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPingAddress.setStatus("mandatory")


class _BiboPingPacketCount_Type(Integer32):
    """Custom type biboPingPacketCount based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BiboPingPacketCount_Type.__name__ = "Integer32"
_BiboPingPacketCount_Object = MibTableColumn
biboPingPacketCount = _BiboPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 6),
    _BiboPingPacketCount_Type()
)
biboPingPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPingPacketCount.setStatus("mandatory")


class _BiboPingPacketSize_Type(Integer32):
    """Custom type biboPingPacketSize based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 4096),
    )


_BiboPingPacketSize_Type.__name__ = "Integer32"
_BiboPingPacketSize_Object = MibTableColumn
biboPingPacketSize = _BiboPingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 7),
    _BiboPingPacketSize_Type()
)
biboPingPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPingPacketSize.setStatus("mandatory")


class _BiboPingPacketTimeout_Type(Integer32):
    """Custom type biboPingPacketTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BiboPingPacketTimeout_Type.__name__ = "Integer32"
_BiboPingPacketTimeout_Object = MibTableColumn
biboPingPacketTimeout = _BiboPingPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 8),
    _BiboPingPacketTimeout_Type()
)
biboPingPacketTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPingPacketTimeout.setStatus("mandatory")


class _BiboPingReceivedPackets_Type(Integer32):
    """Custom type biboPingReceivedPackets based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BiboPingReceivedPackets_Type.__name__ = "Integer32"
_BiboPingReceivedPackets_Object = MibTableColumn
biboPingReceivedPackets = _BiboPingReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 9),
    _BiboPingReceivedPackets_Type()
)
biboPingReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPingReceivedPackets.setStatus("mandatory")


class _BiboPingMinRoundTrip_Type(Integer32):
    """Custom type biboPingMinRoundTrip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BiboPingMinRoundTrip_Type.__name__ = "Integer32"
_BiboPingMinRoundTrip_Object = MibTableColumn
biboPingMinRoundTrip = _BiboPingMinRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 10),
    _BiboPingMinRoundTrip_Type()
)
biboPingMinRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPingMinRoundTrip.setStatus("mandatory")


class _BiboPingMaxRoundTrip_Type(Integer32):
    """Custom type biboPingMaxRoundTrip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BiboPingMaxRoundTrip_Type.__name__ = "Integer32"
_BiboPingMaxRoundTrip_Object = MibTableColumn
biboPingMaxRoundTrip = _BiboPingMaxRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 11),
    _BiboPingMaxRoundTrip_Type()
)
biboPingMaxRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPingMaxRoundTrip.setStatus("mandatory")


class _BiboPingAvgRoundTrip_Type(Integer32):
    """Custom type biboPingAvgRoundTrip based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BiboPingAvgRoundTrip_Type.__name__ = "Integer32"
_BiboPingAvgRoundTrip_Object = MibTableColumn
biboPingAvgRoundTrip = _BiboPingAvgRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 12),
    _BiboPingAvgRoundTrip_Type()
)
biboPingAvgRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboPingAvgRoundTrip.setStatus("mandatory")


class _BiboPingTTL_Type(Integer32):
    """Custom type biboPingTTL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BiboPingTTL_Type.__name__ = "Integer32"
_BiboPingTTL_Object = MibTableColumn
biboPingTTL = _BiboPingTTL_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 13),
    _BiboPingTTL_Type()
)
biboPingTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPingTTL.setStatus("mandatory")


class _BiboPingTOS_Type(Integer32):
    """Custom type biboPingTOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BiboPingTOS_Type.__name__ = "Integer32"
_BiboPingTOS_Object = MibTableColumn
biboPingTOS = _BiboPingTOS_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 27, 1, 1, 14),
    _BiboPingTOS_Type()
)
biboPingTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboPingTOS.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-PING-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "biboping": biboping,
       "biboPingTable": biboPingTable,
       "biboPingEntry": biboPingEntry,
       "biboPingIndex": biboPingIndex,
       "biboPingStatus": biboPingStatus,
       "biboPingCompleted": biboPingCompleted,
       "biboPingSourceAddress": biboPingSourceAddress,
       "biboPingAddress": biboPingAddress,
       "biboPingPacketCount": biboPingPacketCount,
       "biboPingPacketSize": biboPingPacketSize,
       "biboPingPacketTimeout": biboPingPacketTimeout,
       "biboPingReceivedPackets": biboPingReceivedPackets,
       "biboPingMinRoundTrip": biboPingMinRoundTrip,
       "biboPingMaxRoundTrip": biboPingMaxRoundTrip,
       "biboPingAvgRoundTrip": biboPingAvgRoundTrip,
       "biboPingTTL": biboPingTTL,
       "biboPingTOS": biboPingTOS}
)
