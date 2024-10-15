# SNMP MIB module (Nortel-MsCarrier-MscPassport-FrameRelayUniTraceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FrameRelayUniTraceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:31 2024
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

(mscFrUni,
 mscFrUniIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB",
    "mscFrUni",
    "mscFrUniIndex")

(DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscFrUniTrace_ObjectIdentity = ObjectIdentity
mscFrUniTrace = _MscFrUniTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7)
)
_MscFrUniTraceRowStatusTable_Object = MibTable
mscFrUniTraceRowStatusTable = _MscFrUniTraceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 1)
)
if mibBuilder.loadTexts:
    mscFrUniTraceRowStatusTable.setStatus("mandatory")
_MscFrUniTraceRowStatusEntry_Object = MibTableRow
mscFrUniTraceRowStatusEntry = _MscFrUniTraceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 1, 1)
)
mscFrUniTraceRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniTraceMIB", "mscFrUniTraceIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniTraceRowStatusEntry.setStatus("mandatory")
_MscFrUniTraceRowStatus_Type = RowStatus
_MscFrUniTraceRowStatus_Object = MibTableColumn
mscFrUniTraceRowStatus = _MscFrUniTraceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 1, 1, 1),
    _MscFrUniTraceRowStatus_Type()
)
mscFrUniTraceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniTraceRowStatus.setStatus("mandatory")
_MscFrUniTraceComponentName_Type = DisplayString
_MscFrUniTraceComponentName_Object = MibTableColumn
mscFrUniTraceComponentName = _MscFrUniTraceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 1, 1, 2),
    _MscFrUniTraceComponentName_Type()
)
mscFrUniTraceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniTraceComponentName.setStatus("mandatory")
_MscFrUniTraceStorageType_Type = StorageType
_MscFrUniTraceStorageType_Object = MibTableColumn
mscFrUniTraceStorageType = _MscFrUniTraceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 1, 1, 4),
    _MscFrUniTraceStorageType_Type()
)
mscFrUniTraceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniTraceStorageType.setStatus("mandatory")
_MscFrUniTraceIndex_Type = NonReplicated
_MscFrUniTraceIndex_Object = MibTableColumn
mscFrUniTraceIndex = _MscFrUniTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 1, 1, 10),
    _MscFrUniTraceIndex_Type()
)
mscFrUniTraceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniTraceIndex.setStatus("mandatory")
_MscFrUniTraceFilter_ObjectIdentity = ObjectIdentity
mscFrUniTraceFilter = _MscFrUniTraceFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2)
)
_MscFrUniTraceFilterRowStatusTable_Object = MibTable
mscFrUniTraceFilterRowStatusTable = _MscFrUniTraceFilterRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrUniTraceFilterRowStatusTable.setStatus("mandatory")
_MscFrUniTraceFilterRowStatusEntry_Object = MibTableRow
mscFrUniTraceFilterRowStatusEntry = _MscFrUniTraceFilterRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 1, 1)
)
mscFrUniTraceFilterRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniTraceMIB", "mscFrUniTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniTraceMIB", "mscFrUniTraceFilterIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniTraceFilterRowStatusEntry.setStatus("mandatory")
_MscFrUniTraceFilterRowStatus_Type = RowStatus
_MscFrUniTraceFilterRowStatus_Object = MibTableColumn
mscFrUniTraceFilterRowStatus = _MscFrUniTraceFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 1, 1, 1),
    _MscFrUniTraceFilterRowStatus_Type()
)
mscFrUniTraceFilterRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniTraceFilterRowStatus.setStatus("mandatory")
_MscFrUniTraceFilterComponentName_Type = DisplayString
_MscFrUniTraceFilterComponentName_Object = MibTableColumn
mscFrUniTraceFilterComponentName = _MscFrUniTraceFilterComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 1, 1, 2),
    _MscFrUniTraceFilterComponentName_Type()
)
mscFrUniTraceFilterComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniTraceFilterComponentName.setStatus("mandatory")
_MscFrUniTraceFilterStorageType_Type = StorageType
_MscFrUniTraceFilterStorageType_Object = MibTableColumn
mscFrUniTraceFilterStorageType = _MscFrUniTraceFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 1, 1, 4),
    _MscFrUniTraceFilterStorageType_Type()
)
mscFrUniTraceFilterStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniTraceFilterStorageType.setStatus("mandatory")
_MscFrUniTraceFilterIndex_Type = NonReplicated
_MscFrUniTraceFilterIndex_Object = MibTableColumn
mscFrUniTraceFilterIndex = _MscFrUniTraceFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 1, 1, 10),
    _MscFrUniTraceFilterIndex_Type()
)
mscFrUniTraceFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniTraceFilterIndex.setStatus("mandatory")
_MscFrUniTraceFilterOperationalTable_Object = MibTable
mscFrUniTraceFilterOperationalTable = _MscFrUniTraceFilterOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrUniTraceFilterOperationalTable.setStatus("mandatory")
_MscFrUniTraceFilterOperationalEntry_Object = MibTableRow
mscFrUniTraceFilterOperationalEntry = _MscFrUniTraceFilterOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 10, 1)
)
mscFrUniTraceFilterOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniTraceMIB", "mscFrUniTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniTraceMIB", "mscFrUniTraceFilterIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniTraceFilterOperationalEntry.setStatus("mandatory")


