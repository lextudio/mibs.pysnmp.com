# SNMP MIB module (XYLAN-WSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-WSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:19 2024
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

(xylanWsmArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanWsmArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsmPortGroup_ObjectIdentity = ObjectIdentity
wsmPortGroup = _WsmPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1)
)
_WsmPortTable_Object = MibTable
wsmPortTable = _WsmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    wsmPortTable.setStatus("mandatory")
_WsmPortEntry_Object = MibTableRow
wsmPortEntry = _WsmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1)
)
wsmPortEntry.setIndexNames(
    (0, "XYLAN-WSM-MIB", "wsmPortSlotIndex"),
    (0, "XYLAN-WSM-MIB", "wsmPortPortIndex"),
)
if mibBuilder.loadTexts:
    wsmPortEntry.setStatus("mandatory")


class _WsmPortSlotIndex_Type(Integer32):
    """Custom type wsmPortSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_WsmPortSlotIndex_Type.__name__ = "Integer32"
_WsmPortSlotIndex_Object = MibTableColumn
wsmPortSlotIndex = _WsmPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 1),
    _WsmPortSlotIndex_Type()
)
wsmPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsmPortSlotIndex.setStatus("mandatory")


class _WsmPortPortIndex_Type(Integer32):
    """Custom type wsmPortPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WsmPortPortIndex_Type.__name__ = "Integer32"
_WsmPortPortIndex_Object = MibTableColumn
wsmPortPortIndex = _WsmPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 2),
    _WsmPortPortIndex_Type()
)
wsmPortPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsmPortPortIndex.setStatus("mandatory")


class _WsmPortInterfaceType_Type(Integer32):
    """Custom type wsmPortInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 3),
          ("isdnBRI", 2),
          ("universalSerial", 1))
    )


_WsmPortInterfaceType_Type.__name__ = "Integer32"
_WsmPortInterfaceType_Object = MibTableColumn
wsmPortInterfaceType = _WsmPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 3),
    _WsmPortInterfaceType_Type()
)
wsmPortInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsmPortInterfaceType.setStatus("mandatory")


class _WsmPortCableType_Type(Integer32):
    """Custom type wsmPortCableType based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("e1", 15),
          ("indeterminate", 2),
          ("isdnSt", 13),
          ("isdnU", 12),
          ("noneAttached", 1),
          ("rs232DCE", 5),
          ("rs232DTE", 4),
          ("rs530DCE", 9),
          ("rs530DTE", 8),
          ("t1", 14),
          ("unknown", 3),
          ("v35DCE", 7),
          ("v35DTE", 6),
          ("x21DCE", 11),
          ("x21DTE", 10))
    )


_WsmPortCableType_Type.__name__ = "Integer32"
_WsmPortCableType_Object = MibTableColumn
wsmPortCableType = _WsmPortCableType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 4),
    _WsmPortCableType_Type()
)
wsmPortCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsmPortCableType.setStatus("mandatory")


class _WsmPortSerialRxClockPol_Type(Integer32):
    """Custom type wsmPortSerialRxClockPol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("non-inverted", 1))
    )


_WsmPortSerialRxClockPol_Type.__name__ = "Integer32"
_WsmPortSerialRxClockPol_Object = MibTableColumn
wsmPortSerialRxClockPol = _WsmPortSerialRxClockPol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 5),
    _WsmPortSerialRxClockPol_Type()
)
wsmPortSerialRxClockPol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsmPortSerialRxClockPol.setStatus("mandatory")


class _WsmPortSerialTxClockPol_Type(Integer32):
    """Custom type wsmPortSerialTxClockPol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("non-inverted", 1))
    )


_WsmPortSerialTxClockPol_Type.__name__ = "Integer32"
_WsmPortSerialTxClockPol_Object = MibTableColumn
wsmPortSerialTxClockPol = _WsmPortSerialTxClockPol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 6),
    _WsmPortSerialTxClockPol_Type()
)
wsmPortSerialTxClockPol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsmPortSerialTxClockPol.setStatus("mandatory")


class _WsmPortFunctionType_Type(Integer32):
    """Custom type wsmPortFunctionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cbrType", 3),
          ("cellType", 2),
          ("frameType", 1))
    )


_WsmPortFunctionType_Type.__name__ = "Integer32"
_WsmPortFunctionType_Object = MibTableColumn
wsmPortFunctionType = _WsmPortFunctionType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 7),
    _WsmPortFunctionType_Type()
)
wsmPortFunctionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsmPortFunctionType.setStatus("mandatory")


class _WsmPortProtocol_Type(Integer32):
    """Custom type wsmPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 2),
          ("none", 1),
          ("ppp", 3))
    )


_WsmPortProtocol_Type.__name__ = "Integer32"
_WsmPortProtocol_Object = MibTableColumn
wsmPortProtocol = _WsmPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 8),
    _WsmPortProtocol_Type()
)
wsmPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsmPortProtocol.setStatus("mandatory")
_WsmPortIfIndex_Type = Integer32
_WsmPortIfIndex_Object = MibTableColumn
wsmPortIfIndex = _WsmPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 9),
    _WsmPortIfIndex_Type()
)
wsmPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsmPortIfIndex.setStatus("mandatory")


class _WsmPortT1E1StartingTimeSlot_Type(Integer32):
    """Custom type wsmPortT1E1StartingTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WsmPortT1E1StartingTimeSlot_Type.__name__ = "Integer32"
_WsmPortT1E1StartingTimeSlot_Object = MibTableColumn
wsmPortT1E1StartingTimeSlot = _WsmPortT1E1StartingTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 10),
    _WsmPortT1E1StartingTimeSlot_Type()
)
wsmPortT1E1StartingTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsmPortT1E1StartingTimeSlot.setStatus("mandatory")


class _WsmPortT1E1NumberOfTimeSlot_Type(Integer32):
    """Custom type wsmPortT1E1NumberOfTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WsmPortT1E1NumberOfTimeSlot_Type.__name__ = "Integer32"
