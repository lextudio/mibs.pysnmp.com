# SNMP MIB module (SHIVA-AT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SHIVA-AT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:51:12 2024
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

(tATalk,) = mibBuilder.importSymbols(
    "SHIVA-MIB",
    "tATalk")

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

_TRTMPEntryTimeouts_Type = Integer32
_TRTMPEntryTimeouts_Object = MibScalar
tRTMPEntryTimeouts = _TRTMPEntryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 1),
    _TRTMPEntryTimeouts_Type()
)
tRTMPEntryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryTimeouts.setStatus("mandatory")
_TRTMPEntryDeletes_Type = Integer32
_TRTMPEntryDeletes_Object = MibScalar
tRTMPEntryDeletes = _TRTMPEntryDeletes_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 2),
    _TRTMPEntryDeletes_Type()
)
tRTMPEntryDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryDeletes.setStatus("mandatory")
_TRTMPEntryEqualReplaces_Type = Integer32
_TRTMPEntryEqualReplaces_Object = MibScalar
tRTMPEntryEqualReplaces = _TRTMPEntryEqualReplaces_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 3),
    _TRTMPEntryEqualReplaces_Type()
)
tRTMPEntryEqualReplaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryEqualReplaces.setStatus("mandatory")
_TRTMPEntryBetterReplaces_Type = Integer32
_TRTMPEntryBetterReplaces_Object = MibScalar
tRTMPEntryBetterReplaces = _TRTMPEntryBetterReplaces_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 4),
    _TRTMPEntryBetterReplaces_Type()
)
tRTMPEntryBetterReplaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryBetterReplaces.setStatus("mandatory")
_TRTMPEntryAdds_Type = Integer32
_TRTMPEntryAdds_Object = MibScalar
tRTMPEntryAdds = _TRTMPEntryAdds_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 5),
    _TRTMPEntryAdds_Type()
)
tRTMPEntryAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryAdds.setStatus("mandatory")


class _TRTMPZeroCounters_Type(Integer32):
    """Custom type tRTMPZeroCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("zero", 1)
    )


_TRTMPZeroCounters_Type.__name__ = "Integer32"
_TRTMPZeroCounters_Object = MibScalar
tRTMPZeroCounters = _TRTMPZeroCounters_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 6),
    _TRTMPZeroCounters_Type()
)
tRTMPZeroCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRTMPZeroCounters.setStatus("mandatory")
_TZIPDeletes_Type = Integer32
_TZIPDeletes_Object = MibScalar
tZIPDeletes = _TZIPDeletes_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 7),
    _TZIPDeletes_Type()
)
tZIPDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tZIPDeletes.setStatus("mandatory")
_TZIPAdds_Type = Integer32
_TZIPAdds_Object = MibScalar
tZIPAdds = _TZIPAdds_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 8),
    _TZIPAdds_Type()
)
tZIPAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tZIPAdds.setStatus("mandatory")


class _TZIPZeroCounters_Type(Integer32):
    """Custom type tZIPZeroCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("zero", 1)
    )


_TZIPZeroCounters_Type.__name__ = "Integer32"
_TZIPZeroCounters_Object = MibScalar
tZIPZeroCounters = _TZIPZeroCounters_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 9),
    _TZIPZeroCounters_Type()
)
tZIPZeroCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tZIPZeroCounters.setStatus("mandatory")


class _TAARPClearCache_Type(Integer32):
    """Custom type tAARPClearCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TAARPClearCache_Type.__name__ = "Integer32"
_TAARPClearCache_Object = MibScalar
tAARPClearCache = _TAARPClearCache_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 10),
    _TAARPClearCache_Type()
)
tAARPClearCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tAARPClearCache.setStatus("mandatory")


class _TKIPRoutesValid_Type(Integer32):
    """Custom type tKIPRoutesValid based on Integer32"""
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


_TKIPRoutesValid_Type.__name__ = "Integer32"
_TKIPRoutesValid_Object = MibScalar
tKIPRoutesValid = _TKIPRoutesValid_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 11),
    _TKIPRoutesValid_Type()
)
tKIPRoutesValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tKIPRoutesValid.setStatus("mandatory")
_TNBPDeviceObject_Type = OctetString
_TNBPDeviceObject_Object = MibScalar
tNBPDeviceObject = _TNBPDeviceObject_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 12),
    _TNBPDeviceObject_Type()
)
tNBPDeviceObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNBPDeviceObject.setStatus("mandatory")
_TNBPDeviceType_Type = OctetString
_TNBPDeviceType_Object = MibScalar
tNBPDeviceType = _TNBPDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 13),
    _TNBPDeviceType_Type()
)
tNBPDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNBPDeviceType.setStatus("mandatory")
_TNBPDeviceZone_Type = OctetString
_TNBPDeviceZone_Object = MibScalar
tNBPDeviceZone = _TNBPDeviceZone_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 14),
    _TNBPDeviceZone_Type()
)
tNBPDeviceZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNBPDeviceZone.setStatus("mandatory")
_TNBPDeviceSocket_Type = Integer32
_TNBPDeviceSocket_Object = MibScalar
tNBPDeviceSocket = _TNBPDeviceSocket_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 15),
    _TNBPDeviceSocket_Type()
)
tNBPDeviceSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNBPDeviceSocket.setStatus("mandatory")


class _TATDialinNetwork_Type(OctetString):
    """Custom type tATDialinNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TATDialinNetwork_Type.__name__ = "OctetString"
