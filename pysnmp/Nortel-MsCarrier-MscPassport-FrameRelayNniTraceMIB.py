# SNMP MIB module (Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:29 2024
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

(mscFrNni,
 mscFrNniIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB",
    "mscFrNni",
    "mscFrNniIndex")

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

_MscFrNniTrace_ObjectIdentity = ObjectIdentity
mscFrNniTrace = _MscFrNniTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7)
)
_MscFrNniTraceRowStatusTable_Object = MibTable
mscFrNniTraceRowStatusTable = _MscFrNniTraceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1)
)
if mibBuilder.loadTexts:
    mscFrNniTraceRowStatusTable.setStatus("mandatory")
_MscFrNniTraceRowStatusEntry_Object = MibTableRow
mscFrNniTraceRowStatusEntry = _MscFrNniTraceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1, 1)
)
mscFrNniTraceRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniTraceRowStatusEntry.setStatus("mandatory")
_MscFrNniTraceRowStatus_Type = RowStatus
_MscFrNniTraceRowStatus_Object = MibTableColumn
mscFrNniTraceRowStatus = _MscFrNniTraceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1, 1, 1),
    _MscFrNniTraceRowStatus_Type()
)
mscFrNniTraceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniTraceRowStatus.setStatus("mandatory")
_MscFrNniTraceComponentName_Type = DisplayString
_MscFrNniTraceComponentName_Object = MibTableColumn
mscFrNniTraceComponentName = _MscFrNniTraceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1, 1, 2),
    _MscFrNniTraceComponentName_Type()
)
mscFrNniTraceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniTraceComponentName.setStatus("mandatory")
_MscFrNniTraceStorageType_Type = StorageType
_MscFrNniTraceStorageType_Object = MibTableColumn
mscFrNniTraceStorageType = _MscFrNniTraceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1, 1, 4),
    _MscFrNniTraceStorageType_Type()
)
mscFrNniTraceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniTraceStorageType.setStatus("mandatory")
_MscFrNniTraceIndex_Type = NonReplicated
_MscFrNniTraceIndex_Object = MibTableColumn
mscFrNniTraceIndex = _MscFrNniTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1, 1, 10),
    _MscFrNniTraceIndex_Type()
)
mscFrNniTraceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniTraceIndex.setStatus("mandatory")
_MscFrNniTraceFilter_ObjectIdentity = ObjectIdentity
mscFrNniTraceFilter = _MscFrNniTraceFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2)
)
_MscFrNniTraceFilterRowStatusTable_Object = MibTable
mscFrNniTraceFilterRowStatusTable = _MscFrNniTraceFilterRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrNniTraceFilterRowStatusTable.setStatus("mandatory")
_MscFrNniTraceFilterRowStatusEntry_Object = MibTableRow
mscFrNniTraceFilterRowStatusEntry = _MscFrNniTraceFilterRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1, 1)
)
mscFrNniTraceFilterRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceFilterIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniTraceFilterRowStatusEntry.setStatus("mandatory")
_MscFrNniTraceFilterRowStatus_Type = RowStatus
_MscFrNniTraceFilterRowStatus_Object = MibTableColumn
mscFrNniTraceFilterRowStatus = _MscFrNniTraceFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1, 1, 1),
    _MscFrNniTraceFilterRowStatus_Type()
)
mscFrNniTraceFilterRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniTraceFilterRowStatus.setStatus("mandatory")
_MscFrNniTraceFilterComponentName_Type = DisplayString
_MscFrNniTraceFilterComponentName_Object = MibTableColumn
mscFrNniTraceFilterComponentName = _MscFrNniTraceFilterComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1, 1, 2),
    _MscFrNniTraceFilterComponentName_Type()
)
mscFrNniTraceFilterComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniTraceFilterComponentName.setStatus("mandatory")
_MscFrNniTraceFilterStorageType_Type = StorageType
_MscFrNniTraceFilterStorageType_Object = MibTableColumn
mscFrNniTraceFilterStorageType = _MscFrNniTraceFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1, 1, 4),
    _MscFrNniTraceFilterStorageType_Type()
)
mscFrNniTraceFilterStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniTraceFilterStorageType.setStatus("mandatory")
_MscFrNniTraceFilterIndex_Type = NonReplicated
_MscFrNniTraceFilterIndex_Object = MibTableColumn
mscFrNniTraceFilterIndex = _MscFrNniTraceFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1, 1, 10),
    _MscFrNniTraceFilterIndex_Type()
)
mscFrNniTraceFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniTraceFilterIndex.setStatus("mandatory")
_MscFrNniTraceFilterOperationalTable_Object = MibTable
mscFrNniTraceFilterOperationalTable = _MscFrNniTraceFilterOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrNniTraceFilterOperationalTable.setStatus("mandatory")
_MscFrNniTraceFilterOperationalEntry_Object = MibTableRow
mscFrNniTraceFilterOperationalEntry = _MscFrNniTraceFilterOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10, 1)
)
mscFrNniTraceFilterOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceFilterIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniTraceFilterOperationalEntry.setStatus("mandatory")


