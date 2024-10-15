# SNMP MIB module (ZYXEL-IPV6-NDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-IPV6-NDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:06 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIpv6Ndp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelNdpSetup_ObjectIdentity = ObjectIdentity
zyxelNdpSetup = _ZyxelNdpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1)
)
_ZyNdpMaxNumberOfPrefixes_Type = Integer32
_ZyNdpMaxNumberOfPrefixes_Object = MibScalar
zyNdpMaxNumberOfPrefixes = _ZyNdpMaxNumberOfPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 1),
    _ZyNdpMaxNumberOfPrefixes_Type()
)
zyNdpMaxNumberOfPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyNdpMaxNumberOfPrefixes.setStatus("current")
_ZyxelNdpTable_Object = MibTable
zyxelNdpTable = _ZyxelNdpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelNdpTable.setStatus("current")
_ZyxelNdpEntry_Object = MibTableRow
zyxelNdpEntry = _ZyxelNdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 2, 1)
)
zyxelNdpEntry.setIndexNames(
    (0, "ZYXEL-IPV6-NDP-MIB", "zyNdpIfIndex"),
)
if mibBuilder.loadTexts:
    zyxelNdpEntry.setStatus("current")
_ZyNdpIfIndex_Type = Integer32
_ZyNdpIfIndex_Object = MibTableColumn
zyNdpIfIndex = _ZyNdpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 2, 1, 1),
    _ZyNdpIfIndex_Type()
)
zyNdpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyNdpIfIndex.setStatus("current")
_ZyNdpDadAttempts_Type = Integer32
_ZyNdpDadAttempts_Object = MibTableColumn
zyNdpDadAttempts = _ZyNdpDadAttempts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 2, 1, 2),
    _ZyNdpDadAttempts_Type()
)
zyNdpDadAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNdpDadAttempts.setStatus("current")
_ZyNdpNsInterval_Type = Integer32
_ZyNdpNsInterval_Object = MibTableColumn
zyNdpNsInterval = _ZyNdpNsInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 2, 1, 3),
    _ZyNdpNsInterval_Type()
)
zyNdpNsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNdpNsInterval.setStatus("current")
_ZyNdpReachableTime_Type = Integer32
_ZyNdpReachableTime_Object = MibTableColumn
zyNdpReachableTime = _ZyNdpReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 2, 1, 4),
    _ZyNdpReachableTime_Type()
)
zyNdpReachableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNdpReachableTime.setStatus("current")
_ZyxelNdpPrefixTable_Object = MibTable
zyxelNdpPrefixTable = _ZyxelNdpPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelNdpPrefixTable.setStatus("current")
_ZyxelNdpPrefixEntry_Object = MibTableRow
zyxelNdpPrefixEntry = _ZyxelNdpPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1)
)
zyxelNdpPrefixEntry.setIndexNames(
    (0, "ZYXEL-IPV6-NDP-MIB", "zyNdpPrefixIfIndex"),
    (0, "ZYXEL-IPV6-NDP-MIB", "zyNdpPrefixPrefixType"),
    (0, "ZYXEL-IPV6-NDP-MIB", "zyNdpPrefixPrefixIpAddress"),
    (0, "ZYXEL-IPV6-NDP-MIB", "zyNdpPrefixPrefixLength"),
)
if mibBuilder.loadTexts:
    zyxelNdpPrefixEntry.setStatus("current")
