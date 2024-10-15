# SNMP MIB module (WWP-LEOS-DNS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-DNS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:50 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosDnsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16)
)
wwpLeosDnsClientMIB.setRevisions(
        ("2012-03-20 07:00",
         "2003-03-19 10:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosDnsClientMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosDnsClientMIBObjects = _WwpLeosDnsClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1)
)
_WwpLeosDnsClient_ObjectIdentity = ObjectIdentity
wwpLeosDnsClient = _WwpLeosDnsClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1)
)


class _WwpLeosDnsClientStatus_Type(Integer32):
    """Custom type wwpLeosDnsClientStatus based on Integer32"""
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


_WwpLeosDnsClientStatus_Type.__name__ = "Integer32"
_WwpLeosDnsClientStatus_Object = MibScalar
wwpLeosDnsClientStatus = _WwpLeosDnsClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 1),
    _WwpLeosDnsClientStatus_Type()
)
wwpLeosDnsClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDnsClientStatus.setStatus("current")
_WwpLeosDnsClientDhcpDomainName_Type = DisplayString
_WwpLeosDnsClientDhcpDomainName_Object = MibScalar
wwpLeosDnsClientDhcpDomainName = _WwpLeosDnsClientDhcpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 2),
    _WwpLeosDnsClientDhcpDomainName_Type()
)
wwpLeosDnsClientDhcpDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDnsClientDhcpDomainName.setStatus("current")


class _WwpLeosDnsClientDhcpDomainNameState_Type(Integer32):
    """Custom type wwpLeosDnsClientDhcpDomainNameState based on Integer32"""
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


_WwpLeosDnsClientDhcpDomainNameState_Type.__name__ = "Integer32"
_WwpLeosDnsClientDhcpDomainNameState_Object = MibScalar
wwpLeosDnsClientDhcpDomainNameState = _WwpLeosDnsClientDhcpDomainNameState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 3),
    _WwpLeosDnsClientDhcpDomainNameState_Type()
)
wwpLeosDnsClientDhcpDomainNameState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDnsClientDhcpDomainNameState.setStatus("current")
_WwpLeosDnsClientUserDomainName_Type = DisplayString
_WwpLeosDnsClientUserDomainName_Object = MibScalar
wwpLeosDnsClientUserDomainName = _WwpLeosDnsClientUserDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 4),
    _WwpLeosDnsClientUserDomainName_Type()
)
wwpLeosDnsClientUserDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDnsClientUserDomainName.setStatus("current")


class _WwpLeosDnsClientUserDomainNameState_Type(Integer32):
    """Custom type wwpLeosDnsClientUserDomainNameState based on Integer32"""
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


_WwpLeosDnsClientUserDomainNameState_Type.__name__ = "Integer32"
_WwpLeosDnsClientUserDomainNameState_Object = MibScalar
wwpLeosDnsClientUserDomainNameState = _WwpLeosDnsClientUserDomainNameState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 5),
    _WwpLeosDnsClientUserDomainNameState_Type()
)
wwpLeosDnsClientUserDomainNameState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDnsClientUserDomainNameState.setStatus("current")
_WwpLeosDnsServerTable_Object = MibTable
wwpLeosDnsServerTable = _WwpLeosDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosDnsServerTable.setStatus("current")
_WwpLeosDnsServerEntry_Object = MibTableRow
wwpLeosDnsServerEntry = _WwpLeosDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 6, 1)
)
wwpLeosDnsServerEntry.setIndexNames(
    (0, "WWP-LEOS-DNS-CLIENT-MIB", "wwpLeosDnsServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosDnsServerEntry.setStatus("current")


class _WwpLeosDnsServerIndex_Type(Integer32):
    """Custom type wwpLeosDnsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosDnsServerIndex_Type.__name__ = "Integer32"
_WwpLeosDnsServerIndex_Object = MibTableColumn
wwpLeosDnsServerIndex = _WwpLeosDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 6, 1, 1),
    _WwpLeosDnsServerIndex_Type()
)
wwpLeosDnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosDnsServerIndex.setStatus("current")
_WwpLeosDnsServerAddr_Type = IpAddress
_WwpLeosDnsServerAddr_Object = MibTableColumn
wwpLeosDnsServerAddr = _WwpLeosDnsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 6, 1, 2),
    _WwpLeosDnsServerAddr_Type()
)
wwpLeosDnsServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDnsServerAddr.setStatus("current")


class _WwpLeosDnsServerUserPriority_Type(Integer32):
    """Custom type wwpLeosDnsServerUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosDnsServerUserPriority_Type.__name__ = "Integer32"
_WwpLeosDnsServerUserPriority_Object = MibTableColumn
wwpLeosDnsServerUserPriority = _WwpLeosDnsServerUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 6, 1, 3),
    _WwpLeosDnsServerUserPriority_Type()
)
wwpLeosDnsServerUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDnsServerUserPriority.setStatus("current")


