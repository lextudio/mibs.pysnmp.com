# SNMP MIB module (Nortel-Magellan-Passport-FrameRelayUniTraceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FrameRelayUniTraceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:51 2024
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

(frUni,
 frUniIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-FrameRelayUniMIB",
    "frUni",
    "frUniIndex")

(DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

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

_FrUniTrace_ObjectIdentity = ObjectIdentity
frUniTrace = _FrUniTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7)
)
_FrUniTraceRowStatusTable_Object = MibTable
frUniTraceRowStatusTable = _FrUniTraceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 1)
)
if mibBuilder.loadTexts:
    frUniTraceRowStatusTable.setStatus("mandatory")
_FrUniTraceRowStatusEntry_Object = MibTableRow
frUniTraceRowStatusEntry = _FrUniTraceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 1, 1)
)
frUniTraceRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniTraceMIB", "frUniTraceIndex"),
)
if mibBuilder.loadTexts:
    frUniTraceRowStatusEntry.setStatus("mandatory")
_FrUniTraceRowStatus_Type = RowStatus
_FrUniTraceRowStatus_Object = MibTableColumn
frUniTraceRowStatus = _FrUniTraceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 1, 1, 1),
    _FrUniTraceRowStatus_Type()
)
frUniTraceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniTraceRowStatus.setStatus("mandatory")
_FrUniTraceComponentName_Type = DisplayString
_FrUniTraceComponentName_Object = MibTableColumn
frUniTraceComponentName = _FrUniTraceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 1, 1, 2),
    _FrUniTraceComponentName_Type()
)
frUniTraceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniTraceComponentName.setStatus("mandatory")
_FrUniTraceStorageType_Type = StorageType
_FrUniTraceStorageType_Object = MibTableColumn
frUniTraceStorageType = _FrUniTraceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 1, 1, 4),
    _FrUniTraceStorageType_Type()
)
frUniTraceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniTraceStorageType.setStatus("mandatory")
_FrUniTraceIndex_Type = NonReplicated
_FrUniTraceIndex_Object = MibTableColumn
frUniTraceIndex = _FrUniTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 1, 1, 10),
    _FrUniTraceIndex_Type()
)
frUniTraceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniTraceIndex.setStatus("mandatory")
_FrUniTraceFilter_ObjectIdentity = ObjectIdentity
frUniTraceFilter = _FrUniTraceFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2)
)
_FrUniTraceFilterRowStatusTable_Object = MibTable
frUniTraceFilterRowStatusTable = _FrUniTraceFilterRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 1)
)
if mibBuilder.loadTexts:
    frUniTraceFilterRowStatusTable.setStatus("mandatory")
_FrUniTraceFilterRowStatusEntry_Object = MibTableRow
frUniTraceFilterRowStatusEntry = _FrUniTraceFilterRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 1, 1)
)
frUniTraceFilterRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniTraceMIB", "frUniTraceIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniTraceMIB", "frUniTraceFilterIndex"),
)
if mibBuilder.loadTexts:
    frUniTraceFilterRowStatusEntry.setStatus("mandatory")
_FrUniTraceFilterRowStatus_Type = RowStatus
_FrUniTraceFilterRowStatus_Object = MibTableColumn
frUniTraceFilterRowStatus = _FrUniTraceFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 1, 1, 1),
    _FrUniTraceFilterRowStatus_Type()
)
frUniTraceFilterRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniTraceFilterRowStatus.setStatus("mandatory")
_FrUniTraceFilterComponentName_Type = DisplayString
_FrUniTraceFilterComponentName_Object = MibTableColumn
frUniTraceFilterComponentName = _FrUniTraceFilterComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 1, 1, 2),
    _FrUniTraceFilterComponentName_Type()
)
frUniTraceFilterComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniTraceFilterComponentName.setStatus("mandatory")
_FrUniTraceFilterStorageType_Type = StorageType
_FrUniTraceFilterStorageType_Object = MibTableColumn
frUniTraceFilterStorageType = _FrUniTraceFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 1, 1, 4),
    _FrUniTraceFilterStorageType_Type()
)
frUniTraceFilterStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniTraceFilterStorageType.setStatus("mandatory")
_FrUniTraceFilterIndex_Type = NonReplicated
_FrUniTraceFilterIndex_Object = MibTableColumn
frUniTraceFilterIndex = _FrUniTraceFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 1, 1, 10),
    _FrUniTraceFilterIndex_Type()
)
frUniTraceFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniTraceFilterIndex.setStatus("mandatory")
_FrUniTraceFilterOperationalTable_Object = MibTable
frUniTraceFilterOperationalTable = _FrUniTraceFilterOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 10)
)
if mibBuilder.loadTexts:
    frUniTraceFilterOperationalTable.setStatus("mandatory")
