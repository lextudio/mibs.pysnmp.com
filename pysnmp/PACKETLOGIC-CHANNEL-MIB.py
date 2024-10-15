# SNMP MIB module (PACKETLOGIC-CHANNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETLOGIC-CHANNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:07 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(packetlogic2,) = mibBuilder.importSymbols(
    "PACKETLOGIC-MIB",
    "packetlogic2")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

channelstats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2)
)
channelstats.setRevisions(
        ("2012-09-26 12:48",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChannelCfg_ObjectIdentity = ObjectIdentity
channelCfg = _ChannelCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 8)
)
_ChannelNumber_Type = Unsigned32
_ChannelNumber_Object = MibScalar
channelNumber = _ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 8, 1),
    _ChannelNumber_Type()
)
channelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNumber.setStatus("current")
_ChannelInfoTable_Object = MibTable
channelInfoTable = _ChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17)
)
if mibBuilder.loadTexts:
    channelInfoTable.setStatus("current")
_ChannelInfoEntry_Object = MibTableRow
channelInfoEntry = _ChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1)
)
channelInfoEntry.setIndexNames(
    (0, "PACKETLOGIC-CHANNEL-MIB", "channelInfoEntryIndex"),
)
if mibBuilder.loadTexts:
    channelInfoEntry.setStatus("current")


class _ChannelInternalMedia_Type(Integer32):
    """Custom type channelInternalMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("fd-10", 2),
          ("fd-100", 4),
          ("fd-1000", 5),
          ("fd-10000", 6),
          ("hd-10", 1),
          ("hd-100", 3))
    )


_ChannelInternalMedia_Type.__name__ = "Integer32"
_ChannelInternalMedia_Object = MibTableColumn
channelInternalMedia = _ChannelInternalMedia_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 1),
    _ChannelInternalMedia_Type()
)
channelInternalMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalMedia.setStatus("current")


class _ChannelExternalMedia_Type(Integer32):
    """Custom type channelExternalMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("fd-10", 2),
          ("fd-100", 4),
          ("fd-1000", 5),
          ("fd-10000", 6),
          ("hd-10", 1),
          ("hd-100", 3))
    )


_ChannelExternalMedia_Type.__name__ = "Integer32"
_ChannelExternalMedia_Object = MibTableColumn
channelExternalMedia = _ChannelExternalMedia_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 2),
    _ChannelExternalMedia_Type()
)
channelExternalMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalMedia.setStatus("current")


class _ChannelInternalNegotiatedMedia_Type(Integer32):
    """Custom type channelInternalNegotiatedMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fd10", 2),
          ("fd100", 4),
          ("fd1000", 5),
          ("fd10000", 6),
          ("hd10", 1),
          ("hd100", 3),
          ("linkdown", 0))
    )


_ChannelInternalNegotiatedMedia_Type.__name__ = "Integer32"
_ChannelInternalNegotiatedMedia_Object = MibTableColumn
channelInternalNegotiatedMedia = _ChannelInternalNegotiatedMedia_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 3),
    _ChannelInternalNegotiatedMedia_Type()
)
channelInternalNegotiatedMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalNegotiatedMedia.setStatus("current")


class _ChannelExternalNegotiatedMedia_Type(Integer32):
    """Custom type channelExternalNegotiatedMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fd10", 2),
          ("fd100", 4),
          ("fd1000", 5),
          ("fd10000", 6),
          ("hd10", 1),
          ("hd100", 3),
          ("linkdown", 0))
    )


_ChannelExternalNegotiatedMedia_Type.__name__ = "Integer32"
_ChannelExternalNegotiatedMedia_Object = MibTableColumn
channelExternalNegotiatedMedia = _ChannelExternalNegotiatedMedia_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 4),
    _ChannelExternalNegotiatedMedia_Type()
)
channelExternalNegotiatedMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalNegotiatedMedia.setStatus("current")