class _WwpLeosDnsServerDhcpPriority_Type(Integer32):
    """Custom type wwpLeosDnsServerDhcpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosDnsServerDhcpPriority_Type.__name__ = "Integer32"
_WwpLeosDnsServerDhcpPriority_Object = MibTableColumn
wwpLeosDnsServerDhcpPriority = _WwpLeosDnsServerDhcpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 6, 1, 4),
    _WwpLeosDnsServerDhcpPriority_Type()
)
wwpLeosDnsServerDhcpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDnsServerDhcpPriority.setStatus("current")


class _WwpLeosDnsServerScope_Type(Integer32):
    """Custom type wwpLeosDnsServerScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("dhcp", 2),
          ("user", 1))
    )


_WwpLeosDnsServerScope_Type.__name__ = "Integer32"
_WwpLeosDnsServerScope_Object = MibTableColumn
wwpLeosDnsServerScope = _WwpLeosDnsServerScope_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 6, 1, 5),
    _WwpLeosDnsServerScope_Type()
)
wwpLeosDnsServerScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDnsServerScope.setStatus("current")
_WwpLeosDnsServerStatus_Type = RowStatus
_WwpLeosDnsServerStatus_Object = MibTableColumn
wwpLeosDnsServerStatus = _WwpLeosDnsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 6, 1, 6),
    _WwpLeosDnsServerStatus_Type()
)
wwpLeosDnsServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosDnsServerStatus.setStatus("current")
_WwpLeosDnsServerInetAddrType_Type = InetAddressType
_WwpLeosDnsServerInetAddrType_Object = MibTableColumn
wwpLeosDnsServerInetAddrType = _WwpLeosDnsServerInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 6, 1, 7),
    _WwpLeosDnsServerInetAddrType_Type()
)
wwpLeosDnsServerInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDnsServerInetAddrType.setStatus("current")
_WwpLeosDnsServerInetAddr_Type = InetAddress
_WwpLeosDnsServerInetAddr_Object = MibTableColumn
wwpLeosDnsServerInetAddr = _WwpLeosDnsServerInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 6, 1, 8),
    _WwpLeosDnsServerInetAddr_Type()
)
wwpLeosDnsServerInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDnsServerInetAddr.setStatus("current")
_WwpLeosDnsServerExtTable_Object = MibTable
wwpLeosDnsServerExtTable = _WwpLeosDnsServerExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wwpLeosDnsServerExtTable.setStatus("current")
_WwpLeosDnsServerExtEntry_Object = MibTableRow
wwpLeosDnsServerExtEntry = _WwpLeosDnsServerExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 7, 1)
)
wwpLeosDnsServerExtEntry.setIndexNames(
    (0, "WWP-LEOS-DNS-CLIENT-MIB", "wwpLeosDnsServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosDnsServerExtEntry.setStatus("current")


class _WwpLeosDnsServerAdminState_Type(Integer32):
    """Custom type wwpLeosDnsServerAdminState based on Integer32"""
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


_WwpLeosDnsServerAdminState_Type.__name__ = "Integer32"
_WwpLeosDnsServerAdminState_Object = MibTableColumn
wwpLeosDnsServerAdminState = _WwpLeosDnsServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 7, 1, 1),
    _WwpLeosDnsServerAdminState_Type()
)
wwpLeosDnsServerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosDnsServerAdminState.setStatus("current")


class _WwpLeosDnsServerOperState_Type(Integer32):
    """Custom type wwpLeosDnsServerOperState based on Integer32"""
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


