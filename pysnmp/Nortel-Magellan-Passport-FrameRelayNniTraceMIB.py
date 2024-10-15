# SNMP MIB module (Nortel-Magellan-Passport-FrameRelayNniTraceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FrameRelayNniTraceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:49 2024
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

(frNni,
 frNniIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-FrameRelayNniMIB",
    "frNni",
    "frNniIndex")

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

_FrNniTrace_ObjectIdentity = ObjectIdentity
frNniTrace = _FrNniTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7)
)
_FrNniTraceRowStatusTable_Object = MibTable
frNniTraceRowStatusTable = _FrNniTraceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1)
)
if mibBuilder.loadTexts:
    frNniTraceRowStatusTable.setStatus("mandatory")
_FrNniTraceRowStatusEntry_Object = MibTableRow
frNniTraceRowStatusEntry = _FrNniTraceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1, 1)
)
frNniTraceRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceIndex"),
)
if mibBuilder.loadTexts:
    frNniTraceRowStatusEntry.setStatus("mandatory")
_FrNniTraceRowStatus_Type = RowStatus
_FrNniTraceRowStatus_Object = MibTableColumn
frNniTraceRowStatus = _FrNniTraceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1, 1, 1),
    _FrNniTraceRowStatus_Type()
)
frNniTraceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniTraceRowStatus.setStatus("mandatory")
_FrNniTraceComponentName_Type = DisplayString
_FrNniTraceComponentName_Object = MibTableColumn
frNniTraceComponentName = _FrNniTraceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1, 1, 2),
    _FrNniTraceComponentName_Type()
)
frNniTraceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniTraceComponentName.setStatus("mandatory")
_FrNniTraceStorageType_Type = StorageType
_FrNniTraceStorageType_Object = MibTableColumn
frNniTraceStorageType = _FrNniTraceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1, 1, 4),
    _FrNniTraceStorageType_Type()
)
frNniTraceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniTraceStorageType.setStatus("mandatory")
_FrNniTraceIndex_Type = NonReplicated
_FrNniTraceIndex_Object = MibTableColumn
frNniTraceIndex = _FrNniTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1, 1, 10),
    _FrNniTraceIndex_Type()
)
frNniTraceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniTraceIndex.setStatus("mandatory")
_FrNniTraceFilter_ObjectIdentity = ObjectIdentity
frNniTraceFilter = _FrNniTraceFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2)
)
_FrNniTraceFilterRowStatusTable_Object = MibTable
frNniTraceFilterRowStatusTable = _FrNniTraceFilterRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1)
)
if mibBuilder.loadTexts:
    frNniTraceFilterRowStatusTable.setStatus("mandatory")
_FrNniTraceFilterRowStatusEntry_Object = MibTableRow
frNniTraceFilterRowStatusEntry = _FrNniTraceFilterRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1, 1)
)
frNniTraceFilterRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceFilterIndex"),
)
if mibBuilder.loadTexts:
    frNniTraceFilterRowStatusEntry.setStatus("mandatory")
_FrNniTraceFilterRowStatus_Type = RowStatus
_FrNniTraceFilterRowStatus_Object = MibTableColumn
frNniTraceFilterRowStatus = _FrNniTraceFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1, 1, 1),
    _FrNniTraceFilterRowStatus_Type()
)
frNniTraceFilterRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniTraceFilterRowStatus.setStatus("mandatory")
_FrNniTraceFilterComponentName_Type = DisplayString
_FrNniTraceFilterComponentName_Object = MibTableColumn
frNniTraceFilterComponentName = _FrNniTraceFilterComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1, 1, 2),
    _FrNniTraceFilterComponentName_Type()
)
frNniTraceFilterComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniTraceFilterComponentName.setStatus("mandatory")
_FrNniTraceFilterStorageType_Type = StorageType
_FrNniTraceFilterStorageType_Object = MibTableColumn
frNniTraceFilterStorageType = _FrNniTraceFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1, 1, 4),
    _FrNniTraceFilterStorageType_Type()
)
frNniTraceFilterStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniTraceFilterStorageType.setStatus("mandatory")
_FrNniTraceFilterIndex_Type = NonReplicated
_FrNniTraceFilterIndex_Object = MibTableColumn
frNniTraceFilterIndex = _FrNniTraceFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1, 1, 10),
    _FrNniTraceFilterIndex_Type()
)
frNniTraceFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniTraceFilterIndex.setStatus("mandatory")
_FrNniTraceFilterOperationalTable_Object = MibTable
frNniTraceFilterOperationalTable = _FrNniTraceFilterOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10)
)
if mibBuilder.loadTexts:
    frNniTraceFilterOperationalTable.setStatus("mandatory")