class _ChannelActive_Type(Integer32):
    """Custom type channelActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_ChannelActive_Type.__name__ = "Integer32"
_ChannelActive_Object = MibTableColumn
channelActive = _ChannelActive_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 5),
    _ChannelActive_Type()
)
channelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelActive.setStatus("current")
_ChannelName_Type = DisplayString
_ChannelName_Object = MibTableColumn
channelName = _ChannelName_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 6),
    _ChannelName_Type()
)
channelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelName.setStatus("current")
_ChannelInternalNegotiatedMediaTime_Type = Unsigned32
_ChannelInternalNegotiatedMediaTime_Object = MibTableColumn
channelInternalNegotiatedMediaTime = _ChannelInternalNegotiatedMediaTime_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 7),
    _ChannelInternalNegotiatedMediaTime_Type()
)
channelInternalNegotiatedMediaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalNegotiatedMediaTime.setStatus("current")
_ChannelexternalNegotiatedMediaTime_Type = Unsigned32
_ChannelexternalNegotiatedMediaTime_Object = MibTableColumn
channelexternalNegotiatedMediaTime = _ChannelexternalNegotiatedMediaTime_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 8),
    _ChannelexternalNegotiatedMediaTime_Type()
)
channelexternalNegotiatedMediaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelexternalNegotiatedMediaTime.setStatus("current")


class _ChannelInfoEntryIndex_Type(Integer32):
    """Custom type channelInfoEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ChannelInfoEntryIndex_Type.__name__ = "Integer32"
_ChannelInfoEntryIndex_Object = MibTableColumn
channelInfoEntryIndex = _ChannelInfoEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 999),
    _ChannelInfoEntryIndex_Type()
)
channelInfoEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelInfoEntryIndex.setStatus("current")
_NetDeviceTable_Object = MibTable
netDeviceTable = _NetDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25)
)
if mibBuilder.loadTexts:
    netDeviceTable.setStatus("current")
_NetDeviceEntry_Object = MibTableRow
netDeviceEntry = _NetDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1)
)
netDeviceEntry.setIndexNames(
    (0, "PACKETLOGIC-CHANNEL-MIB", "netDeviceEntryIndex"),
)
if mibBuilder.loadTexts:
    netDeviceEntry.setStatus("current")
