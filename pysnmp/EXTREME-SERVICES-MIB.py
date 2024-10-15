# SNMP MIB module (EXTREME-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeServices = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AuthServerType(Integer32, TextualConvention):
    status = "current"
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
        *(("radius", 1),
          ("radius-acct", 2),
          ("tacacs", 3),
          ("tacacs-acct", 4))
    )



class AuthServerAccessType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgmt-access", 1),
          ("netlogin", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeSyslog_ObjectIdentity = ObjectIdentity
extremeSyslog = _ExtremeSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 1)
)
_ExtremeRemoteSyslogServerTable_Object = MibTable
extremeRemoteSyslogServerTable = _ExtremeRemoteSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 1, 1)
)
if mibBuilder.loadTexts:
    extremeRemoteSyslogServerTable.setStatus("current")
_ExtremeRemoteSyslogServerEntry_Object = MibTableRow
extremeRemoteSyslogServerEntry = _ExtremeRemoteSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 1, 1, 1)
)
extremeRemoteSyslogServerEntry.setIndexNames(
    (0, "EXTREME-SERVICES-MIB", "extremeRemoteSyslogServerAddressType"),
    (0, "EXTREME-SERVICES-MIB", "extremeRemoteSyslogServerAddress"),
    (0, "EXTREME-SERVICES-MIB", "extremeRemoteSyslogServerPort"),
    (0, "EXTREME-SERVICES-MIB", "extremeRemoteSyslogServerFacility"),
)
if mibBuilder.loadTexts:
    extremeRemoteSyslogServerEntry.setStatus("current")


class _ExtremeRemoteSyslogServerAddressType_Type(InetAddressType):
    """Custom type extremeRemoteSyslogServerAddressType based on InetAddressType"""


_ExtremeRemoteSyslogServerAddressType_Object = MibTableColumn
extremeRemoteSyslogServerAddressType = _ExtremeRemoteSyslogServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 1, 1, 1, 1),
    _ExtremeRemoteSyslogServerAddressType_Type()
)
extremeRemoteSyslogServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRemoteSyslogServerAddressType.setStatus("current")


class _ExtremeRemoteSyslogServerAddress_Type(InetAddress):
    """Custom type extremeRemoteSyslogServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ExtremeRemoteSyslogServerAddress_Type.__name__ = "InetAddress"
_ExtremeRemoteSyslogServerAddress_Object = MibTableColumn
extremeRemoteSyslogServerAddress = _ExtremeRemoteSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 1, 1, 1, 2),
    _ExtremeRemoteSyslogServerAddress_Type()
)
extremeRemoteSyslogServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRemoteSyslogServerAddress.setStatus("current")


class _ExtremeRemoteSyslogServerPort_Type(Integer32):
    """Custom type extremeRemoteSyslogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeRemoteSyslogServerPort_Type.__name__ = "Integer32"
_ExtremeRemoteSyslogServerPort_Object = MibTableColumn
extremeRemoteSyslogServerPort = _ExtremeRemoteSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 1, 1, 1, 3),
    _ExtremeRemoteSyslogServerPort_Type()
)
extremeRemoteSyslogServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRemoteSyslogServerPort.setStatus("current")


