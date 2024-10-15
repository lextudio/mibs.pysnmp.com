# SNMP MIB module (FLOWMGREXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FLOWMGREXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:09 2024
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

(flowMgrExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "flowMgrExt")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

flowMgrExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApFlowMgrExtFlowTraceOptions_Type(DisplayString):
    """Custom type apFlowMgrExtFlowTraceOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_ApFlowMgrExtFlowTraceOptions_Type.__name__ = "DisplayString"
_ApFlowMgrExtFlowTraceOptions_Object = MibScalar
apFlowMgrExtFlowTraceOptions = _ApFlowMgrExtFlowTraceOptions_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 2),
    _ApFlowMgrExtFlowTraceOptions_Type()
)
apFlowMgrExtFlowTraceOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtFlowTraceOptions.setStatus("current")


class _ApFlowMgrExtFlowTraceState_Type(Integer32):
    """Custom type apFlowMgrExtFlowTraceState based on Integer32"""
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


_ApFlowMgrExtFlowTraceState_Type.__name__ = "Integer32"
_ApFlowMgrExtFlowTraceState_Object = MibScalar
apFlowMgrExtFlowTraceState = _ApFlowMgrExtFlowTraceState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 3),
    _ApFlowMgrExtFlowTraceState_Type()
)
apFlowMgrExtFlowTraceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtFlowTraceState.setStatus("current")


class _ApFlowMgrExtFlowTraceFilename_Type(DisplayString):
    """Custom type apFlowMgrExtFlowTraceFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApFlowMgrExtFlowTraceFilename_Type.__name__ = "DisplayString"
_ApFlowMgrExtFlowTraceFilename_Object = MibScalar
apFlowMgrExtFlowTraceFilename = _ApFlowMgrExtFlowTraceFilename_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 4),
    _ApFlowMgrExtFlowTraceFilename_Type()
)
apFlowMgrExtFlowTraceFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtFlowTraceFilename.setStatus("current")


class _ApFlowMgrExtFlowTraceMaxFileSize_Type(Integer32):
    """Custom type apFlowMgrExtFlowTraceMaxFileSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApFlowMgrExtFlowTraceMaxFileSize_Type.__name__ = "Integer32"
_ApFlowMgrExtFlowTraceMaxFileSize_Object = MibScalar
apFlowMgrExtFlowTraceMaxFileSize = _ApFlowMgrExtFlowTraceMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 5),
    _ApFlowMgrExtFlowTraceMaxFileSize_Type()
)
apFlowMgrExtFlowTraceMaxFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtFlowTraceMaxFileSize.setStatus("current")


class _ApFlowMgrExtFlowTraceDuration_Type(Integer32):
    """Custom type apFlowMgrExtFlowTraceDuration based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ApFlowMgrExtFlowTraceDuration_Type.__name__ = "Integer32"
_ApFlowMgrExtFlowTraceDuration_Object = MibScalar
apFlowMgrExtFlowTraceDuration = _ApFlowMgrExtFlowTraceDuration_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 6),
    _ApFlowMgrExtFlowTraceDuration_Type()
)
apFlowMgrExtFlowTraceDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtFlowTraceDuration.setStatus("current")


class _ApFlowMgrExtPermanentPort1_Type(Integer32):
    """Custom type apFlowMgrExtPermanentPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApFlowMgrExtPermanentPort1_Type.__name__ = "Integer32"
_ApFlowMgrExtPermanentPort1_Object = MibScalar
apFlowMgrExtPermanentPort1 = _ApFlowMgrExtPermanentPort1_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 7),
    _ApFlowMgrExtPermanentPort1_Type()
)
apFlowMgrExtPermanentPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtPermanentPort1.setStatus("current")


class _ApFlowMgrExtPermanentPort2_Type(Integer32):
    """Custom type apFlowMgrExtPermanentPort2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApFlowMgrExtPermanentPort2_Type.__name__ = "Integer32"
_ApFlowMgrExtPermanentPort2_Object = MibScalar
apFlowMgrExtPermanentPort2 = _ApFlowMgrExtPermanentPort2_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 8),
    _ApFlowMgrExtPermanentPort2_Type()
)
apFlowMgrExtPermanentPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtPermanentPort2.setStatus("current")


class _ApFlowMgrExtPermanentPort3_Type(Integer32):
    """Custom type apFlowMgrExtPermanentPort3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApFlowMgrExtPermanentPort3_Type.__name__ = "Integer32"
_ApFlowMgrExtPermanentPort3_Object = MibScalar
apFlowMgrExtPermanentPort3 = _ApFlowMgrExtPermanentPort3_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 9),
    _ApFlowMgrExtPermanentPort3_Type()
)
apFlowMgrExtPermanentPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtPermanentPort3.setStatus("current")


class _ApFlowMgrExtPermanentPort4_Type(Integer32):
    """Custom type apFlowMgrExtPermanentPort4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApFlowMgrExtPermanentPort4_Type.__name__ = "Integer32"
_ApFlowMgrExtPermanentPort4_Object = MibScalar
apFlowMgrExtPermanentPort4 = _ApFlowMgrExtPermanentPort4_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 10),
    _ApFlowMgrExtPermanentPort4_Type()
)
apFlowMgrExtPermanentPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtPermanentPort4.setStatus("current")


class _ApFlowMgrExtReserveCleanTimer_Type(Integer32):
    """Custom type apFlowMgrExtReserveCleanTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApFlowMgrExtReserveCleanTimer_Type.__name__ = "Integer32"
_ApFlowMgrExtReserveCleanTimer_Object = MibScalar
apFlowMgrExtReserveCleanTimer = _ApFlowMgrExtReserveCleanTimer_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 11),
    _ApFlowMgrExtReserveCleanTimer_Type()
)
apFlowMgrExtReserveCleanTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtReserveCleanTimer.setStatus("current")
_ApFlowMgrExtPortIdleTable_Object = MibTable
apFlowMgrExtPortIdleTable = _ApFlowMgrExtPortIdleTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 12)
)
if mibBuilder.loadTexts:
    apFlowMgrExtPortIdleTable.setStatus("current")
_ApFlowMgrExtPortIdleEntry_Object = MibTableRow
apFlowMgrExtPortIdleEntry = _ApFlowMgrExtPortIdleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 12, 1)
)
apFlowMgrExtPortIdleEntry.setIndexNames(
    (0, "FLOWMGREXT-MIB", "apFlowMgrExtPortIdle"),
)
if mibBuilder.loadTexts:
    apFlowMgrExtPortIdleEntry.setStatus("current")
_ApFlowMgrExtPortIdle_Type = Integer32
_ApFlowMgrExtPortIdle_Object = MibTableColumn
apFlowMgrExtPortIdle = _ApFlowMgrExtPortIdle_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 12, 1, 2),
    _ApFlowMgrExtPortIdle_Type()
)
apFlowMgrExtPortIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtPortIdle.setStatus("current")


class _ApFlowMgrExtPortIdleValue_Type(Integer32):
    """Custom type apFlowMgrExtPortIdleValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApFlowMgrExtPortIdleValue_Type.__name__ = "Integer32"
_ApFlowMgrExtPortIdleValue_Object = MibTableColumn
apFlowMgrExtPortIdleValue = _ApFlowMgrExtPortIdleValue_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 12, 1, 3),
    _ApFlowMgrExtPortIdleValue_Type()
)
apFlowMgrExtPortIdleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtPortIdleValue.setStatus("current")


class _ApFlowMgrExtPortLowWaterFCB_Type(Integer32):
    """Custom type apFlowMgrExtPortLowWaterFCB based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApFlowMgrExtPortLowWaterFCB_Type.__name__ = "Integer32"
_ApFlowMgrExtPortLowWaterFCB_Object = MibTableColumn
apFlowMgrExtPortLowWaterFCB = _ApFlowMgrExtPortLowWaterFCB_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 12, 1, 4),
    _ApFlowMgrExtPortLowWaterFCB_Type()
)
apFlowMgrExtPortLowWaterFCB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtPortLowWaterFCB.setStatus("current")


class _ApFlowMgrExtIdleTimer_Type(Integer32):
    """Custom type apFlowMgrExtIdleTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_ApFlowMgrExtIdleTimer_Type.__name__ = "Integer32"
_ApFlowMgrExtIdleTimer_Object = MibScalar
apFlowMgrExtIdleTimer = _ApFlowMgrExtIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 13),
    _ApFlowMgrExtIdleTimer_Type()
)
apFlowMgrExtIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFlowMgrExtIdleTimer.setStatus("current")
_ApFlowMgrStatIfTable_Object = MibTable
apFlowMgrStatIfTable = _ApFlowMgrStatIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14)
)
if mibBuilder.loadTexts:
    apFlowMgrStatIfTable.setStatus("current")
_ApFlowMgrStatIfEntry_Object = MibTableRow
apFlowMgrStatIfEntry = _ApFlowMgrStatIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1)
)
apFlowMgrStatIfEntry.setIndexNames(
    (0, "FLOWMGREXT-MIB", "apFlowMgrStatIfIndex"),
    (0, "FLOWMGREXT-MIB", "apFlowMgrStatIfVlanID"),
)
if mibBuilder.loadTexts:
    apFlowMgrStatIfEntry.setStatus("current")
_ApFlowMgrStatIfIndex_Type = Integer32
_ApFlowMgrStatIfIndex_Object = MibTableColumn
apFlowMgrStatIfIndex = _ApFlowMgrStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 1),
    _ApFlowMgrStatIfIndex_Type()
)
apFlowMgrStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfIndex.setStatus("current")
_ApFlowMgrStatIfVlanID_Type = Integer32
_ApFlowMgrStatIfVlanID_Object = MibTableColumn
apFlowMgrStatIfVlanID = _ApFlowMgrStatIfVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 2),
    _ApFlowMgrStatIfVlanID_Type()
)
apFlowMgrStatIfVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfVlanID.setStatus("current")
_ApFlowMgrStatIfUDPTotal_Type = Integer32
_ApFlowMgrStatIfUDPTotal_Object = MibTableColumn
apFlowMgrStatIfUDPTotal = _ApFlowMgrStatIfUDPTotal_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 3),
    _ApFlowMgrStatIfUDPTotal_Type()
)
apFlowMgrStatIfUDPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfUDPTotal.setStatus("current")
_ApFlowMgrStatIfUDPCur_Type = Integer32
_ApFlowMgrStatIfUDPCur_Object = MibTableColumn
apFlowMgrStatIfUDPCur = _ApFlowMgrStatIfUDPCur_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 4),
    _ApFlowMgrStatIfUDPCur_Type()
)
apFlowMgrStatIfUDPCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfUDPCur.setStatus("current")
_ApFlowMgrStatIfUDPHigh_Type = Integer32
_ApFlowMgrStatIfUDPHigh_Object = MibTableColumn
apFlowMgrStatIfUDPHigh = _ApFlowMgrStatIfUDPHigh_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 5),
    _ApFlowMgrStatIfUDPHigh_Type()
)
apFlowMgrStatIfUDPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfUDPHigh.setStatus("current")
_ApFlowMgrStatIfUDPAvg_Type = Integer32
_ApFlowMgrStatIfUDPAvg_Object = MibTableColumn
apFlowMgrStatIfUDPAvg = _ApFlowMgrStatIfUDPAvg_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 6),
    _ApFlowMgrStatIfUDPAvg_Type()
)
apFlowMgrStatIfUDPAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfUDPAvg.setStatus("current")
_ApFlowMgrStatIfTCPTotal_Type = Integer32
_ApFlowMgrStatIfTCPTotal_Object = MibTableColumn
apFlowMgrStatIfTCPTotal = _ApFlowMgrStatIfTCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 7),
    _ApFlowMgrStatIfTCPTotal_Type()
)
apFlowMgrStatIfTCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfTCPTotal.setStatus("current")
_ApFlowMgrStatIfTCPCur_Type = Integer32
_ApFlowMgrStatIfTCPCur_Object = MibTableColumn
apFlowMgrStatIfTCPCur = _ApFlowMgrStatIfTCPCur_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 8),
    _ApFlowMgrStatIfTCPCur_Type()
)
apFlowMgrStatIfTCPCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfTCPCur.setStatus("current")
_ApFlowMgrStatIfTCPHigh_Type = Integer32
_ApFlowMgrStatIfTCPHigh_Object = MibTableColumn
apFlowMgrStatIfTCPHigh = _ApFlowMgrStatIfTCPHigh_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 9),
    _ApFlowMgrStatIfTCPHigh_Type()
)
apFlowMgrStatIfTCPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfTCPHigh.setStatus("current")
_ApFlowMgrStatIfTCPAvg_Type = Integer32
_ApFlowMgrStatIfTCPAvg_Object = MibTableColumn
apFlowMgrStatIfTCPAvg = _ApFlowMgrStatIfTCPAvg_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 10),
    _ApFlowMgrStatIfTCPAvg_Type()
)
apFlowMgrStatIfTCPAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfTCPAvg.setStatus("current")
_ApFlowMgrStatIfCurrentActiveTCP_Type = Integer32
_ApFlowMgrStatIfCurrentActiveTCP_Object = MibTableColumn
apFlowMgrStatIfCurrentActiveTCP = _ApFlowMgrStatIfCurrentActiveTCP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 11),
    _ApFlowMgrStatIfCurrentActiveTCP_Type()
)
apFlowMgrStatIfCurrentActiveTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfCurrentActiveTCP.setStatus("current")
_ApFlowMgrStatIfCurrentActiveUDP_Type = Integer32
_ApFlowMgrStatIfCurrentActiveUDP_Object = MibTableColumn
apFlowMgrStatIfCurrentActiveUDP = _ApFlowMgrStatIfCurrentActiveUDP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 12),
    _ApFlowMgrStatIfCurrentActiveUDP_Type()
)
apFlowMgrStatIfCurrentActiveUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfCurrentActiveUDP.setStatus("current")
_ApFlowMgrStatIfAccountingReportsRx_Type = Integer32
_ApFlowMgrStatIfAccountingReportsRx_Object = MibTableColumn
apFlowMgrStatIfAccountingReportsRx = _ApFlowMgrStatIfAccountingReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 13),
    _ApFlowMgrStatIfAccountingReportsRx_Type()
)
apFlowMgrStatIfAccountingReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfAccountingReportsRx.setStatus("current")
_ApFlowMgrStatIfResets_Type = Integer32
_ApFlowMgrStatIfResets_Object = MibTableColumn
apFlowMgrStatIfResets = _ApFlowMgrStatIfResets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 14),
    _ApFlowMgrStatIfResets_Type()
)
apFlowMgrStatIfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfResets.setStatus("current")
_ApFlowMgrStatIfFcbCount_Type = Integer32
_ApFlowMgrStatIfFcbCount_Object = MibTableColumn
apFlowMgrStatIfFcbCount = _ApFlowMgrStatIfFcbCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 14, 1, 15),
    _ApFlowMgrStatIfFcbCount_Type()
)
apFlowMgrStatIfFcbCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatIfFcbCount.setStatus("current")
_ApFlowMgrStatSSTable_Object = MibTable
apFlowMgrStatSSTable = _ApFlowMgrStatSSTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15)
)
if mibBuilder.loadTexts:
    apFlowMgrStatSSTable.setStatus("current")
_ApFlowMgrStatSSEntry_Object = MibTableRow
apFlowMgrStatSSEntry = _ApFlowMgrStatSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1)
)
apFlowMgrStatSSEntry.setIndexNames(
    (0, "FLOWMGREXT-MIB", "apFlowMgrStatSSSlot"),
    (0, "FLOWMGREXT-MIB", "apFlowMgrStatSSSubSlot"),
)
if mibBuilder.loadTexts:
    apFlowMgrStatSSEntry.setStatus("current")
