# SNMP MIB module (HP-SNTPclientConfiguration-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SNTPclientConfiguration-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:58 2024
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

(hpicfCommon,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpSntpConfigMod = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8)
)
hpSntpConfigMod.setRevisions(
        ("2015-05-24 00:00",
         "2014-01-13 00:00",
         "2011-02-12 00:00",
         "2009-02-13 12:30",
         "2009-02-10 15:39",
         "2008-11-26 02:39",
         "2000-11-03 02:39")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpSntpConfig_ObjectIdentity = ObjectIdentity
hpSntpConfig = _HpSntpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1)
)


class _HpSntpConfigMode_Type(Integer32):
    """Custom type hpSntpConfigMode based on Integer32"""
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
        *(("broadcast", 3),
          ("dhcp", 4),
          ("disabled", 1),
          ("unicast", 2))
    )


_HpSntpConfigMode_Type.__name__ = "Integer32"
_HpSntpConfigMode_Object = MibScalar
hpSntpConfigMode = _HpSntpConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 1),
    _HpSntpConfigMode_Type()
)
hpSntpConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSntpConfigMode.setStatus("current")


class _HpSntpConfigPollInterval_Type(Integer32):
    """Custom type hpSntpConfigPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_HpSntpConfigPollInterval_Type.__name__ = "Integer32"
_HpSntpConfigPollInterval_Object = MibScalar
hpSntpConfigPollInterval = _HpSntpConfigPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 2),
    _HpSntpConfigPollInterval_Type()
)
hpSntpConfigPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSntpConfigPollInterval.setStatus("current")
_HpSntpConfigServerTable_Object = MibTable
hpSntpConfigServerTable = _HpSntpConfigServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hpSntpConfigServerTable.setStatus("deprecated")
_HpSntpServerEntry_Object = MibTableRow
hpSntpServerEntry = _HpSntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 3, 1)
)
hpSntpServerEntry.setIndexNames(
    (0, "HP-SNTPclientConfiguration-MIB", "hpSntpServerAddress"),
)
if mibBuilder.loadTexts:
    hpSntpServerEntry.setStatus("deprecated")
_HpSntpServerAddress_Type = IpAddress
_HpSntpServerAddress_Object = MibTableColumn
hpSntpServerAddress = _HpSntpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 3, 1, 1),
    _HpSntpServerAddress_Type()
)
hpSntpServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSntpServerAddress.setStatus("deprecated")


class _HpSntpServerVersion_Type(Integer32):
    """Custom type hpSntpServerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HpSntpServerVersion_Type.__name__ = "Integer32"
_HpSntpServerVersion_Object = MibTableColumn
hpSntpServerVersion = _HpSntpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 3, 1, 2),
    _HpSntpServerVersion_Type()
)
hpSntpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpServerVersion.setStatus("deprecated")


class _HpSntpServerPriority_Type(Integer32):
    """Custom type hpSntpServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSntpServerPriority_Type.__name__ = "Integer32"
_HpSntpServerPriority_Object = MibTableColumn
hpSntpServerPriority = _HpSntpServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 3, 1, 3),
    _HpSntpServerPriority_Type()
)
hpSntpServerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpServerPriority.setStatus("deprecated")
_HpSntpServerRowStatus_Type = RowStatus
_HpSntpServerRowStatus_Object = MibTableColumn
hpSntpServerRowStatus = _HpSntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 3, 1, 4),
    _HpSntpServerRowStatus_Type()
)
hpSntpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpServerRowStatus.setStatus("deprecated")
_HpSntpInetConfigServerTable_Object = MibTable
hpSntpInetConfigServerTable = _HpSntpInetConfigServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 4)
)
if mibBuilder.loadTexts:
    hpSntpInetConfigServerTable.setStatus("current")
_HpSntpInetServerEntry_Object = MibTableRow
hpSntpInetServerEntry = _HpSntpInetServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 4, 1)
)
hpSntpInetServerEntry.setIndexNames(
    (0, "HP-SNTPclientConfiguration-MIB", "hpSntpInetServerPriority"),
    (0, "HP-SNTPclientConfiguration-MIB", "hpSntpInetServerAddressType"),
    (0, "HP-SNTPclientConfiguration-MIB", "hpSntpInetServerAddress"),
)
if mibBuilder.loadTexts:
    hpSntpInetServerEntry.setStatus("current")


class _HpSntpInetServerPriority_Type(Integer32):
    """Custom type hpSntpInetServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSntpInetServerPriority_Type.__name__ = "Integer32"
