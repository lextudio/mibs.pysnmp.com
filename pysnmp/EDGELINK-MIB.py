# SNMP MIB module (EDGELINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EDGELINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:34 2024
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
 ObjectName,
 ObjectSyntax,
 NotificationType,
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
    "ObjectName",
    "ObjectSyntax",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Telco_ObjectIdentity = ObjectIdentity
telco = _Telco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564)
)
_EdgeLink_ObjectIdentity = ObjectIdentity
edgeLink = _EdgeLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101)
)
_ElM13v1_ObjectIdentity = ObjectIdentity
elM13v1 = _ElM13v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1)
)
_ElDS1CM_ObjectIdentity = ObjectIdentity
elDS1CM = _ElDS1CM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1)
)
_ElDS1CMTable_Object = MibTable
elDS1CMTable = _ElDS1CMTable_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1)
)
if mibBuilder.loadTexts:
    elDS1CMTable.setStatus("mandatory")
_ElDS1CMEntry_Object = MibTableRow
elDS1CMEntry = _ElDS1CMEntry_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1)
)
elDS1CMEntry.setIndexNames(
    (0, "EDGELINK-MIB", "elDS1CMChannelNumber"),
)
if mibBuilder.loadTexts:
    elDS1CMEntry.setStatus("mandatory")


class _ElDS1CMChannelNumber_Type(Integer32):
    """Custom type elDS1CMChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_ElDS1CMChannelNumber_Type.__name__ = "Integer32"
_ElDS1CMChannelNumber_Object = MibTableColumn
elDS1CMChannelNumber = _ElDS1CMChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 1),
    _ElDS1CMChannelNumber_Type()
)
elDS1CMChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1CMChannelNumber.setStatus("mandatory")


class _ElDS1CMLineCode_Type(Integer32):
    """Custom type elDS1CMLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ds1LineCodeAMI", 0),
          ("ds1LineCodeB8ZS", 1))
    )


_ElDS1CMLineCode_Type.__name__ = "Integer32"
_ElDS1CMLineCode_Object = MibTableColumn
elDS1CMLineCode = _ElDS1CMLineCode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 2),
    _ElDS1CMLineCode_Type()
)
elDS1CMLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elDS1CMLineCode.setStatus("mandatory")


class _ElDS1CMLineBuildout_Type(Integer32):
    """Custom type elDS1CMLineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ds1LineBuildout0to133ft", 0),
          ("ds1LineBuildout133to266ft", 1),
          ("ds1LineBuildout266to399ft", 2),
          ("ds1LineBuildout399to533ft", 3),
          ("ds1LineBuildout533to655ft", 4))
    )


_ElDS1CMLineBuildout_Type.__name__ = "Integer32"
_ElDS1CMLineBuildout_Object = MibTableColumn
elDS1CMLineBuildout = _ElDS1CMLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 3),
    _ElDS1CMLineBuildout_Type()
)
elDS1CMLineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elDS1CMLineBuildout.setStatus("mandatory")


class _ElDS1CMLoopbackMode_Type(Integer32):
    """Custom type elDS1CMLoopbackMode based on Integer32"""
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
        *(("ds1LpbkFacility", 3),
          ("ds1LpbkNone", 1),
          ("ds1LpbkRemoteTerminal", 4),
          ("ds1LpbkTerminal", 2))
    )


_ElDS1CMLoopbackMode_Type.__name__ = "Integer32"
_ElDS1CMLoopbackMode_Object = MibTableColumn
elDS1CMLoopbackMode = _ElDS1CMLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 4),
    _ElDS1CMLoopbackMode_Type()
)
elDS1CMLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elDS1CMLoopbackMode.setStatus("mandatory")


class _ElDS1CMServiceMode_Type(Integer32):
    """Custom type elDS1CMServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ds1SetInService", 1),
          ("ds1SetOutOfService", 0))
    )


_ElDS1CMServiceMode_Type.__name__ = "Integer32"
_ElDS1CMServiceMode_Object = MibTableColumn
elDS1CMServiceMode = _ElDS1CMServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 5),
    _ElDS1CMServiceMode_Type()
)
elDS1CMServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elDS1CMServiceMode.setStatus("mandatory")


class _ElDS1CMInterfaceEquipped_Type(Integer32):
    """Custom type elDS1CMInterfaceEquipped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1Disable", 3),
          ("ds1Equipped", 0),
          ("ds1Unequipped", 1))
    )


_ElDS1CMInterfaceEquipped_Type.__name__ = "Integer32"
_ElDS1CMInterfaceEquipped_Object = MibTableColumn
elDS1CMInterfaceEquipped = _ElDS1CMInterfaceEquipped_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 6),
    _ElDS1CMInterfaceEquipped_Type()
)
elDS1CMInterfaceEquipped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elDS1CMInterfaceEquipped.setStatus("mandatory")
_ElDS1CMChannelName_Type = DisplayString
_ElDS1CMChannelName_Object = MibTableColumn
elDS1CMChannelName = _ElDS1CMChannelName_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 7),
    _ElDS1CMChannelName_Type()
)
elDS1CMChannelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elDS1CMChannelName.setStatus("mandatory")


class _ElDS1CMInputStatus_Type(Integer32):
    """Custom type elDS1CMInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ds1InputPresent", 0),
          ("ds1NoInputpresent", 1))
    )


_ElDS1CMInputStatus_Type.__name__ = "Integer32"
_ElDS1CMInputStatus_Object = MibTableColumn
elDS1CMInputStatus = _ElDS1CMInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 8),
    _ElDS1CMInputStatus_Type()
)
elDS1CMInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1CMInputStatus.setStatus("mandatory")