class _MscFrUniTraceFilterTraceType_Type(OctetString):
    """Custom type mscFrUniTraceFilterTraceType based on OctetString"""
    defaultHexValue = "e0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniTraceFilterTraceType_Type.__name__ = "OctetString"
_MscFrUniTraceFilterTraceType_Object = MibTableColumn
mscFrUniTraceFilterTraceType = _MscFrUniTraceFilterTraceType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 10, 1, 1),
    _MscFrUniTraceFilterTraceType_Type()
)
mscFrUniTraceFilterTraceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniTraceFilterTraceType.setStatus("mandatory")


class _MscFrUniTraceFilterTracedDlci_Type(Unsigned32):
    """Custom type mscFrUniTraceFilterTracedDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_MscFrUniTraceFilterTracedDlci_Type.__name__ = "Unsigned32"
_MscFrUniTraceFilterTracedDlci_Object = MibTableColumn
mscFrUniTraceFilterTracedDlci = _MscFrUniTraceFilterTracedDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 10, 1, 2),
    _MscFrUniTraceFilterTracedDlci_Type()
)
mscFrUniTraceFilterTracedDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniTraceFilterTracedDlci.setStatus("mandatory")


class _MscFrUniTraceFilterDirection_Type(OctetString):
    """Custom type mscFrUniTraceFilterDirection based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniTraceFilterDirection_Type.__name__ = "OctetString"
_MscFrUniTraceFilterDirection_Object = MibTableColumn
mscFrUniTraceFilterDirection = _MscFrUniTraceFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 10, 1, 3),
    _MscFrUniTraceFilterDirection_Type()
)
mscFrUniTraceFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniTraceFilterDirection.setStatus("mandatory")


class _MscFrUniTraceFilterTracedLength_Type(Unsigned32):
    """Custom type mscFrUniTraceFilterTracedLength based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_MscFrUniTraceFilterTracedLength_Type.__name__ = "Unsigned32"
_MscFrUniTraceFilterTracedLength_Object = MibTableColumn
mscFrUniTraceFilterTracedLength = _MscFrUniTraceFilterTracedLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 2, 10, 1, 4),
    _MscFrUniTraceFilterTracedLength_Type()
)
mscFrUniTraceFilterTracedLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniTraceFilterTracedLength.setStatus("mandatory")
_MscFrUniTraceOperationalTable_Object = MibTable
mscFrUniTraceOperationalTable = _MscFrUniTraceOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 10)
)
if mibBuilder.loadTexts:
    mscFrUniTraceOperationalTable.setStatus("mandatory")
_MscFrUniTraceOperationalEntry_Object = MibTableRow
mscFrUniTraceOperationalEntry = _MscFrUniTraceOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 10, 1)
)
mscFrUniTraceOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniTraceMIB", "mscFrUniTraceIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniTraceOperationalEntry.setStatus("mandatory")


class _MscFrUniTraceReceiverName_Type(AsciiString):
    """Custom type mscFrUniTraceReceiverName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscFrUniTraceReceiverName_Type.__name__ = "AsciiString"
_MscFrUniTraceReceiverName_Object = MibTableColumn
mscFrUniTraceReceiverName = _MscFrUniTraceReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 10, 1, 2),
    _MscFrUniTraceReceiverName_Type()
)
mscFrUniTraceReceiverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniTraceReceiverName.setStatus("mandatory")


class _MscFrUniTraceDuration_Type(Unsigned32):
    """Custom type mscFrUniTraceDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MscFrUniTraceDuration_Type.__name__ = "Unsigned32"
_MscFrUniTraceDuration_Object = MibTableColumn
mscFrUniTraceDuration = _MscFrUniTraceDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 10, 1, 3),
    _MscFrUniTraceDuration_Type()
)
mscFrUniTraceDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniTraceDuration.setStatus("mandatory")


class _MscFrUniTraceQueueLimit_Type(Unsigned32):
    """Custom type mscFrUniTraceQueueLimit based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscFrUniTraceQueueLimit_Type.__name__ = "Unsigned32"
