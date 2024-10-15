# SNMP MIB module (SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:09 2024
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

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusServicesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusServicesMIBs")

(SonusName,) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusName")


# MODULE-IDENTITY

sonusSoftswitchClientServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusSoftswitchClientServicesMIBObjects_ObjectIdentity = ObjectIdentity
sonusSoftswitchClientServicesMIBObjects = _SonusSoftswitchClientServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1)
)
_SonusSoftswitch_ObjectIdentity = ObjectIdentity
sonusSoftswitch = _SonusSoftswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1)
)
_SonusPscsConfigObjects_ObjectIdentity = ObjectIdentity
sonusPscsConfigObjects = _SonusPscsConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 1)
)


class _SonusPscsReconnectTimeOut_Type(Integer32):
    """Custom type sonusPscsReconnectTimeOut based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SonusPscsReconnectTimeOut_Type.__name__ = "Integer32"
_SonusPscsReconnectTimeOut_Object = MibScalar
sonusPscsReconnectTimeOut = _SonusPscsReconnectTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 1, 1),
    _SonusPscsReconnectTimeOut_Type()
)
sonusPscsReconnectTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsReconnectTimeOut.setStatus("current")


class _SonusPscsSwitchOver_Type(Integer32):
    """Custom type sonusPscsSwitchOver based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_SonusPscsSwitchOver_Type.__name__ = "Integer32"
_SonusPscsSwitchOver_Object = MibScalar
sonusPscsSwitchOver = _SonusPscsSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 1, 2),
    _SonusPscsSwitchOver_Type()
)
sonusPscsSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsSwitchOver.setStatus("current")
_SonusPscsAdmn_ObjectIdentity = ObjectIdentity
sonusPscsAdmn = _SonusPscsAdmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2)
)
_SonusPscsAdmnNextIndex_Type = Integer32
_SonusPscsAdmnNextIndex_Object = MibScalar
sonusPscsAdmnNextIndex = _SonusPscsAdmnNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 1),
    _SonusPscsAdmnNextIndex_Type()
)
sonusPscsAdmnNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsAdmnNextIndex.setStatus("current")
_SonusPscsAdmnTable_Object = MibTable
sonusPscsAdmnTable = _SonusPscsAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusPscsAdmnTable.setStatus("current")
_SonusPscsAdmnEntry_Object = MibTableRow
sonusPscsAdmnEntry = _SonusPscsAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1)
)
sonusPscsAdmnEntry.setIndexNames(
    (0, "SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsPolicyServerIndex"),
)
if mibBuilder.loadTexts:
    sonusPscsAdmnEntry.setStatus("current")
_SonusPscsPolicyServerIndex_Type = Integer32
_SonusPscsPolicyServerIndex_Object = MibTableColumn
sonusPscsPolicyServerIndex = _SonusPscsPolicyServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 1),
    _SonusPscsPolicyServerIndex_Type()
)
sonusPscsPolicyServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsPolicyServerIndex.setStatus("current")
_SonusPscsPolicyServerName_Type = SonusName
_SonusPscsPolicyServerName_Object = MibTableColumn
sonusPscsPolicyServerName = _SonusPscsPolicyServerName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 2),
    _SonusPscsPolicyServerName_Type()
)
sonusPscsPolicyServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsPolicyServerName.setStatus("current")


class _SonusPscsPolicyServerIpAddress_Type(IpAddress):
    """Custom type sonusPscsPolicyServerIpAddress based on IpAddress"""
    defaultValue = 0


_SonusPscsPolicyServerIpAddress_Object = MibTableColumn
sonusPscsPolicyServerIpAddress = _SonusPscsPolicyServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 3),
    _SonusPscsPolicyServerIpAddress_Type()
)
sonusPscsPolicyServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsPolicyServerIpAddress.setStatus("current")


class _SonusPscsPolicyServerPortNum_Type(Integer32):
    """Custom type sonusPscsPolicyServerPortNum based on Integer32"""
    defaultValue = 3055

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusPscsPolicyServerPortNum_Type.__name__ = "Integer32"
_SonusPscsPolicyServerPortNum_Object = MibTableColumn
sonusPscsPolicyServerPortNum = _SonusPscsPolicyServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 4),
    _SonusPscsPolicyServerPortNum_Type()
)
sonusPscsPolicyServerPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsPolicyServerPortNum.setStatus("current")


class _SonusPscsPolicyServerAdmnState_Type(Integer32):
    """Custom type sonusPscsPolicyServerAdmnState based on Integer32"""
    defaultValue = 1

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