class _ElDS1CMMaskState_Type(Integer32):
    """Custom type elDS1CMMaskState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ds1AlarmedState", 7),
          ("ds1DisabledState", 8),
          ("ds1InputInit", 1),
          ("ds1MonitorActivated", 4),
          ("ds1StatusReported", 6),
          ("ds1TimerRunning", 3),
          ("ds1UnEquipped", 5),
          ("ds1WaitingForInput", 2))
    )


_ElDS1CMMaskState_Type.__name__ = "Integer32"
_ElDS1CMMaskState_Object = MibTableColumn
elDS1CMMaskState = _ElDS1CMMaskState_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 9),
    _ElDS1CMMaskState_Type()
)
elDS1CMMaskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1CMMaskState.setStatus("mandatory")


class _ElDS1CMInterfaceRescan_Type(Integer32):
    """Custom type elDS1CMInterfaceRescan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1AllChannelsAutoSenseDisable", 2),
          ("ds1AllChannelsAutoSenseEnable", 1),
          ("ds1ChannelRescan", 3))
    )


_ElDS1CMInterfaceRescan_Type.__name__ = "Integer32"
_ElDS1CMInterfaceRescan_Object = MibTableColumn
elDS1CMInterfaceRescan = _ElDS1CMInterfaceRescan_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 1, 1, 10),
    _ElDS1CMInterfaceRescan_Type()
)
elDS1CMInterfaceRescan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elDS1CMInterfaceRescan.setStatus("mandatory")


class _ElALLDS1CMLineCode_Type(Integer32):
    """Custom type elALLDS1CMLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1LineCodeAMI", 0),
          ("ds1LineCodeB8ZS", 1),
          ("indeterminate", 2))
    )


_ElALLDS1CMLineCode_Type.__name__ = "Integer32"
_ElALLDS1CMLineCode_Object = MibScalar
elALLDS1CMLineCode = _ElALLDS1CMLineCode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 2),
    _ElALLDS1CMLineCode_Type()
)
elALLDS1CMLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elALLDS1CMLineCode.setStatus("mandatory")


class _ElALLDS1CMLineBuildout_Type(Integer32):
    """Custom type elALLDS1CMLineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ds1LineBuildout0to133ft", 0),
          ("ds1LineBuildout133to266ft", 1),
          ("ds1LineBuildout266to399ft", 2),
          ("ds1LineBuildout399to533ft", 3),
          ("ds1LineBuildout533to655ft", 4),
          ("indeterminate", 5))
    )


_ElALLDS1CMLineBuildout_Type.__name__ = "Integer32"
_ElALLDS1CMLineBuildout_Object = MibScalar
elALLDS1CMLineBuildout = _ElALLDS1CMLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 3),
    _ElALLDS1CMLineBuildout_Type()
)
elALLDS1CMLineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elALLDS1CMLineBuildout.setStatus("mandatory")


class _ElALLDS1CMLoopbackMode_Type(Integer32):
    """Custom type elALLDS1CMLoopbackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ds1LpbkFacility", 3),
          ("ds1LpbkNone", 1),
          ("ds1LpbkRemoteTerminal", 4),
          ("ds1LpbkTerminal", 2),
          ("indeterminate", 5))
    )


_ElALLDS1CMLoopbackMode_Type.__name__ = "Integer32"
_ElALLDS1CMLoopbackMode_Object = MibScalar
elALLDS1CMLoopbackMode = _ElALLDS1CMLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 4),
    _ElALLDS1CMLoopbackMode_Type()
)
elALLDS1CMLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elALLDS1CMLoopbackMode.setStatus("mandatory")


class _ElALLDS1CMServiceMode_Type(Integer32):
    """Custom type elALLDS1CMServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1SetInService", 1),
          ("ds1SetOutOfService", 0),
          ("indeterminate", 2))
    )


_ElALLDS1CMServiceMode_Type.__name__ = "Integer32"
_ElALLDS1CMServiceMode_Object = MibScalar
elALLDS1CMServiceMode = _ElALLDS1CMServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 5),
    _ElALLDS1CMServiceMode_Type()
)
elALLDS1CMServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elALLDS1CMServiceMode.setStatus("mandatory")


class _ElALLDS1CMInterfaceEquipped_Type(Integer32):
    """Custom type elALLDS1CMInterfaceEquipped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1Equipped", 0),
          ("ds1Unequipped", 1),
          ("indeterminate", 2))
    )


_ElALLDS1CMInterfaceEquipped_Type.__name__ = "Integer32"
_ElALLDS1CMInterfaceEquipped_Object = MibScalar
elALLDS1CMInterfaceEquipped = _ElALLDS1CMInterfaceEquipped_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 1, 6),
    _ElALLDS1CMInterfaceEquipped_Type()
)
elALLDS1CMInterfaceEquipped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elALLDS1CMInterfaceEquipped.setStatus("mandatory")
_ElCM_ObjectIdentity = ObjectIdentity
elCM = _ElCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2)
)
_ElCMSystemStatus_Type = DisplayString
_ElCMSystemStatus_Object = MibScalar
elCMSystemStatus = _ElCMSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 1),
    _ElCMSystemStatus_Type()
)
elCMSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elCMSystemStatus.setStatus("mandatory")


class _ElCMDS3ParityMode_Type(Integer32):
    """Custom type elCMDS3ParityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ds3cBitParityMode", 4),
          ("ds3pBitParityMode", 2))
    )


_ElCMDS3ParityMode_Type.__name__ = "Integer32"
_ElCMDS3ParityMode_Object = MibScalar
elCMDS3ParityMode = _ElCMDS3ParityMode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 2),
    _ElCMDS3ParityMode_Type()
)
elCMDS3ParityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMDS3ParityMode.setStatus("mandatory")


class _ElCMDS3LineBuildout_Type(Integer32):
    """Custom type elCMDS3LineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3LineBuildout0to100ft", 0),
          ("ds3LineBuildout100to200ft", 1),
          ("ds3LineBuildout200to450ft", 2))
    )


_ElCMDS3LineBuildout_Type.__name__ = "Integer32"
_ElCMDS3LineBuildout_Object = MibScalar
elCMDS3LineBuildout = _ElCMDS3LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 3),
    _ElCMDS3LineBuildout_Type()
)
elCMDS3LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMDS3LineBuildout.setStatus("mandatory")


class _ElCMDS3TxTiming_Type(Integer32):
    """Custom type elCMDS3TxTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3TxTimingLocal", 2),
          ("ds3TxTimingLooped", 1))
    )