class _ExtremeRemoteSyslogServerFacility_Type(Integer32):
    """Custom type extremeRemoteSyslogServerFacility based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_ExtremeRemoteSyslogServerFacility_Type.__name__ = "Integer32"
_ExtremeRemoteSyslogServerFacility_Object = MibTableColumn
extremeRemoteSyslogServerFacility = _ExtremeRemoteSyslogServerFacility_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 1, 1, 1, 4),
    _ExtremeRemoteSyslogServerFacility_Type()
)
extremeRemoteSyslogServerFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeRemoteSyslogServerFacility.setStatus("current")


class _ExtremeRemoteSyslogServerSeverity_Type(Bits):
    """Custom type extremeRemoteSyslogServerSeverity based on Bits"""
    defaultHexValue = "ff"

    namedValues = NamedValues(
        *(("critical", 0),
          ("debugData", 7),
          ("debugSummary", 5),
          ("debugVerbose", 6),
          ("error", 1),
          ("info", 4),
          ("notice", 3),
          ("warning", 2))
    )

_ExtremeRemoteSyslogServerSeverity_Type.__name__ = "Bits"
_ExtremeRemoteSyslogServerSeverity_Object = MibTableColumn
extremeRemoteSyslogServerSeverity = _ExtremeRemoteSyslogServerSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 1, 1, 1, 5),
    _ExtremeRemoteSyslogServerSeverity_Type()
)
extremeRemoteSyslogServerSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRemoteSyslogServerSeverity.setStatus("current")
_ExtremeRemoteSyslogServerStatus_Type = RowStatus
_ExtremeRemoteSyslogServerStatus_Object = MibTableColumn
extremeRemoteSyslogServerStatus = _ExtremeRemoteSyslogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 1, 1, 1, 6),
    _ExtremeRemoteSyslogServerStatus_Type()
)
extremeRemoteSyslogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeRemoteSyslogServerStatus.setStatus("current")
_ExtremeEnableRemoteSyslog_Type = TruthValue
_ExtremeEnableRemoteSyslog_Object = MibScalar
extremeEnableRemoteSyslog = _ExtremeEnableRemoteSyslog_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 1, 2),
    _ExtremeEnableRemoteSyslog_Type()
)
extremeEnableRemoteSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEnableRemoteSyslog.setStatus("current")
_ExtremeDNS_ObjectIdentity = ObjectIdentity
extremeDNS = _ExtremeDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 3)
)
_ExtremeDNSServerTable_Object = MibTable
extremeDNSServerTable = _ExtremeDNSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 3, 1)
)
if mibBuilder.loadTexts:
    extremeDNSServerTable.setStatus("current")
_ExtremeDNSServerEntry_Object = MibTableRow
extremeDNSServerEntry = _ExtremeDNSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 3, 1, 1)
)
extremeDNSServerEntry.setIndexNames(
    (0, "EXTREME-SERVICES-MIB", "extremeDNSServerAddressIndex"),
)
if mibBuilder.loadTexts:
    extremeDNSServerEntry.setStatus("current")
_ExtremeDNSServerAddressIndex_Type = Integer32
_ExtremeDNSServerAddressIndex_Object = MibTableColumn
extremeDNSServerAddressIndex = _ExtremeDNSServerAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 3, 1, 1, 1),
    _ExtremeDNSServerAddressIndex_Type()
)
extremeDNSServerAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeDNSServerAddressIndex.setStatus("current")
_ExtremeDNSServerAddressType_Type = InetAddressType
_ExtremeDNSServerAddressType_Object = MibTableColumn
extremeDNSServerAddressType = _ExtremeDNSServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 3, 1, 1, 2),
    _ExtremeDNSServerAddressType_Type()
)
extremeDNSServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDNSServerAddressType.setStatus("current")


class _ExtremeDNSServerAddress_Type(InetAddress):
    """Custom type extremeDNSServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ExtremeDNSServerAddress_Type.__name__ = "InetAddress"
_ExtremeDNSServerAddress_Object = MibTableColumn
extremeDNSServerAddress = _ExtremeDNSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 3, 1, 1, 3),
    _ExtremeDNSServerAddress_Type()
)
extremeDNSServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDNSServerAddress.setStatus("current")
_ExtremeAuthServer_ObjectIdentity = ObjectIdentity
extremeAuthServer = _ExtremeAuthServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4)
)
_ExtremeAuthServerEnableTable_Object = MibTable
extremeAuthServerEnableTable = _ExtremeAuthServerEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 1)
)
if mibBuilder.loadTexts:
    extremeAuthServerEnableTable.setStatus("current")
_ExtremeAuthServerEnableEntry_Object = MibTableRow
extremeAuthServerEnableEntry = _ExtremeAuthServerEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 1, 1)
)
extremeAuthServerEnableEntry.setIndexNames(
    (0, "EXTREME-SERVICES-MIB", "extremeAuthServerEnableServerType"),
    (0, "EXTREME-SERVICES-MIB", "extremeAuthServerEnableAccessType"),
)
if mibBuilder.loadTexts:
    extremeAuthServerEnableEntry.setStatus("current")
