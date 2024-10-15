# SNMP MIB module (WaveLAN-Roaming-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WaveLAN-Roaming-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:31 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(att_2,
 att_mgmt,
 wavelan) = mibBuilder.importSymbols(
    "WaveLAN-MIB",
    "att-2",
    "att-mgmt",
    "wavelan")


# MODULE-IDENTITY


# Types definitions



class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WavelanRoaming_ObjectIdentity = ObjectIdentity
wavelanRoaming = _WavelanRoaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3)
)
_WlrGenTable_Object = MibTable
wlrGenTable = _WlrGenTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 1)
)
if mibBuilder.loadTexts:
    wlrGenTable.setStatus("mandatory")
_WlrGenEntry_Object = MibTableRow
wlrGenEntry = _WlrGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 1, 1)
)
wlrGenEntry.setIndexNames(
    (0, "WaveLAN-Roaming-MIB", "wlrGenIndex"),
)
if mibBuilder.loadTexts:
    wlrGenEntry.setStatus("mandatory")
_WlrGenIndex_Type = Integer32
_WlrGenIndex_Object = MibTableColumn
wlrGenIndex = _WlrGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 1, 1, 1),
    _WlrGenIndex_Type()
)
wlrGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrGenIndex.setStatus("mandatory")


class _WlrDomainId_Type(OctetString):
    """Custom type wlrDomainId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WlrDomainId_Type.__name__ = "OctetString"
_WlrDomainId_Object = MibTableColumn
wlrDomainId = _WlrDomainId_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 1, 1, 2),
    _WlrDomainId_Type()
)
wlrDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlrDomainId.setStatus("mandatory")


class _WlrBeaconKey_Type(OctetString):
    """Custom type wlrBeaconKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WlrBeaconKey_Type.__name__ = "OctetString"
_WlrBeaconKey_Object = MibTableColumn
wlrBeaconKey = _WlrBeaconKey_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 1, 1, 3),
    _WlrBeaconKey_Type()
)
wlrBeaconKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlrBeaconKey.setStatus("mandatory")
_WlrMsTable_Object = MibTable
wlrMsTable = _WlrMsTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2)
)
if mibBuilder.loadTexts:
    wlrMsTable.setStatus("mandatory")
_WlrMsEntry_Object = MibTableRow
wlrMsEntry = _WlrMsEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1)
)
wlrMsEntry.setIndexNames(
    (0, "WaveLAN-Roaming-MIB", "wlrMsIndex"),
)
if mibBuilder.loadTexts:
    wlrMsEntry.setStatus("mandatory")
_WlrMsIndex_Type = Integer32
_WlrMsIndex_Object = MibTableColumn
wlrMsIndex = _WlrMsIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 1),
    _WlrMsIndex_Type()
)
wlrMsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsIndex.setStatus("mandatory")


class _WlrRetryLimit_Type(Integer32):
    """Custom type wlrRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WlrRetryLimit_Type.__name__ = "Integer32"
_WlrRetryLimit_Object = MibTableColumn
wlrRetryLimit = _WlrRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 2),
    _WlrRetryLimit_Type()
)
wlrRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlrRetryLimit.setStatus("mandatory")
_WlrNumberOfRecovers_Type = Integer32
_WlrNumberOfRecovers_Object = MibTableColumn
wlrNumberOfRecovers = _WlrNumberOfRecovers_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 3),
    _WlrNumberOfRecovers_Type()
)
wlrNumberOfRecovers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlrNumberOfRecovers.setStatus("mandatory")


class _WlrCommsQuality_Type(Integer32):
    """Custom type wlrCommsQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WlrCommsQuality_Type.__name__ = "Integer32"
_WlrCommsQuality_Object = MibTableColumn
wlrCommsQuality = _WlrCommsQuality_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 4),
    _WlrCommsQuality_Type()
)
wlrCommsQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrCommsQuality.setStatus("mandatory")


