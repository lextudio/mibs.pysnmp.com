# SNMP MIB module (PPP-LCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PPP-LCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:00 2024
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23)
)
_PppLcp_ObjectIdentity = ObjectIdentity
pppLcp = _PppLcp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 1)
)
_PppLink_ObjectIdentity = ObjectIdentity
pppLink = _PppLink_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1)
)
_PppLinkStatusTable_Object = MibTable
pppLinkStatusTable = _PppLinkStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pppLinkStatusTable.setStatus("mandatory")
_PppLinkStatusEntry_Object = MibTableRow
pppLinkStatusEntry = _PppLinkStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1)
)
pppLinkStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppLinkStatusEntry.setStatus("mandatory")


class _PppLinkStatusPhysicalIndex_Type(Integer32):
    """Custom type pppLinkStatusPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppLinkStatusPhysicalIndex_Type.__name__ = "Integer32"
_PppLinkStatusPhysicalIndex_Object = MibTableColumn
pppLinkStatusPhysicalIndex = _PppLinkStatusPhysicalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 1),
    _PppLinkStatusPhysicalIndex_Type()
)
pppLinkStatusPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusPhysicalIndex.setStatus("mandatory")
_PppLinkStatusBadAddresses_Type = Counter32
_PppLinkStatusBadAddresses_Object = MibTableColumn
pppLinkStatusBadAddresses = _PppLinkStatusBadAddresses_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 2),
    _PppLinkStatusBadAddresses_Type()
)
pppLinkStatusBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusBadAddresses.setStatus("mandatory")
_PppLinkStatusBadControls_Type = Counter32
_PppLinkStatusBadControls_Object = MibTableColumn
pppLinkStatusBadControls = _PppLinkStatusBadControls_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 3),
    _PppLinkStatusBadControls_Type()
)
pppLinkStatusBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusBadControls.setStatus("mandatory")
_PppLinkStatusPacketTooLongs_Type = Counter32
_PppLinkStatusPacketTooLongs_Object = MibTableColumn
pppLinkStatusPacketTooLongs = _PppLinkStatusPacketTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 4),
    _PppLinkStatusPacketTooLongs_Type()
)
pppLinkStatusPacketTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusPacketTooLongs.setStatus("mandatory")
_PppLinkStatusBadFCSs_Type = Counter32
_PppLinkStatusBadFCSs_Object = MibTableColumn
pppLinkStatusBadFCSs = _PppLinkStatusBadFCSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 5),
    _PppLinkStatusBadFCSs_Type()
)
pppLinkStatusBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusBadFCSs.setStatus("mandatory")


class _PppLinkStatusLocalMRU_Type(Integer32):
    """Custom type pppLinkStatusLocalMRU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PppLinkStatusLocalMRU_Type.__name__ = "Integer32"
_PppLinkStatusLocalMRU_Object = MibTableColumn
pppLinkStatusLocalMRU = _PppLinkStatusLocalMRU_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 6),
    _PppLinkStatusLocalMRU_Type()
)
pppLinkStatusLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusLocalMRU.setStatus("mandatory")


class _PppLinkStatusRemoteMRU_Type(Integer32):
    """Custom type pppLinkStatusRemoteMRU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PppLinkStatusRemoteMRU_Type.__name__ = "Integer32"
_PppLinkStatusRemoteMRU_Object = MibTableColumn
pppLinkStatusRemoteMRU = _PppLinkStatusRemoteMRU_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 7),
    _PppLinkStatusRemoteMRU_Type()
)
pppLinkStatusRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusRemoteMRU.setStatus("mandatory")


class _PppLinkStatusLocalToPeerACCMap_Type(OctetString):
    """Custom type pppLinkStatusLocalToPeerACCMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PppLinkStatusLocalToPeerACCMap_Type.__name__ = "OctetString"
_PppLinkStatusLocalToPeerACCMap_Object = MibTableColumn
pppLinkStatusLocalToPeerACCMap = _PppLinkStatusLocalToPeerACCMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 8),
    _PppLinkStatusLocalToPeerACCMap_Type()
)
pppLinkStatusLocalToPeerACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusLocalToPeerACCMap.setStatus("mandatory")