_SonusPscsPolicyServerAdmnState_Type.__name__ = "Integer32"
_SonusPscsPolicyServerAdmnState_Object = MibTableColumn
sonusPscsPolicyServerAdmnState = _SonusPscsPolicyServerAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 5),
    _SonusPscsPolicyServerAdmnState_Type()
)
sonusPscsPolicyServerAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsPolicyServerAdmnState.setStatus("current")


class _SonusPscsPolicyServerMode_Type(Integer32):
    """Custom type sonusPscsPolicyServerMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("outOfService", 3),
          ("standby", 2))
    )


_SonusPscsPolicyServerMode_Type.__name__ = "Integer32"
_SonusPscsPolicyServerMode_Object = MibTableColumn
sonusPscsPolicyServerMode = _SonusPscsPolicyServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 6),
    _SonusPscsPolicyServerMode_Type()
)
sonusPscsPolicyServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsPolicyServerMode.setStatus("current")


class _SonusPscsPolicyServerAction_Type(Integer32):
    """Custom type sonusPscsPolicyServerAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 1),
          ("force", 2))
    )


_SonusPscsPolicyServerAction_Type.__name__ = "Integer32"
_SonusPscsPolicyServerAction_Object = MibTableColumn
sonusPscsPolicyServerAction = _SonusPscsPolicyServerAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 7),
    _SonusPscsPolicyServerAction_Type()
)
sonusPscsPolicyServerAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsPolicyServerAction.setStatus("current")


class _SonusPscsTransactionTimer_Type(Integer32):
    """Custom type sonusPscsTransactionTimer based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 60000),
    )


_SonusPscsTransactionTimer_Type.__name__ = "Integer32"
_SonusPscsTransactionTimer_Object = MibTableColumn
sonusPscsTransactionTimer = _SonusPscsTransactionTimer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 8),
    _SonusPscsTransactionTimer_Type()
)
sonusPscsTransactionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsTransactionTimer.setStatus("current")


class _SonusPscsKeepAliveTimer_Type(Integer32):
    """Custom type sonusPscsKeepAliveTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SonusPscsKeepAliveTimer_Type.__name__ = "Integer32"
_SonusPscsKeepAliveTimer_Object = MibTableColumn
sonusPscsKeepAliveTimer = _SonusPscsKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 9),
    _SonusPscsKeepAliveTimer_Type()
)
sonusPscsKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsKeepAliveTimer.setStatus("current")


class _SonusPscsRetryTimer_Type(Integer32):
    """Custom type sonusPscsRetryTimer based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 60000),
    )


_SonusPscsRetryTimer_Type.__name__ = "Integer32"
_SonusPscsRetryTimer_Object = MibTableColumn
sonusPscsRetryTimer = _SonusPscsRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 10),
    _SonusPscsRetryTimer_Type()
)
sonusPscsRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsRetryTimer.setStatus("current")


class _SonusPscsRetries_Type(Integer32):
    """Custom type sonusPscsRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SonusPscsRetries_Type.__name__ = "Integer32"
_SonusPscsRetries_Object = MibTableColumn
sonusPscsRetries = _SonusPscsRetries_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 11),
    _SonusPscsRetries_Type()
)
sonusPscsRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsRetries.setStatus("current")
_SonusPscsPolicyServerRowStatus_Type = RowStatus
_SonusPscsPolicyServerRowStatus_Object = MibTableColumn
sonusPscsPolicyServerRowStatus = _SonusPscsPolicyServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 2, 2, 1, 12),
    _SonusPscsPolicyServerRowStatus_Type()
)
sonusPscsPolicyServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPscsPolicyServerRowStatus.setStatus("current")
_SonusPscsStatusTable_Object = MibTable
sonusPscsStatusTable = _SonusPscsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sonusPscsStatusTable.setStatus("current")
_SonusPscsStatusEntry_Object = MibTableRow
sonusPscsStatusEntry = _SonusPscsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 3, 1)
)
sonusPscsStatusEntry.setIndexNames(
    (0, "SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusPscsStatusEntry.setStatus("current")
_SonusPscsStatusIndex_Type = Integer32
_SonusPscsStatusIndex_Object = MibTableColumn
sonusPscsStatusIndex = _SonusPscsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 3, 1, 1),
    _SonusPscsStatusIndex_Type()
)
sonusPscsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsStatusIndex.setStatus("current")


class _SonusPscsOperState_Type(Integer32):
    """Custom type sonusPscsOperState based on Integer32"""
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
        *(("active", 1),
          ("congested", 3),
          ("down", 4),
          ("dryingup", 5),
          ("standby", 2))
    )