class _MscFrNniTraceFilterTraceType_Type(OctetString):
    """Custom type mscFrNniTraceFilterTraceType based on OctetString"""
    defaultHexValue = "e0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniTraceFilterTraceType_Type.__name__ = "OctetString"
_MscFrNniTraceFilterTraceType_Object = MibTableColumn
mscFrNniTraceFilterTraceType = _MscFrNniTraceFilterTraceType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10, 1, 1),
    _MscFrNniTraceFilterTraceType_Type()
)
mscFrNniTraceFilterTraceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniTraceFilterTraceType.setStatus("mandatory")


class _MscFrNniTraceFilterTracedDlci_Type(Unsigned32):
    """Custom type mscFrNniTraceFilterTracedDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_MscFrNniTraceFilterTracedDlci_Type.__name__ = "Unsigned32"
_MscFrNniTraceFilterTracedDlci_Object = MibTableColumn
mscFrNniTraceFilterTracedDlci = _MscFrNniTraceFilterTracedDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10, 1, 2),
    _MscFrNniTraceFilterTracedDlci_Type()
)
mscFrNniTraceFilterTracedDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniTraceFilterTracedDlci.setStatus("mandatory")


class _MscFrNniTraceFilterDirection_Type(OctetString):
    """Custom type mscFrNniTraceFilterDirection based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniTraceFilterDirection_Type.__name__ = "OctetString"
_MscFrNniTraceFilterDirection_Object = MibTableColumn
mscFrNniTraceFilterDirection = _MscFrNniTraceFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10, 1, 3),
    _MscFrNniTraceFilterDirection_Type()
)
mscFrNniTraceFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniTraceFilterDirection.setStatus("mandatory")


class _MscFrNniTraceFilterTracedLength_Type(Unsigned32):
    """Custom type mscFrNniTraceFilterTracedLength based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_MscFrNniTraceFilterTracedLength_Type.__name__ = "Unsigned32"
_MscFrNniTraceFilterTracedLength_Object = MibTableColumn
mscFrNniTraceFilterTracedLength = _MscFrNniTraceFilterTracedLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10, 1, 4),
    _MscFrNniTraceFilterTracedLength_Type()
)
mscFrNniTraceFilterTracedLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniTraceFilterTracedLength.setStatus("mandatory")
_MscFrNniTraceOperationalTable_Object = MibTable
mscFrNniTraceOperationalTable = _MscFrNniTraceOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10)
)
if mibBuilder.loadTexts:
    mscFrNniTraceOperationalTable.setStatus("mandatory")
_MscFrNniTraceOperationalEntry_Object = MibTableRow
mscFrNniTraceOperationalEntry = _MscFrNniTraceOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10, 1)
)
mscFrNniTraceOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniTraceOperationalEntry.setStatus("mandatory")


class _MscFrNniTraceReceiverName_Type(AsciiString):
    """Custom type mscFrNniTraceReceiverName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscFrNniTraceReceiverName_Type.__name__ = "AsciiString"
_MscFrNniTraceReceiverName_Object = MibTableColumn
mscFrNniTraceReceiverName = _MscFrNniTraceReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10, 1, 2),
    _MscFrNniTraceReceiverName_Type()
)
mscFrNniTraceReceiverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniTraceReceiverName.setStatus("mandatory")


class _MscFrNniTraceDuration_Type(Unsigned32):
    """Custom type mscFrNniTraceDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_MscFrNniTraceDuration_Type.__name__ = "Unsigned32"
_MscFrNniTraceDuration_Object = MibTableColumn
mscFrNniTraceDuration = _MscFrNniTraceDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10, 1, 3),
    _MscFrNniTraceDuration_Type()
)
mscFrNniTraceDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniTraceDuration.setStatus("mandatory")


class _MscFrNniTraceQueueLimit_Type(Unsigned32):
    """Custom type mscFrNniTraceQueueLimit based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscFrNniTraceQueueLimit_Type.__name__ = "Unsigned32"