_ChannelRxPackets_ObjectIdentity = ObjectIdentity
channelRxPackets = _ChannelRxPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1)
)
_ChannelInternalRxPackets_Type = Counter64
_ChannelInternalRxPackets_Object = MibScalar
channelInternalRxPackets = _ChannelInternalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1, 1),
    _ChannelInternalRxPackets_Type()
)
channelInternalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalRxPackets.setStatus("current")
_ChannelExternalRxPackets_Type = Counter64
_ChannelExternalRxPackets_Object = MibScalar
channelExternalRxPackets = _ChannelExternalRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1, 2),
    _ChannelExternalRxPackets_Type()
)
channelExternalRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalRxPackets.setStatus("current")
_ChannelTxPackets_ObjectIdentity = ObjectIdentity
channelTxPackets = _ChannelTxPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2)
)
_ChannelInternalTxPackets_Type = Counter64
_ChannelInternalTxPackets_Object = MibScalar
channelInternalTxPackets = _ChannelInternalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2, 1),
    _ChannelInternalTxPackets_Type()
)
channelInternalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalTxPackets.setStatus("current")
_ChannelExternalTxPackets_Type = Counter64
_ChannelExternalTxPackets_Object = MibScalar
channelExternalTxPackets = _ChannelExternalTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2, 2),
    _ChannelExternalTxPackets_Type()
)
channelExternalTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalTxPackets.setStatus("current")
_ChannelRxBytes_ObjectIdentity = ObjectIdentity
channelRxBytes = _ChannelRxBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3)
)
_ChannelInternalRxBytes_Type = Counter64
_ChannelInternalRxBytes_Object = MibScalar
channelInternalRxBytes = _ChannelInternalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3, 1),
    _ChannelInternalRxBytes_Type()
)
channelInternalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalRxBytes.setStatus("current")
_ChannelExternalRxBytes_Type = Counter64
_ChannelExternalRxBytes_Object = MibScalar
channelExternalRxBytes = _ChannelExternalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3, 2),
    _ChannelExternalRxBytes_Type()
)
channelExternalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalRxBytes.setStatus("current")
_ChannelTxBytes_ObjectIdentity = ObjectIdentity
channelTxBytes = _ChannelTxBytes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4)
)
_ChannelInternalTxBytes_Type = Counter64
_ChannelInternalTxBytes_Object = MibScalar
channelInternalTxBytes = _ChannelInternalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4, 1),
    _ChannelInternalTxBytes_Type()
)
channelInternalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalTxBytes.setStatus("current")
_ChannelExternalTxBytes_Type = Counter64
_ChannelExternalTxBytes_Object = MibScalar
channelExternalTxBytes = _ChannelExternalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4, 2),
    _ChannelExternalTxBytes_Type()
)
channelExternalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalTxBytes.setStatus("current")
_ChannelRxErrors_ObjectIdentity = ObjectIdentity
channelRxErrors = _ChannelRxErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5)
)
_ChannelInternalRxErrors_Type = Counter64
_ChannelInternalRxErrors_Object = MibScalar
channelInternalRxErrors = _ChannelInternalRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5, 1),
    _ChannelInternalRxErrors_Type()
)
channelInternalRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalRxErrors.setStatus("current")
_ChannelExternalRxErrors_Type = Counter64
_ChannelExternalRxErrors_Object = MibScalar
channelExternalRxErrors = _ChannelExternalRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5, 2),
    _ChannelExternalRxErrors_Type()
)
channelExternalRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalRxErrors.setStatus("current")
_ChannelTxErrors_ObjectIdentity = ObjectIdentity
channelTxErrors = _ChannelTxErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6)
)
_ChannelInternalTxErrors_Type = Counter64
_ChannelInternalTxErrors_Object = MibScalar
channelInternalTxErrors = _ChannelInternalTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6, 1),
    _ChannelInternalTxErrors_Type()
)
channelInternalTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalTxErrors.setStatus("current")
_ChannelExternalTxErrors_Type = Counter64
_ChannelExternalTxErrors_Object = MibScalar
channelExternalTxErrors = _ChannelExternalTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6, 2),
    _ChannelExternalTxErrors_Type()
)
channelExternalTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalTxErrors.setStatus("current")
_ChannelRxDrops_ObjectIdentity = ObjectIdentity
channelRxDrops = _ChannelRxDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7)
)
_ChannelInternalRxDrops_Type = Counter64
_ChannelInternalRxDrops_Object = MibScalar
channelInternalRxDrops = _ChannelInternalRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7, 1),
    _ChannelInternalRxDrops_Type()
)
channelInternalRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalRxDrops.setStatus("current")
_ChannelExternalRxDrops_Type = Counter64
_ChannelExternalRxDrops_Object = MibScalar
channelExternalRxDrops = _ChannelExternalRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7, 2),
    _ChannelExternalRxDrops_Type()
)
channelExternalRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalRxDrops.setStatus("current")
_ChannelTxDrops_ObjectIdentity = ObjectIdentity
channelTxDrops = _ChannelTxDrops_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8)
)
_ChannelInternalTxDrops_Type = Counter64
_ChannelInternalTxDrops_Object = MibScalar
channelInternalTxDrops = _ChannelInternalTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8, 1),
    _ChannelInternalTxDrops_Type()
)
channelInternalTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalTxDrops.setStatus("current")
_ChannelExternalTxDrops_Type = Counter64
_ChannelExternalTxDrops_Object = MibScalar
channelExternalTxDrops = _ChannelExternalTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8, 2),
    _ChannelExternalTxDrops_Type()
)
channelExternalTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalTxDrops.setStatus("current")
_ChannelCollisions_ObjectIdentity = ObjectIdentity
channelCollisions = _ChannelCollisions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9)
)
_ChannelInternalCollisions_Type = Counter64
_ChannelInternalCollisions_Object = MibScalar
channelInternalCollisions = _ChannelInternalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9, 1),
    _ChannelInternalCollisions_Type()
)
channelInternalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalCollisions.setStatus("current")
_ChannelExternalCollisions_Type = Counter64
_ChannelExternalCollisions_Object = MibScalar
channelExternalCollisions = _ChannelExternalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9, 2),
    _ChannelExternalCollisions_Type()
)
channelExternalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalCollisions.setStatus("current")
_ChannelMulticast_ObjectIdentity = ObjectIdentity
channelMulticast = _ChannelMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10)
)
_ChannelInternalMulticast_Type = Counter64
_ChannelInternalMulticast_Object = MibScalar
channelInternalMulticast = _ChannelInternalMulticast_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10, 1),
    _ChannelInternalMulticast_Type()
)
channelInternalMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalMulticast.setStatus("current")
_ChannelExternalMulticast_Type = Counter64
_ChannelExternalMulticast_Object = MibScalar
channelExternalMulticast = _ChannelExternalMulticast_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10, 2),
    _ChannelExternalMulticast_Type()
)
channelExternalMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalMulticast.setStatus("current")
_ChannelRxLengthErrors_ObjectIdentity = ObjectIdentity
channelRxLengthErrors = _ChannelRxLengthErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11)
)
_ChannelInternalRxLengthErrors_Type = Counter64
_ChannelInternalRxLengthErrors_Object = MibScalar
channelInternalRxLengthErrors = _ChannelInternalRxLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11, 1),
    _ChannelInternalRxLengthErrors_Type()
)
channelInternalRxLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalRxLengthErrors.setStatus("current")
_ChannelExternalRxLengthErrors_Type = Counter64
_ChannelExternalRxLengthErrors_Object = MibScalar
channelExternalRxLengthErrors = _ChannelExternalRxLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11, 2),
    _ChannelExternalRxLengthErrors_Type()
)
channelExternalRxLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalRxLengthErrors.setStatus("current")
_ChannelRxCrcErrors_ObjectIdentity = ObjectIdentity
channelRxCrcErrors = _ChannelRxCrcErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12)
)
_ChannelInternalRxCrcErrors_Type = Counter64
_ChannelInternalRxCrcErrors_Object = MibScalar
channelInternalRxCrcErrors = _ChannelInternalRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12, 1),
    _ChannelInternalRxCrcErrors_Type()
)
channelInternalRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalRxCrcErrors.setStatus("current")
_ChannelExternalRxCrcErrors_Type = Counter64
_ChannelExternalRxCrcErrors_Object = MibScalar
channelExternalRxCrcErrors = _ChannelExternalRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12, 2),
    _ChannelExternalRxCrcErrors_Type()
)
channelExternalRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalRxCrcErrors.setStatus("current")
_ChannelRxFrameErrors_ObjectIdentity = ObjectIdentity
channelRxFrameErrors = _ChannelRxFrameErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13)
)
_ChannelInternalRxFrameErrors_Type = Counter64
_ChannelInternalRxFrameErrors_Object = MibScalar
channelInternalRxFrameErrors = _ChannelInternalRxFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13, 1),
    _ChannelInternalRxFrameErrors_Type()
)
channelInternalRxFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalRxFrameErrors.setStatus("current")
_ChannelExternalRxFrameErrors_Type = Counter64
_ChannelExternalRxFrameErrors_Object = MibScalar
channelExternalRxFrameErrors = _ChannelExternalRxFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13, 2),
    _ChannelExternalRxFrameErrors_Type()
)
channelExternalRxFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalRxFrameErrors.setStatus("current")
_ChannelRxFifoErrors_ObjectIdentity = ObjectIdentity
channelRxFifoErrors = _ChannelRxFifoErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14)
)
_ChannelINternalRxFifoErrors_Type = Counter64
_ChannelINternalRxFifoErrors_Object = MibScalar
channelINternalRxFifoErrors = _ChannelINternalRxFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14, 1),
    _ChannelINternalRxFifoErrors_Type()
)
channelINternalRxFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelINternalRxFifoErrors.setStatus("current")
_ChannelExternalRxFifoErrors_Type = Counter64
_ChannelExternalRxFifoErrors_Object = MibScalar
channelExternalRxFifoErrors = _ChannelExternalRxFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14, 2),
    _ChannelExternalRxFifoErrors_Type()
)
channelExternalRxFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalRxFifoErrors.setStatus("current")
_ChannelRxMissedErrors_ObjectIdentity = ObjectIdentity
channelRxMissedErrors = _ChannelRxMissedErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15)
)
_ChannelInternalRxMissedErrors_Type = Counter64
_ChannelInternalRxMissedErrors_Object = MibScalar
channelInternalRxMissedErrors = _ChannelInternalRxMissedErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15, 1),
    _ChannelInternalRxMissedErrors_Type()
)
channelInternalRxMissedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalRxMissedErrors.setStatus("current")
_ChannelExternalRxMissedErrors_Type = Counter64
_ChannelExternalRxMissedErrors_Object = MibScalar
channelExternalRxMissedErrors = _ChannelExternalRxMissedErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15, 2),
    _ChannelExternalRxMissedErrors_Type()
)
channelExternalRxMissedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalRxMissedErrors.setStatus("current")
_ChannelTxAborted_ObjectIdentity = ObjectIdentity
channelTxAborted = _ChannelTxAborted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16)
)
_ChannelInternalTxAborted_Type = Counter64
_ChannelInternalTxAborted_Object = MibScalar
channelInternalTxAborted = _ChannelInternalTxAborted_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16, 1),
    _ChannelInternalTxAborted_Type()
)
channelInternalTxAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalTxAborted.setStatus("current")
_ChannelExternalTxAborted_Type = Counter64
_ChannelExternalTxAborted_Object = MibScalar
channelExternalTxAborted = _ChannelExternalTxAborted_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16, 2),
    _ChannelExternalTxAborted_Type()
)
channelExternalTxAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalTxAborted.setStatus("current")
_ChannelTxWindowErrors_ObjectIdentity = ObjectIdentity
channelTxWindowErrors = _ChannelTxWindowErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17)
)
_ChannelInternalTxWindowErrors_Type = Counter64
_ChannelInternalTxWindowErrors_Object = MibScalar
channelInternalTxWindowErrors = _ChannelInternalTxWindowErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17, 1),
    _ChannelInternalTxWindowErrors_Type()
)
channelInternalTxWindowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalTxWindowErrors.setStatus("current")
_ChannelExternalTxWindowErrors_Type = Counter64
_ChannelExternalTxWindowErrors_Object = MibScalar
channelExternalTxWindowErrors = _ChannelExternalTxWindowErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17, 2),
    _ChannelExternalTxWindowErrors_Type()
)
channelExternalTxWindowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalTxWindowErrors.setStatus("current")
_ChannelTxCarrierErrors_ObjectIdentity = ObjectIdentity
channelTxCarrierErrors = _ChannelTxCarrierErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18)
)
_ChannelInternalTxCarrierErrors_Type = Counter64
_ChannelInternalTxCarrierErrors_Object = MibScalar
channelInternalTxCarrierErrors = _ChannelInternalTxCarrierErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18, 1),
    _ChannelInternalTxCarrierErrors_Type()
)
channelInternalTxCarrierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInternalTxCarrierErrors.setStatus("current")
_ChannelExternalTxCarrierErrors_Type = Counter64
_ChannelExternalTxCarrierErrors_Object = MibScalar
channelExternalTxCarrierErrors = _ChannelExternalTxCarrierErrors_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18, 2),
    _ChannelExternalTxCarrierErrors_Type()
)
channelExternalTxCarrierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelExternalTxCarrierErrors.setStatus("current")


