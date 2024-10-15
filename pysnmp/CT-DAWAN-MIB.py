# SNMP MIB module (CT-DAWAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-DAWAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:04 2024
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class TimeStamp(TimeTicks):
    """Custom type TimeStamp based on TimeTicks"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtSSA_ObjectIdentity = ObjectIdentity
ctSSA = _CtSSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497)
)
_CtDAWanDevices_ObjectIdentity = ObjectIdentity
ctDAWanDevices = _CtDAWanDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16)
)
_CtDAWanDeviceNumDevices_Type = Integer32
_CtDAWanDeviceNumDevices_Object = MibScalar
ctDAWanDeviceNumDevices = _CtDAWanDeviceNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 1),
    _CtDAWanDeviceNumDevices_Type()
)
ctDAWanDeviceNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceNumDevices.setStatus("mandatory")
_CtDAWanDevicesTable_Object = MibTable
ctDAWanDevicesTable = _CtDAWanDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2)
)
if mibBuilder.loadTexts:
    ctDAWanDevicesTable.setStatus("mandatory")
_CtDAWanDeviceEntry_Object = MibTableRow
ctDAWanDeviceEntry = _CtDAWanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1)
)
ctDAWanDeviceEntry.setIndexNames(
    (0, "CT-DAWAN-MIB", "ctDAWanDeviceIndex"),
)
if mibBuilder.loadTexts:
    ctDAWanDeviceEntry.setStatus("mandatory")


class _CtDAWanDeviceIndex_Type(Integer32):
    """Custom type ctDAWanDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtDAWanDeviceIndex_Type.__name__ = "Integer32"
_CtDAWanDeviceIndex_Object = MibTableColumn
ctDAWanDeviceIndex = _CtDAWanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 1),
    _CtDAWanDeviceIndex_Type()
)
ctDAWanDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceIndex.setStatus("mandatory")
_CtDAWanDeviceIfIndex_Type = Integer32
_CtDAWanDeviceIfIndex_Object = MibTableColumn
ctDAWanDeviceIfIndex = _CtDAWanDeviceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 2),
    _CtDAWanDeviceIfIndex_Type()
)
ctDAWanDeviceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceIfIndex.setStatus("mandatory")
_CtDAWanDeviceSessionID_Type = Gauge32
_CtDAWanDeviceSessionID_Object = MibTableColumn
ctDAWanDeviceSessionID = _CtDAWanDeviceSessionID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 3),
    _CtDAWanDeviceSessionID_Type()
)
ctDAWanDeviceSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceSessionID.setStatus("mandatory")


class _CtDAWanDeviceState_Type(Integer32):
    """Custom type ctDAWanDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("connecting", 2),
          ("disconnecting", 4),
          ("inactive", 1))
    )


_CtDAWanDeviceState_Type.__name__ = "Integer32"
_CtDAWanDeviceState_Object = MibTableColumn
ctDAWanDeviceState = _CtDAWanDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 4),
    _CtDAWanDeviceState_Type()
)
ctDAWanDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceState.setStatus("mandatory")


class _CtDAWanDeviceDescr_Type(DisplayString):
    """Custom type ctDAWanDeviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtDAWanDeviceDescr_Type.__name__ = "DisplayString"
_CtDAWanDeviceDescr_Object = MibTableColumn
ctDAWanDeviceDescr = _CtDAWanDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 5),
    _CtDAWanDeviceDescr_Type()
)
ctDAWanDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceDescr.setStatus("mandatory")


class _CtDAWanDeviceConnectControl_Type(Integer32):
    """Custom type ctDAWanDeviceConnectControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("disconnect", 2),
          ("unknown", 3))
    )


_CtDAWanDeviceConnectControl_Type.__name__ = "Integer32"
_CtDAWanDeviceConnectControl_Object = MibTableColumn
ctDAWanDeviceConnectControl = _CtDAWanDeviceConnectControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 6),
    _CtDAWanDeviceConnectControl_Type()
)
ctDAWanDeviceConnectControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDAWanDeviceConnectControl.setStatus("mandatory")


class _CtDAWanDeviceConnectType_Type(Integer32):
    """Custom type ctDAWanDeviceConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analogCircuit", 2),
          ("digitalCircuit", 1))
    )