class _PppLinkStatusPeerToLocalACCMap_Type(OctetString):
    """Custom type pppLinkStatusPeerToLocalACCMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PppLinkStatusPeerToLocalACCMap_Type.__name__ = "OctetString"
_PppLinkStatusPeerToLocalACCMap_Object = MibTableColumn
pppLinkStatusPeerToLocalACCMap = _PppLinkStatusPeerToLocalACCMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 9),
    _PppLinkStatusPeerToLocalACCMap_Type()
)
pppLinkStatusPeerToLocalACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusPeerToLocalACCMap.setStatus("mandatory")


class _PppLinkStatusLocalToRemoteProtocolCompression_Type(Integer32):
    """Custom type pppLinkStatusLocalToRemoteProtocolCompression based on Integer32"""
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


_PppLinkStatusLocalToRemoteProtocolCompression_Type.__name__ = "Integer32"
_PppLinkStatusLocalToRemoteProtocolCompression_Object = MibTableColumn
pppLinkStatusLocalToRemoteProtocolCompression = _PppLinkStatusLocalToRemoteProtocolCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 10),
    _PppLinkStatusLocalToRemoteProtocolCompression_Type()
)
pppLinkStatusLocalToRemoteProtocolCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusLocalToRemoteProtocolCompression.setStatus("mandatory")


class _PppLinkStatusRemoteToLocalProtocolCompression_Type(Integer32):
    """Custom type pppLinkStatusRemoteToLocalProtocolCompression based on Integer32"""
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


_PppLinkStatusRemoteToLocalProtocolCompression_Type.__name__ = "Integer32"
_PppLinkStatusRemoteToLocalProtocolCompression_Object = MibTableColumn
pppLinkStatusRemoteToLocalProtocolCompression = _PppLinkStatusRemoteToLocalProtocolCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 11),
    _PppLinkStatusRemoteToLocalProtocolCompression_Type()
)
pppLinkStatusRemoteToLocalProtocolCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusRemoteToLocalProtocolCompression.setStatus("mandatory")


class _PppLinkStatusLocalToRemoteACCompression_Type(Integer32):
    """Custom type pppLinkStatusLocalToRemoteACCompression based on Integer32"""
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


_PppLinkStatusLocalToRemoteACCompression_Type.__name__ = "Integer32"
_PppLinkStatusLocalToRemoteACCompression_Object = MibTableColumn
pppLinkStatusLocalToRemoteACCompression = _PppLinkStatusLocalToRemoteACCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 12),
    _PppLinkStatusLocalToRemoteACCompression_Type()
)
pppLinkStatusLocalToRemoteACCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusLocalToRemoteACCompression.setStatus("mandatory")


class _PppLinkStatusRemoteToLocalACCompression_Type(Integer32):
    """Custom type pppLinkStatusRemoteToLocalACCompression based on Integer32"""
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


_PppLinkStatusRemoteToLocalACCompression_Type.__name__ = "Integer32"
_PppLinkStatusRemoteToLocalACCompression_Object = MibTableColumn
pppLinkStatusRemoteToLocalACCompression = _PppLinkStatusRemoteToLocalACCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 13),
    _PppLinkStatusRemoteToLocalACCompression_Type()
)
pppLinkStatusRemoteToLocalACCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusRemoteToLocalACCompression.setStatus("mandatory")


class _PppLinkStatusTransmitFcsSize_Type(Integer32):
    """Custom type pppLinkStatusTransmitFcsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PppLinkStatusTransmitFcsSize_Type.__name__ = "Integer32"
_PppLinkStatusTransmitFcsSize_Object = MibTableColumn
pppLinkStatusTransmitFcsSize = _PppLinkStatusTransmitFcsSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 14),
    _PppLinkStatusTransmitFcsSize_Type()
)
pppLinkStatusTransmitFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusTransmitFcsSize.setStatus("mandatory")


