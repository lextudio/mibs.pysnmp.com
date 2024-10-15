# SNMP MIB module (ASYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASYNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:54 2024
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

(scanet,) = mibBuilder.importSymbols(
    "SCANET-MIB",
    "scanet")

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

__pysmi_async_ObjectIdentity = ObjectIdentity
_pysmi_async = __pysmi_async_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 45)
)
_AsyncConfig_ObjectIdentity = ObjectIdentity
asyncConfig = _AsyncConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 45, 1)
)
_AsyncConfigTable_Object = MibTable
asyncConfigTable = _AsyncConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 1, 1)
)
if mibBuilder.loadTexts:
    asyncConfigTable.setStatus("mandatory")
_AsyncConfigEntry_Object = MibTableRow
asyncConfigEntry = _AsyncConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 1, 1, 1)
)
asyncConfigEntry.setIndexNames(
    (0, "ASYNC-MIB", "asyncConfigIndex"),
)
if mibBuilder.loadTexts:
    asyncConfigEntry.setStatus("mandatory")
_AsyncConfigIndex_Type = Integer32
_AsyncConfigIndex_Object = MibTableColumn
asyncConfigIndex = _AsyncConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 1, 1, 1, 1),
    _AsyncConfigIndex_Type()
)
asyncConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncConfigIndex.setStatus("mandatory")


class _AsyncConfigDialMode_Type(Integer32):
    """Custom type asyncConfigDialMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pulse", 2),
          ("tone", 1))
    )


_AsyncConfigDialMode_Type.__name__ = "Integer32"
_AsyncConfigDialMode_Object = MibTableColumn
asyncConfigDialMode = _AsyncConfigDialMode_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 1, 1, 1, 2),
    _AsyncConfigDialMode_Type()
)
asyncConfigDialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncConfigDialMode.setStatus("mandatory")


class _AsyncConfigAutoInit_Type(Integer32):
    """Custom type asyncConfigAutoInit based on Integer32"""
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


_AsyncConfigAutoInit_Type.__name__ = "Integer32"
_AsyncConfigAutoInit_Object = MibTableColumn
asyncConfigAutoInit = _AsyncConfigAutoInit_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 1, 1, 1, 3),
    _AsyncConfigAutoInit_Type()
)
asyncConfigAutoInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncConfigAutoInit.setStatus("mandatory")


class _AsyncConfigDialString_Type(OctetString):
    """Custom type asyncConfigDialString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_AsyncConfigDialString_Type.__name__ = "OctetString"
_AsyncConfigDialString_Object = MibTableColumn
asyncConfigDialString = _AsyncConfigDialString_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 1, 1, 1, 4),
    _AsyncConfigDialString_Type()
)
asyncConfigDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncConfigDialString.setStatus("mandatory")


class _AsyncConfigInitString1_Type(OctetString):
    """Custom type asyncConfigInitString1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_AsyncConfigInitString1_Type.__name__ = "OctetString"
_AsyncConfigInitString1_Object = MibTableColumn
asyncConfigInitString1 = _AsyncConfigInitString1_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 1, 1, 1, 5),
    _AsyncConfigInitString1_Type()
)
asyncConfigInitString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncConfigInitString1.setStatus("mandatory")


class _AsyncConfigInitString2_Type(OctetString):
    """Custom type asyncConfigInitString2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_AsyncConfigInitString2_Type.__name__ = "OctetString"
_AsyncConfigInitString2_Object = MibTableColumn
asyncConfigInitString2 = _AsyncConfigInitString2_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 1, 1, 1, 6),
    _AsyncConfigInitString2_Type()
)
asyncConfigInitString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asyncConfigInitString2.setStatus("mandatory")
_AsyncMon_ObjectIdentity = ObjectIdentity
asyncMon = _AsyncMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 45, 2)
)
_AsyncMonTable_Object = MibTable
asyncMonTable = _AsyncMonTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1)
)
if mibBuilder.loadTexts:
    asyncMonTable.setStatus("mandatory")
_AsyncMonEntry_Object = MibTableRow
asyncMonEntry = _AsyncMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1)
)
asyncMonEntry.setIndexNames(
    (0, "ASYNC-MIB", "asyncMonIndex"),
)
if mibBuilder.loadTexts:
    asyncMonEntry.setStatus("mandatory")
