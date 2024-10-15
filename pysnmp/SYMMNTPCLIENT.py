# SNMP MIB module (SYMMNTPCLIENT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMNTPCLIENT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:55 2024
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

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
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

(EnableValue,
 symmPacketService) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "EnableValue",
    "symmPacketService")


# MODULE-IDENTITY

symmNTPClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3)
)
symmNTPClient.setRevisions(
        ("2018-03-21 11:07",)
)


# Types definitions



class NTPCLIENTTIME(Integer32):
    """Custom type NTPCLIENTTIME based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syncNow", 1),
          ("writeOnlyObject", 2))
    )




# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_NtpClientStatusInfo_ObjectIdentity = ObjectIdentity
ntpClientStatusInfo = _NtpClientStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1)
)
_NtpcTimeOffset_Type = Integer32
_NtpcTimeOffset_Object = MibScalar
ntpcTimeOffset = _NtpcTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 1),
    _NtpcTimeOffset_Type()
)
ntpcTimeOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpcTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    ntpcTimeOffset.setUnits("seconds")
_NtpcLastUpdate_Type = DisplayString
_NtpcLastUpdate_Object = MibScalar
ntpcLastUpdate = _NtpcLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 2),
    _NtpcLastUpdate_Type()
)
ntpcLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpcLastUpdate.setStatus("current")
_NtpcStatus_Type = DisplayString
_NtpcStatus_Object = MibScalar
ntpcStatus = _NtpcStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 3),
    _NtpcStatus_Type()
)
ntpcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpcStatus.setStatus("current")
_NtpcServerIP_Type = DisplayString
_NtpcServerIP_Object = MibScalar
ntpcServerIP = _NtpcServerIP_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 4),
    _NtpcServerIP_Type()
)
ntpcServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpcServerIP.setStatus("current")
_NtpcServerLeapIndicator_Type = Integer32
_NtpcServerLeapIndicator_Object = MibScalar
ntpcServerLeapIndicator = _NtpcServerLeapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 5),
    _NtpcServerLeapIndicator_Type()
)
ntpcServerLeapIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpcServerLeapIndicator.setStatus("current")
_NtpcServerStratum_Type = Integer32
_NtpcServerStratum_Object = MibScalar
ntpcServerStratum = _NtpcServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 6),
    _NtpcServerStratum_Type()
)
ntpcServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpcServerStratum.setStatus("current")
_NtpcServerRefID_Type = DisplayString
_NtpcServerRefID_Object = MibScalar
ntpcServerRefID = _NtpcServerRefID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 1, 7),
    _NtpcServerRefID_Type()
)
ntpcServerRefID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpcServerRefID.setStatus("current")
_NtpClientConfigInfo_ObjectIdentity = ObjectIdentity
ntpClientConfigInfo = _NtpClientConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2)
)
_NtpcServerIPAddrTable_Object = MibTable
ntpcServerIPAddrTable = _NtpcServerIPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ntpcServerIPAddrTable.setStatus("current")
_NtpcServerIPAddrEntry_Object = MibTableRow
ntpcServerIPAddrEntry = _NtpcServerIPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1, 1)
)
ntpcServerIPAddrEntry.setIndexNames(
    (0, "SYMMNTPCLIENT", "ntpcServerIPAddrIndex"),
)
if mibBuilder.loadTexts:
    ntpcServerIPAddrEntry.setStatus("current")


class _NtpcServerIPAddrIndex_Type(Integer32):
    """Custom type ntpcServerIPAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NtpcServerIPAddrIndex_Type.__name__ = "Integer32"
_NtpcServerIPAddrIndex_Object = MibTableColumn
ntpcServerIPAddrIndex = _NtpcServerIPAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1, 1, 1),
    _NtpcServerIPAddrIndex_Type()
)
ntpcServerIPAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpcServerIPAddrIndex.setStatus("current")
_NtpcServerIPAddress_Type = DisplayString
_NtpcServerIPAddress_Object = MibTableColumn
ntpcServerIPAddress = _NtpcServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 1, 1, 2),
    _NtpcServerIPAddress_Type()
)
ntpcServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpcServerIPAddress.setStatus("current")
_NtpClientState_Type = EnableValue
_NtpClientState_Object = MibScalar
ntpClientState = _NtpClientState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 2),
    _NtpClientState_Type()
)
ntpClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClientState.setStatus("current")
_NtpClientSyncOnBoot_Type = EnableValue
_NtpClientSyncOnBoot_Object = MibScalar
ntpClientSyncOnBoot = _NtpClientSyncOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 3),
    _NtpClientSyncOnBoot_Type()
)
ntpClientSyncOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClientSyncOnBoot.setStatus("current")


