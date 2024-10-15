# SNMP MIB module (TPLINK-SNMPNOTIFICATIONHOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-SNMPNOTIFICATIONHOST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:39 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(tplinkSnmpMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-SNMP-MIB",
    "tplinkSnmpMIBObjects")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TpSnmpNotificationHost_ObjectIdentity = ObjectIdentity
tpSnmpNotificationHost = _TpSnmpNotificationHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1)
)
_TpSnmpNotificationHostTable_Object = MibTable
tpSnmpNotificationHostTable = _TpSnmpNotificationHostTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpSnmpNotificationHostTable.setStatus("current")
_TpSnmpNotificationHostEntry_Object = MibTableRow
tpSnmpNotificationHostEntry = _TpSnmpNotificationHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1)
)
tpSnmpNotificationHostEntry.setIndexNames(
    (0, "TPLINK-SNMPNOTIFICATIONHOST-MIB", "tpSnmpNotificationHostIpAddr"),
    (0, "TPLINK-SNMPNOTIFICATIONHOST-MIB", "tpSnmpNotificationHostUserName"),
)
if mibBuilder.loadTexts:
    tpSnmpNotificationHostEntry.setStatus("current")
_TpSnmpNotificationHostIpAddr_Type = IpAddress
_TpSnmpNotificationHostIpAddr_Object = MibTableColumn
tpSnmpNotificationHostIpAddr = _TpSnmpNotificationHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 1),
    _TpSnmpNotificationHostIpAddr_Type()
)
tpSnmpNotificationHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostIpAddr.setStatus("current")


class _TpSnmpNotificationHostUserName_Type(OctetString):
    """Custom type tpSnmpNotificationHostUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpSnmpNotificationHostUserName_Type.__name__ = "OctetString"
_TpSnmpNotificationHostUserName_Object = MibTableColumn
tpSnmpNotificationHostUserName = _TpSnmpNotificationHostUserName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 2),
    _TpSnmpNotificationHostUserName_Type()
)
tpSnmpNotificationHostUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostUserName.setStatus("current")


class _TpSnmpNotificationHostUDPPort_Type(Integer32):
    """Custom type tpSnmpNotificationHostUDPPort based on Integer32"""
    defaultValue = 162


_TpSnmpNotificationHostUDPPort_Object = MibTableColumn
tpSnmpNotificationHostUDPPort = _TpSnmpNotificationHostUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 3),
    _TpSnmpNotificationHostUDPPort_Type()
)
tpSnmpNotificationHostUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostUDPPort.setStatus("current")


class _TpSnmpNotificationHostSecMode_Type(Integer32):
    """Custom type tpSnmpNotificationHostSecMode based on Integer32"""
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
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_TpSnmpNotificationHostSecMode_Type.__name__ = "Integer32"
_TpSnmpNotificationHostSecMode_Object = MibTableColumn
tpSnmpNotificationHostSecMode = _TpSnmpNotificationHostSecMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 4),
    _TpSnmpNotificationHostSecMode_Type()
)
tpSnmpNotificationHostSecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostSecMode.setStatus("current")


class _TpSnmpNotificationHostSecLev_Type(Integer32):
    """Custom type tpSnmpNotificationHostSecLev based on Integer32"""
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
        *(("authNoPriv", 2),
          ("authPriv", 3),
          ("noAuthNoPriv", 1))
    )


_TpSnmpNotificationHostSecLev_Type.__name__ = "Integer32"
_TpSnmpNotificationHostSecLev_Object = MibTableColumn
tpSnmpNotificationHostSecLev = _TpSnmpNotificationHostSecLev_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 5),
    _TpSnmpNotificationHostSecLev_Type()
)
tpSnmpNotificationHostSecLev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostSecLev.setStatus("current")


class _TpSnmpNotificationHostNtfyType_Type(Integer32):
    """Custom type tpSnmpNotificationHostNtfyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inform", 2),
          ("trap", 1))
    )


_TpSnmpNotificationHostNtfyType_Type.__name__ = "Integer32"
_TpSnmpNotificationHostNtfyType_Object = MibTableColumn
tpSnmpNotificationHostNtfyType = _TpSnmpNotificationHostNtfyType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 6),
    _TpSnmpNotificationHostNtfyType_Type()
)
tpSnmpNotificationHostNtfyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostNtfyType.setStatus("current")
_TpSnmpNotificationHostRetry_Type = Integer32
_TpSnmpNotificationHostRetry_Object = MibTableColumn
tpSnmpNotificationHostRetry = _TpSnmpNotificationHostRetry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 7),
    _TpSnmpNotificationHostRetry_Type()
)
tpSnmpNotificationHostRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostRetry.setStatus("current")
_TpSnmpNotificationHostTimeout_Type = Integer32
_TpSnmpNotificationHostTimeout_Object = MibTableColumn
tpSnmpNotificationHostTimeout = _TpSnmpNotificationHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 8),
    _TpSnmpNotificationHostTimeout_Type()
)
tpSnmpNotificationHostTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostTimeout.setStatus("current")