_FrUniTraceFilterOperationalEntry_Object = MibTableRow
frUniTraceFilterOperationalEntry = _FrUniTraceFilterOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 10, 1)
)
frUniTraceFilterOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniTraceMIB", "frUniTraceIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniTraceMIB", "frUniTraceFilterIndex"),
)
if mibBuilder.loadTexts:
    frUniTraceFilterOperationalEntry.setStatus("mandatory")


class _FrUniTraceFilterTraceType_Type(OctetString):
    """Custom type frUniTraceFilterTraceType based on OctetString"""
    defaultHexValue = "e0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniTraceFilterTraceType_Type.__name__ = "OctetString"
_FrUniTraceFilterTraceType_Object = MibTableColumn
frUniTraceFilterTraceType = _FrUniTraceFilterTraceType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 10, 1, 1),
    _FrUniTraceFilterTraceType_Type()
)
frUniTraceFilterTraceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniTraceFilterTraceType.setStatus("mandatory")


class _FrUniTraceFilterTracedDlci_Type(Unsigned32):
    """Custom type frUniTraceFilterTracedDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_FrUniTraceFilterTracedDlci_Type.__name__ = "Unsigned32"
_FrUniTraceFilterTracedDlci_Object = MibTableColumn
frUniTraceFilterTracedDlci = _FrUniTraceFilterTracedDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 10, 1, 2),
    _FrUniTraceFilterTracedDlci_Type()
)
frUniTraceFilterTracedDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniTraceFilterTracedDlci.setStatus("mandatory")


class _FrUniTraceFilterDirection_Type(OctetString):
    """Custom type frUniTraceFilterDirection based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniTraceFilterDirection_Type.__name__ = "OctetString"
_FrUniTraceFilterDirection_Object = MibTableColumn
frUniTraceFilterDirection = _FrUniTraceFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 10, 1, 3),
    _FrUniTraceFilterDirection_Type()
)
frUniTraceFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniTraceFilterDirection.setStatus("mandatory")


class _FrUniTraceFilterTracedLength_Type(Unsigned32):
    """Custom type frUniTraceFilterTracedLength based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_FrUniTraceFilterTracedLength_Type.__name__ = "Unsigned32"
_FrUniTraceFilterTracedLength_Object = MibTableColumn
frUniTraceFilterTracedLength = _FrUniTraceFilterTracedLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 2, 10, 1, 4),
    _FrUniTraceFilterTracedLength_Type()
)
frUniTraceFilterTracedLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniTraceFilterTracedLength.setStatus("mandatory")
_FrUniTraceOperationalTable_Object = MibTable
frUniTraceOperationalTable = _FrUniTraceOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 10)
)
if mibBuilder.loadTexts:
    frUniTraceOperationalTable.setStatus("mandatory")
_FrUniTraceOperationalEntry_Object = MibTableRow
frUniTraceOperationalEntry = _FrUniTraceOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 10, 1)
)
frUniTraceOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniTraceMIB", "frUniTraceIndex"),
)
if mibBuilder.loadTexts:
    frUniTraceOperationalEntry.setStatus("mandatory")


class _FrUniTraceReceiverName_Type(AsciiString):
    """Custom type frUniTraceReceiverName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FrUniTraceReceiverName_Type.__name__ = "AsciiString"
_FrUniTraceReceiverName_Object = MibTableColumn
frUniTraceReceiverName = _FrUniTraceReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 10, 1, 2),
    _FrUniTraceReceiverName_Type()
)
frUniTraceReceiverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniTraceReceiverName.setStatus("mandatory")


class _FrUniTraceDuration_Type(Unsigned32):
    """Custom type frUniTraceDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_FrUniTraceDuration_Type.__name__ = "Unsigned32"
_FrUniTraceDuration_Object = MibTableColumn
frUniTraceDuration = _FrUniTraceDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 10, 1, 3),
    _FrUniTraceDuration_Type()
)
frUniTraceDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniTraceDuration.setStatus("mandatory")


class _FrUniTraceQueueLimit_Type(Unsigned32):
    """Custom type frUniTraceQueueLimit based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FrUniTraceQueueLimit_Type.__name__ = "Unsigned32"