_ExtremeAuthServerEnableServerType_Type = AuthServerType
_ExtremeAuthServerEnableServerType_Object = MibTableColumn
extremeAuthServerEnableServerType = _ExtremeAuthServerEnableServerType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 1, 1, 1),
    _ExtremeAuthServerEnableServerType_Type()
)
extremeAuthServerEnableServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeAuthServerEnableServerType.setStatus("current")
_ExtremeAuthServerEnableAccessType_Type = AuthServerAccessType
_ExtremeAuthServerEnableAccessType_Object = MibTableColumn
extremeAuthServerEnableAccessType = _ExtremeAuthServerEnableAccessType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 1, 1, 2),
    _ExtremeAuthServerEnableAccessType_Type()
)
extremeAuthServerEnableAccessType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeAuthServerEnableAccessType.setStatus("current")


class _ExtremeAuthServerEnable_Type(TruthValue):
    """Custom type extremeAuthServerEnable based on TruthValue"""


_ExtremeAuthServerEnable_Object = MibTableColumn
extremeAuthServerEnable = _ExtremeAuthServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 1, 1, 3),
    _ExtremeAuthServerEnable_Type()
)
extremeAuthServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerEnable.setStatus("current")
_ExtremeAuthServerTable_Object = MibTable
extremeAuthServerTable = _ExtremeAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2)
)
if mibBuilder.loadTexts:
    extremeAuthServerTable.setStatus("current")
_ExtremeAuthServerEntry_Object = MibTableRow
extremeAuthServerEntry = _ExtremeAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1)
)
extremeAuthServerEntry.setIndexNames(
    (0, "EXTREME-SERVICES-MIB", "extremeAuthServerIndex"),
)
if mibBuilder.loadTexts:
    extremeAuthServerEntry.setStatus("current")


