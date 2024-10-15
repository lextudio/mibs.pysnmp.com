# SNMP MIB module (ASCEND-CALL-LOGGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-CALL-LOGGING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:53 2024
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

(callLoggingGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "callLoggingGroup")

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

_CallLoggingNumServers_Type = Integer32
_CallLoggingNumServers_Object = MibScalar
callLoggingNumServers = _CallLoggingNumServers_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 1),
    _CallLoggingNumServers_Type()
)
callLoggingNumServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callLoggingNumServers.setStatus("mandatory")
_CallLoggingServerTable_Object = MibTable
callLoggingServerTable = _CallLoggingServerTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 2)
)
if mibBuilder.loadTexts:
    callLoggingServerTable.setStatus("mandatory")
_CallLoggingServerEntry_Object = MibTableRow
callLoggingServerEntry = _CallLoggingServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 2, 1)
)
callLoggingServerEntry.setIndexNames(
    (0, "ASCEND-CALL-LOGGING-MIB", "callLoggingServerIndex"),
)
if mibBuilder.loadTexts:
    callLoggingServerEntry.setStatus("mandatory")
_CallLoggingServerIndex_Type = Integer32
_CallLoggingServerIndex_Object = MibTableColumn
callLoggingServerIndex = _CallLoggingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 2, 1, 1),
    _CallLoggingServerIndex_Type()
)
callLoggingServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callLoggingServerIndex.setStatus("mandatory")


class _CallLoggingCurrentServerFlag_Type(Integer32):
    """Custom type callLoggingCurrentServerFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_CallLoggingCurrentServerFlag_Type.__name__ = "Integer32"
_CallLoggingCurrentServerFlag_Object = MibTableColumn
callLoggingCurrentServerFlag = _CallLoggingCurrentServerFlag_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 2, 1, 2),
    _CallLoggingCurrentServerFlag_Type()
)
callLoggingCurrentServerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callLoggingCurrentServerFlag.setStatus("mandatory")
_CallLoggingServerIPAddress_Type = IpAddress
_CallLoggingServerIPAddress_Object = MibTableColumn
callLoggingServerIPAddress = _CallLoggingServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 2, 1, 3),
    _CallLoggingServerIPAddress_Type()
)
callLoggingServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingServerIPAddress.setStatus("mandatory")


class _CallLoggingEnableActiveServer_Type(Integer32):
    """Custom type callLoggingEnableActiveServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("notApplicable", 1))
    )


_CallLoggingEnableActiveServer_Type.__name__ = "Integer32"
_CallLoggingEnableActiveServer_Object = MibTableColumn
callLoggingEnableActiveServer = _CallLoggingEnableActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 2, 1, 4),
    _CallLoggingEnableActiveServer_Type()
)
callLoggingEnableActiveServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingEnableActiveServer.setStatus("mandatory")


class _CallLoggingStatus_Type(Integer32):
    """Custom type callLoggingStatus based on Integer32"""
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


_CallLoggingStatus_Type.__name__ = "Integer32"
_CallLoggingStatus_Object = MibScalar
callLoggingStatus = _CallLoggingStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 3),
    _CallLoggingStatus_Type()
)
callLoggingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingStatus.setStatus("mandatory")


class _CallLoggingPortNumber_Type(Integer32):
    """Custom type callLoggingPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CallLoggingPortNumber_Type.__name__ = "Integer32"
_CallLoggingPortNumber_Object = MibScalar
callLoggingPortNumber = _CallLoggingPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 4),
    _CallLoggingPortNumber_Type()
)
callLoggingPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingPortNumber.setStatus("mandatory")


class _CallLoggingKey_Type(OctetString):
    """Custom type callLoggingKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CallLoggingKey_Type.__name__ = "OctetString"
_CallLoggingKey_Object = MibScalar
callLoggingKey = _CallLoggingKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 5),
    _CallLoggingKey_Type()
)
callLoggingKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingKey.setStatus("mandatory")
_CallLoggingTimeout_Type = Integer32
_CallLoggingTimeout_Object = MibScalar
callLoggingTimeout = _CallLoggingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 6),
    _CallLoggingTimeout_Type()
)
callLoggingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingTimeout.setStatus("mandatory")


