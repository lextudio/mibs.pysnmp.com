# SNMP MIB module (GBNPlatformOAMSntpClient-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBNPlatformOAMSntpClient-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:55 2024
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

(gbnPlatformOAM,) = mibBuilder.importSymbols(
    "GBNPlatformOAM-MIB",
    "gbnPlatformOAM")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gbnPlatformOAMSntpClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8)
)
gbnPlatformOAMSntpClient.setRevisions(
        ("1901-07-15 20:04",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SntpClientGeneral_ObjectIdentity = ObjectIdentity
sntpClientGeneral = _SntpClientGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1)
)


class _SntpClientMode_Type(Integer32):
    """Custom type sntpClientMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("anycast", 2),
          ("broadcast", 4),
          ("multicast", 8),
          ("unicast", 1))
    )


_SntpClientMode_Type.__name__ = "Integer32"
_SntpClientMode_Object = MibScalar
sntpClientMode = _SntpClientMode_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 1),
    _SntpClientMode_Type()
)
sntpClientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientMode.setStatus("current")


class _SntpClientPollInterval_Type(Integer32):
    """Custom type sntpClientPollInterval based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024),
    )


_SntpClientPollInterval_Type.__name__ = "Integer32"
_SntpClientPollInterval_Object = MibScalar
sntpClientPollInterval = _SntpClientPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 2),
    _SntpClientPollInterval_Type()
)
sntpClientPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientPollInterval.setStatus("current")


class _SntpClientRetransInterval_Type(Integer32):
    """Custom type sntpClientRetransInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SntpClientRetransInterval_Type.__name__ = "Integer32"
_SntpClientRetransInterval_Object = MibScalar
sntpClientRetransInterval = _SntpClientRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 3),
    _SntpClientRetransInterval_Type()
)
sntpClientRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientRetransInterval.setStatus("current")


class _SntpClientRetransTimes_Type(Integer32):
    """Custom type sntpClientRetransTimes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SntpClientRetransTimes_Type.__name__ = "Integer32"
_SntpClientRetransTimes_Object = MibScalar
sntpClientRetransTimes = _SntpClientRetransTimes_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 4),
    _SntpClientRetransTimes_Type()
)
sntpClientRetransTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientRetransTimes.setStatus("current")
_SntpClientServer_Type = IpAddress
_SntpClientServer_Object = MibScalar
sntpClientServer = _SntpClientServer_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 5),
    _SntpClientServer_Type()
)
sntpClientServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientServer.setStatus("current")
_SntpClientSynthFlag_Type = TruthValue
_SntpClientSynthFlag_Object = MibScalar
sntpClientSynthFlag = _SntpClientSynthFlag_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 6),
    _SntpClientSynthFlag_Type()
)
sntpClientSynthFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpClientSynthFlag.setStatus("current")
_SntpClientState_Type = Integer32
_SntpClientState_Object = MibScalar
sntpClientState = _SntpClientState_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 7),
    _SntpClientState_Type()
)
sntpClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpClientState.setStatus("current")
_SntpClientLastSynthTime_Type = Integer32
_SntpClientLastSynthTime_Object = MibScalar
sntpClientLastSynthTime = _SntpClientLastSynthTime_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 8),
    _SntpClientLastSynthTime_Type()
)
sntpClientLastSynthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpClientLastSynthTime.setStatus("current")
_SntpClientLastSynthErrno_Type = Integer32
_SntpClientLastSynthErrno_Object = MibScalar
sntpClientLastSynthErrno = _SntpClientLastSynthErrno_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 9),
    _SntpClientLastSynthErrno_Type()
)
sntpClientLastSynthErrno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpClientLastSynthErrno.setStatus("current")


class _SntpClientAdminStatus_Type(Integer32):
    """Custom type sntpClientAdminStatus based on Integer32"""
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


_SntpClientAdminStatus_Type.__name__ = "Integer32"
_SntpClientAdminStatus_Object = MibScalar
sntpClientAdminStatus = _SntpClientAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 10),
    _SntpClientAdminStatus_Type()
)
sntpClientAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientAdminStatus.setStatus("current")


class _SntpClientBcastDelay_Type(Integer32):
    """Custom type sntpClientBcastDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_SntpClientBcastDelay_Type.__name__ = "Integer32"
_SntpClientBcastDelay_Object = MibScalar
sntpClientBcastDelay = _SntpClientBcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 11),
    _SntpClientBcastDelay_Type()
)
sntpClientBcastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientBcastDelay.setStatus("current")


class _SntpClientMcastTtl_Type(Integer32):
    """Custom type sntpClientMcastTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SntpClientMcastTtl_Type.__name__ = "Integer32"
_SntpClientMcastTtl_Object = MibScalar
sntpClientMcastTtl = _SntpClientMcastTtl_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 12),
    _SntpClientMcastTtl_Type()
)
sntpClientMcastTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientMcastTtl.setStatus("current")
_SntpClientAuthFlag_Type = TruthValue
_SntpClientAuthFlag_Object = MibScalar
sntpClientAuthFlag = _SntpClientAuthFlag_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 13),
    _SntpClientAuthFlag_Type()
)
sntpClientAuthFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientAuthFlag.setStatus("current")
_SntpClientUniKeyID_Type = Unsigned32
_SntpClientUniKeyID_Object = MibScalar
sntpClientUniKeyID = _SntpClientUniKeyID_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 14),
    _SntpClientUniKeyID_Type()
)
sntpClientUniKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientUniKeyID.setStatus("current")
_SntpClientAnyKeyID_Type = Unsigned32
_SntpClientAnyKeyID_Object = MibScalar
sntpClientAnyKeyID = _SntpClientAnyKeyID_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 1, 15),
    _SntpClientAnyKeyID_Type()
)
sntpClientAnyKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientAnyKeyID.setStatus("current")
_SntpClientValidServerTable_Object = MibTable
sntpClientValidServerTable = _SntpClientValidServerTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    sntpClientValidServerTable.setStatus("current")
_SntpClientValidServerEntry_Object = MibTableRow
sntpClientValidServerEntry = _SntpClientValidServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 2, 1)
)
sntpClientValidServerEntry.setIndexNames(
    (0, "GBNPlatformOAMSntpClient-MIB", "sntpClientValidServerNet"),
    (0, "GBNPlatformOAMSntpClient-MIB", "sntpClientValidServerMask"),
)
if mibBuilder.loadTexts:
    sntpClientValidServerEntry.setStatus("current")
