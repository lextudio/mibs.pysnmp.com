# SNMP MIB module (KALEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/KALEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:37 2024
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

(kalExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "kalExt")

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


# MODULE-IDENTITY

apKalExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApKalTable_Object = MibTable
apKalTable = _ApKalTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2)
)
if mibBuilder.loadTexts:
    apKalTable.setStatus("current")
_ApKalEntry_Object = MibTableRow
apKalEntry = _ApKalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1)
)
apKalEntry.setIndexNames(
    (0, "KALEXT-MIB", "apKalName"),
)
if mibBuilder.loadTexts:
    apKalEntry.setStatus("current")


class _ApKalName_Type(DisplayString):
    """Custom type apKalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApKalName_Type.__name__ = "DisplayString"
_ApKalName_Object = MibTableColumn
apKalName = _ApKalName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 1),
    _ApKalName_Type()
)
apKalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalName.setStatus("current")
_ApKalStatus_Type = RowStatus
_ApKalStatus_Object = MibTableColumn
apKalStatus = _ApKalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 2),
    _ApKalStatus_Type()
)
apKalStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalStatus.setStatus("current")


class _ApKalDescription_Type(DisplayString):
    """Custom type apKalDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApKalDescription_Type.__name__ = "DisplayString"
_ApKalDescription_Object = MibTableColumn
apKalDescription = _ApKalDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 3),
    _ApKalDescription_Type()
)
apKalDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalDescription.setStatus("current")


class _ApKalEnable_Type(Integer32):
    """Custom type apKalEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApKalEnable_Type.__name__ = "Integer32"
_ApKalEnable_Object = MibTableColumn
apKalEnable = _ApKalEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 4),
    _ApKalEnable_Type()
)
apKalEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalEnable.setStatus("current")
_ApKalIPAddress_Type = IpAddress
_ApKalIPAddress_Object = MibTableColumn
apKalIPAddress = _ApKalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 5),
    _ApKalIPAddress_Type()
)
apKalIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalIPAddress.setStatus("current")


class _ApKalPort_Type(Integer32):
    """Custom type apKalPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApKalPort_Type.__name__ = "Integer32"
_ApKalPort_Object = MibTableColumn
apKalPort = _ApKalPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 6),
    _ApKalPort_Type()
)
apKalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalPort.setStatus("current")


class _ApKalType_Type(Integer32):
    """Custom type apKalType based on Integer32"""
    defaultValue = 1

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
        *(("ftp", 3),
          ("http", 2),
          ("icmp", 1),
          ("script", 5),
          ("tcp", 4))
    )


_ApKalType_Type.__name__ = "Integer32"
_ApKalType_Object = MibTableColumn
apKalType = _ApKalType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 7),
    _ApKalType_Type()
)
apKalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalType.setStatus("current")


class _ApKalFrequency_Type(Integer32):
    """Custom type apKalFrequency based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApKalFrequency_Type.__name__ = "Integer32"
_ApKalFrequency_Object = MibTableColumn
apKalFrequency = _ApKalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 8),
    _ApKalFrequency_Type()
)
apKalFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalFrequency.setStatus("current")


class _ApKalMaxFailure_Type(Integer32):
    """Custom type apKalMaxFailure based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApKalMaxFailure_Type.__name__ = "Integer32"
_ApKalMaxFailure_Object = MibTableColumn
apKalMaxFailure = _ApKalMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 9),
    _ApKalMaxFailure_Type()
)
apKalMaxFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalMaxFailure.setStatus("current")


class _ApKalRetryPeriod_Type(Integer32):
    """Custom type apKalRetryPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApKalRetryPeriod_Type.__name__ = "Integer32"
_ApKalRetryPeriod_Object = MibTableColumn
apKalRetryPeriod = _ApKalRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 10),
    _ApKalRetryPeriod_Type()
)
apKalRetryPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalRetryPeriod.setStatus("current")


class _ApKalUri_Type(DisplayString):
    """Custom type apKalUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApKalUri_Type.__name__ = "DisplayString"
_ApKalUri_Object = MibTableColumn
apKalUri = _ApKalUri_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 11),
    _ApKalUri_Type()
)
apKalUri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalUri.setStatus("current")


