# SNMP MIB module (EXTREME-NP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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

extremeNPMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeNPModule_ObjectIdentity = ObjectIdentity
extremeNPModule = _ExtremeNPModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 1)
)
_ExtremeNPModuleTable_Object = MibTable
extremeNPModuleTable = _ExtremeNPModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 1, 1)
)
if mibBuilder.loadTexts:
    extremeNPModuleTable.setStatus("current")
_ExtremeNPModuleEntry_Object = MibTableRow
extremeNPModuleEntry = _ExtremeNPModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 1, 1, 1)
)
extremeNPModuleEntry.setIndexNames(
    (0, "EXTREME-NP-MIB", "extremeNPModuleSlotNumber"),
)
if mibBuilder.loadTexts:
    extremeNPModuleEntry.setStatus("current")


class _ExtremeNPModuleSlotNumber_Type(Integer32):
    """Custom type extremeNPModuleSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ExtremeNPModuleSlotNumber_Type.__name__ = "Integer32"
_ExtremeNPModuleSlotNumber_Object = MibTableColumn
extremeNPModuleSlotNumber = _ExtremeNPModuleSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 1, 1, 1, 1),
    _ExtremeNPModuleSlotNumber_Type()
)
extremeNPModuleSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNPModuleSlotNumber.setStatus("current")


class _ExtremeNPModuleDescription_Type(DisplayString):
    """Custom type extremeNPModuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeNPModuleDescription_Type.__name__ = "DisplayString"
_ExtremeNPModuleDescription_Object = MibTableColumn
extremeNPModuleDescription = _ExtremeNPModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 1, 1, 1, 2),
    _ExtremeNPModuleDescription_Type()
)
extremeNPModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNPModuleDescription.setStatus("current")


class _ExtremeNPModuleCurrentSoftware_Type(DisplayString):
    """Custom type extremeNPModuleCurrentSoftware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_ExtremeNPModuleCurrentSoftware_Type.__name__ = "DisplayString"
_ExtremeNPModuleCurrentSoftware_Object = MibTableColumn
extremeNPModuleCurrentSoftware = _ExtremeNPModuleCurrentSoftware_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 1, 1, 1, 3),
    _ExtremeNPModuleCurrentSoftware_Type()
)
extremeNPModuleCurrentSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNPModuleCurrentSoftware.setStatus("current")


class _ExtremeNPModulePrimarySoftware_Type(DisplayString):
    """Custom type extremeNPModulePrimarySoftware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_ExtremeNPModulePrimarySoftware_Type.__name__ = "DisplayString"
_ExtremeNPModulePrimarySoftware_Object = MibTableColumn
extremeNPModulePrimarySoftware = _ExtremeNPModulePrimarySoftware_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 1, 1, 1, 4),
    _ExtremeNPModulePrimarySoftware_Type()
)
extremeNPModulePrimarySoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNPModulePrimarySoftware.setStatus("current")


class _ExtremeNPModuleSecondarySoftware_Type(DisplayString):
    """Custom type extremeNPModuleSecondarySoftware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_ExtremeNPModuleSecondarySoftware_Type.__name__ = "DisplayString"
_ExtremeNPModuleSecondarySoftware_Object = MibTableColumn
extremeNPModuleSecondarySoftware = _ExtremeNPModuleSecondarySoftware_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 1, 1, 1, 5),
    _ExtremeNPModuleSecondarySoftware_Type()
)
extremeNPModuleSecondarySoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNPModuleSecondarySoftware.setStatus("current")


class _ExtremeNPModuleBootromVersion_Type(DisplayString):
    """Custom type extremeNPModuleBootromVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ExtremeNPModuleBootromVersion_Type.__name__ = "DisplayString"
_ExtremeNPModuleBootromVersion_Object = MibTableColumn
extremeNPModuleBootromVersion = _ExtremeNPModuleBootromVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 1, 1, 1, 6),
    _ExtremeNPModuleBootromVersion_Type()
)
extremeNPModuleBootromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNPModuleBootromVersion.setStatus("current")