_AsyncMonIndex_Type = Integer32
_AsyncMonIndex_Object = MibTableColumn
asyncMonIndex = _AsyncMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 1),
    _AsyncMonIndex_Type()
)
asyncMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonIndex.setStatus("mandatory")


class _AsyncMonMode_Type(Integer32):
    """Custom type asyncMonMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("acceptingCall", 9),
          ("connected", 10),
          ("dialing", 12),
          ("hangingUp", 6),
          ("initializingModem", 3),
          ("noConfiguration", 1),
          ("noValidModem", 2),
          ("other", 14),
          ("reserved", 11),
          ("resettingModem", 4),
          ("standBy", 8),
          ("waitingForAnswer", 13),
          ("waitingForHangupAck", 7),
          ("waitingForResetAck", 5))
    )


_AsyncMonMode_Type.__name__ = "Integer32"
_AsyncMonMode_Object = MibTableColumn
asyncMonMode = _AsyncMonMode_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 2),
    _AsyncMonMode_Type()
)
asyncMonMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonMode.setStatus("mandatory")
_AsyncMonTransmitFailedErrors_Type = Counter32
_AsyncMonTransmitFailedErrors_Object = MibTableColumn
asyncMonTransmitFailedErrors = _AsyncMonTransmitFailedErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 3),
    _AsyncMonTransmitFailedErrors_Type()
)
asyncMonTransmitFailedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonTransmitFailedErrors.setStatus("mandatory")
_AsyncMonTransmitCongestions_Type = Counter32
_AsyncMonTransmitCongestions_Object = MibTableColumn
asyncMonTransmitCongestions = _AsyncMonTransmitCongestions_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 4),
    _AsyncMonTransmitCongestions_Type()
)
asyncMonTransmitCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonTransmitCongestions.setStatus("mandatory")
_AsyncMonReceiveLostEndMarkers_Type = Counter32
_AsyncMonReceiveLostEndMarkers_Object = MibTableColumn
asyncMonReceiveLostEndMarkers = _AsyncMonReceiveLostEndMarkers_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 5),
    _AsyncMonReceiveLostEndMarkers_Type()
)
asyncMonReceiveLostEndMarkers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonReceiveLostEndMarkers.setStatus("mandatory")
_AsyncMonReceiveOverflows_Type = Counter32
_AsyncMonReceiveOverflows_Object = MibTableColumn
asyncMonReceiveOverflows = _AsyncMonReceiveOverflows_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 6),
    _AsyncMonReceiveOverflows_Type()
)
asyncMonReceiveOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonReceiveOverflows.setStatus("mandatory")
_AsyncMonReceiveStuffingErrors_Type = Counter32
_AsyncMonReceiveStuffingErrors_Object = MibTableColumn
asyncMonReceiveStuffingErrors = _AsyncMonReceiveStuffingErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 7),
    _AsyncMonReceiveStuffingErrors_Type()
)
asyncMonReceiveStuffingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonReceiveStuffingErrors.setStatus("mandatory")
_AsyncMonReceiveCRCErrors_Type = Counter32
_AsyncMonReceiveCRCErrors_Object = MibTableColumn
asyncMonReceiveCRCErrors = _AsyncMonReceiveCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 8),
    _AsyncMonReceiveCRCErrors_Type()
)
asyncMonReceiveCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonReceiveCRCErrors.setStatus("mandatory")
_AsyncMonReceiveShortPackets_Type = Counter32
_AsyncMonReceiveShortPackets_Object = MibTableColumn
asyncMonReceiveShortPackets = _AsyncMonReceiveShortPackets_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 9),
    _AsyncMonReceiveShortPackets_Type()
)
asyncMonReceiveShortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonReceiveShortPackets.setStatus("mandatory")
_AsyncMonReceiveLongPackets_Type = Counter32
_AsyncMonReceiveLongPackets_Object = MibTableColumn
asyncMonReceiveLongPackets = _AsyncMonReceiveLongPackets_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 10),
    _AsyncMonReceiveLongPackets_Type()
)
asyncMonReceiveLongPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonReceiveLongPackets.setStatus("mandatory")
_AsyncMonReceiveUartOverrunErrors_Type = Counter32
_AsyncMonReceiveUartOverrunErrors_Object = MibTableColumn
asyncMonReceiveUartOverrunErrors = _AsyncMonReceiveUartOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 11),
    _AsyncMonReceiveUartOverrunErrors_Type()
)
asyncMonReceiveUartOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonReceiveUartOverrunErrors.setStatus("mandatory")
_AsyncMonReceiveUartParityErrors_Type = Counter32
_AsyncMonReceiveUartParityErrors_Object = MibTableColumn
asyncMonReceiveUartParityErrors = _AsyncMonReceiveUartParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 12),
    _AsyncMonReceiveUartParityErrors_Type()
)
asyncMonReceiveUartParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonReceiveUartParityErrors.setStatus("mandatory")
_AsyncMonReceiveUartFramingErrors_Type = Counter32
_AsyncMonReceiveUartFramingErrors_Object = MibTableColumn
asyncMonReceiveUartFramingErrors = _AsyncMonReceiveUartFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 13),
    _AsyncMonReceiveUartFramingErrors_Type()
)
asyncMonReceiveUartFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonReceiveUartFramingErrors.setStatus("mandatory")
_AsyncMonReceiveUartBreakErrors_Type = Counter32
_AsyncMonReceiveUartBreakErrors_Object = MibTableColumn
asyncMonReceiveUartBreakErrors = _AsyncMonReceiveUartBreakErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 14),
    _AsyncMonReceiveUartBreakErrors_Type()
)
asyncMonReceiveUartBreakErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonReceiveUartBreakErrors.setStatus("mandatory")


class _AsyncMonCallDirection_Type(Integer32):
    """Custom type asyncMonCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("none", 3),
          ("outgoing", 2))
    )


