# SNMP MIB module (APDNSALG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APDNSALG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:14 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(ApHardwareModuleFamily,
 ApRedundancyState,
 ApTransportType) = mibBuilder.importSymbols(
    "ACMEPACKET-TC",
    "ApHardwareModuleFamily",
    "ApRedundancyState",
    "ApTransportType")

(SysMgmtPercentage,) = mibBuilder.importSymbols(
    "APSYSMGMT-MIB",
    "SysMgmtPercentage")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion",
    "InetZoneIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

apDNSALGModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApDNSALGMIBObjects_ObjectIdentity = ObjectIdentity
apDNSALGMIBObjects = _ApDNSALGMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1)
)
_ApDNSALGMIBGeneralObjects_ObjectIdentity = ObjectIdentity
apDNSALGMIBGeneralObjects = _ApDNSALGMIBGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 1)
)
_ApDNSALGMIBTabularObjects_ObjectIdentity = ObjectIdentity
apDNSALGMIBTabularObjects = _ApDNSALGMIBTabularObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2)
)
_ApDNSALGServerStatusTable_Object = MibTable
apDNSALGServerStatusTable = _ApDNSALGServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apDNSALGServerStatusTable.setStatus("current")
_ApDNSALGServerStatusEntry_Object = MibTableRow
apDNSALGServerStatusEntry = _ApDNSALGServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1)
)
apDNSALGServerStatusEntry.setIndexNames(
    (0, "APDNSALG-MIB", "apDNSALGConfigIndex"),
    (0, "APDNSALG-MIB", "apDNSALGServerIndex"),
    (0, "APDNSALG-MIB", "apDNSALGServerIpAddress"),
)
if mibBuilder.loadTexts:
    apDNSALGServerStatusEntry.setStatus("current")


class _ApDNSALGConfigIndex_Type(Integer32):
    """Custom type apDNSALGConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApDNSALGConfigIndex_Type.__name__ = "Integer32"
_ApDNSALGConfigIndex_Object = MibTableColumn
apDNSALGConfigIndex = _ApDNSALGConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 1),
    _ApDNSALGConfigIndex_Type()
)
apDNSALGConfigIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDNSALGConfigIndex.setStatus("current")


class _ApDNSALGServerIndex_Type(Integer32):
    """Custom type apDNSALGServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApDNSALGServerIndex_Type.__name__ = "Integer32"
_ApDNSALGServerIndex_Object = MibTableColumn
apDNSALGServerIndex = _ApDNSALGServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 2),
    _ApDNSALGServerIndex_Type()
)
apDNSALGServerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDNSALGServerIndex.setStatus("current")


class _ApDNSALGConfigName_Type(DisplayString):
    """Custom type apDNSALGConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApDNSALGConfigName_Type.__name__ = "DisplayString"
_ApDNSALGConfigName_Object = MibTableColumn
apDNSALGConfigName = _ApDNSALGConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 4),
    _ApDNSALGConfigName_Type()
)
apDNSALGConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDNSALGConfigName.setStatus("current")


class _ApDNSALGServerRealm_Type(DisplayString):
    """Custom type apDNSALGServerRealm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApDNSALGServerRealm_Type.__name__ = "DisplayString"
_ApDNSALGServerRealm_Object = MibTableColumn
apDNSALGServerRealm = _ApDNSALGServerRealm_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 5),
    _ApDNSALGServerRealm_Type()
)
apDNSALGServerRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDNSALGServerRealm.setStatus("current")