_SonusPscsOperState_Type.__name__ = "Integer32"
_SonusPscsOperState_Object = MibTableColumn
sonusPscsOperState = _SonusPscsOperState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 3, 1, 2),
    _SonusPscsOperState_Type()
)
sonusPscsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsOperState.setStatus("current")
_SonusPscsAverageTransactionTime_Type = Integer32
_SonusPscsAverageTransactionTime_Object = MibTableColumn
sonusPscsAverageTransactionTime = _SonusPscsAverageTransactionTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 3, 1, 3),
    _SonusPscsAverageTransactionTime_Type()
)
sonusPscsAverageTransactionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsAverageTransactionTime.setStatus("current")
_SonusPscsServerReconnects_Type = Counter32
_SonusPscsServerReconnects_Object = MibTableColumn
sonusPscsServerReconnects = _SonusPscsServerReconnects_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 3, 1, 4),
    _SonusPscsServerReconnects_Type()
)
sonusPscsServerReconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsServerReconnects.setStatus("current")
_SonusPscsTransactionCompleted_Type = Counter64
_SonusPscsTransactionCompleted_Object = MibTableColumn
sonusPscsTransactionCompleted = _SonusPscsTransactionCompleted_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 3, 1, 5),
    _SonusPscsTransactionCompleted_Type()
)
sonusPscsTransactionCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsTransactionCompleted.setStatus("current")
_SonusPscsTransactionRetryAttempts_Type = Counter32
_SonusPscsTransactionRetryAttempts_Object = MibTableColumn
sonusPscsTransactionRetryAttempts = _SonusPscsTransactionRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 3, 1, 6),
    _SonusPscsTransactionRetryAttempts_Type()
)
sonusPscsTransactionRetryAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsTransactionRetryAttempts.setStatus("current")
_SonusPscsTransactionFailedAttempts_Type = Counter32
_SonusPscsTransactionFailedAttempts_Object = MibTableColumn
sonusPscsTransactionFailedAttempts = _SonusPscsTransactionFailedAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 3, 1, 7),
    _SonusPscsTransactionFailedAttempts_Type()
)
sonusPscsTransactionFailedAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsTransactionFailedAttempts.setStatus("current")
_SonusPscsVersion_Type = Integer32
_SonusPscsVersion_Object = MibTableColumn
sonusPscsVersion = _SonusPscsVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 1, 1, 3, 1, 8),
    _SonusPscsVersion_Type()
)
sonusPscsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsVersion.setStatus("current")
_SonusSoftswitchClientServicesMIBNotifications_ObjectIdentity = ObjectIdentity
sonusSoftswitchClientServicesMIBNotifications = _SonusSoftswitchClientServicesMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2)
)
_SonusSoftswitchClientServicesMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusSoftswitchClientServicesMIBNotificationsPrefix = _SonusSoftswitchClientServicesMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 0)
)
_SonusSoftswitchClientServicesMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusSoftswitchClientServicesMIBNotificationsObjects = _SonusSoftswitchClientServicesMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1)
)


class _SonusPscsInServiceReason_Type(Integer32):
    """Custom type sonusPscsInServiceReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 3),
          ("configured", 1),
          ("successfulReConnect", 2))
    )


_SonusPscsInServiceReason_Type.__name__ = "Integer32"
_SonusPscsInServiceReason_Object = MibScalar
sonusPscsInServiceReason = _SonusPscsInServiceReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1, 1),
    _SonusPscsInServiceReason_Type()
)
sonusPscsInServiceReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsInServiceReason.setStatus("current")


class _SonusPscsOutOfServiceReason_Type(Integer32):
    """Custom type sonusPscsOutOfServiceReason based on Integer32"""
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
        *(("configured", 1),
          ("connectionLoss", 2),
          ("incompatibleVersion", 5),
          ("noConnection", 3),
          ("nodeNameChange", 4))
    )


_SonusPscsOutOfServiceReason_Type.__name__ = "Integer32"
_SonusPscsOutOfServiceReason_Object = MibScalar
sonusPscsOutOfServiceReason = _SonusPscsOutOfServiceReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1, 2),
    _SonusPscsOutOfServiceReason_Type()
)
sonusPscsOutOfServiceReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsOutOfServiceReason.setStatus("current")


class _SonusPscsSwitchoverReason_Type(Integer32):
    """Custom type sonusPscsSwitchoverReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("configured", 1),
          ("versionChanged", 3))
    )


_SonusPscsSwitchoverReason_Type.__name__ = "Integer32"
_SonusPscsSwitchoverReason_Object = MibScalar
sonusPscsSwitchoverReason = _SonusPscsSwitchoverReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1, 3),
    _SonusPscsSwitchoverReason_Type()
)
sonusPscsSwitchoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsSwitchoverReason.setStatus("current")