_HpSntpInetServerPriority_Object = MibTableColumn
hpSntpInetServerPriority = _HpSntpInetServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 4, 1, 1),
    _HpSntpInetServerPriority_Type()
)
hpSntpInetServerPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSntpInetServerPriority.setStatus("current")
_HpSntpInetServerAddressType_Type = InetAddressType
_HpSntpInetServerAddressType_Object = MibTableColumn
hpSntpInetServerAddressType = _HpSntpInetServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 4, 1, 2),
    _HpSntpInetServerAddressType_Type()
)
hpSntpInetServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSntpInetServerAddressType.setStatus("current")
_HpSntpInetServerAddress_Type = InetAddress
_HpSntpInetServerAddress_Object = MibTableColumn
hpSntpInetServerAddress = _HpSntpInetServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 4, 1, 3),
    _HpSntpInetServerAddress_Type()
)
hpSntpInetServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSntpInetServerAddress.setStatus("current")


class _HpSntpInetServerVersion_Type(Integer32):
    """Custom type hpSntpInetServerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HpSntpInetServerVersion_Type.__name__ = "Integer32"
_HpSntpInetServerVersion_Object = MibTableColumn
hpSntpInetServerVersion = _HpSntpInetServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 4, 1, 4),
    _HpSntpInetServerVersion_Type()
)
hpSntpInetServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpInetServerVersion.setStatus("current")
_HpSntpInetServerRowStatus_Type = RowStatus
_HpSntpInetServerRowStatus_Object = MibTableColumn
hpSntpInetServerRowStatus = _HpSntpInetServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 4, 1, 5),
    _HpSntpInetServerRowStatus_Type()
)
hpSntpInetServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpInetServerRowStatus.setStatus("current")


class _HpSntpInetServerIsOobm_Type(TruthValue):
    """Custom type hpSntpInetServerIsOobm based on TruthValue"""


_HpSntpInetServerIsOobm_Object = MibTableColumn
hpSntpInetServerIsOobm = _HpSntpInetServerIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 4, 1, 6),
    _HpSntpInetServerIsOobm_Type()
)
hpSntpInetServerIsOobm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpInetServerIsOobm.setStatus("current")


class _HpSntpInetServerAuthKeyId_Type(Unsigned32):
    """Custom type hpSntpInetServerAuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpSntpInetServerAuthKeyId_Type.__name__ = "Unsigned32"
_HpSntpInetServerAuthKeyId_Object = MibTableColumn
hpSntpInetServerAuthKeyId = _HpSntpInetServerAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 4, 1, 7),
    _HpSntpInetServerAuthKeyId_Type()
)
hpSntpInetServerAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpInetServerAuthKeyId.setStatus("current")


class _HpSntpAuthentication_Type(Integer32):
    """Custom type hpSntpAuthentication based on Integer32"""
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


_HpSntpAuthentication_Type.__name__ = "Integer32"
_HpSntpAuthentication_Object = MibScalar
hpSntpAuthentication = _HpSntpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 5),
    _HpSntpAuthentication_Type()
)
hpSntpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSntpAuthentication.setStatus("current")
_HpSntpAuthenticationKeyTable_Object = MibTable
hpSntpAuthenticationKeyTable = _HpSntpAuthenticationKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 6)
)
if mibBuilder.loadTexts:
    hpSntpAuthenticationKeyTable.setStatus("current")
_HpSntpAuthenticationKeyEntry_Object = MibTableRow
hpSntpAuthenticationKeyEntry = _HpSntpAuthenticationKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 6, 1)
)
hpSntpAuthenticationKeyEntry.setIndexNames(
    (0, "HP-SNTPclientConfiguration-MIB", "hpSntpAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    hpSntpAuthenticationKeyEntry.setStatus("current")


class _HpSntpAuthenticationKeyId_Type(Unsigned32):
    """Custom type hpSntpAuthenticationKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpSntpAuthenticationKeyId_Type.__name__ = "Unsigned32"
_HpSntpAuthenticationKeyId_Object = MibTableColumn
hpSntpAuthenticationKeyId = _HpSntpAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 6, 1, 1),
    _HpSntpAuthenticationKeyId_Type()
)
hpSntpAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSntpAuthenticationKeyId.setStatus("current")


class _HpSntpAuthenticationKeyAuthMode_Type(Integer32):
    """Custom type hpSntpAuthenticationKeyAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1))
    )