class _PppLinkStatusReceiveFcsSize_Type(Integer32):
    """Custom type pppLinkStatusReceiveFcsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PppLinkStatusReceiveFcsSize_Type.__name__ = "Integer32"
_PppLinkStatusReceiveFcsSize_Object = MibTableColumn
pppLinkStatusReceiveFcsSize = _PppLinkStatusReceiveFcsSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 15),
    _PppLinkStatusReceiveFcsSize_Type()
)
pppLinkStatusReceiveFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusReceiveFcsSize.setStatus("mandatory")
_PppLinkConfigTable_Object = MibTable
pppLinkConfigTable = _PppLinkConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pppLinkConfigTable.setStatus("mandatory")
_PppLinkConfigEntry_Object = MibTableRow
pppLinkConfigEntry = _PppLinkConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1)
)
pppLinkConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppLinkConfigEntry.setStatus("mandatory")


class _PppLinkConfigInitialMRU_Type(Integer32):
    """Custom type pppLinkConfigInitialMRU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppLinkConfigInitialMRU_Type.__name__ = "Integer32"
_PppLinkConfigInitialMRU_Object = MibTableColumn
pppLinkConfigInitialMRU = _PppLinkConfigInitialMRU_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 1),
    _PppLinkConfigInitialMRU_Type()
)
pppLinkConfigInitialMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLinkConfigInitialMRU.setStatus("mandatory")


class _PppLinkConfigReceiveACCMap_Type(OctetString):
    """Custom type pppLinkConfigReceiveACCMap based on OctetString"""
    defaultHexValue = "ffffffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PppLinkConfigReceiveACCMap_Type.__name__ = "OctetString"
_PppLinkConfigReceiveACCMap_Object = MibTableColumn
pppLinkConfigReceiveACCMap = _PppLinkConfigReceiveACCMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 2),
    _PppLinkConfigReceiveACCMap_Type()
)
pppLinkConfigReceiveACCMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLinkConfigReceiveACCMap.setStatus("mandatory")


class _PppLinkConfigTransmitACCMap_Type(OctetString):
    """Custom type pppLinkConfigTransmitACCMap based on OctetString"""
    defaultHexValue = "ffffffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PppLinkConfigTransmitACCMap_Type.__name__ = "OctetString"
_PppLinkConfigTransmitACCMap_Object = MibTableColumn
pppLinkConfigTransmitACCMap = _PppLinkConfigTransmitACCMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 3),
    _PppLinkConfigTransmitACCMap_Type()
)
pppLinkConfigTransmitACCMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLinkConfigTransmitACCMap.setStatus("mandatory")


class _PppLinkConfigMagicNumber_Type(Integer32):
    """Custom type pppLinkConfigMagicNumber based on Integer32"""
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


_PppLinkConfigMagicNumber_Type.__name__ = "Integer32"
_PppLinkConfigMagicNumber_Object = MibTableColumn
pppLinkConfigMagicNumber = _PppLinkConfigMagicNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 4),
    _PppLinkConfigMagicNumber_Type()
)
pppLinkConfigMagicNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLinkConfigMagicNumber.setStatus("mandatory")


class _PppLinkConfigFcsSize_Type(Integer32):
    """Custom type pppLinkConfigFcsSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PppLinkConfigFcsSize_Type.__name__ = "Integer32"
_PppLinkConfigFcsSize_Object = MibTableColumn
pppLinkConfigFcsSize = _PppLinkConfigFcsSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 5),
    _PppLinkConfigFcsSize_Type()
)
pppLinkConfigFcsSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLinkConfigFcsSize.setStatus("mandatory")
_PppLqr_ObjectIdentity = ObjectIdentity
pppLqr = _PppLqr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2)
)
_PppLqrTable_Object = MibTable
pppLqrTable = _PppLqrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pppLqrTable.setStatus("mandatory")
_PppLqrEntry_Object = MibTableRow
pppLqrEntry = _PppLqrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1)
)
pppLqrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppLqrEntry.setStatus("mandatory")


class _PppLqrQuality_Type(Integer32):
    """Custom type pppLqrQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1),
          ("not-determined", 3))
    )