class _ExtremeNPModuleProcessorState_Type(OctetString):
    """Custom type extremeNPModuleProcessorState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ExtremeNPModuleProcessorState_Type.__name__ = "OctetString"
_ExtremeNPModuleProcessorState_Object = MibTableColumn
extremeNPModuleProcessorState = _ExtremeNPModuleProcessorState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 1, 1, 1, 7),
    _ExtremeNPModuleProcessorState_Type()
)
extremeNPModuleProcessorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNPModuleProcessorState.setStatus("current")
_ExtremeSMAModule_ObjectIdentity = ObjectIdentity
extremeSMAModule = _ExtremeSMAModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2)
)
_ExtremeSMATable_Object = MibTable
extremeSMATable = _ExtremeSMATable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1)
)
if mibBuilder.loadTexts:
    extremeSMATable.setStatus("current")
_ExtremeSMAEntry_Object = MibTableRow
extremeSMAEntry = _ExtremeSMAEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1)
)
extremeSMAEntry.setIndexNames(
    (0, "EXTREME-NP-MIB", "extremeSMASlotNumber"),
)
if mibBuilder.loadTexts:
    extremeSMAEntry.setStatus("current")


class _ExtremeSMASlotNumber_Type(Integer32):
    """Custom type extremeSMASlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ExtremeSMASlotNumber_Type.__name__ = "Integer32"
_ExtremeSMASlotNumber_Object = MibTableColumn
extremeSMASlotNumber = _ExtremeSMASlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 1),
    _ExtremeSMASlotNumber_Type()
)
extremeSMASlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMASlotNumber.setStatus("current")


class _ExtremeSMAProtocolVersion_Type(Integer32):
    """Custom type extremeSMAProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeSMAProtocolVersion_Type.__name__ = "Integer32"
_ExtremeSMAProtocolVersion_Object = MibTableColumn
extremeSMAProtocolVersion = _ExtremeSMAProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 2),
    _ExtremeSMAProtocolVersion_Type()
)
extremeSMAProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMAProtocolVersion.setStatus("current")


class _ExtremeSMAServiceVersion_Type(DisplayString):
    """Custom type extremeSMAServiceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ExtremeSMAServiceVersion_Type.__name__ = "DisplayString"
_ExtremeSMAServiceVersion_Object = MibTableColumn
extremeSMAServiceVersion = _ExtremeSMAServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 3),
    _ExtremeSMAServiceVersion_Type()
)
extremeSMAServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMAServiceVersion.setStatus("current")
_ExtremeSMAUpTime_Type = Unsigned32
_ExtremeSMAUpTime_Object = MibTableColumn
extremeSMAUpTime = _ExtremeSMAUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 4),
    _ExtremeSMAUpTime_Type()
)
extremeSMAUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMAUpTime.setStatus("current")
_ExtremeSMACpuUtilization_Type = Unsigned32
_ExtremeSMACpuUtilization_Object = MibTableColumn
extremeSMACpuUtilization = _ExtremeSMACpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 5),
    _ExtremeSMACpuUtilization_Type()
)
extremeSMACpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMACpuUtilization.setStatus("current")
_ExtremeSMAMemUtilization_Type = Unsigned32
_ExtremeSMAMemUtilization_Object = MibTableColumn
extremeSMAMemUtilization = _ExtremeSMAMemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 6),
    _ExtremeSMAMemUtilization_Type()
)
extremeSMAMemUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMAMemUtilization.setStatus("current")
_ExtremeSMAQosBroadcaster_Type = Unsigned32
_ExtremeSMAQosBroadcaster_Object = MibTableColumn
extremeSMAQosBroadcaster = _ExtremeSMAQosBroadcaster_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 7),
    _ExtremeSMAQosBroadcaster_Type()
)
extremeSMAQosBroadcaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMAQosBroadcaster.setStatus("current")
_ExtremeSMANumFromBroadcaster_Type = Unsigned32
_ExtremeSMANumFromBroadcaster_Object = MibTableColumn
extremeSMANumFromBroadcaster = _ExtremeSMANumFromBroadcaster_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 8),
    _ExtremeSMANumFromBroadcaster_Type()
)
extremeSMANumFromBroadcaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMANumFromBroadcaster.setStatus("current")
_ExtremeSMANumToListener_Type = Unsigned32
_ExtremeSMANumToListener_Object = MibTableColumn
extremeSMANumToListener = _ExtremeSMANumToListener_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 9),
    _ExtremeSMANumToListener_Type()
)
extremeSMANumToListener.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMANumToListener.setStatus("current")
_ExtremeSMABytesBroadcaster_Type = Counter64
_ExtremeSMABytesBroadcaster_Object = MibTableColumn
extremeSMABytesBroadcaster = _ExtremeSMABytesBroadcaster_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 10),
    _ExtremeSMABytesBroadcaster_Type()
)
extremeSMABytesBroadcaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMABytesBroadcaster.setStatus("current")
_ExtremeSMABytesListener_Type = Counter64
_ExtremeSMABytesListener_Object = MibTableColumn
extremeSMABytesListener = _ExtremeSMABytesListener_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 2, 1, 1, 11),
    _ExtremeSMABytesListener_Type()
)
extremeSMABytesListener.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeSMABytesListener.setStatus("current")
_ExtremeATMModule_ObjectIdentity = ObjectIdentity
extremeATMModule = _ExtremeATMModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3)
)
_ExtremeATMCellPduTable_Object = MibTable
extremeATMCellPduTable = _ExtremeATMCellPduTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1)
)
if mibBuilder.loadTexts:
    extremeATMCellPduTable.setStatus("current")