_AsyncMonCallDirection_Type.__name__ = "Integer32"
_AsyncMonCallDirection_Object = MibTableColumn
asyncMonCallDirection = _AsyncMonCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 2, 1, 1, 15),
    _AsyncMonCallDirection_Type()
)
asyncMonCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncMonCallDirection.setStatus("mandatory")
_AsyncPcmcia_ObjectIdentity = ObjectIdentity
asyncPcmcia = _AsyncPcmcia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 45, 3)
)
_AsyncPcmciaTable_Object = MibTable
asyncPcmciaTable = _AsyncPcmciaTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 3, 1)
)
if mibBuilder.loadTexts:
    asyncPcmciaTable.setStatus("mandatory")
_AsyncPcmciaEntry_Object = MibTableRow
asyncPcmciaEntry = _AsyncPcmciaEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 3, 1, 1)
)
asyncPcmciaEntry.setIndexNames(
    (0, "ASYNC-MIB", "asyncPcmciaIndex"),
)
if mibBuilder.loadTexts:
    asyncPcmciaEntry.setStatus("mandatory")
_AsyncPcmciaIndex_Type = Integer32
_AsyncPcmciaIndex_Object = MibTableColumn
asyncPcmciaIndex = _AsyncPcmciaIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 3, 1, 1, 1),
    _AsyncPcmciaIndex_Type()
)
asyncPcmciaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPcmciaIndex.setStatus("mandatory")


class _AsyncPcmciaManufacturerName_Type(OctetString):
    """Custom type asyncPcmciaManufacturerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_AsyncPcmciaManufacturerName_Type.__name__ = "OctetString"
_AsyncPcmciaManufacturerName_Object = MibTableColumn
asyncPcmciaManufacturerName = _AsyncPcmciaManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 3, 1, 1, 2),
    _AsyncPcmciaManufacturerName_Type()
)
asyncPcmciaManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPcmciaManufacturerName.setStatus("mandatory")


class _AsyncPcmciaProductName_Type(OctetString):
    """Custom type asyncPcmciaProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_AsyncPcmciaProductName_Type.__name__ = "OctetString"