_PppLqrQuality_Type.__name__ = "Integer32"
_PppLqrQuality_Object = MibTableColumn
pppLqrQuality = _PppLqrQuality_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 1),
    _PppLqrQuality_Type()
)
pppLqrQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqrQuality.setStatus("mandatory")
_PppLqrInGoodOctets_Type = Counter32
_PppLqrInGoodOctets_Object = MibTableColumn
pppLqrInGoodOctets = _PppLqrInGoodOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 2),
    _PppLqrInGoodOctets_Type()
)
pppLqrInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqrInGoodOctets.setStatus("mandatory")


class _PppLqrLocalPeriod_Type(Integer32):
    """Custom type pppLqrLocalPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PppLqrLocalPeriod_Type.__name__ = "Integer32"
_PppLqrLocalPeriod_Object = MibTableColumn
pppLqrLocalPeriod = _PppLqrLocalPeriod_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 3),
    _PppLqrLocalPeriod_Type()
)
pppLqrLocalPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqrLocalPeriod.setStatus("mandatory")


class _PppLqrRemotePeriod_Type(Integer32):
    """Custom type pppLqrRemotePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PppLqrRemotePeriod_Type.__name__ = "Integer32"
_PppLqrRemotePeriod_Object = MibTableColumn
pppLqrRemotePeriod = _PppLqrRemotePeriod_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 4),
    _PppLqrRemotePeriod_Type()
)
pppLqrRemotePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqrRemotePeriod.setStatus("mandatory")
_PppLqrOutLQRs_Type = Counter32
_PppLqrOutLQRs_Object = MibTableColumn
pppLqrOutLQRs = _PppLqrOutLQRs_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 5),
    _PppLqrOutLQRs_Type()
)
pppLqrOutLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqrOutLQRs.setStatus("mandatory")
_PppLqrInLQRs_Type = Counter32
_PppLqrInLQRs_Object = MibTableColumn
pppLqrInLQRs = _PppLqrInLQRs_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 6),
    _PppLqrInLQRs_Type()
)
pppLqrInLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqrInLQRs.setStatus("mandatory")
_PppLqrConfigTable_Object = MibTable
pppLqrConfigTable = _PppLqrConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pppLqrConfigTable.setStatus("mandatory")
_PppLqrConfigEntry_Object = MibTableRow
pppLqrConfigEntry = _PppLqrConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1)
)
pppLqrConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppLqrConfigEntry.setStatus("mandatory")


class _PppLqrConfigPeriod_Type(Integer32):
    """Custom type pppLqrConfigPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppLqrConfigPeriod_Type.__name__ = "Integer32"
_PppLqrConfigPeriod_Object = MibTableColumn
pppLqrConfigPeriod = _PppLqrConfigPeriod_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1, 1),
    _PppLqrConfigPeriod_Type()
)
pppLqrConfigPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLqrConfigPeriod.setStatus("mandatory")


class _PppLqrConfigStatus_Type(Integer32):
    """Custom type pppLqrConfigStatus based on Integer32"""
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


_PppLqrConfigStatus_Type.__name__ = "Integer32"
_PppLqrConfigStatus_Object = MibTableColumn
pppLqrConfigStatus = _PppLqrConfigStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1, 2),
    _PppLqrConfigStatus_Type()
)
pppLqrConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLqrConfigStatus.setStatus("mandatory")
_PppLqrExtnsTable_Object = MibTable
pppLqrExtnsTable = _PppLqrExtnsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pppLqrExtnsTable.setStatus("mandatory")
_PppLqrExtnsEntry_Object = MibTableRow
pppLqrExtnsEntry = _PppLqrExtnsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3, 1)
)
pppLqrExtnsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppLqrExtnsEntry.setStatus("mandatory")


class _PppLqrExtnsLastReceivedLqrPacket_Type(OctetString):
    """Custom type pppLqrExtnsLastReceivedLqrPacket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(68, 68),
    )