_ApFlowMgrStatSSSlot_Type = Integer32
_ApFlowMgrStatSSSlot_Object = MibTableColumn
apFlowMgrStatSSSlot = _ApFlowMgrStatSSSlot_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 1),
    _ApFlowMgrStatSSSlot_Type()
)
apFlowMgrStatSSSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSSlot.setStatus("current")
_ApFlowMgrStatSSSubSlot_Type = Integer32
_ApFlowMgrStatSSSubSlot_Object = MibTableColumn
apFlowMgrStatSSSubSlot = _ApFlowMgrStatSSSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 2),
    _ApFlowMgrStatSSSubSlot_Type()
)
apFlowMgrStatSSSubSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSSubSlot.setStatus("current")
_ApFlowMgrStatSSUDPTotal_Type = Integer32
_ApFlowMgrStatSSUDPTotal_Object = MibTableColumn
apFlowMgrStatSSUDPTotal = _ApFlowMgrStatSSUDPTotal_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 3),
    _ApFlowMgrStatSSUDPTotal_Type()
)
apFlowMgrStatSSUDPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSUDPTotal.setStatus("current")
_ApFlowMgrStatSSUDPCur_Type = Integer32
_ApFlowMgrStatSSUDPCur_Object = MibTableColumn
apFlowMgrStatSSUDPCur = _ApFlowMgrStatSSUDPCur_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 4),
    _ApFlowMgrStatSSUDPCur_Type()
)
apFlowMgrStatSSUDPCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSUDPCur.setStatus("current")
_ApFlowMgrStatSSUDPHigh_Type = Integer32
_ApFlowMgrStatSSUDPHigh_Object = MibTableColumn
apFlowMgrStatSSUDPHigh = _ApFlowMgrStatSSUDPHigh_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 5),
    _ApFlowMgrStatSSUDPHigh_Type()
)
apFlowMgrStatSSUDPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSUDPHigh.setStatus("current")
_ApFlowMgrStatSSUDPAvg_Type = Integer32
_ApFlowMgrStatSSUDPAvg_Object = MibTableColumn
apFlowMgrStatSSUDPAvg = _ApFlowMgrStatSSUDPAvg_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 6),
    _ApFlowMgrStatSSUDPAvg_Type()
)
apFlowMgrStatSSUDPAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSUDPAvg.setStatus("current")
_ApFlowMgrStatSSTCPTotal_Type = Integer32
_ApFlowMgrStatSSTCPTotal_Object = MibTableColumn
apFlowMgrStatSSTCPTotal = _ApFlowMgrStatSSTCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 7),
    _ApFlowMgrStatSSTCPTotal_Type()
)
apFlowMgrStatSSTCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSTCPTotal.setStatus("current")
_ApFlowMgrStatSSTCPCur_Type = Integer32
_ApFlowMgrStatSSTCPCur_Object = MibTableColumn
apFlowMgrStatSSTCPCur = _ApFlowMgrStatSSTCPCur_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 8),
    _ApFlowMgrStatSSTCPCur_Type()
)
apFlowMgrStatSSTCPCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSTCPCur.setStatus("current")
_ApFlowMgrStatSSTCPHigh_Type = Integer32
_ApFlowMgrStatSSTCPHigh_Object = MibTableColumn
apFlowMgrStatSSTCPHigh = _ApFlowMgrStatSSTCPHigh_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 9),
    _ApFlowMgrStatSSTCPHigh_Type()
)
apFlowMgrStatSSTCPHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSTCPHigh.setStatus("current")
_ApFlowMgrStatSSTCPAvg_Type = Integer32
_ApFlowMgrStatSSTCPAvg_Object = MibTableColumn
apFlowMgrStatSSTCPAvg = _ApFlowMgrStatSSTCPAvg_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 10),
    _ApFlowMgrStatSSTCPAvg_Type()
)
apFlowMgrStatSSTCPAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSTCPAvg.setStatus("current")
_ApFlowMgrStatSSCurrentActiveTCP_Type = Integer32
_ApFlowMgrStatSSCurrentActiveTCP_Object = MibTableColumn
apFlowMgrStatSSCurrentActiveTCP = _ApFlowMgrStatSSCurrentActiveTCP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 11),
    _ApFlowMgrStatSSCurrentActiveTCP_Type()
)
apFlowMgrStatSSCurrentActiveTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSCurrentActiveTCP.setStatus("current")
_ApFlowMgrStatSSCurrentActiveUDP_Type = Integer32
_ApFlowMgrStatSSCurrentActiveUDP_Object = MibTableColumn
apFlowMgrStatSSCurrentActiveUDP = _ApFlowMgrStatSSCurrentActiveUDP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 12),
    _ApFlowMgrStatSSCurrentActiveUDP_Type()
)
apFlowMgrStatSSCurrentActiveUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSCurrentActiveUDP.setStatus("current")
_ApFlowMgrStatSSAccountingReportsRx_Type = Integer32
_ApFlowMgrStatSSAccountingReportsRx_Object = MibTableColumn
apFlowMgrStatSSAccountingReportsRx = _ApFlowMgrStatSSAccountingReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 13),
    _ApFlowMgrStatSSAccountingReportsRx_Type()
)
apFlowMgrStatSSAccountingReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSAccountingReportsRx.setStatus("current")
_ApFlowMgrStatSSResets_Type = Integer32
_ApFlowMgrStatSSResets_Object = MibTableColumn
apFlowMgrStatSSResets = _ApFlowMgrStatSSResets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 14),
    _ApFlowMgrStatSSResets_Type()
)
apFlowMgrStatSSResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSResets.setStatus("current")
_ApFlowMgrStatSSFcbCount_Type = Integer32
_ApFlowMgrStatSSFcbCount_Object = MibTableColumn
apFlowMgrStatSSFcbCount = _ApFlowMgrStatSSFcbCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 15, 1, 15),
    _ApFlowMgrStatSSFcbCount_Type()
)
apFlowMgrStatSSFcbCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrStatSSFcbCount.setStatus("current")
_ApFlowMgrPortTable_Object = MibTable
apFlowMgrPortTable = _ApFlowMgrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16)
)
if mibBuilder.loadTexts:
    apFlowMgrPortTable.setStatus("current")
_ApFlowMgrPortEntry_Object = MibTableRow
apFlowMgrPortEntry = _ApFlowMgrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1)
)
apFlowMgrPortEntry.setIndexNames(
    (0, "FLOWMGREXT-MIB", "apFlowMgrPortIfIndex"),
)
if mibBuilder.loadTexts:
    apFlowMgrPortEntry.setStatus("current")
_ApFlowMgrPortIfIndex_Type = Integer32
_ApFlowMgrPortIfIndex_Object = MibTableColumn
apFlowMgrPortIfIndex = _ApFlowMgrPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 1),
    _ApFlowMgrPortIfIndex_Type()
)
apFlowMgrPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortIfIndex.setStatus("current")
_ApFlowMgrPortSeqBytes_Type = Counter64
_ApFlowMgrPortSeqBytes_Object = MibTableColumn
apFlowMgrPortSeqBytes = _ApFlowMgrPortSeqBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 2),
    _ApFlowMgrPortSeqBytes_Type()
)
apFlowMgrPortSeqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortSeqBytes.setStatus("current")
_ApFlowMgrPortInBytes_Type = Counter64
_ApFlowMgrPortInBytes_Object = MibTableColumn
apFlowMgrPortInBytes = _ApFlowMgrPortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 3),
    _ApFlowMgrPortInBytes_Type()
)
apFlowMgrPortInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortInBytes.setStatus("current")
_ApFlowMgrPortOutBytes_Type = Counter64
_ApFlowMgrPortOutBytes_Object = MibTableColumn
apFlowMgrPortOutBytes = _ApFlowMgrPortOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 4),
    _ApFlowMgrPortOutBytes_Type()
)
apFlowMgrPortOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortOutBytes.setStatus("current")
_ApFlowMgrPortInFrames_Type = Counter64
_ApFlowMgrPortInFrames_Object = MibTableColumn
apFlowMgrPortInFrames = _ApFlowMgrPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 5),
    _ApFlowMgrPortInFrames_Type()
)
apFlowMgrPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortInFrames.setStatus("current")
_ApFlowMgrPortOutFrames_Type = Counter64
_ApFlowMgrPortOutFrames_Object = MibTableColumn
apFlowMgrPortOutFrames = _ApFlowMgrPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 6),
    _ApFlowMgrPortOutFrames_Type()
)
apFlowMgrPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortOutFrames.setStatus("current")
_ApFlowMgrPortTotalInFlows_Type = Counter64
_ApFlowMgrPortTotalInFlows_Object = MibTableColumn
apFlowMgrPortTotalInFlows = _ApFlowMgrPortTotalInFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 7),
    _ApFlowMgrPortTotalInFlows_Type()
)
apFlowMgrPortTotalInFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortTotalInFlows.setStatus("current")
_ApFlowMgrPortTotalOutFlows_Type = Counter64
_ApFlowMgrPortTotalOutFlows_Object = MibTableColumn
apFlowMgrPortTotalOutFlows = _ApFlowMgrPortTotalOutFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 8),
    _ApFlowMgrPortTotalOutFlows_Type()
)
apFlowMgrPortTotalOutFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortTotalOutFlows.setStatus("current")
_ApFlowMgrPortTotalAcctFlows_Type = Counter64
_ApFlowMgrPortTotalAcctFlows_Object = MibTableColumn
apFlowMgrPortTotalAcctFlows = _ApFlowMgrPortTotalAcctFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 9),
    _ApFlowMgrPortTotalAcctFlows_Type()
)
apFlowMgrPortTotalAcctFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortTotalAcctFlows.setStatus("current")
_ApFlowMgrPortCurrTCPFlows_Type = Integer32
_ApFlowMgrPortCurrTCPFlows_Object = MibTableColumn
apFlowMgrPortCurrTCPFlows = _ApFlowMgrPortCurrTCPFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 10),
    _ApFlowMgrPortCurrTCPFlows_Type()
)
apFlowMgrPortCurrTCPFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortCurrTCPFlows.setStatus("current")
_ApFlowMgrPortCurrUDPFlows_Type = Integer32
_ApFlowMgrPortCurrUDPFlows_Object = MibTableColumn
apFlowMgrPortCurrUDPFlows = _ApFlowMgrPortCurrUDPFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 11),
    _ApFlowMgrPortCurrUDPFlows_Type()
)
apFlowMgrPortCurrUDPFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortCurrUDPFlows.setStatus("current")
_ApFlowMgrPortCurrInFlows_Type = Integer32
_ApFlowMgrPortCurrInFlows_Object = MibTableColumn
apFlowMgrPortCurrInFlows = _ApFlowMgrPortCurrInFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 12),
    _ApFlowMgrPortCurrInFlows_Type()
)
apFlowMgrPortCurrInFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortCurrInFlows.setStatus("current")
_ApFlowMgrPortCurrOutFlows_Type = Integer32
_ApFlowMgrPortCurrOutFlows_Object = MibTableColumn
apFlowMgrPortCurrOutFlows = _ApFlowMgrPortCurrOutFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 13),
    _ApFlowMgrPortCurrOutFlows_Type()
)
apFlowMgrPortCurrOutFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortCurrOutFlows.setStatus("current")
_ApFlowMgrPortResetCount_Type = Integer32
_ApFlowMgrPortResetCount_Object = MibTableColumn
apFlowMgrPortResetCount = _ApFlowMgrPortResetCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 14),
    _ApFlowMgrPortResetCount_Type()
)
apFlowMgrPortResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortResetCount.setStatus("current")
_ApFlowMgrPortMTU_Type = Integer32
_ApFlowMgrPortMTU_Object = MibTableColumn
apFlowMgrPortMTU = _ApFlowMgrPortMTU_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 15),
    _ApFlowMgrPortMTU_Type()
)
apFlowMgrPortMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortMTU.setStatus("current")
_ApFlowMgrPortWccAccepted_Type = Integer32
_ApFlowMgrPortWccAccepted_Object = MibTableColumn
apFlowMgrPortWccAccepted = _ApFlowMgrPortWccAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 16),
    _ApFlowMgrPortWccAccepted_Type()
)
apFlowMgrPortWccAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccAccepted.setStatus("current")
_ApFlowMgrPortWccAcceptedSticky_Type = Integer32
_ApFlowMgrPortWccAcceptedSticky_Object = MibTableColumn
apFlowMgrPortWccAcceptedSticky = _ApFlowMgrPortWccAcceptedSticky_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 17),
    _ApFlowMgrPortWccAcceptedSticky_Type()
)
apFlowMgrPortWccAcceptedSticky.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccAcceptedSticky.setStatus("current")
_ApFlowMgrPortWccAcceptedBridge_Type = Integer32
_ApFlowMgrPortWccAcceptedBridge_Object = MibTableColumn
apFlowMgrPortWccAcceptedBridge = _ApFlowMgrPortWccAcceptedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 18),
    _ApFlowMgrPortWccAcceptedBridge_Type()
)
apFlowMgrPortWccAcceptedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccAcceptedBridge.setStatus("current")
_ApFlowMgrPortWccAcceptedSfpFwd_Type = Integer32
_ApFlowMgrPortWccAcceptedSfpFwd_Object = MibTableColumn
apFlowMgrPortWccAcceptedSfpFwd = _ApFlowMgrPortWccAcceptedSfpFwd_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 19),
    _ApFlowMgrPortWccAcceptedSfpFwd_Type()
)
apFlowMgrPortWccAcceptedSfpFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccAcceptedSfpFwd.setStatus("current")
_ApFlowMgrPortWccAcceptedSfp_Type = Integer32
_ApFlowMgrPortWccAcceptedSfp_Object = MibTableColumn
apFlowMgrPortWccAcceptedSfp = _ApFlowMgrPortWccAcceptedSfp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 20),
    _ApFlowMgrPortWccAcceptedSfp_Type()
)
apFlowMgrPortWccAcceptedSfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccAcceptedSfp.setStatus("current")
_ApFlowMgrPortWccForwardSfp_Type = Integer32
_ApFlowMgrPortWccForwardSfp_Object = MibTableColumn
apFlowMgrPortWccForwardSfp = _ApFlowMgrPortWccForwardSfp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 21),
    _ApFlowMgrPortWccForwardSfp_Type()
)
apFlowMgrPortWccForwardSfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccForwardSfp.setStatus("current")
_ApFlowMgrPortWccForward_Type = Integer32
_ApFlowMgrPortWccForward_Object = MibTableColumn
apFlowMgrPortWccForward = _ApFlowMgrPortWccForward_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 22),
    _ApFlowMgrPortWccForward_Type()
)
apFlowMgrPortWccForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccForward.setStatus("current")
_ApFlowMgrPortWccLocal_Type = Integer32
_ApFlowMgrPortWccLocal_Object = MibTableColumn
apFlowMgrPortWccLocal = _ApFlowMgrPortWccLocal_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 23),
    _ApFlowMgrPortWccLocal_Type()
)
apFlowMgrPortWccLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccLocal.setStatus("current")
_ApFlowMgrPortWccTCPSpoof_Type = Integer32
_ApFlowMgrPortWccTCPSpoof_Object = MibTableColumn
apFlowMgrPortWccTCPSpoof = _ApFlowMgrPortWccTCPSpoof_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 24),
    _ApFlowMgrPortWccTCPSpoof_Type()
)
apFlowMgrPortWccTCPSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccTCPSpoof.setStatus("current")
_ApFlowMgrPortWccArpPending_Type = Integer32
_ApFlowMgrPortWccArpPending_Object = MibTableColumn
apFlowMgrPortWccArpPending = _ApFlowMgrPortWccArpPending_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 25),
    _ApFlowMgrPortWccArpPending_Type()
)
apFlowMgrPortWccArpPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccArpPending.setStatus("current")
_ApFlowMgrPortWccRedirect_Type = Integer32
_ApFlowMgrPortWccRedirect_Object = MibTableColumn
apFlowMgrPortWccRedirect = _ApFlowMgrPortWccRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 26),
    _ApFlowMgrPortWccRedirect_Type()
)
apFlowMgrPortWccRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccRedirect.setStatus("current")
_ApFlowMgrPortWccRedirectSticky_Type = Integer32
_ApFlowMgrPortWccRedirectSticky_Object = MibTableColumn
apFlowMgrPortWccRedirectSticky = _ApFlowMgrPortWccRedirectSticky_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 27),
    _ApFlowMgrPortWccRedirectSticky_Type()
)
apFlowMgrPortWccRedirectSticky.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccRedirectSticky.setStatus("current")
_ApFlowMgrPortWccNoChange_Type = Integer32
_ApFlowMgrPortWccNoChange_Object = MibTableColumn
apFlowMgrPortWccNoChange = _ApFlowMgrPortWccNoChange_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 28),
    _ApFlowMgrPortWccNoChange_Type()
)
apFlowMgrPortWccNoChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccNoChange.setStatus("current")
_ApFlowMgrPortWccRouteNotFound_Type = Integer32
_ApFlowMgrPortWccRouteNotFound_Object = MibTableColumn
apFlowMgrPortWccRouteNotFound = _ApFlowMgrPortWccRouteNotFound_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 29),
    _ApFlowMgrPortWccRouteNotFound_Type()
)
apFlowMgrPortWccRouteNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccRouteNotFound.setStatus("current")
_ApFlowMgrPortWccRtLookupError_Type = Integer32
_ApFlowMgrPortWccRtLookupError_Object = MibTableColumn
apFlowMgrPortWccRtLookupError = _ApFlowMgrPortWccRtLookupError_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 30),
    _ApFlowMgrPortWccRtLookupError_Type()
)
apFlowMgrPortWccRtLookupError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccRtLookupError.setStatus("current")
_ApFlowMgrPortWccDiscard_Type = Integer32
_ApFlowMgrPortWccDiscard_Object = MibTableColumn
apFlowMgrPortWccDiscard = _ApFlowMgrPortWccDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 31),
    _ApFlowMgrPortWccDiscard_Type()
)
apFlowMgrPortWccDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccDiscard.setStatus("current")
_ApFlowMgrPortWccRejected_Type = Integer32
_ApFlowMgrPortWccRejected_Object = MibTableColumn
apFlowMgrPortWccRejected = _ApFlowMgrPortWccRejected_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 32),
    _ApFlowMgrPortWccRejected_Type()
)
apFlowMgrPortWccRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccRejected.setStatus("current")
_ApFlowMgrPortWccRejectedSfp_Type = Integer32
_ApFlowMgrPortWccRejectedSfp_Object = MibTableColumn
apFlowMgrPortWccRejectedSfp = _ApFlowMgrPortWccRejectedSfp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 33),
    _ApFlowMgrPortWccRejectedSfp_Type()
)
apFlowMgrPortWccRejectedSfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortWccRejectedSfp.setStatus("current")
_ApFlowMgrPortTotalAckDelete_Type = Integer32
_ApFlowMgrPortTotalAckDelete_Object = MibTableColumn
apFlowMgrPortTotalAckDelete = _ApFlowMgrPortTotalAckDelete_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 34),
    _ApFlowMgrPortTotalAckDelete_Type()
)
apFlowMgrPortTotalAckDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortTotalAckDelete.setStatus("current")
_ApFlowMgrPortPortAckDelete_Type = Integer32
_ApFlowMgrPortPortAckDelete_Object = MibTableColumn
apFlowMgrPortPortAckDelete = _ApFlowMgrPortPortAckDelete_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 35),
    _ApFlowMgrPortPortAckDelete_Type()
)
apFlowMgrPortPortAckDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortPortAckDelete.setStatus("current")
_ApFlowMgrPortMidSpoofRejects_Type = Integer32
_ApFlowMgrPortMidSpoofRejects_Object = MibTableColumn
apFlowMgrPortMidSpoofRejects = _ApFlowMgrPortMidSpoofRejects_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 36),
    _ApFlowMgrPortMidSpoofRejects_Type()
)
apFlowMgrPortMidSpoofRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortMidSpoofRejects.setStatus("current")
_ApFlowMgrPortMidNATReject_Type = Integer32
_ApFlowMgrPortMidNATReject_Object = MibTableColumn
apFlowMgrPortMidNATReject = _ApFlowMgrPortMidNATReject_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 37),
    _ApFlowMgrPortMidNATReject_Type()
)
apFlowMgrPortMidNATReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortMidNATReject.setStatus("current")
_ApFlowMgrPortMidStickyReject_Type = Integer32
_ApFlowMgrPortMidStickyReject_Object = MibTableColumn
apFlowMgrPortMidStickyReject = _ApFlowMgrPortMidStickyReject_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 38),
    _ApFlowMgrPortMidStickyReject_Type()
)
apFlowMgrPortMidStickyReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortMidStickyReject.setStatus("current")
_ApFlowMgrPortSynExceedDelete_Type = Integer32
_ApFlowMgrPortSynExceedDelete_Object = MibTableColumn
apFlowMgrPortSynExceedDelete = _ApFlowMgrPortSynExceedDelete_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 39),
    _ApFlowMgrPortSynExceedDelete_Type()
)
apFlowMgrPortSynExceedDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortSynExceedDelete.setStatus("current")
_ApFlowMgrPortInvalidIP_Type = Integer32
_ApFlowMgrPortInvalidIP_Object = MibTableColumn
apFlowMgrPortInvalidIP = _ApFlowMgrPortInvalidIP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 40),
    _ApFlowMgrPortInvalidIP_Type()
)
apFlowMgrPortInvalidIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortInvalidIP.setStatus("current")
_ApFlowMgrPortBufferShortage_Type = Integer32
_ApFlowMgrPortBufferShortage_Object = MibTableColumn
apFlowMgrPortBufferShortage = _ApFlowMgrPortBufferShortage_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 41),
    _ApFlowMgrPortBufferShortage_Type()
)
apFlowMgrPortBufferShortage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortBufferShortage.setStatus("current")
_ApFlowMgrPortMovedAcctReports_Type = Integer32
_ApFlowMgrPortMovedAcctReports_Object = MibTableColumn
apFlowMgrPortMovedAcctReports = _ApFlowMgrPortMovedAcctReports_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 42),
    _ApFlowMgrPortMovedAcctReports_Type()
)
apFlowMgrPortMovedAcctReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortMovedAcctReports.setStatus("current")
_ApFlowMgrPortUknownQueries_Type = Integer32
_ApFlowMgrPortUknownQueries_Object = MibTableColumn
apFlowMgrPortUknownQueries = _ApFlowMgrPortUknownQueries_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 43),
    _ApFlowMgrPortUknownQueries_Type()
)
apFlowMgrPortUknownQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortUknownQueries.setStatus("current")
_ApFlowMgrPortMappedLeftovers_Type = Integer32
_ApFlowMgrPortMappedLeftovers_Object = MibTableColumn
apFlowMgrPortMappedLeftovers = _ApFlowMgrPortMappedLeftovers_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 44),
    _ApFlowMgrPortMappedLeftovers_Type()
)
apFlowMgrPortMappedLeftovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortMappedLeftovers.setStatus("current")
_ApFlowMgrPortUnmappedLeftovers_Type = Integer32
_ApFlowMgrPortUnmappedLeftovers_Object = MibTableColumn
apFlowMgrPortUnmappedLeftovers = _ApFlowMgrPortUnmappedLeftovers_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 45),
    _ApFlowMgrPortUnmappedLeftovers_Type()
)
apFlowMgrPortUnmappedLeftovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortUnmappedLeftovers.setStatus("current")
_ApFlowMgrPortRemappedIngress_Type = Integer32
_ApFlowMgrPortRemappedIngress_Object = MibTableColumn
apFlowMgrPortRemappedIngress = _ApFlowMgrPortRemappedIngress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 46),
    _ApFlowMgrPortRemappedIngress_Type()
)
apFlowMgrPortRemappedIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortRemappedIngress.setStatus("current")
_ApFlowMgrPortFlowsUnavailable_Type = Integer32
_ApFlowMgrPortFlowsUnavailable_Object = MibTableColumn
apFlowMgrPortFlowsUnavailable = _ApFlowMgrPortFlowsUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 47),
    _ApFlowMgrPortFlowsUnavailable_Type()
)
apFlowMgrPortFlowsUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortFlowsUnavailable.setStatus("current")
_ApFlowMgrPortTCPCsumErrors_Type = Integer32
_ApFlowMgrPortTCPCsumErrors_Object = MibTableColumn
apFlowMgrPortTCPCsumErrors = _ApFlowMgrPortTCPCsumErrors_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 48),
    _ApFlowMgrPortTCPCsumErrors_Type()
)
apFlowMgrPortTCPCsumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortTCPCsumErrors.setStatus("current")
_ApFlowMgrPortOverflowMaps_Type = Integer32
_ApFlowMgrPortOverflowMaps_Object = MibTableColumn
apFlowMgrPortOverflowMaps = _ApFlowMgrPortOverflowMaps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 49),
    _ApFlowMgrPortOverflowMaps_Type()
)
apFlowMgrPortOverflowMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortOverflowMaps.setStatus("current")
_ApFlowMgrPortRouteChangeEvents_Type = Integer32
_ApFlowMgrPortRouteChangeEvents_Object = MibTableColumn
apFlowMgrPortRouteChangeEvents = _ApFlowMgrPortRouteChangeEvents_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 50),
    _ApFlowMgrPortRouteChangeEvents_Type()
)
apFlowMgrPortRouteChangeEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortRouteChangeEvents.setStatus("current")
_ApFlowMgrPortRouteChangeFlows_Type = Integer32
_ApFlowMgrPortRouteChangeFlows_Object = MibTableColumn
apFlowMgrPortRouteChangeFlows = _ApFlowMgrPortRouteChangeFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 51),
    _ApFlowMgrPortRouteChangeFlows_Type()
)
apFlowMgrPortRouteChangeFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortRouteChangeFlows.setStatus("current")
_ApFlowMgrPortRouteChangeRemaps_Type = Integer32
_ApFlowMgrPortRouteChangeRemaps_Object = MibTableColumn
apFlowMgrPortRouteChangeRemaps = _ApFlowMgrPortRouteChangeRemaps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 52),
    _ApFlowMgrPortRouteChangeRemaps_Type()
)
apFlowMgrPortRouteChangeRemaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortRouteChangeRemaps.setStatus("current")
_ApFlowMgrPortOrphanMappings_Type = Integer32
_ApFlowMgrPortOrphanMappings_Object = MibTableColumn
apFlowMgrPortOrphanMappings = _ApFlowMgrPortOrphanMappings_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 16, 1, 53),
    _ApFlowMgrPortOrphanMappings_Type()
)
apFlowMgrPortOrphanMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrPortOrphanMappings.setStatus("current")
_ApFlowMgrDetailTable_Object = MibTable
apFlowMgrDetailTable = _ApFlowMgrDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17)
)
if mibBuilder.loadTexts:
    apFlowMgrDetailTable.setStatus("current")