class _SonusPscsRouteFailureReason_Type(Integer32):
    """Custom type sonusPscsRouteFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("databaseError", 3),
          ("noServiceConfigured", 2),
          ("routeNotFound", 1))
    )


_SonusPscsRouteFailureReason_Type.__name__ = "Integer32"
_SonusPscsRouteFailureReason_Object = MibScalar
sonusPscsRouteFailureReason = _SonusPscsRouteFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1, 4),
    _SonusPscsRouteFailureReason_Type()
)
sonusPscsRouteFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsRouteFailureReason.setStatus("current")
_SonusPscsCallInfo_Type = DisplayString
_SonusPscsCallInfo_Object = MibScalar
sonusPscsCallInfo = _SonusPscsCallInfo_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1, 5),
    _SonusPscsCallInfo_Type()
)
sonusPscsCallInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsCallInfo.setStatus("current")


class _SonusPscsTranErrorReason_Type(Integer32):
    """Custom type sonusPscsTranErrorReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("decodeApiError", 7),
          ("encodeApiError", 6),
          ("invalidParameters", 3),
          ("noSoftswitchAvailable", 1),
          ("receiveError", 4),
          ("transactionTimeout", 2),
          ("transmitError", 5))
    )


_SonusPscsTranErrorReason_Type.__name__ = "Integer32"
_SonusPscsTranErrorReason_Object = MibScalar
sonusPscsTranErrorReason = _SonusPscsTranErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1, 6),
    _SonusPscsTranErrorReason_Type()
)
sonusPscsTranErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsTranErrorReason.setStatus("current")