class _NtpClientPollInterval_Type(Integer32):
    """Custom type ntpClientPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_NtpClientPollInterval_Type.__name__ = "Integer32"
_NtpClientPollInterval_Object = MibScalar
ntpClientPollInterval = _NtpClientPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 4),
    _NtpClientPollInterval_Type()
)
ntpClientPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClientPollInterval.setStatus("current")
_NtpClientTime_Type = NTPCLIENTTIME
_NtpClientTime_Object = MibScalar
ntpClientTime = _NtpClientTime_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 2, 5),
    _NtpClientTime_Type()
)
ntpClientTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClientTime.setStatus("current")
_NtpClientConformance_ObjectIdentity = ObjectIdentity
ntpClientConformance = _NtpClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ntpClientConformance.setStatus("current")
_NtpClientCompliances_ObjectIdentity = ObjectIdentity
ntpClientCompliances = _NtpClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 1)
)
_NtpClientUocGroups_ObjectIdentity = ObjectIdentity
ntpClientUocGroups = _NtpClientUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 2)
)

# Managed Objects groups

ntpClientStatusInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 2, 1)
)
ntpClientStatusInfoGroup.setObjects(
      *(("SYMMNTPCLIENT", "ntpcTimeOffset"),
        ("SYMMNTPCLIENT", "ntpcLastUpdate"),
        ("SYMMNTPCLIENT", "ntpcStatus"),
        ("SYMMNTPCLIENT", "ntpcServerIP"),
        ("SYMMNTPCLIENT", "ntpcServerLeapIndicator"),
        ("SYMMNTPCLIENT", "ntpcServerStratum"),
        ("SYMMNTPCLIENT", "ntpcServerRefID"))
)
if mibBuilder.loadTexts:
    ntpClientStatusInfoGroup.setStatus("current")

ntpClientConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 2, 2)
)
ntpClientConfigInfoGroup.setObjects(
      *(("SYMMNTPCLIENT", "ntpcServerIPAddress"),
        ("SYMMNTPCLIENT", "ntpClientState"),
        ("SYMMNTPCLIENT", "ntpClientSyncOnBoot"),
        ("SYMMNTPCLIENT", "ntpClientPollInterval"))
)
if mibBuilder.loadTexts:
    ntpClientConfigInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntpClientBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ntpClientBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMNTPCLIENT",
    **{"DateAndTime": DateAndTime,
       "TLocalTimeOffset": TLocalTimeOffset,
       "NTPCLIENTTIME": NTPCLIENTTIME,
       "symmNTPClient": symmNTPClient,
       "ntpClientStatusInfo": ntpClientStatusInfo,
       "ntpcTimeOffset": ntpcTimeOffset,
       "ntpcLastUpdate": ntpcLastUpdate,
       "ntpcStatus": ntpcStatus,
       "ntpcServerIP": ntpcServerIP,
       "ntpcServerLeapIndicator": ntpcServerLeapIndicator,
       "ntpcServerStratum": ntpcServerStratum,
       "ntpcServerRefID": ntpcServerRefID,
       "ntpClientConfigInfo": ntpClientConfigInfo,
       "ntpcServerIPAddrTable": ntpcServerIPAddrTable,
       "ntpcServerIPAddrEntry": ntpcServerIPAddrEntry,
       "ntpcServerIPAddrIndex": ntpcServerIPAddrIndex,
       "ntpcServerIPAddress": ntpcServerIPAddress,
       "ntpClientState": ntpClientState,
       "ntpClientSyncOnBoot": ntpClientSyncOnBoot,
       "ntpClientPollInterval": ntpClientPollInterval,
       "ntpClientTime": ntpClientTime,
       "ntpClientConformance": ntpClientConformance,
       "ntpClientCompliances": ntpClientCompliances,
       "ntpClientBasicCompliance": ntpClientBasicCompliance,
       "ntpClientUocGroups": ntpClientUocGroups,
       "ntpClientStatusInfoGroup": ntpClientStatusInfoGroup,
       "ntpClientConfigInfoGroup": ntpClientConfigInfoGroup}
)