_CtDAWanDeviceConnectType_Type.__name__ = "Integer32"
_CtDAWanDeviceConnectType_Object = MibTableColumn
ctDAWanDeviceConnectType = _CtDAWanDeviceConnectType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 7),
    _CtDAWanDeviceConnectType_Type()
)
ctDAWanDeviceConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceConnectType.setStatus("mandatory")


class _CtDAWanDeviceL2Encapsulation_Type(Integer32):
    """Custom type ctDAWanDeviceL2Encapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 2),
          ("unknown", 1))
    )


_CtDAWanDeviceL2Encapsulation_Type.__name__ = "Integer32"
_CtDAWanDeviceL2Encapsulation_Object = MibTableColumn
ctDAWanDeviceL2Encapsulation = _CtDAWanDeviceL2Encapsulation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 8),
    _CtDAWanDeviceL2Encapsulation_Type()
)
ctDAWanDeviceL2Encapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceL2Encapsulation.setStatus("mandatory")


class _CtDAWanDeviceNumConnections_Type(Integer32):
    """Custom type ctDAWanDeviceNumConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtDAWanDeviceNumConnections_Type.__name__ = "Integer32"
_CtDAWanDeviceNumConnections_Object = MibTableColumn
ctDAWanDeviceNumConnections = _CtDAWanDeviceNumConnections_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 9),
    _CtDAWanDeviceNumConnections_Type()
)
ctDAWanDeviceNumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceNumConnections.setStatus("mandatory")
_CtDAWanDeviceCurrentBandwidth_Type = Gauge32
_CtDAWanDeviceCurrentBandwidth_Object = MibTableColumn
ctDAWanDeviceCurrentBandwidth = _CtDAWanDeviceCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 10),
    _CtDAWanDeviceCurrentBandwidth_Type()
)
ctDAWanDeviceCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceCurrentBandwidth.setStatus("mandatory")
_CtDAWanDeviceInitialBandwidth_Type = Gauge32
_CtDAWanDeviceInitialBandwidth_Object = MibTableColumn
ctDAWanDeviceInitialBandwidth = _CtDAWanDeviceInitialBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 11),
    _CtDAWanDeviceInitialBandwidth_Type()
)
ctDAWanDeviceInitialBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceInitialBandwidth.setStatus("mandatory")
_CtDAWanDeviceMaxBandwidth_Type = Gauge32
_CtDAWanDeviceMaxBandwidth_Object = MibTableColumn
ctDAWanDeviceMaxBandwidth = _CtDAWanDeviceMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 12),
    _CtDAWanDeviceMaxBandwidth_Type()
)
ctDAWanDeviceMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceMaxBandwidth.setStatus("mandatory")


class _CtDAWanDeviceH0Support_Type(Integer32):
    """Custom type ctDAWanDeviceH0Support based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CtDAWanDeviceH0Support_Type.__name__ = "Integer32"
_CtDAWanDeviceH0Support_Object = MibTableColumn
ctDAWanDeviceH0Support = _CtDAWanDeviceH0Support_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 13),
    _CtDAWanDeviceH0Support_Type()
)
ctDAWanDeviceH0Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceH0Support.setStatus("mandatory")
_CtDAWanDeviceChargedUnits_Type = Gauge32
_CtDAWanDeviceChargedUnits_Object = MibTableColumn
ctDAWanDeviceChargedUnits = _CtDAWanDeviceChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 14),
    _CtDAWanDeviceChargedUnits_Type()
)
ctDAWanDeviceChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceChargedUnits.setStatus("mandatory")
_CtDAWanDeviceSuccessCalls_Type = Gauge32
_CtDAWanDeviceSuccessCalls_Object = MibTableColumn
ctDAWanDeviceSuccessCalls = _CtDAWanDeviceSuccessCalls_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 15),
    _CtDAWanDeviceSuccessCalls_Type()
)
ctDAWanDeviceSuccessCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceSuccessCalls.setStatus("mandatory")
_CtDAWanDeviceFailCalls_Type = Gauge32
_CtDAWanDeviceFailCalls_Object = MibTableColumn
ctDAWanDeviceFailCalls = _CtDAWanDeviceFailCalls_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 16),
    _CtDAWanDeviceFailCalls_Type()
)
ctDAWanDeviceFailCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceFailCalls.setStatus("mandatory")
_CtDAWanDeviceAcceptCalls_Type = Gauge32
_CtDAWanDeviceAcceptCalls_Object = MibTableColumn
ctDAWanDeviceAcceptCalls = _CtDAWanDeviceAcceptCalls_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 17),
    _CtDAWanDeviceAcceptCalls_Type()
)
ctDAWanDeviceAcceptCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceAcceptCalls.setStatus("mandatory")
_CtDAWanDeviceRefuseCalls_Type = Gauge32
_CtDAWanDeviceRefuseCalls_Object = MibTableColumn
ctDAWanDeviceRefuseCalls = _CtDAWanDeviceRefuseCalls_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 18),
    _CtDAWanDeviceRefuseCalls_Type()
)
ctDAWanDeviceRefuseCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceRefuseCalls.setStatus("mandatory")
_CtDAWanDeviceConnectTime_Type = TimeStamp
_CtDAWanDeviceConnectTime_Object = MibTableColumn
ctDAWanDeviceConnectTime = _CtDAWanDeviceConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 19),
    _CtDAWanDeviceConnectTime_Type()
)
ctDAWanDeviceConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceConnectTime.setStatus("mandatory")


class _CtDAWanDeviceConnectDirection_Type(Integer32):
    """Custom type ctDAWanDeviceConnectDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_CtDAWanDeviceConnectDirection_Type.__name__ = "Integer32"