class _ApKalMethod_Type(Integer32):
    """Custom type apKalMethod based on Integer32"""
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
        *(("get", 2),
          ("head", 1),
          ("post", 3))
    )


_ApKalMethod_Type.__name__ = "Integer32"
_ApKalMethod_Object = MibTableColumn
apKalMethod = _ApKalMethod_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 12),
    _ApKalMethod_Type()
)
apKalMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalMethod.setStatus("current")


class _ApKalPersistence_Type(Integer32):
    """Custom type apKalPersistence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-persistent", 0),
          ("persistent", 1))
    )


_ApKalPersistence_Type.__name__ = "Integer32"
_ApKalPersistence_Object = MibTableColumn
apKalPersistence = _ApKalPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 13),
    _ApKalPersistence_Type()
)
apKalPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalPersistence.setStatus("current")


class _ApKalState_Type(Integer32):
    """Custom type apKalState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alive", 4),
          ("down", 2),
          ("dying", 5),
          ("suspended", 1))
    )


_ApKalState_Type.__name__ = "Integer32"
_ApKalState_Object = MibTableColumn
apKalState = _ApKalState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 14),
    _ApKalState_Type()
)
apKalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apKalState.setStatus("current")


class _ApKalHash_Type(DisplayString):
    """Custom type apKalHash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApKalHash_Type.__name__ = "DisplayString"
_ApKalHash_Object = MibTableColumn
apKalHash = _ApKalHash_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 15),
    _ApKalHash_Type()
)
apKalHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalHash.setStatus("current")


class _ApKalFtpRecordName_Type(DisplayString):
    """Custom type apKalFtpRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApKalFtpRecordName_Type.__name__ = "DisplayString"
_ApKalFtpRecordName_Object = MibTableColumn
apKalFtpRecordName = _ApKalFtpRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 16),
    _ApKalFtpRecordName_Type()
)
apKalFtpRecordName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalFtpRecordName.setStatus("current")


class _ApKalScriptName_Type(DisplayString):
    """Custom type apKalScriptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApKalScriptName_Type.__name__ = "DisplayString"
_ApKalScriptName_Object = MibTableColumn
apKalScriptName = _ApKalScriptName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 17),
    _ApKalScriptName_Type()
)
apKalScriptName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalScriptName.setStatus("current")


class _ApKalScriptArgs_Type(DisplayString):
    """Custom type apKalScriptArgs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApKalScriptArgs_Type.__name__ = "DisplayString"
_ApKalScriptArgs_Object = MibTableColumn
apKalScriptArgs = _ApKalScriptArgs_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 18),
    _ApKalScriptArgs_Type()
)
apKalScriptArgs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalScriptArgs.setStatus("current")


class _ApKalScriptLog_Type(DisplayString):
    """Custom type apKalScriptLog based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApKalScriptLog_Type.__name__ = "DisplayString"
_ApKalScriptLog_Object = MibTableColumn
apKalScriptLog = _ApKalScriptLog_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 46, 2, 1, 19),
    _ApKalScriptLog_Type()
)
apKalScriptLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKalScriptLog.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KALEXT-MIB",
    **{"apKalExtMib": apKalExtMib,
       "apKalTable": apKalTable,
       "apKalEntry": apKalEntry,
       "apKalName": apKalName,
       "apKalStatus": apKalStatus,
       "apKalDescription": apKalDescription,
       "apKalEnable": apKalEnable,
       "apKalIPAddress": apKalIPAddress,
       "apKalPort": apKalPort,
       "apKalType": apKalType,
       "apKalFrequency": apKalFrequency,
       "apKalMaxFailure": apKalMaxFailure,
       "apKalRetryPeriod": apKalRetryPeriod,
       "apKalUri": apKalUri,
       "apKalMethod": apKalMethod,
       "apKalPersistence": apKalPersistence,
       "apKalState": apKalState,
       "apKalHash": apKalHash,
       "apKalFtpRecordName": apKalFtpRecordName,
       "apKalScriptName": apKalScriptName,
       "apKalScriptArgs": apKalScriptArgs,
       "apKalScriptLog": apKalScriptLog}
)