_ZyNdpPrefixIfIndex_Type = Integer32
_ZyNdpPrefixIfIndex_Object = MibTableColumn
zyNdpPrefixIfIndex = _ZyNdpPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1, 1),
    _ZyNdpPrefixIfIndex_Type()
)
zyNdpPrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyNdpPrefixIfIndex.setStatus("current")
_ZyNdpPrefixPrefixType_Type = InetAddressType
_ZyNdpPrefixPrefixType_Object = MibTableColumn
zyNdpPrefixPrefixType = _ZyNdpPrefixPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1, 2),
    _ZyNdpPrefixPrefixType_Type()
)
zyNdpPrefixPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyNdpPrefixPrefixType.setStatus("current")
_ZyNdpPrefixPrefixIpAddress_Type = InetAddress
_ZyNdpPrefixPrefixIpAddress_Object = MibTableColumn
zyNdpPrefixPrefixIpAddress = _ZyNdpPrefixPrefixIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1, 3),
    _ZyNdpPrefixPrefixIpAddress_Type()
)
zyNdpPrefixPrefixIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyNdpPrefixPrefixIpAddress.setStatus("current")
_ZyNdpPrefixPrefixLength_Type = Integer32
_ZyNdpPrefixPrefixLength_Object = MibTableColumn
zyNdpPrefixPrefixLength = _ZyNdpPrefixPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1, 4),
    _ZyNdpPrefixPrefixLength_Type()
)
zyNdpPrefixPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyNdpPrefixPrefixLength.setStatus("current")
_ZyNdpPrefixValidLifetime_Type = Unsigned32
_ZyNdpPrefixValidLifetime_Object = MibTableColumn
zyNdpPrefixValidLifetime = _ZyNdpPrefixValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1, 5),
    _ZyNdpPrefixValidLifetime_Type()
)
zyNdpPrefixValidLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNdpPrefixValidLifetime.setStatus("current")
_ZyNdpPrefixPreferredLifetime_Type = Unsigned32
_ZyNdpPrefixPreferredLifetime_Object = MibTableColumn
zyNdpPrefixPreferredLifetime = _ZyNdpPrefixPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1, 6),
    _ZyNdpPrefixPreferredLifetime_Type()
)
zyNdpPrefixPreferredLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNdpPrefixPreferredLifetime.setStatus("current")
_ZyNdpPrefixNoAutonomousFlagState_Type = EnabledStatus
_ZyNdpPrefixNoAutonomousFlagState_Object = MibTableColumn
zyNdpPrefixNoAutonomousFlagState = _ZyNdpPrefixNoAutonomousFlagState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1, 7),
    _ZyNdpPrefixNoAutonomousFlagState_Type()
)
zyNdpPrefixNoAutonomousFlagState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNdpPrefixNoAutonomousFlagState.setStatus("current")
_ZyNdpPrefixNoOnLinkFlagState_Type = EnabledStatus
_ZyNdpPrefixNoOnLinkFlagState_Object = MibTableColumn
zyNdpPrefixNoOnLinkFlagState = _ZyNdpPrefixNoOnLinkFlagState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1, 8),
    _ZyNdpPrefixNoOnLinkFlagState_Type()
)
zyNdpPrefixNoOnLinkFlagState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNdpPrefixNoOnLinkFlagState.setStatus("current")
_ZyNdpPrefixNoAdvertiseFlagState_Type = EnabledStatus
_ZyNdpPrefixNoAdvertiseFlagState_Object = MibTableColumn
zyNdpPrefixNoAdvertiseFlagState = _ZyNdpPrefixNoAdvertiseFlagState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1, 9),
    _ZyNdpPrefixNoAdvertiseFlagState_Type()
)
zyNdpPrefixNoAdvertiseFlagState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyNdpPrefixNoAdvertiseFlagState.setStatus("current")
_ZyNdpPrefixRowStatus_Type = RowStatus
_ZyNdpPrefixRowStatus_Object = MibTableColumn
zyNdpPrefixRowStatus = _ZyNdpPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 35, 1, 3, 1, 10),
    _ZyNdpPrefixRowStatus_Type()
)
zyNdpPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyNdpPrefixRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IPV6-NDP-MIB",
    **{"zyxelIpv6Ndp": zyxelIpv6Ndp,
       "zyxelNdpSetup": zyxelNdpSetup,
       "zyNdpMaxNumberOfPrefixes": zyNdpMaxNumberOfPrefixes,
       "zyxelNdpTable": zyxelNdpTable,
       "zyxelNdpEntry": zyxelNdpEntry,
       "zyNdpIfIndex": zyNdpIfIndex,
       "zyNdpDadAttempts": zyNdpDadAttempts,
       "zyNdpNsInterval": zyNdpNsInterval,
       "zyNdpReachableTime": zyNdpReachableTime,
       "zyxelNdpPrefixTable": zyxelNdpPrefixTable,
       "zyxelNdpPrefixEntry": zyxelNdpPrefixEntry,
       "zyNdpPrefixIfIndex": zyNdpPrefixIfIndex,
       "zyNdpPrefixPrefixType": zyNdpPrefixPrefixType,
       "zyNdpPrefixPrefixIpAddress": zyNdpPrefixPrefixIpAddress,
       "zyNdpPrefixPrefixLength": zyNdpPrefixPrefixLength,
       "zyNdpPrefixValidLifetime": zyNdpPrefixValidLifetime,
       "zyNdpPrefixPreferredLifetime": zyNdpPrefixPreferredLifetime,
       "zyNdpPrefixNoAutonomousFlagState": zyNdpPrefixNoAutonomousFlagState,
       "zyNdpPrefixNoOnLinkFlagState": zyNdpPrefixNoOnLinkFlagState,
       "zyNdpPrefixNoAdvertiseFlagState": zyNdpPrefixNoAdvertiseFlagState,
       "zyNdpPrefixRowStatus": zyNdpPrefixRowStatus}
)