_ElCMDS3TxTiming_Type.__name__ = "Integer32"
_ElCMDS3TxTiming_Object = MibScalar
elCMDS3TxTiming = _ElCMDS3TxTiming_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 4),
    _ElCMDS3TxTiming_Type()
)
elCMDS3TxTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMDS3TxTiming.setStatus("mandatory")


class _ElCMProtectionMode_Type(Integer32):
    """Custom type elCMProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protModeProtected", 0),
          ("protModeUnprotected", 1))
    )


_ElCMProtectionMode_Type.__name__ = "Integer32"
_ElCMProtectionMode_Object = MibScalar
elCMProtectionMode = _ElCMProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 5),
    _ElCMProtectionMode_Type()
)
elCMProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMProtectionMode.setStatus("mandatory")


class _ElCMCardSelect_Type(Integer32):
    """Custom type elCMCardSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cardAOnline", 0),
          ("cardBOnline", 1))
    )


_ElCMCardSelect_Type.__name__ = "Integer32"
_ElCMCardSelect_Object = MibScalar
elCMCardSelect = _ElCMCardSelect_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 6),
    _ElCMCardSelect_Type()
)
elCMCardSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMCardSelect.setStatus("mandatory")


class _ElCMClearTooManySwitches_Type(Integer32):
    """Custom type elCMClearTooManySwitches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearTooManySwitchesLock", 2),
          ("indeterminate", 1))
    )


_ElCMClearTooManySwitches_Type.__name__ = "Integer32"
_ElCMClearTooManySwitches_Object = MibScalar
elCMClearTooManySwitches = _ElCMClearTooManySwitches_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 7),
    _ElCMClearTooManySwitches_Type()
)
elCMClearTooManySwitches.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMClearTooManySwitches.setStatus("mandatory")


class _ElCMDS3LoopbackMode_Type(Integer32):
    """Custom type elCMDS3LoopbackMode based on Integer32"""
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
        *(("ds3LpbkFacility", 3),
          ("ds3LpbkNone", 1),
          ("ds3LpbkRemoteFacility", 4),
          ("ds3LpbkTerminal", 2))
    )


_ElCMDS3LoopbackMode_Type.__name__ = "Integer32"
_ElCMDS3LoopbackMode_Object = MibScalar
elCMDS3LoopbackMode = _ElCMDS3LoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 8),
    _ElCMDS3LoopbackMode_Type()
)
elCMDS3LoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMDS3LoopbackMode.setStatus("mandatory")


class _ElCMDS3ServiceMode_Type(Integer32):
    """Custom type elCMDS3ServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ds3SetInService", 1),
          ("ds3SetOutOfService", 0))
    )


_ElCMDS3ServiceMode_Type.__name__ = "Integer32"
_ElCMDS3ServiceMode_Object = MibScalar
elCMDS3ServiceMode = _ElCMDS3ServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 9),
    _ElCMDS3ServiceMode_Type()
)
elCMDS3ServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMDS3ServiceMode.setStatus("mandatory")
_ElCMCurTimeDate_Type = DisplayString
_ElCMCurTimeDate_Object = MibScalar
elCMCurTimeDate = _ElCMCurTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 10),
    _ElCMCurTimeDate_Type()
)
elCMCurTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMCurTimeDate.setStatus("mandatory")


class _ElCMBerThreshold_Type(Integer32):
    """Custom type elCMBerThreshold based on Integer32"""
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
        *(("ds3BerThreshold10-6", 1),
          ("ds3BerThreshold10-7", 2),
          ("ds3BerThreshold10-8", 3),
          ("ds3BerThreshold10-9", 4))
    )


_ElCMBerThreshold_Type.__name__ = "Integer32"
_ElCMBerThreshold_Object = MibScalar
elCMBerThreshold = _ElCMBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 11),
    _ElCMBerThreshold_Type()
)
elCMBerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMBerThreshold.setStatus("mandatory")


class _ElCMSystemInfo_Type(DisplayString):
    """Custom type elCMSystemInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ElCMSystemInfo_Type.__name__ = "DisplayString"
_ElCMSystemInfo_Object = MibScalar
elCMSystemInfo = _ElCMSystemInfo_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 12),
    _ElCMSystemInfo_Type()
)
elCMSystemInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elCMSystemInfo.setStatus("mandatory")


class _ElCMPPPPortBaudRate_Type(Integer32):
    """Custom type elCMPPPPortBaudRate based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("baud115200", 11),
          ("baud1200", 2),
          ("baud14400", 6),
          ("baud19200", 7),
          ("baud2400", 3),
          ("baud28800", 8),
          ("baud300", 1),
          ("baud38400", 9),
          ("baud4800", 4),
          ("baud57600", 10),
          ("baud9600", 5))
    )


_ElCMPPPPortBaudRate_Type.__name__ = "Integer32"
_ElCMPPPPortBaudRate_Object = MibScalar
elCMPPPPortBaudRate = _ElCMPPPPortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 2, 13),
    _ElCMPPPPortBaudRate_Type()
)
elCMPPPPortBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elCMPPPPortBaudRate.setStatus("mandatory")
_ElCMIfc_ObjectIdentity = ObjectIdentity
elCMIfc = _ElCMIfc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3)
)
_ElCMRemoteCBitIPAddress_Type = IpAddress
_ElCMRemoteCBitIPAddress_Object = MibScalar
elCMRemoteCBitIPAddress = _ElCMRemoteCBitIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 1),
    _ElCMRemoteCBitIPAddress_Type()
)
elCMRemoteCBitIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMRemoteCBitIPAddress.setStatus("mandatory")
_ElCMLocalCBitIPAddress_Type = IpAddress
_ElCMLocalCBitIPAddress_Object = MibScalar
elCMLocalCBitIPAddress = _ElCMLocalCBitIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 2),
    _ElCMLocalCBitIPAddress_Type()
)
elCMLocalCBitIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMLocalCBitIPAddress.setStatus("mandatory")
_ElCMCBitIPSubnetMask_Type = IpAddress
_ElCMCBitIPSubnetMask_Object = MibScalar
elCMCBitIPSubnetMask = _ElCMCBitIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 3),
    _ElCMCBitIPSubnetMask_Type()
)
elCMCBitIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMCBitIPSubnetMask.setStatus("mandatory")
_ElCMRemotePPPIPAddress_Type = IpAddress
_ElCMRemotePPPIPAddress_Object = MibScalar
elCMRemotePPPIPAddress = _ElCMRemotePPPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 4),
    _ElCMRemotePPPIPAddress_Type()
)
elCMRemotePPPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMRemotePPPIPAddress.setStatus("mandatory")
_ElCMIfcTable_Object = MibTable
elCMIfcTable = _ElCMIfcTable_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5)
)
if mibBuilder.loadTexts:
    elCMIfcTable.setStatus("mandatory")