class _ApDNSALGDomainSuffix_Type(DisplayString):
    """Custom type apDNSALGDomainSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApDNSALGDomainSuffix_Type.__name__ = "DisplayString"
_ApDNSALGDomainSuffix_Object = MibTableColumn
apDNSALGDomainSuffix = _ApDNSALGDomainSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 6),
    _ApDNSALGDomainSuffix_Type()
)
apDNSALGDomainSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDNSALGDomainSuffix.setStatus("current")
_ApDNSALGServerIpAddress_Type = IpAddress
_ApDNSALGServerIpAddress_Object = MibTableColumn
apDNSALGServerIpAddress = _ApDNSALGServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 7),
    _ApDNSALGServerIpAddress_Type()
)
apDNSALGServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDNSALGServerIpAddress.setStatus("current")


class _ApDNSALGServerStatus_Type(Integer32):
    """Custom type apDNSALGServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inservice", 0),
          ("lowerpriority", 1),
          ("oosunreachable", 2))
    )


_ApDNSALGServerStatus_Type.__name__ = "Integer32"
_ApDNSALGServerStatus_Object = MibTableColumn
apDNSALGServerStatus = _ApDNSALGServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 1, 1, 8),
    _ApDNSALGServerStatus_Type()
)
apDNSALGServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDNSALGServerStatus.setStatus("current")
_ApDNSALGStatsTable_Object = MibTable
apDNSALGStatsTable = _ApDNSALGStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2)
)
if mibBuilder.loadTexts:
    apDNSALGStatsTable.setStatus("current")
_ApDnsALGStatsEntry_Object = MibTableRow
apDnsALGStatsEntry = _ApDnsALGStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1)
)
apDnsALGStatsEntry.setIndexNames(
    (0, "APDNSALG-MIB", "apDnsAlgClientRealmIndex"),
)
if mibBuilder.loadTexts:
    apDnsALGStatsEntry.setStatus("current")


class _ApDnsAlgClientRealmIndex_Type(Integer32):
    """Custom type apDnsAlgClientRealmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApDnsAlgClientRealmIndex_Type.__name__ = "Integer32"
_ApDnsAlgClientRealmIndex_Object = MibTableColumn
apDnsAlgClientRealmIndex = _ApDnsAlgClientRealmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 1),
    _ApDnsAlgClientRealmIndex_Type()
)
apDnsAlgClientRealmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDnsAlgClientRealmIndex.setStatus("current")


class _ApDnsAlgClientRealmName_Type(DisplayString):
    """Custom type apDnsAlgClientRealmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApDnsAlgClientRealmName_Type.__name__ = "DisplayString"