_MscFrUniTraceQueueLimit_Object = MibTableColumn
mscFrUniTraceQueueLimit = _MscFrUniTraceQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 10, 1, 4),
    _MscFrUniTraceQueueLimit_Type()
)
mscFrUniTraceQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniTraceQueueLimit.setStatus("mandatory")
_MscFrUniTraceSession_Type = RowPointer
_MscFrUniTraceSession_Object = MibTableColumn
mscFrUniTraceSession = _MscFrUniTraceSession_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 7, 10, 1, 5),
    _MscFrUniTraceSession_Type()
)
mscFrUniTraceSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniTraceSession.setStatus("mandatory")
_FrameRelayUniTraceMIB_ObjectIdentity = ObjectIdentity
frameRelayUniTraceMIB = _FrameRelayUniTraceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 105)
)
_FrameRelayUniTraceGroup_ObjectIdentity = ObjectIdentity
frameRelayUniTraceGroup = _FrameRelayUniTraceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 105, 1)
)
_FrameRelayUniTraceGroupCA_ObjectIdentity = ObjectIdentity
frameRelayUniTraceGroupCA = _FrameRelayUniTraceGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 105, 1, 1)
)
_FrameRelayUniTraceGroupCA02_ObjectIdentity = ObjectIdentity
frameRelayUniTraceGroupCA02 = _FrameRelayUniTraceGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 105, 1, 1, 3)
)
_FrameRelayUniTraceGroupCA02A_ObjectIdentity = ObjectIdentity
frameRelayUniTraceGroupCA02A = _FrameRelayUniTraceGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 105, 1, 1, 3, 2)
)
_FrameRelayUniTraceCapabilities_ObjectIdentity = ObjectIdentity
frameRelayUniTraceCapabilities = _FrameRelayUniTraceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 105, 3)
)
_FrameRelayUniTraceCapabilitiesCA_ObjectIdentity = ObjectIdentity
frameRelayUniTraceCapabilitiesCA = _FrameRelayUniTraceCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 105, 3, 1)
)
_FrameRelayUniTraceCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frameRelayUniTraceCapabilitiesCA02 = _FrameRelayUniTraceCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 105, 3, 1, 3)
)
_FrameRelayUniTraceCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frameRelayUniTraceCapabilitiesCA02A = _FrameRelayUniTraceCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 105, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayUniTraceMIB",
    **{"mscFrUniTrace": mscFrUniTrace,
       "mscFrUniTraceRowStatusTable": mscFrUniTraceRowStatusTable,
       "mscFrUniTraceRowStatusEntry": mscFrUniTraceRowStatusEntry,
       "mscFrUniTraceRowStatus": mscFrUniTraceRowStatus,
       "mscFrUniTraceComponentName": mscFrUniTraceComponentName,
       "mscFrUniTraceStorageType": mscFrUniTraceStorageType,
       "mscFrUniTraceIndex": mscFrUniTraceIndex,
       "mscFrUniTraceFilter": mscFrUniTraceFilter,
       "mscFrUniTraceFilterRowStatusTable": mscFrUniTraceFilterRowStatusTable,
       "mscFrUniTraceFilterRowStatusEntry": mscFrUniTraceFilterRowStatusEntry,
       "mscFrUniTraceFilterRowStatus": mscFrUniTraceFilterRowStatus,
       "mscFrUniTraceFilterComponentName": mscFrUniTraceFilterComponentName,
       "mscFrUniTraceFilterStorageType": mscFrUniTraceFilterStorageType,
       "mscFrUniTraceFilterIndex": mscFrUniTraceFilterIndex,
       "mscFrUniTraceFilterOperationalTable": mscFrUniTraceFilterOperationalTable,
       "mscFrUniTraceFilterOperationalEntry": mscFrUniTraceFilterOperationalEntry,
       "mscFrUniTraceFilterTraceType": mscFrUniTraceFilterTraceType,
       "mscFrUniTraceFilterTracedDlci": mscFrUniTraceFilterTracedDlci,
       "mscFrUniTraceFilterDirection": mscFrUniTraceFilterDirection,
       "mscFrUniTraceFilterTracedLength": mscFrUniTraceFilterTracedLength,
       "mscFrUniTraceOperationalTable": mscFrUniTraceOperationalTable,
       "mscFrUniTraceOperationalEntry": mscFrUniTraceOperationalEntry,
       "mscFrUniTraceReceiverName": mscFrUniTraceReceiverName,
       "mscFrUniTraceDuration": mscFrUniTraceDuration,
       "mscFrUniTraceQueueLimit": mscFrUniTraceQueueLimit,
       "mscFrUniTraceSession": mscFrUniTraceSession,
       "frameRelayUniTraceMIB": frameRelayUniTraceMIB,
       "frameRelayUniTraceGroup": frameRelayUniTraceGroup,
       "frameRelayUniTraceGroupCA": frameRelayUniTraceGroupCA,
       "frameRelayUniTraceGroupCA02": frameRelayUniTraceGroupCA02,
       "frameRelayUniTraceGroupCA02A": frameRelayUniTraceGroupCA02A,
       "frameRelayUniTraceCapabilities": frameRelayUniTraceCapabilities,
       "frameRelayUniTraceCapabilitiesCA": frameRelayUniTraceCapabilitiesCA,
       "frameRelayUniTraceCapabilitiesCA02": frameRelayUniTraceCapabilitiesCA02,
       "frameRelayUniTraceCapabilitiesCA02A": frameRelayUniTraceCapabilitiesCA02A}
)