_SntpClientValidServerNet_Type = IpAddress
_SntpClientValidServerNet_Object = MibTableColumn
sntpClientValidServerNet = _SntpClientValidServerNet_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 2, 1, 1),
    _SntpClientValidServerNet_Type()
)
sntpClientValidServerNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpClientValidServerNet.setStatus("current")
_SntpClientValidServerMask_Type = IpAddress
_SntpClientValidServerMask_Object = MibTableColumn
sntpClientValidServerMask = _SntpClientValidServerMask_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 2, 1, 2),
    _SntpClientValidServerMask_Type()
)
sntpClientValidServerMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpClientValidServerMask.setStatus("current")
_SntpClientValidServerRowStatus_Type = RowStatus
_SntpClientValidServerRowStatus_Object = MibTableColumn
sntpClientValidServerRowStatus = _SntpClientValidServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 2, 1, 3),
    _SntpClientValidServerRowStatus_Type()
)
sntpClientValidServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientValidServerRowStatus.setStatus("current")
_SntpAuthKeyTable_Object = MibTable
sntpAuthKeyTable = _SntpAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    sntpAuthKeyTable.setStatus("current")
_SntpAuthKeyEntry_Object = MibTableRow
sntpAuthKeyEntry = _SntpAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 3, 1)
)
sntpAuthKeyEntry.setIndexNames(
    (0, "GBNPlatformOAMSntpClient-MIB", "sntpAuthKeyId"),
)
if mibBuilder.loadTexts:
    sntpAuthKeyEntry.setStatus("current")


class _SntpAuthKeyId_Type(Unsigned32):
    """Custom type sntpAuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SntpAuthKeyId_Type.__name__ = "Unsigned32"
_SntpAuthKeyId_Object = MibTableColumn
sntpAuthKeyId = _SntpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 3, 1, 1),
    _SntpAuthKeyId_Type()
)
sntpAuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpAuthKeyId.setStatus("current")


class _SntpAuthKeyValue_Type(DisplayString):
    """Custom type sntpAuthKeyValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SntpAuthKeyValue_Type.__name__ = "DisplayString"
_SntpAuthKeyValue_Object = MibTableColumn
sntpAuthKeyValue = _SntpAuthKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 3, 1, 2),
    _SntpAuthKeyValue_Type()
)
sntpAuthKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpAuthKeyValue.setStatus("current")
_SntpAuthKeyTrustFlag_Type = TruthValue
_SntpAuthKeyTrustFlag_Object = MibTableColumn
sntpAuthKeyTrustFlag = _SntpAuthKeyTrustFlag_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 3, 1, 3),
    _SntpAuthKeyTrustFlag_Type()
)
sntpAuthKeyTrustFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpAuthKeyTrustFlag.setStatus("current")
_SntpAuthKeyRowStatus_Type = RowStatus
_SntpAuthKeyRowStatus_Object = MibTableColumn
sntpAuthKeyRowStatus = _SntpAuthKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8, 3, 1, 4),
    _SntpAuthKeyRowStatus_Type()
)
sntpAuthKeyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpAuthKeyRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNPlatformOAMSntpClient-MIB",
    **{"gbnPlatformOAMSntpClient": gbnPlatformOAMSntpClient,
       "sntpClientGeneral": sntpClientGeneral,
       "sntpClientMode": sntpClientMode,
       "sntpClientPollInterval": sntpClientPollInterval,
       "sntpClientRetransInterval": sntpClientRetransInterval,
       "sntpClientRetransTimes": sntpClientRetransTimes,
       "sntpClientServer": sntpClientServer,
       "sntpClientSynthFlag": sntpClientSynthFlag,
       "sntpClientState": sntpClientState,
       "sntpClientLastSynthTime": sntpClientLastSynthTime,
       "sntpClientLastSynthErrno": sntpClientLastSynthErrno,
       "sntpClientAdminStatus": sntpClientAdminStatus,
       "sntpClientBcastDelay": sntpClientBcastDelay,
       "sntpClientMcastTtl": sntpClientMcastTtl,
       "sntpClientAuthFlag": sntpClientAuthFlag,
       "sntpClientUniKeyID": sntpClientUniKeyID,
       "sntpClientAnyKeyID": sntpClientAnyKeyID,
       "sntpClientValidServerTable": sntpClientValidServerTable,
       "sntpClientValidServerEntry": sntpClientValidServerEntry,
       "sntpClientValidServerNet": sntpClientValidServerNet,
       "sntpClientValidServerMask": sntpClientValidServerMask,
       "sntpClientValidServerRowStatus": sntpClientValidServerRowStatus,
       "sntpAuthKeyTable": sntpAuthKeyTable,
       "sntpAuthKeyEntry": sntpAuthKeyEntry,
       "sntpAuthKeyId": sntpAuthKeyId,
       "sntpAuthKeyValue": sntpAuthKeyValue,
       "sntpAuthKeyTrustFlag": sntpAuthKeyTrustFlag,
       "sntpAuthKeyRowStatus": sntpAuthKeyRowStatus}
)