_ApFlowMgrDetailEntry_Object = MibTableRow
apFlowMgrDetailEntry = _ApFlowMgrDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1)
)
apFlowMgrDetailEntry.setIndexNames(
    (0, "FLOWMGREXT-MIB", "apFlowMgrDetailIfIndex"),
)
if mibBuilder.loadTexts:
    apFlowMgrDetailEntry.setStatus("current")
_ApFlowMgrDetailIfIndex_Type = Integer32
_ApFlowMgrDetailIfIndex_Object = MibTableColumn
apFlowMgrDetailIfIndex = _ApFlowMgrDetailIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 1),
    _ApFlowMgrDetailIfIndex_Type()
)
apFlowMgrDetailIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailIfIndex.setStatus("current")
_ApFlowMgrDetailSeqBytes_Type = Integer32
_ApFlowMgrDetailSeqBytes_Object = MibTableColumn
apFlowMgrDetailSeqBytes = _ApFlowMgrDetailSeqBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 2),
    _ApFlowMgrDetailSeqBytes_Type()
)
apFlowMgrDetailSeqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailSeqBytes.setStatus("current")
_ApFlowMgrDetailFlags_Type = Integer32
_ApFlowMgrDetailFlags_Object = MibTableColumn
apFlowMgrDetailFlags = _ApFlowMgrDetailFlags_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 3),
    _ApFlowMgrDetailFlags_Type()
)
apFlowMgrDetailFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailFlags.setStatus("current")
_ApFlowMgrDetailPoolFlows_Type = Integer32
_ApFlowMgrDetailPoolFlows_Object = MibTableColumn
apFlowMgrDetailPoolFlows = _ApFlowMgrDetailPoolFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 4),
    _ApFlowMgrDetailPoolFlows_Type()
)
apFlowMgrDetailPoolFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailPoolFlows.setStatus("current")
_ApFlowMgrDetailInBytes_Type = Integer32
_ApFlowMgrDetailInBytes_Object = MibTableColumn
apFlowMgrDetailInBytes = _ApFlowMgrDetailInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 5),
    _ApFlowMgrDetailInBytes_Type()
)
apFlowMgrDetailInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInBytes.setStatus("current")
_ApFlowMgrDetailOutBytes_Type = Integer32
_ApFlowMgrDetailOutBytes_Object = MibTableColumn
apFlowMgrDetailOutBytes = _ApFlowMgrDetailOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 6),
    _ApFlowMgrDetailOutBytes_Type()
)
apFlowMgrDetailOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailOutBytes.setStatus("current")
_ApFlowMgrDetailInFrames_Type = Integer32
_ApFlowMgrDetailInFrames_Object = MibTableColumn
apFlowMgrDetailInFrames = _ApFlowMgrDetailInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 7),
    _ApFlowMgrDetailInFrames_Type()
)
apFlowMgrDetailInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInFrames.setStatus("current")
_ApFlowMgrDetailTotalInFlows_Type = Integer32
_ApFlowMgrDetailTotalInFlows_Object = MibTableColumn
apFlowMgrDetailTotalInFlows = _ApFlowMgrDetailTotalInFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 8),
    _ApFlowMgrDetailTotalInFlows_Type()
)
apFlowMgrDetailTotalInFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailTotalInFlows.setStatus("current")
_ApFlowMgrDetailTotalOutFlows_Type = Integer32
_ApFlowMgrDetailTotalOutFlows_Object = MibTableColumn
apFlowMgrDetailTotalOutFlows = _ApFlowMgrDetailTotalOutFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 9),
    _ApFlowMgrDetailTotalOutFlows_Type()
)
apFlowMgrDetailTotalOutFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailTotalOutFlows.setStatus("current")
_ApFlowMgrDetailTotalAcctFlows_Type = Integer32
_ApFlowMgrDetailTotalAcctFlows_Object = MibTableColumn
apFlowMgrDetailTotalAcctFlows = _ApFlowMgrDetailTotalAcctFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 10),
    _ApFlowMgrDetailTotalAcctFlows_Type()
)
apFlowMgrDetailTotalAcctFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailTotalAcctFlows.setStatus("current")
_ApFlowMgrDetailResetCount_Type = Integer32
_ApFlowMgrDetailResetCount_Object = MibTableColumn
apFlowMgrDetailResetCount = _ApFlowMgrDetailResetCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 11),
    _ApFlowMgrDetailResetCount_Type()
)
apFlowMgrDetailResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailResetCount.setStatus("current")
_ApFlowMgrDetailCurTCPFlows_Type = Integer32
_ApFlowMgrDetailCurTCPFlows_Object = MibTableColumn
apFlowMgrDetailCurTCPFlows = _ApFlowMgrDetailCurTCPFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 12),
    _ApFlowMgrDetailCurTCPFlows_Type()
)
apFlowMgrDetailCurTCPFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailCurTCPFlows.setStatus("current")
_ApFlowMgrDetailCurUDPFlows_Type = Integer32
_ApFlowMgrDetailCurUDPFlows_Object = MibTableColumn
apFlowMgrDetailCurUDPFlows = _ApFlowMgrDetailCurUDPFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 13),
    _ApFlowMgrDetailCurUDPFlows_Type()
)
apFlowMgrDetailCurUDPFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailCurUDPFlows.setStatus("current")
_ApFlowMgrDetailCurInFlows_Type = Integer32
_ApFlowMgrDetailCurInFlows_Object = MibTableColumn
apFlowMgrDetailCurInFlows = _ApFlowMgrDetailCurInFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 14),
    _ApFlowMgrDetailCurInFlows_Type()
)
apFlowMgrDetailCurInFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailCurInFlows.setStatus("current")
_ApFlowMgrDetailCurOutFlows_Type = Integer32
_ApFlowMgrDetailCurOutFlows_Object = MibTableColumn
apFlowMgrDetailCurOutFlows = _ApFlowMgrDetailCurOutFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 15),
    _ApFlowMgrDetailCurOutFlows_Type()
)
apFlowMgrDetailCurOutFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailCurOutFlows.setStatus("current")
_ApFlowMgrDetailFPFlowCount_Type = Integer32
_ApFlowMgrDetailFPFlowCount_Object = MibTableColumn
apFlowMgrDetailFPFlowCount = _ApFlowMgrDetailFPFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 16),
    _ApFlowMgrDetailFPFlowCount_Type()
)
apFlowMgrDetailFPFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailFPFlowCount.setStatus("current")
_ApFlowMgrDetailTotalInFlowMap_Type = Integer32
_ApFlowMgrDetailTotalInFlowMap_Object = MibTableColumn
apFlowMgrDetailTotalInFlowMap = _ApFlowMgrDetailTotalInFlowMap_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 17),
    _ApFlowMgrDetailTotalInFlowMap_Type()
)
apFlowMgrDetailTotalInFlowMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailTotalInFlowMap.setStatus("current")
_ApFlowMgrDetailInMappedOnlyPrimary_Type = Integer32
_ApFlowMgrDetailInMappedOnlyPrimary_Object = MibTableColumn
apFlowMgrDetailInMappedOnlyPrimary = _ApFlowMgrDetailInMappedOnlyPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 18),
    _ApFlowMgrDetailInMappedOnlyPrimary_Type()
)
apFlowMgrDetailInMappedOnlyPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInMappedOnlyPrimary.setStatus("current")
_ApFlowMgrDetailInMappedOnlyPrevious_Type = Integer32
_ApFlowMgrDetailInMappedOnlyPrevious_Object = MibTableColumn
apFlowMgrDetailInMappedOnlyPrevious = _ApFlowMgrDetailInMappedOnlyPrevious_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 19),
    _ApFlowMgrDetailInMappedOnlyPrevious_Type()
)
apFlowMgrDetailInMappedOnlyPrevious.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInMappedOnlyPrevious.setStatus("current")
_ApFlowMgrDetailInMappedBothPrimary_Type = Integer32
_ApFlowMgrDetailInMappedBothPrimary_Object = MibTableColumn
apFlowMgrDetailInMappedBothPrimary = _ApFlowMgrDetailInMappedBothPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 20),
    _ApFlowMgrDetailInMappedBothPrimary_Type()
)
apFlowMgrDetailInMappedBothPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInMappedBothPrimary.setStatus("current")
_ApFlowMgrDetailInMappedBothPrevious_Type = Integer32
_ApFlowMgrDetailInMappedBothPrevious_Object = MibTableColumn
apFlowMgrDetailInMappedBothPrevious = _ApFlowMgrDetailInMappedBothPrevious_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 21),
    _ApFlowMgrDetailInMappedBothPrevious_Type()
)
apFlowMgrDetailInMappedBothPrevious.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInMappedBothPrevious.setStatus("current")
_ApFlowMgrDetailInNoFPMappings_Type = Integer32
_ApFlowMgrDetailInNoFPMappings_Object = MibTableColumn
apFlowMgrDetailInNoFPMappings = _ApFlowMgrDetailInNoFPMappings_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 22),
    _ApFlowMgrDetailInNoFPMappings_Type()
)
apFlowMgrDetailInNoFPMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInNoFPMappings.setStatus("current")
_ApFlowMgrDetailInIngressQueueLen_Type = Integer32
_ApFlowMgrDetailInIngressQueueLen_Object = MibTableColumn
apFlowMgrDetailInIngressQueueLen = _ApFlowMgrDetailInIngressQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 23),
    _ApFlowMgrDetailInIngressQueueLen_Type()
)
apFlowMgrDetailInIngressQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInIngressQueueLen.setStatus("current")
_ApFlowMgrDetailInOrphanFCBFlows_Type = Integer32
_ApFlowMgrDetailInOrphanFCBFlows_Object = MibTableColumn
apFlowMgrDetailInOrphanFCBFlows = _ApFlowMgrDetailInOrphanFCBFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 24),
    _ApFlowMgrDetailInOrphanFCBFlows_Type()
)
apFlowMgrDetailInOrphanFCBFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInOrphanFCBFlows.setStatus("current")
_ApFlowMgrDetailInTotalOrphanFCB_Type = Integer32
_ApFlowMgrDetailInTotalOrphanFCB_Object = MibTableColumn
apFlowMgrDetailInTotalOrphanFCB = _ApFlowMgrDetailInTotalOrphanFCB_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 25),
    _ApFlowMgrDetailInTotalOrphanFCB_Type()
)
apFlowMgrDetailInTotalOrphanFCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInTotalOrphanFCB.setStatus("current")
_ApFlowMgrDetailInTCPPermPort_Type = Integer32
_ApFlowMgrDetailInTCPPermPort_Object = MibTableColumn
apFlowMgrDetailInTCPPermPort = _ApFlowMgrDetailInTCPPermPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 26),
    _ApFlowMgrDetailInTCPPermPort_Type()
)
apFlowMgrDetailInTCPPermPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInTCPPermPort.setStatus("current")
_ApFlowMgrDetailInUDPPermPort_Type = Integer32
_ApFlowMgrDetailInUDPPermPort_Object = MibTableColumn
apFlowMgrDetailInUDPPermPort = _ApFlowMgrDetailInUDPPermPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 27),
    _ApFlowMgrDetailInUDPPermPort_Type()
)
apFlowMgrDetailInUDPPermPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInUDPPermPort.setStatus("current")
_ApFlowMgrDetailInJoined_Type = Integer32
_ApFlowMgrDetailInJoined_Object = MibTableColumn
apFlowMgrDetailInJoined = _ApFlowMgrDetailInJoined_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 28),
    _ApFlowMgrDetailInJoined_Type()
)
apFlowMgrDetailInJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInJoined.setStatus("current")
_ApFlowMgrDetailInContentExpected_Type = Integer32
_ApFlowMgrDetailInContentExpected_Object = MibTableColumn
apFlowMgrDetailInContentExpected = _ApFlowMgrDetailInContentExpected_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 29),
    _ApFlowMgrDetailInContentExpected_Type()
)
apFlowMgrDetailInContentExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInContentExpected.setStatus("current")
_ApFlowMgrDetailInJoinPending_Type = Integer32
_ApFlowMgrDetailInJoinPending_Object = MibTableColumn
apFlowMgrDetailInJoinPending = _ApFlowMgrDetailInJoinPending_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 30),
    _ApFlowMgrDetailInJoinPending_Type()
)
apFlowMgrDetailInJoinPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInJoinPending.setStatus("current")
_ApFlowMgrDetailInContentPending_Type = Integer32
_ApFlowMgrDetailInContentPending_Object = MibTableColumn
apFlowMgrDetailInContentPending = _ApFlowMgrDetailInContentPending_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 31),
    _ApFlowMgrDetailInContentPending_Type()
)
apFlowMgrDetailInContentPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInContentPending.setStatus("current")
_ApFlowMgrDetailInTCPSYNSent_Type = Integer32
_ApFlowMgrDetailInTCPSYNSent_Object = MibTableColumn
apFlowMgrDetailInTCPSYNSent = _ApFlowMgrDetailInTCPSYNSent_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 32),
    _ApFlowMgrDetailInTCPSYNSent_Type()
)
apFlowMgrDetailInTCPSYNSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInTCPSYNSent.setStatus("current")
_ApFlowMgrDetailInReversePending_Type = Integer32
_ApFlowMgrDetailInReversePending_Object = MibTableColumn
apFlowMgrDetailInReversePending = _ApFlowMgrDetailInReversePending_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 33),
    _ApFlowMgrDetailInReversePending_Type()
)
apFlowMgrDetailInReversePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInReversePending.setStatus("current")
_ApFlowMgrDetailInSFPForwarded_Type = Integer32
_ApFlowMgrDetailInSFPForwarded_Object = MibTableColumn
apFlowMgrDetailInSFPForwarded = _ApFlowMgrDetailInSFPForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 34),
    _ApFlowMgrDetailInSFPForwarded_Type()
)
apFlowMgrDetailInSFPForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSFPForwarded.setStatus("current")
_ApFlowMgrDetailInInPortInflowCount_Type = Integer32
_ApFlowMgrDetailInInPortInflowCount_Object = MibTableColumn
apFlowMgrDetailInInPortInflowCount = _ApFlowMgrDetailInInPortInflowCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 35),
    _ApFlowMgrDetailInInPortInflowCount_Type()
)
apFlowMgrDetailInInPortInflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInInPortInflowCount.setStatus("current")
_ApFlowMgrDetailInDeleted_Type = Integer32
_ApFlowMgrDetailInDeleted_Object = MibTableColumn
apFlowMgrDetailInDeleted = _ApFlowMgrDetailInDeleted_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 36),
    _ApFlowMgrDetailInDeleted_Type()
)
apFlowMgrDetailInDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInDeleted.setStatus("current")
_ApFlowMgrDetailInSpoofed_Type = Integer32
_ApFlowMgrDetailInSpoofed_Object = MibTableColumn
apFlowMgrDetailInSpoofed = _ApFlowMgrDetailInSpoofed_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 37),
    _ApFlowMgrDetailInSpoofed_Type()
)
apFlowMgrDetailInSpoofed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSpoofed.setStatus("current")
_ApFlowMgrDetailInNATInUse_Type = Integer32
_ApFlowMgrDetailInNATInUse_Object = MibTableColumn
apFlowMgrDetailInNATInUse = _ApFlowMgrDetailInNATInUse_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 38),
    _ApFlowMgrDetailInNATInUse_Type()
)
apFlowMgrDetailInNATInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInNATInUse.setStatus("current")
_ApFlowMgrDetailInContentAware_Type = Integer32
_ApFlowMgrDetailInContentAware_Object = MibTableColumn
apFlowMgrDetailInContentAware = _ApFlowMgrDetailInContentAware_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 39),
    _ApFlowMgrDetailInContentAware_Type()
)
apFlowMgrDetailInContentAware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInContentAware.setStatus("current")
_ApFlowMgrDetailInSticky_Type = Integer32
_ApFlowMgrDetailInSticky_Object = MibTableColumn
apFlowMgrDetailInSticky = _ApFlowMgrDetailInSticky_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 40),
    _ApFlowMgrDetailInSticky_Type()
)
apFlowMgrDetailInSticky.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSticky.setStatus("current")
_ApFlowMgrDetailInBridged_Type = Integer32
_ApFlowMgrDetailInBridged_Object = MibTableColumn
apFlowMgrDetailInBridged = _ApFlowMgrDetailInBridged_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 41),
    _ApFlowMgrDetailInBridged_Type()
)
apFlowMgrDetailInBridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInBridged.setStatus("current")
_ApFlowMgrDetailInBuffersPending_Type = Integer32
_ApFlowMgrDetailInBuffersPending_Object = MibTableColumn
apFlowMgrDetailInBuffersPending = _ApFlowMgrDetailInBuffersPending_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 42),
    _ApFlowMgrDetailInBuffersPending_Type()
)
apFlowMgrDetailInBuffersPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInBuffersPending.setStatus("current")
_ApFlowMgrDetailInSYNDOSTimerActive_Type = Integer32
_ApFlowMgrDetailInSYNDOSTimerActive_Object = MibTableColumn
apFlowMgrDetailInSYNDOSTimerActive = _ApFlowMgrDetailInSYNDOSTimerActive_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 43),
    _ApFlowMgrDetailInSYNDOSTimerActive_Type()
)
apFlowMgrDetailInSYNDOSTimerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSYNDOSTimerActive.setStatus("current")
_ApFlowMgrDetailInOverflowMapped_Type = Integer32
_ApFlowMgrDetailInOverflowMapped_Object = MibTableColumn
apFlowMgrDetailInOverflowMapped = _ApFlowMgrDetailInOverflowMapped_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 44),
    _ApFlowMgrDetailInOverflowMapped_Type()
)
apFlowMgrDetailInOverflowMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInOverflowMapped.setStatus("current")
_ApFlowMgrDetailInRejected_Type = Integer32
_ApFlowMgrDetailInRejected_Object = MibTableColumn
apFlowMgrDetailInRejected = _ApFlowMgrDetailInRejected_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 45),
    _ApFlowMgrDetailInRejected_Type()
)
apFlowMgrDetailInRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInRejected.setStatus("current")
_ApFlowMgrDetailInTotalTCPFlows_Type = Integer32
_ApFlowMgrDetailInTotalTCPFlows_Object = MibTableColumn
apFlowMgrDetailInTotalTCPFlows = _ApFlowMgrDetailInTotalTCPFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 46),
    _ApFlowMgrDetailInTotalTCPFlows_Type()
)
apFlowMgrDetailInTotalTCPFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInTotalTCPFlows.setStatus("current")
_ApFlowMgrDetailInTotalUDPFlows_Type = Integer32
_ApFlowMgrDetailInTotalUDPFlows_Object = MibTableColumn
apFlowMgrDetailInTotalUDPFlows = _ApFlowMgrDetailInTotalUDPFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 47),
    _ApFlowMgrDetailInTotalUDPFlows_Type()
)
apFlowMgrDetailInTotalUDPFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInTotalUDPFlows.setStatus("current")
_ApFlowMgrDetailInHTTPSrcFlows_Type = Integer32
_ApFlowMgrDetailInHTTPSrcFlows_Object = MibTableColumn
apFlowMgrDetailInHTTPSrcFlows = _ApFlowMgrDetailInHTTPSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 48),
    _ApFlowMgrDetailInHTTPSrcFlows_Type()
)
apFlowMgrDetailInHTTPSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInHTTPSrcFlows.setStatus("current")
_ApFlowMgrDetailInHTTPDstFlows_Type = Integer32
_ApFlowMgrDetailInHTTPDstFlows_Object = MibTableColumn
apFlowMgrDetailInHTTPDstFlows = _ApFlowMgrDetailInHTTPDstFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 49),
    _ApFlowMgrDetailInHTTPDstFlows_Type()
)
apFlowMgrDetailInHTTPDstFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInHTTPDstFlows.setStatus("current")
_ApFlowMgrDetailInFTPDataSrcFlows_Type = Integer32
_ApFlowMgrDetailInFTPDataSrcFlows_Object = MibTableColumn
apFlowMgrDetailInFTPDataSrcFlows = _ApFlowMgrDetailInFTPDataSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 50),
    _ApFlowMgrDetailInFTPDataSrcFlows_Type()
)
apFlowMgrDetailInFTPDataSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInFTPDataSrcFlows.setStatus("current")
_ApFlowMgrDetailInFTPDataDestFlows_Type = Integer32
_ApFlowMgrDetailInFTPDataDestFlows_Object = MibTableColumn
apFlowMgrDetailInFTPDataDestFlows = _ApFlowMgrDetailInFTPDataDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 51),
    _ApFlowMgrDetailInFTPDataDestFlows_Type()
)
apFlowMgrDetailInFTPDataDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInFTPDataDestFlows.setStatus("current")
_ApFlowMgrDetailInFTPCtrlSrcFlows_Type = Integer32
_ApFlowMgrDetailInFTPCtrlSrcFlows_Object = MibTableColumn
apFlowMgrDetailInFTPCtrlSrcFlows = _ApFlowMgrDetailInFTPCtrlSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 52),
    _ApFlowMgrDetailInFTPCtrlSrcFlows_Type()
)
apFlowMgrDetailInFTPCtrlSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInFTPCtrlSrcFlows.setStatus("current")
_ApFlowMgrDetailInFTPCtrlDestFlows_Type = Integer32
_ApFlowMgrDetailInFTPCtrlDestFlows_Object = MibTableColumn
apFlowMgrDetailInFTPCtrlDestFlows = _ApFlowMgrDetailInFTPCtrlDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 53),
    _ApFlowMgrDetailInFTPCtrlDestFlows_Type()
)
apFlowMgrDetailInFTPCtrlDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInFTPCtrlDestFlows.setStatus("current")
_ApFlowMgrDetailInSSHSrcFlows_Type = Integer32
_ApFlowMgrDetailInSSHSrcFlows_Object = MibTableColumn
apFlowMgrDetailInSSHSrcFlows = _ApFlowMgrDetailInSSHSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 54),
    _ApFlowMgrDetailInSSHSrcFlows_Type()
)
apFlowMgrDetailInSSHSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSSHSrcFlows.setStatus("current")
_ApFlowMgrDetailInSSHDestFlows_Type = Integer32
_ApFlowMgrDetailInSSHDestFlows_Object = MibTableColumn
apFlowMgrDetailInSSHDestFlows = _ApFlowMgrDetailInSSHDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 55),
    _ApFlowMgrDetailInSSHDestFlows_Type()
)
apFlowMgrDetailInSSHDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSSHDestFlows.setStatus("current")
_ApFlowMgrDetailInTelnetSrcFlows_Type = Integer32
_ApFlowMgrDetailInTelnetSrcFlows_Object = MibTableColumn
apFlowMgrDetailInTelnetSrcFlows = _ApFlowMgrDetailInTelnetSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 56),
    _ApFlowMgrDetailInTelnetSrcFlows_Type()
)
apFlowMgrDetailInTelnetSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInTelnetSrcFlows.setStatus("current")
_ApFlowMgrDetailInTelnetDestFlows_Type = Integer32
_ApFlowMgrDetailInTelnetDestFlows_Object = MibTableColumn
apFlowMgrDetailInTelnetDestFlows = _ApFlowMgrDetailInTelnetDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 57),
    _ApFlowMgrDetailInTelnetDestFlows_Type()
)
apFlowMgrDetailInTelnetDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInTelnetDestFlows.setStatus("current")
_ApFlowMgrDetailInRASrcFlows_Type = Integer32
_ApFlowMgrDetailInRASrcFlows_Object = MibTableColumn
apFlowMgrDetailInRASrcFlows = _ApFlowMgrDetailInRASrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 58),
    _ApFlowMgrDetailInRASrcFlows_Type()
)
apFlowMgrDetailInRASrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInRASrcFlows.setStatus("current")
_ApFlowMgrDetailInRADestFlows_Type = Integer32
_ApFlowMgrDetailInRADestFlows_Object = MibTableColumn
apFlowMgrDetailInRADestFlows = _ApFlowMgrDetailInRADestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 59),
    _ApFlowMgrDetailInRADestFlows_Type()
)
apFlowMgrDetailInRADestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInRADestFlows.setStatus("current")
_ApFlowMgrDetailInBGPSrcFlows_Type = Integer32
_ApFlowMgrDetailInBGPSrcFlows_Object = MibTableColumn
apFlowMgrDetailInBGPSrcFlows = _ApFlowMgrDetailInBGPSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 60),
    _ApFlowMgrDetailInBGPSrcFlows_Type()
)
apFlowMgrDetailInBGPSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInBGPSrcFlows.setStatus("current")
_ApFlowMgrDetailInBGPDestFlows_Type = Integer32
_ApFlowMgrDetailInBGPDestFlows_Object = MibTableColumn
apFlowMgrDetailInBGPDestFlows = _ApFlowMgrDetailInBGPDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 61),
    _ApFlowMgrDetailInBGPDestFlows_Type()
)
apFlowMgrDetailInBGPDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInBGPDestFlows.setStatus("current")
_ApFlowMgrDetailInSMTPSrcFlows_Type = Integer32
_ApFlowMgrDetailInSMTPSrcFlows_Object = MibTableColumn
apFlowMgrDetailInSMTPSrcFlows = _ApFlowMgrDetailInSMTPSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 62),
    _ApFlowMgrDetailInSMTPSrcFlows_Type()
)
apFlowMgrDetailInSMTPSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSMTPSrcFlows.setStatus("current")
_ApFlowMgrDetailInSMTPDestFlows_Type = Integer32
_ApFlowMgrDetailInSMTPDestFlows_Object = MibTableColumn
apFlowMgrDetailInSMTPDestFlows = _ApFlowMgrDetailInSMTPDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 63),
    _ApFlowMgrDetailInSMTPDestFlows_Type()
)
apFlowMgrDetailInSMTPDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSMTPDestFlows.setStatus("current")
_ApFlowMgrDetailInPOP3SrcFlows_Type = Integer32
_ApFlowMgrDetailInPOP3SrcFlows_Object = MibTableColumn
apFlowMgrDetailInPOP3SrcFlows = _ApFlowMgrDetailInPOP3SrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 64),
    _ApFlowMgrDetailInPOP3SrcFlows_Type()
)
apFlowMgrDetailInPOP3SrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInPOP3SrcFlows.setStatus("current")
_ApFlowMgrDetailInPOP3DestFlows_Type = Integer32
_ApFlowMgrDetailInPOP3DestFlows_Object = MibTableColumn
apFlowMgrDetailInPOP3DestFlows = _ApFlowMgrDetailInPOP3DestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 65),
    _ApFlowMgrDetailInPOP3DestFlows_Type()
)
apFlowMgrDetailInPOP3DestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInPOP3DestFlows.setStatus("current")
_ApFlowMgrDetailInHTTPSSrcFlows_Type = Integer32
_ApFlowMgrDetailInHTTPSSrcFlows_Object = MibTableColumn
apFlowMgrDetailInHTTPSSrcFlows = _ApFlowMgrDetailInHTTPSSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 66),
    _ApFlowMgrDetailInHTTPSSrcFlows_Type()
)
apFlowMgrDetailInHTTPSSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInHTTPSSrcFlows.setStatus("current")
_ApFlowMgrDetailInHTTPSDestFlows_Type = Integer32
_ApFlowMgrDetailInHTTPSDestFlows_Object = MibTableColumn
apFlowMgrDetailInHTTPSDestFlows = _ApFlowMgrDetailInHTTPSDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 67),
    _ApFlowMgrDetailInHTTPSDestFlows_Type()
)
apFlowMgrDetailInHTTPSDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInHTTPSDestFlows.setStatus("current")
_ApFlowMgrDetailInNNTPSrcFlows_Type = Integer32
_ApFlowMgrDetailInNNTPSrcFlows_Object = MibTableColumn
apFlowMgrDetailInNNTPSrcFlows = _ApFlowMgrDetailInNNTPSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 68),
    _ApFlowMgrDetailInNNTPSrcFlows_Type()
)
apFlowMgrDetailInNNTPSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInNNTPSrcFlows.setStatus("current")
_ApFlowMgrDetailInNNTPDestFlows_Type = Integer32
_ApFlowMgrDetailInNNTPDestFlows_Object = MibTableColumn
apFlowMgrDetailInNNTPDestFlows = _ApFlowMgrDetailInNNTPDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 69),
    _ApFlowMgrDetailInNNTPDestFlows_Type()
)
apFlowMgrDetailInNNTPDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInNNTPDestFlows.setStatus("current")
_ApFlowMgrDetailInSOCKSSrcFlows_Type = Integer32
_ApFlowMgrDetailInSOCKSSrcFlows_Object = MibTableColumn
apFlowMgrDetailInSOCKSSrcFlows = _ApFlowMgrDetailInSOCKSSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 70),
    _ApFlowMgrDetailInSOCKSSrcFlows_Type()
)
apFlowMgrDetailInSOCKSSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSOCKSSrcFlows.setStatus("current")
_ApFlowMgrDetailInSOCKSDestFlows_Type = Integer32
_ApFlowMgrDetailInSOCKSDestFlows_Object = MibTableColumn
apFlowMgrDetailInSOCKSDestFlows = _ApFlowMgrDetailInSOCKSDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 71),
    _ApFlowMgrDetailInSOCKSDestFlows_Type()
)
apFlowMgrDetailInSOCKSDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSOCKSDestFlows.setStatus("current")
_ApFlowMgrDetailInPortLT23SrcFlows_Type = Integer32
_ApFlowMgrDetailInPortLT23SrcFlows_Object = MibTableColumn
apFlowMgrDetailInPortLT23SrcFlows = _ApFlowMgrDetailInPortLT23SrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 72),
    _ApFlowMgrDetailInPortLT23SrcFlows_Type()
)
apFlowMgrDetailInPortLT23SrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInPortLT23SrcFlows.setStatus("current")
_ApFlowMgrDetailInPortLT23DestFlows_Type = Integer32
_ApFlowMgrDetailInPortLT23DestFlows_Object = MibTableColumn
apFlowMgrDetailInPortLT23DestFlows = _ApFlowMgrDetailInPortLT23DestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 73),
    _ApFlowMgrDetailInPortLT23DestFlows_Type()
)
apFlowMgrDetailInPortLT23DestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInPortLT23DestFlows.setStatus("current")
_ApFlowMgrDetailInPortGT1024SrcFlows_Type = Integer32
_ApFlowMgrDetailInPortGT1024SrcFlows_Object = MibTableColumn
apFlowMgrDetailInPortGT1024SrcFlows = _ApFlowMgrDetailInPortGT1024SrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 74),
    _ApFlowMgrDetailInPortGT1024SrcFlows_Type()
)
apFlowMgrDetailInPortGT1024SrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInPortGT1024SrcFlows.setStatus("current")
_ApFlowMgrDetailInPortGT1024DestFlows_Type = Integer32
_ApFlowMgrDetailInPortGT1024DestFlows_Object = MibTableColumn
apFlowMgrDetailInPortGT1024DestFlows = _ApFlowMgrDetailInPortGT1024DestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 75),
    _ApFlowMgrDetailInPortGT1024DestFlows_Type()
)
apFlowMgrDetailInPortGT1024DestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInPortGT1024DestFlows.setStatus("current")
_ApFlowMgrDetailInTimeSrcFlows_Type = Integer32
_ApFlowMgrDetailInTimeSrcFlows_Object = MibTableColumn
apFlowMgrDetailInTimeSrcFlows = _ApFlowMgrDetailInTimeSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 76),
    _ApFlowMgrDetailInTimeSrcFlows_Type()
)
apFlowMgrDetailInTimeSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInTimeSrcFlows.setStatus("current")
_ApFlowMgrDetailInTimeDestSrcFlows_Type = Integer32
_ApFlowMgrDetailInTimeDestSrcFlows_Object = MibTableColumn
apFlowMgrDetailInTimeDestSrcFlows = _ApFlowMgrDetailInTimeDestSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 77),
    _ApFlowMgrDetailInTimeDestSrcFlows_Type()
)
apFlowMgrDetailInTimeDestSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInTimeDestSrcFlows.setStatus("current")
_ApFlowMgrDetailInDNSSrcFlows_Type = Integer32
_ApFlowMgrDetailInDNSSrcFlows_Object = MibTableColumn
apFlowMgrDetailInDNSSrcFlows = _ApFlowMgrDetailInDNSSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 78),
    _ApFlowMgrDetailInDNSSrcFlows_Type()
)
apFlowMgrDetailInDNSSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInDNSSrcFlows.setStatus("current")
_ApFlowMgrDetailInDNSDestFlows_Type = Integer32
_ApFlowMgrDetailInDNSDestFlows_Object = MibTableColumn
apFlowMgrDetailInDNSDestFlows = _ApFlowMgrDetailInDNSDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 79),
    _ApFlowMgrDetailInDNSDestFlows_Type()
)
apFlowMgrDetailInDNSDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInDNSDestFlows.setStatus("current")
_ApFlowMgrDetailInSNMPSrcFlows_Type = Integer32
_ApFlowMgrDetailInSNMPSrcFlows_Object = MibTableColumn
apFlowMgrDetailInSNMPSrcFlows = _ApFlowMgrDetailInSNMPSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 80),
    _ApFlowMgrDetailInSNMPSrcFlows_Type()
)
apFlowMgrDetailInSNMPSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSNMPSrcFlows.setStatus("current")
_ApFlowMgrDetailInSNMPDestFlows_Type = Integer32
_ApFlowMgrDetailInSNMPDestFlows_Object = MibTableColumn
apFlowMgrDetailInSNMPDestFlows = _ApFlowMgrDetailInSNMPDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 81),
    _ApFlowMgrDetailInSNMPDestFlows_Type()
)
apFlowMgrDetailInSNMPDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSNMPDestFlows.setStatus("current")
_ApFlowMgrDetailInSNMPTrapSrcFlows_Type = Integer32
_ApFlowMgrDetailInSNMPTrapSrcFlows_Object = MibTableColumn
apFlowMgrDetailInSNMPTrapSrcFlows = _ApFlowMgrDetailInSNMPTrapSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 82),
    _ApFlowMgrDetailInSNMPTrapSrcFlows_Type()
)
apFlowMgrDetailInSNMPTrapSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSNMPTrapSrcFlows.setStatus("current")
_ApFlowMgrDetailInSNMPTrapDestFlows_Type = Integer32
_ApFlowMgrDetailInSNMPTrapDestFlows_Object = MibTableColumn
apFlowMgrDetailInSNMPTrapDestFlows = _ApFlowMgrDetailInSNMPTrapDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 83),
    _ApFlowMgrDetailInSNMPTrapDestFlows_Type()
)
apFlowMgrDetailInSNMPTrapDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInSNMPTrapDestFlows.setStatus("current")
_ApFlowMgrDetailInNFSSrcFlows_Type = Integer32
_ApFlowMgrDetailInNFSSrcFlows_Object = MibTableColumn
apFlowMgrDetailInNFSSrcFlows = _ApFlowMgrDetailInNFSSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 84),
    _ApFlowMgrDetailInNFSSrcFlows_Type()
)
apFlowMgrDetailInNFSSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInNFSSrcFlows.setStatus("current")
_ApFlowMgrDetailInNFSDestFlows_Type = Integer32
_ApFlowMgrDetailInNFSDestFlows_Object = MibTableColumn
apFlowMgrDetailInNFSDestFlows = _ApFlowMgrDetailInNFSDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 85),
    _ApFlowMgrDetailInNFSDestFlows_Type()
)
apFlowMgrDetailInNFSDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInNFSDestFlows.setStatus("current")
_ApFlowMgrDetailInUDPGT1024SrcFlows_Type = Integer32
_ApFlowMgrDetailInUDPGT1024SrcFlows_Object = MibTableColumn
apFlowMgrDetailInUDPGT1024SrcFlows = _ApFlowMgrDetailInUDPGT1024SrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 86),
    _ApFlowMgrDetailInUDPGT1024SrcFlows_Type()
)
apFlowMgrDetailInUDPGT1024SrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInUDPGT1024SrcFlows.setStatus("current")
_ApFlowMgrDetailInUDPGT1024DestFlows_Type = Integer32
_ApFlowMgrDetailInUDPGT1024DestFlows_Object = MibTableColumn
apFlowMgrDetailInUDPGT1024DestFlows = _ApFlowMgrDetailInUDPGT1024DestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 87),
    _ApFlowMgrDetailInUDPGT1024DestFlows_Type()
)
apFlowMgrDetailInUDPGT1024DestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInUDPGT1024DestFlows.setStatus("current")
_ApFlowMgrDetailInUDPLT1024SrcFlows_Type = Integer32
_ApFlowMgrDetailInUDPLT1024SrcFlows_Object = MibTableColumn
apFlowMgrDetailInUDPLT1024SrcFlows = _ApFlowMgrDetailInUDPLT1024SrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 88),
    _ApFlowMgrDetailInUDPLT1024SrcFlows_Type()
)
apFlowMgrDetailInUDPLT1024SrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInUDPLT1024SrcFlows.setStatus("current")
_ApFlowMgrDetailInUDPLT1024DestFlows_Type = Integer32
_ApFlowMgrDetailInUDPLT1024DestFlows_Object = MibTableColumn
apFlowMgrDetailInUDPLT1024DestFlows = _ApFlowMgrDetailInUDPLT1024DestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 89),
    _ApFlowMgrDetailInUDPLT1024DestFlows_Type()
)
apFlowMgrDetailInUDPLT1024DestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInUDPLT1024DestFlows.setStatus("current")
_ApFlowMgrDetailInExplicitFlows_Type = Integer32
_ApFlowMgrDetailInExplicitFlows_Object = MibTableColumn
apFlowMgrDetailInExplicitFlows = _ApFlowMgrDetailInExplicitFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 90),
    _ApFlowMgrDetailInExplicitFlows_Type()
)
apFlowMgrDetailInExplicitFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInExplicitFlows.setStatus("current")
_ApFlowMgrDetailInAcctSent_Type = Integer32
_ApFlowMgrDetailInAcctSent_Object = MibTableColumn
apFlowMgrDetailInAcctSent = _ApFlowMgrDetailInAcctSent_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 91),
    _ApFlowMgrDetailInAcctSent_Type()
)
apFlowMgrDetailInAcctSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailInAcctSent.setStatus("current")
_ApFlowMgrDetailEgTCPPermPort_Type = Integer32
_ApFlowMgrDetailEgTCPPermPort_Object = MibTableColumn
apFlowMgrDetailEgTCPPermPort = _ApFlowMgrDetailEgTCPPermPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 92),
    _ApFlowMgrDetailEgTCPPermPort_Type()
)
apFlowMgrDetailEgTCPPermPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgTCPPermPort.setStatus("current")
_ApFlowMgrDetailEgUDPPermPort_Type = Integer32
_ApFlowMgrDetailEgUDPPermPort_Object = MibTableColumn
apFlowMgrDetailEgUDPPermPort = _ApFlowMgrDetailEgUDPPermPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 93),
    _ApFlowMgrDetailEgUDPPermPort_Type()
)
apFlowMgrDetailEgUDPPermPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgUDPPermPort.setStatus("current")
_ApFlowMgrDetailEgJoined_Type = Integer32
_ApFlowMgrDetailEgJoined_Object = MibTableColumn
apFlowMgrDetailEgJoined = _ApFlowMgrDetailEgJoined_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 94),
    _ApFlowMgrDetailEgJoined_Type()
)
apFlowMgrDetailEgJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgJoined.setStatus("current")
_ApFlowMgrDetailEgContentExpected_Type = Integer32
_ApFlowMgrDetailEgContentExpected_Object = MibTableColumn
apFlowMgrDetailEgContentExpected = _ApFlowMgrDetailEgContentExpected_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 95),
    _ApFlowMgrDetailEgContentExpected_Type()
)
apFlowMgrDetailEgContentExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgContentExpected.setStatus("current")
_ApFlowMgrDetailEgJoinPending_Type = Integer32
_ApFlowMgrDetailEgJoinPending_Object = MibTableColumn
apFlowMgrDetailEgJoinPending = _ApFlowMgrDetailEgJoinPending_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 96),
    _ApFlowMgrDetailEgJoinPending_Type()
)
apFlowMgrDetailEgJoinPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgJoinPending.setStatus("current")
_ApFlowMgrDetailEgContentPending_Type = Integer32
_ApFlowMgrDetailEgContentPending_Object = MibTableColumn
apFlowMgrDetailEgContentPending = _ApFlowMgrDetailEgContentPending_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 97),
    _ApFlowMgrDetailEgContentPending_Type()
)
apFlowMgrDetailEgContentPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgContentPending.setStatus("current")
_ApFlowMgrDetailEgTCPSYNSent_Type = Integer32
_ApFlowMgrDetailEgTCPSYNSent_Object = MibTableColumn
apFlowMgrDetailEgTCPSYNSent = _ApFlowMgrDetailEgTCPSYNSent_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 98),
    _ApFlowMgrDetailEgTCPSYNSent_Type()
)
apFlowMgrDetailEgTCPSYNSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgTCPSYNSent.setStatus("current")
_ApFlowMgrDetailEgReversePending_Type = Integer32
_ApFlowMgrDetailEgReversePending_Object = MibTableColumn
apFlowMgrDetailEgReversePending = _ApFlowMgrDetailEgReversePending_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 99),
    _ApFlowMgrDetailEgReversePending_Type()
)
apFlowMgrDetailEgReversePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgReversePending.setStatus("current")
_ApFlowMgrDetailEgSFPFowrarded_Type = Integer32
_ApFlowMgrDetailEgSFPFowrarded_Object = MibTableColumn
apFlowMgrDetailEgSFPFowrarded = _ApFlowMgrDetailEgSFPFowrarded_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 100),
    _ApFlowMgrDetailEgSFPFowrarded_Type()
)
apFlowMgrDetailEgSFPFowrarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSFPFowrarded.setStatus("current")
_ApFlowMgrDetailEgInPortInflowCount_Type = Integer32
_ApFlowMgrDetailEgInPortInflowCount_Object = MibTableColumn
apFlowMgrDetailEgInPortInflowCount = _ApFlowMgrDetailEgInPortInflowCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 101),
    _ApFlowMgrDetailEgInPortInflowCount_Type()
)
apFlowMgrDetailEgInPortInflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgInPortInflowCount.setStatus("current")
_ApFlowMgrDetailEgDeleted_Type = Integer32
_ApFlowMgrDetailEgDeleted_Object = MibTableColumn
apFlowMgrDetailEgDeleted = _ApFlowMgrDetailEgDeleted_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 102),
    _ApFlowMgrDetailEgDeleted_Type()
)
apFlowMgrDetailEgDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgDeleted.setStatus("current")
_ApFlowMgrDetailEgSpoofed_Type = Integer32
_ApFlowMgrDetailEgSpoofed_Object = MibTableColumn
apFlowMgrDetailEgSpoofed = _ApFlowMgrDetailEgSpoofed_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 103),
    _ApFlowMgrDetailEgSpoofed_Type()
)
apFlowMgrDetailEgSpoofed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSpoofed.setStatus("current")
_ApFlowMgrDetailEgNATInUse_Type = Integer32
_ApFlowMgrDetailEgNATInUse_Object = MibTableColumn
apFlowMgrDetailEgNATInUse = _ApFlowMgrDetailEgNATInUse_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 104),
    _ApFlowMgrDetailEgNATInUse_Type()
)
apFlowMgrDetailEgNATInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgNATInUse.setStatus("current")
_ApFlowMgrDetailEgContentAware_Type = Integer32
_ApFlowMgrDetailEgContentAware_Object = MibTableColumn
apFlowMgrDetailEgContentAware = _ApFlowMgrDetailEgContentAware_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 105),
    _ApFlowMgrDetailEgContentAware_Type()
)
apFlowMgrDetailEgContentAware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgContentAware.setStatus("current")
_ApFlowMgrDetailEgSticky_Type = Integer32
_ApFlowMgrDetailEgSticky_Object = MibTableColumn
apFlowMgrDetailEgSticky = _ApFlowMgrDetailEgSticky_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 106),
    _ApFlowMgrDetailEgSticky_Type()
)
apFlowMgrDetailEgSticky.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSticky.setStatus("current")
_ApFlowMgrDetailEgBridged_Type = Integer32
_ApFlowMgrDetailEgBridged_Object = MibTableColumn
apFlowMgrDetailEgBridged = _ApFlowMgrDetailEgBridged_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 107),
    _ApFlowMgrDetailEgBridged_Type()
)
apFlowMgrDetailEgBridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgBridged.setStatus("current")
_ApFlowMgrDetailEgBuffersPending_Type = Integer32
_ApFlowMgrDetailEgBuffersPending_Object = MibTableColumn
apFlowMgrDetailEgBuffersPending = _ApFlowMgrDetailEgBuffersPending_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 108),
    _ApFlowMgrDetailEgBuffersPending_Type()
)
apFlowMgrDetailEgBuffersPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgBuffersPending.setStatus("current")
_ApFlowMgrDetailEgSYNDOSTimerActive_Type = Integer32
_ApFlowMgrDetailEgSYNDOSTimerActive_Object = MibTableColumn
apFlowMgrDetailEgSYNDOSTimerActive = _ApFlowMgrDetailEgSYNDOSTimerActive_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 109),
    _ApFlowMgrDetailEgSYNDOSTimerActive_Type()
)
apFlowMgrDetailEgSYNDOSTimerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSYNDOSTimerActive.setStatus("current")
_ApFlowMgrDetailEgOverflowMapped_Type = Integer32
_ApFlowMgrDetailEgOverflowMapped_Object = MibTableColumn
apFlowMgrDetailEgOverflowMapped = _ApFlowMgrDetailEgOverflowMapped_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 110),
    _ApFlowMgrDetailEgOverflowMapped_Type()
)
apFlowMgrDetailEgOverflowMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgOverflowMapped.setStatus("current")
_ApFlowMgrDetailEgRejected_Type = Integer32
_ApFlowMgrDetailEgRejected_Object = MibTableColumn
apFlowMgrDetailEgRejected = _ApFlowMgrDetailEgRejected_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 111),
    _ApFlowMgrDetailEgRejected_Type()
)
apFlowMgrDetailEgRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgRejected.setStatus("current")
_ApFlowMgrDetailEgTotalTCPFlows_Type = Integer32
_ApFlowMgrDetailEgTotalTCPFlows_Object = MibTableColumn
apFlowMgrDetailEgTotalTCPFlows = _ApFlowMgrDetailEgTotalTCPFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 112),
    _ApFlowMgrDetailEgTotalTCPFlows_Type()
)
apFlowMgrDetailEgTotalTCPFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgTotalTCPFlows.setStatus("current")
_ApFlowMgrDetailEgTotalUDPFlows_Type = Integer32
_ApFlowMgrDetailEgTotalUDPFlows_Object = MibTableColumn
apFlowMgrDetailEgTotalUDPFlows = _ApFlowMgrDetailEgTotalUDPFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 113),
    _ApFlowMgrDetailEgTotalUDPFlows_Type()
)
apFlowMgrDetailEgTotalUDPFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgTotalUDPFlows.setStatus("current")
_ApFlowMgrDetailEgHTTPSrcFlows_Type = Integer32
_ApFlowMgrDetailEgHTTPSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgHTTPSrcFlows = _ApFlowMgrDetailEgHTTPSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 114),
    _ApFlowMgrDetailEgHTTPSrcFlows_Type()
)
apFlowMgrDetailEgHTTPSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgHTTPSrcFlows.setStatus("current")
_ApFlowMgrDetailEgHTTPDstFlows_Type = Integer32
_ApFlowMgrDetailEgHTTPDstFlows_Object = MibTableColumn
apFlowMgrDetailEgHTTPDstFlows = _ApFlowMgrDetailEgHTTPDstFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 115),
    _ApFlowMgrDetailEgHTTPDstFlows_Type()
)
apFlowMgrDetailEgHTTPDstFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgHTTPDstFlows.setStatus("current")
_ApFlowMgrDetailEgFTPDataSrcFlows_Type = Integer32
_ApFlowMgrDetailEgFTPDataSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgFTPDataSrcFlows = _ApFlowMgrDetailEgFTPDataSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 116),
    _ApFlowMgrDetailEgFTPDataSrcFlows_Type()
)
apFlowMgrDetailEgFTPDataSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgFTPDataSrcFlows.setStatus("current")
_ApFlowMgrDetailEgFTPDataDestFlows_Type = Integer32
_ApFlowMgrDetailEgFTPDataDestFlows_Object = MibTableColumn
apFlowMgrDetailEgFTPDataDestFlows = _ApFlowMgrDetailEgFTPDataDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 117),
    _ApFlowMgrDetailEgFTPDataDestFlows_Type()
)
apFlowMgrDetailEgFTPDataDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgFTPDataDestFlows.setStatus("current")
_ApFlowMgrDetailEgFTPCtrlSrcFlows_Type = Integer32
_ApFlowMgrDetailEgFTPCtrlSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgFTPCtrlSrcFlows = _ApFlowMgrDetailEgFTPCtrlSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 118),
    _ApFlowMgrDetailEgFTPCtrlSrcFlows_Type()
)
apFlowMgrDetailEgFTPCtrlSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgFTPCtrlSrcFlows.setStatus("current")
_ApFlowMgrDetailEgFTPCtrlDestFlows_Type = Integer32
_ApFlowMgrDetailEgFTPCtrlDestFlows_Object = MibTableColumn
apFlowMgrDetailEgFTPCtrlDestFlows = _ApFlowMgrDetailEgFTPCtrlDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 119),
    _ApFlowMgrDetailEgFTPCtrlDestFlows_Type()
)
apFlowMgrDetailEgFTPCtrlDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgFTPCtrlDestFlows.setStatus("current")
_ApFlowMgrDetailEgSSHSrcFlows_Type = Integer32
_ApFlowMgrDetailEgSSHSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgSSHSrcFlows = _ApFlowMgrDetailEgSSHSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 120),
    _ApFlowMgrDetailEgSSHSrcFlows_Type()
)
apFlowMgrDetailEgSSHSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSSHSrcFlows.setStatus("current")
_ApFlowMgrDetailEgSSHDestFlows_Type = Integer32
_ApFlowMgrDetailEgSSHDestFlows_Object = MibTableColumn
apFlowMgrDetailEgSSHDestFlows = _ApFlowMgrDetailEgSSHDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 121),
    _ApFlowMgrDetailEgSSHDestFlows_Type()
)
apFlowMgrDetailEgSSHDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSSHDestFlows.setStatus("current")
_ApFlowMgrDetailEgTelnetSrcFlows_Type = Integer32
_ApFlowMgrDetailEgTelnetSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgTelnetSrcFlows = _ApFlowMgrDetailEgTelnetSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 122),
    _ApFlowMgrDetailEgTelnetSrcFlows_Type()
)
apFlowMgrDetailEgTelnetSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgTelnetSrcFlows.setStatus("current")
_ApFlowMgrDetailEgTelnetDestFlows_Type = Integer32
_ApFlowMgrDetailEgTelnetDestFlows_Object = MibTableColumn
apFlowMgrDetailEgTelnetDestFlows = _ApFlowMgrDetailEgTelnetDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 123),
    _ApFlowMgrDetailEgTelnetDestFlows_Type()
)
apFlowMgrDetailEgTelnetDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgTelnetDestFlows.setStatus("current")
_ApFlowMgrDetailEgRASrcFlows_Type = Integer32
_ApFlowMgrDetailEgRASrcFlows_Object = MibTableColumn
apFlowMgrDetailEgRASrcFlows = _ApFlowMgrDetailEgRASrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 124),
    _ApFlowMgrDetailEgRASrcFlows_Type()
)
apFlowMgrDetailEgRASrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgRASrcFlows.setStatus("current")
_ApFlowMgrDetailEgRADestFlows_Type = Integer32
_ApFlowMgrDetailEgRADestFlows_Object = MibTableColumn
apFlowMgrDetailEgRADestFlows = _ApFlowMgrDetailEgRADestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 125),
    _ApFlowMgrDetailEgRADestFlows_Type()
)
apFlowMgrDetailEgRADestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgRADestFlows.setStatus("current")
_ApFlowMgrDetailEgBGPSrcFlows_Type = Integer32
_ApFlowMgrDetailEgBGPSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgBGPSrcFlows = _ApFlowMgrDetailEgBGPSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 126),
    _ApFlowMgrDetailEgBGPSrcFlows_Type()
)
apFlowMgrDetailEgBGPSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgBGPSrcFlows.setStatus("current")
_ApFlowMgrDetailEgBGPDestFlows_Type = Integer32
_ApFlowMgrDetailEgBGPDestFlows_Object = MibTableColumn
apFlowMgrDetailEgBGPDestFlows = _ApFlowMgrDetailEgBGPDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 127),
    _ApFlowMgrDetailEgBGPDestFlows_Type()
)
apFlowMgrDetailEgBGPDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgBGPDestFlows.setStatus("current")
_ApFlowMgrDetailEgSMTPSrcFlows_Type = Integer32
_ApFlowMgrDetailEgSMTPSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgSMTPSrcFlows = _ApFlowMgrDetailEgSMTPSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 128),
    _ApFlowMgrDetailEgSMTPSrcFlows_Type()
)
apFlowMgrDetailEgSMTPSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSMTPSrcFlows.setStatus("current")
_ApFlowMgrDetailEgSMTPDestFlows_Type = Integer32
_ApFlowMgrDetailEgSMTPDestFlows_Object = MibTableColumn
apFlowMgrDetailEgSMTPDestFlows = _ApFlowMgrDetailEgSMTPDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 129),
    _ApFlowMgrDetailEgSMTPDestFlows_Type()
)
apFlowMgrDetailEgSMTPDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSMTPDestFlows.setStatus("current")
_ApFlowMgrDetailEgPOP3SrcFlows_Type = Integer32
_ApFlowMgrDetailEgPOP3SrcFlows_Object = MibTableColumn
apFlowMgrDetailEgPOP3SrcFlows = _ApFlowMgrDetailEgPOP3SrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 130),
    _ApFlowMgrDetailEgPOP3SrcFlows_Type()
)
apFlowMgrDetailEgPOP3SrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgPOP3SrcFlows.setStatus("current")
_ApFlowMgrDetailEgPOP3DestFlows_Type = Integer32
_ApFlowMgrDetailEgPOP3DestFlows_Object = MibTableColumn
apFlowMgrDetailEgPOP3DestFlows = _ApFlowMgrDetailEgPOP3DestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 131),
    _ApFlowMgrDetailEgPOP3DestFlows_Type()
)
apFlowMgrDetailEgPOP3DestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgPOP3DestFlows.setStatus("current")
_ApFlowMgrDetailEgHTTPSSrcFlows_Type = Integer32
_ApFlowMgrDetailEgHTTPSSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgHTTPSSrcFlows = _ApFlowMgrDetailEgHTTPSSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 132),
    _ApFlowMgrDetailEgHTTPSSrcFlows_Type()
)
apFlowMgrDetailEgHTTPSSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgHTTPSSrcFlows.setStatus("current")
_ApFlowMgrDetailEgHTTPSDestFlows_Type = Integer32
_ApFlowMgrDetailEgHTTPSDestFlows_Object = MibTableColumn
apFlowMgrDetailEgHTTPSDestFlows = _ApFlowMgrDetailEgHTTPSDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 133),
    _ApFlowMgrDetailEgHTTPSDestFlows_Type()
)
apFlowMgrDetailEgHTTPSDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgHTTPSDestFlows.setStatus("current")
_ApFlowMgrDetailEgNNTPSrcFlows_Type = Integer32
_ApFlowMgrDetailEgNNTPSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgNNTPSrcFlows = _ApFlowMgrDetailEgNNTPSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 134),
    _ApFlowMgrDetailEgNNTPSrcFlows_Type()
)
apFlowMgrDetailEgNNTPSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgNNTPSrcFlows.setStatus("current")
_ApFlowMgrDetailEgNNTPDestFlows_Type = Integer32
_ApFlowMgrDetailEgNNTPDestFlows_Object = MibTableColumn
apFlowMgrDetailEgNNTPDestFlows = _ApFlowMgrDetailEgNNTPDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 135),
    _ApFlowMgrDetailEgNNTPDestFlows_Type()
)
apFlowMgrDetailEgNNTPDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgNNTPDestFlows.setStatus("current")
_ApFlowMgrDetailEgSOCKSSrcFlows_Type = Integer32
_ApFlowMgrDetailEgSOCKSSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgSOCKSSrcFlows = _ApFlowMgrDetailEgSOCKSSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 136),
    _ApFlowMgrDetailEgSOCKSSrcFlows_Type()
)
apFlowMgrDetailEgSOCKSSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSOCKSSrcFlows.setStatus("current")
_ApFlowMgrDetailEgSOCKSDestFlows_Type = Integer32
_ApFlowMgrDetailEgSOCKSDestFlows_Object = MibTableColumn
apFlowMgrDetailEgSOCKSDestFlows = _ApFlowMgrDetailEgSOCKSDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 137),
    _ApFlowMgrDetailEgSOCKSDestFlows_Type()
)
apFlowMgrDetailEgSOCKSDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSOCKSDestFlows.setStatus("current")
_ApFlowMgrDetailEgPortLT23SrcFlows_Type = Integer32
_ApFlowMgrDetailEgPortLT23SrcFlows_Object = MibTableColumn
apFlowMgrDetailEgPortLT23SrcFlows = _ApFlowMgrDetailEgPortLT23SrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 138),
    _ApFlowMgrDetailEgPortLT23SrcFlows_Type()
)
apFlowMgrDetailEgPortLT23SrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgPortLT23SrcFlows.setStatus("current")
_ApFlowMgrDetailEgPortLT23DestFlows_Type = Integer32
_ApFlowMgrDetailEgPortLT23DestFlows_Object = MibTableColumn
apFlowMgrDetailEgPortLT23DestFlows = _ApFlowMgrDetailEgPortLT23DestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 139),
    _ApFlowMgrDetailEgPortLT23DestFlows_Type()
)
apFlowMgrDetailEgPortLT23DestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgPortLT23DestFlows.setStatus("current")
_ApFlowMgrDetailEgPortGT1024SrcFlows_Type = Integer32
_ApFlowMgrDetailEgPortGT1024SrcFlows_Object = MibTableColumn
apFlowMgrDetailEgPortGT1024SrcFlows = _ApFlowMgrDetailEgPortGT1024SrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 140),
    _ApFlowMgrDetailEgPortGT1024SrcFlows_Type()
)
apFlowMgrDetailEgPortGT1024SrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgPortGT1024SrcFlows.setStatus("current")
_ApFlowMgrDetailEgPortGT1024DestFlows_Type = Integer32
_ApFlowMgrDetailEgPortGT1024DestFlows_Object = MibTableColumn
apFlowMgrDetailEgPortGT1024DestFlows = _ApFlowMgrDetailEgPortGT1024DestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 141),
    _ApFlowMgrDetailEgPortGT1024DestFlows_Type()
)
apFlowMgrDetailEgPortGT1024DestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgPortGT1024DestFlows.setStatus("current")
_ApFlowMgrDetailEgTimeSrcFlows_Type = Integer32
_ApFlowMgrDetailEgTimeSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgTimeSrcFlows = _ApFlowMgrDetailEgTimeSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 142),
    _ApFlowMgrDetailEgTimeSrcFlows_Type()
)
apFlowMgrDetailEgTimeSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgTimeSrcFlows.setStatus("current")
_ApFlowMgrDetailEgTimeDestSrcFlows_Type = Integer32
_ApFlowMgrDetailEgTimeDestSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgTimeDestSrcFlows = _ApFlowMgrDetailEgTimeDestSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 143),
    _ApFlowMgrDetailEgTimeDestSrcFlows_Type()
)
apFlowMgrDetailEgTimeDestSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgTimeDestSrcFlows.setStatus("current")
_ApFlowMgrDetailEgDNSSrcFlows_Type = Integer32
_ApFlowMgrDetailEgDNSSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgDNSSrcFlows = _ApFlowMgrDetailEgDNSSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 144),
    _ApFlowMgrDetailEgDNSSrcFlows_Type()
)
apFlowMgrDetailEgDNSSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgDNSSrcFlows.setStatus("current")
_ApFlowMgrDetailEgDNSDestFlows_Type = Integer32
_ApFlowMgrDetailEgDNSDestFlows_Object = MibTableColumn
apFlowMgrDetailEgDNSDestFlows = _ApFlowMgrDetailEgDNSDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 145),
    _ApFlowMgrDetailEgDNSDestFlows_Type()
)
apFlowMgrDetailEgDNSDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgDNSDestFlows.setStatus("current")
_ApFlowMgrDetailEgSNMPSrcFlows_Type = Integer32
_ApFlowMgrDetailEgSNMPSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgSNMPSrcFlows = _ApFlowMgrDetailEgSNMPSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 146),
    _ApFlowMgrDetailEgSNMPSrcFlows_Type()
)
apFlowMgrDetailEgSNMPSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSNMPSrcFlows.setStatus("current")
_ApFlowMgrDetailEgSNMPDestFlows_Type = Integer32
_ApFlowMgrDetailEgSNMPDestFlows_Object = MibTableColumn
apFlowMgrDetailEgSNMPDestFlows = _ApFlowMgrDetailEgSNMPDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 147),
    _ApFlowMgrDetailEgSNMPDestFlows_Type()
)
apFlowMgrDetailEgSNMPDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSNMPDestFlows.setStatus("current")
_ApFlowMgrDetailEgSNMPTrapSrcFlows_Type = Integer32
_ApFlowMgrDetailEgSNMPTrapSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgSNMPTrapSrcFlows = _ApFlowMgrDetailEgSNMPTrapSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 148),
    _ApFlowMgrDetailEgSNMPTrapSrcFlows_Type()
)
apFlowMgrDetailEgSNMPTrapSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSNMPTrapSrcFlows.setStatus("current")
_ApFlowMgrDetailEgSNMPTrapDestFlows_Type = Integer32
_ApFlowMgrDetailEgSNMPTrapDestFlows_Object = MibTableColumn
apFlowMgrDetailEgSNMPTrapDestFlows = _ApFlowMgrDetailEgSNMPTrapDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 149),
    _ApFlowMgrDetailEgSNMPTrapDestFlows_Type()
)
apFlowMgrDetailEgSNMPTrapDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgSNMPTrapDestFlows.setStatus("current")
_ApFlowMgrDetailEgNFSSrcFlows_Type = Integer32
_ApFlowMgrDetailEgNFSSrcFlows_Object = MibTableColumn
apFlowMgrDetailEgNFSSrcFlows = _ApFlowMgrDetailEgNFSSrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 150),
    _ApFlowMgrDetailEgNFSSrcFlows_Type()
)
apFlowMgrDetailEgNFSSrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgNFSSrcFlows.setStatus("current")
_ApFlowMgrDetailEgNFSDestFlows_Type = Integer32
_ApFlowMgrDetailEgNFSDestFlows_Object = MibTableColumn
apFlowMgrDetailEgNFSDestFlows = _ApFlowMgrDetailEgNFSDestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 151),
    _ApFlowMgrDetailEgNFSDestFlows_Type()
)
apFlowMgrDetailEgNFSDestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgNFSDestFlows.setStatus("current")
_ApFlowMgrDetailEgUDPGT1024SrcFlows_Type = Integer32
_ApFlowMgrDetailEgUDPGT1024SrcFlows_Object = MibTableColumn
apFlowMgrDetailEgUDPGT1024SrcFlows = _ApFlowMgrDetailEgUDPGT1024SrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 152),
    _ApFlowMgrDetailEgUDPGT1024SrcFlows_Type()
)
apFlowMgrDetailEgUDPGT1024SrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgUDPGT1024SrcFlows.setStatus("current")
_ApFlowMgrDetailEgUDPGT1024DestFlows_Type = Integer32
_ApFlowMgrDetailEgUDPGT1024DestFlows_Object = MibTableColumn
apFlowMgrDetailEgUDPGT1024DestFlows = _ApFlowMgrDetailEgUDPGT1024DestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 153),
    _ApFlowMgrDetailEgUDPGT1024DestFlows_Type()
)
apFlowMgrDetailEgUDPGT1024DestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgUDPGT1024DestFlows.setStatus("current")
_ApFlowMgrDetailEgUDPLT1024SrcFlows_Type = Integer32
_ApFlowMgrDetailEgUDPLT1024SrcFlows_Object = MibTableColumn
apFlowMgrDetailEgUDPLT1024SrcFlows = _ApFlowMgrDetailEgUDPLT1024SrcFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 154),
    _ApFlowMgrDetailEgUDPLT1024SrcFlows_Type()
)
apFlowMgrDetailEgUDPLT1024SrcFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgUDPLT1024SrcFlows.setStatus("current")
_ApFlowMgrDetailEgUDPLT1024DestFlows_Type = Integer32
_ApFlowMgrDetailEgUDPLT1024DestFlows_Object = MibTableColumn
apFlowMgrDetailEgUDPLT1024DestFlows = _ApFlowMgrDetailEgUDPLT1024DestFlows_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 155),
    _ApFlowMgrDetailEgUDPLT1024DestFlows_Type()
)
apFlowMgrDetailEgUDPLT1024DestFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailEgUDPLT1024DestFlows.setStatus("current")
_ApFlowMgrDetailOutFrames_Type = Integer32
_ApFlowMgrDetailOutFrames_Object = MibTableColumn
apFlowMgrDetailOutFrames = _ApFlowMgrDetailOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 17, 1, 156),
    _ApFlowMgrDetailOutFrames_Type()
)
apFlowMgrDetailOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrDetailOutFrames.setStatus("current")
_ApFlowMgrExtDosTotalAttacks_Type = Integer32
_ApFlowMgrExtDosTotalAttacks_Object = MibScalar
apFlowMgrExtDosTotalAttacks = _ApFlowMgrExtDosTotalAttacks_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 18),
    _ApFlowMgrExtDosTotalAttacks_Type()
)
apFlowMgrExtDosTotalAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDosTotalAttacks.setStatus("current")
_ApFlowMgrExtDosTotalSynAttacks_Type = Integer32
_ApFlowMgrExtDosTotalSynAttacks_Object = MibScalar
apFlowMgrExtDosTotalSynAttacks = _ApFlowMgrExtDosTotalSynAttacks_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 19),
    _ApFlowMgrExtDosTotalSynAttacks_Type()
)
apFlowMgrExtDosTotalSynAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDosTotalSynAttacks.setStatus("current")
_ApFlowMgrExtDosTotalLandAttacks_Type = Integer32
_ApFlowMgrExtDosTotalLandAttacks_Object = MibScalar
apFlowMgrExtDosTotalLandAttacks = _ApFlowMgrExtDosTotalLandAttacks_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 20),
    _ApFlowMgrExtDosTotalLandAttacks_Type()
)
apFlowMgrExtDosTotalLandAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDosTotalLandAttacks.setStatus("current")
_ApFlowMgrExtDosTotalZeroPortAttacks_Type = Integer32
_ApFlowMgrExtDosTotalZeroPortAttacks_Object = MibScalar
apFlowMgrExtDosTotalZeroPortAttacks = _ApFlowMgrExtDosTotalZeroPortAttacks_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 21),
    _ApFlowMgrExtDosTotalZeroPortAttacks_Type()
)
apFlowMgrExtDosTotalZeroPortAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDosTotalZeroPortAttacks.setStatus("current")
_ApFlowMgrExtDosTotalIllegalSourceAttacks_Type = Integer32
_ApFlowMgrExtDosTotalIllegalSourceAttacks_Object = MibScalar
apFlowMgrExtDosTotalIllegalSourceAttacks = _ApFlowMgrExtDosTotalIllegalSourceAttacks_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 22),
    _ApFlowMgrExtDosTotalIllegalSourceAttacks_Type()
)
apFlowMgrExtDosTotalIllegalSourceAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDosTotalIllegalSourceAttacks.setStatus("current")
_ApFlowMgrExtDosTotalIllegalDestinationAttacks_Type = Integer32
_ApFlowMgrExtDosTotalIllegalDestinationAttacks_Object = MibScalar
apFlowMgrExtDosTotalIllegalDestinationAttacks = _ApFlowMgrExtDosTotalIllegalDestinationAttacks_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 23),
    _ApFlowMgrExtDosTotalIllegalDestinationAttacks_Type()
)
apFlowMgrExtDosTotalIllegalDestinationAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDosTotalIllegalDestinationAttacks.setStatus("current")
_ApFlowMgrExtDosTotalPingOfDeathAttacks_Type = Integer32
_ApFlowMgrExtDosTotalPingOfDeathAttacks_Object = MibScalar
apFlowMgrExtDosTotalPingOfDeathAttacks = _ApFlowMgrExtDosTotalPingOfDeathAttacks_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 24),
    _ApFlowMgrExtDosTotalPingOfDeathAttacks_Type()
)
apFlowMgrExtDosTotalPingOfDeathAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDosTotalPingOfDeathAttacks.setStatus("obsolete")
_ApFlowMgrExtDosTotalSmurfAttacks_Type = Integer32
_ApFlowMgrExtDosTotalSmurfAttacks_Object = MibScalar
apFlowMgrExtDosTotalSmurfAttacks = _ApFlowMgrExtDosTotalSmurfAttacks_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 25),
    _ApFlowMgrExtDosTotalSmurfAttacks_Type()
)
apFlowMgrExtDosTotalSmurfAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDosTotalSmurfAttacks.setStatus("current")
_ApFlowMgrExtDosLastAttack_Type = DisplayString
_ApFlowMgrExtDosLastAttack_Object = MibScalar
apFlowMgrExtDosLastAttack = _ApFlowMgrExtDosLastAttack_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 26),
    _ApFlowMgrExtDosLastAttack_Type()
)
apFlowMgrExtDosLastAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDosLastAttack.setStatus("current")
_ApFlowMgrExtDosFirstAttack_Type = DisplayString
_ApFlowMgrExtDosFirstAttack_Object = MibScalar
apFlowMgrExtDosFirstAttack = _ApFlowMgrExtDosFirstAttack_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 27),
    _ApFlowMgrExtDosFirstAttack_Type()
)
apFlowMgrExtDosFirstAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDosFirstAttack.setStatus("current")
_ApFlowMgrExtDOSAttackTable_Object = MibTable
apFlowMgrExtDOSAttackTable = _ApFlowMgrExtDOSAttackTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 28)
)
if mibBuilder.loadTexts:
    apFlowMgrExtDOSAttackTable.setStatus("current")