_ExtremeATMCellPduEntry_Object = MibTableRow
extremeATMCellPduEntry = _ExtremeATMCellPduEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1)
)
extremeATMCellPduEntry.setIndexNames(
    (0, "EXTREME-NP-MIB", "extremeATMPortNumber"),
)
if mibBuilder.loadTexts:
    extremeATMCellPduEntry.setStatus("current")


class _ExtremeATMPortNumber_Type(Integer32):
    """Custom type extremeATMPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ExtremeATMPortNumber_Type.__name__ = "Integer32"
_ExtremeATMPortNumber_Object = MibTableColumn
extremeATMPortNumber = _ExtremeATMPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1, 1),
    _ExtremeATMPortNumber_Type()
)
extremeATMPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMPortNumber.setStatus("current")
_ExtremeATMRxCell_Type = Unsigned32
_ExtremeATMRxCell_Object = MibTableColumn
extremeATMRxCell = _ExtremeATMRxCell_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1, 2),
    _ExtremeATMRxCell_Type()
)
extremeATMRxCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMRxCell.setStatus("current")
_ExtremeATMTxCell_Type = Unsigned32
_ExtremeATMTxCell_Object = MibTableColumn
extremeATMTxCell = _ExtremeATMTxCell_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1, 3),
    _ExtremeATMTxCell_Type()
)
extremeATMTxCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMTxCell.setStatus("current")
_ExtremeATMRxCellHecError_Type = Unsigned32
_ExtremeATMRxCellHecError_Object = MibTableColumn
extremeATMRxCellHecError = _ExtremeATMRxCellHecError_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1, 4),
    _ExtremeATMRxCellHecError_Type()
)
extremeATMRxCellHecError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMRxCellHecError.setStatus("current")
_ExtremeATMRxCellError_Type = Unsigned32
_ExtremeATMRxCellError_Object = MibTableColumn
extremeATMRxCellError = _ExtremeATMRxCellError_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1, 5),
    _ExtremeATMRxCellError_Type()
)
extremeATMRxCellError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMRxCellError.setStatus("current")
_ExtremeATMRxAAL5Pdu_Type = Unsigned32
_ExtremeATMRxAAL5Pdu_Object = MibTableColumn
extremeATMRxAAL5Pdu = _ExtremeATMRxAAL5Pdu_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1, 6),
    _ExtremeATMRxAAL5Pdu_Type()
)
extremeATMRxAAL5Pdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMRxAAL5Pdu.setStatus("current")
_ExtremeATMTxAAL5Pdu_Type = Unsigned32
_ExtremeATMTxAAL5Pdu_Object = MibTableColumn
extremeATMTxAAL5Pdu = _ExtremeATMTxAAL5Pdu_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1, 7),
    _ExtremeATMTxAAL5Pdu_Type()
)
extremeATMTxAAL5Pdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMTxAAL5Pdu.setStatus("current")
_ExtremeATMRxAAL5Bytes_Type = Counter64
_ExtremeATMRxAAL5Bytes_Object = MibTableColumn
extremeATMRxAAL5Bytes = _ExtremeATMRxAAL5Bytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1, 8),
    _ExtremeATMRxAAL5Bytes_Type()
)
extremeATMRxAAL5Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMRxAAL5Bytes.setStatus("current")
_ExtremeATMTxAAL5Bytes_Type = Counter64
_ExtremeATMTxAAL5Bytes_Object = MibTableColumn
extremeATMTxAAL5Bytes = _ExtremeATMTxAAL5Bytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1, 9),
    _ExtremeATMTxAAL5Bytes_Type()
)
extremeATMTxAAL5Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMTxAAL5Bytes.setStatus("current")


class _ExtremeATMPortStatus_Type(DisplayString):
    """Custom type extremeATMPortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ExtremeATMPortStatus_Type.__name__ = "DisplayString"