_FrNniTraceFilterOperationalEntry_Object = MibTableRow
frNniTraceFilterOperationalEntry = _FrNniTraceFilterOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10, 1)
)
frNniTraceFilterOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceFilterIndex"),
)
if mibBuilder.loadTexts:
    frNniTraceFilterOperationalEntry.setStatus("mandatory")


class _FrNniTraceFilterTraceType_Type(OctetString):
    """Custom type frNniTraceFilterTraceType based on OctetString"""
    defaultHexValue = "e0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniTraceFilterTraceType_Type.__name__ = "OctetString"
_FrNniTraceFilterTraceType_Object = MibTableColumn
frNniTraceFilterTraceType = _FrNniTraceFilterTraceType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10, 1, 1),
    _FrNniTraceFilterTraceType_Type()
)
frNniTraceFilterTraceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniTraceFilterTraceType.setStatus("mandatory")


class _FrNniTraceFilterTracedDlci_Type(Unsigned32):
    """Custom type frNniTraceFilterTracedDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_FrNniTraceFilterTracedDlci_Type.__name__ = "Unsigned32"
_FrNniTraceFilterTracedDlci_Object = MibTableColumn
frNniTraceFilterTracedDlci = _FrNniTraceFilterTracedDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10, 1, 2),
    _FrNniTraceFilterTracedDlci_Type()
)
frNniTraceFilterTracedDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniTraceFilterTracedDlci.setStatus("mandatory")


class _FrNniTraceFilterDirection_Type(OctetString):
    """Custom type frNniTraceFilterDirection based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniTraceFilterDirection_Type.__name__ = "OctetString"
_FrNniTraceFilterDirection_Object = MibTableColumn
frNniTraceFilterDirection = _FrNniTraceFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10, 1, 3),
    _FrNniTraceFilterDirection_Type()
)
frNniTraceFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniTraceFilterDirection.setStatus("mandatory")


class _FrNniTraceFilterTracedLength_Type(Unsigned32):
    """Custom type frNniTraceFilterTracedLength based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_FrNniTraceFilterTracedLength_Type.__name__ = "Unsigned32"
_FrNniTraceFilterTracedLength_Object = MibTableColumn
frNniTraceFilterTracedLength = _FrNniTraceFilterTracedLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10, 1, 4),
    _FrNniTraceFilterTracedLength_Type()
)
frNniTraceFilterTracedLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniTraceFilterTracedLength.setStatus("mandatory")
_FrNniTraceOperationalTable_Object = MibTable
frNniTraceOperationalTable = _FrNniTraceOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10)
)
if mibBuilder.loadTexts:
    frNniTraceOperationalTable.setStatus("mandatory")
_FrNniTraceOperationalEntry_Object = MibTableRow
frNniTraceOperationalEntry = _FrNniTraceOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10, 1)
)
frNniTraceOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceIndex"),
)
if mibBuilder.loadTexts:
    frNniTraceOperationalEntry.setStatus("mandatory")


class _FrNniTraceReceiverName_Type(AsciiString):
    """Custom type frNniTraceReceiverName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FrNniTraceReceiverName_Type.__name__ = "AsciiString"
_FrNniTraceReceiverName_Object = MibTableColumn
frNniTraceReceiverName = _FrNniTraceReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10, 1, 2),
    _FrNniTraceReceiverName_Type()
)
frNniTraceReceiverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniTraceReceiverName.setStatus("mandatory")


class _FrNniTraceDuration_Type(Unsigned32):
    """Custom type frNniTraceDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_FrNniTraceDuration_Type.__name__ = "Unsigned32"
_FrNniTraceDuration_Object = MibTableColumn
frNniTraceDuration = _FrNniTraceDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10, 1, 3),
    _FrNniTraceDuration_Type()
)
frNniTraceDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniTraceDuration.setStatus("mandatory")


class _FrNniTraceQueueLimit_Type(Unsigned32):
    """Custom type frNniTraceQueueLimit based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FrNniTraceQueueLimit_Type.__name__ = "Unsigned32"