_ElCMIfcEntry_Object = MibTableRow
elCMIfcEntry = _ElCMIfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1)
)
elCMIfcEntry.setIndexNames(
    (0, "EDGELINK-MIB", "elCMIfcInterfaceNumber"),
)
if mibBuilder.loadTexts:
    elCMIfcEntry.setStatus("mandatory")


class _ElCMIfcInterfaceNumber_Type(Integer32):
    """Custom type elCMIfcInterfaceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifEthernet", 1),
          ("ifPPP", 2))
    )


_ElCMIfcInterfaceNumber_Type.__name__ = "Integer32"
_ElCMIfcInterfaceNumber_Object = MibTableColumn
elCMIfcInterfaceNumber = _ElCMIfcInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 1),
    _ElCMIfcInterfaceNumber_Type()
)
elCMIfcInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elCMIfcInterfaceNumber.setStatus("mandatory")
_ElCMIfcMyIPAddr_Type = IpAddress
_ElCMIfcMyIPAddr_Object = MibTableColumn
elCMIfcMyIPAddr = _ElCMIfcMyIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 2),
    _ElCMIfcMyIPAddr_Type()
)
elCMIfcMyIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMIfcMyIPAddr.setStatus("mandatory")
_ElCMIfcMyIPSubnetAddrMask_Type = IpAddress
_ElCMIfcMyIPSubnetAddrMask_Object = MibTableColumn
elCMIfcMyIPSubnetAddrMask = _ElCMIfcMyIPSubnetAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 3),
    _ElCMIfcMyIPSubnetAddrMask_Type()
)
elCMIfcMyIPSubnetAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMIfcMyIPSubnetAddrMask.setStatus("mandatory")
_ElCMIfcMyDefaultGatewayAddr_Type = IpAddress
_ElCMIfcMyDefaultGatewayAddr_Object = MibTableColumn
elCMIfcMyDefaultGatewayAddr = _ElCMIfcMyDefaultGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 4),
    _ElCMIfcMyDefaultGatewayAddr_Type()
)
elCMIfcMyDefaultGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMIfcMyDefaultGatewayAddr.setStatus("mandatory")
_ElCMIfcTrapSendAddr1_Type = IpAddress
_ElCMIfcTrapSendAddr1_Object = MibTableColumn
elCMIfcTrapSendAddr1 = _ElCMIfcTrapSendAddr1_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 5),
    _ElCMIfcTrapSendAddr1_Type()
)
elCMIfcTrapSendAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMIfcTrapSendAddr1.setStatus("mandatory")
_ElCMIfcTrapSendAddr2_Type = IpAddress
_ElCMIfcTrapSendAddr2_Object = MibTableColumn
elCMIfcTrapSendAddr2 = _ElCMIfcTrapSendAddr2_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 6),
    _ElCMIfcTrapSendAddr2_Type()
)
elCMIfcTrapSendAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMIfcTrapSendAddr2.setStatus("mandatory")
_ElCMIfcTrapSendAddr3_Type = IpAddress
_ElCMIfcTrapSendAddr3_Object = MibTableColumn
elCMIfcTrapSendAddr3 = _ElCMIfcTrapSendAddr3_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 7),
    _ElCMIfcTrapSendAddr3_Type()
)
elCMIfcTrapSendAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMIfcTrapSendAddr3.setStatus("mandatory")
_ElCMIfcTrapSendAddr4_Type = IpAddress
_ElCMIfcTrapSendAddr4_Object = MibTableColumn
elCMIfcTrapSendAddr4 = _ElCMIfcTrapSendAddr4_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 3, 5, 1, 8),
    _ElCMIfcTrapSendAddr4_Type()
)
elCMIfcTrapSendAddr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elCMIfcTrapSendAddr4.setStatus("mandatory")
_ElPM_ObjectIdentity = ObjectIdentity
elPM = _ElPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 4)
)
_ElPMDS3TotalSwitches_Type = Integer32
_ElPMDS3TotalSwitches_Object = MibScalar
elPMDS3TotalSwitches = _ElPMDS3TotalSwitches_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 4, 1),
    _ElPMDS3TotalSwitches_Type()
)
elPMDS3TotalSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elPMDS3TotalSwitches.setStatus("mandatory")


class _ElPMClearAllPMMetrics_Type(Integer32):
    """Custom type elPMClearAllPMMetrics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearAllPMMetrics", 2),
          ("indeterminate", 1))
    )


_ElPMClearAllPMMetrics_Type.__name__ = "Integer32"
_ElPMClearAllPMMetrics_Object = MibScalar
elPMClearAllPMMetrics = _ElPMClearAllPMMetrics_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 4, 2),
    _ElPMClearAllPMMetrics_Type()
)
elPMClearAllPMMetrics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elPMClearAllPMMetrics.setStatus("mandatory")
_ElDS1PM_ObjectIdentity = ObjectIdentity
elDS1PM = _ElDS1PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 5)
)


class _ElDS1PMTimeElapsed_Type(Integer32):
    """Custom type elDS1PMTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_ElDS1PMTimeElapsed_Type.__name__ = "Integer32"
_ElDS1PMTimeElapsed_Object = MibScalar
elDS1PMTimeElapsed = _ElDS1PMTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 5, 1),
    _ElDS1PMTimeElapsed_Type()
)
elDS1PMTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMTimeElapsed.setStatus("mandatory")


class _ElDS1PMValidIntervals_Type(Integer32):
    """Custom type elDS1PMValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ElDS1PMValidIntervals_Type.__name__ = "Integer32"