class _CallLoggingIdBase_Type(Integer32):
    """Custom type callLoggingIdBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              16)
        )
    )
    namedValues = NamedValues(
        *(("base10", 10),
          ("base16", 16),
          ("invalid", 2),
          ("other", 1))
    )


_CallLoggingIdBase_Type.__name__ = "Integer32"
_CallLoggingIdBase_Object = MibScalar
callLoggingIdBase = _CallLoggingIdBase_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 7),
    _CallLoggingIdBase_Type()
)
callLoggingIdBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingIdBase.setStatus("mandatory")


class _CallLoggingResetTime_Type(Integer32):
    """Custom type callLoggingResetTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CallLoggingResetTime_Type.__name__ = "Integer32"
_CallLoggingResetTime_Object = MibScalar
callLoggingResetTime = _CallLoggingResetTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 8),
    _CallLoggingResetTime_Type()
)
callLoggingResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingResetTime.setStatus("mandatory")


class _CallLoggingStopPacketsOnly_Type(Integer32):
    """Custom type callLoggingStopPacketsOnly based on Integer32"""
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


_CallLoggingStopPacketsOnly_Type.__name__ = "Integer32"
_CallLoggingStopPacketsOnly_Object = MibScalar
callLoggingStopPacketsOnly = _CallLoggingStopPacketsOnly_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 9),
    _CallLoggingStopPacketsOnly_Type()
)
callLoggingStopPacketsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingStopPacketsOnly.setStatus("mandatory")
_CallLoggingRetryLimit_Type = Integer32
_CallLoggingRetryLimit_Object = MibScalar
callLoggingRetryLimit = _CallLoggingRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 10),
    _CallLoggingRetryLimit_Type()
)
callLoggingRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingRetryLimit.setStatus("mandatory")


class _CallLoggingAssStatus_Type(Integer32):
    """Custom type callLoggingAssStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 3),
          ("active", 2),
          ("idle", 1))
    )


_CallLoggingAssStatus_Type.__name__ = "Integer32"
_CallLoggingAssStatus_Object = MibScalar
callLoggingAssStatus = _CallLoggingAssStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 11),
    _CallLoggingAssStatus_Type()
)
callLoggingAssStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callLoggingAssStatus.setStatus("mandatory")
_CallLoggingDroppedPacketCount_Type = Integer32
_CallLoggingDroppedPacketCount_Object = MibScalar
callLoggingDroppedPacketCount = _CallLoggingDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 12),
    _CallLoggingDroppedPacketCount_Type()
)
callLoggingDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callLoggingDroppedPacketCount.setStatus("mandatory")


class _CallLoggingRadCompatMode_Type(Integer32):
    """Custom type callLoggingRadCompatMode based on Integer32"""
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
        *(("invalid", 2),
          ("other", 1),
          ("radOldAscend", 3),
          ("radVendorSpecific", 4))
    )


_CallLoggingRadCompatMode_Type.__name__ = "Integer32"
_CallLoggingRadCompatMode_Object = MibScalar
callLoggingRadCompatMode = _CallLoggingRadCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 25, 13),
    _CallLoggingRadCompatMode_Type()
)
callLoggingRadCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callLoggingRadCompatMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-CALL-LOGGING-MIB",
    **{"callLoggingNumServers": callLoggingNumServers,
       "callLoggingServerTable": callLoggingServerTable,
       "callLoggingServerEntry": callLoggingServerEntry,
       "callLoggingServerIndex": callLoggingServerIndex,
       "callLoggingCurrentServerFlag": callLoggingCurrentServerFlag,
       "callLoggingServerIPAddress": callLoggingServerIPAddress,
       "callLoggingEnableActiveServer": callLoggingEnableActiveServer,
       "callLoggingStatus": callLoggingStatus,
       "callLoggingPortNumber": callLoggingPortNumber,
       "callLoggingKey": callLoggingKey,
       "callLoggingTimeout": callLoggingTimeout,
       "callLoggingIdBase": callLoggingIdBase,
       "callLoggingResetTime": callLoggingResetTime,
       "callLoggingStopPacketsOnly": callLoggingStopPacketsOnly,
       "callLoggingRetryLimit": callLoggingRetryLimit,
       "callLoggingAssStatus": callLoggingAssStatus,
       "callLoggingDroppedPacketCount": callLoggingDroppedPacketCount,
       "callLoggingRadCompatMode": callLoggingRadCompatMode}
)