_TATDialinNetwork_Object = MibScalar
tATDialinNetwork = _TATDialinNetwork_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 16),
    _TATDialinNetwork_Type()
)
tATDialinNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tATDialinNetwork.setStatus("mandatory")


class _TATDialinZone_Type(OctetString):
    """Custom type tATDialinZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TATDialinZone_Type.__name__ = "OctetString"
_TATDialinZone_Object = MibScalar
tATDialinZone = _TATDialinZone_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 17),
    _TATDialinZone_Type()
)
tATDialinZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tATDialinZone.setStatus("mandatory")


class _TATRoutingMode_Type(Integer32):
    """Custom type tATRoutingMode based on Integer32"""
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
        *(("conformingRouter", 1),
          ("endNode", 3),
          ("other", 4),
          ("seedRouter", 2))
    )


_TATRoutingMode_Type.__name__ = "Integer32"
_TATRoutingMode_Object = MibScalar
tATRoutingMode = _TATRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 18),
    _TATRoutingMode_Type()
)
tATRoutingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tATRoutingMode.setStatus("mandatory")


class _TATDialinPacketDeliveryMode_Type(Integer32):
    """Custom type tATDialinPacketDeliveryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("endNodeForwarding", 2),
          ("other", 3),
          ("routing", 1))
    )


_TATDialinPacketDeliveryMode_Type.__name__ = "Integer32"
_TATDialinPacketDeliveryMode_Object = MibScalar
tATDialinPacketDeliveryMode = _TATDialinPacketDeliveryMode_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 19),
    _TATDialinPacketDeliveryMode_Type()
)
tATDialinPacketDeliveryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tATDialinPacketDeliveryMode.setStatus("mandatory")
_TRTMPEntryTotal_Type = Integer32
_TRTMPEntryTotal_Object = MibScalar
tRTMPEntryTotal = _TRTMPEntryTotal_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 20),
    _TRTMPEntryTotal_Type()
)
tRTMPEntryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRTMPEntryTotal.setStatus("mandatory")
_TZoneTotal_Type = Integer32
_TZoneTotal_Object = MibScalar
tZoneTotal = _TZoneTotal_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 2, 21),
    _TZoneTotal_Type()
)
tZoneTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tZoneTotal.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SHIVA-AT-MIB",
    **{"tRTMPEntryTimeouts": tRTMPEntryTimeouts,
       "tRTMPEntryDeletes": tRTMPEntryDeletes,
       "tRTMPEntryEqualReplaces": tRTMPEntryEqualReplaces,
       "tRTMPEntryBetterReplaces": tRTMPEntryBetterReplaces,
       "tRTMPEntryAdds": tRTMPEntryAdds,
       "tRTMPZeroCounters": tRTMPZeroCounters,
       "tZIPDeletes": tZIPDeletes,
       "tZIPAdds": tZIPAdds,
       "tZIPZeroCounters": tZIPZeroCounters,
       "tAARPClearCache": tAARPClearCache,
       "tKIPRoutesValid": tKIPRoutesValid,
       "tNBPDeviceObject": tNBPDeviceObject,
       "tNBPDeviceType": tNBPDeviceType,
       "tNBPDeviceZone": tNBPDeviceZone,
       "tNBPDeviceSocket": tNBPDeviceSocket,
       "tATDialinNetwork": tATDialinNetwork,
       "tATDialinZone": tATDialinZone,
       "tATRoutingMode": tATRoutingMode,
       "tATDialinPacketDeliveryMode": tATDialinPacketDeliveryMode,
       "tRTMPEntryTotal": tRTMPEntryTotal,
       "tZoneTotal": tZoneTotal}
)