_ElDS1PMValidIntervals_Object = MibScalar
elDS1PMValidIntervals = _ElDS1PMValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 5, 2),
    _ElDS1PMValidIntervals_Type()
)
elDS1PMValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMValidIntervals.setStatus("mandatory")
_ElDS1PMCur_ObjectIdentity = ObjectIdentity
elDS1PMCur = _ElDS1PMCur_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 6)
)
_ElDS1PMCurTable_Object = MibTable
elDS1PMCurTable = _ElDS1PMCurTable_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 6, 1)
)
if mibBuilder.loadTexts:
    elDS1PMCurTable.setStatus("mandatory")
_ElDS1PMCurEntry_Object = MibTableRow
elDS1PMCurEntry = _ElDS1PMCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 6, 1, 1)
)
elDS1PMCurEntry.setIndexNames(
    (0, "EDGELINK-MIB", "elDS1PMCurChannelNumber"),
)
if mibBuilder.loadTexts:
    elDS1PMCurEntry.setStatus("mandatory")


class _ElDS1PMCurChannelNumber_Type(Integer32):
    """Custom type elDS1PMCurChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_ElDS1PMCurChannelNumber_Type.__name__ = "Integer32"
_ElDS1PMCurChannelNumber_Object = MibTableColumn
elDS1PMCurChannelNumber = _ElDS1PMCurChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 6, 1, 1, 1),
    _ElDS1PMCurChannelNumber_Type()
)
elDS1PMCurChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMCurChannelNumber.setStatus("mandatory")
_ElDS1PMCurLineCodeViolations_Type = Integer32
_ElDS1PMCurLineCodeViolations_Object = MibTableColumn
elDS1PMCurLineCodeViolations = _ElDS1PMCurLineCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 6, 1, 1, 2),
    _ElDS1PMCurLineCodeViolations_Type()
)
elDS1PMCurLineCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMCurLineCodeViolations.setStatus("mandatory")
_ElDS1PMCurErroredSeconds_Type = Integer32
_ElDS1PMCurErroredSeconds_Object = MibTableColumn
elDS1PMCurErroredSeconds = _ElDS1PMCurErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 6, 1, 1, 3),
    _ElDS1PMCurErroredSeconds_Type()
)
elDS1PMCurErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMCurErroredSeconds.setStatus("mandatory")
_ElDS1PMIvl_ObjectIdentity = ObjectIdentity
elDS1PMIvl = _ElDS1PMIvl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 7)
)
_ElDS1PMIvlTable_Object = MibTable
elDS1PMIvlTable = _ElDS1PMIvlTable_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1)
)
if mibBuilder.loadTexts:
    elDS1PMIvlTable.setStatus("mandatory")
_ElDS1PMIvlEntry_Object = MibTableRow
elDS1PMIvlEntry = _ElDS1PMIvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1, 1)
)
elDS1PMIvlEntry.setIndexNames(
    (0, "EDGELINK-MIB", "elDS1PMIvlChannelNumber"),
    (0, "EDGELINK-MIB", "elDS1PMIvlIntervalNumber"),
)
if mibBuilder.loadTexts:
    elDS1PMIvlEntry.setStatus("mandatory")


class _ElDS1PMIvlChannelNumber_Type(Integer32):
    """Custom type elDS1PMIvlChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_ElDS1PMIvlChannelNumber_Type.__name__ = "Integer32"
_ElDS1PMIvlChannelNumber_Object = MibTableColumn
elDS1PMIvlChannelNumber = _ElDS1PMIvlChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1, 1, 1),
    _ElDS1PMIvlChannelNumber_Type()
)
elDS1PMIvlChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMIvlChannelNumber.setStatus("mandatory")


class _ElDS1PMIvlIntervalNumber_Type(Integer32):
    """Custom type elDS1PMIvlIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ElDS1PMIvlIntervalNumber_Type.__name__ = "Integer32"
_ElDS1PMIvlIntervalNumber_Object = MibTableColumn
elDS1PMIvlIntervalNumber = _ElDS1PMIvlIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1, 1, 2),
    _ElDS1PMIvlIntervalNumber_Type()
)
elDS1PMIvlIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMIvlIntervalNumber.setStatus("mandatory")
_ElDS1PMIvlLineCodeViolations_Type = Integer32
_ElDS1PMIvlLineCodeViolations_Object = MibTableColumn
elDS1PMIvlLineCodeViolations = _ElDS1PMIvlLineCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1, 1, 3),
    _ElDS1PMIvlLineCodeViolations_Type()
)
elDS1PMIvlLineCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMIvlLineCodeViolations.setStatus("mandatory")
_ElDS1PMIvlErroredSeconds_Type = Integer32
_ElDS1PMIvlErroredSeconds_Object = MibTableColumn
elDS1PMIvlErroredSeconds = _ElDS1PMIvlErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 7, 1, 1, 4),
    _ElDS1PMIvlErroredSeconds_Type()
)
elDS1PMIvlErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMIvlErroredSeconds.setStatus("mandatory")
_ElDS1PMTot_ObjectIdentity = ObjectIdentity
elDS1PMTot = _ElDS1PMTot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 8)
)
_ElDS1PMTotTable_Object = MibTable
elDS1PMTotTable = _ElDS1PMTotTable_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 8, 1)
)
if mibBuilder.loadTexts:
    elDS1PMTotTable.setStatus("mandatory")
_ElDS1PMTotEntry_Object = MibTableRow
elDS1PMTotEntry = _ElDS1PMTotEntry_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 8, 1, 1)
)
elDS1PMTotEntry.setIndexNames(
    (0, "EDGELINK-MIB", "elDS1PMTotChannelNumber"),
)
if mibBuilder.loadTexts:
    elDS1PMTotEntry.setStatus("mandatory")


class _ElDS1PMTotChannelNumber_Type(Integer32):
    """Custom type elDS1PMTotChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_ElDS1PMTotChannelNumber_Type.__name__ = "Integer32"