_CtDAWanDeviceConnectDirection_Object = MibTableColumn
ctDAWanDeviceConnectDirection = _CtDAWanDeviceConnectDirection_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 20),
    _CtDAWanDeviceConnectDirection_Type()
)
ctDAWanDeviceConnectDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceConnectDirection.setStatus("mandatory")
_CtDAWanDeviceLastDisconnectTime_Type = TimeStamp
_CtDAWanDeviceLastDisconnectTime_Object = MibTableColumn
ctDAWanDeviceLastDisconnectTime = _CtDAWanDeviceLastDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 21),
    _CtDAWanDeviceLastDisconnectTime_Type()
)
ctDAWanDeviceLastDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceLastDisconnectTime.setStatus("mandatory")


class _CtDAWanDeviceLastDisconnectDirection_Type(Integer32):
    """Custom type ctDAWanDeviceLastDisconnectDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_CtDAWanDeviceLastDisconnectDirection_Type.__name__ = "Integer32"
_CtDAWanDeviceLastDisconnectDirection_Object = MibTableColumn
ctDAWanDeviceLastDisconnectDirection = _CtDAWanDeviceLastDisconnectDirection_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 22),
    _CtDAWanDeviceLastDisconnectDirection_Type()
)
ctDAWanDeviceLastDisconnectDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceLastDisconnectDirection.setStatus("mandatory")


class _CtDAWanDeviceLastDisconnectCause_Type(OctetString):
    """Custom type ctDAWanDeviceLastDisconnectCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CtDAWanDeviceLastDisconnectCause_Type.__name__ = "OctetString"
_CtDAWanDeviceLastDisconnectCause_Object = MibTableColumn
ctDAWanDeviceLastDisconnectCause = _CtDAWanDeviceLastDisconnectCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 23),
    _CtDAWanDeviceLastDisconnectCause_Type()
)
ctDAWanDeviceLastDisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceLastDisconnectCause.setStatus("mandatory")


class _CtDAWanDeviceLastDisconnectText_Type(DisplayString):
    """Custom type ctDAWanDeviceLastDisconnectText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtDAWanDeviceLastDisconnectText_Type.__name__ = "DisplayString"
_CtDAWanDeviceLastDisconnectText_Object = MibTableColumn
ctDAWanDeviceLastDisconnectText = _CtDAWanDeviceLastDisconnectText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 2, 1, 24),
    _CtDAWanDeviceLastDisconnectText_Type()
)
ctDAWanDeviceLastDisconnectText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanDeviceLastDisconnectText.setStatus("mandatory")
_CtDAWanTNListTable_Object = MibTable
ctDAWanTNListTable = _CtDAWanTNListTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 3)
)
if mibBuilder.loadTexts:
    ctDAWanTNListTable.setStatus("mandatory")
_CtDAWanTNListEntry_Object = MibTableRow
ctDAWanTNListEntry = _CtDAWanTNListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 3, 1)
)
ctDAWanTNListEntry.setIndexNames(
    (0, "CT-DAWAN-MIB", "ctDAWanDeviceIndex"),
    (0, "CT-DAWAN-MIB", "ctDAWanTNListIndex"),
)
if mibBuilder.loadTexts:
    ctDAWanTNListEntry.setStatus("mandatory")


class _CtDAWanTNListIndex_Type(Integer32):
    """Custom type ctDAWanTNListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtDAWanTNListIndex_Type.__name__ = "Integer32"