_WsmPortT1E1NumberOfTimeSlot_Object = MibTableColumn
wsmPortT1E1NumberOfTimeSlot = _WsmPortT1E1NumberOfTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 1, 1, 1, 11),
    _WsmPortT1E1NumberOfTimeSlot_Type()
)
wsmPortT1E1NumberOfTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsmPortT1E1NumberOfTimeSlot.setStatus("mandatory")
_WsmLinkGroup_ObjectIdentity = ObjectIdentity
wsmLinkGroup = _WsmLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2)
)
_LinkxTable_Object = MibTable
linkxTable = _LinkxTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    linkxTable.setStatus("mandatory")
_LinkxEntry_Object = MibTableRow
linkxEntry = _LinkxEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2, 1, 1)
)
linkxEntry.setIndexNames(
    (0, "XYLAN-WSM-MIB", "linkxPeerID"),
    (0, "XYLAN-WSM-MIB", "linkxIfIndex"),
)
if mibBuilder.loadTexts:
    linkxEntry.setStatus("mandatory")
_LinkxPeerID_Type = Integer32
_LinkxPeerID_Object = MibTableColumn
linkxPeerID = _LinkxPeerID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2, 1, 1, 1),
    _LinkxPeerID_Type()
)
linkxPeerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkxPeerID.setStatus("mandatory")
_LinkxIfIndex_Type = Integer32
_LinkxIfIndex_Object = MibTableColumn
linkxIfIndex = _LinkxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2, 1, 1, 2),
    _LinkxIfIndex_Type()
)
linkxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkxIfIndex.setStatus("mandatory")


class _LinkxDescription_Type(DisplayString):
    """Custom type linkxDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LinkxDescription_Type.__name__ = "DisplayString"
_LinkxDescription_Object = MibTableColumn
linkxDescription = _LinkxDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2, 1, 1, 3),
    _LinkxDescription_Type()
)
linkxDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkxDescription.setStatus("mandatory")


class _LinkxAdminStatus_Type(Integer32):
    """Custom type linkxAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_LinkxAdminStatus_Type.__name__ = "Integer32"
_LinkxAdminStatus_Object = MibTableColumn
linkxAdminStatus = _LinkxAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2, 1, 1, 4),
    _LinkxAdminStatus_Type()
)
linkxAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkxAdminStatus.setStatus("mandatory")


class _LinkxType_Type(Integer32):
    """Custom type linkxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isdnCall", 2),
          ("wsmPort", 1))
    )


_LinkxType_Type.__name__ = "Integer32"
_LinkxType_Object = MibTableColumn
linkxType = _LinkxType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2, 1, 1, 5),
    _LinkxType_Type()
)
linkxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkxType.setStatus("mandatory")


class _LinkxSlot_Type(Integer32):
    """Custom type linkxSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_LinkxSlot_Type.__name__ = "Integer32"
_LinkxSlot_Object = MibTableColumn
linkxSlot = _LinkxSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2, 1, 1, 6),
    _LinkxSlot_Type()
)
linkxSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkxSlot.setStatus("mandatory")


class _LinkxPort_Type(Integer32):
    """Custom type linkxPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_LinkxPort_Type.__name__ = "Integer32"
_LinkxPort_Object = MibTableColumn
linkxPort = _LinkxPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2, 1, 1, 7),
    _LinkxPort_Type()
)
linkxPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkxPort.setStatus("mandatory")


class _LinkxMode_Type(Integer32):
    """Custom type linkxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("ondemand", 1))
    )


_LinkxMode_Type.__name__ = "Integer32"
_LinkxMode_Object = MibTableColumn
linkxMode = _LinkxMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 7, 2, 1, 1, 8),
    _LinkxMode_Type()
)
linkxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkxMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-WSM-MIB",
    **{"wsmPortGroup": wsmPortGroup,
       "wsmPortTable": wsmPortTable,
       "wsmPortEntry": wsmPortEntry,
       "wsmPortSlotIndex": wsmPortSlotIndex,
       "wsmPortPortIndex": wsmPortPortIndex,
       "wsmPortInterfaceType": wsmPortInterfaceType,
       "wsmPortCableType": wsmPortCableType,
       "wsmPortSerialRxClockPol": wsmPortSerialRxClockPol,
       "wsmPortSerialTxClockPol": wsmPortSerialTxClockPol,
       "wsmPortFunctionType": wsmPortFunctionType,
       "wsmPortProtocol": wsmPortProtocol,
       "wsmPortIfIndex": wsmPortIfIndex,
       "wsmPortT1E1StartingTimeSlot": wsmPortT1E1StartingTimeSlot,
       "wsmPortT1E1NumberOfTimeSlot": wsmPortT1E1NumberOfTimeSlot,
       "wsmLinkGroup": wsmLinkGroup,
       "linkxTable": linkxTable,
       "linkxEntry": linkxEntry,
       "linkxPeerID": linkxPeerID,
       "linkxIfIndex": linkxIfIndex,
       "linkxDescription": linkxDescription,
       "linkxAdminStatus": linkxAdminStatus,
       "linkxType": linkxType,
       "linkxSlot": linkxSlot,
       "linkxPort": linkxPort,
       "linkxMode": linkxMode}
)