_ElDS1PMTotChannelNumber_Object = MibTableColumn
elDS1PMTotChannelNumber = _ElDS1PMTotChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 8, 1, 1, 1),
    _ElDS1PMTotChannelNumber_Type()
)
elDS1PMTotChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMTotChannelNumber.setStatus("mandatory")
_ElDS1PMTotLineCodeViolations_Type = Integer32
_ElDS1PMTotLineCodeViolations_Object = MibTableColumn
elDS1PMTotLineCodeViolations = _ElDS1PMTotLineCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 8, 1, 1, 2),
    _ElDS1PMTotLineCodeViolations_Type()
)
elDS1PMTotLineCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMTotLineCodeViolations.setStatus("mandatory")
_ElDS1PMTotErroredSeconds_Type = Integer32
_ElDS1PMTotErroredSeconds_Object = MibTableColumn
elDS1PMTotErroredSeconds = _ElDS1PMTotErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 8, 1, 1, 3),
    _ElDS1PMTotErroredSeconds_Type()
)
elDS1PMTotErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elDS1PMTotErroredSeconds.setStatus("mandatory")
_ElFM_ObjectIdentity = ObjectIdentity
elFM = _ElFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 9)
)


class _ElFMFillAlarmLogTable_Type(Integer32):
    """Custom type elFMFillAlarmLogTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fillAlarmLogTable", 2),
          ("indeterminate", 1))
    )


_ElFMFillAlarmLogTable_Type.__name__ = "Integer32"
_ElFMFillAlarmLogTable_Object = MibScalar
elFMFillAlarmLogTable = _ElFMFillAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 9, 1),
    _ElFMFillAlarmLogTable_Type()
)
elFMFillAlarmLogTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elFMFillAlarmLogTable.setStatus("mandatory")


class _ElFMClearAlarmLog_Type(Integer32):
    """Custom type elFMClearAlarmLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearAlarmLog", 2),
          ("indeterminate", 1))
    )


_ElFMClearAlarmLog_Type.__name__ = "Integer32"
_ElFMClearAlarmLog_Object = MibScalar
elFMClearAlarmLog = _ElFMClearAlarmLog_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 9, 2),
    _ElFMClearAlarmLog_Type()
)
elFMClearAlarmLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elFMClearAlarmLog.setStatus("mandatory")


class _ElFMDS1AutoSenseMode_Type(Integer32):
    """Custom type elFMDS1AutoSenseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableDs1AutoSense", 2),
          ("enableDs1AutoSense", 1),
          ("rescanAllDs1Inputs", 3))
    )


_ElFMDS1AutoSenseMode_Type.__name__ = "Integer32"
_ElFMDS1AutoSenseMode_Object = MibScalar
elFMDS1AutoSenseMode = _ElFMDS1AutoSenseMode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 9, 3),
    _ElFMDS1AutoSenseMode_Type()
)
elFMDS1AutoSenseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elFMDS1AutoSenseMode.setStatus("mandatory")


class _ElFMDS1InputAlarmMode_Type(Integer32):
    """Custom type elFMDS1InputAlarmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnDs1InputLos", 1),
          ("statusOnDs1InputLos", 0))
    )


_ElFMDS1InputAlarmMode_Type.__name__ = "Integer32"
_ElFMDS1InputAlarmMode_Object = MibScalar
elFMDS1InputAlarmMode = _ElFMDS1InputAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 9, 4),
    _ElFMDS1InputAlarmMode_Type()
)
elFMDS1InputAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elFMDS1InputAlarmMode.setStatus("mandatory")
_ElFMAlmLog_ObjectIdentity = ObjectIdentity
elFMAlmLog = _ElFMAlmLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 10)
)
_ElFMAlmLogTable_Object = MibTable
elFMAlmLogTable = _ElFMAlmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1)
)
if mibBuilder.loadTexts:
    elFMAlmLogTable.setStatus("mandatory")
_ElFMAlmLogEntry_Object = MibTableRow
elFMAlmLogEntry = _ElFMAlmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1)
)
elFMAlmLogEntry.setIndexNames(
    (0, "EDGELINK-MIB", "elFMAlmLogEntryNumber"),
)
if mibBuilder.loadTexts:
    elFMAlmLogEntry.setStatus("mandatory")


class _ElFMAlmLogEntryNumber_Type(Integer32):
    """Custom type elFMAlmLogEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ElFMAlmLogEntryNumber_Type.__name__ = "Integer32"
_ElFMAlmLogEntryNumber_Object = MibTableColumn
elFMAlmLogEntryNumber = _ElFMAlmLogEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 1),
    _ElFMAlmLogEntryNumber_Type()
)
elFMAlmLogEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMAlmLogEntryNumber.setStatus("mandatory")
_ElFMAlmLogTableAlarmNumber_Type = Integer32
_ElFMAlmLogTableAlarmNumber_Object = MibTableColumn
elFMAlmLogTableAlarmNumber = _ElFMAlmLogTableAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 2),
    _ElFMAlmLogTableAlarmNumber_Type()
)
elFMAlmLogTableAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMAlmLogTableAlarmNumber.setStatus("mandatory")


class _ElFMAlmLogTableDescription_Type(DisplayString):
    """Custom type elFMAlmLogTableDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ElFMAlmLogTableDescription_Type.__name__ = "DisplayString"
_ElFMAlmLogTableDescription_Object = MibTableColumn
elFMAlmLogTableDescription = _ElFMAlmLogTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 3),
    _ElFMAlmLogTableDescription_Type()
)
elFMAlmLogTableDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMAlmLogTableDescription.setStatus("mandatory")


class _ElFMAlmLogTableStatus_Type(Integer32):
    """Custom type elFMAlmLogTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("set", 1))
    )


_ElFMAlmLogTableStatus_Type.__name__ = "Integer32"
_ElFMAlmLogTableStatus_Object = MibTableColumn
elFMAlmLogTableStatus = _ElFMAlmLogTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 4),
    _ElFMAlmLogTableStatus_Type()
)
elFMAlmLogTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMAlmLogTableStatus.setStatus("mandatory")


class _ElFMAlmLogTableTimestamp_Type(DisplayString):
    """Custom type elFMAlmLogTableTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ElFMAlmLogTableTimestamp_Type.__name__ = "DisplayString"