_WwpLeosDnsServerOperState_Type.__name__ = "Integer32"
_WwpLeosDnsServerOperState_Object = MibTableColumn
wwpLeosDnsServerOperState = _WwpLeosDnsServerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 1, 1, 7, 1, 2),
    _WwpLeosDnsServerOperState_Type()
)
wwpLeosDnsServerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosDnsServerOperState.setStatus("current")
_WwpLeosDnsClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosDnsClientMIBNotificationPrefix = _WwpLeosDnsClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 2)
)
_WwpLeosDnsClientMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosDnsClientMIBNotifications = _WwpLeosDnsClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 2, 0)
)
_WwpLeosDnsClientMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosDnsClientMIBConformance = _WwpLeosDnsClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 3)
)
_WwpLeosDnsClientMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosDnsClientMIBCompliances = _WwpLeosDnsClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 3, 1)
)
_WwpLeosDnsClientMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosDnsClientMIBGroups = _WwpLeosDnsClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 3, 2)
)

# Managed Objects groups

wwpLeosDnsServerEntryIpv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 3, 2, 1)
)
wwpLeosDnsServerEntryIpv6Group.setObjects(
      *(("WWP-LEOS-DNS-CLIENT-MIB", "wwpLeosDnsServerInetAddrType"),
        ("WWP-LEOS-DNS-CLIENT-MIB", "wwpLeosDnsServerInetAddr"))
)
if mibBuilder.loadTexts:
    wwpLeosDnsServerEntryIpv6Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wwpLeosDnsServerEntryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 16, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosDnsServerEntryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-DNS-CLIENT-MIB",
    **{"wwpLeosDnsClientMIB": wwpLeosDnsClientMIB,
       "wwpLeosDnsClientMIBObjects": wwpLeosDnsClientMIBObjects,
       "wwpLeosDnsClient": wwpLeosDnsClient,
       "wwpLeosDnsClientStatus": wwpLeosDnsClientStatus,
       "wwpLeosDnsClientDhcpDomainName": wwpLeosDnsClientDhcpDomainName,
       "wwpLeosDnsClientDhcpDomainNameState": wwpLeosDnsClientDhcpDomainNameState,
       "wwpLeosDnsClientUserDomainName": wwpLeosDnsClientUserDomainName,
       "wwpLeosDnsClientUserDomainNameState": wwpLeosDnsClientUserDomainNameState,
       "wwpLeosDnsServerTable": wwpLeosDnsServerTable,
       "wwpLeosDnsServerEntry": wwpLeosDnsServerEntry,
       "wwpLeosDnsServerIndex": wwpLeosDnsServerIndex,
       "wwpLeosDnsServerAddr": wwpLeosDnsServerAddr,
       "wwpLeosDnsServerUserPriority": wwpLeosDnsServerUserPriority,
       "wwpLeosDnsServerDhcpPriority": wwpLeosDnsServerDhcpPriority,
       "wwpLeosDnsServerScope": wwpLeosDnsServerScope,
       "wwpLeosDnsServerStatus": wwpLeosDnsServerStatus,
       "wwpLeosDnsServerInetAddrType": wwpLeosDnsServerInetAddrType,
       "wwpLeosDnsServerInetAddr": wwpLeosDnsServerInetAddr,
       "wwpLeosDnsServerExtTable": wwpLeosDnsServerExtTable,
       "wwpLeosDnsServerExtEntry": wwpLeosDnsServerExtEntry,
       "wwpLeosDnsServerAdminState": wwpLeosDnsServerAdminState,
       "wwpLeosDnsServerOperState": wwpLeosDnsServerOperState,
       "wwpLeosDnsClientMIBNotificationPrefix": wwpLeosDnsClientMIBNotificationPrefix,
       "wwpLeosDnsClientMIBNotifications": wwpLeosDnsClientMIBNotifications,
       "wwpLeosDnsClientMIBConformance": wwpLeosDnsClientMIBConformance,
       "wwpLeosDnsClientMIBCompliances": wwpLeosDnsClientMIBCompliances,
       "wwpLeosDnsServerEntryCompliance": wwpLeosDnsServerEntryCompliance,
       "wwpLeosDnsClientMIBGroups": wwpLeosDnsClientMIBGroups,
       "wwpLeosDnsServerEntryIpv6Group": wwpLeosDnsServerEntryIpv6Group}
)