_PppLqrExtnsLastReceivedLqrPacket_Type.__name__ = "OctetString"
_PppLqrExtnsLastReceivedLqrPacket_Object = MibTableColumn
pppLqrExtnsLastReceivedLqrPacket = _PppLqrExtnsLastReceivedLqrPacket_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3, 1, 1),
    _PppLqrExtnsLastReceivedLqrPacket_Type()
)
pppLqrExtnsLastReceivedLqrPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqrExtnsLastReceivedLqrPacket.setStatus("mandatory")
_PppTests_ObjectIdentity = ObjectIdentity
pppTests = _PppTests_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 3)
)
_PppEchoTest_ObjectIdentity = ObjectIdentity
pppEchoTest = _PppEchoTest_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 3, 1)
)
_PppDiscardTest_ObjectIdentity = ObjectIdentity
pppDiscardTest = _PppDiscardTest_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PPP-LCP-MIB",
    **{"ppp": ppp,
       "pppLcp": pppLcp,
       "pppLink": pppLink,
       "pppLinkStatusTable": pppLinkStatusTable,
       "pppLinkStatusEntry": pppLinkStatusEntry,
       "pppLinkStatusPhysicalIndex": pppLinkStatusPhysicalIndex,
       "pppLinkStatusBadAddresses": pppLinkStatusBadAddresses,
       "pppLinkStatusBadControls": pppLinkStatusBadControls,
       "pppLinkStatusPacketTooLongs": pppLinkStatusPacketTooLongs,
       "pppLinkStatusBadFCSs": pppLinkStatusBadFCSs,
       "pppLinkStatusLocalMRU": pppLinkStatusLocalMRU,
       "pppLinkStatusRemoteMRU": pppLinkStatusRemoteMRU,
       "pppLinkStatusLocalToPeerACCMap": pppLinkStatusLocalToPeerACCMap,
       "pppLinkStatusPeerToLocalACCMap": pppLinkStatusPeerToLocalACCMap,
       "pppLinkStatusLocalToRemoteProtocolCompression": pppLinkStatusLocalToRemoteProtocolCompression,
       "pppLinkStatusRemoteToLocalProtocolCompression": pppLinkStatusRemoteToLocalProtocolCompression,
       "pppLinkStatusLocalToRemoteACCompression": pppLinkStatusLocalToRemoteACCompression,
       "pppLinkStatusRemoteToLocalACCompression": pppLinkStatusRemoteToLocalACCompression,
       "pppLinkStatusTransmitFcsSize": pppLinkStatusTransmitFcsSize,
       "pppLinkStatusReceiveFcsSize": pppLinkStatusReceiveFcsSize,
       "pppLinkConfigTable": pppLinkConfigTable,
       "pppLinkConfigEntry": pppLinkConfigEntry,
       "pppLinkConfigInitialMRU": pppLinkConfigInitialMRU,
       "pppLinkConfigReceiveACCMap": pppLinkConfigReceiveACCMap,
       "pppLinkConfigTransmitACCMap": pppLinkConfigTransmitACCMap,
       "pppLinkConfigMagicNumber": pppLinkConfigMagicNumber,
       "pppLinkConfigFcsSize": pppLinkConfigFcsSize,
       "pppLqr": pppLqr,
       "pppLqrTable": pppLqrTable,
       "pppLqrEntry": pppLqrEntry,
       "pppLqrQuality": pppLqrQuality,
       "pppLqrInGoodOctets": pppLqrInGoodOctets,
       "pppLqrLocalPeriod": pppLqrLocalPeriod,
       "pppLqrRemotePeriod": pppLqrRemotePeriod,
       "pppLqrOutLQRs": pppLqrOutLQRs,
       "pppLqrInLQRs": pppLqrInLQRs,
       "pppLqrConfigTable": pppLqrConfigTable,
       "pppLqrConfigEntry": pppLqrConfigEntry,
       "pppLqrConfigPeriod": pppLqrConfigPeriod,
       "pppLqrConfigStatus": pppLqrConfigStatus,
       "pppLqrExtnsTable": pppLqrExtnsTable,
       "pppLqrExtnsEntry": pppLqrExtnsEntry,
       "pppLqrExtnsLastReceivedLqrPacket": pppLqrExtnsLastReceivedLqrPacket,
       "pppTests": pppTests,
       "pppEchoTest": pppEchoTest,
       "pppDiscardTest": pppDiscardTest}
)