_AsyncPcmciaProductName_Object = MibTableColumn
asyncPcmciaProductName = _AsyncPcmciaProductName_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 3, 1, 1, 3),
    _AsyncPcmciaProductName_Type()
)
asyncPcmciaProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPcmciaProductName.setStatus("mandatory")
_AsyncPcmciaProductVersionMajor_Type = Integer32
_AsyncPcmciaProductVersionMajor_Object = MibTableColumn
asyncPcmciaProductVersionMajor = _AsyncPcmciaProductVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 3, 1, 1, 4),
    _AsyncPcmciaProductVersionMajor_Type()
)
asyncPcmciaProductVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPcmciaProductVersionMajor.setStatus("mandatory")
_AsyncPcmciaProductVersionMinor_Type = Integer32
_AsyncPcmciaProductVersionMinor_Object = MibTableColumn
asyncPcmciaProductVersionMinor = _AsyncPcmciaProductVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 3, 1, 1, 5),
    _AsyncPcmciaProductVersionMinor_Type()
)
asyncPcmciaProductVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPcmciaProductVersionMinor.setStatus("mandatory")


class _AsyncPcmciaPcmciaSupported_Type(Integer32):
    """Custom type asyncPcmciaPcmciaSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AsyncPcmciaPcmciaSupported_Type.__name__ = "Integer32"
_AsyncPcmciaPcmciaSupported_Object = MibTableColumn
asyncPcmciaPcmciaSupported = _AsyncPcmciaPcmciaSupported_Object(
    (1, 3, 6, 1, 4, 1, 208, 45, 3, 1, 1, 6),
    _AsyncPcmciaPcmciaSupported_Type()
)
asyncPcmciaPcmciaSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asyncPcmciaPcmciaSupported.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASYNC-MIB",
    **{"async": _pysmi_async,
       "asyncConfig": asyncConfig,
       "asyncConfigTable": asyncConfigTable,
       "asyncConfigEntry": asyncConfigEntry,
       "asyncConfigIndex": asyncConfigIndex,
       "asyncConfigDialMode": asyncConfigDialMode,
       "asyncConfigAutoInit": asyncConfigAutoInit,
       "asyncConfigDialString": asyncConfigDialString,
       "asyncConfigInitString1": asyncConfigInitString1,
       "asyncConfigInitString2": asyncConfigInitString2,
       "asyncMon": asyncMon,
       "asyncMonTable": asyncMonTable,
       "asyncMonEntry": asyncMonEntry,
       "asyncMonIndex": asyncMonIndex,
       "asyncMonMode": asyncMonMode,
       "asyncMonTransmitFailedErrors": asyncMonTransmitFailedErrors,
       "asyncMonTransmitCongestions": asyncMonTransmitCongestions,
       "asyncMonReceiveLostEndMarkers": asyncMonReceiveLostEndMarkers,
       "asyncMonReceiveOverflows": asyncMonReceiveOverflows,
       "asyncMonReceiveStuffingErrors": asyncMonReceiveStuffingErrors,
       "asyncMonReceiveCRCErrors": asyncMonReceiveCRCErrors,
       "asyncMonReceiveShortPackets": asyncMonReceiveShortPackets,
       "asyncMonReceiveLongPackets": asyncMonReceiveLongPackets,
       "asyncMonReceiveUartOverrunErrors": asyncMonReceiveUartOverrunErrors,
       "asyncMonReceiveUartParityErrors": asyncMonReceiveUartParityErrors,
       "asyncMonReceiveUartFramingErrors": asyncMonReceiveUartFramingErrors,
       "asyncMonReceiveUartBreakErrors": asyncMonReceiveUartBreakErrors,
       "asyncMonCallDirection": asyncMonCallDirection,
       "asyncPcmcia": asyncPcmcia,
       "asyncPcmciaTable": asyncPcmciaTable,
       "asyncPcmciaEntry": asyncPcmciaEntry,
       "asyncPcmciaIndex": asyncPcmciaIndex,
       "asyncPcmciaManufacturerName": asyncPcmciaManufacturerName,
       "asyncPcmciaProductName": asyncPcmciaProductName,
       "asyncPcmciaProductVersionMajor": asyncPcmciaProductVersionMajor,
       "asyncPcmciaProductVersionMinor": asyncPcmciaProductVersionMinor,
       "asyncPcmciaPcmciaSupported": asyncPcmciaPcmciaSupported}
)