class _NetDeviceEntryIndex_Type(Integer32):
    """Custom type netDeviceEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NetDeviceEntryIndex_Type.__name__ = "Integer32"
_NetDeviceEntryIndex_Object = MibTableColumn
netDeviceEntryIndex = _NetDeviceEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 999),
    _NetDeviceEntryIndex_Type()
)
netDeviceEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netDeviceEntryIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETLOGIC-CHANNEL-MIB",
    **{"channelstats": channelstats,
       "channelCfg": channelCfg,
       "channelNumber": channelNumber,
       "channelInfoTable": channelInfoTable,
       "channelInfoEntry": channelInfoEntry,
       "channelInternalMedia": channelInternalMedia,
       "channelExternalMedia": channelExternalMedia,
       "channelInternalNegotiatedMedia": channelInternalNegotiatedMedia,
       "channelExternalNegotiatedMedia": channelExternalNegotiatedMedia,
       "channelActive": channelActive,
       "channelName": channelName,
       "channelInternalNegotiatedMediaTime": channelInternalNegotiatedMediaTime,
       "channelexternalNegotiatedMediaTime": channelexternalNegotiatedMediaTime,
       "channelInfoEntryIndex": channelInfoEntryIndex,
       "netDeviceTable": netDeviceTable,
       "netDeviceEntry": netDeviceEntry,
       "channelRxPackets": channelRxPackets,
       "channelInternalRxPackets": channelInternalRxPackets,
       "channelExternalRxPackets": channelExternalRxPackets,
       "channelTxPackets": channelTxPackets,
       "channelInternalTxPackets": channelInternalTxPackets,
       "channelExternalTxPackets": channelExternalTxPackets,
       "channelRxBytes": channelRxBytes,
       "channelInternalRxBytes": channelInternalRxBytes,
       "channelExternalRxBytes": channelExternalRxBytes,
       "channelTxBytes": channelTxBytes,
       "channelInternalTxBytes": channelInternalTxBytes,
       "channelExternalTxBytes": channelExternalTxBytes,
       "channelRxErrors": channelRxErrors,
       "channelInternalRxErrors": channelInternalRxErrors,
       "channelExternalRxErrors": channelExternalRxErrors,
       "channelTxErrors": channelTxErrors,
       "channelInternalTxErrors": channelInternalTxErrors,
       "channelExternalTxErrors": channelExternalTxErrors,
       "channelRxDrops": channelRxDrops,
       "channelInternalRxDrops": channelInternalRxDrops,
       "channelExternalRxDrops": channelExternalRxDrops,
       "channelTxDrops": channelTxDrops,
       "channelInternalTxDrops": channelInternalTxDrops,
       "channelExternalTxDrops": channelExternalTxDrops,
       "channelCollisions": channelCollisions,
       "channelInternalCollisions": channelInternalCollisions,
       "channelExternalCollisions": channelExternalCollisions,
       "channelMulticast": channelMulticast,
       "channelInternalMulticast": channelInternalMulticast,
       "channelExternalMulticast": channelExternalMulticast,
       "channelRxLengthErrors": channelRxLengthErrors,
       "channelInternalRxLengthErrors": channelInternalRxLengthErrors,
       "channelExternalRxLengthErrors": channelExternalRxLengthErrors,
       "channelRxCrcErrors": channelRxCrcErrors,
       "channelInternalRxCrcErrors": channelInternalRxCrcErrors,
       "channelExternalRxCrcErrors": channelExternalRxCrcErrors,
       "channelRxFrameErrors": channelRxFrameErrors,
       "channelInternalRxFrameErrors": channelInternalRxFrameErrors,
       "channelExternalRxFrameErrors": channelExternalRxFrameErrors,
       "channelRxFifoErrors": channelRxFifoErrors,
       "channelINternalRxFifoErrors": channelINternalRxFifoErrors,
       "channelExternalRxFifoErrors": channelExternalRxFifoErrors,
       "channelRxMissedErrors": channelRxMissedErrors,
       "channelInternalRxMissedErrors": channelInternalRxMissedErrors,
       "channelExternalRxMissedErrors": channelExternalRxMissedErrors,
       "channelTxAborted": channelTxAborted,
       "channelInternalTxAborted": channelInternalTxAborted,
       "channelExternalTxAborted": channelExternalTxAborted,
       "channelTxWindowErrors": channelTxWindowErrors,
       "channelInternalTxWindowErrors": channelInternalTxWindowErrors,
       "channelExternalTxWindowErrors": channelExternalTxWindowErrors,
       "channelTxCarrierErrors": channelTxCarrierErrors,
       "channelInternalTxCarrierErrors": channelInternalTxCarrierErrors,
       "channelExternalTxCarrierErrors": channelExternalTxCarrierErrors,
       "netDeviceEntryIndex": netDeviceEntryIndex}
)