_ApDnsAlgClientRealmName_Object = MibTableColumn
apDnsAlgClientRealmName = _ApDnsAlgClientRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 2),
    _ApDnsAlgClientRealmName_Type()
)
apDnsAlgClientRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgClientRealmName.setStatus("current")
_ApDnsAlgCurrentQueries_Type = Gauge32
_ApDnsAlgCurrentQueries_Object = MibTableColumn
apDnsAlgCurrentQueries = _ApDnsAlgCurrentQueries_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 3),
    _ApDnsAlgCurrentQueries_Type()
)
apDnsAlgCurrentQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgCurrentQueries.setStatus("current")
_ApDnsAlgTotalQueries_Type = Counter32
_ApDnsAlgTotalQueries_Object = MibTableColumn
apDnsAlgTotalQueries = _ApDnsAlgTotalQueries_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 4),
    _ApDnsAlgTotalQueries_Type()
)
apDnsAlgTotalQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgTotalQueries.setStatus("current")
_ApDnsAlgCurrentSucess_Type = Gauge32
_ApDnsAlgCurrentSucess_Object = MibTableColumn
apDnsAlgCurrentSucess = _ApDnsAlgCurrentSucess_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 5),
    _ApDnsAlgCurrentSucess_Type()
)
apDnsAlgCurrentSucess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgCurrentSucess.setStatus("current")
_ApDnsAlgTotalSucess_Type = Counter32
_ApDnsAlgTotalSucess_Object = MibTableColumn
apDnsAlgTotalSucess = _ApDnsAlgTotalSucess_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 6),
    _ApDnsAlgTotalSucess_Type()
)
apDnsAlgTotalSucess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgTotalSucess.setStatus("current")
_ApDnsAlgCurrentNotFound_Type = Gauge32
_ApDnsAlgCurrentNotFound_Object = MibTableColumn
apDnsAlgCurrentNotFound = _ApDnsAlgCurrentNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 7),
    _ApDnsAlgCurrentNotFound_Type()
)
apDnsAlgCurrentNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgCurrentNotFound.setStatus("current")
_ApDnsAlgTotalNotFound_Type = Counter32
_ApDnsAlgTotalNotFound_Object = MibTableColumn
apDnsAlgTotalNotFound = _ApDnsAlgTotalNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 8),
    _ApDnsAlgTotalNotFound_Type()
)
apDnsAlgTotalNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgTotalNotFound.setStatus("current")
_ApDnsAlgCurrentTimeOut_Type = Gauge32
_ApDnsAlgCurrentTimeOut_Object = MibTableColumn
apDnsAlgCurrentTimeOut = _ApDnsAlgCurrentTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 9),
    _ApDnsAlgCurrentTimeOut_Type()
)
apDnsAlgCurrentTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgCurrentTimeOut.setStatus("current")
_ApDnsAlgTotalTimeOut_Type = Counter32
_ApDnsAlgTotalTimeOut_Object = MibTableColumn
apDnsAlgTotalTimeOut = _ApDnsAlgTotalTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 10),
    _ApDnsAlgTotalTimeOut_Type()
)
apDnsAlgTotalTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgTotalTimeOut.setStatus("current")
_ApDnsAlgCurrentBadStatus_Type = Gauge32
_ApDnsAlgCurrentBadStatus_Object = MibTableColumn
apDnsAlgCurrentBadStatus = _ApDnsAlgCurrentBadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 11),
    _ApDnsAlgCurrentBadStatus_Type()
)
apDnsAlgCurrentBadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgCurrentBadStatus.setStatus("current")
_ApDnsAlgTotalBadStatus_Type = Counter32
_ApDnsAlgTotalBadStatus_Object = MibTableColumn
apDnsAlgTotalBadStatus = _ApDnsAlgTotalBadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 12),
    _ApDnsAlgTotalBadStatus_Type()
)
apDnsAlgTotalBadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgTotalBadStatus.setStatus("current")
_ApDnsAlgCurrentOtherFailures_Type = Gauge32
_ApDnsAlgCurrentOtherFailures_Object = MibTableColumn
apDnsAlgCurrentOtherFailures = _ApDnsAlgCurrentOtherFailures_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 13),
    _ApDnsAlgCurrentOtherFailures_Type()
)
apDnsAlgCurrentOtherFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgCurrentOtherFailures.setStatus("current")
_ApDnsAlgTotalOtherFailures_Type = Counter32
_ApDnsAlgTotalOtherFailures_Object = MibTableColumn
apDnsAlgTotalOtherFailures = _ApDnsAlgTotalOtherFailures_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 14),
    _ApDnsAlgTotalOtherFailures_Type()
)
apDnsAlgTotalOtherFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgTotalOtherFailures.setStatus("current")
_ApDnsAlgAvgLatency_Type = Unsigned32
_ApDnsAlgAvgLatency_Object = MibTableColumn
apDnsAlgAvgLatency = _ApDnsAlgAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 15),
    _ApDnsAlgAvgLatency_Type()
)
apDnsAlgAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgAvgLatency.setStatus("current")
_ApDnsAlgMaxLatency_Type = Unsigned32
_ApDnsAlgMaxLatency_Object = MibTableColumn
apDnsAlgMaxLatency = _ApDnsAlgMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 16),
    _ApDnsAlgMaxLatency_Type()
)
apDnsAlgMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgMaxLatency.setStatus("current")
_ApDnsAlgMaxBurstRate_Type = Unsigned32
_ApDnsAlgMaxBurstRate_Object = MibTableColumn
apDnsAlgMaxBurstRate = _ApDnsAlgMaxBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 1, 2, 2, 1, 17),
    _ApDnsAlgMaxBurstRate_Type()
)
apDnsAlgMaxBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnsAlgMaxBurstRate.setStatus("current")
_ApDNSALGNotificationObjects_ObjectIdentity = ObjectIdentity
apDNSALGNotificationObjects = _ApDNSALGNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2)
)
_ApDNSALGNotifObjects_ObjectIdentity = ObjectIdentity
apDNSALGNotifObjects = _ApDNSALGNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 1)
)