_ExtremeATMPortStatus_Object = MibTableColumn
extremeATMPortStatus = _ExtremeATMPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 1, 1, 10),
    _ExtremeATMPortStatus_Type()
)
extremeATMPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMPortStatus.setStatus("current")
_ExtremeATMVpiVciTable_Object = MibTable
extremeATMVpiVciTable = _ExtremeATMVpiVciTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 2)
)
if mibBuilder.loadTexts:
    extremeATMVpiVciTable.setStatus("current")
_ExtremeATMVpiVciEntry_Object = MibTableRow
extremeATMVpiVciEntry = _ExtremeATMVpiVciEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 2, 1)
)
extremeATMVpiVciEntry.setIndexNames(
    (0, "EXTREME-NP-MIB", "extremeATMPortNum"),
    (0, "EXTREME-NP-MIB", "extremeATMPvc"),
)
if mibBuilder.loadTexts:
    extremeATMVpiVciEntry.setStatus("current")


class _ExtremeATMPortNum_Type(Integer32):
    """Custom type extremeATMPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ExtremeATMPortNum_Type.__name__ = "Integer32"
_ExtremeATMPortNum_Object = MibTableColumn
extremeATMPortNum = _ExtremeATMPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 2, 1, 1),
    _ExtremeATMPortNum_Type()
)
extremeATMPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMPortNum.setStatus("current")


class _ExtremeATMPvc_Type(Integer32):
    """Custom type extremeATMPvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3072),
    )


_ExtremeATMPvc_Type.__name__ = "Integer32"
_ExtremeATMPvc_Object = MibTableColumn
extremeATMPvc = _ExtremeATMPvc_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 2, 1, 2),
    _ExtremeATMPvc_Type()
)
extremeATMPvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMPvc.setStatus("current")


class _ExtremeATMVpi_Type(Integer32):
    """Custom type extremeATMVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ExtremeATMVpi_Type.__name__ = "Integer32"
_ExtremeATMVpi_Object = MibTableColumn
extremeATMVpi = _ExtremeATMVpi_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 2, 1, 3),
    _ExtremeATMVpi_Type()
)
extremeATMVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMVpi.setStatus("current")


class _ExtremeATMVci_Type(Integer32):
    """Custom type extremeATMVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 4095),
    )


_ExtremeATMVci_Type.__name__ = "Integer32"
_ExtremeATMVci_Object = MibTableColumn
extremeATMVci = _ExtremeATMVci_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 3, 2, 1, 4),
    _ExtremeATMVci_Type()
)
extremeATMVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeATMVci.setStatus("current")
_ExtremeMplsModule_ObjectIdentity = ObjectIdentity
extremeMplsModule = _ExtremeMplsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4)
)
_ExtremeMplsTlsTable_Object = MibTable
extremeMplsTlsTable = _ExtremeMplsTlsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1)
)
if mibBuilder.loadTexts:
    extremeMplsTlsTable.setStatus("current")