_MscFrNniTraceQueueLimit_Object = MibTableColumn
mscFrNniTraceQueueLimit = _MscFrNniTraceQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10, 1, 4),
    _MscFrNniTraceQueueLimit_Type()
)
mscFrNniTraceQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniTraceQueueLimit.setStatus("mandatory")
_MscFrNniTraceSession_Type = RowPointer
_MscFrNniTraceSession_Object = MibTableColumn
mscFrNniTraceSession = _MscFrNniTraceSession_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10, 1, 5),
    _MscFrNniTraceSession_Type()
)
mscFrNniTraceSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniTraceSession.setStatus("mandatory")
_FrameRelayNniTraceMIB_ObjectIdentity = ObjectIdentity
frameRelayNniTraceMIB = _FrameRelayNniTraceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106)
)
_FrameRelayNniTraceGroup_ObjectIdentity = ObjectIdentity
frameRelayNniTraceGroup = _FrameRelayNniTraceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 1)
)
_FrameRelayNniTraceGroupCA_ObjectIdentity = ObjectIdentity
frameRelayNniTraceGroupCA = _FrameRelayNniTraceGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 1, 1)
)
_FrameRelayNniTraceGroupCA02_ObjectIdentity = ObjectIdentity
frameRelayNniTraceGroupCA02 = _FrameRelayNniTraceGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 1, 1, 3)
)
_FrameRelayNniTraceGroupCA02A_ObjectIdentity = ObjectIdentity
frameRelayNniTraceGroupCA02A = _FrameRelayNniTraceGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 1, 1, 3, 2)
)
_FrameRelayNniTraceCapabilities_ObjectIdentity = ObjectIdentity
frameRelayNniTraceCapabilities = _FrameRelayNniTraceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 3)
)
_FrameRelayNniTraceCapabilitiesCA_ObjectIdentity = ObjectIdentity
frameRelayNniTraceCapabilitiesCA = _FrameRelayNniTraceCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 3, 1)
)
_FrameRelayNniTraceCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frameRelayNniTraceCapabilitiesCA02 = _FrameRelayNniTraceCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 3, 1, 3)
)
_FrameRelayNniTraceCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frameRelayNniTraceCapabilitiesCA02A = _FrameRelayNniTraceCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB",
    **{"mscFrNniTrace": mscFrNniTrace,
       "mscFrNniTraceRowStatusTable": mscFrNniTraceRowStatusTable,
       "mscFrNniTraceRowStatusEntry": mscFrNniTraceRowStatusEntry,
       "mscFrNniTraceRowStatus": mscFrNniTraceRowStatus,
       "mscFrNniTraceComponentName": mscFrNniTraceComponentName,
       "mscFrNniTraceStorageType": mscFrNniTraceStorageType,
       "mscFrNniTraceIndex": mscFrNniTraceIndex,
       "mscFrNniTraceFilter": mscFrNniTraceFilter,
       "mscFrNniTraceFilterRowStatusTable": mscFrNniTraceFilterRowStatusTable,
       "mscFrNniTraceFilterRowStatusEntry": mscFrNniTraceFilterRowStatusEntry,
       "mscFrNniTraceFilterRowStatus": mscFrNniTraceFilterRowStatus,
       "mscFrNniTraceFilterComponentName": mscFrNniTraceFilterComponentName,
       "mscFrNniTraceFilterStorageType": mscFrNniTraceFilterStorageType,
       "mscFrNniTraceFilterIndex": mscFrNniTraceFilterIndex,
       "mscFrNniTraceFilterOperationalTable": mscFrNniTraceFilterOperationalTable,
       "mscFrNniTraceFilterOperationalEntry": mscFrNniTraceFilterOperationalEntry,
       "mscFrNniTraceFilterTraceType": mscFrNniTraceFilterTraceType,
       "mscFrNniTraceFilterTracedDlci": mscFrNniTraceFilterTracedDlci,
       "mscFrNniTraceFilterDirection": mscFrNniTraceFilterDirection,
       "mscFrNniTraceFilterTracedLength": mscFrNniTraceFilterTracedLength,
       "mscFrNniTraceOperationalTable": mscFrNniTraceOperationalTable,
       "mscFrNniTraceOperationalEntry": mscFrNniTraceOperationalEntry,
       "mscFrNniTraceReceiverName": mscFrNniTraceReceiverName,
       "mscFrNniTraceDuration": mscFrNniTraceDuration,
       "mscFrNniTraceQueueLimit": mscFrNniTraceQueueLimit,
       "mscFrNniTraceSession": mscFrNniTraceSession,
       "frameRelayNniTraceMIB": frameRelayNniTraceMIB,
       "frameRelayNniTraceGroup": frameRelayNniTraceGroup,
       "frameRelayNniTraceGroupCA": frameRelayNniTraceGroupCA,
       "frameRelayNniTraceGroupCA02": frameRelayNniTraceGroupCA02,
       "frameRelayNniTraceGroupCA02A": frameRelayNniTraceGroupCA02A,
       "frameRelayNniTraceCapabilities": frameRelayNniTraceCapabilities,
       "frameRelayNniTraceCapabilitiesCA": frameRelayNniTraceCapabilitiesCA,
       "frameRelayNniTraceCapabilitiesCA02": frameRelayNniTraceCapabilitiesCA02,
       "frameRelayNniTraceCapabilitiesCA02A": frameRelayNniTraceCapabilitiesCA02A}
)