class _ApDNSALGConstraintsStatus_Type(Integer32):
    """Custom type apDNSALGConstraintsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("constraintsExceeded", 1),
          ("inservice", 0))
    )


_ApDNSALGConstraintsStatus_Type.__name__ = "Integer32"
_ApDNSALGConstraintsStatus_Object = MibScalar
apDNSALGConstraintsStatus = _ApDNSALGConstraintsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 1, 1),
    _ApDNSALGConstraintsStatus_Type()
)
apDNSALGConstraintsStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apDNSALGConstraintsStatus.setStatus("current")
_ApDNSALGNotifPrefix_ObjectIdentity = ObjectIdentity
apDNSALGNotifPrefix = _ApDNSALGNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2)
)
_ApDNSALGNotifications_ObjectIdentity = ObjectIdentity
apDNSALGNotifications = _ApDNSALGNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0)
)
_ApDNSALGConformance_ObjectIdentity = ObjectIdentity
apDNSALGConformance = _ApDNSALGConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 3)
)
_ApDNSALGObjectGroups_ObjectIdentity = ObjectIdentity
apDNSALGObjectGroups = _ApDNSALGObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 1)
)
_ApDNSALGNotificationGroups_ObjectIdentity = ObjectIdentity
apDNSALGNotificationGroups = _ApDNSALGNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 2)
)

# Managed Objects groups

apDnsAlgServerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 1, 1)
)
apDnsAlgServerStatusGroup.setObjects(
      *(("APDNSALG-MIB", "apDNSALGConfigIndex"),
        ("APDNSALG-MIB", "apDNSALGServerIndex"),
        ("APDNSALG-MIB", "apDNSALGConfigName"),
        ("APDNSALG-MIB", "apDNSALGServerRealm"),
        ("APDNSALG-MIB", "apDNSALGDomainSuffix"),
        ("APDNSALG-MIB", "apDNSALGServerIpAddress"),
        ("APDNSALG-MIB", "apDNSALGServerStatus"))
)
if mibBuilder.loadTexts:
    apDnsAlgServerStatusGroup.setStatus("current")

apDnsAlgStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 1, 2)
)
apDnsAlgStatsGroup.setObjects(
      *(("APDNSALG-MIB", "apDnsAlgClientRealmIndex"),
        ("APDNSALG-MIB", "apDnsAlgClientRealmName"),
        ("APDNSALG-MIB", "apDnsAlgCurrentQueries"),
        ("APDNSALG-MIB", "apDnsAlgTotalQueries"),
        ("APDNSALG-MIB", "apDnsAlgCurrentSucess"),
        ("APDNSALG-MIB", "apDnsAlgTotalSucess"),
        ("APDNSALG-MIB", "apDnsAlgCurrentNotFound"),
        ("APDNSALG-MIB", "apDnsAlgTotalNotFound"),
        ("APDNSALG-MIB", "apDnsAlgCurrentTimeOut"),
        ("APDNSALG-MIB", "apDnsAlgTotalTimeOut"),
        ("APDNSALG-MIB", "apDnsAlgCurrentBadStatus"),
        ("APDNSALG-MIB", "apDnsAlgTotalBadStatus"),
        ("APDNSALG-MIB", "apDnsAlgCurrentOtherFailures"),
        ("APDNSALG-MIB", "apDnsAlgTotalOtherFailures"),
        ("APDNSALG-MIB", "apDnsAlgAvgLatency"),
        ("APDNSALG-MIB", "apDnsAlgMaxLatency"),
        ("APDNSALG-MIB", "apDnsAlgMaxBurstRate"))
)
if mibBuilder.loadTexts:
    apDnsAlgStatsGroup.setStatus("current")


# Notification objects

apDnsAlgStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 1)
)
apDnsAlgStatusChangeTrap.setObjects(
      *(("APDNSALG-MIB", "apDNSALGConfigName"),
        ("APDNSALG-MIB", "apDNSALGServerRealm"),
        ("APDNSALG-MIB", "apDNSALGServerIpAddress"),
        ("APDNSALG-MIB", "apDNSALGServerStatus"))
)
if mibBuilder.loadTexts:
    apDnsAlgStatusChangeTrap.setStatus(
        "current"
    )

apDnsAlgStatusChangeClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 2)
)
apDnsAlgStatusChangeClearTrap.setObjects(
      *(("APDNSALG-MIB", "apDNSALGConfigName"),
        ("APDNSALG-MIB", "apDNSALGServerRealm"),
        ("APDNSALG-MIB", "apDNSALGServerIpAddress"),
        ("APDNSALG-MIB", "apDNSALGServerStatus"))
)
if mibBuilder.loadTexts:
    apDnsAlgStatusChangeClearTrap.setStatus(
        "current"
    )

apDnsAlgConstraintStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 3)
)
apDnsAlgConstraintStateChangeTrap.setObjects(
      *(("APDNSALG-MIB", "apDNSALGConfigName"),
        ("APDNSALG-MIB", "apDNSALGConstraintsStatus"))
)
if mibBuilder.loadTexts:
    apDnsAlgConstraintStateChangeTrap.setStatus(
        "current"
    )

apDnsAlgConstraintStateChangeClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 4)
)
apDnsAlgConstraintStateChangeClearTrap.setObjects(
      *(("APDNSALG-MIB", "apDNSALGConfigName"),
        ("APDNSALG-MIB", "apDNSALGConstraintsStatus"))
)
if mibBuilder.loadTexts:
    apDnsAlgConstraintStateChangeClearTrap.setStatus(
        "current"
    )

apDnsAlgSvrConstraintStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 5)
)
apDnsAlgSvrConstraintStateChangeTrap.setObjects(
      *(("APDNSALG-MIB", "apDNSALGConfigName"),
        ("APDNSALG-MIB", "apDNSALGServerRealm"),
        ("APDNSALG-MIB", "apDNSALGServerIpAddress"),
        ("APDNSALG-MIB", "apDNSALGConstraintsStatus"))
)
if mibBuilder.loadTexts:
    apDnsAlgSvrConstraintStateChangeTrap.setStatus(
        "current"
    )

apDnsAlgSvrConstraintStateChangeClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 2, 2, 0, 6)
)
apDnsAlgSvrConstraintStateChangeClearTrap.setObjects(
      *(("APDNSALG-MIB", "apDNSALGConfigName"),
        ("APDNSALG-MIB", "apDNSALGServerRealm"),
        ("APDNSALG-MIB", "apDNSALGServerIpAddress"),
        ("APDNSALG-MIB", "apDNSALGConstraintsStatus"))
)
if mibBuilder.loadTexts:
    apDnsAlgSvrConstraintStateChangeClearTrap.setStatus(
        "current"
    )


# Notifications groups

apDNSALGNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 14, 3, 2, 1)
)
apDNSALGNotificationsGroup.setObjects(
      *(("APDNSALG-MIB", "apDnsAlgStatusChangeTrap"),
        ("APDNSALG-MIB", "apDnsAlgStatusChangeClearTrap"),
        ("APDNSALG-MIB", "apDnsAlgConstraintStateChangeTrap"),
        ("APDNSALG-MIB", "apDnsAlgConstraintStateChangeClearTrap"),
        ("APDNSALG-MIB", "apDnsAlgSvrConstraintStateChangeTrap"),
        ("APDNSALG-MIB", "apDnsAlgSvrConstraintStateChangeClearTrap"))
)
if mibBuilder.loadTexts:
    apDNSALGNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APDNSALG-MIB",
    **{"apDNSALGModule": apDNSALGModule,
       "apDNSALGMIBObjects": apDNSALGMIBObjects,
       "apDNSALGMIBGeneralObjects": apDNSALGMIBGeneralObjects,
       "apDNSALGMIBTabularObjects": apDNSALGMIBTabularObjects,
       "apDNSALGServerStatusTable": apDNSALGServerStatusTable,
       "apDNSALGServerStatusEntry": apDNSALGServerStatusEntry,
       "apDNSALGConfigIndex": apDNSALGConfigIndex,
       "apDNSALGServerIndex": apDNSALGServerIndex,
       "apDNSALGConfigName": apDNSALGConfigName,
       "apDNSALGServerRealm": apDNSALGServerRealm,
       "apDNSALGDomainSuffix": apDNSALGDomainSuffix,
       "apDNSALGServerIpAddress": apDNSALGServerIpAddress,
       "apDNSALGServerStatus": apDNSALGServerStatus,
       "apDNSALGStatsTable": apDNSALGStatsTable,
       "apDnsALGStatsEntry": apDnsALGStatsEntry,
       "apDnsAlgClientRealmIndex": apDnsAlgClientRealmIndex,
       "apDnsAlgClientRealmName": apDnsAlgClientRealmName,
       "apDnsAlgCurrentQueries": apDnsAlgCurrentQueries,
       "apDnsAlgTotalQueries": apDnsAlgTotalQueries,
       "apDnsAlgCurrentSucess": apDnsAlgCurrentSucess,
       "apDnsAlgTotalSucess": apDnsAlgTotalSucess,
       "apDnsAlgCurrentNotFound": apDnsAlgCurrentNotFound,
       "apDnsAlgTotalNotFound": apDnsAlgTotalNotFound,
       "apDnsAlgCurrentTimeOut": apDnsAlgCurrentTimeOut,
       "apDnsAlgTotalTimeOut": apDnsAlgTotalTimeOut,
       "apDnsAlgCurrentBadStatus": apDnsAlgCurrentBadStatus,
       "apDnsAlgTotalBadStatus": apDnsAlgTotalBadStatus,
       "apDnsAlgCurrentOtherFailures": apDnsAlgCurrentOtherFailures,
       "apDnsAlgTotalOtherFailures": apDnsAlgTotalOtherFailures,
       "apDnsAlgAvgLatency": apDnsAlgAvgLatency,
       "apDnsAlgMaxLatency": apDnsAlgMaxLatency,
       "apDnsAlgMaxBurstRate": apDnsAlgMaxBurstRate,
       "apDNSALGNotificationObjects": apDNSALGNotificationObjects,
       "apDNSALGNotifObjects": apDNSALGNotifObjects,
       "apDNSALGConstraintsStatus": apDNSALGConstraintsStatus,
       "apDNSALGNotifPrefix": apDNSALGNotifPrefix,
       "apDNSALGNotifications": apDNSALGNotifications,
       "apDnsAlgStatusChangeTrap": apDnsAlgStatusChangeTrap,
       "apDnsAlgStatusChangeClearTrap": apDnsAlgStatusChangeClearTrap,
       "apDnsAlgConstraintStateChangeTrap": apDnsAlgConstraintStateChangeTrap,
       "apDnsAlgConstraintStateChangeClearTrap": apDnsAlgConstraintStateChangeClearTrap,
       "apDnsAlgSvrConstraintStateChangeTrap": apDnsAlgSvrConstraintStateChangeTrap,
       "apDnsAlgSvrConstraintStateChangeClearTrap": apDnsAlgSvrConstraintStateChangeClearTrap,
       "apDNSALGConformance": apDNSALGConformance,
       "apDNSALGObjectGroups": apDNSALGObjectGroups,
       "apDnsAlgServerStatusGroup": apDnsAlgServerStatusGroup,
       "apDnsAlgStatsGroup": apDnsAlgStatsGroup,
       "apDNSALGNotificationGroups": apDNSALGNotificationGroups,
       "apDNSALGNotificationsGroup": apDNSALGNotificationsGroup}
)