class _SonusPscsRejectIndReason_Type(Integer32):
    """Custom type sonusPscsRejectIndReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("errorAVPContent", 3),
          ("errorMsgContent", 4),
          ("maxClientAccount", 5),
          ("miscRegFailure", 6),
          ("notRegistered", 1),
          ("unknownGateway", 2))
    )


_SonusPscsRejectIndReason_Type.__name__ = "Integer32"
_SonusPscsRejectIndReason_Object = MibScalar
sonusPscsRejectIndReason = _SonusPscsRejectIndReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1, 7),
    _SonusPscsRejectIndReason_Type()
)
sonusPscsRejectIndReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsRejectIndReason.setStatus("current")
_SonusPscsCalledNumber_Type = DisplayString
_SonusPscsCalledNumber_Object = MibScalar
sonusPscsCalledNumber = _SonusPscsCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1, 8),
    _SonusPscsCalledNumber_Type()
)
sonusPscsCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsCalledNumber.setStatus("current")
_SonusPscsCallingNumber_Type = DisplayString
_SonusPscsCallingNumber_Object = MibScalar
sonusPscsCallingNumber = _SonusPscsCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1, 9),
    _SonusPscsCallingNumber_Type()
)
sonusPscsCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsCallingNumber.setStatus("current")
_SonusPscsCarrierCode_Type = DisplayString
_SonusPscsCarrierCode_Object = MibScalar
sonusPscsCarrierCode = _SonusPscsCarrierCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 1, 10),
    _SonusPscsCarrierCode_Type()
)
sonusPscsCarrierCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPscsCarrierCode.setStatus("current")

# Managed Objects groups


# Notification objects

sonusSscsInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 0, 1)
)
sonusSscsInServiceNotification.setObjects(
      *(("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsPolicyServerName"),
        ("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsOperState"),
        ("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsInServiceReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSscsInServiceNotification.setStatus(
        "current"
    )

sonusSscsOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 0, 2)
)
sonusSscsOutOfServiceNotification.setObjects(
      *(("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsPolicyServerName"),
        ("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsOutOfServiceReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSscsOutOfServiceNotification.setStatus(
        "current"
    )

sonusSscsSwitchoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 0, 3)
)
sonusSscsSwitchoverNotification.setObjects(
      *(("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsPolicyServerName"),
        ("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsSwitchoverReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSscsSwitchoverNotification.setStatus(
        "current"
    )

sonusSscsRouteFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 0, 4)
)
sonusSscsRouteFailureNotification.setObjects(
      *(("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsPolicyServerName"),
        ("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsRouteFailureReason"),
        ("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsCalledNumber"),
        ("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsCallingNumber"),
        ("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsCarrierCode"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSscsRouteFailureNotification.setStatus(
        "current"
    )

sonusSscsTransErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 0, 5)
)
sonusSscsTransErrorNotification.setObjects(
      *(("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsPolicyServerName"),
        ("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsTranErrorReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSscsTransErrorNotification.setStatus(
        "current"
    )

sonusSscsRejectIndNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 6, 2, 0, 6)
)
sonusSscsRejectIndNotification.setObjects(
      *(("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsPolicyServerName"),
        ("SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB", "sonusPscsRejectIndReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSscsRejectIndNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-SOFTSWITCH-CLIENT-SERVICES-MIB",
    **{"sonusSoftswitchClientServicesMIB": sonusSoftswitchClientServicesMIB,
       "sonusSoftswitchClientServicesMIBObjects": sonusSoftswitchClientServicesMIBObjects,
       "sonusSoftswitch": sonusSoftswitch,
       "sonusPscsConfigObjects": sonusPscsConfigObjects,
       "sonusPscsReconnectTimeOut": sonusPscsReconnectTimeOut,
       "sonusPscsSwitchOver": sonusPscsSwitchOver,
       "sonusPscsAdmn": sonusPscsAdmn,
       "sonusPscsAdmnNextIndex": sonusPscsAdmnNextIndex,
       "sonusPscsAdmnTable": sonusPscsAdmnTable,
       "sonusPscsAdmnEntry": sonusPscsAdmnEntry,
       "sonusPscsPolicyServerIndex": sonusPscsPolicyServerIndex,
       "sonusPscsPolicyServerName": sonusPscsPolicyServerName,
       "sonusPscsPolicyServerIpAddress": sonusPscsPolicyServerIpAddress,
       "sonusPscsPolicyServerPortNum": sonusPscsPolicyServerPortNum,
       "sonusPscsPolicyServerAdmnState": sonusPscsPolicyServerAdmnState,
       "sonusPscsPolicyServerMode": sonusPscsPolicyServerMode,
       "sonusPscsPolicyServerAction": sonusPscsPolicyServerAction,
       "sonusPscsTransactionTimer": sonusPscsTransactionTimer,
       "sonusPscsKeepAliveTimer": sonusPscsKeepAliveTimer,
       "sonusPscsRetryTimer": sonusPscsRetryTimer,
       "sonusPscsRetries": sonusPscsRetries,
       "sonusPscsPolicyServerRowStatus": sonusPscsPolicyServerRowStatus,
       "sonusPscsStatusTable": sonusPscsStatusTable,
       "sonusPscsStatusEntry": sonusPscsStatusEntry,
       "sonusPscsStatusIndex": sonusPscsStatusIndex,
       "sonusPscsOperState": sonusPscsOperState,
       "sonusPscsAverageTransactionTime": sonusPscsAverageTransactionTime,
       "sonusPscsServerReconnects": sonusPscsServerReconnects,
       "sonusPscsTransactionCompleted": sonusPscsTransactionCompleted,
       "sonusPscsTransactionRetryAttempts": sonusPscsTransactionRetryAttempts,
       "sonusPscsTransactionFailedAttempts": sonusPscsTransactionFailedAttempts,
       "sonusPscsVersion": sonusPscsVersion,
       "sonusSoftswitchClientServicesMIBNotifications": sonusSoftswitchClientServicesMIBNotifications,
       "sonusSoftswitchClientServicesMIBNotificationsPrefix": sonusSoftswitchClientServicesMIBNotificationsPrefix,
       "sonusSscsInServiceNotification": sonusSscsInServiceNotification,
       "sonusSscsOutOfServiceNotification": sonusSscsOutOfServiceNotification,
       "sonusSscsSwitchoverNotification": sonusSscsSwitchoverNotification,
       "sonusSscsRouteFailureNotification": sonusSscsRouteFailureNotification,
       "sonusSscsTransErrorNotification": sonusSscsTransErrorNotification,
       "sonusSscsRejectIndNotification": sonusSscsRejectIndNotification,
       "sonusSoftswitchClientServicesMIBNotificationsObjects": sonusSoftswitchClientServicesMIBNotificationsObjects,
       "sonusPscsInServiceReason": sonusPscsInServiceReason,
       "sonusPscsOutOfServiceReason": sonusPscsOutOfServiceReason,
       "sonusPscsSwitchoverReason": sonusPscsSwitchoverReason,
       "sonusPscsRouteFailureReason": sonusPscsRouteFailureReason,
       "sonusPscsCallInfo": sonusPscsCallInfo,
       "sonusPscsTranErrorReason": sonusPscsTranErrorReason,
       "sonusPscsRejectIndReason": sonusPscsRejectIndReason,
       "sonusPscsCalledNumber": sonusPscsCalledNumber,
       "sonusPscsCallingNumber": sonusPscsCallingNumber,
       "sonusPscsCarrierCode": sonusPscsCarrierCode}
)