class _TpSnmpNotificationHostRowStatus_Type(TPRowStatus):
    """Custom type tpSnmpNotificationHostRowStatus based on TPRowStatus"""
    defaultValue = 4


_TpSnmpNotificationHostRowStatus_Object = MibTableColumn
tpSnmpNotificationHostRowStatus = _TpSnmpNotificationHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 1, 1, 9),
    _TpSnmpNotificationHostRowStatus_Type()
)
tpSnmpNotificationHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostRowStatus.setStatus("current")
_TpSnmpNotificationHostV6Table_Object = MibTable
tpSnmpNotificationHostV6Table = _TpSnmpNotificationHostV6Table_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6Table.setStatus("current")
_TpSnmpNotificationHostV6Entry_Object = MibTableRow
tpSnmpNotificationHostV6Entry = _TpSnmpNotificationHostV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1)
)
tpSnmpNotificationHostV6Entry.setIndexNames(
    (0, "TPLINK-SNMPNOTIFICATIONHOST-MIB", "tpSnmpNotificationHostV6Index"),
)
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6Entry.setStatus("current")


class _TpSnmpNotificationHostV6Index_Type(Integer32):
    """Custom type tpSnmpNotificationHostV6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TpSnmpNotificationHostV6Index_Type.__name__ = "Integer32"
_TpSnmpNotificationHostV6Index_Object = MibTableColumn
tpSnmpNotificationHostV6Index = _TpSnmpNotificationHostV6Index_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 1),
    _TpSnmpNotificationHostV6Index_Type()
)
tpSnmpNotificationHostV6Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6Index.setStatus("current")
_TpSnmpNotificationHostV6IpMode_Type = InetAddressType
_TpSnmpNotificationHostV6IpMode_Object = MibTableColumn
tpSnmpNotificationHostV6IpMode = _TpSnmpNotificationHostV6IpMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 2),
    _TpSnmpNotificationHostV6IpMode_Type()
)
tpSnmpNotificationHostV6IpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6IpMode.setStatus("current")
_TpSnmpNotificationHostV6IpAddr_Type = InetAddress
_TpSnmpNotificationHostV6IpAddr_Object = MibTableColumn
tpSnmpNotificationHostV6IpAddr = _TpSnmpNotificationHostV6IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 3),
    _TpSnmpNotificationHostV6IpAddr_Type()
)
tpSnmpNotificationHostV6IpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6IpAddr.setStatus("current")


class _TpSnmpNotificationHostV6UserName_Type(OctetString):
    """Custom type tpSnmpNotificationHostV6UserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TpSnmpNotificationHostV6UserName_Type.__name__ = "OctetString"
_TpSnmpNotificationHostV6UserName_Object = MibTableColumn
tpSnmpNotificationHostV6UserName = _TpSnmpNotificationHostV6UserName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 4),
    _TpSnmpNotificationHostV6UserName_Type()
)
tpSnmpNotificationHostV6UserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6UserName.setStatus("current")


class _TpSnmpNotificationHostV6UDPPort_Type(Integer32):
    """Custom type tpSnmpNotificationHostV6UDPPort based on Integer32"""
    defaultValue = 162


_TpSnmpNotificationHostV6UDPPort_Object = MibTableColumn
tpSnmpNotificationHostV6UDPPort = _TpSnmpNotificationHostV6UDPPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 5),
    _TpSnmpNotificationHostV6UDPPort_Type()
)
tpSnmpNotificationHostV6UDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6UDPPort.setStatus("current")


class _TpSnmpNotificationHostV6SecMode_Type(Integer32):
    """Custom type tpSnmpNotificationHostV6SecMode based on Integer32"""
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
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_TpSnmpNotificationHostV6SecMode_Type.__name__ = "Integer32"
_TpSnmpNotificationHostV6SecMode_Object = MibTableColumn
tpSnmpNotificationHostV6SecMode = _TpSnmpNotificationHostV6SecMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 6),
    _TpSnmpNotificationHostV6SecMode_Type()
)
tpSnmpNotificationHostV6SecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6SecMode.setStatus("current")


class _TpSnmpNotificationHostV6SecLev_Type(Integer32):
    """Custom type tpSnmpNotificationHostV6SecLev based on Integer32"""
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
        *(("authNoPriv", 2),
          ("authPriv", 3),
          ("noAuthNoPriv", 1))
    )