_ElFMAlmLogTableTimestamp_Object = MibTableColumn
elFMAlmLogTableTimestamp = _ElFMAlmLogTableTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 5),
    _ElFMAlmLogTableTimestamp_Type()
)
elFMAlmLogTableTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMAlmLogTableTimestamp.setStatus("mandatory")
_ElFMAlmLogTableChannel_Type = Integer32
_ElFMAlmLogTableChannel_Object = MibTableColumn
elFMAlmLogTableChannel = _ElFMAlmLogTableChannel_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 10, 1, 1, 6),
    _ElFMAlmLogTableChannel_Type()
)
elFMAlmLogTableChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMAlmLogTableChannel.setStatus("mandatory")
_ElFMCurAlm_ObjectIdentity = ObjectIdentity
elFMCurAlm = _ElFMCurAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 11)
)
_ElFMCurAlmTable_Object = MibTable
elFMCurAlmTable = _ElFMCurAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 11, 1)
)
if mibBuilder.loadTexts:
    elFMCurAlmTable.setStatus("mandatory")
_ElFMCurAlmEntry_Object = MibTableRow
elFMCurAlmEntry = _ElFMCurAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 11, 1, 1)
)
elFMCurAlmEntry.setIndexNames(
    (0, "EDGELINK-MIB", "elFMCurAlmTableAlarmNumber"),
    (0, "EDGELINK-MIB", "elFMCurAlmTableChannel"),
)
if mibBuilder.loadTexts:
    elFMCurAlmEntry.setStatus("mandatory")
_ElFMCurAlmTableAlarmNumber_Type = Integer32
_ElFMCurAlmTableAlarmNumber_Object = MibTableColumn
elFMCurAlmTableAlarmNumber = _ElFMCurAlmTableAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 11, 1, 1, 1),
    _ElFMCurAlmTableAlarmNumber_Type()
)
elFMCurAlmTableAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMCurAlmTableAlarmNumber.setStatus("mandatory")
_ElFMCurAlmTableChannel_Type = Integer32
_ElFMCurAlmTableChannel_Object = MibTableColumn
elFMCurAlmTableChannel = _ElFMCurAlmTableChannel_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 11, 1, 1, 2),
    _ElFMCurAlmTableChannel_Type()
)
elFMCurAlmTableChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMCurAlmTableChannel.setStatus("mandatory")