_ExtremeMplsTlsEntry_Object = MibTableRow
extremeMplsTlsEntry = _ExtremeMplsTlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1)
)
extremeMplsTlsEntry.setIndexNames(
    (0, "EXTREME-NP-MIB", "extremeMplsTlsNum"),
)
if mibBuilder.loadTexts:
    extremeMplsTlsEntry.setStatus("current")


class _ExtremeMplsTlsNum_Type(Integer32):
    """Custom type extremeMplsTlsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_ExtremeMplsTlsNum_Type.__name__ = "Integer32"
_ExtremeMplsTlsNum_Object = MibTableColumn
extremeMplsTlsNum = _ExtremeMplsTlsNum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 1),
    _ExtremeMplsTlsNum_Type()
)
extremeMplsTlsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsNum.setStatus("current")


class _ExtremeMplsTlsName_Type(DisplayString):
    """Custom type extremeMplsTlsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExtremeMplsTlsName_Type.__name__ = "DisplayString"
_ExtremeMplsTlsName_Object = MibTableColumn
extremeMplsTlsName = _ExtremeMplsTlsName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 2),
    _ExtremeMplsTlsName_Type()
)
extremeMplsTlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsName.setStatus("current")
_ExtremeMplsTlsLocalIpAddr_Type = IpAddress
_ExtremeMplsTlsLocalIpAddr_Object = MibTableColumn
extremeMplsTlsLocalIpAddr = _ExtremeMplsTlsLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 3),
    _ExtremeMplsTlsLocalIpAddr_Type()
)
extremeMplsTlsLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsLocalIpAddr.setStatus("current")
_ExtremeMplsTlsPeerIpAddr_Type = IpAddress
_ExtremeMplsTlsPeerIpAddr_Object = MibTableColumn
extremeMplsTlsPeerIpAddr = _ExtremeMplsTlsPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 4),
    _ExtremeMplsTlsPeerIpAddr_Type()
)
extremeMplsTlsPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsPeerIpAddr.setStatus("current")
_ExtremeMplsTlsLocalVlanID_Type = Unsigned32
_ExtremeMplsTlsLocalVlanID_Object = MibTableColumn
extremeMplsTlsLocalVlanID = _ExtremeMplsTlsLocalVlanID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 5),
    _ExtremeMplsTlsLocalVlanID_Type()
)
extremeMplsTlsLocalVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsLocalVlanID.setStatus("current")


class _ExtremeMplsTlsLocalVlanName_Type(DisplayString):
    """Custom type extremeMplsTlsLocalVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExtremeMplsTlsLocalVlanName_Type.__name__ = "DisplayString"
_ExtremeMplsTlsLocalVlanName_Object = MibTableColumn
extremeMplsTlsLocalVlanName = _ExtremeMplsTlsLocalVlanName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 6),
    _ExtremeMplsTlsLocalVlanName_Type()
)
extremeMplsTlsLocalVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsLocalVlanName.setStatus("current")
_ExtremeMplsTlsDynamic_Type = Unsigned32
_ExtremeMplsTlsDynamic_Object = MibTableColumn
extremeMplsTlsDynamic = _ExtremeMplsTlsDynamic_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 7),
    _ExtremeMplsTlsDynamic_Type()
)
extremeMplsTlsDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsDynamic.setStatus("current")
_ExtremeMplsTlsType_Type = Unsigned32
_ExtremeMplsTlsType_Object = MibTableColumn
extremeMplsTlsType = _ExtremeMplsTlsType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 8),
    _ExtremeMplsTlsType_Type()
)
extremeMplsTlsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsType.setStatus("current")
_ExtremeMplsTlsVcID_Type = Unsigned32
_ExtremeMplsTlsVcID_Object = MibTableColumn
extremeMplsTlsVcID = _ExtremeMplsTlsVcID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 9),
    _ExtremeMplsTlsVcID_Type()
)
extremeMplsTlsVcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsVcID.setStatus("current")
_ExtremeMplsTlsLocalGroupID_Type = Unsigned32
_ExtremeMplsTlsLocalGroupID_Object = MibTableColumn
extremeMplsTlsLocalGroupID = _ExtremeMplsTlsLocalGroupID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 10),
    _ExtremeMplsTlsLocalGroupID_Type()
)
extremeMplsTlsLocalGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsLocalGroupID.setStatus("current")
_ExtremeMplsTlsRemoteGroupID_Type = Unsigned32
_ExtremeMplsTlsRemoteGroupID_Object = MibTableColumn
extremeMplsTlsRemoteGroupID = _ExtremeMplsTlsRemoteGroupID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 11),
    _ExtremeMplsTlsRemoteGroupID_Type()
)
extremeMplsTlsRemoteGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsRemoteGroupID.setStatus("current")
_ExtremeMplsTlsIngressVcLabel_Type = Unsigned32
_ExtremeMplsTlsIngressVcLabel_Object = MibTableColumn
extremeMplsTlsIngressVcLabel = _ExtremeMplsTlsIngressVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 12),
    _ExtremeMplsTlsIngressVcLabel_Type()
)
extremeMplsTlsIngressVcLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsIngressVcLabel.setStatus("current")
_ExtremeMplsTlsEgressVcLabel_Type = Unsigned32
_ExtremeMplsTlsEgressVcLabel_Object = MibTableColumn
extremeMplsTlsEgressVcLabel = _ExtremeMplsTlsEgressVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 13),
    _ExtremeMplsTlsEgressVcLabel_Type()
)
extremeMplsTlsEgressVcLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsEgressVcLabel.setStatus("current")


class _ExtremeMplsTlsVcState_Type(DisplayString):
    """Custom type extremeMplsTlsVcState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ExtremeMplsTlsVcState_Type.__name__ = "DisplayString"