_CtDAWanTNListIndex_Object = MibTableColumn
ctDAWanTNListIndex = _CtDAWanTNListIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 3, 1, 1),
    _CtDAWanTNListIndex_Type()
)
ctDAWanTNListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanTNListIndex.setStatus("mandatory")


class _CtDAWanTN_Type(DisplayString):
    """Custom type ctDAWanTN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtDAWanTN_Type.__name__ = "DisplayString"
_CtDAWanTN_Object = MibTableColumn
ctDAWanTN = _CtDAWanTN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 16, 3, 1, 2),
    _CtDAWanTN_Type()
)
ctDAWanTN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDAWanTN.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-DAWAN-MIB",
    **{"DisplayString": DisplayString,
       "TimeStamp": TimeStamp,
       "ctSSA": ctSSA,
       "ctDAWanDevices": ctDAWanDevices,
       "ctDAWanDeviceNumDevices": ctDAWanDeviceNumDevices,
       "ctDAWanDevicesTable": ctDAWanDevicesTable,
       "ctDAWanDeviceEntry": ctDAWanDeviceEntry,
       "ctDAWanDeviceIndex": ctDAWanDeviceIndex,
       "ctDAWanDeviceIfIndex": ctDAWanDeviceIfIndex,
       "ctDAWanDeviceSessionID": ctDAWanDeviceSessionID,
       "ctDAWanDeviceState": ctDAWanDeviceState,
       "ctDAWanDeviceDescr": ctDAWanDeviceDescr,
       "ctDAWanDeviceConnectControl": ctDAWanDeviceConnectControl,
       "ctDAWanDeviceConnectType": ctDAWanDeviceConnectType,
       "ctDAWanDeviceL2Encapsulation": ctDAWanDeviceL2Encapsulation,
       "ctDAWanDeviceNumConnections": ctDAWanDeviceNumConnections,
       "ctDAWanDeviceCurrentBandwidth": ctDAWanDeviceCurrentBandwidth,
       "ctDAWanDeviceInitialBandwidth": ctDAWanDeviceInitialBandwidth,
       "ctDAWanDeviceMaxBandwidth": ctDAWanDeviceMaxBandwidth,
       "ctDAWanDeviceH0Support": ctDAWanDeviceH0Support,
       "ctDAWanDeviceChargedUnits": ctDAWanDeviceChargedUnits,
       "ctDAWanDeviceSuccessCalls": ctDAWanDeviceSuccessCalls,
       "ctDAWanDeviceFailCalls": ctDAWanDeviceFailCalls,
       "ctDAWanDeviceAcceptCalls": ctDAWanDeviceAcceptCalls,
       "ctDAWanDeviceRefuseCalls": ctDAWanDeviceRefuseCalls,
       "ctDAWanDeviceConnectTime": ctDAWanDeviceConnectTime,
       "ctDAWanDeviceConnectDirection": ctDAWanDeviceConnectDirection,
       "ctDAWanDeviceLastDisconnectTime": ctDAWanDeviceLastDisconnectTime,
       "ctDAWanDeviceLastDisconnectDirection": ctDAWanDeviceLastDisconnectDirection,
       "ctDAWanDeviceLastDisconnectCause": ctDAWanDeviceLastDisconnectCause,
       "ctDAWanDeviceLastDisconnectText": ctDAWanDeviceLastDisconnectText,
       "ctDAWanTNListTable": ctDAWanTNListTable,
       "ctDAWanTNListEntry": ctDAWanTNListEntry,
       "ctDAWanTNListIndex": ctDAWanTNListIndex,
       "ctDAWanTN": ctDAWanTN}
)