_ApFlowMgrExtDOSAttackEntry_Object = MibTableRow
apFlowMgrExtDOSAttackEntry = _ApFlowMgrExtDOSAttackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 28, 1)
)
apFlowMgrExtDOSAttackEntry.setIndexNames(
    (0, "FLOWMGREXT-MIB", "apFlowMgrExtDOSAttackIndex"),
)
if mibBuilder.loadTexts:
    apFlowMgrExtDOSAttackEntry.setStatus("current")
_ApFlowMgrExtDOSAttackIndex_Type = Integer32
_ApFlowMgrExtDOSAttackIndex_Object = MibTableColumn
apFlowMgrExtDOSAttackIndex = _ApFlowMgrExtDOSAttackIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 28, 1, 1),
    _ApFlowMgrExtDOSAttackIndex_Type()
)
apFlowMgrExtDOSAttackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDOSAttackIndex.setStatus("current")
_ApFlowMgrExtDOSAttackSrcAddress_Type = IpAddress
_ApFlowMgrExtDOSAttackSrcAddress_Object = MibTableColumn
apFlowMgrExtDOSAttackSrcAddress = _ApFlowMgrExtDOSAttackSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 28, 1, 2),
    _ApFlowMgrExtDOSAttackSrcAddress_Type()
)
apFlowMgrExtDOSAttackSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDOSAttackSrcAddress.setStatus("current")
_ApFlowMgrExtDOSAttackDestAddress_Type = IpAddress
_ApFlowMgrExtDOSAttackDestAddress_Object = MibTableColumn
apFlowMgrExtDOSAttackDestAddress = _ApFlowMgrExtDOSAttackDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 28, 1, 3),
    _ApFlowMgrExtDOSAttackDestAddress_Type()
)
apFlowMgrExtDOSAttackDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDOSAttackDestAddress.setStatus("current")
_ApFlowMgrExtDOSAttackFirstEvent_Type = DisplayString
_ApFlowMgrExtDOSAttackFirstEvent_Object = MibTableColumn
apFlowMgrExtDOSAttackFirstEvent = _ApFlowMgrExtDOSAttackFirstEvent_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 28, 1, 4),
    _ApFlowMgrExtDOSAttackFirstEvent_Type()
)
apFlowMgrExtDOSAttackFirstEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDOSAttackFirstEvent.setStatus("current")
_ApFlowMgrExtDOSAttackLastEvent_Type = DisplayString
_ApFlowMgrExtDOSAttackLastEvent_Object = MibTableColumn
apFlowMgrExtDOSAttackLastEvent = _ApFlowMgrExtDOSAttackLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 28, 1, 5),
    _ApFlowMgrExtDOSAttackLastEvent_Type()
)
apFlowMgrExtDOSAttackLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDOSAttackLastEvent.setStatus("current")
_ApFlowMgrExtDOSAttackEventCount_Type = Integer32
_ApFlowMgrExtDOSAttackEventCount_Object = MibTableColumn
apFlowMgrExtDOSAttackEventCount = _ApFlowMgrExtDOSAttackEventCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 28, 1, 6),
    _ApFlowMgrExtDOSAttackEventCount_Type()
)
apFlowMgrExtDOSAttackEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDOSAttackEventCount.setStatus("current")