_ExtremeMplsTlsVcState_Object = MibTableColumn
extremeMplsTlsVcState = _ExtremeMplsTlsVcState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 14),
    _ExtremeMplsTlsVcState_Type()
)
extremeMplsTlsVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsVcState.setStatus("current")
_ExtremeMplsTlsPacketTx_Type = Unsigned32
_ExtremeMplsTlsPacketTx_Object = MibTableColumn
extremeMplsTlsPacketTx = _ExtremeMplsTlsPacketTx_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 15),
    _ExtremeMplsTlsPacketTx_Type()
)
extremeMplsTlsPacketTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsPacketTx.setStatus("current")
_ExtremeMplsTlsPacketRx_Type = Unsigned32
_ExtremeMplsTlsPacketRx_Object = MibTableColumn
extremeMplsTlsPacketRx = _ExtremeMplsTlsPacketRx_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 16),
    _ExtremeMplsTlsPacketRx_Type()
)
extremeMplsTlsPacketRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsPacketRx.setStatus("current")
_ExtremeMplsTlsOctetTx_Type = Counter64
_ExtremeMplsTlsOctetTx_Object = MibTableColumn
extremeMplsTlsOctetTx = _ExtremeMplsTlsOctetTx_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 17),
    _ExtremeMplsTlsOctetTx_Type()
)
extremeMplsTlsOctetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsOctetTx.setStatus("current")
_ExtremeMplsTlsOctetRx_Type = Counter64
_ExtremeMplsTlsOctetRx_Object = MibTableColumn
extremeMplsTlsOctetRx = _ExtremeMplsTlsOctetRx_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21, 4, 1, 1, 18),
    _ExtremeMplsTlsOctetRx_Type()
)
extremeMplsTlsOctetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMplsTlsOctetRx.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-NP-MIB",
    **{"extremeNPMib": extremeNPMib,
       "extremeNPModule": extremeNPModule,
       "extremeNPModuleTable": extremeNPModuleTable,
       "extremeNPModuleEntry": extremeNPModuleEntry,
       "extremeNPModuleSlotNumber": extremeNPModuleSlotNumber,
       "extremeNPModuleDescription": extremeNPModuleDescription,
       "extremeNPModuleCurrentSoftware": extremeNPModuleCurrentSoftware,
       "extremeNPModulePrimarySoftware": extremeNPModulePrimarySoftware,
       "extremeNPModuleSecondarySoftware": extremeNPModuleSecondarySoftware,
       "extremeNPModuleBootromVersion": extremeNPModuleBootromVersion,
       "extremeNPModuleProcessorState": extremeNPModuleProcessorState,
       "extremeSMAModule": extremeSMAModule,
       "extremeSMATable": extremeSMATable,
       "extremeSMAEntry": extremeSMAEntry,
       "extremeSMASlotNumber": extremeSMASlotNumber,
       "extremeSMAProtocolVersion": extremeSMAProtocolVersion,
       "extremeSMAServiceVersion": extremeSMAServiceVersion,
       "extremeSMAUpTime": extremeSMAUpTime,
       "extremeSMACpuUtilization": extremeSMACpuUtilization,
       "extremeSMAMemUtilization": extremeSMAMemUtilization,
       "extremeSMAQosBroadcaster": extremeSMAQosBroadcaster,
       "extremeSMANumFromBroadcaster": extremeSMANumFromBroadcaster,
       "extremeSMANumToListener": extremeSMANumToListener,
       "extremeSMABytesBroadcaster": extremeSMABytesBroadcaster,
       "extremeSMABytesListener": extremeSMABytesListener,
       "extremeATMModule": extremeATMModule,
       "extremeATMCellPduTable": extremeATMCellPduTable,
       "extremeATMCellPduEntry": extremeATMCellPduEntry,
       "extremeATMPortNumber": extremeATMPortNumber,
       "extremeATMRxCell": extremeATMRxCell,
       "extremeATMTxCell": extremeATMTxCell,
       "extremeATMRxCellHecError": extremeATMRxCellHecError,
       "extremeATMRxCellError": extremeATMRxCellError,
       "extremeATMRxAAL5Pdu": extremeATMRxAAL5Pdu,
       "extremeATMTxAAL5Pdu": extremeATMTxAAL5Pdu,
       "extremeATMRxAAL5Bytes": extremeATMRxAAL5Bytes,
       "extremeATMTxAAL5Bytes": extremeATMTxAAL5Bytes,
       "extremeATMPortStatus": extremeATMPortStatus,
       "extremeATMVpiVciTable": extremeATMVpiVciTable,
       "extremeATMVpiVciEntry": extremeATMVpiVciEntry,
       "extremeATMPortNum": extremeATMPortNum,
       "extremeATMPvc": extremeATMPvc,
       "extremeATMVpi": extremeATMVpi,
       "extremeATMVci": extremeATMVci,
       "extremeMplsModule": extremeMplsModule,
       "extremeMplsTlsTable": extremeMplsTlsTable,
       "extremeMplsTlsEntry": extremeMplsTlsEntry,
       "extremeMplsTlsNum": extremeMplsTlsNum,
       "extremeMplsTlsName": extremeMplsTlsName,
       "extremeMplsTlsLocalIpAddr": extremeMplsTlsLocalIpAddr,
       "extremeMplsTlsPeerIpAddr": extremeMplsTlsPeerIpAddr,
       "extremeMplsTlsLocalVlanID": extremeMplsTlsLocalVlanID,
       "extremeMplsTlsLocalVlanName": extremeMplsTlsLocalVlanName,
       "extremeMplsTlsDynamic": extremeMplsTlsDynamic,
       "extremeMplsTlsType": extremeMplsTlsType,
       "extremeMplsTlsVcID": extremeMplsTlsVcID,
       "extremeMplsTlsLocalGroupID": extremeMplsTlsLocalGroupID,
       "extremeMplsTlsRemoteGroupID": extremeMplsTlsRemoteGroupID,
       "extremeMplsTlsIngressVcLabel": extremeMplsTlsIngressVcLabel,
       "extremeMplsTlsEgressVcLabel": extremeMplsTlsEgressVcLabel,
       "extremeMplsTlsVcState": extremeMplsTlsVcState,
       "extremeMplsTlsPacketTx": extremeMplsTlsPacketTx,
       "extremeMplsTlsPacketRx": extremeMplsTlsPacketRx,
       "extremeMplsTlsOctetTx": extremeMplsTlsOctetTx,
       "extremeMplsTlsOctetRx": extremeMplsTlsOctetRx}
)