_FrNniTraceQueueLimit_Object = MibTableColumn
frNniTraceQueueLimit = _FrNniTraceQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10, 1, 4),
    _FrNniTraceQueueLimit_Type()
)
frNniTraceQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniTraceQueueLimit.setStatus("mandatory")
_FrNniTraceSession_Type = RowPointer
_FrNniTraceSession_Object = MibTableColumn
frNniTraceSession = _FrNniTraceSession_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10, 1, 5),
    _FrNniTraceSession_Type()
)
frNniTraceSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniTraceSession.setStatus("mandatory")
_FrameRelayNniTraceMIB_ObjectIdentity = ObjectIdentity
frameRelayNniTraceMIB = _FrameRelayNniTraceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106)
)
_FrameRelayNniTraceGroup_ObjectIdentity = ObjectIdentity
frameRelayNniTraceGroup = _FrameRelayNniTraceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 1)
)
_FrameRelayNniTraceGroupBD_ObjectIdentity = ObjectIdentity
frameRelayNniTraceGroupBD = _FrameRelayNniTraceGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 1, 4)
)
_FrameRelayNniTraceGroupBD01_ObjectIdentity = ObjectIdentity
frameRelayNniTraceGroupBD01 = _FrameRelayNniTraceGroupBD01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 1, 4, 2)
)
_FrameRelayNniTraceGroupBD01A_ObjectIdentity = ObjectIdentity
frameRelayNniTraceGroupBD01A = _FrameRelayNniTraceGroupBD01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 1, 4, 2, 2)
)
_FrameRelayNniTraceCapabilities_ObjectIdentity = ObjectIdentity
frameRelayNniTraceCapabilities = _FrameRelayNniTraceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 3)
)
_FrameRelayNniTraceCapabilitiesBD_ObjectIdentity = ObjectIdentity
frameRelayNniTraceCapabilitiesBD = _FrameRelayNniTraceCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 3, 4)
)
_FrameRelayNniTraceCapabilitiesBD01_ObjectIdentity = ObjectIdentity
frameRelayNniTraceCapabilitiesBD01 = _FrameRelayNniTraceCapabilitiesBD01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 3, 4, 2)
)
_FrameRelayNniTraceCapabilitiesBD01A_ObjectIdentity = ObjectIdentity
frameRelayNniTraceCapabilitiesBD01A = _FrameRelayNniTraceCapabilitiesBD01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 3, 4, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FrameRelayNniTraceMIB",
    **{"frNniTrace": frNniTrace,
       "frNniTraceRowStatusTable": frNniTraceRowStatusTable,
       "frNniTraceRowStatusEntry": frNniTraceRowStatusEntry,
       "frNniTraceRowStatus": frNniTraceRowStatus,
       "frNniTraceComponentName": frNniTraceComponentName,
       "frNniTraceStorageType": frNniTraceStorageType,
       "frNniTraceIndex": frNniTraceIndex,
       "frNniTraceFilter": frNniTraceFilter,
       "frNniTraceFilterRowStatusTable": frNniTraceFilterRowStatusTable,
       "frNniTraceFilterRowStatusEntry": frNniTraceFilterRowStatusEntry,
       "frNniTraceFilterRowStatus": frNniTraceFilterRowStatus,
       "frNniTraceFilterComponentName": frNniTraceFilterComponentName,
       "frNniTraceFilterStorageType": frNniTraceFilterStorageType,
       "frNniTraceFilterIndex": frNniTraceFilterIndex,
       "frNniTraceFilterOperationalTable": frNniTraceFilterOperationalTable,
       "frNniTraceFilterOperationalEntry": frNniTraceFilterOperationalEntry,
       "frNniTraceFilterTraceType": frNniTraceFilterTraceType,
       "frNniTraceFilterTracedDlci": frNniTraceFilterTracedDlci,
       "frNniTraceFilterDirection": frNniTraceFilterDirection,
       "frNniTraceFilterTracedLength": frNniTraceFilterTracedLength,
       "frNniTraceOperationalTable": frNniTraceOperationalTable,
       "frNniTraceOperationalEntry": frNniTraceOperationalEntry,
       "frNniTraceReceiverName": frNniTraceReceiverName,
       "frNniTraceDuration": frNniTraceDuration,
       "frNniTraceQueueLimit": frNniTraceQueueLimit,
       "frNniTraceSession": frNniTraceSession,
       "frameRelayNniTraceMIB": frameRelayNniTraceMIB,
       "frameRelayNniTraceGroup": frameRelayNniTraceGroup,
       "frameRelayNniTraceGroupBD": frameRelayNniTraceGroupBD,
       "frameRelayNniTraceGroupBD01": frameRelayNniTraceGroupBD01,
       "frameRelayNniTraceGroupBD01A": frameRelayNniTraceGroupBD01A,
       "frameRelayNniTraceCapabilities": frameRelayNniTraceCapabilities,
       "frameRelayNniTraceCapabilitiesBD": frameRelayNniTraceCapabilitiesBD,
       "frameRelayNniTraceCapabilitiesBD01": frameRelayNniTraceCapabilitiesBD01,
       "frameRelayNniTraceCapabilitiesBD01A": frameRelayNniTraceCapabilitiesBD01A}
)