_FrUniTraceQueueLimit_Object = MibTableColumn
frUniTraceQueueLimit = _FrUniTraceQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 10, 1, 4),
    _FrUniTraceQueueLimit_Type()
)
frUniTraceQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniTraceQueueLimit.setStatus("mandatory")
_FrUniTraceSession_Type = RowPointer
_FrUniTraceSession_Object = MibTableColumn
frUniTraceSession = _FrUniTraceSession_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 7, 10, 1, 5),
    _FrUniTraceSession_Type()
)
frUniTraceSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniTraceSession.setStatus("mandatory")
_FrameRelayUniTraceMIB_ObjectIdentity = ObjectIdentity
frameRelayUniTraceMIB = _FrameRelayUniTraceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 105)
)
_FrameRelayUniTraceGroup_ObjectIdentity = ObjectIdentity
frameRelayUniTraceGroup = _FrameRelayUniTraceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 105, 1)
)
_FrameRelayUniTraceGroupBD_ObjectIdentity = ObjectIdentity
frameRelayUniTraceGroupBD = _FrameRelayUniTraceGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 105, 1, 4)
)
_FrameRelayUniTraceGroupBD01_ObjectIdentity = ObjectIdentity
frameRelayUniTraceGroupBD01 = _FrameRelayUniTraceGroupBD01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 105, 1, 4, 2)
)
_FrameRelayUniTraceGroupBD01A_ObjectIdentity = ObjectIdentity
frameRelayUniTraceGroupBD01A = _FrameRelayUniTraceGroupBD01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 105, 1, 4, 2, 2)
)
_FrameRelayUniTraceCapabilities_ObjectIdentity = ObjectIdentity
frameRelayUniTraceCapabilities = _FrameRelayUniTraceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 105, 3)
)
_FrameRelayUniTraceCapabilitiesBD_ObjectIdentity = ObjectIdentity
frameRelayUniTraceCapabilitiesBD = _FrameRelayUniTraceCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 105, 3, 4)
)
_FrameRelayUniTraceCapabilitiesBD01_ObjectIdentity = ObjectIdentity
frameRelayUniTraceCapabilitiesBD01 = _FrameRelayUniTraceCapabilitiesBD01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 105, 3, 4, 2)
)
_FrameRelayUniTraceCapabilitiesBD01A_ObjectIdentity = ObjectIdentity
frameRelayUniTraceCapabilitiesBD01A = _FrameRelayUniTraceCapabilitiesBD01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 105, 3, 4, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FrameRelayUniTraceMIB",
    **{"frUniTrace": frUniTrace,
       "frUniTraceRowStatusTable": frUniTraceRowStatusTable,
       "frUniTraceRowStatusEntry": frUniTraceRowStatusEntry,
       "frUniTraceRowStatus": frUniTraceRowStatus,
       "frUniTraceComponentName": frUniTraceComponentName,
       "frUniTraceStorageType": frUniTraceStorageType,
       "frUniTraceIndex": frUniTraceIndex,
       "frUniTraceFilter": frUniTraceFilter,
       "frUniTraceFilterRowStatusTable": frUniTraceFilterRowStatusTable,
       "frUniTraceFilterRowStatusEntry": frUniTraceFilterRowStatusEntry,
       "frUniTraceFilterRowStatus": frUniTraceFilterRowStatus,
       "frUniTraceFilterComponentName": frUniTraceFilterComponentName,
       "frUniTraceFilterStorageType": frUniTraceFilterStorageType,
       "frUniTraceFilterIndex": frUniTraceFilterIndex,
       "frUniTraceFilterOperationalTable": frUniTraceFilterOperationalTable,
       "frUniTraceFilterOperationalEntry": frUniTraceFilterOperationalEntry,
       "frUniTraceFilterTraceType": frUniTraceFilterTraceType,
       "frUniTraceFilterTracedDlci": frUniTraceFilterTracedDlci,
       "frUniTraceFilterDirection": frUniTraceFilterDirection,
       "frUniTraceFilterTracedLength": frUniTraceFilterTracedLength,
       "frUniTraceOperationalTable": frUniTraceOperationalTable,
       "frUniTraceOperationalEntry": frUniTraceOperationalEntry,
       "frUniTraceReceiverName": frUniTraceReceiverName,
       "frUniTraceDuration": frUniTraceDuration,
       "frUniTraceQueueLimit": frUniTraceQueueLimit,
       "frUniTraceSession": frUniTraceSession,
       "frameRelayUniTraceMIB": frameRelayUniTraceMIB,
       "frameRelayUniTraceGroup": frameRelayUniTraceGroup,
       "frameRelayUniTraceGroupBD": frameRelayUniTraceGroupBD,
       "frameRelayUniTraceGroupBD01": frameRelayUniTraceGroupBD01,
       "frameRelayUniTraceGroupBD01A": frameRelayUniTraceGroupBD01A,
       "frameRelayUniTraceCapabilities": frameRelayUniTraceCapabilities,
       "frameRelayUniTraceCapabilitiesBD": frameRelayUniTraceCapabilitiesBD,
       "frameRelayUniTraceCapabilitiesBD01": frameRelayUniTraceCapabilitiesBD01,
       "frameRelayUniTraceCapabilitiesBD01A": frameRelayUniTraceCapabilitiesBD01A}
)
