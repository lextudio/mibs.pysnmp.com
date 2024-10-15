# SNMP MIB module (CXDial-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXDial-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:20 2024
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

(Alias,
 cxDial) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxDial")

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

_CxDialTable_Object = MibTable
cxDialTable = _CxDialTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1)
)
if mibBuilder.loadTexts:
    cxDialTable.setStatus("mandatory")
_CxDialEntry_Object = MibTableRow
cxDialEntry = _CxDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1)
)
cxDialEntry.setIndexNames(
    (0, "CXDial-MIB", "cxDialEntryIndex"),
)
if mibBuilder.loadTexts:
    cxDialEntry.setStatus("mandatory")
_CxDialEntryIndex_Type = Integer32
_CxDialEntryIndex_Object = MibTableColumn
cxDialEntryIndex = _CxDialEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1, 1),
    _CxDialEntryIndex_Type()
)
cxDialEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxDialEntryIndex.setStatus("mandatory")


class _CxDialPhysicalType_Type(Integer32):
    """Custom type cxDialPhysicalType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtr", 1),
          ("isdn", 2))
    )


_CxDialPhysicalType_Type.__name__ = "Integer32"
_CxDialPhysicalType_Object = MibTableColumn
cxDialPhysicalType = _CxDialPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1, 2),
    _CxDialPhysicalType_Type()
)
cxDialPhysicalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxDialPhysicalType.setStatus("mandatory")


class _CxDialFunctionType_Type(Integer32):
    """Custom type cxDialFunctionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onCongestion", 2),
          ("onDemand", 1))
    )


_CxDialFunctionType_Type.__name__ = "Integer32"
_CxDialFunctionType_Object = MibTableColumn
cxDialFunctionType = _CxDialFunctionType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1, 3),
    _CxDialFunctionType_Type()
)
cxDialFunctionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxDialFunctionType.setStatus("mandatory")


class _CxDialRowStatus_Type(Integer32):
    """Custom type cxDialRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxDialRowStatus_Type.__name__ = "Integer32"
_CxDialRowStatus_Object = MibTableColumn
cxDialRowStatus = _CxDialRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1, 6),
    _CxDialRowStatus_Type()
)
cxDialRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxDialRowStatus.setStatus("mandatory")


class _CxDialInactivityTimer_Type(Integer32):
    """Custom type cxDialInactivityTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CxDialInactivityTimer_Type.__name__ = "Integer32"
_CxDialInactivityTimer_Object = MibTableColumn
cxDialInactivityTimer = _CxDialInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1, 10),
    _CxDialInactivityTimer_Type()
)
cxDialInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxDialInactivityTimer.setStatus("mandatory")


class _CxDialBackupPollingTimer_Type(Integer32):
    """Custom type cxDialBackupPollingTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CxDialBackupPollingTimer_Type.__name__ = "Integer32"
_CxDialBackupPollingTimer_Object = MibTableColumn
cxDialBackupPollingTimer = _CxDialBackupPollingTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1, 11),
    _CxDialBackupPollingTimer_Type()
)
cxDialBackupPollingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxDialBackupPollingTimer.setStatus("mandatory")


class _CxDialDelayTimer_Type(Integer32):
    """Custom type cxDialDelayTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CxDialDelayTimer_Type.__name__ = "Integer32"
_CxDialDelayTimer_Object = MibTableColumn
cxDialDelayTimer = _CxDialDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1, 12),
    _CxDialDelayTimer_Type()
)
cxDialDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxDialDelayTimer.setStatus("mandatory")
_CxDialIsdnBcmUSapAlias_Type = Alias
_CxDialIsdnBcmUSapAlias_Object = MibTableColumn
cxDialIsdnBcmUSapAlias = _CxDialIsdnBcmUSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1, 15),
    _CxDialIsdnBcmUSapAlias_Type()
)
cxDialIsdnBcmUSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxDialIsdnBcmUSapAlias.setStatus("mandatory")


class _CxDialIsdnBcmNbrOfBChannels_Type(Integer32):
    """Custom type cxDialIsdnBcmNbrOfBChannels based on Integer32"""
    defaultValue = 1


_CxDialIsdnBcmNbrOfBChannels_Object = MibTableColumn
cxDialIsdnBcmNbrOfBChannels = _CxDialIsdnBcmNbrOfBChannels_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1, 16),
    _CxDialIsdnBcmNbrOfBChannels_Type()
)
cxDialIsdnBcmNbrOfBChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxDialIsdnBcmNbrOfBChannels.setStatus("mandatory")


class _CxDialIsdnBcmDirectoryId_Type(Integer32):
    """Custom type cxDialIsdnBcmDirectoryId based on Integer32"""
    defaultValue = 1


_CxDialIsdnBcmDirectoryId_Object = MibTableColumn
cxDialIsdnBcmDirectoryId = _CxDialIsdnBcmDirectoryId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 1, 1, 17),
    _CxDialIsdnBcmDirectoryId_Type()
)
cxDialIsdnBcmDirectoryId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxDialIsdnBcmDirectoryId.setStatus("mandatory")


class _CxDialMibLevel_Type(Integer32):
    """Custom type cxDialMibLevel based on Integer32"""
    defaultValue = 0


_CxDialMibLevel_Object = MibScalar
cxDialMibLevel = _CxDialMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 46, 2),
    _CxDialMibLevel_Type()
)
cxDialMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxDialMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXDial-MIB",
    **{"cxDialTable": cxDialTable,
       "cxDialEntry": cxDialEntry,
       "cxDialEntryIndex": cxDialEntryIndex,
       "cxDialPhysicalType": cxDialPhysicalType,
       "cxDialFunctionType": cxDialFunctionType,
       "cxDialRowStatus": cxDialRowStatus,
       "cxDialInactivityTimer": cxDialInactivityTimer,
       "cxDialBackupPollingTimer": cxDialBackupPollingTimer,
       "cxDialDelayTimer": cxDialDelayTimer,
       "cxDialIsdnBcmUSapAlias": cxDialIsdnBcmUSapAlias,
       "cxDialIsdnBcmNbrOfBChannels": cxDialIsdnBcmNbrOfBChannels,
       "cxDialIsdnBcmDirectoryId": cxDialIsdnBcmDirectoryId,
       "cxDialMibLevel": cxDialMibLevel}
)