_HpSntpAuthenticationKeyAuthMode_Type.__name__ = "Integer32"
_HpSntpAuthenticationKeyAuthMode_Object = MibTableColumn
hpSntpAuthenticationKeyAuthMode = _HpSntpAuthenticationKeyAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 6, 1, 2),
    _HpSntpAuthenticationKeyAuthMode_Type()
)
hpSntpAuthenticationKeyAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpAuthenticationKeyAuthMode.setStatus("current")


class _HpSntpAuthenticationKeyValue_Type(OctetString):
    """Custom type hpSntpAuthenticationKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpSntpAuthenticationKeyValue_Type.__name__ = "OctetString"
_HpSntpAuthenticationKeyValue_Object = MibTableColumn
hpSntpAuthenticationKeyValue = _HpSntpAuthenticationKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 6, 1, 3),
    _HpSntpAuthenticationKeyValue_Type()
)
hpSntpAuthenticationKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpAuthenticationKeyValue.setStatus("current")
_HpSntpAuthenticationKeyTrusted_Type = TruthValue
_HpSntpAuthenticationKeyTrusted_Object = MibTableColumn
hpSntpAuthenticationKeyTrusted = _HpSntpAuthenticationKeyTrusted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 6, 1, 4),
    _HpSntpAuthenticationKeyTrusted_Type()
)
hpSntpAuthenticationKeyTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpAuthenticationKeyTrusted.setStatus("current")
_HpSntpAuthenticationKeyRowStatus_Type = RowStatus
_HpSntpAuthenticationKeyRowStatus_Object = MibTableColumn
hpSntpAuthenticationKeyRowStatus = _HpSntpAuthenticationKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 6, 1, 5),
    _HpSntpAuthenticationKeyRowStatus_Type()
)
hpSntpAuthenticationKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpAuthenticationKeyRowStatus.setStatus("current")


class _HpSntpAuthenticationKeyEncrypted_Type(OctetString):
    """Custom type hpSntpAuthenticationKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSntpAuthenticationKeyEncrypted_Type.__name__ = "OctetString"
_HpSntpAuthenticationKeyEncrypted_Object = MibTableColumn
hpSntpAuthenticationKeyEncrypted = _HpSntpAuthenticationKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 6, 1, 6),
    _HpSntpAuthenticationKeyEncrypted_Type()
)
hpSntpAuthenticationKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSntpAuthenticationKeyEncrypted.setStatus("current")
_HpSntpServerStatisticsTable_Object = MibTable
hpSntpServerStatisticsTable = _HpSntpServerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 7)
)
if mibBuilder.loadTexts:
    hpSntpServerStatisticsTable.setStatus("current")
_HpSntpServerStatisticsEntry_Object = MibTableRow
hpSntpServerStatisticsEntry = _HpSntpServerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpSntpServerStatisticsEntry.setStatus("current")
_HpSntpServerStatisticsAuthFailedPkts_Type = Counter32
_HpSntpServerStatisticsAuthFailedPkts_Object = MibTableColumn
hpSntpServerStatisticsAuthFailedPkts = _HpSntpServerStatisticsAuthFailedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 7, 1, 1),
    _HpSntpServerStatisticsAuthFailedPkts_Type()
)
hpSntpServerStatisticsAuthFailedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSntpServerStatisticsAuthFailedPkts.setStatus("current")
_HpSntpBroadcastServerTable_Object = MibTable
hpSntpBroadcastServerTable = _HpSntpBroadcastServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 8)
)
if mibBuilder.loadTexts:
    hpSntpBroadcastServerTable.setStatus("current")
_HpSntpBroadcastServerEntry_Object = MibTableRow
hpSntpBroadcastServerEntry = _HpSntpBroadcastServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 8, 1)
)
hpSntpBroadcastServerEntry.setIndexNames(
    (0, "HP-SNTPclientConfiguration-MIB", "hpSntpBroadcastServerAddress"),
)
if mibBuilder.loadTexts:
    hpSntpBroadcastServerEntry.setStatus("current")