class _WlrCurrentApName_Type(DisplayString):
    """Custom type wlrCurrentApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WlrCurrentApName_Type.__name__ = "DisplayString"
_WlrCurrentApName_Object = MibTableColumn
wlrCurrentApName = _WlrCurrentApName_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 5),
    _WlrCurrentApName_Type()
)
wlrCurrentApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrCurrentApName.setStatus("mandatory")
_WlrMsSignOnFailures_Type = Counter32
_WlrMsSignOnFailures_Object = MibTableColumn
wlrMsSignOnFailures = _WlrMsSignOnFailures_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 6),
    _WlrMsSignOnFailures_Type()
)
wlrMsSignOnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsSignOnFailures.setStatus("mandatory")
_WlrMsHandovers_Type = Counter32
_WlrMsHandovers_Object = MibTableColumn
wlrMsHandovers = _WlrMsHandovers_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 7),
    _WlrMsHandovers_Type()
)
wlrMsHandovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsHandovers.setStatus("mandatory")
_WlrMsHandoverFailures_Type = Counter32
_WlrMsHandoverFailures_Object = MibTableColumn
wlrMsHandoverFailures = _WlrMsHandoverFailures_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 8),
    _WlrMsHandoverFailures_Type()
)
wlrMsHandoverFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsHandoverFailures.setStatus("mandatory")
_WlrMsBeaconsMissedNormal_Type = Counter32
_WlrMsBeaconsMissedNormal_Object = MibTableColumn
wlrMsBeaconsMissedNormal = _WlrMsBeaconsMissedNormal_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 9),
    _WlrMsBeaconsMissedNormal_Type()
)
wlrMsBeaconsMissedNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsBeaconsMissedNormal.setStatus("mandatory")
_WlrMsBeaconsMissedSearch_Type = Counter32
_WlrMsBeaconsMissedSearch_Object = MibTableColumn
wlrMsBeaconsMissedSearch = _WlrMsBeaconsMissedSearch_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 10),
    _WlrMsBeaconsMissedSearch_Type()
)
wlrMsBeaconsMissedSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsBeaconsMissedSearch.setStatus("mandatory")
_WlrMsRegularCellSearchEntered_Type = Counter32
_WlrMsRegularCellSearchEntered_Object = MibTableColumn
wlrMsRegularCellSearchEntered = _WlrMsRegularCellSearchEntered_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 11),
    _WlrMsRegularCellSearchEntered_Type()
)
wlrMsRegularCellSearchEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsRegularCellSearchEntered.setStatus("mandatory")
_WlrMsFastCellSearchEntered_Type = Counter32
_WlrMsFastCellSearchEntered_Object = MibTableColumn
wlrMsFastCellSearchEntered = _WlrMsFastCellSearchEntered_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 12),
    _WlrMsFastCellSearchEntered_Type()
)
wlrMsFastCellSearchEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsFastCellSearchEntered.setStatus("mandatory")
_WlrMsTimeInNormalMode_Type = Counter32
_WlrMsTimeInNormalMode_Object = MibTableColumn
wlrMsTimeInNormalMode = _WlrMsTimeInNormalMode_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 13),
    _WlrMsTimeInNormalMode_Type()
)
wlrMsTimeInNormalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsTimeInNormalMode.setStatus("mandatory")
_WlrMsTimeInRegularSearchMode_Type = Counter32
_WlrMsTimeInRegularSearchMode_Object = MibTableColumn
wlrMsTimeInRegularSearchMode = _WlrMsTimeInRegularSearchMode_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 14),
    _WlrMsTimeInRegularSearchMode_Type()
)
wlrMsTimeInRegularSearchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsTimeInRegularSearchMode.setStatus("mandatory")
_WlrMsTimeInFastSearchMode_Type = Counter32
_WlrMsTimeInFastSearchMode_Object = MibTableColumn
wlrMsTimeInFastSearchMode = _WlrMsTimeInFastSearchMode_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 2, 1, 15),
    _WlrMsTimeInFastSearchMode_Type()
)
wlrMsTimeInFastSearchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrMsTimeInFastSearchMode.setStatus("mandatory")
_WlrApTable_Object = MibTable
wlrApTable = _WlrApTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3)
)
if mibBuilder.loadTexts:
    wlrApTable.setStatus("mandatory")
_WlrApEntry_Object = MibTableRow
wlrApEntry = _WlrApEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3, 1)
)
wlrApEntry.setIndexNames(
    (0, "WaveLAN-Roaming-MIB", "wlrApIndex"),
)
if mibBuilder.loadTexts:
    wlrApEntry.setStatus("mandatory")
_WlrApIndex_Type = Integer32
_WlrApIndex_Object = MibTableColumn
wlrApIndex = _WlrApIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3, 1, 1),
    _WlrApIndex_Type()
)
wlrApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrApIndex.setStatus("mandatory")


class _WlrStopCellSearchThreshold_Type(Integer32):
    """Custom type wlrStopCellSearchThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WlrStopCellSearchThreshold_Type.__name__ = "Integer32"
_WlrStopCellSearchThreshold_Object = MibTableColumn
wlrStopCellSearchThreshold = _WlrStopCellSearchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3, 1, 2),
    _WlrStopCellSearchThreshold_Type()
)
wlrStopCellSearchThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlrStopCellSearchThreshold.setStatus("mandatory")