class _ApFlowMgrExtDOSAttackEventType_Type(Integer32):
    """Custom type apFlowMgrExtDOSAttackEventType based on Integer32"""
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
        *(("illegaldst", 7),
          ("illegalsrc", 4),
          ("land", 2),
          ("pingofdeath", 5),
          ("smurf", 6),
          ("syn", 1),
          ("zeroport", 3))
    )


_ApFlowMgrExtDOSAttackEventType_Type.__name__ = "Integer32"
_ApFlowMgrExtDOSAttackEventType_Object = MibTableColumn
apFlowMgrExtDOSAttackEventType = _ApFlowMgrExtDOSAttackEventType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 28, 1, 7),
    _ApFlowMgrExtDOSAttackEventType_Type()
)
apFlowMgrExtDOSAttackEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDOSAttackEventType.setStatus("current")


class _ApFlowMgrExtDOSAttackEventString_Type(DisplayString):
    """Custom type apFlowMgrExtDOSAttackEventString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApFlowMgrExtDOSAttackEventString_Type.__name__ = "DisplayString"
_ApFlowMgrExtDOSAttackEventString_Object = MibTableColumn
apFlowMgrExtDOSAttackEventString = _ApFlowMgrExtDOSAttackEventString_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 28, 1, 8),
    _ApFlowMgrExtDOSAttackEventString_Type()
)
apFlowMgrExtDOSAttackEventString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFlowMgrExtDOSAttackEventString.setStatus("current")

# Managed Objects groups


# Notification objects

apFlowMgrExtDosSynTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 0, 1)
)
if mibBuilder.loadTexts:
    apFlowMgrExtDosSynTrap.setStatus(
        ""
    )

apFlowMgrExtDosLandTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 0, 2)
)
if mibBuilder.loadTexts:
    apFlowMgrExtDosLandTrap.setStatus(
        ""
    )

apFlowMgrExtDosIllegalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 0, 3)
)
if mibBuilder.loadTexts:
    apFlowMgrExtDosIllegalTrap.setStatus(
        ""
    )

apFlowMgrExtDosPingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 0, 4)
)
if mibBuilder.loadTexts:
    apFlowMgrExtDosPingTrap.setStatus(
        ""
    )

apFlowMgrExtDosSmurfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2467, 1, 36, 0, 5)
)
if mibBuilder.loadTexts:
    apFlowMgrExtDosSmurfTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FLOWMGREXT-MIB",
    **{"apFlowMgrExtDosSynTrap": apFlowMgrExtDosSynTrap,
       "apFlowMgrExtDosLandTrap": apFlowMgrExtDosLandTrap,
       "apFlowMgrExtDosIllegalTrap": apFlowMgrExtDosIllegalTrap,
       "apFlowMgrExtDosPingTrap": apFlowMgrExtDosPingTrap,
       "apFlowMgrExtDosSmurfTrap": apFlowMgrExtDosSmurfTrap,
       "flowMgrExtMib": flowMgrExtMib,
       "apFlowMgrExtFlowTraceOptions": apFlowMgrExtFlowTraceOptions,
       "apFlowMgrExtFlowTraceState": apFlowMgrExtFlowTraceState,
       "apFlowMgrExtFlowTraceFilename": apFlowMgrExtFlowTraceFilename,
       "apFlowMgrExtFlowTraceMaxFileSize": apFlowMgrExtFlowTraceMaxFileSize,
       "apFlowMgrExtFlowTraceDuration": apFlowMgrExtFlowTraceDuration,
       "apFlowMgrExtPermanentPort1": apFlowMgrExtPermanentPort1,
       "apFlowMgrExtPermanentPort2": apFlowMgrExtPermanentPort2,
       "apFlowMgrExtPermanentPort3": apFlowMgrExtPermanentPort3,
       "apFlowMgrExtPermanentPort4": apFlowMgrExtPermanentPort4,
       "apFlowMgrExtReserveCleanTimer": apFlowMgrExtReserveCleanTimer,
       "apFlowMgrExtPortIdleTable": apFlowMgrExtPortIdleTable,
       "apFlowMgrExtPortIdleEntry": apFlowMgrExtPortIdleEntry,
       "apFlowMgrExtPortIdle": apFlowMgrExtPortIdle,
       "apFlowMgrExtPortIdleValue": apFlowMgrExtPortIdleValue,
       "apFlowMgrExtPortLowWaterFCB": apFlowMgrExtPortLowWaterFCB,
       "apFlowMgrExtIdleTimer": apFlowMgrExtIdleTimer,
       "apFlowMgrStatIfTable": apFlowMgrStatIfTable,
       "apFlowMgrStatIfEntry": apFlowMgrStatIfEntry,
       "apFlowMgrStatIfIndex": apFlowMgrStatIfIndex,
       "apFlowMgrStatIfVlanID": apFlowMgrStatIfVlanID,
       "apFlowMgrStatIfUDPTotal": apFlowMgrStatIfUDPTotal,
       "apFlowMgrStatIfUDPCur": apFlowMgrStatIfUDPCur,
       "apFlowMgrStatIfUDPHigh": apFlowMgrStatIfUDPHigh,
       "apFlowMgrStatIfUDPAvg": apFlowMgrStatIfUDPAvg,
       "apFlowMgrStatIfTCPTotal": apFlowMgrStatIfTCPTotal,
       "apFlowMgrStatIfTCPCur": apFlowMgrStatIfTCPCur,
       "apFlowMgrStatIfTCPHigh": apFlowMgrStatIfTCPHigh,
       "apFlowMgrStatIfTCPAvg": apFlowMgrStatIfTCPAvg,
       "apFlowMgrStatIfCurrentActiveTCP": apFlowMgrStatIfCurrentActiveTCP,
       "apFlowMgrStatIfCurrentActiveUDP": apFlowMgrStatIfCurrentActiveUDP,
       "apFlowMgrStatIfAccountingReportsRx": apFlowMgrStatIfAccountingReportsRx,
       "apFlowMgrStatIfResets": apFlowMgrStatIfResets,
       "apFlowMgrStatIfFcbCount": apFlowMgrStatIfFcbCount,
       "apFlowMgrStatSSTable": apFlowMgrStatSSTable,
       "apFlowMgrStatSSEntry": apFlowMgrStatSSEntry,
       "apFlowMgrStatSSSlot": apFlowMgrStatSSSlot,
       "apFlowMgrStatSSSubSlot": apFlowMgrStatSSSubSlot,
       "apFlowMgrStatSSUDPTotal": apFlowMgrStatSSUDPTotal,
       "apFlowMgrStatSSUDPCur": apFlowMgrStatSSUDPCur,
       "apFlowMgrStatSSUDPHigh": apFlowMgrStatSSUDPHigh,
       "apFlowMgrStatSSUDPAvg": apFlowMgrStatSSUDPAvg,
       "apFlowMgrStatSSTCPTotal": apFlowMgrStatSSTCPTotal,
       "apFlowMgrStatSSTCPCur": apFlowMgrStatSSTCPCur,
       "apFlowMgrStatSSTCPHigh": apFlowMgrStatSSTCPHigh,
       "apFlowMgrStatSSTCPAvg": apFlowMgrStatSSTCPAvg,
       "apFlowMgrStatSSCurrentActiveTCP": apFlowMgrStatSSCurrentActiveTCP,
       "apFlowMgrStatSSCurrentActiveUDP": apFlowMgrStatSSCurrentActiveUDP,
       "apFlowMgrStatSSAccountingReportsRx": apFlowMgrStatSSAccountingReportsRx,
       "apFlowMgrStatSSResets": apFlowMgrStatSSResets,
       "apFlowMgrStatSSFcbCount": apFlowMgrStatSSFcbCount,
       "apFlowMgrPortTable": apFlowMgrPortTable,
       "apFlowMgrPortEntry": apFlowMgrPortEntry,
       "apFlowMgrPortIfIndex": apFlowMgrPortIfIndex,
       "apFlowMgrPortSeqBytes": apFlowMgrPortSeqBytes,
       "apFlowMgrPortInBytes": apFlowMgrPortInBytes,
       "apFlowMgrPortOutBytes": apFlowMgrPortOutBytes,
       "apFlowMgrPortInFrames": apFlowMgrPortInFrames,
       "apFlowMgrPortOutFrames": apFlowMgrPortOutFrames,
       "apFlowMgrPortTotalInFlows": apFlowMgrPortTotalInFlows,
       "apFlowMgrPortTotalOutFlows": apFlowMgrPortTotalOutFlows,
       "apFlowMgrPortTotalAcctFlows": apFlowMgrPortTotalAcctFlows,
       "apFlowMgrPortCurrTCPFlows": apFlowMgrPortCurrTCPFlows,
       "apFlowMgrPortCurrUDPFlows": apFlowMgrPortCurrUDPFlows,
       "apFlowMgrPortCurrInFlows": apFlowMgrPortCurrInFlows,
       "apFlowMgrPortCurrOutFlows": apFlowMgrPortCurrOutFlows,
       "apFlowMgrPortResetCount": apFlowMgrPortResetCount,
       "apFlowMgrPortMTU": apFlowMgrPortMTU,
       "apFlowMgrPortWccAccepted": apFlowMgrPortWccAccepted,
       "apFlowMgrPortWccAcceptedSticky": apFlowMgrPortWccAcceptedSticky,
       "apFlowMgrPortWccAcceptedBridge": apFlowMgrPortWccAcceptedBridge,
       "apFlowMgrPortWccAcceptedSfpFwd": apFlowMgrPortWccAcceptedSfpFwd,
       "apFlowMgrPortWccAcceptedSfp": apFlowMgrPortWccAcceptedSfp,
       "apFlowMgrPortWccForwardSfp": apFlowMgrPortWccForwardSfp,
       "apFlowMgrPortWccForward": apFlowMgrPortWccForward,
       "apFlowMgrPortWccLocal": apFlowMgrPortWccLocal,
       "apFlowMgrPortWccTCPSpoof": apFlowMgrPortWccTCPSpoof,
       "apFlowMgrPortWccArpPending": apFlowMgrPortWccArpPending,
       "apFlowMgrPortWccRedirect": apFlowMgrPortWccRedirect,
       "apFlowMgrPortWccRedirectSticky": apFlowMgrPortWccRedirectSticky,
       "apFlowMgrPortWccNoChange": apFlowMgrPortWccNoChange,
       "apFlowMgrPortWccRouteNotFound": apFlowMgrPortWccRouteNotFound,
       "apFlowMgrPortWccRtLookupError": apFlowMgrPortWccRtLookupError,
       "apFlowMgrPortWccDiscard": apFlowMgrPortWccDiscard,
       "apFlowMgrPortWccRejected": apFlowMgrPortWccRejected,
       "apFlowMgrPortWccRejectedSfp": apFlowMgrPortWccRejectedSfp,
       "apFlowMgrPortTotalAckDelete": apFlowMgrPortTotalAckDelete,
       "apFlowMgrPortPortAckDelete": apFlowMgrPortPortAckDelete,
       "apFlowMgrPortMidSpoofRejects": apFlowMgrPortMidSpoofRejects,
       "apFlowMgrPortMidNATReject": apFlowMgrPortMidNATReject,
       "apFlowMgrPortMidStickyReject": apFlowMgrPortMidStickyReject,
       "apFlowMgrPortSynExceedDelete": apFlowMgrPortSynExceedDelete,
       "apFlowMgrPortInvalidIP": apFlowMgrPortInvalidIP,
       "apFlowMgrPortBufferShortage": apFlowMgrPortBufferShortage,
       "apFlowMgrPortMovedAcctReports": apFlowMgrPortMovedAcctReports,
       "apFlowMgrPortUknownQueries": apFlowMgrPortUknownQueries,
       "apFlowMgrPortMappedLeftovers": apFlowMgrPortMappedLeftovers,
       "apFlowMgrPortUnmappedLeftovers": apFlowMgrPortUnmappedLeftovers,
       "apFlowMgrPortRemappedIngress": apFlowMgrPortRemappedIngress,
       "apFlowMgrPortFlowsUnavailable": apFlowMgrPortFlowsUnavailable,
       "apFlowMgrPortTCPCsumErrors": apFlowMgrPortTCPCsumErrors,
       "apFlowMgrPortOverflowMaps": apFlowMgrPortOverflowMaps,
       "apFlowMgrPortRouteChangeEvents": apFlowMgrPortRouteChangeEvents,
       "apFlowMgrPortRouteChangeFlows": apFlowMgrPortRouteChangeFlows,
       "apFlowMgrPortRouteChangeRemaps": apFlowMgrPortRouteChangeRemaps,
       "apFlowMgrPortOrphanMappings": apFlowMgrPortOrphanMappings,
       "apFlowMgrDetailTable": apFlowMgrDetailTable,
       "apFlowMgrDetailEntry": apFlowMgrDetailEntry,
       "apFlowMgrDetailIfIndex": apFlowMgrDetailIfIndex,
       "apFlowMgrDetailSeqBytes": apFlowMgrDetailSeqBytes,
       "apFlowMgrDetailFlags": apFlowMgrDetailFlags,
       "apFlowMgrDetailPoolFlows": apFlowMgrDetailPoolFlows,
       "apFlowMgrDetailInBytes": apFlowMgrDetailInBytes,
       "apFlowMgrDetailOutBytes": apFlowMgrDetailOutBytes,
       "apFlowMgrDetailInFrames": apFlowMgrDetailInFrames,
       "apFlowMgrDetailTotalInFlows": apFlowMgrDetailTotalInFlows,
       "apFlowMgrDetailTotalOutFlows": apFlowMgrDetailTotalOutFlows,
       "apFlowMgrDetailTotalAcctFlows": apFlowMgrDetailTotalAcctFlows,
       "apFlowMgrDetailResetCount": apFlowMgrDetailResetCount,
       "apFlowMgrDetailCurTCPFlows": apFlowMgrDetailCurTCPFlows,
       "apFlowMgrDetailCurUDPFlows": apFlowMgrDetailCurUDPFlows,
       "apFlowMgrDetailCurInFlows": apFlowMgrDetailCurInFlows,
       "apFlowMgrDetailCurOutFlows": apFlowMgrDetailCurOutFlows,
       "apFlowMgrDetailFPFlowCount": apFlowMgrDetailFPFlowCount,
       "apFlowMgrDetailTotalInFlowMap": apFlowMgrDetailTotalInFlowMap,
       "apFlowMgrDetailInMappedOnlyPrimary": apFlowMgrDetailInMappedOnlyPrimary,
       "apFlowMgrDetailInMappedOnlyPrevious": apFlowMgrDetailInMappedOnlyPrevious,
       "apFlowMgrDetailInMappedBothPrimary": apFlowMgrDetailInMappedBothPrimary,
       "apFlowMgrDetailInMappedBothPrevious": apFlowMgrDetailInMappedBothPrevious,
       "apFlowMgrDetailInNoFPMappings": apFlowMgrDetailInNoFPMappings,
       "apFlowMgrDetailInIngressQueueLen": apFlowMgrDetailInIngressQueueLen,
       "apFlowMgrDetailInOrphanFCBFlows": apFlowMgrDetailInOrphanFCBFlows,
       "apFlowMgrDetailInTotalOrphanFCB": apFlowMgrDetailInTotalOrphanFCB,
       "apFlowMgrDetailInTCPPermPort": apFlowMgrDetailInTCPPermPort,
       "apFlowMgrDetailInUDPPermPort": apFlowMgrDetailInUDPPermPort,
       "apFlowMgrDetailInJoined": apFlowMgrDetailInJoined,
       "apFlowMgrDetailInContentExpected": apFlowMgrDetailInContentExpected,
       "apFlowMgrDetailInJoinPending": apFlowMgrDetailInJoinPending,
       "apFlowMgrDetailInContentPending": apFlowMgrDetailInContentPending,
       "apFlowMgrDetailInTCPSYNSent": apFlowMgrDetailInTCPSYNSent,
       "apFlowMgrDetailInReversePending": apFlowMgrDetailInReversePending,
       "apFlowMgrDetailInSFPForwarded": apFlowMgrDetailInSFPForwarded,
       "apFlowMgrDetailInInPortInflowCount": apFlowMgrDetailInInPortInflowCount,
       "apFlowMgrDetailInDeleted": apFlowMgrDetailInDeleted,
       "apFlowMgrDetailInSpoofed": apFlowMgrDetailInSpoofed,
       "apFlowMgrDetailInNATInUse": apFlowMgrDetailInNATInUse,
       "apFlowMgrDetailInContentAware": apFlowMgrDetailInContentAware,
       "apFlowMgrDetailInSticky": apFlowMgrDetailInSticky,
       "apFlowMgrDetailInBridged": apFlowMgrDetailInBridged,
       "apFlowMgrDetailInBuffersPending": apFlowMgrDetailInBuffersPending,
       "apFlowMgrDetailInSYNDOSTimerActive": apFlowMgrDetailInSYNDOSTimerActive,
       "apFlowMgrDetailInOverflowMapped": apFlowMgrDetailInOverflowMapped,
       "apFlowMgrDetailInRejected": apFlowMgrDetailInRejected,
       "apFlowMgrDetailInTotalTCPFlows": apFlowMgrDetailInTotalTCPFlows,
       "apFlowMgrDetailInTotalUDPFlows": apFlowMgrDetailInTotalUDPFlows,
       "apFlowMgrDetailInHTTPSrcFlows": apFlowMgrDetailInHTTPSrcFlows,
       "apFlowMgrDetailInHTTPDstFlows": apFlowMgrDetailInHTTPDstFlows,
       "apFlowMgrDetailInFTPDataSrcFlows": apFlowMgrDetailInFTPDataSrcFlows,
       "apFlowMgrDetailInFTPDataDestFlows": apFlowMgrDetailInFTPDataDestFlows,
       "apFlowMgrDetailInFTPCtrlSrcFlows": apFlowMgrDetailInFTPCtrlSrcFlows,
       "apFlowMgrDetailInFTPCtrlDestFlows": apFlowMgrDetailInFTPCtrlDestFlows,
       "apFlowMgrDetailInSSHSrcFlows": apFlowMgrDetailInSSHSrcFlows,
       "apFlowMgrDetailInSSHDestFlows": apFlowMgrDetailInSSHDestFlows,
       "apFlowMgrDetailInTelnetSrcFlows": apFlowMgrDetailInTelnetSrcFlows,
       "apFlowMgrDetailInTelnetDestFlows": apFlowMgrDetailInTelnetDestFlows,
       "apFlowMgrDetailInRASrcFlows": apFlowMgrDetailInRASrcFlows,
       "apFlowMgrDetailInRADestFlows": apFlowMgrDetailInRADestFlows,
       "apFlowMgrDetailInBGPSrcFlows": apFlowMgrDetailInBGPSrcFlows,
       "apFlowMgrDetailInBGPDestFlows": apFlowMgrDetailInBGPDestFlows,
       "apFlowMgrDetailInSMTPSrcFlows": apFlowMgrDetailInSMTPSrcFlows,
       "apFlowMgrDetailInSMTPDestFlows": apFlowMgrDetailInSMTPDestFlows,
       "apFlowMgrDetailInPOP3SrcFlows": apFlowMgrDetailInPOP3SrcFlows,
       "apFlowMgrDetailInPOP3DestFlows": apFlowMgrDetailInPOP3DestFlows,
       "apFlowMgrDetailInHTTPSSrcFlows": apFlowMgrDetailInHTTPSSrcFlows,
       "apFlowMgrDetailInHTTPSDestFlows": apFlowMgrDetailInHTTPSDestFlows,
       "apFlowMgrDetailInNNTPSrcFlows": apFlowMgrDetailInNNTPSrcFlows,
       "apFlowMgrDetailInNNTPDestFlows": apFlowMgrDetailInNNTPDestFlows,
       "apFlowMgrDetailInSOCKSSrcFlows": apFlowMgrDetailInSOCKSSrcFlows,
       "apFlowMgrDetailInSOCKSDestFlows": apFlowMgrDetailInSOCKSDestFlows,
       "apFlowMgrDetailInPortLT23SrcFlows": apFlowMgrDetailInPortLT23SrcFlows,
       "apFlowMgrDetailInPortLT23DestFlows": apFlowMgrDetailInPortLT23DestFlows,
       "apFlowMgrDetailInPortGT1024SrcFlows": apFlowMgrDetailInPortGT1024SrcFlows,
       "apFlowMgrDetailInPortGT1024DestFlows": apFlowMgrDetailInPortGT1024DestFlows,
       "apFlowMgrDetailInTimeSrcFlows": apFlowMgrDetailInTimeSrcFlows,
       "apFlowMgrDetailInTimeDestSrcFlows": apFlowMgrDetailInTimeDestSrcFlows,
       "apFlowMgrDetailInDNSSrcFlows": apFlowMgrDetailInDNSSrcFlows,
       "apFlowMgrDetailInDNSDestFlows": apFlowMgrDetailInDNSDestFlows,
       "apFlowMgrDetailInSNMPSrcFlows": apFlowMgrDetailInSNMPSrcFlows,
       "apFlowMgrDetailInSNMPDestFlows": apFlowMgrDetailInSNMPDestFlows,
       "apFlowMgrDetailInSNMPTrapSrcFlows": apFlowMgrDetailInSNMPTrapSrcFlows,
       "apFlowMgrDetailInSNMPTrapDestFlows": apFlowMgrDetailInSNMPTrapDestFlows,
       "apFlowMgrDetailInNFSSrcFlows": apFlowMgrDetailInNFSSrcFlows,
       "apFlowMgrDetailInNFSDestFlows": apFlowMgrDetailInNFSDestFlows,
       "apFlowMgrDetailInUDPGT1024SrcFlows": apFlowMgrDetailInUDPGT1024SrcFlows,
       "apFlowMgrDetailInUDPGT1024DestFlows": apFlowMgrDetailInUDPGT1024DestFlows,
       "apFlowMgrDetailInUDPLT1024SrcFlows": apFlowMgrDetailInUDPLT1024SrcFlows,
       "apFlowMgrDetailInUDPLT1024DestFlows": apFlowMgrDetailInUDPLT1024DestFlows,
       "apFlowMgrDetailInExplicitFlows": apFlowMgrDetailInExplicitFlows,
       "apFlowMgrDetailInAcctSent": apFlowMgrDetailInAcctSent,
       "apFlowMgrDetailEgTCPPermPort": apFlowMgrDetailEgTCPPermPort,
       "apFlowMgrDetailEgUDPPermPort": apFlowMgrDetailEgUDPPermPort,
       "apFlowMgrDetailEgJoined": apFlowMgrDetailEgJoined,
       "apFlowMgrDetailEgContentExpected": apFlowMgrDetailEgContentExpected,
       "apFlowMgrDetailEgJoinPending": apFlowMgrDetailEgJoinPending,
       "apFlowMgrDetailEgContentPending": apFlowMgrDetailEgContentPending,
       "apFlowMgrDetailEgTCPSYNSent": apFlowMgrDetailEgTCPSYNSent,
       "apFlowMgrDetailEgReversePending": apFlowMgrDetailEgReversePending,
       "apFlowMgrDetailEgSFPFowrarded": apFlowMgrDetailEgSFPFowrarded,
       "apFlowMgrDetailEgInPortInflowCount": apFlowMgrDetailEgInPortInflowCount,
       "apFlowMgrDetailEgDeleted": apFlowMgrDetailEgDeleted,
       "apFlowMgrDetailEgSpoofed": apFlowMgrDetailEgSpoofed,
       "apFlowMgrDetailEgNATInUse": apFlowMgrDetailEgNATInUse,
       "apFlowMgrDetailEgContentAware": apFlowMgrDetailEgContentAware,
       "apFlowMgrDetailEgSticky": apFlowMgrDetailEgSticky,
       "apFlowMgrDetailEgBridged": apFlowMgrDetailEgBridged,
       "apFlowMgrDetailEgBuffersPending": apFlowMgrDetailEgBuffersPending,
       "apFlowMgrDetailEgSYNDOSTimerActive": apFlowMgrDetailEgSYNDOSTimerActive,
       "apFlowMgrDetailEgOverflowMapped": apFlowMgrDetailEgOverflowMapped,
       "apFlowMgrDetailEgRejected": apFlowMgrDetailEgRejected,
       "apFlowMgrDetailEgTotalTCPFlows": apFlowMgrDetailEgTotalTCPFlows,
       "apFlowMgrDetailEgTotalUDPFlows": apFlowMgrDetailEgTotalUDPFlows,
       "apFlowMgrDetailEgHTTPSrcFlows": apFlowMgrDetailEgHTTPSrcFlows,
       "apFlowMgrDetailEgHTTPDstFlows": apFlowMgrDetailEgHTTPDstFlows,
       "apFlowMgrDetailEgFTPDataSrcFlows": apFlowMgrDetailEgFTPDataSrcFlows,
       "apFlowMgrDetailEgFTPDataDestFlows": apFlowMgrDetailEgFTPDataDestFlows,
       "apFlowMgrDetailEgFTPCtrlSrcFlows": apFlowMgrDetailEgFTPCtrlSrcFlows,
       "apFlowMgrDetailEgFTPCtrlDestFlows": apFlowMgrDetailEgFTPCtrlDestFlows,
       "apFlowMgrDetailEgSSHSrcFlows": apFlowMgrDetailEgSSHSrcFlows,
       "apFlowMgrDetailEgSSHDestFlows": apFlowMgrDetailEgSSHDestFlows,
       "apFlowMgrDetailEgTelnetSrcFlows": apFlowMgrDetailEgTelnetSrcFlows,
       "apFlowMgrDetailEgTelnetDestFlows": apFlowMgrDetailEgTelnetDestFlows,
       "apFlowMgrDetailEgRASrcFlows": apFlowMgrDetailEgRASrcFlows,
       "apFlowMgrDetailEgRADestFlows": apFlowMgrDetailEgRADestFlows,
       "apFlowMgrDetailEgBGPSrcFlows": apFlowMgrDetailEgBGPSrcFlows,
       "apFlowMgrDetailEgBGPDestFlows": apFlowMgrDetailEgBGPDestFlows,
       "apFlowMgrDetailEgSMTPSrcFlows": apFlowMgrDetailEgSMTPSrcFlows,
       "apFlowMgrDetailEgSMTPDestFlows": apFlowMgrDetailEgSMTPDestFlows,
       "apFlowMgrDetailEgPOP3SrcFlows": apFlowMgrDetailEgPOP3SrcFlows,
       "apFlowMgrDetailEgPOP3DestFlows": apFlowMgrDetailEgPOP3DestFlows,
       "apFlowMgrDetailEgHTTPSSrcFlows": apFlowMgrDetailEgHTTPSSrcFlows,
       "apFlowMgrDetailEgHTTPSDestFlows": apFlowMgrDetailEgHTTPSDestFlows,
       "apFlowMgrDetailEgNNTPSrcFlows": apFlowMgrDetailEgNNTPSrcFlows,
       "apFlowMgrDetailEgNNTPDestFlows": apFlowMgrDetailEgNNTPDestFlows,
       "apFlowMgrDetailEgSOCKSSrcFlows": apFlowMgrDetailEgSOCKSSrcFlows,
       "apFlowMgrDetailEgSOCKSDestFlows": apFlowMgrDetailEgSOCKSDestFlows,
       "apFlowMgrDetailEgPortLT23SrcFlows": apFlowMgrDetailEgPortLT23SrcFlows,
       "apFlowMgrDetailEgPortLT23DestFlows": apFlowMgrDetailEgPortLT23DestFlows,
       "apFlowMgrDetailEgPortGT1024SrcFlows": apFlowMgrDetailEgPortGT1024SrcFlows,
       "apFlowMgrDetailEgPortGT1024DestFlows": apFlowMgrDetailEgPortGT1024DestFlows,
       "apFlowMgrDetailEgTimeSrcFlows": apFlowMgrDetailEgTimeSrcFlows,
       "apFlowMgrDetailEgTimeDestSrcFlows": apFlowMgrDetailEgTimeDestSrcFlows,
       "apFlowMgrDetailEgDNSSrcFlows": apFlowMgrDetailEgDNSSrcFlows,
       "apFlowMgrDetailEgDNSDestFlows": apFlowMgrDetailEgDNSDestFlows,
       "apFlowMgrDetailEgSNMPSrcFlows": apFlowMgrDetailEgSNMPSrcFlows,
       "apFlowMgrDetailEgSNMPDestFlows": apFlowMgrDetailEgSNMPDestFlows,
       "apFlowMgrDetailEgSNMPTrapSrcFlows": apFlowMgrDetailEgSNMPTrapSrcFlows,
       "apFlowMgrDetailEgSNMPTrapDestFlows": apFlowMgrDetailEgSNMPTrapDestFlows,
       "apFlowMgrDetailEgNFSSrcFlows": apFlowMgrDetailEgNFSSrcFlows,
       "apFlowMgrDetailEgNFSDestFlows": apFlowMgrDetailEgNFSDestFlows,
       "apFlowMgrDetailEgUDPGT1024SrcFlows": apFlowMgrDetailEgUDPGT1024SrcFlows,
       "apFlowMgrDetailEgUDPGT1024DestFlows": apFlowMgrDetailEgUDPGT1024DestFlows,
       "apFlowMgrDetailEgUDPLT1024SrcFlows": apFlowMgrDetailEgUDPLT1024SrcFlows,
       "apFlowMgrDetailEgUDPLT1024DestFlows": apFlowMgrDetailEgUDPLT1024DestFlows,
       "apFlowMgrDetailOutFrames": apFlowMgrDetailOutFrames,
       "apFlowMgrExtDosTotalAttacks": apFlowMgrExtDosTotalAttacks,
       "apFlowMgrExtDosTotalSynAttacks": apFlowMgrExtDosTotalSynAttacks,
       "apFlowMgrExtDosTotalLandAttacks": apFlowMgrExtDosTotalLandAttacks,
       "apFlowMgrExtDosTotalZeroPortAttacks": apFlowMgrExtDosTotalZeroPortAttacks,
       "apFlowMgrExtDosTotalIllegalSourceAttacks": apFlowMgrExtDosTotalIllegalSourceAttacks,
       "apFlowMgrExtDosTotalIllegalDestinationAttacks": apFlowMgrExtDosTotalIllegalDestinationAttacks,
       "apFlowMgrExtDosTotalPingOfDeathAttacks": apFlowMgrExtDosTotalPingOfDeathAttacks,
       "apFlowMgrExtDosTotalSmurfAttacks": apFlowMgrExtDosTotalSmurfAttacks,
       "apFlowMgrExtDosLastAttack": apFlowMgrExtDosLastAttack,
       "apFlowMgrExtDosFirstAttack": apFlowMgrExtDosFirstAttack,
       "apFlowMgrExtDOSAttackTable": apFlowMgrExtDOSAttackTable,
       "apFlowMgrExtDOSAttackEntry": apFlowMgrExtDOSAttackEntry,
       "apFlowMgrExtDOSAttackIndex": apFlowMgrExtDOSAttackIndex,
       "apFlowMgrExtDOSAttackSrcAddress": apFlowMgrExtDOSAttackSrcAddress,
       "apFlowMgrExtDOSAttackDestAddress": apFlowMgrExtDOSAttackDestAddress,
       "apFlowMgrExtDOSAttackFirstEvent": apFlowMgrExtDOSAttackFirstEvent,
       "apFlowMgrExtDOSAttackLastEvent": apFlowMgrExtDOSAttackLastEvent,
       "apFlowMgrExtDOSAttackEventCount": apFlowMgrExtDOSAttackEventCount,
       "apFlowMgrExtDOSAttackEventType": apFlowMgrExtDOSAttackEventType,
       "apFlowMgrExtDOSAttackEventString": apFlowMgrExtDOSAttackEventString}
)