_HpSntpBroadcastServerAddress_Type = IpAddress
_HpSntpBroadcastServerAddress_Object = MibTableColumn
hpSntpBroadcastServerAddress = _HpSntpBroadcastServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 8, 1, 1),
    _HpSntpBroadcastServerAddress_Type()
)
hpSntpBroadcastServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSntpBroadcastServerAddress.setStatus("current")
_HpSntpBroadcastServerStatisticsAuthFailedPkts_Type = Counter32
_HpSntpBroadcastServerStatisticsAuthFailedPkts_Object = MibTableColumn
hpSntpBroadcastServerStatisticsAuthFailedPkts = _HpSntpBroadcastServerStatisticsAuthFailedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 1, 8, 1, 2),
    _HpSntpBroadcastServerStatisticsAuthFailedPkts_Type()
)
hpSntpBroadcastServerStatisticsAuthFailedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSntpBroadcastServerStatisticsAuthFailedPkts.setStatus("current")
_HpTimeSyncMethodMod_ObjectIdentity = ObjectIdentity
hpTimeSyncMethodMod = _HpTimeSyncMethodMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 2)
)


class _HpTimeSyncMethod_Type(Integer32):
    """Custom type hpTimeSyncMethod based on Integer32"""
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
        *(("none", 1),
          ("ntp", 5),
          ("sntp", 2),
          ("timep", 3),
          ("timepOrSntp", 4))
    )


_HpTimeSyncMethod_Type.__name__ = "Integer32"
_HpTimeSyncMethod_Object = MibScalar
hpTimeSyncMethod = _HpTimeSyncMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 2, 1),
    _HpTimeSyncMethod_Type()
)
hpTimeSyncMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpTimeSyncMethod.setStatus("current")
_HpSntpConfigConformance_ObjectIdentity = ObjectIdentity
hpSntpConfigConformance = _HpSntpConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3)
)
_HpSntpConfigCompliances_ObjectIdentity = ObjectIdentity
hpSntpConfigCompliances = _HpSntpConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 1)
)
_HpSntpConfigGroups_ObjectIdentity = ObjectIdentity
hpSntpConfigGroups = _HpSntpConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 2)
)
_HpSntpStatistics_ObjectIdentity = ObjectIdentity
hpSntpStatistics = _HpSntpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 4)
)
_HpSntpStatsRcvdPkts_Type = Counter32
_HpSntpStatsRcvdPkts_Object = MibScalar
hpSntpStatsRcvdPkts = _HpSntpStatsRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 4, 1),
    _HpSntpStatsRcvdPkts_Type()
)
hpSntpStatsRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSntpStatsRcvdPkts.setStatus("current")
_HpSntpStatsSentPkts_Type = Counter32
_HpSntpStatsSentPkts_Object = MibScalar
hpSntpStatsSentPkts = _HpSntpStatsSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 4, 2),
    _HpSntpStatsSentPkts_Type()
)
hpSntpStatsSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSntpStatsSentPkts.setStatus("current")
_HpSntpStatsDroppedPkts_Type = Counter32
_HpSntpStatsDroppedPkts_Object = MibScalar
hpSntpStatsDroppedPkts = _HpSntpStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 4, 3),
    _HpSntpStatsDroppedPkts_Type()
)
hpSntpStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSntpStatsDroppedPkts.setStatus("current")
hpSntpInetServerEntry.registerAugmentions(
    ("HP-SNTPclientConfiguration-MIB",
     "hpSntpServerStatisticsEntry")
)
hpSntpServerStatisticsEntry.setIndexNames(*hpSntpInetServerEntry.getIndexNames())

# Managed Objects groups

hpSntpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 2, 1)
)
hpSntpConfigGroup.setObjects(
      *(("HP-SNTPclientConfiguration-MIB", "hpSntpConfigMode"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpConfigPollInterval"))
)
if mibBuilder.loadTexts:
    hpSntpConfigGroup.setStatus("current")

hpSntpServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 2, 2)
)
hpSntpServerConfigGroup.setObjects(
      *(("HP-SNTPclientConfiguration-MIB", "hpSntpServerVersion"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpServerPriority"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpServerRowStatus"))
)
if mibBuilder.loadTexts:
    hpSntpServerConfigGroup.setStatus("deprecated")

hpTimeSyncMethodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 2, 3)
)
hpTimeSyncMethodGroup.setObjects(
    ("HP-SNTPclientConfiguration-MIB", "hpTimeSyncMethod")
)
if mibBuilder.loadTexts:
    hpTimeSyncMethodGroup.setStatus("current")

hpSntpInetServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 2, 4)
)
hpSntpInetServerConfigGroup.setObjects(
      *(("HP-SNTPclientConfiguration-MIB", "hpSntpInetServerVersion"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpInetServerRowStatus"))
)
if mibBuilder.loadTexts:
    hpSntpInetServerConfigGroup.setStatus("current")

hpSntpAuthenticationKeyIdConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 2, 5)
)
hpSntpAuthenticationKeyIdConfigGroup.setObjects(
      *(("HP-SNTPclientConfiguration-MIB", "hpSntpAuthenticationKeyAuthMode"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpAuthenticationKeyValue"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpAuthenticationKeyTrusted"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpAuthenticationKeyRowStatus"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpServerStatisticsAuthFailedPkts"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpStatsDroppedPkts"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpStatsSentPkts"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpStatsRcvdPkts"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpAuthentication"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpInetServerAuthKeyId"))
)
if mibBuilder.loadTexts:
    hpSntpAuthenticationKeyIdConfigGroup.setStatus("deprecated")

hpSntpInetServerOobmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 2, 6)
)
hpSntpInetServerOobmGroup.setObjects(
    ("HP-SNTPclientConfiguration-MIB", "hpSntpInetServerIsOobm")
)
if mibBuilder.loadTexts:
    hpSntpInetServerOobmGroup.setStatus("current")

hpSntpAuthenticationKeyIdConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 2, 7)
)
hpSntpAuthenticationKeyIdConfigGroup1.setObjects(
      *(("HP-SNTPclientConfiguration-MIB", "hpSntpAuthenticationKeyAuthMode"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpAuthenticationKeyValue"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpAuthenticationKeyEncrypted"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpAuthenticationKeyTrusted"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpAuthenticationKeyRowStatus"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpServerStatisticsAuthFailedPkts"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpStatsDroppedPkts"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpStatsSentPkts"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpStatsRcvdPkts"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpAuthentication"),
        ("HP-SNTPclientConfiguration-MIB", "hpSntpInetServerAuthKeyId"))
)
if mibBuilder.loadTexts:
    hpSntpAuthenticationKeyIdConfigGroup1.setStatus("current")

hpSntpBroadcastServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 2, 8)
)
hpSntpBroadcastServerGroup.setObjects(
    ("HP-SNTPclientConfiguration-MIB", "hpSntpBroadcastServerStatisticsAuthFailedPkts")
)
if mibBuilder.loadTexts:
    hpSntpBroadcastServerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpSntpConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpSntpConfigCompliance.setStatus(
        "deprecated"
    )

hpSntpInetConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpSntpInetConfigCompliance.setStatus(
        "current"
    )

hpSntpAuthenticationConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hpSntpAuthenticationConfigCompliance.setStatus(
        "deprecated"
    )

hpSntpInetConfigComplianceOobm = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hpSntpInetConfigComplianceOobm.setStatus(
        "current"
    )

hpSntpAuthenticationConfigCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 1, 5)
)
if mibBuilder.loadTexts:
    hpSntpAuthenticationConfigCompliance1.setStatus(
        "current"
    )

hpSntpBroadcastServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 8, 3, 1, 6)
)
if mibBuilder.loadTexts:
    hpSntpBroadcastServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SNTPclientConfiguration-MIB",
    **{"hpSntpConfigMod": hpSntpConfigMod,
       "hpSntpConfig": hpSntpConfig,
       "hpSntpConfigMode": hpSntpConfigMode,
       "hpSntpConfigPollInterval": hpSntpConfigPollInterval,
       "hpSntpConfigServerTable": hpSntpConfigServerTable,
       "hpSntpServerEntry": hpSntpServerEntry,
       "hpSntpServerAddress": hpSntpServerAddress,
       "hpSntpServerVersion": hpSntpServerVersion,
       "hpSntpServerPriority": hpSntpServerPriority,
       "hpSntpServerRowStatus": hpSntpServerRowStatus,
       "hpSntpInetConfigServerTable": hpSntpInetConfigServerTable,
       "hpSntpInetServerEntry": hpSntpInetServerEntry,
       "hpSntpInetServerPriority": hpSntpInetServerPriority,
       "hpSntpInetServerAddressType": hpSntpInetServerAddressType,
       "hpSntpInetServerAddress": hpSntpInetServerAddress,
       "hpSntpInetServerVersion": hpSntpInetServerVersion,
       "hpSntpInetServerRowStatus": hpSntpInetServerRowStatus,
       "hpSntpInetServerIsOobm": hpSntpInetServerIsOobm,
       "hpSntpInetServerAuthKeyId": hpSntpInetServerAuthKeyId,
       "hpSntpAuthentication": hpSntpAuthentication,
       "hpSntpAuthenticationKeyTable": hpSntpAuthenticationKeyTable,
       "hpSntpAuthenticationKeyEntry": hpSntpAuthenticationKeyEntry,
       "hpSntpAuthenticationKeyId": hpSntpAuthenticationKeyId,
       "hpSntpAuthenticationKeyAuthMode": hpSntpAuthenticationKeyAuthMode,
       "hpSntpAuthenticationKeyValue": hpSntpAuthenticationKeyValue,
       "hpSntpAuthenticationKeyTrusted": hpSntpAuthenticationKeyTrusted,
       "hpSntpAuthenticationKeyRowStatus": hpSntpAuthenticationKeyRowStatus,
       "hpSntpAuthenticationKeyEncrypted": hpSntpAuthenticationKeyEncrypted,
       "hpSntpServerStatisticsTable": hpSntpServerStatisticsTable,
       "hpSntpServerStatisticsEntry": hpSntpServerStatisticsEntry,
       "hpSntpServerStatisticsAuthFailedPkts": hpSntpServerStatisticsAuthFailedPkts,
       "hpSntpBroadcastServerTable": hpSntpBroadcastServerTable,
       "hpSntpBroadcastServerEntry": hpSntpBroadcastServerEntry,
       "hpSntpBroadcastServerAddress": hpSntpBroadcastServerAddress,
       "hpSntpBroadcastServerStatisticsAuthFailedPkts": hpSntpBroadcastServerStatisticsAuthFailedPkts,
       "hpTimeSyncMethodMod": hpTimeSyncMethodMod,
       "hpTimeSyncMethod": hpTimeSyncMethod,
       "hpSntpConfigConformance": hpSntpConfigConformance,
       "hpSntpConfigCompliances": hpSntpConfigCompliances,
       "hpSntpConfigCompliance": hpSntpConfigCompliance,
       "hpSntpInetConfigCompliance": hpSntpInetConfigCompliance,
       "hpSntpAuthenticationConfigCompliance": hpSntpAuthenticationConfigCompliance,
       "hpSntpInetConfigComplianceOobm": hpSntpInetConfigComplianceOobm,
       "hpSntpAuthenticationConfigCompliance1": hpSntpAuthenticationConfigCompliance1,
       "hpSntpBroadcastServerCompliance": hpSntpBroadcastServerCompliance,
       "hpSntpConfigGroups": hpSntpConfigGroups,
       "hpSntpConfigGroup": hpSntpConfigGroup,
       "hpSntpServerConfigGroup": hpSntpServerConfigGroup,
       "hpTimeSyncMethodGroup": hpTimeSyncMethodGroup,
       "hpSntpInetServerConfigGroup": hpSntpInetServerConfigGroup,
       "hpSntpAuthenticationKeyIdConfigGroup": hpSntpAuthenticationKeyIdConfigGroup,
       "hpSntpInetServerOobmGroup": hpSntpInetServerOobmGroup,
       "hpSntpAuthenticationKeyIdConfigGroup1": hpSntpAuthenticationKeyIdConfigGroup1,
       "hpSntpBroadcastServerGroup": hpSntpBroadcastServerGroup,
       "hpSntpStatistics": hpSntpStatistics,
       "hpSntpStatsRcvdPkts": hpSntpStatsRcvdPkts,
       "hpSntpStatsSentPkts": hpSntpStatsSentPkts,
       "hpSntpStatsDroppedPkts": hpSntpStatsDroppedPkts}
)