class _WlrRegularCellSearchThreshold_Type(Integer32):
    """Custom type wlrRegularCellSearchThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WlrRegularCellSearchThreshold_Type.__name__ = "Integer32"
_WlrRegularCellSearchThreshold_Object = MibTableColumn
wlrRegularCellSearchThreshold = _WlrRegularCellSearchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3, 1, 3),
    _WlrRegularCellSearchThreshold_Type()
)
wlrRegularCellSearchThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlrRegularCellSearchThreshold.setStatus("mandatory")


class _WlrFastCellSearchThreshold_Type(Integer32):
    """Custom type wlrFastCellSearchThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WlrFastCellSearchThreshold_Type.__name__ = "Integer32"
_WlrFastCellSearchThreshold_Object = MibTableColumn
wlrFastCellSearchThreshold = _WlrFastCellSearchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3, 1, 4),
    _WlrFastCellSearchThreshold_Type()
)
wlrFastCellSearchThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlrFastCellSearchThreshold.setStatus("mandatory")
_WlrBeaconInterval_Type = Timeout
_WlrBeaconInterval_Object = MibTableColumn
wlrBeaconInterval = _WlrBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3, 1, 5),
    _WlrBeaconInterval_Type()
)
wlrBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlrBeaconInterval.setStatus("mandatory")
_WlrBeaconTimeout_Type = Timeout
_WlrBeaconTimeout_Object = MibTableColumn
wlrBeaconTimeout = _WlrBeaconTimeout_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3, 1, 6),
    _WlrBeaconTimeout_Type()
)
wlrBeaconTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlrBeaconTimeout.setStatus("mandatory")
_WlrApSignOnRequests_Type = Counter32
_WlrApSignOnRequests_Object = MibTableColumn
wlrApSignOnRequests = _WlrApSignOnRequests_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3, 1, 7),
    _WlrApSignOnRequests_Type()
)
wlrApSignOnRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrApSignOnRequests.setStatus("mandatory")
_WlrApHandoversSent_Type = Counter32
_WlrApHandoversSent_Object = MibTableColumn
wlrApHandoversSent = _WlrApHandoversSent_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3, 1, 8),
    _WlrApHandoversSent_Type()
)
wlrApHandoversSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrApHandoversSent.setStatus("mandatory")
_WlrApHandoversReceived_Type = Counter32
_WlrApHandoversReceived_Object = MibTableColumn
wlrApHandoversReceived = _WlrApHandoversReceived_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 3, 3, 1, 9),
    _WlrApHandoversReceived_Type()
)
wlrApHandoversReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlrApHandoversReceived.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WaveLAN-Roaming-MIB",
    **{"Timeout": Timeout,
       "wavelanRoaming": wavelanRoaming,
       "wlrGenTable": wlrGenTable,
       "wlrGenEntry": wlrGenEntry,
       "wlrGenIndex": wlrGenIndex,
       "wlrDomainId": wlrDomainId,
       "wlrBeaconKey": wlrBeaconKey,
       "wlrMsTable": wlrMsTable,
       "wlrMsEntry": wlrMsEntry,
       "wlrMsIndex": wlrMsIndex,
       "wlrRetryLimit": wlrRetryLimit,
       "wlrNumberOfRecovers": wlrNumberOfRecovers,
       "wlrCommsQuality": wlrCommsQuality,
       "wlrCurrentApName": wlrCurrentApName,
       "wlrMsSignOnFailures": wlrMsSignOnFailures,
       "wlrMsHandovers": wlrMsHandovers,
       "wlrMsHandoverFailures": wlrMsHandoverFailures,
       "wlrMsBeaconsMissedNormal": wlrMsBeaconsMissedNormal,
       "wlrMsBeaconsMissedSearch": wlrMsBeaconsMissedSearch,
       "wlrMsRegularCellSearchEntered": wlrMsRegularCellSearchEntered,
       "wlrMsFastCellSearchEntered": wlrMsFastCellSearchEntered,
       "wlrMsTimeInNormalMode": wlrMsTimeInNormalMode,
       "wlrMsTimeInRegularSearchMode": wlrMsTimeInRegularSearchMode,
       "wlrMsTimeInFastSearchMode": wlrMsTimeInFastSearchMode,
       "wlrApTable": wlrApTable,
       "wlrApEntry": wlrApEntry,
       "wlrApIndex": wlrApIndex,
       "wlrStopCellSearchThreshold": wlrStopCellSearchThreshold,
       "wlrRegularCellSearchThreshold": wlrRegularCellSearchThreshold,
       "wlrFastCellSearchThreshold": wlrFastCellSearchThreshold,
       "wlrBeaconInterval": wlrBeaconInterval,
       "wlrBeaconTimeout": wlrBeaconTimeout,
       "wlrApSignOnRequests": wlrApSignOnRequests,
       "wlrApHandoversSent": wlrApHandoversSent,
       "wlrApHandoversReceived": wlrApHandoversReceived}
)