class _ElFMCurAlmTableDescription_Type(DisplayString):
    """Custom type elFMCurAlmTableDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ElFMCurAlmTableDescription_Type.__name__ = "DisplayString"
_ElFMCurAlmTableDescription_Object = MibTableColumn
elFMCurAlmTableDescription = _ElFMCurAlmTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 11, 1, 1, 3),
    _ElFMCurAlmTableDescription_Type()
)
elFMCurAlmTableDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMCurAlmTableDescription.setStatus("mandatory")
_ElFMTrapFields_ObjectIdentity = ObjectIdentity
elFMTrapFields = _ElFMTrapFields_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 12)
)
_ElFMTrapAlarmNumber_Type = Integer32
_ElFMTrapAlarmNumber_Object = MibScalar
elFMTrapAlarmNumber = _ElFMTrapAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 12, 1),
    _ElFMTrapAlarmNumber_Type()
)
elFMTrapAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMTrapAlarmNumber.setStatus("mandatory")
_ElFMTrapAlarmText_Type = DisplayString
_ElFMTrapAlarmText_Object = MibScalar
elFMTrapAlarmText = _ElFMTrapAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 12, 2),
    _ElFMTrapAlarmText_Type()
)
elFMTrapAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMTrapAlarmText.setStatus("mandatory")
_ElFMTrapTimeStamp_Type = DisplayString
_ElFMTrapTimeStamp_Object = MibScalar
elFMTrapTimeStamp = _ElFMTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 12, 3),
    _ElFMTrapTimeStamp_Type()
)
elFMTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMTrapTimeStamp.setStatus("mandatory")
_ElFMTrapAlarmStatus_Type = Integer32
_ElFMTrapAlarmStatus_Object = MibScalar
elFMTrapAlarmStatus = _ElFMTrapAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 12, 4),
    _ElFMTrapAlarmStatus_Type()
)
elFMTrapAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMTrapAlarmStatus.setStatus("mandatory")
_ElFMTrapChannelNumber_Type = Integer32
_ElFMTrapChannelNumber_Object = MibScalar
elFMTrapChannelNumber = _ElFMTrapChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 12, 5),
    _ElFMTrapChannelNumber_Type()
)
elFMTrapChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elFMTrapChannelNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects

edgeLinkEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 564, 101, 1, 0, 1)
)
edgeLinkEvent.setObjects(
      *(("EDGELINK-MIB", "elFMTrapAlarmNumber"),
        ("EDGELINK-MIB", "elFMTrapAlarmText"),
        ("EDGELINK-MIB", "elFMTrapTimeStamp"),
        ("EDGELINK-MIB", "elFMTrapAlarmStatus"),
        ("EDGELINK-MIB", "elFMTrapChannelNumber"),
        ("EDGELINK-MIB", "elCMSystemStatus"))
)
if mibBuilder.loadTexts:
    edgeLinkEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EDGELINK-MIB",
    **{"telco": telco,
       "edgeLink": edgeLink,
       "elM13v1": elM13v1,
       "edgeLinkEvent": edgeLinkEvent,
       "elDS1CM": elDS1CM,
       "elDS1CMTable": elDS1CMTable,
       "elDS1CMEntry": elDS1CMEntry,
       "elDS1CMChannelNumber": elDS1CMChannelNumber,
       "elDS1CMLineCode": elDS1CMLineCode,
       "elDS1CMLineBuildout": elDS1CMLineBuildout,
       "elDS1CMLoopbackMode": elDS1CMLoopbackMode,
       "elDS1CMServiceMode": elDS1CMServiceMode,
       "elDS1CMInterfaceEquipped": elDS1CMInterfaceEquipped,
       "elDS1CMChannelName": elDS1CMChannelName,
       "elDS1CMInputStatus": elDS1CMInputStatus,
       "elDS1CMMaskState": elDS1CMMaskState,
       "elDS1CMInterfaceRescan": elDS1CMInterfaceRescan,
       "elALLDS1CMLineCode": elALLDS1CMLineCode,
       "elALLDS1CMLineBuildout": elALLDS1CMLineBuildout,
       "elALLDS1CMLoopbackMode": elALLDS1CMLoopbackMode,
       "elALLDS1CMServiceMode": elALLDS1CMServiceMode,
       "elALLDS1CMInterfaceEquipped": elALLDS1CMInterfaceEquipped,
       "elCM": elCM,
       "elCMSystemStatus": elCMSystemStatus,
       "elCMDS3ParityMode": elCMDS3ParityMode,
       "elCMDS3LineBuildout": elCMDS3LineBuildout,
       "elCMDS3TxTiming": elCMDS3TxTiming,
       "elCMProtectionMode": elCMProtectionMode,
       "elCMCardSelect": elCMCardSelect,
       "elCMClearTooManySwitches": elCMClearTooManySwitches,
       "elCMDS3LoopbackMode": elCMDS3LoopbackMode,
       "elCMDS3ServiceMode": elCMDS3ServiceMode,
       "elCMCurTimeDate": elCMCurTimeDate,
       "elCMBerThreshold": elCMBerThreshold,
       "elCMSystemInfo": elCMSystemInfo,
       "elCMPPPPortBaudRate": elCMPPPPortBaudRate,
       "elCMIfc": elCMIfc,
       "elCMRemoteCBitIPAddress": elCMRemoteCBitIPAddress,
       "elCMLocalCBitIPAddress": elCMLocalCBitIPAddress,
       "elCMCBitIPSubnetMask": elCMCBitIPSubnetMask,
       "elCMRemotePPPIPAddress": elCMRemotePPPIPAddress,
       "elCMIfcTable": elCMIfcTable,
       "elCMIfcEntry": elCMIfcEntry,
       "elCMIfcInterfaceNumber": elCMIfcInterfaceNumber,
       "elCMIfcMyIPAddr": elCMIfcMyIPAddr,
       "elCMIfcMyIPSubnetAddrMask": elCMIfcMyIPSubnetAddrMask,
       "elCMIfcMyDefaultGatewayAddr": elCMIfcMyDefaultGatewayAddr,
       "elCMIfcTrapSendAddr1": elCMIfcTrapSendAddr1,
       "elCMIfcTrapSendAddr2": elCMIfcTrapSendAddr2,
       "elCMIfcTrapSendAddr3": elCMIfcTrapSendAddr3,
       "elCMIfcTrapSendAddr4": elCMIfcTrapSendAddr4,
       "elPM": elPM,
       "elPMDS3TotalSwitches": elPMDS3TotalSwitches,
       "elPMClearAllPMMetrics": elPMClearAllPMMetrics,
       "elDS1PM": elDS1PM,
       "elDS1PMTimeElapsed": elDS1PMTimeElapsed,
       "elDS1PMValidIntervals": elDS1PMValidIntervals,
       "elDS1PMCur": elDS1PMCur,
       "elDS1PMCurTable": elDS1PMCurTable,
       "elDS1PMCurEntry": elDS1PMCurEntry,
       "elDS1PMCurChannelNumber": elDS1PMCurChannelNumber,
       "elDS1PMCurLineCodeViolations": elDS1PMCurLineCodeViolations,
       "elDS1PMCurErroredSeconds": elDS1PMCurErroredSeconds,
       "elDS1PMIvl": elDS1PMIvl,
       "elDS1PMIvlTable": elDS1PMIvlTable,
       "elDS1PMIvlEntry": elDS1PMIvlEntry,
       "elDS1PMIvlChannelNumber": elDS1PMIvlChannelNumber,
       "elDS1PMIvlIntervalNumber": elDS1PMIvlIntervalNumber,
       "elDS1PMIvlLineCodeViolations": elDS1PMIvlLineCodeViolations,
       "elDS1PMIvlErroredSeconds": elDS1PMIvlErroredSeconds,
       "elDS1PMTot": elDS1PMTot,
       "elDS1PMTotTable": elDS1PMTotTable,
       "elDS1PMTotEntry": elDS1PMTotEntry,
       "elDS1PMTotChannelNumber": elDS1PMTotChannelNumber,
       "elDS1PMTotLineCodeViolations": elDS1PMTotLineCodeViolations,
       "elDS1PMTotErroredSeconds": elDS1PMTotErroredSeconds,
       "elFM": elFM,
       "elFMFillAlarmLogTable": elFMFillAlarmLogTable,
       "elFMClearAlarmLog": elFMClearAlarmLog,
       "elFMDS1AutoSenseMode": elFMDS1AutoSenseMode,
       "elFMDS1InputAlarmMode": elFMDS1InputAlarmMode,
       "elFMAlmLog": elFMAlmLog,
       "elFMAlmLogTable": elFMAlmLogTable,
       "elFMAlmLogEntry": elFMAlmLogEntry,
       "elFMAlmLogEntryNumber": elFMAlmLogEntryNumber,
       "elFMAlmLogTableAlarmNumber": elFMAlmLogTableAlarmNumber,
       "elFMAlmLogTableDescription": elFMAlmLogTableDescription,
       "elFMAlmLogTableStatus": elFMAlmLogTableStatus,
       "elFMAlmLogTableTimestamp": elFMAlmLogTableTimestamp,
       "elFMAlmLogTableChannel": elFMAlmLogTableChannel,
       "elFMCurAlm": elFMCurAlm,
       "elFMCurAlmTable": elFMCurAlmTable,
       "elFMCurAlmEntry": elFMCurAlmEntry,
       "elFMCurAlmTableAlarmNumber": elFMCurAlmTableAlarmNumber,
       "elFMCurAlmTableChannel": elFMCurAlmTableChannel,
       "elFMCurAlmTableDescription": elFMCurAlmTableDescription,
       "elFMTrapFields": elFMTrapFields,
       "elFMTrapAlarmNumber": elFMTrapAlarmNumber,
       "elFMTrapAlarmText": elFMTrapAlarmText,
       "elFMTrapTimeStamp": elFMTrapTimeStamp,
       "elFMTrapAlarmStatus": elFMTrapAlarmStatus,
       "elFMTrapChannelNumber": elFMTrapChannelNumber}
)