_TpSnmpNotificationHostV6SecLev_Type.__name__ = "Integer32"
_TpSnmpNotificationHostV6SecLev_Object = MibTableColumn
tpSnmpNotificationHostV6SecLev = _TpSnmpNotificationHostV6SecLev_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 7),
    _TpSnmpNotificationHostV6SecLev_Type()
)
tpSnmpNotificationHostV6SecLev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6SecLev.setStatus("current")


class _TpSnmpNotificationHostV6NtfyType_Type(Integer32):
    """Custom type tpSnmpNotificationHostV6NtfyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inform", 2),
          ("trap", 1))
    )


_TpSnmpNotificationHostV6NtfyType_Type.__name__ = "Integer32"
_TpSnmpNotificationHostV6NtfyType_Object = MibTableColumn
tpSnmpNotificationHostV6NtfyType = _TpSnmpNotificationHostV6NtfyType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 8),
    _TpSnmpNotificationHostV6NtfyType_Type()
)
tpSnmpNotificationHostV6NtfyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6NtfyType.setStatus("current")
_TpSnmpNotificationHostV6Retry_Type = Integer32
_TpSnmpNotificationHostV6Retry_Object = MibTableColumn
tpSnmpNotificationHostV6Retry = _TpSnmpNotificationHostV6Retry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 9),
    _TpSnmpNotificationHostV6Retry_Type()
)
tpSnmpNotificationHostV6Retry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6Retry.setStatus("current")
_TpSnmpNotificationHostV6Timeout_Type = Integer32
_TpSnmpNotificationHostV6Timeout_Object = MibTableColumn
tpSnmpNotificationHostV6Timeout = _TpSnmpNotificationHostV6Timeout_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 10),
    _TpSnmpNotificationHostV6Timeout_Type()
)
tpSnmpNotificationHostV6Timeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6Timeout.setStatus("current")


class _TpSnmpNotificationHostV6RowStatus_Type(TPRowStatus):
    """Custom type tpSnmpNotificationHostV6RowStatus based on TPRowStatus"""
    defaultValue = 4


_TpSnmpNotificationHostV6RowStatus_Object = MibTableColumn
tpSnmpNotificationHostV6RowStatus = _TpSnmpNotificationHostV6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 32, 1, 1, 2, 1, 11),
    _TpSnmpNotificationHostV6RowStatus_Type()
)
tpSnmpNotificationHostV6RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSnmpNotificationHostV6RowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SNMPNOTIFICATIONHOST-MIB",
    **{"tpSnmpNotificationHost": tpSnmpNotificationHost,
       "tpSnmpNotificationHostTable": tpSnmpNotificationHostTable,
       "tpSnmpNotificationHostEntry": tpSnmpNotificationHostEntry,
       "tpSnmpNotificationHostIpAddr": tpSnmpNotificationHostIpAddr,
       "tpSnmpNotificationHostUserName": tpSnmpNotificationHostUserName,
       "tpSnmpNotificationHostUDPPort": tpSnmpNotificationHostUDPPort,
       "tpSnmpNotificationHostSecMode": tpSnmpNotificationHostSecMode,
       "tpSnmpNotificationHostSecLev": tpSnmpNotificationHostSecLev,
       "tpSnmpNotificationHostNtfyType": tpSnmpNotificationHostNtfyType,
       "tpSnmpNotificationHostRetry": tpSnmpNotificationHostRetry,
       "tpSnmpNotificationHostTimeout": tpSnmpNotificationHostTimeout,
       "tpSnmpNotificationHostRowStatus": tpSnmpNotificationHostRowStatus,
       "tpSnmpNotificationHostV6Table": tpSnmpNotificationHostV6Table,
       "tpSnmpNotificationHostV6Entry": tpSnmpNotificationHostV6Entry,
       "tpSnmpNotificationHostV6Index": tpSnmpNotificationHostV6Index,
       "tpSnmpNotificationHostV6IpMode": tpSnmpNotificationHostV6IpMode,
       "tpSnmpNotificationHostV6IpAddr": tpSnmpNotificationHostV6IpAddr,
       "tpSnmpNotificationHostV6UserName": tpSnmpNotificationHostV6UserName,
       "tpSnmpNotificationHostV6UDPPort": tpSnmpNotificationHostV6UDPPort,
       "tpSnmpNotificationHostV6SecMode": tpSnmpNotificationHostV6SecMode,
       "tpSnmpNotificationHostV6SecLev": tpSnmpNotificationHostV6SecLev,
       "tpSnmpNotificationHostV6NtfyType": tpSnmpNotificationHostV6NtfyType,
       "tpSnmpNotificationHostV6Retry": tpSnmpNotificationHostV6Retry,
       "tpSnmpNotificationHostV6Timeout": tpSnmpNotificationHostV6Timeout,
       "tpSnmpNotificationHostV6RowStatus": tpSnmpNotificationHostV6RowStatus}
)