class _ExtremeAuthServerIndex_Type(Integer32):
    """Custom type extremeAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ExtremeAuthServerIndex_Type.__name__ = "Integer32"
_ExtremeAuthServerIndex_Object = MibTableColumn
extremeAuthServerIndex = _ExtremeAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 1),
    _ExtremeAuthServerIndex_Type()
)
extremeAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeAuthServerIndex.setStatus("current")
_ExtremeAuthServerAddressType_Type = InetAddressType
_ExtremeAuthServerAddressType_Object = MibTableColumn
extremeAuthServerAddressType = _ExtremeAuthServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 2),
    _ExtremeAuthServerAddressType_Type()
)
extremeAuthServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerAddressType.setStatus("current")
_ExtremeAuthServerAddress_Type = InetAddress
_ExtremeAuthServerAddress_Object = MibTableColumn
extremeAuthServerAddress = _ExtremeAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 3),
    _ExtremeAuthServerAddress_Type()
)
extremeAuthServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerAddress.setStatus("current")
_ExtremeAuthServerClientAddressType_Type = InetAddressType
_ExtremeAuthServerClientAddressType_Object = MibTableColumn
extremeAuthServerClientAddressType = _ExtremeAuthServerClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 4),
    _ExtremeAuthServerClientAddressType_Type()
)
extremeAuthServerClientAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerClientAddressType.setStatus("current")
_ExtremeAuthServerClientAddress_Type = InetAddress
_ExtremeAuthServerClientAddress_Object = MibTableColumn
extremeAuthServerClientAddress = _ExtremeAuthServerClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 5),
    _ExtremeAuthServerClientAddress_Type()
)
extremeAuthServerClientAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerClientAddress.setStatus("current")
_ExtremeAuthServerPort_Type = Integer32
_ExtremeAuthServerPort_Object = MibTableColumn
extremeAuthServerPort = _ExtremeAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 6),
    _ExtremeAuthServerPort_Type()
)
extremeAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerPort.setStatus("current")
_ExtremeAuthServerSecret_Type = OctetString
_ExtremeAuthServerSecret_Object = MibTableColumn
extremeAuthServerSecret = _ExtremeAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 7),
    _ExtremeAuthServerSecret_Type()
)
extremeAuthServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerSecret.setStatus("current")
_ExtremeAuthServerReTransmit_Type = Integer32
_ExtremeAuthServerReTransmit_Object = MibTableColumn
extremeAuthServerReTransmit = _ExtremeAuthServerReTransmit_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 8),
    _ExtremeAuthServerReTransmit_Type()
)
extremeAuthServerReTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerReTransmit.setStatus("current")
_ExtremeAuthServerType_Type = AuthServerType
_ExtremeAuthServerType_Object = MibTableColumn
extremeAuthServerType = _ExtremeAuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 9),
    _ExtremeAuthServerType_Type()
)
extremeAuthServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerType.setStatus("current")
_ExtremeAuthServerIsPrimary_Type = TruthValue
_ExtremeAuthServerIsPrimary_Object = MibTableColumn
extremeAuthServerIsPrimary = _ExtremeAuthServerIsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 10),
    _ExtremeAuthServerIsPrimary_Type()
)
extremeAuthServerIsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerIsPrimary.setStatus("current")
_ExtremeAuthServerAccessType_Type = AuthServerAccessType
_ExtremeAuthServerAccessType_Object = MibTableColumn
extremeAuthServerAccessType = _ExtremeAuthServerAccessType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 11),
    _ExtremeAuthServerAccessType_Type()
)
extremeAuthServerAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeAuthServerAccessType.setStatus("current")
_ExtremeAuthServerStatus_Type = RowStatus
_ExtremeAuthServerStatus_Object = MibTableColumn
extremeAuthServerStatus = _ExtremeAuthServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26, 4, 2, 1, 12),
    _ExtremeAuthServerStatus_Type()
)
extremeAuthServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeAuthServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-SERVICES-MIB",
    **{"AuthServerType": AuthServerType,
       "AuthServerAccessType": AuthServerAccessType,
       "extremeServices": extremeServices,
       "extremeSyslog": extremeSyslog,
       "extremeRemoteSyslogServerTable": extremeRemoteSyslogServerTable,
       "extremeRemoteSyslogServerEntry": extremeRemoteSyslogServerEntry,
       "extremeRemoteSyslogServerAddressType": extremeRemoteSyslogServerAddressType,
       "extremeRemoteSyslogServerAddress": extremeRemoteSyslogServerAddress,
       "extremeRemoteSyslogServerPort": extremeRemoteSyslogServerPort,
       "extremeRemoteSyslogServerFacility": extremeRemoteSyslogServerFacility,
       "extremeRemoteSyslogServerSeverity": extremeRemoteSyslogServerSeverity,
       "extremeRemoteSyslogServerStatus": extremeRemoteSyslogServerStatus,
       "extremeEnableRemoteSyslog": extremeEnableRemoteSyslog,
       "extremeDNS": extremeDNS,
       "extremeDNSServerTable": extremeDNSServerTable,
       "extremeDNSServerEntry": extremeDNSServerEntry,
       "extremeDNSServerAddressIndex": extremeDNSServerAddressIndex,
       "extremeDNSServerAddressType": extremeDNSServerAddressType,
       "extremeDNSServerAddress": extremeDNSServerAddress,
       "extremeAuthServer": extremeAuthServer,
       "extremeAuthServerEnableTable": extremeAuthServerEnableTable,
       "extremeAuthServerEnableEntry": extremeAuthServerEnableEntry,
       "extremeAuthServerEnableServerType": extremeAuthServerEnableServerType,
       "extremeAuthServerEnableAccessType": extremeAuthServerEnableAccessType,
       "extremeAuthServerEnable": extremeAuthServerEnable,
       "extremeAuthServerTable": extremeAuthServerTable,
       "extremeAuthServerEntry": extremeAuthServerEntry,
       "extremeAuthServerIndex": extremeAuthServerIndex,
       "extremeAuthServerAddressType": extremeAuthServerAddressType,
       "extremeAuthServerAddress": extremeAuthServerAddress,
       "extremeAuthServerClientAddressType": extremeAuthServerClientAddressType,
       "extremeAuthServerClientAddress": extremeAuthServerClientAddress,
       "extremeAuthServerPort": extremeAuthServerPort,
       "extremeAuthServerSecret": extremeAuthServerSecret,
       "extremeAuthServerReTransmit": extremeAuthServerReTransmit,
       "extremeAuthServerType": extremeAuthServerType,
       "extremeAuthServerIsPrimary": extremeAuthServerIsPrimary,
       "extremeAuthServerAccessType": extremeAuthServerAccessType,
       "extremeAuthServerStatus": extremeAuthServerStatus}
)
